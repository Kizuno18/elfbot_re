# elfbot.dll decompiled — jiru 0x10358798..0x1035a508

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10358798` `0x10358798`

_143 bytes. (leaf/helper — see body)_

```c
char * sub_10358798(char *a0, unsigned int a1, unsigned int a2)
{
    char *v3;  // eax
    unsigned int v4;  // edi
    unsigned int v5;  // edx
    char *v6;  // eax
    unsigned int v7;  // edx
    unsigned int v8;  // edx
    char *v9;  // eax
    char *iter;  // edi
    unsigned int v11;  // ecx
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char *node;  // [bp-0xc]

    v3 = a0;
    v4 = ((v3 ^ v3 >> 31) - (v3 >> 31) & 15 ^ v3 >> 31) - (v3 >> 31);
    if (!v4)
    {
        v5 = a2 & 127;
        v1 = v5;
        v6 = v3;
        v7 = v5;
        if (a2 != v7)
        {
            sub_10358741(v3, a2 - v5);
            v6 = a0;
            v7 = v1;
        }
        v8 = v7;
        v9 = v6;
        if (!v8)
            return v9;
        for (node = &v9[a2 + -1 * v8]; v1; node += 1)
        {
            v1 -= 1;
            *(node) = 0;
        }
        return a0;
    }
    else
    {
        v0 = -(v4) + 16;
        iter = a0;
        for (v11 = v0; v11; iter += 1)
        {
            v11 -= 1;
            *(iter) = 0;
        }
        sub_10358798(&a0[v0], 0, a2 - v0);
        return a0;
    }
}
```

## `sub_10358827` `0x10358827`

_20 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a4cc4;

unsigned int sub_10358827(void)
{
    g_103a4cc4 = 0;
    g_103a4cc4 = sub_103603e2();
    return 0;
}
```

## `sub_1035883b` `0x1035883b`

_129 bytes. (leaf/helper — see body)_

```c
void sub_1035883b(uint128_t *iter, uint128_t *node, unsigned int a2)
{
    unsigned int i;  // ecx
    int v1;  // xmm1
    int v2;  // xmm2
    int v3;  // xmm3
    int v4;  // xmm5
    int v5;  // xmm6
    int v6;  // xmm7

    i = a2 >> 7;
    do
    {
        v1 = (int)node[1];
        v2 = (int)node[2];
        v3 = (int)node[3];
        *(iter) = *(node);
        *((void*)&iter[1]) = v1;
        *((void*)&iter[2]) = v2;
        *((void*)&iter[3]) = v3;
        v4 = (int)node[5];
        v5 = (int)node[6];
        v6 = (int)node[7];
        iter[4] = node[4];
        *((void*)&iter[5]) = v4;
        *((void*)&iter[6]) = v5;
        *((void*)&iter[7]) = v6;
        node += 8;
        iter += 8;
        i -= 1;
    } while (i != 1);
    return;
}
```

## `sub_10358855` `0x10358855`

_6 bytes. (leaf/helper — see body)_

```c
void sub_10358855(void)
{
}
```

## `sub_103588c2` `0x103588c2`

_227 bytes. (leaf/helper — see body)_

```c
void* sub_103588c2(void* a0, void* iter, unsigned int a2)
{
    void* v4;  // eax
    unsigned int v5;  // ecx
    void* node;  // edi
    void* iter1;  // esi
    unsigned int v16;  // ecx
    unsigned int k;  // ecx
    void* v18;  // edi
    void* iter2;  // edi
    unsigned int v20;  // ecx
    unsigned int v6;  // edi
    unsigned int v7;  // esi
    unsigned int v8;  // ecx
    void* v9;  // eax
    unsigned int v10;  // ecx
    unsigned int v11;  // ecx
    void* v12;  // eax
    unsigned int v13;  // ebx
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    char *i;  // [bp-0x18]
    char *v3;  // [bp-0x14]

    v4 = a0;
    v5 = ((iter ^ iter >> 31) - (iter >> 31) & 15 ^ iter >> 31) - (iter >> 31);
    v6 = ((v4 ^ v4 >> 31) - (v4 >> 31) & 15 ^ v4 >> 31) - (v4 >> 31);
    if (!v5 && !v6)
    {
        v7 = a2;
        v8 = v7 & 127;
        v1 = v8;
        v9 = v4;
        v10 = v8;
        if (v7 != v10)
        {
            sub_1035883b(v4, iter, v7 - v8);
            v9 = a0;
            v10 = v1;
        }
        v11 = v10;
        v12 = v9;
        if (!v11)
            return v12;
        v13 = a2;
        i = iter + v13 - v11;
        for (v3 = v13 + v12 - v11; v1; i += 1)
        {
            v1 -= 1;
            *(v3) = *(i);
            v3 += 1;
        }
        return a0;
    }
    else if (v5 == v6)
    {
        v0 = -(v5) + 16;
        node = a0;
        iter1 = iter;
        for (v16 = v0; v16; iter1 += 1)
        {
            v16 -= 1;
            *((char *)node) = *((char *)iter1);
            node += 1;
        }
        sub_103588c2(a0 + v0, iter + v0, a2 - v0);
        return a0;
    }
    else
    {
        k = a2 >> 2;
        v18 = a0;
        while (k)
        {
            iter2 = v18;
            if (!k)
                break;
            k -= 1;
            *((int *)iter2) = *((int *)iter);
            v18 = iter2 + 4;
            iter += 4;
            break;
        }
        for (v20 = a2 & 3; v20; iter += 1)
        {
            v20 -= 1;
            *((char *)iter2) = *((char *)iter);
            iter2 += 1;
        }
        return a0;
    }
}
```

## `sub_10358aa9` `0x10358aa9`

_108 bytes. refs ".mixcrt"_

```c
typedef struct struct_1 {
    char padding_0[6];
    unsigned short field_6;
    char padding_8[12];
    unsigned short field_14;
    char padding_16[38];
    unsigned int field_3c;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;

unsigned int sub_10358aa9(unsigned int a0)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // esi
    unsigned int v8;  // ebx
    unsigned int v9;  // edi
    struct_1 *v10;  // eax
    struct_1 *v11;  // esi
    int v12;  // edi
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]
    int v4;  // [bp-0x8]

    v3 = a0;
    v2 = a0;
    v1 = v6;
    v0 = v7;
    v8 = 0;
    v2 = 1;
    v4 = 0;
    sub_10353d72(&v4);
    if (v4 > 5)
        return 1;
    v10 = g_1038b050(0, v9);
    v11 = &v10->padding_0[v10->field_3c];
    v12 = &v11->padding_0[v11->field_14 + 24];
    if (v11->field_6 > 0)
    {
        do
        {
            if (!sub_10359ed0(".mixcrt", v12))
            {
                v2 = 0;
                break;
            }
        } while ((v8 += 1, v12 = (int)(v12 + 40), v8 < (unsigned int)v11->field_6));
    }
    return v2;
}
```

## `sub_10358b15` `0x10358b15`

_110 bytes. refs "KERNEL32.DLL", "KERNEL32.DLL", "KERNEL32.DLL"_

```c
typedef struct struct_1 {
    char padding_0[504];
    struct struct_0 *field_1f8;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern struct_0 *g_1038b234;
extern unsigned int g_1038e468;
extern unsigned int g_1038e46c;

unsigned int sub_10358b15(void)
{
    unsigned int v3;  // esi
    unsigned int *v4;  // eax
    struct_1 *v5;  // eax
    unsigned int *v6;  // eax
    unsigned int v7;  // esi
    unsigned int v8;  // ecx
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]

    if (g_1038b234(g_1038e46c, v3) && g_1038e468 != 4294967295)
    {
        v4 = g_1038b234(g_1038e46c, g_1038e468);
        v5 = v4(g_1038e46c, g_1038e468);
        if (!v5)
            goto LABEL_10358b49;
        v6 = &v5->field_1f8->field_0;
    }
    else
    {
LABEL_10358b49:
        v1 = "KERNEL32.DLL";
        v7 = g_1038b050("KERNEL32.DLL");
        if (!v7)
        {
            return "KERNEL32.DLL";
        }
        else if (sub_10358aa9(v8))
        {
            v6 = g_1038b078(v7, "EncodePointer");
        }
        else
        {
            return "KERNEL32.DLL";
        }
    }
    if (v6)
        v0 = v6(v1);
    return v1;
}
```

## `sub_10358b83` `0x10358b83`

_9 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10358b83(void)
{
    unsigned int v0;  // [bp-0x4]

    v0 = 0;
    return sub_10358b15();
}
```

## `sub_10358b8c` `0x10358b8c`

_110 bytes. refs "KERNEL32.DLL", "KERNEL32.DLL", "KERNEL32.DLL"_

```c
typedef struct struct_1 {
    char padding_0[508];
    struct struct_0 *field_1fc;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern struct_0 *g_1038b234;
extern unsigned int g_1038e468;
extern unsigned int g_1038e46c;

unsigned int sub_10358b8c(void)
{
    unsigned int v3;  // esi
    unsigned int *v4;  // eax
    struct_1 *v5;  // eax
    unsigned int *v6;  // eax
    unsigned int v7;  // esi
    unsigned int v8;  // ecx
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]

    if (g_1038b234(g_1038e46c, v3) && g_1038e468 != 4294967295)
    {
        v4 = g_1038b234(g_1038e46c, g_1038e468);
        v5 = v4(g_1038e46c, g_1038e468);
        if (!v5)
            goto LABEL_10358bc0;
        v6 = &v5->field_1fc->field_0;
    }
    else
    {
LABEL_10358bc0:
        v1 = "KERNEL32.DLL";
        v7 = g_1038b050("KERNEL32.DLL");
        if (!v7)
        {
            return "KERNEL32.DLL";
        }
        else if (sub_10358aa9(v8))
        {
            v6 = g_1038b078(v7, "DecodePointer");
        }
        else
        {
            return "KERNEL32.DLL";
        }
    }
    if (v6)
        v0 = v6(v1);
    return v1;
}
```

## `sub_10358bfa` `0x10358bfa`

_9 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b238;

void sub_10358bfa(void)
{
    g_1038b238();
    return;
}
```

