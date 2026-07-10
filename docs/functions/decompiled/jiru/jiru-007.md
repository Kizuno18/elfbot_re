# elfbot.dll decompiled — jiru 0x102f9240..0x102fa971

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_102f9240` `0x102f9240`

_184 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c83c;
extern unsigned int g_1038c840;

unsigned int sub_102f9240(int a0)
{
    unsigned short v6;  // ax
    unsigned int v7;  // edx
    unsigned int v16;  // 4182
    unsigned int v17;  // 4184
    unsigned int v18;  // cc_ndep
    unsigned int v19;  // cc_dep1
    unsigned int v20;  // 4186
    unsigned int v8;  // cc_dep1
    unsigned int v9;  // ebx
    char v10;  // bl
    unsigned int v11;  // 4130
    unsigned int v12;  // 4174
    unsigned int v13;  // 4176
    unsigned int v14;  // 4178
    unsigned int v15;  // 4180
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f2690(a0);
    v6 = v4;
    v2 = v7;
    v8 = v6;
    v1 = v9;
    v0 = 0x1e00;
    v10 = v0;
    v11 = _ccall(0, 15, (unsigned int)v6, 0, 0);
    v12 = _ccall(16, (unsigned int)(v10 - 3), 0, (unsigned int)(char)(v10 < 4));
    v13 = _ccall(19, (unsigned int)(v10 - 4), 0, v12);
    v0 = v6;
    v14 = _ccall(19, (unsigned int)(v10 - 5), 0, v13);
    v15 = _ccall(19, (unsigned int)(v10 - 6), 0, v14);
    v16 = _ccall(19, (unsigned int)(v10 - 7), 0, v15);
    v17 = _ccall(16, (unsigned int)(v10 - 6), 0, v16);
    v18 = v17;
    v19 = v10 - 7;
    v20 = _ccall(0, 19, (unsigned int)(v10 - 7), 0, v17);
    v3 = -(0 < _INSERT(_INSERT(v0, 1, *((char *)((void*)&v0 + 1)) & v10 - 30) & 0xff, 0, (char)_INSERT(v0, 1, *((char *)((void*)&v0 + 1)) & v10 - 30) & 4)) + 1;
    v5 = (g_1038c83c ^ g_1038c840) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f2570(v5);
}
```

## `sub_102f926f` `0x102f926f`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f926f(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f928c` `0x102f928c`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f928c(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f9300` `0x102f9300`

_272 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c804;
extern unsigned int g_1038c808;

unsigned int sub_102f9300(int a0)
{
    unsigned int v5;  // ebx
    unsigned int v6;  // ecx
    unsigned int v15;  // 4575
    int v16;  // cc_dep1
    unsigned int v17;  // 4101
    unsigned int v18;  // eax
    unsigned int v8;  // ecx
    unsigned int v9;  // ecx
    unsigned int v10;  // eax
    unsigned int v12;  // eax
    unsigned int v13;  // eax
    int v14;  // edx
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v3 = sub_102f0650(a0);
    v1 = v5;
    v0 = v6;
    v8 = _INSERT(_INSERT(v6, 1, 0), 0, 164);
    v9 = v8 * 0x1000000 | v8 * 0x100 & 0xff0000 | v8 >> 8 & 0xff00 | v8 >> 24 & 0xff;
    v10 = _INSERT(_INSERT(v3 & 0xffff, 1, 0) & 0xff, 0, ~(~((char)_INSERT(v3 & 0xffff, 1, 0))));
    v12 = v10 * 0x1000000 | v10 * 0x100 & 0xff0000 | v10 >> 8 & 0xff00 | v10 >> 24 & 0xff;
    v13 = _INSERT((char)v12 * 0 | (char)(v12 >> 24), 0, ((char)v12 * 0 | (char)(v12 >> 24)) & (char)~(~(_INSERT((char)v9 * 0 | (char)(v9 >> 24), 0, ((char)v9 * 0 | (char)(v9 >> 24)) - 39))) + 3);
    v1 = -(0 < v13) + 1;
    v14 = -(0 < (v3 & 0xf400)) + 1;
    v15 = _ccall(0, 15, 0, 0, 0);
    v16 = -(0 < v13) + 1;
    if (!(0 < v13) + 1 != v14)
    {
        v17 = _ccall(0, 6, v16, v14, 0);
        v18 = 1;
    }
    else
    {
        v18 = 0;
    }
    v2 = v18;
    v4 = (g_1038c804 ^ g_1038c808) * 2;
    if (v2)
        v4 |= 1;
    return sub_102f0570(v4);
}
```

## `sub_102f93cf` `0x102f93cf`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f93cf(void)
{
}
```

