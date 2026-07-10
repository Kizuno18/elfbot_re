# elfbot.dll decompiled — jiru 0x102ed560..0x102f0e70

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_102ed560` `0x102ed560`

_220 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    int field_0;
    unsigned int field_4;
} struct_0;

unsigned int sub_102ed560(struct_0 *idx, int a1, int a2)
{
    int v0;  // [bp-0x14]
    char v1;  // [bp-0xd]
    unsigned int v2;  // [bp-0xc]
    int v3;  // [bp-0x8]

    v3 = a1;
    v1 = -(-(a2 < a1));
    if (v1)
    {
        v0 = a1;
        a1 = a2;
        a2 = v0;
    }
    v2 = sub_10351234(a1, a2, idx->field_4 - a2);
    if (!v2)
    {
        a1 += idx->field_4 - a2;
        a2 = idx->field_0;
        v2 = sub_10351234(a1, a2, idx->field_4 - a1);
    }
    if (!v2)
    {
        a2 += idx->field_4 - a1;
        a1 = idx->field_0;
        v2 = sub_10351234(a1, a2, v3 - a1);
    }
    if (!v1)
        return v2;
    return -(v2);
}
```

## `sub_102ed640` `0x102ed640`

_107 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    int field_0;
    unsigned int field_4;
} struct_0;

unsigned int sub_102ed640(struct_0 *idx, unsigned int index, unsigned int idx1)
{
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v0 = *((int *)(idx[3].field_0 + index * 4));
    v1 = *((int *)(idx[3].field_0 + idx1 * 4));
    return (v0 == v1 ? sub_102ed560(idx, *((int *)(idx[1].field_4 + index * 4)), *((int *)(idx[1].field_4 + idx1 * 4))) : (v0 <= v1 ? 4294967295 : 1));
}
```

## `sub_102ed6b0` `0x102ed6b0`

_651 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

int sub_102ed6b0(struct_0 *idx, int a1, int a2, unsigned int a3)
{
    unsigned int v8;  // esi
    int v9;  // eax
    unsigned int v10;  // eax
    unsigned int v0;  // [bp-0x24]
    int v1;  // [bp-0x20]
    int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x14]
    unsigned int iter[2];  // [bp-0x10], Other Possible Types: void*
    unsigned int node[2];  // [bp-0xc], Other Possible Types: void*
    int v6;  // [bp-0x8]
    unsigned int v7;  // [bp+0xc]

    v0 = v8;
    if (a1 + 2 == a2)
    {
        v9 = a1;
        if (*((int *)(idx->field_18 + v9 * 4)) > *((int *)(idx->field_18 + a1 * 4 + 4)))
            v9 = sub_102edfe0(a1, a1 + 1);
        return v9;
    }
    else
    {
        if (a1 + 3 == a2)
        {
            if (*((int *)(idx->field_18 + a1 * 4)) > *((int *)(idx->field_18 + a1 * 4 + 8)))
                sub_102edfe0(a1, a1 + 2);
            if (*((int *)(idx->field_18 + a1 * 4)) > *((int *)(idx->field_18 + a1 * 4 + 4)))
            {
                sub_102edfe0(a1, a1 + 1);
            }
            else if (*((int *)(idx->field_18 + a1 * 4 + 4)) > *((int *)(idx->field_18 + a1 * 4 + 8)))
            {
                sub_102edfe0(a1 + 1, a1 + 2);
            }
        }
        iter = idx->field_18 + a1 * 4;
        node = idx->field_18 + a2 * 4;
        v10 = iter[0];
        v3 = iter[0];
        for (iter = &iter[1]; iter < node && (v10 = (unsigned int)iter, *((int *)v10) >= v3); iter = &iter[1])
        {
            v10 = iter[0];
            v3 = iter[0];
        }
        if (iter == node)
            return v10;
        iter = idx->field_18 + a1 * 4;
        while (true)
        {
            for (node = idx->field_18 + a2 * 4 - 4; iter < node && !(*((int *)iter) & a3); iter += 4);
            for (; node > iter && (*((int *)node) & a3); node -= 4);
            if (iter >= node)
                break;
            v2 = node - idx->field_18 >> 2;
            v1 = iter - idx->field_18 >> 2;
            sub_102edfe0(v1, v2);
            iter += 4;
            node -= 4;
        }
        for (node = idx->field_18 + a2 * 4; iter < node && !(*((int *)iter) & a3); iter += 4);
        v6 = iter - idx->field_18 >> 2;
        v7 = a3 >> 1;
        if (!(a3 & 4294967294))
            return a3 >> 1;
        if (a1 + 1 >= v6)
            return sub_102ed6b0(idx, v6, a2, v7);
        sub_102ed6b0(idx, a1, v6, v7);
        return sub_102ed6b0(idx, v6, a2, v7);
    }
}
```

## `sub_102ed6f8` `0x102ed6f8`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102ed6f8(void)
{
}
```

## `sub_102ed940` `0x102ed940`

_868 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_102ed940(unsigned int *idx, int a1, int a2, int a3)
{
    unsigned int v9;  // esi
    unsigned int *v10;  // eax
    unsigned int *v11;  // eax
    unsigned int v0;  // [bp-0x2c]
    unsigned int v1;  // [bp-0x28]
    unsigned int v2;  // [bp-0x24]
    int v3;  // [bp-0x1c]
    unsigned int v4;  // [bp-0x18]
    unsigned int *iter;  // [bp-0x14]
    unsigned int *v6;  // [bp-0x10]
    int node;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]

    v0 = v9;
    if (a1 + 2 == a2)
    {
        v10 = sub_102ed560(idx, *((int *)(idx[3] + a1 * 4)), *((int *)(idx[3] + a1 * 4 + 4)));
        if (v10 > 0)
            v10 = sub_102edfe0(a1, a1 + 1);
        return v10;
    }
    else if (a1 + 3 == a2)
    {
        if (sub_102ed560(idx, *((int *)(idx[3] + a1 * 4)), *((int *)(idx[3] + a1 * 4 + 8))) > 0)
            sub_102edfe0(a1, a1 + 2);
        if (sub_102ed560(idx, *((int *)(idx[3] + a1 * 4)), *((int *)(idx[3] + a1 * 4 + 4))) > 0)
        {
            v11 = sub_102edfe0(a1, a1 + 1);
        }
        else
        {
            v11 = sub_102ed560(idx, *((int *)(idx[3] + a1 * 4 + 4)), *((int *)(idx[3] + a1 * 4 + 8)));
            if (v11 > 0)
                v11 = sub_102edfe0(a1 + 1, a1 + 2);
        }
        return v11;
    }
    else
    {
        if (a3)
        {
            while (true)
            {
                iter = idx[6] + a1 * 4;
                v6 = idx[6] + a2 * 4;
                for (node = a1; iter < v6; node += 1)
                {
                    v2 = *((int *)(idx[3] + node * 4));
                    *(iter) = sub_102ee060(v2, a3);
                    iter += 1;
                }
                sub_102ed6b0(idx, a1, a2, 0x80000000);
                if (*((int *)(idx[6] + a1 * 4)) != *((int *)(idx[6] + a2 * 4 - 4)))
                    break;
                a3 += 4;
            }
        }
        else
        {
            iter = idx[6] + a1 * 4;
            v6 = idx[6] + a2 * 4;
            for (node = a1; iter < v6; node += 1)
            {
                v1 = *((int *)(idx[3] + node * 4));
                *(iter) = sub_102edf80(v1);
                iter += 1;
            }
            sub_102ed6b0(idx, a1, a2, 0x80000000);
        }
        iter = idx[6] + a1 * 4;
        v6 = idx[6] + a2 * 4;
        node = a1 + 1;
        v4 = *(iter);
        iter += 1;
        v8 = 0;
        while (iter < v6)
        {
            v3 = v6 - iter >> 2;
            for (v3 = (v3 <= 0x100 ? v3 + node : node + 0x100); node < v3; node += 1)
            {
                if (*(iter) == v4)
                {
                    v8 += 1;
                    iter += 1;
                }
                else
                {
                    if (v8)
                    {
                        sub_102ed940(idx, node - (v8 + 1), node, a3 + 4);
                        v8 = 0;
                    }
                    v4 = *(iter);
                    iter += 1;
                }
            }
        }
        if (!v8)
            return iter;
        sub_102ed940(idx, a2 - (v8 + 1), a2, a3 + 4);
        return iter;
    }
}
```

