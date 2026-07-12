# Tab reference — Lists, Extras, HUD, Creature Spy, Links

Dedicated coverage for the five tabs that previously only appeared in the
[docs/10](10-feature-subsystems.md) index. With this doc, every ElfBot tab has a
home (see the tab→doc matrix in [docs/00](00-status.md)). Each section is the RE of
that tab's `DialogProc` plus the on-disk state it drives.

## Lists — Friends & Enemies (`TBOTDLGH`, `dlgProc_FriendsEnemies` `0x1001E313`)

Four name lists (one name per line) that classify players, plus display options and
an auto-invite keyword. The proc is thin (tooltips + hide-on-close, HWND
`g_10072fb8`); the lists feed the friend/enemy colouring, the targeting engine and
the aimbot's *zero-friends* shot check.

| Ctrl | List / option |
|---|---|
| 1003 | **Enemies** |
| 1002 | **Friends** |
| 1011 | **Subenemies** — lesser enemies the bot may ignore for keybinds |
| 1008 | **Subfriends** — lesser friends |
| 1006 | markers: enemy red **E**, friend blue **F**, subenemy red **SE**, subfriend blue **SF** |
| 1007 | outfit paint: enemies red / friends blue (subs = lighter shades) |
| 1014 | **auto-invite keyword** — someone messaging e.g. `inv party` / `inv channel` is auto-invited to party/channel |

## Extras — Graphics tweaks (`TBOTDLGF`, `dlgProc_GraphicsTweaks` `0x10007EC4`)

Display/perf tweaks (HWND `g_10072f88`); one option persists to `elfbot.ini`.

| Ctrl | Feature |
|---|---|
| 1004 | **FPS/CPU tweak** — caps the game GUI to 10 fps and spends the budget redrawing the world more; when the client is minimised, disables graphics (CPU → 0) so many clients can run at once |
| 1006 | **reuse object** — keep the crosshair after using an inventory object repeatedly (object must not move) |
| 1002 | **World View** — hide the client GUI and stretch the world to the whole window; client becomes top-most and shrinkable; mouse must be off (coords shift); unfocused fps capped to 20. Sets `g_100ee8bb`, applies via `sub_10039c81`. For cams / multi-client watching |
| 1003 | **see player names off-screen and through floors** |
| 1013 | **LoadLastSkin** toggle → `WritePrivateProfileStringA("GlobalSettings","LoadLastSkin", …, elfbot.ini)` |

## HUD — On-Screen Information (`TBOTDLGJ`, `dlgProc_HudOnScreenInfo` `0x10007B55`)

Two master switches (Player Information + On-Screen Information) gating ~13 overlays
(HWND `g_10072fc4`). All semantics are verbatim from the control tooltips.

**Player Information** (per on-screen player, gathered by looking):
- 1005 master; 1011 guild name; 1014 vocation + level + current(~1%)/max HP;
- 1012 **auto-look** (invisible, no green look text) to gather the above;
- 1013 **mage mana estimation** — assume max mp, subtract mana-shield damage seen,
  add 200 per fluid drunk, painted orange on the mage.

**On-Screen Information** (world overlays):
- 1003 master; 1010 top-left ping / exp-per-hour / damage-last-second / current target;
- 1004 **PZ-lock timers** — 15-min red countdown per dead player, top-left, max 10,
  reset with the bot's Load button;
- 1002 **magic-wall** 20 s timers; 1006 **heal floaters** (light-blue `+%` when a
  creature heals > 1%); 1008 **DPS text** (red `-n%/s` under names losing > 1%/s);
- 1009 **self-buff timers** — haste (green), invisibility (purple), mana-shield
  (blue), magic-wall (yellow) countdowns;
- 1015 **exiva radar** — screen-edge direction markers for exiva'd players + NavNet
  allies; codes `E`(exiva)/`S`(seen)/`A`(ally) + age in seconds + `D`+distance;
  enemies red, friends blue;
- 1016 **active auto-binds** shown top-center with their trigger keys.

## Creature Spy — HUD creature list (`TBOTDLGA`, `dlgProc_HudCreatureList` `0x10006BCE`)

A dockable, scrollable live battle-list window (child list ctrl `1901`, HWND
`g_10072f70`). `WM_INITDIALOG` subclasses a **16800-byte shadow buffer**
`g_10072fd4` (`sub_1002ae81`); `WM_SIZE` resizes the list to fill. The rows come
from the DLL's shadow creature table (stride **168**, `0x63F8B8…0x64A308`, see
[docs/20](20-client-hooks-deep.md)/[docs/21](21-player-state.md)): on-screen
creatures grouped by relative level (`***Level N***`), each row showing
Pos/Health%/Speed/distance — a bot-side mirror of the client battle list, updated
each render tick.

## Links — spectate / remote-control server (`TBOTDLGB`, `dlgProc_LinksNavNet` `0x1001EB33`)

Runs a local relay so **other clients connect to watch or control your character**
(password is always `elfbot`). HWND `g_10072f74`, running flag `g_1005f536`.

| Ctrl | Field |
|---|---|
| 1004 | your IP others connect to (auto; manual behind proxy/router) `g_10134d83` |
| 1006 | listen port `g_10134dc3` |
| 1014 | account number others log in with `g_10134de3` (password fixed `elfbot`) |
| 1003 | **allow control** — checked = connectors can control your char, unchecked = watch-only (live-toggle via `sub_10001160`) |
| 1007 | **Run / Stop Links** — start `sub_100010bf(ip,port,allowControl,acct)`, stop `sub_10001222` |
| 1009/1010 | Links server IP/port to connect **to** `g_10134e03`/`g_10134e43` |
| 1008 | **set client for link use** |

**Set for client use (1008)** requires being logged **off** (`[0x64A9C0] != 31`,
else a "Logout first!" `MessageBoxA`). It then **patches the running client** so
that pressing *Enter Game* routes the connection through the link server instead of
the real login, via `WriteProcessMemory` (process handle `g_1005f612`):

| Address | Bytes | Note |
|---|---|---|
| `0x4F3649` | `e9 ab 00` (44009, 3) | connect/login rel-jmp |
| `0x4F371E` | `e9 a7 00` (42985, 3) | connect/login rel-jmp |
| `0x4F358A` | `eb` (1) | short-jump patch |
| `0x4F3102` | `e9 7e 17 00` (137193, 4) | connect/login rel-jmp |
| `g_10042668 + 66` | `e9 7e 17 00` (137193, 4) | second detour site |
| `0x549F80` | `c2 04 00`? (1218, 3) | near the XTEA routine `0x549F60` — cipher path |

(Contrast with **NavNet** `TBOTDLGC` — position/party sharing via `navserv.exe`,
[docs/18](18-navnet-codec.md) — and the **Proxy** `TBOTDLGQ`, the watcher/controller
listen socket, [docs/09](09-packet-proxy.md).)
