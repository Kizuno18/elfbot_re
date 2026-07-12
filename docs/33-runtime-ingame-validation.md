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

**Not yet captured:** a decoded per-packet trace through the elfbot parser hook
(`0x10001CA8`) with opcodes. The hook is installed, but making it fire requires
sustained real game-world messages routed through the specific `0x45ACD6` dispatch
call; a lone char in an empty temple with headless input (no reliable interactive
desktop for `SendInput`-level movement — `PostMessage`/`keybd_event` do not drive
Tibia's DirectInput movement) produces little such traffic, and the shared RE VM's
client sessions are short-lived (the client set respawns/exits frequently). The hook
*installation* and the *wire traffic* are proven; the *decoded opcode stream* is the
remaining capture, to be taken during a stable session with genuine in-game
activity (walking past creatures / combat).
