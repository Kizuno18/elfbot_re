# elfbot.dll decompiled — jiru 0x10329290..0x1032b520

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10329290` `0x10329290`

_146 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b11c;
extern unsigned int g_1038e180;

int sub_10329290(int a0)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4140
    unsigned long v9;  // 4154
    unsigned int v10;  // eax
    unsigned long v12;  // 4117
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    char v3;  // [bp-0x8], Other Possible Types: unsigned int
    char v4;  // [bp-0x4]

    v3 = 4294967295;
    v2 = sub_1036c68b;
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v1 = *((int *)v8);
    v9 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v9) = &v1;
    sub_10333ef0(260, 0, g_1038e180 ^ &v4, 0);
    v3 = 1;
    v10 = sub_1032e2e0(0, 260);
    g_1038b11c(v10);
    sub_10314590(a0, sub_1032e2e0(0));
    v0 = 1;
    v3 = 0;
    sub_1032e280(0);
    v12 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v12) = v1;
    return a0;
}
```

## `sub_10329330` `0x10329330`

_413 bytes. refs "GetWindowsDirectoryW"_

```c
extern unsigned int g_1038e180;
extern unsigned int g_103a299c;
extern int g_103a2aac;

unsigned int sub_10329330(unsigned int a0)
{
    unsigned long v14;  // ldt
    unsigned long v15;  // gdt
    unsigned short v16;  // fs
    unsigned long v17;  // 4168
    unsigned long v18;  // 4172
    unsigned int v21;  // eax
    unsigned long v22;  // 4113
    char *v0;  // [bp-0xdc]
    unsigned int v1;  // [bp-0xd0]
    int v2;  // [bp-0xcc]
    int v3;  // [bp-0xc8]
    int v4;  // [bp-0xc4]
    int v5;  // [bp-0xc0]
    unsigned int v6;  // [bp-0xbc]
    char v7;  // [bp-0xb8]
    char v8;  // [bp-0x9c]
    char v9;  // [bp-0x3c]
    unsigned int v10;  // [bp-0x10]
    unsigned int v11;  // [bp-0xc]
    unsigned int v12;  // [bp-0x8], Other Possible Types: char
    char v13;  // [bp-0x4]

    v12 = 4294967295;
    v11 = sub_1036c6f9;
    v17 = _ccall(v14, v15, (unsigned int)v16, 0);
    v10 = *((int *)v17);
    v1 = g_1038e180 ^ &v13;
    v18 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int **)v18) = &v10;
    v6 = 0;
    if (!((char)g_103a299c & 1))
    {
        g_103a299c = g_103a299c | 1;
        v12 = 1;
        sub_10314590(&v9, "GetWindowsDirectoryW");
        v12 = 2;
        v0 = &v9;
        sub_1032e600(&v9, &g_103a2aac, 1);
        v12 = 1;
        sub_10314610(&v9);
        v12 = 0;
    }
    if ((char)sub_1032e630(v0))
    {
        sub_10333f40(260, 0);
        v12 = 3;
        sub_1032e650(sub_1032e410(0, 260));
        sub_1031fc10(a0, sub_1032e410(0));
        v6 |= 1;
        v12 = 0;
        sub_1032e3f0(0);
        v21 = a0;
    }
    else
    {
        v5 = sub_10329290(&v7);
        v4 = v5;
        v12 = 4;
        v3 = sub_10319e80(&v8, v4);
        v2 = v3;
        v12 = 5;
        sub_10326c30(v2, a0);
        v6 |= 1;
        v12 = 4;
        sub_10319f00(&v8);
        v12 = 0;
        sub_10314610(&v7);
        v21 = a0;
    }
    v22 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int *)v22) = v10;
    return v21;
}
```

## `sub_1032942f` `0x1032942f`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1032942f(void)
{
}
```

## `sub_103294e0` `0x103294e0`

_257 bytes. refs "CreateFileW"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b120;
extern unsigned int g_1038e180;
extern unsigned int g_103a29a4;
extern int g_103a2aac;

unsigned int sub_103294e0(int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6)
{
    unsigned long v13;  // ldt
    unsigned long v14;  // gdt
    unsigned short v15;  // fs
    unsigned long v16;  // 4165
    unsigned long v17;  // 4169
    unsigned int v18;  // eax
    int v19;  // eax
    unsigned long v20;  // 4113
    unsigned int v0;  // [bp-0x54]
    unsigned int v1;  // [bp-0x50]
    unsigned int v2;  // [bp-0x4c]
    unsigned int v3;  // [bp-0x48]
    unsigned int v4;  // [bp-0x44]
    unsigned int v5;  // [bp-0x40]
    char *v6;  // [bp-0x3c]
    unsigned int v7;  // [bp-0x30]
    char v8;  // [bp-0x2c]
    unsigned int v9;  // [bp-0x10]
    unsigned int v10;  // [bp-0xc]
    char v11;  // [bp-0x8], Other Possible Types: unsigned int
    char v12;  // [bp-0x4]

    v11 = 4294967295;
    v10 = sub_1036c72d;
    v16 = _ccall(v13, v14, (unsigned int)v15, 0);
    v9 = *((int *)v16);
    v7 = g_1038e180 ^ &v12;
    v17 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int **)v17) = &v9;
    if (!((char)g_103a29a4 & 1))
    {
        g_103a29a4 = g_103a29a4 | 1;
        v11 = 0;
        sub_10314590(&v8, "CreateFileW");
        v11 = 1;
        v6 = &v8;
        sub_1032e670(&v8, &g_103a2aac, 1);
        v11 = 0;
        sub_10314610(&v8);
        v11 = 4294967295;
    }
    if ((char)sub_1032e630(v6) && (char)sub_10327630(a0))
    {
        v5 = a6;
        v4 = a5;
        v3 = a4;
        v2 = a3;
        v1 = a2;
        v0 = a1;
        v18 = sub_1032e6a0(sub_10326fd0(a0));
    }
    else
    {
        v5 = a6;
        v4 = a5;
        v3 = a4;
        v2 = a3;
        v1 = a2;
        v0 = a1;
        v19 = sub_10326e70(a0);
        v18 = g_1038b120(v19);
    }
    v20 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int *)v20) = v9;
    return v18;
}
```

## `sub_103295ab` `0x103295ab`

_2 bytes. (leaf/helper — see body)_

```c
void sub_103295ab(void)
{
}
```

## `sub_103295f0` `0x103295f0`

_386 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b124;
extern unsigned int g_1038e180;
extern int g_10390414;

int sub_103295f0(unsigned int a0, int a1, int a2, int a3)
{
    unsigned long v17;  // ldt
    unsigned long v18;  // gdt
    unsigned short v19;  // fs
    unsigned long v20;  // 4145
    unsigned long v21;  // 4162
    int v22;  // eax
    unsigned long v24;  // 4114
    int v0;  // [bp-0xe0]
    int v1;  // [bp-0xdc]
    unsigned int v2;  // [bp-0xd8]
    int v3;  // [bp-0xb8]
    int v4;  // [bp-0xb4]
    unsigned int v5;  // [bp-0xb0]
    char v6;  // [bp-0xac]
    char v7;  // [bp-0x49]
    char v8;  // [bp-0x38]
    int v9;  // [bp-0x1c]
    unsigned int v10;  // [bp-0x18]
    int v11;  // [bp-0x14]
    unsigned int v12;  // [bp-0x10]
    unsigned int v13;  // [bp-0xc]
    unsigned int v14;  // [bp-0x8], Other Possible Types: char
    char v15;  // [bp-0x4]
    int v16;  // [bp+0x14]

    v14 = 4294967295;
    v13 = sub_1036c782;
    v20 = _ccall(v17, v18, (unsigned int)v19, 0);
    v12 = *((int *)v20);
    v9 = g_1038e180 ^ &v15;
    v21 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((unsigned int **)v21) = &v12;
    v5 = 0;
    v10 = 0x8000;
    v11 = &g_10390414;
    v7 = 0;
    sub_1032e240(0x8000, &v7, v9);
    v14 = 1;
    v4 = sub_1032d6d0(a1);
    v3 = v4;
    v14 = 2;
    v2 = sub_1032e2e0(0, 0x8000, sub_10326e70(v3));
    v1 = v11;
    v0 = sub_10326e70(a3);
    v22 = sub_10326e70(a2);
    g_1038b124(v22);
    v14 = 1;
    sub_10319f00(&v6);
    sub_10314590(&v8, sub_1032e2e0(0));
    v14 = 3;
    if ((char)sub_10333ff0(&v8, v11))
    {
        sub_10327170(v16, a0);
        v5 |= 1;
        v14 = 1;
        sub_10314610(&v8);
        v14 = 0;
        sub_1032e280();
    }
    else
    {
        sub_1032e020(&v8);
        v5 |= 1;
        v14 = 1;
        sub_10314610(&v8);
        v14 = 0;
        sub_1032e280();
    }
    v24 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((unsigned int *)v24) = v12;
    return sub_10351225();
}
```

## `sub_10329721` `0x10329721`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10329721(void)
{
    sub_1032975b();
    return;
}
```

