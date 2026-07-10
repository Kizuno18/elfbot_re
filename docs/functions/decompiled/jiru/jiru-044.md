# elfbot.dll decompiled — jiru 0x10335960..0x10336f80

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10335960` `0x10335960`

_136 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10335960(unsigned int a0, int a1)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4140
    unsigned long v13;  // 4154
    unsigned long v14;  // 4117
    unsigned int v0;  // [bp-0x40]
    int v1;  // [bp-0x3c]
    int v2;  // [bp-0x38]
    unsigned int v3;  // [bp-0x30]
    char v4;  // [bp-0x2c]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    char v7;  // [bp-0x8], Other Possible Types: unsigned int
    char v8;  // [bp-0x4]

    v7 = 4294967295;
    v6 = sub_1036e4e1;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v5 = *((int *)v12);
    v0 = g_1038e180 ^ &v8;
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v5;
    v3 = 0;
    v2 = sub_10332ed0(a0, &v4);
    v1 = v2;
    v7 = 1;
    sub_103359f0(a1, a0, v1);
    v3 |= 1;
    v7 = 0;
    sub_1031a3a0(&v4);
    v14 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v14) = v5;
    return a1;
}
```

## `sub_103359f0` `0x103359f0`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_103359f0(unsigned int a0, unsigned int a1, int a2)
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
    v3 = sub_1036e519;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = v10;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v2;
    v1 = 0;
    sub_1031e760(a0, a2);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v2;
    return a0;
}
```

## `sub_10335a50` `0x10335a50`

_84 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10335a50(int a0, int a1)
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
    sub_10336aa0(a1, g_1038e180 ^ &v2, a0, v8, sub_1036e548, -1, &v3);
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v10) = v8;
    return a0;
}
```

## `sub_10335ab0` `0x10335ab0`

_84 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10335ab0(int a0, int a1)
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
    sub_10336ae0(a1, g_1038e180 ^ &v2, a0, v8, sub_1036e578, -1, &v3);
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v10) = v8;
    return a0;
}
```

## `sub_10335b10` `0x10335b10`

_24 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

int sub_10335b10(struct_0 **a0, unsigned int a1)
{
    struct_0 **v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return (*(a0))(a1, a0, &v1);
}
```

## `sub_10335b30` `0x10335b30`

_33 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

struct_0 * sub_10335b30(struct_0 *a0, unsigned int a1)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10347e90(a0, &v1);
    a0->field_4 = a1;
    return a0;
}
```

## `sub_10335b60` `0x10335b60`

_99 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103908a4;

unsigned int sub_10335b60(int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4142
    unsigned int v10;  // eax
    unsigned long v11;  // 4158
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v2 = 4294967295;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v10 = *((int *)v9);
    v1 = *((int *)v9);
    v0 = a0;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v1;
    *((char **)a0) = &g_103908a4;
    v2 = 1;
    sub_103368a0(g_1038e180 ^ &v3, a0, v10, sub_1036e5b3, 0, &v4);
    v12 = sub_10335bd0(g_1038e180 ^ &v3, a0, v10, sub_1036e5b3, -1, &v4);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v10;
    return v12;
}
```

## `sub_10335bd0` `0x10335bd0`

_99 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103908b0;

