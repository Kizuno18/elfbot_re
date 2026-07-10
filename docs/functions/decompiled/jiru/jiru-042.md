# elfbot.dll decompiled — jiru 0x10332920..0x10334320

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10332920` `0x10332920`

_28 bytes. (leaf/helper — see body)_

```c
int sub_10332920(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10332b70(a1, a0, &v1);
    return a0;
}
```

## `sub_10332940` `0x10332940`

_33 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

extern unsigned int g_1039011c;

struct_0 * sub_10332940(struct_0 *a0, struct_0 *a1)
{
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_1031e7a0(v0, a1, 0, g_1039011c);
}
```

## `sub_10332970` `0x10332970`

_136 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    struct struct_0 *field_4;
} struct_0;

char sub_10332970(struct_0 *a0, unsigned int a1)
{
    struct_0 *v8;  // ecx
    struct_0 *v9;  // edx
    unsigned int v0;  // [bp-0x34]
    unsigned int v1;  // [bp-0x30]
    struct_0 *v2;  // [bp-0x28]
    unsigned int v3;  // [bp-0x24]
    struct_0 *v4;  // [bp-0x1c]
    unsigned int v5[2];  // [bp-0x14]
    unsigned int v6[2];  // [bp-0xc]

    v8 = a0;
    v4 = v8;
    v3 = sub_1032ff80(sub_10330c90(a0, a1, v6));
    if (v4->field_0 != v3 || (v8 = v4, v4 = (struct_0 *)v8->field_4, v8->field_4 != v9))
    {
        v2 = a0;
        v1 = sub_1032ff80(sub_10330c60(v8, v4, v5));
        if (v2->field_0 == v1 && v2->field_4 == v9)
            goto LABEL_103329ea;
        v0 = 0;
    }
    else
    {
LABEL_103329ea:
        v0 = 1;
    }
    return v0;
}
```

## `sub_10332a00` `0x10332a00`

_84 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

char sub_10332a00(struct_0 *a0)
{
    unsigned int v4;  // edx
    unsigned int v0;  // [bp-0x20]
    int v1;  // [bp-0x1c]
    unsigned int v2[2];  // [bp-0xc]

    v1 = sub_1032ff80(sub_10330cc0(v2));
    if (a0->padding_0 == v1 && a0->field_4 == v4)
        v0 = 1;
    else
        v0 = 0;
    return v0;
}
```

## `sub_10332a60` `0x10332a60`

_77 bytes. (leaf/helper — see body)_

```c
char sub_10332a60(unsigned int a0)
{
    unsigned int v0;  // [bp-0x10]
    char v1;  // [bp-0xc]
    char v2;  // [bp-0x8]

    sub_1032fd30(&v2);
    if (a0 != sub_10336b20() && !((sub_1032fd00(&v1), a0 == sub_10336b20())))
        v0 = 0;
    else
        v0 = 1;
    return v0;
}
```

## `sub_10332ab0` `0x10332ab0`

_87 bytes. (leaf/helper — see body)_

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

struct_0 * sub_10332ab0(struct_0 *idx, unsigned int a1)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = idx;
    if (!idx->field_0)
        sub_10353616(idx, &v1);
    if (idx->field_4 + a1 > idx->field_0->field_8 || idx->field_4 + a1 < idx->field_0->field_4)
        sub_10353616();
    idx->field_4 = idx->field_4 + a1;
    return idx;
}
```

## `sub_10332b10` `0x10332b10`

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

struct_0 * sub_10332b10(struct_0 *idx, unsigned int a1)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = idx;
    if (!idx->field_0)
        sub_10353616(idx, &v1);
    if (idx->field_4 + a1 * 2 > idx->field_0->field_8 || idx->field_4 + a1 * 2 < idx->field_0->field_4)
        sub_10353616();
    idx->field_4 = idx->field_4 + a1 * 2;
    return idx;
}
```

## `sub_10332b70` `0x10332b70`

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

struct_0 * sub_10332b70(struct_0 *idx, unsigned int a1)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = idx;
    if (!idx->field_0)
        sub_10353616(idx, &v1);
    if (a1 * 28 + idx->field_4 > idx->field_0->field_8 || a1 * 28 + idx->field_4 < idx->field_0->field_4)
        sub_10353616();
    idx->field_4 = a1 * 28 + idx->field_4;
    return idx;
}
```

## `sub_10332bd0` `0x10332bd0`

_22 bytes. (leaf/helper — see body)_

```c
int sub_10332bd0(unsigned int a0)
{
    unsigned int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_1031a280(v0 + 4);
}
```

## `sub_10332bf0` `0x10332bf0`

_151 bytes. (leaf/helper — see body)_

```c
int sub_10332bf0(int a0, char *iter)
{
    int v2;  // edx
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    if (*(iter) == 47 && iter[1] == 47 && iter[2] == 58)
        iter += 3;
    if (!(char)sub_10332c90(a0, &v1) && *(iter))
    {
        v2 = _INSERT(iter, 0, *(iter));
        if (!(char)sub_10336bd0(v2))
            sub_10336b30();
    }
    for (; *(iter); iter += 1)
    {
        sub_10336ba0(_INSERT(iter, 0, *(iter)));
    }
    return a0;
}
```

## `sub_10332c90` `0x10332c90`

_19 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

int sub_10332c90(struct_0 *a0)
{
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_10325be0(v0);
}
```

