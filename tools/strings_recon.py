#!/usr/bin/env python3
import re, os, sys

BASE = "/home/kizudev/Downloads/Elfbot 8.60"

def get_strings(path, minlen=5):
    data=open(path,"rb").read()
    # ascii
    asc=re.findall(rb"[\x20-\x7e]{%d,}"%minlen, data)
    out=[s.decode("latin1") for s in asc]
    # utf-16le
    wide=re.findall(rb"(?:[\x20-\x7e]\x00){%d,}"%minlen, data)
    out+= [w.decode("utf-16le","replace") for w in wide]
    return out, len(data)

PACKERS = ["Armadillo","SoftwareToolworks","Silicon Realms","ASProtect","Themida","VMProtect",
           "PECompact","UPX","Obsidium","ProtectionSDK","Nanomites",".Geddon","CopyMem"]

def cat(path):
    name=os.path.basename(path)
    ss, sz = get_strings(path)
    print("="*70); print(f"{name}  ({sz:,} bytes, {len(ss)} strings)")
    # packer sig
    hits=set()
    blob="\n".join(ss)
    for p in PACKERS:
        if p.lower() in blob.lower():
            hits.add(p)
    if hits: print(f"  PACKER SIG: {sorted(hits)}")
    # urls
    urls=sorted(set(s for s in ss if re.search(r"https?://|www\.|\.com|\.net|\.org",s) and len(s)<120))
    if urls:
        print(f"  URLs/domains ({len(urls)}):")
        for u in urls[:30]: print(f"    {u}")
    # ini/config keys and .exe/.dll/.ini file refs
    files=sorted(set(s for s in ss if re.search(r"\.(ini|dll|exe|dat|elfc|elft|lua|txt|wav|bmp|ico)$",s.strip(),re.I) and len(s)<80))
    if files:
        print(f"  file refs ({len(files)}):")
        for f in files[:40]: print(f"    {f}")

for t in ["elfbot.dll","navserv.exe","loader.exe","elfload.dll"]:
    cat(os.path.join(BASE,t))
