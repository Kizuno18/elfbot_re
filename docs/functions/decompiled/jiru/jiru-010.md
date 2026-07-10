# elfbot.dll decompiled — jiru 0x102fd980..0x102ff110

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_102fd980` `0x102fd980`

_206 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7d8;
extern unsigned int g_1038c7dc;

unsigned int sub_102fd980(int a0)
{
    unsigned int v5;  // ebx
    unsigned int v6;  // ecx
    unsigned int v8;  // ecx
    unsigned int v9;  // ecx
    unsigned int v10;  // eax
    unsigned int v12;  // eax
    unsigned int v13;  // eax
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v3 = sub_102eed50(a0);
    v1 = v5;
    v0 = v6;
    v8 = _INSERT(_INSERT(v6, 1, 0), 0, 101);
    v9 = v8 * 0x1000000 | v8 * 0x100 & 0xff0000 | v8 >> 8 & 0xff00 | v8 >> 24 & 0xff;
    v10 = _INSERT(_INSERT(v3 & 0xffff, 1, 0) & 0xff, 0, ~(~((char)_INSERT(v3 & 0xffff, 1, 0))));
    v12 = v10 * 0x1000000 | v10 * 0x100 & 0xff0000 | v10 >> 8 & 0xff00 | v10 >> 24 & 0xff;
    v13 = _INSERT((char)v12 * 0 | (char)(v12 >> 24), 0, ((char)v12 * 0 | (char)(v12 >> 24)) & (char)~(~(_INSERT((char)v9 * 0 | (char)(v9 >> 24), 0, ((char)v9 * 0 | (char)(v9 >> 24)) - 39))) + 3);
    v2 = -(0 < v13) + 1;
    v4 = (g_1038c7d8 ^ g_1038c7dc) * 2;
    if (v2)
        v4 |= 1;
    return sub_102eebb0(v4);
}
```

## `sub_102fda50` `0x102fda50`

_390 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7f4;
extern unsigned int g_1038c7f8;

unsigned int sub_102fda50(int a0)
{
    unsigned int v7;  // edx
    unsigned int v8;  // ebx
    unsigned int v17;  // eax
    unsigned int v18;  // eax
    unsigned short v19;  // ax
    unsigned int v20;  // cc_dep1
    char v21;  // bl
    unsigned int v22;  // 4376
    unsigned int v23;  // 4142
    unsigned int v24;  // 4144
    unsigned int v25;  // cc_ndep
    unsigned int v26;  // cc_dep1
    unsigned int v27;  // 4146
    unsigned int v30;  // eax
    unsigned int v31;  // 4211
    unsigned int v32;  // eax
    unsigned int v35;  // 4212
    unsigned int v10;  // eax
    unsigned int v38;  // 4119
    unsigned int v39;  // eax
    unsigned int v42;  // 4120
    unsigned int v45;  // 4135
    unsigned int v46;  // eax
    unsigned short v11;  // bx
    unsigned int v47;  // cc_ndep
    unsigned int v48;  // cc_dep1
    unsigned int v49;  // 4136
    unsigned int v52;  // eax
    unsigned int v12;  // eax
    unsigned int v13;  // eax
    unsigned int v15;  // eax
    unsigned short v16;  // bx
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v5 = sub_102efd90(a0);
    v3 = v7;
    v2 = v8;
    v1 = v5 & 0xffff;
    v10 = _INSERT(v1, 1, 0);
    v11 = _INSERT(_INSERT(*((unsigned short *)((void*)&v8 + 1)), 1, 0), 0, 64);
    v12 = v10 * 0x1000000 | v10 * 0x100 & 0xff0000 | v10 >> 8 & 0xff00 | v10 >> 24 & 0xff;
    v13 = _INSERT((char)v12 * 0 | (char)(v12 >> 24), 0, ((char)v12 * 0 | (char)(v12 >> 24)) & (char)~(~(v11)));
    if (!v13)
    {
        v3 = v7;
        v1 = v5 & 0xffff;
        v15 = _INSERT(v1, 1, 0);
        v16 = _INSERT(_INSERT(*((unsigned short *)((void*)&v2 + 1)), 1, 0), 0, 128);
        v17 = v15 * 0x1000000 | v15 * 0x100 & 0xff0000 | v15 >> 8 & 0xff00 | v15 >> 24 & 0xff;
        v18 = _INSERT((char)v17 * 0 | (char)(v17 >> 24), 0, ((char)v17 * 0 | (char)(v17 >> 24)) & (char)~(~(v16)));
        v3 = -(0 < v18) + 1;
        v19 = v5;
        v2 = v7;
        v20 = v19;
        v1 = v2;
        v0 = 31;
        v21 = v0;
        v22 = _ccall(0, 15, (unsigned int)v19, 0, 0);
        v0 = v19;
        v23 = _ccall(19, (unsigned int)(v21 - 6), 0, (unsigned int)(char)(v21 < 5));
        v24 = _ccall(19, (unsigned int)(v21 - 7), 0, v23);
        v25 = v24;
        v26 = v21 - 8;
        v27 = _ccall(0, 19, (unsigned int)(v21 - 8), 0, v24);
        v30 = _INSERT((char)v0 & v21 - 31, 1, (char)v0 & v21 - 31 & 246);
        v31 = _ccall(12, 0, (unsigned int)(char)(0 < v30), (unsigned int)(char)(0 < v30));
        v32 = -(0 < v30) + 1;
        v35 = _ccall(0, 21, v32 - 1, 0, v31);
        v38 = _ccall(21, v32 - 1, 0, v31);
        v39 = v32;
        v42 = _ccall(0, 21, v39 - 1, 0, v38);
        v45 = _ccall(21, v39 - 1, 0, v38);
        v46 = v39;
        v47 = v45;
        v48 = v46 - 1;
        v49 = _ccall(0, 21, v46 - 1, 0, v45);
        if (-(0 < v18) + 1 != v46)
            goto LABEL_102fdba8;
        v52 = 0;
    }
    else
    {
LABEL_102fdba8:
        v52 = 1;
    }
    v4 = v52;
    v6 = (g_1038c7f4 ^ g_1038c7f8) * 2;
    if (v4)
        v6 |= 1;
    return sub_102efcf0(v6);
}
```

## `sub_102fdb2d` `0x102fdb2d`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fdb2d(void)
{
}
```

