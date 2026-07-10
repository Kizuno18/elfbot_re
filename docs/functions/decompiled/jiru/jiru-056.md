# elfbot.dll decompiled — jiru 0x1034a260..0x1034af7b

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1034a260` `0x1034a260`

_32 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

struct_0 ** sub_1034a260(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_10347550(sub_10331570(v0), a1);
}
```

## `sub_1034a280` `0x1034a280`

_88 bytes. (leaf/helper — see body)_

```c
void* sub_1034a280(void* a0, char a1)
{
    int v2;  // eax
    int v3;  // eax
    unsigned int *v0;  // [bp-0x10]
    unsigned int *v1;  // [bp-0xc]

    if (!a1)
    {
        v0 = sub_10341220(a0);
        v3 = sub_10341260(a0);
        *(v0) = ~(v3) & *(v0);
        return a0;
    }
    v1 = sub_10341220(a0);
    v2 = sub_10341260(a0);
    *(v1) = v2 | *(v1);
    return a0;
}
```

## `sub_1034a2e0` `0x1034a2e0`

_22 bytes. (leaf/helper — see body)_

```c
int sub_1034a2e0(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1034a4e0(a0, &v1);
    return a0;
}
```

## `sub_1034a300` `0x1034a300`

_51 bytes. (leaf/helper — see body)_

```c
int sub_1034a300(int a0, int a1, int a2)
{
    char v0;  // [bp-0x10]

    sub_103413d0(&v0, a0);
    sub_103413d0(a1, sub_1034a4c0(a2));
    return a1;
}
```

## `sub_1034a340` `0x1034a340`

_35 bytes. (leaf/helper — see body)_

```c
int sub_1034a340(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return -(0 < (sub_1034a500(a1, a0, &v1) & 0xff)) + 1;
}
```

## `sub_1034a370` `0x1034a370`

_118 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390c50;
extern char g_10390c58;

unsigned int * sub_1034a370(unsigned int *a0, unsigned int *a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4154
    unsigned long v11;  // 4135
    unsigned int v0;  // [bp-0x18]
    unsigned int *v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_10371503;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_10346940(v1, a1);
    v4 = 0;
    sub_103167f0(v1 + 5);
    *(v1) = &g_10390c58;
    v1[5] = &g_10390c50;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_1034a3f0` `0x1034a3f0`

_194 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390c2c;
extern char g_10390c3c;
extern char g_10390c44;

int sub_1034a3f0(unsigned int idx, unsigned int a1)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4139
    unsigned long v11;  // 4153
    unsigned long v12;  // 4123
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char v5;  // [bp-0x8], Other Possible Types: unsigned int
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_10371533;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v0 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    sub_103468a0(idx, a1);
    v5 = 0;
    sub_10316a00(idx + 40);
    v5 = 1;
    *((char **)idx) = &g_10390c44;
    *((char **)(idx + 20)) = &g_10390c3c;
    *((char **)(idx + 40)) = &g_10390c2c;
    v2 = (!a1 ? 0 : a1 + 20);
    v1 = (!idx ? 0 : idx + 20);
    sub_10316940(v1, v2);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v3;
    return idx;
}
```

## `sub_1034a4c0` `0x1034a4c0`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1034a4c0(int a0, int a1)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_10341660(v0, -(a1));
}
```

## `sub_1034a4e0` `0x1034a4e0`

_22 bytes. (leaf/helper — see body)_

```c
int sub_1034a4e0(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1034a540(a0, &v1);
    return a0;
}
```

## `sub_1034a500` `0x1034a500`

_62 bytes. (leaf/helper — see body)_

```c
char sub_1034a500(unsigned int *a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0xc]

    if (a0[1] == *((int *)(a1 + 4)) && a0[2] == *((int *)(a1 + 8)))
        v0 = 1;
    else
        v0 = 0;
    return v0;
}
```

## `sub_1034a540` `0x1034a540`

_109 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_1 *field_0;
    unsigned int field_4;
    unsigned int field_8;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

struct_0 * sub_1034a540(struct_0 *idx)
{
    unsigned int v3;  // eax
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = idx;
    if (!idx->field_0 || !idx->field_4)
        sub_10353616(idx, &v1);
    v3 = sub_10341600(idx);
    if (v3 + 1 > idx->field_0->field_0)
        sub_10353616();
    if (idx->field_8 >= 31)
    {
        idx->field_8 = 0;
        idx->field_4 = idx->field_4 + 4;
        return idx;
    }
    idx->field_8 = idx->field_8 + 1;
    return idx;
}
```

