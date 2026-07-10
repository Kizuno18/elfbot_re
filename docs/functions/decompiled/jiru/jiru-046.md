# elfbot.dll decompiled — jiru 0x10338520..0x10339b20

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10338520` `0x10338520`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10338520(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10339220(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_10338550` `0x10338550`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10338550(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10339190(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_10338580` `0x10338580`

_100 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int * sub_10338580(unsigned int *a0, unsigned int *a1)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4148
    unsigned int v8;  // eax
    unsigned long v9;  // 4164
    unsigned long v10;  // 4123
    unsigned int *v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v8 = *((int *)v7);
    v1 = *((int *)v7);
    v0 = a0;
    v9 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v9) = &v1;
    *(a0) = *(a1);
    sub_103385f0(a1 + 1, g_1038e180 ^ &v2, a0, v8, sub_1036f14b, -1, &v3);
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v10) = v8;
    return a0;
}
```

## `sub_103385f0` `0x103385f0`

_44 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_103385f0(unsigned int *a0, unsigned int *a1)
{
    unsigned int *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    *(a0) = *(a1);
    if (*(a0))
        sub_10338620(a0, &v1);
    return a0;
}
```

## `sub_10338620` `0x10338620`

_26 bytes. (leaf/helper — see body)_

```c
int sub_10338620(unsigned int a0)
{
    InterlockedExchangeAdd(a0 + 4, 1);
    return a0 + 4;
}
```

## `sub_10338640` `0x10338640`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10338640(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10339410(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_10338670` `0x10338670`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10338670(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10339380(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_103386a0` `0x103386a0`

_100 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int * sub_103386a0(unsigned int *a0, unsigned int *a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4148
    unsigned long v10;  // 4164
    unsigned long v11;  // 4123
    unsigned int v0;  // [bp-0x18]
    unsigned int *v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036f17b;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    *(v1) = *(a1);
    sub_103385f0(v1 + 1, a1 + 1);
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_10338710` `0x10338710`

_31 bytes. (leaf/helper — see body)_

```c
int sub_10338710(int a0, char a1, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10339730(&/* unsupported instruction */, a1, 1, a0, &v1);
}
```

## `sub_10338730` `0x10338730`

_31 bytes. (leaf/helper — see body)_

```c
int sub_10338730(int a0, char a1, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10338750(&/* unsupported instruction */, a1, 1, a0, &v1);
}
```

## `sub_10338750` `0x10338750`

_215 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

int sub_10338750(struct_0 *a0, int a1, int a2, int a3)
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
    v2 = &sub_10314a50(a0)->padding_0[v0];
    while (true)
    {
        if ((char)sub_10338830(v2, a1) && !sub_103340f0(v2, a1, a3))
            return v2 - (char *)sub_10314a50(a0);
        if (v2 == sub_10314a50(a0))
            break;
        v2 -= 1;
    }
    return -1;
}
```

## `sub_1033880d` `0x1033880d`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1033880d(void)
{
}
```

## `sub_10338830` `0x10338830`

_26 bytes. (leaf/helper — see body)_

```c
int sub_10338830(char *a0, char *a1)
{
    unsigned int v0;  // eax

    v0 = *(a1);
    return _INSERT(v0, 0, *(a0) == v0);
}
```

## `sub_10338850` `0x10338850`

_79 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    struct struct_0 *field_14;
} struct_0;

struct_0 * sub_10338850(struct_0 *a0, struct_0 *a1)
{
    struct_0 *v1;  // eax
    struct_0 *v0;  // [bp-0x8]

    if (a0->field_14 > a1)
    {
        return a0;
    }
    else if (*((int *)&a0[1].padding_0[0]) != a1)
    {
        v0 = a0->field_14;
        v1 = sub_1031e940(a0, a1, 1);
        if (!*((char *)&v1))
            return v1;
        return sub_1031a440(a0, v0);
    }
    else
    {
        return *((int *)&a0[1].padding_0[0]);
    }
}
```

## `sub_103388a0` `0x103388a0`

_11 bytes. (leaf/helper — see body)_

```c
void sub_103388a0(unsigned int a0)
{
    return;
}
```

## `sub_103388b0` `0x103388b0`

_180 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_103388b0(unsigned int *a0, unsigned int a1)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4178
    unsigned long v11;  // 4182
    unsigned int v13;  // eax
    unsigned long v15;  // 4113
    unsigned int v0;  // [bp-0x24]
    char v1;  // [bp-0x1c]
    char v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036f1b0;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v0 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    if (*(a0) == *((int *)a1))
    {
        sub_10338970(sub_1031a280(a1 + 4));
        v5 = 0;
        sub_1033a0c0(&v2);
        v5 = 4294967295;
        v13 = sub_10339690(&v2);
    }
    else
    {
        sub_103398b0(a0, sub_1031aa20(a1));
        v5 = 1;
        sub_1033a100(&v1);
        v5 = 4294967295;
        v13 = sub_103396e0(&v1);
    }
    v15 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v15) = v3;
    return v13;
}
```

## `sub_10338970` `0x10338970`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int * sub_10338970(unsigned int *a0, unsigned int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4135
    unsigned long v10;  // 4151
    unsigned long v11;  // 4133
    unsigned int v0;  // [bp-0x18]
    unsigned int *v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036f1d8;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_1031a280(v1);
    *(v1) = a1;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_103389d0` `0x103389d0`

_57 bytes. (leaf/helper — see body)_

```c
unsigned int [2] sub_103389d0(int *a0, unsigned int *a1, int a2)
{
    unsigned int v1[2];  // eax
    unsigned int v2;  // edx
    char v0;  // [bp+0x0]

    v1 = sub_10339830(a2, a0, *(a0), a0[1], &v0);
    v2 = v1[1];
    *(a1) = v1[0];
    a1[1] = v2;
    return a1;
}
```

## `sub_10338a10` `0x10338a10`

_31 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    struct struct_0 *field_4;
} struct_0;

typedef struct struct_0 {
    char padding_0[8];
    int field_8;
} struct_0;

struct_0 * sub_10338a10(struct_0 *a0, int a1)
{
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_1032e440(v0->field_4, a1);
    return v0;
}
```

## `sub_10338a30` `0x10338a30`

_31 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    struct struct_0 *field_4;
} struct_0;

typedef struct struct_0 {
    char padding_0[8];
    int field_8;
} struct_0;

struct_0 * sub_10338a30(struct_0 *a0, int a1)
{
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_1032e310(v0->field_4, a1);
    return v0;
}
```

## `sub_10338a50` `0x10338a50`

_29 bytes. (leaf/helper — see body)_

```c
int sub_10338a50(int a0, int a1, int a2)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_1033a140(a1, a2, a0, &v1);
}
```

## `sub_10338a70` `0x10338a70`

_25 bytes. (leaf/helper — see body)_

```c
int sub_10338a70(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_1033a1c0(a1, a0, &v1);
}
```

## `sub_10338a90` `0x10338a90`

_90 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int * sub_10338a90(unsigned int *a0)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4140
    unsigned int v9;  // eax
    unsigned long v10;  // 4156
    unsigned long v11;  // 4123
    unsigned int *v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v9 = *((int *)v8);
    v1 = *((int *)v8);
    v0 = a0;
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v10) = &v1;
    *(a0) = 0;
    sub_10338af0(g_1038e180 ^ &v2, a0, v9, sub_1036f20b, -1, &v3);
    v11 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v11) = v9;
    return a0;
}
```

