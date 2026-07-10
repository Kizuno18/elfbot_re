# elfbot.dll decompiled — jiru 0x1031a88a..0x1031ba90

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1031a88a` `0x1031a88a`

_30 bytes. (leaf/helper — see body)_

```c
int sub_1031a88a(void)
{
    unsigned int v1;  // [bp+0xffff0]
    unsigned int v2;  // [bp+0x100000]
    unsigned int v3;  // [bp+0x10000c]

    sub_10315800(v3);
    v1 |= 1;
    v2 = 0;
    return sub_1031a8b7;
}
```

## `sub_1031a8a8` `0x1031a8a8`

_6 bytes. (leaf/helper — see body)_

```c
int sub_1031a8a8(void)
{
    return sub_1031a8ae;
}
```

## `sub_1031a8ae` `0x1031a8ae`

_11 bytes. (leaf/helper — see body)_

```c
void sub_1031a8ae(void)
{
    unsigned int v1;  // [bp+0x100000]

    v1 = 0;
}
```

## `sub_1031a8b7` `0x1031a8b7`

_5 bytes. (leaf/helper — see body)_

```c
int sub_1031a8b7(void)
{
}
```

## `sub_1031a8be` `0x1031a8be`

_3 bytes. (leaf/helper — see body)_

```c
int sub_1031a8be(void)
{
}
```

## `sub_1031a8e0` `0x1031a8e0`

_104 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1031a8e0(unsigned int a0, unsigned int a1, int a2)
{
    unsigned long v11;  // ldt
    unsigned long v12;  // gdt
    unsigned short v13;  // fs
    unsigned long v14;  // 4150
    unsigned int v15;  // eax
    unsigned long v16;  // 4174
    unsigned long v17;  // 4119
    unsigned int v0;  // [bp-0x28]
    int v1;  // [bp-0x24]
    int v2;  // [bp-0x20]
    int v3;  // [bp-0x1c]
    unsigned int v4;  // [bp-0x18]
    unsigned int v5;  // [bp-0x14]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0x8]
    char v8;  // [bp-0x4]
    char v9;  // [bp+0x0]
    char v10;  // [bp+0x8]

    v7 = 4294967295;
    v14 = _ccall(v11, v12, (unsigned int)v13, 0);
    v15 = *((int *)v14);
    v6 = *((int *)v14);
    v5 = a0;
    v4 = a0;
    v0 = g_1038e180 ^ &v8;
    v16 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int **)v16) = &v6;
    sub_1031ab20(a2, &v10, g_1038e180 ^ &v8, v1, v2, v3, 0, &v0, v15, sub_1036b479, 1, &v9);
    v4 = 1;
    v17 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int *)v17) = v15;
    return a2;
}
```

## `sub_1031a936` `0x1031a936`

_30 bytes. (leaf/helper — see body)_

```c
int sub_1031a936(void)
{
    unsigned int v1;  // [bp+0xffff0]
    unsigned int v2;  // [bp+0x100000]
    unsigned int v3;  // [bp+0x10000c]

    sub_10315800(v3);
    v1 |= 1;
    v2 = 0;
    return sub_1031a98e;
}
```

## `sub_1031a954` `0x1031a954`

_6 bytes. (leaf/helper — see body)_

```c
int sub_1031a954(void)
{
    return sub_1031a97e;
}
```

## `sub_1031a95a` `0x1031a95a`

_30 bytes. (leaf/helper — see body)_

```c
int sub_1031a95a(void)
{
    unsigned int v1;  // [bp+0xffff0]
    unsigned int v2;  // [bp+0x100000]
    unsigned int v3;  // [bp+0x10000c]

    sub_10315800(v3);
    v1 |= 1;
    v2 = 0;
    return sub_1031a987;
}
```

## `sub_1031a978` `0x1031a978`

_6 bytes. (leaf/helper — see body)_

```c
int sub_1031a978(void)
{
    return sub_1031a97e;
}
```

## `sub_1031a97e` `0x1031a97e`

_11 bytes. (leaf/helper — see body)_

```c
void sub_1031a97e(void)
{
    unsigned int v1;  // [bp+0x100000]

    v1 = 0;
}
```

