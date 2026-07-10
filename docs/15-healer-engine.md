## Healer engine

The healer keeps the character alive and mana-topped, and casts offensive
spells/runes on the current target. It runs from two `botMainTickLoop` stages
([`13`](13-engine-tick-loop.md)): `healerManaSpellTick` (trace id 140) for
survival, and `runAttackHealerLogic` (id 150) for offence. Both read the client's
HP/mana globals directly and act by **injecting synthetic incoming packets** into
the client (the same primitive the proxy uses), not by sending real key input.

### Client state read every tick

| Client addr | Meaning |
|---|---|
| `[0x63FE94]` | current HP |
| `[0x63FE90]` | max HP |
| `[0x63FE78]` | current mana |
| `[0x63FE74]` | max mana |

### `healerManaSpellTick` (`0x1002492d`)

The survival core. It first decrements the healer cooldown bank
(`dword_10080BA2`, `dword_10080B98/9C`, `byte_10080BA0/A1`), then evaluates a
priority ladder against the HP/mana it just read. `byte_10080BA6` records what
fired this tick (`0` none, `1` heal spell, `2` potion/mana).

Ladder (highest priority first):

1. **Emergency heal spell.** If `HP < dword_10134E66` (spell threshold) and no
   heal cooldown, pick the spell for the current level from the table
   `dword_100445F8[byte_10134E63]`, set the cast record `word_1004339B` and
   `injectIncomingPacket(&word_1004339B, 15)` — a 15-byte synthetic "you cast X"
   packet — and arm cooldown `byte_10080BA1 = dword_1014F410 + 1`.
2. **Secondary heal tier.** A second threshold `dword_1014F41A` with its own spell
   table `dword_10044610[byte_1014F419]` — the "great/ultimate healing" tier.
3. **Health potion.** If `byte_100FA531` (potion enabled) and `HP <
   dword_100FA571` and `mana >= dword_100FA575`, call
   `sendPacketOpcode406(&byte_100FA531)` (use-item on self), arm
   `dword_10080BA2 = 3`. `byte_100FA4F1` / `dword_100F9499` is the second potion
   slot.
4. **Mana restore.** If mana below `dword_100F949D`, `castManaRestoreSpell` and
   count it in `dword_10080BA7` (used to re-issue a targeted queue action or an
   `injectIncomingPacket(&unk_10043315, 4)` refresh).

The two-slot health-potion + two-tier heal-spell + mana-spell structure is
exactly the Healer dialog's fields ([`10`](10-feature-subsystems.md),
`dlgProc_Healer`).

### `healByNameCommand` (`0x10024cae`)

The CiroScript `autoheal` entry. Maps a heal keyword to a spell code and queues
the cast (unless on cooldown):

| Keyword | Spell code |
|---|---|
| `health` (light heal) | 266 |
| `shealth` (strong/intense heal) | 236 |
| `ghealth` (great heal) | 239 |

### `runAttackHealerLogic` (`0x100235e8`)

Offensive casting on the current target(s). Three target-priority tiers, each a
`{flag, id}` pair:

| Tier | flag | target id | cast |
|---|---|---|---|
| 1 | `byte_100F933A` | `dword_100F9336` | if flag<4: spell 42 (needs mana ≥ **1200** `[0x63FE78]≥0x4B0`) or configured spell `dword_100F94CB` |
| 2 | `byte_100F9335` | `dword_100F9331` | if flag>4 & mana ≥1200: spell 42 |
| 3 | `byte_100F9330` | `dword_100F932C` | configured spell `dword_100F94CB` |

Each candidate is validated with `isCreatureValidTarget` (`0x100237a4`) before the
cast; casting goes through `castRuneOrSpellOnTarget` (`0x1003A60A`) followed by
`setCastCooldown` (`0x10023797`). Spell id **42** is the hardcoded high-mana nuke;
`dword_100F94CB` is the user-selected attack spell/rune. The `!byte_100F933B`
guard is the global "no-cast" gate (shared with the main tick's rune logic).

### The cast/inject primitive

Heals and casts are delivered by `injectIncomingPacket` (`0x1002ADE7`) — a
synthetic **server→client** packet fed into the parser so the client believes the
action occurred — and by `sendPacketOpcode406` for item use. This is why heals
have no visible key input and why the packet lengths (15 for a spell record, 4
for a refresh) are fixed. Detection-wise, the fingerprint is a stream of
well-formed inbound packets with no corresponding user input, correlated with the
HP/mana thresholds above.

## Key globals

| Address | Meaning |
|---|---|
| `[0x63FE94]/[0x63FE90]` | current / max HP (client) |
| `[0x63FE78]/[0x63FE74]` | current / max mana (client) |
| `dword_10134E66` | heal-spell HP threshold |
| `dword_1014F41A` | secondary heal HP threshold |
| `dword_100445F8[]` / `dword_10044610[]` | per-level heal-spell code tables |
| `byte_100FA531` / `byte_100FA4F1` | health-potion slot 1 / 2 config |
| `dword_100FA571` / `dword_100F9499` | potion HP thresholds |
| `dword_100F949D` | mana-restore threshold |
| `dword_100F94CB` | configured attack spell/rune id |
| `dword_100F9336/9331/932C` | target ids, priority tiers 1/2/3 |
| `dword_10080BA2/B98/B9C`, `byte_10080BA0/A1` | heal cooldown counters |
| `byte_10080BA6` | heal action taken this tick (0/1/2) |

## Detection notes

- Foreign reads of `[0x63FE94]`/`[0x63FE78]` (HP/mana) each tick.
- Synthetic inbound packet injection (`injectIncomingPacket`) of 15-byte cast
  records and item-use opcode 406 with no user input, correlated to HP/mana
  thresholds.
- Hardcoded mana gate of 1200 (`0x4B0`) before the spell-42 nuke, and the fixed
  heal spell codes 266/236/239.
