# elfbot.dll decompiled — jiru 0x1032b5e3..0x1032d4e0

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1032b5e3` `0x1032b5e3`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032b5e3(void)
{
}
```

## `sub_1032b620` `0x1032b620`

_210 bytes. refs "DefDlgProcW"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b29c;
extern unsigned int g_1038e180;
extern unsigned int g_103a2a28;
extern int g_103a2a70;

unsigned int sub_1032b620(int a0, int a1, int a2, int a3)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4165
    unsigned long v11;  // 4169
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    char *v0;  // [bp-0x3c]
    unsigned int v1;  // [bp-0x30]
    char v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char v5;  // [bp-0x8], Other Possible Types: unsigned int
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036cdc6;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v1 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    if (!((char)g_103a2a28 & 1))
    {
        g_103a2a28 = g_103a2a28 | 1;
        v5 = 0;
        sub_10314590(&v2, "DefDlgProcW");
        v5 = 1;
        v0 = &v2;
        sub_1032e510(&v2, &g_103a2a70, 1);
        v5 = 0;
        sub_10314610(&v2);
        v5 = 4294967295;
    }
    v12 = (!(char)sub_1032e630(v0) ? g_1038b29c(a0, a1, a2, a3) : sub_1032e760(a0, a1, a2, a3));
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v3;
    return v12;
}
```

## `sub_1032b6cb` `0x1032b6cb`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032b6cb(void)
{
}
```

## `sub_1032b700` `0x1032b700`

_210 bytes. refs "DefWindowProcW"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b320;
extern unsigned int g_1038e180;
extern unsigned int g_103a2a30;
extern int g_103a2a70;

unsigned int sub_1032b700(int a0, int a1, int a2, int a3)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4165
    unsigned long v11;  // 4169
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    char *v0;  // [bp-0x3c]
    unsigned int v1;  // [bp-0x30]
    char v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char v5;  // [bp-0x8], Other Possible Types: unsigned int
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036cdf7;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v1 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    if (!((char)g_103a2a30 & 1))
    {
        g_103a2a30 = g_103a2a30 | 1;
        v5 = 0;
        sub_10314590(&v2, "DefWindowProcW");
        v5 = 1;
        v0 = &v2;
        sub_1032e510(&v2, &g_103a2a70, 1);
        v5 = 0;
        sub_10314610(&v2);
        v5 = 4294967295;
    }
    v12 = (!(char)sub_1032e630(v0) ? g_1038b320(a0, a1, a2, a3) : sub_1032e760(a0, a1, a2, a3));
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v3;
    return v12;
}
```

## `sub_1032b7ab` `0x1032b7ab`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032b7ab(void)
{
}
```

## `sub_1032b7e0` `0x1032b7e0`

_132 bytes. (leaf/helper — see body)_

```c
extern int g_1038b368;
extern unsigned int g_1038e180;

int sub_1032b7e0(int a0, int a1, int a2, int a3, int a4, int a5, int a6)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4139
    unsigned long v9;  // 4153
    unsigned long v10;  // 4134
    char v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]
    char v4;  // [bp-0x4]

    v3 = 4294967295;
    v2 = sub_1036ce2b;
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v1 = *((int *)v8);
    v9 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v9) = &v1;
    sub_1033a4c0(g_1038b368, g_1038e180 ^ &v4, 0);
    sub_1032c850(a0, &v0, a1, a2, a3, a4, a5, a6);
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v10) = v1;
    return a0;
}
```

## `sub_1032b870` `0x1032b870`

_170 bytes. (leaf/helper — see body)_

```c
extern int g_1038b364;
extern unsigned int g_1038e180;
extern int g_103a2a34;
extern unsigned int g_103a2a38;

int sub_1032b870(int a0, int a1, int a2, int a3, int a4, int a5, int a6)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4169
    unsigned int v10;  // ecx
    unsigned long v11;  // 4173
    unsigned long v12;  // 4134
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036ce6d;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = v10;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v2;
    v1 = 0;
    if (!((char)g_103a2a38 & 1))
    {
        g_103a2a38 = g_103a2a38 | 1;
        v4 = 1;
        sub_1033a4c0(g_1038b364);
        v4 = 0;
    }
    sub_1032c850(a0, &g_103a2a34, a1, a2, a3, a4, a5, a6);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v2;
    return a0;
}
```

## `sub_1032b920` `0x1032b920`

_406 bytes. refs "GetOpenFileNameW"_

