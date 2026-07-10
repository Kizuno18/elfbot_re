## Client hook engine (deep)

Supplements doc 08. Traces the ElfBot NG 8.60 `elfbot.dll` (imagebase `0x10000000`) client-hook engine: the incoming-packet MITM detour, the shadow-table maintenance it performs, the game-state snapshot synthesizer it feeds to proxy clients, and the full-light code patch. Client (Tibia 8.60) addresses are absolute at the client imagebase `0x00400000`; DLL globals are absolute at `0x10000000`.

The engine is two independent inline hooks planted into the stock 8.60 client:

| Hook | Client site | Installer | Handler |
|------|-------------|-----------|---------|
| Incoming-packet parser detour | client dispatcher (calls back to `dword_1005D897`) | (planted elsewhere; doc 08) | `hook_incomingPacketParser` `0x10001ca8` |
| Full-light renderer detour | `0x4F4869` (7-byte trampoline) | `installLightHook` `0x10002bdd` | `hook_fullLightDetour` `0x100029a4` |

---

### 1. Incoming-packet detour — `hook_incomingPacketParser` (0x10001ca8)

`__usercall` returning `edx:eax`, single arg in `edi` (`a1`). It is a detour wrapping the client's original message-parse routine. Flow:

```c
v1 = dword_1005D897(...);              // 0x10001cb3 call-through to the ORIGINAL parser
v21 = v1;                              // preserve return value (edx:eax) for the caller
HIDWORD(v1) = MEMORY[0x785D8C] + MEMORY[0x785D84];  // ptr = netbuf_base + read_cursor
switch ((_DWORD)v1) { ... }            // dispatch on the opcode the parser just returned
```

`dword_1005D897` (`0x785D97` fixed) is the trampoline back into the relocated original bytes of the client parser. Its return value low dword is the **opcode** that was just parsed; the engine reconstructs a pointer to the packet body from two client globals:

- `MEMORY[0x785D84]` — network read buffer base
- `MEMORY[0x785D8C]` — current read cursor / packet-start offset within that buffer

`HIDWORD(v1)` (== `netbuf_base + cursor`) is the live pointer to the message body the client just consumed. The `switch` mirrors a subset of server messages into DLL-private tables.

#### 1.1 Shadowed opcodes and the tables they write

```
case 0x0A  world-init      -> zero the 150-slot creature/battle table (0x1005A2A3, stride 40)
case 0xAC  open channel    -> upsert into private-channel table (0x1005CF17, stride 69), tag byte 0xAC
case 0xB2  open priv chan  -> upsert into party/priv-channel table (0x1005C9B3, stride 69), tag byte 0xB2
case 0xD2  VIP add/state   -> insert into creature/battle table, tag 0xD2, len = *(u16)(body+4)+7
case 0xD3  VIP login       -> find slot by dword@+1, set status byte at +7+*(u16@+5) := 1
case 0xD4  VIP logout      -> find slot by dword@+1, set status byte at +7+*(u16@+5) := 0
case 0xDD  VIP remove      -> find slot by dword@+1, clear tag + dword@+1
```

The `0x0A` (world init / login) case clears the whole mirror table so a fresh character login starts from empty shadow state:

```c
for (i = 0; i < 0x96; ++i) {                 // 150 slots
  v3 = (char*)&unk_1005A2A3 + 40*i;
  *v3 = 0;                                    // tag byte
  *(_DWORD*)(v3+1) = 0;                        // id dword
}
```

Insert pattern (VIP add, `0xD2`) — linear scan for a free slot (tag byte == 0), stamp opcode tag, `memcpyBytes` the body:

```c
for (ii = 0; ii < 0x96; ++ii) {
  slot = &unk_1005A2A3 + 40*ii;
  if (!*slot) {                               // free
    *slot = 0xD2;                             // tag
    memcpyBytes(slot+1, body, *(u16*)(body+4) + 7);  // copy id+payload
    break;
  }
}
```

