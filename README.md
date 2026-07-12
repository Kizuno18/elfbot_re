# elfbot_re — ElfBot NG 8.60 reverse engineering

Private research repo. Full static reverse engineering and function-by-function
documentation of **ElfBot NG 8.60**, a memory-injection bot for the Tibia 8.60
game client (circa 2010). Every binary in the distribution is disassembled with
IDA Pro + Hex-Rays and documented here.

Everything is RE of binaries the operator legally possesses, on the operator's
own lab. No game servers are touched — the static RE was additionally confirmed
by injecting the bot into a genuine, offline Tibia 8.6 client and observing it
live ([docs/28](docs/28-runtime-validation.md)).

## The distribution

| File | Size | What it is | Protection |
|---|---|---|---|
| `elfbot.dll` | 4.6 MB | **the bot** — injected into `Tibia.exe`, exports `EcInit` | Armadillo (code plaintext, one encrypted `.aqfu` blob) |
| `loader.exe` | 293 KB | GUI launcher / injector | Borland Delphi, unpacked |
| `elfload.dll` | 36 KB | injected loader stub that maps `elfbot.dll` | MSVC, unpacked |
| `navserv.exe` | 12 KB | NavNet position-sharing server | MSVC, unpacked — **fully documented** |
| `USkin.dll` | 692 KB | third-party window-skinning library (41 `USkin*` exports) | off-the-shelf, unpacked |
| `unins000.exe` | 695 KB | Inno Setup uninstaller | standard, out of scope |

Data assets: `scripts/*.elfc`/`*.elft` (compiled CiroScript cavebot/targeting
scripts), `elfsettings/`, `lootitems.txt`, `outfits.txt`, `hotkeys.ini`,
`sounds/`, `skins/`, `minimaps/`, `playerinfo/`.

## Docs