```c
extern unsigned int g_1038e180;
extern int g_103a2a3c;
extern unsigned int g_103a2a40;
extern int g_103a2a90;

int sub_1032b920(int a0, int a1, int a2, int a3, int a4, int a5, int a6)
{
    unsigned long v14;  // ldt
    unsigned long v15;  // gdt
    unsigned short v16;  // fs
    unsigned long v17;  // 4168
    unsigned long v18;  // 4172
    int v19;  // eax
    unsigned long v20;  // 4113
    char *v0;  // [bp-0xd0]
    unsigned int v1;  // [bp-0xc4]
    int v2;  // [bp-0xc0]
    int v3;  // [bp-0xbc]
    unsigned int v4;  // [bp-0xb8]
    unsigned int v5;  // [bp-0xb4]
    unsigned int v6;  // [bp-0xb0]
    char v7;  // [bp-0xac]
    char v8;  // [bp-0x8c]
    char v9;  // [bp-0x2c]
    unsigned int v10;  // [bp-0x10]
    unsigned int v11;  // [bp-0xc]
    unsigned int v12;  // [bp-0x8], Other Possible Types: char
    char v13;  // [bp-0x4]

    v12 = 4294967295;
    v11 = sub_1036ced3;
    v17 = _ccall(v14, v15, (unsigned int)v16, 0);
    v10 = *((int *)v17);
    v1 = g_1038e180 ^ &v13;
    v18 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int **)v18) = &v10;
    v6 = 0;
    if (!((char)g_103a2a40 & 1))
    {
        g_103a2a40 = g_103a2a40 | 1;
        v12 = 1;
        sub_10314590(&v9, "GetOpenFileNameW");
        v12 = 2;
        v0 = &v9;
        sub_1032ea80(&v9, &g_103a2a90, 1);
        v12 = 1;
        sub_10314610(&v9);
        v12 = 0;
    }
    if ((char)sub_1032e630(v0))
    {
        sub_1032cb00(a0, &g_103a2a3c, a1, a2, a3, a4, a5, a6);
        v12 = 0;
        v6 |= 1;
        v19 = a0;
    }
    else
    {
        v5 = sub_1032b7e0(&v7, a1, a2, a3, a4, a5, a6);
        v4 = v5;
        v12 = 3;
        v3 = sub_10326840(&v8, v4);
        v2 = v3;
        v12 = 4;
        sub_10327230(v2, a0);
        v6 |= 1;
        v12 = 3;
        sub_10319f00(&v8);
        v12 = 0;
        sub_1031a040(&v7);
        v19 = a0;
    }
    v20 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int *)v20) = v10;
    return v19;
}
```

## `sub_1032ba00` `0x1032ba00`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1032ba00(void)
{
}
```

## `sub_1032bac0` `0x1032bac0`

_406 bytes. refs "GetSaveFileNameW"_

```c
extern unsigned int g_1038e180;
extern int g_103a2a44;
extern unsigned int g_103a2a48;
extern int g_103a2a90;

int sub_1032bac0(int a0, int a1, int a2, int a3, int a4, int a5, int a6)
{
    unsigned long v14;  // ldt
    unsigned long v15;  // gdt
    unsigned short v16;  // fs
    unsigned long v17;  // 4168
    unsigned long v18;  // 4172
    int v19;  // eax
    unsigned long v20;  // 4113
    char *v0;  // [bp-0xd0]
    unsigned int v1;  // [bp-0xc4]
    int v2;  // [bp-0xc0]
    int v3;  // [bp-0xbc]
    unsigned int v4;  // [bp-0xb8]
    unsigned int v5;  // [bp-0xb4]
    unsigned int v6;  // [bp-0xb0]
    char v7;  // [bp-0xac]
    char v8;  // [bp-0x8c]
    char v9;  // [bp-0x2c]
    unsigned int v10;  // [bp-0x10]
    unsigned int v11;  // [bp-0xc]
    unsigned int v12;  // [bp-0x8], Other Possible Types: char
    char v13;  // [bp-0x4]

    v12 = 4294967295;
    v11 = sub_1036cf3c;
    v17 = _ccall(v14, v15, (unsigned int)v16, 0);
    v10 = *((int *)v17);
    v1 = g_1038e180 ^ &v13;
    v18 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int **)v18) = &v10;
    v6 = 0;
    if (!((char)g_103a2a48 & 1))
    {
        g_103a2a48 = g_103a2a48 | 1;
        v12 = 1;
        sub_10314590(&v9, "GetSaveFileNameW");
        v12 = 2;
        v0 = &v9;
        sub_1032ea80(&v9, &g_103a2a90, 1);
        v12 = 1;
        sub_10314610(&v9);
        v12 = 0;
    }
    if ((char)sub_1032e630(v0))
    {
        sub_1032cb00(a0, &g_103a2a44, a1, a2, a3, a4, a5, a6);
        v12 = 0;
        v6 |= 1;
        v19 = a0;
    }
    else
    {
        v5 = sub_1032b870(&v7, a1, a2, a3, a4, a5, a6);
        v4 = v5;
        v12 = 3;
        v3 = sub_10326840(&v8, v4);
        v2 = v3;
        v12 = 4;
        sub_10327230(v2, a0);
        v6 |= 1;
        v12 = 3;
        sub_10319f00(&v8);
        v12 = 0;
        sub_1031a040(&v7);
        v19 = a0;
    }
    v20 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int *)v20) = v10;
    return v19;
}
```

## `sub_1032bba0` `0x1032bba0`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1032bba0(void)
{
}
```

## `sub_1032bc60` `0x1032bc60`

_232 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1d4;
extern unsigned int g_1038e180;
extern int g_10390370;

unsigned int sub_1032bc60(unsigned int a0, unsigned int a1)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4140
    unsigned long v12;  // 4154
    unsigned int v13;  // eax
    unsigned int v14;  // eax
    unsigned long v15;  // 4113
    int v0;  // [bp-0x48]
    int v1;  // [bp-0x44]
    unsigned int v2;  // [bp-0x40]
    char v3;  // [bp-0x3c]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8], Other Possible Types: char
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036cf83;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    v2 = 0;
    sub_10333ef0(260, 0, g_1038e180 ^ &v7);
    v6 = 1;
    v13 = sub_1032e2e0(0, 260);
    if (!g_1038b1d4(a1, v13))
    {
        sub_1032dfc0(g_10390370);
        v2 |= 1;
        v6 = 0;
        sub_1032e280(g_10390370);
        v14 = a0;
    }
    else
    {
        v1 = sub_10314590(&v3, sub_1032e2e0(0));
        v0 = v1;
        v6 = 2;
        sub_1032e020(v0);
        v2 |= 1;
        v6 = 1;
        sub_10314610(&v3);
        v6 = 0;
        sub_1032e280();
        v14 = a0;
    }
    v15 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v15) = v4;
    return v14;
}
```

## `sub_1032bd50` `0x1032bd50`

_528 bytes. refs "GetModuleFileNameW"_

```c
extern unsigned int g_1038e180;
extern int g_10390370;
extern unsigned int g_103a2a50;
extern int g_103a2aac;