## `sub_1032975b` `0x1032975b`

_24 bytes. (leaf/helper — see body)_

```c
void sub_1032975b(void)
{
    char v1;  // [bp+0x100000]

    v1 = 1;
    sub_10314610(/* unsupported instruction */ - 52);
    v1 = 0;
    sub_1032e280();
}
```

## `sub_10329790` `0x10329790`

_658 bytes. refs "GetPrivateProfileStringW"_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

extern unsigned int g_1038e180;
extern int g_10390438;
extern unsigned int g_103a29ac;
extern int g_103a2aac;

int sub_10329790(int a0, int a1, int a2, int a3, int a4)
{
    unsigned long v26;  // ldt
    unsigned long v27;  // gdt
    unsigned short v28;  // fs
    unsigned long v29;  // 4178
    unsigned long v30;  // 4182
    unsigned long v33;  // 4114
    struct_0 *v0;  // [bp-0x154]
    int v1;  // [bp-0x150]
    unsigned int v2;  // [bp-0x14c]
    int v3;  // [bp-0x138]
    char *v4;  // [bp-0x130]
    unsigned int v5;  // [bp-0x124]
    int v6;  // [bp-0x120]
    int v7;  // [bp-0x11c]
    unsigned int v8;  // [bp-0x118]
    unsigned int v9;  // [bp-0x114]
    struct_0 *v10;  // [bp-0x110]
    struct_0 *v11;  // [bp-0x10c]
    unsigned int v12;  // [bp-0x108]
    char v13;  // [bp-0x104]
    char v14;  // [bp-0xe4]
    char v15;  // [bp-0x84]
    unsigned short v16;  // [bp-0x66]
    char v17;  // [bp-0x64]
    char v18;  // [bp-0x38]
    unsigned int v19;  // [bp-0x1c]
    unsigned int v20;  // [bp-0x18]
    int v21;  // [bp-0x14]
    unsigned int v22;  // [bp-0x10]
    unsigned int v23;  // [bp-0xc]
    unsigned int v24;  // [bp-0x8], Other Possible Types: char
    char v25;  // [bp-0x4]

    v24 = 4294967295;
    v23 = sub_1036c80d;
    v29 = _ccall(v26, v27, (unsigned int)v28, 0);
    v22 = *((int *)v29);
    v19 = g_1038e180 ^ &v25;
    v5 = v19;
    v30 = _ccall(v26, v27, (unsigned int)v28, 0);
    *((unsigned int **)v30) = &v22;
    v12 = 0;
    v20 = 0x8000;
    v21 = &g_10390438;
    if (!((char)g_103a29ac & 1))
    {
        g_103a29ac = g_103a29ac | 1;
        v24 = 1;
        sub_10314590(&v17, "GetPrivateProfileStringW");
        v24 = 2;
        v4 = &v17;
        sub_1032e6d0(&v17, &g_103a2aac, 1);
        v24 = 1;
        sub_10314610(&v17);
        v24 = 0;
    }
    if ((char)sub_1032e630(v4))
    {
        v16 = 0;
        sub_1032e3b0(0x8000, &v16);
        v24 = 3;
        v11 = sub_10332ed0(&v15);
        v10 = v11;
        v24 = 4;
        v2 = sub_1032e410(0, 0x8000, sub_1031fc50(v10));
        v1 = v21;
        v0 = sub_10326fd0(a3);
        sub_1032e700(sub_10326fd0(a2));
        v24 = 3;
        sub_1031a3a0(&v15);
        sub_1031fc10(&v18, sub_1032e410(0));
        v24 = 5;
        if ((char)sub_10334110(&v18, v21))
        {
            sub_10327230(a4, a0);
            v12 |= 1;
            v24 = 3;
            sub_1031a3a0(&v18);
            v24 = 0;
            sub_1032e3f0();
        }
        else
        {
            sub_10325880(a0, &v18);
            v12 |= 1;
            v24 = 3;
            sub_1031a3a0(&v18);
            v24 = 0;
            sub_1032e3f0();
        }
    }
    else
    {
        v3 = a4;
        v9 = sub_103295f0(&v13, a1, a2, a3);
        v8 = v9;
        v24 = 6;
        v7 = sub_10326840(&v14, v8);
        v6 = v7;
        v24 = 7;
        sub_10327230(v6, a0);
        v12 |= 1;
        v24 = 6;
        sub_10319f00(&v14);
        v24 = 0;
        sub_1031a040(&v13);
    }
    v33 = _ccall(v26, v27, (unsigned int)v28, 0);
    *((unsigned int *)v33) = v22;
    return sub_10351225();
}
```

## `sub_1032992f` `0x1032992f`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032992f(void)
{
    sub_1032996c();
    return;
}
```

## `sub_1032996c` `0x1032996c`

_29 bytes. (leaf/helper — see body)_

```c
void sub_1032996c(void)
{
    char v1;  // [bp+0x100000]

    v1 = 3;
    sub_1031a3a0(/* unsupported instruction */ - 52);
    v1 = 0;
    sub_1032e3f0();
}
```

## `sub_10329a50` `0x10329a50`

_391 bytes. refs "WritePrivateProfileStringW"_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

extern struct_0 *g_1038b1d8;
extern unsigned int g_1038e180;
extern unsigned int g_103a29b4;
extern int g_103a2aac;

