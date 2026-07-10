# All tabs & all their relations

The complete map: every one of the 23 feature tabs, the engine it drives, and how
it interacts with the others. Coordination is always the same shape — one bot
tick ([13](13-engine-tick-loop.md)) fires each engine in a fixed order, and they
share state through global flags and the shadow tables, never by calling each
other directly (except through the CiroScript command layer).

## Per-tab completeness

| Tab (resource) | WndProc | Engine / handler | Deep doc |
|---|---|---|---|
| AutoAim (TBOTDLG7) | `dlgProc_AutoAim` | `computeBestAimSquareAndCast 0x1003CA03` | [26](26-aimbot-combo.md) |
| AutoAim combo (TBOTDLGI) | `dlgProc_AutoAimCombo` | combo sync over NavNet | [26](26-aimbot-combo.md) |
| Targeting (TBOTDLGR) | `dlgProc_Targeting` | `targetingAttackScanTick`, `pickAttackTarget` | [16](16-targeting-engine.md) |
| Targeting editor (TBOTDLGT) | `dlgProc_TargetingEditor` | per-record editor | [16](16-targeting-engine.md) |
| Friends/Enemies (TBOTDLGH) | `dlgProc_FriendsEnemies` | classification lists → `g_1014F41E/1F` | [16](16-targeting-engine.md), [26](26-aimbot-combo.md) |
| Cavebot (TBOTDLGS) | `dlgProc_Cavebot` | walker + waypoint list | [17](17-cavebot-walker.md), [19](19-cavebot-waypoints.md) |
| Healer (TBOTDLGE) | `dlgProc_Healer` | `healerManaSpellTick`, `runAttackHealerLogic` | [15](15-healer-engine.md) |
| Hotkeys (TBOTDLGD) | `dlgProc_Hotkeys` | 96×514 hotkey table + tick | [24](24-hotkeys-alarms.md) |
| Shortkeys (TBOTDLGP) | `dlgProc_Shortkeys` | text-triggered commands | [24](24-hotkeys-alarms.md) |
| Hotkey wizards (TBOTDLGK/M/O) | `dlgProc_HotkeyActionPicker` / `CommandParamPicker` / `CommandBuilder` | CiroScript command assembler | [10](10-feature-subsystems.md), [11](11-ciroscript-engine.md) |
| Command tools (TBOTDLGL/N) | `dlgProc_CommandPicker` / `CommandParamBuilder` | command/item composer | [10](10-feature-subsystems.md) |
| Script editor (TBOTDLGU) | `dlgProc_ScriptEditor` | 4-mode text editor | [10](10-feature-subsystems.md), [14](14-ciroscript-runtime.md) |
| HUD creature list (TBOTDLGA) | `dlgProc_HudCreatureList` | battle-list readout | [21](21-player-state.md) |
| On-screen info (TBOTDLGJ) | `dlgProc_HudOnScreenInfo` | HUD overlays (MP est., timers, DPS) | [21](21-player-state.md) |
| Graphics tweaks (TBOTDLGF) | `dlgProc_GraphicsTweaks` | FPS/light tweaks (full-light hook) | [08](08-client-hooks-engine.md), [20](20-client-hooks-deep.md) |
| NavNet (TBOTDLGC) | `dlgProc_NavNet` | NavNet client codec | [18](18-navnet-codec.md), [04](04-navnet-server.md) |
| Links (TBOTDLGB) | `dlgProc_LinksNavNet` | local link server (patches client) | [09](09-packet-proxy.md) |
| Links proxy (TBOTDLGQ) | `dlgProc_LinksProxy` | proxy/link socket | [09](09-packet-proxy.md) |
| Looting | (waypoint-driven) | corpse scan, container/depot SM | [23](23-looting-engine.md) |
| Skin (TBOTDLGV/W) | `dlgProc_Skin` / `dlgProc_SkinEditor` | USkin theming | [05](05-ui-init-framework.md), [10](10-feature-subsystems.md) |

