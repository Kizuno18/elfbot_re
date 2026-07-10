# elfbot.dll decompiled — jiru 0x102fc39e..0x102fd8b2

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_102fc39e` `0x102fc39e`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fc39e(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fc3eb` `0x102fc3eb`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fc3eb(void)
{
}
```

## `sub_102fc402` `0x102fc402`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fc402(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fc436` `0x102fc436`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fc436(void)
{
}
```

## `sub_102fc445` `0x102fc445`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fc445(void)
{
}
```

## `sub_102fc456` `0x102fc456`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fc456(void)
{
}
```

## `sub_102fc4b0` `0x102fc4b0`

_228 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7ec;
extern unsigned int g_1038c7f0;

int sub_102fc4b0(unsigned int a0)
{
    unsigned int v5;  // ecx
    unsigned int v6;  // eax
    unsigned int v15;  // eax
    char v7;  // cl
    unsigned int v8;  // ecx
    unsigned int v9;  // edx
    int v10;  // edx
    unsigned int v11;  // 4484
    unsigned int v13;  // 4104
    unsigned int v14;  // 4104
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v3 = sub_102ef8d0(a0);
    v1 = v5;
    v6 = v3 * 0x1000000 | v3 * 0x100 & 0xff0000 | v3 >> 8 & 0xff00 | v3 >> 24 & 0xff;
    v7 = (char)(~(~(65)) + 25) + 3;
    v8 = _INSERT(v7 + 15, 0, v7 + 18);
    v0 = v9;
    v2 = -(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 0x11)) + 1;
    v10 = -(0 < (v3 & 0xf900)) + 1;
    v11 = _ccall(0, 15, 0, 0, 0);
    v13 = _ccall(0, 6, -((unsigned int)(char)(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 0x11))) + 1, v10, 0);
    if (-(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 0x11)) + 1 != v10)
    {
        v14 = _ccall(0, 15, 0, 0, 0);
        v15 = 1;
    }
    else
    {
        v15 = 0;
    }
    v2 = v15;
    v4 = (g_1038c7ec ^ g_1038c7f0) * 2;
    if (v15)
        v4 |= 1;
    return sub_102ef750(v4);
}
```

## `sub_102fc5a0` `0x102fc5a0`

_185 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c824;
extern unsigned int g_1038c828;

int sub_102fc5a0(unsigned int a0)
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

    v3 = sub_102f1670(a0);
    v1 = v5;
    v6 = v3 * 0x1000000 | v3 * 0x100 & 0xff0000 | v3 >> 8 & 0xff00 | v3 >> 24 & 0xff;
    v7 = ((char)~(~(75)) ^ 25) + 3;
    v8 = _INSERT(v7 + 5, 0, v7 + 8);
    v0 = v9;
    v2 = -(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 35)) + 1;
    v2 = _INSERT(-(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 35)) + 1, 0, -(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 35)) + 1 == -(0 < (v3 & 64000)) + 1);
    v4 = (g_1038c824 ^ g_1038c828) * 2;
    if (v2)
        v4 |= 1;
    return sub_102f14d0(v4);
}
```

## `sub_102fc660` `0x102fc660`

_162 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c834;
extern unsigned int g_1038c838;

int sub_102fc660(unsigned int a0)
{
    unsigned short v6;  // ax
    unsigned int v7;  // edx
    unsigned int v16;  // 4146
    unsigned int v8;  // cc_dep1
    unsigned int v9;  // ebx
    char v10;  // bl
    unsigned int v11;  // 4130
    unsigned int v12;  // 4142
    unsigned int v13;  // 4144
    unsigned int v14;  // cc_ndep
    unsigned int v15;  // cc_dep1
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f2170(a0);
    v6 = v4;
    v2 = v7;
    v8 = v6;
    v1 = v9;
    v0 = 31;
    v10 = v0;
    v11 = _ccall(0, 15, (unsigned int)v6, 0, 0);
    v0 = v6;
    v12 = _ccall(19, (unsigned int)(v10 - 6), 0, (unsigned int)(char)(v10 < 5));
    v13 = _ccall(19, (unsigned int)(v10 - 7), 0, v12);
    v14 = v13;
    v15 = v10 - 8;
    v16 = _ccall(0, 19, (unsigned int)(v10 - 8), 0, v13);
    v3 = -(-(0 < _INSERT((char)v0 & v10 - 31, 1, (char)v0 & v10 - 31 & 246)));
    v5 = (g_1038c834 ^ g_1038c838) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f2010(v5);
}
```

