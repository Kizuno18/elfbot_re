# elfbot.dll — full function catalog

**Every function in `elfbot.dll` is decompiled to pseudo-C** (angr, offline).
7125 functions across the code sections, 0 decompile failures.

## Decompiled C (the deep layer)

- **[decompiled/jdrv-index.md](decompiled/jdrv-index.md)** — 1190 functions of
  the `.jdrv` section: **ElfBot's own logic**. 20 files, each function with its
  full pseudo-C + an auto-summary of the APIs/strings it touches. **454 are
  named by semantics** (see [named-index.md](named-index.md)) — the 422
  CiroScript command handlers (`cmd_*`), the 23 feature dialog procs
  (`dlgProc_*`), the hook/proxy engine, and the init core.
- **[decompiled/jiru-index.md](decompiled/jiru-index.md)** — 5935 functions of
  `.jiru`/`.cdtemn`: the MSVC STL + Boost template instantiations, the C runtime,
  and feature dispatchers. 99 files of pseudo-C. Mostly library support; the
  bot-relevant dispatchers are the larger ones with WinAPI/socket calls.
- `jdrv.jsonl` / `jiru.jsonl` — machine-readable: one function per line with its
  pseudo-C, resolved API calls, and string refs.

## Named index & command map

- **[named-index.md](named-index.md)** — the 454 semantically-named `.jdrv`
  functions, grouped (core / hooks-proxy / dialogs / CiroScript commands).
- **ciroscript-commands.csv** — canonical `command → handler-address` map for all
  422 CiroScript commands (see [../11-ciroscript-engine.md](../11-ciroscript-engine.md)).

## Structural inventory (cross-check)

- **[catalog-core.md](catalog-core.md)** / **[catalog-support.md](catalog-support.md)**
  / `inventory.json` — a second, independent recovery (capstone byte-scan) giving
  per-function section, size, API calls and category. Used to verify coverage and
  classify library vs bot code.

## How it was produced

- `tools/angr_decompile.py` — angr `CFGFast` per code region + Hex-Rays-style
  decompiler, one pseudo-C blob per function, written to JSONL.
- `tools/render_decompiled.py` — JSONL → grouped markdown, merging the named set
  and the CiroScript command handlers.
- `tools/fn_inventory.py` — the independent capstone structural inventory.

Fully offline (no IDA/Ghidra service required). The prose subsystem docs
(04–11) give the architecture and the meaning; this directory is the exhaustive
per-function evidence — every function, dismantled.
