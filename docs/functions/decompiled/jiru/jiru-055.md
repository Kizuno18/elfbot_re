# elfbot.dll decompiled — jiru 0x103475c0..0x1034a230

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_103475c0` `0x103475c0`

_68 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
    unsigned int field_4;
    struct struct_1 *field_8;
    char padding_c[20];
    struct struct_0 *field_20;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

struct_0 * sub_103475c0(struct_0 *a0, unsigned int a1)
{
    struct_0 *v1;  // eax
    struct_0 *i;  // [bp-0x8]

    v1 = a0;
    for (i = v1->field_20; i; i = i->field_0)
    {
        i->field_8(a1, a0, i->field_4);
        v1 = i->field_0;
    }
    return v1;
}
```

## `sub_10347610` `0x10347610`

_154 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

typedef struct struct_2 {
    struct struct_0 *field_0;
    char padding_4[52];
    void* field_38;
} struct_2;

typedef struct struct_0 {
    char padding_0[52];
    struct struct_1 *field_34;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern unsigned int g_1038e180;

struct_0 ** sub_10347610(struct_2 *a0, struct_0 **a1, unsigned int a2)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4141
    unsigned long v11;  // 4155
    unsigned long v12;  // 4117
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x18]
    char v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char v5;  // [bp-0x8], Other Possible Types: unsigned int
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_10371191;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v0 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    v1 = 0;
    sub_10314db0(&v2, a0->field_38);
    v5 = 1;
    a0->field_0->field_34(a2);
    sub_10347550(a0->field_38, a2);
    sub_10314db0(a1, &v2);
    v1 |= 1;
    v5 = 0;
    sub_103130c0(&v2);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v3;
    return a1;
}
```

## `sub_103476b0` `0x103476b0`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_103476b0(unsigned int a0, int a1)
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
    sub_1034a370(a1, g_1038e180 ^ &v2, 0, v8, sub_103711c9, -1, &v3);
    v11 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v11) = v8;
    return a0;
}
```

## `sub_10347710` `0x10347710`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10347710(unsigned int a0, int a1)
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
    sub_1034a3f0(a1, g_1038e180 ^ &v2, 0, v8, sub_10371209, -1, &v3);
    v11 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v11) = v8;
    return a0;
}
```

## `sub_10347770` `0x10347770`

_19 bytes. (leaf/helper — see body)_

```c
int sub_10347770(unsigned int a0, int *a1)
{
    char v0;  // [bp+0x0]

    return sub_1034a090(*(a1), &v0);
}
```

## `sub_10347790` `0x10347790`

_147 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[40];
    struct struct_1 *field_28;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_10347790(struct_0 **a0)
{
    unsigned int v0[6];  // [bp-0x8c]
    unsigned int v1;  // [bp-0x74]
    unsigned int v2[6];  // [bp-0x6c]
    unsigned int v3;  // [bp-0x54]
    char v4;  // [bp-0x4c]
    char v5;  // [bp-0x2c]
    int v6;  // [bp-0xc]
    int v7;  // [bp-0x8]

    v7 = sub_103131c0(a0);
    v6 = sub_1033e670(a0);
    if (v7 && v7 != v6)
    {
        v3 = 2;
        sub_10313310(v2, 0);
        *(a0)->field_28(&v5);
    }
    v7 = sub_103131a0(a0);
    v6 = sub_1033e650(a0);
    if (!v7)
    {
        return v6;
    }
    else if (v7 != v6)
    {
        v1 = 1;
        sub_10313310(v0, 0);
        return *(a0)->field_28(&v4);
    }
    else
    {
        return v7;
    }
}
```

## `sub_10347830` `0x10347830`

_45 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_10347830(unsigned int *a0, unsigned int *a1)
{
    unsigned int *v0;  // [bp-0xc]
    unsigned int *v1;  // [bp-0x8]

    v0 = (*(a1) < *(a0) ? a1 : a0);
    v1 = v0;
    return v1;
}
```

## `sub_10347860` `0x10347860`

_292 bytes. (leaf/helper — see body)_

```c
int sub_10347860(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, char a4, unsigned int a5, char a6, char a7)
{
    unsigned int v3;  // eax
    unsigned int v4;  // eax
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    int v2;  // [bp-0x8]

    sub_10343540(a0, 0);
    if (a3 > 0 && a3 > a2)
    {
        v1 = a3 - a2 - -(-(0 < a6));
        v2 = 0;
        v0 = 0;
        sub_1031bf00(a0, a3);
        v3 = a7;
        if (v3)
        {
            v3 = &v1;
            v2 = v3;
            v0 = v1 - v2;
        }
        else if (((char)a5 & 64))
        {
            v3 = v1;
            v2 = v3;
        }
        else
        {
            v0 = v1;
        }
        if (v0)
            v3 = sub_103170f0(a0, v0, a4);
        if (a6)
            v3 = sub_103170f0(a0, 1, a6);
        if (a2)
            v3 = sub_1031a6b0(a0, a1, a2);
        if (!v2)
            return v3;
        sub_103170f0(a0, v2, a4);
        return v3;
    }
    v4 = sub_1031bf00(a0, -(-(0 < a6)) + a2);
    if (a6)
        v4 = sub_103170f0(a0, 1, a6);
    if (a2)
        v4 = sub_1031a6b0(a0, a1, a2);
    return v4;
}
```

## `sub_10347990` `0x10347990`

_21 bytes. (leaf/helper — see body)_

```c
int sub_10347990(int a0, int a1)
{
    char v0;  // [bp+0x0]

    return sub_103479b0(a0, a1, &v0);
}
```

## `sub_103479b0` `0x103479b0`

_586 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern unsigned int g_1038e180;

struct_0 ** sub_103479b0(struct_0 **a0, int a1)
{
    unsigned long v20;  // ldt
    unsigned long v21;  // gdt
    unsigned short v22;  // fs
    unsigned long v23;  // 4147
    unsigned int v24;  // ecx
    unsigned int v25;  // ebx
    unsigned int v26;  // esi
    unsigned int v27;  // edi
    unsigned long v28;  // 4169
    unsigned long v29;  // 4123
    int v0;  // [bp-0x64]
    int v1;  // [bp-0x58]
    unsigned int v2;  // [bp-0x50]
    unsigned int v3;  // [bp-0x4c]
    unsigned int v4;  // [bp-0x48]
    unsigned int v5;  // [bp-0x44]
    int v6;  // [bp-0x40]
    unsigned int v7;  // [bp-0x38]
    unsigned int v8;  // [bp-0x34]
    unsigned int v9;  // [bp-0x30]
    unsigned int v10;  // [bp-0x2c]
    struct_0 v11;  // [bp-0x28]
    int iter;  // [bp-0x20]
    int v13;  // [bp-0x1c]
    unsigned int v14;  // [bp-0x18]
    char *v15;  // [bp-0x14], Other Possible Types: unsigned int
    unsigned int v16;  // [bp-0x10]
    unsigned int v17;  // [bp-0xc]
    char v18;  // [bp-0x8], Other Possible Types: unsigned int
    char v19;  // [bp-0x4]

    v18 = 4294967295;
    v17 = sub_10371238;
    v23 = _ccall(v20, v21, (unsigned int)v22, 0);
    v16 = *((int *)v23);
    v15 = v24;
    v5 = v25;
    v4 = v26;
    v3 = v27;
    v2 = g_1038e180 ^ &v19;
    v28 = _ccall(v20, v21, (unsigned int)v22, 0);
    *((unsigned int **)v28) = &v16;
    v15 = &v2;
    v14 = 0;
    v13 = sub_103136c0(a1);
    if (sub_103451d0((char *)a0 + *(a0)->field_4) > 0 && sub_103451d0((char *)a0 + *(a0)->field_4) > v13)
        v6 = sub_103451d0((char *)a0 + *(a0)->field_4) - v13;
    else
        v6 = 0;
    iter = v6;
    sub_103454a0(&v11, a0);
    v18 = 0;
    if (!(char)sub_103455c0(&v11))
    {
        v14 |= 4;
    }
    else
    {
        if (((short)sub_10315ef0((char *)a0 + *(a0)->field_4) & 448) != 64)
        {
            for (v18 = 1; iter > 0; iter -= 1)
            {
                v1 = sub_10345220((char *)a0 + *(a0)->field_4);
                v10 = sub_1033ed20(sub_10315c20((char *)a0 + *(a0)->field_4));
                v9 = sub_1032fd20();
                if ((char)sub_10312db0(&v9, &v10))
                {
                    v14 |= 4;
                    break;
                }
            }
        }
        if (!v14)
        {
            sub_10315c20((char *)a0 + *(a0)->field_4);
            if (sub_10347c20(a1, v13) != v13)
                v14 |= 4;
        }
        if (!v14)
        {
            for (; iter > 0; iter -= 1)
            {
                v0 = sub_10345220((char *)a0 + *(a0)->field_4);
                v8 = sub_1033ed20(sub_10315c20((char *)a0 + *(a0)->field_4));
                v7 = sub_1032fd20();
                if ((char)sub_10312db0(&v7, &v8))
                {
                    v14 |= 4;
                    break;
                }
            }
        }
        sub_103451f0((char *)a0 + *(a0)->field_4, 0);
        v18 = 0;
    }
    sub_10314630((char *)a0 + *(a0)->field_4, v14, 0);
    v18 = 4294967295;
    sub_10345550(&v11);
    v29 = _ccall(v20, v21, (unsigned int)v22, 0);
    *((unsigned int *)v29) = v16;
    return a0;
}
```

## `sub_10347bb3` `0x10347bb3`

_35 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

