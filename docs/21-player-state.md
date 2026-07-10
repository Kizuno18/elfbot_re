## Player-state snapshot & exp meter

elfbot's `stats_exp` engine is the read side of the bot's model of the local character. It never modifies client memory — it copies a handful of fixed Tibia 8.60 globals into a private "shadow" region each tick, keeps a rolling experience-rate window, and tracks per-slot status/light transitions with wall-clock timestamps. The other engines (cavebot, targeting, healer, HUD) read the shadow region instead of poking the client themselves, which is why this engine's reads are the canonical client-memory-access fingerprint for the whole bot.

Called from `botMainTickLoop` (0x100227bd) on a timed schedule (documented separately). Three seed entrypoints, two shared leaf helpers.

### Call graph

```
botMainTickLoop (0x100227bd)
  ├─ snapshotPlayerStats     0x10024fae   (client → shadow, hp/mp/pos)
  ├─ pushExpSampleWindow     0x10023e42   (exp/hour rolling window)
  │    └─ intToAsciiDecimal  0x10040940   (int → status-bar ASCII)
  └─ syncClientLightState    0x1002997f   (status/light table diff + timestamps)
       └─ GetTickCount       0x10040748   (import thunk)
```

---

### snapshotPlayerStats — 0x10024fae

A flat, branchless copy of five hardcoded client globals into shadow state. This is the single hottest client-memory reader in the bot.

```c
int snapshotPlayerStats()
{
  dword_1005F7D1 = MEMORY[0x63FE94];   // HP        <- client HP
  dword_1005F7D5 = MEMORY[0x63FE78];   // mana      <- client mana
  dword_10052768 = MEMORY[0x64F608];   // Z (floor) <- client pos.z
  dword_1005276C = MEMORY[0x64F604];   // Y         <- client pos.y
  dword_10052770 = MEMORY[0x64F600];   // X         <- client pos.x
  return MEMORY[0x64F600];             // returns X
}
```

Client-source layout (Tibia 8.60 client, absolute addresses):

| Client addr | Meaning        | Shadow dst    | Notes |
|-------------|----------------|---------------|-------|
| `0x63FE94`  | Player HP      | `0x1005F7D1`  | dword read |
| `0x63FE78`  | Player mana    | `0x1005F7D5`  | dword read |
| `0x64F600`  | Player pos X   | `0x10052770`  | self-coord block base |
| `0x64F604`  | Player pos Y   | `0x1005276C`  | |
| `0x64F608`  | Player pos Z   | `0x10052768`  | floor level |

Two independent client regions are read: the vitals pair lives in the `0x63FExx` status block (adjacent to the light/status table `syncClientLightState` walks), and the position triple lives in the `0x64F600` self-coordinate block. HP and mana shadows are stored 4 bytes apart (`0x1005F7D1`, `0x1005F7D5`), immediately below the light-state shadow region — the whole player mirror is one packed struct in bot memory.

The shadow position triple `0x10052768/6C/70` is stored Z,Y,X in ascending address order (Z lowest). Other engines index it as a `{z,y,x}` block.

---

### pushExpSampleWindow — 0x10023e42

Maintains a 10-sample circular buffer of experience deltas and reduces it to a single rolling total. Driven on the exp-window cadence (a slower tick than the stat snapshot).

```c
int pushExpSampleWindow()
{
  if ( ++dword_1008B8D4 == 10 )       // advance write index, wrap at 10
    dword_1008B8D4 = 0;
  dword_1008B8AC[dword_1008B8D4] = dword_1008B8A8;  // store accumulated delta
  dword_1008B8A8 = 0;                 // reset accumulator for next interval
  int sum = 0;
  for (unsigned i = 0; i < 10; ++i)
    sum += dword_1008B8AC[i];         // sum all 10 slots
  dword_1008B8D8 = sum;               // rolling total (exp/hour figure)
  return intToAsciiDecimal(dword_100580F0, &aStime[11]);  // render counter to status string
}
```

Structure:

| Global         | Type        | Role |
|----------------|-------------|------|
| `0x1008B8A8`   | dword       | Per-interval exp accumulator; another path (kill/loot handler) adds gained exp here; zeroed each window advance. |
| `0x1008B8AC`   | dword[10]   | Circular buffer of the last 10 interval deltas. |
| `0x1008B8D4`   | dword       | Write index (0..9), pre-incremented with wrap. |
| `0x1008B8D8`   | dword       | Sum of all 10 slots — the displayed exp/hour value. |
| `0x100580F0`   | dword       | A separate counter rendered into the status/HUD string (`&aStime[11]`, offset 11 into an `"stime"`-ish status buffer). |

With 10 slots summed on a fixed interval, `dword_1008B8D8` is a windowed exp rate (slot count × interval = the averaging window). The final `intToAsciiDecimal` call is unrelated to the exp sum — it stamps `dword_100580F0` into a fixed spot in a HUD/status string buffer (`aStime`), i.e. a side-effect status-bar update piggybacked on the timer.

---

### syncClientLightState — 0x1002997f