## `sub_102f9420` `0x102f9420`

_153 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e0;
extern unsigned int g_1038c7e4;

int sub_102f9420(unsigned int a0)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // ecx
    unsigned int v8;  // 4185
    unsigned int v11;  // eax
    unsigned int v12;  // 4108
    unsigned int v13;  // cc_dep1
    unsigned int v14;  // 4108
    unsigned int v15;  // 4158
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102ef270(a0);
    v2 = v6;
    v1 = v7;
    v0 = 64;
    v8 = _ccall(0, 19, 8, 0, 0);
    v11 = _INSERT((char)v4 & (char)(v0 ^ 64), 1, (char)v4 & (char)(v0 ^ 64) & 8);
    if (v11)
    {
        v12 = _ccall(3, ~(v11), 1, 0);
        v13 = v12 | 1;
    }
    else
    {
        v14 = _ccall(3, ~(0), 1, 0);
        v13 = v14 & 4294967294;
    }
    v15 = _ccall(0, v13, 0, 0);
    v3 = -(v15 & 1) + 1;
    v5 = (g_1038c7e0 ^ g_1038c7e4) * 2;
    if (v3)
        v5 |= 1;
    return sub_102ef140(v5);
}
```

## `sub_102f9465` `0x102f9465`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f9465(void)
{
}
```

## `sub_102f94c0` `0x102f94c0`

_150 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7f0;
extern unsigned int g_1038c7f4;

unsigned int sub_102f94c0(unsigned int a0, unsigned int a1, unsigned int a2, int a3, unsigned int a4)
{
    unsigned int v2;  // cc_dep1
    unsigned int v3;  // 4132
    unsigned int v4;  // 4119
    unsigned int v5;  // eax
    char v6;  // cl
    unsigned int v7;  // cc_dep1
    unsigned int v8;  // 4143
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v2 = a2 & 0x800;
    v3 = _ccall(0, 15, a2 & 0x800, 0, 0);
    v4 = _ccall(0, 15, a3, 0, 0);
    if (!((char)v4) && (a3 >= 0 || !a3))
    {
        if (!a3)
            goto LABEL_102f9503;
LABEL_102f94fa:
        v5 = 0;
    }
    else
    {
        if (a3)
            goto LABEL_102f94fa;
LABEL_102f9503:
        v6 = (_INSERT(a0, 1, 81) & 0xff) - 1;
        v7 = v6 - 4;
        v8 = _ccall(0, 4, (unsigned int)(v6 - 4), 8, 0);
        v5 = 1;
    }
    v0 = v5;
    v1 = (g_1038c7f0 ^ g_1038c7f4) * 2;
    if (v0)
        v1 |= 1;
    return sub_102efa50(v1);
}
```

## `sub_102f94d8` `0x102f94d8`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f94d8(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f94f3` `0x102f94f3`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f94f3(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f9515` `0x102f9515`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f9515(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f9560` `0x102f9560`

_129 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c808;
extern unsigned int g_1038c80c;

unsigned int sub_102f9560(int a0)
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
    v4 = sub_102f07c0(a0);
    v1 = v6;
    v7 = v4 * 0x1000000 | v4 * 0x100 & 0xff0000 | v4 >> 8 & 0xff00 | v4 >> 24 & 0xff;
    v0 = v8;
    v3 = -(-(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & ~(~(40)) + 25)));
    v5 = (g_1038c808 ^ g_1038c80c) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0730(v5);
}
```

## `sub_102f9582` `0x102f9582`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102f9582(void)
{
}
```

## `sub_102f95f0` `0x102f95f0`

_223 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7d8;
extern unsigned int g_1038c7dc;

