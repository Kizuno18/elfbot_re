# elfbot.dll decompiled — loader 0x00409ee0..0x0040b0b4

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_00409ee0` `0x00409ee0`

_86 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned short field_0;
} struct_0;

int sub_409ee0(void)
{
    struct_0 **v4;  // ecx
    unsigned short *iter;  // ebx
    int i;  // eax
    unsigned int v7;  // edx
    unsigned int v8;  // eax
    int v0;  // [bp-0xc]
    int v1;  // [bp-0x8]
    int v2;  // [bp-0x4]

    sub_403c80(v4, v0, v1, v2);
    sub_403f60(v4, v0, v1, v2);
    iter = &*(v4)->field_0;
    i = sub_403c80();
    if (i > 0)
    {
        v7 = 1;
        do
        {
            *(iter) = *((char *)(v8 + v7 - 1));
            iter += 1;
            v7 += 1;
            i -= 1;
        } while (i != 1);
    }
    if (*((char *)&v4))
        sub_403c88();
    return;
}
```

## `sub_00409f44` `0x00409f44`

_65 bytes. (leaf/helper — see body)_

```c
int sub_409f44(void)
{
    PWSTR v6;  // eax
    int v7;  // esi
    unsigned int v8;  // ebx
    int i;  // esi
    int v10;  // eax
    int v11;  // esi
    int v0;  // [bp-0x10]
    int v1;  // [bp-0xc]
    int v2;  // [bp-0x8]
    int v3;  // [bp-0x4]
    int v4;  // [bp+0x0]

    lstrlenW(v6);
    sub_403f60(v0, v1, v2, v3, v4);
    v7 = sub_403c80();
    if (v7 <= 0)
        return;
    v8 = 1;
    do
    {
        i = v7;
        v10 = sub_403ed0();
        *((char *)(v10 + v8 - 1)) = (char)v6[1 + v8];
        v8 += 1;
        v11 = i - 1;
        v7 = v11;
    } while (i != 1);
    return;
}
```

## `sub_00409f85` `0x00409f85`

_81 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420898;

int sub_409f85(void)
{
    unsigned long v3;  // ldt
    unsigned long v4;  // gdt
    unsigned short v5;  // fs
    unsigned long v6;  // 4160
    unsigned int v7;  // 4106
    unsigned long v8;  // 4164
    unsigned int v9;  // 4118
    unsigned int v10;  // 4167
    unsigned long v11;  // 4118
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0x8]

    v6 = _ccall(v3, v4, (unsigned int)v5, 0);
    v7 = *((int *)v6);
    v0 = *((int *)v6);
    v8 = _ccall(v3, v4, (unsigned int)v5, 0);
    *((unsigned int **)v8) = &v0;
    v9 = g_420898;
    g_420898 = g_420898 + 1;
    v10 = _ccall(4, 18, v9 + 1, 0, 0);
    if ((char)v10)
    {
        sub_403a10(v7, sub_409fd7, &/* unsupported instruction */, /* unsupported instruction */);
        sub_403a10();
        sub_403a10();
        sub_403a10();
    }
    v11 = _ccall(v3, v4, (unsigned int)v5, 0);
    *((unsigned int *)v11) = v7;
    v1 = sub_409fde;
    return sub_409fd6(/* unsupported instruction */);
}
```

## `sub_00409fd6` `0x00409fd6`

_1 bytes. (leaf/helper — see body)_

```c
void sub_409fd6(void)
{
    return;
}
```

## `sub_00409fd7` `0x00409fd7`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_409fd7(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00409fdc` `0x00409fdc`

_2 bytes. (leaf/helper — see body)_

```c
void sub_409fdc(void)
{
    sub_409fd6();
    return;
}
```

## `sub_00409fde` `0x00409fde`

_2 bytes. (leaf/helper — see body)_

```c
void sub_409fde(unsigned int a0)
{
    return;
}
```

## `sub_00409fe0` `0x00409fe0`

_8 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420898;

void sub_409fe0(void)
{
    g_420898 = g_420898 - 1;
    return;
}
```

## `sub_0040a0d8` `0x0040a0d8`

_869 bytes. refs "kernel32.dll", "GetNativeSystemInfo"_

```c
extern char g_41e4d8;
extern unsigned int g_4208a0;
extern unsigned int g_4208a4;
extern unsigned int g_4208a8;
extern int g_4208ac;
extern char g_4208b0;
extern char g_4208b1;
extern char g_4208b2;
extern char g_4208b3;
extern char g_4208b4;
extern char g_4208b5;
extern unsigned int g_4208b8;
extern int g_4208bc;

