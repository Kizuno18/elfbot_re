# elfbot.dll decompiled — jiru 0x1035c84e..0x1035e223

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1035c84e` `0x1035c84e`

_52 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern unsigned int g_1038ed2c;

struct_0 * sub_1035c84e(unsigned int a0, unsigned int a1, struct_0 *a2)
{
    unsigned int v1;  // esi
    struct_0 *v2;  // eax
    struct_0 *iter;  // eax
    unsigned int v0;  // [bp-0x4]

    v0 = v1;
    v2 = a2;
    do
    {
        iter = v2;
    } while (iter->field_4 != a1 && (iter += 12, v2 = iter, v2 < g_1038ed2c * 12 + a2));
    if (iter < 12 * g_1038ed2c + (char *)a2 && iter->field_4 == a1)
        return iter;
    return NULL;
}
```

## `sub_1035c882` `0x1035c882`

_13 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a3868;

unsigned int sub_1035c882(void)
{
    unsigned int v0;  // [bp-0x4]

    v0 = g_103a3868;
    return sub_10358b8c();
}
```

## `sub_1035c88f` `0x1035c88f`

_411 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[92];
    struct struct_1 *field_5c;
    unsigned int field_60;
    unsigned int field_64;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern int g_1038ed20;
extern unsigned int g_1038ed24;
extern unsigned int g_103a12e0;
extern struct_0 g_103a3860;
extern struct_0 g_103a3864;
extern struct_0 g_103a3868;
extern struct_0 g_103a386c;

void sub_1035c88f(unsigned int a0)
{
    struct_0 *idx;  // edi
    unsigned int v14;  // ebx
    unsigned int v22;  // eax
    unsigned int *v23;  // eax, Other Possible Types: unsigned int
    unsigned int v24;  // eax
    unsigned int v25;  // edx
    unsigned int v15;  // eax
    unsigned int v16;  // eax
    unsigned int v17;  // eax
    struct_0 *v18;  // esi
    unsigned int v19;  // ecx
    unsigned int v20;  // eax
    unsigned int v21;  // eax
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp+0x0]
    unsigned int v5;  // [bp+0xfffd4]
    unsigned int v6;  // [bp+0xfffd8]
    struct_0 *v7;  // [bp+0xfffdc], Other Possible Types: unsigned int
    int i;  // [bp+0xfffe0]
    unsigned int *v9;  // [bp+0xfffe4]
    unsigned int v10;  // [bp+0xfffe8]
    unsigned int v11;  // [bp+0x100000]
    unsigned int v12;  // [bp+0x10000c]

    sub_1035b0cc(&g_103a12e0, 32);
    idx = NULL;
    v10 = 0;
    v7 = 0;
    v14 = v12;
    if (v14 > 11)
    {
        v21 = v14;
        v22 = v21 - 15;
        if (v21 != 15)
        {
            if (v22 != 6)
            {
                if (v22 == 7)
                    goto LABEL_1035c922;
LABEL_1035c906:
                *((unsigned int *)sub_103575e0()) = 22;
                v23 = 0;
                v3 = 0;
                v2 = 0;
                v1 = 0;
                v0 = 0;
                sub_103535f2();
                sub_1035b111(v23, &g_103a12e0, 32, v4);
                return;
            }
            v18 = &g_103a3864.padding_0[0];
            v23 = (unsigned int *)g_103a3864.padding_0;
        }
        else
        {
            v18 = &g_103a386c.padding_0[0];
            v23 = (unsigned int *)g_103a386c.padding_0;
        }
    }
    else if (v14 != 11)
    {
        v15 = v14;
        v23 = 2;
        v16 = v15 - 2;
        if (v15 != 2)
        {
            v17 = v16 - 2;
            if (v16 == 2)
                goto LABEL_1035c8c2;
            if (v17 != 2)
            {
                if (v17 != 4)
                    goto LABEL_1035c906;
                goto LABEL_1035c8c2;
            }
            else
            {
LABEL_1035c922:
                v18 = &g_103a3868.padding_0[0];
                v23 = (unsigned int *)g_103a3868.padding_0;
            }
        }
        else
        {
            v18 = &g_103a3860.padding_0[0];
            v23 = (unsigned int *)g_103a3860.padding_0;
        }
    }
    else
    {
LABEL_1035c8c2:
        idx = sub_10358d31();
        v7 = idx;
        if (idx)
        {
            v23 = &idx->field_5c->field_0;
            v18 = sub_1035c84e(v19, v14, idx->field_5c) + 1;
            v20 = *((int *)&v18->padding_0[0]);
            goto LABEL_1035c951;
        }
    }
    v10 = 1;
    v20 = sub_10358b8c();
LABEL_1035c951:
    v9 = v20;
    v24 = 0;
    if (v9 == 0x1)
    {
        sub_1035b111(v23, &g_103a12e0, 32, v4);
        return;
    }
    if (!v9)
    {
        v23 = 0x3;
        v24 = (unsigned int)sub_10353f33(3);
    }
    if (v10 != v24)
        sub_1035a599(v19, v25, v24);
    v11 = 0;
    if (v14 == 8 || v14 == 11 || v14 == 4)
    {
        v6 = idx->field_60;
        idx->field_60 = 0;
        if (v14 != 8)
            goto LABEL_1035c9db;
        v5 = idx->field_64;
        idx->field_64 = 140;
    }
    if (v14 == 8)
    {
        for (i = g_1038ed20; i < g_1038ed24 + g_1038ed20; i += 1)
        {
            idx->field_5c[2 + 3 * i].field_0 = 0;
        }
    }
    else
    {
LABEL_1035c9db:
        *((unsigned int *)&v18->padding_0[0]) = sub_10358b83();
    }
    v11 = 4294967294;
    sub_1035ca03();
    if (v14 == 8)
        v9(8, idx->field_64);
    else
        v9(v14);
    if (v14 == 8 || v14 == 11 || v14 == 4)
    {
        idx->field_60 = v6;
        if (v14 == 8)
            idx->field_64 = v5;
    }
    sub_1035b111(v23, &g_103a12e0, 32, v4);
    return;
}
```

## `sub_1035c9fd` `0x1035c9fd`

_6 bytes. (leaf/helper — see body)_

```c
void sub_1035c9fd(void)
{
    sub_1035ca03();
    return;
}
```

## `sub_1035ca03` `0x1035ca03`

_15 bytes. (leaf/helper — see body)_

```c
int sub_1035ca03(void)
{
    int v2;  // eax
    unsigned int v1;  // [bp+0xfffe8]

    if (!v1)
        return v2;
    return sub_1035a4c1(0);
}
```

## `sub_1035ca3f` `0x1035ca3f`

_10 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a3874;

int sub_1035ca3f(unsigned int a0)
{
    g_103a3874 = a0;
    return a0;
}
```

## `sub_1035ca49` `0x1035ca49`

_10 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a3878;

int sub_1035ca49(unsigned int a0)
{
    g_103a3878 = a0;
    return a0;
}
```

## `sub_1035ca53` `0x1035ca53`

_16 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1c4;

unsigned int sub_1035ca53(unsigned int a0)
{
    g_1038b1c4(a0);
    return 1;
}
```

## `sub_1035ca63` `0x1035ca63`

_150 bytes. refs "kernel32.dll", "InitializeCriticalSectionAndSpinCount", "InitializeCriticalSectionAndSpinCount"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern unsigned int g_103a1300;
extern unsigned int g_103a3878;

void sub_1035ca63(void)
{
    unsigned int *v10;  // esi
    unsigned int v11;  // eax
    unsigned int v0;  // [bp-0x1c]
    unsigned int *v1;  // [bp-0x18], Other Possible Types: unsigned int
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v5;  // [bp+0xfffe4]
    unsigned int v6;  // [bp+0xfffe8]
    unsigned int v7;  // [bp+0x100000]
    unsigned int v8;  // [bp+0x10000c]
    unsigned int v9;  // [bp+0x100010]

    sub_1035b0cc(&g_103a1300, 20);
    v6 = 0;
    v3 = g_103a3878;
    v10 = sub_10358b8c();
    if (!v10)
    {
        if (sub_10353d3b(/* unsupported instruction */ - 28))
        {
            v3 = 0;
            v2 = 0;
            v11 = 0;
            v1 = 0;
            v0 = 0;
            sub_103534f6();
        }
        if (v6 == 1 || (v11 = g_1038b050("kernel32.dll"), v11 = v11, !v11 || (v2 = (unsigned int)"InitializeCriticalSectionAndSpinCount", v10 = (unsigned int *)g_1038b078(v11, "InitializeCriticalSectionAndSpinCount"), v11 = v11, !v10)))
            v10 = sub_1035ca53;
        v1 = v10;
        g_103a3878 = sub_10358b15();
    }
    v7 = 0;
    v5 = v10(v8, v9);
    v7 = 4294967294;
    sub_1035b111(v8, v9, v11, v2);
    return;
}
```

## `sub_1035cae9` `0x1035cae9`

_23 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

int sub_1035cae9(void)
{
    unsigned int v3;  // eax
    unsigned int v1;  // [bp+0xfffe0]
    struct_0 **v2;  // [bp+0xffff0]

    v3 = *(v2)->field_0;
    v1 = v3;
    return v3 == 3221225495;
}
```

## `sub_1035cb00` `0x1035cb00`

_24 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b084;

void sub_1035cb00(void)
{
    unsigned int v0;  // [bp+0x0]
    unsigned int v2;  // [bp+0xfffe0]
    unsigned int v3;  // [bp+0xfffe4]
    void* v4;  // [bp+0xfffec]

    if (v2 == 3221225495)
    {
        *((unsigned int *)&v4[4]) = 8;
        g_1038b084(v0);
    }
    v3 = 0;
}
```

