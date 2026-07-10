# elfbot.dll decompiled — jiru 0x1035e3bb..0x10360dc5

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1035e3bb` `0x1035e3bb`

_185 bytes. refs ", 260);
    g_103a302c = "_

```c
typedef struct struct_1 {
    char field_0;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1d4;
extern unsigned int g_103a3010;
extern unsigned int g_103a3014;
extern unsigned int g_103a302c;
extern char g_103a3a3c;
extern struct_1 *g_103a4ccc;
extern unsigned int g_103a4cdc;

unsigned int sub_1035e3bb(unsigned int a0)
{
    unsigned int v7;  // ebx
    unsigned int v8;  // esi
    unsigned int v9;  // edi
    unsigned int v10;  // ecx
    unsigned int v11;  // edi
    unsigned int v12;  // eax
    int v13;  // esi
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char *v5;  // [bp-0x8]

    v2 = v7;
    v1 = v8;
    v0 = v9;
    if (!g_103a4cdc)
        sub_1035b7cc();
    g_103a3a3c = 0;
    g_1038b1d4(0, "C:\\Documents and Settings\\Administrador\\Escritorio\\CRACKING\\ArmaG3ddon_v1.9\\dll loader.exe", 260);
    g_103a302c = "C:\\Documents and Settings\\Administrador\\Escritorio\\CRACKING\\ArmaG3ddon_v1.9\\dll loader.exe";
    if (!g_103a4ccc || (v5 = (char *)g_103a4ccc, !g_103a4ccc->field_0))
        v5 = "C:\\Documents and Settings\\Administrador\\Escritorio\\CRACKING\\ArmaG3ddon_v1.9\\dll loader.exe";
    sub_1035e223(v10, v5, NULL, NULL, &v4);
    if (v4 < 0x3fffffff && v3 < 4294967295)
    {
        v11 = v4 * 4;
        v12 = v11 + v3;
        if (v12 >= v3)
        {
            v13 = sub_10357482(v12);
            if (v13)
            {
                sub_1035e223(v12, v5, v13, v11 + v13, &v4);
                g_103a3010 = v4 - 1;
                g_103a3014 = v13;
                return 0;
            }
        }
    }
    return 4294967295;
}
```

## `sub_1035e474` `0x1035e474`

_309 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b040;
extern struct_0 *g_1038b07c;
extern struct_0 *g_1038b278;
extern struct_0 *g_1038b27c;
extern struct_0 *g_1038b280;
extern struct_0 *g_1038b284;
extern unsigned int g_103a3a40;

int sub_1035e474(unsigned int a0)
{
    unsigned int v5;  // eax
    unsigned int v6;  // ebx
    char *v15;  // esi
    unsigned int v16;  // ebp
    unsigned int v17;  // edi
    unsigned short *v7;  // esi
    unsigned int v8;  // edi
    unsigned int v9;  // esi
    unsigned int v10;  // ebx
    unsigned short *iter;  // eax
    unsigned int v12;  // ebp
    unsigned int v13;  // eax
    char *node;  // eax
    unsigned int v0;  // [bp-0x5c]
    unsigned int v1;  // [bp-0x28]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x4]

    v5 = g_103a3a40;
    v6 = 0;
    v7 = NULL;
    v2 = 2;
    if (!v5)
    {
        v7 = g_1038b284(v8, v9, /* unsupported instruction */, v10, a0, a0);
        if (v7)
        {
            g_103a3a40 = 1;
LABEL_1035e4c6:
            if (v7 || !((v7 = (unsigned short *)g_1038b284(), !v7)))
            {
                iter = v7;
                if (*(v7))
                {
                    while (true)
                    {
                        iter += 1;
                        if (*(iter))
                            continue;
                        iter += 1;
                        if (!*(iter))
                            break;
                    }
                }
                v3 = (iter - v7 >> 1) + 1;
                v12 = g_1038b040(0, 0, v7, (iter - v7 >> 1) + 1, 0, 0, 0, 0);
                if (v12)
                {
                    v13 = sub_10357482(v12);
                    v1 = v13;
                    if (v13)
                    {
                        if (!g_1038b040(0, 0, v7, 0, v13, v12, 0, 0))
                        {
                            v0 = v13;
                            sub_1035345e();
                            v13 = 0;
                        }
                        v6 = v13;
                    }
                }
                g_1038b280(v7);
                return v6;
            }
            goto LABEL_1035e4d2;
        }
        else if (g_1038b07c() == 120)
        {
            v5 = 2;
            g_103a3a40 = 2;
        }
        else
        {
            v5 = g_103a3a40;
        }
    }
    if (v5 == 1)
        goto LABEL_1035e4c6;
    if (v5 == 2 || !v5)
    {
        node = g_1038b27c();
        v15 = node;
        if (v15)
        {
            if (*(v15))
            {
                while (true)
                {
                    node += 1;
                    if (*(node))
                        continue;
                    node += 1;
                    if (!*(node))
                        break;
                }
            }
            v16 = node - v15 + 1;
            v17 = sub_10357482(v16);
            if (v17)
            {
                sub_10350b50(v17, v15, v16);
                g_1038b278(v15);
                return v17;
            }
            g_1038b278(v15);
        }
    }
LABEL_1035e4d2:
    return 0;
}
```

## `sub_1035e5a9` `0x1035e5a9`

_148 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b03c;
extern struct_0 *g_1038b0a4;
extern struct_0 *g_1038b148;
extern struct_0 *g_1038b1c8;
extern struct_0 *g_1038b288;
extern unsigned int g_1038e180;
extern unsigned int g_1038e184;

unsigned int sub_1035e5a9(void)
{
    unsigned int v7;  // eax
    unsigned int v8;  // ebx
    unsigned int v9;  // edi
    unsigned int v10;  // esi
    unsigned int v11;  // eax
    unsigned int v12;  // eax
    unsigned int v13;  // eax
    unsigned int v14;  // eax
    unsigned int v15;  // esi
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    char v2;  // [bp-0x14], Other Possible Types: unsigned int
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v7 = g_1038e180;
    v4 = 0;
    v5 = 0;
    v1 = v8;
    v0 = v9;
    if (v7 != 3141592654 && (v7 & 0xffff0000))
    {
        g_1038e184 = ~(v7);
        return ~(v7);
    }
    g_1038b148(&v4, v10);
    v11 = g_1038b1c8(&v4, v10);
    v12 = g_1038b0a4();
    v13 = g_1038b03c();
    g_1038b288(&v2);
    v14 = v3 ^ v2;
    v15 = v5 ^ v4 ^ v11 ^ v12 ^ v13 ^ v14;
    if (v15 == 3141592654)
    {
        v15 = 3141592655;
    }
    else if (!(v15 & 0xffff0000))
    {
        v14 = v15 * 0x10000;
        v15 |= v14;
    }
    g_1038e180 = v15;
    g_1038e184 = ~(v15);
    return v14;
}
```

## `sub_1035e63d` `0x1035e63d`

_1049 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[172];
    unsigned int field_ac;
} struct_0;

int sub_1035e63d(void)
{
    unsigned short v6[35];  // eax
    struct_0 *v7;  // esi
    unsigned int v8;  // ebx
    unsigned int v9;  // edi
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v4 = v6[33];
    v3 = v6[0x22];
    if (!v7)
        return;
    v2 = 0;
    v1 = v8;
    v0 = v9;
    sub_1035a196(&/* unsupported instruction */, 1, v4, 49, &v7->padding_0[4]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 50, &v7->padding_0[8]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 0x33, &v7->padding_0[12]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 52, &v7->padding_0[16]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 53, &v7->padding_0[20]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 54, &v7->padding_0[24]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 55, v7);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 42, &v7->padding_0[32]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 43, &v7->padding_0[36]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 44, &v7->padding_0[40]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 45, &v7->padding_0[44]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 46, &v7->padding_0[48]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 47, &v7->padding_0[52]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 48, &v7->padding_0[28]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 0x44, &v7->padding_0[56]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 69, &v7->padding_0[60]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 70, &v7->padding_0[64]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 71, &v7->padding_0[0x44]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 72, &v7->padding_0[72]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 73, &v7->padding_0[76]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 74, &v7->padding_0[80]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 75, &v7->padding_0[84]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 76, &v7->padding_0[88]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 77, &v7->padding_0[92]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 78, &v7->padding_0[96]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 79, &v7->padding_0[100]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 56, &v7->padding_0[104]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 57, &v7->padding_0[108]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 58, &v7->padding_0[112]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 59, &v7->padding_0[116]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 60, &v7->padding_0[120]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 61, &v7->padding_0[124]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 62, &v7->padding_0[128]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 63, &v7->padding_0[132]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 64, &v7->padding_0[0x88]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 65, &v7->padding_0[140]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 66, &v7->padding_0[144]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 67, &v7->padding_0[148]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 40, &v7->padding_0[152]);
    sub_1035a196(&/* unsupported instruction */, 1, v4, 41, &v7->padding_0[156]);
    sub_1035a196(&/* unsupported instruction */, 1, v3, 31, &v7->padding_0[160]);
    sub_1035a196(&/* unsupported instruction */, 1, v3, 32, &v7->padding_0[164]);
    sub_1035a196(&/* unsupported instruction */, 1, v3, 4099, &v7->padding_0[168]);
    sub_1035a196(&/* unsupported instruction */, 0, v3, 4105, v7 + 1);
    v7->field_ac = v3;
    return;
}
```

## `sub_1035ea56` `0x1035ea56`

_400 bytes. (leaf/helper — see body)_

```c
void sub_1035ea56(unsigned int *idx)
{
    unsigned int v0;  // [bp-0x44]
    unsigned int v1;  // [bp-0x40]
    unsigned int v2;  // [bp-0x3c]
    unsigned int v3;  // [bp-0x38]
    unsigned int v4;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    if (!idx)
        return;
    v15 = idx[1];
    sub_1035345e();
    v14 = idx[2];
    sub_1035345e();
    v13 = idx[3];
    sub_1035345e();
    v12 = idx[4];
    sub_1035345e();
    v11 = idx[5];
    sub_1035345e();
    v10 = idx[6];
    sub_1035345e();
    v9 = *(idx);
    sub_1035345e();
    v8 = idx[8];
    sub_1035345e();
    v7 = idx[9];
    sub_1035345e();
    v6 = idx[10];
    sub_1035345e();
    v5 = idx[11];
    sub_1035345e();
    v4 = idx[12];
    sub_1035345e();
    v3 = idx[13];
    sub_1035345e();
    v2 = idx[7];
    sub_1035345e();
    v1 = idx[14];
    sub_1035345e();
    v0 = idx[15];
    sub_1035345e();
    v15 = idx[16];
    sub_1035345e();
    v14 = idx[0x11];
    sub_1035345e();
    v13 = idx[18];
    sub_1035345e();
    v12 = idx[19];
    sub_1035345e();
    v11 = idx[20];
    sub_1035345e();
    v10 = idx[21];
    sub_1035345e();
    v9 = idx[22];
    sub_1035345e();
    v8 = idx[23];
    sub_1035345e();
    v7 = idx[24];
    sub_1035345e();
    v6 = idx[25];
    sub_1035345e();
    v5 = idx[26];
    sub_1035345e();
    v4 = idx[27];
    sub_1035345e();
    v3 = idx[28];
    sub_1035345e();
    v2 = idx[29];
    sub_1035345e();
    v1 = idx[30];
    sub_1035345e();
    v0 = idx[31];
    sub_1035345e();
    v15 = idx[32];
    sub_1035345e();
    v14 = idx[33];
    sub_1035345e();
    v13 = idx[0x22];
    sub_1035345e();
    v12 = idx[35];
    sub_1035345e();
    v11 = idx[36];
    sub_1035345e();
    v10 = idx[37];
    sub_1035345e();
    v9 = idx[38];
    sub_1035345e();
    v8 = idx[39];
    sub_1035345e();
    v7 = idx[40];
    sub_1035345e();
    v6 = idx[41];
    sub_1035345e();
    v5 = idx[42];
    sub_1035345e();
    return;
}
```

## `sub_1035ebe6` `0x1035ebe6`

_115 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1f0;
extern char g_1038e200;

unsigned int sub_1035ebe6(void* a0)
{
    unsigned int v4;  // ebx
    unsigned int v5;  // esi
    unsigned int v6;  // edi
    unsigned int v7;  // esi
    void* v8;  // edi
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x4]

    v3 = v4;
    v2 = v5;
    v1 = v6;
    if ((int)a0[32])
    {
        v7 = sub_103574c2(1, 184);
        if (!v7)
            return 1;
        if (sub_1035e63d())
        {
            sub_1035ea56(v7);
            v0 = v7;
            sub_1035345e();
        }
        else
        {
            *((unsigned int *)(v7 + 180)) = 1;
            goto LABEL_1035ec38;
        }
        return 1;
    }
    else
    {
        v7 = &g_1038e200;
LABEL_1035ec38:
        v8 = a0 + 212;
        if (*((int *)v8) != &g_1038e200)
            g_1038b1f0(*((int *)v8) + 180);
        *((unsigned int *)v8) = v7;
        return 0;
    }
}
```

## `sub_1035ec59` `0x1035ec59`

_64 bytes. (leaf/helper — see body)_

```c
extern char g_1038e1b4;
extern char g_1038e1b8;
extern char g_1038e1bc;

