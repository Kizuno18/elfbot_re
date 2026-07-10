# elfbot.dll decompiled — jiru 0x10325630..0x10327130

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10325630` `0x10325630`

_70 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b2bc;
extern struct_0 *g_1038b2dc;

unsigned int sub_10325630(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    if (a1 == 1)
    {
        v0 = g_1038b2dc(78);
        v1 = g_1038b2dc(79);
        g_1038b2bc(a0, v0 * 2, v1 * 2, 0, 0, 1);
    }
    return 0;
}
```

## `sub_10325680` `0x10325680`

_94 bytes. refs "COMCTL32.DLL", "_TrackMouseEvent"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b078;
extern struct_0 *g_1038b080;
extern struct_0 *g_1038b2b8;

unsigned int * sub_10325680(void)
{
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int *v4;  // [bp-0xc]
    unsigned int *v5;  // [bp-0x8]

    v5 = g_1038b080("COMCTL32.DLL");
    if (!v5)
        return v5;
    v4 = g_1038b078(v5, "_TrackMouseEvent");
    if (!v4)
        return v4;
    v0 = 16;
    v1 = 0x40000000;
    v2 = g_1038b2b8();
    v3 = 4294967295;
    return v4(&v0);
}
```

## `sub_103256e0` `0x103256e0`

_92 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_103256e0(int a0, int a1)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4140
    unsigned int v8;  // eax
    unsigned int v9;  // ecx
    unsigned long v10;  // 4156
    unsigned long v11;  // 4134
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v8 = *((int *)v7);
    v1 = *((int *)v7);
    v0 = v9;
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v10) = &v1;
    sub_10325a60(a0, a1, g_1038e180 ^ &v2, 0, v8, sub_1036ba29, -1, &v3);
    v11 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v11) = v8;
    return a0;
}
```

## `sub_10325740` `0x10325740`

_92 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10325740(int a0, int a1)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4135
    unsigned int v9;  // eax
    unsigned long v10;  // 4151
    unsigned long v11;  // 4120
    int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v9 = *((int *)v8);
    v1 = *((int *)v8);
    v0 = a0;
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v10) = &v1;
    sub_103257a0(g_1038e180 ^ &v3, a0, v9, sub_1036ba58, -1, &v4);
    v2 = 0;
    sub_103258e0(a1);
    v11 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v11) = v9;
    return a0;
}
```

## `sub_103257a0` `0x103257a0`

_44 bytes. (leaf/helper — see body)_

```c
int sub_103257a0(unsigned int a0)
{
    unsigned int v0;  // [bp-0x10]

    v0 = a0;
    sub_1031a280(&v0);
    sub_103147d0(a0);
    sub_1031a3c0(a0, 0, 0);
    return a0;
}
```

## `sub_103257d0` `0x103257d0`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

void sub_103257d0(int a0)
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
    v3 = sub_1036ba88;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    v4 = 0;
    v4 = 4294967295;
    sub_1031a3a0(v1);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v2;
    return;
}
```

## `sub_10325820` `0x10325820`

_84 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10325820(int a0, int a1)
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
    sub_103301d0(a1, g_1038e180 ^ &v2, a0, v8, sub_1036bab8, -1, &v3);
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v10) = v8;
    return a0;
}
```

## `sub_10325880` `0x10325880`

_84 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10325880(int a0, int a1)
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
    sub_10325900(a1, g_1038e180 ^ &v2, a0, v8, sub_1036bae8, -1, &v3);
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v10) = v8;
    return a0;
}
```

## `sub_103258e0` `0x103258e0`

_30 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

int sub_103258e0(unsigned int a0, struct_0 *a1)
{
    unsigned int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_103259c0(sub_1031fc50(a1));
}
```

## `sub_10325900` `0x10325900`

_34 bytes. (leaf/helper — see body)_

```c
char * sub_10325900(char *a0, int a1)
{
    char *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    *(a0) = 0;
    sub_10325930(a1, a0, &v1);
    return a0;
}
```

## `sub_10325930` `0x10325930`

_144 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

char * sub_10325930(char *a0, int a1)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4139
    unsigned long v12;  // 4153
    unsigned long v13;  // 4129
    unsigned int v0;  // [bp-0x28]
    int v1;  // [bp-0x24], Other Possible Types: unsigned int
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036bb21;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v0 = g_1038e180 ^ &v7;
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    v2 = sub_1031a280(a0 + 4);
    v3 = sub_1031acf0(28, v2);
    v6 = 0;
    if (v3)
        v1 = sub_1031e760(v3, a1);
    else
        v1 = 0;
    *(a0) = 1;
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v13) = v4;
    return a0;
}
```

## `sub_103259c0` `0x103259c0`

_153 bytes. (leaf/helper — see body)_

```c
int sub_103259c0(int a0, unsigned short *iter)
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
        if (!(char)sub_103260f0(v2))
            sub_10325f00();
    }
    for (; *(iter); iter += 1)
    {
        sub_103260b0(_INSERT(iter, 0, *(iter)));
    }
    return a0;
}
```

## `sub_10325a60` `0x10325a60`