## `sub_1035cb28` `0x1035cb28`

_144 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
    unsigned int field_c;
} struct_0;

extern unsigned int g_1038e180;

struct_0 * sub_1035cb28(struct_0 *idx, unsigned int a1, unsigned int a2)
{
    unsigned int v11;  // ebx
    unsigned int v12;  // esi
    unsigned long v21;  // 4117
    unsigned int v13;  // edi
    unsigned long v14;  // ldt
    unsigned long v15;  // gdt
    unsigned short v16;  // fs
    unsigned long v17;  // 4163
    unsigned long v18;  // 4175
    unsigned int v19;  // esi
    unsigned int v20[6];  // ebx
    unsigned int v0;  // [bp-0x2c]
    unsigned int v1;  // [bp-0x28]
    unsigned int v2;  // [bp-0x24]
    unsigned int v3;  // [bp-0x20]
    unsigned int v4;  // [bp-0x1c]
    unsigned int v5;  // [bp-0x18]
    struct_0 *v6;  // [bp-0x14]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]
    unsigned int v9;  // [bp-0x4]
    unsigned int *v10;  // [bp+0x0]

    v9 = v11;
    v8 = v12;
    v7 = v13;
    v6 = idx;
    v5 = a1;
    v4 = a2;
    v3 = a2;
    v2 = sub_1035cbb8;
    v17 = _ccall(v14, v15, (unsigned int)v16, 0);
    v1 = *((int *)v17);
    v3 = g_1038e180 ^ &v1;
    v18 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int **)v18) = &v1;
    while (true)
    {
        v19 = idx->field_c;
        if (v19 == 4294967294 || a1 != 4294967294 && v19 <= a1)
            break;
        v20 = (idx->field_8 ^ *(v10)) + v19 * 12 + 16;
        idx->field_c = v20[0];
        if (v20[1])
            continue;
        sub_10360565(0x101);
        sub_10360584(0x101);
    }
    v21 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int *)v21) = v0;
    return idx;
}
```

## `sub_1035cbb8` `0x1035cbb8`

_33 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_1035cbb8(struct_0 *a0, unsigned int a1)
{
    if (!((char)a0->field_4 & 6))
        return 1;
    sub_10351225();
}
```

## `sub_1035cbd8` `0x1035cbd8`

_37 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
    unsigned int field_10;
    struct struct_0 *field_14;
} struct_0;

typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
    unsigned int field_c;
} struct_0;

int sub_1035cbd8(void)
{
    struct_0 *v3;  // eax
    unsigned int v1;  // [bp+0x8]
    unsigned int *v2;  // [bp+0x10]

    sub_1035cb28(v3->field_14, v3->field_10, v3->field_c);
    *(v2) = v1;
}
```

## `sub_1035cbfe` `0x1035cbfe`

_28 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
    unsigned int field_c;
} struct_0;

struct_0 * sub_1035cbfe(struct_0 *a0)
{
    return sub_1035cb28(a0[2].field_8, a0[1].field_8, a0[1].field_c);
}
```

## `sub_1035cc1a` `0x1035cc1a`

_23 bytes. (leaf/helper — see body)_

```c
int sub_1035cc1a(unsigned int *a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    unsigned int v3;  // [bp-0x4]

    return a0(v0, v1, v2, v3);
}
```

## `sub_1035cc4a` `0x1035cc4a`

_26 bytes. (leaf/helper — see body)_

```c
void sub_1035cc4a(int a0)
{
    int v3;  // edi
    int v4;  // esi
    int v5;  // ebx
    int v0;  // [bp-0x1c]
    char v1;  // [bp+0x0]

    sub_10369d26(a0, v0, 0, 0, v3, v4, v5, &v1);
    return;
}
```

## `sub_1035cc64` `0x1035cc64`

_23 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
    unsigned int field_c;
} struct_0;

int sub_1035cc64(void)
{
    unsigned int v2;  // ecx
    unsigned int v3;  // edx
    struct_0 *v1;  // [bp+0x8]

    sub_1035cb28(v1, v2, v3);
    return;
}
```

## `sub_1035cc7b` `0x1035cc7b`

_6 bytes. (leaf/helper — see body)_

```c
extern char g_1038ed30;

int sub_1035cc7b(void)
{
    return &g_1038ed30;
}
```

## `sub_1035cc81` `0x1035cc81`

_177 bytes. (leaf/helper — see body)_

```c
extern int g_1038ed30;
extern int g_1038ed40;
extern int g_1038eda0;
extern int g_1038efb0;
extern unsigned int g_103a3b80[4];
extern unsigned int g_103a3c80;
extern int g_103a4ca0;

unsigned int sub_1035cc81(void)
{
    int v2;  // eax
    unsigned int v3;  // eax
    unsigned int v4;  // edx
    int v5;  // ecx
    int v6;  // edx
    int iter;  // ecx
    unsigned int v8;  // edi
    unsigned int v0;  // [bp-0x8]

    v2 = g_103a4ca0;
    v0 = 20;
    v2 = 20;
    if (!v2)
    {
        v2 = 0x200;
    }
    else if (!(v2 < 20))
    {
        goto LABEL_1035cca0;
    }
    g_103a4ca0 = v2;
LABEL_1035cca0:
    v3 = sub_103574c2(v2, 4);
    g_103a3c80 = v3;
    if (!v3)
    {
        g_103a4ca0 = 20;
        v3 = sub_103574c2(20, 4);
        g_103a3c80 = v3;
        if (!v3)
            return 26;
    }
    v4 = 0;
    v5 = &g_1038ed30;
    while (true)
    {
        *((int *)(v4 + v3)) = v5;
        v5 += 32;
        v4 += 4;
        if (v5 >= &g_1038efb0)
            break;
        v3 = g_103a3c80;
    }
    v0 = 4294967294;
    v6 = 0;
    iter = &g_1038ed40;
    v0 = v8;
    do
    {
        if (*((int *)((v6 & 31) * 56 + g_103a3b80[v6 >> 5])) == 4294967295 || *((int *)((v6 & 31) * 56 + g_103a3b80[v6 >> 5])) == 4294967294 || !*((int *)((v6 & 31) * 56 + g_103a3b80[v6 >> 5])))
            *((unsigned int *)iter) = 4294967294;
    } while ((iter = (int)(iter + 32), v6 = (int)(v6 + 1), iter < &g_1038eda0));
    return 0;
}
```

## `sub_1035cd32` `0x1035cd32`

_32 bytes. (leaf/helper — see body)_

```c
extern char g_103a3034;
extern unsigned int g_103a3c80;

void sub_1035cd32(void)
{
    unsigned int v0;  // [bp-0x4]

    sub_103625ff();
    if (g_103a3034)
    {
        sub_103623e2();
        v0 = g_103a3c80;
        sub_1035345e();
    }
    else
    {
        v0 = g_103a3c80;
        sub_1035345e();
    }
    return;
}
```

## `sub_1035cd52` `0x1035cd52`

_60 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b1b8;
extern struct_0 g_1038ed30;
extern struct_0 g_1038ef90;

int sub_1035cd52(unsigned int a0, unsigned int a1, struct_0 *idx)
{
    unsigned int v1;  // esi
    int v2;  // eax
    unsigned int v0;  // [bp-0x4]

    v0 = v1;
    if (idx >= &g_1038ed30.padding_0[0] && idx <= &g_1038ef90.padding_0[0])
    {
        v2 = sub_1035a599((idx - &g_1038ed30.padding_0[0] >> 5) + 16, a1, (idx - &g_1038ed30.padding_0[0] >> 5) + 16);
        idx->field_c = idx->field_c | 0x8000;
        return v2;
    }
    return g_1038b1b8(idx + 2);
}
```

## `sub_1035cd8e` `0x1035cd8e`

_46 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[12];
    unsigned int field_c;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1b8;

struct_1 * sub_1035cd8e(unsigned int a0, unsigned int a1, unsigned int a2, struct_1 *idx)
{
    if (a2 >= 20)
        return g_1038b1b8(idx + 2);
    sub_1035a599(a0, a1, a2 + 16);
    idx->field_c = idx->field_c | 0x8000;
    return idx;
}
```

## `sub_1035cdbc` `0x1035cdbc`

_54 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b1bc;
extern struct_0 g_1038ed30;
extern struct_0 g_1038ef90;

int sub_1035cdbc(struct_0 *idx)
{
    if (idx >= &g_1038ed30.padding_0[0] && idx <= &g_1038ef90.padding_0[0])
    {
        idx->field_c = idx->field_c & 4294934527;
        return sub_1035a4c1((idx - &g_1038ed30.padding_0[0] >> 5) + 16);
    }
    return g_1038b1bc(idx + 2);
}
```

## `sub_1035cdf2` `0x1035cdf2`

_42 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b1bc;

int sub_1035cdf2(unsigned int a0, struct_0 *idx)
{
    if (a0 >= 20)
        return g_1038b1bc(idx + 2);
    idx->field_c = idx->field_c & 4294934527;
    return sub_1035a4c1(a0 + 16);
}
```

## `sub_1035ce1c` `0x1035ce1c`

_672 bytes. refs "ccs=", "UTF-8", "UTF-16LE"_

```c
extern unsigned int g_103a387c;
extern unsigned int g_103a3aac;

