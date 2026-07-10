# elfbot.dll decompiled — loader 0x004013cb..0x00402440

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_004013cb` `0x004013cb`

_1 bytes. (leaf/helper — see body)_

```c
int sub_4013cb(void)
{
    sub_4013cc();
    return;
}
```

## `sub_004013cc` `0x004013cc`

_119 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    void* field_0;
    UIntPtr field_4;
} struct_0;

int sub_4013cc(void)
{
    struct_0 *idx;  // ecx
    void* v2;  // eax
    void* v3;  // edi
    unsigned int v4;  // edx
    unsigned int v5;  // esi

    idx->field_4 = 0x100000;
    v3 = VirtualAlloc(v2, 0x100000, MEM_RESERVE, PAGE_READWRITE);
    idx->field_0 = v3;
    if (!v3)
    {
        v5 = v4 + 0xffff & 0xffff0000;
        idx->field_4 = v5;
        idx->field_0 = VirtualAlloc(v2, v5, MEM_RESERVE, PAGE_READWRITE);
    }
    if (!idx->field_0)
        return;
    if ((char)sub_40121c())
        return;
    VirtualFree(idx->field_0, NULL, MEM_RELEASE);
    idx->field_0 = NULL;
    return;
}
```

## `sub_00401443` `0x00401443`

_1 bytes. (leaf/helper — see body)_

```c
int sub_401443(void)
{
    sub_401444();
    return;
}
```

## `sub_00401444` `0x00401444`

_184 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_1 *field_0;
    char padding_4[8];
    unsigned int field_c;
} struct_0;

typedef struct struct_1 {
    struct struct_0 *field_0;
} struct_1;

extern unsigned int g_4205bc;
extern struct_0 *g_4205e0;

int sub_401444(void)
{
    unsigned int v4;  // edx
    unsigned int v5;  // eax
    struct_0 *v6;  // ebx
    struct_0 *idx;  // ebx
    struct_0 **v8;  // edi
    unsigned int v9;  // esi
    unsigned int v10;  // eax
    unsigned int v11[2];  // ecx
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]

    v0 = 4294967295;
    v1 = 0;
    v2 = v4 + v5;
    v6 = g_4205e0;
    while (true)
    {
        idx = v6;
        if (idx == &g_4205e0)
            break;
        v8 = idx->field_0;
        v9 = *((int *)&idx->padding_4[4]);
        if (v5 <= v9 && v9 + idx->field_c <= v2)
        {
            if (v9 < v0)
                v0 = v9;
            v10 = v9 + idx->field_c;
            if (v10 > v1)
                v1 = v10;
            if (!VirtualFree(v9, NULL, MEM_RELEASE))
                g_4205bc = 1;
            sub_40124c();
        }
        v6 = v8;
    }
    v11[0] = 0;
    if (v1)
    {
        v11[0] = v0;
        v11[1] = v1 - v0;
    }
    return;
}
```

## `sub_004014fc` `0x004014fc`

_146 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_1 *field_0;
    char padding_4[8];
    unsigned int field_c;
} struct_0;

typedef struct struct_1 {
    struct struct_0 *field_0;
} struct_1;

extern struct_0 *g_4205e0;

int sub_4014fc(void)
{
    unsigned int v2;  // eax
    unsigned int v3;  // ebp
    unsigned int v4;  // edx
    unsigned int v5[2];  // ecx
    struct_0 *idx;  // esi
    unsigned int v7;  // ebx
    unsigned int v8;  // edi
    unsigned int v0;  // [bp-0x14]

    v3 = v2 & 0xfffff000;
    v0 = v2 + v4 + 0xfff & 0xfffff000;
    v5[0] = v3;
    v5[1] = v0 - v3;
    for (idx = g_4205e0; idx != &g_4205e0; idx = idx->field_0)
    {
        v7 = *((int *)&idx->padding_4[4]);
        v8 = idx->field_c + v7;
        if (v3 > v7)
            v7 = v3;
        if (v8 > v0)
            v8 = v0;
        if (v8 > v7 && !VirtualAlloc(v7, v8 - v7, MEM_COMMIT, PAGE_READWRITE))
        {
            v5[0] = 0;
            return;
        }
    }
    return;
}
```

## `sub_0040158e` `0x0040158e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40158e(void)
{
    sub_401590();
    return;
}
```

## `sub_00401590` `0x00401590`

_125 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_1 *field_0;
    char padding_4[8];
    unsigned int field_c;
} struct_0;

typedef struct struct_1 {
    struct struct_0 *field_0;
} struct_1;

extern unsigned int g_4205bc;
extern struct_0 *g_4205e0;

int sub_401590(void)
{
    unsigned int v2[2];  // ecx
    unsigned int v3;  // eax
    unsigned int v4;  // edx
    unsigned int v5;  // ebp
    struct_0 *idx;  // esi
    unsigned int v7;  // ebx
    unsigned int v8;  // edi
    unsigned int v0[2];  // [bp-0x14], Other Possible Types: unsigned int

    v0 = v2;
    v0 = v3 + 0xfff & 0xfffff000;
    v5 = v3 + v4 & 0xfffff000;
    v2[0] = v0;
    v2[1] = v5 - v0;
    for (idx = g_4205e0; idx != &g_4205e0; idx = idx->field_0)
    {
        v7 = *((int *)&idx->padding_4[4]);
        v8 = idx->field_c + v7;
        if (v7 < v0)
            v7 = v0;
        if (v5 < v8)
            v8 = v5;
        if (v8 > v7 && !VirtualFree(v7, v8 - v7, MEM_DECOMMIT))
            g_4205bc = 2;
    }
    return;
}
```

## `sub_0040160d` `0x0040160d`

_3 bytes. (leaf/helper — see body)_

```c
int sub_40160d(void)
{
    sub_401610();
    return;
}
```

## `sub_00401610` `0x00401610`

_142 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_1 *field_0;
    char padding_4[4];
    unsigned int field_8;
} struct_0;

typedef struct struct_1 {
    struct struct_0 *field_0;
} struct_1;

extern struct_0 *g_4205f0;

