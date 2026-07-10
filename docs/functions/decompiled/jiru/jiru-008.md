# elfbot.dll decompiled — jiru 0x102fa9c0..0x102fc36d

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_102fa9c0` `0x102fa9c0`

_186 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7ec;
extern unsigned int g_1038c7f0;

int sub_102fa9c0(unsigned int a0)
{
    unsigned int v8;  // edx
    unsigned int v9;  // ebx
    unsigned int v11;  // eax
    unsigned int v12;  // 4206
    unsigned short v13;  // bx
    unsigned int v14;  // eax
    unsigned int v15;  // eax
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v2 = a0;
    v5 = sub_102ef8d0(a0);
    v2 = v8;
    v1 = v9;
    v0 = v5 & 0xffff;
    v11 = _INSERT(v0, 1, 0);
    v12 = _ccall(0, 13, 0, 0, 0);
    v13 = _INSERT(_INSERT(*((unsigned short *)((void*)&v9 + 1)), 1, 0), 0, 128);
    v14 = v11 * 0x1000000 | v11 * 0x100 & 0xff0000 | v11 >> 8 & 0xff00 | v11 >> 24 & 0xff;
    v15 = _INSERT((char)v14 * 0 | (char)(v14 >> 24), 0, ((char)v14 * 0 | (char)(v14 >> 24)) & (char)~(~(v13)));
    v4 = -(-(0 < v15));
    v6 = (g_1038c7ec ^ g_1038c7f0) * 2;
    if (v4)
        v6 |= 1;
    return sub_102ef750(v6);
}
```

## `sub_102fa9e0` `0x102fa9e0`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fa9e0(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102faa11` `0x102faa11`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102faa11(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102faa80` `0x102faa80`

_168 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7f8;
extern unsigned int g_1038c7fc;

int sub_102faa80(unsigned int a0)
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

    v4 = sub_102effb0(a0);
    v2 = v6;
    v1 = v7;
    v0 = v4 & 0xffff;
    v9 = _INSERT(v0, 1, 0);
    v10 = _INSERT(_INSERT(*((unsigned short *)((void*)&v7 + 1)), 1, 0), 0, 64);
    v11 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v12 = _INSERT((char)v11 * 0 | (char)(v11 >> 24), 0, ((char)v11 * 0 | (char)(v11 >> 24)) & (char)~(~(v10)));
    v3 = -(-(0 < v12));
    v5 = (g_1038c7f8 ^ g_1038c7fc) * 2;
    if (v3)
        v5 |= 1;
    return sub_102efe30(v5);
}
```

## `sub_102fab30` `0x102fab30`

_209 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c82c;
extern unsigned int g_1038c830;

unsigned int sub_102fab30(int a0)
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
    unsigned int v15;  // 4399
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f1b90(a0);
    v2 = v6;
    v1 = v7;
    v0 = v4 & 0xffff;
    v9 = _INSERT(v0, 1, 0);
    v10 = _INSERT(_INSERT(*((unsigned short *)((void*)&v7 + 1)), 1, 0), 0, 128);
    v11 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v12 = _INSERT((char)v11 * 0 | (char)(v11 >> 24), 0, ((char)v11 * 0 | (char)(v11 >> 24)) & (char)~(~(v10)));
    v2 = -(0 < v12) + 1;
    v13 = -(0 < (v4 & 0x300)) + 1;
    v14 = -(0 < v12) + 1;
    v15 = _ccall(0, 15, 0, 0, 0);
    v16 = _ccall(0, 6, v14, v13, 0);
    v17 = _ccall(5, 6, v14, v13, 0);
    v3 = _INSERT(v14, 0, v17);
    v5 = (g_1038c82c ^ g_1038c830) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f1a10(v5);
}
```

## `sub_102fabb7` `0x102fabb7`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fabb7(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fac10` `0x102fac10`

_193 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c828;
extern unsigned int g_1038c82c;

