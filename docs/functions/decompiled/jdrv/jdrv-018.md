# elfbot.dll decompiled — jdrv 0x1003a720..0x1003c99f

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1003a720` `0x1003a720`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1003a720(void)
{
}
```

## `sub_1003a736` `0x1003a736`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1003a736(void)
{
}
```

## `sub_1003a74c` `0x1003a74c`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1003a74c(void)
{
}
```

## `sub_1003a762` `0x1003a762`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1003a762(void)
{
}
```

## `sub_1003a778` `0x1003a778`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1003a778(void)
{
}
```

## `sub_1003a78e` `0x1003a78e`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1003a78e(void)
{
}
```

## `sub_1003a7a4` `0x1003a7a4`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1003a7a4(void)
{
}
```

## `sub_1003a7ba` `0x1003a7ba`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1003a7ba(void)
{
}
```

## `sub_1003a7d0` `0x1003a7d0`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1003a7d0(void)
{
}
```

## `sub_1003a7e6` `0x1003a7e6`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1003a7e6(void)
{
}
```

## `sub_1003aa9a` `0x1003aa9a`

_1334 bytes. refs "%d/%d", "M %d/%d", "%d/%d"_

```c
typedef struct struct_0 {
    char field_0;
    char padding_1[63];
    struct struct_1 *field_40;
    char padding_44[4];
    unsigned int field_48;
    char field_4c;
    char padding_4d[4];
    char field_51;
    unsigned short field_52;
    unsigned short field_54;
    unsigned short field_56;
    unsigned short field_58;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
    char padding_4[132];
    unsigned int field_88;
} struct_1;

extern char g_1005a014;
extern struct_0 g_1005f645;
extern struct_0 g_1005f651;
extern char g_1005f8a4;
extern char g_1005f8a5;
extern unsigned int g_10080b05;
extern char g_10080b06;
extern unsigned int g_10080b08;
extern unsigned int g_10080b09;
extern char g_10080b4d;
extern unsigned int g_10080b70;
extern unsigned int g_10080b74;
extern unsigned int g_10080b78;
extern unsigned int g_10080b7c;
extern unsigned int g_10080b80;
extern unsigned int g_10080b84;
extern unsigned int g_10080b8c;
extern unsigned int g_10080b90;
extern unsigned int g_1008b8f4;
extern unsigned int g_1008b8f8;
extern unsigned int g_1008b8fc;
extern char g_1008d330;
extern char g_1008d344;
extern char g_1008d350;
extern char g_1008d352;
extern char g_1008d354;
extern char g_100f94c8;
extern char g_100fa579;
extern char g_1013526e;
extern char g_1013526f;
extern char g_10135270;
extern char g_10135275;

int sub_1003aa9a(unsigned int a0, struct_0 *a1, struct_0 *a2)
{
    unsigned int v7;  // ebx
    unsigned int v8;  // esi
    int v16;  // ecx
    struct_0 *v17;  // edi
    struct_0 *i;  // eax
    unsigned int iter;  // ebx
    struct_0 *v20;  // eax
    struct_0 *j;  // eax
    unsigned int node;  // ebx
    struct_0 *k;  // eax
    struct_0 *v24;  // eax
    int v25;  // ecx
    unsigned int v9;  // edi
    unsigned int v26;  // ecx
    char v27;  // cl
    struct_0 *v28;  // eax
    struct_0 *v29;  // edx
    unsigned int iter1;  // ecx
    struct_0 *idx;  // esi
    struct_0 *v32;  // eax
    unsigned int m;  // ecx
    struct_0 *v10;  // eax
    unsigned int v34;  // edi
    struct_0 *v11;  // ebx
    unsigned int v12;  // edx
    char v13;  // cl
    unsigned int v14;  // edi
    unsigned int iter2;  // ebx
    unsigned int v0;  // [bp-0x20]
    struct_0 *v1;  // [bp-0x1c], Other Possible Types: unsigned int
    struct_0 *v2;  // [bp-0x18]
    struct_0 *v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    struct_0 *v5;  // [bp-0x4], Other Possible Types: unsigned int
    struct_0 *v6;  // [bp+0x0]

    g_1005a014 = 0;
    g_10080b70 = v7;
    g_10080b74 = v8;
    g_10080b84 = v8;
    g_10080b78 = v9;
    g_10080b8c = 0;
    v10 = sub_1003ba2f();
    idx = v10;
    v11 = v6;
    g_10080b7c = a2;
    g_10080b90 = 0;
    if (!g_1005a014 && v12 && v10)
    {
        v6 = v11;
        v13 = idx->field_4c;
        if (!idx->field_4c)
        {
            g_10080b05 = 1277187662;
            v14 = 5;
        }
        else if (v13 == 1)
        {
            g_10080b05 = 541859915;
            v14 = 15;
        }
        else if (v13 == 2)
        {
            g_10080b05 = 541859920;
            v14 = 10;
        }
        else if (v13 == 3)
        {
            g_10080b05 = 541859923;
            v14 = 5;
            g_10080b90 = 30;
        }
        else if (v13 == 4)
        {
            g_10080b05 = 541859908;
            v14 = 5;
            g_10080b90 = 30;
        }
        else if (v13 == 5)
        {
            g_10080b05 = 1277184837;
            v14 = 15;
        }
        else if (v13 == 6)
        {
            g_10080b05 = 1277186130;
            v14 = 10;
        }
        else if (v13 == 7)
        {
            g_10080b05 = 1277186893;
            v14 = 5;
            g_10080b90 = 30;
        }
        else if (v13 == 8)
        {
            g_10080b05 = 1277183045;
            v14 = 5;
            g_10080b90 = 30;
        }
        iter2 = &g_10080b09;
        if (g_10080b06 == 32)
            iter2 = &g_10080b08;
        v16 = idx->field_48;
        v17 = (v16 < 8 ? v16 * 5 + 145 : (v16 - 8) * v14 + 185);
        sub_10040940(v16, &g_1005f651.field_0);
        for (i = &g_1005f651.field_0; i->field_0; i = i->padding_1)
        {
            *((char *)iter2) = i->field_0;
            iter2 += 1;
        }
        *((char *)iter2) = 32;
        iter = iter2 + 1;
        v20 = (int)(v17 * idx->field_40->field_88 / 100);
        idx->field_52 = *((unsigned short *)&v17);
        idx->field_54 = *((unsigned short *)&v20);
        v3 = &g_1005f651.field_0;
        sub_10040940(v20, &g_1005f651.field_0);
        for (j = &g_1005f651.field_0; j->field_0; j = j->padding_1)
        {
            *((char *)iter) = j->field_0;
            iter += 1;
        }
        *((char *)iter) = 47;
        node = iter + 1;
        sub_10040940(v17, &g_1005f651.field_0);
        for (k = &g_1005f651.field_0; k->field_0; k = k->padding_1)
        {
            *((char *)node) = k->field_0;
            node += 1;
        }
        *((char *)node) = 0;
        v11 = v17;
        if (g_1013526f)
        {
            a1 = &g_10080b05;
            4935120();
            v3 = &g_1005f645.field_0;
            g_10080b8c = g_10080b8c + 12;
        }
        v24 = &idx->padding_1[31];
        if (v24->field_0 && g_1013526e)
        {
            a1 = v24;
            4935120();
            v3 = &v3->padding_1[11];
            g_10080b8c = g_10080b8c + 12;
        }
        a1 = idx;
        if (g_10080b90)
        {
            v25 = idx->field_48;
            v26 = (v25 < 8 ? v25 * 5 : g_10080b90 * (v25 - 8) + 35);
            idx->field_56 = v26;
            v2 = idx;
            v1 = v26;
            v0 = v1 - idx->field_58;
            wsprintfA(&g_10080b4d, "%d/%d");
            v2 = idx;
            v1 = v11;
            g_10080b80 = sub_10028cf5() + 6;
            v11 = v1;
            v10 = idx;
        }
        else
        {
            g_10080b80 = 0;
            v10 = idx;
        }
    }
    else
    {
        g_10080b80 = 0;
    }
    if (!v10 || g_1005f8a4 || g_1005f8a5)
        return 4935120();
    v27 = idx->field_51;
    if (idx->field_51)
    {
        v28 = a2;
        v29 = &a1->padding_1[11];
        v6 = idx;
        v5 = v11;
        if (v27 == 1)
        {
            g_1008b8f4 = 64;
            g_1008b8f8 = 128;
            g_1008b8fc = 0xff;
            sub_1003b127(v29, v28, "F");
            v3 = v28;
            v20 = v29;
        }
        else if (v27 == 2)
        {
            g_1008b8f4 = 0xff;
            g_1008b8f8 = 0;
            g_1008b8fc = 0;
            sub_1003b127(v29, v28, "E");
            v3 = v28;
            v20 = v29;
        }
        else if (v27 == 3)
        {
            g_1008b8f4 = 64;
            g_1008b8f8 = 128;
            g_1008b8fc = 0xff;
            v20 = &v29->padding_1[5];
            sub_1003b127(&v29->padding_1[5], v28, "SF");
            v3 = v28;
        }
        else
        {
            v3 = v3;
            v20 = v20;
            if (v27 == 4)
            {
                g_1008b8f4 = 0xff;
                g_1008b8f8 = 0;
                g_1008b8fc = 0;
                v20 = &v29->padding_1[5];
                sub_1003b127(&v29->padding_1[5], v28, "SE");
                v3 = v28;
            }
        }
        v11 = v20;
        idx = v3;
    }
    if (g_100f94c8)
    {
        if (idx->field_40)
        {
            iter1 = 0;
            while (iter1 < 0x6a00)
            {
                if (*((int *)&(&g_1008d354)[iter1]) != idx->field_40->field_0 || *((int *)&(&g_1008d330)[iter1]) <= 280)
                {
                    iter1 += 106;
                }
                else
                {
                    v6 = idx;
                    if (((&g_1008d344)[iter1] & 2))
                    {
                        v5 = *((short *)&(&g_1008d352)[iter1]);
                        v4 = *((short *)&(&g_1008d350)[iter1]);
                        wsprintfA(&g_10080b4d, "M %d/%d");
                    }
                    else
                    {
                        wsprintfA(&g_10080b4d, "%d/%d");
                    }
                    g_1008b8f4 = 64;
                    g_1008b8f8 = 128;
                    g_1008b8fc = 0xff;
                    goto LABEL_1003af39;
                }
            }
            goto LABEL_1003af39;
        }
        if (!g_10080b90 || !g_10135270)
            goto LABEL_1003af6d;
        g_1008b8f4 = 0xff;
        g_1008b8f8 = 165;
        g_1008b8fc = 0;
LABEL_1003af39:
        v32 = &a2->padding_1[15 + g_10080b8c];
        sub_1003b127(a1, v32, &g_10080b4d, v11, idx);
        g_10080b80 = sub_10028cf5() + 6;
        idx = v32;
    }
LABEL_1003af6d:
    if (g_100fa579 && g_10135275)
    {
        m = 0;
        for (v34 = 0; m < 10; m += 1)
        {
            v34 = _INSERT(v34, 0, (unsigned short)v34 + *((short *)&idx[1].padding_1[1 + 2 * m]));
        }
        g_10080b7c = g_10080b7c + 16;
        if (v34 >= 10)
            return sub_1003afb0();
    }
    return 4935120();
}
```

## `sub_1003ad4a` `0x1003ad4a`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1003ad4a(void)
{
}
```

