# Hotkey engine, alarms & sound

Two runtime systems that sit beside the combat engines: the **hotkey/label
engine** (`processHotkeyScriptEngine`) that turns key presses and script labels
into CiroScript command execution, and the **alarm + DirectSound** system that
reacts to danger events (player-on-screen, GM detected) with sound, a popup, a
frozen status packet, or an outright disconnect.

## Hotkey / label engine — `processHotkeyScriptEngine` (`0x1002b09e`, 2979 B)

The largest single non-dialog function in `.jdrv`. Once per relevant tick it:

1. Walks the **key table** and **label table** (the hotkey rows configured in the
   Hotkeys dialog and the `[CavebotHotkeys]` script section, accumulated by
   `appendCavebotHotkeyLine` `0x10017289` into `g_101F2EA8`).
2. For each key row, tests the trigger with `GetAsyncKeyState` and a per-row
   cooldown; global hotkeys (window-level) are registered/unregistered as a block
   by `toggleGlobalHotkeys` (`0x1002B02B`, `RegisterHotKey` ids **166–183 + 218**
   on `g_1005F626`).
3. Expands the row's `{}`/`//`-delimited script text through the CiroScript
   command table (`registerCommands_table`, `0x10030442`) — i.e. a hotkey body is
   a CiroScript snippet ([`11`](11-ciroscript-engine.md)).
4. Dispatches each command inside an SEH frame; faults are caught by
   `hotkeyProcExceptionHandler` (`0x10002509`), which logs `"HkeyProc Error … on
   hotkey: <text>"` and, on a stack-overflow (`0xC00000FD`), exits the thread
   rather than corrupting state. Sibling handlers cover the send path
   (`sendProcExceptionHandler`) and action dispatch (`reportActionProcError`).

Related helpers: `buildSpellFromRuneId` (`0x10021C2D`) maps a rune/spell id to its
Tibia spell string (`exori vis`/`exori mort`/…) or rune constant when a hotkey
casts; `previewHotkeyCommandTemplate` / `formatHotkeyParamPrompt` /
`advanceHotkeyParamPrompt` build the parameterised-command UI (placeholders
`{creature}`/`{hp%}`/`{num}`/`{window}` decoded from 4 param nibbles).

The window-message side is hooked by `hookWndProcMouseKeyboard` (`0x10029D4E`,
installed at client `0x5B8428`): it intercepts key/mouse messages, can suppress
hotkeys, and implements the HUD drag + right-click-walk using the map rect
`g_10080B84`.

## Alarm system — `handleAlarmTriggers` (`0x10009489`)

Alarms are a table of **3-byte flag rows** at `g_10207F12` (one row per alarm
type). `parseAlertLine` (`0x10017106`) fills them from the `[Alerts]` script
section, mapping names (`PlayerOnScreen`, `GmDetected`, `PrivateMessage`, …) to a
row and setting the per-action bits from the value. Each tick the handler walks
the rows and, per row byte:

| Byte | Bit set → action |
|---|---|
| `[0]` | **sound**: play DirectSound buffer `g_10052660[idx]`; raise the on-screen flag `g_100580F8` |
| `[1]` | **freeze/notify**: `MEMORY[0x63FEDC] = 0`, inject a status packet via `injectIncomingPacket` (`0x1002ADE7`), raise `g_100580FC` |
| `[2]` | **disconnect**: `shutdown(g_100428D5, SD_BOTH)` — drop the proxy socket (auto-logout on the trigger) |

`handleAlarmTriggersOld` (`0x100093A3`) is the earlier variant. `flashMainWindow`
(`0x10009452`) additionally `FlashWindowEx`-flashes the window for a visual alert.
So a single `GmDetected` alarm can simultaneously beep, pop the on-screen banner,
inject a freeze, flash the window, and **disconnect the client** — the RE point
being that the disconnect is driven from inside the bot, on the proxy socket.

## DirectSound backend

| Function | Addr | Role |
|---|---|---|
| `createDsoundPrimaryBuffer` | `0x1000904C` | `DirectSoundCreate` + cooperative level + primary buffer `WAVEFORMATEX` |
| `loadWavIntoDsoundBuffer` | `0x10008E41` | `mmioOpenA` a WAV, parse RIFF/fmt/data, fill a secondary buffer |
| `getOrLoadNamedSound` | `0x1000954E` | look up `sounds\<name>` in the `g_10287F44` cache (`lstrcmpi`), lazy-load + play once |
| `playSoundBufferLooping` | `0x1000936F` | reset position + play looping if enabled |
| `releaseAllSoundBuffers` | `0x10009142` | release + null the ten buffer/device globals `g_10052658…g_1005267C` on shutdown |

The ten `g_10052658…7C` slots are the fixed alarm sound buffers (Low Health,
Disconnected, etc.); `g_10287F44` is the named-sound cache for script-triggered
`playsound` commands.

## Friends / enemies

Small classification layer feeding targeting: `cmd_isfriend` (`0x1002E815`),
`cmd_isenemy` (`0x1002E7B4`), `cmd_friendcount` (`0x1002DBC8`), `cmd_enemycount`
(`0x1002DB6E`) test a creature name against the Friends/Enemies lists configured
in `dlgProc_FriendsEnemies`. Targeting uses these to avoid attacking friends and
to prioritise/alarm on enemies.

## Detection notes

- `RegisterHotKey` for ids 166–183+218 on a hidden window is a hotkey-engine
  fingerprint.
- `GetAsyncKeyState` polled from a bot thread while a `TibiaClient` window is
  present.
- The alarm disconnect path calls `shutdown()` on the proxy socket — an
  abnormal, bot-driven client disconnect correlated with an on-screen event.
- WAV files under a `sounds\` directory (Low Health / Disconnected / Walker
  Stuck / Creature Detected) loaded via `mmioOpenA` + DirectSound.
