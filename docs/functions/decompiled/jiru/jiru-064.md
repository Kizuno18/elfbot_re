# elfbot.dll decompiled — jiru 0x1035a590..0x1035c835

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1035a590` `0x1035a590`

_9 bytes. (leaf/helper — see body)_

```c
int sub_1035a590(void)
{
    return sub_1035a4c1(10);
}
```

## `sub_1035a599` `0x1035a599`

_49 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1b8;
extern unsigned int g_1038e540[4];

int sub_1035a599(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v2;  // esi
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v1 = v2;
    if (!g_1038e540[2 * a2])
    {
        v0 = a2;
        if (!sub_1035a4d6(a0, a1))
            sub_10353c92(0x11);
    }
    return g_1038b1b8(g_1038e540[2 * a2]);
}
```

## `sub_1035a5ca` `0x1035a5ca`

_72 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b220;
extern unsigned int g_103a36c8;
extern unsigned int g_103a3820;
extern unsigned int g_103a4ca8;
extern unsigned int g_103a4cac;
extern unsigned int g_103a4cb0;
extern unsigned int g_103a4cb4;
extern unsigned int g_103a4cb8;

unsigned int sub_1035a5ca(void)
{
    g_103a4cac = g_1038b220(g_103a36c8, 0, 320);
    if (g_103a4cac)
    {
        g_103a3820 = 0;
        g_103a4ca8 = 0;
        g_103a4cb4 = g_103a4cac;
        g_103a4cb0 = 0;
        g_103a4cb8 = 16;
        return 1;
    }
    return 0;
}
```

## `sub_1035a612` `0x1035a612`

_43 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
} struct_0;

extern unsigned int g_103a4ca8;
extern struct_0 *g_103a4cac;

struct_0 * sub_1035a612(unsigned int a0)
{
    struct_0 *i;  // eax

    for (i = g_103a4cac; i < 20 * g_103a4ca8 + (char *)g_103a4cac; i = &i[1].padding_0[4])
    {
        if (a0 - i->field_c < 0x100000)
            return i;
    }
    return NULL;
}
```

## `sub_1035a63d` `0x1035a63d`

_788 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    char padding_8[4];
    unsigned int field_c;
    struct struct_0 *field_10;
    char padding_14[304];
    unsigned int field_144;
} struct_0;

typedef struct struct_9 {
    unsigned int field_0;
    struct struct_7 *field_4;
    struct struct_6 *field_8;
} struct_9;

typedef struct struct_10 {
    char padding_0[4];
    char field_4;
} struct_10;

typedef struct struct_3 {
    char padding_0[4];
    struct struct_4 *field_4;
    struct struct_3 *field_8;
} struct_3;

typedef struct struct_2 {
    char padding_0[4];
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
    struct struct_1 *field_10;
    char field_14;
} struct_2;

typedef struct struct_7 {
    char padding_0[8];
    struct struct_6 *field_8;
} struct_7;

typedef struct struct_6 {
    char padding_0[4];
    struct struct_7 *field_4;
} struct_6;

typedef struct struct_4 {
} struct_4;

typedef struct struct_1 {
    char padding_0[67];
    char field_43;
} struct_1;

typedef struct struct_12 {
    unsigned int field_0;
} struct_12;

extern struct_12 *g_1038b204;
extern struct_12 *g_1038b254;
extern unsigned int g_103a36c8;
extern struct_2 *g_103a3820;
extern unsigned int g_103a4ca8;
extern unsigned int g_103a4cac;
extern unsigned int g_103a4cb4;
extern unsigned int g_103a4cbc;

struct_0 * sub_1035a63d(struct_0 *iter, void* index)
{
    struct_0 *idx;  // ecx
    struct_0 *v9;  // eax
    struct_9 *idx1;  // ebx
    struct_10 *v18;  // ecx
    unsigned int v19;  // ebx
    char v20;  // 4109
    unsigned int v21;  // 4153
    struct_10 *v22;  // ecx
    unsigned int v23;  // ebx
    char v24;  // 4110
    unsigned int v25;  // 4155
    struct_0 *v26;  // edx
    unsigned int v10;  // esi
    unsigned int v27;  // edx
    struct_0 *v28;  // ebx
    unsigned int v29;  // ecx
    unsigned int v30;  // esi
    char v31;  // 4108
    unsigned int v32;  // 4152
    unsigned int v33;  // esi
    char v34;  // 4109
    unsigned int v35;  // 4154
    unsigned int v11;  // edi
    struct_3 *idx2;  // ecx
    void* v37;  // ebx
    struct_0 *v38;  // eax
    unsigned int v39;  // 4100
    struct_2 *v40;  // eax
    void* v12;  // esi
    unsigned int v13;  // edi
    unsigned int v14;  // ecx
    unsigned int v15;  // ebx
    struct_9 *v16;  // ebx
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    struct_0 *v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp+0xb]

    idx = iter;
    v9 = idx->field_10;
    v2 = v10;
    v1 = v11;
    v12 = index - 4;
    v13 = index - idx->field_c >> 15;
    v3 = 324 + 516 * v13 + (char *)v9;
    v14 = *((int *)v12) - 1;
    v6 = v14;
    if (((char)v14 & 1))
        return v9;
    v0 = v15;
    v16 = v14 + v12;
    v4 = v16->field_0;
    v5 = (int)v12[4];
    index = v16;
    if (!((char)v4 & 1))
    {
        v27 = (v4 >> 4) - 1;
        if (v27 > 0x3f)
            v27 = 63;
        idx1 = v16;
        if (idx1->field_4 == idx1->field_8)
        {
            if (v27 < 0x20)
            {
                v18 = 4 + v27 + (char *)v9;
                v19 = ~(0x80000000 >> ((char)v27 & 31));
                *((unsigned int *)&v9->padding_14[48 + 4 * v13]) = *((int *)&v9->padding_14[48 + 4 * v13]) & v19;
                v20 = v18->padding_0[0];
                v18->padding_0[0] = v18->padding_0[0] - 1;
                v21 = _ccall(4, 19, (unsigned int)(v20 - 1), 0, 0);
                if ((char)v21)
                    iter->field_0 = iter->field_0 & v19;
            }
            else
            {
                v22 = 4 + v27 + (char *)v9;
                v23 = ~(0x80000000 >> ((char)(v27 - 32) & 31));
                *((unsigned int *)&v9->padding_14[176 + 4 * v13]) = *((int *)&v9->padding_14[176 + 4 * v13]) & v23;
                v24 = v22->padding_0[0];
                v22->padding_0[0] = v22->padding_0[0] - 1;
                v25 = _ccall(4, 19, (unsigned int)(v24 - 1), 0, 0);
                if ((char)v25)
                    iter->field_4 = iter->field_4 & v23;
            }
            idx1 = index;
        }
        v14 = v6 + v4;
        idx1->field_8->field_4 = idx1->field_4;
        index->field_4->field_8 = index->field_8;
        v6 = v14;
    }
    v26 = (v14 >> 4) - 1;
    if (v26 > 0x3f)
    {
        v27 = 63;
        v26 = 0x3f;
    }
    v4 = v5 & 1;
    if (!((char)v5 & 1))
    {
        v27 = 63;
        index = v12 - v5;
        v28 = (v5 >> 4) - 1;
        if (v28 > 0x3f)
            v28 = 0x3f;
        v29 = v14 + v5;
        v26 = (v29 >> 4) - 1;
        v6 = v29;
        if (v26 > 0x3f)
            v26 = 0x3f;
        if (v28 != v26)
        {
            if ((int)index[4] == (int)index[8])
            {
                if (v28 < 0x20)
                {
                    v30 = ~(0x80000000 >> (*((char *)&v28) & 31));
                    *((unsigned int *)&v9->padding_14[48 + 4 * v13]) = *((int *)&v9->padding_14[48 + 4 * v13]) & v30;
                    v31 = *((char *)(v28 + v9 + 4));
                    *((char *)(v28 + v9 + 4)) = *((char *)(v28 + v9 + 4)) - 1;
                    v32 = _ccall(4, 19, (unsigned int)(v31 - 1), 0, 0);
                    if ((char)v32)
                        iter->field_0 = iter->field_0 & v30;
                }
                else
                {
                    v33 = ~(0x80000000 >> (*((char *)&(struct struct_0 *)&v28->padding_14[12]) & 31));
                    *((unsigned int *)&v9->padding_14[176 + 4 * v13]) = *((int *)&v9->padding_14[176 + 4 * v13]) & v33;
                    v34 = *((char *)(v28 + v9 + 4));
                    *((char *)(v28 + v9 + 4)) = *((char *)(v28 + v9 + 4)) - 1;
                    v35 = _ccall(4, 19, (unsigned int)(v34 - 1), 0, 0);
                    if ((char)v35)
                        iter->field_4 = iter->field_4 & v33;
                }
            }
            *((int *)((int)index[8] + 4)) = (int)index[4];
            *((int *)((int)index[4] + 8)) = (int)index[8];
        }
        v12 = index;
    }
    else
    {
        v28 = iter;
    }
    if (v4 || v28 != v26)
    {
        idx2 = (char *)v3 + 0x8 * v26;
        v37 = idx2->field_4;
        *((struct_3 **)&v12[8]) = idx2;
        *((void* *)&v12[4]) = v37;
        idx2->field_4 = v12;
        *((void* *)((int)v12[4] + 8)) = v12;
        if ((int)v12[4] == (int)v12[8])
        {
            v7 = *((char *)(v26 + v9 + 4));
            *((char *)(v26 + v9 + 4)) = *((char *)(v26 + v9 + 4)) + 1;
            if (v26 < 0x20)
            {
                if (!v7)
                    iter->field_0 = iter->field_0 | 0x80000000 >> (*((char *)&v26) & 31);
                *((unsigned int *)&v9->padding_14[48 + 4 * v13]) = *((int *)&v9->padding_14[48 + 4 * v13]) | 0x80000000 >> (*((char *)&v26) & 31);
            }
            else
            {
                if (!v7)
                    iter->field_4 = iter->field_4 | 0x80000000 >> (*((char *)&(struct struct_0 *)&v26->padding_14[12]) & 31);
                *((unsigned int *)&v9->padding_14[176 + 4 * v13]) = *((int *)&v9->padding_14[176 + 4 * v13]) | 0x80000000 >> (*((char *)&(struct struct_0 *)&v26->padding_14[12]) & 31);
            }
        }
    }
    *((unsigned int *)v12) = v6;
    *((unsigned int *)(-0x4 + v6 + (char *)v12)) = v6;
    v38 = v3;
    v39 = v38->field_0;
    v38->field_0 = v38->field_0 - 1;
    if (v39 == 1)
    {
        if (g_103a3820)
        {
            g_1038b254(g_103a4cbc * 0x8000 + g_103a3820->field_c, 0x8000, 0x4000);
            g_103a3820->field_8 = g_103a3820->field_8 | 0x80000000 >> ((char)g_103a4cbc & 31);
            *((unsigned int *)&g_103a3820->field_10[2].padding_0[60 + 4 * g_103a4cbc]) = 0;
            g_103a3820->field_10->field_43 = g_103a3820->field_10->field_43 - 1;
            v40 = g_103a3820;
            if (!g_103a3820->field_10->field_43)
            {
                g_103a3820->field_4 = g_103a3820->field_4 & 4294967294;
                v40 = g_103a3820;
            }
            if (v40->field_8 == 4294967295)
            {
                g_1038b254(v40->field_c, 0, 0x8000);
                g_1038b204(g_103a36c8, 0, g_103a3820->field_10);
                sub_10350ec0(g_103a3820, &g_103a3820->field_14, -20 + 20 * g_103a4ca8 - (char *)g_103a3820 + g_103a4cac);
                g_103a4ca8 = g_103a4ca8 - 1;
                if (iter > g_103a3820)
                    iter = iter->padding_14;
                g_103a4cb4 = g_103a4cac;
            }
        }
        v38 = iter;
        g_103a3820 = v38;
        g_103a4cbc = v13;
    }
    return v38;
}
```

## `sub_1035a951` `0x1035a951`

_176 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
    struct struct_0 *field_10;
} struct_2;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b074;
extern struct_0 *g_1038b204;
extern struct_0 *g_1038b220;
extern struct_0 *g_1038b258;
extern unsigned int g_103a36c8;
extern unsigned int g_103a4ca8;
extern unsigned int g_103a4cac;
extern unsigned int g_103a4cb8;

struct_2 * sub_1035a951(void)
{
    unsigned int v3;  // esi
    unsigned int v4;  // esi
    unsigned int v5;  // edi
    unsigned int v6;  // eax
    struct_2 *idx;  // esi
    unsigned int *v8;  // eax
    unsigned int v9;  // eax
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp-0x4]

    v1 = v3;
    v4 = g_103a4ca8;
    v0 = v5;
    if (g_103a4ca8 == g_103a4cb8)
    {
        v6 = g_1038b258(g_103a36c8, 0, g_103a4cac, (g_103a4cb8 + 16) * 20);
        if (!v6)
            return NULL;
        g_103a4cb8 = g_103a4cb8 + 16;
        v4 = g_103a4ca8;
        g_103a4cac = v6;
    }
    idx = v4 * 20 + g_103a4cac;
    v8 = g_1038b220(g_103a36c8, 8, 16836);
    idx->field_10 = v8;
    if (!v8)
        return NULL;
    v9 = g_1038b074(0, 0x100000, 0x2000, 4);
    idx->field_c = v9;
    if (v9)
    {
        idx->field_8 = 4294967295;
        idx->field_0 = 0;
        idx->field_4 = 0;
        g_103a4ca8 = g_103a4ca8 + 1;
        idx->field_10->field_0 = 4294967295;
        return idx;
    }
    g_1038b204(g_103a36c8, 0, idx->field_10);
    return NULL;
}
```