## `sub_102fdb44` `0x102fdb44`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fdb44(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fdb78` `0x102fdb78`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fdb78(void)
{
}
```

## `sub_102fdb87` `0x102fdb87`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fdb87(void)
{
}
```

## `sub_102fdbf0` `0x102fdbf0`

_191 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7ec;
extern unsigned int g_1038c7f0;

int sub_102fdbf0(unsigned int a0)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // ecx
    unsigned int v10;  // ecx
    unsigned int v11;  // eax
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102ef8d0(a0);
    v2 = v6;
    v1 = v7;
    v0 = _INSERT(v4 & 0xffff, 1, 0);
    v10 = _INSERT(_INSERT(v7, 1, 0), 0, 65);
    v11 = _INSERT(v0, 0, (char)v0 & (char)~(~(v10)));
    v3 = -(-(0 < v11));
    v5 = (g_1038c7ec ^ g_1038c7f0) * 2;
    if (v3)
        v5 |= 1;
    return sub_102ef750(v5);
}
```

## `sub_102fdcb0` `0x102fdcb0`

_197 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c820;
extern unsigned int g_1038c824;

unsigned int sub_102fdcb0(int a0)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // ecx
    unsigned int v10;  // ecx
    unsigned int v11;  // eax
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f1390(a0);
    v2 = v6;
    v1 = v7;
    v0 = _INSERT(v4 & 0xffff, 1, 0);
    v10 = _INSERT(_INSERT(v7, 1, 0), 0, 65);
    v11 = _INSERT(v0, 0, (char)v0 & (char)~(~(v10)));
    v3 = -(-(0 < v11));
    v5 = (g_1038c820 ^ g_1038c824) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f1250(v5);
}
```

## `sub_102fdd80` `0x102fdd80`

_131 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c828;
extern unsigned int g_1038c82c;

unsigned int sub_102fdd80(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v7;  // ebx
    unsigned int v8;  // esi
    unsigned int v9;  // edi
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v4 = v7;
    v3 = v8;
    v2 = v9;
    v1 = v7;
    v0 = a0;
    v5 = (!a3 && 1 ? 1 : 0);
    v6 = (g_1038c828 ^ g_1038c82c) * 2;
    if (v5)
        v6 |= 1;
    return sub_102f1810(v6);
}
```

## `sub_102fde10` `0x102fde10`

_126 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c830;
extern unsigned int g_1038c834;

int sub_102fde10(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v7;  // ebx
    unsigned int v8;  // esi
    unsigned int v9;  // edi
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v4 = v7;
    v3 = v8;
    v2 = v9;
    v1 = v7;
    v0 = a0;
    v5 = (!a3 && 1 ? 1 : 0);
    v6 = (g_1038c830 ^ g_1038c834) * 2;
    if (v5)
        v6 |= 1;
    return sub_102f1d10(v6);
}
```

## `sub_102fde90` `0x102fde90`

_180 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c800;
extern unsigned int g_1038c804;

int sub_102fde90(unsigned int a0)
{
    unsigned short v7;  // ax
    unsigned int v8;  // edx
    unsigned int v9;  // cc_dep1
    unsigned int v10;  // ebx
    unsigned int v11;  // 4130
    unsigned int v12;  // 4282
    unsigned int v13;  // 4284
    unsigned int v14;  // 4286
    unsigned int v15;  // 4288
    unsigned int v16;  // cc_ndep
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v5 = sub_102f04d0(a0);
    v7 = v5;
    v3 = v8;
    v9 = v7;
    v2 = v10;
    v0 = 0xd00;
    v11 = _ccall(0, 15, (unsigned int)v7, 0, 0);
    v1 = v7;
    v12 = _ccall(19, 4, 0, 0);
    v13 = _ccall(19, 3, 0, v12);
    v14 = _ccall(16, 4, 0, v13);
    v15 = _ccall(19, 3, 0, v14);
    v16 = v15;
    v4 = -(0 < _INSERT(_INSERT(v1, 1, *((char *)((void*)&v1 + 1)) & (char)v0 - 13) & 0xff, 0, (char)_INSERT(v1, 1, *((char *)((void*)&v1 + 1)) & (char)v0 - 13) & 4)) + 1;
    v6 = (g_1038c800 ^ g_1038c804) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f0430(v6);
}
```

## `sub_102fdebf` `0x102fdebf`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fdebf(void)
{
}
```

