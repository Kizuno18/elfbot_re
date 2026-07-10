# elfbot.dll decompiled — jiru 0x102f7be4..0x102f91cc

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_102f7be4` `0x102f7be4`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f7be4(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f7bfd` `0x102f7bfd`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f7bfd(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f7c60` `0x102f7c60`

_211 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c820;
extern unsigned int g_1038c824;

unsigned int sub_102f7c60(int a0)
{
    unsigned short v7;  // ax
    unsigned int v8;  // edx
    unsigned int v17;  // 4247
    unsigned int v20;  // eax
    unsigned int v21;  // 4149
    unsigned int v22;  // eax
    unsigned int v25;  // 4150
    unsigned int v9;  // cc_dep1
    unsigned int v28;  // 4119
    unsigned int v29;  // eax
    unsigned int v32;  // 4120
    unsigned int v35;  // 4135
    unsigned int v36;  // eax
    unsigned int v10;  // ebx
    unsigned int v37;  // cc_ndep
    unsigned int v38;  // cc_dep1
    unsigned int v39;  // 4136
    unsigned int v11;  // 4130
    unsigned int v12;  // 4239
    unsigned int v13;  // 4241
    unsigned int v14;  // 4243
    unsigned int v15;  // 4245
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
    v0 = 0x1f00;
    v11 = _ccall(0, 15, (unsigned int)v7, 0, 0);
    v1 = v7;
    v12 = _ccall(19, 8, 0, 0);
    v13 = _ccall(19, 7, 0, v12);
    v14 = _ccall(19, 6, 0, v13);
    v15 = _ccall(19, 5, 0, v14);
    v16 = v15;
    v17 = _ccall(0, 19, 4, 0, v15);
    v20 = _INSERT(_INSERT(v1, 1, *((char *)((void*)&v1 + 1)) & (char)v0 - 31) & 0xff, 0, (char)_INSERT(v1, 1, *((char *)((void*)&v1 + 1)) & (char)v0 - 31) & 4);
    v21 = _ccall(12, 0, (unsigned int)(char)(0 < v20), (unsigned int)(char)(0 < v20));
    v22 = -(0 < v20) + 1;
    v25 = _ccall(0, 21, v22 - 1, 0, v21);
    v28 = _ccall(21, v22 - 1, 0, v21);
    v29 = v22;
    v32 = _ccall(0, 21, v29 - 1, 0, v28);
    v35 = _ccall(21, v29 - 1, 0, v28);
    v36 = v29;
    v37 = v35;
    v38 = v36 - 1;
    v39 = _ccall(0, 21, v36 - 1, 0, v35);
    v4 = v36;
    v6 = (g_1038c820 ^ g_1038c824) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f1250(v6);
}
```

## `sub_102f7c8f` `0x102f7c8f`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f7c8f(void)
{
}
```

## `sub_102f7cce` `0x102f7cce`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f7cce(void)
{
}
```

## `sub_102f7ce5` `0x102f7ce5`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f7ce5(void)
{
}
```

## `sub_102f7cf4` `0x102f7cf4`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f7cf4(void)
{
}
```

## `sub_102f7d40` `0x102f7d40`

_161 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7fc;
extern unsigned int g_1038c800;

unsigned int sub_102f7d40(int a0)
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

    v5 = sub_102f02b0(a0);
    v7 = v5;
    v3 = v8;
    v9 = v7;
    v2 = v10;
    v0 = 0xd00;
    v11 = _ccall(0, 15, (unsigned int)v7, 0, 0);
    v1 = v7;
    v4 = -(0 < _INSERT(_INSERT(v1, 1, *((char *)((void*)&v1 + 1)) & (char)v0 - 13) & 0xff, 0, (char)_INSERT(v1, 1, *((char *)((void*)&v1 + 1)) & (char)v0 - 13) & 4)) + 1;
    v6 = (g_1038c7fc ^ g_1038c800) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f0130(v6);
}
```

## `sub_102f7d6f` `0x102f7d6f`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f7d6f(void)
{
}
```

## `sub_102f7df0` `0x102f7df0`

_203 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7f4;
extern unsigned int g_1038c7f8;

