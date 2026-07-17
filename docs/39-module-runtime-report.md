# Per-module runtime report

Runtime status of **every ElfBot module**, consolidated from the two in-game
injection runs — [docs/33](33-runtime-ingame-validation.md) (OT client, direct
`LoadLibrary`) and [docs/38](38-runtime-e2e-genuine-client.md) (genuine Cip 8.60
client on a local Fir3element TFS 0.4, injected by the stock `loader.exe`) — plus the
static engine docs. Each row: the module, its tick/handler entry, the runtime
observation, and the evidence source.

**Legend** — ✅ confirmed live in-game · 🟡 engine confirmed ticking live, behaviour
gated on a scenario (a creature / low HP / a route / a corpse) · ⏳ RE complete,
runtime capture pending a scenario + a stable lab.

## Core — injection, hooks, engine

| Module | Entry | Runtime | Ev |
|---|---|---|---|
| **Injection (loader.exe)** | madCodeHook → `EcInit` | ✅ `loader.exe` maps `elfload`/`USkin`/`elfbot` into the genuine in-world client, **no `err=126`** once the four files are co-located; `EcInit` runs (its `USkin` skin dialog renders in-client) | 38 |
| **Client hooks** | `0x45ACD6` / `0x4F30C0` / `0x5AB5D4` | ✅ patched **byte-for-byte** to the relocated handlers (`0x5AB5D4 = 0x07D61A96` = `hook_captureRenderCtx` rebased; `0x4F30C0 = e9…` JMP; `0x45ACD6` parser rel32) | 33, 38 |
| **Engine tick loop** | `botMainTickLoop 0x100227BD` | ✅ booted (guarded thread); drives all subsystem ticks below | 33, 38 |

## Subsystem engines (dispatched each tick)

| Module | Tick fn | Runtime | Ev |
|---|---|---|---|
| **Snapshot / player-state** | `0x10024FAE` | ✅ shadow **== live in-world player** — HP `[0x63FE94]==E(0x1005F7D1)`, pos `[0x64F600]/[0x64F604]==E(0x10052770)/E(0x1005276C)`, with `[0x64A9C0]==31` (in-world). Ticks per-tick | 33, 38 |
| **Healing** (heal + attack cast) | `0x1002492D` / `0x100235E8` | 🟡 both tick ~10/s live; a cast needs a low-HP scenario ([15](15-healer-engine.md)) | 33 |
| **Targeting** | `0x10023893` | ✅ **behavioural PASS** — with a normal char `Tester` at a Dragon Lord spawn, writing `"Dragon Lord"` into the targeting name-list (`g_100638A8`) + enabling (`g_100F0D3B`=1, HUD-colour `g_100F94C7`=1, write-to-client `g_10135278`=1) made `scanBattleListStatusTick` **match + recolour the matched creature live**: the on-screen `Dragon Lord` battle-list record's outfit-head byte (`+100`) became **106** (docs/16 matcher-A colour) while three non-matching `Dragon` records stayed `0` ([16](16-targeting-engine.md), [36](36-scheduling-and-flags.md)) | 39 |
| **Cavebot / CiroScript** | `0x1002BC68` | 🟡 script tick runs per-tick live; enable = `g_100F0E42`; a walk needs loaded waypoints ([17](17-cavebot-walker.md)) | 33 |
| **Creature Spy / battle-list** | `0x10023A8F` | 🟡 battle-scan ticks ~10/s live; the shadow creature table (`E(0x10077175)`, stride 168) populates only with creatures on screen ([34](34-tabs-lists-extras-hud-spy-links.md)) | 33 |
| **HUD on-screen** | `0x10023E42` | 🟡 exp-window tick runs live; on-screen draw needs the client render path ([34](34-tabs-lists-extras-hud-spy-links.md)) | 33 |
| **Icons / HUD render** | `0x1003E7AA` | ✅ **behavioural PASS** — a runtime-defined icon rendered at the exact offsets set, active/inactive block selection working ([32](32-icons-tab.md)) | 33 |
| **NavNet** | `0x1003FFDF` | 🟡 client + 11-byte encoder RE'd, harness up; `send` gated on the full connect/handshake ([18](18-navnet-codec.md), [04](04-navnet-server.md)) | 33 |

## Feature modules (CiroScript-driven / UI)

