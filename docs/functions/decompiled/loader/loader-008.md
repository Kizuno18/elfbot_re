# elfbot.dll decompiled — loader 0x004051d4..0x0040535a

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_004051d4` `0x004051d4`

_31 bytes. (leaf/helper — see body)_

```c
typedef struct SECURITY_ATTRIBUTES {
    unsigned int nLength;
    void* lpSecurityDescriptor;
    int bInheritHandle;
} SECURITY_ATTRIBUTES;

HANDLE sub_4051d4(SECURITY_ATTRIBUTES *a0, unsigned int a1, PWSTR a2)
{
    return CreateMutexW(a0, -(a1 < 1) + 1 & 127, a2);
}
```

## `sub_004051f3` `0x004051f3`

_1 bytes. (leaf/helper — see body)_

```c
void sub_4051f3(void)
{
    sub_4051f4();
    return;
}
```

## `sub_004051f4` `0x004051f4`

_6 bytes. (leaf/helper — see body)_

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

void sub_4051f4(unsigned int a0)
{
    CRITICAL_SECTION *v0;  // [bp+0x0]

    ::kernel32.dll::DeleteCriticalSection(v0);
    return;
}
```

## `sub_004051fa` `0x004051fa`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4051fa(void)
{
    PWSTR v0;  // [bp+0x0]

    return DeleteFileW(v0);
}
```

## `sub_00405202` `0x00405202`

_2 bytes. (leaf/helper — see body)_

```c
int sub_405202(void)
{
    HANDLE v0;  // [bp+0x0]
    HANDLE v1;  // [bp+0x4]
    HANDLE v2;  // [bp+0x8]
    HANDLE *v3;  // [bp+0xc]
    unsigned int v4;  // [bp+0x10]
    int v5;  // [bp+0x14]
    enum DUPLICATE_HANDLE_OPTIONS v6;  // [bp+0x18]

    return DuplicateHandle(v0, v1, v2, v3, v4, v5, v6);
}
```

## `sub_0040520a` `0x0040520a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40520a(void)
{
    return sub_40520c();
}
```

## `sub_0040520c` `0x0040520c`

_6 bytes. (leaf/helper — see body)_

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

void sub_40520c(unsigned int a0)
{
    CRITICAL_SECTION *v0;  // [bp+0x0]

    ::kernel32.dll::EnterCriticalSection(v0);
    return;
}
```

## `sub_00405212` `0x00405212`

_2 bytes. (leaf/helper — see body)_

```c
int sub_405212(void)
{
    void* v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x4]
    unsigned int v2;  // [bp+0x8]
    unsigned int v3;  // [bp+0xc]

    return EnumCalendarInfoA(v0, v1, v2, v3);
}
```

## `sub_0040521a` `0x0040521a`

_2 bytes. (leaf/helper — see body)_

```c
unsigned int sub_40521a(void)
{
    enum FORMAT_MESSAGE_OPTIONS v0;  // [bp+0x0]
    void* v1;  // [bp+0x4]
    unsigned int v2;  // [bp+0x8]
    unsigned int v3;  // [bp+0xc]
    PSTR v4;  // [bp+0x10]
    unsigned int v5;  // [bp+0x14]
    SByte **v6;  // [bp+0x18]

    return FormatMessageA(v0, v1, v2, v3, v4, v5, v6);
}
```

## `sub_00405222` `0x00405222`

_2 bytes. (leaf/helper — see body)_

```c
int sub_405222(void)
{
    return sub_405224();
}
```

## `sub_00405224` `0x00405224`

_6 bytes. (leaf/helper — see body)_

```c
int sub_405224(unsigned int a0)
{
    HMODULE v0;  // [bp+0x0]

    return ::kernel32.dll::FreeLibrary(v0);
}
```

## `sub_0040522a` `0x0040522a`

_2 bytes. (leaf/helper — see body)_

```c
unsigned int sub_40522a(void)
{
    return GetACP();
}
```

## `sub_00405232` `0x00405232`

_2 bytes. (leaf/helper — see body)_

```c
typedef struct CPINFO {
    unsigned int MaxCharSize;
    Byte DefaultChar[2];
    Byte LeadByte[12];
} CPINFO;

int sub_405232(void)
{
    unsigned int v0;  // [bp+0x0]
    CPINFO *v1;  // [bp+0x4]

    return GetCPInfo(v0, v1);
}
```

## `sub_0040523a` `0x0040523a`

