#!/usr/bin/env python3
import pefile, math, sys, os, hashlib

BASE = "/home/kizudev/Downloads/Elfbot 8.60"
TARGETS = ["elfbot.dll", "elfload.dll", "loader.exe", "navserv.exe", "USkin.dll", "unins000.exe"]

def entropy(data):
    if not data:
        return 0.0
    freq = [0]*256
    for b in data:
        freq[b]+=1
    e=0.0
    ln=len(data)
    for f in freq:
        if f:
            p=f/ln
            e-=p*math.log2(p)
    return e

def analyze(path):
    name=os.path.basename(path)
    print("="*70)
    print(f"FILE: {name}")
    data=open(path,"rb").read()
    print(f"  size: {len(data):,} bytes  sha256: {hashlib.sha256(data).hexdigest()[:16]}")
    try:
        pe=pefile.PE(path, fast_load=False)
    except Exception as e:
        print(f"  !! pefile failed: {e}")
        return
    m=pe.FILE_HEADER.Machine
    print(f"  machine: {hex(m)}  {'x86' if m==0x14c else 'x64' if m==0x8664 else m}")
    print(f"  characteristics: {hex(pe.FILE_HEADER.Characteristics)}  DLL={bool(pe.FILE_HEADER.Characteristics&0x2000)}")
    print(f"  timestamp: {pe.FILE_HEADER.TimeDateStamp:#x} ({__import__('datetime').datetime.utcfromtimestamp(pe.FILE_HEADER.TimeDateStamp)})")
    print(f"  entrypoint RVA: {pe.OPTIONAL_HEADER.AddressOfEntryPoint:#x}  imagebase: {pe.OPTIONAL_HEADER.ImageBase:#x}")
    print(f"  subsystem: {pe.OPTIONAL_HEADER.Subsystem}  linkerver: {pe.OPTIONAL_HEADER.MajorLinkerVersion}.{pe.OPTIONAL_HEADER.MinorLinkerVersion}")
    print("  -- sections --")
    for s in pe.sections:
        nm=s.Name.rstrip(b"\x00").decode("latin1","replace")
        d=s.get_data()
        print(f"    {nm:<10} vaddr={s.VirtualAddress:#010x} vsz={s.Misc_VirtualSize:#010x} rawsz={s.SizeOfRawData:#010x} ent={entropy(d):.2f} flags={s.Characteristics:#010x}")
    # imports
    print("  -- imports (by dll) --")
    try:
        pe.parse_data_directories(directories=[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_IMPORT']])
        if hasattr(pe,"DIRECTORY_ENTRY_IMPORT"):
            for entry in pe.DIRECTORY_ENTRY_IMPORT:
                dll=entry.dll.decode("latin1","replace")
                imps=[imp.name.decode("latin1","replace") if imp.name else f"ord{imp.ordinal}" for imp in entry.imports]
                print(f"    {dll} ({len(imps)}): {', '.join(imps[:40])}{' ...' if len(imps)>40 else ''}")
        else:
            print("    (none / packed)")
    except Exception as e:
        print(f"    import parse err: {e}")
    # exports
    try:
        pe.parse_data_directories(directories=[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_EXPORT']])
        if hasattr(pe,"DIRECTORY_ENTRY_EXPORT"):
            exps=[e.name.decode("latin1","replace") if e.name else f"ord{e.ordinal}" for e in pe.DIRECTORY_ENTRY_EXPORT.symbols]
            print(f"  -- exports ({len(exps)}): {', '.join(exps[:60])}{' ...' if len(exps)>60 else ''}")
    except Exception as e:
        pass
    # imphash / rich header hint
    try:
        print(f"  imphash: {pe.get_imphash()}")
    except: pass
    # resources presence
    dd=pe.OPTIONAL_HEADER.DATA_DIRECTORY
    for d in dd:
        if d.name=="IMAGE_DIRECTORY_ENTRY_RESOURCE" and d.Size:
            print(f"  resources: size={d.Size:#x}")
        if d.name=="IMAGE_DIRECTORY_ENTRY_TLS" and d.Size:
            print(f"  TLS: present (size={d.Size:#x})")
    pe.close()

for t in TARGETS:
    p=os.path.join(BASE,t)
    if os.path.exists(p):
        analyze(p)
    else:
        print(f"MISSING: {t}")
