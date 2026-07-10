# elfbot.dll function catalog — core (.jdrv, bot code)

Offline recovery (capstone) of every function in the `.jdrv` section — ElfBot's own logic. Columns: address, size (bytes), Win32 APIs called (via IAT), notable string literals referenced. Named/deep functions are cross-referenced in docs 05–10. Import thunks excluded.

498 functions.

| Address | Size | APIs called | Strings |
|---|---|---|---|
| `0x10001057` | 52 | - |  |
| `0x100010bf` | 161 | CreateThread,GetCurrentProcess,gethostbyname,inet_addr |  |
| `0x10001160` | 16 | - |  |
| `0x10001170` | 178 | GetCurrentProcess,WriteProcessMemory,gethostbyname,inet_addr |  |
| `0x10001222` | 76 | closesocket,shutdown |  |
| `0x1000126e` | 209 | lstrlen |  |
| `0x1000133f` | 6 | - |  |
| `0x1000134b` | 334 | - |  |
| `0x10001499` | 28 | - |  |
| `0x100014bb` | 0 | - |  |
| `0x1000154b` | 83 | - |  |
| `0x1000159e` | 6 | - |  |
| `0x100015a4` | 356 | - |  |
| `0x10001708` | 217 | lstrlen |  |
| `0x100017e1` | 50 | - |  |
| `0x10001813` | 93 | - |  |
| `0x10001870` | 27 | - |  |
| `0x1000188b` | 158 | - |  |
| `0x10001929` | 55 | - |  |
| `0x10001960` | 310 | GlobalAlloc,GlobalLock |  |
| `0x10001b4a` | 85 | - |  |
| `0x10001b9f` | 153 | GetTickCount |  |
| `0x10001c38` | 82 | - |  |
| `0x1000239b` | 46 | - |  |
| `0x100023c9` | 57 | - |  |
| `0x10002992` | 18 | - |  |
| `0x10002bdd` | 36 | GetCurrentProcess,WriteProcessMemory |  |
| `0x10002c01` | 30 | - |  |
| `0x10002c1f` | 9 | - |  |
| `0x10002c6e` | 25 | - |  |
| `0x10002c87` | 55 | SendMessageA |  |
| `0x10002cbe` | 74 | Sleep |  |
| `0x10002d16` | 48 | SendMessageA |  |
| `0x10002d46` | 824 | GetModuleFileNameA,InitCommonControls,LoadCursorA,LoadIconA | TBOTDLG7 TBOTDLGA TBOTDLGB TBOTDLGC TBOTDLGD TBOTDLGE |
| `0x1000307e` | 88 | GetDlgItem,SendMessageA |  |
| `0x100030d6` | 112 | CreateDirectoryA,lstrcat,lstrcpy,wsprintfA | playerinfo\ %s\playerinfo\%c\ |
| `0x10006b62` | 108 | GetOpenFileNameA | All Files Select or type a filename to be used as save slot |
| `0x10006c65` | 107 | EnableWindow,GetDlgItem,SendDlgItemMessageA |  |
| `0x10006cd0` | 107 | EnableWindow,GetDlgItem,SendDlgItemMessageA |  |
| `0x10007a08` | 333 | SendDlgItemMessageA,closesocket,shutdown | Disconnect Connect |
| `0x10008152` | 306 | lstrcpy |  |
| `0x10008284` | 306 | lstrcpy |  |
| `0x10008a7e` | 963 | SendDlgItemMessageA,lstrcat | Don't |
| `0x10008e41` | 523 | RtlZeroMemory,lstrcat,lstrcpy,mmioAscend,mmioClose,mmioDescend,mmioOpenA,mmioRead |  |
| `0x1000904c` | 246 | DirectSoundCreate,RtlZeroMemory |  |
| `0x100092b0` | 191 | - | sounds\elfng.wav sounds\playeronscreen.wav sounds\gmdetected.wav sound |
| `0x1000936f` | 52 | - |  |
| `0x100093a3` | 175 | shutdown |  |
| `0x10009452` | 55 | FlashWindowEx |  |
| `0x10009489` | 197 | shutdown |  |
| `0x1000954e` | 177 | lstrcmpi,lstrcpy,wsprintfA | sounds\%s |
| `0x1000d287` | 83 | lstrcmpi |  |
| `0x1000d2da` | 1680 | - | Trace paths space exceeded! Trace paths space exceeded! Trace paths sp |
| `0x1000d9b8` | 1786 | - | Trace paths space exceeded! Trace paths space exceeded! Trace paths sp |
| `0x1000e100` | 1465 | - | Trace paths space exceeded! Trace paths space exceeded! Trace paths sp |
| `0x1000e6b9` | 3405 | - | Trace paths space exceeded! Trace paths space exceeded! Trace paths sp |
| `0x1000f40a` | 2978 | - | Trace paths space exceeded! Trace paths space exceeded! Trace paths sp |
| `0x1000ffb0` | 2876 | - | Trace paths space exceeded! Trace paths space exceeded! Trace paths sp |
| `0x10010af0` | 2764 | - | Trace paths space exceeded! Trace paths space exceeded! Trace paths sp |
| `0x100115bc` | 188 | - |  |
| `0x10011678` | 375 | - |  |
| `0x100117ef` | 333 | - |  |
| `0x1001193c` | 333 | - |  |
| `0x10011a89` | 105 | - |  |
| `0x10011af2` | 2363 | lstrcmpi |  |
| `0x1001242d` | 836 | - |  |
| `0x10012771` | 182 | - |  |
| `0x10012827` | 485 | lstrcmpi | others |
| `0x10012a0e` | 160 | lstrcmpi |  |
| `0x10012aae` | 715 | - |  |
| `0x10012d79` | 196 | - |  |
| `0x10012e3d` | 158 | - |  |
| `0x10012edb` | 27 | - |  |
| `0x10012ef6` | 3927 | - |  |
| `0x10013e4d` | 201 | - |  |
| `0x10013f16` | 1188 | - |  |
| `0x100147eb` | 58 | - |  |
| `0x10014825` | 149 | - |  |
| `0x100148ba` | 109 | - |  |
| `0x10014927` | 108 | - |  |
| `0x10014993` | 122 | - |  |
| `0x10014a0d` | 97 | - |  |
| `0x10014a6e` | 127 | - |  |
| `0x10014aed` | 14 | - |  |
| `0x10014afb` | 122 | - |  |
| `0x10014b75` | 122 | - |  |
| `0x10014bef` | 122 | - |  |
| `0x10014c69` | 268 | - |  |
| `0x10014d75` | 239 | - |  |
| `0x10014e64` | 172 | - |  |
| `0x10014f10` | 740 | - |  |
| `0x100151f4` | 16 | - |  |
| `0x10015204` | 36 | - |  |
| `0x10015228` | 63 | lstrcpy,wsprintfA |  >>  %s %s %s |
| `0x10015267` | 950 | DlgDirListA,SendDlgItemMessageA,lstrcat,lstrcpy,lstrlen,wsprintfA | <New Monster> %d %d %d %s scripts\*.elft |
| `0x1001561d` | 177 | - |  |
| `0x100156ce` | 373 | CloseHandle,CreateFileA,GetProcessHeap,GetSaveFileNameA,HeapAlloc,HeapFree,WriteFile,lstrcat … | Targeting Files Select a Targeting file to save scripts\ .elft |
| `0x10015843` | 405 | CloseHandle,CreateFileA,GetFileSize,GetOpenFileNameA,GetProcessHeap,HeapAlloc,HeapFree,ReadFile … | Targeting Files Select a Targeting file to open scripts\ .elft |
| `0x100159d8` | 37 | MessageBoxA | ElfBot was unable to save your settings. If you are running  |
| `0x100159fd` | 380 | CloseHandle,CreateFileA,GetProcessHeap,GetSaveFileNameA,HeapAlloc,HeapFree,WriteFile,lstrcat … | Cavebot Files Select a Cavebot file to save scripts\ .elfc |
| `0x10015b79` | 545 | CloseHandle,CreateFileA,GetFileSize,GetOpenFileNameA,GetProcessHeap,HeapAlloc,HeapFree,ReadFile … | Cavebot Files Select a Cavebot file to open scripts\ .elfc |
| `0x10015da3` | 569 | SendDlgItemMessageA,lstrcat | Center North East South West North-West |
| `0x10015fdc` | 151 | wsprintfA | T 00%d: %s T 0%d: %s T %d: %s T 00%d: %d %d %d T 0%d: %d %d %d T %d: % |
| `0x10016073` | 99 | wsprintfA | %05d %s %s %05d %s %s %05d %s %s %05d %02d %s |
| `0x100160d6` | 525 | SendDlgItemMessageA | <Delete if unused> <New Entry> |
| `0x100162e3` | 245 | DlgDirListA,SendDlgItemMessageA,lstrcat,lstrcpy,lstrlen | scripts\*.elfc |
| `0x100163d8` | 96 | GetTickCount,SendDlgItemMessageA |  |
| `0x10016438` | 947 | lstrcpy,lstrcpyn,lstrlen,wsprintfA | Delay_%dsec wait %d000 |
| `0x100167eb` | 129 | CloseHandle,CreateFileA,GetFileSize,GetProcessHeap,HeapAlloc,HeapFree,ReadFile |  |
| `0x1001686c` | 8275 | IsWindow,MessageBoxA,lstrcat,lstrcmpi,lstrcpyn,wsprintfA | Waypoints Looting CavebotOptions Alerts CavebotHotkeys TargetingMonste |
| `0x100188bf` | 58 | SendDlgItemMessageA,SendMessageA |  |
| `0x100188f9` | 1169 | GlobalAlloc,GlobalFree,GlobalLock,GlobalUnlock,SendDlgItemMessageA,lstrcat,lstrcpy,wsprintfA | [Waypoints] TWRLSAHNUU %c %d %d %d Rope:  Rope Elvenhair rope |
| `0x10018d8a` | 1559 | GlobalAlloc,GlobalFree,GlobalLock,GlobalUnlock,SendDlgItemMessageA,lstrcat,lstrcpy,wsprintfA | [TargetingMonsters] [TargetSelection] |
| `0x100193a1` | 944 | GlobalAlloc,GlobalFree,GlobalLock,GlobalUnlock,SendDlgItemMessageA,lstrcat,lstrcpy,wsprintfA | [Icons] |
| `0x1001b6df` | 310 | SendDlgItemMessageA |  |
| `0x1001b815` | 134 | SendDlgItemMessageA | <New Icon> |
| `0x1001b89b` | 35 | - |  |
| `0x1001cc41` | 112 | CreateSolidBrush,SelectObject,SetBkColor,SetBkMode,SetTextColor,ShowWindow |  |
| `0x1001ccb1` | 542 | SendDlgItemMessageA,lstrcat,lstrcpy |  {creature}  {num}  {hp%}  {hp}  {mp}  {itemid} |
| `0x1001cecf` | 103 | - |  |
| `0x1001cf36` | 539 | SendDlgItemMessageA,lstrcat,wsprintfA |  {creature}  {num}  {hp%}  {hp}  {mp}  {itemid} |
| `0x1001f57d` | 64 | IsWindow,SetFocus,ShowWindow |  |
| `0x1001f5bd` | 2882 | DestroyWindow,IsWindow,SendDlgItemMessageA,SendMessageA |  |
| `0x100200ff` | 212 | CloseHandle,CreateFileA,WriteFile,lstrcat,lstrcpy |  |
| `0x100201d3` | 570 | CloseHandle,CreateFileA,CreateFileMappingA,GetFileSize,MapViewOfFile,UnmapViewOfFile,lstrcat,lstrcpy | Default |
| `0x1002040d` | 162 | CloseHandle,CreateFileA,CreateFileMappingA,GetFileSize,MapViewOfFile,UnmapViewOfFile,lstrcat,lstrcpy | lootitems.txt |
| `0x100204af` | 272 | - |  |
| `0x100205bf` | 838 | closesocket,shutdown |  |
| `0x10020905` | 75 | lstrlen |  |
| `0x10020950` | 133 | send |  |
| `0x10020c48` | 67 | TlsSetValue |  |
| `0x100212a3` | 52 | - |  |
| `0x100212d7` | 72 | - |  |
| `0x1002131f` | 2314 | lstrcat,lstrcpy | Error occured in the following packet:  |
| `0x10021c2d` | 545 | - | exori vis exori mort exori flam exori frigo exori terra exori san |
| `0x10021e4e` | 132 | - |  |
| `0x10021ed2` | 52 | - |  |
| `0x10021f06` | 52 | - |  |
| `0x10021f3a` | 50 | QueryPerformanceCounter,QueryPerformanceFrequency |  |
| `0x10022566` | 599 | CloseHandle,CreateFileA,ReadFile,WriteFile,lstrcpyn,lstrlen,wsprintfA | %s\playerinfo\%c\%s.txt %s\playerinfo\%c\%s.txt |
| `0x1002355e` | 138 | - |  |
| `0x100235e8` | 431 | - |  |
| `0x10023797` | 13 | - |  |
| `0x100237a4` | 189 | - |  |
| `0x10023861` | 26 | - |  |
| `0x1002387b` | 24 | GetTickCount |  |
| `0x10023893` | 434 | - |  |
| `0x10023a45` | 74 | - |  |
| `0x10023a8f` | 947 | - |  |
| `0x10023e42` | 96 | - |  |
| `0x10023ea2` | 527 | GetTickCount,SetWindowTextA,lstrcat,lstrcpy,lstrlen,wsprintfA |    CiroScript.com     - %s -   - Slot %d -   exp/hour |
| `0x100240b1` | 287 | FindWindowExA,GetCurrentProcessId,GetWindowThreadProcessId,IsIconic,SendMessageA,ShowWindow | TibiaClient |
| `0x10024209` | 45 | - |  |
| `0x100244e1` | 790 | CreateThread,GetCommandLineA,GetPrivateProfileStringA,GetProcessHeap,GetTickCount,HeapAlloc,InitializeCriticalSection,WSAStartup … | localhost 7177 7177 7180 localhost 7180 |
| `0x100247f7` | 165 | - |  |
| `0x1002489c` | 145 | - |  |
| `0x1002492d` | 897 | - | PQS; [YX; [YX; [YX; |
| `0x10024d66` | 467 | - | exevo vis hur |
| `0x10024f39` | 117 | - |  |
| `0x10024fae` | 61 | - |  |
| `0x10024feb` | 391 | GetTickCount,lstrcpy | ""3c None |
| `0x10025172` | 328 | CloseHandle,CreateFileA,GetDateFormatA,GetProcessHeap,GetTickCount,GetTimeFormatA,HeapAlloc,HeapFree … | elferrors459.log 'Elfbot NG 4.5.9 - Entry Started on 'dddd' 'MMMM' 'dd |
| `0x100252ba` | 287 | CloseHandle,CreateFileA,GetDateFormatA,GetTickCount,GetTimeFormatA,SetFilePointer,WriteFile,lstrcat … | 'Elfbot NG 4.5.9 - Entry Started on 'dddd' 'MMMM' 'dd', 'yyy elfscript |
| `0x100253d9` | 287 | CloseHandle,CreateFileA,GetDateFormatA,GetTickCount,GetTimeFormatA,SetFilePointer,WriteFile,lstrcat … | 'Elfbot NG 4.5.9 - Entry Started on 'dddd' 'MMMM' 'dd', 'yyy elflock45 |
| `0x100254f8` | 334 | CloseHandle,CreateFileA,GetFileSize,GetProcessHeap,HeapAlloc,HeapFree,ReadFile,lstrcat … |  |
| `0x10025646` | 504 | CloseHandle,CreateFileA,GetFileSize,GetProcessHeap,HeapAlloc,HeapFree,ReadFile,lstrcat … |  |
| `0x1002583e` | 241 | CloseHandle,CreateFileA,DeleteFileA,SetFilePointer,WriteFile,lstrcat,lstrcpy,lstrcpyn … |  |
| `0x1002592f` | 330 | CreateFileA,GetTickCount,SetFilePointer,WriteFile,lstrcat,lstrcpy,lstrlen | elflog.txt |
| `0x10025a79` | 1171 | GetTickCount,lstrcpy,wsprintfA | ""3c None |
| `0x10025f0c` | 1076 | lstrcmp,lstrcpy,lstrcpyn |  |
| `0x10026340` | 219 | Sleep,send |  |
| `0x10026571` | 98 | - |  |
| `0x100265d3` | 137 | - |  |
| `0x100266b1` | 81 | lstrlen |  |
| `0x10026702` | 34 | - |  |
| `0x10026724` | 859 | lstrcmpi,lstrlen | party channel |
| `0x10026a7f` | 96 | WritePrivateProfileStringA,lstrcat,lstrcpy | serverlist.txt Servers |
| `0x10028970` | 126 | GetTickCount,lstrcmp,lstrcpy |  |
| `0x100289ee` | 775 | - | =to tu =veryu =far u =on au9 =highu =soutuU |
| `0x10028cf5` | 23 | - |  |
| `0x10028d0c` | 608 | wsprintfA | +%d%c Invis |
| `0x10029010` | 2365 | lstrcpy,wsprintfA | TWRLSAHNUU %c%d %s +%d %s %d |
| `0x1002994d` | 50 | - |  |
| `0x1002997f` | 226 | GetTickCount |  |
| `0x10029a61` | 218 | lstrcmp,lstrcpyn |  |
| `0x10029b3b` | 515 | lstrcpy |  |
| `0x1002a092` | 166 | - |  |
| `0x1002a138` | 473 | - |  |
| `0x1002a311` | 290 | - |  |
| `0x1002a433` | 1380 | ExitProcess,GlobalAlloc,VirtualProtect,WriteProcessMemory |  |
| `0x1002a9b0` | 83 | - | SQRVW _^ZY[ _^ZY[ |
| `0x1002ade7` | 136 | EnterCriticalSection,LeaveCriticalSection |  |
| `0x1002ae6f` | 18 | - |  |
| `0x1002ae81` | 17 | - |  |
| `0x1002ae92` | 176 | - |  |
| `0x1002af42` | 39 | GetAsyncKeyState |  |
| `0x1002af69` | 194 | GetAsyncKeyState,IsWindow,SendDlgItemMessageA | lmouse |
| `0x1002b02b` | 115 | RegisterHotKey,UnregisterHotKey |  |
| `0x1002b09e` | 3018 | ExitThread,GetAsyncKeyState,GetTickCount,lstrcpy |  |
| `0x1002bc68` | 458 | ExitThread,GetAsyncKeyState,GetTickCount |  |
| `0x1002be32` | 165 | - |  |
| `0x1002bed7` | 97 | - |  |
| `0x1002bf38` | 159 | wsprintfA | %02dh%02dm%02ds %02d:%02d:%02d RPSVh4 %02dd%02dh%02dm%02ds %02d:%02d:% |
| `0x1002bfd7` | 160 | wsprintfA | %d,%03d,%03d,%03d %d,%03d,%03d %d,%03d |
| `0x1002c077` | 84 | lstrcmpi | count |
| `0x1002c0cb` | 156 | lstrcmpi | fist club sword distance shielding |
| `0x1002c167` | 79 | lstrcmpi | fishing mlevel |
| `0x1002c1b6` | 114 | MessageBoxA |  |
| `0x1002c228` | 1561 | lstrcat,lstrcmpi,lstrcpy,lstrlen |  |
| `0x1002c842` | 5802 | GetDateFormatA,GetTickCount,GetTimeFormatA,lstrcat,lstrcmp,lstrcmpi,lstrcpy,lstrlen … | 99h99m99s 99:99:99 HH':'mm':'ss dddd', 'MMMM' 'dd' 'yyyy |
| `0x1002def1` | 6 | - |  |
| `0x1002ff87` | 28 | - |  |
| `0x1002ffa3` | 81 | - |  |
| `0x1002fff4` | 89 | lstrcmpi,lstrlen |  |
| `0x1003004d` | 129 | - |  |
| `0x100300ce` | 343 | - |  |
| `0x10030225` | 257 | - |  |
| `0x10030326` | 152 | lstrcpy |  |
| `0x100303be` | 132 | lstrcmpi |  |
| `0x10030442` | 584 | lstrcmp |  |
| `0x10033dfd` | 54 | lstrcmpi | allmonsters |
| `0x10033e33` | 54 | lstrcmpi | allplayers |
| `0x10033e69` | 56 | lstrcmpi | floormonsters |
| `0x10033ea1` | 56 | lstrcmpi | floorplayers |
| `0x10033ed9` | 56 | lstrcmpi | floorcreatures |
| `0x10033f11` | 56 | lstrcmpi | screenplayers |
| `0x10033f4a` | 55 | lstrcmpi | screenmonsters |
| `0x10033f82` | 13 | - |  |
| `0x10033fba` | 13 | - |  |
| `0x10033ff3` | 12 | - |  |
| `0x1003402b` | 53 | lstrcmpi | shootablecreatures |
| `0x10034060` | 512 | lstrcmpi,lstrcpy,wsprintfA | newmessages |
| `0x10035cd2` | 1862 | - | countolditems countitems sspecial getcount countitemsvisible ihpc |
| `0x1003641a` | 6 | - |  |
| `0x100366f8` | 7 | - |  |
| `0x1003672b` | 1 | - |  |
| `0x10036bb2` | 213 | lstrcmpi | helmet amulet backpack chest lhand rhand |
| `0x10036c87` | 296 | - | ;S0s ;S8r |
| `0x10036daf` | 186 | lstrcmpi | empty empty1 |
| `0x10036e69` | 77 | - |  |
| `0x10036eb6` | 586 | Sleep |  |
| `0x10037100` | 253 | - |  |
| `0x100371fd` | 391 | - |  |
| `0x10037384` | 310 | - |  |
| `0x100374ba` | 287 | - |  |
| `0x100375d9` | 187 | - |  |
| `0x10037694` | 311 | - |  |
| `0x100377cb` | 424 | - |  |
| `0x10037973` | 67 | - |  |
| `0x100379b6` | 89 | wsprintfA | Level spy off. Spying on level +%d. Spying on level -%d. |
| `0x10037a0f` | 89 | - |  |
| `0x10037a68` | 164 | - |  |
| `0x10037b0c` | 358 | - |  |
| `0x10037c72` | 786 | lstrcmpi | enemy subenemy friend subfriend sorcerer druid |
| `0x10037f84` | 29 | - |  |
| `0x10037fa1` | 316 | - |  |
| `0x100380dd` | 876 | lstrcmpi | enemy subenemy sorcerer druid knight paladin |
| `0x10038449` | 178 | - |  |
| `0x100384fb` | 387 | - |  |
| `0x1003867e` | 167 | - |  |
| `0x10038725` | 393 | - |  |
| `0x100388ae` | 580 | GetTickCount |  |
| `0x10038af6` | 554 | - |  |
| `0x10038d20` | 28 | - |  |
| `0x10038e29` | 138 | lstrlen |  |
| `0x10038eb3` | 743 | lstrcmpi | enemy subenemy anyenemy friend subfriend anyfriend |
| `0x1003919a` | 223 | - |  |
| `0x1003927b` | 191 | - |  |
| `0x10039357` | 29 | WriteProcessMemory |  |
| `0x10039374` | 78 | WriteProcessMemory,lstrlen |  |
| `0x100393c2` | 81 | lstrlen |  |
| `0x10039413` | 74 | lstrlen |  |
| `0x1003945d` | 74 | lstrlen |  |
| `0x100394a7` | 676 | IsWindow,SendDlgItemMessageA,lstrcmp,lstrcpy,lstrlen |  |
| `0x1003974b` | 85 | lstrcat,lstrcpy | ***Level  |
| `0x100397a0` | 433 | lstrcat,lstrcmp,lstrlen | Pos: (   Health:    Speed:  |
| `0x10039951` | 45 | - |  |
| `0x1003997e` | 49 | - |  |
| `0x100399af` | 65 | lstrcmpi |  |
| `0x100399f0` | 98 | lstrcmpi |  |
| `0x10039a52` | 103 | - |  |
| `0x10039ab9` | 169 | - |  |
| `0x10039b62` | 89 | FindWindowExA,GetCurrentProcessId,GetWindowThreadProcessId | TibiaClient |
| `0x10039bbb` | 198 | FindWindowExA,GetCurrentProcessId,GetWindowThreadProcessId,SendMessageA,Sleep | TibiaClient |
| `0x10039c81` | 265 | GetClientRect,SendMessageA,SetWindowPos,VirtualProtect |  |
| `0x10039d8a` | 376 | - |  |
| `0x10039f02` | 101 | - |  |
| `0x10039f67` | 97 | - |  |
| `0x10039fc8` | 38 | - |  |
| `0x10039fee` | 81 | - |  |
| `0x1003a03f` | 38 | - |  |
| `0x1003a065` | 147 | - |  |
| `0x1003a0f8` | 80 | - |  |
| `0x1003a148` | 46 | - |  |
| `0x1003a176` | 52 | - |  |
| `0x1003a1aa` | 59 | - |  |
| `0x1003a1e5` | 315 | - |  |
| `0x1003a320` | 186 | lstrcmpi |  |
| `0x1003a3da` | 186 | lstrcmpi |  |
| `0x1003a494` | 188 | lstrcmpi |  |
| `0x1003a550` | 186 | lstrcmpi |  |
| `0x1003a60a` | 1168 | - | exori vis exori mort exori flam exori frigo exori tera exori san |
| `0x1003b0f0` | 55 | - |  |
| `0x1003b127` | 50 | - |  |
| `0x1003b159` | 210 | lstrcat,lstrcpy |  |
| `0x1003b22b` | 2052 | GetTickCount,lstrcat,lstrcpy,wsprintfA | lmouse %s: %s cb%d: %s pb%d: %s %s: %s Ping  :    |
| `0x1003ba2f` | 243 | - |  |
| `0x1003bb22` | 159 | - | ""3DD |
| `0x1003bbc1` | 72 | - |  |
| `0x1003bc09` | 75 | - |  |
| `0x1003bc54` | 67 | - |  |
| `0x1003bc97` | 558 | - |  |
| `0x1003bec5` | 40 | - |  |
| `0x1003beed` | 255 | - |  |
| `0x1003bfec` | 109 | - |  |
| `0x1003c23e` | 83 | - |  |
| `0x1003c291` | 82 | - |  |
| `0x1003c2e3` | 44 | - |  |
| `0x1003c313` | 30 | - |  |
| `0x1003c36f` | 113 | - |  |
| `0x1003c3e3` | 14 | - |  |
| `0x1003c3fc` | 52 | - |  |
| `0x1003c462` | 52 | - |  |
| `0x1003c496` | 50 | - |  |
| `0x1003c4c8` | 50 | - |  |
| `0x1003c4fa` | 48 | - |  |
| `0x1003c52a` | 51 | - |  |
| `0x1003c55d` | 443 | - |  |
| `0x1003c718` | 356 | - |  |
| `0x1003c87c` | 38 | - |  |
| `0x1003c8a2` | 45 | - |  |
| `0x1003c936` | 135 | - |  |
| `0x1003c9bd` | 70 | - |  |
| `0x1003ca03` | 423 | - |  |
| `0x1003cbaa` | 861 | - |  |
| `0x1003cf0b` | 0 | - |  |
| `0x1003d1b7` | 1112 | - |  |
| `0x1003d60f` | 289 | - |  |
| `0x1003d730` | 64 | - |  |
| `0x1003d770` | 212 | - |  |
| `0x1003d844` | 88 | - |  |
| `0x1003d89c` | 259 | GetThreadContext,GetTickCount,wsprintfA | Locked on hotkey: '%s' on command '%s' %d ms Error: %d %lX % Locked on |
| `0x1003e2a0` | 173 | - |  |
| `0x1003e5f2` | 440 | - |  |
| `0x1003e7aa` | 41 | - |  |
| `0x1003e7d3` | 432 | - |  |
| `0x1003e983` | 177 | - |  |
| `0x1003ec1e` | 174 | - |  |
| `0x1003ecf9` | 1690 | CloseHandle,CreateThread,GetTickCount,TerminateThread |  |
| `0x1003f393` | 13 | - |  |
| `0x1003f3a0` | 567 | GetProcessHeap,HeapAlloc |  |
| `0x1003f5d7` | 1208 | CloseHandle,CreateFileA,GetFileSize,GetProcessHeap,HeapAlloc,HeapFree,ReadFile,WriteFile … | %sminimaps\%d\%d.elfm %sminimaps\%d\blankmaps.elfm =fff %sminimaps\%d\ |
| `0x1003ffdf` | 458 | send |  |
| `0x100401a9` | 78 | - |  |
| `0x100401f7` | 83 | - |  |
| `0x10040272` | 166 | - |  |
| `0x10040318` | 814 | BitBlt,CloseClipboard,CloseHandle,CreateCompatibleBitmap,CreateCompatibleDC,CreateFileA,DeleteObject,EmptyClipboard … | .bmp '_'yyMMdd '_'HHmmss'.bmp' |
| `0x10040900` | 54 | - |  |
| `0x10040940` | 101 | - |  |
| `0x100409a8` | 42 | - |  |
| `0x100409e0` | 77 | - |  |
| `0x10040a30` | 70 | - |  |
