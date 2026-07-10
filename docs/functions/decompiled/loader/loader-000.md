# elfbot.dll decompiled — loader 0x0040101c..0x00401368

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_0040101c` `0x0040101c`

_10 bytes. calls WriteFile_

```c
typedef struct OVERLAPPED {
    UIntPtr Internal;
    UIntPtr InternalHigh;
    char Anonymous;
    char padding_9[7];
    HANDLE hEvent;
} OVERLAPPED;

int sub_40101c(void)
{
    char *v4;  // esi
    char v5;  // 4097
    char v6;  // al
    unsigned int v7;  // 4109
    unsigned int *v8;  // edx
    HANDLE v9;  // ebx
    Byte *v0;  // [bp+0x0]
    unsigned int count;  // [bp+0x4]
    unsigned int *v2;  // [bp+0x8]
    OVERLAPPED *v3;  // [bp+0xc]

    v5 = *(v4);
    if (v6 || v5)
        goto LABEL_0x401021;
    v7 = _ccall(13, (unsigned int)(v6 | v5), 0, 0);
    *(v8) = *(v8) + (v6 | v5) + (v7 & 1);
    WriteFile(v9, v0, count, v2, v3);
    return;
}
```

## `sub_0040107e` `0x0040107e`

_8 bytes. (leaf/helper — see body)_

```c
void sub_40107e(unsigned int a0, unsigned int a1, LPArray a2, unsigned int a3)
{
    unsigned int v0;  // [bp+0x0]

    RaiseException(v0, a0, a1, a2);
    return;
}
```

## `sub_00401086` `0x00401086`

_8 bytes. (leaf/helper — see body)_

```c
typedef struct EXCEPTION_RECORD {
    int ExceptionCode;
    unsigned int ExceptionFlags;
    void* ExceptionRecord;
    void* ExceptionAddress;
    unsigned int NumberParameters;
    UIntPtr ExceptionInformation[15];
} EXCEPTION_RECORD;

void sub_401086(void* a0, EXCEPTION_RECORD *a1, void* a2, unsigned int a3)
{
    void* v0;  // [bp+0x0]

    RtlUnwind(v0, a0, a1, a2);
    return;
}
```

## `sub_0040108e` `0x0040108e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40108e(void)
{
    return UnhandledExceptionFilter();
}
```

## `sub_0040109e` `0x0040109e`

_2 bytes. (leaf/helper — see body)_

```c
PSTR sub_40109e(void)
{
    PSTR v0;  // [bp+0x0]

    return CharNextA(v0);
}
```

## `sub_004010a6` `0x004010a6`

_2 bytes. (leaf/helper — see body)_

```c
void sub_4010a6(void)
{
    unsigned int v0;  // [bp+0x0]

    ExitProcess(v0); /* do not return */
}
```

## `sub_004010ae` `0x004010ae`

_2 bytes. calls MessageBoxA_

```c
enum MESSAGEBOX_RESULT sub_4010ae(void)
{
    HWND v0;  // [bp+0x0]
    PSTR v1;  // [bp+0x4]
    PSTR v2;  // [bp+0x8]
    enum MESSAGEBOX_STYLE v3;  // [bp+0xc]

    return MessageBoxA(v0, v1, v2, v3);
}
```

## `sub_004010b6` `0x004010b6`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4010b6(void)
{
    HANDLE v0;  // [bp+0x0]

    return FindClose(v0);
}
```

## `sub_004010be` `0x004010be`

_2 bytes. (leaf/helper — see body)_

```c
typedef struct WIN32_FIND_DATAA {
    unsigned int dwFileAttributes;
    FILETIME ftCreationTime;
    FILETIME ftLastAccessTime;
    FILETIME ftLastWriteTime;
    unsigned int nFileSizeHigh;
    unsigned int nFileSizeLow;
    unsigned int dwReserved0;
    unsigned int dwReserved1;
    CHAR cFileName[260];
    CHAR cAlternateFileName[14];
} WIN32_FIND_DATAA;

typedef struct FILETIME {
    unsigned int dwLowDateTime;
    unsigned int dwHighDateTime;
} FILETIME;

HANDLE sub_4010be(void)
{
    PSTR v0;  // [bp+0x0]
    WIN32_FIND_DATAA *v1;  // [bp+0x4]

    return FindFirstFileA(v0, v1);
}
```