int sub_1035ec59(unsigned int *idx)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (!idx)
        return v2;
    if (*(idx) != *((int *)&g_1038e1b4))
    {
        v0 = *(idx);
        sub_1035345e();
    }
    v1 = idx[1];
    if (v1 != *((int *)&g_1038e1b8))
    {
        v0 = v1;
        v1 = (unsigned int)sub_1035345e();
    }
    if (idx[2] == *((int *)&g_1038e1bc))
        return v1;
    v0 = idx[2];
    return (unsigned int)sub_1035345e();
}
```

## `sub_1035ec99` `0x1035ec99`

_456 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
    unsigned int field_1c;
    char padding_20[30];
    unsigned short field_3e;
    char padding_40[112];
    int field_b0;
    int field_b4;
    char padding_b8[4];
    struct struct_0 *field_bc;
} struct_2;

typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    struct struct_1 *field_8;
} struct_0;

typedef struct struct_1 {
    char field_0;
    char field_1;
} struct_1;

typedef struct struct_6 {
    unsigned int field_0;
} struct_6;

extern struct_6 *g_1038b1f0;
extern struct_0 g_1038e1b4;
extern unsigned int g_1038e1b8;
extern struct_1 *g_1038e1bc;

unsigned int sub_1035ec99(struct_2 *idx)
{
    unsigned int v13;  // ebx
    unsigned int v14;  // esi
    char v23[2];  // edi
    struct_0 *index;  // eax
    unsigned int v15;  // edi
    struct_0 *node;  // edi
    struct_0 *i;  // esi
    unsigned int v18;  // esi
    struct_0 *v19;  // esi
    unsigned int v20;  // edi
    char iter[2];  // eax
    char v22;  // cl
    struct_0 *v0;  // [bp-0x38]
    int v1;  // [bp-0x34]
    int v2;  // [bp-0x30]
    struct_0 *iter1;  // [bp-0x2c], Other Possible Types: unsigned int
    unsigned int v4;  // [bp-0x28]
    unsigned int v5;  // [bp-0x24]
    unsigned int v6;  // [bp-0x20]
    struct_2 *v7;  // [bp-0x1c]
    unsigned int v8;  // [bp-0x18]
    struct_0 *v9;  // [bp-0x14]
    int v10;  // [bp-0x10], Other Possible Types: unsigned int
    int v11;  // [bp-0xc]
    int v12;  // [bp-0x8]

    v6 = v13;
    v5 = v14;
    v4 = v15;
    v7 = idx;
    v8 = 0;
    if (!idx->field_1c && !idx->field_18)
    {
        v12 = 0;
        v11 = 0;
        idx = &g_1038e1b4.field_0;
        goto LABEL_1035ee03;
    }
    node = sub_103574c2(1, 48);
    idx = node;
    if (!node)
        return 1;
    i = idx->field_bc;
    for (iter1 = 12; iter1; i = &i->field_4)
    {
        iter1 -= 1;
        node->field_0 = i->field_0;
        node = &node->field_4;
    }
    v11 = sub_10357482(4);
    if (!v11)
    {
        iter1 = idx;
        sub_1035345e();
    }
    else
    {
        *((unsigned int *)v11) = 0;
        if (idx->field_1c)
        {
            v12 = sub_10357482(4);
            if (!v12)
            {
                v18 = 1;
            }
            else
            {
                *((unsigned int *)v12) = 0;
                v19 = idx;
                v20 = idx->field_3e;
                v10 = sub_1035a196(&v7, 1, v20, 14, v19);
                v10 |= sub_1035a196(&v7, 1, v20, 15, &v19->field_4);
                v9 = &v19->field_8;
                if (sub_1035a196(&v7, 1, v20, 16, v9) || v10)
                {
                    sub_1035ec59(v19);
                    v18 = 4294967295;
                }
                else
                {
                    iter = v9->field_0;
                    while (iter[0])
                    {
                        v22 = iter[0];
                        if (iter[0] >= 48 && v22 <= 57)
                        {
                            iter[0] = v22 - 48;
                            iter = &iter[1];
                        }
                        else if (v22 != 59)
                        {
                            iter = &iter[1];
                        }
                        else
                        {
                            do
                            {
                                v23 = &iter[1];
                                iter[0] = v23[0];
                                iter = v23;
                            } while (iter[0]);
                        }
                    }
                    goto LABEL_1035edf2;
                }
            }
            iter1 = idx;
            sub_1035345e();
            v2 = v11;
            sub_1035345e();
            return v18;
        }
        else
        {
            index = idx;
            index->field_0 = g_1038e1b4.field_0;
            index->field_4 = g_1038e1b8;
            v12 = 0;
            index->field_8 = g_1038e1bc;
LABEL_1035edf2:
            *((unsigned int *)v11) = 1;
            if (v12)
                *((unsigned int *)v12) = 1;
LABEL_1035ee03:
            if (idx->field_b4)
                g_1038b1f0(idx->field_b4);
            if (idx->field_b0 && !g_1038b1f0(idx->field_b0))
            {
                v1 = idx->field_b0;
                sub_1035345e();
                v0 = idx->field_bc;
                sub_1035345e();
            }
            idx->field_b4 = v12;
            idx->field_b0 = v11;
            idx->field_bc = idx;
            return 0;
        }
    }
    return 1;
}
```

## `sub_1035ee61` `0x1035ee61`

_137 bytes. (leaf/helper — see body)_

```c
extern char g_1038e1c0;
extern char g_1038e1c4;
extern char g_1038e1c8;
extern char g_1038e1cc;
extern char g_1038e1d0;
extern char g_1038e1d4;
extern char g_1038e1d8;

int sub_1035ee61(unsigned int *idx)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (!idx)
        return v2;
    if (idx[3] != *((int *)&g_1038e1c0))
    {
        v0 = idx[3];
        sub_1035345e();
    }
    if (idx[4] != *((int *)&g_1038e1c4))
    {
        v0 = idx[4];
        sub_1035345e();
    }
    if (idx[5] != *((int *)&g_1038e1c8))
    {
        v0 = idx[5];
        sub_1035345e();
    }
    if (idx[6] != *((int *)&g_1038e1cc))
    {
        v0 = idx[6];
        sub_1035345e();
    }
    if (idx[7] != *((int *)&g_1038e1d0))
    {
        v0 = idx[7];
        sub_1035345e();
    }
    v1 = idx[8];
    if (v1 != *((int *)&g_1038e1d4))
    {
        v0 = v1;
        v1 = (unsigned int)sub_1035345e();
    }
    if (idx[9] == *((int *)&g_1038e1d8))
        return v1;
    v0 = idx[9];
    return (unsigned int)sub_1035345e();
}
```

## `sub_1035eeea` `0x1035eeea`

_708 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    char padding_0[24];
    unsigned int field_18;
    unsigned int field_1c;
    char padding_20[24];
    unsigned short field_38;
    char padding_3a[118];
    int field_b0;
    char padding_b4[4];
    int field_b8;
    struct struct_0 *field_bc;
} struct_2;

typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    char padding_c[16];
    struct struct_1 *field_1c;
} struct_0;

typedef struct struct_1 {
    char field_0;
    char field_1;
} struct_1;

typedef struct struct_5 {
    unsigned int field_0;
} struct_5;

extern struct_5 *g_1038b1f0;
extern struct_0 g_1038e1b4;

unsigned int sub_1035eeea(struct_2 *a0)
{
    unsigned int v11;  // ebx
    unsigned int v12;  // esi
    int v21;  // eax
    int v22;  // eax
    int v23;  // eax
    unsigned int v24;  // edi
    int v25;  // eax
    int v26;  // eax
    int v27;  // eax
    int v28;  // eax
    int v29;  // eax
    int v30;  // eax
    struct_2 *v13;  // esi
    int v31;  // eax
    unsigned int iter;  // eax
    char v33;  // cl
    unsigned int v34;  // edi
    struct_0 *i;  // esi
    struct_0 *node;  // edi
    struct_2 *v37;  // eax
    unsigned int v14;  // edi
    struct_0 *index;  // ebx
    struct_2 *idx;  // esi
    unsigned int v17;  // esi
    int v18;  // eax
    int v19;  // eax
    int v20;  // eax
    int v0;  // [bp-0x30]
    struct_0 *v1;  // [bp-0x2c], Other Possible Types: int
    struct_0 *v2;  // [bp-0x28], Other Possible Types: int
    struct_0 *iter1;  // [bp-0x24], Other Possible Types: unsigned int
    unsigned int v4;  // [bp-0x20]
    unsigned int v5;  // [bp-0x1c]
    unsigned int v6;  // [bp-0x18]
    struct_2 *v7;  // [bp-0x14]
    unsigned int v8;  // [bp-0x10]
    int v9;  // [bp-0xc]
    int v10;  // [bp-0x8]

    v6 = v11;
    v5 = v12;
    v13 = a0;
    v4 = v14;
    v10 = 0;
    v7 = v13;
    v8 = 0;
    if (!v13->field_18 && !v13->field_1c)
    {
        v10 = 0;
        v9 = 0;
        index = &g_1038e1b4.field_0;
        idx = v13;
        goto LABEL_1035f151;
    }
    index = sub_103574c2(1, 48);
    if (!index)
        return 1;
    v9 = sub_10357482(4);
    if (!v9)
    {
        iter1 = index;
        sub_1035345e();
        goto LABEL_1035ef49;
    }
    else
    {
        *((unsigned int *)v9) = 0;
        if (!v13->field_18)
        {
            iter1 = 12;
            i = &g_1038e1b4.field_0;
            for (node = index; iter1; i = &i->field_4)
            {
                iter1 -= 1;
                node->field_0 = i->field_0;
                node = &node->field_4;
            }
LABEL_1035f11c:
            v37 = &a0->field_bc;
            index->field_0 = *((int *)*((int *)&v37->padding_0[0]));
            index->field_4 = *((int *)(*((int *)&v37->padding_0[0]) + 4));
            index->field_8 = *((int *)(*((int *)&v37->padding_0[0]) + 8));
            *((unsigned int *)v9) = 1;
            idx = a0;
            if (v10)
            {
                *((unsigned int *)v10) = 1;
                idx = a0;
            }
LABEL_1035f151:
            if (idx->field_b8)
                g_1038b1f0(idx->field_b8);
            if (idx->field_b0 && !g_1038b1f0(idx->field_b0))
            {
                v1 = idx->field_bc;
                sub_1035345e();
                v0 = idx->field_b0;
                sub_1035345e();
            }
            idx->field_b8 = v10;
            idx->field_b0 = v9;
            idx->field_bc = index;
            return 0;
        }
        v10 = sub_10357482(4);
        if (!v10)
        {
            iter1 = index;
            sub_1035345e();
            v2 = v9;
            sub_1035345e();
LABEL_1035ef49:
        }
        else
        {
            *((unsigned int *)v10) = 0;
            v17 = v13->field_38;
            v18 = sub_1035a196(&v7, 1, v17, 21, index->padding_c);
            v19 = sub_1035a196(&v7, 1, v17, 20, &index->padding_c[4]);
            v20 = sub_1035a196(&v7, 1, v17, 22, &index->padding_c[8]);
            v21 = sub_1035a196(&v7, 1, v17, 23, &index->padding_c[12]);
            v22 = sub_1035a196(&v7, 1, v17, 24, &index->field_1c);
            v23 = sub_1035a196(&v7, 1, v17, 80, index + 1);
            v24 = v18 | v19 | v20 | v21 | v22 | v23 | sub_1035a196(&v7, 1, v17, 81, &index[1].field_4);
            v25 = sub_1035a196(&v7, 0, v17, 26, &index[1].field_8);
            v26 = sub_1035a196(&v7, 0, v17, 25, (char *)&index[1].field_8 + 1);
            v27 = sub_1035a196(&v7, 0, v17, 84, (char *)&index[1].field_8 + 2);
            v28 = sub_1035a196(&v7, 0, v17, 0x55, (char *)&index[1].field_8 + 3);
            v29 = sub_1035a196(&v7, 0, v17, 86, index[1].padding_c);
            v30 = sub_1035a196(&v7, 0, v17, 87, &index[1].padding_c[1]);
            v31 = sub_1035a196(&v7, 0, v17, 82, &index[1].padding_c[2]);
            if (sub_1035a196(&v7, 0, v17, 83, &index[1].padding_c[3]) || v24 || v25 || v26 || v27 || v28 || v29 || v30 || v31)
            {
                sub_1035ee61(index);
                v2 = index;
                sub_1035345e();
                v1 = v9;
                sub_1035345e();
                v0 = v10;
                sub_1035345e();
            }
            else
            {
                iter = index->field_1c;
                while (*((char *)iter))
                {
                    v33 = *((char *)iter);
                    if (*((char *)iter) >= 48 && v33 <= 57)
                    {
                        *((char *)iter) = v33 - 48;
                        iter += 1;
                    }
                    else if (v33 != 59)
                    {
                        iter += 1;
                    }
                    else
                    {
                        do
                        {
                            v34 = iter + 1;
                            *((char *)iter) = *((char *)v34);
                            iter = v34;
                        } while (*((char *)iter));
                    }
                }
                goto LABEL_1035f11c;
            }
        }
    }
    return 1;
}
```

## `sub_1035f1ae` `0x1035f1ae`

_3 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1035f1ae(void)
{
    return 0;
}
```

