# elfbot.dll decompiled — loader 0x0041c624..0x0041d274

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_0041c624` `0x0041c624`

_85 bytes. (leaf/helper — see body)_

```c
int sub_41c624(void)
{
    unsigned int v11;  // ecx
    int v12;  // esi
    unsigned long v21;  // 4119
    int v13;  // ebx
    int v14;  // edx
    unsigned long v15;  // ldt
    unsigned long v16;  // gdt
    unsigned short v17;  // fs
    unsigned long v18;  // 4124
    unsigned int v19;  // 4103
    unsigned long v20;  // 4133
    int v0;  // [bp-0x34]
    unsigned int v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x28]
    unsigned int v4;  // [bp-0x24]
    int v5;  // [bp-0x20]
    unsigned int v6;  // [bp-0x1c]
    unsigned int v7;  // [bp-0x8]
    char v8;  // [bp-0x4]
    char v9;  // [bp+0x0]

    v7 = v11;
    sub_403e68(v12, v13, v14, &v9);
    v18 = _ccall(v15, v16, (unsigned int)v17, 0);
    v19 = *((int *)v18);
    v6 = *((int *)v18);
    v20 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int **)v20) = &v6;
    v5 = sub_403e78(v19, sub_41c682, &v8);
    v4 = 0;
    v3 = v11;
    v2 = 1;
    v1 = 1;
    v0 = sub_4179e0();
    sub_417678();
    sub_41c168();
    v21 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int *)v21) = v1;
    v3 = sub_41c689;
    sub_41c679();
    return;
}
```

## `sub_0041c679` `0x0041c679`

_9 bytes. (leaf/helper — see body)_

```c
int sub_41c679(void)
{
    return sub_403a10();
}
```

## `sub_0041c682` `0x0041c682`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_41c682(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041c687` `0x0041c687`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41c687(void)
{
    return sub_41c679();
}
```

## `sub_0041c689` `0x0041c689`

_7 bytes. (leaf/helper — see body)_

```c
int sub_41c689(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v0;  // ebx

    return v0;
}
```

## `sub_0041c6b8` `0x0041c6b8`

_439 bytes. (leaf/helper — see body)_

```c
typedef struct LUID {
    unsigned int LowPart;
    int HighPart;
} LUID;

extern unsigned int g_41c873;