int sub_40a0d8(void)
{
    unsigned int v16;  // ebx
    unsigned int v17;  // esi
    unsigned int v18;  // edi
    unsigned int i;  // edi
    void* v20;  // eax
    char *iter;  // edx
    unsigned int v23;  // eax
    unsigned int *v25;  // edi
    unsigned int v0;  // [bp-0x1e0]
    unsigned int v1;  // [bp-0x1dc]
    unsigned int v2;  // [bp-0x1d8]
    unsigned int v3;  // [bp-0x1d4]
    unsigned int v4;  // [bp-0x1d0]
    char v5;  // [bp-0x1cc]
    unsigned int v7;  // [bp-0x14c]
    unsigned short v8;  // [bp-0x38]
    unsigned short v9;  // [bp-0x34]
    char v10;  // [bp-0x32]
    char v11;  // [bp-0x30]
    unsigned int v12;  // [bp-0xc]
    unsigned int v13;  // [bp-0x8]
    unsigned int v14;  // [bp-0x4]

    v14 = v16;
    v13 = v17;
    v12 = v18;
    if (g_41e4d8 && g_4208bc)
    {
        sub_40421c();
        return;
    }
    g_41e4d8 = 1;
    if (!(GetVersion() & 0x80000000))
    {
        sub_4054b4();
        v7 = _INSERT(v7 CONCAT 0, 0, 284);
        if (!GetVersionExW(&v7))
        {
            v7 = 276;
            GetVersionExW(&v7);
        }
        sub_402628();
        i = 128;
        v20 = &v7 + 5;
        iter = &v5;
        do
        {
            *(iter) = *((char *)v20);
            iter += 1;
            v20 += 2;
            i -= 1;
        } while (i != 1);
    }
    else
    {
        sub_4054b4();
        v0 = 148;
        sub_40532c(&v0);
    }
    g_4208a0 = v1;
    g_4208a4 = v2;
    sub_403c54(v0, v1);
    g_4208b0 = v4 == 1;
    g_4208b2 = v4 == 2;
    if (g_4208b0)
        g_4208a8 = (unsigned short)v3;
    else
        g_4208a8 = v3;
    g_4208b4 = 0;
    g_4208b8 = 0;
    if (g_4208b0)
    {
        if (g_4208a0 >= 4)
        {
            if (g_4208a0 == 4)
            {
                if (g_4208a4 >= 10)
                {
                    if (g_4208a4 != 10)
                    {
                        if (g_4208a4 - 11 < 80)
                            g_4208b4 = 5;
                        else
                            g_4208b4 = 6;
                    }
                    else
                    {
                        if (g_4208a8 > 2700)
                        {
                            g_4208b4 = 5;
                        }
                        else
                        {
                            if (g_4208a8 > 2000)
                                g_4208b4 = 4;
                            else
                                g_4208b4 = 3;
                        }
                    }
                }
                else
                {
                    if (g_4208a8 > 1000)
                        g_4208b4 = 2;
                    else
                        g_4208b4 = 1;
                }
            }
            else
            {
                g_4208b4 = 6;
            }
        }
        g_4208b1 = g_4208b4;
        g_4208b3 = 0;
    }
    else if (g_4208b2)
    {
        v23 = g_4208a0 - 4;
        if (g_4208a0 < 4)
        {
            g_4208b4 = 7;
        }
        else if (g_4208a0 == 4)
        {
            g_4208b4 = 8;
        }
        else if (v23 != 1)
        {
            if (v23 != 2)
            {
                g_4208b4 = 13;
            }
            else if (g_4208a4 < 1)
            {
                g_4208b4 = 12;
            }
            else
            {
                g_4208b4 = 13;
            }
        }
        else
        {
            if (g_4208a4 < 1)
            {
                g_4208b4 = 9;
            }
            else if (g_4208a4 == 1)
            {
                g_4208b4 = 10;
            }
            else if (v10 == 1)
            {
                g_4208b4 = 10;
            }
            else
            {
                g_4208b4 = 11;
            }
        }
        g_4208b1 = 0;
        g_4208b3 = g_4208b4;
        if (v7 >= 284)
        {
            g_4208b8 = v8;
        }
        else if (sub_403c80() >= 14)
        {
            sub_403ed0(sub_403c80() - 13);
            g_4208b8 = sub_409c00();
        }
        v25 = GetProcAddress(sub_4052bc("kernel32.dll"), "GetNativeSystemInfo");
        if (v25)
        {
            sub_4054b4();
            v25(&v11);
            g_4208b5 = v9 == 9;
        }
    }
    sub_403be8();
    if (!g_4208b2)
    {
        sub_40421c();
        return;
    }
    if (GetSystemMetrics(SM_SERVERR2))
        sub_403c88();
    if (GetSystemMetrics(SM_TABLETPC))
        sub_403c88();
    if (GetSystemMetrics(SM_STARTER))
        sub_403c88();
    if (g_4208b4 < 12 && GetSystemMetrics(SM_MEDIACENTER))
        sub_403c88();
    if (g_4208b5)
        sub_403c88();
    if (g_4208ac)
        sub_403d40(g_4208ac, " ", g_4208bc);
    sub_40421c();
    return;
}
```

## `sub_0040a4d0` `0x0040a4d0`

_23 bytes. (leaf/helper — see body)_

```c
int sub_40a4d0(void)
{
    unsigned int idx;  // edx
    unsigned int v3;  // 4098
    unsigned int v4;  // cc_op
    unsigned int v5;  // cc_dep1
    unsigned int v6;  // cc_dep2
    unsigned int v7;  // cc_ndep
    unsigned int v8;  // 4112
    unsigned int v9;  // ecx
    unsigned int v10;  // 4122
    unsigned int v11;  // 4128
    char v0;  // [bp+0x0]

    v3 = *((int *)&(&v0)[2 * idx]);
    v8 = _ccall(v4, v5, v6, v7);
    *((unsigned int *)&(&v0)[2 * idx]) = *((int *)&(&v0)[2 * idx]) + v9 + (v8 & 1);
    v10 = _ccall(9, v3, v9 ^ v8 & 1, v8 & 1);
    v11 = _ccall(2, 21, /* unsupported instruction */ - 1, 0, v10);
    /* unsupported instruction */
    /* unsupported instruction */
}
```

## `sub_0040a534` `0x0040a534`

_9 bytes. (leaf/helper — see body)_

```c
int sub_40a534(void)
{
}
```

## `sub_0040a54c` `0x0040a54c`

_238 bytes. (leaf/helper — see body)_

```c
typedef struct MEMORY_BASIC_INFORMATION {
    void* BaseAddress;
    void* AllocationBase;
    enum PAGE_PROTECTION_FLAGS AllocationProtect;
    UIntPtr RegionSize;
    enum VIRTUAL_ALLOCATION_TYPE State;
    enum PAGE_PROTECTION_FLAGS Protect;
    enum PAGE_TYPE Type;
} MEMORY_BASIC_INFORMATION;