unsigned int sub_102f7df0(int a0)
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

    v4 = sub_102efd90(a0);
    v2 = v6;
    v1 = v7;
    v0 = v4 & 0xffff;
    v9 = _INSERT(v0, 1, 0);
    v10 = _INSERT(_INSERT(*((unsigned short *)((void*)&v7 + 1)), 1, 0), 0, 128);
    v11 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v12 = _INSERT((char)v11 * 0 | (char)(v11 >> 24), 0, ((char)v11 * 0 | (char)(v11 >> 24)) & (char)~(~(v10)));
    v2 = -(0 < v12) + 1;
    v3 = _INSERT(-(0 < v12) + 1, 0, -(0 < v12) + 1 == -(0 < (v4 & 0xf900)) + 1);
    v5 = (g_1038c7f4 ^ g_1038c7f8) * 2;
    if (v3)
        v5 |= 1;
    return sub_102efcf0(v5);
}
```

## `sub_102f7ec0` `0x102f7ec0`

_220 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c824;
extern unsigned int g_1038c828;

int sub_102f7ec0(unsigned int a0)
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
    v3 = -(-(0 < v11));
    v5 = (g_1038c824 ^ g_1038c828) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f14d0(v5);
}
```

## `sub_102f7fa0` `0x102f7fa0`

_188 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c838;
extern unsigned int g_1038c83c;

int sub_102f7fa0(unsigned int a0)
{
    unsigned short v6;  // ax
    unsigned int v7;  // edx
    unsigned int v17;  // 4179
    unsigned int v18;  // 4181
    unsigned int v19;  // 4183
    unsigned int v20;  // 4185
    unsigned int v21;  // cc_ndep
    unsigned int v22;  // 4187
    unsigned int v8;  // cc_dep1
    unsigned int v9;  // ebx
    char v10;  // bl
    unsigned int v11;  // 4130
    unsigned int v12;  // cc_ndep
    unsigned int v13;  // cc_dep1
    unsigned int v14;  // 4171
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
    v0 = 0x1f00;
    v10 = v0;
    v11 = _ccall(0, 15, (unsigned int)v6, 0, 0);
    v0 = v6;
    v12 = v10 - 25 < 5;
    v13 = v10 - 31;
    v14 = _ccall(0, 19, (unsigned int)(v10 - 31), 0, (unsigned int)(char)(v10 - 25 < 5));
    v17 = _ccall(19, 8, 0, 0);
    v18 = _ccall(19, 7, 0, v17);
    v19 = _ccall(19, 6, 0, v18);
    v20 = _ccall(19, 5, 0, v19);
    v21 = v20;
    v22 = _ccall(0, 19, 4, 0, v20);
    v3 = -(-(0 < _INSERT(_INSERT(v0, 1, *((char *)((void*)&v0 + 1)) & v10 - 31) & 0xff, 0, (char)_INSERT(v0, 1, *((char *)((void*)&v0 + 1)) & v10 - 31) & 4)));
    v5 = (g_1038c838 ^ g_1038c83c) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f22d0(v5);
}
```

## `sub_102f7fcf` `0x102f7fcf`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f7fcf(void)
{
}
```

## `sub_102f7ff7` `0x102f7ff7`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f7ff7(void)
{
}
```

## `sub_102f801f` `0x102f801f`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f801f(void)
{
}
```

## `sub_102f8070` `0x102f8070`

_390 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7f0;
extern unsigned int g_1038c7f4;

unsigned int sub_102f8070(int a0)
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

    v5 = sub_102efba0(a0);
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
            goto LABEL_102f81c9;
        v52 = 1;
    }
    else
    {
LABEL_102f81c9:
        v52 = 0;
    }
    v4 = v52;
    v6 = (g_1038c7f0 ^ g_1038c7f4) * 2;
    if (v4)
        v6 |= 1;
    return sub_102efa50(v6);
}
```

## `sub_102f814d` `0x102f814d`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f814d(void)
{
}
```

## `sub_102f8164` `0x102f8164`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f8164(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f8198` `0x102f8198`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f8198(void)
{
}
```

## `sub_102f81a7` `0x102f81a7`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f81a7(void)
{
}
```

## `sub_102f8210` `0x102f8210`

_391 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c82c;
extern unsigned int g_1038c830;

