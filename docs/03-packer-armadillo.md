# The Armadillo protection on elfbot.dll

`elfbot.dll` was processed with **Armadillo** (Silicon Realms Toolworks). The
tells:

- A `.Geddon` section — Armadillo's signature marker (from "armaGEDDON").
- Randomized 4–7 char section names (`.jdrv`, `.ukjo`, `.aqfu`, …).
- Linker version zeroed to `0.0`.
- A single high-entropy section `.aqfu` (7.78) that is *not* the code.
- A leftover path string in the image:
  `…\CRACKING\ArmaG3ddon_v1.9\dll loader.exe`. **ArmaG3ddon** is a well-known
  Armadillo unpacker/loader toolkit — its presence indicates this DLL was run
  through an Armadillo *unwrap* step and rebuilt, which is why the code is
  readable on disk.

## Why static RE works anyway

Normally Armadillo with CopyMem-II keeps code pages encrypted and decrypts them
on demand, defeating a static dump. That is **not** the case here:

- IDA auto-analysis recovers **3471 functions** across `.jdrv` / `.jiru` /
  `.cdtemn`, all with coherent control flow.
- The import table (`.idata` inside `.slau`) is fully intact and resolved —
  every WinAPI call decodes to a named thunk.
- Strings are plaintext (`TibiaClient`, `GlobalSettings`, script paths, spell
  words, sound filenames).
- `EcInit`, `DllEntryPoint` and the worker thread decompile cleanly to sensible
  C on the first pass.

The `.ukjo` section (2.75 MB, entropy 0.35) is zero-filled — it is the
`.bss`-like runtime arena the bot allocates into, not packed code. The one
genuinely encrypted region is `.aqfu` (0xB0000, entropy 7.78); it carries no
xrefs from the recovered code and is treated as Armadillo-owned metadata /
a compressed backup, not part of the bot's logic. It is left unanalyzed.

**Conclusion:** no runtime unpacking, memory dump, or live Tibia process is
required. The entire bot is reverse-engineered statically from the on-disk
image. This is the reason this project is a pure static-analysis effort rather
than the runtime-dump approach used for VMProtect/Themida-class targets.

## Transfer / tooling note

The binary is analyzed in a headless IDA (idalib) worker reached over MCP. The
sample is delivered to that worker out-of-band (HTTP fetch) rather than through
the model context, so the 4.6 MB image never transits a prompt. See
`tools/` for the local `pefile` recon scripts.
