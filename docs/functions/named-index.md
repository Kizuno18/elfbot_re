# elfbot.dll — named function index

Every `.jdrv` function that has been identified by semantics. Decompiled C for all 1190 `.jdrv` functions is under [decompiled/](decompiled/jdrv-index.md); this index lists the named ones. `cmd_*` handlers implement CiroScript commands ([doc 11](../11-ciroscript-engine.md)).

**454 named** of 1190 `.jdrv` functions.

## Core / init (5)

| Address | Name | Size | Calls |
|---|---|---|---|
| `0x10002c1f` | `DllEntryPoint` | 67 | CreateThread,GetCurrentProcess |
| `0x10002c87` | `postBotMessage` | 55 | SendMessageA |
| `0x10002cbe` | `EcInit` | 74 | EcInit,Sleep |
| `0x10002d46` | `registerDialogs` | 824 | GetModuleFileNameA,InitCommonControls,LoadCursorA,LoadIconA |
| `0x100172b0` | `parseTargetingRecord` | 5399 |  |

## Hooks / proxy (9)

| Address | Name | Size | Calls |
|---|---|---|---|
| `0x10001a96` | `hook_captureRenderCtx` | 34 |  |
| `0x10001ca8` | `hook_incomingPacketParser` | 696 |  |
| `0x10002041` | `installClientHooks_proxyServer` | 387 | CreateThread,VirtualProtect,WSACleanup,WSAStartup |
| `0x10002235` | `proxyClientThread` | 326 | ExitThread |
| `0x100029a4` | `hook_fullLightDetour` | 561 | WriteProcessMemory |
| `0x10002bd6` | `hook_fullLight_trampoline` | 7 |  |
| `0x10002bdd` | `installLightHook` | 36 | GetCurrentProcess,WriteProcessMemory |
| `0x1002c1b6` | `registerCommand` | 114 | MessageBoxA |
| `0x10030442` | `registerCommands_table` | 4493 |  |

## Feature dialogs (23)

| Address | Name | Size | Calls |
|---|---|---|---|
| `0x10003146` | `dlgProc_AutoAim` | 14876 | CreateDirectoryA,CreateFontA,CreateWindowExA,GetProcessHeap |
| `0x10006bce` | `dlgProc_HudCreatureList` | 149 | GetDlgItem,MoveWindow,SendDlgItemMessageA |
| `0x10006d3b` | `dlgProc_Shortkeys` | 1573 | CreateFontA,CreateWindowExA,GetDlgItem,GetWindowPlacement |
| `0x10007360` | `dlgProc_Hotkeys` | 1704 | CreateFontA,CreateWindowExA,GetDlgItem,GetWindowPlacement |
| `0x10007b55` | `dlgProc_HudOnScreenInfo` | 336 | ShowWindow |
| `0x10007ca5` | `dlgProc_AutoAimCombo` | 543 | SendDlgItemMessageA,ShowWindow |
| `0x10007ec4` | `dlgProc_GraphicsTweaks` | 363 | SendDlgItemMessageA,ShowWindow,WritePrivateProfileStringA |
| `0x1000802f` | `dlgProc_TargetingEditor` | 291 | DestroyWindow,SendDlgItemMessageA |
| `0x100083b6` | `dlgProc_ScriptEditor` | 765 | CloseClipboard,DestroyWindow,EmptyClipboard,GetClipboardData |
| `0x100086b3` | `dlgProc_Skin` | 823 | DestroyWindow,DlgDirListA,GetPrivateProfileStringA,SendDlgItemMessageA |
| `0x10019751` | `dlgProc_Cavebot` | 4014 | DragQueryFile,GetDlgItem,SendDlgItemMessageA,ShowWindow |
| `0x1001a715` | `dlgProc_Targeting` | 4037 | DragQueryFile,GetTickCount,SendDlgItemMessageA,ShowWindow |
| `0x1001b8be` | `dlgProc_SkinEditor` | 5096 | ChooseColorA,CreateSolidBrush,GetDlgItem,SelectObject |
| `0x1001d151` | `dlgProc_CommandBuilder` | 399 | CloseClipboard,DestroyWindow,EmptyClipboard,GlobalAlloc |
| `0x1001d2e0` | `dlgProc_CommandParamBuilder` | 797 | DestroyWindow,EnableWindow,GetDlgItem,MessageBoxA |
| `0x1001d5fd` | `dlgProc_CommandParamPicker` | 2310 | DestroyWindow,EnableWindow,GetDlgItem,MessageBoxA |
| `0x1001df05` | `dlgProc_CommandPicker` | 724 | DestroyWindow,SendDlgItemMessageA,SendMessageA |
| `0x1001e1d9` | `dlgProc_HotkeyActionPicker` | 314 | DestroyWindow,EnableWindow,GetDlgItem,SendDlgItemMessageA |
| `0x1001e313` | `dlgProc_FriendsEnemies` | 210 | ShowWindow |
| `0x1001e3e5` | `dlgProc_Healer` | 990 | SendDlgItemMessageA,ShowWindow |
| `0x1001e7c3` | `dlgProc_NavNet` | 880 | ChooseColorA,SendDlgItemMessageA |
| `0x1001eb33` | `dlgProc_LinksNavNet` | 985 | MessageBoxA,SendDlgItemMessageA,WriteProcessMemory |
| `0x1001ef0c` | `dlgProc_LinksProxy` | 1649 | CreateThread,SendDlgItemMessageA |