unsigned int sub_102f8210(int a0)
{
    unsigned int v7;  // ebx
    unsigned int v8;  // ecx
    unsigned int v17;  // eax
    unsigned int v19;  // eax
    unsigned short v20;  // bx
    unsigned int v21;  // eax
    unsigned int v22;  // eax
    unsigned int v23;  // eax
    unsigned int v24;  // 4108
    unsigned int v25;  // cc_dep1
    unsigned int v26;  // 4108
    unsigned int v9;  // 4136
    unsigned int v27;  // 4126
    unsigned int v28;  // eax
    unsigned int v11;  // edx
    unsigned int v12;  // edx
    unsigned int v13;  // 4269
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v5 = sub_102f1b90(a0);
    v3 = v7;
    v2 = v8;
    v9 = _ccall(0, 4, 44, 1, 0);
    v12 = v11 * 0x1000000 | v11 * 0x100 & 0xff0000 | v11 >> 8 & 0xff00 | v11 >> 24 & 0xff;
    v1 = _INSERT(v5 & 0xffff, 1, 0);
    v13 = _ccall(0, 19, 90, 0, 0);
    v17 = _INSERT(v1, 0, (char)v1 & (char)~(~(_INSERT(90 CONCAT 0, 0, 64))));
    if (!v17)
    {
        v3 = v12 * 0x1000000 | v12 * 0x100 & 0xff0000 | v12 >> 8 & 0xff00 | v12 >> 24 & 0xff;
        v2 = v7;
        v1 = v5 & 0xffff;
        v19 = _INSERT(v1, 1, 0);
        v20 = _INSERT(_INSERT(*((unsigned short *)((void*)&v7 + 1)), 1, 0), 0, 128);
        v21 = v19 * 0x1000000 | v19 * 0x100 & 0xff0000 | v19 >> 8 & 0xff00 | v19 >> 24 & 0xff;
        v22 = _INSERT((char)v21 * 0 | (char)(v21 >> 24), 0, ((char)v21 * 0 | (char)(v21 >> 24)) & (char)~(~(v20)));
        v3 = -(0 < v22) + 1;
        v1 = -(0 < v22) + 1;
        v0 = 4;
        v23 = _INSERT((char)v5 & (char)v0 - 4, 1, (char)v5 & (char)v0 - 4 & 8);
        if (v23)
        {
            v24 = _ccall(3, ~(v23), 1, 0);
            v25 = v24 | 1;
        }
        else
        {
            v26 = _ccall(3, ~(0), 1, 0);
            v25 = v26 & 4294967294;
        }
        v27 = _ccall(0, v25, 0, 0);
        if (v1 != -(v27 & 1) + 1)
            goto LABEL_102f8360;
        v28 = 0;
    }
    else
    {
LABEL_102f8360:
        v28 = 1;
    }
    v4 = v28;
    v6 = (g_1038c82c ^ g_1038c830) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f1a10(v6);
}
```

## `sub_102f8240` `0x102f8240`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f8240(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f827e` `0x102f827e`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f827e(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f83a0` `0x102f83a0`

_183 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e8;
extern unsigned int g_1038c7ec;

unsigned int sub_102f83a0(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
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
    v4 = (!a3 ? 1 : 0);
    v5 = (g_1038c7e8 ^ g_1038c7ec) * 2;
    if (v4)
        v5 |= 1;
    return sub_102ef530(v5);
}
```

## `sub_102f8460` `0x102f8460`

_250 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e0;
extern unsigned int g_1038c7e4;

int sub_102f8460(unsigned int a0)
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

    v4 = sub_102ef270(a0);
    v2 = v6;
    v1 = v7;
    v0 = _INSERT(v4 & 0xffff, 1, 0);
    v10 = _INSERT(_INSERT(v7, 1, 0), 0, 125);
    v11 = _INSERT(v0, 0, (char)v0 & (char)~(~(v10)) + 3);
    v3 = -(0 < v11) + 1;
    v5 = (g_1038c7e0 ^ g_1038c7e4) * 2;
    if (v3)
        v5 |= 1;
    return sub_102ef140(v5);
}
```

## `sub_102f8560` `0x102f8560`

_153 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7fc;
extern unsigned int g_1038c800;

unsigned int sub_102f8560(int a0)
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

    v5 = sub_102f02b0(a0);
    v7 = v5;
    v3 = v8;
    v9 = v7;
    v2 = v10;
    v0 = 31;
    v11 = _ccall(0, 15, (unsigned int)v7, 0, 0);
    v1 = v7;
    v4 = -(0 < _INSERT((char)v1 & (char)v0 - 31, 1, (char)v1 & (char)v0 - 31 & 243)) + 1;
    v6 = (g_1038c7fc ^ g_1038c800) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f0130(v6);
}
```

