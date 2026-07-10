# elfbot.dll decompiled — jiru 0x102f3315..0x102f4d90

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_102f3315` `0x102f3315`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f3315(void)
{
}
```

## `sub_102f3370` `0x102f3370`

_138 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c80c;
extern unsigned int g_1038c810;

unsigned int sub_102f3370(int a0)
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

    v4 = sub_102f0940(a0);
    v2 = v6;
    v1 = v7;
    v0 = v4 & 0xffff;
    v9 = _INSERT(v0, 1, 0);
    v10 = _INSERT(_INSERT(*((unsigned short *)((void*)&v7 + 1)), 1, 0), 0, 128);
    v11 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v12 = _INSERT((char)v11 * 0 | (char)(v11 >> 24), 0, ((char)v11 * 0 | (char)(v11 >> 24)) & (char)~(~(v10)));
    v3 = -(0 < v12) + 1;
    v5 = (g_1038c80c ^ g_1038c810) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0850(v5);
}
```

## `sub_102f3400` `0x102f3400`

_156 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e8;
extern unsigned int g_1038c7ec;

unsigned int sub_102f3400(int a0)
{
    unsigned int v7;  // edx
    unsigned int v8;  // ebx
    unsigned int v9;  // 4241
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v5 = sub_102ef640(a0);
    v3 = v7;
    v2 = v8;
    v0 = 31;
    v1 = v5 & 0xffff;
    v9 = _ccall(0, 19, 244, 0, 0);
    v4 = -(-(0 < _INSERT((char)v1 & (char)v0 - 31, 1, (char)v1 & (char)v0 - 31 & 244)));
    v6 = (g_1038c7e8 ^ g_1038c7ec) * 2;
    if (v4)
        v6 |= 1;
    return sub_102ef530(v6);
}
```

## `sub_102f3459` `0x102f3459`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f3459(void)
{
}
```

## `sub_102f34a0` `0x102f34a0`

_159 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c810;
extern unsigned int g_1038c814;

unsigned int sub_102f34a0(int a0)
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
    v4 = sub_102f0ba0(a0);
    v1 = v6;
    v7 = v4 * 0x1000000 | v4 * 0x100 & 0xff0000 | v4 >> 8 & 0xff00 | v4 >> 24 & 0xff;
    v0 = v8;
    v2 = -(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & ~(~(114)) + 14)) + 1;
    v3 = _INSERT(-(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & ~(~(114)) + 14)) + 1, 0, -(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & ~(~(114)) + 14)) + 1 == -(0 < (v4 & 0xf900)) + 1);
    v5 = (g_1038c810 ^ g_1038c814) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0a30(v5);
}
```

## `sub_102f34c2` `0x102f34c2`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102f34c2(void)
{
}
```

## `sub_102f3550` `0x102f3550`

_196 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c844;
extern unsigned int g_1038c848;

unsigned int sub_102f3550(int a0)
{
    unsigned int v5;  // ecx
    unsigned int v6;  // edx
    unsigned int v7;  // eax
    unsigned int v9;  // eax
    unsigned int v10;  // eax
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v3 = sub_102f2b60(a0);
    v1 = v5;
    v0 = v3;
    v1 = v6;
    v7 = v0 * 0x1000000 | v0 * 0x100 & 0xff0000 | v0 >> 8 & 0xff00 | v0 >> 24 & 0xff;
    v9 = _INSERT(_INSERT((char)v7 * 0 | (char)(v7 >> 24), 0, ((char)v7 * 0 | (char)(v7 >> 24)) & 1), 1, 255);
    v10 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v2 = -(0 < _INSERT((char)v10 * 0 | (char)(v10 >> 24), 1, ~((char)v10 * 0 | (char)(v10 >> 24)))) + 1;
    v4 = (g_1038c844 ^ g_1038c848) * 2;
    if (v2)
        v4 |= 1;
    return sub_102f2ad0(v4);
}
```

## `sub_102f3620` `0x102f3620`

_166 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c83c;
extern unsigned int g_1038c840;

unsigned int sub_102f3620(int a0)
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

    v3 = sub_102f2690(a0);
    v1 = v5;
    v6 = v3 * 0x1000000 | v3 * 0x100 & 0xff0000 | v3 >> 8 & 0xff00 | v3 >> 24 & 0xff;
    v7 = (char)(~(~(82)) + 8) + 3;
    v8 = _INSERT(v7 + 30, 0, v7 + 0x22);
    v0 = v9;
    v2 = -(-(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 - -1)));
    v4 = (g_1038c83c ^ g_1038c840) * 2;
    if (0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 - -1))
        v4 |= 1;
    return sub_102f2570(v4);
}
```

## `sub_102f36d0` `0x102f36d0`

_178 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c804;
extern unsigned int g_1038c808;

unsigned int sub_102f36d0(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v8;  // ebx
    unsigned int v9;  // esi
    unsigned int v10;  // edi
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]

    v5 = v8;
    v4 = v9;
    v3 = v10;
    v2 = v8;
    v1 = a0;
    v0 = 0xffff;
    v6 = (!a3 && 1 ? 1 : 0);
    v7 = (g_1038c804 ^ g_1038c808) * 2;
    if (v6)
        v7 |= 1;
    return sub_102f0570(v7);
}
```

## `sub_102f3790` `0x102f3790`

_199 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7dc;
extern unsigned int g_1038c7e0;

unsigned int sub_102f3790(int a0)
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

    v3 = sub_102ef020(a0);
    v1 = v5;
    v6 = v3 * 0x1000000 | v3 * 0x100 & 0xff0000 | v3 >> 8 & 0xff00 | v3 >> 24 & 0xff;
    v7 = (char)(~(~(75)) + 15) + 3;
    v8 = _INSERT(v7 + 13, 0, v7 + 18);
    v0 = v9;
    v2 = -(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 0x11)) + 1;
    v2 = _INSERT(-(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 0x11)) + 1, 0, -(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 0x11)) + 1 == -(0 < (v3 & 64000)) + 1);
    v4 = (g_1038c7dc ^ g_1038c7e0) * 2;
    if (v2)
        v4 |= 1;
    return sub_102eef00(v4);
}
```

## `sub_102f3860` `0x102f3860`

_121 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7ec;
extern unsigned int g_1038c7f0;

int sub_102f3860(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // edi
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v3 = v6;
    v2 = v7;
    v1 = v6;
    v0 = a0;
    v4 = (!a3 && 1 ? 1 : 0);
    v5 = (g_1038c7ec ^ g_1038c7f0) * 2;
    if (v4)
        v5 |= 1;
    return sub_102ef750(v5);
}
```

