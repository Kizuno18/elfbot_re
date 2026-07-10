# elfbot.dll decompiled — loader 0x00407452..0x00408012

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_00407452` `0x00407452`

_2 bytes. (leaf/helper — see body)_

```c
int sub_407452(void)
{
    return sub_407444();
}
```

## `sub_00407454` `0x00407454`

_9 bytes. (leaf/helper — see body)_

```c
int sub_407454(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v0;  // esi

    return v0;
}
```

## `sub_0040745d` `0x0040745d`

_3 bytes. (leaf/helper — see body)_

```c
int sub_40745d(void)
{
    return sub_407460();
}
```

## `sub_00407460` `0x00407460`

_142 bytes. (leaf/helper — see body)_

```c
extern void g_4073ac;
extern void g_4073e8;
extern unsigned int g_42085c;

int sub_407460(void)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned int i;  // edx
    unsigned int iter;  // eax
    unsigned long v20;  // 4118
    unsigned short v8;  // fs
    unsigned long v9;  // 4139
    unsigned int v10;  // 4109
    unsigned long v11;  // 4148
    int v12;  // esi
    int v13;  // ecx
    unsigned int v14;  // esi
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v2 = 0;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v10 = *((int *)v9);
    v0 = *((int *)v9);
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v0;
    sub_40530c();
    sub_4071d8(&v2, v10, sub_4074f7, &v3, v12, 0, &v4);
    v14 = (unsigned int)sub_4064d0(v13, 1);
    if (v14 - 3 < 3)
    {
        EnumCalendarInfoA(&g_4073ac, sub_40530c(), v14, 4);
        i = 7;
        iter = &g_42085c;
        do
        {
            *((unsigned int *)iter) = 4294967295;
            iter += 4;
            i -= 1;
        } while (i != 1);
        EnumCalendarInfoA(&g_4073e8, sub_40530c(), v14, 3);
    }
    v20 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v20) = &v2;
    v1 = sub_4074fe;
    return sub_4074ee();
}
```

## `sub_004074ee` `0x004074ee`

_9 bytes. (leaf/helper — see body)_

```c
int sub_4074ee(void)
{
    return sub_403a10();
}
```

## `sub_004074f7` `0x004074f7`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4074f7(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004074fc` `0x004074fc`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4074fc(void)
{
    return sub_4074ee();
}
```

## `sub_004074fe` `0x004074fe`

_4 bytes. (leaf/helper — see body)_

```c
void sub_4074fe(unsigned int a0, unsigned int a1, unsigned int a2)
{
    return;
}
```

## `sub_00407510` `0x00407510`

_444 bytes. (leaf/helper — see body)_

```c
extern char g_41e0b8;
extern unsigned int g_420834;