## `sub_1003afb0` `0x1003afb0`

_82 bytes. refs "-%d%c/s"_

```c
extern char g_10080b4d;
extern unsigned int g_1008b8f4;
extern unsigned int g_1008b8f8;
extern unsigned int g_1008b8fc;

int sub_1003afb0(void)
{
    unsigned int v7;  // esi
    unsigned int v8;  // ebx
    int v9;  // edx
    int v10;  // eax
    unsigned int v11;  // edi
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    int v2;  // [bp-0x10]
    int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    unsigned int v5;  // [bp-0x4]

    v5 = v7;
    v4 = v8;
    v3 = v9;
    v2 = v10;
    v1 = 37;
    v0 = v11 / 10;
    wsprintfA(&g_10080b4d, "-%d%c/s");
    g_1008b8f4 = 0xff;
    g_1008b8f8 = 0;
    g_1008b8fc = 0;
    sub_1003b127(v9, v10, &g_10080b4d);
}
```

## `sub_1003b007` `0x1003b007`

_201 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[142];
    char field_8e;
} struct_0;

typedef struct struct_1 {
    char padding_0[143];
    char field_8f;
} struct_1;

extern int g_100429fa;
extern struct_1 *g_10080b7c;
extern unsigned int g_10080b80;
extern unsigned int g_1008b8f4;
extern unsigned int g_1008b8f8;
extern unsigned int g_1008b8fc;
extern char g_1008b900;

int sub_1003b007(unsigned int a0)
{
    struct_0 *v0;  // esi
    int v1;  // edx
    int v2;  // ebx
    int v3;  // ebx
    struct_1 *v4;  // esi
    int v5;  // edx

    g_10080b80 = 6;
    if (v0->field_8e)
    {
        v1 = a0 + g_10080b80;
        g_10080b80 = g_10080b80 + 24;
        g_1008b900 = 1;
        g_1008b8f4 = 0xff;
        g_1008b8f8 = 80;
        g_1008b8fc = 80;
        sub_1003b159(v1, g_10080b7c, &g_100429fa, v0->field_8e, v2, v0);
        g_1008b900 = 0;
        v3 = v1;
        v4 = g_10080b7c;
    }
    if (!v4->field_8f)
        goto LABEL_0x1003b0d0;
    v5 = a0 + g_10080b80;
    g_1008b900 = 1;
    g_1008b8f4 = 100;
    g_1008b8f8 = 100;
    g_1008b8fc = 100;
    sub_1003b159(v5, g_10080b7c, &g_100429fa, v4->field_8f, v3, v4);
    g_1008b900 = 0;
}
```

## `sub_1003b0f0` `0x1003b0f0`

_55 bytes. (leaf/helper — see body)_

```c
extern char g_1008d2ee;
extern char g_1008d330;
extern char g_1008d354;

unsigned int sub_1003b0f0(unsigned int a0)
{
    unsigned int i;  // eax

    for (i = 0; i < 0x6a00; i += 106)
    {
        if (*((int *)&(&g_1008d354)[i]) == a0 && *((int *)&(&g_1008d330)[i]) > 280)
            return &(&g_1008d2ee)[i];
    }
    return 0;
}
```

## `sub_1003b127` `0x1003b127`

_50 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1008b8f4;
extern unsigned int g_1008b8f8;
extern unsigned int g_1008b8fc;

int sub_1003b127(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x1c]
    unsigned int v4;  // [bp-0x18]
    unsigned int v5;  // [bp-0x14]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]

    v8 = 0;
    v7 = a2;
    v6 = g_1008b8fc;
    v5 = g_1008b8f8;
    v4 = g_1008b8f4;
    v3 = 2;
    v2 = a1;
    v1 = a0;
    v0 = 1;
    return 4935120();
}
```

## `sub_1003b159` `0x1003b159`

_210 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
    unsigned short field_1;
} struct_0;

extern unsigned int g_1008b8f4;
extern unsigned int g_1008b8f8;
extern unsigned int g_1008b8fc;
extern char g_1008b900;

int sub_1003b159(unsigned int a0, unsigned int a1, int a2, unsigned int a3)
{
    unsigned int v13;  // ebx
    unsigned int v14;  // eax
    unsigned int v15;  // eax
    unsigned int v16;  // edx
    struct_0 *dst;  // eax
    unsigned int v0;  // [bp-0x9c]
    unsigned int v1;  // [bp-0x98]
    unsigned int v2;  // [bp-0x94]
    unsigned int v3;  // [bp-0x90]
    unsigned int v4;  // [bp-0x8c]
    unsigned int v5;  // [bp-0x88]
    unsigned int v6;  // [bp-0x84]
    char *v7;  // [bp-0x80]
    unsigned int v8;  // [bp-0x7c]
    unsigned int v9;  // [bp-0x74]
    unsigned int v10;  // [bp-0x68]
    char v11;  // [bp-0x64]
    char v12;  // [bp-0x44]

    v10 = v13;
    lstrcpy(&v12, a2);
    v14 = a3;
    v15 = v14;
    if (v15 >= 600)
    {
        sub_10040940(v14 / 600, &v11, v14 % 600);
        lstrcat(&v12, &v11);
        v16 = v14 / 600;
        v9 = v14 / 600;
        if (v16 < 100)
            lstrcat(&v12, ":0");
        else
            lstrcat(&v12, ":");
        v15 = v16;
    }
    sub_10040940(v15 / 10, &v11, v15 % 10);
    for (dst = lstrcat(&v12, &v11); dst->field_0; dst = &(&dst->field_0)[1]);
    if (g_1008b900)
    {
        dst->field_0 = 46;
        *((unsigned short *)&(&dst->field_0)[1]) = _INSERT(v15 / 10, 0, (char)(v15 / 10) + 48);
    }
    v8 = 0;
    v7 = &v12;
    v6 = g_1008b8fc;
    v5 = g_1008b8f8;
    v4 = g_1008b8f4;
    v3 = 2;
    v2 = a1;
    v1 = a0;
    v0 = 1;
    return 4935120();
}
```

## `sub_1003b22b` `0x1003b22b`

_2042 bytes. refs "lmouse", "%s: %s", "cb%d: %s"_

```c
typedef struct struct_0 {
    char field_0;
    char padding_1[255];
    unsigned int field_100;
    unsigned int field_104;
    unsigned int field_108;
    unsigned int field_10c;
    unsigned int field_110;
} struct_0;

typedef struct struct_2 {
    char padding_0[1];
    char field_1;
} struct_2;

