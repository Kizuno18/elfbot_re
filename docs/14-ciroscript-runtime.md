## CiroScript runtime engine

ElfBot NG 8.60 (`elfbot.dll`, imagebase `0x10000000`) drives its cavebot, targeting and hotkey automation from a text-scripting interpreter this doc calls **CiroScript**. It is invoked once per bot tick from `botMainTickLoop (0x100227bd)` (documented elsewhere) and runs the currently-loaded, still-in-source-form scripts by walking a set of flat action tables, evaluating conditions, and dispatching command verbs through three perfect-hash dictionaries. Nothing is compiled to bytecode — the "compiled command stream" is the ASCII script body itself, split on structural characters at run time. That makes the interpreter a large, string-heavy state machine and a rich memory-detection surface.

### Call schedule

```
botMainTickLoop 0x100227bd                (timed, out of scope here)
  └─ runScriptTickProfiler 0x1002bc68      SEH/watchdog frame + arrow-key sampling
       └─ callSub1002b3d7 0x1002b09e       the real per-tick driver (misnamed by the tag)
            ├─ registerCommands_table 0x10030442   lazy dict build + verb dispatch
            │    └─ registerCommand 0x1002c1b6      perfect-hash insert (×~400)
            ├─ evalScriptExpression 0x1002c228      [..] / $var.field evaluator
            │    ├─ parseExpressionOrRange 0x100300ce
            │    │    ├─ parseSignedInt_0 0x10040900
            │    │    ├─ expandQuotedAndVariables 0x10030225
            │    │    └─ randRange 0x10040a30
            │    └─ (recurses into itself and the parsers)
            └─ randRange 0x10040a30                 firing-interval jitter
```

### `runScriptTickProfiler (0x1002bc68)` — watchdog + input sampling wrapper

This is a thin per-tick prologue, not the interpreter proper. Its job is threefold.

**1. Publish a profiling / watchdog context.** Before each phase it writes a block of globals that an external watchdog thread reads to know where the script thread is and how long it has been there:

| Global | Meaning |
|---|---|
| `dword_1005DBBC` | phase id (1, 2, 4, 5 here; 501/502/551/552 in the driver) |
| `dword_1005DBC0` | resume `loc_` address for this phase |
| `dword_1005DBC4` | pointer to the local SEH record `v6` |
| `dword_1005DBC8` | saved stack anchor (`&savedregs`) |
| `dword_1005DBD4` | `GetTickCount()` timestamp of phase entry |
| `dword_1005DBCC` / `dword_1005DBD0` | current command-table base / current script cursor |

`v6[1] = hotkeyProcExceptionHandler` and `v6[0] = TEB->NtTib.ExceptionList` install a per-frame SEH handler: a faulting script command is caught and the phase's `dword_1005DBC0` resume address is used to skip it rather than crash Tibia.

**2. Honour the abort flag.** At every phase boundary:

```c
if ( dword_102E2614 ) { dword_102E2614 = 0; ExitThread(1u); }
```

`g_102E2614` is a "kill this script thread now" latch set from elsewhere (config reload / bot stop). The engine polls it ~6× per tick.

**3. Sample the arrow keys into a direction opcode.**

```c
if (GetAsyncKeyState(VK_UP))    dword_100EE8D8 = 101;   // 38
if (GetAsyncKeyState(VK_RIGHT)) dword_100EE8D8 = 102;   // 39
if (GetAsyncKeyState(VK_DOWN))  dword_100EE8D8 = 103;   // 40
if (GetAsyncKeyState(VK_LEFT))  dword_100EE8D8 = 104;   // 37
```

`g_100EE8D8` is a pending-walk-direction opcode consumed downstream (manual-walk / step commands). `v5 = (dword_10291CDA != 0)` snapshots an "engine armed" flag and is passed as the sole argument (`a1`) to the driver. Then `return callSub1002b3d7(v5)`.

### `callSub1002b3d7 (0x1002b09e)` — the per-tick driver

The tag name is a misnomer; this **is** the hotkey/label execution loop. `a1` (renamed `v55`) is the armed flag. It resets `g_1005DBD0`/`g_1005DBCC` (cursor/table), clears `g_100F9341`/`g_100F934D`, snapshots `v50 = GetTickCount()`, and then iterates a single index `i` across four stitched table ranges:

