# elfbot.dll decompiled — loader 0x0040d98b..0x0040e7a6

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_0040d98b` `0x0040d98b`

_7 bytes. (leaf/helper — see body)_

```c
int sub_40d98b(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v0;  // ebx

    return v0;
}
```

## `sub_0040d992` `0x0040d992`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40d992(void)
{
    sub_40d994();
    return;
}
```

## `sub_0040d994` `0x0040d994`

_82 bytes. (leaf/helper — see body)_

```c
int sub_40d994(void)
{
    int v6;  // ebx
    int v7;  // eax
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4125
    unsigned int v12;  // 4103
    unsigned long v13;  // 4134
    unsigned long v14;  // 4119
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x14]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    sub_403e68(v6, 0, v7, &v4);
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v12 = *((int *)v11);
    v1 = *((int *)v11);
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v13) = &v1;
    sub_409eac(v12, sub_40d9f4, &v3);
    v0 = 0;
    sub_40d900();
    sub_40a918();
    v14 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v14) = v12;
    v2 = sub_40d9fb;
    sub_40d9e6();
    return;
}
```

## `sub_0040d9e6` `0x0040d9e6`

_14 bytes. (leaf/helper — see body)_

```c
int sub_40d9e6(void)
{
    return sub_403a34();
}
```

## `sub_0040d9f4` `0x0040d9f4`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40d9f4(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0040d9f9` `0x0040d9f9`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40d9f9(void)
{
    return sub_40d9e6();
}
```

## `sub_0040d9fb` `0x0040d9fb`

_7 bytes. (leaf/helper — see body)_

```c
int sub_40d9fb(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v0;  // ebx

    return v0;
}
```

## `sub_0040da02` `0x0040da02`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40da02(void)
{
    return sub_40da04();
}
```

## `sub_0040da04` `0x0040da04`

_92 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_4208cc;

int sub_40da04(void)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4165
    unsigned int v9;  // 4111
    unsigned long v10;  // 4169
    int v11;  // ebx
    unsigned long v12;  // 4120
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x14]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v9 = *((int *)v8);
    v0 = *((int *)v8);
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v10) = &v0;
    if (!g_4208cc)
    {
        sub_409eac(v9, sub_40da6e, &v2, v11, 0, 0, &v3);
        sub_409ee0();
        g_4208cc = GetModuleHandleW(NULL);
    }
    v12 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v12) = v9;
    v1 = sub_40da75;
    return sub_40da60(v11, 0, 0, &v3);
}
```

## `sub_0040da60` `0x0040da60`

_14 bytes. (leaf/helper — see body)_

```c
int sub_40da60(void)
{
    return sub_403a34();
}
```

## `sub_0040da6e` `0x0040da6e`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40da6e(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0040da73` `0x0040da73`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40da73(void)
{
    return sub_40da60();
}
```

## `sub_0040da75` `0x0040da75`

_7 bytes. (leaf/helper — see body)_

```c
int sub_40da75(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v0;  // ebx

    return v0;
}
```

## `sub_0040da7c` `0x0040da7c`

_125 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned short field_18;
} struct_0;

int sub_40da7c(void)
{
    int v6;  // ebx
    int v7;  // eax
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4150
    unsigned int v12;  // 4103
    unsigned long v13;  // 4154
    struct_0 *v14;  // eax
    unsigned long v15;  // 4118
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x14]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    sub_403e68(v6, 0, v7, &v4);
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v12 = *((int *)v11);
    v1 = *((int *)v11);
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v13) = &v1;
    if (!v7)
    {
        sub_40da04();
        v14 = sub_40a658();
    }
    else
    {
        sub_409eac(v12, sub_40db07, &v3);
        v0 = 0;
        sub_40da04();
        sub_40a918();
    }
    v15 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v15) = v12;
    v2 = sub_40db0e;
    sub_40daf9();
    return;
}
```

## `sub_0040daf9` `0x0040daf9`

_14 bytes. (leaf/helper — see body)_

```c
int sub_40daf9(void)
{
    return sub_403a34();
}
```