int sub_1032bd50(int a0, unsigned int a1)
{
    unsigned long v17;  // ldt
    unsigned long v18;  // gdt
    unsigned short v19;  // fs
    unsigned long v20;  // 4168
    unsigned long v21;  // 4172
    int v22;  // eax
    unsigned long v23;  // 4113
    char *v0;  // [bp-0x104]
    unsigned int v1;  // [bp-0xf8]
    int v2;  // [bp-0xf4]
    int v3;  // [bp-0xf0]
    unsigned int v4;  // [bp-0xec]
    unsigned int v5;  // [bp-0xe8]
    int v6;  // [bp-0xe4]
    int v7;  // [bp-0xe0]
    unsigned int v8;  // [bp-0xdc]
    char v9;  // [bp-0xd8]
    char v10;  // [bp-0xb8]
    char v11;  // [bp-0x58]
    char v12;  // [bp-0x3c]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8], Other Possible Types: char
    char v16;  // [bp-0x4]

    v15 = 4294967295;
    v14 = sub_1036cff9;
    v20 = _ccall(v17, v18, (unsigned int)v19, 0);
    v13 = *((int *)v20);
    v1 = g_1038e180 ^ &v16;
    v21 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((unsigned int **)v21) = &v13;
    v8 = 0;
    if (!((char)g_103a2a50 & 1))
    {
        g_103a2a50 = g_103a2a50 | 1;
        v15 = 1;
        sub_10314590(&v12, "GetModuleFileNameW");
        v15 = 2;
        v0 = &v12;
        sub_1032eab0(&v12, &g_103a2aac, 1);
        v15 = 1;
        sub_10314610(&v12);
        v15 = 0;
    }
    if ((char)sub_1032e630(v0))
    {
        sub_10333f40(260, 0);
        v15 = 3;
        if (!sub_1032eae0(a1, sub_1032e410(0, 260)))
        {
            sub_10325820(a0, g_10390370);
            v8 |= 1;
            v15 = 0;
            sub_1032e3f0(a1);
            v22 = a0;
        }
        else
        {
            v7 = sub_1031fc10(&v11, sub_1032e410(0));
            v6 = v7;
            v15 = 4;
            sub_10325880(a0, v6);
            v8 |= 1;
            v15 = 3;
            sub_1031a3a0(&v11);
            v15 = 0;
            sub_1032e3f0();
            v22 = a0;
        }
    }
    else
    {
        v5 = sub_1032bc60(&v9, a1);
        v4 = v5;
        v15 = 5;
        v3 = sub_10326840(&v10, v4);
        v2 = v3;
        v15 = 6;
        sub_10327230(v2, a0);
        v8 |= 1;
        v15 = 5;
        sub_10319f00(&v10);
        v15 = 0;
        sub_1031a040(&v9);
        v22 = a0;
    }
    v23 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((unsigned int *)v23) = v13;
    return v22;
}
```

## `sub_1032bebe` `0x1032bebe`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1032bebe(void)
{
}
```

## `sub_1032bf70` `0x1032bf70`

_878 bytes. refs "CreateProcessW"_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

typedef struct struct_1 {
    char padding_0[4];
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
    unsigned int field_10;
    unsigned int field_14;
    unsigned int field_18;
    unsigned int field_1c;
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
    unsigned short field_30;
    unsigned short field_32;
    char padding_34[4];
    unsigned int field_38;
    unsigned int field_3c;
    unsigned int field_40;
} struct_1;

extern struct_0 *g_1038b134;
extern unsigned int g_1038e180;
extern unsigned int g_103a2a58;
extern int g_103a2aac;

