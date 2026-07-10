# elfbot.dll decompiled — jiru 0x10337030..0x103384d0

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10337030` `0x10337030`

_246 bytes. (leaf/helper — see body)_

```c
int sub_10337030(unsigned int a0, int a1)
{
    int v0;  // [bp-0xc]
    int v1;  // [bp-0x8]

    if (a1 > 2 && *((short *)sub_10325ed0(a0, 1)) == 58 && *((short *)sub_10325ed0(a0, 2)) == 47)
        return 2;
    if (a1 == 2 && *((short *)sub_10325ed0(a0, 0)) == 47 && *((short *)sub_10325ed0(a0, 1)) == 47)
        return -1;
    if (a1 > 3 && *((short *)sub_10325ed0(a0, 0)) == 47 && *((short *)sub_10325ed0(a0, 1)) == 47 && *((short *)sub_10325ed0(a0, 2)) != 47)
    {
        v1 = sub_10326540(a0, 47, 2);
        v0 = (v1 < a1 ? v1 : -1);
        return v0;
    }
    if (a1 > 0 && *((short *)sub_10325ed0(a0, 0)) == 47)
        return 0;
    return -1;
}
```

## `sub_10337130` `0x10337130`

_231 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103908cc;

int sub_10337130(unsigned int a0, int a1, int a2, unsigned int a3, unsigned int a4)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned long v17;  // 4129
    unsigned short v10;  // fs
    unsigned long v11;  // 4154
    unsigned long v12;  // 4176
    int v13;  // edi
    int v14;  // esi
    int v15;  // ebx
    int v16;  // eax
    unsigned int v0;  // [bp-0x34]
    int v1;  // [bp-0x1c], Other Possible Types: unsigned int
    int v2;  // [bp-0x18]
    char *v3;  // [bp-0x14], Other Possible Types: unsigned int
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8], Other Possible Types: char
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036eb2e;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v3 = a0;
    v0 = g_1038e180 ^ &v7;
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    v3 = &v0;
    sub_10336ee0(a0, a3, a4, a1);
    v6 = 0;
    *((char **)a0) = &g_103908cc;
    sub_10338b80(g_1038e180 ^ &v7, v13, v14, v15, v16, a0, v1);
    v6 = 1;
    v6 = 2;
    v1 = sub_10350a53(84);
    v6 = 3;
    if (sub_10350a53(84))
    {
        v16 = sub_103381b0();
        v16 = v16;
    }
    else
    {
        v16 = 0;
    }
    v2 = v16;
    v6 = 2;
    sub_10339a50(v2);
    sub_10336b20(a0 + 76);
    sub_10337230(a2);
    v17 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v17) = v4;
    return a0;
}
```

## `sub_103371f2` `0x103371f2`

_24 bytes. (leaf/helper — see body)_

```c
extern char g_10337211;

int sub_103371f2(void)
{
    unsigned int v1;  // [bp+0x100000]

    sub_10338be0();
    v1 = 1;
    return &g_10337211;
}
```

## `sub_10337230` `0x10337230`

_28 bytes. (leaf/helper — see body)_

```c
int sub_10337230(int a0, int a1)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_103325a0(v0, a1);
    return v0;
}
```

## `sub_10337250` `0x10337250`

_162 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern int g_1039e128;

unsigned int sub_10337250(int a0)
{
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // fs
    unsigned long v13;  // 4137
    unsigned long v14;  // 4151
    unsigned int v15;  // eax
    unsigned long v16;  // 4113
    int v0;  // [bp-0xf4]
    unsigned int v1;  // [bp-0xf0]
    int v2;  // [bp-0xec]
    int v3;  // [bp-0xe8]
    char v4;  // [bp-0xe4]
    char v5;  // [bp-0x78]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]
    char v9;  // [bp-0x4]

    v8 = 4294967295;
    v7 = sub_1036eb58;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v6 = *((int *)v13);
    v1 = g_1038e180 ^ &v9;
    v14 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v14) = &v6;
    v0 = a0;
    sub_10334530();
    v3 = sub_10339ac0(&v5, a0);
    v2 = v3;
    v8 = 0;
    sub_10339b20(&v4, v2);
    sub_103533ea(&v4, &g_1039e128);
    v8 = 4294967295;
    v15 = sub_10339380(&v4, &g_1039e128);
    v16 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v16) = v6;
    return v15;
}
```

## `sub_10337300` `0x10337300`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10337300(unsigned int a0, int a1)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4138
    unsigned int v8;  // eax
    unsigned int v9;  // ecx
    unsigned long v10;  // 4154
    unsigned long v11;  // 4131
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v8 = *((int *)v7);
    v1 = *((int *)v7);
    v0 = v9;
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v10) = &v1;
    sub_10338c50(a1, g_1038e180 ^ &v2, 0, v8, sub_1036eb99, -1, &v3);
    v11 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v11) = v8;
    return a0;
}
```

