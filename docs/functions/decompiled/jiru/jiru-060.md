# elfbot.dll decompiled — jiru 0x10353326..0x103544a0

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10353326` `0x10353326`

_11 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    unsigned int field_8;
} struct_0;

extern char g_103945d0;

void sub_10353326(struct_0 *a0)
{
    *((char **)&a0->padding_0[0]) = &g_103945d0;
    sub_103532d2(a0);
    return;
}
```

## `sub_10353331` `0x10353331`

_28 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    unsigned int field_8;
} struct_0;

struct_0 * sub_10353331(struct_0 *a0, char a1)
{
    struct_0 *v0;  // [bp-0x8]

    sub_103532d2(a0);
    if ((a1 & 1))
    {
        v0 = a0;
        sub_10350abd();
    }
    return a0;
}
```

## `sub_1035334d` `0x1035334d`

_34 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    unsigned int field_8;
} struct_0;

extern char g_103945d0;

struct_0 * sub_1035334d(struct_0 *a0, char a1)
{
    struct_0 *v0;  // [bp-0x8]

    *((char **)&a0->padding_0[0]) = &g_103945d0;
    sub_103532d2(a0);
    if ((a1 & 1))
    {
        v0 = a0;
        sub_10350abd();
    }
    return a0;
}
```

## `sub_1035336f` `0x1035336f`

_123 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1035336f(void* a0, unsigned int a1, void* a2, unsigned int a3)
{
    unsigned int v0;  // [bp-0x10]

    if (!a3)
        return 0;
    if (!a0)
    {
        v0 = 22;
        *((unsigned int *)sub_103575e0()) = 22;
        sub_103535f2(0, 0, 0, 0, 0);
        return 22;
    }
    if (a2 && a1 >= a3)
    {
        sub_10350b50(a0, a2, a3);
    }
    else
    {
        sub_10350ad0(a0, 0, a1);
        if (!a2)
        {
            v0 = 22;
            *((unsigned int *)sub_103575e0()) = 22;
            sub_103535f2(0, 0, 0, 0, 0);
            return 22;
        }
        else if (a1 < a3)
        {
            v0 = 0x22;
            *((unsigned int *)sub_103575e0()) = 0x22;
            sub_103535f2(0, 0, 0, 0, 0);
            return 0x22;
        }
        else
        {
            v0 = 22;
            return 22;
        }
    }
    return 0;
}
```

## `sub_103533ea` `0x103533ea`

_74 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b200;
extern unsigned int g_103945d8;

int sub_103533ea(unsigned int a0, char *a1)
{
    unsigned int v8;  // esi
    unsigned int v9;  // edi
    unsigned int *i;  // esi
    char iter[4];  // edi
    unsigned int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x2c]
    unsigned int v2;  // [bp-0x28]
    char v3;  // [bp-0x24], Other Possible Types: unsigned long
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    char *v7;  // [bp-0x8]

    v2 = v8;
    v1 = v9;
    v0 = 8;
    i = &g_103945d8;
    for (iter = &v3; v0; i += 1)
    {
        v0 -= 1;
        *((unsigned int *)&iter[0]) = *(i);
        iter += 1;
    }
    v6 = a0;
    v7 = a1;
    if (a1 && (*(a1) & 8))
        v5 = 0x1994000;
    return g_1038b200(v3, *((unsigned int *)((void*)&v3 + 4)), v4, &v5);
}
```

## `sub_10353434` `0x10353434`

_42 bytes. (leaf/helper — see body)_

```c
extern int g_103a36c4;

void sub_10353434(void)
{
    unsigned int *v1;  // eax

    v1 = sub_10358b8c(g_103a36c4);
    if (v1)
        v1();
    sub_10359fbd(25);
    sub_10358620(0, 1);
    sub_1035852d();
    return;
}
```

## `sub_1035345e` `0x1035345e`

_133 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b07c;
extern struct_0 *g_1038b204;
extern int g_103a0f00;
extern unsigned int g_103a36c8;
extern unsigned int g_103a4cc0;

void sub_1035345e(void)
{
    int v5;  // esi
    int v6;  // eax
    unsigned int *v7;  // eax
    int v0;  // [bp-0xc]
    int v2;  // [bp+0xfffe8]
    unsigned int v3;  // [bp+0x100000]
    int v4;  // [bp+0x10000c]

    sub_1035b0cc(&g_103a0f00, 12);
    v5 = v4;
    if (!v5)
    {
        sub_1035b111();
        return;
    }
    if (g_103a4cc0 == 3)
    {
        sub_1035a599(4);
        v3 = 0;
        v6 = sub_1035a612(v5);
        v2 = v6;
        if (v6)
            sub_1035a63d(v6, v5);
        v3 = 4294967294;
        sub_103534b4();
        if (v2)
        {
            sub_1035b111();
            return;
        }
        v0 = v4;
    }
    else
    {
        v0 = v5;
    }
    if (!g_1038b204(g_103a36c8, 0))
    {
        v7 = sub_103575e0();
        *(v7) = sub_103575a5(g_1038b07c());
        sub_1035b111();
    }
    else
    {
        sub_1035b111();
    }
    return;
}
```

## `sub_103534b4` `0x103534b4`

_9 bytes. (leaf/helper — see body)_

```c
void sub_103534b4(void)
{
    sub_1035a4c1(4);
    return;
}
```

## `sub_103534ec` `0x103534ec`

_10 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a2fe8;

int sub_103534ec(unsigned int a0)
{
    g_103a2fe8 = a0;
    return a0;
}
```

## `sub_103534f6` `0x103534f6`

