# elfbot.dll decompiled — jiru 0x10330560..0x103314a0

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10330560` `0x10330560`

_43 bytes. (leaf/helper — see body)_

```c
int sub_10330560(int a0, int a1, int a2, int a3)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10334730(a1, a2, a3, a0, a0, &v1);
    return a1 + a2;
}
```

## `sub_10330590` `0x10330590`

_129 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    unsigned int field_8;
} struct_0;

extern unsigned int g_1038e180;

unsigned int sub_10330590(struct_0 *a0, int a1, int a2)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned long v17;  // 4119
    unsigned short v9;  // fs
    unsigned long v10;  // 4147
    unsigned int v11;  // eax
    unsigned long v12;  // 4171
    int v13;  // edi
    int v14;  // esi
    int v15;  // ebx
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x28]
    struct_0 *v1;  // [bp-0x18]
    struct_0 *v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]
    char v6;  // [bp+0x0]

    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v11 = *((int *)v10);
    v3 = *((int *)v10);
    v2 = a0;
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v12) = &v3;
    v16 = sub_10330760(a1, g_1038e180 ^ &v5, v13, v14, v15, a0, &v0, v11, sub_1036d970, -1, &v6);
    if ((char)v16)
    {
        v4 = 0;
        v16 = sub_10330850(a0->field_4, a1, a2);
        a0->field_8 = v16;
        v4 = 4294967295;
    }
    v17 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v17) = v11;
    return v16;
}
```

## `sub_103305f6` `0x103305f6`

_30 bytes. (leaf/helper — see body)_

```c
extern char g_1033061b;

int sub_103305f6(void)
{
    unsigned int v1;  // [bp+0x100000]

    sub_103307e0();
    sub_103533ea(0, 0);
    v1 = 4294967295;
    return &g_1033061b;
}
```

## `sub_10330630` `0x10330630`

_51 bytes. (leaf/helper — see body)_

```c
int sub_10330630(unsigned int *a0)
{
    int v0;  // [bp-0xc]

    v0 = (!a0[1] ? 0 : a0[3] - a0[1] >> 1);
    return v0;
}
```

## `sub_10330670` `0x10330670`

_35 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    int field_8;
} struct_0;

int sub_10330670(struct_0 *a0, unsigned int a1)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_103323a0(a0->field_8, a0, a0, &v1);
    return a1;
}
```

## `sub_103306a0` `0x103306a0`

_51 bytes. (leaf/helper — see body)_

```c
int sub_103306a0(unsigned int *a0)
{
    int v0;  // [bp-0xc]

    v0 = (!a0[1] ? 0 : a0[2] - a0[1] >> 1);
    return v0;
}
```

## `sub_103306e0` `0x103306e0`

_118 bytes. (leaf/helper — see body)_

```c
int sub_103306e0(unsigned int *a0, int a1, int a2, int a3, int a4)
{
    int v0;  // [bp-0x20]
    char v1;  // [bp-0x18]
    char v2;  // [bp-0x10]
    int v3;  // [bp-0x8]

    v0 = (!sub_103306a0(a0) ? 0 : sub_10332460(sub_103414f0(&v2)));
    v3 = v0;
    sub_10331b50(a2, a3, 1, a4);
    sub_103414f0(&v1, a1, v3);
    sub_10332420(&v1, a1, v3);
    return a1;
}
```

## `sub_10330760` `0x10330760`

_123 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    unsigned int field_8;
    unsigned int field_c;
} struct_0;

char sub_10330760(struct_0 *idx, int a1)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = idx;
    memset(&idx->field_4, 0, 12);
    if (!a1)
        return 0;
    if (sub_10331b30(idx, &v1) < a1)
    {
        sub_10331e80();
    }
    else
    {
        idx->field_4 = sub_1031eba0(idx, a1);
        idx->field_8 = idx->field_4;
        idx->field_c = idx->field_4 + a1 * 2;
    }
    return 1;
}
```

