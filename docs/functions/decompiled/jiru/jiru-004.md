# elfbot.dll decompiled — jiru 0x102f4db0..0x102f6170

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_102f4db0` `0x102f4db0`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f4db0(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f4e4d` `0x102f4e4d`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f4e4d(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f4e7e` `0x102f4e7e`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f4e7e(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f4ecb` `0x102f4ecb`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f4ecb(void)
{
}
```

## `sub_102f4ee2` `0x102f4ee2`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f4ee2(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f4f16` `0x102f4f16`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f4f16(void)
{
}
```

## `sub_102f4f25` `0x102f4f25`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f4f25(void)
{
}
```

## `sub_102f4f36` `0x102f4f36`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f4f36(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f4f80` `0x102f4f80`

_155 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c808;
extern unsigned int g_1038c80c;

unsigned int sub_102f4f80(int a0)
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

    v4 = sub_102f07c0(a0);
    v2 = v6;
    v1 = v7;
    v0 = v4 & 0xffff;
    v9 = _INSERT(v0, 1, 0);
    v10 = _INSERT(_INSERT(*((unsigned short *)((void*)&v7 + 1)), 1, 0), 0, 128);
    v11 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v12 = _INSERT((char)v11 * 0 | (char)(v11 >> 24), 0, ((char)v11 * 0 | (char)(v11 >> 24)) & (char)~(~(v10)));
    v3 = -(0 < v12) + 1;
    v5 = (g_1038c808 ^ g_1038c80c) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0730(v5);
}
```

## `sub_102f5020` `0x102f5020`

_184 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c804;
extern unsigned int g_1038c808;

unsigned int sub_102f5020(int a0)
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

    v3 = sub_102f0650(a0);
    v1 = v5;
    v0 = v3;
    v1 = v6;
    v7 = v0 * 0x1000000 | v0 * 0x100 & 0xff0000 | v0 >> 8 & 0xff00 | v0 >> 24 & 0xff;
    v9 = _INSERT(_INSERT((char)v7 * 0 | (char)(v7 >> 24), 0, ((char)v7 * 0 | (char)(v7 >> 24)) & 1), 1, 255);
    v10 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v2 = -(0 < _INSERT((char)v10 * 0 | (char)(v10 >> 24), 1, ~((char)v10 * 0 | (char)(v10 >> 24)))) + 1;
    v4 = (g_1038c804 ^ g_1038c808) * 2;
    if (v2)
        v4 |= 1;
    return sub_102f0570(v4);
}
```

## `sub_102f50e0` `0x102f50e0`

_378 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7fc;
extern unsigned int g_1038c800;

unsigned int sub_102f50e0(int a0)
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
    unsigned int v12;  // 4276
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x2c]
    unsigned int v1;  // [bp-0x28]
    unsigned int v2;  // [bp-0x24]
    unsigned int v3;  // [bp-0x20]
    unsigned int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v5 = sub_102f02b0(a0);
    v3 = v7;
    v2 = v8;
    v11 = v10 * 0x1000000 | v10 * 0x100 & 0xff0000 | v10 >> 8 & 0xff00 | v10 >> 24 & 0xff;
    v1 = _INSERT(v5 & 0xffff, 1, 0);
    v12 = _ccall(0, 19, 87, 0, 0);
    v16 = _INSERT(v1, 0, (char)v1 & (char)~(~(_INSERT(87 CONCAT 0, 0, 64))));
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
            goto LABEL_102f5220;
        v27 = 0;
    }
    else
    {
LABEL_102f5220:
        v27 = 1;
    }
    v4 = v27;
    v6 = (g_1038c7fc ^ g_1038c800) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f0130(v6);
}
```

## `sub_102f5140` `0x102f5140`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f5140(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f5260` `0x102f5260`

_207 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c804;
extern unsigned int g_1038c808;