unsigned int sub_102fac10(int a0)
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

    v4 = sub_102f1910(a0);
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
    v5 = (g_1038c828 ^ g_1038c82c) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f1810(v5);
}
```

## `sub_102fac7d` `0x102fac7d`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fac7d(void)
{
}
```

## `sub_102fac8c` `0x102fac8c`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fac8c(void)
{
}
```

## `sub_102face0` `0x102face0`

_134 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c808;
extern unsigned int g_1038c80c;

unsigned int sub_102face0(int a0)
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
    v3 = -(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & ~(~(50)) + 14)) + 1;
    v5 = (g_1038c808 ^ g_1038c80c) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0730(v5);
}
```

## `sub_102fad02` `0x102fad02`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102fad02(void)
{
}
```

## `sub_102fad70` `0x102fad70`

_200 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c800;
extern unsigned int g_1038c804;

int sub_102fad70(unsigned int a0)
{
    unsigned short v6;  // ax
    unsigned int v7;  // edx
    unsigned int v18;  // eax
    unsigned int v19;  // 4203
    unsigned int v20;  // eax
    unsigned int v23;  // 4204
    unsigned int v8;  // cc_dep1
    unsigned int v26;  // 4119
    unsigned int v27;  // eax
    unsigned int v30;  // 4120
    unsigned int v33;  // 4135
    unsigned int v34;  // eax
    unsigned int v35;  // cc_ndep
    unsigned int v9;  // ebx
    unsigned int v36;  // cc_dep1
    unsigned int v37;  // 4136
    char v10;  // bl
    unsigned int v11;  // 4130
    unsigned int v12;  // 4147
    unsigned int v13;  // cc_ndep
    unsigned int v14;  // cc_dep1
    unsigned int v15;  // 4149
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f04d0(a0);
    v6 = v4;
    v2 = v7;
    v8 = v6;
    v1 = v9;
    v0 = 33;
    v10 = v0;
    v11 = _ccall(0, 15, (unsigned int)v6, 0, 0);
    v0 = v6;
    v12 = _ccall(19, (unsigned int)(v10 - 9), 0, (unsigned int)(char)(v10 - 6 < 2));
    v13 = v12;
    v14 = v10 - 10;
    v15 = _ccall(0, 19, (unsigned int)(v10 - 10), 0, v12);
    v18 = _INSERT((char)v0 & v10 - 33, 1, (char)v0 & v10 - 33 & 247);
    v19 = _ccall(12, 0, (unsigned int)(char)(0 < v18), (unsigned int)(char)(0 < v18));
    v20 = -(0 < v18) + 1;
    v23 = _ccall(0, 21, v20 - 1, 0, v19);
    v26 = _ccall(21, v20 - 1, 0, v19);
    v27 = v20;
    v30 = _ccall(0, 21, v27 - 1, 0, v26);
    v33 = _ccall(21, v27 - 1, 0, v26);
    v34 = v27;
    v35 = v33;
    v36 = v34 - 1;
    v37 = _ccall(0, 21, v34 - 1, 0, v33);
    v3 = v34;
    v5 = (g_1038c800 ^ g_1038c804) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0430(v5);
}
```

## `sub_102fad9c` `0x102fad9c`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fad9c(void)
{
}
```

## `sub_102fadb6` `0x102fadb6`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fadb6(void)
{
}
```

## `sub_102fadea` `0x102fadea`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fadea(void)
{
}
```

## `sub_102fadf9` `0x102fadf9`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fadf9(void)
{
}
```

## `sub_102fae50` `0x102fae50`

_213 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c800;
extern unsigned int g_1038c804;

