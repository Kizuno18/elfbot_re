# Full E2E runtime — genuine 8.60 client + local Fir3element TFS + loader.exe

The definitive end-to-end runtime proof: the **stock injector `loader.exe`** maps the
whole ElfBot chain into a **genuine Cip Tibia 8.60 client** that is logged into a
**local TFS 0.4 8.60 (Fir3element) server**, the client hooks patch in byte-for-byte,
the engine boots, and elfbot's player-state shadow **equals the live in-world player**.
This extends [docs/33](33-runtime-ingame-validation.md) (which used an OT client + a
direct `LoadLibrary`) to the real client and the real injector, and it **resolves the
`loader.exe err=126`** left open in [docs/06](06-injection-chain.md).

## Stack

- **Server** — TFS 0.4 8.60, Fir3element `3777` datapack, SQLite
  (`theforgottenserver.s3db`), bound `7171` (login) / `7172` (game). Console:
  `Bound ports: 7171 7172` … `Forgotten server Online!`. Account `1` / password `1`;
  a God char `Godbot` (group 6) plus the default `Account Manager`.
- **Client** — a **genuine Cip `Tibia.exe` 8.60** (retrieved as `Tibia86.rar`), its
  two Cip RSA modulus occurrences swapped in place for the OTServ modulus (309-digit,
  same length), `Tibia.dat/spr/pic` beside it, `hosts` redirecting
  `login0{1..5}.tibia.com → 127.0.0.1`. It **connected, authenticated** (server
  MOTD *"Welcome to the Forgotten Server!"*), reached the character list, and entered
  the world (`[0x64A9C0] == 31`).

## `loader.exe` injects the whole chain — `err=126` resolved