## `sub_10332cb0` `0x10332cb0`

_46 bytes. (leaf/helper — see body)_

```c
int sub_10332cb0(unsigned int a0)
{
    unsigned int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_103148c0(v0, sub_10336c00(v0, sub_1031e920(v0)), 4294967295);
    return v0;
}
```

## `sub_10332ce0` `0x10332ce0`

_494 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

extern unsigned int g_1038e180;

int sub_10332ce0(unsigned int a0, int a1)
{
    unsigned long v11;  // ldt
    unsigned long v12;  // gdt
    unsigned short v13;  // fs
    unsigned long v14;  // 4138
    unsigned long v15;  // 4155
    int v16;  // edx
    char *v17;  // eax
    unsigned long v18;  // 4118
    unsigned int v0;  // [bp-0x48]
    unsigned int v1;  // [bp-0x40]
    unsigned int iter;  // [bp-0x3c]
    unsigned int v3;  // [bp-0x38]
    struct_0 v4;  // [bp-0x34]
    unsigned int v5;  // [bp-0x18]
    char v6;  // [bp-0x11]
    unsigned int v7;  // [bp-0x10]
    unsigned int v8;  // [bp-0xc]
    char v9;  // [bp-0x8], Other Possible Types: unsigned int
    char v10;  // [bp-0x4]

    v9 = 4294967295;
    v8 = sub_1036dd81;
    v14 = _ccall(v11, v12, (unsigned int)v13, 0);
    v7 = *((int *)v14);
    v5 = g_1038e180 ^ &v10;
    v0 = v5;
    v15 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int **)v15) = &v7;
    v1 = 0;
    v3 = sub_10336ce0(a0, sub_1031e920(a0));
    v6 = v3 != 4294967295;
    sub_10315800(&v4);
    v9 = 1;
    for (iter = 0; iter != sub_1031e920(a0); iter += 1)
    {
        if (!iter && sub_1031e920(a0) > 1 && *((char *)sub_103189a0(a0, 0)) == 47 && *((char *)sub_103189a0(a0, 1)) == 47 && (sub_1031e920(a0) == 2 || (v16 = (int)_INSERT(0, 0, *((char *)sub_103189a0(a0, 2))), !(char)sub_10336bd0(_INSERT(0, 0, *((char *)sub_103189a0(a0, 2)))))))
        {
            iter += 1;
            sub_103170d0(&v4, 92);
            sub_103170d0(&v4, 92);
        }
        else if (!v6 || !sub_1031e920(&v4) || *((char *)sub_103189a0(&v4, sub_1031e920(&v4) - 1)) != 92 || *((char *)sub_103189a0(a0, iter)) != 47)
        {
            if (*((char *)sub_103189a0(a0, iter)) == 47)
            {
                sub_103170d0(&v4, 92);
            }
            else
            {
                v17 = sub_103189a0(a0, iter);
                sub_103170d0(&v4, *(v17));
            }
            if (iter > v3 && *((char *)sub_103189a0(a0, iter)) == 47)
                v6 = 0;
        }
    }
    sub_103145d0(a1, &v4);
    v1 |= 1;
    v9 = 0;
    sub_10314610(&v4);
    v18 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int *)v18) = v7;
    return sub_10351225();
}
```

## `sub_10332ed0` `0x10332ed0`

_496 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

extern unsigned int g_1038e180;

int sub_10332ed0(unsigned int a0, unsigned int a1)
{
    unsigned long v11;  // ldt
    unsigned long v12;  // gdt
    unsigned short v13;  // fs
    unsigned long v14;  // 4138
    unsigned long v15;  // 4155
    unsigned short v16;  // dx
    unsigned short *v17;  // eax
    unsigned long v18;  // 4118
    unsigned int v0;  // [bp-0x48]
    unsigned int v1;  // [bp-0x40]
    unsigned int iter;  // [bp-0x3c]
    unsigned int v3;  // [bp-0x38]
    struct_0 v4;  // [bp-0x34]
    unsigned int v5;  // [bp-0x18]
    char v6;  // [bp-0x11]
    unsigned int v7;  // [bp-0x10]
    unsigned int v8;  // [bp-0xc]
    char v9;  // [bp-0x8], Other Possible Types: unsigned int
    char v10;  // [bp-0x4]

    v9 = 4294967295;
    v8 = sub_1036ddd1;
    v14 = _ccall(v11, v12, (unsigned int)v13, 0);
    v7 = *((int *)v14);
    v5 = g_1038e180 ^ &v10;
    v0 = v5;
    v15 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int **)v15) = &v7;
    v1 = 0;
    v3 = sub_10337030(a0, sub_1031e920(a0));
    v6 = v3 != 4294967295;
    sub_103257a0(&v4);
    v9 = 1;
    for (iter = 0; iter != sub_1031e920(a0); iter += 1)
    {
        if (!iter && sub_1031e920(a0) > 1 && *((short *)sub_10325ed0(a0, 0)) == 47 && *((short *)sub_10325ed0(a0, 1)) == 47 && (sub_1031e920(a0) == 2 || (v16 = (unsigned short)*((short *)sub_10325ed0(a0, 2)), !sub_103260f0(*((short *)sub_10325ed0(a0, 2))))))
        {
            iter += 1;
            sub_10325f70(&v4, 92);
            sub_10325f70(&v4, 92);
        }
        else if (!v6 || !sub_1031e920(&v4) || *((short *)sub_10325ed0(&v4, sub_1031e920(&v4) - 1)) != 92 || *((short *)sub_10325ed0(a0, iter)) != 47)
        {
            if (*((short *)sub_10325ed0(a0, iter)) == 47)
            {
                sub_10325f70(&v4, 92);
            }
            else
            {
                v17 = sub_10325ed0(a0, iter);
                sub_10325f70(&v4, *(v17));
            }
            if (iter > v3 && *((short *)sub_10325ed0(a0, iter)) == 47)
                v6 = 0;
        }
    }
    sub_1031e760(a1, &v4);
    v1 |= 1;
    v9 = 0;
    sub_1031a3a0(&v4);
    v18 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int *)v18) = v7;
    return sub_10351225();
}
```