unsigned int [5] sub_1035ce1c(int a0, char *i, int a2)
{
    unsigned int v12;  // ecx
    char iter[2];  // esi
    unsigned int v22;  // eax
    unsigned int v23;  // eax
    char v24[2];  // esi
    unsigned int idx[5];  // eax
    char v14;  // al
    unsigned int v15;  // edi
    unsigned int v16;  // eax
    unsigned int v17;  // eax
    unsigned int v18;  // eax
    unsigned int v19;  // eax
    unsigned int v20;  // eax
    unsigned int v21;  // eax
    unsigned int v0;  // [bp-0x34]
    unsigned int v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x28]
    unsigned int v4;  // [bp-0x24]
    unsigned int v5;  // [bp-0x20]
    unsigned int v6;  // [bp-0x14]
    unsigned int v7;  // [bp-0x10]
    unsigned int v8;  // [bp-0xc]
    unsigned int v9;  // [bp-0x8]
    unsigned int v10;  // [bp+0x8]
    unsigned int v11[5];  // [bp+0x10]

    v9 = g_103a3aac;
    v7 = 0;
    v8 = 0;
    for (v6 = 0; *(i) == 32; i += 1);
    if (*(i) != 97)
    {
        if (*(i) != 114)
        {
            if (*(i) != 0x77)
            {
                v5 = 0;
                v4 = 0;
                v3 = 0;
                v2 = 0;
                v1 = 0;
                *((unsigned int *)sub_103575e0()) = 22;
                sub_103535f2();
                return NULL;
            }
            v10 = 769;
LABEL_1035ce88:
            v9 |= 2;
        }
        else
        {
            v9 |= 1;
            v10 = 0;
        }
        v12 = 1;
        iter = i + 1;
        v14 = iter[0];
        if (iter[0])
        {
            do
            {
                if (!v12)
                    break;
                v16 = v14;
                if (v16 <= 83)
                {
                    if (v16 != 83)
                    {
                        v17 = v16 - 32;
                        if (v16 == 32)
                            continue;
                        v18 = v17 - 11;
                        if (v17 != 11)
                        {
                            v19 = v18 - 1;
                            if (v18 != 1)
                            {
                                v20 = v19 - 24;
                                if (v19 != 24)
                                {
                                    if (v20 != 10)
                                    {
                                        if (v20 != 14)
                                            goto LABEL_1035d05b;
                                        if (!v8)
                                        {
                                            v10 |= 16;
                                            v8 = 1;
                                            continue;
                                        }
                                    }
                                    else
                                    {
                                        v10 |= 128;
                                        continue;
                                    }
                                }
                                else
                                {
                                    if (!((char)v10 & 64))
                                    {
                                        v10 |= 64;
                                        continue;
                                    }
                                }
                            }
                            else
                            {
                                v6 = 1;
                                goto LABEL_1035cfc0;
                            }
                        }
                        else
                        {
                            if (!((char)v10 & 2))
                            {
                                v10 = v10 & 4294967294 | 2;
                                v9 = v9 & 0xfffffffc | 128;
                                continue;
                            }
                        }
                    }
                    else if (!v8)
                    {
                        v10 |= 32;
                        v8 = 1;
                        continue;
                    }
                }
                v21 = v16 - 84;
                if (v16 != 84)
                {
                    v22 = v21 - 14;
                    if (v21 != 14)
                    {
                        v23 = v22 - 1;
                        if (v22 != 1)
                        {
                            if (v23 != 11)
                            {
                                if (v23 != 0x11)
                                    goto LABEL_1035d05b;
                                if (!((unsigned short)v10 & 0xc000))
                                {
                                    v10 |= 0x4000;
                                    continue;
                                }
                            }
                            else
                            {
                                if (!v7)
                                {
                                    v9 &= 4294950911;
                                    v7 = 1;
                                    continue;
                                }
                            }
                        }
                        else
                        {
                            if (!v7)
                            {
                                v9 |= 0x4000;
                                v7 = 1;
                                continue;
                            }
                        }
                    }
                    else
                    {
                        if (!((unsigned short)v10 & 0xc000))
                        {
                            v10 |= 0x8000;
                            continue;
                        }
                    }
                    goto LABEL_1035cfc0;
                }
                else if (((unsigned short)v10 & 0x1000))
                {
LABEL_1035cfc0:
                    v12 = 0;
                    continue;
                }
                else
                {
                    v10 |= 0x1000;
                }
                iter = &iter[1];
                v14 = iter[0];
            } while (iter[0]);
            for (; iter[0] == 32; iter = &iter[1]);
            if (!sub_103631e1("ccs=", iter, 4))
            {
                v24 = iter + 2;
                if (!sub_10363065(v24, "UTF-8"))
                {
                    iter = &v24[2 + 1];
                    v10 |= 0x40000;
                }
                if (!sub_10363065(v24, "UTF-16LE"))
                {
                    iter = v24 + 4;
                    v10 |= 0x20000;
                }
                if (sub_10363065(v24, "UNICODE"))
                    goto LABEL_1035d05b;
                iter = &v24[3 + 1];
                v10 |= 0x10000;
            }
LABEL_1035d05b:
            v4 = 0;
            v3 = 0;
            v2 = 0;
            v1 = 0;
            v0 = 0;
            *((unsigned int *)sub_103575e0()) = 22;
            sub_103535f2();
LABEL_1035d093:
            idx = NULL;
        }
        else
        {
            for (v5 = v15; iter[0] == 32; iter = &iter[1]);
            if (iter[0])
                goto LABEL_1035d05b;
            if (sub_10362e2d(&v6, a0, v10, a2, 384))
                goto LABEL_1035d093;
            idx = v11;
            g_103a387c = g_103a387c + 1;
            idx[3] = v9;
            idx[1] = 0;
            idx[0] = 0;
            idx[2] = 0;
            idx[1 + 2] = 0;
            idx[4] = v6;
        }
        return idx;
    }
    v10 = 265;
    goto LABEL_1035ce88;
}
```

## `sub_1035d0bc` `0x1035d0bc`

_292 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b1b8;
extern unsigned int g_103a1320;
extern unsigned int g_103a3c80;
extern char g_103a4ca0;

void sub_1035d0bc(unsigned int a0)
{
    void* idx;  // edi
    unsigned int v7;  // ecx
    unsigned int *v16;  // eax
    unsigned int v8;  // edx
    void* v9;  // ecx
    void* index;  // esi
    struct_0 **v11;  // eax
    void* v12;  // ecx
    void* v13;  // ecx
    unsigned int v14;  // esi
    int v15;  // eax
    unsigned int v0;  // [bp-0x10]
    void* v1;  // [bp-0xc], Other Possible Types: unsigned int
    unsigned int v2;  // [bp+0x0]
    void* v3;  // [bp+0xfffe4]
    void* v4;  // [bp+0xfffe8], Other Possible Types: unsigned int
    unsigned int v5;  // [bp+0x100000]

    sub_1035b0cc(&g_103a1320, 16);
    idx = NULL;
    v4 = 0;
    v1 = 0x1;
    sub_1035a599(v7, v8, 1);
    v9 = 0x1;
    v5 = 0;
    index = NULL;
    while (true)
    {
        v3 = index;
        if (index >= *((int *)&g_103a4ca0))
            break;
        v11 = g_103a3c80 + index * 4;
        if (*(v11))
        {
            if (!((char)*(v11)->field_c & 131) && (unsigned short)*(v11)->field_c >= 0)
            {
                v12 = v9;
                if (index - 3 <= 0x10 && (v1 = index + 16, v13 = index + 16, v12 = index + 16, !sub_1035a4d6(v9, v8)))
                    break;
                v1 = *((int *)(g_103a3c80 + index * 4));
                sub_1035cd8e(v12, v8, index, *((int *)(g_103a3c80 + index * 4)));
                v1 = *((int *)(g_103a3c80 + index * 4));
                if (((char)v1[12] & 131))
                {
                    sub_1035cdf2(index, v1);
                    v9 = v1;
                }
                else
                {
                    idx = v1;
                    goto LABEL_1035d1af;
                }
            }
            index += 1;
        }
        else
        {
            v14 = index * 4;
            v1 = 0x38;
            v15 = sub_10357482(56);
            *((int *)(v14 + g_103a3c80)) = v15;
            v16 = g_103a3c80 + v14;
            if (!*(v16))
                break;
            v1 = 4000;
            v0 = *(v16) + 32;
            if (!(unsigned int)sub_1035ca63())
            {
                v1 = *((int *)(v14 + g_103a3c80));
                sub_1035345e();
                *((unsigned int *)(v14 + g_103a3c80)) = 0;
                break;
            }
            else
            {
                v1 = *((int *)(v14 + g_103a3c80)) + 32;
                g_1038b1b8(*((int *)(v14 + g_103a3c80)) + 32);
                idx = *((int *)(v14 + g_103a3c80));
            }
LABEL_1035d1af:
            v4 = idx;
            break;
        }
    }
    if (idx)
    {
        *((unsigned int *)&idx[12]) = (int)idx[12] & 0x8000;
        *((unsigned int *)&idx[4]) = 0;
        *((unsigned int *)&idx[8]) = 0;
        *((unsigned int *)idx) = 0;
        *((unsigned int *)&idx[28]) = 0;
        *((unsigned int *)&idx[16]) = 4294967295;
    }
    v5 = 4294967294;
    sub_1035d1e3();
    sub_1035b111(v1, &g_103a1320, 16, v2);
    return;
}
```