int sub_401610(void)
{
    struct_0 *idx;  // ebx
    unsigned int v3;  // eax
    unsigned int index[2];  // edx
    unsigned int v0;  // [bp-0x18]

    while (true)
    {
        for (idx = g_4205f0; idx != &g_4205f0; idx = idx->field_0)
        {
            if ((v3 + 0x3fff & 0xffffc000) <= idx[1].field_0)
            {
                sub_4014fc();
                if (!index[0])
                    return;
                idx->field_8 = idx->field_8 + index[1];
                idx[1].field_0 = (char *)idx[1].field_0 - index[1];
                if (idx[1].field_0)
                    return;
                sub_40124c();
                return;
            }
        }
        sub_401368();
        if (!index[0])
            return;
        sub_401264();
        if (!v0)
        {
            sub_401444();
            index[0] = 0;
            return;
        }
    }
}
```

## `sub_0040169e` `0x0040169e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40169e(void)
{
    sub_4016a0();
    return;
}
```

## `sub_004016a0` `0x004016a0`

_291 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_1 *field_0;
    char padding_4[4];
    unsigned int field_8;
} struct_0;

typedef struct struct_1 {
    struct struct_0 *field_0;
} struct_1;

extern struct_0 *g_4205f0;

int sub_4016a0(void)
{
    unsigned int v3;  // edx
    unsigned int v4;  // edi
    struct_0 *idx;  // ebx
    unsigned int v6;  // eax
    unsigned int index[2];  // ecx
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x18]

    v4 = v3 + 0x3fff & 0xffffc000;
    while (true)
    {
        for (idx = g_4205f0; idx != &g_4205f0 && v6 != idx->field_8; idx = idx->field_0);
        if (v6 == idx->field_8)
        {
            if (v4 <= idx[1].field_0)
                break;
            sub_4013cc();
            if (v0)
            {
                sub_401264();
                if (!v1)
                {
                    sub_401444();
                    index[0] = 0;
                    return;
                }
                continue;
            }
        }
        sub_4013cc();
        if (!v0)
            break;
        sub_401264();
        if (!v1)
        {
            sub_401444();
            index[0] = 0;
            return;
        }
    }
    if (v6 == idx->field_8 && v4 <= idx[1].field_0)
    {
        sub_4014fc();
        if (!index[0])
            return;
        idx->field_8 = idx->field_8 + index[1];
        idx[1].field_0 = (char *)idx[1].field_0 - index[1];
        if (idx[1].field_0)
            return;
        sub_40124c();
        return;
    }
    index[0] = 0;
    return;
}
```

## `sub_004017c3` `0x004017c3`

_1 bytes. (leaf/helper — see body)_

```c
int sub_4017c3(void)
{
    sub_4017c4();
    return;
}
```

## `sub_004017c4` `0x004017c4`

_140 bytes. (leaf/helper — see body)_

```c
int sub_4017c4(void)
{
    unsigned int v5;  // eax
    int v6;  // edx
    unsigned int *v7;  // ecx
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]

    if ((v5 + 0x3fff & 0xffffc000) >= (v6 + v5 & 0xffffc000))
    {
        *(v7) = 0;
        return;
    }
    sub_401590(v6);
    sub_401264();
    if (v0)
    {
        sub_401444();
        v0 = v2;
        v1 = v3;
    }
    if (!v0)
        return;
    sub_4012d8();
    return;
}
```

## `sub_00401850` `0x00401850`

_162 bytes. (leaf/helper — see body)_

```c
typedef struct LIST_ENTRY {
    void* Flink;
    void* Blink;
} LIST_ENTRY;

typedef struct CRITICAL_SECTION_DEBUG {
    unsigned short Type;
    unsigned short CreatorBackTraceIndex;
    void* CriticalSection;
    LIST_ENTRY ProcessLocksList;
    unsigned int EntryCount;
    unsigned int ContentionCount;
    unsigned int Flags;
    unsigned short CreatorBackTraceIndexHigh;
    unsigned short Identifier;
} CRITICAL_SECTION_DEBUG;

typedef struct CRITICAL_SECTION {
    struct CRITICAL_SECTION_DEBUG *DebugInfo;
    int LockCount;
    int RecursionCount;
    HANDLE OwningThread;
    HANDLE LockSemaphore;
    UIntPtr SpinCount;
} CRITICAL_SECTION;

extern char g_420045;
extern char g_4205b8;
extern CRITICAL_SECTION g_4205c0;
extern unsigned int g_420600;
extern unsigned int g_420604;
extern unsigned int g_42060c;
extern unsigned int g_420618;

int sub_401850(void)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4130
    unsigned long v9;  // 4139
    unsigned int i;  // eax
    unsigned long v11;  // 4118
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    char *v2;  // [bp-0x8], Other Possible Types: unsigned int
    char v3;  // [bp-0x4]

    v2 = &v3;
    v1 = sub_401906;
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v0 = *((int *)v8);
    v9 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v9) = &v0;
    InitializeCriticalSection(&g_4205c0.DebugInfo);
    if (g_420045)
        EnterCriticalSection(&g_4205c0.DebugInfo);
    sub_401214();
    sub_401214();
    sub_401214();
    g_420618 = LocalAlloc(GMEM_FIXED, 0xff8);
    if (g_420618)
    {
        i = 3;
        do
        {
            *((unsigned int *)(g_420618 + i * 4 - 12)) = 0;
            i += 1;
        } while (i != 1025);
        g_420604 = &g_420600;
        g_420600 = &g_420600;
        g_42060c = &g_420600;
        g_4205b8 = 1;
    }
    v11 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v11) = v0;
    v2 = sub_40190d;
    return sub_4018f2();
}
```

## `sub_004018f2` `0x004018f2`

_20 bytes. (leaf/helper — see body)_

```c
typedef struct LIST_ENTRY {
    void* Flink;
    void* Blink;
} LIST_ENTRY;

typedef struct CRITICAL_SECTION_DEBUG {
    unsigned short Type;
    unsigned short CreatorBackTraceIndex;
    void* CriticalSection;
    LIST_ENTRY ProcessLocksList;
    unsigned int EntryCount;
    unsigned int ContentionCount;
    unsigned int Flags;
    unsigned short CreatorBackTraceIndexHigh;
    unsigned short Identifier;
} CRITICAL_SECTION_DEBUG;

typedef struct CRITICAL_SECTION {
    struct CRITICAL_SECTION_DEBUG *DebugInfo;
    int LockCount;
    int RecursionCount;
    HANDLE OwningThread;
    HANDLE LockSemaphore;
    UIntPtr SpinCount;
} CRITICAL_SECTION;

extern char g_420045;
extern CRITICAL_SECTION g_4205c0;

void sub_4018f2(void)
{
    if (g_420045)
        LeaveCriticalSection(&g_4205c0.DebugInfo);
    return;
}
```

