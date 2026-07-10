# elfbot.dll decompiled — jiru 0x1031fc10..0x10320c39

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1031fc10` `0x1031fc10`

_58 bytes. (leaf/helper — see body)_

```c
int sub_1031fc10(unsigned int a0, int a1)
{
    unsigned int v0;  // [bp-0x10]

    v0 = a0;
    sub_1031a280(&v0);
    sub_103147d0(a0);
    sub_1031a3c0(a0, 0, 0);
    sub_1031fc70(a1);
    return a0;
}
```

## `sub_1031fc50` `0x1031fc50`

_19 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

struct_0 * sub_1031fc50(struct_0 *a0)
{
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_1031a4a0(v0);
}
```

## `sub_1031fc70` `0x1031fc70`

_38 bytes. (leaf/helper — see body)_

```c
int sub_1031fc70(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_1031fcc0(a1, sub_1031fca0(a1, a0, &v1));
}
```

## `sub_1031fca0` `0x1031fca0`

_17 bytes. (leaf/helper — see body)_

```c
int sub_1031fca0(int a0)
{
    char v0;  // [bp+0x0]

    return sub_103530d4(a0, &v0);
}
```

## `sub_1031fcc0` `0x1031fcc0`

_134 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

struct_0 * sub_1031fcc0(struct_0 *a0, int a1, unsigned int a2)
{
    unsigned int v2;  // eax
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    if ((char)sub_1031fd50(a1, a0, &v1))
        return sub_1031e7a0(a0, a0, a1 - (char *)sub_1031a4a0(a0) >> 1, a2);
    if (!(char)sub_1031e940(a0, a2, 0))
        return a0;
    v2 = sub_1031a4a0(a0);
    sub_1031a9b0(v2, a0->field_18, a1, a2);
    sub_1031a440(a0, a2);
    return a0;
}
```

## `sub_1031fd50` `0x1031fd50`

_54 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

char sub_1031fd50(struct_0 *a0, struct_0 *a1)
{
    struct_0 *v1;  // eax
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    if (a1 >= sub_1031a4a0(v0))
    {
        v1 = sub_1031a4a0(v0);
        if (&v1->padding_0[2 * *((int *)&v0->padding_8[12])] > a1)
            return 1;
    }
    return 0;
}
```

## `sub_1031fd7e` `0x1031fd7e`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1031fd7e(void)
{
}
```

## `sub_1031fd90` `0x1031fd90`

_267 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern int g_10390230;

int sub_1031fd90(unsigned int a0)
{
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    unsigned short v14;  // fs
    unsigned long v15;  // 4141
    unsigned long v16;  // 4158
    unsigned long v17;  // 4114
    int v0;  // [bp-0x80]
    int v1;  // [bp-0x7c]
    int v2;  // [bp-0x78]
    int v3;  // [bp-0x74]
    unsigned int v4;  // [bp-0x70]
    char v5;  // [bp-0x6c]
    char v6;  // [bp-0x34]
    int v7;  // [bp-0x14]
    unsigned int v8;  // [bp-0x10]
    unsigned int v9;  // [bp-0xc]
    unsigned int v10;  // [bp-0x8], Other Possible Types: char
    char v11;  // [bp-0x4]

    v10 = 4294967295;
    v9 = sub_1036b901;
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    v8 = *((int *)v15);
    v7 = g_1038e180 ^ &v11;
    v16 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v16) = &v8;
    v4 = 0;
    sub_1032bd50(&v6, 0, v7);
    v10 = 1;
    if (sub_1032e0a0(v7))
    {
        v3 = sub_10325740(sub_1032e0e0());
        v2 = v3;
        v10 = 2;
        v1 = sub_103256e0(&v5, v2);
        v0 = v1;
        v10 = 3;
        sub_10325880(v0);
        v4 |= 1;
        v10 = 2;
        sub_1031a3a0(&v5);
        v10 = 1;
        sub_103257d0();
        v10 = 0;
        sub_1031a0e0(&v6);
    }
    else
    {
        sub_10325820(g_10390230);
        v4 |= 1;
        v10 = 0;
        sub_1031a0e0(&v6);
    }
    v17 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int *)v17) = v8;
    return sub_10351225();
}
```

## `sub_1031fe59` `0x1031fe59`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1031fe59(void)
{
    sub_1031fe84();
    return;
}
```

## `sub_1031fe84` `0x1031fe84`

_12 bytes. (leaf/helper — see body)_

```c
int sub_1031fe84(void)
{
    char v1;  // [bp+0x100000]

    v1 = 0;
    sub_1031a0e0(/* unsupported instruction */ - 48);
}
```

## `sub_1031feb0` `0x1031feb0`

_165 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b0b0;
extern struct_0 *g_1038b0b4;
extern struct_0 *g_1038b1cc;
extern unsigned int g_1038e180;

char sub_1031feb0(int a0)
{
    char v0;  // [bp-0x46c]
    unsigned short *v1;  // [bp-0x260]
    char v2;  // [bp-0x25c]
    char v3;  // [bp-0x230]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]

    v4 = g_1038e180 ^ &v6;
    if (g_1038b1cc(0, &v0, 260))
    {
        v5 = g_1038b0b4(&v0, &v2);
        if (v5 != 4294967295)
        {
            g_1038b0b0(v5);
            sub_10352da8(a0, &v3);
            v1 = sub_103124e0(a0, 46);
            if (v1)
                *(v1) = 0;
        }
    }
    return sub_10351225();
}
```

## `sub_1031ff60` `0x1031ff60`

_33 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b0b8;

