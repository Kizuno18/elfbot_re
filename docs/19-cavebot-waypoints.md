## Cavebot waypoint loading & format

ElfBot NG 8.60, `elfbot.dll`, imagebase `0x10000000`. All addresses below are file-absolute at that base and match the IDA database names.

The cavebot loader has two entry paths that converge on one in-memory table:

- **Binary path** — `loadCavebotFile(0x10015b79)` reads a `.elfc` file and RLE-decodes it into the config image at `g_101e6ea8`.
- **Text path** — `loadScriptFile(0x100167eb)` -> `parseWaypointsSection(0x10016438)` reads a legacy plain-text route (`.elfa`, `.wpt`) and *appends* waypoint records.

`refreshCavebotDialog(0x100160d6)` is the presentation side; it never parses, it only repaints the GUI list controls from the tables the two loaders populate.

### 1. `loadCavebotFile` (0x10015b79) — path resolution + file read + decode

Signature: `char __stdcall sub_10015B79(_BYTE *a1, int a2)`. `a1` is a name/path, `a2` is a "path is absolute" flag.

Path resolution has three modes:

| Condition | Behavior |
|---|---|
| `a2 != 0` | `a1` is a full path; copy verbatim. |
| `a2 == 0 && *a1 != 0` | Build `PathName + "\Scripts\" + a1 + ".elfc"` (via `aScripts_0`, `aElfc`). |
| `a2 == 0 && *a1 == 0` | Open a `GetOpenFileNameA` dialog (`aCavebotFiles_0` filter, `aSelectACavebot_0` title). Selection lands in `byte_10043198` (a `MAX_PATH` buffer). |

After a dialog pick it sniffs the extension. This test:

```c
v3 = lstrlen(&byte_10043198);
if ( v3 > 5 && (*(int*)((char*)&dword_10043194 + v3) | 0x20202000) == 0x7470772E )
{
    LOBYTE(...) = loadScriptFile(&byte_10043198);   // ".wpt" -> text path
    byte_10043198 = 0;
    return;
}
```

`0x7470772E` is `".wpt"` little-endian; the `| 0x20202000` folds case on the three letters. So a picked `*.wpt` is diverted to the text loader; anything else falls through to the binary loader.

Binary load:

```c
buf = HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, 0x200000);      // 2 MB scratch
hFile = CreateFileA(path, GENERIC_READ, FILE_SHARE_READ, 0, OPEN_EXISTING, FILE_FLAG_SEQUENTIAL_SCAN, 0);
FileSize = GetFileSize(hFile, 0);
ReadFile(hFile, buf, FileSize, &NumberOfBytesWritten, 0);
CloseHandle(hFile);
byte_10207F3A = 0;
decodeRleMapCells(&unk_101E6EA8, 0xA1093, buf);   // sub_10012771: expand into config image
```

`0xA1093` (659,091) is the fixed decompressed size of the whole config image starting at `unk_101E6EA8` — this is not just the waypoint array, it is the entire persisted cavebot state (waypoints + loot + spell/word list + checkbox bytes) laid out contiguously.

**Extra-page migration.** After decode, if the "already migrated" flag `byte_10207F3A` is still 0, it copies the spell/word list out to the script arena:

```c
if ( !byte_10207F3A )
{
    v6 = byte_101F2EA8;                 // source: decoded word-list region
    v7 = byte_10207F3B;                 // dest: 4096-strided script arena
    while ( v6 < byte_10202EA8 )        // walk until end-of-region marker
    {
        memcpyBytes(v7, v6, 0x200);     // 512-byte record
        v6 += 512;
        v7 += 4096;                     // note: 512-in, 4096-out stride expansion
    }
    memsetZero(byte_101F2EA8, 1);
    byte_10207F3A = 1;
}
HeapFree(GetProcessHeap(), 0, buf);
LOBYTE(...) = parseSpellListA();          // sub_10008152: index the word list
```

The stride mismatch (512-byte packed records exploded to 4096-byte slots) is how the compact on-disk spell list is unpacked into the runtime arena that `parseWaypointsSection` later writes `wait`/label strings into (§3, cases 9/10).

### 2. `sub_10012771` — the .elfc RLE decoder (`decodeRleMapCells`)

Signature: `void __stdcall sub_10012771(void *dst, unsigned int size, _DWORD *src)`.

Header gate: if `*src != -352` (i.e. `0xFFFFFFA0`) it is not RLE — just `memcpyBytes(dst, src, size)`. Otherwise `dst` is zeroed and a bytecode stream after the 4-byte header is interpreted. Each opcode's low 6 bits are a *skip* (leave zeroed) count; the top two bits select the write width:

| Opcode `op` | Class | Action |
|---|---|---|
| `op >= 0xC0` | run-skip | `count = ((op & 0x3F) << 8) | src[1]`; advance dst by `count`, consume 2 bytes. Large zero-gap. |
| `0x80..0xBF` | dword | skip `op & 0x3F`, then write a 4-byte value from `src+1`; consume 5 bytes. |
| `0x40..0x7F` | word | skip `op & 0x3F`, then write a 2-byte value; consume 3 bytes. |
| `0x00..0x3F` | byte | skip `op & 0x3F`, then write 1 byte from `src[1]`; a `0` payload byte terminates the stream. |

This is a sparse-image codec: most of the 659 KB image is zero, and the format encodes only the non-zero dword/word/byte cells plus their gaps. That is why the whole config (waypoints, loot, words) round-trips through one call.

### 3. `parseWaypointsSection` (0x10016438) — the `[Waypoints]` text grammar

Signature: `void __stdcall sub_10016438(CHAR *buf, int len)`. This is the grammar for legacy text routes. It is a hand-rolled tokenizer with **four fields per line**, CR and/or LF delimited (handles `\r`, `\n`, and `\r\n`/`\n\r` pairs). Each of the four fields is copied into a 2 KB stack buffer and run through `parseSignedInt_0` (0x10040900):

```
line grammar:  <f1> <sep> <f2> <sep> <f3> <sep> <f4>
  f1 -> v29   (x)
  f2 -> v28   (y)
  f3 -> v27   (z)
  f4 -> v26   (TYPE code, 1..10)
```

Field 4 (`v26`) is the record type. `v26 == 0` skips the line. Table-full guard: `if (dword_10202F06 >= 0x3E6) return;` — the waypoint array holds at most **998** records.

Record allocation and the common header:

```c
v15 = dword_10202F06++;                      // claim slot index
v16 = (char*)&unk_101E6EA8 + 48 * v15;        // 48-byte stride
*(DWORD*)v16       = v29;                      // +0  x
*((DWORD*)v16 + 1) = v28;                      // +4  y
*((DWORD*)v16 + 2) = v27;                      // +8  z
*((WORD*)v16 + 23) = 0;                         // +46 script-slot index = 0
v16[12]            = 0;                          // +12 label/script string = ""
```

**Waypoint record layout (48 bytes, stride `0x30`):**

| Offset | Size | Field | Meaning |
|---|---|---|---|
| +0x00 | dword | `x` | map X |
| +0x04 | dword | `y` | map Y |
| +0x08 | dword | `z` | map Z (floor) |
| +0x0C | 32 B  | `label`/`script` | NUL-terminated string (label name or action text); read via `v16+12` |
| +0x2C | word  | `actionType` | internal action enum (see below) |
| +0x2E | word  | `scriptSlot` | 1-based index into script arena `byte_10207F3B`, or 0 |

Two pre-switch cases (`v26 == 1,2,7`) emit a **paired "approach" record**: they write an internal type 4 (walk) record at the current slot with `z` decremented for type 7, then bump `dword_10202F06` again and start a *second* record at `v16 += 48` with the same coords — so one text line becomes two internal waypoints (walk-up-to + act).

The `switch(v26)` then sets the action type word (+0x2C) and mutates coords. Mapping from **on-disk type code** to **internal actionType**:

| Disk code `v26` | Internal `+0x2C` | Semantics | Coord mutation |
|---|---|---|---|
| 1 | 2 | rope (up) | emits paired walk(4) record first |
| 2 | 3 | ladder / machete-up | paired walk(4); |
| 3 | 4 | (walk variant, N/E) | `y++`; `z++` if `z < 15` |
| 4 | 4 | (walk variant, S/W) | `y--`; `z--` if `z != 0` |
| 5 | 4 | stairs-up-ish | `z--` if `z != 0` |
| 6 | 7 | shovel/rope-hole (down) | none |
| 7 | 6 | ladder/stairs-down | paired walk(4); `z--`; then a THIRD walk(4) record with `z--` again |
| 8 | 4 | plain walk node | none |
| 9 | 5 | **wait/delay action** | `x`=0; writes `"Delay_%dsec"` label + `"wait %d000"` script into arena |
| 10 | 5 | **label / script action** | `x`=0; copies text after the last `\` of field-1 into `+0x0C` (max 32) |
| default | — | invalid | `dword_10202F06--` (rolls back the slot) |

So `actionType` (+0x2C) enum is: **2=rope, 3=ladder, 4=walk, 5=action/label, 6=stairs-down, 7=hole/shovel**. `refreshCavebotDialog` indexes a per-type display-character table with it (§5).

**Case 9 (wait) — script arena write.** It formats `"wait %dsec"`-style strings and finds a free 4096-byte slot in the script arena:

```c
wsprintfA(v30, "Delay_%dsec", v29);          // human label -> +0x0C
lstrcpy(v16 + 12, v30);
wsprintfA(v30, "wait %d000", v29);            // executable script text
for ( v18 = 0, v19 = 0; v18 < 0x80000; v18 += 4096, ++v19 )
    if ( !byte_10207F3B[v18] ) {              // first empty 4096-slot
        *((WORD*)v16 + 23) = v19 + 1;         // +0x2E = 1-based slot index
        lstrcpy(&byte_10207F3B[v18], v30);
        break;
    }
