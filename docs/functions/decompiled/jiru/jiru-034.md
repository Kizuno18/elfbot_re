# elfbot.dll decompiled — jiru 0x10327150..0x103291de

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10327150` `0x10327150`

_19 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

struct_0 * sub_10327150(int a0)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_10326fd0(v0);
}
```

## `sub_10327170` `0x10327170`

_179 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern int g_10390370;

unsigned int sub_10327170(int a0, unsigned int a1)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4137
    unsigned long v12;  // 4151
    unsigned int v13;  // eax
    unsigned long v14;  // 4113
    int v0;  // [bp-0x3c]
    int v1;  // [bp-0x38]
    unsigned int v2;  // [bp-0x30]
    char v3;  // [bp-0x2c]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    char v6;  // [bp-0x8], Other Possible Types: unsigned int
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036bec6;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    v2 = 0;
    if ((char)sub_103275b0(g_1038e180 ^ &v7))
    {
        sub_1032dfc0(g_10390370);
        v6 = 0;
        v2 |= 1;
        v13 = a1;
    }
    else
    {
        v1 = sub_10326a70(a0, &v3);
        v0 = v1;
        v6 = 1;
        sub_1032e020(v0);
        v2 |= 1;
        v6 = 0;
        sub_10314610(&v3);
        v13 = a1;
    }
    v14 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v14) = v4;
    return v13;
}
```

## `sub_10327230` `0x10327230`

_179 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern int g_10390370;

int sub_10327230(int a0, int a1)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4137
    unsigned long v12;  // 4151
    int v13;  // eax
    unsigned long v14;  // 4113
    unsigned int v0;  // [bp-0x3c]
    unsigned int v1;  // [bp-0x38]
    unsigned int v2;  // [bp-0x30]
    char v3;  // [bp-0x2c]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    char v6;  // [bp-0x8], Other Possible Types: unsigned int
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036bf02;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    v2 = 0;
    if ((char)sub_103275b0(g_1038e180 ^ &v7))
    {
        sub_10325820(a1, g_10390370);
        v6 = 0;
        v2 |= 1;
        v13 = a1;
    }
    else
    {
        v1 = sub_10326c30(a0, &v3);
        v0 = v1;
        v6 = 1;
        sub_10325880(a1, v0);
        v2 |= 1;
        v6 = 0;
        sub_1031a3a0(&v3);
        v13 = a1;
    }
    v14 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v14) = v4;
    return v13;
}
```

## `sub_103272f0` `0x103272f0`

_179 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern int g_10390370;

unsigned int sub_103272f0(int a0, unsigned int a1)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4137
    unsigned long v12;  // 4151
    unsigned int v13;  // eax
    unsigned long v14;  // 4113
    int v0;  // [bp-0x3c]
    int v1;  // [bp-0x38]
    unsigned int v2;  // [bp-0x30]
    char v3;  // [bp-0x2c]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    char v6;  // [bp-0x8], Other Possible Types: unsigned int
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036bf3e;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    v2 = 0;
    if ((char)sub_103275b0(g_1038e180 ^ &v7))
    {
        sub_1032e100(g_10390370);
        v6 = 0;
        v2 |= 1;
        v13 = a1;
    }
    else
    {
        v1 = sub_10326df0(a0, &v3);
        v0 = v1;
        v6 = 1;
        sub_1032e160(v0);
        v2 |= 1;
        v6 = 0;
        sub_103257d0(&v3);
        v13 = a1;
    }
    v14 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v14) = v4;
    return v13;
}
```

## `sub_103273b0` `0x103273b0`

_19 bytes. (leaf/helper — see body)_

```c
int sub_103273b0(int a0)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_10326e70(v0);
}
```

## `sub_103273d0` `0x103273d0`

_19 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

struct_0 * sub_103273d0(int a0)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_10326fd0(v0);
}
```

## `sub_103273f0` `0x103273f0`

_19 bytes. (leaf/helper — see body)_

```c
int sub_103273f0(int a0)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_10327130(v0);
}
```

## `sub_10327410` `0x10327410`

_19 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

struct_0 * sub_10327410(int a0)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_10327150(v0);
}
```

## `sub_10327430` `0x10327430`

_95 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10327430(int a0, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4140
    unsigned long v10;  // 4154
    unsigned long v11;  // 4131
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036bf72;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = 0;
    sub_10326a70(a0, a1);
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return a1;
}
```

## `sub_10327490` `0x10327490`

_95 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10327490(int a0, unsigned int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4140
    unsigned long v10;  // 4154
    unsigned long v11;  // 4131
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036bfa6;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = 0;
    sub_10326c30(a0, a1);
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return a1;
}
```

## `sub_103274f0` `0x103274f0`

_95 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_103274f0(int a0, unsigned int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4140
    unsigned long v10;  // 4154
    unsigned long v11;  // 4131
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036bfda;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = 0;
    sub_10327170(a0, a1);
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return a1;
}
```

## `sub_10327550` `0x10327550`

_95 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10327550(int a0, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4140
    unsigned long v10;  // 4154
    unsigned long v11;  // 4131
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036c00e;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = 0;
    sub_10327230(a0, a1);
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return a1;
}
```

## `sub_103275b0` `0x103275b0`

_64 bytes. (leaf/helper — see body)_

```c
char sub_103275b0(int a0)
{
    unsigned int v0;  // [bp-0xc]

    if (!(char)sub_103275f0() && !*((int *)sub_10333eb0(a0)))
        v0 = 1;
    else
        v0 = 0;
    return v0;
}
```

## `sub_103275f0` `0x103275f0`

_64 bytes. (leaf/helper — see body)_

```c
char sub_103275f0(int a0)
{
    unsigned int v0;  // [bp-0xc]

    if (!sub_10333e70(a0) && !sub_10333e90(a0))
        v0 = 0;
    else
        v0 = 1;
    return v0;
}
```

## `sub_10327630` `0x10327630`

_37 bytes. (leaf/helper — see body)_

```c
int sub_10327630(int a0)
{
    unsigned int v0;  // [bp-0x8]

    v0 = sub_10333e90(a0, a0);
    return v0;
}
```

## `sub_10327660` `0x10327660`

_228 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

extern struct_0 *g_1038b040;
extern unsigned int g_1038e180;

unsigned int sub_10327660(unsigned int a0, struct_0 *a1)
{
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    unsigned short v14;  // fs
    unsigned long v15;  // 4144
    unsigned long v16;  // 4158
    unsigned int v17;  // eax
    unsigned int v18;  // eax
    int v19;  // eax
    unsigned long v21;  // 4117
    unsigned int v0;  // [bp-0x68]
    unsigned int v1;  // [bp-0x3c]
    unsigned int v2;  // [bp-0x38]
    unsigned int v3;  // [bp-0x34]
    unsigned int v4;  // [bp-0x30]
    unsigned int v5;  // [bp-0x2c]
    unsigned int v6;  // [bp-0x28]
    int v7;  // [bp-0x14]
    unsigned int v8;  // [bp-0x10]
    unsigned int v9;  // [bp-0xc]
    char v10;  // [bp-0x8], Other Possible Types: unsigned int
    char v11;  // [bp-0x4]

    v10 = 4294967295;
    v9 = sub_1036c04a;
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    v8 = *((int *)v15);
    v5 = g_1038e180 ^ &v11;
    v16 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v16) = &v8;
    v6 = 0;
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v17 = sub_1032db60(sub_1031e920(a1));
    v7 = g_1038b040(0, 0, v17);
    sub_10333ef0(v7 + 1, 0);
    v10 = 1;
    v0 = sub_1032e2e0(0, v7 + 1, 0, 0);
    v18 = sub_1032db60(sub_1031e920(a1));
    g_1038b040(0, 0, v18);
    v19 = sub_1032e2e0(v7);
    sub_1031bdd0(a0, sub_1032e2e0(0, v19), 0);
    v6 |= 1;
    v10 = 0;
    sub_1032e280(v19);
    v21 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int *)v21) = v8;
    return a0;
}
```

