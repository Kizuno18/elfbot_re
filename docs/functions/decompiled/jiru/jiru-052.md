# elfbot.dll decompiled — jiru 0x10341220..0x10343340

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10341220` `0x10341220`

_61 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_1 *field_0;
    unsigned int field_4;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

unsigned int sub_10341220(struct_0 *a0)
{
    unsigned int v3;  // eax
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    if (!a0->field_0 || !a0->field_4)
        sub_10353616(a0, &v1);
    v3 = sub_10341600();
    if (v3 >= a0->field_0->field_0)
        sub_10353616();
    return a0->field_4;
}
```

## `sub_10341260` `0x10341260`

_26 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
} struct_0;

int sub_10341260(struct_0 *a0)
{
    return 1 << ((char)a0->field_8 & 31);
}
```

## `sub_10341280` `0x10341280`

_28 bytes. (leaf/helper — see body)_

```c
int sub_10341280(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10341590(a0, a0, &v1);
    return a1;
}
```

## `sub_103412a0` `0x103412a0`

_51 bytes. (leaf/helper — see body)_

```c
int sub_103412a0(int a0, unsigned int a1, int a2)
{
    sub_103413d0(a0, a0);
    sub_103413d0(sub_10341660(a2));
    return a1;
}
```

## `sub_103412e0` `0x103412e0`

_57 bytes. (leaf/helper — see body)_

```c
unsigned int [2] sub_103412e0(int *a0, unsigned int *a1, int a2)
{
    unsigned int v1[2];  // eax
    unsigned int v2;  // edx
    char v0;  // [bp+0x0]

    v1 = sub_10341680(a2, a0, *(a0), a0[1], &v0);
    v2 = v1[1];
    *(a1) = v1[0];
    a1[1] = v2;
    return a1;
}
```

## `sub_10341320` `0x10341320`

_168 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int [25] sub_10341320(unsigned int *a0, unsigned int *index)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4148
    unsigned long v10;  // 4164
    unsigned long v11;  // 4155
    unsigned int v0;  // [bp-0x18]
    unsigned int idx[25];  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_103706f1;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    idx = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    idx = a0;
    idx[0] = *(index);
    sub_103145d0(&idx[1], index + 1);
    v4 = 0;
    sub_103145d0(&idx[8], index + 8);
    v4 = 1;
    sub_103413f0(index + 15);
    idx[23] = index[23];
    idx[24] = index[24];
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return idx;
}
```

## `sub_103413d0` `0x103413d0`

_28 bytes. (leaf/helper — see body)_

```c
int sub_103413d0(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10341590(a1, a0, &v1);
    return a0;
}
```

## `sub_103413f0` `0x103413f0`

_160 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    char field_8;
    char padding_9[3];
    unsigned int field_c;
    unsigned int field_10;
    unsigned int field_14;
} struct_0;

extern unsigned int g_1038e180;

struct_0 * sub_103413f0(struct_0 *idx, struct_0 *index)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4168
    unsigned int v8;  // eax
    unsigned long v9;  // 4184
    unsigned long v10;  // 4123
    struct_0 *v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v8 = *((int *)v7);
    v1 = *((int *)v7);
    v0 = idx;
    v9 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v9) = &v1;
    idx->field_0 = index->field_0;
    idx->field_4 = index->field_4;
    idx->field_8 = index->field_8;
    idx->field_c = index->field_c;
    idx->field_10 = index->field_10;
    idx->field_14 = index->field_14;
    sub_10341490(index + 1, g_1038e180 ^ &v2, idx, v8, sub_1037071b, -1, &v3);
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v10) = v8;
    return idx;
}
```

## `sub_10341490` `0x10341490`

_84 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10341490(int a0, int a1)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4138
    unsigned int v8;  // eax
    unsigned long v9;  // 4154
    unsigned long v10;  // 4123
    int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v8 = *((int *)v7);
    v1 = *((int *)v7);
    v0 = a0;
    v9 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v9) = &v1;
    sub_103416d0(a1, g_1038e180 ^ &v2, a0, v8, sub_10370748, -1, &v3);
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v10) = v8;
    return a0;
}
```

## `sub_103414f0` `0x103414f0`

_35 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
} struct_0;

int sub_103414f0(struct_0 *a0, int a1)
{
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_103323a0(a1, v0->field_4, v0);
    return a1;
}
```

## `sub_10341520` `0x10341520`

_57 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10341520(unsigned int *a0)
{
    unsigned int v0;  // [bp-0xc]

    v0 = (!a0[1] ? 0 : (int)((a0[3] - a0[1]) / 100));
    return v0;
}
```

## `sub_10341560` `0x10341560`

_46 bytes. (leaf/helper — see body)_

```c
int sub_10341560(int a0, int a1, int a2, int a3)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10343260(a1, a2, a3, a0, a0, &v1);
    return a2 * 100 + a1;
}
```

## `sub_10341590` `0x10341590`

_28 bytes. (leaf/helper — see body)_

```c
int sub_10341590(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_103415b0(a1, a0, &v1);
    return a0;
}
```

## `sub_103415b0` `0x103415b0`

_71 bytes. (leaf/helper — see body)_

```c
unsigned int [3] sub_103415b0(unsigned int *idx, unsigned int *index)
{
    unsigned int v0[3];  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = idx;
    sub_10341910(idx, &v1);
    idx[1] = index[1];
    idx[2] = index[2];
    if (!*(index))
        sub_10353616();
    *(idx) = *(index);
    return idx;
}
```

## `sub_10341600` `0x10341600`

_53 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
    int field_8;
} struct_0;