## `sub_102fc68c` `0x102fc68c`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fc68c(void)
{
}
```

## `sub_102fc6a3` `0x102fc6a3`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fc6a3(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fc710` `0x102fc710`

_166 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c830;
extern unsigned int g_1038c834;

int sub_102fc710(unsigned int a0)
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

    v4 = sub_102f1e90(a0);
    v2 = v6;
    v1 = v7;
    v0 = v4 & 0xffff;
    v9 = _INSERT(v0, 1, 0);
    v10 = _INSERT(_INSERT(*((unsigned short *)((void*)&v7 + 1)), 1, 0), 0, 64);
    v11 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v12 = _INSERT((char)v11 * 0 | (char)(v11 >> 24), 0, ((char)v11 * 0 | (char)(v11 >> 24)) & (char)~(~(v10)));
    v3 = -(-(0 < v12));
    v5 = (g_1038c830 ^ g_1038c834) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f1d10(v5);
}
```

## `sub_102fc7c0` `0x102fc7c0`

_182 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7fc;
extern unsigned int g_1038c800;

unsigned int sub_102fc7c0(unsigned int a0, unsigned int a1, unsigned int a2, int a3)
{
    unsigned int v7;  // ebx
    unsigned int v8;  // esi
    unsigned int v17;  // 4151
    unsigned int v18;  // eax
    unsigned int v19;  // 4149
    unsigned int v9;  // edi
    unsigned int v10;  // 4129
    unsigned int v11;  // 4143
    unsigned int v12;  // 4144
    unsigned int v13;  // cc_ndep
    unsigned int v14;  // 4145
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v3 = v7;
    v2 = v8;
    v1 = v9;
    v10 = _ccall(0, 6, &/* unsupported instruction */, 8, 0);
    v0 = a0;
    v11 = _ccall(19, 14, 0, 0);
    v12 = _ccall(19, 13, 0, v11);
    v13 = v12;
    v14 = _ccall(0, 19, 12, 0, v12);
    v17 = _ccall(0, 15, a3, 0, 0);
    if (a3)
    {
        v18 = 0;
        v19 = _ccall(0, 15, 0, 0, 0);
    }
    else
    {
        v18 = 1;
    }
    v4 = v18;
    v5 = (g_1038c7fc ^ g_1038c800) * 2;
    if (v4)
        v5 |= 1;
    return sub_102f0130(v5);
}
```

## `sub_102fc7d3` `0x102fc7d3`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fc7d3(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fc7f1` `0x102fc7f1`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fc7f1(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fc80a` `0x102fc80a`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fc80a(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fc826` `0x102fc826`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fc826(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fc880` `0x102fc880`

_161 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7f4;
extern unsigned int g_1038c7f8;

unsigned int sub_102fc880(int a0)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // ecx
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

    v4 = sub_102efd90(a0);
    v2 = v6;
    v1 = v7;
    v0 = 4;
    v8 = _INSERT((char)v4 & (char)v0 - 4, 1, (char)v4 & (char)v0 - 4 & 8);
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
    v5 = (g_1038c7f4 ^ g_1038c7f8) * 2;
    if (v3)
        v5 |= 1;
    return sub_102efcf0(v5);
}
```

## `sub_102fc930` `0x102fc930`

_197 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c838;
extern unsigned int g_1038c83c;

int sub_102fc930(unsigned int a0)
{
    unsigned int v8;  // edx
    unsigned int v9;  // ebx
    unsigned int v11;  // eax
    unsigned int v12;  // 4222
    unsigned short v13;  // bx
    unsigned int v14;  // eax
    unsigned int v15;  // 4191
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v2 = a0;
    v5 = sub_102f2420(a0);
    v2 = v8;
    v1 = v9;
    v0 = v5 & 0xffff;
    v11 = _INSERT(v0, 1, 0);
    v12 = _ccall(0, 13, 0, 0, 0);
    v13 = _INSERT(_INSERT(*((unsigned short *)((void*)&v9 + 1)), 1, 0), 0, 128);
    v14 = v11 * 0x1000000 | v11 * 0x100 & 0xff0000 | v11 >> 8 & 0xff00 | v11 >> 24 & 0xff;
    v15 = _ccall(0, 4, 159, 31, 0);
    v16 = _INSERT((char)v14 * 0 | (char)(v14 >> 24), 0, ((char)v14 * 0 | (char)(v14 >> 24)) & (char)~(~(v13)));
    v4 = -(-(0 < v16));
    v6 = (g_1038c838 ^ g_1038c83c) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f22d0(v6);
}
```

