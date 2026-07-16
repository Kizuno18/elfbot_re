# USkin.dll & the statically-linked support section

Covers the two remaining "third-party / library" blocks: the off-the-shelf
`USkin.dll` skinning engine (41 exports, and exactly how ElfBot drives it) and the
5935-function `.jiru`/`.cdtemn` support section (already cataloged — summarised here
with provenance). Both are RE of `samples/USkin.dll` / `samples/elfbot.dll` /
`samples/elfload.dll` at imagebase `0x10000000`.

## USkin.dll — window-skinning library

An off-the-shelf Win32 skinning library (USER32 152 / GDI32 53 / KERNEL32 134
imports; also OLEAUT32, COMCTL32, SHLWAPI, WS2_32). Imagebase `0x10000000`, entry
`0x46C5E`. It applies `.msstyles` themes by subclassing top-level windows. **41
`USkin*` exports**, by role:

| Group | Exports |
|---|---|
| Lifecycle | `USkinInit`(1), `USkinExit`(2), `USkinLoadSkin`(3), `USkinLoadSkinFromBuffer`(10), `USkinLoadSkinFromResource`(11), `USkinOpenSkinData`(14), `USkinCloseSkinData`(15), `USkinApplyThread`(29) |
| Per-window skin | `USkinSetWindowSkin`(27), `USkinRemoveSkin`(5), `USkinRestoreSkin`(6), `USkinEnableWindowSkin`(28) |
| Skin-data getters (shared impl @ `0x3030`/`0x3060`, type-tagged) | `USkinGetInt`(17), `USkinGetBool`(16), `USkinGetDWORD`(18), `USkinGetDouble`(19), `USkinGetColor`(24), `USkinGetFont`(23), `USkinGetEnumValue`(22), `USkinGetString`(20), `USkinGetEnumString`(21) |
| Draw helpers | `USkinDrawFrameControl`(34), `USkinDrawSkinImageSection`(25), `USkinDrawText`(26) |
| System colours | `USkinGetSysColor`(30), `USkinGetSysColorBrush`(31), `USkinGetWinColor`(32), `USkinGetWinColorBrush`(33) |
| Menus | `USkinGetMenu`(9), `USkinSetMenuItemImage`(12), `USkinSetMenuItemImageEx`(13), `USkinUpdateMenuBar`(39) |
| Skin objects | `USkinGetWindowSkinObjectRect`(37), `USkinGetWindowSkinObjectText`(35), `USkinGetWindowSkinObjectVisible`(41), `USkinSetWindowSkinObjectText`(36), `USkinSetWindowSkinObjectVisible`(40) |
| Colour theme | `USkinApplyColorTheme`(7), `USkinApplyColorThemeByRGB`(8) |
| Misc | `USkinAboutSkin`(4), `USkinGetLastError`(38) |

### How ElfBot drives it — the elfload contract

`elfbot.dll` does **not** statically import `USkin.dll`; it is loaded and bound
dynamically by the injected loader **`elfload.dll`**, in its main routine
`sub_10001198` (the bot's UI-thread entry). The sequence:

1. `InitCommonControls()`, register window class `"TBOTDLG00"` (wndproc
   `sub_10001060`), `CreateDialogParamA(hInst, 0x7CF, …)` — the bot's main window.
2. Build `<module-dir>\USkin.dll` from `GetModuleFileNameA`, then
   `g_10003191 = LoadLibraryA(...)`.
3. `g_10003089 = GetProcAddress(USkinInit)` — stored for the init call.
4. `v8 = GetProcAddress(USkinExit)`, then **patch `USkinExit`'s prologue with a 5-byte
   `JMP rel32`**: `v2 = 0xE9`, `rel32 = target − v8 − 5`,
   `WriteProcessMemory(hProc, USkinExit, {E9 rel32}, 5)` — the library's teardown is
   detoured/neutered so unloading the bot doesn't let USkin unwind the skins itself.
5. Build `<module-dir>\elfbot.dll`, `LoadLibraryA`, `EcInit(g_10003085)` — the
   documented boot entry (docs/05/06).
6. Standard `GetMessage`/`TranslateMessage`/`DispatchMessage` pump.

So the entire elfbot↔USkin surface is: **load USkin, resolve `USkinInit` (invoked to
skin the dialogs) and `USkinExit` (immediately JMP-patched), then boot elfbot.** The
rich getter/draw/menu API is USkin's own internal machinery once initialised — the
bot never calls it directly.

### Skin tab (`TBOTDLGV`, `dlgProc_Skin` `0x100086B3`)

Pure UI over the skin files (`Skins\*.msstyles`):

- `WM_INITDIALOG`: read `GlobalSettings/LoadLastSkin` + `GlobalSettings/LastSkin` from
  `elfbot.ini`; `DlgDirListA(…, "Skins\\*.msstyles", 1001, DDL_READONLY)` fills listbox
  `1001`; prepend `"<No Skin>"`; select the entry matching `LastSkin`. If
  `LoadLastSkin == "1"` it sets `g_1004476A = 1` and applies the last skin at startup.
- `WM_COMMAND`: applying a selection routes the chosen `.msstyles` through USkin and
  writes `LastSkin` back to `elfbot.ini` (persisted alongside the docs/34 Extras
  `LoadLastSkin` toggle).

## `.jiru`/`.cdtemn` — the 5935-function support section

This is the statically-linked C/C++ runtime + third-party library block, already
enumerated function-by-function in
[docs/functions/jiru-catalog.md](functions/jiru-catalog.md) (every one of the 5935
carries a purpose derived from its decompiled C, full pseudo-C in
[decompiled/jiru-index.md](functions/decompiled/jiru-index.md)). Provenance:

- **304 crypto/compression dispatchers** — the subsystem in [docs/12](12-script-crypto-compression.md).
  Named primitives include the Blowfish key schedule `blowfishInitKey`
  (`0x102EB340`, 615 B: loads the P-array + four S-boxes from the digits-of-π
  constants, XORs the key in, re-encrypts P/S) and the zlib 1.2.3 inflate/deflate
  cluster. Per docs/12 this cluster is an **unused statically-linked library** — the
  live network cipher is the client's XTEA, not this code.
- **The remainder** — MSVC STL / Boost / C++ runtime glue (allocators, string/stream
  machinery, exception/RTTI plumbing, iterator helpers). These carry a structural
  purpose ("library/support: N loops; calls M helpers") rather than individual prose,
  because they are stock library code, not ElfBot logic. The catalog is the
  authoritative per-function record; there is no bot behaviour hidden among them
  beyond the crypto/compression dispatchers already pulled out.

Net: the "third-party" surface is fully accounted for — USkin's contract is the
minimal `Init` + neutered `Exit` above, and the support section's only bot-relevant
content (the crypto/compression subsystem) is documented in docs/12, with the rest
being identified, cataloged runtime/library glue.
