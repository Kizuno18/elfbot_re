# elfbot.dll `.jdrv` — complete function catalog

All 1190 functions of the bot's own code section, each with name + purpose. Decompiled C in [decompiled/](decompiled/jdrv-index.md). Names: `cmd_*` = CiroScript handlers (doc 11), `dlgProc_*` = feature dialogs (doc 10), hooks/proxy (docs 08/09), the rest described from their pseudo-C.

| Address | Name | Size | Purpose |
|---|---|---|---|
| `0x10001000` | `startNavServerThread` | 54 | Stores config arg in g_10042000 and, if mode==1, spawns the NavNet server worker thread sub_10002041 via CreateThread. |
| `0x10001036` | `debugFormatCreatureRecord` | 33 | Formats a record via sub_10040940 into a 32-byte buffer and emits it with OutputDebugStringA (debug logging helper). |
| `0x10001057` | `packetOpcodeHasCoordFlag` | 52 | Tests bit 0x08 of a per-map-tile record byte (76-byte stride table at *0x785db4) to decide if an item carries an extra coord/stack byte. |
| `0x1000108b` | `packetOpcodeHasExtByteFlag` | 52 | Tests bits 0x90 of the same per-tile 76-byte record byte to decide if an item needs an extra data byte during packet encoding. |
| `0x100010bf` | `initProxyConnectAndStartThread` | 161 | Resolves proxy host (inet_addr/gethostbyname) into g_1005a292, stores port/params, and launches proxy worker thread sub_10002041. |
| `0x10001160` | `setNavServerParam` | 16 | Setter that writes its argument into global g_1005db5c (proxy/nav config value). |
| `0x10001170` | `resolveHostAndPatchSendHook` | 178 | Resolves a host into g_1005a29a and one-time patches Tibia's send routine at 0x571ab1 via WriteProcessMemory, saving the original at g_1005d89b. |
| `0x10001222` | `closeAllProxySockets` | 76 | Sets shutdown flag g_1005a291, closes the main socket g_1005da3d, and iterates the 16-slot socket table g_1005da85 shutting down/closing each. |
| `0x1000126e` | `encodeCreatureAppear` | 209 | Emits a creature-appear (opcode 0x61) packet: registers creature id in g_1005d48f table, copies name, and packs outfit/light/speed fields from the shadow record. |
| `0x1000133f` | `buildMapDescriptionPacket` | 524 | Builds the map-description packet: nested loops over floors/tiles calling sub_1003a176, emitting creatures (sub_1000126e) and RLE skip runs into the output buffer. |
| `0x1000154b` | `encodeVipList` | 83 | Iterates the 10-slot VIP table at 0x6398a4 (12-byte stride) emitting VIP-add (opcode 0x78) entries with optional status byte into the packet. |
| `0x1000159e` | `encodeContainerAndTileItems` | 362 | Emits tile add/remove (opcodes 0x6a/0x6c) records at stored player coords, walking the 160-byte item table and creature list to serialize container/tile state. |
| `0x10001708` | `encodeOpenChannels` | 217 | Iterates the 16-slot channel table at 0x639aa8 (492-byte stride) emitting open-channel (opcode 0x6e) packets with channel id, name and message entries. |
| `0x100017e1` | `copyBattleListRecords` | 50 | Iterates the 150-slot creature/battle table g_1005a2a3 (40-byte stride) copying each active record (len from field+8) into the output via sub_1002ae6f. |
| `0x10001813` | `copyPrivateAndPartyChannels` | 93 | Copies active records from two 20-slot 69-byte-stride tables (g_1005cf17 and g_1005c9b3, private/party message channels) into the output buffer. |
| `0x10001870` | `fillWorldLightRecord` | 27 | Populates a small template (g_10042079..b) with world-light values read from client memory at 0x63bab8 (opcode 0x82 world light). |
| `0x1000188b` | `fillPlayerStatsRecord` | 158 | Snapshots player-stats fields (hp/mana/level/soul/etc.) from client globals at 0x62cd00..2c into the g_10042051 template (opcode 0xA0 stats). |
| `0x10001929` | `fillSkillsRecord` | 55 | Loops 7 skills copying value/percent pairs from client arrays at 0x63b418/0x63b45c into the g_1004206b skills template (opcode 0xA1 skills). |
| `0x10001960` | `buildFullGameStateSnapshot` | 310 | Assembles the complete synthetic login/game-state packet into a GlobalAlloc buffer, invoking all the sub-encoders (map, VIP, stats, skills, light, channels) and writing the length header. |
| `0x10001a96` | `hook_captureRenderCtx` | 34 | capture per-frame client render context pointer |
| `0x10001ab8` | `broadcastPacketToProxyClients` | 134 | Broadcasts an outgoing packet to all connected NavNet proxy clients in g_1005da85, sending a full game-state snapshot (sub_10001960) first to newly-attached (state 2) clients. |
| `0x10001b3e` | `recvHookTrampoline` | 12 | Thin wrapper passing a local stack buffer to sub_10001b4a (incoming-packet hook entry). |
| `0x10001b4a` | `incomingPacketHook` | 82 | Incoming-packet hook: when not disabled (g_1005db65), rewrites the client recv buffer at 0x785d78 and dispatches to original handler chain via g_1005d893. |
| `0x10001b9a` | `nopWrapper1` | 2 | Trivial forwarder to the empty stub sub_10001b9e; effectively a no-op. |
| `0x10001b9e` | `emptyStub1` | 1 | Empty function that immediately returns (padding/no-op stub). |
| `0x10001b9f` | `handleChannelClosePacket` | 151 | On a close-channel packet (opcode 0x99), and rate-limiting 0x87 within 1s via g_1005db54, clears the matching id from the private/party channel tables g_1005cf17/g_1005c9b3. |
| `0x10001bd0` | `emptyStub2` | 2 | Empty function body (no-op stub). |
| `0x10001c38` | `refreshPlayerPositionCache` | 82 | Refreshes the cached player object pointer (g_1005d87f via sub_1003997e when id 0x62cd30 changed) and copies 12 bytes of position into g_1005d883. |
| `0x10001c8a` | `patchContainerCountField` | 30 | If pending value g_1005db50 is set, writes it into field_6 of record g_1005db2a and clears the pending flag. |
| `0x10001ca8` | `hook_incomingPacketParser` | 696 | incoming-packet hook: shadow creature/channel tables + proxy forward |
| `0x10001f75` | `sendClientChatCommand` | 202 | Finds the TibiaClient window of this process and injects ESC/Enter keystrokes plus a call to client function 0x49B2A0 to send a chat/command line. |
| `0x10001fb0` | `emptyStub3` | 2 | Empty function body (no-op stub). |
| `0x10002041` | `installClientHooks_proxyServer` | 387 | install Tibia inline hooks + run embedded proxy TCP server |
| `0x100021c4` | `connectHookRedirectToProxy` | 113 | connect() hook: sets g_1004203a (unless port 796/0x31c), and when a proxy addr g_1005a29a is set, rewrites the sockaddr to the proxy ip/port before calling the original connect at g_1005d89b. |
| `0x10002235` | `proxyClientThread` | 326 | per-connection handler for the embedded proxy server |
| `0x100022e0` | `signatureCheckStub` | 28 | Compares stack values against a magic constant 1650879589 and branches; appears to be a guard/signature check (angr-truncated control flow). |
| `0x10002397` | `emptyStub4` | 4 | Empty function that returns immediately (no-op stub). |
| `0x1000239b` | `removeProxyClientSocket` | 46 | Scans the 16-slot proxy client socket table g_1005da85 for the given socket, clears its entry and state, and returns the slot. |
| `0x100023c9` | `addProxyClientSocket` | 57 | Finds the socket in g_1005da85 or claims a free slot, marking its state=2 (new/needs-snapshot); registration for a newly connected proxy client. |
| `0x10002402` | `readClientDword` | 35 | Reads a 4-byte value from the target (Tibia) process at the given address via ReadProcessMemory on g_1005db68. |
| `0x10002430` | `debugPrintHex` | 41 | Formats an argument as hex with wsprintfA and outputs via OutputDebugStringA (debug helper). |
| `0x10002459` | `debugFormatRecord2` | 33 | Duplicate of sub_10001036: formats a record via sub_10040940 and prints it with OutputDebugStringA. |
| `0x1000247a` | `sendProcExceptionHandler` | 143 | SEH-style handler for the send hook: formats a 'SendProc Error #%d %lX [on hotkey: %s]' message via sub_10025172 and restores saved registers (eip/esp/ebp) in the context record to resume. |
| `0x10002509` | `hotkeyProcExceptionHandler` | 180 | Exception handler for hotkey/command execution: logs 'HkeyProc Error' with command text, exits the thread on stack-overflow code 0xC00000FD, else restores the saved context to resume. |
| `0x100025bd` | `reportActionProcError` | 143 | Formats an 'ActionProc Error #%d %lX on hotkey: %s' message via wsprintfA, logs it via sub_10025172, and restores SEH frame slots in idx (exception handler for hotkey action dispatch). |
| `0x1000264c` | `reportGuiTimerProcError` | 90 | SEH handler that wsprintfA-formats 'GuiTimerProc Error #%d %lX', logs it via sub_10025172, and restores exception-frame registers in idx. |
| `0x100026a6` | `reportTimerProcError` | 139 | SEH handler for TimerProc: unless suppressed by g_1004265e, logs 'TimerProc Error #%d %lX'; on code 0xC0000005-style value sets a flag and ExitThread(1). |
| `0x10002731` | `reportTickProcError` | 190 | SEH handler for TickProc: picks a format string by exception code (400/418/502 vs default), logs via sub_10025172, and restores exception-frame slots in idx. |
| `0x100027ef` | `reportHprProcError` | 419 | SEH handler for HprProc: serializes 8 dwords of a 32-byte context blob (g_1005dc28..) big-endian into a 'HprProc Error' dump string, logs it, and restores the frame. |
| `0x10002992` | `initWaypointOrList` | 18 | Thin wrapper calling sub_1002ae6f(&g_10043598, &g_100435c8, 48) to initialize/clear a 48-byte-stride table between two globals. |
| `0x100029a4` | `hook_fullLightDetour` | 561 | full-light hack detour patching the client light renderer |
| `0x10002bd5` | `sub_10002bd5` | 1 | Empty stub function that immediately returns (no-op / placeholder). |
| `0x10002bd6` | `hook_fullLight_trampoline` | 7 | trampoline to hook_fullLightDetour |
| `0x10002bdd` | `installLightHook` | 36 | install the full-light detour at 0x4F4869 |
| `0x10002c01` | `setToggleOrByteFlag` | 30 | If arg is 0xFF toggles boolean g_10044773 (bitwise NOT), otherwise stores the byte into g_1004476b; returns the input. |
| `0x10002c1f` | `DllEntryPoint` | 67 | DLL entry: on attach spawn worker thread |
| `0x10002c6e` | `callIndirectViaGlobalFn` | 25 | Calls the function pointer at g_1004478d passing four args plus the address of a local stack buffer (indirect dispatch to a bot callback). |
| `0x10002c87` | `postBotMessage` | 55 | SendMessageA(WM_COMMAND) helper to drive host window |
| `0x10002cbe` | `EcInit` | 74 | exported bot init: store client ctx+hWnd, register dialogs, show UI |
| `0x10002d08` | `exitCurrentThread` | 14 | One-line wrapper that calls ExitThread(1) to terminate the calling thread. |
| `0x10002d16` | `postMenuCommand` | 48 | Packs two dword args into a small array and SendMessageA(g_1005f61a, WM_COMMAND(273), 0x539, ...) to post a command/menu message to the main window. |
| `0x10002d46` | `registerDialogs` | 824 | register the 23 TBOTDLG* feature dialogs |
| `0x1000307e` | `setDlgItemColor` | 88 | Builds a 44-byte record (type 0x11) from a dialog item handle, a color/state global and arg, and sends it via SendMessageA(g_10072fc0, 0x404, ...) to a custom control. |
| `0x100030d6` | `createPlayerInfoDirs` | 112 | Creates the 'playerinfo\' directory under the bot base path (g_10042f83) plus per-letter subfolders A-Z via wsprintfA + CreateDirectoryA. |
| `0x10003146` | `dlgProc_AutoAim` | 14876 | dlgProc_AutoAim — feature dialog window procedure (see doc 10) |
| `0x10006b62` | `openSaveSlotFileDialog` | 108 | Fills an OPENFILENAMEA (title 'Select or type a filename to be used as save slot', filter 'All Files') and calls GetOpenFileNameA, clearing g_100f9315 on success. |
| `0x10006bce` | `dlgProc_HudCreatureList` | 149 | dlgProc_HudCreatureList — feature dialog window procedure (see doc 10) |
| `0x10006c1b` | `sub_10006c1b` | 2 | Empty stub function (no body). |
| `0x10006c65` | `setHotkeyRowEnabled` | 107 | For row a0 in dialog g_10072f84: sets checkbox 4000+a0 (BM_SETCHECK) to a1 and enables/disables the paired 5000+a0 and 6000+a0 controls based on !a1. |
| `0x10006cd0` | `setHotkeyRowEnabledAlt` | 107 | Same as sub_10006c65 but for dialog g_10072fcc: sets checkbox 4000+a0 and toggles enable state of controls 5000+a0 and 6000+a0. |
| `0x10006d3b` | `dlgProc_Shortkeys` | 1573 | dlgProc_Shortkeys — feature dialog window procedure (see doc 10) |
| `0x10007360` | `dlgProc_Hotkeys` | 1704 | dlgProc_Hotkeys — feature dialog window procedure (see doc 10) |
| `0x10007a08` | `toggleNavProxyConnection` | 333 | Toggles NavNet/proxy connection state g_1005f537: on connect reads dialog edit fields (host/port/user/pass) and relabels button 'Disconnect', on disconnect shuts down socket g_1005f539 and relabels 'Connect'. |
| `0x10007b55` | `dlgProc_HudOnScreenInfo` | 336 | dlgProc_HudOnScreenInfo — feature dialog window procedure (see doc 10) |
| `0x10007ca5` | `dlgProc_AutoAimCombo` | 543 | dlgProc_AutoAimCombo — feature dialog window procedure (see doc 10) |
| `0x10007ec4` | `dlgProc_GraphicsTweaks` | 363 | dlgProc_GraphicsTweaks — feature dialog window procedure (see doc 10) |
| `0x1000802f` | `dlgProc_TargetingEditor` | 291 | dlgProc_TargetingEditor — feature dialog window procedure (see doc 10) |
| `0x10008152` | `parseSpellListA` | 306 | Splits the g_101f2ea8 newline/CR-delimited spell/word list into 0x202-stride records starting at index 224, copying each token and flagging 'exan '-prefixed entries via sub_10030442. |
| `0x10008284` | `parseSpellListB` | 306 | Same tokenizer as sub_10008152 but over g_1013f32c into records starting at index 352, marking 'exan ' spell entries via sub_10030442. |
| `0x100083b6` | `dlgProc_ScriptEditor` | 765 | dlgProc_ScriptEditor — feature dialog window procedure (see doc 10) |
| `0x100086b3` | `dlgProc_Skin` | 823 | dlgProc_Skin — feature dialog window procedure (see doc 10) |
| `0x10008975` | `sub_10008975` | 2 | Empty stub function (no body). |
| `0x100089ca` | `sub_100089ca` | 2 | Empty stub function (no body). |
| `0x10008a1d` | `sub_10008a1d` | 78 | Opaque/garbled decompilation (misaligned byte-arithmetic, no clear API calls); likely a data thunk or mis-disassembled region. |
| `0x10008a6b` | `populateSettingsDialogCombos` | 982 | Initializes the settings dialog g_10072f8c: sets edit-limits on fields and fills many combo boxes (delays in ms, square counts, name/spell tables) via CB_ADDSTRING loops over config globals. |
| `0x10008e41` | `loadWavIntoDsoundBuffer` | 523 | Opens a WAV file (base path + name) with mmioOpenA, parses RIFF/fmt/data chunks, and creates+fills a DirectSound secondary buffer via the g_10052658 vtable. |
| `0x1000904c` | `createDsoundPrimaryBuffer` | 246 | DirectSoundCreate, SetCooperativeLevel, creates a primary buffer and sets its WAVEFORMATEX (channels/rate/bits from args) then releases the temp buffer. |
| `0x10009142` | `releaseAllSoundBuffers` | 366 | Releases (vtable field_8) and nulls all ten DirectSound buffer/device globals g_10052658..g_1005267c on shutdown. |
| `0x100092b0` | `sub_100092b0` | 191 |  |
| `0x1000936f` | `playSoundBufferLooping` | 52 | If buffer valid and sound enabled, resets play position (field_34) and plays it looping (field_30) via the DirectSoundBuffer vtable. |
| `0x100093a3` | `handleAlarmTriggersOld` | 175 | Per-index alarm dispatcher over g_10207f12 3-byte flag rows: plays a sound buffer, sets on-screen flag g_100580f8, injects a packet via sub_1002ade7, and/or shuts down the socket. |
| `0x10009452` | `flashMainWindow` | 55 | Fills a FLASHWINFO (flags 15, 5 counts) and calls FlashWindowEx to flash the bot/client window for an alert. |
| `0x10009489` | `handleAlarmTriggers` | 197 | Refined per-index alarm handler over g_10207f12 rows: plays the matching DirectSound buffer from g_10052660[], sets flags, injects a status packet via sub_1002ade7, or shuts the socket. |
| `0x1000954e` | `getOrLoadNamedSound` | 175 | Looks up a sound by filename in the g_10287f44 cache table (lstrcmpi), lazily loading 'sounds\<name>' via sub_10008e41 into a free slot, then plays it once (field_30). |
| `0x100095b1` | `sub_100095b1` | 2 | Empty stub function (no body). |
| `0x1000d287` | `isNameInHashTable` | 83 | Checks if a name string exists in the A-Z bucketed hash table g_1000d21f (first-letter index, walks 2-dword entries doing case-insensitive lstrcmpi), returns 1 if found. |
| `0x1000d2da` | `traceMapPathBFS` | 1678 | Breadth-first knight/step pathfinder over an 18x14 tile grid (g_10288fc4 cost map, g_10052774 node pool); expands orthogonal (and diagonal if g_10052784) moves toward target (8,6), returning direction code. |
| `0x1000d946` | `sub_1000d946` | 2 | Empty stub function (no body). |
| `0x1000d96a` | `accumulateTileCosts` | 78 | Iterates the 18x14 tile grid adding per-tile step cost (g_10288fc4) into the running cost map g_10052785, skipping blocked (>=0xFFFFFFFE) tiles. |
| `0x1000d9b8` | `traceMapPathBFSSeeded` | 1745 | Variant of the 18x14 BFS pathfinder that pre-seeds a 3x3 area around the start (a0,a1) from g_10053da9 into a 23-byte-stride node pool, then expands toward target (8,6) returning a direction code. |
| `0x1000dad5` | `resetPathNode` | 39 | Zeroes the fields (field_4/8/10/14/15/16) of a single path/BFS node struct; likely inlined node-init helper (uninitialized pointer in isolation). |
| `0x1000e08e` | `sub_1000e08e` | 2 | Empty/stub function (single ret); no body. |
| `0x1000e0b2` | `applyGridCostOverlay` | 78 | Iterates the 14x18 walk grid (8-byte cells) adding overlay costs g_10288fc4 into the base cost grid g_10052785, skipping blocked (>=0xFFFFFFFE) cells. |
| `0x1000e100` | `floodFillPathCosts` | 1463 | BFS/flood-fill over the 18x14 tile grid from (a0,a1) expanding 4/8-directional neighbors into node table g_10052774, scaling base costs g_10053d69 by a2 and writing per-cell reach cost into g_10288fc4. |
| `0x1000e64d` | `sub_1000e64d` | 2 | Empty/stub function; no body. |
| `0x1000e6b9` | `findBestWaypointPath` | 3364 | Grid path search from center (8,6) to target-radius a2 building node tree g_10052774, then scores reachable goal nodes by distance/cost weighting (g_10053db2, g_10052780) to pick a best walk direction and accumulate per-direction stats. |
| `0x1000e8d8` | `initPathNode` | 39 | Zero-initializes a path-node record's fields (cost/parent/dir flags); truncated body sets field_4/8/10/14/15/16 to 0. |
| `0x1000f30d` | `sub_1000f30d` | 2 | Empty/stub function; no body. |
| `0x1000f406` | `sub_1000f406` | 4 | Empty/stub function (ret only); no body. |
| `0x1000f40a` | `searchPathToTargetRadius` | 2976 | BFS grid pathfinder from (8,6) toward a2-radius of (a0,a1), building node tree g_10052774 with cost/heuristic (field_8 Chebyshev-to-center), then scores goal-flagged nodes to choose best move and update direction stats g_102897a4. |
| `0x1000feb3` | `sub_1000feb3` | 2 | Empty/stub function; no body. |
| `0x1000ffac` | `sub_1000ffac` | 4 | Empty/stub function (ret only); no body. |
| `0x1000ffb0` | `searchLowestCostPath` | 2874 | Grid BFS pathfinder from (8,6) toward radius a2 of (a0,a1); seeds start cost from g_10052b25, expands node tree g_10052774, then scans goal-flagged nodes to pick the one with minimum accumulated cost (field_c) tie-broken by field_10/dir. |
| `0x10010a33` | `sub_10010a33` | 2 | Empty/stub function; no body. |
| `0x10010aec` | `sub_10010aec` | 4 | Empty/stub function (ret only); no body. |
| `0x10010af0` | `searchPathVariant` | 2762 | Another BFS grid pathfinder variant from (8,6) toward radius a2 of (a0,a1), populating node tree g_10052774 and selecting/scoring a best goal node (same 18x14 8-byte-cell cost model as the sibling path functions). |
| `0x100114b9` | `sub_100114b9` | 2 | Empty/stub function; no body. |
| `0x100115bc` | `stampAreaThreatCosts` | 188 | Overlays a threat/avoidance map (g_10052f78 for a2==1, g_100530bc for a2==2) onto the cost grid g_10052785, adding scaled weight a3*value into each unblocked 8-byte cell centered on (a0,a1). |
| `0x10011678` | `lineOfSightWalkable` | 375 | Bresenham-style line trace from client pos (g_10052768/6c) to (a0,a1) checking each cell of blocking map a2 (or sub_1003c87c fallback) for obstruction; returns 1 if the line is clear. |
| `0x100117ef` | `traceLineBlockedAt` | 333 | Bresenham line walk over blocking-map a2 from (a0,a1) along delta (a3-3,a4-3), returning 0 at the first blocked cell along the stepped path (5-arg line-of-sight test). |
| `0x1001193c` | `traceLineBlockedAt6` | 333 | Six-argument Bresenham line-of-sight walk over blocking map a2 (same stepped-cell obstruction trace as sub_100117ef with an extra parameter). |
| `0x10011a89` | `isInsideDangerZone` | 105 | Scans rectangle table g_1005398a..g_10053d68 (5-short records with a floor bitmask) and returns 1 if point (a0,a1) on current floor g_10052770 falls inside any enabled avoid/zone rectangle. |
| `0x10011af2` | `stampCreatureSpellArea` | 2356 | Stamps a creature's spell/attack danger template (area weights a3/a4/a5 selected by spell type) into the 8-byte-stride cost grid g_10052785 around the creature record, adjusting cells the bot should avoid. |
| `0x10011c25` | `sub_10011c25` | 2 | Empty/stub function; no body. |
| `0x100121bd` | `sub_100121bd` | 5 | Empty/stub function; no body. |
| `0x1001242d` | `decideRetreatStep` | 831 | Counts blocked (0xFFFFFFFE) cells in the 5x5 area around the player to detect being surrounded/trapped, then chooses a diagonal/orthogonal escape step via sub_10015204 or falls back to sub_10013e4d. |
| `0x10012609` | `sub_10012609` | 5 | Empty/stub function; no body. |
| `0x10012771` | `decodeRleMapCells` | 180 | Decodes a compressed cell/opcode stream a2 into buffer a0 (opcodes >=192 repeat-fill, >=128 write dword, >=64 write word, else write byte until a zero terminator); falls back to sub_1002ae6f if header != 0xFFFFFFA0. |
| `0x10012813` | `sub_10012813` | 2 | Empty/stub function; no body. |
| `0x10012827` | `findCreatureByName` | 647 | Iterates the 320-byte-stride creature shadow table g_101d5e78..g_101dfe78 matching by id/name/'pk'/'others'/'invisible' filters (lstrcmpi), incrementing hit counters and returning the matching creature record. |
| `0x10012aae` | `updateCreatureSpellThreatMap` | 713 | Walks the 320-byte creature table g_101d5e78..g_101dfe78, classifies each monster's spell type by level thresholds and calls sub_10011af2 to stamp its per-creature threat weight (result cached in field byte 0x22/26). |
| `0x10012b08` | `sub_10012b08` | 2 | Empty/stub function; no body. |
| `0x10012d79` | `creatureInDiamondRange` | 196 | Range test comparing player field_88 against creature record fields at idx+104/108, returning whether the creature lies within a diamond/box distance bound. |
| `0x10012e3d` | `otherPlayerAdjacent` | 158 | Scans the creature list (0x63fef8..0x64a308, 168-byte stride) for another active player on the same floor within distance g_101dfe9f of the player position (index[9],index[10]); returns 1 if found. |
| `0x10012edb` | `sub_10012edb` | 3941 | Large targeting/creature-scan routine over the creature table (uses g_10008a16 map buffers and many targeting config flags g_10043xxx); selects/evaluates targets, full body not fully resolved. |
| `0x1001330d` | `sub_1001330d` | 2 | Empty/stub function; no body. |
| `0x10013314` | `sub_10013314` | 2 | Empty/stub function; no body. |
| `0x100135d7` | `sub_100135d7` | 5 | Empty/stub function; no body. |
| `0x10013742` | `sub_10013742` | 2 | Empty/stub function; no body. |
| `0x1001391a` | `sub_1001391a` | 2 | Empty/stub function; no body. |
| `0x10013e4d` | `stepTowardTarget` | 201 | If target (local v0[9],v0[10]) is not already within 1 tile, runs pathfinder sub_1000d2da toward it (offset into the 18x14 grid) and, on a valid result, issues the walk step via sub_10014825. |
| `0x10013f16` | `buildPathCostGridAndScanCreatures` | 1181 | Builds the 14x18 pathfinding cost grid g_10052785 via sub_1003a148/sub_1003c4fa tile scans, flags blocking/monster items, then re-targets discovered monsters via sub_1000e100/sub_100115bc. |
| `0x10013fe3` | `sub_10013fe3` | 2 | Empty/stub function with no body. |
| `0x10014150` | `sub_10014150` | 5 | Empty/stub function with no body. |
| `0x100143ba` | `stampCreatureAvoidanceWeights` | 353 | Adds avoidance cost weights (128/160/-2) in a 5x5 area of grid g_10052785 around a creature and accumulates directional distance-scaled danger into g_10052f65/69/6d/71. |
| `0x1001451b` | `chooseFleeStep` | 720 | Reads player-relative offsets and directional danger sums to pick the safest adjacent tile to flee toward, then calls sub_10015204 to walk and sets g_100f0dc4=10. |
| `0x100147eb` | `walkToDispatch` | 58 | Wraps pathfind call 4604016() and dispatches to one of two follow-up movement handlers (4288032/4288784) based on its result code. |
| `0x10014825` | `stepInDirection` | 149 | Maps a direction code 1-8 to an adjacent tile offset from player position g_1005f854/g_1005f858 and issues a walk via sub_10015204 or sub_100147eb, setting g_100f0dc4=10. |
| `0x100148ba` | `stepToTargetIfAdjacent` | 109 | If target within 1 tile (/dx/,/dy/<=1) and not paused (g_100f0dcc), calls sub_1000ffb0 then steps toward it via sub_10014825. |
| `0x10014927` | `approachTargetOrPathfind` | 108 | If target within 1 tile calls the melee-adjust handler sub_10014f10, otherwise invokes full pathfinder sub_10013e4d. |
| `0x10014993` | `stepToTargetOrPathfind` | 122 | If target within 1 tile does sub_1000ffb0 then sub_10014825 step, otherwise falls back to pathfinder sub_10013e4d. |
| `0x10014a0d` | `stepTowardTargetDirect` | 97 | Unconditionally computes target offset, calls sub_1000ffb0 with adjusted coords and steps toward target via sub_10014825 when not paused. |
| `0x10014a6e` | `stepToStoredWaypointIfInRange` | 127 | If target within g_101dfe90+2 tiles and a stored destination g_10052778 exists, walks to that stored X/Y/Z via sub_100147eb guarded by flag g_1005277c. |
| `0x10014aed` | `stepInDirectionShim` | 14 | Thin wrapper that forwards a direction in ebx to sub_10014825. |
| `0x10014afb` | `approachInRangeElseSubMode` | 120 | If in-range flag g_100f0e24 set or target within g_101dfe90+2, enters sub-mode and delegates to distance-keeping handler sub_10014e64. |
| `0x10014b67` | `sub_10014b67` | 2 | Empty/stub function with no body. |
| `0x10014b75` | `approachInRangeElseKeepDistanceC69` | 120 | Range-gated approach variant that sets g_100f0e24 and delegates to keep-distance handler sub_10014c69. |
| `0x10014be1` | `sub_10014be1` | 2 | Empty/stub function with no body. |
| `0x10014bef` | `approachInRangeElseKeepDistanceD75` | 120 | Range-gated approach variant that sets g_100f0e24 and delegates to keep-distance handler sub_10014d75. |
| `0x10014c5b` | `sub_10014c5b` | 2 | Empty/stub function with no body. |
| `0x10014c69` | `keepDistanceStepC69` | 264 | Keep-distance movement: if target too close steps closer, at exact range suppresses moves that would break the distance ring by direction, else pathfinds via sub_10013e4d. |
| `0x10014d08` | `sub_10014d08` | 2 | Empty/stub function with no body. |
| `0x10014d3c` | `sub_10014d3c` | 2 | Empty/stub function with no body. |
| `0x10014d75` | `keepDistanceStepD75` | 235 | Keep-distance movement duplicate of sub_10014c69 without the g_100f0e28 early-out, gating directional steps to maintain range then pathfinding via sub_10013e4d. |
| `0x10014dff` | `sub_10014dff` | 2 | Empty/stub function with no body. |
| `0x10014e33` | `sub_10014e33` | 2 | Empty/stub function with no body. |
| `0x10014e64` | `maintainDistanceRingStep` | 172 | Maintains a target distance ring: inside range steps directly, at boundary calls sub_1000e6b9, beyond calls sub_1000f40a, each followed by a directional step via sub_10014825. |
| `0x10014f10` | `handleAdjacentTargetMeleeOrOpenDoor` | 740 | For an adjacent target: opens the correct door via sub_1002ade7 opcodes 111-114 by facing, else picks an unblocked adjacent walk tile from grid state and issues a client walk with cooldown g_100f0dc8. |
| `0x100151f4` | `setMovementState` | 16 | Setter storing its argument into movement-state global g_100f0dc4. |
| `0x10015204` | `walkToTile` | 36 | Computes tile offset from player position and calls the client walk routine 5049888() to path/walk to absolute (a0,a1). |
| `0x10015228` | `formatMonsterListLabel` | 63 | Formats a targeting-list monster label: plain lstrcpy when no condition, else wsprintf '%s %s %s' inserting a comparison operator string by field_21 index. |
| `0x10015267` | `populateTargetingDialogLists` | 950 | Repopulates the targeting GUI: sets spinner/checkbox controls via SendDlgItemMessageA, fills monster listbox from g_101d5e78 table, waypoint list from g_101dfea5, and script file list via DlgDirListA. |
| `0x1001561d` | `encodeSparseSettingsBlob` | 177 | Run-length/variable-width encodes a settings byte buffer into a compact blob (skip zeros, 1/2/4-byte value tags with 0x40/0x80/0xC0/0x3FFF markers), returning encoded length. |
| `0x100156ce` | `saveTargetingFile` | 373 | Serializes targeting settings g_101d5e78 via sub_1001561d and writes them to a chosen or scripts\\*.elft file (GetSaveFileNameA + CreateFileA/WriteFile), warning via sub_100159d8 on failure. |
| `0x10015843` | `loadTargetingFile` | 405 | Reads a .elft targeting file (GetOpenFileNameA or scripts\\ path, ReadFile) into a heap buffer and applies it to g_101d5e78 via decoder sub_10012771. |
| `0x100159d8` | `showSaveFailedMessageBox` | 37 | Shows a one-time MessageBoxA telling the user ElfBot couldn't save settings (Vista/UAC admin hint), guarded by flag g_1005dc49. |
| `0x100159fd` | `saveCavebotFile` | 380 | Serializes cavebot settings g_101e6ea8 via sub_1001561d and writes them to a chosen or scripts\\*.elfc file (GetSaveFileNameA + CreateFileA/WriteFile). |
| `0x10015b79` | `loadCavebotFile` | 545 | Loads a .elfc cavebot file (or imports legacy 'elfa' via sub_100167eb), decodes into g_101e6ea8 via sub_10012771, migrates extra waypoint pages, and refreshes via sub_10008152. |
| `0x10015d9a` | `selectCavebotWaypointWrapper` | 546 | Thin wrapper computing an index and calling sub_10015da3 to select a cavebot waypoint list item. |
| `0x10015da3` | `selectCavebotWaypointListItem` | 32 | Selects (LB_SETCURSEL/48) the waypoint list item g_10042929 in the cavebot dialog list control 0x404 of window g_10072f94. |
| `0x10015fdc` | `formatWaypointListRow` | 151 | Formats a cavebot waypoint list row via wsprintf ('T 00%d: ...') as either a labeled action or numeric X Y Z coords, and returns the waypoint's action-type character. |
| `0x10016073` | `formatLootRow` | 99 | Formats one loot-table entry into a display string via wsprintfA, mapping category byte 0xff/253/254 to ' e'/'g'/'e1' else '%05d %02d %s'. |
| `0x100160d6` | `refreshCavebotDialog` | 525 | Repopulates the cavebot GUI: fills waypoint list (0x404) and loot list (1035) from shadow tables plus rope/shovel/hotkey checkboxes via SendDlgItemMessageA. |
| `0x100162e3` | `listScriptFiles` | 245 | Builds '<dir>scripts\*.elfc' and DlgDirListA-populates listbox 1009, then strips the '.elfc' extension from each listed filename in place. |
| `0x100163d8` | `startScriptExecution` | 96 | Initializes script-run state: reads selected list item into g_100f0e00, zeroes flags, clears buffer g_100f45c5, and stamps start time via GetTickCount. |
| `0x10016438` | `parseWaypointsSection` | 947 | Tokenizes a [Waypoints] text buffer line-by-line into 4 fields and appends decoded waypoint records (walk/rope/ladder/stairs/etc.) to the g_101e6ea8 waypoint table. |
| `0x100167eb` | `loadScriptFile` | 129 | Heap-allocates 2MB, reads the given script file fully via CreateFileA/ReadFile, and passes the buffer+size to the waypoint/config parser sub_10016438. |
| `0x1001686c` | `parseScriptSections` | 1066 | Main .elf config parser: splits text into [Section] blocks, resets shadow tables and dispatches each line to per-section handlers, then refreshes the affected GUI dialogs. |
| `0x10016b8e` | `sub_10016b8e` | 2 | Empty/stub function (2-byte body, no operations). |
| `0x10016baf` | `parseWaypointHotkeyLine` | 565 | Per-line handler for waypoint action/label lines: decodes w/r/l/s/a/h/n/u action codes and parses trailing signed integer coords into the current waypoint record. |
| `0x10016de4` | `parseLootingLine` | 270 | Per-line [Looting] handler: parses item id, category token (e/g/e1 special-cased) and destination-container name into the current 10-word loot record. |
| `0x10016ef2` | `parseCavebotOptionLine` | 532 | Per-line [CavebotOptions] handler: sets Rope/Shovel type, SkipNearbyNodes count and OpenNextBp/LootNearbyTargets/LootDistantTargets yes-no flags. |
| `0x10017106` | `parseAlertLine` | 387 | Per-line [Alerts] handler: maps alert name (PlayerOnScreen/GmDetected/etc.) to a 3-byte flag block and sets sound/popup/(x/r) bits from the value string. |
| `0x10017289` | `appendCavebotHotkeyLine` | 39 | Per-line [CavebotHotkeys] handler: appends the raw line plus CRLF to the accumulated hotkey text buffer g_101f2ea8. |
| `0x100172b0` | `parseTargetingRecord` | 5399 | parse .elft targeting record + HUD-icon fields |
| `0x10017559` | `sub_10017559` | 5 | Empty/stub function (no body). |
| `0x100175e1` | `sub_100175e1` | 5 | Empty/stub function (no body). |
| `0x100176bf` | `sub_100176bf` | 5 | Empty/stub function (no body). |
| `0x100188bf` | `sendDlgItemAndCommand` | 58 | Helper that sends a message to a dialog child control then posts a WM_COMMAND (273) to the parent to simulate/notify a control action. |
| `0x100188f9` | `serializeCavebotScript` | 1169 | Serializes cavebot state (Waypoints/Looting/CavebotOptions/Alerts/CavebotHotkeys sections) into a GlobalAlloc text buffer and loads it into edit control 1002. |
| `0x10018d8a` | `serializeTargetingScript` | 1559 | Serializes targeting state into [TargetingMonsters]/[TargetSelection]/[StanceOptions] text over a 320-byte-stride monster table and pushes it to edit control 1002. |
| `0x100193a1` | `serializeIconsScript` | 944 | Serializes the HUD [Icons] config (name/enabled/size/commands plus per-icon Active/Inactive state icon+bkg ids, alignment, text) into edit control 1002. |
| `0x10019751` | `dlgProc_Cavebot` | 4014 | dlgProc_Cavebot — feature dialog window procedure (see doc 10) |
| `0x100199eb` | `sub_100199eb` | 2 | Empty/stub function (2-byte body, no operations). |
| `0x10019adf` | `sub_10019adf` | 5 | Empty/stub function (no body). |
| `0x1001a136` | `sub_1001a136` | 5 | Empty/stub function (no body). |
| `0x1001a338` | `sub_1001a338` | 5 | Empty/stub function (no body). |
| `0x1001a50a` | `sub_1001a50a` | 5 | Empty/stub function (no body). |
| `0x1001a715` | `dlgProc_Targeting` | 4037 | dlgProc_Targeting — feature dialog window procedure (see doc 10) |
| `0x1001b2af` | `sub_1001b2af` | 5 | Empty/stub function (no body). |
| `0x1001b6df` | `populateIconComboBoxes` | 310 | Fills the Icons dialog combo boxes (size/type/alignX/alignY) with label strings from the g_100423c8/g_10042394/g_10042322/g_1004233a option tables. |
| `0x1001b815` | `populateIconList` | 134 | Repopulates the icons listbox (0x404) by iterating the 4308-byte-stride icon table from g_1014f420 and appending each name plus a '<New Icon>' entry. |
| `0x1001b89b` | `parseSignedInt` | 35 | Parses a signed decimal string: negates sub_10040900's unsigned parse result when a leading '-' is present. |
| `0x1001b8be` | `dlgProc_SkinEditor` | 5096 | dlgProc_SkinEditor — feature dialog window procedure (see doc 10) |
| `0x1001b92a` | `sub_1001b92a` | 5 | Empty/stub function (no body). |
| `0x1001b954` | `sub_1001b954` | 2 | Empty/stub function (2-byte body, no operations). |
| `0x1001b97b` | `sub_1001b97b` | 2 | Empty/stub function (2-byte body, no operations). |
| `0x1001b9a2` | `sub_1001b9a2` | 2 | Empty/stub function (2-byte body, no operations). |
| `0x1001ccb1` | `previewHotkeyCommandTemplate` | 542 | Builds a hotkey command preview by appending placeholder tokens ({creature}/{hp%}/{num}/{window}/etc.) decoded from 4 param nibbles and shows it in edit 1005. |
| `0x1001cecf` | `advanceHotkeyParamPrompt` | 103 | Advances through a hotkey's up-to-4 parameters, storing the current param type in g_100f0d34 and opening prompt dialog 9002, else finishing dialog 9003. |
| `0x1001cf36` | `formatHotkeyParamPrompt` | 539 | Formats the current hotkey-parameter prompt: picks a color code by param index and appends the decoded placeholder token, then loads it into edit 1002. |
| `0x1001d151` | `dlgProc_CommandBuilder` | 399 | dlgProc_CommandBuilder — feature dialog window procedure (see doc 10) |
| `0x1001d2e0` | `dlgProc_CommandParamBuilder` | 797 | dlgProc_CommandParamBuilder — feature dialog window procedure (see doc 10) |
| `0x1001d5fd` | `dlgProc_CommandParamPicker` | 2310 | dlgProc_CommandParamPicker — feature dialog window procedure (see doc 10) |
| `0x1001ddd2` | `sub_1001ddd2` | 2 | Empty/stub function (2-byte body, no operations). |
| `0x1001df05` | `dlgProc_CommandPicker` | 724 | dlgProc_CommandPicker — feature dialog window procedure (see doc 10) |
| `0x1001e1d9` | `dlgProc_HotkeyActionPicker` | 314 | dlgProc_HotkeyActionPicker — feature dialog window procedure (see doc 10) |
| `0x1001e313` | `dlgProc_FriendsEnemies` | 210 | dlgProc_FriendsEnemies — feature dialog window procedure (see doc 10) |
| `0x1001e3e5` | `dlgProc_Healer` | 990 | dlgProc_Healer — feature dialog window procedure (see doc 10) |
| `0x1001e7c3` | `dlgProc_NavNet` | 880 | dlgProc_NavNet — feature dialog window procedure (see doc 10) |
| `0x1001eb33` | `dlgProc_LinksNavNet` | 985 | dlgProc_LinksNavNet — feature dialog window procedure (see doc 10) |
| `0x1001ef0c` | `dlgProc_LinksProxy` | 1649 | dlgProc_LinksProxy — feature dialog window procedure (see doc 10) |
| `0x1001f57d` | `showOrCreateDialog` | 64 | Shows and focuses an existing window if valid, otherwise dispatches a create-dialog request via sub_10002c87 with the given command id and callback. |
| `0x1001f5bd` | `refreshAllSettingsDialogs` | 2882 | Master GUI sync: destroys transient windows then pushes every persisted bot setting (healer/targeting/tools/HUD flags and values) into all settings dialog controls. |
| `0x100200ff` | `saveConfigFile` | 207 | Writes the ~903KB in-memory config blob (g_100f9494) to the resolved config file path via CreateFileA/WriteFile, building the path from name/index globals. |
| `0x10020124` | `sub_10020124` | 5 | Empty/stub function (single ret), no body. |
| `0x100201d3` | `loadConfigAndInitBot` | 560 | Builds a config/profile file path from bot globals, memory-maps it and parses via sub_1002ae6f, then resets bot state and re-inits GUI/loot, returning an LRESULT. |
| `0x10020216` | `sub_10020216` | 5 | Empty/stub function (single ret), no body. |
| `0x10020237` | `sub_10020237` | 5 | Empty/stub function (single ret), no body. |
| `0x1002040d` | `loadLootItemsFile` | 162 | Opens and memory-maps '<basedir>lootitems.txt' via CreateFileA/CreateFileMapping/MapViewOfFile and parses it with sub_100204af, then closes handles. |
| `0x100204af` | `parseLootItemsPairs` | 265 | Scans the lootitems text buffer for pairs of decimal numbers per line, converts each via sub_10040900 into parallel arrays g_1008baee/g_1008c2ee (up to 0x200 entries). |
| `0x100204ea` | `sub_100204ea` | 2 | Empty/stub function (single ret), no body. |
| `0x100204ef` | `sub_100204ef` | 5 | Empty/stub function (single ret), no body. |
| `0x100205bf` | `proxyConnectionTick` | 838 | Iterates the proxy connection table (g_102898ce, stride records) applying idle/timeout counters, tearing down dead sockets, reconnecting, and injecting keepalive/status packets via sub_10020950/sub_1002ae6f. |
| `0x10020905` | `sendProxyStatusPacket` | 75 | Wraps a string payload into a length-prefixed packet (type 406) and sends it to a proxy connection via sub_10020950. |
| `0x10020950` | `proxySendPacket` | 133 | Builds a framed packet from a length-prefixed buffer, passes it through a transform (sub_100212d7) and sends it on the connection's socket via send(). |
| `0x100209d5` | `proxyListenAcceptLoop` | 463 | Creates the proxy listen socket (bind/listen on a configured port), allocates TLS slots, then loops accept()ing clients into the connection table and spawning sub_10020d53 worker threads. |
| `0x10020ba4` | `rewriteConnectPacket` | 164 | When redirect is enabled, rewrites a Tibia login/connect packet's port and IP (resolving g_1013f2a0 via inet_addr/gethostbyname) before forwarding through the original handler g_102898c0. |
| `0x10020c48` | `proxyThreadStoreTls` | 67 | Stores the proxy thread's per-thread context pointers into the five TLS slots (g_1005dc00..g_1005dc10) via TlsSetValue. |
| `0x10020c8b` | `proxyExceptionHandlerA` | 128 | SEH-style handler: reads TLS context, formats a 'ProxyException Error #%d Chunk:' message via wsprintfA/sub_10025172 and restores registers into the exception frame. |
| `0x10020d0b` | `proxyExceptionHandler4` | 72 | SEH-style handler using the g_1005dc14/1c/20 context globals: formats a 'ProxyException4 Error #%d' log message and restores the exception frame. |
| `0x10020d53` | `proxyClientToServerThread` | 742 | Proxy worker thread: recv()s from the client socket, on first packet parses server address/keys, connect()s to the real server, spawns sub_10021047, and relays client->server bytes. |
| `0x10021039` | `sub_10021039` | 14 | Tiny SEH frame unwind stub: writes a saved value into the FS-based exception registration record. |
| `0x10021047` | `proxyServerToClientThread` | 590 | Proxy worker thread: recv()s server->client packets into a 0xf000 buffer, reassembles length-prefixed frames, decrypts/inspects each via sub_100212a3/sub_1002131f and forwards to the client socket. |
| `0x10021295` | `sub_10021295` | 14 | Tiny SEH frame unwind stub: writes a saved value into the FS-based exception registration record. |
| `0x100212a3` | `decryptPacketBlocks` | 52 | Iterates 8-byte blocks of a length-prefixed packet (starting at offset 6) invoking a block cipher routine (helper at 5547296) over each. |
| `0x100212d7` | `encryptPacketBlocks` | 72 | Pads a length-prefixed packet to an 8-byte-aligned XTEA-style block boundary and encrypts each 8-byte block via the helper at 0x54a500. |
| `0x1002131f` | `parseServerPacketOpcodes` | 2228 | Walks a decrypted Tibia game packet opcode-by-opcode (huge switch on byte codes), advancing the cursor per message type and dispatching map/creature updates, floors, and item handlers; logs corrupt packets. |
| `0x100213a0` | `sub_100213a0` | 5 | Empty/stub function (single ret), no body. |
| `0x10021792` | `sub_10021792` | 2 | Empty/stub function (single ret), no body. |
| `0x1002179d` | `sub_1002179d` | 5 | Empty/stub function (single ret), no body. |
| `0x100217c7` | `sub_100217c7` | 2 | Empty/stub function (single ret), no body. |
| `0x100217d2` | `sub_100217d2` | 5 | Empty/stub function (single ret), no body. |
| `0x100217fc` | `sub_100217fc` | 2 | Empty/stub function (single ret), no body. |
| `0x10021807` | `sub_10021807` | 5 | Empty/stub function (single ret), no body. |
| `0x10021828` | `sub_10021828` | 2 | Empty/stub function (single ret), no body. |
| `0x1002186e` | `sub_1002186e` | 2 | Empty/stub function (single ret), no body. |
| `0x10021879` | `sub_10021879` | 5 | Empty/stub function (single ret), no body. |
| `0x100218a0` | `sub_100218a0` | 2 | Empty/stub function (single ret), no body. |
| `0x100218ab` | `sub_100218ab` | 5 | Empty/stub function (single ret), no body. |
| `0x100218d2` | `sub_100218d2` | 2 | Empty/stub function (single ret), no body. |
| `0x100218dd` | `sub_100218dd` | 5 | Empty/stub function (single ret), no body. |
| `0x100218fb` | `sub_100218fb` | 2 | Empty/stub function (single ret), no body. |
| `0x1002193e` | `sub_1002193e` | 2 | Empty/stub function (single ret), no body. |
| `0x10021949` | `sub_10021949` | 5 | Empty/stub function (single ret), no body. |
| `0x10021970` | `sub_10021970` | 2 | Empty/stub function with no body (thunk or padding). |
| `0x1002197b` | `sub_1002197b` | 5 | Empty/stub function with no body (thunk or padding). |
| `0x100219a2` | `sub_100219a2` | 2 | Empty/stub function with no body (thunk or padding). |
| `0x100219ad` | `sub_100219ad` | 5 | Empty/stub function with no body (thunk or padding). |
| `0x100219cb` | `sub_100219cb` | 2 | Empty/stub function with no body (thunk or padding). |
| `0x10021a05` | `sub_10021a05` | 2 | Empty/stub function with no body (thunk or padding). |
| `0x10021a10` | `sub_10021a10` | 2 | Empty/stub function with no body (thunk or padding). |
| `0x10021a3a` | `sub_10021a3a` | 2 | Empty/stub function with no body (thunk or padding). |
| `0x10021a7a` | `sub_10021a7a` | 2 | Empty/stub function with no body (thunk or padding). |
| `0x10021a85` | `sub_10021a85` | 2 | Empty/stub function with no body (thunk or padding). |
| `0x10021aa9` | `sub_10021aa9` | 2 | Empty/stub function with no body (thunk or padding). |
| `0x10021c29` | `sub_10021c29` | 4 | Empty stub that simply returns (thunk or no-op). |
| `0x10021c2d` | `buildSpellFromRuneId` | 490 | Maps a spell/rune id (a1 low bits) to a Tibia spell string (exori vis/mort/…) or a rune constant, building an autohotkey/HUD action record then appending tab/CR via sub_10020950. |
| `0x10021c8c` | `sub_10021c8c` | 5 | Empty/stub function with no body (thunk or padding). |
| `0x10021ca2` | `sub_10021ca2` | 5 | Empty/stub function with no body (thunk or padding). |
| `0x10021cb8` | `sub_10021cb8` | 5 | Empty/stub function with no body (thunk or padding). |
| `0x10021cce` | `sub_10021cce` | 5 | Empty/stub function with no body (thunk or padding). |
| `0x10021ce4` | `sub_10021ce4` | 5 | Empty/stub function with no body (thunk or padding). |
| `0x10021cfa` | `sub_10021cfa` | 5 | Empty/stub function with no body (thunk or padding). |
| `0x10021d10` | `sub_10021d10` | 5 | Empty/stub function with no body (thunk or padding). |
| `0x10021d26` | `sub_10021d26` | 5 | Empty/stub function with no body (thunk or padding). |
| `0x10021d3c` | `sub_10021d3c` | 5 | Empty/stub function with no body (thunk or padding). |
| `0x10021d52` | `sub_10021d52` | 5 | Empty/stub function with no body (thunk or padding). |
| `0x10021d68` | `sub_10021d68` | 5 | Empty/stub function with no body (thunk or padding). |
| `0x10021e4e` | `dispatchActionByType` | 130 | Dispatches a queued action record by its type tag (98/99/97 branches over an inline buffer), else calls sub_10021ed2/sub_10021f06 to toggle client creature flags by id. |
| `0x10021e74` | `sub_10021e74` | 2 | Empty/stub function with no body (thunk or padding). |
| `0x10021ed2` | `setCreatureFlagBit25` | 52 | Indexes the client creature array (via *0x7998dc, 80-byte stride, +36) and masks byte with 25 to set/clear a creature status bit for the given creature id. |
| `0x10021f06` | `setCreatureFlagBit32` | 52 | Indexes the client creature array (via *0x7998dc, 80-byte stride, +35) and masks byte with 32 to set/clear a creature status bit for the given creature id. |
| `0x10021f3a` | `getHighResMillis` | 50 | Reads QueryPerformanceFrequency/Counter and computes an elapsed-milliseconds value (scaled by 1000) as a high-resolution timestamp. |
| `0x10021f6c` | `botUiWorkerLoop` | 1516 | Infinite worker loop: manages hotkey window show/hide, foreground-window detection (GetForegroundWindow/CurrentProcessId), Ctrl+F11/F12 lighthack toggles, config/script reload, HUD title updates, then Sleep(100). |
| `0x10022558` | `sub_10022558` | 14 | Tiny stub that stores a stack value via an internal ccall helper and returns (SEH/frame setup fragment). |
| `0x10022566` | `syncPlayerInfoFiles` | 599 | Iterates the shadow creature table (g_10077175..g_100809cd), writing/reading per-player playerinfo\<X>\<name>.txt files with CreateFileA/WriteFile/ReadFile and parsing vocation/level/guild fields. |
| `0x100227bd` | `botMainTickLoop` | 3467 | Main bot engine thread loop: sets up SEH/watchdog trace globals, calls targeting/healer/cavebot/hud subsystems on GetTickCount intervals, decrements dozens of cooldown timers, ages creature tables, and Sleeps ~10ms per tick. |
| `0x10023548` | `threadExitStub` | 22 | Frame-setup stub that calls ExitThread(1) to terminate the current bot thread. |
| `0x1002355e` | `pickAttackTarget` | 138 | Selects an attack target: returns cavebot lure creature (g_10080bcb) or secondary (g_10080bb3) if reachable via sub_1003bc09, else falls back to sub_1003bc54 targeting. |
| `0x100235e8` | `runAttackHealerLogic` | 431 | Per-tick attack/heal decision: validates candidate creatures via sub_100237a4, checks mana (>=1200 at *0x63fe78) and cooldown flags, and fires spell casts through sub_1003a60a/sub_10023797. |
| `0x10023797` | `setCastCooldown` | 13 | Sets the global cast-cooldown counter g_100f933b to g_101d5e2a+2 (configured spell delay). |
| `0x100237a4` | `isCreatureValidTarget` | 189 | Validates a creature record for targeting: checks it is on our floor (field_2c vs g_1005f85c), visible (field_90), and applies player/monster/summon filters, optionally drawing via sub_10011678. |
| `0x10023861` | `sub_10023861` | 26 | Empty stub that returns immediately (no-op). |
| `0x1002387b` | `snapshotClientTick` | 24 | Snapshots the client tick: stores GetTickCount into g_1008b7cb and the client value at *0x63fe8c into g_1008b7c7, returning that address. |
| `0x10023893` | `targetingAttackScanTick` | 434 | Cavebot/targeting tick: throttles via g_100f45bc, drives autoattack sequence over 16x492-byte slots, calls sub_1003c4fa per creature and emits enter/attack packets. |
| `0x10023a45` | `resolveActiveCreaturePtr` | 74 | Resolves the current creature/target pointer into g_1005e19c, using cached g_100f9355 or falling back to sub_100235e8/sub_1002355e lookups. |
| `0x10023a8f` | `scanBattleListStatusTick` | 947 | Iterates the 168-byte battlelist from 0x63fef8..0x64a308 counting flagged creatures, runs sub_1003a320/3da/494/550 checks, swaps outfit bytes for anti-idle/HUD, sets g_100f49c9/cd. |
| `0x10023e42` | `pushExpSampleWindow` | 96 | Advances a 10-slot circular buffer g_1008b8ac of exp samples, sums them into g_1008b8d8, and formats the total via sub_10040940. |
| `0x10023ea2` | `updateTitleBarStats` | 527 | Builds the window title 'CiroScript.com ... exp/hour' with slot/char name, averages a 5-slot exp-rate ring, and sets it via SetWindowTextA(g_1005f626). |
| `0x100240b1` | `handleClientMinimizeState` | 287 | Watches Tibia client state at 0x64a9c0, finds the TibiaClient window for this process, and minimizes/restores it via ShowWindow/SendMessage per bot config. |
| `0x100241d0` | `formatUnsignedBillions` | 57 | Formats a 64-bit unsigned value as decimal into a buffer via wsprintfA, splitting high/low parts around 1e9 with '%lu%.9lu'. |
| `0x10024209` | `parseUnsignedDecimal` | 45 | Parses an ASCII decimal string to an unsigned integer by the classic digit*10 accumulation loop. |
| `0x10024236` | `parseBigDecimalString` | 159 | Parses a long decimal string exceeding 9 digits by splitting off the last 9 chars and combining high*1e9+low via sub_10024209. |
| `0x1002424e` | `sub_1002424e` | 2 | Empty/stub function (2-byte no-op body). |
| `0x100244e1` | `botDllInit` | 788 | Main bot init: creates worker threads, WSAStartup, licence check via gethostbyname, parses command line, HeapAllocs bot buffers, seeds item tables and reads outfits.txt. |
| `0x10024632` | `sub_10024632` | 2 | Empty/stub function (2-byte no-op body). |
| `0x100247f7` | `seedRuneItemIds` | 165 | Registers a fixed set of rune/spell item IDs (2319, 2981-2985, 2431-2434, 2471-2473, 3503-3504, 2354-2385) via sub_1003c496. |
| `0x1002489c` | `buildFoodItemIdTable` | 145 | Fills the item-id table g_1008caee with food IDs across several ranges (3577-3602, 3620-3729 skipping 3658/3661, 3900-3917, etc.). |
| `0x1002492d` | `healerManaSpellTick` | 897 | Healer engine tick: decrements cooldown counters and, when HP/mana thresholds are crossed, fires heal/mana spells or potions via sub_1002ade7/sub_10039413 packet sends. |
| `0x10024cae` | `healByNameCommand` | 184 | Maps a heal keyword ('health'/'shealth'/'ghealth') to spell code 266/236/239 and queues the self-heal packet via sub_1002ade7 unless on cooldown. |
| `0x10024d66` | `findAdjacentAttackTarget` | 467 | Scans the battlelist for a creature in the tiles adjacent to the player (based on facing direction) and casts an area rune ('exevo vis hur' or configured) at it. |
| `0x10024f39` | `castManaRestoreSpell` | 117 | Casts the mana-restore spell (id 3160) via sub_1002ae92, fills the g_100432e5 spell packet, and sends it with sub_1002ade7. |
| `0x10024fae` | `snapshotPlayerStats` | 61 | Snapshots player HP/mana and XYZ position from client globals (0x63fe94/0x63fe78/0x64f600..608) into bot shadow globals. |
| `0x10024feb` | `handleIncomingPacketOpcodesLite` | 391 | Dispatches select server packet opcodes (0x84 creature turn/anti-KS relabel, 0x96, 0xA1 attack target None, 0x64-0x68) updating bot state and logging. |
| `0x10025172` | `logErrorEntry` | 328 | Appends a timestamped line to elferrors459.log (with a one-time date header) via CreateFileA/WriteFile using wsprintfA '%s.%03d %s'. |
| `0x100252ba` | `logScriptEntry` | 287 | Appends a timestamped line to elfscript.log (one-time date header) via CreateFileA/WriteFile, mirroring the error-log routine. |
| `0x100253d9` | `logLockEntry` | 287 | Appends a timestamped line to elflock459.log (one-time date header) via CreateFileA/WriteFile, mirroring the other log routines. |
| `0x100254f8` | `fileContainsLine` | 328 | Reads a bot data file (path = g_10042d7b + name), splits it on CR/LF and returns 1 if any line case-insensitively matches a1 via lstrcmpi. |
| `0x100255fa` | `sub_100255fa` | 2 | Empty/stub function (2-byte no-op body). |
| `0x10025619` | `sub_10025619` | 2 | Empty/stub function (2-byte no-op body). |
| `0x1002561e` | `sub_1002561e` | 2 | Empty/stub function (2-byte no-op body). |
| `0x10025646` | `readFileLineByIndex` | 496 | Reads a data file, counts its CR/LF-delimited lines, then copies the requested line index (or a random one when a1==-1) back into the a0 buffer. |
| `0x10025740` | `sub_10025740` | 2 | Empty/stub function (2-byte no-op body). |
| `0x100257f9` | `sub_100257f9` | 2 | Empty/stub function (2-byte no-op body). |
| `0x1002580f` | `sub_1002580f` | 2 | Empty/stub function (2-byte no-op body). |
| `0x10025814` | `sub_10025814` | 2 | Empty/stub function (2-byte no-op body). |
| `0x1002583e` | `fileWriteOrDelete` | 241 | File writer keyed on mode a2: deletes (2), appends raw (0), or appends line+CRLF (1) to g_10042d7b+name via CreateFileA/WriteFile/DeleteFileA. |
| `0x1002592f` | `appendPacketToLog` | 330 | Appends a hex/byte dump of a client/server packet (prefixed 'c '/'b ' and a tick timestamp) to elflog.txt, capping at 300 bytes. |
| `0x10025a79` | `handleIncomingPacketOpcodesFull` | 1171 | Full incoming-packet dispatcher (opcodes 0x83/0x84/0x79/0x8C/0x64-0x68/0x96/0xA1/0xDD) updating map/creature state, walk-dir remap, HUD text and error-context globals. |
| `0x10025f0c` | `handleChannelTextPacket` | 1052 | Parses a channel/private text (0x96) packet: matches sender against known channel/command tables and dispatches CiroScript-style {..} labeled command blocks via sub_10030442. |
| `0x10025fb8` | `sub_10025fb8` | 5 | Empty/stub function (5-byte no-op body). |
| `0x100260ee` | `sub_100260ee` | 5 | Empty/stub function (5-byte no-op body). |
| `0x10026179` | `sub_10026179` | 5 | Empty/stub function (5-byte no-op body). |
| `0x10026198` | `sub_10026198` | 5 | Empty/stub function (5-byte no-op body). |
| `0x1002622e` | `sub_1002622e` | 2 | Empty/stub function (2-byte body), likely a no-op thunk or padding entry. |
| `0x1002625c` | `sub_1002625c` | 2 | Empty/stub function (2-byte body), no observable behavior. |
| `0x10026340` | `sendMapClickPacket` | 219 | Builds a 40-byte packet from position/creature globals (g_102898xx, 0x7998xx, g_1013f3xx) and send()s it on the client socket, then Sleep(400). |
| `0x1002641f` | `installGameSendHook` | 284 | SEH-guarded prologue that stashes registers into g_1005dbxx frame, conditionally calls sendMapClickPacket, and patches the outgoing packet buffer at 0x7998a0 via sub_10025a79. |
| `0x1002653b` | `sub_1002653b` | 10 | Empty tail/landing pad reached by the preceding hooked function's non-returning jump. |
| `0x10026545` | `callHudDrawCallback` | 43 | Stores arg0 into g_100428d5 and, unless arg2 == -1, forwards all four args to the function pointer g_100428d1 (a draw/dispatch callback). |
| `0x10026570` | `sub_10026570` | 1 | Empty stub (single-byte ret), no-op. |
| `0x10026571` | `findNearestWaypointRecord` | 98 | Scans the 12-byte-stride table g_100f42a8..g_100f45a8 for the record on the current floor (g_1005f85c) with minimum Manhattan distance to player pos (g_1005f854/858). |
| `0x100265d3` | `claimFarthestWaypointSlot` | 135 | Scans g_100f42a8..g_100f45a8 for the farthest matching-floor record (or first empty slot) and writes x/y/z (a0,a1,a2) into it, reserving a waypoint entry. |
| `0x100265f4` | `sub_100265f4` | 2 | Empty/stub function (2-byte body). |
| `0x100266b0` | `matchLowercasedTokenInList` | 82 | Lowercases up to 20 non-space chars of the input into a scratch buffer, then walks a null-separated string list comparing each entry, returning 1 on match else 0. |
| `0x10026702` | `copyLengthPrefixedString` | 34 | Copies a length-prefixed string (field_0 count, chars at field_2) into a C buffer capped at 255 bytes and null-terminates it. |
| `0x10026724` | `applyChatTriggerReplacements` | 859 | On the last received chat line (g_100f49e5), matches configured trigger keywords (g_1014f3xx/g_101d5exx) and fires reply/afk/party/channel actions via sub_100399af and sub_1002ade7. |
| `0x10026a7f` | `writeServerListIni` | 96 | Builds '<datadir>serverlist.txt' and WritePrivateProfileStringA-writes each 84-byte server record (name at +30, host at +64) under [Servers]. |
| `0x10026adf` | `botRenderTick` | 7340 | Main per-frame bot scan/HUD tick: iterates the creature list (g_1005e1a0..e5a0) and tile grid (0x63fef8..0x64a308), updates target globals g_100434xx, times events with GetTickCount, draws overlays. |
| `0x10027176` | `handleAttackTargetOnTile` | 462 | On the current floor, resolves the creature stack at a tile (sub_1003a03f), finds a valid attackable creature (type 99, flags & 8272), sets target globals g_100434xx and triggers attack/waypoint. |
| `0x1002757b` | `sub_1002757b` | 2 | Empty/stub function (2-byte body). |
| `0x10027708` | `sub_10027708` | 2 | Empty/stub function (2-byte body). |
| `0x10027da9` | `sub_10027da9` | 5 | Empty/stub function (5-byte body), likely a jmp thunk. |
| `0x10027dc9` | `sub_10027dc9` | 5 | Empty/stub function (5-byte body), likely a jmp thunk. |
| `0x1002807a` | `sub_1002807a` | 2 | Trivial wrapper that tail-calls the empty sub_1002807f; no observable behavior. |
| `0x1002807f` | `sub_1002807f` | 1 | Empty/stub function (1-byte body). |
| `0x10028106` | `sub_10028106` | 2 | Empty/stub function (2-byte body). |
| `0x1002842e` | `sub_1002842e` | 2 | Empty/stub function (2-byte body). |
| `0x100288e6` | `sub_100288e6` | 2 | Empty/stub function (2-byte body). |
| `0x10028970` | `registerRecentPlayerName` | 124 | Copies a name (<=63 chars) then finds or inserts it into the 256-slot player table g_100ec0b6, stamping GetTickCount and an associated value (level/id) per entry. |
| `0x100289bb` | `sub_100289bb` | 2 | Empty/stub function (2-byte body). |
| `0x100289ee` | `parseMapClickDirective` | 749 | Parses a script token stream for keywords (up/down/left/right/floor via FourCC compares), computes an offset and calls sub_10029a61 to issue a directional map/use action. |
| `0x10028a45` | `sub_10028a45` | 5 | Empty/stub function (5-byte body), likely a jmp thunk. |
| `0x10028a67` | `sub_10028a67` | 5 | Empty/stub function (5-byte body), likely a jmp thunk. |
| `0x10028a89` | `sub_10028a89` | 5 | Empty/stub function (5-byte body), likely a jmp thunk. |
| `0x10028aab` | `sub_10028aab` | 5 | Empty/stub function (5-byte body), likely a jmp thunk. |
| `0x10028aee` | `sub_10028aee` | 2 | Empty/stub function (2-byte body). |
| `0x10028b11` | `sub_10028b11` | 2 | Empty/stub function (2-byte body). |
| `0x10028b34` | `sub_10028b34` | 2 | Empty/stub function (2-byte body). |
| `0x10028cf5` | `measureStringPixelWidth` | 23 | Sums per-character pixel widths from the font width table g_10044630 across a string to compute its rendered text width. |
| `0x10028d0c` | `drawCreatureMarkerHud` | 608 | Iterates the marker list (g_1005e1a0..e6a0), maps world coords to the minimap/game panel (g_10080b84), and draws target arrows, '+N' damage text, or 'Invis' labels via sub_1003b127/wsprintfA. |
| `0x10028f6c` | `drawTileGridOverlay` | 164 | Draws a 14x18 grid of per-tile text labels over the game panel using sub_10040940 lookups and sub_1003b127 text draws, in white. |
| `0x10029010` | `drawCreatureNameHud` | 2365 | When name-HUD enabled (g_100f0e40/41), walks the on-screen creature array g_101e6ea8 (and self), maps to panel coords, and draws each creature's name/id label via wsprintfA + text draw. |
| `0x1002994d` | `decayTimerTable` | 50 | Iterates the 0x60-stride record table g_1008d2ee..g_10093cee, decrementing per-record countdown fields (+0x42, +0x5e) and clearing the entry when its counter hits zero. |
| `0x1002997f` | `syncClientLightState` | 226 | Detects changes in a client light/status table (0x63fe40 stride-4) versus a shadow copy, updates cached bytes and records GetTickCount timestamps into g_1005f811/g_1005f831 slots. |
| `0x10029a61` | `registerCreatureShadowEntry` | 218 | Finds or allocates a free slot in the creature shadow table (g_1008d2ee, stride ~0x64) by lstrcmp on name, then fills name/coords/type/flags fields via lstrcpyn and calls type-classifier subs. |
| `0x10029b3b` | `updateSelfAndTargetTracking` | 515 | Refreshes the local player pointer/name/position shadow from client globals and computes an auto-walk/attack direction toward the tracked target creature g_100f9320. |
| `0x10029d3e` | `callClientThunkWithLocal` | 16 | Thin trampoline that invokes client function pointer g_100428c5 with the arg plus a stack local, returning void. |
| `0x10029d4e` | `hookWndProcMouseKeyboard` | 836 | Replacement window/message proc (installed at 0x5b8428) that intercepts key/mouse messages, suppresses hotkeys and implements HUD drag/right-click-walk via g_10080b84 map rect and g_100f0eXX offsets. |
| `0x1002a092` | `hitTestHudButtons` | 637 | Given a mouse message, walks the HUD widget table (g_1014f420 stride ~83) resolving anchored x/y positions against the map rect and marks pressed/clicked button flags g_1008a80b/g_1008a88b. |
| `0x1002a2e7` | `sub_1002a2e7` | 2 | Empty/no-op stub (2-byte ret). |
| `0x1002a311` | `relocateInjectedStub` | 290 | Rebases a 722-byte code stub copied to g_10042668: writes prologue bytes and relocates absolute address fields by the load delta, patching pointers to g_10042674/g_1004266c/data slots. |
| `0x1002a433` | `installClientHooks` | 1380 | Core injection: VirtualProtect client sections, GlobalAlloc the relay stub, then WriteProcessMemory a series of jmp/call patches into Tibia.exe redirecting hooks to sub_10026545/sub_10029d4e etc. |
| `0x1002a997` | `sub_1002a997` | 2 | Empty no-op stub (2-byte ret). |
| `0x1002a999` | `callClientRoutineIfFlagClear` | 23 | If guard global g_1005277c is zero, calls client routine at 0x4602030. |
| `0x1002a9b0` | `onCreatureSelectStub` | 83 | Given a creature id, resolves it via sub_1003997e and compares field_a0 of self and target, but the body has no side effects (all paths return). |
| `0x1002aa03` | `hookLookCommand` | 93 | Hook trampoline: when opcode==99 (look) and look/target flags set, forwards the object id to sub_1002a9b0. |
| `0x1002aa60` | `hookUseTargetDispatch` | 87 | Hook keyed on return-address 0x4e87fc/0x4e88ed; when g_101d5e29 set, picks a nonzero id from two args and forwards to sub_1002a9b0. |
| `0x1002aab7` | `hookContainerOpen` | 80 | Hook on container/message code 8: latches g_10080b88 when a container matches the map rect (g_10080b84->field_20+10) under g_100f94ca gating. |
| `0x1002ab07` | `trackBattleListEntry` | 72 | Calls a client method on the object then, if its type field==7, appends the object pointer into the ring buffer g_100f9109[g_100f930d] (wrapping at 128). |
| `0x1002ab4f` | `hookCreatureFieldReset` | 72 | When g_1013f324 set, indexes creature record (a1*492+6606096), zeroes field_38, calls client routine 0x4d1ba0, then restores the saved pointer. |
| `0x1002ab97` | `hookConditionalClientCall` | 51 | Evaluates CPU flags and a bit test combining g_102e2a08/g_1013f27e, conditionally invoking client routine 0x45d900 (4576704). |
| `0x1002abca` | `callClientRoutine45d900` | 20 | Trampoline that calls client routine at 0x45d900. |
| `0x1002abde` | `callClientRoutine45d920` | 20 | Trampoline that calls client routine at 0x45d920 (4577568). |
| `0x1002abf2` | `hookMinimapCoordScale` | 152 | Computes scaled minimap/screen coordinates (arg*480/divisor + base) with g_100ee8d0-dependent +2/-1 zoom adjustment and writes the result through pointer arg. |
| `0x1002ac8a` | `hookCloseContextMenu` | 85 | When context menu is open (g_100ee8bb, g_1005db74) sends WM_KEYDOWN VK_ESCAPE (258/0x1b) to a resolved window to auto-close it, clearing g_1005db74. |
| `0x1002acdf` | `sendSocketGuarded` | 117 | Wraps winsock send() under critical section g_1004287d, using the override socket g_1005f555 if set else the passed socket, storing the id in g_1008b8a4. |
| `0x1002ad54` | `copy16BytesFrom74f1ac` | 35 | Copies a fixed 16-byte block from client address 0x74f1ac into the caller-supplied buffer. |
| `0x1002ad6b` | `sub_1002ad6b` | 2 |  |
| `0x1002ad79` | `formatThreeStringsAndDispatch` | 51 | lstrcpy three strings into globals g_10291cf6/g_10291ef6/g_102920f6 and calls sub_10039bbb to process them. |
| `0x1002adac` | `callClientThunk3Args` | 42 | Trampoline that stashes two extra args as locals and forwards three args to client function pointer g_100428c9. |
| `0x1002adc0` | `loadThreeStringPointers` | 17 | Loads the addresses of the three message globals (g_102920f6/g_10291cf6/g_10291ef6) into stack locals; effectively a no-op setup helper. |
| `0x1002ade7` | `injectIncomingPacket` | 136 | When map loaded and not disabled, under critical section builds a fake incoming packet in g_1004266c buffer (size from a0[0]+8) and dispatches it via stub g_10042668(1). |
| `0x1002ae6f` | `memcpyBytes` | 18 | Byte-wise memcpy: copies a2 bytes from src to dst. |
| `0x1002ae81` | `memsetZero` | 17 | Byte-wise memset-to-zero of a1 bytes at the buffer. |
| `0x1002ae92` | `findContainerItemSlot` | 176 | Scans up to 16 container records (stride 492 at 6606096) for a slot holding item id a0 (optionally matching subtype a2), returning slot index+64 or 0. |
| `0x1002af42` | `pollAllKeyStates` | 39 | Iterates virtual-key codes 0..255 calling GetAsyncKeyState and storing each into the g_1005f120 key-state shadow array. |
| `0x1002af69` | `forwardKeyChangesToDialog` | 194 | Detects async key-state changes (skipping mouse buttons), records them and posts them via SendDlgItemMessageA to the recorder dialog g_10072f84/g_1005f524. |
| `0x1002b02b` | `toggleGlobalHotkeys` | 115 | Registers or unregisters a block of global hotkeys (ids 166-183 plus 218) on window g_1005f626 via RegisterHotKey/UnregisterHotKey depending on a0. |
| `0x1002b09e` | `processHotkeyScriptEngine` | 2979 | Main hotkey/label engine loop: scans key/label/action tables, applies cooldowns and GetAsyncKeyState, expands {}//-delimited script text via sub_10030442 and dispatches commands with exception frames. |
| `0x1002b2d3` | `sub_1002b2d3` | 5 | Empty/no-op stub. |
| `0x1002b3c5` | `callSub1002b3d7` | 2 | Thin wrapper that calls the empty stub sub_1002b3d7. |
| `0x1002b3d7` | `sub_1002b3d7` | 2 | Empty/no-op stub (likely a stripped or inlined action handler). |
| `0x1002b5ba` | `sub_1002b5ba` | 5 | Empty/no-op stub. |
| `0x1002b5d9` | `sub_1002b5d9` | 5 | Empty/stub (5-byte thunk or trap-padding), no decompilable body. |
| `0x1002b661` | `sub_1002b661` | 2 | Empty/stub (2-byte), no decompilable body. |
| `0x1002b680` | `sub_1002b680` | 2 | Empty/stub (2-byte), no decompilable body. |
| `0x1002ba7b` | `sub_1002ba7b` | 5 | Empty/stub (5-byte thunk), no decompilable body. |
| `0x1002ba9a` | `sub_1002ba9a` | 5 | Empty/stub (5-byte thunk), no decompilable body. |
| `0x1002bb2a` | `sub_1002bb2a` | 2 | Empty/stub (2-byte), no decompilable body. |
| `0x1002bb58` | `sub_1002bb58` | 2 | Empty/stub (2-byte), no decompilable body. |
| `0x1002bc1e` | `sub_1002bc1e` | 2 | Empty/stub (2-byte), no decompilable body. |
| `0x1002bc68` | `runScriptTickProfiler` | 458 | Main per-tick engine step: sets g_1005dbXX profiling context blocks (labels, GetTickCount), checks arrow-key GetAsyncKeyState to set g_100ee8d8, aborts via ExitThread when g_102e2614 set, then calls sub_1002b09e. |
| `0x1002be32` | `findTileWithItemAround` | 165 | Scans the 3x3 player-centered tile grid via sub_1003a03f, walking each tile's item stack to find item id a0 (or fishable 3497-3500 when a0==-1), returning matching tile X. |
| `0x1002bed7` | `sub_1002bed7` | 97 | Opaque: mostly FPU/unsupported instructions computing a scaled value (returns v0 - 200 - v2*v2*100), likely a distance/weight formula but body undecoded. |
| `0x1002bf38` | `formatDurationHMS` | 159 | Formats a seconds count into HH:MM:SS / DdHhMmSs style string via wsprintfA, choosing colon vs letter format based on g_1013f325 and whether value exceeds a day. |
| `0x1002bfd7` | `formatThousandsGrouped` | 160 | Formats an unsigned integer with comma thousands-separators (e.g. %d,%03d,%03d) via wsprintfA, picking the group count by magnitude. |
| `0x1002c077` | `getCreatureIdField` | 84 | Parses a creature-token argument via sub_10030225 and compares it to "id" with lstrcmpi (dispatcher stub for the $creature(...).id accessor). |
| `0x1002c0cb` | `skillNameToIndex` | 235 | Maps a skill name string (fist/club/sword/axe/distance/shielding/fishing/mlevel) to its 0-7 index via lstrcmpi comparisons, returning 0 if unknown. |
| `0x1002c1b6` | `registerCommand` | 114 | insert (name,handler) into the CiroScript hash tables |
| `0x1002c228` | `evalScriptExpression` | 7792 | CiroScript expression evaluator: handles [..] arithmetic/comparison sub-expressions (parses operators * / % + - == >= <= != < > && // ? with quotes/parens) and $var.field lookups, registering ~200 variable/function accessors via sub_1002c1b6 into hash tables g_102b2404/g_102d2504, and resolving message/channel objects with lstrcmp/wsprintfA. |
| `0x1002c29f` | `sub_1002c29f` | 2 | Empty/stub (2-byte), no decompilable body. |
| `0x1002c2b8` | `sub_1002c2b8` | 2 | Empty/stub (2-byte), no decompilable body. |
| `0x1002c74e` | `sub_1002c74e` | 5 | Empty/stub (5-byte thunk), no decompilable body. |
| `0x1002c77d` | `sub_1002c77d` | 5 | Empty/stub (5-byte thunk), no decompilable body. |
| `0x1002c7ca` | `sub_1002c7ca` | 5 | Empty/stub (5-byte thunk), no decompilable body. |
| `0x1002c803` | `sub_1002c803` | 2 | Empty/stub (2-byte), no decompilable body. |
| `0x1002c84e` | `sub_1002c84e` | 2 | Empty/stub (2-byte), no decompilable body. |
| `0x1002c874` | `sub_1002c874` | 2 | Empty/stub (2-byte), no decompilable body. |
| `0x1002ca8f` | `sub_1002ca8f` | 2 | Empty/stub (2-byte), no decompilable body. |
| `0x1002caa4` | `sub_1002caa4` | 2 | Empty/stub (2-byte), no decompilable body. |
| `0x1002cad0` | `sub_1002cad0` | 2 | Empty/stub (2-byte), no decompilable body. |
| `0x1002cadc` | `sub_1002cadc` | 2 | Empty/stub (2-byte), no decompilable body. |
| `0x1002cb8e` | `getSelfMp` | 25 | $mp accessor: formats the client's current mana at 0x63fe78 into the output buffer via sub_10040940. |
| `0x1002cba2` | `getSelfMaxMp` | 20 | $maxmp accessor: formats the client's max mana at 0x63fe74 into the output buffer via sub_10040940. |
| `0x1002cbb6` | `getSelfHp` | 20 | $hp accessor: formats the client's current HP at 0x63fe94 into the output buffer via sub_10040940. |
| `0x1002cbca` | `cmd_mppc` | 45 | CiroScript command 'mppc' handler (see doc 11) |
| `0x1002cbf7` | `getSelfHpPercent` | 45 | $hppc accessor: computes HP percent (hp*100/maxhp, 100 if maxhp==0) from 0x63fe94/0x63fe90 and formats it via sub_10040940. |
| `0x1002cc24` | `getSelfMaxHp` | 20 | $maxhp accessor: formats the client's max HP at 0x63fe90 into the output buffer via sub_10040940. |
| `0x1002cc38` | `cmd_cap` | 30 | CiroScript command 'cap' handler (see doc 11) |
| `0x1002cc56` | `cmd_exp` | 20 | CiroScript command 'exp' handler (see doc 11) |
| `0x1002cc6a` | `getSelfLevel` | 20 | $level accessor: formats the client's level at 0x63fe88 into the output buffer via sub_10040940. |
| `0x1002cc7e` | `cmd_mlevel` | 20 | CiroScript command 'mlevel' handler (see doc 11) |
| `0x1002cc92` | `getSelfPosX` | 20 | $posx accessor: formats the player's X coordinate at 0x64f608 into the output buffer via sub_10040940. |
| `0x1002cca6` | `getSelfPosY` | 20 | $posy accessor: formats the player's Y coordinate at 0x64f604 into the output buffer via sub_10040940. |
| `0x1002ccba` | `getSelfPosZ` | 20 | $posz accessor: formats the player's Z coordinate at 0x64f600 into the output buffer via sub_10040940. |
| `0x1002ccce` | `cmd_soul` | 20 | CiroScript command 'soul' handler (see doc 11) |
| `0x1002cce2` | `cmd_stamina` | 20 | CiroScript command 'stamina' handler (see doc 11) |
| `0x1002ccf6` | `cmd_count` | 19 | CiroScript command 'count' handler (see doc 11) |
| `0x1002cd09` | `cmd_screenleft` | 37 | CiroScript command 'screenleft' handler (see doc 11) |
| `0x1002cd2e` | `cmd_screenright` | 40 | CiroScript command 'screenright' handler (see doc 11) |
| `0x1002cd56` | `cmd_screentop` | 37 | CiroScript command 'screentop' handler (see doc 11) |
| `0x1002cd7b` | `cmd_screenbottom` | 40 | CiroScript command 'screenbottom' handler (see doc 11) |
| `0x1002cda3` | `getSelfName` | 27 | $name accessor: copies the player's character name (g_1005f7ed+4) into the output buffer via lstrcpy when the name pointer is set. |
| `0x1002cdbe` | `cmd_time` | 28 | CiroScript command 'time' handler (see doc 11) |
| `0x1002cdda` | `cmd_timems` | 19 | CiroScript command 'timems' handler (see doc 11) |
| `0x1002cded` | `cmd_deltatime` | 34 | CiroScript command 'deltatime' handler (see doc 11) |
| `0x1002ce0f` | `cmd_deltatimems` | 25 | CiroScript command 'deltatimems' handler (see doc 11) |
| `0x1002ce28` | `cmd_return` | 18 | CiroScript command 'return' handler (see doc 11) |
| `0x1002ce3a` | `cmd_exptnl` | 36 | CiroScript command 'exptnl' handler (see doc 11) |
| `0x1002ce5e` | `cmd_exph` | 19 | CiroScript command 'exph' handler (see doc 11) |
| `0x1002ce71` | `cmd_expgained` | 39 | CiroScript command 'expgained' handler (see doc 11) |
| `0x1002ce98` | `cmd_timetnl` | 96 | CiroScript command 'timetnl' handler (see doc 11) |
| `0x1002cef8` | `cmd_exptolevel` | 52 | CiroScript command 'exptolevel' handler (see doc 11) |
| `0x1002cf2c` | `cmd_timetolevel` | 112 | CiroScript command 'timetolevel' handler (see doc 11) |
| `0x1002cf9c` | `cmd_screencount` | 116 | CiroScript command 'screencount' handler (see doc 11) |
| `0x1002d010` | `cmd_mcount` | 272 | CiroScript command 'mcount' handler (see doc 11) |
| `0x1002d049` | `sub_1002d049` | 2 | Empty/stub (2-byte), no decompilable body. |
| `0x1002d122` | `cmd_pcount` | 272 | CiroScript command 'pcount' handler (see doc 11) |
| `0x1002d15b` | `sub_1002d15b` | 2 | Empty/stub (2-byte), no decompilable body. |
| `0x1002d234` | `cmd_monstersaround` | 140 | CiroScript command 'monstersaround' handler (see doc 11) |
| `0x1002d2c0` | `cmd_playersaround` | 148 | CiroScript command 'playersaround' handler (see doc 11) |
| `0x1002d354` | `formatBoolFlagChar0` | 53 | Sets output char to '0' or '1' based on the boolean result of sub_100303be, writing a CiroScript-style flag string. |
| `0x1002d389` | `formatBoolFlagChar1` | 53 | Sets output char to '0' or '1' based on the boolean result of predicate sub_1003a320, writing a flag string. |
| `0x1002d3be` | `formatBoolFlagChar2` | 53 | Sets output char to '0' or '1' based on the boolean result of predicate sub_1003a3da, writing a flag string. |
| `0x1002d3f3` | `formatBoolFlagChar3` | 53 | Sets output char to '0' or '1' based on the boolean result of predicate sub_1003a494, writing a flag string. |
| `0x1002d428` | `formatBoolFlagChar4` | 53 | Sets output char to '0' or '1' based on the boolean result of predicate sub_1003a550, writing a flag string. |
| `0x1002d45d` | `cmd_sbtime` | 28 | CiroScript command 'sbtime' handler (see doc 11) |
| `0x1002d479` | `cmd_sstime` | 28 | CiroScript command 'sstime' handler (see doc 11) |
| `0x1002d495` | `cmd_exectime` | 19 | CiroScript command 'exectime' handler (see doc 11) |
| `0x1002d4a8` | `cmd_synctime` | 24 | CiroScript command 'synctime' handler (see doc 11) |
| `0x1002d4c0` | `cmd_fired` | 19 | CiroScript command 'fired' handler (see doc 11) |
| `0x1002d4d3` | `cmd_formattime` | 99 | CiroScript command 'formattime' handler (see doc 11) |
| `0x1002d536` | `cmd_formatnum` | 26 | CiroScript command 'formatnum' handler (see doc 11) |
| `0x1002d550` | `cmd_ringslot` | 32 | CiroScript command 'ringslot' handler (see doc 11) |
| `0x1002d570` | `cmd_beltslot` | 32 | CiroScript command 'beltslot' handler (see doc 11) |
| `0x1002d590` | `cmd_backslot` | 32 | CiroScript command 'backslot' handler (see doc 11) |
| `0x1002d5b0` | `cmd_rhandslot` | 32 | CiroScript command 'rhandslot' handler (see doc 11) |
| `0x1002d5d0` | `cmd_lhandslot` | 32 | CiroScript command 'lhandslot' handler (see doc 11) |
| `0x1002d5f0` | `cmd_amuletslot` | 32 | CiroScript command 'amuletslot' handler (see doc 11) |
| `0x1002d610` | `cmd_bootsslot` | 32 | CiroScript command 'bootsslot' handler (see doc 11) |
| `0x1002d630` | `cmd_headslot` | 32 | CiroScript command 'headslot' handler (see doc 11) |
| `0x1002d650` | `cmd_chestslot` | 32 | CiroScript command 'chestslot' handler (see doc 11) |
| `0x1002d670` | `cmd_legsslot` | 32 | CiroScript command 'legsslot' handler (see doc 11) |
| `0x1002d690` | `cmd_topitem` | 99 | CiroScript command 'topitem' handler (see doc 11) |
| `0x1002d6f3` | `cmd_istileitem` | 140 | CiroScript command 'istileitem' handler (see doc 11) |
| `0x1002d77f` | `cmd_poisoned` | 25 | CiroScript command 'poisoned' handler (see doc 11) |
| `0x1002d798` | `cmd_poisondmg` | 34 | CiroScript command 'poisondmg' handler (see doc 11) |
| `0x1002d7ba` | `cmd_manashielded` | 25 | CiroScript command 'manashielded' handler (see doc 11) |
| `0x1002d7d3` | `cmd_battlesign` | 25 | CiroScript command 'battlesign' handler (see doc 11) |
| `0x1002d7ec` | `cmd_redbattlesign` | 25 | CiroScript command 'redbattlesign' handler (see doc 11) |
| `0x1002d805` | `cmd_drunk` | 25 | CiroScript command 'drunk' handler (see doc 11) |
| `0x1002d81e` | `cmd_hasted` | 25 | CiroScript command 'hasted' handler (see doc 11) |
| `0x1002d837` | `cmd_paralyzed` | 25 | CiroScript command 'paralyzed' handler (see doc 11) |
| `0x1002d850` | `cmd_inpz` | 25 | CiroScript command 'inpz' handler (see doc 11) |
| `0x1002d869` | `cmd_navion` | 25 | CiroScript command 'navion' handler (see doc 11) |
| `0x1002d882` | `cmd_itemcount` | 83 | CiroScript command 'itemcount' handler (see doc 11) |
| `0x1002d8d5` | `cmd_winitemcount` | 86 | CiroScript command 'winitemcount' handler (see doc 11) |
| `0x1002d92b` | `cmd_fileisline` | 89 | CiroScript command 'fileisline' handler (see doc 11) |
| `0x1002d984` | `cmd_rand` | 87 | CiroScript command 'rand' handler (see doc 11) |
| `0x1002d9db` | `cmd_fileline` | 56 | CiroScript command 'fileline' handler (see doc 11) |
| `0x1002da13` | `cmd_token` | 203 | CiroScript command 'token' handler (see doc 11) |
| `0x1002dabe` | `sub_1002dabe` | 2 | Empty/no-op stub function with no body. |
| `0x1002dae0` | `cmd_filerandomline` | 31 | CiroScript command 'filerandomline' handler (see doc 11) |
| `0x1002daff` | `cmd_connected` | 35 | CiroScript command 'connected' handler (see doc 11) |
| `0x1002db22` | `cmd_pkname` | 18 | CiroScript command 'pkname' handler (see doc 11) |
| `0x1002db34` | `cmd_ping` | 19 | CiroScript command 'ping' handler (see doc 11) |
| `0x1002db47` | `cmd_fps` | 39 | CiroScript command 'fps' handler (see doc 11) |
| `0x1002db6e` | `cmd_enemycount` | 90 | CiroScript command 'enemycount' handler (see doc 11) |
| `0x1002dbc8` | `cmd_friendcount` | 90 | CiroScript command 'friendcount' handler (see doc 11) |
| `0x1002dc22` | `cmd_fishspots` | 26 | CiroScript command 'fishspots' handler (see doc 11) |
| `0x1002dc3c` | `cmd_waypointson` | 21 | CiroScript command 'waypointson' handler (see doc 11) |
| `0x1002dc51` | `cmd_targetingon` | 21 | CiroScript command 'targetingon' handler (see doc 11) |
| `0x1002dc66` | `cmd_autocomboon` | 21 | CiroScript command 'autocomboon' handler (see doc 11) |
| `0x1002dc7b` | `cmd_mshieldtime` | 26 | CiroScript command 'mshieldtime' handler (see doc 11) |
| `0x1002dc95` | `cmd_hastetime` | 26 | CiroScript command 'hastetime' handler (see doc 11) |
| `0x1002dcaf` | `cmd_strengthtime` | 26 | CiroScript command 'strengthtime' handler (see doc 11) |
| `0x1002dcc9` | `cmd_invistime` | 26 | CiroScript command 'invistime' handler (see doc 11) |
| `0x1002dce3` | `cmd_invisible` | 34 | CiroScript command 'invisible' handler (see doc 11) |
| `0x1002dd05` | `cmd_dmgs` | 19 | CiroScript command 'dmgs' handler (see doc 11) |
| `0x1002dd18` | `cmd_lastdmg` | 19 | CiroScript command 'lastdmg' handler (see doc 11) |
| `0x1002dd2b` | `cmd_lastdmgtype` | 19 | CiroScript command 'lastdmgtype' handler (see doc 11) |
| `0x1002dd3e` | `cmd_idlerecvtime` | 25 | CiroScript command 'idlerecvtime' handler (see doc 11) |
| `0x1002dd57` | `cmd_standtime` | 25 | CiroScript command 'standtime' handler (see doc 11) |
| `0x1002dd70` | `cmd_lastdmgtime` | 36 | CiroScript command 'lastdmgtime' handler (see doc 11) |
| `0x1002dd94` | `cmd_islooting` | 30 | CiroScript command 'islooting' handler (see doc 11) |
| `0x1002ddb2` | `cmd_lastdmgername` | 20 | CiroScript command 'lastdmgername' handler (see doc 11) |
| `0x1002ddc6` | `cmd_squaretime` | 19 | CiroScript command 'squaretime' handler (see doc 11) |
| `0x1002ddef` | `getTimeFormatThunk` | 10 | Thin wrapper forwarding args to the Win32 GetTimeFormatA API to format a time value into a string. |
| `0x1002de0f` | `getDateFormatThunk` | 10 | Thin wrapper forwarding args to the Win32 GetDateFormatA API to format a date value into a string. |
| `0x1002de19` | `cmd_cutstr` | 20 | CiroScript command 'cutstr' handler (see doc 11) |
| `0x1002de28` | `copySubstringBounded` | 126 | Copies up to a computed length of chars from a source buffer (offset by sub_100300ce results) into a destination and null-terminates it. |
| `0x1002deab` | `cmd_creature` | 64 | CiroScript command 'creature' handler (see doc 11) |
| `0x1002deeb` | `cmd_mostexposed` | 52 | CiroScript command 'mostexposed' handler (see doc 11) |
| `0x1002df1f` | `cmd_mostexposedcount` | 54 | CiroScript command 'mostexposedcount' handler (see doc 11) |
| `0x1002df55` | `cmd_mostshot` | 52 | CiroScript command 'mostshot' handler (see doc 11) |
| `0x1002df89` | `cmd_mostshotcount` | 54 | CiroScript command 'mostshotcount' handler (see doc 11) |
| `0x1002dfbf` | `cmd_ctrl` | 27 | CiroScript command 'ctrl' handler (see doc 11) |
| `0x1002dfda` | `cmd_shift` | 27 | CiroScript command 'shift' handler (see doc 11) |
| `0x1002dff5` | `cmd_alt` | 27 | CiroScript command 'alt' handler (see doc 11) |
| `0x1002e010` | `cmd_key` | 43 | CiroScript command 'key' handler (see doc 11) |
| `0x1002e03b` | `cmd_skill` | 66 | CiroScript command 'skill' handler (see doc 11) |
| `0x1002e07d` | `cmd_skillpc` | 80 | CiroScript command 'skillpc' handler (see doc 11) |
| `0x1002e0cd` | `cmd_skilltime` | 168 | CiroScript command 'skilltime' handler (see doc 11) |
| `0x1002e175` | `cmd_lastmsg` | 11 | CiroScript command 'lastmsg' handler (see doc 11) |
| `0x1002e180` | `cmd_lastnavmsg` | 11 | CiroScript command 'lastnavmsg' handler (see doc 11) |
| `0x1002e18b` | `cmd_curmsg` | 114 | CiroScript command 'curmsg' handler (see doc 11) |
| `0x1002e1fd` | `cmd_target` | 41 | CiroScript command 'target' handler (see doc 11) |
| `0x1002e226` | `cmd_lastdmger` | 36 | CiroScript command 'lastdmger' handler (see doc 11) |
| `0x1002e24a` | `cmd_self` | 11 | CiroScript command 'self' handler (see doc 11) |
| `0x1002e255` | `cmd_followed` | 39 | CiroScript command 'followed' handler (see doc 11) |
| `0x1002e27c` | `cmd_attacked` | 38 | CiroScript command 'attacked' handler (see doc 11) |
| `0x1002e2a2` | `cmd_pk` | 18 | CiroScript command 'pk' handler (see doc 11) |
| `0x1002e2b4` | `cmd_pattacker` | 17 | CiroScript command 'pattacker' handler (see doc 11) |
| `0x1002e2c5` | `cmd_mattacker` | 17 | CiroScript command 'mattacker' handler (see doc 11) |
| `0x1002e2d6` | `cmd_attacker` | 17 | CiroScript command 'attacker' handler (see doc 11) |
| `0x1002e2ea` | `callHelper38eb3_a` | 15 | Thin wrapper calling sub_10038eb3 with second arg 0. |
| `0x1002e2fc` | `callHelper38eb3_b` | 15 | Thin wrapper calling sub_10038eb3 with second arg 0. |
| `0x1002e30e` | `callHelper38eb3_c` | 15 | Thin wrapper calling sub_10038eb3 with second arg 0. |
| `0x1002e320` | `callHelper38eb3_d` | 15 | Thin wrapper calling sub_10038eb3 with second arg 0. |
| `0x1002e332` | `callHelper38eb3_e` | 15 | Thin wrapper calling sub_10038eb3 with second arg 0. |
| `0x1002e344` | `callHelper38eb3_f` | 15 | Thin wrapper calling sub_10038eb3 with second arg 0. |
| `0x1002e353` | `cmd_coretarget` | 8 | CiroScript command 'coretarget' handler (see doc 11) |
| `0x1002e35e` | `callHelper235e8` | 9 | Thin wrapper forwarding to sub_100235e8. |
| `0x1002e36a` | `callHelper235e8Then2355e` | 20 | Calls sub_100235e8 and, if it returns nonzero, invokes sub_1002355e as a follow-up action. |
| `0x1002e460` | `cmd_name` | 19 | CiroScript command 'name' handler (see doc 11) |
| `0x1002e473` | `cmd_id` | 25 | CiroScript command 'id' handler (see doc 11) |
| `0x1002e48c` | `cmd_posx` | 26 | CiroScript command 'posx' handler (see doc 11) |
| `0x1002e4a6` | `cmd_distance` | 57 | CiroScript command 'distance' handler (see doc 11) |
| `0x1002e4df` | `cmd_distx` | 37 | CiroScript command 'distx' handler (see doc 11) |
| `0x1002e504` | `cmd_disty` | 37 | CiroScript command 'disty' handler (see doc 11) |
| `0x1002e529` | `cmd_posy` | 26 | CiroScript command 'posy' handler (see doc 11) |
| `0x1002e543` | `cmd_posz` | 26 | CiroScript command 'posz' handler (see doc 11) |
| `0x1002e55d` | `cmd_dir` | 26 | CiroScript command 'dir' handler (see doc 11) |
| `0x1002e577` | `cmd_outfit` | 26 | CiroScript command 'outfit' handler (see doc 11) |
| `0x1002e591` | `cmd_hppc` | 29 | CiroScript command 'hppc' handler (see doc 11) |
| `0x1002e5ae` | `cmd_speed` | 29 | CiroScript command 'speed' handler (see doc 11) |
| `0x1002e5cb` | `cmd_isparalyzed` | 32 | CiroScript command 'isparalyzed' handler (see doc 11) |
| `0x1002e5eb` | `cmd_color1` | 26 | CiroScript command 'color1' handler (see doc 11) |
| `0x1002e605` | `cmd_color2` | 26 | CiroScript command 'color2' handler (see doc 11) |
| `0x1002e61f` | `cmd_color3` | 26 | CiroScript command 'color3' handler (see doc 11) |
| `0x1002e639` | `cmd_color4` | 26 | CiroScript command 'color4' handler (see doc 11) |
| `0x1002e653` | `cmd_skull` | 29 | CiroScript command 'skull' handler (see doc 11) |
| `0x1002e670` | `cmd_party` | 29 | CiroScript command 'party' handler (see doc 11) |
| `0x1002e68d` | `cmd_warbanner` | 29 | CiroScript command 'warbanner' handler (see doc 11) |
| `0x1002e6aa` | `cmd_ismonster` | 26 | CiroScript command 'ismonster' handler (see doc 11) |
| `0x1002e6c4` | `cmd_isnpc` | 41 | CiroScript command 'isnpc' handler (see doc 11) |
| `0x1002e6ed` | `cmd_isplayer` | 26 | CiroScript command 'isplayer' handler (see doc 11) |
| `0x1002e707` | `cmd_isonscreen` | 30 | CiroScript command 'isonscreen' handler (see doc 11) |
| `0x1002e725` | `cmd_isshootable` | 50 | CiroScript command 'isshootable' handler (see doc 11) |
| `0x1002e757` | `cmd_canshoot` | 93 | CiroScript command 'canshoot' handler (see doc 11) |
| `0x1002e7b4` | `cmd_isenemy` | 33 | CiroScript command 'isenemy' handler (see doc 11) |
| `0x1002e7d5` | `cmd_isonnavi` | 31 | CiroScript command 'isonnavi' handler (see doc 11) |
| `0x1002e7f4` | `cmd_isleader` | 33 | CiroScript command 'isleader' handler (see doc 11) |
| `0x1002e815` | `cmd_isfriend` | 33 | CiroScript command 'isfriend' handler (see doc 11) |
| `0x1002e836` | `cmd_issubenemy` | 33 | CiroScript command 'issubenemy' handler (see doc 11) |
| `0x1002e857` | `cmd_issubfriend` | 33 | CiroScript command 'issubfriend' handler (see doc 11) |
| `0x1002e878` | `cmd_haslookinfo` | 39 | CiroScript command 'haslookinfo' handler (see doc 11) |
| `0x1002e89f` | `cmd_guild` | 26 | CiroScript command 'guild' handler (see doc 11) |
| `0x1002e8b9` | `cmd_voc` | 30 | CiroScript command 'voc' handler (see doc 11) |
| `0x1002e8d7` | `cmd_vocation` | 33 | CiroScript command 'vocation' handler (see doc 11) |
| `0x1002e8f8` | `cmd_level` | 25 | CiroScript command 'level' handler (see doc 11) |
| `0x1002e911` | `cmd_isknight` | 39 | CiroScript command 'isknight' handler (see doc 11) |
| `0x1002e938` | `cmd_ispaladin` | 39 | CiroScript command 'ispaladin' handler (see doc 11) |
| `0x1002e95f` | `cmd_issorcerer` | 39 | CiroScript command 'issorcerer' handler (see doc 11) |
| `0x1002e986` | `cmd_isdruid` | 39 | CiroScript command 'isdruid' handler (see doc 11) |
| `0x1002e9ad` | `cmd_ismage` | 50 | CiroScript command 'ismage' handler (see doc 11) |
| `0x1002e9df` | `cmd_maxhp` | 27 | CiroScript command 'maxhp' handler (see doc 11) |
| `0x1002e9fa` | `cmd_hp` | 27 | CiroScript command 'hp' handler (see doc 11) |
| `0x1002ea15` | `cmd_maxmp` | 53 | CiroScript command 'maxmp' handler (see doc 11) |
| `0x1002ea4a` | `cmd_mp` | 59 | CiroScript command 'mp' handler (see doc 11) |
| `0x1002ea85` | `cmd_attackedme` | 36 | CiroScript command 'attackedme' handler (see doc 11) |
| `0x1002eaa9` | `cmd_exposedcount` | 33 | CiroScript command 'exposedcount' handler (see doc 11) |
| `0x1002eaca` | `cmd_shotcount` | 33 | CiroScript command 'shotcount' handler (see doc 11) |
| `0x1002f0b6` | `sub_1002f0b6` | 5 | Empty/no-op stub function. |
| `0x1002f0d3` | `sub_1002f0d3` | 5 | Empty/no-op stub function. |
| `0x1002f0f0` | `sub_1002f0f0` | 5 | Empty/no-op stub function. |
| `0x1002f10d` | `sub_1002f10d` | 5 | Empty/no-op stub function. |
| `0x1002f12a` | `sub_1002f12a` | 5 | Empty/no-op stub function. |
| `0x1002f158` | `sub_1002f158` | 5 | Empty/no-op stub function. |
| `0x1002f179` | `sub_1002f179` | 2 | Empty/no-op stub function. |
| `0x1002f193` | `sub_1002f193` | 2 | Empty/no-op stub function. |
| `0x1002f1ad` | `sub_1002f1ad` | 2 | Empty/no-op stub function. |
| `0x1002f1c7` | `sub_1002f1c7` | 2 | Empty/no-op stub function. |
| `0x1002f269` | `sub_1002f269` | 5 | Empty/no-op stub function. |
| `0x1002f294` | `sub_1002f294` | 5 | Empty/no-op stub function. |
| `0x1002f2bf` | `sub_1002f2bf` | 5 | Empty/no-op stub function. |
| `0x1002f2f3` | `sub_1002f2f3` | 5 | Empty/no-op stub function. |
| `0x1002f324` | `sub_1002f324` | 5 | Empty/no-op stub function. |
| `0x1002f349` | `sub_1002f349` | 5 | Empty/no-op stub function. |
| `0x1002f374` | `sub_1002f374` | 2 | Empty/no-op stub function. |
| `0x1002f39c` | `sub_1002f39c` | 2 | Empty/no-op stub function. |
| `0x1002f3c4` | `sub_1002f3c4` | 2 | Empty/no-op stub function. |
| `0x1002f442` | `sub_1002f442` | 2 | Empty/no-op stub function. |
| `0x1002ff85` | `sub_1002ff85` | 2 | Empty return-only stub function. |
| `0x1002ff87` | `toLowerCharInPlace` | 27 | Lowercases a single ASCII character in place (A-Z -> a-z), returning early at the string terminator; a tolower helper. |
| `0x1002ffa2` | `sub_1002ffa2` | 1 | Empty return-only stub function. |
| `0x1002ffa3` | `queueClientActionForTopTarget` | 81 | Stores param into g_100433f1, then based on which of two client globals (0x64ccb0/0x64cd04) is set picks an action type (3 or 10) and calls sub_1002ade7 to enqueue it. |
| `0x1002fff4` | `lookupNameInTable` | 87 | Strips trailing 's', then case-insensitively (lstrcmpi) scans a 40-byte-stride table at g_100ec0b6 (up to 256 entries) returning the matched record's field_24 id. |
| `0x10030027` | `sub_10030027` | 2 | Empty/stub function with no body. |
| `0x1003004d` | `iterateChannelAndSlotTables` | 129 | Walks 16 channel records (492-byte stride from 0x64cd10) skipping subentries, then 10 records (12-byte stride from 0x64cb98); loop bodies are essentially no-ops in this slice. |
| `0x100300ce` | `parseExpressionOrRange` | 337 | Skips spaces and dispatches on the first char: '$'/'[' to variable expansion, quotes to sub_10030225, or copies a token and if it contains '..' evaluates both sides as a numeric range via sub_10040900/sub_10040a30. |
| `0x100300f3` | `sub_100300f3` | 2 | Empty/stub function with no body. |
| `0x10030121` | `sub_10030121` | 2 | Empty/stub function with no body. |
| `0x10030164` | `sub_10030164` | 2 | Empty/stub function with no body. |
| `0x10030225` | `expandQuotedAndVariables` | 244 | Recursively unescapes a token: handles quote toggling, '$$'/'[[' literal escapes, and recurses on '$'/'[' variable/substitution markers, collapsing unquoted spaces into the output buffer. |
| `0x10030236` | `sub_10030236` | 2 | Empty/stub function with no body. |
| `0x10030285` | `sub_10030285` | 5 | Empty/stub function with no body. |
| `0x100302bc` | `sub_100302bc` | 2 | Empty/stub function with no body. |
| `0x100302eb` | `sub_100302eb` | 2 | Empty/stub function with no body. |
| `0x100302fe` | `sub_100302fe` | 2 | Empty/stub function with no body. |
| `0x10030326` | `extractQuotedToken` | 148 | Extracts one script token: if it starts with '$' copies the whole word via lstrcpy, otherwise strips matching quotes and collapses whitespace, writing a null-terminated result. |
| `0x10030337` | `sub_10030337` | 2 | Empty/stub function with no body. |
| `0x10030396` | `sub_10030396` | 2 | Empty/stub function with no body. |
| `0x100303be` | `findNameInCsvList` | 130 | Iterates a comma-separated list at g_10134e6b, trimming leading/trailing spaces of each item, and returns true (1) when an item case-insensitively matches the argument via lstrcmpi. |
| `0x100303f1` | `sub_100303f1` | 2 | Empty/stub function with no body. |
| `0x10030442` | `registerCommands_table` | 4493 | register the CiroScript command handlers |
| `0x100304be` | `sub_100304be` | 5 | Empty/stub function with no body. |
| `0x10030503` | `sub_10030503` | 2 | Empty/stub function with no body. |
| `0x10030526` | `sub_10030526` | 5 | Empty/stub function with no body. |
| `0x10030550` | `sub_10030550` | 2 | Empty/stub function with no body. |
| `0x10030575` | `sub_10030575` | 5 | Empty/stub function with no body. |
| `0x100305b9` | `sub_100305b9` | 2 | Empty/stub function with no body. |
| `0x100305e2` | `sub_100305e2` | 2 | Empty/stub function with no body. |
| `0x1003068a` | `cmd_gotolabel` | 132 | CiroScript command 'gotolabel' handler (see doc 11) |
| `0x1003070e` | `cmd_islocation` | 70 | CiroScript command 'islocation' handler (see doc 11) |
| `0x10030754` | `cmd_isdistance` | 101 | CiroScript command 'isdistance' handler (see doc 11) |
| `0x100307b9` | `cmd_isnotdistance` | 101 | CiroScript command 'isnotdistance' handler (see doc 11) |
| `0x1003081e` | `cmd_isnotlocation` | 70 | CiroScript command 'isnotlocation' handler (see doc 11) |
| `0x10030864` | `cmd_skip` | 20 | CiroScript command 'skip' handler (see doc 11) |
| `0x10030878` | `cmd_wait` | 71 | CiroScript command 'wait' handler (see doc 11) |
| `0x100308bf` | `cmd_refillammo` | 249 | CiroScript command 'refillammo' handler (see doc 11) |
| `0x100309b8` | `cmd_countolditems` | 373 | CiroScript command 'countolditems' handler (see doc 11) |
| `0x10030a3e` | `cmd_sspecial` | 29 | CiroScript command 'sspecial' handler (see doc 11) |
| `0x10030a5b` | `cmd_countitems` | 18 | CiroScript command 'countitems' handler (see doc 11) |
| `0x10030b5c` | `cmd_getcount` | 34 | CiroScript command 'getcount' handler (see doc 11) |
| `0x10030b7e` | `cmd_countitemsvisible` | 25 | CiroScript command 'countitemsvisible' handler (see doc 11) |
| `0x10030b97` | `cmd_uh` | 181 | CiroScript command 'uh' handler (see doc 11) |
| `0x10030c4c` | `cmd_ihpc` | 194 | CiroScript command 'ihpc' handler (see doc 11) |
| `0x10030d0e` | `cmd_sd` | 66 | CiroScript command 'sd' handler (see doc 11) |
| `0x10030d50` | `cmd_displaymap` | 80 | CiroScript command 'displaymap' handler (see doc 11) |
| `0x10030da0` | `cmd_altnavdisplay` | 80 | CiroScript command 'altnavdisplay' handler (see doc 11) |
| `0x10030df0` | `cmd_hmm` | 66 | CiroScript command 'hmm' handler (see doc 11) |
| `0x10030e32` | `cmd_lmm` | 66 | CiroScript command 'lmm' handler (see doc 11) |
| `0x10030e74` | `cmd_icicle` | 66 | CiroScript command 'icicle' handler (see doc 11) |
| `0x10030eb6` | `cmd_stalagmite` | 66 | CiroScript command 'stalagmite' handler (see doc 11) |
| `0x10030ef8` | `cmd_aimtype` | 70 | CiroScript command 'aimtype' handler (see doc 11) |
| `0x10030f3e` | `cmd_explo` | 66 | CiroScript command 'explo' handler (see doc 11) |
| `0x10030f80` | `cmd_autoaim` | 56 | CiroScript command 'autoaim' handler (see doc 11) |
| `0x10030fb8` | `cmd_follow` | 109 | CiroScript command 'follow' handler (see doc 11) |
| `0x10031025` | `cmd_attack` | 115 | CiroScript command 'attack' handler (see doc 11) |
| `0x10031098` | `cmd_whitebox` | 48 | CiroScript command 'whitebox' handler (see doc 11) |
| `0x100310c8` | `cmd_ignoretarget` | 125 | CiroScript command 'ignoretarget' handler (see doc 11) |
| `0x10031145` | `cmd_stopattack` | 99 | CiroScript command 'stopattack' handler (see doc 11) |
| `0x100311a8` | `cmd_setattackmode` | 272 | CiroScript command 'setattackmode' handler (see doc 11) |
| `0x100312b8` | `cmd_autoheal` | 160 | CiroScript command 'autoheal' handler (see doc 11) |
| `0x10031358` | `cmd_equipammy` | 70 | CiroScript command 'equipammy' handler (see doc 11) |
| `0x1003139e` | `cmd_fastequipammy` | 61 | CiroScript command 'fastequipammy' handler (see doc 11) |
| `0x100313db` | `cmd_equipring` | 124 | CiroScript command 'equipring' handler (see doc 11) |
| `0x10031457` | `cmd_equipsring` | 96 | CiroScript command 'equipsring' handler (see doc 11) |
| `0x100314b7` | `cmd_equipboots` | 115 | CiroScript command 'equipboots' handler (see doc 11) |
| `0x1003152a` | `cmd_equiphelm` | 88 | CiroScript command 'equiphelm' handler (see doc 11) |
| `0x10031582` | `cmd_equipchest` | 88 | CiroScript command 'equipchest' handler (see doc 11) |
| `0x100315da` | `cmd_equiphead` | 88 | CiroScript command 'equiphead' handler (see doc 11) |
| `0x10031632` | `cmd_equiplegs` | 88 | CiroScript command 'equiplegs' handler (see doc 11) |
| `0x1003168a` | `cmd_equiprhand` | 124 | CiroScript command 'equiprhand' handler (see doc 11) |
| `0x10031706` | `cmd_equiplhand` | 124 | CiroScript command 'equiplhand' handler (see doc 11) |
| `0x10031782` | `cmd_equipbelt` | 124 | CiroScript command 'equipbelt' handler (see doc 11) |
| `0x100317fe` | `cmd_equipback` | 88 | CiroScript command 'equipback' handler (see doc 11) |
| `0x10031856` | `cmd_say` | 79 | CiroScript command 'say' handler (see doc 11) |
| `0x100318a5` | `cmd_allowwalk` | 31 | CiroScript command 'allowwalk' handler (see doc 11) |
| `0x100318c4` | `cmd_disallowwalk` | 31 | CiroScript command 'disallowwalk' handler (see doc 11) |
| `0x100318e3` | `cmd_setalarm` | 247 | CiroScript command 'setalarm' handler (see doc 11) |
| `0x100319da` | `cmd_flash` | 14 | CiroScript command 'flash' handler (see doc 11) |
| `0x100319ea` | `triggerAction1` | 11 | Thin wrapper that calls sub_10040318 with constant argument 1. |
| `0x100319f5` | `cmd_savescreen` | 43 | CiroScript command 'savescreen' handler (see doc 11) |
| `0x10031a20` | `cmd_changestance` | 289 | CiroScript command 'changestance' handler (see doc 11) |
| `0x10031b41` | `cmd_npcsay` | 79 | CiroScript command 'npcsay' handler (see doc 11) |
| `0x10031b90` | `cmd_gamesay` | 81 | CiroScript command 'gamesay' handler (see doc 11) |
| `0x10031be1` | `cmd_tradesay` | 81 | CiroScript command 'tradesay' handler (see doc 11) |
| `0x10031c32` | `cmd_rlsay` | 81 | CiroScript command 'rlsay' handler (see doc 11) |
| `0x10031c83` | `cmd_helpsay` | 81 | CiroScript command 'helpsay' handler (see doc 11) |
| `0x10031cd4` | `cmd_guildsay` | 81 | CiroScript command 'guildsay' handler (see doc 11) |
| `0x10031d25` | `cmd_sayin` | 147 | CiroScript command 'sayin' handler (see doc 11) |
| `0x10031db8` | `cmd_navsay` | 77 | CiroScript command 'navsay' handler (see doc 11) |
| `0x10031e05` | `cmd_setautocombo` | 119 | CiroScript command 'setautocombo' handler (see doc 11) |
| `0x10031e7c` | `cmd_statusmessage` | 30 | CiroScript command 'statusmessage' handler (see doc 11) |
| `0x10031e9a` | `cmd_settradeoptions` | 208 | CiroScript command 'settradeoptions' handler (see doc 11) |
| `0x10031f6a` | `cmd_buyitems` | 185 | CiroScript command 'buyitems' handler (see doc 11) |
| `0x10032023` | `cmd_buyitemsupto` | 223 | CiroScript command 'buyitemsupto' handler (see doc 11) |
| `0x10032102` | `cmd_sellitemsdownto` | 152 | CiroScript command 'sellitemsdownto' handler (see doc 11) |
| `0x1003219a` | `cmd_sellitems` | 116 | CiroScript command 'sellitems' handler (see doc 11) |
| `0x1003220e` | `cmd_mana` | 140 | CiroScript command 'mana' handler (see doc 11) |
| `0x10032219` | `cmd_smana` | 11 | CiroScript command 'smana' handler (see doc 11) |
| `0x10032224` | `cmd_gmana` | 11 | CiroScript command 'gmana' handler (see doc 11) |
| `0x1003222f` | `cmd_gsmana` | 11 | CiroScript command 'gsmana' handler (see doc 11) |
| `0x100322bb` | `cmd_health` | 139 | CiroScript command 'health' handler (see doc 11) |
| `0x100322c6` | `cmd_shealth` | 11 | CiroScript command 'shealth' handler (see doc 11) |
| `0x100322d1` | `cmd_ghealth` | 11 | CiroScript command 'ghealth' handler (see doc 11) |
| `0x100322dc` | `cmd_uhealth` | 11 | CiroScript command 'uhealth' handler (see doc 11) |
| `0x100322e7` | `cmd_gshealth` | 11 | CiroScript command 'gshealth' handler (see doc 11) |
| `0x10032372` | `cmd_retarget` | 145 | CiroScript command 'retarget' handler (see doc 11) |
| `0x10032403` | `cmd_pm` | 48 | CiroScript command 'pm' handler (see doc 11) |
| `0x10032433` | `cmd_auto` | 246 | CiroScript command 'auto' handler (see doc 11) |
| `0x10032529` | `cmd_end` | 48 | CiroScript command 'end' handler (see doc 11) |
| `0x10032559` | `cmd_break` | 32 | CiroScript command 'break' handler (see doc 11) |
| `0x10032579` | `cmd_turnoff` | 28 | CiroScript command 'turnoff' handler (see doc 11) |
| `0x10032595` | `cmd_reconnect` | 9 | CiroScript command 'reconnect' handler (see doc 11) |
| `0x1003259e` | `cmd_connect` | 255 | CiroScript command 'connect' handler (see doc 11) |
| `0x1003269d` | `cmd_setpos` | 56 | CiroScript command 'setpos' handler (see doc 11) |
| `0x100326d5` | `cmd_listboxsetup` | 145 | CiroScript command 'listboxsetup' handler (see doc 11) |
| `0x10032766` | `cmd_listboxaddline` | 157 | CiroScript command 'listboxaddline' handler (see doc 11) |
| `0x10032803` | `cmd_setcolor` | 74 | CiroScript command 'setcolor' handler (see doc 11) |
| `0x1003284d` | `cmd_displaytext` | 47 | CiroScript command 'displaytext' handler (see doc 11) |
| `0x1003287c` | `cmd_listas` | 51 | CiroScript command 'listas' handler (see doc 11) |
| `0x100328af` | `cmd_dontlist` | 24 | CiroScript command 'dontlist' handler (see doc 11) |
| `0x100328c7` | `cmd_sio` | 147 | CiroScript command 'sio' handler (see doc 11) |
| `0x1003295a` | `cmd_usegrounditem` | 77 | CiroScript command 'usegrounditem' handler (see doc 11) |
| `0x100329a7` | `cmd_opengrounditem` | 97 | CiroScript command 'opengrounditem' handler (see doc 11) |
| `0x10032a08` | `cmd_playsound` | 30 | CiroScript command 'playsound' handler (see doc 11) |
| `0x10032a26` | `cmd_useitem` | 69 | CiroScript command 'useitem' handler (see doc 11) |
| `0x10032a6b` | `cmd_usegroundxyz` | 96 | CiroScript command 'usegroundxyz' handler (see doc 11) |
| `0x10032acb` | `cmd_opengroundxyz` | 99 | CiroScript command 'opengroundxyz' handler (see doc 11) |
| `0x10032b2e` | `cmd_reachgrounditem` | 82 | CiroScript command 'reachgrounditem' handler (see doc 11) |
| `0x10032b80` | `cmd_skin` | 118 | CiroScript command 'skin' handler (see doc 11) |
| `0x10032bf6` | `cmd_stake` | 118 | CiroScript command 'stake' handler (see doc 11) |
| `0x10032c6c` | `cmd_moveto` | 50 | CiroScript command 'moveto' handler (see doc 11) |
| `0x10032c9e` | `cmd_addloot` | 27 | CiroScript command 'addloot' handler (see doc 11) |
| `0x10032cb9` | `cmd_setammy` | 19 | CiroScript command 'setammy' handler (see doc 11) |
| `0x10032ccc` | `cmd_seticontext` | 101 | CiroScript command 'seticontext' handler (see doc 11) |
| `0x10032d31` | `cmd_seticonactive` | 124 | CiroScript command 'seticonactive' handler (see doc 11) |
| `0x10032dad` | `cmd_setoutfitcolor` | 211 | CiroScript command 'setoutfitcolor' handler (see doc 11) |
| `0x10032e52` | `sub_10032e52` | 5 | Function with empty/opaque body returning an int (no visible logic in this slice). |
| `0x10032e85` | `cmd_setoutfit` | 188 | CiroScript command 'setoutfit' handler (see doc 11) |
| `0x10032ebc` | `sub_10032ebc` | 5 | Empty/stub function with no body. |
| `0x10032f46` | `cmd_setitemoutfit` | 105 | CiroScript command 'setitemoutfit' handler (see doc 11) |
| `0x10032f75` | `sub_10032f75` | 2 | Empty/stub function with no body. |
| `0x10032fb1` | `cmd_setrelation` | 220 | CiroScript command 'setrelation' handler (see doc 11) |
| `0x1003308d` | `cmd_setdebug` | 17 | CiroScript command 'setdebug' handler (see doc 11) |
| `0x1003309e` | `cmd_getproperties` | 52 | CiroScript command 'getproperties' handler (see doc 11) |
| `0x100330d2` | `cmd_gettile` | 73 | CiroScript command 'gettile' handler (see doc 11) |
| `0x1003311b` | `cmd_goinvisible` | 30 | CiroScript command 'goinvisible' handler (see doc 11) |
| `0x10033139` | `cmd_moveitems` | 123 | CiroScript command 'moveitems' handler (see doc 11) |
| `0x100331b4` | `cmd_movenitems` | 57 | CiroScript command 'movenitems' handler (see doc 11) |
| `0x100331ed` | `cmd_moveitemsonto` | 200 | CiroScript command 'moveitemsonto' handler (see doc 11) |
| `0x100332af` | `sub_100332af` | 2 | Empty/stub function with no body. |
| `0x100332b7` | `cmd_openitem` | 50 | CiroScript command 'openitem' handler (see doc 11) |
| `0x100332e9` | `cmd_openbpitem` | 60 | CiroScript command 'openbpitem' handler (see doc 11) |
| `0x10033325` | `cmd_openbeltitem` | 60 | CiroScript command 'openbeltitem' handler (see doc 11) |
| `0x10033361` | `cmd_closeallwindows` | 90 | CiroScript command 'closeallwindows' handler (see doc 11) |
| `0x100333bb` | `cmd_reopenwindows` | 114 | CiroScript command 'reopenwindows' handler (see doc 11) |
| `0x1003342d` | `cmd_loadcavebot` | 17 | CiroScript command 'loadcavebot' handler (see doc 11) |
| `0x1003343e` | `cmd_loadtargeting` | 17 | CiroScript command 'loadtargeting' handler (see doc 11) |
| `0x1003344f` | `cmd_loadsetting` | 17 | CiroScript command 'loadsetting' handler (see doc 11) |
| `0x10033460` | `cmd_loadscript` | 17 | CiroScript command 'loadscript' handler (see doc 11) |
| `0x10033471` | `cmd_openitemnew` | 53 | CiroScript command 'openitemnew' handler (see doc 11) |
| `0x100334a6` | `cmd_useitemsonground` | 193 | CiroScript command 'useitemsonground' handler (see doc 11) |
| `0x10033567` | `cmd_useongroundxyz` | 178 | CiroScript command 'useongroundxyz' handler (see doc 11) |
| `0x10033619` | `cmd_repeatuseongroundxyz` | 192 | CiroScript command 'repeatuseongroundxyz' handler (see doc 11) |
| `0x100336d9` | `cmd_useongrounditem` | 159 | CiroScript command 'useongrounditem' handler (see doc 11) |
| `0x10033778` | `cmd_useoninventoryitem` | 133 | CiroScript command 'useoninventoryitem' handler (see doc 11) |
| `0x100337fd` | `cmd_useoncreature` | 162 | CiroScript command 'useoncreature' handler (see doc 11) |
| `0x1003389f` | `cmd_eatfood` | 9 | CiroScript command 'eatfood' handler (see doc 11) |
| `0x100338a8` | `cmd_uhpc` | 195 | CiroScript command 'uhpc' handler (see doc 11) |
| `0x1003396b` | `cmd_soulf` | 275 | CiroScript command 'soulf' handler (see doc 11) |
| `0x100339e0` | `sub_100339e0` | 2 | Empty/stub function with no body. |
| `0x100339fa` | `sub_100339fa` | 2 | Empty/stub function with no body. |
| `0x10033a1c` | `sub_10033a1c` | 2 | Empty/stub function with no body. |
| `0x10033a45` | `sub_10033a45` | 2 | Empty/stub function with no body. |
| `0x10033a86` | `cmd_annisd` | 155 | CiroScript command 'annisd' handler (see doc 11) |
| `0x10033ab5` | `sub_10033ab5` | 2 | Empty/stub function with no body. |
| `0x10033b23` | `cmd_fish` | 21 | CiroScript command 'fish' handler (see doc 11) |
| `0x10033b38` | `cmd_safe` | 27 | CiroScript command 'safe' handler (see doc 11) |
| `0x10033b53` | `cmd_filewrite` | 50 | CiroScript command 'filewrite' handler (see doc 11) |
| `0x10033b85` | `cmd_filewriteline` | 50 | CiroScript command 'filewriteline' handler (see doc 11) |
| `0x10033bb7` | `cmd_log` | 30 | CiroScript command 'log' handler (see doc 11) |
| `0x10033bd5` | `cmd_filedelete` | 39 | CiroScript command 'filedelete' handler (see doc 11) |
| `0x10033bfc` | `cmd_while` | 137 | CiroScript command 'while' handler (see doc 11) |
| `0x10033c66` | `sub_10033c66` | 2 | Empty/stub function with no body. |
| `0x10033c87` | `cmd_loop` | 142 | CiroScript command 'loop' handler (see doc 11) |
| `0x10033cf6` | `sub_10033cf6` | 2 | Empty/stub function with no body. |
| `0x10033d17` | `cmd_foreach` | 1254 | CiroScript command 'foreach' handler (see doc 11) |
| `0x10033d82` | `sub_10033d82` | 2 | Empty/stub function with no body. |
| `0x10034107` | `formatIndexedNameAndLookup` | 97 | wsprintfA-formats an integer ('%d') into a name buffer, lstrcpy's it, then calls sub_10030442 to resolve/lookup it, guarded by g_1008ab93/ab97/100f0e30 state flags. |
| `0x1003415b` | `sub_1003415b` | 2 | Empty/stub function body (2 bytes), no observable logic; likely a compiler-emitted thunk or optimized-away helper. |
| `0x10034211` | `sub_10034211` | 2 | Empty/stub function body (2 bytes), no observable logic. |
| `0x10034264` | `cmd_ifgm` | 27 | CiroScript command 'ifgm' handler (see doc 11) |
| `0x1003427f` | `cmd_ifnogm` | 27 | CiroScript command 'ifnogm' handler (see doc 11) |
| `0x1003429a` | `cmd_ifplayeronscreen` | 27 | CiroScript command 'ifplayeronscreen' handler (see doc 11) |
| `0x100342b5` | `cmd_ifnoplayeronscreen` | 27 | CiroScript command 'ifnoplayeronscreen' handler (see doc 11) |
| `0x100342d0` | `cmd_ifdefaultmessage` | 27 | CiroScript command 'ifdefaultmessage' handler (see doc 11) |
| `0x100342eb` | `cmd_ifprivatemessage` | 27 | CiroScript command 'ifprivatemessage' handler (see doc 11) |
| `0x10034306` | `cmd_ifplayerattacking` | 27 | CiroScript command 'ifplayerattacking' handler (see doc 11) |
| `0x10034321` | `cmd_isposz` | 32 | CiroScript command 'isposz' handler (see doc 11) |
| `0x10034341` | `cmd_istargetname` | 91 | CiroScript command 'istargetname' handler (see doc 11) |
| `0x1003439c` | `cmd_isattackedname` | 88 | CiroScript command 'isattackedname' handler (see doc 11) |
| `0x100343f4` | `cmd_isattacking` | 28 | CiroScript command 'isattacking' handler (see doc 11) |
| `0x10034410` | `cmd_isnotattacking` | 28 | CiroScript command 'isnotattacking' handler (see doc 11) |
| `0x1003442c` | `cmd_istargeting` | 27 | CiroScript command 'istargeting' handler (see doc 11) |
| `0x10034447` | `cmd_isnottargeting` | 115 | CiroScript command 'isnottargeting' handler (see doc 11) |
| `0x100344ba` | `cmd_isnotonscreen` | 96 | CiroScript command 'isnotonscreen' handler (see doc 11) |
| `0x1003451a` | `cmd_ifpoisoned` | 27 | CiroScript command 'ifpoisoned' handler (see doc 11) |
| `0x10034535` | `cmd_ifdrunk` | 27 | CiroScript command 'ifdrunk' handler (see doc 11) |
| `0x10034550` | `cmd_ifhasted` | 27 | CiroScript command 'ifhasted' handler (see doc 11) |
| `0x1003456b` | `cmd_ifparalyzed` | 27 | CiroScript command 'ifparalyzed' handler (see doc 11) |
| `0x10034586` | `cmd_ifnotparalyzed` | 27 | CiroScript command 'ifnotparalyzed' handler (see doc 11) |
| `0x100345a1` | `cmd_ifnothasted` | 27 | CiroScript command 'ifnothasted' handler (see doc 11) |
| `0x100345bc` | `cmd_ifmanashielded` | 27 | CiroScript command 'ifmanashielded' handler (see doc 11) |
| `0x100345d7` | `cmd_ifnotmanashielded` | 27 | CiroScript command 'ifnotmanashielded' handler (see doc 11) |
| `0x100345f2` | `cmd_haste` | 23 | CiroScript command 'haste' handler (see doc 11) |
| `0x10034609` | `cmd_stronghaste` | 23 | CiroScript command 'stronghaste' handler (see doc 11) |
| `0x10034620` | `cmd_charge` | 23 | CiroScript command 'charge' handler (see doc 11) |
| `0x10034637` | `cmd_swiftfoot` | 23 | CiroScript command 'swiftfoot' handler (see doc 11) |
| `0x1003464e` | `cmd_manashield` | 41 | CiroScript command 'manashield' handler (see doc 11) |
| `0x10034677` | `cmd_ewave` | 38 | CiroScript command 'ewave' handler (see doc 11) |
| `0x1003469d` | `cmd_wave` | 36 | CiroScript command 'wave' handler (see doc 11) |
| `0x100346c1` | `cmd_countlower` | 34 | CiroScript command 'countlower' handler (see doc 11) |
| `0x100346e3` | `cmd_counthigher` | 34 | CiroScript command 'counthigher' handler (see doc 11) |
| `0x10034705` | `cmd_caplower` | 40 | CiroScript command 'caplower' handler (see doc 11) |
| `0x1003472d` | `cmd_caphigher` | 40 | CiroScript command 'caphigher' handler (see doc 11) |
| `0x10034755` | `cmd_hplower` | 33 | CiroScript command 'hplower' handler (see doc 11) |
| `0x10034776` | `cmd_if` | 58 | CiroScript command 'if' handler (see doc 11) |
| `0x100347b0` | `cmd_exec` | 45 | CiroScript command 'exec' handler (see doc 11) |
| `0x100347dd` | `cmd_ifnot` | 58 | CiroScript command 'ifnot' handler (see doc 11) |
| `0x10034817` | `cmd_else` | 31 | CiroScript command 'else' handler (see doc 11) |
| `0x10034836` | `cmd_hpmissinglower` | 42 | CiroScript command 'hpmissinglower' handler (see doc 11) |
| `0x10034860` | `cmd_hpmissinghigher` | 42 | CiroScript command 'hpmissinghigher' handler (see doc 11) |
| `0x1003488a` | `cmd_mpmissinglower` | 42 | CiroScript command 'mpmissinglower' handler (see doc 11) |
| `0x100348b4` | `cmd_mpmissinghigher` | 42 | CiroScript command 'mpmissinghigher' handler (see doc 11) |
| `0x100348de` | `cmd_hphigher` | 33 | CiroScript command 'hphigher' handler (see doc 11) |
| `0x100348ff` | `cmd_ringattacking` | 138 | CiroScript command 'ringattacking' handler (see doc 11) |
| `0x10034989` | `cmd_exivalast` | 50 | CiroScript command 'exivalast' handler (see doc 11) |
| `0x100349bb` | `cmd_exivatarget` | 50 | CiroScript command 'exivatarget' handler (see doc 11) |
| `0x100349ed` | `cmd_lootitems` | 9 | CiroScript command 'lootitems' handler (see doc 11) |
| `0x100349f6` | `cmd_stackitems` | 54 | CiroScript command 'stackitems' handler (see doc 11) |
| `0x10034a2c` | `cmd_collectitems` | 379 | CiroScript command 'collectitems' handler (see doc 11) |
| `0x10034ba7` | `cmd_pickupitemsamount` | 226 | CiroScript command 'pickupitemsamount' handler (see doc 11) |
| `0x10034c89` | `cmd_pickupitems` | 340 | CiroScript command 'pickupitems' handler (see doc 11) |
| `0x10034cd3` | `sub_10034cd3` | 2 | Empty/stub function body (2 bytes), no observable logic. |
| `0x10034ddf` | `cmd_moveitemonground` | 124 | CiroScript command 'moveitemonground' handler (see doc 11) |
| `0x10034e5b` | `cmd_dropitemsxyz` | 174 | CiroScript command 'dropitemsxyz' handler (see doc 11) |
| `0x10034e86` | `cmd_dropitemsxyzamount` | 110 | CiroScript command 'dropitemsxyzamount' handler (see doc 11) |
| `0x10034ef4` | `cmd_dropitems` | 35 | CiroScript command 'dropitems' handler (see doc 11) |
| `0x10034f9a` | `cmd_gfbsd` | 24 | CiroScript command 'gfbsd' handler (see doc 11) |
| `0x10034fb2` | `cmd_aimavalanche` | 24 | CiroScript command 'aimavalanche' handler (see doc 11) |
| `0x10034fca` | `cmd_aimthunderstorm` | 24 | CiroScript command 'aimthunderstorm' handler (see doc 11) |
| `0x10034fe2` | `cmd_aimstoneshower` | 24 | CiroScript command 'aimstoneshower' handler (see doc 11) |
| `0x10034ffa` | `cmd_logout` | 41 | CiroScript command 'logout' handler (see doc 11) |
| `0x10035023` | `cmd_crosshair` | 85 | CiroScript command 'crosshair' handler (see doc 11) |
| `0x10035078` | `cmd_xlog` | 24 | CiroScript command 'xlog' handler (see doc 11) |
| `0x10035090` | `cmd_throwpot` | 43 | CiroScript command 'throwpot' handler (see doc 11) |
| `0x100350bb` | `cmd_pickuppot` | 9 | CiroScript command 'pickuppot' handler (see doc 11) |
| `0x100350c4` | `cmd_surroundpot` | 9 | CiroScript command 'surroundpot' handler (see doc 11) |
| `0x100350cd` | `cmd_magwall` | 63 | CiroScript command 'magwall' handler (see doc 11) |
| `0x1003510c` | `cmd_mwallcover` | 53 | CiroScript command 'mwallcover' handler (see doc 11) |
| `0x10035141` | `cmd_mwallshield` | 38 | CiroScript command 'mwallshield' handler (see doc 11) |
| `0x10035167` | `cmd_mplower` | 33 | CiroScript command 'mplower' handler (see doc 11) |
| `0x10035188` | `cmd_mphigher` | 33 | CiroScript command 'mphigher' handler (see doc 11) |
| `0x100351a9` | `cmd_exorihur` | 143 | CiroScript command 'exorihur' handler (see doc 11) |
| `0x10035238` | `cmd_exoricon` | 143 | CiroScript command 'exoricon' handler (see doc 11) |
| `0x100352c7` | `cmd_exorigran` | 158 | CiroScript command 'exorigran' handler (see doc 11) |
| `0x10035365` | `cmd_targethplower` | 65 | CiroScript command 'targethplower' handler (see doc 11) |
| `0x100353a6` | `cmd_spydown` | 80 | CiroScript command 'spydown' handler (see doc 11) |
| `0x100353f6` | `cmd_spyup` | 80 | CiroScript command 'spyup' handler (see doc 11) |
| `0x10035446` | `cmd_refillmana` | 101 | CiroScript command 'refillmana' handler (see doc 11) |
| `0x100354ab` | `cmd_refillhealth` | 99 | CiroScript command 'refillhealth' handler (see doc 11) |
| `0x1003550e` | `cmd_healparalysis` | 59 | CiroScript command 'healparalysis' handler (see doc 11) |
| `0x10035549` | `cmd_paralyze` | 83 | CiroScript command 'paralyze' handler (see doc 11) |
| `0x1003559c` | `cmd_keepmagwall` | 80 | CiroScript command 'keepmagwall' handler (see doc 11) |
| `0x100355ec` | `cmd_dashchase` | 45 | CiroScript command 'dashchase' handler (see doc 11) |
| `0x10035619` | `cmd_race` | 60 | CiroScript command 'race' handler (see doc 11) |
| `0x10035655` | `cmd_moven` | 27 | CiroScript command 'moven' handler (see doc 11) |
| `0x1003565b` | `cmd_movee` | 6 | CiroScript command 'movee' handler (see doc 11) |
| `0x10035661` | `cmd_moves` | 6 | CiroScript command 'moves' handler (see doc 11) |
| `0x10035667` | `cmd_movew` | 6 | CiroScript command 'movew' handler (see doc 11) |
| `0x1003566d` | `cmd_movene` | 6 | CiroScript command 'movene' handler (see doc 11) |
| `0x10035673` | `cmd_movese` | 6 | CiroScript command 'movese' handler (see doc 11) |
| `0x10035679` | `cmd_movesw` | 6 | CiroScript command 'movesw' handler (see doc 11) |
| `0x1003567f` | `cmd_movenw` | 6 | CiroScript command 'movenw' handler (see doc 11) |
| `0x10035685` | `cmd_turnn` | 6 | CiroScript command 'turnn' handler (see doc 11) |
| `0x1003568b` | `cmd_turne` | 6 | CiroScript command 'turne' handler (see doc 11) |
| `0x10035691` | `cmd_turns` | 6 | CiroScript command 'turns' handler (see doc 11) |
| `0x10035697` | `cmd_turnw` | 6 | CiroScript command 'turnw' handler (see doc 11) |
| `0x100356b2` | `cmd_scrollview` | 212 | CiroScript command 'scrollview' handler (see doc 11) |
| `0x10035786` | `cmd_settargeting` | 129 | CiroScript command 'settargeting' handler (see doc 11) |
| `0x10035807` | `cmd_runtargeting` | 11 | CiroScript command 'runtargeting' handler (see doc 11) |
| `0x10035812` | `cmd_setfollowwaypoints` | 108 | CiroScript command 'setfollowwaypoints' handler (see doc 11) |
| `0x1003587e` | `cmd_setopennextbp` | 107 | CiroScript command 'setopennextbp' handler (see doc 11) |
| `0x100358e9` | `cmd_set` | 233 | CiroScript command 'set' handler (see doc 11) |
| `0x10035923` | `sub_10035923` | 2 | Empty/stub function body (2 bytes), no observable logic. |
| `0x10035937` | `sub_10035937` | 2 | Empty/stub function body (2 bytes), no observable logic. |
| `0x100359a0` | `sub_100359a0` | 2 | Empty/stub function body (2 bytes), no observable logic. |
| `0x100359d8` | `cmd_clear` | 106 | CiroScript command 'clear' handler (see doc 11) |
| `0x10035a1f` | `sub_10035a1f` | 2 | Empty/stub function body (2 bytes), no observable logic. |
| `0x10035a44` | `cmd_inc` | 132 | CiroScript command 'inc' handler (see doc 11) |
| `0x10035aa3` | `sub_10035aa3` | 2 | Empty/stub function body (2 bytes), no observable logic. |
| `0x10035aca` | `cmd_dec` | 111 | CiroScript command 'dec' handler (see doc 11) |
| `0x10035b29` | `sub_10035b29` | 2 | Empty/stub function body (2 bytes), no observable logic. |
| `0x10035b3b` | `cmd_swapequip` | 58 | CiroScript command 'swapequip' handler (see doc 11) |
| `0x10035b75` | `cmd_unequip` | 160 | CiroScript command 'unequip' handler (see doc 11) |
| `0x10035c15` | `cmd_setcaption` | 18 | CiroScript command 'setcaption' handler (see doc 11) |
| `0x10035c27` | `cmd_makerune` | 39 | CiroScript command 'makerune' handler (see doc 11) |
| `0x10035c4e` | `sub_10035c4e` | 4 | Empty function that just returns; stub/thunk. |
| `0x10036bae` | `sub_10036bae` | 4 | Empty function that just returns; stub/thunk. |
| `0x10036bb2` | `parseEquipSlotName` | 213 | Maps an equipment slot name string (helmet/amulet/backpack/chest/lhand/rhand/legs/boots/ring/belt) to a slot index 1-10 via lstrcmpi, else 0. |
| `0x10036c87` | `iterateContainerItemsForDeposit` | 290 | Walks the 16-entry, 492-byte-stride container table at 0x64CAD0 matching container id/type and scans 12-byte item records, invoking sub_1003c52a on qualifying items. |
| `0x10036cbb` | `sub_10036cbb` | 2 | Empty/stub function body (2 bytes). |
| `0x10036cd2` | `sub_10036cd2` | 2 | Empty/stub function body (2 bytes). |
| `0x10036d7d` | `sub_10036d7d` | 2 | Empty/stub function body (2 bytes). |
| `0x10036daf` | `resolveContainerRef` | 179 | Resolves a container reference token: skips spaces, returns numeric value, or maps keywords empty/empty1/dp to 99/98/-1, else looks up the container name in the 492-byte-stride table. |
| `0x10036dd2` | `sub_10036dd2` | 5 | Empty/stub function body (5 bytes). |
| `0x10036e19` | `sub_10036e19` | 2 | Empty/stub function body (2 bytes). |
| `0x10036e69` | `openContainerAndNotify` | 77 | Sets container-open state globals (g_10043373/g_1004336b/g_1004336e/g_10043376) from a 12-byte container record and dispatches event 0x11 via sub_1002ade7. |
| `0x10036eb6` | `depositLootStateMachine` | 586 | Runs the loot/deposit-to-depot state machine over g_102e2604 states 2/3/5/7, opening depot (id 3147) via sub_1002ae92, firing events and Sleep(350)-polling while g_100f0e42 set. |
| `0x10037100` | `findContainerItemAndNotify` | 251 | Scans the 16-slot 492-byte container table for an item matching an id or a 3497-3500 range, calling sub_1003c4fa/sub_10038d20 and firing a notify event 0xC. |
| `0x10037194` | `sub_10037194` | 2 | Empty/stub function body (2 bytes). |
| `0x100371fd` | `findMoveSourceDestSlots` | 391 | Nested scan of the container table pairing a source item slot with a destination container/slot (fill logic honoring field_30 capacity and <100 count), then dispatches move event 0x11 (g_10043465). |
| `0x10037384` | `findNthContainerItemSlot` | 310 | Nested container-table scan locating the Nth (v1 counter) matching item across containers and dispatching move/select event 0x11 (g_10043465). |
| `0x100374ba` | `findWalkableAdjacentTile` | 287 | Scans a 14x18 map window around the player (g_1005f854/g_1005f858) via sub_1003a065/sub_1000d9b8 to find the nearest reachable tile, then walks there via sub_100147eb. |
| `0x100375d9` | `stepTowardTargetTile` | 187 | Computes the player's relative offset in the map window, and if outside the center box calls pathfinder sub_1000d9b8 and issues a direction step (1-8 mapped) via sub_10014825. |
| `0x10037694` | `scanTileForItemInRange` | 309 | Scans the 14x18 map window for a ground item whose id is in 4597..0x1200 (via sub_1003a0f8) skipping blocked tiles, building a 32-byte packet (opcode 0x11/131) and dispatching it via sub_1002ade7. |
| `0x100377a6` | `sub_100377a6` | 2 | Empty/stub function body (2 bytes). |
| `0x100377cb` | `findNearestLootableCorpseTile` | 424 | Builds a 63-entry filter list, scans the 14x18 map window skipping ids 386/421/7762 and 99/1948/1968, matches stacked-item ids and picks the closest reachable tile via sub_1003a065/sub_1000d9b8. |
| `0x10037973` | `directionToOffset` | 67 | Switch on a direction code 1-7 (else default), structurally a direction-to-delta lookup; stripped branches all return. |
| `0x100379b6` | `reportLevelSpyStatus` | 89 | Formats and prints level-spy status ('Level spy off.' / 'Spying on level +/-N.') from g_102e2a08 using wsprintfA and sub_10039374. |
| `0x10037a0f` | `markTileFrontOfPlayer` | 89 | Takes player position and facing direction (idx[20]) to compute the tile directly in front and dispatches action 41 via sub_1003a60a. |
| `0x10037a68` | `isTileWalkableAndClear` | 164 | Tests whether tile (a0,a1) is walkable: not blocked by sub_10011a89, has a valid item stack via sub_1003a03f, and passes flag/edge checks (sub_1003c4fa/sub_1003c3fc/sub_1003c462), returning 1 if clear. |
| `0x10037b0c` | `findBestTargetTileByWeight` | 358 | Builds an 18x14 weight/threat grid from the creature list (0x63FEF8..0x64A308) via sub_1003c55d, then picks the highest-weight walkable tile and issues action 41 (sub_1003a60a). |
| `0x10037c72` | `selectBestTargetByFilter` | 786 | Parses an enemy/subenemy/friend/subfriend[:vocation] filter, scans the creature list applying faction (sub_1003a494/550/320/3da) and vocation checks, and selects the highest-threat creature, caching in g_100f9349. |
| `0x10037f84` | `sumCreatureThreatBytes` | 29 | Sums the 20-byte threat/damage array at offset 112 of the local player struct (sub_10023861) and returns the total. |
| `0x10037fa1` | `countCreaturesTargetingSame` | 316 | For a given creature, marks its reachable tiles in an 18x14 grid (sub_1003c87c) then counts other same-floor enemy creatures that can also reach it (sub_1003c718). |
| `0x100380dd` | `selectMostTargetedCreature` | 876 | Parses a faction/vocation filter, collects matching creatures, marks the player's reachable-tile grid, then counts overlaps per creature and returns the most-contested one, caching in g_100f933d. |
| `0x10038449` | `useItemOnAdjacentTile` | 178 | Opens tool item id 3465, then scans the 3x3 tiles around the player (skipping center) via sub_1003c936 and dispatches a use-on-tile event 0x11 (g_10043482). |
| `0x100384fb` | `scanFollowTargetsBroadcast` | 387 | Iterates the 16 open channels (492-byte stride at 0x64cd10) skipping special channel-name FourCCs, walks each channel's creature list via sub_1003c52a, dedupes, and fires a proxy packet (sub_1002ade7) reporting a matched creature. |
| `0x1003867e` | `scanCreatureTableForPlayer` | 165 | Loops the 16 channels and a 0x200-entry creature table (g_1008caee), calling sub_1002ae92 to test each id and on a hit fills the g_1004347b report struct and sends it via sub_1002ade7. |
| `0x10038706` | `sub_10038706` | 2 | Empty/stub function (single ret). |
| `0x10038725` | `scanChannelCreaturesReport` | 393 | For channels whose name matches special FourCCs, scans a 128-entry node table (g_1008baee) and the fixed id 2853, testing each via sub_1002ae92 and emitting a report packet on match. |
| `0x100388ae` | `tickScanAndReportCreatures` | 1136 | Throttled (GetTickCount/500ms) main creature-scan tick decrementing cooldown counters and walking channels/tables to find and report enemies via sub_1002ae92, sending several report-packet variants. |
| `0x10038bef` | `sub_10038bef` | 2 | Empty/stub function (single ret). |
| `0x10038d20` | `findFirstEmptyCreatureSlot` | 28 | Scans the creature table at 0x64cd10 (123-dword stride) up to 16 entries and returns the index of the first slot whose first field is zero (first free slot). |
| `0x10038d3c` | `parseScramCoordCommand` | 237 | When g_1005f535==1, splits a space-delimited command into 5 numbers via sub_10040900, finds a creature in a bounding box (sub_1003bfec), then sets state 2 and posts '## Scram ##' to the GUI list via SendDlgItemMessageA. |
| `0x10038e29` | `sendTwoStringPacket` | 138 | Builds a proxy packet (opcode 110493709) concatenating two length-prefixed strings a0/a1 into a stack buffer and dispatches it via sub_1002ade7. |
| `0x10038eb3` | `resolveTargetSelector` | 743 | Resolves a target-selector string ('enemy'/'friend'/'self'/'target'/numeric id/name) to a creature record, applying distance and filter constraints (sub_1003c23e/sub_1003bbc1) and picking the nearest match under a health/distance bound. |
| `0x1003919a` | `findBestLootCorpseNearby` | 223 | Scans the creature array (0x63fef8..0x64a308, 168-byte stride) for corpses on the player's floor within range whose tile matches, returning the one with the largest remaining amount >= a0. |
| `0x10039279` | `sub_10039279` | 2 | Empty/stub function (single ret). |
| `0x1003927b` | `findNearestMatchingCreature` | 191 | Iterates the creature array on the player's floor within a distance bound, calling sub_1003b0f0 and tracking the entry with the largest field_62 delta (best candidate); computed result not returned in this decomp. |
| `0x1003933a` | `readClientDword` | 29 | Reads 4 bytes from the Tibia client process at address a0 via ReadProcessMemory on handle g_1005f612. |
| `0x10039357` | `writeClientDword` | 29 | Writes 4 bytes to the Tibia client process at address a0 via WriteProcessMemory on handle g_1005f612. |
| `0x10039374` | `injectClientCommandString` | 78 | Writes a command string to client address 0x7e07b0 and the length/flag 60 to 0x7e07ac via WriteProcessMemory, triggering the client to execute an injected command. |
| `0x100393c2` | `sendPrivateMessagePacket` | 81 | Builds a length-prefixed proxy packet (opcode 1942) carrying a string a0 and channel/target id a1 and sends it via sub_1002ade7. |
| `0x10039413` | `sendPacketOpcode406` | 74 | Builds a length-prefixed proxy packet with opcode 406 wrapping string a0 and dispatches it via sub_1002ade7. |
| `0x1003945d` | `sendPacketOpcode1174` | 74 | Builds a length-prefixed proxy packet with opcode 1174 wrapping string a0 and dispatches it via sub_1002ade7. |
| `0x100394a7` | `refreshBattleListWindow` | 676 | Rebuilds the battle-list GUI: enumerates creatures into g_1006f8ac, formats level/pos/health rows (sub_1003974b/sub_100397a0), and diff-updates the listbox 1901 in window g_10072f70 via SendDlgItemMessageA. |
| `0x1003974b` | `formatCreatureLevelRow` | 85 | Formats a '***Level <n>***' string into a1, computing the level delta from g_10052770 and rendering the signed/unsigned number via sub_10040940/sub_10039951. |
| `0x100397a0` | `formatCreatureInfoRow` | 433 | Formats a padded battle-list row string with name, 'Pos: (x,y)', 'Health: n%', and 'Speed: n (delta)' for a creature record using lstrcat and number formatters. |
| `0x10039951` | `formatSignedNumber` | 45 | Writes a leading '+' or '-' sign then formats the absolute value of a0 as decimal via sub_10040940 (signed integer to string). |
| `0x1003997e` | `findCreatureSlotByPointer` | 49 | Scans the creature array (0x63fef8..0x64a308, 168-byte stride) for the slot whose first field equals pointer a0 and returns that slot, else NULL. |
| `0x100399af` | `findCreatureByName` | 65 | Scans the creature array for an active entry (field_90 set) whose name (offset +4) case-insensitively matches a0 via lstrcmpi, returning the slot or NULL. |
| `0x100399f0` | `findCreatureByPosAndName` | 98 | Iterates the creature array matching x/y/z coordinates (offsets +36/+40/+44) and then case-insensitively comparing the name against v8; result not returned in this decomp. |
| `0x10039a52` | `findSelfCreatureByPos` | 103 | Walks the creature array matching x/y/z coords and validates via sub_1003a320, checking the match against g_1005f7ed (the self/player creature). |
| `0x10039ab9` | `parseCreatureDataAtPos` | 169 | Finds the creature at given x/y/z coords then chains parsers sub_1003a320/3a3da/3a494/3a550 over its data fields, storing the resulting pointer into the record. |
| `0x10039b62` | `findTibiaClientWindow` | 89 | Caches and returns the Tibia client HWND by enumerating 'TibiaClient' windows via FindWindowExA and matching GetWindowThreadProcessId to the current process id. |
| `0x10039bbb` | `sendClientLoginKeystrokes` | 196 | Finds the Tibia client window and sends three ESC then an Enter keystroke (SendMessageA WM_KEYDOWN) while temporarily overriding client globals, to reconnect/relog. |
| `0x10039bf6` | `sub_10039bf6` | 2 | Empty/stub function (single ret). |
| `0x10039c81` | `resizeClientAndBotWindows` | 265 | VirtualProtects the client code, patches client window-size dwords via writeClientDword based on g_100ee8bb, repositions the client and bot windows (SetWindowPos), and forces a WM_SIZE. |
| `0x10039d8a` | `loadHotkeyListsIntoTables` | 368 | Zeroes four 0x4000 buffers (g_1005f8a8 etc.) then parses four CR-terminated config text blocks into 0x200 x 32-byte string tables (hotkey/list entries). |
| `0x10039df9` | `sub_10039df9` | 2 | Empty/stub function (single ret). |
| `0x10039e46` | `sub_10039e46` | 2 | Empty/stub function (single ret). |
| `0x10039e93` | `sub_10039e93` | 2 | Empty/stub function (single ret). |
| `0x10039ee0` | `sub_10039ee0` | 2 | Empty/stub function (single ret). |
| `0x10039f02` | `adjustCoordsByViewOffsetRaw` | 101 | Adjusts x/y map coordinates (a0,a1) by a scroll/view offset read from client globals at 0x64f600/604/608, updating the running offset in a2 (raw-pointer variant). |
| `0x10039f67` | `adjustCoordsByViewOffset` | 97 | Adjusts x/y coordinates by the view offset held in bot globals g_1005f854/858/85c and updates the accumulated offset in a2 (same math as sub_10039f02 with named globals). |
| `0x10039fc8` | `adjustCoordsAndDispatch` | 38 | Applies sub_10039f67 coordinate adjustment then forwards a0/a1/a2 to sub_1003a176 (offset-adjust wrapper). |
| `0x10039fee` | `findMapTileByType` | 81 | Scans the client map-tile pool at [0x654118] in 168-byte-stride blocks, iterating 12-byte item records to find the tile whose item type 99 matches *a0. |
| `0x1003a03f` | `resolveTilePtrForCoords` | 38 | Thin wrapper: invokes helper sub_10039f02 then returns the tile pointer for coords via sub_1003a176. |
| `0x1003a065` | `findWalkableTileNear` | 147 | Gets a tile from sub_1003a0f8, iterates its item records skipping types 0x63/0x184a, and tests walkability flags via sub_1003c4fa (bits 0x10/0x200000/0x2000). |
| `0x1003a0f8` | `tilePtrIfInScreenRange` | 80 | Bounds-checks coords against g_10052768/g_1005276c screen window then returns the tile pointer via sub_1003a176, else 0. |
| `0x1003a148` | `tilePtrClampFloor` | 46 | Clamps the z/floor arg (7-z if <=7 else 2) and returns the tile pointer via sub_1003a176. |
| `0x1003a176` | `mapCoordsToTilePtr` | 52 | Converts (x,y,z) to a tile record pointer: computes an index via sub_1003a1aa, subtracts base [0x654110], scales by 168 and adds pool base [0x654118]. |
| `0x1003a1aa` | `mapCoordsToTileIndexAddr` | 59 | Computes the linear address of a tile slot from x/y/z using client map globals (base 0x654134, strides 0x654128/0x65412c, origins 0x65411c-0x654124). |
| `0x1003a1e5` | `checkPlayerOnTileFilter` | 303 | Gets the tile for the player/creature, and unless filter globals g_101d5e6e-71 match its field type (1/2), invokes sub_10023861. |
| `0x1003a218` | `sub_1003a218` | 2 | Empty/stub function (2-byte body, no operation). |
| `0x1003a234` | `sub_1003a234` | 2 | Empty/stub function (2-byte body, no operation). |
| `0x1003a250` | `sub_1003a250` | 2 | Empty/stub function (2-byte body, no operation). |
| `0x1003a2b6` | `sub_1003a2b6` | 2 | Empty/stub function (2-byte body, no operation). |
| `0x1003a2d2` | `sub_1003a2d2` | 2 | Empty/stub function (2-byte body, no operation). |
| `0x1003a2ee` | `sub_1003a2ee` | 2 | Empty/stub function (2-byte body, no operation). |
| `0x1003a320` | `matchNameAgainstListA` | 184 | Iterates the 512-entry, 32-byte-stride name list g_100638a8 doing lstrcmpi matching with '*'/'++'/'+' prefix rules against a target name (checks sub_1003a1e5==3). |
| `0x1003a3c0` | `sub_1003a3c0` | 2 | Empty/stub function (2-byte body, no operation). |
| `0x1003a3da` | `matchNameAgainstListD` | 184 | Iterates 512-entry 32-byte-stride list g_1006b8a8 with lstrcmpi and '*'/'++'/'+' prefix rules against a name (guarded by sub_1003a1e5==4). |
| `0x1003a47a` | `sub_1003a47a` | 2 | Empty/stub function (2-byte body, no operation). |
| `0x1003a494` | `matchNameAgainstListB` | 186 | Iterates 512-entry 32-byte-stride list g_1005f8a8 with lstrcmpi and '*'/'++'/'+' prefix rules against a name (guarded by sub_1003a1e5==1). |
| `0x1003a534` | `sub_1003a534` | 2 | Empty/stub function (2-byte body, no operation). |
| `0x1003a550` | `matchNameAgainstListC` | 184 | Iterates 512-entry 32-byte-stride list g_100678a8 with lstrcmpi and '*'/'++'/'+' prefix rules against a name (guarded by sub_1003a1e5==2). |
| `0x1003a5f0` | `sub_1003a5f0` | 2 | Empty/stub function (2-byte body, no operation). |
| `0x1003a60a` | `castRuneOrSpellOnTarget` | 1103 | Maps an action code to a spell/rune: fills packet globals g_100432xx and either sends a rune-use packet (\r) or spell text (\t/\r), or returns exori/exevo spell strings via sub_10039413. |
| `0x1003a6de` | `sub_1003a6de` | 5 | Empty/stub function (5-byte body, no operation). |
| `0x1003a6f4` | `sub_1003a6f4` | 5 | Empty/stub function (5-byte body, no operation). |
| `0x1003a70a` | `sub_1003a70a` | 5 | Empty/stub function (5-byte body, no operation). |
| `0x1003a720` | `sub_1003a720` | 5 | Empty/stub function (5-byte body, no operation). |
| `0x1003a736` | `sub_1003a736` | 5 | Empty/stub function (5-byte body, no operation). |
| `0x1003a74c` | `sub_1003a74c` | 5 | Empty/stub function (5-byte body, no operation). |
| `0x1003a762` | `sub_1003a762` | 5 | Empty/stub function (5-byte body, no operation). |
| `0x1003a778` | `sub_1003a778` | 5 | Empty/stub function (5-byte body, no operation). |
| `0x1003a78e` | `sub_1003a78e` | 5 | Empty/stub function (5-byte body, no operation). |
| `0x1003a7a4` | `sub_1003a7a4` | 5 | Empty/stub function (5-byte body, no operation). |
| `0x1003a7ba` | `sub_1003a7ba` | 5 | Empty/stub function (5-byte body, no operation). |
| `0x1003a7d0` | `sub_1003a7d0` | 5 | Empty/stub function (5-byte body, no operation). |
| `0x1003a7e6` | `sub_1003a7e6` | 5 | Empty/stub function (5-byte body, no operation). |
| `0x1003aa9a` | `drawCreatureHudBars` | 1334 | Builds the HUD overlay for a targeted creature: formats HP/mana name string, sets color globals, computes bar sizes, and emits draw calls (sub_1003b127) for level/mark/flee status. |
| `0x1003ad4a` | `sub_1003ad4a` | 5 | Empty/stub function (5-byte body, no operation). |
| `0x1003afb0` | `drawHudDpsText` | 82 | Formats a damage-per-second string "-%d%c/s" into g_10080b4d, sets red color globals, and draws it via sub_1003b127. |
| `0x1003b007` | `drawTargetStatusIcons` | 201 | Draws up to two colored status indicators (fields field_8e/field_8f) for the HUD target via sub_1003b159, advancing the y-offset g_10080b80 and setting color globals. |
| `0x1003b0f0` | `findMessageBySenderId` | 55 | Iterates a 106-byte-stride table at g_1008d2ee scanning for a record whose id (g_1008d354) matches a0 and whose timestamp field (g_1008d330) > 280, returns the record. |
| `0x1003b127` | `drawHudTextColored` | 50 | Pushes x/y (a0,a1), the current RGB color globals (g_1008b8f4/f8/fc) and text a2 onto the stack and calls the client text-render thunk at 4935120 to draw a HUD string. |
| `0x1003b159` | `drawHudTimerText` | 210 | Formats a millisecond duration a3 into a mm:ss[.d] string appended to label a2 (via sub_10040940/lstrcat) then renders it at x/y with current color, for HUD timer display. |
| `0x1003b22b` | `renderBotHud` | 2042 | Main HUD/overlay renderer: walks hotkey/cavebot/persist/spell tables and active-effect timer globals, formatting rows (hotkeys, ping/exp/target, buffs like MShield/Invis/Haste) via drawHudText helpers. |
| `0x1003b2b5` | `sub_1003b2b5` | 5 | Empty/stub function (no body). |
| `0x1003b550` | `sub_1003b550` | 5 | Empty/stub function (no body). |
| `0x1003ba2f` | `registerNavTargetCreature` | 230 | Given a client creature pointer a8, looks up/creates a shadow creature record via sub_10023861, copies its 32-byte name and id into fields, and sets targeting/visibility flags. |
| `0x1003baa6` | `stubCallEmpty1` | 2 | Trivial wrapper that calls the empty routine sub_1003bb1b and returns. |
| `0x1003bac2` | `stubCallEmpty2` | 2 | Trivial wrapper that calls the empty routine sub_1003bb1b and returns. |
| `0x1003bacc` | `stubCallEmpty3` | 2 | Trivial wrapper that calls the empty routine sub_1003bb1b and returns. |
| `0x1003bb1b` | `noop` | 7 | No-op function that immediately returns. |
| `0x1003bb22` | `dequeueMarkedCreature` | 157 | Scans the shadow creature table (g_10077175..g_100809cd) for an entry flagged field_4d, picks it, publishes its coords/type into g_1004332b.. and emits a tab-marker via sub_1002ade7. |
| `0x1003bba4` | `sub_1003bba4` | 2 | Empty/stub function (no body). |
| `0x1003bbc1` | `creatureWithinRange` | 72 | Returns idx if the creature record's floor (idx[11]) matches g_10052770 and its /dx/,/dy/ from player pos (g_10052768/6c) are both <= a1, else NULL — a range filter. |
| `0x1003bc09` | `isCreatureReachableWalkable` | 75 | Wraps sub_1003c23e range check then verifies target tile is walkable (sub_10011a89) and, if g_100fa97a set, path-reachable (sub_10011678), returning a reachability boolean. |
| `0x1003bc54` | `selectBestTargetByPriority` | 625 | Scans the creature array (0x63fef8..0x64a308) applying reachability/range/HP filters and tracks best candidates into distance/danger/HP slot arrays for target selection. |
| `0x1003bec5` | `selectClosestTargetCreature` | 295 | Iterates the creature array with a filter callback (sub_1003a320/3da), applying walkable/path/range checks, tracking the lowest-HP reachable creature as the chosen target. |
| `0x1003bfec` | `pickLowestHpTrackedCreature` | 107 | Walks the 32-byte-stride name table g_1005f8a8, resolves each via sub_100399af, and returns the tracked creature with the lowest HP-percent (field 0x88) when g_100f94c9 set. |
| `0x1003c031` | `sub_1003c031` | 2 | Empty/stub function (no body). |
| `0x1003c059` | `pickTargetInAdjacentTiles` | 483 | Buckets creatures within a 3x3 tile window around (a0,a1) of type a2 into a grid, then selects by attack mode a3 (players/monsters) preferring lowest HP-percent. |
| `0x1003c18e` | `sub_1003c18e` | 2 | Empty/stub function (no body). |
| `0x1003c23e` | `isCreatureOnScreenTile` | 83 | Range/screen filter: returns idx if its type matches g_1005f85c and its tile coords fall within the ~15x11 visible window centered on player (g_1005f854/58). |
| `0x1003c291` | `isCoordCreatureOnScreen` | 82 | Same on-screen tile check as sub_1003c23e but on a struct with 2-byte-offset fields (field_0/4/8) instead of 0x24/0x28/0x2c. |
| `0x1003c2e3` | `isTileOnScreen` | 78 | Returns 1 if the given x/y/floor (a0,a1,a2) lie inside the visible ~15x11 screen window around the player and match floor g_1005f85c, else 0. |
| `0x1003c331` | `maybeInvokeGuard` | 47 | Conditionally tail-calls sub_1003c359 when g_1005f8a3 or g_1005f88d flags are set or arg a7==11; otherwise falls through. |
| `0x1003c359` | `stubStoreEbx` | 12 | Near-empty routine that stores a register into a local; effectively a stub/landing pad. |
| `0x1003c365` | `stubCallReturn` | 2 | Trivial wrapper calling the empty sub_1003c36e and returning. |
| `0x1003c36e` | `noop2` | 1 | No-op function that immediately returns. |
| `0x1003c36f` | `isCreatureBlockingOrSpecial` | 141 | Reads a creature's 76-byte record via the client id-table at 0x7998dc and tests its type/flag byte (masks like 0x40) to decide if it blocks path or is a special monster type. |
| `0x1003c3fc` | `creatureHasFlag0x10` | 52 | Reads the creature record flag byte (client id-table at 0x7998dc, offset 37) and returns its bit 0x10 status. |
| `0x1003c430` | `setCreatureFlag0x10` | 50 | Sets bit 0x10 in the creature record's flag byte (client id-table 0x7998dc, offset 37) and returns 1. |
| `0x1003c462` | `creatureHasFlag0x80` | 52 | Reads the creature record flag byte (id-table 0x7998dc, offset 37) and returns its bit 0x80 status. |
| `0x1003c496` | `clearCreatureFlag0x80` | 50 | Clears bit 0x80 (mask 127) in the creature record's flag byte (id-table 0x7998dc, offset 37) and returns 1. |
| `0x1003c4c8` | `setCreatureFlag0x80` | 50 | Sets bit 0x80 in the creature record's flag byte (id-table 0x7998dc, offset 37) and returns 1. |
| `0x1003c4fa` | `getCreatureFlagsDword` | 48 | Returns the full 32-bit flags dword at offset 37 of the creature's 76-byte record via the client id-table at 0x7998dc. |
| `0x1003c52a` | `creatureHasFlag0x20` | 51 | Reads the creature record flag byte (id-table 0x7998dc, offset 37) and returns its bit 0x20 status. |
| `0x1003c55d` | `traceLineMarkTiles` | 443 | Bresenham line-walk between (a0,a1)->(a2,a3) checking each tile via sub_1003c87c for blocking creatures; increments/rolls back a per-tile counter buffer a4, returns line-of-sight result. |
| `0x1003c718` | `lineOfSightWalkable` | 356 | Bresenham line-walk from (a0,a1) to (a2,a3) over the walkability map a4 (offset from g_10052768/6c), returning 1 if a non-walkable tile blocks the path else 0. |
| `0x1003c87c` | `tileBlockedByCreature` | 88 | Looks up the creature list at tile (a0,a1) floor g_10052770 via sub_1003a03f, iterating its 12-byte entries and returning true if any is a blocking/special creature (sub_1003c36f). |
| `0x1003c8bb` | `sub_1003c8bb` | 2 | Empty/stub function (no body). |
| `0x1003c8c2` | `sub_1003c8c2` | 2 | Empty/stub function (single ret), no body. |
| `0x1003c8d8` | `tileHasNonWalkableItem` | 90 | Fetches the tile stack at (a0,a1) via sub_1003a03f and iterates its 12-byte item records, returning 0 if any item (id != 99) is blocking per sub_1003c3fc. |
| `0x1003c919` | `sub_1003c919` | 2 | Empty/stub function (single ret), no body. |
| `0x1003c920` | `sub_1003c920` | 2 | Empty/stub function (single ret), no body. |
| `0x1003c936` | `isTileWalkableInRange` | 131 | Bounds-checks (a0,a1) against player pos (g_10052768/6c, 18x14 screen window) then scans the tile's 12-byte item stack, returning 0 if a blocking item is found. |
| `0x1003c99f` | `sub_1003c99f` | 2 | Empty/stub function (single ret), no body. |
| `0x1003c9a6` | `sub_1003c9a6` | 2 | Empty/stub function (single ret), no body. |
| `0x1003c9bd` | `getTileFirstItemPtr` | 70 | Bounds-checks (a0,a1) against the visible screen window then returns the first item pointer of the tile stack from sub_1003a03f, else NULL. |
| `0x1003ca03` | `targetSelectBestCreature` | 1460 | Cavebot/targeting scan: iterates the client creature table (0x63fef8..0x64a308), builds walkable/reachable grids over the 18x14 screen, scores 7x7 area-effect tiles, and picks/attacks the best target via sub_1003a60a. |
| `0x1003d19a` | `attackMoveToTargetTile` | 1141 | Picks an approach direction to a target from 8 offset tables (near/far x quadrant) using distance/mode g_100fa97a, validates each tile with sub_1003c936 and issues the move via sub_1002ade7. |
| `0x1003d60f` | `drawTargetTileMarkers` | 289 | Marks the tile in front of the player (by facing g_1005f7ed->field_50) and the surrounding 3x3 tiles, calling sub_1003d730/sub_1003a03f and sub_1002ade7 to render markers. |
| `0x1003d730` | `listContainsCoord` | 64 | Iterates a length-prefixed array of {x,z} pairs and returns 1 if entry matches a1 (x) and optionally a2 (z). |
| `0x1003d770` | `drawSpellAreaShape` | 212 | Classifies a rune/spell value (negative=area id 2..351, or 100..10477 range) and dispatches to sub_1003d844 or an internal drawer to render its area-effect footprint. |
| `0x1003d844` | `drawAreaBoxOverlay` | 88 | Fills a large arg frame (colors 71/192, size 100, base g_1005f7ed) and calls the HUD box-drawing routine at 4939408 to draw an area overlay at (a0,a1). |
| `0x1003d89c` | `logTimerThreadDiagnostics` | 259 | Snapshots the timer thread's CONTEXT/EIP and tick deltas, wsprintfA-formats a 'Locked on hotkey'/error diagnostic string and emits it via sub_100253d9. |
| `0x1003d99f` | `botMainTickDispatch` | 2304 | Main per-frame bot tick: syncs client viewport rect into shadow state, watchdogs/restarts the timer thread (Create/Terminate/Suspend/SetThreadContext), then runs targeting, HUD and hotkey subsystems. |
| `0x1003e29f` | `sub_1003e29f` | 1 | Empty/stub function (single ret), no body. |
| `0x1003e2a0` | `drainMessageRingBuffer` | 173 | Advances a 316-byte-stride circular buffer (2000 slots, indices g_100f49dd/e1), memcpy-copying each pending 316-byte record forward and calling sub_10026724 to process it. |
| `0x1003e34d` | `renderHudOverlays` | 460 | Frame render entry: invokes the client draw vtable then paints bot HUD layers (arrows sub_1003b22b, coord/cursor text via wsprintfA+sub_1003b127, minimap, custom labels sub_1003e7aa). |
| `0x1003e35f` | `restoreRenderTarget` | 17 | Copies g_1005e19c into g_63fe5c, restoring a saved client render/frame pointer. |
| `0x1003e392` | `adjustZoomLevel` | 75 | Increments/decrements the zoom level g_64f600 (clamped 0..7) based on command g_102e2a08, then re-renders via sub_1003e3e1. |
| `0x1003e3bf` | `sub_1003e3bf` | 2 | Empty/stub function (single ret), no body. |
| `0x1003e3c6` | `sub_1003e3c6` | 2 | Empty/stub function (single ret), no body. |
| `0x1003e3e1` | `renderMapAtFixedSize` | 121 | Temporarily overrides the game window rect fields on g_10080b84 to 320x240, calls the client draw method, then restores the saved rect and zoom. |
| `0x1003e5f2` | `drawSpellAreaAtTile` | 440 | Renders a spell/rune area footprint at (iter,node): special-cases the 4-quadrant 64px case, otherwise classifies the value, applies directional offset by mode a4, draws via sub_1003d770 and optional label sub_1003b127. |
| `0x1003e7aa` | `drawCustomHudElements` | 473 | Iterates the 4308-byte-stride custom HUD element table (g_1014f420..g_101d5e20), computes anchored x/y from field-relative modes, and draws each element's icon/text via sub_1003e5f2 and sub_1003b127. |
| `0x1003e983` | `walkStepToWaypoint` | 177 | Attempts a walk/click step toward (a0,a1,a2) using the client pathfinder at 4604016, handling result codes and clearing cavebot waypoint-approach flags (g_100f0e45/46, g_100f45a8) on success. |
| `0x1003ea34` | `scriptHotkeyExecThread` | 480 | Thread body: lstrcpy's a 4096-byte hotkey/script text block, parses it splitting on '/' with {}-nesting and '#' comments, dispatching each command line via sub_10030442, then ExitThread. |
| `0x1003eaf2` | `sub_1003eaf2` | 5 | Empty/stub function (multi-byte ret), no body. |
| `0x1003eb06` | `sub_1003eb06` | 5 | Empty/stub function (multi-byte ret), no body. |
| `0x1003ec1e` | `stepAroundObstacle` | 174 | On a blocked path, computes a nearby offset tile and queries sub_1000d9b8 for a direction, remaps the returned direction code and issues the walk via sub_10014825. |
| `0x1003eccc` | `walkToStoredTarget` | 45 | Resolves a stored map target via sub_10037973 and walks toward it with sub_100147eb using the current floor g_1005f85c. |
| `0x1003ecf9` | `cavebotWaypointTick` | 1679 | Cavebot state machine tick (100ms cadence): steps through the waypoint list g_101e6ea8, dispatching per-waypoint-type actions (walk, use, rope/rune, script, lure, stand) with distance-based delay g_100f0df8. |
| `0x1003ef4f` | `sub_1003ef4f` | 2 | Empty/stub function (single ret), no body. |
| `0x1003ef8c` | `sub_1003ef8c` | 2 | Empty/stub function (single ret), no body. |
| `0x1003f189` | `sub_1003f189` | 5 | Empty/stub function (multi-byte ret), no body. |
| `0x1003f2da` | `sub_1003f2da` | 2 | Empty/stub function (single ret), no body. |
| `0x1003f393` | `getPlayerPathNode` | 13 | Returns g_1005f7ed->field_4c (a linked path/route node pointer) or NULL if g_1005f7ed is null. |
| `0x1003f3a0` | `renderMinimapTiles` | 567 | Computes the visible minimap grid around the player from g_10080b84 viewport, iterates 100x100-pixel map cells calling sub_1003f5d7 per cell and blits them via the client draw vtable into g_100f0e78. |
| `0x1003f5d7` | `loadMinimapCell` | 1204 | LRU-caches a 100x100 minimap cell keyed by (x,y,floor): loads/creates '%sminimaps\%d\%d.elfm' files, falls back to blankmaps.elfm or adjacent floors, and writes back sampled colors. |
| `0x1003f644` | `sub_1003f644` | 2 | Empty/stub function with no body (2-byte thunk or ret). |
| `0x1003f667` | `sub_1003f667` | 2 | Empty/stub function with no body (2-byte thunk or ret). |
| `0x1003fa8f` | `navNetClientThreadLoop` | 1356 | NavNet proxy client thread: hex-parses host key, socket/connect to g_1013f31c, sends login (user/pass), then recv-loops parsing type-tagged packets (name/pos/creature/HUD) into shadow tables g_10093cee/g_10095cee, reconnecting on error. |
| `0x1003ffdb` | `sub_1003ffdb` | 4 | Empty function that immediately returns (no-op). |
| `0x1003ffdf` | `sendNavPositionUpdate` | 458 | Builds and encrypts (sub_1002ae6f) an 11-byte NavNet status packet with player XY/Z from 0x63fe74-78 and flags, sends it via g_1005f539, then appends per-creature type-3 records over the 0x63fef8..0x64a308 table when g_1005f53d set. |
| `0x100401a9` | `findItemInContainerSlots` | 78 | Calls sub_1003a0f8 to get a record then iterates its field_0 entries (8-byte stride) returning the first slot whose id matches 0x79c/0x7b0/0x15a6/0x1e5b. |
| `0x100401f7` | `sendUseItemPacket` | 83 | Resolves an item via sub_100401a9 then fills a 12-byte opcode-0x82 packet with the x/y/z coords and dispatches it through sub_1002ade7. |
| `0x1004024a` | `lastNonDefaultListEntry` | 40 | Iterates a count-prefixed list of 8-byte records returning the last entry value that is not the sentinel 99. |
| `0x10040272` | `sendLookOrUsePacket` | 166 | Fetches a tile record via sub_1003a0f8; if a3 matches g_10044628/g_1004462c and a container item (867/868) is present picks it, else uses the top item, then sends a 19-byte opcode-0x83 packet via sub_1002ade7. |
| `0x10040318` | `captureClientWindowBitmap` | 814 | Grabs the Tibia window (sub_10039b62) via GetWindowDC/BitBlt to a compatible bitmap, then either copies it to the clipboard (a0) or writes a timestamped .bmp file with GetDIBits/WriteFile. |
| `0x10040900` | `parseSignedInt` | 54 | Parses an ASCII decimal string (leading byte 2 marks negative) into a signed integer via digit accumulation and two's-complement negation. |
| `0x10040940` | `intToAsciiDecimal` | 101 | Converts an unsigned/signed int to a decimal ASCII string in the a1 buffer (writes '-' sign, builds digits reversed then swaps in place); '0' fast path. |
| `0x100409a8` | `intToHex8` | 42 | Formats a 32-bit value as an 8-char uppercase hex string into a1->padding_0 nibble-by-nibble using arithmetic ASCII conversion. |
| `0x100409e0` | `memsetDword` | 77 | Fills a1 bytes at a0 with the dword value a2, unrolled 8 dwords per iteration then a 4-byte-granular remainder loop (custom memset). |
| `0x10040a30` | `randRange` | 70 | Park-Miller minimal-standard LCG (16807 multiplier, 2147483647 modulus via 127773/2836 split) updating seed g_1005a280 and returning value mod a0. |
| `0x10040a76` | `srandSeed` | 15 | Seeds the LCG PRNG by storing a0 into g_1005a280. |