## `sub_102f38e0` `0x102f38e0`

_173 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c840;
extern unsigned int g_1038c844;

unsigned int sub_102f38e0(int a0)
{
    unsigned int v7;  // ebx
    unsigned int v8;  // edx
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v3 = v7;
    v5 = sub_102f2940(a0);
    v2 = v8;
    v1 = v7;
    v0 = v5 & 0xffff;
    v4 = 1;
    v6 = (g_1038c840 ^ g_1038c844) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f27b0(v6);
}
```

## `sub_102f3990` `0x102f3990`

_169 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7dc;
extern unsigned int g_1038c7e0;

unsigned int sub_102f3990(int a0)
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
    v1 = -(0 < v6) + 1;
    v3 = (g_1038c7dc ^ g_1038c7e0) * 2;
    if (v1)
        v3 |= 1;
    return sub_102eef00(v3);
}
```

## `sub_102f3a40` `0x102f3a40`

_126 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c834;
extern unsigned int g_1038c838;

int sub_102f3a40(unsigned int a0)
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
    v4 = sub_102f2170(a0);
    v1 = v6;
    v7 = v4 * 0x1000000 | v4 * 0x100 & 0xff0000 | v4 >> 8 & 0xff00 | v4 >> 24 & 0xff;
    v0 = v8;
    v3 = -(-(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & ~(~(113)) + 15)));
    v5 = (g_1038c834 ^ g_1038c838) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f2010(v5);
}
```

## `sub_102f3a62` `0x102f3a62`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102f3a62(void)
{
}
```

## `sub_102f3ad0` `0x102f3ad0`

_166 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e0;
extern unsigned int g_1038c7e4;

int sub_102f3ad0(unsigned int a0)
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

    v4 = sub_102ef270(a0);
    v2 = v6;
    v1 = v7;
    v0 = v4 & 0xffff;
    v9 = _INSERT(v0, 1, 0);
    v10 = _INSERT(_INSERT(*((unsigned short *)((void*)&v7 + 1)), 1, 0), 0, 65);
    v11 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v12 = _INSERT((char)v11 * 0 | (char)(v11 >> 24), 0, ((char)v11 * 0 | (char)(v11 >> 24)) & (char)~(~(v10)));
    v3 = -(-(0 < v12));
    v5 = (g_1038c7e0 ^ g_1038c7e4) * 2;
    if (v3)
        v5 |= 1;
    return sub_102ef140(v5);
}
```

## `sub_102f3b80` `0x102f3b80`

_148 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c828;
extern unsigned int g_1038c82c;

unsigned int sub_102f3b80(int a0)
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

    v5 = sub_102f1910(a0);
    v7 = v5;
    v3 = v8;
    v9 = v7;
    v2 = v10;
    v0 = 31;
    v11 = _ccall(0, 15, (unsigned int)v7, 0, 0);
    v1 = v7;
    v4 = -(0 < _INSERT((char)v1 & (char)v0 - 31, 1, (char)v1 & (char)v0 - 31 & 243)) + 1;
    v6 = (g_1038c828 ^ g_1038c82c) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f1810(v6);
}
```

## `sub_102f3bac` `0x102f3bac`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f3bac(void)
{
}
```

## `sub_102f3c20` `0x102f3c20`

_211 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c820;
extern unsigned int g_1038c824;

unsigned int sub_102f3c20(int a0)
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

    v3 = sub_102f1390(a0);
    v1 = v5;
    v0 = v6;
    v8 = _INSERT(_INSERT(v6, 1, 0), 0, 103);
    v9 = v8 * 0x1000000 | v8 * 0x100 & 0xff0000 | v8 >> 8 & 0xff00 | v8 >> 24 & 0xff;
    v10 = _INSERT(_INSERT(v3 & 0xffff, 1, 0) & 0xff, 0, ~(~((char)_INSERT(v3 & 0xffff, 1, 0))));
    v12 = v10 * 0x1000000 | v10 * 0x100 & 0xff0000 | v10 >> 8 & 0xff00 | v10 >> 24 & 0xff;
    v13 = _INSERT((char)v12 * 0 | (char)(v12 >> 24), 0, ((char)v12 * 0 | (char)(v12 >> 24)) & (char)~(~(_INSERT((char)v9 * 0 | (char)(v9 >> 24), 0, ((char)v9 * 0 | (char)(v9 >> 24)) - 41))) + 3);
    v2 = -(-(0 < v13));
    v4 = (g_1038c820 ^ g_1038c824) * 2;
    if (v2)
        v4 |= 1;
    return sub_102f1250(v4);
}
```

## `sub_102f3d00` `0x102f3d00`

_338 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e8;
extern unsigned int g_1038c7ec;