int sub_102fae50(unsigned int a0)
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

    v4 = sub_102f04d0(a0);
    v2 = v6;
    v1 = v7;
    v0 = v4 & 0xffff;
    v9 = _INSERT(v0, 1, 0);
    v10 = _INSERT(_INSERT(*((unsigned short *)((void*)&v7 + 1)), 1, 0), 0, 64);
    v11 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v12 = _INSERT((char)v11 * 0 | (char)(v11 >> 24), 0, ((char)v11 * 0 | (char)(v11 >> 24)) & (char)~(~(v10)));
    v3 = -(-(0 < v12));
    v5 = (g_1038c800 ^ g_1038c804) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0430(v5);
}
```

## `sub_102faf30` `0x102faf30`

_220 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7fc;
extern unsigned int g_1038c800;

unsigned int sub_102faf30(unsigned int a0)
{
    unsigned int v7;  // ebx
    unsigned int v16;  // cc_dep1
    unsigned int v17;  // 4281
    unsigned int v8;  // ecx
    unsigned int v10;  // ecx
    unsigned int v11;  // ecx
    char v12;  // cl
    unsigned int v13;  // 4268
    unsigned int v14;  // 4274
    unsigned int v15;  // cc_ndep
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v1 = a0;
    v4 = sub_102f02b0(a0);
    v1 = v7;
    v0 = v8;
    v10 = _INSERT(_INSERT(v8, 1, 0), 0, 101);
    v11 = v10 * 0x1000000 | v10 * 0x100 & 0xff0000 | v10 >> 8 & 0xff00 | v10 >> 24 & 0xff;
    v12 = (char)v11 * 0 | (char)(v11 >> 24);
    v13 = _ccall(1, (unsigned int)(v12 - 20), 11, 0);
    v14 = _ccall(19, (unsigned int)(v12 - 10), 0, v13);
    v15 = v14;
    v16 = v12 - 11;
    v17 = _ccall(0, 19, (unsigned int)(v12 - 11), 0, v14);
    v3 = 1;
    v5 = (g_1038c7fc ^ g_1038c800) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0130(v5);
}
```

## `sub_102faf50` `0x102faf50`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102faf50(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fb010` `0x102fb010`

_158 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c838;
extern unsigned int g_1038c83c;

int sub_102fb010(unsigned int a0)
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

    v3 = sub_102f2420(a0);
    v1 = v5;
    v6 = v3 * 0x1000000 | v3 * 0x100 & 0xff0000 | v3 >> 8 & 0xff00 | v3 >> 24 & 0xff;
    v7 = (char)(~(~(75)) + 15) + 3;
    v8 = _INSERT(v7 + 13, 0, v7 + 18);
    v0 = v9;
    v2 = -(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 0x11)) + 1;
    v4 = (g_1038c838 ^ g_1038c83c) * 2;
    if (!(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 0x11)) != 4294967295)
        v4 |= 1;
    return sub_102f22d0(v4);
}
```

## `sub_102fb0b0` `0x102fb0b0`

_382 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e0;
extern unsigned int g_1038c7e4;

int sub_102fb0b0(unsigned int a0)
{
    unsigned int v7;  // edx
    unsigned int v8;  // ebx
    unsigned int v17;  // eax
    unsigned int v18;  // eax
    unsigned short v19;  // ax
    unsigned int v20;  // cc_dep1
    char v21;  // bl
    unsigned int v22;  // 4352
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

    v5 = sub_102ef270(a0);
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
            goto LABEL_102fb200;
        v52 = 0;
    }
    else
    {
LABEL_102fb200:
        v52 = 1;
    }
    v4 = v52;
    v6 = (g_1038c7e0 ^ g_1038c7e4) * 2;
    if (v4)
        v6 |= 1;
    return sub_102ef140(v6);
}
```

## `sub_102fb185` `0x102fb185`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fb185(void)
{
}
```

## `sub_102fb19c` `0x102fb19c`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fb19c(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fb1d0` `0x102fb1d0`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fb1d0(void)
{
}
```

## `sub_102fb1df` `0x102fb1df`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fb1df(void)
{
}
```

## `sub_102fb240` `0x102fb240`