int sub_10347bb3(void)
{
    unsigned int v1;  // [bp+0x100000]
    struct_0 **v2;  // [bp+0x10000c]

    sub_10314630((char *)v2 + *(v2)->field_4, 4, 1);
    v1 = 0;
    return "j";
}
```

## `sub_10347c20` `0x10347c20`

_34 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[32];
    struct struct_1 *field_20;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_10347c20(struct_0 **a0, unsigned int a1, unsigned int a2)
{
    struct_0 **v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return *(a0)->field_20(a1, a2, a0, &v1);
}
```

## `sub_10347c50` `0x10347c50`

_20 bytes. (leaf/helper — see body)_

```c
int sub_10347c50(unsigned int a0, unsigned short *a1)
{
    int v1;  // ecx
    char v0;  // [bp+0x0]

    v1 = _INSERT(0, 0, *(a1));
    return sub_10347c70(v1, &v0);
}
```

## `sub_10347c70` `0x10347c70`

_371 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern unsigned int g_1038e180;

struct_0 ** sub_10347c70(struct_0 **a0, unsigned short a1)
{
    unsigned long v20;  // ldt
    unsigned long v21;  // gdt
    unsigned short v22;  // fs
    unsigned long v23;  // 4149
    unsigned int v24;  // ebx
    unsigned int v25;  // esi
    unsigned int v26;  // edi
    unsigned long v27;  // 4171
    int v28[3];  // eax
    unsigned long v29;  // 4123
    unsigned int v0;  // [bp-0x70]
    int v1;  // [bp-0x6c]
    unsigned int v2;  // [bp-0x68]
    unsigned int v3;  // [bp-0x64]
    unsigned int v4;  // [bp-0x60]
    unsigned int v5;  // [bp-0x5c]
    unsigned int v6;  // [bp-0x58]
    unsigned int v7;  // [bp-0x54]
    int v8;  // [bp-0x50]
    int v9;  // [bp-0x4c]
    char v10;  // [bp-0x40]
    struct_0 **v11;  // [bp-0x28]
    unsigned int v12;  // [bp-0x24]
    struct_0 v13;  // [bp-0x20]
    unsigned int v14;  // [bp-0x18]
    char *v15;  // [bp-0x14], Other Possible Types: struct_0 **
    unsigned int v16;  // [bp-0x10]
    unsigned int v17;  // [bp-0xc]
    char v18;  // [bp-0x8], Other Possible Types: unsigned int
    char v19;  // [bp-0x4]

    v18 = 4294967295;
    v17 = sub_10371270;
    v23 = _ccall(v20, v21, (unsigned int)v22, 0);
    v16 = *((int *)v23);
    v15 = a0;
    v6 = v24;
    v5 = v25;
    v4 = v26;
    v3 = g_1038e180 ^ &v19;
    v27 = _ccall(v20, v21, (unsigned int)v22, 0);
    *((unsigned int **)v27) = &v16;
    v15 = &v3;
    v14 = 0;
    sub_103454a0(&v13, a0);
    v18 = 0;
    if ((char)sub_103455c0(&v13))
    {
        v9 = sub_10314d40((char *)a0 + *(a0)->field_4, &v11);
        v8 = v9;
        v18 = 1;
        v12 = sub_10347eb0(v8);
        v18 = 0;
        sub_103130c0(&v11);
        v18 = 2;
        v7 = (!a0 ? NULL : (struct_0 **)((char *)a0 + *(a0)->field_4));
        v2 = a1;
        v1 = sub_10345220((char *)a0 + *(a0)->field_4);
        v0 = v7;
        v28 = sub_10347e60(sub_10315c20((char *)a0 + *(a0)->field_4));
        if ((char)sub_103455c0(sub_10347e10(&v10, v28[0], v28[1], v28[2])))
            v14 |= 4;
        v18 = 0;
    }
    sub_10314630((char *)a0 + *(a0)->field_4, v14, 0);
    v18 = 4294967295;
    sub_10345550(&v13);
    v29 = _ccall(v20, v21, (unsigned int)v22, 0);
    *((unsigned int *)v29) = v16;
    return a0;
}
```

## `sub_10347d9a` `0x10347d9a`

_33 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

int sub_10347d9a(void)
{
    struct_0 **v1;  // [bp+0xfffc0]
    unsigned int v2;  // [bp+0x100000]

    sub_10314630((char *)v1 + *(v1)->field_4, 4, 1);
    v2 = 0;
    return "j";
}
```

## `sub_10347e10` `0x10347e10`

_67 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[24];
    struct struct_1 *field_18;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_10347e10(struct_0 **a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, char a6, unsigned int a7)
{
    unsigned int v2;  // ecx
    struct_0 **v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    v2 = _INSERT(a0, 0, a6);
    *(a0)->field_18(a1, a2, a3, a4, a5, v2, a7, a0, &v1);
    return a1;
}
```

## `sub_10347e60` `0x10347e60`

_40 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    char field_4;
    char padding_5[3];
    unsigned int field_8;
} struct_0;

struct_0 * sub_10347e60(struct_0 *idx, unsigned int a1)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = idx;
    sub_10347e90(idx, &v1);
    idx->field_4 = 0;
    idx->field_8 = a1;
    return idx;
}
```

## `sub_10347e90` `0x10347e90`

_22 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_10347e90(unsigned int *a0)
{
    unsigned int *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_10341910(v0);
    return v0;
}
```

## `sub_10347eb0` `0x10347eb0`

_233 bytes. refs "bad cast"_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
    char padding_c[8];
    char field_14;
} struct_0;

extern unsigned int g_1038e180;
extern int g_103999a0;
extern unsigned int g_103a17a8;
extern unsigned int g_103a2d84;

unsigned int sub_10347eb0(struct_0 **a0)
{
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // fs
    unsigned long v13;  // 4137
    unsigned long v14;  // 4151
    unsigned long v15;  // 4117
    unsigned int v0;  // [bp-0x34]
    char v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x24]
    unsigned int v3;  // [bp-0x20]
    unsigned int v4;  // [bp-0x18]
    unsigned int v5;  // [bp-0x14]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]
    char v9;  // [bp-0x4]

    v8 = 4294967295;
    v7 = sub_10371298;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v6 = *((int *)v13);
    v14 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v14) = &v6;
    sub_10350060(0, g_1038e180 ^ &v9);
    v8 = 0;
    v3 = g_103a2d84;
    v4 = sub_10314f00(&g_103a17a8);
    v5 = sub_10314fb0(a0, v4);
    if (!v5)
    {
        if (v3)
        {
            v5 = v3;
        }
        else if (sub_10347fa0(&v3) == 4294967295)
        {
            sub_103532f5("bad cast");
            sub_103533ea(&v1, &g_103999a0);
        }
        else
        {
            v5 = v3;
            g_103a2d84 = v3;
            v2 = v3;
            sub_10313500(v2);
            sub_10314f90(v2);
        }
    }
    v0 = v5;
    v8 = 4294967295;
    sub_10350081();
    v15 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v15) = v6;
    return v0;
}
```

## `sub_10347fa0` `0x10347fa0`

_140 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10347fa0(unsigned int *a0)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4166
    unsigned long v12;  // 4170
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_103712cb;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v0 = g_1038e180 ^ &v7;
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    if (a0 && !*(a0))
    {
        v2 = sub_10350a53(16);
        v6 = 0;
        v1 = (!v2 ? 0 : sub_10348030(0));
        v3 = v1;
        v6 = 4294967295;
        *(a0) = v3;
    }
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v13) = v4;
    return 4;
}
```

## `sub_10348030` `0x10348030`

_176 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390c84;

int sub_10348030(void* a0, unsigned int a1)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4140
    unsigned long v11;  // 4157
    unsigned long v12;  // 4121
    unsigned int v0;  // [bp-0x98]
    char v1;  // [bp-0x90]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char v5;  // [bp-0x8], Other Possible Types: unsigned int
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_10371306;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v2 = g_1038e180 ^ &v6;
    v0 = v2;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    sub_103153b0(a0, a1);
    v5 = 0;
    *((char **)a0) = &g_10390c84;
    sub_103151b0(&v1, "C");
    v5 = 1;
    sub_10319640(a0, &v1);
    v5 = 0;
    sub_10315290(&v1);
    v5 = 4294967295;
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v3;
    return sub_10351225();
}
```

## `sub_103480e0` `0x103480e0`

_704 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[36];
    int field_24;
} struct_0;

extern unsigned int g_1038e180;

