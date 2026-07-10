# elfbot.dll decompiled — jiru 0x102eb000..0x102ed4ef

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_102eb000` `0x102eb000`

_100 bytes. (leaf/helper — see body)_

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

struct_0 * sub_102eb000(struct_0 *idx, char *a1, unsigned int a2, char a3)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = idx;
    idx->field_16 = a3;
    idx->field_c = a1;
    idx->field_8 = a1;
    if (idx->field_16)
        idx->field_c->field_0 = 0;
    idx->field_10 = &idx->field_8[a2];
    idx->field_15 = 0;
    idx->field_14 = 128;
    sub_102eb160(idx, &v1);
    return idx;
}
```

## `sub_102eb070` `0x102eb070`

_52 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102eb070(char i)
{
    unsigned int v2;  // ecx
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v0 = v2;
    for (v1 = 0; i; i >>= 1)
    {
        v1 += 1;
    }
    return v1;
}
```

## `sub_102eb0b0` `0x102eb0b0`

_81 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102eb0b0(unsigned int a0, char a1)
{
    unsigned int v0;  // [bp-0x10]
    unsigned int i;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v0 = a0;
    v2 = 0;
    for (i = 1 << (a1 - 1 & 31); i; i >>= 1)
    {
        if ((char)sub_102eb190())
            v2 |= i;
    }
    return v2;
}
```

## `sub_102eb110` `0x102eb110`

_65 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102eb110(unsigned int a0, unsigned int a1, char a2)
{
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0xc]
    unsigned int i;  // [bp-0x8]

    v0 = a0;
    for (i = 1 << (a2 - 1 & 31); i; i >>= 1)
    {
        sub_102eb240(_INSERT(0, 0, (a1 & i)));
    }
    return v2;
}
```

## `sub_102eb160` `0x102eb160`

_34 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    char field_4;
    char padding_5[7];
    unsigned int field_c;
    char padding_10[4];
    char field_14;
} struct_0;

struct_0 * sub_102eb160(struct_0 *idx)
{
    idx->field_0 = idx->field_c;
    idx->field_4 = idx->field_14;
    return idx;
}
```

## `sub_102eb190` `0x102eb190`

_51 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    struct struct_1 *field_c;
    char padding_10[4];
    char field_14;
} struct_0;

typedef struct struct_1 {
    char field_0;
} struct_1;

char sub_102eb190(struct_0 *a0)
{
    char v0;  // [bp-0x5]

    v0 = -(-(0 < (a0->field_c->field_0 & a0->field_14)));
    sub_102eb1d0(a0);
    return v0;
}
```

## `sub_102eb1d0` `0x102eb1d0`

_44 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    char field_14;
} struct_0;

struct_0 * sub_102eb1d0(struct_0 *idx)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = idx;
    idx->field_14 = idx->field_14 >> 1;
    if (!idx->field_14)
        idx = sub_102eb200(idx, &v1);
    return idx;
}
```

## `sub_102eb200` `0x102eb200`

_54 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
    unsigned int field_10;
    char field_14;
    char field_15;
} struct_0;

struct_0 * sub_102eb200(struct_0 *a0)
{
    struct_0 *v2;  // eax
    struct_0 *idx;  // [bp-0x8]

    idx = a0;
    idx = a0;
    idx->field_c = idx->field_c + 1;
    v2 = idx;
    if (v2->field_c >= idx->field_10)
    {
        v2 = idx;
        v2->field_15 = 1;
    }
    idx->field_14 = 128;
    return v2;
}
```

## `sub_102eb240` `0x102eb240`

_55 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    struct struct_1 *field_c;
    char padding_10[4];
    char field_14;
} struct_0;

typedef struct struct_1 {
    char field_0;
} struct_1;

int sub_102eb240(struct_0 *a0, char a1)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    if (a1)
        a0->field_c->field_0 = a0->field_c->field_0 | a0->field_14;
    return sub_102eb280(a0, &v1);
}
```

## `sub_102eb280` `0x102eb280`

_44 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    char field_14;
} struct_0;

struct_0 * sub_102eb280(struct_0 *idx)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = idx;
    idx->field_14 = idx->field_14 >> 1;
    if (!idx->field_14)
        idx = sub_102eb2b0(idx, &v1);
    return idx;
}
```

## `sub_102eb2b0` `0x102eb2b0`

_65 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    struct struct_1 *field_c;
    char padding_10[4];
    char field_14;
    char field_15;
} struct_0;

typedef struct struct_1 {
    char field_0;
} struct_1;

struct_0 * sub_102eb2b0(struct_0 *a0)
{
    struct_0 *idx;  // [bp-0x8]

    idx = a0;
    idx = a0;
    idx->field_c = idx->field_c + 1;
    if (idx->field_c >= idx->padding_10)
        idx->field_15 = 1;
    else
        idx->field_c->field_0 = 0;
    idx->field_14 = 128;
    return idx;
}
```

## `sub_102eb300` `0x102eb300`

_59 bytes. (leaf/helper — see body)_

```c
int sub_102eb300(int a0, int a1, int a2)
{
    int v0;  // [bp-0xc]
    int v1;  // [bp-0x8]

    v0 = sub_10350a53(4168);
    v1 = v0;
    sub_102eb340(v1, a0, a1, a2);
    return v1;
}
```

## `sub_102eb340` `0x102eb340`

_615 bytes. (leaf/helper — see body)_