## `sub_102fc950` `0x102fc950`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fc950(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fc985` `0x102fc985`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fc985(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fc9b2` `0x102fc9b2`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fc9b2(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fca00` `0x102fca00`

_144 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e8;
extern unsigned int g_1038c7ec;

unsigned int sub_102fca00(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v2;  // cc_dep1
    unsigned int v3;  // 4132
    unsigned int v4;  // eax
    unsigned int v5;  // 4143
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v2 = a0 & 0x800;
    v3 = _ccall(0, 15, a0 & 0x800, 0, 0);
    if (a1)
    {
        v4 = 0;
    }
    else
    {
        v5 = _ccall(0, 4, 251, 8, 0);
        v4 = 1;
    }
    v0 = v4;
    v1 = (g_1038c7e8 ^ g_1038c7ec) * 2;
    if (v0)
        v1 |= 1;
    return sub_102ef530(v1);
}
```

## `sub_102fca18` `0x102fca18`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fca18(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fca4e` `0x102fca4e`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fca4e(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fcaa0` `0x102fcaa0`

_193 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c838;
extern unsigned int g_1038c83c;

int sub_102fcaa0(unsigned int a0)
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

    v4 = sub_102f2420(a0);
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
    v5 = (g_1038c838 ^ g_1038c83c) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f22d0(v5);
}
```

## `sub_102fcb0d` `0x102fcb0d`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fcb0d(void)
{
}
```

## `sub_102fcb1c` `0x102fcb1c`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fcb1c(void)
{
}
```

## `sub_102fcb70` `0x102fcb70`

_144 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7fc;
extern unsigned int g_1038c800;

unsigned int sub_102fcb70(int a0)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // ecx
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

    v4 = sub_102f02b0(a0);
    v2 = v6;
    v1 = v7;
    v0 = 4;
    v8 = _INSERT((char)v4 & (char)v0 - 4, 1, (char)v4 & (char)v0 - 4 & 8);
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
    v5 = (g_1038c7fc ^ g_1038c800) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0130(v5);
}
```

## `sub_102fcc00` `0x102fcc00`

_207 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c808;
extern unsigned int g_1038c80c;

unsigned int sub_102fcc00(int a0)
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

    v3 = sub_102f07c0(a0);
    v1 = v5;
    v0 = v6;
    v8 = _INSERT(_INSERT(v6, 1, 0), 0, 101);
    v9 = v8 * 0x1000000 | v8 * 0x100 & 0xff0000 | v8 >> 8 & 0xff00 | v8 >> 24 & 0xff;
    v10 = _INSERT(_INSERT(v3 & 0xffff, 1, 0) & 0xff, 0, ~(~((char)_INSERT(v3 & 0xffff, 1, 0))));
    v12 = v10 * 0x1000000 | v10 * 0x100 & 0xff0000 | v10 >> 8 & 0xff00 | v10 >> 24 & 0xff;
    v13 = _INSERT((char)v12 * 0 | (char)(v12 >> 24), 0, ((char)v12 * 0 | (char)(v12 >> 24)) & (char)~(~(_INSERT(((char)v9 * 0 | (char)(v9 >> 24)) - 2 CONCAT 0, 0, ((char)v9 * 0 | (char)(v9 >> 24)) - 39))) + 3);
    v2 = -(0 < v13) + 1;
    v4 = (g_1038c808 ^ g_1038c80c) * 2;
    if (v2)
        v4 |= 1;
    return sub_102f0730(v4);
}
```