The channel cases (`0xAC`/`0xB2`) first scan for an existing slot whose `*(u16)(slot+1)` matches `*(u16)(body)` (channel id) and skip if already present, otherwise take the first free slot — a keyed upsert. VIP state cases (`0xD3`/`0xD4`) match by the full `dword@+1` (creature id) and flip a status byte at a payload-relative offset (`+7 + *(u16@+5)`), leaving the record otherwise intact. `0xDD` clears the record. `0xAC`/`0xD2` additionally set `dword_1005DB4C = 1` when their respective enable flags (`byte_1005DB41` / `byte_1005DB43`) are set — a "channels dirty" latch consumed by the snapshot path.

#### 1.2 Proxy re-broadcast (LABEL_61)

After the shadow update, every packet is forwarded to the connected proxy clients:

```c
v12 = MEMORY[0x785D8C] + MEMORY[0x785D84];
if (MEMORY[0x785D8C] == 9) {                  // cursor at header end -> full app packet
  bufa = v12 - 9;                             // back up to length prefix
  len  = *(u16*)(v12-9) + 2;                  // framed length
  if (len && a1 != 20) {                       // a1==20 suppresses forwarding (internal source)
    for (nn = 0; nn < 0x10; ++nn) {            // 16 proxy client slots
      v14 = dword_1005DA85[nn];                // client SOCKET
      v15 = &unk_1005DAC5 + 4*nn;              // per-slot state
      if (v14) {
        if (*v15 == 2) {                        // state 2 = "needs full snapshot"
          *v15 = 1;                             // -> established
          if (MEMORY[0x636FE0] == 30) {         // client fully in-game
            dword_1005DB0D = v14;
            refreshPlayerPositionCache();       // sub_10001c38
            v16 = buildFullGameStateSnapshot(::buf);   // sub_10001960
            send(dword_1005DB0D, ::buf, v16, 0);       // synthetic login stream
          }
        }
        if (*v15 == 1) send(v14, bufa, len, 0); // live forward
      }
    }
  }
}
```

Two socket arrays:

| Global | Meaning |
|--------|---------|
| `dword_1005DA85[16]` | proxy client SOCKET handles (fixed `0x1005DA85`, 4-byte stride) |
| `unk_1005DAC5[16]` | per-client state: `2` = just connected/needs snapshot, `1` = established |
| `dword_1005DB0D` | scratch: current target socket during snapshot send |

`MEMORY[0x636FE0] == 30` is the client connection-state gate (30 = in-game). When a new proxy client is in state 2 and the game is live, the engine synthesizes and pushes a complete game-state stream so that a freshly-attached client sees the full world without waiting for live packets, then downgrades it to state 1 for incremental forwarding.

---

### 2. Game-state snapshot — `buildFullGameStateSnapshot` (0x10001960)

Called `sub_10001960(char *a1)`; if `a1==NULL` it `GlobalAlloc(GMEM_ZEROINIT, 0xC350)` (50000 bytes) + `GlobalLock` into `buf`. It assembles a synthetic server-to-client login stream by concatenating sub-encoders and back-patching two length words. Layout it writes:

| Offset | Field | Source |
|--------|-------|--------|
| +0 | outer length word (patched last) | computed |
| +3 (word) | inner length word (patched last) | computed |
| +8 | 14-byte template `byte_1004203F` | static; if zeroed, opcode `0x0A` login header |
| +9 | player creature id | `MEMORY[0x62CD30]` |
| +13 | dword `0x64000032` | constant client id/beat |
| +17 (word) | player X | `dword_1005D883` |
| +19 (word) | player Y | `dword_1005D887` |
| +21 (byte) | player Z | `dword_1005D88B` |
| +22 | map description | `buildMapDescriptionPacket` (sub_1000133f) |
| — | VIP list (if `!byte_1005DB46`) | `encodeVipList` (sub_1000154b) |
| — | player stats 0x19 bytes | `fillPlayerStatsRecord` (sub_1000188b) → `byte_10042051` |
| +47 | world light 3 bytes | `fillWorldLightRecord` (sub_10001870) → `byte_10042079` |
| +50 | skills 0x0F bytes (if `!byte_1005DB45`) | `fillSkillsRecord` (sub_10001929) → `byte_1004206A` |
| — | battle list (if `!byte_1005DB43`) | `copyBattleListRecords` (sub_100017e1) |
| — | container/tile items | `encodeContainerAndTileItems` (sub_1000159e) |
| — | open channels (if `!byte_1005DB44`) | `encodeOpenChannels` (sub_10001708) |
| — | private/party channels (if `!byte_1005DB41`) | `copyPrivateAndPartyChannels` (sub_10001813) |