```

The arena `byte_10207F3B` is `0x80000` (512 KB) = 128 slots of 4096 bytes; `+0x2E` on the waypoint stores the 1-based slot number, i.e. this is how a waypoint references a Lua-ish action script string.

**Case 10 (label)** takes the basename after the last backslash of field-1 (`v33`) as the label text (`lstrcpyn(..., 32)`), also action-type 5.

### 4. `loadScriptFile` (0x100167eb) — text loader shell

```c
BOOL __stdcall loadScriptFile(LPCSTR lpFileName) {
    lpBuffer = HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, 0x200000);   // 2 MB
    hFile = CreateFileA(lpFileName, GENERIC_READ, FILE_SHARE_READ, 0, OPEN_EXISTING, 0x20, 0);
    if (hFile != INVALID_HANDLE_VALUE) {
        FileSize = GetFileSize(hFile, 0);
        ReadFile(hFile, lpBuffer, FileSize, &NumberOfBytesWritten, 0);
        CloseHandle(hFile);
    }
    parseWaypointsSection((CHAR*)lpBuffer, FileSize);
    return HeapFree(GetProcessHeap(), 0, lpBuffer);
}
```

Identical read shape to the binary path (same 2 MB scratch, `FILE_FLAG_SEQUENTIAL_SCAN`), but no RLE decode — the text buffer goes straight to the tokenizer. Note `FileSize` is read uninitialized if the open fails, which would pass garbage length to the parser; in practice the open succeeds.

### 5. `refreshCavebotDialog` (0x100160d6) — GUI repaint

Pure presentation. `dword_10072F94` is the cavebot dialog `HWND`. It clears and refills two list controls and syncs checkboxes:

```c
SendDlgItemMessageA(hDlg, 1028, LB_RESETCONTENT, 0, 0);            // waypoint list
for ( i = 0; i < dword_10202F06; ++i ) {
    formatWaypointListRow(lParam, i);                             // sub_10015FDC
    SendDlgItemMessageA(hDlg, 1028, LB_ADDSTRING, -1, lParam);
}
```

Control-ID map:

| ID | Role | Source global |
|---|---|---|
| 1028 | waypoint list box | walks `[0, dword_10202F06)` |
| 1015 / 1016 / 1042 | spin/edit (min/max/round counts) | `dword_10207F0A`, `dword_10207F0E`, `dword_10207F36` |
| 1100..1117 (`<= 0x45D`) | checkbox bank | `byte_10207AC6[j]` (per-ID bool) |
| 1035 | loot item list | loot table `unk_10202F0A` |
| 1024 / 1036 / 1037 | rope/shovel/hotkey checkboxes | `byte_10207F33/34/35` |

`formatWaypointListRow` (0x10015fdc) renders each row. If `byte_100F0E44` (label-display mode) is set and the record has a label, it prints `"T 00%d: %s"` (label); otherwise `"T 00%d: %d %d %d"` (x y z). It then overwrites the first char with a **type glyph** from `selectCavebotWaypointWrapper[*((WORD*)v2 + 22)]` — a per-actionType character table indexed by the +0x2C enum. That table is the human-facing legend of the internal type codes.

`formatLootRow` (0x10016073) renders loot entries from the 20-byte-strided loot table; category byte at `+2` of `0xff`/`253`/`254` maps to marker strings `" e"`, `"g"`, `"e1"`, else `"%05d %02d %s"` (itemid, count, name).

### 6. Loot table scan (inside `refreshCavebotDialog`)

```c
v3 = &unk_10202F0A;                    // loot table base
while ( v2 < 0x1F4 ) {                 // 500 entries
    if ( *(WORD*)v3 || v3[2] || v3[3] ) v9 = v2;   // track last non-empty
    v3 += 20;                                        // 20-byte stride
}
```

**Loot record layout (20 bytes, stride `0x14`, base `0x10202F0A`, 500 max):** `+0` word itemid, `+2` byte category (`0xff`/`0xfd`/`0xfe` special), `+3..` name string.

### 7. `parseSpellListA` (0x10008152) — word/spell list indexer

Called at the end of `loadCavebotFile`. Splits the CR/NUL-delimited word list at `byte_101F2EA8` into `0x202` (514)-byte records starting at output index 224, copying each token; entries beginning `"auto"` (`(v8|0x20202020)==0x6F747561`, i.e. `"auto"` low-case, with a following space) are flagged and registered via `registerCommands_table` (0x10030442, the CiroScript command table). Out of the waypoint path proper but shares the same decoded image.

---

The engine touches no packets directly; it is a file->memory transform. Its runtime footprint is the fixed cluster of globals in §Globals, refreshed by `botMainTickLoop(0x100227bd)` on its schedule. Those globals are the detection surface.

## Key globals

| Address | Meaning |
|---|---|
| `0x101E6EA8` | Config image base AND waypoint table base. Waypoint array of 48-byte records: +0 x, +4 y, +8 z (dword), +0x0C label/script string (32 B), +0x2C actionType word (2=rope,3=ladder,4=walk,5=action,6=stairs-down,7=hole), +0x2E 1-based script-arena slot index. Whole image is 0xA1093 bytes decoded from the .elfc. |
| `0x10202F06` | dword: live waypoint count (records in use at 0x101E6EA8). Cap 0x3E6 (998). Incremented per record, decremented to roll back an invalid line. |
| `0x10202F0A` | Loot item table base. 20-byte records (stride 0x14), 0x1F4 (500) max: +0 word itemid, +2 byte category (0xff/0xfd/0xfe special), +3.. name string. |
| `0x10207F3B` | Script/action string arena. 0x80000 bytes = 128 slots of 4096 bytes; waypoint +0x2E holds the 1-based slot index. Holds 'wait N000' delay scripts and label text. |
| `0x101F2EA8` | Decoded spell/word list region (source for parseSpellListA and the 512->4096 stride migration in loadCavebotFile). |
| `0x10202EA8` | End marker/upper bound of the decoded word-list region (loop stops when source pointer reaches it). |
| `0x10207F3A` | Byte flag: word-list already migrated to the script arena (0 until first load, then 1). |
| `0x10072F94` | HWND of the cavebot config dialog; target of all SendDlgItemMessageA calls. |
| `0x10043198` | MAX_PATH buffer holding the GetOpenFileNameA-selected cavebot file path. |
| `0x10207AC6` | Per-dialog-control-ID checkbox state byte array (indexed by control IDs 1100..1117 in refreshCavebotDialog). |
| `0x10207F0A / 0x10207F0E / 0x10207F36` | dwords: cavebot numeric settings pushed to spin/edit controls 1015/1016/1042 (e.g. min/max/round counts). |
| `0x10207F33 / 0x10207F34 / 0x10207F35` | Bytes: rope / shovel / hotkey cavebot toggle checkbox states (controls 1024/1036/1037). |
| `selectCavebotWaypointWrapper` | Per-actionType display-glyph table, indexed by the waypoint +0x2C type enum to produce the row-prefix character in the list box. |
| `0x100F0E44` | Byte flag: show waypoint labels vs raw x/y/z coords in the list rendering. |

## Detection notes

- Fixed module-relative waypoint table at elfbot.dll+0x1E6EA8 (0x101E6EA8) with a 48-byte stride and the exact field layout x/y/z (3 dwords) + 32-byte string + type word at +0x2C + slot word at +0x2E. Scanning a Tibia.exe-injected module's memory for this contiguous structure array is a strong signature.
- Live waypoint count as a bounded dword at 0x10202F06 with a hard cap of 0x3E6 (998); a non-zero value here inside an injected DLL is a direct 'cavebot active' tell.
- 20-byte loot table at 0x10202F0A capped at 0x1F4 (500) with a category byte (0xff/0xfd/0xfe) at +2 — another fixed-stride array fingerprint.
- 512 KB script-string arena at 0x10207F3B carved into 128 fixed 4096-byte slots; contents include literal generated strings 'wait %d000' and 'Delay_%dsec' — memory-string scanning for these two format products flags a loaded cavebot route.
- The .elfc file format has a 4-byte magic header 0xFFFFFFA0 (little-endian A0 FF FF FF). File-system/behavioral detection: presence of *.elfc under a Scripts\ directory, or ReadFile of such into a 0x200000-byte HeapAlloc buffer.
- GUI control-ID constellation is stable: waypoint list box ID 1028, loot list ID 1035, dialog HWND cached at 0x10072F94. Window-enumeration of the cavebot dialog by these control IDs is possible if the bot UI is visible.
- The CiroScript 'auto '-prefixed word-list entries registered via registerCiroScriptCommands (gotolabel/islocation/isdistance/... command names as embedded strings) are stable in-memory string artifacts of the scripting engine.
- Behavioral: a 512->4096 byte stride-expanding memcpy loop over an on-disk record region right after a large HeapAlloc(0x200000) is a distinctive load-time code pattern if hooking HeapAlloc/ReadFile in the target.
