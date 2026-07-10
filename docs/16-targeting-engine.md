## Targeting engine

ElfBot NG 8.60 (`elfbot.dll`, imagebase `0x10000000`) auto-attack / targeting subsystem. Injected into Tibia 8.60 (`Tibia.exe`, imagebase `0x00400000`). The engine reaches directly into the client's process memory — both to *read* the battle-list / creature tables and to *write* fake incoming packets and outfit bytes. There is no network layer here: "attacking" is done by forging server→client packets into the client's own receive path.

Two of the six seed functions are the periodic drivers, scheduled from `botMainTickLoop` (0x100227bd):

| Function | Addr | Role | Cadence |
|---|---|---|---|
| `scanBattleListStatusTick` | 0x10023a8f | maintain battle-list shadow, classify/color creatures, alarm counters | every tick |
| `targetingAttackScanTick` | 0x10023893 | cavebot loot/attack container scan, forge attack packet | `rand()%100 + 50` ms, gated by throttle byte |
| `resolveActiveCreaturePtr` | 0x10023a45 | resolve active-target pointer into `dword_1005E19C` | per decision |
| `pickAttackTarget` | 0x1002355e | choose best target (lure → priority) | on demand |
| `handleAttackTargetOnTile` | 0x10027176 | per-frame HUD/scan tick, tile-grid target update | per frame |
| `dequeueMarkedCreature` | 0x1003bb22 | pop one marked shadow entry, inject marker packet | on demand |

### Client memory map the engine touches

These are absolute addresses in the *Tibia 8.60 client* (not elfbot). They are the primary memory-detection surface — an anti-cheat that watches these regions for external reads/writes catches the bot.

| Client global | Meaning | Stride / size |
|---|---|---|
| `0x63FEF8 … 0x64A308` | **Battle-list array** — 250 creature records | 168 bytes each |
| `0x63FE78` | local player **mana** (compared `>= 0x4B0`=1200) | dword |
| `0x63FEDC` | client state byte cleared on socket-stop path | byte |
| `0x64CD10 … 0x64EBD0` | **open-container table** — 16 slots | 492 bytes each |
| `0x64CD4C` (`0x64CD10+0x3C`) | first item-id array inside a container slot | dword[] |
| `0x64A9C0` | client "map loaded / game state" gate (`==31` = in-game) | byte |
| `0x64CCB0` | last right-clicked / use-target creature id | dword |
| `0x7998DC` | pointer to the **creature id-table** descriptor | ptr |

Battle-list record fields used by `scanBattleListStatusTick`:

```
+0    creature id (dword; entry occupied when != 0)
+4    name (WORD compared to 19783/19779; name string base for matchers)
+44   position/floor field (compared to dword_1005F85C)
+96   outfit lookType (0 = no outfit / item-outfit)
+100  outfit color: head
+104  outfit color: body
+108  outfit color: legs
+112  outfit color: feet
+144  "visible / on-screen" flag (record processed only when non-zero)
```

### scanBattleListStatusTick — battle-list shadow + HUD coloring (0x10023a8f)

Walks all 250 battle-list records. For each occupied+visible entry (`+144 != 0`) it runs the four name-list matchers and, when a match hits, both tags the shadow record and **overwrites the client's outfit-color bytes** with a fixed palette so the creature is color-coded on screen:

| Matcher | List global | HUD code (`v6[81]`) | Outfit color written |
|---|---|---|---|
| `matchNameAgainstListA` (targeting) | `unk_100638A8` | 1 | 106 |
| `matchNameAgainstListB` | `byte_1005F8A8` | 2 | 96 |
| `matchNameAgainstListC` | `unk_100678A8` | 4 | 77 |
| `matchNameAgainstListD` | `unk_1006B8A8` | 3 | 87 |

Before overwriting, the original head/body/legs/feet colors are saved into the shadow record (`v6[132..135]`, backup-valid flag `v6[136]`) and `byte_100EE8C8` is set. A second pass at the bottom of the function *restores* those original colors from the shadow backup when coloring is disabled (`byte_100EE8C8 && !byte_10135278`) — a save/restore so the recolor is transient and reversible. The recolor is gated by `byte_100F94C7` (HUD-color on) and `byte_10135278` (write-to-client on).

