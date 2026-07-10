# elfbot.dll decompiled — jiru 0x10350008..0x10350eb5

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10350008` `0x10350008`

_47 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1ec;
extern char g_1038df94;
extern int g_103a2de8;
extern int g_103a2e48;

int sub_10350008(unsigned int a0)
{
    unsigned int v2;  // edi
    unsigned int v3;  // esi
    int i;  // esi
    unsigned int v0;  // [bp-0xc]

    if (g_1038b1ec(&g_1038df94, v2))
        return a0;
    v0 = v3;
    i = &g_103a2de8;
    do
    {
        sub_10350978(i);
        i += 24;
    } while (i < &g_103a2e48);
    return a0;
}
```

## `sub_10350037` `0x10350037`

_41 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1f0;
extern char g_1038df94;
extern int g_103a2de8;
extern int g_103a2e48;

void sub_10350037(void)
{
    unsigned int v2;  // esi
    int i;  // esi
    unsigned int v0;  // [bp-0x8]

    if (g_1038b1f0(&g_1038df94) >= 0)
        return;
    v0 = v2;
    i = &g_103a2de8;
    do
    {
        sub_10350983(i);
        i += 24;
    } while (i < &g_103a2e48);
    return;
}
```

## `sub_10350060` `0x10350060`

_33 bytes. (leaf/helper — see body)_

```c
extern char g_103a2de8;

unsigned int * sub_10350060(unsigned int *a0, unsigned int a1)
{
    unsigned int v1;  // eax
    int v0;  // [bp-0x4]

    v1 = a1 & 3;
    *(a0) = v1;
    sub_1035098e(&(&g_103a2de8)[24 * v1], v0);
    return a0;
}
```

## `sub_10350081` `0x10350081`

_18 bytes. (leaf/helper — see body)_

```c
extern char g_103a2de8;

int sub_10350081(unsigned int *a0)
{
    return sub_10350999(&(&g_103a2de8)[24 * *(a0)]);
}
```

## `sub_10350093` `0x10350093`

_21 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    struct struct_1 *field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[4];
    struct struct_0 *field_4;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

struct_2 ** sub_10350093(struct_0 *a0)
{
    struct_2 **v1;  // eax

    v1 = sub_10313110(a0->field_4);
    if (!v1)
        return v1;
    return *(v1)->field_0(1);
}
```

## `sub_103500a8` `0x103500a8`

_28 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

struct_0 ** sub_103500a8(struct_0 **a0)
{
    struct_0 **v0;  // eax

    if (!*(a0))
        return a0;
    v0 = sub_10313110(*(a0));
    if (!v0)
        return v0;
    return *(v0)->padding_0(1);
}
```

## `sub_103500c4` `0x103500c4`

_42 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a2e50;

int sub_103500c4(void)
{
    sub_10350060(&/* unsupported instruction */, 0);
    sub_103500a8(&g_103a2e50);
    g_103a2e50 = 0;
    return sub_10350081(&/* unsupported instruction */);
}
```

## `sub_103500ee` `0x103500ee`

_6 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a2e50;

int sub_103500ee(void)
{
    return g_103a2e50;
}
```

## `sub_103500f4` `0x103500f4`

_37 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a2e50;
extern char g_103a2e74;

int sub_103500f4(unsigned int a0)
{
    if (!g_103a2e74)
    {
        g_103a2e74 = 1;
        sub_103509a4(sub_103500c4);
    }
    g_103a2e50 = a0;
    return a0;
}
```

## `sub_10350119` `0x10350119`

_131 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    int field_8;
    unsigned int field_c;
} struct_0;

typedef struct struct_2 {
    struct struct_1 *field_0;
} struct_2;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_10350119(void)
{
    struct_0 *idx;  // edi
    unsigned int v4;  // esi
    struct_0 **v5;  // eax
    struct_2 **v6;  // eax
    unsigned int v1;  // [bp+0x100000]
    struct_0 *v2;  // [bp+0x10000c]

    sub_10355ad8(4);
    sub_10350060(/* unsupported instruction */ - 16, 0);
    idx = v2;
    v1 = 0;
    v4 = idx->field_c;
    while (true)
    {
        do
        {
            do
            {
                if (!v4)
                {
                    sub_1035345e(idx->field_8);
                    v1 = 4294967295;
                    sub_10350081(/* unsupported instruction */ - 16);
                    return sub_10355b41();
                }
            } while ((v4 -= 1, v5 = (struct_0 **)(idx->field_8 + v4 * 4), !*((int *)(idx->field_8 + v4 * 4))));
        } while ((v6 = (struct_2 **)sub_10313110(*(v5)), !v6));
        *(v6)->field_0(1);
    }
}
```

## `sub_10350179` `0x10350179`

_67 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
} struct_0;

extern struct_0 *g_103a2e4c;

int sub_10350179(void)
{
    struct_0 **v2;  // eax
    unsigned int v3;  // esi
    struct_0 **v4;  // esi
    unsigned int v0;  // [bp-0xc]

    sub_10350060(&/* unsupported instruction */, 0);
    v2 = g_103a2e4c;
    if (g_103a2e4c)
    {
        v0 = v3;
        do
        {
            v4 = v2;
            g_103a2e4c = *(v2);
            sub_10350093(v4);
            sub_10350abd(v4);
            v2 = g_103a2e4c;
        } while (g_103a2e4c);
    }
    return sub_10350081(&/* unsupported instruction */);
}
```