## `sub_1031a987` `0x1031a987`

_5 bytes. (leaf/helper — see body)_

```c
int sub_1031a987(void)
{
}
```

## `sub_1031a98e` `0x1031a98e`

_3 bytes. (leaf/helper — see body)_

```c
int sub_1031a98e(void)
{
}
```

## `sub_1031a9b0` `0x1031a9b0`

_44 bytes. (leaf/helper — see body)_

```c
char sub_1031a9b0(int a0, int a1, int a2, int a3)
{
    int v2;  // ecx
    int v3;  // eax
    char v0;  // [bp-0x5]
    char v1;  // [bp+0x0]

    v0 = sub_10337970(v2, &v1);
    v3 = _INSERT(v0, 0, v0);
    return sub_1031aba0(a0, a1, a2, a3, v3);
}
```

## `sub_1031a9e0` `0x1031a9e0`

_52 bytes. (leaf/helper — see body)_

```c
int sub_1031a9e0(int *a0, int a1)
{
    int v1;  // eax
    int *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    v1 = sub_1031aa20(a1, sub_1031a280(v0 + 1));
    return sub_1031ac10(*(v0), v1);
}
```

## `sub_1031aa20` `0x1031aa20`

_43 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1031aa20(unsigned int *a0)
{
    unsigned int *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return (!(char)sub_1031aa50(a0, &v1) ? *(a0) : -(*(a0) + 1));
}
```

## `sub_1031aa50` `0x1031aa50`

_24 bytes. (leaf/helper — see body)_

```c
int sub_1031aa50(int *a0)
{
    return _INSERT(a0, 0, *(a0) < 0);
}
```

## `sub_1031aa70` `0x1031aa70`

_46 bytes. (leaf/helper — see body)_

```c
int sub_1031aa70(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v1 = a0;
    v1 = a0;
    v0 = a1;
    return sub_1031ac50(sub_1031ac70(sub_1031a280(v1 + 4)));
}
```

## `sub_1031aaa0` `0x1031aaa0`

_127 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1031aaa0(int a0, int *a1)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4137
    unsigned long v12;  // 4154
    unsigned long v13;  // 4135
    unsigned int v0;  // [bp-0x34]
    char v1;  // [bp-0x30]
    int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036b4b9;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v2 = g_1038e180 ^ &v7;
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    v3 = 20;
    sub_10334530(v2, 0);
    sub_1031ad00(a0, *(a1), &v1, 20);
    v6 = 0;
    v0 = 1;
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v13) = v4;
    return sub_10351225();
}
```

## `sub_1031ab20` `0x1031ab20`

_127 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1031ab20(int a0, int *a1)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4137
    unsigned long v12;  // 4154
    unsigned long v13;  // 4135
    unsigned int v0;  // [bp-0x30]
    char v1;  // [bp-0x2c]
    int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036b4f9;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v2 = g_1038e180 ^ &v7;
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    v3 = 19;
    sub_10334530(v2, 0);
    sub_1031ae20(a0, *(a1), &v1, 19);
    v6 = 0;
    v0 = 1;
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v13) = v4;
    return sub_10351225();
}
```

## `sub_1031aba0` `0x1031aba0`

_29 bytes. (leaf/helper — see body)_

```c
int sub_1031aba0(int a0, int a1, int a2, int a3)
{
    char v0;  // [bp+0x0]

    return sub_1031abc0(a0, a1, a2, a3, &v0);
}
```

## `sub_1031abc0` `0x1031abc0`

_32 bytes. (leaf/helper — see body)_

```c
int sub_1031abc0(int a0, int a1, int a2, int a3)
{
    char v0;  // [bp+0x0]

    sub_1031abe0(a0, a1, a2, a3, &v0);
    return a0;
}
```

## `sub_1031abe0` `0x1031abe0`

_33 bytes. (leaf/helper — see body)_

```c
int sub_1031abe0(int a0, unsigned int a1, int a2, unsigned int a3)
{
    char v0;  // [bp+0x0]

    return sub_1035336f(a0, a1 * 2, a2, a3 * 2, &v0);
}
```

## `sub_1031ac10` `0x1031ac10`

_49 bytes. (leaf/helper — see body)_

```c
int sub_1031ac10(int a0, int a1, int a2, int a3)
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
    return sub_1031af40(a0, a1, a2, a3, v4, v3, 0, 0, v0, &v1);
}
```

## `sub_1031ac50` `0x1031ac50`

_21 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_1031ac50(unsigned int *a0, unsigned int a1)
{
    *(a0) = a1;
    return a0;
}
```