## `sub_102ed994` `0x102ed994`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102ed994(void)
{
}
```

## `sub_102edcb0` `0x102edcb0`

_603 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_1 *field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
    unsigned int field_10;
    unsigned int field_14;
    unsigned int field_18;
} struct_0;

typedef struct struct_1 {
    char field_0;
} struct_1;

struct_0 * sub_102edcb0(struct_0 *idx, char *a1, unsigned int a2, unsigned int a3)
{
    struct_0 *v8;  // eax
    unsigned int v0;  // [bp-0x81c]
    struct_0 *k;  // [bp-0x818]
    char *v2;  // [bp-0x814]
    unsigned int v3;  // [bp-0x810]
    int index;  // [bp-0x80c]
    char *i;  // [bp-0x808]
    char v6;  // [bp-0x804]
    char v7;  // [bp-0x404]

    idx->field_10 = a2;
    idx->field_0 = a1;
    idx->field_4 = &idx->field_0[idx->field_10];
    idx->field_8 = idx->field_4 - 4;
    idx->field_c = a3;
    idx->field_14 = 0;
    v0 = sub_1034fef0(-((idx->field_10 >= 0x20000000 ? 1 : 0) & 1) | idx->field_10 * 4, idx);
    idx->field_18 = v0;
    sub_10350ad0(&v6, 0, 0x400);
    for (i = &idx->field_0->field_0; i < idx->field_4; i += 1)
    {
        *((unsigned int *)&(&v6)[4 * *(i)]) = *((int *)&(&v6)[4 * *(i)]) + 1;
    }
    index = 0;
    for (v3 = 0; index < 0x100; index += 1)
    {
        *((unsigned int *)&(&v7)[4 * index]) = v3;
        v3 += *((int *)&(&v6)[4 * index]);
    }
    v2 = &idx->field_0->field_0;
    while (true)
    {
        v8 = idx;
        if (v2 >= v8->field_4)
            break;
        *((char **)(idx->field_c + *((int *)&(&v7)[4 * *(v2)]) * 4)) = v2;
        *((unsigned int *)&(&v7)[4 * *(v2)]) = *((int *)&(&v7)[4 * *(v2)]) + 1;
        v2 += 1;
    }
    for (k = NULL; k < 0x100; k = (char *)&k->field_0 + 1)
    {
        v8 = k;
        if (*((int *)(&v6 + 0x4 * v8)) > 1)
            v8 = sub_102ed940(idx, *((int *)(&v7 + 0x4 * k)) - *((int *)(&v6 + 0x4 * k)), *((int *)(&v7 + 0x4 * k)), 0);
    }
    return v8;
}
```

## `sub_102edf10` `0x102edf10`

_102 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_1 *field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
    unsigned int field_10;
    unsigned int field_14;
    unsigned int field_18;
} struct_0;

typedef struct struct_1 {
    char field_0;
} struct_1;

extern unsigned int g_1038e180;

unsigned int sub_102edf10(char *a0, unsigned int a1, unsigned int a2)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4135
    unsigned long v10;  // 4149
    unsigned int v11;  // eax
    unsigned long v12;  // 4113
    struct_0 v0;  // [bp-0x2c]
    int v1;  // [bp-0x28]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_10369dd8;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_102ee080(g_1038e180 ^ &v5);
    v4 = 0;
    sub_102edcb0(&v0, a0, a1, a2);
    v4 = 4294967295;
    v11 = sub_102ee0a0(g_1038e180 ^ &v5, v0, v1);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v2;
    return v11;
}
```

## `sub_102edf80` `0x102edf80`

_82 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    struct struct_1 *field_8;
} struct_0;

typedef struct struct_1 {
    char field_0;
    char field_1;
    char field_2;
    char field_3;
} struct_1;

unsigned int sub_102edf80(struct_0 *a0, char *a1)
{
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return (a1 < v0->field_8 ? *(a1) * 0x1000000 | a1[1] * 0x10000 | a1[2] * 0x100 | a1[3] : sub_102ed4b0(v0, a1, 0));
}
```

## `sub_102edfbe` `0x102edfbe`

_2 bytes. (leaf/helper — see body)_

```c
void sub_102edfbe(void)
{
}
```

## `sub_102edfe0` `0x102edfe0`

_127 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102edfe0(unsigned int *idx, unsigned int a1, unsigned int a2)
{
    unsigned int v6;  // eax
    unsigned int v0;  // [bp-0x1c]
    unsigned int *v1;  // [bp-0x18]
    unsigned int *v2;  // [bp-0x14]
    unsigned int *v3;  // [bp-0x10]
    unsigned int *v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = idx[3] + a1 * 4;
    v3 = idx[3] + a2 * 4;
    v0 = *(v4);
    *(v4) = *(v3);
    *(v3) = v0;
    v1 = idx[6] + a1 * 4;
    v2 = idx[6] + a2 * 4;
    v5 = *(v1);
    v6 = *(v2);
    *(v1) = v6;
    *(v2) = v5;
    return v6;
}
```

## `sub_102ee060` `0x102ee060`

_29 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102ee060(char **a0, char *a1, unsigned int a2)
{
    char **v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_102ed4b0(v0, a1, a2);
}
```

## `sub_102ee080` `0x102ee080`

_24 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

struct_0 * sub_102ee080(struct_0 *a0)
{
    a0->field_18 = 0;
    return a0;
}
```

## `sub_102ee0a0` `0x102ee0a0`

_34 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

int sub_102ee0a0(struct_0 *a0)
{
    char v0;  // [bp+0x0]

    return sub_10350eb5(a0->field_18, a0, a0->field_18, &v0);
}
```

## `sub_102ee0d0` `0x102ee0d0`

_112 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    struct struct_1 *field_8;
    struct struct_1 *field_c;
    unsigned int field_10;
    char field_14;
    char field_15;
    char field_16;
} struct_0;

typedef struct struct_1 {
    char field_0;
} struct_1;

extern char g_103a17b4;