int sub_10341600(struct_0 *a0)
{
    unsigned int v2;  // eax
    char v0;  // [bp+0x0]

    v2 = sub_10341710(a0, a0->field_8, &v0);
    return (a0->field_4 - v2 >> 2) * 32 + a0->field_8;
}
```

## `sub_10341640` `0x10341640`

_32 bytes. (leaf/helper — see body)_

```c
int sub_10341640(int a0, int a1, int a2)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10341740(a1, a2, a0, &v1);
    return a0;
}
```

## `sub_10341660` `0x10341660`

_28 bytes. (leaf/helper — see body)_

```c
int sub_10341660(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10341760(a1, a0, &v1);
    return a0;
}
```

## `sub_10341680` `0x10341680`

_28 bytes. (leaf/helper — see body)_

```c
int sub_10341680(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10341870(a1, a0, &v1);
    return a0;
}
```

## `sub_103416a0` `0x103416a0`

_35 bytes. (leaf/helper — see body)_

```c
int sub_103416a0(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return -(0 < (sub_103418d0(a1, a0, &v1) & 0xff)) + 1;
}
```

## `sub_103416d0` `0x103416d0`

_54 bytes. (leaf/helper — see body)_

```c
char * sub_103416d0(char *a0, unsigned int a1)
{
    char *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    *(v0) = 0;
    if ((char)sub_103315c0(a1))
        sub_10341930(sub_10331570(a1));
    return v0;
}
```

## `sub_10341710` `0x10341710`

_33 bytes. (leaf/helper — see body)_

```c
int sub_10341710(unsigned int *a0)
{
    char v0;  // [bp-0xc]

    return *((int *)(sub_103414f0(*(a0) + 4, &v0) + 4));
}
```

## `sub_10341740` `0x10341740`

_32 bytes. (leaf/helper — see body)_

```c
int sub_10341740(int a0, int a1, int a2)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10341980(a1, a2, a0, &v1);
    return a0;
}
```

## `sub_10341760` `0x10341760`

_257 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
    int field_8;
} struct_0;

struct_0 * sub_10341760(struct_0 *a0, unsigned int a1)
{
    int v1;  // eax
    struct_0 *idx;  // [bp-0x8]

    idx = a0;
    idx = a0;
    if (!a1)
        return idx;
    if (!idx->padding_0 || !idx->field_4)
        sub_10353616();
    if (a1 >= 0)
    {
        v1 = sub_10341600(idx);
        if (v1 + a1 > *((int *)idx->padding_0))
            sub_10353616();
    }
    else if (sub_10341600(idx) < !(a1))
    {
        sub_10353616();
    }
    if (a1 < 0 && idx->field_8 < !(a1))
    {
        idx->field_8 = idx->field_8 + a1;
        idx->field_4 = idx->field_4 - ((4294967295 - idx->field_8 >> 5) * 4 + 4);
        idx->field_8 = idx->field_8 % 32;
    }
    else
    {
        idx->field_8 = idx->field_8 + a1;
        idx->field_4 = idx->field_4 + (idx->field_8 >> 5) * 4;
        idx->field_8 = idx->field_8 % 32;
    }
    return idx;
}
```

## `sub_10341870` `0x10341870`

_96 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_1 *field_0;
    unsigned int field_4;
} struct_0;

typedef struct struct_1 {
    char padding_0[4];
    unsigned int field_4;
    unsigned int field_8;
} struct_1;

struct_0 * sub_10341870(struct_0 *idx, unsigned int a1)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = idx;
    if (!idx->field_0)
        sub_10353616(idx, &v1);
    if (a1 * 100 + idx->field_4 > idx->field_0->field_8 || a1 * 100 + idx->field_4 < idx->field_0->field_4)
        sub_10353616();
    idx->field_4 = a1 * 100 + idx->field_4;
    return idx;
}
```

## `sub_103418d0` `0x103418d0`

_57 bytes. (leaf/helper — see body)_

```c
int sub_103418d0(unsigned int *a0, unsigned int a1)
{
    unsigned int v0[2];  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    if (!*(a0) || *(a0) != *((int *)a1))
        sub_10353616(a0, &v1);
    return _INSERT(a0[1], 0, a0[1] == *((int *)(a1 + 4)));
}
```

## `sub_10341910` `0x10341910`

_22 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_10341910(unsigned int *a0)
{
    unsigned int *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_10338af0(v0);
    return v0;
}
```

## `sub_10341930` `0x10341930`

_76 bytes. (leaf/helper — see body)_

```c
int sub_10341930(char *a0, unsigned int *a1)
{
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0x8]

    v2 = sub_1031acf0(4, sub_1031a280(a0 + 4));
    v1 = v2;
    if (v1)
    {
        v2 = sub_10314db0(v1, a1);
        v0 = v2;
    }
    else
    {
        v0 = 0;
    }
    *(a0) = 1;
    return v2;
}
```

## `sub_10341980` `0x10341980`

_62 bytes. (leaf/helper — see body)_

```c
unsigned int [3] sub_10341980(unsigned int *a0, unsigned int a1, unsigned int a2)
{
    unsigned int idx[3];  // [bp-0x8]

    idx = a0;
    idx = a0;
    sub_10341910(idx);
    idx[1] = a1;
    idx[2] = 0;
    if (!a2)
        sub_10353616();
    idx[0] = a2;
    return idx;
}
```

## `sub_103419c0` `0x103419c0`

_197 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern unsigned int g_1038e180;

struct_0 ** sub_103419c0(int a0, struct_0 **a1)
{
    unsigned long v11;  // ldt
    unsigned long v12;  // gdt
    unsigned short v13;  // fs
    unsigned long v14;  // 4140
    unsigned long v15;  // 4154
    unsigned long v16;  // 4117
    unsigned int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x2c]
    unsigned int v2;  // [bp-0x28]
    unsigned int v3;  // [bp-0x24]
    unsigned int v4;  // [bp-0x1c]
    char v5;  // [bp-0x18]
    unsigned int v6;  // [bp-0x14]
    unsigned int v7;  // [bp-0x10]
    unsigned int v8;  // [bp-0xc]
    unsigned int v9;  // [bp-0x8]
    char v10;  // [bp-0x4]

    v9 = 4294967295;
    v8 = sub_103707a2;
    v14 = _ccall(v11, v12, (unsigned int)v13, 0);
    v7 = *((int *)v14);
    v0 = g_1038e180 ^ &v10;
    v15 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int **)v15) = &v7;
    v4 = 0;
    if ((unsigned int)sub_1032e0a0(a0 + 160))
    {
        v3 = (unsigned int)sub_103301b0(a0 + 160);
    }
    else
    {
        v2 = sub_103134d0(&v5);
        v1 = v2;
        v9 = 1;
        v4 |= 1;
        v3 = v1;
    }
    v6 = v3;
    sub_10314db0(a1, v6);
    v4 |= 2;
    v9 = 0;
    if (((char)v4 & 1))
    {
        v4 &= 4294967294;
        sub_103130c0(&v5);
    }
    v16 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int *)v16) = v7;
    return a1;
}
```

## `sub_10341a90` `0x10341a90`

_250 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[40];
    int field_28;
    char padding_2c[4];
    char field_30;
} struct_0;

struct_0 * sub_10341a90(struct_0 *idx)
{
    int v0;  // [bp-0x28]
    char v1;  // [bp-0x20]
    char v2;  // [bp-0x14]
    unsigned int i;  // [bp-0x8]

    for (i = 0; i < sub_10340990(idx); i += 1)
    {
        if (!sub_10336b20(&idx->padding_0[16]) || *((int *)sub_103409d0(idx, i)) < 0 || !(char)sub_10340c70(sub_10340870(&idx->padding_0[16], &v2, *((int *)sub_103409d0(idx, i)))))
        {
            sub_103409d0(idx, i);
            sub_10343540(0, v0);
        }
    }
    idx->field_28 = 0;
    if (!sub_10336b20(&idx->padding_0[16]))
        return idx;
    for (idx->field_30 = 0; idx->field_28 < idx->padding_2c; idx->field_28 = idx->field_28 + 1)
    {
        if (!(char)sub_10340c70(sub_10340870(&idx->padding_0[16], &v1, idx->field_28)))
            return idx;
    }
    return idx;
}
```

