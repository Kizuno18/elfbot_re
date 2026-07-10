# elfbot.dll decompiled — jiru 0x10339b80..0x1033acf0

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10339b80` `0x10339b80`

_39 bytes. (leaf/helper — see body)_

```c
int sub_10339b80(int a0, int a1)
{
    char v0;  // [bp-0x8]

    sub_1033a4c0(a1, a0);
    return sub_1033a5e0(&v0);
}
```

## `sub_10339bb0` `0x10339bb0`

_108 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10339bb0(unsigned int a0, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4139
    unsigned long v10;  // 4153
    unsigned long v12;  // 4120
    unsigned int v0;  // [bp-0x1c]
    char v1;  // [bp-0x11]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036f86b;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_1031a280(a0 + 4);
    v4 = 0;
    v1 = 0;
    sub_1033a620(a1, 1, _INSERT(0, 0, v1));
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v2;
    return a0;
}
```

## `sub_10339c20` `0x10339c20`

_39 bytes. (leaf/helper — see body)_

```c
int sub_10339c20(int a0, int a1)
{
    char v0;  // [bp-0x8]

    sub_1033a4c0(a1, a0);
    return sub_1033a650(&v0);
}
```

## `sub_10339c50` `0x10339c50`

_39 bytes. (leaf/helper — see body)_

```c
int sub_10339c50(int a0, int a1)
{
    char v0;  // [bp-0x8]

    sub_1033a4c0(a1, a0);
    return sub_1033a690(&v0);
}
```

## `sub_10339c80` `0x10339c80`

_52 bytes. (leaf/helper — see body)_

```c
int sub_10339c80(int *a0, unsigned int a1)
{
    unsigned int v3;  // eax
    unsigned int v0;  // [bp-0x10]
    int v1;  // [bp-0xc]
    int *v2;  // [bp-0x8]

    v2 = a0;
    v2 = a0;
    v1 = sub_1031a280(v2 + 1);
    v0 = a1;
    v3 = sub_1031aa20(v2);
    return sub_1033a6d0(*(v2), v3);
}
```

## `sub_10339cc0` `0x10339cc0`

_52 bytes. (leaf/helper — see body)_

```c
int sub_10339cc0(int *a0, unsigned int a1)
{
    unsigned int v3;  // eax
    unsigned int v0;  // [bp-0x10]
    int v1;  // [bp-0xc]
    int *v2;  // [bp-0x8]

    v2 = a0;
    v2 = a0;
    v1 = sub_1031a280(v2 + 1);
    v0 = a1;
    v3 = sub_1031aa20(v2);
    return sub_1033a710(*(v2), v3);
}
```

## `sub_10339d00` `0x10339d00`

_39 bytes. (leaf/helper — see body)_

```c
int sub_10339d00(int a0, int a1)
{
    char v0;  // [bp-0x8]

    sub_1033a4c0(a1, a0);
    return sub_1033a750(&v0);
}
```

## `sub_10339d30` `0x10339d30`

_47 bytes. (leaf/helper — see body)_

```c
int sub_10339d30(int a0, int a1, int a2)
{
    int v1;  // edx
    unsigned int v0;  // [bp-0xc]

    v0 = &/* unsupported instruction */;
    v1 = _INSERT(0, 0, *((char *)sub_103378b0((char *)&/* unsupported instruction */ + 3)));
    return sub_1033a790(a0, a1, a2, v1);
}
```

## `sub_10339d60` `0x10339d60`

_13 bytes. (leaf/helper — see body)_

```c
void sub_10339d60(unsigned int a0)
{
    char v0;  // [bp+0x0]

    sub_1033a200(&v0);
    return;
}
```

## `sub_10339d70` `0x10339d70`