| `i` range | Count | Entry stride | Base table | Meaning |
|---|---|---|---|---|
| `0x00–0x5F` | 96 | 514 B | `byte_100FAA3C` | ordinary key hotkeys (VK sampled per entry) |
| `0x60–0x1DF` | 384 | 514 B | `unk_1009A536 - 0x1C1C0` | extended/function-key hotkeys, `0xFF` label marker |
| `0x1E0–0x25F` | 128 | 4308 B | `unk_1014F420` | cavebot/targeting labels, block A |
| `0x260–0x2DF` | 128 | 4308 B | `unk_1014F420 + 2076` off | labels, block B |

Range enablement is gated by flag bytes: `byte_100F94C5`, `byte_100F0E42`, `byte_1013F32B`, `byte_101D5E26`, `byte_10135279` decide whether each block is scanned (the loop jumps `i` forward past disabled blocks). Each 514/4308-byte entry begins with an activation descriptor:

- byte[0] = virtual-key code (for GetAsyncKeyState hotkeys),
- byte[1] = presence/`0xFF`-label flag,
- byte[2..] = the script text.

**Per-entry firing logic.** For key hotkeys the driver debounces GetAsyncKeyState against a per-index last-poll timestamp:

```c
v11 = v50 - dword_1008AA0B[i];          // ms since last poll
if (v11 < 0x64) { ... use cached state ... }        // <100ms: reuse
else {
  if (v11 >= 0x96) dword_1008AA0B[i] = v50;          // >=150ms: resync
  else             dword_1008AA0B[i] += 100;
  v8 = GetAsyncKeyState(vk);
  if (dword_1005F87C == i && !v8) dword_1005F878 = 0;
}
```

Cooldowns and randomised intervals live in a bank of parallel `dword_*[i]` arrays (see globals). Where a label defines a `min..max` delay, the next interval is drawn with `v17 + randRange(v16 - v17 + 1)` (jittered so consecutive fires are not on a fixed period — an intentional anti-detection choice, mirrored in `parseExpressionOrRange`).

**Structural parsing of the action body.** Once an entry fires, its text (`v7`, after skipping the leading key/label token words) is `lstrcpy`'d into a local `v56` buffer and executed. First an inline `auto ` prefix is special-cased (`(v56 | 0x20202020) == 0x6F747561` i.e. `"auto"`, followed by space) to arm auto-repeat via `dword_1008910B[i]`. Otherwise the body is walked byte-by-byte tracking brace depth `v54`:

- `{` → `++v54` (nesting, e.g. conditional block),
- `}` → `--v54`; underflow (`== -1`) sets a re-entry flag,
- unescaped `|` at depth 0 (guarded against `||` and leading/trailing `|`) → statement separator,
- `\0` → final statement.

At each separator the accumulated segment is null-terminated and dispatched via `registerCommands_table(segment, dword_10084C07, 0)`, then the original delimiter byte is restored. `dword_10084C07` carries the current entry index so command handlers know which hotkey/label invoked them. The 0x200 (512) iteration cap bounds pathological scripts. The label block (0x60–0x2DF second loop over `byte_10106B02`, stride 546) repeats the identical brace/pipe splitter with phase ids 551/552 — this is the cavebot/targeting label executor and is where `gotolabel` etc. take effect.

### `registerCommands_table (0x10030442)` — dictionary build + dispatch

Guarded by `byte_10292302`: on first call it registers the entire CiroScript vocabulary, one `registerCommand(table, name, handler)` per verb, into three tables, then flips the guard so the ~400 inserts happen once. The observed names (`aGotolabel_0`→`cmd_gotolabel`, `aIslocation_0`→`cmd_islocation`, `aIsdistance`→`cmd_isdistance`, `aIsnotdistance`, `aIsnotlocation`, …) show the `g_10292304` table holds **conditional predicates** (the `is*`/`isnot*` guards and `gotolabel` control flow) used by cavebot label logic. After the guard, the incoming statement's verb is hashed the same way `registerCommand` hashes and the handler slot is fetched and called. This is a classic split: `g_10292304` = flow/condition commands, `g_102B2404` = variable/`$`-accessors, `g_102D2504` = `[`-expression functions (populated from `evalScriptExpression`).

### `registerCommand (0x1002c1b6)` — perfect-hash insert

