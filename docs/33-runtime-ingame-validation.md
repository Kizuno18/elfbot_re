# Runtime validation, in-game (local TFS 0.4 8.60)

Extends [docs/28](28-runtime-validation.md) (which was headless at the login
screen). Here the bot was injected into a **genuine Tibia 8.60 client logged into a
local TFS 0.4 server and standing in the game world**, and its client hooks were
confirmed installing live — byte-for-byte matching the static RE.

## Setup on the RE VM

- **Server:** TFS 0.4 8.60 (Fir3element `3777` datapack, `x64-windows` build) with
  the SQLite backend, `theforgottenserver.s3db`, config bound to `7171` (login) /
  `7172` (game). Running and listening on both ports.
- **Client:** genuine Cip `Tibia.exe` 8.60 copied to `Tibia_ot.exe` with the two
  Cip RSA modulus occurrences swapped for the OTServ modulus (same length, in
  place), and `hosts` redirecting `login0{1..5}.tibia.com → 127.0.0.1`. Account
  `1` / password `1`, a playable Knight char in the `players` table.
- **In-game confirmation:** the client held an **established TCP connection to
  `127.0.0.1:7172`** (the game world; `7171` is only login), and the in-game flag
  **`[0x64A9C0]` read `31`** (in-world) with a live player HP read. So the char was
  actually standing in the world, not at a menu.

## elfbot injected into the live in-game client

`elfbot.dll` was `LoadLibraryW`-injected into the in-game client process. It mapped
at its imagebase and the client **stayed healthy** (`[0x64A9C0]` remained `31`
throughout) — unlike the crash-prone headless login-screen state in docs/28.

```
elfbot.dll @ 0x10000000  size 0x47D000     (mapped, DllMain ran, worker spawned)
[0x64A9C0] == 31  before and after injection
```

Direct `LoadLibrary` runs `DllMain` (which spawns the worker thread) but does **not**
run the loader's `EcInit`, so the client hooks were installed the same way docs/28
proved: set `hProcess [0x1005DB68] = GetCurrentProcess()` (`0xFFFFFFFF`), clear the
once-guard `[0x1005A290]`, and run `installClientHooks_proxyServer 0x10002041` on a
thread.

## Client hooks installed live — byte-for-byte

After the install thread ran, the three patch sites read exactly the documented
values (imagebase `0x400000`):

| Site | After patch | Redirects to |
|---|---|---|
| `0x45ACD6` | `ce 6f ba 0f` | rel32 → `hook_incomingPacketParser` `0x10001CA8` (verified: `0x45ACD5 + 5 + 0x0FBA6FCE = 0x10001CA8`) |
| `0x4F30C0` | `e9 …` | JMP detour (client draw path) |
| `0x5AB5D4` | `96 1a 00 10` | `= 0x10001A96` `&hook_captureRenderCtx` |

This is the docs/08 / docs/20 hook table, address-for-address and byte-for-byte,
now running in a client that is **actually in the game world** rather than at the
login screen.

## Network path observed

Raw socket traffic was confirmed flowing while in-game by hooking `recv` in
`ws2_32.dll`: a steady stream of small (~14–22 byte) TFS keepalives plus larger
(300+ byte) game-world frames when the char acted. Tibia game frames on the wire
carry the documented `[len:2][adler32:4][XTEA…]` shape (encrypted until the client
decrypts).

## What is confirmed vs. still fine-grained

**Confirmed live, in-game:** server + patched client + in-world char; bot injection
into that live client without destabilising it; the full client-hook installation
(all three sites) byte-for-byte; and real bidirectional socket traffic.

## Update — the bot ENGINE running in-game

A second pass took it further: not just injecting + hooking, but **booting the bot
engine and confirming it reads the live game**.

### Reproducible full stack (session-1 scheduled tasks)

The whole recipe is now repeatable headlessly via tasks that run in the interactive
console session (`/ru kizudev /it /rl HIGHEST`): `RunTFS` (server), `LaunchTibiaOT`
(client), `LoginTibia` (drives the account `1`/`1` login), `WalkTibia` (movement).
The login/walk tasks use `AttachThreadInput` + `SetForegroundWindow` +
`WScript.Shell.SendKeys` — the recipe's foreground trick is required (a bare
`SetForegroundWindow` from a task, or `PostMessage`/`keybd_event`, does **not** drive
the client). Result: char logged into the world, established `127.0.0.1:7172`.

### Relocation gotcha — rebase every elfbot address

`LoadLibrary`-injecting `elfbot.dll` does **not** always land at its preferred
imagebase `0x10000000`. In one client it mapped at `0x10000000` (hard-coded
addresses worked); in a fresh client it **relocated to `0x080C0000`**, so every
`elfbot.dll` address (hook installer, tick loop, hProcess/guard globals, shadow
tables, the parser handler the client patch points at) had to be **rebased by the
actual `module.base`**:

```js
const B = Process.findModuleByName("elfbot.dll").base;   // e.g. 0x080C0000
const E = off => B.add(off - 0x10000000);                // rebase any elfbot addr
```

Client (`0x400000`) addresses need no rebase. The client hook patch then correctly
redirects to the *relocated* handler (e.g. `0x45ACD6` reads `ce 6f c6 07`, whose
rel32 targets the relocated `hook_incomingPacketParser`, not `0x10001CA8`).

### Booting the engine (loader.exe fails → CreateThread the tick loop)

The stock injector `loader.exe` fails here — `loader.log`: `FAIL err=126 (module
could not be found)` — so the normal `EcInit` → dialog → engine chain never runs.
A bare `LoadLibrary` only runs `DllMain` (whose worker `sub_10002D08` exits early
without the loader init). The engine thread `botMainTickLoop 0x100227BD` is created
(guarded) only from `cavebotTargetingStep 0x1003D99F`. So the engine was booted
directly: after installing the hooks, `CreateThread(E(0x100227BD))`.

### Proof: the engine reads the live game

With the tick loop running, the bot's **player-state shadow tables (rebased) equal
the live client values** — `snapshotPlayerStats` (tick id 30) is copying the running
game into the bot each tick:

| Field | Client (`0x400000` base) | elfbot shadow (rebased) | Match |
|---|---|---|---|
| HP | `[0x63FE94]` = 455 | `E(0x1005F7D1)` = 455 | ✅ |
| Mana | `[0x63FE78]` = 65 | `E(0x1005F7D5)` = 65 | ✅ |
| pos X | `[0x64F600]` = 7 | `E(0x10052770)` = 7 | ✅ |
| pos Y | `[0x64F604]` = 117 | `E(0x1005276C)` = 117 | ✅ |

This is the definitive in-game runtime proof: **the ElfBot engine is live in the
game world and mirroring the real player state**, exactly as [docs/13](13-engine-tick-loop.md)/[docs/21](21-player-state.md)
describe.

### Still open

- The **incoming-packet parser hook** (`0x45ACD6` → relocated handler) does not fire
  on movement/map-update packets even with the engine running — that site is a
  specific-opcode dispatch, not the main parse loop; the packet-fed **shadow
  creature/battle-list** table stayed empty because the temple spawn had no
  creatures on screen (`E(0x10077175)` all zero). Populating it needs creatures in
  view (walk to a spawn / summon), which is the next capture.
- Per-tab **behavioural** tests (healer casts, cavebot walks a route, targeting
  attacks) need the matching scenario set up in the TFS world; the engine and its
  player-state read are proven, tab-behaviour scenarios are the follow-up.
