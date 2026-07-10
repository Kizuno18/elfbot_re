# elfbot.dll decompiled — loader 0x00404eeb..0x004051d2

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_00404eeb` `0x00404eeb`

_2 bytes. (leaf/helper — see body)_

```c
void sub_404eeb(void)
{
    sub_404ee5();
    return;
}
```

## `sub_00404eed` `0x00404eed`

_2 bytes. (leaf/helper — see body)_

```c
void sub_404eed(unsigned int a0)
{
    return;
}
```

## `sub_00404eef` `0x00404eef`

_1 bytes. (leaf/helper — see body)_

```c
void sub_404eef(void)
{
    sub_404ef0();
    return;
}
```

## `sub_00404ef0` `0x00404ef0`

_115 bytes. (leaf/helper — see body)_

```c
extern char g_41e008;
extern unsigned int g_420000;
extern unsigned int g_420030;
extern unsigned int g_420038;
extern unsigned int g_42003c;
extern char g_420046;
extern unsigned short g_42004c;
extern unsigned short g_420218;
extern unsigned short g_4203e4;
extern unsigned int g_4205b4;

int sub_404ef0(void)
{
    unsigned int v1;  // 4098
    unsigned int v2;  // eax

    v1 = g_4205b4;
    g_4205b4 = g_4205b4 - 1;
    if (v1 >= 1)
        return v2;
    g_41e008 = 2;
    g_420046 = 2;
    g_420000 = sub_40448c;
    if ((char)sub_402cc0())
        sub_402cf0();
    sub_402db4();
    g_42004c = 55216;
    g_420218 = 55216;
    g_4203e4 = 55216;
    sub_40444c();
    g_42003c = GetCommandLineA();
    g_420038 = sub_401160();
    g_420030 = sub_401158();
    return g_420030;
}
```

## `sub_00404f63` `0x00404f63`

_1 bytes. (leaf/helper — see body)_

```c
HMODULE sub_404f63(void)
{
    PSTR v0;  // [bp+0x0]

    return GetModuleHandleA(v0);
}
```

## `sub_00404f6a` `0x00404f6a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_404f6a(void)
{
    return sub_404f6c();
}
```

## `sub_00404f6c` `0x00404f6c`

_6 bytes. (leaf/helper — see body)_

```c
HGLOBAL sub_404f6c(UIntPtr a0, unsigned int a1)
{
    enum GLOBAL_ALLOC_FLAGS v0;  // [bp+0x0]

    return ::kernel32.dll::LocalAlloc(v0, a0);
}
```

## `sub_00404f72` `0x00404f72`

_2 bytes. (leaf/helper — see body)_

```c
void* sub_404f72(void)
{
    unsigned int v0;  // [bp+0x0]

    return TlsGetValue(v0);
}
```

## `sub_00404f7a` `0x00404f7a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_404f7a(void)
{
    unsigned int v0;  // [bp+0x0]
    void* v1;  // [bp+0x4]

    return TlsSetValue(v0, v1);
}
```

## `sub_00404f82` `0x00404f82`

_2 bytes. (leaf/helper — see body)_

```c
int sub_404f82(void)
{
    sub_404f84();
    return;
}
```

## `sub_00404f84` `0x00404f84`

_9 bytes. (leaf/helper — see body)_

```c
int sub_404f84(void)
{
    unsigned int v1;  // eax

    sub_404f6c(0x40, v1);
    return;
}
```

## `sub_00404f8d` `0x00404f8d`

_3 bytes. (leaf/helper — see body)_

```c
int sub_404f8d(void)
{
    return sub_404f90();
}
```

## `sub_00404f90` `0x00404f90`

_6 bytes. (leaf/helper — see body)_

```c
unsigned int sub_404f90(void)
{
    return 8;
}
```

## `sub_00404f96` `0x00404f96`

_2 bytes. (leaf/helper — see body)_

```c
int sub_404f96(void)
{
    return sub_404f98();
}
```

## `sub_00404f98` `0x00404f98`

_68 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420708;

int sub_404f98(void)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax

    v1 = sub_404f90();
    if (!v1)
        return v1;
    if (g_420708 == 4294967295)
        sub_403a04();
    v2 = sub_404f84();
    return (!v2 ? sub_403a04() : TlsSetValue(g_420708, v2));
}
```

## `sub_00404fdc` `0x00404fdc`

_64 bytes. (leaf/helper — see body)_