## CiroScript commands (417)

| Address | Name | Size | Calls |
|---|---|---|---|
| `0x1002cbca` | `cmd_mppc` | 45 |  |
| `0x1002cc38` | `cmd_cap` | 30 |  |
| `0x1002cc56` | `cmd_exp` | 20 |  |
| `0x1002cc7e` | `cmd_mlevel` | 20 |  |
| `0x1002ccce` | `cmd_soul` | 20 |  |
| `0x1002cce2` | `cmd_stamina` | 20 |  |
| `0x1002ccf6` | `cmd_count` | 19 |  |
| `0x1002cd09` | `cmd_screenleft` | 37 |  |
| `0x1002cd2e` | `cmd_screenright` | 40 |  |
| `0x1002cd56` | `cmd_screentop` | 37 |  |
| `0x1002cd7b` | `cmd_screenbottom` | 40 |  |
| `0x1002cdbe` | `cmd_time` | 28 | GetTickCount |
| `0x1002cdda` | `cmd_timems` | 19 | GetTickCount |
| `0x1002cded` | `cmd_deltatime` | 34 | GetTickCount |
| `0x1002ce0f` | `cmd_deltatimems` | 25 | GetTickCount |
| `0x1002ce28` | `cmd_return` | 18 |  |
| `0x1002ce3a` | `cmd_exptnl` | 36 |  |
| `0x1002ce5e` | `cmd_exph` | 19 |  |
| `0x1002ce71` | `cmd_expgained` | 39 |  |
| `0x1002ce98` | `cmd_timetnl` | 96 | CONCAT |
| `0x1002cef8` | `cmd_exptolevel` | 52 |  |
| `0x1002cf2c` | `cmd_timetolevel` | 112 | CONCAT |
| `0x1002cf9c` | `cmd_screencount` | 116 |  |
| `0x1002d010` | `cmd_mcount` | 272 |  |
| `0x1002d122` | `cmd_pcount` | 272 |  |
| `0x1002d234` | `cmd_monstersaround` | 140 |  |
| `0x1002d2c0` | `cmd_playersaround` | 148 |  |
| `0x1002d45d` | `cmd_sbtime` | 28 |  |
| `0x1002d479` | `cmd_sstime` | 28 |  |
| `0x1002d495` | `cmd_exectime` | 19 |  |
| `0x1002d4a8` | `cmd_synctime` | 24 |  |
| `0x1002d4c0` | `cmd_fired` | 19 |  |
| `0x1002d4d3` | `cmd_formattime` | 99 |  |
| `0x1002d536` | `cmd_formatnum` | 26 |  |
| `0x1002d550` | `cmd_ringslot` | 32 |  |
| `0x1002d570` | `cmd_beltslot` | 32 |  |
| `0x1002d590` | `cmd_backslot` | 32 |  |
| `0x1002d5b0` | `cmd_rhandslot` | 32 |  |
| `0x1002d5d0` | `cmd_lhandslot` | 32 |  |
| `0x1002d5f0` | `cmd_amuletslot` | 32 |  |
| `0x1002d610` | `cmd_bootsslot` | 32 |  |
| `0x1002d630` | `cmd_headslot` | 32 |  |
| `0x1002d650` | `cmd_chestslot` | 32 |  |
| `0x1002d670` | `cmd_legsslot` | 32 |  |
| `0x1002d690` | `cmd_topitem` | 99 |  |
| `0x1002d6f3` | `cmd_istileitem` | 140 |  |
| `0x1002d77f` | `cmd_poisoned` | 25 |  |
| `0x1002d798` | `cmd_poisondmg` | 34 |  |
| `0x1002d7ba` | `cmd_manashielded` | 25 |  |
| `0x1002d7d3` | `cmd_battlesign` | 25 |  |
| `0x1002d7ec` | `cmd_redbattlesign` | 25 |  |
| `0x1002d805` | `cmd_drunk` | 25 |  |
| `0x1002d81e` | `cmd_hasted` | 25 |  |
| `0x1002d837` | `cmd_paralyzed` | 25 |  |
| `0x1002d850` | `cmd_inpz` | 25 |  |
| `0x1002d869` | `cmd_navion` | 25 |  |
| `0x1002d882` | `cmd_itemcount` | 83 |  |
| `0x1002d8d5` | `cmd_winitemcount` | 86 |  |
| `0x1002d92b` | `cmd_fileisline` | 89 |  |
| `0x1002d984` | `cmd_rand` | 87 |  |
| `0x1002d9db` | `cmd_fileline` | 56 |  |
| `0x1002da13` | `cmd_token` | 203 |  |
| `0x1002dae0` | `cmd_filerandomline` | 31 |  |
| `0x1002daff` | `cmd_connected` | 35 |  |
| `0x1002db22` | `cmd_pkname` | 18 |  |
| `0x1002db34` | `cmd_ping` | 19 |  |
| `0x1002db47` | `cmd_fps` | 39 |  |
| `0x1002db6e` | `cmd_enemycount` | 90 |  |
| `0x1002dbc8` | `cmd_friendcount` | 90 |  |
| `0x1002dc22` | `cmd_fishspots` | 26 |  |
| `0x1002dc3c` | `cmd_caveboton` | 21 |  |
| `0x1002dc51` | `cmd_targetingon` | 21 |  |
| `0x1002dc66` | `cmd_autocomboon` | 21 |  |
| `0x1002dc7b` | `cmd_mshieldtime` | 26 |  |
| `0x1002dc95` | `cmd_hastetime` | 26 |  |
| `0x1002dcaf` | `cmd_strengthtime` | 26 |  |
| `0x1002dcc9` | `cmd_invistime` | 26 |  |
| `0x1002dce3` | `cmd_invisible` | 34 |  |
| `0x1002dd05` | `cmd_dmgs` | 19 |  |
| `0x1002dd18` | `cmd_lastdmg` | 19 |  |
| `0x1002dd2b` | `cmd_lastdmgtype` | 19 |  |
| `0x1002dd3e` | `cmd_idlerecvtime` | 25 | GetTickCount |
| `0x1002dd57` | `cmd_standtime` | 25 | GetTickCount |
| `0x1002dd70` | `cmd_lastdmgtime` | 36 | GetTickCount |
| `0x1002dd94` | `cmd_islooting` | 30 |  |
| `0x1002ddb2` | `cmd_lastdmgername` | 20 |  |
| `0x1002ddc6` | `cmd_squaretime` | 19 |  |
| `0x1002de19` | `cmd_cutstr` | 20 |  |
| `0x1002deab` | `cmd_creature` | 64 |  |
| `0x1002deeb` | `cmd_mostexposed` | 52 |  |
| `0x1002df1f` | `cmd_mostexposedcount` | 54 |  |
| `0x1002df55` | `cmd_mostshot` | 52 |  |
| `0x1002df89` | `cmd_mostshotcount` | 54 |  |
| `0x1002dfbf` | `cmd_ctrl` | 27 |  |
| `0x1002dfda` | `cmd_shift` | 27 |  |
| `0x1002dff5` | `cmd_alt` | 27 |  |
| `0x1002e010` | `cmd_key` | 43 | GetAsyncKeyState |
| `0x1002e03b` | `cmd_skill` | 66 |  |
| `0x1002e07d` | `cmd_skillpc` | 80 |  |
| `0x1002e0cd` | `cmd_skilltime` | 168 | CONCAT,GetTickCount |
| `0x1002e175` | `cmd_lastmsg` | 11 |  |
| `0x1002e180` | `cmd_lastnavmsg` | 11 |  |
| `0x1002e18b` | `cmd_curmsg` | 114 | GetCurrentThreadId |
| `0x1002e1fd` | `cmd_target` | 41 |  |
| `0x1002e226` | `cmd_lastdmger` | 36 |  |
| `0x1002e24a` | `cmd_self` | 11 |  |
| `0x1002e255` | `cmd_followed` | 39 |  |
| `0x1002e27c` | `cmd_attacked` | 38 |  |
| `0x1002e2a2` | `cmd_pk` | 18 |  |
| `0x1002e2b4` | `cmd_pattacker` | 17 |  |
| `0x1002e2c5` | `cmd_mattacker` | 17 |  |
| `0x1002e2d6` | `cmd_attacker` | 17 |  |
| `0x1002e353` | `cmd_coretarget` | 8 |  |
| `0x1002e460` | `cmd_name` | 19 |  |
| `0x1002e473` | `cmd_id` | 25 |  |
| `0x1002e48c` | `cmd_posx` | 26 |  |
| `0x1002e4a6` | `cmd_distance` | 57 |  |
| `0x1002e4df` | `cmd_distx` | 37 |  |
| `0x1002e504` | `cmd_disty` | 37 |  |
| `0x1002e529` | `cmd_posy` | 26 |  |
| `0x1002e543` | `cmd_posz` | 26 |  |
| `0x1002e55d` | `cmd_dir` | 26 |  |
| `0x1002e577` | `cmd_outfit` | 26 |  |
| `0x1002e591` | `cmd_hppc` | 29 |  |
| `0x1002e5ae` | `cmd_speed` | 29 |  |
| `0x1002e5cb` | `cmd_isparalyzed` | 32 |  |
| `0x1002e5eb` | `cmd_color1` | 26 |  |
| `0x1002e605` | `cmd_color2` | 26 |  |
| `0x1002e61f` | `cmd_color3` | 26 |  |
| `0x1002e639` | `cmd_color4` | 26 |  |
| `0x1002e653` | `cmd_skull` | 29 |  |
| `0x1002e670` | `cmd_party` | 29 |  |
| `0x1002e68d` | `cmd_warbanner` | 29 |  |
| `0x1002e6aa` | `cmd_ismonster` | 26 |  |
| `0x1002e6c4` | `cmd_isnpc` | 41 |  |
| `0x1002e6ed` | `cmd_isplayer` | 26 |  |
| `0x1002e707` | `cmd_isonscreen` | 30 |  |
| `0x1002e725` | `cmd_isshootable` | 50 |  |
| `0x1002e757` | `cmd_canshoot` | 93 |  |
| `0x1002e7b4` | `cmd_isenemy` | 33 |  |
| `0x1002e7d5` | `cmd_isonnavi` | 31 |  |
| `0x1002e7f4` | `cmd_isleader` | 33 |  |
| `0x1002e815` | `cmd_isfriend` | 33 |  |
| `0x1002e836` | `cmd_issubenemy` | 33 |  |
| `0x1002e857` | `cmd_issubfriend` | 33 |  |
| `0x1002e878` | `cmd_haslookinfo` | 39 |  |
| `0x1002e89f` | `cmd_guild` | 26 |  |
| `0x1002e8b9` | `cmd_voc` | 30 |  |
| `0x1002e8d7` | `cmd_vocation` | 33 |  |
| `0x1002e8f8` | `cmd_level` | 25 |  |
| `0x1002e911` | `cmd_isknight` | 39 |  |
| `0x1002e938` | `cmd_ispaladin` | 39 |  |
| `0x1002e95f` | `cmd_issorcerer` | 39 |  |
| `0x1002e986` | `cmd_isdruid` | 39 |  |
| `0x1002e9ad` | `cmd_ismage` | 50 |  |
| `0x1002e9df` | `cmd_maxhp` | 27 |  |
| `0x1002e9fa` | `cmd_hp` | 27 |  |
| `0x1002ea15` | `cmd_maxmp` | 53 |  |
| `0x1002ea4a` | `cmd_mp` | 59 |  |
| `0x1002ea85` | `cmd_attackedme` | 36 |  |
| `0x1002eaa9` | `cmd_exposedcount` | 33 |  |
| `0x1002eaca` | `cmd_shotcount` | 33 |  |
| `0x1003068a` | `cmd_gotolabel` | 132 | GetTickCount |
| `0x1003070e` | `cmd_islocation` | 70 |  |
| `0x10030754` | `cmd_isdistance` | 101 |  |
| `0x100307b9` | `cmd_isnotdistance` | 101 |  |
| `0x1003081e` | `cmd_isnotlocation` | 70 |  |
| `0x10030864` | `cmd_skip` | 20 |  |
| `0x10030878` | `cmd_wait` | 71 | Sleep |
| `0x100308bf` | `cmd_refillammo` | 249 |  |
| `0x100309b8` | `cmd_countolditems` | 373 | GetTickCount,Sleep |
| `0x10030a3e` | `cmd_sspecial` | 29 |  |
| `0x10030a5b` | `cmd_countitems` | 18 |  |
| `0x10030b5c` | `cmd_getcount` | 34 |  |
| `0x10030b7e` | `cmd_countitemsvisible` | 25 |  |
| `0x10030b97` | `cmd_uh` | 181 |  |
| `0x10030c4c` | `cmd_ihpc` | 194 |  |
| `0x10030d0e` | `cmd_sd` | 66 |  |
| `0x10030d50` | `cmd_displaymap` | 80 |  |
| `0x10030da0` | `cmd_altnavdisplay` | 80 |  |
| `0x10030df0` | `cmd_hmm` | 66 |  |
| `0x10030e32` | `cmd_lmm` | 66 |  |
| `0x10030e74` | `cmd_icicle` | 66 |  |
| `0x10030eb6` | `cmd_stalagmite` | 66 |  |
| `0x10030ef8` | `cmd_aimtype` | 70 |  |
| `0x10030f3e` | `cmd_explo` | 66 |  |
| `0x10030f80` | `cmd_autoaim` | 56 |  |
| `0x10030fb8` | `cmd_follow` | 109 |  |
| `0x10031025` | `cmd_attack` | 115 |  |
| `0x10031098` | `cmd_whitebox` | 48 |  |
| `0x100310c8` | `cmd_ignoretarget` | 125 |  |
| `0x10031145` | `cmd_stopattack` | 99 |  |
| `0x100311a8` | `cmd_setattackmode` | 272 |  |
| `0x100312b8` | `cmd_autoheal` | 160 |  |
| `0x10031358` | `cmd_equipammy` | 70 |  |
| `0x1003139e` | `cmd_fastequipammy` | 61 |  |
| `0x100313db` | `cmd_equipring` | 124 |  |
| `0x10031457` | `cmd_equipsring` | 96 |  |
| `0x100314b7` | `cmd_equipboots` | 115 |  |
| `0x1003152a` | `cmd_equiphelm` | 88 |  |
| `0x10031582` | `cmd_equipchest` | 88 |  |
| `0x100315da` | `cmd_equiphead` | 88 |  |
| `0x10031632` | `cmd_equiplegs` | 88 |  |
| `0x1003168a` | `cmd_equiprhand` | 124 |  |
| `0x10031706` | `cmd_equiplhand` | 124 |  |
| `0x10031782` | `cmd_equipbelt` | 124 |  |
| `0x100317fe` | `cmd_equipback` | 88 |  |
| `0x10031856` | `cmd_say` | 79 | Sleep |
| `0x100318a5` | `cmd_allowwalk` | 31 |  |
| `0x100318c4` | `cmd_disallowwalk` | 31 |  |
| `0x100318e3` | `cmd_setalarm` | 247 | SendDlgItemMessageA |
| `0x100319da` | `cmd_flash` | 14 |  |
| `0x100319f5` | `cmd_savescreen` | 43 |  |
| `0x10031a20` | `cmd_changestance` | 289 |  |
| `0x10031b41` | `cmd_npcsay` | 79 | Sleep |
| `0x10031b90` | `cmd_gamesay` | 81 | Sleep |
| `0x10031be1` | `cmd_tradesay` | 81 | Sleep |
| `0x10031c32` | `cmd_rlsay` | 81 | Sleep |
| `0x10031c83` | `cmd_helpsay` | 81 | Sleep |
| `0x10031cd4` | `cmd_guildsay` | 81 | Sleep |
| `0x10031d25` | `cmd_sayin` | 147 | Sleep |
| `0x10031db8` | `cmd_navsay` | 77 |  |
| `0x10031e05` | `cmd_setautocombo` | 119 | SendDlgItemMessageA |
| `0x10031e7c` | `cmd_statusmessage` | 30 |  |
| `0x10031e9a` | `cmd_settradeoptions` | 208 |  |
| `0x10031f6a` | `cmd_buyitems` | 185 | Sleep |
| `0x10032023` | `cmd_buyitemsupto` | 223 | Sleep |
| `0x10032102` | `cmd_sellitemsdownto` | 152 | Sleep |
| `0x1003219a` | `cmd_sellitems` | 116 | Sleep |
| `0x1003220e` | `cmd_mana` | 140 |  |
| `0x10032219` | `cmd_smana` | 11 |  |
| `0x10032224` | `cmd_gmana` | 11 |  |
| `0x1003222f` | `cmd_gsmana` | 11 |  |
| `0x100322bb` | `cmd_health` | 139 |  |
| `0x100322c6` | `cmd_shealth` | 11 |  |
| `0x100322d1` | `cmd_ghealth` | 11 |  |
| `0x100322dc` | `cmd_uhealth` | 11 |  |
| `0x100322e7` | `cmd_gshealth` | 11 |  |
| `0x10032372` | `cmd_retarget` | 145 |  |
| `0x10032403` | `cmd_pm` | 48 |  |
| `0x10032433` | `cmd_auto` | 246 |  |
| `0x10032529` | `cmd_end` | 48 |  |
| `0x10032559` | `cmd_break` | 32 |  |
| `0x10032579` | `cmd_turnoff` | 28 |  |
| `0x10032595` | `cmd_reconnect` | 9 |  |
| `0x1003259e` | `cmd_connect` | 255 | GetPrivateProfileStringA,GetProcessHeap,HeapAlloc |
| `0x1003269d` | `cmd_setpos` | 56 |  |
| `0x100326d5` | `cmd_listboxsetup` | 145 | GetTickCount |
| `0x10032766` | `cmd_listboxaddline` | 157 | GetTickCount |
| `0x10032803` | `cmd_setcolor` | 74 |  |
| `0x1003284d` | `cmd_displaytext` | 47 |  |
| `0x1003287c` | `cmd_listas` | 51 |  |
| `0x100328af` | `cmd_dontlist` | 24 |  |
| `0x100328c7` | `cmd_sio` | 147 |  |
| `0x1003295a` | `cmd_usegrounditem` | 77 |  |
| `0x100329a7` | `cmd_opengrounditem` | 97 |  |
| `0x10032a08` | `cmd_playsound` | 30 |  |
| `0x10032a26` | `cmd_useitem` | 69 |  |
| `0x10032a6b` | `cmd_usegroundxyz` | 96 |  |
| `0x10032acb` | `cmd_opengroundxyz` | 99 |  |
| `0x10032b2e` | `cmd_reachgrounditem` | 82 | Sleep |
| `0x10032b80` | `cmd_skin` | 118 |  |
| `0x10032bf6` | `cmd_stake` | 118 |  |
| `0x10032c6c` | `cmd_moveto` | 50 |  |
| `0x10032c9e` | `cmd_addloot` | 27 |  |
| `0x10032cb9` | `cmd_setammy` | 19 |  |
| `0x10032ccc` | `cmd_seticontext` | 101 |  |
| `0x10032d31` | `cmd_seticonactive` | 124 |  |
| `0x10032dad` | `cmd_setoutfitcolor` | 211 |  |
| `0x10032e85` | `cmd_setoutfit` | 188 |  |
| `0x10032f46` | `cmd_setitemoutfit` | 105 |  |
| `0x10032fb1` | `cmd_setrelation` | 220 |  |
| `0x1003308d` | `cmd_setdebug` | 17 |  |
| `0x1003309e` | `cmd_getproperties` | 52 |  |
| `0x100330d2` | `cmd_gettile` | 73 |  |
| `0x1003311b` | `cmd_goinvisible` | 30 |  |
| `0x10033139` | `cmd_moveitems` | 123 | Sleep |
| `0x100331b4` | `cmd_movenitems` | 57 |  |
| `0x100331ed` | `cmd_moveitemsonto` | 200 | Sleep |
| `0x100332b7` | `cmd_openitem` | 50 |  |
| `0x100332e9` | `cmd_openbpitem` | 60 |  |
| `0x10033325` | `cmd_openbeltitem` | 60 |  |
| `0x10033361` | `cmd_closeallwindows` | 90 |  |
| `0x100333bb` | `cmd_reopenwindows` | 114 |  |
| `0x1003342d` | `cmd_loadcavebot` | 17 |  |
| `0x1003343e` | `cmd_loadtargeting` | 17 |  |
| `0x1003344f` | `cmd_loadsetting` | 17 |  |
| `0x10033460` | `cmd_loadscript` | 17 |  |
| `0x10033471` | `cmd_openitemnew` | 53 |  |
| `0x100334a6` | `cmd_useitemsonground` | 193 |  |
| `0x10033567` | `cmd_useongroundxyz` | 178 |  |
| `0x10033619` | `cmd_repeatuseongroundxyz` | 192 | Sleep |
| `0x100336d9` | `cmd_useongrounditem` | 159 |  |
| `0x10033778` | `cmd_useoninventoryitem` | 133 |  |
| `0x100337fd` | `cmd_useoncreature` | 162 |  |
| `0x1003389f` | `cmd_eatfood` | 9 |  |
| `0x100338a8` | `cmd_uhpc` | 195 |  |
| `0x1003396b` | `cmd_soulf` | 275 | GetTickCount |
| `0x10033a86` | `cmd_annisd` | 155 |  |
| `0x10033b23` | `cmd_fish` | 21 |  |
| `0x10033b38` | `cmd_safe` | 27 |  |
| `0x10033b53` | `cmd_filewrite` | 50 |  |
| `0x10033b85` | `cmd_filewriteline` | 50 |  |
| `0x10033bb7` | `cmd_log` | 30 |  |
| `0x10033bd5` | `cmd_filedelete` | 39 |  |
| `0x10033bfc` | `cmd_while` | 137 |  |
| `0x10033c87` | `cmd_loop` | 142 |  |
| `0x10033d17` | `cmd_foreach` | 1254 |  |
| `0x10034264` | `cmd_ifgm` | 27 |  |
| `0x1003427f` | `cmd_ifnogm` | 27 |  |
| `0x1003429a` | `cmd_ifplayeronscreen` | 27 |  |
| `0x100342b5` | `cmd_ifnoplayeronscreen` | 27 |  |
| `0x100342d0` | `cmd_ifdefaultmessage` | 27 |  |
| `0x100342eb` | `cmd_ifprivatemessage` | 27 |  |
| `0x10034306` | `cmd_ifplayerattacking` | 27 |  |
| `0x10034321` | `cmd_isposz` | 32 |  |
| `0x10034341` | `cmd_istargetname` | 91 |  |
| `0x1003439c` | `cmd_isattackedname` | 88 |  |
| `0x100343f4` | `cmd_isattacking` | 28 |  |
| `0x10034410` | `cmd_isnotattacking` | 28 |  |
| `0x1003442c` | `cmd_istargeting` | 27 |  |
| `0x10034447` | `cmd_isnottargeting` | 115 |  |
| `0x100344ba` | `cmd_isnotonscreen` | 96 |  |
| `0x1003451a` | `cmd_ifpoisoned` | 27 |  |
| `0x10034535` | `cmd_ifdrunk` | 27 |  |
| `0x10034550` | `cmd_ifhasted` | 27 |  |
| `0x1003456b` | `cmd_ifparalyzed` | 27 |  |
| `0x10034586` | `cmd_ifnotparalyzed` | 27 |  |
| `0x100345a1` | `cmd_ifnothasted` | 27 |  |
| `0x100345bc` | `cmd_ifmanashielded` | 27 |  |
| `0x100345d7` | `cmd_ifnotmanashielded` | 27 |  |
| `0x100345f2` | `cmd_haste` | 23 |  |
| `0x10034609` | `cmd_stronghaste` | 23 |  |
| `0x10034620` | `cmd_charge` | 23 |  |
| `0x10034637` | `cmd_swiftfoot` | 23 |  |
| `0x1003464e` | `cmd_manashield` | 41 |  |
| `0x10034677` | `cmd_ewave` | 38 |  |
| `0x1003469d` | `cmd_wave` | 36 |  |
| `0x100346c1` | `cmd_countlower` | 34 |  |
| `0x100346e3` | `cmd_counthigher` | 34 |  |
| `0x10034705` | `cmd_caplower` | 40 |  |
| `0x1003472d` | `cmd_caphigher` | 40 |  |
| `0x10034755` | `cmd_hplower` | 33 |  |
| `0x10034776` | `cmd_if` | 58 |  |
| `0x100347b0` | `cmd_exec` | 45 |  |
| `0x100347dd` | `cmd_ifnot` | 58 |  |
| `0x10034817` | `cmd_else` | 31 |  |
| `0x10034836` | `cmd_hpmissinglower` | 42 |  |
| `0x10034860` | `cmd_hpmissinghigher` | 42 |  |
| `0x1003488a` | `cmd_mpmissinglower` | 42 |  |
| `0x100348b4` | `cmd_mpmissinghigher` | 42 |  |
| `0x100348de` | `cmd_hphigher` | 33 |  |
| `0x100348ff` | `cmd_ringattacking` | 138 |  |
| `0x10034989` | `cmd_exivalast` | 50 |  |
| `0x100349bb` | `cmd_exivatarget` | 50 |  |
| `0x100349ed` | `cmd_lootitems` | 9 |  |
| `0x100349f6` | `cmd_stackitems` | 54 |  |
| `0x10034a2c` | `cmd_collectitems` | 379 |  |
| `0x10034ba7` | `cmd_pickupitemsamount` | 226 |  |
| `0x10034c89` | `cmd_pickupitems` | 340 | Sleep |
| `0x10034ddf` | `cmd_moveitemonground` | 124 |  |
| `0x10034e5b` | `cmd_dropitemsxyz` | 174 | Sleep |
| `0x10034e86` | `cmd_dropitemsxyzamount` | 110 |  |
| `0x10034ef4` | `cmd_dropitems` | 35 |  |
| `0x10034f9a` | `cmd_aimgfb` | 24 |  |
| `0x10034fb2` | `cmd_aimavalanche` | 24 |  |
| `0x10034fca` | `cmd_aimthunderstorm` | 24 |  |
| `0x10034fe2` | `cmd_aimstoneshower` | 24 |  |
| `0x10034ffa` | `cmd_logout` | 41 |  |
| `0x10035023` | `cmd_crosshair` | 85 |  |
| `0x10035078` | `cmd_xlog` | 24 |  |
| `0x10035090` | `cmd_throwpot` | 43 |  |
| `0x100350bb` | `cmd_pickuppot` | 9 |  |
| `0x100350c4` | `cmd_surroundpot` | 9 |  |
| `0x100350cd` | `cmd_magwall` | 63 |  |
| `0x1003510c` | `cmd_mwallcover` | 53 |  |
| `0x10035141` | `cmd_mwallshield` | 38 |  |
| `0x10035167` | `cmd_mplower` | 33 |  |
| `0x10035188` | `cmd_mphigher` | 33 |  |
| `0x100351a9` | `cmd_exorihur` | 143 |  |
| `0x10035238` | `cmd_exoricon` | 143 |  |
| `0x100352c7` | `cmd_exorigran` | 158 |  |
| `0x10035365` | `cmd_targethplower` | 65 |  |
| `0x100353a6` | `cmd_spydown` | 80 |  |
| `0x100353f6` | `cmd_spyup` | 80 |  |
| `0x10035446` | `cmd_refilldepletedmana` | 101 |  |
| `0x100354ab` | `cmd_refillhealth` | 99 |  |
| `0x1003550e` | `cmd_healparalysis` | 59 |  |
| `0x10035549` | `cmd_paralyze` | 83 |  |
| `0x1003559c` | `cmd_keepmagwall` | 80 |  |
| `0x100355ec` | `cmd_dashchase` | 45 |  |
| `0x10035619` | `cmd_dash` | 60 |  |
| `0x10035655` | `cmd_moven` | 27 |  |
| `0x1003565b` | `cmd_movee` | 6 |  |
| `0x10035661` | `cmd_moves` | 6 |  |
| `0x10035667` | `cmd_movew` | 6 |  |
| `0x1003566d` | `cmd_movene` | 6 |  |
| `0x10035673` | `cmd_movese` | 6 |  |
| `0x10035679` | `cmd_movesw` | 6 |  |
| `0x1003567f` | `cmd_movenw` | 6 |  |
| `0x10035685` | `cmd_turnn` | 6 |  |
| `0x1003568b` | `cmd_turne` | 6 |  |
| `0x10035691` | `cmd_turns` | 6 |  |
| `0x10035697` | `cmd_turnw` | 6 |  |
| `0x100356b2` | `cmd_scrollview` | 212 | WriteProcessMemory |
| `0x10035786` | `cmd_settargeting` | 129 | GetTickCount,SendDlgItemMessageA |
| `0x10035807` | `cmd_runtargeting` | 11 |  |
| `0x10035812` | `cmd_setcavebot` | 108 | SendDlgItemMessageA |
| `0x1003587e` | `cmd_setopennextbp` | 107 | SendDlgItemMessageA |
| `0x100358e9` | `cmd_set` | 233 |  |
| `0x100359d8` | `cmd_clear` | 106 |  |
| `0x10035a44` | `cmd_inc` | 132 |  |
| `0x10035aca` | `cmd_dec` | 111 |  |
| `0x10035b3b` | `cmd_swapequip` | 58 |  |
| `0x10035b75` | `cmd_unequip` | 160 |  |
| `0x10035c15` | `cmd_setcaption` | 18 |  |
| `0x10035c27` | `cmd_makerune` | 39 |  |