## `sub_10358c03` `0x10358c03`

_50 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b234;
extern struct_0 *g_1038b23c;
extern unsigned int g_1038e46c;
extern unsigned int g_103a3390;

unsigned int sub_10358c03(void)
{
    unsigned int v2;  // esi
    unsigned int v3;  // esi
    unsigned int v4;  // esi
    unsigned int v0;  // [bp-0xc]

    v3 = g_1038b234(g_1038e46c, v2);
    if (v3)
        return v3;
    v0 = g_103a3390;
    v4 = sub_10358b8c();
    g_1038b23c(g_1038e46c, v4);
    return v4;
}
```

## `sub_10358c35` `0x10358c35`

_146 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1f8;
extern struct_0 *g_1038b240;
extern unsigned int g_1038e468;
extern unsigned int g_1038e46c;
extern unsigned int g_1038e540[2];
extern unsigned int g_1038e660[2];
extern unsigned int g_103a3398;

int sub_10358c35(void)
{
    unsigned int *v5;  // eax
    unsigned int v6;  // ebx
    unsigned int v7;  // esi
    unsigned int iter[2];  // esi
    unsigned int v9;  // edi
    unsigned int v10;  // edi
    unsigned int node[2];  // esi
    unsigned int v12;  // eax
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    unsigned int v3;  // [bp-0x4]

    if (g_1038e468 != 4294967295)
    {
        v2 = g_103a3398;
        v5 = sub_10358b8c();
        v5(g_1038e468);
        g_1038e468 = 4294967295;
    }
    if (g_1038e46c != 4294967295)
    {
        g_1038b240(g_1038e46c);
        g_1038e46c = 4294967295;
    }
    v3 = v6;
    v2 = v7;
    iter = &g_1038e540[0];
    v1 = v9;
    do
    {
        v10 = iter[0];
        if (v10 && iter[1] != 1)
        {
            g_1038b1f8(v10);
            v0 = v10;
            sub_1035345e();
            iter[0] = 0;
        }
    } while ((iter += 8, iter < &g_1038e660[0]));
    node = &g_1038e540[0];
    do
    {
        v12 = node[0];
        if (v12 && node[1] == 1)
            v12 = g_1038b1f8(v12);
    } while ((node += 8, node < &g_1038e660[0]));
    return v12;
}
```

## `sub_10358c72` `0x10358c72`

_182 bytes. refs "KERNEL32.DLL", "EncodePointer", "DecodePointer"_

```c
typedef struct struct_1 {
    char padding_0[20];
    unsigned int field_14;
    char padding_18[84];
    unsigned int *field_6c;
    unsigned int field_70;
    char padding_74[84];
    char field_c8;
    char padding_c9[130];
    char field_14b;
    char padding_14c[172];
    unsigned int field_1f8;
    unsigned int field_1fc;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern struct_0 *g_1038b1ec;
extern unsigned int g_1038e748;
extern char g_1038e758;
extern char g_1038eca8;
extern int g_103a1198;

int sub_10358c72(unsigned int a0)
{
    unsigned int v5;  // eax
    struct_1 *idx;  // esi
    unsigned int v7;  // ecx
    unsigned int v8;  // eax
    unsigned int v1;  // [bp+0xfffe8]
    unsigned int v2;  // [bp+0x100000]
    struct_1 *v3;  // [bp+0x10000c]
    unsigned int v4;  // [bp+0x100010]

    sub_1035b0cc(&g_103a1198, 12);
    v5 = g_1038b050("KERNEL32.DLL");
    v1 = v5;
    idx = v3;
    *((char **)&idx->padding_18[0x44]) = &g_1038eca8;
    idx->field_14 = 1;
    if (v5 && sub_10358aa9(v7))
    {
        idx->field_1f8 = g_1038b078(v1, "EncodePointer");
        idx->field_1fc = g_1038b078(v1, "DecodePointer");
    }
    idx->field_70 = 1;
    idx->field_c8 = 67;
    idx->field_14b = 67;
    *((char **)&idx->padding_18[80]) = &g_1038e758;
    g_1038b1ec(&g_1038e758);
    sub_1035a599(12);
    v2 = 0;
    v8 = v4;
    idx->field_6c = v8;
    if (!v8)
        idx->field_6c = g_1038e748;
    sub_10355c95(idx->field_6c);
    v2 = 4294967294;
    sub_10358d28();
    return sub_1035b111();
}
```

## `sub_10358d28` `0x10358d28`

_9 bytes. (leaf/helper — see body)_

```c
void sub_10358d28(void)
{
    sub_1035a4c1(12);
    return;
}
```

## `sub_10358d31` `0x10358d31`

_119 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b07c;
extern struct_0 *g_1038b084;
extern struct_0 *g_1038b0a4;
extern unsigned int g_1038e468;
extern unsigned int g_103a3394;

unsigned int [2] sub_10358d31(void)
{
    unsigned int v3;  // edi
    unsigned int v4;  // esi
    unsigned int v5;  // eax
    unsigned int *v6;  // eax
    unsigned int v7[2];  // esi
    unsigned int v8[2];  // esi
    unsigned int *v9;  // eax
    unsigned int v10;  // ecx
    unsigned int v11;  // eax
    unsigned int v0[2];  // [bp-0x1c]
    unsigned int v1[2];  // [bp-0x18], Other Possible Types: unsigned int

    v5 = g_1038b07c(v3, v4);
    v6 = sub_10358c03();
    v7 = v6(g_1038e468);
    if (v7)
    {
        g_1038b084(v5);
        return v7;
    }
    v8 = sub_103574c2(1, 532);
    if (!v8)
    {
        g_1038b084(v5);
        return v8;
    }
    v1 = g_103a3394;
    v9 = sub_10358b8c();
    if (!v9(g_1038e468, v8))
    {
        v1 = v8;
        sub_1035345e();
        g_1038b084(v5);
        return NULL;
    }
    v1 = 0;
    v0 = v8;
    sub_10358c72(v10);
    v11 = g_1038b0a4();
    v8[1] = 4294967295;
    v8[0] = v11;
    g_1038b084(v5);
    return v8;
}
```

## `sub_10358da8` `0x10358da8`

_24 bytes. (leaf/helper — see body)_

```c
unsigned int [2] sub_10358da8(void)
{
    unsigned int v1[2];  // eax

    v1 = sub_10358d31();
    if (!v1)
        sub_10353c92(16);
    return v1;
}
```

## `sub_10358dc0` `0x10358dc0`

_265 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[36];
    unsigned int field_24;
    char padding_28[4];
    unsigned int field_2c;
    char padding_30[4];
    unsigned int field_34;
    char padding_38[4];
    unsigned int field_3c;
    char padding_40[4];
    unsigned int field_44;
    unsigned int field_48;
    char padding_4c[16];
    unsigned int field_5c;
    char padding_60[8];
    unsigned int field_68;
    struct struct_0 *field_6c;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1f0;
extern unsigned int g_1038e670;
extern char g_1038e748;
extern char g_1038e758;
extern char g_1038eca8;
extern int g_103a11b8;

void sub_10358dc0(void)
{
    struct_1 *idx;  // esi
    unsigned int v6;  // edi
    unsigned int *v7;  // edi
    struct_1 *v0;  // [bp-0x10], Other Possible Types: unsigned int
    unsigned int v1;  // [bp-0xc]
    unsigned int v3;  // [bp+0x100000]
    struct_1 *v4;  // [bp+0x10000c]

    sub_1035b0cc(&g_103a11b8, 8);
    idx = v4;
    if (!idx)
    {
        sub_1035b111();
        return;
    }
    if (idx->field_24)
    {
        v1 = idx->field_24;
        sub_1035345e();
    }
    if (idx->field_2c)
    {
        v1 = idx->field_2c;
        sub_1035345e();
    }
    if (idx->field_34)
    {
        v1 = idx->field_34;
        sub_1035345e();
    }
    if (idx->field_3c)
    {
        v1 = idx->field_3c;
        sub_1035345e();
    }
    if (idx->field_44)
    {
        v1 = idx->field_44;
        sub_1035345e();
    }
    if (idx->field_48)
    {
        v1 = idx->field_48;
        sub_1035345e();
    }
    if (idx->field_5c != &g_1038eca8)
    {
        v1 = idx->field_5c;
        sub_1035345e();
    }
    sub_1035a599(13);
    v3 = 0;
    v6 = idx->field_68;
    if (v6 && !g_1038b1f0(v6) && v6 != &g_1038e758)
    {
        v0 = v6;
        sub_1035345e();
    }
    v3 = 4294967294;
    sub_10358ecc();
    sub_1035a599(12);
    v3 = 1;
    v7 = &idx->field_6c->field_0;
    if (v7)
    {
        sub_10355d1b(v7);
        if (v7 != *((int *)&g_1038e748) && v7 != &g_1038e670 && !*(v7))
            sub_10355b55(v7);
    }
    v3 = 4294967294;
    sub_10358ed8();
    v0 = idx;
    sub_1035345e();
    sub_1035b111();
    return;
}
```