int sub_407510(void)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned int v18;  // ecx
    char v19;  // al
    unsigned int v20;  // eax
    unsigned long v23;  // 4118
    unsigned short v10;  // fs
    unsigned long v11;  // 4165
    unsigned int v12;  // 4124
    unsigned long v13;  // 4174
    int iter;  // ebx
    int v15;  // edi
    int v16;  // esi
    int v17;  // ebx
    unsigned int v0;  // [bp-0x38]
    unsigned int v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]
    char v6;  // [bp+0x0]

    v3 = 0;
    v2 = 0;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v12 = *((int *)v11);
    v1 = *((int *)v11);
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v13) = &v1;
    iter = 1;
    sub_403a10(v12, sub_4076da, &v5, v15, v16, v17, 0, 0, 0, 0, 0, &v6);
    sub_40530c();
    sub_4071d8(&v3);
    if ((unsigned int)sub_4064d0(v18, 1) - 3 >= 3)
    {
        if (g_420834 != 4 && g_420834 - 0x11 >= 2)
            v19 = 0;
        else
            v19 = 1;
        if (v19)
        {
            while (iter <= sub_403c80())
            {
                if (*((char *)(v20 + iter - 1)) == 71)
                {
                    iter += 1;
                }
                else if (*((char *)(v20 + iter - 1)) != 103)
                {
                    sub_403bd8(v18, _INSERT(0, 0, *((char *)(v20 + iter - 1))));
                    sub_403c88();
                    iter += 1;
                }
                else
                {
                    iter += 1;
                }
            }
        }
        else
        {
            sub_403a64();
        }
    }
    else
    {
        while (iter <= sub_403c80())
        {
            if (((char)((&g_41e0b8)[*((char *)(v20 + iter - 1)) >> 3] >> (*((char *)(v20 + iter - 1)) & 7)) & 1) == 1)
            {
                v4 = sub_408258();
                sub_403ed8(&v2);
                sub_403c88(&v2);
                iter += sub_408258();
            }
            else if (!sub_40668c())
            {
                sub_403c88();
                iter += 2;
            }
            else if (!sub_40668c())
            {
                sub_403c88();
                iter += 4;
            }
            else if (!sub_40668c())
            {
                sub_403c88();
                iter += 2;
            }
            else if (*((char *)(v20 + iter - 1)) == 89 || *((char *)(v20 + iter - 1)) == 121)
            {
                sub_403c88();
                iter += 1;
            }
            else
            {
                sub_403bd8(v18, _INSERT(0, 0, *((char *)(v20 + iter - 1))));
                sub_403c88();
                iter += 1;
            }
        }
    }
    v23 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v23) = v0;
    v1 = sub_4076e1;
    sub_4076cc();
    return;
}
```

## `sub_004076cc` `0x004076cc`

_14 bytes. (leaf/helper — see body)_

```c
int sub_4076cc(void)
{
    return sub_403a34();
}
```

## `sub_004076da` `0x004076da`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4076da(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004076df` `0x004076df`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4076df(void)
{
    return sub_4076cc();
}
```

## `sub_004076e1` `0x004076e1`

_7 bytes. (leaf/helper — see body)_

```c
void sub_4076e1(unsigned int a0, unsigned int a1)
{
    return;
}
```

## `sub_00407738` `0x00407738`

_10 bytes. (leaf/helper — see body)_

```c
int sub_407738(void)
{
    return;
}
```

## `sub_00407742` `0x00407742`

_2 bytes. (leaf/helper — see body)_

```c
int sub_407742(void)
{
    sub_407744();
    return;
}
```

## `sub_00407744` `0x00407744`

_383 bytes. (leaf/helper — see body)_

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

extern int g_4078c4;
extern void* g_41f5b0;
extern LPArray g_420710;

int sub_407744(void)
{
    unsigned int v18;  // ecx
    void* v19;  // edx
    int v20;  // edi
    int v21;  // esi
    int v22;  // ebx
    int v23;  // ebx
    int v24;  // edi
    int v25;  // eax
    unsigned int v26;  // eax
    char v0;  // [bp-0x45c]
    char *v1;  // [bp-0x35c]
    char v2;  // [bp-0x358]
    char *v3;  // [bp-0x354]
    char v4;  // [bp-0x350]
    int v5;  // [bp-0x34c]
    char v6;  // [bp-0x348]
    int v7;  // [bp-0x344]
    char v8;  // [bp-0x340]
    int v9;  // [bp-0x33c]
    char v10;  // [bp-0x338]
    MEMORY_BASIC_INFORMATION v11;  // [bp-0x334]
    char v12;  // [bp-0x316]
    char v13;  // [bp-0x216]
    char v14;  // [bp-0x111]
    int v15;  // [bp-0xc]
    unsigned int v16;  // [bp-0x8]

    v16 = v18;
    VirtualQuery(v19, &v11, 0x1c);
    if (v11.State != 0x1000 || !sub_4052a4(v11.AllocationBase, &v13, 261))
    {
        sub_4052a4(g_420710, &v13, 261);
        v15 = sub_407738(v20, v21, v22);
    }
    else
    {
        v15 = v19 - v11.AllocationBase;
    }
    sub_408294();
    sub_406658();
    v23 = &g_4078c4;
    v24 = &g_4078c4;
    if ((char)sub_402ea0())
    {
        v23 = sub_403e78();
        v25 = sub_406630();
        if (v25 && *((char *)(v23 + v25 - 1)) != 46)
            v24 = ".";
    }
    v26 = sub_4048c0((int)g_41f5b0[4], &v12, 0x100);
    sub_4054a4(v26, (int)g_41f5b0[4], &v12, 0x100);
    sub_402dc0(v20);
    v1 = &v0;
    v2 = 4;
    v3 = &v14;
    v4 = 6;
    v5 = v15;
    v6 = 5;
    v7 = v23;
    v8 = 6;
    v9 = v24;
    v10 = 6;
    sub_406b7c(4, &v1);
    sub_406630(4, &v1);
    return;
}
```