## `sub_1031ac70` `0x1031ac70`

_124 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_1031ac70(int a0, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4139
    unsigned long v10;  // 4153
    unsigned long v11;  // 4124
    int v0;  // [bp-0x1c], Other Possible Types: unsigned int
    int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036b531;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = sub_1031acf0(28, a0, g_1038e180 ^ &v5);
    v4 = 0;
    if (v1)
        v0 = sub_103145d0(v1, a1);
    else
        v0 = 0;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return 1;
}
```

## `sub_1031acf0` `0x1031acf0`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1031acf0(unsigned int a0, unsigned int a1)
{
    return a1;
}
```

## `sub_1031ad00` `0x1031ad00`

_279 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c770;
extern unsigned int g_1038c780;
extern unsigned int g_1038e180;

int sub_1031ad00(unsigned int a0, int a1, int a2, unsigned int a3)
{
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // fs
    unsigned long v13;  // 4147
    unsigned long v14;  // 4164
    unsigned long v15;  // 4114
    unsigned int v0;  // [bp-0x58]
    unsigned int v1;  // [bp-0x54]
    unsigned int v2;  // [bp-0x50]
    unsigned int v3[5];  // [bp-0x4c]
    char v4;  // [bp-0x38]
    int v5;  // [bp-0x1c]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    char v8;  // [bp-0x8], Other Possible Types: unsigned int
    char v9;  // [bp-0x4]

    v8 = 4294967295;
    v7 = sub_1036b579;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v6 = *((int *)v13);
    v5 = g_1038e180 ^ &v9;
    v14 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v14) = &v6;
    v2 = 0;
    sub_1031b260(a2, a2 + a3, v5);
    if ((char)sub_1031b2c0(a1))
    {
        sub_10315800(&v4);
        v8 = 1;
        if ((char)sub_1031b320(&v4))
        {
            sub_103145d0(a0, &v4);
            v2 |= 1;
            v8 = 0;
            sub_10314610(&v4);
            v15 = _ccall(v10, v11, (unsigned int)v12, 0);
            *((unsigned int *)v15) = v6;
            return sub_10351225();
        }
        v8 = 0;
        sub_10314610(&v4);
    }
    v1 = sub_10312b10(v3, &g_1038c770, &g_1038c780);
    v0 = v1;
    v8 = 2;
    sub_103139f0(v0);
    v8 = 0;
    sub_10312b90(v3);
    sub_10315800(a0);
    v8 = 0;
    v2 |= 1;
    v15 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v15) = v6;
    return sub_10351225();
}
```

## `sub_1031ae20` `0x1031ae20`

_279 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c360;
extern unsigned int g_1038c780;
extern unsigned int g_1038e180;

int sub_1031ae20(unsigned int a0, int a1, int a2, unsigned int a3)
{
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // fs
    unsigned long v13;  // 4147
    unsigned long v14;  // 4164
    unsigned long v15;  // 4114
    unsigned int v0;  // [bp-0x58]
    unsigned int v1;  // [bp-0x54]
    unsigned int v2;  // [bp-0x50]
    unsigned int v3[5];  // [bp-0x4c]
    char v4;  // [bp-0x38]
    int v5;  // [bp-0x1c]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    char v8;  // [bp-0x8], Other Possible Types: unsigned int
    char v9;  // [bp-0x4]

    v8 = 4294967295;
    v7 = sub_1036b5c9;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v6 = *((int *)v13);
    v5 = g_1038e180 ^ &v9;
    v14 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v14) = &v6;
    v2 = 0;
    sub_1031b260(a2, a2 + a3, v5);
    if ((char)sub_1031b290(a1))
    {
        sub_10315800(&v4);
        v8 = 1;
        if ((char)sub_1031b320(&v4))
        {
            sub_103145d0(a0, &v4);
            v2 |= 1;
            v8 = 0;
            sub_10314610(&v4);
            v15 = _ccall(v10, v11, (unsigned int)v12, 0);
            *((unsigned int *)v15) = v6;
            return sub_10351225();
        }
        v8 = 0;
        sub_10314610(&v4);
    }
    v1 = sub_10312b10(v3, &g_1038c360, &g_1038c780);
    v0 = v1;
    v8 = 2;
    sub_103139f0(v0);
    v8 = 0;
    sub_10312b90(v3);
    sub_10315800(a0);
    v8 = 0;
    v2 |= 1;
    v15 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v15) = v6;
    return sub_10351225();
}
```

