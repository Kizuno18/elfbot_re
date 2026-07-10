#!/usr/bin/env python3
"""Offline function inventory for elfbot.dll (no IDA needed).

Recovers function starts from call targets + export/entry, walks each function's
extent, and records the Win32 APIs it calls and the strings it references, then
classifies each function (thunk / crt-library / bot). Produces a JSON dump and a
markdown catalog. Fidelity is below Hex-Rays but it covers every function.
"""
import pefile, capstone, re, json, sys, os

PATH = sys.argv[1] if len(sys.argv) > 1 else "/home/kizudev/Downloads/Elfbot 8.60/elfbot.dll"
pe = pefile.PE(PATH)
IB = pe.OPTIONAL_HEADER.ImageBase

# --- section map ---
secs = []
for s in pe.sections:
    nm = s.Name.rstrip(b"\x00").decode("latin1", "replace")
    va = IB + s.VirtualAddress
    data = s.get_data()
    exec_flag = bool(s.Characteristics & 0x20000000)
    secs.append((nm, va, va + max(s.Misc_VirtualSize, len(data)), data, exec_flag))

def read(va, n):
    for nm, a, b, data, _ in secs:
        if a <= va < b:
            off = va - a
            return data[off:off + n]
    return b""

def in_exec(va):
    for nm, a, b, data, ex in secs:
        if a <= va < b:
            return ex
    return False

def sec_of(va):
    for nm, a, b, data, ex in secs:
        if a <= va < b:
            return nm
    return "?"

# --- imports: IAT addr -> name ---
iat = {}
pe.parse_data_directories()
if hasattr(pe, "DIRECTORY_ENTRY_IMPORT"):
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        dll = entry.dll.decode("latin1", "replace")
        for imp in entry.imports:
            if imp.address:
                nm = imp.name.decode("latin1", "replace") if imp.name else f"{dll}#{imp.ordinal}"
                iat[imp.address] = nm

# --- strings in the image (va -> text) for xref resolution ---
strings = {}
for nm, a, b, data, ex in secs:
    for m in re.finditer(rb"[\x20-\x7e]{4,}", data):
        strings[a + m.start()] = m.group().decode("latin1")

md = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)
md.detail = True

CODE = [(a, b) for nm, a, b, data, ex in secs if ex]

def is_code(va):
    return any(a <= va < b for a, b in CODE)

# --- pass 1: byte-scan for seeds + thunks (robust vs data-in-code) ---
import struct
seeds = set()
thunks = {}   # thunk_va -> api name (6-byte  ff25 [iat])
direct_api = {}  # va of a 'call [iat]'/'jmp [iat]' site -> name (not needed, resolved per-func)
if hasattr(pe, "DIRECTORY_ENTRY_EXPORT"):
    for e in pe.DIRECTORY_ENTRY_EXPORT.symbols:
        if e.address:
            seeds.add(IB + e.address)
seeds.add(IB + pe.OPTIONAL_HEADER.AddressOfEntryPoint)

for nm, a, b, data, ex in secs:
    if not ex:
        continue
    n = len(data)
    for i in range(n - 5):
        op = data[i]
        # E8 rel32 call -> target
        if op == 0xE8:
            rel = struct.unpack_from("<i", data, i + 1)[0]
            t = a + i + 5 + rel
            if is_code(t):
                seeds.add(t)
        # FF 25 [abs32] = jmp thunk ; FF 15 [abs32] = call import
        elif op == 0xFF and data[i + 1] in (0x25, 0x15):
            ptr = struct.unpack_from("<I", data, i + 2)[0]
            if ptr in iat:
                if data[i + 1] == 0x25:
                    thunks[a + i] = iat[ptr]
                    seeds.add(a + i)

seeds = sorted(s for s in seeds if is_code(s))
seed_set = set(seeds)

# --- pass 2: per-function extent + calls + string refs ---
def next_seed_after(va):
    import bisect
    i = bisect.bisect_right(seeds, va)
    return seeds[i] if i < len(seeds) else None

funcs = []
for i, start in enumerate(seeds):
    hard_limit = next_seed_after(start) or (start + 0x4000)
    # cap function scan span
    span = min(hard_limit - start, 0x6000)
    blob = read(start, span)
    if not blob:
        continue
    calls_api, calls_local, strefs = [], 0, []
    end = start
    max_local = start
    terminated = False
    for ins in md.disasm(bytes(blob), start):
        end = ins.address + ins.size
        mn = ins.mnemonic
        # track local branch targets to not stop early
        if mn.startswith("j") and ins.operands and ins.operands[0].type == capstone.x86.X86_OP_IMM:
            t = ins.operands[0].imm
            if start <= t < hard_limit:
                max_local = max(max_local, t)
        if mn == "call" and ins.operands:
            op = ins.operands[0]
            if op.type == capstone.x86.X86_OP_IMM:
                t = op.imm
                if t in thunks:
                    calls_api.append(thunks[t])
                elif t in seed_set:
                    calls_local += 1
            elif op.type == capstone.x86.X86_OP_MEM and op.mem.disp in iat:
                calls_api.append(iat[op.mem.disp])
        # string refs: any imm operand pointing into a known string
        for op in ins.operands:
            if op.type == capstone.x86.X86_OP_IMM and op.imm in strings:
                strefs.append(strings[op.imm][:60])
            elif op.type == capstone.x86.X86_OP_MEM and op.mem.disp in strings:
                strefs.append(strings[op.mem.disp][:60])
        if mn in ("ret", "retn") and ins.address >= max_local:
            terminated = True
            break
        if mn == "int3" and ins.address >= max_local:
            end = ins.address
            break
    size = end - start
    # classify
    api = calls_api
    joined = " ".join(strefs).lower()
    if start in thunks:
        cat = "thunk"; note = f"jmp -> {thunks[start]}"
    elif size <= 8 and calls_api and not calls_local:
        cat = "thunk"; note = f"-> {calls_api[0]}"
    elif any(k in joined for k in ("boost", "std::", "bad_alloc", "bad_cast", "vector<t>", "_cxx", "eh_")) or \
         any(s.startswith(".?A") for s in strefs):
        cat = "library"; note = "MSVC STL / Boost"
    else:
        cat = "bot"
        hot = [a for a in api if a in (
            "WriteProcessMemory","ReadProcessMemory","VirtualProtect","RegisterHotKey",
            "GetAsyncKeyState","connect","send","recv","socket","gethostbyname",
            "GetPrivateProfileStringA","WritePrivateProfileStringA","CreateWindowExA",
            "SendDlgItemMessageA","SetWindowTextA","CreateFileA","BitBlt","DirectSoundCreate")]
        note = ("uses " + ",".join(sorted(set(hot)))) if hot else ""
    funcs.append({
        "addr": f"0x{start:08x}", "size": size, "sec": sec_of(start),
        "cat": cat, "api": sorted(set(api)), "calls": calls_local,
        "strings": strefs[:6], "note": note,
    })

