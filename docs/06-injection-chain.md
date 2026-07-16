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

### elfload.dll functions (all 6, decompiled)

| Address | Name | What it does |
|---|---|---|
| `0x10001000` | `DllMain` | on `DLL_PROCESS_ATTACH` save hinstance, `GetCurrentProcess`, spawn `bootstrapThread` |
| `0x10001041` | `bootstrapThread` | call `mapBotAndRun(hinst,0,0,10)`, then `ExitThread` |
| `0x10001198` | `mapBotAndRun` | **the bootstrap**: `InitCommonControls`; `RegisterClassExA`; `LoadLibraryA("USkin.dll")`+`USkinInit`; `LoadLibraryA("elfbot.dll")`; `GetProcAddress("EcInit")`; `CreateDialogParamA("TBOTDLG00")`; `WriteProcessMemory`; `GetMessage`/`TranslateMessage`/`DispatchMessage` pump; `USkinExit` on exit |
| `0x10001060` | `bootstrapDlgProc` | dialog proc for `TBOTDLG00`; on `WM_COMMAND 0x539` registers a window class + creates the child window |
| `0x10001326` | `exitProc` | `ExitProcess` |
| `0x1000132b` | `nullsub` | empty |

So the confirmed sequence: `USkin.dll`→`USkinInit`, then `elfbot.dll`→
`GetProcAddress("EcInit")`, create the `TBOTDLG00` bootstrap dialog, and run a
message pump that ultimately drives `EcInit`. The rest of elfload's 47 functions
are import thunks and the MSVC CRT.

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

### loader.exe key functions (decompiled)

1780 functions (Delphi RTL/VCL + logic) decompiled; the injection-relevant ones:

| Address | Name | What it does |
|---|---|---|
| `0x0041D274` | `_start` | main: init (`sub_405028`); if `findTibiaClient()` fails → MessageBox **"Please run Tibia first!"** / "Elfbot NG"; else run `sub_403920` (inject + main loop) |
| `0x0041CF9C` | `findTibiaClient` | `FindWindowA("TibiaClient")` + `GetWindowThreadProcessId` + `OpenProcess`; also reads LDT/GDT/`fs` (anti-debug) — returns whether Tibia is up and opens its process |
| `0x0041C6B8` | `enableDebugPrivilege` | `OpenProcessToken` + `LookupPrivilegeValueA(SeDebugPrivilege)` + `AdjustTokenPrivileges`; `GetTokenInformation` for the UAC/elevation check behind the "run as Administrator" warning |
| `0x004143B0` | (madCodeHook inject) | large `LoadLibraryA`-driven routine — the madCodeHook cross-process DLL injection of `elfload.dll` |
| `0x0041AB98`, `0x0041C00C`, `0x0041A334` | remote writers | `WriteProcessMemory` into the Tibia process (bootstrap/parameter passing) |

The full per-function catalog is in
[functions/loader-catalog.md](functions/loader-catalog.md) (1780 functions).

### madCodeHook injection internals (reversed)

The statically-linked **madCodeHook** (Madshi) machinery inside loader.exe was
decompiled and named. The injection works by building a hook trampoline and
spawning a remote thread in the target:

- **Trampoline builder** — a length-disassembler engine: `scanHookPrologue`
  `0x40CE2C` disassembles the target's leading bytes tracking branches/jump
  tables; `analyzeHookRelocInstr` `0x40C8B4` follows call/jmp targets and records
  relocations; `buildTrampolineRegions` `0x40D340` `VirtualQuery`s the target,
  walks its PE sections and assembles the relocatable copied prologue;
  `decodeInsnFlagEffect` / `applyInsnRegDefs` are per-opcode helpers.
- **Remote-thread injection** — `createRemoteThreadHook` `0x40F474` duplicates
  thread handles and uses an ntdll `RtlCreateUserThread`-style API to create a
  thread in the target (Win9x code-patch fallback); `injectRemoteThreadsIntoProcesses`
  `0x4124B8` and `createRemoteThreadPerProcess` `0x41261A` `OpenProcess(0x1F0FFF)`
  + `CreateRemoteThread` across target PIDs.