_125 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7f8;
extern unsigned int g_1038c7fc;

int sub_102fb240(unsigned int a0)
{
    unsigned int v4;  // edx
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v2 = sub_102effb0(a0);
    v0 = v4;
    v1 = _INSERT(_INSERT(v2, 1, 0) & 0xff, 0, (char)_INSERT(v2, 1, 0) & 1);
    v3 = (g_1038c7f8 ^ g_1038c7fc) * 2;
    if (v1)
        v3 |= 1;
    return sub_102efe30(v3);
}
```

## `sub_102fb2c0` `0x102fb2c0`

_390 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c828;
extern unsigned int g_1038c82c;

unsigned int sub_102fb2c0(int a0)
{
    unsigned int v9;  // ebx
    unsigned int v10;  // ecx
    unsigned int v19;  // cc_ndep
    unsigned int v20;  // cc_dep1
    unsigned int v21;  // 4309
    unsigned int v25;  // eax
    unsigned int v26;  // eax
    unsigned int v27;  // eax
    unsigned short v28;  // ax
    unsigned int v29;  // cc_dep1
    unsigned int v30;  // 4244
    int v32;  // eax
    unsigned int v33;  // 4250
    unsigned int v34;  // 4101
    unsigned int v35;  // eax
    unsigned int v12;  // ecx
    unsigned int v13;  // ecx
    unsigned int v14;  // eax
    char v15;  // cl
    unsigned int v16;  // 4290
    unsigned int v17;  // 4296
    unsigned int v18;  // 4302
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x28]
    unsigned int v2;  // [bp-0x24]
    unsigned int v3;  // [bp-0x20]
    int v4;  // [bp-0x1c]
    unsigned int v5;  // [bp-0x1c]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]

    v7 = sub_102f1910(a0);
    v3 = v9;
    v2 = v10;
    v12 = _INSERT(_INSERT(v10, 1, 0), 0, 101);
    v13 = v12 * 0x1000000 | v12 * 0x100 & 0xff0000 | v12 >> 8 & 0xff00 | v12 >> 24 & 0xff;
    v14 = _INSERT(_INSERT(v7 & 0xffff, 1, 0) & 0xff, 0, ~(~((char)_INSERT(v7 & 0xffff, 1, 0))));
    v15 = (char)v13 * 0 | (char)(v13 >> 24);
    v16 = _ccall(1, (unsigned int)(v15 - 20), 12, 0);
    v17 = _ccall(19, (unsigned int)(v15 - 9), 0, v16);
    v18 = _ccall(19, (unsigned int)(v15 - 10), 0, v17);
    v19 = v18;
    v20 = v15 - 11;
    v21 = _ccall(0, 19, (unsigned int)(v15 - 11), 0, v18);
    v25 = v14 * 0x1000000 | v14 * 0x100 & 0xff0000 | v14 >> 8 & 0xff00 | v14 >> 24 & 0xff;
    v26 = _INSERT((char)v25 * 0 | (char)(v25 >> 24), 0, ((char)v25 * 0 | (char)(v25 >> 24)) & (char)~(~(_INSERT(v15 - 11 CONCAT 0, 0, v15 - 40))) + 3);
    if (!v26)
    {
        v3 = v9;
        v27 = v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff;
        v4 = -(0 < ((v27 * 0x1000000 | v27 * 0x100 & 0xff0000 | v27 >> 8 & 0xff00 | v27 >> 24 & 0xff) & ~(~(114)) + 14)) + 1;
        v28 = v7;
        v3 = v5;
        v29 = v28;
        v2 = v9;
        v1 = 31;
        v30 = _ccall(0, 15, (unsigned int)v28, 0, 0);
        v0 = v28;
        v32 = -(0 < _INSERT((char)v0 & (char)v1 - 31, 1, (char)v0 & (char)v1 - 31 & 243)) + 1;
        v33 = _ccall(0, 6, v4, v32, 0);
        if (v4 != v32)
            goto LABEL_102fb41a;
        v34 = _ccall(0, 6, v4, v32, 0);
        v35 = 0;
    }
    else
    {
LABEL_102fb41a:
        v35 = 1;
    }
    v6 = v35;
    v8 = (g_1038c828 ^ g_1038c82c) * 2;
    if (v6)
        v8 |= 1;
    return sub_102f1810(v8);
}
```

