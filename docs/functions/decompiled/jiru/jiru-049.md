# elfbot.dll decompiled — jiru 0x1033d050..0x1033e040

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1033d050` `0x1033d050`

_28 bytes. (leaf/helper — see body)_

```c
int sub_1033d050(unsigned int a0, int a1, unsigned int a2)
{
    unsigned int v0;  // [bp-0x8]

    v0 = 1;
    return sub_1033d010(a1, sub_10337e90(a2));
}
```

## `sub_1033d070` `0x1033d070`

_25 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

unsigned int sub_1033d070(struct_0 **a0, unsigned int *a1)
{
    unsigned int v0;  // eax

    v0 = *(a0)->field_0;
    *(a1) = v0;
    return v0;
}
```

## `sub_1033d090` `0x1033d090`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1033d090(int *a0, int a1)
{
    int *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_10319f70(a1, *(v0));
}
```

## `sub_1033d0b0` `0x1033d0b0`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1033d0b0(int *a0, int a1)
{
    int *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_103325a0(a1, *(v0));
}
```

## `sub_1033d0d0` `0x1033d0d0`

_44 bytes. (leaf/helper — see body)_

```c
int sub_1033d0d0(int a0, int a1)
{
    int v3;  // ecx
    int v4;  // edx
    char v0;  // [bp-0x8]
    char v1;  // [bp-0x6]
    char v2;  // [bp-0x5]

    v1 = 0;
    v3 = _INSERT(a0, 0, v2);
    v4 = _INSERT(0, 0, v1);
    return sub_1033d200(a1, v0, v4, v3, a0);
}
```

## `sub_1033d100` `0x1033d100`

_44 bytes. (leaf/helper — see body)_

```c
int sub_1033d100(int a0, int a1)
{
    int v3;  // ecx
    int v4;  // edx
    char v0;  // [bp-0x9]
    char v1;  // [bp-0x7]
    char v2;  // [bp-0x6]

    v1 = 0;
    v3 = _INSERT(a0, 0, v2);
    v4 = _INSERT(0, 0, v1);
    return sub_1033d270(a1, v0, v4, v3, a0);
}
```

## `sub_1033d130` `0x1033d130`

_44 bytes. (leaf/helper — see body)_

```c
int sub_1033d130(int a0, int a1)
{
    int v3;  // ecx
    int v4;  // edx
    char v0;  // [bp-0x9]
    char v1;  // [bp-0x7]
    char v2;  // [bp-0x6]

    v1 = 0;
    v3 = _INSERT(a0, 0, v2);
    v4 = _INSERT(0, 0, v1);
    return sub_1033d370(a1, v0, v4, v3, a0);
}
```

## `sub_1033d160` `0x1033d160`

_25 bytes. (leaf/helper — see body)_

```c
int sub_1033d160(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_1033d4f0(a1, a0, &v1);
}
```

## `sub_1033d180` `0x1033d180`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1033d180(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_1033d470(a1, a0, &v1);
}
```

## `sub_1033d1a0` `0x1033d1a0`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1033d1a0(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_1033d4d0(a1, a0, &v1);
}
```

## `sub_1033d1c0` `0x1033d1c0`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1033d1c0(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_1033d490(a1, a0, &v1);
}
```

## `sub_1033d1e0` `0x1033d1e0`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1033d1e0(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_1033d4b0(a1, a0, &v1);
}
```

## `sub_1033d200` `0x1033d200`