unsigned int sub_10329a50(int a0, int a1, int a2, int a3)
{
    unsigned long v18;  // ldt
    unsigned long v19;  // gdt
    unsigned short v20;  // fs
    unsigned long v21;  // 4165
    unsigned long v22;  // 4169
    unsigned int v23;  // eax
    int v24;  // eax
    unsigned long v25;  // 4113
    struct_0 *v0;  // [bp-0x124], Other Possible Types: int
    struct_0 *v1;  // [bp-0x120], Other Possible Types: int
    struct_0 *v2;  // [bp-0x11c], Other Possible Types: int
    char *v3;  // [bp-0x114]
    unsigned int v4;  // [bp-0x108]
    int v5;  // [bp-0x104]
    int v6;  // [bp-0x100]
    int v7;  // [bp-0xfc]
    int v8;  // [bp-0xf8]
    char v9;  // [bp-0xf4]
    unsigned int v10;  // [bp-0x94]
    char v11;  // [bp-0x90]
    unsigned int v12;  // [bp-0x30]
    char v13;  // [bp-0x2c]
    unsigned int v14;  // [bp-0x10]
    unsigned int v15;  // [bp-0xc]
    char v16;  // [bp-0x8], Other Possible Types: unsigned int
    char v17;  // [bp-0x4]

    v16 = 4294967295;
    v15 = sub_1036c861;
    v21 = _ccall(v18, v19, (unsigned int)v20, 0);
    v14 = *((int *)v21);
    v4 = g_1038e180 ^ &v17;
    v22 = _ccall(v18, v19, (unsigned int)v20, 0);
    *((unsigned int **)v22) = &v14;
    if (!((char)g_103a29b4 & 1))
    {
        g_103a29b4 = g_103a29b4 | 1;
        v16 = 0;
        sub_10314590(&v13, "WritePrivateProfileStringW");
        v16 = 1;
        v3 = &v13;
        sub_1032e730(&v13, &g_103a2aac, 1);
        v16 = 0;
        sub_10314610(&v13);
        v16 = 4294967295;
    }
    if ((char)sub_1032e630(v3))
    {
        v8 = sub_1032d6d0(a0);
        v7 = v8;
        v16 = 2;
        v2 = sub_10326fd0(v7);
        v1 = sub_10326fd0(a3);
        v0 = sub_10326fd0(a2);
        v12 = sub_1032e760(sub_10326fd0(a1));
        v16 = 4294967295;
        sub_10319f00(&v11);
        v23 = v12;
    }
    else
    {
        v6 = sub_1032d6d0(a0);
        v5 = v6;
        v16 = 3;
        v2 = sub_10326e70(v5);
        v1 = sub_10326e70(a3);
        v0 = sub_10326e70(a2);
        v24 = sub_10326e70(a1);
        v10 = g_1038b1d8(v24);
        v16 = 4294967295;
        sub_10319f00(&v9);
        v23 = v10;
    }
    v25 = _ccall(v18, v19, (unsigned int)v20, 0);
    *((unsigned int *)v25) = v14;
    return v23;
}
```

## `sub_10329b55` `0x10329b55`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10329b55(void)
{
}
```

## `sub_10329be0` `0x10329be0`

_194 bytes. refs "DeleteFileW"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b12c;
extern unsigned int g_1038e180;
extern unsigned int g_103a29bc;
extern int g_103a2aac;

unsigned int sub_10329be0(int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4165
    unsigned long v11;  // 4169
    unsigned int v12;  // eax
    int v13;  // eax
    unsigned long v14;  // 4113
    char *v0;  // [bp-0x3c]
    unsigned int v1;  // [bp-0x30]
    char v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char v5;  // [bp-0x8], Other Possible Types: unsigned int
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036c895;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v1 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    if (!((char)g_103a29bc & 1))
    {
        g_103a29bc = g_103a29bc | 1;
        v5 = 0;
        sub_10314590(&v2, "DeleteFileW");
        v5 = 1;
        v0 = &v2;
        sub_1032e790(&v2, &g_103a2aac, 1);
        v5 = 0;
        sub_10314610(&v2);
        v5 = 4294967295;
    }
    if ((char)sub_1032e630(v0))
    {
        v12 = sub_10335b10(sub_10326fd0(a0));
    }
    else
    {
        v13 = sub_10326e70(a0);
        v12 = g_1038b12c(v13);
    }
    v14 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v14) = v3;
    return v12;
}
```

## `sub_10329cb0` `0x10329cb0`

_212 bytes. refs "MoveFileW"_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

extern struct_0 *g_1038b130;
extern unsigned int g_1038e180;
extern unsigned int g_103a29c4;
extern int g_103a2aac;

unsigned int sub_10329cb0(int a0, int a1)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4165
    unsigned long v12;  // 4169
    unsigned int v13;  // eax
    int v14;  // eax
    unsigned long v15;  // 4113
    struct_0 *v0;  // [bp-0x40], Other Possible Types: int
    char *v1;  // [bp-0x3c]
    unsigned int v2;  // [bp-0x30]
    char v3;  // [bp-0x2c]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    char v6;  // [bp-0x8], Other Possible Types: unsigned int
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036c8c6;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v2 = g_1038e180 ^ &v7;
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    if (!((char)g_103a29c4 & 1))
    {
        g_103a29c4 = g_103a29c4 | 1;
        v6 = 0;
        sub_10314590(&v3, "MoveFileW");
        v6 = 1;
        v1 = &v3;
        sub_1032e7c0(&v3, &g_103a2aac, 1);
        v6 = 0;
        sub_10314610(&v3);
        v6 = 4294967295;
    }
    if ((char)sub_1032e630(v1))
    {
        v0 = sub_10326fd0(a1);
        v13 = sub_1032e650(sub_10326fd0(a0));
    }
    else
    {
        v0 = sub_10326e70(a1);
        v14 = sub_10326e70(a0);
        v13 = g_1038b130(v14);
    }
    v15 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v15) = v4;
    return v13;
}
```

## `sub_10329d90` `0x10329d90`

_85 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

extern char g_103a2a8c;

int sub_10329d90(int a0, int a1)
{
    struct_0 *v0;  // [bp-0x8], Other Possible Types: int

    if (g_103a2a8c && (char)sub_10327630(a0))
    {
        v0 = sub_10326fd0(a1);
        return sub_10354483(sub_10326fd0(a0));
    }
    v0 = sub_10326e70(a1);
    return sub_103543aa(sub_10326e70(a0));
}
```

## `sub_10329df0` `0x10329df0`

_226 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b068;
extern unsigned int g_1038e180;

int sub_10329df0(int a0, int a1, int a2)
{
    unsigned long v11;  // ldt
    unsigned long v12;  // gdt
    unsigned short v13;  // fs
    unsigned long v14;  // 4140
    unsigned long v15;  // 4154
    int v16;  // eax
    int v17;  // eax
    int v19;  // eax
    unsigned long v20;  // 4113
    unsigned int v0;  // [bp-0x50]
    unsigned int v1;  // [bp-0x38]
    unsigned int v2;  // [bp-0x34]
    unsigned int v3;  // [bp-0x30]
    unsigned int v4;  // [bp-0x2c]
    char v5;  // [bp-0x25]
    int v6;  // [bp-0x14]
    unsigned int v7;  // [bp-0x10]
    unsigned int v8;  // [bp-0xc]
    char v9;  // [bp-0x8], Other Possible Types: unsigned int
    char v10;  // [bp-0x4]

    v9 = 4294967295;
    v8 = sub_1036c902;
    v14 = _ccall(v11, v12, (unsigned int)v13, 0);
    v7 = *((int *)v14);
    v3 = g_1038e180 ^ &v10;
    v15 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int **)v15) = &v7;
    v4 = 0;
    v2 = 0;
    v1 = 0;
    v16 = sub_10326e70(a1);
    v6 = g_1038b068(v16);
    if (v6 > 0)
    {
        v5 = 0;
        sub_1032e240(v6 + 2, &v5);
        v9 = 1;
        v0 = sub_1032e2e0(0, v6 + 1);
        v17 = sub_10326e70(a1);
        g_1038b068(v17);
        sub_10314590(a0, sub_1032e2e0(0));
        v4 |= 1;
        v9 = 0;
        sub_1032e280(0);
        v19 = a0;
    }
    else
    {
        sub_103145d0(a0, a2);
        v9 = 0;
        v4 |= 1;
        v19 = a0;
    }
    v20 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int *)v20) = v7;
    return v19;
}
```

## `sub_10329ea4` `0x10329ea4`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10329ea4(void)
{
}
```

## `sub_10329ee0` `0x10329ee0`

_619 bytes. refs "GetEnvironmentVariableW"_

```c
extern unsigned int g_1038e180;
extern int g_10390478;
extern unsigned int g_103a29cc;
extern int g_103a2aac;