## `sub_102fb378` `0x102fb378`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102fb378(void)
{
}
```

## `sub_102fb3bb` `0x102fb3bb`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fb3bb(void)
{
}
```

## `sub_102fb3ff` `0x102fb3ff`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fb3ff(void)
{
}
```

## `sub_102fb40e` `0x102fb40e`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fb40e(void)
{
}
```

## `sub_102fb460` `0x102fb460`

_197 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c810;
extern unsigned int g_1038c814;

unsigned int sub_102fb460(int a0)
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

    v5 = sub_102f0ba0(a0);
    v3 = v5;
    v3 = v7;
    v2 = v8;
    v1 = v9;
    v0 = v5;
    v4 = -(0 < _INSERT(_INSERT(v0, 1, 0) & 0xff, 0, (char)_INSERT(v0, 1, 0) & 1)) + 1;
    v6 = (g_1038c810 ^ g_1038c814) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f0a30(v6);
}
```

## `sub_102fb530` `0x102fb530`

_199 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c820;
extern unsigned int g_1038c824;

unsigned int sub_102fb530(int a0)
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

    v4 = sub_102f1390(a0);
    v2 = v6;
    v1 = v7;
    v0 = 15;
    v8 = _INSERT((char)v4 & (char)v0 - 15, 1, (char)v4 & (char)v0 - 15 & 8);
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
    v5 = (g_1038c820 ^ g_1038c824) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f1250(v5);
}
```

## `sub_102fb600` `0x102fb600`

_125 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7d8;
extern unsigned int g_1038c7dc;

unsigned int sub_102fb600(int a0)
{
    unsigned int v5;  // ebx
    unsigned int v6;  // eax
    unsigned int v7;  // ecx
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v3 = sub_102eed50(a0);
    v1 = v5;
    v6 = v3 * 0x1000000 | v3 * 0x100 & 0xff0000 | v3 >> 8 & 0xff00 | v3 >> 24 & 0xff;
    v0 = v7;
    v2 = -(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & ~(~(50)) + 15)) + 1;
    v4 = (g_1038c7d8 ^ g_1038c7dc) * 2;
    if (v2)
        v4 |= 1;
    return sub_102eebb0(v4);
}
```

## `sub_102fb622` `0x102fb622`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102fb622(void)
{
}
```

## `sub_102fb690` `0x102fb690`

_160 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c838;
extern unsigned int g_1038c83c;

int sub_102fb690(unsigned int a0)
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

    v4 = sub_102f2420(a0);
    v2 = v6;
    v1 = v7;
    v0 = v4 & 0xffff;
    v9 = _INSERT(v0, 1, 0);
    v10 = _INSERT(_INSERT(*((unsigned short *)((void*)&v7 + 1)), 1, 0), 0, 128);
    v11 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v12 = _INSERT((char)v11 * 0 | (char)(v11 >> 24), 0, ((char)v11 * 0 | (char)(v11 >> 24)) & (char)~(~(v10)));
    v3 = -(0 < v12) + 1;
    v5 = (g_1038c838 ^ g_1038c83c) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f22d0(v5);
}
```

## `sub_102fb730` `0x102fb730`

_125 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c83c;
extern unsigned int g_1038c840;

unsigned int sub_102fb730(int a0)
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
    v4 = sub_102f2690(a0);
    v1 = v6;
    v7 = v4 * 0x1000000 | v4 * 0x100 & 0xff0000 | v4 >> 8 & 0xff00 | v4 >> 24 & 0xff;
    v0 = v8;
    v3 = -(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & ~(~(50)) + 14)) + 1;
    v5 = (g_1038c83c ^ g_1038c840) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f2570(v5);
}
```

