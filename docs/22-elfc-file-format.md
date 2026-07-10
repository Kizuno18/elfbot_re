# `.elfc` / `.elft` compiled file format

The compiled cavebot (`.elfc`) and targeting (`.elft`) files are **not
encrypted**. They are a *sparse-write opcode stream* that reconstructs a
fixed-size in-memory table (the cavebot waypoint table `g_101e6ea8`, or the
targeting-record array). This is why they carry ~5 bits/byte of entropy and leak
readable fragments (waypoint labels, NPC names) rather than looking like
ciphertext. The crypto/compression cluster in [`12`](12-script-crypto-compression.md)
is a separate `.jiru` code path and is **not** on the `.elfc`/`.elft` load path
observed here.

## Loader path

`loadCavebotFile` (`0x10015b79`) reads the file, then `decodeSparseTable`
(`sub_10012771`, `0x10012771`) expands it into the target table. The decoder is
reproduced and validated in [`tools/decode_elfc.py`](../tools/decode_elfc.py).

## Container

```
offset 0:  A0 FE FF FF        magic  (uint32 LE 0xFFFFFEA0)
offset 4:  <opcode stream>
```

If the leading dword is not `0xFFFFFEA0` the loader `memcpy`s the file verbatim
(a raw/uncompiled table). Otherwise it zero-fills the destination table and
replays the opcode stream.

## Opcode stream

The destination is a zeroed fixed-size buffer; a write cursor `d` walks forward.
Every opcode first **advances the cursor** (leaving zeros — the "sparse" part),
then writes a literal of a width chosen by the opcode's class. The low 6 bits of
the opcode byte are the skip count (except the `>=0xC0` class, which is a pure
14-bit gap).

| Opcode `b` | Meaning | Encoding | Cursor effect |
|---|---|---|---|
| `b >= 0xC0` | skip a large zero gap | `b, lo` → gap = `((b & 0x3F) << 8) \| lo` | `d += gap`; consumes 2 bytes |
| `0x80..0xBF` | skip then write **dword** | `b, d0,d1,d2,d3` | `d += (b&0x3F)`; write u32; `d += 4`; consumes 5 bytes |
| `0x40..0x7F` | skip then write **word** | `b, w0,w1` | `d += (b&0x3F)`; write u16; `d += 2`; consumes 3 bytes |
| `0x00..0x3F` | skip then write **byte** | `b, v` | `d += (b&0x3F)`; if `v == 0` **END**; else write `v`; `d += 1`; consumes 2 bytes |

The stream terminates on a byte-class opcode (`< 0x40`) whose data byte is `0`.
So a literal string of N bytes is encoded as N consecutive `0x00, <char>` pairs
(skip 0, write one byte), and runs of unchanged/zero table cells become a single
gap opcode — a run-length scheme tuned for a mostly-sparse struct with short
literal islands.

## Validation

`tools/decode_elfc.py` on the shipped samples:

| File | in | header | out (table) | recovered content |
|---|---|---|---|---|
| `CAVE - Dragon Lair - CiroScript.elfc` | 29,097 B | `0xFFFFFEA0` | 283,011 B | waypoint labels `Thais`, `Captain Vip`, `Rashid`, `Xodet`, `Inicio 1/2/3`, `Depot`; travel-NPC names |
| `!TARGETING - CiroScript.elft` | 1,306 B | `0xFFFFFEA0` | 41,005 B | targeting category `others` + per-monster records |

The 283 KB output is the cavebot waypoint table; the 41 KB output is the
targeting record array — the exact in-memory structures the walker
([`17`](17-cavebot-walker.md)) and targeting engine ([`16`](16-targeting-engine.md))
read. The next layer (parsing those tables into typed waypoint/targeting records)
is `parseWaypointsSection` (`0x10016438`) / `parseTargetingRecord` (`0x1001686c`).

## Detection / interop note

Because the format is a plain sparse-opcode encoding, cavebot and targeting
scripts are fully recoverable offline with `decode_elfc.py` — no key needed. An
anti-cheat can also recognise a freshly-`memset` 283 KB table populated in the
bot process right after a `.elfc` file read as a cavebot-load fingerprint.