## `sub_1033078f` `0x1033078f`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1033078f(void)
{
}
```

## `sub_103307e0` `0x103307e0`

_102 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    int field_8;
    unsigned int field_c;
} struct_0;

struct_0 * sub_103307e0(struct_0 *a0)
{
    struct_0 *idx;  // [bp-0x8]

    idx = a0;
    idx = a0;
    if (idx->field_4)
    {
        sub_1033e420(idx->field_4, idx->field_8);
        sub_1033e3d0(idx->field_4, idx->field_c - idx->field_4 >> 1);
    }
    idx->field_4 = 0;
    idx->field_8 = 0;
    idx->field_c = 0;
    return idx;
}
```

## `sub_10330850` `0x10330850`

_46 bytes. (leaf/helper — see body)_

```c
int sub_10330850(int a0, int a1, int a2, int a3)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10334770(a1, a2, a3, a0, a0, &v1);
    return a1 + a2 * 2;
}
```

## `sub_10330880` `0x10330880`

_57 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10330880(unsigned int *a0)
{
    unsigned int v0;  // [bp-0xc]

    v0 = (!a0[1] ? 0 : (int)((a0[3] - a0[1]) / 28));
    return v0;
}
```

## `sub_103308c0` `0x103308c0`

_35 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
} struct_0;

int sub_103308c0(struct_0 *a0, unsigned int a1)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_103327f0(a0->field_4, a0, a0, &v1);
    return a1;
}
```

## `sub_103308f0` `0x103308f0`

_35 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    int field_8;
} struct_0;

int sub_103308f0(struct_0 *a0, unsigned int a1)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_103327f0(a0->field_8, a0, a0, &v1);
    return a1;
}
```

## `sub_10330920` `0x10330920`

_57 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10330920(unsigned int *a0)
{
    unsigned int v0;  // [bp-0xc]

    v0 = (!a0[1] ? 0 : (int)((a0[2] - a0[1]) / 28));
    return v0;
}
```

## `sub_10330960` `0x10330960`

_118 bytes. (leaf/helper — see body)_

```c
int sub_10330960(unsigned int *a0, int a1, int a2, int a3, int a4)
{
    int v0;  // [bp-0x20]
    char v1;  // [bp-0x18]
    char v2;  // [bp-0x10]
    int v3;  // [bp-0x8]

    v0 = (!sub_10330920(a0) ? 0 : sub_103324c0(sub_103414f0(&v2)));
    v3 = v0;
    sub_10331f90(a2, a3, 1, a4);
    sub_103414f0(&v1, a1, v3);
    sub_10332480(&v1, a1, v3);
    return a1;
}
```

## `sub_103309e0` `0x103309e0`

_123 bytes. (leaf/helper — see body)_

```c
char sub_103309e0(unsigned int *idx, int a1)
{
    unsigned int v0[4];  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = idx;
    memset(idx + 1, 0, 12);
    if (!a1)
        return 0;
    if (sub_10331f40(idx, &v1) < a1)
    {
        sub_10332300();
    }
    else
    {
        idx[1] = sub_10332380(a1);
        idx[2] = idx[1];
        idx[3] = a1 * 28 + idx[1];
    }
    return 1;
}
```

## `sub_10330a0f` `0x10330a0f`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10330a0f(void)
{
}
```

## `sub_10330a60` `0x10330a60`

_110 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    int field_8;
    unsigned int field_c;
} struct_0;

struct_0 * sub_10330a60(struct_0 *a0)
{
    struct_0 *idx;  // [bp-0x8]

    idx = a0;
    idx = a0;
    if (idx->field_4)
    {
        sub_10331f60(idx->field_4, idx->field_8);
        sub_1033e3d0(idx->field_4, (idx->field_c - idx->field_4) / 28);
    }
    idx->field_4 = 0;
    idx->field_8 = 0;
    idx->field_c = 0;
    return idx;
}
```

## `sub_10330ad0` `0x10330ad0`

_46 bytes. (leaf/helper — see body)_