## `sub_1035aa01` `0x1035aa01`

_262 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[67];
    char field_43;
} struct_0;

typedef struct struct_1 {
    char padding_0[8];
    unsigned int field_8;
    char padding_c[4];
    struct struct_1 *field_10;
    struct struct_1 *field_14;
    char padding_18[304];
    struct struct_1 *field_148;
    struct struct_1 *field_14c;
    char padding_150[496];
    struct struct_1 *field_340;
    struct struct_1 *field_344;
    char padding_348[27848];
    struct struct_1 *field_7010;
} struct_1;

typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

extern struct_2 *g_1038b074;

unsigned int sub_1035aa01(unsigned int a0, unsigned int a1, void* a2)
{
    void* idx;  // ecx
    unsigned int v7;  // eax
    struct_1 *v16;  // edx
    struct_1 *iter;  // eax
    unsigned int k;  // ecx
    struct_1 *idx1;  // eax
    struct_1 *v21;  // ecx
    struct_1 *v22;  // ecx
    char v23;  // 4162
    void* idx2;  // eax
    unsigned int v8;  // ebx
    unsigned int v9;  // esi
    struct_0 *index;  // esi
    unsigned int v11;  // edi
    unsigned int i;  // ebx
    struct_1 *node;  // eax
    struct_1 *v15;  // edi
    unsigned int j;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    struct_1 *v4;  // [bp-0xc], Other Possible Types: unsigned int
    struct_1 *v5;  // [bp-0x8], Other Possible Types: unsigned int

    v5 = a0;
    v4 = a0;
    idx = a2;
    v7 = (int)idx[8];
    v3 = v8;
    v2 = v9;
    index = (int)idx[16];
    v1 = v11;
    for (i = 0; v7 >= 0; i += 1)
    {
        v7 *= 2;
    }
    node = 324 + 516 * i + (char *)index;
    j = 63;
    v4 = node;
    do
    {
        node->field_8 = node;
        *((struct_1 **)&node->padding_0[4]) = node;
        node = &node->field_8;
        j -= 1;
    } while (j != 1);
    v15 = i * 0x8000 + (int)idx[12];
    if (!g_1038b074(v15, 0x8000, 0x1000, 4))
        return 4294967295;
    v16 = &v15->padding_348[27832];
    v5 = v16;
    if (v15 <= v16)
    {
        iter = &v15->field_10;
        k = (v16 - v15 >> 12) + 1;
        do
        {
            iter->field_8 = 4294967295;
            *((unsigned int *)&iter->padding_348[3236]) = 4294967295;
            *((struct_1 **)&iter->padding_0[0]) = &iter->padding_348[3252];
            *((unsigned int *)&iter->padding_0[4]) = 0xff0;
            *((struct_1 **)&iter->padding_0[4]) = &iter->padding_348[3260];
            *((unsigned int *)&iter->padding_348[3232]) = 0xff0;
            iter = &iter->padding_348[3256];
            k -= 1;
        } while (k != 1);
        v16 = v5;
    }
    idx1 = &v4->padding_150[168];
    v21 = v15->padding_c;
    *((struct_1 **)&idx1->padding_0[4]) = v21;
    v21->field_8 = idx1;
    v22 = v16->padding_c;
    idx1->field_8 = v22;
    *((struct_1 **)&v22->padding_0[4]) = idx1;
    *((unsigned int *)&index[1].padding_0[4 * i]) = 0;
    *((unsigned int *)&index[2].padding_0[60 + 4 * i]) = 1;
    v23 = index->field_43;
    idx2 = a2;
    index->field_43 = index->field_43 + 1;
    if (!v23)
        *((unsigned int *)&idx2[4]) = (int)idx2[4] | 1;
    *((unsigned int *)&idx2[8]) = (int)idx2[8] & ~(0x80000000 >> ((char)i & 31));
    return i;
}
```

## `sub_1035ab07` `0x1035ab07`

_735 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    char padding_8[4];
    unsigned int field_c;
    unsigned int field_10;
} struct_0;

typedef struct struct_3 {
    char padding_0[4];
    char field_4;
} struct_3;

typedef struct struct_6 {
    struct struct_6 *field_0;
    struct struct_5 *field_4;
    struct struct_6 *field_8;
} struct_6;

typedef struct struct_2 {
    char padding_0[4];
    struct struct_1 *field_4;
} struct_2;

typedef struct struct_9 {
    char padding_0[68];
    unsigned int field_44;
} struct_9;

typedef struct struct_5 {
    char padding_0[4];
    struct struct_6 *field_4;
} struct_5;

typedef struct struct_1 {
    char padding_0[8];
    struct struct_1 *field_8;
} struct_1;

unsigned int sub_1035ab07(struct_0 *idx, void* a1, unsigned int iter)
{
    unsigned int v6;  // eax
    void* v7;  // edi
    unsigned int v16;  // 4156
    struct_3 *v17;  // ecx
    unsigned int v18;  // ebx
    char v19;  // 4113
    unsigned int v20;  // 4159
    unsigned int v21;  // edi
    struct_6 *idx1;  // ecx
    struct_9 *v23;  // eax
    char v24;  // cl
    void* v25;  // edx
    unsigned int v8;  // edx
    void* v26;  // eax
    unsigned int v27;  // eax
    void* v28;  // ebx
    unsigned int v29;  // ecx
    void* idx2;  // ebx
    unsigned int v31;  // esi
    unsigned int v32;  // esi
    struct_3 *v33;  // esi
    unsigned int v34;  // ebx
    char v35;  // 4109
    unsigned int v9;  // esi
    unsigned int v36;  // 4153
    struct_3 *v37;  // ecx
    unsigned int v38;  // ebx
    char v39;  // 4110
    unsigned int v40;  // 4155
    struct_2 *v41;  // ecx
    void* v42;  // edi
    struct_9 *v43;  // eax
    char v44;  // cl
    unsigned int v10;  // ecx
    void* index;  // edi
    unsigned int v12;  // ecx
    struct_3 *v13;  // ecx
    unsigned int v14;  // ebx
    char v15;  // 4110
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    int v3;  // [bp-0x8], Other Possible Types: unsigned int
    char v4;  // [bp+0xb]
    char v5;  // [bp+0xf]

    v6 = idx->field_10;
    v7 = a1;
    v8 = v7 - idx->field_c >> 15;
    v1 = v8 * 516 + v6 + 324;
    v9 = iter + 23 & 0xfffffff0;
    v10 = (int)v7[4] - 1;
    index = v10 + v7 - 4;
    iter = v10;
    v3 = *((int *)index);
    if (v9 > iter)
    {
        if (!((char)v3 & 1) && v9 <= v3 + iter)
        {
            v12 = (v3 >> 4) - 1;
            v2 = v12;
            if (v12 > 63)
            {
                v0 = 63;
                v12 = v0;
                v2 = v12;
            }
            if ((int)index[4] == (int)index[8])
            {
                if (v12 < 32)
                {
                    v13 = v2 + v6 + 4;
                    v14 = ~(0x80000000 >> ((char)v12 & 31));
                    *((unsigned int *)(v6 + v8 * 4 + 0x44)) = *((int *)(v6 + v8 * 4 + 0x44)) & v14;
                    v15 = v13->padding_0[0];
                    v13->padding_0[0] = v13->padding_0[0] - 1;
                    v16 = _ccall(4, 19, (unsigned int)(v15 - 1), 0, 0);
                    if ((char)v16)
                        idx->field_0 = idx->field_0 & v14;
                }
                else
                {
                    v17 = v2 + v6 + 4;
                    v18 = ~(0x80000000 >> ((char)(v12 - 32) & 31));
                    *((unsigned int *)(v6 + v8 * 4 + 196)) = *((int *)(v6 + v8 * 4 + 196)) & v18;
                    v19 = v17->padding_0[0];
                    v17->padding_0[0] = v17->padding_0[0] - 1;
                    v20 = _ccall(4, 19, (unsigned int)(v19 - 1), 0, 0);
                    if ((char)v20)
                        idx->field_4 = idx->field_4 & v18;
                }
            }
            *((int *)((int)index[8] + 4)) = (int)index[4];
            *((int *)((int)index[4] + 8)) = (int)index[8];
            v3 += iter - v9;
            if (v3 > 0)
            {
                v21 = (v3 >> 4) - 1;
                idx1 = a1 + v9 - 4;
                if (v21 > 63)
                {
                    v0 = 63;
                    v21 = v0;
                }
                iter = v1 + v21 * 8;
                idx1->field_4 = iter->field_4;
                idx1->field_8 = iter;
                iter->field_4 = idx1;
                *((struct_6 **)&idx1->field_4[1].padding_0[0]) = idx1;
                if (idx1->field_4 == idx1->field_8)
                {
                    v5 = *((char *)(v21 + v6 + 4));
                    *((char *)(v21 + v6 + 4)) = *((char *)(v21 + v6 + 4)) + 1;
                    if (v21 < 32)
                    {
                        if (!v5)
                            idx->field_0 = idx->field_0 | 0x80000000 >> ((char)v21 & 31);
                        v23 = v6 + v8 * 4 + 0x44;
                        v24 = v21;
                    }
                    else
                    {
                        if (!v5)
                            idx->field_4 = idx->field_4 | 0x80000000 >> ((char)(v21 - 32) & 31);
                        v23 = v6 + v8 * 4 + 196;
                        v24 = v21 - 32;
                    }
                    *((unsigned int *)&v23->padding_0[0]) = *((int *)&v23->padding_0[0]) | 0x80000000 >> (v24 & 31);
                }
                v25 = a1;
                v26 = v25 + v9 - 4;
                *((int *)v26) = v3;
                *((int *)(-0x4 + v3 + (char *)v26)) = v3;
            }
            else
            {
                v25 = a1;
            }
            v27 = v9 + 1;
            *((unsigned int *)&v25[4]) = v27;
            *((unsigned int *)(-0x8 + (char *)v25 + v9)) = v27;
        }
        else
        {
            return 0;
        }
    }
    else
    {
        if (v9 < iter)
        {
            v28 = a1;
            iter -= v9;
            v29 = v9 + 1;
            *((unsigned int *)&v28[4]) = v29;
            idx2 = v28 + v9 - 4;
            v31 = (iter >> 4) - 1;
            a1 = idx2;
            *((unsigned int *)&idx2[4]) = v29;
            if (v31 > 63)
            {
                v0 = 63;
                v31 = v0;
            }
            if (!((char)v3 & 1))
            {
                v32 = (v3 >> 4) - 1;
                if (v32 > 63)
                {
                    v0 = 63;
                    v32 = v0;
                }
                if ((int)index[4] == (int)index[8])
                {
                    if (v32 < 32)
                    {
                        v33 = v32 + v6 + 4;
                        v34 = ~(0x80000000 >> ((char)v32 & 31));
                        *((unsigned int *)(v6 + v8 * 4 + 0x44)) = *((int *)(v6 + v8 * 4 + 0x44)) & v34;
                        v35 = v33->padding_0[0];
                        v33->padding_0[0] = v33->padding_0[0] - 1;
                        v36 = _ccall(4, 19, (unsigned int)(v35 - 1), 0, 0);
                        if ((char)v36)
                            idx->field_0 = idx->field_0 & v34;
                    }
                    else
                    {
                        v37 = v32 + v6 + 4;
                        v38 = ~(0x80000000 >> ((char)(v32 - 32) & 31));
                        *((unsigned int *)(v6 + v8 * 4 + 196)) = *((int *)(v6 + v8 * 4 + 196)) & v38;
                        v39 = v37->padding_0[0];
                        v37->padding_0[0] = v37->padding_0[0] - 1;
                        v40 = _ccall(4, 19, (unsigned int)(v39 - 1), 0, 0);
                        if ((char)v40)
                            idx->field_4 = idx->field_4 & v38;
                    }
                    idx2 = a1;
                }
                *((int *)((int)index[8] + 4)) = (int)index[4];
                *((int *)((int)index[4] + 8)) = (int)index[8];
                iter += v3;
                v31 = (iter >> 4) - 1;
                if (v31 > 63)
                {
                    v0 = 63;
                    v31 = v0;
                }
            }
            v41 = v1 + v31 * 8;
            v42 = v41->field_4;
            *((struct_2 **)&idx2[8]) = v41;
            *((void* *)&idx2[4]) = v42;
            v41->field_4 = idx2;
            *((void* *)((int)idx2[4] + 8)) = idx2;
            if ((int)idx2[4] == (int)idx2[8])
            {
                v4 = *((char *)(v31 + v6 + 4));
                *((char *)(v31 + v6 + 4)) = *((char *)(v31 + v6 + 4)) + 1;
                if (v31 < 32)
                {
                    if (!v4)
                        idx->field_0 = idx->field_0 | 0x80000000 >> ((char)v31 & 31);
                    v43 = v6 + v8 * 4 + 0x44;
                    v44 = v31;
                }
                else
                {
                    if (!v4)
                        idx->field_4 = idx->field_4 | 0x80000000 >> ((char)(v31 - 32) & 31);
                    v43 = v6 + v8 * 4 + 196;
                    v44 = v31 - 32;
                }
                *((unsigned int *)&v43->padding_0[0]) = *((int *)&v43->padding_0[0]) | 0x80000000 >> (v44 & 31);
            }
            *((int *)idx2) = iter;
            *((int *)(-0x4 + iter + (char *)idx2)) = iter;
        }
    }
    return 1;
}
```