## `sub_10358ec9` `0x10358ec9`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10358ec9(void)
{
    sub_10358ecc();
    return;
}
```

## `sub_10358ecc` `0x10358ecc`

_9 bytes. (leaf/helper — see body)_

```c
void sub_10358ecc(void)
{
    sub_1035a4c1(13);
    return;
}
```

## `sub_10358ed5` `0x10358ed5`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10358ed5(void)
{
    sub_10358ed8();
    return;
}
```

## `sub_10358ed8` `0x10358ed8`

_9 bytes. (leaf/helper — see body)_

```c
void sub_10358ed8(void)
{
    sub_1035a4c1(12);
    return;
}
```

## `sub_10358ee1` `0x10358ee1`

_105 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b234;
extern struct_0 *g_1038b23c;
extern unsigned int g_1038e468;
extern unsigned int g_1038e46c;
extern unsigned int g_103a3394;

unsigned int sub_10358ee1(unsigned int a0)
{
    unsigned int v2;  // edi
    unsigned int v3;  // edi
    unsigned int v4;  // esi
    unsigned int *v5;  // eax
    unsigned int *v6;  // eax
    unsigned int v7;  // eax
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x4]

    if (g_1038e468 != 4294967295)
    {
        v1 = v2;
        v3 = a0;
        if (!v3)
        {
            if (g_1038b234(g_1038e46c, v4))
            {
                v5 = g_1038b234(g_1038e46c, g_1038e468);
                v3 = v5(g_1038e46c, g_1038e468);
            }
        }
        v0 = g_103a3394;
        v6 = sub_10358b8c();
        v6(g_1038e468, 0);
        v0 = v3;
        sub_10358dc0();
    }
    v7 = g_1038e46c;
    if (g_1038e46c != 4294967295)
        v7 = g_1038b23c(g_1038e46c, 0);
    return v7;
}
```

## `sub_10358f4a` `0x10358f4a`

_388 bytes. refs "KERNEL32.DLL", "FlsAlloc", "FlsGetValue"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern struct_0 *g_1038b0a4;
extern unsigned int g_1038b234;
extern struct_0 *g_1038b238;
extern struct_0 *g_1038b23c;
extern unsigned int g_1038b240;
extern unsigned int g_1038e468;
extern unsigned int g_1038e46c;
extern unsigned int g_103a338c;
extern unsigned int g_103a3390;
extern unsigned int g_103a3394;
extern unsigned int g_103a3398;

unsigned int sub_10358f4a(void)
{
    unsigned int v6;  // edi
    unsigned int v7;  // edi
    unsigned int v16;  // ecx
    unsigned int v17;  // eax
    unsigned int v8;  // esi
    unsigned int v9;  // eax
    unsigned int v10;  // 4098
    unsigned int v11;  // eax
    unsigned int v12;  // eax
    unsigned int v13;  // eax
    unsigned int v14[2];  // esi
    unsigned int *v15;  // eax
    unsigned int v0[2];  // [bp-0x48]
    unsigned int v1;  // [bp-0x44]
    unsigned int v2;  // [bp-0x40]
    unsigned int v3;  // [bp-0x3c]
    unsigned int v4;  // [bp-0x38]

    v7 = g_1038b050("KERNEL32.DLL", v6);
    if (!v7)
    {
        sub_10358c35();
        return 0;
    }
    g_103a338c = g_1038b078(v7, "FlsAlloc", v8);
    g_103a3390 = g_1038b078(v7, "FlsGetValue");
    g_103a3394 = g_1038b078(v7, "FlsSetValue");
    v9 = g_1038b078(v7, "FlsFree");
    v10 = g_103a338c;
    g_103a3398 = v9;
    if (!v10 || !g_103a3390 || !g_103a3394 || !g_103a3398)
    {
        g_103a3390 = g_1038b234;
        g_103a338c = sub_10358bfa;
        g_103a3394 = g_1038b23c;
        g_103a3398 = g_1038b240;
    }
    g_1038e46c = g_1038b238();
    if (g_1038e46c == 4294967295 || !g_1038b23c(g_1038e46c, g_103a3390))
        return 0;
    sub_10353f53();
    v4 = g_103a338c;
    v11 = sub_10358b15();
    v3 = g_103a3390;
    g_103a338c = v11;
    v12 = sub_10358b15();
    v2 = g_103a3394;
    g_103a3390 = v12;
    v13 = sub_10358b15();
    v1 = g_103a3398;
    g_103a3394 = v13;
    g_103a3398 = sub_10358b15();
    if (sub_1035a423())
    {
        v3 = g_103a338c;
        g_1038e468 = sub_10358b8c()(sub_10358dc0);
        if (g_1038e468 != 4294967295)
        {
            v14 = sub_103574c2(1, 532);
            if (v14)
            {
                v1 = g_103a3394;
                v15 = sub_10358b8c();
                if (v15(g_1038e468, v14))
                {
                    v1 = 0;
                    v0 = v14;
                    sub_10358c72(v16);
                    v17 = g_1038b0a4();
                    v14[1] = 4294967295;
                    v14[0] = v17;
                    return 1;
                }
            }
        }
    }
    sub_10358c35();
    return 0;
}
```

## `sub_103590ee` `0x103590ee`

_4 bytes. (leaf/helper — see body)_

```c
unsigned int sub_103590ee(void)
{
    return 1;
}
```

## `sub_103590f2` `0x103590f2`

_3 bytes. (leaf/helper — see body)_

```c
void sub_103590f2(void)
{
}
```

## `sub_10359107` `0x10359107`

_19 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[124];
    struct struct_1 *field_7c;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_10359107(void)
{
    struct_0 *v1;  // eax

    v1 = sub_10358da8();
    if (v1->field_7c)
        v1->field_7c();
}
```

## `sub_1035911a` `0x1035911a`

_98 bytes. (leaf/helper — see body)_

```c
extern int g_103a11e0;
extern int g_103a1200;
extern unsigned int g_103a339c;

void sub_1035911a(void)
{
    unsigned int *v3;  // eax
    unsigned int *v4;  // eax
    unsigned int v0;  // [bp-0xc]
    unsigned int v2;  // [bp+0x100000]

    sub_1035b0cc(&g_103a1200, 8);
    v0 = g_103a339c;
    v3 = sub_10358b8c();
    if (v3)
    {
        v2 = 0;
        v3();
        v2 = 4294967294;
    }
    sub_1035b0cc(&g_103a11e0, 8);
    v4 = (sub_10358da8())[15];
    if (!v4)
    {
        sub_1035852d();
        sub_1035b111();
        return;
    }
    v2 = 0;
    v4();
    v2 = 4294967294;
    sub_1035852d();
    sub_1035b111();
    return;
}
```

## `sub_1035913e` `0x1035913e`

_4 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1035913e(void)
{
    return 1;
}
```

## `sub_10359142` `0x10359142`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10359142(void)
{
}
```

## `sub_10359151` `0x10359151`

_17 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103590ce;
extern unsigned int g_103a339c;

int sub_10359151(void)
{
    unsigned int v0;  // [bp-0x4]

    v0 = &g_103590ce;
    g_103a339c = sub_10358b15();
    return g_103a339c;
}
```

## `sub_10359170` `0x10359170`

_76 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[16];
    int field_10;
} struct_0;

void sub_10359170(unsigned int a0, int a1, struct_0 *a2)
{
    int v2;  // ecx
    int v3;  // ebx
    unsigned int v5;  // edi
    unsigned int v6;  // esi
    char v0;  // [bp-0x4]
    char v1;  // [bp+0x0]

    sub_1036055c(a2, &v0, v2, v3, a1 + 12, &v1)(v5, v6);
    if (a2->field_10 == 0x100)
        sub_1036055c(2);
    else
        sub_1036055c(a2->field_10);
    return;
}
```

## `sub_103591bc` `0x103591bc`

_352 bytes. (leaf/helper — see body)_

```c
extern void g_1038f0d0;
extern void g_103a3b80;

