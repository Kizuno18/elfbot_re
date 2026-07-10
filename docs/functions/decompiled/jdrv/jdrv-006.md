# elfbot.dll decompiled — jdrv 0x10026545..0x1002ad6b

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10026545` `0x10026545`

_43 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_100428d1;
extern unsigned int g_100428d5;

void sub_10026545(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v0;  // [bp-0x1c]

    v0 = a0;
    g_100428d5 = a0;
    if (a2 != 4294967295)
        g_100428d1(a0, a1, a2, a3);
    return;
}
```

## `sub_10026570` `0x10026570`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10026570(void)
{
    return;
}
```

## `sub_10026571` `0x10026571`

_98 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern char g_1005f85c;
extern unsigned int g_100f42a8[3];
extern unsigned int g_100f45a8[3];

unsigned int sub_10026571(void)
{
    unsigned int iter[3];  // ebx
    unsigned int v4;  // eax
    int v5;  // eax
    int v6;  // eax
    unsigned int v0[3];  // [bp-0xc], Other Possible Types: unsigned int
    unsigned int v1;  // [bp-0x8]

    v1 = 4294967295;
    v0 = 0;
    for (iter = &g_100f42a8[0]; iter < &g_100f45a8[0]; iter += 1)
    {
        v4 = *((int *)&g_1005f85c);
        if (iter[0] && *((int *)&g_1005f85c) == iter[2])
        {
            v5 = g_1005f854 - iter[0];
            v6 = g_1005f858 - iter[1];
            v4 = (v6 ^ v6 >> 31) - (v6 >> 31) + (v5 ^ v5 >> 31) - (v5 >> 31);
            if (v4 < v1)
            {
                v1 = v4;
                v0 = iter;
            }
        }
    }
    return v4;
}
```

## `sub_100265d3` `0x100265d3`

_135 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern char g_1005f85c;
extern unsigned int g_100f42a8[3];
extern unsigned int g_100f45a8[3];

unsigned int sub_100265d3(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int iter[3];  // ebx
    unsigned int v4;  // eax
    unsigned int v5[3];  // ebx
    int v6;  // eax
    int v7;  // eax
    unsigned int idx[3];  // ebx
    unsigned int v0;  // [bp-0x10]
    unsigned int v1[3];  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v2 = 0;
    v1 = NULL;
    iter = &g_100f42a8[0];
    while (true)
    {
        if (iter < &g_100f45a8[0])
        {
            v4 = *((int *)&g_1005f85c);
            v5 = iter;
            if (!v5[0])
                break;
            if (*((int *)&g_1005f85c) == iter[2])
            {
                v6 = g_1005f854 - iter[0];
                v7 = g_1005f858 - iter[1];
                v4 = (v7 ^ v7 >> 31) - (v7 >> 31) + (v6 ^ v6 >> 31) - (v6 >> 31);
                if (v4 > v2)
                {
                    v2 = v4;
                    v1 = iter;
                }
            }
            else if (v2 < 4294967295)
            {
                v2 = 4294967295;
                v1 = iter;
            }
            iter += 1;
        }
        else
        {
            v5 = v1;
            break;
        }
    }
    idx = v5;
    if (v5)
    {
        v0 = a0;
        idx[0] = v0;
        v0 = a1;
        idx[1] = v0;
        v0 = a2;
        idx[2] = v0;
    }
    return v4;
}
```

## `sub_100265f4` `0x100265f4`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100265f4(void)
{
}
```

## `sub_100266b0` `0x100266b0`

_82 bytes. (leaf/helper — see body)_

```c
unsigned int sub_100266b0(unsigned int a0, char a1)
{
    char *iter;  // esi
    unsigned int v4;  // ecx
    char *node;  // edi
    char *v6;  // ebx
    char *v7;  // ebx
    int len;  // eax
    char *v9;  // ebx
    unsigned int v10;  // edi
    char v1;  // [bp+0xfff8f]

    v1 += a1;
    iter = /* unsupported instruction */ - 26;
    v4 = 0;
    while (*(node) && v4 < 20)
    {
        if (*(node) != 32)
        {
            *(iter) = *(node) | 32;
            iter += 1;
            v4 += 1;
            node += 1;
        }
        else
        {
            node += 1;
        }
    }
    *(iter) = 0;
    while (true)
    {
        v7 = v6;
        if (!*(v7))
            return 0;
        len = lstrlen(v7);
        v9 = &v7[len + 1];
        v10 = /* unsupported instruction */ - 26;
        do
        {
            if (!len)
                break;
        } while (*(v7) == *((char *)v10));
        v6 = v9;
        if (!len)
            return 1;
    }
}
```

## `sub_10026702` `0x10026702`

_34 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned short field_0;
    char field_2;
} struct_0;

char sub_10026702(void)
{
    unsigned int v1;  // ecx
    struct_0 *v2;  // ebx
    unsigned int i;  // edx
    struct_0 *node;  // esi
    char *iter;  // edi
    char v6;  // al

    v1 = 0;
    i = v2->field_0;
    for (node = &v2->field_2; i && v1 < 0xff; i -= 1)
    {
        v6 = node->field_0;
        *(iter) = node->field_0;
        v1 += 1;
        node = (char *)&node->field_0 + 1;
        iter += 1;
    }
    *(iter) = 0;
    return v6;
}
```

## `sub_10026724` `0x10026724`

_859 bytes. refs "party", "channel"_

```c
typedef struct struct_0 {
    char padding_0[32];
    char field_20;
} struct_0;

extern void* g_100f49e5;
extern unsigned int g_100f932c;
extern char g_100f9330;
extern unsigned int g_100f9331;
extern char g_100f9335;
extern unsigned int g_100f9336;
extern char g_100f933a;
extern int g_100f94cb;
extern char g_1014f38a;
extern char g_1014f3aa;
extern int g_1014f3ca;
extern int g_1014f3ea;
extern char g_1014f40a;
extern char g_101d5e2c;
extern char g_101d5e4c;

void* sub_10026724(void)
{
    void* len;  // eax
    unsigned int v6;  // cc_dep1
    unsigned int v15;  // eax
    unsigned int v16;  // cc_dep1
    int len1;  // eax
    unsigned int v18;  // edi
    int v19;  // ecx
    struct_0 *k;  // esi
    unsigned int v21;  // eax
    unsigned int v22;  // cc_dep1
    int len2;  // eax
    unsigned int v24;  // edi
    unsigned int v7;  // edi
    int v25;  // ecx
    struct_0 *l;  // esi
    int v27;  // eax
    unsigned int v28;  // cc_dep1
    unsigned int v29;  // edi
    void* v30;  // ecx
    struct_0 *m;  // esi
    void* v32;  // eax
    void* v33;  // eax
    void* v34;  // eax
    void* v8;  // ecx
    unsigned int v35;  // edi
    void* v36;  // ecx
    struct_0 *n;  // esi
    struct_0 *v38;  // ebx
    void* v39;  // eax
    void* v40;  // eax
    void* i0;  // ebx
    int v42;  // eax
    char *iter;  // edi
    int v44;  // ecx
    struct_0 *i;  // esi
    int v45;  // eax
    unsigned int v10;  // cc_dep1
    int v11;  // eax
    unsigned int v12;  // edi
    int v13;  // ecx
    int j;  // esi
    unsigned short v0;  // [bp-0x44]
    char v1;  // [bp-0x42]
    unsigned int v2;  // [bp-0x41]
    unsigned short v3;  // [bp-0x41]

    len = g_100f49e5;
    if (!*((char *)g_100f49e5))
        return g_100f49e5;
    if (g_1014f40a && (g_1014f38a || g_1014f3aa || (char)g_1014f3ca || g_101d5e2c || g_101d5e4c))
    {
        len = sub_100303be(g_100f49e5);
        if (len)
        {
            v6 = g_1014f38a;
            if (g_1014f38a)
            {
                len = lstrlen(&g_1014f38a);
                v7 = g_100f49e5 + 32;
                v8 = len;
                do
                {
                    if (!v8)
                        break;
                } while (g_1014f38a == *((char *)v7));
                if (!v6)
                {
                    for (i = len + g_100f49e5 + 32; i->padding_0[0] == 32; i = &i->padding_0[1]);
                    if (i->padding_0[0])
                    {
                        len = sub_100399af(i);
                        if (len)
                        {
                            g_100f932c = len;
                            g_100f9330 = 20;
                        }
                    }
                    else
                    {
                        g_100f932c = 0;
                        g_100f9330 = 0;
                    }
                }
            }
            v10 = g_1014f3aa;
            if (g_1014f3aa)
            {
                v11 = lstrlen(&g_1014f3aa);
                v12 = g_100f49e5 + 32;
                v13 = v11;
                do
                {
                    if (!v13)
                        break;
                } while (g_1014f3aa == *((char *)v12));
                if (!v10)
                {
                    for (j = v11 + g_100f49e5 + 32; *((char *)j) == 32; j += 1);
                    if (*((char *)j))
                    {
                        v15 = sub_100399af(j);
                        if (v15)
                        {
                            g_100f9331 = v15;
                            g_100f9335 = 20;
                            if (g_100f933a)
                            {
                                g_100f933a = g_100f933a + 3;
                                g_100f9335 = g_100f933a;
                            }
                        }
                    }
                    else
                    {
                        g_100f9331 = 0;
                        g_100f9335 = 0;
                    }
                }
            }
            v16 = (char)g_1014f3ca;
            if ((char)g_1014f3ca)
            {
                len1 = lstrlen(&g_1014f3ca);
                v18 = g_100f49e5 + 32;
                v19 = len1;
                do
                {
                    if (!v19)
                        break;
                } while ((char)g_1014f3ca == *((char *)v18));
                if (!v16)
                {
                    for (k = len1 + g_100f49e5 + 32; k->padding_0[0] == 32; k = &k->padding_0[1]);
                    if (k->padding_0[0])
                    {
                        v21 = sub_100399af(k);
                        if (v21)
                            g_100f9336 = v21;
                        if (!g_100f933a)
                            g_100f933a = 24;
                    }
                    else
                    {
                        g_100f9336 = 0;
                        g_100f933a = 0;
                    }
                }
            }
            v22 = g_101d5e2c;
            if (g_101d5e2c)
            {
                len2 = lstrlen(&g_101d5e2c);
                v24 = g_100f49e5 + 32;
                v25 = len2;
                do
                {
                    if (!v25)
                        break;
                } while (g_101d5e2c == *((char *)v24));
                if (!v22)
                {
                    for (l = len2 + g_100f49e5 + 32; l->padding_0[0] == 32; l = &l->padding_0[1]);
                    if (l->padding_0[0])
                    {
                        v27 = sub_100399af(l);
                        if (v27)
                            sub_1003a60a(v27, g_100f94cb);
                    }
                }
            }
            v28 = g_101d5e4c;
            if (g_101d5e4c)
            {
                len = lstrlen(&g_101d5e4c);
                v29 = g_100f49e5 + 32;
                v30 = len;
                do
                {
                    if (!v30)
                        break;
                } while (g_101d5e4c == *((char *)v29));
                if (!v28)
                {
                    for (m = len + g_100f49e5 + 32; m->padding_0[0] == 32; m = &m->padding_0[1]);
                    if (m->padding_0[0])
                    {
                        len = sub_100399af(m);
                        if (len)
                            g_100f9336 = len;
                        if (!g_100f933a)
                            g_100f933a = 24;
                    }
                    else
                    {
                        g_100f9336 = 0;
                        g_100f933a = 0;
                    }
                }
            }
        }
    }
    if (!(char)g_1014f3ea)
        return len;
    v32 = sub_1003a320(g_100f49e5);
    if (!v32)
    {
        v33 = sub_1003a3da(g_100f49e5);
        v32 = v33;
        if (!v33)
            return v33;
    }
    v34 = lstrlen(&g_1014f3ea);
    v35 = g_100f49e5 + 32;
    v36 = v34;
    do
    {
        if (!v36)
            break;
    } while ((char)g_1014f3ea == *((char *)v35));
    if (!v32)
    {
        for (n = v34 + g_100f49e5 + 32; n->padding_0[0] == 32; n = &n->padding_0[1]);
        v38 = n;
        if (!lstrcmpi(v38, "party"))
        {
            v39 = sub_100399af(g_100f49e5);
            if (!v39)
                return v39;
            v0 = 5;
            v1 = 163;
            v2 = *((int *)v39);
            return sub_1002ade7(&v0, 7);
        }
        v40 = lstrcmpi(v38, "channel");
        if (v40)
            return v40;
        i0 = g_100f49e5;
        v42 = lstrlen(g_100f49e5);
        v3 = v42;
        iter = &v2;
        for (v44 = v42; v44; i0 += 1)
        {
            v44 -= 1;
            *(iter) = *((char *)i0);
            iter += 1;
        }
        v45 = v42 + 3;
        v0 = v45;
        v1 = 171;
        v34 = sub_1002ade7(&v0, v45 + 1);
    }
    return v34;
}
```

## `sub_10026a7f` `0x10026a7f`

_96 bytes. calls WritePrivateProfileStringA; refs "serverlist.txt", "Servers"_

```c
extern int g_10042d7b;