```c
void sub_102eb340(int a0, unsigned int a1, int a2, int a3)
{
    unsigned int v0;  // [bp-0x68]
    int node;  // [bp-0x64]
    int k;  // [bp-0x5c]
    unsigned int v3;  // [bp-0x58]
    unsigned int v4;  // [bp-0x54]
    int iter;  // [bp-0x50]
    unsigned int v6;  // [bp-0x4c]
    unsigned int v7;  // [bp-0x48]
    unsigned int v8;  // [bp-0x44]
    unsigned int v9;  // [bp-0x40]
    unsigned int v10;  // [bp-0x3c]
    unsigned int v11;  // [bp-0x38]
    unsigned int v12;  // [bp-0x34]
    unsigned int v13;  // [bp-0x30]
    unsigned int v14;  // [bp-0x2c]
    unsigned int v15;  // [bp-0x28]
    unsigned int v16;  // [bp-0x24]
    unsigned int v17;  // [bp-0x20]
    unsigned int v18;  // [bp-0x1c]
    unsigned int v19;  // [bp-0x18]
    unsigned int v20;  // [bp-0x14]
    unsigned int v21;  // [bp-0x10]
    unsigned int v22;  // [bp-0xc]
    unsigned int v23;  // [bp-0x8]

    v6 = 608135816;
    v7 = 2242054355;
    v8 = 320440878;
    v9 = 57701188;
    v10 = 2752067618;
    v11 = 698298832;
    v12 = 137296536;
    v13 = 3964562569;
    v14 = 1160258022;
    v15 = 953160567;
    v16 = 3193202383;
    v17 = 887688300;
    v18 = 3232508343;
    v19 = 3380367581;
    v20 = 1065670069;
    v21 = 3041331479;
    v22 = 2450970073;
    v23 = 2306472731;
    for (iter = 0; iter < 18; iter += 1)
    {
        *((unsigned int *)(a0 + iter * 4 + 0x1000)) = (&v6)[iter];
    }
    sub_1033a4c0(a3);
    for (iter = 0; iter < 4; iter += 1)
    {
        for (node = 0; node < 0x100; node += 1)
        {
            *((unsigned int *)(iter * 0x400 + a0 + node * 4)) = sub_102eb870();
        }
    }
    iter = 0;
    for (node = 0; iter < 18; iter += 1)
    {
        v0 = 0;
        for (k = 0; k < 4; k += 1)
        {
            v0 = v0 * 0x100 | *((char *)(a1 + node));
            node += 1;
            if (node >= a2)
                node = 0;
        }
        *((unsigned int *)(a0 + iter * 4 + 0x1000)) = *((int *)(a0 + iter * 4 + 0x1000)) ^ v0;
    }
    v3 = 0;
    v4 = 0;
    for (iter = 0; iter < 18; iter += 2)
    {
        sub_102eb5b0(a0, &v3, &v4);
        *((unsigned int *)(a0 + iter * 4 + 0x1000)) = v3;
        *((unsigned int *)(a0 + iter * 4 + 4100)) = v4;
    }
    for (iter = 0; iter < 4; iter += 1)
    {
        for (node = 0; node < 0x100; node += 2)
        {
            sub_102eb5b0(a0, &v3, &v4);
            *((unsigned int *)(iter * 0x400 + a0 + node * 4)) = v3;
            *((unsigned int *)(iter * 0x400 + a0 + node * 4 + 4)) = v4;
        }
    }
    return;
}
```

## `sub_102eb5b0` `0x102eb5b0`

_181 bytes. (leaf/helper — see body)_

```c
int sub_102eb5b0(unsigned int *idx, unsigned int *a1, int *a2)
{
    short i;  // [bp-0x14]
    int v1;  // [bp-0x10], Other Possible Types: unsigned int
    int v2;  // [bp-0xc], Other Possible Types: unsigned int
    int v3;  // [bp-0x8], Other Possible Types: unsigned int

    v1 = *(a1);
    v2 = *(a2);
    for (i = 0; i < 16; i += 1)
    {
        v1 ^= idx[0x400 + i];
        v2 ^= sub_102eb670(idx, v1);
        v3 = v1;
        v1 = v2;
        v2 = v3;
    }
    v3 = v1;
    v1 = v2;
    v2 = v3;
    v2 ^= idx[1040];
    v1 ^= idx[1041];
    *(a1) = v1;
    *(a2) = v2;
    return v2;
}
```

## `sub_102eb670` `0x102eb670`

_85 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    char padding_4[1020];
    unsigned int field_400;
    char padding_404[1020];
    unsigned int field_800;
} struct_0;

int sub_102eb670(struct_0 *a0, char a1)
{
    return (a0->field_0 + a0->field_400 ^ a0->field_800) + *((int *)&a0[1].padding_4[1016 + 4 * a1]);
}
```

## `sub_102eb6d0` `0x102eb6d0`

_26 bytes. (leaf/helper — see body)_

```c
int sub_102eb6d0(int a0)
{
    unsigned int v2;  // ecx
    unsigned int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = v2;
    return sub_10350abd(a0, a0, &v1);
}
```

## `sub_102eb6f0` `0x102eb6f0`

_90 bytes. (leaf/helper — see body)_

```c
int sub_102eb6f0(unsigned int *a0, unsigned int a1, unsigned int a2)
{
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0xc]
    unsigned int i;  // [bp-0x8]

    a2 &= 0xfffffff8;
    i = a1;
    for (v0 = i + (a2 + (a2 >> 31 & 3) >> 2) * 4; i < v0; i += 8)
    {
        v2 = sub_102eb5b0(a0, i, i + 4);
    }
    return v2;
}
```

## `sub_102eb750` `0x102eb750`

_90 bytes. (leaf/helper — see body)_

```c
int sub_102eb750(int a0, int a1, unsigned int a2)
{
    int v2;  // eax
    int v0;  // [bp-0xc]
    int i;  // [bp-0x8]

    a2 &= 0xfffffff8;
    i = a1;
    for (v0 = i + (a2 + (a2 >> 31 & 3) >> 2) * 4; i < v0; i += 8)
    {
        v2 = sub_102eb7b0(a0, i, i + 4);
    }
    return v2;
}
```

## `sub_102eb7b0` `0x102eb7b0`

_181 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    char padding_4[1020];
    unsigned int field_400;
    char padding_404[1020];
    unsigned int field_800;
} struct_0;

int sub_102eb7b0(struct_0 *idx, unsigned int *a1, unsigned int *a2)
{
    short i;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v1 = *(a1);
    v2 = *(a2);
    for (i = 0x11; i > 1; i -= 1)
    {
        v1 ^= *((int *)&idx[1].padding_404[1016 + 4 * i]);
        v2 ^= sub_102eb670(idx, v1);
        v3 = v1;
        v1 = v2;
        v2 = v3;
    }
    v3 = v1;
    v1 = v2;
    v2 = v3;
    v2 ^= idx[1].field_800;
    v1 ^= *((int *)&idx[1].padding_404[1016]);
    *(a1) = v1;
    *(a2) = v2;
    return v2;
}
```

## `sub_102eb870` `0x102eb870`

