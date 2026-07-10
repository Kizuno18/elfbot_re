# elfbot.dll decompiled — loader 0x004113d6..0x0041206e

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_004113d6` `0x004113d6`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4113d6(unsigned int a0, unsigned int a1)
{
    return sub_4113d8();
}
```

## `sub_004113d8` `0x004113d8`

_247 bytes. (leaf/helper — see body)_

```c
typedef struct SECURITY_ATTRIBUTES {
    unsigned int nLength;
    void* lpSecurityDescriptor;
    int bInheritHandle;
} SECURITY_ATTRIBUTES;

int sub_4113d8(PSTR a0, unsigned int a1)
{
    unsigned int v14;  // ebx
    unsigned int v15;  // esi
    unsigned int v16;  // edi
    unsigned long v17;  // ldt
    unsigned long v18;  // gdt
    unsigned short v19;  // fs
    unsigned long v20;  // 4174
    unsigned long v21;  // 4183
    unsigned long v22;  // 4118
    unsigned int v0;  // [bp-0x50]
    unsigned int v1;  // [bp-0x4c]
    char *v2;  // [bp-0x48], Other Possible Types: unsigned int
    unsigned int v3;  // [bp-0x44]
    unsigned int v4;  // [bp-0x40]
    unsigned int v5;  // [bp-0x3c]
    unsigned int v6;  // [bp-0x38]
    PWSTR v7;  // [bp-0x34]
    unsigned int v8;  // [bp-0x30]
    unsigned int v9;  // [bp-0x2c]
    PWSTR v10;  // [bp-0x28]
    HLOCAL v11;  // [bp-0x14]
    SECURITY_ATTRIBUTES v12;  // [bp-0x10]
    char v13;  // [bp-0x4]

    v5 = v14;
    v4 = v15;
    v3 = v16;
    v7 = NULL;
    v6 = 0;
    v10 = NULL;
    v9 = 0;
    v8 = 0;
    v2 = &v13;
    v1 = sub_4114dd;
    v20 = _ccall(v17, v18, (unsigned int)v19, 0);
    v0 = *((int *)v20);
    v21 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((unsigned int **)v21) = &v0;
    if (!(GetVersion() & 0x80000000))
    {
        v11 = NULL;
        sub_41101c();
        sub_409eac();
        sub_403be8(&v9);
        sub_403c88();
        sub_409ee0();
        if (!CreateFileMappingW(0xffffffff, &v12, PAGE_READWRITE, 0, a1, v10))
        {
            sub_403be8();
            sub_409ee0();
            CreateFileMappingW(0xffffffff, &v12, PAGE_READWRITE, 0, a1, v7);
        }
        if (v11)
            LocalFree(v11);
    }
    else
    {
        CreateFileMappingA(0xffffffff, NULL, PAGE_READWRITE, 0, a1, a0);
    }
    v22 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((unsigned int *)v22) = v0;
    v2 = sub_4114e4;
    return sub_4114cf();
}
```

## `sub_004114cf` `0x004114cf`

_14 bytes. (leaf/helper — see body)_

```c
int sub_4114cf(void)
{
    return sub_403a34();
}
```

