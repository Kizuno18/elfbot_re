# elfbot.dll decompiled — jiru 0x102ff13b..0x10300e10

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_102ff13b` `0x102ff13b`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102ff13b(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102ff180` `0x102ff180`

_143 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c808;
extern unsigned int g_1038c80c;

unsigned int sub_102ff180(int a0)
{
    unsigned int v5;  // ecx
    unsigned int v6;  // edx
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v3 = sub_102f07c0(a0);
    v1 = v5;
    v0 = v6;
    v2 = 1;
    v4 = (g_1038c808 ^ g_1038c80c) * 2;
    if (v2)
        v4 |= 1;
    return sub_102f0730(v4);
}
```

## `sub_102ff210` `0x102ff210`

_206 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c810;
extern unsigned int g_1038c814;

unsigned int sub_102ff210(int a0)
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

    v4 = sub_102f0ba0(a0);
    v2 = v6;
    v1 = v7;
    v0 = _INSERT(v4 & 0xffff, 1, 0);
    v9 = _ccall(19, 91, 0, 0);
    v10 = v9;
    v11 = _ccall(0, 19, 90, 0, v9);
    v15 = _INSERT(v0, 0, (char)v0 & (char)~(~(_INSERT(90 CONCAT 0, 0, 65))));
    v3 = -(0 < v15) + 1;
    v5 = (g_1038c810 ^ g_1038c814) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0a30(v5);
}
```

## `sub_102ff273` `0x102ff273`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102ff273(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102ff2e0` `0x102ff2e0`

_154 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7d8;
extern unsigned int g_1038c7dc;

unsigned int sub_102ff2e0(int a0)
{
    unsigned int v4;  // ecx
    unsigned int v5;  // cc_ndep
    unsigned int v6;  // cc_dep1
    unsigned int v9;  // ecx
    unsigned int v10;  // cc_dep1
    unsigned int v11;  // 4179
    unsigned int v12;  // edx
    unsigned int v0;  // [bp-0x18]
    int <0x102ff2e0[is_2]|Stack bp-0x10, 1 B>;  // [bp-0x10]
    unsigned int v1;  // [bp-0x10]
    int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v2 = sub_102eed50(a0);
    v4 = ~(~(12)) + 2;
    v5 = &<0x102ff2e0[is_2]|Stack bp-0x10, 1 B> < &/* unsupported instruction */;
    v6 = v4 + 1;
    v9 = _INSERT(v4 + 5, 0, (char)(v4 + 5) + 3);
    v10 = v9 & 64;
    v11 = _ccall(0, 15, v9 & 64, 0, 0);
    v0 = v12;
    v1 = 1;
    v3 = (g_1038c7d8 ^ g_1038c7dc) * 2;
    if (v1)
        v3 |= 1;
    return sub_102eebb0(v3);
}
```

## `sub_102ff313` `0x102ff313`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102ff313(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102ff32f` `0x102ff32f`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102ff32f(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102ff380` `0x102ff380`

_343 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c840;
extern unsigned int g_1038c844;

unsigned int sub_102ff380(int a0)
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
    v7 = sub_102f2940(a0);
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
            goto LABEL_102ff4a1;
        v25 = 0;
    }
    else
    {
LABEL_102ff4a1:
        v25 = 1;
    }
    v6 = v25;
    v8 = (g_1038c840 ^ g_1038c844) * 2;
    if (v6)
        v8 |= 1;
    return sub_102f27b0(v8);
}
```

## `sub_102ff45f` `0x102ff45f`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102ff45f(void)
{
}
```

## `sub_102ff4e0` `0x102ff4e0`

_196 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c804;
extern unsigned int g_1038c808;

unsigned int sub_102ff4e0(int a0)
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

    v4 = sub_102f0650(a0);
    v2 = v6;
    v1 = v7;
    v0 = _INSERT(v4 & 0xffff, 1, 0);
    v10 = _INSERT(_INSERT(v7, 1, 0), 0, 65);
    v11 = _INSERT(v0, 0, (char)v0 & (char)~(~(v10)));
    v3 = -(0 < v11) + 1;
    v5 = (g_1038c804 ^ g_1038c808) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0570(v5);
}
```

## `sub_102ff5b0` `0x102ff5b0`

_157 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c800;
extern unsigned int g_1038c804;

int sub_102ff5b0(unsigned int a0)
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

    v3 = sub_102f04d0(a0);
    v1 = v5;
    v6 = v3 * 0x1000000 | v3 * 0x100 & 0xff0000 | v3 >> 8 & 0xff00 | v3 >> 24 & 0xff;
    v7 = (char)(~(~(13)) + 0x11) + 3;
    v8 = _INSERT(v7 + 13, 0, v7 + 18);
    v0 = v9;
    v2 = -(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 14)) + 1;
    v4 = (g_1038c800 ^ g_1038c804) * 2;
    if (!(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 14)) != 4294967295)
        v4 |= 1;
    return sub_102f0430(v4);
}
```

## `sub_102ff650` `0x102ff650`

_207 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c80c;
extern unsigned int g_1038c810;

unsigned int sub_102ff650(int a0)
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
    v8 = _INSERT(_INSERT(v6, 1, 0), 0, 101);
    v9 = v8 * 0x1000000 | v8 * 0x100 & 0xff0000 | v8 >> 8 & 0xff00 | v8 >> 24 & 0xff;
    v10 = _INSERT(_INSERT(v3 & 0xffff, 1, 0) & 0xff, 0, ~(~((char)_INSERT(v3 & 0xffff, 1, 0))));
    v12 = v10 * 0x1000000 | v10 * 0x100 & 0xff0000 | v10 >> 8 & 0xff00 | v10 >> 24 & 0xff;
    v13 = _INSERT((char)v12 * 0 | (char)(v12 >> 24), 0, ((char)v12 * 0 | (char)(v12 >> 24)) & (char)~(~(_INSERT(((char)v9 * 0 | (char)(v9 >> 24)) - 2 CONCAT 0, 0, ((char)v9 * 0 | (char)(v9 >> 24)) - 39))) + 3);
    v2 = -(0 < v13) + 1;
    v4 = (g_1038c80c ^ g_1038c810) * 2;
    if (v2)
        v4 |= 1;
    return sub_102f0850(v4);
}
```