int sub_1032bf70(int a0, int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, int a6, int a7, struct_1 *a8, unsigned int a9)
{
    unsigned long v39;  // ldt
    unsigned long v40;  // gdt
    unsigned int v49[2];  // eax
    int v50[2];  // eax
    int v51;  // eax
    unsigned long v52;  // 4114
    unsigned short v41;  // fs
    unsigned long v42;  // 4169
    unsigned long v43;  // 4173
    unsigned int v44[2];  // eax
    int v45[2];  // eax
    int v46[2];  // eax
    unsigned int v47;  // eax
    unsigned int v48[2];  // eax
    unsigned int v0;  // [bp-0x288]
    unsigned int v1;  // [bp-0x284]
    unsigned int v2;  // [bp-0x280]
    unsigned int v3;  // [bp-0x27c]
    unsigned int v4;  // [bp-0x278]
    struct_0 *v5;  // [bp-0x274], Other Possible Types: unsigned int
    struct_0 *v6;  // [bp-0x270], Other Possible Types: int
    struct_1 *v7;  // [bp-0x26c], Other Possible Types: int
    char *v8;  // [bp-0x268], Other Possible Types: unsigned int
    unsigned int v9;  // [bp-0x264]
    unsigned int v10;  // [bp-0x260]
    unsigned int v11;  // [bp-0x25c]
    char *v12;  // [bp-0x258]
    unsigned int v13;  // [bp-0x24c]
    unsigned int v14;  // [bp-0x248]
    unsigned int v15;  // [bp-0x244]
    unsigned int v16;  // [bp-0x240]
    char v17;  // [bp-0x239]
    char v18;  // [bp-0x238]
    char v19;  // [bp-0x230]
    char v20;  // [bp-0x228]
    char v21;  // [bp-0x220]
    unsigned int v22;  // [bp-0x218]
    unsigned short v23;  // [bp-0x212]
    char v24;  // [bp-0x210]
    char v25;  // [bp-0x208]
    char v26;  // [bp-0x200]
    char v27;  // [bp-0x1f8]
    char v28;  // [bp-0x1f0]
    char v29;  // [bp-0x1d4]
    char v30;  // [bp-0x1b8]
    struct_0 v31;  // [bp-0x1a8]
    struct_0 v32;  // [bp-0x40]
    unsigned int v33;  // [bp-0x24]
    char v34;  // [bp-0x20]
    unsigned int v35;  // [bp-0x10]
    unsigned int v36;  // [bp-0xc]
    unsigned int v37;  // [bp-0x8], Other Possible Types: char
    char v38;  // [bp-0x4]

    v37 = 4294967295;
    v36 = sub_1036d061;
    v42 = _ccall(v39, v40, (unsigned int)v41, 0);
    v35 = *((int *)v42);
    v33 = g_1038e180 ^ &v38;
    v13 = v33;
    v43 = _ccall(v39, v40, (unsigned int)v41, 0);
    *((unsigned int **)v43) = &v35;
    if (!((char)g_103a2a58 & 1))
    {
        g_103a2a58 = g_103a2a58 | 1;
        v37 = 0;
        sub_10314590(&v28, "CreateProcessW");
        v37 = 1;
        v12 = &v28;
        sub_1032eb00(&v28, &g_103a2aac, 1);
        v37 = 0;
        sub_10314610(&v28);
        v37 = 4294967295;
    }
    if ((char)sub_1032e630(v12))
    {
        sub_1032e380();
        v37 = 2;
        if (!sub_103275b0(a1))
        {
            sub_10326c30(a1, &v32);
            v37 = 3;
            v44 = sub_10334430(&v27, &v34);
            v11 = v44[1];
            v10 = v44[0];
            v45 = sub_10326160(&v32, &v26);
            v46 = sub_1032daf0(&v25, v45[0], v45[1]);
            sub_103343c0(&v24, v46[0], v46[1]);
            v23 = 0;
            sub_1032e440(&v23);
            v37 = 2;
            sub_1031a3a0(&v32);
        }
        v15 = (!sub_103275b0(a1) ? sub_1032e410(0) : 0);
        v8 = a9;
        v7 = a8;
        v6 = sub_10326fd0(a7);
        v5 = sub_10327150(a6);
        v4 = a5 | 0x400;
        v3 = a4;
        v2 = a3;
        v1 = a2;
        v0 = v15;
        v47 = sub_10326fd0(a0);
        v22 = sub_1032eb30(v47);
        v37 = 4294967295;
        sub_1032e3f0(v47);
    }
    else
    {
        sub_1032e210();
        v37 = 4;
        if (!sub_103275b0(a1))
        {
            sub_10326a70(a1, &v29);
            v37 = 5;
            v48 = sub_10334430(&v21, &v30);
            v11 = v48[1];
            v10 = v48[0];
            v49 = sub_1031b790(&v29, &v20);
            v9 = v49[1];
            v8 = v49[0];
            v50 = sub_1031b6e0(&v29, &v19);
            sub_10334450(&v18, v50[0], v50[1]);
            v17 = 0;
            sub_1032e310(&v17);
            v37 = 4;
            sub_10314610(&v29);
        }
        sub_10327830(&v31, a8);
        v37 = 6;
        v14 = (!sub_103275b0(a1) ? sub_1032e2e0(0) : 0);
        v9 = a9;
        v8 = &v31.padding_0[0];
        v7 = sub_10326e70(a7);
        v6 = sub_10327130(a6);
        v5 = a5 & 4294966271;
        v4 = a4;
        v3 = a3;
        v2 = a2;
        v1 = v14;
        v51 = sub_10326e70(a0);
        v16 = g_1038b134(v51);
        v37 = 4;
        sub_1032d910(v51);
        v37 = 4294967295;
        sub_1032e280();
    }
    v52 = _ccall(v39, v40, (unsigned int)v41, 0);
    *((unsigned int *)v52) = v35;
    return sub_10351225();
}
```

## `sub_1032c151` `0x1032c151`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1032c151(void)
{
}
```

## `sub_1032c2f0` `0x1032c2f0`

_107 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b138;
extern unsigned int g_1038e180;