## `sub_1035f1b1` `0x1035f1b1`

_113 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1035f1b1(char *a0, unsigned int a1, char *node)
{
    char *v5;  // eax
    unsigned int v6;  // edi
    char *v7;  // edx
    char *iter;  // edx
    unsigned int v10;  // edi
    char v11;  // 4103
    unsigned int v14;  // esi
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
            if (node)
            {
                v7 = v5;
                do
                {
                    iter = v7;
                } while (*(iter) && (iter += 1, v6 -= 1, v7 = iter, v6 != 1));
                v10 = v6;
                if (v10)
                {
                    do
                    {
                        v11 = *(node);
                        *(iter) = *(node);
                        iter += 1;
                        node += 1;
                    } while (v11 && (v10 -= 1, v10 != 1));
                    if (v10)
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
                    return v14;
                }
            }
            *(v5) = 0;
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

## `sub_1035f222` `0x1035f222`

_179 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1035f222(char *a0, unsigned int a1, char *a2, unsigned int a3)
{
    unsigned int v6;  // edi
    char *node;  // edx
    char *iter;  // eax
    char v9;  // 4103
    char v11;  // 4103
    unsigned int v12;  // edi
    unsigned int v14;  // esi
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp+0x10]

    if (!a3)
    {
        if (a0)
            goto LABEL_1035f246;
        if (!a1)
            return 0;
    }
    else if (a0)
    {
LABEL_1035f246:
        v6 = a1;
        if (v6 > 0)
        {
            if (!a3)
            {
                *(a0) = 0;
                return 0;
            }
            node = a2;
            if (!node)
            {
                *(a0) = 0;
            }
            else
            {
                iter = a0;
                if (a3 == 4294967295)
                {
                    do
                    {
                        v9 = *(node);
                        *(iter) = *(node);
                        iter += 1;
                        node += 1;
                    } while (v9 && (v6 -= 1, v6 != 1));
                }
                else
                {
                    do
                    {
                        v11 = *(node);
                        *(iter) = *(node);
                        iter += 1;
                        node += 1;
                    } while (v11 && (v12 = v6 - 1, v6 = v12, v6 != 1 && (v5 = a3 - 1, a3 = v5, v6 = v12, a3 != 1)));
                    if (!a3)
                        *(iter) = 0;
                }
                if (v6)
                {
                    return 0;
                }
                else if (a3 == 4294967295)
                {
                    v4 = 80;
                    a0[1 + a1] = 0;
                    return v4;
                }
                else
                {
                    *(a0) = 0;
                    v4 = 0x22;
                    *((unsigned int *)sub_103575e0()) = v4;
                    v4 = 0;
                    v3 = 0;
                    v2 = 0;
                    v1 = 0;
                    v0 = 0;
                    sub_103535f2();
                    return v14;
                }
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

## `sub_1035f2d5` `0x1035f2d5`

_96 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

int sub_1035f2d5(unsigned int a0, int a1, struct_0 **a2)
{
    int i;  // ebx
    int v3;  // eax
    unsigned int v4;  // esi
    unsigned int v5;  // edi
    int v6;  // esi
    char **v7;  // edi
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]

    i = 0;
    v3 = 1;
    if (a1 >= 0)
    {
        v1 = v4;
        v0 = v5;
        do
        {
            if (!v3)
                break;
            v6 = (a1 + i) / 2;
            v7 = a0 + v6 * 8;
            v3 = sub_1035ddf8(*(a2), *(v7));
            if (!v3)
            {
                *(a2) = v7 + 1;
            }
            else if (v3 < 0)
            {
                a1 = v6 - 1;
            }
            else
            {
                i = v6 + 1;
            }
        } while (i <= a1);
    }
    return !v3;
}
```

## `sub_1035f335` `0x1035f335`

_119 bytes. refs "ACP", "OCP"_

```c
typedef struct struct_0 {
    char padding_0[28];
    unsigned int field_1c;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b1e4;
extern unsigned int g_1038e180;

void sub_1035f335(char *a0)
{
    unsigned int v8;  // esi
    char *v9;  // esi
    struct_0 *v10;  // edi
    unsigned int v0;  // [bp-0x20]
    char *v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    char v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]

    v5 = g_1038e180 ^ &v6;
    v3 = v8;
    v9 = a0;
    if (!(v9 && *(v9) && sub_10359ed0(v9, "ACP")))
    {
        v2 = 8;
        v1 = &v4;
        v0 = 4100;
    }
    else if (!sub_10359ed0(v9, "OCP"))
    {
        v2 = 8;
        v1 = &v4;
        v0 = 11;
    }
    else
    {
        sub_10363c11(v9);
        sub_10351225();
        return;
    }
    if (g_1038b1e4(v10->field_1c))
    {
        v9 = &v4;
        sub_10363c11(v9);
        sub_10351225();
    }
    else
    {
        sub_10351225();
    }
    return;
}
```

## `sub_1035f3ac` `0x1035f3ac`

_30 bytes. (leaf/helper — see body)_

```c
extern char g_10396010;

unsigned int sub_1035f3ac(unsigned short i)
{
    unsigned int v0;  // eax

    v0 = 0;
    while (i != *((short *)&(&g_10396010)[v0]))
    {
        v0 += 2;
        if (v0 >= 20)
            return 1;
    }
    return 0;
}
```

## `sub_1035f3ca` `0x1035f3ca`

_50 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1035f3ca(unsigned int a0, char *iter)
{
    unsigned int v1;  // esi
    char node;  // cl

    v1 = 0;
    while (true)
    {
        node = *(iter);
        if (!*(iter))
            break;
        iter += 1;
        if (node - 97 <= 5)
        {
            node -= 39;
        }
        else if (node - 65 <= 5)
        {
            node -= 7;
        }
        v1 = v1 * 16 + node - 48;
    }
    return v1;
}
```

## `sub_1035f3fc` `0x1035f3fc`

_27 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1035f3fc(unsigned int a0, char *a1)
{
    unsigned int v1;  // eax
    char *v2;  // edx
    char *v3;  // edx

    v1 = 0;
    while (true)
    {
        v2 = a1;
        v3 = v2 + 1;
        if ((*(v2) < 65 || *(v2) > 90) && *(v2) - 97 > 25)
            break;
        v1 += 1;
        a1 = v3;
    }
    return v1;
}
```

## `sub_1035f417` `0x1035f417`

_150 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[160];
    char *field_a0;
    unsigned int field_a4;
    char padding_a8[8];
    unsigned int field_b0;
    unsigned int field_b4;
    unsigned int field_b8;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b1e4;
extern unsigned int g_1038e180;

int sub_1035f417(char *a0)
{
    unsigned int v5;  // esi
    unsigned int v6;  // edi
    struct_0 *idx;  // esi
    unsigned int v8;  // ecx
    unsigned int v9;  // edi
    unsigned int v0;  // [bp-0x88]
    unsigned int v1;  // [bp-0x84]
    char v2[120];  // [bp-0x80]
    unsigned int v3;  // [bp-0x8]
    char v4;  // [bp-0x4]

    v3 = g_1038e180 ^ &v4;
    v1 = v5;
    v0 = v6;
    idx = &(sub_10358da8())[19 + 1];
    v9 = sub_1035f3ca(v8, a0);
    if (!g_1038b1e4(v9, (-(0 < *((int *)&idx->padding_0[20])) & 4294963205) + 4098, v2, 120))
    {
        *((unsigned int *)&idx->padding_0[8]) = 0;
    }
    else if (!sub_1035ddf8(*((int *)&idx->padding_0[4]), v2) && sub_1035f3ac(v9))
    {
        *((unsigned int *)&idx->padding_0[8]) = *((int *)&idx->padding_0[8]) | 4;
        *((unsigned int *)&idx->padding_0[28]) = v9;
        *((unsigned int *)&idx->padding_0[24]) = v9;
    }
    return sub_10351225();
}
```

## `sub_1035f4ad` `0x1035f4ad`

_114 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1035f4ad(void* *a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]

    v2 = g_1038e180 ^ &v3;
    return sub_10351225();
}
```

## `sub_1035f51f` `0x1035f51f`

_464 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1e4;
extern unsigned int g_1038e180;

int sub_1035f51f(char *a0)
{
    unsigned int v7;  // ebx
    unsigned int v8;  // esi
    unsigned int v9;  // edi
    void* idx;  // esi
    unsigned int v11;  // ecx
    unsigned int v12;  // edi
    int v13;  // eax
    unsigned int v14;  // edx
    int v15;  // eax
    unsigned int v0;  // [bp-0xc0]
    unsigned int v1;  // [bp-0x8c]
    unsigned int v2;  // [bp-0x88]
    unsigned int v3;  // [bp-0x84]
    char v4[120];  // [bp-0x80]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]

    v5 = g_1038e180 ^ &v6;
    v3 = v7;
    v2 = v8;
    v1 = v9;
    idx = &(sub_10358da8())[19 + 1];
    v12 = sub_1035f3ca(v11, a0);
    if (!g_1038b1e4(v12, (-(0 < (int)idx[20]) & 4294963205) + 4098, v4, 120))
    {
        *((unsigned int *)&idx[8]) = 0;
    }
    else
    {
        if (!sub_1035ddf8((int)idx[4], v4) && g_1038b1e4(v12, (-(0 < (int)idx[16]) & 4294963202) + 4097, v4, 120))
        {
            if (!sub_1035ddf8(*((int *)idx), v4))
            {
                *((unsigned int *)&idx[8]) = (int)idx[8] | 772;
                *((unsigned int *)&idx[24]) = v12;
                goto LABEL_1035f620;
            }
            else if (!((char)idx[8] & 2))
            {
                if ((int)idx[12] && !sub_10363e79(*((int *)idx), v4, (int)idx[12]))
                {
                    *((unsigned int *)&idx[8]) = (int)idx[8] | 2;
                    *((unsigned int *)&idx[28]) = v12;
                    v13 = sub_10352f20(*((int *)idx));
                    if (v13 == (int)idx[12])
                    {
                        *((unsigned int *)&idx[24]) = v12;
                        goto LABEL_1035f623;
                    }
                }
                else if (!((char)(int)idx[8] & 1) && sub_1035f3ac(v12))
                {
                    *((unsigned int *)&idx[8]) = v14 | 1;
LABEL_1035f620:
                    *((unsigned int *)&idx[28]) = v12;
                    goto LABEL_1035f623;
                }
            }
        }
LABEL_1035f623:
        if (((short)(int)idx[8] & 0x300) == 0x300)
        {
LABEL_1035f6d3:
        }
        else if (g_1038b1e4(v12, (-(0 < (int)idx[16]) & 4294963202) + 4097, v4, 120))
        {
            if (!sub_1035ddf8(*((int *)idx), v4))
            {
                *((unsigned int *)&idx[8]) = (int)idx[8] | 0x200;
                if ((int)idx[16])
                {
                    *((unsigned int *)&idx[8]) = (int)idx[8] | 0x100;
                    goto LABEL_1035f6cb;
                }
                else
                {
                    if (!(int)idx[12] || (v15 = sub_10352f20(*((int *)idx)), v15 != (int)idx[12]))
                        goto LABEL_1035f6c4;
                    v0 = 1;
                }
            }
            else
            {
                if ((int)idx[16] || !(int)idx[12] || sub_1035ddf8(*((int *)idx), v4))
                    goto LABEL_1035f6d3;
                v0 = 0;
            }
            if (sub_1035f4ad(idx, v14, v12, v0))
            {
LABEL_1035f6c4:
                *((unsigned int *)&idx[8]) = (int)idx[8] | 0x100;
LABEL_1035f6cb:
                if (!(int)idx[24])
                {
                    *((unsigned int *)&idx[24]) = v12;
                    goto LABEL_1035f6d3;
                }
            }
        }
    }
    return sub_10351225();
}
```

## `sub_1035f6ef` `0x1035f6ef`

_191 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[156];
    char *field_9c;
    char padding_a0[4];
    unsigned int field_a4;
    unsigned int field_a8;
    unsigned int field_ac;
    char padding_b0[4];
    unsigned int field_b4;
    unsigned int field_b8;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b1e4;
extern unsigned int g_1038e180;

int sub_1035f6ef(char *a0)
{
    unsigned int v6;  // esi
    unsigned int v7;  // edi
    struct_0 *idx;  // esi
    unsigned int v9;  // ecx
    unsigned int v10;  // edi
    unsigned int v11;  // edx
    unsigned int v0;  // [bp-0x9c]
    unsigned int v1;  // [bp-0x88]
    unsigned int v2;  // [bp-0x84]
    char v3[120];  // [bp-0x80]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = g_1038e180 ^ &v5;
    v2 = v6;
    v1 = v7;
    idx = &(sub_10358da8())[19 + 1];
    v10 = sub_1035f3ca(v9, a0);
    if (!g_1038b1e4(v10, (-(0 < *((int *)&idx->padding_0[16])) & 4294963202) + 4097, v3, 120))
    {
        *((unsigned int *)&idx->padding_0[8]) = 0;
    }
    else
    {
        if (!sub_1035ddf8(*((int *)&idx->padding_0[0]), v3))
        {
            if (*((int *)&idx->padding_0[16]))
                goto LABEL_1035f789;
            v0 = 1;
        }
        else
        {
            if (*((int *)&idx->padding_0[16]) || !*((int *)&idx->padding_0[12]) || sub_1035ddf8(*((int *)&idx->padding_0[0]), v3))
                goto LABEL_1035f793;
            v0 = 0;
        }
        if (sub_1035f4ad(idx, v11, v10, v0))
        {
LABEL_1035f789:
            *((unsigned int *)&idx->padding_0[8]) = *((int *)&idx->padding_0[8]) | 4;
            *((unsigned int *)&idx->padding_0[24]) = v10;
            *((unsigned int *)&idx->padding_0[28]) = v10;
        }
LABEL_1035f793:
    }
    return sub_10351225();
}
```

## `sub_1035f7ae` `0x1035f7ae`

_101 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1e0;

unsigned int sub_1035f7ae(void)
{
    void* idx;  // esi
    int v3;  // eax
    unsigned int v4;  // 4115
    unsigned int v5;  // eax
    unsigned int v6;  // eax
    unsigned int v0;  // [bp-0x4]

    *((unsigned int *)&idx[16]) = -(0 < sub_10352f20(*((int *)idx)) - 3) + 1;
    v3 = sub_10352f20((int)idx[4]);
    *((unsigned int *)&idx[24]) = 0;
    v4 = (int)idx[16];
    *((unsigned int *)&idx[20]) = -(0 < v3 - 3) + 1;
    if (v4)
    {
        v0 = 2;
        v5 = 2;
    }
    else
    {
        v5 = sub_1035f3fc(*((int *)idx), *((int *)idx));
    }
    *((unsigned int *)&idx[12]) = v5;
    g_1038b1e0(sub_1035f51f, 1);
    v6 = (int)idx[8];
    if (((unsigned short)v6 & 0x100) && ((unsigned short)v6 & 0x200) && ((char)v6 & 7))
        return v6;
    *((unsigned int *)&idx[8]) = 0;
    return v6;
}
```

## `sub_1035f813` `0x1035f813`

_60 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1e0;

unsigned int sub_1035f813(void)
{
    void* idx;  // esi
    int v3;  // eax
    unsigned int v4;  // eax
    unsigned int v5;  // 4141
    unsigned int v6;  // 4142
    unsigned int v7;  // eax
    unsigned int v8;  // eax
    unsigned int v0;  // [bp-0x4]

    v3 = sub_10352f20(*((int *)idx)) - 3;
    v4 = -(0 < v3);
    v5 = _ccall(12, 0, (unsigned int)(char)(0 < v3), (unsigned int)(char)(0 < v3));
    *((unsigned int *)&idx[16]) = v4 + 1;
    v6 = _ccall(4, 18, v4 + 1, 0, v5);
    if (!((char)v6))
    {
        v0 = 2;
        v7 = 2;
    }
    else
    {
        v7 = sub_1035f3fc(*((int *)idx), *((int *)idx));
    }
    *((unsigned int *)&idx[12]) = v7;
    v8 = g_1038b1e0(sub_1035f6ef, 1);
    if (!((char)idx[8] & 4))
        *((unsigned int *)&idx[8]) = 0;
    return v8;
}
```

## `sub_1035f84f` `0x1035f84f`

_483 bytes. refs "Norwegian-Nynorsk"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1b0;
extern struct_0 *g_1038b1e0;
extern struct_0 *g_1038b1e4;
extern struct_0 *g_1038b1e8;
extern struct_0 *g_1038b264;
extern unsigned int g_10395d50;
extern unsigned int g_10395f58;

unsigned int sub_1035f84f(char *a0)
{
    unsigned int v7;  // ebx
    unsigned int v8;  // edi
    void* idx;  // esi
    char v10[65];  // eax
    void* v11;  // edi
    char v12[65];  // eax
    char v13[65];  // edi
    unsigned int v14;  // eax
    unsigned int v15;  // ebx
    unsigned short index[3];  // esi
    unsigned int v0;  // [bp-0x38]
    unsigned int v1;  // [bp-0x34]
    unsigned int v2;  // [bp-0x30]
    unsigned int v3;  // [bp-0x2c]
    unsigned int v4;  // [bp-0x28]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0x4]

    v6 = v7;
    v5 = v8;
    idx = &(sub_10358da8())[19 + 1];
    if (!a0)
    {
        *((unsigned int *)&idx[8]) = (int)idx[8] | 260;
        goto LABEL_1035f927;
    }
    else
    {
        v10 = a0 + 64;
        v11 = idx + 4;
        *((char **)idx) = a0;
        *((char *[65])v11) = v10;
        if (v10 && v10[0])
            sub_1035f2d5(&g_10395f58, 22, v11);
        v12 = *((int *)idx);
        *((unsigned int *)&idx[8]) = 0;
        if (v12 && v12[0])
        {
            if (*((int *)v11) && *((char *)*((int *)v11)))
                sub_1035f7ae();
            else
                sub_1035f813();
            if ((int)idx[8])
                goto LABEL_1035f93c;
            if (sub_1035f2d5(&g_10395d50, 64, idx))
            {
                if (*((int *)v11) && *((char *)*((int *)v11)))
                    sub_1035f7ae();
                else
                    sub_1035f813();
            }
        }
        else
        {
            v13 = *((int *)v11);
            if (v13 && v13[0])
            {
                *((unsigned int *)&idx[20]) = -(0 < sub_10352f20(v13) - 3) + 1;
                g_1038b1e0(sub_1035f417, 1);
                if (!((char)idx[8] & 4))
                    *((unsigned int *)&idx[8]) = 0;
            }
            else
            {
                *((unsigned int *)&idx[8]) = 260;
LABEL_1035f927:
                v14 = g_1038b1e8();
                *((unsigned int *)&idx[24]) = v14;
                *((unsigned int *)&idx[28]) = v14;
            }
        }
        if (!(int)idx[8])
            return 0;
LABEL_1035f93c:
        v15 = (unsigned int)sub_1035f335(-(NULL < a0) & a0 + 128);
        if (!v15 || v15 == 65000 || v15 == 65001 || !g_1038b264((unsigned short)v15) || !g_1038b1b0((int)idx[24], 1))
            return 0;
        if (index)
        {
            index[0] = (short)idx[24];
            index[1] = (short)idx[28];
            index[2] = v15;
        }
        if (!/* unsupported instruction */)
            return 1;
        if (index[0] == 2068)
        {
            if (sub_10359f58(/* unsupported instruction */, 64, "Norwegian-Nynorsk"))
            {
                v4 = 0;
                v3 = 0;
                v2 = 0;
                v1 = 0;
                v0 = 0;
                sub_103534f6();
            }
LABEL_1035f9fe:
            if (g_1038b1e4((int)idx[28], 4098, /* unsupported instruction */ + 64, 64))
            {
                sub_10358719(v15, /* unsupported instruction */ + 128, 16, 10);
                return 1;
            }
        }
        else if (!(!g_1038b1e4((int)idx[24], 4097, /* unsupported instruction */, 64)))
        {
            goto LABEL_1035f9fe;
        }
        return 0;
    }
}
```

## `sub_1035fa32` `0x1035fa32`

_440 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
    char padding_8[12];
    int field_14;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b07c;
extern struct_1 *g_1038b104;
extern struct_1 *g_1038b1a8;
extern struct_1 *g_1038b1ac;
extern unsigned int g_1038e180;
extern char g_1039487c;
extern unsigned int g_103a3a48;

int sub_1035fa32(struct_0 **a0, unsigned int a1, unsigned int a2, int a3, unsigned int a4, unsigned int a5, unsigned int a6, int a7, unsigned int a8)
{
    unsigned int v8;  // eax
    unsigned int v9;  // ebx
    unsigned int v18;  // eax
    unsigned int v10;  // esi
    unsigned int *v11;  // ebx
    unsigned int v12;  // edi
    int v13;  // edi
    unsigned int v14;  // eax
    unsigned int *iter;  // eax
    unsigned int v16;  // eax
    int v17;  // esi
    int v0;  // [bp-0x40], Other Possible Types: unsigned int
    unsigned int v1;  // [bp-0x2c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    struct_0 **v5;  // [bp-0xc], Other Possible Types: unsigned int
    struct_0 **v6;  // [bp-0x8], Other Possible Types: unsigned int
    char v7;  // [bp-0x4]

    v6 = a0;
    v5 = a0;
    v6 = g_1038e180 ^ &v7;
    v8 = g_103a3a48;
    v4 = v9;
    v3 = v10;
    v11 = NULL;
    v2 = v12;
    if (!v8)
    {
        if (g_1038b1a8(1, &g_1039487c, 1, &v5))
        {
            g_103a3a48 = 1;
            goto LABEL_1035faa5;
        }
        else if (g_1038b07c() == 120)
        {
            v1 = 2;
            v8 = 2;
            g_103a3a48 = 2;
        }
        else
        {
            v8 = g_103a3a48;
        }
    }
    if (!(v8 != 2 && v8))
    {
        v17 = 0;
        if (!a7)
            a7 = *(a0)->field_14;
        if (!a6)
            a6 = *(a0)->field_4;
        v18 = sub_1035fd30(a7);
        if (v18 != 4294967295)
        {
            if (v18 != a6)
            {
                v17 = sub_1035fd77(a6, v18, a3, &/* unsupported instruction */, 0, 0);
                if (v17)
                {
                    a3 = v17;
                    goto LABEL_1035fbb4;
                }
            }
            else
            {
LABEL_1035fbb4:
                g_1038b1ac(a7, a2, a3, a4, a5);
                if (v17)
                {
                    v0 = v17;
                    sub_1035345e();
                }
            }
        }
    }
    else if (v8 == 1)
    {
LABEL_1035faa5:
        v5 = 0;
        if (!a6)
            a6 = *(a0)->field_4;
        v0 = a6;
        v13 = g_1038b104(a6, (a8) * 8 + 1, a3, a4, 0, 0);
        if (v13)
        {
            if (v13 > 0 && v13 <= 2147483632)
            {
                v14 = v13 * 2 + 8;
                if (v14 <= 0x400)
                {
                    sub_1035de90();
                    iter = &v0;
                    if (!&v0)
                        goto LABEL_1035fb1e;
                    v0 = 0xcccc;
                    goto LABEL_1035fb1b;
                }
                else
                {
                    iter = sub_10355a15(v14);
                    if (iter)
                    {
                        *(iter) = 0xdddd;
LABEL_1035fb1b:
                        iter += 2;
                    }
                }
LABEL_1035fb1e:
                v11 = iter;
            }
            if (v11)
            {
                sub_10350ad0(v11, 0, v13 * 2);
                v16 = g_1038b104(a6, 1, a3, a4, v11, v13);
                if (v16)
                    v5 = g_1038b1a8(a2, v11, v16, a5);
                sub_103548d8(v11);
            }
        }
    }
    return sub_10351225();
}
```

## `sub_1035fbea` `0x1035fbea`

_64 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

int sub_1035fbea(unsigned int *a0, unsigned int a1, int a2, unsigned int a3, unsigned int a4, unsigned int a5, int a6, unsigned int a7)
{
    unsigned int v3;  // edx
    int v4;  // eax
    struct_0 v0;  // [bp-0x14]
    struct_0 *idx;  // [bp-0xc]
    char v2;  // [bp-0x8]

    sub_103536a7(&v0, a0);
    v4 = sub_1035fa32(&v0, v3, a1, a2, a3, a4, a5, a6, a7);
    if (v2)
        idx[8].field_8 = idx[8].field_8 & 4294967293;
    return v4;
}
```

## `sub_1035fc2a` `0x1035fc2a`

_190 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[3];
    char field_3;
} struct_0;

unsigned int sub_1035fc2a(struct_0 *node, void* iter, unsigned int a1)
{
    unsigned int v2;  // ecx
    unsigned int v3;  // edi
    unsigned int v4;  // edi
    struct_0 *v5;  // eax
    unsigned int v9;  // eax
    unsigned int v0;  // [bp-0x10]
    unsigned int iter1;  // [bp-0x8]

    iter1 = v2;
    iter1 = 0;
    if (!a1)
        return 0;
    v0 = v3;
    if (a1 >= 4 && !((v4 = a1 - 4, !v4)))
    {
        do
        {
            v5 = node;
            node = v5 + 1;
            iter += 4;
            if (!v5->padding_0[0] || v5->padding_0[0] != (char)iter[4])
            {
                return v9;
            }
            if (!node->field_3 || node->field_3 != (char)iter[3])
            {
                return v9;
            }
            if (!node->padding_0[2] || node->padding_0[2] != (char)iter[2])
            {
                return v9;
            }
            if (!node->padding_0[1] || node->padding_0[1] != (char)iter[1])
            {
                return v9;
            }
            iter1 += 4;
        } while (iter1 < v4);
    }
    while (true)
    {
        if (iter1 >= a1)
            return 0;
        if (!node->padding_0[0] || node->padding_0[0] != *((char *)iter))
            break;
        node = &node->padding_0[1];
        iter += 1;
        iter1 += 1;
    }
    return v9;
}
```

## `sub_1035fcf0` `0x1035fcf0`

_64 bytes. (leaf/helper — see body)_

```c
char * sub_1035fcf0(char *a0, char *a1)
{
    char *v8;  // eax
    char *v9;  // edx
    char *v10;  // esi
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x1c]
    unsigned int v4;  // [bp-0x18]
    unsigned int v5;  // [bp-0x14]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]

    v8 = NULL;
    v7 = 0;
    v6 = 0;
    v5 = 0;
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    v9 = a1;
    while (true)
    {
        v8 = _INSERT(v8, 0, *(v9));
        if (!*(v9))
            break;
        v9 += 1;
        *((char *)&v0 + (v8 >> 3)) = *((char *)&v0 + (v8 >> 3)) | 1 << ((char)v8 & 7);
    }
    while (true)
    {
        v10 = a0;
        v8 = _INSERT(v8, 0, *(v10));
        if (!*(v10))
            return v8;
        a0 = v10 + 1;
        if ((*((char *)&v0 + (v8 >> 3)) >> ((char)v8 & 7) & 1) == 1)
            return v10;
    }
}
```

## `sub_1035fd30` `0x1035fd30`

_71 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1e4;
extern unsigned int g_1038e180;

int sub_1035fd30(unsigned int a0)
{
    char v0;  // [bp-0x10]
    char v1;  // [bp-0xa]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]

    v2 = g_1038e180 ^ &v3;
    v1 = 0;
    if (g_1038b1e4(a0, 4100, &v0, 6))
        sub_10363c11(&v0);
    return sub_10351225();
}
```