unsigned int sub_10335bd0(int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4142
    unsigned long v11;  // 4158
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036e5e3;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    *((char **)v1) = &g_103908b0;
    v4 = 1;
    v4 = 0;
    sub_10314610(v1 + 48);
    v4 = 4294967295;
    v12 = sub_10314360(v1);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_10335c40` `0x10335c40`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10335c40(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_10335bd0(v0);
    if (((char)a1 & 1))
        sub_10350abd(v0);
    return v0;
}
```

## `sub_10335c70` `0x10335c70`

_240 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

void sub_10335c70(unsigned int a0)
{
    unsigned long v13;  // ldt
    unsigned long v14;  // gdt
    unsigned short v15;  // fs
    unsigned long v16;  // 4148
    unsigned int v17;  // ebx
    unsigned int v18;  // esi
    unsigned int v19;  // edi
    unsigned long v20;  // 4170
    unsigned long v22;  // 4119
    unsigned int v0;  // [bp-0x50]
    unsigned int v1;  // [bp-0x4c]
    unsigned int v2;  // [bp-0x48]
    unsigned int v3;  // [bp-0x44]
    int v4;  // [bp-0x40]
    int v5;  // [bp-0x3c]
    char v6;  // [bp-0x30]
    char *v7;  // [bp-0x14], Other Possible Types: unsigned int
    unsigned int v8;  // [bp-0x10]
    unsigned int v9;  // [bp-0xc]
    char v10;  // [bp-0x8], Other Possible Types: unsigned int
    char v11;  // [bp-0x4]

    v10 = 4294967295;
    v9 = sub_1036e608;
    v16 = _ccall(v13, v14, (unsigned int)v15, 0);
    v8 = *((int *)v16);
    v7 = a0;
    v3 = v17;
    v2 = v18;
    v1 = v19;
    v0 = g_1038e180 ^ &v11;
    v20 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int **)v20) = &v8;
    v7 = &v0;
    if ((char)sub_10325be0(a0 + 48))
    {
        v10 = 0;
        sub_10335e10((unsigned int)sub_10314310(a0));
        if (sub_10333210(a0 + 40))
        {
            if (!(char)sub_10325be0(a0 + 48))
                sub_1031a660(a0 + 48, ": ");
            v5 = sub_10335d90(&v6);
            v4 = v5;
            v10 = 1;
            sub_10316de0(a0 + 48, v4);
            v10 = 0;
            sub_10314610(&v6);
        }
    }
    v10 = 4294967295;
    sub_102ec9a0(a0 + 48);
    v22 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int *)v22) = v8;
    return;
}
```

## `sub_10335d3a` `0x10335d3a`

_24 bytes. (leaf/helper — see body)_

```c
int sub_10335d3a(void)
{
    int v1;  // [bp+0xfffd0]
    unsigned int v2;  // [bp+0xfffd4]
    unsigned int v3;  // [bp+0x100000]

    v2 = (unsigned int)sub_10314310(v1);
    v3 = 4294967295;
    return sub_10335d61;
}
```

## `sub_10335d52` `0x10335d52`

_6 bytes. (leaf/helper — see body)_

```c
extern char g_10335d58;

int sub_10335d52(void)
{
    return &g_10335d58;
}
```

## `sub_10335d61` `0x10335d61`

_5 bytes. (leaf/helper — see body)_

```c
int sub_10335d61(void)
{
}
```

## `sub_10335d90` `0x10335d90`

_115 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    char padding_0[4];
    struct struct_3 *field_4;
} struct_2;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_0 {
    char padding_0[8];
    struct struct_1 *field_8;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern unsigned int g_1038e180;

int sub_10335d90(struct_2 *a0, unsigned int a1)
{
    unsigned long v3;  // ldt
    unsigned long v4;  // gdt
    unsigned short v5;  // fs
    unsigned long v6;  // 4137
    unsigned int v7;  // eax
    unsigned long v8;  // 4151
    unsigned int v9;  // eax
    unsigned long v10;  // 4131
    unsigned int v0;  // [bp-0x10]
    char v1;  // [bp-0x4]
    char v2;  // [bp+0x0]

    v6 = _ccall(v3, v4, (unsigned int)v5, 0);
    v7 = *((int *)v6);
    v0 = *((int *)v6);
    v8 = _ccall(v3, v4, (unsigned int)v5, 0);
    *((unsigned int **)v8) = &v0;
    v9 = sub_10336b20(g_1038e180 ^ &v1, a0, 0, v7, sub_1036e649, -1, &v2);
    a0->field_4->field_0->field_8(a1, v9);
    v10 = _ccall(v3, v4, (unsigned int)v5, 0);
    *((unsigned int *)v10) = v7;
    return a1;
}
```

## `sub_10335e10` `0x10335e10`

_25 bytes. (leaf/helper — see body)_

```c
int sub_10335e10(unsigned int a0, int a1)
{
    unsigned int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_10314720(v0, a1);
}
```

## `sub_10335e30` `0x10335e30`