## `sub_1035ade6` `0x1035ade6`

_739 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    char padding_c[4];
    struct struct_0 *field_10;
} struct_1;

typedef struct struct_4 {
    char padding_0[8];
    unsigned int field_8;
} struct_4;

typedef struct struct_5 {
    char padding_0[324];
    unsigned int field_144;
} struct_5;

typedef struct struct_6 {
    unsigned int field_0;
    struct struct_6 *field_4;
    struct struct_6 *field_8;
} struct_6;

typedef struct struct_7 {
    char padding_0[4];
    char field_4;
} struct_7;

typedef struct struct_0 {
    unsigned int field_0;
    char padding_4[64];
    unsigned int field_44;
    char field_48;
    char padding_49[123];
    unsigned int field_c4;
    unsigned int field_c8;
} struct_0;

extern unsigned int g_103a3820;
extern unsigned int g_103a4ca8;
extern struct_1 *g_103a4cac;
extern struct_4 *g_103a4cb4;
extern char g_103a4cbc;

int * sub_1035ade6(unsigned int i)
{
    struct_1 *v6;  // eax
    int v7;  // ecx
    unsigned int v15;  // edx
    unsigned int node;  // ecx
    int k;  // edi
    unsigned int v18;  // ecx
    struct_6 *idx;  // edx
    int v20;  // ecx
    int v21;  // esi
    struct_7 *v22;  // edi
    char v23;  // 4112
    unsigned int v24;  // 4168
    unsigned int v8;  // esi
    struct_7 *v25;  // edi
    unsigned int v26;  // ebx
    char v27;  // 4112
    unsigned int v28;  // 4164
    struct_6 *idx1;  // ecx
    struct_6 *v30;  // edi
    int *v31;  // edx
    unsigned int v32;  // ecx
    unsigned int v33;  // ecx
    struct_4 *iter;  // ecx, Other Possible Types: struct_1 *
    unsigned int v10;  // ecx
    unsigned int v11;  // edx
    unsigned int v12;  // eax
    unsigned int v13;  // eax
    unsigned int v14;  // edx
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    struct_5 *v3;  // [bp-0x10]
    int v4;  // [bp-0xc], Other Possible Types: unsigned int
    unsigned int v5;  // [bp-0x8]

    v6 = &g_103a4cac[g_103a4ca8];
    v2 = i + 23 & 0xfffffff0;
    v7 = (v2 >> 4) - 1;
    if (v7 < 32)
    {
        v8 = 4294967295 >> ((char)v7 & 31);
        v4 = 4294967295;
    }
    else
    {
        v8 = 0;
        v4 = 4294967295 >> ((char)(v7 - 32) & 31);
    }
    iter = g_103a4cb4;
    while (true)
    {
        i = iter;
        if (iter >= v6 || (iter->field_4 & v4) || (iter->field_0 & v8))
            break;
        iter += 1;
    }
    if (iter == v6)
    {
        iter = g_103a4cac;
        while (true)
        {
            i = iter;
            if (iter >= g_103a4cb4 || (iter->field_4 & v4) || (iter->field_0 & v8))
                break;
            iter += 1;
        }
        if (iter == g_103a4cb4)
        {
            for (; iter < v6 && !iter->field_8; i = iter + 1);
            if (iter == v6)
            {
                iter = g_103a4cac;
                while (true)
                {
                    i = iter;
                    if (iter >= g_103a4cb4 || iter->field_8)
                        break;
                    iter = &iter[1].field_8;
                }
                if (iter == g_103a4cb4 && !((iter = (struct_4 *)sub_1035a951(), i = (struct_1 *)iter, iter)))
                    goto LABEL_1035aeb4;
            }
            v12 = sub_1035aa01(v10, v11, iter);
            iter->field_10->field_0 = v12;
            if (iter->field_10->field_0 == 4294967295)
            {
LABEL_1035aeb4:
                return NULL;
            }
        }
    }
    g_103a4cb4 = iter;
    v13 = iter->field_10;
    v14 = *((int *)v13);
    v5 = v14;
    if (v14 == 4294967295 || !(*((int *)(v13 + v14 * 4 + 196)) & v4) && !(*((int *)(v13 + v14 * 4 + 0x44)) & v8))
    {
        v5 = 0;
        v15 = *((int *)(v13 + 196));
        for (node = v13 + 0x44; !(v15 & v4) && !(*((int *)node) & v8); node += 4)
        {
            v5 += 1;
            v15 = *((int *)(node + 132));
        }
        v14 = v5;
    }
    v3 = v14 * 516 + v13 + 324;
    k = 0;
    v18 = *((int *)(v13 + v14 * 4 + 0x44)) & v8;
    if (!(*((int *)(v13 + v14 * 4 + 0x44)) & v8))
    {
        v18 = *((int *)(v13 + v14 * 4 + 196)) & v4;
        v0 = 32;
        k = 32;
    }
    for (; v18 >= NULL; k += 1)
    {
        v18 *= 2;
    }
    idx = *((int *)&v3->padding_0[4 + 8 * k]);
    v20 = idx->field_0 - v2;
    v21 = (v20 >> 4) - 1;
    v4 = v20;
    if (v21 > 63)
    {
        v0 = 63;
        v21 = 63;
    }
    if (v21 != k)
    {
        if (idx->field_4 == idx->field_8)
        {
            if (k < 32)
            {
                v22 = v13 + k + 4;
                v1 = ~(0x80000000 >> ((char)k & 31));
                *((unsigned int *)(v13 + v5 * 4 + 0x44)) = v1 & *((int *)(v13 + v5 * 4 + 0x44));
                v23 = v22->padding_0[0];
                v22->padding_0[0] = v22->padding_0[0] - 1;
                v24 = _ccall(4, 19, (unsigned int)(v23 - 1), 0, 0);
                if (!((char)v24))
                    goto LABEL_1035afd7;
                iter = i;
                iter->field_0 = iter->field_0 & v1;
            }
            else
            {
                v25 = v13 + k + 4;
                v26 = ~(0x80000000 >> ((char)(k - 32) & 31));
                *((unsigned int *)(v13 + v5 * 4 + 196)) = *((int *)(v13 + v5 * 4 + 196)) & v26;
                v27 = v25->padding_0[0];
                v25->padding_0[0] = v25->padding_0[0] - 1;
                v1 = v26;
                v28 = _ccall(4, 19, (unsigned int)(v27 - 1), 0, 0);
                if ((char)v28)
                {
                    iter = i;
                    iter->field_4 = iter->field_4 & v1;
                }
                else
                {
LABEL_1035afd7:
                    iter = i;
                }
            }
        }
        idx->field_8->field_4 = idx->field_4;
        idx->field_4->field_8 = idx->field_8;
        if (v4)
        {
            idx1 = &v3->padding_0[8 * v21];
            v30 = idx1->field_4;
            idx->field_8 = idx1;
            idx->field_4 = v30;
            idx1->field_4 = idx;
            idx->field_4->field_8 = idx;
            if (idx->field_4 == idx->field_8)
            {
                *((char *)&i + 3) = *((char *)(v21 + v13 + 4));
                *((char *)(v21 + v13 + 4)) = *((char *)(v21 + v13 + 4)) + 1;
                if (v21 < 32)
                {
                    if (!*((char *)((void*)&i + 3)))
                        iter->field_0 = iter->field_0 | 0x80000000 >> ((char)v21 & 31);
                    *((unsigned int *)(v13 + v5 * 4 + 0x44)) = *((int *)(v13 + v5 * 4 + 0x44)) | 0x80000000 >> ((char)v21 & 31);
                }
                else
                {
                    if (!*((char *)((void*)&i + 3)))
                        iter->field_4 = iter->field_4 | 0x80000000 >> ((char)(v21 - 32) & 31);
                    *((unsigned int *)(v13 + v5 * 4 + 196)) = *((int *)(v13 + v5 * 4 + 196)) | 0x80000000 >> ((char)(v21 - 32) & 31);
                }
            }
            v20 = v4;
            goto LABEL_1035b077;
        }
        else
        {
            v20 = v4;
        }
    }
    else
    {
LABEL_1035b077:
        if (v20)
        {
            idx->field_0 = v20;
            *((int *)(-0x4 + v20 + (char *)idx)) = v20;
        }
    }
    v31 = (char *)idx + v20;
    v32 = v2 + 1;
    *(v31) = v32;
    *((unsigned int *)(-0x4 + (char *)v31 + v2)) = v32;
    v33 = *((int *)&v3->padding_0[0]);
    *((unsigned int *)&v3->padding_0[0]) = v33 + 1;
    if (!v33 && iter == g_103a3820 && v5 == *((int *)&g_103a4cbc))
        g_103a3820 = 0;
    *((unsigned int *)v13) = v5;
    return v31 + 1;
}
```

## `sub_1035b0cc` `0x1035b0cc`

_69 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

char * sub_1035b0cc(unsigned int a0, unsigned int a1)
{
    unsigned long v3;  // ldt
    unsigned long v4;  // gdt
    unsigned short v5;  // fs
    unsigned long v6;  // 4146
    unsigned int v7;  // ebx
    unsigned int v8;  // esi
    unsigned int v9;  // edi
    unsigned long v10;  // 4190
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp+0x0]
    char *v2;  // [bp+0x8]

    v6 = _ccall(v3, v4, (unsigned int)v5, 0);
    v0 = *((int *)v6);
    v2 = &v1;
    /* unsupported instruction */ = (char *)&v0 - a1;
    /* unsupported instruction */ = /* unsupported instruction */ - 4;
    *((unsigned int *)(/* unsupported instruction */ - 4)) = v7;
    /* unsupported instruction */ = /* unsupported instruction */ - 4;
    *((unsigned int *)(/* unsupported instruction */ - 4)) = v8;
    /* unsupported instruction */ = /* unsupported instruction */ - 4;
    *((unsigned int *)(/* unsupported instruction */ - 4)) = v9;
    *((unsigned long *)(/* unsupported instruction */ - 4)) = g_1038e180 ^ &v2;
    *((unsigned int *)(/* unsupported instruction */ - 8)) = v1;
    v10 = _ccall(v3, v4, (unsigned int)v5, 0);
    *((unsigned int **)v10) = &v0;
    return &v0;
}
```