int sub_10026a7f(void)
{
    int dst;  // eax
    unsigned int i;  // ecx
    unsigned int v5;  // ebx
    unsigned int v0;  // [bp-0x134]
    Byte v1[300];  // [bp-0x130]

    lstrcpy(v1, &g_10042d7b);
    dst = lstrcat(v1, "serverlist.txt");
    i = *((int *)0x79cee0);
    if (!*((int *)0x79cedc))
        return dst;
    for (v5 = *((int *)0x79cedc); i; i -= 1)
    {
        v0 = i;
        dst = WritePrivateProfileStringA("Servers", v5 + 30, v5 + 64, v1);
        v5 += 84;
    }
    return dst;
}
```

## `sub_10026adf` `0x10026adf`

_7340 bytes. refs "Server is saving game in "_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned short field_4;
} struct_0;

typedef struct struct_6 {
    char padding_0[144];
    char field_90;
} struct_6;

typedef struct struct_7 {
    char padding_0[88];
    unsigned short field_58;
} struct_7;

typedef struct struct_1 {
    unsigned short field_0;
    char field_2;
} struct_1;

typedef struct struct_9 {
    char padding_0[32];
    char field_20;
} struct_9;

typedef struct struct_2 {
    unsigned short field_0;
    unsigned short field_2;
    char padding_4[1];
    char field_5;
    unsigned short field_6;
    char field_8;
} struct_2;

typedef struct struct_11 {
    unsigned short field_0;
    unsigned short field_2;
    char field_4;
} struct_11;

typedef struct struct_14 {
    char padding_0[4];
    unsigned int field_4;
} struct_14;

typedef struct struct_15 {
    unsigned int field_0;
    unsigned int field_4;
} struct_15;

typedef struct struct_16 {
    char padding_0[36];
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
    char padding_30[96];
    char field_90;
} struct_16;

typedef struct struct_18 {
    char padding_0[136];
    unsigned int field_88;
} struct_18;

typedef struct struct_3 {
    char padding_0[2];
    unsigned short field_2;
    char field_4;
    unsigned short field_5;
    unsigned short field_7;
    char field_9;
} struct_3;

typedef struct struct_21 {
    unsigned int field_0;
    char field_4;
    char padding_5[1];
    char field_6;
} struct_21;

typedef struct struct_4 {
    char padding_0[36];
    unsigned short field_24;
    char padding_26[2];
    unsigned short field_28;
    char padding_2a[2];
    char field_2c;
    char padding_2d[91];
    unsigned int field_88;
} struct_4;

typedef struct struct_5 {
    unsigned int field_0;
} struct_5;

extern char g_10026b93;
extern char g_10026cdd;
extern char g_10028963;
extern struct_5 *g_100428bd;
extern char g_1004335d;
extern unsigned short g_100434c9;
extern unsigned short g_100434cb;
extern char g_100434cd;
extern unsigned short g_100434ce;
extern char g_100434d0;
extern char g_100434d1;
extern char g_10043846;
extern char g_1004384e;
extern char g_10043854;
extern char g_1004385b;
extern char g_10043863;
extern char g_10043868;
extern char g_10043874;
extern char g_10043881;
extern char g_10043890;
extern char g_100584ac;
extern unsigned int g_1005dbac;
extern unsigned int g_1005dbb0;
extern unsigned int g_1005dbb4;
extern unsigned int g_1005dbb8;
extern unsigned int g_1005dc28;
extern unsigned int g_1005dc2c;
extern unsigned int g_1005dc30;
extern unsigned int g_1005dc34;
extern unsigned int g_1005dc38;
extern unsigned int g_1005dc3c;
extern unsigned int g_1005dc40;
extern unsigned int g_1005dc44;
extern struct_2 g_1005e1a0;
extern struct_2 g_1005e5a0;
extern struct_2 g_1005e6a0;
extern unsigned int g_1005f561;
extern unsigned int g_1005f565;
extern unsigned int g_1005f569;
extern int g_1005f56d;
extern unsigned int g_1005f5ad;
extern unsigned int g_1005f5ed;
extern unsigned int g_1005f5f1;
extern unsigned int g_1005f5f5;
extern unsigned int g_1005f5f9;
extern unsigned int g_1005f5fd;
extern unsigned int g_1005f601;
extern unsigned int g_1005f605;
extern int g_1005f7b1;
extern char g_1005f7d9;
extern char g_1005f7da;
extern char g_1005f7db;
extern char g_1005f7dc;
extern char g_1005f7dd;
extern char g_1005f7de;
extern char g_1005f7df;
extern char g_1005f7e0;
extern unsigned int g_1005f7e1;
extern char g_1005f7ed;
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern char g_1005f85c;
extern char g_10077174;
extern char g_10077175;
extern char g_100809cd;
extern char g_10080b6e;
extern unsigned int g_10080baf;
extern unsigned int g_10080bb3;
extern unsigned int g_10080bb7;
extern unsigned int g_10080bbb;
extern unsigned int g_10080bbf;
extern unsigned int g_10080bc3;
extern unsigned int g_10080bc7;
extern unsigned int g_10080bcb;
extern unsigned int g_10080bcf;
extern unsigned int g_10080bd3;
extern unsigned int g_10080bd7;
extern unsigned int g_10080bdb;
extern unsigned int g_10080bdf;
extern void* g_10080be3;
extern unsigned int g_10080be7;
extern unsigned int g_10080beb;
extern unsigned int g_10080bef;
extern unsigned int g_10080bf3;
extern unsigned int g_1008b723;
extern unsigned int g_1008b727;
extern unsigned int g_1008b72b;
extern struct_15 g_1008b7f3;
extern struct_15 g_1008b893;
extern unsigned int g_1008b897;
extern int g_1008b89b;
extern unsigned int g_1008b8a8;
extern unsigned int g_1008b8dc;
extern unsigned int g_1008b8e0;
extern unsigned int g_1008b8ec;
extern unsigned int g_1008b8f0;
extern unsigned int g_1008b945[4];
extern char g_1008b96d;
extern unsigned int g_1009a52e;
extern unsigned int g_1009a532;
extern unsigned int g_100f0dc4;
extern unsigned int g_100f0dcc;
extern unsigned int g_100f0dd0;
extern unsigned int g_100f0dd4;
extern unsigned int g_100f0ddc;
extern int g_100f0e34;
extern unsigned int g_100f0e38;
extern unsigned int g_100f0e3c;
extern unsigned int g_100f0e48;
extern unsigned int g_100f0e4c;
extern unsigned int g_100f0e50;
extern unsigned int g_100f0e7c;
extern char g_100f45ac;
extern char g_100f45bc;
extern char g_100f45bd;
extern char g_100f45c1;
extern unsigned int g_100f49c9;
extern unsigned int g_100f49d5;
extern unsigned int g_100f49d9;
extern void* g_100f49e5;
extern unsigned int g_100f49ed;
extern unsigned int g_100f49f5;
extern unsigned int g_100f49f9;
extern unsigned int g_100f49fd;
extern unsigned int g_100f4a01;
extern struct_1 g_100f8d09;
extern char g_100f9314;
extern char g_100f9316;
extern char g_100f9317;
extern unsigned int g_100f9318;
extern unsigned int g_100f9320;
extern unsigned short g_100f9324;
extern char g_100f94c8;
extern char g_100fa4ef;
extern char g_100fa97b;
extern char g_10134e6b;
extern char g_1014f40d;
extern char g_1014f40e;
extern char g_1014f40f;
extern char g_1014f417;
extern char g_101d5e6c;
extern unsigned int g_101dfe94;
extern char g_101dfea3;
extern unsigned int g_10207f15;
extern char g_10207f33;
extern char g_10207f34;
extern char g_799cfd;

char * sub_10026adf(unsigned int a0, unsigned int a1)
{
    void* v32;  // ebp
    unsigned long v33;  // ldt
    void* v42;  // esi
    struct_6 *v129;  // ebx
    struct_6 *v130;  // eax
    char idx[144];  // eax
    char v132;  // cl
    char v133;  // cl
    struct_3 *v134;  // ebx
    struct_3 *v135;  // ebx
    unsigned int v136;  // ecx
    struct_3 *v137;  // ebx
    char *v43;  // edi
    char v138;  // cl
    unsigned int v139;  // ecx
    unsigned int v140;  // cc_dep1
    char *v141;  // edi
    char v142;  // al
    unsigned int v143;  // eax
    void* v144;  // esi
    unsigned int v145;  // eax
    struct_21 *v146;  // esi
    unsigned int i5;  // ecx
    char *v44;  // edi
    struct_21 *v148;  // esi
    unsigned int iter;  // ecx
    struct_21 *v150;  // esi
    unsigned int iter1;  // ecx
    unsigned int v152;  // ecx
    void* v153;  // esi
    char *iter2;  // edi
    unsigned int i6;  // eax
    unsigned int v156;  // ecx
    unsigned int v157;  // eax
    void* v45;  // ebx
    void* v158;  // edx
    char i7;  // cl
    void* v160;  // eax
    unsigned int v161;  // ebx
    char *v162;  // edx
    unsigned int v163;  // cc_dep1
    void* v164;  // edi
    unsigned int v165;  // ecx
    char *v166;  // esi
    void* v167;  // edi
    struct_0 *v46;  // edx
    void* v168;  // eax
    char i8;  // cl
    void* idx1;  // edx
    void* v171;  // edi
    void* v172;  // edi
    void* i9;  // ebx
    struct_0 *v47;  // edx
    void* i10;  // edi
    void* v175;  // eax
    void* v176;  // edi
    unsigned int v177;  // ebx
    char i19;  // cl
    void* v179;  // esi
    unsigned int v48;  // ebx
    void* v180;  // edi
    unsigned int i11;  // ecx
    unsigned int count;  // eax
    unsigned int v183;  // eax
    unsigned int v184;  // eax
    unsigned int v185;  // esi
    unsigned int v186;  // edi
    struct_6 *v187;  // ebx
    struct_2 *i20;  // eax
    struct_18 *v189;  // eax
    struct_0 *v49;  // edx
    void* v190;  // edx
    unsigned int v192[41];  // eax
    unsigned int v193[41];  // ecx
    struct_4 *v194;  // eax
    unsigned int v195;  // ecx
    struct_2 *i12;  // esi
    struct_4 *idx2;  // ebx
    unsigned int v198;  // eax
    unsigned int i13;  // ebx
    struct_6 *i;  // ebx
    unsigned int v200;  // eax
    struct_9 *v201;  // eax
    int v202;  // eax
    unsigned int i14;  // ecx
    unsigned int v204;  // ecx
    unsigned long v205;  // 4129
    unsigned int v51;  // eax
    unsigned long v34;  // gdt
    unsigned int v52;  // eax
    struct_6 *j;  // ebx
    struct_7 *v54;  // ebx
    void* v55;  // esi
    void* v56;  // eax
    void* v57;  // ebx
    void* index;  // edx
    void* v59;  // ebx
    unsigned short v35;  // fs
    struct_1 *v60;  // esi
    unsigned int k;  // ecx
    void* v62;  // ebx
    void* v63;  // ebx
    unsigned int m[35];  // ebx
    void* v65;  // edx
    unsigned int v66;  // ecx
    struct_9 *v67;  // eax
    unsigned int *v68;  // eax
    void* v69;  // edx
    unsigned long v36;  // 4137
    unsigned int v70;  // eax
    unsigned int v71;  // ebx
    unsigned int v72;  // ecx
    struct_2 *node;  // esi
    unsigned int v74;  // eax
    unsigned int v75;  // eax
    unsigned int v76;  // eax
    unsigned int v77;  // ecx
    unsigned int v78;  // ebx
    unsigned int n;  // ecx
    unsigned int v37;  // 4111
    void* v80;  // esi
    char *v81;  // edi
    unsigned int v82;  // eax
    unsigned int v83;  // ecx
    void* v84;  // edx
    struct_6 *i0;  // ebx
    struct_11 *v86;  // eax
    unsigned int i1;  // ecx
    unsigned int v88;  // esi
    char *v89;  // edi
    unsigned long v38;  // 4145
    unsigned int v90;  // eax
    struct_11 *v91;  // edx
    struct_6 *i2;  // ebx
    unsigned int v93;  // ecx
    unsigned int v94;  // esi
    unsigned int v95;  // edi
    struct_7 *v96;  // ebx
    void* v97;  // edx
    struct_14 *v98;  // eax
    void* v39;  // eax
    unsigned int v99;  // ebx
    unsigned int v100;  // eax
    struct_15 *i3;  // ecx
    void* v102;  // edx
    unsigned int v103;  // ecx
    unsigned int v104;  // esi
    unsigned int v105;  // edi
    struct_16 *v106;  // ebx
    struct_2 *i15;  // eax
    unsigned int v108[41];  // eax
    unsigned int v40;  // ecx
    char *v109;  // esi
    void* i16;  // edi
    unsigned int v111;  // ecx
    char v112;  // dl
    void* v113;  // edx
    unsigned int v114;  // eax
    unsigned int v115;  // eax
    unsigned int v116;  // ecx
    char *v117;  // esi
    char *v118;  // eax
    struct_0 *v41;  // edx
    void* v120;  // edx
    unsigned int v121;  // ecx
    unsigned int v122;  // esi
    unsigned int v123;  // edi
    struct_16 *i4;  // ebx
    unsigned int v125;  // eax
    void* v126;  // edx
    struct_18 *v127;  // eax
    void* v128;  // edx
    unsigned int v0[41];  // [bp-0x214]
    unsigned int v1[41];  // [bp-0x210]
    char *v2;  // [bp-0x200]
    struct_3 *v3;  // [bp-0x1f8], Other Possible Types: char *
    char *v4;  // [bp-0x1f4], Other Possible Types: unsigned int
    void* v5;  // [bp-0x1f0], Other Possible Types: unsigned int
    char *v6;  // [bp-0x1ec], Other Possible Types: struct_0 *, struct_6 *
    char *v7;  // [bp-0x1e8]
    void* v8;  // [bp-0x1e4]
    void* v9;  // [bp-0x1e0], Other Possible Types: char *
    void* v10;  // [bp-0x1dc], Other Possible Types: unsigned int
    void* v11;  // [bp-0x1d8], Other Possible Types: unsigned int
    struct_11 *v12;  // [bp-0x1d4], Other Possible Types: struct_6 *, void*, struct_0 *, int, unsigned int
    unsigned int v13[35];  // [bp-0x1d0], Other Possible Types: void*, unsigned int
    void* v14;  // [bp-0x1cc], Other Possible Types: unsigned int
    void* v15;  // [bp-0x1c4]
    char *v16;  // [bp-0x1c0]
    char *v17;  // [bp-0x1bc]
    struct_0 *v18;  // [bp-0x1b4]
    unsigned int v19;  // [bp-0x1b0]
    void* v20;  // [bp-0x1ac]
    unsigned int v21;  // [bp-0x1a8]
    unsigned int v22;  // [bp-0x19c]
    unsigned int v23[41];  // [bp-0x198], Other Possible Types: unsigned int [4], unsigned long long, unsigned int
    unsigned short v24;  // [bp-0x190]
    unsigned int v25[41];  // [bp-0x154]
    int v27;  // [bp-0x140]
    int v28;  // [bp-0x138], Other Possible Types: char
    char v29;  // [bp-0xc]
    char v30;  // [bp+0x0]

    v29 = _INSERT(*((uint96_t *)(&v27 + 8)), 8, &v30);
    v32 = &v29 + 8;
    g_1005dc28 = 0;
    g_1005dc2c = 0;
    g_1005dc30 = 0;
    g_1005dc34 = 0;
    g_1005dc38 = 0;
    g_1005dc3c = 0;
    g_1005dc40 = 0;
    g_1005dc44 = 0;
    v36 = _ccall(v33, v34, (unsigned int)v35, 0);
    v37 = *((int *)v36);
    v21 = *((int *)v36);
    v38 = _ccall(v33, v34, (unsigned int)v35, 0);
    *((unsigned int **)v38) = &v21;
    g_1005dbb8 = &v29 + 8;
    g_1005dbb4 = &v21;
    g_1005dbac = 1;
    v39 = g_100428bd(v37, sub_100027ef);
    g_1005dbb8 = &v29 + 8;
    g_1005dbb4 = &v21;
    g_1005dbac = 2;
    g_1005dbb0 = &g_10026b93;
    v20 = v39;
    v19 = v40;
    v18 = v41;
    v17 = &v21;
    v16 = &v29 + 8;
    v15 = v42;
    g_1005dbb8 = &v29 + 8;
    g_1005dbb4 = &/* unsupported instruction */;
    g_1005dbac = 3;
    g_1005dbb0 = &g_10026cdd;
    g_10080bdf = g_10080bdb;
    g_10080bdb = v39;
    v44 = v43;
    if (g_10080beb)
    {
        v14 = v39;
        v13 = g_10080bdf;
        v12 = v41;
        v11 = v45;
        v10 = &/* unsupported instruction */;
        v9 = &v29 + 8;
        v8 = v42;
        v7 = v43;
        v46 = v41;
        if (v39 == 0xaa && !((v47 = (struct_0 *)(*((int *)0x7998ac) + *((int *)0x7998b4)), v48 = (unsigned int)v47->field_4, v46 = v47, v46[1].padding_0[2 + v48] != 1 || (v46 = v47, *((short *)&v46[1].padding_0[3 + v48]) != (unsigned short)g_10080beb || (v46 = v47, *((short *)(11 + v48 + (char *)v46)) != (unsigned short)g_10080bef || (v46 = v47, v46[2].padding_0[1 + v48] != (char)g_10080bf3))))))
        {
            v32 = &v29 + 8;
            v11 = v45;
            v44 = v43;
        }
        else
        {
            v49 = v46;
            i = 0x63fef8;
            for (v51 = 0; i < 0x64a308; i = &i[1].padding_0[23])
            {
                if (i->field_90 && g_10080beb == *((int *)&i->padding_0[36]) && g_10080bef == *((int *)&i->padding_0[40]) && g_10080bf3 == *((int *)&i->padding_0[44]))
                    v51 += 1;
            }
            if (v51)
            {
                v6 = v49;
                v52 = 200 / v51;
                for (j = 0x63fef8; j < 0x64a308; j = &j[1].padding_0[23])
                {
                    if (j->field_90 && g_10080beb == *((int *)&j->padding_0[36]) && g_10080bef == *((int *)&j->padding_0[40]) && g_10080bf3 == *((int *)&j->padding_0[44]))
                    {
                        v6 = j;
                        v5 = v52;
                        v54 = &(&g_10077175)[156 * (unsigned long long)(struct struct_6 *)&j[45195].padding_0[61] / 168];
                        if (v54->field_58 > (unsigned short)v52)
                            v54->field_58 = v54->field_58 - (unsigned short)v52;
                        else
                            v54->field_58 = 0;
                        *((unsigned short *)&v54[1].padding_0[0]) = 300;
                    }
                }
            }
            v32 = &v29 + 8;
            v11 = v45;
            v44 = v43;
        }
    }
    v141 = v44;
    g_1005dbb8 = &v29 + 8;
    g_1005dbb4 = &/* unsupported instruction */;
    g_1005dbac = 4;
    g_1005dbb0 = &g_10028963;
    g_1005dbac = v39;
    g_10080beb = 0;
    if (v39 == 0xffffffff)
    {
        sub_10029b3b();
    }
    else
    {
        v14 = v39;
        g_1008b72b = GetTickCount();
        v56 = v39;
        v57 = 0x7998b4;
        index = *((int *)0x7998ac) + *((int *)0x7998b4);
        g_1005dc28 = *((int *)index);
        g_1005dc2c = (int)index[4];
        g_1005dc30 = (int)index[8];
        g_1005dc34 = (int)index[12];
        g_1005dc38 = (int)index[16];
        g_1005dc3c = (int)index[20];
        g_1005dc40 = (int)index[24];
        g_1005dc44 = (int)index[28];
        *((void* *)&v29) = index;
        if (v56 == 0xa)
        {
            sub_10026a7f();
            g_100f9314 = 1;
            g_100f9316 = 0;
            g_100f9317 = 1;
            g_100f9324 = 1;
        }
        else if (v56 == 0x7a)
        {
            v59 = index;
            v60 = &g_100f8d09.field_0;
            k = *((char *)v59);
            for (v62 = v59 + 1; k; k -= 1)
            {
                v63 = v62 + 2;
                if (*((char *)v63))
                {
                    v60->field_0 = *((short *)v62);
                    v60->field_2 = *((char *)v63);
                    v60 = (char *)&v60[1].field_0 + 1;
                }
                v62 = (short)v63[1] + v63 + 1 + 14;
            }
        }
        else if (v56 == 0x6a)
        {
            g_100f0e34 = (short)index[6];
            if (g_100f0e34 == 2128 || g_100f0e34 == 2129 || g_100f0e34 == 2130 || g_100f0e34 == 10181 || g_100f0e34 == 10182)
            {
                for (node = &g_1005e1a0.field_0; node < &g_1005e5a0.field_0; node = (char *)&node[1].field_6 + 1)
                {
                    if (!node->field_6)
                    {
                        node->field_0 = *((short *)index);
                        node->field_2 = (short)index[2];
                        node->field_5 = (char)index[4];
                        node->field_6 = 200;
                        if (g_100f0e34 == 2130 || g_100f0e34 == 10182)
                            node->field_6 = 450;
                        node->field_8 = 1;
                        break;
                    }
                }
            }
            else
            {
                if (g_100f0e34 > 0x64 && ((unsigned short)sub_1003c4fa(g_100f0e34) & 8272) == 8272)
                {
                    for (m = 0x63fef8; m < 0x64a308; m = &m[1 + 7])
                    {
                        v65 = *((unsigned int *)&v29);
                        v66 = (char)v65[4];
                        if (!m[0x22] && m[9] == *((short *)v65) && m[10] == (short)v65[2] && m[11] == v66 && v66 == *((int *)&g_1005f85c) && !((v13 = m, v67 = (struct_9 *)sub_10012827(m, 0, 1), m = m, !v67 || !v67->field_20)))
                        {
                            if (m[0] == g_100f0e38)
                            {
                                g_100f0e38 = 0;
                                g_100f0e3c = 0;
                            }
                            v68 = sub_10039fee(m);
                            if (v68)
                                g_100434d0 = *(v68) - (char)v40;
                            g_100434ce = g_100f0e34;
                            v69 = *((unsigned int *)&v29);
                            v70 = *((short *)v69);
                            v71 = (short)v69[2];
                            v72 = (char)v69[4];
                            g_100434c9 = v70;
                            g_100434cb = v71;
                            g_100434cd = v72;
                            if (v70 - g_1005f854 + 1 <= 2 && v71 - g_1005f858 + 1 <= 2 && v72 == *((int *)&g_1005f85c) && g_10207f34)
                            {
                                g_100434d1 = sub_10038d20();
                                sub_1002ade7("\n", 12);
                                g_100f0dcc = 15;
                                g_100f0dd0 = 4294967295;
                            }
                            else
                            {
                                if (g_10207f33)
                                    sub_100265d3(*((short *)v69), (short)v69[2], v72);
                            }
                            break;
                        }
                        else
                        {
                        }
                    }
                }
            }
        }
        else if (v56 == 0x86)
        {
            v74 = *((int *)index);
            if ((char)index[3] == 64)
                g_1005f5fd = v74;
            else
                g_1005f601 = v74;
            g_1005f605 = v74;
            v75 = sub_1003997e(*((int *)index));
            if (v75)
            {
                v76 = &(&g_10077175)[156 * (v75 - 0x63fef8) / 168];
                *((char *)(v76 + 137)) = 1;
                *((char *)(v76 + 138)) = 0;
            }
        }
        else if (v56 == 0xa0)
        {
            if (!*((short *)index) && g_1014f417)
                sub_10040318(0, 0);
        }
        else
        {
            if (v56 == 0x6e)
            {
                v77 = *((char *)index);
                if (g_10207f33 || g_10207f34)
                {
                    if (!(&g_100f45ac)[v77])
                        (&g_100f45ac)[v77] = 1;
                    g_100f0dd0 = 0;
                    g_100f0dcc = 2;
                }
                if (g_100f9318 != 0xffffffff)
                {
                    if (v77 == *((int *)&g_100f45bd) && (short)index[1] == *((int *)&g_100f45c1))
                    {
                        g_100f9318 = g_100f9318 + 1;
                        g_100f45bc = 0;
                    }
                }
                else
                {
                    if (v77 == *((int *)&g_100f45bd))
                        g_100f45bc = 0;
                }
            }
            else if (v56 == 0x78)
            {
                v78 = (short)index[1];
                if (*((char *)index) == 5)
                {
                    g_100f0e48 = v78;
                }
                else
                {
                    if (*((char *)index) == 6)
                    {
                        g_100f0e4c = v78;
                    }
                    else
                    {
                        if (*((char *)index) == 10)
                            g_100f0e50 = v78;
                    }
                }
            }
            else if (v56 == 0x79)
            {
                if (*((char *)index) == 9)
                    g_1004335d = 0;
            }
            else
            {
                if (v56 == 0x6c)
                {
                    v23 = 0;
                }
                else if (v56 == 0xb5)
                {
                    g_100f0dc4 = 0;
                }
                else if (v56 == 0x84)
                {
                    if (*((int *)&g_1005f7ed) && *((short *)index) == *((int *)(*((int *)&g_1005f7ed) + 36)) && (short)index[2] == *((int *)(*((int *)&g_1005f7ed) + 40)) && (char)index[4] == *((int *)(*((int *)&g_1005f7ed) + 44)))
                    {
                        n = (short)index[6];
                        v80 = index + 8;
                        for (v81 = &v27 + -0x8; n; n -= 1)
                        {
                            *(v81) = *((char *)v80);
                            v80 += 1;
                            v81 += 1;
                        }
                        *(v81) = 0;
                        v82 = sub_10040900(&v27 - 8);
                        v83 = *((char *)(*((unsigned int *)&v29) + 5));
                        if (g_10080be7 && v83 == 30)
                            g_1005f7e1 = v82;
                        if (v83 != 215)
                        {
                            g_1005f5f9 = v83;
                            g_1005f5f1 = v82;
                            v13 = g_1005f605;
                            g_1005f5ed = g_1005f605;
                            g_1005f5f5 = GetTickCount();
                        }
                    }
                    v84 = *((unsigned int *)&v29);
                    if ((char)v84[5] == 5)
                    {
                        i0 = 0x63fef8;
                        for (v86 = NULL; i0 < 0x64a308; i0 = &i0[1].padding_0[23])
                        {
                            if (i0->field_90 && *((short *)v84) == *((int *)&i0->padding_0[36]) && (short)v84[2] == *((int *)&i0->padding_0[40]) && (char)v84[4] == *((int *)&i0->padding_0[44]))
                                v86 = (char *)&v86->field_0 + 1;
                        }
                        if (v86)
                        {
                            v13 = v84;
                            v12 = v86;
                            i1 = (short)v84[6];
                            v88 = v84 + 8;
                            for (v89 = &v27 + -0x8; i1; i1 -= 1)
                            {
                                *(v89) = *((char *)v88);
                                v88 += 1;
                                v89 += 1;
                            }
                            *(v89) = 0;
                            v90 = sub_10040900(&v27 - 8) / (&v27 - 8);
                            v91 = v86;
                            i2 = 0x63fef8;
                            v93 = v91->field_0;
                            v94 = v91->field_2;
                            for (v95 = v91->field_4; i2 < 0x64a308; i2 = &i2[1].padding_0[23])
                            {
                                if (i2->field_90 && v93 == *((int *)&i2->padding_0[36]) && v94 == *((int *)&i2->padding_0[40]) && v95 == *((int *)&i2->padding_0[44]))
                                {
                                    v12 = i2;
                                    v11 = v90;
                                    v96 = &(&g_10077175)[156 * (unsigned long long)(struct struct_6 *)&i2[45195].padding_0[61] / 168];
                                    v96->field_58 = v96->field_58 + (unsigned short)v90;
                                    *((unsigned short *)&v96[1].padding_0[0]) = 300;
                                }
                            }
                        }
                    }
                }
                else if (v56 == 0x85)
                {
                    if (g_1008b893.field_0 && g_1008b897 && (char)index[10] == 4)
                    {
                        v97 = *((unsigned int *)&v29);
                        if (*((short *)v97) == (unsigned short)g_1005f854 && (short)v97[2] == (unsigned short)g_1005f858 && (char)v97[4] == (char)*((int *)&g_1005f85c))
                        {
                            v98 = sub_10039ab9((int)v97[5], (int)v97[7], (int)v97[9]);
                            if (v98)
                            {
                                v99 = v98->field_4;
                                if (v99 == g_1008b893.field_0)
                                {
                                    v100 = GetTickCount() - 20000;
                                    for (i3 = &g_1008b7f3.field_0; i3 < &g_1008b893.field_0; i3 += 1)
                                    {
                                        if (i3->field_0 == v99)
                                        {
                                            i3->field_4 = v100 + 20000;
                                            g_1008b893.field_0 = 0;
                                            break;
                                        }
                                        else
                                        {
                                            if (!i3->field_0 || i3->field_4 < v100)
                                            {
                                                i3->field_0 = v99;
                                                i3->field_4 = v100 + 20000;
                                                g_1008b893.field_0 = 0;
                                                break;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                    v102 = *((unsigned int *)&v29);
                    v103 = *((short *)v102);
                    v104 = (short)v102[2];
                    v105 = (char)v102[4];
                    v106 = 0x63fef8;
                    while (true)
                    {
                        if (v106 < 0x64a308)
                        {
                            if (v106->field_90 && v103 == v106->field_24 && v104 == v106->field_28 && v105 == v106->field_2c)
                                break;
                            v106 = &v106[1].padding_0[23];
                        }
                        else
                        {
                            for (i15 = &g_1005e5a0.field_0; i15 < &g_1005e6a0.field_0; i15 = (char *)&i15[1].field_6 + 1)
                            {
                                if (!i15->field_6)
                                {
                                    i15->field_0 = v103;
                                    i15->field_2 = v104;
                                    i15->field_5 = v105;
                                    i15->field_6 = 20;
                                    i15->field_8 = 3;
                                    break;
                                }
                            }
                        }
                    }
                    if (*((char *)(*((unsigned int *)&v29) + 10)) == 32 && *((int *)&g_1005f7ed) && *((char *)(*((int *)&g_1005f7ed) + 44)) == *((char *)(*((unsigned int *)&v29) + 9)))
                    {
                        if (g_10134e6b)
                        {
                            v108 = sub_10039ab9(*((int *)(*((unsigned int *)&v29) + 5)), *((int *)(*((unsigned int *)&v29) + 7)), *((int *)(*((unsigned int *)&v29) + 9)));
                            if (v108)
                            {
                                v25 = v108;
                                if (!v108[37] && v108[40] != 2)
                                {
                                    v108 = sub_1003a494(&v108[1]);
                                    if (v108)
                                    {
                                        if (g_1014f40d)
                                            goto LABEL_10027887;
                                    }
                                    else
                                    {
                                        v108 = sub_1003a550(&v25[1]);
                                        if (v108)
                                        {
                                            if (g_1014f40e)
                                                goto LABEL_10027887;
                                        }
                                        else
                                        {
                                            v108 = v25;
                                            if (g_1014f40f)
                                                goto LABEL_10027887;
                                        }
                                    }
                                }
                                if (v108)
                                {
                                    v109 = &g_10134e6b;
                                    *((unsigned int *)&v23) = 0;
                                    while (true)
                                    {
                                        i16 = (char *)&v23 + 4;
                                        v111 = 1;
                                        while (true)
                                        {
                                            v112 = *(v109);
                                            if (*(v109) == 44)
                                            {
                                                v109 += 1;
                                                break;
                                            }
                                            else
                                            {
                                                if (v112 == 32 && v111)
                                                {
                                                    v109 += 1;
                                                }
                                                else
                                                {
                                                    if (!v112)
                                                        break;
                                                    *((char *)i16) = v112;
                                                    v111 = 0;
                                                    v109 += 1;
                                                    i16 += 1;
                                                }
                                            }
                                        }
                                        for (*((char *)i16) = 0; i16 > (char *)&v23 + 4 && (char)i16[1] == 32; i16 -= 1)
                                        {
                                            *((char *)&i16[1]) = 0;
                                        }
                                        if (i16 == (char *)&v23 + 4)
                                            break;
                                        v2 = v109;
                                        v113 = *((unsigned int *)&v29);
                                        if ((*((unsigned int *)((void*)&v23 + 4)) == 1768713313 || *((unsigned int *)((void*)&v23 + 4)) == 1768713281) && v24 == 29541)
                                        {
                                            v114 = sub_10039a52(*((int *)v113), (int)v113[2], (int)v113[4]);
                                            if (v114)
                                            {
                                                v1 = v25;
                                                g_10080bb3 = v25;
                                                if (g_100fa4ef && (!g_10080bbb || g_10080baf == v114))
                                                {
                                                    v1 = v25;
                                                    g_10080bbf = v25;
                                                    g_10080bc3 = 8;
                                                    g_10080baf = v114;
                                                    g_10080bbb = 28;
                                                }
                                                g_10080bb7 = 30;
                                            }
                                        }
                                        else
                                        {
                                            v115 = sub_100399f0(*((int *)v113), (int)v113[2], (int)v113[4], (char *)&v23 + 4);
                                            if (v115)
                                            {
                                                v116 = v23;
                                                if (v116 <= g_10080bc7 || !g_10080bb7)
                                                {
                                                    v0 = v25;
                                                    g_10080bb3 = v0;
                                                    g_10080bc7 = v116;
                                                    g_10080bb7 = 30;
                                                    if (g_100fa4ef)
                                                    {
                                                        v0 = v25;
                                                        g_10080bbf = v0;
                                                        g_10080bc3 = 8;
                                                        g_10080baf = v115;
                                                        g_10080bbb = 28;
                                                        g_10080bc7 = g_10080bc7;
                                                    }
                                                }
                                            }
                                        }
                                        v117 = v3;
                                        if (!*(v117))
                                            break;
                                        v109 = v117;
                                        if (g_101d5e6c)
                                        {
                                            v118 = sub_100399af((char *)&v23 + 4, v117);
                                            v2 = v109;
                                            if (v118 && !((v2 = v118, !sub_1003c23e(v2))))
                                            {
                                                break;
                                            }
                                            else
                                            {
                                                v3 = v117;
                                                v109 = v2;
                                            }
                                        }
                                        *((unsigned int *)&v23) = (unsigned int)v23 + 1;
                                    }
                                }
                            }
                        }
LABEL_10027887:
                        v120 = *((unsigned int *)&v29);
                        v121 = (short)v120[5];
                        v122 = (short)v120[7];
                        v123 = (char)v120[9];
                        for (i4 = 0x63fef8; i4 < 0x64a308; i4 = &i4[1].padding_0[23])
                        {
                            if (i4->field_90 && v121 == i4->field_24 && v122 == i4->field_28 && v123 == i4->field_2c)
                            {
                                v125 = sub_10023861();
                                v121 = g_10077174;
                                if (g_10077174 < 20)
                                    *((char *)(g_10077174 + v125 + 112)) = *((char *)(g_10077174 + v125 + 112)) + 1;
                            }
                        }
                    }
                    if (g_101dfea3)
                    {
                        v126 = *((unsigned int *)&v29);
                        if (*((short *)v126) == (unsigned short)g_1005f854 && (short)v126[2] == (unsigned short)g_1005f858 && (char)v126[4] == (char)*((int *)&g_1005f85c) && g_101dfe94 - g_100f0ddc >= 5)
                        {
                            v127 = sub_1003997e(*(0x63fe64));
                            if (v127 && v127->field_88)
                                g_100f9320 = v127;
                        }
                    }
                    v128 = *((unsigned int *)&v29);
                    v129 = 0x63fef8;
                    v130 = NULL;
                    while (true)
                    {
                        if (v129 < 0x64a308)
                        {
                            if (v129->field_90 && *((short *)v128) == *((int *)&v129->padding_0[36]) && (short)v128[2] == *((int *)&v129->padding_0[40]) && (char)v128[4] == *((int *)&v129->padding_0[44]))
                            {
                                if (v130)
                                    break;
                                v130 = v129;
                            }
                            v129 = &v129[1].padding_0[23];
                        }
                        else
                        {
                            if (v130)
                            {
                                idx = sub_10023861();
                                idx[142] = 20;
                                idx[143] = 20;
                                break;
                            }
                        }
                    }
                }
                else if (v56 == 0xa2)
                {
                    g_1005f7db = (char)index[1] & 32;
                    g_1005f7e0 = (char)index[1] & 64;
                    g_1005f7dd = *((char *)index) & 32;
                    g_1005f7dc = *((char *)index) & 64;
                    v132 = *((char *)index) & 1;
                    v133 = v132;
                    if (!(*((char *)index) & 1) || (v133 = v132, v132 && !((v133 = v133, g_1005f7de))))
                        g_1005f7e1 = 0;
                    g_1005f7de = v133;
                    g_1005f7df = *((char *)index) & 8;
                    g_1005f7d9 = (*((char *)index) & 16) >> 4;
                    g_1005f7da = (*((char *)index) & 128) >> 7;
                }
                else if (v56 == 0xaa)
                {
                    v14 = 0xaa;
                    v13 = g_1005dc44;
                    v12 = index;
                    v11 = 7968948;
                    v10 = &/* unsupported instruction */;
                    v9 = &v29 + 8;
                    v8 = v55;
                    v7 = v141;
                    sub_10026702();
                    g_100f49d5 = g_100f49d9;
                    g_100f49e5 = g_100f49d9 * 316 + g_100f49ed;
                    sub_1002ae81(g_100f49e5, 316);
                    lstrcpy(g_100f49e5, &v27 - 8);
                    v134 = (short)index[4] + index + 4 + 2;
                    *((char [2])&g_100f49e5[292]) = v134->padding_0;
                    v135 = &v134->field_2;
                    v136 = v135->padding_0[0];
                    v137 = &v135->padding_0[1];
                    *((char *)&g_100f49e5[294]) = v136;
                    v4 = v136;
                    v3 = &v135->padding_0[1];
                    v23 = 0;
                    if ((char)v4 == 1 || (char)v4 == 2 || (char)v4 == 3 || (char)v4 == 5 || (char)v4 == 19 || (char)v4 == 20)
                    {
                        *((unsigned int *)&g_100f49e5[304]) = (unsigned int)v137->padding_0;
                        *((unsigned int *)&g_100f49e5[308]) = v137->field_2;
                        *((unsigned int *)&g_100f49e5[312]) = v137->field_4;
                        sub_10026702();
                        v23 = 1;
                    }
                    else
                    {
                        if ((char)v4 == 7 || (char)v4 == 8 || (char)v4 == 13 || (char)v4 == 15 || (char)v4 == 0x11)
                        {
                            *((unsigned int *)&g_100f49e5[296]) = (unsigned int)v137->padding_0;
                            sub_10026702();
                            v23 = 1;
                        }
                        else
                        {
                            if ((char)v4 != 9 && (char)v4 != 10 && (char)v4 != 11 && ((char)v4 == 6 || (char)v4 == 12 || (char)v4 == 14))
                            {
                                sub_10026702();
                                v23 = 1;
                            }
                        }
                    }
                    if (v23)
                    {
                        g_100f49d9 = g_100f49d9 + 1;
                        if (g_100f49d9 >= 2000)
                            g_100f49d9 = 0;
                        sub_10026724();
                    }
                    v138 = v4;
                    if (v138 == 1)
                    {
                        if (lstrcmp(&v27 - 8, &g_1005f7b1))
                        {
                            sub_10026702();
                            if (!268592817())
                            {
                                sub_100093a3(3);
                                g_1005f561 = 20;
                            }
                        }
                        else
                        {
                            sub_10026702();
                            if (268592817())
                            {
                                g_1008b8ec = 330;
                            }
                            else
                            {
                                if (268592817())
                                {
                                    g_1008b8ec = 210;
                                }
                                else
                                {
                                    if (268592817())
                                    {
                                        g_1008b8dc = 2020;
                                    }
                                    else
                                    {
                                        if (268592817())
                                        {
                                            g_1008b8e0 = 2000;
                                        }
                                        else
                                        {
                                            if (268592817())
                                            {
                                                g_1008b8ec = 50;
                                            }
                                            else
                                            {
                                                if (268592817())
                                                {
                                                    g_1008b8ec = 100;
                                                }
                                                else
                                                {
                                                    if (268592817())
                                                    {
                                                        g_1008b8f0 = 100;
                                                    }
                                                    else
                                                    {
                                                        if (268592817())
                                                        {
                                                            g_1008b8f0 = 100;
                                                        }
                                                        else
                                                        {
                                                            if (268592817())
                                                                g_1008b8f0 = 100;
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                    else
                    {
                        if (v138 == 6)
                        {
                            sub_100093a3(4);
                            g_1005f565 = 20;
                        }
                        else
                        {
                            if (v138 == 11 || v138 == 12 || v138 == 13 || v138 == 16)
                            {
                                if (g_10207f15)
                                    sub_10009489(1);
                                g_100f49c9 = 20;
                            }
                        }
                    }
                }
                else if (v56 == 0xb4)
                {
                    v139 = *((char *)index);
                    if ((char)v139 == 21)
                    {
                        v23 = 4294967293;
                    }
                    else
                    {
                        if ((char)v139 == 23 || (char)v139 == 24 || (char)v139 == 26)
                        {
                            v23 = 4294967295;
                        }
                        else
                        {
                            if ((char)v139 != 25)
                                goto LABEL_10027e94;
                            v23 = 4294967294;
                        }
                    }
                    v14 = index;
                    v57 = index + 1;
                    g_100f49d5 = g_100f49d9;
                    v12 = g_100f49d9 * 316 + g_100f49ed;
                    g_100f49d9 = g_100f49d9 + 1;
                    v140 = g_100f49d9;
                    if (g_100f49d9 >= 2000)
                        g_100f49d9 = 0;
                    g_100f49e5 = v12;
                    sub_1002ae81(v12, 316);
                    *((unsigned short *)&g_100f49e5[294]) = v23;
                    sub_10026702();
                    v56 = g_100f49e5;
                    v55 = g_100f49e5 + 32;
                    v141 = "Server is saving game in ";
                    v139 = 25;
                    do
                    {
                        if (false)
                            break;
                    } while (*((char *)v55) == g_100584ac);
                    if (v140 == 2000)
                    {
                        v142 = *((char *)v55);
                        if (*((char *)v55) == 111)
                            v142 = 49;
                        v11 = _INSERT(v142, 0, v142 - 48);
                        g_100f4a01 = v11 * 60000;
                        g_100f9324 = (unsigned short)sub_10040a30(2400, v11) + 7800;
                        v139 = 600;
                        v56 = 2400 * 600;
                        g_100f9324 = g_100f9324 + *((unsigned short *)&v56);
                    }
                    index = v11;
LABEL_10027e94:
                    if (*((char *)index) == 26)
                    {
                        v143 = (short)index[1];
                        if (v143 != 24)
                        {
                            if (v143 == 50)
                            {
                                if (g_100fa97b && (int)index[3] == 1936287828 && (int)index[7] == 1952669984)
                                    g_1009a52e = 5;
                            }
                            else
                            {
                                if (v143 == 23)
                                {
                                    if ((int)index[3] == 544567129 && (int)index[7] == 1852727651)
                                        g_1009a532 = 5;
                                }
                                else
                                {
                                    if (v143 == 13)
                                    {
                                        if ((int)index[3] == 544567129 && (int)index[7] == 543519329)
                                        {
                                            g_100f0dd0 = 10;
                                            g_100f0dd4 = 600;
                                        }
                                    }
                                    else
                                    {
                                        if (v143 == 22)
                                        {
                                            if ((int)index[3] == 544567129 && (int)index[7] == 543519329)
                                            {
                                                g_100f0dcc = 0;
                                                g_100f0dd0 = 0;
                                            }
                                        }
                                        else
                                        {
                                            if (v143 == 46)
                                            {
                                                if ((int)index[3] == 544567129 && (int)index[7] == 1852727651)
                                                    g_100f49f5 = 1;
                                            }
                                            else
                                            {
                                                if (v143 == 42)
                                                {
                                                    if ((int)index[3] == 1936287828 && (int)index[7] == 1784835872)
                                                    {
                                                        g_100f0dcc = 0;
                                                        g_100f0dd0 = 0;
                                                        g_100f49f9 = 1;
                                                        g_100f49f5 = 1;
                                                    }
                                                }
                                                else
                                                {
                                                    if (v143 == 31 && (int)index[3] == 544567129 && (int)index[7] == 544825709 && sub_1003997e(g_1008b89b))
                                                        *((char *)(sub_10023861() + 138)) = 1;
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                    else
                    {
                        if (*((char *)index) == 24)
                        {
                            if ((int)index[3] == 544567129 && (int)index[7] == 1702063980)
                            {
                                v144 = index + 12;
                                if (*((char *)v144) != 32)
                                {
                                    v28 = *((char *)v144);
                                    return sub_1002807f();
                                }
                                v28 = (int)_INSERT(*((uint80_t *)&v27), 0, 0);
                                v145 = sub_10040900(&v28, v144);
                                v146 = &v28;
                                g_1008b8a8 = g_1008b8a8 + v145;
                                for (i5 = 0; i5 < 36; i5 += 1)
                                {
                                    if (v146->field_0 == 544825888)
                                    {
                                        if (v146->field_4 >= 65 && v146->field_4 <= 90)
                                        {
                                            v148 = &v146->field_4;
                                            for (iter = 0; *(iter + (char *)v148) != 46 && iter < 63; iter += 1)
                                            {
                                                *(iter + (char *)&g_1005f56d) = *(iter + (char *)v148);
                                            }
                                            *(iter + (char *)&g_1005f56d) = 0;
                                            g_1005f569 = 20;
                                            sub_100093a3(2);
                                            g_1005f5f5 = GetTickCount();
                                            lstrcpy(&g_1005f5ad, &g_1005f56d);
                                            break;
                                        }
                                        else
                                        {
                                            v150 = &v146->field_6;
                                            if ((char)v150->field_0 == 32)
                                                v150 = (char *)&v150->field_0 + 1;
                                            for (iter1 = 0; *(iter1 + (char *)v150) != 46 && iter1 < 63; iter1 += 1)
                                            {
                                                *(iter1 + (char *)&g_1005f5ad) = *(iter1 + (char *)v150);
                                            }
                                            *(iter1 + (char *)&g_1005f5ad) = 0;
                                            g_1005f5f5 = GetTickCount();
                                            break;
                                        }
                                    }
                                    else
                                    {
                                        if (v146->field_4 == 46)
                                        {
                                            g_1005f5f5 = GetTickCount();
                                            g_1005f5ad = 0;
                                            break;
                                        }
                                        else
                                        {
                                            v146 = (char *)&v146->field_0 + 1;
                                        }
                                    }
                                }
                            }
                        }
                        else
                        {
                            *((unsigned int *)&(&v29)[4]) = 0;
                            v152 = _INSERT(v139, 0, *((char *)index));
                            if (*((char *)index) == 25 || (char)v10 == 23)
                            {
                                v11 = v56;
                                v10 = v152;
                                v9 = index;
                                v8 = v57;
                                v7 = &v12;
                                v6 = &v29 + 8;
                                v5 = v55;
                                v4 = v141;
                                if ((int)index[3] == 1852404565)
                                {
                                    if ((int)index[7] == 1752440935)
                                    {
                                        g_100f0e7c = 1;
                                        sub_10028970();
                                    }
                                    else
                                    {
                                        if ((int)index[7] == 1852776551)
                                        {
                                            v153 = index + 16;
                                            iter2 = &v27 - 8;
                                            i6 = (short)index[1] - 18;
                                            if (*((char *)v153) >= 48 && *((char *)v153) <= 57)
                                            {
                                                for (v156 = 0; *((char *)v153) != 32 && v156 < 32; i6 -= 1)
                                                {
                                                    *(iter2) = *((char *)v153);
                                                    iter2 += 1;
                                                    v153 += 1;
                                                    v156 += 1;
                                                }
                                                *(iter2) = 0;
                                                g_100f0e7c = sub_10040900(&v27 - 8, i6, v153);
                                                sub_10028970(v153);
                                            }
                                        }
                                    }
                                }
                                index = v57;
                                v32 = v55;
                            }
                            if (*((char *)index) == 25)
                            {
                                v157 = (short)index[1];
                                v158 = index + 3;
                                if (!*((char *)v158))
                                    *((char *)v158) = 89;
                                *((void* *)&v32[8]) = v158;
                                *((unsigned int *)&v32[316]) = v157;
                                do
                                {
                                    if (false)
                                        break;
                                } while (g_10043846 == *((char *)v158));
                                if (false)
                                {
                                    *((unsigned int *)&v32[4]) = 1;
                                    i7 = *((char *)v158);
                                    if (*((char *)v158) >= 65 && i7 <= 90)
                                    {
                                        v160 = v32 - 308;
                                        for (v161 = 0; i7 != 40 && i7 != 46; i7 = *((char *)v158))
                                        {
                                            *((char *)v160) = i7;
                                            v160 += 1;
                                            v158 += 1;
                                            v161 += 1;
                                        }
                                        if (i7 != 46)
                                        {
                                            *((char *)&v160[1]) = 0;
                                            v10 = v158;
                                            v162 = &g_10077175;
                                            while (true)
                                            {
                                                if (v162 >= &g_100809cd)
                                                    goto LABEL_10028963;
                                                v163 = *(v162);
                                                if (*(v162))
                                                    goto LABEL_10028290;
LABEL_10028290:
                                                v164 = v32 - 308;
                                                v165 = v161;
                                                v166 = v162;
                                                do
                                                {
                                                    if (!v165)
                                                        break;
                                                } while (*(v166) == *((char *)v164));
                                                if (!v163)
                                                    break;
                                                v162 += 156;
                                            }
                                            v167 = v158 + 7;
                                            v168 = v32 - 308;
                                            for (i8 = *((char *)v167); i8 != 41; i8 = *((char *)v167))
                                            {
                                                *((char *)v168) = i8;
                                                v168 += 1;
                                                v167 += 1;
                                            }
                                            *((char *)v168) = 0;
                                            idx1 = v32 - 308;
                                            *((unsigned int *)&idx1[72]) = sub_10040900(v32 - 308, v162);
                                            v171 = v167 + 3;
                                            if (*((char *)v171) == 83)
                                                v171 += 1;
                                            i9 = v171 + 3;
                                            if (*((short *)i9) == 24936)
                                            {
                                                *((char *)&idx1[76]) = 0;
                                            }
                                            else
                                            {
                                                if (*((short *)i9) == 29545)
                                                {
                                                    v172 = i9 + 5;
                                                    if (*((char *)v172) == 32)
                                                        v172 += 1;
                                                    i9 = v172;
                                                    do
                                                    {
                                                        if (false)
                                                            break;
                                                    } while (g_1004384e == *((char *)i9));
                                                    if (false)
                                                    {
                                                        *((char *)&idx1[76]) = 1;
                                                    }
                                                    else
                                                    {
                                                        i9 = i9;
                                                        do
                                                        {
                                                            if (false)
                                                                break;
                                                        } while (g_10043854 == *((char *)i9));
                                                        if (false)
                                                        {
                                                            *((char *)&idx1[76]) = 2;
                                                        }
                                                        else
                                                        {
                                                            i9 = i9;
                                                            do
                                                            {
                                                                if (false)
                                                                    break;
                                                            } while (g_1004385b == *((char *)i9));
                                                            if (false)
                                                            {
                                                                *((char *)&idx1[76]) = 3;
                                                            }
                                                            else
                                                            {
                                                                i9 = i9;
                                                                do
                                                                {
                                                                    if (false)
                                                                        break;
                                                                } while (g_10043863 == *((char *)i9));
                                                                if (false)
                                                                {
                                                                    *((char *)&idx1[76]) = 4;
                                                                }
                                                                else
                                                                {
                                                                    i9 = i9;
                                                                    do
                                                                    {
                                                                        if (false)
                                                                            break;
                                                                    } while (g_10043868 == *((char *)i9));
                                                                    if (false)
                                                                    {
                                                                        *((char *)&idx1[76]) = 5;
                                                                    }
                                                                    else
                                                                    {
                                                                        i9 = i9;
                                                                        do
                                                                        {
                                                                            if (false)
                                                                                break;
                                                                        } while (g_10043874 == *((char *)i9));
                                                                        if (false)
                                                                        {
                                                                            *((char *)&idx1[76]) = 6;
                                                                        }
                                                                        else
                                                                        {
                                                                            i9 = i9;
                                                                            do
                                                                            {
                                                                                if (false)
                                                                                    break;
                                                                            } while (g_10043881 == *((char *)i9));
                                                                            if (false)
                                                                            {
                                                                                *((char *)&idx1[76]) = 7;
                                                                            }
                                                                            else
                                                                            {
                                                                                do
                                                                                {
                                                                                    if (false)
                                                                                        break;
                                                                                } while (g_10043890 == *((char *)i9));
                                                                                if (false)
                                                                                    *((char *)&idx1[76]) = 8;
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                            for (; *((char *)i9) != 46; i9 += 1);
                                            i10 = i9 + 2;
                                            v175 = idx1 + 32;
                                            while (i10 < (int)v32[8] + (int)v32[316])
                                            {
                                                if (*((int *)i10) == 1948280431)
                                                {
                                                    if ((short)i10[4] == 25960)
                                                    {
                                                        v176 = i10 + 7;
                                                        v177 = 0;
                                                        for (i19 = *((char *)v176); i19 != 40 && i19 != 46 && v177 < 31; i19 = *((char *)v176))
                                                        {
                                                            *((char *)v175) = i19;
                                                            v175 += 1;
                                                            v176 += 1;
                                                            v177 += 1;
                                                        }
                                                        if (v177 && i19 == 40)
                                                            v175 -= 1;
                                                        break;
                                                    }
                                                    else
                                                    {
                                                        i10 += 1;
                                                    }
                                                }
                                                else
                                                {
                                                    i10 += 1;
                                                }
                                            }
                                            *((char *)&idx1[78]) = 1;
                                            *((char *)&idx1[80]) = 0;
                                            *((char *)&idx1[77]) = 0;
                                            *((char *)v175) = 0;
                                        }
                                    }
                                    else
                                    {
                                        if (*((int *)v158) == 1634738273 && (int)v158[4] == 1864397417 && (int)v158[8] == 1869815910 && (int)v158[12] == 1646294118)
                                        {
                                            v179 = v158 + 41;
                                            if ((char)v158[21] == 40)
                                                v179 = v158 + 63;
                                            v180 = v32 - 308;
                                            for (i11 = 0; *((char *)v179) != 32 && i11 < 32; i11 += 1)
                                            {
                                                *((char *)v180) = *((char *)v179);
                                                v180 += 1;
                                                v179 += 1;
                                            }
                                            *((char *)v180) = 0;
                                            g_100f49fd = sub_10040900(v32 - 308) * 60000;
                                        }
                                    }
                                }
                                else
                                {
                                    sub_100289ee();
                                }
                            }
                            if (!(int)v32[4])
                                g_10080b6e = 50;
                            if ((int)v32[4] && !g_10080b6e && g_100f94c8)
                            {
                                *((char *)(int)v32[8]) = 0;
                                g_799cfd = 0;
                                *((unsigned int *)&g_100f49e5[300]) = 1;
                            }
                            else
                            {
                                g_799cfd = 1;
                            }
                        }
                    }
                }
                else if (v56 >= 0x64 && v56 <= 0x68)
                {
                    if (g_1008b723)
                    {
                        count = GetTickCount();
                        g_1008b727 = count - g_1008b723;
                        g_1008b723 = 0;
                    }
                }
                else
                {
                    if (v56 == 0x83)
                    {
                        g_10080be7 = (char)index[5];
                        if (g_10080be7 == 13)
                        {
                            if (g_10080bdf == 0x8c)
                            {
                                v183 = sub_1003997e(g_10080be3, index);
                                index = g_10080be3;
                                v184 = v183;
                                if (!v184 || *((int *)(v184 + 36)) == *((short *)g_10080be3) && *((int *)(v184 + 40)) == (short)g_10080be3[2] && *((int *)(v184 + 44)) == (char)g_10080be3[4])
                                {
                                    g_10080beb = 0;
                                    goto LABEL_1002861a;
                                }
                            }
                            v185 = (short)index[2];
                            v186 = (char)index[4];
                            g_10080beb = *((short *)index);
                            g_10080bef = v185;
                            g_10080bf3 = v186;
                            v187 = 0x63fef8;
                            while (true)
                            {
                                if (v187 < 0x64a308)
                                {
                                    if (v187->field_90 && g_10080beb == *((int *)&v187->padding_0[36]) && g_10080bef == *((int *)&v187->padding_0[40]) && g_10080bf3 == *((int *)&v187->padding_0[44]))
                                        break;
                                    v187 = &v187[1].padding_0[23];
                                }
                                else
                                {
                                    for (i20 = &g_1005e5a0.field_0; i20 < &g_1005e6a0.field_0; i20 = (char *)&i20[1].field_6 + 1)
                                    {
                                        if (!i20->field_6)
                                        {
                                            i20->field_0 = g_10080beb;
                                            i20->field_2 = g_10080bef;
                                            i20->field_5 = g_10080bf3;
                                            i20->field_6 = 20;
                                            i20->field_8 = 3;
                                            break;
                                        }
                                    }
                                }
                            }
                        }
LABEL_1002861a:
                        if (g_101dfea3 && g_101dfe94 - g_100f0ddc >= 5)
                        {
                            v189 = sub_1003997e(*(0x63fe64));
                            if (v189 && v189->field_88 && g_1005f854 - *((int *)&v189->padding_0[36]) + 1 <= 2 && g_1005f858 - *((int *)&v189->padding_0[40]) + 1 <= 2 && *((int *)&g_1005f85c) == *((int *)&v189->padding_0[44]))
                            {
                                v190 = *((unsigned int *)&v29);
                                if (((char)v190[5] == 1 || (char)v190[5] == 3 || (char)v190[5] == 4 || (char)v190[5] == 10 || (char)v190[5] == 0x11 || (char)v190[5] == 21) && *((short *)v190) == *((int *)&v189->padding_0[36]) && (short)v190[2] == *((int *)&v189->padding_0[40]) && (char)v190[4] == *((int *)&v189->padding_0[44]))
                                    g_100f9320 = v189;
                            }
                        }
                    }
                    else if (v56 == 0x8f)
                    {
                        if ((short)index[4] < 200)
                        {
                            v192 = sub_1003997e(*((int *)index));
                            if (v192)
                            {
                                v23 = v192;
                                v193 = v23;
                                if (!sub_1003a494(&v23[1]) || g_1014f40d && !v193[37] && v193[40] != 2)
                                {
                                    v193 = v23;
                                    if (!sub_1003a550(&v23[1]) || g_1014f40e && !v193[37] && v193[40] != 2)
                                        goto LABEL_10028788;
                                }
                                g_10080bcb = v193;
                                g_10080bcf = 65;
                                if (g_100fa4ef)
                                {
                                    g_10080bd3 = v193;
                                    g_10080bd7 = 6;
                                }
                            }
LABEL_10028788:
                        }
                    }
                    else
                    {
                        if (v56 == 0x8c)
                        {
                            g_10080be3 = *((int *)index);
                            if ((char)index[4])
                            {
                                v194 = sub_1003997e(*((int *)index), (char)index[4]);
                                if (v194)
                                {
                                    v195 = *((int *)index) - v194->field_88;
                                    if (v195 > 1 && v195 < 101)
                                    {
                                        i12 = &g_1005e1a0.field_0;
                                        for (idx2 = v194; i12 < &g_1005e5a0.field_0; i12 = (char *)&i12[1].field_6 + 1)
                                        {
                                            if (!i12->field_6)
                                            {
                                                i12->field_0 = idx2->field_24;
                                                i12->field_2 = idx2->field_28;
                                                i12->field_5 = idx2->field_2c;
                                                i12->field_6 = 20;
                                                *((unsigned int *)((char *)&i12[1].field_2 + 1)) = v195;
                                                i12->padding_4[0] = 0;
                                                i12->field_8 = 2;
                                                break;
                                            }
                                        }
                                    }
                                    else
                                    {
                                        if (v195 > 0x64)
                                        {
                                            v198 = (unsigned long long)(struct struct_4 *)&v194[46809].padding_2d[31] / 168;
                                            for (i13 = 0; i13 < 0xa; i13 += 1)
                                            {
                                                *((unsigned short *)&(&g_10077175)[92 + 156 * v198 + 2 * i13]) = *((short *)&(&g_10077175)[92 + 156 * v198 + 2 * i13]) + (unsigned short)(~(v195) + 1);
                                            }
                                        }
                                    }
                                }
                            }
                            else
                            {
                                if ((char)index[3] == 64)
                                {
                                    if (g_10207f33 || g_10207f34)
                                    {
                                        v200 = sub_1003997e(*((int *)index), *((int *)index));
                                        if (v200)
                                        {
                                            v13 = *((int *)index);
                                            v12 = v200;
                                            v201 = sub_10012827(v12, 0, 1);
                                            if (v201 && v201->field_20 && *((int *)(v12 + 44)) == *((int *)&g_1005f85c))
                                            {
                                                g_100f0e38 = *((int *)index);
                                                g_100f0e3c = 20;
                                            }
                                        }
                                    }
                                }
                                else
                                {
                                    if (sub_1003997e(*((int *)index)))
                                    {
                                        v22 = 4294967295;
                                        v23 = 0x2329;
                                        i14 = 0;
                                        while (i14 < 0xa)
                                        {
                                            if (!g_1008b945[i14])
                                            {
                                                v22 = i14;
                                                break;
                                            }
                                            else
                                            {
                                                v13 = i14;
                                                v12 = v202;
                                                if (!lstrcmp(&(&g_1008b96d)[32 * i14], v202 + 4))
                                                {
                                                    v22 = i14;
                                                    break;
                                                }
                                                else
                                                {
                                                    v204 = i14;
                                                    if (g_1008b945[v204] < v23)
                                                    {
                                                        v23 = g_1008b945[v204];
                                                        v22 = v204;
                                                        i14 = v204 + 1;
                                                    }
                                                    else
                                                    {
                                                        i14 = v204 + 1;
                                                    }
                                                }
                                            }
                                        }
                                        if (v22 != 0xffffffff)
                                        {
                                            g_1008b945[v22] = 9000;
                                            lstrcpy(&(&g_1008b96d)[32 * v22], v202 + 4);
                                        }
                                    }
                                }
                            }
                        }
                        else if (v56 == 0xffffffff)
                        {
                            sub_10029b3b();
                        }
                    }
                }
            }
        }
    }
LABEL_10028963:
    v205 = _ccall(v33, v34, (unsigned int)v35, 0);
    *((void* *)v205) = v45;
    return v17;
}
```