unsigned int sub_102f5260(int a0)
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

    v3 = sub_102f0650(a0);
    v1 = v5;
    v0 = v6;
    v8 = _INSERT(_INSERT(v6, 1, 0), 0, 101);
    v9 = v8 * 0x1000000 | v8 * 0x100 & 0xff0000 | v8 >> 8 & 0xff00 | v8 >> 24 & 0xff;
    v10 = _INSERT(_INSERT(v3 & 0xffff, 1, 0) & 0xff, 0, ~(~((char)_INSERT(v3 & 0xffff, 1, 0))));
    v12 = v10 * 0x1000000 | v10 * 0x100 & 0xff0000 | v10 >> 8 & 0xff00 | v10 >> 24 & 0xff;
    v13 = _INSERT((char)v12 * 0 | (char)(v12 >> 24), 0, ((char)v12 * 0 | (char)(v12 >> 24)) & (char)~(~(_INSERT((char)v9 * 0 | (char)(v9 >> 24), 0, ((char)v9 * 0 | (char)(v9 >> 24)) - 39))) + 3);
    v2 = -(-(0 < v13));
    v4 = (g_1038c804 ^ g_1038c808) * 2;
    if (v2)
        v4 |= 1;
    return sub_102f0570(v4);
}
```

## `sub_102f5330` `0x102f5330`

_160 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7f8;
extern unsigned int g_1038c7fc;

int sub_102f5330(unsigned int a0, unsigned int a1)
{
    unsigned int v7;  // ebx
    unsigned int v8;  // edx
    unsigned int v9;  // eax
    unsigned int v10;  // 4142
    unsigned int v11;  // cc_dep1
    unsigned int v12;  // 4140
    unsigned int v13;  // 4104
    unsigned int v14;  // 4143
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v3 = v7;
    v5 = sub_102effb0(a0);
    v2 = v8;
    v9 = v5 & 0xffff;
    v1 = v7;
    v0 = v9;
    v10 = _ccall(6, 19, (unsigned int)(*((char *)((void*)&v7 + 1)) - 1), 0, 0);
    if (Conv(32I->1I, vvar_104)) { Goto None } else { Goto None }
    v11 = v9 & 65;
    v12 = _ccall(0, 15, v9 & 65, 0, 0);
    v13 = _ccall(0, 15, 0, 0, 0);
    if (Conv(32I->1I, vvar_106)) { Goto None } else { Goto None }
    v14 = _ccall(0, 4, 72, 31, 0);
    v4 = 1;
    v6 = (g_1038c7f8 ^ g_1038c7fc) * 2;
    if (v4)
        v6 |= 1;
    return sub_102efe30(v6);
}
```

## `sub_102f536c` `0x102f536c`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f536c(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f5390` `0x102f5390`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f5390(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f53e0` `0x102f53e0`

_173 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c82c;
extern unsigned int g_1038c830;

unsigned int sub_102f53e0(int a0)
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

    v4 = sub_102f1b90(a0);
    v6 = v4;
    v2 = v7;
    v8 = v6;
    v1 = v9;
    v0 = 0x1e00;
    v10 = v0;
    v11 = _ccall(0, 15, (unsigned int)v6, 0, 0);
    v0 = v6;
    v12 = _ccall(19, (unsigned int)(v10 - 5), 0, (unsigned int)(char)(v10 < 4));
    v13 = _ccall(19, (unsigned int)(v10 - 6), 0, v12);
    v14 = v13;
    v15 = v10 - 7;
    v16 = _ccall(0, 19, (unsigned int)(v10 - 7), 0, v13);
    v3 = -(-(0 < _INSERT(_INSERT(v0, 1, *((char *)((void*)&v0 + 1)) & v10 - 30) & 0xff, 0, (char)_INSERT(v0, 1, *((char *)((void*)&v0 + 1)) & v10 - 30) & 4)));
    v5 = (g_1038c82c ^ g_1038c830) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f1a10(v5);
}
```

## `sub_102f540f` `0x102f540f`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f540f(void)
{
}
```

## `sub_102f5426` `0x102f5426`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f5426(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f54a0` `0x102f54a0`

_139 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7dc;
extern unsigned int g_1038c7e0;