int sub_1031ff60(unsigned int a0, unsigned int a1)
{
    char v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]

    g_1038b0b8(a0, a1, &v0, 28);
    return v1;
}
```

## `sub_1031ff90` `0x1031ff90`

_268 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    int field_0;
    int field_4;
    int field_8;
    unsigned int field_c;
} struct_0;

extern unsigned int g_103a290c;
extern unsigned int g_103a2914;

char sub_1031ff90(int a0, int a1, int a2, int a3)
{
    int v6;  // eax
    int v7;  // eax
    unsigned int v0;  // [bp-0x1c]
    struct_0 *v1;  // [bp-0x18]
    int v2;  // [bp-0x14]
    struct_0 *idx;  // [bp-0x10]
    int v4;  // [bp-0xc]
    int index;  // [bp-0x8]

    v6 = a1 - g_103a2914;
    index = v6 + (v6 >> 31 & 0xfff) >> 12;
    v7 = a1 - g_103a2914 + a2 - 1;
    v4 = v7 + (v7 >> 31 & 0xfff) >> 12;
    if (index == v4)
    {
        v1 = sub_10350a53(16);
        idx = v1;
        idx->field_c = *((int *)(g_103a290c + index * 4));
        *((struct_0 **)(g_103a290c + index * 4)) = idx;
        idx->field_4 = a1;
        idx->field_8 = a2;
        v0 = sub_1034fef0(a2);
        idx->field_0 = v0;
        sub_10350b50(idx->field_0, a3, a2);
        return 1;
    }
    v2 = v4 * 0x1000 + g_103a2914 - a1;
    sub_1031ff90(a0, a1, v2, a3);
    sub_1031ff90(a0, a1 + v2, a2 - v2, a3 + v2);
    return 1;
}
```

## `sub_103200a0` `0x103200a0`

_107 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a2914;

