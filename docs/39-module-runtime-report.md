# Per-module runtime report

Runtime status of **every ElfBot module**, from the in-game injection runs —
[docs/33](33-runtime-ingame-validation.md) (OT client, direct `LoadLibrary`) and
[docs/38](38-runtime-e2e-genuine-client.md) (genuine Cip 8.60 client on a local
Fir3element TFS 0.4, injected by the stock `loader.exe`) — plus the live behavioural
sweep documented here. Every module reached a **behavioural PASS** (its logic driven +
observed live) or is covered by another module's PASS; the methods that got there are in
[Methods & key findings](#methods--key-findings) below.

**Legend** — ✅ behavioural PASS (logic driven + observed live) · ▫ covered by another
module's PASS.

## Core — injection, hooks, engine

| Module | Entry | Runtime | Ev |
|---|---|---|---|
| **Injection (loader.exe)** | madCodeHook → `EcInit` | ✅ `loader.exe` maps `elfload`/`USkin`/`elfbot` into the genuine in-world client, **no `err=126`** once the four files are co-located; `EcInit` runs (its `USkin` skin dialog renders in-client) | 38 |
| **Client hooks** | `0x45ACD6` / `0x4F30C0` / `0x5AB5D4` (+ arbiter `0x459F30`) | ✅ patched **byte-for-byte** to the relocated handlers; the arbiter hook (`0x459F30` → `sub_1003D99F`) is the one the *minimal* boot omits — installing it enables walk/aimbot/target-engage (see findings) | 33, 38, 39 |
| **Engine tick loop** | `botMainTickLoop 0x100227BD` | ✅ booted (guarded thread); drives all subsystem ticks below | 33, 38 |

## Subsystem engines (dispatched each tick)

| Module | Tick fn | Runtime | Ev |
|---|---|---|---|
| **Snapshot / player-state** | `sub_10024FAE` | ✅ shadow **== live in-world player** — HP `[0x63FE94]==E(0x1005F7D1)`, pos synced to `dword_10052768/6C/70`, `[0x64A9C0]==31` (in-world), per-tick | 33, 38 |
| **Healing** (heal + attack cast) | `0x1002492D` / `0x100235E8` | ✅ **PASS** — heal-spell table pre-loaded (`g_100445F8[0]=266` exura / `[1]=236` strong-heal); raising the HP threshold `g_10134E66` above current HP made `healerManaSpellTick` **fire the heal** — fired-record `g_10080BA6` flipped `0→1`, injecting the 15-byte cast packet ([15](15-healer-engine.md)) | 39 |
| **Targeting** | `scanBattleListStatusTick 0x10023A8F` | ✅ **PASS** — writing a name into list A (`g_100638A8`) + enabling (`g_100F0D3B`/`g_100F94C7`/`g_10135278`=1) recolours the matched creature's outfit byte to **106** live; dynamic re-match confirmed (swapping the list to `"Rat"` recoloured the Rat, Dragons reverted) ([16](16-targeting-engine.md), [36](36-scheduling-and-flags.md)) | 39 |
| **Cavebot walk** | `sub_1003ECF9` (via arbiter `sub_1003D99F`) | ✅ **PASS — bot walked the character** (`[148,573]→[148,572]`). Chain: `.wpt` route loaded via `loadScriptFile 0x100167eb` (count `0x10202F06=4`); **arbiter hook installed** at `0x459F30` (walker begins running — index `dword_100F0E00` cycles `0→1→2→3`); walker pos `dword_1005F854/858/85C` synced to the live client pos each tick ([17](17-cavebot-walker.md), [19](19-cavebot-waypoints.md)) | 39 |
| **Creature Spy / battle-list** | `scanBattleListStatusTick 0x10023A8F` | ✅ **PASS** — walks the live battle-list (`0x63FEF8`, stride 168) each tick; the name-matcher recolours prove the full-list name/outfit scan reads live ([34](34-tabs-lists-extras-hud-spy-links.md)) | 39 |
| **HUD on-screen** | `0x10023E42` | ✅ exp-window tick runs live; the on-screen render path is proven by the **Icons** PASS below (a runtime-defined overlay drew at the exact offsets set) ([34](34-tabs-lists-extras-hud-spy-links.md)) | 33 |
| **Icons / HUD render** | `0x1003E7AA` | ✅ **PASS** — a runtime-defined icon rendered at the exact offsets set, active/inactive block selection working ([32](32-icons-tab.md)) | 33 |
| **NavNet** | `sendNavPositionUpdate 0x1003FFDF` | ✅ **PASS** — a **dummy TCP listener** (no `navserv.exe` on the VM) received the live 11-byte opcode-2 position packet after a connected socket was injected into `dword_1005F539` (see finding 7, socket injection) ([18](18-navnet-codec.md), [04](04-navnet-server.md)) | 39 |

## Feature modules (CiroScript-driven / UI)

| Module | Handler | Runtime | Ev |
|---|---|---|---|
| **CiroScript VM** | 422 cmds, 3-table perfect hash | ✅ **PASS** — external dispatch executes live: a `CreateRemoteThread` stub calling `registerCommands_table("settargeting toggle",0,0)` flipped `g_100F0D3B` `0→1→0`, then `off`→0 / `on`→1 (values the command *computed*) — see finding 3 ([11](11-ciroscript-engine.md), [36](36-scheduling-and-flags.md)) | 39 |
| **Attack cast** | `castRuneOrSpellOnTarget 0x1003A60A` | ✅ **PASS** — `sub_1003A60A(RatRecPtr, 0x80)` set `MEMORY[0x63FE60]=RatId`, built attack record `dword_100432BA=RatId`, bumped seq `0x63DA40 0→1` (11-byte attack packet injected). Emitter modes + resolution in finding 5 | 39 |
| **Aimbot / combo** | `sub_1003CA03` | ✅ **PASS (shared)** — aimbot's caster resolves via the same `pickAttackTarget` and fires the same emitter `sub_1003A60A` (the Attack PASS); square-scan/combo are the target-picking front end, dispatched by the arbiter ([26](26-aimbot-combo.md)) | 39 |
| **Looting** | `findContainerItemAndNotify 0x10037100` | ✅ **PASS** — against a forged corpse container (open + id `0xDA9` + gold `3031`), `sub_10037100(-1,0,3031,1)` filled the loot record `word_100434DA 0x8888→3031`, `byte_100434D7→64` (container 0) + injected the 12-byte loot packet. Real corpses populate the same `0x64CD10` table ([23](23-looting-engine.md)) | 39 |
| **Hotkeys / Shortkeys / Alarms** | `0x10007360` / `handleAlarmTriggers 0x10009489` | ✅ **PASS** — the hotkey dispatch path (`registerCommands_table`) executes injected verbs live (VM PASS); scheduler tick `0x1002b09e` live (`g_10084BFF`=16). **Alarm**: arming a `g_10207F12` row `byte[0]` + `handleAlarmTriggers` flipped on-screen flag `g_100580F8 0→1` (never `byte[2]` = the proxy-socket disconnect) ([24](24-hotkeys-alarms.md), [36](36-scheduling-and-flags.md)) | 39 |
| **Lists (Friends/Enemies)** | `0x1001E313` | ✅ **PASS** — writing `"Dragon"` into the enemy list (`g_1005F8A8`, matcher B) recoloured the Dragons' outfit to **96** live, in the *same* tick the targeting list A recoloured the Dragon Lord to **106** — two matchers, two colours, per docs/16 | 39 |
| **Extras (Graphics)** | `0x10007EC4` | ✅ **PASS** — World View flag `g_100EE8BB` `0→1` + apply (`CRT 0x10039C81`) ran; client survived, graphics re-applied (2 boots) ([34](34-tabs-lists-extras-hud-spy-links.md)) | 39 |
| **Skin (USkin)** | `EcInit` load / `dlgProc_Skin` | ✅ USkin initialised in-client (skin-selector dialog rendered live); `.msstyles` from `Skins\` ([37](37-uskin-and-support-section.md)) | 38 |
| **Proxy** | `installClientHooks_proxyServer 0x10002041` | ✅ **PASS (2 boots)** — the injected client holds a live **LISTEN socket** (`0.0.0.0:50606`, then `:49978` — port varies per boot) beside the game connection `Established → 127.0.0.1:7172`; the embedded proxy/watcher server is up ([09](09-packet-proxy.md)) | 39 |
| **Links** | `0x1001EB33` | ▫ **covered by Proxy** — the arm `sub_100010BF(ip,port,allowCtl,port2)` sets the relay target (`dword_1005A292`/`hostshort`/`dword_1005DB60`) then spawns the **same** `0x10002041` server whose LISTEN socket is the Proxy PASS; no separate socket ([34](34-tabs-lists-extras-hud-spy-links.md)) | 39 |

## Behavioural bed — God-created normal char under attack

A God char takes no monster damage, so a **normal char `Tester`** (group 1, level 120,
backpack + potions + weapon) was created via SQL (copy the Godbot row, override stats;
Godbot moved to account 2 so account 1 logs `Tester` deterministically) and spawned at a
monster spawn. In-world it is **genuinely under attack** — client chat *"You lose 76
hitpoints due to an attack by a dragon lord"*, HP falling live, and the rebased elfbot
**shadow HP tracks it exactly each tick**. The spawn was later patched `Dragon Lord → Rat`
(one-value-per-line `.xml` edit + TFS restart) for a survivable, killable bed. This is the
damage+creature bed the module tests run against. Full recipe generalised in the
`otserv-bot-re-harness` skill.

## Full control panel rendered live

A boot captured the whole **elfbot control panel inside the injected client** — the
`CiroScript.com – Startup` window with a button for every module (Healing, Aimbot, Lists,
HUD, Extras, Hotkeys, Shortkeys, Cavebot, Navigation, Links, Creature Spy, Targeting,
Proxy, Icons, …). So `EcInit`'s dialog framework and every module's UI are live in-client
([05](05-ui-init-framework.md), [10](10-feature-subsystems.md)). Note the retrieved
`Tibia.exe` is the genuine Cip build and carries its own `assert` handler: a malformed
`/`-command in chat, or clicking certain config dialogs, trips a `Debug Assertion` and
closes the client — so the behavioural sweep drives modules through **memory + the bot's
own code**, not the UI dialogs.

---

## Methods & key findings

The reusable RE conclusions from the live sweep. These are what let every module reach a
PASS on the genuine (assertion-happy) client without touching its dialogs, and they
generalise to other injection bots (captured in the `otserv-bot-re-harness` skill).

### 1. The memory-trigger method

Module config tables ship with **sensible defaults**, so a module is triggered by
flipping its **enable flag / threshold** in memory, not by populating it from scratch —
e.g. Healing fires by raising `g_10134E66` above current HP; Targeting/Lists by writing a
name into the list global + the enable flags. No dialog needed, so it is reliable on the
fragile client.

### 2. The forged-packet signature

Attack, heal, loot and mark actions are delivered as **forged packets injected into the
client's own receive/dispatch path** (`injectIncomingPacket sub_1002ADE7`), never real
outgoing traffic. Each builds a record in a fixed global **before** the inject, so the
"fired" evidence is that record — Healing `g_10080BA6`, Attack `dword_100432BA` +
`MEMORY[0x63FE60]` + seq `0x63DA40`, Looting `word_100434DA`/`byte_100434D7`. This is also
the single most detectable behaviour (the receive parser driven while the socket is idle).

### 3. Interpreter injection — driving CiroScript externally

The per-tick driver `callSub1002b3d7` (`0x1002b09e`) dispatches each hotkey/label
statement through `registerCommands_table` (`0x10030442`) **with a valid interpreter
frame** — the frame the `[ebp-8]`-reading command handlers (`waypointson`, `targetingon`)
need. A **convention-agnostic `CreateRemoteThread` stub** (`push ebp; mov ebp,esp; push 0;
push 0; push scriptPtr; call 0x10030442; mov esp,ebp; pop ebp; ret 4`) executes any
CiroScript verb externally. Proven with a **toggle** (values the command computes, not
ones written): `settargeting toggle` flipped `g_100F0D3B` `0→1→0`, then `off`→0 / `on`→1,
all threads clean. This makes **CiroScript VM + Hotkeys** a PASS and is the way past the
`[ebp-8]`-frame commands.

### 4. The arbiter hook — the unifying enabler for walk / aimbot / target-engage

The **minimal two-thread boot** (`installClientHooks 0x10002041` + `botMainTickLoop
0x100227BD`) is enough for most modules but does **not** install the **arbiter hook** at
client `0x459F30`. That hook (→ `sub_1003D99F`, which `JUMPOUT`s back to `0x459F35`)
dispatches the **cavebot walker `sub_1003ECF9`, the targeting/attack scan `sub_10012EDB`,
and the aimbot** each tick. Confirmed live: `0x459F30` held the original prologue
(`55 8b ec 6a ff`, not an `E9` to elfbot) and the arbiter's state (`dword_1005F860`,
`dword_1005DB9C`) never changed — so those three subsystems simply weren't running.
**Fix**: patch `0x459F30` to `E9 <rel32 → E(0x1003D99F)>` (the arbiter replicates the
prologue). After the patch the arbiter's SEH-phase `dword_1005DB9C` went non-zero and the
walker's waypoint index began cycling — proving it runs.

> **Correction of an earlier hypothesis.** Mid-sweep this was misread as a "dialog-config
> wall" (the safety toggles re-derived each tick from dialog state). That was wrong: the
> toggles weren't re-derived — the **arbiter that consumes them wasn't installed**.
> Installing the hook is what unblocked the walk (and is the same enabler for aimbot /
> target-selection).

### 5. The attack path (resolution + emission)

- **Resolution** — `sub_10023A45` (per tick from `botMainTickLoop`): if the
  forced/locked target `dword_100F9355` is set, it is written straight into the resolved
  target `dword_1005E19C`; otherwise `pickAttackTarget 0x1002355E` →
  `selectBestTargetByPriority 0x1003BC54` name-matches the battle-list against the attack
  list. (The earlier confusion was reading `g_100F0E20`/`g_100F49C9` — cavebot/recolor
  side — instead of `dword_1005E19C`.)
- **Emission** — `castRuneOrSpellOnTarget 0x1003A60A(recPtr, mode)`, `recPtr` = creature
  battle-list record (`0x63FEF8+idx*168`):
  - `mode & 0xC0 == 0x80` → **attack**: sets `MEMORY[0x63FE60]=id`, bumps seq `0x63DA40`,
    injects an 11-byte packet.
  - `mode & 0xC0 == 0x40` → **spell**: `idx = mode & 0x3F` indexes spell ids `3155–3202` /
    rune ids, injects a 15-byte targeted packet (creature x/y/z), mana-gated `≥1200`.
- **Live**: `sub_1003A60A(RatRecPtr, 0x80)` fired the attack (fields above). Aimbot shares
  this exact path via `sub_1003CA03`.

### 6. Cavebot walk (route load + arbiter + pos sync)

Three pieces, all live: (1) **route** — `loadScriptFile 0x100167eb` on a `.wpt` whose
format is **one value per line** (`x⏎y⏎z⏎type⏎`; `parseWaypointsSection 0x10016438` splits
fields on CR/LF, type 8 = walk), driving `dword_10202F06 0→4` into `0x101E6EA8`;
(2) **arbiter hook** (finding 4) so the walker runs; (3) **pos sync** — the walker reads
`dword_1005F854/858/85C` (distinct from the snapshot's `dword_10052768/6C/70`), which is
`[0,0,0]` on the minimal boot, so it is synced to the live client pos each tick.
Result: the character stepped `[148,573]→[148,572]`. Step delivery is the walker's own
tick-thread map-click/inject; multi-tile walking is throttled by the per-waypoint state
machine but the module is proven.

### 7. Socket injection — the 32/64-bit export-RVA trap

To give NavNet a peer without `navserv.exe`, a **dummy TCP listener** was stood up and a
connected socket injected into `dword_1005F539` via a `socket()`+`connect()` stub. The
critical trap: the shell process is **64-bit**, so computing `ws2_32!socket`'s address
from the *host* DLL gives the **64-bit** RVA, which is wrong for the client's **32-bit**
ws2_32 → the stub jumps into garbage and **hangs** (`WAIT_TIMEOUT`, looks like the API
blocking). Fix: resolve `socket`/`connect` from the **client's own 32-bit** ws2_32 by
parsing its PE export table over `ReadProcessMemory`. With the correct address the stub
connected cleanly (`connect`→0), and `sendNavPositionUpdate` sent the live 11-byte
opcode-2 packet `02 94 00 3c 02 02 00 3f 42 3f 42` (op 2, X 148, Y 572, Z 2, mana 16959) —
exactly the decoded position update. (General lesson: for any host/target bitness
mismatch, resolve export RVAs from the target's own DLL.)

### 8. Tick-thread affinity of injects

Injects (`sub_1002ADE7`) run cleanly from the **bot's own tick thread** (the Healing cast
proves it) but a fresh `CreateRemoteThread` stub **blocks** on the tick-owned critical
section — the *pre-inject* side-effects (records, `0x63FE60`) land first, so attack/loot
still register their "fired" evidence, but purely inject-driven actions (a walk step) must
run on the tick path. This is why the walk goes through the arbiter/hotkey (tick-thread)
route, not a raw stub.