## `sub_00401906` `0x00401906`

_5 bytes. (leaf/helper — see body)_

```c
void sub_401906(unsigned int a0, unsigned int a1)
{
    sub_403374();
    return;
}
```

## `sub_0040190b` `0x0040190b`

_2 bytes. (leaf/helper — see body)_

```c
void sub_40190b(void)
{
    sub_4018f2();
    return;
}
```

## `sub_0040190d` `0x0040190d`

_7 bytes. (leaf/helper — see body)_

```c
extern char g_4205b8;

char sub_40190d(unsigned int a0)
{
    return g_4205b8;
}
```

## `sub_00401914` `0x00401914`

_187 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_1 *field_0;
    char padding_4[4];
    void* field_8;
} struct_0;

typedef struct struct_1 {
    struct struct_0 *field_0;
} struct_1;

typedef struct LIST_ENTRY {
    void* Flink;
    void* Blink;
} LIST_ENTRY;

typedef struct CRITICAL_SECTION_DEBUG {
    unsigned short Type;
    unsigned short CreatorBackTraceIndex;
    void* CriticalSection;
    LIST_ENTRY ProcessLocksList;
    unsigned int EntryCount;
    unsigned int ContentionCount;
    unsigned int Flags;
    unsigned short CreatorBackTraceIndexHigh;
    unsigned short Identifier;
} CRITICAL_SECTION_DEBUG;

typedef struct CRITICAL_SECTION {
    struct CRITICAL_SECTION_DEBUG *DebugInfo;
    int LockCount;
    int RecursionCount;
    HANDLE OwningThread;
    HANDLE LockSemaphore;
    UIntPtr SpinCount;
} CRITICAL_SECTION;

extern unsigned int g_4019f1;
extern char g_420045;
extern char g_4205b8;
extern CRITICAL_SECTION g_4205c0;
extern struct_1 *g_4205d8;
extern struct_0 *g_4205e0;
extern unsigned int g_420618;

int sub_401914(void)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4150
    unsigned long v9;  // 4154
    struct_0 *i;  // ebx
    struct_1 **v11;  // eax
    unsigned long v12;  // 4118
    unsigned int v13;  // eax
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char *v2;  // [bp-0xc], Other Possible Types: unsigned int
    char v3;  // [bp-0x4]

    if (!g_4205b8)
        return v13;
    v2 = &v3;
    v1 = sub_4019ea;
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v0 = *((int *)v8);
    v9 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v9) = &v0;
    if (g_420045)
        EnterCriticalSection(&g_4205c0.DebugInfo);
    g_4205b8 = 0;
    sub_40118c(g_420618);
    g_420618 = 0;
    for (i = g_4205e0; i != &g_4205e0; i = i->field_0)
    {
        VirtualFree(i->field_8, NULL, MEM_RELEASE);
    }
    sub_401214();
    sub_401214();
    sub_401214();
    v11 = g_4205d8;
    if (g_4205d8)
    {
        do
        {
            g_4205d8 = *(v11);
            sub_40118c(v11);
            v11 = g_4205d8;
        } while (g_4205d8);
    }
    v12 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v12) = v0;
    v2 = &g_4019f1;
    return sub_4019cc();
}
```

## `sub_004019cc` `0x004019cc`

_30 bytes. (leaf/helper — see body)_

```c
typedef struct LIST_ENTRY {
    void* Flink;
    void* Blink;
} LIST_ENTRY;

typedef struct CRITICAL_SECTION_DEBUG {
    unsigned short Type;
    unsigned short CreatorBackTraceIndex;
    void* CriticalSection;
    LIST_ENTRY ProcessLocksList;
    unsigned int EntryCount;
    unsigned int ContentionCount;
    unsigned int Flags;
    unsigned short CreatorBackTraceIndexHigh;
    unsigned short Identifier;
} CRITICAL_SECTION_DEBUG;

typedef struct CRITICAL_SECTION {
    struct CRITICAL_SECTION_DEBUG *DebugInfo;
    int LockCount;
    int RecursionCount;
    HANDLE OwningThread;
    HANDLE LockSemaphore;
    UIntPtr SpinCount;
} CRITICAL_SECTION;

extern char g_420045;
extern CRITICAL_SECTION g_4205c0;

void sub_4019cc(void)
{
    if (g_420045)
        LeaveCriticalSection(&g_4205c0.DebugInfo);
    DeleteCriticalSection(&g_4205c0.DebugInfo);
    return;
}
```

## `sub_004019ea` `0x004019ea`

_5 bytes. (leaf/helper — see body)_

```c
void sub_4019ea(unsigned int a0, unsigned int a1)
{
    sub_403374();
    return;
}
```

## `sub_004019ef` `0x004019ef`

_2 bytes. (leaf/helper — see body)_

```c
void sub_4019ef(void)
{
    sub_4019cc();
    return;
}
```

## `sub_004019f4` `0x004019f4`

_97 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
    struct struct_2 *field_4;
    int field_8;
} struct_1;

typedef struct struct_0 {
    char padding_0[4];
    struct struct_1 *field_4;
} struct_0;

typedef struct struct_2 {
    struct struct_0 *field_0;
} struct_2;

extern unsigned int g_42060c;
extern unsigned int g_420618;

int sub_4019f4(void)
{
    struct_1 *idx;  // eax
    struct_0 **v2;  // edx
    int iter;  // ecx
    struct_0 *v4;  // eax
    struct_0 *v5;  // eax

    if (idx == g_42060c)
        g_42060c = idx->field_4;
    v2 = idx->field_4;
    iter = idx->field_8;
    if (iter > 0x1000)
    {
        v5 = idx->field_0;
        *(v2) = v5;
        v5->field_4 = v2;
        return;
    }
    else if (idx == v2)
    {
        if (iter < 0)
            iter += 3;
        *((unsigned int *)(g_420618 + (iter >> 2) * 4 - 12)) = 0;
        return;
    }
    else
    {
        if (iter < 0)
            iter += 3;
        *((struct_0 ***)(g_420618 + (iter >> 2) * 4 - 12)) = v2;
        v4 = idx->field_0;
        *(v2) = v4;
        v4->field_4 = v2;
        return;
    }
}
```