int sub_103480e0(struct_0 **a0, int a1, int a2, int a3, int a4, struct_0 *a5, char a6, char a7)
{
    unsigned long v23;  // ldt
    unsigned long v24;  // gdt
    int idx[3];  // eax
    unsigned int index[3];  // eax
    unsigned long v36;  // 4116
    unsigned short v25;  // fs
    unsigned long v26;  // 4139
    unsigned int v27;  // esi
    unsigned long v28;  // 4158
    unsigned int v29;  // ecx
    int v30;  // eax
    int v31;  // eax
    int v0;  // [bp-0xb8]
    unsigned int v1;  // [bp-0xb4]
    unsigned int v2;  // [bp-0xb0]
    int v3;  // [bp-0xac]
    unsigned int v4;  // [bp-0xa8]
    unsigned int v5;  // [bp-0xa4]
    unsigned int v6;  // [bp-0xa0]
    unsigned int v7;  // [bp-0x9c]
    unsigned int v8;  // [bp-0x98]
    unsigned int v9;  // [bp-0x94]
    char v10;  // [bp-0x8c]
    char v11;  // [bp-0x80]
    char v12;  // [bp-0x74]
    char v13;  // [bp-0x58]
    struct_0 **v14;  // [bp-0x3c]
    char v15;  // [bp-0x38]
    unsigned int v16;  // [bp-0x1c]
    int v17;  // [bp-0x18]
    unsigned int v18;  // [bp-0x14]
    unsigned int v19;  // [bp-0x10]
    unsigned int v20;  // [bp-0xc]
    char v21;  // [bp-0x8], Other Possible Types: unsigned int
    char v22;  // [bp-0x4]

    v21 = 4294967295;
    v20 = sub_10371350;
    v26 = _ccall(v23, v24, (unsigned int)v25, 0);
    v19 = *((int *)v26);
    v16 = g_1038e180 ^ &v22;
    v2 = v27;
    v1 = v16;
    v28 = _ccall(v23, v24, (unsigned int)v25, 0);
    *((unsigned int **)v28) = &v19;
    if (!((short)sub_10315ef0(a5) & 0x4000))
    {
        v29 = _INSERT(0, 0, a6);
        (*((int *)&*(a0)->padding_0[28]))(a1, a2, a3, a4, a5, v29, a7);
    }
    else
    {
        v9 = sub_10314d40(a5, &v14);
        v8 = v9;
        v21 = 0;
        v18 = sub_10316fe0(v8);
        v21 = 4294967295;
        sub_103130c0(&v14);
        sub_10315800(&v15);
        v21 = 1;
        if (a7)
        {
            v7 = sub_10316f70(v18, &v13);
            v6 = v7;
            v21 = 2;
            sub_1031a130(&v15, v6);
            v21 = 1;
            sub_10314610(&v13);
        }
        else
        {
            v5 = sub_10316f00(v18, &v12);
            v4 = v5;
            v21 = 3;
            sub_1031a130(&v15, v4);
            v21 = 1;
            sub_10314610(&v12);
        }
        if (sub_103451d0(a5) > 0 && !((v30 = sub_103451d0(a5), sub_103451d0(a5) <= sub_1031e920(&v15))))
        {
            v31 = sub_103451d0(a5);
            v3 = v31 - sub_1031e920(&v15);
        }
        else
        {
            v3 = 0;
        }
        v17 = v3;
        if (((short)sub_10315ef0(a5) & 448) != 64)
        {
            idx = sub_10349910(a0, &v11, a2, a3, a4, _INSERT(0, 0, a6), v17);
            a2 = idx[0];
            a3 = idx[1];
            a4 = idx[2];
            v17 = 0;
        }
        v0 = sub_1031e920(&v15);
        index = sub_103498b0(a0, &v10, a2, a3, a4, (unsigned int)sub_102ec9a0(&v15));
        a2 = index[0];
        a3 = index[1];
        a4 = index[2];
        sub_103451f0(a5, 0);
        sub_10349910(a0, a1, a2, a3, a4, _INSERT(0, 0, a6), v17);
        v21 = 4294967295;
        sub_10314610(&v15);
    }
    v36 = _ccall(v23, v24, (unsigned int)v25, 0);
    *((unsigned int *)v36) = v19;
    return sub_10351225();
}
```

## `sub_10348163` `0x10348163`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10348163(void)
{
}
```

## `sub_103483b0` `0x103483b0`

_145 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_103483b0(int a0, int a1, int a2, int a3, int a4, unsigned int a5, char a6, unsigned int a7)
{
    unsigned int v0;  // [bp-0x5c]
    char v1;  // [bp-0x54]
    char v2;  // [bp-0x4c]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v3 = g_1038e180 ^ &v5;
    v4 = 64;
    v0 = a7;
    sub_10349500(a0, a1, a2, a3, a4, a5, _INSERT(0, 0, a6), &v2, sub_103531a2(&v2, 64, sub_10349400(a0, &v1, "ld", sub_10315ef0(a5))));
    return sub_10351225();
}
```

## `sub_10348450` `0x10348450`

_145 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10348450(int a0, int a1, int a2, int a3, int a4, unsigned int a5, char a6, unsigned int a7)
{
    unsigned int v0;  // [bp-0x5c]
    char v1;  // [bp-0x54]
    char v2;  // [bp-0x4c]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v3 = g_1038e180 ^ &v5;
    v4 = 64;
    v0 = a7;
    sub_10349500(a0, a1, a2, a3, a4, a5, _INSERT(0, 0, a6), &v2, sub_103531a2(&v2, 64, sub_10349400(a0, &v1, "lu", sub_10315ef0(a5))));
    return sub_10351225();
}
```

## `sub_103484f0` `0x103484f0`

_149 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

extern unsigned int g_1038e180;

int sub_103484f0(int a0, int a1, int a2, int a3, unsigned int a4, struct_0 *a5, char a6, unsigned int a7, unsigned int a8)
{
    unsigned int v0;  // [bp-0x6c]
    struct_0 *v1;  // [bp-0x68]
    unsigned int v2;  // [bp-0x64]
    char *v3;  // [bp-0x60], Other Possible Types: unsigned int
    unsigned int v4;  // [bp-0x5c]
    char v5;  // [bp-0x54]
    char v6;  // [bp-0x4c]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]
    char v9;  // [bp-0x4]

    v7 = g_1038e180 ^ &v9;
    v8 = 64;
    v4 = a8;
    v3 = a7;
    v4 = sub_103531a2(&v6, 64, sub_10349400(a0, &v5, "Ld", sub_10315ef0(a5)));
    v3 = &v6;
    v2 = _INSERT(v4, 0, a6);
    v1 = a5;
    v0 = a4;
    sub_10349500(a0, a1, a2, a3);
    return sub_10351225();
}
```

## `sub_10348590` `0x10348590`

_149 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

extern unsigned int g_1038e180;

int sub_10348590(int a0, int a1, int a2, int a3, unsigned int a4, struct_0 *a5, char a6, unsigned int a7, unsigned int a8)
{
    unsigned int v0;  // [bp-0x6c]
    struct_0 *v1;  // [bp-0x68]
    unsigned int v2;  // [bp-0x64]
    char *v3;  // [bp-0x60], Other Possible Types: unsigned int
    unsigned int v4;  // [bp-0x5c]
    char v5;  // [bp-0x54]
    char v6;  // [bp-0x4c]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]
    char v9;  // [bp-0x4]

    v7 = g_1038e180 ^ &v9;
    v8 = 64;
    v4 = a8;
    v3 = a7;
    v4 = sub_103531a2(&v6, 64, sub_10349400(a0, &v5, "Lu", sub_10315ef0(a5)));
    v3 = &v6;
    v2 = _INSERT(v4, 0, a6);
    v1 = a5;
    v0 = a4;
    sub_10349500(a0, a1, a2, a3);
    return sub_10351225();
}
```

## `sub_10348630` `0x10348630`

_553 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern unsigned long long g_10390cc8;
extern unsigned long long g_10390cd0;