## `sub_004078cc` `0x004078cc`

_165 bytes. refs "\r\n"_

```c
typedef struct OVERLAPPED {
    UIntPtr Internal;
    UIntPtr InternalHigh;
    char Anonymous;
    char padding_9[7];
    HANDLE hEvent;
} OVERLAPPED;

typedef struct struct_0 {
    char field_0;
} struct_0;

extern void* g_41f470;
extern struct_0 *g_41f554;

int sub_4078cc(void)
{
    unsigned int v4;  // eax
    unsigned int v6;  // eax
    OVERLAPPED v0;  // [bp-0x448]
    char v1;  // [bp-0x444]
    Byte v2[1028];  // [bp-0x404]

    v0 = (OVERLAPPED)0x400;
    sub_407744();
    if (!g_41f554->field_0)
    {
        v6 = sub_4048c0((int)g_41f470[4], &v1, 64);
        sub_4054a4(v6, (int)g_41f470[4], &v1, 64);
        return sub_4054ac(NULL, v2, &v1, 8208);
    }
    sub_4027fc();
    v4 = sub_406630(&v0, 0);
    sub_405434(sub_4052dc(4294967285), v2, v4, &v0, 0);
    return sub_405434(sub_4052dc(4294967285), "\r\n", 0x2, &v0, 0);
}
```

## `sub_00407980` `0x00407980`

_58 bytes. (leaf/helper — see body)_

```c
int sub_407980(void)
{
    unsigned int v7;  // ebx
    unsigned int v8;  // esi
    unsigned int v9;  // edi
    char v10;  // dl
    unsigned long v11;  // ldt
    unsigned long v12;  // gdt
    unsigned short v13;  // fs
    unsigned long v14;  // 4109
    int v0;  // [bp-0x1c]
    int v1;  // [bp-0x18]
    int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    unsigned int v5;  // [bp-0x4]

    v5 = v7;
    v4 = v8;
    v3 = v9;
    if (v10)
        sub_402f44();
    sub_403a64(v0, v1, v2);
    if (v10)
    {
        sub_402f9c();
        v14 = _ccall(v11, v12, (unsigned int)v13, 0);
        *((int *)v14) = v0;
    }
    return;
}
```

## `sub_004079ba` `0x004079ba`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4079ba(unsigned int a0, char a1)
{
    return sub_4079bc();
}
```

## `sub_004079bc` `0x004079bc`

_81 bytes. (leaf/helper — see body)_

```c
int sub_4079bc(void)
{
    unsigned int v8;  // ebx
    unsigned int v9;  // esi
    unsigned long v18;  // 4118
    unsigned int v10;  // edi
    char v11;  // dl
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    unsigned short v14;  // fs
    unsigned long v15;  // 4131
    unsigned int v16;  // 4103
    unsigned long v17;  // 4140
    unsigned int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x2c]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]

    v5 = 0;
    v4 = v8;
    v3 = v9;
    v2 = v10;
    if (v11)
        sub_402f44();
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    v16 = *((int *)v15);
    v0 = *((int *)v15);
    v17 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v17) = &v0;
    sub_406bbc(&v5, v16, sub_407a16, &v6);
    sub_403a64(&v5, v16, sub_407a16, &v6);
    v18 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v18) = &v5;
    v1 = sub_407a1d;
    sub_407a0d();
    return;
}
```

## `sub_00407a0d` `0x00407a0d`

_9 bytes. (leaf/helper — see body)_

```c
int sub_407a0d(void)
{
    return sub_403a10();
}
```

## `sub_00407a16` `0x00407a16`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_407a16(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00407a1b` `0x00407a1b`

