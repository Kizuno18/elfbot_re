# elfbot.dll decompiled — jiru 0x10356fb1..0x10358760

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10356fb1` `0x10356fb1`

_79 bytes. (leaf/helper — see body)_

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

unsigned int sub_10356fb1(int a0, unsigned int *a1)
{
    unsigned int v3;  // eax
    struct_0 v0;  // [bp-0x14]
    struct_1 *idx;  // [bp-0xc]
    char v2;  // [bp-0x8]

    sub_103536a7(&v0, a1);
    v3 = (*((int *)(v0 + 172)) <= 1 ? *((char *)(*((int *)(v0 + 200)) + a0 * 2)) & 4 : sub_1035b7ea(a0, 4, &v0));
    if (v2)
        idx->field_70 = idx->field_70 & 4294967293;
    return v3;
}
```

## `sub_10357000` `0x10357000`

_41 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e738;
extern unsigned int g_103a3058;

unsigned int sub_10357000(int a0)
{
    if (g_103a3058)
        return sub_10356fb1(a0, NULL);
    return *((char *)(g_1038e738 + a0 * 2)) & 4;
}
```

## `sub_10357029` `0x10357029`

_79 bytes. (leaf/helper — see body)_

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

unsigned int sub_10357029(int a0, unsigned int *a1)
{
    unsigned int v3;  // eax
    struct_0 v0;  // [bp-0x14]
    struct_1 *idx;  // [bp-0xc]
    char v2;  // [bp-0x8]

    sub_103536a7(&v0, a1);
    v3 = (*((int *)(v0 + 172)) <= 1 ? *((char *)(*((int *)(v0 + 200)) + a0 * 2)) & 8 : sub_1035b7ea(a0, 8, &v0));
    if (v2)
        idx->field_70 = idx->field_70 & 4294967293;
    return v3;
}
```

## `sub_10357078` `0x10357078`

_41 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e738;
extern unsigned int g_103a3058;

unsigned int sub_10357078(int a0)
{
    if (g_103a3058)
        return sub_10357029(a0, NULL);
    return *((char *)(g_1038e738 + a0 * 2)) & 8;
}
```

## `sub_103570a1` `0x103570a1`

_917 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[254];
    unsigned short field_fe;
} struct_0;

typedef struct struct_4 {
    char padding_0[256];
    unsigned short field_100;
} struct_4;

typedef struct struct_3 {
    unsigned int field_0;
} struct_3;

extern struct_3 *g_1038b1f0;
extern struct_3 *g_1038b230;
extern unsigned int g_1038e180;
extern char g_10394e08;
extern char g_10394f88;

int sub_103570a1(void* idx)
{
    unsigned int v25;  // ebx
    unsigned int v26;  // esi
    unsigned int v35;  // ecx
    char *v36;  // ecx
    unsigned int v37;  // ecx
    struct_4 *v38;  // edx
    void* v39;  // edi
    unsigned int v27;  // edi
    void* v28;  // eax
    int i;  // eax
    char *iter;  // eax
    unsigned int j;  // edi
    unsigned int v32;  // ecx
    struct_0 *v33;  // eax
    struct_0 *v34;  // ecx
    unsigned int v0;  // [bp-0x74]
    unsigned int v1;  // [bp-0x70]
    unsigned int v2;  // [bp-0x6c]
    struct_0 *v3;  // [bp-0x68], Other Possible Types: unsigned int
    unsigned int v4;  // [bp-0x64]
    unsigned int v5;  // [bp-0x58]
    unsigned int v6;  // [bp-0x54]
    unsigned int v7;  // [bp-0x50]
    void* v8;  // [bp-0x4c]
    unsigned int v9;  // [bp-0x48]
    unsigned int v10;  // [bp-0x44]
    struct_0 *v11;  // [bp-0x40]
    struct_0 *v12;  // [bp-0x3c]
    unsigned int v13;  // [bp-0x38]
    int v14;  // [bp-0x34]
    unsigned int v15;  // [bp-0x30]
    unsigned int v16;  // [bp-0x2c]
    struct_0 *v17;  // [bp-0x28], Other Possible Types: struct_4 *
    unsigned int v18;  // [bp-0x24]
    char *v19;  // [bp-0x20], Other Possible Types: unsigned int
    char v20;  // [bp-0x1c], Other Possible Types: unsigned int
    int v22;  // [bp-0x16]
    unsigned int v23;  // [bp-0x8]
    char v24;  // [bp-0x4]

    v23 = g_1038e180 ^ &v24;
    v7 = v25;
    v6 = v26;
    v5 = v27;
    v15 = 0;
    v17 = NULL;
    v19 = 0;
    v16 = 0;
    v18 = 0;
    v8 = idx;
    v9 = 0;
    if ((int)idx[20])
    {
        v28 = idx + 4;
        if (*((int *)v28) || !sub_1035a196(&v8, 0, (short)idx[48], 4100, v28))
        {
            v15 = sub_10357482(4);
            v17 = sub_103574c2(384, 2);
            v19 = sub_103574c2(384, 1);
            v16 = sub_103574c2(384, 1);
            v18 = sub_103574c2(0x101, 1);
            if (v15 && v17 && v18 && v19 && v16)
            {
                *((unsigned int *)v15) = 0;
                i = 0;
                do
                {
                    *((char *)(i + v18)) = i;
                    i += 1;
                } while (i < 0x100);
                if (g_1038b230((int)idx[4], &v20) && v20 <= 5)
                {
                    v14 = (unsigned short)v20;
                    if (v14 > 1 && *((char *)&v22))
                    {
                        iter = &v22 - 1;
                        do
                        {
                            if (!*(iter))
                                break;
                            j = iter[1];
                            for (v32 = *(iter); j <= v32; j += 1)
                            {
                                *((char *)(j + v18)) = 32;
                                v32 = *(iter);
                            }
                            iter += 2;
                        } while (iter[1]);
                    }
                    v11 = v17 + 1;
                    if (sub_1035fbea(0, 1, v18, 0x100, v11, (int)idx[4], 0, 0) && sub_10356e55(NULL, (int)idx[20], 0x100, v18 + 1, 0xff, v19 + 129, 0xff, (int)idx[4], 0) && sub_10356e55(NULL, (int)idx[20], 0x200, v18 + 1, 0xff, v16 + 129, 0xff, (int)idx[4], 0))
                    {
                        v33 = v17;
                        v34 = &v33->field_fe;
                        *((unsigned short *)&v34->padding_0[0]) = 0;
                        v12 = v34;
                        v35 = v19 + 128;
                        *((char *)(v19 + 127)) = 0;
                        *((char *)(v16 + 127)) = 0;
                        *((char *)v35) = 0;
                        v10 = v35;
                        v13 = v16 + 128;
                        *((char *)v13) = 0;
                        if (v14 > 1 && *((char *)&v22))
                        {
                            v36 = &v22 - 1;
                            v19 = &v22 - 1;
                            do
                            {
                                if (!*(v36))
                                    break;
                                v37 = v36[1];
                                if (v37 <= *(v36))
                                {
                                    v38 = &v33->padding_0[2 * v37 + 0x100];
                                    while (true)
                                    {
                                        *((unsigned short *)&v38->padding_0[0]) = 0x8000;
                                        v37 += 1;
                                        v17 = &v38->padding_0[2];
                                        if (v37 > *(v19))
                                            break;
                                        v38 = v17;
                                    }
                                }
                                v36 = v19 + 2;
                                v19 = v36;
                            } while (v36[1]);
                        }
                        sub_10350b50(v33, v33 + 2, 254);
                        sub_10350b50(v19, v19 + 0x100, 127);
                        sub_10350b50(v16, v16 + 0x100, 127);
                        if ((int)idx[192] && !g_1038b1f0((int)idx[192]))
                        {
                            v3 = (int)idx[196] - 254;
                            sub_1035345e();
                            v2 = (int)idx[0xcc] - 128;
                            sub_1035345e();
                            v1 = (int)idx[208] - 128;
                            sub_1035345e();
                            v0 = (int)idx[192];
                            sub_1035345e();
                        }
                        *((unsigned int *)v15) = 1;
                        *((unsigned int *)&idx[192]) = v15;
                        *((struct_0 **)&idx[200]) = v11;
                        *((struct_0 **)&idx[196]) = v12;
                        *((unsigned int *)&idx[0xcc]) = v10;
                        *((unsigned int *)&idx[208]) = v13;
                        *((int *)&idx[172]) = v14;
                        goto LABEL_103573ad;
                    }
                }
            }
        }
        v4 = v15;
        sub_1035345e();
        v3 = v17;
        sub_1035345e();
        v2 = v19;
        sub_1035345e();
        v1 = v16;
        sub_1035345e();
LABEL_103573ad:
        v3 = v18;
        sub_1035345e();
    }
    else
    {
        v39 = idx + 192;
        if (*((int *)v39))
            g_1038b1f0(*((int *)v39));
        *((unsigned int *)v39) = 0;
        *((struct_0 **)&idx[196]) = NULL;
        *((wchar **)&idx[200]) = L"         (((((                  H\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x84\x84\x84\x84\x84\x84\x84\x84\x84\x84\x10\x10\x10\x10\x10\x10\x10\x81\x81\x81\x81\x81\x81\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x10\x10\x10\x10\x10\x10\x82\x82\x82\x82\x82\x82\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x10\x10\x10\x10 ";
        *((char **)&idx[0xcc]) = &g_10394e08;
        *((char **)&idx[208]) = &g_10394f88;
        *((int *)&idx[172]) = 1;
    }
    return sub_10351225();
}
```