## `sub_10027176` `0x10027176`

_462 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    int field_0;
    unsigned int field_4;
    struct struct_0 *field_8;
} struct_0;

typedef struct struct_1 {
    char padding_0[32];
    char field_20;
} struct_1;

typedef struct struct_2 {
    unsigned short field_0;
    unsigned short field_2;
    char field_4;
} struct_2;

extern unsigned short g_100434c9;
extern unsigned short g_100434cb;
extern char g_100434cd;
extern unsigned short g_100434ce;
extern char g_100434d1;
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern char g_1005f85c;
extern unsigned int g_100f0dcc;
extern unsigned int g_100f0dd0;
extern unsigned int g_100f0e38;
extern unsigned int g_100f0e3c;
extern char g_10207f33;
extern char g_10207f34;

int sub_10027176(unsigned int a0, unsigned short *a1)
{
    struct_0 *v4;  // eax
    int i;  // ecx
    struct_2 *v14;  // edx
    unsigned int v15;  // eax
    unsigned int v16;  // ebx
    unsigned int v17;  // ecx
    struct_2 *v18;  // edx
    struct_0 *v6;  // esi
    struct_0 *v7;  // esi
    unsigned int v8[35];  // eax
    struct_1 *v11;  // eax
    struct_2 *v12;  // edx
    int v13;  // eax
    unsigned int v0[35];  // [bp-0x24]
    unsigned int v2;  // [bp+0xffe70]
    struct_2 *v3;  // [bp+0xffffc]

    if (a0 != *((int *)&g_1005f85c))
        goto LABEL_0x10028963;
    if (!g_10207f33)
        if (!g_10207f34)
            goto LABEL_0x10028963;
        else
            goto LABEL_10027198;
LABEL_10027198:
    v4 = sub_1003a03f(*(a1), a1[1], a0);
    if (v4)
    {
        do
        {
            i = 0;
            for (v6 = &v4->field_4; i < v4->field_0; i += 1)
            {
                v7 = v6;
                if (v7->field_0 == 99)
                {
                    v8 = sub_1003997e(v6->field_4, v6, v4, i);
                    if (v8 && !v8[0x22])
                    {
                        v2 = 1;
                        v0 = v8;
                        v11 = sub_10012827(v8, 0, 1);
                        if (v11 && v11->field_20)
                        {
                            if (v8[0] == g_100f0e38)
                            {
                                g_100f0e38 = 0;
                                g_100f0e3c = 0;
                            }
                            v12 = v3;
                            v13 = sub_1003a065(v12->field_0, v12->field_2, v12->field_4);
                            if (v13 && ((unsigned short)sub_1003c4fa(v13, v13) & 8272) == 8272)
                            {
                                g_100434ce = v13;
                                v14 = v3;
                                v15 = v14->field_0;
                                v16 = v14->field_2;
                                v17 = v14->field_4;
                                g_100434c9 = v15;
                                g_100434cb = v16;
                                g_100434cd = v17;
                                if (v15 - g_1005f854 + 1 <= 2 && v16 - g_1005f858 + 1 <= 2 && v17 == *((int *)&g_1005f85c) && g_10207f34)
                                {
                                    g_100434d1 = sub_10038d20();
                                    sub_1002ade7("\n", 12);
                                    g_100f0dcc = 15;
                                    g_100f0dd0 = 4294967295;
                                }
                                else if (g_10207f33)
                                {
                                    sub_100265d3(v14->field_0, v14->field_2, v17);
                                }
                            }
                        }
                        break;
                    }
                    else
                    {
                        i = v4;
                        v4 = v6;
                        v7 = v6->field_4;
                    }
                }
                v6 = v7 + 1;
            }
        } while (!v2 && (v2 = 1, v18 = v3, v4 = (struct_0 *)sub_10039fc8((unsigned int)v18->field_0, (unsigned int)v18->field_2, (unsigned int)v18->field_4), v4));
    }
}
```

## `sub_1002757b` `0x1002757b`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002757b(void)
{
}
```