typedef struct struct_3 {
    unsigned int field_0;
    unsigned int field_4;
    char padding_8[8];
    unsigned int field_10;
    unsigned int field_14;
    unsigned int field_18;
} struct_3;

typedef struct struct_5 {
    char padding_0[28];
    char field_1c;
    char padding_1d[511];
    unsigned int field_21c;
} struct_5;

extern char g_100445f0;
extern unsigned int g_10084c0b[4];
extern unsigned int g_1008b8dc;
extern unsigned int g_1008b8e0;
extern unsigned int g_1008b8e4;
extern unsigned int g_1008b8ec;
extern unsigned int g_1008b8f0;
extern void g_1008b8f4;
extern void g_1008b8f8;
extern unsigned int g_1008b8fc;
extern char g_1008b900;
extern int g_1008b921;
extern unsigned int g_1008b941;
extern unsigned int g_1008b945[4];
extern char g_1008b96d;
extern int g_1008baad;
extern char g_1009a536;
extern char g_100ba736[4];
extern char g_100f0e42;
extern struct_3 *g_100f49f1;
extern unsigned int g_100f49fd;
extern unsigned int g_100f4a01;
extern char g_100f933a;
extern char g_100faa3c[4];
extern char g_10106b02;
extern char g_10135271;
extern char g_10135272;
extern char g_10135276;
extern char g_1013527a;
extern char g_1013f32b;
extern char g_1014f420;
extern char g_101d5e26;

unsigned int sub_1003b22b(void)
{
    unsigned int idx;  // ebx
    unsigned int v12[4];  // eax
    unsigned int v21;  // esi
    unsigned int v22;  // eax
    unsigned int v23;  // ebx
    struct_0 *index;  // ecx
    int v25;  // ebx
    unsigned int iter[7];  // ebx, Other Possible Types: struct_3 *
    unsigned int v27;  // ecx
    unsigned int v28;  // ecx
    unsigned int v29;  // esi
    struct_0 *idx1;  // ecx
    struct_5 *v30;  // eax
    unsigned int v31;  // edx
    unsigned int v32;  // edx
    unsigned int node;  // ebx
    unsigned int v34;  // ebx
    unsigned int idx2;  // ecx
    char v14[2];  // ebx
    unsigned int v15;  // ecx
    char *v16;  // esi
    char *v17;  // edi
    struct_2 *v18;  // ebx
    unsigned int v19;  // ecx
    unsigned int v20;  // eax
    unsigned int v0;  // [bp-0xc18]
    unsigned int v1;  // [bp-0xc14]
    char *v2;  // [bp-0xc10], Other Possible Types: struct_3 *, unsigned int [4], unsigned int
    char v3[2];  // [bp-0xc0c], Other Possible Types: struct_2 *, unsigned int
    unsigned int count;  // [bp-0xc00]
    char v5;  // [bp-0xbfc]
    char v6;  // [bp-0xbfb]
    unsigned int iter1;  // [bp-0xbdc]
    unsigned int iter2;  // [bp-0xbd8]
    Byte v9[3024];  // [bp-0xbd4]

    if (g_1013527a)
    {
        iter1 = 16;
        iter2 = 0;
        while (true)
        {
            if (iter2 >= 736)
            {
                iter2 = 0;
                while (iter2 < 128)
                {
                    v23 = iter2 + 96;
                    if (g_10084c0b[v23])
                    {
                        index = &g_100ba736[276 * v23];
                        v3 = index->field_108;
                        *((unsigned int *)&g_1008b8f4) = index->field_108;
                        v3 = index->field_10c;
                        *((unsigned int *)&g_1008b8f8) = index->field_10c;
                        v3 = index->field_110;
                        g_1008b8fc = index->field_110;
                        if (!index->field_0)
                        {
                            v25 = &(&g_10106b02)[546 * iter2];
                            lstrcpy(v9, v25);
                            lstrcat(v9, ": ");
                            lstrcat(v9, v25 + 0x22);
                            sub_1003b127(425, iter1, v9);
                            iter1 += 12;
                            iter2 += 1;
                        }
                        else if (index->field_0 == 2)
                        {
                            iter2 += 1;
                        }
                        else if (index->field_0 == 3)
                        {
                            sub_1003b127(425, iter1, index->padding_1);
                            iter1 += 12;
                            iter2 += 1;
                        }
                        else
                        {
                            sub_1003b127(index->field_100, index->field_104, index);
                            iter2 += 1;
                        }
                    }
                    else
                    {
                        iter2 += 1;
                    }
                }
            }
            idx = iter2;
            v12 = g_10084c0b[idx];
            idx1 = &g_100ba736[276 * idx];
            v3 = idx1->field_108;
            *((unsigned int *)&g_1008b8f4) = idx1->field_108;
            v3 = idx1->field_10c;
            *((unsigned int *)&g_1008b8f8) = idx1->field_10c;
            v3 = idx1->field_110;
            g_1008b8fc = idx1->field_110;
            if (v12 || idx1->field_0)
            {
                if (idx1->field_0)
                {
                    if (idx1->field_0 != 2)
                    {
                        if (idx1->field_0 == 3)
                        {
                            sub_1003b127(425, iter1, idx1->padding_1);
                            iter1 += 12;
                        }
                        else
                        {
                            sub_1003b127(idx1->field_100, idx1->field_104, idx1);
                        }
                    }
                }
                else
                {
                    if (iter2 < 96)
                    {
                        v14 = &g_100faa3c[0x202 * idx];
                        v15 = v14[0];
                        if (v14[1])
                        {
                            v16 = "lmouse";
                            while (true)
                            {
                                if (v16 < &g_100445f0)
                                {
                                    if (v16[15] == (char)v15)
                                    {
                                        v17 = v16;
                                        break;
                                    }
                                    else
                                    {
                                        v16 += 16;
                                    }
                                }
                                else
                                {
                                    if (v15)
                                    {
                                        v5 = 35;
                                        sub_10040940(v15, &v6);
                                    }
                                    else
                                    {
                                        v5 = 0;
                                    }
                                    v17 = &v5;
                                    break;
                                }
                            }
                            v3 = v14 + 1;
                            v2 = v17;
                            wsprintfA(v9, "%s: %s");
                            goto LABEL_1003b450;
                        }
                    }
                    else if (iter2 < 480)
                    {
                        v18 = &(&g_1009a536)[115136 + 0x202 * idx];
                        if (v18->field_1)
                        {
                            v19 = iter2;
                            if (v19 < 352)
                            {
                                v3 = v18 + 1;
                                v2 = v19 - 223;
                                wsprintfA(v9, "cb%d: %s");
                                goto LABEL_1003b450;
                            }
                            else
                            {
                                v3 = v18 + 1;
                                v2 = v19 - 351;
                                wsprintfA(v9, "pb%d: %s");
                                goto LABEL_1003b450;
                            }
                        }
                    }
                    else
                    {
                        v20 = idx - 480;
                        v21 = 76;
                        if (v20 >= 128)
                        {
                            v20 -= 128;
                            v21 = 2076;
                        }
                        v22 = &(&g_1014f420)[v20 * 4308];
                        if (*((int *)(v22 + 0x44)) && *((char *)(v21 + v22)))
                        {
                            v3 = v21 + v22;
                            v2 = v22;
                            wsprintfA(v9, "%s: %s");
LABEL_1003b450:
                            sub_1003b127(425, iter1, v9);
                            iter1 += 12;
                        }
                    }
                }
            }
            iter2 += 1;
            if (iter2 == 96)
            {
                iter2 = 224;
                if (!g_100f0e42)
                    iter2 = 352;
            }
            if (iter2 == 352 && !g_1013f32b)
                iter2 = 480;
            if (iter2 == 480 && !g_101d5e26)
                iter2 = 736;
        }
    }
    count = GetTickCount();
    iter = g_100f49f1;
    for (v27 = 0; v27 < 32; iter = iter[595].padding_8)
    {
        if (iter[2] >= count)
        {
            v3 = v27;
            v28 = iter[6];
            v29 = iter[5];
            if (!iter[5])
                v29 = iter[5] + 1;
            v2 = iter[1];
            iter1 = iter[1];
            do
            {
                v28 -= 1;
                if (v28 > 31)
                    v28 = 31;
                v30 = 28 + 520 * v28 + (char *)iter;
                if (*((int *)&v30->padding_1d[487]) >= count)
                {
                    if (iter->field_10)
                        iter1 -= 12;
                    if (v30->padding_0[0])
                    {
                        v31 = *((int *)&v30->padding_1d[483]);
                        g_1008b8f4 = v31;
                        v32 = v31 >> 8;
                        g_1008b8f8 = v32;
                        *((char *)&g_1008b8fc) = v32 >> 8;
                        v2 = iter;
                        v1 = v28;
                        v0 = v29;
                        sub_1003b127(iter->field_0, iter1, v30);
                    }
                    if (!iter->field_10)
                        iter1 += 12;
                }
                v29 -= 1;
            } while (v28 != iter->field_18 && v29);
        }
        v27 += 1;
    }
    g_1008b900 = 1;
    if (g_10135271)
    {
        *((unsigned int *)&g_1008b8f4) = 200;
        *((unsigned int *)&g_1008b8f8) = 200;
        g_1008b8fc = 200;
        sub_1003b127(16, 16, "Ping  :   ");
        sub_1003b127(16, 28, "Exph :   ");
        sub_1003b127(116, 16, "Stime  :   ");
        sub_1003b127(116, 28, "Target :   None");
    }
    node = 16;
    if (g_10135276)
    {
        if (g_1008b8dc)
        {
            *((unsigned int *)&g_1008b8f4) = 100;
            *((unsigned int *)&g_1008b8f8) = 100;
            g_1008b8fc = 0xff;
            sub_1003b159(316, 16, "MShield : ", g_1008b8dc);
            node = 28;
        }
        if (g_1008b8e0)
        {
            *((unsigned int *)&g_1008b8f4) = 0xff;
            *((unsigned int *)&g_1008b8f8) = 100;
            g_1008b8fc = 0xff;
            sub_1003b159(316, node, "Invis  : ", g_1008b8e0);
            node += 12;
        }
        if (g_1008b8e4)
        {
            *((unsigned int *)&g_1008b8f4) = 0xff;
            *((unsigned int *)&g_1008b8f8) = 0xff;
            g_1008b8fc = 100;
            sub_1003b159(316, node, "Mwall  : ", g_1008b8e4);
            node += 12;
        }
        if (g_1008b8ec)
        {
            *((unsigned int *)&g_1008b8f4) = 100;
            *((unsigned int *)&g_1008b8f8) = 0xff;
            g_1008b8fc = 100;
            sub_1003b159(316, node, "Haste  : ", g_1008b8ec);
            node += 12;
        }
        if (g_1008b8f0)
        {
            *((unsigned int *)&g_1008b8f4) = 0xff;
            *((unsigned int *)&g_1008b8f8) = 70;
            g_1008b8fc = 70;
            sub_1003b159(316, node, "Strength  : ", g_1008b8f0);
            node += 12;
        }
        if (g_100f49fd)
        {
            *((unsigned int *)&g_1008b8f4) = 225;
            *((unsigned int *)&g_1008b8f8) = 100;
            g_1008b8fc = 225;
            sub_1003b159(316, node, "SBoots  : ", g_100f49fd / 100);
            node += 12;
        }
        if (g_100f4a01)
        {
            *((unsigned int *)&g_1008b8f4) = 247;
            *((unsigned int *)&g_1008b8f8) = 95;
            g_1008b8fc = 95;
            sub_1003b159(316, node, "SSave  : ", g_100f4a01 / 100);
            node += 12;
        }
        if (g_100f933a > 3)
        {
            *((unsigned int *)&g_1008b8f4) = 0xff;
            *((unsigned int *)&g_1008b8f8) = 0xff;
            g_1008b8fc = 0xff;
            sub_1003b159(316, node, "Sync   : ", g_100f933a - 3);
        }
    }
    v34 = 52;
    g_1008b900 = 0;
    *((unsigned int *)&g_1008b8f4) = 0xff;
    *((unsigned int *)&g_1008b8f8) = 100;
    g_1008b8fc = 100;
    if (!g_10135272)
        return sub_10028d0c();
    if (g_1008b941)
    {
        lstrcpy(&g_1008baad, &g_1008b921);
        lstrcat(&g_1008baad, " : ");
        sub_1003b159(16, 52, &g_1008baad, g_1008b941);
        v34 = 0x44;
    }
    for (idx2 = 0; idx2 < 10; idx2 += 1)
    {
        v3 = idx2;
        if (g_1008b945[idx2])
        {
            v2 = g_1008b945[idx2];
            lstrcpy(&g_1008baad, &(&g_1008b96d)[32 * idx2]);
            lstrcat(&g_1008baad, " : ");
            sub_1003b159(16, v34, &g_1008baad, g_1008b945[idx2]);
            v34 += 12;
        }
    }
    return sub_10028d0c();
}
```

## `sub_1003b2b5` `0x1003b2b5`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1003b2b5(void)
{
}
```

