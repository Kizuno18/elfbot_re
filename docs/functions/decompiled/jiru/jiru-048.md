# elfbot.dll decompiled — jiru 0x1033ad30..0x1033d030

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1033ad30` `0x1033ad30`

_49 bytes. (leaf/helper — see body)_

```c
int sub_1033ad30(int a0, int a1, int a2, int a3)
{
    unsigned int v2;  // ecx
    int v3;  // ecx
    int v4;  // edx
    int v0;  // [bp-0x8], Other Possible Types: unsigned int
    char v1;  // [bp+0x0]

    v0 = v2;
    v0 = _INSERT(v2, 2, 0);
    v3 = _INSERT(v2, 0, *((char *)((void*)&v0 + 3)));
    v4 = _INSERT(0, 0, *((char *)((void*)&v0 + 2)));
    return sub_1033c4d0(a0, a1, a2, a3, v4, v3, 0, 0, v0, &v1);
}
```

## `sub_1033ad70` `0x1033ad70`

_720 bytes. (leaf/helper — see body)_

```c
int sub_1033ad70(int a0, int a1, int a2, int a3, unsigned int a4, char a5)
{
    int v1;  // edx
    int v2;  // eax
    int v11;  // eax
    int v12;  // ecx
    int v13;  // edx
    int v14;  // eax
    int v15;  // ecx
    int v16;  // edx
    int v17;  // eax
    int v18;  // ecx
    int v19;  // edx
    int v20;  // eax
    int v3;  // ecx
    int v21;  // ecx
    int v22;  // edx
    int v4;  // edx
    int v5;  // eax
    int v6;  // ecx
    int v7;  // edx
    int v8;  // eax
    int v9;  // ecx
    int v10;  // edx
    char v0;  // [bp-0x6]

    switch (a1)
    {
    case 0:
        v1 = _INSERT(0, 0, a5);
        return sub_1033ce90(a0, a2, a3, 0, v1, 1);
    case 1:
        v2 = _INSERT(a1, 0, a5);
        return sub_1033c7f0(a0, a2, a3, 0, v2, 1);
    case 2:
        v3 = _INSERT(a1, 0, a5);
        return sub_1033ce90(a0, a2, a3, 0, v3, 1);
    case 3:
        v4 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v4, 1);
    case 4:
        v5 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v5, 1);
    case 5:
        v6 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v6, 1);
    case 6:
        v7 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v7, 1);
    case 7:
        v8 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v8, 1);
    case 8:
        v9 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v9, 1);
    case 9:
        v10 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v10, 1);
    case 10:
        v11 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v11, 1);
    case 11:
        v12 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v12, 1);
    case 12:
        v13 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v13, 1);
    case 13:
        v14 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v14, 1);
    case 14:
        v15 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v15, 1);
    case 15:
        v16 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v16, 1);
    case 16:
        v17 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v17, 1);
    case 17:
        v18 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v18, 1);
    case 18:
        v19 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v19, 1);
    case 19:
        v20 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v20, 1);
    default:
        v21 = _INSERT(0, 0, a5);
        v22 = _INSERT(0, 0, v0);
        return sub_1033ce00(a0, a1, a2, a3, v22, v21, 0, 0);
    }
}
```

## `sub_1033b090` `0x1033b090`

_720 bytes. (leaf/helper — see body)_

```c
int sub_1033b090(int a0, int a1, int a2, int a3, unsigned int a4, char a5)
{
    int v1;  // edx
    int v2;  // eax
    int v11;  // eax
    int v12;  // ecx
    int v13;  // edx
    int v14;  // eax
    int v15;  // ecx
    int v16;  // edx
    int v17;  // eax
    int v18;  // ecx
    int v19;  // edx
    int v20;  // eax
    int v3;  // ecx
    int v21;  // ecx
    int v22;  // edx
    int v4;  // edx
    int v5;  // eax
    int v6;  // ecx
    int v7;  // edx
    int v8;  // eax
    int v9;  // ecx
    int v10;  // edx
    char v0;  // [bp-0x6]

    switch (a1)
    {
    case 0:
        v1 = _INSERT(0, 0, a5);
        return sub_1033ce90(a0, a2, a3, 0, v1, 1);
    case 1:
        v2 = _INSERT(a1, 0, a5);
        return sub_1033ce90(a0, a2, a3, 0, v2, 1);
    case 2:
        v3 = _INSERT(a1, 0, a5);
        return sub_1033c7f0(a0, a2, a3, 0, v3, 1);
    case 3:
        v4 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v4, 1);
    case 4:
        v5 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v5, 1);
    case 5:
        v6 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v6, 1);
    case 6:
        v7 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v7, 1);
    case 7:
        v8 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v8, 1);
    case 8:
        v9 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v9, 1);
    case 9:
        v10 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v10, 1);
    case 10:
        v11 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v11, 1);
    case 11:
        v12 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v12, 1);
    case 12:
        v13 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v13, 1);
    case 13:
        v14 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v14, 1);
    case 14:
        v15 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v15, 1);
    case 15:
        v16 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v16, 1);
    case 16:
        v17 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v17, 1);
    case 17:
        v18 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v18, 1);
    case 18:
        v19 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v19, 1);
    case 19:
        v20 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v20, 1);
    default:
        v21 = _INSERT(0, 0, a5);
        v22 = _INSERT(0, 0, v0);
        return sub_1033ce00(a0, a1, a2, a3, v22, v21, 0, 0);
    }
}
```

## `sub_1033b3b0` `0x1033b3b0`

_49 bytes. (leaf/helper — see body)_

```c
int sub_1033b3b0(int a0, int a1, int a2, int a3)
{
    unsigned int v2;  // ecx
    int v3;  // ecx
    int v4;  // edx
    int v0;  // [bp-0x8], Other Possible Types: unsigned int
    char v1;  // [bp+0x0]

    v0 = v2;
    v0 = _INSERT(v2, 2, 0);
    v3 = _INSERT(v2, 0, *((char *)((void*)&v0 + 3)));
    v4 = _INSERT(0, 0, *((char *)((void*)&v0 + 2)));
    return sub_1033c820(a0, a1, a2, a3, v4, v3, 0, 0, v0, &v1);
}
```

## `sub_1033b3f0` `0x1033b3f0`

_43 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1033b3f0(char *iter, unsigned int a1, char *a2)
{
    unsigned int v0;  // eax

    for (; a1 > 0; iter += 1)
    {
        *(iter) = *(a2);
        a1 -= 1;
    }
    return v0;
}
```

