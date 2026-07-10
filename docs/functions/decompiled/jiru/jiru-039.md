# elfbot.dll decompiled — jiru 0x1032f5a0..0x103304f0

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1032f5a0` `0x1032f5a0`

_29 bytes. (leaf/helper — see body)_

```c
int sub_1032f5a0(int a0, unsigned short a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1032f910(_INSERT(0, 0, a1), a0, &v1);
    return a0;
}
```

## `sub_1032f5c0` `0x1032f5c0`

_29 bytes. (leaf/helper — see body)_

```c
int sub_1032f5c0(int a0, unsigned short a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1032f940(_INSERT(0, 0, a1), a0, &v1);
    return a0;
}
```

## `sub_1032f5e0` `0x1032f5e0`

_214 bytes. refs "Day of month is not valid for year"_

```c
extern unsigned int g_1038e180;

int sub_1032f5e0(unsigned int a0, unsigned short a1, unsigned short a2, unsigned short a3)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    int v19;  // ecx
    unsigned short v20;  // ax
    unsigned long v21;  // 4119
    unsigned short v11;  // fs
    unsigned long v12;  // 4147
    unsigned long v13;  // 4163
    int v14;  // eax
    int v15;  // ecx
    int v16;  // edx
    int v17;  // esi
    int v18;  // eax
    int v0;  // [bp-0x68]
    int v1;  // [bp-0x64]
    int v2;  // [bp-0x60]
    int v3;  // [bp-0x5c]
    char v4;  // [bp-0x54]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    char v7;  // [bp-0x8], Other Possible Types: unsigned int
    char v8;  // [bp-0x4]

    v7 = 4294967295;
    v6 = sub_1036d870;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v5 = *((int *)v12);
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v5;
    v14 = _INSERT(&v5, 0, a3);
    v15 = _INSERT(a0, 0, a2);
    v16 = _INSERT(0, 0, a1);
    v18 = _INSERT(sub_1032fa10(v16, v15, v14, g_1038e180 ^ &v8, v17), 0, a2);
    v19 = _INSERT(0, 0, a1);
    v20 = sub_10333be0(v19, v18);
    if (v20 < (sub_10333bc0() & 0xffff))
    {
        v3 = sub_10314590(&v4, "Day of month is not valid for year");
        v2 = v3;
        v7 = 0;
        v1 = sub_1032f6c0(v2);
        v0 = v1;
        v7 = 1;
        sub_10333cd0(v0);
        v7 = 0;
        sub_1032f840();
        v7 = 4294967295;
        sub_10314610(&v4);
    }
    v21 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v21) = v5;
    return a0;
}
```

## `sub_1032f6c0` `0x1032f6c0`

_93 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1039064c;

int sub_1032f6c0(int a0, int a1)
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
    sub_1032f720(a1, g_1038e180 ^ &v2, a0, v8, sub_1036d898, -1, &v3);
    *((char **)a0) = &g_1039064c;
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v10) = v8;
    return a0;
}
```

## `sub_1032f720` `0x1032f720`

_93 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390658;

int sub_1032f720(int a0, int a1)
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
    v3 = sub_1036d8c8;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_1032d470(v1, a1);
    *((char **)v1) = &g_10390658;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_1032f780` `0x1032f780`

_84 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390658;

void sub_1032f780(int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4139
    unsigned long v11;  // 4155
    unsigned long v12;  // 4113
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036d8f8;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    *((char **)v1) = &g_10390658;
    v4 = 0;
    v4 = 4294967295;
    sub_1032d4e0(v1);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v2;
    return;
}
```

## `sub_1032f7e0` `0x1032f7e0`

_44 bytes. (leaf/helper — see body)_

```c
int sub_1032f7e0(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_1032f780(v0);
    if (((char)a1 & 1))
        sub_10350abd(v0);
    return v0;
}
```

## `sub_1032f810` `0x1032f810`

_44 bytes. (leaf/helper — see body)_

```c
int sub_1032f810(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1032f840(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_1032f840` `0x1032f840`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

void sub_1032f840(int a0)
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
    v3 = sub_1036d928;
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

## `sub_1032f890` `0x1032f890`

_44 bytes. (leaf/helper — see body)_

```c
int sub_1032f890(int a0, int a1, int a2, int a3, int a4, int a5)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1032fa70(a1, a2, a3, a4, a5, a0, &v1);
    return a0;
}
```

## `sub_1032f8c0` `0x1032f8c0`

