# elfbot.dll decompiled — jiru 0x1032d550..0x1032e5d0

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1032d550` `0x1032d550`

_44 bytes. (leaf/helper — see body)_

```c
int sub_1032d550(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_1032d4e0(v0);
    if (((char)a1 & 1))
        sub_10350abd(v0);
    return v0;
}
```

## `sub_1032d580` `0x1032d580`

_115 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103903a0;

int sub_1032d580(int a0, int a1)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4138
    unsigned int v9;  // eax
    unsigned long v10;  // 4154
    unsigned long v11;  // 4123
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
    sub_1035327a(a1, g_1038e180 ^ &v3, a0, v9, sub_1036d3b3, -1, &v4);
    v2 = 0;
    *((char **)a0) = &g_103903a0;
    sub_103145d0(a0 + 12, a1 + 12);
    v11 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v11) = v9;
    return a0;
}
```

## `sub_1032d600` `0x1032d600`

_143 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1032d600(unsigned int a0)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4136
    unsigned long v13;  // 4150
    unsigned long v14;  // 4123
    unsigned int v0;  // [bp-0x3c]
    int v1;  // [bp-0x38]
    int v2;  // [bp-0x34]
    char v3;  // [bp-0x2c]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    char v6;  // [bp-0x8], Other Possible Types: unsigned int
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036d3f6;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v4 = *((int *)v12);
    v0 = g_1038e180 ^ &v7;
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v4;
    v2 = sub_103257a0(&v3);
    v1 = v2;
    v6 = 0;
    sub_1031e640(a0, v1);
    v6 = 2;
    sub_1031a3a0(&v3);
    sub_10319ff0(a0 + 32);
    v6 = 3;
    sub_1031a090(a0 + 64);
    v14 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v14) = v4;
    return a0;
}
```

## `sub_1032d690` `0x1032d690`

_17 bytes. (leaf/helper — see body)_

```c
int sub_1032d690(int a0)
{
    char v0;  // [bp+0x0]

    return sub_10333390(a0, &v0);
}
```

## `sub_1032d6b0` `0x1032d6b0`

_17 bytes. (leaf/helper — see body)_

```c
int sub_1032d6b0(int a0)
{
    char v0;  // [bp+0x0]

    return sub_103334a0(a0, &v0);
}
```

## `sub_1032d6d0` `0x1032d6d0`

_149 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1032d6d0(unsigned int a0, unsigned int a1)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4139
    unsigned long v11;  // 4153
    unsigned long v12;  // 4123
    int v0;  // [bp-0x38]
    int v1;  // [bp-0x34]
    char v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char v5;  // [bp-0x8], Other Possible Types: unsigned int
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036d446;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    v1 = sub_10332ed0(&v2, g_1038e180 ^ &v6);
    v0 = v1;
    v5 = 0;
    sub_1031e640(a0, v0);
    v5 = 2;
    sub_1031a3a0(&v2);
    sub_10319ff0(a0 + 32);
    v5 = 3;
    sub_1031a090(a0 + 64);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v3;
    return a0;
}
```

## `sub_1032d770` `0x1032d770`

_17 bytes. (leaf/helper — see body)_

```c
int sub_1032d770(int a0)
{
    char v0;  // [bp+0x0]

    return sub_103330c0(a0, &v0);
}
```

## `sub_1032d790` `0x1032d790`

_17 bytes. (leaf/helper — see body)_

```c
int sub_1032d790(int a0)
{
    char v0;  // [bp+0x0]

    return sub_10333270(a0, &v0);
}
```

## `sub_1032d7b0` `0x1032d7b0`

_92 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1032d7b0(int a0, int a1)
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
    sub_103335b0(a0, a1, g_1038e180 ^ &v2, 0, v8, sub_1036d489, -1, &v3);
    v11 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v11) = v8;
    return a0;
}
```

## `sub_1032d810` `0x1032d810`

_92 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1032d810(int a0, int a1)
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
    sub_103337e0(a0, a1, g_1038e180 ^ &v2, 0, v8, sub_1036d4c9, -1, &v3);
    v11 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v11) = v8;
    return a0;
}
```

## `sub_1032d870` `0x1032d870`