_95 bytes. (leaf/helper — see body)_

```c
void sub_10335e30(unsigned int a0)
{
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x8]
    char v2;  // [bp+0x0]

    v1 = a0;
    if (sub_10336b20(a0, &v2))
    {
        v0 = sub_10336b20(sub_10336b20(sub_10336b20() + 56) + 28);
        sub_10335e90((unsigned int)sub_10335c70(a0));
        return;
    }
    sub_10335c70(a0);
    return;
}
```

## `sub_10335e90` `0x10335e90`

_290 bytes. refs ": \", ", \"_

```c
extern unsigned int g_1038e180;

void sub_10335e90(int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    unsigned short v14;  // fs
    unsigned long v15;  // 4145
    unsigned int v16;  // ecx
    unsigned long v17;  // 4167
    unsigned long v18;  // 4119
    unsigned int v0;  // [bp-0x70]
    int v1;  // [bp-0x60]
    int v2;  // [bp-0x5c]
    int v3;  // [bp-0x58]
    int v4;  // [bp-0x54]
    char v5;  // [bp-0x4c]
    char v6;  // [bp-0x30]
    char *v7;  // [bp-0x14], Other Possible Types: unsigned int
    unsigned int v8;  // [bp-0x10]
    unsigned int v9;  // [bp-0xc]
    unsigned int v10;  // [bp-0x8], Other Possible Types: char
    char v11;  // [bp-0x4]

    v10 = 4294967295;
    v9 = sub_1036e680;
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    v8 = *((int *)v15);
    v7 = v16;
    v0 = g_1038e180 ^ &v11;
    v17 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v17) = &v8;
    v7 = &v0;
    v10 = 0;
    if ((char)sub_10325be0(a3))
    {
        sub_10335e10(a3, a0);
        if (!(char)sub_10332c90(a1))
        {
            sub_1031a660(a3, ": \"");
            v4 = sub_10332ce0(a1, &v6);
            v3 = v4;
            v10 = 1;
            sub_10316de0(a3, v3);
            v10 = 0;
            sub_10314610(&v6);
            sub_1031a660(a3, "\"");
        }
        if (!(char)sub_10332c90(a2))
        {
            sub_1031a660(a3, ", \"");
            v2 = sub_10332ce0(a2, &v5);
            v1 = v2;
            v10 = 2;
            sub_10316de0(a3, v1);
            v10 = 0;
            sub_10314610(&v5);
            sub_1031a660(a3, "\"");
        }
    }
    sub_102ec9a0(a3);
    v18 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int *)v18) = v8;
    return;
}
```

## `sub_10335fa0` `0x10335fa0`

_19 bytes. (leaf/helper — see body)_

```c
int sub_10335fa0(void)
{
    unsigned int v1;  // [bp+0xfffb8]
    unsigned int v2;  // [bp+0x100000]
    unsigned int v3;  // [bp+0x10000c]

    v1 = v3;
    v2 = 4294967295;
    return sub_10335fc2;
}
```

## `sub_10335fb3` `0x10335fb3`

_6 bytes. (leaf/helper — see body)_

```c
int sub_10335fb3(void)
{
    return sub_10335fb9;
}
```

## `sub_10335fb9` `0x10335fb9`

_9 bytes. (leaf/helper — see body)_

```c
void sub_10335fb9(void)
{
    unsigned int v1;  // [bp+0x100000]

    v1 = 4294967295;
}
```

## `sub_10335fc2` `0x10335fc2`

_3 bytes. (leaf/helper — see body)_

```c
int sub_10335fc2(void)
{
}
```

## `sub_10335fe0` `0x10335fe0`

_99 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103908cc;