_28 bytes. (leaf/helper — see body)_

```c
int sub_1032f8c0(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1032fab0(a1, a0, &v1);
    return a0;
}
```

## `sub_1032f8e0` `0x1032f8e0`

_40 bytes. (leaf/helper — see body)_

```c
unsigned short * sub_1032f8e0(unsigned short *a0, unsigned short a1)
{
    unsigned short *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    *(a0) = sub_1032fb90(a0, &v1);
    sub_1032fba0(_INSERT(0, 0, a1));
    return a0;
}
```

## `sub_1032f910` `0x1032f910`

_40 bytes. (leaf/helper — see body)_

```c
unsigned short * sub_1032f910(unsigned short *a0, unsigned short a1)
{
    unsigned short *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    *(a0) = sub_1032fc10(a0, &v1);
    sub_1032fc20(_INSERT(0, 0, a1));
    return a0;
}
```

## `sub_1032f940` `0x1032f940`

_40 bytes. (leaf/helper — see body)_

```c
unsigned short * sub_1032f940(unsigned short *a0, unsigned short a1)
{
    unsigned short *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    *(a0) = sub_1032fb90(a0, &v1);
    sub_1032fc90(_INSERT(0, 0, a1));
    return a0;
}
```

## `sub_1032f970` `0x1032f970`

_130 bytes. (leaf/helper — see body)_

```c
int sub_1032f970(int a0, unsigned int a1)
{
    unsigned int v1;  // ecx
    unsigned int v0;  // [bp-0x8]

    v0 = v1;
    switch (a1)
    {
    case 0:
        sub_1032fd60(a0);
        return a0;
    case 1:
        sub_1032fd30(a0);
        return a0;
    case 2:
        sub_1032fd00(a0);
        return a0;
    case 3:
        sub_1032fda0(a0);
        return a0;
    case 4:
        sub_1032fd80(a0);
        return a0;
    default:
        sub_1032fd60(a0);
        return a0;
    }
}
```

## `sub_1032fa10` `0x1032fa10`

_55 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_1032fa10(unsigned int *a0, unsigned short a1, unsigned short a2, unsigned short a3)
{
    int v0;  // eax
    int v1;  // ecx
    int v2;  // edx

    v0 = _INSERT(0, 0, a3);
    v1 = _INSERT(a0, 0, a2);
    v2 = _INSERT(0, 0, a1);
    *(a0) = sub_10333af0(sub_10333ac0(v2, v1, v0, a0));
    return a0;
}
```

## `sub_1032fa50` `0x1032fa50`

_29 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_1032fa50(unsigned int *a0)
{
    unsigned int *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    *(a0) = sub_10336b20(a0, &v1);
    return a0;
}
```

## `sub_1032fa70` `0x1032fa70`

_54 bytes. (leaf/helper — see body)_

```c
int sub_1032fa70(int a0, int a1, int a2, int a3, int a4, int a5)
{
    int v3;  // edx
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1032fad0(sub_1032fdc0(a1, a2, a3, a4, a5, a0, &v1), v3);
    return a0;
}
```

## `sub_1032fab0` `0x1032fab0`

_32 bytes. (leaf/helper — see body)_

```c
int sub_1032fab0(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1032faf0(a0, a1, a0, &v1);
    return a0;
}
```

## `sub_1032fad0` `0x1032fad0`

_30 bytes. (leaf/helper — see body)_

```c
unsigned int [2] sub_1032fad0(unsigned int *a0, unsigned int a1, unsigned int a2)
{
    *(a0) = a1;
    a0[1] = a2;
    return a0;
}
```

## `sub_1032faf0` `0x1032faf0`

_130 bytes. (leaf/helper — see body)_

```c
int sub_1032faf0(int a0, unsigned int a1)
{
    unsigned int v1;  // ecx
    unsigned int v0;  // [bp-0x8]

    v0 = v1;
    switch (a1)
    {
    case 0:
        sub_10330cc0(a0);
        return a0;
    case 1:
        sub_10330c90(a0);
        return a0;
    case 2:
        sub_10330c60(a0);
        return a0;
    case 3:
        sub_10330d00(a0);
        return a0;
    case 4:
        sub_10330ce0(a0);
        return a0;
    default:
        sub_10330cc0(a0);
        return a0;
    }
}
```

## `sub_1032fb90` `0x1032fb90`

_10 bytes. (leaf/helper — see body)_