_131 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10339d70(unsigned int a0, unsigned int a1, int i, int a3, int a4, int a5)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4144
    unsigned long v11;  // 4168
    unsigned long v12;  // 4126
    unsigned int v0;  // [bp-0x28]
    int v1;  // [bp-0x18], Other Possible Types: unsigned int
    char *v2;  // [bp-0x14], Other Possible Types: unsigned int
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036f890;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v2 = a0;
    v1 = a0;
    v0 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    v2 = &v0;
    v1 = a4;
    for (v5 = 0; i != a3; i += 28)
    {
        sub_10338a50(a5, a4, i);
        a4 += 28;
    }
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v3;
    return a4;
}
```

## `sub_10339dd7` `0x10339dd7`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10339dd7(void)
{
    sub_10339de2();
    return;
}
```

## `sub_10339de2` `0x10339de2`

_33 bytes. (leaf/helper — see body)_

```c
extern char g_10339e15;

int sub_10339de2(void)
{
    unsigned int v1;  // [bp+0xffff0]
    unsigned int v2;  // [bp+0x100000]
    unsigned int v3;  // [bp+0x100014]

    if (v1 == v3)
    {
        sub_103533ea(0, 0);
        v2 = 4294967295;
        return &g_10339e15;
    }
    return sub_10339ded();
}
```

## `sub_10339ded` `0x10339ded`

_20 bytes. (leaf/helper — see body)_

```c
int sub_10339ded(unsigned int a0, int a1)
{
    unsigned int v1;  // [bp+0xffff0]
    int v2;  // [bp+0x100018]

    sub_10338a70(v2, a1);
    v1 += 28;
    return sub_10339de2();
}
```

## `sub_10339e30` `0x10339e30`

_56 bytes. (leaf/helper — see body)_

```c
int sub_10339e30(int a0, int a1, int a2)
{
    unsigned int v3;  // ecx
    int v5;  // ecx
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    char v2;  // [bp-0x5]

    v2 = 0;
    v1 = _INSERT(v3, 0, v2);
    v0 = &/* unsupported instruction */;
    v5 = _INSERT(0, 0, *((char *)sub_103378b0((char *)&/* unsupported instruction */ + 2)));
    return sub_1033a7b0(a0, a1, a2, v5);
}
```

## `sub_10339e70` `0x10339e70`

_56 bytes. (leaf/helper — see body)_

```c
int sub_10339e70(int a0, int a1, int a2)
{
    unsigned int v3;  // ecx
    int v5;  // ecx
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    char v2;  // [bp-0x5]

    v2 = 0;
    v1 = _INSERT(v3, 0, v2);
    v0 = &/* unsupported instruction */;
    v5 = _INSERT(0, 0, *((char *)sub_103378b0((char *)&/* unsupported instruction */ + 2)));
    return sub_1033a7f0(a0, a1, a2, v5);
}
```

## `sub_10339eb0` `0x10339eb0`

_29 bytes. (leaf/helper — see body)_

```c
int sub_10339eb0(int a0, int a1, int a2, int a3)
{
    char v0;  // [bp+0x0]

    return sub_1033a830(a0, a1, a2, a3, &v0);
}
```

## `sub_10339ed0` `0x10339ed0`

_61 bytes. (leaf/helper — see body)_

```c
int sub_10339ed0(int a0, unsigned int a1, unsigned int a2)
{
    int v0;  // [bp-0xc]
    int v1;  // [bp-0x8]

    v0 = a1 - a0;
    v1 = a2 - v0;
    if (v0 > 0)
        sub_10353626(v1, v0, a0, v0);
    return v1;
}
```

## `sub_10339f10` `0x10339f10`

_29 bytes. (leaf/helper — see body)_

```c
int sub_10339f10(int a0, int a1, int a2, int a3)
{
    char v0;  // [bp+0x0]

    return sub_1033a890(a0, a1, a2, a3, &v0);
}
```

## `sub_10339f30` `0x10339f30`

_71 bytes. (leaf/helper — see body)_