_2 bytes. (leaf/helper — see body)_

```c
int sub_407a1b(void)
{
    return sub_407a0d();
}
```

## `sub_00407a1d` `0x00407a1d`

_31 bytes. (leaf/helper — see body)_

```c
int sub_407a1d(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5)
{
    char v1;  // bl
    unsigned long v2;  // ldt
    unsigned long v3;  // gdt
    unsigned short v4;  // fs
    unsigned long v5;  // 4109
    unsigned int v6;  // edi
    unsigned int v0;  // [bp+0x0]

    if (v1)
    {
        sub_402f9c();
        v5 = _ccall(v2, v3, (unsigned int)v4, 0);
        *((unsigned int *)v5) = v0;
    }
    return v6;
}
```

## `sub_00407a3c` `0x00407a3c`

_58 bytes. (leaf/helper — see body)_

```c
int sub_407a3c(void)
{
    unsigned int v7;  // ebx
    unsigned int v8;  // esi
    unsigned int v9;  // edi
    char v10;  // dl
    unsigned long v11;  // ldt
    unsigned long v12;  // gdt
    unsigned short v13;  // fs
    unsigned long v14;  // 4109
    int v0;  // [bp-0x1c]
    int v1;  // [bp-0x18]
    int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    unsigned int v5;  // [bp-0x4]

    v5 = v7;
    v4 = v8;
    v3 = v9;
    if (v10)
        sub_402f44();
    sub_404e44(v0, v1, v2);
    if (v10)
    {
        sub_402f9c();
        v14 = _ccall(v11, v12, (unsigned int)v13, 0);
        *((int *)v14) = v0;
    }
    return;
}
```

## `sub_00407a76` `0x00407a76`

_2 bytes. (leaf/helper — see body)_

```c
int sub_407a76(unsigned int a0, char a1)
{
    return sub_407a78();
}
```

## `sub_00407a78` `0x00407a78`

_94 bytes. (leaf/helper — see body)_

```c
int sub_407a78(void)
{
    unsigned int v9;  // ebx
    unsigned int v10;  // esi
    unsigned long v19;  // 4118
    unsigned int v11;  // edi
    char v12;  // dl
    unsigned long v13;  // ldt
    unsigned long v14;  // gdt
    unsigned short v15;  // fs
    unsigned long v16;  // 4130
    unsigned int v17;  // 4103
    unsigned long v18;  // 4139
    unsigned int v0;  // [bp-0x34]
    unsigned int v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 0;
    v5 = 0;
    v4 = v9;
    v3 = v10;
    v2 = v11;
    if (v12)
        sub_402f44();
    v16 = _ccall(v13, v14, (unsigned int)v15, 0);
    v17 = *((int *)v16);
    v0 = *((int *)v16);
    v18 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int **)v18) = &v0;
    sub_404e44(&v6, v17, sub_407ae4, &v7);
    sub_406bbc(&v6, v17, sub_407ae4, &v7);
    sub_403a64();
    v19 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int **)v19) = &v6;
    v1 = sub_407aeb;
    sub_407ad6();
    return;
}
```

## `sub_00407ad6` `0x00407ad6`

_14 bytes. (leaf/helper — see body)_

```c
int sub_407ad6(void)
{
    return sub_403a34();
}
```

## `sub_00407ae4` `0x00407ae4`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_407ae4(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00407ae9` `0x00407ae9`

_2 bytes. (leaf/helper — see body)_

```c
int sub_407ae9(void)
{
    return sub_407ad6();
}
```

## `sub_00407aeb` `0x00407aeb`

_32 bytes. (leaf/helper — see body)_