int sub_41c6b8(void)
{
    unsigned int v23;  // ebx
    unsigned int v24;  // esi
    unsigned long v33;  // 4148
    void* v34;  // ebx
    int v35;  // esi
    int v36;  // esi
    unsigned int v37;  // ecx
    int v38;  // esi
    unsigned int v39;  // edi
    unsigned int v40;  // eax
    unsigned int v41;  // eax
    int v42;  // esi
    unsigned int v25;  // edi
    unsigned long v43;  // 4118
    unsigned long v44;  // 4118
    unsigned long v26;  // ldt
    unsigned long v27;  // gdt
    unsigned short v28;  // fs
    unsigned long v29;  // 4163
    unsigned long v30;  // 4172
    unsigned long v31;  // 4139
    unsigned int v32;  // 4103
    unsigned int v0;  // [bp-0x54]
    unsigned int v1;  // [bp-0x50]
    char *v2;  // [bp-0x4c], Other Possible Types: unsigned int
    unsigned int v3;  // [bp-0x48]
    unsigned int v4;  // [bp-0x44]
    char *v5;  // [bp-0x40], Other Possible Types: unsigned int
    unsigned int v6;  // [bp-0x3c]
    unsigned int v7;  // [bp-0x38]
    unsigned int v8;  // [bp-0x34]
    unsigned int v9;  // [bp-0x30]
    unsigned int v10;  // [bp-0x2c]
    unsigned int v11;  // [bp-0x28]
    LUID v12;  // [bp-0x24], Other Possible Types: char, unsigned long
    unsigned int v13;  // [bp-0x20]
    LUID v14;  // [bp-0x1c], Other Possible Types: char, unsigned long
    unsigned int v15;  // [bp-0x18]
    LUID v16;  // [bp-0x14]
    unsigned int v17;  // [bp-0x10]
    unsigned int v18;  // [bp-0xc]
    unsigned int v19;  // [bp-0xc]
    HANDLE v20;  // [bp-0x8]
    char v21;  // [bp-0x4]

    v8 = v23;
    v7 = v24;
    v6 = v25;
    v9 = 0;
    v10 = 0;
    v11 = 0;
    v5 = &v21;
    v4 = sub_41c88e;
    v29 = _ccall(v26, v27, (unsigned int)v28, 0);
    v3 = *((int *)v29);
    v30 = _ccall(v26, v27, (unsigned int)v28, 0);
    *((unsigned int **)v30) = &v3;
    if (!OpenProcessToken(GetCurrentProcess(), 40, &v20))
    {
        v44 = _ccall(v26, v27, (unsigned int)v28, 0);
        *((unsigned int *)v44) = v3;
        v5 = sub_41c895;
        return sub_41c880();
    }
    v2 = &v21;
    v1 = sub_41c86c;
    v31 = _ccall(v26, v27, (unsigned int)v28, 0);
    v32 = *((int *)v31);
    v0 = *((int *)v31);
    v33 = _ccall(v26, v27, (unsigned int)v28, 0);
    *((unsigned int **)v33) = &v0;
    v18 = 0;
    GetTokenInformation(v20, TokenPrivileges, NULL, 0, &v19);
    if (v19)
    {
        v34 = sub_40536c(0x40, v19 * 2);
        if (GetTokenInformation(v20, TokenPrivileges, v34, v19 * 2, &v19))
        {
            sub_409eac(&v16);
            if (!LookupPrivilegeValueA(NULL, sub_403e78(&v16), &v16))
            {
                v16 = (LUID)_INSERT(v16 CONCAT 0, 0, 0);
                v17 = 0;
            }
            sub_409eac(&v14);
            if (!LookupPrivilegeValueA(NULL, sub_403e78(&v14), &v14))
            {
                v14 = _INSERT(v14 CONCAT 0, 0, 0);
                v15 = 0;
            }
            sub_409eac(&v12);
            if (!LookupPrivilegeValueA(NULL, sub_403e78(&v12), &v12))
            {
                v12 = _INSERT(v12 CONCAT 0, 0, 0);
                v13 = 0;
            }
            v35 = *((int *)v34) - 1;
            if (v35 >= 0)
            {
                v36 = v35 + 1;
                v37 = 0;
                do
                {
                    v38 = v36;
                    v39 = v37 * 3;
                    if (*((int *)(8 + (char *)v34 + 4 * v39)) == v17)
                    {
                        if (*((int *)(4 + (char *)v34 + 4 * v39)) == v16.LowPart)
                            continue;
                    }
                    else
                    {
                        if (*((int *)(8 + (char *)v34 + 4 * v39)) == v17)
                            continue;
                    }
                    v40 = v37 * 3;
                    if (*((int *)(8 + (char *)v34 + 4 * v40)) == v15)
                    {
                        if (*((int *)(4 + (char *)v34 + 4 * v40)) == v14)
                            continue;
                    }
                    else
                    {
                        if (*((int *)(8 + (char *)v34 + 4 * v40)) == v15)
                            continue;
                    }
                    v41 = v37 * 3;
                    if (*((int *)(8 + (char *)v34 + 4 * v41)) == v13)
                    {
                        if (*((int *)(4 + (char *)v34 + 4 * v41)) == v12)
                            continue;
                    }
                    else
                    {
                        if (*((int *)(8 + (char *)v34 + 4 * v41)) == v13)
                            continue;
                    }
                    *((unsigned int *)(12 + (char *)v34 + 4 * v39)) = *((int *)(12 + (char *)v34 + 4 * v39)) | 2;
                } while ((v37 += 1, v42 = (int)(v38 - 1), v36 = (int)(v38 - 1), v38 != 1));
            }
            AdjustTokenPrivileges(v20, 0, v34, v19, NULL, NULL);
        }
        LocalFree(v34);
    }
    v43 = _ccall(v26, v27, (unsigned int)v28, 0);
    *((unsigned int *)v43) = v32;
    v2 = &g_41c873;
    return sub_41c862();
}
```

## `sub_0041c862` `0x0041c862`

_10 bytes. (leaf/helper — see body)_

```c
int sub_41c862(void)
{
    HANDLE v1;  // [bp+0x100000]

    return CloseHandle(v1);
}
```

## `sub_0041c86c` `0x0041c86c`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_41c86c(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041c871` `0x0041c871`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41c871(void)
{
    return sub_41c862();
}
```

## `sub_0041c880` `0x0041c880`

_14 bytes. (leaf/helper — see body)_

```c
int sub_41c880(void)
{
    return sub_403a34();
}
```

## `sub_0041c88e` `0x0041c88e`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_41c88e(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041c893` `0x0041c893`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41c893(void)
{
    return sub_41c880();
}
```

## `sub_0041c895` `0x0041c895`

_7 bytes. (leaf/helper — see body)_

```c
void sub_41c895(unsigned int a0, unsigned int a1)
{
    return;
}
```

## `sub_0041c89c` `0x0041c89c`

_111 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
} struct_0;

extern char g_41f13c;
extern unsigned int g_41f42c;
extern struct_0 *g_41f468;
extern unsigned short g_4208d8;

void sub_41c89c(void)
{
    unsigned int v3;  // ebx
    unsigned int *v4;  // ebx
    char v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x4]

    v1 = v3;
    g_41f468->field_0 = 1;
    sub_40b044();
    if (!(GetVersion() & 0x80000000))
        sub_41c6b8();
    v4 = sub_40d994();
    if (v4)
    {
        sub_4054b4();
        v4(&v0);
        g_41f13c = *((unsigned short *)&&v0) == 9;
    }
    *((void* *)g_41f42c) = sub_412278;
    g_4208d8 = 0;
    SetLastError(DNS_ERROR_RCODE_NO_ERROR);
    return;
}
```