unsigned int sub_10335fe0(int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4142
    unsigned int v10;  // eax
    unsigned long v11;  // 4158
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v2 = 4294967295;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v10 = *((int *)v9);
    v1 = *((int *)v9);
    v0 = a0;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v1;
    *((char **)a0) = &g_103908cc;
    v2 = 1;
    sub_103369a0(g_1038e180 ^ &v3, a0, v10, sub_1036e6b3, 0, &v4);
    v2 = 4294967295;
    v12 = sub_10335bd0(a0);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v10;
    return v12;
}
```

## `sub_10336050` `0x10336050`

_95 bytes. (leaf/helper — see body)_

```c
void sub_10336050(unsigned int a0)
{
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x8]
    char v2;  // [bp+0x0]

    v1 = a0;
    if (sub_10336b20(a0, &v2))
    {
        v0 = sub_10336b20(sub_10336b20(sub_10336b20() + 56) + 28);
        sub_10337e90((unsigned int)sub_10335c70(a0));
        return;
    }
    sub_10335c70(a0);
    return;
}
```

## `sub_103360b0` `0x103360b0`

_132 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103907a8;
extern char g_103907b0;

unsigned int sub_103360b0(int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4188
    unsigned long v11;  // 4192
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x1c]
    int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036e6ff;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    *((char **)a0) = &g_103907b0;
    *((char **)(a0 + 40)) = &g_103907a8;
    v4 = 1;
    v4 = 0;
    v1 = (!a0 ? 0 : a0 + 40);
    sub_10313d70(v1);
    v4 = 4294967295;
    v12 = sub_10314360(a0);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_10336140` `0x10336140`

_142 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390784;
extern char g_10390794;
extern char g_1039079c;

unsigned int sub_10336140(unsigned int idx)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4195
    unsigned long v11;  // 4199
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036e74f;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    *((char **)idx) = &g_1039079c;
    *((char **)(idx + 40)) = &g_10390794;
    *((char **)(idx + 60)) = &g_10390784;
    v4 = 1;
    v4 = 0;
    v1 = (!idx ? 0 : idx + 60);
    sub_10313bb0(v1);
    v4 = 4294967295;
    v12 = sub_103360b0(idx);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_103361d0` `0x103361d0`

_148 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_103361d0(int a0)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4137
    unsigned long v13;  // 4151
    unsigned long v14;  // 4117
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036e77b;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v4 = *((int *)v12);
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v4;
    v2 = sub_10350a53(64, g_1038e180 ^ &v7);
    v6 = 0;
    v1 = (!v2 ? 0 : sub_10334f50(v2, a0 - 60));
    v3 = v1;
    v6 = 4294967295;
    v0 = (!v3 ? 0 : v3 + 60);
    v14 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v14) = v4;
    return v0;
}
```

## `sub_10336270` `0x10336270`

_42 bytes. (leaf/helper — see body)_

```c
extern int g_1039d384;

int sub_10336270(int a0)
{
    char v0;  // [bp-0x44]

    sub_10334f50(&v0, a0 - 60);
    return sub_103533ea(&v0, &g_1039d384);
}
```

## `sub_103362a0` `0x103362a0`

_132 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103907e0;
extern char g_103907e8;

void sub_103362a0(int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4188
    unsigned long v11;  // 4192
    unsigned long v12;  // 4113
    unsigned int v0;  // [bp-0x1c]
    int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036e7cf;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    *((char **)a0) = &g_103907e8;
    *((char **)(a0 + 40)) = &g_103907e0;
    v4 = 1;
    v4 = 0;
    v1 = (!a0 ? 0 : a0 + 40);
    sub_10313d70(v1);
    v4 = 4294967295;
    sub_1032f840(a0);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v2;
    return;
}
```

## `sub_10336330` `0x10336330`

_142 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103907bc;
extern char g_103907cc;
extern char g_103907d4;

void sub_10336330(unsigned int idx)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4195
    unsigned long v11;  // 4199
    unsigned long v12;  // 4113
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036e81f;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    *((char **)idx) = &g_103907d4;
    *((char **)(idx + 40)) = &g_103907cc;
    *((char **)(idx + 60)) = &g_103907bc;
    v4 = 1;
    v4 = 0;
    v1 = (!idx ? 0 : idx + 60);
    sub_10313bb0(v1);
    v4 = 4294967295;
    sub_103362a0(idx);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v2;
    return;
}
```

## `sub_103363c0` `0x103363c0`