_2 bytes. (leaf/helper — see body)_

```c
unsigned int sub_40523a(void)
{
    unsigned int v0;  // [bp+0x0]
    LPArray v1;  // [bp+0x4]

    return GetCurrentDirectoryA(v0, v1);
}
```

## `sub_00405242` `0x00405242`

_2 bytes. (leaf/helper — see body)_

```c
unsigned int sub_405242(void)
{
    unsigned int v0;  // [bp+0x0]
    LPArray v1;  // [bp+0x4]

    return GetCurrentDirectoryW(v0, v1);
}
```

## `sub_0040524a` `0x0040524a`

_2 bytes. (leaf/helper — see body)_

```c
HANDLE sub_40524a(void)
{
    return GetCurrentProcess();
}
```

## `sub_00405252` `0x00405252`

_2 bytes. (leaf/helper — see body)_

```c
unsigned int sub_405252(void)
{
    return GetCurrentProcessId();
}
```

## `sub_0040525a` `0x0040525a`

_2 bytes. (leaf/helper — see body)_

```c
HANDLE sub_40525a(void)
{
    return GetCurrentThread();
}
```

## `sub_00405262` `0x00405262`

_2 bytes. (leaf/helper — see body)_

```c
unsigned int sub_405262(void)
{
    return GetCurrentThreadId();
}
```

## `sub_0040526a` `0x0040526a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40526a(void)
{
    PSTR v0;  // [bp+0x0]
    unsigned int *v1;  // [bp+0x4]
    unsigned int *v2;  // [bp+0x8]
    unsigned int *v3;  // [bp+0xc]
    unsigned int *v4;  // [bp+0x10]

    return GetDiskFreeSpaceA(v0, v1, v2, v3, v4);
}
```

## `sub_00405272` `0x00405272`

_2 bytes. (leaf/helper — see body)_

```c
int sub_405272(void)
{
    HANDLE v0;  // [bp+0x0]
    unsigned int *v1;  // [bp+0x4]

    return GetExitCodeThread(v0, v1);
}
```

## `sub_0040527a` `0x0040527a`

_2 bytes. (leaf/helper — see body)_

```c
unsigned int sub_40527a(void)
{
    PSTR v0;  // [bp+0x0]

    return GetFileAttributesA(v0);
}
```

## `sub_00405282` `0x00405282`

_2 bytes. (leaf/helper — see body)_

```c
unsigned int sub_405282(void)
{
    PWSTR v0;  // [bp+0x0]

    return GetFileAttributesW(v0);
}
```

## `sub_0040528a` `0x0040528a`

_2 bytes. (leaf/helper — see body)_

```c
unsigned int sub_40528a(void)
{
    HANDLE v0;  // [bp+0x0]
    unsigned int *v1;  // [bp+0x4]

    return GetFileSize(v0, v1);
}
```

## `sub_00405292` `0x00405292`

_2 bytes. (leaf/helper — see body)_

```c
enum WIN32_ERROR sub_405292(void)
{
    return GetLastError();
}
```

## `sub_0040529a` `0x0040529a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40529a(void)
{
    return sub_40529c();
}
```

## `sub_0040529c` `0x0040529c`

_6 bytes. (leaf/helper — see body)_

```c
int sub_40529c(unsigned int a0, LPArray a1, int a2, unsigned int a3)
{
    unsigned int v0;  // [bp+0x0]

    return ::kernel32.dll::GetLocaleInfoA(v0, a0, a1, a2);
}
```

## `sub_004052a2` `0x004052a2`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4052a2(void)
{
    return sub_4052a4();
}
```

## `sub_004052a4` `0x004052a4`

_6 bytes. (leaf/helper — see body)_

```c
unsigned int sub_4052a4(LPArray a0, unsigned int a1, unsigned int a2)
{
    HMODULE v0;  // [bp+0x0]

    return ::kernel32.dll::GetModuleFileNameA(v0, a0, a1);
}
```

## `sub_004052aa` `0x004052aa`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4052aa(void)
{
    return sub_4052ac();
}
```

## `sub_004052ac` `0x004052ac`

_6 bytes. (leaf/helper — see body)_

```c
unsigned int sub_4052ac(LPArray a0, unsigned int a1, unsigned int a2)
{
    HMODULE v0;  // [bp+0x0]

    return ::kernel32.dll::GetModuleFileNameA(v0, a0, a1);
}
```

## `sub_004052b2` `0x004052b2`

_2 bytes. (leaf/helper — see body)_

```c
unsigned int sub_4052b2(void)
{
    HMODULE v0;  // [bp+0x0]
    LPArray v1;  // [bp+0x4]
    unsigned int v2;  // [bp+0x8]

    return GetModuleFileNameW(v0, v1, v2);
}
```

## `sub_004052ba` `0x004052ba`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4052ba(void)
{
    return sub_4052bc();
}
```

