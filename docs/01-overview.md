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

| Subsystem | Deep-dive doc |
|---|---|
| **Client hooks / memory engine** | [08](08-client-hooks-engine.md), [20](20-client-hooks-deep.md) |
| **Master tick loop** | [13](13-engine-tick-loop.md) |
| **CiroScript language + VM** | [07](07-ciroscript-language.md), [11](11-ciroscript-engine.md), runtime [14](14-ciroscript-runtime.md) |
| **Cavebot walker / waypoints** | walker [17](17-cavebot-walker.md), waypoints [19](19-cavebot-waypoints.md) |
| **Targeting** | [16](16-targeting-engine.md) |
| **Healer** | [15](15-healer-engine.md) |
| **Looting** | [23](23-looting-engine.md) |
| **Hotkeys / alarms / sound** | [24](24-hotkeys-alarms.md) |
| **NavNet client + packet proxy** | proxy [09](09-packet-proxy.md), codec [18](18-navnet-codec.md), server [04](04-navnet-server.md) |
| **Player-state readout / HUD** | [21](21-player-state.md), dialogs [10](10-feature-subsystems.md) |
| **Compiled scripts `.elfc`/`.elft`** | format [22](22-elfc-file-format.md); crypto lib [12](12-script-crypto-compression.md) |
| **Feature dialogs (23 windows)** | [10](10-feature-subsystems.md) |

All subsystems above are documented function-by-function; every function is in
the [master catalog](functions/index.md).

## Companion binaries

- **`navserv.exe`** — optional self-hosted NavNet hub; fully documented in
  [`04-navnet-server.md`](04-navnet-server.md). The bot's client half speaks the
  same protocol.
- **`USkin.dll`** — third-party window skinning; used for the bot/loader UI.

## Reading guide

Addresses are file-absolute at the module imagebase (`0x10000000` for
`elfbot.dll`). Function names in later docs match the names persisted in the IDA
database; original `sub_XXXX` addresses are always given alongside.