## `sub_103501bc` `0x103501bc`

_57 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a2e4c;

unsigned int [2] sub_103501bc(unsigned int a0)
{
    unsigned int v0[2];  // eax

    if (!g_103a2e4c)
        sub_103509a4(sub_10350179);
    v0 = sub_10350a53(8);
    if (v0)
    {
        v0[0] = g_103a2e4c;
        v0[1] = a0;
    }
    else
    {
        v0 = NULL;
    }
    g_103a2e4c = v0;
    return v0;
}
```

## `sub_103501f5` `0x103501f5`

_35 bytes. (leaf/helper — see body)_

```c
unsigned int [22] sub_103501f5(unsigned int *a0)
{
    if (a0[20] <= 0)
        return a0;
    return sub_10356943(0, (a0[21] < 16 ? a0 + 16 : a0[16]));
}
```

## `sub_10350218` `0x10350218`

_108 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
    char padding_8[12];
    char field_14;
} struct_0;

extern char g_10394430;

int sub_10350218(unsigned int a0)
{
    struct_0 *idx;  // ecx
    char v5;  // 4132
    struct_0 *v1;  // [bp+0xffff4]
    unsigned int v2;  // [bp+0x100000]
    char v3;  // [bp+0x10000c]

    sub_10355ad8(4);
    v1 = idx;
    idx->field_4 = 1;
    v2 = 0;
    memset(idx->padding_8, 0, 12);
    v5 = v3;
    *((char **)&idx->padding_0[0]) = &g_10394430;
    idx->field_14 = v5;
    sub_10314590(&idx[1].padding_0[3], "*");
    return sub_10355b41(4);
}
```

## `sub_10350261` `0x10350261`

_107 bytes. (leaf/helper — see body)_

```c
extern char g_1038fb68;
extern char g_10394430;

int sub_10350261(unsigned int a0)
{
    unsigned int *v5;  // ecx
    unsigned int *v0;  // [bp-0x8]
    int v1;  // [bp+0x0]
    unsigned int *v3;  // [bp+0xffff4]
    unsigned int v4;  // [bp+0x100000]

    sub_10355ad8(4);
    v3 = v5;
    *(v5) = &g_10394430;
    v0 = v5;
    v4 = 1;
    sub_10350119();
    sub_10314750(v5 + 6, 1, 0);
    *(v5) = &g_1038fb68;
    return sub_10355b41(4, v1);
}
```

## `sub_1035029e` `0x1035029e`

_28 bytes. (leaf/helper — see body)_

```c
int sub_1035029e(unsigned int a0, char a1)
{
    sub_10350261(a0);
    if ((a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_103502ba` `0x103502ba`

_199 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

extern unsigned int g_103a2e50;
extern unsigned int g_103a2e54;
extern unsigned int g_103a2e6c;

int sub_103502ba(void)
{
    unsigned int v4;  // ecx
    struct_0 *v5;  // esi
    unsigned int v0;  // [bp-0x8]
    unsigned int v2;  // [bp+0xffff0]
    char v3;  // [bp+0x100000], Other Possible Types: unsigned int

    sub_10355ad8(8);
    if (g_103a2e50)
        return sub_10355b41();
    sub_10350060(/* unsupported instruction */ - 16, 0);
    v3 &= g_103a2e50;
    if (!g_103a2e50)
    {
        v4 = sub_10350a53(52);
        v2 = v4;
        v3 = 1;
        if (v4)
        {
            v0 = g_103a2e50;
            v5 = sub_10350218(v4);
        }
        else
        {
            v5 = NULL;
        }
        v3 = 0;
        sub_103500f4(v5);
        v5->field_10 = 63;
        sub_10314720(&v5[1].padding_0[4], "C");
        g_103a2e54 = v5;
        sub_10313500(v5);
        g_103a2e6c = g_103a2e54;
    }
    v3 = 4294967295;
    sub_10350081(/* unsupported instruction */ - 16);
    return sub_10355b41();
}
```

## `sub_10350354` `0x10350354`

_74 bytes. (leaf/helper — see body)_

```c
extern int g_1038f8e4;

int sub_10350354(unsigned int a0)
{
    int v2;  // eax
    unsigned int v3;  // esi
    int v4;  // eax
    unsigned int v0;  // [bp-0x4]
    int v1;  // [bp+0x8]

    v2 = sub_10356943(0, 0);
    if (!v2)
        v2 = &g_1038f8e4;
    v0 = v3;
    sub_10314720(a0 + 60, v2);
    if (!v1 || (v4 = (int)sub_10356943(0, v1), !v4))
        v4 = "*";
    return sub_10314720(a0 + 88, v4);
}
```

## `sub_1035039e` `0x1035039e`

_98 bytes. refs "string too long"_

```c
extern char g_10390714;
extern int g_1039ce9c;