## `sub_10357436` `0x10357436`

_38 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[108];
    struct struct_0 *field_6c;
    unsigned int field_70;
} struct_1;

typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern unsigned int g_1038e660;
extern char g_1038e748;

int sub_10357436(void)
{
    struct_1 *v1;  // ecx
    struct_0 *v2;  // eax

    v1 = sub_10358da8();
    v2 = v1->field_6c;
    if (v2 != *((int *)&g_1038e748) && !(g_1038e660 & v1->field_70))
        v2 = sub_10355e09();
    return v2->field_4;
}
```

## `sub_1035745c` `0x1035745c`

_38 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e660;
extern char g_1038e748;

int sub_1035745c(void)
{
    unsigned int v1[29];  // ecx
    unsigned int v2;  // eax

    v1 = sub_10358da8();
    v2 = v1[27];
    if (v2 != *((int *)&g_1038e748) && !(g_1038e660 & v1[28]))
        v2 = sub_10355e09();
    return v2 + 12;
}
```

## `sub_10357482` `0x10357482`

_64 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1b4;
extern char g_103a3060;

int sub_10357482(unsigned int a0)
{
    unsigned int v3;  // esi
    unsigned int v4;  // edi
    int v5;  // esi
    int v6;  // eax
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp-0x4]
    unsigned int v2;  // [bp+0x0]

    v1 = v3;
    v0 = v4;
    v5 = 0;
    while (true)
    {
        v6 = sub_10355a15(v2);
        if (v6)
        {
            return v6;
        }
        else if (*((int *)&g_103a3060) > v6)
        {
            g_1038b1b4(v5);
            v5 += 1000;
            if (v5 > *((int *)&g_103a3060))
                v5 = -1;
            if (v5 == -1)
                return v6;
        }
        else
        {
            return v6;
        }
    }
}
```

## `sub_103574c2` `0x103574c2`

_72 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1b4;
extern char g_103a3060;

unsigned int sub_103574c2(int a0, unsigned int a1)
{
    unsigned int v3;  // esi
    unsigned int v4;  // edi
    unsigned int v5;  // esi
    unsigned int v6;  // eax
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp-0x4]
    int v2;  // [bp+0x0]

    v1 = v3;
    v0 = v4;
    v5 = 0;
    while (true)
    {
        v6 = sub_1035ff29(v2, a0, 0);
        if (v6)
        {
            return v6;
        }
        else if (*((int *)&g_103a3060) > v6)
        {
            g_1038b1b4(v5);
            v5 += 1000;
            if (v5 > *((int *)&g_103a3060))
                v5 = 4294967295;
            if (v5 == 4294967295)
                return v6;
        }
        else
        {
            return v6;
        }
    }
}
```

## `sub_1035750a` `0x1035750a`

_75 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1b4;
extern char g_103a3060;

int sub_1035750a(int a0, unsigned int a1)
{
    unsigned int v3;  // esi
    unsigned int v4;  // edi
    int v5;  // esi
    int v6;  // eax
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp-0x4]
    int v2;  // [bp+0x0]

    v1 = v3;
    v0 = v4;
    v5 = 0;
    while (true)
    {
        v6 = sub_10360047(v2, a0);
        if (v6)
        {
            return v6;
        }
        else if (a0 == v6)
        {
            return v6;
        }
        else if (*((int *)&g_103a3060) > v6)
        {
            g_1038b1b4(v5);
            v5 += 1000;
            if (v5 > *((int *)&g_103a3060))
                v5 = -1;
            if (v5 == -1)
                return v6;
        }
        else
        {
            return v6;
        }
    }
}
```

## `sub_10357555` `0x10357555`

_80 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1b4;
extern char g_103a3060;

int sub_10357555(int a0, int a1, unsigned int a2)
{
    unsigned int v3;  // esi
    unsigned int v4;  // edi
    int v5;  // esi
    int v6;  // eax
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp-0x4]
    int v2;  // [bp+0x0]

    v1 = v3;
    v0 = v4;
    v5 = 0;
    while (true)
    {
        v6 = sub_10360262(v2, a0, a1);
        if (v6)
        {
            return v6;
        }
        else if (a1 == v6)
        {
            return v6;
        }
        else if (*((int *)&g_103a3060) > v6)
        {
            g_1038b1b4(v5);
            v5 += 1000;
            if (v5 > *((int *)&g_103a3060))
                v5 = -1;
            if (v5 == -1)
                return v6;
        }
        else
        {
            return v6;
        }
    }
}
```

## `sub_103575a5` `0x103575a5`

_59 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e2d0[4];
extern unsigned int g_1038e2d4[4];

unsigned int [4] sub_103575a5(unsigned int *a0)
{
    unsigned int v1;  // ecx
    unsigned int v0[4];  // [bp-0x4]

    v1 = 0;
    do
    {
        if (a0 == g_1038e2d0[2 * v1])
            return g_1038e2d4[2 * v1];
    } while ((v1 += 1, v1 < 45));
    if ((char *)&a0[4] + 3 > 0x11)
    {
        v0 = 0xe;
        return (-(v0 < a0 + 47) & v0) + 8;
    }
    v0 = 0xd;
    return v0;
}
```

## `sub_103575e0` `0x103575e0`

_19 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e438;

unsigned int sub_103575e0(void)
{
    unsigned int v1;  // eax

    v1 = sub_10358d31();
    if (v1)
        return v1 + 8;
    return &g_1038e438;
}
```

## `sub_103575f3` `0x103575f3`

_19 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e43c;

