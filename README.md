# ElfBot NG Reverse Engineering

**Architecture, script formats, function catalogs, and local runtime evidence for ElfBot NG on Tibia 8.60.**

[Start here](docs/01-overview.md) · [Documentation](#documentation) · [Function index](docs/functions/index.md) · [Runtime report](docs/39-module-runtime-report.md)

`elfbot_re` is a reverse-engineering reference for **ElfBot NG**, a native Windows
bot that runs inside the Tibia client. The research connects the loading chain,
client hooks, CiroScript interpreter, feature engines, interface, and NavNet
protocol to recovered functions and controlled runtime observations.

The deliverable is a documentation and analysis corpus—not the original vendor
source code, a maintained bot release, or a gameplay setup guide.

## Research highlights

- **Function-level reference.** The `elfbot.dll` index covers **7,125 recovered
  functions** across the bot and support-code sections, with separate coverage
  for the loader and auxiliary components. See the
  [master function index](docs/functions/index.md).
- **From file formats to engine behavior.** The documentation maps the CiroScript
  interpreter and its **422-command** dispatch surface, the `.elfc` / `.elft`
  sparse-opcode format, client-state mirrors, subsystem scheduling, and
  [inter-module relationships](docs/27-subsystem-relations.md).
- **Static findings checked in a local environment.** Reports cover the loading
  chain, byte-matched hooks, live player-state mirrors, and a behavioral test
  sweep against a genuine Tibia 8.60 client connected to a local TFS 0.4 server.
  See the [end-to-end report](docs/38-runtime-e2e-genuine-client.md) and
  [module-level evidence](docs/39-module-runtime-report.md).

## Architecture at a glance

```text
loader.exe
    |
    v
elfload.dll ---------------------> USkin.dll / interface support
    |
    v
elfbot.dll inside Tibia.exe
    |
    +-- EcInit / interface framework
    +-- Client hooks and player-state mirrors
    +-- Engine tick loop
    |     +-- CiroScript / hotkeys
    |     +-- Healing / targeting / cavebot / looting
    |     +-- Lists / alarms / HUD / icons
    |
    +-- Embedded proxy and NavNet client
                              |
                              v
                         navserv.exe
                    position-sharing server
```

The [injection chain](docs/06-injection-chain.md),
[engine loop](docs/13-engine-tick-loop.md), and
[subsystem map](docs/27-subsystem-relations.md) explain how the pieces fit together.
Later runtime reports also distinguish a minimal manually booted engine from the
full loading and hook-initialization path.

## Analyzed components and coverage

| Component | Role | Coverage reference |
| --- | --- | --- |
| `elfbot.dll` | Injected engine, client hooks, CiroScript, feature subsystems, and interface | [Master function index](docs/functions/index.md) |
| `loader.exe` | GUI launcher and injection framework | [Injection chain](docs/06-injection-chain.md) / [Loader catalog](docs/functions/loader-catalog.md) |
| `elfload.dll` | Loader stub connecting injection to bot initialization | [Injection chain](docs/06-injection-chain.md) |
| `navserv.exe` | NavNet position-sharing server | [Server and protocol](docs/04-navnet-server.md) |
| `USkin.dll` | Third-party window-skinning support | [Exports and integration](docs/37-uskin-and-support-section.md) |
| `unins000.exe` | Standard uninstaller | Distribution triage; outside the bot-logic scope |

The [coverage report](docs/00-status.md) separates bot logic from structural
library documentation:

| Analyzed region | Functions | Documentation depth |
| --- | --- | --- |
| `elfbot.dll` `.jdrv` | 1,190 | Bot-region catalog, purpose descriptions, and decompiled output |
| `elfbot.dll` `.jiru` / `.cdtemn` | 5,935 | Support-code catalog and decompiled output; much of the coverage is structural rather than an individual semantic deep-dive |
| `loader.exe` | 1,780 | Loader catalog and decompiled output, with focused injection analysis |
| `elfload.dll` | 6 | Loader-stub analysis |
| `navserv.exe` | 12 | Function-by-function server analysis |

The **7,125 figure applies to `elfbot.dll`**, not the combined distribution.
`USkin.dll` is documented separately through its 41 exported functions and
integration contract; it is not included in that total.

## Documentation

### Choose a reading path

| Goal | Start with |
| --- | --- |
| Understand the system | [Overview](docs/01-overview.md) → [Initialization](docs/05-ui-init-framework.md) → [Engine loop](docs/13-engine-tick-loop.md) |
| Explore scripting and file formats | [CiroScript language](docs/07-ciroscript-language.md) → [Interpreter](docs/11-ciroscript-engine.md) → [File format](docs/22-elfc-file-format.md) |
| Follow client state and feature engines | [Client hooks](docs/20-client-hooks-deep.md) → [Player state](docs/21-player-state.md) → [Subsystem relationships](docs/27-subsystem-relations.md) |
| Inspect runtime evidence | [End-to-end loading](docs/38-runtime-e2e-genuine-client.md) → [Module report](docs/39-module-runtime-report.md) → [Coverage matrix](docs/35-tab-runtime-matrix.md) |
| Navigate recovered functions | [Master index](docs/functions/index.md) → [Bot-region catalog](docs/functions/jdrv-catalog.md) / [Support-region catalog](docs/functions/jiru-catalog.md) |

<details>
<summary><strong>Complete documentation index — 40 chapters</strong></summary>

| Chapter | Subject |
| --- | --- |
| [00 — Status](docs/00-status.md) | Recorded coverage, milestones, and follow-up work |
| [01 — Overview](docs/01-overview.md) | Architecture, loading chain, and subsystem map |
| [02 — Static analysis](docs/02-static-analysis.md) | PE structure, sections, imports, and strings |
| [03 — Armadillo protection](docs/03-packer-armadillo.md) | Protection layout and static-analysis feasibility |
| [04 — NavNet server](docs/04-navnet-server.md) | Server functions and wire protocol |
| [05 — UI and initialization](docs/05-ui-init-framework.md) | Startup, `EcInit`, and dialog framework |
| [06 — Injection chain](docs/06-injection-chain.md) | Launcher, loader stub, and initialization contract |
| [07 — CiroScript language](docs/07-ciroscript-language.md) | Commands, conditionals, and script assets |
| [08 — Client hooks](docs/08-client-hooks-engine.md) | Hooks, shadow tables, and client integration |
| [09 — Packet proxy](docs/09-packet-proxy.md) | Embedded proxy, protocol, and injection behavior |
| [10 — Feature subsystems](docs/10-feature-subsystems.md) | Feature dialogs mapped to implementation |
| [11 — CiroScript engine](docs/11-ciroscript-engine.md) | Command handlers and hash-based dispatch |
| [12 — Crypto and compression](docs/12-script-crypto-compression.md) | Support-library analysis and its separation from the script path |
| [13 — Engine tick loop](docs/13-engine-tick-loop.md) | Timed subsystem dispatch and execution model |
| [14 — CiroScript runtime](docs/14-ciroscript-runtime.md) | Interpreter state and tick-by-tick script execution |
| [15 — Healer](docs/15-healer-engine.md) | Healing decisions, potions, and offensive casting |
| [16 — Targeting](docs/16-targeting-engine.md) | Creature scoring, battle-list scanning, and attack selection |
| [17 — Cavebot walker](docs/17-cavebot-walker.md) | Pathfinding, movement, fleeing, and retreat |
| [18 — NavNet codec](docs/18-navnet-codec.md) | Position-sharing and packet builders |
| [19 — Cavebot waypoints](docs/19-cavebot-waypoints.md) | Record types, loading, and in-memory tables |
| [20 — Client hooks, deep dive](docs/20-client-hooks-deep.md) | Parser integration, shadow tables, and display hooks |
| [21 — Player state](docs/21-player-state.md) | Client-state snapshots and experience tracking |
| [22 — Script file format](docs/22-elfc-file-format.md) | `.elfc` / `.elft` sparse-opcode encoding and decoder |
| [23 — Looting](docs/23-looting-engine.md) | Corpse scanning, containers, and depot state machine |
| [24 — Hotkeys and alarms](docs/24-hotkeys-alarms.md) | Hotkeys, labels, scheduling, and sound |
| [25 — Subsystem synchronization](docs/25-cavebot-targeting-sync.md) | Cavebot, targeting, and healer state coordination |
| [26 — Aimbot and combo](docs/26-aimbot-combo.md) | Aim selection and coordinated casting |
| [27 — Subsystem relationships](docs/27-subsystem-relations.md) | Feature map and cross-module interactions |
| [28 — Initial runtime validation](docs/28-runtime-validation.md) | Injection and client-hook observations |
| [29 — UI geometry](docs/29-ui-layout-geometry.md) | Captured panel and control geometry |
| [30 — Runtime session log](docs/30-runtime-session-log.md) | Early client experiments, failures, and follow-up items |
| [31 — Gap resolutions](docs/31-gap-resolutions.md) | Specific state, command, and behavior corrections |
| [32 — Icons](docs/32-icons-tab.md) | Icon records, rendering, clicks, and script commands |
| [33 — In-game validation](docs/33-runtime-ingame-validation.md) | Live hooks, engine ticks, and player-state mirrors |
| [34 — Supporting feature tabs](docs/34-tabs-lists-extras-hud-spy-links.md) | Lists, Extras, HUD, Creature Spy, and Links |
| [35 — Runtime coverage matrix](docs/35-tab-runtime-matrix.md) | Feature-to-documentation and runtime-evidence mapping |
| [36 — Scheduling and flags](docs/36-scheduling-and-flags.md) | `auto` / `wait` scheduling and subsystem control state |
| [37 — USkin and support sections](docs/37-uskin-and-support-section.md) | Third-party exports, integration, and support-code provenance |
| [38 — End-to-end runtime](docs/38-runtime-e2e-genuine-client.md) | Stock loading chain, resolved loader failure, and live state checks |
| [39 — Module runtime report](docs/39-module-runtime-report.md) | Behavioral observations, shared coverage, and harness methods |

</details>

### Function and data references

The [master function index](docs/functions/index.md) links to the
[bot-code catalog](docs/functions/jdrv-catalog.md),
[support-code catalog](docs/functions/jiru-catalog.md),
[named highlights](docs/functions/named-index.md), and decompiled output.
The [CiroScript command table](docs/functions/ciroscript-commands.csv) provides a
machine-readable entry point into the interpreter surface.

Captured interface geometry is available as
[`ui/elfbot-ui-geometry.json`](ui/elfbot-ui-geometry.json), with context and
limitations in [doc 29](docs/29-ui-layout-geometry.md).

## Runtime evidence: what was actually tested

| Layer | Recorded evidence | Report |
| --- | --- | --- |
| Loading and initialization | Stock `loader.exe` loads the chain into a genuine client; the directory-related loader failure is resolved | [38 — End-to-end runtime](docs/38-runtime-e2e-genuine-client.md) |
| Hooks and state | Installed hook bytes match the recovered handlers; bot-side player state matches the live client | [33 — In-game validation](docs/33-runtime-ingame-validation.md) / [38](docs/38-runtime-e2e-genuine-client.md) |
| Behavioral sweep | Module logic exercised through controlled memory changes, direct dispatch, and observed state changes; some modules share evidence paths | [39 — Module runtime report](docs/39-module-runtime-report.md) |

A recorded **PASS** means the behavior described in that report was observed in
the local harness. It does not mean every user-interface path or every feature
combination was independently exercised end to end. For example, the NavNet test
captured a position packet at a dummy TCP peer, and some module results rely on
shared handlers. The reports preserve these distinctions.

## Repository layout and tools

```text
docs/               Numbered architecture, subsystem, and runtime reports
  functions/        Function catalogs, command tables, and decompiled references
samples/            Sample and asset layout used by the research
tools/              Reconnaissance, decoding, and documentation helpers
ui/                 Captured interface geometry
```

No setup is needed to read the documentation. Selected analysis helpers:

| Tool | Purpose |
| --- | --- |
| [`tools/pe_recon.py`](tools/pe_recon.py) | PE triage and binary structure |
| [`tools/strings_recon.py`](tools/strings_recon.py) | String reconnaissance |
| [`tools/decode_elfc.py`](tools/decode_elfc.py) | Decode the recovered `.elfc` / `.elft` representation |
| [`tools/re_mcp.py`](tools/re_mcp.py) | Client for a separately configured analysis gateway |
| [`tools/render_decompiled.py`](tools/render_decompiled.py) | Render recovered decompilation material |

The research combines local reconnaissance, IDA Pro / Hex-Rays analysis, offline
decompilation, and controlled runtime inspection. Analysis databases are not
committed, and remote helpers require your own lab and local configuration.

## Evidence and limitations

The documentation records an evolving investigation. Later reports resolve some
earlier hypotheses: in particular, the script-format findings in
[doc 22](docs/22-elfc-file-format.md) should not be confused with the separate
crypto / compression support-code analysis, and the loading results in
[doc 38](docs/38-runtime-e2e-genuine-client.md) supersede the earlier unresolved
loader failure.

Coverage includes structural labels for library code, not equally deep semantic
analysis of every recovered function. Optional work, including additional popup
geometry and selected rendering questions, is recorded in the
[status report](docs/00-status.md).

Addresses are hexadecimal **virtual addresses at the stated image base**, not
raw file offsets: typically `0x10000000` for `elfbot.dll` and `0x00400000` for the
executables. Runtime relocation requires rebasing. Recovered names are analysis
labels, not a claim to original vendor symbols, and findings apply to the analyzed
builds rather than every client or bot release.

## Contributing research

Support corrections with the exact binary / build, address, and relevant
instruction sequence, decompilation, or controlled runtime observation.
Distinguish observed behavior from inference and identify whether evidence comes
from an independent test or a shared subsystem path.

Documentation and commit messages use English, UTF-8, LF endings, and a final
newline. Do not include credentials, private lab endpoints, or unrelated personal
data in contributions.
