# Tab coverage & runtime-test matrix

Every ElfBot tab, its dialog proc, its documentation, and its runtime test. This is
the tracker for "document each tab + test in runtime". Runtime tests run against the
in-game harness of [docs/33](33-runtime-ingame-validation.md) (genuine client on a
local TFS 0.4 8.60); the observable is what a Frida/RPM/socket probe confirms.

> **Superseded by [docs/39](39-module-runtime-report.md).** The full behavioural sweep
> drove **every functional module to a PASS** (Targeting, Lists, Creature-Spy, Healing,
> Attack/Aimbot, Looting, Cavebot walk, NavNet, Alarm, Proxy, Extras, Icons, USkin,
> CiroScript VM/Hotkeys). The RT column below is updated to match; the only tabs still ⏳
> are the **UI editor/wizard popups** (their `RT_DIALOG` geometry is the one remaining
> capture). See docs/39 for the per-module evidence + the methods that got there.

Legend — Doc: ✅ dedicated / 🟡 covered within a broader doc. RT (runtime): ✅ behavioural
PASS (see docs/39) / ▫ covered by another module's PASS / ⏳ pending (UI-geometry only).

| Tab | Class | DialogProc | Doc | Runtime test (exercise → observable) | RT |
|---|---|---|---|---|---|
| Healing | TBOTDLGE | `dlgProc_Healer 0x1001E3E5` | [15](15-healer-engine.md) ✅ | set HP threshold, take damage → heal spell/potion cast (send hook + HP mirror `0x1005F7D1`) | ✅ heal fired: threshold `g_10134E66` above HP → `g_10080BA6` 0→1, 15-byte cast (docs/39) |
| Aimbot | TBOTDLGI / DLG7 | `dlgProc_AutoAim 0x10003146` | [26](26-aimbot-combo.md) ✅ | enable + enemy on screen → best-square scan + attack packet | ✅ rides the Attack PASS — shared `pickAttackTarget` + `sub_1003A60A` emitter (docs/39) |
| Targeting | TBOTDLGR | `dlgProc_Targeting 0x1001A715` | [16](16-targeting-engine.md) ✅ | define monster, spawn it → recolour + attack | ✅ name-match recolour live (outfit 106); attack via `sub_1003A60A` (docs/39) |
| Cavebot | TBOTDLGS | `dlgProc_Cavebot 0x10019751` | [17](17-cavebot-walker.md) ✅ | load `.elfc`, enable → walker follows waypoints (`g_100f0e42`, map-click send) | ✅ bot walked the char — route + arbiter hook `0x459F30` + pos sync (docs/39) |
| Hotkeys | TBOTDLGD | `dlgProc_Hotkeys 0x10007360` | [24](24-hotkeys-alarms.md) ✅ | bind key→command, press → CiroScript runs (record `byte_100FAA3C`) | ✅ external verb dispatch executes via `registerCommands_table` (docs/39) |
| Shortkeys | TBOTDLGP | `dlgProc_Shortkeys 0x10006D3B` | [24](24-hotkeys-alarms.md) 🟡 | type trigger text → command fires (table `byte_10106B02`) | ▫ same dispatch path as Hotkeys (VM PASS, docs/39) |
| Lists (Friends/Enemies) | TBOTDLGH | `dlgProc_FriendsEnemies 0x1001E313` | [34](34-tabs-lists-extras-hud-spy-links.md) ✅ | add enemy name → red outfit paint on that player | ✅ enemy name-match recoloured Dragons' outfit to 96 live (docs/39) |
| HUD On-Screen | TBOTDLGJ | `dlgProc_HudOnScreenInfo 0x10007B55` | [34](34-tabs-lists-extras-hud-spy-links.md) ✅ | enable overlays → ping/exp/timers drawn (draw hook `0x4F30C0`) | ✅ render path proven via the Icons PASS (docs/39) |
| Creature Spy | TBOTDLGA | `dlgProc_HudCreatureList 0x10006BCE` | [34](34-tabs-lists-extras-hud-spy-links.md) ✅ | open window → live creature rows from shadow table (stride 168) | ✅ full battle-list scan live — the recolours prove it (docs/39) |
| Extras (Graphics) | TBOTDLGF | `dlgProc_GraphicsTweaks 0x10007EC4` | [34](34-tabs-lists-extras-hud-spy-links.md) ✅ | toggle World View → `g_100ee8bb` set + `sub_10039c81`; toggle FPS tweak → GUI 10fps | ✅ World View flag `g_100ee8bb` 0→1 + apply ran, 2 boots (docs/39) |
| Icons | TBOTDLGW | `dlgProc_SkinEditor 0x1001B8BE` | [32](32-icons-tab.md) ✅ | define icon → `drawCustomHudElements` renders; click → `hitTestHudButtons` → command | ✅ defined a runtime icon; renderer drew it at the exact offsets set (docs/33) |
| NavNet | TBOTDLGC | `dlgProc_NavNet 0x1001E7C3` | [18](18-navnet-codec.md) ✅ | connect navserv → position broadcast (`sendNavPositionUpdate 0x1003FFDF`) | ✅ live 11-byte opcode-2 position packet sent to a dummy peer (docs/39) |
| Links | TBOTDLGB | `dlgProc_LinksNavNet 0x1001EB33` | [34](34-tabs-lists-extras-hud-spy-links.md) ✅ | Run Links → listen socket up; Set-for-client (logged off) → client patches at `0x4F36xx` | ▫ = Proxy server `0x10002041` + relay config; socket covered by Proxy (docs/39) |
| Proxy | TBOTDLGQ | `dlgProc_LinksProxy 0x1001EF0C` | [09](09-packet-proxy.md) ✅ | run proxy → watcher/controller listen socket (`byte_102898CD`) | ✅ live LISTEN socket (`0.0.0.0:50606`), 2 boots (docs/39) |
| Skin | TBOTDLGV | `dlgProc_Skin 0x100086B3` | [05](05-ui-init-framework.md) 🟡 | pick skin → USkin applies `.msstyles`; `elfbot.ini LastSkin` written | ✅ USkin init in-client, skin dialog rendered live (docs/38) |
| Command wizards | TBOTDLGK/L/M/N/O | `0x1001E1D9`/`0x1001DF05`/`0x1001D5FD`/`0x1001D2E0`/`0x1001D151` | [10](10-feature-subsystems.md) 🟡 | open from a hotkey edit → assembles CiroScript string joined by ` \| ` | ⏳ |
| Targeting editor | TBOTDLGT | `dlgProc_TargetingEditor 0x1000802F` | [16](16-targeting-engine.md) 🟡 | open per-target editor → edits 48-byte record `unk_101E6EA8` | ⏳ |
| Script editor | TBOTDLGU | `dlgProc_ScriptEditor 0x100083B6` | [10](10-feature-subsystems.md) 🟡 | open (mode 0–4) → shared editor loads/saves the mode's script | ⏳ |