## `sub_1035d1e0` `0x1035d1e0`

_3 bytes. (leaf/helper — see body)_

```c
void sub_1035d1e0(void)
{
    sub_1035d1e3();
    return;
}
```

## `sub_1035d1e3` `0x1035d1e3`

_9 bytes. (leaf/helper — see body)_

```c
int sub_1035d1e3(void)
{
    return sub_1035a4c1(1);
}
```

## `sub_1035d1ec` `0x1035d1ec`

_652 bytes. refs "UTF-16LE", "UNICODE"_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
    struct struct_1 *field_10;
    char padding_14[8];
    unsigned int field_1c;
} struct_0;

typedef struct struct_1 {
    unsigned short field_0;
    unsigned short field_2;
} struct_1;

extern unsigned int g_103a387c;
extern unsigned int g_103a3aac;

struct_0 * sub_1035d1ec(int a0, unsigned short *a1)
{
    unsigned short v10[2];  // esi
    unsigned short v11[2];  // esi
    unsigned int v20;  // eax
    unsigned int v21;  // eax
    unsigned int v22;  // eax
    unsigned int v23;  // eax
    unsigned int v24;  // eax
    unsigned int v25;  // eax
    unsigned int v26;  // eax
    unsigned short v27[2];  // esi
    unsigned int v13;  // eax
    unsigned int v14;  // ebx
    unsigned int v15;  // edi
    unsigned int v16;  // ecx
    unsigned short iter[2];  // esi
    unsigned short v18;  // ax
    unsigned int v19;  // eax
    unsigned int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x2c]
    unsigned int v2;  // [bp-0x28]
    unsigned int v3;  // [bp-0x24]
    unsigned int v4;  // [bp-0x20]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    unsigned int v7;  // [bp-0x4]
    int v8;  // [bp+0xc]
    struct_0 *idx;  // [bp+0x10]

    v6 = 0;
    v5 = 0;
    v7 = 0;
    v10 = a1;
    while (true)
    {
        v11 = v10;
        if (v11[0] != 32)
            break;
        v10 = &v11[1];
    }
    v13 = v11[0];
    if (v13 != 97)
    {
        if (v13 != 114)
        {
            if (v13 != 0x77)
            {
                v4 = 0;
                v3 = 0;
                v2 = 0;
                v1 = 0;
                v0 = 0;
                *((unsigned int *)sub_103575e0()) = 22;
                sub_103535f2();
                return NULL;
            }
            v14 = 769;
LABEL_1035d259:
            v15 = g_103a3aac | 2;
        }
        else
        {
            v14 = 0;
            v15 = g_103a3aac | 1;
        }
        v16 = 1;
        iter = &v11[1];
        v18 = iter[0];
        if (iter[0])
        {
            do
            {
                if (!v16)
                    break;
                v19 = v18;
                if (v19 <= 83)
                {
                    if (v19 != 83)
                    {
                        v20 = v19 - 32;
                        if (v19 == 32)
                            continue;
                        v21 = v20 - 11;
                        if (v20 != 11)
                        {
                            v22 = v21 - 1;
                            if (v21 != 1)
                            {
                                v23 = v22 - 24;
                                if (v22 != 24)
                                {
                                    if (v23 != 10)
                                    {
                                        if (v23 != 14)
                                        {
                                            v4 = 0;
                                            v3 = 0;
                                            v2 = 0;
                                            v1 = 0;
                                            v0 = 0;
                                            *((unsigned int *)sub_103575e0()) = 22;
                                            sub_103535f2();
                                            return NULL;
                                        }
                                        if (!v5)
                                        {
                                            v5 = 1;
                                            v14 |= 16;
                                            continue;
                                        }
                                    }
                                    else
                                    {
                                        v14 |= 128;
                                        continue;
                                    }
                                }
                                else
                                {
                                    if (!((char)v14 & 64))
                                    {
                                        v14 |= 64;
                                        continue;
                                    }
                                }
                            }
                            else
                            {
                                v7 = 1;
                                goto LABEL_1035d386;
                            }
                        }
                        else
                        {
                            if (!((char)v14 & 2))
                            {
                                v14 = v14 & 4294967294 | 2;
                                v15 = v15 & 0xfffffffc | 128;
                                continue;
                            }
                        }
                    }
                    else if (!v5)
                    {
                        v5 = 1;
                        v14 |= 32;
                        continue;
                    }
                }
                v24 = v19 - 84;
                if (v19 != 84)
                {
                    v25 = v24 - 14;
                    if (v24 != 14)
                    {
                        v26 = v25 - 1;
                        if (v25 != 1)
                        {
                            if (v26 != 11)
                            {
                                if (v26 != 0x11)
                                {
                                    v4 = 0;
                                    v3 = 0;
                                    v2 = 0;
                                    v1 = 0;
                                    v0 = 0;
                                    *((unsigned int *)sub_103575e0()) = 22;
                                    sub_103535f2();
                                    return NULL;
                                }
                                if (!((unsigned short)v14 & 0xc000))
                                {
                                    v14 |= 0x4000;
                                    continue;
                                }
                            }
                            else
                            {
                                if (!v6)
                                {
                                    v6 = 1;
                                    v15 &= 4294950911;
                                    continue;
                                }
                            }
                        }
                        else
                        {
                            if (!v6)
                            {
                                v6 = 1;
                                v15 |= 0x4000;
                                continue;
                            }
                        }
                    }
                    else
                    {
                        if (!((unsigned short)v14 & 0xc000))
                        {
                            v14 |= 0x8000;
                            continue;
                        }
                    }
                    goto LABEL_1035d386;
                }
                else if (((unsigned short)v14 & 0x1000))
                {
LABEL_1035d386:
                    v16 = 0;
                    continue;
                }
                else
                {
                    v14 |= 0x1000;
                }
                iter = &iter[1];
                v18 = iter[0];
            } while (iter[0]);
            if (v7)
            {
                for (; iter[0] == 32; iter = &iter[1]);
                if (sub_10363bdc("c", iter, 4))
                {
                    v4 = 0;
                    v3 = 0;
                    v2 = 0;
                    v1 = 0;
                    v0 = 0;
                    *((unsigned int *)sub_103575e0()) = 22;
                    sub_103535f2();
                    return NULL;
                }
                v27 = iter + 2;
                if (!sub_10363b4b(v27, "U"))
                {
                    iter = &v27[2 + 1];
                    v14 |= 0x40000;
                }
                else if (!sub_10363b4b(v27, L"UTF-16LE"))
                {
                    iter = v27 + 4;
                    v14 |= 0x20000;
                }
                else
                {
                    if (sub_10363b4b(v27, L"UNICODE"))
                    {
                        v4 = 0;
                        v3 = 0;
                        v2 = 0;
                        v1 = 0;
                        v0 = 0;
                        *((unsigned int *)sub_103575e0()) = 22;
                        sub_103535f2();
                        return NULL;
                    }
                    iter = &v27[3 + 1];
                    v14 |= 0x10000;
                }
            }
        }
        for (; iter[0] == 32; iter = &iter[1]);
        if (iter[0])
        {
            v4 = 0;
            v3 = 0;
            v2 = 0;
            v1 = 0;
            v0 = 0;
            *((unsigned int *)sub_103575e0()) = 22;
            sub_103535f2();
            return NULL;
        }
        else if (sub_10363a1e(&/* unsupported instruction */, a0, v14, v8, 384))
        {
            return NULL;
        }
        else
        {
            g_103a387c = g_103a387c + 1;
            idx->field_c = v15;
            idx->field_4 = 0;
            idx->field_0 = 0;
            idx->field_8 = 0;
            idx->field_1c = 0;
            idx->field_10 = a1;
            return idx;
        }
    }
    v14 = 265;
    goto LABEL_1035d259;
}
```

## `sub_1035d478` `0x1035d478`

_72 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[68];
    int field_44;
} struct_0;

int sub_1035d478(int a0)
{
    struct_0 *v1;  // esi
    int v2;  // eax

    v1 = sub_10358d31();
    if (!v1)
    {
        *((unsigned int *)sub_103575e0()) = 12;
        return 0;
    }
    if (v1->field_44)
        return v1->field_44;
    v2 = sub_10357482(36);
    v1->field_44 = v2;
    if (!v2)
    {
        *((unsigned int *)sub_103575e0()) = 12;
        return a0;
    }
    return v1->field_44;
}
```

## `sub_1035d4c0` `0x1035d4c0`

_52 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038f01c;

unsigned int sub_1035d4c0(unsigned int *a0)
{
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    if (a0)
    {
        *(a0) = g_1038f01c;
        return 0;
    }
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    *((unsigned int *)sub_103575e0()) = 22;
    sub_103535f2();
    v4 = 22;
    return v4;
}
```

## `sub_1035d4f4` `0x1035d4f4`

_52 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038f020;

unsigned int sub_1035d4f4(unsigned int *a0)
{
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    if (a0)
    {
        *(a0) = g_1038f020;
        return 0;
    }
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    *((unsigned int *)sub_103575e0()) = 22;
    sub_103535f2();
    v4 = 22;
    return v4;
}
```

## `sub_1035d528` `0x1035d528`

_52 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038f018;