## `sub_1031af40` `0x1031af40`

_720 bytes. (leaf/helper — see body)_

```c
int sub_1031af40(int a0, int a1, int a2, int a3, unsigned int a4, char a5)
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
        return sub_1031b350(a0, a2, a3, 0, v1, 1);
    case 1:
        v2 = _INSERT(a1, 0, a5);
        return sub_1031b380(a0, a2, a3, 0, v2, 1);
    case 2:
        v3 = _INSERT(a1, 0, a5);
        return sub_1031b3b0(a0, a2, a3, 0, v3, 1);
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

## `sub_1031b260` `0x1031b260`

_33 bytes. (leaf/helper — see body)_

```c
unsigned int [2] sub_1031b260(unsigned int *a0, unsigned int a1, unsigned int a2)
{
    *(a0) = a1;
    a0[1] = a2;
    return a0;
}
```

## `sub_1031b290` `0x1031b290`

_39 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    int field_4;
} struct_0;

char sub_1031b290(struct_0 *a0, int a1)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    a0->field_0 = sub_1031b3e0(a1, a0->field_4, a0, &v1);
    return 1;
}
```

## `sub_1031b2c0` `0x1031b2c0`

_91 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char *field_0;
    int field_4;
} struct_0;

char sub_1031b2c0(struct_0 *a0, int a1)
{
    char v0;  // [bp-0x5]

    a0->field_0 = sub_1031b3e0(sub_1031b5c0(a1, a0->field_4, a0));
    if (a1 < 0)
    {
        a0->field_0 = a0->field_0 + 1;
        v0 = 45;
        sub_103149a0(a0->field_0, &v0);
    }
    return 1;
}
```

## `sub_1031b320` `0x1031b320`

_36 bytes. (leaf/helper — see body)_

```c
char sub_1031b320(int *a0, unsigned int a1)
{
    int v0[2];  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1031b5f0(*(a0), a0[1], a0, &v1);
    return 1;
}
```

## `sub_1031b350` `0x1031b350`

_41 bytes. (leaf/helper — see body)_

```c
int sub_1031b350(int a0, int a1, int a2, int a3)
{
    unsigned int v2;  // ecx
    int v3;  // ecx
    int v0;  // [bp-0x8], Other Possible Types: unsigned int
    char v1;  // [bp+0x0]

    v0 = v2;
    v0 = _INSERT(v2, 3, 0);
    v3 = _INSERT(v2, 0, *((char *)((void*)&v0 + 3)));
    return sub_1031b630(a0, a1, a2, a3, v3, v0, &v1);
}
```

## `sub_1031b380` `0x1031b380`

_41 bytes. (leaf/helper — see body)_

```c
int sub_1031b380(int a0, int a1, int a2, int a3)
{
    unsigned int v2;  // ecx
    int v3;  // ecx
    int v0;  // [bp-0x8], Other Possible Types: unsigned int
    char v1;  // [bp+0x0]

    v0 = v2;
    v0 = _INSERT(v2, 3, 0);
    v3 = _INSERT(v2, 0, *((char *)((void*)&v0 + 3)));
    return sub_1031b650(a0, a1, a2, a3, v3, v0, &v1);
}
```

## `sub_1031b3b0` `0x1031b3b0`

_41 bytes. (leaf/helper — see body)_

```c
int sub_1031b3b0(int a0, int a1, int a2, int a3)
{
    unsigned int v2;  // ecx
    int v3;  // ecx
    int v0;  // [bp-0x8], Other Possible Types: unsigned int
    char v1;  // [bp+0x0]

    v0 = v2;
    v0 = _INSERT(v2, 3, 0);
    v3 = _INSERT(v2, 0, *((char *)((void*)&v0 + 3)));
    return sub_1031b670(a0, a1, a2, a3, v3, v0, &v1);
}
```

## `sub_1031b3e0` `0x1031b3e0`

_480 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

extern unsigned int g_1038e180;

int sub_1031b3e0(unsigned int i, char *iter)
{
    unsigned long v24;  // ldt
    unsigned long v25;  // gdt
    unsigned short v26;  // fs
    unsigned long v27;  // 4136
    unsigned long v28;  // 4153
    unsigned long v29;  // 4118
    unsigned int v0;  // [bp-0x70]
    unsigned int v1;  // [bp-0x6c]
    unsigned int v2;  // [bp-0x68]
    char *v3;  // [bp-0x64]
    char v4[6];  // [bp-0x60]
    char v5;  // [bp-0x5a]
    char v6;  // [bp-0x59]
    unsigned int v7;  // [bp-0x58]
    char v8;  // [bp-0x51]
    unsigned int v9;  // [bp-0x50]
    char v10;  // [bp-0x4a]
    char v11;  // [bp-0x49]
    unsigned int v12;  // [bp-0x48]
    int v13;  // [bp-0x44]
    char v14;  // [bp-0x40]
    struct_0 *v15;  // [bp-0x3c]
    char v16;  // [bp-0x35]
    struct_0 v17;  // [bp-0x34]
    int v18;  // [bp-0x18]
    unsigned int v19;  // [bp-0x14]
    unsigned int v20;  // [bp-0x10]
    unsigned int v21;  // [bp-0xc]
    char v22;  // [bp-0x8], Other Possible Types: unsigned int
    char v23;  // [bp-0x4]

    v22 = 4294967295;
    v21 = sub_1036b600;
    v27 = _ccall(v24, v25, (unsigned int)v26, 0);
    v20 = *((int *)v27);
    v18 = g_1038e180 ^ &v23;
    v28 = _ccall(v24, v25, (unsigned int)v26, 0);
    *((unsigned int **)v28) = &v20;
    sub_103134d0(&v14);
    v22 = 0;
    v9 = sub_10316fe0(&v14);
    sub_103189f0(v9, &v17);
    v22 = 1;
    v15 = &v17;
    v12 = sub_1031e920(v18);
    v2 = (!v12 ? 0 : (char)sub_103189d0(v9));
    v10 = v2;
    v19 = 0;
    v1 = (*((char *)sub_103189a0(v15, 0)) <= 0 ? 127 : *((char *)sub_103189a0(v15, 0)));
    v11 = v1;
    v16 = v11;
    v8 = 48;
    v13 = sub_10312da0(&v8);
    do
    {
        if (!v16)
        {
            v19 += 1;
            if (v19 < v12)
            {
                v6 = *((char *)sub_103189a0(v15, v19));
                v0 = (v6 <= 0 ? 127 : v6);
                v11 = v0;
            }
            v16 = v11;
            iter += 1;
            sub_103149a0(iter, &v10);
        }
        v16 -= 1;
        iter += 1;
        v7 = i % 10;
        v4 = (char[6])(v13 + v7);
        v5 = sub_10312f00(v4);
        sub_103149a0(iter, &v5);
        i /= 10;
    } while (i);
    v3 = iter;
    v22 = 0;
    sub_10314610(&v17);
    v22 = 4294967295;
    sub_103130c0(&v14);
    v29 = _ccall(v24, v25, (unsigned int)v26, 0);
    *((unsigned int *)v29) = v20;
    return sub_10351225();
}
```

