#!/usr/bin/env python3
"""Extract per-engine Hex-Rays decompilation closures from the elfbot IDA session.

Seeds are the tick-level entry points found in botMainTickLoop. For each engine,
BFS the internal callee closure (bounded, staying in .jdrv) and pull the real
Hex-Rays pseudocode (now that .jdrv is fully named), one text file per engine.

Usage: extract_engine.py <session_id> <out_dir>
"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import re_mcp as m

DB = sys.argv[1] if len(sys.argv) > 1 else "elfbot"
OUT = sys.argv[2] if len(sys.argv) > 2 else "engines"
JDRV_LO, JDRV_HI = 0x10001000, 0x10041000   # .jdrv (bot code)
DEPTH, CAP = 2, 26

ENGINES = {
    "master_tick":       ["0x100227bd", "0x10021f6c"],                             # botMainTickLoop, botUiWorkerLoop
    "ciroscript_engine": ["0x1002bc68", "0x100300ce", "0x1002c1b6"],               # runScriptTickProfiler, parseExpressionOrRange, registerCommand
    "healer":            ["0x1002492d", "0x100235e8", "0x10024cae", "0x1003a60a", "0x10023797"],  # healerManaSpellTick, runAttackHealerLogic, healByNameCommand, castRuneOrSpellOnTarget, setCastCooldown
    "targeting":         ["0x10023893", "0x10023a8f", "0x10023a45", "0x1001686c", "0x10027176", "0x1003bb22"],  # targetingAttackScanTick, scanBattleListStatusTick, resolveActiveCreaturePtr, parseTargetingRecord, handleAttackTargetOnTile, dequeueMarkedCreature
    "cavebot_walker":    ["0x10012edb", "0x1001242d", "0x10013e4d", "0x1001451b", "0x100143ba", "0x1000e6b9", "0x1000d2da"],  # walker driver, decideRetreatStep, stepTowardTarget, chooseFleeStep, stampCreatureAvoidanceWeights, findBestWaypointPath, traceMapPathBFS
    "cavebot_waypoints": ["0x10015b79", "0x10016438", "0x100167eb", "0x100160d6"], # loadCavebotFile, parseWaypointsSection, loadScriptFile, refreshCavebotDialog
    "navnet_codec":      ["0x1003ffdf", "0x10001960", "0x10001000", "0x10002041"], # sendNavPositionUpdate, buildFullGameStateSnapshot, startNavServerThread, installClientHooks_proxyServer
    "client_hooks":      ["0x10001ca8", "0x100029a4", "0x10002bdd"],               # hook_incomingPacketParser, hook_fullLightDetour, installLightHook
    "stats_exp":         ["0x10023e42", "0x10024fae", "0x1002997f"],               # pushExpSampleWindow, snapshotPlayerStats, syncClientLightState
}


def content(res):
    try:
        return res["result"]["content"][0]["text"]
    except Exception:
        return ""


def decompile(addr):
    txt = content(m.call("ida", "tools/call", {"name": "decompile", "arguments": {"database": DB, "addr": addr}}))
    try:
        d = json.loads(txt)
    except json.JSONDecodeError:
        return None, None
    if isinstance(d, dict):
        return d.get("code") or d.get("pseudocode"), d.get("name")
    return None, None


def callees(addr):
    txt = content(m.call("ida", "tools/call", {"name": "callees", "arguments": {"database": DB, "addrs": [addr]}}))
    try:
        d = json.loads(txt)
    except json.JSONDecodeError:
        return []
    out = []
    for e in d:
        for c in e.get("callees", []):
            if c.get("type") == "internal":
                a = int(c["addr"], 16)
                if JDRV_LO <= a < JDRV_HI:
                    out.append(c["addr"])
    return out


def closure(seeds):
    seen, order, frontier = set(), [], [(s, 0) for s in seeds]
    while frontier and len(order) < CAP:
        addr, depth = frontier.pop(0)
        key = int(addr, 16)
        if key in seen:
            continue
        seen.add(key)
        order.append(addr)
        if depth < DEPTH:
            for c in callees(addr):
                if int(c, 16) not in seen:
                    frontier.append((c, depth + 1))
    return order


def main():
    os.makedirs(OUT, exist_ok=True)
    index = {}
    for name, seeds in ENGINES.items():
        funcs = closure(seeds)
        index[name] = funcs
        path = os.path.join(OUT, f"{name}.txt")
        with open(path, "w") as fh:
            fh.write(f"# engine: {name}\n# seeds: {', '.join(seeds)}\n"
                     f"# functions ({len(funcs)}): {', '.join(funcs)}\n\n")
            for a in funcs:
                code, fname = decompile(a)
                fh.write("=" * 72 + f"\nFUNC {a}  {fname or ''}\n" + "=" * 72 + "\n")
                fh.write((code or "<decompile failed>") + "\n\n")
        print(f"{name}: {len(funcs)} funcs -> {path}", flush=True)
    json.dump(index, open(os.path.join(OUT, "index.json"), "w"), indent=1)
    print("done", flush=True)


if __name__ == "__main__":
    main()