## `sub_10337360` `0x10337360`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10337360(unsigned int a0, int a1)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4138
    unsigned int v8;  // eax
    unsigned int v9;  // ecx
    unsigned long v10;  // 4154
    unsigned long v11;  // 4131
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v8 = *((int *)v7);
    v1 = *((int *)v7);
    v0 = v9;
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v10) = &v1;
    sub_10338cd0(a1, g_1038e180 ^ &v2, 0, v8, sub_1036ebd9, -1, &v3);
    v11 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v11) = v8;
    return a0;
}
```

## `sub_103373c0` `0x103373c0`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_103373c0(unsigned int a0, int a1)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4138
    unsigned int v8;  // eax
    unsigned int v9;  // ecx
    unsigned long v10;  // 4154
    unsigned long v11;  // 4131
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v8 = *((int *)v7);
    v1 = *((int *)v7);
    v0 = v9;
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v10) = &v1;
    sub_10338da0(a1, g_1038e180 ^ &v2, 0, v8, sub_1036ec19, -1, &v3);
    v11 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v11) = v8;
    return a0;
}
```

## `sub_10337420` `0x10337420`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10337420(unsigned int a0, int a1)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4138
    unsigned int v8;  // eax
    unsigned int v9;  // ecx
    unsigned long v10;  // 4154
    unsigned long v11;  // 4131
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v8 = *((int *)v7);
    v1 = *((int *)v7);
    v0 = v9;
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v10) = &v1;
    sub_10338e20(a1, g_1038e180 ^ &v2, 0, v8, sub_1036ec59, -1, &v3);
    v11 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v11) = v8;
    return a0;
}
```

## `sub_10337480` `0x10337480`

_172 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10337480(int a0, int a1)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4140
    unsigned long v11;  // 4157
    unsigned long v13;  // 4114
    char v0;  // [bp-0x38]
    int v1;  // [bp-0x18]
    char v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char v5;  // [bp-0x8], Other Possible Types: unsigned int
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036ec90;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v1 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    sub_10339570(a1, v1, a0);
    v5 = 0;
    if (!(char)sub_10339b80(&v2))
    {
        sub_10339bb0(a1);
        v5 = 1;
        sub_103388b0(sub_10337e90(&v0));
        v5 = 0;
        sub_10319f90(&v0);
    }
    v5 = 4294967295;
    sub_10338430();
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v3;
    return sub_10351225();
}
```

## `sub_10337530` `0x10337530`

_172 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10337530(int a0, int a1)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4140
    unsigned long v11;  // 4157
    unsigned long v13;  // 4114
    char v0;  // [bp-0x38]
    int v1;  // [bp-0x18]
    char v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char v5;  // [bp-0x8], Other Possible Types: unsigned int
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036ecd0;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v1 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    sub_103395d0(a1, v1, a0);
    v5 = 0;
    if (!(char)sub_10339c20(&v2))
    {
        sub_1031a4d0(&v0, a1);
        v5 = 1;
        sub_103388b0(sub_10337e90(&v0));
        v5 = 0;
        sub_10319f90(&v0);
    }
    v5 = 4294967295;
    sub_10338480();
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v3;
    return sub_10351225();
}
```

## `sub_103375e0` `0x103375e0`

_172 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_103375e0(int a0, int a1)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4140
    unsigned long v11;  // 4157
    unsigned long v13;  // 4114
    char v0;  // [bp-0x38]
    int v1;  // [bp-0x18]
    char v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char v5;  // [bp-0x8], Other Possible Types: unsigned int
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036ed10;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v1 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    sub_10339630(a1, v1, a0);
    v5 = 0;
    if (!(char)sub_10339c50(&v2))
    {
        sub_1031e640(&v0, a1);
        v5 = 1;
        sub_103388b0(sub_10337e90(&v0));
        v5 = 0;
        sub_10319f90(&v0);
    }
    v5 = 4294967295;
    sub_103384d0();
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v3;
    return sub_10351225();
}
```