int sub_10348630(int a0, int a1, int a2, int a3, int a4, unsigned int a5, char a6)
{
    unsigned int v17;  // ftop
    unsigned int v24;  // ftop
    unsigned int v25;  // ftop
    unsigned int v26;  // ftop
    unsigned int v27;  // ftop
    unsigned int v28;  // fc3210
    unsigned int v29;  // ftop
    unsigned int v30;  // ftop
    unsigned int v31;  // ftop
    unsigned int v32;  // fc3210
    unsigned int v33;  // ftop
    unsigned int v34;  // ftop
    unsigned int v35;  // ftop
    unsigned int v18;  // ftop
    unsigned int v19;  // ftop
    unsigned int v20;  // ftop
    unsigned int v21;  // ftop
    unsigned int v22;  // fc3210
    unsigned int v23;  // ftop
    int v0;  // [bp-0xb8]
    double v1;  // [bp-0xb4], Other Possible Types: unsigned long
    unsigned int v2;  // [bp-0xac]
    int v3;  // [bp-0xa8]
    int v4;  // [bp-0xa4]
    char v5;  // [bp-0x99]
    int v6;  // [bp-0x98]
    char v7;  // [bp-0x94]
    char v8;  // [bp-0x8c]
    unsigned int v9;  // [bp-0x18]
    unsigned int v10;  // [bp-0x14]
    int iter;  // [bp-0x10]
    int i;  // [bp-0xc]
    int v13;  // [bp-0x8]
    char v14;  // [bp-0x4]
    double v15;  // [bp+0x1c], Other Possible Types: unsigned long

    v9 = g_1038e180 ^ &v14;
    v10 = 108;
    if (sub_1031e920(a5) <= 0 && !((short)sub_10315ef0(a5) & 0x2000))
        v4 = 6;
    else
        v4 = sub_1031e920(a5);
    iter = v4;
    v3 = (iter <= 36 ? iter : 36);
    v6 = v3;
    iter -= v6;
    v13 = 0;
    i = 0;
    if (((short)sub_10315ef0(a5) & 0x3000) == 0x2000)
    {
        /* unsupported instruction */
        /* unsupported instruction */
        /* unsupported instruction */
        v2 = (!((char)((((unsigned short)v17 & 7) * 0x800 | CmpF((/* unsupported instruction */ ? /* unsupported instruction */ : nan), v15) * 0x100 & 0x4500 & 0x4700) >> 8) & 65) ? 1 : 0);
        v5 = v2;
        if (v5)
        {
            v18 = v17 - 1;
            if (/* unsupported instruction */)
            {
                v19 = v18 - 1;
                /* unsupported instruction */
                /* unsupported instruction */
            }
            else
            {
                v19 = v18 - 1;
                /* unsupported instruction */
                /* unsupported instruction */
            }
            /* unsupported instruction */
            /* unsupported instruction */
            v15 = (double)(/* unsupported instruction */ ? /* unsupported instruction */ : nan);
            /* unsupported instruction */
            v17 = v19 + 1;
        }
        while (true)
        {
            v20 = v17 - 1;
            if (/* unsupported instruction */)
            {
                v21 = v20 - 1;
                /* unsupported instruction */
                /* unsupported instruction */
            }
            else
            {
                v21 = v20 - 1;
                /* unsupported instruction */
                /* unsupported instruction */
            }
            if (/* unsupported instruction */)
            {
                v22 = CmpF(/* unsupported instruction */, g_10390cc8) * 0x100 & 0x4500;
                /* unsupported instruction */
                v23 = v21 + 1;
            }
            else
            {
                v22 = CmpF(nan, g_10390cc8) * 0x100 & 0x4500;
                /* unsupported instruction */
                v23 = v21 + 1;
            }
            if (((char)((((unsigned short)v23 & 7) * 0x800 | (unsigned short)v22 & 0x4700) >> 8) & 1) || v13 >= 5000)
                break;
            v24 = v23 - 1;
            if (/* unsupported instruction */)
            {
                v25 = v24 - 1;
                /* unsupported instruction */
                /* unsupported instruction */
            }
            else
            {
                v25 = v24 - 1;
                /* unsupported instruction */
                /* unsupported instruction */
            }
            if (/* unsupported instruction */)
            {
                /* unsupported instruction */
                /* unsupported instruction */
            }
            else
            {
                /* unsupported instruction */
                /* unsupported instruction */
            }
            if (/* unsupported instruction */)
            {
                v15 = (double)/* unsupported instruction */;
                /* unsupported instruction */
                v17 = v25 + 1;
            }
            else
            {
                v15 = (double)nan;
                /* unsupported instruction */
                v17 = v25 + 1;
            }
            v13 += 10;
        }
        v26 = v23 - 1;
        if (/* unsupported instruction */)
        {
            v27 = v26 - 1;
            /* unsupported instruction */
            /* unsupported instruction */
        }
        else
        {
            v27 = v26 - 1;
            /* unsupported instruction */
            /* unsupported instruction */
        }
        if (/* unsupported instruction */)
        {
            v28 = CmpF(/* unsupported instruction */, g_10390cd0) * 0x100 & 0x4500;
            /* unsupported instruction */
            v29 = v27 + 1;
        }
        else
        {
            v28 = CmpF(nan, g_10390cd0) * 0x100 & 0x4500;
            /* unsupported instruction */
            v29 = v27 + 1;
        }
        if (!((char)((((unsigned short)v29 & 7) * 0x800 | (unsigned short)v28 & 0x4700) >> 8) & 65))
        {
            for (; iter >= 10; i += 10)
            {
                v30 = v29 - 1;
                if (/* unsupported instruction */)
                {
                    v31 = v30 - 1;
                    /* unsupported instruction */
                    /* unsupported instruction */
                }
                else
                {
                    v31 = v30 - 1;
                    /* unsupported instruction */
                    /* unsupported instruction */
                }
                if (/* unsupported instruction */)
                {
                    v32 = CmpF(/* unsupported instruction */, v15) * 0x100 & 0x4500;
                    /* unsupported instruction */
                    v33 = v31 + 1;
                }
                else
                {
                    v32 = CmpF(nan, v15) * 0x100 & 0x4500;
                    /* unsupported instruction */
                    v33 = v31 + 1;
                }
                if (((char)((((unsigned short)v33 & 7) * 0x800 | (unsigned short)v32 & 0x4700) >> 8) & 1) || i >= 5000)
                    break;
                v34 = v33 - 1;
                if (/* unsupported instruction */)
                {
                    v35 = v34 - 1;
                    /* unsupported instruction */
                    /* unsupported instruction */
                }
                else
                {
                    v35 = v34 - 1;
                    /* unsupported instruction */
                    /* unsupported instruction */
                }
                if (/* unsupported instruction */)
                {
                    /* unsupported instruction */
                    /* unsupported instruction */
                }
                else
                {
                    /* unsupported instruction */
                    /* unsupported instruction */
                }
                if (/* unsupported instruction */)
                {
                    v15 = (double)/* unsupported instruction */;
                    /* unsupported instruction */
                    v29 = v35 + 1;
                }
                else
                {
                    v15 = (double)nan;
                    /* unsupported instruction */
                    v29 = v35 + 1;
                }
                iter -= 10;
            }
        }
        if (v5)
        {
            if (/* unsupported instruction */)
            {
                /* unsupported instruction */
                /* unsupported instruction */
            }
            else
            {
                /* unsupported instruction */
                /* unsupported instruction */
            }
            /* unsupported instruction */
            /* unsupported instruction */
            v15 = (/* unsupported instruction */ ? /* unsupported instruction */ : nan);
            /* unsupported instruction */
        }
    }
    if (/* unsupported instruction */)
    {
        /* unsupported instruction */
        /* unsupported instruction */
    }
    else
    {
        /* unsupported instruction */
        /* unsupported instruction */
    }
    if (/* unsupported instruction */)
    {
        v1 = /* unsupported instruction */;
        /* unsupported instruction */
    }
    else
    {
        v1 = (double)nan;
        /* unsupported instruction */
    }
    v0 = v6;
    sub_10348c70(a0, a1, a2, a3, a4, a5, _INSERT(i, 0, a6), &v8, v13, i, iter, sub_103531a2(&v8, 108, sub_10348ba0(a0, &v7, 0, sub_10315ef0(a5))));
    return sub_10351225();
}
```

## `sub_10348860` `0x10348860`

_553 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern unsigned long long g_10390cc8;
extern unsigned long long g_10390cd0;

int sub_10348860(int a0, int a1, int a2, int a3, int a4, unsigned int a5, char a6)
{
    unsigned int v17;  // ftop
    unsigned int v24;  // ftop
    unsigned int v25;  // ftop
    unsigned int v26;  // ftop
    unsigned int v27;  // ftop
    unsigned int v28;  // fc3210
    unsigned int v29;  // ftop
    unsigned int v30;  // ftop
    unsigned int v31;  // ftop
    unsigned int v32;  // fc3210
    unsigned int v33;  // ftop
    unsigned int v34;  // ftop
    unsigned int v35;  // ftop
    unsigned int v18;  // ftop
    unsigned int v19;  // ftop
    unsigned int v20;  // ftop
    unsigned int v21;  // ftop
    unsigned int v22;  // fc3210
    unsigned int v23;  // ftop
    int v0;  // [bp-0xb8]
    double v1;  // [bp-0xb4], Other Possible Types: unsigned long
    unsigned int v2;  // [bp-0xac]
    int v3;  // [bp-0xa8]
    int v4;  // [bp-0xa4]
    char v5;  // [bp-0x99]
    int v6;  // [bp-0x98]
    char v7;  // [bp-0x94]
    char v8;  // [bp-0x8c]
    unsigned int v9;  // [bp-0x18]
    unsigned int v10;  // [bp-0x14]
    int iter;  // [bp-0x10]
    int i;  // [bp-0xc]
    int v13;  // [bp-0x8]
    char v14;  // [bp-0x4]
    double v15;  // [bp+0x1c], Other Possible Types: unsigned long

    v9 = g_1038e180 ^ &v14;
    v10 = 108;
    if (sub_1031e920(a5) <= 0 && !((short)sub_10315ef0(a5) & 0x2000))
        v4 = 6;
    else
        v4 = sub_1031e920(a5);
    iter = v4;
    v3 = (iter <= 36 ? iter : 36);
    v6 = v3;
    iter -= v6;
    v13 = 0;
    i = 0;
    if (((short)sub_10315ef0(a5) & 0x3000) == 0x2000)
    {
        /* unsupported instruction */
        /* unsupported instruction */
        /* unsupported instruction */
        v2 = (!((char)((((unsigned short)v17 & 7) * 0x800 | CmpF((/* unsupported instruction */ ? /* unsupported instruction */ : nan), v15) * 0x100 & 0x4500 & 0x4700) >> 8) & 65) ? 1 : 0);
        v5 = v2;
        if (v5)
        {
            v18 = v17 - 1;
            if (/* unsupported instruction */)
            {
                v19 = v18 - 1;
                /* unsupported instruction */
                /* unsupported instruction */
            }
            else
            {
                v19 = v18 - 1;
                /* unsupported instruction */
                /* unsupported instruction */
            }
            /* unsupported instruction */
            /* unsupported instruction */
            v15 = (double)(/* unsupported instruction */ ? /* unsupported instruction */ : nan);
            /* unsupported instruction */
            v17 = v19 + 1;
        }
        while (true)
        {
            v20 = v17 - 1;
            if (/* unsupported instruction */)
            {
                v21 = v20 - 1;
                /* unsupported instruction */
                /* unsupported instruction */
            }
            else
            {
                v21 = v20 - 1;
                /* unsupported instruction */
                /* unsupported instruction */
            }
            if (/* unsupported instruction */)
            {
                v22 = CmpF(/* unsupported instruction */, g_10390cc8) * 0x100 & 0x4500;
                /* unsupported instruction */
                v23 = v21 + 1;
            }
            else
            {
                v22 = CmpF(nan, g_10390cc8) * 0x100 & 0x4500;
                /* unsupported instruction */
                v23 = v21 + 1;
            }
            if (((char)((((unsigned short)v23 & 7) * 0x800 | (unsigned short)v22 & 0x4700) >> 8) & 1) || v13 >= 5000)
                break;
            v24 = v23 - 1;
            if (/* unsupported instruction */)
            {
                v25 = v24 - 1;
                /* unsupported instruction */
                /* unsupported instruction */
            }
            else
            {
                v25 = v24 - 1;
                /* unsupported instruction */
                /* unsupported instruction */
            }
            if (/* unsupported instruction */)
            {
                /* unsupported instruction */
                /* unsupported instruction */
            }
            else
            {
                /* unsupported instruction */
                /* unsupported instruction */
            }
            if (/* unsupported instruction */)
            {
                v15 = (double)/* unsupported instruction */;
                /* unsupported instruction */
                v17 = v25 + 1;
            }
            else
            {
                v15 = (double)nan;
                /* unsupported instruction */
                v17 = v25 + 1;
            }
            v13 += 10;
        }
        v26 = v23 - 1;
        if (/* unsupported instruction */)
        {
            v27 = v26 - 1;
            /* unsupported instruction */
            /* unsupported instruction */
        }
        else
        {
            v27 = v26 - 1;
            /* unsupported instruction */
            /* unsupported instruction */
        }
        if (/* unsupported instruction */)
        {
            v28 = CmpF(/* unsupported instruction */, g_10390cd0) * 0x100 & 0x4500;
            /* unsupported instruction */
            v29 = v27 + 1;
        }
        else
        {
            v28 = CmpF(nan, g_10390cd0) * 0x100 & 0x4500;
            /* unsupported instruction */
            v29 = v27 + 1;
        }
        if (!((char)((((unsigned short)v29 & 7) * 0x800 | (unsigned short)v28 & 0x4700) >> 8) & 65))
        {
            for (; iter >= 10; i += 10)
            {
                v30 = v29 - 1;
                if (/* unsupported instruction */)
                {
                    v31 = v30 - 1;
                    /* unsupported instruction */
                    /* unsupported instruction */
                }
                else
                {
                    v31 = v30 - 1;
                    /* unsupported instruction */
                    /* unsupported instruction */
                }
                if (/* unsupported instruction */)
                {
                    v32 = CmpF(/* unsupported instruction */, v15) * 0x100 & 0x4500;
                    /* unsupported instruction */
                    v33 = v31 + 1;
                }
                else
                {
                    v32 = CmpF(nan, v15) * 0x100 & 0x4500;
                    /* unsupported instruction */
                    v33 = v31 + 1;
                }
                if (((char)((((unsigned short)v33 & 7) * 0x800 | (unsigned short)v32 & 0x4700) >> 8) & 1) || i >= 5000)
                    break;
                v34 = v33 - 1;
                if (/* unsupported instruction */)
                {
                    v35 = v34 - 1;
                    /* unsupported instruction */
                    /* unsupported instruction */
                }
                else
                {
                    v35 = v34 - 1;
                    /* unsupported instruction */
                    /* unsupported instruction */
                }
                if (/* unsupported instruction */)
                {
                    /* unsupported instruction */
                    /* unsupported instruction */
                }
                else
                {
                    /* unsupported instruction */
                    /* unsupported instruction */
                }
                if (/* unsupported instruction */)
                {
                    v15 = (double)/* unsupported instruction */;
                    /* unsupported instruction */
                    v29 = v35 + 1;
                }
                else
                {
                    v15 = (double)nan;
                    /* unsupported instruction */
                    v29 = v35 + 1;
                }
                iter -= 10;
            }
        }
        if (v5)
        {
            if (/* unsupported instruction */)
            {
                /* unsupported instruction */
                /* unsupported instruction */
            }
            else
            {
                /* unsupported instruction */
                /* unsupported instruction */
            }
            /* unsupported instruction */
            /* unsupported instruction */
            v15 = (/* unsupported instruction */ ? /* unsupported instruction */ : nan);
            /* unsupported instruction */
        }
    }
    if (/* unsupported instruction */)
    {
        /* unsupported instruction */
        /* unsupported instruction */
    }
    else
    {
        /* unsupported instruction */
        /* unsupported instruction */
    }
    if (/* unsupported instruction */)
    {
        v1 = /* unsupported instruction */;
        /* unsupported instruction */
    }
    else
    {
        v1 = (double)nan;
        /* unsupported instruction */
    }
    v0 = v6;
    sub_10348c70(a0, a1, a2, a3, a4, a5, _INSERT(i, 0, a6), &v8, v13, i, iter, sub_103531a2(&v8, 108, sub_10348ba0(a0, &v7, 76, sub_10315ef0(a5))));
    return sub_10351225();
}
```

