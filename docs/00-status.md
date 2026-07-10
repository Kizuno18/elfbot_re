# Status & roadmap

Resume point for the ElfBot NG 8.60 RE. What is done, what is in progress.

## Done

- **Recon & tooling** — all 6 PE binaries triaged (`tools/pe_recon.py`,
  `tools/strings_recon.py`); IDA (idalib) headless over MCP; binaries delivered
  to the analysis VM out-of-band (HTTP), never through context.
- **Packer** — `elfbot.dll` is Armadillo but the code is plaintext; static RE is
  viable, no runtime unpack ([03](03-packer-armadillo.md)).
- **navserv.exe** — 100% documented, all 12 functions + NavNet wire protocol
  ([04](04-navnet-server.md)).
- **Init / UI framework** — boot path, `EcInit`, 23-dialog registration
  ([05](05-ui-init-framework.md)).
- **Injection chain** — loader.exe (madCodeHook) → elfload.dll → EcInit
  ([06](06-injection-chain.md)).
- **CiroScript** — command + conditional vocabulary, `.elfc`/`.elft` format
  ([07](07-ciroscript-language.md)).
- **Client hook engine** — inline hooks at Tibia 8.60 hardcoded addresses,
  packet-parser hook, full-light hack, shadow tables ([08](08-client-hooks-engine.md)).
- **Packet proxy** — embedded server, proxy protocol, injection primitive
  ([09](09-packet-proxy.md)).
- **Feature subsystems** — all 23 `TBOTDLG*` procs mapped + named
  ([10](10-feature-subsystems.md)).

## In progress

- **Full function catalog** — classify + name + one-line every one of the 3471
  `elfbot.dll` functions, IDA-driven, in throttled workflow chunks; output to
  `docs/functions/` and names persisted into the IDA db. ~half are Boost/MSVC
  STL/CRT library templates (labelled in bulk), ~half are bot logic (described).

## TODO (deep passes)

- Per-subsystem engine deep-dives: cavebot walker, targeting evaluator, healer,
  hotkey/CiroScript interpreter, HUD renderer, NavNet client encode/decode.
- `.elfc` / `.elft` byte-level format (from the cavebot/targeting loaders).
- `elfload.dll` + `loader.exe` per-function RE (bootstrap + madCodeHook site).
- Reconcile the `SetFunctionAddresses` offset table with the hardcoded hooks.

## Conventions

Addresses are file-absolute (imagebase `0x10000000` for `elfbot.dll`,
`0x400000` for EXEs). Function names in docs match the IDA database. Analysis
persisted to `elfbot.dll.i64` / `navserv.exe.i64` on the VM (not committed).
