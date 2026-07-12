# Tab coverage & runtime-test matrix

Every ElfBot tab, its dialog proc, its documentation, and its runtime test. This is
the tracker for "document each tab + test in runtime". Runtime tests run against the
in-game harness of [docs/33](33-runtime-ingame-validation.md) (genuine client on a
local TFS 0.4 8.60); the observable is what a Frida/RPM/socket probe confirms.

Legend — Doc: ✅ dedicated / 🟡 covered within a broader doc. RT (runtime): ✅ observed
live / 🟡 partially observed / ⏳ pending a stable in-game session.

| Tab | Class | DialogProc | Doc | Runtime test (exercise → observable) | RT |
|---|---|---|---|---|---|
| Healing | TBOTDLGE | `dlgProc_Healer 0x1001E3E5` | [15](15-healer-engine.md) ✅ | set HP threshold, take damage → heal spell/potion cast (send hook + HP mirror `0x1005F7D1`) | ⏳ |
| Aimbot | TBOTDLGI / DLG7 | `dlgProc_AutoAim 0x10003146` | [26](26-aimbot-combo.md) ✅ | enable + enemy on screen → best-square scan + attack packet | ⏳ |
| Targeting | TBOTDLGR | `dlgProc_Targeting 0x1001A715` | [16](16-targeting-engine.md) ✅ | define monster, spawn it → `g_100f0e20` set to creature ptr + attack | ⏳ |
| Cavebot | TBOTDLGS | `dlgProc_Cavebot 0x10019751` | [17](17-cavebot-walker.md) ✅ | load `.elfc`, enable → walker follows waypoints (`g_100f0e42`, map-click send) | ⏳ |
| Hotkeys | TBOTDLGD | `dlgProc_Hotkeys 0x10007360` | [24](24-hotkeys-alarms.md) ✅ | bind key→command, press → CiroScript runs (record `byte_100FAA3C`) | ⏳ |
| Shortkeys | TBOTDLGP | `dlgProc_Shortkeys 0x10006D3B` | [24](24-hotkeys-alarms.md) 🟡 | type trigger text → command fires (table `byte_10106B02`) | ⏳ |
| Lists (Friends/Enemies) | TBOTDLGH | `dlgProc_FriendsEnemies 0x1001E313` | [34](34-tabs-lists-extras-hud-spy-links.md) ✅ | add enemy name → red **E** marker + red outfit paint on that player | ⏳ |
| HUD On-Screen | TBOTDLGJ | `dlgProc_HudOnScreenInfo 0x10007B55` | [34](34-tabs-lists-extras-hud-spy-links.md) ✅ | enable overlays → ping/exp/timers drawn (draw hook `0x4F30C0`) | ⏳ |
| Creature Spy | TBOTDLGA | `dlgProc_HudCreatureList 0x10006BCE` | [34](34-tabs-lists-extras-hud-spy-links.md) ✅ | open window → live creature rows from shadow table (stride 168) | ⏳ |
| Extras (Graphics) | TBOTDLGF | `dlgProc_GraphicsTweaks 0x10007EC4` | [34](34-tabs-lists-extras-hud-spy-links.md) ✅ | toggle World View → `g_100ee8bb` set + `sub_10039c81`; toggle FPS tweak → GUI 10fps | ⏳ |
| Icons | TBOTDLGW | `dlgProc_SkinEditor 0x1001B8BE` | [32](32-icons-tab.md) ✅ | define icon → `drawCustomHudElements` renders; click → `hitTestHudButtons` → command | ⏳ |
| NavNet | TBOTDLGC | `dlgProc_NavNet 0x1001E7C3` | [18](18-navnet-codec.md) ✅ | connect navserv:7175 → position broadcast (`sendNavPositionUpdate 0x1003FFDF`) | ⏳ |
| Links | TBOTDLGB | `dlgProc_LinksNavNet 0x1001EB33` | [34](34-tabs-lists-extras-hud-spy-links.md) ✅ | Run Links → listen socket up; Set-for-client (logged off) → client patches at `0x4F36xx` | ⏳ |
| Proxy | TBOTDLGQ | `dlgProc_LinksProxy 0x1001EF0C` | [09](09-packet-proxy.md) ✅ | run proxy → watcher/controller listen socket (`byte_102898CD`) | ⏳ |
| Skin | TBOTDLGV | `dlgProc_Skin 0x100086B3` | [05](05-ui-init-framework.md) 🟡 | pick skin → USkin applies `.msstyles`; `elfbot.ini LastSkin` written | ⏳ |
| Command wizards | TBOTDLGK/L/M/N/O | `0x1001E1D9`/`0x1001DF05`/`0x1001D5FD`/`0x1001D2E0`/`0x1001D151` | [10](10-feature-subsystems.md) 🟡 | open from a hotkey edit → assembles CiroScript string joined by ` \| ` | ⏳ |
| Targeting editor | TBOTDLGT | `dlgProc_TargetingEditor 0x1000802F` | [16](16-targeting-engine.md) 🟡 | open per-target editor → edits 48-byte record `unk_101E6EA8` | ⏳ |
| Script editor | TBOTDLGU | `dlgProc_ScriptEditor 0x100083B6` | [10](10-feature-subsystems.md) 🟡 | open (mode 0–4) → shared editor loads/saves the mode's script | ⏳ |

## Documentation: complete

Every tab now has a doc home (dedicated ✅ or within a broader engine doc 🟡). The
wizard/editor popups (K/L/M/N/O/T/U) are indexed in docs/10 and their exact geometry
is the pending live-capture noted in [docs/29](29-ui-layout-geometry.md).

## Runtime tests: harness + method

Each RT reuses the [docs/33](33-runtime-ingame-validation.md) setup: inject
`elfbot.dll` into the in-game client, install the client hooks, then exercise the
tab's feature and confirm the documented global/packet/render effect via Frida
(memory read, `send`/`recv` hook, or the draw path). Status is ⏳ where a stable
in-game session with real activity is still needed — the shared RE VM's clients are
short-lived, so runtime tests are taken opportunistically when a client is up and
the re-* MCP tunnel is healthy (retried patiently across its intermittent 502s).