## `sub_102ff6aa` `0x102ff6aa`

_3 bytes. (leaf/helper — see body)_

```c
int sub_102ff6aa(void)
{
}
```

## `sub_102ff730` `0x102ff730`

_179 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c834;
extern unsigned int g_1038c838;

int sub_102ff730(unsigned int a0)
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

    v3 = sub_102f2170(a0);
    v1 = v5;
    v0 = v3;
    v1 = v6;
    v7 = v0 * 0x1000000 | v0 * 0x100 & 0xff0000 | v0 >> 8 & 0xff00 | v0 >> 24 & 0xff;
    v9 = _INSERT(_INSERT((char)v7 * 0 | (char)(v7 >> 24), 0, ((char)v7 * 0 | (char)(v7 >> 24)) & 1), 1, 255);
    v10 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v2 = _INSERT((char)v10 * 0 | (char)(v10 >> 24), 1, ~((char)v10 * 0 | (char)(v10 >> 24)));
    v4 = (g_1038c834 ^ g_1038c838) * 2;
    if (v2)
        v4 |= 1;
    return sub_102f2010(v4);
}
```

## `sub_102ff7f0` `0x102ff7f0`

_134 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c808;
extern unsigned int g_1038c80c;

unsigned int sub_102ff7f0(int a0)
{
    unsigned int v4;  // cc_ndep
    unsigned int v5;  // 4129
    unsigned int v9;  // eax
    unsigned int v10;  // eax
    int v0;  // [bp-0x18]
    int <0x102fe6e0[is_2]|Stack bp-0x10, 1 B>;  // [bp-0x10]
    unsigned int v1;  // [bp-0x10]
    int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v2 = sub_102f07c0(a0);
    v4 = &<0x102fe6e0[is_2]|Stack bp-0x10, 1 B> < &/* unsupported instruction */;
    v5 = _ccall(0, 19, 5, 0, (unsigned int)(char)(&<0x102fe6e0[is_2]|Stack bp-0x10, 1 B> < &/* unsupported instruction */));
    v0 = v2;
    v9 = _INSERT(_INSERT(v0, 0, (char)v0 & 1), 1, ~(0));
    v10 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v1 = _INSERT((char)v10 * 0 | (char)(v10 >> 24), 1, ~((char)v10 * 0 | (char)(v10 >> 24)));
    v3 = (g_1038c808 ^ g_1038c80c) * 2;
    if (v1)
        v3 |= 1;
    return sub_102f0730(v3);
}
```