## `sub_1033b420` `0x1033b420`

_45 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1033b420(unsigned short *iter, unsigned int a1, unsigned short *a2)
{
    unsigned int v0;  // eax

    for (; a1 > 0; iter += 1)
    {
        *(iter) = *(a2);
        a1 -= 1;
    }
    return v0;
}
```

## `sub_1033b450` `0x1033b450`

_61 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1033b450(int a0, unsigned int a1, int a2)
{
    unsigned int v0;  // [bp-0xc]
    int v1;  // [bp-0x8]

    v1 = a1 - a0;
    v0 = a2 + v1;
    if (v1 > 0)
        sub_10353626(a2, v1, a0, v1);
    return v0;
}
```

## `sub_1033b490` `0x1033b490`

_66 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1033b490(int a0, unsigned int a1, int a2)
{
    int v2;  // eax
    unsigned int v0;  // [bp-0xc]
    int v1;  // [bp-0x8]

    v2 = a1 - a0;
    v1 = v2 >> 1;
    v0 = a2 + v1 * 2;
    if (v2 >> 1)
        sub_10353626(a2, v1 * 2, a0, v1 * 2);
    return v0;
}
```

## `sub_1033b4e0` `0x1033b4e0`

_720 bytes. (leaf/helper — see body)_

```c
int sub_1033b4e0(int a0, int a1, int a2, int a3, unsigned int a4, char a5)
{
    int v1;  // edx
    int v2;  // eax
    int v11;  // eax
    int v12;  // ecx
    int v13;  // edx
    int v14;  // eax
    int v15;  // ecx
    int v16;  // edx
    int v17;  // eax
    int v18;  // ecx
    int v19;  // edx
    int v20;  // eax
    int v3;  // ecx
    int v21;  // ecx
    int v22;  // edx
    int v4;  // edx
    int v5;  // eax
    int v6;  // ecx
    int v7;  // edx
    int v8;  // eax
    int v9;  // ecx
    int v10;  // edx
    char v0;  // [bp-0x6]

    switch (a1)
    {
    case 0:
        v1 = _INSERT(0, 0, a5);
        return sub_1033cb40(a0, a2, a3, 0, v1, 1);
    case 1:
        v2 = _INSERT(a1, 0, a5);
        return sub_1033cb70(a0, a2, a3, 0, v2, 1);
    case 2:
        v3 = _INSERT(a1, 0, a5);
        return sub_1033cba0(a0, a2, a3, 0, v3, 1);
    case 3:
        v4 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v4, 1);
    case 4:
        v5 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v5, 1);
    case 5:
        v6 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v6, 1);
    case 6:
        v7 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v7, 1);
    case 7:
        v8 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v8, 1);
    case 8:
        v9 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v9, 1);
    case 9:
        v10 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v10, 1);
    case 10:
        v11 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v11, 1);
    case 11:
        v12 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v12, 1);
    case 12:
        v13 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v13, 1);
    case 13:
        v14 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v14, 1);
    case 14:
        v15 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v15, 1);
    case 15:
        v16 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v16, 1);
    case 16:
        v17 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v17, 1);
    case 17:
        v18 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v18, 1);
    case 18:
        v19 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v19, 1);
    case 19:
        v20 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v20, 1);
    default:
        v21 = _INSERT(0, 0, a5);
        v22 = _INSERT(0, 0, v0);
        return sub_1033ce00(a0, a1, a2, a3, v22, v21, 0, 0);
    }
}
```

## `sub_1033b800` `0x1033b800`

_720 bytes. (leaf/helper — see body)_

```c
int sub_1033b800(int a0, int a1, int a2, int a3, unsigned int a4, char a5)
{
    int v1;  // edx
    int v2;  // eax
    int v11;  // eax
    int v12;  // ecx
    int v13;  // edx
    int v14;  // eax
    int v15;  // ecx
    int v16;  // edx
    int v17;  // eax
    int v18;  // ecx
    int v19;  // edx
    int v20;  // eax
    int v3;  // ecx
    int v21;  // ecx
    int v22;  // edx
    int v4;  // edx
    int v5;  // eax
    int v6;  // ecx
    int v7;  // edx
    int v8;  // eax
    int v9;  // ecx
    int v10;  // edx
    char v0;  // [bp-0x6]

    switch (a1)
    {
    case 0:
        v1 = _INSERT(0, 0, a5);
        return sub_1033cbd0(a0, a2, a3, 0, v1, 1);
    case 1:
        v2 = _INSERT(a1, 0, a5);
        return sub_1033cc00(a0, a2, a3, 0, v2, 1);
    case 2:
        v3 = _INSERT(a1, 0, a5);
        return sub_1033cc30(a0, a2, a3, 0, v3, 1);
    case 3:
        v4 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v4, 1);
    case 4:
        v5 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v5, 1);
    case 5:
        v6 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v6, 1);
    case 6:
        v7 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v7, 1);
    case 7:
        v8 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v8, 1);
    case 8:
        v9 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v9, 1);
    case 9:
        v10 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v10, 1);
    case 10:
        v11 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v11, 1);
    case 11:
        v12 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v12, 1);
    case 12:
        v13 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v13, 1);
    case 13:
        v14 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v14, 1);
    case 14:
        v15 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v15, 1);
    case 15:
        v16 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v16, 1);
    case 16:
        v17 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v17, 1);
    case 17:
        v18 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v18, 1);
    case 18:
        v19 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v19, 1);
    case 19:
        v20 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v20, 1);
    default:
        v21 = _INSERT(0, 0, a5);
        v22 = _INSERT(0, 0, v0);
        return sub_1033ce00(a0, a1, a2, a3, v22, v21, 0, 0);
    }
}
```

## `sub_1033bb20` `0x1033bb20`

_7 bytes. (leaf/helper — see body)_

```c
char sub_1033bb20(void)
{
    return 1;
}
```

## `sub_1033bb30` `0x1033bb30`

_98 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
} struct_0;

extern unsigned int g_1038e180;
extern char g_10390948;

struct_0 * sub_1033bb30(struct_0 *a0, unsigned int a1)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4135
    unsigned int v8;  // eax
    unsigned long v9;  // 4151
    unsigned long v10;  // 4140
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
    sub_1033bba0(g_1038e180 ^ &v2, a0, v8, sub_1036fac8, -1, &v3);
    *((char **)&a0->padding_0[0]) = &g_10390948;
    a0->field_c = a1;
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v10) = v8;
    return a0;
}
```