## `sub_00401a55` `0x00401a55`

_3 bytes. (leaf/helper — see body)_

```c
int sub_401a55(void)
{
    return sub_401a58();
}
```

## `sub_00401a58` `0x00401a58`

_47 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_1 *field_0;
    char padding_4[4];
    unsigned int field_8;
    unsigned int field_c;
} struct_0;

typedef struct struct_1 {
    struct struct_0 *field_0;
} struct_1;

extern unsigned int g_4205bc;
extern struct_0 *g_42061c;

int sub_401a58(void)
{
    struct_0 *i;  // edx
    unsigned int v2;  // eax

    for (i = g_42061c; i != &g_42061c; i = i->field_0)
    {
        if (v2 >= i->field_8 && v2 < i->field_8 + i->field_c)
            return;
    }
    g_4205bc = 3;
    return;
}
```

## `sub_00401a87` `0x00401a87`

_1 bytes. (leaf/helper — see body)_

```c
int sub_401a87(void)
{
    sub_401a88();
    return;
}
```

## `sub_00401a88` `0x00401a88`

_48 bytes. (leaf/helper — see body)_

```c
int sub_401a88(void)
{
    int v2;  // edx
    unsigned int *v3;  // eax
    unsigned int *v4;  // ebx
    unsigned int v5;  // ecx
    int v0;  // [bp-0x4]

    v4 = -0x4 + v2 + (char *)v3;
    if (v2 >= 16)
    {
        *(v4) = 2147483655;
        sub_401c5c(v0);
        return;
    }
    if (v2 < 4)
        return;
    v5 = v2 | 2147483650;
    *(v3) = v5;
    *(v4) = v5;
    return;
}
```

## `sub_00401ab8` `0x00401ab8`

_34 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_4205ac;
extern unsigned int g_4205b0;

int sub_401ab8(void)
{
    void* v1;  // eax

    g_4205ac = g_4205ac + 1;
    g_4205b0 = g_4205b0 + ((int)v1[4] & 2147483644) - 4;
    sub_4020cc();
    return;
}
```

## `sub_00401ada` `0x00401ada`

_2 bytes. (leaf/helper — see body)_

```c
int sub_401ada(unsigned int a0, unsigned int a1)
{
    return sub_401adc();
}
```

## `sub_00401adc` `0x00401adc`

_40 bytes. (leaf/helper — see body)_

```c
int sub_401adc(void)
{
    int v1;  // edx
    unsigned int *v2;  // eax
    unsigned int *v3;  // eax

    if (v1 >= 12)
    {
        *(v2) = v1 | 2;
        sub_401ab8();
        return;
    }
    if (v1 >= 4)
        *(v3) = v1 | 2147483650;
    *((unsigned int *)((char *)v3 + v1)) = *((int *)((char *)v3 + v1)) & 4294967294;
    return;
}
```

## `sub_00401b04` `0x00401b04`

_109 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_4205bc;

int sub_401b04(void)
{
    void* v1;  // eax
    unsigned int v2;  // edx
    void* v3;  // ecx

    v2 = (int)v1[4];
    if ((v2 & 2147483650) != 2147483650)
        g_4205bc = 4;
    v3 = v1 - (v2 & 2147483644);
    if (((v2 ^ *((int *)v3)) & 4294967294))
        g_4205bc = 5;
    if (!(*((char *)v3) & 1))
        return;
    if ((int)v3[4] != *((int *)(8 + (char *)v3 - v3[4])))
        g_4205bc = 6;
    sub_4019f4();
    return;
}
```

## `sub_00401b71` `0x00401b71`

_3 bytes. (leaf/helper — see body)_

```c
int sub_401b71(void)
{
    sub_401b74();
    return;
}
```

## `sub_00401b74` `0x00401b74`

_56 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    char padding_4[4];
    unsigned int field_8;
} struct_0;

int sub_401b74(void)
{
    struct_0 *v1;  // eax
    struct_0 *iter;  // ebx
    unsigned int v3;  // eax
    struct_0 *v4;  // ebx

    iter = v1;
    v3 = iter->field_0;
    if ((v3 & 0x80000000))
    {
        iter = (char *)iter + (v3 & 2147483644);
        v3 = iter->field_0;
    }
    if (!((char)v3 & 2))
    {
        sub_4019f4();
        v4 = (char *)iter + iter->field_8;
        v4->field_0 = v4->field_0 & 4294967294;
    }
    return;
}
```

## `sub_00401bac` `0x00401bac`

_173 bytes. (leaf/helper — see body)_

```c
int sub_401bac(void)
{
    unsigned int v3[4];  // ebx
    unsigned int v5;  // eax
    unsigned int v6;  // ebp
    int v0;  // [bp-0x1c], Other Possible Types: char
    unsigned int v1;  // [bp-0x17]

    *((char *)&v0) = 0;
    v3 = sub_401a58(*((unsigned int *)&v0));
    if (!v3)
        return;
    if (v5 - v3[2] < 12)
        sub_4017c4();
    else
        sub_4017c4();
    v6 = *((unsigned int *)(&v0 + 1));
    if (!v6)
        return;
    sub_401a88();
    if (v6 + v1 < v3[2] + v3[3])
        sub_401adc();
    sub_4012d8();
    v0 = 1;
    return;
}
```

## `sub_00401c59` `0x00401c59`

_3 bytes. (leaf/helper — see body)_

```c
int sub_401c59(void)
{
    sub_401c5c();
    return;
}
```

## `sub_00401c5c` `0x00401c5c`

_133 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
    struct struct_0 *field_4;
    int field_8;
} struct_0;

extern struct_0 *g_42060c;
extern unsigned int g_420618;