_148 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10325a60(int a0, unsigned int a1)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4140
    unsigned long v12;  // 4157
    unsigned long v13;  // 4118
    unsigned int v0;  // [bp-0x38]
    char v1;  // [bp-0x34]
    int v2;  // [bp-0x18]
    int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    char v6;  // [bp-0x8], Other Possible Types: unsigned int
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036bb61;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v2 = g_1038e180 ^ &v7;
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    sub_10325d80(&v1, v2, 0);
    v6 = 1;
    v3 = sub_10325b00(46, -1);
    sub_10325b20(a0, 0, v3);
    v0 = 1;
    v6 = 0;
    sub_1031a3a0(&v1);
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v13) = v4;
    return sub_10351225();
}
```

## `sub_10325b00` `0x10325b00`

_31 bytes. (leaf/helper — see body)_

```c
int sub_10325b00(int a0, char a1, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10325c00(&/* unsupported instruction */, a1, 1, a0, &v1);
}
```

## `sub_10325b20` `0x10325b20`

_103 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10325b20(int a0, unsigned int a1, int a2, int a3)
{
    unsigned long v3;  // ldt
    unsigned long v4;  // gdt
    unsigned short v5;  // fs
    unsigned long v6;  // 4146
    unsigned int v7;  // eax
    unsigned long v8;  // 4160
    unsigned long v9;  // 4131
    unsigned int v0;  // [bp-0x10]
    char v1;  // [bp-0x4]
    char v2;  // [bp+0x0]

    v6 = _ccall(v3, v4, (unsigned int)v5, 0);
    v7 = *((int *)v6);
    v0 = *((int *)v6);
    v8 = _ccall(v3, v4, (unsigned int)v5, 0);
    *((unsigned int **)v8) = &v0;
    sub_10325b90(a0, a2, a3, g_1038e180 ^ &v1, a0, 0, v7, sub_1036bba9, -1, &v2);
    v9 = _ccall(v3, v4, (unsigned int)v5, 0);
    *((unsigned int *)v9) = v7;
    return a1;
}
```

## `sub_10325b90` `0x10325b90`

_66 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

int sub_10325b90(unsigned int a0, struct_0 *a1, int a2, unsigned int a3)
{
    unsigned int v0;  // [bp-0x10]

    v0 = a0;
    sub_1031a280(&v0);
    sub_103147d0(a0);
    sub_1031a3c0(a0, 0, 0);
    sub_1031e7a0(a0, a1, a2, a3);
    return a0;
}
```

## `sub_10325be0` `0x10325be0`

_25 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

int sub_10325be0(struct_0 *a0)
{
    return _INSERT(a0, 0, !a0->field_14);
}
```

## `sub_10325c00` `0x10325c00`

_220 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

int sub_10325c00(struct_0 *a0, int a1, int a2, int a3)
{
    int v0;  // [bp-0x14]
    int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0x8]

    if (!a3)
    {
        v1 = (a2 < *((int *)&a0->padding_8[12]) ? a2 : *((int *)&a0->padding_8[12]));
        return v1;
    }
    if (a3 > *((int *)&a0->padding_8[12]))
        return -1;
    v0 = (a2 < *((int *)&a0->padding_8[12]) - a3 ? a2 : *((int *)&a0->padding_8[12]) - a3);
    v2 = &sub_1031a4a0(a0)->padding_0[2 * v0];
    while (true)
    {
        if ((char)sub_10325ce0(v2, a1) && !sub_10325d00(v2, a1, a3))
            return v2 - (char *)sub_1031a4a0(a0) >> 1;
        if (v2 == sub_1031a4a0(a0))
            break;
        v2 -= 2;
    }
    return -1;
}
```

## `sub_10325cc2` `0x10325cc2`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10325cc2(void)
{
}
```

## `sub_10325ce0` `0x10325ce0`

_26 bytes. (leaf/helper — see body)_

```c
int sub_10325ce0(unsigned short *a0, unsigned short *a1)
{
    unsigned int v0;  // eax

    v0 = *(a1);
    return _INSERT(v0, 0, *(a0) == v0);
}
```

## `sub_10325d00` `0x10325d00`

_25 bytes. (leaf/helper — see body)_

```c
int sub_10325d00(int a0, int a1, int a2)
{
    char v0;  // [bp+0x0]

    return sub_10325d20(a0, a1, a2, &v0);
}
```

## `sub_10325d20` `0x10325d20`