## `sub_1033bba0` `0x1033bba0`

_43 bytes. (leaf/helper — see body)_

```c
extern char g_1039095c;

unsigned int [3] sub_1033bba0(unsigned int *idx)
{
    *(idx) = &g_1039095c;
    idx[1] = 1;
    idx[2] = 1;
    return idx;
}
```

## `sub_1033bbd0` `0x1033bbd0`

_20 bytes. (leaf/helper — see body)_

```c
extern char g_1039095c;

int sub_1033bbd0(unsigned int a0)
{
    *((char **)a0) = &g_1039095c;
    return a0;
}
```

## `sub_1033bbf0` `0x1033bbf0`

_57 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

struct_1 ** sub_1033bbf0(struct_1 **a0)
{
    struct_1 **v0;  // [bp-0x14], Other Possible Types: unsigned int

    if (!a0)
    {
        v0 = 0;
        return a0;
    }
    v0 = *(a0)->field_0(1);
    return v0;
}
```

## `sub_1033bc30` `0x1033bc30`

_44 bytes. (leaf/helper — see body)_

```c
int sub_1033bc30(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_1033bbd0(v0);
    if (((char)a1 & 1))
        sub_10350abd(v0);
    return v0;
}
```

## `sub_1033bc60` `0x1033bc60`

_26 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    int field_c;
} struct_0;

int sub_1033bc60(struct_0 *a0)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_1033be10(a0->field_c, a0, &v1);
}
```