```c
void sub_1032fb90(void)
{
    char v0;  // [bp+0x0]

    sub_10330df0(&v0);
    return;
}
```

## `sub_1032fba0` `0x1032fba0`

_111 bytes. (leaf/helper — see body)_

```c
int sub_1032fba0(unsigned short *a0, unsigned short a1)
{
    unsigned int v1;  // eax
    int v2;  // ecx
    int v3;  // eax
    unsigned short v4;  // ax
    unsigned int v5;  // ecx
    int v6;  // edx
    int v7;  // ecx
    unsigned int v8;  // eax
    unsigned short *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    v1 = (unsigned short)(unsigned int)sub_1032fb90() + 1;
    if (a1 + 1 < v1)
    {
        v2 = _INSERT(0, 0, a1);
        v3 = _INSERT(v1, 0, *(v0));
        return sub_10330e00(v3, v2, 0);
    }
    v4 = sub_10330de0();
    v5 = v4;
    if (a1 <= v5)
    {
        v8 = _INSERT(v4, 0, a1);
        *(v0) = v8;
        return v8;
    }
    v6 = _INSERT(0, 0, a1);
    v7 = _INSERT(v5, 0, *(v0));
    return sub_10330e00(v7, v6, 1);
}
```

## `sub_1032fc10` `0x1032fc10`

_10 bytes. (leaf/helper — see body)_

```c
void sub_1032fc10(void)
{
    char v0;  // [bp+0x0]

    sub_10330f00(&v0);
    return;
}
```

## `sub_1032fc20` `0x1032fc20`

_111 bytes. (leaf/helper — see body)_

```c
int sub_1032fc20(unsigned short *a0, unsigned short a1)
{
    unsigned int v1;  // eax
    int v2;  // ecx
    int v3;  // eax
    unsigned short v4;  // ax
    unsigned int v5;  // ecx
    int v6;  // edx
    int v7;  // ecx
    unsigned int v8;  // eax
    unsigned short *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    v1 = (unsigned short)(unsigned int)sub_1032fc10() + 1;
    if (a1 + 1 < v1)
    {
        v2 = _INSERT(0, 0, a1);
        v3 = _INSERT(v1, 0, *(v0));
        return sub_10330f10(v3, v2, 0);
    }
    v4 = sub_10330ef0();
    v5 = v4;
    if (a1 <= v5)
    {
        v8 = _INSERT(v4, 0, a1);
        *(v0) = v8;
        return v8;
    }
    v6 = _INSERT(0, 0, a1);
    v7 = _INSERT(v5, 0, *(v0));
    return sub_10330f10(v7, v6, 1);
}
```

## `sub_1032fc90` `0x1032fc90`

_111 bytes. (leaf/helper — see body)_

```c
int sub_1032fc90(unsigned short *a0, unsigned short a1)
{
    unsigned int v1;  // eax
    int v2;  // ecx
    int v3;  // eax
    unsigned short v4;  // ax
    unsigned int v5;  // ecx
    int v6;  // edx
    int v7;  // ecx
    unsigned int v8;  // eax
    unsigned short *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    v1 = (unsigned short)(unsigned int)sub_1032fb90() + 1;
    if (a1 + 1 < v1)
    {
        v2 = _INSERT(0, 0, a1);
        v3 = _INSERT(v1, 0, *(v0));
        return sub_10331090(v3, v2, 0);
    }
    v4 = sub_10331080();
    v5 = v4;
    if (a1 <= v5)
    {
        v8 = _INSERT(v4, 0, a1);
        *(v0) = v8;
        return v8;
    }
    v6 = _INSERT(0, 0, a1);
    v7 = _INSERT(v5, 0, *(v0));
    return sub_10331090(v7, v6, 1);
}
```

## `sub_1032fd00` `0x1032fd00`

_22 bytes. (leaf/helper — see body)_

```c
int sub_1032fd00(unsigned int a0)
{
    char v0;  // [bp+0x0]

    sub_1033a4c0(sub_1032fd20(&v0));
    return a0;
}
```

## `sub_1032fd20` `0x1032fd20`

_8 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1032fd20(void)
{
    return 4294967295;
}
```

## `sub_1032fd30` `0x1032fd30`

_22 bytes. (leaf/helper — see body)_

```c
int sub_1032fd30(unsigned int a0)
{
    char v0;  // [bp+0x0]

    sub_1033a4c0(sub_1032fd50(&v0));
    return a0;
}
```

## `sub_1032fd50` `0x1032fd50`

_7 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1032fd50(void)
{
    return 0;
}
```