_85 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10325d20(unsigned short *a0, unsigned short *a1, unsigned int i)
{
    for (; i > 0; i -= 1)
    {
        if (*(a0) != *(a1))
            return (*(a0) >= *(a1)) * 2 - 1;
        a0 += 1;
        a1 += 1;
    }
    return 0;
}
```

## `sub_10325d80` `0x10325d80`

_327 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10325d80(unsigned int a0, unsigned int a1)
{
    unsigned long v15;  // ldt
    unsigned long v16;  // gdt
    unsigned short v17;  // fs
    unsigned long v18;  // 4137
    unsigned long v19;  // 4151
    unsigned long v20;  // 4117
    unsigned int v0;  // [bp-0x70]
    int v1;  // [bp-0x6c]
    int v2;  // [bp-0x68]
    int v3;  // [bp-0x64]
    int v4;  // [bp-0x60]
    int v5;  // [bp-0x5c]
    unsigned int v6;  // [bp-0x54]
    char v7;  // [bp-0x50]
    char v8;  // [bp-0x34]
    int v9;  // [bp-0x18]
    int v10;  // [bp-0x14]
    unsigned int v11;  // [bp-0x10]
    unsigned int v12;  // [bp-0xc]
    unsigned int v13;  // [bp-0x8]
    char v14;  // [bp-0x4]

    v13 = 4294967295;
    v12 = sub_1036bc1b;
    v18 = _ccall(v15, v16, (unsigned int)v17, 0);
    v11 = *((int *)v18);
    v0 = g_1038e180 ^ &v14;
    v19 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int **)v19) = &v11;
    v6 = 0;
    v10 = sub_103263d0(a0, sub_1031e920(a0));
    if (sub_1031e920(a0) && v10 && *((short *)sub_10325ed0(v10)) == 47 && (char)sub_103264b0(a0, v10))
    {
        v5 = sub_10326120(1, 46);
        v4 = v5;
        v13 = 1;
        v6 |= 1;
        v3 = v4;
    }
    else
    {
        v2 = sub_10325b20(a0, &v7, v10, -1);
        v1 = v2;
        v13 = 2;
        v6 |= 2;
        v3 = v1;
    }
    v9 = v3;
    sub_1031e760(a1, v9);
    v6 |= 4;
    v13 = 1;
    if (((char)v6 & 2))
    {
        v6 &= 4294967293;
        sub_1031a3a0(&v7);
    }
    v13 = 0;
    if (((char)v6 & 1))
    {
        v6 &= 4294967294;
        sub_1031a3a0(&v8);
    }
    v20 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int *)v20) = v11;
    return a1;
}
```

## `sub_10325ed0` `0x10325ed0`

_43 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

int sub_10325ed0(struct_0 *a0, unsigned int a1)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    if (a1 > a0->field_14)
        sub_10353616(a0, &v1);
    return &sub_1031a4a0(a0)->padding_0[2 * a1];
}
```

## `sub_10325f00` `0x10325f00`

_103 bytes. (leaf/helper — see body)_

```c
void sub_10325f00(int a0)
{
    char v0;  // [bp-0x24]
    char v1;  // [bp-0x1c]
    char v2;  // [bp-0x14]
    char v3;  // [bp-0xc]

    sub_10326160(&v3, &v2, 1, a0);
    sub_103261b0(&v3, &v2, 1, a0);
    if (*((short *)sub_10326190()) == 58)
        return;
    sub_10326160(&v1, &v0, 1);
    sub_103261b0(&v1, &v0, 1);
    if (*((short *)sub_10326190()) == 47)
        return;
    sub_10325f70(47);
    return;
}
```

## `sub_10325f70` `0x10325f70`

_28 bytes. (leaf/helper — see body)_

```c
short sub_10325f70(int a0, unsigned short a1)
{
    int v2;  // eax
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    v2 = _INSERT(0, 0, a1);
    return sub_10325f90(1, v2, a0, &v1);
}
```

## `sub_10325f90` `0x10325f90`

_112 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    int field_14;
} struct_0;

struct_0 * sub_10325f90(struct_0 *a0, int a1, unsigned short a2)
{
    char v1;  // al
    int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (4294967295 - a0->field_14 <= a1)
    {
        sub_1035039e(a0);
    }
    else if (a1 > 0)
    {
        v0 = a0->field_14 + a1;
        v1 = sub_1031e940(a0, v0, 0);
        if (!v1)
            return a0;
        v2 = _INSERT(v1, 0, a2);
        sub_10326000(a0->field_14, a1, v2);
        sub_1031a440(a0, v0);
        return a0;
    }
    else
    {
        return a0;
    }
}
```

## `sub_10326000` `0x10326000`

_80 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

unsigned short * sub_10326000(struct_0 *a0, unsigned int a1, unsigned int a2)
{
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    struct_0 *v2;  // [bp-0x8]
    unsigned short v3;  // [bp+0xc]

    v2 = a0;
    v2 = a0;
    if (a2 != 1)
    {
        *((unsigned short *)&v1) = v3;
        v0 = a2;
        return sub_10326050(&sub_1031a4a0(v2)->padding_0[2 * a1]);
    }
    return sub_1031a480(&sub_1031a4a0(v2)->padding_0[2 * a1], &v3);
}
```

## `sub_10326050` `0x10326050`

_26 bytes. (leaf/helper — see body)_

```c
int sub_10326050(int a0, int a1, unsigned short a2)
{
    int v1;  // ecx
    char v0;  // [bp+0x0]

    v1 = _INSERT(0, 0, a2);
    return sub_10326070(a0, v1, a1, &v0);
}
```

## `sub_10326070` `0x10326070`

_55 bytes. (leaf/helper — see body)_

```c
unsigned short * sub_10326070(unsigned short *a0, unsigned short a1, unsigned int i)
{
    unsigned int v1;  // ecx
    unsigned short *iter;  // [bp-0x8], Other Possible Types: unsigned int

    iter = v1;
    for (iter = a0; i > 0; i -= 1)
    {
        *(iter) = a1;
        iter += 1;
    }
    return a0;
}
```

## `sub_103260b0` `0x103260b0`

_53 bytes. (leaf/helper — see body)_

```c
short sub_103260b0(int a0, unsigned short a1)
{
    unsigned short v0;  // [bp-0xa]

    v0 = (a1 == 92 ? 47 : a1);
    return sub_10325f70(a0, v0);
}
```

## `sub_103260f0` `0x103260f0`

_45 bytes. (leaf/helper — see body)_

```c
char sub_103260f0(unsigned short a0)
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