_94 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102eb870(int a0)
{
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v3 = sub_102eb8d0(a0) & 0xff;
    v0 = sub_102eb8d0(a0) & 0xff;
    v1 = sub_102eb8d0() & 0xff;
    v2 = sub_102eb8d0() & 0xff;
    return v3 * 0x1000000 | v0 * 0x10000 | v1 * 0x100 | v2;
}
```

## `sub_102eb8d0` `0x102eb8d0`

_24 bytes. (leaf/helper — see body)_

```c
void sub_102eb8d0(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_102eb8f0(0x100, a0, &v1);
    return;
}
```

## `sub_102eb8f0` `0x102eb8f0`

_76 bytes. (leaf/helper — see body)_

```c
int sub_102eb8f0(int *a0, unsigned int a1)
{
    int *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    *(a0) = (sub_102eb940(*(a0), 31415821, a0, &v1) + 1) % 100000000;
    return a1 * (unsigned int)(*(a0) / 10000) / 10000;
}
```

## `sub_102eb940` `0x102eb940`

_122 bytes. (leaf/helper — see body)_

```c
int sub_102eb940(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v1 = a0 / 10000;
    v2 = a0 % 10000;
    v0 = a1 / 10000;
    v3 = a1 % 10000;
    return (v3 * v2 + (unsigned int)((v0 * v2 + v3 * v1) % 10000) * 10000) % 100000000;
}
```

## `sub_102eb9c0` `0x102eb9c0`

_65 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c268;

int sub_102eb9c0(unsigned short a0)
{
    if (!a0)
    {
        g_1038c268 = 0;
        return a0;
    }
    else if (a0 == 1)
    {
        g_1038c268 = 1;
        return a0;
    }
    else
    {
        if (a0 != 2)
            return a0;
        g_1038c268 = 7;
        return a0;
    }
}
```

## `sub_102eba10` `0x102eba10`

_645 bytes. refs "1.2.3"_

```c
extern int g_1038c268;

int sub_102eba10(char *a0, char *a1, int a2, unsigned int a3)
{
    unsigned int v0;  // [bp-0x64]
    char v1;  // [bp-0x60]
    char v2[4];  // [bp-0x60]
    int v3;  // [bp-0x5c]
    char v4[3];  // [bp-0x54]
    unsigned int v5;  // [bp-0x50]
    unsigned int v6;  // [bp-0x28]
    unsigned int iter1;  // [bp-0x24]
    char j[4];  // [bp-0x20]
    char iter[3];  // [bp-0x1c]
    char v10[4];  // [bp-0x18]
    char v11;  // [bp-0x11]
    char node[4];  // [bp-0x10]
    char v13[3];  // [bp-0xc]
    char v14;  // [bp-0x5]

    if (!g_1038c268)
    {
        node = a0;
        iter = a1;
        v10 = &node[a2];
        v13 = &iter[a3 + 2];
        v14 = 255;
        v11 = 1;
        iter[0] = 1;
        iter = &iter[1];
        while (node < v10)
        {
            if (&node[2] < v10 && node[0] == v14 && node[1] == v14 && node[2] == v14)
            {
                iter1 = 3;
                for (j = &node[3]; j < v10 && j[0] == v14; j = &j[1])
                {
                    iter1 += 1;
                }
                do
                {
                    if (iter1 < 3)
                        goto LABEL_102ebb4f;
                    v0 = (iter1 <= 0x101 ? iter1 : 0x101);
                    v6 = v0;
                    iter[0] = 255;
                    iter = &iter[1];
                    iter[0] = v6 - 3;
                    iter = &iter[1];
                    iter1 -= v6;
                } while (iter < v13);
                v11 = 0;
                node = v10;
LABEL_102ebb4f:
                node = &j[-1 * iter1];
            }
            else
            {
                if (node[0] == 255)
                {
                    iter[0] = 255;
                    iter = &iter[1];
                    iter[0] = 255;
                    iter = &iter[1];
                    v14 = node[0];
                    node = &node[1];
                }
                else
                {
                    iter[0] = node[0];
                    v14 = iter[0];
                    iter = &iter[1];
                    node = &node[1];
                }
                if (iter >= v13)
                {
                    v11 = 0;
                    break;
                }
            }
        }
        if (!v11)
        {
            *(a1) = 0;
            sub_10350b50(a1 + 1, a0, a2);
            a2 += 1;
        }
        else
        {
            a2 = iter - a1;
        }
        return a2;
    }
    else
    {
        sub_10350ad0(&v1, 0, 56);
        if (!sub_1034c696(&v1, g_1038c268, "1.2.3", 56))
        {
            v3 = a2;
            v5 = a3;
            v2 = a0;
            v4 = a1;
            a2 = (sub_1034b0ae(&v2, 4) == 1 ? v4 - a1 : 0);
        }
        else
        {
            a2 = 0;
        }
        sub_1034b81d(&v1);
        return a2;
    }
}
```

## `sub_102ebca0` `0x102ebca0`

_492 bytes. refs "1.2.3"_

```c
extern unsigned int g_1038c268;

unsigned int sub_102ebca0(char *a0, char *a1, unsigned int a2, unsigned int a3)
{
    unsigned int v0;  // [bp-0x60]
    unsigned int v1;  // [bp-0x5c]
    char v2[3];  // [bp-0x58], Other Possible Types: char
    unsigned int v3;  // [bp-0x54]
    char *v4;  // [bp-0x4c]
    unsigned int v5;  // [bp-0x48]
    unsigned int v6;  // [bp-0x20]
    unsigned int v7;  // [bp-0x1c]
    char *iter;  // [bp-0x18]
    char v9[3];  // [bp-0x14]
    char *v10;  // [bp-0x10]
    char node[3];  // [bp-0xc]
    char v12;  // [bp-0x5]

    if (!g_1038c268)
    {
        node = a0 + 1;
        iter = a1;
        v9 = &a0[a2];
        v10 = &a1[a3];
        v12 = 255;
        if (!*(a0))
        {
            a2 -= 1;
            sub_10350b50(a1, a0 + 1, a2);
        }
        else
        {
            while (node < v9 && iter < v10)
            {
                if (node[0] == 255)
                {
                    node = &node[1];
                    if (node[0] != 255)
                    {
                        v7 = node[0] + 3;
                        node = &node[1];
                        if (&iter[v7] >= v10)
                            break;
                        while (true)
                        {
                            v7 -= 1;
                            if (!v7)
                                break;
                            *(iter) = v12;
                            iter += 1;
                        }
                    }
                    else
                    {
                        *(iter) = node[0];
                        v12 = *(iter);
                        iter += 1;
                        node = &node[1];
                    }
                }
                else
                {
                    *(iter) = node[0];
                    v12 = *(iter);
                    iter += 1;
                    node = &node[1];
                }
            }
            v0 = (node == v9 ? iter - a1 : 0);
            a2 = v0;
        }
        return a2;
    }
    else
    {
        sub_10350ad0(&v2, 0, 56);
        v3 = a2;
        v5 = a3;
        v2 = a0;
        v4 = a1;
        v6 = sub_1034c7cc(&v2, "1.2.3", 56);
        if (v6)
        {
            a2 = 0;
            return a2;
        }
        v1 = sub_1034c8d8(&v2, 4);
        a2 = (v1 == 1 ? v4 - a1 : 0);
        sub_1034db40(&v2);
        return a2;
    }
}
```