```c
extern char g_420704;
extern unsigned int g_420708;
extern unsigned int g_420718;

void* sub_404fdc(void)
{
    unsigned long v1;  // ldt
    unsigned long v2;  // gdt
    unsigned short v3;  // fs
    unsigned long v4;  // 4106
    void* v5;  // eax
    void* v6;  // eax

    if (!g_420704)
    {
        v4 = _ccall(v1, v2, (unsigned int)v3, 44);
        return *((int *)(*((int *)v4) + g_420708 * 4));
    }
    v5 = TlsGetValue(g_420708);
    if (v5)
        return v5;
    sub_404f98();
    v6 = TlsGetValue(g_420708);
    if (!v6)
        return g_420718;
    return v6;
}
```

## `sub_0040501c` `0x0040501c`

_11 bytes. (leaf/helper — see body)_

```c
int sub_40501c(void)
{
    return sub_404d80();
}
```

## `sub_00405027` `0x00405027`

_1 bytes. (leaf/helper — see body)_

```c
int sub_405027(void)
{
    sub_405028();
    return;
}
```

## `sub_00405028` `0x00405028`

_65 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_41e088;
extern unsigned int g_41e08c;
extern unsigned int g_41e090;
extern unsigned int g_420708;
extern unsigned int g_420710;

int sub_405028(void)
{
    g_420708 = 0;
    g_420710 = GetModuleHandleA(NULL);
    g_41e088 = g_420710;
    g_41e08c = 0;
    g_41e090 = 0;
    sub_40501c();
    sub_40377c();
    return;
}
```

## `sub_00405069` `0x00405069`

_39 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420714;

int sub_405069(void)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4149
    unsigned long v8;  // 4158
    unsigned long v9;  // 4174
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v2 = &/* unsupported instruction */;
    v1 = sub_405091;
    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v0 = *((int *)v7);
    v8 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v8) = &v0;
    g_420714 = g_420714 + 1;
    v9 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v9) = v0;
    v2 = sub_405098;
    return sub_405090(/* unsupported instruction */);
}
```

## `sub_00405090` `0x00405090`

_1 bytes. (leaf/helper — see body)_

```c
void sub_405090(void)
{
    return;
}
```

## `sub_00405091` `0x00405091`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_405091(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00405096` `0x00405096`

_2 bytes. (leaf/helper — see body)_

```c
void sub_405096(void)
{
    sub_405090();
    return;
}
```

## `sub_00405098` `0x00405098`

_2 bytes. (leaf/helper — see body)_

```c
void sub_405098(unsigned int a0)
{
    return;
}
```

## `sub_0040509a` `0x0040509a`

_10 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420714;

int sub_40509a(void)
{
    unsigned int v1;  // eax

    g_420714 = g_420714 - 1;
    return v1;
}
```

## `sub_004050a4` `0x004050a4`

_36 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_42071c;

int sub_4050a4(void)
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
    v1 = sub_4050c9;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v0 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v0;
    g_42071c = g_42071c + 1;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v0;
    v2 = sub_4050d0;
    return sub_4050c8(&v4);
}
```

## `sub_004050c8` `0x004050c8`

_1 bytes. (leaf/helper — see body)_

```c
void sub_4050c8(void)
{
    return;
}
```

## `sub_004050c9` `0x004050c9`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4050c9(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004050ce` `0x004050ce`

_2 bytes. (leaf/helper — see body)_

```c
void sub_4050ce(void)
{
    sub_4050c8();
    return;
}
```

## `sub_004050d0` `0x004050d0`

_2 bytes. (leaf/helper — see body)_

```c
void sub_4050d0(unsigned int a0)
{
    return;
}
```

## `sub_004050d2` `0x004050d2`

_10 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_42071c;

int sub_4050d2(void)
{
    unsigned int v1;  // eax

    g_42071c = g_42071c - 1;
    return v1;
}
```

## `sub_004050e2` `0x004050e2`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4050e2(void)
{
    Byte v0[6];  // [bp+0x0]
    Byte v1;  // [bp+0x4]
    unsigned int v2;  // [bp+0x8]
    unsigned int v3;  // [bp+0xc]
    unsigned int v4;  // [bp+0x10]
    unsigned int v5;  // [bp+0x14]
    unsigned int v6;  // [bp+0x18]
    unsigned int v7;  // [bp+0x1c]
    unsigned int v8;  // [bp+0x20]
    unsigned int v9;  // [bp+0x24]
    PSID *v10;  // [bp+0x28]

    return AllocateAndInitializeSid(v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10);
}
```