unsigned int sub_103575f3(void)
{
    unsigned int v1;  // eax

    v1 = sub_10358d31();
    if (v1)
        return v1 + 12;
    return &g_1038e43c;
}
```

## `sub_10357606` `0x10357606`

_30 bytes. (leaf/helper — see body)_

```c
unsigned int *[4] sub_10357606(unsigned int *a0)
{
    unsigned int v0[4];  // eax
    unsigned int *v1[4];  // eax

    *((unsigned int **)sub_103575f3()) = a0;
    v0 = sub_103575a5(a0);
    v1 = sub_103575e0();
    *(v1) = v0;
    return v1;
}
```

## `sub_10357624` `0x10357624`

_279 bytes. (leaf/helper — see body)_

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

int sub_10357624(int a0, unsigned int *a1)
{
    struct_0 *v9;  // ecx
    unsigned int v10;  // eax
    struct_0 *v11;  // ecx
    int v12;  // eax
    int v13;  // ecx
    int v14;  // eax
    unsigned int v0;  // [bp-0x28]
    struct_0 v1;  // [bp-0x1c]
    struct_1 *idx;  // [bp-0x14]
    char v3;  // [bp-0x10]
    char v4;  // [bp-0xc]
    char v5;  // [bp-0xb]
    char v6;  // [bp-0x8]
    char v7;  // [bp-0x7]
    char v8;  // [bp-0x6]

    sub_103536a7(&v1, a1);
    if (a0 < 0x100)
    {
        v9 = (struct_0 *)v1;
        if (*((int *)((char *)&v9[13].field_0 + 3)) > 1)
        {
            v10 = sub_1035b7ea(a0, 1, &v1);
            v11 = (struct_0 *)v1;
        }
        else
        {
            v10 = *((char *)(*((int *)((char *)&v9[15].field_4 + 1)) + a0 * 2)) & 1;
            v11 = v9;
        }
        if (!v10)
            goto LABEL_10357683;
        v12 = *((char *)(*((int *)((char *)&v11[15].field_8 + 1)) + a0));
    }
    else
    {
        if (*((int *)(v1 + 172)) > 1 && !((a0 = a0, a0 >>= 8, !sub_1035de48(a0 & 0xff, &v1))))
        {
            v0 = 2;
            v6 = a0;
            v7 = a0;
            v8 = 0;
            v13 = 2;
        }
        else
        {
            *((unsigned int *)sub_103575e0()) = 42;
            v6 = a0;
            v7 = 0;
            v13 = 1;
        }
        v14 = sub_10356e55(&v1, *((int *)((unsigned int)v1 + 20)), 0x100, &v6, v13, &v4, 3, *((int *)((unsigned int)v1 + 4)), 1);
        if (!v14)
        {
LABEL_10357683:
            if (!v3)
                return a0;
            idx->field_70 = idx->field_70 & 4294967293;
            return a0;
        }
        v12 = (v14 == 1 ? v4 : v4 * 0x100 | v5);
    }
    if (v3)
        idx->field_70 = idx->field_70 & 4294967293;
    return v12;
}
```

## `sub_1035773b` `0x1035773b`

_39 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a3058;

int sub_1035773b(int a0)
{
    if (g_103a3058)
    {
        return sub_10357624(a0, NULL);
    }
    else if (a0 - 65 <= 25)
    {
        return a0 + 32;
    }
    else
    {
        return a0;
    }
}
```

## `sub_10357762` `0x10357762`

_283 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[112];
    unsigned int field_70;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

typedef struct struct_2 {
    char padding_0[172];
    int field_ac;
    char padding_b0[24];
    unsigned int field_c8;
} struct_2;

typedef struct struct_4 {
    unsigned int field_0;
    unsigned int field_4;
    char padding_8[8];
    unsigned long long field_10;
} struct_4;

struct_1 * sub_10357762(char *a0, struct_0 **a1, unsigned int *a2)
{
    char *iter;  // esi
    struct_1 *idx;  // eax
    struct_4 *idx1;  // ecx
    unsigned short v14;  // ax
    unsigned int v15;  // cc_dep1
    unsigned int v16;  // fc3210
    unsigned short v17;  // ftop
    unsigned int v18;  // 4140
    unsigned int v0;  // [bp-0x54]
    unsigned int v1;  // [bp-0x50]
    unsigned int v2;  // [bp-0x4c]
    unsigned int v3;  // [bp-0x48]
    struct_2 **v4;  // [bp-0x44], Other Possible Types: unsigned int
    char v5;  // [bp-0x34]
    struct_0 v6;  // [bp-0x1c]
    struct_1 *index;  // [bp-0x14]
    char v8;  // [bp-0x10]
    double v9;  // [bp-0xc], Other Possible Types: unsigned long

    iter = a0;
    sub_103536a7(&v6, a2);
    if (a1)
        *(a1) = a0;
    if (!a0)
    {
        *((unsigned int *)sub_103575e0()) = 22;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        idx = (unsigned int)sub_103535f2();
        if (v8)
        {
            idx = index;
            idx->field_70 = idx->field_70 & 4294967293;
        }
        /* unsupported instruction */
        /* unsupported instruction */
        return idx;
    }
    else
    {
        while (true)
        {
            if (!(*((int *)(v6 + 172)) <= 1 ? *((char *)(*((int *)(v6 + 200)) + *(iter) * 2)) & 8 : sub_1035b7ea(*(iter), 8, &v6)))
                break;
            iter += 1;
        }
        v4 = &v6;
        v3 = 0;
        v2 = 0;
        idx1 = sub_103602e0(&v5, iter, sub_10352f20(iter));
        if (a1)
            *(a1) = &iter[idx1->field_4];
        v14 = idx1->field_0;
        if ((v14 & 576))
        {
            /* unsupported instruction */
            /* unsupported instruction */
            v9 = (/* unsupported instruction */ ? /* unsupported instruction */ : nan);
            /* unsupported instruction */
            if (a1)
                *(a1) = a0;
        }
        else if (((char)v14 & 129))
        {
            v15 = *(iter);
            if (/* unsupported instruction */)
            {
                /* unsupported instruction */
                /* unsupported instruction */
                if (v15 == 45)
                    goto LABEL_1035783a;
            }
            else
            {
                /* unsupported instruction */
                /* unsupported instruction */
                if (v15 == 45)
                {
LABEL_1035783a:
                    /* unsupported instruction */
                    /* unsupported instruction */
                }
            }
LABEL_10357850:
            if (/* unsupported instruction */)
            {
                v9 = /* unsupported instruction */;
                /* unsupported instruction */
            }
            else
            {
                v9 = (double)nan;
                /* unsupported instruction */
            }
            *((unsigned int *)sub_103575e0()) = 0x22;
        }
        else
        {
            if ((v14 & 0x100))
            {
                /* unsupported instruction */
                /* unsupported instruction */
                v16 = CmpF((/* unsupported instruction */ ? /* unsupported instruction */ : nan), idx1->field_10) * 0x100 & 0x4500;
                v18 = _ccall(10, 13, (unsigned int)((char)(((v17 - 1 & 7) * 0x800 | (unsigned short)v16 & 0x4700) >> 8) & 0x44), 0, 0);
                if (!((char)v18))
                    goto LABEL_10357850;
                /* unsupported instruction */
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
                v9 = /* unsupported instruction */;
                /* unsupported instruction */
            }
            else
            {
                v9 = (double)nan;
                /* unsupported instruction */
            }
        }
        if (v8)
            index->field_70 = index->field_70 & 4294967293;
        if (!/* unsupported instruction */)
        {
            /* unsupported instruction */
            /* unsupported instruction */
            return idx;
        }
        /* unsupported instruction */
        /* unsupported instruction */
        return idx;
    }
}
```

## `sub_1035787d` `0x1035787d`

_19 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[112];
    unsigned int field_70;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

struct_1 * sub_1035787d(char *a0, struct_0 **a1)
{
    return sub_10357762(a0, a1, NULL);
}
```

## `sub_10357890` `0x10357890`

_11 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    unsigned int field_8;
} struct_0;

extern char g_10395090;

void sub_10357890(struct_0 *a0)
{
    *((char **)&a0->padding_0[0]) = &g_10395090;
    sub_103532d2(a0);
    return;
}
```

## `sub_1035789b` `0x1035789b`

_34 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    unsigned int field_8;
} struct_0;

extern char g_10395090;

struct_0 * sub_1035789b(struct_0 *a0, char a1)
{
    struct_0 *v0;  // [bp-0x8]

    *((char **)&a0->padding_0[0]) = &g_10395090;
    sub_103532d2(a0);
    if ((a1 & 1))
    {
        v0 = a0;
        sub_10350abd();
    }
    return a0;
}
```

## `sub_103578bd` `0x103578bd`

_92 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char field_0;
    char padding_1[3];
    struct struct_0 *field_4;
} struct_1;

typedef struct struct_0 {
    char padding_0[8];
    char field_8;
} struct_0;

typedef struct struct_2 {
    char field_0;
    char padding_1[3];
    unsigned int field_4;
} struct_2;

unsigned int sub_103578bd(struct_1 *a0, struct_2 *a1, unsigned int *a2)
{
    struct_0 *v0;  // eax
    unsigned int v1;  // edx

    v0 = a0->field_4;
    if (v0)
    {
        v1 = &v0->field_8;
        if (*((char *)v1) && (v0 != a1->field_4 && sub_10359ed0(v1, a1->field_4 + 8) || (a1->field_0 & 2) && !(a0->field_0 & 8) || ((char)*(a2) & 1) && !(a0->field_0 & 1) || ((char)*(a2) & 2) && !(a0->field_0 & 2)))
            return 0;
    }
    return 1;
}
```