int sub_1032c2f0(unsigned int a0)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4141
    unsigned long v9;  // 4155
    unsigned long v10;  // 4131
    unsigned int v0;  // [bp-0x58]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]
    char v4;  // [bp-0x4]

    v3 = 4294967295;
    v2 = sub_1036d0a2;
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v1 = *((int *)v8);
    v9 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v9) = &v1;
    v0 = 0x44;
    g_1038b138(&v0, g_1038e180 ^ &v4, 0, 0x44);
    sub_1032d990(&v0);
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v10) = v1;
    return a0;
}
```

## `sub_1032c360` `0x1032c360`

_300 bytes. refs "GetStartupInfoW"_

```c
typedef struct struct_0 {
    unsigned int field_0;
    struct struct_0 *field_4;
    struct struct_0 *field_8;
    struct struct_0 *field_c;
    unsigned int field_10;
    unsigned int field_14;
    unsigned int field_18;
    unsigned int field_1c;
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
    unsigned short field_30;
    unsigned short field_32;
    char padding_34[4];
    unsigned int field_38;
    unsigned int field_3c;
    unsigned int field_40;
} struct_0;

typedef struct struct_1 {
    char padding_0[4];
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
    unsigned int field_10;
    unsigned int field_14;
    unsigned int field_18;
    unsigned int field_1c;
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
    unsigned short field_30;
    unsigned short field_32;
    char padding_34[4];
    unsigned int field_38;
    unsigned int field_3c;
    unsigned int field_40;
} struct_1;

typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

extern struct_0 *g_1038b138;
extern unsigned int g_1038e180;
extern unsigned int g_103a2a60;
extern int g_103a2aac;

struct_0 * sub_1032c360(struct_0 *a0)
{
    unsigned long v11;  // ldt
    unsigned long v12;  // gdt
    unsigned short v13;  // fs
    unsigned long v14;  // 4168
    unsigned long v15;  // 4172
    struct_0 *v16;  // eax
    unsigned long v17;  // 4113
    char *v0;  // [bp-0xd0]
    int v1;  // [bp-0xcc]
    unsigned int v2;  // [bp-0xc4]
    unsigned int v3;  // [bp-0xc0]
    char v4;  // [bp-0xbc]
    struct_1 v5;  // [bp-0xa0]
    unsigned int v6;  // [bp-0x58]
    unsigned int v7;  // [bp-0x10]
    unsigned int v8;  // [bp-0xc]
    char v9;  // [bp-0x8], Other Possible Types: unsigned int
    char v10;  // [bp-0x4]

    v9 = 4294967295;
    v8 = sub_1036d0f5;
    v14 = _ccall(v11, v12, (unsigned int)v13, 0);
    v7 = *((int *)v14);
    v2 = g_1038e180 ^ &v10;
    v15 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int **)v15) = &v7;
    v3 = 0;
    if (!((char)g_103a2a60 & 1))
    {
        g_103a2a60 = g_103a2a60 | 1;
        v9 = 1;
        sub_10314590(&v4, "GetStartupInfoW");
        v9 = 2;
        v1 = &g_103a2aac;
        v0 = &v4;
        sub_1032eb70(&v4, &g_103a2aac, 1);
        v9 = 1;
        sub_10314610(&v4);
        v9 = 0;
    }
    if ((char)sub_1032e630(v0, v1))
    {
        v6 = 0x44;
        sub_10335b10(&v6);
        sub_1032da20(&v6);
        v9 = 0;
        v3 |= 1;
        v16 = a0;
    }
    else
    {
        v5 = (struct_1)0x44;
        g_1038b138(&v5);
        sub_10327a70(a0, &v5);
        v9 = 0;
        v3 |= 1;
        v16 = a0;
    }
    v17 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int *)v17) = v7;
    return v16;
}
```

## `sub_1032c43e` `0x1032c43e`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032c43e(void)
{
}
```

## `sub_1032c490` `0x1032c490`

_91 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b13c;
extern unsigned int g_1038e180;

int sub_1032c490(int a0)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4136
    unsigned int v8;  // eax
    unsigned int v9;  // ecx
    unsigned long v10;  // 4152
    unsigned long v12;  // 4131
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
    sub_10314590(a0, g_1038b13c(g_1038e180 ^ &v2, 0, v8, sub_1036d12c, 4294967295, &v3));
    v12 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v12) = v8;
    return a0;
}
```

## `sub_1032c4f0` `0x1032c4f0`

_360 bytes. refs "GetCommandLineW"_

```c
extern unsigned int g_1038e180;
extern unsigned int g_103a2a68;
extern int g_103a2aac;

unsigned int sub_1032c4f0(unsigned int a0)
{
    unsigned long v14;  // ldt
    unsigned long v15;  // gdt
    unsigned short v16;  // fs
    unsigned long v17;  // 4168
    unsigned long v18;  // 4172
    unsigned int v20;  // eax
    unsigned long v21;  // 4113
    char *v0;  // [bp-0xcc]
    unsigned int v1;  // [bp-0xc0]
    int v2;  // [bp-0xbc]
    int v3;  // [bp-0xb8]
    int v4;  // [bp-0xb4]
    int v5;  // [bp-0xb0]
    unsigned int v6;  // [bp-0xac]
    char v7;  // [bp-0xa8]
    char v8;  // [bp-0x8c]
    char v9;  // [bp-0x2c]
    unsigned int v10;  // [bp-0x10]
    unsigned int v11;  // [bp-0xc]
    unsigned int v12;  // [bp-0x8], Other Possible Types: char
    char v13;  // [bp-0x4]

    v12 = 4294967295;
    v11 = sub_1036d192;
    v17 = _ccall(v14, v15, (unsigned int)v16, 0);
    v10 = *((int *)v17);
    v1 = g_1038e180 ^ &v13;
    v18 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int **)v18) = &v10;
    v6 = 0;
    if (!((char)g_103a2a68 & 1))
    {
        g_103a2a68 = g_103a2a68 | 1;
        v12 = 1;
        sub_10314590(&v9, "GetCommandLineW");
        v12 = 2;
        v0 = &v9;
        sub_1032eba0(&v9, &g_103a2aac, 1);
        v12 = 1;
        sub_10314610(&v9);
        v12 = 0;
    }
    if ((char)sub_1032e630(v0))
    {
        sub_1031fc10(a0, sub_1032ebd0());
        v12 = 0;
        v6 |= 1;
        v20 = a0;
    }
    else
    {
        v5 = sub_1032c490(&v7);
        v4 = v5;
        v12 = 3;
        v3 = sub_10319e80(&v8, v4);
        v2 = v3;
        v12 = 4;
        sub_10326c30(v2, a0);
        v6 |= 1;
        v12 = 3;
        sub_10319f00(&v8);
        v12 = 0;
        sub_10314610(&v7);
        v20 = a0;
    }
    v21 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int *)v21) = v10;
    return v20;
}
```

## `sub_1032c5ba` `0x1032c5ba`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1032c5ba(void)
{
}
```

