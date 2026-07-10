# elfbot.dll decompiled — jiru 0x1031bdd0..0x1031ddd0

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1031bdd0` `0x1031bdd0`

_82 bytes. (leaf/helper — see body)_

```c
int sub_1031bdd0(unsigned int a0, int a1, int a2)
{
    unsigned int v0;  // [bp-0x14]
    char v1;  // [bp-0xa]
    char v2;  // [bp-0x9]

    v0 = a0;
    sub_1031a280(&v0);
    sub_103147d0(a0);
    sub_10314750(a0, 0, 0);
    sub_103378b0(&v2, &/* unsupported instruction */);
    sub_1031be30(a1, a2, _INSERT(0, 0, v1));
    return a0;
}
```

## `sub_1031be30` `0x1031be30`

_159 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

void sub_1031be30(unsigned int a0, char *i, char *a2)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4154
    unsigned int v11;  // eax
    unsigned long v12;  // 4176
    int v13;  // edi
    int v14;  // esi
    int v15;  // ebx
    unsigned long v16;  // 4122
    unsigned int v0;  // [bp-0x2c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]
    char v6;  // [bp+0x0]

    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v11 = *((int *)v10);
    v3 = *((int *)v10);
    v2 = a0;
    v0 = g_1038e180 ^ &v5;
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v12) = &v3;
    v1 = 0;
    sub_1031bf50(i, a2, &v1, g_1038e180 ^ &v5, v13, v14, v15, a0, 0, &v0, v11, sub_1036b660, -1, &v6);
    sub_1031bf00(0);
    for (v4 = 0; i != a2; i += 1)
    {
        sub_103170f0(a0, 1, *(i));
    }
    v16 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v16) = v11;
    return;
}
```

## `sub_1031beb4` `0x1031beb4`

_34 bytes. (leaf/helper — see body)_

```c
extern char g_1031bedd;

int sub_1031beb4(void)
{
    unsigned int *v1;  // [bp+0xfffec]
    unsigned int v2;  // [bp+0x100000]

    sub_10314750(v1, 1, 0);
    sub_103533ea(0, 0);
    v2 = 4294967295;
    return &g_1031bedd;
}
```

## `sub_1031bf00` `0x1031bf00`

_79 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    struct struct_0 *field_14;
} struct_0;

struct_0 * sub_1031bf00(struct_0 *a0, struct_0 *a1)
{
    struct_0 *v1;  // eax
    struct_0 *v0;  // [bp-0x8]

    if (a0->field_14 > a1)
    {
        return a0;
    }
    else if (*((int *)&a0[1].padding_0[0]) != a1)
    {
        v0 = a0->field_14;
        v1 = sub_103149b0(a0, a1, 1);
        if (!*((char *)&v1))
            return v1;
        return sub_10314960(a0, v0);
    }
    else
    {
        return *((int *)&a0[1].padding_0[0]);
    }
}
```

## `sub_1031bf50` `0x1031bf50`

_47 bytes. (leaf/helper — see body)_

```c
int sub_1031bf50(int a0, int a1, int a2)
{
    int v1;  // ecx
    int v2;  // edx
    char v0;  // [bp+0x0]

    v2 = _INSERT(0, 0, *((char *)sub_103378b0((char *)&v1 + 3, &/* unsupported instruction */, v1, &v0)));
    return sub_1031bf80(a0, a1, a2, v2);
}
```

## `sub_1031bf80` `0x1031bf80`

_21 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1031bf80(unsigned int a0, unsigned int a1, unsigned int *a2)
{
    unsigned int v0;  // eax

    v0 = a1 - a0 + *(a2);
    *(a2) = v0;
    return v0;
}
```

## `sub_1031bfa0` `0x1031bfa0`

_29 bytes. (leaf/helper — see body)_

```c
char sub_1031bfa0(char *a0)
{
    do
    {
        if (false)
            break;
    } while (*(a0) != 0xcc);
    return (0 ? 0 : 1);
}
```

## `sub_1031bfc0` `0x1031bfc0`

_71 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1031bfc0(unsigned int a0, unsigned int a1)
{
    if (!a0)
        return a0 + 8;
    if ((unsigned int)(a0 % 4))
    {
        a0 = (a0 >> 2) * 4 + 4;
        if (a0 >= a1)
            a0 -= 4;
    }
    return a0;
}
```

## `sub_1031c010` `0x1031c010`

_17 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c874[4];
extern unsigned int g_103a24e8;

unsigned int [4] sub_1031c010(void)
{
    return g_1038c874[g_103a24e8];
}
```

## `sub_1031c030` `0x1031c030`

_10 bytes. (leaf/helper — see body)_

```c
extern char g_103a24f0;

int sub_1031c030(void)
{
    return &g_103a24f0;
}
```

## `sub_1031c040` `0x1031c040`

_31 bytes. refs "Insufficient memory!"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b30c;

unsigned int sub_1031c040(void)
{
    char v0;  // [bp+0x0]

    g_1038b30c(0, "Insufficient memory!", 0, 16, &v0);
    sub_10353f22(1);
    return 0;
}
```

## `sub_1031c060` `0x1031c060`

_865 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
    unsigned int field_10;
    char padding_14[12];
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    char padding_2c[4];
    unsigned int field_30;
    unsigned int field_34;
    unsigned int field_38;
    char padding_3c[4];
    unsigned int field_40;
    char padding_44[4];
    unsigned int field_48;
    unsigned int field_4c;
    char padding_50[4];
    unsigned int field_54;
    char padding_58[4];
    unsigned int field_5c;
    char padding_60[12];
    unsigned int field_6c;
    unsigned int field_70;
    unsigned int field_74;
    unsigned int field_78;
    unsigned int field_7c;
    unsigned int field_80;
    unsigned int field_84;
} struct_0;

extern unsigned int g_1038e180;
extern char g_103a2610;
extern unsigned int g_103a262c;

int sub_1031c060(int a0, struct_0 *idx, char a2)
{
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    unsigned int v21;  // eax
    unsigned int v22;  // eax
    int v23;  // edx
    unsigned int v24;  // eax
    unsigned int v25;  // eax
    unsigned int v26;  // eax
    unsigned int v27;  // eax
    unsigned int v28;  // eax
    unsigned short v14;  // fs
    unsigned int v29;  // eax
    unsigned int v30;  // eax
    unsigned int v31;  // eax
    unsigned int v32;  // eax
    unsigned int v33;  // eax
    unsigned int v34;  // eax
    unsigned int v35;  // eax
    unsigned long v15;  // 4176
    unsigned long v36;  // 4135
    unsigned int v16;  // esi
    unsigned int v17;  // edi
    unsigned long v18;  // 4180
    unsigned int v19;  // eax
    unsigned int v20;  // eax
    unsigned int v0;  // [bp-0x34]
    unsigned int v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x2c]
    char v3;  // [bp-0x25]
    unsigned int v4;  // [bp-0x20]
    int i;  // [bp-0x1c]
    unsigned int v6;  // [bp-0x18]
    int v7;  // [bp-0x14]
    unsigned int v8;  // [bp-0x10]
    unsigned int v9;  // [bp-0xc]
    char v10;  // [bp-0x8], Other Possible Types: unsigned int
    char v11;  // [bp-0x4]

    v10 = 4294967295;
    v9 = sub_1036b6a7;
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    v8 = *((int *)v15);
    v2 = v16;
    v1 = v17;
    v0 = g_1038e180 ^ &v11;
    v18 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v18) = &v8;
    v4 = 0;
    if (!((char)g_103a262c & 1))
    {
        g_103a262c = g_103a262c | 1;
        v10 = 1;
        sub_10315800(&g_103a2610);
        sub_10353c80(sub_10373dc0);
        v10 = 0;
    }
    if (a2)
    {
        sub_1031e2d0();
        sub_10353f9f(idx->field_4c + idx->field_20 ^ idx->field_6c - idx->field_78 ^ idx->field_24 + idx->field_7c ^ idx->field_5c - idx->field_54 ^ idx->field_30 + idx->field_48 ^ idx->field_28 - idx->field_38 ^ idx->field_40 + idx->field_80 ^ idx->field_c - idx->field_34 ^ idx->field_70 + idx->field_10 ^ idx->field_74 - idx->field_84);
        for (i = 0; i < 8; i += 1)
        {
            switch (i)
            {
            case 0:
                sub_10353fac();
                v19 = sub_10354090();
                v20 = sub_10353fac();
                v6 = v19 | v20 ^ idx->field_20;
                v7 = v23;
                break;
            case 1:
                sub_10353fac();
                v21 = sub_10354090();
                v22 = sub_10353fac();
                v6 = v21 | v22 ^ idx->field_78;
                v7 = v23;
                break;
            case 2:
                sub_10353fac();
                v24 = sub_10354090();
                v25 = sub_10353fac();
                v6 = v24 | v25 ^ idx->field_7c;
                v7 = v23;
                break;
            case 3:
                sub_10353fac();
                v26 = sub_10354090();
                v27 = sub_10353fac();
                v6 = v26 | v27 ^ idx->field_54;
                v7 = v23;
                break;
            case 4:
                sub_10353fac();
                v28 = sub_10354090();
                v29 = sub_10353fac();
                v6 = v28 | v29 ^ idx->field_48;
                v7 = v23;
                break;
            case 5:
                sub_10353fac();
                v30 = sub_10354090();
                v31 = sub_10353fac();
                v6 = v30 | v31 ^ idx->field_38;
                v7 = v23;
                break;
            case 6:
                sub_10353fac();
                v32 = sub_10354090();
                v33 = sub_10353fac();
                v6 = v32 | v33 ^ idx->field_80;
                v7 = v23;
                break;
            case 7:
                sub_10353fac();
                v34 = sub_10354090();
                v35 = sub_10353fac();
                v6 = v34 | v35 ^ idx->field_34;
                v7 = v23;
                break;
            }
            v6 = sub_10353fd0(v6, v7, 36, 0);
            v7 = v23;
            if (v7 <= 0 && (v7 < 0 || v6 < 10))
                v3 = 48;
            else
                v3 = 65;
            sub_1031e310(v3 + v6);
        }
    }
    sub_103145d0(a0, &g_103a2610);
    v36 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int *)v36) = v8;
    return a0;
}
```

