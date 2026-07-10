# elfbot.dll — full function catalog

Per-function inventory of all recovered `elfbot.dll` functions. Two tiers:

- **[catalog-core.md](catalog-core.md)** — the `.jdrv` section (498 functions,
  362 non-thunk): **ElfBot's own logic**. Each row lists the function address,
  size, the Win32 APIs it calls (resolved through the IAT), and notable string
  literals it references.
- **[catalog-support.md](catalog-support.md)** — the `.jiru`/`.cdtemn` sections
  (2488 functions): overwhelmingly **MSVC STL + Boost template instantiations and
  the C runtime**, plus a few feature dispatchers. Bulk-classified; the
  bot-relevant dispatchers are surfaced separately.
- `inventory.json` — machine-readable dump of every function (address, size,
  section, category, APIs, strings, callee count).

## How it was produced

`tools/fn_inventory.py` (capstone + pefile, fully offline). It byte-scans the
code sections for `E8` call targets and `FF25` import thunks to recover function
starts, walks each function's extent, and resolves API calls and string
references. Recovered **2987 / 3471** functions (~86%); the remainder are
functions only reached via jump tables / vtables that a linear+call-target
sweep misses.

## Fidelity caveat

This offline catalog is a **structural** inventory — it tells you *what each
function touches* (which APIs, which strings), not a decompiled semantic
description. The high-fidelity, purpose-level documentation comes from the IDA
Hex-Rays pass (docs 04–10 already cover navserv 100%, the hook engine, the
packet proxy, and all 23 feature dialogs by name). The remaining `.jdrv`
functions get named + described in the IDA catalog pass; this file is the
worklist and the coverage guarantee that no function is unaccounted for.

## Category counts

| Category | Count | Meaning |
|---|---|---|
| bot (`.jdrv`) | ~362 | ElfBot logic — deep-doc target |
| support (`.jiru`) | ~2476 | STL / Boost / CRT templates |
| thunk | 136 | single-jump import wrappers |
| library | 11 | STL/Boost identified by RTTI strings |

## Cross-reference

Functions already named + deeply documented (see docs 05–10) also appear here by
address. The named set so far: `EcInit`, `DllEntryPoint`, `registerDialogs`,
`postBotMessage`, the 23 `dlgProc_*`, `installClientHooks_proxyServer`,
`hook_incomingPacketParser`, `hook_captureRenderCtx`, `hook_fullLightDetour`,
`installLightHook`, `proxyClientThread`, plus the full navserv set.
