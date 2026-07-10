# Looting engine

The looter runs as part of the cavebot: after a kill it finds the nearest
lootable corpse, opens it, pulls configured item ids into destination
containers, and — when a backpack fills or on a `deposit` waypoint — runs a
depot state machine. It reads the client's container list directly and drives
loot moves through the same event dispatcher the rest of the bot uses
(`dispatchClientEvent`, `sub_1002ade7`/`sub_1002ade1`).

## Client container table

The client keeps up to **16 open containers** in a table at `0x64CAD0`,
**492-byte stride**. Each record holds a container id/type, a capacity
(`field_30`), and an array of 12-byte item records `{id, count, …}`. The looter's
scan helpers all walk this table:

| Function | Addr | Role |
|---|---|---|
| `findContainerItemSlot` | `0x1002ae92` | first slot holding item id (opt. subtype) → slot index+64, else 0 |
| `findContainerItemAndNotify` | `0x10037100` | find item by id or range 3497–3500, fire notify event `0x0C` |
| `findMoveSourceDestSlots` | `0x100371fd` | pair a source item with a dest container/slot honouring `field_30` capacity and <100 stack count, dispatch move event `0x11` |
| `findNthContainerItemSlot` | `0x10037384` | locate the Nth matching item across containers, dispatch event `0x11` |
| `iterateContainerItemsForDeposit` | `0x10036c87` | walk the table matching container id/type, invoke `sub_1003c52a` per qualifying 12-byte item |
| `resolveContainerRef` | `0x10036daf` | resolve a container token: number, or keywords `empty`/`empty1`/`dp` → 99/98/−1, else name lookup |
| `openContainerAndNotify` | `0x10036e69` | set open-state globals from a 12-byte record, dispatch event `0x11` |
| `hookContainerOpen` | `0x1002aab7` | client hook (message code 8): latch `g_10080B88` when an opened container matches the cavebot map rect |

## Corpse discovery — `findNearestLootableCorpseTile` (`0x100377cb`)

```c
// parse up to 63 loot item-id filters from the config token stream
for (i = 0; *cfg && i < 0x3F; ++i)
    filter[i] = parseExpressionOrRange(cfg);
buildPathCostGridAndScanCreatures();                 // refresh the 14x18 cost grid
for (j = 0; j < 14; ++j)  if (abs(j-6) <= radius)
  for (k = 0; k < 18; ++k) if (abs(k-8) <= radius) {
     tileX = g_1005F854 + (k-8);  tileY = g_1005F858 + (j-6);   // player-relative
     ... skip ids 386/421/7762 (fields) and 99/1948/1968 ...
     if (stackedItemMatchesFilter) pickClosestReachable(sub_1000d9b8);
  }
```

It scans the 14×18 map window centred on the player (globals `g_1005F854`/`858`/
`85C` = X/Y/Z), within `radius`, skips non-lootable ground ids, matches the top
stacked item against the parsed filter list, and picks the **closest reachable**
corpse tile via the seeded BFS pathfinder (`traceMapPathBFSSeeded`, `0x1000d9b8`)
— i.e. it walks to loot exactly like it walks to a waypoint ([`17`](17-cavebot-walker.md)).

## Ground pickup — `cmd_pickupitems` (`0x10034c89`)

Resolves the tile stack at the player position (`resolveTilePtrForCoords`), and
for each ground item (record type `99`) latches the pickup target into the move
globals `word_100434B8/BA/BC` (X/Y/Z) + `word_100434BD` (item id), then fires the
move. A 3-retry guard (`>3` on the same stack id) prevents an infinite pickup
loop on a stuck item. `cmd_pickupitemsamount` (`0x10034ba7`) is the count-limited
variant; `cmd_stackitems` / `cmd_moveitems` / `cmd_moveitemsonto` are the
container-to-container variants.

## Deposit — `depositLootStateMachine` (`0x10036eb6`)

A state machine over `g_102E2604` that empties loot into a depot. Depot container
id is **3147**.

| State | Action |
|---|---|
| 0 | inspect the currently-open client container (`[0x64CCD4]`): if it is the depot (3147) → state 3; else if a container is open and `[0x64CD04]` clear → `openContainerAndNotify(10,6)`; else → state 2 |
| 2 | if the open container is the depot → state 3; else `findContainerItemSlot(3147,…)` and open it |
| 3/5/7 | move qualifying items into the depot, `Sleep(350)`-poll while `g_100F0E42` (busy) is set |

The loop is gated by `dword_1005F7D5` (player mana shadow) ≥ threshold — deposit
only runs while there is enough mana to also keep healing. `[0x64CCD4]` is the
client's *currently open container id* global.

## Loot configuration

- `parseLootingLine` (`0x10016de4`) — the `[Looting]` section handler: item id +
  category token (`e`/`g`/`e1` special-cased for the loot category byte
  `0xFF`/`253`/`254`) + destination-container name → a 10-word loot record.
- `formatLootRow` (`0x10016073`) — renders a loot record back to the dialog list.
- `loadLootItemsFile` (`0x1002040d`) + `parseLootItemsPairs` (`0x100204af`) —
  memory-map `<basedir>lootitems.txt` and load up to `0x200` id→name pairs into
  the parallel arrays `g_1008BAEE` / `g_1008C2EE` (the item-name database used for
  display).
- `parseCavebotOptionLine` (`0x10016ef2`) — the `LootNearbyTargets` /
  `LootDistantTargets` / `OpenNextBp` flags that gate the whole engine.

## Globals

| Addr | Meaning |
|---|---|
| `0x64CAD0` | client container table (16 × 492 B) |
| `0x64CCD4` | client currently-open container id |
| `0x64CD04` | client container-busy/secondary flag |
| `g_102E2604` | deposit state-machine state |
| `g_1005F854/858/85C` | player X/Y/Z shadow |
| `g_1005F7D5` | player mana shadow (deposit gate) |
| `word_100434B8…BD` | pending pickup target X/Y/Z + item id |
| depot id `3147` | depot container item id |

## Detection notes

- Container item scans over the client table at `0x64CAD0` (492-byte stride) and
  reads of `[0x64CCD4]`/`[0x64CD04]` — foreign or hooked reads of these client
  globals are a loot-engine fingerprint.
- The deposit `Sleep(350)`-poll loop and the exact depot item id `3147` in a move
  sequence are behavioural tells.
- Loot moves are issued through the same synthetic event dispatcher as the rest
  of the bot (events `0x0C`/`0x11`), so they share the packet signature of the
  proxy/injection path ([`09`](09-packet-proxy.md)).