```c
int sub_407aeb(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6)
{
    char v1;  // bl
    unsigned long v2;  // ldt
    unsigned long v3;  // gdt
    unsigned short v4;  // fs
    unsigned long v5;  // 4109
    unsigned int v6;  // edi
    unsigned int v0;  // [bp+0x0]

    if (v1)
    {
        sub_402f9c();
        v5 = _ccall(v2, v3, (unsigned int)v4, 0);
        *((unsigned int *)v5) = v0;
    }
    return v6;
}
```

## `sub_00407b0b` `0x00407b0b`

_1 bytes. (leaf/helper — see body)_

```c
int sub_407b0b(void)
{
    sub_407b0c();
    return;
}
```

## `sub_00407b0c` `0x00407b0c`

_12 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    char field_c;
} struct_0;

int sub_407b0c(void)
{
    struct_0 *v1;  // eax

    if (v1->field_c)
        sub_402df0();
    return;
}
```

## `sub_00407b1c` `0x00407b1c`

_40 bytes. (leaf/helper — see body)_

```c
int sub_407b1c(void)
{
    unsigned short v2;  // cs
    unsigned int v3;  // eax
    unsigned int v4;  // 4100
    unsigned int v5;  // edx
    unsigned int v6;  // esi
    unsigned int v0;  // [bp-0x4]

    *((unsigned short *)&v0) = v2;
    v4 = *((int *)(/* unsupported instruction */ + v3 * 2 + 114));
    *((unsigned int *)(/* unsupported instruction */ + v3 * 2 + 114)) = v4 | v5;
    if ((v4 | v5) < 0)
        return;
    if ((v4 | v5) >= 0)
        goto LABEL_0x407b25;
    *((unsigned int *)(sub_407a78(0, &v0) + 12)) = v6;
    return;
}
```

## `sub_00407b27` `0x00407b27`

_17 bytes. (leaf/helper — see body)_

```c
int sub_407b27(void)
{
    void* v1;  // eax
    char v2;  // 4110
    unsigned int v3;  // 4137
    char v4;  // dl
    void* v5;  // eax

    *((char *)v1) = *((char *)v1) | *((char *)&v1);
    *((char *)v1) = *((char *)v1) + *((char *)&v1);
    *((void* *)v1) = *((int *)v1) + v1;
    v2 = *((char *)v1);
    *((char *)v1) = *((char *)v1) + *((char *)&v1);
    v3 = _ccall(1, (unsigned int)v2, (unsigned int)*((char *)(void*)&v1), 0);
    *((char *)v1) = *((char *)v1) - v4 - ((char)v3 & 1);
    v5 = v1 + 1;
    *((char *)(v5 * 2)) = *((char *)(v5 * 2)) + *((char *)&v5);
    *((char *)v5) = *((char *)v5) + *((char *)&v5);
    sub_407b38();
    return;
}
```

## `sub_00407b38` `0x00407b38`

_63 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_41e198[4];

int sub_407b38(void)
{
    unsigned int v4;  // ebx
    unsigned int v5;  // esi
    int i;  // ebx
    unsigned int v7[4];  // esi
    unsigned int v0[4];  // [bp-0x10]
    unsigned int v1;  // [bp-0x8]
    unsigned int v2;  // [bp-0x4]

    v2 = v4;
    v1 = v5;
    i = 0;
    for (v7 = sub_402608(); i <= 6 && v7 != g_41e198[2 * i]; i += 1);
    if (i > 6)
        v0 = v7;
    sub_407980();
}
```

## `sub_00407ba2` `0x00407ba2`

_4 bytes. (leaf/helper — see body)_

```c
void sub_407ba2(void)
{
    unsigned int v2;  // edx
    unsigned int v0;  // [bp-0x4]

    __unsupported_jumpkind_Ijk_NoDecode()
    __unsupported_jumpkind_Ijk_NoDecode()
    v0 = v2;
}
```

## `sub_00407ba8` `0x00407ba8`

_96 bytes. (leaf/helper — see body)_