## `sub_102ff814` `0x102ff814`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102ff814(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102ff880` `0x102ff880`

_397 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c824;
extern unsigned int g_1038c828;

int sub_102ff880(unsigned int a0)
{
    unsigned int v8;  // edx
    unsigned int v9;  // ebx
    char v18;  // al
    unsigned int v19;  // 4158
    int v20;  // cc_dep1
    unsigned int v21;  // eax
    unsigned int v22;  // 4105
    unsigned int v23;  // 4106
    unsigned int v25;  // eax
    unsigned int v26;  // eax
    unsigned short v27;  // ax
    unsigned int v28;  // cc_dep1
    unsigned int v29;  // 4222
    unsigned int v30;  // 4199
    unsigned int v33;  // 4106
    unsigned int v34;  // eax
    unsigned int v35;  // 4149
    unsigned int v36;  // eax
    unsigned int v11;  // eax
    unsigned int v39;  // 4150
    unsigned int v42;  // 4151
    unsigned int v43;  // eax
    unsigned int v44;  // cc_ndep
    unsigned int v45;  // cc_dep1
    unsigned int v46;  // 4152
    unsigned short v12;  // bx
    unsigned int v49;  // eax
    unsigned int v13;  // eax
    unsigned int v14;  // eax
    unsigned int v15;  // eax
    char v16;  // bl
    unsigned int v17;  // cc_dep1
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x1c]
    unsigned int v4;  // [bp-0x18]
    unsigned int v5;  // [bp-0x10]
    int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]

    v6 = sub_102f1670(a0);
    v4 = v8;
    v3 = v9;
    v2 = v6 & 0xffff;
    v11 = _INSERT(v2, 1, 0);
    v12 = _INSERT(_INSERT(*((unsigned short *)((void*)&v9 + 1)), 1, 0), 0, 64);
    v13 = v11 * 0x1000000 | v11 * 0x100 & 0xff0000 | v11 >> 8 & 0xff00 | v11 >> 24 & 0xff;
    v14 = _INSERT((char)v13 * 0 | (char)(v13 >> 24), 0, ((char)v13 * 0 | (char)(v13 >> 24)) & (char)~(~(v12)));
    if (!v14)
    {
        v4 = v8;
        v15 = v6 & 0xffff;
        v2 = v15;
        v16 = _INSERT(*((unsigned short *)((void*)&v3 + 1)), 1, 0);
        v17 = v15 & 65;
        v18 = v2;
        v19 = _ccall(0, 15, v15 & 65, 0, 0);
        v20 = v18 & v16;
        v21 = _INSERT(v18, 1, v18 & v16);
        v22 = _ccall(0, 13, (unsigned int)(v18 & v16), 0, 0);
        v23 = _ccall(0, 4, 151, 3, 0);
        v25 = v21 * 0x1000000 | v21 * 0x100 & 0xff0000 | v21 >> 8 & 0xff00 | v21 >> 24 & 0xff;
        v26 = _INSERT((char)v25 * 0 | (char)(v25 >> 24), 0, ((char)v25 * 0 | (char)(v25 >> 24)) & (char)~(~(_INSERT(148 CONCAT 0, 0, 0x88))));
        v4 = -(0 < v26) + 1;
        v27 = v6;
        v3 = v8;
        v28 = v27;
        v2 = v3;
        v0 = 31;
        v29 = _ccall(0, 15, (unsigned int)v27, 0, 0);
        v1 = v27;
        v30 = _ccall(0, 19, 253, 0, 0);
        v33 = _ccall(0, 4, 253, 7, 0);
        v34 = _INSERT((char)v1 & (char)v0 - 31, 1, (char)v1 & (char)v0 - 31 & 246);
        v35 = _ccall(12, 0, (unsigned int)(char)(0 < v34), (unsigned int)(char)(0 < v34));
        v36 = -(0 < v34) + 1;
        v39 = _ccall(0, 21, v36 - 1, 0, v35);
        v42 = _ccall(21, v36 - 1, 0, v35);
        v43 = v36;
        v44 = v42;
        v45 = v43 - 1;
        v46 = _ccall(0, 21, v43 - 1, 0, v42);
        if (-(0 < v26) + 1 != v43)
            goto LABEL_102ff9eb;
        v49 = 1;
    }
    else
    {
LABEL_102ff9eb:
        v49 = 0;
    }
    v5 = v49;
    v7 = (g_1038c824 ^ g_1038c828) * 2;
    if (v5)
        v7 |= 1;
    return sub_102f14d0(v7);
}
```

## `sub_102ff911` `0x102ff911`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102ff911(void)
{
}
```