_252 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b0fc;
extern struct_0 *g_1038b208;
extern struct_0 *g_1038b20c;
extern struct_0 *g_1038b210;
extern struct_0 *g_1038b214;
extern unsigned int g_1038e180;

void sub_103534f6(void)
{
    unsigned int v27;  // ecx
    unsigned int v28;  // edx
    unsigned short v37;  // gs
    unsigned int v38;  // 4197
    unsigned int v39;  // id
    unsigned int v40;  // ac
    unsigned int v41;  // eax
    unsigned int v42;  // eax
    unsigned int v29;  // ebx
    unsigned int v30;  // esi
    unsigned int v31;  // edi
    unsigned short v32;  // ss
    unsigned short v33;  // cs
    unsigned short v34;  // ds
    unsigned short v35;  // es
    unsigned short v36;  // fs
    unsigned int v0;  // [bp-0x334]
    char v1;  // [bp-0x32c]
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
    unsigned int v12;  // [bp-0x234]
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
    v16 = v23;
    v15 = v27;
    v14 = v28;
    v13 = v29;
    v12 = v30;
    v11 = v31;
    v22 = v32;
    v19 = v33;
    v10 = v34;
    v9 = v35;
    v8 = v36;
    v7 = v37;
    v38 = _ccall(15, g_1038e180 ^ &v6, 0, 0);
    v0 = v38 | 0x202 | v39 * 0x200000 & 0x200000 | v40 * 0x40000 & 0x40000;
    v20 = v38 | 0x202 | v39 * 0x200000 & 0x200000 | v40 * 0x40000 & 0x40000;
    v21 = &v25;
    v5 = 65537;
    v18 = v25;
    v17 = v24;
    sub_10350ad0(&v1, 0, 80);
    v3 = &v1;
    v2 = v18;
    v4 = &v5;
    v41 = g_1038b214(v30, 3221225485);
    g_1038b210(0);
    if (!g_1038b20c(&v3) && !v41)
        sub_1035b125(2);
    v42 = g_1038b0fc(3221225485);
    g_1038b208(v42);
    sub_10351225();
    return;
}
```

## `sub_103535f2` `0x103535f2`

_36 bytes. (leaf/helper — see body)_

```c
extern int g_103a2fe8;

void sub_103535f2(void)
{
    char v0;  // [bp+0x0]

    sub_10358b8c(g_103a2fe8, &v0);
    if (!sub_10358b8c(g_103a2fe8, &v0))
    {
        sub_1035b125(2);
        sub_103534f6();
        return;
    }
    goto sub_10358b8c(g_103a2fe8, &v0);
}
```

## `sub_10353616` `0x10353616`

_16 bytes. (leaf/helper — see body)_

```c
void sub_10353616(void)
{
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]
    unsigned int v4;  // [bp-0x4]

    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    sub_103535f2();
    return;
}
```

## `sub_10353626` `0x10353626`

_91 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10353626(void* a0, unsigned int a1, void* a2, unsigned int a3)
{
    unsigned int v5;  // esi
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]

    if (!a3)
        return 0;
    if (!a0 || !a2)
    {
        v4 = 22;
        v5 = 22;
        *((unsigned int *)sub_103575e0()) = 22;
    }
    else if (a1 < a3)
    {
        v4 = 0x22;
        *((unsigned int *)sub_103575e0()) = 0x22;
        v5 = 0x22;
    }
    else
    {
        sub_10350ec0(a0, a2, a3);
        return 0;
    }
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    sub_103535f2();
    return v5;
}
```

## `sub_10353681` `0x10353681`

_38 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e1e4;
extern unsigned int g_1038e660;
extern char g_1038e748;

int sub_10353681(void)
{
    unsigned int v1[29];  // eax

    v1 = sub_10358da8();
    if (v1[27] != *((int *)&g_1038e748) && !(g_1038e660 & v1[28]))
        sub_10355e09();
    return g_1038e1e4;
}
```

## `sub_103536a7` `0x103536a7`

_130 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

extern unsigned int g_1038e660;
extern char g_1038e748;
extern char g_1038eb80;

struct_0 * sub_103536a7(struct_0 *idx, unsigned int *a1)
{
    void* idx1;  // eax
    void* index;  // eax
    int v0;  // [bp-0x4]

    idx->field_c = 0;
    if (a1)
    {
        idx->field_0 = *(a1);
        idx->field_4 = a1[1];
        return idx;
    }
    idx1 = sub_10358da8(v0);
    idx->field_8 = idx1;
    idx->field_0 = (int)idx1[108];
    idx->field_4 = (int)idx1[104];
    if (idx->field_0 != *((int *)&g_1038e748) && !(g_1038e660 & (int)idx1[112]))
        idx->field_0 = sub_10355e09();
    if (idx->field_4 != *((int *)&g_1038eb80) && !(g_1038e660 & (int)idx->field_8[112]))
        idx->field_4 = sub_1035b33b();
    index = idx->field_8;
    if (((char)index[112] & 2))
        return idx;
    *((unsigned int *)&index[112]) = (int)index[112] | 2;
    idx->field_c = 1;
    return idx;
}
```

## `sub_10353729` `0x10353729`

_660 bytes. (leaf/helper — see body)_

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

typedef struct struct_2 {
    char padding_0[172];
    int field_ac;
    char padding_b0[24];
    unsigned int field_c8;
} struct_2;