## `sub_1035b111` `0x1035b111`

_20 bytes. (leaf/helper — see body)_

```c
void sub_1035b111(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned long v1;  // ldt
    unsigned long v2;  // gdt
    unsigned short v3;  // fs
    unsigned long v4;  // 4123
    unsigned int v0;  // [bp+0xffff4]

    v4 = _ccall(v1, v2, (unsigned int)v3, 0);
    *((unsigned int *)v4) = v0;
    return;
}
```

## `sub_1035b125` `0x1035b125`

_8 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a4ca4;

void sub_1035b125(void)
{
    g_103a4ca4 = 0;
    return;
}
```

## `sub_1035b12d` `0x1035b12d`

_47 bytes. (leaf/helper — see body)_

```c
int sub_1035b12d(void)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v3;  // eax

    v2 = v1 - 932;
    if (v1 == 932)
        return;
    v3 = v2 - 4;
    if (v2 == 4)
    {
        return;
    }
    else if (v3 != 13)
    {
        return;
    }
    else
    {
        return;
    }
}
```

## `sub_1035b15c` `0x1035b15c`

_85 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    unsigned int field_14;
    unsigned int field_18;
    char field_1c;
    char padding_1d[256];
    char field_11d;
} struct_0;

extern char g_1038e758;

int sub_1035b15c(void)
{
    unsigned int i;  // ebp
    struct_0 *v2;  // eax
    struct_0 *iter;  // ebx
    struct_0 *v4;  // edi
    struct_0 *v5;  // edi
    unsigned int v6;  // eax
    struct_0 *node;  // ecx
    unsigned int j;  // esi

    i = 0x101;
    iter = &v2->field_1c;
    sub_10350ad0(iter, 0, 0x101);
    memset(&v2->padding_0[4], 0, 12);
    v4 = &v2->field_10;
    *((unsigned int *)&v4->padding_0[0]) = 0;
    v5 = &v4->padding_0[4];
    *((unsigned int *)&v5->padding_0[0]) = 0;
    *((unsigned int *)&v5->padding_0[4]) = 0;
    v6 = &g_1038e758 - v2;
    do
    {
        iter->padding_0[0] = iter->padding_0[v6];
        iter = &iter->padding_0[1];
        i -= 1;
    } while (i != 1);
    node = &v2->field_11d;
    j = 0x100;
    do
    {
        node->padding_0[0] = node->padding_0[v6];
        node = &node->padding_0[1];
        j -= 1;
    } while (j != 1);
    return;
}
```

## `sub_1035b1b1` `0x1035b1b1`

_394 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[285];
    char field_11d;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b230;
extern unsigned int g_1038e180;

int sub_1035b1b1(void)
{
    void* v10;  // esi
    unsigned int v11;  // edi
    char v20;  // cl
    unsigned int v21;  // ecx
    struct_1 *v22;  // eax
    unsigned int v23;  // edx
    char v24;  // dl
    unsigned int v12;  // ebx
    unsigned int i;  // eax
    char v14[2];  // ebx
    unsigned int v15;  // ecx
    unsigned int v16;  // eax
    char v17[2];  // ebx
    unsigned int v18;  // eax
    char v19;  // cl
    unsigned int v0;  // [bp-0x520]
    char v1;  // [bp-0x51c]
    char v2;  // [bp-0x516]
    char v3;  // [bp-0x515]
    char v4;  // [bp-0x508]
    char v5;  // [bp-0x4a0]
    char v6;  // [bp-0x308]
    char v7;  // [bp-0x208]
    char v25[256];  // [bp-0x108], Other Possible Types: unsigned short
    unsigned int v8;  // [bp-0x8]

    v8 = g_1038e180 ^ &v5;
    if (g_1038b230((int)v10[4], &v1, v11, v12))
    {
        i = 0;
        do
        {
            *((char *)&v25 + i) = i;
            i += 1;
        } while (i < 0x100);
        v25 = 32;
        if (v2)
        {
            v14 = &v3;
            do
            {
                v15 = v2;
                v16 = v14[0];
                if (v15 <= v16)
                    sub_10350ad0(&v25[v15], 32, v16 - v15 + 1);
            } while ((v17 = v14 + 1, v2 = v17[0], v14 = v17 + 1, v17[0]));
        }
        sub_1035fbea(0, 1, v25, 0x100, &v4, (int)v10[4], (int)v10[12], 0);
        sub_10356e55(NULL, (int)v10[12], 0x100, v25, 0x100, &v7, 0x100, (int)v10[4], 0);
        sub_10356e55(NULL, (int)v10[12], 0x200, v25, 0x100, &v6, 0x100, (int)v10[4], 0);
        v18 = 0;
        do
        {
            v19 = *((short *)&(&v4)[2 * v18]);
            if ((v19 & 1))
            {
                *(29 + (char *)v10 + v18) = *(29 + (char *)v10 + v18) | 16;
                v20 = (&v7)[v18];
                goto LABEL_1035b2bf;
            }
            else if ((v19 & 2))
            {
                *(29 + (char *)v10 + v18) = *(29 + (char *)v10 + v18) | 32;
                v20 = (&v6)[v18];
LABEL_1035b2bf:
                *(285 + (char *)v10 + v18) = v20;
            }
            else
            {
                *(285 + (char *)v10 + v18) = 0;
            }
        } while ((v18 += 1, v18 < 0x100));
    }
    else
    {
        v0 = 4294967199;
        v21 = 0;
        v0 -= v10 + 285;
        do
        {
            v22 = v10 + v21 + 285;
            v23 = &v22->padding_0[v0];
            if (v23 + 32 <= 25)
            {
                *(29 + (char *)v10 + v21) = *(29 + (char *)v10 + v21) | 16;
                v24 = (char)v21 + 32;
                goto LABEL_1035b318;
            }
            else if (v23 <= 25)
            {
                *(29 + (char *)v10 + v21) = *(29 + (char *)v10 + v21) | 32;
                v24 = (char)v21 - 32;
LABEL_1035b318:
                v22->padding_0[0] = v24;
            }
            else
            {
                v22->padding_0[0] = 0;
            }
        } while ((v21 += 1, v21 < 0x100));
    }
    return sub_10351225();
}
```

## `sub_1035b33b` `0x1035b33b`

_152 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[104];
    unsigned int field_68;
    unsigned int field_6c;
    unsigned int field_70;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b1ec;
extern struct_1 *g_1038b1f0;
extern unsigned int g_1038e660;
extern unsigned int g_1038e758;
extern char g_1038eb80;
extern unsigned int g_103a1260;

void sub_1035b33b(unsigned int a0)
{
    struct_0 *idx;  // edi
    unsigned int v5;  // esi
    unsigned int v6;  // ecx
    unsigned int v7;  // edx
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp+0xfffe8]
    unsigned int v3;  // [bp+0x100000]

    sub_1035b0cc(&g_103a1260, 12);
    idx = sub_10358da8();
    if ((g_1038e660 & idx->field_70) && idx->field_6c)
    {
        v5 = idx->field_68;
    }
    else
    {
        v1 = 13;
        sub_1035a599(v6, v7, 13);
        v3 = 0;
        v5 = idx->field_68;
        v2 = v5;
        if (v5 != *((int *)&g_1038eb80))
        {
            v1 = v1;
            if (v5)
            {
                v1 = v5;
                if (!g_1038b1f0(v1))
                {
                    v1 = v5;
                    if (v1 != &g_1038e758)
                    {
                        v0 = v5;
                        sub_1035345e();
                        v1 = v5;
                    }
                }
            }
            idx->field_68 = *((int *)&g_1038eb80);
            v5 = *((int *)&g_1038eb80);
            v2 = *((int *)&g_1038eb80);
            v0 = *((int *)&g_1038eb80);
            g_1038b1ec(*((int *)&g_1038eb80));
        }
        v3 = 4294967294;
        sub_1035b3d6();
    }
    if (!v5)
    {
        sub_10353c92(32);
        sub_1035b111(v0, v1, &g_103a1260, 12);
    }
    else
    {
        sub_1035b111(v0, v1, &g_103a1260, 12);
    }
    return;
}
```

## `sub_1035b3d3` `0x1035b3d3`

_3 bytes. (leaf/helper — see body)_

```c
void sub_1035b3d3(void)
{
    sub_1035b3d6();
    return;
}
```

## `sub_1035b3d6` `0x1035b3d6`

_9 bytes. (leaf/helper — see body)_

```c
int sub_1035b3d6(void)
{
    return sub_1035a4c1(13);
}
```

## `sub_1035b3df` `0x1035b3df`

_122 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

typedef struct struct_3 {
    char padding_0[112];
    unsigned int field_70;
} struct_3;

extern struct_0 *g_1038b25c;
extern struct_0 *g_1038b260;
extern unsigned int g_103a3844;

unsigned int sub_1035b3df(void)
{
    unsigned int v4;  // esi
    unsigned int v5;  // eax
    struct_0 v0;  // [bp-0x14]
    struct_3 *idx;  // [bp-0xc]
    char v2;  // [bp-0x8]

    sub_103536a7(&v0, NULL);
    g_103a3844 = 0;
    if (v4 == 4294967294)
    {
        g_103a3844 = 1;
        v5 = g_1038b260();
    }
    else if (v4 == 4294967293)
    {
        g_103a3844 = 1;
        v5 = g_1038b25c();
    }
    else if (v4 == 0xfffffffc)
    {
        v5 = *((int *)(v0 + 4));
        g_103a3844 = 1;
    }
    else
    {
        if (!v2)
            return v4;
        idx->field_70 = idx->field_70 & 4294967293;
        return v4;
    }
    if (v2)
        idx->field_70 = idx->field_70 & 4294967293;
    return v5;
}
```

## `sub_1035b459` `0x1035b459`

_473 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    char padding_0[4];
    unsigned int field_4;
    char padding_8[4];
    int field_c;
    unsigned short field_10;
    char padding_12[12];
    char field_1e;
} struct_2;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b230;
extern struct_0 *g_1038b264;
extern unsigned int g_1038e180;
extern char g_1038eb84;
extern char g_1038eb88;
extern char g_1038eb8c;
extern char g_1038eb98;
extern unsigned int g_103a3844;

int sub_1035b459(unsigned int a0, struct_2 *idx)
{
    unsigned int v11;  // ebx
    unsigned int v12;  // esi
    unsigned int v22;  // edx
    struct_2 *v23;  // edi
    struct_2 *v24;  // edi
    char iter[2];  // esi
    unsigned int v26;  // edi
    unsigned int l;  // edi
    unsigned int v28;  // eax
    struct_2 *iter1;  // eax
    unsigned int v30;  // ecx
    unsigned int v13;  // edi
    unsigned int v31;  // ecx
    unsigned int v14;  // edi
    unsigned int v15;  // eax
    char *node;  // esi
    char v17;  // cl
    unsigned int k;  // eax
    struct_2 *iter2;  // eax
    unsigned int i;  // ecx
    unsigned int j;  // [bp-0x34]
    unsigned int v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x28]
    unsigned int v4;  // [bp-0x24]
    char v5[2];  // [bp-0x20], Other Possible Types: unsigned int
    char v6;  // [bp-0x1c], Other Possible Types: unsigned int
    int v8;  // [bp-0x16]
    unsigned int v9;  // [bp-0x8]
    char v10;  // [bp-0x4]

    v9 = g_1038e180 ^ &v10;
    v3 = v11;
    v2 = v12;
    v1 = v13;
    v14 = sub_1035b3df();
    a0 = v14;
    if (v14)
    {
        v5 = 0;
        v15 = 0;
        do
        {
            if (*((int *)&(&g_1038eb88)[v15]) == v14)
            {
                sub_10350ad0(&idx->padding_12[10], 0, 0x101);
                v4 = 0;
                iter = &(&g_1038eb98)[48 * v5];
                v5 = iter;
                v26 = v14;
                while (true)
                {
                    if (iter[0] && iter[1])
                    {
                        l = iter[0];
                        for (v28 = iter[1]; l <= v28; l += 1)
                        {
                            idx->padding_12[11 + l] = idx->padding_12[11 + l] | (&g_1038eb84)[v4];
                            v28 = iter[1];
                        }
                        iter += 1;
                        v26 = a0;
                    }
                    else
                    {
                        v4 += 1;
                        iter = v5 + 4;
                        v5 = iter;
                        if (v4 >= 4)
                            break;
                    }
                }
                idx->field_4 = v26;
                *((unsigned int *)&idx->padding_8[0]) = 1;
                j = 6;
                idx->field_c = sub_1035b12d();
                iter1 = &idx->field_10;
                v31 = &(&g_1038eb8c)[v30];
                do
                {
                    *((short *)&iter1->padding_0[0]) = *((short *)v31);
                    v31 += 2;
                    iter1 = &iter1->padding_0[2];
                    j -= 1;
                } while (j != 1);
            }
        } while ((v5 += 1, v15 += 48, v15 < 240));
        if (v14 == 65000 || v14 == 65001 || !g_1038b264((unsigned short)v14))
            return sub_10351225();
        if (g_1038b230(v14, &v6))
        {
            sub_10350ad0(&idx->padding_12[10], 0, 0x101);
            idx->field_4 = v14;
            idx->field_c = 0;
            if (v6 > 1)
            {
                if (*((char *)&v8))
                {
                    node = &v8 - 1;
                    do
                    {
                        v17 = *(node);
                        if (!*(node))
                            break;
                        for (k = node[1]; k <= v17; k += 1)
                        {
                            idx->padding_12[11 + k] = idx->padding_12[11 + k] | 4;
                        }
                        node += 2;
                    } while (node[1]);
                }
                iter2 = &idx->field_1e;
                i = 254;
                do
                {
                    iter2->padding_0[0] = iter2->padding_0[0] | 8;
                    iter2 = &iter2->padding_0[1];
                    i -= 1;
                } while (i != 1);
                idx->field_c = sub_1035b12d();
                *((unsigned int *)&idx->padding_8[0]) = v22;
            }
            else
            {
                *((unsigned int *)&idx->padding_8[0]) = 0;
            }
            v23 = &idx->field_10;
            *((unsigned int *)&v23->padding_0[0]) = 0;
            v24 = &v23->field_4;
            *((unsigned int *)&v24->padding_0[0]) = 0;
            v24->field_4 = 0;
            sub_1035b1b1();
            return sub_10351225();
        }
        else if (!g_103a3844)
        {
            return sub_10351225();
        }
    }
    sub_1035b15c();
    return sub_10351225();
}
```