unsigned int sub_103591bc(int a0, unsigned int a1, unsigned int a2, void* idx)
{
    unsigned int v6;  // eax
    unsigned int v7;  // ebx
    unsigned int v8;  // eax
    unsigned int v9;  // eax
    unsigned int v10;  // edi
    char *v11;  // eax
    char *v12;  // edi
    int v13;  // edi
    void* v14;  // eax
    unsigned int v15;  // edx
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    int v2;  // [bp-0xc]
    int v3;  // [bp-0x8]
    char v4;  // [bp+0x0]
    int v5;  // [bp+0x8]

    v5 = sub_10360e67(idx, v2, a0, &v4);
    v6 = (int)idx[12];
    if (!((char)v6 & 130))
    {
        *((unsigned int *)sub_103575e0()) = 9;
    }
    else if (((char)v6 & 64))
    {
        *((unsigned int *)sub_103575e0()) = 0x22;
    }
    else
    {
        v1 = v7;
        if (((char)v6 & 1))
        {
            *((unsigned int *)&idx[4]) = 0;
            if (((char)v6 & 16))
            {
                *((int *)idx) = (int)idx[8];
                *((unsigned int *)&idx[12]) = v6 & 4294967294;
                goto LABEL_1035921a;
            }
            else
            {
                *((unsigned int *)&idx[12]) = v6 | 32;
                v8 = 4294967295;
            }
        }
        else
        {
LABEL_1035921a:
            v9 = (int)idx[12] & 4294967279 | 2;
            *((unsigned int *)&idx[12]) = v9;
            *((unsigned int *)&idx[4]) = 0;
            v3 = 0;
            if (!((unsigned short)v9 & 268) && (idx != sub_1035cc7b() + 32 && idx != sub_1035cc7b() + 64 || !sub_10360e09(v5)))
                sub_10360dc5(idx);
            v0 = v10;
            if (((short)idx[12] & 264))
            {
                v11 = (int)idx[8];
                v12 = *((int *)idx);
                *((char **)idx) = v11 + 1;
                v13 = v12 - v11;
                *((unsigned int *)&idx[4]) = (int)idx[24] - 1;
                if (v13 > 0)
                {
                    v3 = sub_10360ce9(v5, v11, v13);
                    v3 = v3;
                }
                else
                {
                    if (v5 != 4294967295 && v5 != -2)
                        v14 = (v5 & 31) * 56 + *((int *)&(&g_103a3b80)[4 * (v5 >> 5)]);
                    else
                        v14 = &g_1038f0d0;
                    if (((char)v14[4] & 32) && (sub_1036060a(v5, 0, 0, 2) & v15) == 4294967295)
                        goto LABEL_10359306;
                }
                *((char *)(int)idx[8]) = a2;
            }
            else
            {
                v13 = 1;
                v3 = sub_10360ce9(v5, &/* unsupported instruction */, 1);
                v3 = v3;
            }
            if (v3 != v13)
            {
LABEL_10359306:
                *((unsigned int *)&idx[12]) = (int)idx[12] | 32;
                v8 = 4294967295;
            }
            else
            {
                v8 = a2 & 0xff;
            }
        }
        return v8;
    }
    *((unsigned int *)&idx[12]) = (int)idx[12] | 32;
    return 4294967295;
}
```

## `sub_1035931c` `0x1035931c`

_51 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_1 *field_0;
    int field_4;
    unsigned int field_8;
    char field_c;
} struct_0;

typedef struct struct_1 {
    char field_0;
} struct_1;

int sub_1035931c(void)
{
    struct_0 *idx;  // ecx
    int v2;  // 4096
    char v3;  // al
    unsigned int v4;  // eax
    unsigned int v5;  // edx
    unsigned int *v6;  // esi
    unsigned int *v7;  // esi

    if (!(idx->field_c & 64) || idx->field_8)
    {
        v2 = idx->field_4;
        idx->field_4 = idx->field_4 - 1;
        if (v2 - 1 >= 0)
        {
            idx->field_0->field_0 = v3;
            idx->field_0 = idx->field_0 + 1;
            v4 = v3;
        }
        else
        {
            v4 = sub_103591bc(idx, v5, v3, idx);
        }
        if (v4 == 4294967295)
        {
            *(v6) = 4294967295;
            return;
        }
    }
    *(v7) = *(v7) + 1;
    return;
}
```

## `sub_1035934f` `0x1035934f`

_36 bytes. (leaf/helper — see body)_

```c
int sub_1035934f(void)
{
    unsigned int *v2;  // eax
    int i;  // [bp+0x8]

    while (i > 0)
    {
        i -= 1;
        sub_1035931c();
        if (*(v2) == 4294967295)
            return;
    }
    return;
}
```

## `sub_10359373` `0x10359373`

_490 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
    char padding_10[20];
    char field_24;
} struct_1;

typedef struct struct_2 {
    char padding_0[112];
    unsigned int field_70;
} struct_2;

extern unsigned int g_10359ce7[4];
extern unsigned int g_1038e180;
extern struct_1 g_1038f0d0;
extern char g_10395100;
extern char g_10395120;
extern struct_1 g_103a3b80;