## `sub_102ebe90` `0x102ebe90`

_507 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    char field_8;
} struct_0;

extern unsigned int g_103a1760;
extern char g_103a176a;
extern unsigned int g_103a1770;
extern unsigned int g_103a1778;
extern unsigned int g_103a177c;

char sub_102ebe90(char *a0, int *a1, int a2)
{
    unsigned int v0;  // [bp-0x28]
    int v1;  // [bp-0x24]
    int v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x1c]
    struct_0 *idx;  // [bp-0x18]
    char v5[2];  // [bp-0x14]
    char iter[2];  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    int v8;  // [bp-0x8]

    sub_102ec1f0();
    sub_102ec270();
    v2 = sub_10350a53(a2 + 1);
    v8 = v2;
    sub_102ec090(v8, a2, 1);
    iter = a0;
    v5 = &iter[*(a1)];
    v7 = iter[0];
    for (iter = &iter[1]; iter < v5 && !g_103a176a; iter = &iter[1])
    {
        v3 = sub_102ec2e0(v7, iter[0]);
        idx = v3 * 12 + g_103a177c;
        if (idx->field_0 == 4294967295)
        {
            idx->field_0 = g_103a1778;
            g_103a1778 = g_103a1778 + 1;
            idx->field_4 = v7;
            idx->field_8 = iter[0];
            sub_102ec130(v7, g_103a1760);
            v7 = iter[0];
            if (g_103a1778 > 0x7fff)
            {
                sub_102ec130(258, g_103a1760);
                sub_102ec270();
            }
            else if (g_103a1778 > g_103a1770)
            {
                v0 = g_103a1760;
                g_103a1760 = g_103a1760 + 1;
                sub_102ec130(0x101, v0);
                g_103a1770 = g_103a1770 * 2 | 1;
            }
        }
        else
        {
            v7 = idx->field_0;
        }
    }
    if (!g_103a176a)
    {
        sub_102ec130(v7, g_103a1760);
        sub_102ec130(0x100, g_103a1760);
    }
    if (!g_103a176a)
    {
        *(a1) = sub_102ec100();
        sub_10350b50(a0, v8, *(a1));
    }
    v1 = v8;
    sub_10350abd(v1);
    sub_102ec230();
    return !g_103a176a;
}
```

## `sub_102ec090` `0x102ec090`

_98 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
} struct_0;

extern struct_0 *g_103a1764;
extern char g_103a1768;
extern char g_103a1769;
extern char g_103a176a;
extern unsigned int g_103a1774;
extern unsigned int g_103a1780;

int sub_102ec090(unsigned int a0, unsigned int a1, char a2)
{
    unsigned int v0;  // eax

    g_103a1764 = a0;
    g_103a1780 = g_103a1764;
    g_103a1774 = g_103a1780 + a1;
    g_103a1769 = 128;
    v0 = a2;
    if (v0)
    {
        g_103a1768 = 0;
    }
    else
    {
        g_103a1768 = g_103a1764->field_0;
        v0 = g_103a1764 + 1;
        g_103a1764 = v0;
    }
    g_103a176a = 0;
    return v0;
}
```

## `sub_102ec100` `0x102ec100`

_44 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
} struct_0;

extern struct_0 *g_103a1764;
extern char g_103a1768;
extern unsigned int g_103a1780;

int sub_102ec100(void)
{
    g_103a1764->field_0 = g_103a1768;
    g_103a1764 = g_103a1764 + 1;
    return &g_103a1764[-1 * g_103a1780];
}
```

## `sub_102ec130` `0x102ec130`

_190 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
} struct_0;

extern struct_0 *g_103a1764;
extern char g_103a1768;
extern char g_103a1769;
extern char g_103a176a;
extern char g_103a1774;

int sub_102ec130(unsigned int a0, char a1)
{
    unsigned int v1;  // ecx
    int i;  // [bp-0x8], Other Possible Types: unsigned int

    i = v1;
    for (i = 1 << (a1 - 1 & 31); i; i >>= 1)
    {
        if ((a0 & i))
            g_103a1768 = g_103a1768 | g_103a1769;
        g_103a1769 = g_103a1769 >> 1;
        if (!g_103a1769)
        {
            if (g_103a1764 < *((int *)&g_103a1774))
            {
                g_103a1764->field_0 = g_103a1768;
                g_103a1764 = g_103a1764 + 1;
            }
            if (g_103a1764 >= *((int *)&g_103a1774))
                g_103a176a = 1;
            g_103a1768 = 0;
            g_103a1769 = 128;
        }
    }
    return -(0 < g_103a176a) + 1;
}
```

## `sub_102ec1f0` `0x102ec1f0`

_59 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a176c;
extern unsigned int g_103a177c;

int sub_102ec1f0(void)
{
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v1 = sub_10350a53(420276);
    g_103a177c = v1;
    v0 = sub_10350a53(35023);
    g_103a176c = v0;
    return v0;
}
```

## `sub_102ec230` `0x102ec230`

_51 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a176c;
extern unsigned int g_103a177c;

int sub_102ec230(void)
{
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v1 = g_103a177c;
    sub_10350abd(v1);
    v0 = g_103a176c;
    return sub_10350abd(v0);
}
```

