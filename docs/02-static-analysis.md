# Static analysis — PE structure, imports, strings

All binaries are 32-bit x86 PE. Data below is from `pefile`
(`tools/pe_recon.py`) and IDA. SHA-256 (first 16 hex) is given for provenance.

## elfbot.dll — the bot

- `a5d62a6a8ab85a96…`, 4,706,304 bytes, DLL, imagebase `0x10000000`
- Timestamp 2010-07-06, linker version 0.0 (stripped by the packer)
- Single export: **`EcInit`** (ordinal 1) — the entry the loader calls
- imphash `bb55a0e88a2e524d8cb58131abdb3f62`

### Sections (note the randomized names — a packer tell)

| Section | VSize | Entropy | Notes |
|---|---|---|---|
| `.jdrv` | 0x40000 | 6.36 | code (contains `EcInit`, DllMain) |
| `.laxw` | 0x1000 | 2.01 | small data |
| `.ukjo` | 0x2a2000 | 0.35 | ~2.75 MB zero-filled — runtime buffers (.bss-like) |
| `.jiru` | 0x90000 | 6.32 | code |
| `.cdtemn` | 0x10000 | 0.81 | code/data |
| `.slau` | 0x20000 | 4.61 | data + `.idata` (imports) |
| `.qmfx` | 0x10000 | 6.48 | data |
| `.wmkzg` | 0x10000 | 4.15 | data |
| `.aqfu` | 0xb0000 | **7.78** | encrypted/compressed blob (Armadillo-owned, not main code) |
| `.ekdp` | 0x1000 | 0.00 | zero |
| `.Geddon` | 0x1000 | 4.53 | **Armadillo signature section** |

Despite the packer cosmetics, IDA recovers **3471 functions** with a resolved
import table and readable strings — the real code is *not* encrypted. See
[`03-packer-armadillo.md`](03-packer-armadillo.md).

### Imports (capabilities)

- **Tibia memory access:** `ReadProcessMemory`, `WriteProcessMemory`,
  `VirtualProtect`, `GetThreadContext`/`SetThreadContext`,
  `SuspendThread`/`ResumeThread` (kernel32) — read/write the game process and
  hook its threads.
- **Networking:** `WSOCK32` (`connect`, `send`, `recv`, `gethostbyname`,
  `bind`, `listen`, `accept`, `getsockname`) + `ws2_32.recv` — NavNet client,
  proxy, and packet injection.
- **Windowing / input:** full `user32` set incl. `RegisterHotKey`,
  `GetAsyncKeyState`, `FindWindowExA`, `SendMessageA`, clipboard, `CreateWindowExA`.
- **HUD / drawing:** `GDI32` (`BitBlt`, `CreateCompatibleDC`, `CreateFontA`,
  `GetDIBits`) — on-screen overlays / minimap rendering.
- **Sound:** `winmm` (`mmio*`) + `DSOUND.DirectSoundCreate` — alarm/alert WAVs.
- **Files / config:** `GetPrivateProfileStringA`/`WritePrivateProfileStringA`
  (INI), `CreateFileMappingA`/`MapViewOfFile` (memory-mapped data),
  `comdlg32` file/color dialogs, `SHELL32.DragQueryFile`.

### Key readable strings

`TibiaClient`, `GlobalSettings`, `INITIALIZEDLLADDR`, `scripts\`, `*.elfc`,
`*.elft`, `elfbot.ini`, `hotkeys.ini`, `lootitems.txt`, `outfits.txt`,
`serverlist.txt`, `elflog.txt`, `%s\playerinfo\%c\%s.txt`, spell power words
(`Light`, `Strong`, `Great`, `Spirit`), sound files (`elfng.wav`,
`gmdetected.wav`, `loot.wav`, `monster.wav`, `disconnected.wav`,
`defaultmessage.wav`), `Visit www.tibianeobot.com`, `CiroScript.com`, and the
packer leftover `…CRACKING\ArmaG3ddon_v1.9\dll loader.exe`.

## loader.exe — launcher / injector

- `0a91198e1496e4b0…`, 300,032 bytes, EXE, imagebase `0x400000`
- **Borland Delphi/C++Builder** (fake timestamp `0x2A425E19`, `CODE`/`DATA`/`BSS`
  sections, `.tls`)
- Injection primitives: `OpenProcess`, `VirtualAllocEx`/`VirtualProtectEx`,
  `WriteProcessMemory`, `ReadProcessMemory`, `CreateRemoteThread`-style flow,
  `FindWindowA/ExA`, `GetWindowThreadProcessId`, token/privilege APIs
  (`AdjustTokenPrivileges`, `LookupPrivilegeValueA`) for `SeDebugPrivilege`.
- References `elfload.dll` — the stub it injects.

## elfload.dll — injected loader stub

- `44cac7e08072edd3…`, 36,352 bytes, DLL, imagebase `0x10000000`
- MSVC (linker 5.12), unpacked, `.rsrc` holds a dialog
- Imports: `LoadLibraryA`, `GetProcAddress`, `WriteProcessMemory`,
  `CreateThread`, `CreateDialogParamA` — maps `elfbot.dll` and calls `EcInit`.
- References `elfbot.dll`, `USkin.dll`, `wsock32.dll`.

## navserv.exe — NavNet server

Fully documented in [`04-navnet-server.md`](04-navnet-server.md). MSVC console
app, `ws2_32` TCP hub, no CRT startup.

## USkin.dll — skinning library

- `9ccf45f05dc84f34…`, 708,608 bytes, DLL, MSVC 8.0, unpacked
- 41 `USkin*` exports (`USkinInit`, `USkinLoadSkin`, `USkinSetWindowSkin`, …).
  Off-the-shelf owner-draw theming lib used to skin the loader/bot windows with
  the `.msstyles` files in `skins/`. Out of scope beyond this note.