| Doc | What |
|---|---|
| [`docs/00-status.md`](docs/00-status.md) | Resume point — what's done / in progress / TODO |
| [`docs/01-overview.md`](docs/01-overview.md) | Architecture, injection chain, subsystem map |
| [`docs/02-static-analysis.md`](docs/02-static-analysis.md) | PE structure, sections, imports, strings per binary |
| [`docs/03-packer-armadillo.md`](docs/03-packer-armadillo.md) | The Armadillo protection; why static RE still works |
| [`docs/04-navnet-server.md`](docs/04-navnet-server.md) | `navserv.exe` complete function-by-function + wire protocol |
| [`docs/05-ui-init-framework.md`](docs/05-ui-init-framework.md) | Boot path, `EcInit`, the 23-dialog framework |
| [`docs/06-injection-chain.md`](docs/06-injection-chain.md) | loader.exe (madCodeHook) → elfload.dll → EcInit |
| [`docs/07-ciroscript-language.md`](docs/07-ciroscript-language.md) | CiroScript commands/conditionals, `.elfc`/`.elft` |
| [`docs/08-client-hooks-engine.md`](docs/08-client-hooks-engine.md) | Inline hooks, packet-parser hook, full-light, shadow tables |
| [`docs/09-packet-proxy.md`](docs/09-packet-proxy.md) | Embedded proxy server, protocol, packet injection |
| [`docs/10-feature-subsystems.md`](docs/10-feature-subsystems.md) | All 23 feature dialogs mapped + named |
| [`docs/11-ciroscript-engine.md`](docs/11-ciroscript-engine.md) | CiroScript VM: 422 commands → handlers, hash dispatch |
| [`docs/12-script-crypto-compression.md`](docs/12-script-crypto-compression.md) | Crypto/compression cluster = **unused static lib** (zlib 1.2.3); net cipher is client XTEA |
| [`docs/13-engine-tick-loop.md`](docs/13-engine-tick-loop.md) | **Master control flow** — `botMainTickLoop`, the timed subsystem dispatch |
| [`docs/14-ciroscript-runtime.md`](docs/14-ciroscript-runtime.md) | CiroScript interpreter runtime (script execution each tick) |
| [`docs/15-healer-engine.md`](docs/15-healer-engine.md) | Healer: heal-spell/potion ladder + offensive casting |
| [`docs/16-targeting-engine.md`](docs/16-targeting-engine.md) | Targeting: creature scoring, battle-list, attack |
| [`docs/17-cavebot-walker.md`](docs/17-cavebot-walker.md) | Walker/pathfinder: 18×14 cost grid, BFS, flee/retreat |
| [`docs/18-navnet-codec.md`](docs/18-navnet-codec.md) | NavNet position-sharing + synthetic-packet builders |
| [`docs/19-cavebot-waypoints.md`](docs/19-cavebot-waypoints.md) | Cavebot waypoint loading, record types, in-memory table |
| [`docs/20-client-hooks-deep.md`](docs/20-client-hooks-deep.md) | Client hook engine (deep): parser hook, shadow tables, full-light |
| [`docs/21-player-state.md`](docs/21-player-state.md) | Player-state snapshot + exp meter (client offsets read) |
| [`docs/22-elfc-file-format.md`](docs/22-elfc-file-format.md) | `.elfc`/`.elft` format cracked (sparse-opcode) + `decode_elfc.py` |
| [`docs/23-looting-engine.md`](docs/23-looting-engine.md) | Looter: corpse scan, container table, depot state machine |
| [`docs/24-hotkeys-alarms.md`](docs/24-hotkeys-alarms.md) | Hotkey/label engine, alarms, DirectSound |
| [`docs/25-cavebot-targeting-sync.md`](docs/25-cavebot-targeting-sync.md) | Cavebot ↔ targeting ↔ healer synchrony (the flag triad) |
| [`docs/26-aimbot-combo.md`](docs/26-aimbot-combo.md) | AutoAim square-scan engine + combo sync (PvP core) |
| [`docs/27-subsystem-relations.md`](docs/27-subsystem-relations.md) | **All 23 tabs + every inter-tab relation** (the graph) |
| [`docs/28-runtime-validation.md`](docs/28-runtime-validation.md) | **Live injection into genuine Tibia 8.6** — unpack, DllMain, hooks confirmed |
| [`docs/29-ui-layout-geometry.md`](docs/29-ui-layout-geometry.md) | **Exact pixel geometry of every panel/control** (live capture) + [`ui/*.json`](ui/elfbot-ui-geometry.json) |
| [`docs/30-runtime-session-log.md`](docs/30-runtime-session-log.md) | Live driving of the OTServ-patched client: login path proven to server auth, crash-fix, pending items |
| [`docs/31-gap-resolutions.md`](docs/31-gap-resolutions.md) | 4 behavior-parity GAPs resolved offline: `g_100f0e20` is a creature ptr, `auto N`, `dontlist`, deposit states `{0,2,3,5,7}` |
| [`docs/32-icons-tab.md`](docs/32-icons-tab.md) | **Command Icons tab (TBOTDLGW)**: record layout, render/click path, seticonactive/seticontext |
| [`docs/33-runtime-ingame-validation.md`](docs/33-runtime-ingame-validation.md) | **In-game injection on local TFS 0.4** — bot injected into a live in-world client, hooks confirmed |
| [`docs/34-tabs-lists-extras-hud-spy-links.md`](docs/34-tabs-lists-extras-hud-spy-links.md) | Dedicated RE of Lists, Extras, HUD On-Screen, Creature Spy, Links tabs |
| [`docs/35-tab-runtime-matrix.md`](docs/35-tab-runtime-matrix.md) | **Every tab → doc → runtime-test matrix** (coverage tracker) |
| [`docs/functions/index.md`](docs/functions/index.md) | Master index — every function (7125) decompiled + purpose |

## Method

- **Static analysis:** IDA Pro headless (idalib) + Hex-Rays, driven over MCP.
  Function names/comments are persisted into the `.i64` as analysis proceeds.
- Local triage with `pefile` (`tools/pe_recon.py`, `tools/strings_recon.py`).
- Findings are written here as prose + tables, addresses are file-absolute
  (imagebase `0x10000000` for `elfbot.dll`, `0x400000` for the EXEs).

## Conventions

LF endings, UTF-8, English. Binaries live in `samples/`. IDA databases are not
committed (regenerable). Addresses are given as `0xVA` at the stated imagebase.
