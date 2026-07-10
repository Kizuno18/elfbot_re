# GAP resolutions — 4 behavior-parity questions

Resolved from the offline angr decompile (`docs/functions/decompiled/jdrv.jsonl`),
no live IDB needed. These refine the `g_100f0e20` bridge (docs/25), the `auto`/
`dontlist` model (docs/14, 24) and the deposit state machine (docs/23).

## GAP-2 — `g_100f0e20` is a creature pointer, not a flag

The arbiter `cavebotTargetingStep` @ `0x1003D99F` never writes the non-zero value.
Its only store is the **clear** when targeting is disarmed:

```c
if (g_100f0d3b || g_100f0d3c)
    sub_10012edb(...);   // targeting scan/engage — sets the bridge
else
    g_100f0e20 = 0;      // disarmed -> clear
```

The non-zero write lives in the targeting scan **`sub_10012edb` @ `0x10012edb`**:

```c
// on-screen creature within 2 tiles of the player (g_1005F854 = X, g_1005F858 = Y)
if (v47[36] - g_1005F854 + 1 <= 2 && v47[40] - g_1005F858 + 1 <= 2)
    g_100f0e20 = v47;          // v47 = creature struct pointer
...
g_100f0dc0 = idx1;             // current-target pointer
g_100f0e20 = idx1;             // bridge = same pointer
```

So **`g_100f0e20` holds the pointer to the currently-engaged creature** (the same
value as the current-target pointer `g_100f0dc0`), or `0` when none. It is not a
boolean `1`. `istargeting` / `isnottargeting` test it truthy = "current target
pointer is non-null".

## GAP-6 — `auto N`

Handler path in `processHotkeyScriptEngine` @ `0x1002b09e`. Detection at both
sites (`0x1002b44d`, `0x1002b97b`):

```c
if ((dword[cmd+4] | 0x20202020) == 0x6F747561 && cmd[0] == ' ')  // "auto "
```

On match:
- mark the entry auto/repeating (`byte[entry+2017] = 1`);
- **generation-stamp** the entry: `g_1008910B[i] = g_100F49D5` (current generation
  id);
- token-skip `auto` + whitespace + the `N` token (three scan loops), then dispatch
  **the remainder of the line** (the command after `N`) via `sub_10030442` (the
  CiroScript statement executor).

The per-entry countdown `g_10087A0B[i]` is only **decremented** here
(`-= g_10084BFF`, the tick's ms-delta) and re-armed via the generation id; counters
wrap at `2000`. `N` is the **repeat interval in milliseconds** (documented ElfBot
behaviour), realised as the reload value of that countdown — but the exact
`N → g_10087A0B` reload store is **not isolated in this function's decompile** (`N`
is consumed as a token here; the numeric wiring runs through `sub_10030442` / the
delay path). Confirm the reload store against raw disassembly if byte-exact timing
matters. This is a single global schedule (the driver sweeps entry index `i`), not
a per-module registry.

## GAP-7 — `dontlist`

`sub_100328af` is tiny:

```c
void sub_100328af(void) {
    if (entryIndex != 0xFFFFFFFF)
        g_100EE8B6 = 2;   // per-entry byte_100EE8B6[i] = 2
}
```

`byte_100EE8B6[i]` is the per-entry gate for the HUD running-scripts write-back
(it gates `byte_100BA736[i]`, the condition-result byte the GUI reads). Writing
**`2`** marks the entry **suppressed** — so `dontlist` on a hotkey/label keeps it
executing but **hides it from the HUD "running scripts" list**.

## GAP-11 — deposit state machine

`depositLootStateMachine` @ `0x10036EB6`, state var `g_102E2604`, depot id `3147`,
open-container id read from `[0x64CCD4]`, next-container from `[0x64CD04]`.

**The state set is `{0, 2, 3, 5, 7}` — states 1, 4, 6 do not exist.** The machine
steps `0 → 2 → 3 → 5 → 7 → 0`:

| State | Action / transition |
|---|---|
| 0 | `[0x64CCD4]==0` → **2**; `==3147` → **3**; else (container open, `[0x64CD04]==0`) → `sub_10036e69` (open) |
| 2 | `[0x64CCD4]==3147` → **3**; else find depot item `sub_1002ae92(3147,…)`, build a `0x11` record (`g_10043388` block) via `sub_1002ade7` |
| 3 | `[0x64CCD4]==3147` → `sub_10039413` (deposit); `==0` → **2**; else → **5** |
| 5 | `[0x64CCD4]==0` → **7**; `!=3147` → build `0x11` record (`g_10043454` block) via `sub_1002ade7` |
| 7 | `[0x64CD04]!=0` → `sub_10036e69` (open next); else → **0**, done |

**Threshold gate (GAP-11b):** the whole block is gated by
`g_1005F7D5 >= <arg>` where the right-hand side is a **caller-supplied register
argument (ebx), not a hardcoded literal** — so there is no numeric constant in this
function; the threshold is whatever the deposit-tick caller passes.

**Loop:** after each step, it re-evaluates while the walker flag `g_100F0E42` is
set (`Sleep(350)` between polls, resets `g_100F0E18 = 0`); returns otherwise.