## `sub_004010c6` `0x004010c6`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4010c6(void)
{
    HMODULE v0;  // [bp+0x0]

    return FreeLibrary(v0);
}
```

## `sub_004010ce` `0x004010ce`

_2 bytes. (leaf/helper — see body)_

```c
PSTR sub_4010ce(void)
{
    return GetCommandLineA();
}
```

## `sub_004010d6` `0x004010d6`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4010d6(void)
{
    unsigned int v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x4]
    LPArray v2;  // [bp+0x8]
    int v3;  // [bp+0xc]

    return GetLocaleInfoA(v0, v1, v2, v3);
}
```

## `sub_004010de` `0x004010de`

_2 bytes. (leaf/helper — see body)_

```c
unsigned int sub_4010de(void)
{
    HMODULE v0;  // [bp+0x0]
    LPArray v1;  // [bp+0x4]
    unsigned int v2;  // [bp+0x8]

    return GetModuleFileNameA(v0, v1, v2);
}
```

## `sub_004010e6` `0x004010e6`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4010e6(void)
{
    return sub_4010e8();
}
```

## `sub_004010e8` `0x004010e8`

_6 bytes. (leaf/helper — see body)_

```c
HMODULE sub_4010e8(unsigned int a0)
{
    PSTR v0;  // [bp+0x0]

    return ::kernel32.dll::GetModuleHandleA(v0);
}
```

## `sub_004010ee` `0x004010ee`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4010ee(void)
{
    return sub_4010f0();
}
```

## `sub_004010f0` `0x004010f0`

_6 bytes. (leaf/helper — see body)_

```c
void* sub_4010f0(PSTR a0, unsigned int a1)
{
    HMODULE v0;  // [bp+0x0]

    return ::kernel32.dll::GetProcAddress(v0, a0);
}
```

## `sub_004010f6` `0x004010f6`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4010f6(void)
{
    return sub_4010f8();
}
```

## `sub_004010f8` `0x004010f8`

_6 bytes. (leaf/helper — see body)_

```c
typedef struct STARTUPINFOA {
    unsigned int cb;
    PSTR lpReserved;
    PSTR lpDesktop;
    PSTR lpTitle;
    unsigned int dwX;
    unsigned int dwY;
    unsigned int dwXSize;
    unsigned int dwYSize;
    unsigned int dwXCountChars;
    unsigned int dwYCountChars;
    unsigned int dwFillAttribute;
    enum STARTUPINFOW_FLAGS dwFlags;
    unsigned short wShowWindow;
    unsigned short cbReserved2;
    Byte *lpReserved2;
    HANDLE hStdInput;
    HANDLE hStdOutput;
    HANDLE hStdError;
} STARTUPINFOA;

void sub_4010f8(unsigned int a0)
{
    STARTUPINFOA *v0;  // [bp+0x0]

    GetStartupInfoA(v0);
    return;
}
```

## `sub_004010fe` `0x004010fe`

_2 bytes. (leaf/helper — see body)_

```c
unsigned int sub_4010fe(void)
{
    return GetThreadLocale();
}
```

## `sub_00401106` `0x00401106`

_2 bytes. (leaf/helper — see body)_

```c
int sub_401106(void)
{
    return sub_401108();
}
```

## `sub_00401108` `0x00401108`

_6 bytes. (leaf/helper — see body)_

```c
HMODULE sub_401108(HANDLE a0, enum LOAD_LIBRARY_FLAGS a1, unsigned int a2)
{
    PSTR v0;  // [bp+0x0]

    return ::kernel32.dll::LoadLibraryExA(v0, a0, a1);
}
```

## `sub_0040110e` `0x0040110e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40110e(void)
{
    HINSTANCE v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x4]
    PSTR v2;  // [bp+0x8]
    int v3;  // [bp+0xc]

    return LoadStringA(v0, v1, v2, v3);
}
```

## `sub_00401116` `0x00401116`

_2 bytes. (leaf/helper — see body)_

```c
PSTR sub_401116(void)
{
    LPArray v0;  // [bp+0x0]
    PSTR v1;  // [bp+0x4]
    int v2;  // [bp+0x8]

    return lstrcpynA(v0, v1, v2);
}
```

## `sub_0040111e` `0x0040111e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40111e(void)
{
    return sub_401120();
}
```

## `sub_00401120` `0x00401120`

_6 bytes. (leaf/helper — see body)_

```c
int sub_401120(unsigned int a0)
{
    PSTR v0;  // [bp+0x0]

    return ::kernel32.dll::lstrlenA(v0);
}
```

## `sub_00401126` `0x00401126`

_2 bytes. (leaf/helper — see body)_

```c
int sub_401126(void)
{
    return sub_401128();
}
```

## `sub_00401128` `0x00401128`

_6 bytes. (leaf/helper — see body)_

```c
enum WIN32_ERROR sub_401128(unsigned int a0)
{
    HKEY v0;  // [bp+0x0]