int sub_40a54c(void)
{
    unsigned int v12;  // ebx
    unsigned int v13;  // esi
    unsigned int *v23;  // edx
    unsigned long v24;  // 4118
    unsigned int v14;  // edi
    unsigned long v15;  // ldt
    unsigned long v16;  // gdt
    unsigned short v17;  // fs
    unsigned long v18;  // 4160
    unsigned long v19;  // 4169
    void* v20;  // eax
    char v21;  // al
    unsigned int v0;  // [bp-0x34c]
    unsigned int v1;  // [bp-0x348]
    char *v2;  // [bp-0x344], Other Possible Types: unsigned int
    unsigned int v3;  // [bp-0x340]
    unsigned int v4;  // [bp-0x33c]
    unsigned int v5;  // [bp-0x338]
    unsigned int v6;  // [bp-0x334]
    Char v7[523];  // [bp-0x330]
    char v8;  // [bp-0x125]
    MEMORY_BASIC_INFORMATION v9;  // [bp-0x20]
    char v10;  // [bp-0x4]

    v5 = v12;
    v4 = v13;
    v3 = v14;
    v6 = 0;
    v2 = &v10;
    v1 = sub_40a646;
    v18 = _ccall(v15, v16, (unsigned int)v17, 0);
    v0 = *((int *)v18);
    v19 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int **)v19) = &v0;
    if (VirtualQuery(v20, &v9, 0x1c) != 0x1c || v9.State != 0x1000 || !v9.AllocationBase)
        v21 = 0;
    else
        v21 = 1;
    if (v21 && (!(GetVersion() & 0x80000000) ? GetModuleFileNameW(v9.AllocationBase, v7, 260) : sub_4052ac(v9.AllocationBase, &v8, 260)))
    {
        *(v23) = v9.AllocationBase;
        if (!(GetVersion() & 0x80000000))
        {
            sub_409f44();
            sub_403a64();
        }
        else
        {
            sub_403c54();
        }
    }
    v24 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int *)v24) = v0;
    v2 = sub_40a64d;
    sub_40a63a();
    return;
}
```

## `sub_0040a63a` `0x0040a63a`

_12 bytes. (leaf/helper — see body)_

```c
int sub_40a63a(void)
{
    return sub_403a10();
}
```

## `sub_0040a646` `0x0040a646`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40a646(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0040a64b` `0x0040a64b`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40a64b(void)
{
    return sub_40a63a();
}
```

## `sub_0040a64d` `0x0040a64d`

_9 bytes. (leaf/helper — see body)_

```c
int sub_40a64d(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // ebx

    return v0;
}
```

## `sub_0040a656` `0x0040a656`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40a656(void)
{
    sub_40a658();
    return;
}
```

## `sub_0040a658` `0x0040a658`

_79 bytes. (leaf/helper — see body)_

```c
int sub_40a658(void)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4148
    unsigned long v9;  // 4157
    unsigned long v11;  // 4116
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    char *v2;  // [bp-0x14]
    char v3;  // [bp-0x4]

    v2 = &v3;
    v1 = sub_40a6a0;
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v0 = *((int *)v8);
    v9 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v9) = &v0;
    v11 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v11) = v0;
    return;
}
```

