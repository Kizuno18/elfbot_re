# elfbot.dll decompiled — loader 0x0040e7a8..0x0040f8fe

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_0040e7a8` `0x0040e7a8`

_168 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_41ed28;

int sub_40e7a8(void)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    int v15;  // esi
    unsigned int idx;  // ebx
    int v17;  // esi
    int v18;  // esi
    unsigned long v19;  // 4118
    unsigned short v7;  // fs
    unsigned long v8;  // 4150
    unsigned int v9;  // 4115
    unsigned long v10;  // 4159
    int v11;  // edi
    int v12;  // esi
    int v13;  // ebx
    int v14;  // esi
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x1c]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v9 = *((int *)v8);
    v0 = *((int *)v8);
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v10) = &v0;
    sub_404814(v9, sub_40e867, &v2, v11, v12, v13, 0, 0, &v3);
    if (!g_41ed28)
    {
        sub_409eac();
        sub_40e47c();
        v14 = sub_404654();
        if (v14 >= 0)
        {
            v15 = v14 + 1;
            idx = 0;
            do
            {
                v17 = v15;
                if ((char)sub_409318())
                {
                    g_41ed28 = *((int *)(0 + idx * 16));
                    break;
                }
            } while ((idx += 1, v18 = (int)(v17 - 1), v15 = (int)(v17 - 1), v17 != 1));
        }
    }
    if (g_41ed28)
        OpenProcess(PROCESS_DUP_HANDLE, 0, g_41ed28);
    v19 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v19) = v9;
    v1 = sub_40e86e;
    return sub_40e850();
}
```

## `sub_0040e850` `0x0040e850`

_23 bytes. (leaf/helper — see body)_

```c
int sub_40e850(void)
{
    sub_403a10();
    return sub_404814();
}
```

## `sub_0040e867` `0x0040e867`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40e867(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0040e86c` `0x0040e86c`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40e86c(void)
{
    return sub_40e850();
}
```

## `sub_0040e86e` `0x0040e86e`

_9 bytes. (leaf/helper — see body)_

```c
int sub_40e86e(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5)
{
    unsigned int v0;  // ebx

    return v0;
}
```

## `sub_0040e877` `0x0040e877`

_1 bytes. (leaf/helper — see body)_

```c
int sub_40e877(void)
{
    sub_40e878();
    return;
}
```

## `sub_0040e878` `0x0040e878`

_79 bytes. (leaf/helper — see body)_

```c
int sub_40e878(void)
{
    unsigned int v2;  // ecx
    unsigned int v4;  // ebx
    HANDLE v6;  // eax
    HANDLE v0;  // [bp-0xc], Other Possible Types: unsigned int

    v0 = v2;
    v0 = NULL;
    v4 = (!(GetVersion() & 0x80000000) ? sub_40e7a8() : sub_40e6a4());
    if (v4)
    {
        DuplicateHandle(GetCurrentProcess(), v6, v4, &v0, 0, 0, DUPLICATE_SAME_ACCESS);
        CloseHandle(v4);
    }
    return;
}
```

## `sub_0040e8c7` `0x0040e8c7`

_1 bytes. (leaf/helper — see body)_

```c
int sub_40e8c7(void)
{
    sub_40e8c8();
    return;
}
```

## `sub_0040e8c8` `0x0040e8c8`

_145 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_41ed18;
extern unsigned int g_41ed1c;

int sub_40e8c8(void)
{
    unsigned int v9;  // ebx
    unsigned int v10;  // esi
    unsigned int *v19;  // eax
    unsigned int *v20;  // edx
    unsigned long v21;  // 4118
    unsigned int v11;  // edi
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    unsigned short v14;  // fs
    unsigned long v15;  // 4171
    unsigned int v16;  // 4113
    unsigned long v17;  // 4175
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    char *v2;  // [bp-0x18], Other Possible Types: unsigned int
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 0;
    v5 = v9;
    v4 = v10;
    v3 = v11;
    v2 = &v7;
    v1 = sub_40e962;
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    v16 = *((int *)v15);
    v0 = *((int *)v15);
    v17 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v17) = &v0;
    if (!g_41ed18 && (GetVersion() & 0x80000000))
    {
        sub_409eac();
        LoadLibraryA(sub_403e78());
        g_41ed18 = sub_40ab08(v16);
        g_41ed1c = sub_40ab08();
    }
    if (v19)
        *(v19) = g_41ed18;
    if (v20)
        *(v20) = g_41ed1c;
    v21 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int *)v21) = v16;
    v2 = sub_40e969;
    sub_40e959();
    return;
}
```

## `sub_0040e959` `0x0040e959`

_9 bytes. (leaf/helper — see body)_

```c
int sub_40e959(void)
{
    return sub_403a10();
}
```

## `sub_0040e962` `0x0040e962`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40e962(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0040e967` `0x0040e967`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40e967(void)
{
    return sub_40e959();
}
```

## `sub_0040e969` `0x0040e969`

_6 bytes. (leaf/helper — see body)_

```c
void sub_40e969(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4)
{
    return;
}
```

## `sub_0040e96f` `0x0040e96f`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40e96f(unsigned int a0, unsigned int a1)
{
    sub_40e970();
    return;
}
```

## `sub_0040e970` `0x0040e970`

_231 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_41ecf8;
extern struct_0 *g_41ed00;
extern struct_0 *g_41ed18;