## `sub_103330c0` `0x103330c0`

_285 bytes. refs "boost::filesystem::exists"_

```c
extern unsigned int g_1038e180;

void sub_103330c0(int a0)
{
    unsigned long v13;  // ldt
    unsigned long v14;  // gdt
    unsigned short v15;  // fs
    unsigned long v16;  // 4135
    unsigned long v17;  // 4149
    unsigned long v18;  // 4116
    int v0;  // [bp-0xb8]
    int v1;  // [bp-0xb4]
    int v2;  // [bp-0xb0]
    int v3;  // [bp-0xac]
    char v4;  // [bp-0xa8]
    char v5;  // [bp-0x38]
    char v6;  // [bp-0x1c], Other Possible Types: int
    char v7;  // [bp-0x18], Other Possible Types: int
    int v8;  // [bp-0x14]
    unsigned int v9;  // [bp-0x10]
    unsigned int v10;  // [bp-0xc]
    char v11;  // [bp-0x8], Other Possible Types: unsigned int
    char v12;  // [bp-0x4]

    v11 = 4294967295;
    v10 = sub_1036de1e;
    v16 = _ccall(v13, v14, (unsigned int)v15, 0);
    v9 = *((int *)v16);
    v17 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int **)v17) = &v9;
    sub_103331e0(g_1038e180 ^ &v12);
    v3 = sub_10335870(&v5, &v7);
    v2 = v3;
    v11 = 0;
    sub_10368630(&v6, v2);
    v11 = 4294967295;
    sub_10314610(&v5);
    if (sub_10333210())
    {
        sub_10314590(&v4, "boost::filesystem::exists");
        v11 = 1;
        v1 = sub_10336de0(&v4, a0, v7, v8);
        v0 = v1;
        v11 = 2;
        sub_10336f80(v0);
        v11 = 1;
        sub_10335b60();
        v11 = 4294967295;
        sub_10314610(&v4);
    }
    sub_10333230(v6);
    v18 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int *)v18) = v9;
    return;
}
```

## `sub_103331e0` `0x103331e0`

_34 bytes. (leaf/helper — see body)_

```c
unsigned int [2] sub_103331e0(unsigned int *a0)
{
    unsigned int v0[2];  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    *(a0) = 0;
    a0[1] = sub_10368c80(a0, &v1);
    return a0;
}
```

## `sub_10333210` `0x10333210`

_25 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10333210(unsigned int a0)
{
    return -(0 < *((int *)a0)) & sub_10334530;
}
```

## `sub_10333230` `0x10333230`

_52 bytes. (leaf/helper — see body)_

```c
char sub_10333230(void)
{
    int v3;  // ecx
    unsigned int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    if (sub_10336b20(v3, &v1) && sub_10336b20() != 1)
        v0 = 1;
    else
        v0 = 0;
    return v0;
}
```

## `sub_10333270` `0x10333270`

_285 bytes. refs "boost::filesystem::exists"_

```c
extern unsigned int g_1038e180;