## `sub_102fdf05` `0x102fdf05`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fdf05(void)
{
}
```

## `sub_102fdf50` `0x102fdf50`

_223 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c838;
extern unsigned int g_1038c83c;

int sub_102fdf50(unsigned int a0)
{
    unsigned int v6;  // edx
    char v7;  // al
    int v17;  // cc_dep1
    unsigned int v18;  // 4125
    unsigned int v19;  // eax
    unsigned int v20;  // 4108
    unsigned int v21;  // cc_dep1
    unsigned int v22;  // 4108
    unsigned int v23;  // 4133
    unsigned int v24;  // 4134
    unsigned int v25;  // eax
    unsigned int v8;  // ebx
    unsigned int v28;  // 4135
    unsigned int v31;  // 4119
    unsigned int v32;  // eax
    unsigned int v35;  // 4120
    char v9;  // bl
    unsigned int v38;  // 4135
    unsigned int v39;  // eax
    unsigned int v40;  // cc_ndep
    unsigned int v41;  // cc_dep1
    unsigned int v42;  // 4136
    char v10;  // bl
    unsigned int v11;  // 4181
    unsigned int v12;  // cc_ndep
    unsigned int v13;  // cc_dep1
    unsigned int v14;  // 4188
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f2420(a0);
    v2 = v6;
    v7 = v4;
    v1 = v8;
    v0 = 12;
    v9 = v0;
    v10 = v9 - 8;
    v11 = _ccall(1, (unsigned int)(v9 - 6), 0xff, 0);
    v12 = v11;
    v13 = v9 - 8;
    v14 = _ccall(0, 19, (unsigned int)(v9 - 8), 0, v11);
    v17 = v7 & v10 - 4;
    v18 = _ccall(0, 13, (unsigned int)(v7 & v10 - 4), 0, 0);
    v19 = _INSERT(v7 & v10 - 4, 1, v7 & v10 - 4 & 8);
    if (v19)
    {
        v20 = _ccall(3, ~(v19), 1, 0);
        v21 = v20 | 1;
    }
    else
    {
        v22 = _ccall(3, ~(0), 1, 0);
        v21 = v22 & 4294967294;
    }
    v23 = _ccall(0, v21, 0, 0);
    v24 = _ccall(12, 0, v23 & 1, v23 & 1);
    v25 = -(v23 & 1) + 1;
    v28 = _ccall(0, 21, v25 - 1, 0, v24);
    v31 = _ccall(21, v25 - 1, 0, v24);
    v32 = v25;
    v35 = _ccall(0, 21, v32 - 1, 0, v31);
    v38 = _ccall(21, v32 - 1, 0, v31);
    v39 = v32;
    v40 = v38;
    v41 = v39 - 1;
    v42 = _ccall(0, 21, v39 - 1, 0, v38);
    v3 = v39;
    v5 = (g_1038c838 ^ g_1038c83c) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f22d0(v5);
}
```

## `sub_102fdf8e` `0x102fdf8e`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fdf8e(void)
{
}
```

## `sub_102fdfa9` `0x102fdfa9`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fdfa9(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fdfdf` `0x102fdfdf`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fdfdf(void)
{
}
```

## `sub_102fdfee` `0x102fdfee`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fdfee(void)
{
}
```

## `sub_102fdfff` `0x102fdfff`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fdfff(void)
{
}
```

## `sub_102fe040` `0x102fe040`

_200 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7f0;
extern unsigned int g_1038c7f4;

unsigned int sub_102fe040(int a0)
{
    unsigned int v4;  // edx
    unsigned int v5;  // 4141
    unsigned int v6;  // 4155
    unsigned int v9;  // 4167
    unsigned int v10;  // 4169
    unsigned int v11;  // 4171
    unsigned int v12;  // cc_ndep
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v2 = sub_102efba0(a0);
    v0 = v4;
    v5 = _ccall(0, 4, 14, 0xff, 0);
    v6 = _ccall(0, 19, 3, 0, 0);
    v9 = _ccall(19, 254, 0, 1);
    v10 = _ccall(16, 0xff, 0, v9);
    v11 = _ccall(16, 0, 0, v10);
    v12 = v11;
    v1 = _INSERT(_INSERT(v2, 1, 0) & 0xff, 0, (char)_INSERT(v2, 1, 0) & 1);
    v3 = (g_1038c7f0 ^ g_1038c7f4) * 2;
    if (v1)
        v3 |= 1;
    return sub_102efa50(v3);
}
```

## `sub_102fe06d` `0x102fe06d`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fe06d(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fe08e` `0x102fe08e`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fe08e(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fe0ab` `0x102fe0ab`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fe0ab(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fe110` `0x102fe110`

_120 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e8;
extern unsigned int g_1038c7ec;

