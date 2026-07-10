# Overview — architecture & injection chain

ElfBot NG 8.60 is a **memory-injection bot** for the Tibia 8.60 client. It runs
its logic *inside* `Tibia.exe`'s address space, reading and writing game memory
directly and hooking the client, rather than talking to the server as a separate
program. A small launcher injects a loader stub, which maps the main bot DLL and
hands it the client context.

## Injection chain

```
loader.exe  (Delphi GUI)
   │  enable SeDebugPrivilege (AdjustTokenPrivileges + LookupPrivilegeValueA)
   │  FindWindowA / GetWindowThreadProcessId  → locate Tibia.exe
   │  OpenProcess + VirtualAllocEx + WriteProcessMemory + remote thread
   ▼
elfload.dll  (injected into Tibia.exe)
   │  LoadLibraryA("elfbot.dll") into the game process
   │  GetProcAddress("EcInit")
   │  CreateDialogParamA (loader UI) ; WriteProcessMemory bootstrap
   ▼
elfbot.dll  ::EcInit(clientCtx, hWnd)
   │  store client context (dword_1004478D) + Tibia HWND
   │  Sleep(1000) ; sub_10002D46(hModule,…) ; sub_10002C87(hModule,17000,…, cb=sub_100086B3)
   │  (DllMain already spawned worker thread sub_10002D08 on PROCESS_ATTACH)
   ▼
bot main loop — memory RW, cavebot, hotkeys, HUD, proxy, script engine
```

Confirmed entry points in `elfbot.dll`:

- **`DllEntryPoint`** `0x10002C1F` — on `DLL_PROCESS_ATTACH` saves
  `GetCurrentProcess()` and spawns worker thread **`sub_10002D08`**.
- **`EcInit`** `0x10002CBE` (the sole export) — called by the loader with the
  client context and Tibia window handle; installs the bot's timer/UI with
  callback **`sub_100086B3`**.

## Subsystem map (working)

Derived from imports, strings and the entry call graph; refined as functions are
documented in later docs.

| Subsystem | Evidence | Status |
|---|---|---|
| **Client memory engine** | `ReadProcessMemory`/`WriteProcessMemory`, `VirtualProtect`, thread context APIs; `TibiaClient`, `INITIALIZEDLLADDR` | WIP |
| **Config / settings** | `GetPrivateProfileStringA`, `elfbot.ini`, `GlobalSettings`, `hotkeys.ini`, `serverlist.txt` | WIP |
| **CiroScript engine** | `scripts\*.elfc`/`*.elft`, `CiroScript.com`, compiled script blobs | WIP |
| **Cavebot / walker** | navigation, waypoint execution | WIP |
| **NavNet client** | `WSOCK32` connect/send/recv, `gethostbyname`; mirror of `navserv.exe` | WIP |
| **Hotkeys / input** | `RegisterHotKey`, `GetAsyncKeyState`, `SendMessageA` | WIP |
| **HUD / overlay** | `GDI32` BitBlt/DC/font, `GetDIBits`; minimaps | WIP |
| **Sound / alarms** | `winmm` mmio + `DSOUND`; `*.wav` assets | WIP |
| **Looting** | `lootitems.txt`, `loot.wav` | WIP |
| **GUI (bot windows)** | `CreateWindowExA`, `SendDlgItemMessageA`, `USkin.dll` theming | WIP |
| **GM / anti-detection** | `gmdetected.wav`, flash/alert | WIP |

## Companion binaries

- **`navserv.exe`** — optional self-hosted NavNet hub; fully documented in
  [`04-navnet-server.md`](04-navnet-server.md). The bot's client half speaks the
  same protocol.
- **`USkin.dll`** — third-party window skinning; used for the bot/loader UI.

## Reading guide

Addresses are file-absolute at the module imagebase (`0x10000000` for
`elfbot.dll`). Function names in later docs match the names persisted in the IDA
database; original `sub_XXXX` addresses are always given alongside.