Length fixup:

```c
v4 = v3 - 8 - a1;         // payload length
*((u16*)a1 + 3) = v4;     // inner length @ +6
v4 += 6;
*(u16*)a1 = v4;           // outer length @ +0
return v4 + 2;            // total bytes to send()
```

The `byte_1005DB41..46` flags gate which subsystems are serialized — an operator "what to mirror" config. The mirror tables (creature/battle, channels) filled by the packet detour are precisely the source the battle-list and channel sub-encoders read back out, so the snapshot is reconstructed from the DLL's own shadow state rather than re-reading client structures for those categories.

#### 2.1 Position cache — `refreshPlayerPositionCache` (0x10001c38)

Keeps `dword_1005D87F` pointing at the local player's creature slot and caches XYZ:

```c
v0 = dword_1005D87F ? *(_DWORD*)dword_1005D87F : dword_1005D87F;
if (MEMORY[0x62CD30] != dword_1005D87B || v0 != dword_1005D87B) {  // player id changed
  dword_1005D87B = MEMORY[0x62CD30];                                // cache id
  v1 = findCreatureSlotByPointer(MEMORY[0x62CD30]);                 // sub_1003997e
  if (v1) dword_1005D87F = v1;
}
if (dword_1005D87F)
  memcpyBytes(&dword_1005D883, (void*)(dword_1005D87F + 36), 0xC);  // copy XYZ (12 bytes @ slot+36)
```

`MEMORY[0x62CD30]` is the client's self creature-id. XYZ lives at creature-slot offset `+36`, copied into `dword_1005D883` (X), `dword_1005D887` (Y), `dword_1005D88B` (Z).

#### 2.2 Creature slot lookup — `findCreatureSlotByPointer` (0x1003997e)

Linear scan of the **client** creature array:

```c
v1 = 0x63FEF8;                            // client creature-array base
while (v1 < 0x64A308) {                    // end
  if (a1 == *(_DWORD*)v1) return v1;        // match on slot[0] (id/ptr)
  v1 += 168;                                // 168-byte stride
}
return 0;
```

Array: `[0x63FEF8, 0x64A308)`, 168-byte stride ⇒ 100 slots. This is the stock 8.60 client battle/creature list.

---

### 3. Sub-encoders (mirror → wire)

**`fillPlayerStatsRecord` (0x1000188b)** — snapshots the client stat block at `0x62CD00..0x62CD2C` into the `byte_10042051` template (opcode `0xA0`), producing the 0x19-byte stats message:

```c
byte_10042051 = 0xA0;                       // stats opcode
word_10042052 = MEMORY[0x62CD2C];            // hp
word_10042054 = MEMORY[0x62CD28];            // maxhp
dword_10042056 = MEMORY[0x62CD00];           // cap
dword_1004205A = MEMORY[0x62CD24];           // exp
word_1004205E  = MEMORY[0x62CD20];           // level
byte_10042060  = MEMORY[0x62CD18];           // level%
word_10042061  = MEMORY[0x62CD10];           // mana
word_10042063  = MEMORY[0x62CD0C];           // maxmana
byte_10042065  = MEMORY[0x62CD1C];           // maglevel
byte_10042066  = MEMORY[0x62CD14];           // maglevel%
byte_10042067  = MEMORY[0x62CD08];           // soul
word_10042068  = MEMORY[0x62CD04];           // stamina
```

**`fillWorldLightRecord` (0x10001870)** — builds the 3-byte world-light template `byte_10042079` (opcode `0x82`); level from `MEMORY[0x63BAB8]`, color constant `0xD7` (215):

```c
byte_10042079 = 0x82; byte_1004207A = MEMORY[0x63BAB8]; byte_1004207B = 0xD7;
```