## `sub_10326120` `0x10326120`

_63 bytes. (leaf/helper — see body)_

```c
int sub_10326120(unsigned int a0, int a1, unsigned short a2)
{
    unsigned int v0;  // [bp-0x10]

    v0 = a0;
    sub_1031a280(&v0);
    sub_103147d0(a0);
    sub_103261f0(a1, _INSERT(sub_1031a3c0(a0, 0, 0), 0, a2));
    return a0;
}
```

## `sub_10326160` `0x10326160`

_46 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

int sub_10326160(struct_0 *a0, unsigned int a1)
{
    struct_0 *v2;  // eax
    struct_0 *v0;  // [bp-0xc]
    struct_0 *v1;  // [bp-0x8]

    v1 = a0;
    v1 = a0;
    v0 = v1;
    v2 = sub_1031a4a0(v1);
    sub_10326240(&v2->padding_0[2 * *((int *)&v1->padding_8[12])]);
    return a1;
}
```

## `sub_10326190` `0x10326190`

_19 bytes. (leaf/helper — see body)_

```c
void sub_10326190(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10326280(a0, &v1);
    return;
}
```

## `sub_103261b0` `0x103261b0`

_57 bytes. (leaf/helper — see body)_

```c
unsigned int [2] sub_103261b0(int *a0, unsigned int *a1, int a2)
{
    unsigned int v1[2];  // eax
    unsigned int v2;  // edx
    char v0;  // [bp+0x0]

    v1 = sub_10326260(a2, a0, *(a0), a0[1], &v0);
    v2 = v1[1];
    *(a1) = v1[0];
    a1[1] = v2;
    return a1;
}
```

## `sub_103261f0` `0x103261f0`

_79 bytes. (leaf/helper — see body)_

```c
int sub_103261f0(unsigned int a0, unsigned int a1, unsigned short a2)
{
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]
    char v2;  // [bp+0x0]

    v1 = a0;
    if (a1 == 4294967295)
        sub_1035039e(a0, &v2);
    if (!(char)sub_1031e940(a0, a1, 0))
        return a0;
    *((unsigned short *)&v0) = a2;
    sub_10326000(a0, 0, a1);
    sub_1031a440(a0, a1);
    return a0;
}
```

## `sub_10326240` `0x10326240`

_32 bytes. (leaf/helper — see body)_

```c
int sub_10326240(int a0, int a1, int a2)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_103262f0(a1, a2, a0, &v1);
    return a0;
}
```

## `sub_10326260` `0x10326260`

_27 bytes. (leaf/helper — see body)_

```c
int sub_10326260(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_103262d0(-(a1), a0, &v1);
}
```

## `sub_10326280` `0x10326280`

_72 bytes. (leaf/helper — see body)_

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

int sub_10326280(struct_0 *a0)
{
    struct_0 *v2;  // eax
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    if (v0->field_0 != 0xfffffffe)
    {
        if (!v0->field_0)
            sub_10353616();
        v2 = sub_1031a4a0(v0->field_0);
        if (v0->field_4 >= (char *)v2 + 2 * *((int *)&v0->field_0->padding_8[12]))
            sub_10353616();
    }
    return v0->field_4;
}
```

## `sub_103262d0` `0x103262d0`

_28 bytes. (leaf/helper — see body)_

```c
int sub_103262d0(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10326350(a1, a0, &v1);
    return a0;
}
```

## `sub_103262f0` `0x103262f0`

_93 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

struct struct_0 *[2] sub_103262f0(struct_0 **a0, struct_0 *a1, struct_0 *a2)
{
    struct_0 *v2;  // eax
    struct struct_0 *v0[2];  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10341910(a0, &v1);
    if (!a2 || !a1 || sub_1031a4a0(a2) > a1 || (v2 = (struct_0 *)sub_1031a4a0(a2), a1 > sub_1031a4a0(a2) + *((int *)&a2->padding_8[12]) * 2))
        sub_10353616();
    *(a0) = a2;
    a0[1] = a1;
    return a0;
}
```

## `sub_10326350` `0x10326350`

_125 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
    unsigned int field_4;
} struct_1;

typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

struct_1 * sub_10326350(struct_1 *a0, unsigned int a1)
{
    struct_0 *v1;  // eax
    struct_0 *v2;  // eax
    struct_1 *idx;  // [bp-0x8]

    idx = a0;
    idx = a0;
    if (idx->field_0 != 0xfffffffe)
    {
        if (!idx->field_0)
            sub_10353616();
        v1 = sub_1031a4a0(idx->field_0);
        if (idx->field_4 + a1 * 2 > &v1->padding_0[2 * idx->field_0->field_14] || (v2 = (struct_0 *)sub_1031a4a0(idx->field_0), idx->field_4 + a1 * 2 < sub_1031a4a0(idx->field_0)))
            sub_10353616();
    }
    idx->field_4 = idx->field_4 + a1 * 2;
    return idx;
}
```