_149 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1032d870(unsigned int a0, unsigned int a1)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4139
    unsigned long v11;  // 4153
    unsigned long v12;  // 4123
    int v0;  // [bp-0x38]
    int v1;  // [bp-0x34]
    char v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char v5;  // [bp-0x8], Other Possible Types: unsigned int
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036d516;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    v1 = sub_10332ce0(&v2, g_1038e180 ^ &v6);
    v0 = v1;
    v5 = 0;
    sub_1031a4d0(a0, v0);
    v5 = 2;
    sub_10314610(&v2);
    sub_10319ff0(a0 + 32);
    v5 = 3;
    sub_1031a090(a0 + 64);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v3;
    return a0;
}
```

## `sub_1032d910` `0x1032d910`

_114 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_1032d910(int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4140
    unsigned long v11;  // 4156
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036d567;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    v4 = 2;
    v4 = 1;
    sub_10319f00(v1 + 260);
    v4 = 0;
    sub_10319f00(v1 + 164);
    v4 = 4294967295;
    v12 = sub_10319f00(v1 + 0x44);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_1032d990` `0x1032d990`

_136 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int * sub_1032d990(unsigned int *a0, unsigned int *i)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4139
    unsigned long v10;  // 4159
    unsigned int v11;  // ecx
    unsigned int *iter;  // edi
    unsigned long v13;  // 4127
    unsigned int v0;  // [bp-0x20]
    unsigned int *v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036d5b7;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    v11 = 0x11;
    for (iter = v1; v11; i += 1)
    {
        v11 -= 1;
        *(iter) = *(i);
        iter += 1;
    }
    sub_1032d600(v1 + 0x11);
    v4 = 0;
    sub_1032d600(v1 + 41);
    v4 = 1;
    sub_1032d600(v1 + 65);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v2;
    return v1;
}
```

## `sub_1032da20` `0x1032da20`

_136 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int * sub_1032da20(unsigned int *a0, unsigned int *i)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4139
    unsigned long v10;  // 4159
    unsigned int v11;  // ecx
    unsigned int *iter;  // edi
    unsigned long v13;  // 4127
    unsigned int v0;  // [bp-0x20]
    unsigned int *v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036d607;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    v11 = 0x11;
    for (iter = v1; v11; i += 1)
    {
        v11 -= 1;
        *(iter) = *(i);
        iter += 1;
    }
    sub_1032d600(v1 + 0x11);
    v4 = 0;
    sub_1032d600(v1 + 41);
    v4 = 1;
    sub_1032d600(v1 + 65);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v2;
    return v1;
}
```

## `sub_1032dab0` `0x1032dab0`

_63 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

int sub_1032dab0(struct_0 *a0)
{
    int v4[2];  // eax
    int v5[2];  // eax
    char v0;  // [bp-0x1c]
    char v1;  // [bp-0x14]
    char v2;  // [bp-0xc]

    v4 = sub_10326160(a0, &v2);
    v5 = sub_1032daf0(&v1, v4[0], v4[1]);
    return sub_1032ee10(&v0, v5[0], v5[1]);
}
```

## `sub_1032daf0` `0x1032daf0`

_37 bytes. (leaf/helper — see body)_

```c
int sub_1032daf0(unsigned int a0, int a1)
{
    unsigned int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_10326240(a1, sub_1031a4a0(v0), v0);
    return a1;
}
```

## `sub_1032db20` `0x1032db20`

_51 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

int sub_1032db20(struct_0 *a0, unsigned short a1)
{
    int v4[2];  // eax
    unsigned int v0;  // [bp-0x1c]
    char v1;  // [bp-0x14]
    char v2;  // [bp-0xc]

    *((unsigned short *)&v0) = a1;
    v4 = sub_10326160(a0, &v2);
    return sub_1032ed90(&v1, v4[0], v4[1]);
}
```

## `sub_1032db60` `0x1032db60`

_19 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

struct_0 * sub_1032db60(struct_0 *a0)
{
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_1031fc50(v0);
}
```

## `sub_1032db80` `0x1032db80`

_92 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_1032db80(unsigned int a0, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4135
    unsigned long v10;  // 4151
    unsigned long v11;  // 4120
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036d638;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_10315800(v1);
    v4 = 0;
    sub_1032dc30(a1);
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_1032dbe0` `0x1032dbe0`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

void sub_1032dbe0(int a0)
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
    v3 = sub_1036d668;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    v4 = 0;
    v4 = 4294967295;
    sub_10314610(v1);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v2;
    return;
}
```

## `sub_1032dc30` `0x1032dc30`

_30 bytes. (leaf/helper — see body)_

```c
void sub_1032dc30(unsigned int a0, int a1)
{
    unsigned int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_10332bf0((unsigned int)sub_102ec9a0(a1));
    return;
}
```

## `sub_1032dc50` `0x1032dc50`

_19 bytes. (leaf/helper — see body)_

```c
void sub_1032dc50(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10332cb0(a0, &v1);
    return;
}
```

## `sub_1032dc70` `0x1032dc70`

_39 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    char field_4;
} struct_0;

struct_0 * sub_1032dc70(struct_0 *a0, unsigned int a1)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    a0->field_0 = a1;
    a0->field_4 = 0;
    sub_1032eec0(a0, &v1);
    return a0;
}
```