## `sub_004114dd` `0x004114dd`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4114dd(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004114e2` `0x004114e2`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4114e2(void)
{
    return sub_4114cf();
}
```

## `sub_004114e4` `0x004114e4`

_11 bytes. (leaf/helper — see body)_

```c
int sub_4114e4(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // ebx

    return v0;
}
```

## `sub_004114ef` `0x004114ef`

_1 bytes. (leaf/helper — see body)_

```c
void sub_4114ef(unsigned int a0, unsigned int a1)
{
    sub_4114f0();
    return;
}
```

## `sub_004114f0` `0x004114f0`

_190 bytes. (leaf/helper — see body)_

```c
int sub_4114f0(PSTR a0, unsigned int a1)
{
    unsigned int v12;  // ebx
    unsigned int v13;  // esi
    unsigned int v14;  // edi
    unsigned long v15;  // ldt
    unsigned long v16;  // gdt
    unsigned short v17;  // fs
    unsigned long v18;  // 4194
    unsigned long v19;  // 4198
    unsigned int v20;  // ebx
    unsigned long v21;  // 4118
    unsigned int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x2c]
    char *v2;  // [bp-0x28], Other Possible Types: unsigned int
    unsigned int v3;  // [bp-0x24]
    unsigned int v4;  // [bp-0x20]
    unsigned int v5;  // [bp-0x1c]
    unsigned int v6;  // [bp-0x18]
    PWSTR v7;  // [bp-0x14]
    unsigned int v8;  // [bp-0x10]
    unsigned int v9;  // [bp-0xc]
    PWSTR v10;  // [bp-0x8]
    char v11;  // [bp-0x4]

    v10 = NULL;
    v9 = 0;
    v8 = 0;
    v7 = NULL;
    v6 = 0;
    v5 = v12;
    v4 = v13;
    v3 = v14;
    v2 = &v11;
    v1 = sub_4115bc;
    v18 = _ccall(v15, v16, (unsigned int)v17, 0);
    v0 = *((int *)v18);
    v19 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int **)v19) = &v0;
    v20 = (!a1 ? 4 : 983071);
    if (!(GetVersion() & 0x80000000))
    {
        sub_409eac();
        sub_403be8(&v9);
        sub_403c88();
        sub_409ee0();
        if (!OpenFileMappingW(v20, 0, v10))
        {
            sub_403be8();
            sub_409ee0();
            OpenFileMappingW(v20, 0, v7);
        }
    }
    else
    {
        OpenFileMappingA(v20, 0, a0);
    }
    v21 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int *)v21) = v0;
    v2 = sub_4115c3;
    return sub_4115ae();
}
```

## `sub_004115ae` `0x004115ae`

_14 bytes. (leaf/helper — see body)_

```c
int sub_4115ae(void)
{
    return sub_403a34();
}
```

## `sub_004115bc` `0x004115bc`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4115bc(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004115c1` `0x004115c1`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4115c1(void)
{
    return sub_4115ae();
}
```

## `sub_004115c3` `0x004115c3`

_11 bytes. (leaf/helper — see body)_

```c
int sub_4115c3(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // esi

    return v0;
}
```

## `sub_004115ce` `0x004115ce`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4115ce(void)
{
    sub_4115d0();
    return;
}
```

## `sub_004115d0` `0x004115d0`

