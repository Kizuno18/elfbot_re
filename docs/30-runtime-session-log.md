# Runtime session log — live driving of the OTServ-patched client

Factual log of what was observed and done while driving the live client on the RE
VM (continuation of [docs/28](28-runtime-validation.md)). Addresses verbatim.

## Environment observed

- The Windows VM was **rebooted** mid-session (uptime reset, boot ~15:36). All
  prior injected processes/Frida sessions died.
- **`Tibia_ot.exe` auto-respawns.** It is an IP-patched genuine 8.6 client
  (image size `0x3fa000`; bytes at `0x549F60` = `ff ff 50 8d 8d a4 fe ff` and at
  `0x45ACD6` = `63 00 52 e8 72 89` — **identical to the genuine client**, so the
  elfbot hooks apply unchanged). A supervisor relaunches it on exit: observed PID
  churn `4720 → 4108 → 4340`.
- The VM is a **shared RE workspace**: `C:\Tools\mcp-uploads` also holds
  `magebotv55*.exe`, `XenoBot*.dll`, `ZeroBot-*.dll`, `rubinot_dx.exe`,
  `server.exe` (116 KB — a local server candidate), plus recent `ca.html` /
  `post.txt` / `resp.html` (15:44–15:47) — a parallel session is actively RE'ing
  several bots here.
- Networking: `Proxifier.exe` + `tailscaled.exe` run; the OTServ traffic is
  routed via Proxifier (the genuine client's default CipSoft login is dead, which
  is why plain `Tibia.exe` shows "Tibia Error", but `Tibia_ot.exe` reaches its
  patched host).
- `re-*` MCP infra (`re03-mcp.kizubot.com`, all servers behind one cloudflared
  tunnel) is **intermittently down** — repeated Cloudflare `502 origin_bad_gateway`
  (origin overloaded), recovering then dropping again.
- Binaries available for an independent offline test: genuine `Tibia.exe` +
  `Tibia.dat/spr/pic`, `elfbot.dll`, `elfload.dll`, `USkin.dll`, and the
  `elfsettings/ scripts/ minimaps/ playerinfo/` data dirs.

## UI geometry capture (done earlier this session)

`ui/elfbot-ui-geometry.json` — 16 panels, 369 controls, client-relative
`[class,id,x,y,w,h,text]`, captured live via `EnumChildWindows`+`GetWindowRect` on
injected elfbot. Full write-up in [docs/29](29-ui-layout-geometry.md).

## Runtime login path — driven to a live OTServ

Driving the `Tibia_ot.exe` login screen with `re-winctl` (focus → click account
field → type → Tab → type → Enter) and reading state back with Frida:

| Observation | How verified | Meaning |
|---|---|---|
| Keystrokes reach the login field | Frida `Memory.scanSync` for a unique typed string found it in the **account buffer at `0x2709460`** | the custom Tibia login widget receives input (it just isn't legible in a downscaled screenshot) |
| Login submits | after `1`/`1` + Enter the account buffer reset to `""` and an error dialog appeared | Enter drives the client's login/connect |
| Server answered | dialog: **"Sorry — Invalid account name or password"** | **server-side auth response**, not a socket/timeout error |
| In-game flag | `[0x64A9C0]` reads `2` at the login/char screen (`31` = in-world) | never reached in-world |

**Conclusions:** the VM reaches the OTServ (via Proxifier), the client's
connect/login path runs live, and `1/1` is simply not a valid account on the
server `Tibia_ot.exe` points at (no classic account-manager `1/1`). The in-game
packet path (parser hook `0x45ACD6` body, shadow tables) is now blocked **only on
a valid credential**, not on connectivity.

## Crash cause + fix (connect instrumentation)

A first `connect`/`WSAConnect` Frida interceptor read the `sockaddr` field-by-field
(`readU16` + per-byte). It **crashed the client at the moment of connect** — the
process died and its supervisor respawned it, which had masked the login result
(PID churn). Replacing it with a defensive reader fixed it:

```js
// SAFE: readByteArray returns null on bad memory instead of faulting
function safeSA(p){ try{ var b=p.readByteArray(16); if(!b) return 'null';
  var u=new Uint8Array(b); var port=(u[2]<<8)|u[3];
  var ip=u[4]+'.'+u[5]+'.'+u[6]+'.'+u[7];
  return 'fam'+(u[0]|(u[1]<<8))+' '+ip+':'+port; }catch(e){ return 'ex'; } }
```

Note: a **persistent safe connect-hook is still installed** on the running
`Tibia_ot` Frida session (passive — records connect events, does not alter
behavior).

## Coordination with the "elfbot better" session

A parallel session (`kizu-otc`) is rebuilding ElfBot from this RE. Delivered to it
by cross-session message:

1. The full **runtime contract** (3 blocks) it requested: sync/arbiter model
   (arbiter `cavebotTargetingStep 0x1003D99F`; flag triad `g_100f0d3b` /
   `g_100f0e42` / `g_100f0e20` + one-shot `g_100f0d3c=2`), the per-tick dispatch
   order (docs/25, 13), the single shared CiroScript VM + full `$var→handler`
   table (docs/14, 11), and loot↔walker (no corpse queue — re-scan; docs/23), with
   13 honest GAPs each pointing at the IDB xref that resolves it.
2. The UI geometry status (per-control `text` present; groupbox captions listed).
3. The runtime login finding + a request for valid server credentials.

## Re-point plan (ready to run when infra is stable)

A valid 8.6 test target became available: **`sv.bigot.com.br` → `179.124.178.79`
port `7171`** (proto 860). Resolved live from the VM via a Frida `getaddrinfo`
call (VM DNS reaches it). Credentials for it are held **in the session only — not
stored here (secret)**.

`Tibia_ot.exe` is currently patched at a raw **IP** (a scan of its readable memory
found no `sv.bigot` / `.com.br` hostname string), so it does not point at the test
server. Rather than locate and overwrite the client's login-server config, the
clean redirect is a **Frida `connect`/`WSAConnect` interceptor** that rewrites the
`sockaddr_in` whenever the client dials port 7171/7172:

```js
// port 7171/7172 -> 179.124.178.79:7171 (safe byte writes into the sockaddr)
if (port === 7171 || port === 7172) {
  sa.add(2).writeU8((7171>>8)&0xff); sa.add(3).writeU8(7171&0xff);
  sa.add(4).writeU8(179); sa.add(5).writeU8(124); sa.add(6).writeU8(178); sa.add(7).writeU8(79);
}
```

This works because the OTServ RSA is already patched into `Tibia_ot` (it reached
the previous OTServ), and `sv.bigot.com.br` uses the standard OTServ key. Steps:
install the redirect hook → type `bigleo` + password + Enter → server auth → enter
game (in-world, `[0x64A9C0]==31`) → capture the parser hook `0x45ACD6` firing +
the shadow tables populating.

**Current blocker (this session):** `re-winctl` (the UI typing/screenshot MCP) is
disconnected, and `Tibia_ot.exe` **respawns roughly every minute** (PID churn
`4720→4108→4340→…→2404→3920`) which drops the Frida session with the persistent
hook. A blind Frida-only login (drive keystrokes via `PostMessageA WM_CHAR`) is
possible in principle but not reliable while the process keeps respawning and no
screenshot is available to confirm dialog state. Resume when `re-winctl` returns
and the client is stable.

## Pending

- **Wizard popups** `TBOTDLGK/L/M/N/O/T/U` (command pickers / builders / targeting
  & script editors) — not in the geometry JSON; need a **live capture** with each
  dialog open. Doable offline on the independent genuine `Tibia.exe`.
- **In-game packet test** — the target + method above are ready; blocked only on
  a stable client + `re-winctl` for the login keystrokes.