## `sub_102f858c` `0x102f858c`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f858c(void)
{
}
```

## `sub_102f8600` `0x102f8600`

_248 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c828;
extern unsigned int g_1038c82c;

unsigned int sub_102f8600(int a0)
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
    v2 = _INSERT(-(0 < v13) + 1, 0, -(0 < v13) + 1 == -(0 < (v3 & 0x500)) + 1);
    v4 = (g_1038c828 ^ g_1038c82c) * 2;
    if (v2)
        v4 |= 1;
    return sub_102f1810(v4);
}
```

## `sub_102f8700` `0x102f8700`

_125 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e8;
extern unsigned int g_1038c7ec;

unsigned int sub_102f8700(int a0)
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
    v3 = -(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & ~(~(114)) + 14)) + 1;
    v5 = (g_1038c7e8 ^ g_1038c7ec) * 2;
    if (v3)
        v5 |= 1;
    return sub_102ef530(v5);
}
```

## `sub_102f8722` `0x102f8722`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102f8722(void)
{
}
```

## `sub_102f8790` `0x102f8790`

_142 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c834;
extern unsigned int g_1038c838;

int sub_102f8790(unsigned int a0)
{
    unsigned int v4;  // edx
    unsigned int v5;  // 4141
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v2 = sub_102f2170(a0);
    v0 = v4;
    v5 = _ccall(0, 4, 14, 0xff, 0);
    v1 = _INSERT(_INSERT(v2, 1, 0) & 0xff, 0, (char)_INSERT(v2, 1, 0) & 1);
    v3 = (g_1038c834 ^ g_1038c838) * 2;
    if (v1)
        v3 |= 1;
    return sub_102f2010(v3);
}
```

## `sub_102f87bd` `0x102f87bd`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f87bd(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f8820` `0x102f8820`

_165 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c81c;
extern unsigned int g_1038c820;

int sub_102f8820(unsigned int a0)
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
    v10 = _INSERT(_INSERT(*((unsigned short *)((void*)&v7 + 1)), 1, 0), 0, 128);
    v11 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v12 = _INSERT((char)v11 * 0 | (char)(v11 >> 24), 0, ((char)v11 * 0 | (char)(v11 >> 24)) & (char)~(~(v10)));
    v3 = -(-(0 < v12));
    v5 = (g_1038c81c ^ g_1038c820) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0ff0(v5);
}
```

## `sub_102f88d0` `0x102f88d0`

_209 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c830;
extern unsigned int g_1038c834;

int sub_102f88d0(unsigned int a0)
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

## `sub_102f89b0` `0x102f89b0`

_167 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c818;
extern unsigned int g_1038c81c;

unsigned int sub_102f89b0(int a0)
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

    v4 = sub_102f0f30(a0);
    v2 = v6;
    v1 = v7;
    v0 = v4 & 0xffff;
    v9 = _INSERT(v0, 1, 0);
    v10 = _INSERT(_INSERT(*((unsigned short *)((void*)&v7 + 1)), 1, 0), 0, 65);
    v11 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v12 = _INSERT((char)v11 * 0 | (char)(v11 >> 24), 0, ((char)v11 * 0 | (char)(v11 >> 24)) & (char)~(~(v10)));
    v3 = -(0 < v12) + 1;
    v5 = (g_1038c818 ^ g_1038c81c) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0e70(v5);
}
```

## `sub_102f8a60` `0x102f8a60`

_171 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c838;
extern unsigned int g_1038c83c;