**`fillSkillsRecord` (0x10001929)** — opcode `0xA1`; 7 skills × (value,percent) copied from client arrays `0x62D6D8` (values, +6474968) and `0x62D6BC` (percents, +6474940) into `byte_1004206B/byte_1004206C`, stride 4 in / 2 out over 0x1C bytes.

**`copyBattleListRecords` (0x100017e1)** — walks the 150-slot creature/battle mirror `0x1005A2A3` (stride 40); for each active slot (tag byte set) `memcpyBytes` `*(u16)(slot+5)+8` bytes into the output. Record layout: `[0]=tag, [1..4]=id, [5..6]=len, [7..]=payload`.

**`encodeOpenChannels` (0x10001708)** — walks the 16-slot **client** channel table at `0x6391E8` (stride 492). For each occupied slot emits an open-channel packet `0x6E`: channel index, channel id (`*(u32)(base+4)`), name (`lstrlen`+copy from `base+16`), then a message list from `base+60` (12-byte message records). Uses `packetOpcodeHasCoordFlag` to decide the extra coord byte per item entry.

**`copyPrivateAndPartyChannels` (0x10001813)** — copies active records out of two 20-slot 69-byte-stride mirror tables, `0x1005CF17` (private) then `0x1005C9B3` (party), each record `memcpyBytes`'d `*(u16)(rec+3)+5` bytes. These are the tables the `0xAC`/`0xB2` packet-detour cases fill.

**`encodeVipList` (0x1000154b)** — iterates the 10-slot **client** VIP table at `0x639164`/`0x639168` (stride 12) emitting VIP-add opcode `0x78` entries (index, name dword, optional online byte).

**`buildMapDescriptionPacket` (0x1000133f)** and **`encodeContainerAndTileItems` (0x1000159e)** — the map serializer. They walk floors/tiles via `mapCoordsToTilePtr`, emit creatures through `encodeCreatureAppear` (opcode `0x63`, id 99), items with a `packetOpcodeHasCoordFlag`-gated extra byte, and RLE-encode empty-tile skip runs (0xFF marker). `sub_1000159e` emits tile add/remove opcodes `0x6A`/`0x6C` at the cached player coords (`dword_1005D883-8`, `dword_1005D887-6`). Both consult `dword_1005D48F[]` (visited-creature dedupe list, count in `dword_1005D877`) and the `dword_1005D487`/`dword_1005D47B`/`dword_1005D483` floor-walk state set up during the map pass.

---

### 4. Full-light hack — `installLightHook` (0x10002bdd) + `hook_fullLightDetour` (0x100029a4)

`installLightHook`:

```c
dword_1005F612 = GetCurrentProcess();
return WriteProcessMemory(dword_1005F612, (LPVOID)0x4F4869, hook_fullLight_trampoline, 7, NULL);
```

Overwrites 7 bytes at client `0x4F4869` (inside the light-computation routine) with a trampoline that jumps to `hook_fullLightDetour`. `dword_1005F612` caches the pseudo-handle `GetCurrentProcess()` — all patches are self-writes through WPM (works around code-page protection uniformly).

`hook_fullLightDetour` restores the client registers it clobbered, computes the desired ambient level, then `JUMPOUT(0x4F4878)` back into client code:

```c
*(_DWORD*)(a1-4)   = a2;   // restore locals the stolen bytes touched
*(_DWORD*)(a1-244) = a2;
*(_DWORD*)(a1-240) = a2;
dword_1004476F = -1;       // "level" sentinel = leave unchanged
...
if (dword_1004476F != -1)
  *(_DWORD*)(a3 + 10888) = dword_1004476F;   // write ambient light into renderer struct (esi+0x2A88)
JUMPOUT(0x4F4878);
```

The middle block chooses one of three patch strategies against three client light sites `0x4F46BA`, `0x4F47BF`, `0x4F4840`, each patched with a 6-byte payload:

- **Full-light ON** (`!dword_1004476B && byte_10044773 && MEMORY[0x64F600]==7`): write `unk_1004477B` (nop/skip payload) to all three sites, force `dword_1004476F = 0`.
- **Custom level** (`dword_1004476B != 0`): write `unk_1004477B` to the three sites, then compute a clamped light level from `MEMORY[0x64F600]` (client global ambient level) minus `dword_1004476B` (unless sentinel 254), clamped by day/night thresholds (`0x64`, 7) into `dword_1004476F`.
- **OFF/restore** (else): write `unk_10044787` (original 6-byte payload) back to all three sites, restoring stock behavior.