unsigned int sub_102f95f0(int a0)
{
    unsigned int v6;  // edx
    unsigned int v7;  // ebx
    unsigned int v16;  // 4104
    unsigned int v17;  // 4150
    unsigned int v9;  // eax
    unsigned short v10;  // bx
    unsigned int v11;  // eax
    unsigned int v12;  // eax
    int v13;  // edx
    int v14;  // eax
    unsigned int v15;  // 4455
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102eed50(a0);
    v2 = v6;
    v1 = v7;
    v0 = v4 & 0xffff;
    v9 = _INSERT(v0, 1, 0);
    v10 = _INSERT(_INSERT(*((unsigned short *)((void*)&v7 + 1)), 1, 0), 0, 128);
    v11 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v12 = _INSERT((char)v11 * 0 | (char)(v11 >> 24), 0, ((char)v11 * 0 | (char)(v11 >> 24)) & (char)~(~(v10)));
    v2 = -(0 < v12) + 1;
    v13 = -(0 < (v4 & 0xf900)) + 1;
    v14 = -(0 < v12) + 1;
    v15 = _ccall(0, 15, 0, 0, 0);
    v16 = _ccall(0, 6, v14, v13, 0);
    v17 = _ccall(5, 6, v14, v13, 0);
    v3 = _INSERT(v14, 0, v17);
    v5 = (g_1038c7d8 ^ g_1038c7dc) * 2;
    if (v3)
        v5 |= 1;
    return sub_102eebb0(v5);
}
```

## `sub_102f9685` `0x102f9685`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f9685(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f96e0` `0x102f96e0`

_159 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c834;
extern unsigned int g_1038c838;

int sub_102f96e0(unsigned int a0)
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
    v5 = sub_102f2170(a0);
    v2 = v8;
    v1 = v7;
    v0 = v5 & 0xffff;
    v4 = 1;
    v6 = (g_1038c834 ^ g_1038c838) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f2010(v6);
}
```

## `sub_102f9780` `0x102f9780`

_160 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c818;
extern unsigned int g_1038c81c;

unsigned int sub_102f9780(int a0)
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
    v7 = (char)(~(~(10)) + 19) + 3;
    v8 = _INSERT(v7 + 13, 0, v7 + 18);
    v0 = v9;
    v2 = -(-(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 14)));
    v4 = (g_1038c818 ^ g_1038c81c) * 2;
    if (0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 14))
        v4 |= 1;
    return sub_102f0e70(v4);
}
```

## `sub_102f9820` `0x102f9820`

_228 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c83c;
extern unsigned int g_1038c840;

unsigned int sub_102f9820(unsigned int a0)
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
    v4 = sub_102f2690(a0);
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
    v3 = -(0 < v24) + 1;
    v5 = (g_1038c83c ^ g_1038c840) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f2570(v5);
}
```

## `sub_102f9840` `0x102f9840`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f9840(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f9910` `0x102f9910`

_135 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c814;
extern unsigned int g_1038c818;

unsigned int sub_102f9910(unsigned int a0)
{
    unsigned int v5;  // edx
    unsigned int v9;  // eax
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v0 = a0;
    v2 = sub_102f0dc0(a0);
    v0 = v5;
    v9 = _INSERT(_INSERT(v2 & 0xff, 0, (char)v2 & 1), 1, ~(~(0)));
    v1 = v9;
    v3 = (g_1038c814 ^ g_1038c818) * 2;
    if (v1)
        v3 |= 1;
    return sub_102f0d10(v3);
}
```

## `sub_102f992f` `0x102f992f`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f992f(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f993b` `0x102f993b`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f993b(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f9948` `0x102f9948`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f9948(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f99a0` `0x102f99a0`

_143 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c83c;
extern unsigned int g_1038c840;

unsigned int sub_102f99a0(int a0)
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
    v5 = sub_102f2690(a0);
    v2 = v8;
    v1 = v7;
    v0 = v5 & 0xffff;
    v4 = 1;
    v6 = (g_1038c83c ^ g_1038c840) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f2570(v6);
}
```

## `sub_102f9a30` `0x102f9a30`

_162 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c800;
extern unsigned int g_1038c804;

int sub_102f9a30(unsigned int a0)
{
    unsigned int v4;  // edx
    unsigned int v5;  // 4141
    unsigned int v6;  // 4147
    unsigned int v9;  // 4167
    unsigned int v10;  // 4169
    unsigned int v11;  // 4171
    unsigned int v12;  // cc_ndep
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v2 = sub_102f04d0(a0);
    v0 = v4;
    v5 = _ccall(0, 4, 14, 0xff, 0);
    v6 = _ccall(0, 19, 3, 0, 0);
    v9 = _ccall(19, 254, 0, 1);
    v10 = _ccall(16, 0xff, 0, v9);
    v11 = _ccall(16, 0, 0, v10);
    v12 = v11;
    v1 = _INSERT(_INSERT(v2, 1, 0) & 0xff, 0, (char)_INSERT(v2, 1, 0) & 1);
    v3 = (g_1038c800 ^ g_1038c804) * 2;
    if (v1)
        v3 |= 1;
    return sub_102f0430(v3);
}
```