## `sub_004050ea` `0x004050ea`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4050ea(void)
{
    PSID v0;  // [bp+0x0]
    PSID v1;  // [bp+0x4]

    return EqualSid(v0, v1);
}
```

## `sub_004050f2` `0x004050f2`

_2 bytes. (leaf/helper — see body)_

```c
void* sub_4050f2(void)
{
    PSID v0;  // [bp+0x0]

    return FreeSid(v0);
}
```

## `sub_004050fa` `0x004050fa`

_2 bytes. (leaf/helper — see body)_

```c
unsigned int sub_4050fa(void)
{
    PSID v0;  // [bp+0x0]

    return GetLengthSid(v0);
}
```

## `sub_00405102` `0x00405102`

_2 bytes. (leaf/helper — see body)_

```c
int sub_405102(void)
{
    HANDLE v0;  // [bp+0x0]
    enum TOKEN_INFORMATION_CLASS v1;  // [bp+0x4]
    void* v2;  // [bp+0x8]
    unsigned int v3;  // [bp+0xc]
    unsigned int *v4;  // [bp+0x10]

    return GetTokenInformation(v0, v1, v2, v3, v4);
}
```

## `sub_0040510a` `0x0040510a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40510a(void)
{
    PSECURITY_DESCRIPTOR v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x4]

    return InitializeSecurityDescriptor(v0, v1);
}
```

## `sub_00405112` `0x00405112`

_2 bytes. (leaf/helper — see body)_

```c
int sub_405112(void)
{
    PSID v0;  // [bp+0x0]

    return IsValidSid(v0);
}
```

## `sub_0040511a` `0x0040511a`

_2 bytes. (leaf/helper — see body)_

```c
typedef struct LUID {
    unsigned int LowPart;
    int HighPart;
} LUID;

int sub_40511a(void)
{
    PSTR v0;  // [bp+0x0]
    PSTR v1;  // [bp+0x4]
    LUID *v2;  // [bp+0x8]

    return LookupPrivilegeValueA(v0, v1, v2);
}
```

## `sub_00405122` `0x00405122`

_2 bytes. (leaf/helper — see body)_

```c
int sub_405122(void)
{
    HANDLE v0;  // [bp+0x0]
    enum TOKEN_ACCESS_MASK v1;  // [bp+0x4]
    HANDLE *v2;  // [bp+0x8]

    return OpenProcessToken(v0, v1, v2);
}
```

## `sub_0040512a` `0x0040512a`

_2 bytes. (leaf/helper — see body)_

```c
enum WIN32_ERROR sub_40512a(void)
{
    HKEY v0;  // [bp+0x0]

    return RegCloseKey(v0);
}
```

## `sub_00405132` `0x00405132`

_2 bytes. (leaf/helper — see body)_

```c
typedef struct SECURITY_ATTRIBUTES {
    unsigned int nLength;
    void* lpSecurityDescriptor;
    int bInheritHandle;
} SECURITY_ATTRIBUTES;

enum WIN32_ERROR sub_405132(void)
{
    HKEY v0;  // [bp+0x0]
    PSTR v1;  // [bp+0x4]
    unsigned int v2;  // [bp+0x8]
    PSTR v3;  // [bp+0xc]
    enum REG_OPEN_CREATE_OPTIONS v4;  // [bp+0x10]
    enum REG_SAM_FLAGS v5;  // [bp+0x14]
    SECURITY_ATTRIBUTES *v6;  // [bp+0x18]
    HKEY *v7;  // [bp+0x1c]
    enum REG_CREATE_KEY_DISPOSITION *v8;  // [bp+0x20]

    return RegCreateKeyExA(v0, v1, v2, v3, v4, v5, v6, v7, v8);
}
```

## `sub_0040513a` `0x0040513a`

_2 bytes. (leaf/helper — see body)_

```c
enum WIN32_ERROR sub_40513a(void)
{
    HKEY v0;  // [bp+0x0]
    PSTR v1;  // [bp+0x4]

    return RegDeleteKeyA(v0, v1);
}
```

## `sub_00405142` `0x00405142`

_2 bytes. (leaf/helper — see body)_

```c
enum WIN32_ERROR sub_405142(void)
{
    HKEY v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x4]
    LPArray v2;  // [bp+0x8]
    unsigned int v3;  // [bp+0xc]

    return RegEnumKeyA(v0, v1, v2, v3);
}
```

## `sub_0040514a` `0x0040514a`

_2 bytes. (leaf/helper — see body)_

```c
enum WIN32_ERROR sub_40514a(void)
{
    HKEY v0;  // [bp+0x0]
    PSTR v1;  // [bp+0x4]
    unsigned int v2;  // [bp+0x8]
    enum REG_SAM_FLAGS v3;  // [bp+0xc]
    HKEY *v4;  // [bp+0x10]