## `sub_0040db07` `0x0040db07`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40db07(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0040db0c` `0x0040db0c`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40db0c(void)
{
    return sub_40daf9();
}
```

## `sub_0040db0e` `0x0040db0e`

_7 bytes. (leaf/helper — see body)_

```c
int sub_40db0e(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v0;  // ebx

    return v0;
}
```

## `sub_0040db15` `0x0040db15`

_3 bytes. (leaf/helper — see body)_

```c
int sub_40db15(void)
{
    sub_40db18();
    return;
}
```

## `sub_0040db18` `0x0040db18`

_137 bytes. (leaf/helper — see body)_

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

typedef struct struct_0 {
    unsigned short field_0;
    char padding_2[58];
    unsigned int field_3c;
} struct_0;

int sub_40db18(void)
{
    void* v3;  // eax
    struct_0 **v4;  // edx
    unsigned int v5[31];  // eax
    unsigned int *v6;  // ecx
    MEMORY_BASIC_INFORMATION v0;  // [bp-0x134]
    char v1;  // [bp-0x118]

    if (VirtualQuery(v3, &v0, 0x1c) != 0x1c)
    {
        return;
    }
    else if (v0.State != 0x1000)
    {
        return;
    }
    else if (!v0.AllocationBase)
    {
        return;
    }
    else if (sub_4052ac(v0.AllocationBase, &v1, 260))
    {
        *(v4) = v0.AllocationBase;
        if (*(v4)->field_0 != 23117)
            return;
        v5 = (char *)*(v4) + *(v4)->field_3c;
        if (v5[0] != 17744)
            return;
        *(v6) = (char *)*(v4) + v5[30];
        return;
    }
    else
    {
        return;
    }
}
```

## `sub_0040dba1` `0x0040dba1`

_3 bytes. (leaf/helper — see body)_

```c
int sub_40dba1(void)
{
    sub_40dba4();
    return;
}
```

## `sub_0040dba4` `0x0040dba4`

_142 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[1];
    unsigned int field_1;
} struct_0;

typedef struct struct_1 {
    char padding_0[20];
    int field_14;
    char padding_18[4];
    unsigned int field_1c;
} struct_1;

int sub_40dba4(void)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // esi
    unsigned int v8;  // edi
    struct_0 *v9;  // eax
    unsigned int v10;  // eax
    int v11;  // eax
    unsigned int v12;  // edx
    int v13;  // eax
    struct_1 *v0;  // [bp-0x1c]
    char v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]
    unsigned int v4;  // [bp-0x4]

    v4 = v6;
    v3 = v7;
    v2 = v8;
    if (!v9)
    {
        return;
    }
    else if (!(char)sub_40ddd8(0))
    {
        return;
    }
    else if (v1 != 104)
    {
        return;
    }
    else if (!(GetVersion() & 0x80000000))
    {
        return;
    }
    else if ((char)sub_40db18())
    {
        return;
    }
    else if ((char)sub_40db18())
    {
        v10 = v0->field_14 - 1;
        if (v10 < NULL)
            return;
        v11 = v10 + 1;
        v12 = 0;
        while (true)
        {
            v13 = v11;
            if (*((int *)(v0->field_1c + v12 * 4)) == *((int *)(v9->padding_0)[1]))
                return;
            v12 += 1;
            v11 = v13 - 1;
            if (v13 == 1)
                return;
        }
    }
    else
    {
        return;
    }
}
```

## `sub_0040dc32` `0x0040dc32`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40dc32(void)
{
    sub_40dc34();
    return;
}
```

## `sub_0040dc34` `0x0040dc34`

_4 bytes. (leaf/helper — see body)_

```c
int sub_40dc34(void)
{
    return;
}
```

## `sub_0040dc38` `0x0040dc38`

_199 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_41ec48;
extern char g_41ec4c;
extern char g_41ec50;

unsigned int sub_40dc38(int a0)
{
    int v1;  // ebx
    unsigned int v2;  // eax
    unsigned int ch;  // eax
    unsigned int v4;  // eax
    unsigned int ch1;  // eax

    if (g_41ec50)
        return g_41ec48;
    g_41ec50 = 1;
    v2 = sub_40dc34(a0, v1);
    g_41ec48 = v2 - 16 ^ GetCurrentThreadId();
    GetCurrentThreadId();
    if (!(char)sub_40ddd8(0) || (ch = GetCurrentProcessId(), (GetCurrentProcessId() ^ g_41ec48)))
    {
        v4 = sub_40dc34();
        g_41ec48 = v4 ^ GetCurrentProcessId();
        GetCurrentThreadId();
        if (!(char)sub_40ddd8(0) || (ch1 = GetCurrentProcessId(), (GetCurrentProcessId() ^ g_41ec48)))
            g_41ec48 = 0;
    }
    else
    {
        g_41ec4c = 1;
    }
    return g_41ec48;
}
```

## `sub_0040dcff` `0x0040dcff`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40dcff(void)
{
    sub_40dd00();
    return;
}
```