```c
toLowerCharInPlace(name);                 // case-fold verb
result = 0;
do { c = *p++; result = c + 5*result; } while (c);   // hash: h = 5h + c
if (table == &g_10292304) result &= 0x3FFF;   // 16384 slots
if (table == &g_102B2404) result &= 0x3FFF;   // 16384 slots
if (table == &g_102D2504) result &= 0x1FFF;   //  8192 slots
if (table[2*result]) return MessageBoxA(0, name, table[2*result], 0);  // collision → popup
table[2*result]   = name;                 // slot = {name, handler} pairs
table[2*result+1] = handler;
```

The hash is the polynomial `h = 5*h + c` over the lowercased name, masked to the table size. Slots are 8 bytes (`name`,`handler`). Because the vocabulary is fixed and hand-tuned, it is effectively a **perfect hash** — a genuine collision at build time throws a `MessageBoxA` showing the two colliding names (a dev-time assertion left in the binary). At dispatch time the same hash indexes straight to the handler with no probing.

### `evalScriptExpression (0x1002c228)` — the `[..]` / `$var.field` evaluator

Entered with the first char in `a1` (`$` = 0x24 or `[` = 0x5B), the source pointer in `a2`, and an output buffer in `a3`. It is a recursive-descent evaluator with full operator support: `* / %`, `+ -`, comparisons `== >= <= != < >`, logical `&&`, the script comment/separator `//`, and the ternary `?`, with quote and parenthesis handling. `$name.field` performs a variable/object lookup (message, channel and creature objects are resolved with `lstrcmp`/`lstrcmpi` and formatted back with `wsprintfA`). It shares the `registerCommand` machinery to populate ~200 accessor entries into `g_102B2404`/`g_102D2504`, so `[hp]`, `[$self.x]`, etc. resolve to handler calls. Numeric leaves are delegated to `parseExpressionOrRange`. Results are written as ASCII into `a3` (later re-parsed by `parseSignedInt_0`), so the evaluator is string-in/string-out and reentrant via the same brace/segment splitter as the driver.

### `parseExpressionOrRange (0x100300ce)` — numeric leaf + range parser

Skips leading spaces, then dispatches on the first significant char:

- `\0` → `0`.
- `$` (36) or `[` (91) → call `evalScriptExpression` into a 2000-byte local, then `parseSignedInt_0`.
- `'` / `"` → `expandQuotedAndVariables`, then `parseSignedInt_0`.
- otherwise copy a bare token; if it contains the literal `..` (`*(WORD*)a1 == 11822`, i.e. two `.` bytes `0x2E2E`) treat it as a range `lo..hi`: parse both sides and return a **uniform random draw**:

```c
if (v9 >= v8) return v8 + randRange(v9 - v8 + 1);   // [v8,v9]
else          return v9 + randRange(v8 - v9 + 1);   // [v9,v8]
```

That `a..b` random-range primitive is what powers `delay 800..1200`-style jitter throughout scripts.

### `parseSignedInt_0 (0x10040900)` — ASCII → int

A custom `atoi`. A **leading byte value `2`** (not the character `'2'`) flags a negative number (`v2 = -1`), then digits accumulate `v1 = 10*v1 + (c-'0')` and the result is returned as `v2 ^ (v1 + v2)` — branchless two's-complement negation when `v2 == -1`. The mirror is `intToAsciiDecimal (0x10040940)` which writes an int (with `-` sign) as a reversed-then-swapped decimal string; both are the interpreter's number↔string boundary.

### `expandQuotedAndVariables (0x10030225)` — token unescaper

Recursively expands one token into `a2`: toggles quote state on `'`/`"`, treats `$$`→literal `$` and `[[`→literal `[`, and recurses on a lone `$`/`[` (calling `evalScriptExpression`), advancing the output to the new terminator each time. Unquoted runs of spaces are collapsed unless a real token has been emitted (`v7` flag). This is what lets a script embed `$var` inside a quoted string and get the interpolated value.

### `randRange (0x10040a30)` — Park-Miller LCG

```c
v1 = seed + (seed < 0 ? 0x7FFFFFFF : 0);
seed = 16807*(v1 % 127773) - 2836*(v1 / 127773);   // g_1005A280
return seed % a1;
```

The MINSTD minimal-standard generator (multiplier 16807, modulus 2^31-1 via the 127773/2836 Schrage split), seeded/updated in `g_1005A280`. Every random delay, `a..b` range and firing-interval jitter in the bot comes from this one global — a single deterministic stream keyed on `g_1005A280`.

### Data-structure summary

