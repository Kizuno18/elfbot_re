# Icons tab — Command Icons (TBOTDLGW) deep RE

The **Icons** tab (`TBOTDLGW`, "Command Icons", 573×296) defines user-configurable
on-screen HUD buttons. Each icon renders over the game panel, shows an active or
inactive visual, and **runs a CiroScript command when clicked**. This documents the
record layout, the render path, the click path, and the three script commands.

## Storage — the icon record table

Icons live in a `4308`-byte-stride (`0x10D4`) record array:
**`g_1014f420` … `g_101d5e20`**, indexed by ordinal, terminated by a
record whose name byte is `0` (sentinel). Per-record fields used by the Icons
feature:

| Offset | Field |
|---|---|
| `+0` | name (string; also the end-of-table sentinel) — the lookup key |
| `+32` (`0x20`) | extra sprite-overlay text, a 32-byte string written by `seticontext` |
| `+0x40` (64) | size flag: `0` → 32 px, non-zero → 64 px |
| `+0x44` (68) | **enabled** — record is drawn only if non-zero |
| `+72` | DrawAsBackground flag — foreground rendering only if `0` (or `g_1005f88d` is set) |
| `+76` (`0x4C`) | left-click CiroScript command, 2000-byte string |
| `+2076` (`0x81C`) | right-click CiroScript command, 2000-byte string |
| `+4076` (`0xFEC`) | **Inactive-state** visual block (100 bytes) |
| `+4176` (`0x1050`) | **Active-state** visual block (100 bytes) |
| `+4276` (`0x10B4`) | 32 opaque trailing bytes; preserve when moving or editing a record |

Each 100-byte state block (`idx = record + 4076|4176`):

| Offset in block | Field |
|---|---|
| `+0` | icon type enum, 32-bit |
| `+4` | hover text COLORREF, 32-bit |
| `+8` | four signed 32-bit icon IDs |
| `+24` | background type enum, 32-bit |
| `+28` | opaque 32-bit value; preserve |
| `+32` | four signed 32-bit background IDs |
| `+48` | alignX mode (0 none / 1 rel-prev / 2 map-left / 3 map-right / 4,5 column groups) |
| `+52` | base X offset |
| `+56` | alignY mode (same scheme, vertical) |
| `+60` | base Y offset |
| `+64` | 32-byte text string (drawn via `sub_1003b127`) |
| `+96` | normal text COLORREF, 32-bit |

All integers are little endian. Strings are ANSI bytes with a NUL terminator:
31 bytes maximum for name, extra text, and state text; 1999 for each command.
COLORREF stores red, green, and blue in the low three bytes (`0xHHBBGGRR`);
the high byte is ignored by rendering but retained by the native memory dump.

### General-profile persistence

`saveConfigFile 0x100200ff` writes 903650 bytes beginning at `0x100f9494`;
`loadConfigFile 0x100201d3` copies at most 903648. The icon table therefore
starts at file offset `0x55F8C` (352140), occupies 128 records / `0x86A00`
bytes, and ends at `0xDC98C` (903564), entirely inside the loadable image.
There is no separate binary Icons file or stored count. The `[Icons]` editor
script is a separate text interchange representation of these records.

Five byte flags follow two unrelated HUD bytes:

| File offset | Global | Control | Meaning |
|---|---|---|---|
| `0xDC98E` | `g_101d5e22` | 1023 | Reserve 32 pixels above map |
| `0xDC98F` | `g_101d5e23` | 1068 | Reserve 64 pixels above map |
| `0xDC990` | `g_101d5e24` | 1037 | Reserve 32 pixels below map |
| `0xDC991` | `g_101d5e25` | 1071 | Reserve 64 pixels below map |
| `0xDC992` | `g_101d5e26` | 1074 | Enable Icons |

The editor updates fields directly on `WM_COMMAND`; general Save dumps the
resulting memory. Load refreshes the list through `populateIconList` and
restores the five flags through `sub_1001f5bd`. Record swaps copy all 4308
bytes, and Copy Active copies all 100 state bytes, including opaque bytes
and string slack. See `jdrv-003.md` functions `0x100193a1`, `0x1001b8be`,
`0x1001f5bd`, `0x100200ff`, and `0x100201d3` for the cross-checked layout.

## Per-icon parallel state — four 128-byte arrays

Indexed by the icon's ordinal, four contiguous 128-slot byte arrays:

| Addr | Meaning | Written by |
|---|---|---|
| `g_1008a80b` | pending **left click** | `hitTestHudButtons` (matching mouse release) |
| `g_1008a88b` | pending **right click** | `hitTestHudButtons` (matching mouse release) |
| `g_1008a90b` | **active-state** | `cmd_seticonactive` |
| `g_1008a98b` | active-state (2nd) | `cmd_seticonactive` |