## `sub_0040a6a0` `0x0040a6a0`

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

unsigned int sub_40a6a0(int a0)
{
    struct_1 *v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x8]

    return sub_4030c0(v0, a0, v1);
}
```

## `sub_0040a6a5` `0x0040a6a5`

_7 bytes. (leaf/helper — see body)_

```c
void sub_40a6a5(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int *a10)
{
    unsigned int v0;  // [bp+0x0]

    sub_4034ec(v0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10);
}
```

## `sub_0040a6b3` `0x0040a6b3`

_1 bytes. (leaf/helper — see body)_

```c
int sub_40a6b3(void)
{
    sub_40a6b4();
    return;
}
```

## `sub_0040a6b4` `0x0040a6b4`

_55 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned short field_18;
} struct_0;

int sub_40a6b4(void)
{
    struct_0 *v3;  // eax
    int v0;  // [bp-0x8]
    int v1;  // [bp-0x4]

    v3 = sub_40a658(v0, v1);
    if (!v3)
    {
        return;
    }
    else if (v3->field_18 == 523)
    {
        return;
    }
    else
    {
        return;
    }
}
```

## `sub_0040a6eb` `0x0040a6eb`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40a6eb(void)
{
    sub_40a6ec();
    return;
}
```

## `sub_0040a6ec` `0x0040a6ec`

_8 bytes. (leaf/helper — see body)_

```c
void sub_40a6ec(void)
{
    sub_40a6b4();
    return;
}
```

## `sub_0040a6f4` `0x0040a6f4`

_172 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned short field_18;
    char padding_1a[94];
    unsigned int field_78;
    unsigned int field_7c;
    char padding_80[8];
    unsigned int field_88;
    unsigned int field_8c;
} struct_0;

int sub_40a6f4(void)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned int v16;  // edx
    char v17[2];  // esi
    char v18[2];  // ebx
    char v19[2];  // ebx
    unsigned long v21;  // 4118
    unsigned short v8;  // fs
    unsigned long v9;  // 4152
    unsigned int v10;  // 4117
    unsigned long v11;  // 4161
    int v12;  // esi
    int v13;  // ebx
    struct_0 *index;  // eax
    struct_0 *idx;  // eax
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]
    char v4;  // [bp-0x4]

    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v10 = *((int *)v9);
    v0 = *((int *)v9);
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v0;
    index = sub_40a658(v10, sub_40a7ae, &v4, v12, v13, 0, 0);
    if (index->field_18 == 523)
    {
        idx = &index->field_18;
        v2 = *((int *)&idx->padding_1a[86]);
        v3 = *((int *)&idx->padding_1a[90]);
    }
    else
    {
        v2 = index->field_78;
        v3 = index->field_7c;
    }
    if (v16 >= v2 && v16 < v2 + v3)
    {
        sub_403be8();
        v17 = sub_403e78();
        v18 = v17;
        do
        {
            v18 = &v18[1];
        } while (v18[0] != 46);
        v19[0] = 0;
        sub_403be8(sub_4052c4(v17));
        sub_40a918();
    }
    v21 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v21) = v10;
    v1 = sub_40a7b5;
    sub_40a7a0();
    return;
}
```

## `sub_0040a7a0` `0x0040a7a0`

_14 bytes. (leaf/helper — see body)_

```c
int sub_40a7a0(void)
{
    return sub_403a34();
}
```

