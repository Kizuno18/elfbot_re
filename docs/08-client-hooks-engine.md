# elfbot.dll — client hook engine & packet proxy

The bot integrates with Tibia 8.60 by **inline-patching the client's code** and
maintaining shadow tables from intercepted network packets. Because
`elfbot.dll` is mapped into `Tibia.exe`, "hooks" are `WriteProcessMemory` writes
into the current process at **hard-coded 8.60 addresses** (this build targets one
exact client). This is the lowest layer everything else builds on.

## Hook installer — `installClientHooks_proxyServer` `0x10002041`

Runs once (guarded by `byte_1005A290`). Installs three hooks then runs an
embedded TCP server:

| Client address | Patch | Bot handler | Purpose |
|---|---|---|---|
| `0x5AB5D4` | pointer overwrite (saves orig → `dword_1005D88F`) | `hook_captureRenderCtx` `0x10001A96` | capture a render/context pointer each frame |
| `0x4F30C0` | `E9` JMP detour (saves orig target) | (paired with above) | detour into the client draw path |
| `0x45ACD6` | `E9` JMP detour (saves orig → `dword_1005D897`) | `hook_incomingPacketParser` `0x10001CA8` | intercept incoming packet dispatch |

`VirtualProtect(0x5AB000, 0x604, PAGE_READWRITE)` makes the region writable
first. After hooks, it creates a socket, `bind`s to `hostshort`, `listen`s and
`accept`s in a loop, spawning `sub_10002235` per connection — the **local proxy
/ NavNet control server** embedded in the bot.

## Incoming packet hook — `hook_incomingPacketParser` `0x10001CA8`

The bot's network awareness. It calls the original parser
(`dword_1005D897`), then reads the client's receive buffer at
`MEMORY[0x785D84] + MEMORY[0x785D8C]` and switches on the packet opcode to
maintain shadow tables:

- **Creature/battle table** `unk_1005A2A3` — 150 records × 40 bytes:
  - `0x0A` reset the whole table
  - `0xD2` add a creature (`memcpy` via `sub_1002AE6F`)
  - `0xD3` / `0xD4` set / clear a per-creature flag
  - `0xDD` remove a creature
- **Message/channel tables** `unk_1005CF17`, `unk_1005C9B3` — 20 records × 69
  bytes: `0xAC` / `0xB2` insert (channel open / message class), keyed by a word
  id, copied with `sub_1002AE6F`.

After updating tables, when the packet is a full network message
(`MEMORY[0x785D8C] == 9`, length `= *(u16)(buf) + 2`) it **forwards the raw
packet** to every active proxy client in `dword_1005DA85[16]` (states in
`unk_1005DAC5[16]`): state `2` triggers a handshake (`sub_10001C38` +
`sub_10001960` → `send`), state `1` streams packets. This is the packet-proxy
that feeds external tools / NavNet peers a live copy of the game stream.

## Context trampoline — `hook_captureRenderCtx` `0x10001A96`

Saves the incoming context pointer to `dword_1005DB05` and tail-calls the saved
original (`dword_1005D88F`). Gives the rest of the bot a live pointer to the
client's per-frame render/state context.

## Full-light hack — `hook_fullLightDetour` `0x100029A4`

A mid-function detour (installed by `installLightHook` `0x10002BDD` at
`0x4F4869`, returning via `JUMPOUT 0x4F4878`; trampoline
`hook_fullLight_trampoline` `0x10002BD6`). It patches three 6-byte sites in the
client's light renderer — `0x4F46BA`, `0x4F47BF`, `0x4F4840` — swapping between
two code stubs (`unk_1004477B` vs `unk_10044787`) driven by the toggle
`dword_1004476B`, and computes an ambient-light override written to
`*(ctx + 10888)`. Reads the client light global at `MEMORY[0x64F600]`
(normally `7`). Net effect: **remove darkness / full-light** rendering, on/off.

## Hard-coded Tibia 8.60 addresses (this build)

| Address | Meaning |
|---|---|
| `0x785D84` / `0x785D8C` | incoming network buffer base / offset(len marker) |
| `0x45ACD6` | incoming packet dispatch (hooked) |
| `0x4F30C0`, `0x5AB5D4` | client draw/context path (hooked) |
| `0x4F46BA`, `0x4F47BF`, `0x4F4840`, `0x4F4869`, `0x4F4878` | light renderer patch sites |
| `0x64F600` | client light-level global |
| `0x636FE0` | client state (`== 30` gate for proxy handshake) |
| `0x5AB000` (+0x604) | code region unprotected for patching |

Because these are compile-time constants, this DLL is bound to Tibia 8.60
exactly. Version-portable features (via the `SetFunctionAddresses` script
command) sit on top of this fixed base for the data-structure offsets rather
than the code hooks.

## Bot-side shadow data structures

| Symbol | Layout | Contents |
|---|---|---|
| `unk_1005A2A3` | 150 × 40 B | battle-list creature mirror (id, flags, pos) |
| `unk_1005CF17`, `unk_1005C9B3` | 20 × 69 B | channel / message-class buffers |
| `dword_1005DA85[16]` | 16 × socket | proxy/NavNet client sockets |
| `unk_1005DAC5[16]` | 16 × dword | per-proxy-client state (0/1/2) |
| `dword_1005DB05` | ptr | captured render context |

## Related functions (follow-up)

`sub_10002235` (embedded server per-connection handler), `sub_10001C38` /
`sub_10001960` (proxy handshake / framing), `sub_1002AE6F` (memcpy helper),
`installClientHooks_proxyServer`'s callers. Documented in the networking /
proxy subsystem pass.