int sub_1035039e(void)
{
    unsigned int v1;  // [bp+0xfffb4]
    unsigned int v2;  // [bp+0x100000]

    sub_10355ad8(0x44);
    sub_10314590(/* unsupported instruction */ - 40, "string too long");
    v2 = 0;
    sub_1032d470(/* unsupported instruction */ - 80, /* unsupported instruction */ - 40);
    v1 = &g_10390714;
    sub_103533ea(/* unsupported instruction */ - 80, &g_1039ce9c);
    __debugbreak();
}
```

## `sub_103503dd` `0x103503dd`

_98 bytes. refs "invalid string position"_

```c
extern char g_10390658;
extern int g_103a0eb0;

int sub_103503dd(void)
{
    unsigned int v1;  // [bp+0xfffb4]
    unsigned int v2;  // [bp+0x100000]

    sub_10355ad8(0x44);
    sub_10314590(/* unsupported instruction */ - 40, "invalid string position");
    v2 = 0;
    sub_1032d470(/* unsupported instruction */ - 80, /* unsupported instruction */ - 40);
    v1 = &g_10390658;
    sub_103533ea(/* unsupported instruction */ - 80, &g_103a0eb0);
    __debugbreak();
}
```

## `sub_1035041c` `0x1035041c`

_271 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    int field_4;
    unsigned int field_8;
} struct_0;

int sub_1035041c(int a0, struct_0 *a1)
{
    int v11;  // eax
    unsigned int v12;  // ebx
    int v13;  // ebx
    unsigned int v14;  // edi
    unsigned int v15;  // eax
    unsigned int v16;  // eax
    int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    int v3;  // [bp-0x18]
    int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    int v6;  // [bp-0xc]
    char v7;  // [bp-0x8]
    char v8;  // [bp-0x7]
    char v9;  // [bp+0x9]
    char v10;  // [bp+0xa]

    if (!a1)
    {
        v5 = *((int *)(sub_1035745c(v3) + 8));
        v11 = sub_10357436();
    }
    else
    {
        v5 = a1->field_0;
        v11 = a1->field_4;
    }
    v4 = v11;
    if (!v5)
        return a0;
    v2 = v12;
    v13 = a0;
    v1 = v14;
    if (v13 < 0x100)
    {
        if (!a1)
        {
            if (sub_10356f10(v13))
                goto LABEL_10350493;
        }
        else
        {
            if ((*((char *)(a1->field_8 + v13 * 2)) & 1))
                goto LABEL_1035048f;
        }
LABEL_1035050c:
    }
    else
    {
LABEL_1035048f:
        if (!a1)
        {
LABEL_10350493:
            v6 = v13;
            v6 >>= 8;
            v15 = *((short *)(sub_10356e98() + (char)v6 * 2)) & 0x8000;
        }
        else
        {
            v6 = v13;
            v6 >>= 8;
            v15 = *((short *)(a1->field_8 + (v6 & 0xff) * 2)) >> 15 & 1;
        }
        if (v15)
        {
            v0 = 2;
            a1 = v6;
            v9 = v13;
            v10 = 0;
        }
        else
        {
            a1 = v13;
            v9 = 0;
            v0 = 1;
        }
        v16 = sub_10356e55(0, v5, 0x100, &a1, v0, &v7, 3, v4, 1);
        if (!v16)
            goto LABEL_1035050c;
        v13 = (v16 == 1 ? v7 : v7 * 0x100 | v8);
    }
    return v13;
}
```

## `sub_1035052b` `0x1035052b`

_91 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    int field_8;
    unsigned int field_c;
} struct_0;

struct_0 * sub_1035052b(struct_0 *idx)
{
    unsigned int v1;  // eax
    int v2;  // eax
    unsigned int v3;  // eax
    int v0;  // [bp-0x4]

    idx->field_0 = *((int *)(sub_1035745c(v0) + 4));
    idx->field_4 = sub_10357436(v0);
    v1 = sub_103574c2(0x100, 2);
    idx->field_8 = v1;
    if (!v1)
    {
        v3 = sub_10356e98();
        idx->field_c = 0;
        idx->field_8 = v3;
        return idx;
    }
    v2 = sub_10356e98(0x200);
    sub_10350b50(idx->field_8, v2);
    idx->field_c = 1;
    return idx;
}
```

## `sub_10350586` `0x10350586`

_276 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    int field_4;
    unsigned int field_8;
} struct_0;

int sub_10350586(int a0, struct_0 *a1)
{
    int v10;  // eax
    unsigned int v11;  // ebx
    int v12;  // ebx
    unsigned int v13;  // eax
    unsigned int v14;  // eax
    int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    int v2;  // [bp-0x18]
    int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    char v6;  // [bp-0x8]
    char v7;  // [bp-0x7]
    char v8;  // [bp+0x9]
    char v9;  // [bp+0xa]

    if (!a1)
    {
        v4 = *((int *)(sub_1035745c(v2) + 8));
        v10 = sub_10357436();
    }
    else
    {
        v4 = a1->field_0;
        v10 = a1->field_4;
    }
    v3 = v10;
    if (!v4)
        return a0 - 32;
    v1 = v11;
    v12 = a0;
    if (v12 < 0x100)
    {
        if (!a1)
        {
            if (sub_10356f88(v12))
                goto LABEL_103505ff;
        }
        else
        {
            if ((*((char *)(a1->field_8 + v12 * 2)) & 2))
                goto LABEL_103505fb;
        }
LABEL_1035067c:
    }
    else
    {
LABEL_103505fb:
        if (!a1)
        {
LABEL_103505ff:
            v5 = v12;
            v5 >>= 8;
            v13 = *((short *)(sub_10356e98() + (char)v5 * 2)) & 0x8000;
        }
        else
        {
            v5 = v12;
            v5 >>= 8;
            v13 = *((short *)(a1->field_8 + (v5 & 0xff) * 2)) >> 15 & 1;
        }
        if (v13)
        {
            v0 = 2;
            a1 = v5;
            v8 = v12;
            v9 = 0;
        }
        else
        {
            a1 = v12;
            v8 = 0;
            v0 = 1;
        }
        v14 = sub_10356e55(0, v4, 0x200, &a1, v0, &v6, 3, v3, 1);
        if (!v14)
            goto LABEL_1035067c;
        v12 = (v14 == 1 ? v6 : v6 * 0x100 | v7);
    }
    return v12;
}
```