unsigned int sub_102fe110(unsigned int a0)
{
    unsigned int v5;  // edx
    unsigned int v8;  // eax
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v0 = a0;
    v2 = sub_102ef640(a0);
    v0 = v5;
    v8 = _INSERT(_INSERT(v2 & 0xff, 0, (char)v2 & 1), 1, ~(~(0)));
    v1 = -(0 < v8) + 1;
    v3 = (g_1038c7e8 ^ g_1038c7ec) * 2;
    if (v1)
        v3 |= 1;
    return sub_102ef530(v3);
}
```

## `sub_102fe12f` `0x102fe12f`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fe12f(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fe13d` `0x102fe13d`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fe13d(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fe190` `0x102fe190`

_249 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c80c;
extern unsigned int g_1038c810;

unsigned int sub_102fe190(int a0)
{
    unsigned int v5;  // ebx
    unsigned int v6;  // ecx
    unsigned int v8;  // ecx
    unsigned int v9;  // ecx
    unsigned int v10;  // eax
    unsigned int v12;  // eax
    unsigned int v13;  // eax
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v3 = sub_102f0940(a0);
    v1 = v5;
    v0 = v6;
    v8 = _INSERT(_INSERT(v6, 1, 0), 0, 164);
    v9 = v8 * 0x1000000 | v8 * 0x100 & 0xff0000 | v8 >> 8 & 0xff00 | v8 >> 24 & 0xff;
    v10 = _INSERT(_INSERT(v3 & 0xffff, 1, 0) & 0xff, 0, ~(~((char)_INSERT(v3 & 0xffff, 1, 0))));
    v12 = v10 * 0x1000000 | v10 * 0x100 & 0xff0000 | v10 >> 8 & 0xff00 | v10 >> 24 & 0xff;
    v13 = _INSERT((char)v12 * 0 | (char)(v12 >> 24), 0, ((char)v12 * 0 | (char)(v12 >> 24)) & (char)~(~(_INSERT((char)v9 * 0 | (char)(v9 >> 24), 0, ((char)v9 * 0 | (char)(v9 >> 24)) - 39))) + 3);
    v1 = -(0 < v13) + 1;
    v2 = _INSERT(-(0 < v13) + 1, 0, -(0 < v13) + 1 == -(0 < (v3 & 0x600)) + 1);
    v4 = (g_1038c80c ^ g_1038c810) * 2;
    if (v2)
        v4 |= 1;
    return sub_102f0850(v4);
}
```

## `sub_102fe290` `0x102fe290`

_142 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c820;
extern unsigned int g_1038c824;

unsigned int sub_102fe290(int a0)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // eax
    unsigned int v8;  // ecx
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v2 = v6;
    v4 = sub_102f1390(a0);
    v1 = v6;
    v7 = v4 * 0x1000000 | v4 * 0x100 & 0xff0000 | v4 >> 8 & 0xff00 | v4 >> 24 & 0xff;
    v0 = v8;
    v3 = -(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & ~(~(50)) + 14)) + 1;
    v5 = (g_1038c820 ^ g_1038c824) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f1250(v5);
}
```

## `sub_102fe2b2` `0x102fe2b2`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102fe2b2(void)
{
}
```

## `sub_102fe330` `0x102fe330`

_144 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c824;
extern unsigned int g_1038c828;

int sub_102fe330(unsigned int a0)
{
    unsigned int v4;  // eax
    unsigned int v5;  // ebx
    unsigned int v14;  // cc_ndep
    unsigned int v15;  // cc_dep1
    unsigned int v6;  // 4121
    unsigned int v7;  // cc_ndep
    unsigned int v8;  // cc_dep1
    unsigned int v11;  // ebx
    unsigned int v12;  // ecx
    unsigned int v13;  // ebx
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v2 = sub_102f1670(a0);
    v4 = v2 * 0x1000000 | v2 * 0x100 & 0xff0000 | v2 >> 8 & 0xff00 | v2 >> 24 & 0xff;
    v5 = ~(~(50));
    v6 = _ccall(3, &/* unsupported instruction */, 4, 0);
    v7 = v6;
    v8 = v5 + 1;
    v11 = v5 + 10;
    v0 = v12;
    v13 = v11 + 4;
    v14 = v11 + 4 < v11;
    v15 = v13 + 1;
    v1 = -(0 < ((v4 * 0x1000000 | v4 * 0x100 & 0xff0000 | v4 >> 8 & 0xff00 | v4 >> 24 & 0xff) & v13 + 1)) + 1;
    v3 = (g_1038c824 ^ g_1038c828) * 2;
    if (v1)
        v3 |= 1;
    return sub_102f14d0(v3);
}
```

## `sub_102fe352` `0x102fe352`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102fe352(void)
{
}
```

## `sub_102fe369` `0x102fe369`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fe369(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fe385` `0x102fe385`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fe385(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fe3d0` `0x102fe3d0`

_145 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7ec;
extern unsigned int g_1038c7f0;

