# elfbot_re — ElfBot NG 8.60 reverse engineering

Private research repo. Full static reverse engineering and function-by-function
documentation of **ElfBot NG 8.60**, a memory-injection bot for the Tibia 8.60
game client (circa 2010). Every binary in the distribution is disassembled with
IDA Pro + Hex-Rays and documented here.

Everything is RE of binaries the operator legally possesses, on the operator's
own lab. No game servers are touched; this is pure static analysis.

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
| [`docs/12-script-crypto-compression.md`](docs/12-script-crypto-compression.md) | `.elfc`/`.elft` protection: Blowfish, BWT, LZW, block ciphers |
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