## `sub_1031b5c0` `0x1031b5c0`

_41 bytes. (leaf/helper — see body)_

```c
int sub_1031b5c0(int a0)
{
    int v0;  // [bp-0xc]

    v0 = (a0 < 0 ? -(a0) : a0);
    return v0;
}
```

## `sub_1031b5f0` `0x1031b5f0`

_51 bytes. (leaf/helper — see body)_

```c
int sub_1031b5f0(int a0, int a1, int a2)
{
    int v2;  // edx
    char v0;  // [bp-0x6]
    char v1;  // [bp-0x5]

    sub_103378b0(&v1, &/* unsupported instruction */, a0);
    v2 = _INSERT(0, 0, v0);
    return sub_1031b690(a1, a2, v2);
}
```

## `sub_1031b630` `0x1031b630`

_28 bytes. (leaf/helper — see body)_

```c
int sub_1031b630(unsigned int a0, unsigned int a1, int a2)
{
    char v0;  // [bp+0x0]

    return sub_1031b7c0(sub_10337e90(a2, 1, &v0));
}
```

## `sub_1031b650` `0x1031b650`

_28 bytes. (leaf/helper — see body)_

```c
int sub_1031b650(unsigned int a0, unsigned int a1, int a2)
{
    char v0;  // [bp+0x0]

    return sub_1031b7d0(sub_10337e90(a2, 1, &v0));
}
```