_218 bytes. refs ", *(v7), ", ", 0);
    sub_409b54(&v2, "_

```c
int sub_4115d0(void)
{
    int v8;  // edi
    int v9;  // esi
    char v18;  // cl
    unsigned long v19;  // 4118
    int v10;  // ebx
    int v11;  // eax
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    unsigned short v14;  // fs
    unsigned long v15;  // 4148
    unsigned int v16;  // 4103
    unsigned long v17;  // 4152
    unsigned int v0;  // [bp-0x5c]
    unsigned int v1;  // [bp-0x34]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]
    char v6;  // [bp+0x0]
    int *v7;  // [bp+0x4]

    v4 = 0;
    v3 = 0;
    v2 = 0;
    sub_403e68(v8, v9, v10, 0, 0, 0, 0, 0, v11, &v6);
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    v16 = *((int *)v15);
    v1 = *((int *)v15);
    v17 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v17) = &v1;
    if (v18)
    {
        sub_409eac(v16, sub_4116b8, &v5);
    }
    else
    {
        sub_409eac(v16, sub_4116b8, &v5);
        GetCurrentProcessId();
        sub_409b54(&v3, " ", 0);
        sub_403d40(0);
    }
    sub_409eac();
    sub_409eac(", ", *(v7), ", ", 0);
    sub_409b54(&v2, " ", 0);
    sub_403d40(0);
    v19 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int *)v19) = 0;
    v0 = sub_4116bf;
    sub_4116aa();
    return;
}
```

## `sub_004116aa` `0x004116aa`

_14 bytes. (leaf/helper — see body)_

```c
int sub_4116aa(void)
{
    return sub_403a34();
}
```

## `sub_004116b8` `0x004116b8`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4116b8(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004116bd` `0x004116bd`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4116bd(void)
{
    return sub_4116aa();
}
```

## `sub_004116bf` `0x004116bf`

_9 bytes. (leaf/helper — see body)_

```c
void sub_4116bf(unsigned int a0, unsigned int a1)
{
    return;
}
```

## `sub_004116df` `0x004116df`

_170 bytes. (leaf/helper — see body)_

```c
int sub_4116df(void)
{
    unsigned short v15;  // dx
    unsigned int v16;  // 4101
    unsigned int v25;  // esi
    unsigned int *v26;  // eax
    unsigned long v27;  // 4118
    unsigned int v17;  // ebx
    unsigned int v18;  // esi
    unsigned long v19;  // ldt
    unsigned long v20;  // gdt
    unsigned short v21;  // fs
    unsigned long v22;  // 4128
    unsigned int v23;  // 4103
    unsigned long v24;  // 4137
    unsigned int *v0;  // [bp-0x38]
    unsigned int v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x24]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]
    unsigned int v8;  // [bp-0x4]
    char v10;  // [bp+0xfff8f]
    int v11;  // [bp+0xffff4]
    int v12;  // [bp+0xffff8]
    char v13;  // [bp+0x100003]
    void* v14;  // [bp+0x10000c]

    v10 += (char)v15;
    v16 = x86g_dirtyhelper_IN(Conv(16I->32I, vvar_16{r16|2b}), 0x1<32>);
    v8 = 0;
    v7 = 0;
    v6 = 0;
    v5 = 0;
    v4 = v17;
    v3 = v18;
    v13 = v16;
    v22 = _ccall(v19, v20, (unsigned int)v21, 0);
    v23 = *((int *)v22);
    v2 = *((int *)v22);
    v24 = _ccall(v19, v20, (unsigned int)v21, 0);
    *((unsigned int **)v24) = &v2;
    sub_409eac(v23, sub_411797, /* unsupported instruction */);
    sub_4115d0(/* unsupported instruction */ - 16, ", ", v12);
    sub_403d40(v11);
    v0 = 0xffffffff;
    v25 = sub_4114f0(sub_403e78(-1), 4294967295);
    if (v25)
    {
        v0 = NULL;
        v26 = (unsigned int *)MapViewOfFile(v25, FILE_MAP_READ, 0, 0, NULL);
        v0 = v0;
        if (v26)
        {
            *((unsigned int *)(int)v14[4]) = *(v26);
            UnmapViewOfFile(v26);
            v0 = v26;
        }
        CloseHandle(v25);
    }
    v27 = _ccall(v19, v20, (unsigned int)v21, 0);
    *((unsigned int **)v27) = v0;
    v1 = sub_41179e;
    sub_411789();
    return;
}
```

## `sub_00411789` `0x00411789`

_14 bytes. (leaf/helper — see body)_

```c
int sub_411789(void)
{
    return sub_403a34();
}
```

## `sub_00411797` `0x00411797`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_411797(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041179c` `0x0041179c`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41179c(void)
{
    return sub_411789();
}
```

## `sub_0041179e` `0x0041179e`

_8 bytes. (leaf/helper — see body)_

```c
int sub_41179e(unsigned int a0)
{
    unsigned int v0;  // ebx

    return v0;
}
```

## `sub_004117b3` `0x004117b3`

_78 bytes. (leaf/helper — see body)_

```c
int sub_4117b3(unsigned int a0, unsigned short a1)
{
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp-0x4]
    char v3;  // [bp+0xfff8f]
    unsigned int *v4;  // [bp+0x100000]

    v3 += (char)a1;
    v1 = a0;
    v4 = _INSERT(0, 0, x86g_dirtyhelper_IN(Conv(16I->32I, vvar_1), 0x1<32>));
    if (!(GetVersion() & 0x80000000))
    {
        4265696();
    }
    else if (*(v4) < 0x80000000)
    {
        v0 = /* unsupported instruction */;
        4265696();
    }
    else
    {
        v0 = /* unsupported instruction */;
        4265696();
    }
}
```

## `sub_00411801` `0x00411801`

_3 bytes. (leaf/helper — see body)_

```c
int sub_411801(void)
{
    sub_411804();
    return;
}
```

## `sub_00411804` `0x00411804`

_132 bytes. (leaf/helper — see body)_

```c
int sub_411804(void)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4147
    unsigned int v10;  // 4113
    unsigned long v11;  // 4156
    int v12;  // ebx
    unsigned int v13;  // eax
    unsigned long v14;  // 4118
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x10]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v2 = 0;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v10 = *((int *)v9);
    v1 = *((int *)v9);
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v1;
    sub_409eac(v10, sub_411896, &v3, v12, 0, 0, 0, &v4);
    sub_4115d0(&v2, ", ", 0);
    sub_403d40(0);
    v13 = sub_4114f0(sub_403e78(0), 0);
    if (v13)
        CloseHandle(v13);
    v14 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v14) = 0;
    v0 = sub_41189d;
    sub_411888();
    return;
}
```

## `sub_00411888` `0x00411888`

_14 bytes. (leaf/helper — see body)_

```c
int sub_411888(void)
{
    return sub_403a34();
}
```

## `sub_00411896` `0x00411896`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_411896(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041189b` `0x0041189b`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41189b(void)
{
    return sub_411888();
}
```

## `sub_0041189d` `0x0041189d`

_7 bytes. (leaf/helper — see body)_

```c
int sub_41189d(void)
{
    unsigned int v1;  // ebx

    return v1;
}
```

## `sub_004118af` `0x004118af`

_73 bytes. (leaf/helper — see body)_

```c
int sub_4118af(unsigned int a0, char a1, unsigned int a2)
{
    int v2;  // eax
    char v0;  // [bp+0xfff8f]
    void* v1;  // [bp+0x10000c]

    v0 += a1;
    if (!(GetVersion() & 0x80000000))
        return sub_411804(/* unsupported instruction */);
    if ((int)v1[4] >= 0x80000000 || (v2 = sub_411804(/* unsupported instruction */), !(char)v2))
    {
        v2 = sub_411804(/* unsupported instruction */);
        if (!(char)v2)
            return 0;
    }
    return _INSERT(v2, 0, 1);
}
```

## `sub_004118f8` `0x004118f8`

_126 bytes. (leaf/helper — see body)_

```c
char sub_4118f8(unsigned int a0)
{
    unsigned int v2;  // ebx
    unsigned int v3;  // esi
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]

    v1 = v2;
    v0 = v3;
    4265908();
}
```

## `sub_00411976` `0x00411976`

_2 bytes. (leaf/helper — see body)_

```c
int sub_411976(void)
{
    sub_411978();
    return;
}
```

## `sub_00411978` `0x00411978`

_109 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    unsigned short field_0;
    struct struct_2 *field_2;
} struct_1;

typedef struct struct_0 {
    char field_0;
    unsigned int field_1;
} struct_0;

typedef struct struct_2 {
    struct struct_0 *field_0;
} struct_2;

int sub_411978(void)
{
    struct_1 *v3;  // eax
    struct_0 *iter;  // [bp-0x8], Other Possible Types: struct_1 *, unsigned int
    char v1;  // [bp-0x4]

    iter = v3;
    if (!iter)
    {
        return;
    }
    else if (sub_4118f8(&v1))
    {
        return;
    }
    else if (iter->field_0 == 0x25ff)
    {
        iter = *((int *)*((int *)&(&iter->field_0)[1]));
        if (sub_4118f8(&v1))
        {
            return;
        }
        else if (iter->field_0 == 104)
        {
            iter = *((int *)&(&iter->field_0)[1]);
            return;
        }
        else
        {
            return;
        }
    }
    else
    {
        return;
    }
}
```