unsigned int sub_40e970(unsigned int a0, HANDLE a1)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // esi
    unsigned int v8;  // edi
    HANDLE ch;  // esi
    unsigned int v10;  // edi
    unsigned int i;  // ebx
    unsigned int v0;  // [bp-0x2c]
    unsigned int v1;  // [bp-0x28]
    unsigned int v2;  // [bp-0x24]
    char v3;  // [bp-0x20], Other Possible Types: unsigned int
    unsigned int v4;  // [bp-0x1c]
    unsigned int v5;  // [bp-0x10]

    v2 = v6;
    v1 = v7;
    v0 = v8;
    ch = a1;
    if (a0 <= 0)
    {
        return 0;
    }
    else if (!(GetVersion() & 0x80000000))
    {
        v10 = 0;
        if (!g_41ecf8)
        {
            g_41ecf8 = sub_40d994();
            g_41ed00 = sub_40d994();
        }
        if (!ch)
            ch = GetCurrentProcess();
        for (i = 0x716f0000; g_41ed00(ch, i, &v3, 28) == 28; i = (i == v4 ? i - 0x10000 : v4))
        {
            if (v5 == 0x10000)
            {
                v10 = g_41ecf8(ch, v3, a0, 0x2000, 64);
                break;
            }
        }
        return g_41ecf8(ch, v10, a0, 0x1000, 64);
    }
    else
    {
        sub_40e8c8();
        return g_41ed18(a0);
    }
}
```

## `sub_0040ea57` `0x0040ea57`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40ea57(unsigned int a0, unsigned int a1)
{
    sub_40ea58();
    return;
}
```

## `sub_0040ea58` `0x0040ea58`

_121 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_41ecfc;
extern struct_0 *g_41ed1c;

char sub_40ea58(unsigned int a0, HANDLE a1)
{
    unsigned int v2;  // ebx
    unsigned int v3;  // esi
    HANDLE ch;  // esi
    char v5;  // al
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v1 = v2;
    v0 = v3;
    ch = a1;
    if (!(GetVersion() & 0x80000000))
    {
        if (!g_41ecfc)
            g_41ecfc = sub_40d994();
        if (!ch)
            ch = GetCurrentProcess();
        return g_41ecfc(ch, a0, 0, 0x8000);
    }
    else
    {
        sub_40e8c8();
        if (a0 < 0x80000000 || !g_41ed1c(a0))
            v5 = 0;
        else
            v5 = 1;
        return -(0 < v5);
    }
}
```

## `sub_0040ead1` `0x0040ead1`

_3 bytes. (leaf/helper — see body)_

```c
int sub_40ead1(void)
{
    return sub_40ead4();
}
```

## `sub_0040ead4` `0x0040ead4`

_108 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_41ed2c;
extern unsigned int g_41ed30;
extern unsigned int g_41ed34;
extern unsigned int g_41ed38;

int sub_40ead4(void)
{
    unsigned int v1;  // eax

    sub_40d900();
    v1 = GetVersion();
    if ((v1 & 0x80000000) && !g_41ed2c)
    {
        v1 = sub_40ab08();
        g_41ed2c = v1;
    }
    if (g_41ed30)
        return v1;
    g_41ed30 = sub_40d994();
    g_41ed34 = sub_40d994();
    g_41ed38 = sub_40d994();
    return g_41ed38;
}
```

## `sub_0040eb40` `0x0040eb40`

_61 bytes. (leaf/helper — see body)_

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

int sub_40eb40(void)
{
    void* v2;  // eax
    MEMORY_BASIC_INFORMATION v0;  // [bp-0x24]

    if (VirtualQuery(v2, &v0, 0x1c) == 0x1c && (((char)v0.Protect & 64) || ((char)v0.Protect & 128) || ((char)v0.Protect & 4) || ((char)v0.Protect & 8)))
        return;
    return;
}
```

## `sub_0040eb7d` `0x0040eb7d`

_3 bytes. (leaf/helper — see body)_

```c
int sub_40eb7d(unsigned int a0, unsigned int a1)
{
    return sub_40eb80();
}
```

## `sub_0040eb80` `0x0040eb80`

_156 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_41ed2c;
extern struct_0 *g_41ed30;
extern struct_0 *g_41ed34;
extern struct_0 *g_41ed38;

unsigned int sub_40eb80(unsigned int a0, unsigned int a1)
{
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = 0;
    if (!g_41ed30(a0, a1, 64, &v0, 0, &v1) || g_41ed34(a0, a1))
    {
        v2 = g_41ed38() & 0x80000000;
        if (!v2)
        {
            return v2;
        }
        else if ((a0 & 0x80000000))
        {
            g_41ed2c(65549, a0 >> 12, (a0 & 0xfff) + a1 + 0xfff >> 12, 4294967295, 0x20060000);
            if (g_41ed34(a0, a1))
                return 0;
        }
        else
        {
            return a0 & 0x80000000;
        }
    }
    return 1;
}
```

## `sub_0040ec20` `0x0040ec20`

_8 bytes. (leaf/helper — see body)_

```c
int sub_40ec20(void)
{
    unsigned int v1;  // eax
    unsigned int v2;  // edx

    sub_40eb80(v1, v2);
    return;
}
```

## `sub_0040ec28` `0x0040ec28`

_134 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_41ed2c;
extern struct_0 *g_41ed30;
extern struct_0 *g_41ed34;
extern struct_0 *g_41ed38;

unsigned int sub_40ec28(unsigned int a0, unsigned int a1)
{
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = 0;
    if (!g_41ed30(a0, a1, 32, &v0, 0, &v1))
    {
        v2 = g_41ed38() & 0x80000000;
        if (!v2)
        {
            return v2;
        }
        else if ((a0 & 0x80000000))
        {
            g_41ed2c(65549, a0 >> 12, (a0 & 0xfff) + a1 + 0xfff >> 12, 4294836223, 0);
            if (!g_41ed34(a0, a1))
                return 0;
        }
        else
        {
            return a0 & 0x80000000;
        }
    }
    return 1;
}
```

## `sub_0040ecae` `0x0040ecae`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40ecae(void)
{
    return;
}
```