## `sub_1031c3f0` `0x1031c3f0`

_14 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a2660;

int sub_1031c3f0(unsigned short a0)
{
    g_103a2660 = a0;
    return a0;
}
```

## `sub_1031c400` `0x1031c400`

_1151 bytes. refs ", 1) || !sub_10363e79(g_103a22b0 + 1, "_

```c
typedef struct struct_0 {
    char field_0;
} struct_0;

extern unsigned int g_1038c7f4;
extern unsigned int g_1038c7fc;
extern unsigned int g_1038c808;
extern unsigned int g_1038c818;
extern unsigned int g_1038c828;
extern unsigned int g_1038c834;
extern unsigned int g_103a22a8;
extern struct_0 *g_103a22b0;
extern unsigned int g_103a24e8;

unsigned int sub_1031c400(void)
{
    unsigned int *v18;  // edx
    int v0;  // [bp-0x90]
    int v1;  // [bp-0x8c]
    unsigned int *v2;  // [bp-0x88]
    unsigned int v3;  // [bp-0x84]
    unsigned int v4;  // [bp-0x80]
    unsigned int idx;  // [bp-0x7c]
    int v6;  // [bp-0x74]
    unsigned int v7;  // [bp-0x70]
    unsigned int v8;  // [bp-0x38]
    unsigned int *i;  // [bp-0x34]
    unsigned int *v10;  // [bp-0x30]
    unsigned int *v11;  // [bp-0x20], Other Possible Types: unsigned int
    unsigned int v12;  // [bp-0x1c]
    int v13;  // [bp-0x18]
    int v14;  // [bp-0x14], Other Possible Types: unsigned int
    unsigned int v15;  // [bp-0xc]
    char v16;  // [bp-0x5]

    sub_102eb9c0((g_1038c7f4 ^ g_1038c834 ^ g_1038c808) & 3);
    v12 = sub_1031c880();
    if (!v12)
    {
        g_103a24e8 = 1;
        return 0;
    }
    v8 = g_1038c828 ^ g_1038c7fc ^ g_1038c808 ^ g_1038c818;
    i = v8 + v12;
    v15 = (!(unsigned int)(v8 % 0x1000) ? v8 : ((v8 >> 12) + 1) * 0x1000);
    v10 = v12 + v15;
    v11 = 0;
    sub_1033a4c0(v8);
    v1 = sub_1034fef0(-((v8 >= 0x20000000 ? 1 : 0) & 1) | v8 * 4);
    v13 = v1;
    sub_10350ad0(v13, -1, v8 * 4);
    for (; i < v10 + 1; i += 4)
    {
        v11 = i;
        v3 = sub_102eb8f0(&v6, v8);
        if (*((int *)(v13 + idx * 4)) != 4294967295)
        {
            for (idx = sub_1031bfc0(v3, v8); *((int *)(v13 + idx * 4)) != 4294967295; idx = sub_1031bfc0(sub_102eb8f0(&v6, v8), v8));
            *((unsigned int *)(v13 + idx * 4)) = idx;
        }
        else
        {
            *((unsigned int *)(v13 + idx * 4)) = idx;
        }
        v2 = idx + v12;
        v4 = *(v11);
        *(v11) = *(v2);
        *(v2) = v4;
    }
    v0 = v13;
    sub_10350eb5(v0);
    v14 = v12 + 8;
    v16 = 0;
    if (g_103a22a8 == 1 && (g_103a22b0->field_0 == 47 || (v18 = (unsigned int *)(int)(char)g_103a22b0->field_0, v18 == 0x2d)) && (!sub_10363e79(g_103a22b0 + 1, "s", 1) || !sub_10363e79(g_103a22b0 + 1, "p", 1)))
        v16 = 1;
    v7 = 0;
    v14 = sub_1031c9c0(v14, &v7, _INSERT(v18, 0, v16));
    if (v14)
        sub_1031cd70(v14); /* do not return */
    return 0;
}
```

## `sub_1031c880` `0x1031c880`

_310 bytes. refs "z5O["_

```c
typedef struct struct_0 {
    char padding_0[60];
    unsigned int field_3c;
} struct_0;

typedef struct struct_1 {
    char padding_0[6];
    unsigned short field_6;
    char padding_8[252];
    unsigned int field_104;
    unsigned int field_108;
    char padding_10c[16];
    unsigned int field_11c;
} struct_1;

extern unsigned int g_1038e180;
extern struct_0 *g_103a2234;