## `sub_102ff920` `0x102ff920`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102ff920(void)
{
}
```

## `sub_102ff932` `0x102ff932`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102ff932(void)
{
}
```

## `sub_102ff96d` `0x102ff96d`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102ff96d(void)
{
}
```

## `sub_102ff9a0` `0x102ff9a0`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102ff9a0(void)
{
}
```

## `sub_102ff9b0` `0x102ff9b0`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102ff9b0(void)
{
}
```

## `sub_102ff9c7` `0x102ff9c7`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102ff9c7(void)
{
}
```

## `sub_102ffa30` `0x102ffa30`

_266 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c818;
extern unsigned int g_1038c81c;

unsigned int sub_102ffa30(int a0)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // ecx
    unsigned int v10;  // ecx
    unsigned int v11;  // eax
    int v12;  // edx
    int v13;  // eax
    unsigned int v14;  // 4617
    unsigned int v15;  // 4150
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f0f30(a0);
    v2 = v6;
    v1 = v7;
    v0 = _INSERT(v4 & 0xffff, 1, 0);
    v10 = _INSERT(_INSERT(v7, 1, 0), 0, 125);
    v11 = _INSERT(v0, 0, (char)v0 & (char)~(~(v10)) + 3);
    v2 = -(0 < v11) + 1;
    v12 = -(0 < (v4 & 0xfc00)) + 1;
    v13 = -(0 < v11) + 1;
    v14 = _ccall(0, 6, v13, v12, 0);
    v15 = _ccall(5, 6, v13, v12, 0);
    v3 = _INSERT(v13, 0, v15);
    v5 = (g_1038c818 ^ g_1038c81c) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0e70(v5);
}
```

## `sub_102ffb40` `0x102ffb40`

_165 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c804;
extern unsigned int g_1038c808;

unsigned int sub_102ffb40(int a0)
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

    v5 = sub_102f0650(a0);
    v7 = v5;
    v3 = v8;
    v9 = v7;
    v2 = v10;
    v0 = 0x1f00;
    v11 = _ccall(0, 15, (unsigned int)v7, 0, 0);
    v1 = v7;
    v4 = -(-(0 < _INSERT(_INSERT(v1, 1, *((char *)((void*)&v1 + 1)) & (char)v0 - 31) & 0xff, 0, (char)_INSERT(v1, 1, *((char *)((void*)&v1 + 1)) & (char)v0 - 31) & 4)));
    v6 = (g_1038c804 ^ g_1038c808) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f0570(v6);
}
```

## `sub_102ffb6f` `0x102ffb6f`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102ffb6f(void)
{
}
```

## `sub_102ffbf0` `0x102ffbf0`

_178 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7fc;
extern unsigned int g_1038c800;

unsigned int sub_102ffbf0(int a0)
{
    unsigned int v6;  // edx
    unsigned int v7;  // ebx
    unsigned int v9;  // eax
    unsigned int v10;  // ebx
    unsigned int v11;  // eax
    unsigned int v12;  // eax
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f02b0(a0);
    v2 = v6;
    v1 = v7;
    v0 = v4 & 0xffff;
    v9 = _INSERT(v0, 1, 0);
    v10 = _INSERT(_INSERT(v7, 1, 0), 0, 117);
    v11 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v12 = _INSERT((char)v11 * 0 | (char)(v11 >> 24), 0, ((char)v11 * 0 | (char)(v11 >> 24)) & (char)~(~((unsigned short)_INSERT(v10, 0, 64))));
    v3 = -(-(0 < v12));
    v5 = (g_1038c7fc ^ g_1038c800) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0130(v5);
}
```

## `sub_102ffcb0` `0x102ffcb0`

_225 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c814;
extern unsigned int g_1038c818;