```c
int sub_10339f30(int a0, unsigned int a1, unsigned int a2)
{
    int v0;  // [bp-0xc]
    int v1;  // [bp-0x8]

    v0 = a1 - a0 >> 1;
    v1 = a2 - v0 * 2;
    if (v0 > 0)
        sub_10353626(v1, v0 * 2, a0, v0 * 2);
    return v1;
}
```

## `sub_10339f80` `0x10339f80`

_195 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10339f80(int i, int a1, int a2, int a3)
{
    unsigned long v13;  // ldt
    unsigned long v14;  // gdt
    unsigned short v15;  // fs
    unsigned long v16;  // 4147
    unsigned int v17;  // ecx
    unsigned int v18;  // ebx
    unsigned int v19;  // esi
    unsigned int v20;  // edi
    unsigned long v21;  // 4172
    unsigned long v22;  // 4124
    unsigned int v0;  // [bp-0x4c]
    unsigned int v1;  // [bp-0x48]
    unsigned int v2;  // [bp-0x44]
    unsigned int v3;  // [bp-0x40]
    int v4;  // [bp-0x3c]
    char v5;  // [bp-0x38]
    unsigned int v6;  // [bp-0x1c]
    int v7;  // [bp-0x18]
    char *v8;  // [bp-0x14], Other Possible Types: unsigned int
    unsigned int v9;  // [bp-0x10]
    unsigned int v10;  // [bp-0xc]
    char v11;  // [bp-0x8], Other Possible Types: unsigned int
    char v12;  // [bp-0x4]

    v11 = 4294967295;
    v10 = sub_1036f8b8;
    v16 = _ccall(v13, v14, (unsigned int)v15, 0);
    v9 = *((int *)v16);
    v8 = v17;
    v6 = g_1038e180 ^ &v12;
    v3 = v18;
    v2 = v19;
    v1 = v20;
    v0 = v6;
    v21 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int **)v21) = &v9;
    v8 = &v0;
    v7 = a2;
    sub_103257a0(&v5);
    v11 = 0;
    for (v11 = 1; i != a1; i += 28)
    {
        sub_10338a50(a3, a2, &v5);
        sub_1033a8f0(a2, i);
        a2 += 28;
    }
    v11 = 0;
    v4 = a2;
    v11 = 4294967295;
    sub_1031a3a0(&v5);
    v22 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int *)v22) = v9;
    return sub_10351225();
}
```

## `sub_1033a008` `0x1033a008`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1033a008(void)
{
    sub_1033a013();
    return;
}
```

## `sub_1033a013` `0x1033a013`

_33 bytes. (leaf/helper — see body)_

```c
extern char g_1033a046;

int sub_1033a013(void)
{
    unsigned int v1;  // [bp+0xffff0]
    unsigned int v2;  // [bp+0x100000]
    unsigned int v3;  // [bp+0x100014]

    if (v1 == v3)
    {
        sub_103533ea(0, 0);
        v2 = 0;
        return &g_1033a046;
    }
    return sub_1033a01e();
}
```

## `sub_1033a01e` `0x1033a01e`

_20 bytes. (leaf/helper — see body)_

```c
int sub_1033a01e(int a0)
{
    unsigned int v1;  // [bp+0xffff0]
    int v2;  // [bp+0x100018]

    sub_10338a70(v2, a0);
    v1 += 28;
    return sub_1033a013();
}
```

## `sub_1033a080` `0x1033a080`

_52 bytes. (leaf/helper — see body)_

```c
int sub_1033a080(int i, int a1, int a2)
{
    while (i != a1)
    {
        a1 -= 28;
        a2 -= 28;
        sub_1033a8f0(a2, a1);
    }
    return a2;
}
```

## `sub_1033a0c0` `0x1033a0c0`

_52 bytes. (leaf/helper — see body)_

```c
int sub_1033a0c0(int *a0, unsigned int a1)
{
    unsigned int v3;  // eax
    unsigned int v0;  // [bp-0x10]
    int v1;  // [bp-0xc]
    int *v2;  // [bp-0x8]

    v2 = a0;
    v2 = a0;
    v1 = sub_1031a280(v2 + 1);
    v0 = a1;
    v3 = sub_1031aa20(v2);
    return sub_1033a910(*(v2), v3);
}
```