## `sub_10357919` `0x10357919`

_68 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

typedef struct struct_1 {
    char padding_0[144];
    unsigned int field_90;
} struct_1;

unsigned int sub_10357919(struct_0 **a0)
{
    struct_1 *idx;  // eax

    if (*(a0)->field_0 == 3762507597)
    {
        if (*((int *)(sub_10358da8() + 144)) <= 0)
            return 0;
        idx = sub_10358da8();
        idx->field_90 = idx->field_90 - 1;
        return 0;
    }
    else if (*(a0)->field_0 == 3765269347)
    {
        *((unsigned int *)(sub_10358da8() + 144)) = 0;
    }
    else
    {
        return 0;
    }
}
```

## `sub_1035795d` `0x1035795d`

_166 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    unsigned int field_8;
} struct_0;

typedef struct struct_1 {
    char padding_0[144];
    unsigned int field_90;
} struct_1;

extern int g_103a1058;

void sub_1035795d(void)
{
    struct_0 *v7;  // edi
    void* idx;  // ebx
    int i;  // esi
    struct_1 *index;  // eax
    unsigned int v11;  // eax
    int *v12;  // ecx
    int v1;  // [bp+0xfffe4]
    int v2;  // [bp+0xfffe8]
    unsigned int v3;  // [bp+0x100000]
    void* v4;  // [bp+0x10000c]
    struct_0 *v5;  // [bp+0x100014]
    int v6;  // [bp+0x100018]

    sub_1035b0cc(&g_103a1058, 16);
    v7 = v5;
    idx = v4;
    v2 = (v7->field_4 <= 128 ? (char)idx[8] : (int)idx[8]);
    index = sub_10358da8();
    index->field_90 = index->field_90 + 1;
    for (v3 = 0; i != v6; v2 = i)
    {
        if (i <= -1 || i >= v7->field_4)
            sub_1035911a();
        v11 = i * 8;
        v12 = v7->field_8 + v11;
        i = *(v12);
        v1 = i;
        v3 = 1;
        if (v12[1])
        {
            *((int *)&idx[8]) = i;
            sub_10359170(*((int *)(v7->field_8 + v11 + 4)), idx, 259);
        }
        v3 = 0;
    }
    v3 = 4294967294;
    sub_10357a23();
    if (i != v6)
        sub_1035911a();
    *((int *)&idx[8]) = i;
    sub_1035b111();
    return;
}
```

## `sub_103579df` `0x103579df`

_10 bytes. (leaf/helper — see body)_

```c
unsigned int sub_103579df(void)
{
    unsigned int **v1;  // [bp+0xffff0]

    return sub_10357919(v1);
}
```

## `sub_103579e9` `0x103579e9`

_16 bytes. (leaf/helper — see body)_

```c
void sub_103579e9(void)
{
    unsigned int v1;  // [bp+0x100000]

    v1 = 0;
}
```

## `sub_10357a1d` `0x10357a1d`

_6 bytes. (leaf/helper — see body)_

```c
void sub_10357a1d(void)
{
    sub_10357a23();
    return;
}
```

## `sub_10357a23` `0x10357a23`

_27 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[144];
    int field_90;
} struct_0;

struct_0 * sub_10357a23(void)
{
    struct_0 *v1;  // eax
    struct_0 *v2;  // eax

    v1 = sub_10358da8();
    if (v1->field_90 <= 0)
        return v1;
    v2 = sub_10358da8() + 144;
    *((unsigned int *)&v2->padding_0[0]) = *((int *)&v2->padding_0[0]) - 1;
    return v2;
}
```

## `sub_10357a3e` `0x10357a3e`

_69 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    char padding_4[12];
    unsigned int field_10;
    unsigned int field_14;
    char padding_18[4];
    unsigned int field_1c;
} struct_0;

int sub_10357a3e(void)
{
    struct_0 **v1;  // eax
    unsigned int v2[8];  // eax
    unsigned int v3;  // ecx

    v2 = *(v1);
    if (v2[0] != 3765269347)
    {
        return;
    }
    else if (v2[4] == 3)
    {
        v3 = v2[5];
        if (v3 != 429065504 && v3 != 429065505 && v3 != 429065506)
            return;
        if (v2[7])
            return;
        *((unsigned int *)(sub_10358da8() + 524)) = 1;
        return;
    }
    else
    {
        return;
    }
}
```

## `sub_10357a83` `0x10357a83`

_67 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    unsigned int field_0;
    char padding_4[20];
    unsigned int field_18;
    struct struct_0 *field_1c;
} struct_1;

typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern int g_103a1080;

int sub_10357a83(void)
{
    struct_1 *v3;  // ecx
    unsigned int v4;  // eax
    unsigned int v1;  // [bp+0x100000]
    struct_1 *v2;  // [bp+0x10000c]

    sub_1035b0cc(&g_103a1080, 8);
    v3 = v2;
    if (v3 && v3->field_0 == 3765269347 && v3->field_1c)
    {
        v4 = v3->field_1c->field_4;
        if (v4)
        {
            v1 = 0;
            sub_103528e4(v3->field_18, v4);
            v1 = 4294967294;
        }
    }
    return sub_1035b111();
}
```

## `sub_10357ac6` `0x10357ac6`

_9 bytes. (leaf/helper — see body)_

```c
int sub_10357ac6(void)
{
    char v1;  // [bp+0x100010]

    return v1;
}
```

## `sub_10357acf` `0x10357acf`

_8 bytes. (leaf/helper — see body)_

```c
void sub_10357acf(void)
{
}
```

## `sub_10357ad7` `0x10357ad7`

_37 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    int field_4;
    unsigned int field_8;
} struct_0;

unsigned int sub_10357ad7(unsigned int a0, struct_0 *idx)
{
    unsigned int v0;  // eax

    v0 = idx->field_0 + a0;
    if (idx->field_4 >= 0)
        v0 += *((int *)(*((int *)(idx->field_4 + a0)) + idx->field_8)) + idx->field_4;
    return v0;
}
```

## `sub_10357afc` `0x10357afc`

_19 bytes. (leaf/helper — see body)_

```c
char sub_10357afc(void)
{
    return *((int *)(sub_10358da8() + 144));
}
```

## `sub_10357b0f` `0x10357b0f`

_121 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    int field_0;
    unsigned int field_4;
} struct_0;

typedef struct struct_3 {
    char padding_0[28];
    struct struct_2 *field_1c;
} struct_3;

typedef struct struct_2 {
    char padding_0[12];
    struct struct_1 *field_c;
} struct_2;

typedef struct struct_1 {
    int field_0;
    struct struct_2 *field_4;
    char field_8;
} struct_1;

typedef struct struct_2 {
    char field_0;
    char padding_1[3];
    unsigned int field_4;
} struct_2;

char sub_10357b0f(struct_3 *idx)
{
    struct_0 *v5;  // edi
    unsigned int v6;  // ebx
    unsigned int v7;  // esi
    int v8;  // ebx
    unsigned int v9;  // esi
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    int v3;  // [bp-0xc]
    char v4;  // [bp-0x5]

    if (!v5)
    {
        sub_1035911a();
    }
    else
    {
        v3 = 0;
        v4 = 0;
        if (v5->field_0 <= NULL)
            return v4;
        v1 = v6;
        v0 = v7;
        do
        {
            v8 = idx->field_1c->field_c->field_0;
            v9 = &idx->field_1c->field_c->field_4;
            if (idx->field_1c->field_c->field_0 > NULL)
            {
                v2 = v3 * 16;
                do
                {
                    if (sub_103578bd(v5->field_4 + v2, *((int *)v9), idx->field_1c))
                    {
                        v4 = 1;
                        break;
                    }
                } while ((v8 = (int)(v8 - 1), v9 += 4, v8 > 0));
            }
        } while ((v3 = (int)(v3 + 1), v3 < v5->field_0));
        return v4;
    }
}
```

## `sub_10357b88` `0x10357b88`

_49 bytes. (leaf/helper — see body)_

```c
void sub_10357b88(void)
{
    unsigned int v1;  // [bp+0x100000]

    sub_10355b0b(4);
    if (*((int *)(sub_10358da8(4) + 148)))
        sub_1035911a();
    v1 = 0;
    sub_10359107();
    v1 = 4294967295;
}
```

## `sub_10357bb9` `0x10357bb9`

_24 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[148];
    unsigned int field_94;
} struct_0;

void sub_10357bb9(void)
{
    struct_0 *v2;  // eax
    unsigned int v1;  // [bp+0x10000c]

    v2 = sub_10358da8();
    v2->field_94 = v1;
    sub_103533ea(0, NULL);
    __debugbreak();
}
```