    return RegOpenKeyExA(v0, v1, v2, v3, v4);
}
```

## `sub_00405152` `0x00405152`

_2 bytes. (leaf/helper — see body)_

```c
enum WIN32_ERROR sub_405152(void)
{
    HKEY v0;  // [bp+0x0]
    PSTR v1;  // [bp+0x4]
    unsigned int *v2;  // [bp+0x8]
    enum REG_VALUE_TYPE *v3;  // [bp+0xc]
    Byte *v4;  // [bp+0x10]
    unsigned int *v5;  // [bp+0x14]

    return RegQueryValueExA(v0, v1, v2, v3, v4, v5);
}
```

## `sub_0040515a` `0x0040515a`

_2 bytes. (leaf/helper — see body)_

```c
enum WIN32_ERROR sub_40515a(void)
{
    HKEY v0;  // [bp+0x0]
    PSTR v1;  // [bp+0x4]
    unsigned int v2;  // [bp+0x8]
    enum REG_VALUE_TYPE v3;  // [bp+0xc]
    Byte *v4;  // [bp+0x10]
    unsigned int v5;  // [bp+0x14]

    return RegSetValueExA(v0, v1, v2, v3, v4, v5);
}
```

## `sub_00405162` `0x00405162`

_2 bytes. (leaf/helper — see body)_

```c
enum WIN32_ERROR sub_405162(void)
{
    HKEY v0;  // [bp+0x0]
    PWSTR v1;  // [bp+0x4]
    unsigned int v2;  // [bp+0x8]
    enum REG_VALUE_TYPE v3;  // [bp+0xc]
    Byte *v4;  // [bp+0x10]
    unsigned int v5;  // [bp+0x14]

    return RegSetValueExW(v0, v1, v2, v3, v4, v5);
}
```

## `sub_0040516a` `0x0040516a`

_2 bytes. (leaf/helper — see body)_

```c
typedef struct ACL {
    Byte AclRevision;
    Byte Sbz1;
    unsigned short AclSize;
    unsigned short AceCount;
    unsigned short Sbz2;
} ACL;

int sub_40516a(void)
{
    PSECURITY_DESCRIPTOR v0;  // [bp+0x0]
    int v1;  // [bp+0x4]
    ACL *v2;  // [bp+0x8]
    int v3;  // [bp+0xc]

    return SetSecurityDescriptorDacl(v0, v1, v2, v3);
}
```

## `sub_00405172` `0x00405172`

_2 bytes. (leaf/helper — see body)_

```c
int sub_405172(void)
{
    HANDLE v0;  // [bp+0x0]

    return CloseHandle(v0);
}
```

## `sub_0040517a` `0x0040517a`

_2 bytes. (leaf/helper — see body)_

```c
typedef struct SECURITY_ATTRIBUTES {
    unsigned int nLength;
    void* lpSecurityDescriptor;
    int bInheritHandle;
} SECURITY_ATTRIBUTES;

HANDLE sub_40517a(void)
{
    SECURITY_ATTRIBUTES *v0;  // [bp+0x0]
    int v1;  // [bp+0x4]
    int v2;  // [bp+0x8]
    PSTR v3;  // [bp+0xc]

    return CreateEventA(v0, v1, v2, v3);
}
```

## `sub_00405182` `0x00405182`

_2 bytes. calls CreateFileA_

```c
typedef struct SECURITY_ATTRIBUTES {
    unsigned int nLength;
    void* lpSecurityDescriptor;
    int bInheritHandle;
} SECURITY_ATTRIBUTES;

HANDLE sub_405182(void)
{
    PSTR v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x4]
    enum FILE_SHARE_MODE v2;  // [bp+0x8]
    SECURITY_ATTRIBUTES *v3;  // [bp+0xc]
    enum FILE_CREATION_DISPOSITION v4;  // [bp+0x10]
    enum FILE_FLAGS_AND_ATTRIBUTES v5;  // [bp+0x14]
    HANDLE v6;  // [bp+0x18]

    return CreateFileA(v0, v1, v2, v3, v4, v5, v6);
}
```

## `sub_0040518a` `0x0040518a`

_2 bytes. (leaf/helper — see body)_

```c
typedef struct SECURITY_ATTRIBUTES {
    unsigned int nLength;
    void* lpSecurityDescriptor;
    int bInheritHandle;
} SECURITY_ATTRIBUTES;