## `sub_1033a100` `0x1033a100`

_52 bytes. (leaf/helper — see body)_

```c
int sub_1033a100(int *a0, unsigned int a1)
{
    unsigned int v3;  // eax
    unsigned int v0;  // [bp-0x10]
    int v1;  // [bp-0xc]
    int *v2;  // [bp-0x8]

    v2 = a0;
    v2 = a0;
    v1 = sub_1031a280(v2 + 1);
    v0 = a1;
    v3 = sub_1031aa20(v2);
    return sub_1033a950(*(v2), v3);
}
```

## `sub_1033a140` `0x1033a140`

_125 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1033a140(unsigned int a0, int a1)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4141
    unsigned long v11;  // 4155
    unsigned long v12;  // 4124
    unsigned int v0;  // [bp-0x24]
    int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036f8f1;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v0 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    v2 = sub_1031acf0(28, a0);
    v5 = 0;
    v1 = (!v2 ? 0 : sub_1031e760(v2, a1));
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v3;
    return v1;
}
```

## `sub_1033a1c0` `0x1033a1c0`

_15 bytes. (leaf/helper — see body)_

```c
int sub_1033a1c0(int a0)
{
    return sub_1031b840(a0, 0);
}
```

## `sub_1033a1d0` `0x1033a1d0`

_34 bytes. (leaf/helper — see body)_

```c
int sub_1033a1d0(unsigned int *a0, unsigned int *a1)
{
    unsigned int v0;  // [bp-0x8]

    v0 = *(a0);
    *(a0) = *(a1);
    *(a1) = v0;
    return v0;
}
```

## `sub_1033a200` `0x1033a200`

_17 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

int sub_1033a200(struct_0 *a0)
{
    return a0->field_4;
}
```

## `sub_1033a220` `0x1033a220`

_118 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103908fc;
extern char g_10390904;

int sub_1033a220(unsigned int a0, int a1)
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
    v3 = sub_1036f923;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_103380a0(v1, a1);
    v4 = 0;
    sub_103167f0(v1 + 84);
    *((char **)v1) = &g_10390904;
    *((char **)(v1 + 84)) = &g_103908fc;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_1033a2a0` `0x1033a2a0`

_194 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103908d8;
extern char g_103908e8;
extern char g_103908f0;

int sub_1033a2a0(unsigned int idx, unsigned int a1)
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
    v4 = sub_1036f953;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v0 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    sub_10338000(idx, a1);
    v5 = 0;
    sub_10316a00(idx + 104);
    v5 = 1;
    *((char **)idx) = &g_103908f0;
    *((char **)(idx + 84)) = &g_103908e8;
    *((char **)(idx + 104)) = &g_103908d8;
    v2 = (!a1 ? 0 : a1 + 84);
    v1 = (!idx ? 0 : idx + 84);
    sub_10316940(v1, v2);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v3;
    return idx;
}
```

## `sub_1033a370` `0x1033a370`

_118 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390934;
extern char g_1039093c;