## `sub_102f9a5d` `0x102f9a5d`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f9a5d(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f9a7c` `0x102f9a7c`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f9a7c(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f9a99` `0x102f9a99`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f9a99(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f9ae0` `0x102f9ae0`

_150 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c828;
extern unsigned int g_1038c82c;

unsigned int sub_102f9ae0(int a0)
{
    unsigned int v5;  // ecx
    unsigned int v6;  // eax
    unsigned int v7;  // ecx
    unsigned int v8;  // edx
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v3 = sub_102f1910(a0);
    v1 = v5;
    v6 = v3 * 0x1000000 | v3 * 0x100 & 0xff0000 | v3 >> 8 & 0xff00 | v3 >> 24 & 0xff;
    v7 = _INSERT(~(~(6)) + 24, 0, (char)(~(~(6)) + 24) + 3);
    v0 = v8;
    v2 = -(-(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v7 + 32)));
    v4 = (g_1038c828 ^ g_1038c82c) * 2;
    if (0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v7 + 32))
        v4 |= 1;
    return sub_102f1810(v4);
}
```

## `sub_102f9b80` `0x102f9b80`

_145 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c844;
extern unsigned int g_1038c848;

unsigned int sub_102f9b80(int a0)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // ecx
    unsigned int v8;  // eax
    unsigned int v9;  // 4108
    unsigned int v10;  // cc_dep1
    unsigned int v11;  // 4108
    unsigned int v12;  // 4158
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f2b60(a0);
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
    v3 = -(v12 & 1) + 1;
    v5 = (g_1038c844 ^ g_1038c848) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f2ad0(v5);
}
```

## `sub_102f9c20` `0x102f9c20`

_156 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c83c;
extern unsigned int g_1038c840;

unsigned int sub_102f9c20(int a0)
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
    v7 = (char)(~(~(13)) + 16) + 3;
    v8 = _INSERT(v7 + 13, 0, v7 + 18);
    v0 = v9;
    v2 = -(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 14)) + 1;
    v4 = (g_1038c83c ^ g_1038c840) * 2;
    if (!(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 14)) != 4294967295)
        v4 |= 1;
    return sub_102f2570(v4);
}
```

## `sub_102f9cc0` `0x102f9cc0`

_218 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e0;
extern unsigned int g_1038c7e4;

int sub_102f9cc0(unsigned int a0)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // eax
    unsigned int v8;  // ecx
    int v9;  // edx
    unsigned int v10;  // 4337
    int v11;  // cc_dep1
    unsigned int v12;  // 4104
    unsigned int v13;  // 4101
    unsigned int v14;  // eax
    unsigned int v15;  // 4104
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v2 = v6;
    v4 = sub_102ef270(a0);
    v1 = v6;
    v7 = v4 * 0x1000000 | v4 * 0x100 & 0xff0000 | v4 >> 8 & 0xff00 | v4 >> 24 & 0xff;
    v0 = v8;
    v2 = -(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & ~(~(110)) + 18)) + 1;
    v9 = -(0 < (v4 & 0xfb00)) + 1;
    v10 = _ccall(0, 15, 0, 0, 0);
    v11 = -(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & ~(~(110)) + 18)) + 1;
    v12 = _ccall(0, 6, -((unsigned int)(char)(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & ~(~(110)) + 18))) + 1, v9, 0);
    if (v11 == v9)
    {
        v13 = _ccall(0, 6, v11, v9, 0);
        v14 = 0;
    }
    else
    {
        v15 = _ccall(0, 15, 0, 0, 0);
        v14 = 1;
    }
    v3 = v14;
    v5 = (g_1038c7e0 ^ g_1038c7e4) * 2;
    if (v3)
        v5 |= 1;
    return sub_102ef140(v5);
}
```