## `sub_102fcc5a` `0x102fcc5a`

_3 bytes. (leaf/helper — see body)_

```c
int sub_102fcc5a(void)
{
}
```

## `sub_102fcce0` `0x102fcce0`

_213 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c820;
extern unsigned int g_1038c824;

unsigned int sub_102fcce0(int a0)
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
    v8 = _INSERT(_INSERT(v6, 1, 0), 0, 165);
    v9 = v8 * 0x1000000 | v8 * 0x100 & 0xff0000 | v8 >> 8 & 0xff00 | v8 >> 24 & 0xff;
    v10 = _INSERT(_INSERT(v3 & 0xffff, 1, 0) & 0xff, 0, ~(~((char)_INSERT(v3 & 0xffff, 1, 0))));
    v12 = v10 * 0x1000000 | v10 * 0x100 & 0xff0000 | v10 >> 8 & 0xff00 | v10 >> 24 & 0xff;
    v13 = _INSERT((char)v12 * 0 | (char)(v12 >> 24), 0, ((char)v12 * 0 | (char)(v12 >> 24)) & (char)~(~(_INSERT((char)v9 * 0 | (char)(v9 >> 24), 0, ((char)v9 * 0 | (char)(v9 >> 24)) - 40))) + 3);
    v2 = -(-(0 < v13));
    v4 = (g_1038c820 ^ g_1038c824) * 2;
    if (v2)
        v4 |= 1;
    return sub_102f1250(v4);
}
```

## `sub_102fcdc0` `0x102fcdc0`

_226 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7dc;
extern unsigned int g_1038c7e0;

unsigned int sub_102fcdc0(int a0)
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
    v10 = _INSERT(_INSERT(*((unsigned short *)((void*)&v7 + 1)), 1, 0), 0, 64);
    v11 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v12 = _INSERT((char)v11 * 0 | (char)(v11 >> 24), 0, ((char)v11 * 0 | (char)(v11 >> 24)) & (char)~(~(v10)));
    v3 = -(0 < v12) + 1;
    v5 = (g_1038c7dc ^ g_1038c7e0) * 2;
    if (v3)
        v5 |= 1;
    return sub_102eef00(v5);
}
```

## `sub_102fceb0` `0x102fceb0`

_204 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7f4;
extern unsigned int g_1038c7f8;

unsigned int sub_102fceb0(int a0)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // ecx
    unsigned int v9;  // 4290
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
    v9 = _ccall(0, 4, 109, 19, 0);
    v11 = _INSERT(v0, 0, (char)v0 & (char)~(~(_INSERT(90 CONCAT 0, 0, 64))));
    v3 = -(0 < v11) + 1;
    v5 = (g_1038c7f4 ^ g_1038c7f8) * 2;
    if (v3)
        v5 |= 1;
    return sub_102efcf0(v5);
}
```

## `sub_102fcf11` `0x102fcf11`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fcf11(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fcf80` `0x102fcf80`

_178 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e0;
extern unsigned int g_1038c7e4;