## `sub_103263d0` `0x103263d0`

_219 bytes. (leaf/helper — see body)_

```c
int sub_103263d0(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    if (a1 == 2 && *((short *)sub_10325ed0(a0, 0)) == 47 && *((short *)sub_10325ed0(a0, 1)) == 47)
        return 0;
    if (a1 && *((short *)sub_10325ed0(a0, a1 - 1)) == 47)
        return a1 - 1;
    v1 = sub_10325b00(a0, 47, a1 - 1);
    if (v1 == 4294967295)
        v1 = sub_10325b00(a0, 92, a1 - 1);
    if (v1 == 4294967295)
        v1 = sub_10325b00(a0, 58, a1 - 2);
    if (v1 != 4294967295 && (v1 != 1 || *((short *)sub_10325ed0(a0, 0)) != 47))
        v0 = v1 + 1;
    else
        v0 = 0;
    return v0;
}
```

## `sub_103264b0` `0x103264b0`

_138 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

char sub_103264b0(struct_0 *a0, unsigned int i)
{
    unsigned int v1;  // ecx
    unsigned int v0;  // [bp-0x8]

    for (v0 = v1; i > 0 && *((short *)sub_10325ed0(a0, i - 1)) == 47; i -= 1);
    if (i && (i <= 2 || *((short *)sub_10325ed0(a0, 1)) != 47 || sub_10326540(47, 2) != i) && (i != 2 || *((short *)sub_10325ed0(a0, 1)) != 58))
        v0 = 1;
    else
        v0 = 0;
    return v0;
}
```

## `sub_10326540` `0x10326540`

_31 bytes. (leaf/helper — see body)_

```c
int sub_10326540(int a0, char a1, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10326560(&/* unsupported instruction */, a1, 1, a0, &v1);
}
```

## `sub_10326560` `0x10326560`

_217 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

int sub_10326560(struct_0 *a0, int a1, int a2, int a3)
{
    int v0;  // [bp-0x10]
    int v1;  // [bp-0xc]
    int iter;  // [bp-0x8]

    if (!a3 && a2 <= *((int *)&a0->padding_8[12]))
        return a2;
    if (a2 >= *((int *)&a0->padding_8[12]))
        return -1;
    iter = *((int *)&a0->padding_8[12]) - a2;
    if (a3 <= iter)
    {
        iter -= a3 - 1;
        v0 = &sub_1031a4a0(a0)->padding_0[2 * a2];
        while (true)
        {
            v1 = sub_10326640(v0, iter, a1);
            if (!v1)
                break;
            if (!sub_10325d00(v1, a1, a3))
                return v1 - (char *)sub_1031a4a0(a0) >> 1;
            iter -= (v1 - v0 >> 1) + 1;
            v0 = v1 + 2;
        }
    }
    return -1;
}
```

## `sub_10326640` `0x10326640`

_28 bytes. (leaf/helper — see body)_

```c
int sub_10326640(int a0, int a1, unsigned short *a2)
{
    int v1;  // edx
    char v0;  // [bp+0x0]

    v1 = _INSERT(0, 0, *(a2));
    return sub_10326660(a0, v1, a1, &v0);
}
```

## `sub_10326660` `0x10326660`

_54 bytes. (leaf/helper — see body)_

```c
unsigned short * sub_10326660(unsigned short *a0, unsigned short a1, unsigned int i)
{
    for (; i > 0; i -= 1)
    {
        if (*(a0) == a1)
            return a0;
        a0 += 1;
    }
    return NULL;
}
```

## `sub_103266a0` `0x103266a0`

_197 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b044;
extern unsigned int g_1038e180;

int sub_103266a0(int a0, unsigned int a1)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4136
    unsigned long v12;  // 4150
    unsigned long v13;  // 4120
    int v0;  // [bp-0x3c]
    int v1;  // [bp-0x38]
    char v2;  // [bp-0x30]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8], Other Possible Types: char
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036bc66;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    sub_1032df20(g_1038e180 ^ &v7);
    v6 = 0;
    sub_10319ff0(a0 + 32);
    v6 = 1;
    sub_1031a090(a0 + 64);
    v6 = 2;
    if (g_1038b044(a1, 1))
    {
        v3 = a1;
        sub_10333e10(&v3);
    }
    else
    {
        v1 = sub_10314590(&v2, a1);
        v0 = v1;
        v6 = 3;
        sub_10333e30(v0);
        v6 = 2;
        sub_10314610(&v2);
    }
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v13) = v4;
    return a0;
}
```

## `sub_10326770` `0x10326770`

_197 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b044;
extern unsigned int g_1038e180;

int sub_10326770(int a0, unsigned int a1)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4136
    unsigned long v12;  // 4150
    unsigned long v13;  // 4120
    int v0;  // [bp-0x3c]
    int v1;  // [bp-0x38]
    char v2;  // [bp-0x30]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8], Other Possible Types: char
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036bca7;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    sub_1032df20(g_1038e180 ^ &v7);
    v6 = 0;
    sub_10319ff0(a0 + 32);
    v6 = 1;
    sub_1031a090(a0 + 64);
    v6 = 2;
    if (g_1038b044(a1, 2))
    {
        v3 = a1;
        sub_10333e10(&v3);
    }
    else
    {
        v1 = sub_1031fc10(&v2, a1);
        v0 = v1;
        v6 = 3;
        sub_10333e50(v0);
        v6 = 2;
        sub_1031a3a0(&v2);
    }
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v13) = v4;
    return a0;
}
```

