# elfbot.dll `.jiru`/`.cdtemn` — function catalog

All 5935 support-section functions. **304 bot-logic dispatchers** are described from their pseudo-C (notably a crypto/compression subsystem — see [doc 12](../12-script-crypto-compression.md)); the remainder are statically-linked MSVC STL / Boost / C++ runtime, labelled by structure. Decompiled C in [decompiled/jiru-index.md](decompiled/jiru-index.md).

| Address | Name | Size | Purpose |
|---|---|---|---|
| `0x102eb000` | `sub_102eb000` | 100 | support routine (100 bytes) |
| `0x102eb070` | `sub_102eb070` | 52 | support routine (52 bytes) |
| `0x102eb0b0` | `sub_102eb0b0` | 81 | support routine (81 bytes) |
| `0x102eb110` | `sub_102eb110` | 65 | support routine (65 bytes) |
| `0x102eb160` | `sub_102eb160` | 34 | support routine (34 bytes) |
| `0x102eb190` | `sub_102eb190` | 51 | support routine (51 bytes) |
| `0x102eb1d0` | `sub_102eb1d0` | 44 | support routine (44 bytes) |
| `0x102eb200` | `sub_102eb200` | 54 | support routine (54 bytes) |
| `0x102eb240` | `sub_102eb240` | 55 | support routine (55 bytes) |
| `0x102eb280` | `sub_102eb280` | 44 | support routine (44 bytes) |
| `0x102eb2b0` | `sub_102eb2b0` | 65 | support routine (65 bytes) |
| `0x102eb300` | `sub_102eb300` | 59 | support routine (59 bytes) |
| `0x102eb340` | `blowfishInitKey` | 615 | Blowfish key schedule: loads P-array + 4 S-boxes from digits-of-pi constants, then XORs the key in and re-encrypts P/S via sub_102eb5b0. |
| `0x102eb5b0` | `sub_102eb5b0` | 181 | support routine (181 bytes) |
| `0x102eb670` | `sub_102eb670` | 85 | support routine (85 bytes) |
| `0x102eb6d0` | `sub_102eb6d0` | 26 | support routine (26 bytes) |
| `0x102eb6f0` | `sub_102eb6f0` | 90 | support routine (90 bytes) |
| `0x102eb750` | `sub_102eb750` | 90 | support routine (90 bytes) |
| `0x102eb7b0` | `sub_102eb7b0` | 181 | support routine (181 bytes) |
| `0x102eb870` | `sub_102eb870` | 94 | support routine (94 bytes) |
| `0x102eb8d0` | `sub_102eb8d0` | 24 | support routine (24 bytes) |
| `0x102eb8f0` | `sub_102eb8f0` | 76 | support routine (76 bytes) |
| `0x102eb940` | `sub_102eb940` | 122 | support routine (122 bytes) |
| `0x102eb9c0` | `sub_102eb9c0` | 65 | support routine (65 bytes) |
| `0x102eba10` | `rleCompressOrZlibDeflate` | 645 | RLE-compress 0xFF runs into escape pairs; if g_1038c268 zlib handle set, deflates via sub_1034b0ae instead, writing a leading tag byte. |
| `0x102ebca0` | `rleDecompressOrZlibInflate` | 492 | Inverse of sub_102eba10: expands 0xFF RLE escape pairs, or zlib-inflates via sub_1034c7cc/sub_1034c8d8 when g_1038c268 is set. |
| `0x102ebe90` | `lzwEncode` | 507 | LZW compressor: builds a dictionary via sub_102ec2e0 hash table (g_103a177c), emits codes with sub_102ec130, growing code width past g_103a1770 up to 0x7fff. |
| `0x102ec090` | `sub_102ec090` | 98 | support routine (98 bytes) |
| `0x102ec100` | `sub_102ec100` | 44 | support routine (44 bytes) |
| `0x102ec130` | `sub_102ec130` | 190 | support routine (190 bytes) |
| `0x102ec1f0` | `sub_102ec1f0` | 59 | support routine (59 bytes) |
| `0x102ec230` | `sub_102ec230` | 51 | support routine (51 bytes) |
| `0x102ec270` | `sub_102ec270` | 97 | support routine (97 bytes) |
| `0x102ec2e0` | `sub_102ec2e0` | 150 | support routine (150 bytes) |
| `0x102ec380` | `lzwDecode` | 517 | LZW decompressor: reads codes with sub_102ec590, rebuilds strings from the g_103a176c dictionary/g_103a177c table, emitting bytes into output buffer. |
| `0x102ec445` | `sub_102ec445` | 2 | trivial accessor/forwarder |
| `0x102ec455` | `sub_102ec455` | 2 | trivial accessor/forwarder |
| `0x102ec471` | `sub_102ec471` | 2 | trivial accessor/forwarder |
| `0x102ec590` | `sub_102ec590` | 174 | support routine (174 bytes) |
| `0x102ec640` | `sub_102ec640` | 95 | support routine (95 bytes) |
| `0x102ec6a0` | `sub_102ec6a0` | 515 | support routine (515 bytes) |
| `0x102ec8b0` | `sub_102ec8b0` | 115 | support routine (115 bytes) |
| `0x102ec930` | `sub_102ec930` | 31 | support routine (31 bytes) |
| `0x102ec950` | `sub_102ec950` | 35 | support routine (35 bytes) |
| `0x102ec980` | `sub_102ec980` | 19 | support routine (19 bytes) |
| `0x102ec9a0` | `sub_102ec9a0` | 19 | support routine (19 bytes) |
| `0x102ec9c0` | `sub_102ec9c0` | 137 | support routine (137 bytes) |
| `0x102eca50` | `sub_102eca50` | 511 | support routine (511 bytes) |
| `0x102ecc50` | `bwtInverseTransform` | 253 | Inverse Burrows-Wheeler transform: sorts rotation indices (sub_102edf10), follows the primary-index chain to reconstruct the original byte sequence. |
| `0x102ecd50` | `sub_102ecd50` | 259 | support routine (259 bytes) |
| `0x102ece60` | `sub_102ece60` | 127 | support routine (127 bytes) |
| `0x102ecee0` | `sub_102ecee0` | 152 | support routine (152 bytes) |
| `0x102ecf80` | `sub_102ecf80` | 260 | support routine (260 bytes) |
| `0x102ed090` | `sub_102ed090` | 590 | support routine (590 bytes) |
| `0x102ed2e0` | `sub_102ed2e0` | 341 | support routine (341 bytes) |
| `0x102ed344` | `sub_102ed344` | 5 | trivial accessor/forwarder |
| `0x102ed440` | `sub_102ed440` | 108 | support routine (108 bytes) |
| `0x102ed4a6` | `sub_102ed4a6` | 2 | trivial accessor/forwarder |
| `0x102ed4b0` | `sub_102ed4b0` | 167 | support routine (167 bytes) |
| `0x102ed4ef` | `sub_102ed4ef` | 2 | trivial accessor/forwarder |
| `0x102ed560` | `sub_102ed560` | 220 | support routine (220 bytes) |
| `0x102ed640` | `sub_102ed640` | 107 | support routine (107 bytes) |
| `0x102ed6b0` | `bwtRadixQuicksortByMask` | 651 | BWT suffix quicksort partition by bit-mask a3: presorts small runs, splits indices on the mask bit, recurses on halves shifting the mask (sub_102edfe0 swaps). |
| `0x102ed6f8` | `sub_102ed6f8` | 5 | trivial accessor/forwarder |
| `0x102ed940` | `bwtMsdRadixSortRecurse` | 868 | BWT MSD radix-sort recursion: keys suffixes at depth a3 via sub_102ee060/sub_102edf80, sorts (sub_102ed6b0), and recurses on equal-key groups deeper. |
| `0x102ed994` | `sub_102ed994` | 5 | trivial accessor/forwarder |
| `0x102edcb0` | `bwtBuildSuffixArray` | 603 | BWT setup: fills struct fields, counting-sorts the 256 byte buckets, seeds the suffix-index array, then radix-sorts each multi-entry bucket via sub_102ed940. |
| `0x102edf10` | `sub_102edf10` | 102 | support routine (102 bytes) |
| `0x102edf80` | `sub_102edf80` | 82 | support routine (82 bytes) |
| `0x102edfbe` | `sub_102edfbe` | 2 | trivial accessor/forwarder |
| `0x102edfe0` | `sub_102edfe0` | 127 | support routine (127 bytes) |
| `0x102ee060` | `sub_102ee060` | 29 | support routine (29 bytes) |
| `0x102ee080` | `sub_102ee080` | 24 | support routine (24 bytes) |
| `0x102ee0a0` | `sub_102ee0a0` | 34 | support routine (34 bytes) |
| `0x102ee0d0` | `sub_102ee0d0` | 112 | support routine (112 bytes) |
| `0x102ee140` | `sub_102ee140` | 151 | support routine (151 bytes) |
| `0x102ee1e0` | `sub_102ee1e0` | 245 | support routine (245 bytes) |
| `0x102ee2e0` | `sub_102ee2e0` | 180 | support routine (180 bytes) |
| `0x102ee3a0` | `sub_102ee3a0` | 218 | support routine (218 bytes) |
| `0x102ee480` | `sub_102ee480` | 632 | support routine (632 bytes) |
| `0x102ee700` | `sub_102ee700` | 406 | support routine (406 bytes) |
| `0x102ee8a0` | `sub_102ee8a0` | 300 | support routine (300 bytes) |
| `0x102ee9d0` | `sub_102ee9d0` | 76 | support routine (76 bytes) |
| `0x102eea20` | `sub_102eea20` | 144 | support routine (144 bytes) |
| `0x102eeab0` | `sub_102eeab0` | 134 | support routine (134 bytes) |
| `0x102eeb40` | `sub_102eeb40` | 17 | support routine (17 bytes) |
| `0x102eeb60` | `sub_102eeb60` | 73 | support routine (73 bytes) |
| `0x102eebb0` | `cipherPermuteBlockEnc00` | 415 | Custom bit-mixing block-cipher round: XOR constants interleaved with bitfield ops sub_102f2bf0/c20/ca0/d00 (encrypt direction of the sub_102eed50 pair). |
| `0x102eed50` | `cipherPermuteBlockDec00` | 418 | Inverse of sub_102eebb0: same bit-ops in reverse order with negated shifts, decrypting the block permutation. |
| `0x102eef00` | `cipherPermuteBlockEnc01` | 287 | Custom block-cipher permutation round (encrypt); inverse-paired with sub_102ef020. |
| `0x102ef020` | `cipherPermuteBlockDec01` | 287 | Inverse block-cipher permutation of sub_102eef00 (decrypt, reversed ops, negated shifts). |
| `0x102ef140` | `cipherPermuteBlockEnc02` | 291 | Custom block-cipher permutation round (encrypt); inverse-paired with sub_102ef270. |
| `0x102ef270` | `cipherPermuteBlockDec02` | 292 | Inverse block-cipher permutation of sub_102ef140 (decrypt). |
| `0x102ef3a0` | `sub_102ef3a0` | 192 | support routine (192 bytes) |
| `0x102ef460` | `sub_102ef460` | 194 | support routine (194 bytes) |
| `0x102ef530` | `cipherPermuteBlockEnc03` | 269 | Custom block-cipher permutation round (encrypt); inverse-paired with sub_102ef640. |
| `0x102ef640` | `cipherPermuteBlockDec03` | 268 | Inverse block-cipher permutation of sub_102ef530 (decrypt). |
| `0x102ef750` | `cipherPermuteBlockEnc04` | 377 | Custom block-cipher permutation round (encrypt); inverse-paired with sub_102ef8d0. |
| `0x102ef8d0` | `cipherPermuteBlockDec04` | 378 | Inverse block-cipher permutation of sub_102ef750 (decrypt). |
| `0x102efa50` | `cipherPermuteBlockEnc05` | 335 | Custom block-cipher permutation round (encrypt); inverse-paired with sub_102efba0. |
| `0x102efba0` | `cipherPermuteBlockDec05` | 335 | Inverse block-cipher permutation of sub_102efa50 (decrypt). |
| `0x102efcf0` | `sub_102efcf0` | 145 | support routine (145 bytes) |
| `0x102efd90` | `sub_102efd90` | 146 | support routine (146 bytes) |
| `0x102efe30` | `cipherPermuteBlockEnc06` | 371 | Custom block-cipher permutation round (encrypt); inverse-paired with sub_102effb0. |
| `0x102effb0` | `cipherPermuteBlockDec06` | 371 | Inverse block-cipher permutation of sub_102efe30 (decrypt). |
| `0x102f0130` | `cipherPermuteBlockEnc07` | 379 | Custom block-cipher permutation round (encrypt); inverse-paired with sub_102f02b0. |
| `0x102f02b0` | `cipherPermuteBlockDec07` | 381 | Inverse block-cipher permutation of sub_102f0130 (decrypt). |
| `0x102f0430` | `sub_102f0430` | 157 | support routine (157 bytes) |
| `0x102f04d0` | `sub_102f04d0` | 156 | support routine (156 bytes) |
| `0x102f0570` | `sub_102f0570` | 209 | support routine (209 bytes) |
| `0x102f0650` | `sub_102f0650` | 209 | support routine (209 bytes) |
| `0x102f0730` | `sub_102f0730` | 138 | support routine (138 bytes) |
| `0x102f07c0` | `sub_102f07c0` | 138 | support routine (138 bytes) |
| `0x102f0850` | `sub_102f0850` | 240 | support routine (240 bytes) |
| `0x102f0940` | `sub_102f0940` | 240 | support routine (240 bytes) |
| `0x102f0a30` | `cipherPermuteBlockEnc08` | 356 | Custom block-cipher permutation round (encrypt); inverse-paired with sub_102f0ba0. |
| `0x102f0ba0` | `cipherPermuteBlockDec08` | 358 | Inverse block-cipher permutation of sub_102f0a30 (decrypt). |
| `0x102f0d10` | `sub_102f0d10` | 173 | support routine (173 bytes) |
| `0x102f0dc0` | `sub_102f0dc0` | 174 | support routine (174 bytes) |
| `0x102f0e70` | `sub_102f0e70` | 189 | support routine (189 bytes) |
| `0x102f0f30` | `sub_102f0f30` | 192 | support routine (192 bytes) |
| `0x102f0ff0` | `cipherPermuteBlockEnc09` | 297 | Custom block-cipher permutation round (encrypt); inverse-paired with sub_102f1120. |
| `0x102f1120` | `cipherPermuteBlockDec09` | 295 | Inverse block-cipher permutation of sub_102f0ff0 (decrypt). |
| `0x102f1250` | `cipherPermuteBlockEnc10` | 318 | Custom block-cipher permutation round (encrypt); inverse-paired with sub_102f1390. |
| `0x102f1390` | `cipherPermuteBlockDec10` | 320 | Inverse block-cipher permutation of sub_102f1250 (decrypt). |
| `0x102f14d0` | `cipherPermuteBlockEnc11` | 410 | Custom block-cipher permutation round (encrypt); inverse-paired with sub_102f1670. |
| `0x102f1670` | `cipherPermuteBlockDec11` | 407 | Inverse block-cipher permutation of sub_102f14d0 (decrypt). |
| `0x102f1810` | `cipherPermuteBlockEnc12` | 255 | Custom block-cipher permutation round (encrypt); inverse-paired with sub_102f1910. |
| `0x102f1910` | `cipherPermuteBlockDec12` | 256 | Inverse block-cipher permutation of sub_102f1810 (decrypt). |
| `0x102f1a10` | `cipherPermuteBlockEnc13` | 375 | Custom block-cipher permutation round (encrypt); inverse-paired with sub_102f1b90. |
| `0x102f1b90` | `cipherPermuteBlockDec13` | 375 | Inverse block-cipher permutation of sub_102f1a10 (decrypt). |
| `0x102f1d10` | `cipherPermuteBlockEnc14` | 374 | Custom block-cipher permutation round (encrypt): XOR-constant + bitfield-op mixing network, matching the forward direction of its sibling functions. |
| `0x102f1e90` | `whiteboxCipherPermuteBlockA` | 374 | White-box block cipher round: XORs constants and applies sub_102f2c*/2d00 nonlinear ops to transform a 32-bit word (forward direction). |
| `0x102f2010` | `whiteboxCipherPermuteBlockB` | 351 | Another forward white-box cipher permutation over a 32-bit word using XOR constants and the sub_102f2bf0/c20/ca0/d00 primitive set. |
| `0x102f2170` | `whiteboxCipherInverseBlockB` | 351 | Inverse of sub_102f2010: same constants/ops applied in reverse order with negated rotation shifts to undo the permutation. |
| `0x102f22d0` | `whiteboxCipherPermuteBlockC` | 322 | Forward white-box cipher permutation of a 32-bit word (distinct constant schedule from the other block variants). |
| `0x102f2420` | `whiteboxCipherInverseBlockC` | 322 | Inverse of sub_102f22d0: reverse-order primitives with negated shifts to invert the block-C permutation. |
| `0x102f2570` | `whiteboxCipherPermuteBlockD` | 278 | Forward white-box cipher permutation of a 32-bit word with its own XOR-constant schedule. |
| `0x102f2690` | `whiteboxCipherInverseBlockD` | 278 | Inverse of sub_102f2570: reverse-order primitives with negated shifts. |
| `0x102f27b0` | `whiteboxCipherPermuteBlockE` | 396 | Forward white-box cipher permutation of a 32-bit word (longest constant schedule of the set). |
| `0x102f2940` | `whiteboxCipherInverseBlockE` | 396 | Inverse of sub_102f27b0: reverse-order primitives with negated shifts to undo block-E. |
| `0x102f2ad0` | `sub_102f2ad0` | 140 | support routine (140 bytes) |
| `0x102f2b60` | `sub_102f2b60` | 142 | support routine (142 bytes) |
| `0x102f2bf0` | `sub_102f2bf0` | 43 | support routine (43 bytes) |
| `0x102f2c20` | `sub_102f2c20` | 115 | support routine (115 bytes) |
| `0x102f2ca0` | `sub_102f2ca0` | 94 | support routine (94 bytes) |
| `0x102f2d00` | `sub_102f2d00` | 139 | support routine (139 bytes) |
| `0x102f2d90` | `sub_102f2d90` | 10 | trivial accessor/forwarder |
| `0x102f2da0` | `sub_102f2da0` | 18 | support routine (18 bytes) |
| `0x102f2dc0` | `sub_102f2dc0` | 11 | trivial accessor/forwarder |
| `0x102f2dd0` | `sub_102f2dd0` | 71 | support routine (71 bytes) |
| `0x102f2e20` | `sub_102f2e20` | 45 | support routine (45 bytes) |
| `0x102f2e50` | `sub_102f2e50` | 19 | support routine (19 bytes) |
| `0x102f2e70` | `sub_102f2e70` | 17 | support routine (17 bytes) |
| `0x102f2e90` | `sub_102f2e90` | 19 | support routine (19 bytes) |
| `0x102f2eb0` | `sub_102f2eb0` | 17 | support routine (17 bytes) |
| `0x102f2ed0` | `sub_102f2ed0` | 17 | support routine (17 bytes) |
| `0x102f2ef0` | `sub_102f2ef0` | 18 | support routine (18 bytes) |
| `0x102f2f10` | `sub_102f2f10` | 71 | support routine (71 bytes) |
| `0x102f2f60` | `sub_102f2f60` | 45 | support routine (45 bytes) |
| `0x102f2f90` | `sub_102f2f90` | 20 | support routine (20 bytes) |
| `0x102f2fb0` | `sub_102f2fb0` | 18 | support routine (18 bytes) |
| `0x102f2fd0` | `sub_102f2fd0` | 20 | support routine (20 bytes) |
| `0x102f2ff0` | `sub_102f2ff0` | 18 | support routine (18 bytes) |
| `0x102f3010` | `sub_102f3010` | 14 | trivial accessor/forwarder |
| `0x102f3020` | `sub_102f3020` | 142 | support routine (142 bytes) |
| `0x102f30b0` | `sub_102f30b0` | 175 | support routine (175 bytes) |
| `0x102f30fb` | `sub_102f30fb` | 10 | trivial accessor/forwarder |
| `0x102f3101` | `sub_102f3101` | 3 | trivial accessor/forwarder |
| `0x102f3118` | `sub_102f3118` | 3 | trivial accessor/forwarder |
| `0x102f3127` | `sub_102f3127` | 3 | trivial accessor/forwarder |
| `0x102f3138` | `sub_102f3138` | 3 | trivial accessor/forwarder |
| `0x102f3180` | `sub_102f3180` | 464 | support routine (464 bytes) |
| `0x102f31af` | `sub_102f31af` | 3 | trivial accessor/forwarder |
| `0x102f3200` | `sub_102f3200` | 3 | trivial accessor/forwarder |
| `0x102f3263` | `sub_102f3263` | 3 | trivial accessor/forwarder |
| `0x102f3278` | `sub_102f3278` | 3 | trivial accessor/forwarder |
| `0x102f32a8` | `sub_102f32a8` | 3 | trivial accessor/forwarder |
| `0x102f32b7` | `sub_102f32b7` | 3 | trivial accessor/forwarder |
| `0x102f32dd` | `sub_102f32dd` | 3 | trivial accessor/forwarder |
| `0x102f3315` | `sub_102f3315` | 3 | trivial accessor/forwarder |
| `0x102f3370` | `sub_102f3370` | 138 | support routine (138 bytes) |
| `0x102f3400` | `sub_102f3400` | 156 | support routine (156 bytes) |
| `0x102f3459` | `sub_102f3459` | 3 | trivial accessor/forwarder |
| `0x102f34a0` | `sub_102f34a0` | 159 | support routine (159 bytes) |
| `0x102f34c2` | `sub_102f34c2` | 5 | trivial accessor/forwarder |
| `0x102f3550` | `sub_102f3550` | 196 | support routine (196 bytes) |
| `0x102f3620` | `sub_102f3620` | 166 | support routine (166 bytes) |
| `0x102f36d0` | `sub_102f36d0` | 178 | support routine (178 bytes) |
| `0x102f3790` | `sub_102f3790` | 199 | support routine (199 bytes) |
| `0x102f3860` | `sub_102f3860` | 121 | support routine (121 bytes) |
| `0x102f38e0` | `sub_102f38e0` | 173 | support routine (173 bytes) |
| `0x102f3990` | `sub_102f3990` | 169 | support routine (169 bytes) |
| `0x102f3a40` | `sub_102f3a40` | 126 | support routine (126 bytes) |
| `0x102f3a62` | `sub_102f3a62` | 5 | trivial accessor/forwarder |
| `0x102f3ad0` | `sub_102f3ad0` | 166 | support routine (166 bytes) |
| `0x102f3b80` | `sub_102f3b80` | 148 | support routine (148 bytes) |
| `0x102f3bac` | `sub_102f3bac` | 3 | trivial accessor/forwarder |
| `0x102f3c20` | `sub_102f3c20` | 211 | support routine (211 bytes) |
| `0x102f3d00` | `sub_102f3d00` | 338 | support routine (338 bytes) |
| `0x102f3ddc` | `sub_102f3ddc` | 3 | trivial accessor/forwarder |
| `0x102f3e60` | `sub_102f3e60` | 162 | support routine (162 bytes) |
| `0x102f3e8f` | `sub_102f3e8f` | 3 | trivial accessor/forwarder |
| `0x102f3f10` | `sub_102f3f10` | 225 | support routine (225 bytes) |
| `0x102f3f30` | `sub_102f3f30` | 1 | trivial accessor/forwarder |
| `0x102f4000` | `sub_102f4000` | 126 | support routine (126 bytes) |
| `0x102f4022` | `sub_102f4022` | 5 | trivial accessor/forwarder |
| `0x102f4090` | `sub_102f4090` | 176 | support routine (176 bytes) |
| `0x102f40bf` | `sub_102f40bf` | 3 | trivial accessor/forwarder |
| `0x102f4101` | `sub_102f4101` | 3 | trivial accessor/forwarder |
| `0x102f4150` | `sub_102f4150` | 248 | support routine (248 bytes) |
| `0x102f4250` | `sub_102f4250` | 172 | support routine (172 bytes) |
| `0x102f4300` | `sub_102f4300` | 263 | support routine (263 bytes) |
| `0x102f4410` | `sub_102f4410` | 438 | support routine (438 bytes) |
| `0x102f45d0` | `sub_102f45d0` | 463 | support routine (463 bytes) |
| `0x102f45f0` | `sub_102f45f0` | 1 | trivial accessor/forwarder |
| `0x102f4689` | `sub_102f4689` | 1 | trivial accessor/forwarder |
| `0x102f46af` | `sub_102f46af` | 1 | trivial accessor/forwarder |
| `0x102f46fc` | `sub_102f46fc` | 3 | trivial accessor/forwarder |
| `0x102f4711` | `sub_102f4711` | 1 | trivial accessor/forwarder |
| `0x102f4745` | `sub_102f4745` | 3 | trivial accessor/forwarder |
| `0x102f4754` | `sub_102f4754` | 3 | trivial accessor/forwarder |
| `0x102f4765` | `sub_102f4765` | 3 | trivial accessor/forwarder |
| `0x102f47b0` | `sub_102f47b0` | 185 | support routine (185 bytes) |
| `0x102f4870` | `sub_102f4870` | 229 | support routine (229 bytes) |
| `0x102f4890` | `sub_102f4890` | 1 | trivial accessor/forwarder |
| `0x102f4960` | `sub_102f4960` | 209 | support routine (209 bytes) |
| `0x102f49c3` | `sub_102f49c3` | 1 | trivial accessor/forwarder |
| `0x102f4a40` | `sub_102f4a40` | 154 | support routine (154 bytes) |
| `0x102f4a6c` | `sub_102f4a6c` | 3 | trivial accessor/forwarder |
| `0x102f4ae0` | `sub_102f4ae0` | 121 | support routine (121 bytes) |
| `0x102f4b02` | `sub_102f4b02` | 5 | trivial accessor/forwarder |
| `0x102f4b60` | `sub_102f4b60` | 210 | support routine (210 bytes) |
| `0x102f4c40` | `sub_102f4c40` | 139 | support routine (139 bytes) |
| `0x102f4c64` | `sub_102f4c64` | 1 | trivial accessor/forwarder |
| `0x102f4cd0` | `sub_102f4cd0` | 173 | support routine (173 bytes) |
| `0x102f4d29` | `sub_102f4d29` | 3 | trivial accessor/forwarder |
| `0x102f4d38` | `sub_102f4d38` | 3 | trivial accessor/forwarder |
| `0x102f4d49` | `sub_102f4d49` | 3 | trivial accessor/forwarder |
| `0x102f4d90` | `sub_102f4d90` | 480 | support routine (480 bytes) |
| `0x102f4db0` | `sub_102f4db0` | 1 | trivial accessor/forwarder |
| `0x102f4e4d` | `sub_102f4e4d` | 1 | trivial accessor/forwarder |
| `0x102f4e7e` | `sub_102f4e7e` | 1 | trivial accessor/forwarder |
| `0x102f4ecb` | `sub_102f4ecb` | 3 | trivial accessor/forwarder |
| `0x102f4ee2` | `sub_102f4ee2` | 1 | trivial accessor/forwarder |
| `0x102f4f16` | `sub_102f4f16` | 3 | trivial accessor/forwarder |
| `0x102f4f25` | `sub_102f4f25` | 3 | trivial accessor/forwarder |
| `0x102f4f36` | `sub_102f4f36` | 1 | trivial accessor/forwarder |
| `0x102f4f80` | `sub_102f4f80` | 155 | support routine (155 bytes) |
| `0x102f5020` | `sub_102f5020` | 184 | support routine (184 bytes) |
| `0x102f50e0` | `sub_102f50e0` | 378 | support routine (378 bytes) |
| `0x102f5140` | `sub_102f5140` | 1 | trivial accessor/forwarder |
| `0x102f5260` | `sub_102f5260` | 207 | support routine (207 bytes) |
| `0x102f5330` | `sub_102f5330` | 160 | support routine (160 bytes) |
| `0x102f536c` | `sub_102f536c` | 1 | trivial accessor/forwarder |
| `0x102f5390` | `sub_102f5390` | 1 | trivial accessor/forwarder |
| `0x102f53e0` | `sub_102f53e0` | 173 | support routine (173 bytes) |
| `0x102f540f` | `sub_102f540f` | 3 | trivial accessor/forwarder |
| `0x102f5426` | `sub_102f5426` | 1 | trivial accessor/forwarder |
| `0x102f54a0` | `sub_102f54a0` | 139 | support routine (139 bytes) |
| `0x102f54bf` | `sub_102f54bf` | 1 | trivial accessor/forwarder |
| `0x102f54cd` | `sub_102f54cd` | 1 | trivial accessor/forwarder |
| `0x102f5530` | `sub_102f5530` | 192 | support routine (192 bytes) |
| `0x102f55f0` | `sub_102f55f0` | 168 | support routine (168 bytes) |
| `0x102f56a0` | `sub_102f56a0` | 115 | support routine (115 bytes) |
| `0x102f56bf` | `sub_102f56bf` | 1 | trivial accessor/forwarder |
| `0x102f56cd` | `sub_102f56cd` | 1 | trivial accessor/forwarder |
| `0x102f5720` | `sub_102f5720` | 224 | support routine (224 bytes) |
| `0x102f5754` | `sub_102f5754` | 1 | trivial accessor/forwarder |
| `0x102f5775` | `sub_102f5775` | 1 | trivial accessor/forwarder |
| `0x102f57ae` | `sub_102f57ae` | 3 | trivial accessor/forwarder |
| `0x102f57bd` | `sub_102f57bd` | 3 | trivial accessor/forwarder |
| `0x102f57ce` | `sub_102f57ce` | 3 | trivial accessor/forwarder |
| `0x102f5810` | `sub_102f5810` | 480 | support routine (480 bytes) |
| `0x102f5830` | `sub_102f5830` | 1 | trivial accessor/forwarder |
| `0x102f58cd` | `sub_102f58cd` | 1 | trivial accessor/forwarder |
| `0x102f58fe` | `sub_102f58fe` | 1 | trivial accessor/forwarder |
| `0x102f5946` | `sub_102f5946` | 3 | trivial accessor/forwarder |
| `0x102f595d` | `sub_102f595d` | 1 | trivial accessor/forwarder |
| `0x102f5996` | `sub_102f5996` | 3 | trivial accessor/forwarder |
| `0x102f59a5` | `sub_102f59a5` | 3 | trivial accessor/forwarder |
| `0x102f59b6` | `sub_102f59b6` | 1 | trivial accessor/forwarder |
| `0x102f5a00` | `sub_102f5a00` | 219 | support routine (219 bytes) |
| `0x102f5ae0` | `sub_102f5ae0` | 202 | support routine (202 bytes) |
| `0x102f5b0f` | `sub_102f5b0f` | 3 | trivial accessor/forwarder |
| `0x102f5b59` | `sub_102f5b59` | 3 | trivial accessor/forwarder |
| `0x102f5b68` | `sub_102f5b68` | 3 | trivial accessor/forwarder |
| `0x102f5bc0` | `sub_102f5bc0` | 167 | support routine (167 bytes) |
| `0x102f5c70` | `sub_102f5c70` | 282 | support routine (282 bytes) |
| `0x102f5d90` | `sub_102f5d90` | 126 | support routine (126 bytes) |
| `0x102f5db2` | `sub_102f5db2` | 5 | trivial accessor/forwarder |
| `0x102f5e20` | `sub_102f5e20` | 208 | support routine (208 bytes) |
| `0x102f5e83` | `sub_102f5e83` | 1 | trivial accessor/forwarder |
| `0x102f5f00` | `sub_102f5f00` | 127 | support routine (127 bytes) |
| `0x102f5f22` | `sub_102f5f22` | 5 | trivial accessor/forwarder |
| `0x102f5f90` | `sub_102f5f90` | 214 | support routine (214 bytes) |
| `0x102f5fb2` | `sub_102f5fb2` | 5 | trivial accessor/forwarder |
| `0x102f6070` | `sub_102f6070` | 159 | support routine (159 bytes) |
| `0x102f6110` | `sub_102f6110` | 388 | support routine (388 bytes) |
| `0x102f6170` | `sub_102f6170` | 1 | trivial accessor/forwarder |
| `0x102f62a0` | `sub_102f62a0` | 165 | support routine (165 bytes) |
| `0x102f6350` | `sub_102f6350` | 160 | support routine (160 bytes) |
| `0x102f63f0` | `sub_102f63f0` | 189 | support routine (189 bytes) |
| `0x102f641f` | `sub_102f641f` | 3 | trivial accessor/forwarder |
| `0x102f6436` | `sub_102f6436` | 3 | trivial accessor/forwarder |
| `0x102f6458` | `sub_102f6458` | 3 | trivial accessor/forwarder |
| `0x102f6474` | `sub_102f6474` | 3 | trivial accessor/forwarder |
| `0x102f64c0` | `sub_102f64c0` | 382 | support routine (382 bytes) |
| `0x102f65c3` | `sub_102f65c3` | 3 | trivial accessor/forwarder |
| `0x102f6650` | `sub_102f6650` | 147 | support routine (147 bytes) |
| `0x102f667d` | `sub_102f667d` | 1 | trivial accessor/forwarder |
| `0x102f66f0` | `sub_102f66f0` | 176 | support routine (176 bytes) |
| `0x102f67a0` | `sub_102f67a0` | 174 | support routine (174 bytes) |
| `0x102f6850` | `sub_102f6850` | 150 | support routine (150 bytes) |
| `0x102f687f` | `sub_102f687f` | 3 | trivial accessor/forwarder |
| `0x102f68f0` | `sub_102f68f0` | 126 | support routine (126 bytes) |
| `0x102f6912` | `sub_102f6912` | 5 | trivial accessor/forwarder |
| `0x102f6980` | `sub_102f6980` | 264 | support routine (264 bytes) |
| `0x102f6a90` | `sub_102f6a90` | 240 | support routine (240 bytes) |
| `0x102f6b90` | `sub_102f6b90` | 188 | support routine (188 bytes) |
| `0x102f6bca` | `sub_102f6bca` | 1 | trivial accessor/forwarder |
| `0x102f6be3` | `sub_102f6be3` | 1 | trivial accessor/forwarder |
| `0x102f6c50` | `sub_102f6c50` | 194 | support routine (194 bytes) |
| `0x102f6c81` | `sub_102f6c81` | 1 | trivial accessor/forwarder |
| `0x102f6ca2` | `sub_102f6ca2` | 1 | trivial accessor/forwarder |
| `0x102f6d20` | `sub_102f6d20` | 185 | support routine (185 bytes) |
| `0x102f6d40` | `sub_102f6d40` | 1 | trivial accessor/forwarder |
| `0x102f6d71` | `sub_102f6d71` | 1 | trivial accessor/forwarder |
| `0x102f6de0` | `sub_102f6de0` | 147 | support routine (147 bytes) |
| `0x102f6e0d` | `sub_102f6e0d` | 1 | trivial accessor/forwarder |
| `0x102f6e80` | `sub_102f6e80` | 168 | support routine (168 bytes) |
| `0x102f6ea2` | `sub_102f6ea2` | 5 | trivial accessor/forwarder |
| `0x102f6f30` | `sub_102f6f30` | 158 | support routine (158 bytes) |
| `0x102f6fd0` | `sub_102f6fd0` | 339 | support routine (339 bytes) |
| `0x102f708e` | `sub_102f708e` | 3 | trivial accessor/forwarder |
| `0x102f70ce` | `sub_102f70ce` | 3 | trivial accessor/forwarder |
| `0x102f7130` | `sub_102f7130` | 176 | support routine (176 bytes) |
| `0x102f71e0` | `sub_102f71e0` | 191 | support routine (191 bytes) |
| `0x102f7211` | `sub_102f7211` | 1 | trivial accessor/forwarder |
| `0x102f7232` | `sub_102f7232` | 1 | trivial accessor/forwarder |
| `0x102f72b0` | `sub_102f72b0` | 408 | support routine (408 bytes) |
| `0x102f739e` | `sub_102f739e` | 3 | trivial accessor/forwarder |
| `0x102f73c6` | `sub_102f73c6` | 3 | trivial accessor/forwarder |
| `0x102f73fe` | `sub_102f73fe` | 3 | trivial accessor/forwarder |
| `0x102f7460` | `sub_102f7460` | 158 | support routine (158 bytes) |
| `0x102f7500` | `sub_102f7500` | 164 | support routine (164 bytes) |
| `0x102f75b0` | `sub_102f75b0` | 157 | support routine (157 bytes) |
| `0x102f7650` | `sub_102f7650` | 225 | support routine (225 bytes) |
| `0x102f768a` | `sub_102f768a` | 3 | trivial accessor/forwarder |
| `0x102f76a5` | `sub_102f76a5` | 1 | trivial accessor/forwarder |
| `0x102f76e1` | `sub_102f76e1` | 3 | trivial accessor/forwarder |
| `0x102f76f0` | `sub_102f76f0` | 3 | trivial accessor/forwarder |
| `0x102f7701` | `sub_102f7701` | 3 | trivial accessor/forwarder |
| `0x102f7740` | `sub_102f7740` | 151 | support routine (151 bytes) |
| `0x102f77e0` | `sub_102f77e0` | 258 | support routine (258 bytes) |
| `0x102f78f0` | `sub_102f78f0` | 247 | support routine (247 bytes) |
| `0x102f79f0` | `sub_102f79f0` | 129 | support routine (129 bytes) |
| `0x102f7a80` | `sub_102f7a80` | 161 | support routine (161 bytes) |
| `0x102f7b30` | `sub_102f7b30` | 138 | support routine (138 bytes) |
| `0x102f7bc0` | `sub_102f7bc0` | 146 | support routine (146 bytes) |
| `0x102f7be4` | `sub_102f7be4` | 1 | trivial accessor/forwarder |
| `0x102f7bfd` | `sub_102f7bfd` | 1 | trivial accessor/forwarder |
| `0x102f7c60` | `sub_102f7c60` | 211 | support routine (211 bytes) |
| `0x102f7c8f` | `sub_102f7c8f` | 3 | trivial accessor/forwarder |
| `0x102f7cce` | `sub_102f7cce` | 3 | trivial accessor/forwarder |
| `0x102f7ce5` | `sub_102f7ce5` | 3 | trivial accessor/forwarder |
| `0x102f7cf4` | `sub_102f7cf4` | 3 | trivial accessor/forwarder |
| `0x102f7d40` | `sub_102f7d40` | 161 | support routine (161 bytes) |
| `0x102f7d6f` | `sub_102f7d6f` | 3 | trivial accessor/forwarder |
| `0x102f7df0` | `sub_102f7df0` | 203 | support routine (203 bytes) |
| `0x102f7ec0` | `sub_102f7ec0` | 220 | support routine (220 bytes) |
| `0x102f7fa0` | `sub_102f7fa0` | 188 | support routine (188 bytes) |
| `0x102f7fcf` | `sub_102f7fcf` | 3 | trivial accessor/forwarder |
| `0x102f7ff7` | `sub_102f7ff7` | 3 | trivial accessor/forwarder |
| `0x102f801f` | `sub_102f801f` | 3 | trivial accessor/forwarder |
| `0x102f8070` | `sub_102f8070` | 390 | support routine (390 bytes) |
| `0x102f814d` | `sub_102f814d` | 3 | trivial accessor/forwarder |
| `0x102f8164` | `sub_102f8164` | 1 | trivial accessor/forwarder |
| `0x102f8198` | `sub_102f8198` | 3 | trivial accessor/forwarder |
| `0x102f81a7` | `sub_102f81a7` | 3 | trivial accessor/forwarder |
| `0x102f8210` | `sub_102f8210` | 391 | support routine (391 bytes) |
| `0x102f8240` | `sub_102f8240` | 1 | trivial accessor/forwarder |
| `0x102f827e` | `sub_102f827e` | 1 | trivial accessor/forwarder |
| `0x102f83a0` | `sub_102f83a0` | 183 | support routine (183 bytes) |
| `0x102f8460` | `sub_102f8460` | 250 | support routine (250 bytes) |
| `0x102f8560` | `sub_102f8560` | 153 | support routine (153 bytes) |
| `0x102f858c` | `sub_102f858c` | 3 | trivial accessor/forwarder |
| `0x102f8600` | `sub_102f8600` | 248 | support routine (248 bytes) |
| `0x102f8700` | `sub_102f8700` | 125 | support routine (125 bytes) |
| `0x102f8722` | `sub_102f8722` | 5 | trivial accessor/forwarder |
| `0x102f8790` | `sub_102f8790` | 142 | support routine (142 bytes) |
| `0x102f87bd` | `sub_102f87bd` | 1 | trivial accessor/forwarder |
| `0x102f8820` | `sub_102f8820` | 165 | support routine (165 bytes) |
| `0x102f88d0` | `sub_102f88d0` | 209 | support routine (209 bytes) |
| `0x102f89b0` | `sub_102f89b0` | 167 | support routine (167 bytes) |
| `0x102f8a60` | `sub_102f8a60` | 171 | support routine (171 bytes) |
| `0x102f8a8d` | `sub_102f8a8d` | 1 | trivial accessor/forwarder |
| `0x102f8aa9` | `sub_102f8aa9` | 1 | trivial accessor/forwarder |
| `0x102f8b10` | `sub_102f8b10` | 172 | support routine (172 bytes) |
| `0x102f8b3f` | `sub_102f8b3f` | 3 | trivial accessor/forwarder |
| `0x102f8b56` | `sub_102f8b56` | 3 | trivial accessor/forwarder |
| `0x102f8bd0` | `sub_102f8bd0` | 145 | support routine (145 bytes) |
| `0x102f8c70` | `sub_102f8c70` | 337 | support routine (337 bytes) |
| `0x102f8cbc` | `sub_102f8cbc` | 2 | trivial accessor/forwarder |
| `0x102f8d36` | `sub_102f8d36` | 2 | trivial accessor/forwarder |
| `0x102f8d6f` | `sub_102f8d6f` | 3 | trivial accessor/forwarder |
| `0x102f8dd0` | `sub_102f8dd0` | 420 | support routine (420 bytes) |
| `0x102f8eca` | `sub_102f8eca` | 3 | trivial accessor/forwarder |
| `0x102f8ef2` | `sub_102f8ef2` | 3 | trivial accessor/forwarder |
| `0x102f8f2a` | `sub_102f8f2a` | 3 | trivial accessor/forwarder |
| `0x102f8f80` | `sub_102f8f80` | 134 | support routine (134 bytes) |
| `0x102f8fa5` | `sub_102f8fa5` | 5 | trivial accessor/forwarder |
| `0x102f9010` | `sub_102f9010` | 199 | support routine (199 bytes) |
| `0x102f903c` | `sub_102f903c` | 3 | trivial accessor/forwarder |
| `0x102f9053` | `sub_102f9053` | 3 | trivial accessor/forwarder |
| `0x102f9089` | `sub_102f9089` | 3 | trivial accessor/forwarder |
| `0x102f9098` | `sub_102f9098` | 3 | trivial accessor/forwarder |
| `0x102f90f0` | `sub_102f90f0` | 171 | support routine (171 bytes) |
| `0x102f91a0` | `sub_102f91a0` | 151 | support routine (151 bytes) |
| `0x102f91cc` | `sub_102f91cc` | 3 | trivial accessor/forwarder |
| `0x102f9240` | `sub_102f9240` | 184 | support routine (184 bytes) |
| `0x102f926f` | `sub_102f926f` | 1 | trivial accessor/forwarder |
| `0x102f928c` | `sub_102f928c` | 1 | trivial accessor/forwarder |
| `0x102f9300` | `sub_102f9300` | 272 | support routine (272 bytes) |
| `0x102f93cf` | `sub_102f93cf` | 3 | trivial accessor/forwarder |
| `0x102f9420` | `sub_102f9420` | 153 | support routine (153 bytes) |
| `0x102f9465` | `sub_102f9465` | 3 | trivial accessor/forwarder |
| `0x102f94c0` | `sub_102f94c0` | 150 | support routine (150 bytes) |
| `0x102f94d8` | `sub_102f94d8` | 1 | trivial accessor/forwarder |
| `0x102f94f3` | `sub_102f94f3` | 1 | trivial accessor/forwarder |
| `0x102f9515` | `sub_102f9515` | 1 | trivial accessor/forwarder |
| `0x102f9560` | `sub_102f9560` | 129 | support routine (129 bytes) |
| `0x102f9582` | `sub_102f9582` | 5 | trivial accessor/forwarder |
| `0x102f95f0` | `sub_102f95f0` | 223 | support routine (223 bytes) |
| `0x102f9685` | `sub_102f9685` | 1 | trivial accessor/forwarder |
| `0x102f96e0` | `sub_102f96e0` | 159 | support routine (159 bytes) |
| `0x102f9780` | `sub_102f9780` | 160 | support routine (160 bytes) |
| `0x102f9820` | `sub_102f9820` | 228 | support routine (228 bytes) |
| `0x102f9840` | `sub_102f9840` | 1 | trivial accessor/forwarder |
| `0x102f9910` | `sub_102f9910` | 135 | support routine (135 bytes) |
| `0x102f992f` | `sub_102f992f` | 1 | trivial accessor/forwarder |
| `0x102f993b` | `sub_102f993b` | 1 | trivial accessor/forwarder |
| `0x102f9948` | `sub_102f9948` | 1 | trivial accessor/forwarder |
| `0x102f99a0` | `sub_102f99a0` | 143 | support routine (143 bytes) |
| `0x102f9a30` | `sub_102f9a30` | 162 | support routine (162 bytes) |
| `0x102f9a5d` | `sub_102f9a5d` | 1 | trivial accessor/forwarder |
| `0x102f9a7c` | `sub_102f9a7c` | 1 | trivial accessor/forwarder |
| `0x102f9a99` | `sub_102f9a99` | 1 | trivial accessor/forwarder |
| `0x102f9ae0` | `sub_102f9ae0` | 150 | support routine (150 bytes) |
| `0x102f9b80` | `sub_102f9b80` | 145 | support routine (145 bytes) |
| `0x102f9c20` | `sub_102f9c20` | 156 | support routine (156 bytes) |
| `0x102f9cc0` | `sub_102f9cc0` | 218 | support routine (218 bytes) |
| `0x102f9ce2` | `sub_102f9ce2` | 5 | trivial accessor/forwarder |
| `0x102f9db0` | `sub_102f9db0` | 256 | support routine (256 bytes) |
| `0x102f9eb0` | `sub_102f9eb0` | 343 | support routine (343 bytes) |
| `0x102f9f8f` | `sub_102f9f8f` | 3 | trivial accessor/forwarder |
| `0x102fa010` | `sub_102fa010` | 121 | support routine (121 bytes) |
| `0x102fa090` | `sub_102fa090` | 372 | support routine (372 bytes) |
| `0x102fa0b0` | `sub_102fa0b0` | 1 | trivial accessor/forwarder |
| `0x102fa14d` | `sub_102fa14d` | 5 | trivial accessor/forwarder |
| `0x102fa190` | `sub_102fa190` | 3 | trivial accessor/forwarder |
| `0x102fa210` | `sub_102fa210` | 205 | support routine (205 bytes) |
| `0x102fa2e0` | `sub_102fa2e0` | 198 | support routine (198 bytes) |
| `0x102fa343` | `sub_102fa343` | 1 | trivial accessor/forwarder |
| `0x102fa3b0` | `sub_102fa3b0` | 165 | support routine (165 bytes) |
| `0x102fa460` | `sub_102fa460` | 235 | support routine (235 bytes) |
| `0x102fa550` | `sub_102fa550` | 187 | support routine (187 bytes) |
| `0x102fa57f` | `sub_102fa57f` | 1 | trivial accessor/forwarder |
| `0x102fa5a3` | `sub_102fa5a3` | 1 | trivial accessor/forwarder |
| `0x102fa610` | `sub_102fa610` | 230 | support routine (230 bytes) |
| `0x102fa700` | `sub_102fa700` | 229 | support routine (229 bytes) |
| `0x102fa731` | `sub_102fa731` | 1 | trivial accessor/forwarder |
| `0x102fa752` | `sub_102fa752` | 1 | trivial accessor/forwarder |
| `0x102fa793` | `sub_102fa793` | 3 | trivial accessor/forwarder |
| `0x102fa7a2` | `sub_102fa7a2` | 3 | trivial accessor/forwarder |
| `0x102fa7b3` | `sub_102fa7b3` | 3 | trivial accessor/forwarder |
| `0x102fa7f0` | `sub_102fa7f0` | 168 | support routine (168 bytes) |
| `0x102fa81f` | `sub_102fa81f` | 3 | trivial accessor/forwarder |
| `0x102fa8a0` | `sub_102fa8a0` | 274 | support routine (274 bytes) |
| `0x102fa971` | `sub_102fa971` | 3 | trivial accessor/forwarder |
| `0x102fa9c0` | `sub_102fa9c0` | 186 | support routine (186 bytes) |
| `0x102fa9e0` | `sub_102fa9e0` | 1 | trivial accessor/forwarder |
| `0x102faa11` | `sub_102faa11` | 1 | trivial accessor/forwarder |
| `0x102faa80` | `sub_102faa80` | 168 | support routine (168 bytes) |
| `0x102fab30` | `sub_102fab30` | 209 | support routine (209 bytes) |
| `0x102fabb7` | `sub_102fabb7` | 1 | trivial accessor/forwarder |
| `0x102fac10` | `sub_102fac10` | 193 | support routine (193 bytes) |
| `0x102fac7d` | `sub_102fac7d` | 3 | trivial accessor/forwarder |
| `0x102fac8c` | `sub_102fac8c` | 3 | trivial accessor/forwarder |
| `0x102face0` | `sub_102face0` | 134 | support routine (134 bytes) |
| `0x102fad02` | `sub_102fad02` | 5 | trivial accessor/forwarder |
| `0x102fad70` | `sub_102fad70` | 200 | support routine (200 bytes) |
| `0x102fad9c` | `sub_102fad9c` | 3 | trivial accessor/forwarder |
| `0x102fadb6` | `sub_102fadb6` | 3 | trivial accessor/forwarder |
| `0x102fadea` | `sub_102fadea` | 3 | trivial accessor/forwarder |
| `0x102fadf9` | `sub_102fadf9` | 3 | trivial accessor/forwarder |
| `0x102fae50` | `sub_102fae50` | 213 | support routine (213 bytes) |
| `0x102faf30` | `sub_102faf30` | 220 | support routine (220 bytes) |
| `0x102faf50` | `sub_102faf50` | 1 | trivial accessor/forwarder |
| `0x102fb010` | `sub_102fb010` | 158 | support routine (158 bytes) |
| `0x102fb0b0` | `sub_102fb0b0` | 382 | support routine (382 bytes) |
| `0x102fb185` | `sub_102fb185` | 3 | trivial accessor/forwarder |
| `0x102fb19c` | `sub_102fb19c` | 1 | trivial accessor/forwarder |
| `0x102fb1d0` | `sub_102fb1d0` | 3 | trivial accessor/forwarder |
| `0x102fb1df` | `sub_102fb1df` | 3 | trivial accessor/forwarder |
| `0x102fb240` | `sub_102fb240` | 125 | support routine (125 bytes) |
| `0x102fb2c0` | `sub_102fb2c0` | 390 | support routine (390 bytes) |
| `0x102fb378` | `sub_102fb378` | 5 | trivial accessor/forwarder |
| `0x102fb3bb` | `sub_102fb3bb` | 3 | trivial accessor/forwarder |
| `0x102fb3ff` | `sub_102fb3ff` | 3 | trivial accessor/forwarder |
| `0x102fb40e` | `sub_102fb40e` | 3 | trivial accessor/forwarder |
| `0x102fb460` | `sub_102fb460` | 197 | support routine (197 bytes) |
| `0x102fb530` | `sub_102fb530` | 199 | support routine (199 bytes) |
| `0x102fb600` | `sub_102fb600` | 125 | support routine (125 bytes) |
| `0x102fb622` | `sub_102fb622` | 5 | trivial accessor/forwarder |
| `0x102fb690` | `sub_102fb690` | 160 | support routine (160 bytes) |
| `0x102fb730` | `sub_102fb730` | 125 | support routine (125 bytes) |
| `0x102fb752` | `sub_102fb752` | 5 | trivial accessor/forwarder |
| `0x102fb7c0` | `sub_102fb7c0` | 140 | support routine (140 bytes) |
| `0x102fb850` | `sub_102fb850` | 133 | support routine (133 bytes) |
| `0x102fb8e0` | `sub_102fb8e0` | 154 | support routine (154 bytes) |
| `0x102fb919` | `sub_102fb919` | 3 | trivial accessor/forwarder |
| `0x102fb929` | `sub_102fb929` | 3 | trivial accessor/forwarder |
| `0x102fb980` | `sub_102fb980` | 381 | support routine (381 bytes) |
| `0x102fb9e3` | `sub_102fb9e3` | 1 | trivial accessor/forwarder |
| `0x102fbb00` | `sub_102fbb00` | 124 | support routine (124 bytes) |
| `0x102fbb22` | `sub_102fbb22` | 5 | trivial accessor/forwarder |
| `0x102fbb90` | `sub_102fbb90` | 257 | support routine (257 bytes) |
| `0x102fbca0` | `sub_102fbca0` | 156 | support routine (156 bytes) |
| `0x102fbd40` | `sub_102fbd40` | 165 | support routine (165 bytes) |
| `0x102fbdf0` | `sub_102fbdf0` | 440 | support routine (440 bytes) |
| `0x102fbfb0` | `sub_102fbfb0` | 256 | support routine (256 bytes) |
| `0x102fc0c0` | `sub_102fc0c0` | 179 | support routine (179 bytes) |
| `0x102fc0ec` | `sub_102fc0ec` | 1 | trivial accessor/forwarder |
| `0x102fc130` | `sub_102fc130` | 1 | trivial accessor/forwarder |
| `0x102fc180` | `sub_102fc180` | 141 | support routine (141 bytes) |
| `0x102fc210` | `sub_102fc210` | 159 | support routine (159 bytes) |
| `0x102fc2b0` | `sub_102fc2b0` | 480 | support routine (480 bytes) |
| `0x102fc2d0` | `sub_102fc2d0` | 1 | trivial accessor/forwarder |
| `0x102fc36d` | `sub_102fc36d` | 1 | trivial accessor/forwarder |
| `0x102fc39e` | `sub_102fc39e` | 1 | trivial accessor/forwarder |
| `0x102fc3eb` | `sub_102fc3eb` | 3 | trivial accessor/forwarder |
| `0x102fc402` | `sub_102fc402` | 1 | trivial accessor/forwarder |
| `0x102fc436` | `sub_102fc436` | 3 | trivial accessor/forwarder |
| `0x102fc445` | `sub_102fc445` | 3 | trivial accessor/forwarder |
| `0x102fc456` | `sub_102fc456` | 3 | trivial accessor/forwarder |
| `0x102fc4b0` | `sub_102fc4b0` | 228 | support routine (228 bytes) |
| `0x102fc5a0` | `sub_102fc5a0` | 185 | support routine (185 bytes) |
| `0x102fc660` | `sub_102fc660` | 162 | support routine (162 bytes) |
| `0x102fc68c` | `sub_102fc68c` | 3 | trivial accessor/forwarder |
| `0x102fc6a3` | `sub_102fc6a3` | 1 | trivial accessor/forwarder |
| `0x102fc710` | `sub_102fc710` | 166 | support routine (166 bytes) |
| `0x102fc7c0` | `sub_102fc7c0` | 182 | support routine (182 bytes) |
| `0x102fc7d3` | `sub_102fc7d3` | 1 | trivial accessor/forwarder |
| `0x102fc7f1` | `sub_102fc7f1` | 1 | trivial accessor/forwarder |
| `0x102fc80a` | `sub_102fc80a` | 1 | trivial accessor/forwarder |
| `0x102fc826` | `sub_102fc826` | 1 | trivial accessor/forwarder |
| `0x102fc880` | `sub_102fc880` | 161 | support routine (161 bytes) |
| `0x102fc930` | `sub_102fc930` | 197 | support routine (197 bytes) |
| `0x102fc950` | `sub_102fc950` | 1 | trivial accessor/forwarder |
| `0x102fc985` | `sub_102fc985` | 1 | trivial accessor/forwarder |
| `0x102fc9b2` | `sub_102fc9b2` | 1 | trivial accessor/forwarder |
| `0x102fca00` | `sub_102fca00` | 144 | support routine (144 bytes) |
| `0x102fca18` | `sub_102fca18` | 1 | trivial accessor/forwarder |
| `0x102fca4e` | `sub_102fca4e` | 1 | trivial accessor/forwarder |
| `0x102fcaa0` | `sub_102fcaa0` | 193 | support routine (193 bytes) |
| `0x102fcb0d` | `sub_102fcb0d` | 3 | trivial accessor/forwarder |
| `0x102fcb1c` | `sub_102fcb1c` | 3 | trivial accessor/forwarder |
| `0x102fcb70` | `sub_102fcb70` | 144 | support routine (144 bytes) |
| `0x102fcc00` | `sub_102fcc00` | 207 | support routine (207 bytes) |
| `0x102fcc5a` | `sub_102fcc5a` | 3 | trivial accessor/forwarder |
| `0x102fcce0` | `sub_102fcce0` | 213 | support routine (213 bytes) |
| `0x102fcdc0` | `sub_102fcdc0` | 226 | support routine (226 bytes) |
| `0x102fceb0` | `sub_102fceb0` | 204 | support routine (204 bytes) |
| `0x102fcf11` | `sub_102fcf11` | 1 | trivial accessor/forwarder |
| `0x102fcf80` | `sub_102fcf80` | 178 | support routine (178 bytes) |
| `0x102fcfc8` | `sub_102fcfc8` | 3 | trivial accessor/forwarder |
| `0x102fcff2` | `sub_102fcff2` | 3 | trivial accessor/forwarder |
| `0x102fd040` | `sub_102fd040` | 176 | support routine (176 bytes) |
| `0x102fd0f0` | `sub_102fd0f0` | 381 | support routine (381 bytes) |
| `0x102fd153` | `sub_102fd153` | 1 | trivial accessor/forwarder |
| `0x102fd270` | `sub_102fd270` | 173 | support routine (173 bytes) |
| `0x102fd320` | `sub_102fd320` | 144 | support routine (144 bytes) |
| `0x102fd33f` | `sub_102fd33f` | 1 | trivial accessor/forwarder |
| `0x102fd361` | `sub_102fd361` | 1 | trivial accessor/forwarder |
| `0x102fd3c0` | `sub_102fd3c0` | 200 | support routine (200 bytes) |
| `0x102fd41e` | `sub_102fd41e` | 1 | trivial accessor/forwarder |
| `0x102fd445` | `sub_102fd445` | 1 | trivial accessor/forwarder |
| `0x102fd452` | `sub_102fd452` | 1 | trivial accessor/forwarder |
| `0x102fd490` | `sub_102fd490` | 173 | support routine (173 bytes) |
| `0x102fd540` | `sub_102fd540` | 370 | support routine (370 bytes) |
| `0x102fd613` | `sub_102fd613` | 3 | trivial accessor/forwarder |
| `0x102fd638` | `sub_102fd638` | 3 | trivial accessor/forwarder |
| `0x102fd660` | `sub_102fd660` | 3 | trivial accessor/forwarder |
| `0x102fd6c0` | `sub_102fd6c0` | 166 | support routine (166 bytes) |
| `0x102fd770` | `sub_102fd770` | 132 | support routine (132 bytes) |
| `0x102fd782` | `sub_102fd782` | 1 | trivial accessor/forwarder |
| `0x102fd800` | `sub_102fd800` | 136 | support routine (136 bytes) |
| `0x102fd890` | `sub_102fd890` | 235 | support routine (235 bytes) |
| `0x102fd8b2` | `sub_102fd8b2` | 1 | trivial accessor/forwarder |
| `0x102fd980` | `sub_102fd980` | 206 | support routine (206 bytes) |
| `0x102fda50` | `sub_102fda50` | 390 | support routine (390 bytes) |
| `0x102fdb2d` | `sub_102fdb2d` | 3 | trivial accessor/forwarder |
| `0x102fdb44` | `sub_102fdb44` | 1 | trivial accessor/forwarder |
| `0x102fdb78` | `sub_102fdb78` | 3 | trivial accessor/forwarder |
| `0x102fdb87` | `sub_102fdb87` | 3 | trivial accessor/forwarder |
| `0x102fdbf0` | `sub_102fdbf0` | 191 | support routine (191 bytes) |
| `0x102fdcb0` | `sub_102fdcb0` | 197 | support routine (197 bytes) |
| `0x102fdd80` | `sub_102fdd80` | 131 | support routine (131 bytes) |
| `0x102fde10` | `sub_102fde10` | 126 | support routine (126 bytes) |
| `0x102fde90` | `sub_102fde90` | 180 | support routine (180 bytes) |
| `0x102fdebf` | `sub_102fdebf` | 3 | trivial accessor/forwarder |
| `0x102fdf05` | `sub_102fdf05` | 3 | trivial accessor/forwarder |
| `0x102fdf50` | `sub_102fdf50` | 223 | support routine (223 bytes) |
| `0x102fdf8e` | `sub_102fdf8e` | 3 | trivial accessor/forwarder |
| `0x102fdfa9` | `sub_102fdfa9` | 1 | trivial accessor/forwarder |
| `0x102fdfdf` | `sub_102fdfdf` | 3 | trivial accessor/forwarder |
| `0x102fdfee` | `sub_102fdfee` | 3 | trivial accessor/forwarder |
| `0x102fdfff` | `sub_102fdfff` | 3 | trivial accessor/forwarder |
| `0x102fe040` | `sub_102fe040` | 200 | support routine (200 bytes) |
| `0x102fe06d` | `sub_102fe06d` | 1 | trivial accessor/forwarder |
| `0x102fe08e` | `sub_102fe08e` | 1 | trivial accessor/forwarder |
| `0x102fe0ab` | `sub_102fe0ab` | 1 | trivial accessor/forwarder |
| `0x102fe110` | `sub_102fe110` | 120 | support routine (120 bytes) |
| `0x102fe12f` | `sub_102fe12f` | 1 | trivial accessor/forwarder |
| `0x102fe13d` | `sub_102fe13d` | 1 | trivial accessor/forwarder |
| `0x102fe190` | `sub_102fe190` | 249 | support routine (249 bytes) |
| `0x102fe290` | `sub_102fe290` | 142 | support routine (142 bytes) |
| `0x102fe2b2` | `sub_102fe2b2` | 5 | trivial accessor/forwarder |
| `0x102fe330` | `sub_102fe330` | 144 | support routine (144 bytes) |
| `0x102fe352` | `sub_102fe352` | 5 | trivial accessor/forwarder |
| `0x102fe369` | `sub_102fe369` | 1 | trivial accessor/forwarder |
| `0x102fe385` | `sub_102fe385` | 1 | trivial accessor/forwarder |
| `0x102fe3d0` | `sub_102fe3d0` | 145 | support routine (145 bytes) |
| `0x102fe470` | `obfuscatedFlagChainCompute` | 528 | Heavily-obfuscated (VM-lifted _ccall/_INSERT) routine combining sub_102f1910/ef020 results and globals g_1038c7dc/e0, returning via sub_102eef00. |
| `0x102fe4af` | `sub_102fe4af` | 1 | trivial accessor/forwarder |
| `0x102fe4f5` | `sub_102fe4f5` | 1 | trivial accessor/forwarder |
| `0x102fe508` | `sub_102fe508` | 72 | support routine (72 bytes) |
| `0x102fe550` | `sub_102fe550` | 5 | trivial accessor/forwarder |
| `0x102fe593` | `sub_102fe593` | 1 | trivial accessor/forwarder |
| `0x102fe6e0` | `sub_102fe6e0` | 173 | support routine (173 bytes) |
| `0x102fe790` | `sub_102fe790` | 157 | support routine (157 bytes) |
| `0x102fe830` | `sub_102fe830` | 165 | support routine (165 bytes) |
| `0x102fe8e0` | `sub_102fe8e0` | 161 | support routine (161 bytes) |
| `0x102fe990` | `sub_102fe990` | 154 | support routine (154 bytes) |
| `0x102fe9bc` | `sub_102fe9bc` | 3 | trivial accessor/forwarder |
| `0x102fea30` | `sub_102fea30` | 156 | support routine (156 bytes) |
| `0x102fead0` | `sub_102fead0` | 240 | support routine (240 bytes) |
| `0x102febc0` | `sub_102febc0` | 189 | support routine (189 bytes) |
| `0x102febe4` | `sub_102febe4` | 5 | trivial accessor/forwarder |
| `0x102fec90` | `sub_102fec90` | 168 | support routine (168 bytes) |
| `0x102fed40` | `sub_102fed40` | 217 | support routine (217 bytes) |
| `0x102fed62` | `sub_102fed62` | 5 | trivial accessor/forwarder |
| `0x102fee30` | `sub_102fee30` | 233 | support routine (233 bytes) |
| `0x102fef20` | `sub_102fef20` | 176 | support routine (176 bytes) |
| `0x102fef4f` | `sub_102fef4f` | 3 | trivial accessor/forwarder |
| `0x102fef67` | `sub_102fef67` | 1 | trivial accessor/forwarder |
| `0x102fefe0` | `sub_102fefe0` | 204 | support routine (204 bytes) |
| `0x102ff0b0` | `sub_102ff0b0` | 206 | support routine (206 bytes) |
| `0x102ff110` | `sub_102ff110` | 1 | trivial accessor/forwarder |
| `0x102ff13b` | `sub_102ff13b` | 1 | trivial accessor/forwarder |
| `0x102ff180` | `sub_102ff180` | 143 | support routine (143 bytes) |
| `0x102ff210` | `sub_102ff210` | 206 | support routine (206 bytes) |
| `0x102ff273` | `sub_102ff273` | 1 | trivial accessor/forwarder |
| `0x102ff2e0` | `sub_102ff2e0` | 154 | support routine (154 bytes) |
| `0x102ff313` | `sub_102ff313` | 1 | trivial accessor/forwarder |
| `0x102ff32f` | `sub_102ff32f` | 1 | trivial accessor/forwarder |
| `0x102ff380` | `sub_102ff380` | 343 | support routine (343 bytes) |
| `0x102ff45f` | `sub_102ff45f` | 3 | trivial accessor/forwarder |
| `0x102ff4e0` | `sub_102ff4e0` | 196 | support routine (196 bytes) |
| `0x102ff5b0` | `sub_102ff5b0` | 157 | support routine (157 bytes) |
| `0x102ff650` | `sub_102ff650` | 207 | support routine (207 bytes) |
| `0x102ff6aa` | `sub_102ff6aa` | 3 | trivial accessor/forwarder |
| `0x102ff730` | `sub_102ff730` | 179 | support routine (179 bytes) |
| `0x102ff7f0` | `sub_102ff7f0` | 134 | support routine (134 bytes) |
| `0x102ff814` | `sub_102ff814` | 1 | trivial accessor/forwarder |
| `0x102ff880` | `sub_102ff880` | 397 | support routine (397 bytes) |
| `0x102ff911` | `sub_102ff911` | 3 | trivial accessor/forwarder |
| `0x102ff920` | `sub_102ff920` | 3 | trivial accessor/forwarder |
| `0x102ff932` | `sub_102ff932` | 3 | trivial accessor/forwarder |
| `0x102ff96d` | `sub_102ff96d` | 3 | trivial accessor/forwarder |
| `0x102ff9a0` | `sub_102ff9a0` | 3 | trivial accessor/forwarder |
| `0x102ff9b0` | `sub_102ff9b0` | 3 | trivial accessor/forwarder |
| `0x102ff9c7` | `sub_102ff9c7` | 3 | trivial accessor/forwarder |
| `0x102ffa30` | `sub_102ffa30` | 266 | support routine (266 bytes) |
| `0x102ffb40` | `sub_102ffb40` | 165 | support routine (165 bytes) |
| `0x102ffb6f` | `sub_102ffb6f` | 3 | trivial accessor/forwarder |
| `0x102ffbf0` | `sub_102ffbf0` | 178 | support routine (178 bytes) |
| `0x102ffcb0` | `sub_102ffcb0` | 225 | support routine (225 bytes) |
| `0x102ffcd0` | `sub_102ffcd0` | 1 | trivial accessor/forwarder |
| `0x102ffda0` | `sub_102ffda0` | 209 | support routine (209 bytes) |
| `0x102ffe03` | `sub_102ffe03` | 1 | trivial accessor/forwarder |
| `0x102ffe80` | `sub_102ffe80` | 132 | support routine (132 bytes) |
| `0x102ffea2` | `sub_102ffea2` | 5 | trivial accessor/forwarder |
| `0x102fff10` | `sub_102fff10` | 150 | support routine (150 bytes) |
| `0x102fff3c` | `sub_102fff3c` | 3 | trivial accessor/forwarder |
| `0x102fffb0` | `sub_102fffb0` | 171 | support routine (171 bytes) |
| `0x102fffdb` | `sub_102fffdb` | 3 | trivial accessor/forwarder |
| `0x102fffed` | `sub_102fffed` | 3 | trivial accessor/forwarder |
| `0x1030000d` | `sub_1030000d` | 3 | trivial accessor/forwarder |
| `0x10300070` | `sub_10300070` | 191 | support routine (191 bytes) |
| `0x10300090` | `sub_10300090` | 1 | trivial accessor/forwarder |
| `0x103000b6` | `sub_103000b6` | 1 | trivial accessor/forwarder |
| `0x103000ed` | `sub_103000ed` | 1 | trivial accessor/forwarder |
| `0x10300140` | `sub_10300140` | 165 | support routine (165 bytes) |
| `0x103001f0` | `sub_103001f0` | 136 | support routine (136 bytes) |
| `0x1030020c` | `sub_1030020c` | 1 | trivial accessor/forwarder |
| `0x10300236` | `sub_10300236` | 1 | trivial accessor/forwarder |
| `0x10300280` | `sub_10300280` | 257 | support routine (257 bytes) |
| `0x10300390` | `sub_10300390` | 257 | support routine (257 bytes) |
| `0x103004a0` | `sub_103004a0` | 256 | support routine (256 bytes) |
| `0x103005a0` | `sub_103005a0` | 256 | support routine (256 bytes) |
| `0x103006a0` | `sub_103006a0` | 257 | support routine (257 bytes) |
| `0x103007b0` | `sub_103007b0` | 257 | support routine (257 bytes) |
| `0x103008c0` | `sub_103008c0` | 257 | support routine (257 bytes) |
| `0x103009d0` | `sub_103009d0` | 257 | support routine (257 bytes) |
| `0x10300ae0` | `sub_10300ae0` | 257 | support routine (257 bytes) |
| `0x10300bf0` | `sub_10300bf0` | 257 | support routine (257 bytes) |
| `0x10300d00` | `sub_10300d00` | 257 | support routine (257 bytes) |
| `0x10300e10` | `sub_10300e10` | 257 | support routine (257 bytes) |
| `0x10300f20` | `sub_10300f20` | 257 | support routine (257 bytes) |
| `0x10301030` | `sub_10301030` | 257 | support routine (257 bytes) |
| `0x10301140` | `sub_10301140` | 257 | support routine (257 bytes) |
| `0x10301250` | `sub_10301250` | 257 | support routine (257 bytes) |
| `0x10301360` | `sub_10301360` | 257 | support routine (257 bytes) |
| `0x10301470` | `sub_10301470` | 257 | support routine (257 bytes) |
| `0x10301580` | `sub_10301580` | 257 | support routine (257 bytes) |
| `0x10301690` | `sub_10301690` | 257 | support routine (257 bytes) |
| `0x103017a0` | `sub_103017a0` | 257 | support routine (257 bytes) |
| `0x103018b0` | `sub_103018b0` | 257 | support routine (257 bytes) |
| `0x103019c0` | `sub_103019c0` | 257 | support routine (257 bytes) |
| `0x10301ad0` | `sub_10301ad0` | 257 | support routine (257 bytes) |
| `0x10301be0` | `sub_10301be0` | 257 | support routine (257 bytes) |
| `0x10301cf0` | `sub_10301cf0` | 257 | support routine (257 bytes) |
| `0x10301e00` | `sub_10301e00` | 254 | support routine (254 bytes) |
| `0x10301f00` | `sub_10301f00` | 257 | support routine (257 bytes) |
| `0x10302010` | `sub_10302010` | 256 | support routine (256 bytes) |
| `0x10302110` | `sub_10302110` | 257 | support routine (257 bytes) |
| `0x10302220` | `sub_10302220` | 257 | support routine (257 bytes) |
| `0x10302330` | `sub_10302330` | 257 | support routine (257 bytes) |
| `0x10302440` | `sub_10302440` | 257 | support routine (257 bytes) |
| `0x10302550` | `sub_10302550` | 257 | support routine (257 bytes) |
| `0x10302660` | `sub_10302660` | 257 | support routine (257 bytes) |
| `0x10302770` | `sub_10302770` | 257 | support routine (257 bytes) |
| `0x10302880` | `sub_10302880` | 257 | support routine (257 bytes) |
| `0x10302990` | `sub_10302990` | 257 | support routine (257 bytes) |
| `0x10302aa0` | `sub_10302aa0` | 257 | support routine (257 bytes) |
| `0x10302bb0` | `sub_10302bb0` | 257 | support routine (257 bytes) |
| `0x10302cc0` | `sub_10302cc0` | 257 | support routine (257 bytes) |
| `0x10302dd0` | `sub_10302dd0` | 257 | support routine (257 bytes) |
| `0x10302ee0` | `sub_10302ee0` | 257 | support routine (257 bytes) |
| `0x10302ff0` | `sub_10302ff0` | 257 | support routine (257 bytes) |
| `0x10303100` | `sub_10303100` | 257 | support routine (257 bytes) |
| `0x10303210` | `sub_10303210` | 257 | support routine (257 bytes) |
| `0x10303320` | `sub_10303320` | 257 | support routine (257 bytes) |
| `0x10303430` | `sub_10303430` | 257 | support routine (257 bytes) |
| `0x10303540` | `sub_10303540` | 257 | support routine (257 bytes) |
| `0x10303650` | `sub_10303650` | 257 | support routine (257 bytes) |
| `0x10303760` | `sub_10303760` | 257 | support routine (257 bytes) |
| `0x10303870` | `sub_10303870` | 257 | support routine (257 bytes) |
| `0x10303980` | `sub_10303980` | 257 | support routine (257 bytes) |
| `0x10303a90` | `sub_10303a90` | 257 | support routine (257 bytes) |
| `0x10303ba0` | `sub_10303ba0` | 257 | support routine (257 bytes) |
| `0x10303cb0` | `sub_10303cb0` | 257 | support routine (257 bytes) |
| `0x10303dc0` | `sub_10303dc0` | 257 | support routine (257 bytes) |
| `0x10303ed0` | `sub_10303ed0` | 257 | support routine (257 bytes) |
| `0x10303fe0` | `sub_10303fe0` | 257 | support routine (257 bytes) |
| `0x103040f0` | `sub_103040f0` | 257 | support routine (257 bytes) |
| `0x10304200` | `sub_10304200` | 257 | support routine (257 bytes) |
| `0x10304310` | `sub_10304310` | 257 | support routine (257 bytes) |
| `0x10304420` | `sub_10304420` | 257 | support routine (257 bytes) |
| `0x10304530` | `sub_10304530` | 254 | support routine (254 bytes) |
| `0x10304630` | `sub_10304630` | 257 | support routine (257 bytes) |
| `0x10304740` | `sub_10304740` | 257 | support routine (257 bytes) |
| `0x10304850` | `sub_10304850` | 257 | support routine (257 bytes) |
| `0x10304960` | `sub_10304960` | 257 | support routine (257 bytes) |
| `0x10304a70` | `sub_10304a70` | 257 | support routine (257 bytes) |
| `0x10304b80` | `sub_10304b80` | 257 | support routine (257 bytes) |
| `0x10304c90` | `sub_10304c90` | 257 | support routine (257 bytes) |
| `0x10304da0` | `sub_10304da0` | 254 | support routine (254 bytes) |
| `0x10304ea0` | `sub_10304ea0` | 257 | support routine (257 bytes) |
| `0x10304fb0` | `sub_10304fb0` | 257 | support routine (257 bytes) |
| `0x103050c0` | `sub_103050c0` | 257 | support routine (257 bytes) |
| `0x103051d0` | `sub_103051d0` | 257 | support routine (257 bytes) |
| `0x103052e0` | `sub_103052e0` | 257 | support routine (257 bytes) |
| `0x103053f0` | `sub_103053f0` | 254 | support routine (254 bytes) |
| `0x103054f0` | `sub_103054f0` | 257 | support routine (257 bytes) |
| `0x10305600` | `sub_10305600` | 257 | support routine (257 bytes) |
| `0x10305710` | `sub_10305710` | 257 | support routine (257 bytes) |
| `0x10305820` | `sub_10305820` | 256 | support routine (256 bytes) |
| `0x10305920` | `sub_10305920` | 257 | support routine (257 bytes) |
| `0x10305a30` | `sub_10305a30` | 257 | support routine (257 bytes) |
| `0x10305b40` | `sub_10305b40` | 257 | support routine (257 bytes) |
| `0x10305c50` | `sub_10305c50` | 257 | support routine (257 bytes) |
| `0x10305d60` | `sub_10305d60` | 257 | support routine (257 bytes) |
| `0x10305e70` | `sub_10305e70` | 257 | support routine (257 bytes) |
| `0x10305f80` | `sub_10305f80` | 257 | support routine (257 bytes) |
| `0x10306090` | `sub_10306090` | 257 | support routine (257 bytes) |
| `0x103061a0` | `sub_103061a0` | 257 | support routine (257 bytes) |
| `0x103062b0` | `sub_103062b0` | 254 | support routine (254 bytes) |
| `0x103063b0` | `sub_103063b0` | 254 | support routine (254 bytes) |
| `0x103064b0` | `sub_103064b0` | 256 | support routine (256 bytes) |
| `0x103065b0` | `sub_103065b0` | 257 | support routine (257 bytes) |
| `0x103066c0` | `sub_103066c0` | 257 | support routine (257 bytes) |
| `0x103067d0` | `sub_103067d0` | 257 | support routine (257 bytes) |
| `0x103068e0` | `sub_103068e0` | 257 | support routine (257 bytes) |
| `0x103069f0` | `sub_103069f0` | 257 | support routine (257 bytes) |
| `0x10306b00` | `sub_10306b00` | 257 | support routine (257 bytes) |
| `0x10306c10` | `sub_10306c10` | 257 | support routine (257 bytes) |
| `0x10306d20` | `sub_10306d20` | 256 | support routine (256 bytes) |
| `0x10306e20` | `sub_10306e20` | 257 | support routine (257 bytes) |
| `0x10306f30` | `sub_10306f30` | 257 | support routine (257 bytes) |
| `0x10307040` | `sub_10307040` | 257 | support routine (257 bytes) |
| `0x10307150` | `sub_10307150` | 257 | support routine (257 bytes) |
| `0x10307260` | `sub_10307260` | 257 | support routine (257 bytes) |
| `0x10307370` | `sub_10307370` | 257 | support routine (257 bytes) |
| `0x10307480` | `sub_10307480` | 257 | support routine (257 bytes) |
| `0x10307590` | `sub_10307590` | 257 | support routine (257 bytes) |
| `0x103076a0` | `sub_103076a0` | 257 | support routine (257 bytes) |
| `0x103077b0` | `sub_103077b0` | 257 | support routine (257 bytes) |
| `0x103078c0` | `sub_103078c0` | 257 | support routine (257 bytes) |
| `0x103079d0` | `sub_103079d0` | 257 | support routine (257 bytes) |
| `0x10307ae0` | `sub_10307ae0` | 257 | support routine (257 bytes) |
| `0x10307bf0` | `sub_10307bf0` | 257 | support routine (257 bytes) |
| `0x10307d00` | `sub_10307d00` | 257 | support routine (257 bytes) |
| `0x10307e10` | `sub_10307e10` | 257 | support routine (257 bytes) |
| `0x10307f20` | `sub_10307f20` | 257 | support routine (257 bytes) |
| `0x10308030` | `sub_10308030` | 257 | support routine (257 bytes) |
| `0x10308140` | `sub_10308140` | 257 | support routine (257 bytes) |
| `0x10308250` | `sub_10308250` | 257 | support routine (257 bytes) |
| `0x10308360` | `sub_10308360` | 257 | support routine (257 bytes) |
| `0x10308470` | `sub_10308470` | 257 | support routine (257 bytes) |
| `0x10308580` | `sub_10308580` | 257 | support routine (257 bytes) |
| `0x10308690` | `sub_10308690` | 257 | support routine (257 bytes) |
| `0x103087a0` | `sub_103087a0` | 257 | support routine (257 bytes) |
| `0x103088b0` | `sub_103088b0` | 257 | support routine (257 bytes) |
| `0x103089c0` | `sub_103089c0` | 257 | support routine (257 bytes) |
| `0x10308ad0` | `sub_10308ad0` | 257 | support routine (257 bytes) |
| `0x10308be0` | `sub_10308be0` | 257 | support routine (257 bytes) |
| `0x10308cf0` | `sub_10308cf0` | 254 | support routine (254 bytes) |
| `0x10308df0` | `sub_10308df0` | 257 | support routine (257 bytes) |
| `0x10308f00` | `sub_10308f00` | 257 | support routine (257 bytes) |
| `0x10309010` | `sub_10309010` | 257 | support routine (257 bytes) |
| `0x10309120` | `sub_10309120` | 257 | support routine (257 bytes) |
| `0x10309230` | `sub_10309230` | 257 | support routine (257 bytes) |
| `0x10309340` | `sub_10309340` | 254 | support routine (254 bytes) |
| `0x10309440` | `sub_10309440` | 257 | support routine (257 bytes) |
| `0x10309550` | `sub_10309550` | 257 | support routine (257 bytes) |
| `0x10309660` | `sub_10309660` | 257 | support routine (257 bytes) |
| `0x10309770` | `sub_10309770` | 257 | support routine (257 bytes) |
| `0x10309880` | `sub_10309880` | 257 | support routine (257 bytes) |
| `0x10309990` | `sub_10309990` | 257 | support routine (257 bytes) |
| `0x10309aa0` | `sub_10309aa0` | 257 | support routine (257 bytes) |
| `0x10309bb0` | `sub_10309bb0` | 257 | support routine (257 bytes) |
| `0x10309cc0` | `sub_10309cc0` | 257 | support routine (257 bytes) |
| `0x10309dd0` | `sub_10309dd0` | 257 | support routine (257 bytes) |
| `0x10309ee0` | `sub_10309ee0` | 257 | support routine (257 bytes) |
| `0x10309ff0` | `sub_10309ff0` | 257 | support routine (257 bytes) |
| `0x1030a100` | `sub_1030a100` | 257 | support routine (257 bytes) |
| `0x1030a210` | `sub_1030a210` | 257 | support routine (257 bytes) |
| `0x1030a320` | `sub_1030a320` | 257 | support routine (257 bytes) |
| `0x1030a430` | `sub_1030a430` | 257 | support routine (257 bytes) |
| `0x1030a540` | `sub_1030a540` | 257 | support routine (257 bytes) |
| `0x1030a650` | `sub_1030a650` | 257 | support routine (257 bytes) |
| `0x1030a760` | `sub_1030a760` | 257 | support routine (257 bytes) |
| `0x1030a870` | `sub_1030a870` | 257 | support routine (257 bytes) |
| `0x1030a980` | `sub_1030a980` | 257 | support routine (257 bytes) |
| `0x1030aa90` | `sub_1030aa90` | 257 | support routine (257 bytes) |
| `0x1030aba0` | `sub_1030aba0` | 257 | support routine (257 bytes) |
| `0x1030acb0` | `sub_1030acb0` | 257 | support routine (257 bytes) |
| `0x1030adc0` | `sub_1030adc0` | 257 | support routine (257 bytes) |
| `0x1030aed0` | `sub_1030aed0` | 257 | support routine (257 bytes) |
| `0x1030afe0` | `sub_1030afe0` | 257 | support routine (257 bytes) |
| `0x1030b0f0` | `sub_1030b0f0` | 257 | support routine (257 bytes) |
| `0x1030b200` | `sub_1030b200` | 257 | support routine (257 bytes) |
| `0x1030b310` | `sub_1030b310` | 257 | support routine (257 bytes) |
| `0x1030b420` | `sub_1030b420` | 257 | support routine (257 bytes) |
| `0x1030b530` | `sub_1030b530` | 257 | support routine (257 bytes) |
| `0x1030b640` | `sub_1030b640` | 257 | support routine (257 bytes) |
| `0x1030b750` | `sub_1030b750` | 257 | support routine (257 bytes) |
| `0x1030b860` | `sub_1030b860` | 254 | support routine (254 bytes) |
| `0x1030b960` | `sub_1030b960` | 257 | support routine (257 bytes) |
| `0x1030ba70` | `sub_1030ba70` | 257 | support routine (257 bytes) |
| `0x1030bb80` | `sub_1030bb80` | 257 | support routine (257 bytes) |
| `0x1030bc90` | `sub_1030bc90` | 257 | support routine (257 bytes) |
| `0x1030bda0` | `sub_1030bda0` | 257 | support routine (257 bytes) |
| `0x1030beb0` | `sub_1030beb0` | 257 | support routine (257 bytes) |
| `0x1030bfc0` | `sub_1030bfc0` | 257 | support routine (257 bytes) |
| `0x1030c0d0` | `sub_1030c0d0` | 257 | support routine (257 bytes) |
| `0x1030c1e0` | `sub_1030c1e0` | 257 | support routine (257 bytes) |
| `0x1030c2f0` | `sub_1030c2f0` | 257 | support routine (257 bytes) |
| `0x1030c400` | `sub_1030c400` | 257 | support routine (257 bytes) |
| `0x1030c510` | `sub_1030c510` | 257 | support routine (257 bytes) |
| `0x1030c620` | `sub_1030c620` | 257 | support routine (257 bytes) |
| `0x1030c730` | `sub_1030c730` | 256 | support routine (256 bytes) |
| `0x1030c830` | `sub_1030c830` | 257 | support routine (257 bytes) |
| `0x1030c940` | `sub_1030c940` | 257 | support routine (257 bytes) |
| `0x1030ca50` | `sub_1030ca50` | 257 | support routine (257 bytes) |
| `0x1030cb60` | `sub_1030cb60` | 257 | support routine (257 bytes) |
| `0x1030cc70` | `sub_1030cc70` | 257 | support routine (257 bytes) |
| `0x1030cd80` | `sub_1030cd80` | 257 | support routine (257 bytes) |
| `0x1030ce90` | `sub_1030ce90` | 257 | support routine (257 bytes) |
| `0x1030cfa0` | `sub_1030cfa0` | 257 | support routine (257 bytes) |
| `0x1030d0b0` | `sub_1030d0b0` | 257 | support routine (257 bytes) |
| `0x1030d1c0` | `sub_1030d1c0` | 257 | support routine (257 bytes) |
| `0x1030d2d0` | `sub_1030d2d0` | 257 | support routine (257 bytes) |
| `0x1030d3e0` | `sub_1030d3e0` | 257 | support routine (257 bytes) |
| `0x1030d4f0` | `sub_1030d4f0` | 257 | support routine (257 bytes) |
| `0x1030d600` | `sub_1030d600` | 257 | support routine (257 bytes) |
| `0x1030d710` | `sub_1030d710` | 257 | support routine (257 bytes) |
| `0x1030d820` | `sub_1030d820` | 257 | support routine (257 bytes) |
| `0x1030d930` | `sub_1030d930` | 257 | support routine (257 bytes) |
| `0x1030da40` | `sub_1030da40` | 257 | support routine (257 bytes) |
| `0x1030db50` | `sub_1030db50` | 257 | support routine (257 bytes) |
| `0x1030dc60` | `sub_1030dc60` | 257 | support routine (257 bytes) |
| `0x1030dd70` | `sub_1030dd70` | 257 | support routine (257 bytes) |
| `0x1030de80` | `sub_1030de80` | 257 | support routine (257 bytes) |
| `0x1030df90` | `sub_1030df90` | 257 | support routine (257 bytes) |
| `0x1030e0a0` | `sub_1030e0a0` | 257 | support routine (257 bytes) |
| `0x1030e1b0` | `sub_1030e1b0` | 257 | support routine (257 bytes) |
| `0x1030e2c0` | `sub_1030e2c0` | 257 | support routine (257 bytes) |
| `0x1030e3d0` | `sub_1030e3d0` | 257 | support routine (257 bytes) |
| `0x1030e4e0` | `sub_1030e4e0` | 257 | support routine (257 bytes) |
| `0x1030e5f0` | `sub_1030e5f0` | 257 | support routine (257 bytes) |
| `0x1030e700` | `sub_1030e700` | 257 | support routine (257 bytes) |
| `0x1030e810` | `sub_1030e810` | 257 | support routine (257 bytes) |
| `0x1030e920` | `sub_1030e920` | 257 | support routine (257 bytes) |
| `0x1030ea30` | `sub_1030ea30` | 257 | support routine (257 bytes) |
| `0x1030eb40` | `sub_1030eb40` | 257 | support routine (257 bytes) |
| `0x1030ec50` | `sub_1030ec50` | 257 | support routine (257 bytes) |
| `0x1030ed60` | `sub_1030ed60` | 256 | support routine (256 bytes) |
| `0x1030ee60` | `sub_1030ee60` | 257 | support routine (257 bytes) |
| `0x1030ef70` | `sub_1030ef70` | 257 | support routine (257 bytes) |
| `0x1030f080` | `sub_1030f080` | 257 | support routine (257 bytes) |
| `0x1030f190` | `sub_1030f190` | 257 | support routine (257 bytes) |
| `0x1030f2a0` | `sub_1030f2a0` | 257 | support routine (257 bytes) |
| `0x1030f3b0` | `sub_1030f3b0` | 257 | support routine (257 bytes) |
| `0x1030f4c0` | `sub_1030f4c0` | 257 | support routine (257 bytes) |
| `0x1030f5d0` | `sub_1030f5d0` | 257 | support routine (257 bytes) |
| `0x1030f6e0` | `sub_1030f6e0` | 257 | support routine (257 bytes) |
| `0x1030f7f0` | `sub_1030f7f0` | 257 | support routine (257 bytes) |
| `0x1030f900` | `sub_1030f900` | 257 | support routine (257 bytes) |
| `0x1030fa10` | `sub_1030fa10` | 257 | support routine (257 bytes) |
| `0x1030fb20` | `sub_1030fb20` | 257 | support routine (257 bytes) |
| `0x1030fc30` | `sub_1030fc30` | 257 | support routine (257 bytes) |
| `0x1030fd40` | `sub_1030fd40` | 257 | support routine (257 bytes) |
| `0x1030fe50` | `sub_1030fe50` | 257 | support routine (257 bytes) |
| `0x1030ff60` | `sub_1030ff60` | 257 | support routine (257 bytes) |
| `0x10310070` | `sub_10310070` | 257 | support routine (257 bytes) |
| `0x10310180` | `sub_10310180` | 257 | support routine (257 bytes) |
| `0x10310290` | `sub_10310290` | 257 | support routine (257 bytes) |
| `0x103103a0` | `sub_103103a0` | 254 | support routine (254 bytes) |
| `0x103104a0` | `sub_103104a0` | 257 | support routine (257 bytes) |
| `0x103105b0` | `sub_103105b0` | 257 | support routine (257 bytes) |
| `0x103106c0` | `sub_103106c0` | 257 | support routine (257 bytes) |
| `0x103107d0` | `sub_103107d0` | 257 | support routine (257 bytes) |
| `0x103108e0` | `sub_103108e0` | 257 | support routine (257 bytes) |
| `0x103109f0` | `sub_103109f0` | 257 | support routine (257 bytes) |
| `0x10310b00` | `sub_10310b00` | 257 | support routine (257 bytes) |
| `0x10310c10` | `sub_10310c10` | 257 | support routine (257 bytes) |
| `0x10310d20` | `sub_10310d20` | 257 | support routine (257 bytes) |
| `0x10310e30` | `sub_10310e30` | 257 | support routine (257 bytes) |
| `0x10310f40` | `sub_10310f40` | 257 | support routine (257 bytes) |
| `0x10311050` | `sub_10311050` | 257 | support routine (257 bytes) |
| `0x10311160` | `resolveModuleDirAnsiWide` | 981 | Gets own module path via g_1038b1c4/c8/cc/d4 (GetModuleFileName A/W), strips after last backslash and '.', storing dir + filename into the struct (ANSI/wide branch). |
| `0x10311540` | `sub_10311540` | 97 | support routine (97 bytes) |
| `0x103115b0` | `sub_103115b0` | 208 | support routine (208 bytes) |
| `0x10311680` | `sub_10311680` | 189 | support routine (189 bytes) |
| `0x10311740` | `sub_10311740` | 208 | support routine (208 bytes) |
| `0x10311810` | `sub_10311810` | 193 | support routine (193 bytes) |
| `0x103118e0` | `sub_103118e0` | 93 | support routine (93 bytes) |
| `0x10311940` | `pipeIpcServerLoop` | 833 | Infinite IPC server loop: waits on window msgs (g_1038b344), polls named object g_103a1bec, reads pipe via sub_10311680/810 and marshals A/W strings to peer through g_1038b298/35c. |
| `0x10311c90` | `sub_10311c90` | 57 | support routine (57 bytes) |
| `0x10311ca8` | `sub_10311ca8` | 2 | trivial accessor/forwarder |
| `0x10311cd0` | `sub_10311cd0` | 254 | support routine (254 bytes) |
| `0x10311dc3` | `sub_10311dc3` | 2 | trivial accessor/forwarder |
| `0x10311dd0` | `sub_10311dd0` | 361 | support routine (361 bytes) |
| `0x10311e90` | `sub_10311e90` | 5 | trivial accessor/forwarder |
| `0x10311f40` | `ipcWindowMessageDispatch` | 1265 | Window-message dispatcher for custom IPC codes 992/993/996/1000: enumerates module names, filters 'dll loader'/'System', forwards buffers, else chains to default handler. |
| `0x10312460` | `sub_10312460` | 19 | support routine (19 bytes) |
| `0x10312480` | `sub_10312480` | 21 | support routine (21 bytes) |
| `0x103124a0` | `sub_103124a0` | 21 | support routine (21 bytes) |
| `0x103124c0` | `sub_103124c0` | 22 | support routine (22 bytes) |
| `0x103124e0` | `sub_103124e0` | 22 | support routine (22 bytes) |
| `0x10312500` | `sub_10312500` | 91 | support routine (91 bytes) |
| `0x10312560` | `sub_10312560` | 44 | support routine (44 bytes) |
| `0x10312590` | `sub_10312590` | 54 | support routine (54 bytes) |
| `0x103125d0` | `sub_103125d0` | 108 | support routine (108 bytes) |
| `0x10312640` | `sub_10312640` | 25 | support routine (25 bytes) |
| `0x10312660` | `sub_10312660` | 22 | support routine (22 bytes) |
| `0x10312680` | `sub_10312680` | 61 | support routine (61 bytes) |
| `0x103126c0` | `sub_103126c0` | 33 | support routine (33 bytes) |
| `0x103126f0` | `sub_103126f0` | 61 | support routine (61 bytes) |
| `0x10312730` | `dllMainInitHook` | 474 | DllMain-style entrypoint: on attach zeroes g_103a22a8 state, stores hinstance, and either reads INITIALIZEDLLADDR profile key (g_1038b064/68) or calls init sub_1031e0a0. |
| `0x1031282c` | `sub_1031282c` | 2 | trivial accessor/forwarder |
| `0x10312838` | `sub_10312838` | 5 | trivial accessor/forwarder |
| `0x10312878` | `sub_10312878` | 2 | trivial accessor/forwarder |
| `0x103128ac` | `sub_103128ac` | 13 | trivial accessor/forwarder |
| `0x103128ca` | `sub_103128ca` | 20 | support routine (20 bytes) |
| `0x103128de` | `sub_103128de` | 6 | trivial accessor/forwarder |
| `0x103128e4` | `sub_103128e4` | 11 | trivial accessor/forwarder |
| `0x103128ed` | `sub_103128ed` | 5 | trivial accessor/forwarder |
| `0x10312922` | `sub_10312922` | 13 | trivial accessor/forwarder |
| `0x10312960` | `sub_10312960` | 83 | support routine (83 bytes) |
| `0x103129a1` | `sub_103129a1` | 20 | support routine (20 bytes) |
| `0x103129b5` | `sub_103129b5` | 6 | trivial accessor/forwarder |
| `0x103129bb` | `sub_103129bb` | 20 | support routine (20 bytes) |
| `0x103129cf` | `sub_103129cf` | 6 | trivial accessor/forwarder |
| `0x103129d5` | `sub_103129d5` | 11 | trivial accessor/forwarder |
| `0x103129de` | `sub_103129de` | 5 | trivial accessor/forwarder |
| `0x103129e5` | `sub_103129e5` | 3 | trivial accessor/forwarder |
| `0x10312a00` | `sub_10312a00` | 42 | support routine (42 bytes) |
| `0x10312a30` | `sub_10312a30` | 222 | support routine (222 bytes) |
| `0x10312b10` | `sub_10312b10` | 112 | support routine (112 bytes) |
| `0x10312b80` | `sub_10312b80` | 16 | trivial accessor/forwarder |
| `0x10312b90` | `sub_10312b90` | 84 | support routine (84 bytes) |
| `0x10312bf0` | `sub_10312bf0` | 44 | support routine (44 bytes) |
| `0x10312c20` | `sub_10312c20` | 75 | support routine (75 bytes) |
| `0x10312c70` | `sub_10312c70` | 132 | support routine (132 bytes) |
| `0x10312d00` | `sub_10312d00` | 18 | support routine (18 bytes) |
| `0x10312d20` | `sub_10312d20` | 13 | trivial accessor/forwarder |
| `0x10312d30` | `sub_10312d30` | 16 | trivial accessor/forwarder |
| `0x10312d40` | `sub_10312d40` | 93 | support routine (93 bytes) |
| `0x10312da0` | `sub_10312da0` | 11 | trivial accessor/forwarder |
| `0x10312db0` | `sub_10312db0` | 20 | support routine (20 bytes) |
| `0x10312dd0` | `sub_10312dd0` | 36 | support routine (36 bytes) |
| `0x10312e00` | `sub_10312e00` | 240 | support routine (240 bytes) |
| `0x10312eb6` | `sub_10312eb6` | 2 | trivial accessor/forwarder |
| `0x10312f00` | `sub_10312f00` | 10 | trivial accessor/forwarder |
| `0x10312f10` | `sub_10312f10` | 236 | support routine (236 bytes) |
| `0x10312fd3` | `sub_10312fd3` | 2 | trivial accessor/forwarder |
| `0x10313000` | `sub_10313000` | 30 | support routine (30 bytes) |
| `0x10313020` | `sub_10313020` | 30 | support routine (30 bytes) |
| `0x10313040` | `sub_10313040` | 16 | trivial accessor/forwarder |
| `0x10313050` | `sub_10313050` | 13 | trivial accessor/forwarder |
| `0x10313060` | `sub_10313060` | 44 | support routine (44 bytes) |
| `0x10313090` | `sub_10313090` | 44 | support routine (44 bytes) |
| `0x103130c0` | `sub_103130c0` | 72 | support routine (72 bytes) |
| `0x10313110` | `sub_10313110` | 141 | support routine (141 bytes) |
| `0x103131a0` | `sub_103131a0` | 19 | support routine (19 bytes) |
| `0x103131c0` | `sub_103131c0` | 19 | support routine (19 bytes) |
| `0x103131e0` | `sub_103131e0` | 51 | support routine (51 bytes) |
| `0x10313220` | `sub_10313220` | 65 | support routine (65 bytes) |
| `0x10313270` | `sub_10313270` | 47 | support routine (47 bytes) |
| `0x103132a0` | `sub_103132a0` | 51 | support routine (51 bytes) |
| `0x103132e0` | `sub_103132e0` | 47 | support routine (47 bytes) |
| `0x10313310` | `sub_10313310` | 53 | support routine (53 bytes) |
| `0x10313350` | `sub_10313350` | 44 | support routine (44 bytes) |
| `0x10313380` | `sub_10313380` | 29 | support routine (29 bytes) |
| `0x103133a0` | `sub_103133a0` | 32 | support routine (32 bytes) |
| `0x103133c0` | `sub_103133c0` | 107 | support routine (107 bytes) |
| `0x10313430` | `sub_10313430` | 148 | support routine (148 bytes) |
| `0x103134d0` | `sub_103134d0` | 36 | support routine (36 bytes) |
| `0x10313500` | `sub_10313500` | 111 | support routine (111 bytes) |
| `0x10313570` | `sub_10313570` | 109 | support routine (109 bytes) |
| `0x103135e0` | `sub_103135e0` | 49 | support routine (49 bytes) |
| `0x10313620` | `sub_10313620` | 49 | support routine (49 bytes) |
| `0x10313660` | `sub_10313660` | 44 | support routine (44 bytes) |
| `0x10313690` | `sub_10313690` | 48 | support routine (48 bytes) |
| `0x103136c0` | `sub_103136c0` | 17 | support routine (17 bytes) |
| `0x103136e0` | `streamReadUntilCheckpoint` | 276 | iostream operation guarded by SEH: calls sub_103135e0/13eb0, compares sub_103161b0()==sub_1032fd20() (EOF sentinel) to set success flag; MSVC istream sentry pattern. |
| `0x10313800` | `sub_10313800` | 31 | support routine (31 bytes) |
| `0x10313820` | `sub_10313820` | 28 | support routine (28 bytes) |
| `0x10313840` | `sub_10313840` | 17 | support routine (17 bytes) |
| `0x10313860` | `sub_10313860` | 30 | support routine (30 bytes) |
| `0x10313880` | `sub_10313880` | 33 | support routine (33 bytes) |
| `0x103138b0` | `sub_103138b0` | 84 | support routine (84 bytes) |
| `0x10313910` | `sub_10313910` | 32 | support routine (32 bytes) |
| `0x10313930` | `sub_10313930` | 44 | support routine (44 bytes) |
| `0x10313960` | `sub_10313960` | 31 | support routine (31 bytes) |
| `0x10313980` | `sub_10313980` | 44 | support routine (44 bytes) |
| `0x103139b0` | `sub_103139b0` | 53 | support routine (53 bytes) |
| `0x103139f0` | `sub_103139f0` | 141 | support routine (141 bytes) |
| `0x10313a80` | `sub_10313a80` | 135 | support routine (135 bytes) |
| `0x10313b10` | `sub_10313b10` | 19 | support routine (19 bytes) |
| `0x10313b30` | `sub_10313b30` | 36 | support routine (36 bytes) |
| `0x10313b60` | `sub_10313b60` | 25 | support routine (25 bytes) |
| `0x10313b80` | `sub_10313b80` | 44 | support routine (44 bytes) |
| `0x10313bb0` | `sub_10313bb0` | 20 | support routine (20 bytes) |
| `0x10313bd0` | `sub_10313bd0` | 34 | support routine (34 bytes) |
| `0x10313c00` | `sub_10313c00` | 36 | support routine (36 bytes) |
| `0x10313c30` | `sub_10313c30` | 158 | support routine (158 bytes) |
| `0x10313cd0` | `sub_10313cd0` | 148 | support routine (148 bytes) |
| `0x10313d70` | `sub_10313d70` | 87 | support routine (87 bytes) |
| `0x10313dd0` | `sub_10313dd0` | 117 | support routine (117 bytes) |
| `0x10313e50` | `sub_10313e50` | 44 | support routine (44 bytes) |
| `0x10313e80` | `sub_10313e80` | 44 | support routine (44 bytes) |
| `0x10313eb0` | `sub_10313eb0` | 170 | support routine (170 bytes) |
| `0x10313f60` | `sub_10313f60` | 87 | support routine (87 bytes) |
| `0x10313fc0` | `sub_10313fc0` | 23 | support routine (23 bytes) |
| `0x10313fe0` | `sub_10313fe0` | 109 | support routine (109 bytes) |
| `0x10314050` | `sub_10314050` | 141 | support routine (141 bytes) |
| `0x103140e0` | `sub_103140e0` | 27 | support routine (27 bytes) |
| `0x10314100` | `iosBaseClearThrow` | 385 | std::basic_ios::clear check: masks state&exceptions and throws ios_base::failure with badbit/failbit/eofbit message accordingly (MSVC iostream). |
| `0x10314290` | `sub_10314290` | 115 | support routine (115 bytes) |
| `0x10314310` | `sub_10314310` | 22 | support routine (22 bytes) |
| `0x10314330` | `sub_10314330` | 44 | support routine (44 bytes) |
| `0x10314360` | `sub_10314360` | 99 | support routine (99 bytes) |
| `0x103143d0` | `sub_103143d0` | 93 | support routine (93 bytes) |
| `0x10314430` | `sub_10314430` | 108 | support routine (108 bytes) |
| `0x103144a0` | `sub_103144a0` | 84 | support routine (84 bytes) |
| `0x10314500` | `sub_10314500` | 44 | support routine (44 bytes) |
| `0x10314530` | `sub_10314530` | 93 | support routine (93 bytes) |
| `0x10314590` | `sub_10314590` | 58 | support routine (58 bytes) |
| `0x103145d0` | `sub_103145d0` | 61 | support routine (61 bytes) |
| `0x10314610` | `sub_10314610` | 23 | support routine (23 bytes) |
| `0x10314630` | `sub_10314630` | 43 | support routine (43 bytes) |
| `0x10314660` | `sub_10314660` | 182 | support routine (182 bytes) |
| `0x10314720` | `sub_10314720` | 38 | support routine (38 bytes) |
| `0x10314750` | `sub_10314750` | 118 | support routine (118 bytes) |
| `0x103147d0` | `sub_103147d0` | 28 | support routine (28 bytes) |
| `0x103147f0` | `sub_103147f0` | 57 | support routine (57 bytes) |
| `0x10314830` | `sub_10314830` | 132 | support routine (132 bytes) |
| `0x103148c0` | `sub_103148c0` | 148 | support routine (148 bytes) |
| `0x10314960` | `sub_10314960` | 52 | support routine (52 bytes) |
| `0x103149a0` | `sub_103149a0` | 15 | trivial accessor/forwarder |
| `0x103149b0` | `sub_103149b0` | 148 | support routine (148 bytes) |
| `0x10314a50` | `sub_10314a50` | 45 | support routine (45 bytes) |
| `0x10314a80` | `sub_10314a80` | 51 | support routine (51 bytes) |
| `0x10314ac0` | `stringGrowReallocate` | 285 | std::basic_string::_Reallocate/grow: computes new capacity (max, 1.5x growth), allocates via sub_10314c40, copies old data, updates pointer/capacity fields. |
| `0x10314b72` | `sub_10314b72` | 19 | support routine (19 bytes) |
| `0x10314b85` | `sub_10314b85` | 34 | support routine (34 bytes) |
| `0x10314b93` | `sub_10314b93` | 34 | support routine (34 bytes) |
| `0x10314c40` | `sub_10314c40` | 27 | support routine (27 bytes) |
| `0x10314c60` | `sub_10314c60` | 51 | support routine (51 bytes) |
| `0x10314c8b` | `sub_10314c8b` | 2 | trivial accessor/forwarder |
| `0x10314ca0` | `sub_10314ca0` | 127 | support routine (127 bytes) |
| `0x10314d20` | `sub_10314d20` | 30 | support routine (30 bytes) |
| `0x10314d40` | `sub_10314d40` | 98 | support routine (98 bytes) |
| `0x10314db0` | `sub_10314db0` | 36 | support routine (36 bytes) |
| `0x10314de0` | `sub_10314de0` | 44 | support routine (44 bytes) |
| `0x10314e10` | `sub_10314e10` | 233 | support routine (233 bytes) |
| `0x10314f00` | `sub_10314f00` | 134 | support routine (134 bytes) |
| `0x10314f90` | `sub_10314f90` | 23 | support routine (23 bytes) |
| `0x10314fb0` | `sub_10314fb0` | 130 | support routine (130 bytes) |
| `0x10314ffe` | `sub_10314ffe` | 2 | trivial accessor/forwarder |
| `0x10315040` | `sub_10315040` | 144 | support routine (144 bytes) |
| `0x103150d0` | `sub_103150d0` | 222 | support routine (222 bytes) |
| `0x103151b0` | `sub_103151b0` | 221 | support routine (221 bytes) |
| `0x10315290` | `sub_10315290` | 147 | support routine (147 bytes) |
| `0x10315330` | `sub_10315330` | 93 | support routine (93 bytes) |
| `0x10315390` | `sub_10315390` | 20 | support routine (20 bytes) |
| `0x103153b0` | `sub_103153b0` | 34 | support routine (34 bytes) |
| `0x103153e0` | `sub_103153e0` | 44 | support routine (44 bytes) |
| `0x10315410` | `sub_10315410` | 84 | support routine (84 bytes) |
| `0x10315470` | `sub_10315470` | 44 | support routine (44 bytes) |
| `0x103154a0` | `sub_103154a0` | 55 | support routine (55 bytes) |
| `0x103154e0` | `sub_103154e0` | 79 | support routine (79 bytes) |
| `0x10315530` | `sub_10315530` | 69 | support routine (69 bytes) |
| `0x10315580` | `sub_10315580` | 33 | support routine (33 bytes) |
| `0x103155b0` | `sub_103155b0` | 64 | support routine (64 bytes) |
| `0x103155f0` | `sub_103155f0` | 33 | support routine (33 bytes) |
| `0x10315620` | `sub_10315620` | 64 | support routine (64 bytes) |
| `0x10315660` | `sub_10315660` | 16 | trivial accessor/forwarder |
| `0x10315670` | `sub_10315670` | 45 | support routine (45 bytes) |
| `0x103156a0` | `sub_103156a0` | 59 | support routine (59 bytes) |
| `0x103156e0` | `sub_103156e0` | 16 | trivial accessor/forwarder |
| `0x103156f0` | `sub_103156f0` | 49 | support routine (49 bytes) |
| `0x10315730` | `sub_10315730` | 59 | support routine (59 bytes) |
| `0x10315770` | `sub_10315770` | 44 | support routine (44 bytes) |
| `0x103157a0` | `sub_103157a0` | 92 | support routine (92 bytes) |
| `0x10315800` | `sub_10315800` | 44 | support routine (44 bytes) |
| `0x10315830` | `sub_10315830` | 74 | support routine (74 bytes) |
| `0x10315880` | `sub_10315880` | 93 | support routine (93 bytes) |
| `0x103158e0` | `sub_103158e0` | 84 | support routine (84 bytes) |
| `0x10315940` | `sub_10315940` | 44 | support routine (44 bytes) |
| `0x10315970` | `sub_10315970` | 93 | support routine (93 bytes) |
| `0x103159d0` | `sub_103159d0` | 44 | support routine (44 bytes) |
| `0x10315a00` | `sub_10315a00` | 29 | support routine (29 bytes) |
| `0x10315a20` | `sub_10315a20` | 32 | support routine (32 bytes) |
| `0x10315a40` | `istreamSentryExtractInt` | 365 | MSVC num_get facet extract: constructs istream sentry (sub_10315c40), on success reads via sub_10314d40/16540 and stores parsed value; std::istream::operator>> path. |
| `0x10315b64` | `sub_10315b64` | 33 | support routine (33 bytes) |
| `0x10315bd0` | `sub_10315bd0` | 75 | support routine (75 bytes) |
| `0x10315c20` | `sub_10315c20` | 17 | support routine (17 bytes) |
| `0x10315c40` | `sub_10315c40` | 104 | support routine (104 bytes) |
| `0x10315cb0` | `istreamSentryConstruct` | 452 | std::basic_istream<>::sentry constructor: flushes tied stream, optionally skips whitespace via ctype facet loop, sets stream state good/fail (MSVC). |
| `0x10315e04` | `sub_10315e04` | 2 | trivial accessor/forwarder |
| `0x10315e2a` | `sub_10315e2a` | 33 | support routine (33 bytes) |
| `0x10315ea0` | `sub_10315ea0` | 39 | support routine (39 bytes) |
| `0x10315ed0` | `sub_10315ed0` | 26 | support routine (26 bytes) |
| `0x10315ef0` | `sub_10315ef0` | 17 | support routine (17 bytes) |
| `0x10315f10` | `sub_10315f10` | 107 | support routine (107 bytes) |
| `0x10315f80` | `sub_10315f80` | 66 | support routine (66 bytes) |
| `0x10315fd0` | `sub_10315fd0` | 120 | support routine (120 bytes) |
| `0x10316050` | `sub_10316050` | 77 | support routine (77 bytes) |
| `0x103160a0` | `sub_103160a0` | 24 | support routine (24 bytes) |
| `0x103160c0` | `sub_103160c0` | 66 | support routine (66 bytes) |
| `0x10316110` | `sub_10316110` | 22 | support routine (22 bytes) |
| `0x10316130` | `sub_10316130` | 57 | support routine (57 bytes) |
| `0x10316170` | `sub_10316170` | 17 | support routine (17 bytes) |
| `0x10316190` | `sub_10316190` | 22 | support routine (22 bytes) |
| `0x103161b0` | `istreambufIteratorIncrement` | 282 | std::istreambuf_iterator increment/get: constructs sentry, reads next char via sbumpc (sub_10315c20), sets EOF flag on sentinel; MSVC iterator. |
| `0x10316283` | `sub_10316283` | 33 | support routine (33 bytes) |
| `0x103162f0` | `sub_103162f0` | 132 | support routine (132 bytes) |
| `0x10316380` | `sub_10316380` | 142 | support routine (142 bytes) |
| `0x10316410` | `sub_10316410` | 148 | support routine (148 bytes) |
| `0x103164b0` | `sub_103164b0` | 42 | support routine (42 bytes) |
| `0x103164e0` | `sub_103164e0` | 89 | support routine (89 bytes) |
| `0x10316540` | `sub_10316540` | 48 | support routine (48 bytes) |
| `0x10316570` | `sub_10316570` | 24 | support routine (24 bytes) |
| `0x10316590` | `sub_10316590` | 36 | support routine (36 bytes) |
| `0x103165c0` | `sub_103165c0` | 88 | support routine (88 bytes) |
| `0x10316620` | `sub_10316620` | 88 | support routine (88 bytes) |
| `0x10316680` | `sub_10316680` | 233 | support routine (233 bytes) |
| `0x10316770` | `sub_10316770` | 118 | support routine (118 bytes) |
| `0x103167f0` | `sub_103167f0` | 120 | support routine (120 bytes) |
| `0x10316870` | `sub_10316870` | 194 | support routine (194 bytes) |
| `0x10316940` | `sub_10316940` | 17 | support routine (17 bytes) |
| `0x10316960` | `sub_10316960` | 70 | support routine (70 bytes) |
| `0x103169b0` | `sub_103169b0` | 30 | support routine (30 bytes) |
| `0x103169d0` | `sub_103169d0` | 37 | support routine (37 bytes) |
| `0x10316a00` | `sub_10316a00` | 23 | support routine (23 bytes) |
| `0x10316a20` | `sub_10316a20` | 140 | support routine (140 bytes) |
| `0x10316ab0` | `sub_10316ab0` | 176 | support routine (176 bytes) |
| `0x10316b60` | `numGetDoConvertBool` | 633 | MSVC std::num_get::do_get(bool): if boolalpha reads word and matches truename/falsename, else parses numeric 0/1, sets failbit/eofbit in state flags. |
| `0x10316de0` | `sub_10316de0` | 25 | support routine (25 bytes) |
| `0x10316e00` | `sub_10316e00` | 33 | support routine (33 bytes) |
| `0x10316e30` | `sub_10316e30` | 205 | support routine (205 bytes) |
| `0x10316f00` | `sub_10316f00` | 100 | support routine (100 bytes) |
| `0x10316f70` | `sub_10316f70` | 100 | support routine (100 bytes) |
| `0x10316fe0` | `sub_10316fe0` | 233 | support routine (233 bytes) |
| `0x103170d0` | `sub_103170d0` | 27 | support routine (27 bytes) |
| `0x103170f0` | `sub_103170f0` | 114 | support routine (114 bytes) |
| `0x10317170` | `sub_10317170` | 73 | support routine (73 bytes) |
| `0x103171c0` | `sub_103171c0` | 26 | support routine (26 bytes) |
| `0x103171e0` | `sub_103171e0` | 140 | support routine (140 bytes) |
| `0x10317270` | `sub_10317270` | 230 | support routine (230 bytes) |
| `0x10317360` | `sub_10317360` | 43 | support routine (43 bytes) |
| `0x10317390` | `sub_10317390` | 17 | support routine (17 bytes) |
| `0x103173b0` | `sub_103173b0` | 17 | support routine (17 bytes) |
| `0x103173d0` | `sub_103173d0` | 98 | support routine (98 bytes) |
| `0x10317440` | `sub_10317440` | 98 | support routine (98 bytes) |
| `0x103174b0` | `sub_103174b0` | 98 | support routine (98 bytes) |
| `0x10317520` | `sub_10317520` | 44 | support routine (44 bytes) |
| `0x10317550` | `sub_10317550` | 92 | support routine (92 bytes) |
| `0x103175b0` | `sub_103175b0` | 76 | support routine (76 bytes) |
| `0x10317600` | `numpunctCacheGrouping` | 311 | std::numpunct facet init: caches decimal_point, thousands_sep, grouping, and true/false-name strings from the locale via sub_10317360/18a60 (MSVC). |
| `0x103176d1` | `sub_103176d1` | 30 | support routine (30 bytes) |
| `0x10317760` | `sub_10317760` | 16 | trivial accessor/forwarder |
| `0x10317770` | `sub_10317770` | 16 | trivial accessor/forwarder |
| `0x10317780` | `sub_10317780` | 16 | trivial accessor/forwarder |
| `0x10317790` | `sub_10317790` | 105 | support routine (105 bytes) |
| `0x10317800` | `sub_10317800` | 62 | support routine (62 bytes) |
| `0x10317840` | `sub_10317840` | 78 | support routine (78 bytes) |
| `0x10317890` | `numGetDoGetUShort` | 348 | MSVC std::num_get::do_get for unsigned short: scans digits via sub_103184e0, strtoul-parses, range-checks <=0xffff, applies sign, sets failbit on overflow. |
| `0x103179f0` | `numGetDoGetULong` | 343 | MSVC std::num_get::do_get for unsigned long: scans integer field, strtoul-parses and stores result, setting failbit/eofbit stream flags. |
| `0x10317b50` | `numGetDoGetLong` | 279 | MSVC std::num_get::do_get for long: scans integer field via sub_103184e0, strtol-parses (sub_10350844), stores signed result and stream flags. |
| `0x10317c70` | `numGetDoGetUIntVariant` | 279 | MSVC std::num_get::do_get for an unsigned integer type: scans field, strtoul-parses (sub_1035069a), stores value and failbit/eofbit flags. |
| `0x10317d90` | `numGetDoGetLongLong` | 284 | MSVC std::num_get::do_get for __int64: scans integer field, strtoll-parses (sub_103539bd), stores 64-bit result (low+high) and stream flags. |
| `0x10317eb0` | `numGetDoGetULongLong` | 284 | MSVC std::num_get::do_get for unsigned __int64: scans field, strtoull-parses (sub_103539e6), stores 64-bit result and stream flags. |
| `0x10317fd0` | `numGetDoGetFloat` | 270 | MSVC std::num_get::do_get(float): scans floating field via sub_10318a70, strtof-parses (sub_103508e7), stores float result and failbit/eofbit flags. |
| `0x103180e0` | `numGetDoGetDouble` | 270 | MSVC std::num_get::do_get(double): scans floating field, strtod-parses (sub_10350907), stores double into 8-byte target with stream flags. |
| `0x103181f0` | `numGetDoGetLongDouble` | 270 | MSVC std::num_get::do_get(long double): scans floating field, strtold-parses (sub_1035096e), stores result with failbit/eofbit flags. |
| `0x10318300` | `sub_10318300` | 335 | bot logic dispatcher (described in jiru-logic pass) |
| `0x10318450` | `sub_10318450` | 44 | support routine (44 bytes) |
| `0x10318480` | `sub_10318480` | 84 | support routine (84 bytes) |
| `0x103184e0` | `numGetScanIntegerField` | 1212 | MSVC num_get integer field scanner: reads sign, 0x/0 base prefix, grouping-aware digit run against radix into buffer, tracking thousands separators. |
| `0x10318860` | `sub_10318860` | 2 | trivial accessor/forwarder |
| `0x103188cc` | `sub_103188cc` | 2 | trivial accessor/forwarder |
| `0x103189a0` | `sub_103189a0` | 40 | support routine (40 bytes) |
| `0x103189d0` | `sub_103189d0` | 24 | support routine (24 bytes) |
| `0x103189f0` | `sub_103189f0` | 100 | support routine (100 bytes) |
| `0x10318a60` | `sub_10318a60` | 8 | trivial accessor/forwarder |
| `0x10318a70` | `numGetScanFloatField` | 1933 | MSVC num_get floating field scanner: reads sign, integer/fraction digits with grouping, decimal point, and e/E exponent with sign into buffer. |
| `0x10318d8b` | `sub_10318d8b` | 2 | trivial accessor/forwarder |
| `0x10318df7` | `sub_10318df7` | 2 | trivial accessor/forwarder |
| `0x10319210` | `sub_10319210` | 24 | support routine (24 bytes) |
| `0x10319230` | `sub_10319230` | 36 | support routine (36 bytes) |
| `0x10319260` | `sub_10319260` | 22 | support routine (22 bytes) |
| `0x10319280` | `sub_10319280` | 93 | support routine (93 bytes) |
| `0x103192e0` | `sub_103192e0` | 110 | support routine (110 bytes) |
| `0x10319350` | `numGetMatchLongestName` | 565 | MSVC num_get bool/name matcher: given a candidate-name table separated by first char, advances the stream matching the longest prefix, returns matched index. |
| `0x10319590` | `sub_10319590` | 17 | support routine (17 bytes) |
| `0x103195b0` | `sub_103195b0` | 31 | support routine (31 bytes) |
| `0x103195d0` | `sub_103195d0` | 108 | support routine (108 bytes) |
| `0x10319640` | `sub_10319640` | 41 | support routine (41 bytes) |
| `0x10319670` | `sub_10319670` | 10 | trivial accessor/forwarder |
| `0x10319680` | `sub_10319680` | 8 | trivial accessor/forwarder |
| `0x10319690` | `sub_10319690` | 8 | trivial accessor/forwarder |
| `0x103196a0` | `sub_103196a0` | 8 | trivial accessor/forwarder |
| `0x103196b0` | `logCheckpointDiagnostic` | 428 | Diagnostic logger: formats "Last recorded checkpoint was '<file>', <fn> line <n>" via sub_1031a5*/780 string builders and emits it (sub_10319f70). |
| `0x10319860` | `reportUnhandledException` | 275 | Crash reporter: builds an 'Unhandled Exception' message with global g_103a2288, logs it (sub_10319e80) and writes a report/dump via sub_1032a610. |
| `0x10319980` | `sub_10319980` | 217 | support routine (217 bytes) |
| `0x10319a60` | `sub_10319a60` | 18 | support routine (18 bytes) |
| `0x10319a80` | `formatSehExceptionName` | 705 | Maps a Windows SEH exception code (EXCEPTION_ACCESS_VIOLATION, FLT_*, INT_*, STACK_OVERFLOW, etc.) to its name string and builds a 'C exception ...' report line. |
| `0x10319e80` | `sub_10319e80` | 114 | support routine (114 bytes) |
| `0x10319f00` | `sub_10319f00` | 105 | support routine (105 bytes) |
| `0x10319f70` | `sub_10319f70` | 25 | support routine (25 bytes) |
| `0x10319f90` | `sub_10319f90` | 86 | support routine (86 bytes) |
| `0x10319ff0` | `sub_10319ff0` | 78 | support routine (78 bytes) |
| `0x1031a040` | `sub_1031a040` | 75 | support routine (75 bytes) |
| `0x1031a090` | `sub_1031a090` | 78 | support routine (78 bytes) |
| `0x1031a0e0` | `sub_1031a0e0` | 75 | support routine (75 bytes) |
| `0x1031a130` | `sub_1031a130` | 33 | support routine (33 bytes) |
| `0x1031a160` | `sub_1031a160` | 97 | support routine (97 bytes) |
| `0x1031a1d0` | `sub_1031a1d0` | 20 | support routine (20 bytes) |
| `0x1031a1f0` | `sub_1031a1f0` | 19 | support routine (19 bytes) |
| `0x1031a210` | `sub_1031a210` | 19 | support routine (19 bytes) |
| `0x1031a230` | `sub_1031a230` | 78 | support routine (78 bytes) |
| `0x1031a280` | `sub_1031a280` | 14 | trivial accessor/forwarder |
| `0x1031a290` | `sub_1031a290` | 75 | support routine (75 bytes) |
| `0x1031a2e0` | `sub_1031a2e0` | 35 | support routine (35 bytes) |
| `0x1031a310` | `sub_1031a310` | 35 | support routine (35 bytes) |
| `0x1031a340` | `sub_1031a340` | 34 | support routine (34 bytes) |
| `0x1031a370` | `sub_1031a370` | 34 | support routine (34 bytes) |
| `0x1031a3a0` | `sub_1031a3a0` | 23 | support routine (23 bytes) |
| `0x1031a3c0` | `sub_1031a3c0` | 118 | support routine (118 bytes) |
| `0x1031a440` | `sub_1031a440` | 57 | support routine (57 bytes) |
| `0x1031a480` | `sub_1031a480` | 17 | support routine (17 bytes) |
| `0x1031a4a0` | `sub_1031a4a0` | 45 | support routine (45 bytes) |
| `0x1031a4d0` | `sub_1031a4d0` | 108 | support routine (108 bytes) |
| `0x1031a540` | `sub_1031a540` | 132 | support routine (132 bytes) |
| `0x1031a5d0` | `sub_1031a5d0` | 132 | support routine (132 bytes) |
| `0x1031a660` | `sub_1031a660` | 25 | support routine (25 bytes) |
| `0x1031a680` | `sub_1031a680` | 38 | support routine (38 bytes) |
| `0x1031a6b0` | `sub_1031a6b0` | 206 | support routine (206 bytes) |
| `0x1031a780` | `sub_1031a780` | 132 | support routine (132 bytes) |
| `0x1031a810` | `sub_1031a810` | 104 | support routine (104 bytes) |
| `0x1031a866` | `sub_1031a866` | 30 | support routine (30 bytes) |
| `0x1031a884` | `sub_1031a884` | 6 | trivial accessor/forwarder |
| `0x1031a88a` | `sub_1031a88a` | 30 | support routine (30 bytes) |
| `0x1031a8a8` | `sub_1031a8a8` | 6 | trivial accessor/forwarder |
| `0x1031a8ae` | `sub_1031a8ae` | 11 | trivial accessor/forwarder |
| `0x1031a8b7` | `sub_1031a8b7` | 5 | trivial accessor/forwarder |
| `0x1031a8be` | `sub_1031a8be` | 3 | trivial accessor/forwarder |
| `0x1031a8e0` | `sub_1031a8e0` | 104 | support routine (104 bytes) |
| `0x1031a936` | `sub_1031a936` | 30 | support routine (30 bytes) |
| `0x1031a954` | `sub_1031a954` | 6 | trivial accessor/forwarder |
| `0x1031a95a` | `sub_1031a95a` | 30 | support routine (30 bytes) |
| `0x1031a978` | `sub_1031a978` | 6 | trivial accessor/forwarder |
| `0x1031a97e` | `sub_1031a97e` | 11 | trivial accessor/forwarder |
| `0x1031a987` | `sub_1031a987` | 5 | trivial accessor/forwarder |
| `0x1031a98e` | `sub_1031a98e` | 3 | trivial accessor/forwarder |
| `0x1031a9b0` | `sub_1031a9b0` | 44 | support routine (44 bytes) |
| `0x1031a9e0` | `sub_1031a9e0` | 52 | support routine (52 bytes) |
| `0x1031aa20` | `sub_1031aa20` | 43 | support routine (43 bytes) |
| `0x1031aa50` | `sub_1031aa50` | 24 | support routine (24 bytes) |
| `0x1031aa70` | `sub_1031aa70` | 46 | support routine (46 bytes) |
| `0x1031aaa0` | `sub_1031aaa0` | 127 | support routine (127 bytes) |
| `0x1031ab20` | `sub_1031ab20` | 127 | support routine (127 bytes) |
| `0x1031aba0` | `sub_1031aba0` | 29 | support routine (29 bytes) |
| `0x1031abc0` | `sub_1031abc0` | 32 | support routine (32 bytes) |
| `0x1031abe0` | `sub_1031abe0` | 33 | support routine (33 bytes) |
| `0x1031ac10` | `sub_1031ac10` | 49 | support routine (49 bytes) |
| `0x1031ac50` | `sub_1031ac50` | 21 | support routine (21 bytes) |
| `0x1031ac70` | `sub_1031ac70` | 124 | support routine (124 bytes) |
| `0x1031acf0` | `sub_1031acf0` | 8 | trivial accessor/forwarder |
| `0x1031ad00` | `insertStringOrThrow_variant1` | 279 | std::basic_string insert/assign helper: copies range then either calls sub_1031b2c0 path or throws out_of_range via sub_10312b10(&g_1038c770,&g_1038c780). |
| `0x1031ae20` | `insertStringOrThrow_variant2` | 279 | Near-identical string insert/assign helper to sub_1031ad00 but uses sub_1031b290 and throws with message globals &g_1038c360/&g_1038c780. |
| `0x1031af40` | `stringReplaceDispatch` | 720 | std::basic_string replace/append dispatcher switching on op index a1 (0-19) to sub_1031b350/380/3b0 or sub_1033ce00 with _INSERT-packed args. |
| `0x1031b260` | `sub_1031b260` | 33 | support routine (33 bytes) |
| `0x1031b290` | `sub_1031b290` | 39 | support routine (39 bytes) |
| `0x1031b2c0` | `sub_1031b2c0` | 91 | support routine (91 bytes) |
| `0x1031b320` | `sub_1031b320` | 36 | support routine (36 bytes) |
| `0x1031b350` | `sub_1031b350` | 41 | support routine (41 bytes) |
| `0x1031b380` | `sub_1031b380` | 41 | support routine (41 bytes) |
| `0x1031b3b0` | `sub_1031b3b0` | 41 | support routine (41 bytes) |
| `0x1031b3e0` | `stringFormatGroupedNumber` | 480 | Formats unsigned int i into a string with locale grouping (numpunct via sub_103189a0/sub_1031e920) writing digits with sub_103149a0. |
| `0x1031b5c0` | `sub_1031b5c0` | 41 | support routine (41 bytes) |
| `0x1031b5f0` | `sub_1031b5f0` | 51 | support routine (51 bytes) |
| `0x1031b630` | `sub_1031b630` | 28 | support routine (28 bytes) |
| `0x1031b650` | `sub_1031b650` | 28 | support routine (28 bytes) |
| `0x1031b670` | `sub_1031b670` | 28 | support routine (28 bytes) |
| `0x1031b690` | `sub_1031b690` | 69 | support routine (69 bytes) |
| `0x1031b6e0` | `sub_1031b6e0` | 37 | support routine (37 bytes) |
| `0x1031b710` | `sub_1031b710` | 32 | support routine (32 bytes) |
| `0x1031b730` | `sub_1031b730` | 90 | support routine (90 bytes) |
| `0x1031b790` | `sub_1031b790` | 43 | support routine (43 bytes) |
| `0x1031b7c0` | `sub_1031b7c0` | 13 | trivial accessor/forwarder |
| `0x1031b7d0` | `sub_1031b7d0` | 23 | support routine (23 bytes) |
| `0x1031b7f0` | `sub_1031b7f0` | 44 | support routine (44 bytes) |
| `0x1031b820` | `sub_1031b820` | 23 | support routine (23 bytes) |
| `0x1031b840` | `sub_1031b840` | 44 | support routine (44 bytes) |
| `0x1031b870` | `sub_1031b870` | 67 | support routine (67 bytes) |
| `0x1031b8c0` | `sub_1031b8c0` | 145 | support routine (145 bytes) |
| `0x1031b960` | `sub_1031b960` | 136 | support routine (136 bytes) |
| `0x1031b9f0` | `sub_1031b9f0` | 41 | support routine (41 bytes) |
| `0x1031ba20` | `sub_1031ba20` | 60 | support routine (60 bytes) |
| `0x1031ba60` | `sub_1031ba60` | 37 | support routine (37 bytes) |
| `0x1031ba90` | `stringReplaceInPlace` | 818 | std::basic_string::replace core: shifts/copies buffer regions (sub_103159d0/sub_10313350) handling overlap cases, growing via sub_103149b0. |
| `0x1031bdd0` | `sub_1031bdd0` | 82 | support routine (82 bytes) |
| `0x1031be30` | `sub_1031be30` | 159 | support routine (159 bytes) |
| `0x1031beb4` | `sub_1031beb4` | 34 | support routine (34 bytes) |
| `0x1031bf00` | `sub_1031bf00` | 79 | support routine (79 bytes) |
| `0x1031bf50` | `sub_1031bf50` | 47 | support routine (47 bytes) |
| `0x1031bf80` | `sub_1031bf80` | 21 | support routine (21 bytes) |
| `0x1031bfa0` | `sub_1031bfa0` | 29 | support routine (29 bytes) |
| `0x1031bfc0` | `sub_1031bfc0` | 71 | support routine (71 bytes) |
| `0x1031c010` | `sub_1031c010` | 17 | support routine (17 bytes) |
| `0x1031c030` | `sub_1031c030` | 10 | trivial accessor/forwarder |
| `0x1031c040` | `sub_1031c040` | 31 | support routine (31 bytes) |
| `0x1031c060` | `computeArKeyHash` | 865 | ElfBot anti-debug/key routine: lazily inits g_103a2610 lock, XOR-folds 20 idx fields, runs sub_10353fac/fd0 arithmetic to emit an 8-char hex token into a0. |
| `0x1031c3f0` | `sub_1031c3f0` | 14 | trivial accessor/forwarder |
| `0x1031c400` | `loadArmadilloSection` | 1151 | Armadillo/ArmAccess loader: locates packed section via sub_1031c880, builds a hash/permutation table, checks cmdline for -sp/-p, then jumps to sub_1031cd70. |
| `0x1031c880` | `findArmadilloSection` | 310 | Scans PE section table (g_103a2234) for a section whose name matches decrypted string 'z5O[' with flags 0x40000000, returning its file offset. |
| `0x1031c9c0` | `decryptAndRunPayload` | 618 | Parses Armadillo payload blocks (types 1/2/3): reads ARMSPLASHOFF env, decrypts chunks via sub_1031cc30, invokes sub_1031f410 unless suppressed. |
| `0x1031cc30` | `decompressPayloadBlock` | 320 | Reads a length-prefixed block (high-bit = uncompressed), allocates buffer, decompresses via sub_102ebca0 or copies raw, optionally callbacks a3. |
| `0x1031cd70` | `sub_1031cd70` | 151 | support routine (151 bytes) |
| `0x1031cd88` | `sub_1031cd88` | 1 | trivial accessor/forwarder |
| `0x1031cdc6` | `sub_1031cdc6` | 1 | trivial accessor/forwarder |
| `0x1031cdcd` | `sub_1031cdcd` | 3 | trivial accessor/forwarder |
| `0x1031cdff` | `sub_1031cdff` | 1 | trivial accessor/forwarder |
| `0x1031ce0f` | `sub_1031ce0f` | 136 | support routine (136 bytes) |
| `0x1031ce33` | `sub_1031ce33` | 56 | support routine (56 bytes) |
| `0x1031cebf` | `sub_1031cebf` | 1 | trivial accessor/forwarder |
| `0x1031ced3` | `sub_1031ced3` | 105 | support routine (105 bytes) |
| `0x1031ced7` | `sub_1031ced7` | 2 | trivial accessor/forwarder |
| `0x1031ced9` | `sub_1031ced9` | 1 | trivial accessor/forwarder |
| `0x1031cf0f` | `sub_1031cf0f` | 1 | trivial accessor/forwarder |
| `0x1031cf16` | `sub_1031cf16` | 3 | trivial accessor/forwarder |
| `0x1031cf43` | `sub_1031cf43` | 1 | trivial accessor/forwarder |
| `0x1031cf44` | `applyRelocationsAndImports` | 672 | Loader stage applying base relocations and calling g_1038b070 per import/reloc entry over the unpacked image; sets g_103a24e8 error, angr-mangled EH control flow. |
| `0x1031cf6d` | `sub_1031cf6d` | 1 | trivial accessor/forwarder |
| `0x1031cfb5` | `sub_1031cfb5` | 1 | trivial accessor/forwarder |
| `0x1031cfc9` | `sub_1031cfc9` | 36 | support routine (36 bytes) |
| `0x1031cfcd` | `sub_1031cfcd` | 2 | trivial accessor/forwarder |
| `0x1031cfcf` | `sub_1031cfcf` | 1 | trivial accessor/forwarder |
| `0x1031d024` | `sub_1031d024` | 1 | trivial accessor/forwarder |
| `0x1031d059` | `sub_1031d059` | 1 | trivial accessor/forwarder |
| `0x1031d0c6` | `sub_1031d0c6` | 1 | trivial accessor/forwarder |
| `0x1031d0da` | `sub_1031d0da` | 126 | support routine (126 bytes) |
| `0x1031d0de` | `sub_1031d0de` | 2 | trivial accessor/forwarder |
| `0x1031d0e0` | `sub_1031d0e0` | 1 | trivial accessor/forwarder |
| `0x1031d100` | `sub_1031d100` | 1 | trivial accessor/forwarder |
| `0x1031d133` | `sub_1031d133` | 1 | trivial accessor/forwarder |
| `0x1031d13a` | `sub_1031d13a` | 3 | trivial accessor/forwarder |
| `0x1031d160` | `sub_1031d160` | 8 | trivial accessor/forwarder |
| `0x1031d168` | `sub_1031d168` | 27 | support routine (27 bytes) |
| `0x1031d183` | `sub_1031d183` | 4 | trivial accessor/forwarder |
| `0x1031d189` | `sub_1031d189` | 7 | trivial accessor/forwarder |
| `0x1031d2e0` | `sub_1031d2e0` | 326 | support routine (326 bytes) |
| `0x1031d430` | `resolveImportTable` | 398 | Walks import descriptor array (base a0), LoadLibrary via g_1038b080 and GetProcAddress via g_1038b078, filling IAT; sets error string g_103a24f0 on failure. |
| `0x1031d5c0` | `sub_1031d5c0` | 185 | support routine (185 bytes) |
| `0x1031d680` | `armadilloMainUnpack` | 2108 | Armadillo main unpacking/anti-debug orchestrator: mutex/pipe checks, IsDebuggerPresent, DA/RN token msgs, unpacks image, resolves imports, invokes OEP callbacks. |
| `0x1031dbed` | `sub_1031dbed` | 2 | trivial accessor/forwarder |
| `0x1031dd4f` | `sub_1031dd4f` | 3 | trivial accessor/forwarder |
| `0x1031dd85` | `sub_1031dd85` | 2 | trivial accessor/forwarder |
| `0x1031dd8d` | `sub_1031dd8d` | 1 | trivial accessor/forwarder |
| `0x1031ddb0` | `sub_1031ddb0` | 1 | trivial accessor/forwarder |
| `0x1031ddd0` | `sub_1031ddd0` | 38 | support routine (38 bytes) |
| `0x1031ddea` | `sub_1031ddea` | 1 | trivial accessor/forwarder |
| `0x1031ddfe` | `sub_1031ddfe` | 14 | trivial accessor/forwarder |
| `0x1031de02` | `sub_1031de02` | 2 | trivial accessor/forwarder |
| `0x1031de04` | `sub_1031de04` | 1 | trivial accessor/forwarder |
| `0x1031de58` | `sub_1031de58` | 72 | support routine (72 bytes) |
| `0x1031de8c` | `sub_1031de8c` | 2 | trivial accessor/forwarder |
| `0x1031df50` | `sub_1031df50` | 74 | support routine (74 bytes) |
| `0x1031dfa0` | `sub_1031dfa0` | 10 | trivial accessor/forwarder |
| `0x1031dfb0` | `sub_1031dfb0` | 182 | support routine (182 bytes) |
| `0x1031e070` | `sub_1031e070` | 40 | support routine (40 bytes) |
| `0x1031e0a0` | `dllEntryInitialize` | 290 | DLL init entry: calls INITIALIZEDLLADDR export, runs sub_1031dfb0, on success spawns _start(g_103a2234), else shows error message box via g_1038b30c. |
| `0x1031e129` | `sub_1031e129` | 2 | trivial accessor/forwarder |
| `0x1031e135` | `sub_1031e135` | 2 | trivial accessor/forwarder |
| `0x1031e13e` | `sub_1031e13e` | 2 | trivial accessor/forwarder |
| `0x1031e1b0` | `sub_1031e1b0` | 2 | trivial accessor/forwarder |
| `0x1031e1d0` | `sub_1031e1d0` | 114 | support routine (114 bytes) |
| `0x1031e250` | `sub_1031e250` | 114 | support routine (114 bytes) |
| `0x1031e2d0` | `sub_1031e2d0` | 63 | support routine (63 bytes) |
| `0x1031e310` | `sub_1031e310` | 50 | support routine (50 bytes) |
| `0x1031e350` | `sub_1031e350` | 29 | support routine (29 bytes) |
| `0x1031e370` | `sub_1031e370` | 125 | support routine (125 bytes) |
| `0x1031e3f0` | `sub_1031e3f0` | 165 | support routine (165 bytes) |
| `0x1031e4a0` | `sub_1031e4a0` | 184 | support routine (184 bytes) |
| `0x1031e560` | `sub_1031e560` | 57 | support routine (57 bytes) |
| `0x1031e5a0` | `sub_1031e5a0` | 28 | support routine (28 bytes) |
| `0x1031e5c0` | `sub_1031e5c0` | 113 | support routine (113 bytes) |
| `0x1031e640` | `sub_1031e640` | 108 | support routine (108 bytes) |
| `0x1031e6b0` | `sub_1031e6b0` | 46 | support routine (46 bytes) |
| `0x1031e6e0` | `sub_1031e6e0` | 124 | support routine (124 bytes) |
| `0x1031e760` | `sub_1031e760` | 61 | support routine (61 bytes) |
| `0x1031e7a0` | `sub_1031e7a0` | 185 | support routine (185 bytes) |
| `0x1031e860` | `sub_1031e860` | 28 | support routine (28 bytes) |
| `0x1031e880` | `sub_1031e880` | 157 | support routine (157 bytes) |
| `0x1031e920` | `sub_1031e920` | 17 | support routine (17 bytes) |
| `0x1031e940` | `sub_1031e940` | 148 | support routine (148 bytes) |
| `0x1031e9e0` | `sub_1031e9e0` | 51 | support routine (51 bytes) |
| `0x1031ea20` | `stringReserveGrow` | 285 | std::basic_string capacity-grow helper: computes new capacity (a1/7, 1.5x rule), allocates via sub_1031eba0, copies old data, updates size. |
| `0x1031ead2` | `sub_1031ead2` | 19 | support routine (19 bytes) |
| `0x1031eae5` | `sub_1031eae5` | 34 | support routine (34 bytes) |
| `0x1031eaf3` | `sub_1031eaf3` | 34 | support routine (34 bytes) |
| `0x1031eba0` | `sub_1031eba0` | 27 | support routine (27 bytes) |
| `0x1031ebc0` | `sub_1031ebc0` | 44 | support routine (44 bytes) |
| `0x1031ebf0` | `sub_1031ebf0` | 44 | support routine (44 bytes) |
| `0x1031ec20` | `sub_1031ec20` | 76 | support routine (76 bytes) |
| `0x1031ec70` | `sub_1031ec70` | 29 | support routine (29 bytes) |
| `0x1031ec90` | `sub_1031ec90` | 32 | support routine (32 bytes) |
| `0x1031ecb0` | `sub_1031ecb0` | 33 | support routine (33 bytes) |
| `0x1031ece0` | `sub_1031ece0` | 133 | support routine (133 bytes) |
| `0x1031ed70` | `sub_1031ed70` | 83 | support routine (83 bytes) |
| `0x1031edd0` | `sub_1031edd0` | 574 | support routine (574 bytes) |
| `0x1031f010` | `sub_1031f010` | 120 | support routine (120 bytes) |
| `0x1031f090` | `loadBmpToDIBSection` | 889 | Parses a BMP (magic 0x4D42), builds BITMAPINFO/palette, creates a GDI DIB/logical-palette (g_1038b010/014/01c) and SetDIBits, returning an HBITMAP. |
| `0x1031f410` | `sub_1031f410` | 81 | support routine (81 bytes) |
| `0x1031f45b` | `sub_1031f45b` | 2 | trivial accessor/forwarder |
| `0x1031f470` | `createSplashWindow` | 312 | Creates ArBase splash/loading window: registers class, stores dims in g_103a2658/265c, optionally spins a worker thread, else calls sub_1031f591. |
| `0x1031f584` | `sub_1031f584` | 2 | trivial accessor/forwarder |
| `0x1031f591` | `splashWindowSetup` | 654 | Registers the loading-window class and CreateWindow (sub_1032b300), centers it, sets timer, stores handle in g_103a2664 under key 'LOADINGWINDOW'. |
| `0x1031f840` | `splashWindowProc` | 588 | Splash window WndProc: handles WM_PAINT (BitBlt DIB), WM_DESTROY (free bitmaps), WM_TIMER, mouse-close, forwarding others to sub_1032b700. |
| `0x1031fa90` | `sub_1031fa90` | 197 | support routine (197 bytes) |
| `0x1031fb60` | `sub_1031fb60` | 175 | support routine (175 bytes) |
| `0x1031fc10` | `sub_1031fc10` | 58 | support routine (58 bytes) |
| `0x1031fc50` | `sub_1031fc50` | 19 | support routine (19 bytes) |
| `0x1031fc70` | `sub_1031fc70` | 38 | support routine (38 bytes) |
| `0x1031fca0` | `sub_1031fca0` | 17 | support routine (17 bytes) |
| `0x1031fcc0` | `sub_1031fcc0` | 134 | support routine (134 bytes) |
| `0x1031fd50` | `sub_1031fd50` | 54 | support routine (54 bytes) |
| `0x1031fd7e` | `sub_1031fd7e` | 2 | trivial accessor/forwarder |
| `0x1031fd90` | `getSelfModulePath` | 267 | Bot wrapper: builds a temp object, if sub_1032e0a0 succeeds returns cached path else returns default global g_10390230 string. |
| `0x1031fe59` | `sub_1031fe59` | 2 | trivial accessor/forwarder |
| `0x1031fe84` | `sub_1031fe84` | 12 | trivial accessor/forwarder |
| `0x1031feb0` | `sub_1031feb0` | 165 | support routine (165 bytes) |
| `0x1031ff60` | `sub_1031ff60` | 33 | support routine (33 bytes) |
| `0x1031ff90` | `registerMemoryRegion` | 268 | Recursively splits a memory range [a1,a1+a2) at 0x1000 page boundaries and records each chunk node (copy of a3) into bucket table g_103a290c. |
| `0x103200a0` | `sub_103200a0` | 107 | support routine (107 bytes) |
| `0x103200ac` | `sub_103200ac` | 1 | trivial accessor/forwarder |
| `0x103200db` | `sub_103200db` | 1 | trivial accessor/forwarder |
| `0x103200e2` | `sub_103200e2` | 3 | trivial accessor/forwarder |
| `0x10320110` | `sub_10320110` | 50 | support routine (50 bytes) |
| `0x10320136` | `sub_10320136` | 1 | trivial accessor/forwarder |
| `0x1032014a` | `sub_1032014a` | 106 | support routine (106 bytes) |
| `0x1032014e` | `sub_1032014e` | 2 | trivial accessor/forwarder |
| `0x10320150` | `sub_10320150` | 1 | trivial accessor/forwarder |
| `0x10320186` | `sub_10320186` | 1 | trivial accessor/forwarder |
| `0x1032018d` | `sub_1032018d` | 3 | trivial accessor/forwarder |
| `0x103201bb` | `sub_103201bb` | 202 | support routine (202 bytes) |
| `0x103201eb` | `sub_103201eb` | 1 | trivial accessor/forwarder |
| `0x1032022e` | `sub_1032022e` | 1 | trivial accessor/forwarder |
| `0x1032027b` | `sub_1032027b` | 1 | trivial accessor/forwarder |
| `0x1032028f` | `sub_1032028f` | 82 | support routine (82 bytes) |
| `0x10320293` | `sub_10320293` | 2 | trivial accessor/forwarder |
| `0x10320295` | `sub_10320295` | 1 | trivial accessor/forwarder |
| `0x103202d8` | `sub_103202d8` | 1 | trivial accessor/forwarder |
| `0x103202ec` | `sub_103202ec` | 190 | support routine (190 bytes) |
| `0x103202f0` | `sub_103202f0` | 2 | trivial accessor/forwarder |
| `0x103202f2` | `sub_103202f2` | 1 | trivial accessor/forwarder |
| `0x10320338` | `sub_10320338` | 1 | trivial accessor/forwarder |
| `0x103203b0` | `sub_103203b0` | 134 | support routine (134 bytes) |
| `0x10320440` | `spawnGuardThread` | 774 | Creates a guard thread (g_1038b08c), waits on target a0, generates a random 4-14 char name, creates a hidden window (sub_1032b300) with proc sub_103207b0. |
| `0x103204c8` | `sub_103204c8` | 2 | trivial accessor/forwarder |
| `0x10320704` | `sub_10320704` | 13 | trivial accessor/forwarder |
| `0x10320711` | `sub_10320711` | 6 | trivial accessor/forwarder |
| `0x10320760` | `sub_10320760` | 17 | support routine (17 bytes) |
| `0x10320780` | `sub_10320780` | 35 | support routine (35 bytes) |
| `0x103207b0` | `guardWindowProc` | 833 | Guard/CBT window proc: on WM_DEVICECHANGE toggles page-protect flags, on close/query re-encrypts guarded pages (g_103a2910) using RNG sub_102eb870. |
| `0x103208b6` | `sub_103208b6` | 5 | trivial accessor/forwarder |
| `0x10320908` | `sub_10320908` | 2 | trivial accessor/forwarder |
| `0x10320914` | `sub_10320914` | 5 | trivial accessor/forwarder |
| `0x10320955` | `sub_10320955` | 2 | trivial accessor/forwarder |
| `0x10320961` | `sub_10320961` | 5 | trivial accessor/forwarder |
| `0x10320a50` | `sub_10320a50` | 1 | trivial accessor/forwarder |
| `0x10320a64` | `sub_10320a64` | 67 | support routine (67 bytes) |
| `0x10320a68` | `sub_10320a68` | 2 | trivial accessor/forwarder |
| `0x10320a6a` | `sub_10320a6a` | 1 | trivial accessor/forwarder |
| `0x10320b2d` | `sub_10320b2d` | 2 | trivial accessor/forwarder |
| `0x10320b60` | `sub_10320b60` | 53 | support routine (53 bytes) |
| `0x10320b8c` | `sub_10320b8c` | 2 | trivial accessor/forwarder |
| `0x10320ba0` | `sub_10320ba0` | 46 | support routine (46 bytes) |
| `0x10320bd0` | `sub_10320bd0` | 354 | support routine (354 bytes) |
| `0x10320bf5` | `sub_10320bf5` | 1 | trivial accessor/forwarder |
| `0x10320c39` | `sub_10320c39` | 1 | trivial accessor/forwarder |
| `0x10320cb9` | `sub_10320cb9` | 1 | trivial accessor/forwarder |
| `0x10320cec` | `sub_10320cec` | 1 | trivial accessor/forwarder |
| `0x10320cf3` | `sub_10320cf3` | 3 | trivial accessor/forwarder |
| `0x10320d27` | `sub_10320d27` | 1 | trivial accessor/forwarder |
| `0x10320d35` | `sub_10320d35` | 38 | support routine (38 bytes) |
| `0x10320d4f` | `sub_10320d4f` | 1 | trivial accessor/forwarder |
| `0x10320d63` | `sub_10320d63` | 28 | support routine (28 bytes) |
| `0x10320d67` | `sub_10320d67` | 2 | trivial accessor/forwarder |
| `0x10320d69` | `sub_10320d69` | 1 | trivial accessor/forwarder |
| `0x10320d90` | `sub_10320d90` | 75 | support routine (75 bytes) |
| `0x10320ddb` | `sub_10320ddb` | 55 | support routine (55 bytes) |
| `0x10320dfe` | `sub_10320dfe` | 12 | trivial accessor/forwarder |
| `0x10320e0a` | `sub_10320e0a` | 24 | support routine (24 bytes) |
| `0x10320e22` | `sub_10320e22` | 7 | trivial accessor/forwarder |
| `0x10320e40` | `sub_10320e40` | 148 | support routine (148 bytes) |
| `0x10320e92` | `sub_10320e92` | 1 | trivial accessor/forwarder |
| `0x10320e99` | `sub_10320e99` | 3 | trivial accessor/forwarder |
| `0x10320ec6` | `sub_10320ec6` | 1 | trivial accessor/forwarder |
| `0x10320edb` | `sub_10320edb` | 170 | support routine (170 bytes) |
| `0x10320ef9` | `sub_10320ef9` | 1 | trivial accessor/forwarder |
| `0x10320f5b` | `sub_10320f5b` | 1 | trivial accessor/forwarder |
| `0x10320f74` | `sub_10320f74` | 135 | support routine (135 bytes) |
| `0x10320fef` | `sub_10320fef` | 1 | trivial accessor/forwarder |
| `0x10321003` | `sub_10321003` | 62 | support routine (62 bytes) |
| `0x10321007` | `sub_10321007` | 2 | trivial accessor/forwarder |
| `0x10321009` | `sub_10321009` | 1 | trivial accessor/forwarder |
| `0x10321030` | `sub_10321030` | 1 | trivial accessor/forwarder |
| `0x10321050` | `sub_10321050` | 1678 | support routine (1678 bytes) |
| `0x10321059` | `sub_10321059` | 1 | trivial accessor/forwarder |
| `0x103210bc` | `sub_103210bc` | 1 | trivial accessor/forwarder |
| `0x103210c3` | `sub_103210c3` | 3 | trivial accessor/forwarder |
| `0x10321114` | `sub_10321114` | 1 | trivial accessor/forwarder |
| `0x1032112a` | `sub_1032112a` | 17 | support routine (17 bytes) |
| `0x1032113b` | `sub_1032113b` | 19 | support routine (19 bytes) |
| `0x1032114e` | `sub_1032114e` | 108 | support routine (108 bytes) |
| `0x10321189` | `sub_10321189` | 1 | trivial accessor/forwarder |
| `0x10321190` | `sub_10321190` | 3 | trivial accessor/forwarder |
| `0x103211be` | `sub_103211be` | 90 | support routine (90 bytes) |
| `0x10321222` | `sub_10321222` | 1 | trivial accessor/forwarder |
| `0x10321236` | `sub_10321236` | 45 | support routine (45 bytes) |
| `0x1032123a` | `sub_1032123a` | 2 | trivial accessor/forwarder |
| `0x1032123c` | `sub_1032123c` | 1 | trivial accessor/forwarder |
| `0x10321262` | `sub_10321262` | 1 | trivial accessor/forwarder |
| `0x10321279` | `sub_10321279` | 1 | trivial accessor/forwarder |
| `0x10321292` | `sub_10321292` | 8 | trivial accessor/forwarder |
| `0x1032129b` | `sub_1032129b` | 18 | support routine (18 bytes) |
| `0x103212ad` | `sub_103212ad` | 2 | trivial accessor/forwarder |
| `0x103212b7` | `guardedPageFaultHandler` | 679 | Page-fault/guard handler: maps faulting address to page index, decrypts/re-maps the page from encrypted table g_103a2910, angr-mangled control flow. |
| `0x103212f7` | `sub_103212f7` | 1 | trivial accessor/forwarder |
| `0x103212fe` | `sub_103212fe` | 3 | trivial accessor/forwarder |
| `0x10321395` | `sub_10321395` | 19 | support routine (19 bytes) |
| `0x103213c7` | `sub_103213c7` | 1 | trivial accessor/forwarder |
| `0x103213db` | `sub_103213db` | 146 | support routine (146 bytes) |
| `0x103213df` | `sub_103213df` | 2 | trivial accessor/forwarder |
| `0x103213e1` | `sub_103213e1` | 1 | trivial accessor/forwarder |
| `0x10321466` | `sub_10321466` | 19 | support routine (19 bytes) |
| `0x1032147f` | `sub_1032147f` | 1 | trivial accessor/forwarder |
| `0x10321602` | `sub_10321602` | 1 | trivial accessor/forwarder |
| `0x10321620` | `sub_10321620` | 130 | support routine (130 bytes) |
| `0x10321639` | `sub_10321639` | 1 | trivial accessor/forwarder |
| `0x10321672` | `sub_10321672` | 1 | trivial accessor/forwarder |
| `0x10321679` | `sub_10321679` | 3 | trivial accessor/forwarder |
| `0x103216a7` | `sub_103216a7` | 31 | support routine (31 bytes) |
| `0x103216d0` | `sub_103216d0` | 62 | support routine (62 bytes) |
| `0x10321704` | `sub_10321704` | 3 | trivial accessor/forwarder |
| `0x10321718` | `sub_10321718` | 14 | trivial accessor/forwarder |
| `0x1032171c` | `sub_1032171c` | 2 | trivial accessor/forwarder |
| `0x1032171e` | `sub_1032171e` | 1 | trivial accessor/forwarder |
| `0x10321754` | `sub_10321754` | 1 | trivial accessor/forwarder |
| `0x103217f1` | `sub_103217f1` | 1 | trivial accessor/forwarder |
| `0x103217f8` | `sub_103217f8` | 3 | trivial accessor/forwarder |
| `0x1032188f` | `sub_1032188f` | 19 | support routine (19 bytes) |
| `0x103218c1` | `sub_103218c1` | 1 | trivial accessor/forwarder |
| `0x103218d5` | `sub_103218d5` | 174 | support routine (174 bytes) |
| `0x103218d9` | `sub_103218d9` | 2 | trivial accessor/forwarder |
| `0x103218db` | `sub_103218db` | 1 | trivial accessor/forwarder |
| `0x10321960` | `sub_10321960` | 19 | support routine (19 bytes) |
| `0x10321985` | `sub_10321985` | 1 | trivial accessor/forwarder |
| `0x1032199e` | `sub_1032199e` | 252 | support routine (252 bytes) |
| `0x10321a6e` | `sub_10321a6e` | 1 | trivial accessor/forwarder |
| `0x10321a91` | `sub_10321a91` | 38 | support routine (38 bytes) |
| `0x10321aab` | `sub_10321aab` | 1 | trivial accessor/forwarder |
| `0x10321abf` | `sub_10321abf` | 16 | trivial accessor/forwarder |
| `0x10321ac3` | `sub_10321ac3` | 2 | trivial accessor/forwarder |
| `0x10321ac5` | `sub_10321ac5` | 1 | trivial accessor/forwarder |
| `0x10321b1f` | `sub_10321b1f` | 1 | trivial accessor/forwarder |
| `0x10321e64` | `sub_10321e64` | 1 | trivial accessor/forwarder |
| `0x10321e6b` | `sub_10321e6b` | 3 | trivial accessor/forwarder |
| `0x10321e99` | `sub_10321e99` | 172 | support routine (172 bytes) |
| `0x10321ed5` | `sub_10321ed5` | 1 | trivial accessor/forwarder |
| `0x10321ef3` | `sub_10321ef3` | 184 | support routine (184 bytes) |
| `0x10321f25` | `sub_10321f25` | 1 | trivial accessor/forwarder |
| `0x10321fac` | `sub_10321fac` | 22 | support routine (22 bytes) |
| `0x10321ff0` | `allocPageShadowTables` | 309 | Allocates per-region shadow tables (g_103a26c0/2730/2890) sized from g_103a2820 for the guarded-page subsystem, angr-mangled loop. |
| `0x1032210f` | `sub_1032210f` | 1 | trivial accessor/forwarder |
| `0x10322123` | `sub_10322123` | 436 | support routine (436 bytes) |
| `0x10322127` | `sub_10322127` | 2 | trivial accessor/forwarder |
| `0x10322129` | `sub_10322129` | 1 | trivial accessor/forwarder |
| `0x10322285` | `sub_10322285` | 1 | trivial accessor/forwarder |
| `0x1032228c` | `sub_1032228c` | 3 | trivial accessor/forwarder |
| `0x103222ba` | `sub_103222ba` | 58 | support routine (58 bytes) |
| `0x103222e1` | `sub_103222e1` | 1 | trivial accessor/forwarder |
| `0x10322317` | `sub_10322317` | 1 | trivial accessor/forwarder |
| `0x1032231e` | `sub_1032231e` | 3 | trivial accessor/forwarder |
| `0x1032234c` | `sub_1032234c` | 45 | support routine (45 bytes) |
| `0x1032236d` | `sub_1032236d` | 1 | trivial accessor/forwarder |
| `0x10322385` | `sub_10322385` | 2 | trivial accessor/forwarder |
| `0x10322397` | `sub_10322397` | 67 | support routine (67 bytes) |
| `0x103223b0` | `sub_103223b0` | 1 | trivial accessor/forwarder |
| `0x103223db` | `sub_103223db` | 57 | support routine (57 bytes) |
| `0x10322408` | `sub_10322408` | 1 | trivial accessor/forwarder |
| `0x1032241c` | `sub_1032241c` | 76 | support routine (76 bytes) |
| `0x10322420` | `sub_10322420` | 2 | trivial accessor/forwarder |
| `0x10322422` | `sub_10322422` | 1 | trivial accessor/forwarder |
| `0x1032246b` | `sub_1032246b` | 141 | support routine (141 bytes) |
| `0x1032251b` | `sub_1032251b` | 1 | trivial accessor/forwarder |
| `0x10322534` | `sub_10322534` | 507 | support routine (507 bytes) |
| `0x10322573` | `sub_10322573` | 1 | trivial accessor/forwarder |
| `0x1032257a` | `sub_1032257a` | 3 | trivial accessor/forwarder |
| `0x103225a3` | `sub_103225a3` | 1 | trivial accessor/forwarder |
| `0x1032264a` | `sub_1032264a` | 1 | trivial accessor/forwarder |
| `0x10322674` | `sub_10322674` | 5 | trivial accessor/forwarder |
| `0x1032267a` | `sub_1032267a` | 66 | support routine (66 bytes) |
| `0x103226b8` | `sub_103226b8` | 1 | trivial accessor/forwarder |
| `0x103226ea` | `sub_103226ea` | 1 | trivial accessor/forwarder |
| `0x10322731` | `sub_10322731` | 1 | trivial accessor/forwarder |
| `0x10322745` | `sub_10322745` | 14 | trivial accessor/forwarder |
| `0x10322749` | `sub_10322749` | 2 | trivial accessor/forwarder |
| `0x1032274b` | `sub_1032274b` | 1 | trivial accessor/forwarder |
| `0x10322778` | `sub_10322778` | 1 | trivial accessor/forwarder |
| `0x1032277f` | `sub_1032277f` | 3 | trivial accessor/forwarder |
| `0x103227c8` | `sub_103227c8` | 1 | trivial accessor/forwarder |
| `0x103227ee` | `sub_103227ee` | 1 | trivial accessor/forwarder |
| `0x10322843` | `guardExceptionDispatch` | 655 | Exception/message dispatcher switching on record->field_0 (2/4/5/8/9/3): re-encrypts guarded page table g_103a2910 with RNG, else sub_10322c6a/aef. |
| `0x1032286d` | `sub_1032286d` | 1 | trivial accessor/forwarder |
| `0x10322881` | `sub_10322881` | 36 | support routine (36 bytes) |
| `0x10322885` | `sub_10322885` | 2 | trivial accessor/forwarder |
| `0x10322887` | `sub_10322887` | 1 | trivial accessor/forwarder |
| `0x103228a8` | `sub_103228a8` | 34 | support routine (34 bytes) |
| `0x103228e7` | `sub_103228e7` | 1 | trivial accessor/forwarder |
| `0x103228fe` | `sub_103228fe` | 43 | support routine (43 bytes) |
| `0x10322956` | `sub_10322956` | 1 | trivial accessor/forwarder |
| `0x1032295d` | `sub_1032295d` | 3 | trivial accessor/forwarder |
| `0x103229a4` | `sub_103229a4` | 1 | trivial accessor/forwarder |
| `0x103229fc` | `sub_103229fc` | 1 | trivial accessor/forwarder |
| `0x10322a10` | `sub_10322a10` | 25 | support routine (25 bytes) |
| `0x10322a14` | `sub_10322a14` | 2 | trivial accessor/forwarder |
| `0x10322a16` | `sub_10322a16` | 1 | trivial accessor/forwarder |
| `0x10322a2c` | `sub_10322a2c` | 135 | support routine (135 bytes) |
| `0x10322aef` | `sub_10322aef` | 96 | support routine (96 bytes) |
| `0x10322b81` | `sub_10322b81` | 1 | trivial accessor/forwarder |
| `0x10322bab` | `sub_10322bab` | 1 | trivial accessor/forwarder |
| `0x10322c35` | `sub_10322c35` | 1 | trivial accessor/forwarder |
| `0x10322c3c` | `sub_10322c3c` | 3 | trivial accessor/forwarder |
| `0x10322c6a` | `sub_10322c6a` | 102 | support routine (102 bytes) |
| `0x10322c95` | `sub_10322c95` | 1 | trivial accessor/forwarder |
| `0x10322c9c` | `sub_10322c9c` | 3 | trivial accessor/forwarder |
| `0x10322cca` | `sub_10322cca` | 254 | support routine (254 bytes) |
| `0x10322d70` | `sub_10322d70` | 1 | trivial accessor/forwarder |
| `0x10322d9a` | `sub_10322d9a` | 50 | support routine (50 bytes) |
| `0x10322dce` | `sub_10322dce` | 9 | trivial accessor/forwarder |
| `0x10322dda` | `sub_10322dda` | 82 | support routine (82 bytes) |
| `0x10322e4b` | `sub_10322e4b` | 1 | trivial accessor/forwarder |
| `0x10322e5f` | `sub_10322e5f` | 27 | support routine (27 bytes) |
| `0x10322e63` | `sub_10322e63` | 2 | trivial accessor/forwarder |
| `0x10322e65` | `sub_10322e65` | 1 | trivial accessor/forwarder |
| `0x10322e7d` | `sub_10322e7d` | 95 | support routine (95 bytes) |
| `0x10322eb6` | `sub_10322eb6` | 1 | trivial accessor/forwarder |
| `0x10322ebd` | `sub_10322ebd` | 3 | trivial accessor/forwarder |
| `0x10322eeb` | `sub_10322eeb` | 5 | trivial accessor/forwarder |
| `0x10322f1d` | `sub_10322f1d` | 42 | support routine (42 bytes) |
| `0x10322f60` | `sub_10322f60` | 51 | support routine (51 bytes) |
| `0x10322f87` | `sub_10322f87` | 1 | trivial accessor/forwarder |
| `0x10322f9b` | `sub_10322f9b` | 151 | support routine (151 bytes) |
| `0x10322f9f` | `sub_10322f9f` | 2 | trivial accessor/forwarder |
| `0x10322fa1` | `sub_10322fa1` | 1 | trivial accessor/forwarder |
| `0x10322fbe` | `sub_10322fbe` | 1 | trivial accessor/forwarder |
| `0x10323006` | `sub_10323006` | 1 | trivial accessor/forwarder |
| `0x1032301a` | `sub_1032301a` | 310 | support routine (310 bytes) |
| `0x1032301e` | `sub_1032301e` | 2 | trivial accessor/forwarder |
| `0x10323020` | `sub_10323020` | 1 | trivial accessor/forwarder |
| `0x1032303d` | `sub_1032303d` | 1 | trivial accessor/forwarder |
| `0x10323064` | `sub_10323064` | 1 | trivial accessor/forwarder |
| `0x1032306b` | `sub_1032306b` | 3 | trivial accessor/forwarder |
| `0x10323099` | `sub_10323099` | 58 | support routine (58 bytes) |
| `0x103230d8` | `sub_103230d8` | 150 | support routine (150 bytes) |
| `0x103230ed` | `sub_103230ed` | 1 | trivial accessor/forwarder |
| `0x103230f4` | `sub_103230f4` | 3 | trivial accessor/forwarder |
| `0x10323142` | `sub_10323142` | 1 | trivial accessor/forwarder |
| `0x10323162` | `sub_10323162` | 46 | support routine (46 bytes) |
| `0x10323186` | `sub_10323186` | 17 | support routine (17 bytes) |
| `0x10323194` | `sub_10323194` | 1 | trivial accessor/forwarder |
| `0x103231a8` | `sub_103231a8` | 35 | support routine (35 bytes) |
| `0x103231ac` | `sub_103231ac` | 2 | trivial accessor/forwarder |
| `0x103231ae` | `sub_103231ae` | 1 | trivial accessor/forwarder |
| `0x103231ca` | `sub_103231ca` | 1 | trivial accessor/forwarder |
| `0x103231d5` | `sub_103231d5` | 1 | trivial accessor/forwarder |
| `0x103231e1` | `sub_103231e1` | 5 | trivial accessor/forwarder |
| `0x103231f8` | `sub_103231f8` | 5 | trivial accessor/forwarder |
| `0x1032320f` | `sub_1032320f` | 1 | trivial accessor/forwarder |
| `0x10323245` | `sub_10323245` | 1 | trivial accessor/forwarder |
| `0x1032324c` | `sub_1032324c` | 3 | trivial accessor/forwarder |
| `0x1032329d` | `sub_1032329d` | 1 | trivial accessor/forwarder |
| `0x103232b1` | `sub_103232b1` | 124 | support routine (124 bytes) |
| `0x103232b5` | `sub_103232b5` | 2 | trivial accessor/forwarder |
| `0x103232b7` | `sub_103232b7` | 1 | trivial accessor/forwarder |
| `0x103232f9` | `sub_103232f9` | 3 | trivial accessor/forwarder |
| `0x10323322` | `sub_10323322` | 1 | trivial accessor/forwarder |
| `0x10323335` | `sub_10323335` | 60 | support routine (60 bytes) |
| `0x10323364` | `sub_10323364` | 1 | trivial accessor/forwarder |
| `0x10323378` | `sub_10323378` | 17 | support routine (17 bytes) |
| `0x1032337c` | `sub_1032337c` | 2 | trivial accessor/forwarder |
| `0x1032337e` | `sub_1032337e` | 1 | trivial accessor/forwarder |
| `0x1032338c` | `sub_1032338c` | 73 | support routine (73 bytes) |
| `0x103233bb` | `sub_103233bb` | 1 | trivial accessor/forwarder |
| `0x103233fe` | `sub_103233fe` | 33 | support routine (33 bytes) |
| `0x10323415` | `sub_10323415` | 3 | trivial accessor/forwarder |
| `0x10323429` | `sub_10323429` | 93 | support routine (93 bytes) |
| `0x1032342d` | `sub_1032342d` | 2 | trivial accessor/forwarder |
| `0x1032342f` | `sub_1032342f` | 1 | trivial accessor/forwarder |
| `0x1032344c` | `sub_1032344c` | 1 | trivial accessor/forwarder |
| `0x10323473` | `sub_10323473` | 1 | trivial accessor/forwarder |
| `0x1032348b` | `sub_1032348b` | 102 | support routine (102 bytes) |
| `0x103234c0` | `sub_103234c0` | 1 | trivial accessor/forwarder |
| `0x103234c7` | `sub_103234c7` | 3 | trivial accessor/forwarder |
| `0x103234f5` | `sub_103234f5` | 122 | support routine (122 bytes) |
| `0x10323507` | `sub_10323507` | 1 | trivial accessor/forwarder |
| `0x1032352d` | `sub_1032352d` | 1 | trivial accessor/forwarder |
| `0x10323563` | `sub_10323563` | 1 | trivial accessor/forwarder |
| `0x10323577` | `sub_10323577` | 110 | support routine (110 bytes) |
| `0x1032357b` | `sub_1032357b` | 2 | trivial accessor/forwarder |
| `0x1032357d` | `sub_1032357d` | 1 | trivial accessor/forwarder |
| `0x103235b7` | `sub_103235b7` | 1 | trivial accessor/forwarder |
| `0x103235be` | `sub_103235be` | 3 | trivial accessor/forwarder |
| `0x103235ec` | `sub_103235ec` | 170 | support routine (170 bytes) |
| `0x10323661` | `sub_10323661` | 2 | trivial accessor/forwarder |
| `0x1032369a` | `sub_1032369a` | 68 | support routine (68 bytes) |
| `0x103236d2` | `sub_103236d2` | 1 | trivial accessor/forwarder |
| `0x103236ea` | `sub_103236ea` | 2 | trivial accessor/forwarder |
| `0x10323704` | `sub_10323704` | 2 | trivial accessor/forwarder |
| `0x10323709` | `sub_10323709` | 16 | trivial accessor/forwarder |
| `0x10323710` | `sub_10323710` | 1 | trivial accessor/forwarder |
| `0x10323730` | `sub_10323730` | 356 | support routine (356 bytes) |
| `0x1032376f` | `sub_1032376f` | 1 | trivial accessor/forwarder |
| `0x103237a2` | `sub_103237a2` | 1 | trivial accessor/forwarder |
| `0x103237d0` | `sub_103237d0` | 1 | trivial accessor/forwarder |
| `0x103237d7` | `sub_103237d7` | 3 | trivial accessor/forwarder |
| `0x10323800` | `sub_10323800` | 1 | trivial accessor/forwarder |
| `0x1032383c` | `sub_1032383c` | 1 | trivial accessor/forwarder |
| `0x10323850` | `sub_10323850` | 21 | support routine (21 bytes) |
| `0x10323854` | `sub_10323854` | 2 | trivial accessor/forwarder |
| `0x10323856` | `sub_10323856` | 1 | trivial accessor/forwarder |
| `0x1032388a` | `sub_1032388a` | 1 | trivial accessor/forwarder |
| `0x10323891` | `sub_10323891` | 3 | trivial accessor/forwarder |
| `0x103238bf` | `sub_103238bf` | 106 | support routine (106 bytes) |
| `0x103238f8` | `sub_103238f8` | 1 | trivial accessor/forwarder |
| `0x103238ff` | `sub_103238ff` | 3 | trivial accessor/forwarder |
| `0x1032392d` | `sub_1032392d` | 53 | support routine (53 bytes) |
| `0x1032393b` | `sub_1032393b` | 1 | trivial accessor/forwarder |
| `0x10323968` | `guardedPageDecryptOnAccess` | 632 | On guarded-page access, XOR-decrypts the page in place, updates flags g_103a2934, calls sub_103240bc to re-protect; heavily angr-mangled. |
| `0x10323994` | `sub_10323994` | 1 | trivial accessor/forwarder |
| `0x103239a8` | `sub_103239a8` | 21 | support routine (21 bytes) |
| `0x103239ac` | `sub_103239ac` | 2 | trivial accessor/forwarder |
| `0x103239ae` | `sub_103239ae` | 1 | trivial accessor/forwarder |
| `0x103239c6` | `sub_103239c6` | 1 | trivial accessor/forwarder |
| `0x103239e9` | `sub_103239e9` | 1 | trivial accessor/forwarder |
| `0x10323a00` | `sub_10323a00` | 122 | support routine (122 bytes) |
| `0x10323a6e` | `sub_10323a6e` | 1 | trivial accessor/forwarder |
| `0x10323a82` | `sub_10323a82` | 117 | support routine (117 bytes) |
| `0x10323a86` | `sub_10323a86` | 2 | trivial accessor/forwarder |
| `0x10323a88` | `sub_10323a88` | 1 | trivial accessor/forwarder |
| `0x10323ac9` | `sub_10323ac9` | 1 | trivial accessor/forwarder |
| `0x10323ad0` | `sub_10323ad0` | 3 | trivial accessor/forwarder |
| `0x10323afe` | `sub_10323afe` | 213 | support routine (213 bytes) |
| `0x10323b1f` | `sub_10323b1f` | 1 | trivial accessor/forwarder |
| `0x10323b4a` | `sub_10323b4a` | 1 | trivial accessor/forwarder |
| `0x10323b8c` | `sub_10323b8c` | 1 | trivial accessor/forwarder |
| `0x10323b93` | `sub_10323b93` | 3 | trivial accessor/forwarder |
| `0x10323bdd` | `sub_10323bdd` | 33 | support routine (33 bytes) |
| `0x10323bf4` | `sub_10323bf4` | 3 | trivial accessor/forwarder |
| `0x10323bf8` | `sub_10323bf8` | 1 | trivial accessor/forwarder |
| `0x10323c08` | `sub_10323c08` | 50 | support routine (50 bytes) |
| `0x10323c0c` | `sub_10323c0c` | 2 | trivial accessor/forwarder |
| `0x10323c0e` | `sub_10323c0e` | 1 | trivial accessor/forwarder |
| `0x10323c63` | `sub_10323c63` | 1 | trivial accessor/forwarder |
| `0x10323c8d` | `sub_10323c8d` | 1 | trivial accessor/forwarder |
| `0x10323c8f` | `sub_10323c8f` | 99 | support routine (99 bytes) |
| `0x10323ce6` | `sub_10323ce6` | 1 | trivial accessor/forwarder |
| `0x10323cfa` | `sub_10323cfa` | 111 | support routine (111 bytes) |
| `0x10323cfe` | `sub_10323cfe` | 2 | trivial accessor/forwarder |
| `0x10323d00` | `sub_10323d00` | 1 | trivial accessor/forwarder |
| `0x10323d46` | `sub_10323d46` | 1 | trivial accessor/forwarder |
| `0x10323d4d` | `sub_10323d4d` | 3 | trivial accessor/forwarder |
| `0x10323e04` | `sub_10323e04` | 1 | trivial accessor/forwarder |
| `0x10323e29` | `sub_10323e29` | 1 | trivial accessor/forwarder |
| `0x10323e51` | `sub_10323e51` | 22 | support routine (22 bytes) |
| `0x10323e69` | `sub_10323e69` | 107 | support routine (107 bytes) |
| `0x10323e70` | `sub_10323e70` | 3 | trivial accessor/forwarder |
| `0x10323ebc` | `sub_10323ebc` | 1 | trivial accessor/forwarder |
| `0x10323ed6` | `sub_10323ed6` | 67 | support routine (67 bytes) |
| `0x10323f0d` | `sub_10323f0d` | 1 | trivial accessor/forwarder |
| `0x10323f21` | `sub_10323f21` | 38 | support routine (38 bytes) |
| `0x10323f25` | `sub_10323f25` | 2 | trivial accessor/forwarder |
| `0x10323f27` | `sub_10323f27` | 1 | trivial accessor/forwarder |
| `0x10323f41` | `sub_10323f41` | 1 | trivial accessor/forwarder |
| `0x10323f4b` | `sub_10323f4b` | 91 | support routine (91 bytes) |
| `0x10323fcd` | `sub_10323fcd` | 1 | trivial accessor/forwarder |
| `0x10324025` | `sub_10324025` | 1 | trivial accessor/forwarder |
| `0x1032402c` | `sub_1032402c` | 3 | trivial accessor/forwarder |
| `0x1032405a` | `sub_1032405a` | 25 | support routine (25 bytes) |
| `0x103240bc` | `sub_103240bc` | 150 | support routine (150 bytes) |
| `0x103240f3` | `sub_103240f3` | 1 | trivial accessor/forwarder |
| `0x10324107` | `sub_10324107` | 21 | support routine (21 bytes) |
| `0x1032410b` | `sub_1032410b` | 2 | trivial accessor/forwarder |
| `0x1032410d` | `sub_1032410d` | 1 | trivial accessor/forwarder |
| `0x10324141` | `sub_10324141` | 1 | trivial accessor/forwarder |
| `0x10324176` | `sub_10324176` | 84 | support routine (84 bytes) |
| `0x10324195` | `sub_10324195` | 1 | trivial accessor/forwarder |
| `0x103241b0` | `sub_103241b0` | 1 | trivial accessor/forwarder |
| `0x103241d0` | `sub_103241d0` | 51 | support routine (51 bytes) |
| `0x103241f0` | `sub_103241f0` | 2 | trivial accessor/forwarder |
| `0x10324210` | `sub_10324210` | 151 | support routine (151 bytes) |
| `0x1032428e` | `sub_1032428e` | 2 | trivial accessor/forwarder |
| `0x10324295` | `sub_10324295` | 2 | trivial accessor/forwarder |
| `0x103242a4` | `sub_103242a4` | 2 | trivial accessor/forwarder |
| `0x103242b0` | `insertSortedHandle` | 358 | Inserts entry into a sorted, dynamically-growing pointer array g_103a26a0 (doubling g_103a294c), keeping order by inserting at index idx. |
| `0x10324420` | `sub_10324420` | 122 | support routine (122 bytes) |
| `0x103244a0` | `antiDebugInitAndBranch` | 312 | Anti-debug init: SetProcessShutdownParameters, GetVersion checks, sets g_103a2909/2905 guard flags, branches to sub_103255a0/10325680; angr EH noise. |
| `0x10324512` | `sub_10324512` | 1 | trivial accessor/forwarder |
| `0x10324519` | `sub_10324519` | 3 | trivial accessor/forwarder |
| `0x10324559` | `sub_10324559` | 1 | trivial accessor/forwarder |
| `0x10324598` | `sub_10324598` | 5 | trivial accessor/forwarder |
| `0x103245cc` | `sub_103245cc` | 1 | trivial accessor/forwarder |
| `0x103245e5` | `sub_103245e5` | 32 | support routine (32 bytes) |
| `0x103245ff` | `sub_103245ff` | 1 | trivial accessor/forwarder |
| `0x10324607` | `sub_10324607` | 6 | trivial accessor/forwarder |
| `0x10324613` | `sub_10324613` | 200 | support routine (200 bytes) |
| `0x10324617` | `sub_10324617` | 2 | trivial accessor/forwarder |
| `0x10324619` | `sub_10324619` | 1 | trivial accessor/forwarder |
| `0x10324657` | `sub_10324657` | 1 | trivial accessor/forwarder |
| `0x103246ae` | `sub_103246ae` | 1 | trivial accessor/forwarder |
| `0x103246b5` | `sub_103246b5` | 3 | trivial accessor/forwarder |
| `0x103246e3` | `sub_103246e3` | 142 | support routine (142 bytes) |
| `0x103246fc` | `sub_103246fc` | 1 | trivial accessor/forwarder |
| `0x10324731` | `sub_10324731` | 1 | trivial accessor/forwarder |
| `0x10324738` | `sub_10324738` | 3 | trivial accessor/forwarder |
| `0x1032477c` | `sub_1032477c` | 42 | support routine (42 bytes) |
| `0x10324793` | `sub_10324793` | 1 | trivial accessor/forwarder |
| `0x103247ad` | `sub_103247ad` | 136 | support routine (136 bytes) |
| `0x103247bb` | `sub_103247bb` | 1 | trivial accessor/forwarder |
| `0x103247e2` | `sub_103247e2` | 1 | trivial accessor/forwarder |
| `0x103247e9` | `sub_103247e9` | 3 | trivial accessor/forwarder |
| `0x1032483f` | `sub_1032483f` | 84 | support routine (84 bytes) |
| `0x10324843` | `sub_10324843` | 2 | trivial accessor/forwarder |
| `0x10324845` | `sub_10324845` | 1 | trivial accessor/forwarder |
| `0x10324860` | `sub_10324860` | 1 | trivial accessor/forwarder |
| `0x10324881` | `sub_10324881` | 1 | trivial accessor/forwarder |
| `0x103248a4` | `sub_103248a4` | 38 | support routine (38 bytes) |
| `0x103248be` | `sub_103248be` | 1 | trivial accessor/forwarder |
| `0x103248d2` | `sub_103248d2` | 105 | support routine (105 bytes) |
| `0x103248d6` | `sub_103248d6` | 2 | trivial accessor/forwarder |
| `0x103248d8` | `sub_103248d8` | 1 | trivial accessor/forwarder |
| `0x1032492f` | `sub_1032492f` | 305 | support routine (305 bytes) |
| `0x10324a2f` | `sub_10324a2f` | 1 | trivial accessor/forwarder |
| `0x10324a36` | `sub_10324a36` | 3 | trivial accessor/forwarder |
| `0x10324a64` | `allocGuardPageTables` | 301 | Allocates the guarded-page bookkeeping tables (g_103a2910/2930/2934/2938/293c/290c) sized by page count g_103a2928; angr-mangled. |
| `0x10324b85` | `sub_10324b85` | 1 | trivial accessor/forwarder |
| `0x10324b99` | `sub_10324b99` | 165 | support routine (165 bytes) |
| `0x10324b9d` | `sub_10324b9d` | 2 | trivial accessor/forwarder |
| `0x10324b9f` | `sub_10324b9f` | 1 | trivial accessor/forwarder |
| `0x10324bd6` | `sub_10324bd6` | 1 | trivial accessor/forwarder |
| `0x10324c30` | `sub_10324c30` | 1 | trivial accessor/forwarder |
| `0x10324c49` | `sub_10324c49` | 16 | trivial accessor/forwarder |
| `0x10324c5a` | `sub_10324c5a` | 3 | trivial accessor/forwarder |
| `0x10324c65` | `sub_10324c65` | 167 | support routine (167 bytes) |
| `0x10324cdb` | `sub_10324cdb` | 1 | trivial accessor/forwarder |
| `0x10324ce2` | `sub_10324ce2` | 3 | trivial accessor/forwarder |
| `0x10324d10` | `sub_10324d10` | 127 | support routine (127 bytes) |
| `0x10324d27` | `sub_10324d27` | 1 | trivial accessor/forwarder |
| `0x10324d51` | `sub_10324d51` | 1 | trivial accessor/forwarder |
| `0x10324d86` | `sub_10324d86` | 1 | trivial accessor/forwarder |
| `0x10324d9a` | `sub_10324d9a` | 296 | support routine (296 bytes) |
| `0x10324d9e` | `sub_10324d9e` | 2 | trivial accessor/forwarder |
| `0x10324da0` | `sub_10324da0` | 1 | trivial accessor/forwarder |
| `0x10324dc4` | `sub_10324dc4` | 1 | trivial accessor/forwarder |
| `0x10324e95` | `sub_10324e95` | 1 | trivial accessor/forwarder |
| `0x10324e9c` | `sub_10324e9c` | 3 | trivial accessor/forwarder |
| `0x10324eca` | `sub_10324eca` | 107 | support routine (107 bytes) |
| `0x10324f35` | `sub_10324f35` | 69 | support routine (69 bytes) |
| `0x10324f6e` | `sub_10324f6e` | 1 | trivial accessor/forwarder |
| `0x10324f82` | `sub_10324f82` | 79 | support routine (79 bytes) |
| `0x10324f86` | `sub_10324f86` | 2 | trivial accessor/forwarder |
| `0x10324f88` | `sub_10324f88` | 1 | trivial accessor/forwarder |
| `0x10324fd4` | `sub_10324fd4` | 10 | trivial accessor/forwarder |
| `0x10324fde` | `sub_10324fde` | 56 | support routine (56 bytes) |
| `0x10325030` | `readWriteProcessMemory` | 355 | Wrapper over ReadProcessMemory/WriteProcessMemory (g_1038b0c0/g_1038b0e4) on handle *a0 into g_103a2974, with SEH-style angr control flow. |
| `0x10325066` | `sub_10325066` | 1 | trivial accessor/forwarder |
| `0x103250a3` | `sub_103250a3` | 1 | trivial accessor/forwarder |
| `0x103250aa` | `sub_103250aa` | 3 | trivial accessor/forwarder |
| `0x103250d8` | `sub_103250d8` | 36 | support routine (36 bytes) |
| `0x103250e9` | `sub_103250e9` | 1 | trivial accessor/forwarder |
| `0x10325111` | `sub_10325111` | 4 | trivial accessor/forwarder |
| `0x10325116` | `sub_10325116` | 38 | support routine (38 bytes) |
| `0x10325130` | `sub_10325130` | 1 | trivial accessor/forwarder |
| `0x10325144` | `sub_10325144` | 23 | support routine (23 bytes) |
| `0x10325148` | `sub_10325148` | 2 | trivial accessor/forwarder |
| `0x1032514a` | `sub_1032514a` | 1 | trivial accessor/forwarder |
| `0x103251a7` | `sub_103251a7` | 1 | trivial accessor/forwarder |
| `0x103251ae` | `sub_103251ae` | 3 | trivial accessor/forwarder |
| `0x103251dc` | `sub_103251dc` | 43 | support routine (43 bytes) |
| `0x103251f1` | `sub_103251f1` | 1 | trivial accessor/forwarder |
| `0x10325232` | `sub_10325232` | 1 | trivial accessor/forwarder |
| `0x10325246` | `sub_10325246` | 14 | trivial accessor/forwarder |
| `0x1032524a` | `sub_1032524a` | 2 | trivial accessor/forwarder |
| `0x1032524c` | `sub_1032524c` | 1 | trivial accessor/forwarder |
| `0x10325270` | `sub_10325270` | 159 | support routine (159 bytes) |
| `0x10325310` | `runScriptFromContext` | 589 | Bot logic: builds argument/context objects (sub_1032c360/1031fd90), evaluates via sub_1032bf70 with g_1038c8ac, on success runs sub_10325546(g_103a2818). |
| `0x10325535` | `sub_10325535` | 2 | trivial accessor/forwarder |
| `0x10325546` | `sub_10325546` | 58 | support routine (58 bytes) |
| `0x103255a0` | `sub_103255a0` | 144 | support routine (144 bytes) |
| `0x10325630` | `sub_10325630` | 70 | support routine (70 bytes) |
| `0x10325680` | `sub_10325680` | 94 | support routine (94 bytes) |
| `0x103256e0` | `sub_103256e0` | 92 | support routine (92 bytes) |
| `0x10325740` | `sub_10325740` | 92 | support routine (92 bytes) |
| `0x103257a0` | `sub_103257a0` | 44 | support routine (44 bytes) |
| `0x103257d0` | `sub_103257d0` | 75 | support routine (75 bytes) |
| `0x10325820` | `sub_10325820` | 84 | support routine (84 bytes) |
| `0x10325880` | `sub_10325880` | 84 | support routine (84 bytes) |
| `0x103258e0` | `sub_103258e0` | 30 | support routine (30 bytes) |
| `0x10325900` | `sub_10325900` | 34 | support routine (34 bytes) |
| `0x10325930` | `sub_10325930` | 144 | support routine (144 bytes) |
| `0x103259c0` | `sub_103259c0` | 153 | support routine (153 bytes) |
| `0x10325a60` | `sub_10325a60` | 148 | support routine (148 bytes) |
| `0x10325b00` | `sub_10325b00` | 31 | support routine (31 bytes) |
| `0x10325b20` | `sub_10325b20` | 103 | support routine (103 bytes) |
| `0x10325b90` | `sub_10325b90` | 66 | support routine (66 bytes) |
| `0x10325be0` | `sub_10325be0` | 25 | support routine (25 bytes) |
| `0x10325c00` | `sub_10325c00` | 220 | support routine (220 bytes) |
| `0x10325cc2` | `sub_10325cc2` | 2 | trivial accessor/forwarder |
| `0x10325ce0` | `sub_10325ce0` | 26 | support routine (26 bytes) |
| `0x10325d00` | `sub_10325d00` | 25 | support routine (25 bytes) |
| `0x10325d20` | `sub_10325d20` | 85 | support routine (85 bytes) |
| `0x10325d80` | `resolvePathString` | 327 | Bot string helper: if input starts with '/' resolves via sub_10326120 else via sub_10325b20, assigns result to output string a1. |
| `0x10325ed0` | `sub_10325ed0` | 43 | support routine (43 bytes) |
| `0x10325f00` | `sub_10325f00` | 103 | support routine (103 bytes) |
| `0x10325f70` | `sub_10325f70` | 28 | support routine (28 bytes) |
| `0x10325f90` | `sub_10325f90` | 112 | support routine (112 bytes) |
| `0x10326000` | `sub_10326000` | 80 | support routine (80 bytes) |
| `0x10326050` | `sub_10326050` | 26 | support routine (26 bytes) |
| `0x10326070` | `sub_10326070` | 55 | support routine (55 bytes) |
| `0x103260b0` | `sub_103260b0` | 53 | support routine (53 bytes) |
| `0x103260f0` | `sub_103260f0` | 45 | support routine (45 bytes) |
| `0x10326120` | `sub_10326120` | 63 | support routine (63 bytes) |
| `0x10326160` | `sub_10326160` | 46 | support routine (46 bytes) |
| `0x10326190` | `sub_10326190` | 19 | support routine (19 bytes) |
| `0x103261b0` | `sub_103261b0` | 57 | support routine (57 bytes) |
| `0x103261f0` | `sub_103261f0` | 79 | support routine (79 bytes) |
| `0x10326240` | `sub_10326240` | 32 | support routine (32 bytes) |
| `0x10326260` | `sub_10326260` | 27 | support routine (27 bytes) |
| `0x10326280` | `sub_10326280` | 72 | support routine (72 bytes) |
| `0x103262d0` | `sub_103262d0` | 28 | support routine (28 bytes) |
| `0x103262f0` | `sub_103262f0` | 93 | support routine (93 bytes) |
| `0x10326350` | `sub_10326350` | 125 | support routine (125 bytes) |
| `0x103263d0` | `sub_103263d0` | 219 | support routine (219 bytes) |
| `0x103264b0` | `sub_103264b0` | 138 | support routine (138 bytes) |
| `0x10326540` | `sub_10326540` | 31 | support routine (31 bytes) |
| `0x10326560` | `sub_10326560` | 217 | support routine (217 bytes) |
| `0x10326640` | `sub_10326640` | 28 | support routine (28 bytes) |
| `0x10326660` | `sub_10326660` | 54 | support routine (54 bytes) |
| `0x103266a0` | `sub_103266a0` | 197 | support routine (197 bytes) |
| `0x10326770` | `sub_10326770` | 197 | support routine (197 bytes) |
| `0x10326840` | `sub_10326840` | 162 | support routine (162 bytes) |
| `0x103268f0` | `sub_103268f0` | 162 | support routine (162 bytes) |
| `0x103269a0` | `sub_103269a0` | 201 | support routine (201 bytes) |
| `0x10326a70` | `pointerToStringConvert` | 436 | Converts a pointer value to its string form via cache g_103a2b3c, sub_10333e70/e90 lookups; on invalid pointer builds exception 'Can't convert invalid pointer to string'. |
| `0x10326c30` | `pointerToStringConvertVariant` | 436 | Variant of sub_10326a70 with swapped sub_10333e90/e70 order using sub_10327750, same invalid-pointer exception via g_1039c4cc. |
| `0x10326df0` | `sub_10326df0` | 128 | support routine (128 bytes) |
| `0x10326e70` | `pointerToNumericValue` | 342 | Resolves a pointer (cache g_103a2b3c) to a numeric value via sub_102ec9a0, falling back through sub_10333e70/e90/eb0 dereference. |
| `0x10326fd0` | `pointerToObjectHandle` | 342 | Resolves a pointer (cache g_103a2b3c) to an object handle via sub_1031fc50, falling back through sub_10333e90/e70/eb0. |
| `0x10327130` | `sub_10327130` | 19 | support routine (19 bytes) |
| `0x10327150` | `sub_10327150` | 19 | support routine (19 bytes) |
| `0x10327170` | `sub_10327170` | 179 | support routine (179 bytes) |
| `0x10327230` | `sub_10327230` | 179 | support routine (179 bytes) |
| `0x103272f0` | `sub_103272f0` | 179 | support routine (179 bytes) |
| `0x103273b0` | `sub_103273b0` | 19 | support routine (19 bytes) |
| `0x103273d0` | `sub_103273d0` | 19 | support routine (19 bytes) |
| `0x103273f0` | `sub_103273f0` | 19 | support routine (19 bytes) |
| `0x10327410` | `sub_10327410` | 19 | support routine (19 bytes) |
| `0x10327430` | `sub_10327430` | 95 | support routine (95 bytes) |
| `0x10327490` | `sub_10327490` | 95 | support routine (95 bytes) |
| `0x103274f0` | `sub_103274f0` | 95 | support routine (95 bytes) |
| `0x10327550` | `sub_10327550` | 95 | support routine (95 bytes) |
| `0x103275b0` | `sub_103275b0` | 64 | support routine (64 bytes) |
| `0x103275f0` | `sub_103275f0` | 64 | support routine (64 bytes) |
| `0x10327630` | `sub_10327630` | 37 | support routine (37 bytes) |
| `0x10327660` | `sub_10327660` | 228 | support routine (228 bytes) |
| `0x10327750` | `sub_10327750` | 220 | support routine (220 bytes) |
| `0x10327830` | `copyLogFontStruct` | 366 | Deep-copies a 0x44-byte LOGFONT-like struct: converts three sub-strings (fields 4/8/c) via sub_10326770/10327130 then copies remaining scalar fields. |
| `0x103279a0` | `sub_103279a0` | 193 | support routine (193 bytes) |
| `0x10327a70` | `copyStartupInfoW` | 366 | Deep-copies a STARTUPINFOW-like struct (0x44 bytes): copies 3 embedded wide strings via sub_103266a0 and re-points fields, /GS-guarded. |
| `0x10327be0` | `sub_10327be0` | 193 | support routine (193 bytes) |
| `0x10327cb0` | `sub_10327cb0` | 125 | support routine (125 bytes) |
| `0x10327d30` | `sub_10327d30` | 84 | support routine (84 bytes) |
| `0x10327d74` | `sub_10327d74` | 2 | trivial accessor/forwarder |
| `0x10327d90` | `sub_10327d90` | 162 | support routine (162 bytes) |
| `0x10327e40` | `sub_10327e40` | 30 | support routine (30 bytes) |
| `0x10327e60` | `wideToAnsiOrUtf8` | 417 | Converts a wide string to ANSI (codepage 0) or UTF-8 (65001) into out-buffer, branching on Unicode-support flag sub_10327cb0 (WideCharToMultiByte wrapper). |
| `0x10327f50` | `sub_10327f50` | 5 | trivial accessor/forwarder |
| `0x10328010` | `wideToMultibyteVariant` | 382 | Wide-to-multibyte string conversion (CP 0 vs 65001) selected by sub_10327cb0, using length from sub_102ec980 (WideCharToMultiByte thunk). |
| `0x103280e5` | `sub_103280e5` | 5 | trivial accessor/forwarder |
| `0x103281a0` | `resolveWideStringArg` | 327 | Resolves an arg to a wide/native string: if Unicode-capable (g_103a2a8c) returns direct, else converts via sub_103282f0/sub_10326a70 pipeline. |
| `0x10328221` | `sub_10328221` | 5 | trivial accessor/forwarder |
| `0x103282d9` | `sub_103282d9` | 2 | trivial accessor/forwarder |
| `0x103282f0` | `getStringViewUnicodeOrAnsi` | 286 | Extracts a string view from an object, taking the wide path (sub_10326c30) when g_103a2a8c set or the ANSI path (sub_10326a70) otherwise. |
| `0x10328395` | `sub_10328395` | 2 | trivial accessor/forwarder |
| `0x103283fe` | `sub_103283fe` | 2 | trivial accessor/forwarder |
| `0x10328400` | `sub_10328400` | 20 | support routine (20 bytes) |
| `0x10328414` | `sub_10328414` | 6 | trivial accessor/forwarder |
| `0x1032841a` | `sub_1032841a` | 9 | trivial accessor/forwarder |
| `0x10328423` | `sub_10328423` | 6 | trivial accessor/forwarder |
| `0x10328440` | `emplaceStringArgUnicodeOrAnsi` | 433 | Builds/emplaces a string argument in-place, choosing wide vs ANSI construction based on g_103a2a8c OS-Unicode flag. |
| `0x103284b7` | `sub_103284b7` | 5 | trivial accessor/forwarder |
| `0x103285e7` | `sub_103285e7` | 12 | trivial accessor/forwarder |
| `0x10328610` | `sub_10328610` | 202 | support routine (202 bytes) |
| `0x103286e0` | `sub_103286e0` | 238 | support routine (238 bytes) |
| `0x10328797` | `sub_10328797` | 2 | trivial accessor/forwarder |
| `0x103287c1` | `sub_103287c1` | 12 | trivial accessor/forwarder |
| `0x103287e0` | `getShortPathNameWrapper` | 643 | Lazily resolves GetShortPathNameW (g_103a2aac), calls it into a 260-char buffer on success else ANSI fallback pipeline; sets a0 result string. |
| `0x10328953` | `sub_10328953` | 5 | trivial accessor/forwarder |
| `0x10328a70` | `getFullPathNameWWrapper` | 258 | Calls resolved WinAPI g_1038b108 (GetFullPathNameW-style) with 3 wide-string args into 260-buffer, storing result or g_10390370 error string. |
| `0x10328b3b` | `sub_10328b3b` | 2 | trivial accessor/forwarder |
| `0x10328b65` | `sub_10328b65` | 12 | trivial accessor/forwarder |
| `0x10328b80` | `searchPathWWrapper` | 561 | Lazily resolves SearchPathW (g_103a2984/g_103a2aac), invokes it into 260-buffer with 3 args on success, else ANSI fallback via sub_10328a70. |
| `0x10328d07` | `sub_10328d07` | 5 | trivial accessor/forwarder |
| `0x10328dc0` | `sub_10328dc0` | 146 | support routine (146 bytes) |
| `0x10328e60` | `getTempPathWWrapper` | 409 | Lazily resolves GetTempPathW (g_103a298c), calls g_1038b110(260,buf) into out string, else ANSI fallback via sub_10328dc0. |
| `0x10328f5b` | `sub_10328f5b` | 5 | trivial accessor/forwarder |
| `0x10329000` | `sub_10329000` | 163 | support routine (163 bytes) |
| `0x103290b0` | `getTempFileNameWWrapper` | 472 | Lazily resolves GetTempFileNameW (g_103a2994), calls g_1038b118 with dir/prefix wide strings into 260-buffer, else ANSI fallback sub_10329000. |
| `0x103291de` | `sub_103291de` | 5 | trivial accessor/forwarder |
| `0x10329290` | `sub_10329290` | 146 | support routine (146 bytes) |
| `0x10329330` | `getWindowsDirectoryWWrapper` | 413 | Lazily resolves GetWindowsDirectoryW (g_103a299c), calls sub_1032e650 into 260-buffer, else ANSI fallback via sub_10329290. |
| `0x1032942f` | `sub_1032942f` | 5 | trivial accessor/forwarder |
| `0x103294e0` | `createFileWWrapper` | 257 | Lazily resolves CreateFileW (g_103a29a4/g_103a2aac); calls wide g_1038b120 with 7 args when Unicode+path valid, else ANSI variant. |
| `0x103295ab` | `sub_103295ab` | 2 | trivial accessor/forwarder |
| `0x103295f0` | `getFullPathNameWLongPath` | 386 | Calls WinAPI g_1038b124 into a 0x8000 wide buffer for a path arg, then post-processes result string via sub_10334130/sub_10333ff0 (long-path GetFullPathNameW). |
| `0x10329721` | `sub_10329721` | 2 | trivial accessor/forwarder |
| `0x1032975b` | `sub_1032975b` | 24 | support routine (24 bytes) |
| `0x10329790` | `getPrivateProfileStringWWrapper` | 658 | Lazily resolves GetPrivateProfileStringW (g_103a29ac); calls it into 0x8000 buffer with section/key/file wide args, else ANSI fallback sub_103295f0. |
| `0x1032992f` | `sub_1032992f` | 2 | trivial accessor/forwarder |
| `0x1032996c` | `sub_1032996c` | 29 | support routine (29 bytes) |
| `0x10329a50` | `writePrivateProfileStringWWrapper` | 391 | Lazily resolves WritePrivateProfileStringW (g_103a29b4); calls wide g_1038b1d8 with section/key/value/file, else ANSI variant sub_10326e70. |
| `0x10329b55` | `sub_10329b55` | 2 | trivial accessor/forwarder |
| `0x10329be0` | `sub_10329be0` | 194 | support routine (194 bytes) |
| `0x10329cb0` | `sub_10329cb0` | 212 | support routine (212 bytes) |
| `0x10329d90` | `sub_10329d90` | 85 | support routine (85 bytes) |
| `0x10329df0` | `sub_10329df0` | 226 | support routine (226 bytes) |
| `0x10329ea4` | `sub_10329ea4` | 2 | trivial accessor/forwarder |
| `0x10329ee0` | `getEnvironmentVariableWWrapper` | 619 | Lazily resolves GetEnvironmentVariableW (g_103a29cc); queries length then value into sized buffer, else ANSI fallback comparing default g_10390478. |
| `0x1032a01b` | `sub_1032a01b` | 2 | trivial accessor/forwarder |
| `0x1032a047` | `sub_1032a047` | 5 | trivial accessor/forwarder |
| `0x1032a0ca` | `sub_1032a0ca` | 2 | trivial accessor/forwarder |
| `0x1032a13b` | `sub_1032a13b` | 24 | support routine (24 bytes) |
| `0x1032a170` | `sub_1032a170` | 144 | support routine (144 bytes) |
| `0x1032a200` | `sub_1032a200` | 35 | support routine (35 bytes) |
| `0x1032a230` | `sub_1032a230` | 97 | support routine (97 bytes) |
| `0x1032a274` | `sub_1032a274` | 2 | trivial accessor/forwarder |
| `0x1032a2a0` | `sub_1032a2a0` | 28 | support routine (28 bytes) |
| `0x1032a2c0` | `sub_1032a2c0` | 208 | support routine (208 bytes) |
| `0x1032a366` | `sub_1032a366` | 2 | trivial accessor/forwarder |
| `0x1032a3a0` | `getWindowTextWWrapper` | 605 | Lazily resolves GetWindowTextLengthW+GetWindowTextW (g_103a29d8); gets length then text into buffer, else ANSI fallback sub_1032a2c0. |
| `0x1032a535` | `sub_1032a535` | 2 | trivial accessor/forwarder |
| `0x1032a55d` | `sub_1032a55d` | 5 | trivial accessor/forwarder |
| `0x1032a610` | `messageBoxWWrapper` | 258 | Lazily resolves MessageBoxW (g_103a29e0); calls wide sub_1032e760 with text/caption when Unicode+valid, else ANSI g_1038b30c(MessageBoxA). |
| `0x1032a6e3` | `sub_1032a6e3` | 2 | trivial accessor/forwarder |
| `0x1032a720` | `sub_1032a720` | 217 | support routine (217 bytes) |
| `0x1032a7d7` | `sub_1032a7d7` | 2 | trivial accessor/forwarder |
| `0x1032a800` | `sub_1032a800` | 95 | support routine (95 bytes) |
| `0x1032a843` | `sub_1032a843` | 2 | trivial accessor/forwarder |
| `0x1032a870` | `sub_1032a870` | 221 | support routine (221 bytes) |
| `0x1032a923` | `sub_1032a923` | 2 | trivial accessor/forwarder |
| `0x1032a950` | `getWindowTextViaMessageWrapper` | 425 | Fetches control text via WM_GETTEXTLENGTH(394)/WM_GETTEXT(393) g_1038b33c into sized buffer with sub_1032e630-gated wide handling. |
| `0x1032aa2d` | `sub_1032aa2d` | 2 | trivial accessor/forwarder |
| `0x1032aa55` | `sub_1032aa55` | 5 | trivial accessor/forwarder |
| `0x1032ab00` | `sub_1032ab00` | 226 | support routine (226 bytes) |
| `0x1032abb4` | `sub_1032abb4` | 2 | trivial accessor/forwarder |
| `0x1032abf0` | `sub_1032abf0` | 216 | support routine (216 bytes) |
| `0x1032ac9f` | `sub_1032ac9f` | 2 | trivial accessor/forwarder |
| `0x1032acd0` | `sub_1032acd0` | 101 | support routine (101 bytes) |
| `0x1032ad16` | `sub_1032ad16` | 2 | trivial accessor/forwarder |
| `0x1032ad40` | `sub_1032ad40` | 181 | support routine (181 bytes) |
| `0x1032ae00` | `getWindowTextViaWm14Wrapper` | 376 | Fetches window text via SendMessage WM_GETTEXTLENGTH(14)/WM_GETTEXT(13) into a sized buffer, wide vs ANSI gated by sub_1032e630. |
| `0x1032aed6` | `sub_1032aed6` | 5 | trivial accessor/forwarder |
| `0x1032af80` | `registerClassWWrapper` | 429 | Lazily resolves RegisterClassW (g_103a2a00/g_103a2a70); marshals WNDCLASS fields (incl. 2 wide strings) and calls g_1038b330, else stub. |
| `0x1032b130` | `registerClassExWWrapper` | 453 | Lazily resolves RegisterClassExW (g_103a2a08); marshals WNDCLASSEX fields plus 2 wide strings and calls g_1038b2a8, else stub. |
| `0x1032b300` | `createWindowExWWrapper` | 292 | Lazily resolves CreateWindowExW (g_103a2a10); calls sub_1032e9d0 with class/window wide strings + 10 args when Unicode, else ANSI g_1038b334. |
| `0x1032b3d5` | `sub_1032b3d5` | 2 | trivial accessor/forwarder |
| `0x1032b430` | `sub_1032b430` | 226 | support routine (226 bytes) |
| `0x1032b4e4` | `sub_1032b4e4` | 2 | trivial accessor/forwarder |
| `0x1032b520` | `sub_1032b520` | 241 | support routine (241 bytes) |
| `0x1032b5e3` | `sub_1032b5e3` | 2 | trivial accessor/forwarder |
| `0x1032b620` | `sub_1032b620` | 210 | support routine (210 bytes) |
| `0x1032b6cb` | `sub_1032b6cb` | 2 | trivial accessor/forwarder |
| `0x1032b700` | `sub_1032b700` | 210 | support routine (210 bytes) |
| `0x1032b7ab` | `sub_1032b7ab` | 2 | trivial accessor/forwarder |
| `0x1032b7e0` | `sub_1032b7e0` | 132 | support routine (132 bytes) |
| `0x1032b870` | `sub_1032b870` | 170 | support routine (170 bytes) |
| `0x1032b920` | `getOpenFileNameWWrapper` | 406 | Lazily resolves GetOpenFileNameW (g_103a2a40/g_103a2a90); dispatches to wide handler sub_1032cb00 with g_103a2a3c or ANSI sub_1032b7e0. |
| `0x1032ba00` | `sub_1032ba00` | 5 | trivial accessor/forwarder |
| `0x1032bac0` | `getSaveFileNameWWrapper` | 406 | Lazily resolves GetSaveFileNameW (g_103a2a48); dispatches to wide handler sub_1032cb00 with g_103a2a44 or ANSI fallback sub_1032b870. |
| `0x1032bba0` | `sub_1032bba0` | 5 | trivial accessor/forwarder |
| `0x1032bc60` | `sub_1032bc60` | 232 | support routine (232 bytes) |
| `0x1032bd50` | `getModuleFileNameWWrapper` | 528 | Lazily resolves GetModuleFileNameW (g_103a2a50); calls it into 260-buffer, stores result string or g_10390370 error, else ANSI sub_1032bc60. |
| `0x1032bebe` | `sub_1032bebe` | 5 | trivial accessor/forwarder |
| `0x1032bf70` | `createProcessWWrapper` | 878 | Lazily resolves CreateProcessW (g_103a2a58); marshals cmdline/env/dir + STARTUPINFO and calls g_1038b134 with CREATE_UNICODE flag, else ANSI path. |
| `0x1032c151` | `sub_1032c151` | 5 | trivial accessor/forwarder |
| `0x1032c2f0` | `sub_1032c2f0` | 107 | support routine (107 bytes) |
| `0x1032c360` | `getStartupInfoWWrapper` | 300 | Lazily resolves GetStartupInfoW (g_103a2a60); fills a 0x44 STARTUPINFOW via g_1038b138 then copies via sub_10327a70, else ANSI GetStartupInfoA. |
| `0x1032c43e` | `sub_1032c43e` | 2 | trivial accessor/forwarder |
| `0x1032c490` | `sub_1032c490` | 91 | support routine (91 bytes) |
| `0x1032c4f0` | `getCommandLineWWrapper` | 360 | Lazily resolves GetCommandLineW (g_103a2a68); returns its wide result as a string, else ANSI fallback via sub_1032c490. |
| `0x1032c5ba` | `sub_1032c5ba` | 5 | trivial accessor/forwarder |
| `0x1032c660` | `parseCommandLineToArgv` | 444 | Parses the command line into argv tokens: iterates chars, handling quote (0x22) and space (0x20) delimiters, building token strings (CommandLineToArgv-style). |
| `0x1032c765` | `sub_1032c765` | 2 | trivial accessor/forwarder |
| `0x1032c76b` | `sub_1032c76b` | 4 | trivial accessor/forwarder |
| `0x1032c787` | `sub_1032c787` | 2 | trivial accessor/forwarder |
| `0x1032c830` | `sub_1032c830` | 17 | support routine (17 bytes) |
| `0x1032c850` | `buildOfnStructAnsi` | 473 | Builds a 76-byte OPENFILENAMEA-style struct (filter/title/flags/default-ext ".") for ANSI open/save dialog fallback, resolving several string args. |
| `0x1032ca30` | `sub_1032ca30` | 194 | support routine (194 bytes) |
| `0x1032cb00` | `buildOfnStructWide` | 475 | Builds a 76-byte OPENFILENAMEW-style struct (wide filter/title/flags/default-ext) for the Unicode open/save-file dialog path. |
| `0x1032cce0` | `sub_1032cce0` | 194 | support routine (194 bytes) |
| `0x1032cdb0` | `sub_1032cdb0` | 59 | support routine (59 bytes) |
| `0x1032cdf0` | `sub_1032cdf0` | 59 | support routine (59 bytes) |
| `0x1032ce30` | `sub_1032ce30` | 59 | support routine (59 bytes) |
| `0x1032ce70` | `sub_1032ce70` | 59 | support routine (59 bytes) |
| `0x1032ceb0` | `sub_1032ceb0` | 59 | support routine (59 bytes) |
| `0x1032cef0` | `sub_1032cef0` | 59 | support routine (59 bytes) |
| `0x1032cf30` | `sub_1032cf30` | 59 | support routine (59 bytes) |
| `0x1032cf70` | `sub_1032cf70` | 59 | support routine (59 bytes) |
| `0x1032cfb0` | `sub_1032cfb0` | 59 | support routine (59 bytes) |
| `0x1032cff0` | `sub_1032cff0` | 59 | support routine (59 bytes) |
| `0x1032d030` | `sub_1032d030` | 59 | support routine (59 bytes) |
| `0x1032d070` | `sub_1032d070` | 59 | support routine (59 bytes) |
| `0x1032d0b0` | `sub_1032d0b0` | 59 | support routine (59 bytes) |
| `0x1032d0f0` | `sub_1032d0f0` | 59 | support routine (59 bytes) |
| `0x1032d130` | `sub_1032d130` | 59 | support routine (59 bytes) |
| `0x1032d170` | `sub_1032d170` | 59 | support routine (59 bytes) |
| `0x1032d1b0` | `sub_1032d1b0` | 59 | support routine (59 bytes) |
| `0x1032d1f0` | `sub_1032d1f0` | 59 | support routine (59 bytes) |
| `0x1032d230` | `sub_1032d230` | 59 | support routine (59 bytes) |
| `0x1032d270` | `sub_1032d270` | 59 | support routine (59 bytes) |
| `0x1032d2b0` | `sub_1032d2b0` | 59 | support routine (59 bytes) |
| `0x1032d2f0` | `sub_1032d2f0` | 59 | support routine (59 bytes) |
| `0x1032d330` | `sub_1032d330` | 59 | support routine (59 bytes) |
| `0x1032d370` | `sub_1032d370` | 59 | support routine (59 bytes) |
| `0x1032d3b0` | `sub_1032d3b0` | 59 | support routine (59 bytes) |
| `0x1032d3f0` | `sub_1032d3f0` | 59 | support routine (59 bytes) |
| `0x1032d430` | `sub_1032d430` | 59 | support routine (59 bytes) |
| `0x1032d470` | `sub_1032d470` | 108 | support routine (108 bytes) |
| `0x1032d4e0` | `sub_1032d4e0` | 99 | support routine (99 bytes) |
| `0x1032d550` | `sub_1032d550` | 44 | support routine (44 bytes) |
| `0x1032d580` | `sub_1032d580` | 115 | support routine (115 bytes) |
| `0x1032d600` | `sub_1032d600` | 143 | support routine (143 bytes) |
| `0x1032d690` | `sub_1032d690` | 17 | support routine (17 bytes) |
| `0x1032d6b0` | `sub_1032d6b0` | 17 | support routine (17 bytes) |
| `0x1032d6d0` | `sub_1032d6d0` | 149 | support routine (149 bytes) |
| `0x1032d770` | `sub_1032d770` | 17 | support routine (17 bytes) |
| `0x1032d790` | `sub_1032d790` | 17 | support routine (17 bytes) |
| `0x1032d7b0` | `sub_1032d7b0` | 92 | support routine (92 bytes) |
| `0x1032d810` | `sub_1032d810` | 92 | support routine (92 bytes) |
| `0x1032d870` | `sub_1032d870` | 149 | support routine (149 bytes) |
| `0x1032d910` | `sub_1032d910` | 114 | support routine (114 bytes) |
| `0x1032d990` | `sub_1032d990` | 136 | support routine (136 bytes) |
| `0x1032da20` | `sub_1032da20` | 136 | support routine (136 bytes) |
| `0x1032dab0` | `sub_1032dab0` | 63 | support routine (63 bytes) |
| `0x1032daf0` | `sub_1032daf0` | 37 | support routine (37 bytes) |
| `0x1032db20` | `sub_1032db20` | 51 | support routine (51 bytes) |
| `0x1032db60` | `sub_1032db60` | 19 | support routine (19 bytes) |
| `0x1032db80` | `sub_1032db80` | 92 | support routine (92 bytes) |
| `0x1032dbe0` | `sub_1032dbe0` | 75 | support routine (75 bytes) |
| `0x1032dc30` | `sub_1032dc30` | 30 | support routine (30 bytes) |
| `0x1032dc50` | `sub_1032dc50` | 19 | support routine (19 bytes) |
| `0x1032dc70` | `sub_1032dc70` | 39 | support routine (39 bytes) |
| `0x1032dca0` | `sub_1032dca0` | 36 | support routine (36 bytes) |
| `0x1032dcd0` | `sub_1032dcd0` | 91 | support routine (91 bytes) |
| `0x1032dd30` | `sub_1032dd30` | 27 | support routine (27 bytes) |
| `0x1032dd50` | `sub_1032dd50` | 99 | support routine (99 bytes) |
| `0x1032dda7` | `sub_1032dda7` | 2 | trivial accessor/forwarder |
| `0x1032ddc0` | `sub_1032ddc0` | 62 | support routine (62 bytes) |
| `0x1032de00` | `sub_1032de00` | 93 | support routine (93 bytes) |
| `0x1032de60` | `sub_1032de60` | 105 | support routine (105 bytes) |
| `0x1032ded0` | `sub_1032ded0` | 44 | support routine (44 bytes) |
| `0x1032df00` | `sub_1032df00` | 19 | support routine (19 bytes) |
| `0x1032df20` | `sub_1032df20` | 148 | support routine (148 bytes) |
| `0x1032dfc0` | `sub_1032dfc0` | 84 | support routine (84 bytes) |
| `0x1032e020` | `sub_1032e020` | 84 | support routine (84 bytes) |
| `0x1032e080` | `sub_1032e080` | 28 | support routine (28 bytes) |
| `0x1032e0a0` | `sub_1032e0a0` | 19 | support routine (19 bytes) |
| `0x1032e0c0` | `sub_1032e0c0` | 28 | support routine (28 bytes) |
| `0x1032e0e0` | `sub_1032e0e0` | 19 | support routine (19 bytes) |
| `0x1032e100` | `sub_1032e100` | 84 | support routine (84 bytes) |
| `0x1032e160` | `sub_1032e160` | 84 | support routine (84 bytes) |
| `0x1032e1c0` | `sub_1032e1c0` | 75 | support routine (75 bytes) |
| `0x1032e210` | `sub_1032e210` | 42 | support routine (42 bytes) |
| `0x1032e240` | `sub_1032e240` | 50 | support routine (50 bytes) |
| `0x1032e280` | `sub_1032e280` | 19 | support routine (19 bytes) |
| `0x1032e2a0` | `sub_1032e2a0` | 49 | support routine (49 bytes) |
| `0x1032e2e0` | `sub_1032e2e0` | 40 | support routine (40 bytes) |
| `0x1032e310` | `sub_1032e310` | 103 | support routine (103 bytes) |
| `0x1032e380` | `sub_1032e380` | 42 | support routine (42 bytes) |
| `0x1032e3b0` | `sub_1032e3b0` | 50 | support routine (50 bytes) |
| `0x1032e3f0` | `sub_1032e3f0` | 19 | support routine (19 bytes) |
| `0x1032e410` | `sub_1032e410` | 43 | support routine (43 bytes) |
| `0x1032e440` | `sub_1032e440` | 103 | support routine (103 bytes) |
| `0x1032e4b0` | `sub_1032e4b0` | 84 | support routine (84 bytes) |
| `0x1032e510` | `sub_1032e510` | 41 | support routine (41 bytes) |
| `0x1032e540` | `sub_1032e540` | 41 | support routine (41 bytes) |
| `0x1032e570` | `sub_1032e570` | 41 | support routine (41 bytes) |
| `0x1032e5a0` | `sub_1032e5a0` | 41 | support routine (41 bytes) |
| `0x1032e5d0` | `sub_1032e5d0` | 41 | support routine (41 bytes) |
| `0x1032e600` | `sub_1032e600` | 41 | support routine (41 bytes) |
| `0x1032e630` | `sub_1032e630` | 24 | support routine (24 bytes) |
| `0x1032e650` | `sub_1032e650` | 28 | support routine (28 bytes) |
| `0x1032e670` | `sub_1032e670` | 41 | support routine (41 bytes) |
| `0x1032e6a0` | `sub_1032e6a0` | 48 | support routine (48 bytes) |
| `0x1032e6d0` | `sub_1032e6d0` | 41 | support routine (41 bytes) |
| `0x1032e700` | `sub_1032e700` | 44 | support routine (44 bytes) |
| `0x1032e730` | `sub_1032e730` | 41 | support routine (41 bytes) |
| `0x1032e760` | `sub_1032e760` | 36 | support routine (36 bytes) |
| `0x1032e790` | `sub_1032e790` | 41 | support routine (41 bytes) |
| `0x1032e7c0` | `sub_1032e7c0` | 41 | support routine (41 bytes) |
| `0x1032e7f0` | `sub_1032e7f0` | 41 | support routine (41 bytes) |
| `0x1032e820` | `sub_1032e820` | 41 | support routine (41 bytes) |
| `0x1032e850` | `sub_1032e850` | 41 | support routine (41 bytes) |
| `0x1032e880` | `sub_1032e880` | 41 | support routine (41 bytes) |
| `0x1032e8b0` | `sub_1032e8b0` | 41 | support routine (41 bytes) |
| `0x1032e8e0` | `sub_1032e8e0` | 41 | support routine (41 bytes) |
| `0x1032e910` | `sub_1032e910` | 40 | support routine (40 bytes) |
| `0x1032e940` | `sub_1032e940` | 41 | support routine (41 bytes) |
| `0x1032e970` | `sub_1032e970` | 41 | support routine (41 bytes) |
| `0x1032e9a0` | `sub_1032e9a0` | 41 | support routine (41 bytes) |
| `0x1032e9d0` | `sub_1032e9d0` | 68 | support routine (68 bytes) |
| `0x1032ea20` | `sub_1032ea20` | 41 | support routine (41 bytes) |
| `0x1032ea50` | `sub_1032ea50` | 41 | support routine (41 bytes) |
| `0x1032ea80` | `sub_1032ea80` | 41 | support routine (41 bytes) |
| `0x1032eab0` | `sub_1032eab0` | 41 | support routine (41 bytes) |
| `0x1032eae0` | `sub_1032eae0` | 32 | support routine (32 bytes) |
| `0x1032eb00` | `sub_1032eb00` | 41 | support routine (41 bytes) |
| `0x1032eb30` | `sub_1032eb30` | 60 | support routine (60 bytes) |
| `0x1032eb70` | `sub_1032eb70` | 41 | support routine (41 bytes) |
| `0x1032eba0` | `sub_1032eba0` | 41 | support routine (41 bytes) |
| `0x1032ebd0` | `sub_1032ebd0` | 18 | support routine (18 bytes) |
| `0x1032ebf0` | `sub_1032ebf0` | 42 | support routine (42 bytes) |
| `0x1032ec20` | `sub_1032ec20` | 192 | support routine (192 bytes) |
| `0x1032ecc2` | `sub_1032ecc2` | 30 | support routine (30 bytes) |
| `0x1032ed00` | `sub_1032ed00` | 19 | support routine (19 bytes) |
| `0x1032ed20` | `sub_1032ed20` | 103 | support routine (103 bytes) |
| `0x1032ed90` | `sub_1032ed90` | 126 | support routine (126 bytes) |
| `0x1032ee10` | `sub_1032ee10` | 168 | support routine (168 bytes) |
| `0x1032eec0` | `sub_1032eec0` | 67 | support routine (67 bytes) |
| `0x1032ef10` | `sub_1032ef10` | 34 | support routine (34 bytes) |
| `0x1032ef40` | `sub_1032ef40` | 18 | support routine (18 bytes) |
| `0x1032ef60` | `sub_1032ef60` | 28 | support routine (28 bytes) |
| `0x1032ef80` | `tryAcquireSharedOrUpgradeLock` | 334 | Atomic reader-writer lock acquire: InterlockedCompareExchange spin on the 0x80000000 write-bit and 0x40000000 upgrade-bit with owner-id check (SRW/slim-lock). |
| `0x1032f0d0` | `sub_1032f0d0` | 98 | support routine (98 bytes) |
| `0x1032f140` | `sub_1032f140` | 20 | support routine (20 bytes) |
| `0x1032f160` | `sub_1032f160` | 127 | support routine (127 bytes) |
| `0x1032f1e0` | `sub_1032f1e0` | 10 | trivial accessor/forwarder |
| `0x1032f1f0` | `sub_1032f1f0` | 32 | support routine (32 bytes) |
| `0x1032f210` | `sub_1032f210` | 19 | support routine (19 bytes) |
| `0x1032f230` | `sub_1032f230` | 36 | support routine (36 bytes) |
| `0x1032f260` | `sub_1032f260` | 27 | support routine (27 bytes) |
| `0x1032f280` | `sub_1032f280` | 25 | support routine (25 bytes) |
| `0x1032f2a0` | `sub_1032f2a0` | 160 | support routine (160 bytes) |
| `0x1032f340` | `sub_1032f340` | 29 | support routine (29 bytes) |
| `0x1032f360` | `sub_1032f360` | 12 | trivial accessor/forwarder |
| `0x1032f370` | `sub_1032f370` | 29 | support routine (29 bytes) |
| `0x1032f390` | `sub_1032f390` | 302 | bot logic dispatcher (described in jiru-logic pass) |
| `0x1032f4e0` | `sub_1032f4e0` | 153 | support routine (153 bytes) |
| `0x1032f580` | `sub_1032f580` | 29 | support routine (29 bytes) |
| `0x1032f5a0` | `sub_1032f5a0` | 29 | support routine (29 bytes) |
| `0x1032f5c0` | `sub_1032f5c0` | 29 | support routine (29 bytes) |
| `0x1032f5e0` | `sub_1032f5e0` | 214 | support routine (214 bytes) |
| `0x1032f6c0` | `sub_1032f6c0` | 93 | support routine (93 bytes) |
| `0x1032f720` | `sub_1032f720` | 93 | support routine (93 bytes) |
| `0x1032f780` | `sub_1032f780` | 84 | support routine (84 bytes) |
| `0x1032f7e0` | `sub_1032f7e0` | 44 | support routine (44 bytes) |
| `0x1032f810` | `sub_1032f810` | 44 | support routine (44 bytes) |
| `0x1032f840` | `sub_1032f840` | 75 | support routine (75 bytes) |
| `0x1032f890` | `sub_1032f890` | 44 | support routine (44 bytes) |
| `0x1032f8c0` | `sub_1032f8c0` | 28 | support routine (28 bytes) |
| `0x1032f8e0` | `sub_1032f8e0` | 40 | support routine (40 bytes) |
| `0x1032f910` | `sub_1032f910` | 40 | support routine (40 bytes) |
| `0x1032f940` | `sub_1032f940` | 40 | support routine (40 bytes) |
| `0x1032f970` | `sub_1032f970` | 130 | support routine (130 bytes) |
| `0x1032fa10` | `sub_1032fa10` | 55 | support routine (55 bytes) |
| `0x1032fa50` | `sub_1032fa50` | 29 | support routine (29 bytes) |
| `0x1032fa70` | `sub_1032fa70` | 54 | support routine (54 bytes) |
| `0x1032fab0` | `sub_1032fab0` | 32 | support routine (32 bytes) |
| `0x1032fad0` | `sub_1032fad0` | 30 | support routine (30 bytes) |
| `0x1032faf0` | `sub_1032faf0` | 130 | support routine (130 bytes) |
| `0x1032fb90` | `sub_1032fb90` | 10 | trivial accessor/forwarder |
| `0x1032fba0` | `sub_1032fba0` | 111 | support routine (111 bytes) |
| `0x1032fc10` | `sub_1032fc10` | 10 | trivial accessor/forwarder |
| `0x1032fc20` | `sub_1032fc20` | 111 | support routine (111 bytes) |
| `0x1032fc90` | `sub_1032fc90` | 111 | support routine (111 bytes) |
| `0x1032fd00` | `sub_1032fd00` | 22 | support routine (22 bytes) |
| `0x1032fd20` | `sub_1032fd20` | 8 | trivial accessor/forwarder |
| `0x1032fd30` | `sub_1032fd30` | 22 | support routine (22 bytes) |
| `0x1032fd50` | `sub_1032fd50` | 7 | trivial accessor/forwarder |
| `0x1032fd60` | `sub_1032fd60` | 25 | support routine (25 bytes) |
| `0x1032fd80` | `sub_1032fd80` | 25 | support routine (25 bytes) |
| `0x1032fda0` | `sub_1032fda0` | 25 | support routine (25 bytes) |
| `0x1032fdc0` | `sub_1032fdc0` | 267 | bot logic dispatcher (described in jiru-logic pass) |
| `0x1032fed0` | `sub_1032fed0` | 166 | support routine (166 bytes) |
| `0x1032ff39` | `sub_1032ff39` | 2 | trivial accessor/forwarder |
| `0x1032ff80` | `sub_1032ff80` | 19 | support routine (19 bytes) |
| `0x1032ffa0` | `sub_1032ffa0` | 29 | support routine (29 bytes) |
| `0x1032ffc0` | `sub_1032ffc0` | 261 | bot logic dispatcher (described in jiru-logic pass) |
| `0x103300d0` | `sub_103300d0` | 15 | trivial accessor/forwarder |
| `0x103300e0` | `sub_103300e0` | 34 | support routine (34 bytes) |
| `0x10330110` | `sub_10330110` | 40 | support routine (40 bytes) |
| `0x10330140` | `sub_10330140` | 28 | support routine (28 bytes) |
| `0x10330160` | `sub_10330160` | 32 | support routine (32 bytes) |
| `0x10330180` | `sub_10330180` | 36 | support routine (36 bytes) |
| `0x103301b0` | `sub_103301b0` | 19 | support routine (19 bytes) |
| `0x103301d0` | `sub_103301d0` | 22 | support routine (22 bytes) |
| `0x103301f0` | `sub_103301f0` | 34 | support routine (34 bytes) |
| `0x10330220` | `sub_10330220` | 60 | support routine (60 bytes) |
| `0x10330260` | `sub_10330260` | 26 | support routine (26 bytes) |
| `0x10330280` | `sub_10330280` | 60 | support routine (60 bytes) |
| `0x103302c0` | `sub_103302c0` | 34 | support routine (34 bytes) |
| `0x103302f0` | `sub_103302f0` | 19 | support routine (19 bytes) |
| `0x10330310` | `sub_10330310` | 129 | support routine (129 bytes) |
| `0x10330376` | `sub_10330376` | 30 | support routine (30 bytes) |
| `0x103303b0` | `sub_103303b0` | 49 | support routine (49 bytes) |
| `0x103303f0` | `sub_103303f0` | 118 | support routine (118 bytes) |
| `0x10330470` | `sub_10330470` | 120 | support routine (120 bytes) |
| `0x1033049f` | `sub_1033049f` | 2 | trivial accessor/forwarder |
| `0x103304f0` | `sub_103304f0` | 100 | support routine (100 bytes) |
| `0x10330560` | `sub_10330560` | 43 | support routine (43 bytes) |
| `0x10330590` | `sub_10330590` | 129 | support routine (129 bytes) |
| `0x103305f6` | `sub_103305f6` | 30 | support routine (30 bytes) |
| `0x10330630` | `sub_10330630` | 51 | support routine (51 bytes) |
| `0x10330670` | `sub_10330670` | 35 | support routine (35 bytes) |
| `0x103306a0` | `sub_103306a0` | 51 | support routine (51 bytes) |
| `0x103306e0` | `sub_103306e0` | 118 | support routine (118 bytes) |
| `0x10330760` | `sub_10330760` | 123 | support routine (123 bytes) |
| `0x1033078f` | `sub_1033078f` | 2 | trivial accessor/forwarder |
| `0x103307e0` | `sub_103307e0` | 102 | support routine (102 bytes) |
| `0x10330850` | `sub_10330850` | 46 | support routine (46 bytes) |
| `0x10330880` | `sub_10330880` | 57 | support routine (57 bytes) |
| `0x103308c0` | `sub_103308c0` | 35 | support routine (35 bytes) |
| `0x103308f0` | `sub_103308f0` | 35 | support routine (35 bytes) |
| `0x10330920` | `sub_10330920` | 57 | support routine (57 bytes) |
| `0x10330960` | `sub_10330960` | 118 | support routine (118 bytes) |
| `0x103309e0` | `sub_103309e0` | 123 | support routine (123 bytes) |
| `0x10330a0f` | `sub_10330a0f` | 2 | trivial accessor/forwarder |
| `0x10330a60` | `sub_10330a60` | 110 | support routine (110 bytes) |
| `0x10330ad0` | `sub_10330ad0` | 46 | support routine (46 bytes) |
| `0x10330b00` | `sub_10330b00` | 93 | support routine (93 bytes) |
| `0x10330b60` | `sub_10330b60` | 198 | support routine (198 bytes) |
| `0x10330c30` | `sub_10330c30` | 41 | support routine (41 bytes) |
| `0x10330c60` | `sub_10330c60` | 23 | support routine (23 bytes) |
| `0x10330c80` | `sub_10330c80` | 13 | trivial accessor/forwarder |
| `0x10330c90` | `sub_10330c90` | 23 | support routine (23 bytes) |
| `0x10330cb0` | `sub_10330cb0` | 12 | trivial accessor/forwarder |
| `0x10330cc0` | `sub_10330cc0` | 29 | support routine (29 bytes) |
| `0x10330ce0` | `sub_10330ce0` | 29 | support routine (29 bytes) |
| `0x10330d00` | `sub_10330d00` | 29 | support routine (29 bytes) |
| `0x10330d20` | `sub_10330d20` | 70 | support routine (70 bytes) |
| `0x10330d70` | `sub_10330d70` | 97 | support routine (97 bytes) |
| `0x10330de0` | `sub_10330de0` | 10 | trivial accessor/forwarder |
| `0x10330df0` | `sub_10330df0` | 9 | trivial accessor/forwarder |
| `0x10330e00` | `sub_10330e00` | 103 | support routine (103 bytes) |
| `0x10330e70` | `sub_10330e70` | 127 | support routine (127 bytes) |
| `0x10330ef0` | `sub_10330ef0` | 10 | trivial accessor/forwarder |
| `0x10330f00` | `sub_10330f00` | 9 | trivial accessor/forwarder |
| `0x10330f10` | `sub_10330f10` | 103 | support routine (103 bytes) |
| `0x10330f80` | `sub_10330f80` | 127 | support routine (127 bytes) |
| `0x10331000` | `sub_10331000` | 44 | support routine (44 bytes) |
| `0x10331030` | `sub_10331030` | 75 | support routine (75 bytes) |
| `0x10331080` | `sub_10331080` | 10 | trivial accessor/forwarder |
| `0x10331090` | `sub_10331090` | 103 | support routine (103 bytes) |
| `0x10331100` | `sub_10331100` | 127 | support routine (127 bytes) |
| `0x10331180` | `sub_10331180` | 44 | support routine (44 bytes) |
| `0x103311b0` | `sub_103311b0` | 75 | support routine (75 bytes) |
| `0x10331200` | `sub_10331200` | 49 | support routine (49 bytes) |
| `0x10331240` | `sub_10331240` | 32 | support routine (32 bytes) |
| `0x10331260` | `sub_10331260` | 21 | support routine (21 bytes) |
| `0x10331280` | `sub_10331280` | 13 | trivial accessor/forwarder |
| `0x10331290` | `sub_10331290` | 83 | support routine (83 bytes) |
| `0x103312f0` | `sub_103312f0` | 196 | support routine (196 bytes) |
| `0x103313c0` | `sub_103313c0` | 25 | support routine (25 bytes) |
| `0x103313e0` | `sub_103313e0` | 37 | support routine (37 bytes) |
| `0x10331410` | `sub_10331410` | 35 | support routine (35 bytes) |
| `0x1033142d` | `sub_1033142d` | 2 | trivial accessor/forwarder |
| `0x10331440` | `sub_10331440` | 56 | support routine (56 bytes) |
| `0x10331480` | `sub_10331480` | 19 | support routine (19 bytes) |
| `0x103314a0` | `sub_103314a0` | 32 | support routine (32 bytes) |
| `0x103314c0` | `sub_103314c0` | 144 | support routine (144 bytes) |
| `0x10331550` | `sub_10331550` | 32 | support routine (32 bytes) |
| `0x10331570` | `sub_10331570` | 34 | support routine (34 bytes) |
| `0x103315a0` | `sub_103315a0` | 32 | support routine (32 bytes) |
| `0x103315c0` | `sub_103315c0` | 16 | trivial accessor/forwarder |
| `0x103315d0` | `sub_103315d0` | 144 | support routine (144 bytes) |
| `0x10331660` | `sub_10331660` | 35 | support routine (35 bytes) |
| `0x10331690` | `sub_10331690` | 19 | support routine (19 bytes) |
| `0x103316b0` | `sub_103316b0` | 672 | bot logic dispatcher (described in jiru-logic pass) |
| `0x103317e6` | `sub_103317e6` | 3 | trivial accessor/forwarder |
| `0x103317e9` | `sub_103317e9` | 51 | support routine (51 bytes) |
| `0x103318e9` | `sub_103318e9` | 47 | support routine (47 bytes) |
| `0x103319c0` | `sub_103319c0` | 113 | MSVC std::vector operation |
| `0x10331a40` | `sub_10331a40` | 93 | support routine (93 bytes) |
| `0x10331aa0` | `sub_10331aa0` | 84 | support routine (84 bytes) |
| `0x10331b00` | `sub_10331b00` | 44 | support routine (44 bytes) |
| `0x10331b30` | `sub_10331b30` | 19 | support routine (19 bytes) |
| `0x10331b50` | `sub_10331b50` | 707 | std::basic_string<char>::replace/_reallocate helper: grows narrow-char buffer and splices in a1..a3 chars with SEH __security_cookie frame. |
| `0x10331c88` | `sub_10331c88` | 3 | trivial accessor/forwarder |
| `0x10331c8b` | `sub_10331c8b` | 51 | support routine (51 bytes) |
| `0x10331d9a` | `sub_10331d9a` | 53 | support routine (53 bytes) |
| `0x10331e80` | `sub_10331e80` | 113 | MSVC std::vector operation |
| `0x10331f00` | `sub_10331f00` | 57 | support routine (57 bytes) |
| `0x10331f40` | `sub_10331f40` | 19 | support routine (19 bytes) |
| `0x10331f60` | `sub_10331f60` | 33 | support routine (33 bytes) |
| `0x10331f90` | `sub_10331f90` | 761 | std::basic_string<wchar_t> (28-byte element) replace/reallocate: grows wide-string buffer and inserts a3 elements with SEH cookie frame. |
| `0x103320d1` | `sub_103320d1` | 3 | trivial accessor/forwarder |
| `0x103320d4` | `sub_103320d4` | 51 | support routine (51 bytes) |
| `0x103321f4` | `sub_103321f4` | 53 | support routine (53 bytes) |
| `0x10332300` | `sub_10332300` | 113 | MSVC std::vector operation |
| `0x10332380` | `sub_10332380` | 27 | support routine (27 bytes) |
| `0x103323a0` | `sub_103323a0` | 32 | support routine (32 bytes) |
| `0x103323c0` | `sub_103323c0` | 57 | support routine (57 bytes) |
| `0x10332400` | `sub_10332400` | 25 | support routine (25 bytes) |
| `0x10332420` | `sub_10332420` | 57 | support routine (57 bytes) |
| `0x10332460` | `sub_10332460` | 25 | support routine (25 bytes) |
| `0x10332480` | `sub_10332480` | 57 | support routine (57 bytes) |
| `0x103324c0` | `sub_103324c0` | 25 | support routine (25 bytes) |
| `0x103324e0` | `sub_103324e0` | 93 | support routine (93 bytes) |
| `0x10332540` | `sub_10332540` | 84 | support routine (84 bytes) |
| `0x103325a0` | `sub_103325a0` | 25 | support routine (25 bytes) |
| `0x103325c0` | `sub_103325c0` | 70 | support routine (70 bytes) |
| `0x10332610` | `sub_10332610` | 70 | support routine (70 bytes) |
| `0x10332660` | `sub_10332660` | 62 | support routine (62 bytes) |
| `0x103326a0` | `sub_103326a0` | 9 | trivial accessor/forwarder |
| `0x103326b0` | `sub_103326b0` | 9 | trivial accessor/forwarder |
| `0x103326c0` | `sub_103326c0` | 9 | trivial accessor/forwarder |
| `0x103326d0` | `sub_103326d0` | 25 | support routine (25 bytes) |
| `0x103326f0` | `sub_103326f0` | 30 | support routine (30 bytes) |
| `0x10332710` | `sub_10332710` | 10 | trivial accessor/forwarder |
| `0x10332720` | `sub_10332720` | 16 | trivial accessor/forwarder |
| `0x10332730` | `sub_10332730` | 34 | support routine (34 bytes) |
| `0x10332760` | `sub_10332760` | 62 | support routine (62 bytes) |
| `0x103327a0` | `sub_103327a0` | 44 | support routine (44 bytes) |
| `0x103327d0` | `sub_103327d0` | 28 | support routine (28 bytes) |
| `0x103327f0` | `sub_103327f0` | 74 | support routine (74 bytes) |
| `0x10332840` | `sub_10332840` | 50 | support routine (50 bytes) |
| `0x10332880` | `sub_10332880` | 28 | support routine (28 bytes) |
| `0x103328a0` | `sub_103328a0` | 52 | support routine (52 bytes) |
| `0x103328e0` | `sub_103328e0` | 58 | support routine (58 bytes) |
| `0x10332920` | `sub_10332920` | 28 | support routine (28 bytes) |
| `0x10332940` | `sub_10332940` | 33 | support routine (33 bytes) |
| `0x10332970` | `sub_10332970` | 136 | support routine (136 bytes) |
| `0x10332a00` | `sub_10332a00` | 84 | support routine (84 bytes) |
| `0x10332a60` | `sub_10332a60` | 77 | support routine (77 bytes) |
| `0x10332ab0` | `sub_10332ab0` | 87 | support routine (87 bytes) |
| `0x10332b10` | `sub_10332b10` | 96 | support routine (96 bytes) |
| `0x10332b70` | `sub_10332b70` | 96 | support routine (96 bytes) |
| `0x10332bd0` | `sub_10332bd0` | 22 | support routine (22 bytes) |
| `0x10332bf0` | `sub_10332bf0` | 151 | support routine (151 bytes) |
| `0x10332c90` | `sub_10332c90` | 19 | support routine (19 bytes) |
| `0x10332cb0` | `sub_10332cb0` | 46 | support routine (46 bytes) |
| `0x10332ce0` | `sub_10332ce0` | 494 | boost::filesystem narrow-path normalizer: converts '/' separators to '\\', collapsing UNC/root prefixes, into a boost path string. |
| `0x10332ed0` | `sub_10332ed0` | 496 | boost::filesystem wide-path normalizer: wchar_t version of path preferred-separator conversion ('/'->'\\') with UNC handling. |
| `0x103330c0` | `sub_103330c0` | 285 | boost::filesystem::exists narrow wrapper: builds status via system call, throws boost::filesystem_error 'boost::filesystem::exists' on error. |
| `0x103331e0` | `sub_103331e0` | 34 | support routine (34 bytes) |
| `0x10333210` | `sub_10333210` | 25 | support routine (25 bytes) |
| `0x10333230` | `sub_10333230` | 52 | support routine (52 bytes) |
| `0x10333270` | `sub_10333270` | 285 | boost::filesystem::exists wide wrapper: returns bool existence, throwing filesystem_error 'boost::filesystem::exists' on failure. |
| `0x10333390` | `sub_10333390` | 267 | boost::filesystem::file_size narrow wrapper: queries file status, throws filesystem_error 'boost::filesystem::file_size' on error. |
| `0x103334a0` | `sub_103334a0` | 267 | boost::filesystem::file_size wide wrapper: wchar_t path variant throwing filesystem_error 'boost::filesystem::file_size'. |
| `0x103335b0` | `sub_103335b0` | 449 | boost::filesystem::system_complete narrow: if path relative, resolves against current_path; throws filesystem_error on error. |
| `0x10333780` | `sub_10333780` | 88 | support routine (88 bytes) |
| `0x103337e0` | `sub_103337e0` | 449 | boost::filesystem::system_complete wide: wchar_t variant resolving a relative path to an absolute complete path. |
| `0x103339b0` | `sub_103339b0` | 88 | support routine (88 bytes) |
| `0x10333a10` | `sub_10333a10` | 162 | support routine (162 bytes) |
| `0x10333ac0` | `sub_10333ac0` | 48 | support routine (48 bytes) |
| `0x10333af0` | `sub_10333af0` | 206 | support routine (206 bytes) |
| `0x10333bc0` | `sub_10333bc0` | 17 | support routine (17 bytes) |
| `0x10333be0` | `sub_10333be0` | 96 | support routine (96 bytes) |
| `0x10333c2c` | `sub_10333c2c` | 2 | trivial accessor/forwarder |
| `0x10333c60` | `sub_10333c60` | 100 | support routine (100 bytes) |
| `0x10333cd0` | `sub_10333cd0` | 162 | support routine (162 bytes) |
| `0x10333d80` | `sub_10333d80` | 93 | support routine (93 bytes) |
| `0x10333de0` | `sub_10333de0` | 33 | support routine (33 bytes) |
| `0x10333e10` | `sub_10333e10` | 28 | support routine (28 bytes) |
| `0x10333e30` | `sub_10333e30` | 28 | support routine (28 bytes) |
| `0x10333e50` | `sub_10333e50` | 28 | support routine (28 bytes) |
| `0x10333e70` | `sub_10333e70` | 30 | support routine (30 bytes) |
| `0x10333e90` | `sub_10333e90` | 30 | support routine (30 bytes) |
| `0x10333eb0` | `sub_10333eb0` | 56 | support routine (56 bytes) |
| `0x10333ef0` | `sub_10333ef0` | 69 | support routine (69 bytes) |
| `0x10333f40` | `sub_10333f40` | 69 | support routine (69 bytes) |
| `0x10333f90` | `sub_10333f90` | 82 | support routine (82 bytes) |
| `0x10333ff0` | `sub_10333ff0` | 24 | support routine (24 bytes) |
| `0x10334010` | `sub_10334010` | 47 | support routine (47 bytes) |
| `0x10334040` | `sub_10334040` | 164 | support routine (164 bytes) |
| `0x103340f0` | `sub_103340f0` | 25 | support routine (25 bytes) |
| `0x10334110` | `sub_10334110` | 24 | support routine (24 bytes) |
| `0x10334130` | `sub_10334130` | 24 | support routine (24 bytes) |
| `0x10334150` | `sub_10334150` | 48 | support routine (48 bytes) |
| `0x10334180` | `sub_10334180` | 45 | support routine (45 bytes) |
| `0x103341b0` | `sub_103341b0` | 43 | support routine (43 bytes) |
| `0x103341e0` | `sub_103341e0` | 39 | support routine (39 bytes) |
| `0x10334210` | `sub_10334210` | 19 | support routine (19 bytes) |
| `0x10334230` | `sub_10334230` | 22 | support routine (22 bytes) |
| `0x10334250` | `sub_10334250` | 69 | support routine (69 bytes) |
| `0x103342a0` | `sub_103342a0` | 73 | support routine (73 bytes) |
| `0x103342f0` | `sub_103342f0` | 45 | support routine (45 bytes) |
| `0x10334320` | `sub_10334320` | 43 | support routine (43 bytes) |
| `0x10334350` | `sub_10334350` | 22 | support routine (22 bytes) |
| `0x10334370` | `sub_10334370` | 73 | support routine (73 bytes) |
| `0x103343c0` | `sub_103343c0` | 112 | support routine (112 bytes) |
| `0x10334430` | `sub_10334430` | 20 | support routine (20 bytes) |
| `0x10334450` | `sub_10334450` | 112 | support routine (112 bytes) |
| `0x103344c0` | `sub_103344c0` | 45 | support routine (45 bytes) |
| `0x103344f0` | `sub_103344f0` | 63 | support routine (63 bytes) |
| `0x10334530` | `sub_10334530` | 5 | trivial accessor/forwarder |
| `0x10334540` | `sub_10334540` | 372 | boost::filesystem path lexical/relative-compare helper: handles root-name/root-directory edge cases then subtracts path prefix lengths. |
| `0x103346c0` | `sub_103346c0` | 106 | support routine (106 bytes) |
| `0x10334730` | `sub_10334730` | 64 | support routine (64 bytes) |
| `0x10334770` | `sub_10334770` | 64 | support routine (64 bytes) |
| `0x103347b0` | `sub_103347b0` | 64 | support routine (64 bytes) |
| `0x103347f0` | `sub_103347f0` | 162 | support routine (162 bytes) |
| `0x103348a0` | `sub_103348a0` | 162 | support routine (162 bytes) |
| `0x10334950` | `sub_10334950` | 366 | boost::filesystem path append/compare helper variant: same root-handling logic driven by cached comparison predicates. |
| `0x10334ac0` | `sub_10334ac0` | 37 | support routine (37 bytes) |
| `0x10334af0` | `sub_10334af0` | 37 | support routine (37 bytes) |
| `0x10334b20` | `sub_10334b20` | 44 | support routine (44 bytes) |
| `0x10334b50` | `sub_10334b50` | 62 | support routine (62 bytes) |
| `0x10334b90` | `sub_10334b90` | 84 | support routine (84 bytes) |
| `0x10334bf0` | `sub_10334bf0` | 37 | support routine (37 bytes) |
| `0x10334c20` | `sub_10334c20` | 43 | support routine (43 bytes) |
| `0x10334c50` | `sub_10334c50` | 97 | support routine (97 bytes) |
| `0x10334cc0` | `sub_10334cc0` | 37 | support routine (37 bytes) |
| `0x10334cf0` | `sub_10334cf0` | 43 | support routine (43 bytes) |
| `0x10334d20` | `sub_10334d20` | 97 | support routine (97 bytes) |
| `0x10334d90` | `sub_10334d90` | 51 | support routine (51 bytes) |
| `0x10334dd0` | `sub_10334dd0` | 37 | support routine (37 bytes) |
| `0x10334e00` | `sub_10334e00` | 43 | support routine (43 bytes) |
| `0x10334e30` | `sub_10334e30` | 97 | support routine (97 bytes) |
| `0x10334ea0` | `sub_10334ea0` | 77 | support routine (77 bytes) |
| `0x10334ef0` | `sub_10334ef0` | 84 | support routine (84 bytes) |
| `0x10334f50` | `sub_10334f50` | 158 | support routine (158 bytes) |
| `0x10334ff0` | `sub_10334ff0` | 148 | support routine (148 bytes) |
| `0x10335090` | `sub_10335090` | 158 | support routine (158 bytes) |
| `0x10335130` | `sub_10335130` | 148 | support routine (148 bytes) |
| `0x103351d0` | `sub_103351d0` | 93 | support routine (93 bytes) |
| `0x10335230` | `sub_10335230` | 87 | support routine (87 bytes) |
| `0x10335290` | `sub_10335290` | 16 | Boost library routine |
| `0x103352a0` | `sub_103352a0` | 75 | support routine (75 bytes) |
| `0x103352f0` | `sub_103352f0` | 93 | support routine (93 bytes) |
| `0x10335350` | `sub_10335350` | 158 | support routine (158 bytes) |
| `0x103353f0` | `sub_103353f0` | 148 | support routine (148 bytes) |
| `0x10335490` | `sub_10335490` | 93 | support routine (93 bytes) |
| `0x103354f0` | `sub_103354f0` | 158 | support routine (158 bytes) |
| `0x10335590` | `sub_10335590` | 148 | support routine (148 bytes) |
| `0x10335630` | `sub_10335630` | 93 | support routine (93 bytes) |
| `0x10335690` | `sub_10335690` | 44 | support routine (44 bytes) |
| `0x103356c0` | `sub_103356c0` | 44 | support routine (44 bytes) |
| `0x103356f0` | `sub_103356f0` | 44 | support routine (44 bytes) |
| `0x10335720` | `sub_10335720` | 44 | support routine (44 bytes) |
| `0x10335750` | `sub_10335750` | 44 | support routine (44 bytes) |
| `0x10335780` | `sub_10335780` | 44 | support routine (44 bytes) |
| `0x103357b0` | `sub_103357b0` | 44 | support routine (44 bytes) |
| `0x103357e0` | `sub_103357e0` | 44 | support routine (44 bytes) |
| `0x10335810` | `sub_10335810` | 44 | support routine (44 bytes) |
| `0x10335840` | `sub_10335840` | 47 | support routine (47 bytes) |
| `0x10335870` | `sub_10335870` | 136 | support routine (136 bytes) |
| `0x10335900` | `sub_10335900` | 88 | support routine (88 bytes) |
| `0x10335960` | `sub_10335960` | 136 | support routine (136 bytes) |
| `0x103359f0` | `sub_103359f0` | 88 | support routine (88 bytes) |
| `0x10335a50` | `sub_10335a50` | 84 | support routine (84 bytes) |
| `0x10335ab0` | `sub_10335ab0` | 84 | support routine (84 bytes) |
| `0x10335b10` | `sub_10335b10` | 24 | support routine (24 bytes) |
| `0x10335b30` | `sub_10335b30` | 33 | support routine (33 bytes) |
| `0x10335b60` | `sub_10335b60` | 99 | support routine (99 bytes) |
| `0x10335bd0` | `sub_10335bd0` | 99 | support routine (99 bytes) |
| `0x10335c40` | `sub_10335c40` | 44 | support routine (44 bytes) |
| `0x10335c70` | `sub_10335c70` | 240 | support routine (240 bytes) |
| `0x10335d3a` | `sub_10335d3a` | 24 | support routine (24 bytes) |
| `0x10335d52` | `sub_10335d52` | 6 | trivial accessor/forwarder |
| `0x10335d61` | `sub_10335d61` | 5 | trivial accessor/forwarder |
| `0x10335d90` | `sub_10335d90` | 115 | support routine (115 bytes) |
| `0x10335e10` | `sub_10335e10` | 25 | support routine (25 bytes) |
| `0x10335e30` | `sub_10335e30` | 95 | support routine (95 bytes) |
| `0x10335e90` | `sub_10335e90` | 290 | boost::system/filesystem_error what() message builder: appends ': "path1"' and ', "path2"' quoted path fragments to error stream. |
| `0x10335fa0` | `sub_10335fa0` | 19 | support routine (19 bytes) |
| `0x10335fb3` | `sub_10335fb3` | 6 | trivial accessor/forwarder |
| `0x10335fb9` | `sub_10335fb9` | 9 | trivial accessor/forwarder |
| `0x10335fc2` | `sub_10335fc2` | 3 | trivial accessor/forwarder |
| `0x10335fe0` | `sub_10335fe0` | 99 | support routine (99 bytes) |
| `0x10336050` | `sub_10336050` | 95 | support routine (95 bytes) |
| `0x103360b0` | `sub_103360b0` | 132 | support routine (132 bytes) |
| `0x10336140` | `sub_10336140` | 142 | support routine (142 bytes) |
| `0x103361d0` | `sub_103361d0` | 148 | support routine (148 bytes) |
| `0x10336270` | `sub_10336270` | 42 | support routine (42 bytes) |
| `0x103362a0` | `sub_103362a0` | 132 | support routine (132 bytes) |
| `0x10336330` | `sub_10336330` | 142 | support routine (142 bytes) |
| `0x103363c0` | `sub_103363c0` | 148 | support routine (148 bytes) |
| `0x10336460` | `sub_10336460` | 42 | support routine (42 bytes) |
| `0x10336490` | `sub_10336490` | 132 | support routine (132 bytes) |
| `0x10336520` | `sub_10336520` | 142 | support routine (142 bytes) |
| `0x103365b0` | `sub_103365b0` | 148 | support routine (148 bytes) |
| `0x10336650` | `sub_10336650` | 42 | support routine (42 bytes) |
| `0x10336680` | `sub_10336680` | 132 | support routine (132 bytes) |
| `0x10336710` | `sub_10336710` | 142 | support routine (142 bytes) |
| `0x103367a0` | `sub_103367a0` | 148 | support routine (148 bytes) |
| `0x10336840` | `sub_10336840` | 42 | support routine (42 bytes) |
| `0x10336870` | `sub_10336870` | 44 | support routine (44 bytes) |
| `0x103368a0` | `sub_103368a0` | 78 | support routine (78 bytes) |
| `0x103368f0` | `sub_103368f0` | 29 | support routine (29 bytes) |
| `0x10336910` | `sub_10336910` | 48 | support routine (48 bytes) |
| `0x10336940` | `sub_10336940` | 40 | support routine (40 bytes) |
| `0x10336970` | `sub_10336970` | 44 | support routine (44 bytes) |
| `0x103369a0` | `sub_103369a0` | 78 | support routine (78 bytes) |
| `0x103369f0` | `sub_103369f0` | 167 | support routine (167 bytes) |
| `0x10336aa0` | `sub_10336aa0` | 54 | support routine (54 bytes) |
| `0x10336ae0` | `sub_10336ae0` | 54 | support routine (54 bytes) |
| `0x10336b20` | `sub_10336b20` | 16 | trivial accessor/forwarder |
| `0x10336b30` | `sub_10336b30` | 103 | support routine (103 bytes) |
| `0x10336ba0` | `sub_10336ba0` | 48 | support routine (48 bytes) |
| `0x10336bd0` | `sub_10336bd0` | 45 | support routine (45 bytes) |
| `0x10336c00` | `sub_10336c00` | 219 | support routine (219 bytes) |
| `0x10336ce0` | `sub_10336ce0` | 246 | support routine (246 bytes) |
| `0x10336de0` | `sub_10336de0` | 231 | support routine (231 bytes) |
| `0x10336ea2` | `sub_10336ea2` | 24 | support routine (24 bytes) |
| `0x10336ee0` | `sub_10336ee0` | 123 | support routine (123 bytes) |
| `0x10336f60` | `sub_10336f60` | 28 | support routine (28 bytes) |
| `0x10336f80` | `sub_10336f80` | 162 | support routine (162 bytes) |
| `0x10337030` | `sub_10337030` | 246 | support routine (246 bytes) |
| `0x10337130` | `sub_10337130` | 231 | support routine (231 bytes) |
| `0x103371f2` | `sub_103371f2` | 24 | support routine (24 bytes) |
| `0x10337230` | `sub_10337230` | 28 | support routine (28 bytes) |
| `0x10337250` | `sub_10337250` | 162 | support routine (162 bytes) |
| `0x10337300` | `sub_10337300` | 88 | support routine (88 bytes) |
| `0x10337360` | `sub_10337360` | 88 | support routine (88 bytes) |
| `0x103373c0` | `sub_103373c0` | 88 | support routine (88 bytes) |
| `0x10337420` | `sub_10337420` | 88 | support routine (88 bytes) |
| `0x10337480` | `sub_10337480` | 172 | support routine (172 bytes) |
| `0x10337530` | `sub_10337530` | 172 | support routine (172 bytes) |
| `0x103375e0` | `sub_103375e0` | 172 | support routine (172 bytes) |
| `0x10337690` | `sub_10337690` | 39 | support routine (39 bytes) |
| `0x103376c0` | `sub_103376c0` | 39 | support routine (39 bytes) |
| `0x103376f0` | `sub_103376f0` | 30 | support routine (30 bytes) |
| `0x10337710` | `sub_10337710` | 43 | support routine (43 bytes) |
| `0x10337740` | `sub_10337740` | 45 | support routine (45 bytes) |
| `0x10337770` | `sub_10337770` | 160 | support routine (160 bytes) |
| `0x103377f5` | `sub_103377f5` | 34 | support routine (34 bytes) |
| `0x10337840` | `sub_10337840` | 24 | support routine (24 bytes) |
| `0x10337860` | `sub_10337860` | 70 | support routine (70 bytes) |
| `0x103378b0` | `sub_103378b0` | 11 | trivial accessor/forwarder |
| `0x103378c0` | `sub_103378c0` | 70 | support routine (70 bytes) |
| `0x10337910` | `sub_10337910` | 82 | support routine (82 bytes) |
| `0x10337970` | `sub_10337970` | 11 | trivial accessor/forwarder |
| `0x10337980` | `sub_10337980` | 25 | support routine (25 bytes) |
| `0x103379a0` | `sub_103379a0` | 25 | support routine (25 bytes) |
| `0x103379c0` | `sub_103379c0` | 126 | support routine (126 bytes) |
| `0x10337a25` | `sub_10337a25` | 2 | trivial accessor/forwarder |
| `0x10337a30` | `sub_10337a30` | 33 | support routine (33 bytes) |
| `0x10337a3b` | `sub_10337a3b` | 20 | support routine (20 bytes) |
| `0x10337a80` | `sub_10337a80` | 88 | support routine (88 bytes) |
| `0x10337ae0` | `sub_10337ae0` | 88 | support routine (88 bytes) |
| `0x10337b40` | `sub_10337b40` | 88 | support routine (88 bytes) |
| `0x10337ba0` | `sub_10337ba0` | 88 | support routine (88 bytes) |
| `0x10337c00` | `sub_10337c00` | 78 | support routine (78 bytes) |
| `0x10337c50` | `sub_10337c50` | 36 | support routine (36 bytes) |
| `0x10337c80` | `sub_10337c80` | 64 | support routine (64 bytes) |
| `0x10337cc0` | `sub_10337cc0` | 78 | support routine (78 bytes) |
| `0x10337d10` | `sub_10337d10` | 38 | support routine (38 bytes) |
| `0x10337d40` | `sub_10337d40` | 64 | support routine (64 bytes) |
| `0x10337d80` | `sub_10337d80` | 38 | support routine (38 bytes) |
| `0x10337db0` | `sub_10337db0` | 78 | support routine (78 bytes) |
| `0x10337e00` | `sub_10337e00` | 38 | support routine (38 bytes) |
| `0x10337e30` | `sub_10337e30` | 84 | support routine (84 bytes) |
| `0x10337e90` | `sub_10337e90` | 8 | trivial accessor/forwarder |
| `0x10337ea0` | `sub_10337ea0` | 108 | support routine (108 bytes) |
| `0x10337f10` | `sub_10337f10` | 78 | support routine (78 bytes) |
| `0x10337f60` | `sub_10337f60` | 158 | support routine (158 bytes) |
| `0x10338000` | `sub_10338000` | 148 | support routine (148 bytes) |
| `0x103380a0` | `sub_103380a0` | 115 | support routine (115 bytes) |
| `0x10338120` | `sub_10338120` | 133 | support routine (133 bytes) |
| `0x103381b0` | `sub_103381b0` | 108 | support routine (108 bytes) |
| `0x10338220` | `sub_10338220` | 78 | support routine (78 bytes) |
| `0x10338270` | `sub_10338270` | 158 | support routine (158 bytes) |
| `0x10338310` | `sub_10338310` | 148 | support routine (148 bytes) |
| `0x103383b0` | `sub_103383b0` | 115 | support routine (115 bytes) |
| `0x10338430` | `sub_10338430` | 75 | support routine (75 bytes) |
| `0x10338480` | `sub_10338480` | 75 | support routine (75 bytes) |
| `0x103384d0` | `sub_103384d0` | 75 | support routine (75 bytes) |
| `0x10338520` | `sub_10338520` | 44 | support routine (44 bytes) |
| `0x10338550` | `sub_10338550` | 44 | support routine (44 bytes) |
| `0x10338580` | `sub_10338580` | 100 | support routine (100 bytes) |
| `0x103385f0` | `sub_103385f0` | 44 | support routine (44 bytes) |
| `0x10338620` | `sub_10338620` | 26 | support routine (26 bytes) |
| `0x10338640` | `sub_10338640` | 44 | support routine (44 bytes) |
| `0x10338670` | `sub_10338670` | 44 | support routine (44 bytes) |
| `0x103386a0` | `sub_103386a0` | 100 | support routine (100 bytes) |
| `0x10338710` | `sub_10338710` | 31 | support routine (31 bytes) |
| `0x10338730` | `sub_10338730` | 31 | support routine (31 bytes) |
| `0x10338750` | `sub_10338750` | 215 | support routine (215 bytes) |
| `0x1033880d` | `sub_1033880d` | 2 | trivial accessor/forwarder |
| `0x10338830` | `sub_10338830` | 26 | support routine (26 bytes) |
| `0x10338850` | `sub_10338850` | 79 | support routine (79 bytes) |
| `0x103388a0` | `sub_103388a0` | 11 | trivial accessor/forwarder |
| `0x103388b0` | `sub_103388b0` | 180 | support routine (180 bytes) |
| `0x10338970` | `sub_10338970` | 88 | support routine (88 bytes) |
| `0x103389d0` | `sub_103389d0` | 57 | support routine (57 bytes) |
| `0x10338a10` | `sub_10338a10` | 31 | support routine (31 bytes) |
| `0x10338a30` | `sub_10338a30` | 31 | support routine (31 bytes) |
| `0x10338a50` | `sub_10338a50` | 29 | support routine (29 bytes) |
| `0x10338a70` | `sub_10338a70` | 25 | support routine (25 bytes) |
| `0x10338a90` | `sub_10338a90` | 90 | support routine (90 bytes) |
| `0x10338af0` | `sub_10338af0` | 23 | support routine (23 bytes) |
| `0x10338b10` | `sub_10338b10` | 106 | support routine (106 bytes) |
| `0x10338b80` | `sub_10338b80` | 90 | support routine (90 bytes) |
| `0x10338be0` | `sub_10338be0` | 106 | support routine (106 bytes) |
| `0x10338c50` | `sub_10338c50` | 118 | support routine (118 bytes) |
| `0x10338cd0` | `sub_10338cd0` | 194 | support routine (194 bytes) |
| `0x10338da0` | `sub_10338da0` | 118 | support routine (118 bytes) |
| `0x10338e20` | `sub_10338e20` | 194 | support routine (194 bytes) |
| `0x10338ef0` | `sub_10338ef0` | 118 | support routine (118 bytes) |
| `0x10338f70` | `sub_10338f70` | 194 | support routine (194 bytes) |
| `0x10339040` | `sub_10339040` | 118 | support routine (118 bytes) |
| `0x103390c0` | `sub_103390c0` | 194 | support routine (194 bytes) |
| `0x10339190` | `sub_10339190` | 132 | support routine (132 bytes) |
| `0x10339220` | `sub_10339220` | 142 | support routine (142 bytes) |
| `0x103392b0` | `sub_103392b0` | 148 | support routine (148 bytes) |
| `0x10339350` | `sub_10339350` | 42 | support routine (42 bytes) |
| `0x10339380` | `sub_10339380` | 132 | support routine (132 bytes) |
| `0x10339410` | `sub_10339410` | 142 | support routine (142 bytes) |
| `0x103394a0` | `sub_103394a0` | 148 | support routine (148 bytes) |
| `0x10339540` | `sub_10339540` | 42 | support routine (42 bytes) |
| `0x10339570` | `sub_10339570` | 88 | support routine (88 bytes) |
| `0x103395d0` | `sub_103395d0` | 88 | support routine (88 bytes) |
| `0x10339630` | `sub_10339630` | 88 | support routine (88 bytes) |
| `0x10339690` | `sub_10339690` | 75 | support routine (75 bytes) |
| `0x103396e0` | `sub_103396e0` | 75 | support routine (75 bytes) |
| `0x10339730` | `sub_10339730` | 210 | support routine (210 bytes) |
| `0x10339810` | `sub_10339810` | 28 | support routine (28 bytes) |
| `0x10339830` | `sub_10339830` | 27 | support routine (27 bytes) |
| `0x10339850` | `sub_10339850` | 41 | support routine (41 bytes) |
| `0x10339880` | `sub_10339880` | 47 | support routine (47 bytes) |
| `0x103398b0` | `sub_103398b0` | 97 | support routine (97 bytes) |
| `0x10339920` | `sub_10339920` | 112 | support routine (112 bytes) |
| `0x10339990` | `sub_10339990` | 88 | support routine (88 bytes) |
| `0x103399f0` | `sub_103399f0` | 88 | support routine (88 bytes) |
| `0x10339a50` | `sub_10339a50` | 112 | support routine (112 bytes) |
| `0x10339ac0` | `sub_10339ac0` | 88 | support routine (88 bytes) |
| `0x10339b20` | `sub_10339b20` | 88 | support routine (88 bytes) |
| `0x10339b80` | `sub_10339b80` | 39 | support routine (39 bytes) |
| `0x10339bb0` | `sub_10339bb0` | 108 | support routine (108 bytes) |
| `0x10339c20` | `sub_10339c20` | 39 | support routine (39 bytes) |
| `0x10339c50` | `sub_10339c50` | 39 | support routine (39 bytes) |
| `0x10339c80` | `sub_10339c80` | 52 | support routine (52 bytes) |
| `0x10339cc0` | `sub_10339cc0` | 52 | support routine (52 bytes) |
| `0x10339d00` | `sub_10339d00` | 39 | support routine (39 bytes) |
| `0x10339d30` | `sub_10339d30` | 47 | support routine (47 bytes) |
| `0x10339d60` | `sub_10339d60` | 13 | trivial accessor/forwarder |
| `0x10339d70` | `sub_10339d70` | 131 | support routine (131 bytes) |
| `0x10339dd7` | `sub_10339dd7` | 2 | trivial accessor/forwarder |
| `0x10339de2` | `sub_10339de2` | 33 | support routine (33 bytes) |
| `0x10339ded` | `sub_10339ded` | 20 | support routine (20 bytes) |
| `0x10339e30` | `sub_10339e30` | 56 | support routine (56 bytes) |
| `0x10339e70` | `sub_10339e70` | 56 | support routine (56 bytes) |
| `0x10339eb0` | `sub_10339eb0` | 29 | support routine (29 bytes) |
| `0x10339ed0` | `sub_10339ed0` | 61 | support routine (61 bytes) |
| `0x10339f10` | `sub_10339f10` | 29 | support routine (29 bytes) |
| `0x10339f30` | `sub_10339f30` | 71 | support routine (71 bytes) |
| `0x10339f80` | `sub_10339f80` | 195 | support routine (195 bytes) |
| `0x1033a008` | `sub_1033a008` | 2 | trivial accessor/forwarder |
| `0x1033a013` | `sub_1033a013` | 33 | support routine (33 bytes) |
| `0x1033a01e` | `sub_1033a01e` | 20 | support routine (20 bytes) |
| `0x1033a080` | `sub_1033a080` | 52 | support routine (52 bytes) |
| `0x1033a0c0` | `sub_1033a0c0` | 52 | support routine (52 bytes) |
| `0x1033a100` | `sub_1033a100` | 52 | support routine (52 bytes) |
| `0x1033a140` | `sub_1033a140` | 125 | support routine (125 bytes) |
| `0x1033a1c0` | `sub_1033a1c0` | 15 | trivial accessor/forwarder |
| `0x1033a1d0` | `sub_1033a1d0` | 34 | support routine (34 bytes) |
| `0x1033a200` | `sub_1033a200` | 17 | support routine (17 bytes) |
| `0x1033a220` | `sub_1033a220` | 118 | support routine (118 bytes) |
| `0x1033a2a0` | `sub_1033a2a0` | 194 | support routine (194 bytes) |
| `0x1033a370` | `sub_1033a370` | 118 | support routine (118 bytes) |
| `0x1033a3f0` | `sub_1033a3f0` | 194 | support routine (194 bytes) |
| `0x1033a4c0` | `sub_1033a4c0` | 24 | support routine (24 bytes) |
| `0x1033a4e0` | `sub_1033a4e0` | 118 | support routine (118 bytes) |
| `0x1033a560` | `sub_1033a560` | 118 | support routine (118 bytes) |
| `0x1033a5e0` | `sub_1033a5e0` | 52 | support routine (52 bytes) |
| `0x1033a620` | `sub_1033a620` | 48 | support routine (48 bytes) |
| `0x1033a650` | `sub_1033a650` | 52 | support routine (52 bytes) |
| `0x1033a690` | `sub_1033a690` | 52 | support routine (52 bytes) |
| `0x1033a6d0` | `sub_1033a6d0` | 49 | support routine (49 bytes) |
| `0x1033a710` | `sub_1033a710` | 49 | support routine (49 bytes) |
| `0x1033a750` | `sub_1033a750` | 52 | support routine (52 bytes) |
| `0x1033a790` | `sub_1033a790` | 23 | support routine (23 bytes) |
| `0x1033a7b0` | `sub_1033a7b0` | 57 | support routine (57 bytes) |
| `0x1033a7f0` | `sub_1033a7f0` | 60 | support routine (60 bytes) |
| `0x1033a830` | `sub_1033a830` | 82 | support routine (82 bytes) |
| `0x1033a890` | `sub_1033a890` | 82 | support routine (82 bytes) |
| `0x1033a8f0` | `sub_1033a8f0` | 17 | support routine (17 bytes) |
| `0x1033a910` | `sub_1033a910` | 49 | support routine (49 bytes) |
| `0x1033a950` | `sub_1033a950` | 49 | support routine (49 bytes) |
| `0x1033a990` | `sub_1033a990` | 309 | boost::filesystem path swap: fast-path swaps 7-word inline path representations, else constructs temp and swaps via string move. |
| `0x1033aad0` | `sub_1033aad0` | 58 | support routine (58 bytes) |
| `0x1033ab10` | `sub_1033ab10` | 160 | support routine (160 bytes) |
| `0x1033ab92` | `sub_1033ab92` | 34 | support routine (34 bytes) |
| `0x1033abe0` | `sub_1033abe0` | 160 | support routine (160 bytes) |
| `0x1033ac62` | `sub_1033ac62` | 34 | support routine (34 bytes) |
| `0x1033acb0` | `sub_1033acb0` | 49 | support routine (49 bytes) |
| `0x1033acf0` | `sub_1033acf0` | 49 | support routine (49 bytes) |
| `0x1033ad30` | `sub_1033ad30` | 49 | support routine (49 bytes) |
| `0x1033ad70` | `sub_1033ad70` | 720 | boost::format directive dispatcher (variant A): switches on format-spec type index 0-19 to the matching typed put/feed routine. |
| `0x1033b090` | `sub_1033b090` | 720 | boost::format directive dispatcher (variant B): type-index switch selecting typed output routine, distinct case-0/2 targets from A. |
| `0x1033b3b0` | `sub_1033b3b0` | 49 | support routine (49 bytes) |
| `0x1033b3f0` | `sub_1033b3f0` | 43 | support routine (43 bytes) |
| `0x1033b420` | `sub_1033b420` | 45 | support routine (45 bytes) |
| `0x1033b450` | `sub_1033b450` | 61 | support routine (61 bytes) |
| `0x1033b490` | `sub_1033b490` | 66 | support routine (66 bytes) |
| `0x1033b4e0` | `sub_1033b4e0` | 720 | boost::format directive dispatcher (variant C): type-index switch with cases 0-2 routing to sub_1033cb40/b70/ba0 feed routines. |
| `0x1033b800` | `sub_1033b800` | 720 | boost::format directive dispatcher (variant D): type-index switch routing cases 0-2 to sub_1033cbd0/cc00/cc30 feeders. |
| `0x1033bb20` | `sub_1033bb20` | 7 | trivial accessor/forwarder |
| `0x1033bb30` | `sub_1033bb30` | 98 | support routine (98 bytes) |
| `0x1033bba0` | `sub_1033bba0` | 43 | support routine (43 bytes) |
| `0x1033bbd0` | `sub_1033bbd0` | 20 | support routine (20 bytes) |
| `0x1033bbf0` | `sub_1033bbf0` | 57 | support routine (57 bytes) |
| `0x1033bc30` | `sub_1033bc30` | 44 | support routine (44 bytes) |
| `0x1033bc60` | `sub_1033bc60` | 26 | support routine (26 bytes) |
| `0x1033bc80` | `sub_1033bc80` | 98 | support routine (98 bytes) |
| `0x1033bcf0` | `sub_1033bcf0` | 26 | support routine (26 bytes) |
| `0x1033bd10` | `sub_1033bd10` | 44 | support routine (44 bytes) |
| `0x1033bd40` | `sub_1033bd40` | 44 | support routine (44 bytes) |
| `0x1033bd70` | `sub_1033bd70` | 75 | support routine (75 bytes) |
| `0x1033bdc0` | `sub_1033bdc0` | 75 | support routine (75 bytes) |
| `0x1033be10` | `sub_1033be10` | 50 | support routine (50 bytes) |
| `0x1033be50` | `sub_1033be50` | 50 | support routine (50 bytes) |
| `0x1033be90` | `sub_1033be90` | 720 | boost::format directive dispatcher (variant E): type-index switch routing cases 0-2 to sub_1033cda0/cdd0 feeders. |
| `0x1033c1b0` | `sub_1033c1b0` | 720 | boost::format directive dispatcher (variant F): type-index switch, case1 -> sub_1033ce10, others -> sub_1033cdd0/ce00. |
| `0x1033c4d0` | `sub_1033c4d0` | 720 | boost::format directive dispatcher (variant G): type-index switch, case2 -> sub_1033ce40, others -> sub_1033cdd0/ce00. |
| `0x1033c7f0` | `sub_1033c7f0` | 41 | support routine (41 bytes) |
| `0x1033c820` | `sub_1033c820` | 720 | boost::format directive dispatcher (variant H): type-index switch, case0 -> sub_1033c7f0, cases 1-2 -> sub_1033ce90. |
| `0x1033cb40` | `sub_1033cb40` | 41 | support routine (41 bytes) |
| `0x1033cb70` | `sub_1033cb70` | 41 | support routine (41 bytes) |
| `0x1033cba0` | `sub_1033cba0` | 41 | support routine (41 bytes) |
| `0x1033cbd0` | `sub_1033cbd0` | 41 | support routine (41 bytes) |
| `0x1033cc00` | `sub_1033cc00` | 41 | support routine (41 bytes) |
| `0x1033cc30` | `sub_1033cc30` | 41 | support routine (41 bytes) |
| `0x1033cc60` | `sub_1033cc60` | 44 | support routine (44 bytes) |
| `0x1033cc90` | `sub_1033cc90` | 44 | support routine (44 bytes) |
| `0x1033ccc0` | `sub_1033ccc0` | 105 | support routine (105 bytes) |
| `0x1033cd30` | `sub_1033cd30` | 105 | support routine (105 bytes) |
| `0x1033cda0` | `sub_1033cda0` | 41 | support routine (41 bytes) |
| `0x1033cdd0` | `sub_1033cdd0` | 41 | support routine (41 bytes) |
| `0x1033ce00` | `sub_1033ce00` | 10 | trivial accessor/forwarder |
| `0x1033ce10` | `sub_1033ce10` | 41 | support routine (41 bytes) |
| `0x1033ce40` | `sub_1033ce40` | 41 | support routine (41 bytes) |
| `0x1033ce70` | `sub_1033ce70` | 28 | support routine (28 bytes) |
| `0x1033ce90` | `sub_1033ce90` | 41 | support routine (41 bytes) |
| `0x1033cec0` | `sub_1033cec0` | 28 | support routine (28 bytes) |
| `0x1033cee0` | `sub_1033cee0` | 28 | support routine (28 bytes) |
| `0x1033cf00` | `sub_1033cf00` | 28 | support routine (28 bytes) |
| `0x1033cf20` | `sub_1033cf20` | 28 | support routine (28 bytes) |
| `0x1033cf40` | `sub_1033cf40` | 28 | support routine (28 bytes) |
| `0x1033cf60` | `sub_1033cf60` | 28 | support routine (28 bytes) |
| `0x1033cf80` | `sub_1033cf80` | 28 | support routine (28 bytes) |
| `0x1033cfa0` | `sub_1033cfa0` | 28 | support routine (28 bytes) |
| `0x1033cfc0` | `sub_1033cfc0` | 10 | trivial accessor/forwarder |
| `0x1033cfd0` | `sub_1033cfd0` | 28 | support routine (28 bytes) |
| `0x1033cff0` | `sub_1033cff0` | 28 | support routine (28 bytes) |
| `0x1033d010` | `sub_1033d010` | 27 | support routine (27 bytes) |
| `0x1033d030` | `sub_1033d030` | 27 | support routine (27 bytes) |
| `0x1033d050` | `sub_1033d050` | 28 | support routine (28 bytes) |
| `0x1033d070` | `sub_1033d070` | 25 | support routine (25 bytes) |
| `0x1033d090` | `sub_1033d090` | 27 | support routine (27 bytes) |
| `0x1033d0b0` | `sub_1033d0b0` | 27 | support routine (27 bytes) |
| `0x1033d0d0` | `sub_1033d0d0` | 44 | support routine (44 bytes) |
| `0x1033d100` | `sub_1033d100` | 44 | support routine (44 bytes) |
| `0x1033d130` | `sub_1033d130` | 44 | support routine (44 bytes) |
| `0x1033d160` | `sub_1033d160` | 25 | support routine (25 bytes) |
| `0x1033d180` | `sub_1033d180` | 27 | support routine (27 bytes) |
| `0x1033d1a0` | `sub_1033d1a0` | 27 | support routine (27 bytes) |
| `0x1033d1c0` | `sub_1033d1c0` | 27 | support routine (27 bytes) |
| `0x1033d1e0` | `sub_1033d1e0` | 27 | support routine (27 bytes) |
| `0x1033d200` | `sub_1033d200` | 100 | support routine (100 bytes) |
| `0x1033d270` | `sub_1033d270` | 187 | support routine (187 bytes) |
| `0x1033d2ff` | `sub_1033d2ff` | 61 | support routine (61 bytes) |
| `0x1033d370` | `sub_1033d370` | 187 | support routine (187 bytes) |
| `0x1033d3ff` | `sub_1033d3ff` | 61 | support routine (61 bytes) |
| `0x1033d470` | `sub_1033d470` | 27 | support routine (27 bytes) |
| `0x1033d490` | `sub_1033d490` | 29 | support routine (29 bytes) |
| `0x1033d4b0` | `sub_1033d4b0` | 29 | support routine (29 bytes) |
| `0x1033d4d0` | `sub_1033d4d0` | 15 | trivial accessor/forwarder |
| `0x1033d4e0` | `sub_1033d4e0` | 15 | trivial accessor/forwarder |
| `0x1033d4f0` | `sub_1033d4f0` | 19 | support routine (19 bytes) |
| `0x1033d510` | `sub_1033d510` | 8 | trivial accessor/forwarder |
| `0x1033d520` | `sub_1033d520` | 8 | trivial accessor/forwarder |
| `0x1033d530` | `sub_1033d530` | 8 | trivial accessor/forwarder |
| `0x1033d540` | `sub_1033d540` | 8 | trivial accessor/forwarder |
| `0x1033d550` | `sub_1033d550` | 8 | trivial accessor/forwarder |
| `0x1033d560` | `sub_1033d560` | 8 | trivial accessor/forwarder |
| `0x1033d570` | `sub_1033d570` | 8 | trivial accessor/forwarder |
| `0x1033d580` | `sub_1033d580` | 8 | trivial accessor/forwarder |
| `0x1033d590` | `sub_1033d590` | 8 | trivial accessor/forwarder |
| `0x1033d5a0` | `sub_1033d5a0` | 8 | trivial accessor/forwarder |
| `0x1033d5b0` | `sub_1033d5b0` | 8 | trivial accessor/forwarder |
| `0x1033d5c0` | `sub_1033d5c0` | 8 | trivial accessor/forwarder |
| `0x1033d5d0` | `sub_1033d5d0` | 8 | trivial accessor/forwarder |
| `0x1033d5e0` | `sub_1033d5e0` | 8 | trivial accessor/forwarder |
| `0x1033d5f0` | `sub_1033d5f0` | 8 | trivial accessor/forwarder |
| `0x1033d600` | `sub_1033d600` | 8 | trivial accessor/forwarder |
| `0x1033d610` | `sub_1033d610` | 8 | trivial accessor/forwarder |
| `0x1033d620` | `sub_1033d620` | 8 | trivial accessor/forwarder |
| `0x1033d630` | `sub_1033d630` | 86 | support routine (86 bytes) |
| `0x1033d690` | `sub_1033d690` | 30 | support routine (30 bytes) |
| `0x1033d6b0` | `sub_1033d6b0` | 83 | support routine (83 bytes) |
| `0x1033d710` | `sub_1033d710` | 42 | support routine (42 bytes) |
| `0x1033d740` | `sub_1033d740` | 404 | ElfBot RAID list window creator: lazily creates a LISTBOX child window (g_1038b334 CreateWindowEx) storing HWND in g_103a2c5c, logs RAID error on failure. |
| `0x1033d8e0` | `sub_1033d8e0` | 157 | support routine (157 bytes) |
| `0x1033d980` | `sub_1033d980` | 100 | support routine (100 bytes) |
| `0x1033d9f0` | `sub_1033d9f0` | 254 | ElfBot RAID window message pump/dialog: sends msg 390 to list window g_103a2c5c or opens dialog box (g_1038b14c) guarded by g_103a2b50/51 flags. |
| `0x1033daf0` | `sub_1033daf0` | 102 | support routine (102 bytes) |
| `0x1033db60` | `sub_1033db60` | 100 | support routine (100 bytes) |
| `0x1033dbd0` | `sub_1033dbd0` | 102 | support routine (102 bytes) |
| `0x1033dc40` | `sub_1033dc40` | 100 | support routine (100 bytes) |
| `0x1033dcb0` | `sub_1033dcb0` | 102 | support routine (102 bytes) |
| `0x1033dd20` | `sub_1033dd20` | 100 | support routine (100 bytes) |
| `0x1033dd90` | `sub_1033dd90` | 102 | support routine (102 bytes) |
| `0x1033de00` | `sub_1033de00` | 275 | ElfBot debug-log path builder: GetModuleFileName (g_1038b1d4), strips ext, appends optional '-%u' and '.DbgLog' to form elfbot-N.DbgLog path. |
| `0x1033df20` | `sub_1033df20` | 245 | support routine (245 bytes) |
| `0x1033e020` | `sub_1033e020` | 17 | support routine (17 bytes) |
| `0x1033e040` | `sub_1033e040` | 17 | support routine (17 bytes) |
| `0x1033e060` | `sub_1033e060` | 138 | support routine (138 bytes) |
| `0x1033e0f0` | `sub_1033e0f0` | 75 | support routine (75 bytes) |
| `0x1033e140` | `sub_1033e140` | 87 | support routine (87 bytes) |
| `0x1033e1a0` | `sub_1033e1a0` | 19 | support routine (19 bytes) |
| `0x1033e1c0` | `sub_1033e1c0` | 92 | support routine (92 bytes) |
| `0x1033e220` | `sub_1033e220` | 44 | support routine (44 bytes) |
| `0x1033e250` | `sub_1033e250` | 19 | support routine (19 bytes) |
| `0x1033e270` | `sub_1033e270` | 19 | support routine (19 bytes) |
| `0x1033e290` | `sub_1033e290` | 110 | support routine (110 bytes) |
| `0x1033e300` | `sub_1033e300` | 35 | support routine (35 bytes) |
| `0x1033e330` | `sub_1033e330` | 103 | support routine (103 bytes) |
| `0x1033e3a0` | `sub_1033e3a0` | 33 | support routine (33 bytes) |
| `0x1033e3d0` | `sub_1033e3d0` | 25 | support routine (25 bytes) |
| `0x1033e3f0` | `sub_1033e3f0` | 34 | support routine (34 bytes) |
| `0x1033e420` | `sub_1033e420` | 33 | support routine (33 bytes) |
| `0x1033e450` | `sub_1033e450` | 502 | boost::iostreams/file seekpos helper: adjusts read/write stream position by whence (beg/cur/end) against buffer field_3c with mode-bit checks. |
| `0x1033e650` | `sub_1033e650` | 19 | support routine (19 bytes) |
| `0x1033e670` | `sub_1033e670` | 19 | support routine (19 bytes) |
| `0x1033e690` | `sub_1033e690` | 350 | boost::iostreams device seek variant: computes new offset via sub_1033e7f0 then applies bounded seek for input/output mode bits a8. |
| `0x1033e7da` | `sub_1033e7da` | 2 | trivial accessor/forwarder |
| `0x1033e7f0` | `sub_1033e7f0` | 22 | support routine (22 bytes) |
| `0x1033e810` | `sub_1033e810` | 231 | support routine (231 bytes) |
| `0x1033e82e` | `sub_1033e82e` | 5 | trivial accessor/forwarder |
| `0x1033e85f` | `sub_1033e85f` | 5 | trivial accessor/forwarder |
| `0x1033e8f7` | `sub_1033e8f7` | 2 | trivial accessor/forwarder |
| `0x1033e910` | `sub_1033e910` | 29 | support routine (29 bytes) |
| `0x1033e930` | `sub_1033e930` | 233 | support routine (233 bytes) |
| `0x1033ea0c` | `sub_1033ea0c` | 2 | trivial accessor/forwarder |
| `0x1033ea20` | `sub_1033ea20` | 48 | support routine (48 bytes) |
| `0x1033ea50` | `sub_1033ea50` | 672 | boost::iostreams filtering buffer underflow/reserve: grows internal buffer (>=0x100), reallocs via sub_1033f0b0, resets gptr/eptr pointers. |
| `0x1033ea8a` | `sub_1033ea8a` | 5 | trivial accessor/forwarder |
| `0x1033eace` | `sub_1033eace` | 5 | trivial accessor/forwarder |
| `0x1033eae8` | `sub_1033eae8` | 5 | trivial accessor/forwarder |
| `0x1033ed00` | `sub_1033ed00` | 29 | support routine (29 bytes) |
| `0x1033ed20` | `sub_1033ed20` | 95 | support routine (95 bytes) |
| `0x1033ed80` | `sub_1033ed80` | 29 | support routine (29 bytes) |
| `0x1033eda0` | `sub_1033eda0` | 65 | support routine (65 bytes) |
| `0x1033edf0` | `sub_1033edf0` | 137 | support routine (137 bytes) |
| `0x1033ee80` | `sub_1033ee80` | 237 | support routine (237 bytes) |
| `0x1033ef70` | `sub_1033ef70` | 29 | support routine (29 bytes) |
| `0x1033ef90` | `sub_1033ef90` | 88 | support routine (88 bytes) |
| `0x1033eff0` | `sub_1033eff0` | 29 | support routine (29 bytes) |
| `0x1033f010` | `sub_1033f010` | 29 | support routine (29 bytes) |
| `0x1033f030` | `sub_1033f030` | 51 | support routine (51 bytes) |
| `0x1033f070` | `sub_1033f070` | 51 | support routine (51 bytes) |
| `0x1033f0b0` | `sub_1033f0b0` | 25 | support routine (25 bytes) |
| `0x1033f0d0` | `sub_1033f0d0` | 78 | support routine (78 bytes) |
| `0x1033f120` | `sub_1033f120` | 90 | support routine (90 bytes) |
| `0x1033f180` | `sub_1033f180` | 42 | support routine (42 bytes) |
| `0x1033f1b0` | `sub_1033f1b0` | 126 | support routine (126 bytes) |
| `0x1033f230` | `sub_1033f230` | 42 | support routine (42 bytes) |
| `0x1033f260` | `sub_1033f260` | 123 | support routine (123 bytes) |
| `0x1033f28f` | `sub_1033f28f` | 2 | trivial accessor/forwarder |
| `0x1033f2e0` | `sub_1033f2e0` | 123 | support routine (123 bytes) |
| `0x1033f30f` | `sub_1033f30f` | 2 | trivial accessor/forwarder |
| `0x1033f360` | `sub_1033f360` | 19 | support routine (19 bytes) |
| `0x1033f380` | `sub_1033f380` | 113 | MSVC std::vector operation |
| `0x1033f400` | `sub_1033f400` | 16 | trivial accessor/forwarder |
| `0x1033f410` | `sub_1033f410` | 27 | support routine (27 bytes) |
| `0x1033f430` | `sub_1033f430` | 19 | support routine (19 bytes) |
| `0x1033f450` | `sub_1033f450` | 113 | MSVC std::vector operation |
| `0x1033f4d0` | `sub_1033f4d0` | 27 | support routine (27 bytes) |
| `0x1033f4f0` | `sub_1033f4f0` | 44 | support routine (44 bytes) |
| `0x1033f520` | `sub_1033f520` | 44 | support routine (44 bytes) |
| `0x1033f550` | `sub_1033f550` | 1233 | boost::regex/format bound-arg parser: scans format string for '%' directives, parses each spec (sub_10342000), sets max arg count and flags on formatter. |
| `0x1033fa30` | `sub_1033fa30` | 107 | support routine (107 bytes) |
| `0x1033faa0` | `sub_1033faa0` | 87 | support routine (87 bytes) |
| `0x1033fb00` | `sub_1033fb00` | 16 | Boost library routine |
| `0x1033fb10` | `sub_1033fb10` | 44 | support routine (44 bytes) |
| `0x1033fb40` | `sub_1033fb40` | 75 | support routine (75 bytes) |
| `0x1033fb90` | `sub_1033fb90` | 16 | Boost library routine |
| `0x1033fba0` | `sub_1033fba0` | 44 | support routine (44 bytes) |
| `0x1033fbd0` | `sub_1033fbd0` | 75 | support routine (75 bytes) |
| `0x1033fc20` | `sub_1033fc20` | 141 | support routine (141 bytes) |
| `0x1033fcb0` | `sub_1033fcb0` | 158 | support routine (158 bytes) |
| `0x1033fd50` | `sub_1033fd50` | 148 | support routine (148 bytes) |
| `0x1033fdf0` | `sub_1033fdf0` | 117 | support routine (117 bytes) |
| `0x1033fe70` | `sub_1033fe70` | 93 | support routine (93 bytes) |
| `0x1033fed0` | `sub_1033fed0` | 44 | support routine (44 bytes) |
| `0x1033ff00` | `sub_1033ff00` | 44 | support routine (44 bytes) |
| `0x1033ff30` | `sub_1033ff30` | 132 | support routine (132 bytes) |
| `0x1033ffc0` | `sub_1033ffc0` | 142 | support routine (142 bytes) |
| `0x10340050` | `sub_10340050` | 148 | support routine (148 bytes) |
| `0x103400f0` | `sub_103400f0` | 42 | support routine (42 bytes) |
| `0x10340120` | `sub_10340120` | 37 | support routine (37 bytes) |
| `0x10340150` | `sub_10340150` | 43 | support routine (43 bytes) |
| `0x10340180` | `sub_10340180` | 88 | support routine (88 bytes) |
| `0x103401e0` | `sub_103401e0` | 88 | support routine (88 bytes) |
| `0x10340240` | `sub_10340240` | 444 | boost::format::str(): concatenates prefix + each bound-item string, padding short items to field_3c width with fill char, into output string. |
| `0x10340400` | `sub_10340400` | 107 | support routine (107 bytes) |
| `0x10340470` | `sub_10340470` | 16 | Boost library routine |
| `0x10340480` | `sub_10340480` | 44 | support routine (44 bytes) |
| `0x103404b0` | `sub_103404b0` | 75 | support routine (75 bytes) |
| `0x10340500` | `sub_10340500` | 145 | support routine (145 bytes) |
| `0x103405a0` | `sub_103405a0` | 145 | support routine (145 bytes) |
| `0x10340640` | `sub_10340640` | 145 | support routine (145 bytes) |
| `0x103406e0` | `sub_103406e0` | 38 | support routine (38 bytes) |
| `0x10340710` | `sub_10340710` | 77 | support routine (77 bytes) |
| `0x10340760` | `sub_10340760` | 77 | support routine (77 bytes) |
| `0x103407b0` | `sub_103407b0` | 108 | support routine (108 bytes) |
| `0x10340820` | `sub_10340820` | 78 | support routine (78 bytes) |
| `0x10340870` | `sub_10340870` | 56 | support routine (56 bytes) |
| `0x103408b0` | `sub_103408b0` | 217 | support routine (217 bytes) |
| `0x10340990` | `sub_10340990` | 57 | support routine (57 bytes) |
| `0x103409d0` | `sub_103409d0` | 43 | support routine (43 bytes) |
| `0x10340a00` | `sub_10340a00` | 25 | support routine (25 bytes) |
| `0x10340a20` | `sub_10340a20` | 32 | support routine (32 bytes) |
| `0x10340a40` | `sub_10340a40` | 57 | support routine (57 bytes) |
| `0x10340a80` | `sub_10340a80` | 147 | support routine (147 bytes) |
| `0x10340b20` | `sub_10340b20` | 118 | support routine (118 bytes) |
| `0x10340ba0` | `sub_10340ba0` | 194 | support routine (194 bytes) |
| `0x10340c70` | `sub_10340c70` | 39 | support routine (39 bytes) |
| `0x10340ca0` | `sub_10340ca0` | 49 | support routine (49 bytes) |
| `0x10340ce0` | `sub_10340ce0` | 105 | support routine (105 bytes) |
| `0x10340d50` | `sub_10340d50` | 971 | std::vector<T,100-byte-element> replace/reallocate: grows vector storage and inserts a3 elements with element-wise copy and SEH cookie frame. |
| `0x10340efd` | `sub_10340efd` | 72 | support routine (72 bytes) |
| `0x10341074` | `sub_10341074` | 59 | support routine (59 bytes) |
| `0x103411a0` | `sub_103411a0` | 10 | trivial accessor/forwarder |
| `0x103411b0` | `sub_103411b0` | 10 | trivial accessor/forwarder |
| `0x103411c0` | `sub_103411c0` | 95 | support routine (95 bytes) |
| `0x10341220` | `sub_10341220` | 61 | support routine (61 bytes) |
| `0x10341260` | `sub_10341260` | 26 | support routine (26 bytes) |
| `0x10341280` | `sub_10341280` | 28 | support routine (28 bytes) |
| `0x103412a0` | `sub_103412a0` | 51 | support routine (51 bytes) |
| `0x103412e0` | `sub_103412e0` | 57 | support routine (57 bytes) |
| `0x10341320` | `sub_10341320` | 168 | support routine (168 bytes) |
| `0x103413d0` | `sub_103413d0` | 28 | support routine (28 bytes) |
| `0x103413f0` | `sub_103413f0` | 160 | support routine (160 bytes) |
| `0x10341490` | `sub_10341490` | 84 | support routine (84 bytes) |
| `0x103414f0` | `sub_103414f0` | 35 | support routine (35 bytes) |
| `0x10341520` | `sub_10341520` | 57 | support routine (57 bytes) |
| `0x10341560` | `sub_10341560` | 46 | support routine (46 bytes) |
| `0x10341590` | `sub_10341590` | 28 | support routine (28 bytes) |
| `0x103415b0` | `sub_103415b0` | 71 | support routine (71 bytes) |
| `0x10341600` | `sub_10341600` | 53 | support routine (53 bytes) |
| `0x10341640` | `sub_10341640` | 32 | support routine (32 bytes) |
| `0x10341660` | `sub_10341660` | 28 | support routine (28 bytes) |
| `0x10341680` | `sub_10341680` | 28 | support routine (28 bytes) |
| `0x103416a0` | `sub_103416a0` | 35 | support routine (35 bytes) |
| `0x103416d0` | `sub_103416d0` | 54 | support routine (54 bytes) |
| `0x10341710` | `sub_10341710` | 33 | support routine (33 bytes) |
| `0x10341740` | `sub_10341740` | 32 | support routine (32 bytes) |
| `0x10341760` | `sub_10341760` | 257 | boost dynamic_bitset/pointer iterator advance: moves a block-pointer/bit-offset pair by signed a1, with bounds asserts (sub_10353616). |
| `0x10341870` | `sub_10341870` | 96 | support routine (96 bytes) |
| `0x103418d0` | `sub_103418d0` | 57 | support routine (57 bytes) |
| `0x10341910` | `sub_10341910` | 22 | support routine (22 bytes) |
| `0x10341930` | `sub_10341930` | 76 | support routine (76 bytes) |
| `0x10341980` | `sub_10341980` | 62 | support routine (62 bytes) |
| `0x103419c0` | `sub_103419c0` | 197 | support routine (197 bytes) |
| `0x10341a90` | `sub_10341a90` | 250 | boost::format state reset: clears each bound item's stream/state and resets current-arg index field_28 to 0. |
| `0x10341b90` | `sub_10341b90` | 150 | support routine (150 bytes) |
| `0x10341c30` | `sub_10341c30` | 17 | support routine (17 bytes) |
| `0x10341c50` | `sub_10341c50` | 407 | boost::format operator% overflow/dump helper: on too-many-args throws, else feeds a1 bound items with separator char to output. |
| `0x10341df0` | `sub_10341df0` | 418 | boost::format directive counter: scans format string counting '%' directives (parsing each) to determine expected argument count. |
| `0x10341fa0` | `sub_10341fa0` | 86 | support routine (86 bytes) |
| `0x10342000` | `sub_10342000` | 2439 | boost::format printf-style spec parser: parses one '%[flags][width][.prec][mods]conv' directive, setting flag/width/type bits on a format_item. |
| `0x1034210a` | `sub_1034210a` | 5 | trivial accessor/forwarder |
| `0x10342252` | `sub_10342252` | 5 | trivial accessor/forwarder |
| `0x10342330` | `sub_10342330` | 2 | trivial accessor/forwarder |
| `0x1034296c` | `sub_1034296c` | 2 | trivial accessor/forwarder |
| `0x10342a90` | `sub_10342a90` | 120 | support routine (120 bytes) |
| `0x10342b10` | `sub_10342b10` | 81 | support routine (81 bytes) |
| `0x10342b70` | `sub_10342b70` | 131 | support routine (131 bytes) |
| `0x10342c00` | `sub_10342c00` | 141 | support routine (141 bytes) |
| `0x10342c90` | `sub_10342c90` | 272 | boost::format feed/bind item narrow: on exhausted args throws (too_few_args), else binds current item to matching arg slot and streams it. |
| `0x10342da0` | `sub_10342da0` | 107 | support routine (107 bytes) |
| `0x10342e10` | `sub_10342e10` | 16 | Boost library routine |
| `0x10342e20` | `sub_10342e20` | 44 | support routine (44 bytes) |
| `0x10342e50` | `sub_10342e50` | 75 | support routine (75 bytes) |
| `0x10342ea0` | `sub_10342ea0` | 272 | boost::format feed/bind item variant: same too-few-args guard and item->arg binding logic on an alternate formatter layout. |
| `0x10342fb0` | `streambuf_underflow_sync` | 272 | std::basic_streambuf/istream helper: with SEH stack cookie, checks get-area, calls uflow/underflow and scans a callback table to sync positions. |
| `0x103430c0` | `sub_103430c0` | 71 | support routine (71 bytes) |
| `0x10343110` | `sub_10343110` | 15 | trivial accessor/forwarder |
| `0x10343120` | `sub_10343120` | 101 | support routine (101 bytes) |
| `0x10343190` | `sub_10343190` | 37 | support routine (37 bytes) |
| `0x103431c0` | `sub_103431c0` | 43 | support routine (43 bytes) |
| `0x103431f0` | `sub_103431f0` | 97 | support routine (97 bytes) |
| `0x10343260` | `sub_10343260` | 64 | support routine (64 bytes) |
| `0x103432a0` | `sub_103432a0` | 158 | support routine (158 bytes) |
| `0x10343340` | `sub_10343340` | 148 | support routine (148 bytes) |
| `0x103433e0` | `sub_103433e0` | 117 | support routine (117 bytes) |
| `0x10343460` | `sub_10343460` | 44 | support routine (44 bytes) |
| `0x10343490` | `sub_10343490` | 44 | support routine (44 bytes) |
| `0x103434c0` | `sub_103434c0` | 44 | support routine (44 bytes) |
| `0x103434f0` | `sub_103434f0` | 77 | support routine (77 bytes) |
| `0x10343540` | `sub_10343540` | 27 | support routine (27 bytes) |
| `0x10343560` | `sub_10343560` | 134 | support routine (134 bytes) |
| `0x103435f0` | `sub_103435f0` | 29 | support routine (29 bytes) |
| `0x10343610` | `sub_10343610` | 35 | support routine (35 bytes) |
| `0x10343640` | `sub_10343640` | 35 | support routine (35 bytes) |
| `0x10343670` | `sub_10343670` | 132 | support routine (132 bytes) |
| `0x10343700` | `sub_10343700` | 142 | support routine (142 bytes) |
| `0x10343790` | `sub_10343790` | 148 | support routine (148 bytes) |
| `0x10343830` | `sub_10343830` | 42 | support routine (42 bytes) |
| `0x10343860` | `facet_format_dispatch` | 298 | std::money_get/num_get-style dispatcher choosing a formatting path via facet lookup (sub_1031b6e0) and 64-bit arg packing. |
| `0x10343990` | `sub_10343990` | 62 | support routine (62 bytes) |
| `0x103439d0` | `sub_103439d0` | 64 | support routine (64 bytes) |
| `0x10343a10` | `sub_10343a10` | 151 | support routine (151 bytes) |
| `0x10343ab0` | `sub_10343ab0` | 117 | support routine (117 bytes) |
| `0x10343b30` | `sub_10343b30` | 222 | support routine (222 bytes) |
| `0x10343c10` | `sub_10343c10` | 65 | support routine (65 bytes) |
| `0x10343c60` | `sub_10343c60` | 62 | support routine (62 bytes) |
| `0x10343ca0` | `basic_string_replace` | 389 | std::basic_string::replace core: bounds-check, memmove tail (sub_103159d0), grow/reserve and fill the inserted range. |
| `0x10343e30` | `sub_10343e30` | 246 | support routine (246 bytes) |
| `0x10343f30` | `sub_10343f30` | 214 | support routine (214 bytes) |
| `0x10344010` | `sub_10344010` | 37 | support routine (37 bytes) |
| `0x10344040` | `sub_10344040` | 25 | support routine (25 bytes) |
| `0x10344060` | `sub_10344060` | 57 | support routine (57 bytes) |
| `0x103440a0` | `sub_103440a0` | 14 | trivial accessor/forwarder |
| `0x103440b0` | `sub_103440b0` | 116 | support routine (116 bytes) |
| `0x10344130` | `sub_10344130` | 153 | support routine (153 bytes) |
| `0x103441d0` | `sub_103441d0` | 52 | support routine (52 bytes) |
| `0x10344210` | `sub_10344210` | 43 | support routine (43 bytes) |
| `0x10344240` | `sub_10344240` | 105 | support routine (105 bytes) |
| `0x103442b0` | `sub_103442b0` | 43 | support routine (43 bytes) |
| `0x103442e0` | `sub_103442e0` | 57 | support routine (57 bytes) |
| `0x10344320` | `vector_insert_reallocate` | 711 | std::vector<int>-style _Insert_n: SEH-guarded reallocate with geometric growth and element move (sub_103466f0) at an insertion point. |
| `0x10344456` | `sub_10344456` | 3 | trivial accessor/forwarder |
| `0x10344459` | `sub_10344459` | 51 | support routine (51 bytes) |
| `0x1034456b` | `sub_1034456b` | 53 | support routine (53 bytes) |
| `0x10344660` | `sub_10344660` | 28 | support routine (28 bytes) |
| `0x10344680` | `sub_10344680` | 52 | support routine (52 bytes) |
| `0x103446c0` | `sub_103446c0` | 46 | support routine (46 bytes) |
| `0x103446f0` | `sub_103446f0` | 96 | support routine (96 bytes) |
| `0x10344750` | `sub_10344750` | 45 | support routine (45 bytes) |
| `0x10344780` | `sub_10344780` | 84 | support routine (84 bytes) |
| `0x103447e0` | `sub_103447e0` | 83 | support routine (83 bytes) |
| `0x10344840` | `sub_10344840` | 19 | support routine (19 bytes) |
| `0x10344860` | `sub_10344860` | 178 | support routine (178 bytes) |
| `0x10344920` | `sub_10344920` | 32 | support routine (32 bytes) |
| `0x10344940` | `sub_10344940` | 34 | support routine (34 bytes) |
| `0x10344970` | `sub_10344970` | 146 | support routine (146 bytes) |
| `0x10344a10` | `sub_10344a10` | 88 | support routine (88 bytes) |
| `0x10344a70` | `sub_10344a70` | 88 | support routine (88 bytes) |
| `0x10344ad0` | `sub_10344ad0` | 141 | support routine (141 bytes) |
| `0x10344b60` | `sub_10344b60` | 13 | trivial accessor/forwarder |
| `0x10344b70` | `num_put_iput_char` | 1624 | std::num_put<char>::_Iput: pad/justify a formatted numeric field into an ostreambuf per adjustfield, sign and grouping (locale facet). |
| `0x103451d0` | `sub_103451d0` | 17 | support routine (17 bytes) |
| `0x103451f0` | `sub_103451f0` | 36 | support routine (36 bytes) |
| `0x10345220` | `sub_10345220` | 17 | support routine (17 bytes) |
| `0x10345240` | `ostream_pad_fill` | 568 | std::ostreambuf_iterator fill/pad helper: sentry-guarded writes of a fill char to the stream buffer, setting badbit on failure. |
| `0x1034541d` | `sub_1034541d` | 33 | support routine (33 bytes) |
| `0x103454a0` | `sub_103454a0` | 176 | support routine (176 bytes) |
| `0x10345550` | `sub_10345550` | 97 | support routine (97 bytes) |
| `0x103455c0` | `sub_103455c0` | 17 | support routine (17 bytes) |
| `0x103455e0` | `sub_103455e0` | 110 | support routine (110 bytes) |
| `0x10345635` | `sub_10345635` | 13 | trivial accessor/forwarder |
| `0x10345660` | `sub_10345660` | 62 | support routine (62 bytes) |
| `0x103456a0` | `num_put_iput_variant_a` | 1624 | std::num_put<char>::_Iput variant (field_5c width): sentry-guarded padded numeric output via sub_10347990 put path. |
| `0x10345d00` | `num_put_iput_variant_b` | 1624 | std::num_put<char>::_Iput variant using sub_10347c50 put path: sentry-guarded padded numeric formatting to ostreambuf. |
| `0x10346360` | `sub_10346360` | 87 | support routine (87 bytes) |
| `0x103463c0` | `sub_103463c0` | 78 | support routine (78 bytes) |
| `0x10346410` | `sub_10346410` | 38 | support routine (38 bytes) |
| `0x10346440` | `sub_10346440` | 64 | support routine (64 bytes) |
| `0x10346480` | `sub_10346480` | 126 | support routine (126 bytes) |
| `0x103464e5` | `sub_103464e5` | 2 | trivial accessor/forwarder |
| `0x103464f0` | `sub_103464f0` | 33 | support routine (33 bytes) |
| `0x103464fb` | `sub_103464fb` | 20 | support routine (20 bytes) |
| `0x10346540` | `sub_10346540` | 127 | support routine (127 bytes) |
| `0x103465c0` | `sub_103465c0` | 55 | support routine (55 bytes) |
| `0x10346600` | `sub_10346600` | 127 | support routine (127 bytes) |
| `0x10346680` | `sub_10346680` | 101 | support routine (101 bytes) |
| `0x103466f0` | `sub_103466f0` | 37 | support routine (37 bytes) |
| `0x10346720` | `sub_10346720` | 43 | support routine (43 bytes) |
| `0x10346750` | `sub_10346750` | 97 | support routine (97 bytes) |
| `0x103467c0` | `sub_103467c0` | 64 | support routine (64 bytes) |
| `0x10346800` | `sub_10346800` | 158 | support routine (158 bytes) |
| `0x103468a0` | `sub_103468a0` | 148 | support routine (148 bytes) |
| `0x10346940` | `sub_10346940` | 117 | support routine (117 bytes) |
| `0x103469c0` | `sub_103469c0` | 33 | support routine (33 bytes) |
| `0x103469f0` | `sub_103469f0` | 104 | support routine (104 bytes) |
| `0x10346a60` | `sub_10346a60` | 44 | support routine (44 bytes) |
| `0x10346a90` | `sub_10346a90` | 44 | support routine (44 bytes) |
| `0x10346ac0` | `sub_10346ac0` | 121 | support routine (121 bytes) |
| `0x10346b40` | `sub_10346b40` | 31 | support routine (31 bytes) |
| `0x10346b60` | `sub_10346b60` | 53 | support routine (53 bytes) |
| `0x10346ba0` | `sub_10346ba0` | 33 | support routine (33 bytes) |
| `0x10346bd0` | `sub_10346bd0` | 104 | support routine (104 bytes) |
| `0x10346c40` | `sub_10346c40` | 75 | support routine (75 bytes) |
| `0x10346c90` | `sub_10346c90` | 78 | support routine (78 bytes) |
| `0x10346ce0` | `sub_10346ce0` | 28 | support routine (28 bytes) |
| `0x10346d00` | `sub_10346d00` | 46 | support routine (46 bytes) |
| `0x10346d30` | `sub_10346d30` | 29 | support routine (29 bytes) |
| `0x10346d50` | `sub_10346d50` | 35 | support routine (35 bytes) |
| `0x10346d80` | `sub_10346d80` | 118 | support routine (118 bytes) |
| `0x10346e00` | `sub_10346e00` | 194 | support routine (194 bytes) |
| `0x10346ed0` | `sub_10346ed0` | 132 | support routine (132 bytes) |
| `0x10346f60` | `sub_10346f60` | 142 | support routine (142 bytes) |
| `0x10346ff0` | `sub_10346ff0` | 148 | support routine (148 bytes) |
| `0x10347090` | `sub_10347090` | 42 | support routine (42 bytes) |
| `0x103470c0` | `sub_103470c0` | 193 | support routine (193 bytes) |
| `0x10347190` | `sub_10347190` | 158 | support routine (158 bytes) |
| `0x10347230` | `sub_10347230` | 53 | support routine (53 bytes) |
| `0x10347270` | `sub_10347270` | 19 | support routine (19 bytes) |
| `0x10347290` | `ios_copyfmt_apply` | 269 | std::ios_base::_Init-from-locale: copy flags/precision/width and imbue facet-derived state into a stream, running fixup callbacks. |
| `0x103473a0` | `sub_103473a0` | 40 | support routine (40 bytes) |
| `0x103473d0` | `sub_103473d0` | 42 | support routine (42 bytes) |
| `0x10347400` | `sub_10347400` | 170 | support routine (170 bytes) |
| `0x103474b0` | `sub_103474b0` | 147 | support routine (147 bytes) |
| `0x10347550` | `sub_10347550` | 101 | support routine (101 bytes) |
| `0x103475c0` | `sub_103475c0` | 68 | support routine (68 bytes) |
| `0x10347610` | `sub_10347610` | 154 | support routine (154 bytes) |
| `0x103476b0` | `sub_103476b0` | 88 | support routine (88 bytes) |
| `0x10347710` | `sub_10347710` | 88 | support routine (88 bytes) |
| `0x10347770` | `sub_10347770` | 19 | support routine (19 bytes) |
| `0x10347790` | `sub_10347790` | 147 | support routine (147 bytes) |
| `0x10347830` | `sub_10347830` | 45 | support routine (45 bytes) |
| `0x10347860` | `num_put_write_padded` | 292 | std::num_put padding writer: emits internal/left/right fill plus optional sign char and the digit string to the output iterator. |
| `0x10347990` | `sub_10347990` | 21 | support routine (21 bytes) |
| `0x103479b0` | `ostream_put_string` | 586 | std::ostreambuf_iterator string put: sentry-guarded write of n chars with locale widen, setting failbit/badbit as needed. |
| `0x10347bb3` | `sub_10347bb3` | 35 | support routine (35 bytes) |
| `0x10347c20` | `sub_10347c20` | 34 | support routine (34 bytes) |
| `0x10347c50` | `sub_10347c50` | 20 | support routine (20 bytes) |
| `0x10347c70` | `num_put_put_char` | 371 | std::num_put<wchar>::put(bool/char): sentry-guarded widen+put of a single formatted char via facet ctype. |
| `0x10347d9a` | `sub_10347d9a` | 33 | support routine (33 bytes) |
| `0x10347e10` | `sub_10347e10` | 67 | support routine (67 bytes) |
| `0x10347e60` | `sub_10347e60` | 40 | support routine (40 bytes) |
| `0x10347e90` | `sub_10347e90` | 22 | support routine (22 bytes) |
| `0x10347eb0` | `sub_10347eb0` | 233 | support routine (233 bytes) |
| `0x10347fa0` | `sub_10347fa0` | 140 | support routine (140 bytes) |
| `0x10348030` | `sub_10348030` | 176 | support routine (176 bytes) |
| `0x103480e0` | `num_put_do_put_int` | 704 | std::num_put integer put entry: if showbase/hex, format string then dispatch to width/fill logic (sub_10349910) via facet vtable. |
| `0x10348163` | `sub_10348163` | 5 | trivial accessor/forwarder |
| `0x103483b0` | `sub_103483b0` | 145 | support routine (145 bytes) |
| `0x10348450` | `sub_10348450` | 145 | support routine (145 bytes) |
| `0x103484f0` | `sub_103484f0` | 149 | support routine (149 bytes) |
| `0x10348590` | `sub_10348590` | 149 | support routine (149 bytes) |
| `0x10348630` | `num_put_do_put_double_fixed` | 553 | std::num_put<char>::do_put(double) fixed path: x87 FP loop building the digit magnitude then handing to sub_10348c70 formatter. |
| `0x10348860` | `num_put_do_put_double_sci` | 553 | std::num_put<char>::do_put(double) scientific path: x87 FP normalization loop feeding sub_10348c70 with %e-style flags. |
| `0x10348a90` | `sub_10348a90` | 119 | support routine (119 bytes) |
| `0x10348b10` | `sub_10348b10` | 44 | support routine (44 bytes) |
| `0x10348b40` | `sub_10348b40` | 84 | support routine (84 bytes) |
| `0x10348ba0` | `sub_10348ba0` | 202 | support routine (202 bytes) |
| `0x10348c70` | `num_put_format_float_grouped` | 1933 | std::num_put float formatter core: apply locale grouping/decimal point, sign, exponent split and emit padded digit groups to iterator. |
| `0x10349400` | `sub_10349400` | 249 | support routine (249 bytes) |
| `0x10349500` | `num_put_format_int_grouped` | 936 | std::num_put integer formatter core: insert thousands separators per locale grouping and emit sign/prefix + digits to iterator. |
| `0x103498b0` | `sub_103498b0` | 85 | support routine (85 bytes) |
| `0x10349910` | `sub_10349910` | 74 | support routine (74 bytes) |
| `0x10349960` | `sub_10349960` | 103 | support routine (103 bytes) |
| `0x103499d0` | `num_put_emit_groups` | 262 | std::num_put grouping emit helper: splits a digit run on separator positions (sub_10353a90) and writes groups + separators to the iterator. |
| `0x10349ae0` | `sub_10349ae0` | 83 | support routine (83 bytes) |
| `0x10349b40` | `sub_10349b40` | 50 | support routine (50 bytes) |
| `0x10349b80` | `sub_10349b80` | 29 | support routine (29 bytes) |
| `0x10349ba0` | `sub_10349ba0` | 89 | support routine (89 bytes) |
| `0x10349c00` | `sub_10349c00` | 31 | support routine (31 bytes) |
| `0x10349c20` | `sub_10349c20` | 127 | support routine (127 bytes) |
| `0x10349ca0` | `sub_10349ca0` | 66 | support routine (66 bytes) |
| `0x10349cf0` | `sub_10349cf0` | 127 | support routine (127 bytes) |
| `0x10349d70` | `sub_10349d70` | 24 | support routine (24 bytes) |
| `0x10349d90` | `sub_10349d90` | 73 | support routine (73 bytes) |
| `0x10349de0` | `sub_10349de0` | 78 | support routine (78 bytes) |
| `0x10349e30` | `sub_10349e30` | 36 | support routine (36 bytes) |
| `0x10349e60` | `sub_10349e60` | 64 | support routine (64 bytes) |
| `0x10349ea0` | `sub_10349ea0` | 25 | support routine (25 bytes) |
| `0x10349ec0` | `sub_10349ec0` | 238 | support routine (238 bytes) |
| `0x10349fb0` | `sub_10349fb0` | 125 | support routine (125 bytes) |
| `0x1034a030` | `sub_1034a030` | 88 | support routine (88 bytes) |
| `0x1034a090` | `num_get_get_pointer` | 370 | std::num_get<wchar>::get for pointer/void*: sentry-guarded read of formatted value via facet, setting iostate on failure. |
| `0x1034a1b9` | `sub_1034a1b9` | 33 | support routine (33 bytes) |
| `0x1034a230` | `sub_1034a230` | 36 | support routine (36 bytes) |
| `0x1034a260` | `sub_1034a260` | 32 | support routine (32 bytes) |
| `0x1034a280` | `sub_1034a280` | 88 | support routine (88 bytes) |
| `0x1034a2e0` | `sub_1034a2e0` | 22 | support routine (22 bytes) |
| `0x1034a300` | `sub_1034a300` | 51 | support routine (51 bytes) |
| `0x1034a340` | `sub_1034a340` | 35 | support routine (35 bytes) |
| `0x1034a370` | `sub_1034a370` | 118 | support routine (118 bytes) |
| `0x1034a3f0` | `sub_1034a3f0` | 194 | support routine (194 bytes) |
| `0x1034a4c0` | `sub_1034a4c0` | 27 | support routine (27 bytes) |
| `0x1034a4e0` | `sub_1034a4e0` | 22 | support routine (22 bytes) |
| `0x1034a500` | `sub_1034a500` | 62 | support routine (62 bytes) |
| `0x1034a540` | `sub_1034a540` | 109 | support routine (109 bytes) |
| `0x1034a5b0` | `sub_1034a5b0` | 82 | support routine (82 bytes) |
| `0x1034a610` | `sub_1034a610` | 48 | support routine (48 bytes) |
| `0x1034a640` | `sub_1034a640` | 20 | support routine (20 bytes) |
| `0x1034a660` | `sub_1034a660` | 96 | support routine (96 bytes) |
| `0x1034a6c0` | `sub_1034a6c0` | 92 | support routine (92 bytes) |
| `0x1034a720` | `sub_1034a720` | 10 | trivial accessor/forwarder |
| `0x1034a730` | `sub_1034a730` | 29 | support routine (29 bytes) |
| `0x1034a750` | `sub_1034a750` | 75 | support routine (75 bytes) |
| `0x1034a7a0` | `sub_1034a7a0` | 56 | support routine (56 bytes) |
| `0x1034a7e0` | `sub_1034a7e0` | 122 | support routine (122 bytes) |
| `0x1034a860` | `sub_1034a860` | 30 | support routine (30 bytes) |
| `0x1034a880` | `sub_1034a880` | 22 | support routine (22 bytes) |
| `0x1034a8a0` | `sub_1034a8a0` | 22 | support routine (22 bytes) |
| `0x1034a8c0` | `sub_1034a8c0` | 105 | support routine (105 bytes) |
| `0x1034a930` | `sub_1034a930` | 131 | support routine (131 bytes) |
| `0x1034a997` | `sub_1034a997` | 2 | trivial accessor/forwarder |
| `0x1034a9a2` | `sub_1034a9a2` | 33 | support routine (33 bytes) |
| `0x1034a9ad` | `sub_1034a9ad` | 20 | support routine (20 bytes) |
| `0x1034a9f0` | `sub_1034a9f0` | 82 | support routine (82 bytes) |
| `0x1034aa50` | `sub_1034aa50` | 60 | support routine (60 bytes) |
| `0x1034aa90` | `sub_1034aa90` | 164 | support routine (164 bytes) |
| `0x1034ab16` | `sub_1034ab16` | 34 | support routine (34 bytes) |
| `0x1034ab60` | `sub_1034ab60` | 98 | support routine (98 bytes) |
| `0x1034abd0` | `sub_1034abd0` | 29 | support routine (29 bytes) |
| `0x1034abf0` | `sub_1034abf0` | 56 | support routine (56 bytes) |
| `0x1034ac30` | `sub_1034ac30` | 44 | support routine (44 bytes) |
| `0x1034ac60` | `sub_1034ac60` | 75 | support routine (75 bytes) |
| `0x1034acb0` | `sub_1034acb0` | 69 | support routine (69 bytes) |
| `0x1034ad00` | `sub_1034ad00` | 43 | support routine (43 bytes) |
| `0x1034ad30` | `sub_1034ad30` | 16 | trivial accessor/forwarder |
| `0x1034ad40` | `sub_1034ad40` | 8 | trivial accessor/forwarder |
| `0x1034ad50` | `sub_1034ad50` | 8 | trivial accessor/forwarder |
| `0x1034ad60` | `sub_1034ad60` | 8 | trivial accessor/forwarder |
| `0x1034ad70` | `sub_1034ad70` | 8 | trivial accessor/forwarder |
| `0x1034ad80` | `sub_1034ad80` | 8 | trivial accessor/forwarder |
| `0x1034ad90` | `sub_1034ad90` | 8 | trivial accessor/forwarder |
| `0x1034ada0` | `sub_1034ada0` | 8 | trivial accessor/forwarder |
| `0x1034adb0` | `sub_1034adb0` | 8 | trivial accessor/forwarder |
| `0x1034adc0` | `sub_1034adc0` | 8 | trivial accessor/forwarder |
| `0x1034add0` | `sub_1034add0` | 111 | support routine (111 bytes) |
| `0x1034ae2d` | `sub_1034ae2d` | 13 | trivial accessor/forwarder |
| `0x1034ae3a` | `sub_1034ae3a` | 14 | trivial accessor/forwarder |
| `0x1034ae48` | `sub_1034ae48` | 25 | support routine (25 bytes) |
| `0x1034ae80` | `sub_1034ae80` | 38 | support routine (38 bytes) |
| `0x1034aed7` | `sub_1034aed7` | 31 | support routine (31 bytes) |
| `0x1034aeed` | `sub_1034aeed` | 24 | support routine (24 bytes) |
| `0x1034af10` | `sub_1034af10` | 23 | support routine (23 bytes) |
| `0x1034af77` | `sub_1034af77` | 4 | trivial accessor/forwarder |
| `0x1034af7b` | `sub_1034af7b` | 48 | support routine (48 bytes) |
| `0x1034af89` | `sub_1034af89` | 141 | support routine (141 bytes) |
| `0x1034b03f` | `sub_1034b03f` | 34 | support routine (34 bytes) |
| `0x1034b061` | `sub_1034b061` | 77 | support routine (77 bytes) |
| `0x1034b0ae` | `zlib_deflate` | 1903 | zlib deflate() state machine: emits gzip/zlib header bytes, name/comment/extra fields and drives block flushing per flush level. |
| `0x1034b81d` | `sub_1034b81d` | 173 | support routine (173 bytes) |
| `0x1034b8ca` | `sub_1034b8ca` | 99 | support routine (99 bytes) |
| `0x1034b92d` | `sub_1034b92d` | 126 | support routine (126 bytes) |
| `0x1034b9ab` | `sub_1034b9ab` | 325 | support routine (325 bytes) |
| `0x1034baf0` | `sub_1034baf0` | 138 | support routine (138 bytes) |
| `0x1034bb7a` | `sub_1034bb7a` | 228 | support routine (228 bytes) |
| `0x1034bc5e` | `zlib_deflate_stored` | 296 | zlib deflate_stored: copy uncompressed stored blocks, filling the window and flushing when pending output is full. |
| `0x1034bd86` | `zlib_deflate_fast` | 750 | zlib deflate_fast: LZ77 hash-chain match, emit literal/length-distance via _tr_tally, slide window and flush blocks. |
| `0x1034c074` | `zlib_deflate_slow` | 971 | zlib deflate_slow: lazy-match LZ77 with previous-match comparison, emitting literals/matches and flushing blocks. |
| `0x1034c43f` | `sub_1034c43f` | 135 | support routine (135 bytes) |
| `0x1034c4c6` | `sub_1034c4c6` | 464 | support routine (464 bytes) |
| `0x1034c696` | `sub_1034c696` | 33 | support routine (33 bytes) |
| `0x1034c6b7` | `sub_1034c6b7` | 91 | support routine (91 bytes) |
| `0x1034c712` | `sub_1034c712` | 186 | support routine (186 bytes) |
| `0x1034c7cc` | `sub_1034c7cc` | 23 | support routine (23 bytes) |
| `0x1034c7e3` | `sub_1034c7e3` | 29 | support routine (29 bytes) |
| `0x1034c800` | `sub_1034c800` | 216 | support routine (216 bytes) |
| `0x1034c8d8` | `zlib_tr_flush_block` | 4593 | zlib _tr_flush_block / compress_block: build dynamic Huffman trees, pick stored/fixed/dynamic block type and emit compressed data. |
| `0x1034db40` | `sub_1034db40` | 62 | support routine (62 bytes) |
| `0x1034db7e` | `sub_1034db7e` | 586 | support routine (586 bytes) |
| `0x1034ddc8` | `sub_1034ddc8` | 26 | support routine (26 bytes) |
| `0x1034dde2` | `sub_1034dde2` | 544 | support routine (544 bytes) |
| `0x1034e002` | `sub_1034e002` | 94 | support routine (94 bytes) |
| `0x1034e060` | `sub_1034e060` | 176 | support routine (176 bytes) |
| `0x1034e110` | `sub_1034e110` | 445 | support routine (445 bytes) |
| `0x1034e2cd` | `sub_1034e2cd` | 188 | support routine (188 bytes) |
| `0x1034e389` | `sub_1034e389` | 1178 | support routine (1178 bytes) |
| `0x1034e823` | `zlib_compress_block_send` | 566 | zlib compress_block inner: emit Huffman codes for literal/length and distance symbols from the sym_buf via send_bits. |
| `0x1034ea59` | `sub_1034ea59` | 946 | support routine (946 bytes) |
| `0x1034ee0b` | `sub_1034ee0b` | 66 | support routine (66 bytes) |
| `0x1034ee4d` | `sub_1034ee4d` | 31 | support routine (31 bytes) |
| `0x1034ee6c` | `sub_1034ee6c` | 109 | support routine (109 bytes) |
| `0x1034eed9` | `sub_1034eed9` | 87 | support routine (87 bytes) |
| `0x1034ef30` | `sub_1034ef30` | 120 | support routine (120 bytes) |
| `0x1034efa8` | `sub_1034efa8` | 100 | support routine (100 bytes) |
| `0x1034f00c` | `sub_1034f00c` | 119 | support routine (119 bytes) |
| `0x1034f083` | `zlib_gen_codes` | 488 | zlib gen_bitlen/gen_codes: assign Huffman code lengths from frequencies and build canonical codes for a tree descriptor. |
| `0x1034f26b` | `sub_1034f26b` | 97 | support routine (97 bytes) |
| `0x1034f2cc` | `sub_1034f2cc` | 139 | support routine (139 bytes) |
| `0x1034f357` | `sub_1034f357` | 455 | support routine (455 bytes) |
| `0x1034f51e` | `zlib_flush_block_choose` | 501 | zlib _tr_flush_block wrapper: build literal/distance trees, compute static vs dynamic block cost and emit the chosen block. |
| `0x1034f713` | `sub_1034f713` | 17 | support routine (17 bytes) |
| `0x1034f724` | `sub_1034f724` | 11 | trivial accessor/forwarder |
| `0x1034f72f` | `sub_1034f72f` | 988 | support routine (988 bytes) |
| `0x1034fb0b` | `zlib_build_tree` | 979 | zlib build_tree / scan_tree: Huffman tree construction via heap (pqdownheap) and bit-length code scan for tree compression. |
| `0x1034fede` | `sub_1034fede` | 6 | trivial accessor/forwarder |
| `0x1034fee4` | `sub_1034fee4` | 6 | trivial accessor/forwarder |
| `0x1034feea` | `sub_1034feea` | 6 | trivial accessor/forwarder |
| `0x1034fef0` | `sub_1034fef0` | 5 | trivial accessor/forwarder |
| `0x1034fef5` | `sub_1034fef5` | 24 | support routine (24 bytes) |
| `0x1034ff0d` | `sub_1034ff0d` | 21 | support routine (21 bytes) |
| `0x1034ff22` | `sub_1034ff22` | 9 | trivial accessor/forwarder |
| `0x1034ff2b` | `sub_1034ff2b` | 9 | trivial accessor/forwarder |
| `0x1034ff34` | `sub_1034ff34` | 70 | support routine (70 bytes) |
| `0x1034ff7a` | `sub_1034ff7a` | 80 | support routine (80 bytes) |
| `0x1034ffca` | `sub_1034ffca` | 62 | support routine (62 bytes) |
| `0x10350008` | `sub_10350008` | 47 | support routine (47 bytes) |
| `0x10350037` | `sub_10350037` | 41 | support routine (41 bytes) |
| `0x10350060` | `sub_10350060` | 33 | support routine (33 bytes) |
| `0x10350081` | `sub_10350081` | 18 | support routine (18 bytes) |
| `0x10350093` | `sub_10350093` | 21 | support routine (21 bytes) |
| `0x103500a8` | `sub_103500a8` | 28 | support routine (28 bytes) |
| `0x103500c4` | `sub_103500c4` | 42 | support routine (42 bytes) |
| `0x103500ee` | `sub_103500ee` | 6 | trivial accessor/forwarder |
| `0x103500f4` | `sub_103500f4` | 37 | support routine (37 bytes) |
| `0x10350119` | `sub_10350119` | 131 | support routine (131 bytes) |
| `0x10350179` | `sub_10350179` | 67 | support routine (67 bytes) |
| `0x103501bc` | `sub_103501bc` | 57 | support routine (57 bytes) |
| `0x103501f5` | `sub_103501f5` | 35 | support routine (35 bytes) |
| `0x10350218` | `sub_10350218` | 108 | support routine (108 bytes) |
| `0x10350261` | `sub_10350261` | 107 | support routine (107 bytes) |
| `0x1035029e` | `sub_1035029e` | 28 | support routine (28 bytes) |
| `0x103502ba` | `sub_103502ba` | 199 | support routine (199 bytes) |
| `0x10350354` | `sub_10350354` | 74 | support routine (74 bytes) |
| `0x1035039e` | `sub_1035039e` | 98 | support routine (98 bytes) |
| `0x103503dd` | `sub_103503dd` | 98 | support routine (98 bytes) |
| `0x1035041c` | `crt_toupper_locale` | 271 | CRT towupper/ctype-based uppercase mapping: look up locale ctype table or fold ASCII letter to uppercase. |
| `0x1035052b` | `sub_1035052b` | 91 | support routine (91 bytes) |
| `0x10350586` | `crt_tolower_locale` | 276 | CRT towlower/ctype-based lowercase mapping: locale ctype lookup, else fold ASCII letter to lowercase (a0-32). |
| `0x1035069a` | `crt_strtol_core` | 406 | CRT strtol/strtoul core: skip whitespace, parse optional sign and base prefix, accumulate digits with overflow clamp. |
| `0x10350830` | `sub_10350830` | 20 | support routine (20 bytes) |
| `0x10350844` | `sub_10350844` | 163 | support routine (163 bytes) |
| `0x103508e7` | `sub_103508e7` | 32 | support routine (32 bytes) |
| `0x10350907` | `sub_10350907` | 103 | support routine (103 bytes) |
| `0x1035096e` | `sub_1035096e` | 5 | trivial accessor/forwarder |
| `0x10350973` | `sub_10350973` | 5 | trivial accessor/forwarder |
| `0x10350978` | `sub_10350978` | 11 | trivial accessor/forwarder |
| `0x10350983` | `sub_10350983` | 11 | trivial accessor/forwarder |
| `0x1035098e` | `sub_1035098e` | 11 | trivial accessor/forwarder |
| `0x10350999` | `sub_10350999` | 11 | trivial accessor/forwarder |
| `0x103509a4` | `sub_103509a4` | 32 | support routine (32 bytes) |
| `0x103509c4` | `sub_103509c4` | 2 | trivial accessor/forwarder |
| `0x103509de` | `sub_103509de` | 35 | support routine (35 bytes) |
| `0x103509e9` | `sub_103509e9` | 62 | support routine (62 bytes) |
| `0x10350a27` | `sub_10350a27` | 19 | support routine (19 bytes) |
| `0x10350a3a` | `sub_10350a3a` | 25 | support routine (25 bytes) |
| `0x10350a53` | `sub_10350a53` | 106 | support routine (106 bytes) |
| `0x10350abd` | `sub_10350abd` | 5 | trivial accessor/forwarder |
| `0x10350ad0` | `sub_10350ad0` | 122 | support routine (122 bytes) |
| `0x10350b50` | `sub_10350b50` | 711 | support routine (711 bytes) |
| `0x10350bb3` | `sub_10350bb3` | 1 | trivial accessor/forwarder |
| `0x10350bd3` | `sub_10350bd3` | 1 | trivial accessor/forwarder |
| `0x10350c11` | `sub_10350c11` | 3 | trivial accessor/forwarder |
| `0x10350c37` | `sub_10350c37` | 1 | trivial accessor/forwarder |
| `0x10350cdb` | `sub_10350cdb` | 1 | trivial accessor/forwarder |
| `0x10350ce7` | `sub_10350ce7` | 1 | trivial accessor/forwarder |
| `0x10350cf9` | `sub_10350cf9` | 3 | trivial accessor/forwarder |
| `0x10350d13` | `sub_10350d13` | 1 | trivial accessor/forwarder |
| `0x10350d3a` | `sub_10350d3a` | 2 | trivial accessor/forwarder |
| `0x10350d45` | `sub_10350d45` | 3 | trivial accessor/forwarder |
| `0x10350d95` | `sub_10350d95` | 3 | trivial accessor/forwarder |
| `0x10350dbf` | `sub_10350dbf` | 1 | trivial accessor/forwarder |
| `0x10350e77` | `sub_10350e77` | 1 | trivial accessor/forwarder |
| `0x10350e85` | `sub_10350e85` | 3 | trivial accessor/forwarder |
| `0x10350e9b` | `sub_10350e9b` | 1 | trivial accessor/forwarder |
| `0x10350eb5` | `sub_10350eb5` | 5 | trivial accessor/forwarder |
| `0x10350ec0` | `sub_10350ec0` | 711 | support routine (711 bytes) |
| `0x10350f23` | `sub_10350f23` | 1 | trivial accessor/forwarder |
| `0x10350f43` | `sub_10350f43` | 1 | trivial accessor/forwarder |
| `0x10350f81` | `sub_10350f81` | 3 | trivial accessor/forwarder |
| `0x10350fa7` | `sub_10350fa7` | 1 | trivial accessor/forwarder |
| `0x1035104b` | `sub_1035104b` | 1 | trivial accessor/forwarder |
| `0x10351057` | `sub_10351057` | 1 | trivial accessor/forwarder |
| `0x10351069` | `sub_10351069` | 3 | trivial accessor/forwarder |
| `0x10351083` | `sub_10351083` | 1 | trivial accessor/forwarder |
| `0x103510aa` | `sub_103510aa` | 2 | trivial accessor/forwarder |
| `0x103510b5` | `sub_103510b5` | 3 | trivial accessor/forwarder |
| `0x10351105` | `sub_10351105` | 3 | trivial accessor/forwarder |
| `0x1035112f` | `sub_1035112f` | 1 | trivial accessor/forwarder |
| `0x103511e7` | `sub_103511e7` | 1 | trivial accessor/forwarder |
| `0x103511f5` | `sub_103511f5` | 3 | trivial accessor/forwarder |
| `0x1035120b` | `sub_1035120b` | 1 | trivial accessor/forwarder |
| `0x10351225` | `sub_10351225` | 275 | support routine (275 bytes) |
| `0x10351234` | `sub_10351234` | 5630 | support routine (5630 bytes) |
| `0x103528b4` | `sub_103528b4` | 43 | support routine (43 bytes) |
| `0x103528df` | `sub_103528df` | 5 | trivial accessor/forwarder |
| `0x103528e4` | `sub_103528e4` | 7 | trivial accessor/forwarder |
| `0x103528eb` | `sub_103528eb` | 82 | support routine (82 bytes) |
| `0x1035293d` | `sub_1035293d` | 54 | support routine (54 bytes) |
| `0x10352973` | `sub_10352973` | 48 | support routine (48 bytes) |
| `0x103529a3` | `sub_103529a3` | 213 | support routine (213 bytes) |
| `0x10352a78` | `sub_10352a78` | 152 | support routine (152 bytes) |
| `0x10352aa6` | `sub_10352aa6` | 2 | trivial accessor/forwarder |
| `0x10352b0f` | `sub_10352b0f` | 3 | trivial accessor/forwarder |
| `0x10352b15` | `sub_10352b15` | 115 | support routine (115 bytes) |
| `0x10352b88` | `sub_10352b88` | 40 | support routine (40 bytes) |
| `0x10352bb0` | `sub_10352bb0` | 33 | support routine (33 bytes) |
| `0x10352bd1` | `sub_10352bd1` | 76 | support routine (76 bytes) |
| `0x10352c1d` | `sub_10352c1d` | 94 | support routine (94 bytes) |
| `0x10352c80` | `sub_10352c80` | 43 | support routine (43 bytes) |
| `0x10352cb0` | `sub_10352cb0` | 138 | support routine (138 bytes) |
| `0x10352cb7` | `sub_10352cb7` | 9 | trivial accessor/forwarder |
| `0x10352cc0` | `sub_10352cc0` | 101 | support routine (101 bytes) |
| `0x10352da8` | `sub_10352da8` | 28 | support routine (28 bytes) |
| `0x10352dd5` | `sub_10352dd5` | 11 | trivial accessor/forwarder |
| `0x10352de0` | `sub_10352de0` | 195 | support routine (195 bytes) |
| `0x10352ea0` | `sub_10352ea0` | 45 | support routine (45 bytes) |
| `0x10352ecd` | `sub_10352ecd` | 34 | support routine (34 bytes) |
| `0x10352eef` | `sub_10352eef` | 48 | support routine (48 bytes) |
| `0x10352f20` | `sub_10352f20` | 139 | support routine (139 bytes) |
| `0x10352fb0` | `sub_10352fb0` | 292 | support routine (292 bytes) |
| `0x103530d4` | `sub_103530d4` | 22 | support routine (22 bytes) |
| `0x103530ea` | `sub_103530ea` | 61 | support routine (61 bytes) |
| `0x10353127` | `sub_10353127` | 123 | support routine (123 bytes) |
| `0x103531a2` | `sub_103531a2` | 28 | support routine (28 bytes) |
| `0x103531be` | `sub_103531be` | 14 | trivial accessor/forwarder |
| `0x103531cc` | `sub_103531cc` | 28 | support routine (28 bytes) |
| `0x103531e8` | `sub_103531e8` | 27 | support routine (27 bytes) |
| `0x10353203` | `sub_10353203` | 17 | support routine (17 bytes) |
| `0x10353214` | `sub_10353214` | 78 | support routine (78 bytes) |
| `0x10353262` | `sub_10353262` | 24 | support routine (24 bytes) |
| `0x1035327a` | `sub_1035327a` | 88 | support routine (88 bytes) |
| `0x103532d2` | `sub_103532d2` | 22 | support routine (22 bytes) |
| `0x103532e8` | `sub_103532e8` | 13 | trivial accessor/forwarder |
| `0x103532f5` | `sub_103532f5` | 25 | support routine (25 bytes) |
| `0x1035330e` | `sub_1035330e` | 24 | support routine (24 bytes) |
| `0x10353326` | `sub_10353326` | 11 | trivial accessor/forwarder |
| `0x10353331` | `sub_10353331` | 28 | support routine (28 bytes) |
| `0x1035334d` | `sub_1035334d` | 34 | support routine (34 bytes) |
| `0x1035336f` | `sub_1035336f` | 123 | support routine (123 bytes) |
| `0x103533ea` | `sub_103533ea` | 74 | support routine (74 bytes) |
| `0x10353434` | `sub_10353434` | 42 | support routine (42 bytes) |
| `0x1035345e` | `sub_1035345e` | 133 | support routine (133 bytes) |
| `0x103534b4` | `sub_103534b4` | 9 | trivial accessor/forwarder |
| `0x103534ec` | `sub_103534ec` | 10 | trivial accessor/forwarder |
| `0x103534f6` | `crt_capture_context_report` | 252 | CRT unhandled-exception/report helper capturing full register+segment context (gs/ss/cs/ds) into a CONTEXT-like buffer. |
| `0x103535f2` | `sub_103535f2` | 36 | support routine (36 bytes) |
| `0x10353616` | `sub_10353616` | 16 | trivial accessor/forwarder |
| `0x10353626` | `sub_10353626` | 91 | support routine (91 bytes) |
| `0x10353681` | `sub_10353681` | 38 | support routine (38 bytes) |
| `0x103536a7` | `sub_103536a7` | 130 | support routine (130 bytes) |
| `0x10353729` | `crt_mbtowc_locale` | 660 | CRT __toascii/mbtowc-style multibyte parse using locale lc_ctype table to decode a multibyte char and advance the pointer. |
| `0x103539bd` | `sub_103539bd` | 41 | support routine (41 bytes) |
| `0x103539e6` | `sub_103539e6` | 42 | support routine (42 bytes) |
| `0x10353a10` | `sub_10353a10` | 96 | support routine (96 bytes) |
| `0x10353a70` | `sub_10353a70` | 30 | support routine (30 bytes) |
| `0x10353a90` | `sub_10353a90` | 173 | support routine (173 bytes) |
| `0x10353b3d` | `sub_10353b3d` | 31 | support routine (31 bytes) |
| `0x10353b5c` | `sub_10353b5c` | 185 | support routine (185 bytes) |
| `0x10353c15` | `sub_10353c15` | 47 | support routine (47 bytes) |
| `0x10353c44` | `sub_10353c44` | 54 | support routine (54 bytes) |
| `0x10353c7a` | `sub_10353c7a` | 6 | trivial accessor/forwarder |
| `0x10353c80` | `sub_10353c80` | 18 | support routine (18 bytes) |
| `0x10353c92` | `sub_10353c92` | 36 | support routine (36 bytes) |
| `0x10353cb6` | `sub_10353cb6` | 38 | support routine (38 bytes) |
| `0x10353cdc` | `sub_10353cdc` | 21 | support routine (21 bytes) |
| `0x10353cf1` | `sub_10353cf1` | 9 | trivial accessor/forwarder |
| `0x10353cfa` | `sub_10353cfa` | 9 | trivial accessor/forwarder |
| `0x10353d03` | `sub_10353d03` | 24 | support routine (24 bytes) |
| `0x10353d1b` | `sub_10353d1b` | 32 | support routine (32 bytes) |
| `0x10353d3b` | `sub_10353d3b` | 55 | support routine (55 bytes) |
| `0x10353d72` | `sub_10353d72` | 60 | support routine (60 bytes) |
| `0x10353dae` | `sub_10353dae` | 146 | support routine (146 bytes) |
| `0x10353e40` | `sub_10353e40` | 208 | support routine (208 bytes) |
| `0x10353f0a` | `sub_10353f0a` | 3 | trivial accessor/forwarder |
| `0x10353f0d` | `sub_10353f0d` | 15 | trivial accessor/forwarder |
| `0x10353f22` | `sub_10353f22` | 17 | support routine (17 bytes) |
| `0x10353f33` | `sub_10353f33` | 17 | support routine (17 bytes) |
| `0x10353f44` | `sub_10353f44` | 15 | trivial accessor/forwarder |
| `0x10353f53` | `sub_10353f53` | 76 | support routine (76 bytes) |
| `0x10353f9f` | `sub_10353f9f` | 13 | trivial accessor/forwarder |
| `0x10353fac` | `sub_10353fac` | 34 | support routine (34 bytes) |
| `0x10353fd0` | `sub_10353fd0` | 178 | support routine (178 bytes) |
| `0x10354090` | `sub_10354090` | 31 | support routine (31 bytes) |
| `0x103540af` | `sub_103540af` | 10 | trivial accessor/forwarder |
| `0x103540b9` | `sub_103540b9` | 49 | support routine (49 bytes) |
| `0x103540ea` | `sub_103540ea` | 34 | support routine (34 bytes) |
| `0x1035410c` | `sub_1035410c` | 60 | support routine (60 bytes) |
| `0x10354150` | `cxx_frame_handler_dispatch` | 431 | MSVC C++ EH: __CxxFrameHandler catch-funclet dispatcher walking the try/catch state map to unwind and invoke a handler. |
| `0x103542e6` | `sub_103542e6` | 186 | support routine (186 bytes) |
| `0x103543a0` | `sub_103543a0` | 10 | trivial accessor/forwarder |
| `0x103543aa` | `sub_103543aa` | 19 | support routine (19 bytes) |
| `0x103543bd` | `sub_103543bd` | 188 | support routine (188 bytes) |
| `0x10354479` | `sub_10354479` | 10 | trivial accessor/forwarder |
| `0x10354483` | `sub_10354483` | 19 | support routine (19 bytes) |
| `0x103544a0` | `sub_103544a0` | 52 | support routine (52 bytes) |
| `0x103544e0` | `sub_103544e0` | 170 | support routine (170 bytes) |
| `0x1035458a` | `cxx_frame_unwind_to_state` | 572 | MSVC C++ EH unwind: FrameUnwindToState destructing locals down the state chain via the unwind map (SEH-driven). |
| `0x103547c6` | `sub_103547c6` | 36 | support routine (36 bytes) |
| `0x103547f0` | `sub_103547f0` | 117 | support routine (117 bytes) |
| `0x10354870` | `sub_10354870` | 104 | support routine (104 bytes) |
| `0x103548d8` | `sub_103548d8` | 27 | support routine (27 bytes) |
| `0x103548f3` | `sub_103548f3` | 32 | support routine (32 bytes) |
| `0x10354913` | `sub_10354913` | 121 | support routine (121 bytes) |
| `0x1035498c` | `crt_getptd_mbstate_init` | 998 | CRT locale mbtowc setup: obtain thread locale ctype table and initialize multibyte decode state before conversion. |
| `0x10354d72` | `crt_mbrtowc_worker` | 1117 | CRT _mbtowc/mbrtowc worker: decode a UTF-8/DBCS sequence using the current locale codepage tables into a wchar output. |
| `0x103551cf` | `crt_fwrite_core` | 431 | CRT fwrite/_write buffered output core: validate stream/buffer, set EINVAL errno on null args and flush data in chunks. |
| `0x1035537e` | `sub_1035537e` | 29 | support routine (29 bytes) |
| `0x1035539b` | `crt_mkgmtime_normalize` | 709 | CRT _mkgmtime/_mktime worker: validates a tm-like struct against time_t range, applies TZ offsets, and normalizes seconds/minutes/hours/days fields (sets EINVAL=22). |
| `0x10355660` | `sub_10355660` | 36 | support routine (36 bytes) |
| `0x10355690` | `sub_10355690` | 70 | support routine (70 bytes) |
| `0x103556d6` | `crt_dll_main_dispatch` | 473 | CRT DllMain-style reason dispatcher (attach/detach/thread) calling FLS/TLS init (sub_10358f4a), version-info parse, and cleanup via g_1038b* imports. |
| `0x103558af` | `sub_103558af` | 226 | support routine (226 bytes) |
| `0x10355982` | `sub_10355982` | 17 | support routine (17 bytes) |
| `0x10355993` | `sub_10355993` | 3 | trivial accessor/forwarder |
| `0x103559a5` | `sub_103559a5` | 33 | support routine (33 bytes) |
| `0x103559c6` | `sub_103559c6` | 70 | support routine (70 bytes) |
| `0x10355a0c` | `sub_10355a0c` | 9 | trivial accessor/forwarder |
| `0x10355a15` | `sub_10355a15` | 193 | support routine (193 bytes) |
| `0x10355a4e` | `sub_10355a4e` | 2 | trivial accessor/forwarder |
| `0x10355ad8` | `sub_10355ad8` | 51 | support routine (51 bytes) |
| `0x10355b0b` | `sub_10355b0b` | 54 | support routine (54 bytes) |
| `0x10355b41` | `sub_10355b41` | 20 | support routine (20 bytes) |
| `0x10355b55` | `crt_lc_freelocaleinfo` | 320 | CRT __freetlocinfo/__freelocaleinfo: frees the per-category locale data (lconv, ctype/mbcs tables, 6-category array) guarding against static defaults. |
| `0x10355c95` | `sub_10355c95` | 134 | support routine (134 bytes) |
| `0x10355d1b` | `sub_10355d1b` | 140 | support routine (140 bytes) |
| `0x10355da7` | `sub_10355da7` | 36 | support routine (36 bytes) |
| `0x10355dcb` | `sub_10355dcb` | 62 | support routine (62 bytes) |
| `0x10355e09` | `sub_10355e09` | 106 | support routine (106 bytes) |
| `0x10355e73` | `sub_10355e73` | 12 | trivial accessor/forwarder |
| `0x10355e7f` | `sub_10355e7f` | 83 | support routine (83 bytes) |
| `0x10355ed2` | `sub_10355ed2` | 138 | support routine (138 bytes) |
| `0x10355f5c` | `sub_10355f5c` | 3 | trivial accessor/forwarder |
| `0x10355f5f` | `sub_10355f5f` | 9 | trivial accessor/forwarder |
| `0x10355f68` | `sub_10355f68` | 62 | support routine (62 bytes) |
| `0x10355fa6` | `crt_parse_lc_name` | 297 | CRT locale-name parser: splits a language[_country[.codepage]] string into fixed 64/64/16-byte fields of a locale struct, handling leading '.'. |
| `0x103560cf` | `sub_103560cf` | 107 | support routine (107 bytes) |
| `0x1035613a` | `crt_getlocaleinfo_build` | 369 | CRT locale-info builder: enumerates LC categories, calls GetLocaleInfo (sub_10355f68) per category, and returns/frees the assembled locale record. |
| `0x103562ab` | `crt_expand_lcid_langcountry` | 468 | CRT locale helper: given a language string resolves LCID/codepage, handling the 'C' locale specially and writing 6-byte lang and 4-byte country outputs. |
| `0x1035647f` | `crt_setlocale_category` | 758 | CRT __get_qualified_locale / setlocale per-category worker: sets one LC category string on the locale struct, updates MRU codepage list and ctype tables. |
| `0x10356775` | `crt_setlocale_all_parse` | 462 | CRT setlocale(LC_ALL,...) parser: handles combined 'LC_...=...;' strings or per-category application across the 6 categories, else applies one string. |
| `0x10356943` | `crt_setlocale_impl` | 329 | CRT setlocale() implementation body: locks locale, allocates a locale struct, applies category strings via sub_10356775, and commits or rolls back. |
| `0x10356a69` | `sub_10356a69` | 8 | trivial accessor/forwarder |
| `0x10356a71` | `sub_10356a71` | 9 | trivial accessor/forwarder |
| `0x10356a7a` | `sub_10356a7a` | 3 | trivial accessor/forwarder |
| `0x10356a7d` | `sub_10356a7d` | 9 | trivial accessor/forwarder |
| `0x10356a86` | `sub_10356a86` | 2 | trivial accessor/forwarder |
| `0x10356aab` | `sub_10356aab` | 3 | trivial accessor/forwarder |
| `0x10356aae` | `sub_10356aae` | 5 | trivial accessor/forwarder |
| `0x10356ab3` | `crt_lc_wcstombs_mbstowcs` | 930 | CRT LC codepage string transcoder: converts between MB and wide strings via WideCharToMultiByte/MultiByteToWideChar (g_1038b104/228/22c) with heap/_alloca buffers. |
| `0x10356e55` | `sub_10356e55` | 67 | support routine (67 bytes) |
| `0x10356e98` | `sub_10356e98` | 41 | support routine (41 bytes) |
| `0x10356ec1` | `sub_10356ec1` | 79 | support routine (79 bytes) |
| `0x10356f10` | `sub_10356f10` | 41 | support routine (41 bytes) |
| `0x10356f39` | `sub_10356f39` | 79 | support routine (79 bytes) |
| `0x10356f88` | `sub_10356f88` | 41 | support routine (41 bytes) |
| `0x10356fb1` | `sub_10356fb1` | 79 | support routine (79 bytes) |
| `0x10357000` | `sub_10357000` | 41 | support routine (41 bytes) |
| `0x10357029` | `sub_10357029` | 79 | support routine (79 bytes) |
| `0x10357078` | `sub_10357078` | 41 | support routine (41 bytes) |
| `0x103570a1` | `crt_setmbcp_build_tables` | 917 | CRT _setmbcp/__updatetmbcinfo: builds MBCS lead-byte and case-conversion tables for the codepage into the mbcinfo struct, or installs the default UTF/1252 table. |
| `0x10357436` | `sub_10357436` | 38 | support routine (38 bytes) |
| `0x1035745c` | `sub_1035745c` | 38 | support routine (38 bytes) |
| `0x10357482` | `sub_10357482` | 64 | support routine (64 bytes) |
| `0x103574c2` | `sub_103574c2` | 72 | support routine (72 bytes) |
| `0x1035750a` | `sub_1035750a` | 75 | support routine (75 bytes) |
| `0x10357555` | `sub_10357555` | 80 | support routine (80 bytes) |
| `0x103575a5` | `sub_103575a5` | 59 | support routine (59 bytes) |
| `0x103575e0` | `sub_103575e0` | 19 | support routine (19 bytes) |
| `0x103575f3` | `sub_103575f3` | 19 | support routine (19 bytes) |
| `0x10357606` | `sub_10357606` | 30 | support routine (30 bytes) |
| `0x10357624` | `crt_towlower_towupper_l` | 279 | CRT _towlower_l/_towupper_l-style char classify+convert: uses locale ctype/mbcs tables or LCMapString (sub_10356e55) for chars >=0x100. |
| `0x1035773b` | `sub_1035773b` | 39 | support routine (39 bytes) |
| `0x10357762` | `crt_strtod_locale` | 283 | CRT strtod/_strtod_l: skips locale whitespace, parses a floating-point token via sub_103602e0 producing a double (FPU-heavy, EINVAL/ERANGE handling). |
| `0x1035787d` | `sub_1035787d` | 19 | support routine (19 bytes) |
| `0x10357890` | `sub_10357890` | 11 | trivial accessor/forwarder |
| `0x1035789b` | `sub_1035789b` | 34 | support routine (34 bytes) |
| `0x103578bd` | `sub_103578bd` | 92 | support routine (92 bytes) |
| `0x10357919` | `sub_10357919` | 68 | support routine (68 bytes) |
| `0x1035795d` | `sub_1035795d` | 166 | support routine (166 bytes) |
| `0x103579df` | `sub_103579df` | 10 | trivial accessor/forwarder |
| `0x103579e9` | `sub_103579e9` | 16 | trivial accessor/forwarder |
| `0x10357a1d` | `sub_10357a1d` | 6 | trivial accessor/forwarder |
| `0x10357a23` | `sub_10357a23` | 27 | support routine (27 bytes) |
| `0x10357a3e` | `sub_10357a3e` | 69 | support routine (69 bytes) |
| `0x10357a83` | `sub_10357a83` | 67 | support routine (67 bytes) |
| `0x10357ac6` | `sub_10357ac6` | 9 | trivial accessor/forwarder |
| `0x10357acf` | `sub_10357acf` | 8 | trivial accessor/forwarder |
| `0x10357ad7` | `sub_10357ad7` | 37 | support routine (37 bytes) |
| `0x10357afc` | `sub_10357afc` | 19 | support routine (19 bytes) |
| `0x10357b0f` | `sub_10357b0f` | 121 | support routine (121 bytes) |
| `0x10357b88` | `sub_10357b88` | 49 | support routine (49 bytes) |
| `0x10357bb9` | `sub_10357bb9` | 24 | support routine (24 bytes) |
| `0x10357bd1` | `sub_10357bd1` | 172 | support routine (172 bytes) |
| `0x10357c61` | `sub_10357c61` | 9 | trivial accessor/forwarder |
| `0x10357c6a` | `sub_10357c6a` | 107 | support routine (107 bytes) |
| `0x10357cf1` | `sub_10357cf1` | 6 | trivial accessor/forwarder |
| `0x10357cf7` | `sub_10357cf7` | 118 | support routine (118 bytes) |
| `0x10357d6d` | `crt_eh_copy_ctor_helper` | 371 | CRT C++ EH __CxxFrameHandler helper: copies/constructs a catch object (bitwise, copy-ctor, or by-reference) into the catch frame per the catchable-type flags. |
| `0x10357ed8` | `sub_10357ed8` | 4 | trivial accessor/forwarder |
| `0x10357edc` | `sub_10357edc` | 8 | trivial accessor/forwarder |
| `0x10357eec` | `sub_10357eec` | 133 | support routine (133 bytes) |
| `0x10357f71` | `sub_10357f71` | 4 | trivial accessor/forwarder |
| `0x10357f75` | `sub_10357f75` | 8 | trivial accessor/forwarder |
| `0x10357f7d` | `sub_10357f7d` | 108 | support routine (108 bytes) |
| `0x10357fe9` | `sub_10357fe9` | 242 | support routine (242 bytes) |
| `0x103580db` | `crt_eh_frame_handler` | 854 | CRT C++ exception frame handler: walks try-block/catch tables of a FuncInfo, matches the thrown type, and dispatches to the catch handler / unwind. |
| `0x10358431` | `sub_10358431` | 24 | support routine (24 bytes) |
| `0x10358449` | `sub_10358449` | 228 | support routine (228 bytes) |
| `0x1035852d` | `sub_1035852d` | 243 | support routine (243 bytes) |
| `0x10358620` | `sub_10358620` | 30 | support routine (30 bytes) |
| `0x1035863e` | `sub_1035863e` | 219 | support routine (219 bytes) |
| `0x10358719` | `sub_10358719` | 40 | support routine (40 bytes) |
| `0x10358741` | `sub_10358741` | 79 | support routine (79 bytes) |
| `0x10358759` | `sub_10358759` | 7 | trivial accessor/forwarder |
| `0x10358760` | `sub_10358760` | 1 | trivial accessor/forwarder |
| `0x10358798` | `sub_10358798` | 143 | support routine (143 bytes) |
| `0x10358827` | `sub_10358827` | 20 | support routine (20 bytes) |
| `0x1035883b` | `sub_1035883b` | 129 | support routine (129 bytes) |
| `0x10358855` | `sub_10358855` | 6 | trivial accessor/forwarder |
| `0x103588c2` | `sub_103588c2` | 227 | support routine (227 bytes) |
| `0x10358aa9` | `sub_10358aa9` | 108 | support routine (108 bytes) |
| `0x10358b15` | `sub_10358b15` | 110 | support routine (110 bytes) |
| `0x10358b83` | `sub_10358b83` | 9 | trivial accessor/forwarder |
| `0x10358b8c` | `sub_10358b8c` | 110 | support routine (110 bytes) |
| `0x10358bfa` | `sub_10358bfa` | 9 | trivial accessor/forwarder |
| `0x10358c03` | `sub_10358c03` | 50 | support routine (50 bytes) |
| `0x10358c35` | `sub_10358c35` | 146 | support routine (146 bytes) |
| `0x10358c72` | `sub_10358c72` | 182 | support routine (182 bytes) |
| `0x10358d28` | `sub_10358d28` | 9 | trivial accessor/forwarder |
| `0x10358d31` | `sub_10358d31` | 119 | support routine (119 bytes) |
| `0x10358da8` | `sub_10358da8` | 24 | support routine (24 bytes) |
| `0x10358dc0` | `crt_fls_thread_cleanup` | 265 | CRT per-thread (FLS) cleanup callback: frees per-thread locale/multibyte buffers and the ptd's allocated fields, guarding static defaults. |
| `0x10358ec9` | `sub_10358ec9` | 3 | trivial accessor/forwarder |
| `0x10358ecc` | `sub_10358ecc` | 9 | trivial accessor/forwarder |
| `0x10358ed5` | `sub_10358ed5` | 3 | trivial accessor/forwarder |
| `0x10358ed8` | `sub_10358ed8` | 9 | trivial accessor/forwarder |
| `0x10358ee1` | `sub_10358ee1` | 105 | support routine (105 bytes) |
| `0x10358f4a` | `crt_init_fls` | 388 | CRT FLS init: resolves KERNEL32 FlsAlloc/Get/Set/Free (falling back to TLS shims), allocates an FLS index and installs the thread-cleanup callback. |
| `0x103590ee` | `sub_103590ee` | 4 | trivial accessor/forwarder |
| `0x103590f2` | `sub_103590f2` | 3 | trivial accessor/forwarder |
| `0x10359107` | `sub_10359107` | 19 | support routine (19 bytes) |
| `0x1035911a` | `sub_1035911a` | 98 | support routine (98 bytes) |
| `0x1035913e` | `sub_1035913e` | 4 | trivial accessor/forwarder |
| `0x10359142` | `sub_10359142` | 3 | trivial accessor/forwarder |
| `0x10359151` | `sub_10359151` | 17 | support routine (17 bytes) |
| `0x10359170` | `sub_10359170` | 76 | support routine (76 bytes) |
| `0x103591bc` | `crt_fputc_flush` | 352 | CRT _flsbuf/_fputc worker: flushes a FILE stream buffer, handling buffering flags, low-level _write, and error/EOF status bit updates. |
| `0x1035931c` | `sub_1035931c` | 51 | support routine (51 bytes) |
| `0x1035934f` | `sub_1035934f` | 36 | support routine (36 bytes) |
| `0x10359373` | `crt_scanf_engine` | 490 | CRT scanf-family core (_input_l): drives the format-string state machine over a stream, dispatching conversion specifiers via a jump table. |
| `0x1035951c` | `sub_1035951c` | 27 | support routine (27 bytes) |
| `0x10359537` | `sub_10359537` | 79 | support routine (79 bytes) |
| `0x10359586` | `sub_10359586` | 58 | support routine (58 bytes) |
| `0x103595c0` | `sub_103595c0` | 8 | trivial accessor/forwarder |
| `0x103595c8` | `sub_103595c8` | 55 | support routine (55 bytes) |
| `0x103595ff` | `crt_scanf_length_modifier` | 271 | CRT scanf format helper: parses length/type modifiers (I64/I32, h, l, ll, w) setting the conversion width/size flags. |
| `0x103596f7` | `crt_printf_format_specifier` | 1432 | CRT printf-family core (_output): formats one conversion specifier (d/i/o/u/x/e/f/g/s/c/n/p), producing digits, padding and sign into the output. |
| `0x10359d07` | `sub_10359d07` | 202 | support routine (202 bytes) |
| `0x10359dd1` | `sub_10359dd1` | 134 | support routine (134 bytes) |
| `0x10359e57` | `sub_10359e57` | 103 | support routine (103 bytes) |
| `0x10359ebe` | `sub_10359ebe` | 9 | trivial accessor/forwarder |
| `0x10359ed0` | `sub_10359ed0` | 135 | support routine (135 bytes) |
| `0x10359f13` | `sub_10359f13` | 1 | trivial accessor/forwarder |
| `0x10359f58` | `sub_10359f58` | 101 | support routine (101 bytes) |
| `0x10359fbd` | `crt_report_runtime_error` | 416 | CRT __crtMessageBox / _NMSG_WRITE: maps a runtime-error code to a message and shows it via MessageBox, or writes to stderr (VC runtime error text). |
| `0x1035a15d` | `sub_1035a15d` | 57 | support routine (57 bytes) |
| `0x1035a196` | `crt_getlocaleinfo_alloc` | 346 | CRT __crtGetLocaleInfoA wrapper: calls GetLocaleInfo into a stack/heap buffer and returns an allocated copy of the locale string or integer value. |
| `0x1035a2f0` | `sub_1035a2f0` | 10 | trivial accessor/forwarder |
| `0x1035a2fa` | `sub_1035a2fa` | 91 | support routine (91 bytes) |
| `0x1035a355` | `sub_1035a355` | 90 | support routine (90 bytes) |
| `0x1035a3af` | `sub_1035a3af` | 116 | support routine (116 bytes) |
| `0x1035a423` | `sub_1035a423` | 73 | support routine (73 bytes) |
| `0x1035a4c1` | `sub_1035a4c1` | 21 | support routine (21 bytes) |
| `0x1035a4d6` | `sub_1035a4d6` | 184 | support routine (184 bytes) |
| `0x1035a508` | `sub_1035a508` | 2 | trivial accessor/forwarder |
| `0x1035a590` | `sub_1035a590` | 9 | trivial accessor/forwarder |
| `0x1035a599` | `sub_1035a599` | 49 | support routine (49 bytes) |
| `0x1035a5ca` | `sub_1035a5ca` | 72 | support routine (72 bytes) |
| `0x1035a612` | `sub_1035a612` | 43 | support routine (43 bytes) |
| `0x1035a63d` | `sub_1035a63d` | 788 | support routine (788 bytes) |
| `0x1035a951` | `sub_1035a951` | 176 | support routine (176 bytes) |
| `0x1035aa01` | `sub_1035aa01` | 262 | support routine (262 bytes) |
| `0x1035ab07` | `sub_1035ab07` | 735 | support routine (735 bytes) |
| `0x1035ade6` | `sub_1035ade6` | 739 | support routine (739 bytes) |
| `0x1035b0cc` | `sub_1035b0cc` | 69 | support routine (69 bytes) |
| `0x1035b111` | `sub_1035b111` | 20 | support routine (20 bytes) |
| `0x1035b125` | `sub_1035b125` | 8 | trivial accessor/forwarder |
| `0x1035b12d` | `sub_1035b12d` | 47 | support routine (47 bytes) |
| `0x1035b15c` | `sub_1035b15c` | 85 | support routine (85 bytes) |
| `0x1035b1b1` | `crt_ctype_build_ctable` | 394 | CRT locale ctype-table builder: fills the 256-entry _pctype and case-conversion arrays via GetStringType/LCMapString or the C-locale ASCII fallback. |
| `0x1035b33b` | `sub_1035b33b` | 152 | support routine (152 bytes) |
| `0x1035b3d3` | `sub_1035b3d3` | 3 | trivial accessor/forwarder |
| `0x1035b3d6` | `sub_1035b3d6` | 9 | trivial accessor/forwarder |
| `0x1035b3df` | `sub_1035b3df` | 122 | support routine (122 bytes) |
| `0x1035b459` | `crt_setmbcp_codepage_info` | 473 | CRT __getmbcp/__setmbcp helper: initializes an mbcinfo struct for a codepage (932/936/etc. lead/trail ranges) or via GetCPInfo/GetStringType tables. |
| `0x1035b632` | `crt_setmbcp_locked` | 399 | CRT _setmbcp implementation: allocates a 544-byte mbcinfo, populates it via sub_1035b459, publishes it and updates the global MBCS lead/case tables. |
| `0x1035b793` | `sub_1035b793` | 9 | trivial accessor/forwarder |
| `0x1035b79c` | `sub_1035b79c` | 2 | trivial accessor/forwarder |
| `0x1035b7cc` | `sub_1035b7cc` | 30 | support routine (30 bytes) |
| `0x1035b7ea` | `sub_1035b7ea` | 182 | support routine (182 bytes) |
| `0x1035b8a0` | `sub_1035b8a0` | 149 | support routine (149 bytes) |
| `0x1035b935` | `sub_1035b935` | 113 | support routine (113 bytes) |
| `0x1035b9a6` | `sub_1035b9a6` | 128 | support routine (128 bytes) |
| `0x1035ba26` | `sub_1035ba26` | 22 | support routine (22 bytes) |
| `0x1035ba3c` | `sub_1035ba3c` | 64 | support routine (64 bytes) |
| `0x1035ba7e` | `sub_1035ba7e` | 21 | support routine (21 bytes) |
| `0x1035ba93` | `sub_1035ba93` | 29 | support routine (29 bytes) |
| `0x1035bab2` | `sub_1035bab2` | 12 | trivial accessor/forwarder |
| `0x1035bac0` | `sub_1035bac0` | 12 | trivial accessor/forwarder |
| `0x1035bacc` | `crt_cvt_write_exponent` | 365 | CRT _cftoe/_fcvt-family formatter: writes the exponent part ('e+000') and inserts the locale decimal point into a converted floating-point string. |
| `0x1035bc39` | `sub_1035bc39` | 206 | support routine (206 bytes) |
| `0x1035bd07` | `sub_1035bd07` | 30 | support routine (30 bytes) |
| `0x1035bd25` | `crt_cvt_hexfloat` | 881 | CRT %a hex-float formatter (_cfltcvt): converts a double to a '0x1.hhhp+e' hexadecimal-float string with rounding, sign and exponent. |
| `0x1035c096` | `sub_1035c096` | 245 | support routine (245 bytes) |
| `0x1035c18b` | `sub_1035c18b` | 185 | support routine (185 bytes) |
| `0x1035c244` | `sub_1035c244` | 248 | support routine (248 bytes) |
| `0x1035c33c` | `sub_1035c33c` | 134 | support routine (134 bytes) |
| `0x1035c3c2` | `sub_1035c3c2` | 33 | support routine (33 bytes) |
| `0x1035c3e3` | `sub_1035c3e3` | 31 | support routine (31 bytes) |
| `0x1035c402` | `sub_1035c402` | 41 | support routine (41 bytes) |
| `0x1035c467` | `sub_1035c467` | 101 | support routine (101 bytes) |
| `0x1035c490` | `sub_1035c490` | 146 | support routine (146 bytes) |
| `0x1035c522` | `sub_1035c522` | 8 | trivial accessor/forwarder |
| `0x1035c52a` | `sub_1035c52a` | 9 | trivial accessor/forwarder |
| `0x1035c533` | `sub_1035c533` | 36 | support routine (36 bytes) |
| `0x1035c557` | `sub_1035c557` | 36 | support routine (36 bytes) |
| `0x1035c580` | `sub_1035c580` | 41 | support routine (41 bytes) |
| `0x1035c5b0` | `sub_1035c5b0` | 66 | support routine (66 bytes) |
| `0x1035c600` | `sub_1035c600` | 164 | support routine (164 bytes) |
| `0x1035c689` | `sub_1035c689` | 20 | support routine (20 bytes) |
| `0x1035c69d` | `sub_1035c69d` | 3 | trivial accessor/forwarder |
| `0x1035c6bb` | `sub_1035c6bb` | 1 | trivial accessor/forwarder |
| `0x1035c6bc` | `sub_1035c6bc` | 350 | support routine (350 bytes) |
| `0x1035c81a` | `sub_1035c81a` | 27 | support routine (27 bytes) |
| `0x1035c835` | `sub_1035c835` | 25 | support routine (25 bytes) |
| `0x1035c84e` | `sub_1035c84e` | 52 | support routine (52 bytes) |
| `0x1035c882` | `sub_1035c882` | 13 | trivial accessor/forwarder |
| `0x1035c88f` | `crt_signal_raise` | 411 | CRT raise() implementation: looks up the signal's handler table entry (SIGINT/ILL/FPE/SEGV/TERM/ABRT/BREAK), resets it, and invokes the handler. |
| `0x1035c9fd` | `sub_1035c9fd` | 6 | trivial accessor/forwarder |
| `0x1035ca03` | `sub_1035ca03` | 15 | trivial accessor/forwarder |
| `0x1035ca3f` | `sub_1035ca3f` | 10 | trivial accessor/forwarder |
| `0x1035ca49` | `sub_1035ca49` | 10 | trivial accessor/forwarder |
| `0x1035ca53` | `sub_1035ca53` | 16 | trivial accessor/forwarder |
| `0x1035ca63` | `sub_1035ca63` | 150 | support routine (150 bytes) |
| `0x1035cae9` | `sub_1035cae9` | 23 | support routine (23 bytes) |
| `0x1035cb00` | `sub_1035cb00` | 24 | support routine (24 bytes) |
| `0x1035cb28` | `sub_1035cb28` | 144 | support routine (144 bytes) |
| `0x1035cbb8` | `sub_1035cbb8` | 33 | support routine (33 bytes) |
| `0x1035cbd8` | `sub_1035cbd8` | 37 | support routine (37 bytes) |
| `0x1035cbfe` | `sub_1035cbfe` | 28 | support routine (28 bytes) |
| `0x1035cc1a` | `sub_1035cc1a` | 23 | support routine (23 bytes) |
| `0x1035cc4a` | `sub_1035cc4a` | 26 | support routine (26 bytes) |
| `0x1035cc64` | `sub_1035cc64` | 23 | support routine (23 bytes) |
| `0x1035cc7b` | `sub_1035cc7b` | 6 | trivial accessor/forwarder |
| `0x1035cc81` | `sub_1035cc81` | 177 | support routine (177 bytes) |
| `0x1035cd32` | `sub_1035cd32` | 32 | support routine (32 bytes) |
| `0x1035cd52` | `sub_1035cd52` | 60 | support routine (60 bytes) |
| `0x1035cd8e` | `sub_1035cd8e` | 46 | support routine (46 bytes) |
| `0x1035cdbc` | `sub_1035cdbc` | 54 | support routine (54 bytes) |
| `0x1035cdf2` | `sub_1035cdf2` | 42 | support routine (42 bytes) |
| `0x1035ce1c` | `crt_parse_fopen_mode` | 672 | CRT _openfile mode parser (narrow): parses fopen mode string ('r/w/a' + b/t/+/S/R/T/D/N/ccs=) into oflag/commit flags and opens the fd. |
| `0x1035d0bc` | `crt_ioinit_alloc_fh` | 292 | CRT __ioinit / _alloc_osfhnd: grows the file-handle (_iob/ioinfo) table, allocating and initializing new ioinfo blocks under lock. |
| `0x1035d1e0` | `sub_1035d1e0` | 3 | trivial accessor/forwarder |
| `0x1035d1e3` | `sub_1035d1e3` | 9 | trivial accessor/forwarder |
| `0x1035d1ec` | `crt_parse_wfopen_mode` | 652 | CRT _wopenfile mode parser (wide): wide-char counterpart of sub_1035ce1c parsing wchar fopen mode + ccs= into oflag and opening the fd. |
| `0x1035d478` | `sub_1035d478` | 72 | support routine (72 bytes) |
| `0x1035d4c0` | `sub_1035d4c0` | 52 | support routine (52 bytes) |
| `0x1035d4f4` | `sub_1035d4f4` | 52 | support routine (52 bytes) |
| `0x1035d528` | `sub_1035d528` | 52 | support routine (52 bytes) |
| `0x1035d55c` | `sub_1035d55c` | 6 | trivial accessor/forwarder |
| `0x1035d562` | `sub_1035d562` | 6 | trivial accessor/forwarder |
| `0x1035d568` | `sub_1035d568` | 6 | trivial accessor/forwarder |
| `0x1035d56e` | `sub_1035d56e` | 6 | trivial accessor/forwarder |
| `0x1035d574` | `crt_tzset` | 827 | CRT _tzset implementation: reads the TZ env var (or GetTimeZoneInformation), parsing offset/DST names into _timezone/_daylight/_tzname globals. |
| `0x1035d81e` | `sub_1035d81e` | 5 | trivial accessor/forwarder |
| `0x1035d823` | `sub_1035d823` | 9 | trivial accessor/forwarder |
| `0x1035d8bd` | `sub_1035d8bd` | 501 | support routine (501 bytes) |
| `0x1035dab2` | `crt_isindst` | 430 | CRT _isindst: given a tm computes whether the time falls within the daylight-saving window using the cached DST start/end rules. |
| `0x1035dc60` | `sub_1035dc60` | 70 | support routine (70 bytes) |
| `0x1035dca6` | `sub_1035dca6` | 9 | trivial accessor/forwarder |
| `0x1035dcaf` | `sub_1035dcaf` | 56 | support routine (56 bytes) |
| `0x1035dce7` | `sub_1035dce7` | 9 | trivial accessor/forwarder |
| `0x1035dcf0` | `sub_1035dcf0` | 53 | support routine (53 bytes) |
| `0x1035dd25` | `sub_1035dd25` | 211 | support routine (211 bytes) |
| `0x1035ddf8` | `sub_1035ddf8` | 80 | support routine (80 bytes) |
| `0x1035de48` | `sub_1035de48` | 54 | support routine (54 bytes) |
| `0x1035de7e` | `sub_1035de7e` | 14 | trivial accessor/forwarder |
| `0x1035de90` | `sub_1035de90` | 22 | support routine (22 bytes) |
| `0x1035dea6` | `sub_1035dea6` | 22 | support routine (22 bytes) |
| `0x1035debc` | `crt_ioinit_std_handles` | 562 | CRT __ioinit: allocates the initial ioinfo handle arrays and inherits/initializes std handles (stdin/out/err) with their file-type flags. |
| `0x1035e0e5` | `sub_1035e0e5` | 4 | trivial accessor/forwarder |
| `0x1035e0e9` | `sub_1035e0e9` | 10 | trivial accessor/forwarder |
| `0x1035e0fc` | `sub_1035e0fc` | 76 | support routine (76 bytes) |
| `0x1035e148` | `sub_1035e148` | 219 | support routine (219 bytes) |
| `0x1035e223` | `crt_parse_cmdline` | 408 | CRT _parse_cmdline / __crtGetCommandLine tokenizer: splits a command line into argv[] handling quotes and backslash-quote escaping, counting bytes. |
| `0x1035e3bb` | `sub_1035e3bb` | 185 | support routine (185 bytes) |
| `0x1035e474` | `crt_get_env_a` | 309 | CRT __crtGetEnvironmentStringsA: fetches the process environment block (wide preferred, converted to ANSI) into a freshly allocated buffer. |
| `0x1035e5a9` | `sub_1035e5a9` | 148 | support routine (148 bytes) |
| `0x1035e63d` | `crt_init_lc_time_names` | 1049 | CRT __init_time / lc_time init: fills the __lc_time_data struct by fetching ~45 GetLocaleInfo LOCALE_S* fields (day/month names, formats) for the locale. |
| `0x1035ea56` | `crt_unaligned_block_copy` | 400 | Copies 43 dwords from a table pointer into locals, each followed by a helper call; MSVC CRT/inlined block-copy or checksum loop, not bot logic. |
| `0x1035ebe6` | `sub_1035ebe6` | 115 | support routine (115 bytes) |
| `0x1035ec59` | `sub_1035ec59` | 64 | support routine (64 bytes) |
| `0x1035ec99` | `crt_setloc_ctype` | 456 | MSVC CRT locale setup: allocates locale node, reads ctype/category strings via __crtGetLocaleInfoA (sub_1035a196), rebuilds refcounted lc_category table. |
| `0x1035ee61` | `sub_1035ee61` | 137 | support routine (137 bytes) |
| `0x1035eeea` | `crt_setloc_monetary` | 708 | MSVC CRT __getlocaleinfo variant: allocates locale struct, fetches ~16 LC_MONETARY/NUMERIC fields via sub_1035a196, semicolon-strips grouping string, updates refcounts. |
| `0x1035f1ae` | `sub_1035f1ae` | 3 | trivial accessor/forwarder |
| `0x1035f1b1` | `sub_1035f1b1` | 113 | support routine (113 bytes) |
| `0x1035f222` | `sub_1035f222` | 179 | support routine (179 bytes) |
| `0x1035f2d5` | `sub_1035f2d5` | 96 | support routine (96 bytes) |
| `0x1035f335` | `sub_1035f335` | 119 | support routine (119 bytes) |
| `0x1035f3ac` | `sub_1035f3ac` | 30 | support routine (30 bytes) |
| `0x1035f3ca` | `sub_1035f3ca` | 50 | support routine (50 bytes) |
| `0x1035f3fc` | `sub_1035f3fc` | 27 | support routine (27 bytes) |
| `0x1035f417` | `sub_1035f417` | 150 | support routine (150 bytes) |
| `0x1035f4ad` | `sub_1035f4ad` | 114 | support routine (114 bytes) |
| `0x1035f51f` | `crt_get_qualified_locale_lcid` | 464 | MSVC CRT __get_qualified_locale: probes LCID against language/country/codepage via GetLocaleInfo (g_1038b1e4) to resolve a fully-qualified locale. |
| `0x1035f6ef` | `sub_1035f6ef` | 191 | support routine (191 bytes) |
| `0x1035f7ae` | `sub_1035f7ae` | 101 | support routine (101 bytes) |
| `0x1035f813` | `sub_1035f813` | 60 | support routine (60 bytes) |
| `0x1035f84f` | `crt_get_lc_all_name` | 483 | MSVC CRT locale-name parser: splits LC_ALL string into language/country/codepage, validates codepage (g_1038b264/IsValidCodePage), handles Norwegian-Nynorsk special case. |
| `0x1035fa32` | `crt_lc_wctomb_l` | 440 | MSVC CRT __crtLCMapStringA/wctomb path with W2A fallback: uses GetStringTypeW/WideCharToMultiByte thunks, __malloc_crt scratch buffer, ANSI codepage mapping. |
| `0x1035fbea` | `sub_1035fbea` | 64 | support routine (64 bytes) |
| `0x1035fc2a` | `sub_1035fc2a` | 190 | support routine (190 bytes) |
| `0x1035fcf0` | `sub_1035fcf0` | 64 | support routine (64 bytes) |
| `0x1035fd30` | `sub_1035fd30` | 71 | support routine (71 bytes) |
| `0x1035fd77` | `crt_wcstombs_via_widechar` | 434 | MSVC CRT string transcode: MultiByteToWideChar then WideCharToMultiByte (g_1038b104/g_1038b040) with __malloc_crt scratch buffer, one codepage to another. |
| `0x1035ff29` | `crt_calloc_impl` | 272 | MSVC CRT calloc/_calloc_base: overflow-checks count*size, locks heap g_103a13c0, allocates (HeapAlloc g_1038b220) and zero-fills, retries via _callnewh. |
| `0x10360020` | `sub_10360020` | 5 | trivial accessor/forwarder |
| `0x10360025` | `sub_10360025` | 9 | trivial accessor/forwarder |
| `0x10360047` | `crt_realloc_impl` | 524 | MSVC CRT realloc/_realloc_base: locks heap, tries in-place small-block regrow (sub_1035a612) else HeapReAlloc (g_1038b258), retry loop, sets errno. |
| `0x10360185` | `sub_10360185` | 6 | trivial accessor/forwarder |
| `0x1036018b` | `sub_1036018b` | 9 | trivial accessor/forwarder |
| `0x10360262` | `sub_10360262` | 121 | support routine (121 bytes) |
| `0x103602e0` | `sub_103602e0` | 165 | support routine (165 bytes) |
| `0x10360385` | `sub_10360385` | 13 | trivial accessor/forwarder |
| `0x10360392` | `sub_10360392` | 45 | support routine (45 bytes) |
| `0x103603af` | `sub_103603af` | 28 | support routine (28 bytes) |
| `0x103603cb` | `sub_103603cb` | 7 | trivial accessor/forwarder |
| `0x103603e2` | `sub_103603e2` | 96 | support routine (96 bytes) |
| `0x10360442` | `sub_10360442` | 13 | trivial accessor/forwarder |
| `0x10360450` | `sub_10360450` | 32 | support routine (32 bytes) |
| `0x10360470` | `sub_10360470` | 33 | support routine (33 bytes) |
| `0x10360490` | `sub_10360490` | 36 | support routine (36 bytes) |
| `0x103604b5` | `sub_103604b5` | 132 | support routine (132 bytes) |
| `0x10360539` | `sub_10360539` | 35 | support routine (35 bytes) |
| `0x1036055c` | `sub_1036055c` | 29 | support routine (29 bytes) |
| `0x10360565` | `sub_10360565` | 11 | trivial accessor/forwarder |
| `0x10360584` | `sub_10360584` | 3 | trivial accessor/forwarder |
| `0x10360587` | `sub_10360587` | 131 | support routine (131 bytes) |
| `0x1036060a` | `crt_fileno_to_osfhandle` | 271 | MSVC CRT _get_osfhandle: validates fd against __pioinfo table g_103a3b80, checks FOPEN flag, returns underlying OS handle or EBADF. |
| `0x10360719` | `sub_10360719` | 10 | trivial accessor/forwarder |
| `0x10360723` | `crt_write_translate` | 1478 | MSVC CRT _write text/unicode translation: LF->CRLF expansion and MBCS/UTF-16/UTF-8 conversion (g_1038b040/g_1038b244) before WriteFile on an fd. |
| `0x10360ce9` | `sub_10360ce9` | 210 | support routine (210 bytes) |
| `0x10360dbb` | `sub_10360dbb` | 10 | trivial accessor/forwarder |
| `0x10360dc5` | `sub_10360dc5` | 68 | support routine (68 bytes) |
| `0x10360e09` | `sub_10360e09` | 94 | support routine (94 bytes) |
| `0x10360e67` | `sub_10360e67` | 45 | support routine (45 bytes) |
| `0x10360e94` | `sub_10360e94` | 22 | support routine (22 bytes) |
| `0x10360eaa` | `crt_wctomb_s_l` | 351 | MSVC CRT wctomb_s/_wctomb_s_l: converts one wide char to multibyte via WideCharToMultiByte (g_1038b040), validates buffer, sets EILSEQ/EINVAL. |
| `0x10361009` | `sub_10361009` | 27 | support routine (27 bytes) |
| `0x10361024` | `sub_10361024` | 74 | support routine (74 bytes) |
| `0x1036106e` | `crt_output_format_core` | 2447 | MSVC CRT _output/printf engine: parses format flags/width/precision, dispatches conversions (d,i,o,x,e,f,g,s,c,n,p), builds field with padding. |
| `0x10361a1e` | `crt_message_box_report` | 445 | MSVC CRT __crtMessageBoxA: dynamically loads USER32 MessageBoxA/GetActiveWindow/GetProcessWindowStation, adjusts flags for non-interactive station, shows box. |
| `0x10361bdb` | `sub_10361bdb` | 70 | support routine (70 bytes) |
| `0x10361c21` | `crt_wide_write_console_a` | 315 | MSVC CRT ANSI console/text output helper with A/W fallback (g_1038b198), __malloc_crt scratch, MultiByteToWideChar (g_1038b1e4) then output. |
| `0x10361d5c` | `sub_10361d5c` | 59 | support routine (59 bytes) |
| `0x10361d97` | `crt_wide_write_console_w` | 317 | Sibling of sub_10361c21: wide-to-ANSI console output with A/W runtime detection, scratch buffer, WideCharToMultiByte fallback path. |
| `0x10361ed4` | `sub_10361ed4` | 59 | support routine (59 bytes) |
| `0x10361f0f` | `sub_10361f0f` | 166 | support routine (166 bytes) |
| `0x10361fb5` | `sub_10361fb5` | 166 | support routine (166 bytes) |
| `0x1036205b` | `sub_1036205b` | 189 | support routine (189 bytes) |
| `0x10362118` | `sub_10362118` | 187 | support routine (187 bytes) |
| `0x103621d3` | `sub_103621d3` | 142 | support routine (142 bytes) |
| `0x10362270` | `sub_10362270` | 223 | support routine (223 bytes) |
| `0x10362350` | `sub_10362350` | 31 | support routine (31 bytes) |
| `0x1036236f` | `sub_1036236f` | 9 | trivial accessor/forwarder |
| `0x10362378` | `sub_10362378` | 106 | support routine (106 bytes) |
| `0x103623e2` | `sub_103623e2` | 150 | support routine (150 bytes) |
| `0x10362478` | `sub_10362478` | 9 | trivial accessor/forwarder |
| `0x10362481` | `sub_10362481` | 98 | support routine (98 bytes) |
| `0x103624e3` | `sub_103624e3` | 66 | support routine (66 bytes) |
| `0x10362525` | `sub_10362525` | 187 | support routine (187 bytes) |
| `0x103625c2` | `sub_103625c2` | 5 | trivial accessor/forwarder |
| `0x103625c7` | `sub_103625c7` | 17 | support routine (17 bytes) |
| `0x103625f6` | `sub_103625f6` | 9 | trivial accessor/forwarder |
| `0x103625ff` | `sub_103625ff` | 9 | trivial accessor/forwarder |
| `0x10362608` | `crt_openfile_a` | 1881 | MSVC CRT _openfile/_sopen: maps fopen mode+share flags to CreateFileA (g_1038b120) access/disposition, allocates fd slot, detects UTF-8/UTF-16 BOM. |
| `0x10362d61` | `sub_10362d61` | 153 | support routine (153 bytes) |
| `0x10362dfa` | `sub_10362dfa` | 5 | trivial accessor/forwarder |
| `0x10362dff` | `sub_10362dff` | 46 | support routine (46 bytes) |
| `0x10362e2d` | `sub_10362e2d` | 30 | support routine (30 bytes) |
| `0x10362e4b` | `crt_strcoll_l` | 538 | MSVC CRT _strcoll_l/mbtowc collate: per-char LCMapString compare (sub_10356e55) of two MBCS strings under a locale, falls back to plain strcmp. |
| `0x10363065` | `sub_10363065` | 19 | support routine (19 bytes) |
| `0x10363078` | `crt_strncoll_l` | 361 | MSVC CRT _strncoll_l: length-bounded MBCS collation compare using lead-byte handling and LCMapString, else __strncmp fallback (sub_1035fc2a). |
| `0x103631e1` | `sub_103631e1` | 23 | support routine (23 bytes) |
| `0x103631f8` | `crt_openfile_a_variant` | 1882 | Near-duplicate of sub_10362608 CRT _openfile using CreateFile thunk g_1038b194: fopen-mode to Win32 flag translation, fd allocation, BOM detection. |
| `0x10363952` | `sub_10363952` | 153 | support routine (153 bytes) |
| `0x103639eb` | `sub_103639eb` | 5 | trivial accessor/forwarder |
| `0x103639f0` | `sub_103639f0` | 46 | support routine (46 bytes) |
| `0x10363a1e` | `sub_10363a1e` | 30 | support routine (30 bytes) |
| `0x10363a3c` | `crt_wcsicoll_l` | 271 | MSVC CRT _wcsicoll_l/wcsicmp: case-insensitive wide-string compare, ASCII lowercasing fast path or per-char locale fold (sub_10367127). |
| `0x10363b4b` | `sub_10363b4b` | 145 | support routine (145 bytes) |
| `0x10363bdc` | `sub_10363bdc` | 53 | support routine (53 bytes) |
| `0x10363c11` | `sub_10363c11` | 17 | support routine (17 bytes) |
| `0x10363c22` | `sub_10363c22` | 129 | support routine (129 bytes) |
| `0x10363ca3` | `sub_10363ca3` | 130 | support routine (130 bytes) |
| `0x10363d25` | `sub_10363d25` | 81 | support routine (81 bytes) |
| `0x10363d76` | `sub_10363d76` | 19 | support routine (19 bytes) |
| `0x10363d89` | `sub_10363d89` | 240 | support routine (240 bytes) |
| `0x10363e79` | `sub_10363e79` | 92 | support routine (92 bytes) |
| `0x10363ed5` | `sub_10363ed5` | 1346 | support routine (1346 bytes) |
| `0x10364417` | `sub_10364417` | 1346 | support routine (1346 bytes) |
| `0x10364959` | `crt_strtod_parse` | 1680 | MSVC CRT strtod/_strtod_l: skips whitespace then parses a floating-point numeric literal from a string under locale (idx), sets EINVAL if empty. |
| `0x10365019` | `sub_10365019` | 125 | support routine (125 bytes) |
| `0x10365096` | `sub_10365096` | 129 | support routine (129 bytes) |
| `0x10365117` | `sub_10365117` | 113 | support routine (113 bytes) |
| `0x10365188` | `sub_10365188` | 146 | support routine (146 bytes) |
| `0x1036521a` | `sub_1036521a` | 5 | trivial accessor/forwarder |
| `0x1036521f` | `sub_1036521f` | 9 | trivial accessor/forwarder |
| `0x10365228` | `sub_10365228` | 34 | support routine (34 bytes) |
| `0x1036524a` | `crt_alloc_fd_slot` | 391 | MSVC CRT _alloc_osfhnd: scans/locks __pioinfo table g_103a3b80, allocates a free fd entry (growing table via sub_103574c2), returns fd index. |
| `0x10365317` | `sub_10365317` | 6 | trivial accessor/forwarder |
| `0x1036531d` | `sub_1036531d` | 9 | trivial accessor/forwarder |
| `0x103653e0` | `sub_103653e0` | 9 | trivial accessor/forwarder |
| `0x103653e9` | `sub_103653e9` | 194 | support routine (194 bytes) |
| `0x103654ab` | `crt_wctomb_internal` | 275 | MSVC CRT internal wide-to-multibyte single-char convert: uses locale mbtable (v2+20) or WideCharToMultiByte (g_1038b104), returns byte count. |
| `0x103655be` | `sub_103655be` | 23 | support routine (23 bytes) |
| `0x103655d5` | `crt_strtoul_parse` | 555 | MSVC CRT strtol/strtoul/_strtoxl_l: parses signed/unsigned integer in radix 2..36 with sign/prefix handling and overflow clamp under locale. |
| `0x10365800` | `sub_10365800` | 41 | support routine (41 bytes) |
| `0x10365829` | `crt_cvt_float_to_string` | 2246 | MSVC CRT floating-point formatting core (_cfltcvt/_fassign): converts a double to decimal digit string with rounding, exponent, and sign fields. |
| `0x103660ef` | `sub_103660ef` | 142 | support routine (142 bytes) |
| `0x1036617d` | `sub_1036617d` | 160 | support routine (160 bytes) |
| `0x1036621d` | `crt_control87_fpflags` | 771 | MSVC CRT _control87/_statusfp: reads x87/SSE control-status words and translates hardware exception/rounding bits into CRT flag bitmask. |
| `0x10366520` | `sub_10366520` | 114 | support routine (114 bytes) |
| `0x10366592` | `sub_10366592` | 113 | support routine (113 bytes) |
| `0x10366603` | `sub_10366603` | 3 | trivial accessor/forwarder |
| `0x10366606` | `sub_10366606` | 8 | trivial accessor/forwarder |
| `0x1036660e` | `sub_1036660e` | 215 | support routine (215 bytes) |
| `0x103666e5` | `sub_103666e5` | 10 | trivial accessor/forwarder |
| `0x103666ef` | `crt_lseek_i64` | 436 | MSVC CRT _lseeki64: seeks an fd, resyncs text-mode/pipe buffering and CRLF lookahead state before/after the Win32 SetFilePointer call. |
| `0x103668a3` | `crt_read_translate` | 1473 | MSVC CRT _read text/unicode translation: ReadFile then CRLF->LF collapse and MBCS/UTF-16/UTF-8 decode into caller buffer for a text-mode fd. |
| `0x10366e64` | `sub_10366e64` | 148 | support routine (148 bytes) |
| `0x10366ef8` | `sub_10366ef8` | 195 | support routine (195 bytes) |
| `0x10366fbb` | `sub_10366fbb` | 10 | trivial accessor/forwarder |
| `0x10366fc5` | `sub_10366fc5` | 114 | support routine (114 bytes) |
| `0x10367037` | `sub_10367037` | 188 | support routine (188 bytes) |
| `0x103670f3` | `sub_103670f3` | 52 | support routine (52 bytes) |
| `0x10367127` | `sub_10367127` | 173 | support routine (173 bytes) |
| `0x103671d4` | `sub_103671d4` | 236 | support routine (236 bytes) |
| `0x103672c0` | `sub_103672c0` | 23 | support routine (23 bytes) |
| `0x103672d7` | `sub_103672d7` | 149 | support routine (149 bytes) |
| `0x1036736c` | `crt_lc_mbtowc_l` | 548 | MSVC CRT __crtLCMapStringA/mbtowc path with A/W fallback and __malloc_crt scratch: multibyte-to-wide locale mapping (g_1038b040/g_1038b1ac). |
| `0x10367590` | `sub_10367590` | 62 | support routine (62 bytes) |
| `0x103675d0` | `sub_103675d0` | 97 | support routine (97 bytes) |
| `0x10367631` | `sub_10367631` | 460 | support routine (460 bytes) |
| `0x103677fd` | `sub_103677fd` | 31 | support routine (31 bytes) |
| `0x1036781c` | `sub_1036781c` | 45 | support routine (45 bytes) |
| `0x10367849` | `sub_10367849` | 68 | support routine (68 bytes) |
| `0x10367876` | `sub_10367876` | 28 | support routine (28 bytes) |
| `0x10367892` | `sub_10367892` | 18 | support routine (18 bytes) |
| `0x103678bb` | `sub_103678bb` | 44 | support routine (44 bytes) |
| `0x103678e7` | `crt_getstringtype_w` | 609 | MSVC CRT __crtGetStringTypeA: A/W runtime detection, converts MBCS to UTF-16 (g_1038b104) then GetStringTypeW (g_1038b228) with scratch buffer. |
| `0x10367b48` | `sub_10367b48` | 64 | support routine (64 bytes) |
| `0x10367b88` | `crt_comparestring_a` | 905 | MSVC CRT __crtCompareStringA: A/W fallback CompareString (g_1038b174/g_1038b178) transcoding both operands to UTF-16 with __malloc_crt scratch. |
| `0x10367f11` | `sub_10367f11` | 64 | support routine (64 bytes) |
| `0x10367f51` | `sub_10367f51` | 248 | support routine (248 bytes) |
| `0x10368049` | `sub_10368049` | 77 | support routine (77 bytes) |
| `0x10368096` | `sub_10368096` | 93 | support routine (93 bytes) |
| `0x103680f3` | `crt_mbtowc_onechar` | 588 | MSVC CRT _mbtowc internal: decodes one (possibly lead+trail) MBCS char to wide using __mbctype table g_103a3020 / MultiByteToWideChar. |
| `0x1036833f` | `sub_1036833f` | 80 | support routine (80 bytes) |
| `0x1036838f` | `sub_1036838f` | 186 | support routine (186 bytes) |
| `0x10368449` | `sub_10368449` | 19 | support routine (19 bytes) |
| `0x10368460` | `sub_10368460` | 10 | trivial accessor/forwarder |
| `0x10368470` | `sub_10368470` | 209 | support routine (209 bytes) |
| `0x10368550` | `sub_10368550` | 209 | support routine (209 bytes) |
| `0x10368630` | `sub_10368630` | 28 | support routine (28 bytes) |
| `0x10368650` | `sub_10368650` | 28 | support routine (28 bytes) |
| `0x10368670` | `sub_10368670` | 174 | support routine (174 bytes) |
| `0x10368720` | `sub_10368720` | 174 | support routine (174 bytes) |
| `0x103687d0` | `sub_103687d0` | 23 | support routine (23 bytes) |
| `0x103687f0` | `sub_103687f0` | 23 | support routine (23 bytes) |
| `0x10368810` | `sub_10368810` | 40 | support routine (40 bytes) |
| `0x1036881d` | `sub_1036881d` | 3 | trivial accessor/forwarder |
| `0x10368840` | `crt_seh_wrapped_op_a` | 406 | MSVC CRT routine guarded by a fs:[0] SEH __except frame (g_103a3ad8/sub_10371880 handler) walking a linked list; likely locale/atexit table op. |
| `0x103689e0` | `crt_seh_wrapped_op_b` | 402 | Sibling of sub_10368840: SEH-guarded (fs:[0] frame) linked-list traversal helper with a distinct callback g_1038b15c. |
| `0x10368b80` | `sub_10368b80` | 28 | support routine (28 bytes) |
| `0x10368ba0` | `sub_10368ba0` | 28 | support routine (28 bytes) |
| `0x10368bc0` | `sub_10368bc0` | 16 | trivial accessor/forwarder |
| `0x10368bd0` | `sub_10368bd0` | 9 | trivial accessor/forwarder |
| `0x10368bd9` | `sub_10368bd9` | 48 | support routine (48 bytes) |
| `0x10368c10` | `sub_10368c10` | 30 | support routine (30 bytes) |
| `0x10368c30` | `sub_10368c30` | 6 | trivial accessor/forwarder |
| `0x10368c40` | `sub_10368c40` | 6 | trivial accessor/forwarder |
| `0x10368c50` | `sub_10368c50` | 6 | trivial accessor/forwarder |
| `0x10368c60` | `sub_10368c60` | 31 | support routine (31 bytes) |
| `0x10368c80` | `sub_10368c80` | 103 | support routine (103 bytes) |
| `0x10368cf0` | `sub_10368cf0` | 103 | support routine (103 bytes) |
| `0x10368d60` | `crt_avl_tree_rebalance` | 1216 | Generic AVL/red-black tree node rebalance/rotation routine over struct_0{parent, child[]}; pure pointer-shuffling data-structure code (STL-like tree). |
| `0x10369420` | `sub_10369420` | 178 | support routine (178 bytes) |
| `0x103694e0` | `crt_seh_once_init` | 300 | MSVC CRT SEH-guarded one-time init (fs:[0] frame, handler sub_10371880): sets a run-once flag on g_103a3b38 and initializes g_103a3b1c. |
| `0x10369610` | `crt_seh_list_walk` | 450 | MSVC CRT SEH-guarded (fs:[0] frame, handler sub_103718c1) traversal of a linked list with callbacks g_1038b154/g_1038b158; atexit/locale cleanup. |
| `0x103697e0` | `sub_103697e0` | 11 | trivial accessor/forwarder |
| `0x103697f0` | `sub_103697f0` | 25 | support routine (25 bytes) |
| `0x10369810` | `sub_10369810` | 6 | Boost library routine |
| `0x10369820` | `sub_10369820` | 25 | support routine (25 bytes) |
| `0x10369840` | `sub_10369840` | 6 | Boost library routine |
| `0x10369850` | `sub_10369850` | 13 | trivial accessor/forwarder |
| `0x10369860` | `sub_10369860` | 21 | support routine (21 bytes) |
| `0x10369880` | `sub_10369880` | 8 | trivial accessor/forwarder |
| `0x10369890` | `sub_10369890` | 15 | trivial accessor/forwarder |
| `0x103698a0` | `sub_103698a0` | 39 | support routine (39 bytes) |
| `0x103698d0` | `sub_103698d0` | 19 | support routine (19 bytes) |
| `0x103698f0` | `sub_103698f0` | 10 | trivial accessor/forwarder |
| `0x10369900` | `sub_10369900` | 17 | support routine (17 bytes) |
| `0x10369920` | `sub_10369920` | 1 | trivial accessor/forwarder |
| `0x10369930` | `sub_10369930` | 27 | support routine (27 bytes) |
| `0x10369950` | `sub_10369950` | 117 | support routine (117 bytes) |
| `0x103699d0` | `sub_103699d0` | 117 | support routine (117 bytes) |
| `0x10369a50` | `sub_10369a50` | 103 | support routine (103 bytes) |
| `0x10369ac0` | `sub_10369ac0` | 47 | support routine (47 bytes) |
| `0x10369af0` | `sub_10369af0` | 162 | support routine (162 bytes) |
| `0x10369ba0` | `sub_10369ba0` | 370 | support routine (370 bytes) |
| `0x10369d20` | `sub_10369d20` | 5 | trivial accessor/forwarder |
| `0x10369d26` | `sub_10369d26` | 6 | trivial accessor/forwarder |
| `0x10369d2c` | `sub_10369d2c` | 35 | support routine (35 bytes) |
| `0x10369d4f` | `sub_10369d4f` | 103 | support routine (103 bytes) |
| `0x10369db6` | `sub_10369db6` | 6 | trivial accessor/forwarder |
| `0x10369dbc` | `sub_10369dbc` | 6 | trivial accessor/forwarder |
| `0x10369dd0` | `sub_10369dd0` | 8 | trivial accessor/forwarder |
| `0x10369dd8` | `sub_10369dd8` | 27 | support routine (27 bytes) |
| `0x10369e00` | `sub_10369e00` | 11 | trivial accessor/forwarder |
| `0x10369e0b` | `sub_10369e0b` | 27 | support routine (27 bytes) |
| `0x10369e26` | `sub_10369e26` | 11 | trivial accessor/forwarder |
| `0x10369e31` | `sub_10369e31` | 27 | support routine (27 bytes) |
| `0x10369e4c` | `sub_10369e4c` | 8 | trivial accessor/forwarder |
| `0x10369e54` | `sub_10369e54` | 8 | trivial accessor/forwarder |
| `0x10369e5c` | `sub_10369e5c` | 27 | support routine (27 bytes) |
| `0x10369e80` | `sub_10369e80` | 37 | support routine (37 bytes) |
| `0x10369eb0` | `sub_10369eb0` | 27 | support routine (27 bytes) |
| `0x10369ed0` | `sub_10369ed0` | 8 | trivial accessor/forwarder |
| `0x10369ed8` | `sub_10369ed8` | 8 | trivial accessor/forwarder |
| `0x10369ee0` | `sub_10369ee0` | 27 | support routine (27 bytes) |
| `0x10369f00` | `sub_10369f00` | 8 | trivial accessor/forwarder |
| `0x10369f08` | `sub_10369f08` | 27 | support routine (27 bytes) |
| `0x10369f30` | `sub_10369f30` | 8 | trivial accessor/forwarder |
| `0x10369f38` | `sub_10369f38` | 27 | support routine (27 bytes) |
| `0x10369f60` | `sub_10369f60` | 8 | trivial accessor/forwarder |
| `0x10369f68` | `sub_10369f68` | 27 | support routine (27 bytes) |
| `0x10369f90` | `sub_10369f90` | 11 | trivial accessor/forwarder |
| `0x10369f9b` | `sub_10369f9b` | 27 | support routine (27 bytes) |
| `0x10369fc0` | `sub_10369fc0` | 8 | trivial accessor/forwarder |
| `0x10369fc8` | `sub_10369fc8` | 27 | support routine (27 bytes) |
| `0x10369ff0` | `sub_10369ff0` | 8 | trivial accessor/forwarder |
| `0x10369ff8` | `sub_10369ff8` | 27 | support routine (27 bytes) |
| `0x1036a020` | `sub_1036a020` | 11 | trivial accessor/forwarder |
| `0x1036a02b` | `sub_1036a02b` | 27 | support routine (27 bytes) |
| `0x1036a050` | `sub_1036a050` | 8 | trivial accessor/forwarder |
| `0x1036a058` | `sub_1036a058` | 27 | support routine (27 bytes) |
| `0x1036a080` | `sub_1036a080` | 8 | trivial accessor/forwarder |
| `0x1036a088` | `sub_1036a088` | 27 | support routine (27 bytes) |
| `0x1036a0b0` | `sub_1036a0b0` | 8 | trivial accessor/forwarder |
| `0x1036a0b8` | `sub_1036a0b8` | 27 | support routine (27 bytes) |
| `0x1036a0e0` | `sub_1036a0e0` | 8 | trivial accessor/forwarder |
| `0x1036a0e8` | `sub_1036a0e8` | 27 | support routine (27 bytes) |
| `0x1036a110` | `sub_1036a110` | 11 | trivial accessor/forwarder |
| `0x1036a11b` | `sub_1036a11b` | 27 | support routine (27 bytes) |
| `0x1036a140` | `sub_1036a140` | 8 | trivial accessor/forwarder |
| `0x1036a148` | `sub_1036a148` | 11 | trivial accessor/forwarder |
| `0x1036a153` | `sub_1036a153` | 27 | support routine (27 bytes) |
| `0x1036a170` | `sub_1036a170` | 8 | trivial accessor/forwarder |
| `0x1036a178` | `sub_1036a178` | 11 | trivial accessor/forwarder |
| `0x1036a183` | `sub_1036a183` | 27 | support routine (27 bytes) |
| `0x1036a1a0` | `sub_1036a1a0` | 11 | trivial accessor/forwarder |
| `0x1036a1ab` | `sub_1036a1ab` | 27 | support routine (27 bytes) |
| `0x1036a1d0` | `sub_1036a1d0` | 8 | trivial accessor/forwarder |
| `0x1036a1d8` | `sub_1036a1d8` | 27 | support routine (27 bytes) |
| `0x1036a200` | `sub_1036a200` | 28 | support routine (28 bytes) |
| `0x1036a21c` | `sub_1036a21c` | 27 | support routine (27 bytes) |
| `0x1036a240` | `sub_1036a240` | 8 | trivial accessor/forwarder |
| `0x1036a248` | `sub_1036a248` | 27 | support routine (27 bytes) |
| `0x1036a270` | `sub_1036a270` | 8 | trivial accessor/forwarder |
| `0x1036a278` | `sub_1036a278` | 11 | trivial accessor/forwarder |
| `0x1036a283` | `sub_1036a283` | 11 | trivial accessor/forwarder |
| `0x1036a28e` | `sub_1036a28e` | 30 | support routine (30 bytes) |
| `0x1036a2b0` | `sub_1036a2b0` | 8 | trivial accessor/forwarder |
| `0x1036a2b8` | `sub_1036a2b8` | 11 | trivial accessor/forwarder |
| `0x1036a2c3` | `sub_1036a2c3` | 27 | support routine (27 bytes) |
| `0x1036a2e0` | `sub_1036a2e0` | 8 | trivial accessor/forwarder |
| `0x1036a2e8` | `sub_1036a2e8` | 11 | trivial accessor/forwarder |
| `0x1036a2f3` | `sub_1036a2f3` | 27 | support routine (27 bytes) |
| `0x1036a310` | `sub_1036a310` | 8 | trivial accessor/forwarder |
| `0x1036a318` | `sub_1036a318` | 27 | support routine (27 bytes) |
| `0x1036a340` | `sub_1036a340` | 8 | trivial accessor/forwarder |
| `0x1036a348` | `sub_1036a348` | 11 | trivial accessor/forwarder |
| `0x1036a353` | `sub_1036a353` | 27 | support routine (27 bytes) |
| `0x1036a370` | `sub_1036a370` | 8 | trivial accessor/forwarder |
| `0x1036a378` | `sub_1036a378` | 27 | support routine (27 bytes) |
| `0x1036a3a0` | `sub_1036a3a0` | 8 | trivial accessor/forwarder |
| `0x1036a3a8` | `sub_1036a3a8` | 27 | support routine (27 bytes) |
| `0x1036a3d0` | `sub_1036a3d0` | 27 | support routine (27 bytes) |
| `0x1036a3f0` | `sub_1036a3f0` | 8 | trivial accessor/forwarder |
| `0x1036a3f8` | `sub_1036a3f8` | 27 | support routine (27 bytes) |
| `0x1036a420` | `sub_1036a420` | 25 | support routine (25 bytes) |
| `0x1036a439` | `sub_1036a439` | 27 | support routine (27 bytes) |
| `0x1036a460` | `sub_1036a460` | 8 | trivial accessor/forwarder |
| `0x1036a468` | `sub_1036a468` | 27 | support routine (27 bytes) |
| `0x1036a490` | `sub_1036a490` | 8 | trivial accessor/forwarder |
| `0x1036a498` | `sub_1036a498` | 27 | support routine (27 bytes) |
| `0x1036a4c0` | `sub_1036a4c0` | 11 | trivial accessor/forwarder |
| `0x1036a4cb` | `sub_1036a4cb` | 27 | support routine (27 bytes) |
| `0x1036a4f0` | `sub_1036a4f0` | 11 | trivial accessor/forwarder |
| `0x1036a4fb` | `sub_1036a4fb` | 11 | trivial accessor/forwarder |
| `0x1036a506` | `sub_1036a506` | 40 | support routine (40 bytes) |
| `0x1036a530` | `sub_1036a530` | 8 | trivial accessor/forwarder |
| `0x1036a538` | `sub_1036a538` | 11 | trivial accessor/forwarder |
| `0x1036a543` | `sub_1036a543` | 11 | trivial accessor/forwarder |
| `0x1036a54e` | `sub_1036a54e` | 11 | trivial accessor/forwarder |
| `0x1036a559` | `sub_1036a559` | 11 | trivial accessor/forwarder |
| `0x1036a564` | `sub_1036a564` | 8 | trivial accessor/forwarder |
| `0x1036a56c` | `sub_1036a56c` | 27 | support routine (27 bytes) |
| `0x1036a590` | `sub_1036a590` | 8 | trivial accessor/forwarder |
| `0x1036a598` | `sub_1036a598` | 11 | trivial accessor/forwarder |
| `0x1036a5a3` | `sub_1036a5a3` | 11 | trivial accessor/forwarder |
| `0x1036a5ae` | `sub_1036a5ae` | 11 | trivial accessor/forwarder |
| `0x1036a5b9` | `sub_1036a5b9` | 11 | trivial accessor/forwarder |
| `0x1036a5c4` | `sub_1036a5c4` | 27 | support routine (27 bytes) |
| `0x1036a5e0` | `sub_1036a5e0` | 8 | trivial accessor/forwarder |
| `0x1036a5e8` | `sub_1036a5e8` | 27 | support routine (27 bytes) |
| `0x1036a610` | `sub_1036a610` | 8 | trivial accessor/forwarder |
| `0x1036a618` | `sub_1036a618` | 27 | support routine (27 bytes) |
| `0x1036a640` | `sub_1036a640` | 8 | trivial accessor/forwarder |
| `0x1036a648` | `sub_1036a648` | 27 | support routine (27 bytes) |
| `0x1036a670` | `sub_1036a670` | 8 | trivial accessor/forwarder |
| `0x1036a678` | `sub_1036a678` | 27 | support routine (27 bytes) |
| `0x1036a6a0` | `sub_1036a6a0` | 8 | trivial accessor/forwarder |
| `0x1036a6a8` | `sub_1036a6a8` | 27 | support routine (27 bytes) |
| `0x1036a6d0` | `sub_1036a6d0` | 8 | trivial accessor/forwarder |
| `0x1036a6d8` | `sub_1036a6d8` | 27 | support routine (27 bytes) |
| `0x1036a700` | `sub_1036a700` | 8 | trivial accessor/forwarder |
| `0x1036a708` | `sub_1036a708` | 8 | trivial accessor/forwarder |
| `0x1036a710` | `sub_1036a710` | 27 | support routine (27 bytes) |
| `0x1036a730` | `sub_1036a730` | 8 | trivial accessor/forwarder |
| `0x1036a738` | `sub_1036a738` | 27 | support routine (27 bytes) |
| `0x1036a760` | `sub_1036a760` | 8 | trivial accessor/forwarder |
| `0x1036a768` | `sub_1036a768` | 27 | support routine (27 bytes) |
| `0x1036a790` | `sub_1036a790` | 8 | trivial accessor/forwarder |
| `0x1036a798` | `sub_1036a798` | 27 | support routine (27 bytes) |
| `0x1036a7c0` | `sub_1036a7c0` | 8 | trivial accessor/forwarder |
| `0x1036a7c8` | `sub_1036a7c8` | 27 | support routine (27 bytes) |
| `0x1036a7f0` | `sub_1036a7f0` | 8 | trivial accessor/forwarder |
| `0x1036a7f8` | `sub_1036a7f8` | 39 | support routine (39 bytes) |
| `0x1036a81f` | `sub_1036a81f` | 27 | support routine (27 bytes) |
| `0x1036a840` | `sub_1036a840` | 8 | trivial accessor/forwarder |
| `0x1036a848` | `sub_1036a848` | 39 | support routine (39 bytes) |
| `0x1036a86f` | `sub_1036a86f` | 27 | support routine (27 bytes) |
| `0x1036a890` | `sub_1036a890` | 11 | trivial accessor/forwarder |
| `0x1036a89b` | `sub_1036a89b` | 27 | support routine (27 bytes) |
| `0x1036a8c0` | `sub_1036a8c0` | 25 | support routine (25 bytes) |
| `0x1036a8d9` | `sub_1036a8d9` | 27 | support routine (27 bytes) |
| `0x1036a900` | `sub_1036a900` | 25 | support routine (25 bytes) |
| `0x1036a919` | `sub_1036a919` | 27 | support routine (27 bytes) |
| `0x1036a940` | `sub_1036a940` | 8 | trivial accessor/forwarder |
| `0x1036a948` | `sub_1036a948` | 27 | support routine (27 bytes) |
| `0x1036a970` | `sub_1036a970` | 8 | trivial accessor/forwarder |
| `0x1036a978` | `sub_1036a978` | 11 | trivial accessor/forwarder |
| `0x1036a983` | `sub_1036a983` | 27 | support routine (27 bytes) |
| `0x1036a9a0` | `sub_1036a9a0` | 11 | trivial accessor/forwarder |
| `0x1036a9ab` | `sub_1036a9ab` | 27 | support routine (27 bytes) |
| `0x1036a9d0` | `sub_1036a9d0` | 8 | trivial accessor/forwarder |
| `0x1036a9d8` | `sub_1036a9d8` | 11 | trivial accessor/forwarder |
| `0x1036a9e3` | `sub_1036a9e3` | 27 | support routine (27 bytes) |
| `0x1036aa00` | `sub_1036aa00` | 11 | trivial accessor/forwarder |
| `0x1036aa0b` | `sub_1036aa0b` | 27 | support routine (27 bytes) |
| `0x1036aa30` | `sub_1036aa30` | 11 | trivial accessor/forwarder |
| `0x1036aa3b` | `sub_1036aa3b` | 11 | trivial accessor/forwarder |
| `0x1036aa46` | `sub_1036aa46` | 40 | support routine (40 bytes) |
| `0x1036aa70` | `sub_1036aa70` | 8 | trivial accessor/forwarder |
| `0x1036aa78` | `sub_1036aa78` | 8 | trivial accessor/forwarder |
| `0x1036aa80` | `sub_1036aa80` | 8 | trivial accessor/forwarder |
| `0x1036aa88` | `sub_1036aa88` | 11 | trivial accessor/forwarder |
| `0x1036aa93` | `sub_1036aa93` | 11 | trivial accessor/forwarder |
| `0x1036aa9e` | `sub_1036aa9e` | 40 | support routine (40 bytes) |
| `0x1036aad0` | `sub_1036aad0` | 25 | support routine (25 bytes) |
| `0x1036aae9` | `sub_1036aae9` | 27 | support routine (27 bytes) |
| `0x1036ab10` | `sub_1036ab10` | 25 | support routine (25 bytes) |
| `0x1036ab29` | `sub_1036ab29` | 27 | support routine (27 bytes) |
| `0x1036ab50` | `sub_1036ab50` | 8 | trivial accessor/forwarder |
| `0x1036ab58` | `sub_1036ab58` | 27 | support routine (27 bytes) |
| `0x1036ab80` | `sub_1036ab80` | 11 | trivial accessor/forwarder |
| `0x1036ab8b` | `sub_1036ab8b` | 27 | support routine (27 bytes) |
| `0x1036abb0` | `sub_1036abb0` | 11 | trivial accessor/forwarder |
| `0x1036abbb` | `sub_1036abbb` | 11 | trivial accessor/forwarder |
| `0x1036abc6` | `sub_1036abc6` | 40 | support routine (40 bytes) |
| `0x1036abf0` | `sub_1036abf0` | 25 | support routine (25 bytes) |
| `0x1036ac09` | `sub_1036ac09` | 27 | support routine (27 bytes) |
| `0x1036ac30` | `sub_1036ac30` | 25 | support routine (25 bytes) |
| `0x1036ac49` | `sub_1036ac49` | 27 | support routine (27 bytes) |
| `0x1036ac70` | `sub_1036ac70` | 25 | support routine (25 bytes) |
| `0x1036ac89` | `sub_1036ac89` | 27 | support routine (27 bytes) |
| `0x1036acb0` | `sub_1036acb0` | 8 | trivial accessor/forwarder |
| `0x1036acb8` | `sub_1036acb8` | 27 | support routine (27 bytes) |
| `0x1036ace0` | `sub_1036ace0` | 27 | support routine (27 bytes) |
| `0x1036ad00` | `sub_1036ad00` | 8 | trivial accessor/forwarder |
| `0x1036ad08` | `sub_1036ad08` | 37 | support routine (37 bytes) |
| `0x1036ad30` | `sub_1036ad30` | 8 | trivial accessor/forwarder |
| `0x1036ad38` | `sub_1036ad38` | 37 | support routine (37 bytes) |
| `0x1036ad60` | `sub_1036ad60` | 8 | trivial accessor/forwarder |
| `0x1036ad68` | `sub_1036ad68` | 37 | support routine (37 bytes) |
| `0x1036ad90` | `sub_1036ad90` | 8 | trivial accessor/forwarder |
| `0x1036ad98` | `sub_1036ad98` | 37 | support routine (37 bytes) |
| `0x1036adc0` | `sub_1036adc0` | 8 | trivial accessor/forwarder |
| `0x1036adc8` | `sub_1036adc8` | 37 | support routine (37 bytes) |
| `0x1036adf0` | `sub_1036adf0` | 8 | trivial accessor/forwarder |
| `0x1036adf8` | `sub_1036adf8` | 37 | support routine (37 bytes) |
| `0x1036ae20` | `sub_1036ae20` | 8 | trivial accessor/forwarder |
| `0x1036ae28` | `sub_1036ae28` | 37 | support routine (37 bytes) |
| `0x1036ae50` | `sub_1036ae50` | 8 | trivial accessor/forwarder |
| `0x1036ae58` | `sub_1036ae58` | 37 | support routine (37 bytes) |
| `0x1036ae80` | `sub_1036ae80` | 8 | trivial accessor/forwarder |
| `0x1036ae88` | `sub_1036ae88` | 37 | support routine (37 bytes) |
| `0x1036aeb0` | `sub_1036aeb0` | 8 | trivial accessor/forwarder |
| `0x1036aeb8` | `sub_1036aeb8` | 37 | support routine (37 bytes) |
| `0x1036aee0` | `sub_1036aee0` | 8 | trivial accessor/forwarder |
| `0x1036aee8` | `sub_1036aee8` | 27 | support routine (27 bytes) |
| `0x1036af10` | `sub_1036af10` | 8 | trivial accessor/forwarder |
| `0x1036af18` | `sub_1036af18` | 8 | trivial accessor/forwarder |
| `0x1036af20` | `sub_1036af20` | 37 | support routine (37 bytes) |
| `0x1036af50` | `sub_1036af50` | 25 | support routine (25 bytes) |
| `0x1036af69` | `sub_1036af69` | 27 | support routine (27 bytes) |
| `0x1036af90` | `sub_1036af90` | 8 | trivial accessor/forwarder |
| `0x1036af98` | `sub_1036af98` | 8 | trivial accessor/forwarder |
| `0x1036afa0` | `sub_1036afa0` | 37 | support routine (37 bytes) |
| `0x1036afd0` | `sub_1036afd0` | 8 | trivial accessor/forwarder |
| `0x1036afd8` | `sub_1036afd8` | 37 | support routine (37 bytes) |
| `0x1036b000` | `sub_1036b000` | 8 | trivial accessor/forwarder |
| `0x1036b008` | `sub_1036b008` | 8 | trivial accessor/forwarder |
| `0x1036b010` | `sub_1036b010` | 8 | trivial accessor/forwarder |
| `0x1036b018` | `sub_1036b018` | 8 | trivial accessor/forwarder |
| `0x1036b020` | `sub_1036b020` | 11 | trivial accessor/forwarder |
| `0x1036b02b` | `sub_1036b02b` | 11 | trivial accessor/forwarder |
| `0x1036b036` | `sub_1036b036` | 30 | support routine (30 bytes) |
| `0x1036b054` | `sub_1036b054` | 8 | trivial accessor/forwarder |
| `0x1036b05c` | `sub_1036b05c` | 11 | trivial accessor/forwarder |
| `0x1036b067` | `sub_1036b067` | 11 | trivial accessor/forwarder |
| `0x1036b072` | `sub_1036b072` | 11 | trivial accessor/forwarder |
| `0x1036b07d` | `sub_1036b07d` | 30 | support routine (30 bytes) |
| `0x1036b09b` | `sub_1036b09b` | 8 | trivial accessor/forwarder |
| `0x1036b0a3` | `sub_1036b0a3` | 8 | trivial accessor/forwarder |
| `0x1036b0ab` | `sub_1036b0ab` | 8 | trivial accessor/forwarder |
| `0x1036b0b3` | `sub_1036b0b3` | 27 | support routine (27 bytes) |
| `0x1036b0ce` | `sub_1036b0ce` | 8 | trivial accessor/forwarder |
| `0x1036b0d6` | `sub_1036b0d6` | 8 | trivial accessor/forwarder |
| `0x1036b0de` | `sub_1036b0de` | 11 | trivial accessor/forwarder |
| `0x1036b0e9` | `sub_1036b0e9` | 11 | trivial accessor/forwarder |
| `0x1036b0f4` | `sub_1036b0f4` | 8 | trivial accessor/forwarder |
| `0x1036b0fc` | `sub_1036b0fc` | 40 | support routine (40 bytes) |
| `0x1036b130` | `sub_1036b130` | 8 | trivial accessor/forwarder |
| `0x1036b138` | `sub_1036b138` | 11 | trivial accessor/forwarder |
| `0x1036b143` | `sub_1036b143` | 11 | trivial accessor/forwarder |
| `0x1036b14e` | `sub_1036b14e` | 27 | support routine (27 bytes) |
| `0x1036b170` | `sub_1036b170` | 8 | trivial accessor/forwarder |
| `0x1036b178` | `sub_1036b178` | 11 | trivial accessor/forwarder |
| `0x1036b183` | `sub_1036b183` | 11 | trivial accessor/forwarder |
| `0x1036b18e` | `sub_1036b18e` | 27 | support routine (27 bytes) |
| `0x1036b1b0` | `sub_1036b1b0` | 11 | trivial accessor/forwarder |
| `0x1036b1bb` | `sub_1036b1bb` | 27 | support routine (27 bytes) |
| `0x1036b1e0` | `sub_1036b1e0` | 8 | trivial accessor/forwarder |
| `0x1036b1e8` | `sub_1036b1e8` | 27 | support routine (27 bytes) |
| `0x1036b210` | `sub_1036b210` | 8 | trivial accessor/forwarder |
| `0x1036b218` | `sub_1036b218` | 27 | support routine (27 bytes) |
| `0x1036b240` | `sub_1036b240` | 8 | trivial accessor/forwarder |
| `0x1036b248` | `sub_1036b248` | 27 | support routine (27 bytes) |
| `0x1036b270` | `sub_1036b270` | 8 | trivial accessor/forwarder |
| `0x1036b278` | `sub_1036b278` | 27 | support routine (27 bytes) |
| `0x1036b2a0` | `sub_1036b2a0` | 8 | trivial accessor/forwarder |
| `0x1036b2a8` | `sub_1036b2a8` | 27 | support routine (27 bytes) |
| `0x1036b2d0` | `sub_1036b2d0` | 8 | trivial accessor/forwarder |
| `0x1036b2d8` | `sub_1036b2d8` | 27 | support routine (27 bytes) |
| `0x1036b300` | `sub_1036b300` | 8 | trivial accessor/forwarder |
| `0x1036b308` | `sub_1036b308` | 27 | support routine (27 bytes) |
| `0x1036b330` | `sub_1036b330` | 11 | trivial accessor/forwarder |
| `0x1036b33b` | `sub_1036b33b` | 27 | support routine (27 bytes) |
| `0x1036b360` | `sub_1036b360` | 8 | trivial accessor/forwarder |
| `0x1036b368` | `sub_1036b368` | 25 | support routine (25 bytes) |
| `0x1036b381` | `sub_1036b381` | 27 | support routine (27 bytes) |
| `0x1036b3a0` | `sub_1036b3a0` | 8 | trivial accessor/forwarder |
| `0x1036b3a8` | `sub_1036b3a8` | 25 | support routine (25 bytes) |
| `0x1036b3c1` | `sub_1036b3c1` | 27 | support routine (27 bytes) |
| `0x1036b3e0` | `sub_1036b3e0` | 8 | trivial accessor/forwarder |
| `0x1036b3e8` | `sub_1036b3e8` | 25 | support routine (25 bytes) |
| `0x1036b401` | `sub_1036b401` | 27 | support routine (27 bytes) |
| `0x1036b420` | `sub_1036b420` | 25 | support routine (25 bytes) |
| `0x1036b439` | `sub_1036b439` | 27 | support routine (27 bytes) |
| `0x1036b460` | `sub_1036b460` | 25 | support routine (25 bytes) |
| `0x1036b479` | `sub_1036b479` | 27 | support routine (27 bytes) |
| `0x1036b4a0` | `sub_1036b4a0` | 25 | support routine (25 bytes) |
| `0x1036b4b9` | `sub_1036b4b9` | 37 | support routine (37 bytes) |
| `0x1036b4e0` | `sub_1036b4e0` | 25 | support routine (25 bytes) |
| `0x1036b4f9` | `sub_1036b4f9` | 37 | support routine (37 bytes) |
| `0x1036b520` | `sub_1036b520` | 3 | trivial accessor/forwarder |
| `0x1036b523` | `sub_1036b523` | 14 | trivial accessor/forwarder |
| `0x1036b531` | `sub_1036b531` | 27 | support routine (27 bytes) |
| `0x1036b550` | `sub_1036b550` | 8 | trivial accessor/forwarder |
| `0x1036b558` | `sub_1036b558` | 25 | support routine (25 bytes) |
| `0x1036b571` | `sub_1036b571` | 8 | trivial accessor/forwarder |
| `0x1036b579` | `sub_1036b579` | 37 | support routine (37 bytes) |
| `0x1036b5a0` | `sub_1036b5a0` | 8 | trivial accessor/forwarder |
| `0x1036b5a8` | `sub_1036b5a8` | 25 | support routine (25 bytes) |
| `0x1036b5c1` | `sub_1036b5c1` | 8 | trivial accessor/forwarder |
| `0x1036b5c9` | `sub_1036b5c9` | 37 | support routine (37 bytes) |
| `0x1036b5f0` | `sub_1036b5f0` | 8 | trivial accessor/forwarder |
| `0x1036b5f8` | `sub_1036b5f8` | 8 | trivial accessor/forwarder |
| `0x1036b600` | `sub_1036b600` | 37 | support routine (37 bytes) |
| `0x1036b630` | `sub_1036b630` | 8 | trivial accessor/forwarder |
| `0x1036b638` | `sub_1036b638` | 37 | support routine (37 bytes) |
| `0x1036b660` | `sub_1036b660` | 27 | support routine (27 bytes) |
| `0x1036b680` | `sub_1036b680` | 14 | trivial accessor/forwarder |
| `0x1036b68e` | `sub_1036b68e` | 25 | support routine (25 bytes) |
| `0x1036b6a7` | `sub_1036b6a7` | 27 | support routine (27 bytes) |
| `0x1036b6c2` | `sub_1036b6c2` | 8 | trivial accessor/forwarder |
| `0x1036b6ca` | `sub_1036b6ca` | 37 | support routine (37 bytes) |
| `0x1036b6ef` | `sub_1036b6ef` | 11 | trivial accessor/forwarder |
| `0x1036b6fa` | `sub_1036b6fa` | 11 | trivial accessor/forwarder |
| `0x1036b705` | `sub_1036b705` | 11 | trivial accessor/forwarder |
| `0x1036b710` | `sub_1036b710` | 11 | trivial accessor/forwarder |
| `0x1036b71b` | `sub_1036b71b` | 11 | trivial accessor/forwarder |
| `0x1036b726` | `sub_1036b726` | 11 | trivial accessor/forwarder |
| `0x1036b731` | `sub_1036b731` | 11 | trivial accessor/forwarder |
| `0x1036b73c` | `sub_1036b73c` | 40 | support routine (40 bytes) |
| `0x1036b770` | `sub_1036b770` | 8 | trivial accessor/forwarder |
| `0x1036b778` | `sub_1036b778` | 11 | trivial accessor/forwarder |
| `0x1036b783` | `sub_1036b783` | 11 | trivial accessor/forwarder |
| `0x1036b78e` | `sub_1036b78e` | 27 | support routine (27 bytes) |
| `0x1036b7b0` | `sub_1036b7b0` | 11 | trivial accessor/forwarder |
| `0x1036b7bb` | `sub_1036b7bb` | 14 | trivial accessor/forwarder |
| `0x1036b7c9` | `sub_1036b7c9` | 14 | trivial accessor/forwarder |
| `0x1036b7d7` | `sub_1036b7d7` | 27 | support routine (27 bytes) |
| `0x1036b800` | `sub_1036b800` | 11 | trivial accessor/forwarder |
| `0x1036b80b` | `sub_1036b80b` | 27 | support routine (27 bytes) |
| `0x1036b830` | `sub_1036b830` | 3 | trivial accessor/forwarder |
| `0x1036b833` | `sub_1036b833` | 14 | trivial accessor/forwarder |
| `0x1036b841` | `sub_1036b841` | 27 | support routine (27 bytes) |
| `0x1036b860` | `sub_1036b860` | 27 | support routine (27 bytes) |
| `0x1036b880` | `sub_1036b880` | 8 | trivial accessor/forwarder |
| `0x1036b888` | `sub_1036b888` | 8 | trivial accessor/forwarder |
| `0x1036b890` | `sub_1036b890` | 11 | trivial accessor/forwarder |
| `0x1036b89b` | `sub_1036b89b` | 40 | support routine (40 bytes) |
| `0x1036b8d0` | `sub_1036b8d0` | 8 | trivial accessor/forwarder |
| `0x1036b8d8` | `sub_1036b8d8` | 8 | trivial accessor/forwarder |
| `0x1036b8e0` | `sub_1036b8e0` | 8 | trivial accessor/forwarder |
| `0x1036b8e8` | `sub_1036b8e8` | 25 | support routine (25 bytes) |
| `0x1036b901` | `sub_1036b901` | 37 | support routine (37 bytes) |
| `0x1036b926` | `sub_1036b926` | 11 | trivial accessor/forwarder |
| `0x1036b931` | `sub_1036b931` | 8 | trivial accessor/forwarder |
| `0x1036b939` | `sub_1036b939` | 11 | trivial accessor/forwarder |
| `0x1036b944` | `sub_1036b944` | 40 | support routine (40 bytes) |
| `0x1036b96c` | `sub_1036b96c` | 11 | trivial accessor/forwarder |
| `0x1036b977` | `sub_1036b977` | 27 | support routine (27 bytes) |
| `0x1036b992` | `sub_1036b992` | 11 | trivial accessor/forwarder |
| `0x1036b99d` | `sub_1036b99d` | 11 | trivial accessor/forwarder |
| `0x1036b9a8` | `sub_1036b9a8` | 8 | trivial accessor/forwarder |
| `0x1036b9b0` | `sub_1036b9b0` | 11 | trivial accessor/forwarder |
| `0x1036b9bb` | `sub_1036b9bb` | 11 | trivial accessor/forwarder |
| `0x1036b9c6` | `sub_1036b9c6` | 11 | trivial accessor/forwarder |
| `0x1036b9d1` | `sub_1036b9d1` | 11 | trivial accessor/forwarder |
| `0x1036b9dc` | `sub_1036b9dc` | 40 | support routine (40 bytes) |
| `0x1036ba10` | `sub_1036ba10` | 25 | support routine (25 bytes) |
| `0x1036ba29` | `sub_1036ba29` | 27 | support routine (27 bytes) |
| `0x1036ba50` | `sub_1036ba50` | 8 | trivial accessor/forwarder |
| `0x1036ba58` | `sub_1036ba58` | 27 | support routine (27 bytes) |
| `0x1036ba80` | `sub_1036ba80` | 8 | trivial accessor/forwarder |
| `0x1036ba88` | `sub_1036ba88` | 27 | support routine (27 bytes) |
| `0x1036bab0` | `sub_1036bab0` | 8 | trivial accessor/forwarder |
| `0x1036bab8` | `sub_1036bab8` | 27 | support routine (27 bytes) |
| `0x1036bae0` | `sub_1036bae0` | 8 | trivial accessor/forwarder |
| `0x1036bae8` | `sub_1036bae8` | 27 | support routine (27 bytes) |
| `0x1036bb10` | `sub_1036bb10` | 3 | trivial accessor/forwarder |
| `0x1036bb13` | `sub_1036bb13` | 14 | trivial accessor/forwarder |
| `0x1036bb21` | `sub_1036bb21` | 27 | support routine (27 bytes) |
| `0x1036bb40` | `sub_1036bb40` | 8 | trivial accessor/forwarder |
| `0x1036bb48` | `sub_1036bb48` | 25 | support routine (25 bytes) |
| `0x1036bb61` | `sub_1036bb61` | 37 | support routine (37 bytes) |
| `0x1036bb90` | `sub_1036bb90` | 25 | support routine (25 bytes) |
| `0x1036bba9` | `sub_1036bba9` | 27 | support routine (27 bytes) |
| `0x1036bbd0` | `sub_1036bbd0` | 25 | support routine (25 bytes) |
| `0x1036bbe9` | `sub_1036bbe9` | 25 | support routine (25 bytes) |
| `0x1036bc02` | `sub_1036bc02` | 25 | support routine (25 bytes) |
| `0x1036bc1b` | `sub_1036bc1b` | 27 | support routine (27 bytes) |
| `0x1036bc40` | `sub_1036bc40` | 8 | trivial accessor/forwarder |
| `0x1036bc48` | `sub_1036bc48` | 11 | trivial accessor/forwarder |
| `0x1036bc53` | `sub_1036bc53` | 11 | trivial accessor/forwarder |
| `0x1036bc5e` | `sub_1036bc5e` | 8 | trivial accessor/forwarder |
| `0x1036bc66` | `sub_1036bc66` | 27 | support routine (27 bytes) |
| `0x1036bc81` | `sub_1036bc81` | 8 | trivial accessor/forwarder |
| `0x1036bc89` | `sub_1036bc89` | 11 | trivial accessor/forwarder |
| `0x1036bc94` | `sub_1036bc94` | 11 | trivial accessor/forwarder |
| `0x1036bc9f` | `sub_1036bc9f` | 8 | trivial accessor/forwarder |
| `0x1036bca7` | `sub_1036bca7` | 27 | support routine (27 bytes) |
| `0x1036bcc2` | `sub_1036bcc2` | 8 | trivial accessor/forwarder |
| `0x1036bcca` | `sub_1036bcca` | 11 | trivial accessor/forwarder |
| `0x1036bcd5` | `sub_1036bcd5` | 11 | trivial accessor/forwarder |
| `0x1036bce0` | `sub_1036bce0` | 27 | support routine (27 bytes) |
| `0x1036bcfb` | `sub_1036bcfb` | 8 | trivial accessor/forwarder |
| `0x1036bd03` | `sub_1036bd03` | 11 | trivial accessor/forwarder |
| `0x1036bd0e` | `sub_1036bd0e` | 11 | trivial accessor/forwarder |
| `0x1036bd19` | `sub_1036bd19` | 27 | support routine (27 bytes) |
| `0x1036bd34` | `sub_1036bd34` | 8 | trivial accessor/forwarder |
| `0x1036bd3c` | `sub_1036bd3c` | 11 | trivial accessor/forwarder |
| `0x1036bd47` | `sub_1036bd47` | 11 | trivial accessor/forwarder |
| `0x1036bd52` | `sub_1036bd52` | 8 | trivial accessor/forwarder |
| `0x1036bd5a` | `sub_1036bd5a` | 27 | support routine (27 bytes) |
| `0x1036bd75` | `sub_1036bd75` | 8 | trivial accessor/forwarder |
| `0x1036bd7d` | `sub_1036bd7d` | 25 | support routine (25 bytes) |
| `0x1036bd96` | `sub_1036bd96` | 8 | trivial accessor/forwarder |
| `0x1036bd9e` | `sub_1036bd9e` | 8 | trivial accessor/forwarder |
| `0x1036bda6` | `sub_1036bda6` | 30 | support routine (30 bytes) |
| `0x1036bdc4` | `sub_1036bdc4` | 8 | trivial accessor/forwarder |
| `0x1036bdcc` | `sub_1036bdcc` | 25 | support routine (25 bytes) |
| `0x1036bde5` | `sub_1036bde5` | 8 | trivial accessor/forwarder |
| `0x1036bded` | `sub_1036bded` | 8 | trivial accessor/forwarder |
| `0x1036bdf5` | `sub_1036bdf5` | 30 | support routine (30 bytes) |
| `0x1036be13` | `sub_1036be13` | 8 | trivial accessor/forwarder |
| `0x1036be1b` | `sub_1036be1b` | 25 | support routine (25 bytes) |
| `0x1036be34` | `sub_1036be34` | 27 | support routine (27 bytes) |
| `0x1036be4f` | `sub_1036be4f` | 8 | trivial accessor/forwarder |
| `0x1036be57` | `sub_1036be57` | 8 | trivial accessor/forwarder |
| `0x1036be5f` | `sub_1036be5f` | 27 | support routine (27 bytes) |
| `0x1036be7a` | `sub_1036be7a` | 8 | trivial accessor/forwarder |
| `0x1036be82` | `sub_1036be82` | 8 | trivial accessor/forwarder |
| `0x1036be8a` | `sub_1036be8a` | 27 | support routine (27 bytes) |
| `0x1036bea5` | `sub_1036bea5` | 25 | support routine (25 bytes) |
| `0x1036bebe` | `sub_1036bebe` | 8 | trivial accessor/forwarder |
| `0x1036bec6` | `sub_1036bec6` | 27 | support routine (27 bytes) |
| `0x1036bee1` | `sub_1036bee1` | 25 | support routine (25 bytes) |
| `0x1036befa` | `sub_1036befa` | 8 | trivial accessor/forwarder |
| `0x1036bf02` | `sub_1036bf02` | 27 | support routine (27 bytes) |
| `0x1036bf1d` | `sub_1036bf1d` | 25 | support routine (25 bytes) |
| `0x1036bf36` | `sub_1036bf36` | 8 | trivial accessor/forwarder |
| `0x1036bf3e` | `sub_1036bf3e` | 27 | support routine (27 bytes) |
| `0x1036bf59` | `sub_1036bf59` | 25 | support routine (25 bytes) |
| `0x1036bf72` | `sub_1036bf72` | 27 | support routine (27 bytes) |
| `0x1036bf8d` | `sub_1036bf8d` | 25 | support routine (25 bytes) |
| `0x1036bfa6` | `sub_1036bfa6` | 27 | support routine (27 bytes) |
| `0x1036bfc1` | `sub_1036bfc1` | 25 | support routine (25 bytes) |
| `0x1036bfda` | `sub_1036bfda` | 27 | support routine (27 bytes) |
| `0x1036bff5` | `sub_1036bff5` | 25 | support routine (25 bytes) |
| `0x1036c00e` | `sub_1036c00e` | 27 | support routine (27 bytes) |
| `0x1036c029` | `sub_1036c029` | 8 | trivial accessor/forwarder |
| `0x1036c031` | `sub_1036c031` | 25 | support routine (25 bytes) |
| `0x1036c04a` | `sub_1036c04a` | 27 | support routine (27 bytes) |
| `0x1036c065` | `sub_1036c065` | 8 | trivial accessor/forwarder |
| `0x1036c06d` | `sub_1036c06d` | 25 | support routine (25 bytes) |
| `0x1036c086` | `sub_1036c086` | 27 | support routine (27 bytes) |
| `0x1036c0a1` | `sub_1036c0a1` | 11 | trivial accessor/forwarder |
| `0x1036c0ac` | `sub_1036c0ac` | 14 | trivial accessor/forwarder |
| `0x1036c0ba` | `sub_1036c0ba` | 14 | trivial accessor/forwarder |
| `0x1036c0c8` | `sub_1036c0c8` | 27 | support routine (27 bytes) |
| `0x1036c0e3` | `sub_1036c0e3` | 11 | trivial accessor/forwarder |
| `0x1036c0ee` | `sub_1036c0ee` | 14 | trivial accessor/forwarder |
| `0x1036c0fc` | `sub_1036c0fc` | 14 | trivial accessor/forwarder |
| `0x1036c10a` | `sub_1036c10a` | 27 | support routine (27 bytes) |
| `0x1036c125` | `sub_1036c125` | 11 | trivial accessor/forwarder |
| `0x1036c130` | `sub_1036c130` | 14 | trivial accessor/forwarder |
| `0x1036c13e` | `sub_1036c13e` | 14 | trivial accessor/forwarder |
| `0x1036c14c` | `sub_1036c14c` | 27 | support routine (27 bytes) |
| `0x1036c167` | `sub_1036c167` | 11 | trivial accessor/forwarder |
| `0x1036c172` | `sub_1036c172` | 14 | trivial accessor/forwarder |
| `0x1036c180` | `sub_1036c180` | 14 | trivial accessor/forwarder |
| `0x1036c18e` | `sub_1036c18e` | 27 | support routine (27 bytes) |
| `0x1036c1a9` | `sub_1036c1a9` | 8 | trivial accessor/forwarder |
| `0x1036c1b1` | `sub_1036c1b1` | 25 | support routine (25 bytes) |
| `0x1036c1ca` | `sub_1036c1ca` | 8 | trivial accessor/forwarder |
| `0x1036c1d2` | `sub_1036c1d2` | 27 | support routine (27 bytes) |
| `0x1036c1ed` | `sub_1036c1ed` | 8 | trivial accessor/forwarder |
| `0x1036c1f5` | `sub_1036c1f5` | 25 | support routine (25 bytes) |
| `0x1036c20e` | `sub_1036c20e` | 8 | trivial accessor/forwarder |
| `0x1036c216` | `sub_1036c216` | 27 | support routine (27 bytes) |
| `0x1036c231` | `sub_1036c231` | 8 | trivial accessor/forwarder |
| `0x1036c239` | `sub_1036c239` | 11 | trivial accessor/forwarder |
| `0x1036c244` | `sub_1036c244` | 11 | trivial accessor/forwarder |
| `0x1036c24f` | `sub_1036c24f` | 11 | trivial accessor/forwarder |
| `0x1036c25a` | `sub_1036c25a` | 30 | support routine (30 bytes) |
| `0x1036c278` | `sub_1036c278` | 8 | trivial accessor/forwarder |
| `0x1036c280` | `sub_1036c280` | 8 | trivial accessor/forwarder |
| `0x1036c288` | `sub_1036c288` | 11 | trivial accessor/forwarder |
| `0x1036c293` | `sub_1036c293` | 8 | trivial accessor/forwarder |
| `0x1036c29b` | `sub_1036c29b` | 30 | support routine (30 bytes) |
| `0x1036c2b9` | `sub_1036c2b9` | 8 | trivial accessor/forwarder |
| `0x1036c2c1` | `sub_1036c2c1` | 31 | support routine (31 bytes) |
| `0x1036c2e0` | `sub_1036c2e0` | 11 | trivial accessor/forwarder |
| `0x1036c2eb` | `sub_1036c2eb` | 11 | trivial accessor/forwarder |
| `0x1036c2f6` | `sub_1036c2f6` | 11 | trivial accessor/forwarder |
| `0x1036c301` | `sub_1036c301` | 11 | trivial accessor/forwarder |
| `0x1036c30c` | `sub_1036c30c` | 8 | trivial accessor/forwarder |
| `0x1036c314` | `sub_1036c314` | 30 | support routine (30 bytes) |
| `0x1036c332` | `sub_1036c332` | 8 | trivial accessor/forwarder |
| `0x1036c33a` | `sub_1036c33a` | 8 | trivial accessor/forwarder |
| `0x1036c342` | `sub_1036c342` | 25 | support routine (25 bytes) |
| `0x1036c35b` | `sub_1036c35b` | 37 | support routine (37 bytes) |
| `0x1036c380` | `sub_1036c380` | 8 | trivial accessor/forwarder |
| `0x1036c388` | `sub_1036c388` | 8 | trivial accessor/forwarder |
| `0x1036c390` | `sub_1036c390` | 25 | support routine (25 bytes) |
| `0x1036c3a9` | `sub_1036c3a9` | 27 | support routine (27 bytes) |
| `0x1036c3c4` | `sub_1036c3c4` | 14 | trivial accessor/forwarder |
| `0x1036c3d2` | `sub_1036c3d2` | 8 | trivial accessor/forwarder |
| `0x1036c3da` | `sub_1036c3da` | 8 | trivial accessor/forwarder |
| `0x1036c3e2` | `sub_1036c3e2` | 8 | trivial accessor/forwarder |
| `0x1036c3ea` | `sub_1036c3ea` | 31 | support routine (31 bytes) |
| `0x1036c409` | `sub_1036c409` | 11 | trivial accessor/forwarder |
| `0x1036c414` | `sub_1036c414` | 11 | trivial accessor/forwarder |
| `0x1036c41f` | `sub_1036c41f` | 11 | trivial accessor/forwarder |
| `0x1036c42a` | `sub_1036c42a` | 11 | trivial accessor/forwarder |
| `0x1036c435` | `sub_1036c435` | 30 | support routine (30 bytes) |
| `0x1036c453` | `sub_1036c453` | 8 | trivial accessor/forwarder |
| `0x1036c45b` | `sub_1036c45b` | 8 | trivial accessor/forwarder |
| `0x1036c463` | `sub_1036c463` | 25 | support routine (25 bytes) |
| `0x1036c47c` | `sub_1036c47c` | 27 | support routine (27 bytes) |
| `0x1036c497` | `sub_1036c497` | 14 | trivial accessor/forwarder |
| `0x1036c4a5` | `sub_1036c4a5` | 8 | trivial accessor/forwarder |
| `0x1036c4ad` | `sub_1036c4ad` | 8 | trivial accessor/forwarder |
| `0x1036c4b5` | `sub_1036c4b5` | 8 | trivial accessor/forwarder |
| `0x1036c4bd` | `sub_1036c4bd` | 31 | support routine (31 bytes) |
| `0x1036c4dc` | `sub_1036c4dc` | 11 | trivial accessor/forwarder |
| `0x1036c4e7` | `sub_1036c4e7` | 11 | trivial accessor/forwarder |
| `0x1036c4f2` | `sub_1036c4f2` | 30 | support routine (30 bytes) |
| `0x1036c510` | `sub_1036c510` | 8 | trivial accessor/forwarder |
| `0x1036c518` | `sub_1036c518` | 25 | support routine (25 bytes) |
| `0x1036c531` | `sub_1036c531` | 27 | support routine (27 bytes) |
| `0x1036c54c` | `sub_1036c54c` | 14 | trivial accessor/forwarder |
| `0x1036c55a` | `sub_1036c55a` | 8 | trivial accessor/forwarder |
| `0x1036c562` | `sub_1036c562` | 8 | trivial accessor/forwarder |
| `0x1036c56a` | `sub_1036c56a` | 31 | support routine (31 bytes) |
| `0x1036c589` | `sub_1036c589` | 11 | trivial accessor/forwarder |
| `0x1036c594` | `sub_1036c594` | 11 | trivial accessor/forwarder |
| `0x1036c59f` | `sub_1036c59f` | 30 | support routine (30 bytes) |
| `0x1036c5bd` | `sub_1036c5bd` | 8 | trivial accessor/forwarder |
| `0x1036c5c5` | `sub_1036c5c5` | 25 | support routine (25 bytes) |
| `0x1036c5de` | `sub_1036c5de` | 27 | support routine (27 bytes) |
| `0x1036c5f9` | `sub_1036c5f9` | 14 | trivial accessor/forwarder |
| `0x1036c607` | `sub_1036c607` | 8 | trivial accessor/forwarder |
| `0x1036c60f` | `sub_1036c60f` | 8 | trivial accessor/forwarder |
| `0x1036c617` | `sub_1036c617` | 31 | support routine (31 bytes) |
| `0x1036c636` | `sub_1036c636` | 11 | trivial accessor/forwarder |
| `0x1036c641` | `sub_1036c641` | 11 | trivial accessor/forwarder |
| `0x1036c64c` | `sub_1036c64c` | 30 | support routine (30 bytes) |
| `0x1036c66a` | `sub_1036c66a` | 8 | trivial accessor/forwarder |
| `0x1036c672` | `sub_1036c672` | 25 | support routine (25 bytes) |
| `0x1036c68b` | `sub_1036c68b` | 27 | support routine (27 bytes) |
| `0x1036c6a6` | `sub_1036c6a6` | 14 | trivial accessor/forwarder |
| `0x1036c6b4` | `sub_1036c6b4` | 8 | trivial accessor/forwarder |
| `0x1036c6bc` | `sub_1036c6bc` | 8 | trivial accessor/forwarder |
| `0x1036c6c4` | `sub_1036c6c4` | 31 | support routine (31 bytes) |
| `0x1036c6e3` | `sub_1036c6e3` | 11 | trivial accessor/forwarder |
| `0x1036c6ee` | `sub_1036c6ee` | 11 | trivial accessor/forwarder |
| `0x1036c6f9` | `sub_1036c6f9` | 30 | support routine (30 bytes) |
| `0x1036c717` | `sub_1036c717` | 14 | trivial accessor/forwarder |
| `0x1036c725` | `sub_1036c725` | 8 | trivial accessor/forwarder |
| `0x1036c72d` | `sub_1036c72d` | 27 | support routine (27 bytes) |
| `0x1036c748` | `sub_1036c748` | 8 | trivial accessor/forwarder |
| `0x1036c750` | `sub_1036c750` | 11 | trivial accessor/forwarder |
| `0x1036c75b` | `sub_1036c75b` | 8 | trivial accessor/forwarder |
| `0x1036c763` | `sub_1036c763` | 31 | support routine (31 bytes) |
| `0x1036c782` | `sub_1036c782` | 40 | support routine (40 bytes) |
| `0x1036c7aa` | `sub_1036c7aa` | 14 | trivial accessor/forwarder |
| `0x1036c7b8` | `sub_1036c7b8` | 8 | trivial accessor/forwarder |
| `0x1036c7c0` | `sub_1036c7c0` | 8 | trivial accessor/forwarder |
| `0x1036c7c8` | `sub_1036c7c8` | 8 | trivial accessor/forwarder |
| `0x1036c7d0` | `sub_1036c7d0` | 8 | trivial accessor/forwarder |
| `0x1036c7d8` | `sub_1036c7d8` | 31 | support routine (31 bytes) |
| `0x1036c7f7` | `sub_1036c7f7` | 11 | trivial accessor/forwarder |
| `0x1036c802` | `sub_1036c802` | 11 | trivial accessor/forwarder |
| `0x1036c80d` | `sub_1036c80d` | 40 | support routine (40 bytes) |
| `0x1036c835` | `sub_1036c835` | 14 | trivial accessor/forwarder |
| `0x1036c843` | `sub_1036c843` | 8 | trivial accessor/forwarder |
| `0x1036c84b` | `sub_1036c84b` | 11 | trivial accessor/forwarder |
| `0x1036c856` | `sub_1036c856` | 11 | trivial accessor/forwarder |
| `0x1036c861` | `sub_1036c861` | 30 | support routine (30 bytes) |
| `0x1036c87f` | `sub_1036c87f` | 14 | trivial accessor/forwarder |
| `0x1036c88d` | `sub_1036c88d` | 8 | trivial accessor/forwarder |
| `0x1036c895` | `sub_1036c895` | 27 | support routine (27 bytes) |
| `0x1036c8b0` | `sub_1036c8b0` | 14 | trivial accessor/forwarder |
| `0x1036c8be` | `sub_1036c8be` | 8 | trivial accessor/forwarder |
| `0x1036c8c6` | `sub_1036c8c6` | 27 | support routine (27 bytes) |
| `0x1036c8e1` | `sub_1036c8e1` | 8 | trivial accessor/forwarder |
| `0x1036c8e9` | `sub_1036c8e9` | 25 | support routine (25 bytes) |
| `0x1036c902` | `sub_1036c902` | 27 | support routine (27 bytes) |
| `0x1036c91d` | `sub_1036c91d` | 14 | trivial accessor/forwarder |
| `0x1036c92b` | `sub_1036c92b` | 8 | trivial accessor/forwarder |
| `0x1036c933` | `sub_1036c933` | 8 | trivial accessor/forwarder |
| `0x1036c93b` | `sub_1036c93b` | 31 | support routine (31 bytes) |
| `0x1036c95a` | `sub_1036c95a` | 8 | trivial accessor/forwarder |
| `0x1036c962` | `sub_1036c962` | 8 | trivial accessor/forwarder |
| `0x1036c96a` | `sub_1036c96a` | 11 | trivial accessor/forwarder |
| `0x1036c975` | `sub_1036c975` | 40 | support routine (40 bytes) |
| `0x1036c99d` | `sub_1036c99d` | 8 | trivial accessor/forwarder |
| `0x1036c9a5` | `sub_1036c9a5` | 27 | support routine (27 bytes) |
| `0x1036c9c0` | `sub_1036c9c0` | 8 | trivial accessor/forwarder |
| `0x1036c9c8` | `sub_1036c9c8` | 25 | support routine (25 bytes) |
| `0x1036c9e1` | `sub_1036c9e1` | 27 | support routine (27 bytes) |
| `0x1036c9fc` | `sub_1036c9fc` | 14 | trivial accessor/forwarder |
| `0x1036ca0a` | `sub_1036ca0a` | 8 | trivial accessor/forwarder |
| `0x1036ca12` | `sub_1036ca12` | 14 | trivial accessor/forwarder |
| `0x1036ca20` | `sub_1036ca20` | 8 | trivial accessor/forwarder |
| `0x1036ca28` | `sub_1036ca28` | 8 | trivial accessor/forwarder |
| `0x1036ca30` | `sub_1036ca30` | 31 | support routine (31 bytes) |
| `0x1036ca4f` | `sub_1036ca4f` | 11 | trivial accessor/forwarder |
| `0x1036ca5a` | `sub_1036ca5a` | 11 | trivial accessor/forwarder |
| `0x1036ca65` | `sub_1036ca65` | 30 | support routine (30 bytes) |
| `0x1036ca83` | `sub_1036ca83` | 14 | trivial accessor/forwarder |
| `0x1036ca91` | `sub_1036ca91` | 8 | trivial accessor/forwarder |
| `0x1036ca99` | `sub_1036ca99` | 27 | support routine (27 bytes) |
| `0x1036cab4` | `sub_1036cab4` | 14 | trivial accessor/forwarder |
| `0x1036cac2` | `sub_1036cac2` | 8 | trivial accessor/forwarder |
| `0x1036caca` | `sub_1036caca` | 27 | support routine (27 bytes) |
| `0x1036cae5` | `sub_1036cae5` | 8 | trivial accessor/forwarder |
| `0x1036caed` | `sub_1036caed` | 25 | support routine (25 bytes) |
| `0x1036cb06` | `sub_1036cb06` | 27 | support routine (27 bytes) |
| `0x1036cb21` | `sub_1036cb21` | 8 | trivial accessor/forwarder |
| `0x1036cb29` | `sub_1036cb29` | 31 | support routine (31 bytes) |
| `0x1036cb48` | `sub_1036cb48` | 11 | trivial accessor/forwarder |
| `0x1036cb53` | `sub_1036cb53` | 11 | trivial accessor/forwarder |
| `0x1036cb5e` | `sub_1036cb5e` | 30 | support routine (30 bytes) |
| `0x1036cb7c` | `sub_1036cb7c` | 14 | trivial accessor/forwarder |
| `0x1036cb8a` | `sub_1036cb8a` | 8 | trivial accessor/forwarder |
| `0x1036cb92` | `sub_1036cb92` | 27 | support routine (27 bytes) |
| `0x1036cbad` | `sub_1036cbad` | 14 | trivial accessor/forwarder |
| `0x1036cbbb` | `sub_1036cbbb` | 8 | trivial accessor/forwarder |
| `0x1036cbc3` | `sub_1036cbc3` | 27 | support routine (27 bytes) |
| `0x1036cbde` | `sub_1036cbde` | 8 | trivial accessor/forwarder |
| `0x1036cbe6` | `sub_1036cbe6` | 25 | support routine (25 bytes) |
| `0x1036cbff` | `sub_1036cbff` | 27 | support routine (27 bytes) |
| `0x1036cc1a` | `sub_1036cc1a` | 8 | trivial accessor/forwarder |
| `0x1036cc22` | `sub_1036cc22` | 31 | support routine (31 bytes) |
| `0x1036cc41` | `sub_1036cc41` | 11 | trivial accessor/forwarder |
| `0x1036cc4c` | `sub_1036cc4c` | 11 | trivial accessor/forwarder |
| `0x1036cc57` | `sub_1036cc57` | 30 | support routine (30 bytes) |
| `0x1036cc75` | `sub_1036cc75` | 14 | trivial accessor/forwarder |
| `0x1036cc83` | `sub_1036cc83` | 11 | trivial accessor/forwarder |
| `0x1036cc8e` | `sub_1036cc8e` | 11 | trivial accessor/forwarder |
| `0x1036cc99` | `sub_1036cc99` | 8 | trivial accessor/forwarder |
| `0x1036cca1` | `sub_1036cca1` | 40 | support routine (40 bytes) |
| `0x1036ccc9` | `sub_1036ccc9` | 14 | trivial accessor/forwarder |
| `0x1036ccd7` | `sub_1036ccd7` | 11 | trivial accessor/forwarder |
| `0x1036cce2` | `sub_1036cce2` | 11 | trivial accessor/forwarder |
| `0x1036cced` | `sub_1036cced` | 8 | trivial accessor/forwarder |
| `0x1036ccf5` | `sub_1036ccf5` | 40 | support routine (40 bytes) |
| `0x1036cd1d` | `sub_1036cd1d` | 14 | trivial accessor/forwarder |
| `0x1036cd2b` | `sub_1036cd2b` | 8 | trivial accessor/forwarder |
| `0x1036cd33` | `sub_1036cd33` | 27 | support routine (27 bytes) |
| `0x1036cd4e` | `sub_1036cd4e` | 14 | trivial accessor/forwarder |
| `0x1036cd5c` | `sub_1036cd5c` | 8 | trivial accessor/forwarder |
| `0x1036cd64` | `sub_1036cd64` | 27 | support routine (27 bytes) |
| `0x1036cd7f` | `sub_1036cd7f` | 14 | trivial accessor/forwarder |
| `0x1036cd8d` | `sub_1036cd8d` | 8 | trivial accessor/forwarder |
| `0x1036cd95` | `sub_1036cd95` | 27 | support routine (27 bytes) |
| `0x1036cdb0` | `sub_1036cdb0` | 14 | trivial accessor/forwarder |
| `0x1036cdbe` | `sub_1036cdbe` | 8 | trivial accessor/forwarder |
| `0x1036cdc6` | `sub_1036cdc6` | 27 | support routine (27 bytes) |
| `0x1036cde1` | `sub_1036cde1` | 14 | trivial accessor/forwarder |
| `0x1036cdef` | `sub_1036cdef` | 8 | trivial accessor/forwarder |
| `0x1036cdf7` | `sub_1036cdf7` | 27 | support routine (27 bytes) |
| `0x1036ce12` | `sub_1036ce12` | 25 | support routine (25 bytes) |
| `0x1036ce2b` | `sub_1036ce2b` | 27 | support routine (27 bytes) |
| `0x1036ce46` | `sub_1036ce46` | 14 | trivial accessor/forwarder |
| `0x1036ce54` | `sub_1036ce54` | 25 | support routine (25 bytes) |
| `0x1036ce6d` | `sub_1036ce6d` | 27 | support routine (27 bytes) |
| `0x1036ce88` | `sub_1036ce88` | 14 | trivial accessor/forwarder |
| `0x1036ce96` | `sub_1036ce96` | 8 | trivial accessor/forwarder |
| `0x1036ce9e` | `sub_1036ce9e` | 31 | support routine (31 bytes) |
| `0x1036cebd` | `sub_1036cebd` | 11 | trivial accessor/forwarder |
| `0x1036cec8` | `sub_1036cec8` | 11 | trivial accessor/forwarder |
| `0x1036ced3` | `sub_1036ced3` | 30 | support routine (30 bytes) |
| `0x1036cef1` | `sub_1036cef1` | 14 | trivial accessor/forwarder |
| `0x1036ceff` | `sub_1036ceff` | 8 | trivial accessor/forwarder |
| `0x1036cf07` | `sub_1036cf07` | 31 | support routine (31 bytes) |
| `0x1036cf26` | `sub_1036cf26` | 11 | trivial accessor/forwarder |
| `0x1036cf31` | `sub_1036cf31` | 11 | trivial accessor/forwarder |
| `0x1036cf3c` | `sub_1036cf3c` | 30 | support routine (30 bytes) |
| `0x1036cf5a` | `sub_1036cf5a` | 8 | trivial accessor/forwarder |
| `0x1036cf62` | `sub_1036cf62` | 25 | support routine (25 bytes) |
| `0x1036cf7b` | `sub_1036cf7b` | 8 | trivial accessor/forwarder |
| `0x1036cf83` | `sub_1036cf83` | 27 | support routine (27 bytes) |
| `0x1036cf9e` | `sub_1036cf9e` | 14 | trivial accessor/forwarder |
| `0x1036cfac` | `sub_1036cfac` | 8 | trivial accessor/forwarder |
| `0x1036cfb4` | `sub_1036cfb4` | 8 | trivial accessor/forwarder |
| `0x1036cfbc` | `sub_1036cfbc` | 31 | support routine (31 bytes) |
| `0x1036cfdb` | `sub_1036cfdb` | 8 | trivial accessor/forwarder |
| `0x1036cfe3` | `sub_1036cfe3` | 11 | trivial accessor/forwarder |
| `0x1036cfee` | `sub_1036cfee` | 11 | trivial accessor/forwarder |
| `0x1036cff9` | `sub_1036cff9` | 30 | support routine (30 bytes) |
| `0x1036d017` | `sub_1036d017` | 14 | trivial accessor/forwarder |
| `0x1036d025` | `sub_1036d025` | 11 | trivial accessor/forwarder |
| `0x1036d030` | `sub_1036d030` | 8 | trivial accessor/forwarder |
| `0x1036d038` | `sub_1036d038` | 8 | trivial accessor/forwarder |
| `0x1036d040` | `sub_1036d040` | 11 | trivial accessor/forwarder |
| `0x1036d04b` | `sub_1036d04b` | 11 | trivial accessor/forwarder |
| `0x1036d056` | `sub_1036d056` | 11 | trivial accessor/forwarder |
| `0x1036d061` | `sub_1036d061` | 40 | support routine (40 bytes) |
| `0x1036d089` | `sub_1036d089` | 25 | support routine (25 bytes) |
| `0x1036d0a2` | `sub_1036d0a2` | 27 | support routine (27 bytes) |
| `0x1036d0bd` | `sub_1036d0bd` | 14 | trivial accessor/forwarder |
| `0x1036d0cb` | `sub_1036d0cb` | 11 | trivial accessor/forwarder |
| `0x1036d0d6` | `sub_1036d0d6` | 31 | support routine (31 bytes) |
| `0x1036d0f5` | `sub_1036d0f5` | 30 | support routine (30 bytes) |
| `0x1036d113` | `sub_1036d113` | 25 | support routine (25 bytes) |
| `0x1036d12c` | `sub_1036d12c` | 27 | support routine (27 bytes) |
| `0x1036d147` | `sub_1036d147` | 14 | trivial accessor/forwarder |
| `0x1036d155` | `sub_1036d155` | 8 | trivial accessor/forwarder |
| `0x1036d15d` | `sub_1036d15d` | 31 | support routine (31 bytes) |
| `0x1036d17c` | `sub_1036d17c` | 11 | trivial accessor/forwarder |
| `0x1036d187` | `sub_1036d187` | 11 | trivial accessor/forwarder |
| `0x1036d192` | `sub_1036d192` | 30 | support routine (30 bytes) |
| `0x1036d1b0` | `sub_1036d1b0` | 8 | trivial accessor/forwarder |
| `0x1036d1b8` | `sub_1036d1b8` | 8 | trivial accessor/forwarder |
| `0x1036d1c0` | `sub_1036d1c0` | 8 | trivial accessor/forwarder |
| `0x1036d1c8` | `sub_1036d1c8` | 25 | support routine (25 bytes) |
| `0x1036d1e1` | `sub_1036d1e1` | 37 | support routine (37 bytes) |
| `0x1036d206` | `sub_1036d206` | 8 | trivial accessor/forwarder |
| `0x1036d20e` | `sub_1036d20e` | 11 | trivial accessor/forwarder |
| `0x1036d219` | `sub_1036d219` | 11 | trivial accessor/forwarder |
| `0x1036d224` | `sub_1036d224` | 11 | trivial accessor/forwarder |
| `0x1036d22f` | `sub_1036d22f` | 31 | support routine (31 bytes) |
| `0x1036d24e` | `sub_1036d24e` | 40 | support routine (40 bytes) |
| `0x1036d276` | `sub_1036d276` | 8 | trivial accessor/forwarder |
| `0x1036d27e` | `sub_1036d27e` | 37 | support routine (37 bytes) |
| `0x1036d2a3` | `sub_1036d2a3` | 8 | trivial accessor/forwarder |
| `0x1036d2ab` | `sub_1036d2ab` | 11 | trivial accessor/forwarder |
| `0x1036d2b6` | `sub_1036d2b6` | 11 | trivial accessor/forwarder |
| `0x1036d2c1` | `sub_1036d2c1` | 11 | trivial accessor/forwarder |
| `0x1036d2cc` | `sub_1036d2cc` | 31 | support routine (31 bytes) |
| `0x1036d2eb` | `sub_1036d2eb` | 40 | support routine (40 bytes) |
| `0x1036d313` | `sub_1036d313` | 8 | trivial accessor/forwarder |
| `0x1036d31b` | `sub_1036d31b` | 37 | support routine (37 bytes) |
| `0x1036d340` | `sub_1036d340` | 8 | trivial accessor/forwarder |
| `0x1036d348` | `sub_1036d348` | 11 | trivial accessor/forwarder |
| `0x1036d353` | `sub_1036d353` | 27 | support routine (27 bytes) |
| `0x1036d370` | `sub_1036d370` | 8 | trivial accessor/forwarder |
| `0x1036d378` | `sub_1036d378` | 11 | trivial accessor/forwarder |
| `0x1036d383` | `sub_1036d383` | 27 | support routine (27 bytes) |
| `0x1036d3a0` | `sub_1036d3a0` | 8 | trivial accessor/forwarder |
| `0x1036d3a8` | `sub_1036d3a8` | 11 | trivial accessor/forwarder |
| `0x1036d3b3` | `sub_1036d3b3` | 27 | support routine (27 bytes) |
| `0x1036d3d0` | `sub_1036d3d0` | 8 | trivial accessor/forwarder |
| `0x1036d3d8` | `sub_1036d3d8` | 8 | trivial accessor/forwarder |
| `0x1036d3e0` | `sub_1036d3e0` | 11 | trivial accessor/forwarder |
| `0x1036d3eb` | `sub_1036d3eb` | 11 | trivial accessor/forwarder |
| `0x1036d3f6` | `sub_1036d3f6` | 27 | support routine (27 bytes) |
| `0x1036d420` | `sub_1036d420` | 8 | trivial accessor/forwarder |
| `0x1036d428` | `sub_1036d428` | 8 | trivial accessor/forwarder |
| `0x1036d430` | `sub_1036d430` | 11 | trivial accessor/forwarder |
| `0x1036d43b` | `sub_1036d43b` | 11 | trivial accessor/forwarder |
| `0x1036d446` | `sub_1036d446` | 27 | support routine (27 bytes) |
| `0x1036d470` | `sub_1036d470` | 25 | support routine (25 bytes) |
| `0x1036d489` | `sub_1036d489` | 27 | support routine (27 bytes) |
| `0x1036d4b0` | `sub_1036d4b0` | 25 | support routine (25 bytes) |
| `0x1036d4c9` | `sub_1036d4c9` | 27 | support routine (27 bytes) |
| `0x1036d4f0` | `sub_1036d4f0` | 8 | trivial accessor/forwarder |
| `0x1036d4f8` | `sub_1036d4f8` | 8 | trivial accessor/forwarder |
| `0x1036d500` | `sub_1036d500` | 11 | trivial accessor/forwarder |
| `0x1036d50b` | `sub_1036d50b` | 11 | trivial accessor/forwarder |
| `0x1036d516` | `sub_1036d516` | 27 | support routine (27 bytes) |
| `0x1036d540` | `sub_1036d540` | 11 | trivial accessor/forwarder |
| `0x1036d54b` | `sub_1036d54b` | 14 | trivial accessor/forwarder |
| `0x1036d559` | `sub_1036d559` | 14 | trivial accessor/forwarder |
| `0x1036d567` | `sub_1036d567` | 27 | support routine (27 bytes) |
| `0x1036d590` | `sub_1036d590` | 11 | trivial accessor/forwarder |
| `0x1036d59b` | `sub_1036d59b` | 14 | trivial accessor/forwarder |
| `0x1036d5a9` | `sub_1036d5a9` | 14 | trivial accessor/forwarder |
| `0x1036d5b7` | `sub_1036d5b7` | 27 | support routine (27 bytes) |
| `0x1036d5e0` | `sub_1036d5e0` | 11 | trivial accessor/forwarder |
| `0x1036d5eb` | `sub_1036d5eb` | 14 | trivial accessor/forwarder |
| `0x1036d5f9` | `sub_1036d5f9` | 14 | trivial accessor/forwarder |
| `0x1036d607` | `sub_1036d607` | 27 | support routine (27 bytes) |
| `0x1036d630` | `sub_1036d630` | 8 | trivial accessor/forwarder |
| `0x1036d638` | `sub_1036d638` | 27 | support routine (27 bytes) |
| `0x1036d660` | `sub_1036d660` | 8 | trivial accessor/forwarder |
| `0x1036d668` | `sub_1036d668` | 27 | support routine (27 bytes) |
| `0x1036d690` | `sub_1036d690` | 8 | trivial accessor/forwarder |
| `0x1036d698` | `sub_1036d698` | 27 | support routine (27 bytes) |
| `0x1036d6c0` | `sub_1036d6c0` | 8 | trivial accessor/forwarder |
| `0x1036d6c8` | `sub_1036d6c8` | 27 | support routine (27 bytes) |
| `0x1036d6f0` | `sub_1036d6f0` | 11 | trivial accessor/forwarder |
| `0x1036d6fb` | `sub_1036d6fb` | 27 | support routine (27 bytes) |
| `0x1036d720` | `sub_1036d720` | 8 | trivial accessor/forwarder |
| `0x1036d728` | `sub_1036d728` | 27 | support routine (27 bytes) |
| `0x1036d750` | `sub_1036d750` | 8 | trivial accessor/forwarder |
| `0x1036d758` | `sub_1036d758` | 27 | support routine (27 bytes) |
| `0x1036d780` | `sub_1036d780` | 8 | trivial accessor/forwarder |
| `0x1036d788` | `sub_1036d788` | 27 | support routine (27 bytes) |
| `0x1036d7b0` | `sub_1036d7b0` | 8 | trivial accessor/forwarder |
| `0x1036d7b8` | `sub_1036d7b8` | 27 | support routine (27 bytes) |
| `0x1036d7e0` | `sub_1036d7e0` | 8 | trivial accessor/forwarder |
| `0x1036d7e8` | `sub_1036d7e8` | 27 | support routine (27 bytes) |
| `0x1036d810` | `sub_1036d810` | 27 | support routine (27 bytes) |
| `0x1036d830` | `sub_1036d830` | 8 | trivial accessor/forwarder |
| `0x1036d838` | `sub_1036d838` | 8 | trivial accessor/forwarder |
| `0x1036d840` | `sub_1036d840` | 27 | support routine (27 bytes) |
| `0x1036d860` | `sub_1036d860` | 8 | trivial accessor/forwarder |
| `0x1036d868` | `sub_1036d868` | 8 | trivial accessor/forwarder |
| `0x1036d870` | `sub_1036d870` | 27 | support routine (27 bytes) |
| `0x1036d890` | `sub_1036d890` | 8 | trivial accessor/forwarder |
| `0x1036d898` | `sub_1036d898` | 27 | support routine (27 bytes) |
| `0x1036d8c0` | `sub_1036d8c0` | 8 | trivial accessor/forwarder |
| `0x1036d8c8` | `sub_1036d8c8` | 27 | support routine (27 bytes) |
| `0x1036d8f0` | `sub_1036d8f0` | 8 | trivial accessor/forwarder |
| `0x1036d8f8` | `sub_1036d8f8` | 27 | support routine (27 bytes) |
| `0x1036d920` | `sub_1036d920` | 8 | trivial accessor/forwarder |
| `0x1036d928` | `sub_1036d928` | 27 | support routine (27 bytes) |
| `0x1036d950` | `sub_1036d950` | 27 | support routine (27 bytes) |
| `0x1036d970` | `sub_1036d970` | 27 | support routine (27 bytes) |
| `0x1036d990` | `sub_1036d990` | 8 | trivial accessor/forwarder |
| `0x1036d998` | `sub_1036d998` | 27 | support routine (27 bytes) |
| `0x1036d9c0` | `sub_1036d9c0` | 8 | trivial accessor/forwarder |
| `0x1036d9c8` | `sub_1036d9c8` | 27 | support routine (27 bytes) |
| `0x1036d9f0` | `sub_1036d9f0` | 8 | trivial accessor/forwarder |
| `0x1036d9f8` | `sub_1036d9f8` | 8 | trivial accessor/forwarder |
| `0x1036da00` | `sub_1036da00` | 27 | support routine (27 bytes) |
| `0x1036da20` | `sub_1036da20` | 8 | trivial accessor/forwarder |
| `0x1036da28` | `sub_1036da28` | 27 | support routine (27 bytes) |
| `0x1036da50` | `sub_1036da50` | 8 | trivial accessor/forwarder |
| `0x1036da58` | `sub_1036da58` | 8 | trivial accessor/forwarder |
| `0x1036da60` | `sub_1036da60` | 27 | support routine (27 bytes) |
| `0x1036da80` | `sub_1036da80` | 8 | trivial accessor/forwarder |
| `0x1036da88` | `sub_1036da88` | 27 | support routine (27 bytes) |
| `0x1036dab0` | `sub_1036dab0` | 8 | trivial accessor/forwarder |
| `0x1036dab8` | `sub_1036dab8` | 27 | support routine (27 bytes) |
| `0x1036dae0` | `sub_1036dae0` | 8 | trivial accessor/forwarder |
| `0x1036dae8` | `sub_1036dae8` | 8 | trivial accessor/forwarder |
| `0x1036daf0` | `sub_1036daf0` | 27 | support routine (27 bytes) |
| `0x1036db10` | `sub_1036db10` | 8 | trivial accessor/forwarder |
| `0x1036db18` | `sub_1036db18` | 27 | support routine (27 bytes) |
| `0x1036db40` | `sub_1036db40` | 3 | trivial accessor/forwarder |
| `0x1036db43` | `sub_1036db43` | 14 | trivial accessor/forwarder |
| `0x1036db51` | `sub_1036db51` | 27 | support routine (27 bytes) |
| `0x1036db70` | `sub_1036db70` | 3 | trivial accessor/forwarder |
| `0x1036db73` | `sub_1036db73` | 14 | trivial accessor/forwarder |
| `0x1036db81` | `sub_1036db81` | 27 | support routine (27 bytes) |
| `0x1036dba0` | `sub_1036dba0` | 27 | support routine (27 bytes) |
| `0x1036dbc0` | `sub_1036dbc0` | 8 | trivial accessor/forwarder |
| `0x1036dbc8` | `sub_1036dbc8` | 27 | support routine (27 bytes) |
| `0x1036dbf0` | `sub_1036dbf0` | 8 | trivial accessor/forwarder |
| `0x1036dbf8` | `sub_1036dbf8` | 27 | support routine (27 bytes) |
| `0x1036dc20` | `sub_1036dc20` | 8 | trivial accessor/forwarder |
| `0x1036dc28` | `sub_1036dc28` | 27 | support routine (27 bytes) |
| `0x1036dc50` | `sub_1036dc50` | 27 | support routine (27 bytes) |
| `0x1036dc70` | `sub_1036dc70` | 8 | trivial accessor/forwarder |
| `0x1036dc78` | `sub_1036dc78` | 27 | support routine (27 bytes) |
| `0x1036dca0` | `sub_1036dca0` | 8 | trivial accessor/forwarder |
| `0x1036dca8` | `sub_1036dca8` | 37 | support routine (37 bytes) |
| `0x1036dcd0` | `sub_1036dcd0` | 8 | trivial accessor/forwarder |
| `0x1036dcd8` | `sub_1036dcd8` | 27 | support routine (27 bytes) |
| `0x1036dd00` | `sub_1036dd00` | 8 | trivial accessor/forwarder |
| `0x1036dd08` | `sub_1036dd08` | 27 | support routine (27 bytes) |
| `0x1036dd30` | `sub_1036dd30` | 8 | trivial accessor/forwarder |
| `0x1036dd38` | `sub_1036dd38` | 27 | support routine (27 bytes) |
| `0x1036dd60` | `sub_1036dd60` | 8 | trivial accessor/forwarder |
| `0x1036dd68` | `sub_1036dd68` | 25 | support routine (25 bytes) |
| `0x1036dd81` | `sub_1036dd81` | 37 | support routine (37 bytes) |
| `0x1036ddb0` | `sub_1036ddb0` | 8 | trivial accessor/forwarder |
| `0x1036ddb8` | `sub_1036ddb8` | 25 | support routine (25 bytes) |
| `0x1036ddd1` | `sub_1036ddd1` | 37 | support routine (37 bytes) |
| `0x1036de00` | `sub_1036de00` | 8 | trivial accessor/forwarder |
| `0x1036de08` | `sub_1036de08` | 11 | trivial accessor/forwarder |
| `0x1036de13` | `sub_1036de13` | 11 | trivial accessor/forwarder |
| `0x1036de1e` | `sub_1036de1e` | 30 | support routine (30 bytes) |
| `0x1036de40` | `sub_1036de40` | 8 | trivial accessor/forwarder |
| `0x1036de48` | `sub_1036de48` | 11 | trivial accessor/forwarder |
| `0x1036de53` | `sub_1036de53` | 11 | trivial accessor/forwarder |
| `0x1036de5e` | `sub_1036de5e` | 30 | support routine (30 bytes) |
| `0x1036de80` | `sub_1036de80` | 8 | trivial accessor/forwarder |
| `0x1036de88` | `sub_1036de88` | 11 | trivial accessor/forwarder |
| `0x1036de93` | `sub_1036de93` | 11 | trivial accessor/forwarder |
| `0x1036de9e` | `sub_1036de9e` | 30 | support routine (30 bytes) |
| `0x1036dec0` | `sub_1036dec0` | 8 | trivial accessor/forwarder |
| `0x1036dec8` | `sub_1036dec8` | 11 | trivial accessor/forwarder |
| `0x1036ded3` | `sub_1036ded3` | 11 | trivial accessor/forwarder |
| `0x1036dede` | `sub_1036dede` | 30 | support routine (30 bytes) |
| `0x1036df00` | `sub_1036df00` | 31 | support routine (31 bytes) |
| `0x1036df1f` | `sub_1036df1f` | 8 | trivial accessor/forwarder |
| `0x1036df27` | `sub_1036df27` | 8 | trivial accessor/forwarder |
| `0x1036df2f` | `sub_1036df2f` | 11 | trivial accessor/forwarder |
| `0x1036df3a` | `sub_1036df3a` | 11 | trivial accessor/forwarder |
| `0x1036df45` | `sub_1036df45` | 11 | trivial accessor/forwarder |
| `0x1036df50` | `sub_1036df50` | 40 | support routine (40 bytes) |
| `0x1036df80` | `sub_1036df80` | 25 | support routine (25 bytes) |
| `0x1036df99` | `sub_1036df99` | 27 | support routine (27 bytes) |
| `0x1036dfc0` | `sub_1036dfc0` | 31 | support routine (31 bytes) |
| `0x1036dfdf` | `sub_1036dfdf` | 8 | trivial accessor/forwarder |
| `0x1036dfe7` | `sub_1036dfe7` | 8 | trivial accessor/forwarder |
| `0x1036dfef` | `sub_1036dfef` | 11 | trivial accessor/forwarder |
| `0x1036dffa` | `sub_1036dffa` | 11 | trivial accessor/forwarder |
| `0x1036e005` | `sub_1036e005` | 11 | trivial accessor/forwarder |
| `0x1036e010` | `sub_1036e010` | 40 | support routine (40 bytes) |
| `0x1036e040` | `sub_1036e040` | 25 | support routine (25 bytes) |
| `0x1036e059` | `sub_1036e059` | 27 | support routine (27 bytes) |
| `0x1036e080` | `sub_1036e080` | 8 | trivial accessor/forwarder |
| `0x1036e088` | `sub_1036e088` | 30 | support routine (30 bytes) |
| `0x1036e0b0` | `sub_1036e0b0` | 8 | trivial accessor/forwarder |
| `0x1036e0b8` | `sub_1036e0b8` | 30 | support routine (30 bytes) |
| `0x1036e0e0` | `sub_1036e0e0` | 8 | trivial accessor/forwarder |
| `0x1036e0e8` | `sub_1036e0e8` | 27 | support routine (27 bytes) |
| `0x1036e110` | `sub_1036e110` | 8 | trivial accessor/forwarder |
| `0x1036e118` | `sub_1036e118` | 30 | support routine (30 bytes) |
| `0x1036e140` | `sub_1036e140` | 8 | trivial accessor/forwarder |
| `0x1036e148` | `sub_1036e148` | 30 | support routine (30 bytes) |
| `0x1036e170` | `sub_1036e170` | 8 | trivial accessor/forwarder |
| `0x1036e178` | `sub_1036e178` | 27 | support routine (27 bytes) |
| `0x1036e1a0` | `sub_1036e1a0` | 8 | trivial accessor/forwarder |
| `0x1036e1a8` | `sub_1036e1a8` | 11 | trivial accessor/forwarder |
| `0x1036e1b3` | `sub_1036e1b3` | 27 | support routine (27 bytes) |
| `0x1036e1d0` | `sub_1036e1d0` | 8 | trivial accessor/forwarder |
| `0x1036e1d8` | `sub_1036e1d8` | 11 | trivial accessor/forwarder |
| `0x1036e1e3` | `sub_1036e1e3` | 27 | support routine (27 bytes) |
| `0x1036e200` | `sub_1036e200` | 8 | trivial accessor/forwarder |
| `0x1036e208` | `sub_1036e208` | 11 | trivial accessor/forwarder |
| `0x1036e213` | `sub_1036e213` | 27 | support routine (27 bytes) |
| `0x1036e230` | `sub_1036e230` | 8 | trivial accessor/forwarder |
| `0x1036e238` | `sub_1036e238` | 11 | trivial accessor/forwarder |
| `0x1036e243` | `sub_1036e243` | 27 | support routine (27 bytes) |
| `0x1036e260` | `sub_1036e260` | 8 | trivial accessor/forwarder |
| `0x1036e268` | `sub_1036e268` | 27 | support routine (27 bytes) |
| `0x1036e290` | `sub_1036e290` | 8 | trivial accessor/forwarder |
| `0x1036e298` | `sub_1036e298` | 27 | support routine (27 bytes) |
| `0x1036e2c0` | `sub_1036e2c0` | 8 | trivial accessor/forwarder |
| `0x1036e2c8` | `sub_1036e2c8` | 27 | support routine (27 bytes) |
| `0x1036e2f0` | `sub_1036e2f0` | 8 | trivial accessor/forwarder |
| `0x1036e2f8` | `sub_1036e2f8` | 27 | support routine (27 bytes) |
| `0x1036e320` | `sub_1036e320` | 8 | trivial accessor/forwarder |
| `0x1036e328` | `sub_1036e328` | 11 | trivial accessor/forwarder |
| `0x1036e333` | `sub_1036e333` | 27 | support routine (27 bytes) |
| `0x1036e350` | `sub_1036e350` | 8 | trivial accessor/forwarder |
| `0x1036e358` | `sub_1036e358` | 11 | trivial accessor/forwarder |
| `0x1036e363` | `sub_1036e363` | 27 | support routine (27 bytes) |
| `0x1036e380` | `sub_1036e380` | 8 | trivial accessor/forwarder |
| `0x1036e388` | `sub_1036e388` | 27 | support routine (27 bytes) |
| `0x1036e3b0` | `sub_1036e3b0` | 8 | trivial accessor/forwarder |
| `0x1036e3b8` | `sub_1036e3b8` | 11 | trivial accessor/forwarder |
| `0x1036e3c3` | `sub_1036e3c3` | 27 | support routine (27 bytes) |
| `0x1036e3e0` | `sub_1036e3e0` | 8 | trivial accessor/forwarder |
| `0x1036e3e8` | `sub_1036e3e8` | 11 | trivial accessor/forwarder |
| `0x1036e3f3` | `sub_1036e3f3` | 27 | support routine (27 bytes) |
| `0x1036e410` | `sub_1036e410` | 8 | trivial accessor/forwarder |
| `0x1036e418` | `sub_1036e418` | 27 | support routine (27 bytes) |
| `0x1036e440` | `sub_1036e440` | 8 | trivial accessor/forwarder |
| `0x1036e448` | `sub_1036e448` | 25 | support routine (25 bytes) |
| `0x1036e461` | `sub_1036e461` | 27 | support routine (27 bytes) |
| `0x1036e480` | `sub_1036e480` | 25 | support routine (25 bytes) |
| `0x1036e499` | `sub_1036e499` | 27 | support routine (27 bytes) |
| `0x1036e4c0` | `sub_1036e4c0` | 8 | trivial accessor/forwarder |
| `0x1036e4c8` | `sub_1036e4c8` | 25 | support routine (25 bytes) |
| `0x1036e4e1` | `sub_1036e4e1` | 27 | support routine (27 bytes) |
| `0x1036e500` | `sub_1036e500` | 25 | support routine (25 bytes) |
| `0x1036e519` | `sub_1036e519` | 27 | support routine (27 bytes) |
| `0x1036e540` | `sub_1036e540` | 8 | trivial accessor/forwarder |
| `0x1036e548` | `sub_1036e548` | 27 | support routine (27 bytes) |
| `0x1036e570` | `sub_1036e570` | 8 | trivial accessor/forwarder |
| `0x1036e578` | `sub_1036e578` | 27 | support routine (27 bytes) |
| `0x1036e5a0` | `sub_1036e5a0` | 8 | trivial accessor/forwarder |
| `0x1036e5a8` | `sub_1036e5a8` | 11 | trivial accessor/forwarder |
| `0x1036e5b3` | `sub_1036e5b3` | 27 | support routine (27 bytes) |
| `0x1036e5d0` | `sub_1036e5d0` | 8 | trivial accessor/forwarder |
| `0x1036e5d8` | `sub_1036e5d8` | 11 | trivial accessor/forwarder |
| `0x1036e5e3` | `sub_1036e5e3` | 27 | support routine (27 bytes) |
| `0x1036e600` | `sub_1036e600` | 8 | trivial accessor/forwarder |
| `0x1036e608` | `sub_1036e608` | 27 | support routine (27 bytes) |
| `0x1036e630` | `sub_1036e630` | 25 | support routine (25 bytes) |
| `0x1036e649` | `sub_1036e649` | 27 | support routine (27 bytes) |
| `0x1036e670` | `sub_1036e670` | 8 | trivial accessor/forwarder |
| `0x1036e678` | `sub_1036e678` | 8 | trivial accessor/forwarder |
| `0x1036e680` | `sub_1036e680` | 27 | support routine (27 bytes) |
| `0x1036e6a0` | `sub_1036e6a0` | 8 | trivial accessor/forwarder |
| `0x1036e6a8` | `sub_1036e6a8` | 11 | trivial accessor/forwarder |
| `0x1036e6b3` | `sub_1036e6b3` | 27 | support routine (27 bytes) |
| `0x1036e6d0` | `sub_1036e6d0` | 8 | trivial accessor/forwarder |
| `0x1036e6d8` | `sub_1036e6d8` | 39 | support routine (39 bytes) |
| `0x1036e6ff` | `sub_1036e6ff` | 27 | support routine (27 bytes) |
| `0x1036e720` | `sub_1036e720` | 8 | trivial accessor/forwarder |
| `0x1036e728` | `sub_1036e728` | 39 | support routine (39 bytes) |
| `0x1036e74f` | `sub_1036e74f` | 27 | support routine (27 bytes) |
| `0x1036e770` | `sub_1036e770` | 11 | trivial accessor/forwarder |
| `0x1036e77b` | `sub_1036e77b` | 27 | support routine (27 bytes) |
| `0x1036e7a0` | `sub_1036e7a0` | 8 | trivial accessor/forwarder |
| `0x1036e7a8` | `sub_1036e7a8` | 39 | support routine (39 bytes) |
| `0x1036e7cf` | `sub_1036e7cf` | 27 | support routine (27 bytes) |
| `0x1036e7f0` | `sub_1036e7f0` | 8 | trivial accessor/forwarder |
| `0x1036e7f8` | `sub_1036e7f8` | 39 | support routine (39 bytes) |
| `0x1036e81f` | `sub_1036e81f` | 27 | support routine (27 bytes) |
| `0x1036e840` | `sub_1036e840` | 11 | trivial accessor/forwarder |
| `0x1036e84b` | `sub_1036e84b` | 27 | support routine (27 bytes) |
| `0x1036e870` | `sub_1036e870` | 8 | trivial accessor/forwarder |
| `0x1036e878` | `sub_1036e878` | 39 | support routine (39 bytes) |
| `0x1036e89f` | `sub_1036e89f` | 27 | support routine (27 bytes) |
| `0x1036e8c0` | `sub_1036e8c0` | 8 | trivial accessor/forwarder |
| `0x1036e8c8` | `sub_1036e8c8` | 39 | support routine (39 bytes) |
| `0x1036e8ef` | `sub_1036e8ef` | 27 | support routine (27 bytes) |
| `0x1036e910` | `sub_1036e910` | 11 | trivial accessor/forwarder |
| `0x1036e91b` | `sub_1036e91b` | 27 | support routine (27 bytes) |
| `0x1036e940` | `sub_1036e940` | 8 | trivial accessor/forwarder |
| `0x1036e948` | `sub_1036e948` | 39 | support routine (39 bytes) |
| `0x1036e96f` | `sub_1036e96f` | 27 | support routine (27 bytes) |
| `0x1036e990` | `sub_1036e990` | 8 | trivial accessor/forwarder |
| `0x1036e998` | `sub_1036e998` | 39 | support routine (39 bytes) |
| `0x1036e9bf` | `sub_1036e9bf` | 27 | support routine (27 bytes) |
| `0x1036e9e0` | `sub_1036e9e0` | 11 | trivial accessor/forwarder |
| `0x1036e9eb` | `sub_1036e9eb` | 27 | support routine (27 bytes) |
| `0x1036ea10` | `sub_1036ea10` | 11 | trivial accessor/forwarder |
| `0x1036ea1b` | `sub_1036ea1b` | 27 | support routine (27 bytes) |
| `0x1036ea40` | `sub_1036ea40` | 11 | trivial accessor/forwarder |
| `0x1036ea4b` | `sub_1036ea4b` | 27 | support routine (27 bytes) |
| `0x1036ea70` | `sub_1036ea70` | 8 | trivial accessor/forwarder |
| `0x1036ea78` | `sub_1036ea78` | 11 | trivial accessor/forwarder |
| `0x1036ea83` | `sub_1036ea83` | 11 | trivial accessor/forwarder |
| `0x1036ea8e` | `sub_1036ea8e` | 27 | support routine (27 bytes) |
| `0x1036eab0` | `sub_1036eab0` | 8 | trivial accessor/forwarder |
| `0x1036eab8` | `sub_1036eab8` | 11 | trivial accessor/forwarder |
| `0x1036eac3` | `sub_1036eac3` | 27 | support routine (27 bytes) |
| `0x1036eae0` | `sub_1036eae0` | 8 | trivial accessor/forwarder |
| `0x1036eae8` | `sub_1036eae8` | 30 | support routine (30 bytes) |
| `0x1036eb10` | `sub_1036eb10` | 8 | trivial accessor/forwarder |
| `0x1036eb18` | `sub_1036eb18` | 11 | trivial accessor/forwarder |
| `0x1036eb23` | `sub_1036eb23` | 11 | trivial accessor/forwarder |
| `0x1036eb2e` | `sub_1036eb2e` | 27 | support routine (27 bytes) |
| `0x1036eb50` | `sub_1036eb50` | 8 | trivial accessor/forwarder |
| `0x1036eb58` | `sub_1036eb58` | 30 | support routine (30 bytes) |
| `0x1036eb80` | `sub_1036eb80` | 25 | support routine (25 bytes) |
| `0x1036eb99` | `sub_1036eb99` | 27 | support routine (27 bytes) |
| `0x1036ebc0` | `sub_1036ebc0` | 25 | support routine (25 bytes) |
| `0x1036ebd9` | `sub_1036ebd9` | 27 | support routine (27 bytes) |
| `0x1036ec00` | `sub_1036ec00` | 25 | support routine (25 bytes) |
| `0x1036ec19` | `sub_1036ec19` | 27 | support routine (27 bytes) |
| `0x1036ec40` | `sub_1036ec40` | 25 | support routine (25 bytes) |
| `0x1036ec59` | `sub_1036ec59` | 27 | support routine (27 bytes) |
| `0x1036ec80` | `sub_1036ec80` | 8 | trivial accessor/forwarder |
| `0x1036ec88` | `sub_1036ec88` | 8 | trivial accessor/forwarder |
| `0x1036ec90` | `sub_1036ec90` | 37 | support routine (37 bytes) |
| `0x1036ecc0` | `sub_1036ecc0` | 8 | trivial accessor/forwarder |
| `0x1036ecc8` | `sub_1036ecc8` | 8 | trivial accessor/forwarder |
| `0x1036ecd0` | `sub_1036ecd0` | 37 | support routine (37 bytes) |
| `0x1036ed00` | `sub_1036ed00` | 8 | trivial accessor/forwarder |
| `0x1036ed08` | `sub_1036ed08` | 8 | trivial accessor/forwarder |
| `0x1036ed10` | `sub_1036ed10` | 37 | support routine (37 bytes) |
| `0x1036ed40` | `sub_1036ed40` | 27 | support routine (27 bytes) |
| `0x1036ed60` | `sub_1036ed60` | 27 | support routine (27 bytes) |
| `0x1036ed80` | `sub_1036ed80` | 25 | support routine (25 bytes) |
| `0x1036ed99` | `sub_1036ed99` | 27 | support routine (27 bytes) |
| `0x1036edc0` | `sub_1036edc0` | 25 | support routine (25 bytes) |
| `0x1036edd9` | `sub_1036edd9` | 27 | support routine (27 bytes) |
| `0x1036ee00` | `sub_1036ee00` | 25 | support routine (25 bytes) |
| `0x1036ee19` | `sub_1036ee19` | 27 | support routine (27 bytes) |
| `0x1036ee40` | `sub_1036ee40` | 25 | support routine (25 bytes) |
| `0x1036ee59` | `sub_1036ee59` | 27 | support routine (27 bytes) |
| `0x1036ee80` | `sub_1036ee80` | 8 | trivial accessor/forwarder |
| `0x1036ee88` | `sub_1036ee88` | 11 | trivial accessor/forwarder |
| `0x1036ee93` | `sub_1036ee93` | 11 | trivial accessor/forwarder |
| `0x1036ee9e` | `sub_1036ee9e` | 27 | support routine (27 bytes) |
| `0x1036eec0` | `sub_1036eec0` | 8 | trivial accessor/forwarder |
| `0x1036eec8` | `sub_1036eec8` | 27 | support routine (27 bytes) |
| `0x1036eef0` | `sub_1036eef0` | 8 | trivial accessor/forwarder |
| `0x1036eef8` | `sub_1036eef8` | 11 | trivial accessor/forwarder |
| `0x1036ef03` | `sub_1036ef03` | 27 | support routine (27 bytes) |
| `0x1036ef20` | `sub_1036ef20` | 8 | trivial accessor/forwarder |
| `0x1036ef28` | `sub_1036ef28` | 11 | trivial accessor/forwarder |
| `0x1036ef33` | `sub_1036ef33` | 27 | support routine (27 bytes) |
| `0x1036ef50` | `sub_1036ef50` | 8 | trivial accessor/forwarder |
| `0x1036ef58` | `sub_1036ef58` | 11 | trivial accessor/forwarder |
| `0x1036ef63` | `sub_1036ef63` | 27 | support routine (27 bytes) |
| `0x1036ef80` | `sub_1036ef80` | 8 | trivial accessor/forwarder |
| `0x1036ef88` | `sub_1036ef88` | 11 | trivial accessor/forwarder |
| `0x1036ef93` | `sub_1036ef93` | 27 | support routine (27 bytes) |
| `0x1036efb0` | `sub_1036efb0` | 8 | trivial accessor/forwarder |
| `0x1036efb8` | `sub_1036efb8` | 11 | trivial accessor/forwarder |
| `0x1036efc3` | `sub_1036efc3` | 11 | trivial accessor/forwarder |
| `0x1036efce` | `sub_1036efce` | 27 | support routine (27 bytes) |
| `0x1036eff0` | `sub_1036eff0` | 8 | trivial accessor/forwarder |
| `0x1036eff8` | `sub_1036eff8` | 27 | support routine (27 bytes) |
| `0x1036f020` | `sub_1036f020` | 8 | trivial accessor/forwarder |
| `0x1036f028` | `sub_1036f028` | 11 | trivial accessor/forwarder |
| `0x1036f033` | `sub_1036f033` | 27 | support routine (27 bytes) |
| `0x1036f050` | `sub_1036f050` | 8 | trivial accessor/forwarder |
| `0x1036f058` | `sub_1036f058` | 11 | trivial accessor/forwarder |
| `0x1036f063` | `sub_1036f063` | 27 | support routine (27 bytes) |
| `0x1036f080` | `sub_1036f080` | 8 | trivial accessor/forwarder |
| `0x1036f088` | `sub_1036f088` | 11 | trivial accessor/forwarder |
| `0x1036f093` | `sub_1036f093` | 27 | support routine (27 bytes) |
| `0x1036f0b0` | `sub_1036f0b0` | 8 | trivial accessor/forwarder |
| `0x1036f0b8` | `sub_1036f0b8` | 27 | support routine (27 bytes) |
| `0x1036f0e0` | `sub_1036f0e0` | 8 | trivial accessor/forwarder |
| `0x1036f0e8` | `sub_1036f0e8` | 27 | support routine (27 bytes) |
| `0x1036f110` | `sub_1036f110` | 8 | trivial accessor/forwarder |
| `0x1036f118` | `sub_1036f118` | 27 | support routine (27 bytes) |
| `0x1036f140` | `sub_1036f140` | 11 | trivial accessor/forwarder |
| `0x1036f14b` | `sub_1036f14b` | 27 | support routine (27 bytes) |
| `0x1036f170` | `sub_1036f170` | 11 | trivial accessor/forwarder |
| `0x1036f17b` | `sub_1036f17b` | 27 | support routine (27 bytes) |
| `0x1036f1a0` | `sub_1036f1a0` | 8 | trivial accessor/forwarder |
| `0x1036f1a8` | `sub_1036f1a8` | 8 | trivial accessor/forwarder |
| `0x1036f1b0` | `sub_1036f1b0` | 27 | support routine (27 bytes) |
| `0x1036f1d0` | `sub_1036f1d0` | 8 | trivial accessor/forwarder |
| `0x1036f1d8` | `sub_1036f1d8` | 27 | support routine (27 bytes) |
| `0x1036f200` | `sub_1036f200` | 11 | trivial accessor/forwarder |
| `0x1036f20b` | `sub_1036f20b` | 27 | support routine (27 bytes) |
| `0x1036f230` | `sub_1036f230` | 8 | trivial accessor/forwarder |
| `0x1036f238` | `sub_1036f238` | 27 | support routine (27 bytes) |
| `0x1036f260` | `sub_1036f260` | 11 | trivial accessor/forwarder |
| `0x1036f26b` | `sub_1036f26b` | 27 | support routine (27 bytes) |
| `0x1036f290` | `sub_1036f290` | 8 | trivial accessor/forwarder |
| `0x1036f298` | `sub_1036f298` | 27 | support routine (27 bytes) |
| `0x1036f2c0` | `sub_1036f2c0` | 8 | trivial accessor/forwarder |
| `0x1036f2c8` | `sub_1036f2c8` | 11 | trivial accessor/forwarder |
| `0x1036f2d3` | `sub_1036f2d3` | 27 | support routine (27 bytes) |
| `0x1036f2f0` | `sub_1036f2f0` | 8 | trivial accessor/forwarder |
| `0x1036f2f8` | `sub_1036f2f8` | 11 | trivial accessor/forwarder |
| `0x1036f303` | `sub_1036f303` | 27 | support routine (27 bytes) |
| `0x1036f320` | `sub_1036f320` | 8 | trivial accessor/forwarder |
| `0x1036f328` | `sub_1036f328` | 11 | trivial accessor/forwarder |
| `0x1036f333` | `sub_1036f333` | 27 | support routine (27 bytes) |
| `0x1036f350` | `sub_1036f350` | 8 | trivial accessor/forwarder |
| `0x1036f358` | `sub_1036f358` | 11 | trivial accessor/forwarder |
| `0x1036f363` | `sub_1036f363` | 27 | support routine (27 bytes) |
| `0x1036f380` | `sub_1036f380` | 8 | trivial accessor/forwarder |
| `0x1036f388` | `sub_1036f388` | 11 | trivial accessor/forwarder |
| `0x1036f393` | `sub_1036f393` | 27 | support routine (27 bytes) |
| `0x1036f3b0` | `sub_1036f3b0` | 8 | trivial accessor/forwarder |
| `0x1036f3b8` | `sub_1036f3b8` | 11 | trivial accessor/forwarder |
| `0x1036f3c3` | `sub_1036f3c3` | 27 | support routine (27 bytes) |
| `0x1036f3e0` | `sub_1036f3e0` | 8 | trivial accessor/forwarder |
| `0x1036f3e8` | `sub_1036f3e8` | 11 | trivial accessor/forwarder |
| `0x1036f3f3` | `sub_1036f3f3` | 27 | support routine (27 bytes) |
| `0x1036f410` | `sub_1036f410` | 8 | trivial accessor/forwarder |
| `0x1036f418` | `sub_1036f418` | 11 | trivial accessor/forwarder |
| `0x1036f423` | `sub_1036f423` | 27 | support routine (27 bytes) |
| `0x1036f440` | `sub_1036f440` | 8 | trivial accessor/forwarder |
| `0x1036f448` | `sub_1036f448` | 39 | support routine (39 bytes) |
| `0x1036f46f` | `sub_1036f46f` | 27 | support routine (27 bytes) |
| `0x1036f490` | `sub_1036f490` | 8 | trivial accessor/forwarder |
| `0x1036f498` | `sub_1036f498` | 39 | support routine (39 bytes) |
| `0x1036f4bf` | `sub_1036f4bf` | 27 | support routine (27 bytes) |
| `0x1036f4e0` | `sub_1036f4e0` | 11 | trivial accessor/forwarder |
| `0x1036f4eb` | `sub_1036f4eb` | 27 | support routine (27 bytes) |
| `0x1036f510` | `sub_1036f510` | 8 | trivial accessor/forwarder |
| `0x1036f518` | `sub_1036f518` | 39 | support routine (39 bytes) |
| `0x1036f53f` | `sub_1036f53f` | 27 | support routine (27 bytes) |
| `0x1036f560` | `sub_1036f560` | 8 | trivial accessor/forwarder |
| `0x1036f568` | `sub_1036f568` | 39 | support routine (39 bytes) |
| `0x1036f58f` | `sub_1036f58f` | 27 | support routine (27 bytes) |
| `0x1036f5b0` | `sub_1036f5b0` | 11 | trivial accessor/forwarder |
| `0x1036f5bb` | `sub_1036f5bb` | 27 | support routine (27 bytes) |
| `0x1036f5e0` | `sub_1036f5e0` | 8 | trivial accessor/forwarder |
| `0x1036f5e8` | `sub_1036f5e8` | 27 | support routine (27 bytes) |
| `0x1036f610` | `sub_1036f610` | 8 | trivial accessor/forwarder |
| `0x1036f618` | `sub_1036f618` | 27 | support routine (27 bytes) |
| `0x1036f640` | `sub_1036f640` | 8 | trivial accessor/forwarder |
| `0x1036f648` | `sub_1036f648` | 27 | support routine (27 bytes) |
| `0x1036f670` | `sub_1036f670` | 8 | trivial accessor/forwarder |
| `0x1036f678` | `sub_1036f678` | 27 | support routine (27 bytes) |
| `0x1036f6a0` | `sub_1036f6a0` | 8 | trivial accessor/forwarder |
| `0x1036f6a8` | `sub_1036f6a8` | 27 | support routine (27 bytes) |
| `0x1036f6d0` | `sub_1036f6d0` | 8 | trivial accessor/forwarder |
| `0x1036f6d8` | `sub_1036f6d8` | 27 | support routine (27 bytes) |
| `0x1036f700` | `sub_1036f700` | 8 | trivial accessor/forwarder |
| `0x1036f708` | `sub_1036f708` | 27 | support routine (27 bytes) |
| `0x1036f730` | `sub_1036f730` | 25 | support routine (25 bytes) |
| `0x1036f749` | `sub_1036f749` | 27 | support routine (27 bytes) |
| `0x1036f770` | `sub_1036f770` | 25 | support routine (25 bytes) |
| `0x1036f789` | `sub_1036f789` | 27 | support routine (27 bytes) |
| `0x1036f7b0` | `sub_1036f7b0` | 8 | trivial accessor/forwarder |
| `0x1036f7b8` | `sub_1036f7b8` | 27 | support routine (27 bytes) |
| `0x1036f7e0` | `sub_1036f7e0` | 25 | support routine (25 bytes) |
| `0x1036f7f9` | `sub_1036f7f9` | 27 | support routine (27 bytes) |
| `0x1036f820` | `sub_1036f820` | 25 | support routine (25 bytes) |
| `0x1036f839` | `sub_1036f839` | 27 | support routine (27 bytes) |
| `0x1036f860` | `sub_1036f860` | 11 | trivial accessor/forwarder |
| `0x1036f86b` | `sub_1036f86b` | 27 | support routine (27 bytes) |
| `0x1036f890` | `sub_1036f890` | 27 | support routine (27 bytes) |
| `0x1036f8b0` | `sub_1036f8b0` | 8 | trivial accessor/forwarder |
| `0x1036f8b8` | `sub_1036f8b8` | 37 | support routine (37 bytes) |
| `0x1036f8e0` | `sub_1036f8e0` | 3 | trivial accessor/forwarder |
| `0x1036f8e3` | `sub_1036f8e3` | 14 | trivial accessor/forwarder |
| `0x1036f8f1` | `sub_1036f8f1` | 27 | support routine (27 bytes) |
| `0x1036f910` | `sub_1036f910` | 8 | trivial accessor/forwarder |
| `0x1036f918` | `sub_1036f918` | 11 | trivial accessor/forwarder |
| `0x1036f923` | `sub_1036f923` | 27 | support routine (27 bytes) |
| `0x1036f940` | `sub_1036f940` | 8 | trivial accessor/forwarder |
| `0x1036f948` | `sub_1036f948` | 11 | trivial accessor/forwarder |
| `0x1036f953` | `sub_1036f953` | 27 | support routine (27 bytes) |
| `0x1036f970` | `sub_1036f970` | 8 | trivial accessor/forwarder |
| `0x1036f978` | `sub_1036f978` | 11 | trivial accessor/forwarder |
| `0x1036f983` | `sub_1036f983` | 27 | support routine (27 bytes) |
| `0x1036f9a0` | `sub_1036f9a0` | 8 | trivial accessor/forwarder |
| `0x1036f9a8` | `sub_1036f9a8` | 11 | trivial accessor/forwarder |
| `0x1036f9b3` | `sub_1036f9b3` | 27 | support routine (27 bytes) |
| `0x1036f9d0` | `sub_1036f9d0` | 11 | trivial accessor/forwarder |
| `0x1036f9db` | `sub_1036f9db` | 27 | support routine (27 bytes) |
| `0x1036fa00` | `sub_1036fa00` | 11 | trivial accessor/forwarder |
| `0x1036fa0b` | `sub_1036fa0b` | 27 | support routine (27 bytes) |
| `0x1036fa30` | `sub_1036fa30` | 8 | trivial accessor/forwarder |
| `0x1036fa38` | `sub_1036fa38` | 37 | support routine (37 bytes) |
| `0x1036fa60` | `sub_1036fa60` | 11 | trivial accessor/forwarder |
| `0x1036fa6b` | `sub_1036fa6b` | 27 | support routine (27 bytes) |
| `0x1036fa90` | `sub_1036fa90` | 11 | trivial accessor/forwarder |
| `0x1036fa9b` | `sub_1036fa9b` | 27 | support routine (27 bytes) |
| `0x1036fac0` | `sub_1036fac0` | 8 | trivial accessor/forwarder |
| `0x1036fac8` | `sub_1036fac8` | 27 | support routine (27 bytes) |
| `0x1036faf0` | `sub_1036faf0` | 8 | trivial accessor/forwarder |
| `0x1036faf8` | `sub_1036faf8` | 27 | support routine (27 bytes) |
| `0x1036fb20` | `sub_1036fb20` | 8 | trivial accessor/forwarder |
| `0x1036fb28` | `sub_1036fb28` | 27 | support routine (27 bytes) |
| `0x1036fb50` | `sub_1036fb50` | 8 | trivial accessor/forwarder |
| `0x1036fb58` | `sub_1036fb58` | 27 | support routine (27 bytes) |
| `0x1036fb80` | `sub_1036fb80` | 8 | trivial accessor/forwarder |
| `0x1036fb88` | `sub_1036fb88` | 11 | trivial accessor/forwarder |
| `0x1036fb93` | `sub_1036fb93` | 11 | trivial accessor/forwarder |
| `0x1036fb9e` | `sub_1036fb9e` | 27 | support routine (27 bytes) |
| `0x1036fbc0` | `sub_1036fbc0` | 8 | trivial accessor/forwarder |
| `0x1036fbc8` | `sub_1036fbc8` | 11 | trivial accessor/forwarder |
| `0x1036fbd3` | `sub_1036fbd3` | 11 | trivial accessor/forwarder |
| `0x1036fbde` | `sub_1036fbde` | 27 | support routine (27 bytes) |
| `0x1036fc00` | `sub_1036fc00` | 3 | trivial accessor/forwarder |
| `0x1036fc03` | `sub_1036fc03` | 14 | trivial accessor/forwarder |
| `0x1036fc11` | `sub_1036fc11` | 27 | support routine (27 bytes) |
| `0x1036fc30` | `sub_1036fc30` | 3 | trivial accessor/forwarder |
| `0x1036fc33` | `sub_1036fc33` | 14 | trivial accessor/forwarder |
| `0x1036fc41` | `sub_1036fc41` | 27 | support routine (27 bytes) |
| `0x1036fc60` | `sub_1036fc60` | 8 | trivial accessor/forwarder |
| `0x1036fc68` | `sub_1036fc68` | 27 | support routine (27 bytes) |
| `0x1036fc90` | `sub_1036fc90` | 8 | trivial accessor/forwarder |
| `0x1036fc98` | `sub_1036fc98` | 27 | support routine (27 bytes) |
| `0x1036fcc0` | `sub_1036fcc0` | 8 | trivial accessor/forwarder |
| `0x1036fcc8` | `sub_1036fcc8` | 27 | support routine (27 bytes) |
| `0x1036fcf0` | `sub_1036fcf0` | 11 | trivial accessor/forwarder |
| `0x1036fcfb` | `sub_1036fcfb` | 11 | trivial accessor/forwarder |
| `0x1036fd06` | `sub_1036fd06` | 30 | support routine (30 bytes) |
| `0x1036fd24` | `sub_1036fd24` | 8 | trivial accessor/forwarder |
| `0x1036fd2c` | `sub_1036fd2c` | 27 | support routine (27 bytes) |
| `0x1036fd47` | `sub_1036fd47` | 8 | trivial accessor/forwarder |
| `0x1036fd4f` | `sub_1036fd4f` | 27 | support routine (27 bytes) |
| `0x1036fd6a` | `sub_1036fd6a` | 8 | trivial accessor/forwarder |
| `0x1036fd72` | `sub_1036fd72` | 27 | support routine (27 bytes) |
| `0x1036fd8d` | `sub_1036fd8d` | 8 | trivial accessor/forwarder |
| `0x1036fd95` | `sub_1036fd95` | 27 | support routine (27 bytes) |
| `0x1036fdb0` | `sub_1036fdb0` | 8 | trivial accessor/forwarder |
| `0x1036fdb8` | `sub_1036fdb8` | 27 | support routine (27 bytes) |
| `0x1036fdd3` | `sub_1036fdd3` | 8 | trivial accessor/forwarder |
| `0x1036fddb` | `sub_1036fddb` | 27 | support routine (27 bytes) |
| `0x1036fdf6` | `sub_1036fdf6` | 8 | trivial accessor/forwarder |
| `0x1036fdfe` | `sub_1036fdfe` | 27 | support routine (27 bytes) |
| `0x1036fe19` | `sub_1036fe19` | 8 | trivial accessor/forwarder |
| `0x1036fe21` | `sub_1036fe21` | 27 | support routine (27 bytes) |
| `0x1036fe3c` | `sub_1036fe3c` | 8 | trivial accessor/forwarder |
| `0x1036fe44` | `sub_1036fe44` | 27 | support routine (27 bytes) |
| `0x1036fe5f` | `sub_1036fe5f` | 11 | trivial accessor/forwarder |
| `0x1036fe6a` | `sub_1036fe6a` | 31 | support routine (31 bytes) |
| `0x1036fe89` | `sub_1036fe89` | 40 | support routine (40 bytes) |
| `0x1036fec0` | `sub_1036fec0` | 8 | trivial accessor/forwarder |
| `0x1036fec8` | `sub_1036fec8` | 11 | trivial accessor/forwarder |
| `0x1036fed3` | `sub_1036fed3` | 11 | trivial accessor/forwarder |
| `0x1036fede` | `sub_1036fede` | 11 | trivial accessor/forwarder |
| `0x1036fee9` | `sub_1036fee9` | 14 | trivial accessor/forwarder |
| `0x1036fef7` | `sub_1036fef7` | 27 | support routine (27 bytes) |
| `0x1036ff20` | `sub_1036ff20` | 8 | trivial accessor/forwarder |
| `0x1036ff28` | `sub_1036ff28` | 27 | support routine (27 bytes) |
| `0x1036ff50` | `sub_1036ff50` | 11 | trivial accessor/forwarder |
| `0x1036ff5b` | `sub_1036ff5b` | 27 | support routine (27 bytes) |
| `0x1036ff80` | `sub_1036ff80` | 8 | trivial accessor/forwarder |
| `0x1036ff88` | `sub_1036ff88` | 27 | support routine (27 bytes) |
| `0x1036ffb0` | `sub_1036ffb0` | 8 | trivial accessor/forwarder |
| `0x1036ffb8` | `sub_1036ffb8` | 11 | trivial accessor/forwarder |
| `0x1036ffc3` | `sub_1036ffc3` | 11 | trivial accessor/forwarder |
| `0x1036ffce` | `sub_1036ffce` | 11 | trivial accessor/forwarder |
| `0x1036ffd9` | `sub_1036ffd9` | 14 | trivial accessor/forwarder |
| `0x1036ffe7` | `sub_1036ffe7` | 8 | trivial accessor/forwarder |
| `0x1036ffef` | `sub_1036ffef` | 27 | support routine (27 bytes) |
| `0x10370010` | `sub_10370010` | 25 | support routine (25 bytes) |
| `0x10370029` | `sub_10370029` | 27 | support routine (27 bytes) |
| `0x10370050` | `sub_10370050` | 8 | trivial accessor/forwarder |
| `0x10370058` | `sub_10370058` | 27 | support routine (27 bytes) |
| `0x10370080` | `sub_10370080` | 11 | trivial accessor/forwarder |
| `0x1037008b` | `sub_1037008b` | 27 | support routine (27 bytes) |
| `0x103700b0` | `sub_103700b0` | 8 | trivial accessor/forwarder |
| `0x103700b8` | `sub_103700b8` | 27 | support routine (27 bytes) |
| `0x103700e0` | `sub_103700e0` | 8 | trivial accessor/forwarder |
| `0x103700e8` | `sub_103700e8` | 27 | support routine (27 bytes) |
| `0x10370110` | `sub_10370110` | 8 | trivial accessor/forwarder |
| `0x10370118` | `sub_10370118` | 27 | support routine (27 bytes) |
| `0x10370140` | `sub_10370140` | 8 | trivial accessor/forwarder |
| `0x10370148` | `sub_10370148` | 11 | trivial accessor/forwarder |
| `0x10370153` | `sub_10370153` | 11 | trivial accessor/forwarder |
| `0x1037015e` | `sub_1037015e` | 30 | support routine (30 bytes) |
| `0x10370180` | `sub_10370180` | 8 | trivial accessor/forwarder |
| `0x10370188` | `sub_10370188` | 27 | support routine (27 bytes) |
| `0x103701b0` | `sub_103701b0` | 8 | trivial accessor/forwarder |
| `0x103701b8` | `sub_103701b8` | 27 | support routine (27 bytes) |
| `0x103701e0` | `sub_103701e0` | 8 | trivial accessor/forwarder |
| `0x103701e8` | `sub_103701e8` | 27 | support routine (27 bytes) |
| `0x10370210` | `sub_10370210` | 8 | trivial accessor/forwarder |
| `0x10370218` | `sub_10370218` | 27 | support routine (27 bytes) |
| `0x10370240` | `sub_10370240` | 8 | trivial accessor/forwarder |
| `0x10370248` | `sub_10370248` | 27 | support routine (27 bytes) |
| `0x10370270` | `sub_10370270` | 8 | trivial accessor/forwarder |
| `0x10370278` | `sub_10370278` | 11 | trivial accessor/forwarder |
| `0x10370283` | `sub_10370283` | 27 | support routine (27 bytes) |
| `0x103702a0` | `sub_103702a0` | 8 | trivial accessor/forwarder |
| `0x103702a8` | `sub_103702a8` | 11 | trivial accessor/forwarder |
| `0x103702b3` | `sub_103702b3` | 27 | support routine (27 bytes) |
| `0x103702d0` | `sub_103702d0` | 8 | trivial accessor/forwarder |
| `0x103702d8` | `sub_103702d8` | 27 | support routine (27 bytes) |
| `0x10370300` | `sub_10370300` | 8 | trivial accessor/forwarder |
| `0x10370308` | `sub_10370308` | 27 | support routine (27 bytes) |
| `0x10370330` | `sub_10370330` | 8 | trivial accessor/forwarder |
| `0x10370338` | `sub_10370338` | 39 | support routine (39 bytes) |
| `0x1037035f` | `sub_1037035f` | 27 | support routine (27 bytes) |
| `0x10370380` | `sub_10370380` | 8 | trivial accessor/forwarder |
| `0x10370388` | `sub_10370388` | 39 | support routine (39 bytes) |
| `0x103703af` | `sub_103703af` | 27 | support routine (27 bytes) |
| `0x103703d0` | `sub_103703d0` | 11 | trivial accessor/forwarder |
| `0x103703db` | `sub_103703db` | 27 | support routine (27 bytes) |
| `0x10370400` | `sub_10370400` | 25 | support routine (25 bytes) |
| `0x10370419` | `sub_10370419` | 27 | support routine (27 bytes) |
| `0x10370440` | `sub_10370440` | 25 | support routine (25 bytes) |
| `0x10370459` | `sub_10370459` | 27 | support routine (27 bytes) |
| `0x10370480` | `sub_10370480` | 25 | support routine (25 bytes) |
| `0x10370499` | `sub_10370499` | 8 | trivial accessor/forwarder |
| `0x103704a1` | `sub_103704a1` | 8 | trivial accessor/forwarder |
| `0x103704a9` | `sub_103704a9` | 37 | support routine (37 bytes) |
| `0x103704d0` | `sub_103704d0` | 8 | trivial accessor/forwarder |
| `0x103704d8` | `sub_103704d8` | 27 | support routine (27 bytes) |
| `0x10370500` | `sub_10370500` | 8 | trivial accessor/forwarder |
| `0x10370508` | `sub_10370508` | 27 | support routine (27 bytes) |
| `0x10370530` | `sub_10370530` | 11 | trivial accessor/forwarder |
| `0x1037053b` | `sub_1037053b` | 11 | trivial accessor/forwarder |
| `0x10370546` | `sub_10370546` | 11 | trivial accessor/forwarder |
| `0x10370551` | `sub_10370551` | 27 | support routine (27 bytes) |
| `0x10370570` | `sub_10370570` | 11 | trivial accessor/forwarder |
| `0x1037057b` | `sub_1037057b` | 27 | support routine (27 bytes) |
| `0x103705a0` | `sub_103705a0` | 8 | trivial accessor/forwarder |
| `0x103705a8` | `sub_103705a8` | 27 | support routine (27 bytes) |
| `0x103705d0` | `sub_103705d0` | 11 | trivial accessor/forwarder |
| `0x103705db` | `sub_103705db` | 11 | trivial accessor/forwarder |
| `0x103705e6` | `sub_103705e6` | 11 | trivial accessor/forwarder |
| `0x103705f1` | `sub_103705f1` | 27 | support routine (27 bytes) |
| `0x10370610` | `sub_10370610` | 8 | trivial accessor/forwarder |
| `0x10370618` | `sub_10370618` | 11 | trivial accessor/forwarder |
| `0x10370623` | `sub_10370623` | 27 | support routine (27 bytes) |
| `0x10370640` | `sub_10370640` | 8 | trivial accessor/forwarder |
| `0x10370648` | `sub_10370648` | 11 | trivial accessor/forwarder |
| `0x10370653` | `sub_10370653` | 27 | support routine (27 bytes) |
| `0x10370670` | `sub_10370670` | 8 | trivial accessor/forwarder |
| `0x10370678` | `sub_10370678` | 40 | support routine (40 bytes) |
| `0x103706a0` | `sub_103706a0` | 11 | trivial accessor/forwarder |
| `0x103706ab` | `sub_103706ab` | 27 | support routine (27 bytes) |
| `0x103706d0` | `sub_103706d0` | 11 | trivial accessor/forwarder |
| `0x103706db` | `sub_103706db` | 11 | trivial accessor/forwarder |
| `0x103706e6` | `sub_103706e6` | 11 | trivial accessor/forwarder |
| `0x103706f1` | `sub_103706f1` | 27 | support routine (27 bytes) |
| `0x10370710` | `sub_10370710` | 11 | trivial accessor/forwarder |
| `0x1037071b` | `sub_1037071b` | 27 | support routine (27 bytes) |
| `0x10370740` | `sub_10370740` | 8 | trivial accessor/forwarder |
| `0x10370748` | `sub_10370748` | 27 | support routine (27 bytes) |
| `0x10370770` | `sub_10370770` | 25 | support routine (25 bytes) |
| `0x10370789` | `sub_10370789` | 25 | support routine (25 bytes) |
| `0x103707a2` | `sub_103707a2` | 27 | support routine (27 bytes) |
| `0x103707c0` | `sub_103707c0` | 8 | trivial accessor/forwarder |
| `0x103707c8` | `sub_103707c8` | 8 | trivial accessor/forwarder |
| `0x103707d0` | `sub_103707d0` | 8 | trivial accessor/forwarder |
| `0x103707d8` | `sub_103707d8` | 30 | support routine (30 bytes) |
| `0x10370800` | `sub_10370800` | 8 | trivial accessor/forwarder |
| `0x10370808` | `sub_10370808` | 27 | support routine (27 bytes) |
| `0x10370830` | `sub_10370830` | 8 | trivial accessor/forwarder |
| `0x10370838` | `sub_10370838` | 27 | support routine (27 bytes) |
| `0x10370860` | `sub_10370860` | 8 | trivial accessor/forwarder |
| `0x10370868` | `sub_10370868` | 27 | support routine (27 bytes) |
| `0x10370890` | `sub_10370890` | 8 | trivial accessor/forwarder |
| `0x10370898` | `sub_10370898` | 27 | support routine (27 bytes) |
| `0x103708c0` | `sub_103708c0` | 8 | trivial accessor/forwarder |
| `0x103708c8` | `sub_103708c8` | 27 | support routine (27 bytes) |
| `0x103708f0` | `sub_103708f0` | 8 | trivial accessor/forwarder |
| `0x103708f8` | `sub_103708f8` | 27 | support routine (27 bytes) |
| `0x10370920` | `sub_10370920` | 8 | trivial accessor/forwarder |
| `0x10370928` | `sub_10370928` | 27 | support routine (27 bytes) |
| `0x10370950` | `sub_10370950` | 8 | trivial accessor/forwarder |
| `0x10370958` | `sub_10370958` | 27 | support routine (27 bytes) |
| `0x10370980` | `sub_10370980` | 8 | trivial accessor/forwarder |
| `0x10370988` | `sub_10370988` | 11 | trivial accessor/forwarder |
| `0x10370993` | `sub_10370993` | 27 | support routine (27 bytes) |
| `0x103709b0` | `sub_103709b0` | 8 | trivial accessor/forwarder |
| `0x103709b8` | `sub_103709b8` | 11 | trivial accessor/forwarder |
| `0x103709c3` | `sub_103709c3` | 27 | support routine (27 bytes) |
| `0x103709e0` | `sub_103709e0` | 8 | trivial accessor/forwarder |
| `0x103709e8` | `sub_103709e8` | 27 | support routine (27 bytes) |
| `0x10370a10` | `sub_10370a10` | 8 | trivial accessor/forwarder |
| `0x10370a18` | `sub_10370a18` | 39 | support routine (39 bytes) |
| `0x10370a3f` | `sub_10370a3f` | 27 | support routine (27 bytes) |
| `0x10370a60` | `sub_10370a60` | 8 | trivial accessor/forwarder |
| `0x10370a68` | `sub_10370a68` | 39 | support routine (39 bytes) |
| `0x10370a8f` | `sub_10370a8f` | 27 | support routine (27 bytes) |
| `0x10370ab0` | `sub_10370ab0` | 11 | trivial accessor/forwarder |
| `0x10370abb` | `sub_10370abb` | 27 | support routine (27 bytes) |
| `0x10370ae0` | `sub_10370ae0` | 8 | trivial accessor/forwarder |
| `0x10370ae8` | `sub_10370ae8` | 40 | support routine (40 bytes) |
| `0x10370b10` | `sub_10370b10` | 8 | trivial accessor/forwarder |
| `0x10370b18` | `sub_10370b18` | 27 | support routine (27 bytes) |
| `0x10370b40` | `sub_10370b40` | 27 | support routine (27 bytes) |
| `0x10370b60` | `sub_10370b60` | 25 | support routine (25 bytes) |
| `0x10370b79` | `sub_10370b79` | 27 | support routine (27 bytes) |
| `0x10370ba0` | `sub_10370ba0` | 25 | support routine (25 bytes) |
| `0x10370bb9` | `sub_10370bb9` | 27 | support routine (27 bytes) |
| `0x10370be0` | `sub_10370be0` | 8 | trivial accessor/forwarder |
| `0x10370be8` | `sub_10370be8` | 27 | support routine (27 bytes) |
| `0x10370c10` | `sub_10370c10` | 8 | trivial accessor/forwarder |
| `0x10370c18` | `sub_10370c18` | 11 | trivial accessor/forwarder |
| `0x10370c23` | `sub_10370c23` | 30 | support routine (30 bytes) |
| `0x10370c50` | `sub_10370c50` | 8 | trivial accessor/forwarder |
| `0x10370c58` | `sub_10370c58` | 27 | support routine (27 bytes) |
| `0x10370c80` | `sub_10370c80` | 8 | trivial accessor/forwarder |
| `0x10370c88` | `sub_10370c88` | 27 | support routine (27 bytes) |
| `0x10370cb0` | `sub_10370cb0` | 8 | trivial accessor/forwarder |
| `0x10370cb8` | `sub_10370cb8` | 27 | support routine (27 bytes) |
| `0x10370ce0` | `sub_10370ce0` | 27 | support routine (27 bytes) |
| `0x10370d00` | `sub_10370d00` | 8 | trivial accessor/forwarder |
| `0x10370d08` | `sub_10370d08` | 11 | trivial accessor/forwarder |
| `0x10370d13` | `sub_10370d13` | 30 | support routine (30 bytes) |
| `0x10370d40` | `sub_10370d40` | 8 | trivial accessor/forwarder |
| `0x10370d48` | `sub_10370d48` | 11 | trivial accessor/forwarder |
| `0x10370d53` | `sub_10370d53` | 30 | support routine (30 bytes) |
| `0x10370d80` | `sub_10370d80` | 27 | support routine (27 bytes) |
| `0x10370da0` | `sub_10370da0` | 8 | trivial accessor/forwarder |
| `0x10370da8` | `sub_10370da8` | 11 | trivial accessor/forwarder |
| `0x10370db3` | `sub_10370db3` | 27 | support routine (27 bytes) |
| `0x10370dd0` | `sub_10370dd0` | 8 | trivial accessor/forwarder |
| `0x10370dd8` | `sub_10370dd8` | 11 | trivial accessor/forwarder |
| `0x10370de3` | `sub_10370de3` | 27 | support routine (27 bytes) |
| `0x10370e00` | `sub_10370e00` | 8 | trivial accessor/forwarder |
| `0x10370e08` | `sub_10370e08` | 27 | support routine (27 bytes) |
| `0x10370e30` | `sub_10370e30` | 11 | trivial accessor/forwarder |
| `0x10370e3b` | `sub_10370e3b` | 44 | support routine (44 bytes) |
| `0x10370e67` | `sub_10370e67` | 27 | support routine (27 bytes) |
| `0x10370e90` | `sub_10370e90` | 8 | trivial accessor/forwarder |
| `0x10370e98` | `sub_10370e98` | 27 | support routine (27 bytes) |
| `0x10370ec0` | `sub_10370ec0` | 11 | trivial accessor/forwarder |
| `0x10370ecb` | `sub_10370ecb` | 27 | support routine (27 bytes) |
| `0x10370ef0` | `sub_10370ef0` | 8 | trivial accessor/forwarder |
| `0x10370ef8` | `sub_10370ef8` | 11 | trivial accessor/forwarder |
| `0x10370f03` | `sub_10370f03` | 27 | support routine (27 bytes) |
| `0x10370f20` | `sub_10370f20` | 8 | trivial accessor/forwarder |
| `0x10370f28` | `sub_10370f28` | 11 | trivial accessor/forwarder |
| `0x10370f33` | `sub_10370f33` | 27 | support routine (27 bytes) |
| `0x10370f50` | `sub_10370f50` | 8 | trivial accessor/forwarder |
| `0x10370f58` | `sub_10370f58` | 39 | support routine (39 bytes) |
| `0x10370f7f` | `sub_10370f7f` | 27 | support routine (27 bytes) |
| `0x10370fa0` | `sub_10370fa0` | 8 | trivial accessor/forwarder |
| `0x10370fa8` | `sub_10370fa8` | 39 | support routine (39 bytes) |
| `0x10370fcf` | `sub_10370fcf` | 27 | support routine (27 bytes) |
| `0x10370ff0` | `sub_10370ff0` | 11 | trivial accessor/forwarder |
| `0x10370ffb` | `sub_10370ffb` | 27 | support routine (27 bytes) |
| `0x10371020` | `sub_10371020` | 28 | support routine (28 bytes) |
| `0x1037103c` | `sub_1037103c` | 8 | trivial accessor/forwarder |
| `0x10371044` | `sub_10371044` | 11 | trivial accessor/forwarder |
| `0x1037104f` | `sub_1037104f` | 27 | support routine (27 bytes) |
| `0x10371070` | `sub_10371070` | 28 | support routine (28 bytes) |
| `0x1037108c` | `sub_1037108c` | 27 | support routine (27 bytes) |
| `0x103710b0` | `sub_103710b0` | 8 | trivial accessor/forwarder |
| `0x103710b8` | `sub_103710b8` | 8 | trivial accessor/forwarder |
| `0x103710c0` | `sub_103710c0` | 27 | support routine (27 bytes) |
| `0x103710e0` | `sub_103710e0` | 8 | trivial accessor/forwarder |
| `0x103710e8` | `sub_103710e8` | 8 | trivial accessor/forwarder |
| `0x103710f0` | `sub_103710f0` | 25 | support routine (25 bytes) |
| `0x10371109` | `sub_10371109` | 27 | support routine (27 bytes) |
| `0x10371130` | `sub_10371130` | 8 | trivial accessor/forwarder |
| `0x10371138` | `sub_10371138` | 25 | support routine (25 bytes) |
| `0x10371151` | `sub_10371151` | 27 | support routine (27 bytes) |
| `0x10371170` | `sub_10371170` | 8 | trivial accessor/forwarder |
| `0x10371178` | `sub_10371178` | 25 | support routine (25 bytes) |
| `0x10371191` | `sub_10371191` | 27 | support routine (27 bytes) |
| `0x103711b0` | `sub_103711b0` | 25 | support routine (25 bytes) |
| `0x103711c9` | `sub_103711c9` | 27 | support routine (27 bytes) |
| `0x103711f0` | `sub_103711f0` | 25 | support routine (25 bytes) |
| `0x10371209` | `sub_10371209` | 27 | support routine (27 bytes) |
| `0x10371230` | `sub_10371230` | 8 | trivial accessor/forwarder |
| `0x10371238` | `sub_10371238` | 27 | support routine (27 bytes) |
| `0x10371260` | `sub_10371260` | 8 | trivial accessor/forwarder |
| `0x10371268` | `sub_10371268` | 8 | trivial accessor/forwarder |
| `0x10371270` | `sub_10371270` | 27 | support routine (27 bytes) |
| `0x10371290` | `sub_10371290` | 8 | trivial accessor/forwarder |
| `0x10371298` | `sub_10371298` | 27 | support routine (27 bytes) |
| `0x103712c0` | `sub_103712c0` | 11 | trivial accessor/forwarder |
| `0x103712cb` | `sub_103712cb` | 27 | support routine (27 bytes) |
| `0x103712f0` | `sub_103712f0` | 11 | trivial accessor/forwarder |
| `0x103712fb` | `sub_103712fb` | 11 | trivial accessor/forwarder |
| `0x10371306` | `sub_10371306` | 40 | support routine (40 bytes) |
| `0x10371330` | `sub_10371330` | 8 | trivial accessor/forwarder |
| `0x10371338` | `sub_10371338` | 8 | trivial accessor/forwarder |
| `0x10371340` | `sub_10371340` | 8 | trivial accessor/forwarder |
| `0x10371348` | `sub_10371348` | 8 | trivial accessor/forwarder |
| `0x10371350` | `sub_10371350` | 40 | support routine (40 bytes) |
| `0x10371380` | `sub_10371380` | 8 | trivial accessor/forwarder |
| `0x10371388` | `sub_10371388` | 27 | support routine (27 bytes) |
| `0x103713b0` | `sub_103713b0` | 8 | trivial accessor/forwarder |
| `0x103713b8` | `sub_103713b8` | 8 | trivial accessor/forwarder |
| `0x103713c0` | `sub_103713c0` | 8 | trivial accessor/forwarder |
| `0x103713c8` | `sub_103713c8` | 40 | support routine (40 bytes) |
| `0x103713f0` | `sub_103713f0` | 8 | trivial accessor/forwarder |
| `0x103713f8` | `sub_103713f8` | 8 | trivial accessor/forwarder |
| `0x10371400` | `sub_10371400` | 40 | support routine (40 bytes) |
| `0x10371430` | `sub_10371430` | 8 | trivial accessor/forwarder |
| `0x10371438` | `sub_10371438` | 8 | trivial accessor/forwarder |
| `0x10371440` | `sub_10371440` | 27 | support routine (27 bytes) |
| `0x10371460` | `sub_10371460` | 3 | trivial accessor/forwarder |
| `0x10371463` | `sub_10371463` | 14 | trivial accessor/forwarder |
| `0x10371471` | `sub_10371471` | 27 | support routine (27 bytes) |
| `0x10371490` | `sub_10371490` | 8 | trivial accessor/forwarder |
| `0x10371498` | `sub_10371498` | 27 | support routine (27 bytes) |
| `0x103714c0` | `sub_103714c0` | 8 | trivial accessor/forwarder |
| `0x103714c8` | `sub_103714c8` | 8 | trivial accessor/forwarder |
| `0x103714d0` | `sub_103714d0` | 27 | support routine (27 bytes) |
| `0x103714f0` | `sub_103714f0` | 8 | trivial accessor/forwarder |
| `0x103714f8` | `sub_103714f8` | 11 | trivial accessor/forwarder |
| `0x10371503` | `sub_10371503` | 27 | support routine (27 bytes) |
| `0x10371520` | `sub_10371520` | 8 | trivial accessor/forwarder |
| `0x10371528` | `sub_10371528` | 11 | trivial accessor/forwarder |
| `0x10371533` | `sub_10371533` | 27 | support routine (27 bytes) |
| `0x10371550` | `sub_10371550` | 11 | trivial accessor/forwarder |
| `0x1037155b` | `sub_1037155b` | 27 | support routine (27 bytes) |
| `0x10371580` | `sub_10371580` | 27 | support routine (27 bytes) |
| `0x103715a0` | `sub_103715a0` | 11 | trivial accessor/forwarder |
| `0x103715ab` | `sub_103715ab` | 27 | support routine (27 bytes) |
| `0x103715d0` | `sub_103715d0` | 8 | trivial accessor/forwarder |
| `0x103715d8` | `sub_103715d8` | 27 | support routine (27 bytes) |
| `0x10371600` | `sub_10371600` | 8 | trivial accessor/forwarder |
| `0x10371608` | `sub_10371608` | 27 | support routine (27 bytes) |
| `0x1037170a` | `sub_1037170a` | 27 | support routine (27 bytes) |
| `0x10371730` | `sub_10371730` | 11 | trivial accessor/forwarder |
| `0x1037173b` | `sub_1037173b` | 46 | support routine (46 bytes) |
| `0x10371770` | `sub_10371770` | 11 | trivial accessor/forwarder |
| `0x1037177b` | `sub_1037177b` | 46 | support routine (46 bytes) |
| `0x103717b0` | `sub_103717b0` | 14 | trivial accessor/forwarder |
| `0x103717be` | `sub_103717be` | 26 | support routine (26 bytes) |
| `0x103717e0` | `sub_103717e0` | 14 | trivial accessor/forwarder |
| `0x103717ee` | `sub_103717ee` | 26 | support routine (26 bytes) |
| `0x10371810` | `sub_10371810` | 14 | trivial accessor/forwarder |
| `0x1037181e` | `sub_1037181e` | 27 | support routine (27 bytes) |
| `0x10371840` | `sub_10371840` | 14 | trivial accessor/forwarder |
| `0x1037184e` | `sub_1037184e` | 25 | support routine (25 bytes) |
| `0x10371867` | `sub_10371867` | 25 | support routine (25 bytes) |
| `0x10371880` | `sub_10371880` | 27 | support routine (27 bytes) |
| `0x103718a0` | `sub_103718a0` | 25 | support routine (25 bytes) |
| `0x103718b9` | `sub_103718b9` | 8 | trivial accessor/forwarder |
| `0x103718c1` | `sub_103718c1` | 40 | support routine (40 bytes) |
| `0x103718f0` | `sub_103718f0` | 8 | trivial accessor/forwarder |
| `0x103718f8` | `sub_103718f8` | 8 | trivial accessor/forwarder |
| `0x10371900` | `sub_10371900` | 27 | support routine (27 bytes) |
| `0x10371920` | `sub_10371920` | 8 | trivial accessor/forwarder |
| `0x10371928` | `sub_10371928` | 27 | support routine (27 bytes) |
| `0x10371950` | `sub_10371950` | 15 | trivial accessor/forwarder |
| `0x10371960` | `sub_10371960` | 15 | trivial accessor/forwarder |
| `0x10371970` | `sub_10371970` | 15 | trivial accessor/forwarder |
| `0x10371980` | `sub_10371980` | 15 | trivial accessor/forwarder |
| `0x10371990` | `sub_10371990` | 15 | trivial accessor/forwarder |
| `0x103719a0` | `sub_103719a0` | 15 | trivial accessor/forwarder |
| `0x103719b0` | `sub_103719b0` | 15 | trivial accessor/forwarder |
| `0x103719c0` | `sub_103719c0` | 15 | trivial accessor/forwarder |
| `0x103719d0` | `sub_103719d0` | 15 | trivial accessor/forwarder |
| `0x103719e0` | `sub_103719e0` | 15 | trivial accessor/forwarder |
| `0x103719f0` | `sub_103719f0` | 15 | trivial accessor/forwarder |
| `0x10371a00` | `sub_10371a00` | 15 | trivial accessor/forwarder |
| `0x10371a10` | `sub_10371a10` | 15 | trivial accessor/forwarder |
| `0x10371a20` | `sub_10371a20` | 15 | trivial accessor/forwarder |
| `0x10371a30` | `sub_10371a30` | 17 | support routine (17 bytes) |
| `0x10371a50` | `sub_10371a50` | 17 | support routine (17 bytes) |
| `0x10371a70` | `sub_10371a70` | 17 | support routine (17 bytes) |
| `0x10371a90` | `sub_10371a90` | 17 | support routine (17 bytes) |
| `0x10371ab0` | `sub_10371ab0` | 15 | trivial accessor/forwarder |
| `0x10371ac0` | `sub_10371ac0` | 15 | trivial accessor/forwarder |
| `0x10371ad0` | `sub_10371ad0` | 15 | trivial accessor/forwarder |
| `0x10371ae0` | `sub_10371ae0` | 15 | trivial accessor/forwarder |
| `0x10371af0` | `sub_10371af0` | 15 | trivial accessor/forwarder |
| `0x10371b00` | `sub_10371b00` | 15 | trivial accessor/forwarder |
| `0x10371b10` | `sub_10371b10` | 15 | trivial accessor/forwarder |
| `0x10371b20` | `sub_10371b20` | 15 | trivial accessor/forwarder |
| `0x10371b30` | `sub_10371b30` | 15 | trivial accessor/forwarder |
| `0x10371b40` | `sub_10371b40` | 15 | trivial accessor/forwarder |
| `0x10371b50` | `sub_10371b50` | 15 | trivial accessor/forwarder |
| `0x10371b60` | `sub_10371b60` | 15 | trivial accessor/forwarder |
| `0x10371b70` | `sub_10371b70` | 15 | trivial accessor/forwarder |
| `0x10371b80` | `sub_10371b80` | 15 | trivial accessor/forwarder |
| `0x10371b90` | `sub_10371b90` | 5717 | support routine (5717 bytes) |
| `0x103731f0` | `sub_103731f0` | 15 | trivial accessor/forwarder |
| `0x10373200` | `sub_10373200` | 15 | trivial accessor/forwarder |
| `0x10373210` | `sub_10373210` | 15 | trivial accessor/forwarder |
| `0x10373220` | `sub_10373220` | 15 | trivial accessor/forwarder |
| `0x10373230` | `sub_10373230` | 15 | trivial accessor/forwarder |
| `0x10373240` | `sub_10373240` | 15 | trivial accessor/forwarder |
| `0x10373250` | `sub_10373250` | 15 | trivial accessor/forwarder |
| `0x10373260` | `sub_10373260` | 15 | trivial accessor/forwarder |
| `0x10373270` | `sub_10373270` | 15 | trivial accessor/forwarder |
| `0x10373280` | `sub_10373280` | 15 | trivial accessor/forwarder |
| `0x10373290` | `sub_10373290` | 15 | trivial accessor/forwarder |
| `0x103732a0` | `sub_103732a0` | 15 | trivial accessor/forwarder |
| `0x103732b0` | `sub_103732b0` | 15 | trivial accessor/forwarder |
| `0x103732c0` | `sub_103732c0` | 15 | trivial accessor/forwarder |
| `0x103732d0` | `sub_103732d0` | 15 | trivial accessor/forwarder |
| `0x103732e0` | `sub_103732e0` | 15 | trivial accessor/forwarder |
| `0x103732f0` | `sub_103732f0` | 15 | trivial accessor/forwarder |
| `0x10373300` | `sub_10373300` | 15 | trivial accessor/forwarder |
| `0x10373310` | `sub_10373310` | 15 | trivial accessor/forwarder |
| `0x10373320` | `sub_10373320` | 15 | trivial accessor/forwarder |
| `0x10373330` | `sub_10373330` | 15 | trivial accessor/forwarder |
| `0x10373340` | `sub_10373340` | 15 | trivial accessor/forwarder |
| `0x10373350` | `sub_10373350` | 15 | trivial accessor/forwarder |
| `0x10373360` | `sub_10373360` | 15 | trivial accessor/forwarder |
| `0x10373370` | `sub_10373370` | 15 | trivial accessor/forwarder |
| `0x10373380` | `sub_10373380` | 15 | trivial accessor/forwarder |
| `0x10373390` | `sub_10373390` | 15 | trivial accessor/forwarder |
| `0x103733a0` | `sub_103733a0` | 15 | trivial accessor/forwarder |
| `0x103733b0` | `sub_103733b0` | 15 | trivial accessor/forwarder |
| `0x103733c0` | `sub_103733c0` | 17 | support routine (17 bytes) |
| `0x103733e0` | `sub_103733e0` | 15 | trivial accessor/forwarder |
| `0x103733f0` | `sub_103733f0` | 15 | trivial accessor/forwarder |
| `0x10373400` | `sub_10373400` | 15 | trivial accessor/forwarder |
| `0x10373410` | `sub_10373410` | 15 | trivial accessor/forwarder |
| `0x10373420` | `sub_10373420` | 15 | trivial accessor/forwarder |
| `0x10373430` | `sub_10373430` | 15 | trivial accessor/forwarder |
| `0x10373440` | `sub_10373440` | 15 | trivial accessor/forwarder |
| `0x10373450` | `sub_10373450` | 15 | trivial accessor/forwarder |
| `0x10373460` | `sub_10373460` | 15 | trivial accessor/forwarder |
| `0x10373470` | `sub_10373470` | 15 | trivial accessor/forwarder |
| `0x10373480` | `sub_10373480` | 15 | trivial accessor/forwarder |
| `0x10373490` | `sub_10373490` | 15 | trivial accessor/forwarder |
| `0x103734a0` | `sub_103734a0` | 15 | trivial accessor/forwarder |
| `0x103734b0` | `sub_103734b0` | 15 | trivial accessor/forwarder |
| `0x103734c0` | `sub_103734c0` | 33 | support routine (33 bytes) |
| `0x103734f0` | `sub_103734f0` | 15 | trivial accessor/forwarder |
| `0x10373500` | `sub_10373500` | 15 | trivial accessor/forwarder |
| `0x10373510` | `sub_10373510` | 15 | trivial accessor/forwarder |
| `0x10373520` | `sub_10373520` | 15 | trivial accessor/forwarder |
| `0x10373530` | `sub_10373530` | 15 | trivial accessor/forwarder |
| `0x10373540` | `sub_10373540` | 15 | trivial accessor/forwarder |
| `0x10373550` | `sub_10373550` | 15 | trivial accessor/forwarder |
| `0x10373560` | `sub_10373560` | 15 | trivial accessor/forwarder |
| `0x10373570` | `sub_10373570` | 15 | trivial accessor/forwarder |
| `0x10373580` | `sub_10373580` | 15 | trivial accessor/forwarder |
| `0x10373590` | `sub_10373590` | 15 | trivial accessor/forwarder |
| `0x103735a0` | `sub_103735a0` | 15 | trivial accessor/forwarder |
| `0x103735b0` | `sub_103735b0` | 15 | trivial accessor/forwarder |
| `0x103735c0` | `sub_103735c0` | 15 | trivial accessor/forwarder |
| `0x103735d0` | `sub_103735d0` | 15 | trivial accessor/forwarder |
| `0x103735e0` | `sub_103735e0` | 15 | trivial accessor/forwarder |
| `0x103735f0` | `sub_103735f0` | 15 | trivial accessor/forwarder |
| `0x10373600` | `sub_10373600` | 15 | trivial accessor/forwarder |
| `0x10373610` | `sub_10373610` | 15 | trivial accessor/forwarder |
| `0x10373620` | `sub_10373620` | 15 | trivial accessor/forwarder |
| `0x10373630` | `sub_10373630` | 15 | trivial accessor/forwarder |
| `0x10373640` | `sub_10373640` | 15 | trivial accessor/forwarder |
| `0x10373650` | `sub_10373650` | 15 | trivial accessor/forwarder |
| `0x10373660` | `sub_10373660` | 15 | trivial accessor/forwarder |
| `0x10373670` | `sub_10373670` | 15 | trivial accessor/forwarder |
| `0x10373680` | `sub_10373680` | 15 | trivial accessor/forwarder |
| `0x10373690` | `sub_10373690` | 15 | trivial accessor/forwarder |
| `0x103736a0` | `sub_103736a0` | 15 | trivial accessor/forwarder |
| `0x103736b0` | `sub_103736b0` | 15 | trivial accessor/forwarder |
| `0x103736c0` | `sub_103736c0` | 15 | trivial accessor/forwarder |
| `0x103736d0` | `sub_103736d0` | 15 | trivial accessor/forwarder |
| `0x103736e0` | `sub_103736e0` | 15 | trivial accessor/forwarder |
| `0x103736f0` | `sub_103736f0` | 15 | trivial accessor/forwarder |
| `0x10373700` | `sub_10373700` | 15 | trivial accessor/forwarder |
| `0x10373710` | `sub_10373710` | 15 | trivial accessor/forwarder |
| `0x10373720` | `sub_10373720` | 15 | trivial accessor/forwarder |
| `0x10373730` | `sub_10373730` | 15 | trivial accessor/forwarder |
| `0x10373740` | `sub_10373740` | 15 | trivial accessor/forwarder |
| `0x10373750` | `sub_10373750` | 15 | trivial accessor/forwarder |
| `0x10373760` | `sub_10373760` | 15 | trivial accessor/forwarder |
| `0x10373770` | `sub_10373770` | 15 | trivial accessor/forwarder |
| `0x10373780` | `sub_10373780` | 15 | trivial accessor/forwarder |
| `0x10373790` | `sub_10373790` | 15 | trivial accessor/forwarder |
| `0x103737a0` | `sub_103737a0` | 15 | trivial accessor/forwarder |
| `0x103737b0` | `sub_103737b0` | 15 | trivial accessor/forwarder |
| `0x103737c0` | `sub_103737c0` | 15 | trivial accessor/forwarder |
| `0x103737d0` | `sub_103737d0` | 15 | trivial accessor/forwarder |
| `0x103737e0` | `sub_103737e0` | 15 | trivial accessor/forwarder |
| `0x103737f0` | `sub_103737f0` | 15 | trivial accessor/forwarder |
| `0x10373800` | `sub_10373800` | 15 | trivial accessor/forwarder |
| `0x10373810` | `sub_10373810` | 15 | trivial accessor/forwarder |
| `0x10373820` | `sub_10373820` | 15 | trivial accessor/forwarder |
| `0x10373830` | `sub_10373830` | 15 | trivial accessor/forwarder |
| `0x10373840` | `sub_10373840` | 15 | trivial accessor/forwarder |
| `0x10373850` | `sub_10373850` | 15 | trivial accessor/forwarder |
| `0x10373860` | `sub_10373860` | 15 | trivial accessor/forwarder |
| `0x10373870` | `sub_10373870` | 21 | support routine (21 bytes) |
| `0x10373890` | `sub_10373890` | 15 | trivial accessor/forwarder |
| `0x103738a0` | `sub_103738a0` | 15 | trivial accessor/forwarder |
| `0x103738b0` | `sub_103738b0` | 15 | trivial accessor/forwarder |
| `0x103738c0` | `sub_103738c0` | 15 | trivial accessor/forwarder |
| `0x103738d0` | `sub_103738d0` | 15 | trivial accessor/forwarder |
| `0x103738e0` | `sub_103738e0` | 15 | trivial accessor/forwarder |
| `0x103738f0` | `sub_103738f0` | 15 | trivial accessor/forwarder |
| `0x10373900` | `sub_10373900` | 15 | trivial accessor/forwarder |
| `0x10373910` | `sub_10373910` | 15 | trivial accessor/forwarder |
| `0x10373920` | `sub_10373920` | 15 | trivial accessor/forwarder |
| `0x10373930` | `sub_10373930` | 15 | trivial accessor/forwarder |
| `0x10373940` | `sub_10373940` | 15 | trivial accessor/forwarder |
| `0x10373950` | `sub_10373950` | 15 | trivial accessor/forwarder |
| `0x10373960` | `sub_10373960` | 15 | trivial accessor/forwarder |
| `0x10373970` | `sub_10373970` | 30 | support routine (30 bytes) |
| `0x10373990` | `sub_10373990` | 33 | support routine (33 bytes) |
| `0x103739c0` | `sub_103739c0` | 33 | support routine (33 bytes) |
| `0x103739f0` | `sub_103739f0` | 33 | support routine (33 bytes) |
| `0x10373a20` | `sub_10373a20` | 28 | support routine (28 bytes) |
| `0x10373a40` | `sub_10373a40` | 20 | support routine (20 bytes) |
| `0x10373a60` | `sub_10373a60` | 108 | support routine (108 bytes) |
| `0x10373ad0` | `sub_10373ad0` | 15 | trivial accessor/forwarder |
| `0x10373ae0` | `sub_10373ae0` | 15 | trivial accessor/forwarder |
| `0x10373af0` | `sub_10373af0` | 15 | trivial accessor/forwarder |
| `0x10373b00` | `sub_10373b00` | 15 | trivial accessor/forwarder |
| `0x10373b10` | `sub_10373b10` | 15 | trivial accessor/forwarder |
| `0x10373b20` | `sub_10373b20` | 15 | trivial accessor/forwarder |
| `0x10373b30` | `sub_10373b30` | 15 | trivial accessor/forwarder |
| `0x10373b40` | `sub_10373b40` | 15 | trivial accessor/forwarder |
| `0x10373b50` | `sub_10373b50` | 15 | trivial accessor/forwarder |
| `0x10373b60` | `sub_10373b60` | 15 | trivial accessor/forwarder |
| `0x10373b70` | `sub_10373b70` | 15 | trivial accessor/forwarder |
| `0x10373b80` | `sub_10373b80` | 15 | trivial accessor/forwarder |
| `0x10373b90` | `sub_10373b90` | 15 | trivial accessor/forwarder |
| `0x10373ba0` | `sub_10373ba0` | 15 | trivial accessor/forwarder |
| `0x10373bb0` | `sub_10373bb0` | 15 | trivial accessor/forwarder |
| `0x10373bc0` | `sub_10373bc0` | 15 | trivial accessor/forwarder |
| `0x10373bd0` | `sub_10373bd0` | 15 | trivial accessor/forwarder |
| `0x10373be0` | `sub_10373be0` | 15 | trivial accessor/forwarder |
| `0x10373bf0` | `sub_10373bf0` | 15 | trivial accessor/forwarder |
| `0x10373c00` | `sub_10373c00` | 15 | trivial accessor/forwarder |
| `0x10373c10` | `sub_10373c10` | 15 | trivial accessor/forwarder |
| `0x10373c20` | `sub_10373c20` | 15 | trivial accessor/forwarder |
| `0x10373c30` | `sub_10373c30` | 15 | trivial accessor/forwarder |
| `0x10373c40` | `sub_10373c40` | 15 | trivial accessor/forwarder |
| `0x10373c50` | `sub_10373c50` | 15 | trivial accessor/forwarder |
| `0x10373c60` | `sub_10373c60` | 15 | trivial accessor/forwarder |
| `0x10373c70` | `sub_10373c70` | 15 | trivial accessor/forwarder |
| `0x10373c80` | `sub_10373c80` | 15 | trivial accessor/forwarder |
| `0x10373c8f` | `sub_10373c8f` | 22 | support routine (22 bytes) |
| `0x10373ca5` | `sub_10373ca5` | 12 | trivial accessor/forwarder |
| `0x10373cb1` | `sub_10373cb1` | 22 | support routine (22 bytes) |
| `0x10373cc7` | `sub_10373cc7` | 12 | trivial accessor/forwarder |
| `0x10373ce0` | `sub_10373ce0` | 11 | trivial accessor/forwarder |
| `0x10373cf0` | `sub_10373cf0` | 11 | trivial accessor/forwarder |
| `0x10373d00` | `sub_10373d00` | 11 | trivial accessor/forwarder |
| `0x10373d10` | `sub_10373d10` | 11 | trivial accessor/forwarder |
| `0x10373d20` | `sub_10373d20` | 11 | trivial accessor/forwarder |
| `0x10373d30` | `sub_10373d30` | 11 | trivial accessor/forwarder |
| `0x10373d40` | `sub_10373d40` | 11 | trivial accessor/forwarder |
| `0x10373d50` | `sub_10373d50` | 11 | trivial accessor/forwarder |
| `0x10373d60` | `sub_10373d60` | 11 | trivial accessor/forwarder |
| `0x10373d70` | `sub_10373d70` | 11 | trivial accessor/forwarder |
| `0x10373d80` | `sub_10373d80` | 11 | trivial accessor/forwarder |
| `0x10373d90` | `sub_10373d90` | 11 | trivial accessor/forwarder |
| `0x10373da0` | `sub_10373da0` | 11 | trivial accessor/forwarder |
| `0x10373db0` | `sub_10373db0` | 15 | trivial accessor/forwarder |
| `0x10373dc0` | `sub_10373dc0` | 15 | trivial accessor/forwarder |
| `0x10373dd0` | `sub_10373dd0` | 15 | trivial accessor/forwarder |
| `0x10373de0` | `sub_10373de0` | 15 | trivial accessor/forwarder |
| `0x10373df0` | `sub_10373df0` | 15 | trivial accessor/forwarder |
| `0x10373e00` | `sub_10373e00` | 15 | trivial accessor/forwarder |
| `0x10373e10` | `sub_10373e10` | 15 | trivial accessor/forwarder |
| `0x10373e1f` | `sub_10373e1f` | 10 | trivial accessor/forwarder |
| `0x10373e29` | `sub_10373e29` | 10 | trivial accessor/forwarder |
| `0x10373e33` | `sub_10373e33` | 10 | trivial accessor/forwarder |
| `0x10373e3d` | `sub_10373e3d` | 10 | trivial accessor/forwarder |
| `0x10373e47` | `sub_10373e47` | 20 | support routine (20 bytes) |
| `0x10373e60` | `sub_10373e60` | 11 | trivial accessor/forwarder |
| `0x10373e70` | `sub_10373e70` | 11 | trivial accessor/forwarder |
| `0x10373e80` | `sub_10373e80` | 46 | support routine (46 bytes) |
| `0x10373eb0` | `sub_10373eb0` | 46 | support routine (46 bytes) |
| `0x1037b000` | `sub_1037b000` | 49157 | support routine (49157 bytes) |