## `sub_1035069a` `0x1035069a`

_406 bytes. refs "0123456789abcdefghijklmnopqrstuvwxyz", "0123456789abcdefghijklmnopqrstuvwxyz"_

```c
typedef struct struct_0 {
    char field_0;
    char field_1;
} struct_0;

extern char g_10394484;

unsigned int sub_1035069a(char *a0, struct_0 **a1, unsigned int a2, unsigned int *a3)
{
    unsigned int v8;  // ebx
    char v9[2];  // esi
    char v17;  // bl
    char v18[2];  // eax
    unsigned int v19;  // eax
    unsigned int v10;  // edi
    char v11[2];  // edi
    unsigned int v12;  // eax
    char v13[2];  // esi
    char iter[2];  // esi
    char v15[2];  // esi
    unsigned int j;  // eax
    unsigned int v0;  // [bp-0x24]
    char v1[2];  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    char v4[2];  // [bp-0x14]
    char v5[2];  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    char v7;  // [bp-0x5]

    if (a3)
        *(a3) = 0;
    v2 = v8;
    v1 = v9;
    v0 = v10;
    v11 = a0;
    v12 = v11[0];
    v13 = v11;
    while (true)
    {
        iter = v13;
        if (!sub_10357078(v12))
            break;
        v15 = &iter[1];
        v12 = v15[0];
        v13 = v15;
    }
    if (iter[0] != 45 && iter[0] != 43)
    {
        v7 = 43;
    }
    else
    {
        v7 = iter[0];
        iter = &iter[1];
    }
    if (a2 >= 0 && a2 != 1 && a2 <= 36)
    {
        if (a2 > 0)
        {
            if (a2 == 16 && iter[0] == 48 && (iter[1] == 120 || iter[1] == 88))
                goto LABEL_1035073b;
        }
        else
        {
            if (iter[0] != 48)
            {
                a2 = 10;
            }
            else
            {
                if (iter[1] != 120 && iter[1] != 88)
                {
                    a2 = 8;
                }
                else
                {
                    a2 = 16;
LABEL_1035073b:
                    iter += 1;
                }
            }
        }
        for (v5 = iter; iter[0] == 48; iter = &iter[1]);
        v6 = 0;
        v4 = iter;
        j = sub_10353a90("0123456789abcdefghijklmnopqrstuvwxyz", sub_1035773b(iter[0], a2));
        if (j)
        {
            do
            {
                v17 = (char)j - 92;
                v3 = v6;
                v6 = a2 * v3 + (char)j - 92;
                iter = &iter[1];
                j = sub_10353a90("0123456789abcdefghijklmnopqrstuvwxyz", sub_1035773b(iter[0], a2));
            } while (j);
        }
        else
        {
            v17 = *((char *)((void*)&a2 + 3));
        }
        if (v5 == iter)
        {
            if (a1)
                *(a1) = a0;
        }
        else
        {
            v18 = &iter[-1 * (&g_10394484)[a2]];
            if (v18 - v4 >= 0 && (v18 - v4 > 0 || (v19 = v6 - (int)(char)v17, v6 < v6 - (int)(char)v17 || (v6 - (int)(char)v17) / a2 != v3)))
            {
                *((unsigned int *)sub_103575e0()) = 0x22;
                if (a3)
                    *(a3) = 1;
                v6 = 4294967295;
                v7 = 43;
            }
            if (v7 == 45)
                v6 = -(v6);
            if (!a1)
                return v6;
            *(a1) = iter;
            return v6;
        }
    }
    else if (a1)
    {
        *(a1) = v11;
    }
    return 0;
}
```

## `sub_10350830` `0x10350830`

_20 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
} struct_0;