int sub_401c5c(void)
{
    struct_0 *idx;  // eax
    int v2;  // edx
    int v3;  // edx
    int v4;  // edx
    struct_0 *v5;  // eax
    struct_0 *v6;  // edx
    struct_0 *v7;  // eax
    struct_0 *v8;  // edx

    idx->field_8 = v2;
    *((int *)(-0x4 + (char *)idx + v2)) = v2;
    if (v2 <= 0x1000)
    {
        v3 = v2;
        if (v3 < NULL)
            v3 += 3;
        v4 = v3 >> 2;
        v5 = *((int *)(g_420618 + v4 * 4 - 12));
        if (v5)
        {
            v6 = v5->field_0;
            idx->field_4 = v5;
            idx->field_0 = v6;
            v5->field_0 = idx;
            v6->field_4 = idx;
            return;
        }
        *((struct_0 **)(g_420618 + v4 * 4 - 12)) = idx;
        idx->field_4 = idx;
        idx->field_0 = idx;
        return;
    }
    else
    {
        if (v2 >= 0x3c00 && (char)sub_401bac())
            return;
        v7 = g_42060c;
        g_42060c = idx;
        v8 = v7->field_0;
        idx->field_4 = v7;
        idx->field_0 = v8;
        v7->field_0 = idx;
        v8->field_4 = idx;
        return;
    }
}
```

## `sub_00401ce1` `0x00401ce1`

_3 bytes. (leaf/helper — see body)_

```c
int sub_401ce1(void)
{
    return sub_401ce4();
}
```

## `sub_00401ce4` `0x00401ce4`

_74 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern unsigned int g_4205bc;
extern int g_420610;
extern struct_0 *g_420614;

unsigned int sub_401ce4(void)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax

    if (g_420610 <= 0)
    {
        return v2;
    }
    else if (g_420610 < 12)
    {
        g_4205bc = 7;
        return v1;
    }
    else
    {
        g_420614->field_0 = g_420610 | 2;
        sub_401ab8();
        g_420614 = 0;
        g_420610 = 0;
        return 0;
    }
}
```

## `sub_00401d2e` `0x00401d2e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_401d2e(void)
{
    sub_401d30();
    return;
}
```

## `sub_00401d30` `0x00401d30`

_137 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420610;
extern unsigned int g_420614;

int sub_401d30(void)
{
    unsigned int v5[2];  // eax
    int v6;  // eax
    unsigned int v7;  // esi
    unsigned int v0;  // [bp-0x1c]
    unsigned int iter;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]

    v0 = v5[0];
    iter = v5[1];
    sub_401ce4();
    sub_401264(v5[0]);
    if (!v2)
        return;
    if (v2 < v5[0])
    {
        v6 = sub_401b04();
        v0 = v5[0] - v6;
        iter += v6;
    }
    v7 = v2 + v3;
    if (v0 + iter < v7)
        iter += sub_401b74();
    if (v7 == v0 + iter)
    {
        sub_401a88();
        iter -= 4;
    }
    g_420614 = v0;
    g_420610 = iter;
    return;
}
```

## `sub_00401db9` `0x00401db9`

_3 bytes. (leaf/helper — see body)_

```c
int sub_401db9(void)
{
    sub_401dbc();
    return;
}
```

## `sub_00401dbc` `0x00401dbc`

_43 bytes. (leaf/helper — see body)_

```c
int sub_401dbc(void)
{
    unsigned int v0;  // [bp-0xc]

    sub_401610();
    if (v0 && (char)sub_401d30())
        return;
    return;
}
```

## `sub_00401de7` `0x00401de7`

_1 bytes. (leaf/helper — see body)_

```c
int sub_401de7(void)
{
    sub_401de8();
    return;
}
```

## `sub_00401de8` `0x00401de8`

_49 bytes. (leaf/helper — see body)_

```c
int sub_401de8(void)
{
    unsigned int v0;  // [bp-0x10]

    sub_4016a0();
    if (v0 && (char)sub_401d30())
        return;
    return;
}
```

## `sub_00401e19` `0x00401e19`

_3 bytes. (leaf/helper — see body)_

```c
int sub_401e19(void)
{
    sub_401e1c();
    return;
}
```

## `sub_00401e1c` `0x00401e1c`

_44 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420618;

int sub_401e1c(void)
{
    int v1;  // eax
    int v2;  // eax
    int v3;  // eax

    if (v1 < 0)
        v2 = v1 + 3;
    v3 = v2 >> 2;
    if (v3 <= 0x400)
    {
        do
        {
        } while (!*((int *)(g_420618 + v3 * 4 - 12)) && (v3 = (int)(v3 + 1), v3 != 1025));
    }
    return;
}
```

## `sub_00401e48` `0x00401e48`

_244 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    struct struct_0 *field_4;
} struct_0;

typedef struct struct_1 {
    char padding_0[8];
    int field_8;
} struct_1;

typedef struct struct_3 {
    unsigned int field_0;
} struct_3;

extern unsigned int g_4205ac;
extern unsigned int g_4205b0;
extern struct_0 *g_420604;
extern struct_1 *g_42060c;
extern unsigned int g_420610;
extern struct_3 *g_420614;

int sub_401e48(void)
{
    int v1;  // eax
    int i;  // esi
    struct_0 *iter;  // ebx
    int v4;  // eax
    unsigned int *v5;  // eax

    i = v1;
    while (true)
    {
        iter = g_420604;
        if (i > g_420604[1].field_0 && !((iter = (struct_0 *)g_42060c, v4 = g_42060c->field_8, i <= v4)))
        {
            g_42060c->field_8 = i;
            do
            {
                iter = iter->field_4;
            } while (i > iter[1].field_0);
            g_42060c->field_8 = v4;
            if (iter != g_42060c)
            {
                g_42060c = iter;
                goto LABEL_401eeb;
            }
            if (i <= 0x1000 && !((iter = (struct_0 *)sub_401e1c(), !iter)))
                goto LABEL_401eeb;
            if (!(char)sub_401dbc())
            {
                return;
            }
            else if (i <= g_420610)
            {
                g_420610 = g_420610 - i;
                if (g_420610 < 12)
                {
                    i += g_420610;
                    g_420610 = 0;
                }
                v5 = &g_420614->field_0;
                g_420614 = (char *)g_420614 + i;
                *(v5) = i | 2;
                g_4205ac = g_4205ac + 1;
                g_4205b0 = g_4205b0 + i - 4;
                return;
            }
        }
        else
        {
LABEL_401eeb:
            sub_4019f4();
            if (iter[1].field_0 - i >= 12)
            {
                sub_401c5c();
                break;
            }
            else
            {
                i = iter[1].field_0;
                if (iter == g_42060c)
                    g_42060c = iter->field_4;
                *((unsigned int *)((char *)iter + i)) = *((int *)((char *)iter + i)) & 4294967294;
                break;
            }
        }
    }
    iter->field_0 = i | 2;
    g_4205ac = g_4205ac + 1;
    g_4205b0 = g_4205b0 + i - 4;
    return;
}
```