int sub_102fe3d0(unsigned int a0)
{
    unsigned int v7;  // edx
    unsigned int v8;  // ebx
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v5 = sub_102ef8d0(a0);
    v3 = v7;
    v2 = v8;
    v0 = 14;
    v1 = v5 & 0xffff;
    v4 = -(-(0 < _INSERT((char)v1 & (char)v0 - 14, 1, (char)v1 & (char)v0 - 14 & 228)));
    v6 = (g_1038c7ec ^ g_1038c7f0) * 2;
    if (v4)
        v6 |= 1;
    return sub_102ef750(v6);
}
```

## `sub_102fe470` `0x102fe470`

_528 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7dc;
extern unsigned int g_1038c7e0;

unsigned int sub_102fe470(int a0)
{
    unsigned int v9;  // ebx
    unsigned int v10;  // edx
    unsigned int v19;  // 4276
    unsigned int v20;  // cc_ndep
    unsigned int v21;  // 4101
    unsigned int v23;  // 4196
    char v24;  // cl
    unsigned int v25;  // 4197
    unsigned int v26;  // cc_ndep
    unsigned int v27;  // 4198
    unsigned int v11;  // 4201
    unsigned int v31;  // edx
    unsigned int v33;  // eax
    unsigned int v35;  // eax
    unsigned short v36;  // bx
    unsigned int v37;  // eax
    unsigned int v38;  // eax
    unsigned int v12;  // 4202
    unsigned int v39;  // eax
    unsigned int v40;  // 4108
    unsigned int v41;  // cc_dep1
    unsigned int v42;  // 4108
    unsigned int v43;  // 4126
    unsigned int v44;  // eax
    unsigned int v13;  // 4203
    unsigned int v14;  // 4204
    unsigned int v15;  // cc_ndep
    unsigned int v16;  // 4101
    unsigned int v17;  // 4101
    unsigned int v18;  // ecx
    unsigned int v0;  // [bp-0x2c]
    unsigned int v1;  // [bp-0x28]
    int v2;  // [bp-0x24], Other Possible Types: unsigned int
    unsigned int v3;  // [bp-0x20]
    int v4;  // [bp-0x1c], Other Possible Types: unsigned int
    unsigned int v5;  // [bp-0x14]
    unsigned int v6;  // [bp-0x10]
    int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]

    v5 = v9;
    v7 = sub_102f1910(a0);
    v4 = v7;
    v4 = v10;
    v11 = _ccall(16, 1, 0, (unsigned int)(char)(&/* unsupported instruction */ < &v4));
    v12 = _ccall(16, 2, 0, v11);
    v13 = _ccall(16, 3, 0, v12);
    v14 = _ccall(16, 4, 0, v13);
    v15 = v14;
    if (!((char)(0 ? 1 : 0)))
    {
        v16 = _ccall(12, 16, 5, 0, v15);
        if (!((char)v16) || !((v17 = (unsigned int)_ccall(4, 16, 5, 0, v15), !((char)v17))))
        {
            v3 = v18;
            v2 = v7;
            v19 = _ccall(16, 13, 0, 0);
            v20 = v19;
            if (!((char)(0 ? 1 : 0)))
                v21 = _ccall(12, 16, 14, 0, v20);
            v7 = sub_102ef020(a0);
            v3 = v9 & 0x800 & 16;
            v2 = v18;
            v23 = _ccall(19, 2, 0, 0);
            v24 = _INSERT(v18, 1, 0);
            v25 = _ccall(19, 1, 0, v23);
            v26 = v25;
            v27 = _ccall(0, 19, 0, 0, v25);
            v31 = v10 * 0x1000000 | v10 * 0x100 & 0xff0000 | v10 >> 8 & 0xff00 | v10 >> 24 & 0xff;
            v1 = _INSERT(v7 & 0xffff, 1, *((char *)((void*)&v7 & 0xffff + 1)) & v24);
            v33 = _INSERT(v1, 0, (char)v1 & (char)~(~(_INSERT(v24, 0, 64))));
            if (!v33)
            {
                v3 = v31 * 0x1000000 | v31 * 0x100 & 0xff0000 | v31 >> 8 & 0xff00 | v31 >> 24 & 0xff;
                v2 = v9 & 0x800 & 16;
                v1 = v7 & 0xffff;
                v35 = _INSERT(v1, 1, 0);
                v36 = _INSERT(_INSERT(*((unsigned short *)((void*)&v2 + 1)), 1, 0), 0, 128);
                v37 = v35 * 0x1000000 | v35 * 0x100 & 0xff0000 | v35 >> 8 & 0xff00 | v35 >> 24 & 0xff;
                v38 = _INSERT((char)v37 * 0 | (char)(v37 >> 24), 0, ((char)v37 * 0 | (char)(v37 >> 24)) & (char)~(~(v36)));
                v3 = -(0 < v38) + 1;
                v1 = -(0 < v38) + 1;
                v0 = 4;
                v39 = _INSERT((char)v7 & (char)v0 - 4, 1, (char)v7 & (char)v0 - 4 & 8);
                if (v39)
                {
                    v40 = _ccall(3, ~(v39), 1, 0);
                    v41 = v40 | 1;
                }
                else
                {
                    v42 = _ccall(3, ~(0), 1, 0);
                    v41 = v42 & 4294967294;
                }
                v43 = _ccall(0, v41, 0, 0);
                if (v1 != -(v43 & 1) + 1)
                    goto LABEL_102fe699;
                v44 = 0;
            }
            else
            {
LABEL_102fe699:
                v44 = 1;
            }
            v6 = v44;
            v8 = (g_1038c7dc ^ g_1038c7e0) * 2;
            if (v6)
                v8 |= 1;
            return sub_102eef00(v8);
        }
    }
}
```

## `sub_102fe4af` `0x102fe4af`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fe4af(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fe4f5` `0x102fe4f5`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fe4f5(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fe508` `0x102fe508`

_72 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c828;
extern unsigned int g_1038c82c;

int sub_102fe508(void)
{
    char v3;  // al
    char v4;  // dl
    unsigned int v1;  // [bp+0xffff8]
    unsigned int v2;  // [bp+0x100000]

    v1 = _INSERT(v3 CONCAT 0, 0, v3 & v4 - 4);
    v2 = (g_1038c828 ^ g_1038c82c) * 2;
    if (v1)
        v2 |= 1;
    sub_102f1810(v2);
    return;
}
```

## `sub_102fe550` `0x102fe550`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102fe550(void)
{
}
```

## `sub_102fe593` `0x102fe593`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fe593(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fe6e0` `0x102fe6e0`

_173 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c834;
extern unsigned int g_1038c838;