HANDLE sub_40518a(void)
{
    PWSTR v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x4]
    enum FILE_SHARE_MODE v2;  // [bp+0x8]
    SECURITY_ATTRIBUTES *v3;  // [bp+0xc]
    enum FILE_CREATION_DISPOSITION v4;  // [bp+0x10]
    enum FILE_FLAGS_AND_ATTRIBUTES v5;  // [bp+0x14]
    HANDLE v6;  // [bp+0x18]

    return CreateFileW(v0, v1, v2, v3, v4, v5, v6);
}
```

## `sub_00405192` `0x00405192`

_2 bytes. (leaf/helper — see body)_

```c
typedef struct SECURITY_ATTRIBUTES {
    unsigned int nLength;
    void* lpSecurityDescriptor;
    int bInheritHandle;
} SECURITY_ATTRIBUTES;

HANDLE sub_405192(void)
{
    HANDLE v0;  // [bp+0x0]
    SECURITY_ATTRIBUTES *v1;  // [bp+0x4]
    enum PAGE_PROTECTION_FLAGS v2;  // [bp+0x8]
    unsigned int v3;  // [bp+0xc]
    unsigned int v4;  // [bp+0x10]
    PSTR v5;  // [bp+0x14]

    return CreateFileMappingA(v0, v1, v2, v3, v4, v5);
}
```

## `sub_0040519a` `0x0040519a`

_2 bytes. (leaf/helper — see body)_

```c
typedef struct SECURITY_ATTRIBUTES {
    unsigned int nLength;
    void* lpSecurityDescriptor;
    int bInheritHandle;
} SECURITY_ATTRIBUTES;

HANDLE sub_40519a(void)
{
    HANDLE v0;  // [bp+0x0]
    SECURITY_ATTRIBUTES *v1;  // [bp+0x4]
    enum PAGE_PROTECTION_FLAGS v2;  // [bp+0x8]
    unsigned int v3;  // [bp+0xc]
    unsigned int v4;  // [bp+0x10]
    PWSTR v5;  // [bp+0x14]

    return CreateFileMappingW(v0, v1, v2, v3, v4, v5);
}
```

## `sub_004051a2` `0x004051a2`

_2 bytes. (leaf/helper — see body)_

```c
typedef struct SECURITY_ATTRIBUTES {
    unsigned int nLength;
    void* lpSecurityDescriptor;
    int bInheritHandle;
} SECURITY_ATTRIBUTES;

HANDLE sub_4051a2(void)
{
    SECURITY_ATTRIBUTES *v0;  // [bp+0x0]
    int v1;  // [bp+0x4]
    PSTR v2;  // [bp+0x8]

    return CreateMutexA(v0, v1, v2);
}
```

## `sub_004051aa` `0x004051aa`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4051aa(unsigned int a0, unsigned int a1, unsigned int a2)
{
    return sub_4051ac();
}
```

## `sub_004051ac` `0x004051ac`

_31 bytes. (leaf/helper — see body)_

```c
typedef struct SECURITY_ATTRIBUTES {
    unsigned int nLength;
    void* lpSecurityDescriptor;
    int bInheritHandle;
} SECURITY_ATTRIBUTES;

HANDLE sub_4051ac(SECURITY_ATTRIBUTES *a0, unsigned int a1, PSTR a2)
{
    return CreateMutexA(a0, -(a1 < 1) + 1 & 127, a2);
}
```

## `sub_004051cb` `0x004051cb`

_1 bytes. (leaf/helper — see body)_

```c
typedef struct SECURITY_ATTRIBUTES {
    unsigned int nLength;
    void* lpSecurityDescriptor;
    int bInheritHandle;
} SECURITY_ATTRIBUTES;

HANDLE sub_4051cb(void)
{
    SECURITY_ATTRIBUTES *v0;  // [bp+0x0]
    int v1;  // [bp+0x4]
    PWSTR v2;  // [bp+0x8]

    return CreateMutexW(v0, v1, v2);
}
```

## `sub_004051d2` `0x004051d2`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4051d2(unsigned int a0, unsigned int a1, unsigned int a2)
{
    return sub_4051d4();
}
```