## `sub_10337690` `0x10337690`

_39 bytes. (leaf/helper — see body)_

```c
int sub_10337690(int a0, int a1)
{
    char v0;  // [bp-0x8]

    sub_1033a4c0(a1, a0);
    return sub_10339c80(&v0);
}
```

## `sub_103376c0` `0x103376c0`

_39 bytes. (leaf/helper — see body)_

```c
int sub_103376c0(int a0, int a1)
{
    char v0;  // [bp-0x8]

    sub_1033a4c0(a1, a0);
    return sub_10339cc0(&v0);
}
```

## `sub_103376f0` `0x103376f0`

_30 bytes. (leaf/helper — see body)_

```c
unsigned int sub_103376f0(unsigned int a0)
{
    return (!a0 ? 0 : sub_10339d00((char *)&/* unsupported instruction */ + 3));
}
```

## `sub_10337710` `0x10337710`

_43 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    unsigned int field_8;
} struct_0;

unsigned int sub_10337710(struct_0 *a0, int a1, char a2)
{
    char v0;  // [bp-0x9]

    v0 = a2;
    return sub_10330310(a0, a1, &v0);
}
```

## `sub_10337740` `0x10337740`

_45 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    unsigned int field_8;
} struct_0;

unsigned int sub_10337740(struct_0 *a0, int a1, unsigned short a2)
{
    unsigned short v0;  // [bp-0xa]

    v0 = a2;
    return sub_10330590(a0, a1, &v0);
}
```

## `sub_10337770` `0x10337770`

_160 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

void sub_10337770(unsigned int a0, unsigned short *i, unsigned short *a2)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4154
    unsigned int v11;  // eax
    unsigned long v12;  // 4176
    int v13;  // edi
    int v14;  // esi
    int v15;  // ebx
    unsigned long v16;  // 4122
    unsigned int v0;  // [bp-0x2c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]
    char v6;  // [bp+0x0]

    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v11 = *((int *)v10);
    v3 = *((int *)v10);
    v2 = a0;
    v0 = g_1038e180 ^ &v5;
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v12) = &v3;
    v1 = 0;
    sub_10339d30(i, a2, &v1, g_1038e180 ^ &v5, v13, v14, v15, a0, 0, &v0, v11, sub_1036ed40, -1, &v6);
    sub_10338850(0);
    for (v4 = 0; i != a2; i += 1)
    {
        sub_10325f90(a0, 1, *(i));
    }
    v16 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v16) = v11;
    return;
}
```

## `sub_103377f5` `0x103377f5`

_34 bytes. (leaf/helper — see body)_

```c
extern char g_1033781e;