unsigned int sub_1035d528(unsigned int *a0)
{
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    if (a0)
    {
        *(a0) = g_1038f018;
        return 0;
    }
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    *((unsigned int *)sub_103575e0()) = 22;
    sub_103535f2();
    v4 = 22;
    return v4;
}
```

## `sub_1035d55c` `0x1035d55c`

_6 bytes. (leaf/helper — see body)_

```c
extern char g_1038f01c;

int sub_1035d55c(void)
{
    return &g_1038f01c;
}
```

## `sub_1035d562` `0x1035d562`

_6 bytes. (leaf/helper — see body)_

```c
extern char g_1038f020;

int sub_1035d562(void)
{
    return &g_1038f020;
}
```

## `sub_1035d568` `0x1035d568`

_6 bytes. (leaf/helper — see body)_

```c
extern char g_1038f018;

int sub_1035d568(void)
{
    return &g_1038f018;
}
```

## `sub_1035d56e` `0x1035d56e`

_6 bytes. (leaf/helper — see body)_

```c
extern char g_1038f0a8;

int sub_1035d56e(void)
{
    return &g_1038f0a8;
}
```

## `sub_1035d574` `0x1035d574`

_827 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    int field_0;
    struct struct_3 *field_4;
} struct_2;

typedef struct struct_3 {
    char field_0;
    char padding_1[62];
    char field_3f;
} struct_3;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b040;
extern struct_0 *g_1038b26c;
extern unsigned int g_1038f0b0;
extern unsigned int g_1038f0bc;
extern unsigned int g_103a1340;
extern void g_103a3880;
extern char g_103a3884;
extern unsigned short g_103a38c6;
extern unsigned int g_103a38d4;
extern char g_103a38d8;
extern unsigned short g_103a391a;
extern unsigned int g_103a3928;
extern unsigned int g_103a392c;
extern void* g_103a3930;

void sub_1035d574(void)
{
    unsigned int v18;  // ecx
    unsigned int v19;  // edx
    void* iter;  // esi
    unsigned int v28;  // eax
    unsigned int v29;  // eax
    unsigned int v30;  // eax
    unsigned int *v31;  // eax
    unsigned int *v32;  // eax
    void* v20;  // esi
    unsigned int v21;  // eax
    unsigned int v22;  // eax
    unsigned int *v23;  // eax
    unsigned int *v24;  // eax
    unsigned int *v25;  // eax
    struct_2 *v26;  // edi
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    void* v5;  // [bp-0xc], Other Possible Types: unsigned int
    unsigned int v6;  // [bp+0x0]
    void* v8;  // [bp+0xfffc8]
    unsigned int v9;  // [bp+0xfffcc]
    int v10;  // [bp+0xfffd0]
    unsigned int v11;  // [bp+0xfffd4]
    unsigned int v12;  // [bp+0xfffd8]
    unsigned int v13;  // [bp+0xfffdc]
    unsigned int v14;  // [bp+0xfffe0]
    struct_2 *idx;  // [bp+0xfffe4]
    unsigned int v16;  // [bp+0xfffe8]
    unsigned int v17;  // [bp+0x100000]

    sub_1035b0cc(&g_103a1340, 44);
    v9 = 0;
    memset(/* unsupported instruction */ - 44, 0, 20);
    sub_1035a599(v18, v19, 7);
    v17 = 0;
    idx = sub_1035d56e();
    if (sub_1035d528(/* unsupported instruction */ - 28))
    {
        v5 = 0;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        sub_103534f6();
    }
    if (sub_1035d4c0(/* unsupported instruction */ - 36))
    {
        v5 = 0;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        sub_103534f6();
    }
    if (sub_1035d4f4(/* unsupported instruction */ - 40))
    {
        v5 = 0;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        sub_103534f6();
    }
    v10 = sub_10357436();
    g_103a392c = 0;
    g_1038f0bc = 4294967295;
    g_1038f0b0 = 4294967295;
    v20 = sub_10363c22("TZ");
    v8 = v20;
    if (!(v20 && *((char *)v20)))
    {
        if (g_103a3930)
        {
            v5 = g_103a3930;
            sub_1035345e();
            g_103a3930 = 0;
        }
        v5 = &g_103a3880;
        v5 = v5;
        if (g_1038b26c(&g_103a3880) != 4294967295)
        {
            g_103a392c = 1;
            v22 = *((int *)&g_103a3880) * 60;
            v16 = v22;
            if (g_103a38c6)
                v16 = v22 + g_103a38d4 * 60;
            if (g_103a391a && g_103a3928)
            {
                v14 = 1;
                v13 = (g_103a3928 - g_103a38d4) * 60;
            }
            else
            {
                v14 = 0;
                v13 = 0;
            }
            if (g_1038b040(v10, 0, &g_103a3884, 4294967295, idx->field_0, 63, 0, /* unsupported instruction */ - 48) && !v11)
                *((char *)(idx->field_0 + 63)) = 0;
            else
                *((char *)idx->field_0) = 0;
            if (g_1038b040(v10, 0, &g_103a38d8, 4294967295, idx->field_4, 63, 0, /* unsupported instruction */ - 48) && !v11)
                idx->field_4->field_3f = 0;
            else
                idx->field_4->field_0 = 0;
        }
    }
    else if (g_103a3930)
    {
        v5 = g_103a3930;
        v5 = v5;
        if (sub_10359ed0(v20, g_103a3930) && g_103a3930)
        {
            v5 = g_103a3930;
            sub_1035345e();
            goto LABEL_1035d657;
        }
    }
    else
    {
LABEL_1035d657:
        g_103a3930 = sub_10357482(sub_10352f20(v20) + 1);
        v5 = v20;
        if (g_103a3930)
        {
            v21 = sub_10352f20(v20);
            v5 = v20;
            if (sub_10359f58(g_103a3930, v21 + 1, v5))
            {
                v5 = NULL;
                v4 = 0;
                v3 = 0;
                v2 = 0;
                v1 = 0;
                sub_103534f6();
                goto LABEL_1035d797;
            }
        }
    }
    v12 = 1;
LABEL_1035d797:
    v23 = sub_1035d568();
    *(v23) = v16;
    v24 = sub_1035d55c();
    *(v24) = v14;
    v25 = sub_1035d562();
    *(v25) = v13;
    v17 = 4294967294;
    sub_1035d823();
    if (v12)
    {
        sub_1035b111(v5, &g_103a1340, 44, v6);
        return;
    }
    v26 = idx;
    if (sub_1035f222(v26->field_0, 64, v20, 3))
    {
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        sub_103534f6();
    }
    iter = v20 + 3;
    if (*((char *)iter) == 45)
    {
        v9 = 1;
        iter += 1;
    }
    for (v16 = sub_10363c11(iter) * 3600; *((char *)iter) == 43 || *((char *)iter) >= 48 && *((char *)iter) <= 57; iter += 1);
    if (*((char *)iter) == 58)
    {
        v28 = sub_10363c11(iter + 1);
        for (v16 += v28 * 60; *((char *)iter) >= 48 && *((char *)iter) <= 57; iter += 1);
        if (*((char *)iter) == 58)
        {
            v29 = sub_10363c11(iter + 1);
            for (v16 += v29; *((char *)iter) >= 48 && *((char *)iter) <= 57; iter += 1);
        }
    }
    if (v9)
        v16 = -(v16);
    v30 = *((char *)iter);
    v14 = v30;
    if (!v30)
    {
        v26->field_4->field_0 = 0;
    }
    else if (sub_1035f222(v26->field_4, 64, iter, 3))
    {
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        sub_103534f6();
    }
    v31 = sub_1035d568();
    *(v31) = v16;
    v32 = sub_1035d55c();
    *(v32) = v14;
    sub_1035b111(v5, &g_103a1340, 44, v6);
    return;
}
```