## `sub_00401f3c` `0x00401f3c`

_370 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    struct struct_1 *field_0;
    struct struct_3 *field_4;
    unsigned int field_8;
} struct_2;

typedef struct struct_1 {
    char padding_0[4];
    struct struct_2 *field_4;
} struct_1;

typedef struct struct_3 {
    struct struct_1 *field_0;
} struct_3;

typedef struct LIST_ENTRY {
    void* Flink;
    void* Blink;
} LIST_ENTRY;

typedef struct CRITICAL_SECTION_DEBUG {
    unsigned short Type;
    unsigned short CreatorBackTraceIndex;
    void* CriticalSection;
    LIST_ENTRY ProcessLocksList;
    unsigned int EntryCount;
    unsigned int ContentionCount;
    unsigned int Flags;
    unsigned short CreatorBackTraceIndexHigh;
    unsigned short Identifier;
} CRITICAL_SECTION_DEBUG;

typedef struct CRITICAL_SECTION {
    struct CRITICAL_SECTION_DEBUG *DebugInfo;
    int LockCount;
    int RecursionCount;
    HANDLE OwningThread;
    HANDLE LockSemaphore;
    UIntPtr SpinCount;
} CRITICAL_SECTION;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern unsigned int g_4020bf;
extern char g_420045;
extern unsigned int g_4205ac;
extern unsigned int g_4205b0;
extern char g_4205b8;
extern CRITICAL_SECTION g_4205c0;
extern unsigned int g_420610;
extern struct_0 *g_420614;
extern unsigned int g_420618;

int sub_401f3c(void)
{
    unsigned int v10;  // ebx
    unsigned int v11;  // esi
    int v20;  // eax
    struct_2 *idx;  // edx
    struct_2 *v22;  // esi
    struct_1 **v23;  // eax
    int iter;  // eax
    int node;  // ecx
    struct_2 *v26;  // eax
    unsigned int *v27;  // eax
    unsigned long v28;  // 4122
    unsigned int v12;  // edi
    int v13;  // eax
    unsigned long v14;  // ldt
    unsigned long v15;  // gdt
    unsigned short v16;  // fs
    unsigned long v17;  // 4150
    unsigned long v18;  // 4154
    unsigned int v19;  // ebx
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    char *v2;  // [bp-0x1c], Other Possible Types: unsigned int
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    struct_1 *v6;  // [bp-0xc]
    int v7;  // [bp-0x8], Other Possible Types: unsigned int
    char v8;  // [bp-0x4]

    v5 = v10;
    v4 = v11;
    v3 = v12;
    if ((g_4205b8 || (char)sub_401850()) && v13 <= 2147483640)
    {
        v2 = &v8;
        v1 = sub_4020b8;
        v17 = _ccall(v14, v15, (unsigned int)v16, 0);
        v0 = *((int *)v17);
        v18 = _ccall(v14, v15, (unsigned int)v16, 0);
        *((unsigned int **)v18) = &v0;
        if (g_420045)
            EnterCriticalSection(&g_4205c0.DebugInfo);
        v19 = v13 + 7 & 0xfffffffc;
        if (v19 < 12)
            v19 = 12;
        if (v19 <= 0x1000)
        {
            v20 = v19;
            if (v20 < NULL)
                v20 += 3;
            idx = *((int *)(g_420618 + (v20 >> 2) * 4 - 12));
            if (idx)
            {
                v22 = idx;
                *((unsigned int *)((char *)v22 + v19)) = *((int *)((char *)v22 + v19)) & 4294967294;
                v23 = idx->field_4;
                if (idx == v23)
                {
                    iter = v19;
                    if (iter < NULL)
                        iter += 3;
                    *((unsigned int *)(g_420618 + (iter >> 2) * 4 - 12)) = 0;
                }
                else
                {
                    node = v19;
                    if (node < NULL)
                        node += 3;
                    *((struct_1 ***)(g_420618 + (node >> 2) * 4 - 12)) = v23;
                    v6 = idx->field_0;
                    v6->field_4 = v23;
                    *(v23) = v6;
                }
                v26 = v22;
                v26->field_0 = idx->field_8 | 2;
                v7 = &v26->field_4;
                g_4205ac = g_4205ac + 1;
                g_4205b0 = g_4205b0 + v19 - 4;
                sub_40351c();
                return;
            }
        }
        if (v19 > g_420610)
        {
            v7 = sub_401e48();
            v28 = _ccall(v14, v15, (unsigned int)v16, 0);
            *((unsigned int *)v28) = v0;
            v2 = &g_4020bf;
            sub_4020a4();
            return;
        }
        g_420610 = g_420610 - v19;
        if (g_420610 < 12)
        {
            v19 += g_420610;
            g_420610 = 0;
        }
        v27 = &g_420614->field_0;
        g_420614 = (char *)g_420614 + v19;
        *(v27) = v19 | 2;
        v7 = v27 + 1;
        g_4205ac = g_4205ac + 1;
        g_4205b0 = g_4205b0 + v19 - 4;
        sub_40351c();
        return;
    }
    v7 = 0;
    return;
}
```

## `sub_004020a4` `0x004020a4`

_20 bytes. (leaf/helper — see body)_

```c
typedef struct LIST_ENTRY {
    void* Flink;
    void* Blink;
} LIST_ENTRY;

typedef struct CRITICAL_SECTION_DEBUG {
    unsigned short Type;
    unsigned short CreatorBackTraceIndex;
    void* CriticalSection;
    LIST_ENTRY ProcessLocksList;
    unsigned int EntryCount;
    unsigned int ContentionCount;
    unsigned int Flags;
    unsigned short CreatorBackTraceIndexHigh;
    unsigned short Identifier;
} CRITICAL_SECTION_DEBUG;