Globals: `byte_10044773` = full-light enable flag; `dword_1004476B` = requested light delta (0=full, 254=absolute, else subtract); `dword_1004476F` = computed level or `-1` sentinel; `MEMORY[0x64F600]` = client's world ambient-light byte. `a3+10888` (0x2A88) is the field in the client render context that holds the effective tile light level.

---

### 5. Helpers

- `memcpyBytes` (0x1002ae6f): `qmemcpy` wrapper; every table copy routes through it.
- `packetOpcodeHasCoordFlag` (called throughout; header not in closure): returns whether an item opcode carries an extra stack/coord byte — governs the `+1` byte after each item id in map/channel/tile encoders.
- Thunks: `send` (0x100408ce), `WriteProcessMemory` (0x10040772), `GetCurrentProcess` (0x1004073c), `GlobalAlloc` (0x1004074e), `GlobalLock` (0x10040754).

---

### 6. Memory / packet touch summary

Reads (client): `0x62CD00–0x62CD30` (player stats+id), `0x63BAB8` (light), `0x62D6BC/0x62D6D8` (skills), `0x639164` (VIP), `0x6391E8` (channels), `0x63FEF8–0x64A308` (creatures), `0x62CD90` (tile/item table), `0x636FE0` (conn state), `0x64F600` (ambient light), `0x785D84/0x785D8C` (netbuf/cursor).

Writes (client .text via WPM): `0x4F4869` (light trampoline), `0x4F46BA/0x4F47BF/0x4F4840` (light patch sites).

DLL private tables (all at imagebase `0x10000000`): `0x1005A2A3` creature/battle mirror, `0x1005CF17`/`0x1005C9B3` channel mirrors, `0x1005DA85`/`0x1005DAC5` proxy socket + state arrays, `0x1005D883..8B` cached player XYZ, `0x10042051/0x10042079/0x1004206A` stat/light/skill templates, `0x1004476B/6F/73` light-hack config.

## Key globals

