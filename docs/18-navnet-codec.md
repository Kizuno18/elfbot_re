## NavNet & synthetic-packet codec

ElfBot NG 8.60 (`elfbot.dll`, imagebase `0x10000000`) injected into Tibia 8.60 client (imagebase `0x400000`). This engine covers two cooperating protocols: the **NavNet** peer position/creature-sharing wire format, and a **synthetic server-packet forger** whose output is injected back into the client by an embedded localhost proxy. All addresses are file-absolute at the stated imagebases. Function names and `0xADDR` match the IDA database.

### 1. Topology

```
botMainTickLoop(0x100227bd) ──timed──▶ sendNavPositionUpdate(0x1003ffdf)
                                            │ send() over dword_1005F539 (NavNet peer socket)
                                            ▼
                                     NavNet peers (position + creature relay)

installClientHooks_proxyServer(0x10002041) [own thread]
   ├─ inline-hooks Tibia client (0x5AB5D4 / 0x4F30C0 / 0x45ACD6)
   └─ localhost accept loop ──▶ CreateThread(signatureCheckStub, conn_socket)
                                     │
                                     ▼
                            buildFullGameStateSnapshot(0x10001960)
                            forges a real 8.60 server packet from client memory,
                            proxy replays it into the client's parser
```

The two halves share the same serialization primitives (`packetOpcodeHasCoordFlag`, `encodeCreatureAppear`, `memcpyBytes`) and the same client-memory layout knowledge, so they are documented as one engine.

---

### 2. NavNet position update — `sendNavPositionUpdate` (0x1003ffdf)

Called on the bot tick. Builds status/position packets on a 0x2000-byte stack buffer (`buf`, ebp-0x2000) and pushes them through the NavNet peer socket `dword_1005F539` via the imported `send` thunk (0x100408ce).

**Step 1 — floor/sequence change beacon.** Compares a monotonically changing dword `dword_1005F7E5` against last-sent `dword_100EE8CC`. On change it emits a 5-byte opcode-`0x06` record `[06][dword_1005F7E5]` and updates the shadow:

```c
if ( dword_1005F7E5 != dword_100EE8CC ) {
    dword_100EE8CC = dword_1005F7E5;
    buf = 6;                         // opcode 0x06
    v13 = dword_1005F7E5;
    send(dword_1005F539, &buf, 5, 0);
}
```

**Step 2 — position status packet (opcode 0x02, 11 bytes).** Layout:

| off | size | field | source |
|-----|------|-------|--------|
| 0 | 1 | opcode = `0x02` | literal |
| 1 | 4 | attack-target XY | `dword_10052768` / `dword_1005276C`, zeroed if no target |
| 5 | 1 | target Z / attack flag | `dword_10052770` |
| 6 | 1 | flags = `(2*byte_1005F7D9) | byte_100EE8BA` | status/alarm bits |
| 7 | 2 | player X | `MEMORY[0x63FE78]` |
| 9 | 2 | player Y | `MEMORY[0x63FE74]` |

The target coords are included only when `!dword_1005F541 || dword_1005F545` (a "share target" toggle); otherwise zeroed. `byte_100EE8BA` is a one-shot event flag cleared after read (`byte_100EE8BA = 0`).

**Step 3 — dedupe + creature relay.** The 11-byte packet is compared against the last-sent copy cached at `unk_1009A4EE`. `byte_1005F538` is a "force send" flag:

- Force set: `send(...,11,...)`, cache to `unk_1009A4EE`, clear force flag, then run the creature-relay loop below.
- Force clear: byte-compare current vs `unk_1009A4EE`; send + re-cache only if they differ (position moved). No creature relay on this path.