    return ::advapi32.dll::RegCloseKey(v0);
}
```

## `sub_0040112e` `0x0040112e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40112e(void)
{
    return sub_401130();
}
```

## `sub_00401130` `0x00401130`

_6 bytes. (leaf/helper — see body)_

```c
enum WIN32_ERROR sub_401130(PSTR a0, unsigned int a1, enum REG_SAM_FLAGS a2, HKEY *a3, unsigned int a4)
{
    HKEY v0;  // [bp+0x0]

    return ::advapi32.dll::RegOpenKeyExA(v0, a0, a1, a2, a3);
}
```

## `sub_00401136` `0x00401136`

_2 bytes. (leaf/helper — see body)_

```c
int sub_401136(void)
{
    return sub_401138();
}
```

## `sub_00401138` `0x00401138`

_6 bytes. (leaf/helper — see body)_

```c
enum WIN32_ERROR sub_401138(PSTR a0, unsigned int *a1, enum REG_VALUE_TYPE *a2, Byte *a3, unsigned int *a4, unsigned int a5)
{
    HKEY v0;  // [bp+0x0]

    return ::advapi32.dll::RegQueryValueExA(v0, a0, a1, a2, a3, a4);
}
```

## `sub_0040113e` `0x0040113e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40113e(void)
{
    unsigned int v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x4]
    LPArray v2;  // [bp+0x8]
    int v3;  // [bp+0xc]
    PSTR v4;  // [bp+0x10]
    int v5;  // [bp+0x14]
    PSTR v6;  // [bp+0x18]
    int *v7;  // [bp+0x1c]

    return WideCharToMultiByte(v0, v1, v2, v3, v4, v5, v6, v7);
}
```

## `sub_00401146` `0x00401146`

_2 bytes. (leaf/helper — see body)_

```c
int sub_401146(void)
{
    BSTR *v0;  // [bp+0x0]
    PWSTR v1;  // [bp+0x4]
    unsigned int v2;  // [bp+0x8]

    return SysReAllocStringLen(v0, v1, v2);
}
```

## `sub_0040114e` `0x0040114e`

_2 bytes. (leaf/helper — see body)_

```c
void sub_40114e(void)
{
    BSTR v0;  // [bp+0x0]

    SysFreeString(v0);
    return;
}
```

## `sub_00401156` `0x00401156`

_2 bytes. (leaf/helper — see body)_

```c
int sub_401156(void)
{
    return sub_401158();
}
```

## `sub_00401158` `0x00401158`

_6 bytes. (leaf/helper — see body)_

```c
unsigned int sub_401158(void)
{
    return ::kernel32.dll::GetCurrentThreadId();
}
```

## `sub_0040115e` `0x0040115e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40115e(void)
{
    return sub_401160();
}
```

## `sub_00401160` `0x00401160`

_34 bytes. (leaf/helper — see body)_

```c
unsigned int sub_401160(void)
{
    char v0;  // [bp-0x48]
    char v1;  // [bp-0x1c]
    unsigned short v2;  // [bp-0x18]

    sub_4010f8(&v0);
    if (!(v1 & 1))
        return 10;
    return v2;
}
```

## `sub_00401182` `0x00401182`

_2 bytes. (leaf/helper — see body)_

```c
HGLOBAL sub_401182(void)
{
    enum GLOBAL_ALLOC_FLAGS v0;  // [bp+0x0]
    UIntPtr v1;  // [bp+0x4]

    return LocalAlloc(v0, v1);
}
```

## `sub_0040118a` `0x0040118a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40118a(void)
{
    return sub_40118c();
}
```

## `sub_0040118c` `0x0040118c`

_6 bytes. (leaf/helper — see body)_

```c
HLOCAL sub_40118c(unsigned int a0)
{
    HLOCAL v0;  // [bp+0x0]

    return ::kernel32.dll::LocalFree(v0);
}
```

## `sub_00401192` `0x00401192`

_2 bytes. (leaf/helper — see body)_

```c
void* sub_401192(void)
{
    void* v0;  // [bp+0x0]
    UIntPtr v1;  // [bp+0x4]
    enum VIRTUAL_ALLOCATION_TYPE v2;  // [bp+0x8]
    enum PAGE_PROTECTION_FLAGS v3;  // [bp+0xc]

    return VirtualAlloc(v0, v1, v2, v3);
}
```

## `sub_0040119a` `0x0040119a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40119a(void)
{
    void* v0;  // [bp+0x0]
    UIntPtr v1;  // [bp+0x4]
    enum VIRTUAL_FREE_TYPE v2;  // [bp+0x8]

    return VirtualFree(v0, v1, v2);
}
```

## `sub_004011a2` `0x004011a2`

_2 bytes. (leaf/helper — see body)_

```c
typedef struct CRITICAL_SECTION {
    struct CRITICAL_SECTION_DEBUG *DebugInfo;
    int LockCount;
    int RecursionCount;
    HANDLE OwningThread;
    HANDLE LockSemaphore;
    UIntPtr SpinCount;
} CRITICAL_SECTION;

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