## `sub_0040dd00` `0x0040dd00`

_20 bytes. (leaf/helper — see body)_

```c
extern char g_41ec4c;
extern char g_41ec50;

char sub_40dd00(void)
{
    int v1;  // ecx

    if (!g_41ec50)
        sub_40dc38(v1);
    return g_41ec4c;
}
```

## `sub_0040dd14` `0x0040dd14`

_183 bytes. (leaf/helper — see body)_

```c
int sub_40dd14(void)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned int *v17;  // edx
    int node;  // edx
    unsigned int v19;  // 4122
    unsigned int v20;  // 4106
    char v21;  // cl
    unsigned int *iter;  // eax
    unsigned int v23;  // edx
    int v24;  // edx
    unsigned short v10;  // fs
    unsigned int v25;  // 4127
    unsigned int v26;  // 4106
    unsigned long v27;  // 4134
    unsigned long v28;  // 4116
    unsigned long v11;  // 4152
    unsigned int v12;  // 4116
    unsigned long v13;  // 4161
    unsigned int *v14;  // eax
    unsigned int v15;  // 4127
    unsigned int v16;  // 4106
    unsigned int v0;  // [bp-0x28]
    int v1;  // [bp-0x1c]
    int v2;  // [bp-0x18]
    int v3;  // [bp-0x14]
    unsigned int *v4;  // [bp-0x10]
    char v5;  // [bp-0x9]
    char v6;  // [bp-0x4]

    v5 = 0;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v12 = *((int *)v11);
    v0 = *((int *)v11);
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v13) = &v0;
    v4 = sub_40464c(v12, sub_40ddc1, &v6, v1, v2, v3);
    v14 = v4;
    iter = v14 >> 1;
    v15 = _ccall(8, 27, v14 >> 1, v14, 0);
    if ((char)v15)
    {
        v16 = _ccall(27, v14 >> 1, v14, 0);
        iter = (char *)iter + (v16 & 1);
    }
    v17 = (char *)iter + 2;
    node = v17 >> 1;
    v19 = _ccall(8, 27, v17 >> 1, v17, 0);
    if ((char)v19)
    {
        v20 = _ccall(27, v17 >> 1, v17, 0);
        node += v20 & 1;
    }
    v21 = 0;
    if (node > 0)
    {
        do
        {
            if (*((int *)(*(iter) + iter * 12)) > v23)
            {
                iter = (char *)iter - node;
                if (iter < 0)
                    iter = NULL;
            }
            else if (*((int *)(*(iter) + iter * 12 + 4)) > v23)
            {
                v5 = *((char *)(*(iter) + iter * 12 + 8));
                v27 = _ccall(v8, v9, (unsigned int)v10, 0);
                *((unsigned int *)v27) = v12;
                return;
            }
            else
            {
                iter = (char *)iter + node;
                if (iter >= v4)
                    iter = (char *)v4 + 1;
            }
            if (v21)
                break;
            if (node == 1)
            {
                v21 = 1;
            }
            else
            {
                v24 = node + 1;
                node = v24 >> 1;
                v25 = _ccall(8, 27, v24 >> 1, v24, 0);
                if ((char)v25)
                {
                    v26 = _ccall(27, v24 >> 1, v24, 0);
                    node += v26 & 1;
                }
            }
        } while (node > 0);
    }
    v28 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v28) = v12;
    return;
}
```

## `sub_0040ddc1` `0x0040ddc1`

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

unsigned int sub_40ddc1(int a0)
{
    struct_1 *v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x8]

    return sub_4030c0(v0, a0, v1);
}
```

## `sub_0040ddc6` `0x0040ddc6`

_5 bytes. (leaf/helper — see body)_

```c
void sub_40ddc6(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int *a10)
{
    unsigned int v0;  // [bp+0x0]

    sub_4034ec(v0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10);
}
```

## `sub_0040ddd5` `0x0040ddd5`

_3 bytes. (leaf/helper — see body)_

```c
int sub_40ddd5(void)
{
    sub_40ddd8();
    return;
}
```

## `sub_0040ddd8` `0x0040ddd8`

_118 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_41ec54;

int sub_40ddd8(void)
{
    int v6;  // edi
    int v7;  // esi
    int v8;  // ebx
    unsigned int v9;  // eax
    unsigned int v10;  // ecx
    unsigned int v11;  // edx
    HANDLE ch;  // eax
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x20]
    char *v3;  // [bp-0x1c]
    char v4;  // [bp-0xc]
    unsigned int v5;  // [bp+0x4]

    if (v5 && !(char)sub_40dd14(v6, v7, v8))
        return;
    if (!g_41ec54)
        g_41ec54 = sub_40d994();
    if (v9)
    {
        v3 = &v4;
        v2 = v10;
        v1 = v11;
        v0 = v9;
        ch = GetCurrentProcess();
        if (g_41ec54(ch) && v10 == v4)
            return;
    }
    return;
}
```