## `sub_1035b632` `0x1035b632`

_399 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[104];
    struct struct_0 *field_68;
    char padding_6c[4];
    char field_70;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
} struct_0;

typedef struct struct_3 {
    unsigned int field_0;
} struct_3;

extern struct_3 *g_1038b1ec;
extern struct_3 *g_1038b1f0;
extern char g_1038e660;
extern unsigned int g_1038e758[4];
extern char g_1038e978;
extern char g_1038ea80;
extern struct_0 *g_1038eb80;
extern unsigned int g_103a1280;
extern unsigned short g_103a3848;
extern unsigned int g_103a3854;
extern unsigned int g_103a3858;
extern unsigned int g_103a385c;

void sub_1035b632(unsigned int a0)
{
    struct_1 *index;  // edi
    unsigned int v9[4];  // ebx
    unsigned int v18;  // edx
    int idx;  // eax
    int node;  // eax
    int iter;  // eax
    unsigned int v10;  // eax
    unsigned int idx1[4];  // ebx
    unsigned int v12;  // ecx
    unsigned int i[4];  // esi
    unsigned int iter1[4];  // edi
    int v15;  // eax
    struct_1 *idx2;  // esi
    unsigned int v17;  // ecx
    unsigned int v0[4];  // [bp-0x18]
    struct_0 *v1;  // [bp-0x10], Other Possible Types: unsigned int [4], unsigned int
    unsigned int v2[4];  // [bp-0xc], Other Possible Types: unsigned int
    struct_1 *v3;  // [bp+0xfffe0]
    int v4;  // [bp+0xfffe4], Other Possible Types: unsigned int
    int v5;  // [bp+0xfffe8]
    unsigned int v6;  // [bp+0x100000]
    unsigned int v7;  // [bp+0x10000c]

    sub_1035b0cc(&g_103a1280, 20);
    v4 = 4294967295;
    index = sub_10358da8();
    v3 = index;
    sub_1035b33b(&g_103a1280);
    v9 = index->field_68;
    v10 = sub_1035b3df();
    v7 = v10;
    if (v10 == v9[1])
    {
        v4 = 0;
        sub_1035b111(v1, v2, &g_103a1280, 20);
        return;
    }
    idx1 = sub_10357482(544);
    if (!idx1)
    {
        sub_1035b111(v1, 544, &g_103a1280, 20);
        return;
    }
    v12 = 0x88;
    i = index->field_68;
    for (iter1 = idx1; v12; i = &i[1])
    {
        v12 -= 1;
        iter1[0] = i[0];
        iter1 = &iter1[1];
    }
    idx1[0] = 0;
    v15 = sub_1035b459(v7, idx1);
    v4 = v15;
    if (!v15)
    {
        idx2 = v3;
        if (!g_1038b1f0(idx2->field_68) && idx2->field_68 != &g_1038e758[0])
        {
            v1 = idx2->field_68;
            sub_1035345e();
        }
        idx2->field_68 = idx1;
        g_1038b1ec(idx1);
        if ((idx2->field_70 & 2))
        {
            v1 = idx1;
            sub_1035b111(idx1, idx2->field_68, &g_103a1280, 20);
            return;
        }
        if (!(g_1038e660 & 1))
        {
            sub_1035a599(v17, v18, 13);
            v6 = 0;
            g_103a3854 = idx1[1];
            g_103a3858 = idx1[2];
            g_103a385c = idx1[3];
            idx = 0;
            while (true)
            {
                v5 = idx;
                if (idx >= 5)
                    break;
                (&g_103a3848)[idx] = *((short *)(16 + (char *)idx1 + 2 * idx));
                idx += 1;
            }
            node = 0;
            while (true)
            {
                v5 = node;
                if (node >= 0x101)
                    break;
                (&g_1038e978)[node] = *(28 + node + (char *)idx1);
                node += 1;
            }
            iter = 0;
            while (true)
            {
                v5 = iter;
                if (iter >= 0x100)
                    break;
                (&g_1038ea80)[iter] = *(285 + iter + (char *)idx1);
                iter += 1;
            }
            if (!g_1038b1f0(g_1038eb80) && g_1038eb80 != &g_1038e758[0])
            {
                v0 = g_1038eb80;
                sub_1035345e();
            }
            g_1038eb80 = idx1;
            g_1038b1ec(idx1);
            v6 = 4294967294;
            sub_1035b793(idx1);
            v1 = idx1;
            sub_1035b111(idx1, idx2->field_68, &g_103a1280, 20);
            return;
        }
        else
        {
            v1 = idx1;
            sub_1035b111(idx1, idx2->field_68, &g_103a1280, 20);
            return;
        }
    }
    else if (v15 == -1)
    {
        if (idx1 != &g_1038e758[0])
        {
            v2 = idx1;
            sub_1035345e();
        }
        *((unsigned int *)sub_103575e0()) = 22;
        sub_1035b111(v7, idx1, &g_103a1280, 20);
        return;
    }
    else
    {
        v2 = idx1;
        sub_1035b111(v7, idx1, &g_103a1280, 20);
        return;
    }
}
```

## `sub_1035b793` `0x1035b793`

_9 bytes. (leaf/helper — see body)_

```c
int sub_1035b793(void)
{
    return sub_1035a4c1(13);
}
```

## `sub_1035b79c` `0x1035b79c`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1035b79c(void)
{
}
```

## `sub_1035b7cc` `0x1035b7cc`

_30 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a4cdc;

unsigned int sub_1035b7cc(void)
{
    if (!g_103a4cdc)
    {
        sub_1035b632(4294967293);
        g_103a4cdc = 1;
    }
    return 0;
}
```

## `sub_1035b7ea` `0x1035b7ea`

_182 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

typedef struct struct_1 {
    char padding_0[112];
    unsigned int field_70;
} struct_1;

unsigned int sub_1035b7ea(int a0, unsigned int a1, unsigned int *a2)
{
    unsigned int v8;  // eax
    int v0;  // [bp-0x24]
    struct_0 v1;  // [bp-0x1c]
    struct_1 *idx;  // [bp-0x14]
    char v3;  // [bp-0x10]
    char v4;  // [bp-0xc]
    char v5;  // [bp-0xb]
    char v6;  // [bp-0xa]
    char v7;  // [bp-0x8], Other Possible Types: unsigned short

    sub_103536a7(&v1, a2);
    if (a0 + 1 <= 0x100)
    {
        v8 = *((short *)(*((int *)(v1 + 200)) + a0 * 2));
    }
    else
    {
        a0 >>= 8;
        if (sub_1035de48(a0 & 0xff, &v1))
        {
            v0 = 2;
            v4 = a0;
            v5 = a0;
            v6 = 0;
        }
        else
        {
            v4 = a0;
            v5 = 0;
            v0 = 1;
        }
        if (!sub_1035fbea(&v1, 1, &v4, v0, &v7, *((int *)(v1 + 4)), *((int *)(v1 + 20)), 1))
        {
            if (!v3)
                return 0;
            idx->field_70 = idx->field_70 & 4294967293;
            return 0;
        }
        v8 = v7;
    }
    if (v3)
        idx->field_70 = idx->field_70 & 4294967293;
    return v8 & a1;
}
```

## `sub_1035b8a0` `0x1035b8a0`

_149 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1035b8a0(unsigned int a0, unsigned int a1, unsigned long long a2, unsigned int a3)
{
    unsigned int v0;  // eax
    unsigned int i;  // ecx
    unsigned long v10;  // 4170
    unsigned int v11;  // eax
    unsigned int v12;  // esi
    unsigned int v13;  // ecx
    unsigned int v14;  // edx
    unsigned long long v2;  // ebx
    unsigned int v3;  // edx
    unsigned int v5;  // 4166
    unsigned long v6;  // 4167
    unsigned int v7;  // ebx
    unsigned int v8;  // edx
    unsigned int v9;  // 4169

    if (!a3)
        return (a1 % a2 CONCAT a0) / a2;
    v0 = a0;
    i = a3;
    v2 = a2;
    v3 = a1;
    do
    {
        v5 = _ccall(27, i >> 1, i, 0);
        v6 = _ccall(v2, 1, v5, 4);
        v9 = _ccall(27, v3 >> 1, v3, 0);
        v10 = _ccall(v0, 1, v9, 4);
        v0 = v10;
        i >>= 1;
        v2 = v6;
        v3 >>= 1;
    } while (i);
    v12 = (v8 CONCAT v11) / v7;
    v13 = v12 * a3;
    v14 = a2 * v12 >> 32;
    if (v14 + v13 < 0 || v14 + v13 > a1 || v14 + v13 >= a1 && (unsigned int)(a2 * v12) > a0)
        v12 -= 1;
    return v12;
}
```

## `sub_1035b935` `0x1035b935`

_113 bytes. (leaf/helper — see body)_

```c
typedef struct struct_3 {
    char padding_0[112];
    unsigned int field_70;
} struct_3;

typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