## `sub_10357bd1` `0x10357bd1`

_172 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

typedef struct struct_1 {
    char padding_0[140];
    unsigned int field_8c;
} struct_1;

extern int g_103a10f8;

int sub_10357bd1(unsigned int a0)
{
    void* v14;  // edi
    struct_0 *v15;  // esi
    int v16;  // ecx
    struct_1 *v17;  // eax
    unsigned int v1;  // [bp+0xfffd0]
    unsigned int v2;  // [bp+0xfffd4]
    unsigned int v3;  // [bp+0xfffd8]
    unsigned int v4[2];  // [bp+0xfffdc]
    unsigned int v5;  // [bp+0xfffe0]
    int v6;  // [bp+0xfffe8], Other Possible Types: unsigned int
    unsigned int v7;  // [bp+0x100000]
    struct_0 *v8;  // [bp+0x10000c]
    void* v9;  // [bp+0x100010]
    unsigned int v10;  // [bp+0x100014]
    int v11;  // [bp+0x100018]
    int v12;  // [bp+0x10001c]
    int v13;  // [bp+0x100020]

    sub_1035b0cc(&g_103a10f8, 44);
    v14 = v9;
    v15 = v8;
    v6 = v16;
    v1 = 0;
    v5 = (int)v14[4];
    v4[0] = sub_10352b88(/* unsupported instruction */ - 60, v15->field_18);
    v3 = *((int *)(sub_10358da8() + 0x88));
    v2 = *((int *)(sub_10358da8() + 140));
    *((struct_0 **)(sub_10358da8() + 0x88)) = v15;
    v17 = sub_10358da8();
    v17->field_8c = v10;
    v7 = 0;
    v10 = 1;
    v7 = 1;
    v6 = sub_10352c1d(v14, v11, v16, v12, v13);
    v7 = 0;
    v7 = 4294967294;
    v10 = 0;
    sub_10357cf7();
    return sub_1035b111();
}
```

## `sub_10357c61` `0x10357c61`

_9 bytes. (leaf/helper — see body)_

```c
int sub_10357c61(void)
{
    return sub_10357a3e();
}
```

## `sub_10357c6a` `0x10357c6a`

_107 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    unsigned int field_8;
    unsigned int field_c;
    unsigned int field_10;
} struct_0;

void sub_10357c6a(void)
{
    struct_0 *idx;  // esi
    void* v8;  // edi
    int v9;  // ecx
    unsigned int v10;  // ebx
    unsigned int v11;  // eax
    unsigned int i;  // [bp+0xfffe4]
    unsigned int v2;  // [bp+0xfffe8]
    unsigned int v3;  // [bp+0xfffec]
    unsigned int v4;  // [bp+0x100000]
    void* v5;  // [bp+0x100010]
    struct_0 *v6;  // [bp+0x100018]

    /* unsupported instruction */ = v3 - 4;
    *((unsigned int *)(sub_10358da8() + 524)) = 0;
    idx = v6;
    v8 = v5;
    v9 = (idx->field_4 <= 128 ? (char)v8[8] : (int)v8[8]);
    v10 = idx->field_10;
    for (i = 0; i < idx->field_c; i += 1)
    {
        v11 = i * 20 + v10;
        if (v9 > *((int *)(v11 + 4)) && v9 <= *((int *)(v11 + 8)))
        {
            v9 = *((int *)(idx->field_8 + *((int *)(v11 + 4)) * 8 + 8));
            break;
        }
    }
    /* unsupported instruction */ = /* unsupported instruction */ - 4;
    *((int *)(/* unsupported instruction */ - 4)) = v9;
    /* unsupported instruction */ = /* unsupported instruction */ - 4;
    *((struct_0 **)(/* unsupported instruction */ - 4)) = idx;
    *((unsigned int *)(/* unsupported instruction */ - 4)) = 0;
    *((void* *)(/* unsupported instruction */ - 8)) = v8;
    sub_1035795d();
    v2 = 0;
    v4 = 0;
}
```

## `sub_10357cf1` `0x10357cf1`

_6 bytes. (leaf/helper — see body)_

```c
void sub_10357cf1(void)
{
    sub_10357cf7();
    return;
}
```

## `sub_10357cf7` `0x10357cf7`

_118 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[140];
    unsigned int field_8c;
} struct_1;

typedef struct struct_0 {
    char padding_0[136];
    unsigned int field_88;
} struct_0;

typedef struct struct_2 {
    unsigned int field_0;
    char padding_4[12];
    unsigned int field_10;
    struct struct_1 *field_14;
    unsigned int field_18;
} struct_2;

struct_1 * sub_10357cf7(void)
{
    void* v10;  // edi
    struct_0 *v11;  // eax
    struct_1 *v12;  // eax
    struct_2 *v13;  // esi
    struct_1 *v14;  // eax
    struct_1 *v15;  // eax
    struct_2 *v0;  // [bp-0x8]
    unsigned int v1;  // [bp-0x4]
    unsigned int v3;  // [bp+0xfffd0]
    unsigned int v4;  // [bp+0xfffd4]
    unsigned int v5;  // [bp+0xfffd8]
    unsigned int *v6;  // [bp+0xfffdc]
    unsigned int v7;  // [bp+0xfffe0]
    unsigned int v8;  // [bp+0xfffe8]
    unsigned int v9;  // [bp+0x100014]

    *((unsigned int *)&v10[4]) = v7;
    sub_10352bd1(v6);
    v11 = sub_10358da8();
    v11->field_88 = v5;
    v12 = sub_10358da8();
    v12->field_8c = v4;
    if (v13->field_0 != 3765269347)
    {
        return v12;
    }
    else if (v13->field_10 == 3)
    {
        v14 = v13->field_14;
        if (v14 != 0x19930520 && v14 != 0x19930521 && v14 != 0x19930522)
            return v14;
        if (v3)
        {
            return v14;
        }
        else if (v8)
        {
            v15 = sub_10352bb0(v13->field_18);
            if (!v15)
                return v15;
            v1 = v9;
            v0 = v13;
            return sub_10357a83();
        }
        else
        {
            return v14;
        }
    }
    else
    {
        return v12;
    }
}
```

## `sub_10357d6d` `0x10357d6d`

_371 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    int field_0;
    struct struct_0 *field_4;
    unsigned int field_8;
} struct_1;

typedef struct struct_0 {
    char padding_0[8];
    char field_8;
} struct_0;

typedef struct struct_2 {
    char field_0;
    char padding_1[19];
    unsigned int field_14;
} struct_2;

extern int g_103a1120;

int sub_10357d6d(void)
{
    struct_1 *v8;  // eax
    int v9;  // eax
    void* v10;  // esi
    unsigned int v11;  // eax
    struct_2 *v12;  // edi
    unsigned int v13;  // eax
    struct_2 *v0;  // [bp-0xc], Other Possible Types: unsigned int
    unsigned int v2;  // [bp+0xfffe8]
    unsigned int v3;  // [bp+0x100000]
    void* v4;  // [bp+0x10000c]
    void* v5;  // [bp+0x100010]
    struct_1 *v6;  // [bp+0x100014]
    struct_2 *v7;  // [bp+0x100018]

    sub_1035b0cc(&g_103a1120, 12);
    v2 = 0;
    v8 = v6;
    if (v8->field_4 && v8->field_4->field_8 && (v8->field_8 || (v8->field_0 & 0x80000000)))
    {
        v9 = v8->field_0;
        v10 = v5;
        if (v9 >= 0)
            v10 = v8->field_8 + v5 + 12;
        v3 = 0;
        v0 = 1;
        if (((char)v9 & 8))
        {
            if (sub_10360385((int)v4[24]) && sub_10360385(v10, 1))
            {
                v11 = (int)v4[24];
                *((unsigned int *)v10) = v11;
                v0 = &v7->padding_1[7];
                goto LABEL_10357df2;
            }
LABEL_10357ec7:
            sub_1035911a();
        }
        else
        {
            v12 = v7;
            if ((1 & v12->field_0))
            {
                if (!sub_10360385((int)v4[24]) || !sub_10360385(v10, 1))
                    goto LABEL_10357ec7;
                sub_10350ec0(v10, (int)v4[24], v12->field_14);
                if (v12->field_14 == 4 && (v11 = (unsigned int)*((int *)v10), v11))
                {
                    v0 = &v12->padding_1[7];
                    v0 = &v12->padding_1[7];
LABEL_10357df2:
                    *((unsigned int *)v10) = sub_10357ad7(v11, v0);
                }
            }
            else if (!*((int *)&v12[1].field_0))
            {
                if (!sub_10360385() || !sub_10360385(v10, 1))
                    goto LABEL_10357ec7;
                v13 = sub_10357ad7((int)v4[24], &v12->padding_1[7]);
                sub_10350ec0(v10, v13, v12->field_14);
            }
            else
            {
                if (!sub_10360385() || !sub_10360385(v10, 1) || !sub_10360385(*((int *)&v12[1].field_0)))
                    goto LABEL_10357ec7;
                v0 = 0;
                v2 = (unsigned int)(((v12->field_0 & 4)) + 1);
            }
        }
        v3 = 4294967294;
    }
    return sub_1035b111();
}
```

