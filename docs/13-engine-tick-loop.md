# The engine tick loop — master control flow

Everything the bot *does* at runtime is driven from one function:
**`botMainTickLoop`** (`0x100227bd`, 3467 bytes), the body of the bot's main
engine thread (spawned from `EcInit` → the worker-thread setup). This doc traces
that loop end-to-end; it is the spine every other engine doc hangs off.

A second thread, **`botUiWorkerLoop`** (`0x10021f6c`), handles window/hotkey/UI
housekeeping on a 100 ms cadence and is covered at the end.

## Shape of the loop

```c
void __noreturn botMainTickLoop(LPVOID)
{
    // zero a 0x7D000-byte scratch region, install the watchdog trace frame
    dword_10058178 = GetTickCount() - 10;
    while (1) {
        if (dword_102E2614) ExitThread(1);      // shutdown flag
        Sleep(10);                              // ~10 ms per tick
        ... dispatch every subsystem, gated by GetTickCount deltas ...
        dword_100580F0 = getHighResMillis() - tickStart;   // per-tick profile
    }
}
```

Two structural features matter:

- **10 ms base tick.** `Sleep(0xA)` sets the loop cadence; every subsystem below
  is additionally rate-limited by its own `GetTickCount()` delta check, so the
  bot's timing is wall-clock driven, not tick-count driven.
- **Watchdog trace frame.** Before *each* subsystem call the loop writes a
  numeric **trace id** into `dword_1005DB78` (values 8, 10, 20, 30, 40, 50, 60,
  61, 90, 100, 110, 120, 130, 140, 150, 160, 170, 190, 200) plus a resume label
  into `dword_1005DB7C` and the current `GetTickCount()` into `dword_1005DB88`.
  A structured-exception handler (`reportTimerProcError`, `0x100026a6`) reads
  that id if a subsystem faults, so a crash is attributed to the exact stage.
  This is why the decompilation is a wall of `dword_1005DB78 = <id>` assignments
  between calls — it is an in-house per-stage watchdog, not real logic.

## Dispatch schedule (one tick)

In execution order, with the trace id, gate, and the named handler:

| id | Gate | Handler | What it does |
|---|---|---|---|
| 30 | every tick | `snapshotPlayerStats` (`0x10024fae`) | copy hp/mp/pos/skills from client memory into the bot's shadow state |
| 50 | every tick | *(inline)* | mirror the client light value `dword_10043956` ← `[0x79C31C]`, write back to `[0x4EAFA5]` (full-light) |
| 60/61 | 100 ms sub-loop | `syncClientLightState` (`0x1002997f`), `decayTimerTable` (`0x1002994d`), `sendMapClickPacket` | age the ~30 cooldown timers, the 156-byte-stride battle-list ageing, condition timers |
| 8 | inside 100 ms loop | *(inline)* | close a stale file handle; roll the creature "seen recently" ring buffers |
| 20 | 100 ms | `proxyConnectionTick` (`0x100205bf`) | service the embedded proxy/NavNet socket |
| 40 | 100 ms | `resolveActiveCreaturePtr` (`0x10023a45`) | refresh the current-target creature pointer |
| 90 | 100 ms | `pushExpSampleWindow` (`0x10023e42`) | push an exp/hr sample into the rolling window |
| 190 | 100 ms | `sendNavPositionUpdate` (`0x1003ffdf`) | broadcast this char's position to NavNet peers |
| 100 | every tick | `runScriptTickProfiler` (`0x1002bc68`) | **CiroScript engine tick** — run active cavebot/script commands ([14](14-ciroscript-runtime.md)) |
| 140 | in-game only | `healerManaSpellTick` (`0x1002492d`) | **healer**: mana-restore + heal spell/rune decisions ([15](15-healer-engine.md)) |
| 150 | in-game only | `runAttackHealerLogic` (`0x100235e8`) → `castRuneOrSpellOnTarget` (`0x1003a60a`), gated by `isCreatureReachableWalkable` | attack-rune / offensive-spell casting on the current target |
| 170 | in-game only | `scanBattleListStatusTick` (`0x10023a8f`) | re-scan the battle list, update per-creature status |
| 160 | interval | `dequeueMarkedCreature` (`0x1003bb22`) | pop the next marked/looted creature |
| 200 | `rand(100)+50` ms | `targetingAttackScanTick` (`0x10023893`) | **targeting**: pick + attack the best creature ([16](16-targeting-engine.md)) |
| 130 | not in-game | `sendClientLoginKeystrokes` (`0x10039bbb`) | **auto-login**: replay stored login keystrokes when logged out |

The **in-game gate** is `MEMORY[0x64A9C0] == 31` — a client global that reads 31
while a character is in the world. When it is not 31 the loop takes the *else*
branch: it clears the per-creature timers and, if auto-login is armed
(`byte_10207F23`), calls `sendClientLoginKeystrokes` on a `rand(100)+200` ms
jitter. This is how ElfBot auto-relogs after a disconnect.

## Timer bank

The bulk of the 100 ms sub-loop is ~30 guarded decrements of cooldown globals
(`dword_1008B8DC…F0`, `dword_1005F561/565/569`, the `dword_1008B945[10]` array,
etc.) and the ageing of two creature tables:

- the **battle-list shadow** at `byte_10077175`, 156-byte stride, bounded by
  `dword_10080B05` — per-entry "last seen" slots (`+92`, `+112`), attack/health
  decay fields (`+88`, `+90`), rolled on 3-tick and 20-slot cursors;
- the **condition/effect table** `unk_1005E1A0…word_1005E6A0`, 8-byte stride,
  decrementing `+3` and incrementing `+4` (an age counter).

These are the data structures the targeting and healer engines read; the tick
loop is what keeps them fresh and expires them.

## `botUiWorkerLoop` (`0x10021f6c`)

The UI thread. An infinite `Sleep(100)` loop that:

- shows/hides the hotkey overlay window based on `GetForegroundWindow` +
  `GetCurrentProcessId` (only when Tibia is focused);
- toggles the full-light hack on **Ctrl+F11 / Ctrl+F12** (`GetAsyncKeyState`);
- reloads config/scripts when their dirty flags are set;
- updates the HUD window title.

It carries no combat logic — it is the human-facing half while `botMainTickLoop`
is the engine half.

## Where each engine is documented

- CiroScript runtime → [14](14-ciroscript-runtime.md)
- Healer → [15](15-healer-engine.md)
- Targeting → [16](16-targeting-engine.md)
- Cavebot walker / pathfinder → [17](17-cavebot-walker.md)
- NavNet codec → [18](18-navnet-codec.md)
- (client hooks [08](08-client-hooks-engine.md), packet proxy [09](09-packet-proxy.md) already exist)