int sub_1031c880(void)
{
    unsigned long v19;  // ldt
    unsigned long v20;  // gdt
    unsigned short v21;  // fs
    unsigned long v22;  // 4176
    unsigned long v23;  // 4180
    unsigned long v24;  // 4114
    unsigned int v0;  // [bp-0x60]
    unsigned int v1;  // [bp-0x5c]
    unsigned int v2;  // [bp-0x58]
    int v3;  // [bp-0x54]
    int v4;  // [bp-0x50]
    unsigned int v5;  // [bp-0x4c]
    struct_0 *v6;  // [bp-0x48]
    struct_1 *v7;  // [bp-0x44]
    struct_1 *iter;  // [bp-0x40]
    struct_1 *v9;  // [bp-0x3c]
    char v10;  // [bp-0x38]
    unsigned int v11;  // [bp-0x1c]
    struct_0 *v12;  // [bp-0x18]
    unsigned int v13;  // [bp-0x14]
    unsigned int v14;  // [bp-0x10]
    unsigned int v15;  // [bp-0xc]
    unsigned int v16;  // [bp-0x8]
    char v17;  // [bp-0x4]

    v16 = 4294967295;
    v15 = sub_1036b6ca;
    v22 = _ccall(v19, v20, (unsigned int)v21, 0);
    v14 = *((int *)v22);
    v11 = g_1038e180 ^ &v17;
    v1 = v11;
    v23 = _ccall(v19, v20, (unsigned int)v21, 0);
    *((unsigned int **)v23) = &v14;
    v12 = g_103a2234;
    if (v12)
    {
        v6 = v12;
        v9 = &v12->padding_0[v6->field_3c];
        v7 = &v9->padding_8[240];
        iter = v7;
        v5 = v9->field_6;
        sub_1031c060(&v10, "z5O[", 1);
        v16 = 0;
        v13 = 0;
        while (true)
        {
            if (v13 < v5)
            {
                if ((*((int *)&iter->padding_8[28]) & 0x40000000) && *((int *)&iter->padding_8[8]) >= 8)
                {
                    v4 = &v12->padding_0[*((int *)&iter->padding_8[4])];
                    v0 = 8;
                    if (!sub_10351234(v4, (unsigned int)sub_102ec980(&v10)))
                    {
                        v3 = v4;
                        v16 = 4294967295;
                        sub_10314610(&v10);
                        break;
                    }
                }
                v13 += 1;
                iter = &iter->padding_8[32];
            }
            else
            {
                v2 = 0;
                v16 = 4294967295;
                sub_10314610(&v10);
                break;
            }
        }
    }
    v24 = _ccall(v19, v20, (unsigned int)v21, 0);
    *((unsigned int *)v24) = v14;
    return sub_10351225();
}
```

## `sub_1031c9c0` `0x1031c9c0`

_618 bytes. refs "ARMSPLASHOFF"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b068;
extern unsigned int g_1038e180;
extern char g_1038f8e4;
extern unsigned int g_103a2238;
extern unsigned int g_103a2660;

int sub_1031c9c0(void* iter, unsigned int *a1, char a2)
{
    int v0;  // [bp-0x12c]
    int v1;  // [bp-0x128]
    unsigned int v2;  // [bp-0x124]
    unsigned int v3;  // [bp-0x124]
    unsigned int v4;  // [bp-0x120]
    int v5;  // [bp-0x11c]
    unsigned int v6;  // [bp-0x118]
    char v7;  // [bp-0x114]
    char v8;  // [bp-0x113]
    unsigned int v9;  // [bp-0x10]
    int v10;  // [bp-0xc]
    char v11;  // [bp-0x5]
    char v12;  // [bp-0x4]

    v9 = g_1038e180 ^ &v12;
    *(a1) = 0;
    v11 = *((char *)iter);
    iter += 1;
    if (v11 == 1)
    {
        if (!a2 && g_103a2238 != 8)
            *(a1) = sub_1031ece0(0);
    }
    else
    {
        if (v11 == 2 || v11 == 3)
        {
            g_103a2660 = *((short *)iter);
            iter += 2;
            v4 = *((int *)iter);
            iter += 4;
            v1 = sub_1034fef0(v4 + 0x10000);
            v5 = v1;
            v10 = v5;
            while (true)
            {
                v6 = v4 + 0x10000;
                iter = sub_1031cc30(iter, v10, &v6, 0);
                if (!iter)
                    return sub_10351225();
                if (!v6)
                    break;
                v10 += v6;
            }
            v7 = g_1038f8e4;
            sub_10350ad0(&v8, 0, 0xff);
            if (!g_1038b068("ARMSPLASHOFF", &v7, 0x100))
            {
                v7 = 0;
            }
            else if (v7 == 48 || !v7)
            {
                v7 = 0;
            }
            else
            {
                v7 = 1;
            }
            if (!v7 && !a2 && g_103a2238 != 8 && g_103a2238 != 9)
                sub_1031f410(v5, v11 == 3, 0);
            v0 = v5;
            sub_10350eb5(v0);
        }
    }
    while (*((char *)iter))
    {
        iter += 1;
        for (iter += 4; (v2 = (unsigned int)*((int *)iter), iter += 4, v3 = v2 & 2147483647, (v2 & 2147483647)); iter += v3);
    }
    iter += 1;
    return sub_10351225();
}
```

## `sub_1031cc30` `0x1031cc30`

_320 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    void* field_4;
} struct_0;

extern unsigned int g_103a24e8;