```c
int sub_407ba8(void)
{
    void* v2;  // eax
    char v3;  // 4110
    unsigned int v12;  // 4178
    unsigned int v13;  // 4102
    unsigned int v14;  // 4109
    unsigned int v4;  // 4141
    int v5;  // edx
    void* v6;  // eax
    char v7;  // 4125
    unsigned int v8;  // ebx
    char v9;  // dl
    char v10;  // dl
    unsigned int v11;  // 4171
    unsigned int v0;  // [bp-0x4]

    *((char *)v2) = *((char *)v2) | *((char *)&v2);
    *((char *)v2) = *((char *)v2) + *((char *)&v2);
    *((void* *)v2) = *((int *)v2) + v2;
    v3 = *((char *)v2);
    *((char *)v2) = *((char *)v2) + *((char *)&v2);
    v4 = _ccall(1, (unsigned int)v3, (unsigned int)*((char *)(void*)&v2), 0);
    *((char *)v2) = *((char *)v2) - (char)v5 - ((char)v4 & 1);
    v6 = v2 + 1;
    *((char *)(v6 * 2)) = *((char *)(v6 * 2)) + *((char *)&v6);
    v7 = *((char *)v6);
    *((char *)v6) = *((char *)v6) + *((char *)&v6);
    v0 = v8;
    v9 = (char)v6;
    v10 = v9 - 1;
    v11 = _ccall(1, (unsigned int)v7, (unsigned int)*((char *)(void*)&v6), 0);
    v12 = _ccall(4, 19, (unsigned int)(v9 - 1), 0, v11);
    if ((char)v12)
    {
        sub_403470(v5);
        return;
    }
    v13 = _ccall(19, (unsigned int)(v9 - 1), 0, v11);
    v14 = _ccall(4, 19, (unsigned int)(v10 - 1), 0, v13);
    if ((char)v14)
    {
        sub_403470(v5);
        return;
    }
    if (v10 - 2 < 22)
        sub_407980();
    sub_407b38();
    sub_403470(v5);
    return;
}
```

## `sub_00407c08` `0x00407c08`

_2 bytes. (leaf/helper — see body)_

```c
void sub_407c08(unsigned int a0)
{
    return;
}
```

## `sub_00407c0a` `0x00407c0a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_407c0a(void)
{
    return sub_407c0c();
}
```

## `sub_00407c0c` `0x00407c0c`

_139 bytes. (leaf/helper — see body)_

```c
int sub_407c0c(void)
{
    unsigned int v5;  // ebx
    unsigned int v6;  // esi
    unsigned long v15;  // 4157
    unsigned int v16;  // eax
    unsigned int v17;  // edx
    unsigned long v18;  // 4119
    void* v7;  // edi
    unsigned int v8;  // 4106
    unsigned int v9;  // ecx
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // fs
    unsigned long v13;  // 4153
    unsigned int v14;  // 4105
    unsigned int v0;  // [bp-0x38]
    void* v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x28]

    v3 = v5;
    v2 = v6;
    v1 = v7;
    v8 = _ccall(5, 15, 0, 0, 0);
    if (v9 != 1 & (char)v8)
        goto LABEL_0x407ba4;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v14 = *((int *)v13);
    v0 = *((int *)v13);
    v15 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v15) = &v0;
    if (v16)
        sub_403aa8(v14, sub_407ca8, v7);
    else
        sub_404e44(v14, sub_407ca8, v7);
    *((int *)&v7[28]) = (int)v7[4];
    *((char *)&v7[24]) = 11;
    *((unsigned int *)&v7[20]) = v17;
    *((char *)&v7[16]) = 11;
    *((unsigned int *)&v7[12]) = v9 - 1;
    *((char *)&v7[8]) = 0;
    sub_404e44(2, v7 - 28);
    sub_4079bc(2, v7 - 28);
    v18 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v18) = 2;
    v0 = sub_407caf;
    sub_407c97();
    return;
}
```

## `sub_00407c97` `0x00407c97`

_17 bytes. (leaf/helper — see body)_

```c
int sub_407c97(void)
{
    sub_403a10();
    return sub_403a10();
}
```

## `sub_00407ca8` `0x00407ca8`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_407ca8(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00407cad` `0x00407cad`

