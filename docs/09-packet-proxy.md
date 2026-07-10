# elfbot.dll — packet proxy / IPC server

ElfBot exposes the live Tibia network stream to external tools and NavNet peers,
and lets them inject packets, through an embedded TCP server plus the incoming
packet hook. This is the "proxy" half of the networking subsystem; the NavNet
client half is covered in the NavNet docs.

## Two halves

- **Inbound (server → tools):** `hook_incomingPacketParser` `0x10001CA8`
  ([08](08-client-hooks-engine.md)) copies each incoming game packet to every
  subscribed proxy client socket in `dword_1005DA85[16]`.
- **Outbound (tools → server) + control:** the embedded TCP server accepts proxy
  clients and lets them inject packets into the client's send path.

## Embedded server

`installClientHooks_proxyServer` `0x10002041` `socket`/`bind(hostshort)`/
`listen`/`accept` loop spawns one `proxyClientThread` `0x10002235` per
connection.

## Proxy client protocol — `proxyClientThread` `0x10002235`

On connect it seeds a 40-byte state record (`unk_10042004`) and, if
`byte_1004203A`, sends a 14-byte banner (`byte_1004202C`). Then a `recv(1024)`
loop dispatches on the command byte at offset +6:

| Cmd | Action |
|---|---|
| `1` | send the 40-byte state record back |
| `10` | subscribe (`sub_100023C9` registers the socket in the proxy slot array); if `MEMORY[0x636FE0] != 30` kick a resync (`sub_10039BBB`) |
| `20` | disconnect: `closesocket` + `sub_1000239B` (unregister slot) + `ExitThread` |
| `0x87` | no-op / keepalive |
| other | if injection enabled (`dword_1005DB5C`): treat payload as a packet, set length `= *(u16)buf - 4`, and **inject it into the Tibia send path** via `sub_1002ADE7` |

`sub_1002ADE7` is the **packet-injection primitive** — it hands a crafted buffer
to the client's outgoing network routine, so external tools (and CiroScript
`say`/`use`/move commands that go over the wire) reach the server as if the
client sent them. `sub_1002AE6F` is the bot's `memcpy`.

## Slot management

- `dword_1005DA85[16]` — proxy client sockets; `unk_1005DAC5[16]` — per-socket
  state (`0` free, `1` streaming, `2` handshaking).
- `sub_100023C9` claims a slot for a socket; `sub_1000239B` releases it.
- `dword_1005DB5C` / `dword_1005DB58` gate injection and resync behaviour.
- `MEMORY[0x636FE0] == 30` is the client "in-game" state used to gate proxy
  work.

## Relationship to NavNet

The 16-socket proxy array is shared with the NavNet client: NavNet peers connect
as proxy clients to exchange positions, and the same forward path
(`hook_incomingPacketParser`) drives both. The NavNet wire protocol matches
`navserv.exe` ([04](04-navnet-server.md)); the client encoder/decoder lives in
the NavNet dialog subsystem (`connect`/`gethostbyname` in `sub_10020D53` /
`sub_1003FAA1`), documented in the NavNet client pass.

## Follow-up

- `sub_1002ADE7` (injection) — exact client send-routine call and framing.
- `sub_10001C38` / `sub_10001960` — proxy handshake + framing used by the
  inbound forwarder.
- NavNet client encode/decode (`sub_10020BA4`, `sub_100244E1`, `sub_1003FAA1`).