## `sub_1035fd77` `0x1035fd77`

_434 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b040;
extern struct_0 *g_1038b104;
extern struct_0 *g_1038b230;
extern unsigned int g_1038e180;

int sub_1035fd77(unsigned int a0, unsigned int a1, void* a2, int *a3, unsigned int a4, unsigned int a5)
{
    unsigned int v12;  // ebx
    unsigned int v13;  // esi
    unsigned int v14;  // edi
    int v15;  // esi
    unsigned int v16;  // eax
    unsigned int *iter;  // eax
    int v18;  // eax
    unsigned int v0;  // [bp-0xc8]
    unsigned int v1;  // [bp-0x6c]
    unsigned int v2;  // [bp-0x44]
    unsigned int v3;  // [bp-0x40]
    unsigned int v4;  // [bp-0x3c]
    unsigned int v5;  // [bp-0x30]
    int v6;  // [bp-0x28]
    unsigned int v7;  // [bp-0x24]
    unsigned int *v8;  // [bp-0x20]
    char v9;  // [bp-0x1c], Other Possible Types: unsigned int
    unsigned int v10;  // [bp-0x8]
    char v11;  // [bp-0x4]

    v10 = g_1038e180 ^ &v11;
    v4 = v12;
    v3 = v13;
    v6 = *(a3);
    v2 = v14;
    v7 = 0;
    v5 = 0;
    if (a0 == a1)
        return sub_10351225();
    if (g_1038b230(a0, &v9) && v9 == 1 && g_1038b230(a1, &v9))
    {
        v15 = v6;
        v5 = 1;
        if (v15 == -1)
            v15 = sub_10352f20(a2) + 1;
LABEL_1035fe5f:
        v8 = NULL;
    }
    else
    {
        v15 = g_1038b104(a0, 1, a2, v6, 0, 0);
        if (!v15)
            return sub_10351225();
        v1 = a0;
        if (v15 <= 0 || (v1 = v1, v15 > 2147483632))
            goto LABEL_1035fe5f;
        v16 = v15 * 2 + 8;
        if (v16 <= 0x400)
        {
            sub_1035de90();
            iter = &v1;
            if (!&v1)
                goto LABEL_1035fe5a;
            v1 = 0xcccc;
            goto LABEL_1035fe57;
        }
        else
        {
            iter = sub_10355a15(v16);
            if (iter)
            {
                *(iter) = 0xdddd;
LABEL_1035fe57:
                iter += 2;
            }
        }
LABEL_1035fe5a:
        v8 = iter;
    }
    if (!v8)
        return sub_10351225();
    sub_10350ad0(v8, 0, v15 * 2);
    if (g_1038b104(a0, 1, a2, v6, v8, v15))
    {
        if (a4)
        {
            if (g_1038b040(a1, 0, v8, v15, a4, a5, 0, 0))
                v7 = a4;
        }
        else
        {
            if (v5 || (v15 = (int)g_1038b040(a1, 0, v8, v15, 0, 0, 0, 0), v15))
            {
                v7 = sub_103574c2(1, v15);
                if (v7)
                {
                    v18 = g_1038b040(a1, 0, v8, v15, v7, v15, 0, 0);
                    if (!v18)
                    {
                        v0 = v7;
                        sub_1035345e();
                        v7 = 0;
                    }
                    else if (v6 != -1)
                    {
                        *(a3) = v18;
                    }
                }
            }
        }
    }
    sub_103548d8(v8);
    return sub_10351225();
}
```

## `sub_1035ff29` `0x1035ff29`

_272 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b220;
extern unsigned int g_103a13c0;
extern unsigned int g_103a36c8;
extern unsigned int g_103a3a44;
extern char g_103a4cb0;
extern char g_103a4cc0;

void sub_1035ff29(unsigned int a0)
{
    unsigned int v10;  // ecx
    unsigned int v11;  // eax
    unsigned int v12;  // 4107
    unsigned int v13;  // 4153
    unsigned int v14;  // 4154
    unsigned int v15;  // ecx
    unsigned int v16;  // esi
    void* v17;  // ebx
    unsigned int v18;  // edx
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    void* v5;  // [bp+0xfffe8], Other Possible Types: unsigned int
    unsigned int v6;  // [bp+0x100000]
    unsigned int v7;  // [bp+0x10000c]
    unsigned int v8;  // [bp+0x100010]
    unsigned int *v9;  // [bp+0x100014]

    sub_1035b0cc(&g_103a13c0, 12);
    v10 = v7;
    if (v10 > 0)
    {
        v4 = 0xffffffe0;
        v11 = 0xffffffe0 / v10;
        v12 = v8;
        v13 = _ccall(12, 0, (unsigned int)(char)(v11 < v12), (unsigned int)(char)(v11 < v12));
        v14 = _ccall(4, 18, -((unsigned int)(char)(v11 < v12)) + 1, 0, v13);
        if (!((char)v14))
            goto LABEL_1035ff6c;
        *((unsigned int *)sub_103575e0()) = 12;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        sub_103535f2();
    }
    else
    {
LABEL_1035ff6c:
        v15 = v8 * v10;
        v16 = v15;
        v7 = v16;
        if (!v16)
            v16 = 1;
        do
        {
            v17 = NULL;
            v5 = 0;
            if (v16 > 0xffffffe0)
                continue;
            if (*((int *)&g_103a4cc0) == 3 && !((v16 = v16 + 15 & 0xfffffff0, v8 = v16, v7 > *((int *)&g_103a4cb0))))
            {
                sub_1035a599(v15, v18, 4);
                v6 = 0;
                v5 = sub_1035ade6(v7);
                v6 = 4294967294;
                sub_10360025();
                v17 = v5;
                if (!v17)
                    goto LABEL_1035ffde;
                sub_10350ad0(v17, 0, v7);
            }
            if (v17)
            {
                sub_1035b111(v2, v3, v4, &g_103a13c0);
                return;
            }
LABEL_1035ffde:
            v17 = g_1038b220(g_103a36c8, 8, v16);
            if (v17)
            {
                sub_1035b111(v2, v3, v4, &g_103a13c0);
                return;
            }
            if (!g_103a3a44)
            {
                if (!v17 && v9)
                    *(v9) = 12;
                sub_1035b111(v2, v3, v4, &g_103a13c0);
                return;
            }
            v15 = v16;
        } while (sub_103540ea(v16));
        if (v9)
            *(v9) = 12;
    }
    sub_1035b111(v2, v3, v4, &g_103a13c0);
    return;
}
```