int sub_10329ee0(unsigned int a0, int a1, int a2)
{
    unsigned long v19;  // ldt
    unsigned long v20;  // gdt
    unsigned short v21;  // fs
    unsigned long v22;  // 4172
    unsigned long v23;  // 4176
    unsigned long v26;  // 4114
    unsigned int v0;  // [bp-0x11c]
    unsigned int v1;  // [bp-0x104]
    unsigned int v2;  // [bp-0x100]
    char *v3;  // [bp-0xfc]
    unsigned int v4;  // [bp-0xf0]
    int v5;  // [bp-0xec]
    int v6;  // [bp-0xe8]
    unsigned int v7;  // [bp-0xe4]
    char v8;  // [bp-0xe0]
    unsigned short v9;  // [bp-0x7e]
    char v10;  // [bp-0x7c]
    char v11;  // [bp-0x60]
    char v12;  // [bp-0x44]
    unsigned int v13;  // [bp-0x28]
    int v14;  // [bp-0x14]
    unsigned int v15;  // [bp-0x10]
    unsigned int v16;  // [bp-0xc]
    unsigned int v17;  // [bp-0x8], Other Possible Types: char
    char v18;  // [bp-0x4]

    v17 = 4294967295;
    v16 = sub_1036c975;
    v22 = _ccall(v19, v20, (unsigned int)v21, 0);
    v15 = *((int *)v22);
    v13 = g_1038e180 ^ &v18;
    v4 = v13;
    v23 = _ccall(v19, v20, (unsigned int)v21, 0);
    *((unsigned int **)v23) = &v15;
    v7 = 0;
    if (!((char)g_103a29cc & 1))
    {
        g_103a29cc = g_103a29cc | 1;
        v17 = 1;
        sub_10314590(&v10, "GetEnvironmentVariableW");
        v17 = 2;
        v3 = &v10;
        sub_1032e540(&v10, &g_103a2aac, 1);
        v17 = 1;
        sub_10314610(&v10);
        v17 = 0;
    }
    if ((char)sub_1032e630(v3))
    {
        v2 = 0;
        v1 = 0;
        v14 = sub_1032eae0(sub_10326fd0(a1));
        if (v14 > 0)
        {
            v9 = 0;
            sub_1032e3b0(v14 + 4, &v9);
            v17 = 3;
            v0 = sub_1032e410(0, v14 + 2);
            sub_1032eae0(sub_10326fd0(a1));
            sub_1031fc10(a0, sub_1032e410(0));
            v7 |= 1;
            v17 = 0;
            sub_1032e3f0(0);
        }
        else
        {
            sub_1031e760(a0, a2);
            v17 = 0;
            v7 |= 1;
        }
    }
    else
    {
        sub_10314590(&v12, &g_10390478);
        v17 = 4;
        sub_10329df0(&v11, a1, &v12);
        v17 = 5;
        if ((char)sub_10334130(&v11, &v12))
        {
            sub_1031e760(a0, a2);
            v7 |= 1;
            v17 = 4;
            sub_10314610(&v11);
            v17 = 0;
            sub_10314610(&v12);
        }
        else
        {
            v6 = sub_10319e80(&v8, &v11);
            v5 = v6;
            v17 = 6;
            sub_10326c30(v5, a0);
            v7 |= 1;
            v17 = 5;
            sub_10319f00(&v8);
            v17 = 4;
            sub_10314610(&v11);
            v17 = 0;
            sub_10314610(&v12);
        }
    }
    v26 = _ccall(v19, v20, (unsigned int)v21, 0);
    *((unsigned int *)v26) = v15;
    return sub_10351225();
}
```

## `sub_1032a01b` `0x1032a01b`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032a01b(void)
{
    sub_1032a047();
    return;
}
```

## `sub_1032a047` `0x1032a047`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1032a047(void)
{
}
```

## `sub_1032a0ca` `0x1032a0ca`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032a0ca(void)
{
    sub_1032a13b();
    return;
}
```

## `sub_1032a13b` `0x1032a13b`

_24 bytes. (leaf/helper — see body)_

```c
void sub_1032a13b(void)
{
    char v1;  // [bp+0x100000]

    v1 = 4;
    sub_10314610(/* unsupported instruction */ - 92);
    v1 = 0;
    sub_10314610(/* unsupported instruction */ - 64);
}
```

## `sub_1032a170` `0x1032a170`

_144 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b064;
extern unsigned int g_1038e180;

char sub_1032a170(int a0)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4136
    unsigned long v12;  // 4150
    int v13;  // eax
    unsigned long v14;  // 4117
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x1c]
    char v2;  // [bp-0x15]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]
    char v7;  // [bp+0x8]

    v5 = 4294967295;
    v4 = sub_1036c9a5;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v3 = *((int *)v11);
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v3;
    v5 = 0;
    v1 = (!sub_1032e0a0(g_1038e180 ^ &v6) ? 0 : (unsigned int)sub_102ec9a0(sub_103301b0()));
    v0 = v1;
    v13 = sub_10326e70(a0);
    v2 = -(-(0 < g_1038b064(v13)));
    v5 = 4294967295;
    sub_1031a040(&v7);
    v14 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v14) = v3;
    return v2;
}
```

## `sub_1032a200` `0x1032a200`

_35 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b064;

int sub_1032a200(int a0, int a1)
{
    int v1;  // eax
    int v0;  // [bp-0x8]

    v0 = sub_10326e70(a1);
    v1 = sub_10326e70(a0);
    return -(-(0 < g_1038b064(v1)));
}
```

## `sub_1032a230` `0x1032a230`

_97 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b340;

int sub_1032a230(int a0, int a1, int a2, int a3)
{
    int v1;  // eax
    char v0;  // [bp+0x0]

    if ((char)sub_1032e630(&v0) && (char)sub_10327630(a3))
        return sub_1032e760(a0, a1, a2, sub_10326fd0(a3));
    v1 = sub_10326e70(a3);
    return g_1038b340(a0, a1, a2, v1);
}
```

## `sub_1032a274` `0x1032a274`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032a274(void)
{
}
```

## `sub_1032a2a0` `0x1032a2a0`

_28 bytes. (leaf/helper — see body)_

```c
int sub_1032a2a0(int a0, int a1)
{
    return sub_1032a230(a0, 323, 0, a1);
}
```

## `sub_1032a2c0` `0x1032a2c0`

_208 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b2b0;
extern struct_0 *g_1038b2b4;
extern unsigned int g_1038e180;

int sub_1032a2c0(unsigned int a0, unsigned int a1)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4140
    unsigned long v11;  // 4154
    unsigned int v12;  // eax
    unsigned int v14;  // eax
    unsigned long v15;  // 4113
    unsigned int v0;  // [bp-0x2c]
    char v1;  // [bp-0x25]
    int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char v5;  // [bp-0x8], Other Possible Types: unsigned int
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036c9e1;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    v2 = g_1038b2b0(a1, g_1038e180 ^ &v6, 0);
    if (v2 > 0)
    {
        v1 = 0;
        sub_1032e240(v2 + 1, &v1);
        v5 = 1;
        v12 = sub_1032e2e0(0, v2 + 1);
        g_1038b2b4(a1, v12);
        sub_10314590(a0, sub_1032e2e0(0));
        v0 = 1;
        v5 = 0;
        sub_1032e280(0);
        v14 = a0;
    }
    else
    {
        sub_10315800(a0);
        v5 = 0;
        v0 = 1;
        v14 = a0;
    }
    v15 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v15) = v3;
    return v14;
}
```

## `sub_1032a366` `0x1032a366`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032a366(void)
{
}
```

## `sub_1032a3a0` `0x1032a3a0`

_605 bytes. refs "GetWindowTextLengthW", "GetWindowTextW"_