## `sub_102ec270` `0x102ec270`

_97 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a1760;
extern unsigned int g_103a1770;
extern unsigned int g_103a1778;
extern unsigned int g_103a177c;

int sub_102ec270(void)
{
    unsigned int v2;  // ecx
    unsigned int v3;  // eax
    unsigned int idx;  // [bp-0x8]

    idx = v2;
    for (idx = 0; idx < 35023; idx += 1)
    {
        *((unsigned int *)(g_103a177c + idx * 12)) = 4294967295;
    }
    g_103a1778 = 259;
    g_103a1760 = 9;
    v3 = 1 << ((char)g_103a1760 & 31);
    g_103a1770 = v3 - 1;
    return v3 - 1;
}
```

## `sub_102ec2e0` `0x102ec2e0`

_150 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    char padding_4[4];
    char field_8;
} struct_0;

extern unsigned int g_103a177c;

unsigned int sub_102ec2e0(unsigned int a0, unsigned int a1)
{
    unsigned int v4;  // eax
    unsigned int v0;  // [bp-0x14]
    struct_0 *v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v4 = a1 * 128;
    v3 = v4 ^ a0;
    v0 = (!(v4 ^ a0) ? 1 : 35023 - v3);
    v2 = v0;
    while (true)
    {
        v1 = v3 * 12 + g_103a177c;
        if (v1->field_0 == 4294967295)
            return v3;
        if (v1->padding_4 == a0 && v1->field_8 == a1)
            return v3;
        v3 = (v3 < v2 ? 35023 - v2 + v3 : v3 - v2);
    }
}
```

## `sub_102ec380` `0x102ec380`

_517 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[4];
    int field_4;
    char field_8;
} struct_1;

typedef struct struct_0 {
    char field_0;
} struct_0;

extern int g_103a1760;
extern char g_103a176a;
extern struct_0 *g_103a176c;
extern unsigned int g_103a1778;
extern unsigned int g_103a177c;

char sub_102ec380(unsigned int a0, void* a1, int a2)
{
    char v0;  // [bp-0x31]
    char *v1;  // [bp-0x30]
    char *v2;  // [bp-0x2c]
    struct_1 *idx;  // [bp-0x28]
    int v4;  // [bp-0x24]
    unsigned int v5;  // [bp-0x20]
    int v6;  // [bp-0x1c]
    int v7;  // [bp-0x18]
    char *iter;  // [bp-0x14]
    char i;  // [bp-0xd]
    char *v10;  // [bp-0xc]
    char *v11;  // [bp-0x8]

    sub_102ec1f0();
    sub_102ec090(a0, *((int *)a1), 0);
    v2 = sub_10350a53(a2 + 1);
    v10 = v2;
    v11 = &v10[a2 + 1];
    iter = v10;
    i = 0;
    while (!i)
    {
        sub_102ec270();
        v6 = sub_102ec590(g_103a1760);
        if (v6 == 0x100)
            i = 1;
        v7 = v6;
        *(iter) = v7;
        iter += 1;
        while (!i)
        {
            v4 = sub_102ec590(g_103a1760);
            if (v4 == 0x100)
            {
                i = 1;
                break;
            }
            else
            {
                if (v4 == 258)
                    break;
                if (v4 == 0x101)
                {
                    g_103a1760 = g_103a1760 + 1;
                }
                else
                {
                    if (v4 >= g_103a1778)
                    {
                        g_103a176c->field_0 = v7;
                        v5 = sub_102ec640(1, v6);
                    }
                    else
                    {
                        v5 = sub_102ec640(0, v4);
                    }
                    for (v7 = g_103a176c[1 + v5].field_0; v5 && iter < v11; iter += 1)
                    {
                        v5 -= 1;
                        *(iter) = g_103a176c[v5].field_0;
                    }
                    idx = g_103a1778 * 12 + g_103a177c;
                    idx->field_4 = v6;
                    idx->field_8 = v7;
                    g_103a1778 = g_103a1778 + 1;
                    v6 = v4;
                }
            }
        }
    }
    *((unsigned long *)a1) = iter - v10;
    sub_10350b50(a0, v10, *((int *)a1));
    v1 = v10;
    sub_10350abd(v1);
    sub_102ec230();
    if (!g_103a176a && iter != v11)
    {
        v0 = 1;
        return v0;
    }
    v0 = 0;
    return v0;
}
```

## `sub_102ec445` `0x102ec445`

_2 bytes. (leaf/helper — see body)_

```c
void sub_102ec445(void)
{
}
```

## `sub_102ec455` `0x102ec455`

_2 bytes. (leaf/helper — see body)_

```c
void sub_102ec455(void)
{
}
```

## `sub_102ec471` `0x102ec471`

_2 bytes. (leaf/helper — see body)_

```c
void sub_102ec471(void)
{
}
```

## `sub_102ec590` `0x102ec590`

_174 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
} struct_0;

extern struct_0 *g_103a1764;
extern char g_103a1768;
extern char g_103a1769;
extern char g_103a176a;
extern char g_103a1774;

unsigned int sub_102ec590(unsigned int a0)
{
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v2 = 0;
    v0 = a0;
    while (true)
    {
        v1 = v0 - 1;
        if (!v0)
            break;
        v2 *= 2;
        if ((g_103a1768 & g_103a1769))
            v2 |= 1;
        g_103a1769 = g_103a1769 >> 1;
        if (!g_103a1769)
        {
            if (g_103a1764 >= *((int *)&g_103a1774))
            {
                g_103a176a = 1;
                g_103a1768 = 0;
            }
            else
            {
                g_103a1768 = g_103a1764->field_0;
                g_103a1764 = g_103a1764 + 1;
            }
            g_103a1769 = 128;
        }
        v0 = v1;
    }
    return v2;
}
```

## `sub_102ec640` `0x102ec640`

_95 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
    char field_8;
} struct_0;

extern unsigned int g_103a176c;
extern unsigned int g_103a177c;