## `sub_10327750` `0x10327750`

_220 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b104;
extern unsigned int g_1038e180;

int sub_10327750(unsigned int a0, unsigned int a1)
{
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    unsigned short v14;  // fs
    unsigned long v15;  // 4140
    unsigned long v16;  // 4154
    unsigned int v17;  // eax
    unsigned int v18;  // eax
    int v19;  // eax
    unsigned long v20;  // 4117
    int v0;  // [bp-0x5c]
    unsigned int v1;  // [bp-0x58]
    int v2;  // [bp-0x38]
    unsigned int v3;  // [bp-0x34]
    unsigned int v4;  // [bp-0x30]
    unsigned int v5;  // [bp-0x2c]
    unsigned int v6;  // [bp-0x28]
    int v7;  // [bp-0x14]
    unsigned int v8;  // [bp-0x10]
    unsigned int v9;  // [bp-0xc]
    char v10;  // [bp-0x8], Other Possible Types: unsigned int
    char v11;  // [bp-0x4]

    v10 = 4294967295;
    v9 = sub_1036c086;
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    v8 = *((int *)v15);
    v5 = g_1038e180 ^ &v11;
    v16 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v16) = &v8;
    v6 = 0;
    v4 = 0;
    v3 = 0;
    v2 = sub_1031e920(a1);
    v17 = (unsigned int)sub_102ec980(a1);
    v7 = g_1038b104(0, 0, v17);
    sub_10333f40(v7 + 1, 0);
    v10 = 1;
    v1 = sub_1032e410(0, v7 + 1);
    v0 = sub_1031e920(a1);
    v18 = (unsigned int)sub_102ec980(a1);
    g_1038b104(0, 0, v18);
    v19 = sub_1032e410(0, sub_1032e410(v7));
    sub_10333f90(v19);
    v6 |= 1;
    v10 = 0;
    sub_1032e3f0(v19);
    v20 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int *)v20) = v8;
    return a0;
}
```

## `sub_10327830` `0x10327830`

_366 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    int field_4;
    int field_8;
    int field_c;
    unsigned int field_10;
    unsigned int field_14;
    unsigned int field_18;
    unsigned int field_1c;
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
    unsigned short field_30;
    unsigned short field_32;
    char padding_34[4];
    unsigned int field_38;
    unsigned int field_3c;
    unsigned int field_40;
} struct_0;

typedef struct struct_1 {
    char padding_0[4];
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
    unsigned int field_10;
    unsigned int field_14;
    unsigned int field_18;
    unsigned int field_1c;
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
    unsigned short field_30;
    unsigned short field_32;
    char padding_34[4];
    unsigned int field_38;
    unsigned int field_3c;
    unsigned int field_40;
} struct_1;

extern unsigned int g_1038e180;

struct_0 * sub_10327830(struct_0 *a0, struct_1 *index)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4142
    unsigned long v10;  // 4158
    unsigned long v11;  // 4336
    unsigned int v0;  // [bp-0x18]
    struct_0 *idx;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036c0c8;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    idx = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    idx = a0;
    sub_10326770(idx + 1, index->field_4);
    v4 = 0;
    sub_10326770(&idx[2].field_1c, index->field_8);
    v4 = 1;
    sub_10326770(&idx[3].field_38, index->field_c);
    v4 = 2;
    idx->field_0 = 0x44;
    idx->field_4 = sub_10327130(idx + 1);
    idx->field_8 = sub_10327130(&idx[2].field_1c);
    idx->field_c = sub_10327130(&idx[3].field_38);
    idx->field_10 = index->field_10;
    idx->field_14 = index->field_14;
    idx->field_18 = index->field_18;
    idx->field_1c = index->field_1c;
    idx->field_20 = index->field_20;
    idx->field_24 = index->field_24;
    idx->field_28 = index->field_28;
    idx->field_2c = index->field_2c;
    idx->field_30 = index->field_30;
    idx->field_32 = index->field_32;
    idx->field_38 = index->field_38;
    idx->field_3c = index->field_3c;
    idx->field_40 = index->field_40;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return idx;
}
```

## `sub_103279a0` `0x103279a0`

_193 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    int field_4;
    int field_8;
    int field_c;
} struct_0;

extern unsigned int g_1038e180;

struct_0 * sub_103279a0(struct_0 *a0, unsigned int *i)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4139
    unsigned long v10;  // 4159
    unsigned int v11;  // ecx
    struct_0 *iter;  // edi
    unsigned long v13;  // 4132
    unsigned int v0;  // [bp-0x20]
    struct_0 *idx;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036c10a;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    idx = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    idx = a0;
    v11 = 0x11;
    for (iter = idx; v11; i += 1)
    {
        v11 -= 1;
        iter->field_0 = *(i);
        iter = &iter->field_4;
    }
    sub_1032d600();
    v4 = 0;
    sub_1032d600();
    v4 = 1;
    sub_1032d600();
    v4 = 2;
    idx->field_4 = sub_10327130(&idx[4].field_4);
    idx->field_8 = sub_10327130(&idx[10].field_4);
    idx->field_c = sub_10327130(&idx[16].field_4);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v2;
    return idx;
}
```

## `sub_10327a70` `0x10327a70`

_366 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    struct struct_0 *field_4;
    struct struct_0 *field_8;
    struct struct_0 *field_c;
    unsigned int field_10;
    unsigned int field_14;
    unsigned int field_18;
    unsigned int field_1c;
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
    unsigned short field_30;
    unsigned short field_32;
    char padding_34[4];
    unsigned int field_38;
    unsigned int field_3c;
    unsigned int field_40;
} struct_0;

typedef struct struct_1 {
    char padding_0[4];
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
    unsigned int field_10;
    unsigned int field_14;
    unsigned int field_18;
    unsigned int field_1c;
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
    unsigned short field_30;
    unsigned short field_32;
    char padding_34[4];
    unsigned int field_38;
    unsigned int field_3c;
    unsigned int field_40;
} struct_1;

typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

extern unsigned int g_1038e180;

struct_0 * sub_10327a70(struct_0 *a0, struct_1 *index)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4142
    unsigned long v10;  // 4158
    unsigned long v11;  // 4336
    unsigned int v0;  // [bp-0x18]
    struct_0 *idx;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036c14c;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    idx = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    idx = a0;
    sub_103266a0(idx + 1, index->field_4);
    v4 = 0;
    sub_103266a0(&idx[2].field_1c, index->field_8);
    v4 = 1;
    sub_103266a0(&idx[3].field_38, index->field_c);
    v4 = 2;
    idx->field_0 = 0x44;
    idx->field_4 = sub_10327150(idx + 1);
    idx->field_8 = sub_10327150(&idx[2].field_1c);
    idx->field_c = sub_10327150(&idx[3].field_38);
    idx->field_10 = index->field_10;
    idx->field_14 = index->field_14;
    idx->field_18 = index->field_18;
    idx->field_1c = index->field_1c;
    idx->field_20 = index->field_20;
    idx->field_24 = index->field_24;
    idx->field_28 = index->field_28;
    idx->field_2c = index->field_2c;
    idx->field_30 = index->field_30;
    idx->field_32 = index->field_32;
    idx->field_38 = index->field_38;
    idx->field_3c = index->field_3c;
    idx->field_40 = index->field_40;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return idx;
}
```