int sub_102ee0d0(int a0, char *a1, void* a2, unsigned int a3)
{
    struct_0 v0;  // [bp-0x1c]

    g_103a17b4 = 0;
    sub_102eb000(&v0, a1, a3, 1);
    sub_102ee140(a0, *((int *)a2), &v0);
    *((unsigned int *)a2) = sub_102eeb60() + 7 >> 3;
    if ((char)sub_102eeb40())
        g_103a17b4 = 1;
    return -(0 < g_103a17b4) + 1;
}
```

## `sub_102ee140` `0x102ee140`

_151 bytes. (leaf/helper — see body)_

```c
int sub_102ee140(char *a0, unsigned int a1, int a2)
{
    char v0;  // [bp-0x244d]
    char v1;  // [bp-0x244c]
    char *v2;  // [bp-0xc]
    char *iter;  // [bp-0x8]

    iter = a0;
    v2 = &iter[a1];
    sub_102ee1e0(&v1);
    while (iter < v2)
    {
        v0 = *(iter);
        iter += 1;
        sub_102ee2e0(&v1, v0, a2);
        sub_102ee3a0(&v1, v0);
    }
    return sub_102ee2e0(&v1, 0x100, a2);
}
```

## `sub_102ee1e0` `0x102ee1e0`

_245 bytes. (leaf/helper — see body)_

```c
unsigned int [271] sub_102ee1e0(unsigned int *idx)
{
    unsigned int v1;  // ecx
    unsigned int v2[271];  // eax
    unsigned int index[271];  // [bp-0x8], Other Possible Types: unsigned int

    index = v1;
    idx[262] = 1;
    idx[261] = 0;
    idx[259] = 2;
    idx[260] = 4294967295;
    idx[266] = 0x100;
    idx[265] = 1;
    idx[263] = 1;
    idx[264] = 0;
    idx[0x100] = 1;
    idx[270] = 0x101;
    idx[269] = 1;
    idx[267] = 1;
    idx[268] = 0;
    idx[0x101] = 2;
    idx[258] = 3;
    for (index = NULL; index < 0x100; index = (char *)&index[0] + 1)
    {
        *((unsigned int *)((char *)idx + 0x4 * index)) = 4294967295;
    }
    return v2;
}
```

## `sub_102ee2e0` `0x102ee2e0`

_180 bytes. (leaf/helper — see body)_

```c
unsigned int [258] sub_102ee2e0(unsigned int *a0, unsigned int idx, unsigned int a2)
{
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int i;  // [bp-0x8]

    v1 = 0;
    v2 = 1;
    v0 = 0;
    i = a0[idx];
    if (i == 4294967295)
        i = a0[0x101];
    for (; i; i = a0[260 + 4 * i])
    {
        if (!((char)i & 1))
            v1 |= v2;
        v2 *= 2;
        v0 += 1;
    }
    sub_102eb110(a2, v1, v0);
    if (a0[idx] != 4294967295)
        return a0;
    sub_102eb110(a2, idx, 8);
    return sub_102ee8a0(a0, idx);
}
```

## `sub_102ee3a0` `0x102ee3a0`

_218 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[1036];
    unsigned int field_40c;
} struct_0;

unsigned int sub_102ee3a0(struct_0 *a0, unsigned int idx)
{
    unsigned int v2;  // eax
    unsigned int i;  // [bp-0xc]
    unsigned int iter;  // [bp-0x8]

    if (a0->field_40c == 0x8000)
        sub_102ee480(a0);
    v2 = a0;
    for (i = *((int *)(v2 + idx * 4)); i != 4294967295; i = *((int *)&a0[1].padding_0[v2]))
    {
        (&a0->field_40c)[4 * i] = (&a0->field_40c)[4 * i] + 1;
        for (iter = i; iter > 0 && *((int *)&a0->padding_0[0x3fc + 16 * iter]) < (&a0->field_40c)[4 * i]; iter -= 1);
        if (i != iter)
        {
            sub_102ee700(a0, i, iter);
            i = iter;
        }
        v2 = i * 16;
    }
    return v2;
}
```

## `sub_102ee480` `0x102ee480`

_632 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
    char padding_4[1028];
    unsigned int field_408;
} struct_0;

struct_0 * sub_102ee480(struct_0 *idx)
{
    unsigned int index[263];  // edx
    unsigned int idx1[263];  // eax
    struct_0 *v6;  // eax
    struct_0 *iter;  // [bp-0x14]
    struct_0 *node;  // [bp-0x10], Other Possible Types: unsigned int
    unsigned int v2;  // [bp-0xc]
    struct_0 *iter1;  // [bp-0x8]

    iter = idx->field_408 - 1;
    for (iter1 = iter; iter1 >= NULL; iter1 = (char *)&iter1->field_0 + 1)
    {
        if (*((int *)(1044 + (char *)idx + 0x10 * iter1)))
        {
            index = 1036 + (char *)idx + 0x10 * iter1;
            idx1 = 1036 + (char *)idx + 0x10 * iter;
            idx1[0] = index[0];
            idx1[1] = index[1];
            idx1[2] = index[2];
            idx1[3] = index[3];
            *((unsigned int *)(1036 + (char *)idx + 0x10 * iter)) = *((int *)(1036 + (char *)idx + 0x10 * iter)) + 1 >> 1;
            iter = (char *)&iter->field_0 + 1;
        }
    }
    v6 = idx;
    for (iter1 = v6->field_408 - 2; iter >= NULL; iter = (char *)&iter->field_0 + 1)
    {
        node = (char *)&iter1->field_0 + 1;
        *((struct struct_0 **)(1036 + (char *)idx + 0x10 * iter)) = *((int *)(1036 + (char *)idx + 0x10 * iter1)) + (char *)(&idx[1].field_0)[4 * node];
        v2 = *((int *)(1036 + (char *)idx + 0x10 * iter));
        *((unsigned int *)(1044 + (char *)idx + 0x10 * iter)) = 0;
        for (node = (char *)&iter->field_0 + 1; v2 < (&idx[1].field_0)[4 * node]; node += 1);
        node -= 1;
        sub_10350ec0(1036 + (char *)idx + 0x10 * iter, 1052 + (char *)idx + 0x10 * &iter->field_0, (node - iter) * 16);
        *((unsigned int *)(1036 + (char *)idx + 0x10 * node)) = v2;
        *((struct_0 **)(1048 + (char *)idx + 0x10 * node)) = iter1;
        *((unsigned int *)(1044 + (char *)idx + 0x10 * node)) = 0;
        iter1 = (char *)&iter1->field_0 + 2;
    }
    for (iter1 = idx->field_408 - 1; iter1 >= NULL; iter1 = (char *)&iter1->field_0 + 1)
    {
        if (*((int *)(1044 + (char *)idx + 0x10 * iter1)))
        {
            node = *((int *)(1048 + (char *)idx + 0x10 * iter1));
            (&idx->field_0)[node] = iter1;
        }
        else
        {
            node = *((int *)(1048 + (char *)idx + 0x10 * iter1));
            *((struct_0 **)&idx[1].padding_4[16 + 16 * node]) = iter1;
            *((struct_0 **)&idx[1].padding_4[16 * node]) = iter1;
        }
    }
    return v6;
}
```

## `sub_102ee700` `0x102ee700`

_406 bytes. (leaf/helper — see body)_

```c
int sub_102ee700(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int idx[263];  // eax
    unsigned int idx1[263];  // edx
    unsigned int index[263];  // eax
    unsigned int idx2[263];  // edx
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    if (*((int *)(a0 + a1 * 16 + 1044)))
    {
        *((unsigned int *)(a0 + *((int *)(a0 + a1 * 16 + 1048)) * 4)) = a2;
    }
    else
    {
        *((unsigned int *)(a0 + *((int *)(a0 + a1 * 16 + 1048)) * 16 + 1040)) = a2;
        *((unsigned int *)(a0 + (*((int *)(a0 + a1 * 16 + 1048)) + 1) * 16 + 1040)) = a2;
    }
    if (*((int *)(a0 + a2 * 16 + 1044)))
    {
        *((unsigned int *)(a0 + *((int *)(a0 + a2 * 16 + 1048)) * 4)) = a1;
    }
    else
    {
        *((unsigned int *)(a0 + *((int *)(a0 + a2 * 16 + 1048)) * 16 + 1040)) = a1;
        *((unsigned int *)(a0 + (*((int *)(a0 + a2 * 16 + 1048)) + 1) * 16 + 1040)) = a1;
    }
    idx = a0 + a1 * 16 + 1036;
    v0 = idx[0];
    v1 = idx[1];
    v2 = idx[2];
    v3 = idx[3];
    idx1 = a0 + a2 * 16 + 1036;
    index = a0 + a1 * 16 + 1036;
    index[0] = idx1[0];
    index[1] = idx1[1];
    index[2] = idx1[2];
    index[3] = idx1[3];
    *((unsigned int *)(a0 + a1 * 16 + 1040)) = v1;
    v1 = *((int *)(a0 + a2 * 16 + 1040));
    idx2 = a0 + a2 * 16 + 1036;
    idx2[0] = v0;
    idx2[1] = v1;
    idx2[2] = v2;
    idx2[3] = v3;
    return v2;
}
```

## `sub_102ee8a0` `0x102ee8a0`

_300 bytes. (leaf/helper — see body)_

```c
unsigned int [259] sub_102ee8a0(unsigned int *idx, unsigned int idx1)
{
    unsigned int idx2[263];  // edx
    unsigned int index[263];  // eax
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v0 = idx[258] - 1;
    v2 = idx[258];
    v1 = idx[258] + 1;
    idx[258] = idx[258] + 2;
    idx2 = &idx[4 * v0 + 259];
    index = &idx[4 * v2 + 259];
    index[0] = idx2[0];
    index[1] = idx2[1];
    index[2] = idx2[2];
    index[3] = idx2[3];
    idx[260 + 4 * v2] = v0;
    idx[idx[262 + 4 * v2]] = v2;
    idx[262 + 4 * v0] = v2;
    idx[261 + 4 * v0] = 0;
    idx[262 + 4 * v1] = idx1;
    idx[261 + 4 * v1] = 1;
    idx[259 + 4 * v1] = 0;
    idx[260 + 4 * v1] = v0;
    idx[idx1] = v1;
    return idx;
}
```

## `sub_102ee9d0` `0x102ee9d0`

_76 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    struct struct_1 *field_8;
    struct struct_1 *field_c;
    unsigned int field_10;
    char field_14;
    char field_15;
    char field_16;
} struct_0;

typedef struct struct_1 {
    char field_0;
} struct_1;

extern char g_103a17b4;

int sub_102ee9d0(char *a0, int a1, unsigned int *a2, int a3)
{
    struct_0 v0;  // [bp-0x1c]

    g_103a17b4 = 0;
    sub_102eb000(&v0, a0, *(a2), 0);
    *(a2) = sub_102eea20(&v0, a1, a3);
    return -(0 < g_103a17b4) + 1;
}
```