int sub_102fe6e0(unsigned int a0)
{
    unsigned int v4;  // eax
    unsigned int v5;  // ecx
    char v16;  // cl
    unsigned int v17;  // ecx
    unsigned int v18;  // edx
    unsigned int v10;  // 4199
    unsigned int v11;  // ecx
    unsigned int v12;  // cc_ndep
    unsigned int v13;  // cc_dep1
    unsigned int v0;  // [bp-0x18]
    int <0x102fe6e0[is_2]|Stack bp-0x10, 1 B>;  // [bp-0x10]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v2 = sub_102f2170(a0);
    v4 = v2 * 0x1000000 | v2 * 0x100 & 0xff0000 | v2 >> 8 & 0xff00 | v2 >> 24 & 0xff;
    v5 = ~(~(13)) + 4;
    v10 = _ccall(18, v5 + 1, 0, (unsigned int)(char)(&<0x102fe6e0[is_2]|Stack bp-0x10, 1 B> < &/* unsupported instruction */));
    v11 = v5 + 12;
    v12 = v10;
    v13 = v11 + 1;
    v16 = (char)(v11 + 1) + 3;
    v17 = _INSERT(v16 + 13, 0, v16 + 18);
    v0 = v18;
    v1 = -(0 < ((v4 * 0x1000000 | v4 * 0x100 & 0xff0000 | v4 >> 8 & 0xff00 | v4 >> 24 & 0xff) & v17 + 14)) + 1;
    v3 = (g_1038c834 ^ g_1038c838) * 2;
    if (!(0 < ((v4 * 0x1000000 | v4 * 0x100 & 0xff0000 | v4 >> 8 & 0xff00 | v4 >> 24 & 0xff) & v17 + 14)) != 4294967295)
        v3 |= 1;
    return sub_102f2010(v3);
}
```

## `sub_102fe790` `0x102fe790`

_157 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c804;
extern unsigned int g_1038c808;

unsigned int sub_102fe790(int a0)
{
    unsigned int v6;  // edx
    unsigned int v7;  // ebx
    unsigned int v8;  // eax
    unsigned int v9;  // 4108
    unsigned int v10;  // cc_dep1
    unsigned int v11;  // 4108
    unsigned int v12;  // 4159
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f0650(a0);
    v2 = v6;
    v1 = v7;
    v0 = 1040;
    v8 = _INSERT(_INSERT(v4 & 0xffff, 1, (char)v4 & *((char *)((void*)&v0 + 1)) - 4) & 0xff, 0, (char)_INSERT(v4 & 0xffff, 1, (char)v4 & *((char *)((void*)&v0 + 1)) - 4) & 4);
    if (v8)
    {
        v9 = _ccall(3, ~(v8), 1, 0);
        v10 = v9 | 1;
    }
    else
    {
        v11 = _ccall(3, ~(0), 1, 0);
        v10 = v11 & 4294967294;
    }
    v12 = _ccall(0, v10, 0, 0);
    v3 = -(-(v12 & 1));
    v5 = (g_1038c804 ^ g_1038c808) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0570(v5);
}
```

## `sub_102fe830` `0x102fe830`

_165 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7dc;
extern unsigned int g_1038c7e0;

unsigned int sub_102fe830(int a0)
{
    unsigned int v6;  // edx
    unsigned int v7;  // ebx
    unsigned int v9;  // eax
    unsigned short v10;  // bx
    unsigned int v11;  // eax
    unsigned int v12;  // eax
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102ef020(a0);
    v2 = v6;
    v1 = v7;
    v0 = v4 & 0xffff;
    v9 = _INSERT(v0, 1, 0);
    v10 = _INSERT(_INSERT(*((unsigned short *)((void*)&v7 + 1)), 1, 0), 0, 65);
    v11 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v12 = _INSERT((char)v11 * 0 | (char)(v11 >> 24), 0, ((char)v11 * 0 | (char)(v11 >> 24)) & (char)~(~(v10)));
    v3 = -(0 < v12) + 1;
    v5 = (g_1038c7dc ^ g_1038c7e0) * 2;
    if (v3)
        v5 |= 1;
    return sub_102eef00(v5);
}
```

## `sub_102fe8e0` `0x102fe8e0`

_161 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c840;
extern unsigned int g_1038c844;

unsigned int sub_102fe8e0(int a0)
{
    unsigned int v4;  // edx
    unsigned int v6;  // eax
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v2 = sub_102f2940(a0);
    v0 = v4;
    v6 = _INSERT(_INSERT(v2 & 0xff, 0, (char)v2 & 1), 1, 0);
    v1 = -(0 < v6) + 1;
    v3 = (g_1038c840 ^ g_1038c844) * 2;
    if (v1)
        v3 |= 1;
    return sub_102f27b0(v3);
}
```

## `sub_102fe990` `0x102fe990`

_154 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7dc;
extern unsigned int g_1038c7e0;

unsigned int sub_102fe990(int a0)
{
    unsigned short v7;  // ax
    unsigned int v8;  // edx
    unsigned int v9;  // cc_dep1
    unsigned int v10;  // ebx
    unsigned int v11;  // 4130
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v5 = sub_102ef020(a0);
    v7 = v5;
    v3 = v8;
    v9 = v7;
    v2 = v10;
    v0 = 31;
    v11 = _ccall(0, 15, (unsigned int)v7, 0, 0);
    v1 = v7;
    v4 = -(-(0 < _INSERT((char)v1 & (char)v0 - 31, 1, (char)v1 & (char)v0 - 31 & 243)));
    v6 = (g_1038c7dc ^ g_1038c7e0) * 2;
    if (v4)
        v6 |= 1;
    return sub_102eef00(v6);
}
```

## `sub_102fe9bc` `0x102fe9bc`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fe9bc(void)
{
}
```