## `sub_1031b670` `0x1031b670`

_28 bytes. (leaf/helper — see body)_

```c
int sub_1031b670(unsigned int a0, unsigned int a1, int a2)
{
    char v0;  // [bp+0x0]

    return sub_1031b820(sub_10337e90(a2, 1, &v0));
}
```

## `sub_1031b690` `0x1031b690`

_69 bytes. (leaf/helper — see body)_

```c
int sub_1031b690(int a0, int a1, int a2)
{
    int v2[2];  // eax
    int v3[2];  // eax
    char v0;  // [bp-0x14]
    char v1;  // [bp-0xc]

    v2 = sub_1031b790(&v1, a1, a2, a0);
    v3 = sub_1031b6e0(&v0, v2[0], v2[1]);
    return sub_1031b870(v3[0], v3[1]);
}
```

## `sub_1031b6e0` `0x1031b6e0`

_37 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

int sub_1031b6e0(struct_0 *a0, unsigned int a1)
{
    struct_0 *v0;  // [bp-0xc]
    struct_0 *v1;  // [bp-0x8]

    v1 = a0;
    v1 = a0;
    v0 = v1;
    sub_1031b710(sub_10314a50(v1));
    return a1;
}
```

## `sub_1031b710` `0x1031b710`

_32 bytes. (leaf/helper — see body)_

```c
int sub_1031b710(int a0, int a1, int a2)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1031b730(a1, a2, a0, &v1);
    return a0;
}
```

## `sub_1031b730` `0x1031b730`

_90 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

struct struct_0 *[2] sub_1031b730(struct_0 **a0, struct_0 *a1, struct_0 *a2)
{
    struct_0 *v2;  // eax
    struct struct_0 *v0[2];  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10341910(a0, &v1);
    if (!a2 || !a1 || sub_10314a50(a2) > a1 || (v2 = (struct_0 *)sub_10314a50(a2), a1 > sub_10314a50(a2) + *((int *)&a2->padding_8[12])))
        sub_10353616();
    *(a0) = a2;
    a0[1] = a1;
    return a0;
}
```

## `sub_1031b790` `0x1031b790`

_43 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