Placing the four files **in one directory** (`C:\elf\`) —
`loader.exe` + `elfload.dll` + `elfbot.dll` + `USkin.dll` — and running `loader.exe`
against the live client **injected cleanly, no `err=126`**, and produced no failure
log. The client's 32-bit module list afterwards:

```
elfload.dll @ 0x10000000
USkin.dll   @ 0x06E60000
elfbot.dll  @ 0x07D60000    (relocated from its 0x10000000 imagebase)
```

This confirms the [docs/06](06-injection-chain.md) root-cause analysis: the historical
`err=126` was **candidate 1 — elfload's directory-relative load of `elfbot.dll` /
`USkin.dll`** (it resolves them from its own module directory via `GetModuleFileNameA`
+ append), *not* madCodeHook-on-Win10. Co-locate the DLLs and madCodeHook injects fine
on Windows 10. So `loader.exe` **works** on the modern lab once the three payload DLLs
sit next to it.

## Booting the engine (loader ran `EcInit`, hooks/tick still need the docs/33 kick)

`loader.exe` → `elfload` → `EcInit` initialised the bot **UI** (its `USkin`
"Choose a skin file to load" dialog rendered live inside the client), but — exactly as
[docs/33](33-runtime-ingame-validation.md) found — `EcInit` alone did **not** install
the client hooks or start the tick loop. Those were kicked with the docs/33 sequence,
here driven **cross-process** (frida cannot attach the 32-bit WOW64 client on this
lab, so the writes/threads were issued from a 64-bit helper via
`WriteProcessMemory` / `CreateRemoteThread`, rebased to the `0x07D60000` load base
`E(off) = 0x07D60000 + (off − 0x10000000)`):

1. `E(0x1005DB68) = 0xFFFFFFFF` (`hProcess` = current-process pseudo-handle)
2. `E(0x1005A290) = 0` (clear the once-guard)
3. `CreateRemoteThread(E(0x10002041))` — `installClientHooks_proxyServer`
4. `CreateRemoteThread(E(0x100227BD))` — `botMainTickLoop`

## Proof — hooks byte-for-byte + shadow == live player

**Client hooks** (client imagebase `0x400000`), read back after the boot — before the
kick they held the original bytes; after, they are the documented patches, redirected
to the **relocated** handlers:

| Site | Bytes after | Meaning |
|---|---|---|
| `0x45ACD6` | `ce 6f 90 07` | rel32 of the packet-parser hook branch into the elfbot module |
| `0x4F30C0` | `e9 …` | JMP detour installed (client draw path) |
| `0x5AB5D4` | `96 1a d6 07` | `= 0x07D61A96` = `hook_captureRenderCtx` (`0x10001A96`) rebased — exact |

**Engine reads the live game** — with `botMainTickLoop` running and the char **in the
world (`[0x64A9C0] == 31`)**, `snapshotPlayerStats` mirrors the live client into the
(rebased) shadow:

| Field | Client (`0x400000`) | elfbot shadow (rebased) | Match |
|---|---|---|---|
| HP | `[0x63FE94]` = 150 | `E(0x1005F7D1)` = 150 | ✅ |
| pos | `[0x64F600]` = 7 | `E(0x10052770)` = 7 | ✅ |
| pos | `[0x64F604]` = 50 | `E(0x1005276C)` = 50 | ✅ |

So the ElfBot engine is **live inside the genuine client on the local Fir3element
server, injected by the stock `loader.exe`, hooking byte-for-byte and mirroring the
real in-world player** — the complete injected-runtime E2E.

## Reproduced — independent second live run

The whole chain was reproduced on a fresh VM boot to confirm it is deterministic, not
a one-off. `Account Manager` was deleted from the `players` table so **`Godbot` (God,
group 6) is the only character** — the login is then unambiguous. `Godbot` was
relocated to a **Dragon Lord spawn at `149,574,2`** (its position stored `z,y,x` in
the client: `[0x64F600]=2 [0x64F604]=574 [0x64F608]=149`). Results, all consistent
with the first run:

- `loader.exe` mapped **`elfload.dll @ 0x10000000`, `USkin.dll @ 0x07D70000`,
  `elfbot.dll @ 0x082B0000`** — a *different* relocation base than the first run,
  which is exactly why every elfbot address must be rebased by the live module base
  (`E(off) = base + (off − 0x10000000)`).
- After the docs/33 boot kick, **`0x45ACD6` = `ce 6f e5 07`** — the packet-parser
  hook's rel32 into the relocated elfbot module (`0x45ACDB + 0x07E56FCE = 0x082B2CA8`),
  byte-for-byte as expected at this base.
- **Tick loop confirmed live**: the tick ms-delta `g_10084BFF` advanced between two
  samples (`15 → 16`) — `botMainTickLoop` is running and updating each pass.
- **Shadow == live player**: `Godbot` HP/mana `2000/2000` read equal in the client
  (`[0x63FE94]`/`[0x63FE78]`) and the rebased elfbot shadow (`E(0x1005F7D1)` /
  `E(0x1005F7D5)`), with `[0x64A9C0] == 31` (in-world).
- **Creatures present**: the on-screen Dragon Lord spawn shows in the client's
  creature list as `Dragon Lord` records at **stride 168** (`0x63FEFC`, `0x63FFA4`,
  `0x64004C`, `0x6400F4` …) — the scenario source the Targeting / Creature-Spy
  behavioural captures read from.
- **elfbot UI live in-client**: the `USkin` "Choose a skin file to load" dialog
  (`TBOTDLGV`) rendered inside the client, confirming `EcInit`'s dialog framework +
  USkin init are running.

## Lab method note (winctl unavailable)

The desktop-control MCP was down for this run and frida's 32-bit attach was unusable,
so the whole session was driven through a frida session attached to **`explorer.exe`
(session 1)** as a shell: `CreateProcessW` to launch the setup/TFS/client and run
PowerShell, `CreateFileW`/`ReadFile` for file read-back, `SendInput`/`mouse_event` +
`FindWindow` for the GUI login, `System.Drawing` screen grabs exfiltrated as base64
for vision, and `OpenProcess`/`ReadProcessMemory`/`WriteProcessMemory`/
`CreateRemoteThread` for the cross-process injection, boot, and verification of the
32-bit client.