_2 bytes. (leaf/helper — see body)_

```c
int sub_407cad(void)
{
    return sub_407c97();
}
```

## `sub_00407caf` `0x00407caf`

_9 bytes. (leaf/helper — see body)_

```c
int sub_407caf(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // ebx

    return v0;
}
```

## `sub_00407cb8` `0x00407cb8`

_13 bytes. (leaf/helper — see body)_

```c
void sub_407cb8(unsigned int *a0, unsigned int a1)
{
    *(a0) = a1;
    sub_403470();
    return;
}
```

## `sub_00407cc5` `0x00407cc5`

_1 bytes. (leaf/helper — see body)_

```c
void sub_407cc5(void)
{
    return;
}
```

## `sub_00407cc6` `0x00407cc6`

_2 bytes. (leaf/helper — see body)_

```c
void sub_407cc6(void)
{
    sub_407cc8();
    return;
}
```

## `sub_00407cc8` `0x00407cc8`

_26 bytes. (leaf/helper — see body)_

```c
void sub_407cc8(unsigned int a0)
{
    char v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x8]

    sub_407c0c(&v0);
    sub_407cb8(&v1, a0);
    return;
}
```

## `sub_00407ce2` `0x00407ce2`

_26 bytes. (leaf/helper — see body)_

```c
int sub_407ce2(void)
{
    sub_407a3c();
    return sub_403470();
}
```

## `sub_00407cfc` `0x00407cfc`

_127 bytes. (leaf/helper — see body)_

```c
int sub_407cfc(void)
{
    int *v1;  // eax
    int v2;  // eax
    unsigned int v3;  // eax
    unsigned int v5;  // eax

    v2 = *(v1);
    if (v2 <= -1073741678)
    {
        if (v2 == -1073741678)
        {
            return;
        }
        else if (v2 <= -1073741682)
        {
            if (v2 != -1073741682)
            {
                v3 = v2 + 0x3ffffffb;
                if (v2 == -1073741819)
                {
                    return;
                }
                else if (v3 != 135)
                {
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
        else
        {
            if (v2 + 0x3fffff71 >= 2)
                return;
            return;
        }
    }
    else
    {
        if (v2 <= -1073741674)
        {
            if (v2 != -1073741674)
            {
                v5 = v2 + 0x3fffff6d;
                if (v2 == -1073741677)
                {
                    return;
                }
                else if (v5 != 1)
                {
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
        else
        {
            if (v2 != -1073741571)
                return;
            return;
        }
    }
}
```

## `sub_00407d7b` `0x00407d7b`

_1 bytes. (leaf/helper — see body)_

```c
void sub_407d7b(void)
{
    sub_407d7c();
    return;
}
```

## `sub_00407d7c` `0x00407d7c`

_24 bytes. (leaf/helper — see body)_

```c
int sub_407d7c(void)
{
    int v0;  // [bp-0x4]

    sub_407cfc(v0);
    return;
}
```

## `sub_00407d94` `0x00407d94`

_407 bytes. (leaf/helper — see body)_

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