struct_3 * sub_1035b935(char *a0, unsigned int *a1)
{
    unsigned int v4;  // esi
    char iter[2];  // esi
    char v14;  // 4103
    unsigned int v6;  // eax
    unsigned int v7;  // cc_op
    unsigned int v8;  // cc_dep2
    unsigned int v9;  // 4104
    int v10;  // eax
    struct_3 *idx;  // eax
    char v12[2];  // esi
    char v13[2];  // esi
    unsigned int v0;  // [bp-0x18]
    struct_0 v1;  // [bp-0x14]
    struct_3 *v2;  // [bp-0xc]
    char v3;  // [bp-0x8]

    v0 = v4;
    sub_103536a7(&v1, a1);
    iter = a0;
    v6 = sub_1035773b(iter[0]);
    v7 = 6;
    v8 = 101;
    while (true)
    {
        v9 = _ccall(4, v7, v6, v8, 0);
        if ((char)v9)
            break;
        iter = &iter[1];
        v6 = sub_10357000(iter[0]);
        v7 = 15;
        v8 = 0;
    }
    v10 = sub_1035773b(iter[0]);
    if (v10 == 120)
        iter += 1;
    idx = _INSERT(v10, 0, iter[0]);
    iter[0] = *((char *)*((int *)*((int *)(v1 + 188))));
    v12 = &iter[1];
    do
    {
        v13 = v12;
        v14 = v13[0];
        v13[0] = *((char *)&idx);
        idx = _INSERT(idx, 0, v14);
        v12 = &v13[1];
    } while (v13[0]);
    if (v3 != v13[0])
    {
        idx = v2;
        idx->field_70 = idx->field_70 & 4294967293;
    }
    return idx;
}
```

## `sub_1035b9a6` `0x1035b9a6`

_128 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
    char field_1;
    char padding_2[110];
    unsigned int field_70;
} struct_0;

struct_0 * sub_1035b9a6(struct_0 *a0, unsigned int *a1)
{
    unsigned int v5;  // esi
    struct_0 *node;  // eax
    char v7;  // cl
    struct_0 *iter;  // eax
    struct_0 *v9;  // eax
    unsigned int v10;  // ebx
    char j;  // 4103
    struct_0 *v12;  // edx
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    struct_0 v2;  // [bp-0x14]
    struct_0 *v3;  // [bp-0xc]
    char v4;  // [bp-0x8]

    v1 = v5;
    sub_103536a7(&v2, a1);
    node = a0;
    v7 = node->field_0;
    if (node->field_0)
    {
        do
        {
        } while (v7 != *((char *)*((int *)*((int *)(v2 + 188)))) && (node += 1, v7 = node->field_0, node->field_0));
    }
    if (node->field_0)
    {
        for (iter = &node->field_1; iter->field_0 && iter->field_0 != 101 && iter->field_0 != 69; iter = &iter->field_1);
        v9 = iter;
        do
        {
            v9 = &v9->field_1;
        } while (v9->field_0 == 48);
        v0 = v10;
        if (iter->field_0 == *((char *)*((int *)*((int *)(v2 + 188)))))
            iter = &iter->field_1;
        do
        {
            j = iter->field_0;
            iter = &iter->field_1;
            v12 = &iter->field_1;
            iter->field_0 = iter->field_0;
            iter = v12;
        } while (j);
    }
    if (v4)
    {
        iter = v3;
        iter->field_70 = iter->field_70 & 4294967293;
    }
    return iter;
}
```

## `sub_1035ba26` `0x1035ba26`

_22 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1035ba26(unsigned long long *a0)
{
    unsigned short v1;  // ftop
    unsigned int v2;  // 4145

    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    v2 = _ccall(10, 13, (unsigned int)((char)(((v1 & 7) * 0x800 | (short)(CmpF((/* unsupported instruction */ ? /* unsupported instruction */ : nan), *(a0))) * 0x100 & 0x4500 & 0x4700) >> 8) & 65), 0, 0);
    if ((char)v2)
        return 0;
    return 1;
}
```

## `sub_1035ba3c` `0x1035ba3c`

_64 bytes. (leaf/helper — see body)_

```c
unsigned int [2] sub_1035ba3c(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int *a3, unsigned int a4, unsigned int a5)
{
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]

    v2 = a0;
    v1 = a5;
    v0 = a4;
    if (!a2)
    {
        sub_10361fb5(&/* unsupported instruction */);
        *(a3) = a2;
        return a3;
    }
    sub_10361f0f(&v2);
    *(a3) = v2;
    a3[1] = a0;
    return a3;
}
```

## `sub_1035ba7e` `0x1035ba7e`

_21 bytes. (leaf/helper — see body)_

```c
unsigned int [2] sub_1035ba7e(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int *a4, unsigned int a5)
{
    unsigned int v0;  // [bp+0x0]

    return sub_1035ba3c(a0, a1, a3, a4, a5, v0);
}
```

## `sub_1035ba93` `0x1035ba93`

_29 bytes. (leaf/helper — see body)_

```c
int sub_1035ba93(void)
{
    unsigned int v1;  // edi
    void* v2;  // eax

    if (v1)
        sub_10350ec0(v2 + v1, v2, sub_10352f20(v2) + 1);
    return;
}
```

## `sub_1035bab2` `0x1035bab2`

_12 bytes. (leaf/helper — see body)_

```c
typedef struct struct_3 {
    char padding_0[112];
    unsigned int field_70;
} struct_3;

struct_3 * sub_1035bab2(unsigned int a0, char *a1)
{
    unsigned int *v0;  // [bp+0x0]

    return sub_1035b935(a1, v0);
}
```

## `sub_1035bac0` `0x1035bac0`

_12 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
    char field_1;
    char padding_2[110];
    unsigned int field_70;
} struct_0;

struct_0 * sub_1035bac0(unsigned int a0, struct_0 *a1)
{
    unsigned int *v0;  // [bp+0x0]

    return sub_1035b9a6(a1, v0);
}
```

## `sub_1035bacc` `0x1035bacc`

_365 bytes. refs "e+000"_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

extern char g_103a3aa8;

int sub_1035bacc(void)
{
    char v14[5];  // eax
    unsigned int *v15;  // eax
    char v24[5];  // esi
    int v25;  // edx
    char index[5];  // esi
    int v27;  // edx
    int v16;  // eax
    char v18[5];  // esi
    char v19[5];  // eax
    char v20[5];  // esi
    char v21[5];  // ecx
    char v22[5];  // esi
    int v23;  // eax
    unsigned int v0;  // [bp-0x34]
    unsigned int v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x28]
    unsigned int v4;  // [bp-0x24]
    struct_0 v5;  // [bp-0x14]
    struct_0 *idx;  // [bp-0xc]
    char v7;  // [bp-0x8]
    int v8;  // [bp+0x4]
    int v9;  // [bp+0x8]
    unsigned int v10;  // [bp+0xc]
    unsigned int v11[4];  // [bp+0x10]
    char v12;  // [bp+0x14]
    unsigned int *v13;  // [bp+0x18]

    sub_103536a7(&v5, v13);
    if (!v14 || v8 <= 0)
    {
        v15 = sub_103575e0();
        v4 = 22;
    }
    else
    {
        if (v9 > 0)
            v16 = v9;
        else
            v16 = 0;
        if (v8 <= v16 + 9)
        {
            v15 = sub_103575e0();
            v4 = 0x22;
        }
        else
        {
            if (v12)
                sub_1035ba93();
            v18 = v14;
            if (v11[0] == 45)
            {
                v14[0] = 45;
                v18 = &v14[1];
            }
            if (v9 > 0)
            {
                v19 = &v18[1];
                v18[0] = v19[0];
                v18 = v19;
                v18[0] = *((char *)*((int *)*((int *)(v5 + 188))));
            }
            v20 = &v18[v9 + (!v12)];
            if (sub_10359f58(v20, (v8 == -1 ? -1 : v14 - v20 + v8), "e+000"))
            {
                v4 = 0;
                v3 = 0;
                v2 = 0;
                v1 = 0;
                v0 = 0;
                sub_103534f6();
            }
            v21 = &v20[2];
            if (v10)
                v20[0] = 69;
            v22 = &v20[1];
            if (*((char *)v11[3]) != 48)
            {
                v23 = v11[1] - 1;
                if (v11[1] - 1 < 0)
                {
                    v23 = -(v23);
                    v22[0] = 45;
                }
                v24 = &v22[1];
                if (v23 >= 100)
                {
                    v25 = v23 >> 31;
                    v4 = 100;
                    v24[0] = v24[0] + (char)((v25 CONCAT v23) / 100);
                    v23 = (v25 CONCAT v23) % 100;
                }
                index = &v24[1];
                if (v23 >= 10)
                {
                    v27 = v23 >> 31;
                    v4 = 10;
                    index[0] = index[0] + (char)((v27 CONCAT v23) / 10);
                    v23 = (v27 CONCAT v23) % 10;
                }
                index[1] = index[1] + (char)v23;
            }
            if ((g_103a3aa8 & 1) && v21[0] == 48)
                sub_10350ec0(v21, &v21[1], 3);
            if (!v7)
                return;
            idx[8].field_8 = idx[8].field_8 & 4294967293;
            return;
        }
    }
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    *(v15) = v4;
    sub_103535f2();
    if (v7)
        idx[8].field_8 = idx[8].field_8 & 4294967293;
    return;
}
```

## `sub_1035bc39` `0x1035bc39`

_206 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1035bc39(int *a0, char *a1, int a2, int a3, int a4, int a5)
{
    int v9;  // edi
    int v10;  // esi
    int v11;  // ebx
    unsigned int v0;  // [bp-0x50]
    unsigned int v1;  // [bp-0x4c]
    unsigned int v2;  // [bp-0x48]
    unsigned int v3;  // [bp-0x44]
    unsigned int v4;  // [bp-0x40]
    char v5;  // [bp-0x30], Other Possible Types: unsigned int
    char v6;  // [bp-0x20]
    unsigned int v7;  // [bp-0x8]
    char v8;  // [bp-0x4]

    v7 = g_1038e180 ^ &v8;
    v4 = 22;
    sub_103621d3(*(a0), a0[1], &v5, &v6, 22, v9, v10, v11);
    if (!a1 || a2 <= 0)
    {
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        *((unsigned int *)sub_103575e0()) = 22;
        sub_103535f2();
    }
    else if (sub_1036205b(&a1[(v5 == 45) + (a3 > 0)], (a2 == -1 ? -1 : a2 - (v5 == 45) - (a3 > 0)), a3 + 1, &v5))
    {
        *(a1) = 0;
    }
    else
    {
        sub_1035bacc(a2, a3, a4, &v5, 0, a5);
    }
    return sub_10351225();
}
```

## `sub_1035bd07` `0x1035bd07`

_30 bytes. (leaf/helper — see body)_

```c
int sub_1035bd07(int *a0, char *a1, int a2, int a3, int a4)
{
    return sub_1035bc39(a0, a1, a2, a3, a4, 0);
}
```

## `sub_1035bd25` `0x1035bd25`

_881 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

typedef struct struct_3 {
    char padding_0[112];
    unsigned int field_70;
} struct_3;

typedef struct struct_4 {
    char padding_0[4];
    unsigned int field_4;
} struct_4;