## `sub_102f9ce2` `0x102f9ce2`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102f9ce2(void)
{
}
```

## `sub_102f9db0` `0x102f9db0`

_256 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c824;
extern unsigned int g_1038c828;

int sub_102f9db0(unsigned int a0)
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

    v4 = sub_102f1670(a0);
    v2 = v6;
    v1 = v7;
    v0 = _INSERT(v4 & 0xffff, 1, 0);
    v10 = _INSERT(_INSERT(v7, 1, 0), 0, 125);
    v11 = _INSERT(v0, 0, (char)v0 & (char)~(~(v10)) + 3);
    v2 = -(0 < v11) + 1;
    v3 = _INSERT(-(0 < v11) + 1, 0, -(0 < v11) + 1 == -(0 < (v4 & 0xfc00)) + 1);
    v5 = (g_1038c824 ^ g_1038c828) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f14d0(v5);
}
```

## `sub_102f9eb0` `0x102f9eb0`

_343 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7f8;
extern unsigned int g_1038c7fc;

int sub_102f9eb0(unsigned int a0)
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
    v7 = sub_102effb0(a0);
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
            goto LABEL_102f9fd2;
        v25 = 1;
    }
    else
    {
LABEL_102f9fd2:
        v25 = 0;
    }
    v6 = v25;
    v8 = (g_1038c7f8 ^ g_1038c7fc) * 2;
    if (v6)
        v8 |= 1;
    return sub_102efe30(v8);
}
```

## `sub_102f9f8f` `0x102f9f8f`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f9f8f(void)
{
}
```

## `sub_102fa010` `0x102fa010`

_121 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e4;
extern unsigned int g_1038c7e8;

unsigned int sub_102fa010(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
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
    v6 = (g_1038c7e4 ^ g_1038c7e8) * 2;
    if (v5)
        v6 |= 1;
    return sub_102ef3a0(v6);
}
```

## `sub_102fa090` `0x102fa090`

_372 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7fc;
extern unsigned int g_1038c800;

unsigned int sub_102fa090(unsigned int a0)
{
    unsigned int v10;  // ebx
    unsigned int v19;  // 4291
    unsigned int v20;  // cc_ndep
    unsigned int v21;  // cc_dep1
    unsigned int v22;  // 4298
    unsigned int v26;  // eax
    unsigned int v27;  // eax
    unsigned int v28;  // eax
    unsigned int v11;  // ecx
    unsigned short v29;  // ax
    unsigned int v30;  // cc_dep1
    unsigned int v31;  // 4244
    unsigned int v33;  // eax
    unsigned int v13;  // ecx
    unsigned int v14;  // ecx
    unsigned int v15;  // eax
    char v16;  // cl
    unsigned int v17;  // 4279
    unsigned int v18;  // 4285
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x14]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]

    v3 = a0;
    v7 = sub_102f02b0(a0);
    v3 = v10;
    v2 = v11;
    v13 = _INSERT(_INSERT(v11, 1, 0), 0, 101);
    v14 = v13 * 0x1000000 | v13 * 0x100 & 0xff0000 | v13 >> 8 & 0xff00 | v13 >> 24 & 0xff;
    v15 = _INSERT(_INSERT(v7 & 0xffff, 1, 0) & 0xff, 0, ~(~((char)_INSERT(v7 & 0xffff, 1, 0))));
    v16 = (char)v14 * 0 | (char)(v14 >> 24);
    v17 = _ccall(1, (unsigned int)(v16 - 20), 12, 0);
    v18 = _ccall(19, (unsigned int)(v16 - 9), 0, v17);
    v19 = _ccall(19, (unsigned int)(v16 - 10), 0, v18);
    v20 = v19;
    v21 = v16 - 11;
    v22 = _ccall(0, 19, (unsigned int)(v16 - 11), 0, v19);
    v26 = v15 * 0x1000000 | v15 * 0x100 & 0xff0000 | v15 >> 8 & 0xff00 | v15 >> 24 & 0xff;
    v27 = _INSERT((char)v26 * 0 | (char)(v26 >> 24), 0, ((char)v26 * 0 | (char)(v26 >> 24)) & (char)~(~(_INSERT(v16 - 11 CONCAT 0, 0, v16 - 40))) + 3);
    if (!v27)
    {
        v3 = v10;
        v28 = v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff;
        v4 = -(0 < ((v28 * 0x1000000 | v28 * 0x100 & 0xff0000 | v28 >> 8 & 0xff00 | v28 >> 24 & 0xff) & ~(~(114)) + 14)) + 1;
        v29 = v7;
        v3 = v5;
        v30 = v29;
        v2 = v10;
        v0 = 31;
        v31 = _ccall(0, 15, (unsigned int)v29, 0, 0);
        v1 = v29;
        if (v4 != -(0 < _INSERT((char)v1 & (char)v0 - 31, 1, (char)v1 & (char)v0 - 31 & 243)) + 1)
            goto LABEL_102fa1d6;
        v33 = 1;
    }
    else
    {
LABEL_102fa1d6:
        v33 = 0;
    }
    v6 = v33;
    v8 = (g_1038c7fc ^ g_1038c800) * 2;
    if (v6)
        v8 |= 1;
    return sub_102f0130(v8);
}
```