Diffs a client status/light table against a shadow copy and records timestamped transitions. This is the most detection-relevant function: it walks a hardcoded stride-4 client array, keeps a byte-per-slot shadow, and a per-slot 0/1/2 state machine with two GetTickCount arrays.

Client table geometry (all absolute client addresses):

- Primary table base: `0x63FE40`, stride 4.
- First loop bound `< 0x63FE5C` → 7 slots at `0x63FE40, 44, 48, 4C, 50, 54, 58`.
- Second loop bound `< 0x63FE60` → 8 slots (`0x63FE40 … 0x63FE5C`).
- Companion byte read at `v1 - 28` (i.e. `0x63FE24 + i*4`) — a parallel region 28 bytes below the primary table.
- Special-cased slot: when the cursor hits `0x63FE5C`, the byte is instead sourced from `0x63FE7C`.
- Extra scalar reads: `0x63FE84` → `byte_1005F7F8`; `0x63FE7C` → `byte_1005F800`.

```c
char syncClientLightState()
{
  // gated refresh: only rebuild the shadow copy when a version/epoch dword changed
  if ( dword_1005F7E5 != dword_1005F7E9 )
  {
    dword_1005F7E9 = dword_1005F7E5;              // latch new epoch
    for (v1 = 0x63FE40, v2 = 0; v1 < 0x63FE5C; v1 += 4, ++v2) {
      byte_1005F7F1[v2] = *(BYTE*)v1;             // primary table byte -> shadow A
      byte_1005F7F9[v2] = *(BYTE*)(v1 - 28);      // companion byte   -> shadow B
    }
    byte_1005F7F8 = MEMORY[0x63FE84];             // trailing scalar
    byte_1005F800 = MEMORY[0x63FE7C];             // trailing scalar
    dword_1005F809 = 0;                           // clear all per-slot state flags
  }

  // per-slot change detection with timestamping
  for (v3 = 0x63FE40, v4 = 0; v3 < 0x63FE60; v3 += 4, ++v4) {
    BYTE cur = *(BYTE*)(v3 - 28);                 // companion byte for this slot
    if ( v3 == 0x63FE5C )
      cur = MEMORY[0x63FE7C];                     // slot 7 override
    if ( cur != byte_1005F7F9[v4] ) {             // changed vs shadow B?
      byte_1005F7F9[v4] = cur;
      if ( (&dword_1005F809)[v4] && cur ) {       // was already flagged AND non-zero now
        (&dword_1005F809)[v4] = 2;                // state = re-seen
        dword_1005F831[v4] = GetTickCount();      // re-seen timestamp
      } else {
        (&dword_1005F809)[v4] = 1;                // state = first-seen
        byte_1005F801[v4] = cur;                  // cache the new value
        dword_1005F811[v4] = GetTickCount();      // first-seen timestamp
      }
    }
  }
  return ...;
}
```

Per-slot state machine (`byte`-indexed off `dword_1005F809`):

| Value | Meaning |
|-------|---------|
| 0 | Never seen / reset by epoch change |
| 1 | First transition observed → `dword_1005F811[i]` stamped, value cached in `byte_1005F801[i]` |
| 2 | Subsequent non-zero transition → `dword_1005F831[i]` stamped |

The two timestamp arrays give the rest of the bot "when did slot i first change" and "when did it last change" — consistent with tracking on-screen creatures/status icons (light, party, skull, or similar per-entity flags) appearing and reappearing, used by targeting/anti-idle logic to age entries.

### Shadow-state memory map (bot side, imagebase 0x10000000)

Contiguous player-mirror block, low→high address:

| Bot addr      | Type      | Written by | Meaning |
|---------------|-----------|------------|---------|
| `0x1005F7D1`  | dword     | snapshot   | HP |
| `0x1005F7D5`  | dword     | snapshot   | mana |
| `0x1005F7E5`  | dword     | (client)   | light/status epoch, read by sync |
| `0x1005F7E9`  | dword     | sync       | latched epoch (last-processed) |
| `0x1005F7F1`  | byte[7]   | sync       | shadow copy A (primary table) |
| `0x1005F7F8`  | byte      | sync       | scalar from `0x63FE84` |
| `0x1005F7F9`  | byte[8]   | sync       | shadow copy B (companion, diffed each tick) |
| `0x1005F800`  | byte      | sync       | scalar from `0x63FE7C` |
| `0x1005F801`  | byte[8]   | sync       | cached new value per slot on first-seen |
| `0x1005F809`  | byte[8]   | sync       | per-slot state flags (0/1/2) |
| `0x1005F811`  | dword[8]  | sync       | first-seen GetTickCount per slot |
| `0x1005F831`  | dword[8]  | sync       | re-seen GetTickCount per slot |
| `0x10052768`  | dword     | snapshot   | pos Z |
| `0x1005276C`  | dword     | snapshot   | pos Y |
| `0x10052770`  | dword     | snapshot   | pos X |
| `0x100580F0`  | dword     | (elsewhere)| HUD counter rendered by exp meter |
| `0x1008B8A8`  | dword     | exp meter  | interval exp accumulator |
| `0x1008B8AC`  | dword[10] | exp meter  | exp sample ring |
| `0x1008B8D4`  | dword     | exp meter  | ring write index |
| `0x1008B8D8`  | dword     | exp meter  | rolling exp total |

