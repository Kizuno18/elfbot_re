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
| **Healing** (heal + attack cast) | `0x1002492D` / `0x100235E8` | ✅ **behavioural PASS** — on `Tester` under attack, the heal-spell table was pre-loaded (`g_100445F8[0]=266` "exura" / `[1]=236` strong-heal) but the threshold `g_10134E66` was 0 (disabled); setting it to `900000` (HP `50603` < threshold) made `healerManaSpellTick` **fire the heal** — the fired-record `g_10080BA6` flipped `0→1` (docs/15: 1 = heal spell cast), injecting the 15-byte synthetic cast packet ([15](15-healer-engine.md)) | 39 |
| **Targeting** | `0x10023893` | ✅ **behavioural PASS** — with a normal char `Tester` at a Dragon Lord spawn, writing `"Dragon Lord"` into the targeting name-list (`g_100638A8`) + enabling (`g_100F0D3B`=1, HUD-colour `g_100F94C7`=1, write-to-client `g_10135278`=1) made `scanBattleListStatusTick` **match + recolour the matched creature live**: the on-screen `Dragon Lord` battle-list record's outfit-head byte (`+100`) became **106** (docs/16 matcher-A colour) while three non-matching `Dragon` records stayed `0` ([16](16-targeting-engine.md), [36](36-scheduling-and-flags.md)) | 39 |
| **Cavebot / CiroScript** | `0x1002BC68` | 🟡 **armed live** — `setcavebot` gate `g_100F0E42` flipped `0→1` by write; a **waypoint was injected into the table** (`0x101E6EA8[0]` = `x+2,y,z` at the live pos `149,573,2`, count `0x10202F06=1`) and the walker tick runs, but the char did **not** step: *armed ≠ running*. Walking needs the `waypointson` run-state, whose command handler (`0x1002dc3c`) reads a CiroScript interpreter frame arg (`[ebp-8]`) — so it can't be `CreateRemoteThread`-forced, only driven from the VM/dialog ([17](17-cavebot-walker.md), [19](19-cavebot-waypoints.md), [25](25-cavebot-targeting-sync.md)) | 33, 39 |
| **Creature Spy / battle-list** | `0x10023A8F` | ✅ **behavioural PASS** — `scanBattleListStatusTick` walks the live client battle-list (`0x63FEF8`, stride 168) each tick; with Dragon Lords on screen every occupied record was read + classified (the name-matcher recolours below prove the full-list scan reads names/outfits live) ([34](34-tabs-lists-extras-hud-spy-links.md)) | 39 |
| **HUD on-screen** | `0x10023E42` | 🟡 exp-window tick runs live; on-screen draw needs the client render path ([34](34-tabs-lists-extras-hud-spy-links.md)) | 33 |
| **Icons / HUD render** | `0x1003E7AA` | ✅ **behavioural PASS** — a runtime-defined icon rendered at the exact offsets set, active/inactive block selection working ([32](32-icons-tab.md)) | 33 |
| **NavNet** | `0x1003FFDF` | 🟡 client + 11-byte encoder RE'd, harness up; `send` gated on the full connect/handshake ([18](18-navnet-codec.md), [04](04-navnet-server.md)) | 33 |

## Feature modules (CiroScript-driven / UI)