## `sub_004052bc` `0x004052bc`

_6 bytes. (leaf/helper — see body)_

```c
HMODULE sub_4052bc(unsigned int a0)
{
    PSTR v0;  // [bp+0x0]

    return ::kernel32.dll::GetModuleHandleA(v0);
}
```

## `sub_004052c2` `0x004052c2`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4052c2(void)
{
    return sub_4052c4();
}
```

## `sub_004052c4` `0x004052c4`

_6 bytes. (leaf/helper — see body)_

```c
HMODULE sub_4052c4(unsigned int a0)
{
    PSTR v0;  // [bp+0x0]

    return ::kernel32.dll::GetModuleHandleA(v0);
}
```

## `sub_004052ca` `0x004052ca`

_2 bytes. (leaf/helper — see body)_

```c
HMODULE sub_4052ca(void)
{
    PWSTR v0;  // [bp+0x0]

    return GetModuleHandleW(v0);
}
```

## `sub_004052d2` `0x004052d2`

_2 bytes. (leaf/helper — see body)_

```c
void* sub_4052d2(void)
{
    HMODULE v0;  // [bp+0x0]
    PSTR v1;  // [bp+0x4]

    return GetProcAddress(v0, v1);
}
```

## `sub_004052da` `0x004052da`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4052da(void)
{
    return sub_4052dc();
}
```

## `sub_004052dc` `0x004052dc`

_6 bytes. (leaf/helper — see body)_

```c
HANDLE sub_4052dc(unsigned int a0)
{
    enum STD_HANDLE v0;  // [bp+0x0]

    return ::kernel32.dll::GetStdHandle(v0);
}
```

## `sub_004052e2` `0x004052e2`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4052e2(void)
{
    unsigned int v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x4]
    LPArray v2;  // [bp+0x8]
    int v3;  // [bp+0xc]
    LPArray v4;  // [bp+0x10]

    return GetStringTypeExA(v0, v1, v2, v3, v4);
}
```

## `sub_004052ea` `0x004052ea`

_2 bytes. (leaf/helper — see body)_

```c
unsigned int sub_4052ea(void)
{
    LPArray v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x4]

    return GetSystemDirectoryA(v0, v1);
}
```

## `sub_004052f2` `0x004052f2`

_2 bytes. (leaf/helper — see body)_

```c
unsigned int sub_4052f2(void)
{
    LPArray v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x4]

    return GetSystemDirectoryW(v0, v1);
}
```

## `sub_004052fa` `0x004052fa`

_2 bytes. (leaf/helper — see body)_

```c
unsigned int sub_4052fa(void)
{
    unsigned int v0;  // [bp+0x0]
    LPArray v1;  // [bp+0x4]

    return GetTempPathW(v0, v1);
}
```

## `sub_00405302` `0x00405302`

_2 bytes. (leaf/helper — see body)_

```c
typedef struct CONTEXT {
    enum CONTEXT_FLAGS ContextFlags;
    unsigned int Dr0;
    unsigned int Dr1;
    unsigned int Dr2;
    unsigned int Dr3;
    unsigned int Dr6;
    unsigned int Dr7;
    FLOATING_SAVE_AREA FloatSave;
    unsigned int SegGs;
    unsigned int SegFs;
    unsigned int SegEs;
    unsigned int SegDs;
    unsigned int Edi;
    unsigned int Esi;
    unsigned int Ebx;
    unsigned int Edx;
    unsigned int Ecx;
    unsigned int Eax;
    unsigned int Ebp;
    unsigned int Eip;
    unsigned int SegCs;
    unsigned int EFlags;
    unsigned int Esp;
    unsigned int SegSs;
    Byte ExtendedRegisters[512];
} CONTEXT;

typedef struct FLOATING_SAVE_AREA {
    unsigned int ControlWord;
    unsigned int StatusWord;
    unsigned int TagWord;
    unsigned int ErrorOffset;
    unsigned int ErrorSelector;
    unsigned int DataOffset;
    unsigned int DataSelector;
    Byte RegisterArea[80];
    unsigned int Spare0;
} FLOATING_SAVE_AREA;