## `sub_10348a90` `0x10348a90`

_119 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10348a90(int a0, int a1, int a2, int a3, int a4, int a5, char a6, int a7)
{
    int v4;  // eax
    char v0;  // [bp-0x4c]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]

    v1 = g_1038e180 ^ &v3;
    v2 = 64;
    v4 = sub_103531a2(&v0, 64, "%p", a7, a0);
    sub_10349500(a0, a1, a2, a3, a4, a5, _INSERT(v4, 0, a6), &v0, v4);
    return sub_10351225();
}
```

## `sub_10348b10` `0x10348b10`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10348b10(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10348b40(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_10348b40` `0x10348b40`

_84 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390c84;

int sub_10348b40(unsigned int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4139
    unsigned long v11;  // 4155
    int v12;  // eax
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_10371388;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    *((char **)v1) = &g_10390c84;
    v4 = 0;
    v4 = 4294967295;
    v12 = sub_10315390(v1);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_10348ba0` `0x10348ba0`

_202 bytes. (leaf/helper — see body)_

```c
char [5] sub_10348ba0(unsigned int a0, char *a1, char a2, unsigned int a3)
{
    char v0;  // [bp-0xd]
    unsigned int v1;  // [bp-0xc]
    char iter[5];  // [bp-0x8]

    iter = a1;
    iter[0] = 37;
    iter = &iter[1];
    if (((char)a3 & 32))
    {
        iter[0] = 43;
        iter = &iter[1];
    }
    if (((char)a3 & 16))
    {
        iter[0] = 35;
        iter = &iter[1];
    }
    iter[0] = 46;
    iter = &iter[1];
    iter[0] = 42;
    iter = &iter[1];
    if (a2)
    {
        iter[0] = a2;
        iter = &iter[1];
    }
    v1 = a3 & 0x3000;
    v0 = (v1 == 0x2000 ? 0x66 : (char)((v1 != 0x1000) * 2 + 101));
    iter[0] = v0;
    iter = &iter[1];
    iter[0] = 0;
    return a1;
}
```

## `sub_10348c70` `0x10348c70`

_1933 bytes. refs " : "_

```c
typedef struct struct_0 {
    char padding_0[36];
    int field_24;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
    int field_8;
} struct_1;

extern unsigned int g_1038e180;

int sub_10348c70(int a0, int a1, int a2, int a3, int a4, struct_0 *a5, char a6, char *iter1, unsigned int a8, unsigned int a9, unsigned int a10, int iter)
{
    unsigned long v43;  // ldt
    unsigned long v44;  // gdt
    int index[3];  // eax
    unsigned int idx[3];  // eax
    int v57;  // ecx
    unsigned int idx1[3];  // eax
    unsigned int idx2[3];  // eax
    int v60;  // ecx
    int v61[3];  // eax
    int v62;  // eax
    unsigned short v45;  // fs
    unsigned int v64[3];  // eax
    int v65;  // edx
    unsigned int v66[3];  // eax
    struct_1 *v67;  // eax
    unsigned int v69[3];  // eax
    int v70;  // edx
    unsigned int v71[3];  // eax
    unsigned long v46;  // 4139
    unsigned long v73;  // 4118
    unsigned long v47;  // 4156
    struct_0 **v48;  // eax
    char *v49;  // eax
    int v51[3];  // eax
    int v52[3];  // eax
    unsigned int v0;  // [bp-0x134]
    char *v1;  // [bp-0x130], Other Possible Types: int, unsigned int
    unsigned int v2;  // [bp-0x12c]
    int v3;  // [bp-0x128]
    int v4;  // [bp-0x124]
    unsigned int v5;  // [bp-0x120]
    unsigned int v6;  // [bp-0x11c]
    unsigned int v7;  // [bp-0x118]
    char v8;  // [bp-0x114]
    char v9;  // [bp-0x108]
    char v10;  // [bp-0xfc]
    char v11;  // [bp-0xf0]
    char v12;  // [bp-0xe4]
    char v13;  // [bp-0xd8]
    char v14;  // [bp-0xcc]
    char v15;  // [bp-0xc0]
    char v16;  // [bp-0xb4]
    char v17;  // [bp-0xa8]
    char v18;  // [bp-0x9c]
    char v19;  // [bp-0x90]
    struct_0 **v20;  // [bp-0x84]
    int v21;  // [bp-0x80]
    int v22;  // [bp-0x7c]
    unsigned int v23;  // [bp-0x78]
    char node[2];  // [bp-0x74]
    struct_0 v25;  // [bp-0x70]
    char v26;  // [bp-0x54]
    unsigned int v27;  // [bp-0x38]
    int v28;  // [bp-0x34], Other Possible Types: unsigned int
    int v29;  // [bp-0x30]
    char v30;  // [bp-0x29]
    unsigned int v31;  // [bp-0x28]
    unsigned int v32;  // [bp-0x24]
    char v33;  // [bp-0x20]
    char v34;  // [bp-0x1f]
    char v35;  // [bp-0x1e]
    char v36;  // [bp-0x19]
    unsigned int v37;  // [bp-0x18]
    char *v38;  // [bp-0x14]
    unsigned int v39;  // [bp-0x10]
    unsigned int v40;  // [bp-0xc]
    char v41;  // [bp-0x8], Other Possible Types: unsigned int
    char v42;  // [bp-0x4]

    v41 = 4294967295;
    v40 = sub_103713c8;
    v46 = _ccall(v43, v44, (unsigned int)v45, 0);
    v39 = *((int *)v46);
    v27 = g_1038e180 ^ &v42;
    v2 = v27;
    v47 = _ccall(v43, v44, (unsigned int)v45, 0);
    *((unsigned int **)v47) = &v39;
    v7 = sub_10314d40(a5, &v20);
    v6 = v7;
    v41 = 0;
    v37 = sub_10316fe0(v6);
    v41 = 4294967295;
    sub_103130c0(&v20);
    sub_103189f0(v37, &v26);
    v41 = 1;
    v30 = sub_103189d0(v37);
    sub_10315800(&v25);
    v41 = 2;
    v1 = a0 + 8;
    v0 = 0;
    v36 = sub_10318a60(48);
    if (*(iter1) != 43 && *(iter1) != 45)
        v5 = 0;
    else
        v5 = 1;
    v31 = v5;
    v48 = sub_10353681();
    v33 = *(v48)->padding_0[0];
    v34 = 101;
    v35 = 0;
    v28 = sub_10353a90(iter1, 101, iter);
    v32 = sub_10353a90(iter1, v33, iter);
    if (!v32)
        a10 = 0;
    if (*((char *)(unsigned int)sub_102ec9a0(&v26)) != 127 && *((char *)(unsigned int)sub_102ec9a0(&v26)) > 0)
    {
        sub_1031a6b0(&v25, iter1, iter);
        if (!v28)
        {
            sub_103170f0(&v25, a10, 48);
        }
        else
        {
            if (!v32)
            {
                sub_103170f0(&v25, a8, 48);
                a8 = 0;
            }
            sub_1031e4a0(&v25, v28 - iter1, a10, 48);
        }
        a10 = 0;
        if (!v32)
        {
            sub_103170f0(&v25, a8, 48);
        }
        else
        {
            sub_1031e4a0(&v25, 1 + v32 - iter1, a9, 48);
            sub_1031e4a0(&v25, v32 - iter1, a8, 48);
            a9 = 0;
        }
        a8 = 0;
        node = (unsigned int)sub_102ec9a0(&v26);
        v1 = &v33;
        v23 = sub_10355690(sub_103189a0(&v25, 0));
        while (node[0] != 127 && node[0] > 0 && node[0] < v23 - v31)
        {
            v23 -= node[0];
            sub_1031e4a0(&v25, v23, 1, 0);
            if (node[1] > 0)
                node = &node[1];
        }
        iter1 = sub_103189a0(&v25, 0);
        a10 = 0;
        iter = sub_1031e920(&v25);
    }
    v29 = a8 + a9 + a10 + iter;
    if (sub_103451d0(a5) > 0 && sub_103451d0(a5) > v29)
        v4 = sub_103451d0(a5) - v29;
    else
        v4 = 0;
    v29 = v4;
    v49 = sub_10315ef0(a5) & 448;
    v38 = v49;
    if (v38 != 0x40 && v38 != 0x100)
    {
        v51 = sub_10349910(a0, &v19, a2, a3, a4, _INSERT(v49, 0, a6), v29);
        a2 = v51[0];
        a3 = v51[1];
        a4 = v51[2];
        v29 = 0;
    }
    else if (v38 == 0x100)
    {
        if (v31 > 0)
        {
            v52 = sub_10349960(a0, &v18, a2, a3, a4, iter1, 1);
            a2 = v52[0];
            a3 = v52[1];
            a4 = v52[2];
            v49 = iter1 + 1;
            iter1 = v49;
            iter -= 1;
        }
        index = sub_10349910(a0, &v17, a2, a3, a4, _INSERT(v49, 0, a6), v29);
        a2 = index[0];
        a3 = index[1];
        a4 = index[2];
        v29 = 0;
    }
    v32 = sub_10353a90(iter1, v33, iter);
    if (v32)
    {
        v22 = 1 + v32 - iter1;
        idx = sub_103499d0(a0, &v16, a2, a3, a4, iter1, v22 - 1, _INSERT(0, 0, v30));
        a2 = idx[0];
        a3 = idx[1];
        a4 = idx[2];
        v57 = _INSERT(idx[1], 0, v36);
        idx1 = sub_10349910(a0, &v15, a2, a3, a4, v57, a8);
        a2 = idx1[0];
        a3 = idx1[1];
        a4 = idx1[2];
        v1 = 1;
        idx2 = sub_10349910(a0, &v14, a2, a3, a4, sub_10319210(v37));
        a2 = idx2[0];
        a3 = idx2[1];
        a4 = idx2[2];
        v60 = _INSERT(idx2[1], 0, v36);
        v61 = sub_10349910(a0, &v13, a2, a3, a4, v60, a9);
        a2 = v61[0];
        a3 = v61[1];
        a4 = v61[2];
        iter1 = &iter1[v22];
        iter -= v22;
    }
    v62 = sub_10353a90(iter1, 101, iter);
    v28 = v62;
    if (v28)
    {
        v21 = 1 + v28 - iter1;
        v64 = sub_103499d0(a0, &v12, a2, a3, a4, iter1, v21 - 1, _INSERT(v62, 0, v30));
        a2 = v64[0];
        a3 = v64[1];
        a4 = v64[2];
        v65 = _INSERT(v64[1], 0, v36);
        v66 = sub_10349910(a0, &v11, a2, a3, a4, v65, a10);
        a2 = v66[0];
        a3 = v66[1];
        a4 = v66[2];
        a10 = 0;
        v3 = (!(sub_10315ef0(a5) & 4) ? "e" : "E");
        v67 = sub_10349960(a0, &v10, a2, a3, a4, v3, 1);
        a2 = v67->field_0;
        a3 = v67->field_4;
        v62 = v67->field_8;
        a4 = v62;
        iter1 = &iter1[v21];
        iter -= v21;
    }
    v69 = sub_103499d0(a0, &v9, a2, a3, a4, iter1, iter, _INSERT(v62, 0, v30));
    a2 = v69[0];
    a3 = v69[1];
    a4 = v69[2];
    v70 = _INSERT(v69[1], 0, v36);
    v71 = sub_10349910(a0, &v8, a2, a3, a4, v70, a10);
    a2 = v71[0];
    a3 = v71[1];
    a4 = v71[2];
    sub_103451f0(a5, 0);
    sub_10349910(a0, a1, a2, a3, a4, _INSERT(0, 0, a6), v29);
    v41 = 1;
    sub_10314610(&v25);
    v41 = 4294967295;
    sub_10314610(&v26);
    v73 = _ccall(v43, v44, (unsigned int)v45, 0);
    *((unsigned int *)v73) = v39;
    return sub_10351225();
}
```

## `sub_10349400` `0x10349400`

_249 bytes. (leaf/helper — see body)_

```c
char sub_10349400(unsigned int a0, char *a1, char *a2, unsigned int a3)
{
    char v0;  // [bp-0xe]
    char v1;  // [bp-0xd]
    unsigned int v2;  // [bp-0xc]
    char iter[4];  // [bp-0x8]

    iter = a1;
    iter[0] = 37;
    iter = &iter[1];
    if (((char)a3 & 32))
    {
        iter[0] = 43;
        iter = &iter[1];
    }
    if (((char)a3 & 8))
    {
        iter[0] = 35;
        iter = &iter[1];
    }
    if (*(a2) != 76)
    {
        iter[0] = *(a2);
        iter = &iter[1];
    }
    else
    {
        iter[0] = 73;
        iter = &iter[1];
        iter[0] = 54;
        iter = &iter[1];
        iter[0] = 52;
        iter = &iter[1];
    }
    v2 = a3 & 0xe00;
    if (v2 == 0x400)
    {
        v1 = 111;
    }
    else
    {
        v0 = (v2 == 0x800 ? (-(0 < (a3 & 4)) & 224) + 120 : a2[1]);
        v1 = v0;
    }
    iter[0] = v1;
    iter = &iter[1];
    iter[0] = 0;
    return *((char *)&a1);
}
```

## `sub_10349500` `0x10349500`

_936 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[36];
    int field_24;
} struct_0;

extern unsigned int g_1038e180;

int sub_10349500(int a0, int a1, int a2, int a3, int a4, struct_0 *a5, char a6, char *a7, int node)
{
    unsigned long v23;  // ldt
    unsigned long v24;  // gdt
    int idx[3];  // eax
    unsigned int idx1[3];  // eax
    unsigned long v36;  // 4118
    unsigned short v25;  // fs
    unsigned long v26;  // 4139
    unsigned long v27;  // 4156
    int index[3];  // eax
    unsigned int idx2[3];  // eax
    unsigned int v0;  // [bp-0x94]
    int v1;  // [bp-0x90]
    int v2;  // [bp-0x8c]
    int v3;  // [bp-0x88]
    unsigned int v4;  // [bp-0x84]
    unsigned int v5;  // [bp-0x80]
    char v6;  // [bp-0x7c]
    char v7;  // [bp-0x70]
    char v8;  // [bp-0x64]
    char v9;  // [bp-0x58]
    struct_0 **v10;  // [bp-0x4c]
    int iter1;  // [bp-0x48]
    unsigned int iter;  // [bp-0x44]
    char v13;  // [bp-0x40]
    unsigned int v14;  // [bp-0x24]
    int v15;  // [bp-0x20]
    int v16;  // [bp-0x1c]
    unsigned int v17;  // [bp-0x18]
    unsigned int v18;  // [bp-0x14]
    unsigned int v19;  // [bp-0x10]
    unsigned int v20;  // [bp-0xc]
    unsigned int v21;  // [bp-0x8]
    char v22;  // [bp-0x4]

    v21 = 4294967295;
    v20 = sub_10371400;
    v26 = _ccall(v23, v24, (unsigned int)v25, 0);
    v19 = *((int *)v26);
    v14 = g_1038e180 ^ &v22;
    v0 = v14;
    v27 = _ccall(v23, v24, (unsigned int)v25, 0);
    *((unsigned int **)v27) = &v19;
    v5 = sub_10314d40(a5, &v10);
    v4 = v5;
    v21 = 0;
    v17 = sub_10316fe0(v4);
    v21 = 4294967295;
    sub_103130c0(&v10);
    sub_103189f0(v17, &v13);
    v21 = 1;
    if (*(a7) != 43 && *(a7) != 45)
    {
        if (*(a7) == 48 && (a7[1] == 120 || a7[1] == 88))
            v3 = 2;
        else
            v3 = 0;
        v2 = v3;
    }
    else
    {
        v2 = 1;
    }
    v16 = v2;
    if (*((char *)(unsigned int)sub_102ec9a0(&v13)) != 127 && *((char *)(unsigned int)sub_102ec9a0(&v13)) > 0)
    {
        iter = (unsigned int)sub_102ec9a0(&v13);
        iter1 = node;
        while (*((char *)iter) != 127 && *((char *)iter) > 0 && *((char *)iter) < iter1 - v16)
        {
            iter1 -= *((char *)iter);
            sub_10353626(&a7[iter1 + 1], node + 1 - iter1, &a7[iter1], node + 1 - iter1);
            a7[iter1] = 0;
            node += 1;
            if (*((char *)(iter + 1)) > 0)
                iter += 1;
        }
    }
    if (sub_103451d0(a5) > 0 && sub_103451d0(a5) > node)
        v1 = sub_103451d0(a5) - node;
    else
        v1 = 0;
    v15 = v1;
    v18 = sub_10315ef0(a5) & 448;
    if (v18 != 64 && v18 != 0x100)
    {
        index = sub_10349910(a0, &v9, a2, a3, a4, _INSERT(v18, 0, a6), v15);
        a2 = index[0];
        a3 = index[1];
        a4 = index[2];
        v15 = 0;
    }
    else if (v18 == 0x100)
    {
        idx2 = sub_10349960(a0, &v8, a2, a3, a4, a7, v16);
        a2 = idx2[0];
        a3 = idx2[1];
        a4 = idx2[2];
        a7 = &a7[v16];
        node -= v16;
        idx = sub_10349910(a0, &v7, a2, a3, a4, _INSERT(a7, 0, a6), v15);
        a2 = idx[0];
        a3 = idx[1];
        a4 = idx[2];
        v15 = 0;
    }
    idx1 = sub_103499d0(a0, &v6, a2, a3, a4, a7, node, sub_103189d0(v17));
    a2 = idx1[0];
    a3 = idx1[1];
    a4 = idx1[2];
    sub_103451f0(a5, 0);
    sub_10349910(a0, a1, a2, a3, a4, _INSERT(0, 0, a6), v15);
    v21 = 4294967295;
    sub_10314610(&v13);
    v36 = _ccall(v23, v24, (unsigned int)v25, 0);
    *((unsigned int *)v36) = v19;
    return sub_10351225();
}
```

## `sub_103498b0` `0x103498b0`

_85 bytes. (leaf/helper — see body)_

```c
unsigned int [3] sub_103498b0(unsigned int a0, unsigned int *idx, unsigned int a2, unsigned int a3, unsigned int a4, char *i, unsigned int a6)
{
    int v0;  // eax
    int v1;  // eax

    for (; a6 > 0; i += 1)
    {
        v1 = _INSERT(v0, 0, *(i));
        sub_1031a280(&a2);
        sub_10349ae0(v1);
        a6 -= 1;
        v0 = sub_1031a280(&a2);
    }
    *(idx) = a2;
    idx[1] = a3;
    idx[2] = a4;
    return idx;
}
```

## `sub_10349910` `0x10349910`

_74 bytes. (leaf/helper — see body)_

```c
unsigned int [3] sub_10349910(unsigned int a0, unsigned int *idx, unsigned int a2, unsigned int a3, unsigned int a4, char a5, unsigned int i)
{
    int v0;  // ecx

    while (i > 0)
    {
        v0 = _INSERT(0, 0, a5);
        sub_1031a280(&a2);
        sub_10349ae0(v0);
        i -= 1;
        sub_1031a280(&a2);
    }
    *(idx) = a2;
    idx[1] = a3;
    idx[2] = a4;
    return idx;
}
```

## `sub_10349960` `0x10349960`

_103 bytes. (leaf/helper — see body)_

```c
unsigned int [3] sub_10349960(unsigned int a0, unsigned int *idx, unsigned int a2, unsigned int a3, unsigned int a4, char *i, unsigned int a6)
{
    int v2;  // eax
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]

    for (; a6 > 0; i += 1)
    {
        v1 = a0 + 8;
        v0 = 0;
        v2 = sub_10318a60(*(i));
        sub_1031a280(&a2);
        sub_10349ae0(v2);
        a6 -= 1;
        sub_1031a280(&a2);
    }
    *(idx) = a2;
    idx[1] = a3;
    idx[2] = a4;
    return idx;
}
```

## `sub_103499d0` `0x103499d0`

_262 bytes. (leaf/helper — see body)_

```c
unsigned int [3] sub_103499d0(unsigned int a0, unsigned int *index, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int iter, unsigned int a6, char a7)
{
    unsigned int idx[3];  // eax
    unsigned int idx1[3];  // eax
    unsigned int v0;  // [bp-0x28]
    unsigned int v1[3];  // [bp-0x24]
    unsigned int v2[3];  // [bp-0x18]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    unsigned int v5;  // [bp+0x1c]

    while (true)
    {
        v4 = sub_10353a90(iter, 0, a6);
        v0 = (!v4 ? a6 : v4 - iter);
        v3 = v0;
        idx = sub_10349960(a0, v2, a2, a3, a4, iter, v3);
        a2 = idx[0];
        a3 = idx[1];
        a4 = idx[2];
        iter += v3;
        v5 = a6 - v3;
        if (a6 == v3)
            break;
        if (a7)
        {
            idx1 = sub_10349910(a0, v1, a2, a3, a4, a7, 1);
            a2 = idx1[0];
            a3 = idx1[1];
            a4 = idx1[2];
        }
        iter += 1;
        a6 = v5 - 1;
    }
    *(index) = a2;
    index[1] = a3;
    index[2] = a4;
    return index;
}
```

## `sub_10349ae0` `0x10349ae0`

_83 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    char field_4;
    char padding_5[3];
    struct struct_0 *field_8;
} struct_0;