unsigned int sub_102f54a0(unsigned int a0)
{
    unsigned int v5;  // edx
    unsigned int v8;  // eax
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v0 = a0;
    v2 = sub_102ef020(a0);
    v0 = v5;
    v8 = _INSERT(_INSERT(v2 & 0xff, 0, (char)v2 & 1), 1, ~(~(0)));
    v1 = -(0 < v8) + 1;
    v3 = (g_1038c7dc ^ g_1038c7e0) * 2;
    if (v1)
        v3 |= 1;
    return sub_102eef00(v3);
}
```

## `sub_102f54bf` `0x102f54bf`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f54bf(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f54cd` `0x102f54cd`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f54cd(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f5530` `0x102f5530`

_192 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7ec;
extern unsigned int g_1038c7f0;

int sub_102f5530(unsigned int a0)
{
    unsigned int v7;  // edx
    unsigned int v8;  // ebx
    unsigned int v9;  // ecx
    int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    int v3;  // [bp-0x18], Other Possible Types: unsigned int
    unsigned int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v5 = sub_102ef8d0(a0);
    v3 = v5;
    v3 = v7;
    v2 = v8;
    v1 = v9;
    v0 = v5;
    v4 = _INSERT(_INSERT(v0, 1, 0) & 0xff, 0, (char)_INSERT(v0, 1, 0) & 1);
    v6 = (g_1038c7ec ^ g_1038c7f0) * 2;
    if (v4)
        v6 |= 1;
    return sub_102ef750(v6);
}
```

## `sub_102f55f0` `0x102f55f0`

_168 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c814;
extern unsigned int g_1038c818;

unsigned int sub_102f55f0(int a0)
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

    v4 = sub_102f0dc0(a0);
    v2 = v6;
    v1 = v7;
    v0 = 10;
    v8 = _INSERT((char)v4 & (char)v0 - 10, 1, (char)v4 & (char)v0 - 10 & 8);
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
    v5 = (g_1038c814 ^ g_1038c818) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0d10(v5);
}
```

## `sub_102f56a0` `0x102f56a0`

_115 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7dc;
extern unsigned int g_1038c7e0;

unsigned int sub_102f56a0(unsigned int a0)
{
    unsigned int v5;  // edx
    unsigned int v8;  // eax
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v0 = a0;
    v2 = sub_102ef020(a0);
    v0 = v5;
    v8 = _INSERT(_INSERT(v2 & 0xff, 0, (char)v2 & 1), 1, ~(~(0)));
    v1 = v8;
    v3 = (g_1038c7dc ^ g_1038c7e0) * 2;
    if (v1)
        v3 |= 1;
    return sub_102eef00(v3);
}
```

## `sub_102f56bf` `0x102f56bf`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f56bf(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f56cd` `0x102f56cd`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f56cd(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f5720` `0x102f5720`

_224 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c804;
extern unsigned int g_1038c808;

unsigned int sub_102f5720(int a0)
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
    unsigned int v12;  // 4145
    int v15;  // cc_dep1
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f0650(a0);
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
    v5 = (g_1038c804 ^ g_1038c808) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0570(v5);
}
```

## `sub_102f5754` `0x102f5754`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f5754(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f5775` `0x102f5775`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f5775(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f57ae` `0x102f57ae`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f57ae(void)
{
}
```

## `sub_102f57bd` `0x102f57bd`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f57bd(void)
{
}
```

## `sub_102f57ce` `0x102f57ce`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f57ce(void)
{
}
```

## `sub_102f5810` `0x102f5810`

_480 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c83c;
extern unsigned int g_1038c840;

unsigned int sub_102f5810(unsigned int a0)
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
    unsigned int v39;  // 4267
    unsigned int v40;  // 4142
    unsigned int v41;  // 4144
    unsigned int v42;  // cc_ndep
    unsigned int v43;  // cc_dep1
    unsigned int v44;  // 4146
    unsigned int v47;  // eax
    unsigned int v12;  // ecx
    unsigned int v48;  // 4214
    unsigned int v49;  // eax
    unsigned int v52;  // 4215
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
    v6 = sub_102f2690(a0);
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
            goto LABEL_102f59c7;
        v69 = 1;
    }
    else
    {
LABEL_102f59c7:
        v69 = 0;
    }
    v5 = v69;
    v7 = (g_1038c83c ^ g_1038c840) * 2;
    if (v5)
        v7 |= 1;
    return sub_102f2570(v7);
}
```

## `sub_102f5830` `0x102f5830`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f5830(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f58cd` `0x102f58cd`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f58cd(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f58fe` `0x102f58fe`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f58fe(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f5946` `0x102f5946`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f5946(void)
{
}
```

## `sub_102f595d` `0x102f595d`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f595d(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f5996` `0x102f5996`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f5996(void)
{
}
```

## `sub_102f59a5` `0x102f59a5`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f59a5(void)
{
}
```

## `sub_102f59b6` `0x102f59b6`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f59b6(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f5a00` `0x102f5a00`

_219 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c830;
extern unsigned int g_1038c834;

int sub_102f5a00(unsigned int a0)
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

    v4 = sub_102f1e90(a0);
    v2 = v6;
    v1 = v7;
    v0 = _INSERT(v4 & 0xffff, 1, 0);
    v10 = _INSERT(_INSERT(v7, 1, 0), 0, 125);
    v11 = _INSERT(v0, 0, (char)v0 & (char)~(~(v10)) + 3);
    v3 = -(0 < v11) + 1;
    v5 = (g_1038c830 ^ g_1038c834) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f1d10(v5);
}
```

## `sub_102f5ae0` `0x102f5ae0`

_202 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c808;
extern unsigned int g_1038c80c;

unsigned int sub_102f5ae0(int a0)
{
    unsigned short v7;  // ax
    unsigned int v8;  // edx
    unsigned int v17;  // 4285
    unsigned int v20;  // 4119
    unsigned int v21;  // eax
    unsigned int v24;  // 4120
    unsigned int v9;  // cc_dep1
    unsigned int v27;  // 4135
    unsigned int v28;  // eax
    unsigned int v29;  // cc_ndep
    unsigned int v30;  // cc_dep1
    unsigned int v31;  // 4136
    unsigned int v10;  // ebx
    unsigned int v11;  // 4130
    unsigned int v12;  // eax
    unsigned int v13;  // 4284
    unsigned int v14;  // eax
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v5 = sub_102f07c0(a0);
    v7 = v5;
    v3 = v8;
    v9 = v7;
    v2 = v10;
    v0 = 0x1f00;
    v11 = _ccall(0, 15, (unsigned int)v7, 0, 0);
    v1 = v7;
    v12 = _INSERT(_INSERT(v1, 1, *((char *)((void*)&v1 + 1)) & (char)v0 - 31) & 0xff, 0, (char)_INSERT(v1, 1, *((char *)((void*)&v1 + 1)) & (char)v0 - 31) & 4);
    v13 = _ccall(12, 0, (unsigned int)(char)(0 < v12), (unsigned int)(char)(0 < v12));
    v14 = -(0 < v12) + 1;
    v17 = _ccall(0, 21, v14 - 1, 0, v13);
    v20 = _ccall(21, v14 - 1, 0, v13);
    v21 = v14;
    v24 = _ccall(0, 21, v21 - 1, 0, v20);
    v27 = _ccall(21, v21 - 1, 0, v20);
    v28 = v21;
    v29 = v27;
    v30 = v28 - 1;
    v31 = _ccall(0, 21, v28 - 1, 0, v27);
    v4 = v28;
    v6 = (g_1038c808 ^ g_1038c80c) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f0730(v6);
}
```