unsigned int sub_102ffcb0(unsigned int a0)
{
    unsigned int v7;  // ebx
    unsigned int v16;  // cc_dep1
    unsigned int v8;  // ecx
    unsigned int v10;  // ecx
    unsigned int v11;  // ecx
    unsigned int v12;  // eax
    unsigned int v14;  // eax
    char v15;  // cl
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v1 = a0;
    v4 = sub_102f0dc0(a0);
    v1 = v7;
    v0 = v8;
    v10 = _INSERT(_INSERT(v8, 1, 0), 0, 101);
    v11 = v10 * 0x1000000 | v10 * 0x100 & 0xff0000 | v10 >> 8 & 0xff00 | v10 >> 24 & 0xff;
    v12 = _INSERT(_INSERT(v4 & 0xffff, 1, 0) & 0xff, 0, ~(~((char)_INSERT(v4 & 0xffff, 1, 0))));
    v14 = v12 * 0x1000000 | v12 * 0x100 & 0xff0000 | v12 >> 8 & 0xff00 | v12 >> 24 & 0xff;
    v15 = ~(~(_INSERT((char)v11 * 0 | (char)(v11 >> 24), 0, ((char)v11 * 0 | (char)(v11 >> 24)) - 40)));
    v16 = v15 + 1;
    v3 = -(-(0 < _INSERT((char)v14 * 0 | (char)(v14 >> 24), 0, ((char)v14 * 0 | (char)(v14 >> 24)) & v15 + 3)));
    v5 = (g_1038c814 ^ g_1038c818) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0d10(v5);
}
```

## `sub_102ffcd0` `0x102ffcd0`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102ffcd0(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102ffda0` `0x102ffda0`

_209 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c830;
extern unsigned int g_1038c834;

int sub_102ffda0(unsigned int a0)
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

    v4 = sub_102f1e90(a0);
    v2 = v6;
    v1 = v7;
    v0 = _INSERT(v4 & 0xffff, 1, 0);
    v9 = _ccall(0, 19, 90, 0, 0);
    v13 = _INSERT(v0, 0, (char)v0 & (char)~(~(_INSERT(90 CONCAT 0, 0, 64))));
    v3 = -(-(0 < v13));
    v5 = (g_1038c830 ^ g_1038c834) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f1d10(v5);
}
```

## `sub_102ffe03` `0x102ffe03`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102ffe03(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102ffe80` `0x102ffe80`

_132 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e0;
extern unsigned int g_1038c7e4;

int sub_102ffe80(unsigned int a0)
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
    v4 = sub_102ef270(a0);
    v1 = v6;
    v7 = v4 * 0x1000000 | v4 * 0x100 & 0xff0000 | v4 >> 8 & 0xff00 | v4 >> 24 & 0xff;
    v0 = v8;
    v3 = -(-(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & ~(~(48)) + 16)));
    v5 = (g_1038c7e0 ^ g_1038c7e4) * 2;
    if (v3)
        v5 |= 1;
    return sub_102ef140(v5);
}
```

## `sub_102ffea2` `0x102ffea2`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102ffea2(void)
{
}
```

## `sub_102fff10` `0x102fff10`

_150 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c80c;
extern unsigned int g_1038c810;

unsigned int sub_102fff10(int a0)
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

    v5 = sub_102f0940(a0);
    v7 = v5;
    v3 = v8;
    v9 = v7;
    v2 = v10;
    v0 = 13;
    v11 = _ccall(0, 15, (unsigned int)v7, 0, 0);
    v1 = v7;
    v4 = -(0 < _INSERT((char)v1 & (char)v0 - 13, 1, (char)v1 & (char)v0 - 13 & 227)) + 1;
    v6 = (g_1038c80c ^ g_1038c810) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f0850(v6);
}
```

## `sub_102fff3c` `0x102fff3c`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fff3c(void)
{
}
```

## `sub_102fffb0` `0x102fffb0`

_171 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c820;
extern unsigned int g_1038c824;