int sub_102fcf80(unsigned int a0)
{
    unsigned int v6;  // edx
    unsigned int v7;  // ebx
    unsigned int v16;  // 4191
    unsigned int v17;  // 4193
    unsigned int v18;  // cc_ndep
    unsigned int v19;  // 4195
    char v8;  // bl
    unsigned int v9;  // cc_ndep
    unsigned int v10;  // cc_dep1
    unsigned int v11;  // 4214
    unsigned int v14;  // 4187
    unsigned int v15;  // 4189
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102ef270(a0);
    v2 = v6;
    v1 = v7;
    v0 = 0xd00;
    v8 = v0;
    v0 = v4 & 0xffff;
    v9 = v8 - 9 < 3;
    v10 = v8 - 13;
    v11 = _ccall(0, 19, (unsigned int)(v8 - 13), 0, (unsigned int)(char)(v8 - 9 < 3));
    v14 = _ccall(19, 8, 0, 0);
    v15 = _ccall(19, 7, 0, v14);
    v16 = _ccall(19, 6, 0, v15);
    v17 = _ccall(19, 5, 0, v16);
    v18 = v17;
    v19 = _ccall(0, 19, 4, 0, v17);
    v3 = -(-(0 < _INSERT(_INSERT(v0, 1, *((char *)((void*)&v0 + 1)) & v8 - 13) & 0xff, 0, (char)_INSERT(v0, 1, *((char *)((void*)&v0 + 1)) & v8 - 13) & 4)));
    v5 = (g_1038c7e0 ^ g_1038c7e4) * 2;
    if (v3)
        v5 |= 1;
    return sub_102ef140(v5);
}
```

## `sub_102fcfc8` `0x102fcfc8`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fcfc8(void)
{
}
```

## `sub_102fcff2` `0x102fcff2`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fcff2(void)
{
}
```

## `sub_102fd040` `0x102fd040`

_176 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c818;
extern unsigned int g_1038c81c;

unsigned int sub_102fd040(int a0, unsigned int a1)
{
    unsigned int v9;  // ebx
    unsigned int v10;  // esi
    unsigned int v11;  // edi
    unsigned int v12;  // edx
    unsigned int v13;  // 4154
    unsigned int v14;  // 4156
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x1c]
    unsigned int v4;  // [bp-0x18]
    unsigned int v5;  // [bp-0x14]
    unsigned int v6;  // [bp-0x10]
    int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]

    v5 = v9;
    v4 = v10;
    v3 = v11;
    v7 = sub_102f0f30(a0);
    v2 = v12;
    v1 = v9;
    v0 = v7 & 0xffff;
    v13 = _ccall(4, 19, (unsigned int)(*((char *)((void*)&v9 + 1)) - 1), 0, 0);
    if (Conv(32I->1I, vvar_128)) { Goto None } else { Goto None }
    v14 = _ccall(0, 15, v0 & 0x800, 0, 0);
    if (Conv(32I->1I, vvar_129)) { Goto None } else { Goto None }
    v6 = 1;
    v8 = (g_1038c818 ^ g_1038c81c) * 2;
    if (v6)
        v8 |= 1;
    return sub_102f0e70(v8);
}
```

## `sub_102fd0f0` `0x102fd0f0`

_381 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c820;
extern unsigned int g_1038c824;

unsigned int sub_102fd0f0(int a0)
{
    unsigned int v7;  // ebx
    unsigned int v8;  // ecx
    unsigned int v18;  // eax
    unsigned short v19;  // bx
    unsigned int v20;  // eax
    unsigned int v21;  // eax
    unsigned int v22;  // eax
    unsigned int v23;  // 4108
    unsigned int v24;  // cc_dep1
    unsigned int v25;  // 4108
    unsigned int v26;  // 4126
    unsigned int v27;  // eax
    unsigned int v10;  // edx
    unsigned int v11;  // edx
    unsigned int v12;  // 4304
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v5 = sub_102f1390(a0);
    v3 = v7;
    v2 = v8;
    v11 = v10 * 0x1000000 | v10 * 0x100 & 0xff0000 | v10 >> 8 & 0xff00 | v10 >> 24 & 0xff;
    v1 = _INSERT(v5 & 0xffff, 1, 0);
    v12 = _ccall(0, 19, 90, 0, 0);
    v16 = _INSERT(v1, 0, (char)v1 & (char)~(~(_INSERT(90 CONCAT 0, 0, 64))));
    if (!v16)
    {
        v3 = v11 * 0x1000000 | v11 * 0x100 & 0xff0000 | v11 >> 8 & 0xff00 | v11 >> 24 & 0xff;
        v2 = v7;
        v1 = v5 & 0xffff;
        v18 = _INSERT(v1, 1, 0);
        v19 = _INSERT(_INSERT(*((unsigned short *)((void*)&v7 + 1)), 1, 0), 0, 128);
        v20 = v18 * 0x1000000 | v18 * 0x100 & 0xff0000 | v18 >> 8 & 0xff00 | v18 >> 24 & 0xff;
        v21 = _INSERT((char)v20 * 0 | (char)(v20 >> 24), 0, ((char)v20 * 0 | (char)(v20 >> 24)) & (char)~(~(v19)));
        v3 = -(0 < v21) + 1;
        v1 = -(0 < v21) + 1;
        v0 = 4;
        v22 = _INSERT((char)v5 & (char)v0 - 4, 1, (char)v5 & (char)v0 - 4 & 8);
        if (v22)
        {
            v23 = _ccall(3, ~(v22), 1, 0);
            v24 = v23 | 1;
        }
        else
        {
            v25 = _ccall(3, ~(0), 1, 0);
            v24 = v25 & 4294967294;
        }
        v26 = _ccall(0, v24, 0, 0);
        if (v1 != -(v26 & 1) + 1)
            goto LABEL_102fd235;
        v27 = 0;
    }
    else
    {
LABEL_102fd235:
        v27 = 1;
    }
    v4 = v27;
    v6 = (g_1038c820 ^ g_1038c824) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f1250(v6);
}
```

## `sub_102fd153` `0x102fd153`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fd153(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fd270` `0x102fd270`