- **Shared-memory IPC** — `createSharedMemoryMapping` `0x4113D8` /
  `initSharedIpcMapping` `0x40F0C4` set up named pagefile-backed sections;
  `buildInjectionSecurityDescriptor` `0x41101C` builds a DACL granting owner +
  SYSTEM access (via `getProcessTokenUser` `0x410F9C`) so loader and injected DLL
  share hook/session state (`getOrInitSharedProcessInfo`, `cleanupSharedHookTables`).
- **PE export resolution** — `mapOwnModuleImage` `0x40A83C` maps the module's
  on-disk image; `resolveApiViaMappedImage` `0x40A918` / `resolveExportByOrdinalRange`
  `0x40AB08` walk the export table by name/ordinal (avoids IAT hooks).
- **Process discovery** — `initToolhelp32Api` `0x4054F4` +
  `findProcessByModulePath` `0x40E6A4` / `findHelperProcess` `0x40E7A8` enumerate
  processes via ToolHelp32.

Net: loader.exe uses madCodeHook to inject `elfload.dll` into `Tibia.exe` by
`OpenProcess` + shared-memory-coordinated `CreateRemoteThread`, with a relocated
trampoline so the DLL maps cleanly. Delphi decompiles less cleanly than the MSVC
binaries, so names come from the WinAPI/string anchors.

## Why `loader.exe` fails `err=126` on the modern lab (root cause)

The runtime harness ([docs/33](33-runtime-ingame-validation.md)) found `loader.exe`
logs `FAIL err=126` (`ERROR_MOD_NOT_FOUND`) and never boots the engine, so injection
there is done by a direct `LoadLibrary` + `CreateThread(botMainTickLoop)` instead.
Statically the 126 is pinned to the load chain, not to the pieces people usually
suspect:

- **Target detection is fine.** loader finds the client by
  `FindWindowA("TibiaClient", …)` (`0x405482`) → `GetWindowThreadProcessId`
  (`0x40549A`); a genuine 8.60 client — even the RSA-patched `Tibia_ot.exe` — keeps
  the `TibiaClient` window class, so this resolves (a mismatch would raise the
  `"Please run Tibia first!"` MessageBox, not `126`).
- **elfbot's dependencies are present.** Its imports are all stock system DLLs
  (`WSOCK32`, `ws2_32`, `DSOUND`, `winmm`, `SHELL32`, `comdlg32`, `GDI32`,
  `COMCTL32`, `user32`, `kernel32`) — all on the Win10 lab. `elfload.dll` itself only
  needs `user32`/`kernel32`/`comctl32`. So the `126` is not a missing static import.

That leaves two candidates, both consistent with the observed failure:

1. **elfload's directory-relative resolution.** Once mapped, `elfload!sub_10001198`
   builds `<its own module dir>\USkin.dll` and `<…>\elfbot.dll` from
   `GetModuleFileNameA` + append and `LoadLibraryA`s them. If madCodeHook maps
   `elfload.dll` from a path where `elfbot.dll`/`USkin.dll` are not co-located, that
   directory-relative load returns `126`. All three DLLs must sit in one folder.
2. **madCodeHook on Win10.** The injector is circa-2010 Madshi code; its
   remote-thread + `findHelperProcess` (`0x40E7A8`) cross-session/cross-bitness model
   predates Win10 session isolation. A missing/creatable madCodeHook helper module in
   that path also surfaces as `126` from the remote `LoadLibrary`.

The [docs/33](33-runtime-ingame-validation.md) direct-`LoadLibrary(elfbot.dll)` +
manual hook install + `CreateThread(0x100227BD)` reproduces the loader's end state
while bypassing both the madCodeHook path and the directory-relative resolution —
which is exactly why it succeeds where `loader.exe` `126`-fails. A live confirmation
of the fix (co-locate the three DLLs, run `loader.exe` against the client window) is
gated on the runtime stack being present; the RE-level root cause is the load chain
above.