unsigned int sub_102fffb0(int a0)
{
    unsigned short v6;  // ax
    unsigned int v7;  // ebx
    unsigned int v16;  // 4120
    unsigned int v19;  // 4149
    unsigned int v22;  // eax
    unsigned int v23;  // 4108
    unsigned int v24;  // cc_dep1
    unsigned int v25;  // 4108
    unsigned int v26;  // 4158
    unsigned int v9;  // ecx
    unsigned int v10;  // 4127
    char v11;  // cl
    unsigned int v12;  // 4107
    unsigned int v13;  // 4113
    unsigned int v14;  // cc_ndep
    unsigned int v15;  // cc_dep1
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f1390(a0);
    v6 = v4;
    v2 = v7;
    v1 = v9;
    v0 = 2;
    v10 = _ccall(0, 15, (unsigned int)v6, 0, 0);
    v11 = v0;
    v12 = _ccall(15, (unsigned int)v6, 0, 0);
    v13 = _ccall(19, (unsigned int)(v11 - 1), 0, v12);
    v14 = v13;
    v15 = v11 - 2;
    v16 = _ccall(0, 19, (unsigned int)(v11 - 2), 0, v13);
    v19 = _ccall(0, 19, 8, 0, 0);
    v22 = _INSERT((char)v6 & v11 - 2, 1, (char)v6 & v11 - 2 & 8);
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
    v3 = -(v26 & 1) + 1;
    v5 = (g_1038c820 ^ g_1038c824) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f1250(v5);
}
```

## `sub_102fffdb` `0x102fffdb`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fffdb(void)
{
}
```

## `sub_102fffed` `0x102fffed`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102fffed(void)
{
}
```

## `sub_1030000d` `0x1030000d`

_3 bytes. (leaf/helper — see body)_

```c
void sub_1030000d(void)
{
}
```

## `sub_10300070` `0x10300070`

_191 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c844;
extern unsigned int g_1038c848;

unsigned int sub_10300070(unsigned int a0)
{
    unsigned int v8;  // edx
    unsigned int v9;  // ebx
    unsigned int v11;  // eax
    unsigned int v12;  // 4154
    unsigned short v13;  // bx
    unsigned int v14;  // eax
    unsigned int v15;  // 4245
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v2 = a0;
    v5 = sub_102f2b60(a0);
    v2 = v8;
    v1 = v9;
    v0 = v5 & 0xffff;
    v11 = _INSERT(v0, 1, 0);
    v12 = _ccall(0, 13, 0, 0, 0);
    v13 = _INSERT(_INSERT(*((unsigned short *)((void*)&v9 + 1)), 1, 0), 0, 128);
    v14 = v11 * 0x1000000 | v11 * 0x100 & 0xff0000 | v11 >> 8 & 0xff00 | v11 >> 24 & 0xff;
    v15 = _ccall(0, 4, 159, 31, 0);
    v16 = _INSERT((char)v14 * 0 | (char)(v14 >> 24), 0, ((char)v14 * 0 | (char)(v14 >> 24)) & (char)~(~(v13)));
    v4 = -(0 < v16) + 1;
    v6 = (g_1038c844 ^ g_1038c848) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f2ad0(v6);
}
```

## `sub_10300090` `0x10300090`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10300090(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103000b6` `0x103000b6`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103000b6(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103000ed` `0x103000ed`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103000ed(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10300140` `0x10300140`

_165 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7dc;
extern unsigned int g_1038c7e0;

unsigned int sub_10300140(int a0)
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

## `sub_103001f0` `0x103001f0`

_136 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c840;
extern unsigned int g_1038c844;