## `sub_10027708` `0x10027708`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10027708(void)
{
}
```

## `sub_10027da9` `0x10027da9`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10027da9(void)
{
}
```

## `sub_10027dc9` `0x10027dc9`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10027dc9(void)
{
}
```

## `sub_1002807a` `0x1002807a`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002807a(unsigned int a0)
{
    sub_1002807f();
    return;
}
```

## `sub_1002807f` `0x1002807f`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1002807f(unsigned int a0)
{
}
```

## `sub_10028106` `0x10028106`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10028106(void)
{
}
```

## `sub_1002842e` `0x1002842e`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002842e(void)
{
}
```

## `sub_100288e6` `0x100288e6`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100288e6(void)
{
}
```

## `sub_10028970` `0x10028970`

_124 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
    char padding_1[31];
    unsigned int field_20;
    unsigned int field_24;
} struct_0;

extern struct_0 g_100ec0b6;

int sub_10028970(void)
{
    unsigned int i;  // ecx
    unsigned int v6;  // eax
    unsigned int v7;  // edx
    struct_0 *iter;  // ebx
    unsigned int v9;  // ecx
    unsigned int v10;  // edi
    unsigned int v0;  // [bp-0x50]
    unsigned int v1;  // [bp-0x4c]
    unsigned int v2;  // [bp-0x48]
    unsigned short v3;  // [bp-0x44]

    for (i = 0; i < v6 && i < 63; i += 1)
    {
        *(i + (char *)&v3) = *((char *)(i + v7));
    }
    *(i + (char *)&v3) = 0;
    iter = &g_100ec0b6.field_0;
    for (v9 = 0; v9 < 0x100; iter += 1)
    {
        if (!iter->field_0)
        {
            iter->field_24 = v10;
            lstrcpy(iter, &v3);
            iter->field_20 = GetTickCount();
            return;
        }
        v2 = v7;
        v1 = v10;
        v0 = v9;
        v10 = v10;
        if (!lstrcmp(iter, &v3))
        {
            iter->field_24 = v10;
            iter->field_20 = GetTickCount();
            return;
        }
        v9 = v0 + 1;
    }
    return;
}
```

## `sub_100289bb` `0x100289bb`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100289bb(void)
{
}
```