_100 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_1033d200(void* a0, unsigned int *a1)
{
    unsigned int *v0;  // [bp-0x10], Other Possible Types: unsigned int
    unsigned int *v1;  // [bp-0x8]

    sub_1031a160(*((int *)a0));
    v1 = sub_1031acf0(4, sub_1031a280(*((int *)a0) + 4));
    if (v1)
    {
        *(v1) = *(a1);
        v0 = v1;
    }
    else
    {
        v0 = 0;
    }
    return sub_1031ac50(*((int *)a0), (int)a0[4]);
}
```

## `sub_1033d270` `0x1033d270`

_187 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int * sub_1033d270(void* a0, int a1)
{
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // fs
    unsigned long v13;  // 4146
    unsigned long v14;  // 4168
    unsigned int *v15;  // eax
    unsigned long v16;  // 4119
    unsigned int v0;  // [bp-0x3c]
    int v1;  // [bp-0x2c]
    unsigned int v2;  // [bp-0x20]
    int v3;  // [bp-0x1c]
    int v4;  // [bp-0x18]
    char *v5;  // [bp-0x14], Other Possible Types: void*
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    char v8;  // [bp-0x8], Other Possible Types: unsigned int
    char v9;  // [bp-0x4]

    v8 = 4294967295;
    v7 = sub_1036fc11;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v6 = *((int *)v13);
    v5 = a0;
    v0 = g_1038e180 ^ &v9;
    v14 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v14) = &v6;
    v5 = &v0;
    sub_1031a160(*((int *)a0));
    v8 = 0;
    v2 = sub_1031a280(*((int *)a0) + 4);
    v3 = sub_1031acf0(28, v2);
    v8 = 1;
    v1 = (!v3 ? 0 : sub_103145d0(v3, a1));
    v4 = v1;
    v8 = 0;
    v8 = 4294967295;
    v15 = sub_1031ac50(*((int *)a0), (int)a0[4]);
    v16 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v16) = v6;
    return v15;
}
```

## `sub_1033d2ff` `0x1033d2ff`

_61 bytes. (leaf/helper — see body)_

```c
extern char g_1033d343;

int sub_1033d2ff(void)
{
    unsigned int **v1;  // [bp+0xfffe0]
    int v2;  // [bp+0xfffe4]
    unsigned int v3;  // [bp+0x100000]

    v2 = sub_1031acf0(1, sub_1031a280(*(v1) + 1));
    sub_1031ac50(*(v1), 0);
    sub_103533ea(0, 0);
    v3 = 4294967295;
    return &g_1033d343;
}
```

## `sub_1033d370` `0x1033d370`

_187 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int * sub_1033d370(void* a0, int a1)
{
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // fs
    unsigned long v13;  // 4146
    unsigned long v14;  // 4168
    unsigned int *v15;  // eax
    unsigned long v16;  // 4119
    unsigned int v0;  // [bp-0x3c]
    int v1;  // [bp-0x2c]
    unsigned int v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x1c]
    int v4;  // [bp-0x18]
    char *v5;  // [bp-0x14], Other Possible Types: void*
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    char v8;  // [bp-0x8], Other Possible Types: unsigned int
    char v9;  // [bp-0x4]

    v8 = 4294967295;
    v7 = sub_1036fc41;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v6 = *((int *)v13);
    v5 = a0;
    v0 = g_1038e180 ^ &v9;
    v14 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v14) = &v6;
    v5 = &v0;
    sub_1031a160(*((int *)a0));
    v8 = 0;
    v2 = sub_1031a280(*((int *)a0) + 4);
    v3 = sub_1031acf0(28, v2);
    v8 = 1;
    v1 = (!v3 ? 0 : sub_1031e760(v3, a1));
    v4 = v1;
    v8 = 0;
    v8 = 4294967295;
    v15 = sub_1031ac50(*((int *)a0), (int)a0[4]);
    v16 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v16) = v6;
    return v15;
}
```

## `sub_1033d3ff` `0x1033d3ff`

_61 bytes. (leaf/helper — see body)_

```c
extern char g_1033d443;

int sub_1033d3ff(void)
{
    unsigned int **v1;  // [bp+0xfffe0]
    int v2;  // [bp+0xfffe4]
    unsigned int v3;  // [bp+0x100000]

    v2 = sub_1031acf0(1, sub_1031a280(*(v1) + 1));
    sub_1031ac50(*(v1), 0);
    sub_103533ea(0, 0);
    v3 = 4294967295;
    return &g_1033d443;
}
```

## `sub_1033d470` `0x1033d470`

_27 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

int sub_1033d470(struct_0 **a0, unsigned int *a1)
{
    unsigned int v0;  // eax

    v0 = *(a0)->field_0;
    *(a1) = v0;
    return _INSERT(v0, 0, 1);
}
```

## `sub_1033d490` `0x1033d490`

_29 bytes. (leaf/helper — see body)_

```c
char sub_1033d490(int *a0, int a1)
{
    int *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_10319f70(a1, *(v0));
    return 1;
}
```

## `sub_1033d4b0` `0x1033d4b0`

