# elfbot.dll decompiled — loader 0x00405362..0x0040578f

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_00405362` `0x00405362`

_2 bytes. (leaf/helper — see body)_

```c
HMODULE sub_405362(void)
{
    PSTR v0;  // [bp+0x0]
    HANDLE v1;  // [bp+0x4]
    enum LOAD_LIBRARY_FLAGS v2;  // [bp+0x8]

    return LoadLibraryExA(v0, v1, v2);
}
```

## `sub_0040536a` `0x0040536a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40536a(void)
{
    return sub_40536c();
}
```

## `sub_0040536c` `0x0040536c`

_6 bytes. (leaf/helper — see body)_

```c
HGLOBAL sub_40536c(UIntPtr a0, unsigned int a1)
{
    enum GLOBAL_ALLOC_FLAGS v0;  // [bp+0x0]

    return ::kernel32.dll::LocalAlloc(v0, a0);
}
```

## `sub_00405372` `0x00405372`

_2 bytes. (leaf/helper — see body)_

```c
HLOCAL sub_405372(void)
{
    HLOCAL v0;  // [bp+0x0]

    return LocalFree(v0);
}
```

## `sub_0040537a` `0x0040537a`

_2 bytes. (leaf/helper — see body)_

```c
void* sub_40537a(void)
{
    HANDLE v0;  // [bp+0x0]
    enum FILE_MAP v1;  // [bp+0x4]
    unsigned int v2;  // [bp+0x8]
    unsigned int v3;  // [bp+0xc]
    UIntPtr v4;  // [bp+0x10]

    return MapViewOfFile(v0, v1, v2, v3, v4);
}
```

## `sub_00405382` `0x00405382`

_2 bytes. (leaf/helper — see body)_

```c
HANDLE sub_405382(void)
{
    enum SYNCHRONIZATION_ACCESS_RIGHTS v0;  // [bp+0x0]
    int v1;  // [bp+0x4]
    PSTR v2;  // [bp+0x8]

    return OpenEventA(v0, v1, v2);
}
```

## `sub_0040538a` `0x0040538a`

_2 bytes. (leaf/helper — see body)_

```c
HANDLE sub_40538a(void)
{
    unsigned int v0;  // [bp+0x0]
    int v1;  // [bp+0x4]
    PSTR v2;  // [bp+0x8]

    return OpenFileMappingA(v0, v1, v2);
}
```

## `sub_00405392` `0x00405392`

_2 bytes. (leaf/helper — see body)_

```c
HANDLE sub_405392(void)
{
    unsigned int v0;  // [bp+0x0]
    int v1;  // [bp+0x4]
    PWSTR v2;  // [bp+0x8]

    return OpenFileMappingW(v0, v1, v2);
}
```

## `sub_0040539a` `0x0040539a`

_2 bytes. (leaf/helper — see body)_

```c
HANDLE sub_40539a(void)
{
    unsigned int v0;  // [bp+0x0]
    int v1;  // [bp+0x4]
    PSTR v2;  // [bp+0x8]

    return OpenMutexA(v0, v1, v2);
}
```

## `sub_004053a2` `0x004053a2`

_2 bytes. (leaf/helper — see body)_

```c
HANDLE sub_4053a2(void)
{
    enum SYNCHRONIZATION_ACCESS_RIGHTS v0;  // [bp+0x0]
    int v1;  // [bp+0x4]
    PWSTR v2;  // [bp+0x8]

    return OpenMutexW(v0, v1, v2);
}
```

## `sub_004053aa` `0x004053aa`

_2 bytes. (leaf/helper — see body)_

```c
HANDLE sub_4053aa(void)
{
    enum PROCESS_ACCESS_RIGHTS v0;  // [bp+0x0]
    int v1;  // [bp+0x4]
    unsigned int v2;  // [bp+0x8]

    return OpenProcess(v0, v1, v2);
}
```

## `sub_004053b2` `0x004053b2`

_2 bytes. calls ReadFile_

```c
typedef struct OVERLAPPED {
    UIntPtr Internal;
    UIntPtr InternalHigh;
    char Anonymous;
    char padding_9[7];
    HANDLE hEvent;
} OVERLAPPED;