## `sub_102eea20` `0x102eea20`

_144 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[1036];
    unsigned int field_40c;
} struct_0;

char * sub_102eea20(int a0, char *a1, unsigned int a2)
{
    unsigned int v0;  // [bp-0x2450]
    struct_0 v1;  // [bp-0x244c]
    char *iter;  // [bp-0xc]
    char *v3;  // [bp-0x8]

    iter = a1;
    v3 = &iter[a2];
    sub_102ee1e0(&v1);
    while (iter < v3 && (v0 = sub_102eeab0(&v1, a0), v0 != 0x100))
    {
        *(iter) = v0;
        iter += 1;
        sub_102ee3a0(&v1, v0);
    }
    return iter - a1;
}
```

## `sub_102eeab0` `0x102eeab0`

_134 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102eeab0(unsigned int *a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0xc]
    unsigned int i;  // [bp-0x8]

    for (i = 0; !a0[261 + 4 * i]; i += sub_102eb190(a1))
    {
        i = a0[262 + 4 * i];
    }
    v0 = a0[262 + 4 * i];
    if (v0 != 0x101)
        return v0;
    v0 = sub_102eb0b0(a1, 8);
    sub_102ee8a0(a0, v0);
    return v0;
}
```

## `sub_102eeb40` `0x102eeb40`

_17 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[21];
    char field_15;
} struct_0;

int sub_102eeb40(struct_0 *a0)
{
    return _INSERT(a0, 0, a0->field_15);
}
```

## `sub_102eeb60` `0x102eeb60`

_73 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    char field_4;
    char padding_5[7];
    unsigned int field_c;
    char padding_10[4];
    char field_14;
} struct_0;

int sub_102eeb60(struct_0 *a0)
{
    unsigned int v2;  // eax
    unsigned int v3;  // eax
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    v2 = sub_102eb070(v0->field_4);
    v3 = sub_102eb070(v0->field_14);
    return v2 + (v0->field_c - (v0->field_0 + 1)) * 8 + 8 - v3;
}
```

## `sub_102eebb0` `0x102eebb0`

_415 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102eebb0(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 1646658810;
    a0 = sub_102f2bf0(a0, 5, &v0);
    a0 ^= 1091465309;
    a0 = sub_102f2c20(a0, 10, 3, 7);
    a0 = sub_102f2d00(a0, 12, 5);
    a0 ^= 3150139645;
    a0 = sub_102f2d00(a0, 15, 16);
    a0 = sub_102f2c20(a0, 13, 6, 11);
    a0 = sub_102f2d00(a0, 4, 2);
    a0 = sub_102f2c20(a0, 22, 3, 8);
    a0 = sub_102f2d00(a0, 21, 3);
    a0 = sub_102f2c20(a0, 3, 18, 2);
    a0 = sub_102f2d00(a0, 12, 9);
    a0 = sub_102f2c20(a0, 31, 0, 25);
    a0 = sub_102f2d00(a0, 0x11, 5);
    a0 = sub_102f2bf0(a0, 30);
    a0 = sub_102f2d00(a0, 3, 1);
    a0 = sub_102f2ca0(a0, 6, 14);
    a0 ^= 592828697;
    a0 = sub_102f2bf0(a0, 24);
    a0 = sub_102f2c20(a0, 25, 3, 13);
    a0 ^= 2309325724;
    a0 = sub_102f2c20(a0, 5, 8, 3);
    return a0;
}
```

## `sub_102eed50` `0x102eed50`

_418 bytes. (leaf/helper — see body)_

```c
int sub_102eed50(int a0)
{
    char v0;  // [bp+0x0]

    a0 = sub_102f2c20(a0, 5, 8, -3, &v0);
    a0 ^= 2309325724;
    a0 = sub_102f2c20(a0, 25, 3, -13);
    a0 = sub_102f2bf0(a0, -24);
    a0 ^= 592828697;
    a0 = sub_102f2ca0(a0, 6, 14);
    a0 = sub_102f2d00(a0, 3, 1);
    a0 = sub_102f2bf0(a0, -30);
    a0 = sub_102f2d00(a0, 0x11, 5);
    a0 = sub_102f2c20(a0, 31, 0, -25);
    a0 = sub_102f2d00(a0, 12, 9);
    a0 = sub_102f2c20(a0, 3, 18, -2);
    a0 = sub_102f2d00(a0, 21, 3);
    a0 = sub_102f2c20(a0, 22, 3, -0x8);
    a0 = sub_102f2d00(a0, 4, 2);
    a0 = sub_102f2c20(a0, 13, 6, -11);
    a0 = sub_102f2d00(a0, 15, 16);
    a0 ^= 3150139645;
    a0 = sub_102f2d00(a0, 12, 5);
    a0 = sub_102f2c20(a0, 10, 3, -7);
    a0 ^= 1091465309;
    a0 = sub_102f2bf0(a0, -5);
    a0 ^= 1646658810;
    return a0;
}
```

## `sub_102eef00` `0x102eef00`

_287 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102eef00(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 1655224037;
    a0 = sub_102f2ca0(a0, 7, 10, &v0);
    a0 = sub_102f2c20(a0, 12, 12, 4);
    a0 = sub_102f2ca0(a0, 1, 12);
    a0 ^= 1476301873;
    a0 = sub_102f2c20(a0, 26, 4, 24);
    a0 = sub_102f2bf0(a0, 10);
    a0 = sub_102f2c20(a0, 27, 1, 24);
    a0 ^= 1013248778;
    a0 = sub_102f2bf0(a0, 16);
    a0 = sub_102f2c20(a0, 23, 0, 4);
    a0 = sub_102f2d00(a0, 2, 12);
    a0 = sub_102f2ca0(a0, 7, 11);
    a0 ^= 3525813092;
    a0 = sub_102f2bf0(a0, 15);
    a0 = sub_102f2c20(a0, 28, 0, 25);
    return a0;
}
```