typedef struct CRITICAL_SECTION {
    struct CRITICAL_SECTION_DEBUG *DebugInfo;
    int LockCount;
    int RecursionCount;
    HANDLE OwningThread;
    HANDLE LockSemaphore;
    UIntPtr SpinCount;
} CRITICAL_SECTION;

extern char g_420045;
extern CRITICAL_SECTION g_4205c0;

void sub_4020a4(void)
{
    if (g_420045)
        LeaveCriticalSection(&g_4205c0.DebugInfo);
    return;
}
```

## `sub_004020b8` `0x004020b8`

_5 bytes. (leaf/helper — see body)_

```c
void sub_4020b8(unsigned int a0, unsigned int a1)
{
    sub_403374();
    return;
}
```

## `sub_004020bd` `0x004020bd`

_2 bytes. (leaf/helper — see body)_

```c
void sub_4020bd(void)
{
    sub_4020a4();
    return;
}
```

## `sub_004020c9` `0x004020c9`

_3 bytes. (leaf/helper — see body)_

```c
int sub_4020c9(void)
{
    sub_4020cc();
    return;
}
```

## `sub_004020cc` `0x004020cc`

_391 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    int field_8;
} struct_0;

typedef struct LIST_ENTRY {
    void* Flink;
    void* Blink;
} LIST_ENTRY;

typedef struct CRITICAL_SECTION_DEBUG {
    unsigned short Type;
    unsigned short CreatorBackTraceIndex;
    void* CriticalSection;
    LIST_ENTRY ProcessLocksList;
    unsigned int EntryCount;
    unsigned int ContentionCount;
    unsigned int Flags;
    unsigned short CreatorBackTraceIndexHigh;
    unsigned short Identifier;
} CRITICAL_SECTION_DEBUG;

typedef struct CRITICAL_SECTION {
    struct CRITICAL_SECTION_DEBUG *DebugInfo;
    int LockCount;
    int RecursionCount;
    HANDLE OwningThread;
    HANDLE LockSemaphore;
    UIntPtr SpinCount;
} CRITICAL_SECTION;

extern unsigned int g_402265;
extern char g_420045;
extern unsigned int g_4205ac;
extern unsigned int g_4205b0;
extern char g_4205b8;
extern unsigned int g_4205bc;
extern CRITICAL_SECTION g_4205c0;
extern int g_420610;
extern unsigned int g_420614;

int sub_4020cc(void)
{
    unsigned int v9;  // ecx
    unsigned int v10;  // ebx
    void* v19;  // esi
    unsigned int v20;  // ebx
    int v21;  // edx
    void* v22;  // eax
    unsigned int v23;  // ebx
    struct_0 *v24;  // edi
    struct_0 *v25;  // eax
    unsigned long v26;  // 4124
    unsigned int v11;  // esi
    unsigned int v12;  // edi
    unsigned long v13;  // ldt
    unsigned long v14;  // gdt
    unsigned short v15;  // fs
    unsigned long v16;  // 4150
    unsigned long v17;  // 4154
    void* v18;  // eax
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    char *v2;  // [bp-0x18], Other Possible Types: unsigned int
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = v9;
    v5 = v10;
    v4 = v11;
    v3 = v12;
    g_4205bc = 0;
    if (!g_4205b8 && !(char)sub_401850())
    {
        g_4205bc = 8;
        v6 = 8;
        return;
    }
    v2 = &v7;
    v1 = sub_40225e;
    v16 = _ccall(v13, v14, (unsigned int)v15, 0);
    v0 = *((int *)v16);
    v17 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int **)v17) = &v0;
    if (g_420045)
        EnterCriticalSection(&g_4205c0.DebugInfo);
    v19 = v18 - 4;
    v20 = *((int *)v19);
    if (!((char)v20 & 2))
    {
        g_4205bc = 9;
    }
    else
    {
        g_4205ac = g_4205ac - 1;
        g_4205b0 = g_4205b0 - ((v20 & 2147483644) - 4);
        if (((char)v20 & 1))
        {
            v21 = (int)v19[4];
            if (v21 < 12 || (v21 & 2147483651))
            {
                g_4205bc = 10;
            }
            else
            {
                v22 = v19 - v21;
                if (v21 != (int)v22[8])
                {
                    g_4205bc = 10;
                }
                else
                {
                    v20 += v21;
                    v19 = v22;
                    sub_4019f4();
                    goto LABEL_4021a0;
                }
            }
        }
        else
        {
LABEL_4021a0:
            v23 = v20 & 2147483644;
            v24 = v19 + v23;
            if (v24 == g_420614)
            {
                g_420614 = g_420614 - v23;
                g_420610 = g_420610 + v23;
                if (g_420610 > 0x3c00)
                    sub_401ce4();
                v6 = 0;
                sub_40351c();
                return;
            }
            if (!((char)v24->field_0 & 2))
            {
                v25 = v24;
                if (!v25->field_4 || !v25->field_0 || v25->field_8 < 12)
                {
                    g_4205bc = 11;
                }
                else
                {
                    sub_4019f4();
LABEL_40222c:
                    sub_401c5c();
                }
            }
            else if ((v24->field_0 & 2147483644) < 4)
            {
                g_4205bc = 11;
            }
            else
            {
                v24->field_0 = v24->field_0 | 1;
                goto LABEL_40222c;
            }
        }
    }
    v6 = g_4205bc;
    v26 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int *)v26) = v0;
    v2 = &g_402265;
    sub_40224a();
    return;
}
```

## `sub_0040224a` `0x0040224a`

_20 bytes. (leaf/helper — see body)_

```c
typedef struct LIST_ENTRY {
    void* Flink;
    void* Blink;
} LIST_ENTRY;

typedef struct CRITICAL_SECTION_DEBUG {
    unsigned short Type;
    unsigned short CreatorBackTraceIndex;
    void* CriticalSection;
    LIST_ENTRY ProcessLocksList;
    unsigned int EntryCount;
    unsigned int ContentionCount;
    unsigned int Flags;
    unsigned short CreatorBackTraceIndexHigh;
    unsigned short Identifier;
} CRITICAL_SECTION_DEBUG;

typedef struct CRITICAL_SECTION {
    struct CRITICAL_SECTION_DEBUG *DebugInfo;
    int LockCount;
    int RecursionCount;
    HANDLE OwningThread;
    HANDLE LockSemaphore;
    UIntPtr SpinCount;
} CRITICAL_SECTION;

extern char g_420045;
extern CRITICAL_SECTION g_4205c0;

void sub_40224a(void)
{
    if (g_420045)
        LeaveCriticalSection(&g_4205c0.DebugInfo);
    return;
}
```