_29 bytes. (leaf/helper — see body)_

```c
char sub_1033d4b0(int *a0, int a1)
{
    int *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_103325a0(a1, *(v0));
    return 1;
}
```

## `sub_1033d4d0` `0x1033d4d0`

_15 bytes. (leaf/helper — see body)_

```c
char sub_1033d4d0(unsigned int a0)
{
    return 0;
}
```

## `sub_1033d4e0` `0x1033d4e0`

_15 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1033d4e0(unsigned int a0)
{
    return 0;
}
```

## `sub_1033d4f0` `0x1033d4f0`

_19 bytes. (leaf/helper — see body)_

```c
int sub_1033d4f0(unsigned int a0)
{
    unsigned int v0;  // [bp-0x8]

    v0 = 0;
    return sub_10337e90(a0);
}
```

## `sub_1033d510` `0x1033d510`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1033d510(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_10338550(a0 - 84, v0);
}
```

## `sub_1033d520` `0x1033d520`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1033d520(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_10335690(a0 - 40, v0);
}
```

## `sub_1033d530` `0x1033d530`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1033d530(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_10335810(a0 - 40, v0);
}
```

## `sub_1033d540` `0x1033d540`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1033d540(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_103356f0(a0 - 60, v0);
}
```

## `sub_1033d550` `0x1033d550`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1033d550(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_10335780(a0 - 40, v0);
}
```

## `sub_1033d560` `0x1033d560`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1033d560(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_10338640(a0 - 104, v0);
}
```

## `sub_1033d570` `0x1033d570`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1033d570(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_103357e0(a0 - 60, v0);
}
```

## `sub_1033d580` `0x1033d580`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1033d580(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_10335720(a0 - 40, v0);
}
```

## `sub_1033d590` `0x1033d590`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1033d590(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_103356f0(a0 - 40, v0);
}
```

## `sub_1033d5a0` `0x1033d5a0`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1033d5a0(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_103357b0(a0 - 40, v0);
}
```

## `sub_1033d5b0` `0x1033d5b0`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1033d5b0(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_103356c0(a0 - 40, v0);
}
```

## `sub_1033d5c0` `0x1033d5c0`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1033d5c0(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_10338640(a0 - 84, v0);
}
```

## `sub_1033d5d0` `0x1033d5d0`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1033d5d0(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_10338520(a0 - 104, v0);
}
```

## `sub_1033d5e0` `0x1033d5e0`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1033d5e0(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_10335690(a0 - 60, v0);
}
```

## `sub_1033d5f0` `0x1033d5f0`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1033d5f0(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_10338670(a0 - 84, v0);
}
```

## `sub_1033d600` `0x1033d600`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1033d600(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_103357e0(a0 - 40, v0);
}
```

## `sub_1033d610` `0x1033d610`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1033d610(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_10335780(a0 - 60, v0);
}
```

## `sub_1033d620` `0x1033d620`

_8 bytes. (leaf/helper — see body)_

```c
int sub_1033d620(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_10338520(a0 - 84, v0);
}
```

## `sub_1033d630` `0x1033d630`

_86 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1033d630(unsigned int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4135
    unsigned int v10;  // eax
    unsigned long v11;  // 4151
    unsigned long v12;  // 4120
    unsigned int v0;  // [bp-0x14]
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
    sub_1031a280(a0);
    sub_1033d690(g_1038e180 ^ &v3, a0, v10, sub_1036fc68, 0, &v4);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v10;
    return a0;
}
```

## `sub_1033d690` `0x1033d690`

_30 bytes. (leaf/helper — see body)_

```c
unsigned int [2] sub_1033d690(unsigned int *a0)
{
    *(a0) = 0;
    a0[1] = 0;
    return a0;
}
```

## `sub_1033d6b0` `0x1033d6b0`

_83 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

void sub_1033d6b0(unsigned int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4136
    unsigned int v10;  // eax
    unsigned long v11;  // 4152
    unsigned long v12;  // 4113
    unsigned int v0;  // [bp-0x14]
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
    sub_1033d710(g_1038e180 ^ &v3, a0, v10, sub_1036fcc8, 0, &v4);
    v2 = 4294967295;
    sub_103388a0(a0);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v10;
    return;
}
```