```c
int sub_10330ad0(int a0, int a1, int a2, int a3)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_103347b0(a1, a2, a3, a0, a0, &v1);
    return a2 * 28 + a1;
}
```

## `sub_10330b00` `0x10330b00`

_93 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
} struct_0;

extern unsigned int g_1038e180;
extern char g_10390664;

struct_0 * sub_10330b00(struct_0 *a0, struct_0 *a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4154
    unsigned long v11;  // 4128
    unsigned int v0;  // [bp-0x18]
    struct_0 *v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036d998;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_1032de60(v1, a1);
    *((char **)&v1->padding_0[0]) = &g_10390664;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_10330b60` `0x10330b60`

_198 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
    unsigned int field_18;
} struct_0;

extern unsigned int g_1039011c;

struct_0 * sub_10330b60(struct_0 *a0, unsigned int a1, unsigned int a2, unsigned short a3)
{
    struct_0 *v2;  // eax
    struct_0 *v3;  // eax
    unsigned int v4;  // eax
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0x8]

    if (a0->field_14 < a1)
    {
        sub_103503dd(a0);
    }
    else if (g_1039011c - a0->field_14 <= a2)
    {
        sub_1035039e();
    }
    else if (a2 > 0)
    {
        v1 = a0->field_14 + a2;
        if (!(char)sub_1031e940(a0, v1, 0))
            return a0;
        v2 = sub_1031a4a0(a0);
        v3 = sub_1031a4a0(a0);
        v4 = _INSERT(sub_1031ebf0(&v3->padding_0[2 * a1 + 2 * a2], a0->field_18 - a1 - a2, &v2->padding_0[2 * a1], a0->field_14 - a1) CONCAT 0, 0, a3);
        v0 = v4;
        sub_10326000(a0, a1, a2);
        sub_1031a440(a0, v1);
        return a0;
    }
    else
    {
        return a0;
    }
}
```

## `sub_10330c30` `0x10330c30`

_41 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10330c30(unsigned int a0, unsigned int a1)
{
    unsigned int v2;  // ecx
    unsigned int v0;  // [bp-0x8]
    char v1;  // [bp+0xc]

    v0 = v2;
    v0 = (!a1 ? 0 : sub_10332760(&v1));
    return v0;
}
```

## `sub_10330c60` `0x10330c60`

_23 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_10330c60(unsigned int a0, unsigned int a1, unsigned int *a2)
{
    unsigned int v2;  // edx
    char v0;  // [bp+0x0]

    sub_1032fad0(a2, sub_10330c80(&v0), v2);
    return a2;
}
```

## `sub_10330c80` `0x10330c80`

_13 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10330c80(void)
{
    return 4294967295;
}
```

## `sub_10330c90` `0x10330c90`

_23 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_10330c90(unsigned int a0, unsigned int a1, unsigned int *a2)
{
    unsigned int v2;  // edx
    char v0;  // [bp+0x0]

    sub_1032fad0(a2, sub_10330cb0(&v0), v2);
    return a2;
}
```

## `sub_10330cb0` `0x10330cb0`

_12 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10330cb0(void)
{
    return 0;
}
```

## `sub_10330cc0` `0x10330cc0`

_29 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_10330cc0(unsigned int *a0)
{
    unsigned int v0;  // eax
    unsigned int v1;  // edx

    v0 = sub_10330c80();
    sub_1032fad0(a0, v0 - 1, v1 - (v0 < 1));
    return a0;
}
```

## `sub_10330ce0` `0x10330ce0`

_29 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_10330ce0(unsigned int *a0)
{
    unsigned int v0;  // eax
    unsigned int v1;  // edx

    v0 = sub_10330c80();
    sub_1032fad0(a0, v0 - 2, v1 - (v0 < 2));
    return a0;
}
```

## `sub_10330d00` `0x10330d00`

_29 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_10330d00(unsigned int *a0)
{
    unsigned int v0;  // eax
    unsigned int v1;  // edx

    v0 = sub_10330cb0();
    sub_1032fad0(a0, v0 + 1, v1 + (v0 + 1 < v0));
    return a0;
}
```

## `sub_10330d20` `0x10330d20`

_70 bytes. (leaf/helper — see body)_

```c
char sub_10330d20(unsigned int a0, unsigned int a1, int a2)
{
    unsigned int v4;  // edx
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    unsigned int v2[2];  // [bp-0xc]
    unsigned int v3;  // [bp+0x8]

    v1 = sub_1032ff80(sub_10330c60(a0, a1, v2));
    if (a2 == v1 && v3 == v4)
        v0 = 1;
    else
        v0 = 0;
    return v0;
}
```

## `sub_10330d70` `0x10330d70`

_97 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10330d70(unsigned int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    if ((char)sub_10332610(a0, a1, &v1))
    {
        return 0;
    }
    else if ((char)sub_103325c0(a0, a1))
    {
        return 1;
    }
    else
    {
        v0 = a1;
        return (!sub_10330d20(a0, 0, a0) ? 5 : 2);
    }
}
```

## `sub_10330de0` `0x10330de0`

_10 bytes. (leaf/helper — see body)_

```c
void sub_10330de0(void)
{
    char v0;  // [bp+0x0]

    sub_103326a0(&v0);
    return;
}
```

## `sub_10330df0` `0x10330df0`

_9 bytes. (leaf/helper — see body)_

```c
unsigned short sub_10330df0(void)
{
    return 1;
}
```

## `sub_10330e00` `0x10330e00`

_103 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

void sub_10330e00(void)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4135
    unsigned long v12;  // 4149
    unsigned long v13;  // 4113
    int v0;  // [bp-0x40]
    int v1;  // [bp-0x3c]
    char v2;  // [bp-0x38]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036d9c8;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v3 = *((int *)v11);
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v3;
    v1 = sub_10330e70(g_1038e180 ^ &v6);
    v0 = v1;
    v5 = 0;
    sub_10333cd0(v0);
    v5 = 4294967295;
    sub_1032f840(&v2);
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v13) = v3;
    return;
}
```

## `sub_10330e70` `0x10330e70`

_127 bytes. refs "Day of month value is out of range 1..31"_

```c
extern unsigned int g_1038e180;
extern char g_1039064c;

int sub_10330e70(int a0)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4138
    unsigned long v13;  // 4152
    unsigned long v14;  // 4125
    unsigned int v0;  // [bp-0x3c]
    int v1;  // [bp-0x38]
    int v2;  // [bp-0x34]
    char v3;  // [bp-0x2c]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    char v6;  // [bp-0x8], Other Possible Types: unsigned int
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036da00;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v4 = *((int *)v12);
    v0 = g_1038e180 ^ &v7;
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v4;
    v2 = sub_10314590(&v3, "Day of month value is out of range 1..31");
    v1 = v2;
    v6 = 0;
    sub_1032f720(a0, v1);
    v6 = 2;
    sub_10314610(&v3);
    *((char **)a0) = &g_1039064c;
    v14 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v14) = v4;
    return a0;
}
```

## `sub_10330ef0` `0x10330ef0`

_10 bytes. (leaf/helper — see body)_

```c
void sub_10330ef0(void)
{
    char v0;  // [bp+0x0]

    sub_103326b0(&v0);
    return;
}
```

## `sub_10330f00` `0x10330f00`

_9 bytes. (leaf/helper — see body)_

```c
unsigned short sub_10330f00(void)
{
    return 1400;
}
```

## `sub_10330f10` `0x10330f10`

_103 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10330f10(void)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4135
    unsigned long v11;  // 4149
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    int v0;  // [bp-0x40]
    int v1;  // [bp-0x3c]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036da28;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = sub_10330f80(g_1038e180 ^ &v5);
    v0 = v1;
    v4 = 0;
    sub_103347f0(v0);
    v4 = 4294967295;
    v12 = sub_10331030();
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_10330f80` `0x10330f80`

_127 bytes. refs "Year is out of valid range: 1400..10000"_

```c
extern unsigned int g_1038e180;
extern char g_1039069c;

int sub_10330f80(int a0)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4138
    unsigned long v13;  // 4152
    unsigned long v14;  // 4125
    unsigned int v0;  // [bp-0x3c]
    int v1;  // [bp-0x38]
    int v2;  // [bp-0x34]
    char v3;  // [bp-0x2c]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    char v6;  // [bp-0x8], Other Possible Types: unsigned int
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036da60;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v4 = *((int *)v12);
    v0 = g_1038e180 ^ &v7;
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v4;
    v2 = sub_10314590(&v3, "Year is out of valid range: 1400..10000");
    v1 = v2;
    v6 = 0;
    sub_1032f720(a0, v1);
    v6 = 2;
    sub_10314610(&v3);
    *((char **)a0) = &g_1039069c;
    v14 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v14) = v4;
    return a0;
}
```

## `sub_10331000` `0x10331000`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10331000(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10331030(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_10331030` `0x10331030`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