## `sub_1034a5b0` `0x1034a5b0`

_82 bytes. (leaf/helper — see body)_

```c
char sub_1034a5b0(char a0, char a0, unsigned int a1, unsigned int a2)
{
    unsigned int v9;  // ecx
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x6]
    char v7;  // [bp-0x5]

    v5 = v9;
    v7 = 0;
    v4 = &a1;
    v3 = &/* unsupported instruction */;
    v6 = sub_10337970();
    v4 = _INSERT(v6 CONCAT 0, 0, v7);
    *((char *)&v3) = v6;
    v2 = a2;
    v1 = a1;
    v0 = sub_10349d70(&/* unsupported instruction */);
    return sub_1034a930(sub_10349d70(&/* unsupported instruction */));
}
```

## `sub_1034a610` `0x1034a610`

_48 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_1034a610(unsigned int *i, unsigned int *a1, unsigned int *a2)
{
    while (i != a1)
    {
        a1 += 25;
        a2 += 25;
        sub_103469f0(a2, a1);
    }
    return a2;
}
```

## `sub_1034a640` `0x1034a640`

_20 bytes. (leaf/helper — see body)_

```c
int sub_1034a640(int a0, int a1)
{
    sub_103413d0(a0, a1);
    return a0;
}
```

## `sub_1034a660` `0x1034a660`

_96 bytes. (leaf/helper — see body)_

```c
int sub_1034a660(int a0)
{
    int v6;  // eax
    int v0;  // [bp-0x20]
    char v1;  // [bp-0x1c]
    char v2;  // [bp-0x10]
    char v3;  // [bp+0x8]
    char v4;  // [bp+0x14]
    char v5;  // [bp+0x20]

    while ((char)sub_1034a340(&v3, &v4))
    {
        v6 = sub_10341280(&v3, &v1);
        sub_10341280(&v5, &v2);
        sub_1034a860(v6, v0);
        sub_1034a2e0(&v5);
        sub_1034a2e0(&v3);
    }
    sub_103413d0(a0, &v5);
    return a0;
}
```

## `sub_1034a6c0` `0x1034a6c0`

_92 bytes. (leaf/helper — see body)_

```c
int sub_1034a6c0(int a0)
{
    char v0;  // [bp-0x1c]
    char v1;  // [bp-0x10]
    char v2;  // [bp+0x8]
    char v3;  // [bp+0x14]
    char v4;  // [bp+0x20]

    while ((char)sub_1034a340(&v2, &v3))
    {
        sub_10341280(sub_1034a880(&v1, sub_10341280(sub_1034a880(&v0), &v0)), &v1);
        sub_1034a860();
    }
    sub_103413d0(a0, &v4);
    return a0;
}
```

## `sub_1034a720` `0x1034a720`

_10 bytes. (leaf/helper — see body)_

```c
int sub_1034a720(unsigned int *a0)
{
    return *(a0);
}
```

## `sub_1034a730` `0x1034a730`

_29 bytes. (leaf/helper — see body)_

```c
int sub_1034a730(int a0, int a1, int a2, int a3)
{
    char v0;  // [bp+0x0]

    return sub_1034a9f0(a0, a1, a2, a3, &v0);
}
```

## `sub_1034a750` `0x1034a750`

_75 bytes. (leaf/helper — see body)_

```c
int sub_1034a750(int a0, unsigned int a1, unsigned int a2)
{
    int v0;  // [bp-0xc]
    int v1;  // [bp-0x8]

    v0 = a1 - a0 >> 2;
    v1 = a2 - v0 * 4;
    if (v0 > 0)
        sub_10353626(v1, v0 * 4, a0, v0 * 4);
    return v1;
}
```

## `sub_1034a7a0` `0x1034a7a0`

_56 bytes. (leaf/helper — see body)_

```c
int sub_1034a7a0(int a0, int a1, int a2)
{
    unsigned int v3;  // ecx
    int v5;  // ecx
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    char v2;  // [bp-0x5]

    v2 = 0;
    v1 = _INSERT(v3, 0, v2);
    v0 = &/* unsupported instruction */;
    v5 = _INSERT(0, 0, *((char *)sub_103378b0((char *)&/* unsupported instruction */ + 2)));
    return sub_1034aa50(a0, a1, a2, v5);
}
```

## `sub_1034a7e0` `0x1034a7e0`

_122 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int * sub_1034a7e0(int *a0, int a1, char a2)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4147
    unsigned int v12;  // eax
    unsigned long v13;  // 4163
    int v14;  // edx
    unsigned long v15;  // 4123
    int *v0;  // [bp-0x2c]
    int v1;  // [bp-0x28]
    int v2;  // [bp-0x24]
    int *v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]
    char v7;  // [bp+0x0]

    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v12 = *((int *)v11);
    v4 = *((int *)v11);
    v3 = a0;
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v13) = &v4;
    *(a0) = a1;
    v14 = _INSERT(0, 0, a2);
    sub_1034aa90(a1, v14, g_1038e180 ^ &v6, a0, v12, sub_1037155b, -1, &v7);
    v5 = 0;
    v2 = a1;
    v1 = a1;
    v0 = a0 + 1;
    sub_10334530();
    v15 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v15) = v12;
    return a0;
}
```