## `sub_1032c660` `0x1032c660`

_444 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

extern unsigned int g_1038e180;

int sub_1032c660(unsigned int a0)
{
    unsigned long v17;  // ldt
    unsigned long v18;  // gdt
    unsigned short v19;  // fs
    unsigned long v20;  // 4139
    unsigned long v21;  // 4156
    struct_0 *v22;  // eax
    unsigned int v23[2];  // eax
    unsigned short *v24;  // eax
    int v25;  // eax
    unsigned long v26;  // 4118
    unsigned int v0;  // [bp-0x88]
    unsigned int v1;  // [bp-0x84]
    char v2;  // [bp-0x80]
    char v3;  // [bp-0x78]
    char v4;  // [bp-0x6d]
    unsigned int v5;  // [bp-0x6c]
    unsigned int v6;  // [bp-0x68]
    char v7;  // [bp-0x64]
    struct_0 v8;  // [bp-0x54]
    struct_0 v9;  // [bp-0x38]
    unsigned int v10;  // [bp-0x1c]
    struct_0 v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8], Other Possible Types: char
    char v16;  // [bp-0x4]

    v15 = 4294967295;
    v14 = sub_1036d1e1;
    v20 = _ccall(v17, v18, (unsigned int)v19, 0);
    v13 = *((int *)v20);
    v10 = g_1038e180 ^ &v16;
    v0 = v10;
    v21 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((unsigned int **)v21) = &v13;
    v1 = 0;
    sub_1032c4f0(&v9);
    v15 = 1;
    sub_103257a0(&v8);
    v15 = 2;
    sub_1032ebf0();
    v15 = 3;
    v22 = sub_1032daf0(&v3);
    v11 = (struct_0)v22->padding_0;
    v12 = v22->field_4;
    v23 = sub_10326160(&v9, &v2);
    v5 = v23[0];
    v6 = v23[1];
    while (true)
    {
        if (!(char)sub_10343610(&v5))
        {
            sub_1032ec20(&v7);
            v1 |= 1;
            v15 = 2;
            sub_1032ed00(&v7);
            v15 = 1;
            sub_1031a3a0(&v8);
            v15 = 0;
            sub_1031a3a0(&v9);
            v26 = _ccall(v17, v18, (unsigned int)v19, 0);
            *((unsigned int *)v26) = v13;
            return sub_10351225();
        }
        while ((char)sub_10343610(&v5) && *((short *)sub_10326280(&v11)) == 32)
        {
            sub_1032e4b0();
        }
        v4 = 0;
        if ((char)sub_10343610(&v5))
        {
            if (*((short *)sub_10326280(&v11)) == 0x22)
            {
                sub_1032e4b0();
                if (!v4)
                {
                    v4 = 1;
                    return sub_1032c76b();
                }
            }
            else if (*((short *)sub_10326280(&v11)) != 32 || v4)
            {
                break;
            }
        }
        if (!(char)sub_10325be0(&v8))
        {
            sub_1032ed20(&v8);
            sub_1032dab0(&v8);
        }
    }
    v24 = sub_10326280(&v11);
    v25 = _INSERT(v24, 0, *(v24));
    sub_1032db20(v25);
    sub_1032e4b0(v25);
}
```

## `sub_1032c765` `0x1032c765`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032c765(void)
{
    sub_1032c76b();
    return;
}
```

## `sub_1032c76b` `0x1032c76b`

_4 bytes. (leaf/helper — see body)_

```c
void sub_1032c76b(void)
{
}
```