## `sub_10341b90` `0x10341b90`

_150 bytes. (leaf/helper — see body)_

```c
int sub_10341b90(unsigned int *a0)
{
    unsigned int v0;  // [bp-0x14]
    unsigned int v1[16];  // [bp-0x10]
    int v2;  // [bp-0xc], Other Possible Types: unsigned int
    unsigned int i;  // [bp-0x8]

    v2 = sub_1031e920(a0 + 13);
    for (i = 0; i < sub_10340990(a0); i += 1)
    {
        v1 = sub_103409d0(a0, i);
        v2 += sub_1031e920(&v1[1]);
        if (v1[0] == 4294967294)
        {
            v0 = v1[15];
            v2 = *((int *)sub_10344750(&v2, &v0));
        }
        v2 += sub_1031e920(&v1[8]);
    }
    return v2;
}
```

## `sub_10341c30` `0x10341c30`

_17 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[80];
    char field_50;
} struct_0;

int sub_10341c30(struct_0 *a0)
{
    return _INSERT(a0, 0, a0->field_50);
}
```

## `sub_10341c50` `0x10341c50`

_407 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10341c50(unsigned int a0, unsigned int a1)
{
    unsigned long v18;  // ldt
    unsigned long v19;  // gdt
    unsigned short v20;  // fs
    unsigned long v21;  // 4141
    unsigned long v22;  // 4155
    int v23;  // ecx
    unsigned int v24;  // eax
    unsigned long v25;  // 4113
    int v0;  // [bp-0x114]
    unsigned int v1[25];  // [bp-0x108]
    unsigned int v2;  // [bp-0xa4]
    unsigned int v3[25];  // [bp-0xa0]
    unsigned int v4[25];  // [bp-0x9c]
    unsigned int v5;  // [bp-0x98]
    unsigned int v6;  // [bp-0x94]
    unsigned int v7;  // [bp-0x90]
    unsigned int v8;  // [bp-0x8c]
    char *v9;  // [bp-0x84]
    unsigned int v10[25];  // [bp-0x80]
    void* v11;  // [bp-0x1c]
    unsigned int i;  // [bp-0x18]
    char v13;  // [bp-0x11]
    unsigned int v14;  // [bp-0x10]
    unsigned int v15;  // [bp-0xc]
    unsigned int v16;  // [bp-0x8]
    char v17;  // [bp-0x4]

    v16 = 4294967295;
    v15 = sub_103707d8;
    v21 = _ccall(v18, v19, (unsigned int)v20, 0);
    v14 = *((int *)v21);
    v2 = g_1038e180 ^ &v17;
    v22 = _ccall(v18, v19, (unsigned int)v20, 0);
    *((unsigned int **)v22) = &v14;
    v8 = sub_103419c0(a0, &v11);
    v7 = v8;
    v16 = 0;
    v13 = sub_10314d20(sub_10314e10(v7), 32);
    v16 = 4294967295;
    sub_103130c0(&v11);
    if (!sub_10340990(a0))
    {
        v6 = sub_10340a80(v10, v13);
        v5 = v6;
        v16 = 1;
        sub_103435f0(a1, v5);
        v16 = 4294967295;
        sub_103407b0(v10);
    }
    else
    {
        if (a1 > sub_10340990(a0))
        {
            v9 = v1;
            v4 = sub_10340a80(v1, v13);
            v3 = v4;
            v16 = 2;
            v16 = 4294967295;
            sub_103408b0(a0, a1);
        }
        sub_10343560(0, 0);
        for (i = 0; i < a1; i += 1)
        {
            v23 = _INSERT(0, 0, v13);
            sub_103409d0(a0, i);
            sub_10344780(v23, v0);
        }
    }
    v24 = sub_10343540(0);
    v25 = _ccall(v18, v19, (unsigned int)v20, 0);
    *((unsigned int *)v25) = v14;
    return v24;
}
```

## `sub_10341df0` `0x10341df0`