## `sub_004119e5` `0x004119e5`

_3 bytes. (leaf/helper — see body)_

```c
int sub_4119e5(void)
{
    sub_4119e8();
    return;
}
```

## `sub_004119e8` `0x004119e8`

_123 bytes. (leaf/helper — see body)_

```c
int sub_4119e8(void)
{
    void* i;  // ebx
    enum VIRTUAL_ALLOCATION_TYPE v6;  // eax
    enum VIRTUAL_ALLOCATION_TYPE v7;  // eax
    unsigned int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x2c]
    int v2;  // [bp-0x28]
    unsigned int v3;  // [bp-0x1c]

    if ((GetVersion() & 0x80000000))
    {
        sub_4053f4(NULL, v7, PAGE_GRAPHICS_READONLY, 64);
        return;
    }
    for (i = 0x5f040000; VirtualQuery(i, &v2, 0x1c) == 0x1c; i += v3)
    {
        if (*((unsigned int *)(&v2 + 16)) == 0x10000)
        {
            v1 = 64;
            v0 = 0x2000;
            sub_411a16();
            return;
        }
        v3 = (*((unsigned int *)(&v2 + 12)) < 0x10000 ? 0x10000 : *((unsigned int *)(&v2 + 12)) & 0xffff0000);
    }
    sub_4053f4(NULL, v6, PAGE_GRAPHICS_READONLY, 64);
    return;
}
```

## `sub_00411a16` `0x00411a16`

_15 bytes. (leaf/helper — see body)_

