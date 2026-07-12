# Icons tab — Command Icons (TBOTDLGW) deep RE

The **Icons** tab (`TBOTDLGW`, "Command Icons", 573×296) defines user-configurable
on-screen HUD buttons. Each icon renders over the game panel, shows an active or
inactive visual, and **runs a CiroScript command when clicked**. This documents the
record layout, the render path, the click path, and the three script commands.

## Storage — the icon record table

Icons live in the same `4308`-byte-stride (`0x10D4`) record array as the targeting
definitions: **`g_1014f420` … `g_101d5e20`**, indexed by ordinal, terminated by a
record whose name byte is `0` (sentinel). Per-record fields used by the Icons
feature:

| Offset | Field |
|---|---|
| `+0` | name (string; also the end-of-table sentinel) — the lookup key |
| `+32` (`0x20`) | **command text** — the CiroScript run when the icon is clicked (set by `seticontext`) |
| `+0x40` (64) | size flag: `0` → 32 px, non-zero → 64 px |
| `+0x44` (68) | **enabled** — record is drawn only if non-zero |
| `+72` | hide flag — drawn only if `0` (or the global override `g_1005f88d` is set) |
| `+4076` (`0xFEC`) | **Inactive-state** visual block (100 bytes) |
| `+4176` (`0x1050`) | **Active-state** visual block (100 bytes) |

Each 100-byte state block (`idx = record + 4076|4176`):

| Offset in block | Field |
|---|---|
| `+0` | icon id (sprite) |
| `+8` | background id |
| `+24` | color |
| `+32` | text |
| `+48` | alignX mode (0 none / 1 rel-prev / 2 map-left / 3 map-right / 4,5 column groups) |
| `+52` | base X offset |
| `+56` | alignY mode (same scheme, vertical) |
| `+60` | base Y offset |
| `+64` | text-overlay + per-state colors (drawn via `sub_1003b127`) |

## Per-icon parallel state — four 128-byte arrays

Indexed by the icon's ordinal, four contiguous 128-slot byte arrays:

| Addr | Meaning | Written by |
|---|---|---|
| `g_1008a80b` | **pressed** | `hitTestHudButtons` (mouse down on the icon) |
| `g_1008a88b` | **clicked** | `hitTestHudButtons` (mouse up / release = fire) |
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
4. draws the background+icon (`sub_1003e5f2`, block `+8` / color `+24`) and the text
   overlay (`sub_1003b127`, block `+64`), using the *selected* color triple
   `g_1008b8f4/8/c` (highlight variant `+4` when the record is the hovered one
   `g_10291cf2`, else `+96`).

## Click — `hookWndProcMouseKeyboard` @ `0x10029d4e` → `hitTestHudButtons` @ `0x1002a092`

Mouse/keyboard reach the client through the replacement window proc installed at
`0x5b8428` (`hookWndProcMouseKeyboard`), which also does HUD drag and
right-click-walk. For a mouse message it calls **`hitTestHudButtons`**: that walks
the same `g_1014f420` widget table, recomputes each icon's anchored on-screen rect
(same anchoring math as the renderer, against the map rect), finds the icon under
the cursor, and sets the **pressed** (`g_1008a80b[ord]`) / **clicked**
(`g_1008a88b[ord]`) flags. The bot tick then consumes the clicked flag and runs
that icon's `+32` **command text** through the CiroScript VM (same interpreter as
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
  name and `lstrcpy`s `<text>` into the record `+32` (its **command text**), i.e.
  reprograms what the icon does when clicked.
- **`exoricon`** (`cmd_exoricon 0x10035238`) — **NOT** an icon-HUD command despite
  the name; it is the "**exori con**" area attack: requires level ≥ 35
  (`[0x63fe78]`), resolves the target `g_1008b89b`, optionally turns to face it,
  sets `g_100f9328=1` and casts `"exori con"` via `sub_10039413`. The name is a
  spell ("exori con"), not "exor-icon".

## Relation to other tabs

The icon records share the `g_1014f420` array (stride `0x10D4`) with the
**Targeting** creature definitions — the same editor/serializer machinery backs
both, and both are rendered/hit-tested through the client draw + wndproc hooks. The
icon command text runs on the same single CiroScript VM as every other module
(see [docs/14](14-ciroscript-runtime.md), [docs/31](31-gap-resolutions.md)).