typedef struct LIST_ENTRY {
    void* Flink;
    void* Blink;
} LIST_ENTRY;

void sub_4011a2(void)
{
    CRITICAL_SECTION *v0;  // [bp+0x0]

    InitializeCriticalSection(v0);
    return;
}
```

## `sub_004011aa` `0x004011aa`

_2 bytes. (leaf/helper — see body)_

```c
typedef struct CRITICAL_SECTION {
    struct CRITICAL_SECTION_DEBUG *DebugInfo;
    int LockCount;
    int RecursionCount;
    HANDLE OwningThread;
    HANDLE LockSemaphore;
    UIntPtr SpinCount;
} CRITICAL_SECTION;

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

typedef struct LIST_ENTRY {
    void* Flink;
    void* Blink;
} LIST_ENTRY;

void sub_4011aa(void)
{
    CRITICAL_SECTION *v0;  // [bp+0x0]

    EnterCriticalSection(v0);
    return;
}
```

## `sub_004011b2` `0x004011b2`

_2 bytes. (leaf/helper — see body)_

```c
typedef struct CRITICAL_SECTION {
    struct CRITICAL_SECTION_DEBUG *DebugInfo;
    int LockCount;
    int RecursionCount;
    HANDLE OwningThread;
    HANDLE LockSemaphore;
    UIntPtr SpinCount;
} CRITICAL_SECTION;

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

typedef struct LIST_ENTRY {
    void* Flink;
    void* Blink;
} LIST_ENTRY;

void sub_4011b2(void)
{
    CRITICAL_SECTION *v0;  // [bp+0x0]

    LeaveCriticalSection(v0);
    return;
}
```

## `sub_004011ba` `0x004011ba`

_2 bytes. (leaf/helper — see body)_

```c
typedef struct CRITICAL_SECTION {
    struct CRITICAL_SECTION_DEBUG *DebugInfo;
    int LockCount;
    int RecursionCount;
    HANDLE OwningThread;
    HANDLE LockSemaphore;
    UIntPtr SpinCount;
} CRITICAL_SECTION;

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

typedef struct LIST_ENTRY {
    void* Flink;
    void* Blink;
} LIST_ENTRY;

void sub_4011ba(void)
{
    CRITICAL_SECTION *v0;  // [bp+0x0]

    DeleteCriticalSection(v0);
    return;
}
```

## `sub_004011c2` `0x004011c2`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4011c2(void)
{
    return sub_4011c4();
}
```

## `sub_004011c4` `0x004011c4`

_79 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
} struct_0;

typedef struct struct_3 {
    char padding_0[4];
    struct struct_0 *field_4;
} struct_3;

extern unsigned int g_4205d8;
extern struct_0 *g_4205dc;

struct_0 ** sub_4011c4(void)
{
    unsigned int *v1;  // ecx
    unsigned int i;  // edx
    struct_3 *v3;  // eax
    struct_0 **v4;  // eax

    if (!g_4205dc)
    {
        v1 = LocalAlloc(GMEM_FIXED, 0x644);
        if (!v1)
            return NULL;
        *(v1) = g_4205d8;
        g_4205d8 = v1;
        i = 0;
        do
        {
            v3 = &v1[4 * i + 1];
            *((struct_0 **)&v3->padding_0[0]) = g_4205dc;
            g_4205dc = v3;
            i += 1;
        } while (i != 100);
    }
    v4 = g_4205dc;
    g_4205dc = *(v4);
    return v4;
}
```

## `sub_00401213` `0x00401213`

_1 bytes. (leaf/helper — see body)_

```c
int sub_401213(void)
{
    sub_401214();
    return;
}
```

## `sub_00401214` `0x00401214`

_6 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
    struct struct_0 *field_4;
} struct_0;

int sub_401214(void)
{
    struct_0 *v1;  // eax

    v1->field_0 = v1;
    v1->field_4 = v1;
    return;
}
```

