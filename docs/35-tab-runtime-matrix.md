# Tab coverage & runtime-test matrix

Every ElfBot tab, its dialog proc, its documentation, and its runtime test. This is
the tracker for "document each tab + test in runtime". Runtime tests run against the
in-game harness of [docs/33](33-runtime-ingame-validation.md) (genuine client on a
local TFS 0.4 8.60); the observable is what a Frida/RPM/socket probe confirms.

Legend — Doc: ✅ dedicated / 🟡 covered within a broader doc. RT (runtime): ✅ observed
live / 🟡 partially observed / ⏳ pending a stable in-game session.

| Tab | Class | DialogProc | Doc | Runtime test (exercise → observable) | RT |
|---|---|---|---|---|---|
| Healing | TBOTDLGE | `dlgProc_Healer 0x1001E3E5` | [15](15-healer-engine.md) ✅ | set HP threshold, take damage → heal spell/potion cast (send hook + HP mirror `0x1005F7D1`) | 🟡 engine ticks live (`0x1002492D`); cast pending low-HP scenario |
| Aimbot | TBOTDLGI / DLG7 | `dlgProc_AutoAim 0x10003146` | [26](26-aimbot-combo.md) ✅ | enable + enemy on screen → best-square scan + attack packet | ⏳ |
| Targeting | TBOTDLGR | `dlgProc_Targeting 0x1001A715` | [16](16-targeting-engine.md) ✅ | define monster, spawn it → `g_100f0e20` set to creature ptr + attack | 🟡 scan ticks live (`0x10023893`); attack pending a creature on screen |
| Cavebot | TBOTDLGS | `dlgProc_Cavebot 0x10019751` | [17](17-cavebot-walker.md) ✅ | load `.elfc`, enable → walker follows waypoints (`g_100f0e42`, map-click send) | 🟡 script tick runs per-tick live (`0x1002BC68`); walk pending waypoints |
| Hotkeys | TBOTDLGD | `dlgProc_Hotkeys 0x10007360` | [24](24-hotkeys-alarms.md) ✅ | bind key→command, press → CiroScript runs (record `byte_100FAA3C`) | ⏳ |
| Shortkeys | TBOTDLGP | `dlgProc_Shortkeys 0x10006D3B` | [24](24-hotkeys-alarms.md) 🟡 | type trigger text → command fires (table `byte_10106B02`) | ⏳ |
| Lists (Friends/Enemies) | TBOTDLGH | `dlgProc_FriendsEnemies 0x1001E313` | [34](34-tabs-lists-extras-hud-spy-links.md) ✅ | add enemy name → red **E** marker + red outfit paint on that player | ⏳ |
| HUD On-Screen | TBOTDLGJ | `dlgProc_HudOnScreenInfo 0x10007B55` | [34](34-tabs-lists-extras-hud-spy-links.md) ✅ | enable overlays → ping/exp/timers drawn (draw hook `0x4F30C0`) | 🟡 exp-window tick runs live (`0x10023E42`); on-screen draw pending client render |
| Creature Spy | TBOTDLGA | `dlgProc_HudCreatureList 0x10006BCE` | [34](34-tabs-lists-extras-hud-spy-links.md) ✅ | open window → live creature rows from shadow table (stride 168) | 🟡 battle scan ticks live (`0x10023A8F`); rows pending creatures on screen |
| Extras (Graphics) | TBOTDLGF | `dlgProc_GraphicsTweaks 0x10007EC4` | [34](34-tabs-lists-extras-hud-spy-links.md) ✅ | toggle World View → `g_100ee8bb` set + `sub_10039c81`; toggle FPS tweak → GUI 10fps | ⏳ |
| Icons | TBOTDLGW | `dlgProc_SkinEditor 0x1001B8BE` | [32](32-icons-tab.md) ✅ | define icon → `drawCustomHudElements` renders; click → `hitTestHudButtons` → command | ✅ defined a runtime icon; renderer drew it at the exact offsets set (docs/33) |
| NavNet | TBOTDLGC | `dlgProc_NavNet 0x1001E7C3` | [18](18-navnet-codec.md) ✅ | connect navserv:7175 → position broadcast (`sendNavPositionUpdate 0x1003FFDF`) | 🟡 client + encoder RE'd, harness set up; send gated on connect handshake (docs/33) |
| Links | TBOTDLGB | `dlgProc_LinksNavNet 0x1001EB33` | [34](34-tabs-lists-extras-hud-spy-links.md) ✅ | Run Links → listen socket up; Set-for-client (logged off) → client patches at `0x4F36xx` | ⏳ |
| Proxy | TBOTDLGQ | `dlgProc_LinksProxy 0x1001EF0C` | [09](09-packet-proxy.md) ✅ | run proxy → watcher/controller listen socket (`byte_102898CD`) | ⏳ |
| Skin | TBOTDLGV | `dlgProc_Skin 0x100086B3` | [05](05-ui-init-framework.md) 🟡 | pick skin → USkin applies `.msstyles`; `elfbot.ini LastSkin` written | ⏳ |
| Command wizards | TBOTDLGK/L/M/N/O | `0x1001E1D9`/`0x1001DF05`/`0x1001D5FD`/`0x1001D2E0`/`0x1001D151` | [10](10-feature-subsystems.md) 🟡 | open from a hotkey edit → assembles CiroScript string joined by ` \| ` | ⏳ |
| Targeting editor | TBOTDLGT | `dlgProc_TargetingEditor 0x1000802F` | [16](16-targeting-engine.md) 🟡 | open per-target editor → edits 48-byte record `unk_101E6EA8` | ⏳ |
| Script editor | TBOTDLGU | `dlgProc_ScriptEditor 0x100083B6` | [10](10-feature-subsystems.md) 🟡 | open (mode 0–4) → shared editor loads/saves the mode's script | ⏳ |

## Documentation: complete

Every tab now has a doc home (dedicated ✅ or within a broader engine doc 🟡). The
wizard/editor popups (K/L/M/N/O/T/U) are indexed in docs/10.

### Wizard-popup geometry (B) — why it is runtime-gated

Their exact control geometry cannot be lifted statically: `elfbot.dll` is Armadillo
and its resource directory (`IMAGE_DIRECTORY_ENTRY_RESOURCE`) is a **16-byte stub** —
the real `RT_DIALOG` templates live inside the encrypted `.aqfu` section
(`0x3CB000`, 0xB0000) and are only rebuilt in memory after the packer runs. So the
authoritative geometry source is one of, both needing the bot mapped + unpacked in a
live process:

- read the **in-memory `RT_DIALOG` templates** (the `DLGTEMPLATE`/`DLGITEMTEMPLATE`
  x/y/cx/cy in dialog units) once Armadillo has decrypted resources, or
- open each wizard and `GetWindowRect` its child controls (the docs/29 live-capture
  method, which only covered the always-visible panels, not these on-demand popups).

The general (docs/29) panels were captured this way; the seven popups are the
remaining live capture, gated on the runtime stack (which was wiped from the lab VM
on re-image — the docs/33 stack is not currently resident).

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