## `sub_10360020` `0x10360020`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10360020(void)
{
    sub_10360025();
    return;
}
```

## `sub_10360025` `0x10360025`

_9 bytes. (leaf/helper — see body)_

```c
int sub_10360025(void)
{
    return sub_1035a4c1(4);
}
```

## `sub_10360047` `0x10360047`

_524 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
} struct_0;

extern struct_0 *g_1038b07c;
extern struct_0 *g_1038b220;
extern struct_0 *g_1038b258;
extern unsigned int g_103a13e0;
extern unsigned int g_103a36c8;
extern unsigned int g_103a3a44;
extern char g_103a4cb0;
extern unsigned int g_103a4cc0;

void sub_10360047(unsigned int a0)
{
    void* v9;  // ebx
    void* v10;  // esi
    void* v18;  // eax
    void* v19;  // edi
    unsigned int *v20[4];  // eax
    unsigned int *v21[4];  // eax
    unsigned int v22;  // eax
    unsigned int v11;  // ecx
    unsigned int v12;  // edx
    struct_0 *v13;  // eax
    void* v14;  // eax
    void* v15;  // eax
    struct_0 *v16;  // eax
    void* v17;  // eax
    unsigned int v0;  // [bp-0x24]
    void* v1;  // [bp-0x20]
    void* v2;  // [bp-0x18]
    void* v3;  // [bp-0xc]
    struct_0 *v4;  // [bp+0xfffe4]
    void* v5;  // [bp+0xfffe8]
    unsigned int v6;  // [bp+0x100000]
    void* v7;  // [bp+0x10000c]
    void* v8;  // [bp+0x100010], Other Possible Types: unsigned int

    sub_1035b0cc(&g_103a13e0, 16);
    v9 = v7;
    if (!v9)
    {
        sub_10355a15(v8);
        sub_1035b111(v0, v1, v10, v2);
        return;
    }
    v10 = v8;
    if (!v10)
    {
        v3 = v9;
        sub_1035345e();
        sub_1035b111(v0, v1, v10, v2);
        return;
    }
    v1 = v1;
    if (g_103a4cc0 == 3)
    {
        do
        {
            v5 = NULL;
            if (v10 > 0xffffffe0)
                goto LABEL_10360220;
            sub_1035a599(v11, v12, 4);
            v6 = 0;
            v13 = sub_1035a612(v9);
            v4 = v13;
            if (v13)
            {
                if (v10 <= *((int *)&g_103a4cb0))
                {
                    if (sub_1035ab07(v13, v9, v10))
                    {
                        v5 = v9;
                    }
                    else
                    {
                        v14 = sub_1035ade6(v10);
                        v5 = v14;
                        if (v14)
                        {
                            v15 = (int)v9[4] - 1;
                            if (v15 >= v10)
                                v15 = v10;
                            sub_10350b50(v5, v9, v15);
                            v16 = sub_1035a612(v9);
                            v4 = v16;
                            sub_1035a63d(v16, v9);
                        }
                    }
                }
                if (!v5)
                {
                    if (!v10)
                    {
                        v10 = 0x1;
                        v8 = 1;
                    }
                    v10 = v10 + 15 & 0xfffffff0;
                    v8 = v10;
                    v17 = g_1038b220(g_103a36c8, 0, v10);
                    v5 = v17;
                    if (v17)
                    {
                        v18 = (int)v9[4] - 1;
                        if (v18 >= v10)
                            v18 = v10;
                        sub_10350b50(v5, v9, v18);
                        sub_1035a63d(v4, v9);
                    }
                }
            }
            v6 = 4294967294;
            sub_1036018b();
            if (!v4)
            {
                if (!v10)
                    v10 = 0x1;
                v10 = v10 + 15 & 0xfffffff0;
                v8 = v10;
                v1 = NULL;
                v0 = g_103a36c8;
                v19 = g_1038b258(g_103a36c8, 0, v9, v10);
                v10 = v9;
                v2 = v10;
            }
            else
            {
                v19 = v5;
            }
            if (v19)
            {
                sub_1035b111(v0, v1, v10, v2);
                return;
            }
            if (!g_103a3a44)
            {
                v1 = v1;
                if (true)
                {
                    v21 = sub_103575e0();
                    v1 = v1;
                    if (v4)
                    {
                        *(v21) = 0xc;
                        sub_1035b111(v0, v1, v10, v2);
                        return;
                    }
                    goto LABEL_1036024d;
                }
                else
                {
                    sub_1035b111(v0, v1, v10, v2);
                    return;
                }
            }
        } while (sub_103540ea(v10));
        v20 = sub_103575e0();
        v1 = v1;
        if (v4)
        {
            *(v20) = 0xc;
            sub_1035b111(v0, v1, v10, v2);
            return;
        }
    }
    else
    {
        do
        {
            if (v10 > 0xffffffe0)
            {
LABEL_10360220:
                sub_103540ea(v10);
                v20 = sub_103575e0();
                *(v20) = 0xc;
                sub_1035b111(v0, v1, v10, v2);
                return;
            }
            if (!v10)
                v10 = 0x1;
            v0 = 0;
            v22 = g_1038b258(g_103a36c8, 0, v9, v10);
            v1 = v9;
            if (v22)
            {
                v10 = v10;
                sub_1035b111(v0, v1, v10, v2);
                return;
            }
            if (g_103a3a44 == v22)
            {
                v1 = v9;
                if (true)
                {
                    v21 = sub_103575e0();
                    v1 = v9;
                }
                else
                {
                    v10 = v10;
                    sub_1035b111(v0, v1, v10, v2);
                    return;
                }
LABEL_1036024d:
                *(v21) = sub_103575a5(g_1038b07c());
                sub_1035b111(v0, v1, v10, v2);
                return;
            }
        } while ((v1 = v9, v10 = v10, sub_103540ea(v10)));
        v20 = sub_103575e0();
        v1 = v9;
    }
    *(v20) = sub_103575a5(g_1038b07c());
    sub_1035b111(v0, v1, v10, v2);
    return;
}
```