unsigned int sub_102f3d00(int a0)
{
    unsigned int v9;  // ebx
    unsigned int v10;  // edx
    unsigned int v19;  // eax
    unsigned int v20;  // eax
    unsigned short v21;  // ax
    unsigned int v22;  // cc_dep1
    unsigned int v23;  // 4382
    unsigned int v25;  // eax
    unsigned int v12;  // eax
    unsigned short v13;  // bx
    unsigned int v14;  // eax
    unsigned int v15;  // eax
    unsigned int v17;  // eax
    unsigned short v18;  // bx
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x1c]
    unsigned int v4;  // [bp-0x18]
    unsigned int v5;  // [bp-0x14]
    unsigned int v6;  // [bp-0x10]
    int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]

    v5 = v9;
    v7 = sub_102ef640(a0);
    v4 = v10;
    v3 = v9;
    v2 = v7 & 0xffff;
    v12 = _INSERT(v7 & 0xffff, 1, 0);
    v13 = _INSERT(_INSERT(*((unsigned short *)((void*)&v9 + 1)), 1, 0), 0, 64);
    v14 = v12 * 0x1000000 | v12 * 0x100 & 0xff0000 | v12 >> 8 & 0xff00 | v12 >> 24 & 0xff;
    v15 = _INSERT((char)v14 * 0 | (char)(v14 >> 24), 0, ((char)v14 * 0 | (char)(v14 >> 24)) & (char)~(~(v13)));
    if (!v15)
    {
        v4 = v10;
        v2 = v7 & 0xffff;
        v17 = _INSERT(v7 & 0xffff, 1, 0);
        v18 = _INSERT(_INSERT(*((unsigned short *)((void*)&v3 + 1)), 1, 0), 0, 128);
        v19 = v17 * 0x1000000 | v17 * 0x100 & 0xff0000 | v17 >> 8 & 0xff00 | v17 >> 24 & 0xff;
        v20 = _INSERT((char)v19 * 0 | (char)(v19 >> 24), 0, ((char)v19 * 0 | (char)(v19 >> 24)) & (char)~(~(v18)));
        v4 = -(0 < v20) + 1;
        v21 = v7;
        v3 = v10;
        v22 = v21;
        v2 = v3;
        v0 = 13;
        v23 = _ccall(0, 15, (unsigned int)v21, 0, 0);
        v1 = v21;
        if (-(0 < v20) + 1 != -(0 < _INSERT((char)v1 & (char)v0 - 13, 1, (char)v1 & (char)v0 - 13 & 227)) + 1)
            goto LABEL_102f3e1c;
        v25 = 0;
    }
    else
    {
LABEL_102f3e1c:
        v25 = 1;
    }
    v6 = v25;
    v8 = (g_1038c7e8 ^ g_1038c7ec) * 2;
    if (v6)
        v8 |= 1;
    return sub_102ef530(v8);
}
```

## `sub_102f3ddc` `0x102f3ddc`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f3ddc(void)
{
}
```

## `sub_102f3e60` `0x102f3e60`

_162 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c82c;
extern unsigned int g_1038c830;

unsigned int sub_102f3e60(int a0)
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

    v5 = sub_102f1b90(a0);
    v7 = v5;
    v3 = v8;
    v9 = v7;
    v2 = v10;
    v0 = 0xd00;
    v11 = _ccall(0, 15, (unsigned int)v7, 0, 0);
    v1 = v7;
    v4 = -(-(0 < _INSERT(_INSERT(v1, 1, *((char *)((void*)&v1 + 1)) & (char)v0 - 13) & 0xff, 0, (char)_INSERT(v1, 1, *((char *)((void*)&v1 + 1)) & (char)v0 - 13) & 4)));
    v6 = (g_1038c82c ^ g_1038c830) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f1a10(v6);
}
```

## `sub_102f3e8f` `0x102f3e8f`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f3e8f(void)
{
}
```

## `sub_102f3f10` `0x102f3f10`

_225 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e8;
extern unsigned int g_1038c7ec;

unsigned int sub_102f3f10(unsigned int a0)
{
    unsigned int v7;  // ebx
    unsigned int v16;  // 4271
    unsigned int v17;  // cc_ndep
    unsigned int v18;  // cc_dep1
    unsigned int v19;  // 4278
    unsigned int v23;  // eax
    unsigned int v24;  // eax
    unsigned int v8;  // ecx
    unsigned int v10;  // ecx
    unsigned int v11;  // ecx
    unsigned int v12;  // eax
    char v13;  // cl
    unsigned int v14;  // 4259
    unsigned int v15;  // 4265
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v1 = a0;
    v4 = sub_102ef640(a0);
    v1 = v7;
    v0 = v8;
    v10 = _INSERT(_INSERT(v8, 1, 16), 0, 101);
    v11 = v10 * 0x1000000 | v10 * 0x100 & 0xff0000 | v10 >> 8 & 0xff00 | v10 >> 24 & 0xff;
    v12 = _INSERT(_INSERT(v4 & 0xffff, 1, (char)v4 & 16) & 0xff, 0, ~(~((char)_INSERT(v4 & 0xffff, 1, (char)v4 & 16))));
    v13 = (char)v11 * 0 | (char)(v11 >> 24);
    v14 = _ccall(1, (unsigned int)(v13 - 20), 12, 0);
    v15 = _ccall(19, (unsigned int)(v13 - 9), 0, v14);
    v16 = _ccall(19, (unsigned int)(v13 - 10), 0, v15);
    v17 = v16;
    v18 = v13 - 11;
    v19 = _ccall(0, 19, (unsigned int)(v13 - 11), 0, v16);
    v23 = v12 * 0x1000000 | v12 * 0x100 & 0xff0000 | v12 >> 8 & 0xff00 | v12 >> 24 & 0xff;
    v24 = _INSERT((char)v23 * 0 | (char)(v23 >> 24), 0, ((char)v23 * 0 | (char)(v23 >> 24)) & (char)~(~(_INSERT(v13 - 11 CONCAT 0, 0, v13 - 40))) + 3);
    v3 = -(0 < v24) + 1;
    v5 = (g_1038c7e8 ^ g_1038c7ec) * 2;
    if (v3)
        v5 |= 1;
    return sub_102ef530(v5);
}
```

## `sub_102f3f30` `0x102f3f30`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f3f30(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f4000` `0x102f4000`

_126 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c838;
extern unsigned int g_1038c83c;

int sub_102f4000(unsigned int a0)
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
    v4 = sub_102f2420(a0);
    v1 = v6;
    v7 = v4 * 0x1000000 | v4 * 0x100 & 0xff0000 | v4 >> 8 & 0xff00 | v4 >> 24 & 0xff;
    v0 = v8;
    v3 = -(-(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & ~(~(113)) + 15)));
    v5 = (g_1038c838 ^ g_1038c83c) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f22d0(v5);
}
```

## `sub_102f4022` `0x102f4022`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102f4022(void)
{
}
```

## `sub_102f4090` `0x102f4090`

_176 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c820;
extern unsigned int g_1038c824;