## `sub_10327be0` `0x10327be0`

_193 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    struct struct_0 *field_4;
    struct struct_0 *field_8;
    struct struct_0 *field_c;
} struct_0;

typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

extern unsigned int g_1038e180;

struct_0 * sub_10327be0(struct_0 *a0, unsigned int *i)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4139
    unsigned long v10;  // 4159
    unsigned int v11;  // ecx
    struct_0 *iter;  // edi
    unsigned long v13;  // 4132
    unsigned int v0;  // [bp-0x20]
    struct_0 *idx;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036c18e;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    idx = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    idx = a0;
    v11 = 0x11;
    for (iter = idx; v11; i += 1)
    {
        v11 -= 1;
        iter->field_0 = *(i);
        iter = &iter->field_4;
    }
    sub_1032d600();
    v4 = 0;
    sub_1032d600();
    v4 = 1;
    sub_1032d600();
    v4 = 2;
    idx->field_4 = sub_10327150(&idx[4].field_4);
    idx->field_8 = sub_10327150(&idx[10].field_4);
    idx->field_c = sub_10327150(&idx[16].field_4);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v2;
    return idx;
}
```

## `sub_10327cb0` `0x10327cb0`

_125 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1c0;
extern unsigned int g_1038e180;

char sub_10327cb0(void)
{
    unsigned int v0;  // [bp-0xb0]
    unsigned int v1;  // [bp-0xac]
    unsigned int v2;  // [bp-0xa8]
    unsigned int v3;  // [bp-0xa4]
    unsigned int v4;  // [bp-0x9c]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]
    char v8;  // [bp-0x4]

    v5 = g_1038e180 ^ &v8;
    v7 = 4;
    v6 = 0;
    v1 = 148;
    g_1038b1c0(&v1);
    if (v4 == 1 && v2 == 4 && !v3)
        v0 = 1;
    else
        v0 = 0;
    return sub_10351225();
}
```

## `sub_10327d30` `0x10327d30`

_84 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1c0;
extern unsigned int g_1038e180;

int sub_10327d30(void)
{
    unsigned int v0;  // [bp-0xa4]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]

    v2 = g_1038e180 ^ &v3;
    v0 = 148;
    g_1038b1c0(&v0, 148);
    return sub_10351225();
}
```

## `sub_10327d74` `0x10327d74`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10327d74(void)
{
}
```

## `sub_10327d90` `0x10327d90`

_162 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10327d90(void)
{
    unsigned int v0;  // [bp-0xb4]
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]
    char v8;  // [bp-0x4]

    v4 = g_1038e180 ^ &v8;
    v6 = 5;
    v7 = 1;
    v5 = 2;
    v0 = 156;
    return sub_10351225();
}
```

## `sub_10327e40` `0x10327e40`

_30 bytes. (leaf/helper — see body)_

```c
int sub_10327e40(void)
{
    unsigned int v2;  // ecx
    unsigned int v0;  // [bp-0x8]

    v0 = v2;
    v0 = 600;
    return -(sub_10327d30() < 600) + 1;
}
```

## `sub_10327e60` `0x10327e60`

_417 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

extern struct_0 *g_1038b040;
extern unsigned int g_1038e180;

int sub_10327e60(int a0, struct_0 *a1)
{
    unsigned long v14;  // ldt
    unsigned long v15;  // gdt
    unsigned int v24;  // eax
    unsigned long v26;  // 4113
    unsigned short v16;  // fs
    unsigned long v17;  // 4136
    unsigned long v18;  // 4150
    unsigned int v19;  // eax
    unsigned int v20;  // eax
    int v22;  // eax
    unsigned int v23;  // eax
    unsigned int v0;  // [bp-0x80]
    unsigned int v1;  // [bp-0x54]
    unsigned int v2;  // [bp-0x50]
    int v3;  // [bp-0x4c], Other Possible Types: unsigned int
    char *v4;  // [bp-0x48], Other Possible Types: unsigned int
    unsigned int v5;  // [bp-0x44]
    unsigned int v6;  // [bp-0x40]
    int v7;  // [bp-0x2c]
    int v8;  // [bp-0x18]
    unsigned int v9;  // [bp-0x14]
    unsigned int v10;  // [bp-0x10]
    unsigned int v11;  // [bp-0xc]
    char v12;  // [bp-0x8], Other Possible Types: unsigned int
    char v13;  // [bp-0x4]

    v12 = 4294967295;
    v11 = sub_1036c1d2;
    v17 = _ccall(v14, v15, (unsigned int)v16, 0);
    v10 = *((int *)v17);
    v5 = g_1038e180 ^ &v13;
    v18 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int **)v18) = &v10;
    v6 = 0;
    v9 = 0;
    if (sub_10327cb0())
    {
        v4 = &v9;
        v3 = "*";
        v2 = 0;
        v1 = 0;
        v19 = sub_1032db60(sub_1031e920(a1));
        v8 = g_1038b040(0, 64, v19);
        sub_10333ef0(v8 + 1, 0);
        v12 = 1;
        v0 = sub_1032e2e0(0, sub_1032e2a0("*", &v9));
        v20 = sub_1032db60(sub_1031e920(a1));
        g_1038b040(0, 64, v20);
        sub_10314590(a0, sub_1032e2e0(0));
        v6 |= 1;
        v12 = 0;
        sub_1032e280(0);
        v22 = a0;
    }
    else
    {
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v23 = sub_1032db60(sub_1031e920(a1));
        v7 = g_1038b040(65001, 0, v23);
        sub_10333ef0(v7 + 1, 0);
        v12 = 2;
        v0 = sub_1032e2e0(0, v7 + 1, 0, 0);
        v24 = sub_1032db60(sub_1031e920(a1));
        g_1038b040(65001, 0, v24);
        sub_10314590(a0, sub_1032e2e0(0));
        v6 |= 1;
        v12 = 0;
        sub_1032e280(0);
        v22 = a0;
    }
    v26 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int *)v26) = v10;
    return v22;
}
```