## `sub_102ef020` `0x102ef020`

_287 bytes. (leaf/helper — see body)_

```c
int sub_102ef020(int a0)
{
    char v0;  // [bp+0x0]

    a0 = sub_102f2c20(a0, 28, 0, -25, &v0);
    a0 = sub_102f2bf0(a0, -15);
    a0 ^= 3525813092;
    a0 = sub_102f2ca0(a0, 7, 11);
    a0 = sub_102f2d00(a0, 2, 12);
    a0 = sub_102f2c20(a0, 23, 0, -0x4);
    a0 = sub_102f2bf0(a0, -0x10);
    a0 ^= 1013248778;
    a0 = sub_102f2c20(a0, 27, 1, -24);
    a0 = sub_102f2bf0(a0, -10);
    a0 = sub_102f2c20(a0, 26, 4, -24);
    a0 ^= 1476301873;
    a0 = sub_102f2ca0(a0, 1, 12);
    a0 = sub_102f2c20(a0, 12, 12, -0x4);
    a0 = sub_102f2ca0(a0, 7, 10);
    a0 ^= 1655224037;
    return a0;
}
```

## `sub_102ef140` `0x102ef140`

_291 bytes. (leaf/helper — see body)_

```c
int sub_102ef140(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 933374301;
    a0 = sub_102f2c20(a0, 28, 0, 15, &v0);
    a0 = sub_102f2bf0(a0, 27);
    a0 ^= 2782158571;
    a0 = sub_102f2d00(a0, 20, 2);
    a0 = sub_102f2c20(a0, 21, 0, 4);
    a0 ^= 3275186556;
    a0 = sub_102f2bf0(a0, 20);
    a0 = sub_102f2d00(a0, 8, 5);
    a0 = sub_102f2bf0(a0, 29);
    a0 = sub_102f2d00(a0, 19, 10);
    a0 = sub_102f2c20(a0, 12, 14, 7);
    a0 = sub_102f2d00(a0, 10, 2);
    a0 ^= 3917727009;
    a0 = sub_102f2ca0(a0, 7, 0x11);
    a0 = sub_102f2bf0(a0, 22);
    a0 ^= 139910844;
    return a0;
}
```

## `sub_102ef270` `0x102ef270`

_292 bytes. (leaf/helper — see body)_

```c
int sub_102ef270(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 139910844;
    a0 = sub_102f2bf0(a0, -22, &v0);
    a0 = sub_102f2ca0(a0, 7, 0x11);
    a0 ^= 3917727009;
    a0 = sub_102f2d00(a0, 10, 2);
    a0 = sub_102f2c20(a0, 12, 14, -7);
    a0 = sub_102f2d00(a0, 19, 10);
    a0 = sub_102f2bf0(a0, -29);
    a0 = sub_102f2d00(a0, 8, 5);
    a0 = sub_102f2bf0(a0, -20);
    a0 ^= 3275186556;
    a0 = sub_102f2c20(a0, 21, 0, -0x4);
    a0 = sub_102f2d00(a0, 20, 2);
    a0 ^= 2782158571;
    a0 = sub_102f2bf0(a0, -27);
    a0 = sub_102f2c20(a0, 28, 0, -15);
    a0 ^= 933374301;
    return a0;
}
```

## `sub_102ef3a0` `0x102ef3a0`

_192 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102ef3a0(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 4019980981;
    a0 = sub_102f2ca0(a0, 4, 21, &v0);
    a0 = sub_102f2d00(a0, 20, 9);
    a0 ^= 167786298;
    a0 = sub_102f2d00(a0, 4, 16);
    a0 ^= 4293943382;
    a0 = sub_102f2c20(a0, 24, 4, 5);
    a0 = sub_102f2bf0(a0, 19);
    a0 = sub_102f2ca0(a0, 2, 10);
    a0 = sub_102f2bf0(a0, 9);
    a0 = sub_102f2ca0(a0, 7, 15);
    return a0;
}
```

## `sub_102ef460` `0x102ef460`

_194 bytes. (leaf/helper — see body)_

```c
int sub_102ef460(int a0)
{
    char v0;  // [bp+0x0]

    a0 = sub_102f2ca0(a0, 7, 15, &v0);
    a0 = sub_102f2bf0(a0, -9);
    a0 = sub_102f2ca0(a0, 2, 10);
    a0 = sub_102f2bf0(a0, -19);
    a0 = sub_102f2c20(a0, 24, 4, -5);
    a0 ^= 4293943382;
    a0 = sub_102f2d00(a0, 4, 16);
    a0 ^= 167786298;
    a0 = sub_102f2d00(a0, 20, 9);
    a0 = sub_102f2ca0(a0, 4, 21);
    a0 ^= 4019980981;
    return a0;
}
```

## `sub_102ef530` `0x102ef530`

_269 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102ef530(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 4201368960;
    a0 = sub_102f2d00(a0, 0x11, 7, &v0);
    a0 = sub_102f2ca0(a0, 7, 20);
    a0 = sub_102f2bf0(a0, 28);
    a0 = sub_102f2c20(a0, 7, 1, 3);
    a0 ^= 169040055;
    a0 = sub_102f2c20(a0, 24, 0, 5);
    a0 = sub_102f2d00(a0, 23, 2);
    a0 ^= 4232910574;
    a0 = sub_102f2ca0(a0, 8, 16);
    a0 = sub_102f2bf0(a0, 16);
    a0 = sub_102f2d00(a0, 22, 8);
    a0 = sub_102f2ca0(a0, 4, 20);
    a0 = sub_102f2bf0(a0, 11);
    a0 = sub_102f2d00(a0, 16, 4);
    return a0;
}
```

## `sub_102ef640` `0x102ef640`

_268 bytes. (leaf/helper — see body)_

