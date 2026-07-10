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

- **Full decompilation** — **every** `elfbot.dll` function decompiled to pseudo-C
  (angr, offline): 1190 `.jdrv` (bot code) + 5935 `.jiru`/`.cdtemn` (STL/Boost/
  support) = **7125 functions, 0 failures**. In `docs/functions/decompiled/`.
- **CiroScript engine** — 422 commands mapped to their handler functions +
  3-table perfect-hash dispatch mechanism ([11](11-ciroscript-engine.md)).
- **Named set** — 454 `.jdrv` functions named by semantics
  (`docs/functions/named-index.md`).
- **elfload.dll** — all 6 real functions decompiled ([06](06-injection-chain.md)).

- **Every function documented** — `.jdrv` 1190 funcs name+purpose
  ([functions/jdrv-catalog.md](functions/jdrv-catalog.md)); `.jiru`/`.cdtemn`
  5935 funcs (299 dispatchers described + rest labelled,
  [functions/jiru-catalog.md](functions/jiru-catalog.md)). Master index:
  [functions/index.md](functions/index.md).
- **Script crypto/compression** — the `.elfc`/`.elft` protection stack
  (Blowfish, BWT, LZW, custom block ciphers) mapped ([12](12-script-crypto-compression.md)).

- **loader.exe** — all 1780 functions decompiled + purpose; the madCodeHook
  injection internals (trampoline, remote-thread, shared-mem IPC) reversed
  ([06](06-injection-chain.md), [functions/loader-catalog.md](functions/loader-catalog.md)).

## Coverage: complete

Every function in every binary is decompiled to pseudo-C **and** has a purpose:

| Binary | Functions | Coverage |
|---|---|---|
| elfbot.dll `.jdrv` | 1190 | name + purpose (454 semantic, rest described) |
| elfbot.dll `.jiru`/`.cdtemn` | 5935 | 304 dispatchers described, 5631 structural |
| loader.exe | 1780 | 68 injection described, rest structural |
| elfload.dll | 6 | 100% |
| navserv.exe | 12 | 100% |

## Optional follow-ups

- Bulk-import the full 1158-name map (`ciroscript-commands.csv` + catalogs) into
  the IDA db via a script (the 37 core names are already applied + saved).
- `.elfc`/`.elft` exact byte layout: run a sample through the mapped
  decrypt/decompress functions ([12](12-script-crypto-compression.md)).
- Reconcile the `SetFunctionAddresses` offset table with the hardcoded hooks.

## Conventions

Addresses are file-absolute (imagebase `0x10000000` for `elfbot.dll`,
`0x400000` for EXEs). Function names in docs match the IDA database. Analysis
persisted to `elfbot.dll.i64` / `navserv.exe.i64` on the VM (not committed).