int sub_1035bd25(struct_4 *a0, char *a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int *a5)
{
    unsigned int v15;  // esi
    unsigned int v16;  // edi
    char v25[9];  // esi
    unsigned int v26;  // ebx
    char v27[9];  // esi
    char iter[9];  // esi
    unsigned int v29;  // eax
    unsigned int v30;  // ecx
    char iter1[9];  // eax
    char v32[9];  // esi
    unsigned int v33;  // eax
    unsigned int v34;  // 4106
    char iter2[9];  // esi
    int v35;  // eax
    int v36;  // edx
    unsigned int v37;  // 4141
    unsigned int v38;  // 4101
    char node[9];  // esi
    int v40;  // eax
    char v42[9];  // edi
    unsigned int v43;  // edx
    int v44;  // ecx
    int *v18;  // eax
    unsigned int v45;  // 4101
    unsigned int v46;  // 4101
    unsigned int v19;  // ebx
    char v20[9];  // ebx
    int v21;  // eax
    char v22[9];  // esi
    char v23[4];  // eax
    char v24[9];  // esi
    unsigned int v0;  // [bp-0x44]
    unsigned int v1;  // [bp-0x40]
    unsigned int v2;  // [bp-0x3c]
    unsigned int v3;  // [bp-0x38]
    int v4;  // [bp-0x34], Other Possible Types: unsigned int
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    struct_0 v7;  // [bp-0x28]
    struct_3 *idx;  // [bp-0x20]
    char v9;  // [bp-0x1c]
    unsigned int v10;  // [bp-0x18]
    unsigned int v11;  // [bp-0x14]
    unsigned int v12;  // [bp-0x10]
    unsigned int v13;  // [bp-0xc]
    unsigned int v14;  // [bp-0x8]

    v6 = v15;
    v5 = v16;
    v10 = 0x3ff;
    v14 = 48;
    sub_103536a7(&v7, a5);
    if (a3 < 0)
        a3 = 0;
    iter2 = a1;
    if (!iter2 || a2 <= 0)
    {
        v18 = sub_103575e0();
        v4 = 22;
    }
    else
    {
        iter2[0] = 0;
        if (a2 <= a3 + 11)
        {
            v18 = sub_103575e0();
            v4 = 0x22;
        }
        else
        {
            v12 = (unsigned int)a0->padding_0;
            v4 = v19;
            if (((unsigned short)(a0->field_4 >> 20) & 0x7ff) == 0x7ff)
            {
                v20 = &iter2[2];
                v21 = sub_1035bd07(a0, v20, (a2 == 4294967295 ? 4294967295 : a2 - 2), a3, 0);
                if (v21)
                {
                    iter2[0] = 0;
                    if (v9)
                        idx->field_70 = idx->field_70 & 4294967293;
                }
                else
                {
                    if (v20[0] == 45)
                    {
                        iter2[0] = 45;
                        iter2 = &iter2[1];
                    }
                    iter2[0] = 48;
                    v22 = &iter2[1];
                    v22[0] = ((char)((!a4) + 1) & 224) + 120;
                    v23 = sub_10352ea0(&v22[1], 101);
                    if (v23)
                    {
                        v23[0] = ((char)((!a4) + 1) & 224) + 112;
                        v23[3] = 0;
                    }
LABEL_1035c082:
                    if (v9)
                        idx->field_70 = idx->field_70 & 4294967293;
                    v21 = 0;
                }
            }
            else
            {
                if ((a0->field_4 & 0x80000000))
                {
                    iter2[0] = 45;
                    iter2 = &iter2[1];
                }
                iter2[0] = 48;
                v24 = &iter2[1];
                v24[0] = ((char)((!a4) + 1) & 224) + 120;
                v25 = &v24[1];
                v26 = (-(0 < a4) & 0xffffffe0) + 39;
                if (!(a0->field_4 & 0x7ff00000))
                {
                    v25[0] = 48;
                    v27 = &v25[1];
                    v10 = (!a0->padding_0 && !(a0->field_4 & 0xfffff) ? 0 : 0x3fe);
                }
                else
                {
                    v25[0] = 49;
                    v27 = &v25[1];
                }
                iter = &v27[1];
                a1 = v27;
                if (!a3)
                    a1[0] = 0;
                else
                    a1[0] = *((char *)*((int *)*((int *)(v7 + 188))));
                v13 = a0->field_4 & 0xfffff;
                if ((a0->field_4 & 0xfffff) || a0->padding_0 > 0)
                {
                    v12 = 0;
                    v13 = 0xf0000;
                    do
                    {
                        if (a3 <= 0)
                            break;
                        v29 = (unsigned short)sub_10362350() + 48;
                        if ((unsigned short)v29 > 57)
                            v29 += v26;
                        v30 = v13;
                        v14 -= 4;
                        iter[0] = v29;
                        iter = &iter[1];
                        a3 -= 1;
                        v12 = (v30 CONCAT v12) >> 4;
                        v13 = v30 >> 4;
                    } while ((unsigned short)v14 >= 0);
                    if ((unsigned short)v14 >= 0 && (unsigned short)sub_10362350() > 8)
                    {
                        for (iter1 = &iter[1]; iter1[0] == 0x66 || iter1[0] == 70; iter1 = &iter1[1])
                        {
                            iter1[0] = 48;
                        }
                        if (iter1 == a1)
                        {
                            iter1[1] = iter1[1] + 1;
                        }
                        else if (iter1[0] == 57)
                        {
                            iter1[0] = (char)v26 + 58;
                        }
                        else
                        {
                            iter1[0] = iter1[0] + 1;
                        }
                    }
                }
                if (a3 > 0)
                {
                    sub_10350ad0(iter, 48, a3);
                    iter = &iter[a3];
                }
                if (!a1[0])
                    iter = a1;
                iter[0] = ((char)((!a4) + 1) & 224) + 112;
                v32 = &iter[1];
                v33 = sub_10362350() & 0x7ff;
                v34 = v10;
                v35 = v33 - v34;
                v3 = 0;
                v36 = 4294967295 - (v33 < v34);
                v37 = _ccall(8, 12, 0, 0 ^ (unsigned int)(char)(v33 < v34), (unsigned int)(char)(v33 < v34));
                if (!((char)v37) && !((v38 = (unsigned int)_ccall(14, 12, 0, 0 ^ (unsigned int)(char)(v33 < v34), (unsigned int)(char)(v33 < v34)), (char)v38 && v35 < 0)))
                {
                    v32[0] = 43;
                    node = &v32[1];
                    v40 = v35;
                }
                else
                {
                    v32[0] = 45;
                    node = &v32[1];
                    v36 = -(v36 + (0 < v35));
                    v40 = -(v35);
                }
                v42 = node;
                node[0] = 48;
                if (v36 >= 0 && (v36 > 0 || v40 >= 1000))
                {
                    node[0] = (char)sub_10362270(v40, v36, 1000, 0) + 48;
                    node = &node[1];
                    v11 = v43;
                    v40 = v44;
                    v36 = 0;
                    if (node != v42)
                        goto LABEL_1035c03c;
                }
                if (v36 < 0 || (v45 = (unsigned int)_ccall(14, 15, v36, 0, 0), (char)v45 && v40 < 100))
                    goto LABEL_1035c053;
LABEL_1035c03c:
                node[0] = (char)sub_10362270(v40, v36, 100, 0) + 48;
                v11 = v43;
                node = &node[1];
                v40 = v44;
                v36 = 0;
LABEL_1035c053:
                if (node != v42 || v36 >= 0 && !((v46 = (unsigned int)_ccall(14, 15, v36, 0, 0), (char)v46 && v40 < 10)))
                {
                    node[0] = (char)sub_10362270(v40, v36, 10, 0) + 48;
                    v11 = v43;
                    node = &node[1];
                    v40 = v44;
                    v11 = 0;
                }
                node[0] = (char)v40 + 48;
                node[1] = 0;
                goto LABEL_1035c082;
            }
            return v21;
        }
    }
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    *(v18) = v4;
    sub_103535f2();
    if (v9)
        idx->field_70 = idx->field_70 & 4294967293;
    return v4;
}
```

## `sub_1035c096` `0x1035c096`

_245 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

int sub_1035c096(void)
{
    void* index;  // eax
    unsigned int v13;  // esi
    char v14[2];  // ecx
    char v15[2];  // eax
    char v16[2];  // esi
    char v17[2];  // esi
    unsigned int v0;  // [bp-0x34]
    unsigned int v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x28]
    unsigned int v4;  // [bp-0x24]
    struct_0 v5;  // [bp-0x14]
    struct_0 *idx;  // [bp-0xc]
    char v7;  // [bp-0x8]
    unsigned int v8;  // [bp+0x4]
    unsigned int v9;  // [bp+0x8]
    char v10;  // [bp+0xc]
    unsigned int *v11;  // [bp+0x10]

    v13 = (int)index[4] - 1;
    sub_103536a7(&v5, v11);
    if (v14 && v8 > NULL)
    {
        if (v10 && v13 == v9)
        {
            v15 = &v14[v13 + (*((int *)index) == 45)];
            v15[0] = 48;
            v15[1] = 0;
        }
        v16 = v14;
        if (*((int *)index) == 45)
        {
            v14[0] = 45;
            v16 = &v14[1];
        }
        if ((int)index[4] <= NULL)
        {
            sub_1035ba93();
            v16[0] = 48;
            v17 = &v16[1];
        }
        else
        {
            v17 = &v16[index[4]];
        }
        if (v9 > NULL)
        {
            sub_1035ba93();
            v17[0] = *((char *)*((int *)*((int *)(v5 + 188))));
            if ((int)index[4] < NULL)
            {
                if (v10 || v9 >= v9)
                    v9 = -((int)index[4]);
                sub_1035ba93();
                sub_10350ad0(&v17[1], 48, v9);
            }
        }
        if (!v7)
            return;
        idx[8].field_8 = idx[8].field_8 & 4294967293;
        return;
    }
    v4 = 22;
    *((unsigned int *)sub_103575e0()) = 22;
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    sub_103535f2();
    if (v7)
        idx[8].field_8 = idx[8].field_8 & 4294967293;
    return;
}
```

## `sub_1035c18b` `0x1035c18b`

_185 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1035c18b(int *a0, char *a1, int a2, int a3, int a4)
{
    int v10;  // edi
    int v11;  // esi
    int v12;  // ebx
    unsigned int v0;  // [bp-0x50]
    unsigned int v1;  // [bp-0x4c]
    unsigned int v2;  // [bp-0x48]
    unsigned int v3;  // [bp-0x44]
    unsigned int v4;  // [bp-0x40]
    char v5;  // [bp-0x30], Other Possible Types: unsigned int
    unsigned int v6;  // [bp-0x2c]
    char v7;  // [bp-0x20]
    unsigned int v8;  // [bp-0x8]
    char v9;  // [bp-0x4]

    v8 = g_1038e180 ^ &v9;
    v4 = 22;
    sub_103621d3(*(a0), a0[1], &v5, &v7, 22, v10, v11, v12);
    if (!a1 || a2 <= 0)
    {
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        *((unsigned int *)sub_103575e0()) = 22;
        sub_103535f2();
    }
    else if (sub_1036205b(&a1[v5 == 45], (a2 == -1 ? -1 : a2 - (v5 == 45)), v6 + a3, &v5))
    {
        *(a1) = 0;
    }
    else
    {
        sub_1035c096(a2, a3, 0, a4);
    }
    return sub_10351225();
}
```

## `sub_1035c244` `0x1035c244`

_248 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1035c244(int *a0, char *a1, int a2, int a3, int a4, int a5)
{
    int v11;  // edi
    int v12;  // esi
    int v13;  // ebx
    unsigned int v14;  // eax
    void* v15;  // edi
    int v16;  // eax
    void* v17;  // edi
    unsigned int v0;  // [bp-0x54]
    unsigned int v1;  // [bp-0x50]
    unsigned int v2;  // [bp-0x4c]
    unsigned int v3;  // [bp-0x48]
    unsigned int v4;  // [bp-0x44]
    char v5;  // [bp-0x34], Other Possible Types: unsigned int
    int v6;  // [bp-0x30]
    int v7;  // [bp-0x24]
    char v8;  // [bp-0x20]
    unsigned int v9;  // [bp-0x8]
    char v10;  // [bp-0x4]

    v9 = g_1038e180 ^ &v10;
    v4 = 22;
    sub_103621d3(*(a0), a0[1], &v5, &v8, 22, v11, v12, v13);
    if (!a1 || a2 <= 0)
    {
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        *((unsigned int *)sub_103575e0()) = 22;
        sub_103535f2();
    }
    else
    {
        v7 = v6 - 1;
        v14 = v5 == 45;
        v15 = &a1[v14];
        if (sub_1036205b(v15, (a2 == -1 ? -1 : a2 - v14), a3, &v5))
        {
            *(a1) = 0;
        }
        else
        {
            v16 = v6 - 1;
            if (v16 >= -0x4 && v16 < a3)
            {
                if (v7 < v16)
                {
                    do
                    {
                        v15 += 1;
                    } while (*((char *)v15));
                    *((char *)&v17[2]) = 0;
                }
                sub_1035c096(a2, a3, 1, a5);
            }
            else
            {
                sub_1035bacc(a2, a3, a4, &v5, 1, a5);
            }
        }
    }
    return sub_10351225();
}
```

## `sub_1035c33c` `0x1035c33c`

_134 bytes. (leaf/helper — see body)_

```c
int sub_1035c33c(void* a0, char *a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6)
{
    if (a3 != 101 && a3 != 69)
    {
        if (a3 == 0x66)
            return sub_1035c18b(a0, a1, a2, a4, a6);
        if (a3 == 97 || a3 == 65)
            return sub_1035bd25(a0, a1, a2, a4, a5, a6);
        return sub_1035c244(a0, a1, a2, a4, a5, a6);
        return sub_1035bd25(a0, a1, a2, a4, a5, a6);
    }
    return sub_1035bc39(a0, a1, a2, a4, a5, a6);
}
```

## `sub_1035c3c2` `0x1035c3c2`

_33 bytes. (leaf/helper — see body)_

```c
int sub_1035c3c2(void* a0, char *a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5)
{
    return sub_1035c33c(a0, a1, a2, a3, a4, a5, 0);
}
```

## `sub_1035c3e3` `0x1035c3e3`

_31 bytes. (leaf/helper — see body)_

```c
extern char g_1038ec80;

unsigned int sub_1035c3e3(void)
{
    unsigned int i;  // edi
    unsigned int v3;  // esi
    unsigned int v4;  // eax
    unsigned int v0;  // [bp-0xc]

    i = 0;
    do
    {
        v3 = &(&g_1038ec80)[i];
        v0 = *((int *)v3);
        i += 4;
        *((unsigned int *)v3) = sub_10358b15();
    } while (i < 40);
    return v4;
}
```

## `sub_1035c402` `0x1035c402`

_41 bytes. (leaf/helper — see body)_