int sub_4053b2(void)
{
    HANDLE v0;  // [bp+0x0]
    Byte *v1;  // [bp+0x4]
    unsigned int v2;  // [bp+0x8]
    unsigned int *v3;  // [bp+0xc]
    OVERLAPPED *v4;  // [bp+0x10]

    return ReadFile(v0, v1, v2, v3, v4);
}
```

## `sub_004053ba` `0x004053ba`

_2 bytes. calls ReadProcessMemory_

```c
int sub_4053ba(void)
{
    HANDLE v0;  // [bp+0x0]
    void* v1;  // [bp+0x4]
    void* v2;  // [bp+0x8]
    UIntPtr v3;  // [bp+0xc]
    UIntPtr *v4;  // [bp+0x10]

    return ReadProcessMemory(v0, v1, v2, v3, v4);
}
```

## `sub_004053c2` `0x004053c2`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4053c2(void)
{
    HANDLE v0;  // [bp+0x0]

    return ReleaseMutex(v0);
}
```

## `sub_004053ca` `0x004053ca`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4053ca(void)
{
    HANDLE v0;  // [bp+0x0]

    return SetEvent(v0);
}
```

## `sub_004053d2` `0x004053d2`

_2 bytes. (leaf/helper — see body)_

```c
void sub_4053d2(void)
{
    enum WIN32_ERROR v0;  // [bp+0x0]

    SetLastError(v0);
    return;
}
```

## `sub_004053da` `0x004053da`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4053da(void)
{
    HANDLE v0;  // [bp+0x0]
    enum THREAD_PRIORITY v1;  // [bp+0x4]

    return SetThreadPriority(v0, v1);
}
```

## `sub_004053e2` `0x004053e2`

_2 bytes. (leaf/helper — see body)_

```c
void sub_4053e2(void)
{
    unsigned int v0;  // [bp+0x0]

    Sleep(v0);
    return;
}
```

## `sub_004053ea` `0x004053ea`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4053ea(void)
{
    void* v0;  // [bp+0x0]

    return UnmapViewOfFile(v0);
}
```

## `sub_004053f2` `0x004053f2`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4053f2(void)
{
    return sub_4053f4();
}
```

## `sub_004053f4` `0x004053f4`

_6 bytes. (leaf/helper — see body)_

```c
void* sub_4053f4(UIntPtr a0, enum VIRTUAL_ALLOCATION_TYPE a1, enum PAGE_PROTECTION_FLAGS a2, unsigned int a3)
{
    void* v0;  // [bp+0x0]

    return ::kernel32.dll::VirtualAlloc(v0, a0, a1, a2);
}
```

## `sub_004053fa` `0x004053fa`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4053fa(void)
{
    return sub_4053fc();
}
```

## `sub_004053fc` `0x004053fc`

_6 bytes. (leaf/helper — see body)_

```c
int sub_4053fc(UIntPtr a0, enum VIRTUAL_FREE_TYPE a1, unsigned int a2)
{
    void* v0;  // [bp+0x0]

    return ::kernel32.dll::VirtualFree(v0, a0, a1);
}
```

## `sub_00405402` `0x00405402`

_2 bytes. calls VirtualProtect_

```c
int sub_405402(void)
{
    void* v0;  // [bp+0x0]
    UIntPtr v1;  // [bp+0x4]
    enum PAGE_PROTECTION_FLAGS v2;  // [bp+0x8]
    enum PAGE_PROTECTION_FLAGS *v3;  // [bp+0xc]

    return VirtualProtect(v0, v1, v2, v3);
}
```

## `sub_0040540a` `0x0040540a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40540a(void)
{
    HANDLE v0;  // [bp+0x0]
    void* v1;  // [bp+0x4]
    UIntPtr v2;  // [bp+0x8]
    enum PAGE_PROTECTION_FLAGS v3;  // [bp+0xc]
    enum PAGE_PROTECTION_FLAGS *v4;  // [bp+0x10]

    return VirtualProtectEx(v0, v1, v2, v3, v4);
}
```

## `sub_00405412` `0x00405412`

_2 bytes. (leaf/helper — see body)_

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

UIntPtr sub_405412(void)
{
    void* v0;  // [bp+0x0]
    MEMORY_BASIC_INFORMATION *v1;  // [bp+0x4]
    UIntPtr v2;  // [bp+0x8]

    return VirtualQuery(v0, v1, v2);
}
```