## `sub_0040ecaf` `0x0040ecaf`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40ecaf(void)
{
    sub_40ecb0();
    return;
}
```

## `sub_0040ecb0` `0x0040ecb0`

_8 bytes. (leaf/helper — see body)_

```c
int sub_40ecb0(void)
{
    unsigned int v1;  // eax
    unsigned int v2;  // edx

    sub_40ec28(v1, v2);
    return;
}
```

## `sub_0040ecb8` `0x0040ecb8`

_575 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_41ed08;

int sub_40ecb8(void)
{
    HANDLE v28;  // edx
    int v29;  // edi
    char v38;  // cl
    unsigned int v39;  // ebx
    unsigned int v40;  // ecx
    unsigned int v41;  // esi
    unsigned int v42;  // eax
    unsigned int v43;  // eax
    int v44;  // esi
    int v45;  // esi
    unsigned int v46;  // edi
    int v47;  // esi
    int v30;  // esi
    unsigned int idx;  // ebx
    int v49;  // eax
    int v50;  // eax
    int v51;  // eax
    int v52;  // esi
    int v53;  // eax
    unsigned long v54;  // 4118
    int v31;  // ebx
    unsigned long v32;  // ldt
    unsigned long v33;  // gdt
    unsigned short v34;  // fs
    unsigned long v35;  // 4128
    unsigned int v36;  // 4103
    unsigned long v37;  // 4137
    unsigned int v0;  // [bp-0x94]
    int v1;  // [bp-0x90], Other Possible Types: unsigned int
    unsigned int v2;  // [bp-0x8c]
    unsigned int v3;  // [bp-0x88]
    char v4;  // [bp-0x70]
    unsigned int v5;  // [bp-0x6c]
    unsigned int v6;  // [bp-0x68]
    unsigned int v7;  // [bp-0x64]
    enum WIN32_ERROR v8;  // [bp-0x5c]
    unsigned int v9;  // [bp-0x50]
    unsigned int v10;  // [bp-0x4c]
    char v11;  // [bp-0x44]
    unsigned int v12;  // [bp-0x40]
    enum WIN32_ERROR v13;  // [bp-0x38]
    unsigned int v14;  // [bp-0x30]
    int *v15;  // [bp-0x2c]
    unsigned int v16;  // [bp-0x28]
    unsigned int v17;  // [bp-0x24]
    unsigned int v18;  // [bp-0x20]
    unsigned int v19;  // [bp-0x1c]
    struct_0 *iter;  // [bp-0x18]
    char v21;  // [bp-0x14], Other Possible Types: int
    unsigned int v22;  // [bp-0x10]
    unsigned int v23;  // [bp-0xc]
    HANDLE ch;  // [bp-0x8]
    char v25;  // [bp-0x4]
    unsigned int v26;  // [bp+0x4]
    unsigned int *v27;  // [bp+0x8]

    v22 = 0;
    ch = v28;
    sub_40402c(v29, v30, v31);
    v35 = _ccall(v32, v33, (unsigned int)v34, 0);
    v36 = *((int *)v35);
    v3 = *((int *)v35);
    v37 = _ccall(v32, v33, (unsigned int)v34, 0);
    *((unsigned int **)v37) = &v3;
    v23 = 0;
    sub_40d8e0(v36, sub_40ef0e, &v25);
    if (!v4)
    {
        SetLastError(v8);
    }
    else if (!v11)
    {
        SetLastError(v13);
    }
    else if (!v38 && v10)
    {
        SetLastError(0x770000);
    }
    else
    {
        if (!ch || (GetVersion() & 0x80000000))
            ch = GetCurrentProcess();
        v14 = sub_40e970(v12, ch);
        sub_403f60(v36, sub_40ef0e);
        v39 = v22;
        v40 = v7;
        iter = v39 + v40 + 4;
        v41 = v14;
        v19 = v41 + v40 + 4;
        v2 = 0;
        v1 = v6;
        v42 = v39;
        v1 = v6 - v42;
        v2 = -(v6 < v42);
        v17 = v6 - v42;
        v18 = -(v6 < v42);
        v2 = 0;
        v1 = v6;
        v43 = v41;
        v1 = v6 - v43;
        v2 = -(v6 < v43);
        v15 = v6 - v43;
        v16 = -(v6 < v43);
        sub_402628();
        v44 = sub_404654();
        if (v44 >= 0)
        {
            v45 = v44 + 1;
            v46 = 0;
            do
            {
                v47 = v45;
                idx = v9 + v46 * 28;
                if (*((int *)(idx + 20)) || *((int *)(idx + 24)))
                {
                    if (*((char *)(idx + 16)))
                    {
                        v49 = sub_40dba4();
                        v2 = 0;
                        v1 = v49;
                        v50 = *((int *)(idx + 20)) - (char *)v15;
                        v1 = v49 - v50;
                        v2 = -(-(v16) - (*((int *)(idx + 20)) < v15)) - (v49 < v50);
                        *((unsigned int *)(*((int *)(idx + 20)) - v17)) = v49 - v50 - 4;
                    }
                    else if (*((int *)(idx + 24)))
                    {
                        *((int *)&iter->padding_0[0]) = sub_40dba4();
                        *((unsigned int *)(*((int *)(idx + 24)) - v17)) = v19;
                        iter = &iter->field_4;
                        v19 += 4;
                    }
                    else
                    {
                        v51 = sub_40dba4();
                        *((int *)(*((int *)(idx + 20)) - v17)) = v51;
                    }
                }
            } while ((v46 += 1, v52 = (int)(v47 - 1), v45 = (int)(v47 - 1), v47 != 1));
        }
        sub_40e2d8();
        v53 = sub_403c80(&v21);
        if (g_41ed08(ch, v14, v22, v53) && sub_403c80() == v21)
            v23 = v5 - v6 + v14;
        if (v27)
            *(v27) = v14;
        if (v26)
            sub_40421c();
    }
    v54 = _ccall(v32, v33, (unsigned int)v34, 0);
    *((HANDLE *)v54) = ch;
    v0 = sub_40ef15;
    sub_40eef7();
    return;
}
```

## `sub_0040eef7` `0x0040eef7`

_23 bytes. (leaf/helper — see body)_

```c
int sub_40eef7(void)
{
    sub_4040f0();
    return sub_403a10();
}
```