int sub_103377f5(void)
{
    unsigned int *v1;  // [bp+0xfffec]
    unsigned int v2;  // [bp+0x100000]

    sub_1031a3c0(v1, 1, 0);
    sub_103533ea(0, 0);
    v2 = 4294967295;
    return &g_1033781e;
}
```

## `sub_10337840` `0x10337840`

_24 bytes. (leaf/helper — see body)_

```c
char sub_10337840(int a0)
{
    int v1;  // ecx
    int v2;  // eax
    char v0;  // [bp+0x0]

    v2 = _INSERT(0, 0, *((char *)((void*)&v1 + 3)));
    return sub_10339d60(a0, v2, v1, &v0);
}
```

## `sub_10337860` `0x10337860`

_70 bytes. (leaf/helper — see body)_

```c
unsigned int [2] sub_10337860(unsigned int *a0, int i, int a2, unsigned int a3, unsigned int a4)
{
    for (; i != a2; i += 2)
    {
        sub_1031a280(&a3);
        sub_10338a10(i);
        sub_1031a280(&a3);
    }
    *(a0) = a3;
    a0[1] = a4;
    return a0;
}
```

## `sub_103378b0` `0x103378b0`

_11 bytes. (leaf/helper — see body)_

```c
int sub_103378b0(unsigned int a0)
{
    return a0;
}
```

## `sub_103378c0` `0x103378c0`

_70 bytes. (leaf/helper — see body)_

```c
unsigned int [2] sub_103378c0(unsigned int *a0, int i, int a2, unsigned int a3, unsigned int a4)
{
    for (; i != a2; i += 1)
    {
        sub_1031a280(&a3);
        sub_10338a30(i);
        sub_1031a280(&a3);
    }
    *(a0) = a3;
    a0[1] = a4;
    return a0;
}
```

## `sub_10337910` `0x10337910`

_82 bytes. (leaf/helper — see body)_

```c
char sub_10337910(char a0, unsigned int a0, char a1, unsigned int a2, unsigned int a3, unsigned int a4)
{
    unsigned int v8;  // ecx
    char v9;  // al
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    int v5;  // [bp-0x8], Other Possible Types: unsigned int
    char v6;  // [bp+0x0]

    v5 = v8;
    v5 = _INSERT(v8, 3, 0);
    v9 = sub_10337970(&/* unsupported instruction */, &/* unsupported instruction */, v5, &v6);
    *((char *)&v5 + 2) = v9;
    v4 = _INSERT(v9, 0, *((char *)((void*)&v5 + 3)));
    *((char *)&v3) = *((char *)((void*)&v5 + 2));
    v2 = a4;
    v1 = a3;
    v0 = sub_10337840(&/* unsupported instruction */);
    return sub_10339d70(sub_10337840(&/* unsupported instruction */));
}
```

## `sub_10337970` `0x10337970`

_11 bytes. (leaf/helper — see body)_

```c
char sub_10337970(void)
{
    char v1;  // cl

    return v1;
}
```

## `sub_10337980` `0x10337980`

_25 bytes. (leaf/helper — see body)_

```c
int sub_10337980(int a0, int a1, int a2)
{
    char v0;  // [bp+0x0]

    return sub_10339e30(a0, a1, a2, &v0);
}
```

## `sub_103379a0` `0x103379a0`

_25 bytes. (leaf/helper — see body)_

```c
int sub_103379a0(int a0, int a1, int a2)
{
    char v0;  // [bp+0x0]

    return sub_10339e70(a0, a1, a2, &v0);
}
```

## `sub_103379c0` `0x103379c0`

_126 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_103379c0(unsigned int a0, unsigned int a1, int i, unsigned int a3, int a4, unsigned int a5)
{
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // fs
    unsigned long v13;  // 4144
    unsigned int v14;  // ebx
    unsigned int v15;  // esi
    unsigned int v16;  // edi
    unsigned long v17;  // 4168
    int v18;  // eax
    unsigned long v19;  // 4122
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x1c]
    int v4;  // [bp-0x18], Other Possible Types: unsigned int
    char *v5;  // [bp-0x14], Other Possible Types: unsigned int
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]
    char v9;  // [bp-0x4]

    v8 = 4294967295;
    v7 = sub_1036ed60;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v6 = *((int *)v13);
    v5 = a0;
    v4 = a0;
    v3 = v14;
    v2 = v15;
    v1 = v16;
    v0 = g_1038e180 ^ &v9;
    v17 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v17) = &v6;
    v5 = &v0;
    v4 = i;
    for (v8 = 0; a3 > 0; i += 28)
    {
        v18 = sub_10338a50(i, a4);
        a3 -= 1;
    }
    v19 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v19) = v6;
    return v18;
}
```

## `sub_10337a25` `0x10337a25`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10337a25(void)
{
    sub_10337a30();
    return;
}
```

## `sub_10337a30` `0x10337a30`

_33 bytes. (leaf/helper — see body)_

```c
extern char g_10337a63;