## `sub_10357ed8` `0x10357ed8`

_4 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10357ed8(void)
{
    return 1;
}
```

## `sub_10357edc` `0x10357edc`

_8 bytes. (leaf/helper — see body)_

```c
void sub_10357edc(void)
{
}
```

## `sub_10357eec` `0x10357eec`

_133 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    int field_4;
    unsigned int field_8;
} struct_0;

extern int g_103a1140;

int sub_10357eec(void)
{
    unsigned int v10[3];  // eax
    unsigned int v11;  // ebx
    struct_0 *v12;  // esi
    struct_0 *v13;  // edi
    int v14;  // eax
    struct_0 *v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2[3];  // [bp-0x10], Other Possible Types: unsigned int
    struct_0 *v3;  // [bp-0xc], Other Possible Types: unsigned int
    unsigned int v5;  // [bp+0x100000]
    struct_0 *v6;  // [bp+0x10000c]
    unsigned int v7;  // [bp+0x100010]
    unsigned int v8[3];  // [bp+0x100014]
    struct_0 *v9;  // [bp+0x100018]

    sub_1035b0cc(&g_103a1140, 8);
    v10 = v8;
    v11 = (!(v10[0] & 0x80000000) ? v10[2] + v7 + 12 : v7);
    v5 = 0;
    v12 = v9;
    v3 = v12;
    v2 = v10;
    v1 = v7;
    v13 = v6;
    v0 = v13;
    v14 = sub_10357d6d();
    if (v14 == 1)
    {
        v3 = sub_10357ad7(v13[2].field_0, &v12->field_8);
        sub_103528e4(v11, v12[2].field_0);
    }
    else if (v14 == 2)
    {
        v3 = 1;
        v2 = sub_10357ad7(v13[2].field_0, &v12->field_8);
        sub_103528e4(v11, v12[2].field_0);
    }
    v5 = 4294967294;
    return sub_1035b111();
}
```

## `sub_10357f71` `0x10357f71`

_4 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10357f71(void)
{
    return 1;
}
```

## `sub_10357f75` `0x10357f75`

_8 bytes. (leaf/helper — see body)_

```c
void sub_10357f75(void)
{
}
```

## `sub_10357f7d` `0x10357f7d`

_108 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
} struct_0;

typedef struct struct_1 {
    char padding_0[8];
    unsigned int field_8;
} struct_1;

int sub_10357f7d(unsigned int a0, unsigned int a1, struct_0 *a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, struct_1 *a8)
{
    struct_0 *v10;  // ebx
    struct_1 *v11;  // esi
    int v12;  // ecx
    unsigned int v13[2];  // edi
    unsigned int v14;  // eax
    struct_0 *v0;  // [bp-0x2c]
    struct_1 *v1;  // [bp-0x28]
    unsigned int v2;  // [bp-0x24]
    unsigned int v3;  // [bp-0x20]
    unsigned int v4;  // [bp-0x1c]
    unsigned int v5;  // [bp-0x18]
    struct_0 *v6;  // [bp-0x14], Other Possible Types: struct_1 *
    struct_1 *v7;  // [bp-0x10], Other Possible Types: unsigned int
    struct_0 *v8;  // [bp-0xc], Other Possible Types: struct_1 *, unsigned int
    unsigned int v9;  // [bp-0x8]

    if (a6)
    {
        v9 = a6;
        v8 = v10;
        v7 = v11;
        v6 = a2;
        sub_10357eec();
    }
    if (!a8)
    {
        v8 = v11;
        v8 = v11;
    }
    else
    {
        v8 = a8;
        v8 = a8;
    }
    sub_103528eb(v12, v8, a2);
    v9 = v13[0];
    v8 = a5;
    v7 = a4;
    v6 = v11;
    sub_1035795d();
    v5 = 0x100;
    v4 = a7;
    v3 = a5;
    v11->field_8 = v13[1] + 1;
    v2 = a3;
    v1 = v11;
    v0 = a2;
    v14 = sub_10357bd1(v10->field_c);
    if (!v14)
        return v14;
    return sub_103528b4(v14, v11);
}
```

## `sub_10357fe9` `0x10357fe9`

_242 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[128];
    unsigned int field_80;
} struct_0;

typedef struct struct_1 {
    char padding_0[12];
    unsigned int field_c;
} struct_1;

typedef struct struct_2 {
    char padding_0[8];
    char field_8;
} struct_2;

unsigned int sub_10357fe9(unsigned int a0, unsigned int a1, unsigned int *a2, unsigned int a3, unsigned int a4, unsigned int a5, struct_1 *a6, int a7, unsigned int a8, unsigned int a9)
{
    int v3;  // edi
    struct_0 *v4;  // eax
    unsigned int v13;  // edx
    unsigned int v14;  // eax
    unsigned int v5;  // eax
    unsigned int v6;  // eax
    int v7;  // esi
    unsigned int iter[5];  // eax
    unsigned int v9;  // ebx
    int v10;  // esi
    void* v11;  // eax
    struct_2 *v12;  // ecx
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v2 = a0;
    v1 = a0;
    if (*(a2) == 2147483651)
        return v14;
    if (*((int *)(sub_10358da8(v3) + 128)))
    {
        v4 = sub_10358da8();
        v5 = sub_10358b83();
        if (v4->field_80 != v5 && *(a2) != 3762507597 && !((v6 = sub_103529a3(a2, a3, a4, a5, a6, a8, a9), !v6)))
            goto LABEL_103580d7;
    }
    if (!a6->field_c)
        sub_1035911a();
    v7 = a7;
    iter = sub_10352b15(a6, a8, v7, &v2, &v1);
    v6 = v2;
    if (v6 < v1)
    {
        v0 = v9;
        do
        {
            v10 = v7;
            if (v10 >= iter[0])
            {
                v10 = v7;
                if (v10 <= iter[1])
                {
                    v11 = iter[3] * 16 + iter[4];
                    v12 = (int)v11[12];
                    if (!v12 || (v10 = v7, !v12->field_8))
                    {
                        v10 = v7;
                        if (!((char)v11[16] & 64))
                        {
                            sub_10357f7d(v12, v13, a2, a4, a5, a6, 0, a8, a9);
                            v10 = a7;
                        }
                    }
                }
            }
        } while ((v7 = v10, v2 += 1, v6 = v2, iter += 20, v6 < v1));
    }
LABEL_103580d7:
    return v6;
}
```

## `sub_103580db` `0x103580db`

_854 bytes. refs "bad exception"_

```c
typedef struct struct_2 {
    unsigned int field_0;
    int field_4;
    char padding_8[4];
    unsigned int field_c;
    char padding_10[12];
    struct struct_1 *field_1c;
} struct_2;

typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    unsigned int field_8;
} struct_0;

typedef struct struct_3 {
    char padding_0[12];
    int field_c;
    unsigned int field_10;
} struct_3;

typedef struct struct_1 {
    char padding_0[12];
    struct struct_0 *field_c;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    char field_8;
} struct_0;

extern int g_1038e444;
extern unsigned int g_10395090;
extern char g_103a115c;

unsigned int [38] sub_103580db(unsigned int a0, unsigned int a1, struct_2 *idx, void* a2, unsigned int a3, unsigned int a4, struct_2 *a5, char a6, unsigned int a7, void* a8)
{
    void* v17;  // ecx
    unsigned int v18;  // ebx
    unsigned int v26[2];  // edi
    unsigned int v27;  // esi
    unsigned int v28;  // eax
    struct_2 *v29;  // edi
    struct_3 *iter;  // eax
    unsigned int node;  // ebx
    unsigned int v32;  // ecx
    unsigned int v33;  // edx
    struct_2 *v19;  // ebx
    unsigned int v35[38];  // eax
    unsigned int v20;  // edi
    struct_2 *v21;  // ebx
    unsigned int i;  // ebx
    unsigned int v24[38];  // eax
    void* v0;  // [bp-0x4c]
    unsigned int v1;  // [bp-0x48]
    struct_2 *v2;  // [bp-0x44], Other Possible Types: void*
    struct_1 *v3;  // [bp-0x40], Other Possible Types: unsigned int
    unsigned int v4;  // [bp-0x3c]
    struct_2 *v5;  // [bp-0x38]
    unsigned int v6;  // [bp-0x34]
    unsigned int v7;  // [bp-0x30]
    struct_0 v8;  // [bp-0x30]
    unsigned int v9;  // [bp-0x24]
    unsigned int v10;  // [bp-0x20]
    int v11;  // [bp-0x1c]
    int v12;  // [bp-0x18]
    unsigned int v13;  // [bp-0x14]
    unsigned int v14;  // [bp-0x10]
    unsigned int v15;  // [bp-0xc]
    char v16;  // [bp-0x5]

    v17 = a2;
    v6 = v18;
    v19 = a5;
    v5 = idx;
    v4 = v20;
    v16 = 0;
    v15 = (v19->field_4 <= 128 ? (char)v17[8] : (int)v17[8]);
    if (v15 < 4294967295 || v15 >= v19->field_4)
        sub_1035911a();
    v21 = v19;
    if (idx->field_0 == 3765269347)
    {
        i = 429065504;
        if (*((int *)&idx->padding_10[0]) == 3 && (*((int *)&idx->padding_10[4]) == 429065504 || *((int *)&idx->padding_10[4]) == 429065505 || *((int *)&idx->padding_10[4]) == 429065506) && !idx->field_1c)
        {
            v24 = sub_10358da8();
            if (!v24[0x22])
                return v24;
            idx = *((int *)(sub_10358da8() + 0x88));
            a3 = *((int *)(sub_10358da8() + 140));
            if (!sub_10360385(idx, 1))
                sub_1035911a();
            if (idx->field_0 == 3765269347 && *((int *)&idx->padding_10[0]) == 3 && (*((int *)&idx->padding_10[4]) == 429065504 || *((int *)&idx->padding_10[4]) == 429065505 || *((int *)&idx->padding_10[4]) == 429065506) && !idx->field_1c)
                sub_1035911a();
            if (*((int *)(sub_10358da8() + 148)))
            {
                v26 = *((int *)(sub_10358da8() + 148));
                v27 = 0;
                *((unsigned int *)(sub_10358da8() + 148)) = 0;
                idx = idx;
                if (!sub_10357b0f(idx))
                {
                    if (v26[0] > 0)
                    {
                        for (i = 0; !(char)sub_103531e8(*((int *)(i + v26[1] + 4)), &g_1038e444); i += 16)
                        {
                            v27 += 1;
                        }
                        v3 = 1;
                        v2 = idx;
                        sub_10357a83();
                        idx = "bad exception";
                        sub_10353214(&v8, &idx);
                        v7 = &g_10395090;
                        sub_103533ea(&v7, &g_103a115c);
                    }
                }
            }
        }
        if (idx->field_0 == 3765269347 && *((int *)&idx->padding_10[0]) == 3 && !((v28 = (unsigned int)*((int *)&idx->padding_10[4]), *((int *)&idx->padding_10[4]) != i && *((int *)&idx->padding_10[4]) != 429065505 && *((int *)&idx->padding_10[4]) != 429065506)))
        {
            v29 = a5;
            if (v29->field_c > 0)
            {
                for (iter = sub_10352b15(v29, a7, v15, &v13, &v10); v13 < v10; iter += 1)
                {
                    if (*((int *)&iter->padding_0[0]) <= v15 && v15 <= *((int *)&iter->padding_0[4]))
                    {
                        v14 = iter->field_10;
                        v11 = iter->field_c;
                        if (iter->field_c > 0)
                        {
                            do
                            {
                                node = &idx->field_1c->field_c->field_4;
                                v12 = idx->field_1c->field_c->field_0;
                                if (idx->field_1c->field_c->field_0 <= 0)
                                    continue;
                                do
                                {
                                    v9 = *((int *)node);
                                    if (sub_103578bd(v14, *((int *)node), idx->field_1c))
                                    {
                                        v16 = 1;
                                        sub_10357f7d(v32, v33, idx, a3, a4, a5, v9, a7, a8);
                                        goto LABEL_10358343;
                                    }
                                } while ((v12 = (int)(v12 - 1), node += 4, v12 > 0));
                            } while ((v11 = (int)(v11 - 1), v14 += 16, v11 > 0));
                        }
                    }
LABEL_10358343:
                    v13 += 1;
                }
                v29 = a5;
            }
            if (a6)
            {
                v3 = 1;
                v2 = idx;
                sub_10357a83();
            }
            if (v16 || (v29->field_0 & 0x1fffffff) < 429065505 || !v29->field_1c || sub_10357b0f(idx))
                goto LABEL_10358419;
            sub_10358da8();
            sub_10358da8();
            *((struct_2 **)(sub_10358da8() + 0x88)) = idx;
            *((unsigned int *)(sub_10358da8() + 140)) = a3;
            if (!a8)
            {
                v2 = a2;
                v2 = a2;
            }
            else
            {
                v2 = a8;
                v2 = a8;
            }
            sub_103528eb(a3, v2, idx);
            idx = a5;
            v3 = 4294967295;
            v2 = idx;
            v1 = a4;
            v0 = a2;
            sub_1035795d();
            v3 = idx->field_1c;
            sub_10357b88();
        }
        v21 = a5;
    }
    if (v21->field_c > 0 && !a6)
        sub_10357fe9(v32, v33, idx, a2, a3, a4, v21, v15, a7, a8);
LABEL_10358419:
    v35 = sub_10358da8();
    if (!v35[37])
        return v35;
    return sub_1035911a();
}
```

## `sub_10358431` `0x10358431`

_24 bytes. (leaf/helper — see body)_

```c
extern char g_10395090;