Every command handler behind these tabs (422 `cmd_*`) and every engine function
is in the [function catalog](functions/jdrv-catalog.md); the CiroScript verbs are
in [11](11-ciroscript-engine.md).

## The relation graph

```
                 Hotkeys / Shortkeys / auto ─────────────┐  (bind/fire any command)
                          │                               │
   Friends/Enemies ──classify(g_1014F41E/1F)──► AutoAim ──┤
        │                                         │       │
        │                                         ▼       ▼
        └──► Targeting ──g_100f0e20──► Cavebot ── CiroScript tick ── Healer
                 │  (active target)      │  walker           │
                 │                       │                   ├─ offensive cast
                 ▼                       ▼                   │   (uses target)
             Battle-list          Looting ◄──kill──┐         │
             shadow table         (corpse scan)    │         ▼
                 ▲                       │          │     player-state
                 │                       ▼          │     snapshot / HUD
          packet hook ──► shadow tables (creatures/channels/map)
                 │                                  ▲
                 ▼                                  │
          NavNet / proxy ──positions/combo──► Combo sync ─┘
```

## Every relation, explicitly

- **Hotkeys / Shortkeys / `auto` → all engines.** Hotkeys bind any CiroScript
  command; `auto N` fires a command block every N ms. This is how every feature
  is triggered ([24](24-hotkeys-alarms.md), [11](11-ciroscript-engine.md)).
- **Friends/Enemies → Targeting & AutoAim.** The name lists set the live
  friend/enemy flags (`g_1014F41E/1F`) that Targeting uses to decide *whom* to
  attack and AutoAim uses to guarantee *zero friends* in an area cast
  ([26](26-aimbot-combo.md)).
- **Targeting ↔ Cavebot.** The tick arbiter `cavebotTargetingStep 0x1003D99F`
  runs targeting first, publishes "engaged" in `g_100F0E20`, then the walker
  runs; the cavebot script gates walking with `istargeting`/`isnottargeting`
  ([25](25-cavebot-targeting-sync.md)).
- **Targeting → AutoAim.** They share the current-target pointers
  (`g_10080BCB`/`g_10080BB3`); `sd`/`autoaim` fall back to the active target.
- **Cavebot → Looting.** After a kill the cavebot script (or targeting's
  looting flag) invokes the loot commands; the looter scans the corpse container
  and moves items ([23](23-looting-engine.md)).
- **Cavebot → Refiller / trade.** Refill commands (`refillmana`/`refillhealth`/
  `refillammo`) and NPC trade (`buyitems`/`sellitems`/`settradeoptions`) run from
  cavebot waypoints (go-to-city loops) as ordinary CiroScript.
- **Healer → target (offensive).** Healer runs first each tick on HP/MP
  thresholds; its offensive branch (`runAttackHealerLogic`) casts on the current
  target, so it rides `g_100F0E20` too ([15](15-healer-engine.md)).
- **Packet hook → everything.** The incoming-packet hook maintains the shadow
  creature/channel/map tables all engines read ([08](08-client-hooks-engine.md));
  no engine issues its own reads for that data.
- **NavNet ↔ HUD ↔ Combo.** NavNet positions feed the HUD/minimap dots and the
  combo sync (leader's position/`navsay` triggers followers' synchronized SD)
  ([18](18-navnet-codec.md), [26](26-aimbot-combo.md)).
- **Graphics tweaks → client hooks.** The FPS/full-light options toggle the
  inline client hooks ([08](08-client-hooks-engine.md), [20](20-client-hooks-deep.md)).
- **All state ← client hooks + player-state snapshot.** Every tick begins by
  snapshotting HP/MP/pos/skills from client memory ([21](21-player-state.md)),
  which every engine then reads.

Nothing is missing from the tab set: all 23 dialogs are mapped, each to a named
engine and a deep doc, and every pairwise interaction above is grounded in the
shared globals / shadow tables named in those docs.