_148 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_103363c0(int a0)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4137
    unsigned long v13;  // 4151
    unsigned long v14;  // 4117
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036e84b;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v4 = *((int *)v12);
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v4;
    v2 = sub_10350a53(64, g_1038e180 ^ &v7);
    v6 = 0;
    v1 = (!v2 ? 0 : sub_10335090(v2, a0 - 60));
    v3 = v1;
    v6 = 4294967295;
    v0 = (!v3 ? 0 : v3 + 60);
    v14 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v14) = v4;
    return v0;
}
```

## `sub_10336460` `0x10336460`

_42 bytes. (leaf/helper — see body)_

```c
extern int g_1039d44c;

int sub_10336460(int a0)
{
    char v0;  // [bp-0x44]

    sub_10335090(&v0, a0 - 60);
    return sub_103533ea(&v0, &g_1039d44c);
}
```

## `sub_10336490` `0x10336490`

_132 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390858;
extern char g_10390860;

void sub_10336490(int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4188
    unsigned long v11;  // 4192
    unsigned long v12;  // 4113
    unsigned int v0;  // [bp-0x1c]
    int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036e89f;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    *((char **)a0) = &g_10390860;
    *((char **)(a0 + 40)) = &g_10390858;
    v4 = 1;
    v4 = 0;
    v1 = (!a0 ? 0 : a0 + 40);
    sub_10313d70(v1);
    v4 = 4294967295;
    sub_10331030(a0);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v2;
    return;
}
```

## `sub_10336520` `0x10336520`

_142 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390834;
extern char g_10390844;
extern char g_1039084c;

void sub_10336520(unsigned int idx)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4195
    unsigned long v11;  // 4199
    unsigned long v12;  // 4113
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036e8ef;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    *((char **)idx) = &g_1039084c;
    *((char **)(idx + 40)) = &g_10390844;
    *((char **)(idx + 60)) = &g_10390834;
    v4 = 1;
    v4 = 0;
    v1 = (!idx ? 0 : idx + 60);
    sub_10313bb0(v1);
    v4 = 4294967295;
    sub_10336490(idx);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v2;
    return;
}
```

## `sub_103365b0` `0x103365b0`

_148 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_103365b0(int a0)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4137
    unsigned long v13;  // 4151
    unsigned long v14;  // 4117
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036e91b;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v4 = *((int *)v12);
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v4;
    v2 = sub_10350a53(64, g_1038e180 ^ &v7);
    v6 = 0;
    v1 = (!v2 ? 0 : sub_10335350(v2, a0 - 60));
    v3 = v1;
    v6 = 4294967295;
    v0 = (!v3 ? 0 : v3 + 60);
    v14 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v14) = v4;
    return v0;
}
```

## `sub_10336650` `0x10336650`

_42 bytes. (leaf/helper — see body)_

```c
extern int g_1039d580;

int sub_10336650(int a0)
{
    char v0;  // [bp-0x44]

    sub_10335350(&v0, a0 - 60);
    return sub_103533ea(&v0, &g_1039d580);
}
```

## `sub_10336680` `0x10336680`

_132 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390890;
extern char g_10390898;

void sub_10336680(int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4188
    unsigned long v11;  // 4192
    unsigned long v12;  // 4113
    unsigned int v0;  // [bp-0x1c]
    int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036e96f;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    *((char **)a0) = &g_10390898;
    *((char **)(a0 + 40)) = &g_10390890;
    v4 = 1;
    v4 = 0;
    v1 = (!a0 ? 0 : a0 + 40);
    sub_10313d70(v1);
    v4 = 4294967295;
    sub_103311b0(a0);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v2;
    return;
}
```

## `sub_10336710` `0x10336710`

_142 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1039086c;
extern char g_1039087c;
extern char g_10390884;

void sub_10336710(unsigned int idx)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4195
    unsigned long v11;  // 4199
    unsigned long v12;  // 4113
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036e9bf;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    *((char **)idx) = &g_10390884;
    *((char **)(idx + 40)) = &g_1039087c;
    *((char **)(idx + 60)) = &g_1039086c;
    v4 = 1;
    v4 = 0;
    v1 = (!idx ? 0 : idx + 60);
    sub_10313bb0(v1);
    v4 = 4294967295;
    sub_10336680(idx);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v2;
    return;
}
```

