# Injection chain — loader.exe → elfload.dll → EcInit

How ElfBot gets its code running inside the Tibia client. Three stages, three
binaries. Per-function IDA detail for `elfload.dll` and `loader.exe` is added in
follow-up passes; this doc establishes the mechanism from imports, strings and
the confirmed `elfbot.dll` entry.

## Stage 1 — loader.exe (Delphi GUI, "Elfbot NG")

Borland Delphi launcher (Delphi exception classes `EControlC`, `EConvertError`,
`ESafecallException`, `EOutOfMemory` present; fake 1992 timestamp). What it does:

- **Find the client:** `FindWindowA` / `FindWindowExA` +
  `GetWindowThreadProcessId` to locate a running `Tibia.exe`. If none:
  **"Please run Tibia first!"**.
- **Acquire rights:** `OpenProcess`, `OpenProcessToken`,
  `AdjustTokenPrivileges` + `LookupPrivilegeValueA` — enable `SeDebugPrivilege`
  so it can write into the client. `GetThreadContext` / thread manipulation
  present for the injection.
- **Inject:** links **`madCodeHook`** (Madshi's code-injection / API-hooking
  library) — the loader does not hand-roll `CreateRemoteThread`; it uses
  madCodeHook to map **`elfload.dll`** into the Tibia process. `elfload.dll` is
  referenced by name.
- Also a UI (`Elfbot NG` window) for choosing the client and launch options.

madCodeHook handles the cross-process DLL injection and the trampoline setup;
this is why `loader.exe`'s own import set looks lighter than a from-scratch
injector.

## Stage 2 — elfload.dll (bootstrap, runs inside Tibia.exe)

Small MSVC DLL (36 KB) mapped into the client by stage 1. It carries an app
manifest (`name="Elfbot.dll"`, common-controls v6) and a dialog resource. On
load it:

1. `USkinInit` — initialize the `USkin.dll` theming engine (the bot/loader
   windows are skinned).
2. `LoadLibraryA("elfbot.dll")` — map the main bot into the client's address
   space (Armadillo stub runs here, in-process).
3. `GetProcAddress` the export **`EcInit`**.
4. `CreateDialogParamA` — create the loader/bootstrap dialog; `WriteProcessMemory`
   present for any in-process patching.
5. Call **`EcInit(clientCtx, hWnd)`** with the client context and Tibia window.
6. `USkinExit` on teardown.

Imports confirm the flow: `LoadLibraryA`, `GetProcAddress`, `CreateThread`,
`CreateDialogParamA`, `WriteProcessMemory`; references `elfbot.dll`, `USkin.dll`,
`wsock32.dll`, `comctl32.dll`.

## Stage 3 — elfbot.dll::EcInit (bot init)

Documented in [`05-ui-init-framework.md`](05-ui-init-framework.md):
`EcInit` stores the client context + window handle, registers the 23 feature
dialogs (`registerDialogs` `0x10002D46`), and shows the main control window. From
here the bot reads/writes Tibia memory directly (it shares the client's address
space, so no `ReadProcessMemory` round-trips are needed for most work — pointers
are dereferenced in-process; `ReadProcessMemory`/`WriteProcessMemory` remain for
specific cross-guard writes).

## Why in-process matters

Because `elfbot.dll` lives inside `Tibia.exe`, the "memory engine" is mostly
plain pointer dereferences against the client's data structures, using offsets
supplied at runtime (the `SetFunctionAddresses` CiroScript command / loader
config) so one bot build tracks multiple client patches. This is the classic
2010-era Tibia bot architecture: injected DLL + configurable client offsets +
a script VM driving cavebot/targeting.

## TODO (IDA passes)

- `elfload.dll`: enumerate and document its handful of functions (bootstrap,
  dialog proc, EcInit thunk).
- `loader.exe`: map the Delphi form + the madCodeHook injection call site and
  the client-detection / privilege code. Delphi RTTI aids naming.