## `sub_1035d81e` `0x1035d81e`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1035d81e(void)
{
    sub_1035d823();
    return;
}
```

## `sub_1035d823` `0x1035d823`

_9 bytes. (leaf/helper — see body)_

```c
int sub_1035d823(void)
{
    return sub_1035a4c1(7);
}
```

## `sub_1035d8bd` `0x1035d8bd`

_501 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038efac[4];
extern char g_1038efb0;
extern unsigned int g_1038efe0[4];
extern char g_1038efe4;
extern unsigned int g_1038f0b0;
extern unsigned int g_1038f0b4;
extern unsigned int g_1038f0b8;
extern unsigned int g_1038f0bc;
extern unsigned int g_1038f0c0;
extern int g_1038f0c4;

int sub_1035d8bd(void)
{
    unsigned int v17;  // edi
    unsigned int v18;  // eax
    unsigned int index;  // eax
    unsigned int v27;  // esi
    unsigned int v28;  // edi
    int v29;  // edx
    unsigned int v30;  // eax
    int v31;  // esi
    unsigned int v32;  // edi
    int v33;  // eax
    unsigned int v34;  // 4101
    unsigned int v19;  // cc_op
    unsigned int v35[4];  // esi
    unsigned int v36;  // ecx
    unsigned int v37;  // eax
    int v38;  // 4102
    unsigned int v39;  // 4112
    unsigned int v20;  // cc_dep1
    unsigned int v21;  // eax
    unsigned int v22;  // eax
    unsigned int v23;  // 4105
    unsigned int idx;  // eax
    unsigned int v25;  // esi
    unsigned int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x2c]
    unsigned int v2;  // [bp-0x28]
    unsigned int v3;  // [bp-0x24]
    unsigned int v4;  // [bp-0x20]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]
    unsigned int v8;  // [bp+0x4]
    unsigned int idx1;  // [bp+0x8]
    unsigned int v10;  // [bp+0xc]
    unsigned int v11;  // [bp+0x10]
    int v12;  // [bp+0x14]
    unsigned int v13;  // [bp+0x18]
    unsigned int v14;  // [bp+0x1c]
    unsigned int v15;  // [bp+0x20]
    unsigned int v16;  // [bp+0x24]

    v7 = 0;
    v17 = v10;
    v18 = v17;
    if (idx1 == 1)
    {
        v19 = 15;
        v20 = v18 & 2147483651;
        v21 = v18 & 2147483651;
        if ((v18 & 2147483651) < 0)
        {
            v22 = v21 - 1 | 0xfffffffc;
            v19 = 18;
            v20 = v22 + 1;
            v21 = v22 + 1;
        }
        v5 = v21;
        v23 = _ccall(4, v19, v20, 0, 0);
        if ((!((char)v23) || (v4 = 100, !v17 % 100)) && (int)((v17 + 1900) % 400))
        {
            idx = index * 4;
            v25 = *((int *)(idx + (char *)&g_1038efe0[0]));
        }
        else
        {
            idx = index * 4;
            v25 = *((int *)(idx + (char *)&g_1038efac[0]));
        }
        idx1 = idx;
        v4 = 100;
        v27 = v25 + 1;
        v4 = 7;
        v6 = (v17 + 299) / 400;
        v28 = v10;
        v29 = (v28 * 365 + (v28 - 1 + (v28 - 1 >> 31 & 3) >> 2) + v27 + v6 - (v17 - 1) / 100 - 25563) % 7;
        v30 = v11 * 7 - v29 + v12;
        v31 = (v29 <= v12 ? v27 + v30 - 7 : v27 + v30);
        v32 = v28;
        if (v11 == 5)
        {
            if ((v5 || (v4 = 100, !v28 % 100)) && (int)((v28 + 1900) % 400))
                v33 = *((int *)&(&g_1038efe4)[idx1]);
            else
                v33 = *((int *)&(&g_1038efb0)[idx1]);
            v32 = v28;
            if (v31 > v33)
            {
                v31 -= 7;
                v32 = v28;
            }
        }
    }
    else
    {
        if ((v18 & 2147483651) < 0)
        {
            v34 = _ccall(4, 18, ((v18 & 2147483651) - 1 | 0xfffffffc) + 1, 0, 0);
            if ((char)v34)
                goto LABEL_1035d9e2;
        }
        else if (!(v18 & 2147483651))
        {
LABEL_1035d9e2:
            v4 = 100;
            if (v17 % 100)
                goto LABEL_1035da09;
        }
        if ((int)((v17 + 1900) % 400))
        {
            v35 = g_1038efe0[index];
        }
        else
        {
LABEL_1035da09:
            v35 = g_1038efac[index];
        }
        v31 = (char *)v35 + v13;
        v32 = v17;
    }
    if (v8 == 1)
    {
        g_1038f0b4 = v31;
        g_1038f0b8 = ((v36 * 60 + v14) * 60 + v15) * 1000 + v16;
        g_1038f0b0 = v32;
        return;
    }
    g_1038f0c0 = v31;
    g_1038f0c4 = g_1038f0b8;
    if (sub_1035d4f4(&v7))
    {
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        sub_103534f6();
    }
    v37 = v7 * 1000;
    v38 = g_1038f0c4;
    g_1038f0c4 = g_1038f0c4 + v37;
    v39 = _ccall(8, 3, v38, v37, 0);
    if ((char)v39)
    {
        g_1038f0c4 = g_1038f0c4 + 86400000;
        g_1038f0c0 = g_1038f0c0 - 1;
    }
    else if (g_1038f0c4 >= 86400000)
    {
        g_1038f0c4 = g_1038f0c4 - 86400000;
        g_1038f0c0 = g_1038f0c0 + 1;
    }
    g_1038f0bc = v32;
    return;
}
```

## `sub_1035dab2` `0x1035dab2`

_430 bytes. (leaf/helper — see body)_

```c
extern char g_1038f0b0;
extern int g_1038f0b4;
extern char g_1038f0b8;
extern char g_1038f0bc;
extern char g_1038f0c0;
extern char g_1038f0c4;
extern unsigned short g_103a38c4;
extern unsigned short g_103a38c8;
extern unsigned short g_103a38ca;
extern unsigned short g_103a38ce;
extern unsigned short g_103a38d0;
extern unsigned short g_103a38d2;
extern unsigned short g_103a3918;
extern unsigned short g_103a391c;
extern unsigned short g_103a391e;
extern unsigned short g_103a3922;
extern unsigned short g_103a3924;
extern unsigned short g_103a3926;
extern unsigned int g_103a392c;

unsigned int sub_1035dab2(void)
{
    unsigned int v14;  // ecx
    unsigned int idx[6];  // edi
    unsigned int v16;  // edx
    unsigned int v17;  // ebx
    int v18;  // edx
    unsigned int v20;  // eax
    unsigned int v0;  // [bp-0x5c]
    unsigned int v1;  // [bp-0x38]
    unsigned int v2;  // [bp-0x30]
    unsigned int v3;  // [bp-0x2c]
    unsigned int v4;  // [bp-0x28]
    unsigned int v5;  // [bp-0x24]
    unsigned int v6;  // [bp-0x20]
    unsigned int v7;  // [bp-0x1c]
    unsigned int v8;  // [bp-0x18]
    unsigned int v9;  // [bp-0x14]
    unsigned int v10;  // [bp-0x10]
    unsigned int v11;  // [bp-0x8]
    unsigned int v12;  // [bp-0x8]

    v11 = v14;
    v12 = 0;
    if (sub_1035d4c0(&v12))
    {
        v10 = 0;
        v9 = 0;
        v8 = 0;
        v7 = 0;
        v6 = 0;
        sub_103534f6();
    }
    if (!v12)
        return 0;
    v16 = idx[5];
    v10 = v17;
    if (v16 != *((int *)&g_1038f0b0) || v16 != *((int *)&g_1038f0bc))
    {
        if (g_103a392c)
        {
            v9 = g_103a3926;
            v8 = g_103a3924;
            v7 = g_103a3922;
            if (!g_103a3918)
            {
                v6 = 0;
                v5 = g_103a391c;
                v4 = g_103a391e;
                v3 = v16;
                v2 = 1;
            }
            else
            {
                v6 = g_103a391e;
                v5 = 0;
                v4 = 0;
                v3 = v16;
                v2 = 0;
            }
            sub_1035d8bd(1);
            v9 = g_103a38d2;
            v8 = g_103a38d0;
            v7 = g_103a38ce;
            if (!g_103a38c4)
            {
                v6 = 0;
                v5 = g_103a38c8;
                v4 = g_103a38ca;
                v3 = idx[5];
                v2 = 1;
            }
            else
            {
                v6 = g_103a38ca;
                v5 = 0;
                v4 = 0;
                v3 = idx[5];
                v2 = 0;
            }
            sub_1035d8bd(0);
        }
        else
        {
            v1 = 2;
            v1 = 4;
            sub_1035d8bd(1, 1, v16, 1, 0, 0, 0, 0, 0);
            v0 = 2;
            v0 = 10;
            sub_1035d8bd(0, 1, idx[5], 5, 0, 0, 0, 0, 0);
        }
    }
    v18 = idx[1 + 1];
    if (g_1038f0b4 < *((int *)&g_1038f0c0))
    {
        if (v18 < g_1038f0b4)
        {
            return 0;
        }
        else if (v18 > *((int *)&g_1038f0c0))
        {
            return 0;
        }
        else if (v18 <= g_1038f0b4)
        {
            v20 = ((idx[2] * 60 + idx[1]) * 60 + idx[0]) * 1000;
            return (v18 == g_1038f0b4 ? v20 >= *((int *)&g_1038f0b8) : v20 < *((int *)&g_1038f0c4));
        }
        else if (v18 >= *((int *)&g_1038f0c0))
        {
            v20 = ((idx[2] * 60 + idx[1]) * 60 + idx[0]) * 1000;
            return (v18 == g_1038f0b4 ? v20 >= *((int *)&g_1038f0b8) : v20 < *((int *)&g_1038f0c4));
        }
    }
    else
    {
        if (v18 >= *((int *)&g_1038f0c0) && v18 <= g_1038f0b4)
        {
            if (v18 <= *((int *)&g_1038f0c0))
            {
                v20 = ((idx[2] * 60 + idx[1]) * 60 + idx[0]) * 1000;
                return (v18 == g_1038f0b4 ? v20 >= *((int *)&g_1038f0b8) : v20 < *((int *)&g_1038f0c4));
            }
            else if (v18 < g_1038f0b4)
            {
                return 0;
            }
            else
            {
                v20 = ((idx[2] * 60 + idx[1]) * 60 + idx[0]) * 1000;
                return (v18 == g_1038f0b4 ? v20 >= *((int *)&g_1038f0b8) : v20 < *((int *)&g_1038f0c4));
            }
        }
    }
    return 1;
}
```

## `sub_1035dc60` `0x1035dc60`

_70 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a1360;
extern unsigned int g_103a3934;