| Address | Meaning |
|---|---|
| `0x1005A2A3` | DLL-private creature/battle-list mirror table, 150 slots x 40-byte stride; record = [0]tag/opcode, [1..4]id, [5..6]len, [7..]payload. Filled by packet-detour cases 0xD2/0xD3/0xD4/0xDD, read back by copyBattleListRecords. |
| `0x1005CF17` | DLL-private private-channel mirror table, 20 slots x 69-byte stride; record = [0]tag(0xAC), [1..2]channel id, [3..4]len, [5..]payload. Filled by detour case 0xAC. |
| `0x1005C9B3` | DLL-private party/priv-channel mirror table, 20 slots x 69-byte stride; tag 0xB2. Filled by detour case 0xB2. |
| `0x1005DA85` | Array of 16 proxy-client WinSock SOCKET handles (4-byte stride); targets of the re-broadcast send(). |
| `0x1005DAC5` | Per-proxy-client state array, 16 x 4 bytes; 2 = just connected/needs full snapshot, 1 = established/live-forward. |
| `0x1005DB0D` | Scratch: current target socket handle during a snapshot send(). |
| `0x1005D87B` | Cached self creature id (mirror of client 0x62CD30) used to detect player-slot changes. |
| `0x1005D87F` | Cached pointer to the local player's client creature slot. |
| `0x1005D883` | Cached player X (word). Followed by 0x1005D887 = player Y, 0x1005D88B = player Z; 12-byte block copied from creature-slot+36. |
| `0x1005D877` | Count of entries in the visited-creature dedupe list dword_1005D48F during map serialization. |
| `0x1005D48F` | Visited-creature id list used to dedupe creatures already emitted in the map description vs tile records. |
| `0x1005D487` | Map-walk 'player floor seen' latch; with 0x1005D47B/0x1005D47F/0x1005D483 holds floor-walk cursor state. |
| `0x10042051` | Player-stats packet template (opcode 0xA0), 0x19 bytes, filled by fillPlayerStatsRecord from client globals. |
| `0x10042079` | World-light packet template (opcode 0x82), 3 bytes, filled by fillWorldLightRecord. |
| `0x1004206A` | Skills packet template (opcode 0xA1); byte_1004206B/1004206C hold the value/percent pairs. |
| `0x1004203F` | 14-byte login-header template copied at snapshot offset +8; when zero the engine writes an explicit 0x0A login header. |
| `0x1005DB41` | Enable flag: mirror private/party channels (gates copyPrivateAndPartyChannels and the 0xAC dirty latch). |
| `0x1005DB43` | Enable flag: mirror battle list (gates copyBattleListRecords and the 0xD2 dirty latch). |
| `0x1005DB44` | Enable flag: mirror open channels (gates encodeOpenChannels). |
| `0x1005DB45` | Flag: suppress skills/light sub-records in the snapshot (also zeroes player Z word). |
| `0x1005DB46` | Enable flag: mirror VIP list (gates encodeVipList). |
| `0x1005DB4C` | 'Channels dirty' latch set to 1 by 0xAC/0xD2 detour cases when their enable flags are set. |
| `0x1005F612` | Cached GetCurrentProcess() pseudo-handle used as hProcess for all self-WriteProcessMemory patches. |
| `0x1004476B` | Full-light hack requested delta: 0 = full light, 254 = absolute level, else subtract from client ambient 0x64F600. |
| `0x1004476F` | Computed effective light level written into the render context; -1 sentinel = leave unchanged. |
| `0x10044773` | Full-light hack master enable flag. |
| `0x1004477B` | 6-byte patch payload (skip/nop) written to the three client light sites when the hack is active. |
| `0x10044787` | 6-byte original patch payload restored to the three client light sites when the hack is disabled. |
| `0x1005D897` | Trampoline (dword_1005D897 -> 0x785D97 fixed) to the relocated original bytes of the client incoming-packet parser; called through at detour entry. |

## Detection notes

- Inline trampoline at client 0x4F4869: 7 bytes overwritten by installLightHook. Stock 8.60 .text at that address differs from the injected jump; a text-integrity hash of the light routine (0x4F4840..0x4F4878) detects it.
- Three 6-byte patches at client 0x4F46BA, 0x4F47BF, 0x4F4840 toggled by the full-light detour. Any of these deviating from the known-good bytes (payload unk_10044787) is a positive.
- The incoming-packet parser is detoured: a call/jmp redirecting the client dispatcher to elfbot.dll's 0x10001ca8 instead of the original code that 0x785D97 trampolines back to. Verify the parser prologue bytes and that the return target 0x785D97 holds relocated original instructions rather than the untouched client code.
- All code patches are applied via WriteProcessMemory against GetCurrentProcess() (self-patch). Hooking/monitoring WPM with hProcess == current process and lpBaseAddress in the client .text range (0x4F46BA/0x4F47BF/0x4F4840/0x4F4869) is a direct behavioral trip.
- Up to 16 extra WinSock sockets (dword_1005DA85 array) that send() copies of every framed server packet: an unexpected local proxy connection fan-out. A game-side heuristic can flag the client sourcing outbound sends of server-message frames it should only receive.
- elfbot.dll private mirror tables at fixed RVA-derived addresses 0x1005A2A3 (150x40), 0x1005CF17 / 0x1005C9B3 (20x69), 0x1005DA85 / 0x1005DAC5 socket arrays — scanning for these structured tables inside the injected module (or any non-client module) is a memory-signature detection.
- The synthetic login snapshot embeds constant 0x64000032 at buffer+13 and world-light color constant 0xD7; a proxy client parsing these constants confirms elfbot-generated (not server-generated) framing.
- Reads of the exact client global cluster 0x62CD00..0x62CD30, 0x63BAB8, 0x62D6BC/0x62D6D8, 0x639164, 0x6391E8, 0x63FEF8, 0x636FE0, 0x64F600, 0x785D84/0x785D8C from a foreign module thread is a coherent access fingerprint (guard pages / access-origin checks on these addresses catch the mirror path).