## `sub_0040ef0e` `0x0040ef0e`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40ef0e(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0040ef13` `0x0040ef13`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40ef13(void)
{
    return sub_40eef7();
}
```

## `sub_0040ef15` `0x0040ef15`

_12 bytes. (leaf/helper — see body)_

```c
int sub_40ef15(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // [bp+0xffffc]

    return v0;
}
```

## `sub_0040ef21` `0x0040ef21`

_3 bytes. (leaf/helper — see body)_

```c
int sub_40ef21(void)
{
    HANDLE v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x4]
    PSECURITY_DESCRIPTOR v2;  // [bp+0x8]
    unsigned int v3;  // [bp+0xc]
    unsigned int *v4;  // [bp+0x10]

    return GetKernelObjectSecurity(v0, v1, v2, v3, v4);
}
```

## `sub_0040ef2a` `0x0040ef2a`

_55 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_41ed1c;
extern struct_0 *g_41ed44;
extern struct_0 *g_41ed48;
extern struct_0 *g_41ed58;

unsigned int sub_40ef2a(unsigned int *a0)
{
    unsigned int v0;  // ebx

    g_41ed48(a0[4], 4294967295, v0, /* unsupported instruction */);
    g_41ed58(a0[4]);
    g_41ed44(a0[3]);
    g_41ed1c(a0);
    return 0;
}
```

## `sub_0040ef61` `0x0040ef61`

_352 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned int field_20;
    char padding_24[32];
    struct struct_1 *field_44;
} struct_0;

typedef struct struct_1 {
    int field_0;
} struct_1;

extern struct_1 *g_41ed1c;
extern struct_1 *g_41ed44;
extern struct_1 *g_41ed48;
extern struct_1 *g_41ed4c;
extern struct_1 *g_41ed50;
extern struct_1 *g_41ed54;
extern struct_1 *g_41ed58;
extern struct_1 *g_41ed5c;
extern struct_1 *g_41ed60;
extern struct_1 *g_41ed64;
extern struct_1 *g_41ed68;

int sub_40ef61(void)
{
    int *v6;  // ebx
    unsigned int v7;  // edi
    unsigned int v16;  // eax
    int i;  // edx
    int v19;  // cc_dep2
    int v20;  // cc_dep2
    unsigned int v22;  // 4103
    unsigned int v23;  // 4109
    unsigned int v24;  // ebx
    unsigned int v25;  // eax
    unsigned int v8;  // esi
    unsigned int v26;  // eax
    unsigned int v27;  // eax
    unsigned int v28;  // ebx
    unsigned int v9;  // ebx
    int v10;  // esi
    int v11;  // edx
    unsigned int v12;  // cc_op
    int v13;  // cc_dep2
    unsigned int v14;  // cc_ndep
    int v15;  // edx
    unsigned int iter;  // [bp-0x18]
    int v1;  // [bp-0x14]
    char v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    struct_0 *ch;  // [bp-0x8]
    unsigned int v5[4];  // [bp+0x4]

    ch = NtGetCurrentPeb();
    v3 = 0;
    v6 = &ch->field_44->field_0;
    v1 = g_41ed64(v7, v8, v9) ^ ch;
    iter = 20;
    do
    {
        v10 = 0;
        v11 = *(v6) - 1;
        v12 = 15;
        v13 = 0;
        v14 = 0;
        if (v11 >= 0)
        {
            v15 = v11 + 1;
            v16 = 0;
            do
            {
                i = v15;
                v11 = v6[2 + 2 * v16];
                v12 = 15;
                v19 = 0;
                if (!v11 || !((v12 = 6, v19 = v1, v11 != v19 && !((v12 = 13, v11 = (int)(unsigned int)(char)(*((char *)((char *)&v6[1 + 2 * v16] + 3)) & 128), v20 = 0, v19 = 0, (*((char *)((char *)&v6[1 + 2 * v16] + 3)) & 128))))))
                    continue;
                v10 += 1;
                v12 = 6;
                v11 = v10;
                v14 = 0;
                v19 = 1;
                if (v10 > 1)
                    break;
                v14 = _ccall(v12, v11, v19, 0);
                v16 += 1;
                v12 = 21;
                v11 = i - 1;
                v13 = 0;
                v15 = i - 1;
            } while (i != 1);
        }
        v22 = _ccall(v12, v11, v13, v14);
        v23 = _ccall(14, 21, v10 - 1, 0, v22);
    } while ((char)v23 && (g_41ed68(100), iter -= 1, iter = iter, iter != 1));
    if ((ch->field_20 & 0x30800000))
    {
        g_41ed1c(v5);
        return v3;
    }
    v24 = g_41ed5c(0, 0, v5[0], v5[1], 0, &v2);
    if (!v24)
    {
        g_41ed1c(v5);
        return v3;
    }
    g_41ed48(v24, 4294967295);
    g_41ed60(v24, &v3);
    if (!(ch->field_20 & 0x30800000))
    {
        v25 = g_41ed4c(v5 + 1, 0, 0, 2);
        v26 = g_41ed50(v25);
        v27 = g_41ed4c(v26);
        if (g_41ed54(v27))
        {
            v5[3] = g_41ed44(32771);
            v28 = g_41ed5c(0, 0, v5[2], v5, 0, &v2);
            if (!v28)
                return v3;
            g_41ed58(v28);
            return v3;
        }
    }
    g_41ed1c(v5);
    return v3;
}
```

## `sub_0040f0c1` `0x0040f0c1`

_3 bytes. (leaf/helper — see body)_

```c
int sub_40f0c1(void)
{
    sub_40f0c4();
    return;
}
```

## `sub_0040f0c4` `0x0040f0c4`

_564 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    int field_8;
    int field_c;
} struct_0;

extern unsigned int g_41ed3c;
extern unsigned int g_41ed40;
extern unsigned int g_41ed44;
extern unsigned int g_41ed48;
extern unsigned int g_41ed4c;
extern unsigned int g_41ed50;
extern unsigned int g_41ed54;
extern unsigned int g_41ed58;
extern unsigned int g_41ed5c;
extern unsigned int g_41ed60;
extern unsigned int g_41ed64;
extern unsigned int g_41ed68;

int sub_40f0c4(void)
{
    unsigned long v11;  // ldt
    unsigned long v12;  // gdt
    unsigned int v21;  // edx
    unsigned int v22;  // edx
    unsigned int *v23;  // eax
    unsigned int *v24;  // edx
    unsigned long v25;  // 4119
    unsigned short v13;  // fs
    unsigned long v14;  // 4177
    unsigned int v15;  // 4118
    unsigned long v16;  // 4181
    int v17;  // edi
    int v18;  // esi
    int v19;  // ebx
    struct_0 *idx;  // edi
    struct_0 *v0;  // [bp-0x40]
    unsigned int v1;  // [bp-0x38]
    unsigned int v2;  // [bp-0x34]
    unsigned int v3;  // [bp-0x30]
    unsigned int v4;  // [bp-0x2c]
    unsigned int iter;  // [bp-0x14]
    unsigned int index[2];  // [bp-0x10]
    char v7;  // [bp-0x9]
    struct_0 *v8;  // [bp-0x8]
    char v9;  // [bp-0x4]

    index = NULL;
    v14 = _ccall(v11, v12, (unsigned int)v13, 0);
    v15 = *((int *)v14);
    v4 = *((int *)v14);
    v16 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int **)v16) = &v4;
    if (!g_41ed44)
    {
        g_41ed44 = sub_40d994(v15, sub_40f301, &v9, v17, v18, v19);
        g_41ed48 = sub_40d994();
        g_41ed4c = sub_40d994();
        g_41ed50 = sub_40d994();
        g_41ed54 = sub_40d994();
        g_41ed58 = sub_40d994();
        g_41ed5c = sub_40d994();
        g_41ed60 = sub_40d994();
        g_41ed64 = sub_40d994();
        g_41ed68 = sub_40d994();
    }
    if (!g_41ed3c && (GetVersion() & 0x80000000))
    {
        sub_409eac();
        v0 = NULL;
        v8 = CreateFileMappingA(0xffffffff, NULL, PAGE_READWRITE, 0, 16, sub_403e78());
        if (v8)
        {
            v7 = GetLastError() != ERROR_ALREADY_EXISTS;
            idx = (struct_0 *)MapViewOfFile(v8, FILE_MAP_ALL_ACCESS, 0, 0, NULL);
            v0 = v8;
            if (idx)
            {
                iter = 50;
                do
                {
                    if (v7)
                        break;
                    v3 = idx->field_4;
                    v2 = idx->field_0;
                    v21 = index[1];
                    if (index[1] == idx->field_4)
                    {
                        v21 = index[0];
                        v3 = idx->field_0;
                    }
                } while (v21 != v3 && (Sleep(50), iter -= 1, iter = iter, iter != 1));
                if (!v7)
                {
                    v3 = idx->field_4;
                    v2 = idx->field_0;
                    v22 = index[1];
                    if (index[1] == idx->field_4)
                    {
                        v22 = index[0];
                        v3 = idx->field_0;
                    }
                    if (v22 == v3)
                        goto LABEL_40f2ac;
                }
                idx->field_8 = sub_40ecb8(0, 0);
                idx->field_c = sub_40ecb8(0, 0);
                idx->field_0 = index[0];
                idx->field_4 = index[1];
                sub_40e878(0, 0);
LABEL_40f2ac:
                g_41ed3c = idx->field_8;
                g_41ed40 = idx->field_c;
                UnmapViewOfFile(idx);
                v0 = idx;
            }
            CloseHandle(v8);
        }
    }
    *(v23) = g_41ed3c;
    *(v24) = g_41ed40;
    v25 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((struct_0 **)v25) = v0;
    v1 = sub_40f308;
    sub_40f2f8();
    return;
}
```