## `sub_100289ee` `0x100289ee`

_749 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_10052768;
extern unsigned int g_1005276c;

unsigned int sub_100289ee(unsigned int a0, void* a1)
{
    unsigned int v9;  // ecx
    void* iter;  // edi
    unsigned long v19;  // 4127
    void* v20;  // edi
    unsigned int v21;  // eax
    unsigned int v22;  // eax
    unsigned int v23;  // ebx
    unsigned int v11;  // eax
    unsigned int v12;  // ecx
    unsigned int v13;  // ebx
    void* node;  // esi
    unsigned long v15;  // ldt
    unsigned long v16;  // gdt
    unsigned short v17;  // ss
    unsigned long v18;  // 4133
    int v0;  // [bp-0x64]
    int v1;  // [bp-0x60]
    unsigned int v2;  // [bp-0x5c]
    unsigned int v3;  // [bp-0x58]
    unsigned int v4;  // [bp-0x50]
    int v5;  // [bp-0x4c]
    unsigned int v6;  // [bp-0x48]
    char v7;  // [bp-0x44]

    v9 = (short)a1[2];
    iter = a1;
    while (true)
    {
        while (true)
        {
            v12 = v9;
            if (!v9)
                return v11;
            if (*((int *)iter) == 544434464)
                break;
            iter += 1;
            v9 = v12 - 1;
        }
        v13 = 0;
        for (node = a1; node < iter && v13 < 32; node += 1)
        {
            v18 = _ccall(v15, v16, (unsigned int)v17, &v7 + v13);
            *((char *)v18) = *((char *)node);
            v13 += 1;
        }
        if (v13 == 32)
            return v11;
        v19 = _ccall(v15, v16, (unsigned int)v17, &v7 + v13);
        *((char *)v19) = 0;
        v11 = (int)iter[4];
        if (v11 == 1851880563)
            return v11;
        if (v11 == 1948282740)
        {
            v6 = 1;
            v5 = 0;
            v20 = iter + 11;
            goto LABEL_10028b3d;
        }
        if (v11 == 2037540214)
        {
            v6 = 3;
            v5 = 0;
            v20 = iter + 20;
            goto LABEL_10028b3d;
        }
        if (v11 == 544366950)
        {
            v6 = 2;
            v5 = 0;
            v20 = iter + 15;
            goto LABEL_10028b3d;
        }
        else if (v11 == 1629515375)
        {
            v6 = 1;
            v21 = (int)iter[9];
            if (v21 == 1702326124)
            {
                v5 = -1;
                v20 = iter + 28;
            }
            else
            {
                if (v21 == 1751607656)
                {
                    v5 = 1;
                    v20 = iter + 29;
                }
                else
                {
                    return v21;
                }
            }
LABEL_10028b3d:
            v22 = *((int *)v20);
            v23 = (int)v20[4];
            if (v22 == 1953656686)
            {
                if (v23 == 1702309224)
                {
                    v4 = 7;
                    v3 = 4294967117;
                    v2 = 4294967117;
                    break;
                }
                else
                {
                    if (v23 == 1634020712)
                    {
                        v4 = 1;
                        v3 = 179;
                        v2 = 4294967117;
                        break;
                    }
                    else
                    {
                        v4 = 0;
                        v3 = 0;
                        v2 = 0xffffff00;
                        break;
                    }
                }
            }
            else
            {
                if (v22 == 1953853299)
                {
                    if (v23 == 1702309224)
                    {
                        v4 = 5;
                        v3 = 4294967117;
                        v2 = 179;
                        break;
                    }
                    else
                    {
                        if (v23 == 1634020712)
                        {
                            v4 = 3;
                            v3 = 179;
                            v2 = 179;
                            break;
                        }
                        else
                        {
                            v4 = 4;
                            v3 = 0;
                            v2 = 0x100;
                            break;
                        }
                    }
                }
                else
                {
                    if (v22 == 1953719671)
                    {
                        v4 = 6;
                        v3 = 0xffffff00;
                        v2 = 0;
                        break;
                    }
                    else
                    {
                        if (v22 == 1953718629)
                        {
                            v4 = 2;
                            v3 = 0x100;
                            v2 = 0;
                            break;
                        }
                        else
                        {
                            return v22;
                        }
                    }
                }
            }
        }
        else if (v11 == 1987011169)
        {
            v6 = 0;
            v5 = 1;
            v4 = 4294967295;
            break;
        }
        else if (v11 == 1869374818)
        {
            v6 = 0;
            v5 = -1;
            v4 = 4294967295;
            break;
        }
        else
        {
            iter += 1;
            v9 = v12 - 1;
        }
    }
    if (!v6)
    {
        v1 = 0;
        v0 = 0;
    }
    else if (v6 == 1)
    {
        v1 = v3 * 50 >> 8;
        v0 = v2 * 50 >> 8;
    }
    else if (v6 == 2)
    {
        v1 = v3 * 175 >> 8;
        v0 = v2 * 175 >> 8;
    }
    else if (v6 == 3)
    {
        v1 = v3 * 375 >> 8;
        v0 = v2 * 375 >> 8;
    }
    return sub_10029a61(1, &v7, &v7, g_10052768 + v1, g_1005276c + v0, v5, 0);
}
```

## `sub_10028a45` `0x10028a45`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10028a45(void)
{
}
```

## `sub_10028a67` `0x10028a67`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10028a67(void)
{
}
```

## `sub_10028a89` `0x10028a89`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10028a89(void)
{
}
```

## `sub_10028aab` `0x10028aab`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10028aab(void)
{
}
```

## `sub_10028aee` `0x10028aee`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10028aee(void)
{
}
```

## `sub_10028b11` `0x10028b11`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10028b11(void)
{
}
```

## `sub_10028b34` `0x10028b34`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10028b34(void)
{
}
```

## `sub_10028cf5` `0x10028cf5`

_23 bytes. (leaf/helper — see body)_

```c
extern char g_10044630;

unsigned int sub_10028cf5(void)
{
    unsigned int v1;  // eax
    char *iter;  // esi
    unsigned int v3;  // ecx

    v1 = 0;
    while (true)
    {
        v3 = *(iter);
        if (!v3)
            break;
        v1 += (&g_10044630)[v3] - 1;
        iter += 1;
    }
    return v1;
}
```

## `sub_10028d0c` `0x10028d0c`

_608 bytes. refs "+%d%c", "Invis"_

```c
typedef struct struct_1 {
    unsigned short field_0;
    unsigned short field_2;
    char field_4;
    char field_5;
    unsigned short field_6;
    char padding_8[4];
    unsigned int field_c;
} struct_1;

typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
    unsigned int field_18;
    unsigned int field_1c;
} struct_0;

typedef struct struct_2 {
    char padding_0[48];
    unsigned int field_30;
    unsigned int field_34;
} struct_2;

extern int g_100429fa;
extern struct_1 g_1005e1a0;
extern struct_1 g_1005e6a0;
extern struct_2 *g_1005f7ed;
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern unsigned int g_1005f85c;
extern struct_0 *g_10080b84;
extern unsigned int g_1008b8f4;
extern unsigned int g_1008b8f8;
extern unsigned int g_1008b8fc;
extern char g_1008b900;
extern unsigned int g_100ee8d0;
extern unsigned int g_100ee8d4;
extern char g_10135273;
extern char g_10135274;

unsigned int sub_10028d0c(void)
{
    unsigned int v12;  // eax
    unsigned int v13;  // eax
    struct_1 *i;  // esi
    struct_1 *v15;  // esi
    unsigned int v16;  // edi
    unsigned int v17;  // ecx
    unsigned int v18;  // edx
    unsigned int v19;  // edx
    unsigned int v0;  // [bp-0x64]
    unsigned int v1;  // [bp-0x60]
    unsigned int v2;  // [bp-0x4c]
    unsigned int v3;  // [bp-0x48]
    Byte v4[32];  // [bp-0x3c]
    struct_1 *v5;  // [bp-0x1c]
    unsigned int v6;  // [bp-0x18]
    unsigned int v7;  // [bp-0x14]
    int v8;  // [bp-0x10]
    unsigned int v9;  // [bp-0xc]
    unsigned int v10;  // [bp-0x8]

    if (!g_10135273 && !g_10135274)
        return v12;
    v10 = g_10080b84->field_1c;
    v13 = *((int *)&g_10080b84[1].padding_0[0]);
    v9 = v13;
    for (i = &g_1005e1a0.field_0; i < &g_1005e6a0.field_0; i = v15 + 1)
    {
        v15 = i;
        if (v15->field_6)
        {
            v5 = i;
            v6 = i->field_6;
            v16 = i->field_5 - g_1005f85c;
            v13 = (i->field_0 - g_1005f854 + 7 + v16) * 32;
            v17 = (i->field_2 - g_1005f858 + 5 + v16) * 32;
            v3 = g_1005f7ed->field_30 + g_100ee8d0;
            if (v3)
            {
                v18 = (!*((int *)0x63fee8) ? 32 : 0);
                v13 = (v3 < 0x100 ? v13 + 32 - v3 - v18 : v13 - (32 + v3) + v18);
            }
            v2 = g_1005f7ed->field_34 + g_100ee8d4;
            if (v2)
            {
                v19 = (!*((int *)0x63fee4) ? 32 : 0);
                v17 = (v2 < 0x100 ? v17 + 32 - v2 - v19 : v17 - (32 + v2) + v19);
            }
            if (v5->padding_8[0] == 2)
                v17 -= v5->field_4;
            if (v13 < 0x200 && v17 < 384)
            {
                v8 = (unsigned int)((v13 * v10 & 4294967295) / 480) + g_10080b84->field_14;
                v13 = (unsigned int)((v17 * v9 & 4294967295) / 352) + g_10080b84->field_18;
                v7 = v13;
                if (v5->padding_8[0] == 1 && g_10135273)
                {
                    g_1008b900 = 1;
                    g_1008b8f4 = 0xff;
                    g_1008b8f8 = 0xff;
                    g_1008b8fc = 100;
                    v13 = sub_1003b159(v8, v7, &g_100429fa, v6);
                }
                else if (v5->padding_8[0] == 2 && g_10135274)
                {
                    g_1008b8f4 = 155;
                    g_1008b8f8 = 218;
                    g_1008b8fc = 251;
                    v1 = 37;
                    v0 = v5->field_c;
                    wsprintfA(v4, "+%d%c");
                    v13 = sub_1003b127(v8, v7, v4);
                }
                else if (v5->padding_8[0] == 3)
                {
                    g_1008b8f4 = 179;
                    g_1008b8f8 = 176;
                    g_1008b8fc = 208;
                    v8 += 7;
                    v7 += 14;
                    v13 = sub_1003b127(v8, v7, "Invis");
                }
            }
            v15 = v5;
        }
    }
    g_1008b900 = 0;
    return v13;
}
```

## `sub_10028f6c` `0x10028f6c`

_164 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
    unsigned int field_18;
} struct_0;

extern unsigned int g_10052785[4];
extern struct_0 *g_10080b84;
extern unsigned int g_1008b8f4;
extern unsigned int g_1008b8f8;
extern unsigned int g_1008b8fc;

void sub_10028f6c(void)
{
    unsigned int v5;  // eax
    unsigned int v6;  // eax
    unsigned int i;  // [bp+0xffff4]
    unsigned int j;  // [bp+0xffff8]
    unsigned int v3;  // [bp+0xffffc]
    unsigned int v4;  // [bp+0x100000]

    g_1008b8f4 = 0xff;
    g_1008b8f8 = 0xff;
    g_1008b8fc = 0xff;
    for (i = 0; i < 14; i += 1)
    {
        for (j = 0; j < 18; j += 1)
        {
            sub_10040940(g_10052785[36 * i + 2 * j], /* unsupported instruction */ - 56);
            v5 = v4 / 15;
            v6 = v3 / 11;
            sub_1003b127(v5 * j - (v5 >> 1) + g_10080b84->field_14, v6 * i - (v6 >> 1) + g_10080b84->field_18, /* unsupported instruction */ - 56);
        }
    }
    return;
}
```

## `sub_10029010` `0x10029010`

_2365 bytes. refs "%c%d", "%s +%d", "%s %d"_

```c
typedef struct struct_4 {
    char padding_0[8];
    unsigned int field_8;
    char padding_c[32];
    unsigned short field_2c;
} struct_4;

typedef struct struct_5 {
    char padding_0[2];
    unsigned short field_2;
} struct_5;

typedef struct struct_1 {
    char field_0;
    char padding_1[1];
    unsigned short field_2;
    char padding_4[6];
    unsigned short field_a;
} struct_1;

typedef struct struct_3 {
    char field_0;
    char padding_1[1];
    unsigned short field_2;
    unsigned short field_4;
    unsigned short field_6;
    unsigned short field_8;
} struct_3;

typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
    unsigned int field_18;
    void* field_1c;
    unsigned int field_20;
} struct_0;

extern unsigned int g_10052768;
extern unsigned int g_1005276c;
extern unsigned int g_10052770;
extern char g_1005f537;
extern unsigned int g_1005f7ed;
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern unsigned int g_1005f85c;
extern struct_0 *g_10080b84;
extern unsigned int g_1008b8f4;
extern void g_1008b8f8;
extern void g_1008b8fc;
extern void g_1008d2ee;
extern void g_10093cee;
extern char g_100f0e40;
extern char g_100f0e41;
extern char g_100f0e44;
extern char g_100f0e54;
extern unsigned int g_100f0e60;
extern unsigned int g_100f0e64;
extern char g_10134d81;
extern char g_1014f414;
extern struct_4 g_101e6ea8;
extern char g_10202f06;