## `sub_10327f50` `0x10327f50`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10327f50(void)
{
}
```

## `sub_10328010` `0x10328010`

_382 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b104;
extern unsigned int g_1038e180;

unsigned int sub_10328010(unsigned int a0, unsigned int a1)
{
    unsigned long v13;  // ldt
    unsigned long v14;  // gdt
    unsigned int v23;  // eax
    unsigned long v25;  // 4113
    unsigned short v15;  // fs
    unsigned long v16;  // 4135
    unsigned long v17;  // 4149
    unsigned int v18;  // eax
    unsigned int v19;  // eax
    unsigned int v21;  // eax
    unsigned int v22;  // eax
    int v0;  // [bp-0x70]
    unsigned int v1;  // [bp-0x6c]
    int v2;  // [bp-0x4c]
    unsigned int v3;  // [bp-0x48]
    unsigned int v4;  // [bp-0x44]
    unsigned int v5;  // [bp-0x40]
    unsigned int v6;  // [bp-0x3c]
    int v7;  // [bp-0x28]
    int v8;  // [bp-0x14]
    unsigned int v9;  // [bp-0x10]
    unsigned int v10;  // [bp-0xc]
    char v11;  // [bp-0x8], Other Possible Types: unsigned int
    char v12;  // [bp-0x4]

    v11 = 4294967295;
    v10 = sub_1036c216;
    v16 = _ccall(v13, v14, (unsigned int)v15, 0);
    v9 = *((int *)v16);
    v5 = g_1038e180 ^ &v12;
    v17 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int **)v17) = &v9;
    v6 = 0;
    if (sub_10327cb0())
    {
        v4 = 0;
        v3 = 0;
        v2 = sub_1031e920(a1);
        v18 = (unsigned int)sub_102ec980(a1);
        v8 = g_1038b104(0, 0, v18);
        sub_10333f40(v8 + 1, 0);
        v11 = 1;
        v1 = sub_1032e410(0, v8 + 1);
        v0 = sub_1031e920(a1);
        v19 = (unsigned int)sub_102ec980(a1);
        g_1038b104(0, 0, v19);
        sub_1031fc10(a0, sub_1032e410(0));
        v6 |= 1;
        v11 = 0;
        sub_1032e3f0(0);
        v21 = a0;
    }
    else
    {
        v4 = 0;
        v3 = 0;
        v2 = sub_1031e920(a1);
        v22 = (unsigned int)sub_102ec980(a1);
        v7 = g_1038b104(65001, 0, v22);
        sub_10333f40(v7 + 1, 0);
        v11 = 2;
        v1 = sub_1032e410(0, v7 + 1);
        v0 = sub_1031e920(a1);
        v23 = (unsigned int)sub_102ec980(a1);
        g_1038b104(65001, 0, v23);
        sub_1031fc10(a0, sub_1032e410(0));
        v6 |= 1;
        v11 = 0;
        sub_1032e3f0(0);
        v21 = a0;
    }
    v25 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int *)v25) = v9;
    return v21;
}
```

## `sub_103280e5` `0x103280e5`

_5 bytes. (leaf/helper — see body)_

```c
void sub_103280e5(void)
{
}
```

## `sub_103281a0` `0x103281a0`

_327 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103a2a8c;

unsigned int sub_103281a0(int a0)
{
    unsigned long v15;  // ldt
    unsigned long v16;  // gdt
    unsigned short v17;  // fs
    unsigned long v18;  // 4138
    unsigned long v19;  // 4152
    unsigned int v20;  // eax
    unsigned int v21;  // edx
    unsigned long v22;  // 4113
    int v0;  // [bp-0x128]
    int v1;  // [bp-0x124]
    int v2;  // [bp-0x120]
    int v3;  // [bp-0x11c]
    char v4;  // [bp-0x118]
    char v5;  // [bp-0xfc]
    char v6;  // [bp-0x9c]
    unsigned int v7;  // [bp-0x80]
    unsigned int v8;  // [bp-0x7c]
    char v9;  // [bp-0x74]
    char v10;  // [bp-0x11]
    unsigned int v11;  // [bp-0x10]
    unsigned int v12;  // [bp-0xc]
    char v13;  // [bp-0x8], Other Possible Types: unsigned int
    char v14;  // [bp-0x4]

    v13 = 4294967295;
    v12 = sub_1036c25a;
    v18 = _ccall(v15, v16, (unsigned int)v17, 0);
    v11 = *((int *)v18);
    v19 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int **)v19) = &v11;
    sub_1032d6d0(a0, g_1038e180 ^ &v14);
    v13 = 0;
    v10 = sub_103282f0(&v9);
    v13 = 4294967295;
    sub_10319f00(&v9);
    if (!v10)
    {
        v20 = 0;
    }
    else if (g_103a2a8c)
    {
        v20 = sub_1032d6b0(a0);
    }
    else
    {
        v3 = sub_1032d6d0(a0, &v4);
        v2 = v3;
        v13 = 1;
        v1 = sub_10326a70(v2, a0);
        v0 = v1;
        v13 = 2;
        sub_1032db80(v0);
        v13 = 3;
        v7 = sub_1032d690(&v6);
        v8 = v21;
        v13 = 2;
        sub_1032dbe0();
        v13 = 1;
        sub_10314610(&v4);
        v13 = 4294967295;
        sub_10319f00(&v5);
        v20 = v7;
    }
    v22 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int *)v22) = v11;
    return v20;
}
```

## `sub_10328221` `0x10328221`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10328221(void)
{
    sub_103282d9();
    return;
}
```

## `sub_103282d9` `0x103282d9`

_2 bytes. (leaf/helper — see body)_

```c
void sub_103282d9(void)
{
}
```

## `sub_103282f0` `0x103282f0`

_286 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103a2a8c;