int sub_10353729(unsigned int *a0, char *a1, struct_0 **a2, int a3, unsigned int a4)
{
    unsigned int v18;  // ebx
    unsigned int v19;  // edi
    char v28[3];  // edi
    int v29;  // edi
    char v30;  // cl
    int v31;  // esi
    unsigned int v32;  // eax
    int v33;  // edx
    int v34;  // ecx
    unsigned int v35;  // eax
    char v20[3];  // edi
    unsigned int v21;  // esi
    struct_2 *v22;  // esi
    struct_2 *v23;  // esi
    char v24[3];  // edi
    unsigned int v25;  // eax
    char v26[3];  // edi
    char v27[3];  // edi
    unsigned int v0;  // [bp-0x58]
    unsigned int v1;  // [bp-0x54]
    unsigned int v2;  // [bp-0x50]
    unsigned int v3;  // [bp-0x4c]
    unsigned int v4;  // [bp-0x48]
    unsigned int v5;  // [bp-0x44]
    unsigned int v6;  // [bp-0x40]
    struct_0 v7;  // [bp-0x3c]
    struct_1 *idx;  // [bp-0x34]
    char v9;  // [bp-0x30]
    int v10;  // [bp-0x28]
    unsigned int v11;  // [bp-0x20]
    int v12;  // [bp-0x1c]
    int v13;  // [bp-0x14]
    int v14;  // [bp-0x14]
    int v15;  // [bp-0x10], Other Possible Types: unsigned int
    char iter[3];  // [bp-0xc]
    char v17;  // [bp-0x5]

    v6 = v18;
    v5 = v19;
    sub_103536a7(&v7, a0);
    v20 = a1;
    if (a2)
        *(a2) = v20;
    if (v20 && (!a3 || a3 >= 2 && a3 <= 36))
    {
        v4 = v21;
        v13 = 0;
        v15 = 0;
        v22 = (struct_2 *)v7;
        do
        {
            v23 = v22;
            v24 = &v20[1];
            v17 = v20[0];
            if (v23->field_ac > 1)
            {
                v25 = sub_1035b7ea(v17, 8, &v7);
                v23 = (struct_2 *)v7;
            }
            else
            {
                v25 = *((char *)(v23->field_c8 + v17 * 2)) & 8;
            }
        } while ((v20 = v24, v22 = v23, v25));
        iter = v24;
        if (v17 == 45)
        {
            a4 |= 2;
        }
        else
        {
            v26 = v24;
            if (v17 != 43)
                goto LABEL_103537f0;
        }
        v27 = &v24[1];
        iter = v27;
        v17 = v24[0];
        v26 = v27;
LABEL_103537f0:
        v3 = 16;
        if (a3)
        {
LABEL_1035381d:
            if (a3 == 16 && v17 == 48 && (v26[0] == 120 || v26[0] == 88))
            {
                v28 = &v26[1];
                v17 = v28[0];
                iter = &v28[1];
            }
        }
        else if (v17 != 48)
        {
            a3 = 10;
        }
        else if (v26[0] != 120 && v26[0] != 88)
        {
            a3 = 8;
        }
        else
        {
            a3 = 16;
            goto LABEL_1035381d;
        }
        v29 = a3;
        v10 = v29 >> 31;
        v11 = 0;
        v12 = sub_1035b8a0(-1, -1, v29, v10);
        while (true)
        {
            v30 = v17;
            if (((char)*((short *)(v23->field_c8 + v17 * 2)) & 4))
            {
                v31 = v30 - 48;
            }
            else
            {
                if (!(*((short *)(v23->field_c8 + v17 * 2)) & 259))
                    break;
                v32 = v30;
                if (v30 - 97 <= 25)
                    v32 -= 32;
                v31 = v32 - 55;
            }
            if (v31 >= a3)
                break;
            a4 |= 8;
            if (v15 >= v33 && (v15 > v33 || v13 >= v12) && (v13 != v12 || v15 != v33 || NULL >= v11 && (NULL > v11 || v31 > v34)))
            {
                a4 |= 4;
                if (!a2)
                    break;
            }
            else
            {
                v35 = sub_103544a0(v29, v10, v13, v15);
                v13 = v35 + v31;
                v15 = v33 + (v35 + v31 < v35);
            }
            iter = &iter[1];
            v17 = iter[0];
        }
        iter = &iter[1];
        if (!((char)a4 & 8))
        {
            if (a2)
                iter = a1;
            v13 = 0;
            v15 = 0;
        }
        else if (((char)a4 & 4) || !((char)a4 & 1) && (((char)a4 & 2) && (v15 > -0x80000000 || v15 >= -0x80000000 && v13 > NULL) || !((char)a4 & 2) && v15 >= 2147483647 && (v15 > 2147483647 || v13 > -1)))
        {
            *((unsigned int *)sub_103575e0()) = 0x22;
            if (((char)a4 & 1))
            {
                v13 = -1;
                v15 = -1;
            }
            else if (((char)a4 & 2))
            {
                v13 = 0;
                v15 = -0x80000000;
            }
            else
            {
                v13 = -1;
                v15 = 2147483647;
            }
        }
        if (a2)
            *(a2) = iter;
        v14 = v13;
        if (((char)a4 & 2))
        {
            v14 = -(v13);
            v15 = -(v15 + (0 < v13));
        }
        if (!v9)
            return v14;
        idx->field_70 = idx->field_70 & 4294967293;
        return v14;
    }
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    *((unsigned int *)sub_103575e0()) = 22;
    sub_103535f2();
    if (v9)
        idx->field_70 = idx->field_70 & 4294967293;
    return 0;
}
```

## `sub_103539bd` `0x103539bd`

_41 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

extern unsigned int g_1038e750;
extern unsigned int g_103a3058;

int sub_103539bd(char *a0, struct_0 **a1, int a2)
{
    unsigned int v0;  // [bp-0x18]

    v0 = (!g_103a3058 ? &g_1038e750 : 0);
    return sub_10353729((!g_103a3058 ? &g_1038e750 : 0), a0, a1, a2, 0);
}
```