unsigned int sub_102f4090(int a0)
{
    unsigned short v7;  // ax
    unsigned int v8;  // edx
    unsigned int v17;  // 4274
    unsigned int v9;  // cc_dep1
    unsigned int v10;  // ebx
    unsigned int v11;  // 4130
    unsigned int v12;  // 4266
    unsigned int v13;  // 4268
    unsigned int v14;  // 4270
    unsigned int v15;  // 4272
    unsigned int v16;  // cc_ndep
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v5 = sub_102f1390(a0);
    v7 = v5;
    v3 = v8;
    v9 = v7;
    v2 = v10;
    v0 = 0xc00;
    v11 = _ccall(0, 15, (unsigned int)v7, 0, 0);
    v1 = v7;
    v12 = _ccall(19, 8, 0, 0);
    v13 = _ccall(19, 7, 0, v12);
    v14 = _ccall(19, 6, 0, v13);
    v15 = _ccall(19, 5, 0, v14);
    v16 = v15;
    v17 = _ccall(0, 19, 4, 0, v15);
    v4 = -(0 < _INSERT(_INSERT(v1, 1, *((char *)((void*)&v1 + 1)) & (char)v0 - 12) & 0xff, 0, (char)_INSERT(v1, 1, *((char *)((void*)&v1 + 1)) & (char)v0 - 12) & 4)) + 1;
    v6 = (g_1038c820 ^ g_1038c824) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f1250(v6);
}
```

## `sub_102f40bf` `0x102f40bf`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f40bf(void)
{
}
```

## `sub_102f4101` `0x102f4101`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f4101(void)
{
}
```

## `sub_102f4150` `0x102f4150`

_248 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c828;
extern unsigned int g_1038c82c;

unsigned int sub_102f4150(int a0)
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

    v3 = sub_102f1910(a0);
    v1 = v5;
    v0 = v6;
    v8 = _INSERT(_INSERT(v6, 1, 0), 0, 164);
    v9 = v8 * 0x1000000 | v8 * 0x100 & 0xff0000 | v8 >> 8 & 0xff00 | v8 >> 24 & 0xff;
    v10 = _INSERT(_INSERT(v3 & 0xffff, 1, 0) & 0xff, 0, ~(~((char)_INSERT(v3 & 0xffff, 1, 0))));
    v12 = v10 * 0x1000000 | v10 * 0x100 & 0xff0000 | v10 >> 8 & 0xff00 | v10 >> 24 & 0xff;
    v13 = _INSERT((char)v12 * 0 | (char)(v12 >> 24), 0, ((char)v12 * 0 | (char)(v12 >> 24)) & (char)~(~(_INSERT((char)v9 * 0 | (char)(v9 >> 24), 0, ((char)v9 * 0 | (char)(v9 >> 24)) - 39))) + 3);
    v1 = -(0 < v13) + 1;
    v2 = _INSERT(-(0 < v13) + 1, 0, -(0 < v13) + 1 == -(0 < (v3 & 0x600)) + 1);
    v4 = (g_1038c828 ^ g_1038c82c) * 2;
    if (v2)
        v4 |= 1;
    return sub_102f1810(v4);
}
```

## `sub_102f4250` `0x102f4250`

_172 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c81c;
extern unsigned int g_1038c820;

int sub_102f4250(unsigned int a0)
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

    v4 = sub_102f1120(a0);
    v2 = v6;
    v1 = v7;
    v0 = v4 & 0xffff;
    v9 = _INSERT(v0, 1, 0);
    v10 = _INSERT(_INSERT(*((unsigned short *)((void*)&v7 + 1)), 1, 0), 0, 65);
    v11 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v12 = _INSERT((char)v11 * 0 | (char)(v11 >> 24), 0, ((char)v11 * 0 | (char)(v11 >> 24)) & (char)~(~(v10)));
    v3 = -(-(0 < v12));
    v5 = (g_1038c81c ^ g_1038c820) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0ff0(v5);
}
```

## `sub_102f4300` `0x102f4300`

_263 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c820;
extern unsigned int g_1038c824;

unsigned int sub_102f4300(int a0)
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
    v10 = _INSERT(_INSERT(v7, 1, 0), 0, 122);
    v11 = _INSERT(v0, 0, (char)v0 & (char)~(~(v10)) + 6);
    v2 = -(0 < v11) + 1;
    v3 = _INSERT(-(0 < v11) + 1, 0, -(0 < v11) + 1 == -(0 < (v4 & 0xfc00)) + 1);
    v5 = (g_1038c820 ^ g_1038c824) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f1250(v5);
}
```

## `sub_102f4410` `0x102f4410`

_438 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c810;
extern unsigned int g_1038c814;