_418 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10341df0(unsigned int a0, char a1, int a2, char a3)
{
    unsigned long v17;  // ldt
    unsigned long v18;  // gdt
    unsigned long v27;  // 4119
    unsigned short v19;  // fs
    unsigned long v20;  // 4137
    unsigned long v21;  // 4153
    char *v22;  // eax
    char *v23;  // eax
    void* v24;  // eax
    unsigned int v25[2];  // eax
    int v26[2];  // eax
    unsigned int v0;  // [bp-0x70]
    unsigned int v1;  // [bp-0x6c]
    unsigned int v2;  // [bp-0x64]
    unsigned int v3;  // [bp-0x5c]
    unsigned int v4;  // [bp-0x58]
    struct struct_0 *v5[2];  // [bp-0x54]
    char v6;  // [bp-0x4c]
    unsigned int v7[2];  // [bp-0x44]
    struct struct_0 *v8[2];  // [bp-0x3c]
    struct struct_0 *v9[2];  // [bp-0x34]
    unsigned int v10[5];  // [bp-0x2c]
    unsigned int node;  // [bp-0x18]
    unsigned int iter;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]
    char v16;  // [bp-0x4]

    v15 = 4294967295;
    v14 = sub_10370808;
    v20 = _ccall(v17, v18, (unsigned int)v19, 0);
    v13 = *((int *)v20);
    v2 = g_1038e180 ^ &v16;
    v21 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((unsigned int **)v21) = &v13;
    iter = 0;
    node = 0;
    while (true)
    {
        iter = sub_10338710(a0, a1, iter);
        if (iter == 4294967295)
            break;
        if (iter + 1 >= sub_1031e920(a0))
        {
            if ((a3 & 1))
            {
                v4 = sub_1033fa30(v10, iter, sub_1031e920(a0));
                v3 = v4;
                v15 = 0;
                sub_1033fc20(v3);
                v15 = 4294967295;
                sub_1033fbd0(v10);
            }
            else
            {
                node += 1;
                break;
            }
        }
        v22 = sub_103189a0(a0, iter + 1);
        v23 = sub_103189a0(a0, iter);
        if (*(v22) == *(v23))
        {
            iter += 2;
        }
        else
        {
            iter += 1;
            v24 = sub_10340120(a0, v5);
            v25 = sub_10340150(a0, v9);
            v1 = v25[1];
            v0 = v25[0];
            v26 = sub_10340a40(sub_10340120(a0, v8), v7, iter);
            iter = sub_1031ba20(sub_103447e0(&v6, a2, v26[0], v26[1]), v24);
            if (iter < sub_1031e920(a0) && *((char *)sub_103189a0(a0, iter)) == a1)
                iter += 1;
            node += 1;
        }
    }
    v27 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((unsigned int *)v27) = v13;
    return node;
}
```

## `sub_10341fa0` `0x10341fa0`

_86 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

int sub_10341fa0(unsigned int a0, struct_0 *a1, unsigned int a2, unsigned int a3)
{
    unsigned int v6[2];  // eax
    int v7[2];  // eax
    unsigned int v0;  // [bp-0x2c]
    unsigned int v1;  // [bp-0x28]
    unsigned int v2[2];  // [bp-0x24]
    struct struct_0 *v3[2];  // [bp-0x1c]
    unsigned int v4[2];  // [bp-0x14]
    struct struct_0 *v5[2];  // [bp-0xc]

    v6 = sub_10340a40(sub_10340120(a1, v5), v4, a3);
    v1 = v6[1];
    v0 = v6[0];
    v7 = sub_10340a40(sub_10340120(a1, v3), v2, a2);
    return sub_103434f0(v7[0], v7[1]);
}
```

## `sub_10342000` `0x10342000`

_2439 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    char padding_4[56];
    unsigned int field_3c;
    unsigned int field_40;
    char field_44;
    char padding_45[3];
    unsigned int field_48;
    char padding_4c[16];
    unsigned int field_5c;
    unsigned int field_60;
} struct_0;

typedef struct struct_1 {
    struct_0 field_0;
    unsigned int field_4;
} struct_1;

typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;