## `sub_1032c787` `0x1032c787`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032c787(void)
{
}
```

## `sub_1032c830` `0x1032c830`

_17 bytes. (leaf/helper — see body)_

```c
int sub_1032c830(int a0)
{
    char v0;  // [bp+0x0]

    return sub_103547c6(a0, &v0);
}
```

## `sub_1032c850` `0x1032c850`

_473 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern int g_10390370;

int sub_1032c850(unsigned int a0, unsigned int a1, unsigned int a2, int a3, int a4, int a5, unsigned int a6, int a7)
{
    unsigned long v23;  // ldt
    unsigned long v24;  // gdt
    unsigned short v25;  // fs
    unsigned long v26;  // 4139
    unsigned long v27;  // 4156
    unsigned long v28;  // 4118
    unsigned int v0;  // [bp-0x130]
    int v1;  // [bp-0x12c]
    int v2;  // [bp-0x128]
    unsigned int v3;  // [bp-0x124]
    char v4;  // [bp-0x120]
    char v5;  // [bp-0x101]
    char v6;  // [bp-0x100]
    char v7;  // [bp-0xf0], Other Possible Types: unsigned int
    unsigned int v8;  // [bp-0xec]
    int v9;  // [bp-0xe4]
    unsigned int v10;  // [bp-0xd8]
    unsigned int v11;  // [bp-0xd4]
    int v12;  // [bp-0xd0]
    int v13;  // [bp-0xc4]
    unsigned int v14;  // [bp-0xbc]
    int v15;  // [bp-0xb4]
    char v16;  // [bp-0x98]
    char v17;  // [bp-0x78]
    unsigned int v18;  // [bp-0x14]
    unsigned int v19;  // [bp-0x10]
    unsigned int v20;  // [bp-0xc]
    unsigned int v21;  // [bp-0x8], Other Possible Types: char
    char v22;  // [bp-0x4]

    v21 = 4294967295;
    v20 = sub_1036d24e;
    v26 = _ccall(v23, v24, (unsigned int)v25, 0);
    v19 = *((int *)v26);
    v18 = g_1038e180 ^ &v22;
    v0 = v18;
    v27 = _ccall(v23, v24, (unsigned int)v25, 0);
    *((unsigned int **)v27) = &v19;
    v3 = 0;
    sub_103266a0(&v17, ".");
    v21 = 1;
    v5 = 0;
    sub_1032e240(a3, &v5);
    v21 = 2;
    sub_1032ca30(&v6, a4);
    sub_10350ad0(&v7, 0, 76);
    v7 = 76;
    v8 = a2;
    v9 = sub_103273b0(a5);
    v10 = 1;
    v11 = sub_1032e2e0(0);
    v13 = sub_103273b0(&v17);
    v12 = a3;
    v14 = a6;
    v15 = sub_103273b0(a7);
    sub_1032dfc0(g_10390370);
    v21 = 3;
    if (sub_10335b10(&v7))
    {
        v2 = sub_10314590(&v4, sub_1032e2e0(0));
        v1 = v2;
        v21 = 4;
        sub_1032e080(v1);
        v21 = 3;
        sub_10314610(&v4);
    }
    sub_10335a50(&v16);
    v3 |= 1;
    v21 = 2;
    sub_1031a040(&v16);
    v21 = 1;
    sub_1032e280();
    v21 = 0;
    sub_10319f00(&v17);
    v28 = _ccall(v23, v24, (unsigned int)v25, 0);
    *((unsigned int *)v28) = v19;
    return sub_10351225();
}
```

## `sub_1032ca30` `0x1032ca30`

_194 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

extern unsigned int g_1038e180;

int sub_1032ca30(unsigned int a0, int a1)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4136
    unsigned long v12;  // 4153
    unsigned long v14;  // 4114
    unsigned int v0;  // [bp-0x40]
    char v1;  // [bp-0x3c]
    struct_0 v2;  // [bp-0x30]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036d27e;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v3 = g_1038e180 ^ &v7;
    v0 = v3;
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    if (!sub_103275b0(a1))
    {
        sub_10326a70(a1, &v2);
        v6 = 0;
        if (!(char)sub_10325be0(&v2))
        {
            sub_10334180(&v1);
            if (*((char *)sub_103341b0(&v1)) == 92)
                sub_103170d0(&v2, 42);
        }
        sub_10352cb0(sub_1032e2e0(0, (unsigned int)sub_102ec9a0(&v2)));
        v6 = 4294967295;
        sub_10314610(&v2);
    }
    v14 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v14) = v4;
    return sub_10351225();
}
```

## `sub_1032cb00` `0x1032cb00`

_475 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

extern unsigned int g_1038e180;
extern int g_10390370;

int sub_1032cb00(unsigned int a0, unsigned int a1, unsigned int a2, int a3, int a4, int a5, unsigned int a6, int a7)
{
    unsigned long v23;  // ldt
    unsigned long v24;  // gdt
    unsigned short v25;  // fs
    unsigned long v26;  // 4139
    unsigned long v27;  // 4156
    unsigned long v28;  // 4118
    unsigned int v0;  // [bp-0x130]
    int v1;  // [bp-0x12c]
    int v2;  // [bp-0x128]
    unsigned int v3;  // [bp-0x124]
    char v4;  // [bp-0x120]
    unsigned short v5;  // [bp-0x102]
    char v6;  // [bp-0x100]
    char v7;  // [bp-0xf0], Other Possible Types: unsigned int
    unsigned int v8;  // [bp-0xec]
    struct_0 *v9;  // [bp-0xe4]
    unsigned int v10;  // [bp-0xd8]
    unsigned int v11;  // [bp-0xd4]
    int v12;  // [bp-0xd0]
    struct_0 *v13;  // [bp-0xc4]
    unsigned int v14;  // [bp-0xbc]
    struct_0 *v15;  // [bp-0xb4]
    char v16;  // [bp-0x98]
    char v17;  // [bp-0x78]
    unsigned int v18;  // [bp-0x14]
    unsigned int v19;  // [bp-0x10]
    unsigned int v20;  // [bp-0xc]
    unsigned int v21;  // [bp-0x8], Other Possible Types: char
    char v22;  // [bp-0x4]

    v21 = 4294967295;
    v20 = sub_1036d2eb;
    v26 = _ccall(v23, v24, (unsigned int)v25, 0);
    v19 = *((int *)v26);
    v18 = g_1038e180 ^ &v22;
    v0 = v18;
    v27 = _ccall(v23, v24, (unsigned int)v25, 0);
    *((unsigned int **)v27) = &v19;
    v3 = 0;
    sub_103266a0(&v17, ".");
    v21 = 1;
    v5 = 0;
    sub_1032e3b0(a3, &v5);
    v21 = 2;
    sub_1032cce0(&v6, a4);
    sub_10350ad0(&v7, 0, 76);
    v7 = 76;
    v8 = a2;
    v9 = sub_103273d0(a5);
    v10 = 1;
    v11 = sub_1032e410(0);
    v13 = sub_103273d0(&v17);
    v12 = a3;
    v14 = a6;
    v15 = sub_103273d0(a7);
    sub_10325820(&v16, g_10390370);
    v21 = 3;
    if (sub_10335b10(&v7))
    {
        v2 = sub_1031fc10(&v4, sub_1032e410(0));
        v1 = v2;
        v21 = 4;
        sub_1032e0c0(v1);
        v21 = 3;
        sub_1031a3a0(&v4);
    }
    sub_10335ab0(&v16);
    v3 |= 1;
    v21 = 2;
    sub_1031a0e0(&v16);
    v21 = 1;
    sub_1032e3f0();
    v21 = 0;
    sub_10319f00(&v17);
    v28 = _ccall(v23, v24, (unsigned int)v25, 0);
    *((unsigned int *)v28) = v19;
    return sub_10351225();
}
```

