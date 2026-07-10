# AutoAim (aimbot) & combo engine

The PvP core — the AutoAim tab (TBOTDLG7, `dlgProc_AutoAim`) calls it "the heart
of the pvp-bot". It picks the best square to land an area rune/spell on the most
enemies while hitting **zero friends**, then casts it. Combo (TBOTDLGI) layers
multi-client burst synchronization on top.

## The aim engine — `computeBestAimSquareAndCast` `0x1003CA03`

Every `aim*` command routes here (they differ only in which rune/area pattern).
Per invocation it:

1. `snapshotPlayerStats` `0x10024FAE` — refresh the player position
   (`g_10052768`/`g_1005276C`/`g_10052770` = x/y/z).
2. Zero six scan grids (`memset` `0x1002AE81` ×6) — the per-square enemy-count /
   friend-count / reachability accumulators.
3. Walk the shadow creature table, classify each creature **friend vs enemy**
   using the Friends/Enemies flags (`g_1014F41E` / `g_1014F41F`, set by the
   Friends/Enemies tab), and stamp its position into the grids.
4. For every candidate cast square, score = enemies covered by the area pattern,
   **rejecting any square whose pattern touches a friend** (or a protection
   zone / non-line-of-sight tile via `isCreatureReachableWalkable`
   `0x1003BC09`).
5. Pick the highest-scoring square and cast the configured rune/spell at it via
   `castRuneOrSpellOnTarget` `0x1003A60A` (which writes the "use rune on tile"
   packet). Falls back to `autoaim` on the current target
   (`g_10080BCB`/`g_10080BB3`, shared with [targeting](16-targeting-engine.md))
   when no multi-hit square beats the threshold.

The area pattern is what distinguishes the commands:

| Command | Rune / spell | Pattern |
|---|---|---|
| `aimgfb` (`cmd_gfbsd`) | Great Fireball | 3×3 |
| `aimavalanche` | Avalanche | 3×3 |
| `aimstoneshower` | Stone Shower | cross/large |
| `aimthunderstorm` | Thunderstorm | large area |
| `explo` | Explosion | 3×3 |
| `icicle` / `stalagmite` | icicle / stalagmite runes | single/line |
| `hmm` / `lmm` | heavy/light magic missile | single |
| `sd` (`cmd_sd`) | Sudden Death | single target |
| `aimtype <rune>` | configure the fallback `autoaim` rune | — |
| `autoaim` | cast the fallback rune at the best single enemy | 1 |

## Relations to other tabs

- **Friends/Enemies** (TBOTDLGH, `dlgProc_FriendsEnemies`) — supplies the
  friend/enemy/subfriend/subenemy name lists that drive the "zero friends"
  constraint. Without a correct classification the aimbot would hit teammates.
  Flags `g_1014F41E`/`g_1014F41F` are the live per-creature classification the
  engine reads.
- **Targeting** ([16](16-targeting-engine.md)) — shares the current-target
  pointers `g_10080BCB`/`g_10080BB3`; `autoaim`/`sd` fall back to the active
  target. Targeting picks *who* to attack; the aimbot decides *where* to drop the
  area rune.
- **Hotkeys** ([24](24-hotkeys-alarms.md)) — `aim*` are normal CiroScript
  commands, so they are bound to hotkeys (or `auto`-fired) like anything else;
  the "autoaim hotkey" and combo binds are the usual trigger.

## Combo — `dlgProc_AutoAimCombo` (TBOTDLGI)

The combo tab coordinates a **synchronized burst** across multiple bot clients
(a "combo" of players SD-ing one target at once):

- Action mode (No Action / Attack / Follow), a 200–2000 ms delay, a leader/name
  list, and the combo rune (SD).
- `autocomboon` (`cmd_autocomboon`, `g_...`) arms it; `alt`/`ctrl`/`shift`/`key`
  modifiers gate manual triggering.
- Coordination rides the **NavNet** channel ([18](18-navnet-codec.md)): the
  leader's `navsay`/position triggers the followers' combo cast on the same
  target within the configured delay, so several clients land SD in the same
  server tick.

So the PvP path is: Friends/Enemies classify → Targeting selects → aimbot places
the area rune (zero friends) → Combo synchronizes the burst across the NavNet
party. All are CiroScript-command-driven and fire from the hotkey/tick engine.