unsigned int * sub_1033a370(unsigned int *a0, unsigned int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4154
    unsigned long v11;  // 4135
    unsigned int v0;  // [bp-0x18]
    unsigned int *v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036f983;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_103383b0(v1, a1);
    v4 = 0;
    sub_103167f0(v1 + 21);
    *(v1) = &g_1039093c;
    v1[21] = &g_10390934;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_1033a3f0` `0x1033a3f0`

_194 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390910;
extern char g_10390920;
extern char g_10390928;

int sub_1033a3f0(unsigned int idx, unsigned int a1)
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
    v4 = sub_1036f9b3;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v0 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    sub_10338310(idx, a1);
    v5 = 0;
    sub_10316a00(idx + 104);
    v5 = 1;
    *((char **)idx) = &g_10390928;
    *((char **)(idx + 84)) = &g_10390920;
    *((char **)(idx + 104)) = &g_10390910;
    v2 = (!a1 ? 0 : a1 + 84);
    v1 = (!idx ? 0 : idx + 84);
    sub_10316940(v1, v2);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v3;
    return idx;
}
```

## `sub_1033a4c0` `0x1033a4c0`

_24 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_1033a4c0(unsigned int *a0, unsigned int a1)
{
    *(a0) = a1;
    return a0;
}
```

## `sub_1033a4e0` `0x1033a4e0`

_118 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int * sub_1033a4e0(int *a0, int a1)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4144
    unsigned int v12;  // eax
    unsigned long v13;  // 4160
    unsigned long v14;  // 4123
    int *v0;  // [bp-0x28]
    int v1;  // [bp-0x24]
    int v2;  // [bp-0x20]
    int *v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]
    char v7;  // [bp+0x0]

    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v12 = *((int *)v11);
    v4 = *((int *)v11);
    v3 = a0;
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v13) = &v4;
    *(a0) = a1;
    sub_1033ab10(a1, g_1038e180 ^ &v6, a0, v12, sub_1036f9db, -1, &v7);
    v5 = 0;
    v2 = a1;
    v1 = a1;
    v0 = a0 + 1;
    sub_10334530();
    v14 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v14) = v12;
    return a0;
}
```

## `sub_1033a560` `0x1033a560`

_118 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int * sub_1033a560(int *a0, int a1)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4144
    unsigned int v12;  // eax
    unsigned long v13;  // 4160
    unsigned long v14;  // 4123
    int *v0;  // [bp-0x28]
    int v1;  // [bp-0x24]
    int v2;  // [bp-0x20]
    int *v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]
    char v7;  // [bp+0x0]

    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v12 = *((int *)v11);
    v4 = *((int *)v11);
    v3 = a0;
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v13) = &v4;
    *(a0) = a1;
    sub_1033abe0(a1, g_1038e180 ^ &v6, a0, v12, sub_1036fa0b, -1, &v7);
    v5 = 0;
    v2 = a1;
    v1 = a1;
    v0 = a0 + 1;
    sub_10334530();
    v14 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v14) = v12;
    return a0;
}
```

## `sub_1033a5e0` `0x1033a5e0`

_52 bytes. (leaf/helper — see body)_

```c
int sub_1033a5e0(int *a0, unsigned int a1)
{
    unsigned int v3;  // eax
    unsigned int v0;  // [bp-0x10]
    int v1;  // [bp-0xc]
    int *v2;  // [bp-0x8]

    v2 = a0;
    v2 = a0;
    v1 = sub_1031a280(v2 + 1);
    v0 = a1;
    v3 = sub_1031aa20(v2);
    return sub_1033acb0(*(v2), v3);
}
```

## `sub_1033a620` `0x1033a620`

_48 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_1033a620(unsigned int a0, unsigned int *a1)
{
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v1 = a0;
    v1 = a0;
    v0 = *(a1);
    return sub_1031ac50(v1, sub_1033aad0(sub_1031a280(v1 + 4)));
}
```

## `sub_1033a650` `0x1033a650`

_52 bytes. (leaf/helper — see body)_

```c
int sub_1033a650(int *a0, unsigned int a1)
{
    unsigned int v3;  // eax
    unsigned int v0;  // [bp-0x10]
    int v1;  // [bp-0xc]
    int *v2;  // [bp-0x8]

    v2 = a0;
    v2 = a0;
    v1 = sub_1031a280(v2 + 1);
    v0 = a1;
    v3 = sub_1031aa20(v2);
    return sub_1033acf0(*(v2), v3);
}
```

## `sub_1033a690` `0x1033a690`

_52 bytes. (leaf/helper — see body)_