## `sub_0041c90b` `0x0041c90b`

_1 bytes. (leaf/helper — see body)_

```c
void sub_41c90b(void)
{
    sub_41c90c();
    return;
}
```

## `sub_0041c90c` `0x0041c90c`

_119 bytes. (leaf/helper — see body)_

```c
extern char g_41f110;
extern HANDLE g_41f130;
extern char g_41f408;
extern unsigned int g_41f40c;
extern unsigned int g_420b10;
extern unsigned int g_420b28;
extern unsigned int g_420b58;

int sub_41c90c(void)
{
    unsigned int v1;  // eax

    v1 = sub_419198();
    if (g_41f110 && !g_420b28)
    {
        if (g_41f130)
        {
            CloseHandle(g_41f130);
            g_41f130 = 0;
        }
        g_41f110 = 0;
        v1 = (unsigned int)sub_4051f4(&g_420b10);
    }
    if (g_41f408)
    {
        g_41f408 = 0;
        v1 = (unsigned int)sub_4051f4(&g_420b58);
    }
    if (g_41f40c)
        v1 = UnmapViewOfFile(g_41f40c);
    return v1;
}
```

## `sub_0041c983` `0x0041c983`

_1 bytes. (leaf/helper — see body)_

```c
void sub_41c983(void)
{
    sub_41c984();
    return;
}
```

## `sub_0041c984` `0x0041c984`

_1493 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_4208d4;

int sub_41c984(void)
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
    v1 = sub_41cf5a;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v0 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v0;
    v11 = g_4208d4;
    g_4208d4 = g_4208d4 + 1;
    v12 = _ccall(4, 18, v11 + 1, 0, 0);
    if ((char)v12)
    {
        sub_41c90c();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_404814();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_404814();
        sub_404814();
        sub_404814();
        sub_404814();
        sub_404814();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
    }
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v0;
    v2 = sub_41cf61;
    return sub_41cf59(&v4);
}
```

## `sub_0041cf59` `0x0041cf59`

_1 bytes. (leaf/helper — see body)_

```c
void sub_41cf59(void)
{
    return;
}
```

## `sub_0041cf5a` `0x0041cf5a`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_41cf5a(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041cf5f` `0x0041cf5f`

_2 bytes. (leaf/helper — see body)_

```c
void sub_41cf5f(void)
{
    sub_41cf59();
    return;
}
```

## `sub_0041cf61` `0x0041cf61`

_2 bytes. (leaf/helper — see body)_

```c
void sub_41cf61(unsigned int a0)
{
    return;
}
```

## `sub_0041cf63` `0x0041cf63`

_1 bytes. (leaf/helper — see body)_

```c
void sub_41cf63(void)
{
    sub_41cf64();
    return;
}
```

## `sub_0041cf64` `0x0041cf64`

_44 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_4208d4;

int sub_41cf64(void)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4153
    unsigned long v10;  // 4157
    unsigned int v11;  // 4119
    unsigned long v12;  // 4118
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    char *v2;  // [bp-0x8], Other Possible Types: unsigned int
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v2 = &v3;
    v1 = sub_41cf91;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v0 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v0;
    v11 = g_4208d4;
    g_4208d4 = g_4208d4 - 1;
    if (v11 < 1)
        sub_41c89c();
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v0;
    v2 = sub_41cf98;
    return sub_41cf90(&v4);
}
```

## `sub_0041cf90` `0x0041cf90`

_1 bytes. (leaf/helper — see body)_

```c
void sub_41cf90(void)
{
    return;
}
```

## `sub_0041cf91` `0x0041cf91`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_41cf91(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041cf96` `0x0041cf96`

_2 bytes. (leaf/helper — see body)_

```c
void sub_41cf96(void)
{
    sub_41cf90();
    return;
}
```

## `sub_0041cf98` `0x0041cf98`

_2 bytes. (leaf/helper — see body)_

```c
void sub_41cf98(unsigned int a0)
{
    return;
}
```