## `sub_0040541a` `0x0040541a`

_2 bytes. (leaf/helper — see body)_

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

UIntPtr sub_40541a(void)
{
    HANDLE v0;  // [bp+0x0]
    void* v1;  // [bp+0x4]
    MEMORY_BASIC_INFORMATION *v2;  // [bp+0x8]
    UIntPtr v3;  // [bp+0xc]

    return VirtualQueryEx(v0, v1, v2, v3);
}
```

## `sub_00405422` `0x00405422`

_2 bytes. (leaf/helper — see body)_

```c
enum WAIT_EVENT sub_405422(void)
{
    unsigned int v0;  // [bp+0x0]
    LPArray v1;  // [bp+0x4]
    int v2;  // [bp+0x8]
    unsigned int v3;  // [bp+0xc]

    return WaitForMultipleObjects(v0, v1, v2, v3);
}
```

## `sub_0040542a` `0x0040542a`

_2 bytes. (leaf/helper — see body)_

```c
enum WAIT_EVENT sub_40542a(void)
{
    HANDLE v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x4]

    return WaitForSingleObject(v0, v1);
}
```

## `sub_00405432` `0x00405432`

_2 bytes. (leaf/helper — see body)_

```c
int sub_405432(void)
{
    return sub_405434();
}
```

## `sub_00405434` `0x00405434`

_6 bytes. calls WriteFile_

```c
typedef struct OVERLAPPED {
    UIntPtr Internal;
    UIntPtr InternalHigh;
    char Anonymous;
    char padding_9[7];
    HANDLE hEvent;
} OVERLAPPED;