Two population counters are accumulated: `v3` (creatures matching name-word 19783/19779 or `+96==75`) → `dword_100F49C9`, and `v4` (unmatched hostiles on the player's floor: `*(dword)i < 0x40000000`, `i != dword_1005F7ED` [the player's own record], `dword_1005F85C == *(i+44)`) → `dword_100F49CD`. Each drives `handleAlarmTriggers` when its per-alarm mask row in `dword_10207F12` is armed. `dword_1005F7ED` is the local-player creature record pointer; the `!= player` test is how the bot excludes itself from the enemy count.

The shadow table (`byte_10077175`, 156-byte stride, `v6 += 156`) runs in lockstep with the battle-list (`i += 168`) — element *n* of one maps to element *n* of the other.

### The name matchers — matchNameAgainstList{A,B,C,D} (0x1003a320 / 494 / 550 / 3da)

Four identical routines over four 512-entry × 32-byte name tables. Each entry is a NUL-terminated pattern; empty first byte ends the list. Prefix grammar:

```
'*'         (byte 42)   → suffix/owner match against caller field +32
"++" (0x2B2B = 11051)   → match name+2 (double-plus prefix)
'+'         (byte 43)   → match name+1 (single-plus prefix)
(none)                  → exact lstrcmpi against the 32-byte pattern
```

Each is guarded by `checkPlayerOnTileFilter` (sub_1003a1e5) returning a list-index (1=B,2=C,3=D,4=... ) — a player-on-tile override so a specific tile's occupant can be forced into a list. Match returns 1.

| List | Table global | Entries | Purpose (inferred) |
|---|---|---|---|
| A | `unk_100638A8` | 512×32 | targeting monster list (attack) |
| B | `byte_1005F8A8` | 512×32 | secondary / friend list |
| C | `unk_100678A8` | 512×32 | list C |
| D | `unk_1006B8A8` | 512×32 | list D |

### targetingAttackScanTick — cavebot loot/attack tick (0x10023893)

Runs on the `rand()%100+50` ms schedule. Structure:

```
if (byte_100F45BC) { --byte_100F45BC; }          // throttle: skip N ticks after an action
else if ((byte_100F9326||byte_1014F418) && dword_100F9318 != -1) {
    dword_100F0DF8 = 5;                            // set bot sub-state
    if (dword_100F9318)  findContainerItemAndNotify(0,1);   // loot open container
    else { build 12-byte packet from 0x64CCB0 → injectIncomingPacket }  // attack last-used creature
}
else if (byte_10207F35) {                          // auto-attack enabled
    for i in 0..15:                                 // 16 container slots @ 492 bytes
      if slot occupied && item-count == capacity:
        walk item array (v2 = slot+0x64CD4C, +=3 dwords):
          if (getCreatureFlagsDword(*v2) & 0x10):   // flag 0x10 = attackable/targetable
            fill byte_100434D2 attack record, inject 12-byte packet, set throttle=6, return
}
```

The 12-byte record at `byte_100434D2` (fields `byte_100434D7/D9/DA/DC/DD`) is the forged **"attack creature" opcode** written into the client via `injectIncomingPacket`. `byte_100434D7 = i + 64` encodes the container/slot; `word_100434DA` is the creature id. Throttle byte `byte_100F45BC` is set to 6 or 10 after every injection to space out actions.

`getCreatureFlagsDword` (0x1003c4fa) reads the client creature descriptor:

```c
return *(DWORD*)( *(DWORD*)(MEMORY[0x7998DC] + 8)     // id-table base
                  + 76 * (a1 - *MEMORY[0x7998DC])     // 76-byte records, indexed by id-min
                  + 36 );                             // flags dword at +36
```

Flag bit `0x10` = the "is a valid attack target" bit the engine keys on.

### resolveActiveCreaturePtr — active-target resolution (0x10023a45)