## `sub_1032dca0` `0x1032dca0`

_36 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1032dca0(int a0)
{
    unsigned int v3;  // eax
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    v3 = sub_103455c0(a0, &v1) & 0xff;
    if (!v3)
        return v3;
    return sub_1032dcd0();
}
```

## `sub_1032dcd0` `0x1032dcd0`

_91 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b140;

int sub_1032dcd0(int *a0)
{
    int v3;  // eax
    unsigned int v4;  // eax
    unsigned int v0;  // [bp-0xc]
    int v1;  // [bp-0x8]

    v0 = 0x80000000;
    InterlockedExchangeAdd(a0, 0x80000000);
    v1 = *(a0);
    if ((v1 & 0x40000000))
    {
        return v1;
    }
    else if (v1 > -0x80000000)
    {
        v3 = sub_1032dd30(a0, 30);
        if ((char)v3)
            return v3;
        v4 = sub_1032dd50();
        return g_1038b140(v4);
    }
    else
    {
        return v1;
    }
}
```

## `sub_1032dd30` `0x1032dd30`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1032dd30(unsigned int a0, char a1)
{
    InterlockedExchange8(a0 + (a1 >> 3), *((char *)(a0 + (a1 >> 3))) | 1 << (a1 & 7));
    return -(-(0 < ((*((char *)(a0 + (a1 >> 3))) >> (a1 & 7) & 1) == 1)));
}
```

## `sub_1032dd50` `0x1032dd50`

_99 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b128;

unsigned int sub_1032dd50(struct_0 *a0)
{
    unsigned int v4;  // 4110
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v2 = sub_1032df00(&a0->field_4, a0);
    if (v2)
        return v2;
    v1 = sub_1032ddc0(0, 0);
    v4 = InterlockedCompareExchange(&a0->field_4, v1, 0);
    v0 = (0 == v4 ? 0 : v4);
    if (!v0)
        return v1;
    g_1038b128(v1);
    return v0;
}
```

## `sub_1032dda7` `0x1032dda7`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032dda7(void)
{
}
```

## `sub_1032ddc0` `0x1032ddc0`

_62 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b144;
extern int g_1039c7e8;

unsigned int sub_1032ddc0(unsigned int a0, unsigned int a1)
{
    char v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x8]

    v1 = g_1038b144(0, a0, a1, 0);
    if (!v1)
    {
        sub_10369820();
        sub_103533ea(&v0, &g_1039c7e8);
    }
    return v1;
}
```

## `sub_1032de00` `0x1032de00`

_93 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103905e4;

int sub_1032de00(int a0, int a1)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4138
    unsigned int v8;  // eax
    unsigned long v9;  // 4154
    unsigned long v10;  // 4128
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
    sub_1032de60(a1, g_1038e180 ^ &v2, a0, v8, sub_1036d698, -1, &v3);
    *((char **)a0) = &g_103905e4;
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v10) = v8;
    return a0;
}
```

## `sub_1032de60` `0x1032de60`

_105 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
} struct_0;

extern unsigned int g_1038e180;
extern char g_103905f0;

struct_0 * sub_1032de60(struct_0 *a0, struct_0 *a1)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4138
    unsigned int v8;  // eax
    unsigned long v9;  // 4154
    unsigned long v10;  // 4144
    struct_0 *v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v8 = *((int *)v7);
    v1 = *((int *)v7);
    v0 = a0;
    v9 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v9) = &v1;
    sub_1035327a(a1, g_1038e180 ^ &v2, a0, v8, sub_1036d6c8, -1, &v3);
    *((char **)&a0->padding_0[0]) = &g_103905f0;
    a0->field_c = a1->field_c;
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v10) = v8;
    return a0;
}
```

## `sub_1032ded0` `0x1032ded0`

_44 bytes. (leaf/helper — see body)_

```c
int sub_1032ded0(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_103697e0(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_1032df00` `0x1032df00`

_19 bytes. (leaf/helper — see body)_

```c
int sub_1032df00(unsigned int *a0)
{
    unsigned int v0;  // [bp-0x8]

    v0 = *(a0);
    return v0;
}
```

## `sub_1032df20` `0x1032df20`