## `sub_102fa0b0` `0x102fa0b0`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fa0b0(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fa14d` `0x102fa14d`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102fa14d(void)
{
}
```

## `sub_102fa190` `0x102fa190`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fa190(void)
{
}
```

## `sub_102fa210` `0x102fa210`

_205 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e0;
extern unsigned int g_1038c7e4;

int sub_102fa210(unsigned int a0)
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
    v2 = -(-(0 < v13));
    v4 = (g_1038c7e0 ^ g_1038c7e4) * 2;
    if (v2)
        v4 |= 1;
    return sub_102ef140(v4);
}
```

## `sub_102fa2e0` `0x102fa2e0`

_198 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c808;
extern unsigned int g_1038c80c;

unsigned int sub_102fa2e0(int a0)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // ecx
    unsigned int v9;  // 4304
    unsigned int v10;  // cc_ndep
    unsigned int v11;  // 4305
    unsigned int v15;  // eax
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f07c0(a0);
    v2 = v6;
    v1 = v7;
    v0 = _INSERT(v4 & 0xffff, 1, 0);
    v9 = _ccall(19, 91, 0, 0);
    v10 = v9;
    v11 = _ccall(0, 19, 90, 0, v9);
    v15 = _INSERT(v0, 0, (char)v0 & (char)~(~(_INSERT(90 CONCAT 0, 0, 65))));
    v3 = -(0 < v15) + 1;
    v5 = (g_1038c808 ^ g_1038c80c) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0730(v5);
}
```

## `sub_102fa343` `0x102fa343`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fa343(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fa3b0` `0x102fa3b0`

_165 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c828;
extern unsigned int g_1038c82c;

unsigned int sub_102fa3b0(int a0)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // ecx
    unsigned int v8;  // eax
    unsigned int v9;  // 4108
    unsigned int v10;  // cc_dep1
    unsigned int v11;  // 4108
    unsigned int v12;  // 4159
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f1910(a0);
    v2 = v6;
    v1 = v7;
    v0 = 0x800;
    v8 = _INSERT(_INSERT(v4 & 0xffff, 1, (char)v4 & *((char *)((void*)&v0 + 1)) - 8) & 0xff, 0, (char)_INSERT(v4 & 0xffff, 1, (char)v4 & *((char *)((void*)&v0 + 1)) - 8) & 4);
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
    v5 = (g_1038c828 ^ g_1038c82c) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f1810(v5);
}
```

## `sub_102fa460` `0x102fa460`

_235 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c844;
extern unsigned int g_1038c848;

unsigned int sub_102fa460(int a0)
{
    unsigned int v5;  // ecx
    unsigned int v6;  // eax
    unsigned int v15;  // eax
    char v7;  // cl
    unsigned int v8;  // ecx
    unsigned int v9;  // edx
    int v10;  // edx
    unsigned int v11;  // 4513
    unsigned int v13;  // 4104
    unsigned int v14;  // 4104
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v3 = sub_102f2b60(a0);
    v1 = v5;
    v6 = v3 * 0x1000000 | v3 * 0x100 & 0xff0000 | v3 >> 8 & 0xff00 | v3 >> 24 & 0xff;
    v7 = (char)(~(~(75)) + 15) + 3;
    v8 = _INSERT(v7 + 13, 0, v7 + 18);
    v0 = v9;
    v2 = -(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 0x11)) + 1;
    v10 = -(0 < (v3 & 64000)) + 1;
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
    v4 = (g_1038c844 ^ g_1038c848) * 2;
    if (v15)
        v4 |= 1;
    return sub_102f2ad0(v4);
}
```

## `sub_102fa550` `0x102fa550`

_187 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c838;
extern unsigned int g_1038c83c;