## `sub_1034a860` `0x1034a860`

_30 bytes. (leaf/helper — see body)_

```c
void* sub_1034a860(void* a0, int a1)
{
    void* v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_1034a280(v0, sub_10340c70(a1));
}
```

## `sub_1034a880` `0x1034a880`

_22 bytes. (leaf/helper — see body)_

```c
int sub_1034a880(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1034a8a0(a0, &v1);
    return a0;
}
```

## `sub_1034a8a0` `0x1034a8a0`

_22 bytes. (leaf/helper — see body)_

```c
int sub_1034a8a0(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1034a8c0(a0, &v1);
    return a0;
}
```

## `sub_1034a8c0` `0x1034a8c0`

_105 bytes. (leaf/helper — see body)_

```c
char * sub_1034a8c0(char *a0)
{
    char *v2;  // eax
    char *v3;  // eax
    char *idx;  // [bp-0x8]

    idx = a0;
    idx = a0;
    if (*((int *)&idx[8]))
    {
        *((unsigned int *)&idx[8]) = *((int *)&idx[8]) - 1;
        return idx;
    }
    if (!*((int *)&idx) || !*((int *)&idx[4]))
        sub_10353616();
    v2 = sub_10341710(idx);
    if (*((int *)&idx[4]) <= v2)
        sub_10353616();
    v3 = *((int *)&idx[4]) - 4;
    *((char **)&idx[4]) = v3;
    *((unsigned int *)&idx[8]) = 31;
    return v3;
}
```

## `sub_1034a930` `0x1034a930`

_131 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1034a930(unsigned int a0, unsigned int a1, int i, int a3, int a4, int a5)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4144
    unsigned long v11;  // 4168
    unsigned long v12;  // 4126
    unsigned int v0;  // [bp-0x28]
    int v1;  // [bp-0x18], Other Possible Types: unsigned int
    char *v2;  // [bp-0x14], Other Possible Types: unsigned int
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_10371580;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v2 = a0;
    v1 = a0;
    v0 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    v2 = &v0;
    v1 = a4;
    for (v5 = 0; i != a3; i += 100)
    {
        sub_10346d30(a5, a4, i);
        a4 += 100;
    }
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v3;
    return a4;
}
```

## `sub_1034a997` `0x1034a997`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1034a997(void)
{
    sub_1034a9a2();
    return;
}
```