int sub_10359373(struct_0 *a0, char *a1, unsigned int *a2, unsigned int a3)
{
    unsigned int v26;  // ebx
    char *v27;  // ebx
    char v36;  // 4107
    int v37;  // ecx
    unsigned int v28;  // esi
    unsigned int v29;  // edi
    int v30;  // eax
    unsigned int v31;  // eax
    struct_1 *v32;  // eax
    int v33;  // eax
    unsigned int v34;  // eax
    struct_1 *v35;  // eax
    unsigned int v0;  // [bp-0x29c]
    unsigned int v1;  // [bp-0x298]
    unsigned int v2;  // [bp-0x294]
    unsigned int v3;  // [bp-0x290]
    unsigned int v4;  // [bp-0x28c]
    unsigned int v5;  // [bp-0x288]
    unsigned int v6;  // [bp-0x284]
    unsigned int v7;  // [bp-0x280]
    struct_0 v8;  // [bp-0x260]
    struct_2 *idx;  // [bp-0x258]
    char v10;  // [bp-0x254]
    unsigned int v11;  // [bp-0x250]
    unsigned int v12;  // [bp-0x24c]
    unsigned int v13;  // [bp-0x248]
    char *v14;  // [bp-0x244]
    unsigned int v15;  // [bp-0x240]
    unsigned int v16;  // [bp-0x23c]
    unsigned int v17;  // [bp-0x238]
    int v18;  // [bp-0x230]
    unsigned int v19;  // [bp-0x228]
    unsigned int v20;  // [bp-0x224]
    unsigned int v21;  // [bp-0x21c]
    char v22;  // [bp-0x215]
    unsigned int v23;  // [bp-0x214]
    char v24;  // [bp-0x1fc]
    unsigned int v25;  // [bp-0x8]

    v25 = g_1038e180 ^ &v24;
    v7 = v26;
    v27 = a1;
    v6 = v28;
    v5 = v29;
    v19 = a3;
    v13 = 0;
    v23 = 0;
    v16 = 0;
    v21 = 0;
    v17 = 0;
    v12 = 0;
    v15 = 0;
    sub_103536a7(&v8, a2);
    if (!a0)
    {
LABEL_103593d3:
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        *((unsigned int *)sub_103575e0()) = 22;
        v0 = 0;
        sub_103535f2();
        if (v10)
            idx->field_70 = idx->field_70 & 4294967293;
    }
    else if (!(a0->field_c & 64))
    {
        if (sub_10360e67(a0) != 4294967295 && sub_10360e67(a0) != 4294967294)
        {
            v30 = sub_10360e67(a0);
            v31 = sub_10360e67(a0);
            v32 = (v31 & 31) * 56 + (&g_103a3b80.field_0)[v30 >> 5];
        }
        else
        {
            v32 = &g_1038f0d0.field_0;
        }
        if (!(v32->field_24 & 127))
        {
            if (sub_10360e67(a0) != 4294967295 && sub_10360e67(a0) != 4294967294)
            {
                v33 = sub_10360e67(a0);
                v34 = sub_10360e67(a0);
                v35 = (v34 & 31) * 56 + (&g_103a3b80.field_0)[v33 >> 5];
            }
            else
            {
                v35 = &g_1038f0d0.field_0;
            }
            if (!(v35->field_24 & 128))
                goto LABEL_103594b1;
            goto LABEL_103593d3;
        }
    }
    else
    {
LABEL_103594b1:
        if (!v27)
            goto LABEL_103593d3;
        v36 = *(v27);
        v37 = 0;
        v18 = 0;
        v20 = 0;
        v11 = 0;
        v22 = v36;
        if (v36)
        {
            while (true)
            {
                v14 = v27 + 1;
                if (v18 < NULL)
                    break;
                v4 = 7;
                v37 = (&g_10395120)[8 * (v36 - 32 <= 88 ? *(&(&g_10395100)[v36]) & 15 : 0) + v37] >> 4;
                if (v37 <= 7)
                    goto g_10359ce7[v37];
                v27 = v14;
                v36 = *(v27);
                v22 = v36;
                if (!v36)
                    break;
            }
        }
        if (v10)
            idx->field_70 = idx->field_70 & 4294967293;
    }
    return sub_10351225();
}
```

## `sub_1035951c` `0x1035951c`

_27 bytes. (leaf/helper — see body)_

```c
void sub_1035951c(void)
{
    unsigned int v8;  // esi
    unsigned int v1;  // [bp+0xfff8c]
    unsigned int v2;  // [bp+0xfffb4]
    unsigned int v3;  // [bp+0xfffc0]
    unsigned int v4;  // [bp+0xfffc4]
    unsigned int v5;  // [bp+0xfffc8]
    unsigned int v6;  // [bp+0xfffe4]
    unsigned int v7;  // [bp+0xfffec]

    v6 = 4294967295;
    v1 = v8;
    v2 = v8;
    v4 = v8;
    v5 = v8;
    v7 = v8;
    v3 = v8;
}
```

## `sub_10359537` `0x10359537`

_79 bytes. (leaf/helper — see body)_

```c
int sub_10359537(unsigned int a0, char a1)
{
    unsigned int v2;  // eax
    unsigned int v3;  // eax
    unsigned int v4;  // eax
    unsigned int v5;  // eax
    unsigned int v1;  // [bp+0xfffec]

    v2 = a1;
    v3 = v2 - 32;
    if (v2 == 32)
        v1 |= 2;
    v4 = v3 - 3;
    if (v3 == 3)
    {
        v1 |= 128;
    }
    else if (v4 != 8)
    {
        v5 = v4 - 9;
        if (v5 == 1)
            v1 |= 4;
        if (v5 != 4)
            goto LABEL_0x10359c8f;
        v1 |= 8;
    }
    else
    {
        v1 |= 1;
    }
}
```

## `sub_10359586` `0x10359586`

_58 bytes. (leaf/helper — see body)_

```c
int sub_10359586(unsigned int a0, char a1)
{
    int *v4;  // edi
    int *v5;  // edi
    int v6;  // edi
    int v7;  // esi
    unsigned int v1;  // [bp+0xfffc4], Other Possible Types: int
    int *v2;  // [bp+0xfffd8]
    unsigned int v3;  // [bp+0xfffec]

    if (a1 != 42)
        v1 = v1 * 10 + a1 - 48;
    v5 = v4 + 1;
    v2 = v5;
    v6 = v5[1];
    v1 = v6;
    if (v6 >= v7)
        goto LABEL_0x10359c8f;
    v3 |= 4;
    v1 = -(v1);
}
```

## `sub_103595c0` `0x103595c0`

_8 bytes. (leaf/helper — see body)_

```c
void sub_103595c0(void)
{
    unsigned int v2;  // esi
    unsigned int v1;  // [bp+0xfffe4]

    v1 = v2;
}
```

## `sub_103595c8` `0x103595c8`

_55 bytes. (leaf/helper — see body)_

```c
int sub_103595c8(unsigned int a0, char a1)
{
    int *v3;  // edi
    int *v4;  // edi
    int v5;  // edi
    int v6;  // esi
    int *v1;  // [bp+0xfffd8]
    int v2;  // [bp+0xfffe4], Other Possible Types: unsigned int

    if (a1 != 42)
        v2 = v2 * 10 + a1 - 48;
    v4 = v3 + 1;
    v1 = v4;
    v5 = v4[1];
    v2 = v5;
    if (v5 >= v6)
        goto LABEL_0x10359c8f;
    v2 = 4294967295;
}
```

## `sub_103595ff` `0x103595ff`

_271 bytes. (leaf/helper — see body)_

```c
int sub_103595ff(unsigned int a0, char a1)
{
    char *v10;  // ebx
    char v11[2];  // ebx
    char v12;  // al
    unsigned int v13;  // esi
    char v14;  // 4102
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]
    unsigned int v4;  // [bp-0x4]
    unsigned int v6;  // [bp+0xfff90]
    char *v7;  // [bp+0xfffbc], Other Possible Types: char [2]
    unsigned int v8;  // [bp+0xfffc0]
    unsigned int v9;  // [bp+0xfffec]

    if (a1 == 73)
    {
        v12 = v11[0];
        if (v11[0] == 54 && v11[1] == 52)
        {
            v9 |= 0x8000;
            *(&v7) = v11 + 1;
        }
        if (v12 == 0x33 && v11[1] == 50)
        {
            v9 &= 4294934527;
            *(&v7) = v11 + 1;
        }
        if (v12 == 100)
            goto LABEL_0x10359c8f;
        if (v12 == 105)
            goto LABEL_0x10359c8f;
        if (v12 == 111)
            goto LABEL_0x10359c8f;
        if (v12 == 117)
            goto LABEL_0x10359c8f;
        if (v12 == 120)
            goto LABEL_0x10359c8f;
        if (v12 == 88)
            goto LABEL_0x10359c8f;
        v6 = v13;
        v8 = v13;
        if (sub_1035de48(73, /* unsupported instruction */ - 100))
        {
            sub_1035931c();
            v14 = v11[0];
            *(&v7) = &v11[1];
            if (!v14)
            {
                *((unsigned int *)sub_103575e0()) = 22;
                v4 = 0;
                v3 = 0;
                v2 = 0;
                v1 = 0;
                v0 = 0;
            }
        }
        sub_1035931c();
    }
    else if (a1 == 104)
    {
        v9 |= 32;
    }
    else if (a1 != 108)
    {
        if (a1 != 0x77)
            goto LABEL_0x10359c8f;
        v9 |= 0x800;
    }
    else if (*(v10) == 108)
    {
        v9 |= 0x1000;
        v7 = v10 + 1;
    }
    else
    {
        v9 |= 16;
    }
}
```

## `sub_103596f7` `0x103596f7`

_1432 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned short field_0;
} struct_0;

typedef struct struct_3 {
    char padding_0[4];
    unsigned short field_4;
} struct_3;

typedef struct struct_1 {
    char field_0;
} struct_1;

extern struct_1 *g_1038e470;
extern struct_1 *g_1038e474;
extern unsigned int g_1038ec98;
extern unsigned int g_1038eca0;
extern unsigned int g_1038eca4;

int sub_103596f7(unsigned int a0, char a1)
{
    unsigned int v26;  // eax
    unsigned int v27;  // eax
    struct_0 **v34;  // edi, Other Possible Types: unsigned int [2], void*, void* *, struct_3 *, unsigned int
    unsigned short *v35;  // eax
    unsigned short *v36;  // esi, Other Possible Types: int
    unsigned int v37;  // 4117
    char *v38;  // eax
    int v39;  // 4102
    int v40;  // cc_dep1
    char *v41;  // ebx
    unsigned int v42;  // esi
    unsigned int v28;  // eax
    char *v43;  // eax
    char v44;  // dl
    unsigned int v45;  // esi
    unsigned int v46[2];  // edi
    unsigned int *v47;  // eax
    unsigned int v50;  // 4113
    void* v51;  // esi
    unsigned int iter;  // ecx
    unsigned int v53;  // edi
    unsigned int v54;  // 4125
    unsigned int v55;  // edi
    char *iter1;  // eax
    char *iter2;  // eax
    unsigned int v58;  // eax
    unsigned int v59;  // 4113
    char v60;  // 4105
    unsigned short v61;  // cx
    unsigned int v62;  // eax
    unsigned int v63;  // edx
    struct_3 *v64;  // edi
    unsigned int v30;  // eax
    unsigned int v65;  // eax
    unsigned int v67;  // edi
    unsigned int v68;  // eax
    void* node;  // esi
    unsigned int v70;  // eax
    unsigned int v71;  // eax
    int v72;  // ecx
    unsigned int v31;  // eax
    int v73;  // ecx
    unsigned int v74;  // edx
    char *v75;  // eax
    void* v76;  // esi
    unsigned int v77;  // 4132
    unsigned short v78;  // ax
    int v79;  // ebx
    int v80;  // edi
    char *v81;  // eax
    void* v82;  // esi
    unsigned int v83;  // eax
    void* v32;  // edi
    unsigned int v33;  // 4117
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0xc]
    unsigned int v3;  // [bp+0xfff84]
    unsigned int v4;  // [bp+0xfff88]
    unsigned int v5;  // [bp+0xfff8c]
    int v6;  // [bp+0xfff94]
    char *v7;  // [bp+0xfff9c], Other Possible Types: unsigned int
    char *v8;  // [bp+0xfffb0], Other Possible Types: unsigned int
    unsigned int v9;  // [bp+0xfffb4]
    unsigned int v10;  // [bp+0xfffb8]
    unsigned short *v11;  // [bp+0xfffc0]
    unsigned int v12;  // [bp+0xfffc4]
    int v13;  // [bp+0xfffc8], Other Possible Types: unsigned int
    char v14;  // [bp+0xfffcc]
    char v15;  // [bp+0xfffcd]
    int v16;  // [bp+0xfffd0], Other Possible Types: unsigned short
    int v17;  // [bp+0xfffd4]
    struct_0 **v18;  // [bp+0xfffd8], Other Possible Types: unsigned int [2], void*, void* *, struct_3 *, unsigned int
    char *v19;  // [bp+0xfffdc], Other Possible Types: int
    unsigned short *v20;  // [bp+0xfffe0], Other Possible Types: void*, char *
    int v21;  // [bp+0xfffe4], Other Possible Types: unsigned int
    char v22;  // [bp+0xfffeb]
    unsigned short v23;  // [bp+0xfffec], Other Possible Types: unsigned int
    char v24;  // [bp+0xffff0]

    v26 = a1;
    if (v26 <= 100)
    {
        if (v26 == 100)
            goto LABEL_103598f4;
        if (v26 <= 83)
        {
            if (v26 == 83 && !((short)v23 & 2096))
            {
                v23 |= 0x800;
                goto LABEL_1035977d;
            }
            if (v26 != 65)
            {
                v27 = v26 - 66;
                if (v27 == 1 && !(v23 & 2096))
                {
                    v23 = *((int *)&v23) | 0x800;
                    goto LABEL_103597da;
                }
                v28 = v27 - 2;
                if (v28 == 1 || v28 == 3)
                    goto LABEL_10359729;
            }
            else
            {
LABEL_10359729:
                v5 = 1;
                v22 = a1 + 32;
                v44 = a1 + 32;
LABEL_10359736:
                v23 |= 64;
                v39 = v21;
                v40 = v21;
                v41 = /* unsupported instruction */ - 20;
                v20 = v41;
                v7 = 0x200;
                if (v39 < v36)
                {
                    v21 = 6;
                }
                else
                {
                    if (v40 == v36)
                    {
                        if (v44 == 103)
                            v21 = 1;
                    }
                    else
                    {
                        if (v21 > 0x200)
                            v21 = 0x200;
                        if (v21 > 163)
                        {
                            v42 = v21 + 349;
                            v43 = sub_10357482(v42);
                            v44 = v22;
                            v8 = v43;
                            if (v43)
                            {
                                v20 = v43;
                                v7 = v42;
                                v41 = v43;
                            }
                            else
                            {
                                v21 = 163;
                            }
                            v45 = 0;
                        }
                    }
                }
                v46 = v34 + 1;
                v3 = v34[0];
                v4 = v46[1];
                v18[0] = v46;
                v0 = g_1038ec98;
                v47 = sub_10358b8c();
                v47(/* unsupported instruction */ - 128, v41, v7, v44, v21, v5, /* unsupported instruction */ - 100);
                if (((char)v23 & 128) && v21 == v45)
                {
                    v1 = g_1038eca4;
                    sub_10358b8c()(v41, /* unsupported instruction */ - 100);
                }
                if (v22 == 103 && (v23 & 128) == v45)
                {
                    v1 = g_1038eca0;
                    sub_10358b8c()(v41, /* unsupported instruction */ - 100);
                }
                if (*(v41) == 45)
                {
                    v23 |= 0x100;
                    v41 += 1;
                    v20 = v41;
                }
                goto LABEL_1035986a;
            }
        }
        else
        {
            if (v26 == 88)
                goto LABEL_103599ff;
            v30 = v26 - 89;
            v31 = v30 - 1;
            if (v30 == 1)
            {
                v35 = &*(v34)->field_0;
                v18 = v34 + 1;
                if (v35 != v36 && *((int *)&v35[2]) != v36)
                {
                    v37 = (short)v23 & 0x800;
                    v38 = *(v35);
                    v20 = *((int *)&v35[2]);
                    if ((unsigned short)v37)
                    {
                        v38 = &v38;
                        v11 = 0x1;
                        goto LABEL_10359b74;
                    }
                    else
                    {
                        v11 = v36;
                        goto LABEL_10359b74;
                    }
                }
                else
                {
                    v20 = &g_1038e470->field_0;
                    v41 = &g_1038e470->field_0;
LABEL_1035986a:
                    v38 = sub_10352f20(v41);
                    goto LABEL_10359b74;
                }
            }
            v44 = a1;
            if (v31 == a0)
                goto LABEL_10359736;
            if (v31 - a0 == 2)
            {
LABEL_103597da:
                v32 = v34 + 4;
                v33 = (short)v23 & 2064;
                v18 = v32;
                if ((unsigned short)v33)
                {
                    if (sub_10361009(/* unsupported instruction */ - 40, /* unsupported instruction */ - 20, 0x200, (short)v32[4]))
                        v9 = 1;
                }
                else
                {
                    v24 = (char)v32[4];
                    v19 = 0x1;
                }
                v20 = /* unsupported instruction */ - 20;
            }
        }
    }
    else if (v26 <= 112)
    {
        if (v26 == 112)
        {
            v21 = 8;
LABEL_103599ff:
            v10 = a0;
            goto LABEL_10359a25;
        }
        if (v26 >= 101)
        {
            v44 = a1;
            if (v26 <= 103)
                goto LABEL_10359736;
            if (v26 == 105)
            {
LABEL_103598f4:
                v23 |= 64;
                goto LABEL_103598f8;
            }
            if (v26 == 110)
            {
                v51 = *(v34);
                v18 = v34 + 1;
                if (!sub_10360e94())
                    goto LABEL_0x10359ca8;
                if (((char)v23 & 32))
                    *((unsigned short *)v51) = v16;
                else
                    *((int *)v51) = *((int *)&v16);
                v9 = 1;
                if (!v8)
                    goto LABEL_0x10359c8f;
                v41 = v8;
                sub_1035345e();
                v8 = 0;
            }
            if (v26 == 111)
            {
                v50 = (char)v23 & 128;
                v19 = 8;
                if ((char)v50)
                {
                    v23 |= 0x200;
                    goto LABEL_103598ff;
                }
            }
        }
    }
    else
    {
        if (v26 == 115)
        {
LABEL_1035977d:
            iter = v21;
            if (v21 == 4294967295)
                iter = 2147483647;
            v53 = v34 + 4;
            v54 = (short)v23 & 2064;
            v18 = v53;
            v55 = *((int *)(v53 - 4));
            v20 = v55;
            if ((unsigned short)v54)
            {
                if (v55 == v45)
                    v20 = &g_1038e474->field_0;
                iter1 = v20;
                for (v11 = 0x1; iter != v45 && (iter -= 1, *((short *)&iter1) != (unsigned short)v45); iter1 += 2);
                v38 = iter1 - v20 >> 1;
                goto LABEL_10359b74;
            }
            else
            {
                if (v55 == v45)
                    v20 = &g_1038e470->field_0;
                for (iter2 = v20; iter != v45 && (iter -= 1, *(iter2)); iter2 += 1);
                v38 = iter2 - v20;
                goto LABEL_10359b74;
            }
        }
        v58 = v26 - 116;
        if (v58 == 1)
        {
LABEL_103598f8:
            v19 = 10;
            goto LABEL_103598ff;
        }
        else if (v58 == 4)
        {
            v10 = 39;
LABEL_10359a25:
            v59 = (char)v23 & 128;
            v19 = 16;
            if ((char)v59)
            {
                v60 = v10;
                v14 = 48;
                v15 = v60 + 81;
                v13 = 2;
            }
LABEL_103598ff:
            v61 = v23;
            if (v61 < 0 || (v61 & 0x1000))
            {
                v62 = (unsigned int)v34->padding_0;
                v63 = *((int *)&v34->field_4);
                v64 = &v34[1].padding_0[2];
                goto LABEL_10359a83;
            }
            else
            {
                v64 = &v34->field_4;
                if (((char)v61 & 32))
                {
                    v18 = v64;
                    v62 = (!((char)v61 & 64) ? v64->field_4 : v64->field_4);
                    v63 = v62 >> 31;
                }
                else
                {
                    v62 = *((int *)&v64->field_4);
                    v63 = (!((char)v61 & 64) ? 0 : v62 >> 31);
LABEL_10359a83:
                    v18 = v64;
                }
            }
            v65 = v62;
            if (((char)v61 & 64))
            {
                v65 = v62;
                if (v63 <= v45 && (v63 < v45 || (v65 = v62, v65 < v45)))
                {
                    v63 = -(v63 + (0 < v62));
                    v23 |= 0x100;
                    v65 = -(v62);
                }
            }
            v67 = v65;
            if (!((short)v23 & 0x9000))
                v63 = 0;
            if (v21 < NULL)
            {
                v21 = 1;
            }
            else
            {
                v23 &= 4294967287;
                if (v21 > 0x200)
                    v21 = 0x200;
            }
            v68 = v67;
            if (!v68 && !v63)
                v13 &= v68 | v63;
            node = /* unsupported instruction */ + 491;
            while (true)
            {
                v70 = v21;
                v21 -= 1;
                if (v70 <= NULL && !v67 && !v63)
                    break;
                v71 = sub_1035b8a0(v67, v63, v19, v19 >> 31);
                v73 = v72 + 48;
                v7 = v63;
                v67 = v71;
                v63 = v74;
                if (v73 > 57)
                    v73 += v10;
                *((char *)node) = v73;
                node -= 1;
            }
            v75 = /* unsupported instruction */ + 491 - node;
            v76 = node + 1;
            v77 = (short)v23 & 0x200;
            v19 = v75;
            v20 = v76;
            if ((unsigned short)v77 && (!v75 || *((char *)v76) != 48))
            {
                v20 -= 1;
                *((char *)v20) = 48;
                v38 = v75 + 1;
LABEL_10359b74:
                v19 = v38;
            }
        }
    }
    if (!v9)
    {
        v78 = v23;
        if (((char)v78 & 64))
        {
            if ((v78 & 0x100))
            {
                v14 = 45;
            }
            else if (((char)v78 & 1))
            {
                v14 = 43;
            }
            else
            {
                if (!((char)v78 & 2))
                    goto LABEL_10359bad;
                v14 = 32;
            }
            v13 = 1;
        }
LABEL_10359bad:
        v79 = v12 - v19 - v13;
        if (!((char)v23 & 12))
            sub_1035934f(32, v79, v17);
        v80 = v17;
        sub_10361024(v13);
        if (((char)v23 & 8) && !((char)v23 & 4))
            sub_1035934f(48, v79, v80);
        v81 = v19;
        if (v11 && v81 > NULL)
        {
            v82 = v20;
            v7 = v81;
            do
            {
                v83 = *((short *)v82);
                v7 += 1;
                v82 += 2;
                if (sub_10361009(/* unsupported instruction */ - 112, /* unsupported instruction */ + 492, 6, v83) || !v6)
                {
                    v16 = -1;
                    break;
                }
            } while ((sub_10361024(v6), v7));
        }
        else
        {
            sub_10361024(v81);
        }
        if (v16 >= NULL && ((char)v23 & 4))
            sub_1035934f(32, v79, v80);
    }
    if (!v8)
        goto LABEL_0x10359c8f;
    v41 = v8;
    sub_1035345e();
    v8 = 0;
}
```