## `sub_102fea30` `0x102fea30`

_156 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7dc;
extern unsigned int g_1038c7e0;

unsigned int sub_102fea30(int a0)
{
    unsigned int v4;  // edx
    unsigned int v6;  // eax
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v2 = sub_102ef020(a0);
    v0 = v4;
    v6 = _INSERT(_INSERT(v2 & 0xff, 0, (char)v2 & 1), 1, 0);
    v1 = v6;
    v3 = (g_1038c7dc ^ g_1038c7e0) * 2;
    if (v1)
        v3 |= 1;
    return sub_102eef00(v3);
}
```

## `sub_102fead0` `0x102fead0`

_240 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7f4;
extern unsigned int g_1038c7f8;

unsigned int sub_102fead0(int a0)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // ecx
    unsigned int v10;  // ecx
    unsigned int v11;  // eax
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102efd90(a0);
    v2 = v6;
    v1 = v7;
    v0 = _INSERT(v4 & 0xffff, 1, 0);
    v10 = _INSERT(_INSERT(v7, 1, 0), 0, 125);
    v11 = _INSERT(v0, 0, (char)v0 & (char)~(~(v10)) + 3);
    v3 = -(0 < v11) + 1;
    v5 = (g_1038c7f4 ^ g_1038c7f8) * 2;
    if (v3)
        v5 |= 1;
    return sub_102efcf0(v5);
}
```

## `sub_102febc0` `0x102febc0`

_189 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c80c;
extern unsigned int g_1038c810;

unsigned int sub_102febc0(int a0)
{
    unsigned int v8;  // ebx
    unsigned int v9;  // esi
    unsigned int v10;  // edi
    unsigned int v11;  // eax
    unsigned int v12;  // ecx
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]

    v4 = v8;
    v3 = v9;
    v2 = v10;
    v6 = sub_102f0940(a0);
    v1 = v8;
    v11 = v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff;
    v0 = v12;
    v5 = -(0 < ((v11 * 0x1000000 | v11 * 0x100 & 0xff0000 | v11 >> 8 & 0xff00 | v11 >> 24 & 0xff) & ~(~(115)) - 0x33)) + 1;
    v7 = (g_1038c80c ^ g_1038c810) * 2;
    if (v5)
        v7 |= 1;
    return sub_102f0850(v7);
}
```

## `sub_102febe4` `0x102febe4`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102febe4(void)
{
}
```

## `sub_102fec90` `0x102fec90`

_168 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c818;
extern unsigned int g_1038c81c;

unsigned int sub_102fec90(int a0)
{
    unsigned int v5;  // ecx
    unsigned int v6;  // eax
    char v7;  // cl
    unsigned int v8;  // ecx
    unsigned int v9;  // edx
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v3 = sub_102f0f30(a0);
    v1 = v5;
    v6 = v3 * 0x1000000 | v3 * 0x100 & 0xff0000 | v3 >> 8 & 0xff00 | v3 >> 24 & 0xff;
    v7 = (char)(~(~(4)) + 25) + 3;
    v8 = _INSERT(v7 + 16, 0, v7 + 18);
    v0 = v9;
    v2 = -(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 14)) + 1;
    v4 = (g_1038c818 ^ g_1038c81c) * 2;
    if (!(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 14)) != 4294967295)
        v4 |= 1;
    return sub_102f0e70(v4);
}
```

## `sub_102fed40` `0x102fed40`

_217 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c800;
extern unsigned int g_1038c804;

int sub_102fed40(unsigned int a0)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // eax
    unsigned int v16;  // 4104
    unsigned int v8;  // ebx
    unsigned int v9;  // ecx
    int v11;  // edx
    int v12;  // cc_dep1
    unsigned int v13;  // 4234
    unsigned int v14;  // 4101
    unsigned int v15;  // eax
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v2 = v6;
    v4 = sub_102f04d0(a0);
    v1 = v6;
    v7 = v4 * 0x1000000 | v4 * 0x100 & 0xff0000 | v4 >> 8 & 0xff00 | v4 >> 24 & 0xff;
    v8 = ~(~(110)) - -13;
    v0 = v9;
    v2 = -(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & v8 + 5)) + 1;
    v11 = -(0 < (v4 & 0xfc00)) + 1;
    v12 = -(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & v8 + 5)) + 1;
    v13 = _ccall(0, 6, -((unsigned int)(char)(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & v8 + 5))) + 1, v11, 0);
    if (v12 == v11)
    {
        v14 = _ccall(0, 6, v12, v11, 0);
        v15 = 0;
    }
    else
    {
        v16 = _ccall(0, 15, 0, 0, 0);
        v15 = 1;
    }
    v3 = v15;
    v5 = (g_1038c800 ^ g_1038c804) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0430(v5);
}
```