```c
extern unsigned int g_1038e180;
extern unsigned int g_103a29d8;
extern int g_103a2a70;

unsigned int sub_1032a3a0(unsigned int a0, unsigned int a1)
{
    unsigned long v16;  // ldt
    unsigned long v17;  // gdt
    unsigned short v18;  // fs
    unsigned long v19;  // 4168
    unsigned long v20;  // 4172
    unsigned int v23;  // eax
    unsigned long v24;  // 4113
    unsigned int v0;  // [bp-0xf4]
    int v1;  // [bp-0xf0]
    int v2;  // [bp-0xec]
    int v3;  // [bp-0xe8]
    int v4;  // [bp-0xe4]
    unsigned int v5;  // [bp-0xe0]
    char v6;  // [bp-0xdc]
    char v7;  // [bp-0xc0]
    unsigned short v8;  // [bp-0x5e]
    char v9;  // [bp-0x5c]
    char v10;  // [bp-0x40]
    int v11;  // [bp-0x14]
    unsigned int v12;  // [bp-0x10]
    unsigned int v13;  // [bp-0xc]
    unsigned int v14;  // [bp-0x8], Other Possible Types: char
    char v15;  // [bp-0x4]

    v14 = 4294967295;
    v13 = sub_1036ca65;
    v19 = _ccall(v16, v17, (unsigned int)v18, 0);
    v12 = *((int *)v19);
    v0 = g_1038e180 ^ &v15;
    v20 = _ccall(v16, v17, (unsigned int)v18, 0);
    *((unsigned int **)v20) = &v12;
    v5 = 0;
    if (!((char)g_103a29d8 & 1))
    {
        g_103a29d8 = g_103a29d8 | 1;
        v14 = 1;
        sub_10314590(&v10, "GetWindowTextLengthW");
        v14 = 2;
        sub_1032e7f0(&v10, &g_103a2a70, 1);
        v14 = 1;
        sub_10314610(&v10);
        v14 = 0;
    }
    if (!((char)g_103a29d8 & 2))
    {
        g_103a29d8 = g_103a29d8 | 2;
        v14 = 3;
        sub_10314590(&v9, "GetWindowTextW");
        v14 = 4;
        sub_1032e820(&v9, &g_103a2a70, 1);
        v14 = 3;
        sub_10314610(&v9);
        v14 = 0;
    }
    if ((char)sub_1032e630() && (char)sub_1032e630())
    {
        v11 = sub_10335b10(a1);
        if (v11 > 0)
        {
            v8 = 0;
            sub_1032e3b0(v11 + 1, &v8);
            v14 = 5;
            sub_1032eae0(a1, sub_1032e410(0, v11 + 1));
            sub_1031fc10(a0, sub_1032e410(0));
            v5 |= 1;
            v14 = 0;
            sub_1032e3f0(0);
            v23 = a0;
        }
        else
        {
            sub_103257a0(a0);
            v14 = 0;
            v5 |= 1;
            v23 = a0;
        }
    }
    else
    {
        v4 = sub_1032a2c0(&v6, a1);
        v3 = v4;
        v14 = 6;
        v2 = sub_10319e80(&v7, v3);
        v1 = v2;
        v14 = 7;
        sub_10326c30(v1, a0);
        v5 |= 1;
        v14 = 6;
        sub_10319f00(&v7);
        v14 = 0;
        sub_10314610(&v6);
        v23 = a0;
    }
    v24 = _ccall(v16, v17, (unsigned int)v18, 0);
    *((unsigned int *)v24) = v12;
    return v23;
}
```

## `sub_1032a535` `0x1032a535`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032a535(void)
{
    sub_1032a55d();
    return;
}
```

## `sub_1032a55d` `0x1032a55d`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1032a55d(void)
{
}
```

## `sub_1032a610` `0x1032a610`

_258 bytes. refs "MessageBoxW"_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

extern struct_0 *g_1038b30c;
extern unsigned int g_1038e180;
extern unsigned int g_103a29e0;
extern int g_103a2a70;

unsigned int sub_1032a610(int a0, int a1, int a2, unsigned int a3)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4165
    unsigned long v13;  // 4169
    unsigned int v14;  // eax
    int v15;  // eax
    unsigned long v16;  // 4113
    struct_0 *v0;  // [bp-0x44], Other Possible Types: int
    unsigned int v1;  // [bp-0x40]
    char *v2;  // [bp-0x3c]
    unsigned int v3;  // [bp-0x30]
    char v4;  // [bp-0x2c]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    char v7;  // [bp-0x8], Other Possible Types: unsigned int
    char v8;  // [bp-0x4]

    v7 = 4294967295;
    v6 = sub_1036ca99;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v5 = *((int *)v12);
    v3 = g_1038e180 ^ &v8;
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v5;
    if (!((char)g_103a29e0 & 1))
    {
        g_103a29e0 = g_103a29e0 | 1;
        v7 = 0;
        sub_10314590(&v4, "MessageBoxW");
        v7 = 1;
        v2 = &v4;
        sub_1032e850(&v4, &g_103a2a70, 1);
        v7 = 0;
        sub_10314610(&v4);
        v7 = 4294967295;
    }
    if ((char)sub_1032e630(v2) && ((char)sub_10327630(a1) || (char)sub_10327630(a2)))
    {
        v1 = a3;
        v0 = sub_10326fd0(a2);
        v14 = sub_1032e760(a0, sub_10326fd0(a1));
    }
    else
    {
        v1 = a3;
        v0 = sub_10326e70(a2);
        v15 = sub_10326e70(a1);
        v14 = g_1038b30c(a0, v15);
    }
    v16 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v16) = v5;
    return v14;
}
```

## `sub_1032a6e3` `0x1032a6e3`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032a6e3(void)
{
}
```

## `sub_1032a720` `0x1032a720`

_217 bytes. refs "SetWindowTextW"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b2e4;
extern unsigned int g_1038e180;
extern unsigned int g_103a29e8;
extern int g_103a2a70;

unsigned int sub_1032a720(int a0, int a1)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4165
    unsigned long v11;  // 4169
    unsigned int v12;  // eax
    int v13;  // eax
    unsigned long v14;  // 4113
    char *v0;  // [bp-0x3c]
    unsigned int v1;  // [bp-0x30]
    char v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char v5;  // [bp-0x8], Other Possible Types: unsigned int
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036caca;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v1 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    if (!((char)g_103a29e8 & 1))
    {
        g_103a29e8 = g_103a29e8 | 1;
        v5 = 0;
        sub_10314590(&v2, "SetWindowTextW");
        v5 = 1;
        v0 = &v2;
        sub_1032e880(&v2, &g_103a2a70, 1);
        v5 = 0;
        sub_10314610(&v2);
        v5 = 4294967295;
    }
    if ((char)sub_1032e630(v0) && (char)sub_10327630(a1))
    {
        v12 = sub_1032e650(a0, sub_10326fd0(a1));
    }
    else
    {
        v13 = sub_10326e70(a1);
        v12 = g_1038b2e4(a0, v13);
    }
    v14 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v14) = v3;
    return v12;
}
```

## `sub_1032a7d7` `0x1032a7d7`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032a7d7(void)
{
}
```

## `sub_1032a800` `0x1032a800`

_95 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b340;

int sub_1032a800(int a0, int a1)
{
    int v1;  // eax
    char v0;  // [bp+0x0]

    if ((char)sub_1032e630(&v0) && (char)sub_10327630(a1))
        return sub_1032e760(a0, 384, 0, sub_10326fd0(a1));
    v1 = sub_10326e70(a1);
    return g_1038b340(a0, 384, 0, v1);
}
```

## `sub_1032a843` `0x1032a843`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032a843(void)
{
}
```

## `sub_1032a870` `0x1032a870`

_221 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b340;
extern unsigned int g_1038e180;

int sub_1032a870(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4147
    unsigned long v11;  // 4161
    unsigned int v12;  // eax
    unsigned int v14;  // eax
    unsigned long v15;  // 4113
    unsigned int v0;  // [bp-0x2c]
    char v1;  // [bp-0x25]
    int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char v5;  // [bp-0x8], Other Possible Types: unsigned int
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036cb06;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    v2 = g_1038b340(a1, 394, a2, 0, g_1038e180 ^ &v6, 0);
    if (v2 != -1)
    {
        v1 = 0;
        sub_1032e240(v2 + 1, &v1);
        v5 = 1;
        v12 = sub_1032e2e0(0);
        g_1038b340(a1, 393, a2, v12);
        sub_10314590(a0, sub_1032e2e0(0));
        v0 = 1;
        v5 = 0;
        sub_1032e280(0);
        v14 = a0;
    }
    else
    {
        sub_10315800(a0);
        v5 = 0;
        v0 = 1;
        v14 = a0;
    }
    v15 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v15) = v3;
    return v14;
}
```

## `sub_1032a923` `0x1032a923`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032a923(void)
{
}
```