## `sub_0040a7ae` `0x0040a7ae`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40a7ae(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0040a7b3` `0x0040a7b3`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40a7b3(void)
{
    return sub_40a7a0();
}
```

## `sub_0040a7b5` `0x0040a7b5`

_8 bytes. (leaf/helper — see body)_

```c
int sub_40a7b5(unsigned int a0)
{
    unsigned int v0;  // ebx

    return v0;
}
```

## `sub_0040a7bd` `0x0040a7bd`

_3 bytes. (leaf/helper — see body)_

```c
int sub_40a7bd(void)
{
    sub_40a7c0();
    return;
}
```

## `sub_0040a7c0` `0x0040a7c0`

_103 bytes. (leaf/helper — see body)_

```c
int sub_40a7c0(void)
{
    unsigned short v1[13];  // eax
    unsigned short v2[13];  // esi
    unsigned int v3;  // ebp
    unsigned int v4;  // ebp
    unsigned int v5;  // ecx
    unsigned int v6;  // ebp
    unsigned int v7;  // edx

    v2 = (v1[12] == 523 ? (unsigned short [13])&v1[10 + 2] : (unsigned short [13])&v1[9 + 7]);
    v3 = v1[3] - 1;
    if (v3 < 0)
        return;
    v4 = v3 + 1;
    v5 = 0;
    while (true)
    {
        v6 = v4;
        if (v7 >= *((int *)(12 + (char *)v2 + 40 * v5)) && (v5 == v1[3] - 1 || v7 < *((int *)(52 + (char *)v2 + 40 * v5))))
            break;
        v5 += 1;
        v4 = v6 - 1;
        if (v6 == 1)
            return;
    }
    return;
}
```

## `sub_0040a827` `0x0040a827`

_1 bytes. (leaf/helper — see body)_

```c
int sub_40a827(void)
{
    sub_40a828();
    return;
}
```

## `sub_0040a828` `0x0040a828`

_19 bytes. (leaf/helper — see body)_

```c
int sub_40a828(void)
{
    return;
}
```

## `sub_0040a83b` `0x0040a83b`

_1 bytes. (leaf/helper — see body)_

```c
int sub_40a83b(void)
{
    sub_40a83c();
    return;
}
```

## `sub_0040a83c` `0x0040a83c`

_218 bytes. calls CreateFileA_

```c
int sub_40a83c(void)
{
    unsigned int v1;  // ebx
    LPArray v2;  // eax
    HANDLE v3;  // eax
    HANDLE v5;  // ebx

    if (!(GetVersion() & 0x80000000))
    {
        v1 = sub_40536c(0x40, 522);
        GetModuleFileNameW(v2, v1, 260);
        v3 = CreateFileW(v1, 0x80000000, FILE_SHARE_READ, NULL, OPEN_EXISTING, SECURITY_ANONYMOUS, NULL);
    }
    else
    {
        v1 = sub_40536c(0x40, 261);
        sub_4052ac(v2, v1, 260);
        v3 = CreateFileA(v1, 0x80000000, FILE_SHARE_READ, NULL, OPEN_EXISTING, SECURITY_ANONYMOUS, NULL);
    }
    LocalFree(v1);
    if (v3 == 0xffffffff)
        return;
    v5 = (!(GetVersion() & 0x80000000) ? CreateFileMappingW(v3, NULL, PAGE_READONLY, 0, 0, NULL) : CreateFileMappingA(v3, NULL, PAGE_READONLY, 0, 0, NULL));
    if (v5)
    {
        MapViewOfFile(v5, FILE_MAP_READ, 0, 0, NULL);
        CloseHandle(v5);
    }
    CloseHandle(v3);
    return;
}
```

## `sub_0040a916` `0x0040a916`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40a916(void)
{
    sub_40a918();
    return;
}
```

## `sub_0040a918` `0x0040a918`

_485 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned short field_18;
    char padding_1a[94];
    unsigned int field_78;
    char padding_7c[12];
    unsigned int field_88;
} struct_0;

typedef struct struct_1 {
    char padding_0[24];
    int field_18;
    char padding_1c[8];
    unsigned int field_24;
} struct_1;

typedef struct struct_4 {
    char padding_0[24];
    unsigned short field_18;
} struct_4;

typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

extern struct_2 *g_41e4d0;
extern struct_2 *g_41e4d4;

int sub_40a918(void)
{
    int v13;  // edi
    HMODULE v14;  // eax
    char v23;  // cl
    unsigned long v24;  // ldt
    unsigned long v25;  // gdt
    unsigned short v26;  // fs
    unsigned long v27;  // 4128
    unsigned int v28;  // 4103
    unsigned long v29;  // 4137
    unsigned int v30[9];  // esi
    unsigned long v31;  // 4116
    struct_4 *v32;  // ebx
    int v15;  // edi
    int v16;  // esi
    int v17;  // ebx
    struct_0 *v18;  // ebx
    struct_1 *idx;  // esi
    unsigned int v20;  // eax
    PSTR v21;  // edx
    unsigned short v22;  // di
    unsigned int v0;  // [bp-0x50]
    unsigned int iter;  // [bp-0x38], Other Possible Types: int
    int v2;  // [bp-0x34]
    char v3;  // [bp-0x2d]
    int v4;  // [bp-0x2c]
    unsigned int v5;  // [bp-0x28]
    unsigned int v6;  // [bp-0x24]
    unsigned int v7;  // [bp-0x20]
    unsigned int v8;  // [bp-0x1c]
    int v9;  // [bp-0x18], Other Possible Types: unsigned int
    unsigned int index;  // [bp-0x14]
    char v11;  // [bp-0x4]

    v13 = 0;
    if (!v14)
        return;
    v18 = sub_40a658(v15, v16, v17);
    if (v18)
    {
        v2 = sub_40a828();
        v6 = (v18->field_18 == 523 ? v18->field_88 : v18->field_78);
        idx = (char *)v14 + v6;
        if (idx)
        {
            v20 = idx->field_18 - 1;
            if (v20 >= NULL)
            {
                iter = v20 + 1;
                index = 0;
                do
                {
                    if (!lstrcmpA(*((int *)(*((int *)&idx->padding_1c[4]) + (char *)v14 + 4 * index)) + (char *)v14, v21))
                    {
                        v22 = *((short *)(idx->field_24 + (char *)v14 + 2 * index));
                        v9 = *((int *)(*((int *)&idx->padding_1c[0]) + (char *)v14 + 4 * v22));
                        if (v23 || v9 > v2)
                        {
                            v4 = (char *)v14 + v9;
                            if (g_41e4d0 && (char)g_41e4d0())
                            {
                                v13 = v4;
                                break;
                            }
                            else
                            {
                                v5 = (!g_41e4d4 ? NULL : g_41e4d4());
                                v3 = !v5;
                                if (!v5)
                                    v5 = sub_40a83c();
                                if (v5)
                                {
                                    v27 = _ccall(v24, v25, (unsigned int)v26, 0);
                                    v28 = *((int *)v27);
                                    v0 = *((int *)v27);
                                    v29 = _ccall(v24, v25, (unsigned int)v26, 0);
                                    *((unsigned int **)v29) = &v0;
                                    v8 = *((int *)&idx->padding_1c[4]);
                                    v7 = *((int *)&idx->padding_1c[0]);
                                    v30 = sub_40a7c0(v28, sub_40aa9c, &v11) + v5;
                                    if (v30[8] == v8 && v30[7] == v7)
                                        v9 = *((int *)(sub_40a7c0() + v5 + v22 * 4));
                                    v31 = _ccall(v24, v25, (unsigned int)v26, 0);
                                    *((unsigned int *)v31) = v28;
                                    if (v3)
                                        UnmapViewOfFile(v5);
                                }
                            }
                        }
                        v13 = sub_40a6f4();
                        break;
                    }
                } while ((index += 1, iter -= 1, iter = (int)iter, iter != 1));
            }
        }
    }
    if (v13)
        return;
    v32 = sub_40a658();
    if (!v32)
        return;
    if (v32->field_18 == 523)
        return;
    GetProcAddress(v14, sub_403e78());
    return;
}
```

## `sub_0040aa9c` `0x0040aa9c`

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

unsigned int sub_40aa9c(int a0)
{
    struct_1 *v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x8]

    return sub_4030c0(v0, a0, v1);
}
```