int sub_10337a30(void)
{
    unsigned int v1;  // [bp+0xffff0]
    unsigned int v2;  // [bp+0x100000]
    unsigned int v3;  // [bp+0x10000c]

    if (v1 == v3)
    {
        sub_103533ea(0, 0);
        v2 = 4294967295;
        return &g_10337a63;
    }
    return sub_10337a3b();
}
```

## `sub_10337a3b` `0x10337a3b`

_20 bytes. (leaf/helper — see body)_

```c
int sub_10337a3b(void)
{
    int v2;  // ecx
    unsigned int v1;  // [bp+0xffff0]

    sub_10338a70(v2);
    v1 += 28;
    return sub_10337a30();
}
```

## `sub_10337a80` `0x10337a80`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10337a80(unsigned int a0, int a1)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4138
    unsigned int v8;  // eax
    unsigned int v9;  // ecx
    unsigned long v10;  // 4154
    unsigned long v11;  // 4131
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v8 = *((int *)v7);
    v1 = *((int *)v7);
    v0 = v9;
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v10) = &v1;
    sub_10338ef0(a1, g_1038e180 ^ &v2, 0, v8, sub_1036ed99, -1, &v3);
    v11 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v11) = v8;
    return a0;
}
```

## `sub_10337ae0` `0x10337ae0`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10337ae0(unsigned int a0, int a1)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4138
    unsigned int v8;  // eax
    unsigned int v9;  // ecx
    unsigned long v10;  // 4154
    unsigned long v11;  // 4131
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v8 = *((int *)v7);
    v1 = *((int *)v7);
    v0 = v9;
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v10) = &v1;
    sub_10338f70(a1, g_1038e180 ^ &v2, 0, v8, sub_1036edd9, -1, &v3);
    v11 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v11) = v8;
    return a0;
}
```

## `sub_10337b40` `0x10337b40`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10337b40(unsigned int a0, int a1)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4138
    unsigned int v8;  // eax
    unsigned int v9;  // ecx
    unsigned long v10;  // 4154
    unsigned long v11;  // 4131
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v8 = *((int *)v7);
    v1 = *((int *)v7);
    v0 = v9;
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v10) = &v1;
    sub_10339040(a1, g_1038e180 ^ &v2, 0, v8, sub_1036ee19, -1, &v3);
    v11 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v11) = v8;
    return a0;
}
```

