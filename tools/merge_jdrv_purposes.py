#!/usr/bin/env python3
"""Deepen .jdrv purposes WITHOUT touching names.

The .jdrv catalog already names every function (elfbot's canonical set) and gives
each a purpose, but ~457 of them (the cmd_* CiroScript handlers, HUD vars, dialog
procs) carry only a thin "CiroScript command 'X' handler (see doc 11)" line. The
workflow produced deep, mechanism-level purposes for exactly those. This merges
the DEEP PURPOSES onto the EXISTING NAMES (agent-proposed names are discarded),
regenerates jdrv-catalog.md, and updates jdrv-purposes.json.
"""
import json, glob, re, os

REPO = "/home/kizudev/Documents/Repos/elfbot_re"
RDIR = "/tmp/claude-1000/-home-kizudev-Documents-Repos-magebot-re/9b8c3669-5386-483d-bbab-ee0854da4916/scratchpad/elfbot_results"
FN = f"{REPO}/docs/functions"

def norm(a):
    a = str(a).lower().strip()
    return a if a.startswith("0x") else "0x" + a

# parse the authoritative catalog: addr -> (name, size, purpose), preserving order
row_re = re.compile(r"^\|\s*`(0x[0-9a-fA-F]+)`\s*\|\s*`([^`]+)`\s*\|\s*(\d+)\s*\|\s*(.*?)\s*\|\s*$")
rows = []  # (addr, name, size, purpose)
header = []
for line in open(f"{FN}/jdrv-catalog.md"):
    m = row_re.match(line)
    if m:
        rows.append([m.group(1).lower(), m.group(2), m.group(3), m.group(4)])
    elif not rows:
        header.append(line.rstrip("\n"))

# agent deep purposes (ignore agent names)
deep = {}
for rf in glob.glob(f"{RDIR}/chunk_*.json"):
    try:
        for e in json.load(open(rf)):
            deep[norm(e["addr"])] = e.get("purpose", "").strip()
    except Exception as ex:
        print("skip", rf, ex)

cmd_re = re.compile(r"CiroScript command '([^']+)' handler")
updated = 0
for r in rows:
    addr, name, size, purpose = r
    dp = deep.get(addr)
    if not dp:
        continue
    # preserve the doc-11 pointer for CiroScript handlers
    m = cmd_re.search(purpose)
    if m and "doc 11" not in dp:
        dp = f"{dp} (CiroScript '{m.group(1)}', doc 11)"
    r[3] = dp.replace("|", "\\|").replace("\n", " ")
    updated += 1

# rewrite catalog
out = list(header)
if not out:
    out = ["# elfbot.dll `.jdrv` — complete function catalog", "",
           "All 1190 functions of the bot's own code section, each with name + purpose.", "",
           "| Address | Name | Size | Purpose |", "|---|---|---|---|"]
for addr, name, size, purpose in rows:
    out.append(f"| `{addr}` | `{name}` | {size} | {purpose} |")
open(f"{FN}/jdrv-catalog.md", "w").write("\n".join(out) + "\n")

# update purposes sidecar (name + purpose), keyed by addr
pur = json.load(open(f"{FN}/jdrv-purposes.json"))
pur = {norm(k): v for k, v in pur.items()}
by_addr = {r[0]: r for r in rows}
for addr, dp in deep.items():
    if addr in by_addr:
        pur[addr] = {"name": by_addr[addr][1], "purpose": by_addr[addr][3]}
json.dump(pur, open(f"{FN}/jdrv-purposes.json", "w"), indent=0)

print(f"deepened {updated} .jdrv purposes (names untouched) | catalog rows {len(rows)} | "
      f"purposes.json now {len(pur)}")