## `sub_1032a950` `0x1032a950`

_425 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b33c;
extern unsigned int g_1038e180;

unsigned int sub_1032a950(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned long v13;  // ldt
    unsigned long v14;  // gdt
    unsigned short v15;  // fs
    unsigned long v16;  // 4135
    unsigned long v17;  // 4149
    unsigned int v18;  // eax
    unsigned int v20;  // eax
    unsigned long v21;  // 4113
    int v0;  // [bp-0xb8]
    int v1;  // [bp-0xb4]
    int v2;  // [bp-0xb0]
    int v3;  // [bp-0xac]
    unsigned int v4;  // [bp-0xa8]
    char v5;  // [bp-0xa4]
    char v6;  // [bp-0x88]
    unsigned short v7;  // [bp-0x26]
    int v8;  // [bp-0x14]
    unsigned int v9;  // [bp-0x10]
    unsigned int v10;  // [bp-0xc]
    char v11;  // [bp-0x8], Other Possible Types: unsigned int
    char v12;  // [bp-0x4]

    v11 = 4294967295;
    v10 = sub_1036cb5e;
    v16 = _ccall(v13, v14, (unsigned int)v15, 0);
    v9 = *((int *)v16);
    v17 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int **)v17) = &v9;
    v4 = 0;
    if ((char)sub_1032e630(g_1038e180 ^ &v12))
    {
        v8 = sub_1032e760(a1, 394, a2, 0);
        if (v8 != -1)
        {
            v7 = 0;
            sub_1032e3b0(v8 + 1, &v7);
            v11 = 1;
            v18 = sub_1032e410(0);
            g_1038b33c(a1, 393, a2, v18);
            sub_1031fc10(a0, sub_1032e410(0));
            v4 |= 1;
            v11 = 0;
            sub_1032e3f0(0);
            v20 = a0;
        }
        else
        {
            sub_103257a0(a0);
            v11 = 0;
            v4 |= 1;
            v20 = a0;
        }
    }
    else
    {
        v3 = sub_1032a870(&v5, a1, a2);
        v2 = v3;
        v11 = 2;
        v1 = sub_10319e80(&v6, v2);
        v0 = v1;
        v11 = 3;
        sub_10326c30(v0, a0);
        v4 |= 1;
        v11 = 2;
        sub_10319f00(&v6);
        v11 = 0;
        sub_10314610(&v5);
        v20 = a0;
    }
    v21 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int *)v21) = v9;
    return v20;
}
```

## `sub_1032aa2d` `0x1032aa2d`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032aa2d(void)
{
    sub_1032aa55();
    return;
}
```

## `sub_1032aa55` `0x1032aa55`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1032aa55(void)
{
}
```

## `sub_1032ab00` `0x1032ab00`

_226 bytes. refs "DialogBoxParamW"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b2ac;
extern unsigned int g_1038e180;
extern unsigned int g_103a29f0;
extern int g_103a2a70;

unsigned int sub_1032ab00(int a0, int a1, unsigned int a2, unsigned int a3, unsigned int a4)
{
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // fs
    unsigned long v13;  // 4165
    unsigned long v14;  // 4169
    unsigned int v15;  // eax
    int v16;  // eax
    unsigned long v17;  // 4113
    unsigned int v0;  // [bp-0x48]
    unsigned int v1;  // [bp-0x44]
    unsigned int v2;  // [bp-0x40]
    char *v3;  // [bp-0x3c]
    unsigned int v4;  // [bp-0x30]
    char v5;  // [bp-0x2c]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    char v8;  // [bp-0x8], Other Possible Types: unsigned int
    char v9;  // [bp-0x4]

    v8 = 4294967295;
    v7 = sub_1036cb92;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v6 = *((int *)v13);
    v4 = g_1038e180 ^ &v9;
    v14 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v14) = &v6;
    if (!((char)g_103a29f0 & 1))
    {
        g_103a29f0 = g_103a29f0 | 1;
        v8 = 0;
        sub_10314590(&v5, "DialogBoxParamW");
        v8 = 1;
        v3 = &v5;
        sub_1032e8b0(&v5, &g_103a2a70, 1);
        v8 = 0;
        sub_10314610(&v5);
        v8 = 4294967295;
    }
    if ((char)sub_1032e630(v3))
    {
        v2 = a4;
        v1 = a3;
        v0 = a2;
        v15 = sub_1032e910(a0, sub_10326fd0(a1));
    }
    else
    {
        v2 = a4;
        v1 = a3;
        v0 = a2;
        v16 = sub_10326e70(a1);
        v15 = g_1038b2ac(a0, v16);
    }
    v17 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v17) = v6;
    return v15;
}
```

## `sub_1032abb4` `0x1032abb4`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032abb4(void)
{
}
```

## `sub_1032abf0` `0x1032abf0`

_216 bytes. refs "CreateDialogIndirectParamW"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b2ec;
extern unsigned int g_1038e180;
extern unsigned int g_103a29f8;
extern int g_103a2a70;

unsigned int sub_1032abf0(int a0, int a1, int a2, int a3, int a4)
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
    v4 = sub_1036cbc3;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v1 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    if (!((char)g_103a29f8 & 1))
    {
        g_103a29f8 = g_103a29f8 | 1;
        v5 = 0;
        sub_10314590(&v2, "CreateDialogIndirectParamW");
        v5 = 1;
        v0 = &v2;
        sub_1032e8e0(&v2, &g_103a2a70, 1);
        v5 = 0;
        sub_10314610(&v2);
        v5 = 4294967295;
    }
    v12 = (!(char)sub_1032e630(v0) ? g_1038b2ec(a0, a1, a2, a3, a4) : sub_1032e910(a0, a1, a2, a3, a4));
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v3;
    return v12;
}
```

## `sub_1032ac9f` `0x1032ac9f`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032ac9f(void)
{
}
```

## `sub_1032acd0` `0x1032acd0`

_101 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b340;

int sub_1032acd0(int a0, int a1)
{
    int v2;  // eax
    unsigned int v3;  // eax
    char v0;  // [bp+0x0]

    if ((char)sub_1032e630(&v0) && (char)sub_10327630(a1))
        return -(-(0 < sub_1032e760(a0, 12, 0, sub_10326fd0(a1))));
    v2 = sub_10326e70(a1);
    v3 = -(-(0 < g_1038b340(a0, 12, 0, v2)));
    return v3;
}
```

## `sub_1032ad16` `0x1032ad16`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032ad16(void)
{
}
```

## `sub_1032ad40` `0x1032ad40`

_181 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b340;
extern unsigned int g_1038e180;

int sub_1032ad40(int a0, unsigned int a1)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4146
    unsigned long v11;  // 4160
    unsigned int v12;  // eax
    unsigned long v14;  // 4117
    unsigned int v0;  // [bp-0x2c]
    char v1;  // [bp-0x25]
    int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char v5;  // [bp-0x8], Other Possible Types: unsigned int
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036cbff;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    v2 = g_1038b340(a1, 14, 0, 0, g_1038e180 ^ &v6, 0);
    v1 = 0;
    sub_1032e240(v2 + 1, &v1);
    v5 = 1;
    v12 = sub_1032e2e0(0);
    g_1038b340(a1, 13, v2 + 1, v12);
    sub_10314590(a0, sub_1032e2e0(0));
    v0 = 1;
    v5 = 0;
    sub_1032e280(0);
    v14 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v14) = v3;
    return a0;
}
```

## `sub_1032ae00` `0x1032ae00`