## `sub_10359d07` `0x10359d07`

_202 bytes. (leaf/helper — see body)_

```c
int sub_10359d07(unsigned int a0, unsigned int a1, unsigned int *a2, char *a3, int a4, unsigned int a5, unsigned int a6, unsigned int a7)
{
    unsigned int v11;  // esi
    unsigned int v12;  // edi
    int v13;  // eax
    int v14;  // ecx
    unsigned int v15;  // edx
    unsigned int v0;  // [bp-0x44]
    unsigned int v1;  // [bp-0x40]
    unsigned int v2;  // [bp-0x3c]
    unsigned int v3;  // [bp-0x38]
    unsigned int v4;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    char *v7;  // [bp-0x24]
    int v8;  // [bp-0x20]
    char *v9;  // [bp-0x1c]
    unsigned int v10;  // [bp-0x18]

    if (!a5)
    {
        v6 = 0;
        v5 = 0;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        *((unsigned int *)sub_103575e0()) = 22;
        sub_103535f2();
        return -1;
    }
    v6 = v11;
    v5 = v12;
    if (a4 && !a3)
    {
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        *((unsigned int *)sub_103575e0()) = 22;
        sub_103535f2();
        v13 = -1;
    }
    else
    {
        v8 = 2147483647;
        if (a4 <= 2147483647)
            v8 = a4;
        v10 = 66;
        v9 = a3;
        v7 = a3;
        v13 = a2(&v7, a5, a6, a7);
        a5 = v13;
        if (a3)
        {
            v8 = v8;
            if (v13 >= 0)
            {
                v8 -= 1;
                if (v8 - 1 >= 0)
                {
                    *(v7) = 0;
                }
                else
                {
                    v8 = v8;
                    if (sub_103591bc(v14, v15, 0, &v7) == 4294967295)
                        goto LABEL_10359dbe;
                }
                v13 = a5;
            }
            else
            {
LABEL_10359dbe:
                a3[1 + a4] = 0;
                v13 = (unsigned int)((v8 >= 0) - 2);
            }
        }
    }
    return v13;
}
```