char sub_10342000(struct_1 *a0, int *a1, struct_0 *idx, unsigned int a3, unsigned int a4, char a5)
{
    unsigned int v23;  // esi
    int v24;  // eax
    unsigned int v33[2];  // eax
    unsigned int v34;  // edx
    struct_1 *v35;  // eax
    char *v38;  // eax
    char v39;  // al
    char *v42;  // eax
    char v43;  // al
    int v44;  // edx
    int v45;  // eax
    char *v47;  // eax
    char v48;  // al
    unsigned int v49[2];  // eax
    unsigned int v50;  // eax
    struct_1 *v51;  // ecx
    int v52;  // ecx
    char *v26;  // eax
    unsigned int v53[2];  // eax
    unsigned int v54;  // edx
    struct_1 *v55;  // eax
    char *v58;  // eax
    char v59;  // al
    char *v60;  // eax
    char v61;  // al
    unsigned int v62[2];  // eax
    char v27;  // al
    unsigned int v63;  // eax
    struct_1 *v64;  // ecx
    int v65;  // ecx
    unsigned int v66[2];  // eax
    unsigned int v67;  // edx
    struct_1 *v68;  // eax
    char *v69;  // eax
    char v70;  // al
    char *v71;  // eax
    char v72;  // al
    char *v73;  // eax
    char v74;  // al
    char *v77;  // eax
    char v78;  // al
    char *v79;  // eax
    int v80;  // eax
    int v83;  // eax
    char *v85;  // eax
    char v86;  // al
    char *v30;  // eax
    char v31;  // al
    int v32;  // ecx
    unsigned int v0;  // [bp-0x88]
    unsigned int v1;  // [bp-0x84]
    unsigned int v2;  // [bp-0x80]
    unsigned int v3;  // [bp-0x70]
    unsigned int v4;  // [bp-0x68]
    unsigned int v5;  // [bp-0x64]
    unsigned int v6;  // [bp-0x60]
    unsigned int v7;  // [bp-0x5c]
    unsigned int v8;  // [bp-0x58]
    unsigned int v9;  // [bp-0x50]
    unsigned int v10;  // [bp-0x4c]
    unsigned int v11;  // [bp-0x48]
    char v12;  // [bp-0x44]
    char v13;  // [bp-0x3c]
    char v14;  // [bp-0x34]
    char v15;  // [bp-0x2c]
    char v16;  // [bp-0x24]
    char v17;  // [bp-0x1c], Other Possible Types: unsigned int
    char v18;  // [bp-0x15]
    unsigned int v19;  // [bp-0x14]
    unsigned int v20;  // [bp-0x10]
    unsigned int v21;  // [bp-0xc]
    char v22;  // [bp-0x5]

    v9 = v23;
    idx->field_0 = 4294967295;
    v22 = 0;
    v18 = 0;
    v19 = (unsigned int)a0->field_0.padding_0;
    v20 = a0->field_0.field_4;
    v21 = sub_1031ba20(a1, &v19) + a4;
    if ((char)sub_10343640(a1))
    {
        v8 = v21;
        v24 = sub_1031ba20(a0, &v19) + a4;
        sub_10342a90(_INSERT(v24, 0, a5), v24);
        return 0;
    }
    v26 = sub_10334250(a0);
    v27 = sub_10314d20(sub_10337e90(a3), 124);
    if (*(v26) == v27)
    {
        v18 = 1;
        sub_10342b10(a1);
        if ((char)sub_10343640(a1))
        {
            v7 = v21;
            sub_10342a90(_INSERT(0, 0, a5), sub_1031ba20(a0, &v19) + a4);
            return 0;
        }
    }
    v30 = sub_10334250(a0);
    v31 = sub_10314d20(sub_10337e90(a3), 48);
    if (*(v30) != v31 && !((v32 = (int)_INSERT(0, 0, *((char *)sub_10334250(a0))), !(char)sub_10344840(a3, _INSERT(0, 0, *((char *)sub_10334250(a0)))))))
    {
        v33 = sub_10344860(&v16, a0, a1, &v17, a3);
        v34 = v33[1];
        v35 = a0;
        *((unsigned int *)&v35->field_0.padding_0[0]) = v33[0];
        v35->field_0.field_4 = v34;
        if ((char)sub_10343640(a1))
        {
            v6 = v21;
            sub_10342a90(_INSERT(0, 0, a5), sub_1031ba20(a0, &v19) + a4);
            return 0;
        }
        v38 = sub_10334250(a0);
        v39 = sub_10314d20(sub_10337e90(a3), 37);
        if (*(v38) == v39)
        {
            idx->field_0 = v17 - 1;
            sub_10342b10();
            if (!v18)
                return 1;
            v6 = v21;
            sub_10342a90(_INSERT(0, 0, a5), sub_1031ba20(a0, &v19) + a4);
        }
        v42 = sub_10334250(a0);
        v43 = sub_10314d20(sub_10337e90(a3), 36);
        if (*(v42) == v43)
        {
            idx->field_0 = v17 - 1;
            sub_10342b10();
        }
        else
        {
            idx->field_3c = v17;
            idx->field_0 = 4294967295;
            goto LABEL_1034242e;
        }
    }
    while (true)
    {
        if ((char)sub_10343610(a1))
        {
            v5 = 0;
            v44 = _INSERT(0, 0, *((char *)sub_10334250(a0)));
            v11 = (char)sub_10344920(a3, v44);
            switch ((char)sub_10344920(a3, v44))
            {
            case 32:
                idx->field_60 = idx->field_60 | 2;
                break;
            case 35:
                idx->field_48 = idx->field_48 | 24;
                break;
            case 39:
                break;
            case 43:
                idx->field_48 = idx->field_48 | 32;
                break;
            case 45:
                idx->field_48 = idx->field_48 | 64;
                break;
            case 48:
                idx->field_60 = idx->field_60 | 1;
                break;
            case 61:
                idx->field_60 = idx->field_60 | 4;
                break;
            case 95:
                idx->field_48 = idx->field_48 | 0x100;
                break;
            case 104: case 108:
                break;
            default:
                goto LABEL_10342379;
            }
            sub_10342b10();
        }
        else
        {
            if ((char)sub_10343640(a1))
            {
                v4 = v21;
                v45 = sub_1031ba20(a0, &v19) + a4;
                sub_10342a90(_INSERT(v45, 0, a5), v45);
                return 1;
            }
LABEL_10342379:
            v47 = sub_10334250(a0);
            v48 = sub_10314d20(sub_10337e90(a3), 42);
            if (*(v47) == v48)
            {
                v49 = sub_10344970(&v15, a0->field_0.padding_0, a0->field_0.field_4, *(a1), a1[1], a3);
                v50 = v49[1];
                v51 = a0;
                *((unsigned int *)&v51->field_0.padding_0[0]) = v49[0];
                v51->field_0.field_4 = v50;
                break;
            }
        }
    }
    if ((char)sub_10343610(a1))
    {
        v52 = _INSERT(0, 0, *((char *)sub_10334250(a0)));
        if ((char)sub_10344840(a3, v52))
        {
            v53 = sub_10344860(&v14, a0, a1, &idx->field_3c, a3);
            v54 = v53[1];
            v55 = a0;
            *((unsigned int *)&v55->field_0.padding_0[0]) = v53[0];
            v55->field_0.field_4 = v54;
        }
    }
LABEL_1034242e:
    if ((char)sub_10343640(a1))
    {
        v3 = v21;
        sub_10342a90(_INSERT(0, 0, a5), sub_1031ba20(a0, &v19) + a4);
        return 1;
    }
    v58 = sub_10334250(a0);
    v59 = sub_10314d20(sub_10337e90(a3), 46);
    if (*(v58) == v59)
    {
        sub_10342b10();
        if ((char)sub_10343610(a1))
        {
            v60 = sub_10334250(a0);
            v61 = sub_10314d20(sub_10337e90(a3), 42);
            if (*(v60) == v61)
            {
                v62 = sub_10344970(&v13, a0->field_0.padding_0, a0->field_0.field_4, *(a1), a1[1], a3);
                v63 = v62[1];
                v64 = a0;
                *((unsigned int *)&v64->field_0.padding_0[0]) = v62[0];
                v64->field_0.field_4 = v63;
            }
        }
        if ((char)sub_10343610(a1) && !((v65 = (int)_INSERT(0, 0, *((char *)sub_10334250(a0))), !(char)sub_10344840(a3, _INSERT(0, 0, *((char *)sub_10334250(a0)))))))
        {
            v66 = sub_10344860(&v12, a0, a1, &idx->field_40, a3);
            v67 = v66[1];
            v68 = a0;
            *((unsigned int *)&v68->field_0.padding_0[0]) = v66[0];
            v68->field_0.field_4 = v67;
            v22 = 1;
        }
        else
        {
            idx->field_40 = 0;
        }
    }
    while ((char)sub_10343610(a1))
    {
        v69 = sub_10334250(a0);
        v70 = sub_10314d20(sub_10337e90(a3), 108);
        if (*(v69) != v70)
        {
            v71 = sub_10334250(a0);
            v72 = sub_10314d20(sub_10337e90(a3), 76);
            if (*(v71) != v72)
            {
                v73 = sub_10334250(a0);
                v74 = sub_10314d20(sub_10337e90(a3), 104);
                if (*(v73) != v74)
                    break;
            }
        }
        sub_10342b10();
    }
    if ((char)sub_10343640(a1))
    {
        v2 = v21;
        sub_10342a90(_INSERT(0, 0, a5), sub_1031ba20(a0, &v19) + a4);
        return 1;
    }
    if (v18)
    {
        v77 = sub_10334250(a0);
        v78 = sub_10314d20(sub_10337e90(a3), 124);
        if (*(v77) == v78)
        {
            sub_10342b10();
            return 1;
        }
    }
    v2 = 0;
    v79 = sub_10334250(a0);
    v80 = _INSERT(v79, 0, *(v79));
    v10 = (char)sub_10344920(a3, v80);
    switch ((char)sub_10344920(a3, v80))
    {
    case 67: case 99:
        idx->field_5c = 1;
        break;
    case 71:
        idx->field_48 = idx->field_48 | 4;
        break;
    case 83: case 115:
        if (v22)
            idx->field_5c = idx->field_40;
        idx->field_40 = 6;
        break;
    case 84:
        sub_10342b10();
        if ((char)sub_10343640(a1))
        {
            v1 = v21;
            sub_10342a90(_INSERT(0, 0, a5), sub_1031ba20(a0, &v19) + a4);
        }
        else
        {
            idx->field_44 = *((char *)sub_10334250(a0));
        }
        idx->field_60 = idx->field_60 | 8;
        idx->field_0 = 4294967294;
        break;
    case 103:
        idx->field_48 = idx->field_48 & 4294963711;
        idx->field_48 = idx->field_48 | 0x200;
        idx->field_48 = idx->field_48 & 4294955007;
        break;
    case 110:
        idx->field_0 = 4294967293;
        break;
    case 111:
        idx->field_48 = idx->field_48 & 4294963711;
        idx->field_48 = idx->field_48 | 0x400;
        break;
    case 116:
        idx->field_44 = sub_10314d20(sub_10337e90(a3), 32);
        idx->field_60 = idx->field_60 | 8;
        idx->field_0 = 4294967294;
        break;
    case 69:
        idx->field_48 = idx->field_48 | 4;
    case 101:
        idx->field_48 = idx->field_48 & 4294955007;
        idx->field_48 = idx->field_48 | 0x1000;
        idx->field_48 = idx->field_48 & 4294963711;
        idx->field_48 = idx->field_48 | 0x200;
        break;
    case 88:
        idx->field_48 = idx->field_48 | 4;
    case 112: case 120:
        idx->field_48 = idx->field_48 & 4294963711;
        idx->field_48 = idx->field_48 | 0x800;
        break;
    case 102:
        idx->field_48 = idx->field_48 & 4294955007;
        idx->field_48 = idx->field_48 | 0x2000;
    case 100: case 105: case 117:
        idx->field_48 = idx->field_48 & 4294963711;
        idx->field_48 = idx->field_48 | 0x200;
        break;
    default:
        v2 = v21;
        v83 = sub_1031ba20(a0, &v19) + a4;
        sub_10342a90(_INSERT(v83, 0, a5), v83);
        break;
    }
    sub_10342b10();
    if (!v18)
        return 1;
    if ((char)sub_10343610(a1))
    {
        v85 = sub_10334250(a0);
        v86 = sub_10314d20(sub_10337e90(a3), 124);
        if (*(v85) == v86)
        {
            sub_10342b10();
            return 1;
        }
    }
    v0 = v21;
    sub_10342a90(_INSERT(0, 0, a5), sub_1031ba20(a0, &v19) + a4);
    return 1;
}
```

## `sub_1034210a` `0x1034210a`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1034210a(void)
{
}
```