## `sub_1033d710` `0x1033d710`

_42 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b128;

unsigned int sub_1033d710(struct_0 *a0)
{
    struct_0 *v2;  // ecx
    unsigned int v3;  // eax
    unsigned int v0;  // [bp-0x8]

    v2 = &a0->field_4;
    InterlockedExchange(v2, 0);
    v3 = (unsigned int)v2->padding_0;
    v0 = (unsigned int)v2->padding_0;
    if (v0)
        v3 = g_1038b128(v0);
    return v3;
}
```

## `sub_1033d740` `0x1033d740`

_404 bytes. refs "LISTBOX"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b07c;
extern struct_0 *g_1038b308;
extern struct_0 *g_1038b334;
extern unsigned int g_1038e180;
extern char g_103a2b50;
extern char g_103a2b51;
extern char g_103a2b58;
extern unsigned int g_103a2c5c;

unsigned int sub_1033d740(char a0)
{
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // fs
    unsigned long v13;  // 4166
    unsigned long v14;  // 4170
    unsigned int v15;  // eax
    unsigned int v16;  // eax
    unsigned long v17;  // 4113
    int v0;  // [bp-0xe8]
    int v1;  // [bp-0xe4]
    unsigned int v2;  // [bp-0xe0]
    unsigned int v3;  // [bp-0xdc]
    char v4;  // [bp-0xd8]
    unsigned int v5;  // [bp-0xbc]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    char v8;  // [bp-0x8], Other Possible Types: unsigned int
    char v9;  // [bp-0x4]

    v8 = 4294967295;
    v7 = sub_1036fd06;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v6 = *((int *)v13);
    v14 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v14) = &v6;
    if (!g_103a2b58)
        sub_1033d8e0(g_1038e180 ^ &v9);
    if (a0 && !g_103a2c5c && !g_103a2b50 && !g_103a2b51)
    {
        v15 = g_1038b050(0, 0);
        v16 = g_1038b334(0x40000, "LISTBOX", &g_103a2b58, 0x10f45100, 0x80000000, 0x80000000, 0x80000000, 0x80000000, 0, 0, v15);
        g_103a2c5c = v16;
        if (!g_103a2c5c)
        {
            v5 = g_1038b07c();
            v3 = sub_1033ee80("RAID error %1$u creating listwindow, reverting to older format.", &v5);
            v2 = v3;
            v8 = 0;
            v1 = sub_1033ef90(&v4, sub_1033ef70("RAID error %1$u creating listwindow, reverting to older format.", &v5));
            v0 = v1;
            v8 = 1;
            sub_1033d980(v0);
            v8 = 0;
            sub_10314610(&v4);
            v8 = 4294967295;
            v16 = sub_1033e060();
        }
    }
    else
    {
        v16 = a0;
        if (!v16 && g_103a2c5c)
        {
            v16 = g_1038b308(g_103a2c5c);
            g_103a2c5c = 0;
        }
    }
    v17 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v17) = v6;
    return v16;
}
```

## `sub_1033d8e0` `0x1033d8e0`

_157 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern int g_103a2b58;

int sub_1033d8e0(void)
{
    char *v0;  // [bp-0x11c]
    char *v1;  // [bp-0x118]
    char v2;  // [bp-0x114]
    unsigned int v3;  // [bp-0x8]
    char v4;  // [bp-0x4]

    v3 = g_1038e180 ^ &v4;
    if (!g_103a2c60)
        sub_1033de00(0, 0);
    sub_10352cb0(&v2, "C:\\Archivos de programa\\ElfBot NG\\elfbot-2.DbgLog");
    v1 = sub_103124a0(&v2, 92);
    v0 = (!v1 ? &v2 : v1 + 1);
    sub_10352cb0(&g_103a2b58, v0);
    return sub_10351225();
}
```

## `sub_1033d980` `0x1033d980`

_100 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_1033d980(int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4152
    unsigned int v11;  // eax
    unsigned long v12;  // 4113
    unsigned int v0;  // [bp-0x74]
    char v1;  // [bp-0x70]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036fd2c;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_10319e80(&v1, a0);
    v4 = 0;
    sub_1033d9f0(0, &v1);
    v4 = 4294967295;
    v11 = sub_10319f00(&v1);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v2;
    return v11;
}
```