void sub_10331030(int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4137
    unsigned long v11;  // 4153
    unsigned long v12;  // 4113
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036da88;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    v4 = 0;
    v4 = 4294967295;
    sub_1032f780(v1);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v2;
    return;
}
```

## `sub_10331080` `0x10331080`

_10 bytes. (leaf/helper — see body)_

```c
void sub_10331080(void)
{
    char v0;  // [bp+0x0]

    sub_103326c0(&v0);
    return;
}
```

## `sub_10331090` `0x10331090`

_103 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10331090(void)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4135
    unsigned long v11;  // 4149
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    int v0;  // [bp-0x40]
    int v1;  // [bp-0x3c]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036dab8;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = sub_10331100(g_1038e180 ^ &v5);
    v0 = v1;
    v4 = 0;
    sub_103348a0(v0);
    v4 = 4294967295;
    v12 = sub_103311b0();
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_10331100` `0x10331100`

_127 bytes. refs "Month number is out of range 1..12"_

```c
extern unsigned int g_1038e180;
extern char g_103906d0;

int sub_10331100(int a0)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4138
    unsigned long v13;  // 4152
    unsigned long v14;  // 4125
    unsigned int v0;  // [bp-0x3c]
    int v1;  // [bp-0x38]
    int v2;  // [bp-0x34]
    char v3;  // [bp-0x2c]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    char v6;  // [bp-0x8], Other Possible Types: unsigned int
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036daf0;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v4 = *((int *)v12);
    v0 = g_1038e180 ^ &v7;
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v4;
    v2 = sub_10314590(&v3, "Month number is out of range 1..12");
    v1 = v2;
    v6 = 0;
    sub_1032f720(a0, v1);
    v6 = 2;
    sub_10314610(&v3);
    *((char **)a0) = &g_103906d0;
    v14 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v14) = v4;
    return a0;
}
```