## `sub_0040f2f8` `0x0040f2f8`

_9 bytes. (leaf/helper — see body)_

```c
int sub_40f2f8(void)
{
    return sub_403a10();
}
```

## `sub_0040f301` `0x0040f301`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40f301(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0040f306` `0x0040f306`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40f306(void)
{
    return sub_40f2f8();
}
```

## `sub_0040f308` `0x0040f308`

_9 bytes. (leaf/helper — see body)_

```c
int sub_40f308(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // ebx

    return v0;
}
```

## `sub_0040f311` `0x0040f311`

_3 bytes. (leaf/helper — see body)_

```c
int sub_40f311(void)
{
    sub_40f314();
    return;
}
```

## `sub_0040f314` `0x0040f314`

_79 bytes. (leaf/helper — see body)_

```c
int sub_40f314(void)
{
    int v2;  // ebx
    int v3;  // ecx
    unsigned int ch;  // eax
    char v0;  // [bp+0x0]

    if ((char)sub_40ddd8(0, v2, v3, &v0) && (char)sub_40ddd8(0))
    {
        ch = GetCurrentProcessId();
        if ((ch ^ sub_40dc38(v3)) == v3)
            return;
    }
    return;
}
```

## `sub_0040f363` `0x0040f363`

_1 bytes. (leaf/helper — see body)_

```c
int sub_40f363(void)
{
    sub_40f364();
    return;
}
```

## `sub_0040f364` `0x0040f364`

_136 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[32];
    unsigned int field_20;
} struct_0;

int sub_40f364(void)
{
    int v2;  // edi
    int v3;  // esi
    struct_0 *v4;  // eax
    unsigned int v0;  // [bp-0x8]

    v0 = 0;
    v2 = sub_404654();
    if (v2 < 0)
        return;
    do
    {
        v3 = v2 - 1;
        if (v3 >= 0)
        {
            do
            {
                if (*((int *)(v4->field_20 + v2 * 28 + 12)) == *((int *)(v4->field_20 + v3 * 28 + 12)) && (char)sub_40f314())
                {
                    v0 = *((int *)(v4->field_20 + v2 * 28 + 4)) - 6;
                    return;
                }
            } while ((v3 = (int)(v3 - 1), v3 != -1));
        }
    } while ((v2 = (int)(v2 - 1), v2 != -1));
    return;
}
```

## `sub_0040f3ec` `0x0040f3ec`

_50 bytes. (leaf/helper — see body)_