_173 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c80c;
extern unsigned int g_1038c810;

unsigned int sub_102fd270(int a0)
{
    unsigned int v5;  // ecx
    unsigned int v6;  // eax
    char v7;  // cl
    char v8;  // dl
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v3 = sub_102f0940(a0);
    v1 = v5;
    v6 = v3 * 0x1000000 | v3 * 0x100 & 0xff0000 | v3 >> 8 & 0xff00 | v3 >> 24 & 0xff;
    v7 = (char)(~(~(10)) + 12) + 1;
    v0 = _INSERT(v8 - 8, 0, v8 - 9);
    v2 = -(-(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & _INSERT(v7 + 22, 0, v7 + 27) + 14)));
    v4 = (g_1038c80c ^ g_1038c810) * 2;
    if (v2)
        v4 |= 1;
    return sub_102f0850(v4);
}
```

## `sub_102fd320` `0x102fd320`

_144 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c844;
extern unsigned int g_1038c848;

unsigned int sub_102fd320(unsigned int a0)
{
    unsigned int v5;  // edx
    unsigned int v14;  // 4172
    unsigned int v15;  // 4178
    unsigned int v16;  // cc_ndep
    unsigned int v17;  // 4185
    unsigned int v21;  // eax
    unsigned int v6;  // 4124
    unsigned int v7;  // 4130
    unsigned int v8;  // 4136
    unsigned int v9;  // 4142
    unsigned int v10;  // 4148
    unsigned int v11;  // 4154
    unsigned int v12;  // 4160
    unsigned int v13;  // 4166
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v0 = a0;
    v2 = sub_102f2b60(a0);
    v0 = v5;
    v6 = _ccall(3, &v0, 4, 0);
    v7 = _ccall(19, 13, 0, v6);
    v8 = _ccall(19, 12, 0, v7);
    v9 = _ccall(19, 11, 0, v8);
    v10 = _ccall(19, 10, 0, v9);
    v11 = _ccall(19, 9, 0, v10);
    v12 = _ccall(19, 8, 0, v11);
    v13 = _ccall(19, 7, 0, v12);
    v14 = _ccall(19, 6, 0, v13);
    v15 = _ccall(19, 5, 0, v14);
    v16 = v15;
    v17 = _ccall(0, 19, 4, 0, v15);
    v21 = _INSERT(_INSERT(v2 & 0xff, 0, (char)v2 & 1), 1, ~(~(0)));
    v1 = -(0 < v21) + 1;
    v3 = (g_1038c844 ^ g_1038c848) * 2;
    if (v1)
        v3 |= 1;
    return sub_102f2ad0(v3);
}
```

## `sub_102fd33f` `0x102fd33f`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fd33f(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fd361` `0x102fd361`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fd361(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fd3c0` `0x102fd3c0`

_200 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e4;
extern unsigned int g_1038c7e8;