unsigned int sub_103001f0(char a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4)
{
    unsigned int v2;  // eax
    unsigned int v3;  // eax
    unsigned int v4;  // cc_dep1
    unsigned int v5;  // 4156
    unsigned int v6;  // eax
    unsigned int v7;  // 4103
    unsigned int v8;  // cc_ndep
    unsigned int v9;  // edi
    unsigned int v10;  // cc_dep1
    unsigned int v11;  // 4109
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v2 = a2 * 0x1000000 | a2 * 0x100 & 0xff0000 | a2 >> 8 & 0xff00 | a2 >> 24 & 0xff;
    v3 = v2 * 0x1000000 | v2 * 0x100 & 0xff0000 | v2 >> 8 & 0xff00 | v2 >> 24 & 0xff;
    v4 = v3 & 0x800;
    v5 = _ccall(0, 15, v3 & 0x800, 0, 0);
    if (a3)
    {
        v6 = 0;
    }
    else
    {
        v7 = _ccall(15, a3, 0, 0);
        v8 = v7;
        v10 = v9 - 1;
        v11 = _ccall(0, 21, v9 - 1, 0, v7);
        v6 = 1;
    }
    v0 = v6;
    v1 = (g_1038c840 ^ g_1038c844) * 2;
    if (v0)
        v1 |= 1;
    return sub_102f27b0(v1);
}
```

## `sub_1030020c` `0x1030020c`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1030020c(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10300236` `0x10300236`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10300236(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10300280` `0x10300280`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10300280(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 106;
    v7 = 181;
    v8 = 47;
    v9 = 124;
    v10 = 175;
    v11 = 123;
    v12 = 0xaa;
    v13 = 126;
    v0 = 11;
    v14 = 7;
    idx = (&v6)[a0 >> 11 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_10300390` `0x10300390`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10300390(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 233;
    v7 = 0xee;
    v8 = 75;
    v9 = 105;
    v10 = 84;
    v11 = 181;
    v12 = 200;
    v13 = 0x44;
    v0 = 7;
    v14 = 7;
    idx = (&v6)[a0 >> 7 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_103004a0` `0x103004a0`

_256 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_103004a0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 104;
    v7 = 123;
    v8 = 60;
    v9 = 54;
    v10 = 154;
    v11 = 236;
    v12 = 202;
    v13 = 24;
    v0 = 1;
    v14 = 7;
    idx = (&v6)[a0 >> 1 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_103005a0` `0x103005a0`

_256 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_103005a0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 53;
    v7 = 185;
    v8 = 250;
    v9 = 1;
    v10 = 145;
    v11 = 78;
    v12 = 184;
    v13 = 0x11;
    v0 = 1;
    v14 = 7;
    idx = (&v6)[a0 >> 1 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_103006a0` `0x103006a0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_103006a0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 11;
    v7 = 39;
    v8 = 93;
    v9 = 250;
    v10 = 197;
    v11 = 127;
    v12 = 15;
    v13 = 126;
    v0 = 3;
    v14 = 7;
    idx = (&v6)[a0 >> 3 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_103007b0` `0x103007b0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_103007b0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 205;
    v7 = 225;
    v8 = 84;
    v9 = 212;
    v10 = 24;
    v11 = 218;
    v12 = 27;
    v13 = 37;
    v0 = 6;
    v14 = 7;
    idx = (&v6)[a0 >> 6 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_103008c0` `0x103008c0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_103008c0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 0xdd;
    v7 = 128;
    v8 = 162;
    v9 = 15;
    v10 = 219;
    v11 = 25;
    v12 = 117;
    v13 = 178;
    v0 = 5;
    v14 = 7;
    idx = (&v6)[a0 >> 5 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_103009d0` `0x103009d0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_103009d0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 64;
    v7 = 0xaa;
    v8 = 0;
    v9 = 145;
    v10 = 86;
    v11 = 183;
    v12 = 178;
    v13 = 107;
    v0 = 19;
    v14 = 7;
    idx = (&v6)[a0 >> 19 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_10300ae0` `0x10300ae0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10300ae0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 88;
    v7 = 175;
    v8 = 30;
    v9 = 208;
    v10 = 86;
    v11 = 147;
    v12 = 144;
    v13 = 218;
    v0 = 6;
    v14 = 7;
    idx = (&v6)[a0 >> 6 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_10300bf0` `0x10300bf0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10300bf0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 26;
    v7 = 165;
    v8 = 154;
    v9 = 184;
    v10 = 186;
    v11 = 37;
    v12 = 7;
    v13 = 226;
    v0 = 12;
    v14 = 7;
    idx = (&v6)[a0 >> 12 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_10300d00` `0x10300d00`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10300d00(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 181;
    v7 = 250;
    v8 = 117;
    v9 = 0x44;
    v10 = 116;
    v11 = 26;
    v12 = 167;
    v13 = 207;
    v0 = 14;
    v14 = 7;
    idx = (&v6)[a0 >> 14 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_10300e10` `0x10300e10`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10300e10(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 215;
    v7 = 189;
    v8 = 0x33;
    v9 = 83;
    v10 = 0x66;
    v11 = 197;
    v12 = 227;
    v13 = 0;
    v0 = 9;
    v14 = 7;
    idx = (&v6)[a0 >> 9 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