_376 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_1032ae00(unsigned int a0, unsigned int a1)
{
    unsigned long v13;  // ldt
    unsigned long v14;  // gdt
    unsigned short v15;  // fs
    unsigned long v16;  // 4135
    unsigned long v17;  // 4149
    unsigned int v20;  // eax
    unsigned long v21;  // 4113
    int v0;  // [bp-0xb8]
    int v1;  // [bp-0xb4]
    int v2;  // [bp-0xb0]
    int v3;  // [bp-0xac]
    unsigned int v4;  // [bp-0xa8]
    char v5;  // [bp-0xa4]
    char v6;  // [bp-0x88]
    unsigned short v7;  // [bp-0x26]
    int v8;  // [bp-0x14]
    unsigned int v9;  // [bp-0x10]
    unsigned int v10;  // [bp-0xc]
    unsigned int v11;  // [bp-0x8], Other Possible Types: char
    char v12;  // [bp-0x4]

    v11 = 4294967295;
    v10 = sub_1036cc57;
    v16 = _ccall(v13, v14, (unsigned int)v15, 0);
    v9 = *((int *)v16);
    v17 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int **)v17) = &v9;
    v4 = 0;
    if ((char)sub_1032e630(g_1038e180 ^ &v12))
    {
        v8 = sub_1032e760(a1, 14, 0, 0);
        v7 = 0;
        sub_1032e3b0(v8 + 1, &v7);
        v11 = 1;
        sub_1032e760(a1, 13, v8 + 1, sub_1032e410(0));
        sub_1031fc10(a0, sub_1032e410(0));
        v4 |= 1;
        v11 = 0;
        sub_1032e3f0(0);
        v20 = a0;
    }
    else
    {
        v3 = sub_1032ad40(&v5, a1);
        v2 = v3;
        v11 = 2;
        v1 = sub_10319e80(&v6, v2);
        v0 = v1;
        v11 = 3;
        sub_10326c30(v0, a0);
        v4 |= 1;
        v11 = 2;
        sub_10319f00(&v6);
        v11 = 0;
        sub_10314610(&v5);
        v20 = a0;
    }
    v21 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int *)v21) = v9;
    return v20;
}
```

## `sub_1032aed6` `0x1032aed6`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1032aed6(void)
{
}
```

## `sub_1032af80` `0x1032af80`

_429 bytes. refs "RegisterClassW"_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
    unsigned int field_10;
    unsigned int field_14;
    unsigned int field_18;
    unsigned int field_1c;
    unsigned int field_20;
    unsigned int field_24;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b330;
extern unsigned int g_1038e180;
extern unsigned int g_103a2a00;
extern int g_103a2a70;