## `sub_1032fd60` `0x1032fd60`

_25 bytes. (leaf/helper — see body)_

```c
int sub_1032fd60(unsigned int a0)
{
    sub_1033a4c0(sub_1032fd20() - 1);
    return a0;
}
```

## `sub_1032fd80` `0x1032fd80`

_25 bytes. (leaf/helper — see body)_

```c
int sub_1032fd80(unsigned int a0)
{
    sub_1033a4c0(sub_1032fd20() - 2);
    return a0;
}
```

## `sub_1032fda0` `0x1032fda0`

_25 bytes. (leaf/helper — see body)_

```c
int sub_1032fda0(unsigned int a0)
{
    sub_1033a4c0(sub_1032fd50() + 1);
    return a0;
}
```

## `sub_1032fdc0` `0x1032fdc0`

_267 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1032fdc0(int a0, int a1, int a2, int a3, int a4)
{
    unsigned int v2;  // esi
    unsigned int v3;  // edi
    unsigned int v4;  // esi
    unsigned int v5;  // eax
    int v6;  // edx
    unsigned int v8;  // esi
    unsigned int v9;  // eax
    int v10;  // edx
    unsigned int v11;  // eax
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v1 = v2;
    v0 = v3;
    if (a0 >= 0 && a1 >= 0 && a2 >= 0 && (a4 > 0 || a4 >= 0 && a3 >= 0))
    {
        v4 = sub_103544a0(a0, a0 >> 31, 3600, 0);
        v5 = sub_103544a0(a1, a1 >> 31, 60, 0);
        return sub_103544a0(v4 + v5 + a2, v6 + v6 + (v4 + v5 < v4) + (a2 >> 31) + (v4 + v5 + a2 < v4 + v5), sub_1032f360(), v6) + a3;
    }
    a0 = sub_10333de0(a0);
    a1 = sub_10333de0(a1);
    a2 = sub_10333de0(a2);
    a3 = sub_103344f0(a3, a4);
    v8 = sub_103544a0(a0, a0 >> 31, 3600, 0);
    v9 = sub_103544a0(a1, a1 >> 31, 60, 0);
    v11 = sub_103544a0(v8 + v9 + a2, v10 + v10 + (v8 + v9 < v8) + (a2 >> 31) + (v8 + v9 + a2 < v8 + v9), sub_1032f360(), v10);
    return sub_103544a0(v11 + a3, v10 + v10 + (v11 + a3 < v11), -1, -1);
}
```

## `sub_1032fed0` `0x1032fed0`

_166 bytes. (leaf/helper — see body)_

```c
int sub_1032fed0(int a0, int *a1, int *a2)
{
    int v5;  // edi
    int v6;  // esi
    int v7;  // esi
    int v8;  // eax
    unsigned int v9;  // edx
    int v10;  // eax
    int v11;  // edx
    char v0;  // [bp-0x24]
    char v1;  // [bp-0x1c]
    char v2;  // [bp-0x14]
    int v3;  // [bp-0xc]
    int v4;  // [bp-0x8]

    if (!(char)sub_10331480(v5, v6) && !(char)sub_10331480())
    {
        v7 = sub_1032f340(a1);
        v8 = sub_1032f340(a2);
        v3 = v7 - v8;
        v4 = v9 - v9 - (v7 < v8);
        sub_1032f890(a0, 0, 0, 0, v3, v4);
        return a0;
    }
    v10 = sub_103314a0(&v1);
    sub_103314a0(&v2, &v0, v10);
    sub_10334540(&v2, &v0, v10);
    sub_1032f8c0(a0, sub_10330d70(sub_1032ff80(), v11));
    return a0;
}
```

## `sub_1032ff39` `0x1032ff39`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032ff39(void)
{
}
```

## `sub_1032ff80` `0x1032ff80`

_19 bytes. (leaf/helper — see body)_

```c
int sub_1032ff80(unsigned int *a0)
{
    return *(a0);
}
```

## `sub_1032ffa0` `0x1032ffa0`

_29 bytes. (leaf/helper — see body)_

```c
int sub_1032ffa0(unsigned int *a0)
{
    int v2;  // edx
    unsigned int *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_10330d20(sub_1032ff80(v0), v2);
}
```

## `sub_1032ffc0` `0x1032ffc0`