## `sub_103539e6` `0x103539e6`

_42 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

extern unsigned int g_1038e750;
extern unsigned int g_103a3058;

int sub_103539e6(char *a0, struct_0 **a1, int a2)
{
    unsigned int v0;  // [bp-0x18]

    v0 = (!g_103a3058 ? &g_1038e750 : 0);
    return sub_10353729((!g_103a3058 ? &g_1038e750 : 0), a0, a1, a2, 1);
}
```

## `sub_10353a10` `0x10353a10`

_96 bytes. refs ";
    g_1038ec88 = ", ";
    g_1038ec8c = "_

```c
extern unsigned int g_1038ec80;
extern unsigned int g_1038ec84;
extern unsigned int g_1038ec88;
extern unsigned int g_1038ec8c;
extern unsigned int g_1038ec90;
extern unsigned int g_1038ec94;
extern unsigned int g_1038ec98;
extern unsigned int g_1038ec9c;
extern unsigned int g_1038eca0;
extern unsigned int g_1038eca4;

int sub_10353a10(void)
{
    g_1038ec80 = sub_1035c3c2;
    g_1038ec84 = "j";
    g_1038ec88 = "j";
    g_1038ec8c = "j";
    g_1038ec90 = sub_1035ba26;
    g_1038ec94 = sub_1035c3c2;
    g_1038ec98 = sub_1035c33c;
    g_1038ec9c = sub_1035ba3c;
    g_1038eca0 = sub_1035b9a6;
    g_1038eca4 = sub_1035b935;
    return sub_1035c3c2;
}
```

## `sub_10353a70` `0x10353a70`

_30 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a2ff4;

int sub_10353a70(unsigned int a0)
{
    sub_10353a10();
    g_103a2ff4 = sub_1035c467();
    if (!a0)
        return g_103a2ff4;
    return sub_1035c402();
}
```

## `sub_10353a90` `0x10353a90`

_173 bytes. (leaf/helper — see body)_

```c
void* sub_10353a90(void* a0, char a1, void* a2)
{
    void* v1;  // eax
    void* iter;  // edx
    char v8;  // cl
    void* v9;  // eax
    void* v10;  // eax
    void* v11;  // eax
    unsigned int v3;  // ebx
    void* v13;  // edx
    void* v4;  // eax
    unsigned int v5;  // edi
    void* v6;  // eax
    unsigned int v0;  // [bp-0x8]

    v1 = a2;
    if (!v1)
        return v1;
    iter = a0;
    v3 = a1;
    if (((char)iter & 3))
    {
        do
        {
            v4 = v1;
            iter += 1;
            if (!(*((char *)iter) ^ (char)v3))
                return iter - 1;
            v1 = v4 - 1;
            if (v4 == 0x1)
                return v1;
            v1 = v1;
            v13 = iter;
        } while (((char)iter & 3));
    }
    v9 = v1 - 4;
    if (v1 >= 0x4)
    {
        v0 = v5;
        v3 *= 0x1010101;
        do
        {
            v6 = v9;
            iter += 4;
            if (((*((int *)iter) ^ v3 ^ 4294967295 ^ 2130640639 + (*((int *)iter) ^ v3)) & 0x81010100))
            {
                v8 = (int)iter[4];
                if (!(v8 ^ (char)v3))
                {
                    return iter - 4;
                }
                else if (!v8)
                {
                    return iter - 3;
                }
                else if ((0 ^ (char)v3))
                {
                    return iter - 1;
                }
                else
                {
                    return iter - 2;
                }
            }
        } while ((v9 = v6 - 4, v9 = v9, v6 >= 0x4));
    }
    v10 = v9 + 4;
    if (v9 == 0xfffffffc)
        return v9 + 4;
    while (true)
    {
        v11 = v10;
        if (!(*((char *)iter) ^ (char)v3))
            return iter - 0;
        v10 = v11 - 1;
        iter += 1;
        if (v11 == 0x1)
            return v11 - 1;
    }
}
```

## `sub_10353b3d` `0x10353b3d`

_31 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10353b3d(unsigned int a0)
{
    unsigned int v1;  // esi
    int v0;  // [bp-0x4]

    v1 = *((int *)(sub_10358da8(v0) + 128));
    *((unsigned int *)(sub_10358da8(v0) + 128)) = a0;
    return v1;
}
```

## `sub_10353b5c` `0x10353b5c`

_185 bytes. (leaf/helper — see body)_

```c
extern int g_103a4cd4;
extern int g_103a4cd8;

