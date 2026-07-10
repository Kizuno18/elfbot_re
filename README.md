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
| [`docs/01-overview.md`](docs/01-overview.md) | Architecture, injection chain, subsystem map |
| [`docs/02-static-analysis.md`](docs/02-static-analysis.md) | PE structure, sections, imports, strings per binary |
| [`docs/03-packer-armadillo.md`](docs/03-packer-armadillo.md) | The Armadillo protection on `elfbot.dll`; why static RE still works |
| [`docs/04-navnet-server.md`](docs/04-navnet-server.md) | `navserv.exe` complete function-by-function + wire protocol |
| `docs/05-injection-chain.md` | `loader.exe` + `elfload.dll` + `EcInit` (WIP) |
| `docs/06+` | `elfbot.dll` core + subsystems (WIP) |

## Method

- **Static analysis:** IDA Pro headless (idalib) + Hex-Rays, driven over MCP.
  Function names/comments are persisted into the `.i64` as analysis proceeds.
- Local triage with `pefile` (`tools/pe_recon.py`, `tools/strings_recon.py`).
- Findings are written here as prose + tables, addresses are file-absolute
  (imagebase `0x10000000` for `elfbot.dll`, `0x400000` for the EXEs).

## Conventions

LF endings, UTF-8, English. Binaries live in `samples/`. IDA databases are not
committed (regenerable). Addresses are given as `0xVA` at the stated imagebase.