## `sub_0040aaa1` `0x0040aaa1`

_5 bytes. (leaf/helper — see body)_

```c
void sub_40aaa1(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int *a10)
{
    unsigned int v0;  // [bp+0x0]

    sub_4034ec(v0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10);
}
```

## `sub_0040ab07` `0x0040ab07`

_1 bytes. (leaf/helper — see body)_

```c
int sub_40ab07(void)
{
    sub_40ab08();
    return;
}
```

## `sub_0040ab08` `0x0040ab08`

_97 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    int field_14;
    char padding_18[4];
    unsigned int field_1c;
} struct_0;

typedef struct struct_1 {
    char padding_0[24];
    unsigned short field_18;
} struct_1;

int sub_40ab08(void)
{
    int v1;  // esi
    struct_0 *v2;  // eax
    PSTR v3;  // edx
    int v4;  // ebx
    HMODULE v5;  // eax
    struct_1 *v6;  // eax

    v1 = 0;
    v2 = (unsigned int)sub_40a6ec();
    if (v2)
    {
        v4 = &v3[-1 * v2->field_10];
        if (v4 >= 0 && v4 < v2->field_14 && *((int *)(v2->field_1c + (char *)v5 + 4 * v4)))
            v1 = sub_40a6f4();
    }
    if (v1)
        return;
    v6 = sub_40a658();
    if (!v6)
        return;
    if (v6->field_18 == 523)
        return;
    GetProcAddress(v5, v3);
    return;
}
```

## `sub_0040ab69` `0x0040ab69`

_3 bytes. (leaf/helper — see body)_

```c
int sub_40ab69(void)
{
    sub_40ab6c();
    return;
}
```

## `sub_0040ab6c` `0x0040ab6c`

_263 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    int field_14;
    int field_18;
    unsigned int field_1c;
    char padding_20[4];
    unsigned int field_24;
} struct_0;

int sub_40ab6c(void)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    struct_0 *idx;  // esi
    unsigned int v18;  // eax
    int v19;  // eax
    int v20;  // eax
    unsigned int v21;  // eax
    unsigned int v22;  // edx
    unsigned int v23;  // eax
    unsigned int v24;  // eax
    int v25;  // eax
    unsigned int v26;  // edi
    unsigned short v9;  // fs
    int v27;  // eax
    unsigned int v28;  // eax
    char v29;  // cl
    unsigned long v30;  // 4118
    unsigned long v10;  // 4161
    unsigned int v11;  // 4120
    unsigned long v12;  // 4170
    int v13;  // edi
    int v14;  // esi
    int v15;  // ebx
    struct_0 *v16;  // eax
    unsigned int v0;  // [bp-0x3c]
    unsigned int v1;  // [bp-0x34]
    unsigned int v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0xc]
    char v5;  // [bp-0x4]
    unsigned int *v6;  // [bp+0x4]

    v3 = 0;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v11 = *((int *)v10);
    v2 = *((int *)v10);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v12) = &v2;
    sub_403a10(v11, sub_40ac81, &v5, v13, v14, v15, 0, 0);
    v16 = (unsigned int)sub_40a6ec();
    if (v16)
    {
        idx = v16;
        v18 = idx->field_14 - 1;
        if (v18 >= NULL)
        {
            v19 = v18 + 1;
            v4 = 0;
            do
            {
                v20 = v19;
                if (*((int *)(idx->field_1c + v21 + v4 * 4)) + v21 == v22)
                {
                    v24 = idx->field_18 - 1;
                    if (v24 >= NULL)
                    {
                        v25 = v24 + 1;
                        v26 = 0;
                        do
                        {
                            v27 = v25;
                            if (*((short *)(idx->field_24 + v21 + v26 * 2)) == v4)
                            {
                                sub_403be8();
                                break;
                            }
                        } while ((v26 += 1, v28 = v27 - 1, v25 = (int)(v27 - 1), v27 != 1));
                    }
                    if (!*(v6))
                    {
                        sub_409b08(&v3);
                        sub_403ccc(&v3);
                        break;
                    }
                }
            } while ((v4 += 1, v23 = v20 - 1, v19 = (int)(v20 - 1), v20 != 1));
        }
    }
    if (v29 && (char)sub_40acac())
    {
        v0 = *(v6);
        sub_403d40(*(v6), ".", 0);
    }
    v30 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v30) = v0;
    v1 = sub_40ac88;
    sub_40ac73();
    return;
}
```