```c
int sub_411a16(unsigned int a0, UIntPtr a1)
{
    enum VIRTUAL_ALLOCATION_TYPE v1;  // edi
    enum PAGE_PROTECTION_FLAGS v0;  // [bp+0x0]

    sub_4053f4(a1, v1, v0, a0);
}
```

## `sub_00411a72` `0x00411a72`

_2 bytes. (leaf/helper — see body)_

```c
int sub_411a72(void)
{
    sub_411a74();
    return;
}
```

## `sub_00411a74` `0x00411a74`

_231 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[6];
    unsigned short field_6;
    char padding_8[240];
    char field_f8;
    char field_f9;
    char field_fa;
    char field_fb;
    char field_fc;
    char field_fd;
    char padding_fe[6];
    unsigned int field_104;
    int field_108;
} struct_0;

typedef struct struct_1 {
    char padding_0[28];
    unsigned int field_1c;
} struct_1;

int sub_411a74(void)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // esi
    unsigned int idx;  // edx
    char iter[4];  // eax
    unsigned int v18;  // eax
    int v19;  // edx
    unsigned int v8;  // edi
    struct_0 *v9;  // ebp
    struct_1 *v10;  // edi
    struct_0 *node;  // ebx
    unsigned int v12;  // eax
    unsigned int v13;  // eax
    unsigned int v14;  // eax
    unsigned int v0;  // [bp-0x50]
    char v1;  // [bp-0x38]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]
    unsigned int v4;  // [bp-0x4]

    v4 = v6;
    v3 = v7;
    v2 = v8;
    v9 = sub_40a658(0);
    v10 = (unsigned int)sub_40a6ec();
    if (!v9)
    {
        return;
    }
    else if (v10)
    {
        node = &v9->field_f8;
        v12 = v9->field_6 - 1;
        if (v12 < NULL)
            return;
        v13 = v12 + 1;
        while (true)
        {
            v14 = v13;
            if (node->padding_0[0] == 46 && (node->padding_0[1] == 100 || node->padding_0[1] == 0x44) && (node->padding_0[2] == 97 || node->padding_0[1] == 65) && (node->padding_0[3] == 116 || node->padding_0[1] == 84) && (node->padding_0[4] == 97 || node->padding_0[1] == 65) && !node->padding_0[5])
                break;
            node = &node->padding_8[32];
            v13 = v14 - 1;
            if (v14 == 1)
                return;
        }
        idx = 0;
        iter = &v1;
        do
        {
            *((unsigned int *)&iter[0]) = *((int *)(v10->field_1c + v18 + idx * 4)) + v18;
            idx += 1;
            iter += 1;
        } while (idx != 10);
        v19 = sub_4093d8(2147483647, 0, 0, *((int *)&node->padding_8[8]));
        if (v19 < NULL)
            return;
        v0 = v18 + *((int *)&node->padding_8[4]) + v19;
        return;
    }
    else
    {
        return;
    }
}
```

## `sub_00411b5b` `0x00411b5b`

_1 bytes. (leaf/helper — see body)_

```c
int sub_411b5b(void)
{
    sub_411b5c();
    return;
}
```

## `sub_00411b5c` `0x00411b5c`

_103 bytes. (leaf/helper — see body)_

```c
int sub_411b5c(void)
{
    unsigned int v2;  // eax
    unsigned int idx;  // edi
    unsigned int v4;  // edx
    unsigned int v5;  // ecx
    char v0;  // [bp-0xd]

    if (!v2)
        return;
    idx = 0;
    while (true)
    {
        if (!*((int *)(v2 + idx * 4)))
            return;
        if (*((int *)(v2 + idx * 4)) == v4)
            break;
        idx += 1;
    }
    v0 = sub_40eb40();
    if (!(char)sub_40ec20())
        return;
    *((unsigned int *)(v2 + idx * 4)) = v5;
    if (!v0)
        return;
    sub_40ecb0();
    return;
}
```

## `sub_00411bc3` `0x00411bc3`

_1 bytes. (leaf/helper — see body)_

```c
int sub_411bc3(void)
{
    sub_411bc4();
    return;
}
```

## `sub_00411bc4` `0x00411bc4`

_213 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    int field_14;
    char padding_18[4];
    unsigned int field_1c;
} struct_0;

int sub_411bc4(void)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned int v18;  // eax
    unsigned int v19;  // edx
    unsigned int v20;  // eax
    unsigned int v21;  // ecx
    unsigned long v22;  // 4116
    unsigned short v10;  // fs
    unsigned long v11;  // 4155
    unsigned long v12;  // 4164
    struct_0 *v13;  // eax
    unsigned int v14;  // eax
    int v15;  // eax
    unsigned int index;  // esi
    int v17;  // eax
    unsigned int v0;  // [bp-0x2c]
    unsigned int v1;  // [bp-0x28]
    char *v2;  // [bp-0x24]
    struct_0 *idx;  // [bp-0x14]
    char v4;  // [bp-0xe]
    char v5;  // [bp-0xd]
    char v6;  // [bp-0x4]

    v5 = 0;
    v2 = &v6;
    v1 = sub_411c8d;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v0 = *((int *)v11);
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v0;
    v13 = (unsigned int)sub_40a6ec();
    if (v13)
    {
        idx = v13;
        v14 = idx->field_14 - 1;
        if (v14 >= NULL)
        {
            v15 = v14 + 1;
            index = 0;
            do
            {
                v17 = v15;
                if (*((int *)(idx->field_1c + v18 + index * 4)) + v18 == v19 && (char)sub_411b5c())
                {
                    v4 = sub_40eb40();
                    if ((char)sub_40ec20())
                    {
                        *((unsigned int *)(idx->field_1c + v18 + index * 4)) = v21 - v18;
                        v5 = 1;
                        if (v4)
                        {
                            sub_40ecb0();
                            break;
                        }
                    }
                    else
                    {
                        sub_411b5c();
                        break;
                    }
                }
            } while ((index += 1, v20 = v17 - 1, v15 = (int)(v17 - 1), v17 != 1));
        }
    }
    v22 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v22) = v0;
    return;
}
```