## `sub_1032cce0` `0x1032cce0`

_194 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1032cce0(unsigned int a0, int a1)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4136
    unsigned long v12;  // 4153
    unsigned long v14;  // 4114
    unsigned int v0;  // [bp-0x40]
    char v1;  // [bp-0x3c]
    char v2;  // [bp-0x30]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036d31b;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v3 = g_1038e180 ^ &v7;
    v0 = v3;
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    if (!sub_103275b0(a1))
    {
        sub_10326c30(a1, &v2);
        v6 = 0;
        if (!(char)sub_10325be0(&v2))
        {
            sub_103342f0(&v1);
            if (*((short *)sub_10334320(&v1)) == 92)
                sub_10325f70(&v2, 42);
        }
        sub_10352da8(sub_1032e410(0, sub_1031fc50(&v2)));
        v6 = 4294967295;
        sub_1031a3a0(&v2);
    }
    v14 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v14) = v4;
    return sub_10351225();
}
```

## `sub_1032cdb0` `0x1032cdb0`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032cdb0(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032cdf0` `0x1032cdf0`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032cdf0(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032ce30` `0x1032ce30`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032ce30(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032ce70` `0x1032ce70`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032ce70(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032ceb0` `0x1032ceb0`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032ceb0(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032cef0` `0x1032cef0`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032cef0(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032cf30` `0x1032cf30`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032cf30(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032cf70` `0x1032cf70`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032cf70(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032cfb0` `0x1032cfb0`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032cfb0(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032cff0` `0x1032cff0`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032cff0(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032d030` `0x1032d030`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032d030(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032d070` `0x1032d070`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032d070(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032d0b0` `0x1032d0b0`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032d0b0(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032d0f0` `0x1032d0f0`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032d0f0(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032d130` `0x1032d130`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032d130(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032d170` `0x1032d170`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032d170(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032d1b0` `0x1032d1b0`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032d1b0(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032d1f0` `0x1032d1f0`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032d1f0(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032d230` `0x1032d230`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032d230(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032d270` `0x1032d270`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032d270(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032d2b0` `0x1032d2b0`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032d2b0(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032d2f0` `0x1032d2f0`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032d2f0(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032d330` `0x1032d330`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032d330(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032d370` `0x1032d370`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032d370(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032d3b0` `0x1032d3b0`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032d3b0(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032d3f0` `0x1032d3f0`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032d3f0(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032d430` `0x1032d430`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern char g_103a2a8c;

unsigned int sub_1032d430(int a0, int a1, char a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (a2 && !g_103a2a8c)
        return 0;
    v0 = (unsigned int)sub_102ec9a0(a0);
    v1 = (unsigned int)sub_102ec9a0(a1);
    v2 = g_1038b050(v1);
    return g_1038b078(v2);
}
```

## `sub_1032d470` `0x1032d470`

_108 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103903a0;

int sub_1032d470(int a0, int a1)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4135
    unsigned int v9;  // eax
    unsigned long v10;  // 4151
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
    sub_10353203(g_1038e180 ^ &v3, a0, v9, sub_1036d353, -1, &v4);
    v2 = 0;
    *((char **)a0) = &g_103903a0;
    sub_103145d0(a0 + 12, a1);
    v11 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v11) = v9;
    return a0;
}
```

## `sub_1032d4e0` `0x1032d4e0`

_99 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103903a0;

void sub_1032d4e0(int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4142
    unsigned int v10;  // eax
    unsigned long v11;  // 4158
    unsigned long v12;  // 4113
    int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x8], Other Possible Types: unsigned int
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v2 = 4294967295;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v10 = *((int *)v9);
    v1 = *((int *)v9);
    v0 = a0;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v1;
    *((char **)a0) = &g_103903a0;
    v2 = 1;
    v2 = 0;
    sub_10314610(a0 + 12);
    sub_103532d2(g_1038e180 ^ &v3, a0, v10, sub_1036d383, -1, &v4);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v10;
    return;
}
```