_261 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    int field_0;
    int field_4;
    int field_8;
    unsigned short field_c;
    char padding_e[2];
    unsigned int field_10;
    unsigned int field_14;
} struct_0;

int sub_1032ffc0(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int *a3)
{
    int v12;  // edx
    unsigned int v13;  // ecx
    unsigned int v14;  // ecx
    unsigned int v0;  // [bp-0x98]
    struct_0 *v1;  // [bp-0x94]
    unsigned int v2;  // [bp-0x5c]
    int v3;  // [bp-0x58]
    char v4;  // [bp-0x54], Other Possible Types: int
    unsigned int v5;  // [bp-0x50]
    int v6;  // [bp-0x4c]
    struct_0 *v7;  // [bp-0x48]
    int v8;  // [bp-0x44]
    char v9;  // [bp-0x3c]
    char v10;  // [bp-0x30]
    char v11;  // [bp-0xc]

    sub_103300d0(&v11);
    v8 = sub_103346c0(&v11);
    v2 = sub_10354870(v8, v12, 1000000, 0);
    v3 = v12;
    v5 = sub_103547f0(v8, v12, 1000000, 0);
    v7 = a3(&v2, &v10);
    sub_1032f580(&/* unsupported instruction */, v7->field_c);
    v1 = v7;
    sub_1032f5c0(&v1, v7->field_10 + 1);
    v13 = v7->field_14 + 1900;
    v0 = v13;
    sub_1032f5a0(&v0, v0);
    sub_1032f5e0(&v4, v13, *((unsigned short *)&v7), v14);
    v6 = sub_103544e0(sub_1032f360(), v12, 1000000, 0);
    sub_1032f890(&v9, v7->field_8, v7->field_4, v7->field_0, v6 * v5, 0);
    sub_10330140(&v9);
    sub_103300e0(v4);
    return a2;
}
```

## `sub_103300d0` `0x103300d0`

_15 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b148;

int sub_103300d0(unsigned int a0)
{
    char v0;  // [bp+0x0]

    return g_1038b148(a0, &v0);
}
```

## `sub_103300e0` `0x103300e0`

_34 bytes. (leaf/helper — see body)_

```c
int sub_103300e0(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]
    unsigned int v2;  // [bp+0x4]
    char v3;  // [bp+0x8]

    v0 = a0;
    sub_10330110(&v2, &v3, 0, a0, &v1);
    return a0;
}
```

## `sub_10330110` `0x10330110`

_40 bytes. (leaf/helper — see body)_

```c
int sub_10330110(int a0, int a1, int a2, int a3)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10330180(a0, a1, a2, a3, a0, &v1);
    return a0;
}
```

## `sub_10330140` `0x10330140`

_28 bytes. (leaf/helper — see body)_

```c
int sub_10330140(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10330160(a1, a0, &v1);
    return a0;
}
```

## `sub_10330160` `0x10330160`

_32 bytes. (leaf/helper — see body)_

```c
unsigned int [2] sub_10330160(unsigned int *a0, unsigned int *a1)
{
    unsigned int v0;  // edx

    v0 = a1[1];
    *(a0) = *(a1);
    a0[1] = v0;
    return a0;
}
```

## `sub_10330180` `0x10330180`

_36 bytes. (leaf/helper — see body)_

```c
int sub_10330180(unsigned int a0, int a1, int a2)
{
    char v0;  // [bp+0x0]
    char v1;  // [bp+0x10]

    sub_10334530(&v1, &v0);
    sub_103312f0(a1, a2);
    return a0;
}
```

## `sub_103301b0` `0x103301b0`

_19 bytes. (leaf/helper — see body)_

```c
void sub_103301b0(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10331570(a0, &v1);
    return;
}
```

## `sub_103301d0` `0x103301d0`

_22 bytes. (leaf/helper — see body)_

```c
char * sub_103301d0(char *a0)
{
    *(a0) = 0;
    return a0;
}
```

## `sub_103301f0` `0x103301f0`

_34 bytes. (leaf/helper — see body)_

```c
char * sub_103301f0(char *a0, int a1)
{
    char *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    *(a0) = 0;
    sub_103314c0(a1, a0, &v1);
    return a0;
}
```

## `sub_10330220` `0x10330220`

_60 bytes. (leaf/helper — see body)_