```c
int sub_102ef640(int a0)
{
    char v0;  // [bp+0x0]

    a0 = sub_102f2d00(a0, 16, 4, &v0);
    a0 = sub_102f2bf0(a0, -11);
    a0 = sub_102f2ca0(a0, 4, 20);
    a0 = sub_102f2d00(a0, 22, 8);
    a0 = sub_102f2bf0(a0, -0x10);
    a0 = sub_102f2ca0(a0, 8, 16);
    a0 ^= 4232910574;
    a0 = sub_102f2d00(a0, 23, 2);
    a0 = sub_102f2c20(a0, 24, 0, -5);
    a0 ^= 169040055;
    a0 = sub_102f2c20(a0, 7, 1, -3);
    a0 = sub_102f2bf0(a0, -28);
    a0 = sub_102f2ca0(a0, 7, 20);
    a0 = sub_102f2d00(a0, 0x11, 7);
    a0 ^= 4201368960;
    return a0;
}
```

## `sub_102ef750` `0x102ef750`

_377 bytes. (leaf/helper — see body)_

```c
int sub_102ef750(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 1633304884;
    a0 = sub_102f2d00(a0, 3, 21, &v0);
    a0 = sub_102f2c20(a0, 22, 3, 12);
    a0 = sub_102f2bf0(a0, 27);
    a0 = sub_102f2c20(a0, 12, 13, 9);
    a0 = sub_102f2bf0(a0, 0x11);
    a0 = sub_102f2d00(a0, 10, 16);
    a0 ^= 192571826;
    a0 = sub_102f2d00(a0, 18, 1);
    a0 = sub_102f2bf0(a0, 30);
    a0 = sub_102f2c20(a0, 9, 1, 4);
    a0 = sub_102f2ca0(a0, 2, 22);
    a0 = sub_102f2bf0(a0, 31);
    a0 = sub_102f2d00(a0, 8, 20);
    a0 = sub_102f2c20(a0, 22, 8, 0x11);
    a0 ^= 3554372988;
    a0 = sub_102f2d00(a0, 20, 10);
    a0 = sub_102f2c20(a0, 15, 4, 11);
    a0 = sub_102f2bf0(a0, 11);
    a0 = sub_102f2ca0(a0, 5, 20);
    a0 ^= 2189619859;
    return a0;
}
```

## `sub_102ef8d0` `0x102ef8d0`

_378 bytes. (leaf/helper — see body)_

```c
int sub_102ef8d0(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 2189619859;
    a0 = sub_102f2ca0(a0, 5, 20, &v0);
    a0 = sub_102f2bf0(a0, -11);
    a0 = sub_102f2c20(a0, 15, 4, -11);
    a0 = sub_102f2d00(a0, 20, 10);
    a0 ^= 3554372988;
    a0 = sub_102f2c20(a0, 22, 8, -17);
    a0 = sub_102f2d00(a0, 8, 20);
    a0 = sub_102f2bf0(a0, -31);
    a0 = sub_102f2ca0(a0, 2, 22);
    a0 = sub_102f2c20(a0, 9, 1, -0x4);
    a0 = sub_102f2bf0(a0, -30);
    a0 = sub_102f2d00(a0, 18, 1);
    a0 ^= 192571826;
    a0 = sub_102f2d00(a0, 10, 16);
    a0 = sub_102f2bf0(a0, -17);
    a0 = sub_102f2c20(a0, 12, 13, -9);
    a0 = sub_102f2bf0(a0, -27);
    a0 = sub_102f2c20(a0, 22, 3, -12);
    a0 = sub_102f2d00(a0, 3, 21);
    a0 ^= 1633304884;
    return a0;
}
```

## `sub_102efa50` `0x102efa50`

_335 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102efa50(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 3617845311;
    a0 = sub_102f2bf0(a0, 29, &v0);
    a0 = sub_102f2c20(a0, 24, 6, 20);
    a0 = sub_102f2bf0(a0, 16);
    a0 = sub_102f2ca0(a0, 1, 11);
    a0 ^= 2629160650;
    a0 = sub_102f2c20(a0, 15, 16, 10);
    a0 = sub_102f2bf0(a0, 0x11);
    a0 ^= 1359884984;
    a0 = sub_102f2ca0(a0, 2, 12);
    a0 = sub_102f2c20(a0, 9, 7, 6);
    a0 = sub_102f2ca0(a0, 5, 19);
    a0 = sub_102f2bf0(a0, 30);
    a0 = sub_102f2d00(a0, 26, 2);
    a0 = sub_102f2ca0(a0, 3, 12);
    a0 ^= 692010110;
    a0 = sub_102f2d00(a0, 30, 1);
    a0 = sub_102f2ca0(a0, 8, 10);
    a0 = sub_102f2bf0(a0, 1);
    return a0;
}
```

## `sub_102efba0` `0x102efba0`

_335 bytes. (leaf/helper — see body)_

```c
int sub_102efba0(int a0)
{
    char v0;  // [bp+0x0]

    a0 = sub_102f2bf0(a0, -1, &v0);
    a0 = sub_102f2ca0(a0, 8, 10);
    a0 = sub_102f2d00(a0, 30, 1);
    a0 ^= 692010110;
    a0 = sub_102f2ca0(a0, 3, 12);
    a0 = sub_102f2d00(a0, 26, 2);
    a0 = sub_102f2bf0(a0, -30);
    a0 = sub_102f2ca0(a0, 5, 19);
    a0 = sub_102f2c20(a0, 9, 7, -6);
    a0 = sub_102f2ca0(a0, 2, 12);
    a0 ^= 1359884984;
    a0 = sub_102f2bf0(a0, -17);
    a0 = sub_102f2c20(a0, 15, 16, -10);
    a0 ^= 2629160650;
    a0 = sub_102f2ca0(a0, 1, 11);
    a0 = sub_102f2bf0(a0, -0x10);
    a0 = sub_102f2c20(a0, 24, 6, -20);
    a0 = sub_102f2bf0(a0, -29);
    a0 ^= 3617845311;
    return a0;
}
```

## `sub_102efcf0` `0x102efcf0`

_145 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102efcf0(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 1724717517;
    a0 = sub_102f2bf0(a0, 21, &v0);
    a0 ^= 1929954867;
    a0 = sub_102f2bf0(a0, 8);
    a0 ^= 2783894239;
    a0 = sub_102f2ca0(a0, 4, 14);
    a0 ^= 1067218587;
    a0 = sub_102f2bf0(a0, 27);
    a0 = sub_102f2c20(a0, 10, 4, 2);
    return a0;
}
```

## `sub_102efd90` `0x102efd90`

_146 bytes. (leaf/helper — see body)_

```c
int sub_102efd90(int a0)
{
    char v0;  // [bp+0x0]

    a0 = sub_102f2c20(a0, 10, 4, -2, &v0);
    a0 = sub_102f2bf0(a0, -27);
    a0 ^= 1067218587;
    a0 = sub_102f2ca0(a0, 4, 14);
    a0 ^= 2783894239;
    a0 = sub_102f2bf0(a0, -0x8);
    a0 ^= 1929954867;
    a0 = sub_102f2bf0(a0, -21);
    a0 ^= 1724717517;
    return a0;
}
```

## `sub_102efe30` `0x102efe30`

_371 bytes. (leaf/helper — see body)_

```c
int sub_102efe30(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 824075227;
    a0 = sub_102f2c20(a0, 19, 11, 15, &v0);
    a0 = sub_102f2bf0(a0, 6);
    a0 = sub_102f2d00(a0, 24, 7);
    a0 = sub_102f2c20(a0, 22, 9, 2);
    a0 = sub_102f2ca0(a0, 7, 13);
    a0 = sub_102f2c20(a0, 3, 24, 2);
    a0 = sub_102f2d00(a0, 19, 6);
    a0 = sub_102f2ca0(a0, 3, 11);
    a0 = sub_102f2bf0(a0, 11);
    a0 = sub_102f2c20(a0, 28, 3, 25);
    a0 = sub_102f2bf0(a0, 19);
    a0 = sub_102f2d00(a0, 28, 3);
    a0 = sub_102f2bf0(a0, 10);
    a0 = sub_102f2d00(a0, 6, 21);
    a0 = sub_102f2bf0(a0, 12);
    a0 = sub_102f2ca0(a0, 6, 22);
    a0 = sub_102f2bf0(a0, 1);
    a0 = sub_102f2c20(a0, 7, 10, 4);
    a0 ^= 59979578;
    return a0;
}
```