# refine classification: .jiru with no bot API and no bot strings -> library/support
BOT_STR = ("elfbot","cavebot","target","hotkey","navserv","navnet","tibia","aim",
           "loot","skin","script",".elf","waypoint","monster","rune","potion","hunt")
for f in funcs:
    if f["cat"] == "bot" and f["sec"] in (".jiru", ".cdtemn"):
        botsig = any(h in "".join(f["api"]) for h in ("ProcessMemory","socket","send","recv",
                     "RegisterHotKey","PrivateProfile","CreateWindowExA","BitBlt")) or \
                 any(any(k in s.lower() for k in BOT_STR) for s in f["strings"])
        if not botsig:
            f["cat"] = "support"

# --- output ---
OUT = os.path.dirname(os.path.abspath(__file__)) + "/../docs/functions"
os.makedirs(OUT, exist_ok=True)
json.dump(funcs, open(OUT + "/inventory.json", "w"), indent=0)

from collections import Counter
cats = Counter(f["cat"] for f in funcs)
bysec = Counter(f["sec"] for f in funcs)

def row(f):
    api = ",".join(f["api"][:8]) or "-"
    strs = " | ".join(s for s in f["strings"] if s.strip())[:80]
    extra = f" — {strs}" if strs else ""
    return f"| `{f['addr']}` | {f['size']} | {api}{(' …' if len(f['api'])>8 else '')} |{(' '+strs) if strs else ''}"

# core catalog: .jdrv (bot's own code)
core = [f for f in funcs if f["sec"] == ".jdrv"]
with open(OUT + "/catalog-core.md", "w") as fh:
    fh.write("# elfbot.dll function catalog — core (.jdrv, bot code)\n\n")
    fh.write("Offline recovery (capstone) of every function in the `.jdrv` section — "
             "ElfBot's own logic. Columns: address, size (bytes), Win32 APIs called "
             "(via IAT), notable string literals referenced. Named/deep functions are "
             "cross-referenced in docs 05–10. Import thunks excluded.\n\n")
    fh.write(f"{len(core)} functions.\n\n")
    fh.write("| Address | Size | APIs called | Strings |\n|---|---|---|---|\n")
    for f in sorted(core, key=lambda x: x["addr"]):
        if f["cat"] == "thunk":
            continue
        api = ",".join(f["api"][:8]) or "-"
        if len(f["api"]) > 8: api += " …"
        strs = " ".join(s for s in f["strings"] if s.strip())[:70].replace("|", "/")
        fh.write(f"| `{f['addr']}` | {f['size']} | {api} | {strs} |\n")

# support catalog: .jiru/.cdtemn (STL/Boost/CRT + dispatchers)
sup = [f for f in funcs if f["sec"] in (".jiru", ".cdtemn")]
with open(OUT + "/catalog-support.md", "w") as fh:
    fh.write("# elfbot.dll function catalog — support (.jiru/.cdtemn)\n\n")
    fh.write("The `.jiru`/`.cdtemn` sections hold MSVC STL + Boost template "
             "instantiations, the C runtime, and some feature dispatchers. Functions "
             "flagged `bot`/`support` below; those calling bot APIs or referencing bot "
             "strings are the real dispatchers worth a deep pass.\n\n")
    fh.write(f"{len(sup)} functions "
             f"({sum(1 for f in sup if f['cat']=='bot')} flagged bot-relevant).\n\n")
    fh.write("## Bot-relevant dispatchers in .jiru\n\n")
    fh.write("| Address | Size | APIs called | Strings |\n|---|---|---|---|\n")
    for f in sorted(sup, key=lambda x: x["addr"]):
        if f["cat"] != "bot":
            continue
        api = ",".join(f["api"][:8]) or "-"
        strs = " ".join(s for s in f["strings"] if s.strip())[:70].replace("|", "/")
        fh.write(f"| `{f['addr']}` | {f['size']} | {api} | {strs} |\n")

print(f"functions recovered: {len(funcs)}")
print("by category:", dict(cats))
print("by section:", dict(bysec))
print(f"catalog-core.md: {len([f for f in core if f['cat']!='thunk'])} funcs")
print(f"catalog-support.md bot-relevant: {sum(1 for f in sup if f['cat']=='bot')}")
apis = Counter()
for f in funcs:
    for a in f["api"]:
        apis[a] += 1
print("top APIs:", apis.most_common(12))