unsigned int sub_102ec640(unsigned int iter, unsigned int i)
{
    unsigned int v1;  // ecx
    struct_0 *idx;  // [bp-0x8], Other Possible Types: unsigned int

    for (idx = v1; i > 0xff; i = idx->field_4)
    {
        idx = i * 12 + g_103a177c;
        *((char *)(g_103a176c + iter)) = idx->field_8;
        iter += 1;
    }
    *((char *)(g_103a176c + iter)) = i;
    iter += 1;
    return iter;
}
```

## `sub_102ec6a0` `0x102ec6a0`

_515 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    struct struct_0 *field_4;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    struct struct_0 *field_c;
} struct_1;

struct_0 * sub_102ec6a0(struct_1 *idx, struct_0 *a1, unsigned int a2, int a3)
{
    struct_0 *v20;  // eax
    struct_0 *v0;  // [bp-0x4c]
    unsigned int v1;  // [bp-0x48]
    unsigned int v2;  // [bp-0x44]
    unsigned int v3;  // [bp-0x44]
    unsigned int v4;  // [bp-0x40]
    struct_0 *v5;  // [bp-0x3c]
    struct_0 *v6;  // [bp-0x38]
    unsigned int v7;  // [bp-0x34]
    unsigned int v8;  // [bp-0x30]
    unsigned int v9;  // [bp-0x2c]
    unsigned int v10;  // [bp-0x2c]
    unsigned int v11;  // [bp-0x28]
    struct_0 *v12;  // [bp-0x24]
    unsigned int v13;  // [bp-0x20]
    unsigned int v14;  // [bp-0x1c]
    struct_0 *v15;  // [bp-0x18]
    unsigned int v16;  // [bp-0x14]
    unsigned int v17;  // [bp-0x10]
    unsigned int v18;  // [bp-0xc]
    struct_0 *iter;  // [bp-0x8]

    v13 = 2654435769;
    v17 = 32;
    v18 = idx->field_0;
    v16 = idx->field_4;
    v14 = idx->field_8;
    v15 = idx->field_c;
    a2 &= 0xfffffff8;
    iter = a1;
    v12 = &(&iter->field_0)[a2 >> 2];
    if (a3 > 0)
    {
        while (iter < v12)
        {
            v11 = iter->field_0;
            v6 = iter->field_4;
            v7 = 0;
            v9 = 32;
            v8 = v11;
            v5 = v6;
            while (true)
            {
                v10 = v9 - 1;
                if (!v9)
                    break;
                v7 -= 1640531527;
                v11 += v6 * 16 + v18 ^ (char *)v6 + v7 ^ (v6 >> 5) + v16;
                v6 = (v11 * 16 + v14 ^ v11 + v7 ^ (v11 >> 5) + (char *)v15) + (char *)v6;
                v9 = v10;
            }
            iter->field_0 = v11;
            iter = &iter->field_4;
            v20 = v6;
            iter->field_0 = v20;
            iter = &iter->field_4;
            if (a3 > 1)
            {
                v16 = v8;
                v20 = v5;
                v15 = v20;
            }
        }
        return v20;
    }
    else
    {
        while (iter < v12)
        {
            v4 = iter->field_0;
            v0 = iter->field_4;
            v1 = 3337565984;
            v2 = 32;
            while (true)
            {
                v3 = v2 - 1;
                if (!v2)
                    break;
                v0 = (char *)v0 - (v4 * 16 + v14 ^ v4 + v1 ^ (v4 >> 5) + (char *)v15);
                v4 -= v0 * 16 + v18 ^ (char *)v0 + v1 ^ (v0 >> 5) + v16;
                v1 += 1640531527;
                v2 = v3;
            }
            iter->field_0 = v4;
            iter = &iter->field_4;
            iter->field_0 = v0;
            iter = &iter->field_4;
            if (a3 < 0)
            {
                v16 = v4;
                v15 = v0;
            }
        }
        return v20;
    }
}
```

## `sub_102ec8b0` `0x102ec8b0`

_115 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    void* field_4;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    struct struct_0 *field_c;
} struct_1;