## `sub_00411c8d` `0x00411c8d`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
    char padding_8[4];
    void* field_c;
    char padding_10[4];
    void* field_14;
    void* field_18;
} struct_1;

unsigned int sub_411c8d(int a0)
{
    struct_1 *v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x8]

    return sub_4030c0(v0, a0, v1);
}
```

## `sub_00411c92` `0x00411c92`

_5 bytes. (leaf/helper — see body)_

```c
void sub_411c92(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int *a10)
{
    unsigned int v0;  // [bp+0x0]

    sub_4034ec(v0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10);
}
```

## `sub_00411ca3` `0x00411ca3`

_1 bytes. (leaf/helper — see body)_

```c
void sub_411ca3(unsigned int a0)
{
    sub_411ca4();
    return;
}
```

## `sub_00411ca4` `0x00411ca4`

_127 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned short field_0;
    char padding_2[10];
    unsigned int field_c;
    char padding_10[44];
    unsigned int field_3c;
    char padding_40[64];
    unsigned int field_80;
} struct_0;

struct_0 * sub_411ca4(struct_0 *a0, unsigned int a1, unsigned int a2)
{
    struct_0 *v0;  // eax
    struct_0 *idx;  // ecx
    unsigned int v2;  // edi
    unsigned int v3;  // ebx
    struct_0 *node;  // edi
    unsigned int v5;  // esi
    unsigned int *iter;  // esi

    v0 = a0;
    if (v0->field_0 != 23117)
        return v0;
    idx = v0->field_3c + (char *)v0;
    if (idx->field_0 != 17744)
        return v0;
    v2 = idx->field_80;
    if (!v2)
        return v0;
    v3 = *((int *)&idx->padding_40[16]);
    if (v2 >= v3)
    {
        return v0;
    }
    else if (node)
    {
        for (node = v2 + (char *)v0; node->field_c; node = &node->padding_10[4])
        {
            if (!v5)
            {
                return v0;
            }
            else if (v5 >= v3)
            {
                return v0;
            }
            else if (v5 + (char *)a0)
            {
                for (v5 = *((int *)&node->padding_10[0]); *(iter); iter += 1)
                {
                    if (*(iter) == a1)
                    {
                        v0 = sub_40eb80(iter, 4);
                        if (v0)
                            *(iter) = a2;
                    }
                }
            }
            else
            {
                return v0;
            }
        }
        return v0;
    }
    else
    {
        return v0;
    }
}
```

## `sub_00411d23` `0x00411d23`

_1 bytes. (leaf/helper — see body)_

```c
void sub_411d23(void)
{
    return;
}
```

## `sub_00411d24` `0x00411d24`

_132 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned short field_0;
    char padding_2[10];
    unsigned int field_c;
    char padding_10[44];
    unsigned int field_3c;
    char padding_40[64];
    unsigned int field_80;
} struct_0;