## `sub_10360185` `0x10360185`

_6 bytes. (leaf/helper — see body)_

```c
void sub_10360185(void)
{
    sub_1036018b();
    return;
}
```

## `sub_1036018b` `0x1036018b`

_9 bytes. (leaf/helper — see body)_

```c
int sub_1036018b(void)
{
    return sub_1035a4c1(4);
}
```

## `sub_10360262` `0x10360262`

_121 bytes. (leaf/helper — see body)_

```c
int sub_10360262(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v5;  // ebx
    unsigned int v6;  // esi
    unsigned int v7;  // edi
    unsigned int v8;  // esi
    unsigned int v9;  // edi
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]

    v5 = 0;
    if (a1 > 0)
    {
        v4 = 0xffffffe0;
        if (v4 / a1 < a2)
        {
            v4 = 0;
            v3 = 0;
            v2 = 0;
            v1 = 0;
            v0 = 0;
            *((unsigned int *)sub_103575e0()) = 12;
            sub_103535f2();
            return 0;
        }
    }
    v4 = v6;
    v3 = v7;
    v8 = a2 * a1;
    if (a0)
        v5 = (unsigned int)sub_1035c490(a0);
    v2 = a2 * a1;
    v9 = (unsigned int)sub_10360047(a0);
    if (v9 && v5 < v8)
        sub_10350ad0(v5 + v9, 0, v8 - v5);
    return v9;
}
```

## `sub_103602e0` `0x103602e0`

_165 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_103602e0(unsigned int *idx, int a1, unsigned int a2, unsigned int a3, unsigned int a4, int a5)
{
    unsigned int v7;  // ebx
    int v8;  // edi
    int v9;  // esi
    int v10;  // ebx
    unsigned int v11;  // eax
    char v0;  // [bp-0x28], Other Possible Types: unsigned int
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    char v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]

    v5 = g_1038e180 ^ &v6;
    v7 = 0;
    v3 = sub_10364959(&v4, &v0, a1, 0, 0, 0, 0, a5, v8, v9, v10);
    if (((char)v3 & 4))
    {
        v7 = 0x200;
        v1 = 0;
        v2 = 0;
    }
    else
    {
        v11 = sub_10363ed5(&v4, &v1);
        if (((char)v3 & 2) || v11 == 1)
            v7 = 128;
        if (((char)v3 & 1) || v11 == 2)
            v7 |= 0x100;
    }
    idx[1] = v0 - a1;
    idx[4] = v1;
    idx[5] = v2;
    *(idx) = v7;
    return sub_10351225();
}
```

## `sub_10360385` `0x10360385`

_13 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10360385(unsigned int a0)
{
    unsigned int v0;  // eax

    v0 = 1;
    if (!a0)
        v0 = 0;
    return v0;
}
```

## `sub_10360392` `0x10360392`

_45 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a1400;

void sub_10360392(unsigned int a0)
{
    unsigned int v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0xfffe8]
    unsigned int v2;  // [bp+0x100000]

    sub_1035b0cc(&g_103a1400, 12);
    v2 = 0;
    v1 = 1;
    v2 = 4294967294;
    sub_1035b111(&g_103a1400, 12, v0, a0);
    return;
}
```

## `sub_103603af` `0x103603af`

_28 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

unsigned int sub_103603af(void)
{
    struct_0 **v1;  // [bp+0xffff0]

    if (*(v1)->field_0 == 3221225477)
    {
        return 1;
    }
    else if (*(v1)->field_0 != 3221225501)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `sub_103603cb` `0x103603cb`

_7 bytes. (leaf/helper — see body)_

```c
void sub_103603cb(void)
{
    unsigned int v1;  // [bp+0xfffe8]

    v1 = 0;
}
```

## `sub_103603e2` `0x103603e2`

_96 bytes. (leaf/helper — see body)_

```c
unsigned int sub_103603e2(void)
{
    unsigned int v9;  // ebx
    unsigned int v10;  // 4217
    unsigned int v11;  // id
    unsigned int v12;  // ac
    unsigned int v13;  // ecx
    unsigned int v14;  // 4123
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]

    v7 = 0;
    v5 = 0;
    v6 = 0;
    v1 = v9;
    v10 = _ccall(15, 0, 0, 0);
    v0 = v10 | 0x202 | v11 * 0x200000 & 0x200000 | v12 * 0x40000 & 0x40000;
    v13 = v0;
    v0 ^= 0x200000;
    v14 = v0;
    v0 = v14 & 2261 | 0x202 | ((char)(v14 >> 10) ? 4294967295 : 1) & 0x400 | ((char)(v14 >> 21) ? 1 : 0) * 0x200000 & 0x200000 | ((char)(v14 >> 18) ? 1 : 0) * 0x40000 & 0x40000;
    if (v0 != v13)
    {
        v0 = v13;
        x86g_dirtyhelper_CPUID_sse3(unsupported_<class 'pyvex.expr.GSPTR'>())
        /* unsupported instruction */
        v5 = 0;
        v2 = v9;
        v3 = v0 - v13;
        v4 = v13;
        x86g_dirtyhelper_CPUID_sse3(unsupported_<class 'pyvex.expr.GSPTR'>())
        /* unsupported instruction */
        v7 = v3;
        v6 = 1;
    }
    if ((v7 & 0x4000000) && (unsigned int)sub_10360392(v9))
        return 1;
    return 0;
}
```

## `sub_10360442` `0x10360442`

_13 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a4cc8;

unsigned int sub_10360442(void)
{
    g_103a4cc8 = sub_103603e2();
    return 0;
}
```

