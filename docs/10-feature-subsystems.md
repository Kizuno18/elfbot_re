# elfbot.dll — feature subsystems (the 23 dialogs)

Each `TBOTDLG*` resource is a feature tab/window with its own `DialogProc`
(registered by `registerDialogs` `0x10002D46`, see [05](05-ui-init-framework.md)).
Mapped by IDA analysis of every proc; names below are the identifiers now
persisted in the database. This is the master index of bot features; deep
per-function docs hang off each subsystem.

## AutoAim / PvP combo (the aimbot)

- **`dlgProc_AutoAim`** `0x10003146` (TBOTDLG7) — the aimbot tab, described in
  its own tooltips as *"the heart of the pvp-bot"*. `WM_INITDIALOG` `GlobalAlloc`s
  a 0x42800-byte table of aim commands + help text. Commands: `aimgfb`,
  `aimavalanche`, `aimthunderstorm`, `aimstoneshower`, `aimtype`, `autoaim`,
  `autoaimtarget`. Each computes the best square to hit the most enemies with
  **zero friends** (respects protection zones, traces shots), or falls back to
  `autoaim` with the configured rune (`aimtype`).
- **`dlgProc_AutoAimCombo`** `0x10007CA5` (TBOTDLGI) — combo synchronization:
  action modes (No Action / Attack / Follow), 200–2000 ms delay, leader/name
  list, SD-rune combo. Coordinates multi-client "combo" burst attacks.

## Targeting (monster attack AI)

- **`dlgProc_Targeting`** `0x1001A715` (TBOTDLGR) — the targeting config window:
  a list (ctrl 1028) of up to **128 monster entries × 320-byte records**
  (name + attack strategy, spells, priorities, danger). Loads/saves `.elft`
  (drag-drop, ext check `elft`).
- **`dlgProc_TargetingEditor`** `0x1000802F` (TBOTDLGT) — per-target editor popup;
  edits records in `unk_101E6EA8` (48-byte stride), name-vs-numeric display flag
  `byte_100F0E44`.
- **`dlgProc_FriendsEnemies`** `0x1001E313` (TBOTDLGH) — player classification:
  enemies / friends / subenemies / subfriends name lists + auto-invite keyword.
  Feeds friend/enemy colouring and the aimbot's "zero friends" logic.

## Cavebot (waypoint hunting)

- **`dlgProc_Cavebot`** `0x10019751` (TBOTDLGS) — waypoint list (ctrl 1028) +
  embedded creature list (ctrl 1035); shows the **NeoBot** ad banner
  (`A new bot for Tibia called NeoBot … www.tibianeobot.com`) — confirming the
  ElfBot NG → NeoBot rebrand. Loads/saves `.elfc`.

## Healer

- **`dlgProc_Healer`** `0x1001E3E5` (TBOTDLGE) — health spell + mana/health potion
  type combos (Light/Strong/Great/Ultimate/Spirit potions, UH Rune) with delays;
  refill thresholds (`refillhealth`, `refillmana`). Casts/uses to keep HP/MP up.

## Hotkeys

- **`dlgProc_Hotkeys`** `0x10007360` (TBOTDLGD) — up to **96 hotkey rows** in
  `byte_100FAA3C` (514-byte records: `[0]` key/button code, `[1]` enabled,
  `[2..]` command text). Master enables: `byte_100F94C5` (bot hotkeys),
  `byte_1013F32B` (persistent hotkeys).
- **`dlgProc_Shortkeys`** `0x10006D3B` (TBOTDLGP) — "Shortkeys": text-triggered
  commands, table `byte_10106B02` (546-byte entries: `+0` trigger text, `+33`
  active, `+34` command), master flag `byte_10135279`, prefix symbol
  `byte_1013F327`.
- **`dlgProc_HotkeyActionPicker`** `0x1001E1D9` (TBOTDLGK),
  **`dlgProc_CommandParamPicker`** `0x1001D5FD` (TBOTDLGM),
  **`dlgProc_CommandBuilder`** `0x1001D151` (TBOTDLGO) — the wizard that assembles
  a CiroScript command string (joined with `" | "`) for a hotkey.

## Command builder / tools (script authoring)