```c
int sub_40f3ec(void)
{
    unsigned int v3;  // ecx
    int v4;  // esi
    int v5;  // ebx
    unsigned int *v6;  // ebx
    unsigned int v7;  // eax
    unsigned int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = v3;
    v6 = sub_40d994(v4, v5, v3, &v1);
    if (v6 && v6(v7, &v0))
        return;
    v0 = 0;
    return;
}
```

## `sub_0040f41e` `0x0040f41e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40f41e(void)
{
    sub_40f420();
    return;
}
```

## `sub_0040f420` `0x0040f420`

_73 bytes. (leaf/helper — see body)_

```c
int sub_40f420(void)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4123
    unsigned long v10;  // 4132
    unsigned int v11;  // eax
    int v12;  // ecx
    unsigned long v13;  // 4150
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    char *v2;  // [bp-0x18]
    char v3;  // [bp-0x5]
    char v4;  // [bp-0x4]

    v3 = 0;
    if (!(GetVersion() & 0x80000000))
        return;
    v2 = &v4;
    v1 = sub_40f460;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v0 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v0;
    v3 = (*((char *)((v11 ^ sub_40dc38(v12)) + 32)) & 24);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v0;
    return;
}
```

## `sub_0040f460` `0x0040f460`

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

unsigned int sub_40f460(int a0)
{
    struct_1 *v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x8]

    return sub_4030c0(v0, a0, v1);
}
```

## `sub_0040f465` `0x0040f465`

_5 bytes. (leaf/helper — see body)_

```c
void sub_40f465(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int *a10)
{
    unsigned int v0;  // [bp+0x0]

    sub_4034ec(v0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10);
}
```

## `sub_0040f473` `0x0040f473`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40f473(void)
{
    sub_40f474();
    return;
}
```

## `sub_0040f474` `0x0040f474`

_1597 bytes. (leaf/helper — see body)_

```c
typedef struct struct_8 {
    char field_0;
    char padding_1[3];
    unsigned int field_4;
} struct_8;

typedef struct struct_1 {
    char padding_0[32];
    unsigned int field_20;
} struct_1;

typedef struct struct_3 {
    struct struct_1 *field_0;
} struct_3;

typedef struct struct_6 {
    char padding_0[1];
    struct struct_7 *field_1;
} struct_6;

typedef struct struct_0 {
    char field_0;
} struct_0;

typedef struct struct_7 {
    unsigned int field_0;
} struct_7;

extern unsigned int g_40fb1a;
extern struct_7 *g_41ed08;
extern struct_7 *g_41ed14;
extern void g_41ed6c;