## `sub_10342252` `0x10342252`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10342252(void)
{
}
```

## `sub_10342330` `0x10342330`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10342330(void)
{
}
```

## `sub_1034296c` `0x1034296c`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1034296c(void)
{
}
```

## `sub_10342a90` `0x10342a90`

_120 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10342a90(char a0, unsigned int a1, unsigned int a2)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4168
    unsigned long v12;  // 4172
    unsigned int v13;  // eax
    unsigned int v14;  // eax
    unsigned long v15;  // 4113
    unsigned int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x2c]
    unsigned int v2;  // [bp-0x28]
    unsigned int v3[5];  // [bp-0x24]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_10370838;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v0 = g_1038e180 ^ &v7;
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    v13 = a0;
    v14 = v13 & 1;
    if (((char)v13 & 1))
    {
        v2 = sub_1033fa30(v3, a1, a2);
        v1 = v2;
        v6 = 0;
        sub_1033fc20(v1);
        v6 = 4294967295;
        v14 = sub_1033fbd0(v3);
    }
    v15 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v15) = v4;
    return v14;
}
```

## `sub_10342b10` `0x10342b10`

_81 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
    unsigned int field_4;
} struct_1;

typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

struct_1 * sub_10342b10(struct_1 *a0)
{
    struct_0 *v2;  // eax
    struct_1 *idx;  // [bp-0x8]

    idx = a0;
    idx = a0;
    if (idx->field_0 != 0xfffffffe)
    {
        if (!idx->field_0)
            sub_10353616();
        v2 = sub_10314a50(idx->field_0);
        if (idx->field_4 >= &v2->padding_0[idx->field_0->field_14])
            sub_10353616();
    }
    idx->field_4 = idx->field_4 + 1;
    return idx;
}
```

## `sub_10342b70` `0x10342b70`

_131 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[68];
    char field_44;
    char padding_45[3];
    unsigned int field_48;
    char padding_4c[20];
    unsigned int field_60;
} struct_0;

struct_0 * sub_10342b70(struct_0 *a0)
{
    struct_0 *v2;  // eax
    struct_0 *idx;  // [bp-0x8]

    idx = a0;
    idx = a0;
    if (((char)idx->field_60 & 1))
    {
        if (((char)idx->field_48 & 64))
        {
            idx->field_60 = idx->field_60 & 4294967294;
        }
        else
        {
            idx->field_60 = idx->field_60 & 4294967293;
            idx->field_44 = 48;
            idx->field_48 = idx->field_48 & 4294966847 | 0x100;
        }
    }
    v2 = idx->field_60 & 2;
    if (((char)idx->field_60 & 2) && ((char)idx->field_48 & 32))
    {
        v2 = idx;
        idx->field_60 = v2->field_60 & 4294967293;
    }
    return v2;
}
```

## `sub_10342c00` `0x10342c00`

_141 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern int g_1039fe84;