void* sub_10358431(void* a0, void* a1)
{
    sub_1035327a(a0, a1);
    *((char **)a0) = &g_10395090;
    return a0;
}
```

## `sub_10358449` `0x10358449`

_228 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    unsigned int field_0;
    char field_4;
    char padding_5[11];
    unsigned int field_10;
    unsigned int field_14;
    char padding_18[4];
    struct struct_0 *field_1c;
} struct_2;

typedef struct struct_0 {
    char padding_0[8];
    struct struct_1 *field_8;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

unsigned int sub_10358449(unsigned int a0, unsigned int a1, struct_2 *a2, void* a3, unsigned int a4, unsigned int a5, struct_2 *a6, unsigned int a7, void* a8, char a9)
{
    unsigned int v8;  // edx
    void* v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    struct_2 *v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    int v6;  // [bp-0x8]
    char v7;  // [bp+0x0]

    if (*((int *)(sub_10358da8(v4, v5, v6, &v7) + 524)) || a2->field_0 == 3765269347 || a2->field_0 == 2147483686 || (a6->field_0 & 0x1fffffff) < 429065506 || !((char)a6[1].field_0 & 1))
    {
        if ((a2->field_4 & 0x66))
        {
            if (*((int *)&a6->field_4) && !a7)
            {
                v3 = 4294967295;
                v2 = a6;
                v1 = a5;
                v0 = a3;
                sub_1035795d();
            }
        }
        else
        {
            if (*((int *)&a6->padding_5[7]) || (a6->field_0 & 0x1fffffff) >= 429065505 && a6->field_1c)
            {
                if (a2->field_0 == 3765269347 && a2->field_10 >= 3 && a2->field_14 > 429065506 && a2->field_1c->field_8)
                    return a2->field_1c->field_8(a2, a3, a4, a5, a6, a7, a8, a9);
                sub_103580db(a2, v8, a2, a3, a4, a5, a6, a9, a7, a8);
            }
        }
    }
    return 1;
}
```

## `sub_1035852d` `0x1035852d`

_243 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b20c;
extern struct_0 *g_1038b210;
extern unsigned int g_1038e180;
extern char g_1038e464;

void sub_1035852d(void)
{
    int v27;  // esi
    unsigned int v28;  // eax
    unsigned short v37;  // fs
    unsigned short v38;  // gs
    unsigned int v39;  // 4174
    unsigned int v40;  // id
    unsigned int v41;  // ac
    unsigned int v29;  // ecx
    unsigned int v30;  // edx
    unsigned int v31;  // ebx
    unsigned int v32;  // edi
    unsigned short v33;  // ss
    unsigned short v34;  // cs
    unsigned short v35;  // ds
    unsigned short v36;  // es
    unsigned int v0;  // [bp-0x334]
    char v1;  // [bp-0x32c], Other Possible Types: unsigned int
    unsigned int v2;  // [bp-0x320]
    char *v3;  // [bp-0x2dc]
    char *v4;  // [bp-0x2d8]
    unsigned int v5;  // [bp-0x2d4]
    char v6;  // [bp-0x2ac]
    unsigned short v7;  // [bp-0x248]
    unsigned short v8;  // [bp-0x244]
    unsigned short v9;  // [bp-0x240]
    unsigned short v10;  // [bp-0x23c]
    unsigned int v11;  // [bp-0x238]
    int v12;  // [bp-0x234]
    unsigned int v13;  // [bp-0x230]
    unsigned int v14;  // [bp-0x22c]
    unsigned int v15;  // [bp-0x228]
    unsigned int v16;  // [bp-0x224]
    unsigned int v17;  // [bp-0x220]
    unsigned int v18;  // [bp-0x21c]
    unsigned short v19;  // [bp-0x218]
    unsigned int v20;  // [bp-0x214]
    char *v21;  // [bp-0x210]
    unsigned short v22;  // [bp-0x20c]
    unsigned int v23;  // [bp-0x8]
    unsigned int v24;  // [bp-0x4]
    char v25;  // [bp+0x0], Other Possible Types: unsigned int

    v23 = g_1038e180 ^ &v6;
    if ((g_1038e464 & 1))
        sub_10359fbd(10);
    v28 = sub_1035c882(v27);
    if (v28)
        v28 = sub_1035c88f(22);
    if ((g_1038e464 & 2))
    {
        v16 = v28;
        v15 = v29;
        v14 = v30;
        v13 = v31;
        v12 = v27;
        v11 = v32;
        v22 = v33;
        v19 = v34;
        v10 = v35;
        v9 = v36;
        v8 = v37;
        v7 = v38;
        v39 = _ccall(13, (unsigned int)(g_1038e464 & 2), 0, 0);
        v0 = v39 | 0x202 | v40 * 0x200000 & 0x200000 | v41 * 0x40000 & 0x40000;
        v20 = v39 | 0x202 | v40 * 0x200000 & 0x200000 | v41 * 0x40000 & 0x40000;
        v21 = &v25;
        v5 = 65537;
        v18 = v25;
        v17 = v24;
        sub_10350ad0(&v1, 0, 80);
        v3 = &v1;
        v1 = 1073741845;
        v2 = v18;
        v4 = &v5;
        g_1038b210(0);
        g_1038b20c(&v3);
    }
    sub_10353f33(3);
    __debugbreak();
}
```

## `sub_10358620` `0x10358620`

_30 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e464;

unsigned int sub_10358620(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // eax

    v0 = g_1038e464;
    g_1038e464 = ~(a1) & v0 | a0 & a1;
    return v0;
}
```

## `sub_1035863e` `0x1035863e`

_219 bytes. (leaf/helper — see body)_

```c
int sub_1035863e(void)
{
    void* v10;  // ecx
    unsigned int v11;  // edi
    unsigned int v20;  // edx
    void* iter;  // ecx
    char v22;  // 4106
    unsigned int *v12;  // eax
    void* v13;  // ecx
    unsigned int v15;  // eax
    unsigned int v16;  // eax
    void* node;  // ecx
    void* iter1;  // edi
    unsigned int v19;  // eax
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x1c]
    unsigned int v4;  // [bp-0x18]
    unsigned int v5;  // [bp-0x14]
    void* iter2;  // [bp-0x8], Other Possible Types: unsigned int
    unsigned int v7;  // [bp+0x4]
    unsigned int v8;  // [bp+0x8]
    unsigned int v9;  // [bp+0xc]

    iter2 = v10;
    if (!v10)
    {
        v5 = 22;
        v5 = 0;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        *((unsigned int *)sub_103575e0()) = v5;
        sub_103535f2();
        return;
    }
    v5 = v11;
    if (v7 <= NULL)
    {
LABEL_10358670:
        v12 = sub_103575e0();
        v4 = 22;
        goto LABEL_10358677;
    }
    *((char *)v10) = 0;
    if (v7 <= (unsigned int)((v9) + 1))
    {
LABEL_1035869e:
        v12 = sub_103575e0();
        v4 = 0x22;
LABEL_10358677:
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        *(v12) = v4;
        sub_103535f2();
    }
    else
    {
        if (v8 - 2 > 0x22)
            goto LABEL_10358670;
        iter2 = 0;
        v13 = v10;
        if (v9)
        {
            *((char *)v10) = 45;
            iter2 = 1;
            v16 = -(v15);
            v13 = v10 + 1;
        }
        node = v13;
        iter1 = node;
        do
        {
            v19 = v16 / v8;
            v20 = v16 % v8;
        } while ((*((char *)node) = (v20 <= 9 ? (char)v20 + 48 : (char)v20 + 87), node += 1, iter2 += 1, v19 > 0 && (v16 = v19, iter2 < v7)));
        if (iter2 >= v7)
        {
            *((char *)v10) = 0;
            goto LABEL_1035869e;
        }
        else
        {
            *((char *)node) = 0;
            iter = node - 1;
            do
            {
                v22 = *((char *)iter);
                *((char *)iter) = *((char *)iter1);
                iter -= 1;
                *((char *)iter1) = v22;
                iter1 += 1;
            } while (iter1 < iter);
        }
    }
    return;
}
```

## `sub_10358719` `0x10358719`

_40 bytes. (leaf/helper — see body)_

```c
int sub_10358719(int a0, unsigned int a1, int a2, unsigned int a3)
{
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    if (a3 == 10 && a0 < 0)
    {
        v1 = 1;
        v0 = 10;
    }
    else
    {
        v1 = 0;
        v0 = a3;
    }
    return sub_1035863e(a2);
}
```

## `sub_10358741` `0x10358741`

_79 bytes. (leaf/helper — see body)_

```c
void sub_10358741(void* iter, unsigned int a1)
{
    unsigned int i;  // ecx

    i = a1 >> 7;
    do
    {
        memset(iter, 0, 128);
        iter += 128;
        i -= 1;
    } while (i != 1);
    return;
}
```

## `sub_10358759` `0x10358759`

_7 bytes. (leaf/helper — see body)_

```c
void sub_10358759(void)
{
    sub_10358760();
    return;
}
```

## `sub_10358760` `0x10358760`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10358760(void)
{
}
```

