# AGENT-ARCHAEOLOGY — elfbot_re

Evidence base: **2 transcript projections, 0 null children**, plus the safe project-memory bundle. Projection 1 (earlier session) is large (~3171 lines / ~1.79 MiB) and was inspected at six stratified pages — findings from it are **sampled rather than exhaustive**. Projection 2 (14 lines / 3.6 KB) was read exhaustively to its `[END]` marker. Raw tool inputs/outputs were omitted from the projections and secret-like values appear as `[REDACTED:...]` markers; only the existence of redaction is noted here, never any value. Raw Claude stores, databases, `.git`, `.claude`, and credentials were unavailable by design and were not sought.

## What This Project Is

- Private research repo performing complete reverse engineering of **ElfBot NG 4.1.6** (per recovered memory; README shorthand conflates it with the target client version), a memory-injection bot for the genuine Tibia 8.60 game client.
- It contains no product source code — the deliverable is a documentation corpus: 40 numbered docs (`docs/00`–`docs/39`) plus `docs/functions/` catalogs covering **all 7,125 decompiled functions** across `elfbot.dll`, `loader.exe`, `elfload.dll`, `navserv.exe`, and `USkin.dll`.
- Analysis tooling lives in `tools/` (Python recon/decompile helpers such as `pe_recon.py`, `strings_recon.py`, `decode_elfc.py`, `re_mcp.py`, plus `wf_jdrv_docs.mjs`), driven through remote RE MCP servers (IDA, Ghidra, x64dbg, Frida, Cheat Engine, Wireshark, winctl, procmon, upload) configured in `.mcp.json`.
- `samples/` holds the analyzed binaries (`elfbot.dll` is Armadillo-packed with plaintext code; the rest unpacked) and data assets; `ui/elfbot-ui-geometry.json` captures live pixel geometry for 16 panels / 369 controls.
- Per `docs/00-status.md` the RE is declared finished — static decompilation, E2E injection proof (`docs/38`), and a per-module behavioral sweep driving every module to PASS (`docs/39`); complexity lives in the sheer size and cross-linking of the docs corpus, not in runnable code.

## Timeline of Agent Work

### Phase A — full ElfBot RE + in-game validation (projection 1, sampled at 6 strata)

User intent: document every ElfBot NG function and validate behavior against a real Tibia 8.6 client + local server, replicating the recipe from a sibling `magebot_re` effort. Session ended mid-debugging.

- Landed work named in conversation: `docs/26` (aimbot + combo sync), `docs/27` (all-tab relation graph), `docs/28`/`docs/30`/`docs/33` (runtime validation logs), `docs/35` (tab→doc→runtime matrix), `ui/elfbot-ui-geometry.json` (16 panels, 369 controls); IDA rename `computeBestAimSquareAndCast` at `0x1003ca03`; pushed `origin/main@7989789` (~49 commits, ~36 docs at that point).
- Decisions: the crypto/compression cluster judged a dead statically-linked library (zlib 1.2.3) off the script path — the real network cipher is the Tibia client XTEA at `0x549F60`; `.elfc`/`.elft` script files identified as plaintext opcode streams; Frida chosen over x64dbg on the shared Windows VM; test backend stood up as local Fir3element TFS 0.4 + SQLite god-character + RSA patch + hosts redirect; OTServ credentials were taken from a sibling session and deliberately kept out of the repo (redacted here as everywhere).
- Attempted → fixed during the session: SSH key setup (force-append); blind session-0 screen grab (schtasks forced session-1 + frida-read screenshots); connect-hook crash (`readByteArray` wrapped in try); Frida `-File` argument mangling (switched to `-EncodedCommand`); gateway 502/524 errors (backoff); a modded kizu-otc dat/spr replaced with the genuine `Tibia86.rar` asset.
- Attempted → still failing when the transcript cut off: live `loader.exe` injection failing with err 126; patched client failing the dat signature check ("Cannot open C:\Windows\system32\Tibia.dat", err 4); wizard popup geometry capture.

### Phase B — RE MCP suite status check (projection 2, read exhaustively)

Zero landed changes; purely an availability question ("ta com acesso a mcp de re?"). Suite found live: lumen (elfbot.dll index: 211 files / 23,660 chunks), frida (3 devices: local/socket/barebone), die (uploads empty), r2. Dormant until a target/session exists: ida-windows-re-lab, ghidra headless, x64dbg; support servers arkana, ce, procmon, wireshark, winctl, upload. Idle-state failures observed and expected, none fixed: ghidra probe `connected:false` (credentials unconfigured, localhost:13100 down), x64dbg "not connected", empty `list_scannable`. Session ended awaiting a target choice ("qual alvo?").