unsigned int sub_102f4410(int a0)
{
    unsigned int v8;  // ebx
    unsigned int v9;  // ecx
    unsigned int v18;  // cc_ndep
    unsigned int v19;  // cc_dep1
    unsigned int v20;  // 4313
    unsigned int v24;  // eax
    int v25;  // eax
    int v26;  // eax
    unsigned int v27;  // 4105
    unsigned int v28;  // edx
    unsigned int v30;  // eax
    unsigned short v31;  // bx
    unsigned int v32;  // eax
    unsigned int v33;  // eax
    unsigned int v34;  // eax
    unsigned int v35;  // 4499
    unsigned int v36;  // eax
    unsigned int v11;  // ecx
    unsigned int v39;  // 4500
    unsigned int v42;  // 4119
    unsigned int v43;  // eax
    unsigned int v46;  // 4120
    unsigned int v12;  // ecx
    unsigned int v49;  // 4135
    unsigned int v50;  // eax
    unsigned int v51;  // cc_ndep
    unsigned int v52;  // cc_dep1
    unsigned int v53;  // 4136
    unsigned int v56;  // eax
    unsigned int v13;  // eax
    char v14;  // cl
    unsigned int v15;  // 4294
    unsigned int v16;  // 4300
    unsigned int v17;  // 4306
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x1c]
    unsigned int v4;  // [bp-0x18]
    unsigned int v5;  // [bp-0x10]
    int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]

    v6 = sub_102f0ba0(a0);
    v4 = v8;
    v3 = v9;
    v11 = _INSERT(_INSERT(v9, 1, 0), 0, 101);
    v12 = v11 * 0x1000000 | v11 * 0x100 & 0xff0000 | v11 >> 8 & 0xff00 | v11 >> 24 & 0xff;
    v13 = _INSERT(_INSERT(v6 & 0xffff, 1, 0) & 0xff, 0, ~(~((char)_INSERT(v6 & 0xffff, 1, 0))));
    v14 = (char)v12 * 0 | (char)(v12 >> 24);
    v15 = _ccall(1, (unsigned int)(v14 - 20), 12, 0);
    v16 = _ccall(19, (unsigned int)(v14 - 9), 0, v15);
    v17 = _ccall(19, (unsigned int)(v14 - 10), 0, v16);
    v18 = v17;
    v19 = v14 - 11;
    v20 = _ccall(0, 19, (unsigned int)(v14 - 11), 0, v17);
    v24 = v13 * 0x1000000 | v13 * 0x100 & 0xff0000 | v13 >> 8 & 0xff00 | v13 >> 24 & 0xff;
    v25 = _INSERT((char)v24 * 0 | (char)(v24 >> 24), 0, ((char)v24 * 0 | (char)(v24 >> 24)) & (char)~(~(_INSERT(v14 - 11 CONCAT 0, 0, v14 - 40))) + 3);
    v26 = v25;
    if (!v26)
    {
        v27 = _ccall(0, 15, v26, 0, 0);
        v4 = v28;
        v3 = v8;
        v2 = v6 & 0xffff;
        v30 = _INSERT(v2, 1, 0);
        v31 = _INSERT(_INSERT(*((unsigned short *)((void*)&v8 + 1)), 1, 0), 0, 128);
        v32 = v30 * 0x1000000 | v30 * 0x100 & 0xff0000 | v30 >> 8 & 0xff00 | v30 >> 24 & 0xff;
        v33 = _INSERT((char)v32 * 0 | (char)(v32 >> 24), 0, ((char)v32 * 0 | (char)(v32 >> 24)) & (char)~(~(v31)));
        v4 = -(0 < v33) + 1;
        v3 = v28;
        v2 = v3;
        v0 = 31;
        v1 = v6 & 0xffff;
        v34 = _INSERT((char)v1 & (char)v0 - 31, 1, (char)v1 & (char)v0 - 31 & 246);
        v35 = _ccall(12, 0, (unsigned int)(char)(0 < v34), (unsigned int)(char)(0 < v34));
        v36 = -(0 < v34) + 1;
        v39 = _ccall(0, 21, v36 - 1, 0, v35);
        v42 = _ccall(21, v36 - 1, 0, v35);
        v43 = v36;
        v46 = _ccall(0, 21, v43 - 1, 0, v42);
        v49 = _ccall(21, v43 - 1, 0, v42);
        v50 = v43;
        v51 = v49;
        v52 = v50 - 1;
        v53 = _ccall(0, 21, v50 - 1, 0, v49);
        if (-(0 < v33) + 1 != v50)
            goto LABEL_102f4592;
        v56 = 0;
    }
    else
    {
LABEL_102f4592:
        v56 = 1;
    }
    v5 = v56;
    v7 = (g_1038c810 ^ g_1038c814) * 2;
    if (v5)
        v7 |= 1;
    return sub_102f0a30(v7);
}
```

## `sub_102f45d0` `0x102f45d0`

_463 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c810;
extern unsigned int g_1038c814;

unsigned int sub_102f45d0(unsigned int a0)
{
    unsigned int v9;  // ebx
    unsigned int v18;  // 4295
    unsigned int v19;  // cc_ndep
    unsigned int v20;  // cc_dep1
    unsigned int v21;  // 4302
    unsigned int v25;  // eax
    int v26;  // eax
    int v27;  // eax
    unsigned int v10;  // ecx
    unsigned int v28;  // 4105
    unsigned int v29;  // edx
    unsigned int v31;  // eax
    unsigned int v32;  // 4154
    unsigned short v33;  // bx
    unsigned int v34;  // eax
    unsigned int v35;  // eax
    unsigned short v36;  // ax
    unsigned int v37;  // cc_dep1
    char v38;  // bl
    unsigned int v39;  // 4280
    unsigned int v40;  // 4134
    unsigned int v41;  // cc_ndep
    unsigned int v42;  // cc_dep1
    unsigned int v43;  // 4136
    unsigned int v46;  // eax
    unsigned int v47;  // 4211
    unsigned int v12;  // ecx
    unsigned int v48;  // eax
    unsigned int v51;  // 4212
    unsigned int v54;  // 4119
    unsigned int v55;  // eax
    unsigned int v13;  // ecx
    unsigned int v58;  // 4120
    unsigned int v61;  // 4135
    unsigned int v62;  // eax
    unsigned int v63;  // cc_ndep
    unsigned int v64;  // cc_dep1
    unsigned int v65;  // 4136
    unsigned int v14;  // eax
    unsigned int v68;  // eax
    char v15;  // cl
    unsigned int v16;  // 4283
    unsigned int v17;  // 4289
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v5;  // [bp-0x10]
    int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]

    v3 = a0;
    v6 = sub_102f0ba0(a0);
    v3 = v9;
    v2 = v10;
    v12 = _INSERT(_INSERT(v10, 1, 0), 0, 101);
    v13 = v12 * 0x1000000 | v12 * 0x100 & 0xff0000 | v12 >> 8 & 0xff00 | v12 >> 24 & 0xff;
    v14 = _INSERT(_INSERT(v6 & 0xffff, 1, 0) & 0xff, 0, ~(~((char)_INSERT(v6 & 0xffff, 1, 0))));
    v15 = (char)v13 * 0 | (char)(v13 >> 24);
    v16 = _ccall(1, (unsigned int)(v15 - 20), 12, 0);
    v17 = _ccall(19, (unsigned int)(v15 - 9), 0, v16);
    v18 = _ccall(19, (unsigned int)(v15 - 10), 0, v17);
    v19 = v18;
    v20 = v15 - 11;
    v21 = _ccall(0, 19, (unsigned int)(v15 - 11), 0, v18);
    v25 = v14 * 0x1000000 | v14 * 0x100 & 0xff0000 | v14 >> 8 & 0xff00 | v14 >> 24 & 0xff;
    v26 = _INSERT((char)v25 * 0 | (char)(v25 >> 24), 0, ((char)v25 * 0 | (char)(v25 >> 24)) & (char)~(~(_INSERT(v15 - 11 CONCAT 0, 0, v15 - 40))) + 3);
    v27 = v26;
    if (!v27)
    {
        v28 = _ccall(0, 15, v27, 0, 0);
        v3 = v29;
        v2 = v9;
        v1 = v6 & 0xffff;
        v31 = _INSERT(v1, 1, 0);
        v32 = _ccall(0, 13, 0, 0, 0);
        v33 = _INSERT(_INSERT(*((unsigned short *)((void*)&v9 + 1)), 1, 0), 0, 128);
        v34 = v31 * 0x1000000 | v31 * 0x100 & 0xff0000 | v31 >> 8 & 0xff00 | v31 >> 24 & 0xff;
        v35 = _INSERT((char)v34 * 0 | (char)(v34 >> 24), 0, ((char)v34 * 0 | (char)(v34 >> 24)) & (char)~(~(v33)));
        v3 = -(0 < v35) + 1;
        v36 = v6;
        v2 = v29;
        v37 = v36;
        v1 = v2;
        v0 = 31;
        v38 = v0;
        v39 = _ccall(0, 15, (unsigned int)v36, 0, 0);
        v0 = v36;
        v40 = _ccall(19, (unsigned int)(v38 - 7), 0, (unsigned int)(char)(v38 < 6));
        v41 = v40;
        v42 = v38 - 8;
        v43 = _ccall(0, 19, (unsigned int)(v38 - 8), 0, v40);
        v46 = _INSERT((char)v0 & v38 - 31, 1, (char)v0 & v38 - 31 & 246);
        v47 = _ccall(12, 0, (unsigned int)(char)(0 < v46), (unsigned int)(char)(0 < v46));
        v48 = -(0 < v46) + 1;
        v51 = _ccall(0, 21, v48 - 1, 0, v47);
        v54 = _ccall(21, v48 - 1, 0, v47);
        v55 = v48;
        v58 = _ccall(0, 21, v55 - 1, 0, v54);
        v61 = _ccall(21, v55 - 1, 0, v54);
        v62 = v55;
        v63 = v61;
        v64 = v62 - 1;
        v65 = _ccall(0, 21, v62 - 1, 0, v61);
        if (-(0 < v35) + 1 != v62)
            goto LABEL_102f4777;
        v68 = 0;
    }
    else
    {
LABEL_102f4777:
        v68 = 1;
    }
    v5 = v68;
    v7 = (g_1038c810 ^ g_1038c814) * 2;
    if (v5)
        v7 |= 1;
    return sub_102f0a30(v7);
}
```