```c
int sub_1033a690(int *a0, unsigned int a1)
{
    unsigned int v3;  // eax
    unsigned int v0;  // [bp-0x10]
    int v1;  // [bp-0xc]
    int *v2;  // [bp-0x8]

    v2 = a0;
    v2 = a0;
    v1 = sub_1031a280(v2 + 1);
    v0 = a1;
    v3 = sub_1031aa20(v2);
    return sub_1033ad30(*(v2), v3);
}
```

## `sub_1033a6d0` `0x1033a6d0`

_49 bytes. (leaf/helper — see body)_

```c
int sub_1033a6d0(int a0, int a1, int a2, int a3)
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
    return sub_1033ad70(a0, a1, a2, a3, v4, v3, 0, 0, v0, &v1);
}
```

## `sub_1033a710` `0x1033a710`

_49 bytes. (leaf/helper — see body)_

```c
int sub_1033a710(int a0, int a1, int a2, int a3)
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
    return sub_1033b090(a0, a1, a2, a3, v4, v3, 0, 0, v0, &v1);
}
```

## `sub_1033a750` `0x1033a750`

_52 bytes. (leaf/helper — see body)_

```c
int sub_1033a750(int *a0, unsigned int a1)
{
    unsigned int v3;  // eax
    unsigned int v0;  // [bp-0x10]
    int v1;  // [bp-0xc]
    int *v2;  // [bp-0x8]

    v2 = a0;
    v2 = a0;
    v1 = sub_1031a280(v2 + 1);
    v0 = a1;
    v3 = sub_1031aa20(v2);
    return sub_1033b3b0(*(v2), v3);
}
```

## `sub_1033a790` `0x1033a790`