struct_0 * sub_102ec8b0(struct_1 a0, struct_0 *a1, unsigned int a2, int a3)
{
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    struct_1 v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]

    v6 = (unsigned int)(__ROR__(a0, 8));
    v0 = __ROR__(v6, 8);
    v1 = __ROR__(v0, 8);
    v2 = a0;
    v3 = v6;
    v4 = v0;
    v5 = v1;
    return sub_102ec6a0(&v2, a1, a2, a3);
}
```

## `sub_102ec930` `0x102ec930`

_31 bytes. (leaf/helper — see body)_

```c
int sub_102ec930(int a0, int a1, unsigned int a2)
{
    char v0;  // [bp+0x0]

    return sub_1034ddc8(a2 ^ 4294967295, a0, a1, &v0) ^ 4294967295;
}
```

## `sub_102ec950` `0x102ec950`

_35 bytes. (leaf/helper — see body)_

```c
int sub_102ec950(unsigned int a0, unsigned int a1)
{
    int v1;  // eax
    char v0;  // [bp+0x0]

    v1 = sub_1031e920(a1, &v0);
    return sub_102ec930(sub_102ec980(v1), v1, a1);
}
```

## `sub_102ec980` `0x102ec980`

_19 bytes. (leaf/helper — see body)_

```c
void sub_102ec980(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_102ec9a0(a0, &v1);
    return;
}
```

## `sub_102ec9a0` `0x102ec9a0`

_19 bytes. (leaf/helper — see body)_

```c
void sub_102ec9a0(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10314a50(a0, &v1);
    return;
}
```

## `sub_102ec9c0` `0x102ec9c0`

_137 bytes. (leaf/helper — see body)_

```c
char sub_102ec9c0(int a0, int *a1, int a2)
{
    int v0;  // [bp-0x10]
    int v1;  // [bp-0xc]
    int v2;  // [bp-0x8]

    v1 = sub_1034fef0(a2);
    v2 = v1;
    sub_102eca50(a0, v2, a1);
    sub_102ecc50(v2, a0, a1);
    sub_102ecd50(a0, v2, *(a1));
    sub_102ee0d0(v2, a0, a1, a2);
    v0 = v2;
    sub_10350eb5(v0);
    return 1;
}
```

## `sub_102eca50` `0x102eca50`

_511 bytes. (leaf/helper — see body)_

```c
char sub_102eca50(char *a0, char *a1, int *a2)
{
    unsigned int v0;  // [bp-0x2c]
    unsigned int v1;  // [bp-0x28]
    unsigned int iter1;  // [bp-0x24]
    char j[4];  // [bp-0x20]
    char iter[3];  // [bp-0x1c]
    char v5[4];  // [bp-0x18]
    char v6;  // [bp-0x11]
    char node[4];  // [bp-0x10]
    char v8[3];  // [bp-0xc]
    char v9;  // [bp-0x5]

    node = a0;
    iter = a1;
    v5 = &node[*(a2)];
    v8 = &iter[*(a2) + 2];
    v9 = 255;
    v6 = 1;
    iter[0] = 1;
    iter = &iter[1];
    while (node < v5)
    {
        if (&node[2] < v5 && node[0] == v9 && node[1] == v9 && node[2] == v9)
        {
            iter1 = 3;
            for (j = &node[3]; j < v5 && j[0] == v9; j = &j[1])
            {
                iter1 += 1;
            }
            do
            {
                if (iter1 < 3)
                    goto LABEL_102ecb86;
                v0 = (iter1 <= 0x101 ? iter1 : 0x101);
                v1 = v0;
                iter[0] = 255;
                iter = &iter[1];
                iter[0] = v1 - 3;
                iter = &iter[1];
                iter1 -= v1;
            } while (iter < v8);
            v6 = 0;
            node = v5;
LABEL_102ecb86:
            node = &j[-1 * iter1];
        }
        else
        {
            if (node[0] == 255)
            {
                iter[0] = 255;
                iter = &iter[1];
                iter[0] = 255;
                iter = &iter[1];
                v9 = node[0];
                node = &node[1];
            }
            else
            {
                iter[0] = node[0];
                v9 = iter[0];
                iter = &iter[1];
                node = &node[1];
            }
            if (iter >= v8)
            {
                v6 = 0;
                break;
            }
        }
    }
    if (v6)
    {
        *(a2) = iter - a1;
        return v6;
    }
    *(a1) = 0;
    sub_10350b50(a1 + 1, a0, *(a2));
    *(a2) = *(a2) + 1;
    return v6;
}
```

## `sub_102ecc50` `0x102ecc50`

_253 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    char field_4;
} struct_0;

int sub_102ecc50(int a0, struct_0 *a1, void* a2)
{
    int v0;  // [bp-0x1c]
    int v1;  // [bp-0x18]
    unsigned int idx;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    struct_0 *iter;  // [bp-0x8]

    v1 = sub_1034fef0(-((*((int *)a2) >= 0x20000000 ? 1 : 0) & 1) | *((int *)a2) * 4);
    v4 = v1;
    sub_102edf10(a0, *((int *)a2), v4);
    v3 = 4294967295;
    iter = &a1->field_4;
    for (idx = 0; idx < *((int *)a2); idx += 1)
    {
        if (v3 == 4294967295 && *((int *)(v4 + idx * 4)) == a0 + 1)
            v3 = idx;
        if (*((int *)(v4 + idx * 4)) == a0)
        {
            *((char *)&iter->field_0) = *((char *)(a0 + *((int *)a2) - 1));
            iter = (char *)&iter->field_0 + 1;
        }
        else
        {
            *((char *)&iter->field_0) = *((char *)(*((int *)(v4 + idx * 4)) - 1));
            iter = (char *)&iter->field_0 + 1;
        }
    }
    a1->field_0 = v3;
    *((unsigned int *)a2) = *((int *)a2) + 4;
    v0 = v4;
    return sub_10350eb5(v0);
}
```

## `sub_102ecd50` `0x102ecd50`

_259 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_102ecd50(char *a0, char *a1, unsigned int a2)
{
    int i;  // [bp-0x120]
    unsigned short v1;  // [bp-0x11c]
    unsigned int v2;  // [bp-0x18]
    char *iter;  // [bp-0x14]
    char *v4;  // [bp-0x10]
    char *j;  // [bp-0xc]
    char *k;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v2 = g_1038e180 ^ &v7;
    for (i = 0; i < 0x100; i += 1)
    {
        *((char *)&v1 + i) = i;
    }
    j = a0;
    iter = a1;
    for (v4 = &a0[a2]; j < v4; j += 1)
    {
        for (k = &v1; *(k) != *(j); k += 1);
        *(iter) = k - &v1;
        iter += 1;
        if (k != &v1)
        {
            sub_10350ec0((char *)&v1 + 1, &v1, k - &v1);
            *((char *)&v1) = *(j);
        }
    }
    return sub_10351225();
}
```

## `sub_102ece60` `0x102ece60`

_127 bytes. (leaf/helper — see body)_

```c
char sub_102ece60(unsigned int a0, unsigned int *a1, int a2)
{
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    char v2;  // [bp-0xd]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v3 = *(a1);
    v1 = sub_1034fef0(a2);
    v4 = v1;
    v2 = 0;
    if (sub_102eca50(a0, v4, a1))
    {
        sub_10350b50(a0, v4, *(a1));
        v2 = 1;
    }
    else
    {
        *(a1) = v3;
    }
    v0 = v4;
    sub_10350eb5(v0);
    return v2;
}
```

## `sub_102ecee0` `0x102ecee0`

_152 bytes. (leaf/helper — see body)_

```c
char sub_102ecee0(int a0, int *a1, int a2)
{
    int v0;  // [bp-0x10]
    int v1;  // [bp-0xc]
    int v2;  // [bp-0x8]

    v1 = sub_1034fef0(a2);
    v2 = v1;
    sub_102ee9d0(a0, v2, a1, a2);
    sub_102ecf80(v2, a0, *(a1));
    sub_102ed090(a0, v2, a1);
    if ((char)sub_102ed2e0(v2, a0, a1, a2))
    {
        v0 = v2;
        sub_10350eb5(v0);
        return 1;
    }
    return 0;
}
```

## `sub_102ecf80` `0x102ecf80`

_260 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_102ecf80(char *a0, char *a1, unsigned int a2)
{
    char v0;  // [bp-0x11d]
    char *v1;  // [bp-0x11c]
    int i;  // [bp-0x118]
    char v3;  // [bp-0x114]
    char v4;  // [bp-0x113]
    unsigned int v5;  // [bp-0x14]
    char *node;  // [bp-0x10]
    char *v7;  // [bp-0xc]
    char *iter;  // [bp-0x8]
    char v9;  // [bp-0x4]

    v5 = g_1038e180 ^ &v9;
    for (i = 0; i < 0x100; i += 1)
    {
        (&v3)[i] = i;
    }
    iter = a0;
    node = a1;
    for (v7 = &a0[a2]; iter < v7; iter += 1)
    {
        v1 = &(&v3)[*(iter)];
        *(node) = *(v1);
        node += 1;
        if (v1 != &v3)
        {
            v0 = *(v1);
            sub_10350ec0(&v4, &v3, v1 - &v3);
            v3 = v0;
        }
    }
    return sub_10351225();
}
```