## `sub_1003b550` `0x1003b550`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1003b550(void)
{
}
```

## `sub_1003ba2f` `0x1003ba2f`

_230 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[64];
    void* field_40;
    unsigned int field_44;
    char padding_48[4];
    char field_4c;
    char field_4d;
    char field_4e;
    char field_4f;
    char field_50;
    char padding_51[7];
    unsigned short field_58;
    unsigned short field_5a;
} struct_0;

extern char g_1005f7ed;
extern char g_10080b6f;
extern char g_101d5e21;

struct_0 * sub_1003ba2f(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, void* a8)
{
    void* v10;  // eax
    void* v11;  // ebx
    struct_0 *index;  // eax
    struct_0 *idx;  // eax
    struct_0 *idx1;  // eax
    void* v15;  // edx
    unsigned int v16;  // ebx
    unsigned int v17;  // esi
    unsigned int v18;  // edi
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    char *v2;  // [bp-0x20]
    char *v3;  // [bp-0x1c]
    unsigned int v4;  // [bp-0x18]
    void* v5;  // [bp-0x14]
    unsigned int v6;  // [bp-0x10]
    struct_0 *v7;  // [bp-0xc]
    struct_0 *v8;  // [bp-0x8]
    char v9;  // [bp-0x4]

    g_10080b6f = 3;
    v10 = a8 - 4;
    if ((char)v10[3] != 64 && v10 != *((int *)&g_1005f7ed))
    {
        v11 = v10;
        v8 = sub_10023861();
        if (v8->field_44 != *((int *)v11))
        {
            sub_1002ae81(v8, 156);
            sub_1002ae6f(v8, v11 + 4, 32);
            idx = v8;
            idx->field_4d = 1;
            idx->field_4f = 1;
            idx->field_4e = 0;
            idx->field_50 = 0;
            idx->field_44 = *((int *)v11);
            idx->field_40 = v11;
            idx->field_58 = 0;
            idx->field_5a = 0;
            idx->field_4c = 0;
            return idx;
        }
        index = v8;
        if (index->field_4e)
            return index;
        if (!g_101d5e21 && index->field_50)
            return index;
        if (g_101d5e21 && index->field_50)
        {
            index->field_4d = 1;
            return index;
        }
        index->field_4d = 1;
        return index;
    }
    idx1 = sub_10023861(v10);
    v15 = v10;
    if (idx1->field_44 != *((int *)v15))
    {
        v7 = idx1;
        v6 = *((int *)v15);
        v5 = v15;
        v4 = v16;
        v3 = &v8;
        v2 = &v9;
        v1 = v17;
        v0 = v18;
        sub_1002ae81(idx1, 156);
        idx1->field_44 = *((int *)v15);
    }
    idx1->field_40 = v15;
    return idx1;
}
```

## `sub_1003baa6` `0x1003baa6`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003baa6(void)
{
    sub_1003bb1b();
    return;
}
```

## `sub_1003bac2` `0x1003bac2`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003bac2(void)
{
    sub_1003bb1b();
    return;
}
```

## `sub_1003bacc` `0x1003bacc`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003bacc(void)
{
    sub_1003bb1b();
    return;
}
```

## `sub_1003bb1b` `0x1003bb1b`

_7 bytes. (leaf/helper — see body)_

```c
void sub_1003bb1b(void)
{
    return;
}
```

## `sub_1003bb22` `0x1003bb22`

_157 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[64];
    struct struct_0 *field_40;
    char padding_44[9];
    char field_4d;
    char padding_4e[1];
    char field_4f;
    char field_50;
} struct_1;

typedef struct struct_0 {
    char padding_0[36];
    unsigned short field_24;
    char padding_26[2];
    unsigned short field_28;
    char padding_2a[2];
    char field_2c;
} struct_0;

extern unsigned short g_1004332b;
extern unsigned short g_1004332d;
extern char g_1004332f;
extern unsigned short g_10043330;
extern struct_1 g_10077175;
extern struct_1 g_100809cd;
extern char g_10080b6d;
extern char g_101d5e20;

struct_1 * sub_1003bb22(void)
{
    struct_1 *iter;  // eax
    struct_1 *index;  // eax
    struct_0 *idx;  // eax
    struct_1 *v6;  // eax
    unsigned int v0;  // [bp-0xc]
    struct_1 *v1;  // [bp-0x8]

    v1 = NULL;
    iter = &g_10077175.padding_0[0];
    while (true)
    {
        if (iter < &g_100809cd.padding_0[0])
        {
            if (iter->field_4d && (!iter->field_4f || !g_101d5e20))
            {
                index = iter;
                if (!index->field_50)
                    break;
                v1 = iter;
                iter = &iter[1].padding_44[7];
            }
            else
            {
                iter = &iter[1].padding_44[7];
            }
        }
        else
        {
            if (v1)
            {
                index = v1;
                break;
            }
            else
            {
                g_10080b6d = 0;
                return iter;
            }
        }
    }
    index->field_4d = 0;
    idx = index->field_40;
    g_1004332b = idx->field_24;
    g_1004332d = idx->field_28;
    g_1004332f = idx->field_2c;
    g_10043330 = 99;
    v0 = 11;
    v6 = sub_1002ade7("\t");
    g_10080b6d = 1;
    return v6;
}
```