## `sub_0040121a` `0x0040121a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40121a(void)
{
    sub_40121c();
    return;
}
```

## `sub_0040121c` `0x0040121c`

_48 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
    struct struct_0 *field_4;
    unsigned int field_8;
    unsigned int field_c;
} struct_0;

int sub_40121c(void)
{
    struct_0 *idx;  // eax
    unsigned int v2[2];  // edx
    struct_0 *v3;  // eax
    struct_0 *v4;  // edx

    idx = sub_4011c4();
    if (idx)
    {
        idx->field_8 = v2[0];
        idx->field_c = v2[1];
        v4 = v3->field_0;
        idx->field_0 = v4;
        idx->field_4 = v3;
        v4->field_4 = idx;
        v3->field_0 = idx;
    }
    return;
}
```

## `sub_0040124c` `0x0040124c`

_24 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    struct struct_0 *field_0;
    struct struct_1 *field_4;
} struct_2;

typedef struct struct_0 {
    char padding_0[4];
    struct struct_1 *field_4;
} struct_0;

typedef struct struct_1 {
    struct struct_0 *field_0;
} struct_1;

extern struct_0 *g_4205dc;

int sub_40124c(void)
{
    struct_2 *v1;  // eax
    struct_0 **v2;  // edx
    struct_0 *v3;  // ecx

    v2 = v1->field_4;
    v3 = v1->field_0;
    *(v2) = v3;
    v3->field_4 = v2;
    v1->field_0 = g_4205dc;
    g_4205dc = v1;
    return;
}
```

## `sub_00401264` `0x00401264`

_113 bytes. (leaf/helper — see body)_

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

int sub_401264(void)
{
    struct_0 **v1;  // eax
    struct_0 *index;  // ebx
    unsigned int idx[2];  // ecx
    struct_0 **v4;  // edi

    index = *(v1);
    idx[0] = idx[0];
    idx[1] = idx[1];
    do
    {
        v4 = index->field_0;
        if (index->field_8 + index->field_c == idx[0])
        {
            sub_40124c();
            idx[0] = index->field_8;
            idx[1] = idx[1] + index->field_c;
        }
        else if (index->field_8 == idx[0] + idx[1])
        {
            sub_40124c();
            idx[1] = idx[1] + index->field_c;
        }
    } while ((index = (struct_0 *)v4, v1 != index));
    if (!(char)sub_40121c())
        idx[0] = 0;
    return;
}
```

## `sub_004012d5` `0x004012d5`

_3 bytes. (leaf/helper — see body)_

```c
int sub_4012d5(void)
{
    sub_4012d8();
    return;
}
```

## `sub_004012d8` `0x004012d8`

_143 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

int sub_4012d8(void)
{
    unsigned int v1[4];  // eax
    unsigned int v2[4];  // ebx
    unsigned int v3[4];  // ebx
    unsigned int idx[4];  // ebx
    struct_0 *index;  // edx
    unsigned int v6;  // esi
    unsigned int v7;  // eax
    unsigned int v9;  // edi
    int v10;  // ecx

    v2 = v1;
    v3 = v2;
    while (true)
    {
        idx = v3;
        v6 = (unsigned int)index->padding_0;
        v7 = idx[2];
        if (v6 >= v7 && v6 + index->field_4 <= v7 + idx[3])
            break;
        v3 = idx[0];
        if (v2 == idx[0])
            return;
    }
    if (v6 == v7)
    {
        idx[2] = idx[2] + index->field_4;
        idx[3] = idx[3] - index->field_4;
        if (!idx[3])
            sub_40124c();
    }
    else
    {
        v9 = v7 + idx[3];
        if (index->padding_0 + index->field_4 == v9)
        {
            idx[3] = idx[3] - index->field_4;
        }
        else
        {
            v10 = (int)(index->padding_0 + index->field_4);
            *((char [4])&idx[3]) = index->padding_0 - v7;
            if (!(char)sub_40121c(v10, v9 - v10))
                return;
        }
    }
    return;
}
```

## `sub_00401367` `0x00401367`

_1 bytes. (leaf/helper — see body)_

```c
int sub_401367(void)
{
    sub_401368();
    return;
}
```

## `sub_00401368` `0x00401368`

_99 bytes. (leaf/helper — see body)_

```c
int sub_401368(void)
{
    int v1;  // eax
    unsigned int v2;  // esi
    void* v3;  // edx
    void* v4;  // edi

    v2 = (v1 < 0x100000 ? 0x100000 : v1 + 0xffff & 0xffff0000);
    *((unsigned int *)&v3[4]) = v2;
    v4 = VirtualAlloc(NULL, v2, MEM_RESERVE, PAGE_NOACCESS);
    *((void* *)v3) = v4;
    if (!v4)
        return;
    if ((char)sub_40121c())
        return;
    VirtualFree(*((int *)v3), NULL, MEM_RELEASE);
    *((void* *)v3) = NULL;
    return;
}
```