## `sub_102fed62` `0x102fed62`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102fed62(void)
{
}
```

## `sub_102fee30` `0x102fee30`

_233 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c83c;
extern unsigned int g_1038c840;

unsigned int sub_102fee30(int a0)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // ecx
    unsigned int v10;  // ecx
    unsigned int v11;  // eax
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f2690(a0);
    v2 = v6;
    v1 = v7;
    v0 = _INSERT(v4 & 0xffff, 1, 0);
    v10 = _INSERT(_INSERT(v7, 1, 0), 0, 124);
    v11 = _INSERT(v0, 0, (char)v0 & (char)~(~(v10)) - -4);
    v3 = -(-(0 < v11));
    v5 = (g_1038c83c ^ g_1038c840) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f2570(v5);
}
```

## `sub_102fef20` `0x102fef20`

_176 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c824;
extern unsigned int g_1038c828;

int sub_102fef20(unsigned int a0)
{
    unsigned short v6;  // ax
    unsigned int v7;  // edx
    unsigned int v8;  // cc_dep1
    unsigned int v9;  // ebx
    char v10;  // bl
    unsigned int v11;  // 4130
    unsigned int v12;  // 4139
    unsigned int v13;  // cc_ndep
    unsigned int v14;  // cc_dep1
    unsigned int v15;  // 4141
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f1670(a0);
    v6 = v4;
    v2 = v7;
    v8 = v6;
    v1 = v9;
    v0 = 0x1e00;
    v10 = v0;
    v11 = _ccall(0, 15, (unsigned int)v6, 0, 0);
    v0 = v6;
    v12 = _ccall(19, (unsigned int)(v10 - 6), 0, (unsigned int)(char)(v10 - 2 < 3));
    v13 = v12;
    v14 = v10 - 7;
    v15 = _ccall(0, 19, (unsigned int)(v10 - 7), 0, v12);
    v3 = -(-(0 < _INSERT(_INSERT(v0, 1, *((char *)((void*)&v0 + 1)) & v10 - 30) & 0xff, 0, (char)_INSERT(v0, 1, *((char *)((void*)&v0 + 1)) & v10 - 30) & 4)));
    v5 = (g_1038c824 ^ g_1038c828) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f14d0(v5);
}
```

## `sub_102fef4f` `0x102fef4f`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fef4f(void)
{
}
```

## `sub_102fef67` `0x102fef67`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fef67(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fefe0` `0x102fefe0`

_204 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e0;
extern unsigned int g_1038c7e4;

int sub_102fefe0(unsigned int a0)
{
    unsigned int v5;  // ebx
    unsigned int v6;  // ecx
    unsigned int v8;  // ecx
    unsigned int v9;  // ecx
    unsigned int v10;  // eax
    unsigned int v12;  // eax
    unsigned int v13;  // eax
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v3 = sub_102ef270(a0);
    v1 = v5;
    v0 = v6;
    v8 = _INSERT(_INSERT(v6, 1, 0), 0, 164);
    v9 = v8 * 0x1000000 | v8 * 0x100 & 0xff0000 | v8 >> 8 & 0xff00 | v8 >> 24 & 0xff;
    v10 = _INSERT(_INSERT(v3 & 0xffff, 1, 0) & 0xff, 0, ~(~((char)_INSERT(v3 & 0xffff, 1, 0))));
    v12 = v10 * 0x1000000 | v10 * 0x100 & 0xff0000 | v10 >> 8 & 0xff00 | v10 >> 24 & 0xff;
    v13 = _INSERT((char)v12 * 0 | (char)(v12 >> 24), 0, ((char)v12 * 0 | (char)(v12 >> 24)) & (char)~(~(_INSERT((char)v9 * 0 | (char)(v9 >> 24), 0, ((char)v9 * 0 | (char)(v9 >> 24)) - 39))) + 3);
    v2 = -(0 < v13) + 1;
    v4 = (g_1038c7e0 ^ g_1038c7e4) * 2;
    if (v2)
        v4 |= 1;
    return sub_102ef140(v4);
}
```

## `sub_102ff0b0` `0x102ff0b0`

_206 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7ec;
extern unsigned int g_1038c7f0;

int sub_102ff0b0(unsigned int a0)
{
    unsigned int v5;  // ecx
    unsigned int v6;  // edx
    unsigned int v15;  // 4205
    unsigned int v18;  // eax
    unsigned int v19;  // eax
    unsigned int v7;  // eax
    unsigned int v8;  // edi
    unsigned int v9;  // edi
    unsigned int v10;  // cc_dep1
    unsigned int v11;  // 4310
    char v14;  // al
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v3 = sub_102ef8d0(a0);
    v1 = v5;
    v0 = v3;
    v1 = v6;
    v7 = v0 * 0x1000000 | v0 * 0x100 & 0xff0000 | v0 >> 8 & 0xff00 | v0 >> 24 & 0xff;
    v9 = v8 - 2;
    v10 = v9 - 1;
    v11 = _ccall(0, 21, v9 - 1, 0, 0);
    v14 = _INSERT(v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff, 1, 0);
    v15 = _ccall(0, 19, 1, 0, 0);
    v18 = _INSERT(v14 & 1, 1, ~(v14 & 1));
    v19 = v18 * 0x1000000 | v18 * 0x100 & 0xff0000 | v18 >> 8 & 0xff00 | v18 >> 24 & 0xff;
    v2 = _INSERT((char)v19 * 0 | (char)(v19 >> 24), 1, ~((char)v19 * 0 | (char)(v19 >> 24)));
    v4 = (g_1038c7ec ^ g_1038c7f0) * 2;
    if (v2)
        v4 |= 1;
    return sub_102ef750(v4);
}
```

## `sub_102ff110` `0x102ff110`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102ff110(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