```c
int sub_10330220(int a0, int a1)
{
    int v1;  // ecx
    char v0;  // [bp-0x6]

    if (!(char)sub_103315c0(a0))
        return sub_103314c0(a1);
    v1 = _INSERT(0, 0, v0);
    return sub_10331550(a1, v1);
}
```

## `sub_10330260` `0x10330260`

_26 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10330260(char *a0)
{
    return -(0 < *(a0)) & sub_103315c0;
}
```

## `sub_10330280` `0x10330280`

_60 bytes. (leaf/helper — see body)_

```c
char * sub_10330280(unsigned int a0, int a1)
{
    int v1;  // ecx
    char v0;  // [bp-0x6]

    if (!(char)sub_103315c0(a0))
        return sub_10325930(a0, a1);
    v1 = _INSERT(0, 0, v0);
    return sub_103315a0(a1, v1);
}
```

## `sub_103302c0` `0x103302c0`

_34 bytes. (leaf/helper — see body)_

```c
char * sub_103302c0(char *a0, int a1)
{
    char *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    *(a0) = 0;
    sub_103315d0(a1, a0, &v1);
    return a0;
}
```

## `sub_103302f0` `0x103302f0`

_19 bytes. (leaf/helper — see body)_

```c
void sub_103302f0(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10331660(a0, &v1);
    return;
}
```

## `sub_10330310` `0x10330310`

_129 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    unsigned int field_8;
} struct_0;

extern unsigned int g_1038e180;

unsigned int sub_10330310(struct_0 *a0, int a1, int a2)
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
    v16 = sub_10330470(a1, g_1038e180 ^ &v5, v13, v14, v15, a0, &v0, v11, sub_1036d950, -1, &v6);
    if ((char)v16)
    {
        v4 = 0;
        v16 = sub_10330560(a0->field_4, a1, a2);
        a0->field_8 = v16;
        v4 = 4294967295;
    }
    v17 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v17) = v11;
    return v16;
}
```

## `sub_10330376` `0x10330376`

_30 bytes. (leaf/helper — see body)_

```c
extern char g_1033039b;

int sub_10330376(void)
{
    unsigned int v1;  // [bp+0x100000]

    sub_103304f0();
    sub_103533ea(0, 0);
    v1 = 4294967295;
    return &g_1033039b;
}
```

## `sub_103303b0` `0x103303b0`

_49 bytes. (leaf/helper — see body)_

```c
unsigned int sub_103303b0(unsigned int *a0)
{
    unsigned int v0;  // [bp-0xc]

    v0 = (!a0[1] ? 0 : a0[3] - a0[1]);
    return v0;
}
```

## `sub_103303f0` `0x103303f0`

_118 bytes. (leaf/helper — see body)_

```c
int sub_103303f0(unsigned int *a0, int a1, int a2, int a3, int a4)
{
    int v0;  // [bp-0x20]
    char v1;  // [bp-0x18]
    char v2;  // [bp-0x10]
    int v3;  // [bp-0x8]

    v0 = (!sub_1032e2a0(a0) ? 0 : sub_10332400(sub_103414f0(&v2)));
    v3 = v0;
    sub_103316b0(a2, a3, 1, a4);
    sub_103414f0(&v1, a1, v3);
    sub_103323c0(&v1, a1, v3);
    return a1;
}
```

## `sub_10330470` `0x10330470`

_120 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    unsigned int field_8;
    unsigned int field_c;
} struct_0;

char sub_10330470(struct_0 *idx, int a1)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = idx;
    memset(&idx->field_4, 0, 12);
    if (!a1)
        return 0;
    if (sub_10331690(idx, &v1) < a1)
    {
        sub_103319c0();
    }
    else
    {
        idx->field_4 = sub_10314c40(idx, a1);
        idx->field_8 = idx->field_4;
        idx->field_c = idx->field_4 + a1;
    }
    return 1;
}
```

## `sub_1033049f` `0x1033049f`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1033049f(void)
{
}
```

## `sub_103304f0` `0x103304f0`

_100 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    int field_8;
    unsigned int field_c;
} struct_0;

struct_0 * sub_103304f0(struct_0 *a0)
{
    struct_0 *idx;  // [bp-0x8]

    idx = a0;
    idx = a0;
    if (idx->field_4)
    {
        sub_1033e420(idx->field_4, idx->field_8);
        sub_1033e3d0(idx->field_4, idx->field_c - idx->field_4);
    }
    idx->field_4 = 0;
    idx->field_8 = 0;
    idx->field_c = 0;
    return idx;
}
```