char sub_103282f0(int a0)
{
    unsigned long v19;  // ldt
    unsigned long v20;  // gdt
    unsigned long v29;  // 4119
    unsigned short v21;  // fs
    unsigned long v22;  // 4189
    unsigned int v23;  // ecx
    unsigned int v24;  // ebx
    unsigned int v25;  // esi
    unsigned int v26;  // edi
    unsigned long v27;  // 4193
    char v28;  // al
    unsigned int v0;  // [bp-0xb0]
    unsigned int v1;  // [bp-0xac]
    unsigned int v2;  // [bp-0xa8]
    unsigned int v3;  // [bp-0xa4]
    int v4;  // [bp-0xa0]
    int v5;  // [bp-0x9c]
    unsigned int v6;  // [bp-0x98]
    unsigned int v7;  // [bp-0x94]
    char v8;  // [bp-0x8c]
    char v9;  // [bp-0x70]
    char v10;  // [bp-0x51]
    char v11;  // [bp-0x50]
    char v12;  // [bp-0x34]
    char v13;  // [bp-0x15]
    char *v14;  // [bp-0x14], Other Possible Types: unsigned int
    unsigned int v15;  // [bp-0x10]
    unsigned int v16;  // [bp-0xc]
    unsigned int v17;  // [bp-0x8], Other Possible Types: char
    char v18;  // [bp-0x4]

    v17 = 4294967295;
    v16 = sub_1036c29b;
    v22 = _ccall(v19, v20, (unsigned int)v21, 0);
    v15 = *((int *)v22);
    v14 = v23;
    v3 = v24;
    v2 = v25;
    v1 = v26;
    v0 = g_1038e180 ^ &v18;
    v27 = _ccall(v19, v20, (unsigned int)v21, 0);
    *((unsigned int **)v27) = &v15;
    v14 = &v0;
    v17 = 0;
    if (g_103a2a8c)
    {
        v7 = sub_10326c30(a0, &v11);
        v6 = v7;
        v17 = 1;
        sub_10325740(&v12, v6);
        v17 = 2;
        v13 = sub_1032d790(&v12);
        v17 = 1;
        sub_103257d0(&v12);
        v17 = 0;
        sub_1031a3a0(&v11);
        v28 = v13;
    }
    else
    {
        v5 = sub_10326a70(a0, &v8);
        v4 = v5;
        v17 = 3;
        sub_1032db80(v4);
        v17 = 4;
        v10 = sub_1032d770(&v9);
        v17 = 3;
        sub_1032dbe0();
        v17 = 0;
        sub_10314610(&v8);
        v28 = v10;
    }
    v29 = _ccall(v19, v20, (unsigned int)v21, 0);
    *((unsigned int *)v29) = v15;
    return v28;
}
```

## `sub_10328395` `0x10328395`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10328395(void)
{
    sub_103283fe();
    return;
}
```

## `sub_103283fe` `0x103283fe`

_2 bytes. (leaf/helper — see body)_

```c
void sub_103283fe(void)
{
    sub_1032841a();
    return;
}
```

## `sub_10328400` `0x10328400`

_20 bytes. (leaf/helper — see body)_

```c
int sub_10328400(void)
{
    char v1;  // [bp+0xfff7b]
    unsigned int v2;  // [bp+0x100000]

    v1 = 0;
    v2 = 4294967295;
    return sub_10328423;
}
```

## `sub_10328414` `0x10328414`

_6 bytes. (leaf/helper — see body)_

```c
int sub_10328414(void)
{
    return sub_1032841a;
}
```

## `sub_1032841a` `0x1032841a`

_9 bytes. (leaf/helper — see body)_

```c
void sub_1032841a(void)
{
    unsigned int v1;  // [bp+0x100000]

    v1 = 4294967295;
}
```

## `sub_10328423` `0x10328423`

_6 bytes. (leaf/helper — see body)_

```c
char sub_10328423(void)
{
}
```

## `sub_10328440` `0x10328440`

_433 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103a2a8c;

int sub_10328440(int a0)
{
    unsigned long v20;  // ldt
    unsigned long v21;  // gdt
    unsigned short v22;  // fs
    unsigned long v23;  // 4172
    unsigned long v24;  // 4176
    int v25;  // eax
    unsigned long v26;  // 4113
    unsigned int v0;  // [bp-0x150]
    int v1;  // [bp-0x14c]
    int v2;  // [bp-0x148]
    int v3;  // [bp-0x144]
    int v4;  // [bp-0x140]
    int v5;  // [bp-0x13c]
    int v6;  // [bp-0x138]
    int v7;  // [bp-0x134]
    int v8;  // [bp-0x130]
    unsigned int v9;  // [bp-0x12c]
    char v10;  // [bp-0x128]
    char v11;  // [bp-0x10c]
    char v12;  // [bp-0xf0]
    char v13;  // [bp-0x90]
    char v14;  // [bp-0x74]
    unsigned int v15;  // [bp-0x10]
    unsigned int v16;  // [bp-0xc]
    unsigned int v17;  // [bp-0x8], Other Possible Types: char
    char v18;  // [bp-0x4]
    char v19;  // [bp+0x8]

    v17 = 4294967295;
    v16 = sub_1036c314;
    v23 = _ccall(v20, v21, (unsigned int)v22, 0);
    v15 = *((int *)v23);
    v0 = g_1038e180 ^ &v18;
    v24 = _ccall(v20, v21, (unsigned int)v22, 0);
    *((unsigned int **)v24) = &v15;
    v9 = 0;
    v17 = 1;
    if (g_103a2a8c)
    {
        sub_1032d810(a0, &v19);
        v9 |= 1;
        v17 = 0;
        sub_103257d0(&v19);
        v25 = a0;
    }
    else
    {
        v8 = sub_1032d6d0(&v19, &v11);
        v7 = v8;
        v17 = 2;
        v6 = sub_10326a70(v7, &v19);
        v5 = v6;
        v17 = 3;
        sub_1032db80(v5);
        v17 = 4;
        v4 = sub_1032d7b0(&v10, &v13, a0);
        v3 = v4;
        v17 = 5;
        v2 = sub_1032d870(v3);
        v1 = v2;
        v17 = 6;
        sub_10326df0(v1, v3);
        v9 |= 1;
        v17 = 5;
        sub_10319f00(&v14);
        v17 = 4;
        sub_1032dbe0();
        v17 = 3;
        sub_1032dbe0();
        v17 = 2;
        sub_10314610(&v11);
        v17 = 1;
        sub_10319f00(&v12);
        v17 = 0;
        sub_103257d0(&v19);
        v25 = a0;
    }
    v26 = _ccall(v20, v21, (unsigned int)v22, 0);
    *((unsigned int *)v26) = v15;
    return v25;
}
```

## `sub_103284b7` `0x103284b7`

_5 bytes. (leaf/helper — see body)_

```c
void sub_103284b7(void)
{
    sub_103285e7();
    return;
}
```

## `sub_103285e7` `0x103285e7`

_12 bytes. (leaf/helper — see body)_

```c
void sub_103285e7(void)
{
    char v1;  // [bp+0x100000]

    v1 = 0;
    sub_103257d0(/* unsupported instruction */ + 12);
}
```

## `sub_10328610` `0x10328610`

_202 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10328610(int a0, unsigned int a1)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4141
    int v11;  // eax
    unsigned long v12;  // 4158
    int v13;  // eax
    unsigned long v15;  // 4118
    unsigned int v0;  // [bp-0x54]
    char v1;  // [bp-0x50]
    int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char v5;  // [bp-0x8], Other Possible Types: unsigned int
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036c35b;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v11 = g_1038e180 ^ &v6;
    v2 = v11;
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v12) = &v3;
    v13 = sub_1032bc60(&v1, 0, v11);
    v5 = 1;
    sub_1032db80(sub_1032e0e0(v11, v13, v13, 0));
    v5 = 3;
    sub_1031a040(&v1);
    sub_1032dc50();
    if (!(char)sub_10325be0(a1))
        sub_1032dc30(a1);
    sub_10332ce0(a0);
    v0 = 1;
    v5 = 0;
    sub_1032dbe0(a0);
    v15 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v15) = v3;
    return sub_10351225();
}
```