The action tables are flat arrays of fixed-stride records indexed by the global `i` in `callSub1002b3d7`. Parallel state arrays (all `dword_*[i]`) hold per-entry timers:

| Array base | Role |
|---|---|
| `dword_10084C0B[i]` | active delay/interval for entry i |
| `dword_10087A0B[i]` | remaining auto-repeat / hold countdown |
| `dword_1008858B[i]` | saved script cursor for a suspended `{}` block |
| `dword_1008910B[i]` / `dword_10089C8B[i]` | auto-repeat sequence counters (wrap at 0x7D0=2000) |
| `dword_10086E8B[i]` | accumulated elapsed time toward next fire |
| `dword_1008578B[i]` / `dword_1008630B[i]` | random-interval min / max bounds |
| `dword_1008AA0B[i]` | last GetAsyncKeyState poll timestamp |
| `dword_10084BFF` | this tick's Δt (ms since last tick) |
| `dword_100F49D5` | current auto-repeat generation id |
| `byte_100BA736[276*i]` | per-entry "condition satisfied" result byte written back for the GUI |
| `byte_1008A90B[i]` | targeting hysteresis counter (decremented when `dword_1005F63B` set) |

The verb is the executable code; the tables above are the schedule/state. Anything scanning `elfbot.dll`'s data section for these arrays, or for the `g_1005DBBC..D4` watchdog block being written every tick, has a reliable liveness signal.

## Key globals

| Address | Meaning |
|---|---|
| `0x1005DBBC` | Watchdog phase id written every phase (1/2/4/5 in the profiler, 501/502/551/552 in the driver); external watchdog reads it to know where the script thread is. |
| `0x1005DBC0` | Per-phase SEH resume address (loc_) used to skip a faulting command instead of crashing Tibia. |
| `0x1005DBC4` | Pointer to the on-stack SEH record for the current phase frame. |
| `0x1005DBC8` | Saved stack anchor (&savedregs) for the current phase. |
| `0x1005DBCC` | Current command-table / statement base pointer being executed (liveness signal). |
| `0x1005DBD0` | Current script text cursor of the statement in flight. |
| `0x1005DBD4` | GetTickCount timestamp of phase entry; watchdog uses it to detect a hung script thread. |
| `0x102E2614` | Abort latch: when set, the engine zeroes it and calls ExitThread(1) to tear down the script thread; polled ~6x per tick. |
| `0x100EE8D8` | Pending manual-walk direction opcode set from arrow keys (101=up,102=right,103=down,104=left). |
| `0x10291CDA` | Engine-armed flag snapshotted into the driver's a1 argument (gates whether held-key hotkeys execute). |
| `0x10292304` | Command hash table #1 (16384 slots, {name,handler} pairs): control-flow and condition verbs (gotolabel, is*/isnot*). |
| `0x102B2404` | Command hash table #2 (16384 slots): $-variable / accessor handlers registered by evalScriptExpression. |
| `0x102D2504` | Command hash table #3 (8192 slots): [-expression function handlers. |
| `0x10292302` | One-shot guard byte: 0 until the command dictionaries are built, then set so the ~400 registrations run once. |
| `0x1005A280` | Park-Miller LCG seed — the single RNG state feeding every randRange draw (delays, a..b ranges, firing jitter). |
| `0x100FAA3C` | Base of the 96 ordinary-key hotkey records (stride 514: [vk][flags][script text...]). |
| `0x1009A536` | Base region for extended/function-key hotkey records (indices 0x60-0x1DF, stride 514; 0xFF byte marks a label entry). |
| `0x1014F420` | Base of the 256 cavebot/targeting label records (stride 4308), split into blocks A and B. |
| `0x10106B02` | Second label-record table walked by the driver's targeting loop (stride 546). |
| `0x10084C0B` | Per-entry active delay/interval array (indexed by hotkey/label index i). |
| `0x10087A0B` | Per-entry remaining auto-repeat / key-hold countdown array. |
| `0x1008858B` | Per-entry saved script cursor for a suspended {} conditional block. |
| `0x1008910B` | Per-entry auto-repeat sequence counter (wraps at 0x7D0=2000), paired with dword_10089C8B. |
| `0x10086E8B` | Per-entry accumulated elapsed time toward the next fire. |
| `0x1008578B` | Per-entry random-interval minimum bound. |
| `0x1008630B` | Per-entry random-interval maximum bound (used with randRange for jittered firing). |
| `0x1008AA0B` | Per-entry last GetAsyncKeyState poll timestamp (100/150ms debounce window). |
| `0x10084BFF` | This tick's delta-time in ms (elapsed since previous tick), subtracted from all countdown timers. |
| `0x100F49D5` | Current auto-repeat generation id, stamped into per-entry sequence counters. |
| `0x10084C07` | Currently-executing hotkey/label index, passed to every dispatched command handler so it knows its caller. |
| `0x100BA736` | Per-entry condition-result byte array (stride 276) written back for the GUI to show which hotkeys/labels are satisfied. |
| `0x1008A90B` | Per-target hysteresis counter, decremented when dword_1005F63B is set (targeting stickiness). |
| `0x100EE8B6` | Per-entry busy/executed flag for the current tick (1 = active), gates the write-back to byte_100BA736. |
| `0x1005F878` | Held-key latch cleared when the tracked key (dword_1005F87C) is released. |