```c
void sub_1035c402(void)
{
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    int v5;  // [bp-0x4]

    if (sub_10362378(0, 0x10000, 0x30000, v5))
    {
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        sub_103534f6();
    }
    return;
}
```

## `sub_1035c467` `0x1035c467`

_101 bytes. refs "KERNEL32", "IsProcessorFeaturePresent"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;

unsigned int sub_1035c467(void)
{
    unsigned int v4;  // eax
    unsigned int *v5;  // eax
    unsigned short v14;  // ftop
    unsigned short v15;  // ftop
    unsigned int v17;  // 4143
    unsigned int v6;  // ftop
    unsigned int v7;  // ftop
    unsigned int v8;  // ftop
    unsigned int v9;  // ftop
    unsigned int v10;  // ftop
    unsigned int v11;  // ftop
    unsigned int v12;  // ftop
    unsigned short v13;  // ftop
    double v0;  // [bp-0x28], Other Possible Types: unsigned long
    double v1;  // [bp-0x20], Other Possible Types: unsigned long
    double v2;  // [bp-0x18]

    v4 = g_1038b050("KERNEL32");
    if (v4)
    {
        v5 = g_1038b078(v4, "IsProcessorFeaturePresent");
        if (v5)
            return v5(0);
    }
    v7 = v6 - 1;
    if (/* unsupported instruction */)
    {
        v8 = v7 - 1;
        /* unsupported instruction */
        /* unsupported instruction */
    }
    else
    {
        v8 = v7 - 1;
        /* unsupported instruction */
        /* unsupported instruction */
    }
    if (/* unsupported instruction */)
    {
        v1 = /* unsupported instruction */;
        /* unsupported instruction */
        v9 = v8 + 1;
    }
    else
    {
        v1 = (double)nan;
        /* unsupported instruction */
        v9 = v8 + 1;
    }
    v10 = v9 - 1;
    if (/* unsupported instruction */)
    {
        v11 = v10 - 1;
        /* unsupported instruction */
        /* unsupported instruction */
    }
    else
    {
        v11 = v10 - 1;
        /* unsupported instruction */
        /* unsupported instruction */
    }
    if (/* unsupported instruction */)
    {
        v0 = /* unsupported instruction */;
        /* unsupported instruction */
        v12 = v11 + 1;
    }
    else
    {
        v0 = (double)nan;
        /* unsupported instruction */
        v12 = v11 + 1;
    }
    v13 = v12 - 1;
    if (/* unsupported instruction */)
    {
        v14 = v13 - 1;
        /* unsupported instruction */
        /* unsupported instruction */
    }
    else
    {
        v14 = v13 - 1;
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
        v2 = (double)/* unsupported instruction */;
        /* unsupported instruction */
        v15 = v14 + 1;
    }
    else
    {
        v2 = (double)nan;
        /* unsupported instruction */
        v15 = v14 + 1;
    }
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    v17 = _ccall(10, 13, (unsigned int)((char)(((v15 & 7) * 0x800 | (short)(CmpF((/* unsupported instruction */ ? /* unsupported instruction */ : nan), v2)) * 0x100 & 0x4500 & 0x4700) >> 8) & 5), 0, 0);
    if ((char)v17)
        return 0;
    return 1;
}
```

## `sub_1035c490` `0x1035c490`

_146 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
} struct_0;

extern struct_0 *g_1038b268;
extern unsigned int g_103a12a0;
extern unsigned int g_103a36c8;
extern unsigned int g_103a4cc0;

void sub_1035c490(unsigned int a0)
{
    void* v9;  // ebx
    unsigned int v10;  // ecx
    unsigned int v11;  // edx
    struct_0 *v12;  // eax
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    struct_0 *v5;  // [bp+0xfffe4]
    unsigned int v6;  // [bp+0xfffe8]
    unsigned int v7;  // [bp+0x100000]
    void* v8;  // [bp+0x10000c]

    sub_1035b0cc(&g_103a12a0, 16);
    v9 = v8;
    if (!v9)
    {
        *((unsigned int *)sub_103575e0()) = 22;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        sub_103535f2();
        sub_1035b111(0, 0, 0, &g_103a12a0);
        return;
    }
    if (g_103a4cc0 == 3)
    {
        sub_1035a599(v10, v11, 4);
        v7 = 0;
        v12 = sub_1035a612(v9);
        v5 = v12;
        if (v12)
            v6 = (int)v9[4] - 9;
        v7 = 4294967294;
        sub_1035c52a();
        if (v5)
        {
            v9 = v9;
            sub_1035b111(v2, v3, v9, &g_103a12a0);
            return;
        }
    }
    v3 = 0;
    v2 = g_103a36c8;
    g_1038b268(g_103a36c8, 0, v9);
    sub_1035b111(v2, v3, v9, &g_103a12a0);
    return;
}
```

## `sub_1035c522` `0x1035c522`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1035c522(void)
{
    sub_1035c52a();
    return;
}
```

## `sub_1035c52a` `0x1035c52a`

_9 bytes. (leaf/helper — see body)_

```c
int sub_1035c52a(void)
{
    return sub_1035a4c1(4);
}
```

## `sub_1035c533` `0x1035c533`

_36 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
} struct_0;

extern struct_0 *g_103990cc;

struct_0 ** sub_1035c533(void)
{
    struct_0 **iter;  // esi

    iter = &g_103990cc;
    return &g_103990cc;
}
```

## `sub_1035c557` `0x1035c557`

_36 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
} struct_0;

extern struct_0 *g_103990d4;

struct_0 ** sub_1035c557(void)
{
    struct_0 **iter;  // esi

    iter = &g_103990d4;
    return &g_103990d4;
}
```

## `sub_1035c580` `0x1035c580`

_41 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1035c580(void* a0)
{
    void* v0;  // eax

    if (*((short *)a0) != 23117)
        return 0;
    v0 = (int)a0[60] + a0;
    if (*((int *)v0) == 17744)
        return (short)v0[24] == 267;
    return 0;
}
```

## `sub_1035c5b0` `0x1035c5b0`

_66 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[6];
    unsigned short field_6;
    char padding_8[12];
    unsigned short field_14;
    char padding_16[38];
    unsigned int field_3c;
} struct_0;

unsigned int [10] sub_1035c5b0(struct_0 *a0, unsigned int a1)
{
    struct_0 *v0;  // ecx
    unsigned int v1;  // esi
    unsigned int v2;  // edx
    unsigned int v3[10];  // eax

    v0 = &a0->padding_0[a0->field_3c];
    v1 = v0->field_6;
    v2 = 0;
    v3 = &v0->padding_0[v0->field_14 + 24];
    if (v1)
    {
        do
        {
            if (a1 >= v3[3] && a1 < v3[2] + v3[3])
                return v3;
        } while ((v2 += 1, v3 += 40, v2 < v1));
    }
    return NULL;
}
```

## `sub_1035c600` `0x1035c600`

_164 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[6];
    unsigned short field_6;
    char padding_8[12];
    unsigned short field_14;
    char padding_16[38];
    unsigned int field_3c;
} struct_0;

extern char g_10000000;
extern unsigned int g_1038e180;
extern unsigned int g_103a12c0;

unsigned int sub_1035c600(unsigned int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4152
    unsigned long v11;  // 4174
    struct_0 *v12;  // eax
    unsigned int v13;  // eax
    unsigned long v14;  // 4150
    unsigned long v15;  // 4125
    unsigned int v0;  // [bp-0x2c]
    char *v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]

    v5 = 4294967294;
    v4 = &g_103a12c0;
    v3 = sub_10354150;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v4 ^= g_1038e180;
    v0 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = &v0;
    v5 = 0;
    if (sub_1035c580(&g_10000000))
    {
        v12 = sub_1035c5b0(&g_10000000, a0 - &g_10000000);
        if (v12)
        {
            v13 = *((int *)&v12->padding_16[14]);
            v14 = _ccall(v7, v8, (unsigned int)v9, 0);
            *((unsigned int *)v14) = v2;
            return ~(v13 >> 31) & 1;
        }
    }
    v15 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v15) = v2;
    return 0;
}
```

## `sub_1035c689` `0x1035c689`

_20 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

int sub_1035c689(void)
{
    struct_0 **v1;  // [bp+0xffff0]

    return *(v1)->field_0 == 3221225477;
}
```

## `sub_1035c69d` `0x1035c69d`

_3 bytes. (leaf/helper — see body)_

```c
void sub_1035c69d(void)
{
}
```

## `sub_1035c6bb` `0x1035c6bb`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1035c6bb(void)
{
    return;
}
```

## `sub_1035c6bc` `0x1035c6bc`

_350 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    char padding_0[92];
    struct struct_0 *field_5c;
    unsigned int field_60;
    unsigned int field_64;
} struct_2;

typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    struct struct_1 *field_8;
    char field_c;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern int g_1038ed20;
extern unsigned int g_1038ed24;
extern unsigned int g_1038ed2c;

struct_2 * sub_1035c6bc(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    struct_2 *idx;  // esi
    struct_0 *v5;  // edx
    unsigned int v14;  // ecx
    unsigned int v15;  // eax
    unsigned int v16;  // edi
    unsigned int v6;  // edi
    unsigned int v7;  // ebx
    struct_0 *v8;  // ecx
    struct_0 *iter;  // ecx
    unsigned int *v10;  // ebx
    struct_2 *v11;  // eax
    unsigned int v12;  // ecx
    int i;  // edx
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0xc]
    unsigned int *v3;  // [bp-0x8], Other Possible Types: unsigned int

    v3 = a0;
    v2 = a0;
    idx = sub_10358d31();
    if (!idx)
        return idx;
    v5 = idx->field_5c;
    v1 = v6;
    v0 = v7;
    v8 = v5;
    do
    {
        iter = v8;
    } while (iter->field_0 != a2 && (iter += 12, v8 = iter, v8 < g_1038ed2c * 12 + v5));
    if (iter >= &(&v5->field_0)[3 * g_1038ed2c] || iter->field_0 != a2)
        iter = NULL;
    if (!iter || (v10 = (unsigned int *)iter->field_8, v3 = v10, !v10))
    {
        v11 = NULL;
    }
    else if (v10 == 0x5)
    {
        iter->field_8 = NULL;
        v11 = 0x1;
    }
    else
    {
        if (v10 != 0x1)
        {
            v2 = idx->field_60;
            idx->field_60 = a3;
            v12 = iter->field_4;
            if (v12 == 8)
            {
                i = g_1038ed20;
                if (g_1038ed20 < g_1038ed24 + g_1038ed20)
                {
                    v14 = g_1038ed20 * 12;
                    do
                    {
                        *((unsigned int *)(8 + v14 + (char *)idx->field_5c)) = 0;
                        i += 1;
                        v14 += 12;
                    } while (i < g_1038ed24 + g_1038ed20);
                    v10 = v3;
                }
                v15 = iter->field_0;
                v16 = idx->field_64;
                if (v15 == 3221225614)
                {
                    idx->field_64 = 131;
                }
                else if (v15 == 3221225616)
                {
                    idx->field_64 = 129;
                }
                else if (v15 == 3221225617)
                {
                    idx->field_64 = 132;
                }
                else if (v15 == 3221225619)
                {
                    idx->field_64 = 133;
                }
                else if (v15 == 3221225613)
                {
                    idx->field_64 = 130;
                }
                else if (v15 == 3221225615)
                {
                    idx->field_64 = 134;
                }
                else if (v15 == 3221225618)
                {
                    idx->field_64 = 138;
                }
                v10(8, idx->field_64);
                idx->field_64 = v16;
            }
            else
            {
                iter->field_8 = NULL;
                v10(v12);
            }
            idx->field_60 = v2;
        }
        v11 = 0xffffffff;
    }
    return v11;
}
```

## `sub_1035c81a` `0x1035c81a`

_27 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    char padding_0[92];
    struct struct_0 *field_5c;
    unsigned int field_60;
    unsigned int field_64;
} struct_2;

typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    struct struct_1 *field_8;
    char field_c;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

struct_2 * sub_1035c81a(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    if (a2 != 3765269347)
        return NULL;
    return sub_1035c6bc(a0, a1, 3765269347, a3);
}
```

## `sub_1035c835` `0x1035c835`

_25 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a3860;
extern unsigned int g_103a3864;
extern unsigned int g_103a3868;
extern unsigned int g_103a386c;

int sub_1035c835(unsigned int a0)
{
    g_103a3860 = a0;
    g_103a3864 = a0;
    g_103a3868 = a0;
    g_103a386c = a0;
    return a0;
}
```