## `sub_103286e0` `0x103286e0`

_238 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1dc;
extern unsigned int g_1038e180;
extern int g_10390370;

unsigned int sub_103286e0(unsigned int a0, int a1)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4140
    unsigned long v13;  // 4154
    unsigned int v14;  // eax
    unsigned int v15;  // eax
    unsigned long v16;  // 4113
    unsigned int v0;  // [bp-0x60]
    int v1;  // [bp-0x48]
    int v2;  // [bp-0x44]
    unsigned int v3;  // [bp-0x40]
    char v4;  // [bp-0x3c]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8], Other Possible Types: char
    char v8;  // [bp-0x4]

    v7 = 4294967295;
    v6 = sub_1036c3a9;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v5 = *((int *)v12);
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v5;
    v3 = 0;
    sub_10333ef0(260, 0, g_1038e180 ^ &v8);
    v7 = 1;
    v0 = sub_1032e2e0(0, 260);
    v14 = (unsigned int)sub_102ec9a0(a1);
    if (g_1038b1dc(v14))
    {
        v2 = sub_10314590(&v4, sub_1032e2e0(0));
        v1 = v2;
        v7 = 2;
        sub_1032e020(v1);
        v3 |= 1;
        v7 = 1;
        sub_10314610(&v4);
        v7 = 0;
        sub_1032e280();
        v15 = a0;
    }
    else
    {
        sub_1032dfc0(g_10390370);
        v3 |= 1;
        v7 = 0;
        sub_1032e280(g_10390370);
        v15 = a0;
    }
    v16 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v16) = v5;
    return v15;
}
```

## `sub_10328797` `0x10328797`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10328797(void)
{
    sub_103287c1();
    return;
}
```

## `sub_103287c1` `0x103287c1`

_12 bytes. (leaf/helper — see body)_

```c
void sub_103287c1(void)
{
    char v1;  // [bp+0x100000]

    v1 = 0;
    sub_1032e280();
}
```

## `sub_103287e0` `0x103287e0`

_643 bytes. refs "GetShortPathNameW"_

```c
extern unsigned int g_1038e180;
extern int g_10390370;
extern unsigned int g_103a297c;
extern int g_103a2aac;

int sub_103287e0(int a0, unsigned int a1)
{
    unsigned long v24;  // ldt
    unsigned long v25;  // gdt
    unsigned short v26;  // fs
    unsigned long v27;  // 4168
    unsigned long v28;  // 4172
    unsigned int v29;  // eax
    int v30;  // eax
    unsigned long v31;  // 4113
    unsigned int v0;  // [bp-0x1a4]
    char *v1;  // [bp-0x190]
    unsigned int v2;  // [bp-0x184]
    int v3;  // [bp-0x180]
    int v4;  // [bp-0x17c]
    unsigned int v5;  // [bp-0x178]
    unsigned int v6;  // [bp-0x174]
    int v7;  // [bp-0x170]
    int v8;  // [bp-0x16c]
    int v9;  // [bp-0x168]
    int v10;  // [bp-0x164]
    int v11;  // [bp-0x160]
    int v12;  // [bp-0x15c]
    unsigned int v13;  // [bp-0x158]
    char v14;  // [bp-0x154]
    char v15;  // [bp-0x134]
    char v16;  // [bp-0x118]
    char v17;  // [bp-0xb8]
    char v18;  // [bp-0x58]
    char v19;  // [bp-0x3c]
    unsigned int v20;  // [bp-0x10]
    unsigned int v21;  // [bp-0xc]
    unsigned int v22;  // [bp-0x8], Other Possible Types: char
    char v23;  // [bp-0x4]

    v22 = 4294967295;
    v21 = sub_1036c435;
    v27 = _ccall(v24, v25, (unsigned int)v26, 0);
    v20 = *((int *)v27);
    v2 = g_1038e180 ^ &v23;
    v28 = _ccall(v24, v25, (unsigned int)v26, 0);
    *((unsigned int **)v28) = &v20;
    v13 = 0;
    if (!((char)g_103a297c & 1))
    {
        g_103a297c = g_103a297c | 1;
        v22 = 1;
        sub_10314590(&v19, "GetShortPathNameW");
        v22 = 2;
        v1 = &v19;
        sub_1032e540(&v19, &g_103a2aac, 1);
        v22 = 1;
        sub_10314610(&v19);
        v22 = 0;
    }
    if ((char)sub_1032e630(v1))
    {
        sub_10333f40(260, 0);
        v22 = 3;
        v0 = sub_1032e410(0, 260);
        v29 = sub_1031fc50(a1);
        if (sub_1032eae0(v29))
        {
            v12 = sub_1031fc10(&v18, sub_1032e410(0));
            v11 = v12;
            v22 = 4;
            sub_10325880(a0, v11);
            v13 |= 1;
            v22 = 3;
            sub_1031a3a0(&v18);
            v22 = 0;
            sub_1032e3f0();
            v30 = a0;
        }
        else
        {
            sub_10325820(a0, g_10390370);
            v13 |= 1;
            v22 = 0;
            sub_1032e3f0(v29);
            v30 = a0;
        }
    }
    else
    {
        v10 = sub_1031e1d0(&v16, a1);
        v9 = v10;
        v22 = 5;
        v8 = sub_10326a70(v9, &v15);
        v7 = v8;
        v22 = 6;
        v6 = sub_103286e0(&v14, v7);
        v5 = v6;
        v22 = 7;
        v4 = sub_10326840(&v17, v5);
        v3 = v4;
        v22 = 8;
        sub_10327230(v3, a0);
        v13 |= 1;
        v22 = 7;
        sub_10319f00(&v17);
        v22 = 6;
        sub_1031a040(&v14);
        v22 = 5;
        sub_10314610(&v15);
        v22 = 0;
        sub_10319f00(&v16);
        v30 = a0;
    }
    v31 = _ccall(v24, v25, (unsigned int)v26, 0);
    *((unsigned int *)v31) = v20;
    return v30;
}
```