## `sub_1003bba4` `0x1003bba4`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003bba4(void)
{
}
```

## `sub_1003bbc1` `0x1003bbc1`

_72 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_10052768;
extern unsigned int g_1005276c;
extern char g_10052770;

unsigned int [12] sub_1003bbc1(unsigned int *idx, unsigned int a1)
{
    unsigned int v0;  // eax
    unsigned int v1;  // eax

    if (idx[11] != *((int *)&g_10052770))
        return NULL;
    v0 = idx[9] - g_10052768;
    if (idx[9] - g_10052768 < 0)
        v0 = ~(v0) + 1;
    if (v0 > a1)
        return NULL;
    v1 = idx[10] - g_1005276c;
    if (idx[10] - g_1005276c < 0)
        v1 = ~(v1) + 1;
    if (v1 > a1)
        return NULL;
    return idx;
}
```

## `sub_1003bc09` `0x1003bc09`

_75 bytes. (leaf/helper — see body)_

```c
extern char g_100fa97a;

unsigned int [11] sub_1003bc09(int *a0)
{
    unsigned int v1[11];  // eax
    unsigned int v2[11];  // eax
    char v0;  // [bp+0x0]

    v1 = sub_1003c23e(a0, &v0);
    if (!v1)
        return v1;
    v2 = sub_10011a89(v1[9], v1[10]);
    if (v2)
        return NULL;
    if (g_100fa97a)
    {
        v2 = sub_10011678(a0[9], a0[10], 0);
        if (!v2)
            return v2;
    }
    return _INSERT(v2, 0, 1);
}
```

## `sub_1003bc54` `0x1003bc54`

_625 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[36];
    int field_24;
    int field_28;
    char padding_2c[92];
    char field_88;
    char padding_89[7];
    unsigned int field_90;
    unsigned int field_94;
    char padding_98[8];
    unsigned int field_a0;
} struct_0;

typedef struct struct_1 {
    char padding_0[76];
    char field_4c;
    char padding_4d[7];
    unsigned short field_54;
    unsigned short field_56;
    unsigned short field_58;
} struct_1;

extern char g_100678a8;
extern char g_10077175;
extern char g_100f94c8;
extern char g_100f94c9;
extern char g_100fa97a;
extern char g_10134e6a;
extern char g_1013f27d;
extern char g_1014f40d;
extern char g_1014f40e;

int sub_1003bc54(void)
{
    char v12;  // cl
    unsigned int v13;  // eax
    unsigned long v22;  // 4121
    unsigned long v23;  // 4132
    unsigned long v24;  // 4143
    unsigned int v25;  // ebx
    struct_0 *j;  // ebx
    unsigned int v27;  // eax
    unsigned int v28;  // ecx
    unsigned int v29;  // ecx
    struct_0 *v31;  // eax
    unsigned int i;  // ecx
    unsigned int v32;  // edx
    struct_1 *idx;  // ebx
    unsigned int v34;  // edx
    unsigned int v35;  // ecx
    unsigned long v36;  // 4133
    unsigned long v37;  // 4113
    unsigned long v38;  // 4125
    char v39;  // cl
    int v40;  // edx
    unsigned long v15;  // ldt
    unsigned int v41;  // ecx
    unsigned long v42;  // 4142
    unsigned long v43;  // 4113
    unsigned long v44;  // 4125
    char v45;  // cl
    unsigned int v46;  // edx
    unsigned int v47;  // ecx
    unsigned long v48;  // 4133
    unsigned long v49;  // 4113
    unsigned long v50;  // 4125
    unsigned long v16;  // gdt
    unsigned int v51;  // edx
    unsigned int v52;  // ecx
    unsigned long v53;  // 4133
    unsigned long v54;  // 4113
    unsigned long v55;  // 4125
    unsigned int v56;  // ecx
    unsigned long v57;  // 4124
    unsigned long v58;  // 4124
    unsigned long v59;  // 4124
    unsigned short v17;  // ss
    unsigned long v18;  // 4158
    unsigned long v19;  // 4162
    unsigned long v20;  // 4166
    unsigned long v21;  // 4108
    struct_0 *v0;  // [bp-0x70]
    char v1;  // [bp-0x5d]
    struct_0 *v2;  // [bp-0x5c]
    unsigned int *v3;  // [bp-0x58]
    unsigned int v4;  // [bp-0x50]
    char v5;  // [bp-0x4c]
    char v6;  // [bp-0x40]
    char v7;  // [bp-0x34]
    char v8;  // [bp-0x28]
    char v9;  // [bp-0x1c]
    char v10;  // [bp-0x10]

    v3 = sub_1003a494;
    v12 = g_1014f40d;
    if (v13 == &g_100678a8)
    {
        v3 = sub_1003a550;
        v12 = g_1014f40e;
    }
    v1 = v12;
    for (i = 0; i < 12; i += 4)
    {
        v18 = _ccall(v15, v16, (unsigned int)v17, &v10 + i);
        *((unsigned int *)v18) = 101;
        v19 = _ccall(v15, v16, (unsigned int)v17, &v9 + i);
        *((unsigned int *)v19) = 0;
        v20 = _ccall(v15, v16, (unsigned int)v17, &v8 + i);
        *((unsigned int *)v20) = 20000;
        if (!g_10134e6a)
        {
            v21 = _ccall(v15, v16, (unsigned int)v17, &v8 + i);
            *((unsigned int *)v21) = 0;
        }
        v22 = _ccall(v15, v16, (unsigned int)v17, &v7 + i);
        *((unsigned int *)v22) = 0;
        v23 = _ccall(v15, v16, (unsigned int)v17, &v6 + i);
        *((unsigned int *)v23) = 20000;
        v24 = _ccall(v15, v16, (unsigned int)v17, &v5 + i);
        *((unsigned int *)v24) = 0;
    }
    if (!v25)
        j = 0x63fef8;
    while (j < 0x64a308)
    {
        v2 = j;
        if (j->field_90 && sub_1003c23e(j))
        {
            v27 = v3(&j->padding_0[4]);
            v29 = v28;
            if (v29 > 2)
                v29 = 2;
            v4 = v29 * 4;
            if (!v27 || v1 && !v0->field_94 && v0->field_a0 != 2)
                goto LABEL_1003be85;
            v0 = v2;
            if (sub_10011a89(v0->field_24, v0->field_28))
                goto LABEL_1003be85;
            v31 = v0;
            if (g_100fa97a)
            {
                v0 = v31;
                if (!sub_10011678(v31->field_24, v31->field_28, 0))
                    goto LABEL_1003be85;
                else
                    v31 = v0;
            }
            if (v32)
            {
                v0 = v31;
                if (!sub_1003bbc1(v31, v32))
                    goto LABEL_1003be85;
                else
                    v31 = v0;
            }
            if (g_100f94c8)
            {
                v0 = v31;
                idx = &(&g_10077175)[156 * (unsigned long long)(struct struct_0 *)&v31[39959].padding_2c[16] / 168];
                v31 = v0;
                if (g_1013f27d && idx->field_54)
                {
                    v34 = idx->field_54;
                    v35 = v4;
                    v36 = _ccall(v15, v16, (unsigned int)v17, &v6 + v35);
                    if (v34 <= *((int *)v36))
                    {
                        v37 = _ccall(v15, v16, (unsigned int)v17, &v6 + v35);
                        *((unsigned int *)v37) = v34;
                        v38 = _ccall(v15, v16, (unsigned int)v17, &v5 + v35);
                        *((struct_0 **)v38) = v31;
                    }
                }
                if (!idx->field_56)
                    goto LABEL_1003be6a;
                if (g_10134e6a)
                {
                    v39 = idx->field_4c;
                    if (idx->field_4c != 3 && v39 != 4 && v39 != 7 && v39 != 8)
                        goto LABEL_1003be6a;
                    v40 = idx->field_56 - idx->field_58;
                    v41 = v4;
                    v42 = _ccall(v15, v16, (unsigned int)v17, &v8 + v41);
                    if (v40 > *((int *)v42))
                        goto LABEL_1003be85;
                    v43 = _ccall(v15, v16, (unsigned int)v17, &v8 + v41);
                    *((int *)v43) = v40;
                    v44 = _ccall(v15, v16, (unsigned int)v17, &v7 + v41);
                    *((struct_0 **)v44) = v31;
                }
                if (g_100f94c9 && !((v45 = idx->field_4c, idx->field_4c != 3 && idx->field_4c != 4 && idx->field_4c != 7 && idx->field_4c != 8)))
                {
                    v46 = idx->field_58;
                    v47 = v4;
                    v48 = _ccall(v15, v16, (unsigned int)v17, &v8 + v47);
                    if (v46 >= *((int *)v48))
                    {
                        v49 = _ccall(v15, v16, (unsigned int)v17, &v8 + v47);
                        *((unsigned int *)v49) = v46;
                        v50 = _ccall(v15, v16, (unsigned int)v17, &v7 + v47);
                        *((struct_0 **)v50) = v31;
                        goto LABEL_1003be85;
                    }
                }
            }
LABEL_1003be6a:
            v51 = v31->field_88;
            v52 = v4;
            v53 = _ccall(v15, v16, (unsigned int)v17, &v10 + v52);
            if (v51 < *((int *)v53))
            {
                v54 = _ccall(v15, v16, (unsigned int)v17, &v10 + v52);
                *((unsigned int *)v54) = v51;
                v55 = _ccall(v15, v16, (unsigned int)v17, &v9 + v52);
                *((struct_0 **)v55) = v31;
                goto LABEL_1003be85;
            }
        }
        else
        {
LABEL_1003be85:
            j = &v2[1].padding_0[4];
        }
    }
    v56 = 8;
    while (true)
    {
        v57 = _ccall(v15, v16, (unsigned int)v17, &v7 + v56);
        if (*((int *)v57))
            return;
        v58 = _ccall(v15, v16, (unsigned int)v17, &v5 + v56);
        if (*((int *)v58))
            return;
        v59 = _ccall(v15, v16, (unsigned int)v17, &v9 + v56);
        if (*((int *)v59))
        {
            return;
        }
        else if (v56)
        {
            v56 -= 4;
        }
        else
        {
            return;
        }
    }
}
```

## `sub_1003bec5` `0x1003bec5`

_295 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[36];
    int field_24;
    int field_28;
    char padding_2c[92];
    char field_88;
} struct_0;

extern char g_1005f7ed;
extern char g_1006b8a8;
extern char g_100fa97a;

int sub_1003bec5(void)
{
    unsigned int v10;  // eax
    unsigned int v11;  // ecx
    unsigned int v20;  // ecx
    unsigned long v21;  // ldt
    unsigned long v22;  // gdt
    unsigned short v23;  // ss
    unsigned long v24;  // 4133
    unsigned long v25;  // 4123
    unsigned long v26;  // 4113
    unsigned long v27;  // 4125
    unsigned int v12;  // ebx
    struct_0 *i;  // ebx
    unsigned int v14;  // eax
    unsigned int v15;  // ecx
    struct_0 *v17;  // eax
    unsigned int v18;  // edx
    unsigned int v19;  // edx
    struct_0 *v0;  // [bp-0x3c]
    struct_0 *v1;  // [bp-0x2c]
    unsigned int *v2;  // [bp-0x28]
    unsigned int v3;  // [bp-0x20]
    unsigned int v4;  // [bp-0x1c]
    unsigned int v5;  // [bp-0x18]
    unsigned int v6;  // [bp-0x14]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]

    v2 = sub_1003a320;
    if (v10 == &g_1006b8a8)
        v2 = sub_1003a3da;
    v4 = 0;
    v7 = v11;
    v5 = 0;
    v8 = v11;
    v6 = 0;
    if (!v12)
        i = 0x63fef8;
    for (; i < 0x64a308; i = &v1[1].padding_0[31])
    {
        v1 = i;
        if (*((int *)&i[1].padding_0[7]) && sub_1003c23e(i))
        {
            v14 = v2(&i->padding_0[4]);
            v15 = v11;
            if (v15 > 2)
                v15 = 2;
            v3 = v15 * 4;
            if (!v14)
                goto LABEL_1003bfc4;
            v0 = v1;
            if (sub_10011a89(v0->field_24, v0->field_28))
                goto LABEL_1003bfc4;
            v17 = v0;
            if (g_100fa97a)
            {
                v0 = v17;
                if (!sub_10011678(v17->field_24, v17->field_28, 0))
                    goto LABEL_1003bfc4;
                else
                    v17 = v0;
            }
            if (v18)
            {
                v0 = v17;
                if (!sub_1003bbc1(v17, v18))
                    goto LABEL_1003bfc4;
                else
                    v17 = v0;
            }
            v19 = v17->field_88;
            v20 = v3;
            v24 = _ccall(v21, v22, (unsigned int)v23, &/* unsupported instruction */ + v20);
            if (v19 < *((int *)v24))
            {
                v25 = _ccall(v21, v22, (unsigned int)v23, &/* unsupported instruction */ + v20);
                if (*((int *)v25) != 200 || v17 != *((int *)&g_1005f7ed))
                {
                    v26 = _ccall(v21, v22, (unsigned int)v23, &/* unsupported instruction */ + v20);
                    *((unsigned int *)v26) = v19;
                    v27 = _ccall(v21, v22, (unsigned int)v23, &v4 + v20);
                    *((struct_0 **)v27) = v17;
                }
            }
        }
LABEL_1003bfc4:
    }
    return;
}
```