int sub_1031b790(struct_0 *a0, int a1)
{
    struct_0 *v1;  // eax
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    v1 = sub_10314a50(v0);
    sub_1031b710(a1, &v1->padding_0[v0->field_14], v0);
    return a1;
}
```

## `sub_1031b7c0` `0x1031b7c0`

_13 bytes. (leaf/helper — see body)_

```c
void sub_1031b7c0(unsigned int a0)
{
    return;
}
```

## `sub_1031b7d0` `0x1031b7d0`

_23 bytes. (leaf/helper — see body)_

```c
void sub_1031b7d0(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1031b7f0(0, a0, &v1);
    return;
}
```

## `sub_1031b7f0` `0x1031b7f0`

_44 bytes. (leaf/helper — see body)_

```c
int sub_1031b7f0(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_10314610(v0);
    if (((char)a1 & 1))
        sub_10350abd(v0);
    return v0;
}
```

## `sub_1031b820` `0x1031b820`

_23 bytes. (leaf/helper — see body)_

```c
void sub_1031b820(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1031b840(0, a0, &v1);
    return;
}
```

## `sub_1031b840` `0x1031b840`

_44 bytes. (leaf/helper — see body)_

```c
int sub_1031b840(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_1031a3a0(v0);
    if (((char)a1 & 1))
        sub_10350abd(v0);
    return v0;
}
```

## `sub_1031b870` `0x1031b870`

_67 bytes. (leaf/helper — see body)_

```c
int sub_1031b870(int a0, int a1, int a2, int a3, int a4, int a5, int a6)
{
    int v2;  // edx
    char v0;  // [bp-0x6]
    char v1;  // [bp-0x5]

    sub_103378b0(&v1, &/* unsupported instruction */, a0);
    v2 = _INSERT(0, 0, v0);
    return sub_1031b8c0(a1, a2, a3, a4, a5, a6, v2);
}
```

## `sub_1031b8c0` `0x1031b8c0`

_145 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1031b8c0(int a0, int a1, int a2, int a3, int a4, int a5, int a6)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4143
    unsigned long v11;  // 4160
    unsigned long v12;  // 4118
    int v0;  // [bp-0x34]
    char v1;  // [bp-0x30]
    int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036b638;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v2 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    sub_1031bdd0(a5, a6, v2, a0);
    v5 = 0;
    sub_1031b960(a1, a2, a3, a4, &v1);
    v0 = a0;
    v5 = 4294967295;
    sub_10314610(&v1);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v3;
    return sub_10351225();
}
```

## `sub_1031b960` `0x1031b960`

_136 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

int sub_1031b960(struct_0 *a0, int a1, int a2, int a3, int a4, int a5)
{
    unsigned int v7[2];  // eax
    int v0;  // [bp-0x2c]
    int v1;  // [bp-0x28]
    char v2;  // [bp-0x24]
    unsigned int v3;  // [bp-0x1c]
    unsigned int v4;  // [bp-0x18]
    int v5;  // [bp-0xc]
    int v6;  // [bp-0x8]

    v5 = a1;
    v6 = a2;
    v7 = sub_1031b6e0(a0, &v2);
    v3 = v7[0];
    v4 = v7[1];
    v0 = a1;
    v1 = a2;
    return sub_1031ba60(sub_1031b9f0(v0, v1, v3, v4, sub_1031b9f0(a3, a4, v5, v6, a5)));
}
```

## `sub_1031b9f0` `0x1031b9f0`

_41 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1031b9f0(unsigned int a0, unsigned int a1)
{
    unsigned int v2;  // ecx
    unsigned int v0;  // [bp-0x8]
    char v1;  // [bp+0xc]

    v0 = v2;
    v0 = (!a1 ? 0 : sub_1031ba20(&v1));
    return v0;
}
```

## `sub_1031ba20` `0x1031ba20`

_60 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

