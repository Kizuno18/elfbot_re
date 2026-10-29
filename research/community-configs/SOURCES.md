# community corpus provenance

access date for all entries: 2026-09-06

these are text-only excerpts copied from public historical pages. they are not executable here and are not represented as verified working bot profiles. the source pages describe elfbot ng / tibia 8.60 unless noted. hashes are sha-256 of the local corpus file bytes

| local file | direct source | title / date | type | sha-256 | authenticity and version note |
| --- | --- | --- | --- | --- | --- |
| `webcheats/hotkeys/elfbot-hotkeys-sample.txt` | https://www.webcheats.com.br/topic/85571-scripts-hotkeys-e-shortkeys-de-ng-e-elfbot/ | Scripts, hotkeys e shortkeys de ng e elfbot / 2009 page, historical forum | hotkeys | `3119a7fa24d2e98eaf745a46abc302e331ac124a32d6d7a0ec335cad2edd328e` | user-posted Portuguese examples; page labels NG/ElfBot but does not identify a precise client build |
| `fodastico/hotkeys/elfbot-hotkeys-sample.txt` | https://fodasticobaiak.blogspot.com/p/hotkeys_7.html | Hotkeys Elfbot / page states Tibia 8.6 | hotkeys | `4467a28a52c611a39bc031fd69092de4e5cd5c661edadc9145d01e8db95b0d34` | public blog snippets; likely copied/curated community scripts, syntax may include server-specific conventions |
| `fodastico/hotkeys/anti-push.txt` | https://fodasticobaiak.blogspot.com/p/hotkeys_7.html | Hotkeys Elfbot / page states Tibia 8.6 | hotkey | `15b872b7feb6adf8b78974d1513b239cb11ae3603592678bc0dfe2a9607816b1` | copied code block; item IDs and anti-push behavior are server/config dependent |
| `fodastico/hotkeys/anti-idle.txt` | https://fodasticobaiak.blogspot.com/p/hotkeys_7.html | Hotkeys Elfbot / page states Tibia 8.6 | hotkey | `a1792c54338417d65308c44d3bcd8e5848325000065eab9360e3e6b36f8f1d7a` | copied code block; `$time`/`$idletime` behavior should be treated as historical syntax |
| `ricardogalvis/hotkeys/push-max-on-target.txt` | https://ricardogalvis.wixsite.com/elfbot-hotkeys/push-max-on-target-with-numpad-comp | Push Max On Target / page titled ElfBot NG 8.60 | hotkey | `357af787dc3553fa9c5fcb085b15fc7305b48e227485c09d1b834470dcdffab6` | first-party tutorial page for the site author; preserved representative code lines, not a full saved profile |
| `elfbot-brasil/hotkeys/actions-reference.txt` | https://www.elfbot.com.br/2023/01/lista-de-acoes-e-condicoes-para-elfbot.html | Lista de Ações e Condições para Elfbot / 2023-01-07 | command reference | `3ecd0a2d410343a8fe72fd47eb4fde5ea9e0ab9917a2c6139f7707f3a1a24969` | reference transcription, not a runnable profile; article documents `loadcavebot`, `loadtargeting`, and `.elfs` text scripts |
| `mpcforum/hotkeys/load-cavebot.txt` | https://www.mpcforum.pl/topic/1453207-elfbot-wpt-pomocy/ | ElfBot WPT Pomocy / 2015-08 | hotkeys | `095e2645572778e17453d81dca2400c595787b30027aea64e51a1fa9d12dab68` | forum replies with placeholders (`ID`, `x`, script names); useful syntax sample, incomplete by design |
| `tibiadash/hotkeys/pz-runner.txt` | https://www.tibiadash.com/2010/03/tutorial-elfbot-ng-depot-mana-e-soft.html | Tutorial Elfbot NG – Depot, Mana e Soft refiller / 2010-03 | hotkey | `3c7fdf1e0ba27b9cfbb61bc6aa82d8bc90e70ae1fd36e5e92aaa6df2824de590` | page attributes script to `advanced_killer`; historical ElfBot NG syntax, intended as a safety/cavebot-switch example |
| `tibiadash/cavebot/depot-softboots.txt` | https://www.tibiadash.com/2010/03/tutorial-elfbot-ng-depot-mana-e-soft.html | Tutorial Elfbot NG – Depot, Mana e Soft refiller / 2010-03 | cavebot action excerpt | `7fa18352ce37702ec54812094bc50113f19fb3271efff0b1428cc2328e0bf808` | copied action lines; contains an explicit `(ITEM ID)` placeholder and should not be treated as a complete route |

## format evidence and unavailable artifacts

the historical Tibiaking guide documents that ElfBot stores targeting as `.elft` and cavebot/waypoint profiles as `.elfc`: https://tibiaking.com/topic/218-compartilhando-scripts-e-importando-do-tibiabot-ng/

the 2010 MPCForum post listed direct `.elfc` and `.elft` links for Venore Swamp Trolls, but both tested URLs now return HTTP 404 and were not saved. no executable, installer, archive, DLL, or other binary was downloaded