## `sub_102f45f0` `0x102f45f0`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f45f0(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f4689` `0x102f4689`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f4689(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f46af` `0x102f46af`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f46af(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f46fc` `0x102f46fc`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f46fc(void)
{
}
```

## `sub_102f4711` `0x102f4711`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f4711(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f4745` `0x102f4745`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f4745(void)
{
}
```

## `sub_102f4754` `0x102f4754`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f4754(void)
{
}
```

## `sub_102f4765` `0x102f4765`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f4765(void)
{
}
```

## `sub_102f47b0` `0x102f47b0`

_185 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c840;
extern unsigned int g_1038c844;

unsigned int sub_102f47b0(int a0)
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

    v4 = sub_102f2940(a0);
    v2 = v6;
    v1 = v7;
    v0 = v4 & 0xffff;
    v9 = _INSERT(v0, 1, 0);
    v10 = _INSERT(_INSERT(*((unsigned short *)((void*)&v7 + 1)), 1, 0), 0, 128);
    v11 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v12 = _INSERT((char)v11 * 0 | (char)(v11 >> 24), 0, ((char)v11 * 0 | (char)(v11 >> 24)) & (char)~(~(v10)));
    v2 = -(0 < v12) + 1;
    v3 = _INSERT(-(0 < v12) + 1, 0, -(0 < v12) + 1 == -(0 < (v4 & 0xf900)) + 1);
    v5 = (g_1038c840 ^ g_1038c844) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f27b0(v5);
}
```

## `sub_102f4870` `0x102f4870`

_229 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e0;
extern unsigned int g_1038c7e4;

int sub_102f4870(unsigned int a0)
{
    unsigned int v7;  // ebx
    unsigned int v16;  // 4291
    unsigned int v17;  // cc_ndep
    unsigned int v18;  // cc_dep1
    unsigned int v19;  // 4298
    unsigned int v23;  // eax
    unsigned int v24;  // eax
    unsigned int v8;  // ecx
    unsigned int v10;  // ecx
    unsigned int v11;  // ecx
    unsigned int v12;  // eax
    char v13;  // cl
    unsigned int v14;  // 4279
    unsigned int v15;  // 4285
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v1 = a0;
    v4 = sub_102ef270(a0);
    v1 = v7;
    v0 = v8;
    v10 = _INSERT(_INSERT(v8, 1, 0), 0, 101);
    v11 = v10 * 0x1000000 | v10 * 0x100 & 0xff0000 | v10 >> 8 & 0xff00 | v10 >> 24 & 0xff;
    v12 = _INSERT(_INSERT(v4 & 0xffff, 1, 0) & 0xff, 0, ~(~((char)_INSERT(v4 & 0xffff, 1, 0))));
    v13 = (char)v11 * 0 | (char)(v11 >> 24);
    v14 = _ccall(1, (unsigned int)(v13 - 20), 12, 0);
    v15 = _ccall(19, (unsigned int)(v13 - 9), 0, v14);
    v16 = _ccall(19, (unsigned int)(v13 - 10), 0, v15);
    v17 = v16;
    v18 = v13 - 11;
    v19 = _ccall(0, 19, (unsigned int)(v13 - 11), 0, v16);
    v23 = v12 * 0x1000000 | v12 * 0x100 & 0xff0000 | v12 >> 8 & 0xff00 | v12 >> 24 & 0xff;
    v24 = _INSERT((char)v23 * 0 | (char)(v23 >> 24), 0, ((char)v23 * 0 | (char)(v23 >> 24)) & (char)~(~(_INSERT(v13 - 11 CONCAT 0, 0, v13 - 40))) + 3);
    v3 = -(-(0 < v24));
    v5 = (g_1038c7e0 ^ g_1038c7e4) * 2;
    if (v3)
        v5 |= 1;
    return sub_102ef140(v5);
}
```

## `sub_102f4890` `0x102f4890`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f4890(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f4960` `0x102f4960`