## `sub_102effb0` `0x102effb0`

_371 bytes. (leaf/helper — see body)_

```c
int sub_102effb0(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 59979578;
    a0 = sub_102f2c20(a0, 7, 10, -0x4, &v0);
    a0 = sub_102f2bf0(a0, -1);
    a0 = sub_102f2ca0(a0, 6, 22);
    a0 = sub_102f2bf0(a0, -12);
    a0 = sub_102f2d00(a0, 6, 21);
    a0 = sub_102f2bf0(a0, -10);
    a0 = sub_102f2d00(a0, 28, 3);
    a0 = sub_102f2bf0(a0, -19);
    a0 = sub_102f2c20(a0, 28, 3, -25);
    a0 = sub_102f2bf0(a0, -11);
    a0 = sub_102f2ca0(a0, 3, 11);
    a0 = sub_102f2d00(a0, 19, 6);
    a0 = sub_102f2c20(a0, 3, 24, -2);
    a0 = sub_102f2ca0(a0, 7, 13);
    a0 = sub_102f2c20(a0, 22, 9, -2);
    a0 = sub_102f2d00(a0, 24, 7);
    a0 = sub_102f2bf0(a0, -6);
    a0 = sub_102f2c20(a0, 19, 11, -15);
    a0 ^= 824075227;
    return a0;
}
```

## `sub_102f0130` `0x102f0130`

_379 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102f0130(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 894000583;
    a0 = sub_102f2bf0(a0, 30, &v0);
    a0 = sub_102f2c20(a0, 28, 2, 5);
    a0 = sub_102f2ca0(a0, 8, 10);
    a0 = sub_102f2c20(a0, 18, 7, 15);
    a0 = sub_102f2d00(a0, 18, 0);
    a0 = sub_102f2bf0(a0, 3);
    a0 = sub_102f2d00(a0, 21, 5);
    a0 = sub_102f2ca0(a0, 6, 21);
    a0 = sub_102f2c20(a0, 21, 3, 2);
    a0 ^= 1483602454;
    a0 = sub_102f2bf0(a0, 13);
    a0 = sub_102f2c20(a0, 4, 25, 3);
    a0 = sub_102f2d00(a0, 27, 3);
    a0 = sub_102f2ca0(a0, 1, 11);
    a0 ^= 663409347;
    a0 = sub_102f2c20(a0, 15, 0, 7);
    a0 = sub_102f2bf0(a0, 24);
    a0 = sub_102f2d00(a0, 10, 0x11);
    a0 ^= 2120344958;
    a0 = sub_102f2ca0(a0, 6, 16);
    return a0;
}
```

## `sub_102f02b0` `0x102f02b0`

_381 bytes. (leaf/helper — see body)_

```c
int sub_102f02b0(int a0)
{
    char v0;  // [bp+0x0]

    a0 = sub_102f2ca0(a0, 6, 16, &v0);
    a0 ^= 2120344958;
    a0 = sub_102f2d00(a0, 10, 0x11);
    a0 = sub_102f2bf0(a0, -24);
    a0 = sub_102f2c20(a0, 15, 0, -7);
    a0 ^= 663409347;
    a0 = sub_102f2ca0(a0, 1, 11);
    a0 = sub_102f2d00(a0, 27, 3);
    a0 = sub_102f2c20(a0, 4, 25, -3);
    a0 = sub_102f2bf0(a0, -13);
    a0 ^= 1483602454;
    a0 = sub_102f2c20(a0, 21, 3, -2);
    a0 = sub_102f2ca0(a0, 6, 21);
    a0 = sub_102f2d00(a0, 21, 5);
    a0 = sub_102f2bf0(a0, -3);
    a0 = sub_102f2d00(a0, 18, 0);
    a0 = sub_102f2c20(a0, 18, 7, -15);
    a0 = sub_102f2ca0(a0, 8, 10);
    a0 = sub_102f2c20(a0, 28, 2, -5);
    a0 = sub_102f2bf0(a0, -30);
    a0 ^= 894000583;
    return a0;
}
```

## `sub_102f0430` `0x102f0430`

_157 bytes. (leaf/helper — see body)_

```c
int sub_102f0430(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 2839853111;
    a0 = sub_102f2ca0(a0, 8, 18, &v0);
    a0 = sub_102f2d00(a0, 6, 21);
    a0 = sub_102f2c20(a0, 6, 14, 3);
    a0 = sub_102f2bf0(a0, 19);
    a0 ^= 3457438835;
    a0 = sub_102f2bf0(a0, 14);
    a0 = sub_102f2c20(a0, 22, 6, 5);
    a0 ^= 1018222023;
    return a0;
}
```

## `sub_102f04d0` `0x102f04d0`

_156 bytes. (leaf/helper — see body)_

```c
int sub_102f04d0(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 1018222023;
    a0 = sub_102f2c20(a0, 22, 6, -5, &v0);
    a0 = sub_102f2bf0(a0, -14);
    a0 ^= 3457438835;
    a0 = sub_102f2bf0(a0, -19);
    a0 = sub_102f2c20(a0, 6, 14, -3);
    a0 = sub_102f2d00(a0, 6, 21);
    a0 = sub_102f2ca0(a0, 8, 18);
    a0 ^= 2839853111;
    return a0;
}
```

## `sub_102f0570` `0x102f0570`

_209 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102f0570(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 1599336559;
    a0 = sub_102f2ca0(a0, 5, 10, &v0);
    a0 ^= 3821409299;
    a0 = sub_102f2d00(a0, 28, 3);
    a0 ^= 3171031454;
    a0 = sub_102f2ca0(a0, 4, 0x11);
    a0 = sub_102f2bf0(a0, 2);
    a0 = sub_102f2d00(a0, 8, 3);
    a0 = sub_102f2c20(a0, 15, 1, 14);
    a0 = sub_102f2d00(a0, 3, 16);
    a0 ^= 3383304650;
    a0 = sub_102f2c20(a0, 0x11, 9, 14);
    return a0;
}
```

## `sub_102f0650` `0x102f0650`

_209 bytes. (leaf/helper — see body)_

```c
int sub_102f0650(int a0)
{
    char v0;  // [bp+0x0]

    a0 = sub_102f2c20(a0, 0x11, 9, -14, &v0);
    a0 ^= 3383304650;
    a0 = sub_102f2d00(a0, 3, 16);
    a0 = sub_102f2c20(a0, 15, 1, -14);
    a0 = sub_102f2d00(a0, 8, 3);
    a0 = sub_102f2bf0(a0, -2);
    a0 = sub_102f2ca0(a0, 4, 0x11);
    a0 ^= 3171031454;
    a0 = sub_102f2d00(a0, 28, 3);
    a0 ^= 3821409299;
    a0 = sub_102f2ca0(a0, 5, 10);
    a0 ^= 1599336559;
    return a0;
}
```

## `sub_102f0730` `0x102f0730`