int sub_405302(void)
{
    HANDLE v0;  // [bp+0x0]
    CONTEXT *v1;  // [bp+0x4]

    return GetThreadContext(v0, v1);
}
```

## `sub_0040530a` `0x0040530a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40530a(void)
{
    return sub_40530c();
}
```

## `sub_0040530c` `0x0040530c`

_6 bytes. (leaf/helper — see body)_

```c
unsigned int sub_40530c(void)
{
    return ::kernel32.dll::GetThreadLocale();
}
```

## `sub_00405312` `0x00405312`

_2 bytes. (leaf/helper — see body)_

```c
unsigned int sub_405312(void)
{
    return GetTickCount();
}
```

## `sub_0040531a` `0x0040531a`

_2 bytes. (leaf/helper — see body)_

```c
unsigned int sub_40531a(void)
{
    return GetVersion();
}
```

## `sub_00405322` `0x00405322`

_2 bytes. (leaf/helper — see body)_

```c
typedef struct OSVERSIONINFOA {
    unsigned int dwOSVersionInfoSize;
    unsigned int dwMajorVersion;
    unsigned int dwMinorVersion;
    unsigned int dwBuildNumber;
    unsigned int dwPlatformId;
    CHAR szCSDVersion[128];
} OSVERSIONINFOA;

int sub_405322(void)
{
    OSVERSIONINFOA *v0;  // [bp+0x0]

    return GetVersionExA(v0);
}
```

## `sub_0040532a` `0x0040532a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40532a(void)
{
    return sub_40532c();
}
```

## `sub_0040532c` `0x0040532c`

_6 bytes. (leaf/helper — see body)_

```c
typedef struct OSVERSIONINFOA {
    unsigned int dwOSVersionInfoSize;
    unsigned int dwMajorVersion;
    unsigned int dwMinorVersion;
    unsigned int dwBuildNumber;
    unsigned int dwPlatformId;
    CHAR szCSDVersion[128];
} OSVERSIONINFOA;

int sub_40532c(unsigned int a0)
{
    OSVERSIONINFOA *v0;  // [bp+0x0]

    return ::kernel32.dll::GetVersionExA(v0);
}
```

## `sub_00405332` `0x00405332`

_2 bytes. (leaf/helper — see body)_

```c
typedef struct OSVERSIONINFOW {
    unsigned int dwOSVersionInfoSize;
    unsigned int dwMajorVersion;
    unsigned int dwMinorVersion;
    unsigned int dwBuildNumber;
    unsigned int dwPlatformId;
    Char szCSDVersion[128];
} OSVERSIONINFOW;

int sub_405332(void)
{
    OSVERSIONINFOW *v0;  // [bp+0x0]

    return GetVersionExW(v0);
}
```

## `sub_0040533a` `0x0040533a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40533a(void)
{
    return sub_40533c();
}
```

## `sub_0040533c` `0x0040533c`

_6 bytes. (leaf/helper — see body)_

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

void sub_40533c(unsigned int a0)
{
    CRITICAL_SECTION *v0;  // [bp+0x0]

    ::kernel32.dll::InitializeCriticalSection(v0);
    return;
}
```

## `sub_00405342` `0x00405342`

_2 bytes. (leaf/helper — see body)_

```c
int sub_405342(void)
{
    void* v0;  // [bp+0x0]
    UIntPtr v1;  // [bp+0x4]

    return IsBadReadPtr(v0, v1);
}
```

## `sub_0040534a` `0x0040534a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40534a(void)
{
    return sub_40534c();
}
```

## `sub_0040534c` `0x0040534c`

_6 bytes. (leaf/helper — see body)_

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

void sub_40534c(unsigned int a0)
{
    CRITICAL_SECTION *v0;  // [bp+0x0]

    ::kernel32.dll::LeaveCriticalSection(v0);
    return;
}
```

## `sub_00405352` `0x00405352`

_2 bytes. (leaf/helper — see body)_

```c
HMODULE sub_405352(void)
{
    PSTR v0;  // [bp+0x0]

    return LoadLibraryA(v0);
}
```

## `sub_0040535a` `0x0040535a`

_2 bytes. (leaf/helper — see body)_

```c
HMODULE sub_40535a(void)
{
    PWSTR v0;  // [bp+0x0]

    return LoadLibraryW(v0);
}
```

