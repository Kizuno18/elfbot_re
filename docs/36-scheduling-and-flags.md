# Per-entry scheduler & subsystem-state flags (gap closure)

Closes the byte-exact micro-gaps left open in [docs/31](31-gap-resolutions.md): the
`auto N` reload store (GAP-6, noted there as "not isolated in the decompile") and the
literal armed values of the three subsystem-state globals the runtime bridges use.
All resolved from raw disassembly of `samples/elfbot.dll` (imagebase `0x10000000`)
with a local capstone pass — no live IDB required, so it stands independent of the
runtime lab.

## The per-entry hotkey scheduler — `auto` vs `wait`

`processHotkeyScriptEngine` (`0x1002b09e`) sweeps a flat bank of parallel arrays
indexed by the hotkey/action entry `i`. Two CiroScript commands arm the timers, and
they write **different** arrays — which corrects the docs/31 guess that `N` reloaded
into `g_10087A0B`. `auto`'s interval actually lands in `g_10084C0B`; `g_10087A0B` is
the separate `wait`/hold cooldown.

| Array | Elem | Meaning | Written by |
|---|---|---|---|
| `g_10084C0B[i]` | dword | auto-repeat interval `N` (0 = auto off) | `auto` `0x10032433` @ `0x10032470` |
| `g_10086E8B[i]` | dword | auto elapsed accumulator (advances by tick delta, wraps at `N`) | `auto` @ `0x10032477`; engine |
| `g_10087A0B[i]` | dword | `wait` cooldown / key-hold countdown (`0xFFFFFFFF` = held) | `wait` `0x10030878` @ `0x100308b4`; `end` `0x10032529` |
| `g_1008578B[i]` / `g_1008630B[i]` | dword | aim-auto min/max square params | `auto` |
| `g_1008910B[i]` | dword | generation stamp (`= g_100F49D5`) | engine / auto path |
| `g_1008AA0B[i]` | dword | last-fire timestamp (100 ms rate gate) | engine |
| `g_10084BFF` | dword | current tick ms-delta (the decrement step) | engine |

### `auto N` — `0x10032433` (command `auto`)

Toggle. `N = sub_100300ce()` (the token→integer/variable evaluator). With entry index
`i` (arg `[ebp+0xc]`, `-1` → no-op):

- if `g_10084C0B[i]` already set → **Auto Off**: zero `g_10084C0B/g_1008578B/g_1008630B/g_1008858B/g_10087A0B[i]`, chat `"Auto Off: <cmd>"`.
- else **Auto On**: `g_1008578B[i]=esi`, `g_1008630B[i]=edi` (min/max square), `iter=N` (clamped to ≥1 if a square param is set), then

  ```
  0x10032470  89 04 9d 0b 4c 08 10   mov [ebx*4 + 0x10084C0B], eax   ; interval = N
  0x10032477  89 04 9d 8b 6e 08 10   mov [ebx*4 + 0x10086E8B], eax   ; accumulator = N
  ```

  clear `g_1008858B/g_10087A0B[i]`, chat `"Auto On: <cmd>"`.

### `wait N` — `0x10030878` (command `wait`)

`N = sub_100300ce()`. With entry index `i` (`[ebp+0xc]`):

- `i != -1` → the entry cooldown:

  ```
  0x100308b4  89 04 9d 0b 7a 08 10   mov [ebx*4 + 0x10087A0B], eax   ; cooldown = N
  ```

  suppresses that entry's re-fire for `N` ms; the engine decrements it by `g_10084BFF`
  each pass and, while non-zero, it overrides the auto fire.
- `i == -1` (standalone in a script) → a blocking sleep:
  `for (t = 0; t < N; t += 100) { if (!g_100F0E42) return; Sleep(100); g_100F0E18 = 0; }`
  — chunked 100 ms `Sleep`s that bail the moment the Cavebot/script engine flag clears.

### `end` — `0x10032529` (command `end`)

`g_10087A0B[i] = 0xFFFFFFFF` (marks the entry "held"; the engine consumes `0xFFFFFFFF`
on the next tick by resetting it to 0) and raises the `g_1008AB93`/`g_1008AB97`
completion flags.

**Engine consumption** (`processHotkeyScriptEngine`): each pass, if `g_10084C0B[i]`
(auto on) it advances `g_10086E8B[i]` by `g_10084BFF` and fires + re-arms when the
accumulator reaches `N`; a non-zero `g_10087A0B[i]` (wait) is decremented first and
gates the fire; the 100 ms `g_1008AA0B[i]` timestamp gate throttles held-key autos.
One global schedule swept by entry index — not a per-module registry.

## Subsystem-state flag literals

Three globals bridge the tabs to the engine (the docs/25 triad, docs/31 bridges).
Their exact armed values, from the store sites:

| Global | Meaning | Armed value | Store site |
|---|---|---|---|
| `g_100F0D3B` | **Targeting** master-enable | `1` on / `0` off / toggle | `settargeting` `0x10035786` @ `0x10035797`: `c6 05 3b 0d 0f 10 01` (`mov byte [0x100F0D3B], 1`) |
| `g_100F0E42` | **Cavebot / script** engine-active | `1` on / `0` off / toggle | `setcavebot` `0x10035812` → `sub_100163d8` @ `0x10016408`: `a2 42 0e 0f 10` (`mov [0x100F0E42], al`) |
| `g_100F0E20` | current **target creature** pointer | live creature-struct pointer (heap addr; `0` = none) | set by the targeting scan `sub_10012edb` (`0x10012edb`); cleared by the arbiter `cavebotTargetingStep` `0x1003D99F` (docs/31) |

`settargeting` and `setcavebot` share one on/off/toggle shape: compare the arg to
`"on"`/`"off"`/`"toggle"`, set the flag, mirror it to the tab checkbox
(`BM_SETCHECK`, `wParam` from the resolved state) — targeting → ctrl `1046` in HWND
`g_10072F8C`, cavebot → ctrl `1012` in HWND `g_10072F94`.

- `g_100F0D3B` also stamps `g_100F0DE0 = GetTickCount()` at enable.
- `g_100F0E42` also clears `g_100F0E45`/`g_100F0DF8`, subclasses the `0x400`-byte
  waypoint mirror `g_100F45C5` (`sub_1002ae81`), sets `g_100F0E00` = selected
  waypoint + 1, and stamps `g_100F0E04 = GetTickCount()` at start. Beyond enabling the
  walker it is the **global abort gate** read by `wait` (`0x10030878`) and the hotkey
  engine — i.e. "is the bot still running".
- `g_100F0E20` is a pointer, not a literal: the scan writes the chosen creature's
  struct address and the attack path dereferences it; the arbiter only ever nulls it.