unsigned int sub_10029010(void)
{
    struct_4 *node;  // ebx
    unsigned int v36;  // ecx
    unsigned int v44;  // ecx
    unsigned int v45;  // ecx
    unsigned int v46;  // ecx
    int v47;  // esi
    int v48;  // edi
    int v49;  // eax
    char iter[2];  // edi
    void* iter1;  // esi
    char v53[2];  // edi
    unsigned int v37;  // eax
    struct_5 *v54;  // eax
    char v55[2];  // edi
    struct_5 *v56;  // edi
    int v57;  // eax
    char v58[2];  // edi
    char v59[2];  // edi
    unsigned int v60;  // eax
    unsigned int v61;  // eax
    void* iter2;  // edx
    int v63;  // edi
    unsigned int v38;  // esi
    char v64;  // al
    struct_1 *v65;  // esi
    unsigned int v66;  // ecx
    unsigned short v67;  // bx
    struct_1 *v68;  // esi
    unsigned int v69;  // ecx
    unsigned short v70;  // bx
    unsigned int v71;  // esi
    unsigned int v72;  // edi
    unsigned int v39;  // edi
    struct_3 *index;  // eax
    unsigned short v74;  // di
    unsigned int v75;  // ecx
    void* v76;  // edx
    void* v78;  // edx
    unsigned int v79;  // ecx
    unsigned int v80;  // edx
    unsigned int n;  // ecx
    unsigned int v82;  // esi
    unsigned int v40;  // ecx
    unsigned int v83;  // edi
    unsigned int v84;  // eax
    unsigned int v85;  // ecx
    void* v86;  // ebx
    void* v87;  // esi
    int v88;  // edi
    struct_4 *v41;  // esi
    void* j;  // ebx
    unsigned int idx[12];  // eax
    unsigned int v0;  // [bp-0x199c]
    void* v1;  // [bp-0x1998], Other Possible Types: unsigned int
    char l[2];  // [bp-0x1994], Other Possible Types: unsigned int
    void* v3;  // [bp-0x1988]
    unsigned int v4;  // [bp-0x1984]
    unsigned int v5;  // [bp-0x1980]
    unsigned int v6;  // [bp-0x197c]
    char i;  // [bp-0x195d]
    unsigned int m;  // [bp-0x195c]
    unsigned int v9;  // [bp-0x1958]
    unsigned int v10;  // [bp-0x1954]
    unsigned int v11;  // [bp-0x1950]
    unsigned int v12;  // [bp-0x194c]
    unsigned int v13;  // [bp-0x1948]
    unsigned int v14;  // [bp-0x1940]
    unsigned int v15;  // [bp-0x193c]
    unsigned int v16;  // [bp-0x1938]
    unsigned int v17;  // [bp-0x1934]
    unsigned int v18;  // [bp-0x1930]
    unsigned int v19;  // [bp-0x192c]
    char v20;  // [bp-0x1928]
    char v21;  // [bp-0x1927]
    unsigned short v22;  // [bp-0x1926]
    unsigned short v23;  // [bp-0x191e]
    Byte v24[256];  // [bp-0x128]
    unsigned int v25;  // [bp-0x28]
    unsigned int v26;  // [bp-0x24]
    unsigned int v27;  // [bp-0x20]
    unsigned int v28;  // [bp-0x1c]
    int v29;  // [bp-0x18]
    unsigned int v30;  // [bp-0x14]
    unsigned int v31;  // [bp-0x10]
    int v32;  // [bp-0xc], Other Possible Types: unsigned int
    struct_4 *v33;  // [bp-0x8], Other Possible Types: int, unsigned int

    if (g_100f0e41 || g_100f0e40)
    {
        v10 = g_1005f854 - g_100f0e60 - (g_10080b84->field_1c >> 1);
        v12 = v10 + g_10080b84->field_1c;
        v11 = g_1005f858 - g_100f0e64 - (g_10080b84->field_20 >> 1);
        v13 = v11 + g_10080b84->field_20;
        node = &g_101e6ea8.padding_0[0];
        v36 = 0;
        v37 = _INSERT(v13, 0, g_1005f537);
        i = g_1005f537;
        g_1008b8f4 = 0xff;
        *((unsigned int *)&g_1008b8f8) = 0xff;
        for (*((unsigned int *)&g_1008b8fc) = 0xff; v36 < *((int *)&g_10202f06) || !i; i = 1)
        {
            v36 = v36;
            if (i)
            {
                v38 = *((int *)&node->padding_0[0]);
                v39 = *((int *)&node->padding_0[4]);
            }
            else
            {
                v38 = g_1005f854;
                v39 = g_1005f858;
            }
            if (v38 >= v10 && v38 <= v12 && v39 >= v11 && v39 <= v13)
            {
                v33 = v38 - v10 + g_10080b84->field_14 - 2;
                v32 = v39 - v11 + g_10080b84->field_18 - 8;
                v37 = node->field_8;
                v40 = *((int *)&g_100f0e54);
                if (*((int *)&g_100f0e54) == 4294967295)
                    v40 = g_1005f85c;
                if (!v40 - v37 || !i)
                {
                    if (!i)
                    {
                        lstrcpy(v24, g_1005f7ed + 4);
                    }
                    else if (g_100f0e44)
                    {
                        lstrcpy(v24, node->padding_c);
                    }
                    else
                    {
                        v6 = v36 + 1;
                        v5 = *((char *)(node->field_2c + sub_10015d9a));
                        wsprintfA(v24, "%c%d");
                    }
                    sub_1003b127(v33, v32, ".", node);
                    v33 -= sub_10028cf5() >> 1;
                    v32 -= 7;
                    v41 = v33;
                    v37 = sub_1003b127(v41, v32, v24);
                    node = v41;
                }
            }
            if (i)
            {
                v36 += 1;
                node = &node[1].padding_0[2];
            }
        }
    }
    v19 = 0;
    for (j = &g_1008d2ee; j < &g_10093cee; j = v86 + 106)
    {
        v86 = j;
        if ((char)v86[32] && (v86 = j, (int)v86[74]))
        {
            v86 = j + 32;
            idx = sub_100399af(j + 32, j);
            if (idx)
            {
                *((unsigned int *)&v86[74]) = idx[9];
                *((unsigned int *)&v86[78]) = idx[10];
                *((unsigned int *)&v86[82]) = idx[11];
                *((unsigned short *)&v86[64]) = (short)v86[64] | 128;
            }
            v44 = (short)v86[64] & 127;
            if ((int)v86[70] == 1 || v44 == 3)
            {
                g_1008b8f4 = 0xff;
                *((unsigned int *)&g_1008b8f8) = 72;
                *((unsigned int *)&g_1008b8fc) = 72;
            }
            else if ((int)v86[70] == 2 || v44 == 2)
            {
                g_1008b8f4 = 104;
                *((unsigned int *)&g_1008b8f8) = 104;
                *((unsigned int *)&g_1008b8fc) = 0xff;
                if (!g_10134d81)
                {
                    v45 = (int)v86[90];
                    if ((int)v86[90])
                    {
                        g_1008b8fc = v45;
                        v46 = v45 >> 8;
                        g_1008b8f8 = v46;
                        *((char *)&g_1008b8f4) = v46 >> 8;
                    }
                }
            }
            else
            {
                g_1008b8f4 = 200;
                *((unsigned int *)&g_1008b8f8) = 200;
                *((unsigned int *)&g_1008b8fc) = 200;
                if (*((int *)v86) == 2036621644)
                {
                    g_1008b8f4 = 0xff;
                    *((unsigned int *)&g_1008b8f8) = 0;
                    *((unsigned int *)&g_1008b8fc) = 0xff;
                }
            }
            v37 = (int)v86[94];
            if ((int)v86[94])
            {
                v37 &= 4;
                if (!v37)
                {
                    g_1008b8f4 = 0xff - g_1008b8f4;
                    *((unsigned int *)&g_1008b8f8) = 0xff - *((int *)&g_1008b8f8);
                    v37 = 0xff - *((int *)&g_1008b8fc);
                    *((unsigned int *)&g_1008b8fc) = v37;
                }
            }
            if (g_100f0e41 || g_100f0e40)
            {
                v71 = (int)v86[74];
                v72 = (int)v86[78];
                if (v71 >= v10 && v71 <= v12 && v72 >= v11 && v72 <= v13)
                {
                    v33 = v71 - v10 + g_10080b84->field_14 - 2;
                    v32 = v72 - v11 + g_10080b84->field_18 - 8;
                    index = &(&v20)[12 * v19];
                    v74 = (unsigned short)v32 + 3;
                    index->field_2 = v33;
                    index->field_8 = v74;
                    index->field_4 = v33 + 3;
                    index->field_6 = v74 + 7;
                    v19 += 1;
                    v75 = *((int *)&g_100f0e54);
                    if (*((int *)&g_100f0e54) == 4294967295)
                        v75 = g_1005f85c;
                    v76 = v86;
                    if (g_1014f414)
                        v76 = v86 + 32;
                    v78 = v76;
                    v79 = v75 - (int)v86[82];
                    if (!v79)
                    {
                        lstrcpy(v24, v78);
                    }
                    else if (v79 < 55)
                    {
                        v4 = v79;
                        v3 = v78;
                        wsprintfA(v24, "%s +%d");
                    }
                    else
                    {
                        v4 = v79;
                        v3 = v78;
                        wsprintfA(v24, "%s %d");
                    }
                    sub_1003b127(v33, v32, ".", v86);
                    v80 = sub_10028cf5();
                    v33 -= v80 >> 1;
                    v32 -= 7;
                    v9 = 0;
                    while (true)
                    {
                        if (v9 >= 64)
                            break;
                        m = 0;
                        while (m < 64)
                        {
                            v86 = &v20;
                            n = 0;
                            while (n < v19)
                            {
                                l = n;
                                v82 = v33 + v9;
                                v83 = v32 + m;
                                v84 = v80 + v82;
                                v85 = v83 + 9;
                                if ((unsigned short)v82 < (short)v86[2])
                                    v82 = _INSERT(v82, 0, (short)v86[2]);
                                if ((unsigned short)v84 > (short)v86[4])
                                    v84 = _INSERT(v84, 0, (short)v86[4]);
                                if ((unsigned short)v83 < (short)v86[8])
                                    v83 = _INSERT(v83, 0, (short)v86[8]);
                                if ((unsigned short)v85 > (short)v86[6])
                                    v85 = _INSERT(v85, 0, (short)v86[6]);
                                if (v82 > v84 || v83 > v85)
                                {
                                    v86 += 12;
                                    n += 1;
                                }
                                else
                                {
                                    m += 2;
                                }
                            }
                            goto LABEL_1002954b;
                        }
                        v9 += 2;
                    }
LABEL_1002954b:
                    v19 += 1;
                    v87 = v33 + v9;
                    v88 = v32 + m;
                    *((unsigned short *)&v86[2]) = *((unsigned short *)&v87);
                    *((unsigned short *)&v86[8]) = v88;
                    *((unsigned short *)&v86[4]) = *((unsigned short *)&v80 + 3 + v87);
                    *((unsigned short *)&v86[6]) = v88 + 8;
                    v37 = sub_1003b127(v87, v88, v24, v33);
                    v86 = v87;
                }
                goto LABEL_1002993c;
            }
            v37 = g_10052770 - (int)v86[82];
            v47 = g_10052768 - (int)v86[74] + v37;
            v48 = g_1005276c - (int)v86[78] + v37;
            if (v47 < 50000)
            {
                v31 = 4294967295;
                v33 = v47;
            }
            else
            {
                v31 = 1;
                v33 = ~(v33) + 1;
            }
            if (v48 < 50000)
            {
                v30 = 4294967295;
                v32 = v48;
            }
            else
            {
                v30 = 1;
                v32 = ~(v48) + 1;
            }
            if (v33 < 8 && !((v86 = v86, v32 >= 6)))
                goto LABEL_1002993c;
            v49 = v33;
            if (v49 < v32)
                v49 = v32;
            v29 = v49;
            v28 = v33 * 0x10000 / v29;
            v17 = v28;
            v37 = v32 * 0x10000 / v29;
            v27 = v37;
            v16 = v37;
            if (!g_10080b84 || !((v86 = v86, (short)v86[64] >= 1)))
                goto LABEL_1002993c;
            iter = v24;
            iter1 = v86;
            if (g_1014f414)
                iter1 = v86 + 32;
            for (; *((char *)iter1); iter = &iter[1])
            {
                iter[0] = *((char *)iter1);
                iter1 += 1;
            }
            iter[0] = 32;
            v53 = &iter[1];
            v54 = 300 - (int)v86[66];
            if ((short)v86[64] == 1)
            {
                v53[0] = 69;
            }
            else if ((short)v86[64] == 2)
            {
                v53[0] = 65;
            }
            else if ((short)v86[64] >= 3)
            {
                v53[0] = 83;
            }
            v55 = &v53[1];
            if (v54 >= 0x64)
            {
                sub_10040940(v54, v55, v55);
                v56 = &v54->field_2;
            }
            else
            {
                if (v54 < 0xc)
                    v54 = NULL;
                sub_10040940(v54, v55, v55);
                v56 = &v54->padding_0[1];
            }
            *((unsigned short *)&v56->padding_0[0]) = 17440;
            l = v33 + v32;
            sub_10040940(v33 + v32, &v56->field_2, &v56->field_2);
            if ((char)v86[64] != 1)
            {
                if (v57)
                {
                    for (v57 = g_10052770 - (int)v86[82]; l[0]; l = &l[1]);
                    l[0] = 32;
                    v58 = &l[1];
                    if (v57 > 32)
                    {
                        v58[0] = 45;
                        v59 = &v58[1];
                        v57 = ~(v57) + 1;
                    }
                    else
                    {
                        v58[0] = 43;
                        v59 = &v58[1];
                    }
                    sub_10040940(v57, v59);
                }
            }
            v60 = g_10080b84->field_1c >> 1;
            v26 = v60;
            v1 = g_10080b84;
            v0 = v60;
            v61 = sub_10028cf5();
            v18 = v61;
            if (v31 == 1)
                v60 -= v61;
            v28 = (v60 * v28 >> 16) * v31;
            v25 = g_10080b84->field_20 >> 1;
            v27 = ((v30 == 1 ? v25 - 11 : v25 - 1) * v27 >> 16) * v30;
            iter2 = g_10080b84->field_14 + v26 + v28;
            v63 = g_10080b84->field_18 + v25 + v27;
            v1 = v86;
            if (v17 == 0x10000)
            {
                v64 = (char)v31 + 8;
            }
            else
            {
LABEL_10029803:
                if (v16 == 0x10000)
                {
                    v37 = v30 + 16;
                    v15 = 0;
                    v14 = 0;
                }
                else
                {
LABEL_1002992b:
                    v37 = sub_1003b127(iter2, v63, v24, v86);
                    v86 = iter2;
                    goto LABEL_1002993c;
                }
                while (true)
                {
                    v68 = &v20;
                    v69 = 0;
                    while (true)
                    {
                        if (v69 >= v19)
                        {
                            v19 += 1;
                            v20 = v37;
                            v21 = v15;
                            v22 = *((unsigned short *)&iter2);
                            v23 = *((unsigned short *)&v18 + iter2);
                            goto LABEL_1002992b;
                        }
                        if (v68->field_0 == (char)v37 && (char)v15 == v68->padding_1 && (iter2 > g_10080b84->field_1c || !((v70 = (unsigned short)iter2 + (unsigned short)v18, (iter2 + v18 < (unsigned int)v68->field_2 || iter2 + v18 > (unsigned int)v68->field_a) && ((unsigned int)*((unsigned short *)(void*)&iter2) < (unsigned int)v68->field_2 || (unsigned int)*((unsigned short *)(void*)&iter2) > (unsigned int)v68->field_a) && ((unsigned int)*((unsigned short *)(void*)&iter2) >= (unsigned int)v68->field_2 || iter2 + v18 <= (unsigned int)v68->field_a)))))
                            break;
                        v68 += 1;
                        v69 += 1;
                    }
                    if (v14 < 8)
                    {
                        iter2 += 12;
                        v14 += 1;
                    }
                    else if (v14 == 8)
                    {
                        iter2 -= 108;
                        v14 += 1;
                    }
                    else if (v14 < 16)
                    {
                        iter2 -= 12;
                        v14 += 1;
                    }
                    else if (v15 < 16)
                    {
                        iter2 += 96;
                        v14 = 0;
                        v63 = (v30 == 4294967295 ? v63 + 10 : v63 - 10);
                        v15 += 1;
                    }
                    else
                    {
                        goto LABEL_1002993c;
                    }
                }
            }
            while (true)
            {
                v65 = &v20;
                v66 = 0;
                while (true)
                {
                    if (v66 >= v19)
                    {
                        v19 += 1;
                        v20 = v64;
                        v22 = v63;
                        v23 = 9 + v63;
                        goto LABEL_10029803;
                    }
                    if (v65->field_0 == v64 && !((v67 = (short)v63 + 9, ((unsigned int)((short)v63 + 9) < (unsigned int)v65->field_2 || (unsigned int)((short)v63 + 9) > (unsigned int)v65->field_a) && ((unsigned int)(unsigned short)v63 < (unsigned int)v65->field_2 || (unsigned int)(unsigned short)v63 > (unsigned int)v65->field_a) && ((unsigned int)(unsigned short)v63 >= (unsigned int)v65->field_2 || (unsigned int)((short)v63 + 9) <= (unsigned int)v65->field_a))))
                        break;
                    v65 += 1;
                    v66 += 1;
                }
                v63 += 3;
            }
        }
        else
        {
LABEL_1002993c:
        }
    }
    return v37;
}
```

## `sub_1002994d` `0x1002994d`

_50 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[66];
    unsigned int field_42;
    char padding_46[24];
    unsigned int field_5e;
} struct_0;

extern struct_0 g_1008d2ee;
extern struct_0 g_10093cee;

unsigned int sub_1002994d(void)
{
    struct_0 *iter;  // ebx
    unsigned int v2;  // eax

    for (iter = &g_1008d2ee.padding_0[0]; iter < &g_10093cee.padding_0[0]; iter = &iter[1].padding_0[6])
    {
        v2 = *((int *)&(iter->padding_0)[1]);
        if (!*((int *)&(iter->padding_0)[1]))
        {
            iter->padding_0[0] = 0;
            iter->padding_0[32] = 0;
        }
        else
        {
            *((unsigned int *)&(iter->padding_0)[1]) = v2 - 1;
            v2 = *((int *)&iter->padding_46[22]);
            if (*((int *)&iter->padding_46[22]))
            {
                v2 -= 1;
                *((unsigned int *)&iter->padding_46[22]) = v2;
            }
        }
    }
    return v2;
}
```

## `sub_1002997f` `0x1002997f`

_226 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f7e5;
extern unsigned int g_1005f7e9;
extern char g_1005f7f1;
extern char g_1005f7f8;
extern char g_1005f7f9;
extern char g_1005f800;
extern char g_1005f801;
extern unsigned int g_1005f809;
extern unsigned int g_1005f811;
extern unsigned int g_1005f831;

int sub_1002997f(void)
{
    unsigned int count;  // eax
    void* i;  // ecx
    unsigned int node;  // edi
    void* j;  // ecx
    unsigned int iter;  // edi
    unsigned int v8;  // eax
    unsigned int v9;  // eax
    unsigned int v0;  // [bp-0x8]
    void* v1;  // [bp-0x4]

    count = g_1005f7e5;
    if (g_1005f7e5 != g_1005f7e9)
    {
        g_1005f7e9 = g_1005f7e5;
        i = 0x63fe40;
        for (node = 0; i < 0x63fe5c; i += 4)
        {
            (&g_1005f7f1)[node] = *((char *)i);
            (&g_1005f7f9)[node] = (char)i[28];
            node += 1;
        }
        g_1005f7f8 = *(0x63fe84);
        count = _INSERT(g_1005f7e5, 0, *(0x63fe7c));
        g_1005f800 = *(0x63fe7c);
        g_1005f809 = 0;
        g_1005f809 = 0;
    }
    j = 0x63fe40;
    for (iter = 0; j < 0x63fe60; j += 4)
    {
        count = _INSERT(count, 0, (char)j[28]);
        if (j == 0x63fe5c)
            count = *((int *)0x63fe7c);
        if ((char)count != (&g_1005f7f9)[iter])
        {
            (&g_1005f7f9)[iter] = count;
            v8 = count;
            if (!*(iter + (char *)&g_1005f809) || *(iter + (char *)&g_1005f809) && !((v9 = _INSERT(count, 0, (char)count), v8 = _INSERT(count, 0, (char)count), (char)count)))
            {
                *(iter + (char *)&g_1005f809) = 1;
                (&g_1005f801)[iter] = v8;
                v1 = j;
                v0 = iter;
                count = GetTickCount();
                iter = v0;
                j = v1;
                (&g_1005f811)[iter] = count;
            }
            else
            {
                *(iter + (char *)&g_1005f809) = 2;
                v1 = j;
                v0 = iter;
                count = GetTickCount();
                iter = v0;
                j = v1;
                (&g_1005f831)[iter] = count;
            }
        }
        iter += 1;
    }
    return count;
}
```

## `sub_10029a61` `0x10029a61`

_218 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
    char padding_1[63];
    unsigned short field_40;
    char padding_42[4];
    unsigned int field_46;
    unsigned int field_4a;
    unsigned int field_4e;
    unsigned int field_52;
    unsigned int field_56;
} struct_0;

extern struct_0 g_1008d2ee;
extern struct_0 g_10093cee;

int sub_10029a61(unsigned int a0, int a1, int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6)
{
    unsigned int v2;  // eax
    struct_0 *iter;  // ebx
    struct_0 *v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    if (a0 == 1)
    {
        v2 = sub_1003a494(a2);
        if (v2)
        {
            v1 = 1;
        }
        else
        {
            v2 = sub_1003a320(a2);
            if (v2)
                v1 = 2;
        }
    }
    v0 = NULL;
    iter = &g_1008d2ee.field_0;
    while (true)
    {
        if (iter < &g_10093cee.field_0)
        {
            if (iter->field_0)
            {
                v2 = lstrcmp(&iter->padding_1[31], a2);
                if (!v2)
                    goto LABEL_10029ae2;
            }
            else if (!v0)
            {
                v0 = iter;
                *((unsigned int *)&iter[1].padding_1[9]) = 0;
            }
            iter = &iter[1].padding_1[13];
        }
        else
        {
            iter = v0;
            if (!iter)
                return v2;
LABEL_10029ae2:
            lstrcpyn(iter, a1, 32);
            lstrcpyn(&iter->padding_1[31], a2, 32);
            *((unsigned int *)((char *)&iter->field_46 + 2)) = a3;
            *((unsigned int *)((char *)&iter->field_4a + 2)) = a4;
            *((unsigned int *)((char *)&iter->field_4e + 2)) = a5;
            iter->field_40 = a0;
            *((unsigned int *)&(iter->padding_42)[1]) = v1;
            *((unsigned int *)&iter->padding_42[0]) = 300;
            *((unsigned int *)((char *)&iter->field_52 + 2)) = a6;
            if (((char)a6 & 1))
            {
                *((unsigned int *)&iter[1].padding_1[1]) = 16;
                break;
            }
        }
    }
    return a6 & 1;
}
```

## `sub_10029b3b` `0x10029b3b`

_515 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
    char field_4;
    char padding_5[31];
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    unsigned int field_14;
} struct_0;

typedef struct struct_3 {
    char padding_0[36];
    unsigned int field_24;
    unsigned int field_28;
} struct_3;