## `sub_10359dd1` `0x10359dd1`

_134 bytes. (leaf/helper — see body)_

```c
int sub_10359dd1(unsigned int a0, unsigned int a1, char *a2, int a3, unsigned int a4, unsigned int a5, unsigned int a6)
{
    unsigned int v6;  // esi
    int v7;  // eax
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]

    if (!a4)
    {
        v5 = 0;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        *((unsigned int *)sub_103575e0()) = 22;
        sub_103535f2();
        return -1;
    }
    v5 = v6;
    if (!a2 || a3 <= 0)
    {
        *((unsigned int *)sub_103575e0()) = 22;
    }
    else
    {
        v7 = sub_10359d07(a0, a1, sub_1036106e, a2, a3, a4, a5, a6);
        if (v7 < 0)
            *(a2) = 0;
        if (v7 != -2)
            return v7;
        *((unsigned int *)sub_103575e0()) = 0x22;
    }
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    sub_103535f2();
    return -1;
}
```

## `sub_10359e57` `0x10359e57`

_103 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern int g_103a1220;
extern struct_0 g_103a33a0;
extern struct_0 *g_103a33a4;

void sub_10359e57(void)
{
    struct_0 *idx;  // esi
    unsigned int v6;  // ecx
    struct_0 *v7;  // edx
    struct_0 *v0;  // [bp-0xc], Other Possible Types: unsigned int
    struct_0 *v2;  // [bp+0xfffe8]
    unsigned int v3;  // [bp+0x100000]
    struct_0 *v4;  // [bp+0x10000c]

    sub_1035b0cc(&g_103a1220, 12);
    sub_1035a599(14);
    v3 = 0;
    idx = v4;
    v6 = idx->field_4;
    if (v6)
    {
        v7 = &g_103a33a0.padding_0[0];
        while (true)
        {
            v2 = g_103a33a4;
            if (!g_103a33a4)
                break;
            if (g_103a33a4->padding_0 == v6)
            {
                v7->field_4 = g_103a33a4->field_4;
                v0 = g_103a33a4;
                sub_1035345e();
                break;
            }
            else
            {
                v7 = g_103a33a4;
            }
        }
        v0 = idx->field_4;
        sub_1035345e();
        idx->field_4 = 0;
    }
    v3 = 4294967294;
    sub_10359ebe();
    sub_1035b111();
    return;
}
```

## `sub_10359ebe` `0x10359ebe`

_9 bytes. (leaf/helper — see body)_

```c
void sub_10359ebe(void)
{
    sub_1035a4c1(14);
    return;
}
```

## `sub_10359ed0` `0x10359ed0`

_135 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10359ed0(void* a0, char *a1)
{
    void* node;  // edx
    char iter[4];  // ecx
    unsigned int v9;  // eax
    char v10;  // al
    char v11;  // al
    unsigned int v12;  // 4118
    char v2;  // 4104
    unsigned int v3;  // cc_dep1
    unsigned int v4;  // cc_dep2
    char v5;  // al
    char v6;  // al
    char v7;  // al
    char v8;  // al

    node = a0;
    iter = a1;
    if (!((char)node & 3))
    {
        while (true)
        {
LABEL_10359ee0:
            v7 = *((int *)node);
            v3 = v7;
            v4 = iter[0];
            if (v7 != iter[0])
                break;
            v8 = v7;
            if (!v8)
                return 0;
            v3 = v8;
            v4 = iter[1];
            if (v8 != iter[1])
                break;
            v9 = _INSERT(v8, 1, v8);
            if (!v8)
                return 0;
            v10 = v9 >> 16;
            v3 = v10;
            v4 = iter[2];
            if (v10 != iter[2])
                break;
            v11 = v10;
            if (!v11)
                return 0;
            v3 = v11;
            v4 = iter[3];
            if (v11 != iter[3])
                break;
            iter += 1;
            node += 4;
            if (!v11)
                return 0;
        }
    }
    else if (((char)node & 1))
    {
        v2 = *((char *)node);
        node += 1;
        v3 = v2;
        v4 = iter[0];
        if (v2 == iter[0])
        {
            iter = &iter[1];
            if (!v2)
                return 0;
            if ((node & 2))
                goto LABEL_10359f3c;
            goto LABEL_10359ee0;
        }
    }
    else
    {
LABEL_10359f3c:
        v5 = *((short *)node);
        node += 2;
        v3 = v5;
        v4 = iter[0];
        if (v5 == iter[0])
        {
            v6 = v5;
            if (!v6)
                return 0;
            v3 = v6;
            v4 = iter[1];
            if (v6 == iter[1])
            {
                if (!v6)
                    return 0;
                iter = &iter[2];
                goto LABEL_10359ee0;
                goto LABEL_10359ee0;
            }
        }
    }
    v12 = _ccall(4, v3, v4, 0);
    return -(v12 & 1) * 2 + 1;
}
```

## `sub_10359f13` `0x10359f13`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10359f13(void)
{
}
```

## `sub_10359f58` `0x10359f58`

_101 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10359f58(char *a0, unsigned int a1, char *iter)
{
    char *v5;  // ecx
    unsigned int v6;  // edi
    char *v7;  // edx
    char v8;  // 4103
    unsigned int v12;  // esi
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]

    v5 = a0;
    if (v5)
    {
        v6 = a1;
        if (v6 > NULL)
        {
            if (!iter)
            {
                *(v5) = 0;
            }
            else
            {
                v7 = v5;
                do
                {
                    v8 = *(iter);
                    *(v7) = *(iter);
                    iter += 1;
                } while (v8 && (v6 -= 1, v7 += 1, v6 != 1));
                if (v6)
                    return 0;
                *(v5) = 0;
                v4 = 0x22;
                *((unsigned int *)sub_103575e0()) = v4;
                v4 = 0;
                v3 = 0;
                v2 = 0;
                v1 = 0;
                v0 = 0;
                sub_103535f2();
                return v12;
            }
        }
    }
    v4 = 22;
    *((unsigned int *)sub_103575e0()) = v4;
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    sub_103535f2();
    return v4;
}
```

## `sub_10359fbd` `0x10359fbd`

_416 bytes. refs "Runtime Error!\n\nProgram: ", "<program name unknown>", "..."_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1d4;
extern struct_0 *g_1038b244;
extern struct_0 *g_1038b248;
extern unsigned int g_1038e480[4];
extern unsigned int g_1038e484[4];
extern unsigned int g_103a3054;
extern char g_103a3386;
extern char g_103a33a8;
extern void g_103a33c1;
extern char g_103a34c5;
extern char g_103a36bc;

unsigned int sub_10359fbd(unsigned int a0, unsigned int a1, unsigned int *a2)
{
    unsigned int v11;  // esi
    unsigned int v12;  // edi
    unsigned int v13;  // edi
    unsigned int v14;  // eax
    int v15;  // eax
    unsigned int v16;  // ebp
    void* *v17;  // esi
    int v18;  // eax
    unsigned int v19;  // eax
    unsigned int v0;  // [bp-0x34]
    unsigned int v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x28]
    unsigned int v4;  // [bp-0x24]
    unsigned int v5;  // [bp-0x20]
    unsigned int v6;  // [bp-0x1c]
    unsigned int v7;  // [bp-0x18]
    unsigned int v8;  // [bp-0x10]
    unsigned int v9;  // [bp-0xc]
    unsigned int v10;  // [bp-0x4]

    v10 = a0;
    v9 = v11;
    v8 = v12;
    v13 = 0;
    do
    {
    } while (a2 != g_1038e480[2 * v13] && (v13 += 1, v13 < 23));
    if (v13 >= 23)
        return v19;
    if (!(sub_10361bdb(3, /* unsupported instruction */) != 1 && !((v14 = sub_10361bdb(3), !v14 && g_103a3054 == 1))))
    {
        v14 = g_1038b248(4294967284);
        v16 = v14;
        if (v16 && v16 != 4294967295)
        {
            v6 = 0;
            v5 = &/* unsupported instruction */;
            v17 = &g_1038e484[2 * v13];
            v18 = sub_10352f20(*(v17));
            v14 = g_1038b244(v16, *(v17), v18);
        }
    }
    else if (a2 != 0xfc)
    {
        if (sub_10359f58(&g_103a33a8, 788, "Runtime Error!\n\nProgram: "))
        {
            v7 = 0;
            v6 = 0;
            v5 = 0;
            v4 = 0;
            v3 = 0;
            sub_103534f6();
        }
        g_103a34c5 = 0;
        if (!g_1038b1d4(0, &g_103a33c1, 260) && sub_10359f58(&g_103a33c1, 763, "<program name unknown>"))
        {
            v4 = 0;
            v3 = 0;
            v2 = 0;
            v1 = 0;
            v0 = 0;
            sub_103534f6();
        }
        if (sub_10352f20(&g_103a33c1) + 1 > 60 && !((v15 = (int)(sub_10352f20(&g_103a33c1) + &g_103a3386), !sub_1035f222(v15, &g_103a36bc - v15, "...", 3))))
        {
            v4 = 0;
            v3 = 0;
            v2 = 0;
            v1 = 0;
            v0 = 0;
            sub_103534f6();
        }
        if (sub_1035f1b1(&g_103a33a8, 788, "\n\n"))
        {
            v4 = 0;
            v3 = 0;
            v2 = 0;
            v1 = 0;
            v0 = 0;
            sub_103534f6();
        }
        if (sub_1035f1b1(&g_103a33a8, 788, g_1038e484[2 * v13]))
        {
            v4 = 0;
            v3 = 0;
            v2 = 0;
            v1 = 0;
            v0 = 0;
            sub_103534f6();
        }
        v14 = sub_10361a1e(&g_103a33a8, "Microsoft Visual C++ Runtime Library", 73744);
    }
    return v14;
}
```

## `sub_1035a15d` `0x1035a15d`

_57 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a3054;

unsigned int sub_1035a15d(unsigned int a0, unsigned int a1)
{
    unsigned int v1;  // eax
    unsigned int v2;  // edx
    unsigned int v3;  // ecx

    if (sub_10361bdb(3) != 1)
    {
        v1 = sub_10361bdb(3);
        if (v1)
        {
            return v1;
        }
        else if (g_103a3054 != 1)
        {
            return v1;
        }
    }
    sub_10359fbd(3, v2, 0xfc);
    return sub_10359fbd(v3, v2, 0xff);
}
```

