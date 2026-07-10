# elfbot.dll — master function index

Every function in `elfbot.dll` is decompiled and documented. Coverage:

| Section | Functions | Documented |
|---|---|---|
| `.jdrv` (bot code) | 1190 | name + purpose each — [jdrv-catalog.md](jdrv-catalog.md) |
| `.jiru`/`.cdtemn` (support) | 5935 | 299 dispatchers described + rest labelled — [jiru-catalog.md](jiru-catalog.md) |
| **total** | **7125** | pseudo-C for all in [decompiled/](decompiled/jdrv-index.md) |

## Where to look

- **What a function does** → [jdrv-catalog.md](jdrv-catalog.md) (bot logic, 1190
  funcs) / [jiru-catalog.md](jiru-catalog.md) (support, 5935 funcs).
- **Its decompiled C** → [decompiled/jdrv-index.md](decompiled/jdrv-index.md) /
  [decompiled/jiru-index.md](decompiled/jiru-index.md).
- **Named highlights** → [named-index.md](named-index.md) (454 core/dialog/hook/cmd).
- **CiroScript commands** → [ciroscript-commands.csv](ciroscript-commands.csv) +
  [doc 11](../11-ciroscript-engine.md).

## Subsystem map (bot logic)

| Subsystem | Doc | Key functions |
|---|---|---|
| Init / UI framework | [05](../05-ui-init-framework.md) | EcInit, registerDialogs, 23 dlgProc_* |
| Injection chain | [06](../06-injection-chain.md) | elfload mapBotAndRun, loader madCodeHook |
| Client hooks | [08](../08-client-hooks-engine.md) | installClientHooks_proxyServer, hook_incomingPacketParser, full-light |
| Packet proxy / NavNet | [09](../09-packet-proxy.md) | proxyClientThread, buildFullGameStateSnapshot, packet encoders |
| CiroScript engine | [11](../11-ciroscript-engine.md) | registerCommand + 422 cmd_* handlers |
| Script crypto/compression | [12](../12-script-crypto-compression.md) | Blowfish, BWT, LZW, block ciphers |
| Feature dialogs | [10](../10-feature-subsystems.md) | AutoAim/Targeting/Cavebot/Healer/Hotkeys/HUD/Skin |