## `sub_1033d9f0` `0x1033d9f0`

_254 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b14c;
extern struct_0 *g_1038b2f4;
extern struct_0 *g_1038b340;
extern unsigned int g_1038e180;
extern char g_103a2b50;
extern char g_103a2b51;
extern char g_103a2b58;
extern int g_103a2c5c;

int sub_1033d9f0(int a0, int a1)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4166
    unsigned long v12;  // 4170
    unsigned int v13;  // eax
    unsigned long v14;  // 4113
    unsigned int v0;  // [bp-0x7c]
    char v1;  // [bp-0x78]
    char v2;  // [bp-0x15]
    int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036fd4f;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v0 = g_1038e180 ^ &v7;
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    v13 = g_103a2b58;
    if (!g_103a2b58)
        v13 = sub_1033d8e0();
    if (!g_103a2b51 && !g_103a2b50)
    {
        if (g_103a2c5c)
        {
            v3 = sub_1032a800(g_103a2c5c, a1);
            g_1038b340(g_103a2c5c, 390, v3, 0);
            v13 = g_1038b2f4(g_103a2c5c);
        }
        else
        {
            sub_103266a0(&v1, &g_103a2b58);
            v6 = 0;
            v2 = sub_1032a610(a0, a1, &v1, 65537) == 2;
            v6 = 4294967295;
            sub_10319f00(&v1);
            v13 = v2;
            if (v13)
                v13 = g_1038b14c(1);
        }
    }
    v14 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v14) = v4;
    return v13;
}
```

## `sub_1033daf0` `0x1033daf0`

_102 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_1033daf0(int a0, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4152
    unsigned int v11;  // eax
    unsigned long v12;  // 4113
    unsigned int v0;  // [bp-0x74]
    char v1;  // [bp-0x70]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036fd72;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_10319e80(&v1, a1);
    v4 = 0;
    sub_1033d9f0(a0, &v1);
    v4 = 4294967295;
    v11 = sub_10319f00(&v1);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v2;
    return v11;
}
```

## `sub_1033db60` `0x1033db60`

_100 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_1033db60(int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4152
    unsigned int v11;  // eax
    unsigned long v12;  // 4113
    unsigned int v0;  // [bp-0x74]
    char v1;  // [bp-0x70]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036fd95;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_1031e1d0(&v1, a0);
    v4 = 0;
    sub_1033d9f0(0, &v1);
    v4 = 4294967295;
    v11 = sub_10319f00(&v1);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v2;
    return v11;
}
```

## `sub_1033dbd0` `0x1033dbd0`

_102 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_1033dbd0(int a0, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4152
    unsigned int v11;  // eax
    unsigned long v12;  // 4113
    unsigned int v0;  // [bp-0x74]
    char v1;  // [bp-0x70]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036fdb8;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_1031e1d0(&v1, a1);
    v4 = 0;
    sub_1033d9f0(a0, &v1);
    v4 = 4294967295;
    v11 = sub_10319f00(&v1);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v2;
    return v11;
}
```

## `sub_1033dc40` `0x1033dc40`

_100 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_1033dc40(unsigned int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4152
    unsigned int v11;  // eax
    unsigned long v12;  // 4113
    unsigned int v0;  // [bp-0x74]
    char v1;  // [bp-0x70]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036fddb;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_103266a0(&v1, a0);
    v4 = 0;
    sub_1033d9f0(0, &v1);
    v4 = 4294967295;
    v11 = sub_10319f00(&v1);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v2;
    return v11;
}
```

## `sub_1033dcb0` `0x1033dcb0`

_102 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_1033dcb0(int a0, unsigned int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4152
    unsigned int v11;  // eax
    unsigned long v12;  // 4113
    unsigned int v0;  // [bp-0x74]
    char v1;  // [bp-0x70]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036fdfe;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_103266a0(&v1, a1);
    v4 = 0;
    sub_1033d9f0(a0, &v1);
    v4 = 4294967295;
    v11 = sub_10319f00(&v1);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v2;
    return v11;
}
```

## `sub_1033dd20` `0x1033dd20`