_138 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102f0730(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 913548452;
    a0 = sub_102f2ca0(a0, 7, 16, &v0);
    a0 ^= 3087435536;
    a0 = sub_102f2ca0(a0, 3, 22);
    a0 ^= 3469001533;
    a0 = sub_102f2bf0(a0, 0x11);
    a0 = sub_102f2ca0(a0, 1, 12);
    a0 = sub_102f2c20(a0, 25, 5, 10);
    return a0;
}
```

## `sub_102f07c0` `0x102f07c0`

_138 bytes. (leaf/helper — see body)_

```c
int sub_102f07c0(int a0)
{
    char v0;  // [bp+0x0]

    a0 = sub_102f2c20(a0, 25, 5, -10, &v0);
    a0 = sub_102f2ca0(a0, 1, 12);
    a0 = sub_102f2bf0(a0, -17);
    a0 ^= 3469001533;
    a0 = sub_102f2ca0(a0, 3, 22);
    a0 ^= 3087435536;
    a0 = sub_102f2ca0(a0, 7, 16);
    a0 ^= 913548452;
    return a0;
}
```

## `sub_102f0850` `0x102f0850`

_240 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102f0850(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 2293158517;
    a0 = sub_102f2bf0(a0, 15, &v0);
    a0 = sub_102f2d00(a0, 10, 14);
    a0 = sub_102f2c20(a0, 5, 21, 2);
    a0 = sub_102f2d00(a0, 3, 0x11);
    a0 ^= 3345442031;
    a0 = sub_102f2bf0(a0, 10);
    a0 = sub_102f2ca0(a0, 4, 18);
    a0 = sub_102f2c20(a0, 4, 9, 3);
    a0 = sub_102f2bf0(a0, 5);
    a0 = sub_102f2ca0(a0, 6, 10);
    a0 = sub_102f2d00(a0, 8, 20);
    a0 = sub_102f2c20(a0, 27, 1, 24);
    return a0;
}
```

## `sub_102f0940` `0x102f0940`

_240 bytes. (leaf/helper — see body)_

```c
int sub_102f0940(int a0)
{
    char v0;  // [bp+0x0]

    a0 = sub_102f2c20(a0, 27, 1, -24, &v0);
    a0 = sub_102f2d00(a0, 8, 20);
    a0 = sub_102f2ca0(a0, 6, 10);
    a0 = sub_102f2bf0(a0, -5);
    a0 = sub_102f2c20(a0, 4, 9, -3);
    a0 = sub_102f2ca0(a0, 4, 18);
    a0 = sub_102f2bf0(a0, -10);
    a0 ^= 3345442031;
    a0 = sub_102f2d00(a0, 3, 0x11);
    a0 = sub_102f2c20(a0, 5, 21, -2);
    a0 = sub_102f2d00(a0, 10, 14);
    a0 = sub_102f2bf0(a0, -15);
    a0 ^= 2293158517;
    return a0;
}
```

## `sub_102f0a30` `0x102f0a30`

_356 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102f0a30(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 3921427965;
    a0 = sub_102f2d00(a0, 26, 5, &v0);
    a0 = sub_102f2c20(a0, 27, 4, 16);
    a0 ^= 1414672152;
    a0 = sub_102f2c20(a0, 14, 16, 6);
    a0 = sub_102f2d00(a0, 31, 0);
    a0 = sub_102f2ca0(a0, 3, 22);
    a0 = sub_102f2d00(a0, 31, 0);
    a0 = sub_102f2ca0(a0, 6, 19);
    a0 ^= 2794081577;
    a0 = sub_102f2ca0(a0, 6, 23);
    a0 = sub_102f2c20(a0, 27, 3, 18);
    a0 = sub_102f2bf0(a0, 28);
    a0 = sub_102f2ca0(a0, 3, 10);
    a0 ^= 2189125973;
    a0 = sub_102f2d00(a0, 31, 0);
    a0 ^= 244022934;
    a0 = sub_102f2ca0(a0, 5, 14);
    a0 = sub_102f2d00(a0, 4, 22);
    a0 = sub_102f2c20(a0, 6, 22, 5);
    return a0;
}
```

## `sub_102f0ba0` `0x102f0ba0`

_358 bytes. (leaf/helper — see body)_

```c
int sub_102f0ba0(int a0)
{
    char v0;  // [bp+0x0]

    a0 = sub_102f2c20(a0, 6, 22, -5, &v0);
    a0 = sub_102f2d00(a0, 4, 22);
    a0 = sub_102f2ca0(a0, 5, 14);
    a0 ^= 244022934;
    a0 = sub_102f2d00(a0, 31, 0);
    a0 ^= 2189125973;
    a0 = sub_102f2ca0(a0, 3, 10);
    a0 = sub_102f2bf0(a0, -28);
    a0 = sub_102f2c20(a0, 27, 3, -18);
    a0 = sub_102f2ca0(a0, 6, 23);
    a0 ^= 2794081577;
    a0 = sub_102f2ca0(a0, 6, 19);
    a0 = sub_102f2d00(a0, 31, 0);
    a0 = sub_102f2ca0(a0, 3, 22);
    a0 = sub_102f2d00(a0, 31, 0);
    a0 = sub_102f2c20(a0, 14, 16, -6);
    a0 ^= 1414672152;
    a0 = sub_102f2c20(a0, 27, 4, -0x10);
    a0 = sub_102f2d00(a0, 26, 5);
    a0 ^= 3921427965;
    return a0;
}
```

## `sub_102f0d10` `0x102f0d10`

_173 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102f0d10(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 744219921;
    a0 = sub_102f2c20(a0, 23, 7, 19, &v0);
    a0 = sub_102f2bf0(a0, 12);
    a0 = sub_102f2ca0(a0, 5, 11);
    a0 = sub_102f2d00(a0, 7, 22);
    a0 = sub_102f2ca0(a0, 8, 23);
    a0 = sub_102f2c20(a0, 10, 0x11, 4);
    a0 = sub_102f2bf0(a0, 1);
    a0 = sub_102f2c20(a0, 3, 4, 2);
    return a0;
}
```

## `sub_102f0dc0` `0x102f0dc0`

_174 bytes. (leaf/helper — see body)_

```c
int sub_102f0dc0(int a0)
{
    char v0;  // [bp+0x0]

    a0 = sub_102f2c20(a0, 3, 4, -2, &v0);
    a0 = sub_102f2bf0(a0, -1);
    a0 = sub_102f2c20(a0, 10, 0x11, -0x4);
    a0 = sub_102f2ca0(a0, 8, 23);
    a0 = sub_102f2d00(a0, 7, 22);
    a0 = sub_102f2ca0(a0, 5, 11);
    a0 = sub_102f2bf0(a0, -12);
    a0 = sub_102f2c20(a0, 23, 7, -19);
    a0 ^= 744219921;
    return a0;
}
```

## `sub_102f0e70` `0x102f0e70`

_189 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102f0e70(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 211791105;
    a0 = sub_102f2bf0(a0, 24, &v0);
    a0 = sub_102f2d00(a0, 8, 19);
    a0 ^= 3007219773;
    a0 = sub_102f2d00(a0, 15, 13);
    a0 = sub_102f2bf0(a0, 12);
    a0 ^= 420175507;
    a0 = sub_102f2c20(a0, 22, 1, 5);
    a0 = sub_102f2d00(a0, 23, 6);
    a0 = sub_102f2ca0(a0, 5, 10);
    a0 = sub_102f2bf0(a0, 8);
    return a0;
}
```