## `sub_1003bfec` `0x1003bfec`

_107 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[144];
    char field_90;
} struct_0;

extern char g_1005f8a8[4];
extern char g_100f94c9;

struct_0 * sub_1003bfec(void)
{
    unsigned int v5;  // ebx
    char *v6;  // eax
    struct_0 *v7;  // eax
    unsigned int v0;  // [bp-0x14]
    unsigned int iter;  // [bp-0x10]
    struct_0 *v2;  // [bp-0xc]
    char v3;  // [bp-0x5]

    v0 = v5;
    iter = 0;
    v3 = 101;
    v2 = NULL;
    while (iter < 0x200)
    {
        v6 = &g_1005f8a8[32 * iter];
        if (!*(v6))
            return v2;
        v7 = sub_100399af(v6);
        if (v7)
        {
            if (!g_100f94c9)
                return v7;
            if (v7->padding_0[0x88] < v3)
            {
                v3 = v7->padding_0[0x88];
                v2 = v7;
            }
            iter += 1;
        }
        else
        {
            iter += 1;
        }
    }
    return v2;
}
```

## `sub_1003c031` `0x1003c031`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003c031(void)
{
}
```

## `sub_1003c059` `0x1003c059`

_483 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    char padding_0[136];
    char field_88;
} struct_2;

typedef struct struct_0 {
    char padding_0[36];
    unsigned short field_24;
    char padding_26[2];
    unsigned short field_28;
    char padding_2a[2];
    char field_2c;
    char padding_2d[99];
    char field_90;
} struct_0;

extern char g_100f94c9;

struct_2 * sub_1003c059(unsigned short a0, unsigned short a1, char a2, unsigned int a3)
{
    unsigned short v13;  // cx
    unsigned short v14;  // di
    struct_2 *v23;  // eax
    struct_0 *iter;  // eax
    unsigned short v16;  // bx
    unsigned short v17;  // bx
    struct_0 **v19;  // ebx
    struct_2 **node;  // eax
    struct_2 *v21;  // eax
    struct_2 *v22;  // eax
    struct_2 **v0;  // [bp-0x2f0]
    unsigned short v1;  // [bp-0x2e6]
    char v2[704];  // [bp-0x2e4]
    struct_2 *v3;  // [bp-0x24]
    char v4;  // [bp-0x1d]
    struct_2 *v5;  // [bp-0x1c]
    unsigned int iter1;  // [bp-0x18]
    char v7;  // [bp-0x11]
    char v8;  // [bp-0x11]
    char v9;  // [bp-0x11]
    struct_2 *v10;  // [bp-0x10]
    unsigned int i;  // [bp-0xc]
    unsigned int iter2;  // [bp-0x8]

    sub_1002ae81(v2, 704);
    v13 = a0 - 1;
    v14 = a1 - 1;
    iter = 0x63fef8;
    while (true)
    {
        if (iter->field_90 && a2 == iter->field_2c)
        {
            v16 = iter->field_24;
            if (v16 >= v13 && v16 <= a0 + 1)
            {
                v1 = (v16 - v13) * 4;
                v17 = iter->field_28;
                if (v17 >= v14 && v17 <= a1 + 1)
                {
                    iter1 = 0;
                    for (v19 = &v2[_INSERT((v17 - v14) * 16 CONCAT 0, 0, (v17 - v14) * 16 + v1)]; iter1 < 16; iter1 += 1)
                    {
                        if (!*(v19))
                        {
                            *(v19) = iter;
                            break;
                        }
                    }
                }
            }
        }
        if (iter >= 0x64a308)
            break;
        iter = &iter[1].padding_0[23];
    }
    v4 = 101;
    v3 = NULL;
    v10 = NULL;
    v9 = 101;
    for (i = 0; i < 3; i += 1)
    {
        iter2 = 0;
        while (iter2 < 3)
        {
            node = &v2[16 * i + 4 * iter2];
            iter1 = 0;
            while (true)
            {
                if (iter1 >= 16)
                {
                    iter2 += 1;
                    break;
                }
                else if (*(node))
                {
                    v0 = node;
                    v7 = v9;
                    if (*(node))
                    {
                        v5 = *(node);
                        if (sub_1003a494((struct struct_2 *)&*(node)->padding_0[4]))
                        {
                            if (a3 == 2)
                            {
                                v21 = v5;
                                if (!g_100f94c9)
                                    return v21;
                                if (v21->field_88 < v4)
                                {
                                    v4 = v21->field_88;
                                    v3 = v21;
                                }
                            }
                            v7 = v9;
                        }
                        else if (sub_1003a320((struct struct_2 *)&v5->padding_0[4]))
                        {
                            if (a3 == 1)
                            {
                                v22 = v5;
                                if (v22->field_88 < v4 && v22->field_88 <= 90)
                                {
                                    v4 = v22->field_88;
                                    v3 = v22;
                                }
                            }
                            v7 = v9;
                        }
                        else
                        {
                            v23 = v5;
                            if (a3 == 2 || (v7 = v9, (unsigned int)v8 < (unsigned int)v7 && !((v7 = v9, v8 > 90))))
                            {
                                v8 = v23->field_88;
                                v10 = v23;
                                v7 = v8;
                            }
                        }
                    }
                    v9 = v7;
                    node += 1;
                    iter1 -= 1;
                }
                else
                {
                    iter2 += 1;
                    break;
                }
            }
        }
    }
    return (!v3 ? (!v10 ? NULL : v10) : v3);
}
```

## `sub_1003c18e` `0x1003c18e`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003c18e(void)
{
}
```