## `sub_10328953` `0x10328953`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10328953(void)
{
}
```

## `sub_10328a70` `0x10328a70`

_258 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b108;
extern unsigned int g_1038e180;
extern int g_10390370;

unsigned int sub_10328a70(unsigned int a0, int a1, int a2, int a3)
{
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    unsigned short v14;  // fs
    unsigned long v15;  // 4140
    unsigned long v16;  // 4154
    int v17;  // eax
    unsigned int v18;  // eax
    unsigned long v19;  // 4113
    int v0;  // [bp-0x6c]
    int v1;  // [bp-0x68]
    unsigned int v2;  // [bp-0x64]
    unsigned int v3;  // [bp-0x60]
    int v4;  // [bp-0x48]
    int v5;  // [bp-0x44]
    unsigned int v6;  // [bp-0x40]
    char v7;  // [bp-0x3c]
    unsigned int v8;  // [bp-0x10]
    unsigned int v9;  // [bp-0xc]
    unsigned int v10;  // [bp-0x8], Other Possible Types: char
    char v11;  // [bp-0x4]

    v10 = 4294967295;
    v9 = sub_1036c47c;
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    v8 = *((int *)v15);
    v16 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v16) = &v8;
    v6 = 0;
    sub_10333ef0(260, 0, g_1038e180 ^ &v11);
    v10 = 1;
    v3 = sub_1032e2e0(0, 0);
    v2 = 260;
    v1 = sub_10326e70(a3);
    v0 = sub_10326e70(a2);
    v17 = sub_10326e70(a1);
    if (g_1038b108(v17))
    {
        v5 = sub_10314590(&v7, sub_1032e2e0(0));
        v4 = v5;
        v10 = 2;
        sub_1032e020(v4);
        v6 |= 1;
        v10 = 1;
        sub_10314610(&v7);
        v10 = 0;
        sub_1032e280();
        v18 = a0;
    }
    else
    {
        sub_1032dfc0(g_10390370);
        v6 |= 1;
        v10 = 0;
        sub_1032e280(g_10390370);
        v18 = a0;
    }
    v19 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int *)v19) = v8;
    return v18;
}
```

## `sub_10328b3b` `0x10328b3b`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10328b3b(void)
{
    sub_10328b65();
    return;
}
```

## `sub_10328b65` `0x10328b65`

_12 bytes. (leaf/helper — see body)_

```c
void sub_10328b65(void)
{
    char v1;  // [bp+0x100000]

    v1 = 0;
    sub_1032e280();
}
```

## `sub_10328b80` `0x10328b80`

_561 bytes. refs "SearchPathW"_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

extern unsigned int g_1038e180;
extern int g_10390370;
extern unsigned int g_103a2984;
extern int g_103a2aac;

int sub_10328b80(int a0, int a1, int a2, int a3)
{
    unsigned long v21;  // ldt
    unsigned long v22;  // gdt
    unsigned short v23;  // fs
    unsigned long v24;  // 4168
    unsigned long v25;  // 4172
    unsigned int v26;  // eax
    int v27;  // eax
    unsigned long v28;  // 4113
    struct_0 *v0;  // [bp-0x124]
    struct_0 *v1;  // [bp-0x120]
    unsigned int v2;  // [bp-0x11c]
    unsigned int v3;  // [bp-0x118]
    char *v4;  // [bp-0x104]
    unsigned int v5;  // [bp-0xf8]
    int v6;  // [bp-0xf4]
    int v7;  // [bp-0xf0]
    unsigned int v8;  // [bp-0xec]
    unsigned int v9;  // [bp-0xe8]
    int v10;  // [bp-0xe4]
    int v11;  // [bp-0xe0]
    unsigned int v12;  // [bp-0xdc]
    char v13;  // [bp-0xd8]
    char v14;  // [bp-0xb8]
    char v15;  // [bp-0x58]
    char v16;  // [bp-0x3c]
    unsigned int v17;  // [bp-0x10]
    unsigned int v18;  // [bp-0xc]
    unsigned int v19;  // [bp-0x8], Other Possible Types: char
    char v20;  // [bp-0x4]

    v19 = 4294967295;
    v18 = sub_1036c4f2;
    v24 = _ccall(v21, v22, (unsigned int)v23, 0);
    v17 = *((int *)v24);
    v5 = g_1038e180 ^ &v20;
    v25 = _ccall(v21, v22, (unsigned int)v23, 0);
    *((unsigned int **)v25) = &v17;
    v12 = 0;
    if (!((char)g_103a2984 & 1))
    {
        g_103a2984 = g_103a2984 | 1;
        v19 = 1;
        sub_10314590(&v16, "SearchPathW");
        v19 = 2;
        v4 = &v16;
        sub_1032e570(&v16, &g_103a2aac, 1);
        v19 = 1;
        sub_10314610(&v16);
        v19 = 0;
    }
    if ((char)sub_1032e630(v4))
    {
        sub_10333f40(260, 0);
        v19 = 3;
        v3 = sub_1032e410(0, 0);
        v2 = 260;
        v1 = sub_10326fd0(a3);
        v0 = sub_10326fd0(a2);
        v26 = sub_10326fd0(a1);
        if (sub_1032e700(v26))
        {
            v11 = sub_1031fc10(&v15, sub_1032e410(0));
            v10 = v11;
            v19 = 4;
            sub_10325880(a0, v10);
            v12 |= 1;
            v19 = 3;
            sub_1031a3a0(&v15);
            v19 = 0;
            sub_1032e3f0();
            v27 = a0;
        }
        else
        {
            sub_10325820(a0, g_10390370);
            v12 |= 1;
            v19 = 0;
            sub_1032e3f0(v26);
            v27 = a0;
        }
    }
    else
    {
        v9 = sub_10328a70(&v13, a1, a2, a3);
        v8 = v9;
        v19 = 5;
        v7 = sub_10326840(&v14, v8);
        v6 = v7;
        v19 = 6;
        sub_10327230(v6, a0);
        v12 |= 1;
        v19 = 5;
        sub_10319f00(&v14);
        v19 = 0;
        sub_1031a040(&v13);
        v27 = a0;
    }
    v28 = _ccall(v21, v22, (unsigned int)v23, 0);
    *((unsigned int *)v28) = v17;
    return v27;
}
```

## `sub_10328d07` `0x10328d07`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10328d07(void)
{
}
```

## `sub_10328dc0` `0x10328dc0`

_146 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b10c;
extern unsigned int g_1038e180;

int sub_10328dc0(int a0)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4140
    unsigned long v9;  // 4154
    unsigned int v10;  // eax
    unsigned long v12;  // 4117
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    char v3;  // [bp-0x8], Other Possible Types: unsigned int
    char v4;  // [bp-0x4]

    v3 = 4294967295;
    v2 = sub_1036c531;
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v1 = *((int *)v8);
    v9 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v9) = &v1;
    sub_10333ef0(260, 0, g_1038e180 ^ &v4, 0);
    v3 = 1;
    v10 = sub_1032e2e0(0);
    g_1038b10c(260, v10);
    sub_10314590(a0, sub_1032e2e0(0));
    v0 = 1;
    v3 = 0;
    sub_1032e280(0);
    v12 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v12) = v1;
    return a0;
}
```

## `sub_10328e60` `0x10328e60`