int sub_102f8a60(unsigned int a0)
{
    unsigned int v4;  // edx
    unsigned int v5;  // 4141
    unsigned int v6;  // 4134
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v2 = sub_102f2420(a0);
    v0 = v4;
    v5 = _ccall(0, 4, 14, 0xff, 0);
    v6 = _ccall(0, 4, 8, 0xff, 0);
    v1 = -(0 < _INSERT(_INSERT(v2, 1, 0) & 0xff, 0, (char)_INSERT(v2, 1, 0) & 1)) + 1;
    v3 = (g_1038c838 ^ g_1038c83c) * 2;
    if (v1)
        v3 |= 1;
    return sub_102f22d0(v3);
}
```

## `sub_102f8a8d` `0x102f8a8d`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f8a8d(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f8aa9` `0x102f8aa9`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f8aa9(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f8b10` `0x102f8b10`

_172 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c830;
extern unsigned int g_1038c834;

int sub_102f8b10(unsigned int a0)
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

    v4 = sub_102f1e90(a0);
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
    v3 = -(0 < _INSERT(_INSERT(v0, 1, *((char *)((void*)&v0 + 1)) & v10 - 30) & 0xff, 0, (char)_INSERT(v0, 1, *((char *)((void*)&v0 + 1)) & v10 - 30) & 4)) + 1;
    v5 = (g_1038c830 ^ g_1038c834) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f1d10(v5);
}
```

## `sub_102f8b3f` `0x102f8b3f`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f8b3f(void)
{
}
```

## `sub_102f8b56` `0x102f8b56`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f8b56(void)
{
}
```

## `sub_102f8bd0` `0x102f8bd0`

_145 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c820;
extern unsigned int g_1038c824;

unsigned int sub_102f8bd0(int a0)
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

    v5 = sub_102f1390(a0);
    v3 = v7;
    v2 = v8;
    v0 = 14;
    v1 = v5 & 0xffff;
    v4 = -(-(0 < _INSERT((char)v1 & (char)v0 - 14, 1, (char)v1 & (char)v0 - 14 & 228)));
    v6 = (g_1038c820 ^ g_1038c824) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f1250(v6);
}
```

## `sub_102f8c70` `0x102f8c70`

_337 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c814;
extern unsigned int g_1038c818;

unsigned int sub_102f8c70(int a0)
{
    unsigned int v8;  // edx
    unsigned int v9;  // ebx
    unsigned int v18;  // eax
    unsigned int v19;  // eax
    unsigned int v21;  // eax
    unsigned short v22;  // bx
    unsigned int v23;  // eax
    unsigned int v24;  // eax
    unsigned short v25;  // ax
    unsigned int v26;  // cc_dep1
    unsigned int v27;  // 4267
    unsigned int v10;  // eax
    unsigned int v28;  // eax
    unsigned int v29;  // 4220
    unsigned int v30;  // eax
    unsigned int v33;  // 4221
    unsigned int v36;  // 4151
    unsigned int v37;  // eax
    unsigned int v11;  // 4228
    unsigned int v38;  // cc_ndep
    unsigned int v39;  // cc_dep1
    unsigned int v40;  // 4152
    unsigned int v43;  // eax
    unsigned int v12;  // 4229
    unsigned int v13;  // cc_ndep
    unsigned int v14;  // 4230
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x1c]
    unsigned int v4;  // [bp-0x18]
    unsigned int v5;  // [bp-0x10]
    int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]

    v6 = sub_102f0dc0(a0);
    v4 = v8;
    v3 = v9;
    v2 = v6 & 0xffff;
    v10 = _INSERT(v2, 1, 0);
    v11 = _ccall(19, 128, 0, 0);
    v12 = _ccall(19, 127, 0, v11);
    v13 = v12;
    v14 = _ccall(0, 19, 126, 0, v12);
    v18 = v10 * 0x1000000 | v10 * 0x100 & 0xff0000 | v10 >> 8 & 0xff00 | v10 >> 24 & 0xff;
    v19 = _INSERT((char)v18 * 0 | (char)(v18 >> 24), 0, ((char)v18 * 0 | (char)(v18 >> 24)) & (char)~(~(_INSERT(126 CONCAT 0, 0, 64))));
    if (!v19)
    {
        v4 = v8;
        v2 = v6 & 0xffff;
        v21 = _INSERT(v2, 1, 0);
        v22 = _INSERT(_INSERT(*((unsigned short *)((void*)&v3 + 1)), 1, 0), 0, 0x88);
        v23 = v21 * 0x1000000 | v21 * 0x100 & 0xff0000 | v21 >> 8 & 0xff00 | v21 >> 24 & 0xff;
        v24 = _INSERT((char)v23 * 0 | (char)(v23 >> 24), 0, ((char)v23 * 0 | (char)(v23 >> 24)) & (char)~(~(v22)));
        v4 = -(0 < v24) + 1;
        v25 = v6;
        v3 = v8;
        v26 = v25;
        v2 = v3;
        v0 = 31;
        v27 = _ccall(0, 15, (unsigned int)v25, 0, 0);
        v1 = v25;
        v28 = _INSERT((char)v1 & (char)v0 - 31, 1, (char)v1 & (char)v0 - 31 & 246);
        v29 = _ccall(12, 0, (unsigned int)(char)(0 < v28), (unsigned int)(char)(0 < v28));
        v30 = -(0 < v28) + 1;
        v33 = _ccall(0, 21, v30 - 1, 0, v29);
        v36 = _ccall(21, v30 - 1, 0, v29);
        v37 = v30;
        v38 = v36;
        v39 = v37 - 1;
        v40 = _ccall(0, 21, v37 - 1, 0, v36);
        if (-(0 < v24) + 1 != v37)
            goto LABEL_102f8d93;
        v43 = 1;
    }
    else
    {
LABEL_102f8d93:
        v43 = 0;
    }
    v5 = v43;
    v7 = (g_1038c814 ^ g_1038c818) * 2;
    if (v5)
        v7 |= 1;
    return sub_102f0d10(v7);
}
```