char sub_10333270(int a0)
{
    unsigned long v15;  // ldt
    unsigned long v16;  // gdt
    unsigned short v17;  // fs
    unsigned long v18;  // 4135
    unsigned long v19;  // 4149
    char v20;  // al
    unsigned long v21;  // 4116
    unsigned int v0;  // [bp-0xd4]
    unsigned int v1;  // [bp-0xbc]
    int v2;  // [bp-0xb8]
    int v3;  // [bp-0xb4]
    int v4;  // [bp-0xb0]
    int v5;  // [bp-0xac]
    char v6;  // [bp-0xa8]
    char v7;  // [bp-0x38]
    char v8;  // [bp-0x1c], Other Possible Types: unsigned int
    int v9;  // [bp-0x18], Other Possible Types: unsigned int
    int v10;  // [bp-0x14]
    unsigned int v11;  // [bp-0x10]
    unsigned int v12;  // [bp-0xc]
    char v13;  // [bp-0x8], Other Possible Types: unsigned int
    char v14;  // [bp-0x4]

    v13 = 4294967295;
    v12 = sub_1036de5e;
    v18 = _ccall(v15, v16, (unsigned int)v17, 0);
    v11 = *((int *)v18);
    v1 = g_1038e180 ^ &v14;
    v19 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int **)v19) = &v11;
    sub_103331e0(&v9);
    v5 = sub_10335960(&v7, &v9);
    v4 = v5;
    v13 = 0;
    sub_10368650(&v8, v4);
    v13 = 4294967295;
    sub_1031a3a0(&v7);
    if (sub_10333210(&v9))
    {
        sub_10314590(&v6, "boost::filesystem::exists");
        v13 = 1;
        v3 = sub_10337130(&v6, a0, v9, v10);
        v2 = v3;
        v13 = 2;
        sub_10337250(v2);
        v13 = 1;
        sub_10335fe0();
        v13 = 4294967295;
        sub_10314610(&v6);
    }
    v0 = v8;
    v20 = sub_10333230();
    v21 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int *)v21) = v11;
    return v20;
}
```

## `sub_10333390` `0x10333390`

_267 bytes. refs "boost::filesystem::file_size"_

```c
extern unsigned int g_1038e180;

int sub_10333390(int a0)
{
    unsigned long v13;  // ldt
    unsigned long v14;  // gdt
    unsigned short v15;  // fs
    unsigned long v16;  // 4138
    unsigned long v17;  // 4152
    unsigned long v18;  // 4121
    int v0;  // [bp-0xbc]
    int v1;  // [bp-0xb8]
    int v2;  // [bp-0xb4]
    int v3;  // [bp-0xb0]
    char v4;  // [bp-0xac]
    char v5;  // [bp-0x3c]
    char v6;  // [bp-0x20], Other Possible Types: int
    int v7;  // [bp-0x1c]
    unsigned int v8;  // [bp-0x18]
    unsigned int v9;  // [bp-0x10]
    unsigned int v10;  // [bp-0xc]
    char v11;  // [bp-0x8], Other Possible Types: unsigned int
    char v12;  // [bp-0x4]

    v11 = 4294967295;
    v10 = sub_1036de9e;
    v16 = _ccall(v13, v14, (unsigned int)v15, 0);
    v9 = *((int *)v16);
    v17 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int **)v17) = &v9;
    v3 = sub_10335870(&v5, g_1038e180 ^ &v12);
    v2 = v3;
    v11 = 0;
    sub_103687f0(&v6, v2);
    v11 = 4294967295;
    sub_10314610(&v5);
    if (sub_10333210(&v6))
    {
        sub_10314590(&v4, "boost::filesystem::file_size");
        v11 = 1;
        v1 = sub_10336de0(&v4, a0, v6, v7);
        v0 = v1;
        v11 = 2;
        sub_10336f80(v0);
        v11 = 1;
        sub_10335b60();
        v11 = 4294967295;
        sub_10314610(&v4);
    }
    v18 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int *)v18) = v9;
    return v8;
}
```

## `sub_103334a0` `0x103334a0`

_267 bytes. refs "boost::filesystem::file_size"_

```c
extern unsigned int g_1038e180;

int sub_103334a0(int a0)
{
    unsigned long v13;  // ldt
    unsigned long v14;  // gdt
    unsigned short v15;  // fs
    unsigned long v16;  // 4138
    unsigned long v17;  // 4152
    unsigned long v18;  // 4121
    int v0;  // [bp-0xbc]
    int v1;  // [bp-0xb8]
    int v2;  // [bp-0xb4]
    int v3;  // [bp-0xb0]
    char v4;  // [bp-0xac]
    char v5;  // [bp-0x3c]
    char v6;  // [bp-0x20], Other Possible Types: int
    int v7;  // [bp-0x1c]
    unsigned int v8;  // [bp-0x18]
    unsigned int v9;  // [bp-0x10]
    unsigned int v10;  // [bp-0xc]
    char v11;  // [bp-0x8], Other Possible Types: unsigned int
    char v12;  // [bp-0x4]

    v11 = 4294967295;
    v10 = sub_1036dede;
    v16 = _ccall(v13, v14, (unsigned int)v15, 0);
    v9 = *((int *)v16);
    v17 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int **)v17) = &v9;
    v3 = sub_10335960(&v5, g_1038e180 ^ &v12);
    v2 = v3;
    v11 = 0;
    sub_103687d0(&v6, v2);
    v11 = 4294967295;
    sub_1031a3a0(&v5);
    if (sub_10333210(&v6))
    {
        sub_10314590(&v4, "boost::filesystem::file_size");
        v11 = 1;
        v1 = sub_10337130(&v4, a0, v6, v7);
        v0 = v1;
        v11 = 2;
        sub_10337250(v0);
        v11 = 1;
        sub_10335fe0();
        v11 = 4294967295;
        sub_10314610(&v4);
    }
    v18 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int *)v18) = v9;
    return v8;
}
```

## `sub_103335b0` `0x103335b0`

_449 bytes. refs "boost::filesystem::system_complete"_

```c
extern unsigned int g_1038e180;