_209 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c834;
extern unsigned int g_1038c838;

int sub_102f4960(unsigned int a0)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // ecx
    unsigned int v9;  // 4304
    unsigned int v13;  // eax
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f2170(a0);
    v2 = v6;
    v1 = v7;
    v0 = _INSERT(v4 & 0xffff, 1, 0);
    v9 = _ccall(0, 19, 90, 0, 0);
    v13 = _INSERT(v0, 0, (char)v0 & (char)~(~(_INSERT(90 CONCAT 0, 0, 64))));
    v3 = -(-(0 < v13));
    v5 = (g_1038c834 ^ g_1038c838) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f2010(v5);
}
```

## `sub_102f49c3` `0x102f49c3`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f49c3(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f4a40` `0x102f4a40`

_154 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c818;
extern unsigned int g_1038c81c;

unsigned int sub_102f4a40(int a0)
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

    v5 = sub_102f0f30(a0);
    v7 = v5;
    v3 = v8;
    v9 = v7;
    v2 = v10;
    v0 = 15;
    v11 = _ccall(0, 15, (unsigned int)v7, 0, 0);
    v1 = v7;
    v4 = -(0 < _INSERT((char)v1 & (char)v0 - 15, 1, (char)v1 & (char)v0 - 15 & 225)) + 1;
    v6 = (g_1038c818 ^ g_1038c81c) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f0e70(v6);
}
```

## `sub_102f4a6c` `0x102f4a6c`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f4a6c(void)
{
}
```

## `sub_102f4ae0` `0x102f4ae0`

_121 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c83c;
extern unsigned int g_1038c840;

unsigned int sub_102f4ae0(int a0)
{
    unsigned int v5;  // ebx
    unsigned int v6;  // ecx
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v3 = sub_102f2690(a0);
    v1 = v5;
    v0 = v6;
    v2 = 1;
    v4 = (g_1038c83c ^ g_1038c840) * 2;
    if (v2)
        v4 |= 1;
    return sub_102f2570(v4);
}
```

## `sub_102f4b02` `0x102f4b02`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102f4b02(void)
{
}
```

## `sub_102f4b60` `0x102f4b60`

_210 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c814;
extern unsigned int g_1038c818;

unsigned int sub_102f4b60(int a0)
{
    unsigned int v7;  // edx
    unsigned int v8;  // ebx
    unsigned int v9;  // ecx
    int v0;  // [bp-0x2c]
    unsigned int v1;  // [bp-0x28]
    unsigned int v2;  // [bp-0x24]
    int v3;  // [bp-0x20], Other Possible Types: unsigned int
    unsigned int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v5 = sub_102f0dc0(a0);
    v3 = v5;
    v3 = v7;
    v2 = v8;
    v1 = v9;
    v0 = v5;
    v4 = -(0 < _INSERT(_INSERT(v0, 1, 0) & 0xff, 0, (char)_INSERT(v0, 1, 0) & 1)) + 1;
    v6 = (g_1038c814 ^ g_1038c818) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f0d10(v6);
}
```

## `sub_102f4c40` `0x102f4c40`

_139 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c80c;
extern unsigned int g_1038c810;

unsigned int sub_102f4c40(int a0)
{
    unsigned int v4;  // cc_ndep
    unsigned int v5;  // 4129
    unsigned int v9;  // eax
    unsigned int v10;  // eax
    int v0;  // [bp-0x18]
    int <0x102f4c40[is_2]|Stack bp-0x10, 1 B>;  // [bp-0x10]
    unsigned int v1;  // [bp-0x10]
    int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v2 = sub_102f0940(a0);
    v4 = &<0x102f4c40[is_2]|Stack bp-0x10, 1 B> < &/* unsupported instruction */;
    v5 = _ccall(0, 19, 5, 0, (unsigned int)(char)(&<0x102f4c40[is_2]|Stack bp-0x10, 1 B> < &/* unsupported instruction */));
    v0 = v2;
    v9 = _INSERT(_INSERT(v0, 0, (char)v0 & 1), 1, ~(0));
    v10 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v1 = -(0 < _INSERT((char)v10 * 0 | (char)(v10 >> 24), 1, ~((char)v10 * 0 | (char)(v10 >> 24)))) + 1;
    v3 = (g_1038c80c ^ g_1038c810) * 2;
    if (v1)
        v3 |= 1;
    return sub_102f0850(v3);
}
```

## `sub_102f4c64` `0x102f4c64`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f4c64(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f4cd0` `0x102f4cd0`

_173 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7d8;
extern unsigned int g_1038c7dc;

unsigned int sub_102f4cd0(int a0)
{
    unsigned int v6;  // edx
    unsigned int v7;  // ebx
    unsigned int v17;  // 4135
    unsigned int v20;  // 4119
    unsigned int v21;  // eax
    unsigned int v24;  // 4120
    unsigned int v8;  // eax
    unsigned int v27;  // 4135
    unsigned int v28;  // eax
    unsigned int v29;  // cc_ndep
    unsigned int v30;  // cc_dep1
    unsigned int v31;  // 4136
    unsigned int v9;  // 4108
    unsigned int v10;  // cc_dep1
    unsigned int v11;  // 4108
    unsigned int v12;  // 4133
    unsigned int v13;  // 4134
    unsigned int v14;  // eax
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102eed50(a0);
    v2 = v6;
    v1 = v7;
    v0 = 2;
    v8 = _INSERT((char)v4 & (char)v0 - 2, 1, (char)v4 & (char)v0 - 2 & 8);
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
    v13 = _ccall(12, 0, v12 & 1, v12 & 1);
    v14 = -(v12 & 1) + 1;
    v17 = _ccall(0, 21, v14 - 1, 0, v13);
    v20 = _ccall(21, v14 - 1, 0, v13);
    v21 = v14;
    v24 = _ccall(0, 21, v21 - 1, 0, v20);
    v27 = _ccall(21, v21 - 1, 0, v20);
    v28 = v21;
    v29 = v27;
    v30 = v28 - 1;
    v31 = _ccall(0, 21, v28 - 1, 0, v27);
    v3 = v28;
    v5 = (g_1038c7d8 ^ g_1038c7dc) * 2;
    if (v3)
        v5 |= 1;
    return sub_102eebb0(v5);
}
```

## `sub_102f4d29` `0x102f4d29`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f4d29(void)
{
}
```