## `sub_103367a0` `0x103367a0`

_148 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_103367a0(int a0)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4137
    unsigned long v13;  // 4151
    unsigned long v14;  // 4117
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036e9eb;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v4 = *((int *)v12);
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v4;
    v2 = sub_10350a53(64, g_1038e180 ^ &v7);
    v6 = 0;
    v1 = (!v2 ? 0 : sub_103354f0(v2, a0 - 60));
    v3 = v1;
    v6 = 4294967295;
    v0 = (!v3 ? 0 : v3 + 60);
    v14 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v14) = v4;
    return v0;
}
```

## `sub_10336840` `0x10336840`

_42 bytes. (leaf/helper — see body)_

```c
extern int g_1039d634;

int sub_10336840(int a0)
{
    char v0;  // [bp-0x44]

    sub_103354f0(&v0, a0 - 60);
    return sub_103533ea(&v0, &g_1039d634);
}
```

## `sub_10336870` `0x10336870`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10336870(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_10335b60(v0);
    if (((char)a1 & 1))
        sub_10350abd(v0);
    return v0;
}
```

## `sub_103368a0` `0x103368a0`

_78 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_103368a0(int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4140
    unsigned int v10;  // eax
    unsigned long v11;  // 4156
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v2 = 4294967295;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v10 = *((int *)v9);
    v1 = *((int *)v9);
    v0 = a0;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v1;
    v2 = 0;
    v12 = sub_103368f0(g_1038e180 ^ &v3, a0, v10, sub_1036ea1b, -1, &v4);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v10;
    return v12;
}
```

## `sub_103368f0` `0x103368f0`

_29 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_103368f0(unsigned int *a0)
{
    unsigned int *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    if (*(a0))
        a0 = sub_10336910(a0, &v1);
    return a0;
}
```

## `sub_10336910` `0x10336910`

_48 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    struct struct_0 *field_0;
    unsigned int field_4;
} struct_2;

typedef struct struct_0 {
    char padding_0[4];
    struct struct_1 *field_4;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

struct_2 * sub_10336910(struct_2 *a0)
{
    struct_2 *v3;  // eax
    struct_2 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    v3 = &a0->field_4;
    InterlockedExchangeAdd(v3, 4294967295);
    if (v3->field_0 != 1)
        return v3;
    a0->field_0->field_4(a0, &v1);
    return sub_10336940();
}
```

## `sub_10336940` `0x10336940`

_40 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    struct struct_0 *field_0;
    char padding_4[4];
    unsigned int field_8;
} struct_2;

typedef struct struct_0 {
    char padding_0[8];
    struct struct_1 *field_8;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

struct_2 * sub_10336940(struct_2 *a0)
{
    struct_2 *v3;  // eax
    struct_2 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    v3 = &a0->field_8;
    InterlockedExchangeAdd(v3, 4294967295);
    if (v3->field_0 == 1)
        v3 = a0->field_0->field_8(a0, &v1);
    return v3;
}
```

## `sub_10336970` `0x10336970`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10336970(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_10335fe0(v0);
    if (((char)a1 & 1))
        sub_10350abd(v0);
    return v0;
}
```

## `sub_103369a0` `0x103369a0`

_78 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int * sub_103369a0(unsigned int *a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4140
    unsigned long v11;  // 4156
    unsigned int *v12;  // eax
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x18]
    unsigned int *v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036ea4b;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    v4 = 0;
    v4 = 4294967295;
    v12 = sub_103368f0(v1 + 1);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_103369f0` `0x103369f0`

_167 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