extern char g_1005dc8c;
extern int g_1005f7b1;
extern struct_0 *g_1005f7e5;
extern struct_1 *g_1005f7ed;
extern int g_1005f854;
extern char g_1005f858;
extern char g_1005f85c;
extern unsigned int g_100f0ddc;
extern char g_100f9314;
extern char g_100f9315;
extern unsigned int g_100f9318;
extern struct_3 *g_100f9320;
extern char g_100f9327;
extern char g_1014f416;
extern char g_1014f418;
extern unsigned int g_101dfe94;
extern unsigned int g_102e2a08;

unsigned int [6] sub_10029b3b(void)
{
    struct_1 *v3;  // eax
    unsigned int v4;  // eax
    unsigned int v5;  // eax
    unsigned int v6[6];  // eax
    unsigned int v7[6];  // eax
    unsigned int v8[6];  // ebx
    int v9;  // eax
    unsigned int v10[6];  // ecx
    int v11;  // eax
    unsigned int v0;  // [bp-0x64]
    unsigned int v1[6];  // [bp-0x48]

    v1 = g_1005f7e5;
    v3 = g_1005f7ed;
    if (g_1005f7ed)
        v3 = g_1005f7ed->field_0;
    if (*((int *)0x63fe98) != g_1005f7e5 || v3 != g_1005f7e5)
    {
        g_1005f7e5 = *((int *)0x63fe98);
        v4 = sub_1003997e(*(0x63fe98));
        if (v4)
            g_1005f7ed = v4;
        lstrcpy(&g_1005f7b1, &g_1005f7ed->field_4);
        sub_1002387b();
    }
    if (g_1005f7ed)
    {
        if (g_1005f7ed->field_24 != g_1005f854 || g_1005f7ed->field_28 != *((int *)&g_1005f858) || g_1005f7ed->field_2c != *((int *)&g_1005f85c))
            g_100f9327 = 1;
        sub_1002ae6f(&g_1005f854, &g_1005f7ed->field_24, 12);
    }
    if (g_102e2a08)
    {
        v5 = *((int *)0x64f600) + g_102e2a08;
        if (!v5 || v5 > 50)
            v5 = 1;
        if (v5 > 15)
            v5 = 15;
        v6 = sub_10002c01(v5);
    }
    else
    {
        v6 = sub_10002c01(0);
    }
    if (g_100f9314)
    {
        if (g_100f9315)
        {
            g_1005dc8c = 0;
            g_100f9315 = 0;
        }
        g_100f9314 = 0;
        v6 = v1;
        if (g_1014f416 && v6 != g_1005f7e5 && !g_1005dc8c)
        {
            g_1005dc8c = 0;
            v6 = sub_1001f5bd();
        }
        g_100f9318 = 4294967295;
        if (g_1014f418)
            g_100f9318 = 0;
    }
    if (!g_100f9320)
        return v6;
    v7 = sub_10012827(g_100f9320, 0, 1);
    if (v7)
    {
        v7 = sub_10012d79(g_100f9320, v7);
        if (v7 && v7[4] != 1 && v7[4] != 9)
        {
            v7 = v7[5] & 63;
            if (v7)
            {
                if (v7 >= 0x6 && v7 <= 0xd)
                {
                    v8 = v7;
                    v9 = g_1005f854 - g_100f9320->field_24;
                    v10 = (v9 ^ v9 >> 31) - (v9 >> 31);
                    v11 = *((int *)&g_1005f858) - g_100f9320->field_28;
                    v7 = (v11 ^ v11 >> 31) - (v11 >> 31);
                    if (v7 < v10)
                        v7 = v10;
                    if (v7 > 0x3 && (v8 != 0xb || v7 > 0x5) && (v8 != 0xc || v7 > 0x4))
                    {
                        g_100f9320 = 0;
                        return v7;
                    }
                    v7 = v8;
                }
                v7 = sub_1003a60a(g_100f9320, v7);
                v0 = g_101dfe94;
                g_100f0ddc = g_101dfe94;
            }
        }
    }
    g_100f9320 = 0;
    return v7;
}
```

## `sub_10029d3e` `0x10029d3e`

_16 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_100428c5;

void sub_10029d3e(unsigned int a0)
{
    char v0;  // [bp+0x0]

    g_100428c5(a0, &v0);
    return;
}
```

## `sub_10029d4e` `0x10029d4e`

_836 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
    unsigned short field_c;
    unsigned short field_e;
} struct_0;

typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

typedef struct struct_3 {
    char padding_0[28];
    unsigned int field_1c;
    unsigned int field_20;
} struct_3;

extern struct_2 *g_100428c1;
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern unsigned int g_1005f85c;
extern struct_3 *g_10080b84;
extern char g_100ee8bb;
extern char g_100f0e41;
extern unsigned int g_100f0e54;
extern unsigned int g_100f0e58;
extern unsigned int g_100f0e5c;
extern unsigned int g_100f0e60;
extern unsigned int g_100f0e64;
extern unsigned int g_100f0e68;
extern unsigned int g_100f0e6c;
extern unsigned int g_100f0e70;
extern unsigned int g_100f0e74;
extern char g_100f94c6;
extern unsigned int g_79cf88;

int sub_10029d4e(void)
{
    unsigned int v21;  // ecx
    unsigned int v22;  // edx
    unsigned int v31;  // eax
    unsigned int v32;  // eax
    unsigned int v33;  // eax
    unsigned int v34;  // eax
    unsigned int v35;  // eax
    unsigned int v36;  // ecx
    unsigned int v23;  // ebx
    unsigned int v24;  // esi
    struct_0 *idx;  // ecx
    unsigned int v27;  // edx
    unsigned int v28;  // edi
    unsigned int v29;  // ebx
    unsigned int v30;  // eax
    unsigned int v0;  // [bp-0x54]
    unsigned int v1;  // [bp-0x50]
    char *v2;  // [bp-0x4c]
    unsigned int v3;  // [bp-0x48]
    unsigned int v4;  // [bp-0x44]
    unsigned int v5;  // [bp-0x40]
    struct_0 *v6;  // [bp-0x3c]
    unsigned int v7;  // [bp-0x38]
    unsigned int v8;  // [bp-0x30]
    char *v9;  // [bp-0x2c]
    struct_0 **v10;  // [bp-0x28]
    unsigned int v11;  // [bp-0x24]
    unsigned int v12;  // [bp-0x20]
    unsigned int v13;  // [bp-0x1c]
    unsigned int v14;  // [bp-0x18]
    struct_0 *v15;  // [bp-0x14]
    char v16;  // [bp-0x4]
    struct_0 *v17;  // [bp+0x4]
    unsigned int v18;  // [bp+0x8]
    unsigned int v19;  // [bp+0xc]
    unsigned int v20;  // [bp+0x10]

    if (g_100f94c6 == 2)
    {
        g_79cf88 = 7;
        g_100f94c6 = g_100f94c6 - 1;
    }
    v15 = v17;
    v14 = g_100428c1(v17, v18, v19, v20);
    v13 = v21;
    v12 = v22;
    v11 = v23;
    v10 = &v15;
    v9 = &v16;
    v8 = v24;
    idx = v17;
    if ((*((int *)&idx->padding_0[4]) == 0x101 || *((int *)&idx->padding_0[4]) == 0x100) && (idx->field_8 >= 96 && idx->field_8 <= 105 || idx->field_8 == 110 || idx->field_8 == 106 || idx->field_8 == 111 || idx->field_8 == 107 || idx->field_8 == 109))
        idx->field_8 = 0;
    v27 = *((int *)&idx->padding_0[4]);
    if (g_100ee8bb && *((int *)0x64a9c0) == 31 && (v27 == 513 || v27 == 0x202 || v27 == 516 || v27 == 517))
        *((unsigned int *)&idx->field_c) = 4294967295;
    if (!g_100f0e41)
    {
        sub_1002a092();
        return;
    }
    else if (g_10080b84)
    {
        if (v27 == 0x200)
        {
            v7 = 6597056;
            v6 = idx;
            v5 = 0x200;
            v4 = v23;
            v3 = &/* unsupported instruction */;
            v2 = &v16;
            v1 = v24;
            v0 = v28;
            v29 = idx->field_e - *((int *)&g_10080b84->padding_0[24]) - (g_10080b84->field_20 >> 1) + g_1005f858 - g_100f0e64;
            g_100f0e68 = idx->field_c - *((int *)&g_10080b84->padding_0[20]) - (g_10080b84->field_1c >> 1) + g_1005f854 - g_100f0e60;
            g_100f0e6c = v29;
            v27 = 0x200;
        }
        if (v27 == 516)
        {
            v30 = idx->field_c;
            if (v30 <= *((int *)&g_10080b84->padding_0[20]))
            {
                sub_1002a092();
                return;
            }
            if (v30 < *((int *)&g_10080b84->padding_0[20]) + g_10080b84->field_1c)
            {
                v31 = idx->field_e;
                if (v31 > *((int *)&g_10080b84->padding_0[24]) && v31 < *((int *)&g_10080b84->padding_0[24]) + g_10080b84->field_20)
                {
                    g_100f0e5c = *((int *)&idx->field_c);
                    *((unsigned int *)&idx->field_c) = 4294967295;
                }
            }
            sub_1002a092();
            return;
        }
        else
        {
            if (v27 == 0x200 && g_100f0e5c)
            {
                g_100f0e60 = (*((int *)&idx->field_c) & 0xffff) - (g_100f0e5c & 0xffff) + g_100f0e70;
                g_100f0e64 = (*((int *)&idx->field_c) >> 16) - (g_100f0e5c >> 16) + g_100f0e74;
                sub_1002a092();
                return;
            }
            if (v27 == 517)
            {
                if (g_100f0e5c)
                {
                    v7 = g_100f0e60;
                    g_100f0e70 = v7;
                    v7 = g_100f0e64;
                    g_100f0e74 = v7;
                    g_100f0e5c = 0;
                    *((unsigned int *)&idx->field_c) = 4294967295;
                }
                sub_1002a092();
                return;
            }
            else if (v27 == 513)
            {
                v32 = idx->field_c;
                if (v32 <= *((int *)&g_10080b84->padding_0[20]))
                {
                    sub_1002a092();
                    return;
                }
                if (v32 < *((int *)&g_10080b84->padding_0[20]) + g_10080b84->field_1c)
                {
                    v33 = idx->field_e;
                    if (v33 > *((int *)&g_10080b84->padding_0[24]) && v33 < *((int *)&g_10080b84->padding_0[24]) + g_10080b84->field_20)
                        g_100f0e58 = *((int *)&idx->field_c);
                }
                sub_1002a092();
                return;
            }
            else if (v27 != 0x202)
            {
                sub_1002a092();
                return;
            }
            else if (!g_10080b84)
            {
                sub_1002a092();
                return;
            }
            else if (g_100f0e58)
            {
                v34 = *((int *)&idx->field_c);
                *((unsigned int *)&idx->field_c) = 4294967295;
                if (v34 == g_100f0e58)
                {
                    v7 = g_1005f85c;
                    sub_10015204((v34 & 0xffff) - *((int *)&g_10080b84->padding_0[20]) - (g_10080b84->field_1c >> 1) + g_1005f854 - g_100f0e60, (v34 >> 16) - *((int *)&g_10080b84->padding_0[24]) - (g_10080b84->field_20 >> 1) + g_1005f858 - g_100f0e64);
                }
                else
                {
                    v35 = v34 >> 16;
                    v36 = g_100f0e58 >> 16;
                    if (v35 < v36)
                    {
                        if (v35 < v36 - 5)
                        {
                            if (g_100f0e54 == 4294967295)
                            {
                                v7 = g_1005f85c;
                                g_100f0e54 = v7;
                            }
                            if (g_100f0e54)
                                g_100f0e54 = g_100f0e54 - 1;
                        }
                    }
                    else
                    {
                        if (v35 > v36 && v35 - 5 > v36)
                        {
                            if (g_100f0e54 == 4294967295)
                            {
                                v7 = g_1005f85c;
                                g_100f0e54 = v7;
                            }
                            if (g_100f0e54 < 15)
                                g_100f0e54 = g_100f0e54 + 1;
                        }
                    }
                }
                g_100f0e58 = 0;
                sub_1002a092();
                return;
            }
            else
            {
                sub_1002a092();
                return;
            }
        }
    }
    else
    {
        sub_1002a092();
        return;
    }
}
```

## `sub_1002a092` `0x1002a092`

_637 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
    unsigned int field_18;
    unsigned int field_1c;
    unsigned int field_20;
} struct_0;

typedef struct struct_1 {
    char padding_0[48];
    unsigned int field_30;
    char padding_34[4];
    unsigned int field_38;
} struct_1;

extern struct_0 *g_10080b84;
extern char g_1008a80b;
extern char g_1008a88b;
extern char g_1008a90b;
extern char g_1008a98b;
extern unsigned int g_1014f420[15];
extern unsigned int g_101d5e20[15];
extern char g_101d5e26;
extern unsigned int g_10291cea;
extern struct_1 *g_10291cee;
extern unsigned int g_10291cf2;

unsigned int sub_1002a092(void* index)
{
    unsigned int v14;  // edx
    unsigned int idx;  // eax
    unsigned int v24;  // eax
    unsigned int v26;  // ecx
    unsigned int v29[15];  // ebx
    unsigned int v16[15];  // ebx
    unsigned int v17;  // eax
    unsigned int v18;  // edx
    unsigned int idx1[15];  // ebx
    unsigned int iter;  // eax
    unsigned int node;  // ecx
    char v22;  // dl
    char v23;  // dl
    unsigned int v0;  // [bp-0x3c]
    unsigned int v1;  // [bp-0x34]
    unsigned int v2;  // [bp-0x30]
    unsigned int v3;  // [bp-0x2c]
    unsigned int v4;  // [bp-0x28]
    unsigned int v5[15];  // [bp-0x24]
    unsigned int v6;  // [bp-0x20]
    unsigned int v7;  // [bp-0x1c]
    unsigned int v8;  // [bp-0x18]
    unsigned int v9;  // [bp-0x14]
    unsigned int v10;  // [bp-0x10]
    unsigned int v11;  // [bp-0xc]
    unsigned int v12;  // [bp-0x8]

    if (*((int *)0x64a9c0) != 31)
    {
        return 6597056;
    }
    else if (!g_10080b84)
    {
        return 6597056;
    }
    else if (!g_101d5e26)
    {
        return 6597056;
    }
    else
    {
        v14 = (int)index[4];
        if (v14 == 0x200)
        {
            g_10291cf2 = 0;
        }
        else if (v14 != 513 && v14 != 516 && (v14 != 0x202 || !g_10291cee))
        {
            if (v14 != 517)
            {
                return 6597056;
            }
            else if (!g_10291cea)
            {
                return 6597056;
            }
        }
        v1 = v14;
        idx = (short)index[12];
        v3 = idx;
        v2 = (short)index[14];
        v11 = 0;
        v10 = 0;
        v9 = 0;
        v8 = 0;
        v7 = 0;
        v6 = 0;
        v0 = 0;
        v16 = &g_1014f420[0];
        while (true)
        {
            if (v16 >= &g_101d5e20[0])
                return idx;
            if (!(char)v16[0])
                return idx;
            if (v16[1 + 2])
            {
                v5 = v16;
                v12 = 32;
                if (v16[1 + 1])
                    v12 = 64;
                v17 = v0;
                v18 = 4076;
                v4 = 0;
                if ((&g_1008a90b)[v17] || (&g_1008a98b)[v17])
                {
                    v18 = 4176;
                    v4 = 1;
                }
                idx1 = (char *)v16 + v18;
                iter = idx1[13];
                node = idx1[1];
                v22 = idx1[12];
                if (v22 == 1)
                {
                    iter += v11;
                }
                else if (v22 == 2)
                {
                    iter += g_10080b84->field_14;
                }
                else if (v22 == 3)
                {
                    iter = iter + g_10080b84->field_14 + g_10080b84->field_1c;
                }
                else if (v22 == 4)
                {
                    iter += v9;
                }
                else if (v22 == 5)
                {
                    iter += v7;
                }
                v23 = idx1[14];
                if (v23 == 1)
                {
                    node += v10;
                }
                else if (v23 == 2)
                {
                    node += g_10080b84->field_18;
                }
                else if (v23 == 3)
                {
                    node = node + g_10080b84->field_18 + g_10080b84->field_20;
                }
                else if (v23 == 4)
                {
                    node += v8;
                }
                else if (v23 == 5)
                {
                    node += v6;
                }
                v11 = iter;
                v10 = node;
                if (v4)
                {
                    v9 = iter;
                    v8 = node;
                }
                else
                {
                    v7 = iter;
                    v6 = node;
                }
                v24 = iter;
                if (v24 > 100000)
                    v24 = 0;
                idx = v24;
                v26 = node;
                if (v26 > 100000)
                    v26 = 0;
                if (v3 >= idx && v3 <= v12 + iter && v2 >= v26 && v2 <= v12 + node)
                    break;
                v16 = v5;
            }
            v0 += 1;
            v16 = &v16[71 + 12];
        }
        v29 = v5;
        if (v1 == 513)
        {
            g_10291cee = v29;
        }
        else if (v1 == 516)
        {
            g_10291cea = v29;
        }
        else if (v1 == 0x202 && v29 == g_10291cee)
        {
            idx = v0;
            (&g_1008a80b)[idx] = 1;
        }
        else if (v1 == 517 && v29 == g_10291cea)
        {
            idx = v0;
            (&g_1008a88b)[idx] = 1;
        }
        else
        {
            if (v1 != 0x200)
                return idx;
            g_10291cf2 = v29;
            return idx;
        }
        *((unsigned int *)&index[12]) = 4294967295;
        return idx;
    }
}
```

## `sub_1002a2e7` `0x1002a2e7`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002a2e7(void)
{
}
```

## `sub_1002a311` `0x1002a311`

_290 bytes. (leaf/helper — see body)_

```c
extern char *g_10042668;
extern unsigned int g_1004266c;
extern char g_10042674;
extern char g_1004267c;
extern char g_1004267e;
extern char g_10042682;
extern char g_10042684;

unsigned int sub_1002a311(void)
{
    unsigned int v1;  // eax

    v1 = g_10042668 + 5213760;
    *(g_10042668) = 0x55;
    *((unsigned int *)&g_10042668[1]) = 4285197451;
    *((unsigned int *)&g_10042668[114]) = *((int *)&g_10042668[114]) - v1;
    *((unsigned int *)&g_10042668[125]) = *((int *)&g_10042668[125]) - v1;
    *((unsigned int *)&g_10042668[152]) = *((int *)&g_10042668[152]) - v1;
    *((unsigned int *)&g_10042668[164]) = *((int *)&g_10042668[164]) - v1;
    *((unsigned int *)&g_10042668[175]) = *((int *)&g_10042668[175]) - v1;
    *((unsigned int *)&g_10042668[211]) = *((int *)&g_10042668[211]) - v1;
    *((unsigned int *)&g_10042668[244]) = *((int *)&g_10042668[244]) - v1;
    *((unsigned int *)&g_10042668[258]) = *((int *)&g_10042668[258]) - v1;
    *((unsigned int *)&g_10042668[272]) = *((int *)&g_10042668[272]) - v1;
    *((unsigned int *)&g_10042668[633]) = *((int *)&g_10042668[633]) - v1;
    *((unsigned int *)&g_10042668[644]) = *((int *)&g_10042668[644]) - v1;
    *((unsigned int *)&g_10042668[658]) = *((int *)&g_10042668[658]) - v1;
    *((unsigned int *)&g_10042668[672]) = *((int *)&g_10042668[672]) - v1;
    *((char **)&g_10042668[62]) = &g_10042674;
    *((unsigned int **)&g_10042668[120]) = &g_1004266c;
    *((char **)&g_10042668[137]) = &g_10042674;
    *((unsigned int **)&g_10042668[147]) = &g_1004266c;
    *((unsigned int **)&g_10042668[159]) = &g_1004266c;
    *((unsigned int **)&g_10042668[0xaa]) = &g_1004266c;
    *((char **)&g_10042668[229]) = &g_10042674;
    *((unsigned int **)&g_10042668[239]) = &g_1004266c;
    *((unsigned int **)&g_10042668[267]) = &g_1004266c;
    *((char **)&g_10042668[617]) = &g_10042674;
    *((unsigned int **)&g_10042668[628]) = &g_1004266c;
    *((unsigned int **)&g_10042668[639]) = &g_1004266c;
    *((unsigned int **)&g_10042668[667]) = &g_1004266c;
    *((char **)&g_10042668[200]) = &g_1004267c;
    *((char **)&g_10042668[253]) = &g_10042682;
    *((char **)&g_10042668[283]) = &g_1004267c;
    *((char **)&g_10042668[653]) = &g_10042684;
    *((char **)&g_10042668[683]) = &g_1004267e;
    g_1004266c = &g_1004267c;
    return v1;
}
```

## `sub_1002a433` `0x1002a433`

_1380 bytes. calls VirtualProtect, WriteProcessMemory_

```c
extern void g_10042668;
extern unsigned int g_100428bd;
extern unsigned int g_100428c1;
extern unsigned int g_100428c9;
extern unsigned int g_100428d1;
extern void g_1004395a;
extern unsigned int g_1004395c;
extern char g_100584f8;
extern HANDLE g_1005f612;
extern UIntPtr g_1005f622;
extern unsigned int g_1005f651;
extern unsigned int g_102898c0;