## `sub_1034a9a2` `0x1034a9a2`

_33 bytes. (leaf/helper — see body)_

```c
extern char g_1034a9d5;

int sub_1034a9a2(void)
{
    unsigned int v1;  // [bp+0xffff0]
    unsigned int v2;  // [bp+0x100000]
    unsigned int v3;  // [bp+0x100014]

    if (v1 == v3)
    {
        sub_103533ea(0, 0);
        v2 = 4294967295;
        return &g_1034a9d5;
    }
    return sub_1034a9ad();
}
```

## `sub_1034a9ad` `0x1034a9ad`

_20 bytes. (leaf/helper — see body)_

```c
int sub_1034a9ad(unsigned int a0, int a1)
{
    unsigned int v1;  // [bp+0xffff0]
    int v2;  // [bp+0x100018]

    sub_10340a00(v2, a1);
    v1 += 100;
    return sub_1034a9a2();
}
```

## `sub_1034a9f0` `0x1034a9f0`

_82 bytes. (leaf/helper — see body)_

```c
char sub_1034a9f0(char a0, char a0, unsigned int a1, unsigned int a2)
{
    unsigned int v9;  // ecx
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x6]
    char v7;  // [bp-0x5]

    v5 = v9;
    v7 = 0;
    v4 = &a1;
    v3 = &/* unsupported instruction */;
    v6 = sub_10337970();
    v4 = _INSERT(v6 CONCAT 0, 0, v7);
    *((char *)&v3) = v6;
    v2 = a2;
    v1 = a1;
    v0 = sub_10349d70(&/* unsupported instruction */);
    return sub_1034acb0(sub_10349d70(&/* unsupported instruction */));
}
```

## `sub_1034aa50` `0x1034aa50`

_60 bytes. (leaf/helper — see body)_

```c
char sub_1034aa50(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    char v3;  // [bp-0x9]
    unsigned int v4;  // [bp-0x8]

    v4 = a0 + a1 * 4;
    v3 = 0;
    v2 = _INSERT(a0, 0, v3);
    v1 = a2;
    v0 = a1;
    return sub_1034ad00(sub_10349d70(&/* unsupported instruction */));
}
```

## `sub_1034aa90` `0x1034aa90`

_164 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int * sub_1034aa90(unsigned int *a0, int a1, char a2)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4149
    unsigned long v13;  // 4171
    int v14;  // edi
    int v15;  // esi
    int v16;  // ebx
    unsigned long v18;  // 4126
    unsigned int v0;  // [bp-0x34]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    char *v4;  // [bp-0x14], Other Possible Types: unsigned int *
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    char v7;  // [bp-0x8], Other Possible Types: unsigned int
    char v8;  // [bp-0x4]

    v7 = 4294967295;
    v6 = sub_103715ab;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v5 = *((int *)v12);
    v4 = a0;
    v0 = g_1038e180 ^ &v8;
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v5;
    v4 = &v0;
    *(a0) = 0;
    v7 = 0;
    v2 = sub_10350a53(20, g_1038e180 ^ &v8, v14, v15, v16);
    v7 = 1;
    if (v2)
        v1 = sub_1034ab60(a1, _INSERT(0, 0, a2));
    else
        v1 = 0;
    v3 = v1;
    v7 = 0;
    *(a0) = v3;
    v18 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v18) = v5;
    return a0;
}
```

## `sub_1034ab16` `0x1034ab16`

_34 bytes. (leaf/helper — see body)_

```c
extern char g_1034ab3f;