An icon draws its **Active** block when `g_1008a90b[ord] || g_1008a98b[ord]` is
non-zero, else the **Inactive** block.

## Render — `drawCustomHudElements` @ `0x1003e7aa`

Called every frame from the client draw hook (the `0x4F30C0` JMP detour /
`callHudDrawCallback 0x10026545`). It walks `g_1014f420` and for each **enabled**
record (`+0x44`):
1. picks size `32`/`64` from `+0x40`;
2. selects the Active (`+4176`) or Inactive (`+4076`) block via the
   `g_1008a90b`/`g_1008a98b` arrays;
3. resolves the anchored X/Y from the block's align modes (`+48`/`+56`) and offsets
   (`+52`/`+60`) against the map-panel rect `g_10080b84` (fields `+0x14`/`+0x18`
   = panel left/top, `+0x1c`/`+0x20` = width/height) and running column cursors;
4. draws the background (`+32` IDs / `+24` type) and icon (`+8` IDs / `+0` type)
   through `sub_1003e5f2`, and the text
   overlay (`sub_1003b127`, block `+64`), using the *selected* color triple
   `g_1008b8f4/8/c` (highlight variant `+4` when the record is the hovered one
   `g_10291cf2`, else `+96`).

## Click — `hookWndProcMouseKeyboard` @ `0x10029d4e` → `hitTestHudButtons` @ `0x1002a092`

Mouse/keyboard reach the client through the replacement window proc installed at
`0x5b8428` (`hookWndProcMouseKeyboard`), which also does HUD drag and
right-click-walk. For a mouse message it calls **`hitTestHudButtons`**: that walks
the same `g_1014f420` widget table, recomputes each icon's anchored on-screen rect
(same anchoring math as the renderer, against the map rect), finds the icon under
the cursor, and remembers the mouse-down record in `g_10291cee` (left) or
`g_10291cea` (right). Matching release sets the pending left/right click byte
at `g_1008a80b[ord]` / `g_1008a88b[ord]`. The bot tick consumes that flag and runs
the corresponding `+76` / `+2076` command through the CiroScript VM (same interpreter as
hotkeys/cavebot/targeting — self-char as subject).

So the full loop: **define icon (editor) → render (drawCustomHudElements) → click
(hitTestHudButtons) → run its command text (CiroScript)**, with `seticonactive`
letting a script flip the icon's active/inactive visual programmatically.

## Config UI — `dlgProc_SkinEditor` @ `0x1001b8be`

The Icons list editor (HWND `g_10072f90`): `populateIconList 0x1001b815` fills the
listbox (`0x404`) from the table plus a trailing `'<New Icon>'`;
`populateIconComboBoxes 0x1001b6df` fills the size/type/alignX/alignY combos from
the option tables `g_100423c8/g_10042394/g_10042322/g_1004233a`. `WM_COMMAND` (273)
reads the combo/edit selections into `g_101d5e22…26` and handles rename (1029),
delete (1038, array-shift `sub_1002ae6f`), clear (1075), move up/down (1026) over
the `0x10D4`-byte records. `serializeIconsScript 0x100193a1` dumps the whole
`[Icons]` config (name/enabled/size/commands + per-icon Active/Inactive icon+bkg
ids, alignment, text) into edit control 1002 for the shared script editor
(`dlgProc_ScriptEditor` mode 4 = Icons).

## The three icon CiroScript commands

- **`seticonactive <name> <value>`** (`cmd_seticonactive 0x10032d31`) — finds the
  icon by name, writes `value/100` (capped at `250`) into `g_1008a90b[ord]` and
  `g_1008a98b[ord]`. Non-zero → the icon shows its **Active** visual. (The catalog's
  "mana value" wording is incidental; it is a generic active-level.)
- **`seticontext <name> <text>`** (`cmd_seticontext 0x10032ccc`) — finds the icon by
  name and `lstrcpy`s `<text>` into the record `+32`, the extra sprite-overlay
  text drawn by `sub_1003e5f2`. It does not change either click command.
- **`exoricon`** (`cmd_exoricon 0x10035238`) — **NOT** an icon-HUD command despite
  the name; it is the "**exori con**" area attack: requires level ≥ 35
  (`[0x63fe78]`), resolves the target `g_1008b89b`, optionally turns to face it,
  sets `g_100f9328=1` and casts `"exori con"` via `sub_10039413`. The name is a
  spell ("exori con"), not "exor-icon".

## Relation to other tabs

The icon records occupy `g_1014f420` with stride `0x10D4`; the separate
**Targeting** creature definitions begin at `g_101d5e78` with stride `0x140`.
Icons are rendered/hit-tested through the client draw + wndproc hooks. The
icon command text runs on the same single CiroScript VM as every other module
(see [docs/14](14-ciroscript-runtime.md), [docs/31](31-gap-resolutions.md)).