## `sub_1003c23e` `0x1003c23e`

_83 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[36];
    unsigned short field_24;
    char padding_26[2];
    unsigned short field_28;
    char padding_2a[2];
    char field_2c;
} struct_0;

extern unsigned short g_1005f854;
extern unsigned short g_1005f858;
extern char g_1005f85c;

struct_0 * sub_1003c23e(struct_0 *idx)
{
    unsigned short v0;  // cx
    unsigned short v1;  // dx

    if (!idx)
        return idx;
    if (idx->field_2c != g_1005f85c)
        return NULL;
    v0 = idx->field_24 - g_1005f854 + 8;
    if (v0 && v0 < 16)
    {
        v1 = idx->field_28 - g_1005f858 + 6;
        if (v1 && v1 < 12)
            return idx;
    }
    return NULL;
}
```

## `sub_1003c291` `0x1003c291`

_82 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned short field_0;
    char padding_2[2];
    unsigned short field_4;
    char padding_6[2];
    char field_8;
} struct_0;

extern unsigned short g_1005f854;
extern unsigned short g_1005f858;
extern char g_1005f85c;

struct_0 * sub_1003c291(struct_0 *a0)
{
    unsigned short v0;  // cx
    unsigned short v1;  // dx

    if (!a0)
        return a0;
    if (a0->field_8 != g_1005f85c)
        return NULL;
    v0 = a0->field_0 - g_1005f854 + 8;
    if (v0 && v0 < 16)
    {
        v1 = a0->field_4 - g_1005f858 + 6;
        if (v1 && v1 < 12)
            return a0;
    }
    return NULL;
}
```

## `sub_1003c2e3` `0x1003c2e3`

_78 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_1005f854;
extern unsigned short g_1005f858;
extern char g_1005f85c;

unsigned int sub_1003c2e3(unsigned short a0, unsigned short a1, char a2)
{
    unsigned short v0;  // cx
    unsigned short v1;  // dx

    if (a2 != g_1005f85c)
        return 0;
    v0 = a0 - g_1005f854 + 8;
    if (!v0)
    {
        return 0;
    }
    else if (v0 < 16)
    {
        v1 = a1 - g_1005f858 + 6;
        if (!v1)
        {
            return 0;
        }
        else if (v1 < 12)
        {
            return _INSERT(0, 0, 1);
        }
        else
        {
            return 0;
        }
    }
    else
    {
        return 0;
    }
}
```

## `sub_1003c331` `0x1003c331`

_47 bytes. (leaf/helper — see body)_

```c
extern char g_1005f88d;
extern char g_1005f8a3;

int sub_1003c331(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7)
{
    unsigned int v1;  // eax
    unsigned int v0;  // [bp+0x0]

    if (g_1005f8a3 || g_1005f88d || a7 == 11)
        v1 = _INSERT(v0, 0, 1);
    else
        v1 = 0;
    if (v1)
        sub_1003c359(); /* do not return */
}
```

## `sub_1003c359` `0x1003c359`

_12 bytes. (leaf/helper — see body)_

```c
void sub_1003c359(void)
{
    unsigned int v2;  // ebx
    unsigned int v0;  // [bp-0x3c]

    v0 = v2;
}
```

## `sub_1003c365` `0x1003c365`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003c365(void)
{
    sub_1003c36e();
    return;
}
```

## `sub_1003c36e` `0x1003c36e`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1003c36e(void)
{
    return;
}
```

## `sub_1003c36f` `0x1003c36f`

_141 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1009a52e;
extern unsigned int g_1009a532;

unsigned int sub_1003c36f(unsigned int a0)
{
    unsigned int v0;  // esi
    unsigned int v1;  // ecx

    v0 = (a0 - *((int *)*((int *)0x7998dc))) * 76 + *((int *)(*((int *)0x7998dc) + 8));
    v1 = *((int *)(1 + v0 + 36)) & 0xffffff;
    if (v1 == 6291552)
        return 1;
    if (g_1009a52e)
    {
        if (v1 == 4194368)
        {
            return 1;
        }
        else if (v1 == 2097248)
        {
            return 1;
        }
    }
    if (!g_1009a532 || v1 != 2097248)
        return _INSERT(*((char *)(1 + v0 + 36)), 0, *((char *)(1 + v0 + 36)) & 64);
    return 1;
    return _INSERT(*((char *)(1 + v0 + 36)), 0, *((char *)(1 + v0 + 36)) & 64);
}
```

## `sub_1003c3fc` `0x1003c3fc`

_52 bytes. (leaf/helper — see body)_

```c
int sub_1003c3fc(unsigned int a0)
{
    return _INSERT(*((char *)(1 + (a0 - *((int *)*((int *)0x7998dc))) * 76 + *((int *)(*((int *)0x7998dc) + 8)) + 36)), 0, *((char *)(1 + (a0 - *((int *)*((int *)0x7998dc))) * 76 + *((int *)(*((int *)0x7998dc) + 8)) + 36)) & 16);
}
```

## `sub_1003c430` `0x1003c430`

_50 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1003c430(unsigned int a0)
{
    unsigned int v0;  // esi

    v0 = (a0 - *((int *)*((int *)0x7998dc))) * 76 + *((int *)(*((int *)0x7998dc) + 8));
    *((char *)(1 + v0 + 36)) = *((char *)(1 + v0 + 36)) | 16;
    return 1;
}
```

## `sub_1003c462` `0x1003c462`

_52 bytes. (leaf/helper — see body)_

```c
int sub_1003c462(unsigned int a0)
{
    return _INSERT(*((char *)(1 + (a0 - *((int *)*((int *)0x7998dc))) * 76 + *((int *)(*((int *)0x7998dc) + 8)) + 36)), 0, *((char *)(1 + (a0 - *((int *)*((int *)0x7998dc))) * 76 + *((int *)(*((int *)0x7998dc) + 8)) + 36)) & 128);
}
```

## `sub_1003c496` `0x1003c496`

_50 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1003c496(unsigned int a0)
{
    unsigned int v0;  // esi

    v0 = (a0 - *((int *)*((int *)0x7998dc))) * 76 + *((int *)(*((int *)0x7998dc) + 8));
    *((char *)(1 + v0 + 36)) = *((char *)(1 + v0 + 36)) & 127;
    return 1;
}
```

## `sub_1003c4c8` `0x1003c4c8`

