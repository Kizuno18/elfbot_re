# elfbot.dll — initialization & UI framework

The bot is a dialog-driven Win32 application injected into `Tibia.exe`. This
doc covers the boot path and the window/message framework that hosts every
feature. Feature-specific dialogs are documented per-subsystem in later docs.

## Boot path

1. **`DllEntryPoint`** `0x10002C1F` — on `DLL_PROCESS_ATTACH` stores
   `GetCurrentProcess()` in `dword_1005F612` and spawns thread `sub_10002D08`
   (a stub that immediately `ExitThread(1)` — real init happens via the export).
2. **`EcInit(clientCtx, hWnd)`** `0x10002CBE` — the sole export, called by
   `elfload.dll` after mapping the bot. Saves the client context pointer
   (`dword_1004478D`) and the Tibia window handle (`hWnd`), `Sleep(1000)`, then:
   - `sub_10002D46(hModule, …)` — **registers all bot dialogs** (below).
   - `sub_10002C87(hModule, 17000, 0, cb=sub_100086B3, 0)` — posts the initial
     "show window" command to the host window.

## Dialog registration — `registerDialogs` `0x10002D46`

`InitCommonControls`, then registers ~23 dialog templates from the DLL's
resources, each paired with a window procedure. Registration uses a shared
descriptor and helper `sub_10002D16`. The resource `TBOTDLG*` names map to
feature windows/tabs; the paired procs are the per-feature controllers:

| Resource | WndProc | Feature (see subsystem docs) |
|---|---|---|
| TBOTDLG7 | `sub_10003146` | main control window (14 KB master proc) |
| TBOTDLGA | `sub_10006BCE` | *(mapped by dialog-feature workflow)* |
| TBOTDLGB | `sub_1001EB33` | *(writes Tibia memory — combat/action)* |
| TBOTDLGC | `sub_1001E7C3` | |
| TBOTDLGD | `sub_10007360` | |
| TBOTDLGE | `sub_1001E3E5` | |
| TBOTDLGF | `sub_10007EC4` | |
| TBOTDLGH | `sub_1001E313` | |
| TBOTDLGI | `sub_10007CA5` | |
| TBOTDLGJ | `sub_10007B55` | |
| TBOTDLGK | `sub_1001E1D9` | |
| TBOTDLGL | `sub_1001DF05` | |
| TBOTDLGM | `sub_1001D5FD` | |
| TBOTDLGN | `sub_1001D2E0` | |
| TBOTDLGO | `sub_1001D151` | |
| TBOTDLGP | `sub_10006D3B` | |
| TBOTDLGQ | `sub_1001EF0C` | |
| TBOTDLGR | `sub_1001A715` | |
| TBOTDLGS | `sub_10019751` | |
| TBOTDLGT | `sub_1000802F` | |
| TBOTDLGU | `sub_100083B6` | |
| TBOTDLGV | `sub_100086B3` | **skin selector** (confirmed) |
| TBOTDLGW | `sub_1001B8BE` | (5 KB proc) |

## Message helper — `postBotMessage` `0x10002C87`

Wraps `SendMessageA(hWnd, WM_COMMAND=0x111, wParam, lParam[])` to drive the host
window from anywhere in the bot (menu commands, dialog show/hide). Command ids
seen: `0x53A` (show main), `0x53B` (apply skin), `1020` (re-focus main dlg).

## Skin selector — `sub_100086B3` (TBOTDLGV)

The one dialog proc read in full so far. On `WM_INITDIALOG` it reads
`elfbot.ini [GlobalSettings] LoadLastSkin` / `LastSkin`, lists `Skins\*.msstyles`
into a listbox (`DlgDirListA` + `<No Skin>`), preselects the saved skin. On OK it
saves `LastSkin`, builds the skin path and applies it via
`SendMessageA(hWnd, WM_COMMAND, 0x53B, path)` — the host then loads it through
`USkin.dll`. Establishes the global config convention: **`elfbot.ini`, section
`[GlobalSettings]`**.

## Global config

- `elfbot.ini` `[GlobalSettings]` — `LoadLastSkin`, `LastSkin`, and the general
  bot options (login/client settings, window text, feature toggles).
- Per-feature INIs: `hotkeys.ini` (`[CavebotHotkeys]`, persistent hotkeys),
  cavebot/targeting scripts (`scripts\*.elfc` / `*.elft`), `lootitems.txt`,
  `outfits.txt`, `serverlist.txt`, `elfsettings\`.