## `sub_102f5b0f` `0x102f5b0f`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f5b0f(void)
{
}
```

## `sub_102f5b59` `0x102f5b59`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f5b59(void)
{
}
```

## `sub_102f5b68` `0x102f5b68`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f5b68(void)
{
}
```

## `sub_102f5bc0` `0x102f5bc0`

_167 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7dc;
extern unsigned int g_1038c7e0;

unsigned int sub_102f5bc0(int a0)
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

## `sub_102f5c70` `0x102f5c70`

_282 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c83c;
extern unsigned int g_1038c840;

unsigned int sub_102f5c70(int a0)
{
    unsigned int v5;  // ebx
    unsigned int v6;  // ecx
    unsigned int v16;  // 4672
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

    v3 = sub_102f2690(a0);
    v1 = v5;
    v0 = v6;
    v8 = _INSERT(_INSERT(v6, 1, 0), 0, 164);
    v9 = v8 * 0x1000000 | v8 * 0x100 & 0xff0000 | v8 >> 8 & 0xff00 | v8 >> 24 & 0xff;
    v10 = _INSERT(_INSERT(v3 & 0xffff, 1, 0) & 0xff, 0, ~(~((char)_INSERT(v3 & 0xffff, 1, 0))));
    v12 = v10 * 0x1000000 | v10 * 0x100 & 0xff0000 | v10 >> 8 & 0xff00 | v10 >> 24 & 0xff;
    v13 = _INSERT((char)v12 * 0 | (char)(v12 >> 24), 0, ((char)v12 * 0 | (char)(v12 >> 24)) & (char)~(~(_INSERT((char)v9 * 0 | (char)(v9 >> 24), 0, ((char)v9 * 0 | (char)(v9 >> 24)) - 38))) + 2);
    v1 = -(0 < v13) + 1;
    v14 = -(0 < (v3 & 0x600)) + 1;
    v16 = _ccall(0, 6, -((unsigned int)(char)(0 < v13)) + 1, v14, 0);
    v2 = (-(0 < v13) + 1 == v14 ? 0 : 1);
    v4 = (g_1038c83c ^ g_1038c840) * 2;
    if (v2)
        v4 |= 1;
    return sub_102f2570(v4);
}
```