## `sub_10338af0` `0x10338af0`

_23 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_10338af0(unsigned int *a0)
{
    *(a0) = 0;
    return a0;
}
```

## `sub_10338b10` `0x10338b10`

_106 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10338b10(int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4139
    unsigned long v10;  // 4153
    unsigned int v11;  // eax
    unsigned long v12;  // 4113
    unsigned int v0[2];  // [bp-0x18]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]
    char v4;  // [bp-0x4]

    v3 = 4294967295;
    v2 = sub_1036f238;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v1 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v1;
    sub_10338a90(v0);
    v3 = 0;
    sub_10339880(a0, g_1038e180 ^ &v4, sub_10338a90(v0), sub_10338a90(v0), a0);
    v3 = 4294967295;
    v11 = sub_103368a0(v0);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v1;
    return v11;
}
```

## `sub_10338b80` `0x10338b80`

_90 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int * sub_10338b80(unsigned int *a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4140
    unsigned long v11;  // 4156
    unsigned long v12;  // 4123
    unsigned int v0;  // [bp-0x18]
    unsigned int *v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036f26b;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    *(v1) = 0;
    sub_10338af0(v1 + 1);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v2;
    return v1;
}
```

## `sub_10338be0` `0x10338be0`

_106 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int * sub_10338be0(int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4139
    unsigned long v10;  // 4153
    unsigned int *v11;  // eax
    unsigned long v12;  // 4113
    unsigned int v0[2];  // [bp-0x18]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]
    char v4;  // [bp-0x4]

    v3 = 4294967295;
    v2 = sub_1036f298;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v1 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v1;
    sub_10338b80(v0);
    v3 = 0;
    sub_10339880(a0, g_1038e180 ^ &v4, sub_10338b80(v0), sub_10338b80(v0), a0);
    v3 = 4294967295;
    v11 = sub_103369a0(v0);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v1;
    return v11;
}
```

