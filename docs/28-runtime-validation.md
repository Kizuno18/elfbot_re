# Runtime validation (live injection into genuine Tibia 8.6)

The static RE (docs 01–27) was confirmed **live** by injecting `elfbot.dll` into a
genuine CipSoft Tibia 8.6 client and instrumenting it with Frida on the RE VM.
Everything the static analysis predicted was observed in the running process.

## Setup

- Genuine `Tibia.exe` 8.6 (CipSoft, sha256 `bcda2db9…`, imagebase `0x400000`, no
  ASLR) spawned suspended via Frida on the headless Windows VM.
- The VM has no interactive desktop (sits at LogonUI), so the GUI debuggers
  (x32dbg/x64dbg) and the client's OpenGL window don't come up — but **Frida
  works headlessly** and Tibia's process image initializes fine (3 threads, stays
  at the login screen; the in-game flag `[0x64A9C0]` reads `0`).
- `elfbot.dll` was `LoadLibrary`-injected directly (bypassing `loader.exe`'s
  `FindWindow "TibiaClient"`, which needs a window).

## 1. Genuine-client offsets are real (confirms docs/08)

Reading Tibia's mapped image at the hard-coded addresses the bot patches shows
real client code/globals:

| Address | Bytes read | Meaning |
|---|---|---|
| `0x549F60` | `ff ff 50 8d 8d a4 fe ff ff e8 c2 5e 00 00 …` | the client XTEA routine the proxy's `decryptPacketBlocks` calls |
| `0x45ACD6` | `63 00 52 e8 72 89 04 00` | incoming-packet dispatch (a `call` site) |
| `0x4F30C0` | `ff 50 e8 ba cf 06 00 89` | draw/context path |
| `0x64A9C0` | `0` | in-game flag (0 = not in world) |

## 2. Armadillo: no runtime unpacking (confirms docs/03)

After `LoadLibraryW("elfbot.dll")` the module mapped at its imagebase `0x10000000`
(size `0x47D000`), export **`EcInit` @ `0x10002CBE`**. Reading its code live:

```
0x10002CBE:  55 8b ec 89 0d 8d 47 04 10 ff 75 08 8f 05 1a f6
             push ebp; mov ebp,esp; mov [0x1004478D], ecx; ...
```

That is byte-for-byte the static decompile (`dword_1004478D = this`). The
high-entropy `.aqfu` blob at `base+0x3CB000` read `1d 34 0e 5a 1d 2f 4d 1f …` —
**identical to the on-disk encrypted bytes, i.e. never decrypted in memory**. So
the code is plaintext on disk *and* in RAM, `.aqfu` is an inert blob, and there
is **zero runtime unpacking**. The static disassembly is the code that runs.

## 3. DllMain spawns the worker (confirms docs/05)

`LoadLibrary` fired `DllEntryPoint`, which was caught spawning a thread:

```
[CreateThread] start=0x10002D08
```

exactly matching `DllEntryPoint` → `CreateThread(sub_10002D08)` (the worker stub).

## 4. The client hook engine, live (confirms docs/08)

Invoking `installClientHooks_proxyServer 0x10002041` as a thread (with `hProcess`
`[0x1005DB68]` set to `GetCurrentProcess()` = `0xFFFFFFFF` and the once-guard
`[0x1005A290]` cleared) produced exactly the documented patch sequence, captured
by hooking `VirtualProtect` / `WriteProcessMemory`:

```
[VP]  addr=0x5AB000 sz=1540(0x604) newprot=0x4 (PAGE_READWRITE)
[WPM] dst=0x5AB5D4 sz=4 bytes=96 1a 00 10   → &hook_captureRenderCtx (0x10001A96)
[WPM] dst=0x4F30C0 sz=1 bytes=e9             → JMP detour
[WPM] dst=0x45ACD6 sz=4 bytes=ce 6f ba 0f   → rel to hook_incomingPacketParser (0x10001CA8)
```

Reading the sites back after the patch confirmed they **landed**:

| Site | After patch | Redirects to |
|---|---|---|
| `0x5AB5D4` | `96 1a 00 10` = `0x10001A96` | `hook_captureRenderCtx` |
| `0x45ACD6` | `ce 6f ba 0f` → `0x10001CA8` | `hook_incomingPacketParser` |
| `0x4F30C0` | `e9 …` | JMP detour |

This is the docs/08 hook table, address-for-address and byte-for-byte, running in
a live client. (First attempt no-op'd because `hProcess` was still null — the bot
relies on that global being set during the normal `EcInit`/loader init, and the
installer self-guards against re-running; both were reproduced to make the writes
land.)

## What was not exercised

The **incoming-packet parser hook body** (shadow creature/channel tables, the
proxy forward) only fires on real game packets, which needs the client connected
and in-game. Headless at the login screen there is no server session
(`[0x64A9C0]==0`), so that path was installed but not triggered. Connecting to an
OTServ requires the client to render + interact (patch login host + RSA, account
manager) which the no-desktop VM can't drive. Everything reachable without an
in-game session — injection, unpack, DllMain, and the full hook installation —
was confirmed live and matches the static RE exactly.