## `sub_1035a196` `0x1035a196`

_346 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b07c;
extern unsigned int g_1038e180;
extern char g_103a36bc;
extern char g_103a36c4;

int sub_1035a196(int a0, unsigned int a1, int a2, int a3, void* a4)
{
    unsigned int v13;  // ebx
    unsigned int v14;  // esi
    unsigned int v15;  // edi
    char *v16;  // edi
    int v17;  // esi
    unsigned int v18;  // eax
    char *v19;  // edi
    char *v20;  // edi
    char *v21;  // edi
    unsigned int v0;  // [bp-0xb8]
    unsigned int v1;  // [bp-0xb4]
    unsigned int v2;  // [bp-0xb0]
    unsigned int v3;  // [bp-0xac]
    char *v4;  // [bp-0xa8], Other Possible Types: unsigned int
    unsigned int v5;  // [bp-0xa4]
    unsigned int v6;  // [bp-0xa0]
    unsigned int v7;  // [bp-0x9c]
    int v8;  // [bp-0x94]
    unsigned int v9;  // [bp-0x8c]
    char v10;  // [bp-0x88]
    char v11;  // [bp-0x68]
    unsigned int v12;  // [bp-0x8]

    v12 = g_1038e180 ^ &v11;
    v7 = v13;
    v6 = v14;
    v5 = v15;
    if (a1 == 1)
    {
        v16 = &v10;
        v9 = 0;
        v17 = sub_10361ed4(a0, a2, a3, &v10, 128, 0);
        if (v17)
        {
LABEL_1035a241:
            v18 = sub_103574c2(v17, 1);
            *((unsigned int *)a4) = v18;
            if (!v18)
            {
                if (v9)
                    goto LABEL_1035a259;
            }
            else
            {
                if (sub_1035f222(v18, v17, v16, v17 - 1))
                {
                    v4 = 0;
                    v3 = 0;
                    v2 = 0;
                    v1 = 0;
                    v0 = 0;
                    sub_103534f6();
                }
                if (v9)
                {
                    v4 = v16;
                    sub_1035345e();
                    goto LABEL_1035a2a1;
                }
            }
        }
        else if (g_1038b07c() == 122 && !((v8 = (int)sub_10361ed4(a0, a2, a3, 0, 0, 0), !v8 || (v16 = (char *)sub_103574c2(v8, 1), !v16))))
        {
            v9 = 1;
            v17 = sub_10361ed4(a0, a2, a3, v16, v8, 0);
            if (v17)
                goto LABEL_1035a241;
LABEL_1035a259:
            v4 = v16;
            sub_1035345e();
        }
LABEL_1035a260:
    }
    else
    {
        if (a1 || (v19 = &g_103a36bc, !sub_10361d5c(a0, a2, a3, &g_103a36bc, 4, 0)))
            goto LABEL_1035a260;
        *((char *)a4) = 0;
        do
        {
            v20 = v19;
        } while (sub_10357000(*(v20)) && (v21 = v20 + 2, *((char *)a4) = *((char *)(void*)&*((char *)a4) * 10) + *(v20) - 48, v19 = v20 + 2, v19 < &g_103a36c4));
LABEL_1035a2a1:
    }
    return sub_10351225();
}
```

## `sub_1035a2f0` `0x1035a2f0`

_10 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a36c4;

int sub_1035a2f0(unsigned int a0)
{
    g_103a36c4 = a0;
    return a0;
}
```

## `sub_1035a2fa` `0x1035a2fa`

_91 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1035a2fa(unsigned int a0)
{
    unsigned int v10;  // esi
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]
    unsigned int v8;  // [bp-0x8]

    v7 = a0;
    v6 = a0;
    v5 = v10;
    v8 = 0;
    v6 = 0;
    if (sub_10353d3b(&v8))
    {
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        sub_103534f6();
    }
    if (sub_10353d72(&v6))
    {
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        sub_103534f6();
    }
    if (v8 != 2)
    {
        v5 = 3;
        return v5;
    }
    else if (v6 >= 5)
    {
        return 1;
    }
    else
    {
        v5 = 3;
        return v5;
    }
}
```

## `sub_1035a355` `0x1035a355`

_90 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b24c;
extern struct_0 *g_1038b250;
extern unsigned int g_103a36c8;
extern unsigned int g_103a4cc0;

unsigned int sub_1035a355(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v0;  // ecx

    g_103a36c8 = g_1038b250(!a2, 0x1000, 0);
    if (!g_103a36c8)
        return 0;
    g_103a4cc0 = sub_1035a2fa(v0);
    if (g_103a4cc0 != 3)
    {
        return 1;
    }
    else if (!sub_1035a5ca(1016))
    {
        g_1038b24c(g_103a36c8);
        g_103a36c8 = 0;
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `sub_1035a3af` `0x1035a3af`

_116 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
    unsigned int field_10;
    char padding_14[16];
    char field_24;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b204;
extern struct_1 *g_1038b24c;
extern struct_1 *g_1038b254;
extern unsigned int g_103a36c8;
extern char g_103a4ca8;
extern struct_0 *g_103a4cac;
extern unsigned int g_103a4cc0;

void sub_1035a3af(void)
{
    unsigned int v4;  // ebx
    unsigned int v5;  // edi
    int i;  // edi
    unsigned int v7;  // esi
    unsigned int v8;  // esi
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    if (g_103a4cc0 == 3)
    {
        v2 = v4;
        v1 = v5;
        i = 0;
        if (*((int *)&g_103a4ca8) > 0)
        {
            v0 = v7;
            v8 = &g_103a4cac->field_10;
            do
            {
                g_1038b254(*((int *)(v8 - 4)), 0, 0x8000);
                g_1038b204(g_103a36c8, 0, *((int *)v8));
                v8 += 20;
                i += 1;
            } while (i < *((int *)&g_103a4ca8));
        }
        g_1038b204(g_103a36c8, 0, g_103a4cac);
    }
    g_1038b24c(g_103a36c8);
    g_103a36c8 = 0;
    return;
}
```

## `sub_1035a423` `0x1035a423`

_73 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e540[4];
extern unsigned int g_1038e544[4];
extern char g_103a36d0;

unsigned int sub_1035a423(void)
{
    int idx;  // esi
    unsigned int v2;  // edi
    int *v3;  // eax

    idx = 0;
    v2 = &g_103a36d0;
    while (true)
    {
        if (g_1038e544[2 * idx] == 0x1)
        {
            v3 = &g_1038e540[2 * idx];
            *(v3) = v2;
            v2 += 24;
            if (!sub_1035ca63(*(v3), 4000))
            {
                g_1038e540[2 * idx] = 0;
                return 0;
            }
        }
        idx += 1;
        if (idx >= 36)
            return 1;
    }
}
```

## `sub_1035a4c1` `0x1035a4c1`

_21 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1bc;
extern unsigned int g_1038e540[4];

int sub_1035a4c1(unsigned int a0)
{
    char v0;  // [bp+0x0]

    return g_1038b1bc(g_1038e540[2 * a0], &v0);
}
```

## `sub_1035a4d6` `0x1035a4d6`

_184 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e540[4];
extern int g_103a1240;
extern unsigned int g_103a36c8;

int sub_1035a4d6(unsigned int a0, unsigned int a1)
{
    unsigned int v5;  // ecx
    unsigned int v6;  // edx
    unsigned int *v7;  // esi
    int v8;  // edi
    int v0;  // [bp-0xc]
    unsigned int v2;  // [bp+0xfffe8]
    unsigned int v3;  // [bp+0x100000]
    unsigned int v4;  // [bp+0x10000c]

    sub_1035b0cc(&g_103a1240, 12);
    v2 = 1;
    if (!g_103a36c8)
    {
        sub_1035a15d(v5, v6);
        sub_10359fbd(v5, v6, 0x1e);
        sub_10353cdc(0xff); /* do not return */
    }
    v7 = &g_1038e540[2 * v4];
    if (*(v7))
        return sub_1035b111();
    v8 = sub_10357482(24);
    if (!v8)
    {
        *((unsigned int *)sub_103575e0()) = 12;
    }
    else
    {
        sub_1035a599(10);
        v3 = 0;
        if (*(v7))
        {
            v0 = v8;
            sub_1035345e();
        }
        else if (!sub_1035ca63(v8, 4000))
        {
            v0 = v8;
            sub_1035345e();
            *((unsigned int *)sub_103575e0()) = 12;
            v2 = 0;
        }
        else
        {
            *(v7) = v8;
        }
        v3 = 4294967294;
        sub_1035a590();
    }
    return sub_1035b111();
}
```

## `sub_1035a508` `0x1035a508`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1035a508(unsigned int a0)
{
}
```