extern struct_0 *g_41efe8;
extern struct_0 *g_41f018;

int sub_411d24(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v15;  // eax
    unsigned int v16;  // ecx
    unsigned int v17;  // edx
    unsigned int v18;  // ebx
    unsigned int v19;  // esi
    unsigned int v20;  // 4139
    unsigned int v21;  // id
    unsigned int v22;  // ac
    unsigned int i;  // ebx
    unsigned int v0;  // [bp-0x4c]
    unsigned int v1;  // [bp-0x48]
    unsigned int v2;  // [bp-0x40]
    char *v3;  // [bp-0x3c]
    char *v4;  // [bp-0x38]
    unsigned int v5;  // [bp-0x34]
    unsigned int v6;  // [bp-0x30]
    unsigned int v7;  // [bp-0x2c]
    unsigned int v8;  // [bp-0x28]
    struct_0 *v9;  // [bp-0x24], Other Possible Types: char
    char v10;  // [bp-0x20]
    struct_0 *v11;  // [bp-0x1c]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    char v14;  // [bp-0x4]

    v8 = v15;
    v7 = v16;
    v6 = v17;
    v5 = v18;
    v4 = &v9;
    v3 = &v14;
    v2 = v19;
    v20 = _ccall(6, &/* unsupported instruction */, 32, 0);
    v1 = v20 | 0x202 | v21 * 0x200000 & 0x200000 | v22 * 0x40000 & 0x40000;
    i = 0;
    for (v9 = NULL; g_41f018(i, &v10, 28) == 28; i += v12)
    {
        if (v13 == 0x1000 && v11 && v9 != v11)
        {
            v9 = v11;
            if (!a2 && v11 >= 0x80000000)
                return v0;
            if (g_41efe8(v11, &v10, 2))
                sub_411ca4(v11, a0, a1);
        }
    }
    return v0;
}
```

## `sub_00411dac` `0x00411dac`

_10 bytes. (leaf/helper — see body)_

```c
int sub_411dac(void)
{
    unsigned int v1;  // eax
    unsigned int v2;  // edx

    sub_411d24(v1, v2, 1);
    return;
}
```

## `sub_00411db6` `0x00411db6`

_2 bytes. (leaf/helper — see body)_

```c
void sub_411db6(void)
{
    sub_411db8();
    return;
}
```

## `sub_00411db8` `0x00411db8`

_28 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_41efc4;
extern struct_0 *g_41f01c;

unsigned int sub_411db8(unsigned int a0)
{
    unsigned int v0;  // [bp-0xc]
    char v1;  // [bp+0x0]

    g_41f01c(a0, &v1);
    v0 = 0;
    g_41efc4(&v0, 0);
    return 0;
}
```

## `sub_00411dd4` `0x00411dd4`

_35 bytes. (leaf/helper — see body)_

```c
int sub_411dd4(void)
{
    int v0;  // [bp-0x4]

    sub_40d900();
    if (!sub_40a658(v0))
        return 0;
    return sub_411978();
}
```

## `sub_00411df7` `0x00411df7`

_1 bytes. (leaf/helper — see body)_

```c
void sub_411df7(void)
{
    sub_411df8();
    return;
}
```

## `sub_00411df8` `0x00411df8`

_88 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned int field_28;
} struct_0;