_23 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1033a790(unsigned int a0, unsigned int a1, unsigned int *a2)
{
    unsigned int v0;  // eax

    v0 = (a1 - a0 >> 1) + *(a2);
    *(a2) = v0;
    return v0;
}
```

## `sub_1033a7b0` `0x1033a7b0`

_57 bytes. (leaf/helper — see body)_

```c
int sub_1033a7b0(unsigned int a0, int a1, int a2)
{
    int v2;  // edx
    char v0;  // [bp-0x9]
    unsigned int v1;  // [bp-0x8]

    v1 = a0 + a1;
    v0 = 0;
    v2 = _INSERT(0, 0, v0);
    return sub_1033b3f0(sub_10349d70(&/* unsupported instruction */, a1, a2, v2));
}
```

## `sub_1033a7f0` `0x1033a7f0`

_60 bytes. (leaf/helper — see body)_

```c
int sub_1033a7f0(unsigned int a0, int a1, int a2)
{
    int v2;  // ecx
    char v0;  // [bp-0x9]
    unsigned int v1;  // [bp-0x8]

    v1 = a0 + a1 * 2;
    v0 = 0;
    v2 = _INSERT(a0, 0, v0);
    return sub_1033b420(sub_10349d70(&/* unsupported instruction */, a1, a2, v2));
}
```

## `sub_1033a830` `0x1033a830`

_82 bytes. (leaf/helper — see body)_

```c
char sub_1033a830(char a0, char a0, int a1, int a2)
{
    unsigned int v6;  // ecx
    int v7;  // eax
    int v8;  // ecx
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x6]
    char v4;  // [bp-0x5]

    v2 = v6;
    v4 = 0;
    v1 = &/* unsupported instruction */;
    v0 = &/* unsupported instruction */;
    v3 = sub_10337970();
    v7 = _INSERT(v3 CONCAT 0, 0, v4);
    v8 = _INSERT(0, 0, v3);
    return sub_1033b450(sub_10349d70(&/* unsupported instruction */, sub_10349d70(&/* unsupported instruction */, a1, a2, v8, v7)));
}
```

## `sub_1033a890` `0x1033a890`

_82 bytes. (leaf/helper — see body)_

```c
char sub_1033a890(char a0, char a0, int a1, int a2)
{
    unsigned int v6;  // ecx
    int v7;  // eax
    int v8;  // ecx
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x6]
    char v4;  // [bp-0x5]

    v2 = v6;
    v4 = 0;
    v1 = &/* unsupported instruction */;
    v0 = &/* unsupported instruction */;
    v3 = sub_10337970();
    v7 = _INSERT(v3 CONCAT 0, 0, v4);
    v8 = _INSERT(0, 0, v3);
    return sub_1033b490(sub_10349d70(&/* unsupported instruction */, sub_10349d70(&/* unsupported instruction */, a1, a2, v8, v7)));
}
```

## `sub_1033a8f0` `0x1033a8f0`

_17 bytes. (leaf/helper — see body)_

```c
int sub_1033a8f0(unsigned int a0, int a1)
{
    char v0;  // [bp+0x0]

    return sub_1033a990(a1, &v0);
}
```

## `sub_1033a910` `0x1033a910`

_49 bytes. (leaf/helper — see body)_

```c
int sub_1033a910(int a0, int a1, int a2, int a3)
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
    return sub_1033b4e0(a0, a1, a2, a3, v4, v3, 0, 0, v0, &v1);
}
```

## `sub_1033a950` `0x1033a950`

_49 bytes. (leaf/helper — see body)_

```c
int sub_1033a950(int a0, int a1, int a2, int a3)
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
    return sub_1033b800(a0, a1, a2, a3, v4, v3, 0, 0, v0, &v1);
}
```

## `sub_1033a990` `0x1033a990`

_309 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1033a990(unsigned int *idx, unsigned int *index)
{
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    unsigned short v14;  // fs
    unsigned long v15;  // 4142
    unsigned long v16;  // 4159
    unsigned int idx1[7];  // eax
    unsigned int idx2[7];  // eax
    unsigned int v19[7];  // ecx
    unsigned int v20[7];  // ecx
    unsigned long v21;  // 4114
    char v0;  // [bp-0x48]
    unsigned int v1;  // [bp-0x2c]
    unsigned int v2;  // [bp-0x28]
    unsigned int v3;  // [bp-0x24]
    unsigned int v4;  // [bp-0x20]
    unsigned int v5;  // [bp-0x1c]
    int v6;  // [bp-0x18]
    unsigned int v7;  // [bp-0x14]
    unsigned int v8;  // [bp-0x10]
    unsigned int v9;  // [bp-0xc]
    unsigned int v10;  // [bp-0x8]
    char v11;  // [bp-0x4]

    v10 = 4294967295;
    v9 = sub_1036fa38;
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    v8 = *((int *)v15);
    v6 = g_1038e180 ^ &v11;
    v16 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v16) = &v8;
    if ((char)sub_1033bb20(idx, index, v6, idx))
    {
        idx1 = idx + 1;
        v2 = idx1[0];
        v3 = idx1[1];
        v4 = idx1[2];
        v5 = idx1[3];
        idx2 = index + 1;
        v19 = idx + 1;
        v19[0] = idx2[0];
        v19[1] = idx2[1];
        v19[2] = idx2[2];
        v19[3] = idx2[3];
        v20 = index + 1;
        v20[0] = v2;
        v20[1] = v3;
        v20[2] = v4;
        v20[3] = v5;
        v7 = idx[5];
        idx[5] = index[5];
        index[5] = v7;
        v1 = idx[6];
        idx[6] = index[6];
        index[6] = v1;
    }
    else
    {
        sub_1031e760(&v0, idx);
        v10 = 0;
        sub_103325a0(idx, index);
        sub_103325a0(index, &v0);
        v10 = 4294967295;
        sub_1031a3a0(&v0);
    }
    v21 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int *)v21) = v8;
    return sub_10351225();
}
```

## `sub_1033aad0` `0x1033aad0`