int sub_10353b5c(int a0)
{
    unsigned int *v5;  // esi
    unsigned int *v6;  // edi
    unsigned int *v7;  // ebx
    unsigned int *v8;  // ebp
    unsigned int *v9;  // esi
    unsigned int *v11;  // eax
    unsigned int *v12;  // eax
    int v13;  // eax
    unsigned int *v14;  // eax
    int v0;  // [bp-0x14]
    int v1;  // [bp-0x10]
    int v2;  // [bp-0xc]
    int v3;  // [bp-0x8]
    unsigned int *v4;  // [bp-0x4], Other Possible Types: int

    v5 = sub_10358b8c(g_103a4cd8, v0, v1, v2, v3, v4);
    v4 = v5;
    v6 = sub_10358b8c(g_103a4cd4);
    if (v6 < v5 || !((v7 = (unsigned int *)(v6 - v5), v8 = v7 + 4, v8 >= 0x4)))
    {
LABEL_10353c0d:
        return 0;
    }
    v9 = sub_1035c490(v5);
    if (v9 < v8)
    {
        v11 = 0x800;
        if (v9 < 0x800)
            v11 = v9;
        v12 = v11 + v9;
        if ((v12 < v9 || (v13 = (int)sub_1035750a(v5, v12), !v13)) && !((v14 = v9 + 16, v14 >= v9 && (v13 = (int)sub_1035750a(v5, v14), v13))))
            goto LABEL_10353c0d;
        v6 = v13 + (v7 >> 2) * 4;
        g_103a4cd8 = sub_10358b15(v13);
    }
    *(v6) = sub_10358b15(a0);
    g_103a4cd4 = sub_10358b15(v6 + 1);
    return a0;
}
```

## `sub_10353c15` `0x10353c15`

_47 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a4cd4;
extern unsigned int g_103a4cd8;

unsigned int sub_10353c15(void)
{
    unsigned int *v2;  // esi
    int v0;  // [bp-0x4]

    v2 = sub_103574c2(32, 4, v0);
    g_103a4cd8 = sub_10358b15(v2);
    g_103a4cd4 = g_103a4cd8;
    if (v2)
    {
        *(v2) = 0;
        return 0;
    }
    return 24;
}
```

## `sub_10353c44` `0x10353c44`

_54 bytes. (leaf/helper — see body)_

```c
extern int g_103a0f20;

int sub_10353c44(void)
{
    int v1;  // [bp+0xfffe8]
    unsigned int v2;  // [bp+0x100000]
    int v3;  // [bp+0x10000c]

    sub_1035b0cc(&g_103a0f20, 12);
    sub_10353cf1(&g_103a0f20, 12);
    v2 = 0;
    v1 = sub_10353b5c(v3);
    v2 = 4294967294;
    sub_10353c7a();
    return sub_1035b111();
}
```

## `sub_10353c7a` `0x10353c7a`

_6 bytes. (leaf/helper — see body)_

```c
void sub_10353c7a(void)
{
    sub_10353cfa();
    return;
}
```

## `sub_10353c80` `0x10353c80`

_18 bytes. (leaf/helper — see body)_

```c
int sub_10353c80(unsigned int a0)
{
    unsigned int v0;  // [bp-0x4]

    v0 = a0;
    return -(-(0 < sub_10353c44())) - 1;
}
```

## `sub_10353c92` `0x10353c92`

_36 bytes. (leaf/helper — see body)_

```c
extern int g_1038e1f0;

void sub_10353c92(int a0)
{
    sub_1035a15d();
    sub_10359fbd(a0);
    sub_10358b8c(g_1038e1f0)(0xff);
    return;
}
```

## `sub_10353cb6` `0x10353cb6`

_38 bytes. refs "mscoree.dll", "CorExitProcess", "CorExitProcess"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;

void sub_10353cb6(void)
{
    unsigned int v1;  // eax
    unsigned int *v2;  // eax

    v1 = g_1038b050("mscoree.dll");
    if (!v1)
        return;
    v2 = g_1038b078(v1, "CorExitProcess");
    if (!v2)
        return;
    v2("CorExitProcess");
    return;
}
```

## `sub_10353cdc` `0x10353cdc`

_21 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b14c;

void sub_10353cdc(unsigned int a0)
{
    unsigned int v0;  // [bp-0x4]

    v0 = a0;
    sub_10353cb6();
    g_1038b14c(a0);
    __debugbreak();
}
```

## `sub_10353cf1` `0x10353cf1`

_9 bytes. (leaf/helper — see body)_

```c
void sub_10353cf1(void)
{
    sub_1035a599(8);
    return;
}
```

## `sub_10353cfa` `0x10353cfa`

_9 bytes. (leaf/helper — see body)_

```c
void sub_10353cfa(void)
{
    sub_1035a4c1(8);
    return;
}
```

## `sub_10353d03` `0x10353d03`

_24 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

int sub_10353d03(void)
{
    struct_0 **i;  // esi
    struct_0 **v0;  // [bp+0x4]

    for (; i < v0; i += 1)
    {
        if (*(i))
            (*(i))();
    }
    return;
}
```

## `sub_10353d1b` `0x10353d1b`

_32 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

unsigned int sub_10353d1b(struct_0 **i, struct_0 **a1)
{
    unsigned int v0;  // eax

    for (v0 = 0; i < a1; i += 1)
    {
        if (v0)
            return v0;
        if (*(i))
            v0 = (*(i))();
    }
    return v0;
}
```

## `sub_10353d3b` `0x10353d3b`

_55 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a2ffc;

unsigned int sub_10353d3b(unsigned int *a0)
{
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    int v5;  // [bp-0x4]

    if (a0 && g_103a2ffc)
    {
        *(a0) = g_103a2ffc;
        return 0;
    }
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    *((unsigned int *)sub_103575e0(v5)) = 22;
    sub_103535f2();
    v4 = 22;
    return v4;
}
```

## `sub_10353d72` `0x10353d72`

_60 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a2ffc;
extern unsigned int g_103a3008;

unsigned int sub_10353d72(unsigned int *a0)
{
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    int v5;  // [bp-0x4]

    if (a0 && g_103a2ffc)
    {
        *(a0) = g_103a3008;
        return 0;
    }
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    *((unsigned int *)sub_103575e0(v5)) = 22;
    sub_103535f2();
    v4 = 22;
    return v4;
}
```

## `sub_10353dae` `0x10353dae`