_50 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1003c4c8(unsigned int a0)
{
    unsigned int v0;  // esi

    v0 = (a0 - *((int *)*((int *)0x7998dc))) * 76 + *((int *)(*((int *)0x7998dc) + 8));
    *((char *)(1 + v0 + 36)) = *((char *)(1 + v0 + 36)) | 128;
    return 1;
}
```

## `sub_1003c4fa` `0x1003c4fa`

_48 bytes. (leaf/helper — see body)_

```c
int sub_1003c4fa(unsigned int a0)
{
    return *((int *)((a0 - *((int *)*((int *)0x7998dc))) * 76 + *((int *)(*((int *)0x7998dc) + 8)) + 36));
}
```

## `sub_1003c52a` `0x1003c52a`

_51 bytes. (leaf/helper — see body)_

```c
int sub_1003c52a(unsigned int a0)
{
    return _INSERT(*((char *)((a0 - *((int *)*((int *)0x7998dc))) * 76 + *((int *)(*((int *)0x7998dc) + 8)) + 36)), 0, *((char *)((a0 - *((int *)*((int *)0x7998dc))) * 76 + *((int *)(*((int *)0x7998dc) + 8)) + 36)) & 32);
}
```

## `sub_1003c55d` `0x1003c55d`

_443 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
} struct_0;

extern unsigned int g_10052768;
extern unsigned int g_1005276c;

unsigned int sub_1003c55d(int a0, int a1, int a2, int a3, unsigned int a4)
{
    int v11;  // eax
    int v12;  // eax
    int v19;  // eax
    struct_0 **v20;  // eax
    unsigned int i;  // ecx
    int v13;  // eax
    int node;  // esi
    int v15;  // edi
    int v16;  // edi
    int v17;  // ecx
    char *v18;  // ebx
    unsigned int idx;  // [bp-0xb0]
    char *v1;  // [bp-0xac]
    unsigned int v2;  // [bp-0x2c]
    int v3;  // [bp-0x20]
    int iter;  // [bp-0x20]
    int v5;  // [bp-0x1c]
    int v6;  // [bp-0x18]
    int v7;  // [bp-0x14]
    int v8;  // [bp-0x10]
    unsigned int v9;  // [bp-0xc]
    unsigned int v10;  // [bp-0x8]

    idx = 0;
    v11 = a2 - a0;
    if (v11 < 40)
    {
        v10 = 1;
        v8 = v11;
    }
    else
    {
        v10 = 4294967295;
        v8 = ~(v8) + 1;
    }
    v12 = a3 - a1;
    if (v12 < 40)
    {
        v9 = 1;
        v7 = v12;
    }
    else
    {
        v9 = 4294967295;
        v7 = ~(v7) + 1;
    }
    if (v8 >= 8)
    {
        return 0;
    }
    else if (v7 >= 6)
    {
        return 0;
    }
    else
    {
        v2 = 0;
        if (v8 != v7)
        {
            if (v10 == 1 && v9 == 4294967295)
            {
                if (v7 <= v8)
                    v2 = 1;
            }
            else
            {
                if (v10 == 4294967295 && v9 == 4294967295)
                {
                    v2 = 1;
                }
                else if (v10 == 4294967295 && v9 == 1 && v7 > v8)
                {
                    v2 = 1;
                }
            }
        }
        if (v2)
        {
            v5 = a2;
            iter = a3;
            v10 = ~(v10) + 1;
            v9 = ~(v9) + 1;
        }
        else
        {
            v5 = a0;
            iter = a1;
        }
        v13 = v8;
        if (v13 < v7)
            v13 = v7;
        v6 = v13;
        node = 0;
        v15 = 0;
        node = 0;
        v16 = 0;
        if (v2)
            node = -1;
        while (true)
        {
            iter = v3;
            v17 = v5;
            if (sub_1003c87c(v5, iter, node, v15, node))
            {
                v20 = &v1;
                for (i = idx; i; i -= 1)
                {
                    *(v20)->field_0 = *(v20)->field_0 - 1;
                    v20 += 1;
                }
                return 0;
            }
            else
            {
                if (a4)
                {
                    v18 = (iter - g_1005276c + 6) * 18 + v5 - g_10052768 + 8 + a4;
                    *(v18) = *(v18) + 1;
                    (&v1)[idx] = v18;
                    idx += 1;
                    node = v17 + 1;
                    v16 = iter;
                }
                else
                {
                    node = v17 + 1;
                    v16 = iter;
                }
                iter = v3;
                if (node >= v6)
                    return 1;
                node += v8;
                v15 = v16 + v7;
                v19 = v6;
                if (node >= v19)
                {
                    node -= v19;
                    v5 += v10;
                }
                if (v15 >= v19)
                {
                    v15 -= v19;
                    iter += v9;
                }
            }
        }
    }
}
```

## `sub_1003c718` `0x1003c718`

_356 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_10052768;
extern unsigned int g_1005276c;

unsigned int sub_1003c718(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4)
{
    unsigned int v8;  // eax
    unsigned int v9;  // eax
    unsigned int v10;  // eax
    unsigned int iter;  // esi
    unsigned int node;  // edi
    unsigned int v13;  // ecx
    unsigned int v14;  // eax
    unsigned int v0;  // [bp-0x2c]
    unsigned int i;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]

    v8 = a2 - a0;
    if (v8 < 40)
    {
        v7 = 1;
        v5 = v8;
    }
    else
    {
        v7 = 4294967295;
        v5 = ~(v5) + 1;
    }
    v9 = a3 - a1;
    if (v9 < 40)
    {
        v6 = 1;
        v4 = v9;
    }
    else
    {
        v6 = 4294967295;
        v4 = ~(v4) + 1;
    }
    if (v5 >= 8)
    {
        return 0;
    }
    else if (v4 >= 6)
    {
        return 0;
    }
    else
    {
        v0 = 0;
        if (v5 != v4)
        {
            if (v7 == 1 && v6 == 4294967295)
            {
                if (v4 <= v5)
                    v0 = 1;
            }
            else
            {
                if (v7 == 4294967295 && v6 == 4294967295)
                {
                    v0 = 1;
                }
                else if (v7 == 4294967295 && v6 == 1 && v4 > v5)
                {
                    v0 = 1;
                }
            }
        }
        if (v0)
        {
            v2 = a2;
            i = a3;
            v7 = ~(v7) + 1;
            v6 = ~(v6) + 1;
        }
        else
        {
            v2 = a0;
            i = a1;
        }
        v10 = v5;
        if (v10 < v4)
            v10 = v4;
        v3 = v10;
        iter = 0;
        node = 0;
        v13 = 0;
        if (v0)
            v13 = 4294967295;
        for (; !*((char *)((i - g_1005276c + 6) * 18 + v2 - g_10052768 + 8 + a4)); i += v6)
        {
            v13 += 1;
            if (v13 >= v3)
                return 1;
            iter += v5;
            node += v4;
            v14 = v3;
            if (iter >= v14)
            {
                iter -= v14;
                v2 += v7;
            }
            if (node >= v14)
                node -= v14;
        }
        return 0;
    }
}
```

## `sub_1003c87c` `0x1003c87c`

_88 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
} struct_0;

extern int g_10052770;

unsigned int sub_1003c87c(int a0, int a1)
{
    struct_0 *v2;  // eax
    struct_0 *iter;  // esi
    struct_0 *v4;  // ebx
    unsigned int v5;  // eax
    struct_0 *v0;  // [bp-0xc]
    struct_0 *v1;  // [bp-0x8]

    v2 = sub_1003a03f(a0, a1, g_10052770);
    if (!v2)
        return 1;
    iter = &v2->field_4;
    v4 = 12 * v2->field_0 + (char *)iter;
    while (iter < v4)
    {
        if (iter->field_0 != 99)
        {
            v1 = iter;
            v0 = v4;
            v5 = sub_1003c36f(iter->field_0);
            if (v5)
                return v5;
            iter = &iter[1].field_4;
        }
        else
        {
            iter = &iter[1].field_4;
        }
    }
    return 0;
}
```

## `sub_1003c8bb` `0x1003c8bb`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003c8bb(void)
{
}
```

## `sub_1003c8c2` `0x1003c8c2`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003c8c2(void)
{
}
```

## `sub_1003c8d8` `0x1003c8d8`

_90 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
} struct_0;

extern int g_10052770;

unsigned int sub_1003c8d8(int a0, int a1)
{
    struct_0 *v2;  // eax
    struct_0 *iter;  // esi
    struct_0 *v4;  // ebx
    struct_0 *v0;  // [bp-0xc]
    struct_0 *v1;  // [bp-0x8]

    v2 = sub_1003a03f(a0, a1, g_10052770);
    if (!v2)
        return 0;
    iter = &v2->field_4;
    v4 = 12 * v2->field_0 + (char *)iter;
    while (iter < v4)
    {
        if (iter->field_0 != 99)
        {
            v1 = iter;
            v0 = v4;
            if (sub_1003c3fc(iter->field_0))
                return 0;
            iter = &iter[1].field_4;
        }
        else
        {
            iter = &iter[1].field_4;
        }
    }
    return 1;
}
```

## `sub_1003c919` `0x1003c919`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003c919(void)
{
}
```

## `sub_1003c920` `0x1003c920`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003c920(void)
{
}
```

## `sub_1003c936` `0x1003c936`

_131 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
} struct_0;

extern unsigned int g_10052768;
extern unsigned int g_1005276c;
extern int g_10052770;

unsigned int sub_1003c936(int a0, int a1)
{
    struct_0 *v2;  // eax
    struct_0 *i;  // esi
    struct_0 *v4;  // ebx
    struct_0 *v0;  // [bp-0xc]
    struct_0 *v1;  // [bp-0x8]

    if (a0 - g_10052768 + 8 >= 18)
    {
        return 0;
    }
    else if (a1 - g_1005276c + 6 >= 14)
    {
        return 0;
    }
    else
    {
        v2 = sub_1003a03f(a0, a1, g_10052770);
        if (!v2)
            return 0;
        i = &v2->field_4;
        for (v4 = 12 * v2->field_0 + (char *)i; i < v4; i = &i[1].field_4)
        {
            if (i->field_0 == 99)
                return 0;
            v1 = i;
            v0 = v4;
            if (sub_1003c3fc(i->field_0))
                return 0;
        }
        return 1;
    }
}
```

## `sub_1003c99f` `0x1003c99f`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003c99f(void)
{
}
```