int sub_1002a433(void)
{
    enum PAGE_PROTECTION_FLAGS v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x23]

    VirtualProtect(0x401000, 0x1b7000, PAGE_EXECUTE_READWRITE, &v0);
    VirtualProtect(0x5b8000, 0x618, PAGE_READWRITE, &v0);
    *((HGLOBAL *)&g_10042668) = GlobalAlloc(GMEM_FIXED, 0x2d2);
    if (!*((int *)&g_10042668))
        ExitProcess(0); /* do not return */
    VirtualProtect(*((int *)&g_10042668), 0x2d2, PAGE_EXECUTE_READWRITE, &v0);
    sub_1002ae6f(*((int *)&g_10042668), 5213760, 722);
    sub_1002a311();
    v0 = (enum PAGE_PROTECTION_FLAGS)233;
    WriteProcessMemory(g_1005f612, 0x4f8e40, &v0, 0x1, &g_1005f622);
    v0 = (enum PAGE_PROTECTION_FLAGS)263378390;
    WriteProcessMemory(g_1005f612, 0x4f8e41, &v0, 0x4, &g_1005f622);
    g_100428d1 = *((int *)0x5b85e4);
    v0 = (enum PAGE_PROTECTION_FLAGS)sub_10026545;
    WriteProcessMemory(g_1005f612, 0x5b85e4, &v0, 0x4, NULL);
    g_100428c1 = *((int *)0x5b8428);
    v0 = (enum PAGE_PROTECTION_FLAGS)sub_10029d4e;
    WriteProcessMemory(g_1005f612, 0x5b8428, &v0, 0x4, &g_1005f622);
    g_100428bd = *((int *)0x45c3a6) + 4572074;
    v0 = (enum PAGE_PROTECTION_FLAGS)264021813;
    WriteProcessMemory(g_1005f612, 0x45c3a6, &v0, 0x4, &g_1005f622);
    v0 = (enum PAGE_PROTECTION_FLAGS)263475826;
    WriteProcessMemory(g_1005f612, 0x4f5824, &v0, 0x4, &g_1005f622);
    v0 = (enum PAGE_PROTECTION_FLAGS)233;
    WriteProcessMemory(g_1005f612, 0x459f30, &v0, 0x1, &g_1005f622);
    v0 = (enum PAGE_PROTECTION_FLAGS)264125034;
    WriteProcessMemory(g_1005f612, 0x459f31, &v0, 0x4, &g_1005f622);
    g_1004395c = "d";
    WriteProcessMemory(g_1005f612, 0x4eafa3, &g_1004395a, 0xd, NULL);
    v0 = (enum PAGE_PROTECTION_FLAGS)233;
    WriteProcessMemory(g_1005f612, 0x4d054d, &v0, 0x1, &g_1005f622);
    v0 = (enum PAGE_PROTECTION_FLAGS)263642619;
    WriteProcessMemory(g_1005f612, 0x4d054e, &v0, 0x4, &g_1005f622);
    v0 = (enum PAGE_PROTECTION_FLAGS)233;
    WriteProcessMemory(g_1005f612, 0x459fb3, &v0, 0x1, &g_1005f622);
    v0 = (enum PAGE_PROTECTION_FLAGS)264047826;
    WriteProcessMemory(g_1005f612, 0x459fb4, &v0, 0x4, &g_1005f622);
    sub_10002bdd();
    v0 = (enum PAGE_PROTECTION_FLAGS)233;
    WriteProcessMemory(g_1005f612, 0x4ecf97, &v0, 0x1, &g_1005f622);
    v0 = (enum PAGE_PROTECTION_FLAGS)263445590;
    WriteProcessMemory(g_1005f612, 0x4ecf98, &v0, 0x4, &g_1005f622);
    v0 = (enum PAGE_PROTECTION_FLAGS)233;
    WriteProcessMemory(g_1005f612, 0x4f601c, &v0, 0x1, &g_1005f622);
    v0 = (enum PAGE_PROTECTION_FLAGS)263408553;
    WriteProcessMemory(g_1005f612, 0x4f601d, &v0, 0x4, &g_1005f622);
    v0 = (enum PAGE_PROTECTION_FLAGS)233;
    WriteProcessMemory(g_1005f612, 0x4f6064, &v0, 0x1, &g_1005f622);
    v0 = (enum PAGE_PROTECTION_FLAGS)263408501;
    WriteProcessMemory(g_1005f612, 0x4f6065, &v0, 0x4, &g_1005f622);
    v0 = (enum PAGE_PROTECTION_FLAGS)233;
    WriteProcessMemory(g_1005f612, 0x4f27f6, &v0, 0x1, &g_1005f622);
    v0 = (enum PAGE_PROTECTION_FLAGS)263422876;
    WriteProcessMemory(g_1005f612, 0x4f27f7, &v0, 0x4, &g_1005f622);
    v0 = (enum PAGE_PROTECTION_FLAGS)233;
    WriteProcessMemory(g_1005f612, 0x45c7a8, &v0, 0x1, &g_1005f622);
    v0 = (enum PAGE_PROTECTION_FLAGS)264037282;
    WriteProcessMemory(g_1005f612, 0x45c7a9, &v0, 0x4, &g_1005f622);
    if (*(0x57d5bf) == 255)
    {
        g_102898c0 = *((int *)0x57d5c1);
        g_1005f651 = &g_100584f8;
        WriteProcessMemory(g_1005f612, 0x57d5c1, &g_1005f651, 0x4, NULL);
    }
    v0 = (enum PAGE_PROTECTION_FLAGS)235;
    WriteProcessMemory(g_1005f612, 0x46029d, &v0, 0x1, &g_1005f622);
    WriteProcessMemory(g_1005f612, 0x4f1ad5, &v0, 0x1, &g_1005f622);
    v0 = (enum PAGE_PROTECTION_FLAGS)233;
    v1 = 264285038;
    WriteProcessMemory(g_1005f612, 0x41ff94, &v0, 0x5, &g_1005f622);
    g_100428c9 = *((int *)0x45c6d7) + 4572891;
    v0 = (enum PAGE_PROTECTION_FLAGS)264038097;
    WriteProcessMemory(0xffffffff, 0x45c6d7, &v0, 0x4, NULL);
    v0 = (enum PAGE_PROTECTION_FLAGS)233;
    v1 = 263363432;
    WriteProcessMemory(g_1005f612, 0x500ef3, &v0, 0x5, &g_1005f622);
    v0 = (enum PAGE_PROTECTION_FLAGS)233;
    v1 = 263461125;
    WriteProcessMemory(g_1005f612, 0x4e90f9, &v0, 0x5, &g_1005f622);
    v0 = (enum PAGE_PROTECTION_FLAGS)233;
    v1 = 263601553;
    WriteProcessMemory(g_1005f612, 0x4c6d21, &v0, 0x5, &g_1005f622);
    v0 = (enum PAGE_PROTECTION_FLAGS)233;
    v1 = 264006294;
    return WriteProcessMemory(g_1005f612, 0x463efe, &v0, 0x5, &g_1005f622);
}
```

## `sub_1002a997` `0x1002a997`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002a997(void)
{
    return;
}
```

## `sub_1002a999` `0x1002a999`

_23 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005277c;

void sub_1002a999(void)
{
    if (!g_1005277c)
        4602032();
}
```

## `sub_1002a9b0` `0x1002a9b0`

_83 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[160];
    unsigned int field_a0;
} struct_0;

extern char g_1005f7e5;
extern struct_0 *g_1005f7ed;

int sub_1002a9b0(void)
{
    int v1;  // edi
    int v2;  // esi
    int v3;  // edx
    int v4;  // ecx
    int v5;  // ebx
    struct_0 *v6;  // eax
    int v0;  // [bp+0x4]

    if (v0 == *((int *)&g_1005f7e5))
        return;
    v6 = sub_1003997e(v0, v1, v2, v3, v4, v5);
    if (!v6)
        return;
    if (!g_1005f7ed->field_a0 || !v6->field_a0)
        return;
    return;
    return;
}
```

## `sub_1002aa03` `0x1002aa03`

_93 bytes. (leaf/helper — see body)_

```c
extern char g_101d5e29;
extern char g_101d5e72;
extern char g_101d5e73;

void sub_1002aa03(void)
{
    unsigned int v7;  // esi
    int v8;  // ecx
    unsigned int v1;  // [bp+0xfffd4]
    int v2;  // [bp+0xfffd8]
    unsigned int v3;  // [bp+0xfffdc]
    unsigned int v4;  // [bp+0xfffe0]
    int v5;  // [bp+0xfffe4]
    unsigned int v6;  // [bp+0xfffe8]

    v7 = v1;
    v4 = v7;
    v8 = v2;
    v5 = v8;
    if (v7 == 99 && (g_101d5e72 || g_101d5e73) && v8 < 0x40000000 && g_101d5e29 && g_101d5e72)
        sub_1002a9b0(v8);
    v6 = v3;
}
```

## `sub_1002aa60` `0x1002aa60`

_87 bytes. (leaf/helper — see body)_

```c
extern char g_101d5e29;
extern char g_101d5e72;

void sub_1002aa60(int a0, int a1)
{
    int v2;  // ecx
    unsigned int v1;  // [bp+0x100008]

    if ((v1 == 0x4e87fc || v1 == 5147309) && g_101d5e29)
    {
        v2 = a0;
        if (!v2)
            v2 = a1;
        if (v2 < 0x40000000 && !g_101d5e29 && g_101d5e72)
            sub_1002a9b0(v2);
    }
}
```

## `sub_1002aab7` `0x1002aab7`

_80 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned int field_20;
} struct_0;

extern char g_1005f88d;
extern struct_0 *g_10080b84;
extern unsigned int g_10080b88;
extern char g_100f94ca;

void sub_1002aab7(void)
{
    unsigned int v2[9];  // edi
    unsigned int v3;  // esi
    unsigned int v1;  // [bp+0xffff0]

    if (v2[2] == 8)
    {
        if (g_100f94ca && !g_1005f88d)
            v3 = v2[2];
        if (!g_10080b88 && g_10080b84 && g_10080b84->field_20 + 10 == v2[8])
            g_10080b88 = v2;
    }
    v1 = v3;
}
```

## `sub_1002ab07` `0x1002ab07`

_72 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[68];
    struct struct_1 *field_44;
} struct_0;

typedef struct struct_5 {
    struct struct_2 *field_0;
    char padding_4[32];
    struct struct_4 *field_24;
} struct_5;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

typedef struct struct_2 {
    char padding_0[40];
    struct struct_1 *field_28;
} struct_2;

typedef struct struct_4 {
    char padding_0[8];
    unsigned int field_8;
} struct_4;

extern unsigned int g_100f9109;
extern unsigned int g_100f930d;

void sub_1002ab07(unsigned int a0, struct_0 *a1)
{
    struct_5 *v1;  // esi

    a1->field_44();
    if (v1->field_24->field_8 == 7)
    {
        (&g_100f9109)[g_100f930d] = v1;
        g_100f930d = g_100f930d + 1;
        if (!v1->field_0->field_28() || g_100f930d >= 128)
            g_100f930d = 0;
    }
}
```

## `sub_1002ab4f` `0x1002ab4f`

_72 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    char padding_0[56];
    struct struct_0 *field_38;
} struct_2;

typedef struct struct_0 {
    char padding_0[56];
    unsigned int field_38;
} struct_0;

extern char g_1013f324;

void sub_1002ab4f(unsigned int a0, struct_2 *a1)
{
    struct_2 *v11;  // edx
    unsigned int v12;  // eax
    struct_2 *v13;  // ebx
    unsigned int v14;  // esi
    unsigned int v15;  // edi
    struct_0 *idx;  // ebx
    unsigned int v17;  // edi
    struct_0 *v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x1c]
    unsigned int v4;  // [bp-0x18]
    struct_2 *v5;  // [bp-0x10]
    struct_2 *v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]
    struct_2 *v8;  // [bp-0x4], Other Possible Types: unsigned int

    v11 = a1;
    if (g_1013f324)
    {
        v8 = v12;
        v7 = a0;
        v6 = a1;
        v5 = v13;
        v4 = /* unsupported instruction */;
        v3 = v14;
        v2 = v15;
        idx = a1 * 492 + 6606096;
        v17 = idx->field_38;
        idx->field_38 = 0;
        v1 = v17;
        v0 = idx;
        5052128();
        a1->field_38 = v0;
        v11 = v5;
    }
    v8 = v11;
}
```

## `sub_1002ab97` `0x1002ab97`

_51 bytes. (leaf/helper — see body)_

```c
extern char g_1013f27e;
extern unsigned int g_102e2a08;

void sub_1002ab97(void)
{
    unsigned int v2;  // cc_op
    unsigned int v3;  // cc_dep1
    unsigned int v4;  // cc_dep2
    unsigned int v5;  // cc_ndep
    unsigned int v6;  // 4138
    unsigned short v0;  // [bp-0x2]

    v6 = _ccall(v2, v3, v4, v5);
    v0 = (unsigned short)v6 | 0x202;
    if (!_INSERT(g_102e2a08, 0, (char)g_102e2a08 | g_1013f27e) && ((char)((v0 & 2261) >> 6) & 1) == 1)
        4576704();
}
```

## `sub_1002abca` `0x1002abca`

_20 bytes. (leaf/helper — see body)_

```c
void sub_1002abca(void)
{
    0x45d900();
}
```

## `sub_1002abde` `0x1002abde`

_20 bytes. (leaf/helper — see body)_

```c
void sub_1002abde(void)
{
    4577568();
}
```

## `sub_1002abf2` `0x1002abf2`

_152 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[32];
    int field_20;
} struct_0;

extern unsigned int g_100ee8d0;

void sub_1002abf2(void)
{
    unsigned int v5;  // eax
    int v6;  // ebx
    int v7;  // eax
    unsigned int v8;  // eax
    struct_0 *v9;  // edi
    int v10;  // ebx
    unsigned int v11;  // eax
    int v12;  // eax
    unsigned int v1;  // [bp+0x10000c]
    unsigned int v2;  // [bp+0x100010]
    unsigned int *v3;  // [bp+0x100014]
    int v4;  // [bp+0x100034]

    v5 = 0x45d900();
    v7 = v1 * 480 / v6 + v5;
    v8 = (v7 + (v7 >> 31 & 31) >> 5) + 1;
    if (g_100ee8d0 == 0xffffffe0)
    {
        v8 = (v8 == 1 ? 0 : v8 - 1);
    }
    else if (g_100ee8d0 == 64)
    {
        v8 += 2;
    }
    *(v3) = v8;
    v10 = v9->field_20;
    v4 = v10;
    v11 = 4577568();
    v12 = v2 * 352 / v10 + v11;
}
```

## `sub_1002ac8a` `0x1002ac8a`

_85 bytes. calls SendMessageA_

```c
extern char g_1005db74;
extern char g_100ee8bb;

void sub_1002ac8a(int a0, int a1)
{
    int v2;  // edi
    int v3;  // esi
    int v4;  // ebx
    char v0;  // [bp+0x0]

    if (a0 != v2 && g_100ee8bb && *((int *)0x64a9c0) == 31 && g_1005db74)
    {
        SendMessageA(sub_10039b62(v2, v3, /* unsupported instruction */, &v0, v4, a1, a0, 6597056), 258, 0x1b, NULL);
        g_1005db74 = 0;
    }
}
```

## `sub_1002acdf` `0x1002acdf`

_117 bytes. (leaf/helper — see body)_

```c
typedef struct LIST_ENTRY {
    void* Flink;
    void* Blink;
} LIST_ENTRY;

typedef struct CRITICAL_SECTION_DEBUG {
    unsigned short Type;
    unsigned short CreatorBackTraceIndex;
    void* CriticalSection;
    LIST_ENTRY ProcessLocksList;
    unsigned int EntryCount;
    unsigned int ContentionCount;
    unsigned int Flags;
    unsigned short CreatorBackTraceIndexHigh;
    unsigned short Identifier;
} CRITICAL_SECTION_DEBUG;

typedef struct CRITICAL_SECTION {
    struct CRITICAL_SECTION_DEBUG *DebugInfo;
    int LockCount;
    int RecursionCount;
    HANDLE OwningThread;
    HANDLE LockSemaphore;
    UIntPtr SpinCount;
} CRITICAL_SECTION;

extern CRITICAL_SECTION g_1004287d;
extern SOCKET g_1005f555;
extern char g_1008b8a3;
extern unsigned int g_1008b8a4;

int sub_1002acdf(unsigned int a0, PSTR a1, int a2, enum SEND_RECV_FLAGS a3)
{
    int count;  // eax
    unsigned int v12;  // ecx
    unsigned int v13;  // edx
    unsigned int v14;  // ebx
    unsigned int v15;  // esi
    unsigned int v16;  // edi
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    char *v2;  // [bp-0x20]
    char *v3;  // [bp-0x1c]
    unsigned int v4;  // [bp-0x18]
    unsigned int v5;  // [bp-0x14]
    unsigned int v6;  // [bp-0x10]
    int v7;  // [bp-0xc], Other Possible Types: unsigned int
    char v8;  // [bp-0x8]
    char v9;  // [bp-0x5]
    char v10;  // [bp-0x4]

    v9 = 0;
    if (g_1008b8a3)
    {
        EnterCriticalSection(&g_1004287d.DebugInfo);
        v9 = 1;
    }
    if (g_1005f555)
    {
        count = send(g_1005f555, a1, a2, a3);
        g_1005f555 = count;
    }
    else
    {
        v7 = a0;
        g_1008b8a4 = a0;
        count = send(a0, a1, a2, a3);
    }
    if (!v9)
        return count;
    v7 = count;
    v6 = v12;
    v5 = v13;
    v4 = v14;
    v3 = &v8;
    v2 = &v10;
    v1 = v15;
    v0 = v16;
    LeaveCriticalSection(&g_1004287d.DebugInfo);
    return count;
}
```

## `sub_1002ad54` `0x1002ad54`

_35 bytes. (leaf/helper — see body)_

```c
int sub_1002ad54(void)
{
    char *i;  // esi
    unsigned int v5;  // ecx
    char *v0;  // [bp-0x1c]
    char *v1;  // [bp-0x18]
    char v2;  // [bp-0x4]
    char *iter;  // [bp+0x4]

    v1 = &v2;
    v0 = &v2;
    i = 0x74f1ac;
    for (v5 = 16; v5; i += 1)
    {
        v5 -= 1;
        *(iter) = *(i);
        iter += 1;
    }
    return;
}
```

## `sub_1002ad6b` `0x1002ad6b`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002ad6b(void)
{
}
```