int sub_407d94(void* a0)
{
    unsigned long v16;  // ldt
    unsigned long v17;  // gdt
    int v23;  // ebx
    int v24;  // esi
    unsigned long v25;  // 4118
    unsigned short v18;  // fs
    unsigned long v19;  // 4197
    unsigned int v20;  // 4120
    unsigned long v21;  // 4201
    unsigned int idx[7];  // ebx
    unsigned int v0;  // [bp-0x188]
    unsigned int v1;  // [bp-0x170]
    char v2;  // [bp-0x16c]
    unsigned int v3;  // [bp-0x168]
    char v4;  // [bp-0x164]
    unsigned int v5;  // [bp-0x160]
    char v6;  // [bp-0x15c]
    unsigned int v7;  // [bp-0x158]
    unsigned int v8;  // [bp-0x154]
    unsigned int v9;  // [bp-0x150]
    unsigned int v10;  // [bp-0x14c]
    char v11;  // [bp-0x148]
    char v12;  // [bp-0x129]
    MEMORY_BASIC_INFORMATION v13;  // [bp-0x24]
    unsigned int v14;  // [bp-0x8]
    char v15;  // [bp-0x4]

    v9 = 0;
    v7 = 0;
    v8 = 0;
    v14 = 0;
    v19 = _ccall(v16, v17, (unsigned int)v18, 0);
    v20 = *((int *)v19);
    v0 = *((int *)v19);
    v21 = _ccall(v16, v17, (unsigned int)v18, 0);
    *((unsigned int **)v21) = &v0;
    idx = (int)a0[4];
    if (!idx[5])
        sub_404e44(v20, sub_407f4f, &v15, v24, v23, 0);
    else
        sub_404e44(v20, sub_407f4f, &v15, v24, v23, 0);
    VirtualQuery(idx[3], &v13, 0x1c);
    if (v13.State == 0x1000 && sub_4052a4(v13.AllocationBase, &v12, 261))
    {
        v10 = idx[3];
        v11 = 5;
        sub_403c54();
        4220292();
    }
    v1 = idx[3];
    v2 = 5;
    v3 = v14;
    v4 = 11;
    v5 = idx[6];
    v6 = 5;
    sub_404e44(2, &v1);
    sub_4079bc(2, &v1);
    v25 = _ccall(v16, v17, (unsigned int)v18, 0);
    *((unsigned int *)v25) = 2;
    v0 = sub_407f56;
    return sub_407f2b();
}
```

## `sub_00407f2b` `0x00407f2b`

_36 bytes. (leaf/helper — see body)_

```c
int sub_407f2b(void)
{
    sub_403a10();
    sub_403a34();
    return sub_403a10();
}
```

## `sub_00407f4f` `0x00407f4f`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_407f4f(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00407f54` `0x00407f54`

_2 bytes. (leaf/helper — see body)_

```c
int sub_407f54(void)
{
    return sub_407f2b();
}
```

## `sub_00407f56` `0x00407f56`

_8 bytes. (leaf/helper — see body)_

```c
int sub_407f56(unsigned int a0)
{
    unsigned int v0;  // ebx

    return v0;
}
```

## `sub_00407f5e` `0x00407f5e`

_181 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    struct struct_1 *field_c;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_407f5e(void)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned long v15;  // 4118
    unsigned short v7;  // fs
    unsigned long v8;  // 4148
    unsigned int v9;  // 4115
    unsigned long v10;  // 4157
    int v11;  // ebx
    unsigned int v12;  // edx
    unsigned int *v13;  // eax
    struct_0 *v14;  // ebx
    unsigned int v0;  // [bp-0x2c]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x10]
    char v3;  // [bp-0xc]

    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v9 = *((int *)v8);
    v1 = *((int *)v8);
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v10) = &v1;
    v12 = (sub_407cfc(v9, sub_40801b, &/* unsupported instruction */, v11, 0) & 0xff) - 3;
    if (v12 < 8)
    {
LABEL_407f9c:
        v14 = sub_407980();
    }
    else if (v12 != 8)
    {
        if (v12 - 9 < 10)
            goto LABEL_407f9c;
        v2 = *(v13);
        v3 = 0;
        v0 = 0;
        sub_404e44(0, &v2);
        v14 = sub_4079bc(0, &v2);
    }
    else
    {
        v14 = sub_407d94(&/* unsupported instruction */);
    }
    if ((char)sub_402ea0())
        v14->field_c = v13;
    v15 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v15) = v0;
    v1 = sub_408022;
    sub_408012();
    return;
}
```

## `sub_00408012` `0x00408012`

_8 bytes. (leaf/helper — see body)_

```c
int sub_408012(void)
{
    sub_403a10();
}
```