unsigned int sub_10342c00(int a0)
{
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // fs
    unsigned long v13;  // 4137
    unsigned long v14;  // 4151
    unsigned int v15;  // eax
    unsigned long v16;  // 4113
    int v0;  // [bp-0x74]
    unsigned int v1;  // [bp-0x70]
    int v2;  // [bp-0x6c]
    int v3;  // [bp-0x68]
    char v4;  // [bp-0x64]
    char v5;  // [bp-0x38]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]
    char v9;  // [bp-0x4]

    v8 = 4294967295;
    v7 = sub_10370868;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v6 = *((int *)v13);
    v1 = g_1038e180 ^ &v9;
    v14 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v14) = &v6;
    v0 = a0;
    sub_10334530();
    v3 = sub_10344a10(&v5, a0);
    v2 = v3;
    v8 = 0;
    sub_10344a70(&v4, v2);
    sub_103533ea(&v4, &g_1039fe84);
    v8 = 4294967295;
    v15 = sub_10343670(&v4, &g_1039fe84);
    v16 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v16) = v6;
    return v15;
}
```

## `sub_10342c90` `0x10342c90`

_272 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[40];
    int field_28;
} struct_0;

extern unsigned int g_1038e180;

unsigned int sub_10342c90(struct_0 *a0, int a1)
{
    unsigned long v11;  // ldt
    unsigned long v12;  // gdt
    unsigned short v13;  // fs
    unsigned long v14;  // 4178
    unsigned long v15;  // 4182
    unsigned int v16;  // eax
    unsigned int v17;  // eax
    int v18;  // eax
    unsigned long v20;  // 4113
    int v0;  // [bp-0x48]
    struct_0 *v1;  // [bp-0x44]
    unsigned int v2;  // [bp-0x40]
    unsigned int v3;  // [bp-0x34]
    int v4;  // [bp-0x30]
    int v5;  // [bp-0x2c]
    unsigned int v6;  // [bp-0x14]
    unsigned int v7;  // [bp-0x10]
    unsigned int v8;  // [bp-0xc]
    unsigned int v9;  // [bp-0x8]
    char v10;  // [bp-0x4]

    v9 = 4294967295;
    v8 = sub_10370898;
    v14 = _ccall(v11, v12, (unsigned int)v13, 0);
    v7 = *((int *)v14);
    v3 = g_1038e180 ^ &v10;
    v15 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int **)v15) = &v7;
    if (a0->field_28 >= *((int *)&a0[1].padding_0[0]))
    {
        v16 = sub_10341c30(a0) & 0xff;
        if (!((char)v16 & 4))
        {
            v20 = _ccall(v11, v12, (unsigned int)v13, 0);
            *((unsigned int *)v20) = v7;
            return v16 & 4;
        }
        v5 = sub_10342da0(a0->field_28, *((int *)&a0[1].padding_0[0]));
        v4 = v5;
        v9 = 0;
        sub_10344ad0(v4);
        v9 = 4294967295;
        sub_10342e50();
    }
    v6 = 0;
    while (true)
    {
        if (v6 >= sub_10340990(a0))
            break;
        v18 = sub_103409d0(a0, v6);
        if (*((int *)v18) == a0->field_28)
        {
            v2 = sub_10344b60(&a0[3].padding_0[28]);
            v1 = &a0[1].field_28;
            v0 = sub_103409d0(a0, v6) + 4;
            sub_10344b70(a1, sub_103409d0(a0, v6));
        }
        v6 += 1;
    }
    v20 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int *)v20) = v7;
    return v17;
}
```

## `sub_10342da0` `0x10342da0`

_107 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390b7c;

unsigned int [5] sub_10342da0(unsigned int *a0, unsigned int a1, unsigned int a2)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4135
    unsigned long v10;  // 4151
    unsigned long v11;  // 4152
    unsigned int v0;  // [bp-0x18]
    unsigned int idx[5];  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_103708c8;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    idx = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    idx = a0;
    sub_1033faa0(idx);
    idx[0] = &g_10390b7c;
    idx[3] = a1;
    idx[4] = a2;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return idx;
}
```

## `sub_10342e10` `0x10342e10`

_16 bytes. (leaf/helper — see body)_

```c
int sub_10342e10(unsigned int a0)
{
    return "boost::too_many_args: format-string referred to less arguments than were passed";
}
```

## `sub_10342e20` `0x10342e20`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10342e20(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10342e50(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_10342e50` `0x10342e50`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10342e50(int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4137
    unsigned long v11;  // 4153
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_103708f8;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    v4 = 0;
    v4 = 4294967295;
    v12 = sub_1033fb40(v1);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_10342ea0` `0x10342ea0`

_272 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10342ea0(void* a0, int a1)
{
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    unsigned short v14;  // fs
    unsigned long v15;  // 4178
    unsigned long v16;  // 4182
    unsigned int v17;  // eax
    unsigned int v18;  // eax
    int v19;  // eax
    unsigned long v21;  // 4113
    int v0;  // [bp-0x40]
    void* v1;  // [bp-0x3c]
    unsigned int v2;  // [bp-0x38]
    unsigned int v3;  // [bp-0x34]
    unsigned int v4;  // [bp-0x30]
    unsigned int v5;  // [bp-0x2c]
    unsigned int v6[5];  // [bp-0x28]
    unsigned int v7;  // [bp-0x14]
    unsigned int v8;  // [bp-0x10]
    unsigned int v9;  // [bp-0xc]
    unsigned int v10;  // [bp-0x8]
    char v11;  // [bp-0x4]

    v10 = 4294967295;
    v9 = sub_10370928;
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    v8 = *((int *)v15);
    v3 = g_1038e180 ^ &v11;
    v16 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v16) = &v8;
    if ((int)a0[40] >= (int)a0[44])
    {
        v17 = sub_10341c30(a0) & 0xff;
        if (!((char)v17 & 4))
        {
            v21 = _ccall(v12, v13, (unsigned int)v14, 0);
            *((unsigned int *)v21) = v8;
            return v17 & 4;
        }
        v5 = sub_10342da0(v6, (int)a0[40], (int)a0[44]);
        v4 = v5;
        v10 = 0;
        sub_10344ad0(v4);
        v10 = 4294967295;
        sub_10342e50(v6);
    }
    v7 = 0;
    while (true)
    {
        if (v7 >= sub_10340990(a0))
            break;
        v19 = sub_103409d0(a0, v7);
        if (*((int *)v19) == (int)a0[40])
        {
            v2 = sub_10344b60(a0 + 160);
            v1 = a0 + 84;
            v0 = sub_103409d0(a0, v7) + 4;
            sub_103456a0(a1, sub_103409d0(a0, v7));
        }
        v7 += 1;
    }
    v21 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int *)v21) = v8;
    return v18;
}
```

## `sub_10342fb0` `0x10342fb0`

_272 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10342fb0(void* a0, int a1)
{
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    unsigned short v14;  // fs
    unsigned long v15;  // 4178
    unsigned long v16;  // 4182
    unsigned int v17;  // eax
    unsigned int v18;  // eax
    int v19;  // eax
    unsigned long v21;  // 4113
    int v0;  // [bp-0x40]
    void* v1;  // [bp-0x3c]
    unsigned int v2;  // [bp-0x38]
    unsigned int v3;  // [bp-0x34]
    unsigned int v4;  // [bp-0x30]
    unsigned int v5;  // [bp-0x2c]
    unsigned int v6[5];  // [bp-0x28]
    unsigned int v7;  // [bp-0x14]
    unsigned int v8;  // [bp-0x10]
    unsigned int v9;  // [bp-0xc]
    unsigned int v10;  // [bp-0x8]
    char v11;  // [bp-0x4]

    v10 = 4294967295;
    v9 = sub_10370958;
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    v8 = *((int *)v15);
    v3 = g_1038e180 ^ &v11;
    v16 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v16) = &v8;
    if ((int)a0[40] >= (int)a0[44])
    {
        v17 = sub_10341c30(a0) & 0xff;
        if (!((char)v17 & 4))
        {
            v21 = _ccall(v12, v13, (unsigned int)v14, 0);
            *((unsigned int *)v21) = v8;
            return v17 & 4;
        }
        v5 = sub_10342da0(v6, (int)a0[40], (int)a0[44]);
        v4 = v5;
        v10 = 0;
        sub_10344ad0(v4);
        v10 = 4294967295;
        sub_10342e50(v6);
    }
    v7 = 0;
    while (true)
    {
        if (v7 >= sub_10340990(a0))
            break;
        v19 = sub_103409d0(a0, v7);
        if (*((int *)v19) == (int)a0[40])
        {
            v2 = sub_10344b60(a0 + 160);
            v1 = a0 + 84;
            v0 = sub_103409d0(a0, v7) + 4;
            sub_10345d00(a1, sub_103409d0(a0, v7));
        }
        v7 += 1;
    }
    v21 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int *)v21) = v8;
    return v18;
}
```

## `sub_103430c0` `0x103430c0`

_71 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    char field_8;
    char padding_9[3];
    unsigned int field_c;
    unsigned int field_10;
    unsigned int field_14;
} struct_0;

char sub_103430c0(struct_0 *idx, char a1)
{
    idx->field_0 = 0;
    idx->field_4 = 6;
    idx->field_8 = a1;
    idx->field_c = 513;
    idx->field_14 = 0;
    idx->field_10 = 0;
    return *((char *)&idx);
}
```