int sub_405434(Byte *a0, unsigned int a1, unsigned int *a2, OVERLAPPED *a3, unsigned int a4)
{
    HANDLE v0;  // [bp+0x0]

    return ::kernel32.dll::WriteFile(v0, a0, a1, a2, a3);
}
```

## `sub_0040543a` `0x0040543a`

_2 bytes. calls WriteProcessMemory_

```c
int sub_40543a(void)
{
    HANDLE v0;  // [bp+0x0]
    void* v1;  // [bp+0x4]
    void* v2;  // [bp+0x8]
    UIntPtr v3;  // [bp+0xc]
    UIntPtr *v4;  // [bp+0x10]

    return WriteProcessMemory(v0, v1, v2, v3, v4);
}
```

## `sub_00405442` `0x00405442`

_2 bytes. (leaf/helper — see body)_

```c
PWSTR sub_405442(void)
{
    PWSTR v0;  // [bp+0x0]
    PWSTR v1;  // [bp+0x4]

    return lstrcatW(v0, v1);
}
```

## `sub_0040544a` `0x0040544a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40544a(void)
{
    PSTR v0;  // [bp+0x0]
    PSTR v1;  // [bp+0x4]

    return lstrcmpA(v0, v1);
}
```

## `sub_00405452` `0x00405452`

_2 bytes. (leaf/helper — see body)_

```c
int sub_405452(void)
{
    PSTR v0;  // [bp+0x0]
    PSTR v1;  // [bp+0x4]

    return lstrcmpiA(v0, v1);
}
```

## `sub_0040545a` `0x0040545a`

_2 bytes. (leaf/helper — see body)_

```c
PSTR sub_40545a(void)
{
    PSTR v0;  // [bp+0x0]
    PSTR v1;  // [bp+0x4]

    return lstrcpyA(v0, v1);
}
```

## `sub_00405462` `0x00405462`

_2 bytes. (leaf/helper — see body)_

```c
PWSTR sub_405462(void)
{
    PWSTR v0;  // [bp+0x0]
    PWSTR v1;  // [bp+0x4]

    return lstrcpyW(v0, v1);
}
```

## `sub_0040546a` `0x0040546a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40546a(void)
{
    PSTR v0;  // [bp+0x0]

    return lstrlenA(v0);
}
```

## `sub_00405472` `0x00405472`

_2 bytes. (leaf/helper — see body)_

```c
int sub_405472(void)
{
    PWSTR v0;  // [bp+0x0]

    return lstrlenW(v0);
}
```

## `sub_0040547a` `0x0040547a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40547a(void)
{
    return sub_40547c();
}
```

## `sub_0040547c` `0x0040547c`

_6 bytes. (leaf/helper — see body)_

```c
PSTR sub_40547c(unsigned int a0)
{
    PSTR v0;  // [bp+0x0]

    return ::user32.dll::CharNextA(v0);
}
```

## `sub_00405482` `0x00405482`

_2 bytes. (leaf/helper — see body)_

```c
HWND sub_405482(void)
{
    PSTR v0;  // [bp+0x0]
    PSTR v1;  // [bp+0x4]

    return FindWindowA(v0, v1);
}
```

## `sub_0040548a` `0x0040548a`

_2 bytes. (leaf/helper — see body)_

```c
HWND sub_40548a(void)
{
    HWND v0;  // [bp+0x0]
    HWND v1;  // [bp+0x4]
    PSTR v2;  // [bp+0x8]
    PSTR v3;  // [bp+0xc]

    return FindWindowExA(v0, v1, v2, v3);
}
```

## `sub_00405492` `0x00405492`

_2 bytes. (leaf/helper — see body)_

```c
int sub_405492(void)
{
    enum SYSTEM_METRICS_INDEX v0;  // [bp+0x0]

    return GetSystemMetrics(v0);
}
```

## `sub_0040549a` `0x0040549a`

_2 bytes. (leaf/helper — see body)_

```c
unsigned int sub_40549a(void)
{
    HWND v0;  // [bp+0x0]
    unsigned int *v1;  // [bp+0x4]

    return GetWindowThreadProcessId(v0, v1);
}
```

## `sub_004054a2` `0x004054a2`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4054a2(void)
{
    return sub_4054a4();
}
```

## `sub_004054a4` `0x004054a4`

_6 bytes. (leaf/helper — see body)_

```c
int sub_4054a4(unsigned int a0, PSTR a1, int a2, unsigned int a3)
{
    HINSTANCE v0;  // [bp+0x0]

    return ::user32.dll::LoadStringA(v0, a0, a1, a2);
}
```

## `sub_004054aa` `0x004054aa`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4054aa(void)
{
    return sub_4054ac();
}
```

## `sub_004054ac` `0x004054ac`

_6 bytes. calls MessageBoxA_

```c
enum MESSAGEBOX_RESULT sub_4054ac(PSTR a0, PSTR a1, enum MESSAGEBOX_STYLE a2, unsigned int a3)
{
    HWND v0;  // [bp+0x0]

    return ::user32.dll::MessageBoxA(v0, a0, a1, a2);
}
```

## `sub_004054b2` `0x004054b2`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4054b2(void)
{
    return sub_4054b4();
}
```

## `sub_004054b4` `0x004054b4`

_8 bytes. (leaf/helper — see body)_

```c
void sub_4054b4(void)
{
    sub_4028d0();
    return;
}
```

## `sub_004054bc` `0x004054bc`

_36 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420720;

