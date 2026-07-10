# elfbot.dll — cavebot walker & targeting engine

The two AI engines that drive hunting: the **cavebot walker** (moves the
character along a path, avoiding danger) and the **targeting evaluator** (chooses
and attacks creatures). Both run off the main bot tick and read the shadow
creature table populated by the packet hook ([08](08-client-hooks-engine.md)).
Function names below are persisted in the IDA db and catalogued in
[functions/jdrv-catalog.md](functions/jdrv-catalog.md).

## Main loop

- **`botMainTickLoop`** `0x100227BD` (3467 B) — the bot's heartbeat thread.
  Each tick (guarded by `GetTickCount` deltas + `Sleep`) it snapshots client
  state, runs targeting, healer and cavebot steps, and updates the HUD. Reads
  the local-player struct (x/y at `+0x58/+0x5A`, container/battle pointers) and
  the creature records.
- **`botUiWorkerLoop`** `0x10021F6C` — the UI/timer worker that services the
  dialog messages and periodic redraws.

## Pathfinding (the walker)

A real cost-grid shortest-path search, not naive step-toward. Node records carry
`{x, y, parent*, g-cost, f-cost, flags}` (an open/closed list Dijkstra/A*).

| Function | Role |
|---|---|
| `findBestWaypointPath` `0x1000E6B9` | main path search to a waypoint over the cost grid |
| `searchLowestCostPath` `0x1000FFB0`, `searchPathToTargetRadius` `0x1000F40A`, `searchPathVariant` `0x10010AF0` | path-search variants (to a tile / into a radius) |
| `traceMapPathBFS` `0x1000D2DA`, `traceMapPathBFSSeeded` `0x1000D9B8` | BFS flood over walkable tiles |
| `buildPathCostGridAndScanCreatures` `0x10013F16` | build the per-tile cost grid and scan creatures onto it |
| `floodFillPathCosts` `0x1000E100`, `accumulateTileCosts` `0x1000D96A`, `applyGridCostOverlay` `0x1000E0B2` | populate/overlay tile costs |
| `lineOfSightWalkable` `0x10011678`, `traceLineBlockedAt` `0x100117EF` | Bresenham line-of-sight / blocking test |
| `decodeRleMapCells` `0x10012771` | decode the client's RLE map tiles into the walkability grid |

### Threat avoidance

The walker weights tiles by monster danger so it routes *around* spell areas:

- `stampCreatureSpellArea` `0x10011AF2` / `updateCreatureSpellThreatMap`
  `0x10012AAE` — stamp each creature's attack/spell footprint onto the cost grid.
- `stampCreatureAvoidanceWeights` `0x100143BA`, `stampAreaThreatCosts`
  `0x100115BC`, `isInsideDangerZone` `0x10011A89` — danger-zone weighting.
- `decideRetreatStep` `0x1001242D`, `chooseFleeStep` `0x1001451B` — flee logic
  when cornered.

### Stepping

Once a path/target is chosen, movement is issued via a family of step helpers
that pick a direction and either melee-approach or keep distance:

- `stepTowardTarget` `0x10013E4D`, `approachTargetOrPathfind` `0x10014927`,
  `stepToTargetOrPathfind` `0x10014993`.
- `keepDistanceStepC69` `0x10014C69` / `keepDistanceStepD75` `0x10014D75` /
  `maintainDistanceRingStep` `0x10014E64` — ranged "keep N sqm" behaviour.
- `handleAdjacentTargetMeleeOrOpenDoor` `0x10014F10` — melee when adjacent, open
  doors in the way.
- `walkToTile` `0x10015204` / `walkToDispatch` `0x100147EB` /
  `stepInDirection` `0x10014825` — final move dispatch (feeds the client walk).

## Targeting evaluator

- **`pickAttackTarget`** `0x1002355E` — target selection priority:
  1. the locked target `g_10080BCB` if still valid (`sub_1003BC09` = on-screen /
     reachable check);
  2. else the previous target `g_10080BB3` if valid;
  3. else `sub_1003BC54` scans the battle list for the best candidate by the
     targeting rules.
- `targetingAttackScanTick` `0x10023893` — per-tick targeting: re-evaluate,
  attack, cast the configured spell/rune.
- `isCreatureValidTarget` `0x100237A4` — gate a creature against the active
  `.elft` rules (name, vocation, distance, reachable/shootable).
- `runAttackHealerLogic` `0x100235E8` — combined attack + heal decision per tick.
- `scanBattleListStatusTick` `0x10023A8F`, `resolveActiveCreaturePtr`
  `0x10023A45` — walk the shadow battle list (`unk_1005A2A3`, 150×40 B) and
  resolve the active creature pointer in client memory.
- `buildSpellFromRuneId` `0x10021C2D` — map a rune/spell selection to the words
  to `say`.

The targeting rules themselves come from the `.elft` records parsed by
`parseTargetingRecord` `0x100172B0` (fields `Name:/Hpmin:/MonsterAttacks:/
Stance:/ActionSpell:/AttackMode:/...`, see [11](11-ciroscript-engine.md)).

## Data flow

```
packet hook → shadow creature table (150×40B) + map tiles
   │
botMainTickLoop ──► pickAttackTarget ──► targetingAttackScanTick ─► say spell / attack
   │                     └── isCreatureValidTarget (.elft rules)
   └──► cavebot: buildPathCostGridAndScanCreatures ─► findBestWaypointPath
             └── stampCreatureSpellArea (threat) ─► step helpers ─► walkToTile
```

Both engines are pure in-process reads of the client's data structures (shared
address space) plus the shadow tables, so they react within one tick without
server round-trips.