```c
if (dword_100F9355)                       // sticky/forced target set
    dword_1005E19C = dword_100F9355;
else {
    if (runAttackHealerLogic(0)) {         // 0x100235e8 — heal/support cast first
        p = pickAttackTarget();            // 0x1002355e — else pick attack target
        dword_1005E19C = p ? *p : 0;
    } else dword_1005E19C = ...;
}
```

`dword_1005E19C` is the resolved **current-target pointer** the rest of the bot reads. `dword_100F9355` is a forced/locked target override.

`runAttackHealerLogic` (0x100235e8) is a 3-tier cast decision (`byte_100F933A` / `byte_100F9335` / `byte_100F9330` priority levels). It validates the candidate with `isCreatureValidTarget`, checks mana `MEMORY[0x63FE78] >= 0x4B0` (1200) and cooldown `byte_100F933B`, then casts via `castRuneOrSpellOnTarget(targetId, spellCode)`. Spell code **42** is the fixed high-priority spell; `dword_100F94CB` is the configured default spell code. `setCastCooldown` re-arms the cooldown after each cast.

### pickAttackTarget — priority selection (0x1002355e)

```c
if (dword_10080BCB && dword_10080BCF && byte_1014F41F && isCreatureReachableWalkable(dword_10080BCB))
    return dword_10080BCB;                 // cavebot lure creature (primary)
if (dword_10080BB7 && dword_10080BB3 && byte_1014F41E && isCreatureReachableWalkable(dword_10080BB3))
    return dword_10080BB3;                 // lure creature (secondary)
result = selectBestTargetByPriority(0);    // full priority scan
if (!result && byte_1013F27F)
    result = selectBestTargetByPriority(0);// retry with relaxed constraints
return result;
```

Selection order: **lure targets first** (kept for cavebot spawn-luring), then a full priority scan `selectBestTargetByPriority`. Both lure paths are gated on `isCreatureReachableWalkable` — this is the **walker interaction**: a creature is only chosen if the pathfinder can actually reach it, so targeting never picks a target the walker can't walk to. `dword_10080BCB/BB3` are the lure-creature id globals; `byte_1014F41F/1E` enable each lure slot.

### dequeueMarkedCreature — pop marked shadow entry (0x1003bb22)

Scans the shadow table (`byte_10077175 … byte_100809CD`, 156-byte stride) for the *last* entry with action-flag `v0[80]` set and not skipped (`v0[77]` set, and not `v0[79] && byte_101D5E20`). On finding one it clears the flag and publishes the creature's map position into the marker packet buffer:

```
word_1004332B = *(WORD*)(rec+36)    // x
word_1004332D = *(WORD*)(rec+40)    // y
byte_1004332F = *(BYTE*)(rec+44)    // z (floor)
word_10043330 = 99                  // marker sub-type
injectIncomingPacket(byte_10043328, 11)   // 11-byte marker packet
byte_10080B6D = 1                    // "have marker" flag  (0 if none)
```

Shadow record fields: `+77` skip/consumed flag, `+79` conditional-skip flag, `+80` action-pending flag, `+16*4`(=+64) pointer to the live creature record (from which x/y/z at +36/+40/+44 are read).

### injectIncomingPacket — the injection primitive (0x1002ade7)

The core of "attack without sending a real packet". Gated on `!byte_100F0D36` (injection enabled) and `MEMORY[0x64A9C0] == 31` (client in-game). Under a critical section it copies the caller's payload into the client's incoming-packet buffer `dword_1004266C+8` (length `*(WORD*)a1 + 8`, capacity marker `2048`), sets `byte_1004287C` = "synthetic packet in flight", and calls the client's packet-dispatch stub `lpAddress(1)`. The client then processes the forged packet as if the server sent it. `handleIncomingPacketOpcodesLite` pre-processes opcode bytes. This is the single most detectable behavior: an external module driving the client's own receive-parser with hand-built packets.