## `sub_10326840` `0x10326840`

_162 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10326840(int a0, unsigned int a1)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4136
    unsigned long v9;  // 4150
    unsigned long v11;  // 4120
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    char v3;  // [bp-0x8], Other Possible Types: unsigned int
    char v4;  // [bp-0x4]

    v3 = 4294967295;
    v2 = sub_1036bce0;
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v1 = *((int *)v8);
    v9 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v9) = &v1;
    sub_1032df20(g_1038e180 ^ &v4, a0);
    v3 = 0;
    sub_10319ff0(a0 + 32);
    v3 = 1;
    sub_1031a090(a0 + 64);
    v3 = 2;
    if (sub_1032e0a0())
    {
        sub_10333e30(sub_1032e0e0());
    }
    else
    {
        v0 = 0;
        sub_10333e10(&v0);
    }
    v11 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v11) = v1;
    return a0;
}
```

## `sub_103268f0` `0x103268f0`

_162 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_103268f0(int a0, unsigned int a1)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4136
    unsigned long v9;  // 4150
    unsigned long v11;  // 4120
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    char v3;  // [bp-0x8], Other Possible Types: unsigned int
    char v4;  // [bp-0x4]

    v3 = 4294967295;
    v2 = sub_1036bd19;
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v1 = *((int *)v8);
    v9 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v9) = &v1;
    sub_1032df20(g_1038e180 ^ &v4, a0);
    v3 = 0;
    sub_10319ff0(a0 + 32);
    v3 = 1;
    sub_1031a090(a0 + 64);
    v3 = 2;
    if (sub_1032e0a0())
    {
        sub_10333e50(sub_1032e0e0());
    }
    else
    {
        v0 = 0;
        sub_10333e10(&v0);
    }
    v11 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v11) = v1;
    return a0;
}
```

## `sub_103269a0` `0x103269a0`

_201 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_103269a0(int a0, unsigned int a1)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4136
    unsigned long v12;  // 4150
    unsigned long v13;  // 4120
    int v0;  // [bp-0x3c]
    int v1;  // [bp-0x38]
    unsigned int v2;  // [bp-0x30]
    char v3;  // [bp-0x2c]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8], Other Possible Types: char
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036bd5a;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    sub_1032df20(g_1038e180 ^ &v7);
    v6 = 0;
    sub_10319ff0(a0 + 32);
    v6 = 1;
    sub_1031a090(a0 + 64);
    v6 = 2;
    if (sub_1032e0a0())
    {
        sub_103301b0(&v3);
        v1 = sub_10332ed0(&v3);
        v0 = v1;
        v6 = 3;
        sub_10333e50(v0);
        v6 = 2;
        sub_1031a3a0(&v3);
    }
    else
    {
        v2 = 0;
        sub_10333e10(&v2);
    }
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v13) = v4;
    return a0;
}
```

## `sub_10326a70` `0x10326a70`

_436 bytes. refs "Can't convert invalid pointer to string"_

```c
extern unsigned int g_1038e180;
extern int g_1039c4cc;
extern int g_103a2b3c;