## `sub_0040ac73` `0x0040ac73`

_14 bytes. (leaf/helper — see body)_

```c
int sub_40ac73(void)
{
    return sub_403a34();
}
```

## `sub_0040ac81` `0x0040ac81`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40ac81(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0040ac86` `0x0040ac86`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40ac86(void)
{
    return sub_40ac73();
}
```

## `sub_0040ac88` `0x0040ac88`

_9 bytes. (leaf/helper — see body)_

```c
void sub_40ac88(unsigned int a0, unsigned int a1)
{
    return;
}
```

## `sub_0040acac` `0x0040acac`

_675 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[1];
    char field_1;
    char field_2;
} struct_0;

int sub_40acac(void)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned int v19;  // cc_op
    unsigned int v20;  // cc_dep1
    unsigned int v21;  // cc_dep2
    unsigned int v22;  // cc_ndep
    unsigned int v23;  // 4103
    unsigned int v24;  // 4109
    int v25;  // esi
    int v26;  // edi
    int v27;  // edi
    int v28;  // esi
    unsigned short v11;  // fs
    int v29;  // edi
    int v30;  // edi
    int v31;  // esi
    int v32;  // edi
    unsigned int v33;  // edi
    unsigned int i;  // edi
    unsigned int *v35;  // edx
    unsigned int v36;  // edi
    char v37;  // al
    int v38;  // eax
    unsigned long v12;  // 4161
    int v39;  // eax
    int v40;  // eax
    unsigned long v41;  // 4118
    unsigned int v13;  // 4120
    unsigned long v14;  // 4170
    int v15;  // edi
    int v16;  // esi
    int v17;  // ebx
    struct_0 **v18;  // eax
    unsigned int v0;  // [bp-0x3c]
    unsigned int v1;  // [bp-0x34]
    unsigned int v2;  // [bp-0x1c]
    char v3;  // [bp-0x12]
    char v4;  // [bp-0x11]
    int v5;  // [bp-0x10]
    char v6;  // [bp-0x9]
    char v7;  // [bp-0x4]

    v2 = 0;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v13 = *((int *)v12);
    v1 = *((int *)v12);
    v14 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v14) = &v1;
    v6 = 0;
    sub_403a10(v13, sub_40af5d, &v7, v15, v16, v17, 0, 0);
    sub_4092b8(0);
    if (*(v18) && *(v18)->padding_0 == 64)
    {
        sub_403a10();
        v23 = _ccall(v19, v20, v21, v22);
        v24 = _ccall(14, 21, sub_403c80() - 1, 0, v23);
        if (!((char)v24) && *(v18)->field_1 == 37)
        {
            v25 = sub_403c80() - 1;
            if (v25 >= 3)
            {
                do
                {
                    if ((&*(v18)->field_1)[v25] == 37 && (*(v18)->padding_0)[v25] == 64)
                    {
                        sub_403ed8(&v2);
                        sub_403ccc(&v2);
                        break;
                    }
                } while ((v25 = (int)(v25 - 1), v25 != 2));
            }
        }
        v5 = 3;
        if (sub_403c80() > 6 && *(v18)->field_1 == 95 && *(v18)->field_2 == 36)
        {
            v26 = sub_403c80() - 1;
            if (v26 >= 5)
            {
                v27 = v26 - 4;
                v28 = 5;
                do
                {
                    v29 = v27;
                    if ((&*(v18)->field_1)[v28] == 36 && (*(v18)->padding_0)[v28] == 64)
                    {
                        v5 = v28 + 1;
                        break;
                    }
                } while ((v28 = (int)(v28 + 1), v30 = (int)(v29 - 1), v27 = (int)(v29 - 1), v29 != 1));
            }
        }
        v4 = 0;
        v3 = 0;
        v31 = v5;
        v32 = sub_403c80();
        if (v32 >= v31)
        {
            v33 = v32 - v31 + 1;
            do
            {
                i = v33;
                if ((&*(v18)->field_1)[v31] == 36)
                {
                    if (sub_403c80() <= v31 + 1 || (&*(v18)->field_1)[v31] != 100)
                        v37 = 0;
                    else
                        v37 = 1;
                    v4 = v37;
                    sub_403f18();
                    sub_403c88();
                    v3 = 1;
                    break;
                }
                if ((&*(v18)->field_1)[v31] == 64)
                {
                    *((char *)(sub_403ed0() + v31 - 1)) = 46;
                    if (!*(v35))
                        sub_403ed8(v35);
                }
                v31 += 1;
                v36 = i - 1;
                v33 = v36;
            } while (i != 1);
        }
        if (*(v35))
        {
            v38 = sub_403c80();
            if (v38 + 2 < sub_403c80())
            {
                sub_403c80();
                sub_403f18();
                v3 = 0;
            }
            else
            {
                sub_403a10();
            }
        }
        if (v3)
            sub_403f18();
        if (*(v18))
        {
            if (*(v18)->padding_0 == 37)
            {
                sub_403f18();
            }
            else if (*(v18)->padding_0 == 46)
            {
                *((char *)sub_403ed0()) = 64;
            }
        }
        if (*(v18))
        {
            v39 = sub_403c80();
            if ((&*(v18)->field_1)[v39] == 46)
            {
                if (v4)
                    sub_403c88();
                else
                    sub_403c88();
            }
        }
        sub_408fb4();
        if (*(v18))
        {
            v40 = sub_403c80();
            if ((&*(v18)->field_1)[v40] == 46)
                sub_403c88();
        }
        v6 = 1;
    }
    v41 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v41) = v0;
    v1 = sub_40af64;
    sub_40af4f();
    return;
}
```