### Phase C — completion and merge (project memory; postdates both projections)

- Repo state: `origin/main` HEAD `10fc20e`, PR #1 squash-merged from branch `claude/frosty-cartwright-d1ffb9` consolidating 20 commits; working tree clean except untracked `.lumenignore`.
- Three-layer proof shipped: static decompilation (7,125 functions across every binary, docs 00–39) → full E2E injection (`docs/38`, stock `loader.exe` into a genuine RSA-patched 8.60 client on local Fir3element TFS 0.4, hooks byte-exact, shadow state equal to the live player) → per-module behavioral sweep (`docs/39`) with every module at PASS: Targeting, Lists, Creature Spy recolor, Healing cast, Attack/Aimbot emitter, Cavebot walk, NavNet opcode-2 packet, Looting, Alarm, Proxy LISTEN socket, Extras, Icons, USkin, CiroScript VM, Hotkeys.
- Corrections landed late: the arbiter hook `0x459F30` (→ `sub_1003D99F`) installed manually flipped three previously "blocked" subsystems (cavebot walk, targeting attack engagement, aimbot) to PASS — the minimal boot path omits it; the attack path re-documented as forced target `dword_100F9355` → resolver `sub_10023A45` → emitter `sub_1003A60A(rec_ptr, mode)` → sender `sub_1002ADE7` (11-byte attack / 15-byte spell packets, spells mana-gated ≥1200); loader err 126 root-caused to elfload's directory-relative LoadLibrary — fix was co-locating all four binaries (not madCodeHook-on-Win10); crypto verdict finalized (Blowfish/BWT/LZW stack = dead zlib 1.2.3 lib; `.elfc`/`.elft` are plaintext sparse-opcode streams, magic `0xFFFFFEA0`, recoverable via `tools/decode_elfc.py`).
- Eight generalized methodologies distilled into a global skill, `otserv-bot-re-harness` (7 references, ~956 lines). Closed out as "documentation review complete, ready for closure" with nothing pending.

## Hard-Won Gotchas

- Always rebasing addresses is mandatory: `E(off) = base + (off − 0x10000000)`; the dll base varies per boot (ASLR bases 0x82b0000 / 0x8460000 / 0x8660000 observed).
- Tick-thread affinity: real game mutations fire only from `botMainTickLoop 0x100227BD`; external `CreateRemoteThread` sets state variables but hangs on packet injection.
- 32/64-bit export RVA trap: resolve ws2_32/etc RVAs from the *target's own* PE export table via ReadProcessMemory — host-DLL RVAs are wrong addresses that look like hangs (this fixed NavNet).
- Frida cannot attach 32-bit WOW64 clients in this lab — attach `explorer.exe` and drive everything cross-process (WPM/CreateRemoteThread).
- NavNet send is gated on the connect handshake; sending before handshake silently does nothing.
- `g_100f0e20` is set nonzero inside `sub_10012edb` (nonliteral reference); `dontlist` maps to `2@g_100EE8B6`.
- Deposit FSM uses only states {0,2,3,5,7}; states 1/4/6 are absent from the binary.
- `Tibia.dat` is validated by a hardcoded signature CMP `0x4C8B0005` at `0x51DC74`; WOW64 System32→SysWOW64 redirection silently breaks file provisioning.
- The available `Tibia.exe` is a debug build (only build available, byte-identical ×4) that trips Debug Assertions on config dialogs/malformed chat; the engine must boot after world+creatures render (empty-world assert).
- Waypoint text format: one value per line, CR/LF delimited; the walker keeps its own position shadow `dword_1005F854/858/85C`, separate from the generic snapshot at `dword_10052768…`.
- Tooling ops: the ghidra server must be started manually before use (localhost:13100); x64dbg needs an explicit session before any tool call; litterbox rejects `.exe` uploads; parallel sessions ran on the shared VM (interference risk).

## Open Threads

