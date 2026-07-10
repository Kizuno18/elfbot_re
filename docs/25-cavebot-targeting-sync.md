# Cavebot ↔ targeting ↔ healer synchrony

How the independent engines coordinate. They are **not** nested — each is a
separate handler fired from the one bot tick ([13](13-engine-tick-loop.md)) in a
fixed order, and they talk to each other through a small set of shared global
flags plus the CiroScript conditionals (`istargeting` / `isnottargeting`). This
doc ties the pieces (docs [14](14-ciroscript-runtime.md), [16](16-targeting-engine.md),
[17](17-cavebot-walker.md), [15](15-healer-engine.md)) into the interplay.

## The three master flags

| Global | Meaning | Set by | Read by |
|---|---|---|---|
| `g_100f0d3b` | **targeting engine armed** | `cmd_settargeting` (`on`/`off`/`toggle`, `0x10035786`); the Targeting tab checkbox | the tick arbiter, `cmd_targetingon` |
| `g_100f0e42` | **cavebot walker armed** ("follow waypoints") | `cmd_setfollowwaypoints` (`0x10035812`, also drives dialog ctrl 1012); the Cavebot tab checkbox | the tick arbiter, `cmd_waypointson`, most walk/action commands |
| `g_100f0e20` | **targeting currently has an active creature** (the bridge) | the tick arbiter (recomputed each tick) | `cmd_istargeting` / `cmd_isnottargeting` in scripts |
| `g_100f0d3c` | one-shot **run-targeting** request (`cmd_runtargeting` = `2`) | `runtargeting` | the tick arbiter |

`g_100f0d3b` / `g_100f0e42` are the two independent on/off switches a user (or a
script via `settargeting` / `setfollowwaypoints`) flips; they mirror the two tab
checkboxes. `g_100f0e20` is the read-only bridge the cavebot script uses to know
"am I in a fight right now".

## The per-tick arbiter — `cavebotTargetingStep` `0x1003D99F`

Each tick this driver runs the two engines in order and maintains the bridge
flag:

```c
if (g_100f0d3b || g_100f0d3c) {   // targeting armed or a runtargeting request
    g_100f0e20 = 0;               // reset "has target"
    ... scan the battle list, pick + attack the best creature ...
    // g_100f0e20 is set back to non-zero while a valid creature is engaged
}
if (g_100f0e42) {                 // cavebot walker armed
    ... execute the current waypoint / step along the path ...
}
```

So **targeting runs before the walker**. Targeting decides whether a creature is
engaged and publishes that in `g_100f0e20`; the walker (and the cavebot action
script) then reads it to decide whether to move. Combat pre-empts walking within
the same tick without either engine calling the other directly — they are
decoupled through `g_100f0e20`.

(The same ordering is visible in the tick schedule in [13](13-engine-tick-loop.md):
`targetingAttackScanTick` id 200, the CiroScript/cavebot tick id 100, healer ids
140/150. The arbiter is the cavebot-side consumer of the targeting result.)

## How the cavebot *script* coordinates with targeting

The cavebot waypoint list is CiroScript; it gates itself on the targeting state
rather than being force-paused:

- `istargeting <cmd>` — run `<cmd>` only if `g_100f0e20` is set (a creature is
  being fought). Used to hold position / cast while fighting.
- `isnottargeting <cmd>` — run only when no creature is engaged. Used to resume
  walking, loot, or skin once combat is over.
- `Stand` waypoints + `Lure` — the classic pattern: walk into a spawn, `Stand`,
  let monsters gather (targeting stays off or in lure mode), then engage. The
  "lure until N monsters" behaviour is script-driven (`monstersaround` /
  `countMonsterToStopLure`-style conditions) on top of these flags.
- `settargeting off` / `setfollowwaypoints off` inside an action script let a
  waypoint temporarily disable one engine (e.g. stop walking to do a quest
  action, or stop attacking near an NPC).

## Healer in the mix

The healer is a third independent tick handler (ids 140 `healerManaSpellTick`,
150 `runAttackHealerLogic`) that runs **before** targeting each tick and is gated
only by the in-game flag (`MEMORY[0x64A9C0] == 31`) and its own HP/MP thresholds
— it does not wait on targeting or cavebot. Offensive casting (id 150,
`castRuneOrSpellOnTarget`) *does* use the current target (so it piggybacks on
`g_100f0e20`), which is why heal and attack share `runAttackHealerLogic`.

## Summary of the loop each tick (in-game)

```
snapshot player state / light / timers
  ├─ healer: mana + heal spell/rune            (140/150, threshold-gated)
  ├─ attack: cast rune/spell on current target (150, needs g_100f0e20)
  ├─ CiroScript tick: run cavebot action script (100, uses istargeting/isnottargeting)
  └─ arbiter 0x1003D99F:
        if targeting armed  → scan+attack, set g_100f0e20   (200)
        if follow-waypoints → walk / step to next waypoint
NavNet position broadcast + proxy service
```

Everything is one thread, one tick, communicating through shared globals — no
locks, no message passing between engines. That is the whole "synchrony": a
fixed dispatch order plus the `g_100f0e20` / `g_100f0d3b` / `g_100f0e42` flag
triad.