## `sub_10331180` `0x10331180`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10331180(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_103311b0(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_103311b0` `0x103311b0`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

void sub_103311b0(int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4137
    unsigned long v11;  // 4153
    unsigned long v12;  // 4113
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036db18;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    v4 = 0;
    v4 = 4294967295;
    sub_1032f780(v1);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v2;
    return;
}
```

## `sub_10331200` `0x10331200`

_49 bytes. (leaf/helper — see body)_

```c
int sub_10331200(int a0, unsigned int a1, int a2)
{
    int v1[2];  // eax
    char v0;  // [bp-0xc]

    v1 = sub_10334540(&v0, a2, a0);
    sub_10331240(v1[0], v1[1]);
    return a1;
}
```

## `sub_10331240` `0x10331240`

_32 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_10331240(unsigned int *a0, unsigned int a1, unsigned int a2)
{
    unsigned int *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_1032fad0(v0, a1, a2);
    return v0;
}
```

## `sub_10331260` `0x10331260`

_21 bytes. (leaf/helper — see body)_

```c
int sub_10331260(int a0, int a1)
{
    char v0;  // [bp+0x0]

    return sub_10331280(a0, a1, &v0);
}
```

## `sub_10331280` `0x10331280`

_13 bytes. (leaf/helper — see body)_