int sub_103200a0(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v12;  // 4109
    unsigned int v13;  // 4199
    unsigned int v14;  // id
    unsigned int v15;  // ac
    unsigned int v16;  // ebx
    unsigned int v17;  // esi
    unsigned int v18;  // edi
    unsigned int v19;  // 4110
    unsigned int v0;  // [bp-0x40]
    unsigned int v1;  // [bp-0x3c]
    char *v2;  // [bp-0x38]
    char *v3;  // [bp-0x34]
    unsigned int v4;  // [bp-0x30]
    unsigned int v5;  // [bp-0x2c]
    unsigned int v6;  // [bp-0x28]
    unsigned int v7;  // [bp-0x24]
    unsigned int v8;  // [bp-0x20]
    unsigned int v9;  // [bp-0x20]
    char v10;  // [bp-0x1c]
    char v11;  // [bp-0x4]

    v12 = _ccall(0, 6, &v10, 24, 0);
    g_103a2914 = a2;
    v8 = a0;
    v7 = a2;
    v13 = _ccall(6, &v11, 24, 0);
    v9 = v13 | 0x202 | v14 * 0x200000 & 0x200000 | v15 * 0x40000 & 0x40000;
    v6 = v8;
    v5 = a1;
    v4 = v16;
    v3 = &v9;
    v2 = &v11;
    v1 = v17;
    v0 = v18;
    if (!(1))
        goto LABEL_103200e0;
LABEL_103200e0:
    for (; (v19 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v19 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
}
```

## `sub_103200ac` `0x103200ac`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103200ac(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103200db` `0x103200db`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103200db(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103200e2` `0x103200e2`

_3 bytes. (leaf/helper — see body)_

```c
void sub_103200e2(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10320110` `0x10320110`

_50 bytes. (leaf/helper — see body)_

```c
int sub_10320110(void)
{
    unsigned int v22;  // cc_op
    unsigned int v23;  // cc_dep1
    unsigned int v24;  // cc_dep2
    unsigned int v25;  // cc_ndep

    if (!(1))
        goto LABEL_1032012c;
LABEL_1032012c:
    v22 = 15;
    v23 = 3;
    v24 = 0;
    v25 = 0;
}
```

## `sub_10320136` `0x10320136`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10320136(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032014a` `0x1032014a`

_106 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

extern unsigned int g_103a291c;

int sub_1032014a(void)
{
    unsigned int v7;  // 4097
    unsigned int v8;  // eax
    unsigned int v9;  // 4110
    struct_0 *v1;  // [bp+0x8]
    char *v2;  // [bp+0xc]
    unsigned int v3;  // [bp+0x14]
    unsigned int v4;  // [bp+0x18]
    unsigned int v5;  // [bp+0x1c]
    unsigned int v6;  // [bp+0x20]

    v7 = v6;
    v8 = v5 * 0x1000000 | v5 * 0x100 & 0xff0000 | v5 >> 8 & 0xff00 | v5 >> 24 & 0xff;
    g_103a291c = v1->field_14;
    v6 = ~(~(v4));
    v5 = v8 * 0x1000000 | v8 * 0x100 & 0xff0000 | v8 >> 8 & 0xff00 | v8 >> 24 & 0xff;
    v6 = v7 & 2261 | 0x202 | ((char)(v7 >> 10) ? 4294967295 : 1) & 0x400 | ((char)(v7 >> 21) ? 1 : 0) * 0x200000 & 0x200000 | ((char)(v7 >> 18) ? 1 : 0) * 0x40000 & 0x40000;
    v4 = v6;
    v3 = g_103a291c;
    v2 = &v6;
    if (!(1))
        goto LABEL_1032018b;
LABEL_1032018b:
    for (; (v9 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v9 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
}
```

## `sub_1032014e` `0x1032014e`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032014e(void)
{
}
```

## `sub_10320150` `0x10320150`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10320150(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10320186` `0x10320186`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10320186(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032018d` `0x1032018d`

_3 bytes. (leaf/helper — see body)_

```c
void sub_1032018d(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103201bb` `0x103201bb`

_202 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
} struct_0;

extern struct_0 *g_103a2928;
extern unsigned int g_103a2930;
extern unsigned int g_103a2934;
extern unsigned int g_103a2938;

int sub_103201bb(void)
{
    char v15;  // bh
    char v16;  // dl
    unsigned int v25;  // 4101
    unsigned int v26;  // 4103
    unsigned int v27;  // 4101
    unsigned int v28;  // 4101
    unsigned int v29;  // 4101
    unsigned int v30;  // 4101
    unsigned int v31;  // 4101
    unsigned int v32;  // 4101
    unsigned int v33;  // edx
    unsigned int v34;  // ebx
    unsigned int v17;  // ebx
    unsigned int v35;  // ebp
    unsigned int v36;  // ecx
    char *v37;  // eax
    unsigned int v38;  // ecx
    char *v40;  // eax
    unsigned int v41;  // 4110
    unsigned int v42;  // id
    unsigned int v43;  // ac
    unsigned int v44;  // cc_op
    unsigned int v18;  // ecx
    unsigned int v45;  // 4104
    unsigned int v46;  // cc_dep1
    unsigned int v47;  // cc_dep2
    unsigned int v51;  // 4101
    unsigned int v19;  // edi
    unsigned int v20;  // edi
    unsigned int v21;  // eax
    unsigned int v22;  // eax
    unsigned int v23;  // edx
    unsigned int v24;  // esi
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    char *v3;  // [bp-0x18], Other Possible Types: unsigned int
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    char *v7;  // [bp-0x8], Other Possible Types: unsigned int
    char *v8;  // [bp-0x4], Other Possible Types: unsigned int
    unsigned int v10;  // [bp+0x4]
    char *v11;  // [bp+0xffff4]
    unsigned int v12;  // [bp+0xffff8]
    unsigned int v13;  // [bp+0xffffc]

    v17 = _INSERT(0, 1, v15 + v16);
    if (v18 == 1)
    {
        v20 = v19 * 0x2000000;
        v22 = sub_1034fef0(v18 - 1 | v21);
    }
    v13 = v22;
    g_103a2930 = v13;
    v8 = g_103a2930;
    v7 = v18;
    v6 = v23;
    v5 = v17;
    v3 = /* unsupported instruction */;
    v2 = v24;
    v1 = v20;
LABEL_103201f5:
    v25 = _ccall(0, 15, 0, 0, 0);
    if ((char)v25)
        goto LABEL_103201f7;
    else
        goto LABEL_103201f8;
    while (true)
    {
LABEL_103201f7:
        __unsupported_jumpkind_Ijk_NoDecode()
        while (true)
        {
LABEL_103201f8:
            v26 = _ccall(10, 15, 0, 0, 0);
            if ((char)v26)
            {
                v27 = _ccall(8, 15, 0, 0, 0);
                if (!((char)v27))
                {
                    if (!(1))
                        goto LABEL_103201fd;
                    v28 = _ccall(10, 15, 0, 0, 0);
                    if (!((char)v28))
                    {
                        v29 = _ccall(0, 15, 0, 0, 0);
                        if ((char)v29)
                            break;
                        else
                            continue;
                    }
                    v30 = _ccall(8, 15, 0, 0, 0);
                    if ((char)v30)
                        goto LABEL_103201f5;
                    goto LABEL_103201fe;
                }
                __unsupported_jumpkind_Ijk_NoDecode()
                v31 = _ccall(8, 15, 0, 0, 0);
                if (!((char)v31))
                    goto LABEL_103201fe;
LABEL_103201f5:
                if ((v32 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v32))
                    break;
            }
            else
            {
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_103201fd:
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_103201fe:
                v33 = v6;
                v34 = v5;
                v35 = v3;
                v36 = 0;
                v37 = &g_103a2928->field_0;
                do
                {
                    *(v37) = *(v37) + *((char *)&v37);
                    v38 = _INSERT(v36, 0, (v37 * v33 >= 0x80000000 ? 1 : 0));
                    v8 = -(v38) | v37 * v33;
                    v12 = sub_1034fef0(-(v38) | v37 * v33);
                    g_103a2934 = v12;
                    v11 = sub_1034fef0(-((g_103a2928 >= 0x20000000 ? 1 : 0) & 1) | g_103a2928 * 4);
                    v40 = v11;
                    g_103a2938 = v40;
                    v8 = v40;
                    v37 = v8;
                    if (&v10 >= NULL)
                        goto LABEL_10320264;
LABEL_10320264:
                    v41 = _ccall(3, &v8, 4, 0);
                    v8 = v41 | 0x202 | v42 * 0x200000 & 0x200000 | v43 * 0x40000 & 0x40000;
                    v7 = v37;
                    v6 = v18;
                    v5 = v23;
                    v4 = v34;
                    v3 = &v8;
                    v2 = v35;
                    v1 = v2;
                    v0 = v1;
                    __unsupported_jumpkind_Ijk_NoDecode()
                    v44 = 6;
                    v33 = 0;
                    v45 = _ccall(0, 6, v23, v23, 0);
                    v46 = v23;
                    v47 = v23;
                    if ((char)v45)
                        break;
                    if (!(1))
                        goto LABEL_10320271;
LABEL_10320271:
                    v34 = 0;
                    v44 = 15;
                    v36 = 3;
                    v46 = 3;
                    v47 = 0;
                } while (false);
                v51 = _ccall(2, v44, v46, v47, 0);
                if ((char)v51)
                    goto LABEL_0x10320282;
            }
        }
    }
}
```

## `sub_103201eb` `0x103201eb`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103201eb(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032022e` `0x1032022e`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1032022e(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032027b` `0x1032027b`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1032027b(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032028f` `0x1032028f`

_82 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a293c;

int sub_1032028f(void)
{
    unsigned int v8;  // 4097
    unsigned int v9;  // eax
    unsigned int v10;  // 4110
    unsigned int v11;  // edx
    unsigned int v13;  // 4104
    unsigned int v14;  // cc_dep1
    unsigned int v15;  // cc_dep2
    unsigned int v17;  // 4101
    void* v1;  // [bp+0x8]
    char *v2;  // [bp+0xc]
    unsigned int v3;  // [bp+0x14]
    unsigned int v4;  // [bp+0x18]
    unsigned int v5;  // [bp+0x1c]
    unsigned int v6;  // [bp+0x20]
    char v7;  // [bp+0x28]

    v8 = v6;
    v9 = sub_1034fef0(0x1000);
    *((unsigned int *)&v1[20]) = v9;
    g_103a293c = (int)v1[20];
    v6 = v9;
    if (&v7 >= NULL)
        goto LABEL_103202c1;
LABEL_103202c1:
    v10 = _ccall(3, &v6, 4, 0);
    v6 = v10 | 0x202 | ((char)(v8 >> 10) ? 4294967295 : 1) & 0x400 | ((char)(v8 >> 21) ? 1 : 0) * 0x200000 & 0x200000 | ((char)(v8 >> 18) ? 1 : 0) * 0x40000 & 0x40000;
    v5 = v6;
    v4 = g_103a293c;
    v3 = v11;
    v2 = &v6;
    v13 = _ccall(0, 6, v11, v11, 0);
    v14 = v11;
    if (!((char)v13))
    {
        __unsupported_jumpkind_Ijk_NoDecode()
        if (0)
            goto LABEL_0x10320266;
        v17 = _ccall(2, 15, 3, 0, 0);
        if ((char)v17)
            goto LABEL_0x103202df;
    }
    else
    {
        v17 = _ccall(2, 6, v14, v15, 0);
        if ((char)v17)
            goto LABEL_0x103202df;
    }
}
```

## `sub_10320293` `0x10320293`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10320293(void)
{
}
```

## `sub_10320295` `0x10320295`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10320295(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103202d8` `0x103202d8`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103202d8(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103202ec` `0x103202ec`

_190 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a290c;
extern unsigned int g_103a2928;
extern unsigned int g_103a2930;
extern unsigned int g_103a2934;
extern unsigned int g_103a2938;

int sub_103202ec(void)
{
    void* v10;  // ebp
    unsigned int v11;  // eax
    unsigned int v20;  // 4101
    unsigned int v21;  // 4101
    unsigned int v22;  // 4101
    unsigned int v23;  // 4101
    unsigned int v24;  // 4101
    unsigned int idx;  // eax
    void* v26;  // ebp
    unsigned int v27;  // 4106
    unsigned int v28;  // 4115
    unsigned int v12;  // ecx
    unsigned int v13;  // edx
    unsigned int v14;  // cc_op
    unsigned int v15;  // cc_dep1
    unsigned int v16;  // cc_dep2
    unsigned int v17;  // 4101
    unsigned int v18;  // 4103
    unsigned int v19;  // 4101
    unsigned int v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x4]
    void* v2;  // [bp+0x8], Other Possible Types: unsigned int
    void* v3;  // [bp+0xc]
    char *v4;  // [bp+0x10], Other Possible Types: unsigned int
    unsigned int v5;  // [bp+0x14]
    unsigned int v6;  // [bp+0x18]
    unsigned int v7;  // [bp+0x1c]
    unsigned int v8;  // [bp+0x20]
    char v9;  // [bp+0x24]

    v10 = v2;
    *((unsigned int *)&v10[24]) = sub_1034fef0(-((g_103a2928 >= 0x20000000 ? 1 : 0) & 1) | g_103a2928 * 4);
    v11 = (int)v10[24];
    g_103a290c = v11;
    v8 = v11;
    v7 = v12;
    v6 = v13;
    v5 = v4;
    v4 = &v9;
    v3 = v10;
    v2 = v1;
    v1 = v0;
    v14 = 15;
    v15 = 0;
    v16 = 0;
LABEL_10320342:
    v17 = _ccall(0, 15, 0, 0, 0);
    if ((char)v17)
        goto LABEL_10320344;
    else
        goto LABEL_10320345;
    while (true)
    {
LABEL_10320344:
        __unsupported_jumpkind_Ijk_NoDecode()
        while (true)
        {
LABEL_10320345:
            v18 = _ccall(10, 15, 0, 0, 0);
            if ((char)v18)
            {
                v19 = _ccall(8, 15, 0, 0, 0);
                if (!((char)v19))
                {
                    v14 = 15;
                    v15 = 0;
                    v16 = 0;
                    if (!(1))
                        goto LABEL_1032034a;
                    v20 = _ccall(10, 15, 0, 0, 0);
                    if (!((char)v20))
                    {
                        v21 = _ccall(0, 15, 0, 0, 0);
                        if ((char)v21)
                            break;
                        else
                            continue;
                    }
                    v22 = _ccall(8, 15, 0, 0, 0);
                    if ((char)v22)
                        goto LABEL_10320342;
                    goto LABEL_1032034b;
                }
                __unsupported_jumpkind_Ijk_NoDecode()
                v23 = _ccall(8, 15, 0, 0, 0);
                if (!((char)v23))
                    goto LABEL_1032034b;
LABEL_10320342:
                if ((v24 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v24))
                    break;
            }
            else
            {
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_1032034a:
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_1032034b:
                idx = v8;
                v26 = v3;
                *((unsigned int *)&v26[4]) = 0;
                while (true)
                {
                    v27 = _ccall(v14, v15, v16, 0);
                    v28 = _ccall(12, 9, idx, &g_103a2928 ^ v27 & 1, v27 & 1);
                    if (!((char)v28))
                        break;
                    *((unsigned int *)(g_103a2930 + (int)v26[4] * 4)) = 4294967295;
                    *((unsigned int *)(g_103a2934 + (int)v26[4] * 4)) = 0;
                    *((unsigned int *)(g_103a2938 + (int)v26[4] * 4)) = 4294967295;
                    idx = (int)v26[4];
                    *((unsigned int *)(g_103a290c + idx * 4)) = 0;
                    v14 = 3;
                    v15 = (int)v26[4];
                    v16 = 1;
                    *((unsigned int *)&v26[4]) = (int)v26[4] + 1;
                }
                return;
            }
        }
    }
}
```

## `sub_103202f0` `0x103202f0`

_2 bytes. (leaf/helper — see body)_

```c
void sub_103202f0(void)
{
}
```

## `sub_103202f2` `0x103202f2`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103202f2(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10320338` `0x10320338`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10320338(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103203b0` `0x103203b0`

_134 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a290c;
extern unsigned int g_103a2910;
extern unsigned int g_103a2930;
extern unsigned int g_103a2934;
extern unsigned int g_103a2938;
extern unsigned int g_103a293c;

int sub_103203b0(void)
{
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v5 = g_103a2930;
    sub_10350eb5(v5);
    v4 = g_103a2910;
    sub_10350eb5(v4);
    v3 = g_103a2934;
    sub_10350eb5(v3);
    v2 = g_103a2938;
    sub_10350eb5(v2);
    v1 = g_103a293c;
    sub_10350eb5(v1);
    v0 = g_103a290c;
    return sub_10350eb5(v0);
}
```

## `sub_10320440` `0x10320440`

_774 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

extern struct_0 *g_1038b03c;
extern struct_0 *g_1038b050;
extern struct_0 *g_1038b088;
extern struct_0 *g_1038b08c;
extern struct_0 *g_1038b1b4;
extern struct_0 *g_1038b2c8;
extern struct_0 *g_1038b2e0;
extern struct_0 *g_1038b304;
extern struct_0 *g_1038b348;
extern struct_0 *g_1038b34c;
extern unsigned int g_1038e180;
extern int g_103a2ad0;

int sub_10320440(int a0)
{
    unsigned long v25;  // ldt
    unsigned long v26;  // gdt
    unsigned int v35;  // eax
    unsigned int v36;  // eax
    unsigned long v38;  // 4120
    unsigned short v27;  // fs
    unsigned long v28;  // 4150
    unsigned int v29;  // ecx
    unsigned int v30;  // eax
    unsigned long v31;  // 4175
    unsigned int v32;  // edi
    unsigned int v33;  // esi
    unsigned int v34;  // ebx
    unsigned int v0;  // [bp-0x270]
    unsigned int v1;  // [bp-0x260]
    unsigned int v2;  // [bp-0x25c]
    unsigned int v3;  // [bp-0x258]
    char v4;  // [bp-0x254]
    char v5;  // [bp-0x1f4]
    char v6;  // [bp-0x194]
    int v7;  // [bp-0x178]
    int v8;  // [bp-0x174]
    int v9;  // [bp-0x174]
    unsigned int v10;  // [bp-0x170]
    char v11;  // [bp-0x16c]
    unsigned int v12;  // [bp-0x168]
    unsigned int v13;  // [bp-0x15c]
    struct_0 *v14;  // [bp-0x148]
    int v15;  // [bp-0x140]
    char v16;  // [bp-0x13c]
    struct_0 v17;  // [bp-0x38]
    unsigned int v18;  // [bp-0x1c]
    char *iter;  // [bp-0x18]
    char *v20;  // [bp-0x14], Other Possible Types: unsigned int
    unsigned int v21;  // [bp-0x10]
    unsigned int v22;  // [bp-0xc]
    char v23;  // [bp-0x8], Other Possible Types: unsigned int
    char v24;  // [bp-0x4]

    v23 = 4294967295;
    v22 = sub_1036b944;
    v28 = _ccall(v25, v26, (unsigned int)v27, 0);
    v21 = *((int *)v28);
    v20 = v29;
    v30 = g_1038e180 ^ &v24;
    v18 = v30;
    v0 = v30;
    v31 = _ccall(v25, v26, (unsigned int)v27, 0);
    *((unsigned int **)v31) = &v21;
    v20 = &v0;
    v35 = g_1038b08c(2, v30, v32, v33, v34);
    g_1038b088(v35);
    do
    {
        if (!(char)sub_10320780(a0))
            goto LABEL_103204ca;
        else
            goto LABEL_0x103204a0;
    } while (g_1038b304(a0, 500) == 258);
    g_1038b1b4(250);
LABEL_103204ca:
    if ((char)sub_10320780(a0))
    {
        g_1038b304(a0, 30000);
        g_1038b1b4(500);
        v36 = sub_10320760(0);
        sub_1033a4c0(v36 ^ g_1038b03c());
        v8 = sub_102eb8f0(&v15, 10) + 4;
        iter = &v16;
        while (true)
        {
            v9 = v8 - 1;
            if (!v8)
                break;
            v7 = sub_102eb8f0(&v15, 52);
            *(iter) = (-(v7 < 26) & 32) + 65 + (unsigned int)(v7 % 26);
            iter += 1;
            v8 = v9;
        }
        *(iter) = 0;
        v2 = sub_103266a0(&v16, &v17);
        v1 = v2;
        v23 = 0;
        sub_10326c30(&v16, &v17);
        v23 = 2;
        sub_10319f00(&v5);
        sub_10350ad0(&v11, 0, 40);
        v12 = sub_103207b0;
        v13 = g_1038b050(0);
        v14 = sub_1031fc50(&v17);
        sub_1032af80(&v11);
        sub_1031e1d0(&v4, &v17);
        v23 = 3;
        v10 = sub_1032b300(0, &v4, &g_103a2ad0, 0xcf0000, -0x80000000, -0x80000000, -0x80000000, -0x80000000, 0, 0, g_1038b050(0, 0));
        v23 = 2;
        sub_10319f00(&v4);
        g_1038b2e0(v10, 1, 10000, 0);
        v23 = 4;
        while ((char)sub_10320780(a0) && g_1038b2c8(&v6, 0, 0, 0) > 0)
        {
            g_1038b348(&v6);
            g_1038b34c(&v6);
        }
        v23 = 2;
        v3 = 0;
        v23 = 4294967295;
        sub_1031a3a0(&v17);
    }
    v38 = _ccall(v25, v26, (unsigned int)v27, 0);
    *((unsigned int *)v38) = v21;
    return sub_10351225();
}
```

## `sub_103204c8` `0x103204c8`

_2 bytes. (leaf/helper — see body)_

```c
void sub_103204c8(void)
{
}
```

## `sub_10320704` `0x10320704`

_13 bytes. (leaf/helper — see body)_

```c
extern char g_1032071e;

int sub_10320704(void)
{
    unsigned int v1;  // [bp+0x100000]

    v1 = 2;
    return &g_1032071e;
}
```

## `sub_10320711` `0x10320711`

_6 bytes. (leaf/helper — see body)_

```c
extern char g_10320717;

int sub_10320711(void)
{
    return &g_10320717;
}
```

## `sub_10320760` `0x10320760`

_17 bytes. (leaf/helper — see body)_

```c
int sub_10320760(int a0)
{
    char v0;  // [bp+0x0]

    return sub_1035410c(a0, &v0);
}
```

## `sub_10320780` `0x10320780`

_35 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b0bc;
extern unsigned int g_103a2900;

int sub_10320780(unsigned int a0)
{
    char v0;  // [bp+0x0]

    g_1038b0bc(a0, &g_103a2900, &v0);
    return g_103a2900 == 259;
}
```

## `sub_103207b0` `0x103207b0`

_833 bytes. refs "Shutdown", "Shutdown"_

```c
typedef struct struct_1 {
    unsigned int field_0;
    char padding_4[8];
    unsigned int field_c;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b03c;
extern struct_0 *g_1038b0c0;
extern struct_0 *g_1038b0c4;
extern struct_0 *g_1038b1b8;
extern struct_0 *g_1038b1bc;
extern struct_0 *g_1038b2c0;
extern struct_0 *g_1038b2c4;
extern struct_0 *g_1038b2fc;
extern unsigned int g_1038c7f4;
extern unsigned int g_1038c808;
extern unsigned int g_1038c834;
extern struct_1 *g_1038c8ac;
extern unsigned int g_1038e180;
extern char g_103a26a4;
extern char g_103a2905;
extern char g_103a2909;
extern char g_103a290b;
extern unsigned int g_103a2910;
extern unsigned int g_103a2914;
extern unsigned int g_103a2920;
extern char g_103a2928;
extern unsigned int g_103a2934;
extern int g_103a2970;

int sub_103207b0(int a0, int a1, unsigned int a2, int a3)
{
    unsigned int v25;  // edx
    unsigned int v26;  // ebx
    unsigned int v35;  // ecx
    unsigned int v36;  // esi
    unsigned int v37;  // edi
    unsigned int v39;  // 4104
    unsigned int v40;  // cc_dep1
    unsigned int v43;  // 4101
    unsigned int v44;  // eax
    unsigned int v27;  // ebx
    unsigned int v29;  // eax
    unsigned int v30;  // edx
    unsigned int v31;  // edx
    unsigned int v32;  // 4110
    unsigned int v33;  // id
    unsigned int v34;  // ac
    unsigned int v0;  // [bp-0x10ac]
    unsigned int v1;  // [bp-0x10a8]
    char *v2;  // [bp-0x10a4]
    char *v3;  // [bp-0x10a0]
    unsigned int v4;  // [bp-0x109c]
    unsigned int v5;  // [bp-0x1098]
    unsigned int v6;  // [bp-0x1094]
    unsigned int v7;  // [bp-0x1090]
    unsigned int v8;  // [bp-0x108c]
    unsigned int v9;  // [bp-0x108c]
    int idx;  // [bp-0x1038]
    char v11;  // [bp-0x1034]
    unsigned int v12;  // [bp-0x34]
    unsigned int v13;  // [bp-0x30]
    char v14;  // [bp-0x2c]
    int j;  // [bp-0x28]
    char v16;  // [bp-0x21]
    unsigned int v17;  // [bp-0x20]
    unsigned int v18;  // [bp-0x1c]
    int v19;  // [bp-0x18]
    unsigned int v20;  // [bp-0x14]
    unsigned int v21;  // [bp-0x10]
    char v22;  // [bp-0xc], Other Possible Types: unsigned int
    int i;  // [bp-0x8]
    char v24;  // [bp-0x4]

    v12 = g_1038e180 ^ &v24;
    if (a1 == 536)
    {
        if ((char)sub_10327e40())
        {
            if (a2 == 18)
            {
                g_103a290b = 0;
                g_103a2920 = g_1038b03c();
                for (i = 0; i < *((int *)&g_103a2928); i += 1)
                {
                    v21 = i * 0x1000 + g_103a2914;
                    if (g_103a2905 && !((char)*((int *)(g_103a2934 + i * 4)) & 1))
                    {
                        g_1038b0c4(g_1038c8ac->field_0, v21, 0x1000, 4, &v22);
                        v20 = v22 | 0x100;
                        g_1038b0c4(g_1038c8ac->field_0, v21, 0x1000, v20, &v22);
                    }
                }
            }
            else if (a2 != 7 && a2 == 4)
            {
                g_103a290b = 1;
            }
        }
    }
    else
    {
        if (a1 == 0x11)
        {
            if (g_103a2909)
            {
                g_1038b2c0(a0, "Shutdown", 1);
                g_1038b2c4(g_1038c8ac->field_c, sub_10320b60, 0);
                g_1038b2fc(a0, "Shutdown");
            }
        }
        else
        {
            if (a1 == 22)
            {
                if (g_103a2909)
                {
                    v18 = a2;
                    v19 = a3;
                    g_1038b2c4(g_1038c8ac->field_c, sub_10320ba0, &v18);
                }
            }
            else
            {
                if (a1 != 275)
                {
                    sub_1032b700(a0, a1, a2, a3);
                }
                else if ((((char)g_1038c7f4 ^ (char)g_1038c834 ^ (char)g_1038c808) & 8))
                {
                    g_1038b1b8(&g_103a26a4);
                    v16 = 1;
                    v17 = 0;
                    for (j = 0; j < *((int *)&g_103a2928); j += 1)
                    {
                        v13 = j * 0x1000 + g_103a2914;
                        v27 = v26;
                        while (((char)v25 & 1) && ((char)*((int *)(g_103a2934 + j * 4)) & 4) && (v29 = g_1038b0c0(g_1038c8ac->field_0, v13, &v11, 0x1000, &v14), v29))
                        {
                            v30 = v17;
                            v31 = v30 + 1;
                            v17 = v31;
                            v8 = v29;
                            if (v30 + 1 >= 0)
                                goto LABEL_10320a39;
LABEL_10320a39:
                            v32 = _ccall(3, v30, 1, 0);
                            v9 = v32 | 0x202 | v33 * 0x200000 & 0x200000 | v34 * 0x40000 & 0x40000;
                            v7 = v8;
                            v6 = v35;
                            v5 = v31;
                            v4 = v27;
                            v3 = &v9;
                            v2 = &v24;
                            v1 = v36;
                            v0 = v37;
                            v25 = 0;
                            v39 = _ccall(0, 6, v31, v31, 0);
                            v40 = v31;
                            if (!((char)v39))
                            {
                                if (!(1))
                                    goto LABEL_10320a46;
LABEL_10320a46:
                                v27 = 0;
                                v43 = _ccall(2, 15, 3, 0, 0);
                                if ((char)v43)
                                    goto LABEL_0x10320a57;
                            }
                            else
                            {
                                v43 = _ccall(2, 6, v40, v31, 0);
                                if ((char)v43)
                                    goto LABEL_0x10320a57;
                            }
                        }
                    }
                    if (!v17)
                        g_103a2920 = g_1038b03c();
                    if (!v16)
                    {
                        for (idx = 0; idx < *((int *)&g_103a2928); idx += 1)
                        {
                            v44 = sub_102eb870(&g_103a2970);
                            *((unsigned int *)(g_103a2910 + idx * 4)) = v44 ^ *((int *)(g_103a2910 + idx * 4));
                        }
                    }
                    g_1038b1bc(&g_103a26a4);
                }
            }
        }
    }
    return sub_10351225();
}
```

## `sub_103208b6` `0x103208b6`

_5 bytes. (leaf/helper — see body)_

```c
void sub_103208b6(void)
{
}
```

## `sub_10320908` `0x10320908`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10320908(void)
{
    sub_10320914();
    return;
}
```

## `sub_10320914` `0x10320914`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10320914(void)
{
}
```

## `sub_10320955` `0x10320955`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10320955(void)
{
    sub_10320961();
    return;
}
```

## `sub_10320961` `0x10320961`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10320961(void)
{
}
```

## `sub_10320a50` `0x10320a50`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10320a50(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10320a64` `0x10320a64`

_67 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b03c;
extern unsigned int g_103a2920;
extern unsigned int g_103a2938;

int sub_10320a64(void)
{
    int v2;  // eax
    void* v1;  // [bp+0x8]

    v2 = sub_102ec930(v1 - 4144, 0x1000, 4294967295);
    if (v2 == *((int *)(g_103a2938 + (int)v1[36] * 4)))
        g_103a2920 = g_1038b03c();
    *((char *)&v1[29]) = 0;
}
```

## `sub_10320a68` `0x10320a68`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10320a68(void)
{
}
```

## `sub_10320a6a` `0x10320a6a`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10320a6a(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10320b2d` `0x10320b2d`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10320b2d(void)
{
}
```

## `sub_10320b60` `0x10320b60`

_53 bytes. refs "Shutdown"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b2c0;
extern struct_0 *g_1038b340;

unsigned int sub_10320b60(unsigned int a0)
{
    char v0;  // [bp+0x0]

    if (g_1038b340(a0, 0x11, 0, 0, &v0))
        return 1;
    g_1038b2c0(a0, "Shutdown", 0);
    return 0;
}
```

## `sub_10320b8c` `0x10320b8c`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10320b8c(void)
{
}
```

## `sub_10320ba0` `0x10320ba0`

_46 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b340;

unsigned int sub_10320ba0(unsigned int a0, unsigned int *a1)
{
    unsigned int v2;  // ecx
    unsigned int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = v2;
    g_1038b340(a0, 22, *(a1), a1[1], a1, &v1);
    return 1;
}
```

## `sub_10320bd0` `0x10320bd0`

_354 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b07c;
extern struct_0 *g_1038b098;
extern struct_0 *g_1038b128;
extern unsigned int g_1038e180;
extern unsigned int g_1039024c;
extern char g_10390258;

char sub_10320bd0(unsigned int a0, unsigned int a1)
{
    unsigned int v22;  // ebx
    unsigned int v23;  // esi
    unsigned int v32;  // 4101
    unsigned int v33;  // 4101
    int v34;  // cc_dep1
    unsigned int v35;  // 4101
    int v36;  // eax
    unsigned int v37;  // ecx
    unsigned int v38;  // 4163
    unsigned int v39;  // id
    unsigned int v40;  // ac
    unsigned int v41;  // edx
    unsigned int v24;  // edi
    unsigned int v42;  // 4110
    unsigned int v43;  // 4101
    unsigned int v25;  // 4101
    unsigned int v26;  // 4103
    unsigned int v27;  // 4101
    unsigned int v28;  // 4101
    unsigned int v29;  // 4101
    unsigned int v30;  // 4101
    unsigned int v31;  // 4101
    unsigned int v0;  // [bp-0x150]
    unsigned int v1;  // [bp-0x14c]
    char *v2;  // [bp-0x148]
    char *v3;  // [bp-0x144]
    unsigned int v4;  // [bp-0x140]
    unsigned int v5;  // [bp-0x13c]
    char *v6;  // [bp-0x138], Other Possible Types: unsigned int
    char *v7;  // [bp-0x134], Other Possible Types: int
    unsigned int v8;  // [bp-0x130]
    unsigned int v9;  // [bp-0x12c]
    unsigned int v10;  // [bp-0x128]
    unsigned int v11;  // [bp-0x124]
    char *iter;  // [bp-0x120], Other Possible Types: char
    char v13;  // [bp-0x11c]
    unsigned int v14;  // [bp-0x1c]
    char *i;  // [bp-0x18]
    int v16;  // [bp-0x14]
    int idx;  // [bp-0x10]
    char *v18;  // [bp-0xc]
    unsigned int v19;  // [bp-0x8]
    char v20;  // [bp-0x4]

    v14 = g_1038e180 ^ &v20;
    v11 = v14;
    v10 = a0;
    v9 = a1;
    v8 = v22;
    v7 = &iter;
    v6 = &v20;
    v5 = v23;
    v4 = v24;
LABEL_10320bff:
    v25 = _ccall(0, 15, 0, 0, 0);
    if ((char)v25)
        goto LABEL_10320c01;
    else
        goto LABEL_10320c02;
    while (true)
    {
LABEL_10320c01:
        __unsupported_jumpkind_Ijk_NoDecode()
        while (true)
        {
LABEL_10320c02:
            v26 = _ccall(10, 15, 0, 0, 0);
            if ((char)v26)
            {
                v27 = _ccall(8, 15, 0, 0, 0);
                if (!((char)v27))
                {
                    if (!(1))
                        goto LABEL_10320c07;
                    v28 = _ccall(10, 15, 0, 0, 0);
                    if (!((char)v28))
                    {
                        v29 = _ccall(0, 15, 0, 0, 0);
                        if ((char)v29)
                            break;
                        else
                            continue;
                    }
                    v30 = _ccall(8, 15, 0, 0, 0);
                    if ((char)v30)
                        goto LABEL_10320bff;
                    goto LABEL_10320c08;
                }
                __unsupported_jumpkind_Ijk_NoDecode()
                v31 = _ccall(8, 15, 0, 0, 0);
                if (!((char)v31))
                    goto LABEL_10320c08;
LABEL_10320bff:
                if ((v32 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v32))
                    break;
            }
            else
            {
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_10320c07:
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_10320c08:
                v18 = &g_10390258;
                v19 = &g_1039024c;
                idx = 0;
                if (idx >= 2)
                    return sub_10351225();
                v33 = _ccall(0, 6, idx, 2, 0);
                iter = &v13;
                for (i = v18; (*(iter) = (char)((int)(char)*(i) ^ 211), *(iter)); i += 1)
                {
                    iter += 1;
                }
                v16 = g_1038b098(0, 0, &v13);
                v34 = v16;
                if (v16)
                {
                    v35 = _ccall(0, 6, v34, 0, 0);
                    v36 = g_1038b128(v16);
                }
                else
                {
                    v8 = v37;
                    v7 = v16;
                    v38 = _ccall(6, v34, 0, 0);
                    v8 = v38 | 0x202 | v39 * 0x200000 & 0x200000 | v40 * 0x40000 & 0x40000;
                    v6 = v37;
                    v5 = v41;
                    v4 = v22;
                    v3 = &v8;
                    v2 = &v20;
                    v1 = v5;
                    v0 = v4;
                    if (!(1))
                        goto LABEL_10320cf1;
LABEL_10320cf1:
                    for (; (v42 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v42 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
                    v36 = g_1038b07c();
                    if (v36 == 6)
                    {
                        v43 = _ccall(0, 6, v36, 6, 0);
                        return sub_10351225();
                    }
                }
                v7 = v36;
            }
        }
    }
}
```

## `sub_10320bf5` `0x10320bf5`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10320bf5(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10320c39` `0x10320c39`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10320c39(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