## `sub_10337ba0` `0x10337ba0`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10337ba0(unsigned int a0, int a1)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4138
    unsigned int v8;  // eax
    unsigned int v9;  // ecx
    unsigned long v10;  // 4154
    unsigned long v11;  // 4131
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v8 = *((int *)v7);
    v1 = *((int *)v7);
    v0 = v9;
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v10) = &v1;
    sub_103390c0(a1, g_1038e180 ^ &v2, 0, v8, sub_1036ee59, -1, &v3);
    v11 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v11) = v8;
    return a0;
}
```

## `sub_10337c00` `0x10337c00`

_78 bytes. (leaf/helper — see body)_

```c
char sub_10337c00(char a0, char a0, int a1, int a2)
{
    unsigned int v5;  // ecx
    int v6;  // edx
    int v7;  // eax
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]
    char v2;  // [bp-0x6]
    char v3;  // [bp-0x5]

    v1 = v5;
    v3 = 0;
    v0 = &/* unsupported instruction */;
    v2 = sub_10337970();
    v6 = _INSERT(0, 0, v3);
    v7 = _INSERT(v2 CONCAT 0, 0, v2);
    return sub_10339eb0(sub_10349d70(&/* unsupported instruction */, sub_10349d70(&/* unsupported instruction */, a1, a2, v7, v6)));
}
```

## `sub_10337c50` `0x10337c50`

_36 bytes. (leaf/helper — see body)_

```c
char * sub_10337c50(char *i, char *a1, char *a2)
{
    char *v0;  // eax

    for (; i != a1; i += 1)
    {
        *(i) = *(a2);
    }
    return v0;
}
```

## `sub_10337c80` `0x10337c80`

_64 bytes. (leaf/helper — see body)_

```c
char sub_10337c80(int a0, int a1, int a2, char a3)
{
    unsigned int v5;  // ecx
    int v6;  // eax
    int v7;  // ecx
    int v8;  // edx
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x6]
    char v4;  // [bp-0x5]

    v2 = v5;
    v4 = 0;
    v1 = &/* unsupported instruction */;
    v0 = &/* unsupported instruction */;
    v3 = sub_10337970();
    v6 = _INSERT(v3 CONCAT 0, 0, v4);
    v7 = _INSERT(0, 0, v3);
    v8 = _INSERT(0, 0, a3);
    return sub_10339ed0(a0, a1, a2, v8, v7, v6);
}
```

## `sub_10337cc0` `0x10337cc0`

_78 bytes. (leaf/helper — see body)_

```c
char sub_10337cc0(char a0, char a0, int a1, int a2)
{
    unsigned int v5;  // ecx
    int v6;  // edx
    int v7;  // eax
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]
    char v2;  // [bp-0x6]
    char v3;  // [bp-0x5]

    v1 = v5;
    v3 = 0;
    v0 = &/* unsupported instruction */;
    v2 = sub_10337970();
    v6 = _INSERT(0, 0, v3);
    v7 = _INSERT(v2 CONCAT 0, 0, v2);
    return sub_10339f10(sub_10349d70(&/* unsupported instruction */, sub_10349d70(&/* unsupported instruction */, a1, a2, v7, v6)));
}
```

## `sub_10337d10` `0x10337d10`

_38 bytes. (leaf/helper — see body)_

```c
unsigned short * sub_10337d10(unsigned short *i, unsigned short *a1, unsigned short *a2)
{
    unsigned short *v0;  // eax

    for (; i != a1; i += 1)
    {
        *(i) = *(a2);
    }
    return v0;
}
```

## `sub_10337d40` `0x10337d40`

_64 bytes. (leaf/helper — see body)_

```c
char sub_10337d40(int a0, int a1, int a2, char a3)
{
    unsigned int v5;  // ecx
    int v6;  // eax
    int v7;  // ecx
    int v8;  // edx
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x6]
    char v4;  // [bp-0x5]

    v2 = v5;
    v4 = 0;
    v1 = &/* unsupported instruction */;
    v0 = &/* unsupported instruction */;
    v3 = sub_10337970();
    v6 = _INSERT(v3 CONCAT 0, 0, v4);
    v7 = _INSERT(0, 0, v3);
    v8 = _INSERT(0, 0, a3);
    return sub_10339f30(a0, a1, a2, v8, v7, v6);
}
```

## `sub_10337d80` `0x10337d80`

_38 bytes. (leaf/helper — see body)_

```c
int sub_10337d80(int i, int a1, unsigned int a2)
{
    int v0;  // eax

    for (; i != a1; i += 28)
    {
        sub_10338a70(i);
    }
    return v0;
}
```

## `sub_10337db0` `0x10337db0`

_78 bytes. (leaf/helper — see body)_

```c
char sub_10337db0(char a0, char a0, int a1, int a2)
{
    unsigned int v5;  // ecx
    int v6;  // edx
    int v7;  // eax
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]
    char v2;  // [bp-0x6]
    char v3;  // [bp-0x5]

    v1 = v5;
    v3 = 0;
    v0 = &/* unsupported instruction */;
    v2 = sub_10337970();
    v6 = _INSERT(0, 0, v3);
    v7 = _INSERT(v2 CONCAT 0, 0, v2);
    return sub_10339f80(sub_10349d70(&/* unsupported instruction */, sub_10349d70(&/* unsupported instruction */, a1, a2, v7, v6)));
}
```

## `sub_10337e00` `0x10337e00`

_38 bytes. (leaf/helper — see body)_

```c
int sub_10337e00(int i, int a1, int a2)
{
    int v0;  // eax

    for (; i != a1; i += 28)
    {
        sub_103325a0(i, a2);
    }
    return v0;
}
```

## `sub_10337e30` `0x10337e30`

_84 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10337e30(int a0, int a1, unsigned int a2, unsigned int a3, char a4)
{
    int v4;  // eax
    char v0;  // [bp-0xa]
    char v1;  // [bp-0x9]
    unsigned int v2;  // [bp-0x8]

    v2 = a2 - (int)((a1 - a0) / 28) * 28;
    v1 = 0;
    v4 = sub_10349d70(&/* unsupported instruction */, v0, _INSERT(v2, 0, a4), v1);
    sub_1033a080(a0, a1, v4);
    return v2;
}
```