_58 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1033aad0(unsigned int a0, unsigned int a1)
{
    unsigned int *v0;  // [bp-0xc], Other Possible Types: unsigned int
    unsigned int *v1;  // [bp-0x8]

    v1 = sub_1031acf0(4, a0);
    if (!v1)
    {
        v0 = 0;
        return 0;
    }
    *(v1) = a1;
    v0 = v1;
    return 0;
}
```

## `sub_1033ab10` `0x1033ab10`

_160 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int * sub_1033ab10(unsigned int *a0, int a1)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4149
    unsigned long v13;  // 4171
    int v14;  // edi
    int v15;  // esi
    int v16;  // ebx
    unsigned long v17;  // 4126
    unsigned int v0;  // [bp-0x34]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    char *v4;  // [bp-0x14], Other Possible Types: unsigned int *
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    char v7;  // [bp-0x8], Other Possible Types: unsigned int
    char v8;  // [bp-0x4]

    v7 = 4294967295;
    v6 = sub_1036fa6b;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v5 = *((int *)v12);
    v4 = a0;
    v0 = g_1038e180 ^ &v8;
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v5;
    v4 = &v0;
    *(a0) = 0;
    v7 = 0;
    v2 = sub_10350a53(16, g_1038e180 ^ &v8, v14, v15, v16);
    v7 = 1;
    v1 = (!v2 ? 0 : sub_1033bb30(a1));
    v3 = v1;
    v7 = 0;
    *(a0) = v3;
    v17 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v17) = v5;
    return a0;
}
```

## `sub_1033ab92` `0x1033ab92`

_34 bytes. (leaf/helper — see body)_

```c
extern char g_1033abbb;

int sub_1033ab92(void)
{
    unsigned int v1;  // [bp+0x100000]
    int v2;  // [bp+0x10000c]

    sub_1033be10(v2);
    sub_103533ea(0, 0);
    v1 = 4294967295;
    return &g_1033abbb;
}
```

## `sub_1033abe0` `0x1033abe0`

_160 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int * sub_1033abe0(unsigned int *a0, int a1)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4149
    unsigned long v13;  // 4171
    int v14;  // edi
    int v15;  // esi
    int v16;  // ebx
    unsigned long v17;  // 4126
    unsigned int v0;  // [bp-0x34]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    char *v4;  // [bp-0x14], Other Possible Types: unsigned int *
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    char v7;  // [bp-0x8], Other Possible Types: unsigned int
    char v8;  // [bp-0x4]

    v7 = 4294967295;
    v6 = sub_1036fa9b;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v5 = *((int *)v12);
    v4 = a0;
    v0 = g_1038e180 ^ &v8;
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v5;
    v4 = &v0;
    *(a0) = 0;
    v7 = 0;
    v2 = sub_10350a53(16, g_1038e180 ^ &v8, v14, v15, v16);
    v7 = 1;
    v1 = (!v2 ? 0 : sub_1033bc80(a1));
    v3 = v1;
    v7 = 0;
    *(a0) = v3;
    v17 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v17) = v5;
    return a0;
}
```

## `sub_1033ac62` `0x1033ac62`

_34 bytes. (leaf/helper — see body)_

```c
extern char g_1033ac8b;

int sub_1033ac62(void)
{
    unsigned int v1;  // [bp+0x100000]
    int v2;  // [bp+0x10000c]

    sub_1033be50(v2);
    sub_103533ea(0, 0);
    v1 = 4294967295;
    return &g_1033ac8b;
}
```

## `sub_1033acb0` `0x1033acb0`

_49 bytes. (leaf/helper — see body)_

```c
int sub_1033acb0(int a0, int a1, int a2, int a3)
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
    return sub_1033be90(a0, a1, a2, a3, v4, v3, 0, 0, v0, &v1);
}
```

## `sub_1033acf0` `0x1033acf0`

_49 bytes. (leaf/helper — see body)_

```c
int sub_1033acf0(int a0, int a1, int a2, int a3)
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
    return sub_1033c1b0(a0, a1, a2, a3, v4, v3, 0, 0, v0, &v1);
}
```