## `sub_102fb752` `0x102fb752`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102fb752(void)
{
}
```

## `sub_102fb7c0` `0x102fb7c0`

_140 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c830;
extern unsigned int g_1038c834;

int sub_102fb7c0(unsigned int a0, unsigned int a1)
{
    unsigned int v7;  // ebx
    unsigned int v8;  // edx
    unsigned int v9;  // 4142
    unsigned int v10;  // 4143
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v3 = v7;
    v5 = sub_102f1e90(a0);
    v2 = v8;
    v1 = v7;
    v0 = v5 & 0xffff;
    v9 = _ccall(6, 19, (unsigned int)(*((char *)((void*)&v7 + 1)) - 1), 0, 0);
    if (Conv(32I->1I, vvar_96)) { Goto None } else { Goto None }
    v10 = _ccall(0, 15, 0, 0, 0);
    if (Conv(32I->1I, vvar_97)) { Goto None } else { Goto None }
    v4 = 1;
    v6 = (g_1038c830 ^ g_1038c834) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f1d10(v6);
}
```

## `sub_102fb850` `0x102fb850`

_133 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c800;
extern unsigned int g_1038c804;

int sub_102fb850(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
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
    v6 = (g_1038c800 ^ g_1038c804) * 2;
    if (v5)
        v6 |= 1;
    return sub_102f0430(v6);
}
```

## `sub_102fb8e0` `0x102fb8e0`

_154 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c804;
extern unsigned int g_1038c808;

unsigned int sub_102fb8e0(int a0)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // ecx
    unsigned int v16;  // 4158
    unsigned int v8;  // 4159
    unsigned int v11;  // 4106
    unsigned int v12;  // eax
    unsigned int v13;  // 4108
    unsigned int v14;  // cc_dep1
    unsigned int v15;  // 4108
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f0650(a0);
    v2 = v6;
    v1 = v7;
    v0 = 127;
    v8 = _ccall(0, 19, 14, 0, 0);
    v11 = _ccall(0, 4, 14, 6, 0);
    v12 = _INSERT((char)v4 & (char)(v0 - 1 ^ 126), 1, (char)v4 & (char)(v0 - 1 ^ 126) & 8);
    if (v12)
    {
        v13 = _ccall(3, ~(v12), 1, 0);
        v14 = v13 | 1;
    }
    else
    {
        v15 = _ccall(3, ~(0), 1, 0);
        v14 = v15 & 4294967294;
    }
    v16 = _ccall(0, v14, 0, 0);
    v3 = -(v16 & 1) + 1;
    v5 = (g_1038c804 ^ g_1038c808) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0570(v5);
}
```

## `sub_102fb919` `0x102fb919`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fb919(void)
{
}
```

## `sub_102fb929` `0x102fb929`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fb929(void)
{
}
```

## `sub_102fb980` `0x102fb980`

_381 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c820;
extern unsigned int g_1038c824;

unsigned int sub_102fb980(int a0)
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
            goto LABEL_102fbac6;
        v27 = 1;
    }
    else
    {
LABEL_102fbac6:
        v27 = 0;
    }
    v4 = v27;
    v6 = (g_1038c820 ^ g_1038c824) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f1250(v6);
}
```

## `sub_102fb9e3` `0x102fb9e3`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fb9e3(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fbb00` `0x102fbb00`

_124 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e8;
extern unsigned int g_1038c7ec;

unsigned int sub_102fbb00(int a0)
{
    unsigned int v5;  // ebx
    unsigned int v6;  // ecx
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v3 = sub_102ef640(a0);
    v1 = v5;
    v0 = v6;
    v2 = 1;
    v4 = (g_1038c7e8 ^ g_1038c7ec) * 2;
    if (v2)
        v4 |= 1;
    return sub_102ef530(v4);
}
```

## `sub_102fbb22` `0x102fbb22`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102fbb22(void)
{
}
```