## `sub_10337e90` `0x10337e90`

_8 bytes. (leaf/helper — see body)_

```c
int sub_10337e90(unsigned int a0)
{
    return a0;
}
```

## `sub_10337ea0` `0x10337ea0`

_108 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10337ea0(unsigned int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4135
    unsigned int v10;  // eax
    unsigned long v11;  // 4151
    unsigned long v12;  // 4123
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x8]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v10 = *((int *)v9);
    v1 = *((int *)v9);
    v0 = a0;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v1;
    sub_10337f10(g_1038e180 ^ &v3, a0, v10, sub_1036ee9e, -1, &v4);
    sub_10337f10(g_1038e180 ^ &v3, a0, v10, sub_1036ee9e, 0, &v4);
    v2 = 1;
    sub_10315800(a0 + 56);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v10;
    return a0;
}
```

## `sub_10337f10` `0x10337f10`

_78 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10337f10(unsigned int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4135
    unsigned long v11;  // 4151
    unsigned long v12;  // 4123
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036eec8;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    sub_10315800(v1);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v2;
    return v1;
}
```

## `sub_10337f60` `0x10337f60`

_158 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103908d8;
extern char g_103908e8;
extern char g_103908f0;

unsigned int sub_10337f60(unsigned int idx, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4139
    unsigned long v10;  // 4153
    unsigned long v11;  // 4142
    int v0;  // [bp-0x24]
    int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036ef03;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_10338000(a1, g_1038e180 ^ &v5);
    v4 = 0;
    v1 = (!a1 ? 0 : a1 + 104);
    v0 = v1;
    sub_10313b60(idx + 104);
    *((char **)idx) = &g_103908f0;
    *((char **)(idx + 84)) = &g_103908e8;
    *((char **)(idx + 104)) = &g_103908d8;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return idx;
}
```

## `sub_10338000` `0x10338000`

_148 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103908fc;
extern char g_10390904;

unsigned int * sub_10338000(unsigned int *a0, unsigned int a1)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4139
    unsigned long v9;  // 4153
    unsigned long v10;  // 4135
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]
    char v4;  // [bp-0x4]

    v3 = 4294967295;
    v2 = sub_1036ef33;
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v1 = *((int *)v8);
    v9 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v9) = &v1;
    sub_103380a0(a1, g_1038e180 ^ &v4);
    v3 = 0;
    v0 = (!a1 ? 0 : a1 + 84);
    sub_10313a80(a0 + 21, v0);
    *(a0) = &g_10390904;
    a0[21] = &g_103908fc;
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v10) = v1;
    return a0;
}
```

## `sub_103380a0` `0x103380a0`

_115 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103908a4;

int sub_103380a0(int a0, int a1)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4138
    unsigned int v9;  // eax
    unsigned long v10;  // 4154
    unsigned long v11;  // 4123
    int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v9 = *((int *)v8);
    v1 = *((int *)v8);
    v0 = a0;
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v10) = &v1;
    sub_10338120(a1, g_1038e180 ^ &v3, a0, v9, sub_1036ef63, -1, &v4);
    v2 = 0;
    *((char **)a0) = &g_103908a4;
    sub_10338580(a1 + 76);
    v11 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v11) = v9;
    return a0;
}
```

## `sub_10338120` `0x10338120`

_133 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103908b0;

unsigned int [12] sub_10338120(unsigned int *a0, unsigned int *idx)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4154
    unsigned int v11;  // ecx
    unsigned long v12;  // 4123
    unsigned int v0;  // [bp-0x18]
    unsigned int index[12];  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036ef93;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    index = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    index = a0;
    sub_10314290(index, idx);
    v4 = 0;
    index[0] = &g_103908b0;
    v11 = idx[11];
    index[10] = idx[10];
    index[11] = v11;
    sub_103145d0(index + 1, idx + 12);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v2;
    return index;
}
```

