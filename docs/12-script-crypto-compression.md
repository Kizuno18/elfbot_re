# elfbot.dll — crypto & compression subsystem

> **Resolved — this cluster is unused, statically-linked library code.** A full
> reverse call-graph walk (12 levels up from every crypto/compression entry) hits
> **33 functions and never reaches ElfBot's own bot logic** (`.jdrv`,
> `< 0x1002C000`); the only string anywhere in that tree is **`"1.2.3"` — the
> zlib version**. So the whole Blowfish + BWT + LZW + RLE/zlib + white-box-cipher
> stack is a third-party archive/compression library the toolchain linked in
> (zlib 1.2.3, pulled via a Boost / compression dependency) that the bot **never
> calls**. It has no live target:
>
> - **Not the `.elfc`/`.elft`** — those are a sparse-write opcode stream, not
>   ciphertext ([`22-elfc-file-format.md`](22-elfc-file-format.md)).
> - **Not the network stream** — the proxy cipher (`decryptPacketBlocks` /
>   `encryptPacketBlocks` `0x100212A3/0x100212D7`, [09](09-packet-proxy.md))
>   processes 8-byte blocks by calling the **Tibia client's own XTEA routine at
>   `0x549F60`**, not this cluster.
> - **Not online DRM** — elfbot.dll imports no HTTP/WinINet; there is no reachable
>   caller from bot code.
>
> **Indirect-dispatch check (airtight):** a raw scan for stored pointers to the
> cipher/compression entries finds refs only inside the library's own dispatch
> tables — `.rdata` at `0x1038F70C`/`0x103901C4`/`0x1038F770`/`0x10390228` and
> jiru code `0x1031C730` — all `>= 0x1031C000`, i.e. still the statically-linked
> runtime, never `.jdrv` bot logic (`< 0x1002C000`). So even accounting for
> function-pointer dispatch, no path reaches ElfBot's code.
>
> The function inventory below is still a correct RE of the library; it simply is
> not part of ElfBot's runtime behaviour.

A cluster of ~59 functions in `.jiru` implements a full compress-then-encrypt
stack: BWT + LZW + RLE/zlib compression and a Blowfish + custom/white-box
block-cipher bank. Present in the binary and reversed here; the exact data it is
applied to at runtime is noted in the correction above.

## Compression stages

| Address | Name | Purpose |
|---|---|---|
| `0x102eba10` | `rleCompressOrZlibDeflate` | RLE-compress 0xFF runs into escape pairs; if g_1038c268 zlib handle set, deflates via sub_1034b0ae instead, writing a leading tag byte. |
| `0x102ebca0` | `rleDecompressOrZlibInflate` | Inverse of sub_102eba10: expands 0xFF RLE escape pairs, or zlib-inflates via sub_1034c7cc/sub_1034c8d8 when g_1038c268 is set. |
| `0x102ebe90` | `lzwEncode` | LZW compressor: builds a dictionary via sub_102ec2e0 hash table (g_103a177c), emits codes with sub_102ec130, growing code width past g_103a1770 up to 0x7fff. |
| `0x102ec380` | `lzwDecode` | LZW decompressor: reads codes with sub_102ec590, rebuilds strings from the g_103a176c dictionary/g_103a177c table, emitting bytes into output buffer. |
| `0x102ecc50` | `bwtInverseTransform` | Inverse Burrows-Wheeler transform: sorts rotation indices (sub_102edf10), follows the primary-index chain to reconstruct the original byte sequence. |
| `0x102ed6b0` | `bwtRadixQuicksortByMask` | BWT suffix quicksort partition by bit-mask a3: presorts small runs, splits indices on the mask bit, recurses on halves shifting the mask (sub_102edfe0 swaps). |
| `0x102ed940` | `bwtMsdRadixSortRecurse` | BWT MSD radix-sort recursion: keys suffixes at depth a3 via sub_102ee060/sub_102edf80, sorts (sub_102ed6b0), and recurses on equal-key groups deeper. |
| `0x102edcb0` | `bwtBuildSuffixArray` | BWT setup: fills struct fields, counting-sorts the 256 byte buckets, seeds the suffix-index array, then radix-sorts each multi-entry bucket via sub_102ed940. |
| `0x102eebb0` | `cipherPermuteBlockEnc00` | Custom bit-mixing block-cipher round: XOR constants interleaved with bitfield ops sub_102f2bf0/c20/ca0/d00 (encrypt direction of the sub_102eed50 pair). |
| `0x1031cc30` | `decompressPayloadBlock` | Reads a length-prefixed block (high-bit = uncompressed), allocates buffer, decompresses via sub_102ebca0 or copies raw, optionally callbacks a3. |
| `0x1034b0ae` | `zlib_deflate` | zlib deflate() state machine: emits gzip/zlib header bytes, name/comment/extra fields and drives block flushing per flush level. |
| `0x1034bc5e` | `zlib_deflate_stored` | zlib deflate_stored: copy uncompressed stored blocks, filling the window and flushing when pending output is full. |
| `0x1034bd86` | `zlib_deflate_fast` | zlib deflate_fast: LZ77 hash-chain match, emit literal/length-distance via _tr_tally, slide window and flush blocks. |
| `0x1034c074` | `zlib_deflate_slow` | zlib deflate_slow: lazy-match LZ77 with previous-match comparison, emitting literals/matches and flushing blocks. |
| `0x1034c8d8` | `zlib_tr_flush_block` | zlib _tr_flush_block / compress_block: build dynamic Huffman trees, pick stored/fixed/dynamic block type and emit compressed data. |
| `0x1034e823` | `zlib_compress_block_send` | zlib compress_block inner: emit Huffman codes for literal/length and distance symbols from the sym_buf via send_bits. |
| `0x1034f083` | `zlib_gen_codes` | zlib gen_bitlen/gen_codes: assign Huffman code lengths from frequencies and build canonical codes for a tree descriptor. |
| `0x1034f51e` | `zlib_flush_block_choose` | zlib _tr_flush_block wrapper: build literal/distance trees, compute static vs dynamic block cost and emit the chosen block. |
| `0x1034fb0b` | `zlib_build_tree` | zlib build_tree / scan_tree: Huffman tree construction via heap (pqdownheap) and bit-length code scan for tree compression. |