int sub_40f474(unsigned int a0, struct_8 *a1, int a2, unsigned int a3, unsigned int a4, unsigned int a5, struct_0 **a6)
{
    unsigned int i;  // ecx
    unsigned int v39;  // ecx
    unsigned long v48;  // 4127
    unsigned long v49;  // 4136
    int v50;  // ecx
    int v51;  // eax
    int v52;  // eax
    unsigned long v53;  // 4129
    unsigned int v54;  // 4104
    unsigned long v55;  // 4138
    struct_3 **v56;  // eax
    unsigned long v57;  // 4129
    HANDLE v40;  // esi
    unsigned int v58;  // 4104
    unsigned long v59;  // 4138
    void* idx;  // esi
    int v61;  // eax
    unsigned int v62;  // ebx
    unsigned int idx1;  // eax
    unsigned int v64;  // ebx
    unsigned int j;  // ebx
    char l[4];  // esi
    char node[4];  // edi
    struct_8 *v41;  // edi
    unsigned int v68;  // ecx
    unsigned int v69;  // ebx
    unsigned long v70;  // 4128
    unsigned int v71;  // 4103
    unsigned long v72;  // 4137
    unsigned long v73;  // 4118
    unsigned long v74;  // 4118
    unsigned int v75;  // esi
    HANDLE ch;  // eax
    unsigned int v42;  // ebx
    HANDLE ch1;  // eax
    unsigned int v78;  // edi
    void* k;  // esi
    void* iter;  // edi
    unsigned int v81;  // ecx
    unsigned long v82;  // 4118
    int v43;  // edi
    int v44;  // ebx
    unsigned long v45;  // ldt
    unsigned long v46;  // gdt
    unsigned short v47;  // fs
    char v0;  // [bp-0x188]
    char v1;  // [bp-0xe1]
    unsigned int v2;  // [bp-0xdc]
    unsigned int v3;  // [bp-0xcc]
    int v4;  // [bp-0xc7]
    int v5;  // [bp-0xc2]
    unsigned long v6;  // [bp-0xbc]
    struct_6 *index;  // [bp-0xa0]
    unsigned long v8;  // [bp-0x98]
    unsigned int v9;  // [bp-0x90]
    unsigned int v10;  // [bp-0x88]
    int v11;  // [bp-0x80]
    unsigned int v12;  // [bp-0x7c]
    unsigned int v13;  // [bp-0x70]
    unsigned int v14;  // [bp-0x6c]
    int v15;  // [bp-0x64], Other Possible Types: unsigned int
    struct_8 *v16;  // [bp-0x60], Other Possible Types: unsigned int
    unsigned int v17;  // [bp-0x5c]
    int iter1;  // [bp-0x4c]
    int v19;  // [bp-0x48], Other Possible Types: unsigned int
    int v20;  // [bp-0x44], Other Possible Types: unsigned int
    unsigned int v21;  // [bp-0x40]
    int v22;  // [bp-0x3c], Other Possible Types: unsigned int
    int v23;  // [bp-0x38], Other Possible Types: unsigned int
    unsigned int v24;  // [bp-0x34]
    unsigned int v25;  // [bp-0x34]
    unsigned int *v26;  // [bp-0x30], Other Possible Types: unsigned int
    unsigned int v27;  // [bp-0x2c]
    char *v28;  // [bp-0x28]
    int v29;  // [bp-0x24]
    HANDLE v30;  // [bp-0x20], Other Possible Types: unsigned int *
    unsigned int *v31;  // [bp-0x1c], Other Possible Types: unsigned int
    int v32;  // [bp-0x18]
    unsigned int v33;  // [bp-0x14]
    struct_1 **v34;  // [bp-0x10], Other Possible Types: unsigned int
    struct_1 *v35;  // [bp-0xc], Other Possible Types: unsigned int
    int v36;  // [bp-0x8], Other Possible Types: unsigned int
    char v37;  // [bp-0x4]

    i = 48;
    do
    {
        v34 = 0;
        v33 = 0;
        i -= 1;
    } while (i != 1);
    v30 = v40;
    v41 = a1;
    v42 = a0;
    sub_40402c(v43, v40, v44, v39);
    v28 = &v37;
    v27 = sub_40fb4f;
    v48 = _ccall(v45, v46, (unsigned int)v47, 0);
    v26 = *((int *)v48);
    v49 = _ccall(v45, v46, (unsigned int)v47, 0);
    *((unsigned int **)v49) = &v26;
    v36 = 0;
    if (!(GetVersion() & 0x80000000))
    {
        v75 = 0;
        if (!v41)
        {
            ch = GetCurrentProcess();
            ch1 = GetCurrentThread();
            if (DuplicateHandle(GetCurrentProcess(), ch1, ch, &v30, 0, 0, DUPLICATE_SAME_ACCESS))
            {
                v31 = 0;
                GetKernelObjectSecurity(v40, 4, NULL, 0, &v31);
                if (v31 > 0)
                {
                    v75 = sub_402504();
                    if (GetKernelObjectSecurity(v40, 4, v75, v31 * 2, &v31))
                    {
                        v8 = 12;
                        (&v8)[1] = v75;
                        v9 = 0;
                        v41 = &v8;
                    }
                }
                CloseHandle(v40);
            }
        }
        sub_40e2d8();
        GetCurrentProcessId();
        v31 = sub_40f3ec();
        sub_40fb64(v42);
        if (sub_40f3ec(v42) != sub_40f3ec())
        {
            v26 = sub_40da7c();
            if (v26)
            {
                v24 = (!v41 ? NULL : v41->field_4);
                v25 = (!v41 ? NULL : v41->field_4);
                v23 = 0;
                v22 = 0;
                if (a2)
                {
                    if ((*((char *)((void*)&a5 + 2)) & 1))
                        v23 = a2;
                    else
                        v22 = a2;
                }
                v78 = sub_40e970(37, v42);
                v42 = v24;
                if (v78)
                {
                    v23 = v75;
                    v22 = v78;
                    k = &g_41ed6c;
                    iter = &v1;
                    for (v81 = 9; v81; k += 4)
                    {
                        v81 -= 1;
                        *((int *)iter) = *((int *)k);
                        iter += 4;
                    }
                    *((char *)iter) = *((char *)k);
                    v2 = a3;
                    v3 = v22;
                    v4 = sub_40d994();
                    v5 = sub_40d994();
                    if (g_41ed08(v42, v3, &v1, 37, &v30) && v26(v42, (!v41 ? NULL : v41->field_4), -(NULL < (((char)a5 & 4))), NULL, &v30, 37, v3, a4, &v31, &v27) >= 0)
                    {
                        v36 = sub_40f3ec();
                        *(a6) = v28;
                        v42 = v24;
                    }
                    else
                    {
                        sub_40ea58(v3, v42);
                        v42 = v24;
                    }
                }
            }
        }
        else
        {
            v36 = g_41ed14(v42, v41, a2, a3, a4, a5, a6);
        }
        sub_402524();
    }
    else if (v42 && v42 != 4294967295)
    {
        v35 = sub_40fb64(v42);
        if (v35 && sub_40dc38(v50) != v35 && !(char)sub_40f420())
        {
            SetLastError(ERROR_CALL_NOT_IMPLEMENTED);
            v35 ^= sub_40dc38(v50);
            v34 = &v35;
            sub_40d994();
            sub_40d8e0();
            if (sub_40464c() >= 7)
            {
                sub_404654();
                sub_40d8e0();
                sub_40421c();
                if (v11 < 200 && sub_40464c() >= 5)
                {
                    v51 = sub_404654();
                    v52 = sub_404654();
                    if (*((int *)(v14 + v51 * 28 + 12)) == *((int *)(v14 + v52 * 28 - 16)))
                    {
                        v33 = v10;
                        sub_404654();
                        sub_40d8e0();
                        sub_40421c();
                        if (v11 < 500 && sub_40f364())
                        {
                            v32 = sub_40ecb8(0, 0);
                            v53 = _ccall(v45, v46, (unsigned int)v47, 0);
                            v54 = *((int *)v53);
                            v19 = *((int *)v53);
                            v55 = _ccall(v45, v46, (unsigned int)v47, 0);
                            *((unsigned int **)v55) = &v19;
                            sub_40d8e0(v54, sub_40f90a, &v37);
                            v56 = sub_40f364(v54, sub_40f90a, &v37);
                            if (!v56)
                            {
                                v74 = _ccall(v45, v46, (unsigned int)v47, 0);
                                *((unsigned int *)v74) = v54;
                                v21 = &g_40fb1a;
                                return sub_40f8fe();
                            }
                            *(v56) = &v34;
                            v29 = sub_40ecb8(0, 0);
                            v57 = _ccall(v45, v46, (unsigned int)v47, 0);
                            v58 = *((int *)v57);
                            v17 = *((int *)v57);
                            v59 = _ccall(v45, v46, (unsigned int)v47, 0);
                            *((unsigned int **)v59) = &v17;
                            sub_40d8e0(v58, sub_40f8ea, &v37);
                            idx = v14 + sub_404654() * 28 - 56;
                            sub_40ecb8(0, 0);
                            v16 = 0;
                            v15 = sub_40ecb8(0, 0);
                            v15 = sub_40ecb8(0, 0) - (int)idx[8];
                            v16 = -(sub_40ecb8(0, 0) < (int)idx[8]);
                            *((int *)(int)idx[20]) = sub_40ecb8(0, 0) - (int)idx[8];
                            v61 = sub_404654();
                            if (v61 >= 0)
                            {
                                iter1 = v61 + 1;
                                v62 = 0;
                                do
                                {
                                    idx1 = v62 * 6;
                                    if (*((int *)(v13 + idx1 * 8)) < (int)idx[4] && *((int *)(v13 + idx1 * 8 + 4)) > (int)idx[4] && *((short *)*((int *)(v13 + idx1 * 8))) == 2154)
                                    {
                                        *((unsigned short *)*((int *)(v13 + idx1 * 8))) = 6250;
                                        break;
                                    }
                                } while ((v62 += 1, iter1 = (int)(iter1 - 1), iter1 = iter1, iter1 != 1));
                            }
                            if (!a2)
                            {
                                a2 = -0x3000;
                            }
                            else if (a2 > 0)
                            {
                                a2 = -(a2);
                            }
                            v21 = sub_40e970(20, NULL);
                            *((unsigned int *)sub_40e970(20, NULL)) = a3;
                            *((unsigned int *)(sub_40e970(20, NULL) + 4)) = a4;
                            v31 = NULL;
                            v30 = NULL;
                            sub_40d994(v58, sub_40f8ea);
                            sub_40c63c();
                            v64 = 10;
                            do
                            {
                                j = v64;
                                if (*((unsigned short *)((void*)&v6 + 2)) != 161)
                                    continue;
                                if (v31)
                                {
                                    v30 = *((int *)(index->padding_0)[1]);
                                    break;
                                }
                                else
                                {
                                    v31 = *((int *)(index->padding_0)[1]);
                                }
                                sub_40c63c();
                                v16 = v41;
                                l = &v0;
                                node = &v6;
                                for (v68 = 9; v68; l += 1)
                                {
                                    v68 -= 1;
                                    *(node) = *(l);
                                    node += 1;
                                }
                                v69 = j - 1;
                                v64 = v69;
                            } while (j != 1);
                            if (v31 || v30)
                            {
                                sub_40d900();
                                v20 = sub_40ab08();
                                sub_40d900();
                                v19 = sub_40ab08();
                                if (sub_40ab08() && sub_40ab08())
                                {
                                    if (v31)
                                        sub_40ab08()(*(v31));
                                    if (v30)
                                        sub_40ab08()(*(v30));
                                }
                            }
                            else
                            {
                                v20 = 0;
                                v19 = 0;
                            }
                            v70 = _ccall(v45, v46, (unsigned int)v47, 0);
                            v71 = *((int *)v70);
                            v14 = *((int *)v70);
                            v72 = _ccall(v45, v46, (unsigned int)v47, 0);
                            *((unsigned int **)v72) = &v14;
                            if ((char)sub_40f0c4(v71, sub_40f8b9, &v37) && !(v35->field_20 & 0x30800000))
                                v36 = sub_40ecb8(NULL, NULL)(v41, a2, v33, sub_40e970(20, NULL), a5, a6);
                            v73 = _ccall(v45, v46, (unsigned int)v47, 0);
                            *((struct_8 **)v73) = v41;
                            v12 = sub_40f8c0;
                            return sub_40f88e();
                        }
                    }
                }
            }
        }
        else
        {
            SetLastError(ERROR_INVALID_PARAMETER);
        }
    }
    else
    {
        v42 = 87;
        SetLastError(ERROR_INVALID_PARAMETER);
    }
    v82 = _ccall(v45, v46, (unsigned int)v47, 0);
    *((unsigned int *)v82) = v42;
    v27 = sub_40fb56;
    return sub_40fb27();
}
```

## `sub_0040f88e` `0x0040f88e`

_43 bytes. (leaf/helper — see body)_

```c
unsigned int sub_40f88e(void)
{
    unsigned int v5;  // eax
    unsigned int v6;  // eax
    unsigned int v7;  // eax
    unsigned int *v1;  // [bp+0xfffc0]
    unsigned int v2;  // [bp+0xfffc4]
    unsigned int *v3;  // [bp+0xfffe8]
    unsigned int *v4;  // [bp+0xfffec]

    if (!v2)
    {
        return v7;
    }
    else if (v1)
    {
        if (v3)
            v5 = v1(*(v3));
        if (!v4)
            return v5;
        v1(*(v4));
        return v5;
    }
    else
    {
        return v6;
    }
}
```

## `sub_0040f8b9` `0x0040f8b9`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40f8b9(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0040f8be` `0x0040f8be`