_146 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b370;
extern struct_0 *g_1038c204;
extern unsigned int *g_1038c208;
extern unsigned int *g_1038c228;
extern unsigned int g_103945f8;
extern struct_0 *g_103a4ce0;

unsigned int sub_10353dae(unsigned int a0)
{
    unsigned int v2;  // eax
    unsigned int v3;  // esi
    unsigned int v4;  // edi
    struct_0 **v5;  // esi
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp-0x4]

    if (g_103945f8 && sub_1035c600(&g_103945f8))
        sub_10353a70(a0);
    sub_1035c3e3();
    v2 = sub_10353d1b(&g_1038c208, &g_1038c228);
    if (v2)
        return v2;
    v1 = v3;
    v0 = v4;
    sub_10353c80(sub_1035c557);
    v5 = &g_1038b370;
    do
    {
        if (*(v5))
            (*(v5))();
    } while ((v5 += 4, v5 < &g_1038c204));
    if (!g_103a4ce0 || !sub_1035c600(&g_103a4ce0))
        return 0;
    g_103a4ce0(0, 2, 0);
    return 0;
}
```

## `sub_10353e40` `0x10353e40`

_208 bytes. (leaf/helper — see body)_

```c
extern int g_1038c244;
extern int g_1038c250;
extern int g_103a0f40;
extern char g_103a3034;
extern unsigned int g_103a3038;
extern unsigned int g_103a303c;
extern int g_103a4cd4;
extern int g_103a4cd8;

void sub_10353e40(void)
{
    int *v7;  // esi
    unsigned int v8;  // eax
    int *v1;  // [bp+0xfffe4]
    int *v2;  // [bp+0xfffe8]
    unsigned int v3;  // [bp+0x100000]
    unsigned int v4;  // [bp+0x10000c]
    unsigned int v5;  // [bp+0x100010]
    char v6;  // [bp+0x100014]

    sub_1035b0cc(&g_103a0f40, 16);
    sub_1035a599(8);
    v3 = 0;
    if (g_103a303c != 1)
    {
        g_103a3038 = 1;
        g_103a3034 = v6;
        if (!v5)
        {
            v2 = sub_10358b8c(g_103a4cd8);
            v7 = sub_10358b8c(g_103a4cd4);
            v1 = v7;
            if (v2)
            {
                while (true)
                {
                    v7 += 1;
                    v1 = v7;
                    if (v7 < v2)
                        break;
                    if (!*(v7) || (v8 = sub_10358b83(), *(v7) == sub_10358b83()))
                        continue;
                    sub_10358b8c(*(v7))();
                }
            }
            sub_10353d03(&g_1038c244);
        }
        sub_10353d03(&g_1038c250);
    }
    v3 = 4294967294;
    sub_10353f0d();
    if (*((int *)&v6))
    {
        sub_1035b111();
        return;
    }
    g_103a303c = 1;
    sub_1035a4c1(8);
    sub_10353cdc(v4); /* do not return */
}
```

## `sub_10353f0a` `0x10353f0a`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10353f0a(void)
{
    sub_10353f0d();
    return;
}
```

## `sub_10353f0d` `0x10353f0d`

_15 bytes. (leaf/helper — see body)_

```c
void sub_10353f0d(void)
{
    unsigned int v1;  // [bp+0x100014]

    if (v1)
        sub_1035a4c1(8);
    return;
}
```

## `sub_10353f22` `0x10353f22`

_17 bytes. (leaf/helper — see body)_

```c
void sub_10353f22(unsigned int a0)
{
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]
    unsigned int v2;  // [bp-0x4]

    v2 = 0;
    v1 = 0;
    v0 = a0;
    sub_10353e40();
    return;
}
```

## `sub_10353f33` `0x10353f33`

_17 bytes. (leaf/helper — see body)_

```c
void sub_10353f33(unsigned int a0)
{
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]
    unsigned int v2;  // [bp-0x4]

    v2 = 0;
    v1 = 1;
    v0 = a0;
    sub_10353e40();
    return;
}
```

## `sub_10353f44` `0x10353f44`

_15 bytes. (leaf/helper — see body)_

```c
void sub_10353f44(void)
{
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]
    unsigned int v2;  // [bp-0x4]

    v2 = 1;
    v1 = 0;
    v0 = 0;
    sub_10353e40();
    return;
}
```

## `sub_10353f53` `0x10353f53`

_76 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e1f0;

void sub_10353f53(void)
{
    unsigned int v2;  // esi
    int v0;  // [bp-0x4]

    v2 = sub_10358b83(v0);
    sub_103540af(v2);
    sub_1035ca49(v2);
    sub_103534ec(v2);
    sub_1035a2f0(v2);
    sub_1035ca3f(v2);
    sub_1035c835(v2);
    sub_1035c6bb(v2);
    sub_10359151(v2);
    g_1038e1f0 = sub_10358b15("j");
    return;
}
```

## `sub_10353f9f` `0x10353f9f`

_13 bytes. (leaf/helper — see body)_

```c
void sub_10353f9f(unsigned int a0)
{
    *((unsigned int *)(sub_10358da8() + 20)) = a0;
    return;
}
```

## `sub_10353fac` `0x10353fac`

_34 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

unsigned int sub_10353fac(void)
{
    struct_0 *idx;  // eax
    unsigned int v2;  // ecx

    idx = sub_10358da8();
    v2 = idx->field_14 * 0x343fd + 2531011;
    idx->field_14 = v2;
    return v2 >> 16 & 0x7fff;
}
```

## `sub_10353fd0` `0x10353fd0`