## `sub_103381b0` `0x103381b0`

_108 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_103381b0(unsigned int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4135
    unsigned int v10;  // eax
    unsigned long v11;  // 4151
    unsigned long v12;  // 4123
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x8]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v10 = *((int *)v9);
    v1 = *((int *)v9);
    v0 = a0;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v1;
    sub_10338220(g_1038e180 ^ &v3, a0, v10, sub_1036efce, -1, &v4);
    sub_10338220(g_1038e180 ^ &v3, a0, v10, sub_1036efce, 0, &v4);
    v2 = 1;
    sub_10315800(a0 + 56);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v10;
    return a0;
}
```

## `sub_10338220` `0x10338220`

_78 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10338220(unsigned int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4135
    unsigned long v11;  // 4151
    unsigned long v12;  // 4123
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036eff8;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    sub_103257a0(v1);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v2;
    return v1;
}
```

## `sub_10338270` `0x10338270`

_158 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390910;
extern char g_10390920;
extern char g_10390928;

unsigned int sub_10338270(unsigned int idx, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4139
    unsigned long v10;  // 4153
    unsigned long v11;  // 4142
    int v0;  // [bp-0x24]
    int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036f033;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_10338310(a1, g_1038e180 ^ &v5);
    v4 = 0;
    v1 = (!a1 ? 0 : a1 + 104);
    v0 = v1;
    sub_10313b60(idx + 104);
    *((char **)idx) = &g_10390928;
    *((char **)(idx + 84)) = &g_10390920;
    *((char **)(idx + 104)) = &g_10390910;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return idx;
}
```

## `sub_10338310` `0x10338310`

_148 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390934;
extern char g_1039093c;

unsigned int * sub_10338310(unsigned int *a0, unsigned int a1)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4139
    unsigned long v9;  // 4153
    unsigned long v10;  // 4135
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]
    char v4;  // [bp-0x4]

    v3 = 4294967295;
    v2 = sub_1036f063;
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v1 = *((int *)v8);
    v9 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v9) = &v1;
    sub_103383b0(a1, g_1038e180 ^ &v4);
    v3 = 0;
    v0 = (!a1 ? 0 : a1 + 84);
    sub_10313a80(a0 + 21, v0);
    *(a0) = &g_1039093c;
    a0[21] = &g_10390934;
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v10) = v1;
    return a0;
}
```

## `sub_103383b0` `0x103383b0`

_115 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103908cc;

unsigned int * sub_103383b0(unsigned int *a0, unsigned int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4154
    unsigned long v11;  // 4123
    unsigned int v0;  // [bp-0x18]
    unsigned int *v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036f093;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_10338120(v1, a1);
    v4 = 0;
    *(v1) = &g_103908cc;
    sub_103386a0(a1 + 76);
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_10338430` `0x10338430`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10338430(int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4137
    unsigned int v10;  // eax
    unsigned long v11;  // 4153
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v2 = 4294967295;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v10 = *((int *)v9);
    v1 = *((int *)v9);
    v0 = a0;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v1;
    v2 = 0;
    v12 = sub_103388a0(g_1038e180 ^ &v3, a0, v10, sub_1036f0b8, -1, &v4);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v10;
    return v12;
}
```

## `sub_10338480` `0x10338480`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10338480(int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4137
    unsigned int v10;  // eax
    unsigned long v11;  // 4153
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v2 = 4294967295;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v10 = *((int *)v9);
    v1 = *((int *)v9);
    v0 = a0;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v1;
    v2 = 0;
    v12 = sub_103388a0(g_1038e180 ^ &v3, a0, v10, sub_1036f0e8, -1, &v4);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v10;
    return v12;
}
```

## `sub_103384d0` `0x103384d0`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_103384d0(int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4137
    unsigned int v10;  // eax
    unsigned long v11;  // 4153
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v2 = 4294967295;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v10 = *((int *)v9);
    v1 = *((int *)v9);
    v0 = a0;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v1;
    v2 = 0;
    v12 = sub_103388a0(g_1038e180 ^ &v3, a0, v10, sub_1036f118, -1, &v4);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v10;
    return v12;
}
```