## `sub_10343110` `0x10343110`

_15 bytes. (leaf/helper — see body)_

```c
void sub_10343110(unsigned int a0)
{
    char v0;  // [bp+0x0]

    sub_10343460(0, &v0);
    return;
}
```

## `sub_10343120` `0x10343120`

_101 bytes. (leaf/helper — see body)_

```c
int sub_10343120(char a0, char a0, int a1)
{
    int v9;  // edx
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x6]
    char v5;  // [bp-0x5]

    v5 = 0;
    v3 = &/* unsupported instruction */;
    v2 = &/* unsupported instruction */;
    v4 = sub_10337970();
    v3 = _INSERT(v4 CONCAT 0, 0, v5);
    *((char *)&v2) = v4;
    v1 = &/* unsupported instruction */;
    v0 = &/* unsupported instruction */;
    v9 = _INSERT(0, 0, *((char *)sub_103378b0((char *)&/* unsupported instruction */ + 1)));
    return sub_10346360(sub_10349d70(&/* unsupported instruction */, sub_10349d70(&/* unsupported instruction */, a1, v9)));
}
```

## `sub_10343190` `0x10343190`

_37 bytes. (leaf/helper — see body)_

```c
int sub_10343190(int a0, int a1, int a2, int a3)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_103463c0(a1, a2, a3, a0, a0, &v1);
}
```

## `sub_103431c0` `0x103431c0`

_43 bytes. (leaf/helper — see body)_

```c
int sub_103431c0(char a0, char a0, int a1)
{
    char v0;  // [bp+0x0]

    return sub_10346410(sub_10349d70(&/* unsupported instruction */, sub_10349d70(&/* unsupported instruction */, a1, &v0)));
}
```

## `sub_103431f0` `0x103431f0`

_97 bytes. (leaf/helper — see body)_

```c
int sub_103431f0(char a0, char a0, int a1)
{
    int v9;  // ecx
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x6]
    char v5;  // [bp-0x5]

    v5 = 0;
    v3 = &/* unsupported instruction */;
    v4 = sub_10337970();
    *((char *)&v3) = v5;
    v2 = _INSERT(v4 CONCAT 0, 0, v4);
    v1 = &/* unsupported instruction */;
    v0 = &/* unsupported instruction */;
    v9 = _INSERT(0, 0, *((char *)sub_103378b0((char *)&/* unsupported instruction */ + 1)));
    return sub_10346440(sub_10349d70(&/* unsupported instruction */, sub_10349d70(&/* unsupported instruction */, a1, v9)));
}
```

## `sub_10343260` `0x10343260`

_64 bytes. (leaf/helper — see body)_

```c
char sub_10343260(int a0, int a1, int a2, int a3)
{
    unsigned int v5;  // ecx
    int v6;  // eax
    int v7;  // ecx
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x6]
    char v4;  // [bp-0x5]

    v2 = v5;
    v4 = 0;
    v1 = &/* unsupported instruction */;
    v0 = &/* unsupported instruction */;
    v3 = sub_10337970();
    v6 = _INSERT(v3 CONCAT 0, 0, v4);
    v7 = _INSERT(0, 0, v3);
    return sub_10346480(a0, a1, a2, a3, v7, v6);
}
```

## `sub_103432a0` `0x103432a0`

_158 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390bdc;
extern char g_10390bec;
extern char g_10390bf4;

unsigned int sub_103432a0(unsigned int idx, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4139
    unsigned long v10;  // 4153
    unsigned long v11;  // 4142
    int v0;  // [bp-0x24]
    int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_10370993;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_10343340(a1, g_1038e180 ^ &v5);
    v4 = 0;
    v1 = (!a1 ? 0 : a1 + 40);
    v0 = v1;
    sub_10313b60(idx + 40);
    *((char **)idx) = &g_10390bf4;
    *((char **)(idx + 20)) = &g_10390bec;
    *((char **)(idx + 40)) = &g_10390bdc;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return idx;
}
```

## `sub_10343340` `0x10343340`

_148 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390c00;
extern char g_10390c08;

unsigned int * sub_10343340(unsigned int *a0, unsigned int a1)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4139
    unsigned long v9;  // 4153
    unsigned long v10;  // 4135
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]
    char v4;  // [bp-0x4]

    v3 = 4294967295;
    v2 = sub_103709c3;
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v1 = *((int *)v8);
    v9 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v9) = &v1;
    sub_103433e0(a1, g_1038e180 ^ &v4);
    v3 = 0;
    v0 = (!a1 ? 0 : a1 + 20);
    sub_10313a80(a0 + 5, v0);
    *(a0) = &g_10390c08;
    a0[5] = &g_10390c00;
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v10) = v1;
    return a0;
}
```