## `sub_102f8cbc` `0x102f8cbc`

_2 bytes. (leaf/helper — see body)_

```c
int sub_102f8cbc(void)
{
}
```

## `sub_102f8d36` `0x102f8d36`

_2 bytes. (leaf/helper — see body)_

```c
int sub_102f8d36(void)
{
}
```

## `sub_102f8d6f` `0x102f8d6f`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f8d6f(void)
{
}
```

## `sub_102f8dd0` `0x102f8dd0`

_420 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c810;
extern unsigned int g_1038c814;

unsigned int sub_102f8dd0(int a0)
{
    unsigned int v8;  // ebx
    unsigned int v9;  // ecx
    unsigned int v19;  // eax
    char v20;  // cl
    unsigned int v21;  // cc_dep1
    unsigned int v23;  // eax
    unsigned short v24;  // ax
    unsigned int v25;  // cc_dep1
    unsigned int v26;  // 4168
    unsigned int v27;  // 4212
    unsigned int v31;  // eax
    char v11;  // cl
    unsigned int v13;  // edx
    unsigned int v15;  // ecx
    unsigned int v16;  // ecx
    unsigned int v17;  // eax
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]

    v4 = v8;
    v6 = sub_102f0ba0(a0);
    v3 = v9;
    v11 = (char)(~(~(12)) + 0x11) + 3;
    v2 = v13;
    if (!(__buildin_bswap32(v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & _INSERT(v11 + 13, 0, v11 + 18) + 14))
    {
        v4 = v8;
        v3 = v9;
        v15 = _INSERT(_INSERT(v9, 1, 0), 0, 164);
        v16 = v15 * 0x1000000 | v15 * 0x100 & 0xff0000 | v15 >> 8 & 0xff00 | v15 >> 24 & 0xff;
        v17 = _INSERT(_INSERT(v6 & 0xffff, 1, 0) & 0xff, 0, ~(~((char)_INSERT(v6 & 0xffff, 1, 0))));
        v19 = v17 * 0x1000000 | v17 * 0x100 & 0xff0000 | v17 >> 8 & 0xff00 | v17 >> 24 & 0xff;
        v20 = ~(~(_INSERT((char)v16 * 0 | (char)(v16 >> 24), 0, ((char)v16 * 0 | (char)(v16 >> 24)) - 39)));
        v21 = v20 + 1;
        v23 = _INSERT((char)v19 * 0 | (char)(v19 >> 24), 0, ((char)v19 * 0 | (char)(v19 >> 24)) & v20 + 3);
        v4 = -(0 < v23) + 1;
        v24 = v6;
        v3 = v8;
        v25 = v24;
        v2 = v8;
        v0 = 31;
        v26 = _ccall(0, 15, (unsigned int)v24, 0, 0);
        v1 = v24;
        v27 = _ccall(0, 19, 243, 0, 0);
        if (-(0 < v23) + 1 != -(0 < _INSERT((char)v1 & (char)v0 - 31, 1, (char)v1 & (char)v0 - 31 & 243)) + 1)
            goto LABEL_102f8f45;
        v31 = 1;
    }
    else
    {
LABEL_102f8f45:
        v31 = 0;
    }
    v5 = v31;
    v7 = (g_1038c810 ^ g_1038c814) * 2;
    if (v5)
        v7 |= 1;
    return sub_102f0a30(v7);
}
```