int sub_1031ba20(unsigned int *a0, struct_0 *a1)
{
    unsigned int v0[2];  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    if (v0[0] != 4294967294 && (!v0[0] || v0[0] != a1->padding_0))
        sub_10353616();
    return v0[1] - a1->field_4;
}
```

## `sub_1031ba60` `0x1031ba60`

_37 bytes. (leaf/helper — see body)_

```c
int sub_1031ba60(int a0, int a1, int a2, int a3)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_1031ba90(a1, a2, a3, 0, -1, a0, &v1);
}
```

## `sub_1031ba90` `0x1031ba90`

_818 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

void* sub_1031ba90(void* idx, unsigned int a1, int a2, void* a3, unsigned int a4, int a5)
{
    struct_0 *v3;  // eax
    struct_0 *v4;  // eax
    struct_0 *v13;  // eax
    struct_0 *v14;  // eax
    struct_0 *v15;  // eax
    struct_0 *v16;  // eax
    struct_0 *v17;  // eax
    struct_0 *v18;  // eax
    struct_0 *v19;  // eax
    struct_0 *v20;  // eax
    struct_0 *v21;  // eax
    struct_0 *v22;  // eax
    struct_0 *v5;  // eax
    struct_0 *v23;  // eax
    struct_0 *v24;  // eax
    struct_0 *v6;  // eax
    struct_0 *v7;  // eax
    struct_0 *v8;  // eax
    struct_0 *v9;  // eax
    struct_0 *v10;  // eax
    struct_0 *v11;  // eax
    struct_0 *v12;  // eax
    unsigned int v0;  // [bp-0x10]
    int v1;  // [bp-0xc]
    int v2;  // [bp-0x8]

    if ((int)idx[20] >= a1 && sub_1031e920(idx) >= a4)
    {
        if ((int)idx[20] - a1 < a2)
            a2 = (int)idx[20] - a1;
        v1 = sub_1031e920() - a4;
        if (v1 < a5)
            a5 = v1;
        if (4294967295 - a5 <= (int)idx[20] - a2)
            sub_1035039e();
        v2 = (int)idx[20] - a2 - a1;
        v0 = (int)idx[20] + a5 - a2;
        if ((int)idx[20] < v0)
            sub_103149b0(idx, v0, 0);
        if (idx != a3)
        {
            v3 = sub_10314a50(idx);
            v4 = sub_10314a50(idx);
            sub_103159d0(&v4->padding_0[a1 + a5], (int)idx[24] - a1 - a5, &v3->padding_0[a1 + a2], v2);
            v5 = sub_10314a50(a3);
            v6 = sub_10314a50(idx);
            sub_10313350(&v6->padding_0[a1], (int)idx[24] - a1, &v5->padding_0[a4], a5);
            sub_10314960(idx, v0);
            return idx;
        }
        else if (a5 <= a2)
        {
            v7 = sub_10314a50(idx);
            v8 = sub_10314a50(idx);
            sub_103159d0(&v8->padding_0[a1], (int)idx[24] - a1, &v7->padding_0[a4], a5);
            v9 = sub_10314a50(idx);
            v10 = sub_10314a50(idx);
            sub_103159d0(&v10->padding_0[a1 + a5], (int)idx[24] - a1 - a5, &v9->padding_0[a1 + a2], v2);
            sub_10314960(idx, v0);
            return idx;
        }
        else if (a4 <= a1)
        {
            v11 = sub_10314a50(idx);
            v12 = sub_10314a50(idx);
            sub_103159d0(&v12->padding_0[a1 + a5], (int)idx[24] - a1 - a5, &v11->padding_0[a1 + a2], v2);
            v13 = sub_10314a50(idx);
            v14 = sub_10314a50(idx);
            sub_103159d0(&v14->padding_0[a1], (int)idx[24] - a1, &v13->padding_0[a4], a5);
            sub_10314960(idx, v0);
            return idx;
        }
        else if (a1 + a2 <= a4)
        {
            v15 = sub_10314a50(idx);
            v16 = sub_10314a50(idx);
            sub_103159d0(&v16->padding_0[a1 + a5], (int)idx[24] - a1 - a5, &v15->padding_0[a1 + a2], v2);
            v17 = sub_10314a50(idx);
            v18 = sub_10314a50(idx);
            sub_103159d0(&v18->padding_0[a1], (int)idx[24] - a1, &v17->padding_0[a5 + a4 + -1 * a2], a5);
            sub_10314960(idx, v0);
            return idx;
        }
        else
        {
            v19 = sub_10314a50(idx);
            v20 = sub_10314a50(idx);
            sub_103159d0(&v20->padding_0[a1], (int)idx[24] - a1, &v19->padding_0[a4], a2);
            v21 = sub_10314a50(idx);
            v22 = sub_10314a50(idx);
            sub_103159d0(&v22->padding_0[a1 + a5], (int)idx[24] - a1 - a5, &v21->padding_0[a1 + a2], v2);
            v23 = sub_10314a50(idx);
            v24 = sub_10314a50(idx);
            sub_103159d0(&v24->padding_0[a1 + a2], (int)idx[24] - a1 - a2, &v23->padding_0[a4 + a5], a5 - a2);
            sub_10314960(idx, v0);
            return idx;
        }
    }
    sub_103503dd(idx);
}
```