## `sub_102fbb90` `0x102fbb90`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c81c;
extern unsigned int g_1038c820;

int sub_102fbb90(unsigned int a0)
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

    v4 = sub_102f1120(a0);
    v2 = v6;
    v1 = v7;
    v0 = _INSERT(v4 & 0xffff, 1, 0);
    v10 = _INSERT(_INSERT(v7, 1, 0), 0, 125);
    v11 = _INSERT(v0, 0, (char)v0 & (char)~(~(v10)) + 3);
    v2 = -(0 < v11) + 1;
    v3 = _INSERT(-(0 < v11) + 1, 0, -(0 < v11) + 1 == -(0 < (v4 & 0xfc00)) + 1);
    v5 = (g_1038c81c ^ g_1038c820) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0ff0(v5);
}
```

## `sub_102fbca0` `0x102fbca0`

_156 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c804;
extern unsigned int g_1038c808;

unsigned int sub_102fbca0(int a0)
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

## `sub_102fbd40` `0x102fbd40`

_165 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c814;
extern unsigned int g_1038c818;

unsigned int sub_102fbd40(int a0)
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

    v4 = sub_102f0dc0(a0);
    v2 = v6;
    v1 = v7;
    v0 = v4 & 0xffff;
    v9 = _INSERT(v0, 1, 0);
    v10 = _INSERT(_INSERT(*((unsigned short *)((void*)&v7 + 1)), 1, 0), 0, 65);
    v11 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v12 = _INSERT((char)v11 * 0 | (char)(v11 >> 24), 0, ((char)v11 * 0 | (char)(v11 >> 24)) & (char)~(~(v10)));
    v3 = -(0 < v12) + 1;
    v5 = (g_1038c814 ^ g_1038c818) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0d10(v5);
}
```

## `sub_102fbdf0` `0x102fbdf0`

_440 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c804;
extern unsigned int g_1038c808;

unsigned int sub_102fbdf0(int a0)
{
    unsigned int v8;  // ebx
    unsigned int v9;  // ecx
    unsigned int v18;  // cc_ndep
    unsigned int v19;  // cc_dep1
    unsigned int v20;  // 4309
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
    unsigned int v35;  // 4526
    unsigned int v36;  // eax
    unsigned int v11;  // ecx
    unsigned int v39;  // 4527
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
    unsigned int v15;  // 4290
    unsigned int v16;  // 4296
    unsigned int v17;  // 4302
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x1c]
    unsigned int v4;  // [bp-0x18]
    unsigned int v5;  // [bp-0x10]
    int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]

    v6 = sub_102f0650(a0);
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
            goto LABEL_102fbf74;
        v56 = 0;
    }
    else
    {
LABEL_102fbf74:
        v56 = 1;
    }
    v5 = v56;
    v7 = (g_1038c804 ^ g_1038c808) * 2;
    if (v5)
        v7 |= 1;
    return sub_102f0570(v7);
}
```

## `sub_102fbfb0` `0x102fbfb0`

_256 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c814;
extern unsigned int g_1038c818;

unsigned int sub_102fbfb0(int a0)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // ecx
    unsigned int v10;  // ecx
    unsigned int v11;  // eax
    int v12;  // edx
    int v13;  // eax
    unsigned int v14;  // 4569
    unsigned int v15;  // 4150
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f0dc0(a0);
    v2 = v6;
    v1 = v7;
    v0 = _INSERT(v4 & 0xffff, 1, 0);
    v10 = _INSERT(_INSERT(v7, 1, 0), 0, 128);
    v11 = _INSERT(v0, 0, (char)v0 & (char)~(~(v10)));
    v2 = -(0 < v11) + 1;
    v12 = -(0 < (v4 & 0xfc00)) + 1;
    v13 = -(0 < v11) + 1;
    v14 = _ccall(0, 6, v13, v12, 0);
    v15 = _ccall(5, 6, v13, v12, 0);
    v3 = _INSERT(v13, 0, v15);
    v5 = (g_1038c814 ^ g_1038c818) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0d10(v5);
}
```