## `sub_10360450` `0x10360450`

_32 bytes. (leaf/helper — see body)_

```c
void sub_10360450(int a0)
{
    int v3;  // edi
    int v4;  // esi
    int v5;  // ebx
    int v0;  // [bp-0x20]
    char v1;  // [bp-0x4]
    char v2;  // [bp+0x0]

    sub_10369d26(a0, v0, 0, 0, &v1, v3, v4, v5, &v2);
    return;
}
```

## `sub_10360470` `0x10360470`

_33 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_10360470(struct_0 *a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4)
{
    if (!((char)a0->field_4 & 6))
        return 1;
    sub_10351225();
}
```

## `sub_10360490` `0x10360490`

_36 bytes. (leaf/helper — see body)_

```c
int sub_10360490(void)
{
    int v4[11];  // eax
    int v0;  // [bp-0x4]
    unsigned int v2;  // [bp+0x8]
    unsigned int *v3;  // [bp+0x10]

    sub_103604b5(v4[9], v4[10], v0);
    *(v3) = v2;
}
```

## `sub_103604b5` `0x103604b5`

_132 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int [4] sub_103604b5(unsigned int a0, unsigned int a1)
{
    unsigned int v9;  // ebx
    unsigned int v10;  // esi
    unsigned int v19;  // esi
    unsigned int index;  // esi
    unsigned long v21;  // 4118
    unsigned int v11;  // edi
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    unsigned short v14;  // fs
    unsigned long v15;  // 4149
    unsigned long v16;  // 4162
    unsigned int idx[4];  // eax
    unsigned int v18;  // ebx
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    unsigned int v7;  // [bp-0x4]
    unsigned int v8[4];  // [bp+0x0]

    v7 = v9;
    v6 = v10;
    v5 = v11;
    v4 = a0;
    v3 = 4294967294;
    v2 = sub_10360470;
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    v1 = *((int *)v15);
    v0 = g_1038e180 ^ &v1;
    v16 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v16) = &v1;
    while (true)
    {
        idx = v8;
        v18 = idx[2];
        v19 = idx[3];
        if (v19 == 4294967295 || a0 != 4294967295 && v19 <= a0)
            break;
        index = v19 * 3;
        v2 = *((int *)(v18 + index * 4));
        idx[3] = *((int *)(v18 + index * 4));
        if (!*((int *)(v18 + index * 4 + 4)))
        {
            sub_10360565(0x101);
            sub_10360584(0x101);
        }
    }
    v21 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int *)v21) = v0;
    return idx;
}
```

## `sub_10360539` `0x10360539`

_35 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[4];
    unsigned int field_4;
    char padding_8[4];
    struct struct_0 *field_c;
} struct_1;

typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
} struct_0;

unsigned int sub_10360539(void)
{
    unsigned int v1;  // eax
    unsigned long v2;  // ldt
    unsigned long v3;  // gdt
    unsigned short v4;  // fs
    unsigned long v5;  // 4125
    struct_1 *v6;  // ecx

    v1 = 0;
    v5 = _ccall(v2, v3, (unsigned int)v4, 0);
    v6 = *((int *)v5);
    if (v6->field_4 == sub_10360470 && v6->padding_8 == v6->field_c->field_c)
        v1 = 1;
    return v1;
}
```

## `sub_1036055c` `0x1036055c`

_29 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038f12c;
extern unsigned int g_1038f130;
extern char g_1038f134;

int sub_1036055c(void)
{
    unsigned int v2;  // ecx
    unsigned int v3;  // eax
    unsigned int v0;  // [bp-0x8]

    v0 = v2;
    g_1038f130 = v2;
    g_1038f12c = v3;
    *((int *)&g_1038f134) = /* unsupported instruction */;
    return;
}
```

## `sub_10360565` `0x10360565`

_11 bytes. (leaf/helper — see body)_

```c
void sub_10360565(unsigned int a0)
{
    unsigned int v2;  // ebx
    unsigned int v3;  // ecx
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp-0x4]

    v1 = v2;
    v0 = v3;
}
```

## `sub_10360584` `0x10360584`

_3 bytes. (leaf/helper — see body)_

```c
int sub_10360584(void)
{
    unsigned int *v1;  // eax

    v1();
    return;
}
```

## `sub_10360587` `0x10360587`

_131 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    char padding_0[4];
    char field_4;
} struct_2;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b07c;
extern struct_0 *g_1038b1a4;
extern unsigned int g_103a3b80[4];

unsigned int sub_10360587(unsigned int a0, unsigned int a1, int a2, int a3, unsigned int a4, unsigned int a5)
{
    int v3;  // edi
    int v4;  // esi
    unsigned int v5;  // eax
    unsigned int *v6;  // eax
    struct_2 *v7;  // eax
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]
    char v2;  // [bp+0x0]

    v1 = a0;
    v0 = a0;
    v1 = a4;
    v5 = sub_10365117(a2, v3, v4, a3, a4, &v2);
    if (v5 == 4294967295)
    {
        *((unsigned int *)sub_103575e0()) = 9;
    }
    else
    {
        v0 = g_1038b1a4(v5, a3, &v1, a5);
        if (g_1038b1a4(v5, a3, &v1, a5) != 4294967295 || !((v6 = (unsigned int *)g_1038b07c(), v6)))
        {
            v7 = g_103a3b80[a2 >> 5] + (a2 & 31) * 56 + 4;
            v7->padding_0[0] = v7->padding_0[0] & 253;
            return g_1038b1a4(v5, a3, &v1, a5);
        }
        sub_10357606(v6);
    }
    return 4294967295;
}
```

## `sub_1036060a` `0x1036060a`

_271 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a1420;
extern char g_103a3b70;
extern unsigned int g_103a3b80[4];

void sub_1036060a(unsigned int a0)
{
    unsigned int v13;  // eax
    unsigned int *v14;  // ebx
    unsigned int v15;  // esi
    unsigned int v16;  // edx
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp+0x0]
    unsigned int v6;  // [bp+0xfffe0]
    unsigned int v7;  // [bp+0xfffe4]
    unsigned int v8;  // [bp+0x100000]
    unsigned int v9;  // [bp+0x10000c]
    int v10;  // [bp+0x100010]
    unsigned int v11;  // [bp+0x100014]
    unsigned int v12;  // [bp+0x100018]

    sub_1035b0cc(&g_103a1420, 20);
    v6 = 4294967295;
    v7 = 4294967295;
    v13 = v9;
    if (v13 == 4294967294)
    {
        *((unsigned int *)sub_103575f3()) = 0;
        *((unsigned int *)sub_103575e0()) = 9;
    }
    else
    {
        if (v13 >= 0 && v13 < *((int *)&g_103a3b70))
        {
            v14 = &g_103a3b80[v13 >> 5];
            v15 = (v13 & 31) * 56;
            if (!(*((char *)(*(v14) + v15 + 4)) & 1))
            {
                *((unsigned int *)sub_103575f3()) = 0;
                *((unsigned int *)sub_103575e0()) = 9;
                v4 = 0;
                v3 = 0;
                v2 = 0;
                v1 = 0;
                v0 = 0;
                sub_103535f2();
                sub_1035b111(&g_103a1420, 20, v5, a0);
                return;
            }
            sub_10365188(v13);
            v8 = 0;
            if ((*((char *)(*(v14) + v15 + 4)) & 1))
            {
                v6 = sub_10360587(v13, v16, v9, v10, v11, v12);
                v7 = v16;
            }
            else
            {
                *((unsigned int *)sub_103575e0()) = 9;
                *((unsigned int *)sub_103575f3()) = 0;
                v6 = 4294967295;
                v7 = 4294967295;
            }
            v8 = 4294967294;
            sub_10360719();
            sub_1035b111(&g_103a1420, 20, v5, a0);
            return;
        }
        *((unsigned int *)sub_103575f3()) = 0;
        *((unsigned int *)sub_103575e0()) = 9;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        sub_103535f2();
    }
    sub_1035b111(&g_103a1420, 20, v5, a0);
    return;
}
```

## `sub_10360719` `0x10360719`

_10 bytes. (leaf/helper — see body)_

```c
void sub_10360719(void)
{
    int v1;  // [bp+0x10000c]

    sub_10365228(v1);
    return;
}
```

## `sub_10360723` `0x10360723`

_1478 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[108];
    struct struct_0 *field_6c;
} struct_1;

typedef struct struct_6 {
    unsigned int field_0;
    char field_4;
} struct_6;

typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

extern struct_2 *g_1038b040;
extern struct_2 *g_1038b07c;
extern struct_2 *g_1038b19c;
extern struct_2 *g_1038b1a0;
extern struct_2 *g_1038b244;
extern unsigned int g_1038e180;
extern unsigned int g_103a3b80[4];