int sub_103335b0(unsigned int a0, unsigned int a1)
{
    unsigned long v19;  // ldt
    unsigned long v20;  // gdt
    unsigned short v21;  // fs
    unsigned long v22;  // 4137
    unsigned long v23;  // 4154
    unsigned long v24;  // 4114
    unsigned int v0;  // [bp-0x100]
    int v1;  // [bp-0xfc]
    int v2;  // [bp-0xf8]
    int v3;  // [bp-0xf4]
    int v4;  // [bp-0xf0]
    int v5;  // [bp-0xec]
    int v6;  // [bp-0xe8]
    unsigned int v7;  // [bp-0xe4]
    char v8;  // [bp-0xe0]
    char v9;  // [bp-0xc4]
    char v10;  // [bp-0x54]
    char v11;  // [bp-0x38]
    unsigned int v12;  // [bp-0x1c]
    char v13;  // [bp-0x18], Other Possible Types: int
    int v14;  // [bp-0x14]
    unsigned int v15;  // [bp-0x10]
    unsigned int v16;  // [bp-0xc]
    unsigned int v17;  // [bp-0x8], Other Possible Types: char
    char v18;  // [bp-0x4]

    v17 = 4294967295;
    v16 = sub_1036df50;
    v22 = _ccall(v19, v20, (unsigned int)v21, 0);
    v15 = *((int *)v22);
    v12 = g_1038e180 ^ &v18;
    v0 = v12;
    v23 = _ccall(v19, v20, (unsigned int)v21, 0);
    *((unsigned int **)v23) = &v15;
    v7 = 0;
    if ((char)sub_10332c90(a1))
    {
        sub_10334ef0(a1);
        v17 = 0;
        v7 |= 1;
    }
    else
    {
        sub_10315800(&v11);
        v17 = 1;
        v6 = sub_10335870(&v10, &v11);
        v5 = v6;
        v17 = 2;
        sub_10368ba0(&v13, v5);
        v17 = 1;
        sub_10314610(&v10);
        if (sub_10333210(&v13))
        {
            sub_10314590(&v9, "boost::filesystem::system_complete");
            v17 = 3;
            v4 = sub_10336de0(&v9, a1, v13, v14);
            v3 = v4;
            v17 = 4;
            sub_10336f80(v3);
            v17 = 3;
            sub_10335b60();
            v17 = 1;
            sub_10314610(&v9);
        }
        v2 = sub_10333780(&v8, &v11);
        v1 = v2;
        v17 = 5;
        sub_1032db80(a0, v1);
        v7 |= 1;
        v17 = 1;
        sub_10314610(&v8);
        v17 = 0;
        sub_10314610(&v11);
    }
    v24 = _ccall(v19, v20, (unsigned int)v21, 0);
    *((unsigned int *)v24) = v15;
    return sub_10351225();
}
```

## `sub_10333780` `0x10333780`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10333780(int a0, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned int v10;  // ecx
    unsigned long v11;  // 4154
    unsigned long v12;  // 4131
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036df99;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = v10;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v2;
    v1 = 0;
    sub_103145d0(a0, a1);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v2;
    return a0;
}
```

## `sub_103337e0` `0x103337e0`

_449 bytes. refs "boost::filesystem::system_complete"_

```c
extern unsigned int g_1038e180;

int sub_103337e0(unsigned int a0, unsigned int a1)
{
    unsigned long v19;  // ldt
    unsigned long v20;  // gdt
    unsigned short v21;  // fs
    unsigned long v22;  // 4137
    unsigned long v23;  // 4154
    unsigned long v24;  // 4114
    unsigned int v0;  // [bp-0x100]
    int v1;  // [bp-0xfc]
    int v2;  // [bp-0xf8]
    int v3;  // [bp-0xf4]
    int v4;  // [bp-0xf0]
    int v5;  // [bp-0xec]
    int v6;  // [bp-0xe8]
    unsigned int v7;  // [bp-0xe4]
    char v8;  // [bp-0xe0]
    char v9;  // [bp-0xc4]
    char v10;  // [bp-0x54]
    char v11;  // [bp-0x38]
    unsigned int v12;  // [bp-0x1c]
    char v13;  // [bp-0x18], Other Possible Types: int
    int v14;  // [bp-0x14]
    unsigned int v15;  // [bp-0x10]
    unsigned int v16;  // [bp-0xc]
    unsigned int v17;  // [bp-0x8], Other Possible Types: char
    char v18;  // [bp-0x4]

    v17 = 4294967295;
    v16 = sub_1036e010;
    v22 = _ccall(v19, v20, (unsigned int)v21, 0);
    v15 = *((int *)v22);
    v12 = g_1038e180 ^ &v18;
    v0 = v12;
    v23 = _ccall(v19, v20, (unsigned int)v21, 0);
    *((unsigned int **)v23) = &v15;
    v7 = 0;
    if ((char)sub_10332c90(a1))
    {
        sub_10332540(a0, a1);
        v17 = 0;
        v7 |= 1;
    }
    else
    {
        sub_103257a0(&v11);
        v17 = 1;
        v6 = sub_10335960(&v10, &v11);
        v5 = v6;
        v17 = 2;
        sub_10368b80(&v13, v5);
        v17 = 1;
        sub_1031a3a0(&v10);
        if (sub_10333210(&v13))
        {
            sub_10314590(&v9, "boost::filesystem::system_complete");
            v17 = 3;
            v4 = sub_10337130(&v9, a1, v13, v14);
            v3 = v4;
            v17 = 4;
            sub_10337250(v3);
            v17 = 3;
            sub_10335fe0();
            v17 = 1;
            sub_10314610(&v9);
        }
        v2 = sub_103339b0(&v8, &v11);
        v1 = v2;
        v17 = 5;
        sub_10325740(a0, v1);
        v7 |= 1;
        v17 = 1;
        sub_1031a3a0(&v8);
        v17 = 0;
        sub_1031a3a0(&v11);
    }
    v24 = _ccall(v19, v20, (unsigned int)v21, 0);
    *((unsigned int *)v24) = v15;
    return sub_10351225();
}
```