int sub_1034ab16(void)
{
    unsigned int v1;  // [bp+0x100000]

    sub_1034ad30(/* unsupported instruction */ + 8);
    sub_103533ea(0, 0);
    v1 = 4294967295;
    return &g_1034ab3f;
}
```

## `sub_1034ab60` `0x1034ab60`

_98 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
} struct_0;

extern unsigned int g_1038e180;
extern char g_10390ce8;

struct_0 * sub_1034ab60(struct_0 *a0, unsigned int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4135
    unsigned long v10;  // 4151
    unsigned long v11;  // 4140
    unsigned int v0;  // [bp-0x18]
    struct_0 *v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_103715d8;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_1033bba0(v1);
    *((char **)&v1->padding_0[0]) = &g_10390ce8;
    v1->field_c = a1;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_1034abd0` `0x1034abd0`

_29 bytes. (leaf/helper — see body)_

```c
int sub_1034abd0(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_1034ad30(a0 + 12, a0, &v1);
}
```

## `sub_1034abf0` `0x1034abf0`

_56 bytes. (leaf/helper — see body)_

```c
extern int g_1038dee8;

unsigned int sub_1034abf0(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0xc]

    v0 = (!(char)sub_103531e8(&g_1038dee8) ? 0 : a0 + 16);
    return v0;
}
```

## `sub_1034ac30` `0x1034ac30`

_44 bytes. (leaf/helper — see body)_

```c
int sub_1034ac30(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1034ac60(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_1034ac60` `0x1034ac60`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1034ac60(unsigned int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4137
    unsigned long v11;  // 4153
    int v12;  // eax
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_10371608;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    v4 = 0;
    v4 = 4294967295;
    v12 = sub_1033bbd0(v1);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_1034acb0` `0x1034acb0`

_69 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1034acb0(int a0, unsigned int a1, int a2)
{
    int v2;  // eax
    unsigned int v0;  // [bp-0xc]
    int v1;  // [bp-0x8]

    v2 = a1 - a0;
    v1 = v2 >> 2;
    v0 = a2 + v1 * 4;
    if (v2 >> 2)
        sub_10353626(a2, v1 * 4, a0, v1 * 4);
    return v0;
}
```

## `sub_1034ad00` `0x1034ad00`

_43 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1034ad00(unsigned int *iter, unsigned int a1, unsigned int *a2)
{
    unsigned int v0;  // eax

    for (; a1 > 0; iter += 1)
    {
        *(iter) = *(a2);
        a1 -= 1;
    }
    return v0;
}
```

## `sub_1034ad30` `0x1034ad30`

_16 bytes. (leaf/helper — see body)_

```c
int sub_1034ad30(unsigned int a0, unsigned int a1)
{
    return a1;
}
```

## `sub_1034ad40` `0x1034ad40`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1034ad40(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_10346a60(a0 - 40, v0);
}
```

## `sub_1034ad50` `0x1034ad50`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1034ad50(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_10343490(a0 - 20, v0);
}
```

## `sub_1034ad60` `0x1034ad60`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1034ad60(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_1033fed0(a0 - 40, v0);
}
```

## `sub_1034ad70` `0x1034ad70`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1034ad70(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_10346a60(a0 - 20, v0);
}
```

## `sub_1034ad80` `0x1034ad80`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1034ad80(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_1033fed0(a0 - 20, v0);
}
```

## `sub_1034ad90` `0x1034ad90`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1034ad90(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_103434c0(a0 - 20, v0);
}
```

## `sub_1034ada0` `0x1034ada0`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1034ada0(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_1033ff00(a0 - 20, v0);
}
```

## `sub_1034adb0` `0x1034adb0`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1034adb0(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_10343490(a0 - 40, v0);
}
```

## `sub_1034adc0` `0x1034adc0`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1034adc0(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_10346a90(a0 - 20, v0);
}
```

## `sub_1034add0` `0x1034add0`

_111 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
    char padding_1[3];
    unsigned int field_4;
} struct_0;

extern unsigned int g_1038e180;
extern unsigned int g_103a0da8;