void sub_1035dc60(unsigned int a0)
{
    unsigned int v2;  // ecx
    unsigned int v3;  // edx
    unsigned int v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x100000]

    sub_1035b0cc(&g_103a1360, 8);
    if (g_103a3934)
    {
        sub_1035b111(&g_103a1360, 8, v0, a0);
        return;
    }
    sub_1035a599(v2, v3, 6);
    v1 = 0;
    if (!g_103a3934)
    {
        sub_1035d574();
        g_103a3934 = g_103a3934 + 1;
    }
    v1 = 4294967294;
    sub_1035dca6();
    sub_1035b111(&g_103a1360, 8, v0, a0);
    return;
}
```

## `sub_1035dca6` `0x1035dca6`

_9 bytes. (leaf/helper — see body)_

```c
int sub_1035dca6(void)
{
    return sub_1035a4c1(6);
}
```

## `sub_1035dcaf` `0x1035dcaf`

_56 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a1380;

void sub_1035dcaf(unsigned int a0)
{
    unsigned int v3;  // ecx
    unsigned int v4;  // edx
    unsigned int v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0xfffe8]
    unsigned int v2;  // [bp+0x100000]

    sub_1035b0cc(&g_103a1380, 12);
    sub_1035a599(v3, v4, 6);
    v2 = 0;
    v1 = sub_1035dab2();
    v2 = 4294967294;
    sub_1035dce7();
    sub_1035b111(&g_103a1380, 12, v0, a0);
    return;
}
```

## `sub_1035dce7` `0x1035dce7`

_9 bytes. (leaf/helper — see body)_

```c
int sub_1035dce7(void)
{
    return sub_1035a4c1(6);
}
```

## `sub_1035dcf0` `0x1035dcf0`

_53 bytes. (leaf/helper — see body)_

```c
int sub_1035dcf0(char *iter, char *node)
{
    unsigned int v0;  // eax
    unsigned int v1;  // ecx

    do
    {
        v0 = *(iter);
        iter += 1;
        if (v0 - 65 <= 25)
            v0 += 32;
        v1 = *(node);
        node += 1;
        if (v1 - 65 <= 25)
            v1 += 32;
    } while (v0 && v0 == v1);
    return v0 - v1;
}
```

## `sub_1035dd25` `0x1035dd25`

_211 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

int sub_1035dd25(char *a0, char *a1, unsigned int *a2)
{
    unsigned int v9;  // edi
    char *v10;  // edi
    int v11;  // eax
    unsigned int v12;  // esi
    int v13;  // esi
    int v14;  // eax
    unsigned int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x2c]
    unsigned int v2;  // [bp-0x28]
    unsigned int v3;  // [bp-0x24]
    unsigned int v4;  // [bp-0x20]
    unsigned int v5;  // [bp-0x1c]
    struct_0 v6;  // [bp-0x14]
    struct_0 *idx;  // [bp-0xc]
    char v8;  // [bp-0x8]

    sub_103536a7(&v6, a2);
    if (!a0)
    {
        v5 = 0;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        *((unsigned int *)sub_103575e0()) = 22;
        sub_103535f2();
        if (!v8)
            return 2147483647;
        idx[8].field_8 = idx[8].field_8 & 4294967293;
        return 2147483647;
    }
    else
    {
        v5 = v9;
        v10 = a1;
        if (!v10)
        {
            v4 = 0;
            v3 = 0;
            v2 = 0;
            v1 = 0;
            v0 = 0;
            *((unsigned int *)sub_103575e0()) = 22;
            sub_103535f2();
            if (v8)
                idx[8].field_8 = idx[8].field_8 & 4294967293;
            v11 = 2147483647;
        }
        else
        {
            if (!*((int *)(v6 + 20)))
            {
                v11 = sub_1035dcf0(a0, v10);
            }
            else
            {
                v4 = v12;
                do
                {
                    a0 += 1;
                    v13 = sub_10357624(*(a0), &v6);
                    v14 = sub_10357624(*(v10), &v6);
                    v10 += 1;
                } while (v13 && (a0 = a0, v13 == v14));
                v11 = v13 - v14;
            }
            if (v8)
                idx[8].field_8 = idx[8].field_8 & 4294967293;
        }
        return v11;
    }
}
```

## `sub_1035ddf8` `0x1035ddf8`

_80 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a3058;

int sub_1035ddf8(char *a0, char *a1)
{
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char *v5;  // [bp+0x0]

    if (g_103a3058)
        return sub_1035dd25(a0, a1, NULL);
    if (a0 && a1)
        return sub_1035dcf0(v5, a0);
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    *((unsigned int *)sub_103575e0()) = 22;
    sub_103535f2();
    return 2147483647;
}
```

## `sub_1035de48` `0x1035de48`

_54 bytes. (leaf/helper — see body)_

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

unsigned int sub_1035de48(char a0, unsigned int *a1)
{
    unsigned int v3;  // eax
    struct_0 v0;  // [bp-0x14]
    struct_1 *idx;  // [bp-0xc]
    char v2;  // [bp-0x8]

    sub_103536a7(&v0, a1);
    v3 = *((short *)(*((int *)(v0 + 200)) + a0 * 2));
    if (v2)
        idx->field_70 = idx->field_70 & 4294967293;
    return v3 & 0x8000;
}
```

## `sub_1035de7e` `0x1035de7e`

_14 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1035de7e(char a0)
{
    return sub_1035de48(a0, NULL);
}
```

## `sub_1035de90` `0x1035de90`

_22 bytes. (leaf/helper — see body)_

```c
int sub_1035de90(void)
{
    return;
}
```

## `sub_1035dea6` `0x1035dea6`

_22 bytes. (leaf/helper — see body)_

```c
int sub_1035dea6(void)
{
    return;
}
```

## `sub_1035debc` `0x1035debc`

_562 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    unsigned int field_0;
    char field_4;
    char field_5;
    char padding_6[2];
    unsigned int field_8;
    char padding_c[24];
    char field_24;
    char field_25;
    char field_26;
} struct_1;

typedef struct struct_2 {
    char padding_0[4];
    char field_4;
} struct_2;

typedef struct struct_5 {
    unsigned int field_0;
    char field_4;
    char padding_5[3];
    unsigned int field_8;
} struct_5;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b138;
extern struct_0 *g_1038b248;
extern struct_0 *g_1038b270;
extern struct_0 *g_1038b274;
extern unsigned int g_103a13a0;
extern unsigned int g_103a3b70;
extern void g_103a3b80;

void sub_1035debc(void)
{
    unsigned int v11;  // esi
    struct_1 *iter;  // eax
    unsigned int v21;  // ecx
    void* idx;  // esi
    int v23;  // ebx
    struct_5 *idx1;  // esi
    unsigned int v25;  // eax
    unsigned int v26;  // edi
    unsigned int v27;  // eax
    unsigned int v28;  // eax
    struct_1 *i;  // ecx
    struct_2 *v14;  // eax
    int v15;  // edi
    struct_2 *v16;  // ebx
    unsigned int j;  // esi
    struct_1 *node;  // eax
    unsigned int *v19;  // ecx
    struct_1 *k;  // edx
    struct_5 *v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x1c]
    void* v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x10]
    unsigned short v6;  // [bp+0xfffd2]
    struct_2 *v7;  // [bp+0xfffd4]
    int v8;  // [bp+0xfffe4]
    unsigned int *v9;  // [bp+0xfffe8]
    unsigned int v10;  // [bp+0x100000]

    sub_1035b0cc(&g_103a13a0, 84);
    v10 = 0;
    g_1038b138(/* unsupported instruction */ - 100);
    v10 = 4294967294;
    v4 = 56;
    v11 = 32;
    v11 = 32;
    iter = sub_103574c2(32, 56);
    if (!iter)
    {
        v11 = 32;
        sub_1035b111(v25, v3, v11, v4);
        return;
    }
    *((struct_1 **)&g_103a3b80) = iter;
    g_103a3b70 = 32;
    for (i = &iter[45].field_25; iter < i; i = *((int *)&g_103a3b80) + 0x700)
    {
        iter->field_4 = 0;
        iter->field_0 = 4294967295;
        iter->field_5 = 10;
        iter->field_8 = 0;
        iter->field_24 = 0;
        iter->field_25 = 10;
        iter->field_26 = 10;
        iter = &iter[1].padding_c[5];
    }
    if (v6)
    {
        v14 = v7;
        if (v14)
        {
            v15 = (int)v14->padding_0;
            v16 = &v14->field_4;
            v9 = &v16->padding_0[v15];
            if (v15 >= 0x800)
                v15 = 0x800;
            for (j = 1; g_103a3b70 < v15; j += 1)
            {
                v4 = 56;
                v11 = 32;
                node = sub_103574c2(32, 56);
                if (node)
                {
                    v19 = &(&g_103a3b80)[4 * j];
                    *(v19) = node;
                    g_103a3b70 = g_103a3b70 + 32;
                    for (k = &node[45].field_25; node < k; k = *(v19) + 0x700)
                    {
                        node->field_4 = 0;
                        node->field_0 = 4294967295;
                        node->field_5 = 10;
                        node->field_8 = 0;
                        node->field_24 = node->field_24 & 128;
                        node->field_25 = 10;
                        node->field_26 = 10;
                        node = &node[1].padding_c[5];
                    }
                }
                else
                {
                    v15 = g_103a3b70;
                    break;
                }
            }
            v8 = 0;
            if (v15 > NULL)
            {
                do
                {
                    v21 = *(v9);
                    if (v21 != 4294967295)
                    {
                        v11 = v11;
                        if (v21 != 4294967294)
                        {
                            v11 = v11;
                            if ((v16->padding_0[0] & 1) && ((v16->padding_0[0] & 8) || (v11 = v21, g_1038b274(v11))))
                            {
                                idx = (v8 & 31) * 56 + *((int *)&(&g_103a3b80)[4 * (v8 >> 5)]);
                                *((unsigned int *)idx) = *(v9);
                                *((char *)&idx[4]) = v16->padding_0[0];
                                v11 = 4000;
                                v3 = idx + 12;
                                if (!(unsigned int)sub_1035ca63())
                                {
                                    sub_1035b111(v25, v3, v11, v4);
                                    return;
                                }
                                *((unsigned int *)&idx[8]) = (int)idx[8] + 1;
                            }
                        }
                    }
                } while ((v8 = (int)(v8 + 1), v16 += 1, v9 += 4, v8 < v15));
            }
        }
    }
    v23 = 0;
    while (true)
    {
        idx1 = v23 * 56 + *((int *)&g_103a3b80);
        if (idx1->field_0 != 4294967295 && idx1->field_0 != 4294967294)
        {
            idx1->field_4 = idx1->field_4 | 128;
        }
        else
        {
            idx1->field_4 = 129;
            if (!v23)
            {
                v2 = 4294967286;
                v25 = 4294967286;
            }
            else
            {
                v25 = -(0 < v23 - 1) - 11;
            }
            v26 = g_1038b248(v25);
            if (v26 != 4294967295 && v26 && !((v27 = g_1038b274(v26), !v27)))
            {
                idx1->field_0 = v26;
                v28 = v27 & 0xff;
                if (v28 == 2)
                {
                    idx1->field_4 = idx1->field_4 | 64;
                }
                else if (v28 == 3)
                {
                    idx1->field_4 = idx1->field_4 | 8;
                }
                v1 = 4000;
                v0 = idx1 + 1;
                if (!(unsigned int)sub_1035ca63())
                {
                    v25 = v25;
                    sub_1035b111(v25, v3, v11, v4);
                    return;
                }
                idx1->field_8 = idx1->field_8 + 1;
            }
            else
            {
                idx1->field_4 = idx1->field_4 | 64;
                idx1->field_0 = 4294967294;
            }
        }
        v23 += 1;
        if (v23 >= 3)
        {
            g_1038b270(g_103a3b70);
            sub_1035b111(g_103a3b70, v3, v11, v4);
            return;
        }
    }
}
```

## `sub_1035e0e5` `0x1035e0e5`

_4 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1035e0e5(void)
{
    return 1;
}
```