## `sub_102f8eca` `0x102f8eca`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f8eca(void)
{
}
```

## `sub_102f8ef2` `0x102f8ef2`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f8ef2(void)
{
}
```

## `sub_102f8f2a` `0x102f8f2a`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f8f2a(void)
{
}
```

## `sub_102f8f80` `0x102f8f80`

_134 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c818;
extern unsigned int g_1038c81c;

unsigned int sub_102f8f80(int a0)
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
    v4 = sub_102f0f30(a0);
    v1 = v6;
    v7 = v4 * 0x1000000 | v4 * 0x100 & 0xff0000 | v4 >> 8 & 0xff00 | v4 >> 24 & 0xff;
    v0 = v8;
    v3 = -(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & ~(~(112)) + 16)) + 1;
    v5 = (g_1038c818 ^ g_1038c81c) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0e70(v5);
}
```

## `sub_102f8fa5` `0x102f8fa5`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102f8fa5(void)
{
}
```

## `sub_102f9010` `0x102f9010`

_199 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c80c;
extern unsigned int g_1038c810;

unsigned int sub_102f9010(int a0)
{
    unsigned short v6;  // ax
    unsigned int v7;  // edx
    unsigned int v16;  // 4146
    unsigned int v19;  // eax
    unsigned int v20;  // 4211
    unsigned int v21;  // eax
    unsigned int v24;  // 4212
    unsigned int v8;  // cc_dep1
    unsigned int v27;  // 4119
    unsigned int v28;  // eax
    unsigned int v31;  // 4120
    unsigned int v34;  // 4135
    unsigned int v35;  // eax
    unsigned int v9;  // ebx
    unsigned int v36;  // cc_ndep
    unsigned int v37;  // cc_dep1
    unsigned int v38;  // 4136
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

    v4 = sub_102f0940(a0);
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
    v19 = _INSERT((char)v0 & v10 - 31, 1, (char)v0 & v10 - 31 & 246);
    v20 = _ccall(12, 0, (unsigned int)(char)(0 < v19), (unsigned int)(char)(0 < v19));
    v21 = -(0 < v19) + 1;
    v24 = _ccall(0, 21, v21 - 1, 0, v20);
    v27 = _ccall(21, v21 - 1, 0, v20);
    v28 = v21;
    v31 = _ccall(0, 21, v28 - 1, 0, v27);
    v34 = _ccall(21, v28 - 1, 0, v27);
    v35 = v28;
    v36 = v34;
    v37 = v35 - 1;
    v38 = _ccall(0, 21, v35 - 1, 0, v34);
    v3 = v35;
    v5 = (g_1038c80c ^ g_1038c810) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0850(v5);
}
```

## `sub_102f903c` `0x102f903c`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f903c(void)
{
}
```

## `sub_102f9053` `0x102f9053`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f9053(void)
{
}
```

## `sub_102f9089` `0x102f9089`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f9089(void)
{
}
```

## `sub_102f9098` `0x102f9098`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f9098(void)
{
}
```

## `sub_102f90f0` `0x102f90f0`

_171 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c844;
extern unsigned int g_1038c848;

unsigned int sub_102f90f0(int a0)
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

    v4 = sub_102f2b60(a0);
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
    v5 = (g_1038c844 ^ g_1038c848) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f2ad0(v5);
}
```

## `sub_102f91a0` `0x102f91a0`

_151 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c840;
extern unsigned int g_1038c844;

unsigned int sub_102f91a0(int a0)
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

    v5 = sub_102f2940(a0);
    v7 = v5;
    v3 = v8;
    v9 = v7;
    v2 = v10;
    v0 = 13;
    v11 = _ccall(0, 15, (unsigned int)v7, 0, 0);
    v1 = v7;
    v4 = -(-(0 < _INSERT((char)v1 & (char)v0 - 13, 1, (char)v1 & (char)v0 - 13 & 227)));
    v6 = (g_1038c840 ^ g_1038c844) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f27b0(v6);
}
```

## `sub_102f91cc` `0x102f91cc`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f91cc(void)
{
}
```