## `sub_102fc0c0` `0x102fc0c0`

_179 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7f8;
extern unsigned int g_1038c7fc;

int sub_102fc0c0(unsigned int a0)
{
    unsigned short v6;  // ax
    unsigned int v7;  // edx
    unsigned int v16;  // eax
    unsigned int v8;  // cc_dep1
    unsigned int v9;  // ebx
    unsigned int v10;  // 4127
    unsigned int v12;  // eax
    unsigned short v13;  // bx
    unsigned int v14;  // eax
    unsigned int v15;  // 4276
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102effb0(a0);
    v6 = v4;
    v2 = v7;
    v8 = v6;
    v1 = v9;
    v0 = v6;
    v10 = _ccall(0, 15, (unsigned int)v6, 0, 0);
    v12 = _INSERT(v0, 1, 0);
    v13 = _INSERT(_INSERT(*((unsigned short *)((void*)&v9 + 1)), 1, 0), 0, 65);
    v14 = v12 * 0x1000000 | v12 * 0x100 & 0xff0000 | v12 >> 8 & 0xff00 | v12 >> 24 & 0xff;
    v15 = _ccall(0, 4, 95, 30, 0);
    v16 = _INSERT((char)v14 * 0 | (char)(v14 >> 24), 0, ((char)v14 * 0 | (char)(v14 >> 24)) & (char)~(~(v13)));
    v3 = -(0 < v16) + 1;
    v5 = (g_1038c7f8 ^ g_1038c7fc) * 2;
    if (v3)
        v5 |= 1;
    return sub_102efe30(v5);
}
```

## `sub_102fc0ec` `0x102fc0ec`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fc0ec(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fc130` `0x102fc130`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fc130(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fc180` `0x102fc180`

_141 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c830;
extern unsigned int g_1038c834;

int sub_102fc180(unsigned int a0)
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
    v0 = 5;
    v8 = _INSERT((char)v4 & (char)v0 - 5, 1, (char)v4 & (char)v0 - 5 & 8);
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

## `sub_102fc210` `0x102fc210`

_159 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c81c;
extern unsigned int g_1038c820;

int sub_102fc210(unsigned int a0)
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

    v3 = sub_102f1120(a0);
    v1 = v5;
    v6 = v3 * 0x1000000 | v3 * 0x100 & 0xff0000 | v3 >> 8 & 0xff00 | v3 >> 24 & 0xff;
    v7 = (char)(~(~(75)) + 15) + 3;
    v8 = _INSERT(v7 + 13, 0, v7 + 18);
    v0 = v9;
    v2 = -(-(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 0x11)));
    v4 = (g_1038c81c ^ g_1038c820) * 2;
    if (0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 0x11))
        v4 |= 1;
    return sub_102f0ff0(v4);
}
```

## `sub_102fc2b0` `0x102fc2b0`

_480 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e4;
extern unsigned int g_1038c7e8;

unsigned int sub_102fc2b0(unsigned int a0)
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
    v6 = sub_102ef460(a0);
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
            goto LABEL_102fc468;
        v69 = 0;
    }
    else
    {
LABEL_102fc468:
        v69 = 1;
    }
    v5 = v69;
    v7 = (g_1038c7e4 ^ g_1038c7e8) * 2;
    if (v5)
        v7 |= 1;
    return sub_102ef3a0(v7);
}
```

## `sub_102fc2d0` `0x102fc2d0`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fc2d0(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102fc36d` `0x102fc36d`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102fc36d(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