## `sub_0040de4e` `0x0040de4e`

_70 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_4208c4;

int sub_40de4e(void)
{
    unsigned long v3;  // ldt
    unsigned long v4;  // gdt
    unsigned short v5;  // fs
    unsigned long v6;  // 4158
    unsigned int v7;  // 4105
    unsigned long v8;  // 4162
    unsigned int v9;  // 4117
    unsigned int v10;  // 4165
    unsigned long v11;  // 4118
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0x8]

    v6 = _ccall(v3, v4, (unsigned int)v5, 0);
    v7 = *((int *)v6);
    v0 = *((int *)v6);
    v8 = _ccall(v3, v4, (unsigned int)v5, 0);
    *((unsigned int **)v8) = &v0;
    v9 = g_4208c4;
    g_4208c4 = g_4208c4 + 1;
    v10 = _ccall(4, 18, v9 + 1, 0, 0);
    if ((char)v10)
    {
        sub_403a10(v7, sub_40de95, &/* unsupported instruction */, /* unsupported instruction */);
        sub_403a10();
        sub_403a10();
    }
    v11 = _ccall(v3, v4, (unsigned int)v5, 0);
    *((unsigned int *)v11) = v7;
    v1 = sub_40de9c;
    return sub_40de94(/* unsupported instruction */);
}
```

## `sub_0040de94` `0x0040de94`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40de94(void)
{
    return;
}
```

## `sub_0040de95` `0x0040de95`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40de95(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0040de9a` `0x0040de9a`

_2 bytes. (leaf/helper — see body)_

```c
void sub_40de9a(void)
{
    sub_40de94();
    return;
}
```

## `sub_0040de9c` `0x0040de9c`

_2 bytes. (leaf/helper — see body)_

```c
void sub_40de9c(unsigned int a0)
{
    return;
}
```

## `sub_0040de9e` `0x0040de9e`

_10 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_4208c4;

int sub_40de9e(void)
{
    unsigned int v1;  // eax

    g_4208c4 = g_4208c4 - 1;
    return v1;
}
```

## `sub_0040e275` `0x0040e275`

_3 bytes. (leaf/helper — see body)_

```c
int sub_40e275(void)
{
    unsigned long v1;  // ldt
    unsigned long v2;  // gdt
    unsigned short v3;  // es
    unsigned int v4;  // eax
    unsigned long v5;  // 4107

    v5 = _ccall(v1, v2, (unsigned int)v3, v4);
    *((char *)v5) = *((char *)v5) + (char)v4;
    sub_40e278();
    return;
}
```

## `sub_0040e278` `0x0040e278`

_95 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_41ec58;
extern unsigned int g_41ec5c;
extern unsigned int g_41ec60;
extern unsigned int g_41ec64;
extern unsigned int g_41ec68;

int sub_40e278(void)
{
    unsigned int v1;  // eax

    if (g_41ec58)
        return v1;
    g_41ec68 = sub_40d994();
    g_41ec58 = sub_40d994();
    g_41ec5c = sub_40d994();
    g_41ec60 = sub_40d994();
    g_41ec64 = sub_40d994();
    return g_41ec64;
}
```

## `sub_0040e2d7` `0x0040e2d7`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40e2d7(void)
{
    sub_40e2d8();
    return;
}
```

## `sub_0040e2d8` `0x0040e2d8`

_99 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_41ed04;
extern unsigned int g_41ed08;
extern unsigned int g_41ed0c;
extern unsigned int g_41ed10;
extern unsigned int g_41ed14;

int sub_40e2d8(void)
{
    unsigned int v1;  // eax

    if (g_41ed04)
        return v1;
    g_41ed04 = sub_40d994();
    g_41ed08 = sub_40d994();
    g_41ed0c = sub_40d994();
    g_41ed10 = sub_40d994();
    g_41ed14 = sub_40d994();
    return g_41ed14;
}
```