typedef struct struct_0 {
    char padding_0[36];
    struct struct_1 *field_24;
    char padding_28[12];
    struct struct_1 *field_34;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

struct_0 * sub_10349ae0(struct_0 *a0, char a1)
{
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    if (a0->field_8)
    {
        v0 = _INSERT(a0, 0, a1);
        v2 = sub_1033ed20(a0->field_8);
        v1 = sub_1032fd20();
        if (!(char)sub_10312db0(&v1, &v2))
            return a0;
    }
    a0->field_4 = 1;
    return a0;
}
```

## `sub_10349b40` `0x10349b40`

_50 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_10349b40(unsigned int *i, unsigned int *a1, unsigned int *a2)
{
    for (; i != a1; i += 25)
    {
        sub_103469f0(a2, i);
        a2 += 25;
    }
    return a2;
}
```

## `sub_10349b80` `0x10349b80`

_29 bytes. (leaf/helper — see body)_

```c
int sub_10349b80(int a0, int a1, int a2, int a3)
{
    char v0;  // [bp+0x0]

    return sub_1034a5b0(a0, a1, a2, a3, &v0);
}
```

## `sub_10349ba0` `0x10349ba0`

_89 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10349ba0(int a0, int a1, unsigned int a2)
{
    int v5;  // eax
    char v0;  // [bp-0xb]
    char v1;  // [bp-0xa]
    char v2;  // [bp-0x9]
    unsigned int v3;  // [bp-0x8]

    v3 = a2 - (int)((a1 - a0) / 100) * 100;
    v2 = 0;
    v1 = 0;
    v5 = sub_10349d70(&/* unsupported instruction */, v0, v1, _INSERT(v3, 0, v2));
    sub_1034a610(a0, a1, v5);
    return v3;
}
```

## `sub_10349c00` `0x10349c00`

_31 bytes. (leaf/helper — see body)_

```c
int sub_10349c00(int a0, int a1)
{
    int v1;  // ecx
    char v0;  // [bp+0x0]

    sub_1034a640(a0, a1, _INSERT(0, 0, *((char *)((void*)&v1 + 3))), v1, &v0);
    return a0;
}
```

## `sub_10349c20` `0x10349c20`

_127 bytes. (leaf/helper — see body)_

```c
int sub_10349c20(int a0)
{
    char v0;  // [bp-0x5c]
    char v1;  // [bp-0x50]
    char v2;  // [bp-0x44]
    unsigned int v3;  // [bp-0x38]
    unsigned int v4;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    char v6;  // [bp-0x2c]
    char v7;  // [bp-0x13]
    char v8;  // [bp-0x12]
    char v9;  // [bp-0x11]
    char v10;  // [bp-0x10]
    char v11;  // [bp+0x8]
    char v12;  // [bp+0x14]
    char v13;  // [bp+0x20]

    sub_103412a0(&v13, &v10, sub_10344040(&v12, &v11));
    v9 = 0;
    v8 = 0;
    *((char *)&v5) = v9;
    v4 = v8;
    v3 = v7;
    sub_10349c00(&v2, &v13);
    sub_103413d0(&v1, &v12);
    sub_103413d0(&v0, &v11);
    sub_1034a660(&v6);
    sub_103413d0(a0, &v10);
    return a0;
}
```

## `sub_10349ca0` `0x10349ca0`

_66 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10349ca0(char a0, unsigned int a0, unsigned int a1, char a2, unsigned int a3, unsigned int a4, char *a5)
{
    unsigned int v2;  // eax
    int v3;  // eax
    char v0;  // [bp-0x10]

    while (true)
    {
        v2 = sub_1034a340(&/* unsupported instruction */);
        if (!(char)v2)
            break;
        v3 = _INSERT(v2, 0, *(a5));
        sub_10341280(&/* unsupported instruction */, &v0);
        sub_1034a280(v3, &/* unsupported instruction */);
        sub_1034a2e0();
    }
    return v2;
}
```

## `sub_10349cf0` `0x10349cf0`

_127 bytes. (leaf/helper — see body)_

```c
int sub_10349cf0(int a0)
{
    char v0;  // [bp-0x64]
    char v1;  // [bp-0x58]
    char v2;  // [bp-0x4c]
    unsigned int v3;  // [bp-0x40]
    unsigned int v4;  // [bp-0x3c]
    unsigned int v5;  // [bp-0x38]
    char v6;  // [bp-0x2c]
    char v7;  // [bp-0x13]
    char v8;  // [bp-0x12]
    char v9;  // [bp-0x11]
    char v10;  // [bp-0x10]
    char v11;  // [bp+0x8]
    char v12;  // [bp+0x14]
    char v13;  // [bp+0x20]

    sub_1034a300(&v10, sub_10344040(&v12, &v11));
    v9 = 0;
    v8 = 0;
    *((char *)&v5) = v9;
    v4 = v8;
    v3 = v7;
    sub_10349c00(&v2, &v13);
    sub_103413d0(&v1, &v12);
    sub_103413d0(&v0, &v11);
    sub_1034a6c0(&v6);
    sub_103413d0(a0, &v10);
    return a0;
}
```

## `sub_10349d70` `0x10349d70`

_24 bytes. (leaf/helper — see body)_

```c
char sub_10349d70(int a0)
{
    int v1;  // ecx
    int v2;  // eax
    char v0;  // [bp+0x0]

    v2 = _INSERT(0, 0, *((char *)((void*)&v1 + 3)));
    return sub_1034a720(a0, v2, v1, &v0);
}
```

## `sub_10349d90` `0x10349d90`

_73 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10349d90(int a0, unsigned int a1, int a2)
{
    int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v0 = a1 - a0 >> 2;
    v1 = a2 + v0 * 4;
    if (v0 > 0)
        sub_10353626(a2, v0 * 4, a0, v0 * 4);
    return v1;
}
```

## `sub_10349de0` `0x10349de0`

_78 bytes. (leaf/helper — see body)_

```c
char sub_10349de0(char a0, char a0, unsigned int a1, unsigned int a2)
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
    v6 = sub_10337970();
    *((char *)&v4) = v7;
    v3 = _INSERT(v6 CONCAT 0, 0, v6);
    v2 = a2;
    v1 = a1;
    v0 = sub_10349d70(&/* unsupported instruction */);
    return sub_1034a730(sub_10349d70(&/* unsupported instruction */));
}
```

## `sub_10349e30` `0x10349e30`

_36 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_10349e30(unsigned int *i, unsigned int *a1, unsigned int *a2)
{
    unsigned int *v0;  // eax

    for (; i != a1; i += 1)
    {
        *(i) = *(a2);
    }
    return v0;
}
```

