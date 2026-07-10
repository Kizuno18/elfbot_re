#!/usr/bin/env python3
"""Decode a compiled ElfBot .elfc / .elft file.

Reimplements elfbot.dll `sub_10012771` (0x10012771): the compiled cavebot/
targeting files are a sparse-write opcode stream into a fixed in-memory table,
NOT an encrypted blob. Header magic is 0xFFFFFEA0 (bytes A0 FE FF FF). Each
opcode carries a skip count (low 6 bits) then a byte/word/dword literal; the
stream ends at a byte-op whose data byte is 0. Files without the magic are
stored raw (memcpy fallback).

Usage: decode_elfc.py <file.elfc> [out.bin]
"""
import sys, struct

MAGIC = 0xFFFFFEA0


def decode(data, dst_size=1 << 21):
    if len(data) < 4 or struct.unpack_from("<I", data, 0)[0] != MAGIC:
        return bytes(data)                       # raw / no magic -> stored verbatim
    dst = bytearray(dst_size)
    s = 4                                        # src cursor (past the 4-byte magic)
    d = 0                                        # dst cursor
    while s < len(data):
        op = data[s]
        if op >= 0xC0:                           # skip a 14-bit zero gap
            gap = ((op & 0x3F) << 8) | data[s + 1]
            d += gap
            s += 2
        elif op >= 0x80:                         # skip (op&0x3F), write dword
            d += op & 0x3F
            struct.pack_into("<I", dst, d, struct.unpack_from("<I", data, s + 1)[0])
            d += 4
            s += 5
        elif op >= 0x40:                         # skip (op&0x3F), write word
            d += op & 0x3F
            struct.pack_into("<H", dst, d, struct.unpack_from("<H", data, s + 1)[0])
            d += 2
            s += 3
        else:                                    # skip (op&0x3F), write one byte
            d += op & 0x3F
            b = data[s + 1]
            if b == 0:                           # terminator
                break
            dst[d] = b
            d += 1
            s += 2
    return bytes(dst[:d])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    raw = open(sys.argv[1], "rb").read()
    out = decode(raw)
    header = struct.unpack_from("<I", raw, 0)[0] if len(raw) >= 4 else 0
    sys.stderr.write(f"in={len(raw)}B header=0x{header:08X} "
                     f"{'(magic, decoded)' if header == MAGIC else '(raw)'} out={len(out)}B\n")
    if len(sys.argv) > 2:
        open(sys.argv[2], "wb").write(out)
    else:
        sys.stdout.buffer.write(out)
