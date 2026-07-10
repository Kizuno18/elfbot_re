# CiroScript — ElfBot 8.60 scripting language

ElfBot's cavebot and targeting behaviour is driven by **CiroScript** (the engine
is credited to `ciroscript.com/tibia`). Scripts come in two flavours:

- **Cavebot scripts** `*.elfc` — waypoint lists + per-waypoint action scripts.
- **Targeting scripts** `*.elft` — per-creature targeting rules and priorities.

Hotkeys (`hotkeys.ini`) and persistent hotkeys use the same command language.

This reference is compiled from the string table; the authoritative
command → handler dispatch table will be cross-checked against the parser in
`elfbot.dll` in a later pass (the interpreter lives in the hotkey/cavebot
subsystems).

## Compiled file format (`.elfc` / `.elft`)

Binary, not text. Observed structure:

- Header `A0 FE FF FF` (a length/marker) followed by a repeating magic
  `40 42 7E 42` between records.
- Strings are stored with high-bit control bytes **`0x40`** and **`0x80`**
  inserted as field/word delimiters (e.g. `Cir·Scri·pt` → `43 69 72 80 53 63 72
  69 40 70 74` decodes to "CiroScript"). `0x40`/`0x80` act as token/word
  separators inside the packed stream.
- `.elft` additionally carries fixed binary creature-config records (repeating
  `37 FF 37 FF … C0 97 00 FF` = per-creature colour/priority/behaviour fields).

The loader that decodes this format is in the cavebot/targeting subsystem
(`loadcavebot` / `loadtargeting`); byte-level layout is documented there once
the parser is reversed.

## Statement (action) commands

**Movement / walking**
`moven`, `moves`, `movee`, `movew`, `movene`, `movenw`, `movese`, `movesw`,
`moveto`, `walk`, `stand`, `standtime`, `turnn`/`turns`/`turne`/`turnw`,
`setpos`. Obstacle tools: `rope`, `shovel`, `machete`, `ladder`, `pick`.

**Item use**
`useitem`, `usegrounditem`, `usegroundxyz`, `useoncreature`,
`useongrounditem`, `useongroundxyz`, `useoninventoryitem`,
`useitemsonground`.

**Looting / inventory**
`pickupitems`, `pickupitemsamount`, `pickuppot`, `dropitems`, `dropitemsxyz`,
`dropitemsxyzamount`, `moveitems`, `moveitemsonto`, `moveitemonground`,
`reachgrounditem`, `lootitems`.

**Equipment slots**
`equiphelm`/`equiphead`, `equipammy` (amulet), `equipback`, `equipbelt`,
`equipboots`, `equipchest`, `equiplegs`, `equiplhand`, `equiprhand`,
`equipring`, `equipsring`.

**Chat / combat / misc**
`say`, `sayin`, `sayto`, `attack`, `skin`, `follow`, `flash`, `logout`,
`listen`, `alarm`, `pause`, `wait`, `label`, `gotolabel`, `return`.

**Auto hotkey family**
`autoaim`, `autoaimtarget`, `autocomboon`, `autobomb`, `autoheal`, `autouQ`.

## Setting commands

`setalarm`, `setammy`, `setattackmode`, `setautocombo`, `setcaption`
(Tibia window title), `setcavebot`, `setcolor`, `setdebug`,
`setfollowwaypoints`, `seticonactive`, `seticontext`, `setitemoutfit`,
`setopennextbp` (auto-open next backpack), `setoutfit`, `setoutfitcolor`,
`setpos`, `setrelation`, `settargeting`, `settradeoptions`,
**`SetFunctionAddresses`** — loads the Tibia client memory offsets the bot
reads/writes (the version-portability mechanism; see the memory-engine doc),
`loadcavebot`, `loadtargeting`, `turnon`/`turnoff`.

## Conditional commands

Prefix a statement with a condition; the statement runs only if it holds.

**Character stats**
`hphigher`/`hplower`, `hpmissinghigher`/`hpmissinglower`,
`caphigher`/`caplower`, `haste`/`hasted`/`hastetime`.

**Status flags** (`if…` / `ifnot…`)
`ifparalyzed`/`ifnotparalyzed`, `ifhasted`/`ifnothasted`,
`ifmanashielded`/`ifnotmanashielded`, `ifpoisoned`, `ifdrunk`,
`ifgm`/`ifnogm`, `ifplayeronscreen`/`ifnoplayeronscreen`,
`ifplayerattacking`, `ifprivatemessage`, `ifdefaultmessage`, `ifnot`.

**Counting**
`count`, `counthigher`/`countlower`, `countitems`, `countitemsvisible`,
`countolditems`, `getcount`, `enemycount`, `friendcount`, `exposedcount`.

**State predicates** (`is…` / `isnot…`)
- Vocation: `isknight`, `ismage`, `ispaladin`, `isdruid`.
- Targeting/combat: `isattacking`/`isnotattacking`, `isattackedname`,
  `istargeting`/`isnottargeting`, `islooting`, `isdistance`/`isnotdistance`,
  `isonscreen`/`isnotonscreen`, `islocation`/`isnotlocation`,
  `ismonster`, `isnpc`, `isplayer`, `isenemy`, `isfriend`, `isleader`,
  `isnavi`/`isonnavi`.
- Message classes: `ischannel`, `isbroadcast`, `isprivate`, `isdefault`,
  `isorangetext`, `isgame`, `isguild`, `ishelp`, `isinfo`, `isaction`,
  `isbotlook`, `ishaslookinfo`.

## Two script kinds vs. the same VM

Cavebot (`.elfc`) executes a linear waypoint list; each waypoint may be a move,
a stand, or an action label whose body is a CiroScript action script. Targeting
(`.elft`) evaluates, per visible creature, a rule list (`istargeting` /
`isattackedname` / vocation gates) to decide attack mode, spell/rune, and
priority. Both share the statement + conditional vocabulary above, interpreted
by the same engine.