```c
if (!byte_100F0D36 && MEMORY[0x64A9C0] == 31) {
    EnterCriticalSection(&CriticalSection);
    handleIncomingPacketOpcodesLite(a1, ...);
    len = *(WORD*)a1 + 8;
    *(DWORD*)buf = 0; *(DWORD*)(buf+4) = 0;
    memcpy(buf+8, a1+2, len-8);
    byte_1004287C = 1;
    lpAddress(1);                 // client incoming-packet dispatch
    byte_1004287C = 0;
    LeaveCriticalSection(&CriticalSection);
}
```

### findContainerItemAndNotify — loot scan (0x10037100)

Walks the 16 container slots (492-byte stride, item array at slot+0x64CD4C). Matches by container-id / item-id, or the special auto-loot range `v4 >= 0xDA9 && v4 <= 0xDAC` (item ids 3497–3500 — corpse/loot-bag ids). When `a3==0` it filters items by `getCreatureFlagsDword & 0x10`. On the Nth match it fills the same `byte_100434D2` attack/move record and injects a 12-byte packet, optionally routing to a free creature/container slot via `findFirstEmptyCreatureSlot`.

### parseTargetingRecord — config parser (0x1001686c)

Parses ElfBot's `.elf` script text into the shadow tables. Splits on CR/LF, dispatches `[Section]` headers via `lstrcmpi` against a fixed section-name set: `Waypoints`, `Looting`, `CavebotOptions`, `Alerts`, `CavebotHotkeys`, `TargetingMonster`, `TargetSelection`, `StanceOptions`, `Icons`. Each section zeroes then repopulates its backing tables — notably `TargetingMonster` clears `dword_101D5E78` (0xA000 bytes) and `TargetSelection` clears the waypoint/name buffers. Section body lines are dispatched via a computed jump `jmp [ebp+var_808]` into per-section `loc_` handlers. On completion it refreshes the cavebot (`refreshCavebotDialog`) and targeting (`populateTargetingDialogLists`) GUI dialogs. This is where the name-list globals (`unk_100638A8` et al.) and the targeting-record fields are populated from user config.

### Target lifecycle summary

1. `scanBattleListStatusTick` reads the client battle-list, classifies each creature against the name-lists, colors it on the HUD (write to client outfit bytes), and keeps the 156-byte shadow table in sync.
2. `resolveActiveCreaturePtr` → `runAttackHealerLogic` (support casts) → `pickAttackTarget` (lure → walker-reachable priority scan) picks the target id into `dword_1005E19C`.
3. `targetingAttackScanTick` / `findContainerItemAndNotify` build the 12-byte attack record `byte_100434D2` and inject it via `injectIncomingPacket`, then throttle for 6–10 ticks.
4. `dequeueMarkedCreature` publishes marked creatures' coords and injects an 11-byte marker packet.

All attack/mark/loot actions are delivered as **forged incoming packets**, never real outgoing traffic — packet-side detection must watch the client's *receive* parser being driven while the socket is idle.

## Key globals