unsigned int * sub_1031cc30(unsigned int *iter, unsigned int a1, unsigned int *a2, unsigned int a3)
{
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    struct_0 *v3;  // [bp-0x18], Other Possible Types: unsigned int
    unsigned int v4;  // [bp-0x14]
    int v5;  // [bp-0x10], Other Possible Types: unsigned int
    unsigned int v6;  // [bp-0xc]
    char v7;  // [bp-0x5]

    v7 = 0;
    v6 = *(iter);
    iter += 1;
    if ((v6 & 0x80000000))
    {
        v6 &= 2147483647;
        v7 = 1;
    }
    if (v6)
    {
        if (a1)
        {
            if (!v7)
            {
                v4 = sub_1034fef0(v6 + 0x100);
                v5 = sub_1034fef0(v6 + 0x100);
                sub_10350b50(sub_1034fef0(v6 + 0x100), iter, v6);
                iter = (char *)iter + v6;
                if (a3)
                {
                    v2 = 0;
                    v1 = v6;
                    v0 = sub_1034fef0(v6 + 0x100);
                    sub_102ec8b0(a3, v3, sub_1034fef0(v6 + 0x100), sub_1034fef0(v6 + 0x100));
                }
                v6 = sub_102ebca0(sub_1034fef0(v6 + 0x100), a1, v6, *(a2));
                if (!v6)
                {
                    g_103a24e8 = 0;
                    return NULL;
                }
                v3 = sub_1034fef0(v6 + 0x100);
                sub_10350eb5(sub_1034fef0(v6 + 0x100));
                v6 = v6;
            }
            else
            {
                sub_10350b50(a1, iter, v6);
                iter = (char *)iter + v6;
                if (a3)
                {
                    v2 = 0;
                    v1 = v6;
                    v0 = a1;
                    sub_102ec8b0(a3, v3, v4, v5);
                    v6 = v6;
                }
            }
        }
        else
        {
            iter = (char *)iter + v6;
        }
    }
    *(a2) = v6;
    return iter;
}
```

## `sub_1031cd70` `0x1031cd70`

_151 bytes. (leaf/helper — see body)_

```c
void sub_1031cd70(unsigned int a0, unsigned int a1, unsigned int *a2)
{
    unsigned int v16;  // eax
    unsigned int v17;  // ebx
    unsigned int v26;  // 4101
    unsigned int v27;  // 4101
    unsigned int *v28;  // eax
    unsigned int v29;  // 4163
    unsigned int v30;  // id
    unsigned int v31;  // ac
    unsigned int v32;  // 4110
    unsigned int v18;  // esi
    unsigned int v19;  // edi
    unsigned int v20;  // 4101
    unsigned int v21;  // 4103
    unsigned int v22;  // 4101
    unsigned int v23;  // 4101
    unsigned int v24;  // 4101
    unsigned int v25;  // 4101
    unsigned int v0;  // [bp-0x8c]
    unsigned int v1;  // [bp-0x88]
    unsigned int v2;  // [bp-0x88]
    char *v3;  // [bp-0x84]
    unsigned int v4;  // [bp-0x84]
    char *v5;  // [bp-0x80]
    char *v6;  // [bp-0x7c], Other Possible Types: unsigned int
    unsigned int v7;  // [bp-0x78]
    unsigned int v8;  // [bp-0x78]
    unsigned int v9;  // [bp-0x74]
    unsigned int v10;  // [bp-0x74]
    unsigned int *v11;  // [bp-0x70], Other Possible Types: unsigned int
    unsigned int v12;  // [bp-0x6c]
    char v13;  // [bp-0x68]
    unsigned int v14;  // [bp-0x38]
    char v15;  // [bp-0x4]

    v12 = v16;
    v11 = a0;
    v10 = a1;
    v8 = v17;
    v6 = &v13;
    v5 = &v15;
    v4 = v18;
    v1 = v19;
LABEL_1031cd92:
    v20 = _ccall(0, 15, 0, 0, 0);
    if ((char)v20)
        goto LABEL_1031cd94;
    else
        goto LABEL_1031cd95;
    while (true)
    {
LABEL_1031cd94:
        __unsupported_jumpkind_Ijk_NoDecode()
        while (true)
        {
LABEL_1031cd95:
            v21 = _ccall(10, 15, 0, 0, 0);
            if ((char)v21)
            {
                v22 = _ccall(8, 15, 0, 0, 0);
                if (!((char)v22))
                {
                    if (!(1))
                        goto LABEL_1031cd9a;
                    v23 = _ccall(10, 15, 0, 0, 0);
                    if (!((char)v23))
                    {
                        v24 = _ccall(0, 15, 0, 0, 0);
                        if ((char)v24)
                            break;
                        else
                            continue;
                    }
                    v25 = _ccall(8, 15, 0, 0, 0);
                    if ((char)v25)
                        goto LABEL_1031cd92;
                    goto LABEL_1031cd9b;
                }
                __unsupported_jumpkind_Ijk_NoDecode()
                v26 = _ccall(8, 15, 0, 0, 0);
                if (!((char)v26))
                    goto LABEL_1031cd9b;
LABEL_1031cd92:
                if ((v27 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v27))
                    break;
            }
            else
            {
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_1031cd9a:
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_1031cd9b:
                v28 = a2;
                v14 = *(v28);
                v12 = *(v28);
                v11 = v28;
                v29 = _ccall(15, 0, 0, 0);
                v12 = v29 | 0x202 | v30 * 0x200000 & 0x200000 | v31 * 0x40000 & 0x40000;
                v9 = *(v28);
                v7 = v10;
                v6 = v8;
                v5 = &v12;
                v3 = &v15;
                v2 = v4;
                v0 = v1;
                if (!(1))
                    goto LABEL_1031cdcb;
LABEL_1031cdcb:
                for (; (v32 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v32 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
                a2 += 1;
                sub_1034fef0(v14);
            }
        }
    }
}
```

## `sub_1031cd88` `0x1031cd88`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1031cd88(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1031cdc6` `0x1031cdc6`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1031cdc6(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1031cdcd` `0x1031cdcd`

_3 bytes. (leaf/helper — see body)_

```c
void sub_1031cdcd(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1031cdff` `0x1031cdff`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1031cdff(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1031ce0f` `0x1031ce0f`

_136 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    char padding_0[1435095125];
    char field_5589d055;
} struct_2;

int sub_1031ce0f(void)
{
    unsigned int v19;  // ebp
    struct_2 *idx;  // ebx
    unsigned int v7;  // [bp-0x4]
    unsigned int v9;  // [bp+0xfffcc]
    unsigned int v10;  // [bp+0xfffd0]

    v19 = /* unsupported instruction */ - 0;
    idx->field_5589d055 = idx->field_5589d055 >> 1 | idx->field_5589d055 * 128;
    v9 = v10;
    v7 = 0;
    sub_1031ce33();
    return;
}
```

## `sub_1031ce33` `0x1031ce33`

_56 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1031ce33(unsigned int a0, unsigned int *a1)
{
    unsigned int v0;  // [bp+0x0]
    unsigned int v2;  // [bp+0xfffcc]
    unsigned int v3;  // [bp+0x100000]
    unsigned int *v4;  // [bp+0x10000c]

    v4 = sub_1031cc30(v4, v3, a1, v0);
    if (!v4)
    {
        return 0;
    }
    else if (v2)
    {
        v3 += v2;
    }
}
```

## `sub_1031cebf` `0x1031cebf`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1031cebf(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1031ced3` `0x1031ced3`

_105 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[56];
    unsigned int field_38;
} struct_0;

extern char g_deadc0d5;

int sub_1031ced3(void)
{
    void* v13;  // ebp
    struct_0 *v14;  // edx
    unsigned int v15;  // eax
    void* v16;  // ecx
    unsigned int v17;  // 4156
    unsigned long long v18;  // 4157
    unsigned long v19;  // 4161
    unsigned int v20;  // 4110
    unsigned int v0;  // [bp-0x4]
    unsigned int v1;  // [bp+0x0]
    unsigned int v2;  // [bp+0x0]
    void* v3;  // [bp+0x4], Other Possible Types: unsigned int
    char *v4;  // [bp+0x8], Other Possible Types: void*
    unsigned int v5;  // [bp+0xc]
    struct_0 *v6;  // [bp+0x10]
    unsigned int v7;  // [bp+0x10]
    void* v8;  // [bp+0x14]
    unsigned int v9;  // [bp+0x18]
    unsigned int v10;  // [bp+0x1c]
    unsigned int v11;  // [bp+0x20]
    unsigned int v12;  // [bp+0x20]

    v13 = v4;
    v14 = (int)v13[24];
    v15 = v14->field_38;
    *((unsigned int *)&v13[8]) = v15;
    v11 = ~(~(v9));
    v10 = v15;
    v16 = ~(__buildin_bswap32(v11));
    v17 = _ccall(0, v12 & 2261, 0, 0);
    v18 = _ccall((unsigned int)g_deadc0d5, 1, v17, 1);
    g_deadc0d5 = v18;
    v19 = _ccall((int)v16[100], 1, (unsigned int)(v18 >> 32) & 2261, 4);
    *((unsigned int *)&v16[100]) = v19;
    v9 = 0xdeadc0de;
    v8 = v16;
    v6 = v14;
    v5 = v7;
    v4 = &v10;
    v3 = v13;
    v1 = v3;
    v0 = v2;
    if (!(1))
        goto LABEL_1031cf14;
LABEL_1031cf14:
    for (; (v20 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v20 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
    v10 = 4;
    v9 = 0x1000;
    sub_1031cf43();
    return;
}
```

## `sub_1031ced7` `0x1031ced7`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1031ced7(void)
{
}
```

## `sub_1031ced9` `0x1031ced9`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1031ced9(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1031cf0f` `0x1031cf0f`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1031cf0f(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1031cf16` `0x1031cf16`

_3 bytes. (leaf/helper — see body)_

```c
void sub_1031cf16(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1031cf43` `0x1031cf43`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1031cf43(void)
{
    unsigned int v2;  // ecx
    unsigned int v0;  // [bp-0x4]

    v0 = v2;
    sub_1031cf44();
    return;
}
```

## `sub_1031cf44` `0x1031cf44`

_672 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[2];
    unsigned short field_2;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b070;
extern unsigned int g_103a24dc;
extern unsigned int g_103a24e0;
extern unsigned int g_103a24e8;

int sub_1031cf44(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4)
{
    unsigned int v10;  // cc_op
    unsigned int v11;  // cc_dep1
    unsigned int v20;  // 4101
    unsigned int v21;  // 4101
    void* v22;  // edx
    void* v23;  // ebx
    void* v24;  // ebp
    void* v25;  // esi
    void* v26;  // edi
    void* v27;  // eax
    void* v28;  // ecx
    unsigned int v29;  // 4110
    unsigned int v12;  // cc_dep2
    unsigned int v30;  // id
    unsigned int v31;  // ac
    unsigned int v32;  // cc_op
    unsigned int v33;  // 4104
    void* v34;  // cc_dep1
    unsigned int v36;  // 4101
    struct_0 *v38;  // edx
    unsigned int v39;  // eax
    unsigned int v13;  // 4103
    unsigned int v40;  // ecx
    struct_0 *v41;  // cc_dep1
    unsigned int v42;  // 4101
    unsigned int v43;  // eax
    unsigned int v44;  // 4110
    unsigned int v45;  // id
    unsigned int v46;  // ac
    unsigned int v47;  // cc_op
    unsigned int v48;  // 4104
    unsigned int v14;  // 4101
    unsigned int v50;  // 4103
    unsigned int v51;  // 4101
    unsigned int v52;  // 4101
    unsigned int v53;  // 4101
    void* v54;  // ecx
    void* v55;  // ebp
    unsigned int v15;  // 4101
    unsigned int v65;  // 4101
    unsigned int v16;  // 4101
    unsigned int v17;  // 4101
    unsigned int v18;  // 4101
    unsigned int v19;  // 4101
    int v0;  // [bp-0x59]
    void* v1;  // [bp-0x8]
    void* v2;  // [bp-0x4]
    void* v3;  // [bp+0x0]
    void* v4;  // [bp+0x18], Other Possible Types: unsigned int

    while (true)
    {
        v13 = _ccall(10, v10, v11, v12, 0);
        if (!((char)v13) || (v14 = (unsigned int)_ccall(2, v10, v11, v12, 0), (char)v14))
            goto LABEL_1031cf7e;
        else
            goto LABEL_1031cf70;
LABEL_1031cf70:
        v15 = _ccall(8, v10, v11, v12, 0);
        if ((char)v15)
        {
            __unsupported_jumpkind_Ijk_NoDecode()
            v19 = _ccall(8, v10, v11, v12, 0);
            if (!((char)v19))
                goto LABEL_1031cf80;
            goto LABEL_1031cf77;
        }
        v10 = 15;
        v11 = 0;
        v12 = 0;
        if (!(1))
            goto LABEL_1031cf7f;
        v16 = _ccall(10, 15, 0, 0, 0);
        if (!((char)v16))
        {
            v17 = _ccall(0, 15, 0, 0, 0);
            if ((char)v17)
                break;
            continue;
        }
        v18 = _ccall(8, 15, 0, 0, 0);
        if (!((char)v18))
            goto LABEL_1031cf80;
LABEL_1031cf77:
        v20 = _ccall(4, v10, v11, v12, 0);
        if (!((char)v20) || (v21 = (unsigned int)_ccall(0, v10, v11, v12, 0), (char)v21))
            break;
    }
    __unsupported_jumpkind_Ijk_NoDecode()
LABEL_1031cf7e:
    __unsupported_jumpkind_Ijk_NoDecode()
LABEL_1031cf7f:
    __unsupported_jumpkind_Ijk_NoDecode()
LABEL_1031cf80:
    v22 = *((unsigned int *)(&v0 + 105));
    v23 = *((unsigned int *)(&v0 + 101));
    v24 = *((unsigned int *)(&v0 + 93));
    v25 = *((unsigned int *)(&v0 + 89));
    v26 = *((unsigned int *)(&v0 + 0x55));
    v27 = (int)v24[24];
    if ((int)v27[92] > 5)
    {
        v28 = (int)v24[24];
        if ((int)v28[0x88])
        {
            v4 = v27;
            if ((int)v28[0x88] >= 0)
                goto LABEL_1031cf9e;
LABEL_1031cf9e:
            v29 = _ccall(6, (int)v28[0x88], 0, 0);
            v4 = v29 | 0x202 | v30 * 0x200000 & 0x200000 | v31 * 0x40000 & 0x40000;
            a4 = v27;
            a3 = v28;
            a2 = v22;
            a1 = v23;
            a0 = &v4;
            v3 = v24;
            v2 = v25;
            v1 = v26;
            v32 = 6;
            v33 = _ccall(0, 6, v22, v22, 0);
            v34 = v22;
            if (!((char)v33))
            {
                if (!(1))
                    goto LABEL_1031cfab;
LABEL_1031cfab:
                v32 = 15;
                v34 = 0x3;
                v22 = NULL;
            }
            v36 = _ccall(2, v32, v34, v22, 0);
            if ((char)v36)
                goto LABEL_0x1031cfbc;
        }
    }
    if (!(int)v24[12])
        __unsupported_jumpkind_Ijk_NoDecode()
    a3 = (int)v24[12];
    sub_10350b50((int)v24[12], (int)v24[48], *((int *)((int)v24[24] + 60)));
    *((int *)&v24[32]) = (int)v24[40];
    v38 = (int)v24[36];
    v39 = v38->field_2 * 40 + (int)v24[32];
    *((unsigned int *)&v24[16]) = v39;
    v40 = (int)v24[32];
    if (v40 >= (int)v24[16])
    {
        v43 = (int)v24[12];
        if (v43 != (int)v24[20])
        {
            v4 = v43;
            if (v43 >= (int)v24[20])
                goto LABEL_1031d0af;
LABEL_1031d0af:
            v44 = _ccall(6, v43, (int)v24[20], 0);
            *((unsigned int *)&(&v0)[113]) = v44 | 0x202 | v45 * 0x200000 & 0x200000 | v46 * 0x40000 & 0x40000;
            *((unsigned int *)&(&v0)[109]) = v43;
            *((unsigned int *)&(&v0)[105]) = v40;
            *((struct_0 **)&(&v0)[101]) = v38;
            *((void* *)&(&v0)[97]) = v23;
            *((void* *)&(&v0)[93]) = &v0 - 113;
            *((void* *)&(&v0)[89]) = v24;
            *((void* *)&(&v0)[0x55]) = v25;
            *((void* *)&(&v0)[81]) = v26;
            v47 = 6;
            v48 = _ccall(0, 6, v38, v38, 0);
            v41 = v38;
            if (!((char)v48))
            {
                if (!(1))
                    goto LABEL_1031d0bc;
LABEL_1031d0bc:
                v47 = 15;
                v41 = 0x3;
                v38 = NULL;
            }
            v65 = _ccall(2, v47, v41, v38, 0);
            if ((char)v65)
                goto LABEL_0x1031d0cd;
        }
        else if ((char)sub_1031d430((int)v24[12], *((int *)((int)v24[24] + 104))))
        {
            *((int *)&v24[32]) = (int)v24[40];
            while (true)
            {
                if ((int)v24[32] < (int)v24[16])
                {
                    *((int *)&v24[84]) = *((int *)((int)v24[32] + 36));
                    *((char *)&v24[74]) = 0;
                    *((char *)&v24[89]) = 0;
                    *((char *)&v24[73]) = 0;
                    if (((int)v24[84] & 536870944))
                        *((char *)&v24[73]) = 1;
                    if (((int)v24[84] & 0x40000000))
                        *((char *)&v24[74]) = 1;
                    if (((int)v24[84] & 0x80000000))
                        *((char *)&v24[89]) = 1;
                    *((unsigned int *)&v24[72]) = 1;
                    if ((char)v24[73])
                    {
                        if ((char)v24[89])
                        {
                            *((unsigned int *)&v24[72]) = 64;
                        }
                        else if ((char)v24[74])
                        {
                            *((unsigned int *)&v24[72]) = 32;
                        }
                        else
                        {
                            *((unsigned int *)&v24[72]) = 16;
                        }
                    }
                    else
                    {
                        if ((char)v24[74])
                        {
                            if ((char)v24[89])
                                *((unsigned int *)&v24[72]) = 4;
                            else
                                *((unsigned int *)&v24[72]) = 2;
                        }
                    }
                    *((int *)&v24[88]) = (int)v24[12] + *((int *)((int)v24[32] + 12));
                    *((int *)&v24[80]) = *((int *)((int)v24[32] + 8));
                    *((int *)&(&v0)[93]) = (int)v24[72];
                    *((int *)&(&v0)[89]) = (int)v24[80];
                    *((int *)&(&v0)[0x55]) = (int)v24[88];
                    if (!g_1038b070(*((unsigned int *)(&v0 + 0x55)), *((unsigned int *)(&v0 + 89)), *((unsigned int *)(&v0 + 93)), *((unsigned int *)(&v0 + 97))))
                        g_103a24e8 = 4;
                    *((unsigned int *)&v24[32]) = (int)v24[32] + 40;
                }
                else
                {
                    g_103a24e0 = (int)v24[12] + *((int *)((int)v24[24] + 16));
                    *((int *)&v24[100]) = (int)v24[48];
                    sub_10350eb5((int)v24[100]);
                    g_103a24dc = (int)v24[12];
                }
            }
        }
    }
    *((unsigned int *)&(&v0)[113]) = v39;
    *((unsigned int *)&(&v0)[109]) = v40;
    *((struct_0 **)&(&v0)[105]) = v38;
    *((void* *)&(&v0)[101]) = v23;
    *((void* *)&(&v0)[97]) = &v0 - 117;
    *((void* *)&(&v0)[93]) = v24;
    *((void* *)&(&v0)[89]) = v25;
    *((void* *)&(&v0)[0x55]) = v26;
    v41 = NULL;
    v42 = _ccall(0, 15, 0, 0, 0);
    if ((char)v42)
    {
LABEL_1031d065:
        __unsupported_jumpkind_Ijk_NoDecode()
    }
    while (true)
    {
        v50 = _ccall(10, 15, v41, 0, 0);
        if (!((char)v50) || v41 < NULL)
            break;
        v51 = _ccall(8, 15, v41, 0, 0);
        if (!((char)v51))
        {
            v41 = NULL;
            __unsupported_jumpkind_Ijk_NoDecode()
            goto LABEL_1031d06b;
        }
        __unsupported_jumpkind_Ijk_NoDecode()
        v52 = _ccall(8, 15, v41, 0, 0);
        if (!((char)v52))
            goto LABEL_1031d06c;
        if (v41 || (v53 = (unsigned int)_ccall(0, 15, v41, 0, 0), (char)v53))
            goto LABEL_1031d065;
    }
    __unsupported_jumpkind_Ijk_NoDecode()
LABEL_1031d06b:
    __unsupported_jumpkind_Ijk_NoDecode()
LABEL_1031d06c:
    v27 = *((unsigned int *)(&v0 + 109));
    v54 = *((unsigned int *)(&v0 + 105));
    v55 = *((unsigned int *)(&v0 + 89));
}
```

## `sub_1031cf6d` `0x1031cf6d`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1031cf6d(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1031cfb5` `0x1031cfb5`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1031cfb5(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1031cfc9` `0x1031cfc9`

_36 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b074;

int sub_1031cfc9(void)
{
    void* v1;  // [bp+0x8]

    g_1038b074(0, (int)v1[8], 0x1000, 4);
    __unsupported_jumpkind_Ijk_NoDecode()
    __debugbreak();
}
```

## `sub_1031cfcd` `0x1031cfcd`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1031cfcd(void)
{
}
```

## `sub_1031cfcf` `0x1031cfcf`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1031cfcf(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1031d024` `0x1031d024`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1031d024(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1031d059` `0x1031d059`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1031d059(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1031d0c6` `0x1031d0c6`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1031d0c6(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1031d0da` `0x1031d0da`

_126 bytes. (leaf/helper — see body)_

```c
int sub_1031d0da(void)
{
    void* v7;  // ebp
    unsigned int v8;  // 4097
    unsigned int v17;  // 4205
    unsigned int v18;  // 4110
    unsigned int v9;  // edx
    unsigned int v10;  // 4108
    unsigned int v11;  // cc_dep1
    unsigned int v12;  // cc_dep2
    unsigned int v13;  // edx
    unsigned int v15[36];  // eax
    unsigned int v16;  // ecx
    void* v1;  // [bp+0x8]
    char *v2;  // [bp+0xc]
    unsigned int v3;  // [bp+0x14]
    unsigned int v4;  // [bp+0x18]
    unsigned int v5[36];  // [bp+0x1c]
    unsigned int v6;  // [bp+0x20]

    v7 = v1;
    v8 = v6;
    v9 = (int)v7[12];
    v10 = *((int *)((int)v7[24] + 0x88));
    v11 = v9;
    v12 = v10;
    v13 = v9 + v10;
    *((unsigned int *)&v7[60]) = v13;
    v15 = (int)v7[24];
    v16 = v15[35];
    *((unsigned int *)&v7[64]) = v16;
    v6 = v16;
    v5 = v15;
    v17 = _ccall(3, v11, v12, 0);
    v6 = v17 | 0x202 | ((char)(v8 >> 10) ? 4294967295 : 1) & 0x400 | ((char)(v8 >> 21) ? 1 : 0) * 0x200000 & 0x200000 | ((char)(v8 >> 18) ? 1 : 0) * 0x40000 & 0x40000;
    v4 = v6;
    v3 = v13;
    v2 = &v6;
    v1 = v7;
    if (!(1))
        goto LABEL_1031d138;
LABEL_1031d138:
    for (; (v18 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v18 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
    sub_1031d160();
    return;
}
```

## `sub_1031d0de` `0x1031d0de`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1031d0de(void)
{
}
```

## `sub_1031d0e0` `0x1031d0e0`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1031d0e0(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1031d100` `0x1031d100`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1031d100(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1031d133` `0x1031d133`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1031d133(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1031d13a` `0x1031d13a`

_3 bytes. (leaf/helper — see body)_

```c
void sub_1031d13a(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1031d160` `0x1031d160`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1031d160(void)
{
    int v2;  // edx
    int v1;  // [bp+0xfffc8]

    return sub_1031d168(v1, v2);
}
```

## `sub_1031d168` `0x1031d168`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1031d168(unsigned int a0, unsigned short a1)
{
    int v1;  // ecx
    int v0;  // [bp+0xffff8]

    sub_1031d2e0(v0, v1);
}
```

## `sub_1031d183` `0x1031d183`

_4 bytes. (leaf/helper — see body)_

```c
void sub_1031d183(void)
{
    unsigned int v1;  // cc_op
    unsigned int v2;  // cc_dep1
    unsigned int v3;  // cc_dep2
    unsigned int v4;  // cc_ndep
    unsigned int v5;  // 4101
    unsigned int v6;  // 4101

    v5 = _ccall(0, v1, v2, v3, v4);
    if ((char)v5)
        goto LABEL_0x1031d18c;
    v6 = _ccall(12, v1, v2, v3, v4);
    if ((char)v6)
        goto LABEL_0x1031d18a;
    else
        goto LABEL_0x1031d187;
}
```

## `sub_1031d189` `0x1031d189`

_7 bytes. (leaf/helper — see body)_

```c
void sub_1031d189(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1031d2e0` `0x1031d2e0`

_326 bytes. (leaf/helper — see body)_

```c
char sub_1031d2e0(unsigned int a0, unsigned int a1, void* a2, unsigned int a3)
{
    unsigned short *v0;  // [bp-0x34]
    unsigned short *v1;  // [bp-0x30]
    unsigned short v2;  // [bp-0x2c]
    unsigned short v3;  // [bp-0x28]
    unsigned short v4;  // [bp-0x24]
    unsigned int v5;  // [bp-0x20]
    unsigned int v6;  // [bp-0x1c]
    void* v7;  // [bp-0x18]
    unsigned int *v8;  // [bp-0x14]
    void* v9;  // [bp-0x10]
    unsigned int v10;  // [bp-0xc]
    void* iter;  // [bp-0x8]

    iter = a2;
    v9 = iter + a3;
    v10 = a0 - a1;
    if (a0 == a1)
        return 1;
    while (iter < v9)
    {
        v6 = *((int *)iter);
        v5 = (int)iter[4];
        v7 = iter + v5;
        if (v7 > v9)
            v7 = v9;
        iter += 8;
        v8 = v6 + a0;
        while (iter < v7)
        {
            v2 = *((short *)iter);
            iter += 2;
            v4 = (v2 & 0xf000) >> 12;
            v3 = v2 & 0xfff;
            if (v4 == 1)
            {
                v1 = v3 + (char *)v8;
                *(v1) = *(v1) + (unsigned short)((v10 & 0xff00) >> 16);
            }
            else if (v4 == 2)
            {
                v0 = v3 + (char *)v8;
                *(v0) = *(v0) + (unsigned short)(v10 & 0xff);
            }
            else if (v4 == 3)
            {
                *((unsigned int *)((char *)v8 + v3)) = *((int *)((char *)v8 + v3)) + v10;
            }
            else if (v4)
            {
                return 0;
            }
        }
    }
    return 1;
}
```

## `sub_1031d430` `0x1031d430`

_398 bytes. refs "File \", ", error %d", "File \"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b078;
extern struct_0 *g_1038b07c;
extern struct_0 *g_1038b080;
extern struct_0 *g_1038b084;
extern unsigned int g_103a24e8;
extern int g_103a24f0;

char sub_1031d430(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0x28]
    unsigned short v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x20]
    int v3;  // [bp-0x1c]
    unsigned int *node;  // [bp-0x18]
    unsigned int *iter1;  // [bp-0x14]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int iter[5];  // [bp-0x8]

    v7 = 0x80000000;
    if (!a1)
        return 1;
    for (iter = a1 + a0; iter[3]; iter += 1)
    {
        v3 = iter[3] + a0;
        node = iter[0] + a0;
        iter1 = iter[4] + a0;
        g_1038b084(0);
        v6 = g_1038b080(v3);
        if (!v6)
        {
            g_103a24e8 = 3;
            sub_10353127(&g_103a24f0, "File \"%s\", error %d", v3, g_1038b07c());
            return 0;
        }
        for (; *(node); node += 1)
        {
            v2 = 0;
            if ((*(node) & 0x80000000))
            {
                v1 = *(node);
                v2 = g_1038b078(v6, v1);
                if (!v2)
                {
                    g_103a24e8 = 3;
                    sub_10353127(&g_103a24f0, "File \"%s\", ordinal %d", v3, v1);
                    return 0;
                }
            }
            else
            {
                v0 = *(node) + a0 + 2;
                v2 = g_1038b078(v6, v0);
                if (!v2)
                {
                    g_103a24e8 = 3;
                    sub_10353127(&g_103a24f0, "File \"%s\", function \"%s\"", v3, v0);
                    return 0;
                }
            }
            *(iter1) = v2;
            iter1 += 1;
        }
    }
    return 1;
}
```

## `sub_1031d5c0` `0x1031d5c0`

_185 bytes. (leaf/helper — see body)_

```c
unsigned int [31] sub_1031d5c0(unsigned int *a0, int a1)
{
    unsigned int v0[31];  // [bp-0x2c]
    unsigned int index;  // [bp-0x28]
    unsigned int v2[31];  // [bp-0x24]
    unsigned int v3[31];  // [bp-0x1c]
    unsigned int idx[31];  // [bp-0x18]
    unsigned int v5[31];  // [bp-0x14]
    unsigned int v6[31];  // [bp-0xc]
    unsigned int v7[31];  // [bp-0x8]

    v5 = (char *)a0 + a0[15];
    v3 = v5 + 2;
    idx = (char *)a0 + v5[30];
    v7 = (char *)a0 + idx[8];
    v2 = (char *)a0 + idx[9];
    v6 = (char *)a0 + idx[7];
    for (index = 0; index < idx[6]; index += 1)
    {
        v0 = (char *)a0 + v7[index];
        if (!sub_1035ddf8(v0, a1))
            return (char *)a0 + v6[*((short *)((char *)v2 + 2 * index))];
    }
    return NULL;
}
```

## `sub_1031d680` `0x1031d680`

_2108 bytes. refs "%X::DA%08X", "RN%08X", "%08X"_

```c
typedef struct struct_16 {
    char field_0;
} struct_16;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern unsigned int g_1038b02c;
extern struct_0 *g_1038b064;
extern struct_0 *g_1038b068;
extern struct_0 *g_1038b078;
extern struct_0 *g_1038b07c;
extern struct_0 *g_1038b080;
extern struct_0 *g_1038b088;
extern struct_0 *g_1038b08c;
extern struct_0 *g_1038b090;
extern struct_0 *g_1038b094;
extern struct_0 *g_1038b098;
extern struct_0 *g_1038b09c;
extern struct_0 *g_1038b1b4;
extern struct_0 *g_1038b1c0;
extern struct_0 *g_1038b1c8;
extern unsigned int g_1038b290;
extern unsigned int g_1038b2f8;
extern struct_0 *g_1038b300;
extern struct_0 *g_1038b304;
extern struct_0 *g_1038b340;
extern unsigned int g_1038c7f4;
extern unsigned int g_1038c800;
extern unsigned int g_1038c808;
extern unsigned int g_1038c814;
extern unsigned int g_1038c824;
extern unsigned int g_1038c834;
extern unsigned int g_1038c844;
extern unsigned int g_1038c868;
extern unsigned int g_1038e180;
extern unsigned int g_103a22a8;
extern unsigned int g_103a22b0;
extern struct_0 *g_103a22cc;
extern struct_0 *g_103a22d0;
extern char g_103a22d4;
extern unsigned int g_103a24dc;
extern struct_0 *g_103a24e0;
extern unsigned int g_103a24e8;
extern int g_103a24f0;
extern int g_103a2ad0;

int sub_1031d680(void)
{
    unsigned long v53;  // ldt
    unsigned long v54;  // gdt
    unsigned int v63;  // eax
    int v64;  // cc_dep1
    unsigned int v65;  // ecx
    unsigned int v66;  // 4155
    unsigned int v67;  // id
    unsigned int v68;  // ac
    unsigned int v69;  // edx
    unsigned int v70;  // ebx
    unsigned int v71;  // esi
    unsigned int v72;  // 4110
    unsigned short v55;  // fs
    unsigned int v73;  // esi
    unsigned int v75;  // eax
    unsigned int v76;  // 4101
    unsigned long v77;  // 4119
    unsigned int v78;  // ebx
    unsigned int v79;  // edi
    unsigned int v80;  // 4101
    unsigned int v81;  // 4103
    unsigned long v56;  // 4136
    unsigned int v82;  // 4101
    unsigned int v83;  // 4101
    unsigned int v84;  // 4101
    unsigned int v85;  // 4101
    unsigned int v86;  // 4101
    unsigned int v87;  // 4101
    unsigned long v89;  // 4114
    unsigned long v57;  // 4153
    unsigned int v62;  // eax
    unsigned int v0;  // [bp-0x874]
    char *v1;  // [bp-0x870], Other Possible Types: unsigned int
    char *v2;  // [bp-0x86c]
    struct_16 **v3;  // [bp-0x868], Other Possible Types: unsigned int
    unsigned int v4;  // [bp-0x864]
    unsigned int v5;  // [bp-0x860]
    unsigned int v6;  // [bp-0x85c]
    unsigned int v7;  // [bp-0x858]
    char *v8;  // [bp-0x854]
    unsigned int v9;  // [bp-0x80c]
    int v10;  // [bp-0x808]
    int v11;  // [bp-0x804]
    int v12;  // [bp-0x800]
    int v13;  // [bp-0x7fc]
    unsigned int v14;  // [bp-0x7f8]
    unsigned int v15;  // [bp-0x7f4]
    char v16;  // [bp-0x7f0]
    char v17;  // [bp-0x790]
    char v18;  // [bp-0x774]
    char v19;  // [bp-0x711]
    unsigned int v20;  // [bp-0x710]
    char v21;  // [bp-0x70c]
    unsigned int *v22;  // [bp-0x6ec]
    unsigned int v23;  // [bp-0x6e8]
    int v24;  // [bp-0x6d8]
    unsigned int v25;  // [bp-0x650]
    char v26;  // [bp-0x649]
    char v27;  // [bp-0x648]
    char v28;  // [bp-0x628]
    unsigned int v29;  // [bp-0x61c]
    char v30;  // [bp-0x4c0], Other Possible Types: unsigned int
    char v31;  // [bp-0x4b0]
    int j;  // [bp-0x44c]
    char v33;  // [bp-0x448]
    char v34;  // [bp-0x348]
    char v35;  // [bp-0x280]
    unsigned int v36;  // [bp-0x148]
    unsigned int v37;  // [bp-0x144]
    unsigned int v38;  // [bp-0x140]
    int i;  // [bp-0x13c]
    unsigned int v40;  // [bp-0x138]
    unsigned int v41;  // [bp-0x134]
    unsigned int v42;  // [bp-0x130]
    unsigned int v43;  // [bp-0x12c]
    char v44;  // [bp-0x128]
    unsigned int v45;  // [bp-0x1c]
    unsigned int iter;  // [bp-0x18]
    char v47;  // [bp-0x11]
    unsigned int v48;  // [bp-0x10]
    unsigned int v49;  // [bp-0xc]
    unsigned int v50;  // [bp-0x8], Other Possible Types: char
    char v51;  // [bp-0x4]

    v50 = 4294967295;
    v49 = sub_1036b73c;
    v56 = _ccall(v53, v54, (unsigned int)v55, 0);
    v48 = *((int *)v56);
    v45 = g_1038e180 ^ &v51;
    v9 = v45;
    v57 = _ccall(v53, v54, (unsigned int)v55, 0);
    *((unsigned int **)v57) = &v48;
    v47 = 1;
    sub_10319a60();
    iter = g_1038b02c;
    iter += 1;
    iter = g_1038b2f8;
    iter += 1;
    iter = g_1038b290;
    iter += 1;
    sub_103540b9(sub_1031c040);
    sub_10353127(&v44, "%X::DA%08X", g_1038b1c8(g_1038c844 ^ g_1038c800));
    if (g_1038b09c(2031617, 0, &v44))
        v47 = 0;
    if (v47 && (((char)g_1038c7f4 ^ (char)g_1038c834 ^ (char)g_1038c808) & 32))
    {
        sub_10353127(&v44, "RN%08X", g_1038c868 ^ g_1038c824 ^ g_1038c844);
        v42 = g_1038b098(0, 0, &v44);
        if (!v42 || g_1038b07c() != 183)
            goto LABEL_1031d8da;
        v41 = g_1038b094(v42, 30000);
        if (!v41 || v41 == 128)
        {
            sub_10353127(&v44, "%08X", g_1038c868 ^ g_1038c824 ^ g_1038c844);
            for (i = 0; i < 300 && (v40 = g_1038b300("MainClass", &v44), !v40); i += 1)
            {
                g_1038b1b4(100);
            }
            if (v40)
            {
                v36 = g_1038c868 ^ g_1038c824 ^ g_1038c844;
                v37 = sub_10352f20(g_103a22b0) + 1;
                v38 = g_103a22b0;
                g_1038b340(v40, 74, 0, &v36);
            }
            g_1038b090(v42);
        }
    }
    else
    {
LABEL_1031d8da:
        sub_1031df50(1);
        if (v47 && !(((char)g_1038c7f4 ^ (char)g_1038c834 ^ (char)g_1038c808) & 64) && !g_1038b068("_PAD64", &v34, 0x200))
        {
            sub_10350ad0(&v34, 35, 200);
            v35 = 0;
            for (j = 1; j <= 64; j += 1)
            {
                sub_10353127(&v33, "_PAD%d", j);
                g_1038b064(&v33, &v34);
            }
            if (((g_1038c7f4 ^ g_1038c834 ^ g_1038c808) & 16))
                goto LABEL_1031dc46;
            sub_1032c360(&v28);
            v50 = 0;
            v13 = sub_1031fd90(&v21);
            v12 = v13;
            v50 = 1;
            sub_103268f0(v12);
            v50 = 3;
            sub_1031a0e0(&v21);
            if (g_103a22a8 == 1 && !v29 && !(char)sub_103275b0())
                v29 = sub_10327150();
            sub_1032bd50(&v27, 0);
            v50 = 4;
            if ((char)sub_1031e350())
            {
                v20 = 0;
                v50 = 3;
                sub_1031a0e0(&v27);
                v50 = 0;
                sub_10319f00(&v31);
                v50 = 4294967295;
                sub_1031e250();
            }
            else
            {
                v11 = sub_1032c4f0(&v17);
                v10 = v11;
                v50 = 5;
                sub_1031e1d0(v10);
                v50 = 6;
                sub_1031e1d0(sub_1032e0e0(v10));
                v50 = 7;
                v19 = -(0 < sub_1032bf70(&v16, &v18, 0, 0, 0, 0, &g_103a2ad0, &g_103a2ad0, &v28, &v30)) + 1;
                v50 = 6;
                sub_10319f00(&v16);
                v50 = 5;
                sub_10319f00(&v18);
                v50 = 4;
                sub_1031a3a0(&v17);
                if (v19)
                {
                    g_103a24e8 = 6;
                    sub_10353127(&g_103a24f0, "(Location XEB, error code %d)", g_1038b07c());
                    v15 = 0;
                    v50 = 3;
                    sub_1031a0e0(&v27);
                    v50 = 0;
                    sub_10319f00(&v31);
                    v50 = 4294967295;
                    sub_1031e250();
                }
                else
                {
                    g_1038b304(v30, 10000);
                    v14 = 1;
                    v50 = 3;
                    sub_1031a0e0(&v27);
                    v50 = 0;
                    sub_10319f00(&v31);
                    v50 = 4294967295;
                    sub_1031e250();
                }
            }
        }
        else
        {
LABEL_1031dc46:
            if ((((char)g_1038c7f4 ^ (char)g_1038c834 ^ (char)g_1038c808) & 16))
            {
                sub_10353127(&v44, "%X::DA%08X", g_1038b1c8(g_1038c844 ^ g_1038c800));
                if (!g_1038b09c(2031617, 0, &v44))
                {
                    v62 = g_1038b08c(1);
                    g_1038b088(v62);
                    v26 = 0;
                    v25 = g_1038b080("Kernel32");
                    if (v25)
                    {
                        v22 = g_1038b078(v25, "IsDebuggerPresent");
                        if (v22 && v22())
                            v26 = 1;
                    }
                    v23 = 148;
                    v8 = &v23;
                    v63 = g_1038b1c0(&v23);
                    v64 = v24;
                    if (v24 == 2)
                    {
                        v7 = v65;
                        v6 = v63;
                        v66 = _ccall(6, v64, 2, 0);
                        v7 = v66 | 0x202 | v67 * 0x200000 & 0x200000 | v68 * 0x40000 & 0x40000;
                        v5 = v65;
                        v4 = v69;
                        v3 = v70;
                        v2 = &v7;
                        v1 = &v51;
                        v0 = v71;
                        if (!(1))
                            goto LABEL_1031dd4d;
LABEL_1031dd4d:
                        for (; (v72 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v72 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
                        if (0)
                            goto LABEL_0x1031dd69;
                        else
                            goto LABEL_0x1031dd46;
                    }
                    else
                    {
                        v76 = _ccall(0, 6, v64, 2, 0);
                        v77 = _ccall(v53, v54, (unsigned int)v55, 32);
                        v75 = *((int *)v77);
                        if (*((int *)v77))
                        {
                            v7 = v75;
                            v6 = v65;
                            v5 = v69;
                            v4 = v78;
                            v3 = &v8;
                            v2 = &v51;
                            v1 = v73;
                            v0 = v79;
                            v80 = _ccall(0, 15, 0, 0, 0);
                            if ((char)v80)
                                goto LABEL_1031ddbc;
                            else
                                goto LABEL_1031ddbd;
                            while (true)
                            {
LABEL_1031ddbc:
                                __unsupported_jumpkind_Ijk_NoDecode()
                                while (true)
                                {
LABEL_1031ddbd:
                                    v81 = _ccall(10, 15, 0, 0, 0);
                                    if (!((char)v81))
                                    {
                                        __unsupported_jumpkind_Ijk_NoDecode()
                                        __unsupported_jumpkind_Ijk_NoDecode()
                                        g_103a22d4 = 1;
                                    }
                                    v82 = _ccall(8, 15, 0, 0, 0);
                                    if (!((char)v82))
                                    {
                                        if (false)
                                        {
                                            __unsupported_jumpkind_Ijk_NoDecode()
                                            g_103a22d4 = 1;
                                        }
                                        v83 = _ccall(10, 15, 0, 0, 0);
                                        if (!((char)v83))
                                        {
                                            v84 = _ccall(0, 15, 0, 0, 0);
                                            if ((char)v84)
                                                break;
                                            else
                                                continue;
                                        }
                                        else
                                        {
                                            v85 = _ccall(8, 15, 0, 0, 0);
                                            if (!((char)v85))
                                                g_103a22d4 = 1;
                                        }
                                    }
                                    else
                                    {
                                        __unsupported_jumpkind_Ijk_NoDecode()
                                        v86 = _ccall(8, 15, 0, 0, 0);
                                        if (!((char)v86))
                                            g_103a22d4 = 1;
                                    }
                                    if ((v87 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v87))
                                        break;
                                }
                            }
                        }
                        else
                        {
                            if (v26)
                            {
                                sub_10353127(&v44, "%X:DAF", g_1038b1c8());
                                g_1038b098(0, 0, &v44);
                            }
                            else
                            {
                                sub_103244a0(!g_103a22a8); /* do not return */
                            }
                        }
                    }
                }
            }
            else if ((((char)g_1038c814 ^ (char)g_1038c834 ^ (char)g_1038c808) & 2))
            {
                sub_103118e0();
            }
            v43 = sub_1031c400();
            sub_1031df50(0);
            sub_103540b9(0);
            if (v43 == 1)
                v43 = g_103a22d0(&g_103a22a8);
            sub_103540b9(sub_1031c040);
            if (g_103a22cc)
                g_103a22cc();
            if (g_103a24e0)
                g_103a24e0(g_103a24dc, 0, 0);
        }
    }
    v89 = _ccall(v53, v54, (unsigned int)v55, 0);
    *((unsigned int *)v89) = v48;
    return sub_10351225();
}
```

## `sub_1031dbed` `0x1031dbed`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1031dbed(void)
{
}
```

## `sub_1031dd4f` `0x1031dd4f`

_3 bytes. (leaf/helper — see body)_

```c
void sub_1031dd4f(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1031dd85` `0x1031dd85`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1031dd85(void)
{
}
```

## `sub_1031dd8d` `0x1031dd8d`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1031dd8d(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1031ddb0` `0x1031ddb0`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1031ddb0(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1031ddd0` `0x1031ddd0`

_38 bytes. (leaf/helper — see body)_

```c
void sub_1031ddd0(unsigned int a0, unsigned int a1)
{
    unsigned int v11;  // cc_op
    unsigned int v12;  // cc_dep1
    unsigned int v21;  // edi
    unsigned int v23;  // 4104
    unsigned int v24;  // cc_dep1
    unsigned int v26;  // 4101
    unsigned int v13;  // cc_dep2
    unsigned int v14;  // cc_ndep
    unsigned int v15;  // 4104
    unsigned int v16;  // 4110
    unsigned int v17;  // id
    unsigned int v18;  // ac
    unsigned int v19;  // ebx
    unsigned int v20;  // esi
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    unsigned int v6;  // [bp-0x4]
    unsigned int v7;  // [bp+0x0]
    unsigned int v8;  // [bp+0x0]

    v15 = _ccall(2, v11, v12, v13, v14);
    if (!((char)v15))
        goto LABEL_1031ddd3;
LABEL_1031ddd3:
    v16 = _ccall(v11, v12, v13, v14);
    v7 = v16 | 0x202 | v17 * 0x200000 & 0x200000 | v18 * 0x40000 & 0x40000;
    v6 = v8;
    v5 = a0;
    v4 = a1;
    v3 = v19;
    v2 = /* unsupported instruction */;
    v1 = v20;
    v0 = v21;
    v23 = _ccall(0, 6, a1, a1, 0);
    v24 = a1;
    if (!((char)v23))
    {
        if (!(1))
            goto LABEL_1031dde0;
LABEL_1031dde0:
        if (0)
            goto LABEL_0x1031dd78;
        v26 = _ccall(2, 15, 3, 0, 0);
        if ((char)v26)
            goto LABEL_0x1031ddf1;
    }
    else
    {
        v26 = _ccall(2, 6, v24, a1, 0);
        if ((char)v26)
            goto LABEL_0x1031ddf1;
    }
}
```