- Wizard/editor popup geometry for 7 dialogs (TBOTDLG K/L/M/N/O/T/U) — the single remaining optional item. Their `RT_DIALOG` templates are an Armadillo-encrypted stub decrypted transiently at CreateDialog time; capture needs live GetWindowRect or a per-id CreateDialogParam harness without EcInit (EcInit crashes non-Tibia hosts because it installs 0x400000-based hooks).
- Hook `0x45ACD6` firing + shadow tables holding creatures: raised mid-debug right where projection 1 cut off; never revisited in the sampled strata nor in memory — status unknown.
- jiru/cdtemn artifact state unreconciled (see Contradictions); resolvable via `idb_list` on ida-windows-re-lab before trusting either side.
- Deposit FSM missing states 1/4/6: observed, never explained.
- Patched-client dat-sig failure (err 4): mechanism now understood (signature CMP above) but neither source records a fix or a successful patched-client boot.
- Dormant RE tooling (ghidra credentials unconfigured, x64dbg session-gated) spins up only once a new target is picked; the MCP-status session literally ended awaiting "qual alvo?".
- HUD renderer deep pass and reconciling the `SetFunctionAddresses` offset table with hardcoded hooks remain listed as optional follow-ups in `docs/00-status.md`.

## Recovered Memory

Source: safe bundle `/home/kizudev/.dsh/exp/memory-safe/elfbot_re` — `manifest.json` + `git-summary.txt` + 59 claude-mem summary entries; no `memory-*.md` files exist (`memoryFiles: []`); masks cover `.git` and `.claude`; redaction counts: 16 credential-label-value, 14 opaque-token, 1 long-hex.

- Project of record: RE of ElfBot NG 4.1.6 (`elfbot.dll` x86, `elfload.dll`, `loader.exe`, `USkin.dll`) against the genuine Tibia 8.60 client; findings live entirely as this docs-only repo.
- Status: complete and merged (details in Timeline Phase C); chronic but non-fatal blocker throughout was lab VM instability (502s, ~10-minute reboots, degradation after repeated injections) — the recipes outlived it.
- Hypotheses of record reversed during the work: the "dialog-owned config wall" and "attack unreachable" theories were wrong because the wrong globals were measured (cavebot/recolor side instead of the attack resolver).
- Assets: `ui/elfbot-ui-geometry.json` (16 panels, 369 controls) covers main-panel UI; function catalogs under `docs/functions/`; tooling under `tools/`; binaries in `samples/`.
- Next steps recorded: none pending; any new work starts from `docs/39` plus the `otserv-bot-re-harness` skill.
- Current-state rules check (this audit): repo root has no `CLAUDE.md`/`AGENTS.md`, so only the sanitized global rules apply; `.editorconfig` and `.gitattributes` exist as the infra rules require; no CI configuration and no build system exist (nothing to build). No rule violations with hard evidence were found; the only gap is the missing repo-level CLAUDE.md documenting workflow conventions (the docs themselves encode them instead).

## Contradictions

- **jiru state**: projection 1 marks jiru/cdtemn label-only/unfinished; projection 2's lumen catalog already lists `.jiru`/`.jdrv`, implying a populated IDB on ida-windows-re-lab. Unresolved — verify with `idb_list` before trusting either side.
- **Repo head/doc count**: projection 1 pushed `origin/main@7989789` (~49 commits, ~36 docs); memory records HEAD `10fc20e` as a squash-merged PR (#1) consolidating 20 commits with docs 00–39 (40 docs). Memory postdates the transcript and reflects the merge, so treat memory as current.
- **Version naming**: projection 1 shorthand "elfbot ng 8.60" conflates bot and client versions; memory pins **ElfBot NG 4.1.6** against the Tibia 8.60 client. The README carries the same conflation.
- **Frida attachment style**: projection 1 used Frida directly on the shared Windows VM; memory records Frida unable to attach 32-bit WOW64 clients, everything driven cross-process via explorer.exe. Different environments/approaches — do not assume direct attach works where it was not proven.
- **Tool inventory drift**: memory lists `tools/angr_decompile.py` among project assets, but the current `tools/` directory contains `decode_elfc.py`, `extract_engine.py`, `fn_inventory.py`, `merge_jdrv_purposes.py`, `pe_recon.py`, `re_mcp.py`, `render_decompiled.py`, `strings_recon.py`, `wf_jdrv_docs.mjs` — no `angr_decompile.py`. Either renamed/removed after the memory entry or living outside the repo; unverified from sanitized sources.
- **Resolved reversals (kept for the record)**: loader err 126 went from open failure (projection 1) to root-caused fix (memory); "attack unreachable"/"config wall" hypotheses were reversed by the documented resolver path. USkin "per-function docs" stayed open in projection 1 while memory shows only module-level PASS in `docs/39` — per-function USkin coverage is unconfirmed, not a blocker.