## `sub_102f4d38` `0x102f4d38`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f4d38(void)
{
}
```

## `sub_102f4d49` `0x102f4d49`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f4d49(void)
{
}
```

## `sub_102f4d90` `0x102f4d90`

_480 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c80c;
extern unsigned int g_1038c810;

unsigned int sub_102f4d90(unsigned int a0)
{
    unsigned int v9;  // ebx
    unsigned int v18;  // 4291
    unsigned int v19;  // cc_ndep
    unsigned int v20;  // cc_dep1
    unsigned int v21;  // 4298
    unsigned int v25;  // eax
    int v26;  // eax
    int v27;  // eax
    unsigned int v10;  // ecx
    unsigned int v28;  // 4105
    unsigned int v29;  // edx
    unsigned int v31;  // eax
    unsigned int v32;  // 4206
    unsigned short v33;  // bx
    unsigned int v34;  // eax
    unsigned int v35;  // eax
    unsigned short v36;  // ax
    unsigned int v37;  // cc_dep1
    char v38;  // bl
    unsigned int v39;  // 4280
    unsigned int v40;  // 4142
    unsigned int v41;  // 4144
    unsigned int v42;  // cc_ndep
    unsigned int v43;  // cc_dep1
    unsigned int v44;  // 4146
    unsigned int v47;  // eax
    unsigned int v12;  // ecx
    unsigned int v48;  // 4211
    unsigned int v49;  // eax
    unsigned int v52;  // 4212
    unsigned int v55;  // 4119
    unsigned int v56;  // eax
    unsigned int v13;  // ecx
    unsigned int v59;  // 4120
    unsigned int v62;  // 4135
    unsigned int v63;  // eax
    unsigned int v64;  // cc_ndep
    unsigned int v65;  // cc_dep1
    unsigned int v66;  // 4136
    unsigned int v14;  // eax
    unsigned int v69;  // eax
    char v15;  // cl
    unsigned int v16;  // 4279
    unsigned int v17;  // 4285
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v5;  // [bp-0x10]
    int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]

    v3 = a0;
    v6 = sub_102f0940(a0);
    v3 = v9;
    v2 = v10;
    v12 = _INSERT(_INSERT(v10, 1, 0), 0, 101);
    v13 = v12 * 0x1000000 | v12 * 0x100 & 0xff0000 | v12 >> 8 & 0xff00 | v12 >> 24 & 0xff;
    v14 = _INSERT(_INSERT(v6 & 0xffff, 1, 0) & 0xff, 0, ~(~((char)_INSERT(v6 & 0xffff, 1, 0))));
    v15 = (char)v13 * 0 | (char)(v13 >> 24);
    v16 = _ccall(1, (unsigned int)(v15 - 20), 12, 0);
    v17 = _ccall(19, (unsigned int)(v15 - 9), 0, v16);
    v18 = _ccall(19, (unsigned int)(v15 - 10), 0, v17);
    v19 = v18;
    v20 = v15 - 11;
    v21 = _ccall(0, 19, (unsigned int)(v15 - 11), 0, v18);
    v25 = v14 * 0x1000000 | v14 * 0x100 & 0xff0000 | v14 >> 8 & 0xff00 | v14 >> 24 & 0xff;
    v26 = _INSERT((char)v25 * 0 | (char)(v25 >> 24), 0, ((char)v25 * 0 | (char)(v25 >> 24)) & (char)~(~(_INSERT(v15 - 11 CONCAT 0, 0, v15 - 40))) + 3);
    v27 = v26;
    if (!v27)
    {
        v28 = _ccall(0, 15, v27, 0, 0);
        v3 = v29;
        v2 = v9;
        v1 = v6 & 0xffff;
        v31 = _INSERT(v1, 1, 0);
        v32 = _ccall(0, 13, 0, 0, 0);
        v33 = _INSERT(_INSERT(*((unsigned short *)((void*)&v9 + 1)), 1, 0), 0, 128);
        v34 = v31 * 0x1000000 | v31 * 0x100 & 0xff0000 | v31 >> 8 & 0xff00 | v31 >> 24 & 0xff;
        v35 = _INSERT((char)v34 * 0 | (char)(v34 >> 24), 0, ((char)v34 * 0 | (char)(v34 >> 24)) & (char)~(~(v33)));
        v3 = -(0 < v35) + 1;
        v36 = v6;
        v2 = v29;
        v37 = v36;
        v1 = v2;
        v0 = 31;
        v38 = v0;
        v39 = _ccall(0, 15, (unsigned int)v36, 0, 0);
        v0 = v36;
        v40 = _ccall(19, (unsigned int)(v38 - 6), 0, (unsigned int)(char)(v38 < 5));
        v41 = _ccall(19, (unsigned int)(v38 - 7), 0, v40);
        v42 = v41;
        v43 = v38 - 8;
        v44 = _ccall(0, 19, (unsigned int)(v38 - 8), 0, v41);
        v47 = _INSERT((char)v0 & v38 - 31, 1, (char)v0 & v38 - 31 & 246);
        v48 = _ccall(12, 0, (unsigned int)(char)(0 < v47), (unsigned int)(char)(0 < v47));
        v49 = -(0 < v47) + 1;
        v52 = _ccall(0, 21, v49 - 1, 0, v48);
        v55 = _ccall(21, v49 - 1, 0, v48);
        v56 = v49;
        v59 = _ccall(0, 21, v56 - 1, 0, v55);
        v62 = _ccall(21, v56 - 1, 0, v55);
        v63 = v56;
        v64 = v62;
        v65 = v63 - 1;
        v66 = _ccall(0, 21, v63 - 1, 0, v62);
        if (-(0 < v35) + 1 != v63)
            goto LABEL_102f4f47;
        v69 = 1;
    }
    else
    {
LABEL_102f4f47:
        v69 = 0;
    }
    v5 = v69;
    v7 = (g_1038c80c ^ g_1038c810) * 2;
    if (v5)
        v7 |= 1;
    return sub_102f0850(v7);
}
```