int sub_103369f0(struct_0 *a0, unsigned int a1, int a2, int a3, int a4)
{
    int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    int v2;  // [bp-0x10]
    int v3;  // [bp-0x8]

    if (*((int *)&a0->padding_8[12]) < a1)
        sub_103503dd();
    if (*((int *)&a0->padding_8[12]) - a1 < a2)
        a2 = *((int *)&a0->padding_8[12]) - a1;
    v2 = (a2 < a4 ? a2 : a4);
    v3 = sub_10325d00(&sub_1031a4a0(a0)->padding_0[2 * a1], a3, v2);
    if (!v3)
    {
        v0 = (a2 < a4 ? -1 : a2 != a4);
        v1 = v0;
        return v1;
    }
    v1 = v3;
    return v1;
}
```

## `sub_10336aa0` `0x10336aa0`

_54 bytes. (leaf/helper — see body)_

```c
char * sub_10336aa0(char *a0, unsigned int a1)
{
    char *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    *(v0) = 0;
    if ((char)sub_103315c0(a1))
        sub_103314c0(v0, sub_10331570(a1));
    return v0;
}
```

## `sub_10336ae0` `0x10336ae0`

_54 bytes. (leaf/helper — see body)_

```c
char * sub_10336ae0(char *a0, unsigned int a1)
{
    char *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    *(v0) = 0;
    if ((char)sub_103315c0(a1))
        sub_10325930(v0, sub_10331570(a1));
    return v0;
}
```

## `sub_10336b20` `0x10336b20`

_16 bytes. (leaf/helper — see body)_

```c
int sub_10336b20(unsigned int *a0)
{
    return *(a0);
}
```

## `sub_10336b30` `0x10336b30`

_103 bytes. (leaf/helper — see body)_

```c
char sub_10336b30(unsigned int a0)
{
    char *v5;  // eax
    unsigned int v0;  // [bp-0x24]
    char v1;  // [bp-0x1c]
    char v2;  // [bp-0x14]
    char v3;  // [bp-0xc]

    sub_1031b790(a0, &v3);
    v5 = (unsigned int)sub_10334210(sub_103389d0(&v2, 1, a0, v0));
    if (*(v5) != 58)
    {
        sub_1031b790(a0, &v1);
        v5 = (unsigned int)sub_10334210(sub_103389d0(&v0, 1, &v2));
        if (*(v5) != 47)
            v5 = sub_103170d0(a0, 47);
    }
    return *((char *)&v5);
}
```

## `sub_10336ba0` `0x10336ba0`

_48 bytes. (leaf/helper — see body)_

```c
char sub_10336ba0(int a0, char a1)
{
    char v0;  // [bp-0x9]

    v0 = (a1 == 92 ? 47 : a1);
    return sub_103170d0(a0, v0);
}
```

## `sub_10336bd0` `0x10336bd0`

_45 bytes. (leaf/helper — see body)_

```c
char sub_10336bd0(char a0)
{
    unsigned int v1;  // ecx
    unsigned int v0;  // [bp-0x8]

    v0 = v1;
    if (a0 != 47 && a0 != 92)
        v0 = 0;
    else
        v0 = 1;
    return v0;
}
```

## `sub_10336c00` `0x10336c00`

_219 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

int sub_10336c00(struct_0 *a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    if (a1 == 2 && *((char *)sub_103189a0(a0, 0)) == 47 && *((char *)sub_103189a0(a0, 1)) == 47)
        return 0;
    if (a1 && *((char *)sub_103189a0(a0, a1 - 1)) == 47)
        return a1 - 1;
    v1 = sub_10338730(47, a1 - 1);
    if (v1 == 4294967295)
        v1 = sub_10338730(92, a1 - 1);
    if (v1 == 4294967295)
        v1 = sub_10338730(58, a1 - 2);
    if (v1 != 4294967295 && (v1 != 1 || *((char *)sub_103189a0(a0, 0)) != 47))
        v0 = v1 + 1;
    else
        v0 = 0;
    return v0;
}
```

## `sub_10336ce0` `0x10336ce0`

_246 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