int sub_10326a70(int a0, int a1)
{
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    unsigned short v14;  // fs
    unsigned long v15;  // 4139
    unsigned long v16;  // 4153
    int v18;  // eax
    unsigned long v20;  // 4113
    int v0;  // [bp-0x90]
    int v1;  // [bp-0x8c]
    unsigned int v2;  // [bp-0x84]
    char v3;  // [bp-0x80]
    char v4;  // [bp-0x64]
    char v5;  // [bp-0x3c]
    int v6;  // [bp-0x20]
    int v7;  // [bp-0x1c]
    unsigned int v8;  // [bp-0x10]
    unsigned int v9;  // [bp-0xc]
    unsigned int v10;  // [bp-0x8], Other Possible Types: char
    char v11;  // [bp-0x4]

    v10 = 4294967295;
    v9 = sub_1036bda6;
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    v8 = *((int *)v15);
    v16 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v16) = &v8;
    v2 = 0;
    sub_1032dc70(&g_103a2b3c, g_1038e180 ^ &v11);
    v10 = 1;
    if (sub_1032e0a0(&g_103a2b3c, g_1038e180 ^ &v11))
    {
        sub_103145d0(a1, sub_1032e0e0());
        v2 |= 1;
        v10 = 0;
        sub_1032dca0(&g_103a2b3c);
        v18 = a1;
    }
    else
    {
        v6 = sub_10333e70(a0);
        if (v6)
        {
            sub_103145d0(a1, v6);
            v2 |= 1;
            v10 = 0;
            sub_1032dca0(&g_103a2b3c);
            v18 = a1;
        }
        else
        {
            v7 = sub_10333e90(a0);
            if (v7)
            {
                v1 = sub_10327660(&v5, v7);
                v0 = v1;
                v10 = 2;
                sub_1032e080(v0);
                v10 = 1;
                sub_10314610(&v5);
                sub_103145d0(a1, sub_1032e0e0());
                v2 |= 1;
                v10 = 0;
                sub_1032dca0(v0);
                v18 = a1;
            }
            else
            {
                sub_10314590(&v3, "Can't convert invalid pointer to string");
                v10 = 3;
                sub_1032d470(&v3);
                sub_103533ea(&v4, &g_1039c4cc);
                v10 = 1;
                sub_10314610(&v3);
                v10 = 0;
                v18 = sub_1032dca0();
            }
        }
    }
    v20 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int *)v20) = v8;
    return v18;
}
```

## `sub_10326c30` `0x10326c30`

_436 bytes. refs "Can't convert invalid pointer to string"_

```c
extern unsigned int g_1038e180;
extern int g_1039c4cc;
extern int g_103a2b3c;

unsigned int sub_10326c30(int a0, unsigned int a1)
{
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    unsigned short v14;  // fs
    unsigned long v15;  // 4139
    unsigned long v16;  // 4153
    unsigned int v18;  // eax
    unsigned long v20;  // 4113
    int v0;  // [bp-0x90]
    int v1;  // [bp-0x8c]
    unsigned int v2;  // [bp-0x84]
    char v3;  // [bp-0x80]
    char v4;  // [bp-0x64]
    char v5;  // [bp-0x3c]
    int v6;  // [bp-0x20]
    int v7;  // [bp-0x1c]
    unsigned int v8;  // [bp-0x10]
    unsigned int v9;  // [bp-0xc]
    unsigned int v10;  // [bp-0x8], Other Possible Types: char
    char v11;  // [bp-0x4]

    v10 = 4294967295;
    v9 = sub_1036bdf5;
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    v8 = *((int *)v15);
    v16 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v16) = &v8;
    v2 = 0;
    sub_1032dc70(&g_103a2b3c, g_1038e180 ^ &v11);
    v10 = 1;
    if (sub_1032e0a0(&g_103a2b3c, g_1038e180 ^ &v11))
    {
        sub_1031e760(a1, sub_1032e0e0());
        v2 |= 1;
        v10 = 0;
        sub_1032dca0(&g_103a2b3c);
        v18 = a1;
    }
    else
    {
        v6 = sub_10333e90(a0);
        if (v6)
        {
            sub_1031e760(a1, v6);
            v2 |= 1;
            v10 = 0;
            sub_1032dca0(&g_103a2b3c);
            v18 = a1;
        }
        else
        {
            v7 = sub_10333e70(a0);
            if (v7)
            {
                v1 = sub_10327750(&v5, v7);
                v0 = v1;
                v10 = 2;
                sub_1032e0c0(v0);
                v10 = 1;
                sub_1031a3a0(&v5);
                sub_1031e760(a1, sub_1032e0e0());
                v2 |= 1;
                v10 = 0;
                sub_1032dca0(v0);
                v18 = a1;
            }
            else
            {
                sub_10314590(&v3, "Can't convert invalid pointer to string");
                v10 = 3;
                sub_1032d470(&v3);
                sub_103533ea(&v4, &g_1039c4cc);
                v10 = 1;
                sub_10314610(&v3);
                v10 = 0;
                v18 = sub_1032dca0();
            }
        }
    }
    v20 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int *)v20) = v8;
    return v18;
}
```

## `sub_10326df0` `0x10326df0`

_128 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10326df0(int a0, int a1)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4140
    unsigned long v13;  // 4154
    unsigned long v14;  // 4117
    unsigned int v0;  // [bp-0x40]
    unsigned int v1;  // [bp-0x3c]
    unsigned int v2;  // [bp-0x38]
    unsigned int v3;  // [bp-0x30]
    char v4;  // [bp-0x2c]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    char v7;  // [bp-0x8], Other Possible Types: unsigned int
    char v8;  // [bp-0x4]

    v7 = 4294967295;
    v6 = sub_1036be34;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v5 = *((int *)v12);
    v0 = g_1038e180 ^ &v8;
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v5;
    v3 = 0;
    v2 = sub_10326c30(a0, &v4);
    v1 = v2;
    v7 = 1;
    sub_10325740(a1, v1);
    v3 |= 1;
    v7 = 0;
    sub_1031a3a0(&v4);
    v14 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v14) = v5;
    return a1;
}
```

## `sub_10326e70` `0x10326e70`

_342 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern int g_103a2b3c;