_148 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1032df20(unsigned int a0)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4139
    unsigned long v12;  // 4153
    unsigned long v13;  // 4120
    unsigned int v0;  // [bp-0x20]
    unsigned int *v1;  // [bp-0x1c], Other Possible Types: unsigned int
    unsigned int *v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036d6fb;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v3 = *((int *)v11);
    v0 = g_1038e180 ^ &v6;
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v3;
    sub_1031a280(a0 + 4);
    v5 = 0;
    v2 = sub_1031acf0(4, sub_1031a280(a0 + 4));
    if (v2)
    {
        *(v2) = 0;
        v1 = v2;
    }
    else
    {
        v1 = 0;
    }
    sub_1031ac50(a0, 0);
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v13) = v3;
    return a0;
}
```

## `sub_1032dfc0` `0x1032dfc0`

_84 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1032dfc0(int a0, int a1)
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
    sub_103301d0(a1, g_1038e180 ^ &v2, a0, v8, sub_1036d728, -1, &v3);
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v10) = v8;
    return a0;
}
```

## `sub_1032e020` `0x1032e020`

_84 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1032e020(int a0, int a1)
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
    sub_103301f0(a1, g_1038e180 ^ &v2, a0, v8, sub_1036d758, -1, &v3);
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v10) = v8;
    return a0;
}
```

## `sub_1032e080` `0x1032e080`

_28 bytes. (leaf/helper — see body)_

```c
int sub_1032e080(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10330220(a1, a0, &v1);
    return a0;
}
```

## `sub_1032e0a0` `0x1032e0a0`

_19 bytes. (leaf/helper — see body)_

```c
void sub_1032e0a0(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10330260(a0, &v1);
    return;
}
```

## `sub_1032e0c0` `0x1032e0c0`

_28 bytes. (leaf/helper — see body)_

```c
int sub_1032e0c0(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10330280(a1, a0, &v1);
    return a0;
}
```

## `sub_1032e0e0` `0x1032e0e0`

_19 bytes. (leaf/helper — see body)_

```c
void sub_1032e0e0(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_103301b0(a0, &v1);
    return;
}
```

## `sub_1032e100` `0x1032e100`

_84 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1032e100(int a0, int a1)
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
    sub_103301d0(a1, g_1038e180 ^ &v2, a0, v8, sub_1036d788, -1, &v3);
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v10) = v8;
    return a0;
}
```

## `sub_1032e160` `0x1032e160`

_84 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1032e160(int a0, int a1)
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
    sub_103302c0(a1, g_1038e180 ^ &v2, a0, v8, sub_1036d7b8, -1, &v3);
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v10) = v8;
    return a0;
}
```

## `sub_1032e1c0` `0x1032e1c0`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_1032e1c0(int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4137
    unsigned int v10;  // eax
    unsigned long v11;  // 4153
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
    v12 = sub_103302f0(g_1038e180 ^ &v3, a0, v10, sub_1036d7e8, -1, &v4);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v10;
    return v12;
}
```

## `sub_1032e210` `0x1032e210`

_42 bytes. (leaf/helper — see body)_

```c
int sub_1032e210(unsigned int a0)
{
    unsigned int v0;  // [bp-0x10]

    v0 = a0;
    sub_1031a280(&v0);
    sub_103147d0(a0);
    sub_10330470(0);
    return a0;
}
```

## `sub_1032e240` `0x1032e240`

_50 bytes. (leaf/helper — see body)_

```c
int sub_1032e240(unsigned int a0, int a1, int a2)
{
    unsigned int v0;  // [bp-0x10]

    v0 = a0;
    sub_1031a280(&v0);
    sub_103147d0(a0);
    sub_10330310(a1, a2);
    return a0;
}
```

## `sub_1032e280` `0x1032e280`

_19 bytes. (leaf/helper — see body)_

```c
void sub_1032e280(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_103304f0(a0, &v1);
    return;
}
```

## `sub_1032e2a0` `0x1032e2a0`

_49 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1032e2a0(unsigned int *a0)
{
    unsigned int v0;  // [bp-0xc]

    v0 = (!a0[1] ? 0 : a0[2] - a0[1]);
    return v0;
}
```

## `sub_1032e2e0` `0x1032e2e0`

_40 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

int sub_1032e2e0(struct_0 *a0, unsigned int a1)
{
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    if (a1 >= sub_1032e2a0(v0))
        sub_10353616();
    return v0->field_4 + a1;
}
```

## `sub_1032e310` `0x1032e310`

_103 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    int field_8;
} struct_0;