int sub_411df8(void)
{
    int v6;  // eax
    int v7;  // ecx
    struct_0 *v8;  // eax
    unsigned int v9;  // eax
    int v0;  // [bp-0x14]
    int v1;  // [bp-0x10]
    int v2;  // [bp-0xc]
    int v3;  // [bp-0x8]
    int v4;  // [bp-0x4]

    v6 = sub_40d900();
    v8 = sub_40a658(v7, v1, v2, v3, v4);
    if (!v8)
        return;
    v0 = _INSERT(v7, 0, sub_40eb40());
    if (!(char)sub_40ec20(v0))
        return;
    v8->field_28 = v9 - v6;
    if (!(char)v0)
        return;
    sub_40ecb0();
    return;
}
```

## `sub_00411e50` `0x00411e50`

_526 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_41f03c;
extern unsigned int g_41f040;
extern unsigned int g_41f044;
extern int g_41f048;
extern unsigned int g_41f055;
extern unsigned int g_41f05a;
extern int g_41f07c;
extern unsigned int g_41f093;
extern char g_41f097;
extern unsigned int g_41f0b4;
extern unsigned int g_41f0b9;
extern int g_420ae4;
extern int g_420ae8;

int sub_411e50(void)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned int idx[5];  // ebx
    unsigned int v20;  // edi
    unsigned int v21;  // edi
    unsigned int v22;  // edx
    unsigned int v23;  // edi
    unsigned int v24;  // edx
    unsigned int v25;  // eax
    int v26;  // eax
    unsigned long v28;  // 4118
    unsigned short v11;  // fs
    unsigned long v12;  // 4183
    unsigned int v13;  // 4120
    unsigned long v14;  // 4187
    int v15;  // edi
    int v16;  // esi
    int v17;  // ebx
    HANDLE v18;  // esi
    unsigned int v0;  // [bp-0x70]
    unsigned int v1;  // [bp-0x68]
    unsigned int v2;  // [bp-0x4c]
    unsigned int v3;  // [bp-0x34]
    unsigned int v4;  // [bp-0x30]
    unsigned int v5;  // [bp-0x2c]
    char v6;  // [bp-0xd]
    char v7;  // [bp-0x4]

    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v13 = *((int *)v12);
    v5 = *((int *)v12);
    v14 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v14) = &v5;
    if (g_41f044 < 0x80000000)
    {
        sub_409eac(v13, sub_412067, &v7, v15, v16, v17, 0);
        v18 = CreateFileMappingA(0xffffffff, NULL, PAGE_READWRITE, 0, 20, sub_403e78());
        if (v18)
        {
            v6 = GetLastError() != ERROR_ALREADY_EXISTS;
            idx = (unsigned int [5])MapViewOfFile(v18, FILE_MAP_ALL_ACCESS, 0, 0, NULL);
            if (idx)
            {
                v20 = 50;
                do
                {
                    v21 = v20;
                    if (v6)
                        break;
                    v4 = idx[1];
                    v3 = idx[0];
                    v22 = *((int *)4);
                    if (*((int *)4) == idx[1])
                    {
                        v22 = *((int *)NULL);
                        v4 = idx[0];
                    }
                } while (v22 != v4 && (Sleep(50), v23 = v21 - 1, v20 = v21 - 1, v21 != 1));
                if (v6)
                {
LABEL_411f22:
                    g_41f03c = sub_40ecb8(0, 0);
                    g_41f040 = sub_40ecb8(0, 0);
                    g_41f044 = sub_40ecb8(0, 0);
                    idx[2] = g_41f03c;
                    idx[3] = g_41f040;
                    idx[4] = g_41f044;
                    sub_410f64(0, 0);
                    sub_40e878();
                }
                else if (idx[1] == *((int *)4))
                {
                    if (idx[0] == *((int *)0))
                        goto LABEL_411f97;
                    goto LABEL_411f22;
                }
                else
                {
                    if (idx[1] != *((int *)4))
                        goto LABEL_411f22;
LABEL_411f97:
                    g_41f03c = idx[2];
                    g_41f040 = idx[3];
                    g_41f044 = idx[4];
                }
                UnmapViewOfFile(idx);
            }
            CloseHandle(v18);
        }
    }
    if (g_41f044 >= 0x80000000)
    {
        g_41f055 = v24;
        g_41f05a = v25;
        v2 = 0;
        v26 = sub_411dd4();
        sub_41708c(4, &g_420ae4, &g_41f048, v26);
        sub_40d994(4, &g_420ae4, &g_41f048, v26);
        g_41f093 = sub_411978() - &g_41f097;
        g_41f0b4 = v24;
        g_41f0b9 = v25;
        sub_40d994(0);
        v0 = 4;
        sub_41708c(4, &g_420ae8, &g_41f07c, sub_411978(0));
    }
    v28 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v28) = v0;
    v1 = sub_41206e;
    sub_41205e();
    return;
}
```

## `sub_0041205e` `0x0041205e`

_9 bytes. (leaf/helper — see body)_

```c
int sub_41205e(void)
{
    return sub_403a10();
}
```

## `sub_00412067` `0x00412067`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_412067(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041206c` `0x0041206c`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41206c(void)
{
    return sub_41205e();
}
```

## `sub_0041206e` `0x0041206e`

_7 bytes. (leaf/helper — see body)_

```c
void sub_41206e(unsigned int a0, unsigned int a1)
{
    return;
}
```