## Detection notes

- Watchdog write signature: g_1005DBBC..g_1005DBD4 (0x1005DBBC-0x1005DBD4) is a 6-DWORD block rewritten every phase every tick with a phase id, a resume loc_ address inside elfbot.dll's .text, an SEH record pointer, a stack anchor and a fresh GetTickCount. A memory scanner that samples this region twice sees the timestamp and phase id churn on a fixed cadence — a strong bot-alive signal even without touching Tibia's own memory.
- SEH callback pointer: g_1005DBC4 points at an on-stack EXCEPTION_REGISTRATION whose handler is hotkeyProcExceptionHandler inside elfbot.dll; the fs:[0] chain therefore contains a frame pointing into an injected module. Walking the current thread's SEH chain and checking whether any handler lands outside the main image is a clean detection.
- Arrow-key polling: GetAsyncKeyState(37..40) is called four times per tick from injected code (0x1002bd7c-0x1002bdce). A hook/telemetry on GetAsyncKeyState seeing a caller return address inside elfbot.dll, or seeing all four arrow VKs polled in a tight burst every ~50ms, fingerprints the manual-walk sampler.
- Bulk GetAsyncKeyState debounce: the driver polls GetAsyncKeyState for every enabled hotkey VK with a 100/150ms resync window (g_1008AA0B[i]). The characteristic pattern is dozens of distinct VK codes queried in one call burst on a fixed 100ms grid — human input never produces that.
- ExitThread abort behaviour: g_102E2614 (0x102E2614) is polled and, when set, triggers ExitThread(1) from injected code. A thread whose start address is inside elfbot.dll and which self-terminates via ExitThread on a flag flip is anomalous for a legit Tibia thread.
- Deterministic RNG stream: g_1005A280 (0x1005A280) is a single Park-Miller MINSTD seed advanced by exactly seed = 16807*(v%127773) - 2836*(v/127773) on every delay/range draw. The 16807/127773/2836 constants are a byte-pattern signature in .text (0x10040a30), and the resulting inter-action timing is a reproducible LCG sequence — behavioural timing analysis can flag the too-regular MINSTD distribution of action intervals.
- Command dictionary in memory: three fixed-size hash tables at g_10292304 / g_102B2404 / g_102D2504 (16384/16384/8192 slots of {name,handler}) are populated once (guard byte_10292302) with plaintext lowercase verb strings like gotolabel, islocation, isdistance, isnotlocation. Scanning elfbot.dll's data for this dense array of known CiroScript verb strings, or the h=5h+c hash constant, is a direct static+runtime fingerprint.
- Dev assertion left in build: registerCommand (0x1002c1b6) calls MessageBoxA(0, name, existing, 0) on a hash collision — an unexpected MessageBoxA from an injected module is a loud, catchable artefact.
- Flat action-table arrays: the parallel per-entry timer banks (g_10084C0B, g_10087A0B, g_1008858B, g_10086E8B, g_1008578B, g_1008630B, g_1008AA0B, all based near 0x10084C00-0x1008AA0B) plus the 4308-byte label records at g_1014F420 form a recognisable contiguous data layout in elfbot.dll; their addresses are stable for this build and can be signatured directly.
- auto-prefix opcode: statements are pattern-matched against (dword | 0x20202020)==0x6F747561 (ASCII "auto") to arm auto-repeat. That exact 32-bit compare against 0x6F747561 in .text (0x1002b44d and 0x1002b97b) is a byte-pattern signature for the CiroScript executor.