_2 bytes. (leaf/helper — see body)_

```c
unsigned int sub_40f8be(void)
{
    return sub_40f88e();
}
```

## `sub_0040f8c0` `0x0040f8c0`

_30 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_40f8f1;

int sub_40f8c0(unsigned int a0, unsigned int a1)
{
    unsigned long v3;  // ldt
    unsigned long v4;  // gdt
    unsigned short v5;  // fs
    unsigned long v6;  // 4118
    unsigned int v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0xfffc8]
    unsigned int v2;  // [bp+0x100000]

    if (!v2)
        sub_40ea58(v1, NULL);
    v6 = _ccall(v3, v4, (unsigned int)v5, 0);
    *((unsigned int *)v6) = v0;
    a1 = &g_40f8f1;
    return sub_40f8de();
}
```

## `sub_0040f8de` `0x0040f8de`

_12 bytes. (leaf/helper — see body)_

```c
char sub_40f8de(void)
{
    unsigned int v1;  // [bp+0xfffe4]

    return sub_40ea58(v1, NULL);
}
```

## `sub_0040f8ea` `0x0040f8ea`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40f8ea(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0040f8ef` `0x0040f8ef`

_2 bytes. (leaf/helper — see body)_

```c
char sub_40f8ef(void)
{
    return sub_40f8de();
}
```

## `sub_0040f8fe` `0x0040f8fe`

_12 bytes. (leaf/helper — see body)_

```c
char sub_40f8fe(void)
{
    unsigned int v1;  // [bp+0xffff0]

    return sub_40ea58(v1, NULL);
}
```