| Module | Handler | Runtime | Ev |
|---|---|---|---|
| **CiroScript VM** | 422 cmds, 3-table perfect hash | ✅ dispatch + `auto`/`wait`/`end` scheduler arrays pinned byte-exact ([11](11-ciroscript-engine.md), [36](36-scheduling-and-flags.md)); per-command runs via a hotkey/label | 36 |
| **Hotkeys / Shortkeys / Alarms** | `0x10007360` / `0x10006D3B` | ⏳ bind → CiroScript run; RE complete ([24](24-hotkeys-alarms.md)) | — |
| **Aimbot / combo** | `0x10003146` | ⏳ square-scan + combo; needs an enemy on screen ([26](26-aimbot-combo.md)) | — |
| **Looting** | corpse scan / depot SM | ⏳ needs a corpse (kill a creature) ([23](23-looting-engine.md)) | — |
| **Lists (Friends/Enemies)** | `0x1001E313` | ⏳ colouring/markers on named players ([34](34-tabs-lists-extras-hud-spy-links.md)) | — |
| **Extras (Graphics)** | `0x10007EC4` | ⏳ World View sets `g_100EE8BB` ([34](34-tabs-lists-extras-hud-spy-links.md)) | — |
| **Skin (USkin)** | `EcInit` load / `dlgProc_Skin` | ✅ USkin initialised in-client (skin-selector dialog rendered live); `.msstyles` from `Skins\` ([37](37-uskin-and-support-section.md)) | 38 |
| **Proxy** | `0x1001EF0C` | ⏳ watcher/controller listen socket ([09](09-packet-proxy.md)) | — |
| **Links** | `0x1001EB33` | ⏳ relay + client `0x4F36xx` patch ([34](34-tabs-lists-extras-hud-spy-links.md)) | — |

## God-created scenario — normal char under attack (behavioural bed)

Because a God char takes no monster damage, a **normal char `Tester`** (group 1,
level 120, 15000 HP, backpack + 200 health potions + a weapon) was created via SQL by
copying the Godbot row and overriding stats (Godbot moved to account 2 so account 1
logs `Tester` deterministically), spawned at the Dragon Lord spawn. In-world it is
**genuinely under attack** — client chat *"You lose 76 hitpoints due to an attack by a
dragon lord"*, HP falling `15000 → 14257 → 11663 → 6465`, and the rebased elfbot
**shadow HP tracks it exactly each tick**. This is the damage/creature bed the
behavioural module tests run against. The **Targeting** recolor (below) was captured
in this scenario — the matched `Dragon Lord`'s name/outfit is recoloured on-screen
live.

## Full control panel rendered live (every module UI present)

A second live run (fresh boot, elfbot relocated to `0x082B0000`) captured the whole
**elfbot control panel rendered inside the injected client** — the `CiroScript.com –
Startup – 00 exp/hour` window with a button for **every module**:

```
Healing   Aimbot     Lists       HUD          1 2 3 4 5
Extras    Hotkeys    Shortkeys   Reconnect    Save  Custom
Cavebot   Navigation Links       Creature Spy Load  Help
Targeting Proxy      Icons                    OK
```

So `EcInit`'s dialog framework and **every module's UI are live in-client** — each
button opens that module's config dialog ([05](05-ui-init-framework.md),
[10](10-feature-subsystems.md)). Note the retrieved `Tibia.exe` is a **debug build**
(it carries `assert` strings like `Password!=NULL`): a malformed `/`-command typed
into chat tripped a `Debug Assertion` and closed the client — normal gameplay input
(clicking, walking) does not, but it makes extended behavioural runs on this exact
binary fragile.

## What is fully confirmed vs. gated

**Live-confirmed (✅):** injection via the real loader, all three client hooks
byte-for-byte, the engine tick loop (its `g_10084BFF` ms-delta advances live), the
player-state snapshot mirroring the **live in-world player** (HP/mana `2000/2000` on
the God char `Godbot` at the Dragon Lord spawn), **every module's UI rendered live
in-client** (the control panel above), Icons render, and USkin init — on the genuine
8.60 client + local Fir3element server.

**Engine-live, behaviour-gated (🟡):** Healing, Targeting, Cavebot, Creature Spy, HUD
and NavNet engines are all **confirmed ticking live** on their documented schedules;
their remaining behavioural captures each need a specific scenario — a creature on
screen (Targeting attack / Creature-Spy rows / the `0x45ACD6` parser feeding the
shadow creature table), a low-HP moment (Healing cast), loaded waypoints (Cavebot
walk), a corpse (Looting), or a live `navserv` (NavNet send). The intended setup is a
God char at a monster spawn (Godbot was relocated to a Dragon Lord spawn at
`149,574,2`) plus `/c`-summoned creatures; those scenario runs are the remaining
capture, taken when the shared RE-lab MCP link is healthy (it drops frequently —
Cloudflare 502/524 and full frida disconnects).