unsigned int sub_1032e310(struct_0 *a0, int a1)
{
    unsigned int v2;  // eax
    int v3;  // esi
    unsigned int v4;  // eax
    int v5[2];  // eax
    char v0;  // [bp-0x14]
    char v1;  // [bp-0xc]

    v2 = sub_1032e2a0(a0);
    if (v2 >= sub_103303b0(v3, a0))
    {
        v5 = sub_10330670(&v1, a1);
        return sub_103303f0(&v0, v5[0], v5[1]);
    }
    v4 = sub_10330560(a0->field_8, 1, a1);
    a0->field_8 = v4;
    return v4;
}
```

## `sub_1032e380` `0x1032e380`

_42 bytes. (leaf/helper — see body)_

```c
int sub_1032e380(unsigned int a0)
{
    unsigned int v0;  // [bp-0x10]

    v0 = a0;
    sub_1031a280(&v0);
    sub_103147d0(a0);
    sub_10330760(0);
    return a0;
}
```

## `sub_1032e3b0` `0x1032e3b0`

_50 bytes. (leaf/helper — see body)_

```c
int sub_1032e3b0(unsigned int a0, int a1, int a2)
{
    unsigned int v0;  // [bp-0x10]

    v0 = a0;
    sub_1031a280(&v0);
    sub_103147d0(a0);
    sub_10330590(a1, a2);
    return a0;
}
```

## `sub_1032e3f0` `0x1032e3f0`

_19 bytes. (leaf/helper — see body)_

```c
void sub_1032e3f0(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_103307e0(a0, &v1);
    return;
}
```

## `sub_1032e410` `0x1032e410`

_43 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

int sub_1032e410(struct_0 *a0, unsigned int a1)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    if (a1 >= sub_103306a0(a0, &v1))
        sub_10353616();
    return a0->field_4 + a1 * 2;
}
```

## `sub_1032e440` `0x1032e440`

_103 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    int field_8;
} struct_0;

unsigned int sub_1032e440(struct_0 *a0, int a1)
{
    int v2;  // esi
    unsigned int v3;  // eax
    unsigned int v4;  // eax
    int v5[2];  // eax
    char v0;  // [bp-0x14]
    char v1;  // [bp-0xc]

    v3 = sub_103306a0(v2, a0);
    if (v3 >= sub_10330630(v2, a0))
    {
        v5 = sub_10330670(&v1, a1);
        return sub_103306e0(&v0, v5[0], v5[1]);
    }
    v4 = sub_10330850(a0->field_8, 1, a1);
    a0->field_8 = v4;
    return v4;
}
```

## `sub_1032e4b0` `0x1032e4b0`

_84 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
    unsigned int field_4;
} struct_1;

typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

struct_1 * sub_1032e4b0(struct_1 *a0)
{
    struct_0 *v2;  // eax
    struct_1 *idx;  // [bp-0x8]

    idx = a0;
    idx = a0;
    if (idx->field_0 != 0xfffffffe)
    {
        if (!idx->field_0)
            sub_10353616();
        v2 = sub_1031a4a0(idx->field_0);
        if (idx->field_4 >= &v2->padding_0[2 * idx->field_0->field_14])
            sub_10353616();
    }
    idx->field_4 = idx->field_4 + 2;
    return idx;
}
```

## `sub_1032e510` `0x1032e510`

_41 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_1032e510(unsigned int *a0, int a1, int a2, char a3)
{
    unsigned int *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    *(v0) = sub_1032cdb0(a1, a2, a3);
    return v0;
}
```

## `sub_1032e540` `0x1032e540`

_41 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_1032e540(unsigned int *a0, int a1, int a2, char a3)
{
    unsigned int *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    *(v0) = sub_1032cdf0(a1, a2, a3);
    return v0;
}
```

## `sub_1032e570` `0x1032e570`

_41 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_1032e570(unsigned int *a0, int a1, int a2, char a3)
{
    unsigned int *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    *(v0) = sub_1032ce30(a1, a2, a3);
    return v0;
}
```

## `sub_1032e5a0` `0x1032e5a0`

_41 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_1032e5a0(unsigned int *a0, int a1, int a2, char a3)
{
    unsigned int *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    *(v0) = sub_1032ce70(a1, a2, a3);
    return v0;
}
```

## `sub_1032e5d0` `0x1032e5d0`

_41 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_1032e5d0(unsigned int *a0, int a1, int a2, char a3)
{
    unsigned int *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    *(v0) = sub_1032ceb0(a1, a2, a3);
    return v0;
}
```