**Creature relay (type-3 records).** Guarded by `!byte_101D5E28 && dword_1005F53D` (relay enabled, not suppressed). Walks the client visible-creature table from `0x63FEF8` to `0x64A308` in **168-byte stride** (this is Tibia 8.60's on-screen creature array; the loop bound `6553336 == 0x63FEF8`). For each slot whose `+144` byte (visible/active flag) is set and whose name at `+4` matches `matchNameAgainstListB`, it appends:

```c
*p = 3;                              // type 3 = creature-share record
strcpy(p+1, name@(i+4)); p += len+1; // NUL-terminated name
*(WORD*)p = *(WORD*)(i+36);           // creature X
*(WORD*)p = *(WORD*)(i+40);           // creature Y
*(BYTE*)p = *(BYTE*)(i+44);           // creature Z
```

Creature-record field offsets inside the 168-byte slot: `+4` name, `+36` X, `+40` Y, `+44` Z, `+144` active flag. The accumulated block is sent as one `send()` if non-empty. This is how NavNet peers see each other's tracked targets.

---

### 3. Name-list matcher — `matchNameAgainstListB` (0x1003a494)

Shared filter used by the creature relay. Guarded by `checkPlayerOnTileFilter` (a tile-based pre-filter; returns 1 to short-circuit). Iterates the **512-entry, 32-byte-stride** name table `byte_1005F8A8` with `lstrcmpi` and prefix rules:

| first bytes | rule |
|-------------|------|
| `\0` | end of list |
| `*` (0x2A) | wildcard/self-relative compare against `this+32` |
| `++` (word 11051 = 0x2B2B) | compare arg name to entry `+2` |
| `+` (0x2B) | compare arg name to entry `+1` |
| else | compare arg name to entry verbatim |

Returns 1 on first match. The `sub_1003a1e5==1` guard mentioned in the header gates the whole scan. This is the bot's targeting/friend name list — directly a detection surface.

---

### 4. Synthetic game-state builder — `buildFullGameStateSnapshot` (0x10001960)

Forges a complete Tibia 8.60 server-to-client packet from the client's own memory. Allocates a 0xC350-byte (50000) `GlobalAlloc(GMEM_MOVEABLE, ...)` + `GlobalLock` buffer (`buf` global) when passed NULL. Layout of the produced packet:

| off | size | content | encoder |
|-----|------|---------|---------|
| 0 | 2 | outer length (payload+6) | written last |
| 2 | 1 | — | header region |
| 3 | 2 | inner length (payload) | written last |
| 8 | 14 | login/self-appear template `byte_1004203F` | inline / patched |
| 17 | 2 | player X | `dword_1005D883` |
| 19 | 2 | player Y | `dword_1005D887` |
| 21 | 1 | player Z | `dword_1005D88B` |
| 22.. | var | **map description** | `buildMapDescriptionPacket` (0x1000133f) |
| — | var | VIP list | `encodeVipList` (0x1000154b) |
| — | 25 | player stats (opcode 0xA0) `byte_10042051` | `fillPlayerStatsRecord` (0x1000188b) |
| 47 | 3 | world light (opcode 0x82) `byte_10042079` | `fillWorldLightRecord` (0x10001870) |
| 50 | 15 | skills (opcode 0xA1) `byte_1004206A` | `fillSkillsRecord` (0x10001929) |
| — | var | battle list | `copyBattleListRecords` (0x100017e1) |
| — | var | tile/container items (0x6A/0x6C) | `encodeContainerAndTileItems` (0x1000159e) |
| — | var | open channels (0x6E) | `encodeOpenChannels` (0x10001708) |
| — | var | private/party channels | `copyPrivateAndPartyChannels` (0x10001813) |

When `byte_1004203F == 0` the login stub is synthesized: opcode `10` (0x0A self-appear), player-id `MEMORY[0x62CD30]`, and constant `1677721650` (0x63FFFFF2). Each sub-encoder is gated by a `byte_1005DB4x` "skip" flag so the caller can produce partial snapshots. Final length fixup:

```c
v4 = v3 - 8 - a1;          // inner payload length
*((WORD*)a1 + 3) = v4;     // off 6 inner length
v4 += 6;
*(WORD*)a1 = v4;           // off 0 outer length
return v4 + 2;
```

#### 4a. Map description — `buildMapDescriptionPacket` (0x1000133f)

Reproduces Tibia 8.60's map-description encoding: floor range chosen from player Z (`dword_1005D88B`; underground `>7` uses Z-2..Z+2 clamped to 15, surface uses floors 7..0), then nested `18 (0x12) × 14 (0x0E)` tile scan via `mapCoordsToTilePtr(x,y,z)`. Per tile it emits stack items, `0xFF` skip-run RLE (`v19` run counter, max 255), and creatures through `encodeCreatureAppear` when the item id is `99` (0x63 = creature marker). Uses `packetOpcodeHasCoordFlag` to decide whether a third stack byte follows. It also records container-holding creature ids into `dword_1005D48F[]` (indexed by `dword_1005D877`) and sets `dword_1005D487` on the first tile, consumed later by the tile-item encoder.

#### 4b. VIP list — `encodeVipList` (0x1000154b)

Iterates the **10-slot, 12-byte-stride** VIP table based at `0x639164`/`0x639168` (i.e. slot i at `0x639164 + 12*i`). Each non-zero entry emits opcode `0x78` (120) VIP-add: `[78][slot][WORD name/id]` plus an optional online status byte, again gated by `packetOpcodeHasCoordFlag`.

#### 4c. Player stats — `fillPlayerStatsRecord` (0x1000188b)

Snapshots the client stat block at `0x62CD00..0x62CD2C` into the 25-byte template `byte_10042051` (opcode `0xA0` = -96). Field map:

| tpl off | client addr | field |
|---------|-------------|-------|
| 0 | — | opcode 0xA0 |
| +1 | 0x62CD2C | HP |
| +3 | 0x62CD28 | max HP |
| +5 | 0x62CD00 | capacity |
| +9 | 0x62CD24 | experience |
| +13 | 0x62CD20 | level |
| +15 | 0x62CD18 | level % |
| +16 | 0x62CD10 | mana |
| +18 | 0x62CD0C | max mana |
| +20 | 0x62CD1C | magic level |
| +21 | 0x62CD14 | magic level % |
| +22 | 0x62CD08 | soul |
| +23 | 0x62CD04 | stamina |

#### 4d. World light — `fillWorldLightRecord` (0x10001870)

3-byte template `byte_10042079` = `[82][MEMORY[0x63BAB8] level][0xD7 color]` (opcode `0x82` world light).

#### 4e. Skills — `fillSkillsRecord` (0x10001929)

Opcode `0xA1` (-95) into `byte_1004206A`. Loops 7 skills (0x1C bytes / 4-byte stride) copying value from `0x62D8D8` region (`6474968 = 0x62D858`, `6474940 = 0x62D83C`) as value/percent pairs into `byte_1004206B[]`/`byte_1004206C[]`.

#### 4f. Battle list — `copyBattleListRecords` (0x100017e1)

Copies the **150-slot (0x96), 40-byte-stride** creature/battle table `unk_1005A2A3` verbatim. Each active slot (`+0` non-zero) copies `WORD@+5 + 8` bytes (record length prefix at `+5`) into the output. This is the pre-serialized battle-list already maintained by the client hooks.

#### 4g. Tile / container items — `encodeContainerAndTileItems` (0x1000159e)

Runs only when `dword_1005D487` (set by the map builder). Emits tile add/remove opcodes `0x6A` (106) / `0x6C` (108) at the stored player coords (`dword_1005D883-8`, `dword_1005D887-6`, `dword_1005D483`). Walks the **160-byte-stride** item/container table at `0x62CD90` (up to 0xFA=250 slots), skipping ids already recorded in `dword_1005D48F[]`, then walks the tile item stack from `mapCoordsToTilePtr(0,0,z)`, using `encodeCreatureAppear` for id `99` and `packetOpcodeHasCoordFlag` for stack-byte handling.

#### 4h. Open channels — `encodeOpenChannels` (0x10001708)

Iterates the **16-slot, 492-byte-stride** channel table at `0x6391E8` (channel id at `+0`, `+4`; name at `+16` via `lstrlen`; message array at `+60` with 12-byte entries). Emits opcode `0x6E` (110) open-channel packets: `[6e][slot][WORD id][WORD namelen][name][WORD count][messages...]`.

#### 4i. Private/party channels — `copyPrivateAndPartyChannels` (0x10001813)

Copies two **20-slot (0x14), 69-byte-stride** tables `unk_1005CF17` (private) and `unk_1005C9B3` (party) verbatim; each active slot copies `WORD@+3 + 5` bytes.

---

### 5. Client hooks + proxy server — `installClientHooks_proxyServer` (0x10002041)

Runs on its own thread (started by `startNavServerThread` 0x10001000, whose body failed to decompile but whose only job per its name/xref is `CreateThread(installClientHooks_proxyServer)`). One-time init gated by `byte_1005A290`:

**Three inline hooks into the Tibia 8.60 client (imagebase 0x400000):**

| target | original saved to | hook installed | purpose |
|--------|-------------------|----------------|---------|
| `0x5AB5D4` (call-table slot) | `dword_1005D88F` | overwrites pointer with `hook_captureRenderCtx` | grabs render/game context ptr; `VirtualProtect(0x5AB000,0x604,PAGE_READWRITE)` first |
| `0x4F30C0` | `dword_1005D893 = target+5+rel` | writes `0xE9` (jmp) if byte was `0xE9` | function detour |
| `0x45ACD6` | `dword_1005D897 = target+rel(4566234)` | writes rel32 to `hook_incomingPacketParser-4566234` | intercepts the client's incoming-packet parser — the injection point for forged packets |

Hooks are written with `WriteProcessMemory(hProcess, ...)` (self-process handle) so they survive as real patched bytes.

**Proxy accept loop.** `WSAStartup(2.2)`, `socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)` → `s`, binds `sockaddr_in` built inside `WSAData.lpVendorInfo+2` (family 2, port `word_1005DA2F = htons(hostshort)`, addr `dword_1005DA31 = 0` = INADDR_ANY), `listen(s,5)`, then loops `accept` spawning `CreateThread(signatureCheckStub, conn_socket)` per connection. `byte_1005A291` breaks the loop and triggers `WSACleanup`. `signatureCheckStub` (last-connection socket stored in `lpParameter`) is the per-client worker that drives `buildFullGameStateSnapshot` and replays forged packets through the `0x45ACD6` parser hook.

---

### 6. Serialization primitives

- `packetOpcodeHasCoordFlag` (0x100014ec xref target): given a stack item opcode, returns whether an extra stack-position byte follows (Tibia 8.60 stackable/count item rule). Called from every item/creature encoder.
- `encodeCreatureAppear`: serializes a creature-appear sub-packet for creature id (item id `99`/`0x63`). Shared by map, tile and container encoders.
- `memcpyBytes` (0x1002ae6f): thin `qmemcpy` wrapper used for all template/table blits.
- `mapCoordsToTilePtr`: resolves `(x,y,z)` to the client tile struct pointer (returns int* where `[0]` = stack count, `[1..]` = 3-dword item records `{opcode, count/id, coordbyte}`).

The rest of the closure (`send`, `socket`, `bind`, `listen`, `htons`, `WSAStartup`, `GlobalAlloc`, `GlobalLock`, `VirtualProtect`, `WriteProcessMemory`, `CreateThread`) are plain IAT thunks.

## Key globals

| Address | Meaning |
|---|---|
| `dword_1005F539` | NavNet peer TCP socket handle; destination for all sendNavPositionUpdate() send() calls. |
| `dword_1005F7E5 / dword_100EE8CC` | Current floor/sequence counter and its last-sent shadow; mismatch triggers the 0x06 beacon. |
| `dword_1005F541 / dword_1005F545` | Share-target toggle pair gating whether attack-target coords are included in the 0x02 status packet. |
| `dword_10052768 / dword_1005276C / dword_10052770` | Current attack-target X / Y / Z (or attack flag) coordinates copied into the NavNet status packet. |
| `byte_1005F7D9 / byte_100EE8BA` | Status/alarm flag bits combined into the packet flags byte; byte_100EE8BA is a one-shot event flag cleared after read. |
| `byte_1005F538` | Force-send flag for the NavNet status packet; when set, sends unconditionally and runs the creature relay, then clears. |
| `unk_1009A4EE` | 11-byte cache of the last-sent NavNet status packet, used to suppress duplicate position sends. |
| `byte_101D5E28 / dword_1005F53D` | Creature-relay suppress flag and enable flag; both must permit before type-3 creature records are appended. |
| `0x63FEF8..0x64A308` | Tibia 8.60 client visible-creature array, 168-byte stride; NavNet reads name@+4, X@+36, Y@+40, Z@+44, active@+144. |
| `MEMORY[0x63FE74] / MEMORY[0x63FE78]` | Local player Y / X client globals read into the NavNet position packet. |
| `byte_1005F8A8` | 512-entry 32-byte-stride name/target list matched by matchNameAgainstListB; the bot's friend/target filter. |
| `buf (0x10001960 global)` | GlobalLock'd 50000-byte scratch buffer holding the forged synthetic server packet. |
| `dword_1005D883 / dword_1005D887 / dword_1005D88B` | Cached player X / Y / Z used across the map, tile and channel encoders. |
| `byte_1005DB41..46` | Per-section skip flags gating which sub-encoders run in buildFullGameStateSnapshot (party/channels/battle/light/VIP). |
| `byte_10042051 / byte_1004206A / byte_10042079 / byte_1004203F` | Static packet templates: player stats (0xA0), skills (0xA1), world light (0x82), login/self-appear stub. |
| `0x62CD00..0x62CD30` | Client player-stats block (HP/mana/cap/exp/level/soul/stamina/player-id) sourced by fillPlayerStatsRecord. |
| `0x62CD90` | Client container/item table, 160-byte stride, walked by encodeContainerAndTileItems. |
| `0x639164 / 0x6391E8` | VIP table (12-byte stride, 10 slots) and channel table (492-byte stride, 16 slots). |
| `unk_1005A2A3 / unk_1005CF17 / unk_1005C9B3` | Pre-serialized battle-list (150x40), private-channel (20x69) and party-channel (20x69) record tables. |
| `dword_1005D487 / dword_1005D877 / dword_1005D48F` | Map-scan flag, captured-creature-id count, and the creature-id array shared between map and tile encoders. |
| `byte_1005A290 / byte_1005A291` | Proxy one-time-init guard and accept-loop shutdown flag. |
| `dword_1005D88F / dword_1005D893 / dword_1005D897` | Saved original targets of the three client inline hooks (render-ctx slot, 0x4F30C0 detour, incoming-packet parser). |
| `word_1005DA2F / dword_1005DA31` | Proxy listen sockaddr_in port (htons) and bind address (0 = INADDR_ANY). |

## Detection notes

- Three fixed-address inline hooks in the Tibia 8.60 client (imagebase 0x400000): a call-table slot overwrite at 0x5AB5D4, a 0xE9 detour at 0x4F30C0, and a rel32 patch at 0x45ACD6 (incoming-packet parser). Integrity-scan these bytes against a clean client image — any of them modified is a definitive elfbot fingerprint.
- The saved-original pointers dword_1005D88F/dword_1005D893/dword_1005D897 in elfbot.dll hold client addresses (0x5AB5D4 slot value, 0x4F30C0+5+rel, 0x45ACD6+rel) — reading these back and comparing to the live client detour targets confirms an active hook.
- A localhost TCP listener created by the module: socket()/bind(INADDR_ANY, htons(word_1005DA2F))/listen(backlog 5)/accept loop in a non-client thread. Enumerate listening sockets owned by the Tibia process; an unexpected LISTEN socket spawning per-connection threads is the proxy server.
- NavNet peer traffic: outbound TCP on dword_1005F539 carrying an 11-byte opcode-0x02 record [02][targetXY 4][targetZ 1][flags 1][playerX 2][playerY 2], a 5-byte opcode-0x06 beacon, and variable type-3 name+coord creature records. Distinct from real Tibia login-server protocol; flag on the wire.
- Memory-scan the module for the fixed global tables: 512-entry 32-byte-stride name list at byte_1005F8A8, VIP scan of 0x639164 (12B), channel scan of 0x6391E8 (492B), battle-list unk_1005A2A3 (150x40), and the 168-byte-stride read walk over the client creature array 0x63FEF8..0x64A308 — these access patterns (reading player stat block 0x62CD00, light 0x63BAB8, skills 0x62D83C) are not something the vanilla client does from an injected DLL.
- A 50000-byte GlobalAlloc/GlobalLock buffer that gets populated with a byte-for-byte valid 8.60 server packet (correct outer/inner length headers, opcodes 0x0A/0xA0/0xA1/0x82/0x6A/0x6C/0x6E/0x78) and then fed into the client's own parser via the 0x45ACD6 hook — a forged inbound packet whose source is the client's own memory rather than the network socket.
- WriteProcessMemory / VirtualProtect(0x5AB000, 0x604, PAGE_READWRITE) calls against the host process itself and WSAStartup(2.2) from within the injected module are behavioral tripwires observable via API hooking or ETW.
- byte_1005A290 (proxy init guard) and byte_1005A291 (shutdown) plus the shadow-cache unk_1009A4EE are stable module-relative offsets — a signature over the sendNavPositionUpdate packet-build code (imm 0x02/0x06 opcodes, 168 stride, 0x63FE74/0x63FE78 reads) yields a reliable static YARA-style match on elfbot.dll.