## `sub_102f5d90` `0x102f5d90`

_126 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e8;
extern unsigned int g_1038c7ec;

unsigned int sub_102f5d90(int a0)
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
    v4 = sub_102ef640(a0);
    v1 = v6;
    v7 = v4 * 0x1000000 | v4 * 0x100 & 0xff0000 | v4 >> 8 & 0xff00 | v4 >> 24 & 0xff;
    v0 = v8;
    v3 = -(-(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & ~(~(114)) + 14)));
    v5 = (g_1038c7e8 ^ g_1038c7ec) * 2;
    if (v3)
        v5 |= 1;
    return sub_102ef530(v5);
}
```

## `sub_102f5db2` `0x102f5db2`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102f5db2(void)
{
}
```

## `sub_102f5e20` `0x102f5e20`

_208 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c81c;
extern unsigned int g_1038c820;

int sub_102f5e20(unsigned int a0)
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

    v4 = sub_102f1120(a0);
    v2 = v6;
    v1 = v7;
    v0 = _INSERT(v4 & 0xffff, 1, 0);
    v9 = _ccall(0, 19, 90, 0, 0);
    v13 = _INSERT(v0, 0, (char)v0 & (char)~(~(_INSERT(90 CONCAT 0, 0, 64))));
    v3 = -(0 < v13) + 1;
    v5 = (g_1038c81c ^ g_1038c820) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0ff0(v5);
}
```

## `sub_102f5e83` `0x102f5e83`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f5e83(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f5f00` `0x102f5f00`

_127 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c804;
extern unsigned int g_1038c808;

unsigned int sub_102f5f00(int a0)
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
    v4 = sub_102f0650(a0);
    v1 = v6;
    v7 = v4 * 0x1000000 | v4 * 0x100 & 0xff0000 | v4 >> 8 & 0xff00 | v4 >> 24 & 0xff;
    v0 = v8;
    v3 = -(-(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & ~(~(50)) + 15)));
    v5 = (g_1038c804 ^ g_1038c808) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0570(v5);
}
```

## `sub_102f5f22` `0x102f5f22`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102f5f22(void)
{
}
```

## `sub_102f5f90` `0x102f5f90`

_214 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c800;
extern unsigned int g_1038c804;

int sub_102f5f90(unsigned int a0)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // eax
    unsigned int v8;  // ecx
    int v9;  // edx
    unsigned int v10;  // 4316
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
    v4 = sub_102f04d0(a0);
    v1 = v6;
    v7 = v4 * 0x1000000 | v4 * 0x100 & 0xff0000 | v4 >> 8 & 0xff00 | v4 >> 24 & 0xff;
    v0 = v8;
    v2 = -(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & ~(~(114)) + 14)) + 1;
    v9 = -(0 < (v4 & 0xf900)) + 1;
    v10 = _ccall(0, 15, 0, 0, 0);
    v11 = -(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & ~(~(114)) + 14)) + 1;
    v12 = _ccall(0, 6, -((unsigned int)(char)(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & ~(~(114)) + 14))) + 1, v9, 0);
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
    v5 = (g_1038c800 ^ g_1038c804) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0430(v5);
}
```

## `sub_102f5fb2` `0x102f5fb2`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102f5fb2(void)
{
}
```

## `sub_102f6070` `0x102f6070`

_159 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7ec;
extern unsigned int g_1038c7f0;

int sub_102f6070(unsigned int a0)
{
    unsigned int v4;  // edx
    unsigned int v6;  // eax
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v2 = sub_102ef8d0(a0);
    v0 = v4;
    v6 = _INSERT(_INSERT(v2 & 0xff, 0, (char)v2 & 1), 1, 0);
    v1 = v6;
    v3 = (g_1038c7ec ^ g_1038c7f0) * 2;
    if (v1)
        v3 |= 1;
    return sub_102ef750(v3);
}
```

## `sub_102f6110` `0x102f6110`

_388 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7dc;
extern unsigned int g_1038c7e0;

unsigned int sub_102f6110(int a0)
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
    unsigned int v12;  // 4299
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v5 = sub_102ef020(a0);
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
            goto LABEL_102f625c;
        v27 = 0;
    }
    else
    {
LABEL_102f625c:
        v27 = 1;
    }
    v4 = v27;
    v6 = (g_1038c7dc ^ g_1038c7e0) * 2;
    if (v4)
        v6 |= 1;
    return sub_102eef00(v6);
}
```

## `sub_102f6170` `0x102f6170`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f6170(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

