#!/usr/bin/env python3
"""Render angr decompiled JSONL -> documented markdown catalog.

Reads docs/functions/decompiled/<tag>.jsonl (one function per line with pseudo-C)
and emits grouped markdown with each function's pseudo-C plus an auto-summary.
Known/named functions get their documented name.
"""
import json, os, sys, re, textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
DEC = HERE + "/../docs/functions/decompiled"
TAG = sys.argv[1] if len(sys.argv) > 1 else "jdrv"
PER_FILE = 60

# addr -> (name, doc-ref) for functions already documented in docs 04-10
NAMED = {
 "0x10002c1f": ("DllEntryPoint", "05"), "0x10002cbe": ("EcInit", "05"),
 "0x10002d46": ("registerDialogs", "05"), "0x10002c87": ("postBotMessage", "05"),
 "0x10002d08": ("worker_stub", "05"),
 "0x10002041": ("installClientHooks_proxyServer", "08"),
 "0x100029a4": ("hook_fullLightDetour", "08"), "0x10002bd6": ("hook_fullLight_trampoline", "08"),
 "0x10002bdd": ("installLightHook", "08"), "0x10001a96": ("hook_captureRenderCtx", "08"),
 "0x10001ca8": ("hook_incomingPacketParser", "08"), "0x10002235": ("proxyClientThread", "09"),
 "0x10003146": ("dlgProc_AutoAim", "10"), "0x10006bce": ("dlgProc_HudCreatureList", "10"),
 "0x1001eb33": ("dlgProc_LinksNavNet", "10"), "0x1001e7c3": ("dlgProc_NavNet", "10"),
 "0x10007360": ("dlgProc_Hotkeys", "10"), "0x1001e3e5": ("dlgProc_Healer", "10"),
 "0x10007ec4": ("dlgProc_GraphicsTweaks", "10"), "0x1001e313": ("dlgProc_FriendsEnemies", "10"),
 "0x10007ca5": ("dlgProc_AutoAimCombo", "10"), "0x10007b55": ("dlgProc_HudOnScreenInfo", "10"),
 "0x1001e1d9": ("dlgProc_HotkeyActionPicker", "10"), "0x1001df05": ("dlgProc_CommandPicker", "10"),
 "0x1001d5fd": ("dlgProc_CommandParamPicker", "10"), "0x1001d2e0": ("dlgProc_CommandParamBuilder", "10"),
 "0x1001d151": ("dlgProc_CommandBuilder", "10"), "0x10006d3b": ("dlgProc_Shortkeys", "10"),
 "0x1001ef0c": ("dlgProc_LinksProxy", "10"), "0x1001a715": ("dlgProc_Targeting", "10"),
 "0x10019751": ("dlgProc_Cavebot", "10"), "0x1000802f": ("dlgProc_TargetingEditor", "10"),
 "0x100083b6": ("dlgProc_ScriptEditor", "10"), "0x100086b3": ("dlgProc_Skin", "10"),
 "0x1001b8be": ("dlgProc_SkinEditor", "10"),
}

def summarize(c, apis, strs):
    apis = apis or []
    hot = [a for a in apis if a in (
        "WriteProcessMemory","ReadProcessMemory","VirtualProtect","RegisterHotKey",
        "GetAsyncKeyState","connect","send","recv","socket","gethostbyname","bind","listen",
        "GetPrivateProfileStringA","WritePrivateProfileStringA","CreateWindowExA","CreateThread",
        "SendDlgItemMessageA","SendMessageA","CreateFileA","ReadFile","WriteFile","BitBlt",
        "DirectSoundCreate","mmioOpenA","MessageBoxA")]
    bits = []
    if hot: bits.append("calls " + ", ".join(sorted(set(hot))[:6]))
    if strs: bits.append("refs " + ", ".join('"%s"' % s for s in strs[:3]))
    return "; ".join(bits) or "(leaf/helper — see body)"

rows = [json.loads(l) for l in open(os.path.join(DEC, TAG + ".jsonl"))]
rows.sort(key=lambda r: int(r["addr"], 16))
withc = [r for r in rows if r.get("c")]
os.makedirs(os.path.join(DEC, TAG), exist_ok=True)

idx = []
for gi in range(0, len(withc), PER_FILE):
    grp = withc[gi:gi + PER_FILE]
    fn = "%s-%03d.md" % (TAG, gi // PER_FILE)
    lo, hi = grp[0]["addr"], grp[-1]["addr"]
    with open(os.path.join(DEC, TAG, fn), "w") as fh:
        fh.write(f"# elfbot.dll decompiled — {TAG} {lo}..{hi}\n\n")
        fh.write("angr pseudo-C for each function in this address range. Named functions "
                 "link to their subsystem doc. Auto-summary lists the APIs/strings each touches.\n\n")
        for r in grp:
            a = r["addr"]
            nm, ref = NAMED.get(a, (None, None))
            title = f"{nm} `{a}`" if nm else f"`sub_{a[2:]}` `{a}`"
            fh.write(f"## {title}\n\n")
            if nm:
                fh.write(f"Named — see [doc {ref}](../../{ref}-*.md). ")
            fh.write(f"_{r['size']} bytes. {summarize(r.get('c'), r.get('apis'), r.get('strs'))}_\n\n")
            fh.write("```c\n" + (r["c"] or "").strip() + "\n```\n\n")
    idx.append((fn, lo, hi, len(grp)))

with open(os.path.join(DEC, f"{TAG}-index.md"), "w") as fh:
    fh.write(f"# {TAG} decompiled — index\n\n")
    fh.write(f"{len(withc)} functions decompiled (of {len(rows)} in region; "
             f"{len(rows)-len(withc)} thunks/failed).\n\n")
    fh.write("| File | Range | Funcs |\n|---|---|---|\n")
    for fn, lo, hi, n in idx:
        fh.write(f"| [{fn}]({TAG}/{fn}) | {lo}..{hi} | {n} |\n")

print(f"rendered {len(withc)} funcs into {len(idx)} files under {DEC}/{TAG}/")