## `sub_102ed090` `0x102ed090`

_590 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    char field_4;
} struct_0;

int sub_102ed090(struct_0 *node, char *a1, unsigned int *a2)
{
    int v0;  // [bp-0x838]
    int v1;  // [bp-0x834]
    unsigned int v2;  // [bp-0x830]
    unsigned int idx1;  // [bp-0x82c]
    unsigned int v4;  // [bp-0x828]
    int idx;  // [bp-0x824]
    struct_0 *v6;  // [bp-0x820]
    struct_0 *iter1;  // [bp-0x81c]
    unsigned int index;  // [bp-0x818]
    int v9;  // [bp-0x814]
    unsigned int v10;  // [bp-0x810]
    char v11;  // [bp-0x80c]
    char v12;  // [bp-0x410]
    char v13;  // [bp-0x40c]
    char *iter;  // [bp-0x8], Other Possible Types: struct_0 *

    v10 = node->field_0;
    node = &node->field_4;
    *(a2) = *(a2) - 4;
    v1 = sub_1034fef0(-((*(a2) >= 0x20000000 ? 1 : 0) & 1) | *(a2) * 4);
    v9 = v1;
    for (index = 0; index < 0x100; index += 1)
    {
        *((unsigned int *)&(&v11)[4 * index]) = 0;
        *((unsigned int *)&(&v13)[4 * index]) = 0;
    }
    iter1 = node;
    for (v6 = (char *)iter1 + *(a2); iter1 < v6; iter1 = (char *)&iter1->field_0 + 1)
    {
        *((unsigned int *)&(&v11)[4 * (char)iter1->field_0]) = *((int *)&(&v11)[4 * (char)iter1->field_0]) + 1;
    }
    for (idx = 1; idx < 0x100; idx += 1)
    {
        *((unsigned int *)&(&v13)[4 * idx]) = *((int *)&(&v12)[4 * idx]) + (&v10)[idx];
    }
    iter = node;
    for (v4 = 0; v4 < *(a2); iter = (char *)&iter->field_0 + 1)
    {
        *((unsigned int *)(v9 + *((int *)&(&v13)[4 * (char)iter->field_0]) * 4)) = v4;
        *((unsigned int *)&(&v13)[4 * (char)iter->field_0]) = *((int *)&(&v13)[4 * (char)iter->field_0]) + 1;
        v4 += 1;
    }
    iter = a1;
    v2 = 0;
    for (idx1 = v10; v2 < *(a2); idx1 = *((int *)(v9 + idx1 * 4)))
    {
        *(iter) = *((char *)node + idx1);
        iter += 1;
        v2 += 1;
    }
    v0 = v9;
    return sub_10350eb5(v0);
}
```

## `sub_102ed2e0` `0x102ed2e0`

_341 bytes. (leaf/helper — see body)_

```c
int sub_102ed2e0(char *a0, char *a1, int *a2, unsigned int a3)
{
    unsigned int v0;  // [bp-0x1c]
    char *iter;  // [bp-0x18]
    char v2[3];  // [bp-0x14]
    char *v3;  // [bp-0x10]
    char node[3];  // [bp-0xc]
    char v5;  // [bp-0x5]

    node = a0 + 1;
    iter = a1;
    v2 = &a0[*(a2)];
    v3 = &a1[a3];
    v5 = 255;
    if (!*(a0))
    {
        *(a2) = *(a2) - 1;
        return _INSERT(sub_10350b50(a1, a0 + 1, *(a2)), 0, 1);
    }
    while (node < v2 && iter < v3)
    {
        if (node[0] == 255)
        {
            node = &node[1];
            if (node[0] != 255)
            {
                v0 = node[0] + 3;
                node = &node[1];
                if (&iter[v0] >= v3)
                    break;
                while (true)
                {
                    v0 -= 1;
                    if (!v0)
                        break;
                    *(iter) = v5;
                    iter += 1;
                }
            }
            else
            {
                *(iter) = node[0];
                v5 = *(iter);
                iter += 1;
                node = &node[1];
            }
        }
        else
        {
            *(iter) = node[0];
            v5 = *(iter);
            iter += 1;
            node = &node[1];
        }
    }
    *(a2) = iter - a1;
    return node == v2;
}
```

## `sub_102ed344` `0x102ed344`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102ed344(void)
{
}
```

## `sub_102ed440` `0x102ed440`

_108 bytes. (leaf/helper — see body)_

```c
char sub_102ed440(unsigned int a0, int *a1, unsigned int a2)
{
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v1 = sub_1034fef0(a2);
    v2 = v1;
    if (!(char)sub_102ed2e0(a0, v2, a1, a2))
        return 0;
    sub_10350b50(a0, v2, *(a1));
    v0 = v2;
    sub_10350eb5(v0);
    return 1;
}
```

## `sub_102ed4a6` `0x102ed4a6`

_2 bytes. (leaf/helper — see body)_

```c
void sub_102ed4a6(void)
{
}
```

## `sub_102ed4b0` `0x102ed4b0`

_167 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
} struct_0;

unsigned int sub_102ed4b0(struct_0 **a0, char *iter, unsigned int a2)
{
    int i;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    if (a2)
    {
        v1 = a0[1] - iter;
        if (a2 < v1)
            return sub_102edf80(&iter[a2]);
        a2 -= v1;
        return sub_102edf80(&(*(a0))[a2]);
    }
    else
    {
        v2 = 0;
        for (i = 0; i < 4; i += 1)
        {
            v2 = v2 * 0x100 | *(iter);
            iter += 1;
            if (iter >= a0[1])
                iter = &*(a0)->field_0;
        }
        return v2;
    }
}
```

## `sub_102ed4ef` `0x102ed4ef`

_2 bytes. (leaf/helper — see body)_

```c
void sub_102ed4ef(void)
{
}
```