## `sub_1035e0e9` `0x1035e0e9`

_10 bytes. (leaf/helper — see body)_

```c
void sub_1035e0e9(void)
{
    unsigned int v1;  // [bp+0x100000]

    v1 = 4294967294;
}
```

## `sub_1035e0fc` `0x1035e0fc`

_76 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b1f8;
extern struct_0 *g_103a3b80;
extern struct_0 *g_103a3c80;

void sub_1035e0fc(void)
{
    unsigned int v4;  // esi
    unsigned int v5;  // edi
    struct_0 **iter;  // esi
    struct_0 *v7;  // edi
    struct_0 *i;  // eax
    struct_0 *v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0x8]
    unsigned int v2;  // [bp-0x4]

    v2 = v4;
    v1 = v5;
    iter = &g_103a3b80;
    do
    {
        v7 = *(iter);
        if (v7)
        {
            for (i = &v7[149].padding_0[4]; v7 < i; i = &(*(iter))[149].padding_0[4])
            {
                if (v7->field_8)
                    g_1038b1f8(v7 + 1);
                v7 = &v7[4].field_8;
            }
            v0 = *(iter);
            sub_1035345e();
            *(iter) = NULL;
        }
    } while ((iter += 4, iter < &g_103a3c80));
    return;
}
```

## `sub_1035e148` `0x1035e148`

_219 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
} struct_0;

extern unsigned int g_103a301c;
extern struct_0 *g_103a3048;
extern unsigned int g_103a4cd0;
extern unsigned int g_103a4cdc;

unsigned int sub_1035e148(void)
{
    char *i;  // esi
    int v7;  // edi
    void* iter;  // edi
    char *v9;  // esi
    unsigned int v10;  // ebp
    unsigned int v11;  // eax
    unsigned int v12;  // eax
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    char *v4;  // [bp-0x14], Other Possible Types: unsigned int

    if (!g_103a4cdc)
        sub_1035b7cc();
    i = &g_103a3048->field_0;
    if (!g_103a3048)
        return 4294967295;
    for (v7 = 0; *(i); i = &i[sub_10352f20(i) + 1])
    {
        if (*(i) != 61)
            v7 += 1;
    }
    iter = sub_103574c2(v7 + 1, 4);
    g_103a301c = iter;
    if (iter)
    {
        v9 = &g_103a3048->field_0;
        while (true)
        {
            if (*(v9))
            {
                v10 = sub_10352f20(v9) + 1;
                if (*(v9) != 61)
                {
                    v11 = sub_103574c2(v10, 1);
                    *((unsigned int *)iter) = v11;
                    if (v11)
                    {
                        if (sub_10359f58(v11, v10, v9))
                        {
                            v4 = 0;
                            v3 = 0;
                            v2 = 0;
                            v1 = 0;
                            v0 = 0;
                            sub_103534f6();
                        }
                        iter += 4;
                    }
                    else
                    {
                        v4 = g_103a301c;
                        sub_1035345e();
                        g_103a301c = 0;
                        v12 = 4294967295;
                        break;
                    }
                }
                v9 = &v9[v10];
            }
            else
            {
                v4 = &g_103a3048->field_0;
                sub_1035345e();
                g_103a3048 = 0;
                *((unsigned int *)iter) = 0;
                g_103a4cd0 = 1;
                v12 = 0;
                break;
            }
        }
        return v12;
    }
    return 4294967295;
}
```

## `sub_1035e223` `0x1035e223`

_408 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
} struct_0;

struct_0 ** sub_1035e223(unsigned int a0, char *a1, struct_0 **iter, char *node, unsigned int *a4)
{
    unsigned int *i;  // ecx
    unsigned int v4;  // ebx
    unsigned int iter1;  // ecx
    char v9[2];  // eax
    char v10;  // al
    char *iter2;  // edx
    char j[2];  // esi
    unsigned int *v5;  // edi
    char v6;  // bl
    unsigned int v7;  // ebx
    char v0[2];  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v2 = a0;
    i = a4;
    v1 = v4;
    v0 = j;
    *(v5) = 0;
    j = a1;
    iter2 = node;
    *(i) = 1;
    if (iter)
    {
        iter += 1;
        *(iter) = iter2;
    }
    v2 = 0;
    do
    {
        if (j[0] == 0x22)
        {
            v6 = 0x22;
            j = &j[1];
            v2 = !v2;
            continue;
        }
        else
        {
            *(v5) = *(v5) + 1;
            if (iter2)
            {
                *(iter2) = j[0];
                node = iter2 + 1;
            }
            v6 = j[0];
            j = &j[1];
            node = node;
            if (sub_10363d76(j[0]))
            {
                *(v5) = *(v5) + 1;
                if (node)
                {
                    node += 1;
                    *(node) = j[0];
                    j = &j[1];
                }
                else
                {
                    j = &j[1];
                }
            }
            iter2 = node;
            i = a4;
            if (!v6)
            {
                j = &j[1];
                goto LABEL_1035e2b5;
            }
        }
    } while (v2 || v6 != 32 && v6 != 9);
    if (iter2)
        iter2[1] = 0;
LABEL_1035e2b5:
    for (; j[0]; i = a4)
    {
        for (v2 = 0; j[0] == 32 || j[0] == 9; j = &j[1]);
        if (!j[0])
            break;
        if (iter)
        {
            iter += 1;
            *(iter) = iter2;
            *(i) = *(i) + 1;
        }
        else
        {
            *(i) = *(i) + 1;
        }
        while (true)
        {
            v7 = 1;
            for (iter1 = 0; j[0] == 92; iter1 += 1)
            {
                j = &j[1];
            }
            if (j[0] == 0x22)
            {
                if (!((char)iter1 & 1))
                {
                    if (v2 && !((v9 = j + 1, v9[0] != 0x22)))
                    {
                        j = v9;
                    }
                    else
                    {
                        v7 = 0;
                        v2 = !v2;
                    }
                }
                iter1 >>= 1;
            }
            if (iter1)
            {
                do
                {
                    iter1 -= 1;
                    if (iter2)
                    {
                        *(iter2) = 92;
                        iter2 += 1;
                    }
                } while ((*(v5) = *(v5) + 1, iter1));
                node = iter2;
            }
            v10 = j[0];
            if (!j[0] || !v2 && (v10 == 32 || v10 == 9))
                break;
            if (v7)
            {
                if (iter2)
                {
                    node = node;
                    if (sub_10363d76(v10))
                    {
                        node += 1;
                        *(node) = j[0];
                        j = &j[1];
                        *(v5) = *(v5) + 1;
                    }
                    node += 1;
                    *(node) = j[0];
                }
                else if (sub_10363d76(v10))
                {
                    j = &j[1];
                    *(v5) = *(v5) + 1;
                }
                *(v5) = *(v5) + 1;
                iter2 = node;
            }
            j = &j[1];
        }
        if (iter2)
        {
            *(iter2) = 0;
            iter2 += 1;
            node = iter2;
        }
        *(v5) = *(v5) + 1;
    }
    if (iter)
        *(iter) = 0;
    *(i) = *(i) + 1;
    return iter;
}
```