int sub_10350830(void)
{
    struct_0 *v2;  // eax
    int v0;  // [bp-0x4]

    v2 = sub_1035745c(v0);
    sub_10357436(v0);
    return v2->field_8;
}
```

## `sub_10350844` `0x10350844`

_163 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
    char field_1;
} struct_0;

unsigned int sub_10350844(char *a0, struct_0 **a1, unsigned int a2, unsigned int *a3)
{
    char v1[2];  // ebx
    unsigned int v2;  // eax
    char v3[2];  // esi
    char iter[2];  // esi
    char v5[2];  // esi
    unsigned int v6;  // eax
    char v0;  // [bp+0xb]

    if (!a1)
        a1 = &a0;
    v1 = a0;
    v2 = v1[0];
    v3 = v1;
    while (true)
    {
        iter = v3;
        if (!sub_10357078(v2))
            break;
        v5 = &iter[1];
        v2 = v5[0];
        v3 = v5;
    }
    if (iter[0] != 45 && iter[0] != 43)
    {
        v0 = 43;
    }
    else
    {
        v0 = iter[0];
        iter = &iter[1];
    }
    v6 = sub_1035069a(iter, a1, a2, a3);
    if (iter == *(a1))
        *(a1) = v1;
    if ((v1 != *(a1) || !v6) && (v0 != 43 || v6 <= 2147483647))
    {
        if (v0 != 45)
        {
            return v6;
        }
        else if (v6 <= 0x80000000)
        {
            return -(v6);
        }
    }
    *((unsigned int *)sub_103575e0()) = 0x22;
    if (a3)
        *(a3) = 1;
    return (unsigned int)((v0 == 45) + 2147483647);
}
```

## `sub_103508e7` `0x103508e7`

_32 bytes. (leaf/helper — see body)_

```c
void sub_103508e7(int a0, int a1, int a2, int a3)
{
    int v2;  // ecx
    unsigned int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    sub_10350907(a0, a1, a2, a3, v2, &v1);
    if (/* unsupported instruction */)
    {
        v0 = /* unsupported instruction */;
        /* unsupported instruction */
    }
    else
    {
        v0 = nan;
        /* unsupported instruction */
    }
    if (!/* unsupported instruction */)
    {
        /* unsupported instruction */
        /* unsupported instruction */
        return;
    }
    /* unsupported instruction */
    /* unsupported instruction */
    return;
}
```

## `sub_10350907` `0x10350907`

_103 bytes. (leaf/helper — see body)_

```c
int sub_10350907(int a0, unsigned int a1, int a2, int a3, int iter, unsigned int *a4)
{
    int v2;  // esi
    unsigned int v3;  // esi
    unsigned int v10;  // ftop
    unsigned int v11;  // cc_op
    int v12;  // cc_dep1
    unsigned int v13;  // cc_ndep
    unsigned int v15;  // 4104
    unsigned int v16;  // ftop
    unsigned int v17;  // ftop
    unsigned int v18;  // 4131
    unsigned int v4;  // ftop
    unsigned int v5;  // ftop
    unsigned int *v6;  // eax
    unsigned int v7;  // ftop
    unsigned int i;  // ftop
    unsigned int v9;  // ftop
    double v0;  // [bp-0xc], Other Possible Types: unsigned long
    char v1;  // [bp+0x0]

    v3 = *((int *)sub_103575e0(v2, a0, a0, &v1));
    *((unsigned int *)sub_103575e0(v2, a0, a0, &v1)) = 0;
    sub_1035787d(a2, a3);
    if (/* unsupported instruction */)
    {
        v0 = /* unsupported instruction */;
        /* unsupported instruction */
        v5 = v4 + 1;
    }
    else
    {
        v0 = (double)nan;
        /* unsupported instruction */
        v5 = v4 + 1;
    }
    *(a4) = *((int *)sub_103575e0());
    v6 = sub_103575e0();
    v7 = v5 - 1;
    if (/* unsupported instruction */)
    {
        i = v7 - 1;
        /* unsupported instruction */
        /* unsupported instruction */
    }
    else
    {
        i = v7 - 1;
        /* unsupported instruction */
        /* unsupported instruction */
    }
    for (*(v6) = v3; iter > 0; i = v10 + 1)
    {
        v9 = i - 1;
        if (/* unsupported instruction */)
        {
            v10 = v9 - 1;
            /* unsupported instruction */
            /* unsupported instruction */
        }
        else
        {
            v10 = v9 - 1;
            /* unsupported instruction */
            /* unsupported instruction */
        }
        iter -= 1;
        /* unsupported instruction */
        /* unsupported instruction */
        v0 = (/* unsupported instruction */ ? /* unsupported instruction */ : nan);
        /* unsupported instruction */
    }
    if (iter < 0)
    {
        v11 = 6;
        v12 = 0;
        v13 = 0;
        iter = -(iter);
        do
        {
            v15 = _ccall(v11, v12, iter, v13);
            v13 = v15;
            v11 = 21;
            v12 = iter - 1;
            iter = 0;
            iter -= 1;
            v16 = i - 1;
            if (/* unsupported instruction */)
            {
                v17 = v16 - 1;
                /* unsupported instruction */
                /* unsupported instruction */
            }
            else
            {
                v17 = v16 - 1;
                /* unsupported instruction */
                /* unsupported instruction */
            }
            /* unsupported instruction */
            /* unsupported instruction */
            v0 = (/* unsupported instruction */ ? /* unsupported instruction */ : nan);
            /* unsupported instruction */
            i = v17 + 1;
            v18 = _ccall(4, 21, v12, 0, v13);
        } while (!((char)v18));
    }
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    return iter;
}
```

## `sub_1035096e` `0x1035096e`

_5 bytes. (leaf/helper — see body)_