_178 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10353fd0(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    int v0;  // edi
    unsigned int i;  // eax
    unsigned int v10;  // edx
    unsigned int v11;  // 4169
    unsigned long v12;  // 4170
    unsigned int v13;  // eax
    unsigned long long v14;  // eax
    unsigned int v15;  // ecx
    unsigned int v16;  // edx
    unsigned int v17;  // eax
    unsigned int v2;  // eax
    unsigned int v3;  // eax
    unsigned int v4;  // edx
    unsigned int v5;  // ecx
    unsigned int v7;  // 4166
    unsigned long v8;  // 4167
    unsigned int v9;  // ecx

    v0 = 0;
    if (a1 < 0)
    {
        v0 = 1;
        a1 = -(a1) - (0 < a0);
        a0 = -(a0);
    }
    i = a3;
    if (a3 < 0)
    {
        i = -(i) - (0 < a2);
        a3 = i;
        a2 = -(a2);
    }
    if (!i)
    {
        v2 = (a1 % a2 CONCAT a0) % a2;
        if (v0 - 1 < 0)
            return (a1 % a2 CONCAT a0) % a2;
    }
    else
    {
        v3 = a0;
        v4 = a1;
        v5 = a2;
        do
        {
            v7 = _ccall(27, i >> 1, i, 0);
            v8 = _ccall(v5, 1, v7, 4);
            v11 = _ccall(27, v4 >> 1, v4, 0);
            v12 = _ccall(v3, 1, v11, 4);
            i >>= 1;
            v3 = v12;
            v4 >>= 1;
            v5 = v8;
        } while (i);
        v14 = (unsigned int)((v10 CONCAT v13) / v9);
        v15 = v14 * a3;
        v16 = v14 * a2 >> 32;
        v17 = v14 * a2;
        if (v16 + v15 < 0 || v16 + v15 > a1 || v16 + v15 >= a1 && v17 > a0)
            v17 -= a2;
        v2 = v17 - a0;
        if (v0 - 1 >= 0)
            return v17 - a0;
    }
    return -(v2);
}
```

## `sub_10354090` `0x10354090`

_31 bytes. (leaf/helper — see body)_

```c
int sub_10354090(void)
{
    char v1;  // cl

    if (v1 >= 64)
    {
        return;
    }
    else if (v1 >= 32)
    {
        return;
    }
    else if ((v1 & 31))
    {
        return;
    }
    else
    {
        return;
    }
}
```

## `sub_103540af` `0x103540af`

_10 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a3040;

int sub_103540af(unsigned int a0)
{
    g_103a3040 = a0;
    return a0;
}
```

## `sub_103540b9` `0x103540b9`

_49 bytes. (leaf/helper — see body)_

```c
extern int g_103a3040;

unsigned int sub_103540b9(int a0)
{
    unsigned int v1;  // eax
    int v0;  // [bp-0x4]

    sub_1035a599(4, v0);
    v1 = sub_10358b8c(g_103a3040);
    g_103a3040 = sub_10358b15(a0);
    sub_1035a4c1(4);
    return v1;
}
```

## `sub_103540ea` `0x103540ea`

_34 bytes. (leaf/helper — see body)_

```c
extern int g_103a3040;

unsigned int sub_103540ea(unsigned int a0)
{
    unsigned int *v0;  // eax

    v0 = sub_10358b8c(g_103a3040);
    if (!v0)
    {
        return 0;
    }
    else if (v0(a0))
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
```

## `sub_1035410c` `0x1035410c`

_60 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b148;

unsigned int sub_1035410c(unsigned int a0, unsigned int a1, unsigned int *a2)
{
    unsigned int v2;  // eax
    unsigned int v3;  // edx
    unsigned int v0;  // [bp-0xc]
    char v1;  // [bp+0x0]

    v0 = a0;
    g_1038b148(&v0, a0, a0, &v1);
    v2 = sub_10354870(a0 + 0x2ac18000, a0 - 27111903 + (a0 + 0x2ac18000 < a0), 10000000, 0);
    if (a2)
    {
        *(a2) = v2;
        a2[1] = v3;
    }
    return v2;
}
```

## `sub_10354150` `0x10354150`

_431 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    char field_4;
} struct_0;

extern unsigned int g_1038e180;
extern unsigned int g_10395088;

unsigned int sub_10354150(struct_0 *a0, void* a1, unsigned int a2)
{
    void* idx;  // ebx
    unsigned int v7;  // esi
    int v16;  // eax
    unsigned int v17;  // 4101
    void* v18;  // eax
    void* v8;  // edi
    int v9;  // edi
    int v10;  // esi
    int v11;  // ebx
    int v12;  // ebp
    unsigned int v13;  // eax
    unsigned int v14[7];  // ebx
    unsigned int v15;  // eax
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    struct_0 *v3;  // [bp-0x8]
    unsigned int v4;  // [bp-0x4]
    void* v5;  // [bp+0x0]

    idx = a1;
    v7 = (int)idx[8] ^ g_1038e180;
    *((char *)&v0 + 3) = 0;
    v2 = 1;
    v8 = idx + 16;
    if (*((int *)v7) != -2)
        sub_10351225(v9, v10, /* unsupported instruction */, v11);
    sub_10351225(v9, v10, /* unsupported instruction */, v11);
    if (!(a0->field_4 & 0x66))
    {
        v12 = (int)idx[12];
        v3 = a0;
        v4 = a2;
        *((struct_0 ***)&idx[4]) = &v3;
        if (v12 == -2)
            return v0;
        do
        {
            v13 = v12 * 3;
            v14 = v7 + v13 * 4 + 16;
            v15 = v14[0];
            v1 = v14[0];
            if (!*((int *)(v7 + v13 * 4 + 20)))
                continue;
            v16 = sub_1035cc1a();
            *((char *)&v0 + 3) = 1;
            if (v16 >= 0)
            {
                v17 = _ccall(14, 15, v16, 0, 0);
                if ((char)v17)
                {
                    v15 = v1;
                }
                else
                {
                    if (a0->field_0 == 3765269347 && g_10395088 && sub_1035c600(&g_10395088))
                        sub_10357a83(a0, 1);
                    sub_1035cc4a();
                    v18 = a1;
                    if ((int)v18[12] != v12)
                    {
                        sub_1035cc64(v8, &g_1038e180);
                        v18 = v5;
                    }
                    *((int *)&v18[12]) = v11;
                    if (*((int *)v7) != -2)
                        sub_10351225();
                    sub_10351225();
                    sub_10360565(1);
                    goto v14[2];
                }
            }
            else
            {
                v2 = 0;
                goto LABEL_103541fb;
            }
        } while ((v12 = (int)v15, v15 != 4294967294));
        v0 = v0;
        if (!*((char *)((void*)&v0 + 3)))
            return v0;
    }
    else
    {
        if ((int)idx[12] == -2)
            return v0;
        sub_1035cc64(v8, &g_1038e180);
        v0 = v0;
    }
LABEL_103541fb:
    if (*((int *)v7) != -2)
        sub_10351225();
    sub_10351225();
    return v0;
}
```