_409 bytes. refs "GetTempPathW"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b110;
extern unsigned int g_1038e180;
extern unsigned int g_103a298c;
extern int g_103a2aac;

unsigned int sub_10328e60(unsigned int a0)
{
    unsigned long v14;  // ldt
    unsigned long v15;  // gdt
    unsigned short v16;  // fs
    unsigned long v17;  // 4168
    unsigned long v18;  // 4172
    unsigned int v19;  // eax
    unsigned int v21;  // eax
    unsigned long v22;  // 4113
    char *v0;  // [bp-0xdc]
    unsigned int v1;  // [bp-0xd0]
    int v2;  // [bp-0xcc]
    int v3;  // [bp-0xc8]
    int v4;  // [bp-0xc4]
    int v5;  // [bp-0xc0]
    unsigned int v6;  // [bp-0xbc]
    char v7;  // [bp-0xb8]
    char v8;  // [bp-0x9c]
    char v9;  // [bp-0x3c]
    unsigned int v10;  // [bp-0x10]
    unsigned int v11;  // [bp-0xc]
    unsigned int v12;  // [bp-0x8], Other Possible Types: char
    char v13;  // [bp-0x4]

    v12 = 4294967295;
    v11 = sub_1036c59f;
    v17 = _ccall(v14, v15, (unsigned int)v16, 0);
    v10 = *((int *)v17);
    v1 = g_1038e180 ^ &v13;
    v18 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int **)v18) = &v10;
    v6 = 0;
    if (!((char)g_103a298c & 1))
    {
        g_103a298c = g_103a298c | 1;
        v12 = 1;
        sub_10314590(&v9, "GetTempPathW");
        v12 = 2;
        v0 = &v9;
        sub_1032e5a0(&v9, &g_103a2aac, 1);
        v12 = 1;
        sub_10314610(&v9);
        v12 = 0;
    }
    if ((char)sub_1032e630(v0))
    {
        sub_10333f40(260, 0);
        v12 = 3;
        v19 = sub_1032e410(0);
        g_1038b110(260, v19);
        sub_1031fc10(a0, sub_1032e410(0));
        v6 |= 1;
        v12 = 0;
        sub_1032e3f0(0);
        v21 = a0;
    }
    else
    {
        v5 = sub_10328dc0(&v7);
        v4 = v5;
        v12 = 4;
        v3 = sub_10319e80(&v8, v4);
        v2 = v3;
        v12 = 5;
        sub_10326c30(v2, a0);
        v6 |= 1;
        v12 = 4;
        sub_10319f00(&v8);
        v12 = 0;
        sub_10314610(&v7);
        v21 = a0;
    }
    v22 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int *)v22) = v10;
    return v21;
}
```

## `sub_10328f5b` `0x10328f5b`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10328f5b(void)
{
}
```

## `sub_10329000` `0x10329000`

_163 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b114;
extern unsigned int g_1038e180;

int sub_10329000(int a0, int a1, int a2, unsigned int a3)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4140
    unsigned long v12;  // 4154
    int v13;  // eax
    unsigned long v15;  // 4117
    int v0;  // [bp-0x40]
    unsigned int v1;  // [bp-0x3c]
    unsigned int v2;  // [bp-0x38]
    unsigned int v3;  // [bp-0x24]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    char v6;  // [bp-0x8], Other Possible Types: unsigned int
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036c5de;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    sub_10333ef0(260, 0, g_1038e180 ^ &v7, 0);
    v6 = 1;
    v2 = sub_1032e2e0(0);
    v1 = a3;
    v0 = sub_10326e70(a2);
    v13 = sub_10326e70(a1);
    g_1038b114(v13);
    sub_10314590(a0, sub_1032e2e0(0));
    v3 = 1;
    v6 = 0;
    sub_1032e280(0);
    v15 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v15) = v4;
    return a0;
}
```

## `sub_103290b0` `0x103290b0`

_472 bytes. refs "GetTempFileNameW"_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

extern struct_0 *g_1038b118;
extern unsigned int g_1038e180;
extern unsigned int g_103a2994;
extern int g_103a2aac;

unsigned int sub_103290b0(unsigned int a0, int a1, int a2, unsigned int a3)
{
    unsigned long v17;  // ldt
    unsigned long v18;  // gdt
    unsigned short v19;  // fs
    unsigned long v20;  // 4168
    unsigned long v21;  // 4172
    struct_0 *v22;  // eax
    unsigned int v24;  // eax
    unsigned long v25;  // 4113
    struct_0 *v0;  // [bp-0xf4]
    unsigned int v1;  // [bp-0xf0]
    unsigned int v2;  // [bp-0xec]
    char *v3;  // [bp-0xdc]
    unsigned int v4;  // [bp-0xd0]
    int v5;  // [bp-0xcc]
    int v6;  // [bp-0xc8]
    int v7;  // [bp-0xc4]
    int v8;  // [bp-0xc0]
    unsigned int v9;  // [bp-0xbc]
    char v10;  // [bp-0xb8]
    char v11;  // [bp-0x9c]
    char v12;  // [bp-0x3c]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8], Other Possible Types: char
    char v16;  // [bp-0x4]

    v15 = 4294967295;
    v14 = sub_1036c64c;
    v20 = _ccall(v17, v18, (unsigned int)v19, 0);
    v13 = *((int *)v20);
    v4 = g_1038e180 ^ &v16;
    v21 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((unsigned int **)v21) = &v13;
    v9 = 0;
    if (!((char)g_103a2994 & 1))
    {
        g_103a2994 = g_103a2994 | 1;
        v15 = 1;
        sub_10314590(&v12, "GetTempFileNameW");
        v15 = 2;
        v3 = &v12;
        sub_1032e5d0(&v12, &g_103a2aac, 1);
        v15 = 1;
        sub_10314610(&v12);
        v15 = 0;
    }
    if ((char)sub_1032e630(v3) && ((char)sub_10327630(a1) || (char)sub_10327630(a2)))
    {
        sub_10333f40(260, 0);
        v15 = 3;
        v2 = sub_1032e410(0);
        v1 = a3;
        v0 = sub_10326fd0(a2);
        v22 = sub_10326fd0(a1);
        g_1038b118(v22);
        sub_1031fc10(a0, sub_1032e410(0));
        v9 |= 1;
        v15 = 0;
        sub_1032e3f0(0);
        v24 = a0;
    }
    else
    {
        v8 = sub_10329000(&v10, a1, a2, a3);
        v7 = v8;
        v15 = 4;
        v6 = sub_10319e80(&v11, v7);
        v5 = v6;
        v15 = 5;
        sub_10326c30(v5, a0);
        v9 |= 1;
        v15 = 4;
        sub_10319f00(&v11);
        v15 = 0;
        sub_10314610(&v10);
        v24 = a0;
    }
    v25 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((unsigned int *)v25) = v13;
    return v24;
}
```

## `sub_103291de` `0x103291de`

_5 bytes. (leaf/helper — see body)_

```c
void sub_103291de(void)
{
}
```