## `sub_0040e33b` `0x0040e33b`

_1 bytes. (leaf/helper — see body)_

```c
int sub_40e33b(void)
{
    sub_40e33c();
    return;
}
```

## `sub_0040e33c` `0x0040e33c`

_294 bytes. (leaf/helper — see body)_

```c
int sub_40e33c(void)
{
    int v8;  // ecx
    int v9;  // edi
    int v18;  // eax
    unsigned int v19;  // eax
    unsigned int v20;  // edx
    unsigned int v21;  // ebx
    unsigned long v22;  // 4132
    int v10;  // esi
    int v11;  // ebx
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    unsigned short v14;  // fs
    unsigned long v15;  // 4126
    unsigned int v16;  // 4103
    unsigned long v17;  // 4135
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x18]
    int v3;  // [bp-0x8]
    char v4;  // [bp-0x4]
    char v5;  // [bp+0x0]
    PSID v6;  // [bp+0x4]
    void* v7;  // [bp+0x8]

    v3 = v8;
    sub_403e68(v9, v10, v11, v8, &v5);
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    v16 = *((int *)v15);
    v1 = *((int *)v15);
    v17 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v17) = &v1;
    v18 = sub_40464c(v16, sub_40e46b, &v4);
    if (v18 == (int)v7[8])
    {
        if (!(int)v7[8])
        {
            v0 = 64;
            sub_404808();
        }
        else
        {
            v0 = (int)v7[8] * 2;
            sub_404808();
        }
    }
    *((unsigned int *)(*((int *)(int)v7[4]) + (int)v7[8] * 16)) = v19;
    sub_403a64();
    *((unsigned int *)(*((int *)(int)v7[4]) + (int)v7[8] * 16 + 8)) = v20;
    v21 = (!v6 ? NULL : GetLengthSid(v6));
    sub_403f60();
    if (v21 > 0)
        sub_402628();
    *((unsigned int *)&v7[8]) = (int)v7[8] + 1;
    v22 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int *)v22) = v16;
    v2 = sub_40e472;
    sub_40e462();
    return;
}
```

## `sub_0040e462` `0x0040e462`

_9 bytes. (leaf/helper — see body)_

```c
int sub_40e462(void)
{
    return sub_403a10();
}
```

## `sub_0040e46b` `0x0040e46b`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40e46b(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0040e470` `0x0040e470`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40e470(void)
{
    return sub_40e462();
}
```

## `sub_0040e472` `0x0040e472`

_8 bytes. (leaf/helper — see body)_

```c
void sub_40e472(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4)
{
    return;
}
```

## `sub_0040e47a` `0x0040e47a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40e47a(void)
{
    sub_40e47c();
    return;
}
```

## `sub_0040e47c` `0x0040e47c`

_492 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern char g_400000;
extern struct_0 *g_41ec58;
extern struct_0 *g_41ec5c;
extern struct_0 *g_41ec68;
extern struct_0 *g_41ed20;

int sub_40e47c(void)
{
    unsigned int v10;  // eax
    unsigned long v11;  // ldt
    HGLOBAL v20;  // esi
    unsigned int v21;  // eax
    HGLOBAL v22;  // ebx
    HGLOBAL v23;  // ebx
    unsigned long v25;  // 4121
    unsigned long v12;  // gdt
    unsigned short v13;  // fs
    unsigned long v14;  // 4160
    unsigned int v15;  // 4120
    unsigned long v16;  // 4169
    int v17;  // edi
    int v18;  // esi
    int v19;  // ebx
    unsigned int v0;  // [bp-0x190]
    unsigned int v1;  // [bp-0x18c]
    unsigned int v2;  // [bp-0x184]
    unsigned int v3;  // [bp-0x158]
    unsigned int v4;  // [bp-0x138]
    HANDLE v5;  // [bp-0x10], Other Possible Types: unsigned int
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]
    char v8;  // [bp-0x4]

    v7 = v10;
    v14 = _ccall(v11, v12, (unsigned int)v13, 0);
    v15 = *((int *)v14);
    v3 = *((int *)v14);
    v16 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int **)v16) = &v3;
    sub_404814(v15, sub_40e679, &v8, v17, v18, v19, 0, 0);
    v6 = 0;
    if (!(GetVersion() & 0x80000000))
    {
        if (!g_41ed20)
            g_41ed20 = sub_40da7c();
        v5 = 0;
        g_41ed20(5, 0, 0, &v5);
        v20 = NULL;
        if (!v5)
        {
            v5 = 0x10000;
            do
            {
                v5 *= 2;
                LocalFree(v20);
                v20 = sub_40536c(0x40, v5);
                v21 = g_41ed20(5, v20, v5, 0);
            } while (v21 && v5 != &g_400000);
        }
        else
        {
            v5 *= 2;
            v20 = sub_40536c(0x40, v5);
            v21 = g_41ed20(5, v20, v5, 0);
        }
        if (!v21)
        {
            v22 = v20;
            while (true)
            {
                v23 = v22;
                if ((int)v23[60])
                {
                    sub_409f44(0, &v8);
                    sub_40e33c(0, &v8);
                }
                else
                {
                    sub_40e33c(0, &v8);
                }
                if (!*((int *)v23))
                    break;
                v22 = v23 + *((int *)v23);
            }
        }
        LocalFree(v20);
    }
    else
    {
        sub_40e278();
        v5 = g_41ec68(2, 0);
        if (v5 != 0xffffffff)
        {
            v4 = 296;
            if (g_41ec58(v5, &v4))
            {
                do
                {
                    sub_403c54(0, &v8);
                    sub_40e33c(0, &v8);
                } while (g_41ec5c(v5, &v4));
            }
            CloseHandle(v5);
        }
    }
    v0 = v6;
    sub_404808();
    v25 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int *)v25) = v1;
    v2 = sub_40e680;
    sub_40e668();
    return;
}
```