unsigned int sub_102fd3c0(int a0)
{
    unsigned int v5;  // ecx
    unsigned int v6;  // edx
    unsigned int v15;  // 4193
    int v18;  // cc_dep1
    unsigned int v20;  // 4105
    unsigned int v7;  // eax
    unsigned int v8;  // 4292
    unsigned int v9;  // 4293
    unsigned int v10;  // cc_ndep
    unsigned int v11;  // 4294
    char v14;  // al
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v3 = sub_102ef460(a0);
    v1 = v5;
    v0 = v3;
    v1 = v6;
    v7 = v3 * 0x1000000 | v3 * 0x100 & 0xff0000 | v3 >> 8 & 0xff00 | v3 >> 24 & 0xff;
    v8 = _ccall(19, 2, 0, 0);
    v9 = _ccall(19, 1, 0, v8);
    v10 = v9;
    v11 = _ccall(0, 19, 0, 0, v9);
    v14 = _INSERT(v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff, 1, 0);
    v15 = _ccall(0, 19, 1, 0, 0);
    v18 = v14 & 1;
    v20 = _ccall(0, 13, (unsigned int)(v14 & 1), 0, 0);
    v2 = _INSERT(v14, 0, v14 & 1);
    v4 = (g_1038c7e4 ^ g_1038c7e8) * 2;
    if (v2)
        v4 |= 1;
    return sub_102ef3a0(v4);
}
```

## `sub_102fd41e` `0x102fd41e`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fd41e(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fd445` `0x102fd445`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fd445(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fd452` `0x102fd452`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fd452(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fd490` `0x102fd490`

_173 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c834;
extern unsigned int g_1038c838;

int sub_102fd490(unsigned int a0)
{
    unsigned int v6;  // edx
    unsigned int v7;  // ebx
    unsigned int v9;  // eax
    unsigned short v10;  // bx
    unsigned int v11;  // eax
    unsigned int v12;  // eax
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f2170(a0);
    v2 = v6;
    v1 = v7;
    v0 = v4 & 0xffff;
    v9 = _INSERT(v0, 1, 0);
    v10 = _INSERT(_INSERT(*((unsigned short *)((void*)&v7 + 1)), 1, 0), 0, 64);
    v11 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v12 = _INSERT((char)v11 * 0 | (char)(v11 >> 24), 0, ((char)v11 * 0 | (char)(v11 >> 24)) & (char)~(~(v10)));
    v3 = -(0 < v12) + 1;
    v5 = (g_1038c834 ^ g_1038c838) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f2010(v5);
}
```

## `sub_102fd540` `0x102fd540`

_370 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c814;
extern unsigned int g_1038c818;

unsigned int sub_102fd540(int a0)
{
    unsigned int v7;  // edx
    unsigned int v8;  // ebx
    unsigned int v17;  // eax
    unsigned int v18;  // eax
    unsigned short v19;  // ax
    unsigned int v20;  // cc_dep1
    char v21;  // bl
    unsigned int v22;  // 4291
    unsigned int v23;  // cc_ndep
    unsigned int v24;  // cc_dep1
    unsigned int v25;  // 4174
    unsigned int v28;  // eax
    unsigned int v29;  // 4179
    unsigned int v30;  // eax
    unsigned int v33;  // 4180
    unsigned int v36;  // 4151
    unsigned int v10;  // eax
    unsigned int v37;  // eax
    unsigned int v38;  // cc_ndep
    unsigned int v39;  // cc_dep1
    unsigned int v40;  // 4152
    unsigned int v43;  // eax
    unsigned short v11;  // bx
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

    v5 = sub_102f0dc0(a0);
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
        v16 = _INSERT(_INSERT(*((unsigned short *)((void*)&v2 + 1)), 1, 0), 0, 0x88);
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
        v23 = v21 - 27 < 3;
        v24 = v21 - 31;
        v25 = _ccall(0, 19, (unsigned int)(v21 - 31), 0, (unsigned int)(char)(v21 - 27 < 3));
        v28 = _INSERT((char)v0 & v21 - 31, 1, (char)v0 & v21 - 31 & 246);
        v29 = _ccall(12, 0, (unsigned int)(char)(0 < v28), (unsigned int)(char)(0 < v28));
        v30 = -(0 < v28) + 1;
        v33 = _ccall(0, 21, v30 - 1, 0, v29);
        v36 = _ccall(21, v30 - 1, 0, v29);
        v37 = v30;
        v38 = v36;
        v39 = v37 - 1;
        v40 = _ccall(0, 21, v37 - 1, 0, v36);
        if (-(0 < v18) + 1 != v37)
            goto LABEL_102fd684;
        v43 = 1;
    }
    else
    {
LABEL_102fd684:
        v43 = 0;
    }
    v4 = v43;
    v6 = (g_1038c814 ^ g_1038c818) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f0d10(v6);
}
```

## `sub_102fd613` `0x102fd613`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fd613(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fd638` `0x102fd638`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fd638(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fd660` `0x102fd660`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fd660(void)
{
}
```

## `sub_102fd6c0` `0x102fd6c0`

_166 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7fc;
extern unsigned int g_1038c800;

unsigned int sub_102fd6c0(int a0)
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

    v4 = sub_102f02b0(a0);
    v2 = v6;
    v1 = v7;
    v0 = v4 & 0xffff;
    v9 = _INSERT(v0, 1, 0);
    v10 = _INSERT(_INSERT(*((unsigned short *)((void*)&v7 + 1)), 1, 0), 0, 65);
    v11 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v12 = _INSERT((char)v11 * 0 | (char)(v11 >> 24), 0, ((char)v11 * 0 | (char)(v11 >> 24)) & (char)~(~(v10)));
    v3 = -(-(0 < v12));
    v5 = (g_1038c7fc ^ g_1038c800) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0130(v5);
}
```

## `sub_102fd770` `0x102fd770`

_132 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c810;
extern unsigned int g_1038c814;

unsigned int sub_102fd770(unsigned int a0, unsigned int a1)
{
    unsigned int v4;  // 4125
    char v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v4 = _ccall(0, 6, &v0, 8, 0);
    v1 = (!a1 && 1 ? 1 : 0);
    v2 = (g_1038c810 ^ g_1038c814) * 2;
    if (v1)
        v2 |= 1;
    return sub_102f0a30(v2);
}
```

## `sub_102fd782` `0x102fd782`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fd782(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fd800` `0x102fd800`

_136 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c830;
extern unsigned int g_1038c834;

int sub_102fd800(unsigned int a0)
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

    v4 = sub_102f1e90(a0);
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
    v3 = -(-(v12 & 1));
    v5 = (g_1038c830 ^ g_1038c834) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f1d10(v5);
}
```

## `sub_102fd890` `0x102fd890`

_235 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c804;
extern unsigned int g_1038c808;

unsigned int sub_102fd890(unsigned int a0)
{
    unsigned int v8;  // ebx
    unsigned int v17;  // cc_dep1
    unsigned int v18;  // 4354
    unsigned int v9;  // ecx
    unsigned int v11;  // ecx
    unsigned int v12;  // ecx
    char v13;  // cl
    unsigned int v14;  // 4341
    unsigned int v15;  // 4347
    unsigned int v16;  // cc_ndep
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v1 = a0;
    v5 = sub_102f0650(a0);
    v1 = v8;
    v0 = v9;
    v11 = _INSERT(_INSERT(v9, 1, 0), 0, 101);
    v12 = v11 * 0x1000000 | v11 * 0x100 & 0xff0000 | v11 >> 8 & 0xff00 | v11 >> 24 & 0xff;
    v13 = (char)v12 * 0 | (char)(v12 >> 24);
    v14 = _ccall(1, (unsigned int)(v13 - 20), 11, 0);
    v15 = _ccall(19, (unsigned int)(v13 - 10), 0, v14);
    v16 = v15;
    v17 = v13 - 11;
    v18 = _ccall(0, 19, (unsigned int)(v13 - 11), 0, v15);
    v4 = 1;
    v6 = (g_1038c804 ^ g_1038c808) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f0570(v6);
}
```

## `sub_102fd8b2` `0x102fd8b2`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fd8b2(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