## Documentation: complete

Every tab now has a doc home (dedicated ✅ or within a broader engine doc 🟡). The
wizard/editor popups (K/L/M/N/O/T/U) are indexed in docs/10.

### Wizard-popup geometry (B) — investigated live; capture path narrowed

Their control geometry cannot be lifted statically: `elfbot.dll` is Armadillo and its
resource directory (`IMAGE_DIRECTORY_ENTRY_RESOURCE`) is a **16-byte stub** — the real
`RT_DIALOG` templates sit in the encrypted `.aqfu` section (`0x3CB000`, 0xB0000).
A live injection pass this session (Frida, `elfbot.dll` mapped into a 32-bit WOW64
host — note it is an **x86** DLL, so a 32-bit host is required; it loads at its
preferred base `0x10000000`) pinned down what does *not* work and what remains:

- **`FindResourceW`/resource walk after load — fails.** With the module mapped, a
  scan of ids 1–4000 for `RT_DIALOG` returned **zero**, and a memory scan of the whole
  module for the wide class strings `TBOTDLG*` returned **zero** (only the 23 ASCII
  `TBOTDLG?` class names from the `RegisterClassEx` table at `0x100428de…0x1004485c`
  are present). So Armadillo does **not** restore the PE resource directory in the
  mapped image — the templates are decrypted only **transiently, at dialog-creation
  time**, through the bot's own (IAT-hooked) resource path.
- **Booting `EcInit` in a throwaway host — crashes it.** `EcInit(0)` on a non-Tibia
  host tears the process down: `EcInit` is Tibia-coupled (it installs the client
  inline hooks at the `0x400000`-based Tibia addresses, which are not that host).

So the viable capture is one of: **(a)** inject into a real in-game Tibia client and,
per wizard, either `GetWindowRect` the child controls (the docs/29 live method — it
only covered the always-visible panels, not these on-demand popups) or hook
`CreateWindowExW/A` (controls arrive as pixel client-rects) while the popup opens; or
**(b)** a targeted harness that calls `CreateDialogParam` for each wizard id directly
(so Armadillo decrypts that one template) with `CreateWindowExW` hooked, *without*
running `EcInit`'s client-hook path. Both need a live client — which **is** available: the
same genuine 8.60 client + local Fir3element TFS that the
[docs/39](39-module-runtime-report.md) behavioural sweep ran on. So (a) is runnable. The
reason the geometry is still uncaptured is that the sweep drove every module through
**memory + the bot's own code paths**, never the config **dialogs** — the genuine client's
assertion handler trips when those on-demand popups are driven, which is why the module
tests avoided them. So the wizard/editor popup geometry is the one remaining artefact,
pending a dedicated `CreateWindowExW`-hook (or `CreateDialogParam`) pass that opens each
popup live.

## Runtime tests: harness + method

Each RT reuses the [docs/33](33-runtime-ingame-validation.md) setup: inject
`elfbot.dll` into the in-game client, install the client hooks, boot the tick loop,
then exercise the tab's feature and confirm the documented global/packet/render
effect via Frida (memory read, `send`/`recv` hook, or the draw path).

### Foundation — confirmed live in-game (docs/33)

- ✅ **Reproducible stack** — TFS 0.4 8.60 + RSA/hosts-patched client + scripted
  session-1 login → char in the world (`inGame==31`, `7172` connection).
- ✅ **Injection + client hooks** — `elfbot.dll` maps (rebase by `module.base` — it
  relocates), hooks patch `0x45ACD6`/`0x4F30C0`/`0x5AB5D4` to the relocated handlers.
- ✅ **Engine running** — `botMainTickLoop` booted; the bot's **player-state shadow
  equals the live client** (HP/mana/pos), proving the tick loop reads the game.

Because the shared tick loop drives every subsystem, the ✅ foundation means each
tab's engine *runs*; what each per-tab RT still needs is the **scenario** (a creature
to target/attack, a corpse to loot, a route to walk, chat to parse). Those are ⏳:
the packet-fed shadow creature/battle-list stayed empty (temple spawn, no creatures
on screen), and the `0x45ACD6` parser hook is a specific-opcode dispatch that
movement packets don't hit. Scenario-driven tab tests are the remaining capture,
taken opportunistically when a client is up and the re-* MCP tunnel is healthy
(retried patiently across its intermittent 502s).