## `sub_0040af4f` `0x0040af4f`

_14 bytes. (leaf/helper — see body)_

```c
int sub_40af4f(void)
{
    return sub_403a34();
}
```

## `sub_0040af5d` `0x0040af5d`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40af5d(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0040af62` `0x0040af62`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40af62(void)
{
    return sub_40af4f();
}
```

## `sub_0040af64` `0x0040af64`

_10 bytes. (leaf/helper — see body)_

```c
char sub_40af64(unsigned int a0, unsigned int a1)
{
    char v0;  // [bp+0xfffff]

    return v0;
}
```

## `sub_0040afb4` `0x0040afb4`

_25 bytes. (leaf/helper — see body)_

```c
int sub_40afb4(void)
{
    return;
}
```

## `sub_0040afcd` `0x0040afcd`

_3 bytes. (leaf/helper — see body)_

```c
int sub_40afcd(void)
{
    return sub_40afd0();
}
```

## `sub_0040afd0` `0x0040afd0`

_18 bytes. (leaf/helper — see body)_

```c
int sub_40afd0(void)
{
    return sub_408ef4();
}
```

## `sub_0040b044` `0x0040b044`

_35 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_41f460;
extern struct_0 *g_41f4a8;

unsigned int * sub_40b044(void)
{
    unsigned int *v1;  // eax

    v1 = &g_41f460->field_0;
    if (!g_41f460->field_0)
    {
        g_41f460->field_0 = sub_408ed4;
        v1 = &g_41f4a8->field_0;
        g_41f4a8->field_0 = sub_40afd0;
    }
    return v1;
}
```

## `sub_0040b067` `0x0040b067`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40b067(void)
{
    sub_40b068();
    return;
}
```

## `sub_0040b068` `0x0040b068`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_42089c;

int sub_40b068(void)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4157
    unsigned long v10;  // 4161
    unsigned int v11;  // 4117
    unsigned int v12;  // 4164
    unsigned long v13;  // 4118
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    char *v2;  // [bp-0x8], Other Possible Types: unsigned int
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v2 = &v3;
    v1 = sub_40b0b4;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v0 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v0;
    v11 = g_42089c;
    g_42089c = g_42089c + 1;
    v12 = _ccall(4, 18, v11 + 1, 0, 0);
    if ((char)v12)
    {
        sub_40a534();
        sub_404814();
        sub_4040f0();
    }
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v0;
    v2 = sub_40b0bb;
    return sub_40b0b3(&v4);
}
```

## `sub_0040b0b3` `0x0040b0b3`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40b0b3(void)
{
    return;
}
```

## `sub_0040b0b4` `0x0040b0b4`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40b0b4(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