int sub_10326e70(int a0)
{
    unsigned long v14;  // ldt
    unsigned long v15;  // gdt
    unsigned short v16;  // fs
    unsigned long v17;  // 4138
    unsigned long v18;  // 4152
    unsigned int v19;  // eax
    unsigned long v20;  // 4113
    int v0;  // [bp-0x58]
    int v1;  // [bp-0x54]
    unsigned int v2;  // [bp-0x4c]
    unsigned int v3;  // [bp-0x48]
    char v4;  // [bp-0x44]
    unsigned int v5;  // [bp-0x28]
    unsigned int v6;  // [bp-0x24]
    int v7;  // [bp-0x20]
    int v8;  // [bp-0x1c]
    unsigned int v9;  // [bp-0x10]
    unsigned int v10;  // [bp-0xc]
    char v11;  // [bp-0x8], Other Possible Types: unsigned int
    char v12;  // [bp-0x4]

    v11 = 4294967295;
    v10 = sub_1036be5f;
    v17 = _ccall(v14, v15, (unsigned int)v16, 0);
    v9 = *((int *)v17);
    v18 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int **)v18) = &v9;
    sub_1032dc70(&g_103a2b3c, g_1038e180 ^ &v12);
    v11 = 0;
    if (sub_1032e0a0(&g_103a2b3c, g_1038e180 ^ &v12))
    {
        v6 = (unsigned int)sub_102ec9a0(sub_103301b0());
        v11 = 4294967295;
        sub_1032dca0();
        v19 = v6;
    }
    else
    {
        v7 = sub_10333e70(a0);
        if (v7)
        {
            v5 = (unsigned int)sub_102ec9a0(v7);
            v11 = 4294967295;
            sub_1032dca0();
            v19 = v5;
        }
        else
        {
            v8 = sub_10333e90(a0);
            if (v8)
            {
                v1 = sub_10327660(&v4, v8);
                v0 = v1;
                v11 = 1;
                sub_1032e080(v0);
                v11 = 0;
                sub_10314610(&v4);
                v3 = (unsigned int)sub_102ec9a0(sub_103301b0());
                v11 = 4294967295;
                sub_1032dca0();
                v19 = v3;
            }
            else
            {
                v2 = *((int *)sub_10333eb0(a0));
                v11 = 4294967295;
                sub_1032dca0();
                v19 = v2;
            }
        }
    }
    v20 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int *)v20) = v9;
    return v19;
}
```

## `sub_10326fd0` `0x10326fd0`

_342 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

extern unsigned int g_1038e180;
extern int g_103a2b3c;

struct_0 * sub_10326fd0(int a0)
{
    unsigned long v14;  // ldt
    unsigned long v15;  // gdt
    unsigned short v16;  // fs
    unsigned long v17;  // 4138
    unsigned long v18;  // 4152
    struct_0 *v19;  // eax
    unsigned long v20;  // 4113
    int v0;  // [bp-0x58]
    int v1;  // [bp-0x54]
    struct_0 *v2;  // [bp-0x4c]
    struct_0 *v3;  // [bp-0x48]
    char v4;  // [bp-0x44]
    struct_0 *v5;  // [bp-0x28]
    struct_0 *v6;  // [bp-0x24]
    struct_0 *v7;  // [bp-0x20]
    int v8;  // [bp-0x1c]
    unsigned int v9;  // [bp-0x10]
    unsigned int v10;  // [bp-0xc]
    char v11;  // [bp-0x8], Other Possible Types: unsigned int
    char v12;  // [bp-0x4]

    v11 = 4294967295;
    v10 = sub_1036be8a;
    v17 = _ccall(v14, v15, (unsigned int)v16, 0);
    v9 = *((int *)v17);
    v18 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int **)v18) = &v9;
    sub_1032dc70(&g_103a2b3c, g_1038e180 ^ &v12);
    v11 = 0;
    if (sub_1032e0a0(&g_103a2b3c, g_1038e180 ^ &v12))
    {
        v6 = sub_1031fc50(sub_103301b0());
        v11 = 4294967295;
        sub_1032dca0();
        v19 = v6;
    }
    else
    {
        v7 = sub_10333e90(a0);
        if (v7)
        {
            v5 = sub_1031fc50(v7);
            v11 = 4294967295;
            sub_1032dca0();
            v19 = v5;
        }
        else
        {
            v8 = sub_10333e70(a0);
            if (v8)
            {
                v1 = sub_10327750(&v4, v8);
                v0 = v1;
                v11 = 1;
                sub_1032e0c0(v0);
                v11 = 0;
                sub_1031a3a0(&v4);
                v3 = sub_1031fc50(sub_103301b0());
                v11 = 4294967295;
                sub_1032dca0();
                v19 = v3;
            }
            else
            {
                v2 = *((int *)sub_10333eb0(a0));
                v11 = 4294967295;
                sub_1032dca0();
                v19 = v2;
            }
        }
    }
    v20 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int *)v20) = v9;
    return v19;
}
```

## `sub_10327130` `0x10327130`

_19 bytes. (leaf/helper — see body)_

```c
int sub_10327130(int a0)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_10326e70(v0);
}
```