## `sub_103542e6` `0x103542e6`

_186 bytes. (leaf/helper — see body)_

```c
extern int g_1038e180;
extern int g_103a0f60;

int sub_103542e6(void)
{
    char *v11;  // edi
    char *v12;  // esi
    int v13;  // eax
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v6;  // [bp+0xfffe8]
    unsigned int v7;  // [bp+0x100000]
    char *v8;  // [bp+0x10000c], Other Possible Types: int
    char *v9;  // [bp+0x100010]
    int v10;  // [bp+0x100014]

    sub_1035b0cc(&g_103a0f60, 12);
    v6 = 0;
    v11 = v8;
    if (!v11 || (v12 = v9, !v12 || !*(v12)))
    {
        *((unsigned int *)sub_103575e0()) = 22;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        sub_103535f2();
        goto LABEL_1035431d;
    }
    v13 = sub_1035d0bc();
    v8 = v13;
    if (!v13)
    {
        *((unsigned int *)sub_103575e0()) = 24;
        goto LABEL_1035431d;
    }
    else
    {
        v7 = 0;
        if (!*(v11))
        {
            *((unsigned int *)sub_103575e0()) = 22;
            sub_1035cb28(&g_1038e180, /* unsupported instruction */ - 16, -2);
LABEL_1035431d:
        }
        else
        {
            v6 = sub_1035ce1c(v11, v12, v10, v13);
            v7 = 4294967294;
            sub_103543a0();
        }
    }
    return sub_1035b111();
}
```

## `sub_103543a0` `0x103543a0`

_10 bytes. (leaf/helper — see body)_

```c
void sub_103543a0(void)
{
    int v1;  // [bp+0x10000c]

    sub_1035cdbc(v1);
    return;
}
```

## `sub_103543aa` `0x103543aa`

_19 bytes. (leaf/helper — see body)_

```c
int sub_103543aa(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]
    unsigned int v2;  // [bp-0x4]

    v2 = 64;
    v1 = a1;
    v0 = a0;
    return sub_103542e6();
}
```

## `sub_103543bd` `0x103543bd`

_188 bytes. (leaf/helper — see body)_

```c
extern int g_1038e180;
extern int g_103a0f80;

int sub_103543bd(void)
{
    unsigned short *v11;  // ebx
    unsigned short *v12;  // edi
    int v13;  // eax
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v6;  // [bp+0xfffe8]
    unsigned int v7;  // [bp+0x100000]
    unsigned short *v8;  // [bp+0x10000c], Other Possible Types: int
    unsigned short *v9;  // [bp+0x100010]
    int v10;  // [bp+0x100014]

    sub_1035b0cc(&g_103a0f80, 12);
    v6 = 0;
    v11 = v8;
    if (!v11 || (v12 = v9, !v12 || !*(v12)))
    {
        *((unsigned int *)sub_103575e0()) = 22;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        sub_103535f2();
        goto LABEL_103543f4;
    }
    v13 = sub_1035d0bc();
    v8 = v13;
    if (!v13)
    {
        *((unsigned int *)sub_103575e0()) = 24;
        goto LABEL_103543f4;
    }
    else
    {
        v7 = 0;
        if (!*(v11))
        {
            *((unsigned int *)sub_103575e0()) = 22;
            sub_1035cb28(&g_1038e180, /* unsupported instruction */ - 16, -2);
LABEL_103543f4:
        }
        else
        {
            v6 = sub_1035d1ec(v11, v12, v10, v13);
            v7 = 4294967294;
            sub_10354479();
        }
    }
    return sub_1035b111();
}
```

## `sub_10354479` `0x10354479`

_10 bytes. (leaf/helper — see body)_

```c
void sub_10354479(void)
{
    int v1;  // [bp+0x10000c]

    sub_1035cdbc(v1);
    return;
}
```

## `sub_10354483` `0x10354483`

_19 bytes. (leaf/helper — see body)_

```c
int sub_10354483(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]
    unsigned int v2;  // [bp-0x4]

    v2 = 64;
    v1 = a1;
    v0 = a0;
    return sub_103543bd();
}
```

## `sub_103544a0` `0x103544a0`

_52 bytes. (leaf/helper — see body)_

```c
int sub_103544a0(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    return a0 * a2;
}
```