```c
int sub_10331280(void)
{
    unsigned int v0;  // [bp+0x4]

    return sub_1032ff80(&v0);
}
```

## `sub_10331290` `0x10331290`

_83 bytes. (leaf/helper — see body)_

```c
char sub_10331290(int *a0, int *a1)
{
    int v3;  // edx
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    int v2;  // [bp-0xc]

    v2 = sub_1032f340(a0);
    v1 = sub_1032f340(a1);
    if (v3 <= v3 && (v3 < v3 || v2 < v1))
        v0 = 1;
    else
        v0 = 0;
    return v0;
}
```

## `sub_103312f0` `0x103312f0`

_196 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    int field_4;
} struct_0;

struct_0 * sub_103312f0(struct_0 *idx, unsigned int a1, int *a2)
{
    int v5;  // edi
    int v6;  // esi
    int v7;  // eax
    int v8;  // edx
    unsigned int v9;  // eax
    int v10;  // eax
    int v11;  // eax
    unsigned int v12[2];  // eax
    unsigned int v13;  // edx
    unsigned int v0;  // [bp-0x24]
    int v1;  // [bp-0x20]
    char v2;  // [bp-0x1c]
    char v3;  // [bp-0x10]
    char v4;  // [bp-0xc]

    sub_1032fad0(idx, 1, 0);
    if (!(char)sub_103326d0(v5, v6, idx, v0, v1) && !(char)sub_103313c0() && !(char)sub_10331410())
    {
        v7 = sub_10336b20();
        v9 = sub_103544a0(v7, 0, sub_10331440(), v8);
        v10 = sub_1032f340(a2);
        sub_1032fad0(&v0, v9 + v10, v8 + v8 + (v9 + v10 < v9));
        idx->field_0 = v0;
        idx->field_4 = v1;
        return idx;
    }
    v11 = sub_103326f0(&v3);
    sub_103314a0(&v4, &v2, v11);
    v12 = sub_10334950(&v4, &v2, v11);
    v13 = v12[1];
    idx->field_0 = v12[0];
    idx->field_4 = v13;
    return idx;
}
```

## `sub_103313c0` `0x103313c0`

_25 bytes. (leaf/helper — see body)_

```c
int sub_103313c0(int *a0)
{
    int *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_103313e0(*(a0), a0, &v1);
}
```

## `sub_103313e0` `0x103313e0`

_37 bytes. (leaf/helper — see body)_

```c
char sub_103313e0(unsigned int a0)
{
    int v1;  // ecx
    char v0;  // [bp+0x0]

    sub_1032fd60(&/* unsupported instruction */);
    return a0 == sub_10336b20(v1, &v0);
}
```

## `sub_10331410` `0x10331410`

_35 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10331410(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return (!(char)sub_10332710(a0, &v1) ? 0 : sub_10332660());
}
```

## `sub_1033142d` `0x1033142d`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1033142d(void)
{
}
```

## `sub_10331440` `0x10331440`

_56 bytes. (leaf/helper — see body)_

```c
int sub_10331440(void)
{
    int v4;  // edx
    unsigned int v0;  // [bp-0x14]
    int v1;  // [bp-0xc]
    int v2;  // [bp-0x8]

    v1 = 86400;
    v2 = 0;
    v0 = sub_1032f360();
    return sub_103544a0(v1, v2, v0, v4);
}
```

## `sub_10331480` `0x10331480`

_19 bytes. (leaf/helper — see body)_

```c
void sub_10331480(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10332660(a0, &v1);
    return;
}
```

## `sub_103314a0` `0x103314a0`

_32 bytes. (leaf/helper — see body)_

```c
unsigned int [2] sub_103314a0(unsigned int *a0, unsigned int *a1)
{
    unsigned int v0;  // edx

    v0 = a0[1];
    *(a1) = *(a0);
    a1[1] = v0;
    return a1;
}
```