## `sub_10349e60` `0x10349e60`

_64 bytes. (leaf/helper — see body)_

```c
char sub_10349e60(int a0, int a1, int a2, char a3)
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
    return sub_1034a750(a0, a1, a2, v8, v7, v6);
}
```

## `sub_10349ea0` `0x10349ea0`

_25 bytes. (leaf/helper — see body)_

```c
int sub_10349ea0(int a0, int a1, int a2)
{
    char v0;  // [bp+0x0]

    return sub_1034a7a0(a0, a1, a2, &v0);
}
```

## `sub_10349ec0` `0x10349ec0`

_238 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10349ec0(char *a0, unsigned int a1)
{
    unsigned long v13;  // ldt
    unsigned long v14;  // gdt
    unsigned short v15;  // fs
    unsigned long v16;  // 4136
    unsigned long v17;  // 4150
    unsigned int v19;  // eax
    unsigned long v20;  // 4113
    unsigned int v0;  // [bp-0x38]
    unsigned int v1;  // [bp-0x34]
    void* v2;  // [bp-0x30]
    void* v3;  // [bp-0x2c]
    unsigned int v4;  // [bp-0x28]
    unsigned int v5;  // [bp-0x24]
    void* v6;  // [bp-0x1c]
    void* v7;  // [bp-0x18]
    char v8;  // [bp-0x12]
    unsigned int v9;  // [bp-0x10]
    unsigned int v10;  // [bp-0xc]
    unsigned int v11;  // [bp-0x8]
    char v12;  // [bp-0x4]

    v11 = 4294967295;
    v10 = sub_10371440;
    v16 = _ccall(v13, v14, (unsigned int)v15, 0);
    v9 = *((int *)v16);
    v1 = g_1038e180 ^ &v12;
    v17 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int **)v17) = &v9;
    if ((char)sub_103315c0(a0))
    {
        if ((char)sub_103315c0(a1))
        {
            *((char *)&v0) = v8;
            v5 = sub_10314db0(&v7, (unsigned int)sub_103301b0(a1));
            v4 = v5;
            v11 = 0;
            sub_1034a260(v4);
            v11 = 4294967295;
            v19 = sub_103130c0(&v7);
        }
        else
        {
            v19 = sub_1033e300(a0);
        }
    }
    else
    {
        v19 = sub_103315c0(a1);
        if ((char)v19)
        {
            v3 = sub_10314db0(&v6, (unsigned int)sub_103301b0(a1));
            v2 = v3;
            v11 = 1;
            sub_10341930(a0, v2);
            v11 = 4294967295;
            v19 = sub_103130c0(&v6);
        }
    }
    v20 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int *)v20) = v9;
    return v19;
}
```

## `sub_10349fb0` `0x10349fb0`

_125 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int [25] sub_10349fb0(unsigned int a0, unsigned int *a1)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4141
    unsigned long v11;  // 4155
    unsigned long v12;  // 4124
    unsigned int v0;  // [bp-0x24]
    unsigned int v1[25];  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_10371471;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v0 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    v2 = sub_1031acf0(100, a0);
    v5 = 0;
    v1 = (!v2 ? 0 : sub_10341320(v2, a1));
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v3;
    return v1;
}
```