_100 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_1033dd20(unsigned int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4152
    unsigned int v11;  // eax
    unsigned long v12;  // 4113
    unsigned int v0;  // [bp-0x74]
    char v1;  // [bp-0x70]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036fe21;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_10326770(&v1, a0);
    v4 = 0;
    sub_1033d9f0(0, &v1);
    v4 = 4294967295;
    v11 = sub_10319f00(&v1);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v2;
    return v11;
}
```

## `sub_1033dd90` `0x1033dd90`

_102 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_1033dd90(int a0, unsigned int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4152
    unsigned int v11;  // eax
    unsigned long v12;  // 4113
    unsigned int v0;  // [bp-0x74]
    char v1;  // [bp-0x70]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036fe44;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_10326770(&v1, a1);
    v4 = 0;
    sub_1033d9f0(a0, &v1);
    v4 = 4294967295;
    v11 = sub_10319f00(&v1);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v2;
    return v11;
}
```

## `sub_1033de00` `0x1033de00`

_275 bytes. refs "-%u", ".DbgLog"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b1d4;
extern unsigned int g_1038e180;
extern char g_1038f8e4;

int sub_1033de00(unsigned int a0, int a1)
{
    char v0;  // [bp-0x11c]
    char v1;  // [bp-0x11b]
    unsigned int v2;  // [bp-0x10]
    char *v3;  // [bp-0xc]
    char *v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v2 = g_1038e180 ^ &v5;
    if (!a0)
        a0 = g_1038b050(0);
    v0 = g_1038f8e4;
    sub_10350ad0(&v1, 0, 259);
    g_1038b1d4(a0, &v0, 260);
    v3 = sub_103124a0(&v0, 92);
    if (!v3)
        v3 = &v0;
    v4 = sub_103124a0(&v0, 46);
    if (!v4 || v4 < v3)
        v4 = sub_10312480(&v0, 0);
    if (a1)
    {
        sub_10353127(v4, "-%u", a1);
        v4 = sub_10312480(v4, 0);
    }
    sub_10352cb0(v4, ".DbgLog");
    sub_10352cb0("C:\\Archivos de programa\\ElfBot NG\\elfbot-2.DbgLog", &v0);
    return sub_10351225();
}
```

## `sub_1033df20` `0x1033df20`

_245 bytes. refs "%1%.%2$03d --- "_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b150;
extern unsigned int g_1038e180;

int sub_1033df20(int a0)
{
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    unsigned short v14;  // fs
    unsigned long v15;  // 4141
    unsigned long v16;  // 4158
    unsigned long v19;  // 4118
    unsigned int v0;  // [bp-0x10c]
    unsigned int v1;  // [bp-0x108]
    unsigned int v2;  // [bp-0x104]
    char v3;  // [bp-0x58]
    char v4;  // [bp-0x4a]
    char v5;  // [bp-0x48]
    unsigned int v6;  // [bp-0x1c]
    char v7;  // [bp-0x18]
    unsigned int v8;  // [bp-0x10]
    unsigned int v9;  // [bp-0xc]
    char v10;  // [bp-0x8], Other Possible Types: unsigned int
    char v11;  // [bp-0x4]

    v10 = 4294967295;
    v9 = sub_1036fe89;
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    v8 = *((int *)v15);
    v6 = g_1038e180 ^ &v11;
    v16 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v16) = &v8;
    v2 = 0;
    g_1038b150(&v3, v6);
    sub_1033e040(&v7);
    sub_1035537e(&v5, 44, "%c", sub_1033e020(&v7));
    v1 = sub_1033ee80("%1%.%2$03d --- ", &v5, &v4);
    v0 = v1;
    v10 = 1;
    sub_1033eff0();
    sub_1033ef90(a0, sub_1033f010());
    v2 |= 1;
    v10 = 0;
    sub_1033e060();
    v19 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int *)v19) = v8;
    return sub_10351225();
}
```

## `sub_1033e020` `0x1033e020`

_17 bytes. (leaf/helper — see body)_

```c
int sub_1033e020(int a0)
{
    char v0;  // [bp+0x0]

    return sub_10355660(a0, &v0);
}
```

## `sub_1033e040` `0x1033e040`

_17 bytes. (leaf/helper — see body)_

```c
int sub_1033e040(int a0)
{
    char v0;  // [bp+0x0]

    return sub_1035410c(a0, &v0);
}
```