```c
int sub_1035096e(int a0)
{
    unsigned int v4;  // edx
    int v0;  // [bp+0x0]
    int v1;  // [bp+0x4]
    int v2;  // [bp+0x8]
    unsigned int *v3;  // [bp+0xc]

    return sub_10350907(a0, v4, v0, v1, v2, v3);
}
```

## `sub_10350973` `0x10350973`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10350973(void)
{
    sub_10357afc();
    return;
}
```

## `sub_10350978` `0x10350978`

_11 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1c4;

void sub_10350978(unsigned int a0)
{
    g_1038b1c4(a0);
    return;
}
```

## `sub_10350983` `0x10350983`

_11 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1f8;

void sub_10350983(unsigned int a0)
{
    g_1038b1f8(a0);
    return;
}
```

## `sub_1035098e` `0x1035098e`

_11 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1b8;

void sub_1035098e(unsigned int a0)
{
    g_1038b1b8(a0);
    return;
}
```

## `sub_10350999` `0x10350999`

_11 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1bc;

void sub_10350999(unsigned int a0)
{
    g_1038b1bc(a0);
    return;
}
```

## `sub_103509a4` `0x103509a4`

_32 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038dfcc;
extern unsigned int g_103a2e98;

unsigned int sub_103509a4(unsigned int a0)
{
    if (g_1038dfcc)
    {
        g_1038dfcc = g_1038dfcc - 1;
        (&g_103a2e98)[g_1038dfcc] = a0;
        return g_1038dfcc;
    }
    return sub_1035852d();
}
```

## `sub_103509c4` `0x103509c4`

_2 bytes. (leaf/helper — see body)_

```c
void sub_103509c4(void)
{
    sub_103509de();
    return;
}
```

## `sub_103509de` `0x103509de`

_35 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038dfcc;
extern unsigned int g_103a2e94[4];
extern unsigned int g_103a2e98[4];

unsigned int sub_103509de(void)
{
    unsigned int idx;  // eax
    unsigned int v2[4];  // ecx
    unsigned int i;  // eax

    for (; i < 10; i = g_1038dfcc)
    {
        v2 = g_103a2e98[idx];
        i = idx + 1;
        g_1038dfcc = i;
        if (v2)
            g_103a2e94[i]();
    }
    return i;
}
```

## `sub_103509e9` `0x103509e9`

_62 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    struct struct_1 *field_0;
    char padding_4[4];
    int field_8;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1f4;
extern int g_103a2ec8;
extern int g_103a2fc0;

void sub_103509e9(void)
{
    unsigned int v4;  // ebx
    unsigned int v5;  // esi
    unsigned int v6;  // edi
    int v7;  // ebx
    struct_1 *v8;  // esi
    struct_1 *v9;  // esi
    struct_1 *v10;  // edi
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]
    unsigned int v2;  // [bp-0x4]

    v2 = v4;
    v1 = v5;
    v0 = v6;
    v7 = &g_103a2ec8;
    do
    {
        v8 = g_1038b1f4(v7, 0);
        if (v8)
        {
            do
            {
                v9 = v8;
                v10 = v9->field_0;
                sub_10355ed2(v9->field_8);
                sub_1035345e(v9);
                v8 = v10;
            } while (v9->field_0);
        }
    } while ((v7 = (int)(v7 + 4), v7 < &g_103a2fc0));
    return;
}
```

## `sub_10350a27` `0x10350a27`

_19 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10350a27(void)
{
    return -(0 < sub_10353c80(sub_103509e9)) & 24;
}
```

## `sub_10350a3a` `0x10350a3a`

_25 bytes. (leaf/helper — see body)_

```c
extern int g_1038e178;
extern char g_1038fb70;

int sub_10350a3a(unsigned int a0)
{
    int v1;  // esi

    sub_10353262(&g_1038e178, 1, v1);
    *((char **)a0) = &g_1038fb70;
    return a0;
}
```

## `sub_10350a53` `0x10350a53`

_106 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038fb70;
extern int g_10399bb4;
extern char g_103a2fd8;
extern void g_103a2fe4;

void sub_10350a53(int a0)
{
    unsigned int v0;  // [bp-0x10]

    do
    {
        if (sub_10355a15(a0))
            return;
    } while (sub_103540ea(a0));
    if (!(g_103a2fe4 & 1))
    {
        *((unsigned int *)&g_103a2fe4) = *((int *)&g_103a2fe4) | 1;
        sub_10350a3a(&g_103a2fd8);
        sub_10353c80(sub_10373e47);
    }
    sub_1035327a(&g_103a2fd8);
    v0 = &g_1038fb70;
    sub_103533ea(&v0, &g_10399bb4);
    __debugbreak();
}
```