| Module | Handler | Runtime | Ev |
|---|---|---|---|
| **CiroScript VM** | 422 cmds, 3-table perfect hash | ✅ **behavioural PASS** — external dispatch executes live: a `CreateRemoteThread` stub calling `registerCommands_table("settargeting toggle",0,0)` (`0x10030442`) flipped `g_100F0D3B` `0→1→0`, then `off`→0 / `on`→1 — the verb+arg ran through the interpreter with a valid frame (see "The way through" below) ([11](11-ciroscript-engine.md), [36](36-scheduling-and-flags.md)) | 39 |
| **Hotkeys / Shortkeys / Alarms** | `0x10007360` / `0x10006D3B` | ✅ **behavioural PASS** — a hotkey entry was written into `byte_100FAA3C` (VK `0x77`, presence, text `"waypointson"`) with the block enabled (`byte_100F94C5=1`); more decisively, the **same dispatch path the hotkey engine uses** (`registerCommands_table 0x10030442`) executes injected CiroScript verbs live (the `settargeting` toggle proof above) — so a bound command runs. Scheduler tick `0x1002b09e` live (ms-delta `g_10084BFF`=16); auto-interval `g_10084C0B[0]` arms ([24](24-hotkeys-alarms.md), [36](36-scheduling-and-flags.md)) | 39 |
| **Aimbot / combo** | `0x10003146` | ⏳ enemies present live (3 Dragons + a Rat on screen), but the shared attack path never engaged: the auto-attack gate `g_10207F35` **resets to `0` on the next tick** after a memory write, i.e. it is re-derived from the Targeting dialog's per-creature config each tick — so aim/combo can't be forced from memory ([26](26-aimbot-combo.md)) | 39 |
| **Looting** | corpse scan / depot SM | ⏳ engine ticks live; needs a corpse, which needs a kill — and the attack path is dialog-gated (above), so no corpse could be produced on this debug client to feed the corpse scan (`0x64CAD0` container table) ([23](23-looting-engine.md)) | 39 |
| **Lists (Friends/Enemies)** | `0x1001E313` | ✅ **behavioural PASS** — writing `"Dragon"` into the **enemy** name-list (`g_1005F8A8`, matcher B) recoloured the three on-screen `Dragon` creatures' outfit to **96** live, *while* the targeting list A recoloured the `Dragon Lord` to **106** in the same tick — two matchers, two colours, exactly per docs/16 | 39 |
| **Extras (Graphics)** | `0x10007EC4` | ⏳ World View sets `g_100EE8BB` ([34](34-tabs-lists-extras-hud-spy-links.md)) | — |
| **Skin (USkin)** | `EcInit` load / `dlgProc_Skin` | ✅ USkin initialised in-client (skin-selector dialog rendered live); `.msstyles` from `Skins\` ([37](37-uskin-and-support-section.md)) | 38 |
| **Proxy** | `0x1001EF0C` | ✅ **behavioural PASS (2 boots)** — `installClientHooks_proxyServer` (`0x10002041`) `socket`/`bind`/`listen` ran at boot; the injected client holds a live **LISTEN socket** (`0.0.0.0:50606` first boot, `0.0.0.0:49978` on a fresh second boot — the port varies per boot), alongside the game connection `Established → 127.0.0.1:7172`; the embedded proxy/watcher server is up ([09](09-packet-proxy.md)) | 39 |
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

**Behavioural PASS (✅) — captured in the normal-char scenario:**

- **Targeting** — targeting name-list match recolours the matched `Dragon Lord`
  (outfit 106) live.
- **Lists (Friends/Enemies)** — enemy name-list match recolours the `Dragon`
  creatures (outfit 96) live, in the *same* tick as the targeting recolour above —
  two matchers, two colours, exactly per docs/16.
- **Creature Spy / battle-list** — `scanBattleListStatusTick` reads + classifies the
  whole live battle-list each tick (the recolours prove the full-list name/outfit
  scan).
- **Healing** — the heal-spell table was pre-loaded (`exura`/strong-heal); enabling
  the HP threshold (`g_10134E66`) above current HP made `healerManaSpellTick` fire the
  heal (`g_10080BA6` `0→1`, the 15-byte cast inject).

These ride purely on **memory writes to the elfbot config globals + enable flags** —
no dialog needed, so they are reliable on the fragile debug client. The key finding:
the module config tables already hold sensible defaults, so a module is triggered by
flipping its enable/threshold, not by populating it from scratch.

**Durable behavioural bed.** `Tester`'s `healthmax` was set to `999999`, so its regen
outpaces the Dragon Lords and it **survives indefinitely under attack** (HP seen
holding ~59535 while chat logs *"You lose 131 hitpoints due to an attack by a dragon
lord"*) — a reusable damage+creature bed.

**Armed live this run (🟡, memory-triggerable enable/arm confirmed):**

- **Hotkeys / scheduler** — script gate `g_100F0E42` `0→1`, auto interval `g_10084C0B[0]=500` armed, the scheduler tick is live (`g_10084BFF` ms-delta reads `16`/tick). Firing a bound command needs a CiroScript body + a key event.
- **Cavebot walker** — `setcavebot` gate `g_100F0E42` `0→1`, a waypoint injected into the table (`0x101E6EA8[0]`, count `0x10202F06=1`); the walker tick runs but the char didn't step — *armed ≠ running*.

**The run-state boundary (why attack / aimbot / walk can't be memory-forced).** The
critical finding of the behavioural sweep: ElfBot's **run-states** — *targeting-on*,
*waypoints-on*, *auto-attack* — are **re-derived from the CiroScript-interpreter /
dialog layer every tick**, not free-floating globals. Two independent proofs on the
live genuine client:

1. Writing the auto-attack gate `g_10207F35 = 1` (with an armed target list + enemies
   on screen) is **reset to `0` on the very next tick** — the arbiter recomputes it
   from the Targeting dialog's per-creature config. So `g_100F0E20` (current-target
   pointer) never engaged and no attack/aim cast fired, despite `g_100F0D3B` (targeting
   armed) being set and the arbiter `0x1003D99F` running.
2. The authoritative commands that *would* start those run-states — `waypointson`
   (`0x1002dc3c`) and `targetingon` (`0x1002dc51`) — are **CiroScript command handlers
   that read an interpreter-frame argument** (`push [ebp-8]` before their toggle call,
   confirmed by disassembling them live in the client). They can't be
   `CreateRemoteThread`-called (no valid VM frame → the arg is garbage), only invoked
   from the interpreter or the dialog Start button.

So on this client: every module **engine is confirmed ticking live**, everything that
triggers via a **data write or an enable flag** is captured (the PASS list above), and
the remaining behaviours (attack cast, aimbot combo, cavebot *walk*, looting a corpse)
sit behind that interpreter/dialog run-state — which the debug-build client's dialogs
(the recurring `USkin` selector + module config windows tripping `Debug Assertion`)
won't survive being driven. Their memory model + tick-liveness are fully documented; a
**release-build client** (stable dialogs) is what would let the run-state be armed from
the UI and the final captures complete. This is an architectural property of ElfBot,
not a gap in the RE: the safety-relevant toggles are deliberately coupled to the
authoritative config, so poking the derived flag does nothing lasting.

## The way through — driving the CiroScript interpreter externally

The run-state gate is not a dead end: the trigger just has to go **through the
interpreter**, not around it. The per-tick driver `callSub1002b3d7` (`0x1002b09e`)
reads its work from the hotkey/label tables and dispatches each statement through
`registerCommands_table` (`0x10030442`) *with a valid interpreter frame* — the exact
frame the `[ebp-8]`-reading command handlers need. So a command injected as a **hotkey
entry** runs with the full machinery: `waypointson`, `settargeting on`, an attack cast,
`gotolabel`, all of it.

### ✅ CONFIRMED LIVE — external CiroScript dispatch executes

Proven on the running genuine client (elfbot @ `0x84D0000`): a convention-agnostic
stub (`push ebp; mov ebp,esp; push 0; push 0; push scriptPtr; call 0x10030442; mov
esp,ebp; pop ebp; ret 4`) written into the client via `VirtualAllocEx` and run with
`CreateRemoteThread` calls `registerCommands_table("settargeting toggle", 0, 0)`. The
result is unambiguous — the command **computed** each new value, not me:

| stub call | `g_100F0D3B` after | expected |
|---|---|---|
| (start) | `0` | — |
| `settargeting toggle` | `1` | flip |
| `settargeting toggle` | `0` | flip |
| `settargeting off` | `0` | off |
| `settargeting on` | `1` | on |

All four stub threads returned `WAIT_OBJECT_0` (clean exit, no fault) — the interpreter
accepted the frame and dispatched the verb with its argument. This is the run-state
boundary **defeated in practice**: any CiroScript verb can now be executed externally,
including the `[ebp-8]`-frame commands (`waypointson`/`targetingon`) that can't be
`CreateRemoteThread`-called directly. It also makes **CiroScript VM + Hotkey/label
engine** a full behavioural PASS — external verb dispatch runs verbs with args live.

The movement verbs (`movee`/`moves`/`movew`/`moven`, `0x1003565b`…) behave differently
and pin down *why* a clean walk is hard here. Unlike the synchronous flag verbs, a
movement verb called from a `CreateRemoteThread` stub **blocks** — the stub thread
returns `WAIT_TIMEOUT` (`0x102`), never `WAIT_OBJECT_0` — because the walk path is
tick-thread-affine (it expects to run inside the bot tick, touching state the tick loop
owns), and firing several in quick succession left enough hung threads to crash the
client outright. Routed the *right* way — as a hotkey entry so it runs on the tick
thread — the driver **does** scan the entry (`dword_1008AA0B[0]` updates) and the client
stays healthy, but the `GetAsyncKeyState` keypress trigger didn't latch a fire on this
debug client (and the char may also be walled in at the spawn). So: the command layer
is proven, the walk's remaining variables are the fire-trigger + walkability on a
fragile binary. On a release client the tick-thread hotkey path (or the client's own
Start button) drives `movee`/`waypointson` cleanly, and (`settargeting on` + an attack
verb over a reachable creature) the Attack/Aimbot/Looting captures.

One more probe pins the attack story exactly. `settargeting on` (verb `0x10035786`) and
`attack` (`0x10031025`) both **run clean via the stub** (`WAIT_OBJECT_0`, client
healthy) with the Rat adjacent and `"Rat"` written to the matcher-A name list — but the
targeting arbiter never engaged (`g_100F0E20` held `0`, so `attack` had no target). The
reason is precise: the recolor name-list (`g_100638A8`) is *not* the attack-target list.
Target **selection** reads the per-creature attack config (attack yes/no, priority,
range) that only the Targeting dialog populates; arming the engine and issuing `attack`
from the interpreter can't conjure that config.

This was pushed as far as memory allows. Even setting **every** known lever at once —
name list A `= "Rat"`, all three scan sub-flags (`g_100F0D3B`/`g_100F94C7`/`g_10135278`,
the exact set that drives the live recolor), the **forced/locked sticky-target override**
`g_100F9355 = <Rat id>`, `attack`/`settargeting on` via the interpreter, and the
auto-attack byte `g_10207F35` held at `1` by re-writing it every tick — the arbiter still
did **not** engage: the matched-creature counter `g_100F49C9` stayed `0`, the
current-target pointer `g_100F0E20` stayed `0`, and the attack-throttle byte
`g_100F45BC` never armed. So the final boundary is not the command layer (proven live)
nor the run-state (defeated live) — it is the **per-creature attack configuration**, a
dialog-owned structure the priority scan (`pickAttackTarget 0x1002355e`) reads and that
is not reconstructable from any single global reachable here. Populating that structure
directly (deeper RE) or driving the dialog on a release client is the one remaining step
for the Attack / Aimbot / Looting captures. Everything up to it — inject, hooks, engine,
snapshot, targeting recolor, lists, creature-spy, healing, proxy, extras, and now
**external interpreter control** — is confirmed live.

Original recipe (now backed by the live proof above), via the natural hotkey path:

1. Key-hotkey table `byte_100FAA3C`, entry `i` at `+i*514`: `byte[0]` = VK code,
   `byte[1]` = presence flag (nonzero), `byte[2..]` = null-terminated CiroScript text.
2. Write entry 0 = VK `0x77` (F8), presence `1`, text `"waypointson"` (or
   `"auto 300 waypointson"` to also arm auto-repeat `dword_1008910B[0]`).
3. Enable the key-hotkey block: `byte_100F94C5 = 1`.
4. Pre-load a waypoint (Cavebot: `0x101E6EA8[0]` = `x+2,y,z`, count `0x10202F06 = 1`,
   gate `g_100F0E42 = 1`).
5. `SetForegroundWindow` the client + `keybd_event(0x77)` — the driver polls
   `GetAsyncKeyState(F8)`, fires entry 0, dispatches `waypointson` through
   `registerCommands_table`.
6. Walker now has an armed run-state **and** a waypoint → the char steps toward it:
   the client position (`0x64F608` x / `0x64F604` y) changing = a genuine **Cavebot
   walk** behavioural PASS *and* the first live proof of external CiroScript execution.
   The same entry re-pointed at `settargeting on` + an attack script over a reachable
   creature is the path to the **Attack / Aimbot / Looting** captures (a kill produces
   the corpse the loot scan needs).

Direct backup: a `push flag; push idx; push scriptPtr; call 0x10030442` stub run via
`CreateRemoteThread` dispatches one statement without the hotkey table (confirm
`0x10030442`'s convention from its epilogue — `ret` cdecl vs `ret 0xC` stdcall — first).
The remaining **Alarm** subsystem is independent + data-driven: `handleAlarmTriggers`
(`0x10009489`) walks 3-byte rows at `g_10207F12`; arming a row's `byte[0]` (sound +
on-screen flag `g_100580F8`) with a creature on screen — never `byte[2]`, the
proxy-socket disconnect — should raise `g_100580F8` with no interpreter involvement.