- **`dlgProc_CommandPicker`** `0x1001DF05` (TBOTDLGL) — category listbox of the 7
  action groups: **Attack, Miscellaneous, Movement, Inventory, Restoration,
  Cavebot, Settings** — the taxonomy of CiroScript statements.
- **`dlgProc_CommandParamBuilder`** `0x1001D2E0` (TBOTDLGN) — item/parameter
  composer, item table `dword_1005E198` (1064-byte stride).
- **`dlgProc_ScriptEditor`** `0x100083B6` (TBOTDLGU) — shared multi-line editor,
  4 modes via `dword_10072FB4`: Persistent commands, Edit Cavebot Script, Edit
  Targeting Script, Icons.

## HUD / on-screen display

- **`dlgProc_HudCreatureList`** `0x10006BCE` (TBOTDLGA) — live creature/battle
  list (ctrl 1901), shadow buffer `unk_10072FD4` (175 × 96-char rows), grouped by
  relative level (`***Level N***`), rows show Pos/Health%/Speed/distance. Reads
  the DLL's shadow creature table (stride **168**, `0x63F8B8…0x64A308`).
- **`dlgProc_HudOnScreenInfo`** `0x10007B55` (TBOTDLGJ) — ~14 toggles: MP
  estimation for mages, PZ-lock/death timers, healing-percent floaters, DPS
  text, self-buff timers (haste/invis/manashield/magic-wall), top-left
  ping/exp/damage/target HUD.
- **`dlgProc_GraphicsTweaks`** `0x10007EC4` (TBOTDLGF) — display tweaks (FPS/CPU
  tweak, etc.); also touches `elfbot.ini [GlobalSettings]`.

## NavNet / Links (multiplayer)

- **`dlgProc_NavNet`** `0x1001E7C3` (TBOTDLGC) — connect to a shared **NavNet**
  server (`navserv.exe`, port **7175**): server IP, display name, password,
  custom name colour, colour-reduction toggle. Party members broadcast
  position/name/colour (see [04](04-navnet-server.md)).
- **`dlgProc_LinksNavNet`** `0x1001EB33` (TBOTDLGB) — "Links": run a local link
  server so other clients connect (password fixed `elfbot`); toggles remote
  control; when logged off (`MEMORY[0x64A9C0]==31`) **patches the client**
  (`WriteProcessMemory` at `0x4F3649`, `0x4F371E`, `0x4F358A`, `0x4F3102`,
  `0x549F80`) to route through the link. Writes Tibia memory.
- **`dlgProc_LinksProxy`** `0x1001EF0C` (TBOTDLGQ) — the link/proxy server config
  (listen socket for watchers/controllers), running flag `byte_102898CD`, packed
  action/target bits.

## Skinning

- **`dlgProc_Skin`** `0x100086B3` (TBOTDLGV) — skin selector, `elfbot.ini
  [GlobalSettings] LoadLastSkin/LastSkin`, `Skins\*.msstyles` (see
  [05](05-ui-init-framework.md)).
- **`dlgProc_SkinEditor`** `0x1001B8BE` (TBOTDLGW) — custom-skin designer, 128 ×
  **4308-byte** window/icon records at `unk_1014F420`.

## Feature → dialog summary

| Feature | Dialogs |
|---|---|
| AutoAim / combo | TBOTDLG7, TBOTDLGI |
| Targeting | TBOTDLGR, TBOTDLGT, TBOTDLGH |
| Cavebot | TBOTDLGS |
| Healer | TBOTDLGE |
| Hotkeys | TBOTDLGD, TBOTDLGP, TBOTDLGK, TBOTDLGM, TBOTDLGO |
| Command tools | TBOTDLGL, TBOTDLGN, TBOTDLGU |
| HUD | TBOTDLGA, TBOTDLGJ, TBOTDLGF |
| NavNet / Links | TBOTDLGC, TBOTDLGB, TBOTDLGQ |
| Skin | TBOTDLGV, TBOTDLGW |

Each subsystem gets a deep pass (per-function decompilation of the engine
helpers each proc drives) in dedicated docs; this index anchors that work and
records the on-disk data structures each feature owns.