## `sub_0041cf9a` `0x0041cf9a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41cf9a(void)
{
    return sub_41cf9c();
}
```

## `sub_0041cf9c` `0x0041cf9c`

_484 bytes. refs "TibiaClient", "TibiaClient"_

```c
int sub_41cf9c(void)
{
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    char v20;  // bl
    unsigned int v21;  // esi
    char v22;  // bl
    unsigned int v23;  // esi
    unsigned long v24;  // 4118
    unsigned short v12;  // fs
    unsigned long v13;  // 4166
    unsigned int v14;  // 4120
    unsigned long v15;  // 4175
    int v16;  // edi
    int v17;  // esi
    int v18;  // ebx
    HWND i;  // edi
    unsigned int v0;  // [bp-0x258]
    unsigned int v1;  // [bp-0x250]
    unsigned int v2;  // [bp-0x238]
    Byte v3[260];  // [bp-0x118]
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    HANDLE v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]
    char v8;  // [bp-0x4]

    v5 = 0;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v14 = *((int *)v13);
    v0 = *((int *)v13);
    v15 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v15) = &v0;
    v7 = 0;
    sub_402754(v14, sub_41d199, &v8, v16, v17, v18, 0, 0);
    sub_406550(v14, sub_41d199, &v8, v16, v17, v18, 0, 0);
    sub_403ccc();
    i = FindWindowA("TibiaClient", NULL);
    if (i)
    {
        GetWindowThreadProcessId(i, &v4);
        v6 = OpenProcess(0x1f0fff, 0, v4);
        v20 = 0;
        if (v6)
        {
            v21 = sub_405770();
            v2 = 548;
            sub_405790();
            do
            {
                if (!lstrcmpiA(v3, sub_403e78()))
                {
                    v20 = 1;
                    break;
                }
            } while (sub_4057b0());
            CloseHandle(v21);
            if (!v20)
            {
                sub_41c624();
                v7 = 1;
            }
            else
            {
                do
                {
                    i = FindWindowExA(NULL, i, "TibiaClient", NULL);
                    if (!i)
                        break;
                    GetWindowThreadProcessId(i, &v4);
                    v6 = OpenProcess(0x1f0fff, 0, v4);
                    v22 = 0;
                    if (v6)
                    {
                        v23 = sub_405770();
                        v2 = 548;
                        sub_405790();
                        do
                        {
                            if (!lstrcmpiA(v3, sub_403e78()))
                            {
                                v22 = 1;
                                break;
                            }
                        } while (sub_4057b0());
                        CloseHandle(v23);
                    }
                    if (!v22)
                    {
                        sub_41c624();
                        v7 = 1;
                        break;
                    }
                } while (i);
            }
        }
    }
    v24 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v24) = v14;
    v1 = sub_41d1a0;
    return sub_41d180();
}
```

## `sub_0041d180` `0x0041d180`

_25 bytes. (leaf/helper — see body)_

```c
int sub_41d180(void)
{
    sub_403a34();
    return sub_403a10();
}
```

## `sub_0041d199` `0x0041d199`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_41d199(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041d19e` `0x0041d19e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41d19e(void)
{
    return sub_41d180();
}
```

## `sub_0041d1a0` `0x0041d1a0`

_10 bytes. (leaf/helper — see body)_

```c
int sub_41d1a0(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // [bp+0x100000]

    return v0;
}
```

## `sub_0041d1cc` `0x0041d1cc`

_30 bytes. (leaf/helper — see body)_

```c
int sub_41d1cc(void)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4143
    unsigned long v10;  // 4152
    unsigned long v11;  // 4163
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    char *v2;  // [bp-0x8], Other Possible Types: unsigned int
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v2 = &v3;
    v1 = sub_41d1eb;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v0 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v0;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v0;
    v2 = sub_41d1f2;
    return sub_41d1ea(&v4);
}
```

## `sub_0041d1ea` `0x0041d1ea`

_1 bytes. (leaf/helper — see body)_

```c
void sub_41d1ea(void)
{
    return;
}
```

## `sub_0041d1eb` `0x0041d1eb`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_41d1eb(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041d1f0` `0x0041d1f0`

_2 bytes. (leaf/helper — see body)_

```c
void sub_41d1f0(void)
{
    sub_41d1ea();
    return;
}
```

## `sub_0041d1f2` `0x0041d1f2`

_2 bytes. (leaf/helper — see body)_

```c
void sub_41d1f2(unsigned int a0)
{
    return;
}
```

## `sub_0041d274` `0x0041d274`

_54 bytes. refs "Please run Tibia first!", "Elfbot NG"_

```c
void _start(void)
{
    sub_405028();
    if (!sub_41cf9c())
        sub_4054ac(NULL, "Please run Tibia first!", "Elfbot NG", 0);
    sub_403920(); /* do not return */
}
```