| Address | Meaning |
|---|---|
| `0x63FEF8` | Client battle-list array base: 250 creature records, 168-byte stride, runs to 0x64A308. Primary read surface. |
| `0x63FE78` | Local player mana (client). Compared >= 0x4B0 (1200) before casting. |
| `0x64A9C0` | Client game-state gate; ==31 means in-game/map-loaded (injection guard). |
| `0x64CD10` | Open-container table base: 16 slots, 492-byte stride to 0x64EBD0; item-id array at slot+0x3C (0x64CD4C). |
| `0x64CCB0` | Last right-clicked / use-target creature id used to build the attack packet. |
| `0x7998DC` | Pointer to the client creature id-table descriptor; 76-byte records, flags dword at +36, bit 0x10 = attackable. |
| `0x10077175` | elfbot shadow creature table base: 156-byte stride to 0x100809CD, mirrors battle-list; holds HUD color code (+81), outfit backup (+132..136), action flags (+77/79/80). |
| `0x100638A8` | Name list A (targeting/attack): 512 entries x 32 bytes, wildcard patterns. |
| `0x1005F8A8` | Name list B: 512x32 name patterns. |
| `0x100678A8` | Name list C: 512x32 name patterns. |
| `0x1006B8A8` | Name list D: 512x32 name patterns. |
| `0x100434D2` | 12-byte forged attack/move packet record (fields at +5=D7 slot, +7=D9, +8=DA creature id word, +A=DC, +B=DD). |
| `0x10043328` | 11-byte marker packet buffer; x at 0x1004332B, y at 0x1004332D, z at 0x1004332F, sub-type 0x10043330. |
| `0x1004266C` | Pointer to the client's incoming-packet buffer written by injectIncomingPacket; payload at +8, capacity marker 0x10042670=2048. |
| `0x1005E19C` | Resolved current-target pointer written by resolveActiveCreaturePtr. |
| `0x100F9355` | Forced/locked target id override (sticky target). |
| `0x100F45BC` | Auto-attack throttle countdown byte; set to 6/10 after each injected action to space actions out. |
| `0x10207F35` | Auto-attack-enabled flag gating the container attack scan. |
| `0x100F49C9` | Live count of matched/priority creatures (written each battle-list scan). |
| `0x100F49CD` | Live count of unmatched hostiles on the player's floor. |
| `0x1005F7ED` | Local-player creature record pointer (used to exclude self from enemy count). |
| `0x10080BCB` | Primary cavebot lure creature id (targeted first if walker-reachable). |
| `0x10080BB3` | Secondary lure creature id. |
| `0x10207F12` | Per-alarm mask/config rows (3-byte stride) driving handleAlarmTriggers and triggerAlarmAction. |
| `0x10052660` | Array of DirectSound buffer objects, one per alarm row, played on trigger. |
| `0x100F94CB` | Configured default attack spell code passed to castRuneOrSpellOnTarget. |
| `0x10135278` | Enable write-to-client outfit recolor (byte_10135278). |
| `0x100F94C7` | Enable HUD color-coding (sets shadow +81 codes). |
| `0x100F0D36` | Injection-disabled flag (guards injectIncomingPacket). |

## Detection notes

- Forged incoming packets while socket idle: injectIncomingPacket (0x1002ade7) writes into the client's incoming-packet buffer at *(0x1004266C)+8 and calls the client dispatch stub lpAddress(1) with byte_1004287C=1 as an in-flight marker. Anti-cheat can hook/instrument the client's packet-parse entry and flag packets that arrive with no corresponding recv() from the socket.
- External writes to battle-list outfit bytes: scanBattleListStatusTick overwrites client offsets +100/+104/+108/+112 (outfit colors) with fixed palette values 106/96/77/87 for matched creatures. A memory guard on the battle-list region (0x63FEF8..0x64A308) catches these writes; the fixed color constants are a signature.
- Fixed absolute client addresses: the engine hardcodes 0x63FE78 (mana), 0x63FEF8 (battle-list), 0x64A9C0 (state==31), 0x64CCB0, 0x64CD10 (containers), 0x7998DC (creature id-table). Any external process reading these exact addresses (VirtualQueryEx/ReadProcessMemory patterns, or a guard-page trap) fingerprints the bot.
- Shadow tables in elfbot's own module: 250x156-byte table at 0x10077175 mirroring the client battle-list, and four 512x32 name-list tables at 0x100638A8/0x1005F8A8/0x100678A8/0x1006B8A8. Scanning the injected DLL's data section for a 156-byte-stride mirror of the client's 168-byte creature records is a strong heuristic.
- Timing signature: targetingAttackScanTick fires on rand()%100+50 ms and self-throttles via byte_100F45BC (6-10 tick gaps after each action). Attack packets clustered at ~50-150ms jittered intervals, always as injected (not sent) packets, with no mouse/keyboard input preceding them, is a behavioral tell.
- getCreatureFlagsDword (0x1003c4fa) dereferences *(0x7998DC) and reads flags at record+36 masking 0x10 — an external read of the client's private creature descriptor table indexed by id-min; watching reads of *(0x7998DC)+8 from outside the client's own code catches the targeting scan.
- Marker packet with sub-type 0x63 (99) at word_10043330 built in dequeueMarkedCreature and injected as an 11-byte packet — a specific forged opcode/payload shape that can be signatured on the injected receive path.