## `sub_10350abd` `0x10350abd`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10350abd(void)
{
    sub_1035345e();
    return;
}
```

## `sub_10350ad0` `0x10350ad0`

_122 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a4cc8;

void* sub_10350ad0(void* a0, char a1, unsigned int a2)
{
    unsigned int k;  // edx
    unsigned int v2;  // eax
    unsigned int v3;  // edi
    void* iter;  // edi
    void* v5;  // ecx
    unsigned int i;  // ecx
    unsigned int v8;  // ecx
    unsigned int v9;  // ecx
    unsigned int v0;  // [bp-0x4]

    k = a2;
    if (!k)
        return a0;
    v2 = a1;
    if (!a1 && k >= 0x100 && g_103a4cc8)
        return sub_10358798();
    v0 = v3;
    iter = a0;
    if (k >= 4)
    {
        v5 = -(a0);
        i = v5 & 3;
        if (((char)v5 & 3))
        {
            k -= i;
            do
            {
                *((char *)iter) = v2;
                iter += 1;
                i -= 1;
            } while (i != 1);
        }
        v2 *= 0x1010101;
        v8 = k;
        k &= 3;
        if ((v8 & 0xfffffffc))
        {
            for (v9 = v8 >> 2; v9; iter += 4)
            {
                v9 -= 1;
                *((unsigned int *)iter) = v2;
            }
            if (!k)
                return a0;
        }
    }
    do
    {
        *((char *)iter) = v2;
        iter += 1;
        k -= 1;
    } while (k != 1);
    return a0;
}
```

## `sub_10350b50` `0x10350b50`

_711 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_10350cc4[4];
extern unsigned int g_10350e60[4];
extern unsigned int g_103a4cc8;

void* sub_10350b50(void* a0, void* a1, unsigned int a2)
{
    void* v2;  // esi
    void* v3;  // edi
    unsigned int v12;  // ecx
    unsigned int v13;  // edx
    unsigned int v14;  // ecx
    void* iter;  // esi
    void* node;  // edi
    unsigned int v6;  // ecx
    unsigned int v7;  // edx
    unsigned int v8;  // ecx
    unsigned int v9;  // ecx
    void* iter1;  // edi
    void* iter2;  // esi
    void* v0;  // [bp-0x14]
    void* v1;  // [bp-0x10]

    v2 = a1;
    v3 = a0;
    if (v3 > v2 && v3 < a2 + v2)
    {
        iter = a2 + v2 - 4;
        node = a2 + v3 - 4;
        if (!((char)node & 3))
        {
            v6 = a2 >> 2;
            v7 = a2 & 3;
        }
        else
        {
            switch (a2)
            {
            case 0:
                break;
            case 1:
                goto LABEL_10350e78;
            case 2:
                goto LABEL_10350e88;
            case 3:
                goto LABEL_10350e9c;
            default:
                v8 = a2 - (node & 3);
                switch (node & 3)
                {
                case 1:
                    v7 = 3 & v8;
                    *((char *)&node[3]) = (char)iter[3];
                    iter -= 1;
                    v6 = v8 >> 2;
                    node -= 1;
                    break;
                case 2:
                    v7 = 3 & v8;
                    *((char *)&node[3]) = (char)iter[3];
                    v6 = v8 >> 2;
                    *((char *)&node[2]) = (char)iter[2];
                    iter -= 2;
                    node -= 2;
                    break;
                case 3:
                    v7 = 3 & v8;
                    *((char *)&node[3]) = (char)iter[3];
                    *((char *)&node[2]) = (char)iter[2];
                    v6 = v8 >> 2;
                    *((char *)&node[1]) = (char)iter[1];
                    iter -= 3;
                    node -= 3;
                    break;
                }
            }
        }
        switch (v6)
        {
        case 0:
            *((int *)(28 + (char *)node + 4 * v9)) = *((int *)(28 + (char *)iter + 4 * v9));
        case 1:
            *((int *)(24 + (char *)node + 4 * v9)) = *((int *)(24 + (char *)iter + 4 * v9));
            break;
        case 2:
            *((int *)(20 + (char *)node + 4 * v9)) = *((int *)(20 + (char *)iter + 4 * v9));
            goto LABEL_10350e2c;
        case 3:
LABEL_10350e2c:
            *((int *)(16 + (char *)node + 4 * v9)) = *((int *)(16 + (char *)iter + 4 * v9));
            goto LABEL_10350e34;
        case 4:
LABEL_10350e34:
            *((int *)(12 + (char *)node + 4 * v9)) = *((int *)(12 + (char *)iter + 4 * v9));
            goto LABEL_10350e3c;
        case 5:
LABEL_10350e3c:
            *((int *)(8 + (char *)node + 4 * v9)) = *((int *)(8 + (char *)iter + 4 * v9));
            goto LABEL_10350e44;
        case 6:
LABEL_10350e44:
            *((int *)(4 + (char *)node + 4 * v9)) = *((int *)(4 + (char *)iter + 4 * v9));
            goto LABEL_10350e57;
        case 7:
LABEL_10350e57:
            goto g_10350e60[v7];
        default:
            for (; v6; iter += 0xfffffffc)
            {
                v6 -= 1;
                *((int *)node) = *((int *)iter);
                node += 0xfffffffc;
            }
            switch (v7)
            {
            case 0:
                return a0;
            case 1:
LABEL_10350e78:
                *((char *)&node[3]) = (char)iter[3];
                return a0;
            case 2:
LABEL_10350e88:
                *((char *)&node[3]) = (char)iter[3];
                *((char *)&node[2]) = (char)iter[2];
                return a0;
            case 3:
LABEL_10350e9c:
                *((char *)&node[3]) = (char)iter[3];
                *((char *)&node[2]) = (char)iter[2];
                *((char *)&node[1]) = (char)iter[1];
                return a0;
            }
        }
    }
    iter1 = v3;
    iter2 = v2;
    if (a2 >= 0x100)
    {
        iter1 = v3;
        iter2 = v2;
        if (g_103a4cc8)
        {
            v1 = v3;
            v0 = v2;
            iter1 = v1;
            iter2 = v0;
            if ((v3 & 15) == (v2 & 15))
                return sub_103588c2();
        }
    }
    if (!((char)iter1 & 3))
    {
        v12 = a2 >> 2;
        v13 = a2 & 3;
    }
    else
    {
        switch (a2)
        {
        case 0:
            return a0;
        case 1:
            *((char *)iter1) = *((char *)iter2);
            return a0;
        case 2:
            *((char *)iter1) = *((char *)iter2);
            *((char *)&iter1[1]) = (char)iter2[1];
            return a0;
        case 3:
            *((char *)iter1) = *((char *)iter2);
            *((char *)&iter1[1]) = (char)iter2[1];
            *((char *)&iter1[2]) = (char)iter2[2];
            return a0;
        default:
            v14 = a2 - 4 + (iter1 & 3);
            switch (iter1 & 3)
            {
            case 0:
                break;
            case 1:
                v13 = 3 & v14;
                *((char *)iter1) = *((char *)iter2);
                *((char *)&iter1[1]) = (char)iter2[1];
                v12 = v14 >> 2;
                *((char *)&iter1[2]) = (char)iter2[2];
                iter2 += 3;
                iter1 += 3;
                break;
            case 2:
                v13 = 3 & v14;
                *((char *)iter1) = *((char *)iter2);
                v12 = v14 >> 2;
                *((char *)&iter1[1]) = (char)iter2[1];
                iter2 += 2;
                iter1 += 2;
                break;
            case 3:
                v13 = 3 & v14;
                *((char *)iter1) = *((char *)iter2);
                iter2 += 1;
                v12 = v14 >> 2;
                iter1 += 1;
                break;
            }
        }
    }
    switch (v12)
    {
    case 7:
        *((int *)(-28 + (char *)iter1 + 4 * v12)) = *((int *)(-28 + (char *)iter2 + 4 * v12));
    case 6:
        *((int *)(-24 + (char *)iter1 + 4 * v12)) = *((int *)(-24 + (char *)iter2 + 4 * v12));
        break;
    case 5:
        *((int *)(-20 + (char *)iter1 + 4 * v12)) = *((int *)(-20 + (char *)iter2 + 4 * v12));
        goto LABEL_10350c90;
    case 4:
LABEL_10350c90:
        *((int *)(-0x10 + (char *)iter1 + 4 * v12)) = *((int *)(-0x10 + (char *)iter2 + 4 * v12));
        goto LABEL_10350c98;
    case 3:
LABEL_10350c98:
        *((int *)(-12 + (char *)iter1 + 4 * v12)) = *((int *)(-12 + (char *)iter2 + 4 * v12));
        goto LABEL_10350ca0;
    case 2:
LABEL_10350ca0:
        *((int *)(-0x8 + (char *)iter1 + 4 * v12)) = *((int *)(-0x8 + (char *)iter2 + 4 * v12));
        goto LABEL_10350ca8;
    case 1:
LABEL_10350ca8:
        *((int *)(-0x4 + (char *)iter1 + 4 * v12)) = *((int *)(-0x4 + (char *)iter2 + 4 * v12));
        goto LABEL_10350cbb;
    case 0:
LABEL_10350cbb:
        goto g_10350cc4[v13];
    default:
        for (; v12; iter2 += 4)
        {
            v12 -= 1;
            *((int *)iter1) = *((int *)iter2);
            iter1 += 4;
        }
        goto g_10350cc4[v13];
    }
}
```

## `sub_10350bb3` `0x10350bb3`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10350bb3(void)
{
}
```