int sub_102fa550(unsigned int a0)
{
    unsigned short v6;  // ax
    unsigned int v7;  // edx
    unsigned int v16;  // 4203
    unsigned int v17;  // 4205
    unsigned int v18;  // 4207
    unsigned int v19;  // cc_ndep
    unsigned int v20;  // cc_dep1
    unsigned int v21;  // 4209
    unsigned int v8;  // cc_dep1
    unsigned int v9;  // ebx
    char v10;  // bl
    unsigned int v11;  // 4130
    unsigned int v12;  // 4195
    unsigned int v13;  // 4197
    unsigned int v14;  // 4199
    unsigned int v15;  // 4201
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f2420(a0);
    v6 = v4;
    v2 = v7;
    v8 = v6;
    v1 = v9;
    v0 = 0x1e00;
    v10 = v0;
    v11 = _ccall(0, 15, (unsigned int)v6, 0, 0);
    v12 = _ccall(16, (unsigned int)(v10 - 4), 0, (unsigned int)(char)(v10 - 3 < 2));
    v13 = _ccall(16, (unsigned int)(v10 - 3), 0, v12);
    v0 = v6;
    v14 = _ccall(19, (unsigned int)(v10 - 4), 0, v13);
    v15 = _ccall(19, (unsigned int)(v10 - 5), 0, v14);
    v16 = _ccall(19, (unsigned int)(v10 - 6), 0, v15);
    v17 = _ccall(16, (unsigned int)(v10 - 5), 0, v16);
    v18 = _ccall(19, (unsigned int)(v10 - 6), 0, v17);
    v19 = v18;
    v20 = v10 - 7;
    v21 = _ccall(0, 19, (unsigned int)(v10 - 7), 0, v18);
    v3 = -(0 < _INSERT(_INSERT(v0, 1, *((char *)((void*)&v0 + 1)) & v10 - 30) & 0xff, 0, (char)_INSERT(v0, 1, *((char *)((void*)&v0 + 1)) & v10 - 30) & 4)) + 1;
    v5 = (g_1038c838 ^ g_1038c83c) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f22d0(v5);
}
```

## `sub_102fa57f` `0x102fa57f`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fa57f(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fa5a3` `0x102fa5a3`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fa5a3(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fa610` `0x102fa610`

_230 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c810;
extern unsigned int g_1038c814;

unsigned int sub_102fa610(int a0)
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

    v4 = sub_102f0ba0(a0);
    v2 = v6;
    v1 = v7;
    v0 = _INSERT(v4 & 0xffff, 1, 0);
    v10 = _INSERT(_INSERT(v7, 1, 0), 0, 125);
    v11 = _INSERT(v0, 0, (char)v0 & (char)~(~(v10)) + 3);
    v3 = -(-(0 < v11));
    v5 = (g_1038c810 ^ g_1038c814) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0a30(v5);
}
```

## `sub_102fa700` `0x102fa700`

_229 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c81c;
extern unsigned int g_1038c820;

int sub_102fa700(unsigned int a0)
{
    unsigned int v6;  // edx
    char v7;  // al
    unsigned int v16;  // 4157
    unsigned int v17;  // eax
    unsigned int v18;  // 4108
    unsigned int v19;  // cc_dep1
    unsigned int v20;  // 4108
    unsigned int v21;  // 4133
    unsigned int v22;  // 4134
    unsigned int v23;  // eax
    unsigned int v8;  // ebx
    unsigned int v26;  // 4135
    unsigned int v29;  // 4119
    unsigned int v30;  // eax
    unsigned int v33;  // 4120
    char v9;  // bl
    unsigned int v36;  // 4135
    unsigned int v37;  // eax
    unsigned int v38;  // cc_ndep
    unsigned int v39;  // cc_dep1
    unsigned int v40;  // 4136
    char v10;  // bh
    unsigned int v11;  // cc_dep1
    unsigned int v12;  // 4141
    int v15;  // cc_dep1
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f1120(a0);
    v2 = v6;
    v7 = v4;
    v1 = v8;
    v0 = 0x100;
    v9 = v0;
    v10 = v9 - 1;
    v11 = v9 - 1;
    v12 = _ccall(0, 19, (unsigned int)(v9 - 1), 0, 0);
    v15 = v7 & v10;
    v16 = _ccall(0, 13, (unsigned int)(v7 & v10), 0, 0);
    v17 = _INSERT(_INSERT(v7, 1, v7 & v10) & 0xff, 0, (char)_INSERT(v7, 1, v7 & v10) & 4);
    if (v17)
    {
        v18 = _ccall(3, ~(v17), 1, 0);
        v19 = v18 | 1;
    }
    else
    {
        v20 = _ccall(3, ~(0), 1, 0);
        v19 = v20 & 4294967294;
    }
    v21 = _ccall(0, v19, 0, 0);
    v22 = _ccall(12, 0, v21 & 1, v21 & 1);
    v23 = -(v21 & 1) + 1;
    v26 = _ccall(0, 21, v23 - 1, 0, v22);
    v29 = _ccall(21, v23 - 1, 0, v22);
    v30 = v23;
    v33 = _ccall(0, 21, v30 - 1, 0, v29);
    v36 = _ccall(21, v30 - 1, 0, v29);
    v37 = v30;
    v38 = v36;
    v39 = v37 - 1;
    v40 = _ccall(0, 21, v37 - 1, 0, v36);
    v3 = v37;
    v5 = (g_1038c81c ^ g_1038c820) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0ff0(v5);
}
```

## `sub_102fa731` `0x102fa731`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fa731(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fa752` `0x102fa752`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fa752(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fa793` `0x102fa793`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fa793(void)
{
}
```

## `sub_102fa7a2` `0x102fa7a2`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fa7a2(void)
{
}
```

## `sub_102fa7b3` `0x102fa7b3`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fa7b3(void)
{
}
```

## `sub_102fa7f0` `0x102fa7f0`

_168 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c824;
extern unsigned int g_1038c828;

int sub_102fa7f0(unsigned int a0)
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

    v5 = sub_102f1670(a0);
    v7 = v5;
    v3 = v8;
    v9 = v7;
    v2 = v10;
    v0 = 0x1f00;
    v11 = _ccall(0, 15, (unsigned int)v7, 0, 0);
    v1 = v7;
    v4 = -(-(0 < _INSERT(_INSERT(v1, 1, *((char *)((void*)&v1 + 1)) & (char)v0 - 31) & 0xff, 0, (char)_INSERT(v1, 1, *((char *)((void*)&v1 + 1)) & (char)v0 - 31) & 4)));
    v6 = (g_1038c824 ^ g_1038c828) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f14d0(v6);
}
```

## `sub_102fa81f` `0x102fa81f`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fa81f(void)
{
}
```

## `sub_102fa8a0` `0x102fa8a0`

_274 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c804;
extern unsigned int g_1038c808;

unsigned int sub_102fa8a0(int a0)
{
    unsigned int v5;  // ebx
    unsigned int v6;  // ecx
    unsigned int v15;  // 4597
    int v16;  // cc_dep1
    unsigned int v17;  // 4101
    unsigned int v18;  // eax
    unsigned int v8;  // ecx
    unsigned int v9;  // ecx
    unsigned int v10;  // eax
    unsigned int v12;  // eax
    unsigned int v13;  // eax
    int v14;  // edx
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v3 = sub_102f0650(a0);
    v1 = v5;
    v0 = v6;
    v8 = _INSERT(_INSERT(v6, 1, 0), 0, 164);
    v9 = v8 * 0x1000000 | v8 * 0x100 & 0xff0000 | v8 >> 8 & 0xff00 | v8 >> 24 & 0xff;
    v10 = _INSERT(_INSERT(v3 & 0xffff, 1, 0) & 0xff, 0, ~(~((char)_INSERT(v3 & 0xffff, 1, 0))));
    v12 = v10 * 0x1000000 | v10 * 0x100 & 0xff0000 | v10 >> 8 & 0xff00 | v10 >> 24 & 0xff;
    v13 = _INSERT((char)v12 * 0 | (char)(v12 >> 24), 0, ((char)v12 * 0 | (char)(v12 >> 24)) & (char)~(~(_INSERT((char)v9 * 0 | (char)(v9 >> 24), 0, ((char)v9 * 0 | (char)(v9 >> 24)) - 39))) + 3);
    v1 = -(0 < v13) + 1;
    v14 = -(0 < (v3 & 0x500)) + 1;
    v15 = _ccall(0, 15, 0, 0, 0);
    v16 = -(0 < v13) + 1;
    if (!(0 < v13) + 1 != v14)
    {
        v17 = _ccall(0, 6, v16, v14, 0);
        v18 = 1;
    }
    else
    {
        v18 = 0;
    }
    v2 = v18;
    v4 = (g_1038c804 ^ g_1038c808) * 2;
    if (v2)
        v4 |= 1;
    return sub_102f0570(v4);
}
```

## `sub_102fa971` `0x102fa971`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fa971(void)
{
}
```

