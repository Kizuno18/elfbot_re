# ElfBot NG UI — exact panel & control geometry

Pixel-exact layout of every ElfBot window/panel and control, for recreating the
UI (e.g. "elfbot better"). Captured **live at runtime**: `elfbot.dll` (reports
itself as **ElfBot NG 4.1.6**) injected into a genuine Tibia 8.6 client, then
every window enumerated with `EnumChildWindows` + `GetWindowRect` via Frida.

Full machine-readable data: **[`ui/elfbot-ui-geometry.json`](../ui/elfbot-ui-geometry.json)**
— 16 panels, 369 controls, each `[class, ctrlId, x, y, w, h, text]` in
**client-relative pixels** (x,y = offset from the panel's top-left).

## How the UI is structured

- The panels are **not resource dialogs** — `elfbot.dll` has its resource
  directory stripped by Armadillo and imports only `CreateWindowExA` (no
  `CreateDialog*`). Every window is a registered class (`registerDialogs`
  `0x10002D46` → `RegisterClassExA` for `TBOTDLG7`, `TBOTDLGA`…`TBOTDLGW`) and
  every control is a raw `CreateWindowEx` child. So layout = the exact x/y/w/h
  passed at creation (confirmed by the live rects).
- **`TBOTDLG7`** is the main window ("ElfBot NG 4.1.6"), a **426×114** bar of 24
  buttons — the tab strip in the screenshot. `TBOTDLG00` (408×68) is the bootstrap
  container.
- Clicking a tab button posts `WM_COMMAND <id>`; the handler creates the
  corresponding `TBOTDLG*` panel as a separate top-level window next to the bar.

## Panel sizes

| Panel | Class | Size (px) | Controls |
|---|---|---|---|
| Main tab bar | TBOTDLG7 | 426 × 114 | 24 |
| Auto-Healing | TBOTDLGE | 408 × 239 | 37 |
| Extras | TBOTDLGF | 408 × 216 | 18 |
| Lists (Friends/Enemies) | TBOTDLGH | 408 × 276 | 19 |
| Aimbot | TBOTDLGI | 408 × 359 | 40 |
| HUD Display | TBOTDLGJ | 408 × 255 | 18 |
| Custom Hotkeys | TBOTDLGD | 412 × 353 | rows |
| Custom Shortkeys | TBOTDLGP | 412 × 353 | rows |
| Monster Targeting | TBOTDLGR | 576 × 440 | 74 |
| Cavebot | TBOTDLGS | 600 × 440 | 71 |
| Command Icons | TBOTDLGW | 573 × 296 | 76 |
| Creature Spy | TBOTDLGA | 459 × 176 | 1 |
| Link Server | TBOTDLGB | 249 × 252 | 15 |
| Navigation Server | TBOTDLGC | 249 × 203 | 14 |
| Safety Proxy Server | TBOTDLGQ | 246 × 302 | 26 |
| Skin selector | TBOTDLGV | 177 × 206 | 3 |

## The main tab bar (TBOTDLG7, 426×114)

24 buttons on a 5-column × 4-row grid. Standard tab button = **75 × 21 px**;
columns at **x = 3, 78, 153, 228, 303**; rows at **y = 26, 46, 67, 88**. The
top-right block holds settings-slot buttons **1–5** (24 × 21 at x = 303/327/351/
375/399, y = 26), **Save/Load** (72 × 21 at x = 303, y = 46/67), and **Help/
Custom** (48 × 21 at x = 375).

Row layout (label @ x,y):
- y=26: Healing(3) · Aimbot(78) · Lists(153) · HUD(228) · slots 1-5(303+)
- y=46: Extras(3) · Hotkeys(78) · Shortkeys(153) · Reconnect(228) · Save(303) · Custom(375)
- y=67: Cavebot(3) · Navigation(78) · Links(153) · Creature Spy(228) · Load(303) · Help(375)
- y=88: Targeting(3) · Proxy(78) · Icons(153)

## Repeating-row panels

**Hotkeys** (TBOTDLGD) and **Shortkeys** (TBOTDLGP) build their list as rows,
24 px pitch starting at y=73:
- Hotkeys row: checkbox `Button` (id 4000+N) @x=17 **16×16**; key `Edit` (5000+N)
  @x=38 **38×16**; command `Edit` (6000+N) @x=80 **294×16**.
- Shortkeys row: checkbox @x=17 **16×16**; trigger `Edit` @x=38 **50×16**;
  command `Edit` @x=92 **282×16**.

## Notes for recreation

- Control classes are the standard Win32 ones: `Button` (used for checkboxes,
  group boxes with a caption, and push buttons — distinguish by style),
  `Edit`, `ListBox`, `Static`, `msctls_trackbar32` (sliders on Targeting).
- Group-box captions (e.g. "Auto-Heal :", "Core Aimbot :", "Looting") are
  `Button` controls with `BS_GROUPBOX`, sized to the whole group region — useful
  as section frames.
- The command-wizard popups (`TBOTDLGK/L/M/N/O/T/U`) open contextually when
  editing a command and were not in this snapshot; re-run the capture with those
  dialogs open to add them.
- Font is the default GUI font (MS Sans Serif 8pt on the era's client); control
  heights of 15/13/21 px match that metric.