## `sub_1034a030` `0x1034a030`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1034a030(int a0, int a1, char a2)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4141
    unsigned int v8;  // eax
    unsigned long v9;  // 4157
    int v10;  // eax
    unsigned long v11;  // 4123
    int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v8 = *((int *)v7);
    v1 = *((int *)v7);
    v0 = a0;
    v9 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v9) = &v1;
    v10 = _INSERT(&v1, 0, a2);
    sub_1034a7e0(a1, v10, g_1038e180 ^ &v2, a0, v8, sub_10371498, -1, &v3);
    v11 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v11) = v8;
    return a0;
}
```

## `sub_1034a090` `0x1034a090`

_370 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern unsigned int g_1038e180;

struct_0 ** sub_1034a090(struct_0 **a0, unsigned int a1)
{
    unsigned long v15;  // ldt
    unsigned long v16;  // gdt
    unsigned short v17;  // fs
    unsigned long v18;  // 4149
    unsigned long v19;  // 4171
    char v20;  // al
    struct_0 *v21;  // eax
    unsigned long v22;  // 4123
    unsigned int v0;  // [bp-0x64]
    unsigned int v1;  // [bp-0x54]
    unsigned int v2;  // [bp-0x50]
    unsigned int v3;  // [bp-0x4c]
    char v4;  // [bp-0x40]
    struct_0 v5;  // [bp-0x34]
    struct_0 **v6;  // [bp-0x28]
    unsigned int v7;  // [bp-0x24]
    struct_0 v8;  // [bp-0x20]
    unsigned int v9;  // [bp-0x18]
    char *v10;  // [bp-0x14], Other Possible Types: struct_0 **
    unsigned int v11;  // [bp-0x10]
    unsigned int v12;  // [bp-0xc]
    char v13;  // [bp-0x8], Other Possible Types: unsigned int
    char v14;  // [bp-0x4]

    v13 = 4294967295;
    v12 = sub_103714d0;
    v18 = _ccall(v15, v16, (unsigned int)v17, 0);
    v11 = *((int *)v18);
    v10 = a0;
    v0 = g_1038e180 ^ &v14;
    v19 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int **)v19) = &v11;
    v10 = &v0;
    v9 = 0;
    sub_103454a0(&v8, a0);
    v13 = 0;
    if ((char)sub_103455c0(&v8))
    {
        v3 = sub_10314d40((char *)a0 + *(a0)->field_4, &v6);
        v2 = v3;
        v13 = 1;
        v7 = sub_10347eb0(v2);
        v13 = 0;
        sub_103130c0(&v6);
        v13 = 2;
        v1 = (!a0 ? NULL : (struct_0 **)((char *)a0 + *(a0)->field_4));
        v20 = sub_10345220((char *)a0 + *(a0)->field_4);
        v21 = sub_10347e60(&v5, sub_10315c20((char *)a0 + *(a0)->field_4));
        if ((char)sub_103455c0(sub_10347e10(v7, &v4, v21->padding_0, v21->field_4, v21[1].padding_0, v1, v20, a1)))
            v9 |= 4;
        v13 = 0;
    }
    sub_10314630((char *)a0 + *(a0)->field_4, v9, 0);
    v13 = 4294967295;
    sub_10345550(&v8);
    v22 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int *)v22) = v11;
    return a0;
}
```

## `sub_1034a1b9` `0x1034a1b9`

_33 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

int sub_1034a1b9(void)
{
    struct_0 **v1;  // [bp+0xfffc0]
    unsigned int v2;  // [bp+0x100000]

    sub_10314630((char *)v1 + *(v1)->field_4, 4, 1);
    v2 = 0;
    return "j";
}
```

## `sub_1034a230` `0x1034a230`

_36 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[48];
    char field_30;
} struct_0;

int sub_1034a230(struct_0 *idx, char a1)
{
    char v0;  // [bp-0x5]

    v0 = idx->field_30;
    idx->field_30 = a1;
    return _INSERT(idx, 0, v0);
}
```