## `sub_103339b0` `0x103339b0`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_103339b0(unsigned int a0, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned int v10;  // ecx
    unsigned long v11;  // 4154
    unsigned long v12;  // 4131
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036e059;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = v10;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v2;
    v1 = 0;
    sub_1031e760(a0, a1);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v2;
    return a0;
}
```

## `sub_10333a10` `0x10333a10`

_162 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern int g_1039d384;

unsigned int sub_10333a10(int a0)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4137
    unsigned long v12;  // 4151
    unsigned int v13;  // eax
    unsigned long v14;  // 4113
    int v0;  // [bp-0x94]
    int v1;  // [bp-0x90]
    char v2;  // [bp-0x8c]
    char v3;  // [bp-0x4c]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036e088;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    sub_10334530(a0, g_1038e180 ^ &v7);
    v1 = sub_10337300(&v3, a0);
    v0 = v1;
    v6 = 0;
    sub_10337360(&v2, v0);
    sub_103533ea(&v2, &g_1039d384);
    v6 = 4294967295;
    v13 = sub_103360b0(&v2, &g_1039d384);
    v14 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v14) = v4;
    return v13;
}
```

## `sub_10333ac0` `0x10333ac0`

_48 bytes. (leaf/helper — see body)_

```c
short sub_10333ac0(unsigned short *idx, unsigned short a1, unsigned short a2, unsigned short a3)
{
    *(idx) = a1;
    idx[1] = a2;
    idx[2] = a3;
    return *((unsigned short *)&idx);
}
```

## `sub_10333af0` `0x10333af0`

_206 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10333af0(unsigned int a0)
{
    int v0;  // [bp-0x18]
    unsigned short v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned short v3;  // [bp-0xc]
    unsigned short v4;  // [bp-0x8]

    v3 = (14 - (sub_10333bc0(v0) & 0xffff)) / 12;
    v4 = (unsigned short)sub_10333bc0(v0) + 4800 - v3;
    v1 = (sub_10333bc0() & 0xffff) + v3 * 12 - 3;
    v2 = (sub_10333bc0() & 0xffff) + (int)((v1 * 0x99 + 2) / 5) + v4 * 365 + (v4 + (v4 >> 31 & 3) >> 2) - (int)(v4 / 100) + (int)(v4 / 400) - 32045;
    return v2;
}
```

## `sub_10333bc0` `0x10333bc0`

_17 bytes. (leaf/helper — see body)_

```c
int sub_10333bc0(unsigned short *a0)
{
    return _INSERT(a0, 0, *(a0));
}
```

## `sub_10333be0` `0x10333be0`

_96 bytes. (leaf/helper — see body)_

```c
unsigned short sub_10333be0(unsigned short a0)
{
    unsigned int v2;  // ecx
    unsigned int v3;  // ecx
    int v4;  // ecx
    unsigned short v5;  // ax
    unsigned int v0;  // [bp-0x8]
    unsigned short v1;  // [bp+0x8]

    v0 = v2;
    v0 = sub_10333bc0(&v1) & 0xffff;
    v3 = v0 - 2;
    switch (v3)
    {
    case 0:
        v4 = _INSERT(v3, 0, a0);
        v5 = (!(char)sub_10333c60(v4) ? 28 : 29);
        return v5;
    case 2: case 4: case 7: case 9:
        return 30;
    default:
        return 31;
    }
}
```

## `sub_10333c2c` `0x10333c2c`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10333c2c(void)
{
}
```

## `sub_10333c60` `0x10333c60`

_100 bytes. (leaf/helper — see body)_

```c
char sub_10333c60(void)
{
    unsigned int v2;  // ecx
    unsigned int v3;  // eax
    unsigned int v4;  // eax
    unsigned int v0;  // [bp-0x8]
    unsigned short v1;  // [bp+0x4]

    v0 = v2;
    v3 = sub_10333bc0(&v1) & 0xffff;
    v4 = v3 & 3;
    if ((v3 & 3) < 0)
        v4 = (v4 - 1 | 0xfffffffc) + 1;
    if (!v4 && ((int)((sub_10333bc0(&v1) & 0xffff) % 100) || !(int)((sub_10333bc0(&v1) & 0xffff) % 400)))
        v0 = 1;
    else
        v0 = 0;
    return v0;
}
```