## `sub_1033bc80` `0x1033bc80`

_98 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
} struct_0;

extern unsigned int g_1038e180;
extern char g_10390970;

struct_0 * sub_1033bc80(struct_0 *a0, unsigned int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4135
    unsigned long v10;  // 4151
    unsigned long v11;  // 4140
    unsigned int v0;  // [bp-0x18]
    struct_0 *v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036faf8;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_1033bba0(v1);
    *((char **)&v1->padding_0[0]) = &g_10390970;
    v1->field_c = a1;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_1033bcf0` `0x1033bcf0`

_26 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    int field_c;
} struct_0;

int sub_1033bcf0(struct_0 *a0)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_1033be50(a0->field_c, a0, &v1);
}
```

## `sub_1033bd10` `0x1033bd10`

_44 bytes. (leaf/helper — see body)_

```c
int sub_1033bd10(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1033bd70(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_1033bd40` `0x1033bd40`

_44 bytes. (leaf/helper — see body)_

```c
int sub_1033bd40(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1033bdc0(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_1033bd70` `0x1033bd70`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1033bd70(unsigned int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4137
    unsigned long v11;  // 4153
    int v12;  // eax
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036fb28;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    v4 = 0;
    v4 = 4294967295;
    v12 = sub_1033bbd0(v1);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_1033bdc0` `0x1033bdc0`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1033bdc0(unsigned int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4137
    unsigned long v11;  // 4153
    int v12;  // eax
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036fb58;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    v4 = 0;
    v4 = 4294967295;
    v12 = sub_1033bbd0(v1);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_1033be10` `0x1033be10`

_50 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1033be10(unsigned int a0)
{
    unsigned int v0;  // [bp-0x10]

    if (!a0)
    {
        v0 = 0;
        return a0;
    }
    v0 = sub_1033cc60(1);
    return v0;
}
```

## `sub_1033be50` `0x1033be50`

_50 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1033be50(unsigned int a0)
{
    unsigned int v0;  // [bp-0x10]

    if (!a0)
    {
        v0 = 0;
        return a0;
    }
    v0 = sub_1033cc90(1);
    return v0;
}
```

## `sub_1033be90` `0x1033be90`

_720 bytes. (leaf/helper — see body)_

```c
int sub_1033be90(int a0, int a1, int a2, int a3, unsigned int a4, char a5)
{
    int v1;  // edx
    int v2;  // eax
    int v11;  // eax
    int v12;  // ecx
    int v13;  // edx
    int v14;  // eax
    int v15;  // ecx
    int v16;  // edx
    int v17;  // eax
    int v18;  // ecx
    int v19;  // edx
    int v20;  // eax
    int v3;  // ecx
    int v21;  // ecx
    int v22;  // edx
    int v4;  // edx
    int v5;  // eax
    int v6;  // ecx
    int v7;  // edx
    int v8;  // eax
    int v9;  // ecx
    int v10;  // edx
    char v0;  // [bp-0x6]

    switch (a1)
    {
    case 0:
        v1 = _INSERT(0, 0, a5);
        return sub_1033cda0(a0, a2, a3, 0, v1, 1);
    case 1:
        v2 = _INSERT(a1, 0, a5);
        return sub_1033cdd0(a0, a2, a3, 0, v2, 1);
    case 2:
        v3 = _INSERT(a1, 0, a5);
        return sub_1033cdd0(a0, a2, a3, 0, v3, 1);
    case 3:
        v4 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v4, 1);
    case 4:
        v5 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v5, 1);
    case 5:
        v6 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v6, 1);
    case 6:
        v7 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v7, 1);
    case 7:
        v8 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v8, 1);
    case 8:
        v9 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v9, 1);
    case 9:
        v10 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v10, 1);
    case 10:
        v11 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v11, 1);
    case 11:
        v12 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v12, 1);
    case 12:
        v13 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v13, 1);
    case 13:
        v14 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v14, 1);
    case 14:
        v15 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v15, 1);
    case 15:
        v16 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v16, 1);
    case 16:
        v17 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v17, 1);
    case 17:
        v18 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v18, 1);
    case 18:
        v19 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v19, 1);
    case 19:
        v20 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v20, 1);
    default:
        v21 = _INSERT(0, 0, a5);
        v22 = _INSERT(0, 0, v0);
        return sub_1033ce00(a0, a1, a2, a3, v22, v21, 0, 0);
    }
}
```

## `sub_1033c1b0` `0x1033c1b0`

_720 bytes. (leaf/helper — see body)_

```c
int sub_1033c1b0(int a0, int a1, int a2, int a3, unsigned int a4, char a5)
{
    int v1;  // edx
    int v2;  // eax
    int v11;  // eax
    int v12;  // ecx
    int v13;  // edx
    int v14;  // eax
    int v15;  // ecx
    int v16;  // edx
    int v17;  // eax
    int v18;  // ecx
    int v19;  // edx
    int v20;  // eax
    int v3;  // ecx
    int v21;  // ecx
    int v22;  // edx
    int v4;  // edx
    int v5;  // eax
    int v6;  // ecx
    int v7;  // edx
    int v8;  // eax
    int v9;  // ecx
    int v10;  // edx
    char v0;  // [bp-0x6]

    switch (a1)
    {
    case 0:
        v1 = _INSERT(0, 0, a5);
        return sub_1033cdd0(a0, a2, a3, 0, v1, 1);
    case 1:
        v2 = _INSERT(a1, 0, a5);
        return sub_1033ce10(a0, a2, a3, 0, v2, 1);
    case 2:
        v3 = _INSERT(a1, 0, a5);
        return sub_1033cdd0(a0, a2, a3, 0, v3, 1);
    case 3:
        v4 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v4, 1);
    case 4:
        v5 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v5, 1);
    case 5:
        v6 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v6, 1);
    case 6:
        v7 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v7, 1);
    case 7:
        v8 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v8, 1);
    case 8:
        v9 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v9, 1);
    case 9:
        v10 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v10, 1);
    case 10:
        v11 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v11, 1);
    case 11:
        v12 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v12, 1);
    case 12:
        v13 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v13, 1);
    case 13:
        v14 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v14, 1);
    case 14:
        v15 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v15, 1);
    case 15:
        v16 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v16, 1);
    case 16:
        v17 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v17, 1);
    case 17:
        v18 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v18, 1);
    case 18:
        v19 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v19, 1);
    case 19:
        v20 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v20, 1);
    default:
        v21 = _INSERT(0, 0, a5);
        v22 = _INSERT(0, 0, v0);
        return sub_1033ce00(a0, a1, a2, a3, v22, v21, 0, 0);
    }
}
```

## `sub_1033c4d0` `0x1033c4d0`

_720 bytes. (leaf/helper — see body)_

```c
int sub_1033c4d0(int a0, int a1, int a2, int a3, unsigned int a4, char a5)
{
    int v1;  // edx
    int v2;  // eax
    int v11;  // eax
    int v12;  // ecx
    int v13;  // edx
    int v14;  // eax
    int v15;  // ecx
    int v16;  // edx
    int v17;  // eax
    int v18;  // ecx
    int v19;  // edx
    int v20;  // eax
    int v3;  // ecx
    int v21;  // ecx
    int v22;  // edx
    int v4;  // edx
    int v5;  // eax
    int v6;  // ecx
    int v7;  // edx
    int v8;  // eax
    int v9;  // ecx
    int v10;  // edx
    char v0;  // [bp-0x6]

    switch (a1)
    {
    case 0:
        v1 = _INSERT(0, 0, a5);
        return sub_1033cdd0(a0, a2, a3, 0, v1, 1);
    case 1:
        v2 = _INSERT(a1, 0, a5);
        return sub_1033cdd0(a0, a2, a3, 0, v2, 1);
    case 2:
        v3 = _INSERT(a1, 0, a5);
        return sub_1033ce40(a0, a2, a3, 0, v3, 1);
    case 3:
        v4 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v4, 1);
    case 4:
        v5 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v5, 1);
    case 5:
        v6 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v6, 1);
    case 6:
        v7 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v7, 1);
    case 7:
        v8 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v8, 1);
    case 8:
        v9 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v9, 1);
    case 9:
        v10 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v10, 1);
    case 10:
        v11 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v11, 1);
    case 11:
        v12 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v12, 1);
    case 12:
        v13 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v13, 1);
    case 13:
        v14 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v14, 1);
    case 14:
        v15 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v15, 1);
    case 15:
        v16 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v16, 1);
    case 16:
        v17 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v17, 1);
    case 17:
        v18 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v18, 1);
    case 18:
        v19 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v19, 1);
    case 19:
        v20 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v20, 1);
    default:
        v21 = _INSERT(0, 0, a5);
        v22 = _INSERT(0, 0, v0);
        return sub_1033ce00(a0, a1, a2, a3, v22, v21, 0, 0);
    }
}
```

## `sub_1033c7f0` `0x1033c7f0`

_41 bytes. (leaf/helper — see body)_

```c
int sub_1033c7f0(int a0, int a1, int a2, int a3)
{
    unsigned int v2;  // ecx
    int v3;  // ecx
    int v0;  // [bp-0x8], Other Possible Types: unsigned int
    char v1;  // [bp+0x0]

    v0 = v2;
    v0 = _INSERT(v2, 3, 0);
    v3 = _INSERT(v2, 0, *((char *)((void*)&v0 + 3)));
    return sub_1033ce70(a0, a1, a2, a3, v3, v0, &v1);
}
```

## `sub_1033c820` `0x1033c820`

_720 bytes. (leaf/helper — see body)_

```c
int sub_1033c820(int a0, int a1, int a2, int a3, unsigned int a4, char a5)
{
    int v4;  // eax
    int v13;  // eax
    int v14;  // ecx
    int v15;  // edx
    int v16;  // eax
    int v17;  // ecx
    int v18;  // edx
    int v19;  // eax
    int v20;  // ecx
    int v21;  // edx
    int v22;  // eax
    int v5;  // ecx
    int v23;  // ecx
    int v24;  // edx
    int v6;  // edx
    int v7;  // eax
    int v8;  // ecx
    int v9;  // edx
    int v10;  // eax
    int v11;  // ecx
    int v12;  // edx
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x6]

    switch (a1)
    {
    case 0:
        v1 = 1;
        *((char *)&v0) = a5;
        return sub_1033c7f0(a0, a2, a3, 0);
    case 1:
        v4 = _INSERT(a1, 0, a5);
        return sub_1033ce90(a0, a2, a3, 0, v4, 1);
    case 2:
        v5 = _INSERT(a1, 0, a5);
        return sub_1033ce90(a0, a2, a3, 0, v5, 1);
    case 3:
        v6 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v6, 1);
    case 4:
        v7 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v7, 1);
    case 5:
        v8 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v8, 1);
    case 6:
        v9 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v9, 1);
    case 7:
        v10 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v10, 1);
    case 8:
        v11 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v11, 1);
    case 9:
        v12 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v12, 1);
    case 10:
        v13 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v13, 1);
    case 11:
        v14 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v14, 1);
    case 12:
        v15 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v15, 1);
    case 13:
        v16 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v16, 1);
    case 14:
        v17 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v17, 1);
    case 15:
        v18 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v18, 1);
    case 16:
        v19 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v19, 1);
    case 17:
        v20 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v20, 1);
    case 18:
        v21 = _INSERT(0, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v21, 1);
    case 19:
        v22 = _INSERT(a1, 0, a5);
        return sub_1033ce00(a0, a2, a3, 0, v22, 1);
    default:
        v23 = _INSERT(0, 0, a5);
        v24 = _INSERT(0, 0, v2);
        return sub_1033ce00(a0, a1, a2, a3, v24, v23, 0, 0);
    }
}
```

## `sub_1033cb40` `0x1033cb40`

_41 bytes. (leaf/helper — see body)_

```c
int sub_1033cb40(int a0, int a1, int a2, int a3)
{
    unsigned int v2;  // ecx
    int v3;  // ecx
    int v0;  // [bp-0x8], Other Possible Types: unsigned int
    char v1;  // [bp+0x0]

    v0 = v2;
    v0 = _INSERT(v2, 3, 0);
    v3 = _INSERT(v2, 0, *((char *)((void*)&v0 + 3)));
    return sub_1033cec0(a0, a1, a2, a3, v3, v0, &v1);
}
```

## `sub_1033cb70` `0x1033cb70`

_41 bytes. (leaf/helper — see body)_

```c
int sub_1033cb70(int a0, int a1, int a2, int a3)
{
    unsigned int v2;  // ecx
    int v3;  // ecx
    int v0;  // [bp-0x8], Other Possible Types: unsigned int
    char v1;  // [bp+0x0]

    v0 = v2;
    v0 = _INSERT(v2, 3, 0);
    v3 = _INSERT(v2, 0, *((char *)((void*)&v0 + 3)));
    return sub_1033cee0(a0, a1, a2, a3, v3, v0, &v1);
}
```

## `sub_1033cba0` `0x1033cba0`

_41 bytes. (leaf/helper — see body)_

```c
int sub_1033cba0(int a0, int a1, int a2, int a3)
{
    unsigned int v2;  // ecx
    int v3;  // ecx
    int v0;  // [bp-0x8], Other Possible Types: unsigned int
    char v1;  // [bp+0x0]

    v0 = v2;
    v0 = _INSERT(v2, 3, 0);
    v3 = _INSERT(v2, 0, *((char *)((void*)&v0 + 3)));
    return sub_1033cf00(a0, a1, a2, a3, v3, v0, &v1);
}
```

## `sub_1033cbd0` `0x1033cbd0`

_41 bytes. (leaf/helper — see body)_

```c
int sub_1033cbd0(int a0, int a1, int a2, int a3)
{
    unsigned int v2;  // ecx
    int v3;  // ecx
    int v0;  // [bp-0x8], Other Possible Types: unsigned int
    char v1;  // [bp+0x0]

    v0 = v2;
    v0 = _INSERT(v2, 3, 0);
    v3 = _INSERT(v2, 0, *((char *)((void*)&v0 + 3)));
    return sub_1033cf20(a0, a1, a2, a3, v3, v0, &v1);
}
```

## `sub_1033cc00` `0x1033cc00`

_41 bytes. (leaf/helper — see body)_

```c
int sub_1033cc00(int a0, int a1, int a2, int a3)
{
    unsigned int v2;  // ecx
    int v3;  // ecx
    int v0;  // [bp-0x8], Other Possible Types: unsigned int
    char v1;  // [bp+0x0]

    v0 = v2;
    v0 = _INSERT(v2, 3, 0);
    v3 = _INSERT(v2, 0, *((char *)((void*)&v0 + 3)));
    return sub_1033cf40(a0, a1, a2, a3, v3, v0, &v1);
}
```

## `sub_1033cc30` `0x1033cc30`

_41 bytes. (leaf/helper — see body)_

```c
int sub_1033cc30(int a0, int a1, int a2, int a3)
{
    unsigned int v2;  // ecx
    int v3;  // ecx
    int v0;  // [bp-0x8], Other Possible Types: unsigned int
    char v1;  // [bp+0x0]

    v0 = v2;
    v0 = _INSERT(v2, 3, 0);
    v3 = _INSERT(v2, 0, *((char *)((void*)&v0 + 3)));
    return sub_1033cf60(a0, a1, a2, a3, v3, v0, &v1);
}
```

## `sub_1033cc60` `0x1033cc60`

_44 bytes. (leaf/helper — see body)_

```c
int sub_1033cc60(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1033ccc0(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_1033cc90` `0x1033cc90`

_44 bytes. (leaf/helper — see body)_

```c
int sub_1033cc90(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1033cd30(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_1033ccc0` `0x1033ccc0`

_105 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

void sub_1033ccc0(int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4140
    unsigned long v11;  // 4156
    unsigned long v12;  // 4113
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036fb9e;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    v4 = 2;
    v4 = 1;
    sub_10314610(v1 + 56);
    v4 = 0;
    sub_1032dbe0(v1 + 28);
    v4 = 4294967295;
    sub_1032dbe0(v1);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v2;
    return;
}
```

## `sub_1033cd30` `0x1033cd30`

_105 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

void sub_1033cd30(int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4140
    unsigned long v11;  // 4156
    unsigned long v12;  // 4113
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036fbde;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    v4 = 2;
    v4 = 1;
    sub_10314610(v1 + 56);
    v4 = 0;
    sub_103257d0(v1 + 28);
    v4 = 4294967295;
    sub_103257d0(v1);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v2;
    return;
}
```

## `sub_1033cda0` `0x1033cda0`

_41 bytes. (leaf/helper — see body)_

```c
int sub_1033cda0(int a0, int a1, int a2, int a3)
{
    unsigned int v2;  // ecx
    int v3;  // ecx
    int v0;  // [bp-0x8], Other Possible Types: unsigned int
    char v1;  // [bp+0x0]

    v0 = v2;
    v0 = _INSERT(v2, 3, 0);
    v3 = _INSERT(v2, 0, *((char *)((void*)&v0 + 3)));
    return sub_1033cf80(a0, a1, a2, a3, v3, v0, &v1);
}
```

## `sub_1033cdd0` `0x1033cdd0`

_41 bytes. (leaf/helper — see body)_

```c
int sub_1033cdd0(int a0, int a1, int a2, int a3)
{
    unsigned int v2;  // ecx
    int v3;  // ecx
    int v0;  // [bp-0x8], Other Possible Types: unsigned int
    char v1;  // [bp+0x0]

    v0 = v2;
    v0 = _INSERT(v2, 3, 0);
    v3 = _INSERT(v2, 0, *((char *)((void*)&v0 + 3)));
    return sub_1033cfa0(a0, a1, a2, a3, v3, v0, &v1);
}
```

## `sub_1033ce00` `0x1033ce00`

_10 bytes. (leaf/helper — see body)_

```c
void sub_1033ce00(void)
{
    char v0;  // [bp+0x0]

    sub_1033cfc0(&v0);
    return;
}
```

## `sub_1033ce10` `0x1033ce10`

_41 bytes. (leaf/helper — see body)_

```c
int sub_1033ce10(int a0, int a1, int a2, int a3)
{
    unsigned int v2;  // ecx
    int v3;  // ecx
    int v0;  // [bp-0x8], Other Possible Types: unsigned int
    char v1;  // [bp+0x0]

    v0 = v2;
    v0 = _INSERT(v2, 3, 0);
    v3 = _INSERT(v2, 0, *((char *)((void*)&v0 + 3)));
    return sub_1033cfd0(a0, a1, a2, a3, v3, v0, &v1);
}
```

## `sub_1033ce40` `0x1033ce40`

_41 bytes. (leaf/helper — see body)_

```c
int sub_1033ce40(int a0, int a1, int a2, int a3)
{
    unsigned int v2;  // ecx
    int v3;  // ecx
    int v0;  // [bp-0x8], Other Possible Types: unsigned int
    char v1;  // [bp+0x0]

    v0 = v2;
    v0 = _INSERT(v2, 3, 0);
    v3 = _INSERT(v2, 0, *((char *)((void*)&v0 + 3)));
    return sub_1033cff0(a0, a1, a2, a3, v3, v0, &v1);
}
```

## `sub_1033ce70` `0x1033ce70`

_28 bytes. (leaf/helper — see body)_

```c
int sub_1033ce70(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v0;  // [bp-0x8]

    v0 = 1;
    return sub_1033d030(sub_10337e90(a2));
}
```

## `sub_1033ce90` `0x1033ce90`

_41 bytes. (leaf/helper — see body)_

```c
int sub_1033ce90(int a0, int a1, int a2, int a3)
{
    unsigned int v2;  // ecx
    int v3;  // ecx
    int v0;  // [bp-0x8], Other Possible Types: unsigned int
    char v1;  // [bp+0x0]

    v0 = v2;
    v0 = _INSERT(v2, 3, 0);
    v3 = _INSERT(v2, 0, *((char *)((void*)&v0 + 3)));
    return sub_1033d050(a0, a1, a2, a3, v3, v0, &v1);
}
```

## `sub_1033cec0` `0x1033cec0`

_28 bytes. (leaf/helper — see body)_

```c
int sub_1033cec0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v0;  // [bp-0x8]

    v0 = 1;
    return sub_1033d070(sub_10337e90(a2));
}
```

## `sub_1033cee0` `0x1033cee0`

_28 bytes. (leaf/helper — see body)_

```c
int sub_1033cee0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v0;  // [bp-0x8]

    v0 = 1;
    return sub_1033d090(sub_10337e90(a2));
}
```

## `sub_1033cf00` `0x1033cf00`

_28 bytes. (leaf/helper — see body)_

```c
int sub_1033cf00(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v0;  // [bp-0x8]

    v0 = 1;
    return sub_1033d0b0(sub_10337e90(a2));
}
```

## `sub_1033cf20` `0x1033cf20`

_28 bytes. (leaf/helper — see body)_

```c
int sub_1033cf20(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v0;  // [bp-0x8]

    v0 = 1;
    return sub_1033d0d0(sub_10337e90(a2));
}
```

## `sub_1033cf40` `0x1033cf40`

_28 bytes. (leaf/helper — see body)_

```c
int sub_1033cf40(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v0;  // [bp-0x8]

    v0 = 1;
    return sub_1033d100(sub_10337e90(a2));
}
```

## `sub_1033cf60` `0x1033cf60`

_28 bytes. (leaf/helper — see body)_

```c
int sub_1033cf60(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v0;  // [bp-0x8]

    v0 = 1;
    return sub_1033d130(sub_10337e90(a2));
}
```

## `sub_1033cf80` `0x1033cf80`

_28 bytes. (leaf/helper — see body)_

```c
int sub_1033cf80(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v0;  // [bp-0x8]

    v0 = 1;
    return sub_1033d180(sub_10337e90(a2));
}
```

## `sub_1033cfa0` `0x1033cfa0`

_28 bytes. (leaf/helper — see body)_

```c
int sub_1033cfa0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v0;  // [bp-0x8]

    v0 = 1;
    return sub_1033d1a0(sub_10337e90(a2));
}
```

## `sub_1033cfc0` `0x1033cfc0`

_10 bytes. (leaf/helper — see body)_

```c
void sub_1033cfc0(void)
{
    sub_10334530();
    return;
}
```

## `sub_1033cfd0` `0x1033cfd0`

_28 bytes. (leaf/helper — see body)_

```c
int sub_1033cfd0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v0;  // [bp-0x8]

    v0 = 1;
    return sub_1033d1c0(sub_10337e90(a2));
}
```

## `sub_1033cff0` `0x1033cff0`

_28 bytes. (leaf/helper — see body)_

```c
int sub_1033cff0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v0;  // [bp-0x8]

    v0 = 1;
    return sub_1033d1e0(sub_10337e90(a2));
}
```

## `sub_1033d010` `0x1033d010`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1033d010(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_1033d4e0(a1, a0, &v1);
}
```

## `sub_1033d030` `0x1033d030`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1033d030(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_1033d160(a1, a0, &v1);
}
```