short sub_1032af80(struct_0 *idx)
{
    unsigned long v21;  // ldt
    unsigned long v22;  // gdt
    unsigned short v23;  // fs
    unsigned long v24;  // 4169
    unsigned long v25;  // 4173
    unsigned long v26;  // 4114
    char *v0;  // [bp-0x130]
    unsigned int v1;  // [bp-0x124]
    unsigned short v2;  // [bp-0x11e]
    char v3;  // [bp-0x11c]
    unsigned int v4;  // [bp-0x100]
    unsigned int v5;  // [bp-0xfc]
    unsigned int v6;  // [bp-0xf8]
    unsigned int v7;  // [bp-0xf4]
    unsigned int v8;  // [bp-0xf0]
    unsigned int v9;  // [bp-0xec]
    unsigned int v10;  // [bp-0xe8]
    unsigned int v11;  // [bp-0xe4]
    int v12;  // [bp-0xe0]
    int v13;  // [bp-0xdc]
    char v14;  // [bp-0xd8]
    char v15;  // [bp-0x78]
    unsigned int v16;  // [bp-0x14]
    unsigned int v17;  // [bp-0x10]
    unsigned int v18;  // [bp-0xc]
    char v19;  // [bp-0x8], Other Possible Types: unsigned int
    char v20;  // [bp-0x4]

    v19 = 4294967295;
    v18 = sub_1036cca1;
    v24 = _ccall(v21, v22, (unsigned int)v23, 0);
    v17 = *((int *)v24);
    v16 = g_1038e180 ^ &v20;
    v1 = v16;
    v25 = _ccall(v21, v22, (unsigned int)v23, 0);
    *((unsigned int **)v25) = &v17;
    if (!((char)g_103a2a00 & 1))
    {
        g_103a2a00 = g_103a2a00 | 1;
        v19 = 0;
        sub_10314590(&v3, "RegisterClassW");
        v19 = 1;
        v0 = &v3;
        sub_1032e940(&v3, &g_103a2a70, 1);
        v19 = 0;
        sub_10314610(&v3);
        v19 = 4294967295;
    }
    if ((char)sub_1032e630(v0))
    {
        sub_10335b10(idx);
    }
    else
    {
        sub_10326770(&v14, idx->field_24);
        v19 = 2;
        sub_10326770(&v15, idx->field_20);
        v19 = 3;
        v6 = idx->field_8;
        v7 = idx->field_c;
        v11 = idx->field_1c;
        v10 = idx->field_18;
        v9 = idx->field_14;
        v8 = idx->field_10;
        v5 = idx->field_4;
        v13 = sub_10327130(&v14);
        v12 = sub_10327130(&v15);
        v4 = idx->field_0;
        v2 = g_1038b330(&v4);
        v19 = 2;
        sub_10319f00(&v15);
        v19 = 4294967295;
        sub_10319f00(&v14);
    }
    v26 = _ccall(v21, v22, (unsigned int)v23, 0);
    *((unsigned int *)v26) = v17;
    return sub_10351225();
}
```

## `sub_1032b130` `0x1032b130`

_453 bytes. refs "RegisterClassExW"_

```c
typedef struct struct_0 {
    unsigned int field_0;
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
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b2a8;
extern unsigned int g_1038e180;
extern unsigned int g_103a2a08;
extern int g_103a2a70;

short sub_1032b130(struct_0 *idx)
{
    unsigned long v23;  // ldt
    unsigned long v24;  // gdt
    unsigned short v25;  // fs
    unsigned long v26;  // 4169
    unsigned long v27;  // 4173
    unsigned long v28;  // 4114
    char *v0;  // [bp-0x138]
    unsigned int v1;  // [bp-0x12c]
    unsigned short v2;  // [bp-0x126]
    char v3;  // [bp-0x124]
    unsigned int v4;  // [bp-0x108]
    unsigned int v5;  // [bp-0x104]
    unsigned int v6;  // [bp-0x100]
    unsigned int v7;  // [bp-0xfc]
    unsigned int v8;  // [bp-0xf8]
    unsigned int v9;  // [bp-0xf4]
    unsigned int v10;  // [bp-0xf0]
    unsigned int v11;  // [bp-0xec]
    unsigned int v12;  // [bp-0xe8]
    int v13;  // [bp-0xe4]
    int v14;  // [bp-0xe0]
    unsigned int v15;  // [bp-0xdc]
    char v16;  // [bp-0xd8]
    char v17;  // [bp-0x78]
    unsigned int v18;  // [bp-0x14]
    unsigned int v19;  // [bp-0x10]
    unsigned int v20;  // [bp-0xc]
    char v21;  // [bp-0x8], Other Possible Types: unsigned int
    char v22;  // [bp-0x4]

    v21 = 4294967295;
    v20 = sub_1036ccf5;
    v26 = _ccall(v23, v24, (unsigned int)v25, 0);
    v19 = *((int *)v26);
    v18 = g_1038e180 ^ &v22;
    v1 = v18;
    v27 = _ccall(v23, v24, (unsigned int)v25, 0);
    *((unsigned int **)v27) = &v19;
    if (!((char)g_103a2a08 & 1))
    {
        g_103a2a08 = g_103a2a08 | 1;
        v21 = 0;
        sub_10314590(&v3, "RegisterClassExW");
        v21 = 1;
        v0 = &v3;
        sub_1032e970(&v3, &g_103a2a70, 1);
        v21 = 0;
        sub_10314610(&v3);
        v21 = 4294967295;
    }
    if ((char)sub_1032e630(v0))
    {
        sub_10335b10(idx);
    }
    else
    {
        sub_10326770(&v16, idx->field_28);
        v21 = 2;
        sub_10326770(&v17, idx->field_24);
        v21 = 3;
        v4 = idx->field_0;
        v7 = idx->field_c;
        v8 = idx->field_10;
        v12 = idx->field_20;
        v11 = idx->field_1c;
        v10 = idx->field_18;
        v9 = idx->field_14;
        v6 = idx->field_8;
        v14 = sub_10327130(&v16);
        v13 = sub_10327130(&v17);
        v5 = idx->field_4;
        v15 = idx->field_2c;
        v2 = g_1038b2a8(&v4);
        v21 = 2;
        sub_10319f00(&v17);
        v21 = 4294967295;
        sub_10319f00(&v16);
    }
    v28 = _ccall(v23, v24, (unsigned int)v25, 0);
    *((unsigned int *)v28) = v19;
    return sub_10351225();
}
```

## `sub_1032b300` `0x1032b300`

_292 bytes. refs "CreateWindowExW"_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

extern struct_0 *g_1038b334;
extern unsigned int g_1038e180;
extern unsigned int g_103a2a10;
extern int g_103a2a70;

unsigned int sub_1032b300(int a0, int a1, int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int a10, unsigned int a11)
{
    unsigned long v17;  // ldt
    unsigned long v18;  // gdt
    unsigned short v19;  // fs
    unsigned long v20;  // 4165
    unsigned long v21;  // 4169
    unsigned int v22;  // eax
    int v23;  // eax
    unsigned long v24;  // 4113
    struct_0 *v0;  // [bp-0x64], Other Possible Types: int
    unsigned int v1;  // [bp-0x60]
    unsigned int v2;  // [bp-0x5c]
    unsigned int v3;  // [bp-0x58]
    unsigned int v4;  // [bp-0x54]
    unsigned int v5;  // [bp-0x50]
    unsigned int v6;  // [bp-0x4c]
    unsigned int v7;  // [bp-0x48]
    unsigned int v8;  // [bp-0x44]
    unsigned int v9;  // [bp-0x40]
    char *v10;  // [bp-0x3c]
    unsigned int v11;  // [bp-0x30]
    char v12;  // [bp-0x2c]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    char v15;  // [bp-0x8], Other Possible Types: unsigned int
    char v16;  // [bp-0x4]

    v15 = 4294967295;
    v14 = sub_1036cd33;
    v20 = _ccall(v17, v18, (unsigned int)v19, 0);
    v13 = *((int *)v20);
    v11 = g_1038e180 ^ &v16;
    v21 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((unsigned int **)v21) = &v13;
    if (!((char)g_103a2a10 & 1))
    {
        g_103a2a10 = g_103a2a10 | 1;
        v15 = 0;
        sub_10314590(&v12, "CreateWindowExW");
        v15 = 1;
        v10 = &v12;
        sub_1032e9a0(&v12, &g_103a2a70, 1);
        v15 = 0;
        sub_10314610(&v12);
        v15 = 4294967295;
    }
    if ((char)sub_1032e630(v10))
    {
        v9 = a11;
        v8 = a10;
        v7 = a9;
        v6 = a8;
        v5 = a7;
        v4 = a6;
        v3 = a5;
        v2 = a4;
        v1 = a3;
        v0 = sub_10326fd0(a2);
        v22 = sub_1032e9d0(a0, sub_10326fd0(a1));
    }
    else
    {
        v9 = a11;
        v8 = a10;
        v7 = a9;
        v6 = a8;
        v5 = a7;
        v4 = a6;
        v3 = a5;
        v2 = a4;
        v1 = a3;
        v0 = sub_10326e70(a2);
        v23 = sub_10326e70(a1);
        v22 = g_1038b334(a0, v23);
    }
    v24 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((unsigned int *)v24) = v13;
    return v22;
}
```

## `sub_1032b3d5` `0x1032b3d5`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032b3d5(void)
{
}
```

## `sub_1032b430` `0x1032b430`

_226 bytes. refs "CreateDialogParamW"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b2a4;
extern unsigned int g_1038e180;
extern unsigned int g_103a2a18;
extern int g_103a2a70;

unsigned int sub_1032b430(int a0, int a1, unsigned int a2, unsigned int a3, unsigned int a4)
{
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // fs
    unsigned long v13;  // 4165
    unsigned long v14;  // 4169
    unsigned int v15;  // eax
    int v16;  // eax
    unsigned long v17;  // 4113
    unsigned int v0;  // [bp-0x48]
    unsigned int v1;  // [bp-0x44]
    unsigned int v2;  // [bp-0x40]
    char *v3;  // [bp-0x3c]
    unsigned int v4;  // [bp-0x30]
    char v5;  // [bp-0x2c]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    char v8;  // [bp-0x8], Other Possible Types: unsigned int
    char v9;  // [bp-0x4]

    v8 = 4294967295;
    v7 = sub_1036cd64;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v6 = *((int *)v13);
    v4 = g_1038e180 ^ &v9;
    v14 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v14) = &v6;
    if (!((char)g_103a2a18 & 1))
    {
        g_103a2a18 = g_103a2a18 | 1;
        v8 = 0;
        sub_10314590(&v5, "CreateDialogParamW");
        v8 = 1;
        v3 = &v5;
        sub_1032ea20(&v5, &g_103a2a70, 1);
        v8 = 0;
        sub_10314610(&v5);
        v8 = 4294967295;
    }
    if ((char)sub_1032e630(v3))
    {
        v2 = a4;
        v1 = a3;
        v0 = a2;
        v15 = sub_1032e910(a0, sub_10326fd0(a1));
    }
    else
    {
        v2 = a4;
        v1 = a3;
        v0 = a2;
        v16 = sub_10326e70(a1);
        v15 = g_1038b2a4(a0, v16);
    }
    v17 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v17) = v6;
    return v15;
}
```

## `sub_1032b4e4` `0x1032b4e4`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032b4e4(void)
{
}
```

## `sub_1032b520` `0x1032b520`

_241 bytes. refs "DrawTextW"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b2a0;
extern unsigned int g_1038e180;
extern unsigned int g_103a2a20;
extern int g_103a2a70;

unsigned int sub_1032b520(int a0, int a1, unsigned int a2, unsigned int a3, unsigned int a4)
{
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // fs
    unsigned long v13;  // 4165
    unsigned long v14;  // 4169
    unsigned int v15;  // eax
    int v16;  // eax
    unsigned long v17;  // 4113
    unsigned int v0;  // [bp-0x48]
    unsigned int v1;  // [bp-0x44]
    unsigned int v2;  // [bp-0x40]
    char *v3;  // [bp-0x3c]
    unsigned int v4;  // [bp-0x30]
    char v5;  // [bp-0x2c]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    char v8;  // [bp-0x8], Other Possible Types: unsigned int
    char v9;  // [bp-0x4]

    v8 = 4294967295;
    v7 = sub_1036cd95;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v6 = *((int *)v13);
    v4 = g_1038e180 ^ &v9;
    v14 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v14) = &v6;
    if (!((char)g_103a2a20 & 1))
    {
        g_103a2a20 = g_103a2a20 | 1;
        v8 = 0;
        sub_10314590(&v5, "DrawTextW");
        v8 = 1;
        v3 = &v5;
        sub_1032ea50(&v5, &g_103a2a70, 1);
        v8 = 0;
        sub_10314610(&v5);
        v8 = 4294967295;
    }
    if ((char)sub_1032e630(v3) && (char)sub_10327630(a1))
    {
        v2 = a4;
        v1 = a3;
        v0 = a2;
        v15 = sub_1032e910(a0, sub_10326fd0(a1));
    }
    else
    {
        v2 = a4;
        v1 = a3;
        v0 = a2;
        v16 = sub_10326e70(a1);
        v15 = g_1038b2a0(a0, v16);
    }
    v17 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v17) = v6;
    return v15;
}
```