## `sub_10333cd0` `0x10333cd0`

_162 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern int g_1039d44c;

unsigned int sub_10333cd0(int a0)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4137
    unsigned long v12;  // 4151
    unsigned int v13;  // eax
    unsigned long v14;  // 4113
    int v0;  // [bp-0x94]
    int v1;  // [bp-0x90]
    char v2;  // [bp-0x8c]
    char v3;  // [bp-0x4c]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036e0b8;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    sub_10334530(a0, g_1038e180 ^ &v7);
    v1 = sub_103373c0(&v3, a0);
    v0 = v1;
    v6 = 0;
    sub_10337420(&v2, v0);
    sub_103533ea(&v2, &g_1039d44c);
    v6 = 4294967295;
    v13 = sub_103362a0(&v2, &g_1039d44c);
    v14 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v14) = v4;
    return v13;
}
```

## `sub_10333d80` `0x10333d80`

_93 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390658;

int sub_10333d80(int a0, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4154
    unsigned long v11;  // 4128
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036e0e8;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_1032d580(v1, a1);
    *((char **)v1) = &g_10390658;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_10333de0` `0x10333de0`

_33 bytes. (leaf/helper — see body)_

```c
int sub_10333de0(int a0)
{
    unsigned int v1;  // ecx
    int v0;  // [bp-0x8], Other Possible Types: unsigned int

    v0 = v1;
    v0 = (a0 < 0 ? -(a0) : a0);
    return v0;
}
```

## `sub_10333e10` `0x10333e10`

_28 bytes. (leaf/helper — see body)_

```c
int sub_10333e10(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10337480(a1, a0, &v1);
    return a0;
}
```

## `sub_10333e30` `0x10333e30`

_28 bytes. (leaf/helper — see body)_

```c
int sub_10333e30(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10337530(a1, a0, &v1);
    return a0;
}
```

## `sub_10333e50` `0x10333e50`

_28 bytes. (leaf/helper — see body)_

```c
int sub_10333e50(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_103375e0(a1, a0, &v1);
    return a0;
}
```

## `sub_10333e70` `0x10333e70`

_30 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10333e70(unsigned int a0)
{
    return (!a0 ? 0 : sub_10337690((char *)&/* unsupported instruction */ + 3));
}
```

## `sub_10333e90` `0x10333e90`

_30 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10333e90(unsigned int a0)
{
    return (!a0 ? 0 : sub_103376c0((char *)&/* unsupported instruction */ + 3));
}
```

## `sub_10333eb0` `0x10333eb0`

_56 bytes. (leaf/helper — see body)_

```c
extern int g_1039d548;

unsigned int sub_10333eb0(int a0)
{
    char v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x8]

    v1 = sub_103376f0(a0);
    if (!v1)
    {
        sub_10335230();
        sub_103533ea(&v0, &g_1039d548);
    }
    return v1;
}
```

## `sub_10333ef0` `0x10333ef0`

_69 bytes. (leaf/helper — see body)_

```c
int sub_10333ef0(unsigned int a0, int a1, int a2)
{
    unsigned int v0;  // [bp-0x14]
    char v1;  // [bp-0x9]

    v0 = a0;
    sub_1031a280(&v0);
    sub_103147d0(a0);
    v1 = sub_10337970(&/* unsupported instruction */);
    sub_10337710(a1, a2, _INSERT(0, 0, v1));
    return a0;
}
```

## `sub_10333f40` `0x10333f40`

_69 bytes. (leaf/helper — see body)_

```c
int sub_10333f40(unsigned int a0, int a1, int a2)
{
    unsigned int v0;  // [bp-0x14]
    char v1;  // [bp-0x9]

    v0 = a0;
    sub_1031a280(&v0);
    sub_103147d0(a0);
    v1 = sub_10337970(&/* unsupported instruction */);
    sub_10337740(a1, a2, _INSERT(0, 0, v1));
    return a0;
}
```

## `sub_10333f90` `0x10333f90`

_82 bytes. (leaf/helper — see body)_

```c
int sub_10333f90(unsigned int a0, int a1, int a2)
{
    unsigned int v0;  // [bp-0x14]
    char v1;  // [bp-0xa]
    char v2;  // [bp-0x9]

    v0 = a0;
    sub_1031a280(&v0);
    sub_103147d0(a0);
    sub_1031a3c0(a0, 0, 0);
    sub_103378b0(&v2, &/* unsupported instruction */);
    sub_10337770(a1, a2, _INSERT(0, 0, v1));
    return a0;
}
```

## `sub_10333ff0` `0x10333ff0`

_24 bytes. (leaf/helper — see body)_

```c
int sub_10333ff0(unsigned int a0, int a1)
{
    char v0;  // [bp+0x0]

    return -(0 < sub_10334010(a1, &v0)) + 1;
}
```

## `sub_10334010` `0x10334010`

_47 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    int field_14;
} struct_0;

