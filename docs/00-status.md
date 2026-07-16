# Status & roadmap

Resume point for the ElfBot NG 8.60 RE. What is done, what is in progress.

## Complete

RE is finished. Every function of every binary is decompiled and carries a
purpose (0 blanks: jdrv 1190, jiru 5935, loader 1780, elfload 6, navserv 12).
All 23 tabs are mapped to a named engine + deep doc, and every inter-tab relation
is documented ([27](27-subsystem-relations.md), [25](25-cavebot-targeting-sync.md),
[26](26-aimbot-combo.md)). The crypto/compression cluster is resolved as **unused
statically-linked library code** (zlib 1.2.3 + archive lib; no path to bot logic
even via pointer dispatch — [12](12-script-crypto-compression.md)); the real
network cipher is the Tibia client's XTEA at `0x549F60` and `.elfc`/`.elft` are
plaintext opcode streams ([22](22-elfc-file-format.md)). IDA `.i64` fully named
and saved. 38 docs (00–37).

The static side is complete, including the previously-deferred third-party surface:
`USkin.dll`'s 41 exports + the elfload load/`Init`/neutered-`Exit` contract, and the
`.jiru`/`.cdtemn` support-section provenance, are documented in
[37](37-uskin-and-support-section.md); the last byte-exact micro-gaps (`auto`/`wait`
scheduler arrays, the `settargeting`/`setcavebot`/target-ptr flag literals) are
pinned in [36](36-scheduling-and-flags.md). The `loader.exe` `err=126` injection
failure is root-caused at the RE level (the elfload directory-relative
`elfbot`/`USkin` load + madCodeHook-on-Win10, [06](06-injection-chain.md)); the
docs/33 direct-`LoadLibrary` path is the proven substitute.

What remains is purely **live-target** work, and it is gated on the runtime stack —
which was wiped when the lab VM was re-imaged (the docs/33 TFS 0.4 8.60 server +
RSA-patched 8.60 client are no longer resident, and the Tibia client is not
reproducible from this repo): per-tab **behavioural** scenarios (a creature to
attack/loot, a route to walk), the seven wizard/editor popups' exact geometry (their
`RT_DIALOG` templates are Armadillo-encrypted — capturable only from the bot mapped +
unpacked in a live client, [35](35-tab-runtime-matrix.md)), and the live `loader.exe`
re-run. The engine itself was already proven live in-game in a prior session
([33](33-runtime-ingame-validation.md)).

## Done (detail)

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

- **Names applied to the IDB** — the full `.jdrv` catalog is now written into
  `elfbot.dll.i64` on the VM: **893 functions named + 1188 purpose comments**
  (was 454 offline), plus 51 from the engine deep-dives. Saved; Hex-Rays reads
  with real names throughout.
- **Engine deep-dives (all runtime flows traced)** — from the named Hex-Rays:
  master tick loop ([13](13-engine-tick-loop.md)), CiroScript runtime
  ([14](14-ciroscript-runtime.md)), healer ([15](15-healer-engine.md)), targeting
  ([16](16-targeting-engine.md)), cavebot walker/pathfinder
  ([17](17-cavebot-walker.md)) + waypoint format ([19](19-cavebot-waypoints.md)),
  NavNet codec ([18](18-navnet-codec.md)), client hooks deep
  ([20](20-client-hooks-deep.md)), player-state/exp ([21](21-player-state.md)),
  looting ([23](23-looting-engine.md)), hotkeys/alarms/sound
  ([24](24-hotkeys-alarms.md)).
- **`.elfc`/`.elft` byte format cracked** — the compiled files are **not
  encrypted**: a sparse-opcode table encoding (magic `0xFFFFFEA0`). Decoder
  `tools/decode_elfc.py` recovers the 283 KB waypoint + 41 KB targeting tables
  from real samples ([22](22-elfc-file-format.md)). Refines [12](12-script-crypto-compression.md)
  (that crypto cluster is a separate, unused-for-these-files path).

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

- HUD renderer deep pass (the on-screen draw callbacks; partially covered in
  [20](20-client-hooks-deep.md) / [21](21-player-state.md)).
- Reconcile the `SetFunctionAddresses` offset table with the hardcoded hooks.
- The `.jiru`/`.cdtemn` support section stays catalogued (5935 funcs) with its
  provenance now written up ([37](37-uskin-and-support-section.md)); the stock MSVC
  STL/Boost/CRT glue is identified, not individually deep-documented (outside
  bot-logic scope — the only bot-relevant part, the crypto/compression subsystem, is
  in [12](12-script-crypto-compression.md)).

## Conventions

Addresses are file-absolute (imagebase `0x10000000` for `elfbot.dll`,
`0x400000` for EXEs). Function names in docs match the IDA database. Analysis
persisted to `elfbot.dll.i64` / `navserv.exe.i64` on the VM (not committed).