unsigned int sub_10336ce0(struct_0 *a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    if (a1 > 2 && *((char *)sub_103189a0(a0, 1)) == 58 && *((char *)sub_103189a0(a0, 2)) == 47)
        return 2;
    if (a1 == 2 && *((char *)sub_103189a0(a0, 0)) == 47 && *((char *)sub_103189a0(a0, 1)) == 47)
        return 4294967295;
    if (a1 > 3 && *((char *)sub_103189a0(a0, 0)) == 47 && *((char *)sub_103189a0(a0, 1)) == 47 && *((char *)sub_103189a0(a0, 2)) != 47)
    {
        v1 = sub_10338710(47, 2);
        v0 = (v1 < a1 ? v1 : 4294967295);
        return v0;
    }
    if (a1 > 0 && *((char *)sub_103189a0(a0, 0)) == 47)
        return 0;
    return 4294967295;
}
```

## `sub_10336de0` `0x10336de0`

_231 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103908a4;

unsigned int * sub_10336de0(unsigned int *a0, int a1, int a2, int a3, int a4)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4154
    unsigned long v13;  // 4176
    int v14;  // edi
    int v15;  // esi
    int v16;  // ebx
    unsigned long v17;  // 4129
    unsigned int v0;  // [bp-0x34]
    int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x1c]
    int v3;  // [bp-0x18]
    char *v4;  // [bp-0x14], Other Possible Types: unsigned int *
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8], Other Possible Types: char
    char v8;  // [bp-0x4]

    v7 = 4294967295;
    v6 = sub_1036ea8e;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v5 = *((int *)v12);
    v4 = a0;
    v0 = g_1038e180 ^ &v8;
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v5;
    v4 = &v0;
    sub_10336ee0(a3, a4, a1, g_1038e180 ^ &v8, v14, v15, v16);
    v7 = 0;
    *(a0) = &g_103908a4;
    sub_10338a90(a3, a4, a1, g_1038e180 ^ &v8, v14, v15, v16);
    v7 = 1;
    v7 = 2;
    v2 = sub_10350a53(84);
    v7 = 3;
    v1 = (!v2 ? 0 : sub_10337ea0());
    v3 = v1;
    v7 = 2;
    sub_10339920(v3);
    sub_10336b20(a0 + 19);
    sub_10336f60(a2);
    v17 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v17) = v5;
    return a0;
}
```

## `sub_10336ea2` `0x10336ea2`

_24 bytes. (leaf/helper — see body)_

```c
extern char g_10336ec1;

int sub_10336ea2(void)
{
    unsigned int v1;  // [bp+0x100000]

    sub_10338b10();
    v1 = 1;
    return &g_10336ec1;
}
```

## `sub_10336ee0` `0x10336ee0`

_123 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103908b0;

unsigned int [12] sub_10336ee0(unsigned int *a0, unsigned int a1, unsigned int a2, int a3)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4154
    unsigned long v11;  // 4123
    unsigned int v0;  // [bp-0x18]
    unsigned int idx[12];  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036eac3;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    idx = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    idx = a0;
    sub_10314430(idx, a3);
    v4 = 0;
    idx[0] = &g_103908b0;
    idx[10] = a1;
    idx[11] = a2;
    sub_10315800(idx + 1);
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return idx;
}
```

## `sub_10336f60` `0x10336f60`

_28 bytes. (leaf/helper — see body)_

```c
int sub_10336f60(int a0, int a1)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_10319f70(v0, a1);
    return v0;
}
```

## `sub_10336f80` `0x10336f80`

_162 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern int g_1039dfb0;

unsigned int sub_10336f80(int a0)
{
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // fs
    unsigned long v13;  // 4137
    unsigned long v14;  // 4151
    unsigned int v15;  // eax
    unsigned long v16;  // 4113
    int v0;  // [bp-0xf4]
    unsigned int v1;  // [bp-0xf0]
    int v2;  // [bp-0xec]
    int v3;  // [bp-0xe8]
    char v4;  // [bp-0xe4]
    char v5;  // [bp-0x78]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]
    char v9;  // [bp-0x4]

    v8 = 4294967295;
    v7 = sub_1036eae8;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v6 = *((int *)v13);
    v1 = g_1038e180 ^ &v9;
    v14 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v14) = &v6;
    v0 = a0;
    sub_10334530();
    v3 = sub_10339990(&v5, a0);
    v2 = v3;
    v8 = 0;
    sub_103399f0(&v4, v2);
    sub_103533ea(&v4, &g_1039dfb0);
    v8 = 4294967295;
    v15 = sub_10339190(&v4, &g_1039dfb0);
    v16 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v16) = v6;
    return v15;
}
```