## `sub_10350bd3` `0x10350bd3`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10350bd3(void)
{
}
```

## `sub_10350c11` `0x10350c11`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10350c11(void)
{
}
```

## `sub_10350c37` `0x10350c37`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10350c37(void)
{
}
```

## `sub_10350cdb` `0x10350cdb`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10350cdb(void)
{
}
```

## `sub_10350ce7` `0x10350ce7`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10350ce7(void)
{
}
```

## `sub_10350cf9` `0x10350cf9`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10350cf9(void)
{
}
```

## `sub_10350d13` `0x10350d13`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10350d13(void)
{
}
```

## `sub_10350d3a` `0x10350d3a`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10350d3a(void)
{
}
```

## `sub_10350d45` `0x10350d45`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10350d45(void)
{
}
```

## `sub_10350d95` `0x10350d95`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10350d95(void)
{
}
```

## `sub_10350dbf` `0x10350dbf`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10350dbf(void)
{
}
```

## `sub_10350e77` `0x10350e77`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10350e77(void)
{
}
```

## `sub_10350e85` `0x10350e85`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10350e85(void)
{
}
```

## `sub_10350e9b` `0x10350e9b`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10350e9b(void)
{
}
```

## `sub_10350eb5` `0x10350eb5`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10350eb5(void)
{
    sub_10350abd();
    return;
}
```