int sub_4054bc(void)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4146
    unsigned long v10;  // 4155
    unsigned long v11;  // 4171
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    char *v2;  // [bp-0x8], Other Possible Types: unsigned int
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v2 = &v3;
    v1 = sub_4054e1;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v0 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v0;
    g_420720 = g_420720 + 1;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v0;
    v2 = sub_4054e8;
    return sub_4054e0(&v4);
}
```

## `sub_004054e0` `0x004054e0`

_1 bytes. (leaf/helper — see body)_

```c
void sub_4054e0(void)
{
    return;
}
```

## `sub_004054e1` `0x004054e1`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4054e1(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004054e6` `0x004054e6`

_2 bytes. (leaf/helper — see body)_

```c
void sub_4054e6(void)
{
    sub_4054e0();
    return;
}
```

## `sub_004054e8` `0x004054e8`

_2 bytes. (leaf/helper — see body)_

```c
void sub_4054e8(unsigned int a0)
{
    return;
}
```

## `sub_004054ea` `0x004054ea`

_10 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420720;

int sub_4054ea(void)
{
    unsigned int v1;  // eax

    g_420720 = g_420720 - 1;
    return v1;
}
```

## `sub_004054f4` `0x004054f4`

_346 bytes. refs "kernel32.dll", "CreateToolhelp32Snapshot", "Heap32ListFirst"_

```c
extern HMODULE g_420728;
extern unsigned int g_42072c;
extern unsigned int g_420730;
extern unsigned int g_420734;
extern unsigned int g_420738;
extern unsigned int g_42073c;
extern unsigned int g_420740;
extern unsigned int g_420744;
extern unsigned int g_420748;
extern unsigned int g_42074c;
extern unsigned int g_420750;
extern unsigned int g_420754;
extern unsigned int g_420758;
extern unsigned int g_42075c;
extern unsigned int g_420760;
extern unsigned int g_420764;
extern unsigned int g_420768;

unsigned int sub_4054f4(void)
{
    void* v1;  // eax

    if (!g_420728)
    {
        v1 = sub_4052bc("kernel32.dll");
        g_420728 = v1;
        if (g_420728)
        {
            g_42072c = GetProcAddress(g_420728, "CreateToolhelp32Snapshot");
            g_420730 = GetProcAddress(g_420728, "Heap32ListFirst");
            g_420734 = GetProcAddress(g_420728, "Heap32ListNext");
            g_420738 = GetProcAddress(g_420728, "Heap32First");
            g_42073c = GetProcAddress(g_420728, "Heap32Next");
            g_420740 = GetProcAddress(g_420728, "Toolhelp32ReadProcessMemory");
            g_420744 = GetProcAddress(g_420728, "Process32First");
            g_420748 = GetProcAddress(g_420728, "Process32Next");
            g_42074c = GetProcAddress(g_420728, "Process32FirstW");
            g_420750 = GetProcAddress(g_420728, "Process32NextW");
            g_420754 = GetProcAddress(g_420728, "Thread32First");
            g_420758 = GetProcAddress(g_420728, "Thread32Next");
            g_42075c = GetProcAddress(g_420728, "Module32First");
            g_420760 = GetProcAddress(g_420728, "Module32Next");
            g_420764 = GetProcAddress(g_420728, "Module32FirstW");
            v1 = GetProcAddress(g_420728, "Module32NextW");
            g_420768 = v1;
        }
    }
    if (!g_420728)
    {
        return 0;
    }
    else if (!g_42072c)
    {
        return 0;
    }
    else
    {
        return _INSERT(v1, 0, 1);
    }
}
```

## `sub_00405770` `0x00405770`

_31 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_42072c;

int sub_405770(void)
{
    unsigned int v3;  // ebx
    unsigned int v4;  // esi
    unsigned int v5;  // eax
    unsigned int v6;  // edx
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp-0x4]

    v1 = v3;
    v0 = v4;
    if ((char)sub_4054f4())
        g_42072c(v5, v6);
    return;
}
```

## `sub_0040578f` `0x0040578f`

_1 bytes. (leaf/helper — see body)_

```c
int sub_40578f(void)
{
    sub_405790();
    return;
}
```