## `sub_10338c50` `0x10338c50`

_118 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103907a8;
extern char g_103907b0;

int sub_10338c50(unsigned int a0, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4154
    unsigned long v11;  // 4135
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036f2d3;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_10314290(v1, a1);
    v4 = 0;
    sub_103167f0(v1 + 40);
    *((char **)v1) = &g_103907b0;
    *((char **)(v1 + 40)) = &g_103907a8;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_10338cd0` `0x10338cd0`

_194 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390784;
extern char g_10390794;
extern char g_1039079c;

unsigned int sub_10338cd0(unsigned int idx, unsigned int a1)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4139
    unsigned long v11;  // 4153
    unsigned long v12;  // 4123
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char v5;  // [bp-0x8], Other Possible Types: unsigned int
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036f303;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v0 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    sub_10334ff0(idx, a1);
    v5 = 0;
    sub_10316a00(idx + 60);
    v5 = 1;
    *((char **)idx) = &g_1039079c;
    *((char **)(idx + 40)) = &g_10390794;
    *((char **)(idx + 60)) = &g_10390784;
    v2 = (!a1 ? 0 : a1 + 40);
    v1 = (!idx ? 0 : idx + 40);
    sub_10316940(v1, v2);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v3;
    return idx;
}
```

## `sub_10338da0` `0x10338da0`

_118 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103907e0;
extern char g_103907e8;

int sub_10338da0(unsigned int a0, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4154
    unsigned long v11;  // 4135
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036f333;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_103351d0(v1, a1);
    v4 = 0;
    sub_103167f0(v1 + 40);
    *((char **)v1) = &g_103907e8;
    *((char **)(v1 + 40)) = &g_103907e0;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_10338e20` `0x10338e20`

_194 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103907bc;
extern char g_103907cc;
extern char g_103907d4;

int sub_10338e20(unsigned int idx, unsigned int a1)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4139
    unsigned long v11;  // 4153
    unsigned long v12;  // 4123
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char v5;  // [bp-0x8], Other Possible Types: unsigned int
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036f363;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v0 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    sub_10335130(idx, a1);
    v5 = 0;
    sub_10316a00(idx + 60);
    v5 = 1;
    *((char **)idx) = &g_103907d4;
    *((char **)(idx + 40)) = &g_103907cc;
    *((char **)(idx + 60)) = &g_103907bc;
    v2 = (!a1 ? 0 : a1 + 40);
    v1 = (!idx ? 0 : idx + 40);
    sub_10316940(v1, v2);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v3;
    return idx;
}
```

## `sub_10338ef0` `0x10338ef0`

_118 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390858;
extern char g_10390860;

int sub_10338ef0(unsigned int a0, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4154
    unsigned long v11;  // 4135
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036f393;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_10335490(v1, a1);
    v4 = 0;
    sub_103167f0(v1 + 40);
    *((char **)v1) = &g_10390860;
    *((char **)(v1 + 40)) = &g_10390858;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_10338f70` `0x10338f70`

_194 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390834;
extern char g_10390844;
extern char g_1039084c;

int sub_10338f70(unsigned int idx, unsigned int a1)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4139
    unsigned long v11;  // 4153
    unsigned long v12;  // 4123
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char v5;  // [bp-0x8], Other Possible Types: unsigned int
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036f3c3;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v0 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    sub_103353f0(idx, a1);
    v5 = 0;
    sub_10316a00(idx + 60);
    v5 = 1;
    *((char **)idx) = &g_1039084c;
    *((char **)(idx + 40)) = &g_10390844;
    *((char **)(idx + 60)) = &g_10390834;
    v2 = (!a1 ? 0 : a1 + 40);
    v1 = (!idx ? 0 : idx + 40);
    sub_10316940(v1, v2);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v3;
    return idx;
}
```

## `sub_10339040` `0x10339040`

_118 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390890;
extern char g_10390898;

int sub_10339040(unsigned int a0, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4154
    unsigned long v11;  // 4135
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036f3f3;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_10335630(v1, a1);
    v4 = 0;
    sub_103167f0(v1 + 40);
    *((char **)v1) = &g_10390898;
    *((char **)(v1 + 40)) = &g_10390890;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_103390c0` `0x103390c0`

_194 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1039086c;
extern char g_1039087c;
extern char g_10390884;

int sub_103390c0(unsigned int idx, unsigned int a1)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4139
    unsigned long v11;  // 4153
    unsigned long v12;  // 4123
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char v5;  // [bp-0x8], Other Possible Types: unsigned int
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036f423;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v0 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    sub_10335590(idx, a1);
    v5 = 0;
    sub_10316a00(idx + 60);
    v5 = 1;
    *((char **)idx) = &g_10390884;
    *((char **)(idx + 40)) = &g_1039087c;
    *((char **)(idx + 60)) = &g_1039086c;
    v2 = (!a1 ? 0 : a1 + 40);
    v1 = (!idx ? 0 : idx + 40);
    sub_10316940(v1, v2);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v3;
    return idx;
}
```

## `sub_10339190` `0x10339190`

_132 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103908fc;
extern char g_10390904;

unsigned int sub_10339190(int a0)
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
    v3 = sub_1036f46f;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    *((char **)a0) = &g_10390904;
    *((char **)(a0 + 84)) = &g_103908fc;
    v4 = 1;
    v4 = 0;
    v1 = (!a0 ? 0 : a0 + 84);
    sub_10313d70(v1);
    v4 = 4294967295;
    v12 = sub_10335b60(a0);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_10339220` `0x10339220`

_142 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103908d8;
extern char g_103908e8;
extern char g_103908f0;

unsigned int sub_10339220(unsigned int idx)
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
    v3 = sub_1036f4bf;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    *((char **)idx) = &g_103908f0;
    *((char **)(idx + 84)) = &g_103908e8;
    *((char **)(idx + 104)) = &g_103908d8;
    v4 = 1;
    v4 = 0;
    v1 = (!idx ? 0 : idx + 104);
    sub_10313bb0(v1);
    v4 = 4294967295;
    v12 = sub_10339190(idx);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_103392b0` `0x103392b0`

_148 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_103392b0(int a0)
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
    v5 = sub_1036f4eb;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v4 = *((int *)v12);
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v4;
    v2 = sub_10350a53(108, g_1038e180 ^ &v7);
    v6 = 0;
    v1 = (!v2 ? 0 : sub_10337f60(v2, a0 - 104));
    v3 = v1;
    v6 = 4294967295;
    v0 = (!v3 ? 0 : v3 + 104);
    v14 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v14) = v4;
    return v0;
}
```

## `sub_10339350` `0x10339350`

_42 bytes. (leaf/helper — see body)_

```c
extern int g_1039dfb0;

int sub_10339350(int a0)
{
    char v0;  // [bp-0x70]

    sub_10337f60(&v0, a0 - 104);
    return sub_103533ea(&v0, &g_1039dfb0);
}
```

## `sub_10339380` `0x10339380`

_132 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390934;
extern char g_1039093c;

unsigned int sub_10339380(int a0)
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
    v3 = sub_1036f53f;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    *((char **)a0) = &g_1039093c;
    *((char **)(a0 + 84)) = &g_10390934;
    v4 = 1;
    v4 = 0;
    v1 = (!a0 ? 0 : a0 + 84);
    sub_10313d70(v1);
    v4 = 4294967295;
    v12 = sub_10335fe0(a0);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_10339410` `0x10339410`

_142 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390910;
extern char g_10390920;
extern char g_10390928;

unsigned int sub_10339410(unsigned int idx)
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
    v3 = sub_1036f58f;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    *((char **)idx) = &g_10390928;
    *((char **)(idx + 84)) = &g_10390920;
    *((char **)(idx + 104)) = &g_10390910;
    v4 = 1;
    v4 = 0;
    v1 = (!idx ? 0 : idx + 104);
    sub_10313bb0(v1);
    v4 = 4294967295;
    v12 = sub_10339380(idx);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_103394a0` `0x103394a0`

_148 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_103394a0(int a0)
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
    v5 = sub_1036f5bb;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v4 = *((int *)v12);
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v4;
    v2 = sub_10350a53(108, g_1038e180 ^ &v7);
    v6 = 0;
    v1 = (!v2 ? 0 : sub_10338270(v2, a0 - 104));
    v3 = v1;
    v6 = 4294967295;
    v0 = (!v3 ? 0 : v3 + 104);
    v14 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v14) = v4;
    return v0;
}
```

## `sub_10339540` `0x10339540`

_42 bytes. (leaf/helper — see body)_

```c
extern int g_1039e128;

int sub_10339540(int a0)
{
    char v0;  // [bp-0x70]

    sub_10338270(&v0, a0 - 104);
    return sub_103533ea(&v0, &g_1039e128);
}
```

## `sub_10339570` `0x10339570`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int * sub_10339570(unsigned int *a0, unsigned int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4135
    unsigned long v10;  // 4151
    unsigned long v11;  // 4133
    unsigned int v0;  // [bp-0x18]
    unsigned int *v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036f5e8;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_1031a280(v1);
    *(v1) = a1;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_103395d0` `0x103395d0`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int * sub_103395d0(unsigned int *a0, unsigned int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4135
    unsigned long v10;  // 4151
    unsigned long v11;  // 4133
    unsigned int v0;  // [bp-0x18]
    unsigned int *v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036f618;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_1031a280(v1);
    *(v1) = a1;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_10339630` `0x10339630`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int * sub_10339630(unsigned int *a0, unsigned int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4135
    unsigned long v10;  // 4151
    unsigned long v11;  // 4133
    unsigned int v0;  // [bp-0x18]
    unsigned int *v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036f648;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_1031a280(v1);
    *(v1) = a1;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_10339690` `0x10339690`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

void sub_10339690(unsigned int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4137
    unsigned long v11;  // 4153
    unsigned long v12;  // 4113
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036f678;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    v4 = 0;
    v4 = 4294967295;
    sub_103388a0(v1);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v2;
    return;
}
```

## `sub_103396e0` `0x103396e0`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

void sub_103396e0(unsigned int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4137
    unsigned long v11;  // 4153
    unsigned long v12;  // 4113
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036f6a8;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    v4 = 0;
    v4 = 4294967295;
    sub_103388a0(v1);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v2;
    return;
}
```

## `sub_10339730` `0x10339730`

_210 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

unsigned int sub_10339730(struct_0 *a0, int a1, unsigned int a2, int a3)
{
    int v0;  // [bp-0x10]
    int v1;  // [bp-0xc]
    int iter;  // [bp-0x8]

    if (!a3 && a2 <= *((int *)&a0->padding_8[12]))
        return a2;
    if (a2 >= *((int *)&a0->padding_8[12]))
        return 4294967295;
    iter = *((int *)&a0->padding_8[12]) - a2;
    if (a3 <= iter)
    {
        iter -= a3 - 1;
        v0 = &sub_10314a50(a0)->padding_0[a2];
        while (true)
        {
            v1 = sub_10339810(v0, iter, a1);
            if (!v1)
                break;
            if (!sub_103340f0(v1, a1, a3))
                return v1 - (char *)sub_10314a50(a0);
            iter -= v1 - v0 + 1;
            v0 = v1 + 1;
        }
    }
    return 4294967295;
}
```

## `sub_10339810` `0x10339810`

_28 bytes. (leaf/helper — see body)_

```c
int sub_10339810(int a0, int a1, char *a2)
{
    char v0;  // [bp+0x0]

    return sub_10353a90(a0, *(a2), a1, &v0);
}
```

## `sub_10339830` `0x10339830`

_27 bytes. (leaf/helper — see body)_

```c
int sub_10339830(int a0, int a1)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_1031e5a0(v0, -(a1));
}
```

## `sub_10339850` `0x10339850`

_41 bytes. (leaf/helper — see body)_

```c
int sub_10339850(unsigned int *a0, unsigned int *a1)
{
    unsigned int v0;  // [bp-0x8]

    v0 = *(a1);
    *(a1) = *(a0);
    *(a0) = v0;
    return v0;
}
```

## `sub_10339880` `0x10339880`

_47 bytes. (leaf/helper — see body)_

```c
int sub_10339880(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1033a1d0(a0, a1, a0, &v1);
    return sub_10339850(a0 + 4, a1 + 4);
}
```

## `sub_103398b0` `0x103398b0`

_97 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int [2] sub_103398b0(unsigned int *a0, unsigned int a1, unsigned int a2)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4135
    unsigned long v10;  // 4151
    unsigned long v11;  // 4145
    unsigned int v0;  // [bp-0x18]
    unsigned int v1[2];  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036f6d8;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_1031a280(v1);
    v1[0] = a1;
    v1[1] = a2;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_10339920` `0x10339920`

_112 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10339920(int a0, unsigned int a1)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4142
    unsigned long v11;  // 4156
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    char v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036f708;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    v1 = sub_1033a4e0(a1, a0, g_1038e180 ^ &v6);
    v0 = v1;
    v5 = 0;
    sub_10339880(v0, a1);
    v5 = 4294967295;
    v12 = sub_103368a0(&v2);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v3;
    return v12;
}
```

## `sub_10339990` `0x10339990`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10339990(unsigned int a0, int a1)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4138
    unsigned int v8;  // eax
    unsigned int v9;  // ecx
    unsigned long v10;  // 4154
    unsigned long v11;  // 4131
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
    sub_1033a220(a1, g_1038e180 ^ &v2, 0, v8, sub_1036f749, -1, &v3);
    v11 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v11) = v8;
    return a0;
}
```

## `sub_103399f0` `0x103399f0`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_103399f0(unsigned int a0, int a1)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4138
    unsigned int v8;  // eax
    unsigned int v9;  // ecx
    unsigned long v10;  // 4154
    unsigned long v11;  // 4131
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
    sub_1033a2a0(a1, g_1038e180 ^ &v2, 0, v8, sub_1036f789, -1, &v3);
    v11 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v11) = v8;
    return a0;
}
```

## `sub_10339a50` `0x10339a50`

_112 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int * sub_10339a50(int a0, unsigned int a1)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4142
    unsigned long v11;  // 4156
    unsigned int *v12;  // eax
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2[2];  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036f7b8;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    v1 = sub_1033a560(a1, a0, g_1038e180 ^ &v6);
    v0 = v1;
    v5 = 0;
    sub_10339880(v0, a1);
    v5 = 4294967295;
    v12 = sub_103369a0(v2);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v3;
    return v12;
}
```

## `sub_10339ac0` `0x10339ac0`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10339ac0(unsigned int a0, int a1)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4138
    unsigned int v8;  // eax
    unsigned int v9;  // ecx
    unsigned long v10;  // 4154
    unsigned long v11;  // 4131
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
    sub_1033a370(a1, g_1038e180 ^ &v2, 0, v8, sub_1036f7f9, -1, &v3);
    v11 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v11) = v8;
    return a0;
}
```

## `sub_10339b20` `0x10339b20`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10339b20(unsigned int a0, int a1)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4138
    unsigned int v8;  // eax
    unsigned int v9;  // ecx
    unsigned long v10;  // 4154
    unsigned long v11;  // 4131
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
    sub_1033a3f0(a1, g_1038e180 ^ &v2, 0, v8, sub_1036f839, -1, &v3);
    v11 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v11) = v8;
    return a0;
}
```

