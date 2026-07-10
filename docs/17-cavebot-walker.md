## Cavebot walker & pathfinder

The walker turns a destination (a cavebot waypoint, a target creature, a lootable
corpse, or a flee vector) into a single walk step each time it runs. It operates
on an **18×14 tile grid window centred on the player** (grid centre ≈ `(8,6)`),
builds a per-tile cost map, runs a BFS from the destination back to the centre,
and emits the first step's direction — delivered to the client as a map-click
packet or a keystroke.

### Grid & cost model

| Global | Role |
|---|---|
| `g_10052785` | base 14×18 walk-cost grid (8-byte cells) |
| `g_10288fc4` | per-tile step-cost overlay (blocking = `>= 0xFFFFFFFE`) |
| `g_10052774` | BFS node pool (expansion tree) |
| `g_10052784` | diagonal-moves-allowed flag |
| `g_1005F854/858/85C` | player X/Y/Z (grid is player-relative) |
| `g_10052f65/69/6d/71` | accumulated directional danger sums (N/E/S/W) |

`buildPathCostGridAndScanCreatures` (`0x10013F16`) rebuilds the grid each pass:
it scans the tiles via `sub_1003a148`/`sub_1003c4fa`, flags blocking items and
monster tiles, and re-targets discovered monsters. `accumulateTileCosts`
(`0x1000d96a`) / `applyGridCostOverlay` (`0x1000e0b2`) fold the overlay into the
base grid, skipping blocked cells.

### Pathfinders (BFS family)

All expand a node tree from the goal toward the centre `(8,6)` and return a
direction code; they differ in goal shape and cost model:

| Function | Addr | Goal |
|---|---|---|
| `traceMapPathBFS` | `0x1000d2da` | shortest path to an exact tile (orthogonal + diagonal if `g_10052784`) |
| `traceMapPathBFSSeeded` | `0x1000d9b8` | same, pre-seeding a 3×3 area around the start (used by loot/approach) |
| `floodFillPathCosts` | `0x1000e100` | flood-fill reach costs into `g_10288fc4` from a point |
| `findBestWaypointPath` | `0x1000e6b9` | reach within radius; scores goal nodes by distance/cost weight |
| `searchPathToTargetRadius` | `0x1000f40a` | BFS toward a radius of a point, Chebyshev heuristic |
| `searchLowestCostPath` | `0x1000ffb0` | pick the min-accumulated-cost goal node |
| `searchPathVariant` | `0x10010af0` | radius variant, same 8-byte-cell model |

The multiple variants exist because "walk to a waypoint tile", "get within attack
range of a creature", and "get to the cheapest reachable tile toward a goal" are
different optimisation targets over the same grid.

### Movement dispatch

| Function | Addr | Behaviour |
|---|---|---|
| `stepTowardTarget` | `0x10013e4d` | if target > 1 tile away, `traceMapPathBFS` toward it then issue the step (`sub_10014825`) |
| `walkToDispatch` | `0x100147eb` | run the pathfinder then route to one of two movement handlers by result code |
| `approachTargetOrPathfind` | `0x10014927` | if within 1 tile → melee-adjust; else full pathfind |
| `stepToTargetOrPathfind` | `0x10014993` | within 1 tile → `searchLowestCostPath` + step; else pathfind |
| `keepDistanceStepC69` / `D75` | `0x10014c69`/`0x10014d75` | keep-distance: step closer if too far, suppress range-breaking moves at exact range, else pathfind |
| `maintainDistanceRingStep` | `0x10014e64` | ring-keeping around a target via `findBestWaypointPath` |
| `stepToStoredWaypointIfInRange` | `0x10014a6e` | walk to a stored destination `g_10052778` when in range |

The keep-distance steppers are what implement a paladin/mage "stay N tiles from
the monster" behaviour: at the exact ring they mask out any direction that would
change the distance and only take neutral moves.

### Retreat, flee & creature avoidance

- `stampCreatureAvoidanceWeights` (`0x100143ba`) adds danger cost (weights
  `128`/`160`/`-2`) in a **5×5 area around each creature** and accumulates
  direction-scaled danger into `g_10052f65/69/6d/71`.
- `chooseFleeStep` (`0x1001451b`) reads those directional danger sums and the
  player-relative offsets to pick the **safest adjacent tile**, walks to it via
  `sub_10015204`, and sets `g_100f0dc4 = 10` (a flee-hold timer).
- `decideRetreatStep` (`0x1001242d`) is the higher-level retreat driver that
  chooses between advancing on a target and retreating via the pathfinder.

So the danger map is the inverse of the goal cost map: avoidance stamps raise the
cost near monsters, and flee inverts the objective to *maximise* distance from the
accumulated danger direction.

### Step delivery

A chosen direction becomes client movement through `sendMapClickPacket`
(`0x10026340`, an auto-walk map click) or a directional step packet — both issued
via the synthetic-packet/injection path, so the walker leaves the same
inbound/outbound signature as the rest of the engine ([`09`](09-packet-proxy.md)).
The waypoint that seeds the destination and its file format are in
[`19`](19-cavebot-waypoints.md).

## Detection notes

- A process maintaining an 18×14 player-relative cost grid and reading tile/creature
  data from the client map window each tick.
- Auto-walk map-click packets (`sendMapClickPacket`) emitted without a mouse click,
  or directional step packets on a pathfinder cadence.
- The 5×5 creature-avoidance stamp and the flee-hold behaviour (moving directly
  away from clustered creatures) are behavioural tells distinct from human walking.