## `sub_0040225e` `0x0040225e`

_5 bytes. (leaf/helper — see body)_

```c
void sub_40225e(unsigned int a0, unsigned int a1)
{
    sub_403374();
    return;
}
```

## `sub_00402263` `0x00402263`

_2 bytes. (leaf/helper — see body)_

```c
void sub_402263(void)
{
    sub_40224a();
    return;
}
```

## `sub_0040226e` `0x0040226e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40226e(unsigned int a0, unsigned int a1)
{
    return sub_402270();
}
```

## `sub_00402270` `0x00402270`

_463 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_4205b0;
extern unsigned int g_420610;
extern unsigned int g_420614;

int sub_402270(void)
{
    unsigned int v3;  // edx
    unsigned int iter;  // esi
    void* v5;  // eax
    void* v6;  // ebp
    unsigned int v7;  // edi
    void* v8;  // ebx
    void* v9;  // ebx
    void* idx;  // edx
    int v0;  // [bp-0x18]
    int v1;  // [bp-0x14], Other Possible Types: unsigned int

    iter = v3 + 7 & 0xfffffffc;
    if (iter < 12)
        iter = 12;
    v6 = v5 - 4;
    v7 = *((int *)v6) & 2147483644;
    v8 = v6 + v7;
    if (v7 >= iter)
    {
        v0 = v7 - iter;
        if (v8 == g_420614)
        {
            g_420614 = g_420614 - (v7 - iter);
            g_420610 = g_420610 + v7 - iter;
            if (g_420610 < 12)
            {
                g_420614 = g_420614 + v7 - iter;
                g_420610 = g_420610 - (v7 - iter);
                iter = v7;
            }
        }
        else
        {
            v9 = v8;
            if (!(*((char *)v9) & 2))
            {
                v0 = v7 - iter + (int)v9[8];
                sub_4019f4(v7 - iter + (int)v9[8]);
            }
            if (v0 >= 12)
            {
                *((unsigned int *)((char *)v6 + iter)) = v0 | 2;
                sub_401ab8();
            }
            else
            {
                iter = v7;
            }
        }
    }
    else
    {
        while (true)
        {
            v1 = iter - v7;
            if (v8 == g_420614)
            {
                if (g_420610 >= v1)
                {
                    g_420610 = g_420610 - v1;
                    g_420614 = g_420614 + v1;
                    if (g_420610 < 12)
                    {
                        g_420614 = g_420614 + g_420610;
                        iter += g_420610;
                        g_420610 = 0;
                    }
                    g_4205b0 = g_4205b0 + iter - v7;
                    *((unsigned int *)v6) = iter | *((int *)v6) & 2147483651;
                    return;
                }
                sub_401ce4();
                v8 = v6 + v7;
            }
            if (!(*((char *)v8) & 2))
            {
                idx = v8;
                if ((int)idx[8] < v1)
                {
                    v8 = idx + (int)idx[8];
                    v1 -= (int)idx[8];
                }
                else
                {
                    sub_4019f4((int)idx[8]);
                    if ((int)idx[8] - v1 >= 12)
                    {
                        sub_401c5c((int)idx[8] - v1);
                        break;
                    }
                    else
                    {
                        iter += (int)idx[8] - v1;
                        *((unsigned int *)((char *)v6 + iter)) = *((int *)((char *)v6 + iter)) & 4294967294;
                        break;
                    }
                }
            }
            if (!(*((int *)v8) & 0x80000000) || !(char)sub_401de8())
                return;
            v8 = v6 + v7;
        }
    }
    g_4205b0 = g_4205b0 + iter - v7;
    *((unsigned int *)v6) = iter | *((int *)v6) & 2147483651;
    return;
}
```

## `sub_0040243f` `0x0040243f`

_1 bytes. (leaf/helper — see body)_

```c
int sub_40243f(void)
{
    sub_402440();
    return;
}
```

## `sub_00402440` `0x00402440`

_166 bytes. (leaf/helper — see body)_

```c
typedef struct LIST_ENTRY {
    void* Flink;
    void* Blink;
} LIST_ENTRY;

typedef struct CRITICAL_SECTION_DEBUG {
    unsigned short Type;
    unsigned short CreatorBackTraceIndex;
    void* CriticalSection;
    LIST_ENTRY ProcessLocksList;
    unsigned int EntryCount;
    unsigned int ContentionCount;
    unsigned int Flags;
    unsigned short CreatorBackTraceIndexHigh;
    unsigned short Identifier;
} CRITICAL_SECTION_DEBUG;

typedef struct CRITICAL_SECTION {
    struct CRITICAL_SECTION_DEBUG *DebugInfo;
    int LockCount;
    int RecursionCount;
    HANDLE OwningThread;
    HANDLE LockSemaphore;
    UIntPtr SpinCount;
} CRITICAL_SECTION;

extern unsigned int g_4024f8;
extern char g_420045;
extern char g_4205b8;
extern CRITICAL_SECTION g_4205c0;

int sub_402440(void)
{
    unsigned int v5;  // ecx
    unsigned long v6;  // ldt
    void* v14;  // eax
    unsigned long v15;  // 4118
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4150
    unsigned int v10;  // 4103
    unsigned long v11;  // 4154
    int v12;  // edi
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x18]
    int v2;  // [bp-0x8], Other Possible Types: unsigned int
    char v3;  // [bp-0x4]

    v2 = v5;
    if (!g_4205b8 && !(char)sub_401850())
    {
        v2 = 0;
        return;
    }
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v10 = *((int *)v9);
    v0 = *((int *)v9);
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v0;
    if (g_420045)
        EnterCriticalSection(&g_4205c0.DebugInfo);
    if ((char)sub_402270(v10, sub_4024f1, &v3))
    {
        v2 = v14;
    }
    else
    {
        v12 = sub_401f3c();
        if (v12)
        {
            sub_402628();
            sub_4020cc();
        }
        v2 = v12;
    }
    v15 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v15) = v10;
    v1 = &g_4024f8;
    sub_4024dd();
    return;
}
```