The pipeline is a classic **BWT → MTF/RLE → LZW/entropy** compressor (bzip2-like:
Burrows-Wheeler transform + suffix-array radix sort, run-length escapes, LZW
dictionary), with an optional zlib deflate path gated by `g_1038c268`.

## Encryption stages

| Address | Name | Purpose |
|---|---|---|
| `0x102eb340` | `blowfishInitKey` | Blowfish key schedule: loads P-array + 4 S-boxes from digits-of-pi constants, then XORs the key in and re-encrypts P/S via sub_102eb5b0. |
| `0x102eebb0` | `cipherPermuteBlockEnc00` | Custom bit-mixing block-cipher round: XOR constants interleaved with bitfield ops sub_102f2bf0/c20/ca0/d00 (encrypt direction of the sub_102eed50 pair). |
| `0x102eed50` | `cipherPermuteBlockDec00` | Inverse of sub_102eebb0: same bit-ops in reverse order with negated shifts, decrypting the block permutation. |
| `0x102eef00` | `cipherPermuteBlockEnc01` | Custom block-cipher permutation round (encrypt); inverse-paired with sub_102ef020. |
| `0x102ef020` | `cipherPermuteBlockDec01` | Inverse block-cipher permutation of sub_102eef00 (decrypt, reversed ops, negated shifts). |
| `0x102ef140` | `cipherPermuteBlockEnc02` | Custom block-cipher permutation round (encrypt); inverse-paired with sub_102ef270. |
| `0x102ef270` | `cipherPermuteBlockDec02` | Inverse block-cipher permutation of sub_102ef140 (decrypt). |
| `0x102ef530` | `cipherPermuteBlockEnc03` | Custom block-cipher permutation round (encrypt); inverse-paired with sub_102ef640. |
| `0x102ef640` | `cipherPermuteBlockDec03` | Inverse block-cipher permutation of sub_102ef530 (decrypt). |
| `0x102ef750` | `cipherPermuteBlockEnc04` | Custom block-cipher permutation round (encrypt); inverse-paired with sub_102ef8d0. |
| `0x102ef8d0` | `cipherPermuteBlockDec04` | Inverse block-cipher permutation of sub_102ef750 (decrypt). |
| `0x102efa50` | `cipherPermuteBlockEnc05` | Custom block-cipher permutation round (encrypt); inverse-paired with sub_102efba0. |
| `0x102efba0` | `cipherPermuteBlockDec05` | Inverse block-cipher permutation of sub_102efa50 (decrypt). |
| `0x102efe30` | `cipherPermuteBlockEnc06` | Custom block-cipher permutation round (encrypt); inverse-paired with sub_102effb0. |
| `0x102effb0` | `cipherPermuteBlockDec06` | Inverse block-cipher permutation of sub_102efe30 (decrypt). |
| `0x102f0130` | `cipherPermuteBlockEnc07` | Custom block-cipher permutation round (encrypt); inverse-paired with sub_102f02b0. |
| `0x102f02b0` | `cipherPermuteBlockDec07` | Inverse block-cipher permutation of sub_102f0130 (decrypt). |
| `0x102f0a30` | `cipherPermuteBlockEnc08` | Custom block-cipher permutation round (encrypt); inverse-paired with sub_102f0ba0. |
| `0x102f0ba0` | `cipherPermuteBlockDec08` | Inverse block-cipher permutation of sub_102f0a30 (decrypt). |
| `0x102f0ff0` | `cipherPermuteBlockEnc09` | Custom block-cipher permutation round (encrypt); inverse-paired with sub_102f1120. |
| `0x102f1120` | `cipherPermuteBlockDec09` | Inverse block-cipher permutation of sub_102f0ff0 (decrypt). |
| `0x102f1250` | `cipherPermuteBlockEnc10` | Custom block-cipher permutation round (encrypt); inverse-paired with sub_102f1390. |
| `0x102f1390` | `cipherPermuteBlockDec10` | Inverse block-cipher permutation of sub_102f1250 (decrypt). |
| `0x102f14d0` | `cipherPermuteBlockEnc11` | Custom block-cipher permutation round (encrypt); inverse-paired with sub_102f1670. |
| `0x102f1670` | `cipherPermuteBlockDec11` | Inverse block-cipher permutation of sub_102f14d0 (decrypt). |
| `0x102f1810` | `cipherPermuteBlockEnc12` | Custom block-cipher permutation round (encrypt); inverse-paired with sub_102f1910. |
| `0x102f1910` | `cipherPermuteBlockDec12` | Inverse block-cipher permutation of sub_102f1810 (decrypt). |
| `0x102f1a10` | `cipherPermuteBlockEnc13` | Custom block-cipher permutation round (encrypt); inverse-paired with sub_102f1b90. |
| `0x102f1b90` | `cipherPermuteBlockDec13` | Inverse block-cipher permutation of sub_102f1a10 (decrypt). |
| `0x102f1d10` | `cipherPermuteBlockEnc14` | Custom block-cipher permutation round (encrypt): XOR-constant + bitfield-op mixing network, matching the forward direction of its sibling functions. |
| `0x102f1e90` | `whiteboxCipherPermuteBlockA` | White-box block cipher round: XORs constants and applies sub_102f2c*/2d00 nonlinear ops to transform a 32-bit word (forward direction). |
| `0x102f2010` | `whiteboxCipherPermuteBlockB` | Another forward white-box cipher permutation over a 32-bit word using XOR constants and the sub_102f2bf0/c20/ca0/d00 primitive set. |
| `0x102f2170` | `whiteboxCipherInverseBlockB` | Inverse of sub_102f2010: same constants/ops applied in reverse order with negated rotation shifts to undo the permutation. |
| `0x102f22d0` | `whiteboxCipherPermuteBlockC` | Forward white-box cipher permutation of a 32-bit word (distinct constant schedule from the other block variants). |
| `0x102f2420` | `whiteboxCipherInverseBlockC` | Inverse of sub_102f22d0: reverse-order primitives with negated shifts to invert the block-C permutation. |
| `0x102f2570` | `whiteboxCipherPermuteBlockD` | Forward white-box cipher permutation of a 32-bit word with its own XOR-constant schedule. |
| `0x102f2690` | `whiteboxCipherInverseBlockD` | Inverse of sub_102f2570: reverse-order primitives with negated shifts. |
| `0x102f27b0` | `whiteboxCipherPermuteBlockE` | Forward white-box cipher permutation of a 32-bit word (longest constant schedule of the set). |
| `0x102f2940` | `whiteboxCipherInverseBlockE` | Inverse of sub_102f27b0: reverse-order primitives with negated shifts to undo block-E. |
| `0x102fe470` | `obfuscatedFlagChainCompute` | Heavily-obfuscated (VM-lifted _ccall/_INSERT) routine combining sub_102f1910/ef020 results and globals g_1038c7dc/e0, returning via sub_102eef00. |

A **Blowfish** key schedule (P-array + S-boxes seeded from the digits of pi)
plus a bank of ~15 custom **block-cipher permutation rounds**, each an
encrypt/decrypt pair (`cipherPermuteBlockEncNN` / `DecNN`) built from a small set
of nonlinear bitfield primitives (`sub_102f2bf0/c20/ca0/d00`), and a set of
**white-box cipher** variants (A–E) that fold the key into the code. An
obfuscated (VM-lifted) flag-chain routine ties results together. This is the
anti-tamper layer over the script format and likely the same primitive set the
author used for the online script DRM (`ciroscript.com`).

## Relationship to the file format

`.elfc`/`.elft` header (`A0 FE FF FF` + magic `40 42 7E 42`, high-bit `0x40`/`0x80`
field delimiters — see [07](07-ciroscript-language.md)) wraps a
compressed+encrypted CiroScript token stream. The loaders
(`0x10015b79` open `.elfc`, `0x10015843` open `.elft`) call into this subsystem
to recover the plaintext command lines, which then feed the interpreter
([11](11-ciroscript-engine.md)). Full byte-level format recovery = run a sample
`.elfc` through these decrypt/decompress functions; the function set is now
mapped.