unsigned int sub_1034add0(unsigned int *a0, struct_0 *a1)
{
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // fs
    unsigned long v13;  // 4159
    unsigned long v14;  // 4181
    unsigned int v15;  // eax
    unsigned long v16;  // 4119
    unsigned int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x2c]
    unsigned int v2;  // [bp-0x28]
    unsigned int v3;  // [bp-0x24]
    char *v4;  // [bp-0x1c]
    unsigned int v5;  // [bp-0x14]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]
    char v9;  // [bp-0x4]

    v8 = 4294967294;
    v7 = &g_103a0da8;
    v6 = sub_10354150;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v5 = *((int *)v13);
    v7 ^= g_1038e180;
    v0 = g_1038e180 ^ &v9;
    v14 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v14) = &v5;
    v4 = &v0;
    a1->field_0 = 0;
    a1->field_4 = 0;
    v8 = 0;
    v15 = a0(a1, g_1038e180 ^ &v9, v1, v2, v3);
    v8 = 4294967294;
    v16 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v16) = v5;
    return v15;
}
```

## `sub_1034ae2d` `0x1034ae2d`

_13 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

void sub_1034ae2d(void)
{
    unsigned int v1;  // [bp+0xfffe8]
    struct_0 **v2;  // [bp+0xffff0]

    v1 = *(v2)->field_0;
    sub_1034ae3a();
    return;
}
```

## `sub_1034ae3a` `0x1034ae3a`

_14 bytes. (leaf/helper — see body)_

```c
void sub_1034ae3a(void)
{
    int v2;  // eax
    int v1;  // [bp+0xffff0]

    sub_1034ae80(v1, v2);
    return;
}
```

## `sub_1034ae48` `0x1034ae48`

_25 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
    char padding_1[3];
    unsigned int field_4;
} struct_0;

int sub_1034ae48(void)
{
    unsigned int v1;  // [bp+0xfffe8]
    unsigned int v2;  // [bp+0x100000]
    struct_0 *v3;  // [bp+0x100010]

    v3->field_0 = 1;
    v3->field_4 = v1;
    v2 = 4294967294;
}
```

## `sub_1034ae80` `0x1034ae80`

_38 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    struct struct_1 *field_8;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

unsigned int sub_1034ae80(unsigned int a0, struct_0 *a1)
{
    if (a1->field_8)
        a1->field_8(a0, a1);
    return 1;
}
```

## `sub_1034aed7` `0x1034aed7`

_31 bytes. (leaf/helper — see body)_

```c
int sub_1034aed7(void)
{
    unsigned long v1;  // ldt
    unsigned long v2;  // gdt
    unsigned short v3;  // fs
    unsigned long v4;  // 4149
    unsigned int v5;  // ebx
    unsigned int v0;  // [bp+0x4]

    v4 = _ccall(v1, v2, (unsigned int)v3, 0);
    *((unsigned int *)v4) = v0;
    if (v5)
        return;
    return;
}
```

## `sub_1034aeed` `0x1034aeed`

_24 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1034aeed(unsigned int a0, unsigned int a1, unsigned int *idx)
{
    idx[41] = 4294967295;
    idx[46] = idx[46] + 4;
    return 0;
}
```

## `sub_1034af10` `0x1034af10`

_23 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1034af10(void)
{
    return 0;
}
```

## `sub_1034af77` `0x1034af77`

_4 bytes. (leaf/helper — see body)_

```c
int sub_1034af77(void)
{
    unsigned int *v1;  // eax

    *(v1) = *(v1) + 1;
    sub_1034af7b();
    return;
}
```

## `sub_1034af7b` `0x1034af7b`

_48 bytes. (leaf/helper — see body)_

```c
int sub_1034af7b(void)
{
    unsigned int v3;  // eax
    unsigned int v4;  // esi
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4143
    unsigned int v1;  // [bp+0xffff4]
    unsigned int *v2;  // [bp+0x100010]

    v2(v3);
    v1 = v4;
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v8) = v3;
}
```