int sub_10334010(struct_0 *a0, int a1)
{
    int v1;  // eax
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    v1 = sub_103136c0(a1);
    return sub_10334040(0, v0->field_14, a1, v1);
}
```

## `sub_10334040` `0x10334040`

_164 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

unsigned int sub_10334040(struct_0 *a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4)
{
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0x8]

    if (*((int *)&a0->padding_8[12]) < a1)
        sub_103503dd();
    if (*((int *)&a0->padding_8[12]) - a1 < a2)
        a2 = *((int *)&a0->padding_8[12]) - a1;
    v4 = (a2 < a4 ? a2 : a4);
    v1 = v4;
    v0 = a3;
    v5 = sub_103340f0(&sub_10314a50(a0)->padding_0[a1]);
    if (!v5)
    {
        v2 = (a2 < a4 ? 4294967295 : a2 != a4);
        v3 = v2;
        return v3;
    }
    v3 = v5;
    return v3;
}
```

## `sub_103340f0` `0x103340f0`

_25 bytes. (leaf/helper — see body)_

```c
int sub_103340f0(int a0, int a1, int a2)
{
    char v0;  // [bp+0x0]

    return sub_10351234(a0, a1, a2, &v0);
}
```

## `sub_10334110` `0x10334110`

_24 bytes. (leaf/helper — see body)_

```c
int sub_10334110(unsigned int a0, int a1)
{
    char v0;  // [bp+0x0]

    return -(0 < sub_10335840(a1, &v0)) + 1;
}
```

## `sub_10334130` `0x10334130`

_24 bytes. (leaf/helper — see body)_

```c
int sub_10334130(unsigned int a0, int a1)
{
    char v0;  // [bp+0x0]

    return -(0 < sub_10334150(a1, &v0)) + 1;
}
```

## `sub_10334150` `0x10334150`

_48 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

unsigned int sub_10334150(struct_0 *a0, void* a1)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    v1 = sub_1031e920(a1);
    v2 = sub_10314a50(a1);
    return sub_10334040(v0, 0, *((int *)&v0->padding_8[12]), v2, v1);
}
```

## `sub_10334180` `0x10334180`

_45 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

int sub_10334180(struct_0 *a0, unsigned int a1)
{
    int v1[2];  // eax
    char v0;  // [bp-0xc]

    v1 = sub_1031b790(a0, &v0);
    sub_103341e0(v1[0], v1[1]);
    return a1;
}
```

## `sub_103341b0` `0x103341b0`

_43 bytes. (leaf/helper — see body)_

```c
int sub_103341b0(int *a0)
{
    char v0;  // [bp+0x0]

    sub_10334230(a0, a0[1], a0[2], &v0);
    return sub_10334210(a0, a0[1], a0[2], &v0);
}
```

## `sub_103341e0` `0x103341e0`

_39 bytes. (leaf/helper — see body)_

```c
unsigned int [3] sub_103341e0(unsigned int *idx, unsigned int a1, unsigned int a2)
{
    unsigned int v0[3];  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = idx;
    sub_10338af0(idx, &v1);
    idx[1] = a1;
    idx[2] = a2;
    return idx;
}
```

## `sub_10334210` `0x10334210`

_19 bytes. (leaf/helper — see body)_

```c
void sub_10334210(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10334250(a0, &v1);
    return;
}
```

## `sub_10334230` `0x10334230`

_22 bytes. (leaf/helper — see body)_

```c
int sub_10334230(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_103342a0(a0, &v1);
    return a0;
}
```

## `sub_10334250` `0x10334250`

_69 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
    unsigned int field_4;
} struct_0;

typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

int sub_10334250(struct_0 *a0)
{
    struct_0 *v2;  // eax
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    if (v0->field_0 != 0xfffffffe)
    {
        if (!v0->field_0)
            sub_10353616();
        v2 = sub_10314a50(v0->field_0);
        if (v0->field_4 >= (char *)v2 + *((int *)&v0->field_0->padding_8[12]))
            sub_10353616();
    }
    return v0->field_4;
}
```

## `sub_103342a0` `0x103342a0`

_73 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
    unsigned int field_4;
} struct_0;

typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

struct_0 * sub_103342a0(struct_0 *a0)
{
    unsigned int v2;  // eax
    struct_0 *idx;  // [bp-0x8]

    idx = a0;
    idx = a0;
    if (idx->field_0 != 4294967294)
    {
        if (!idx->field_0)
            sub_10353616();
        v2 = sub_10314a50(idx->field_0);
        if (idx->field_4 <= v2)
            sub_10353616();
    }
    idx->field_4 = idx->field_4 - 1;
    return idx;
}
```

## `sub_103342f0` `0x103342f0`

_45 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

unsigned int * sub_103342f0(struct_0 *a0, unsigned int *a1)
{
    unsigned int v1[2];  // eax
    char v0;  // [bp-0xc]

    v1 = sub_10326160(a0, &v0);
    sub_103341e0(a1, v1[0], v1[1]);
    return a1;
}
```

## `sub_10334320` `0x10334320`

_43 bytes. (leaf/helper — see body)_

```c
void sub_10334320(int *a0)
{
    char v0;  // [bp+0x0]

    sub_10326190(sub_10334350(a0, a0[1], a0[2], &v0));
    return;
}
```