int sub_10360723(unsigned int a0, unsigned int a1, int a2, void* a3, void* a4)
{
    unsigned int v26;  // esi
    unsigned int v27;  // ebx
    unsigned int v34;  // esi
    struct_6 *v35;  // eax
    void* v36;  // eax
    unsigned int v37;  // esi
    void* v38;  // ecx
    char *iter;  // eax
    char v40;  // dl
    void* v41;  // esi
    void* v42;  // eax
    unsigned int v28;  // ebx
    unsigned int *v43;  // edi
    unsigned int iter1;  // esi
    void* v45;  // ecx
    unsigned short *iter2;  // eax
    unsigned short v47;  // dx
    void* v48;  // esi
    void* v49;  // eax
    void* v50;  // ecx
    unsigned short *v51;  // eax
    unsigned int *v29;  // edi
    unsigned short v52;  // dx
    int v53;  // esi
    int v54;  // edi
    void* node;  // esi
    char v30[37];  // eax
    char v31;  // 4161
    void* v32;  // ecx
    struct_1 *v33;  // eax
    unsigned int v0;  // [bp-0x5f8]
    unsigned int v1;  // [bp-0x5d0]
    unsigned int v2;  // [bp-0x5b8]
    unsigned int v3;  // [bp-0x5b4]
    unsigned int v4;  // [bp-0x5b0]
    unsigned int v5;  // [bp-0x5ac]
    unsigned int v6;  // [bp-0x5a8]
    unsigned int *v7;  // [bp-0x5a4], Other Possible Types: unsigned int
    unsigned int v8;  // [bp-0x5a0]
    unsigned int v9;  // [bp-0x59c]
    char v10;  // [bp-0x598], Other Possible Types: unsigned int
    unsigned int v11;  // [bp-0x594]
    unsigned int *v12;  // [bp-0x58c]
    void* v13;  // [bp-0x588], Other Possible Types: char
    unsigned int v14;  // [bp-0x584]
    void* v15;  // [bp-0x57c]
    void* i;  // [bp-0x578], Other Possible Types: unsigned int
    char v17;  // [bp-0x571]
    unsigned int v18;  // [bp-0x570]
    void* k;  // [bp-0x56c], Other Possible Types: unsigned int
    char v20;  // [bp-0x568]
    char v21;  // [bp-0x51c]
    char v22;  // [bp-0x414]
    unsigned short v23;  // [bp-0x164]
    char v24;  // [bp-0x10]
    unsigned int v25;  // [bp-0x8]

    v25 = g_1038e180 ^ &v21;
    v9 = v26;
    v15 = NULL;
    v14 = 0;
    if (!a4)
        return sub_10351225();
    if (!a3)
    {
        *((unsigned int *)sub_103575f3()) = 0;
        v8 = 0;
        v7 = 0;
        v6 = 0;
        v5 = 0;
        v4 = 0;
        *((unsigned int *)sub_103575e0()) = 22;
        sub_103535f2();
    }
    else
    {
        v8 = v27;
        v28 = (a2 & 31) * 56;
        v7 = v29;
        v43 = &g_103a3b80[a2 >> 5];
        v30 = *(v43) + v28;
        v31 = v30[36];
        v32 = _INSERT(a0, 0, v31 & 127);
        v12 = v43;
        v17 = v31 & 127;
        if (((v31 & 127) == 2 || *((char *)&v32) == 1) && (v32 = ~(a4), !(*((char *)(void*)&v32) & 1)))
        {
            *((unsigned int *)sub_103575f3()) = 0;
            v6 = 0;
            v5 = 0;
            v4 = 0;
            v3 = 0;
            v2 = 0;
            *((unsigned int *)sub_103575e0()) = 22;
            sub_103535f2();
            goto LABEL_10360cc9;
        }
        if ((v30[4] & 32))
            sub_10360587(v32, a1, a2, 0, 0, 2);
        if (sub_10360e09(a2) && (*((char *)(v28 + *(v43) + 4)) & 128) && (v33 = (struct_1 *)sub_10358da8(), g_1038b19c(*((int *)(v28 + *(v43))), &v10) && (*((int *)((sub_10358da8())[13 + 1] + 20)) || v17)))
        {
            k = 0;
            node = a3;
            v10 = g_1038b1a0();
            if (a4 <= NULL)
                goto LABEL_10360c7b;
            i = NULL;
            while (true)
            {
                if (!v17)
                {
                    v11 = *((char *)node) == 10;
                    if (sub_1035de7e(*((char *)node)))
                    {
                        if (a3 - node + a4 <= 1 || sub_103655be(&v18, node, 2) == 4294967295)
                            goto LABEL_10360c71;
                        node += 1;
                        i += 1;
                    }
                    else if (sub_103655be(&v18, node, 1) == 4294967295)
                    {
                        goto LABEL_10360c71;
                    }
                    i += 1;
                    node += 1;
                    v34 = g_1038b040(v10, 0, &v18, 1, &v24, 5, 0, 0);
                    if (!v34)
                        goto LABEL_10360c71;
                    if (!g_1038b244(*((int *)(v28 + *(v43))), &v24, v34, &k, 0))
                        goto LABEL_10360c68;
                    v15 += k;
                    if (k < v34)
                        goto LABEL_10360c71;
                    v24 = v24;
                    if (v11)
                    {
                        v24 = 13;
                        if (!g_1038b244(*((int *)(v28 + *(v43))), &v24, 1, &k, 0))
                            goto LABEL_10360c68;
                        if (k < 1)
                            goto LABEL_10360c71;
                        v14 += 1;
                        v15 += 1;
                    }
                }
                else
                {
                    if (v17 == 1 || v17 == 2)
                    {
                        i += 2;
                        v18 = *((short *)node);
                        node += 2;
                        v11 = (unsigned short)v18 == 10;
                    }
                    if (v17 == 1 || !((v24 = v24, v17 != 2)))
                    {
                        if ((unsigned short)sub_103653e9(v18) != (unsigned short)v18)
                            goto LABEL_10360c68;
                        v15 += 1;
                        if (v11)
                        {
                            v0 = 13;
                            v18 = 13;
                            if ((unsigned short)sub_103653e9(v18) != (unsigned short)v18)
                                goto LABEL_10360c68;
                            v15 += 1;
                            v14 += 1;
                        }
                    }
                }
                if (i >= a4)
                    goto LABEL_10360c71;
                node = node;
            }
            goto LABEL_10360c68;
        }
        else
        {
            v35 = *(v43) + v28;
            if ((v35->field_4 & 128))
            {
                v36 = a3;
                v37 = 0;
                v18 = 0;
                if (!v17)
                {
                    k = v36;
                    if (a4 <= NULL)
                        goto LABEL_10360ca2;
                    do
                    {
                        i = 0;
                        v38 = k - a3;
                        iter = &v20;
                        do
                        {
                            if (v38 >= a4)
                                break;
                            k += 1;
                            v40 = *((char *)k);
                            v38 += 1;
                            if (*((char *)k) == 10)
                            {
                                v14 += 1;
                                *(iter) = 13;
                                iter += 1;
                                i += 1;
                            }
                            *(iter) = v40;
                            iter += 1;
                            i += 1;
                        } while (i < 0x400);
                        v41 = iter - &v20;
                        if (!g_1038b244(*((int *)(v28 + *(v43))), &v20, v41, &v13, 0))
                            goto LABEL_10360c68;
                    } while ((v42 = v13, v15 = (void*)(v15 + v42), v42 >= v41 && k - a3 < a4));
                }
                else
                {
                    if (v17 == 2)
                    {
                        k = v36;
                        if (a4 <= NULL)
                            goto LABEL_10360ca2;
                        do
                        {
                            iter1 = 0;
                            v45 = k - a3;
                            iter2 = &v20;
                            do
                            {
                                if (v45 >= a4)
                                    break;
                                k += 2;
                                v47 = *((short *)k);
                                v45 += 2;
                                if (v47 == 10)
                                {
                                    v14 += 2;
                                    *(iter2) = 13;
                                    iter2 += 1;
                                    iter1 += 2;
                                }
                                v43 = v12;
                                *(iter2) = v47;
                                iter2 += 1;
                                iter1 += 2;
                            } while (iter1 < 0x3ff);
                            v48 = iter2 - &v20;
                            if (!g_1038b244(*((int *)(v28 + *(v43))), &v20, v48, &v13, 0))
                                goto LABEL_10360c68;
                        } while ((v49 = v13, v15 = (void*)(v15 + v49), v49 >= v48 && k - a3 < a4));
                    }
                    else
                    {
                        i = v36;
                        if (a4 <= NULL)
                            goto LABEL_10360ca2;
                        do
                        {
                            k = 0;
                            v50 = i - a3;
                            v0 = 2;
                            v51 = &v23;
                            do
                            {
                                if (v50 >= a4)
                                    break;
                                v52 = *((short *)i);
                                i += 2;
                                v50 += 2;
                                if (v52 == 10)
                                {
                                    *(v51) = 13;
                                    v51 += 1;
                                    k += 2;
                                }
                                k += 2;
                                *(v51) = v52;
                                v51 += 1;
                            } while (k < 338);
                            v53 = 0;
                            v54 = g_1038b040(65001, 0, &v23, (v51 - &v23) / 2, &v22, 683, 0, 0);
                            if (!v54)
                                goto LABEL_10360c68;
                            else
                                goto LABEL_10360bef;
                            do
                            {
LABEL_10360bef:
                                if (!g_1038b244(*((int *)(v28 + *(v12))), &(&v22)[v53], v54 - v53, &v13, 0))
                                {
                                    v18 = g_1038b07c();
                                    break;
                                }
                            } while ((v53 = (int)(v53 + v13), v54 > v53));
                        } while (v54 <= v53 && (v15 = (void*)(i - a3), v15 < a4));
                        goto LABEL_10360c68;
                    }
                }
            }
            else if (g_1038b244(v35->field_0, a3, a4, &v13, 0))
            {
                v18 = 0;
                v15 = v13;
            }
            else
            {
LABEL_10360c68:
                v18 = g_1038b07c();
            }
        }
LABEL_10360c71:
        if (!v15)
        {
            v43 = v12;
LABEL_10360c7b:
            v37 = 0;
            if (v18)
            {
                v1 = 5;
                v37 = 5;
                if (v18 == 5)
                {
                    *((unsigned int *)sub_103575e0()) = 9;
                    goto LABEL_10360cc2;
                }
                else
                {
                    sub_10357606(v18);
                    goto LABEL_10360cc9;
                }
            }
LABEL_10360ca2:
            if ((*((char *)(v28 + *(v43) + 4)) & 64) && *((char *)a3) == 26)
            {
                goto LABEL_10360cd1;
            }
            else
            {
                *((unsigned int *)sub_103575e0()) = 28;
LABEL_10360cc2:
                *((unsigned int *)sub_103575f3()) = v37;
            }
LABEL_10360cc9:
        }
LABEL_10360cd1:
    }
    return sub_10351225();
}
```

## `sub_10360ce9` `0x10360ce9`

_210 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a1440;
extern char g_103a3b70;
extern unsigned int g_103a3b80[4];

void sub_10360ce9(unsigned int a0)
{
    unsigned int v11;  // eax
    unsigned int *v12;  // ebx
    unsigned int v13;  // esi
    unsigned int v14;  // edx
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp+0x0]
    int v6;  // [bp+0xfffe8], Other Possible Types: unsigned int
    unsigned int v7;  // [bp+0x100000]
    unsigned int v8;  // [bp+0x10000c]
    void* v9;  // [bp+0x100010]
    void* v10;  // [bp+0x100014]

    sub_1035b0cc(&g_103a1440, 16);
    v11 = v8;
    if (v11 == 4294967294)
    {
        *((unsigned int *)sub_103575f3()) = 0;
        *((unsigned int *)sub_103575e0()) = 9;
    }
    else
    {
        if (v11 >= 0 && v11 < *((int *)&g_103a3b70))
        {
            v12 = &g_103a3b80[v11 >> 5];
            v13 = (v11 & 31) * 56;
            if ((*((char *)(*(v12) + v13 + 4)) & 1))
            {
                sub_10365188(v11);
                v7 = 0;
                if ((*((char *)(*(v12) + v13 + 4)) & 1))
                {
                    v6 = sub_10360723(v11, v14, v8, v9, v10);
                }
                else
                {
                    *((unsigned int *)sub_103575e0()) = 9;
                    *((unsigned int *)sub_103575f3()) = 0;
                    v6 = 4294967295;
                }
                v7 = 4294967294;
                sub_10360dbb();
                sub_1035b111(&g_103a1440, 16, v5, a0);
                return;
            }
        }
        *((unsigned int *)sub_103575f3()) = 0;
        *((unsigned int *)sub_103575e0()) = 9;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        sub_103535f2();
    }
    sub_1035b111(&g_103a1440, 16, v5, a0);
    return;
}
```

## `sub_10360dbb` `0x10360dbb`

_10 bytes. (leaf/helper — see body)_

```c
void sub_10360dbb(void)
{
    int v1;  // [bp+0x10000c]

    sub_10365228(v1);
    return;
}
```

## `sub_10360dc5` `0x10360dc5`

_68 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
    unsigned int field_4;
    struct struct_0 *field_8;
    unsigned int field_c;
    char padding_10[8];
    unsigned int field_18;
} struct_0;

extern unsigned int g_103a387c;

struct_0 * sub_10360dc5(struct_0 *idx)
{
    struct_0 *v0;  // eax
    struct_0 *v1;  // eax

    g_103a387c = g_103a387c + 1;
    v0 = sub_10357482(0x1000);
    idx->field_8 = v0;
    if (v0)
    {
        idx->field_c = idx->field_c | 8;
        idx->field_18 = 0x1000;
    }
    else
    {
        idx->field_c = idx->field_c | 4;
        idx->field_8 = &idx->padding_10[4];
        idx->field_18 = 2;
    }
    v1 = idx->field_8;
    idx->field_4 = 0;
    idx->field_0 = v1;
    return v1;
}
```

