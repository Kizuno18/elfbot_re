# navserv.exe — NavNet position-sharing server

`navserv.exe` (12 KB, console, `ws2_32`) is the standalone **NavNet server**: a
tiny TCP hub that shares party player positions, enemy sightings and a chat
channel ("navsay") between multiple ElfBot clients hunting together. It is fully
unpacked and small enough that every function is documented below.

- Arch: x86, subsystem console, imagebase `0x400000`
- Build: MSVC (linker 5.12), timestamp 2009-04-07
- 12 real functions + import thunks. No CRT startup (custom `start`).

## Configuration (`navserv.ini`, section `[navserv]`)

Loaded once at startup by `readIniKey`:

| Key | Global | Meaning |
|---|---|---|
| `password` | `String1` | server password (any player) |
| `leaderpassword` | `byte_404041` | leader password (grants leader rights) |
| `port` | `hostshort` | TCP listen port |
| `sendenemies` | `dword_404434` | broadcast enemy sightings (bool) |
| `sendonlyleaderpositions` | `dword_404430` | only relay leader positions (bool) |
| `onlyleaderscannavsay` | `dword_40442C` | restrict navsay chat to leaders (bool) |
| `updateinterval` | `dword_404438` | broadcast period in ms |

## In-memory state

Two flat, fixed-capacity tables in `.data`, scanned linearly by pointer stride:

**Player table** — records of **436 bytes** from `unk_404874` to `dword_41FC74`.

| Offset | Type | Field |
|---|---|---|
| +0 | dword | client socket (0 = empty slot) |
| +8 | char[64] | player name |
| +72 | char[64] | aka / real character name |
| +392 | dword | login id (`v134`) |
| +416 | dword | secondary id (`v133`) |
| +396..+416 | word[] | x (+400), y (+404), z (+408), dir (+396) |
| +412,+414 | word | extra coords (last known) |
| +420 | dword | last-position tick |
| +424 | dword | target creature id |
| +432 | byte | connection index (broadcast id) |

**Enemy table** — records of **84 bytes** from `dword_41FC74` to `dword_425074`.

| Offset | Type | Field |
|---|---|---|
| +0 | char[64] | enemy name (0 = empty) |
| +64 (idx16) | dword | x |
| +68 (idx17) | dword | y |
| +72 (idx18) | dword | z |
| +76 (idx19) | dword | last-seen tick |
| +80 (idx20) | dword | announced flag |

`dword_425074` is a global seconds counter, bumped every 1000 ms by the
broadcaster. Staleness thresholds: players/enemies expire from broadcasts after
`0x1E` (30) ticks; position deltas are sent while age `< 2` ticks.

## Wire protocol

One byte opcode + payload, little-endian, null-terminated strings.

**Client → server**
| Op | Payload | Handler action |
|---|---|---|
| 1 | id(4), realid(4), name\0, aka\0, password\0 | login: validate password, register slot, send welcome (8) + full state |
| 2 | x(2), y(2), z(1), dir(1), coords(2+2) | update own position |
| 3 | name\0, x(2), y(2), z(1) | report enemy sighting → `findOrAddEnemy` |
| 6 | creatureId(4) | set/clear own target creature |
| 7 | text\0 | navsay chat (gated by `onlyleaderscannavsay`) |

**Server → client**
| Op | Payload | Meaning |
|---|---|---|
| 1 | idx, name\0 | enemy added |
| 2 | idx, id(4), creatureId(4), name\0, aka\0 | player added |
| 3 | idx, x(2), y(2), z(1), dir(1), coords | player position |
| 4 | idx, x(2), y(2), z(1) | enemy position |
| 7 | idx, text\0 | navsay relayed |
| 8 | sendenemies, sendonlyleader, connIdx | welcome / feature flags |

## Functions

| Address | Name | Role |
|---|---|---|
| `0x401012` | `main_entry` | load config, print colored banner, spawn `serverListenThread`, block on stdin until Enter, `ExitProcess` |
| `0x40199F` | `readIniKey` | `GetPrivateProfileStringA([navserv], key)` from `navserv.ini` |
| `0x4019F1` | `serverListenThread` | `WSAStartup`; spawn `broadcastDeltaThread`; `socket`/`bind(port)`/`listen(5)`; `accept` loop → one `clientHandlerThread` per connection |
| `0x401BBD` | `broadcastDeltaThread` | every `updateinterval` ms build a delta packet (player joins op2 / positions op3, enemy joins op1 / positions op4) and `send` to every connected client; ticks the seconds counter |
| `0x401E1F` | `checkPassword` | true if string equals server or leader password |
| `0x401E63` | `clientHandlerThread` | per-client `recv` loop: first packet is login (op1) → password check → `addPlayerSlot` → welcome(op8) + `sendFullState`; then dispatches ops 2/3/4/6/7; logs off and `removePlayerSlot` on disconnect |
| `0x402B32` | `findOrAddEnemy` | find enemy record by name; else reuse an empty or the oldest (>30 tick) slot |
| `0x402BE6` | `broadcastToPlayers` | `send` a buffer to every connected player socket (used for navsay) |
| `0x402C18` | `addPlayerSlot` | claim first empty player record for a socket, return its pointer |
| `0x402C47` | `removePlayerSlot` | zero the player record whose socket matches |
| `0x402C72` | `sendFullState` | send all current enemies (op1) + players (op2) to a freshly joined client |
| `0x402D50` | `atoiSigned` | custom decimal parser; leading byte `0x02` marks a negative value |

All console output is serialized through a single `CriticalSection` and colored
via `SetConsoleTextAttribute` (7 = label grey, 15 = value white, 12 = error red).

## Relationship to elfbot.dll

The bot half of NavNet lives in `elfbot.dll` (client side: `WSOCK32` `connect`
/ `send` / `recv`, `gethostbyname`). `navserv.exe` is the optional self-hosted
hub; a party can instead point at any shared host running this binary. See the
elfbot networking subsystem docs for the client encoder/decoder.