---

### intToAsciiDecimal — 0x10040940

`__stdcall(int a1, BYTE* a2)`. Standard reverse-build itoa: `'0'` fast path when `a1 == 0` (writes the WORD `0x0030` = `"0\0"`); writes a leading `'-'` for negatives; emits digits least-significant-first via `v2 /= 10`, NUL-terminates, then in-place reverses the digit span. Pure leaf, no globals. Used here to stamp the exp/status counter into the HUD string; shared with other formatting sites.

### GetTickCount — 0x10040748

Plain IAT thunk to `kernel32!GetTickCount`. The millisecond timestamps in `dword_1005F811` / `dword_1005F831` are `kernel32` tick counts, not client time.

## Key globals

| Address | Meaning |
|---|---|
| `0x1005F7D1` | Shadow player HP; copied from client 0x63FE94 by snapshotPlayerStats each tick. |
| `0x1005F7D5` | Shadow player mana; copied from client 0x63FE78. |
| `0x10052770` | Shadow player position X; from client 0x64F600. Base of the {Z@2768, Y@276C, X@2770} self-coordinate block consumed by cavebot/targeting. |
| `0x1005276C` | Shadow player position Y; from client 0x64F604. |
| `0x10052768` | Shadow player position Z (floor); from client 0x64F608. |
| `0x1008B8A8` | Per-interval experience accumulator; summed exp gained since last window advance, zeroed by pushExpSampleWindow. |
| `0x1008B8AC` | 10-slot circular buffer of per-interval exp deltas (exp/hour sample ring). |
| `0x1008B8D4` | Write index (0..9, wraps) into the exp sample ring. |
| `0x1008B8D8` | Sum of all 10 exp ring slots — the displayed rolling exp/hour figure. |
| `0x100580F0` | HUD/status counter dword rendered to ASCII (into aStime[11]) by the exp meter. |
| `0x1005F7E5` | Client light/status-table epoch/version dword; when it differs from the latched copy the shadow table is rebuilt. |
| `0x1005F7E9` | Latched (last-processed) epoch value for the light/status table. |
| `0x1005F7F1` | Shadow copy A of the primary client status table 0x63FE40 (7 bytes). |
| `0x1005F7F9` | Shadow copy B (companion region 0x63FE24, diffed each tick, 8 slots). |
| `0x1005F801` | Per-slot cache of the newly-observed value on a first-seen transition (8 bytes). |
| `0x1005F809` | Per-slot transition state flags, 0=unseen 1=first-seen 2=re-seen (8 bytes). |
| `0x1005F811` | Per-slot GetTickCount timestamp of the first observed transition (8 dwords). |
| `0x1005F831` | Per-slot GetTickCount timestamp of a subsequent transition (8 dwords). |
| `0x1005F7F8` | Shadow scalar copied from client 0x63FE84. |
| `0x1005F800` | Shadow scalar copied from client 0x63FE7C. |

## Detection notes

- Fixed-address client reads with no pointer walk: repeated reads of Tibia 8.60 globals 0x63FE94 (HP), 0x63FE78 (mana), 0x64F600/604/608 (X/Y/Z) at high frequency from a foreign module. An in-client integrity check can hardcode these addresses and watch which module's code accesses them (e.g. VEH/page-guard on the self-coordinate block, or a scan of return addresses landing in elfbot.dll's 0x1002xxxx range).
- The five snapshot reads form a fixed instruction signature at 0x10024fb5..0x10024fea: five mov-from-absolute-address into a contiguous 0x1005F7D1/0x1005F7D5 + 0x10052768/6C/70 destination block. A byte-pattern scan for these absolute operands (0x63FE94, 0x63FE78, 0x64F600 immediates back-to-back) uniquely fingerprints this build.
- Shadow-state region 0x1005F7D1–0x1005F831 is a stable, densely-packed struct that always mirrors live client values one tick behind. An anti-cheat with read access to the bot module can correlate 0x1005F7D1 == client HP and 0x10052770 == client X to prove memory-mirroring — near-zero false positives.
- syncClientLightState reads from client 0x63FE40 (stride-4, 8 slots) plus the companion region 28 bytes below and scalars at 0x63FE7C/0x63FE84 — an access pattern (7-8 sequential stride-4 reads of the status table by non-client code) that a client-side trap on that table would catch.
- Two GetTickCount timestamp arrays (0x1005F811 first-seen, 0x1005F831 re-seen) plus a 10-slot exp-rate ring at 0x1008B8AC are bot-only bookkeeping absent from a legitimate client — their presence/shape is a static-scan signature in a memory dump of the process.
- The exp meter's fixed 10-sample ring summed into 0x1008B8D8 produces a suspiciously regular exp/hour readout; behaviourally, perfectly periodic sampling and status-string updates (aStime buffer writes) betray automated, timer-driven bookkeeping rather than a human client.