## `sub_0040e668` `0x0040e668`

_17 bytes. (leaf/helper — see body)_

```c
int sub_40e668(void)
{
    return sub_403a34();
}
```

## `sub_0040e679` `0x0040e679`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40e679(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0040e67e` `0x0040e67e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40e67e(void)
{
    return sub_40e668();
}
```

## `sub_0040e680` `0x0040e680`

_7 bytes. (leaf/helper — see body)_

```c
void sub_40e680(unsigned int a0, unsigned int a1)
{
    return;
}
```

## `sub_0040e6a4` `0x0040e6a4`

_216 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_41ed24;

int sub_40e6a4(void)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    int v16;  // esi
    int v17;  // esi
    unsigned int idx;  // ebx
    int v19;  // esi
    int v20;  // esi
    unsigned long v21;  // 4118
    unsigned short v8;  // fs
    unsigned long v9;  // 4156
    unsigned int v10;  // 4119
    unsigned long v11;  // 4165
    int v12;  // edi
    int v13;  // esi
    int v14;  // ebx
    unsigned int v0;  // [bp-0x12c]
    unsigned int v1;  // [bp-0x124]
    char v2;  // [bp-0x10d]
    unsigned int v3;  // [bp-0x8]
    char v4;  // [bp-0x4]

    v3 = 0;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v10 = *((int *)v9);
    v0 = *((int *)v9);
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v0;
    sub_404814(v10, sub_40e796, &v4, v12, v13, v14, 0);
    if (!g_41ed24)
    {
        sub_4052ac(sub_40d900(), &v2, 260);
        sub_40e47c(v10);
        v16 = sub_404654();
        if (v16 >= 0)
        {
            v17 = v16 + 1;
            idx = 0;
            do
            {
                v19 = v17;
                sub_403c54();
                if ((char)sub_409318())
                {
                    g_41ed24 = *((int *)(v3 + idx * 16));
                    break;
                }
            } while ((idx += 1, v20 = (int)(v19 - 1), v17 = (int)(v19 - 1), v19 != 1));
        }
    }
    if (g_41ed24)
        OpenProcess(PROCESS_DUP_HANDLE, 0, g_41ed24);
    v21 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v21) = v10;
    v1 = sub_40e79d;
    return sub_40e77c();
}
```

## `sub_0040e77c` `0x0040e77c`

_26 bytes. (leaf/helper — see body)_

```c
int sub_40e77c(void)
{
    sub_403a10();
    return sub_404814();
}
```

## `sub_0040e796` `0x0040e796`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40e796(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0040e79b` `0x0040e79b`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40e79b(void)
{
    return sub_40e77c();
}
```

## `sub_0040e79d` `0x0040e79d`

_9 bytes. (leaf/helper — see body)_

```c
int sub_40e79d(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // ebx

    return v0;
}
```

## `sub_0040e7a6` `0x0040e7a6`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40e7a6(void)
{
    return sub_40e7a8();
}
```

