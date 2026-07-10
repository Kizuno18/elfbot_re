# elfbot.dll decompiled — loader 0x0040801b..0x00408f5a

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_0040801b` `0x0040801b`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40801b(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00408020` `0x00408020`

_2 bytes. (leaf/helper — see body)_

```c
int sub_408020(void)
{
    return sub_408012();
}
```

## `sub_00408022` `0x00408022`

_7 bytes. (leaf/helper — see body)_

```c
int sub_408022(void)
{
    unsigned int v1;  // ebx

    return v1;
}
```

## `sub_00408029` `0x00408029`

_3 bytes. (leaf/helper — see body)_

```c
int sub_408029(void)
{
    return sub_40802c();
}
```

## `sub_0040802c` `0x0040802c`

_16 bytes. (leaf/helper — see body)_

```c
int sub_40802c(void)
{
    sub_4078cc();
    return sub_4039f8();
}
```

## `sub_0040803c` `0x0040803c`

_130 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern char g_405b04;
extern char g_407bb8;
extern char g_407ce4;
extern char g_407f60;
extern struct_0 *g_41f430;
extern unsigned int g_41f43c;
extern unsigned int g_41f460;
extern unsigned int g_41f49c;
extern unsigned int g_41f4a4;
extern unsigned int g_41f4a8;
extern unsigned int g_41f534;
extern unsigned int g_420884;
extern unsigned int g_420888;

int sub_40803c(void)
{
    g_420884 = sub_407a3c();
    g_420888 = sub_407a3c();
    *((char **)g_41f43c) = &g_407bb8;
    *((void* *)g_41f4a4) = sub_40802c;
    *((char **)g_41f460) = &g_405b04;
    *((void* *)g_41f49c) = sub_407d7c;
    *((char **)g_41f4a8) = &g_407f60;
    *((void* *)g_41f534) = sub_407cc8;
    g_41f430->field_0 = &g_407ce4;
    return &g_407ce4;
}
```

## `sub_004080be` `0x004080be`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4080be(void)
{
    return sub_4080c0();
}
```

## `sub_004080c0` `0x004080c0`

_107 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    void* field_0;
    char padding_4[8];
    char field_c;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

typedef struct struct_2 {
    char padding_0[12];
    char field_c;
} struct_2;

extern struct_0 *g_41f43c;
extern struct_0 *g_41f460;
extern struct_0 *g_41f49c;
extern struct_0 *g_41f4a4;
extern struct_0 *g_41f4a8;
extern struct_0 *g_41f534;
extern struct_1 *g_420884;
extern struct_2 *g_420888;

unsigned int * sub_4080c0(void)
{
    g_420884->field_c = 1;
    (int)g_420884->field_0[8]();
    g_420884 = 0;
    g_420888->field_c = 1;
    sub_402e1c();
    g_420888 = 0;
    g_41f43c->field_0 = 0;
    g_41f4a4->field_0 = 0;
    g_41f460->field_0 = 0;
    g_41f49c->field_0 = 0;
    g_41f4a8->field_0 = 0;
    g_41f534->field_0 = 0;
    return g_41f534;
}
```

## `sub_0040812b` `0x0040812b`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40812b(void)
{
    sub_40812c();
    return;
}
```

## `sub_0040812c` `0x0040812c`

_85 bytes. (leaf/helper — see body)_

```c
typedef struct OSVERSIONINFOA {
    unsigned int dwOSVersionInfoSize;
    unsigned int dwMajorVersion;
    unsigned int dwMinorVersion;
    unsigned int dwBuildNumber;
    unsigned int dwPlatformId;
    CHAR szCSDVersion[128];
} OSVERSIONINFOA;

extern unsigned int g_41e0a4;
extern unsigned int g_41e0a8;
extern unsigned int g_41e0ac;
extern unsigned int g_41e0b0;

int sub_40812c(void)
{
    unsigned int v2;  // eax
    OSVERSIONINFOA v0;  // [bp-0x94]

    v0.dwOSVersionInfoSize = 148;
    v2 = GetVersionExA(&v0);
    if (!v2)
        return v2;
    g_41e0a4 = v0.dwPlatformId;
    g_41e0a8 = v0.dwMajorVersion;
    g_41e0ac = v0.dwMinorVersion;
    g_41e0b0 = v0.dwBuildNumber;
    return sub_403c54();
}
```

## `sub_00408181` `0x00408181`

_3 bytes. (leaf/helper — see body)_

```c
int sub_408181(void)
{
    sub_408184();
    return;
}
```

## `sub_00408184` `0x00408184`

_117 bytes. (leaf/helper — see body)_

```c
extern char g_41e0b8;

int sub_408184(void)
{
    char *v1;  // eax
    int v2;  // edx
    int i;  // esi
    unsigned int v4;  // ecx
    unsigned int v5;  // ecx
    unsigned int v6;  // ecx

    if (!v1)
    {
        return;
    }
    else if (!v1[v2])
    {
        return;
    }
    else if (!v2)
    {
        return;
    }
    else
    {
        for (i = v2 - 1; i >= NULL && (v4 = (unsigned int)v1[i], ((&g_41e0b8)[v4 >> 3] >> (unsigned int)((char)v4 & 7) & 1) == 1); i -= 1);
        v5 = v2 - i;
        v6 = v5 & 2147483649;
        if ((v5 & 2147483649) < NULL)
            v6 = (v6 - 1 | 4294967294) + 1;
        if (v6)
            return;
        return;
    }
}
```

## `sub_004081f9` `0x004081f9`

_3 bytes. (leaf/helper — see body)_

```c
int sub_4081f9(void)
{
    sub_4081fc();
    return;
}
```

## `sub_004081fc` `0x004081fc`

_35 bytes. (leaf/helper — see body)_

```c
extern char g_42083c;

int sub_4081fc(void)
{
    int v0;  // [bp-0x8]
    int v1;  // [bp-0x4]

    if (g_42083c)
    {
        sub_403e78(v0, v1);
        sub_408184();
    }
    return;
}
```

## `sub_0040821f` `0x0040821f`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40821f(void)
{
    sub_408220();
    return;
}
```

## `sub_00408220` `0x00408220`

_21 bytes. (leaf/helper — see body)_

```c
extern char g_42083c;

int sub_408220(void)
{
    if (!g_42083c)
        return 0;
    return sub_408184();
}
```

## `sub_00408235` `0x00408235`

_3 bytes. (leaf/helper — see body)_

```c
int sub_408235(void)
{
    sub_408238();
    return;
}
```

## `sub_00408238` `0x00408238`

_29 bytes. (leaf/helper — see body)_

```c
extern char g_42083c;

int sub_408238(void)
{
    unsigned int v1;  // eax

    if (g_42083c)
        sub_40547c(v1);
    return;
}
```

## `sub_00408255` `0x00408255`

_3 bytes. (leaf/helper — see body)_

```c
int sub_408255(void)
{
    sub_408258();
    return;
}
```

## `sub_00408258` `0x00408258`

_57 bytes. (leaf/helper — see body)_

```c
extern char g_41e0b8;
extern char g_42083c;

int sub_408258(void)
{
    unsigned int v1;  // eax
    unsigned int v2;  // edx

    if (!g_42083c)
        return;
    if (((&g_41e0b8)[*((char *)(v1 + v2 - 1)) >> 3] >> (*((char *)(v1 + v2 - 1)) & 7) & 1) != 1)
        return;
    sub_403e78();
    sub_408238();
    return;
}
```

## `sub_00408291` `0x00408291`

_3 bytes. (leaf/helper — see body)_

```c
int sub_408291(unsigned int a0, unsigned int a1)
{
    return sub_408294();
}
```

## `sub_00408294` `0x00408294`

_40 bytes. (leaf/helper — see body)_

```c
unsigned int sub_408294(unsigned int a0, char a1)
{
    unsigned int i;  // eax
    unsigned int v4;  // eax
    int v0;  // [bp-0x8]
    int v1;  // [bp-0x4]

    i = sub_4082bc(v0, v1);
    if (!a1)
    {
        return i;
    }
    else if (i)
    {
        do
        {
            v4 = i;
            i = sub_4082bc();
        } while (i);
        return v4;
    }
    else
    {
        return i;
    }
}
```

## `sub_004082bc` `0x004082bc`

_64 bytes. (leaf/helper — see body)_

```c
int sub_4082bc(void)
{
    int v0;  // [bp-0xc]
    int v1;  // [bp-0x8]
    int v2;  // [bp-0x4]

    if (!sub_4066d0(v0, v1, v2))
        return;
    while (true)
    {
        if ((char)sub_408220() < 1)
        {
            return;
        }
        else if (!sub_4066d0())
        {
            return;
        }
    }
}
```

## `sub_004082fc` `0x004082fc`

_91 bytes. (leaf/helper — see body)_

```c
int sub_4082fc(void)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned long v18;  // 4119
    unsigned short v10;  // fs
    unsigned long v11;  // 4151
    unsigned int v12;  // 4114
    unsigned long v13;  // 4160
    unsigned int v14;  // eax
    int v15;  // ebx
    int v17;  // ecx
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x18]
    char v3;  // [bp-0xc], Other Possible Types: int
    int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]
    char v6;  // [bp+0x0]

    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v12 = *((int *)v11);
    v1 = *((int *)v11);
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v13) = &v1;
    sub_40529c(v14, 0x1004, &v3 + 1, 7);
    sub_403c54(v12, sub_408360, &v5, v15, 0, v3, v4, &v6, v6);
    v0 = 0;
    sub_4064d0(v17, GetACP());
    v18 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v18) = v12;
    v2 = sub_408367;
    sub_408357();
    return;
}
```

## `sub_00408357` `0x00408357`

_9 bytes. (leaf/helper — see body)_

```c
int sub_408357(void)
{
    return sub_403a10();
}
```

## `sub_00408360` `0x00408360`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_408360(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00408365` `0x00408365`

_2 bytes. (leaf/helper — see body)_

```c
int sub_408365(void)
{
    return sub_408357();
}
```

## `sub_00408367` `0x00408367`

_7 bytes. (leaf/helper — see body)_

```c
int sub_408367(void)
{
    unsigned int v1;  // ebx

    return v1;
}
```

## `sub_0040836e` `0x0040836e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40836e(unsigned int a0)
{
    return sub_408370();
}
```

## `sub_00408370` `0x00408370`

_96 bytes. (leaf/helper — see body)_

```c
extern char g_41e0b8;

int sub_408370(unsigned int a0)
{
    unsigned int v7;  // edi
    int ch;  // eax
    unsigned int v16;  // 4151
    int i;  // esi
    unsigned int v10;  // ebx
    int v11;  // eax
    char v12;  // 4106
    unsigned int v13;  // ebx
    char v14;  // 4100
    unsigned int v15;  // 4149
    int v0;  // [bp-0x14]
    int v1;  // [bp-0x10]
    int v2;  // [bp-0xc]
    int v3;  // [bp-0x8]
    char v4;  // [bp-0x5]
    char v5;  // [bp-0x5]
    char v6;  // [bp+0x0]

    v7 = a0 - 20;
    ch = GetCPInfo(sub_4082fc(v7, v0, v1, v2, v3, &v6), v7);
    for (i = 0; i < 12; i += 2)
    {
        v11 = _INSERT(ch, 0, *((char *)(v7 + i + 6)) | *((char *)(v7 + i + 7)));
        if (!*((char *)(v7 + i + 6)) && !*((char *)(v7 + i + 7)))
            return v11;
        v12 = *((char *)(v7 + i + 6));
        ch = _INSERT(v11, 0, v12);
        v10 = _INSERT(v10, 0, *((char *)(v7 + i + 7)) - v12);
        if (*((char *)(v7 + i + 7)) >= v12)
        {
            v13 = v10 + 1;
            v4 = ch;
            do
            {
                ch = v4;
                v14 = (&g_41e0b8)[ch >> 3];
                (&g_41e0b8)[ch >> 3] = (&g_41e0b8)[ch >> 3] | 1 << ((char)ch & 7);
                v5 = v4 + 1;
                v15 = _ccall(16, (unsigned int)(v4 + 1), 0, (unsigned int)v14 >> ((char)ch & 7) & 1);
                v16 = _ccall(4, 19, (unsigned int)((char)v13 - 1), 0, v15);
                v4 = v5;
                v13 = _INSERT(v13, 0, (char)v13 - 1);
            } while (!((char)v16));
        }
    }
    return ch;
}
```

## `sub_004083d0` `0x004083d0`

_21 bytes. (leaf/helper — see body)_

```c
extern char g_41e280;
extern int g_420834;

char sub_4083d0(void)
{
    int v1;  // eax
    unsigned int v2;  // cc_op
    unsigned int v3;  // cc_dep2
    unsigned int v4;  // 4105

    v1 = g_420834;
    v2 = 6;
    v3 = 31;
    if (g_420834 <= 31)
    {
        v2 = 0;
        v3 = 0;
        v1 = (&g_41e280)[g_420834 >> 3] >> ((char)g_420834 & 7) & 1;
    }
    v4 = _ccall(2, v2, v1, v3, 0);
    return v4;
}
```

## `sub_004083e5` `0x004083e5`

_3 bytes. (leaf/helper — see body)_

```c
int sub_4083e5(void)
{
    return sub_4083e8();
}
```

## `sub_004083e8` `0x004083e8`

_338 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_40853c;
extern unsigned int g_41e0a4;
extern unsigned int g_41e0b8;
extern unsigned int g_420830;
extern unsigned int g_420834;
extern unsigned int g_420838;
extern char g_42083c;
extern char g_42083d;

int sub_4083e8(void)
{
    unsigned int v4;  // eax
    unsigned int *i;  // esi
    unsigned int v14;  // 4117
    unsigned int j;  // eax
    char *iter;  // edx
    unsigned int v17;  // eax
    unsigned short *node;  // edx
    unsigned int v19;  // eax
    unsigned short v20;  // 4127
    unsigned int v21;  // eax
    unsigned int v22;  // eax
    unsigned int *iter1;  // edi
    unsigned int v7;  // ecx
    unsigned int v8;  // eax
    unsigned int v9;  // eax
    unsigned int v10;  // cc_op
    unsigned int v11;  // cc_dep1
    unsigned int v12;  // cc_dep2
    unsigned int v13;  // cc_ndep
    unsigned short v0[129];  // [bp-0x19a]
    Byte v1[148];  // [bp-0x98]
    char v2;  // [bp-0x4]

    g_420830 = 1033;
    g_420834 = 9;
    g_420838 = 1;
    v4 = sub_40530c();
    if (v4)
        g_420830 = v4;
    if ((unsigned short)v4)
    {
        g_420834 = (unsigned short)v4 & 0x3ff;
        g_420838 = (unsigned short)v4 >> 10;
    }
    i = &g_40853c;
    iter1 = &g_41e0b8;
    for (v7 = 8; v7; i += 1)
    {
        v7 -= 1;
        *(iter1) = *(i);
        iter1 += 1;
    }
    if (g_41e0a4 == 2)
    {
        v8 = sub_4083d0();
        if ((char)v8)
        {
            g_42083d = 0;
            g_42083c = 0;
            return v8;
        }
        sub_408370(&v2);
        v9 = sub_4029bc();
        v14 = _ccall(5, v10, v11, v12, v13);
        g_42083c = v14;
        if (((char)v14 & 1))
        {
            g_42083d = 0;
            return v9;
        }
        j = 128;
        iter = &v1[0];
        do
        {
            *(iter) = j;
            j += 1;
            iter += 1;
        } while (j != 0x100);
        GetStringTypeExA(g_420830, 2, v1, 128, v0);
        v17 = 128;
        node = &v0[0];
        do
        {
            v19 = v17;
            v20 = *(node);
            g_42083d = *(node) == 2;
        } while (v20 != 2 && (node += 2, v21 = v19 - 1, v17 = v19 - 1, v19 != 1));
        return v19;
    }
    else
    {
        g_42083d = GetSystemMetrics(SM_MIDEASTENABLED);
        v22 = GetSystemMetrics(SM_DBCSENABLED);
        g_42083c = v22;
        if (!v22)
            return v22;
        return sub_408370(&v2);
    }
}
```

## `sub_0040855c` `0x0040855c`

_701 bytes. refs ":mm", ":mm:ss", ":mm:ss"_

```c
typedef struct struct_0 {
    char field_0;
} struct_0;

typedef struct struct_2 {
    struct struct_0 *field_0;
} struct_2;

extern char g_420774;
extern char g_420775;
extern char g_420776;
extern char g_420777;
extern char g_420778;
extern char g_420779;
extern char g_420784;
extern char g_42083c;
extern char g_42083e;

int sub_40855c(void)
{
    unsigned int i;  // ecx
    unsigned long v19;  // ldt
    unsigned long v20;  // gdt
    unsigned short v21;  // fs
    unsigned long v22;  // 4127
    unsigned long v23;  // 4136
    int v24;  // ecx
    unsigned long v25;  // 4120
    unsigned int v0;  // [bp-0x68]
    struct_2 **v1;  // [bp-0x44]
    struct_0 **v2;  // [bp-0x40]
    struct_2 **v3;  // [bp-0x3c]
    struct_0 **v4;  // [bp-0x38]
    char *v5;  // [bp-0x34]
    struct_0 **v6;  // [bp-0x30]
    char *v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    char *v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x14]
    int v12;  // [bp-0x10]
    int v13;  // [bp-0xc]
    int v14;  // [bp-0x8]
    char v15;  // [bp-0x4]

    i = 8;
    do
    {
        v12 = 0;
        v11 = 0;
        i -= 1;
    } while (i != 1);
    v10 = &v15;
    v9 = sub_408827;
    v22 = _ccall(v19, v20, (unsigned int)v21, 0);
    v8 = *((int *)v22);
    v23 = _ccall(v19, v20, (unsigned int)v21, 0);
    *((unsigned int **)v23) = &v8;
    sub_4083e8();
    sub_407288();
    if (g_42083c)
        sub_407460();
    sub_40530c();
    v7 = &v11;
    sub_4071d8(&v11);
    sub_403a64(&v11);
    sub_4071d8(&/* unsupported instruction */);
    g_420774 = (unsigned int)sub_4064d0(v24, 0);
    v6 = &v10;
    sub_4071d8(&v10);
    g_420775 = (unsigned int)sub_4064d0(v24, 0);
    g_420776 = sub_407224();
    g_420777 = sub_407224();
    v5 = &v9;
    sub_4071d8(&v9);
    g_420778 = (unsigned int)sub_4064d0(v24, 0);
    g_420779 = sub_407224();
    v4 = &v7;
    sub_4071d8(&v7);
    sub_407510(&v7);
    sub_403a64();
    v3 = &v6;
    sub_4071d8(&v6);
    sub_407510(&v6);
    sub_403a64();
    g_420784 = sub_407224();
    v2 = &v5;
    sub_4071d8(&v5);
    sub_403a64(&v5);
    v1 = &v4;
    sub_4071d8(&v4);
    sub_403a64(&v4);
    sub_403a10();
    sub_403a10();
    sub_4071d8(&v3);
    if (!(unsigned int)sub_4064d0(v24, 0))
        sub_403aa8();
    else
        sub_403aa8();
    sub_4071d8(&v2);
    if (!(unsigned int)sub_4064d0(v24, 0))
    {
        sub_4071d8(&v1);
        if (!(unsigned int)sub_4064d0(v24, 0))
            sub_403aa8();
        else
            sub_403aa8();
    }
    sub_403d40(v12, ":mm", v14, v13);
    sub_403d40(v12, ":mm:ss", v14, v13);
    g_42083e = sub_407224(v12, ":mm:ss", v14, v13);
    v25 = _ccall(v19, v20, (unsigned int)v21, 0);
    *((int *)v25) = v12;
    v0 = sub_40882e;
    return sub_408819();
}
```

## `sub_00408819` `0x00408819`

_14 bytes. (leaf/helper — see body)_

```c
int sub_408819(void)
{
    return sub_403a34();
}
```

## `sub_00408827` `0x00408827`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_408827(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0040882c` `0x0040882c`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40882c(void)
{
    return sub_408819();
}
```

## `sub_0040882e` `0x0040882e`

_5 bytes. (leaf/helper — see body)_

```c
void sub_40882e(void)
{
    return;
}
```

## `sub_004088d4` `0x004088d4`

_31 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
} struct_0;

extern struct_0 *g_41e284;

int sub_4088d4(void)
{
    unsigned int i;  // eax

    for (; g_41e284; i = sub_402524())
    {
        g_41e284 = g_41e284->field_0;
    }
    return i;
}
```

## `sub_004088f3` `0x004088f3`

_1 bytes. (leaf/helper — see body)_

```c
void sub_4088f3(void)
{
    sub_4088f4();
    return;
}
```

## `sub_004088f4` `0x004088f4`

_54 bytes. refs "kernel32.dll", "GetDiskFreeSpaceExA"_

```c
extern void g_4065bc;
extern unsigned int g_41e0dc;

void* sub_4088f4(void)
{
    void* v1;  // eax
    void* v2;  // ebx

    v1 = sub_4052bc("kernel32.dll");
    v2 = v1;
    if (v2)
    {
        v1 = GetProcAddress(v2, "GetDiskFreeSpaceExA");
        g_41e0dc = v1;
    }
    if (!g_41e0dc)
    {
        v1 = &g_4065bc;
        g_41e0dc = &g_4065bc;
    }
    return v1;
}
```

## `sub_00408950` `0x00408950`

_14 bytes. (leaf/helper — see body)_

```c
int sub_408950(void)
{
    unsigned int *v1;  // eax

    *(v1) = 0;
    sub_402e1c();
    return;
}
```

## `sub_00408c30` `0x00408c30`

_372 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420880;

int sub_408c30(void)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4157
    unsigned int v9;  // 4105
    unsigned long v10;  // 4161
    unsigned int v11;  // 4117
    unsigned int v12;  // 4164
    unsigned long v13;  // 4118
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0x8]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v9 = *((int *)v8);
    v0 = *((int *)v8);
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v10) = &v0;
    v11 = g_420880;
    g_420880 = g_420880 + 1;
    v12 = _ccall(4, 18, v11 + 1, 0, 0);
    if ((char)v12)
    {
        sub_408950(v9, sub_408da5, &v2, &v3);
        sub_4088d4();
        sub_4080c0();
        sub_404124();
        sub_404124();
        sub_404124();
        sub_403a10();
        sub_404814();
        sub_404814();
        sub_404124();
        sub_404124();
        sub_404124();
        sub_404124();
        sub_404124();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403a10();
        sub_403fcc();
        sub_403a10();
    }
    v13 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v13) = v9;
    v1 = sub_408dac;
    return sub_408da4(&v3);
}
```

## `sub_00408da4` `0x00408da4`

_1 bytes. (leaf/helper — see body)_

```c
void sub_408da4(void)
{
    return;
}
```

## `sub_00408da5` `0x00408da5`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_408da5(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00408daa` `0x00408daa`

_2 bytes. (leaf/helper — see body)_

```c
void sub_408daa(void)
{
    sub_408da4();
    return;
}
```

## `sub_00408dac` `0x00408dac`

_2 bytes. (leaf/helper — see body)_

```c
void sub_408dac(unsigned int a0)
{
    return;
}
```

## `sub_00408dae` `0x00408dae`

_105 bytes. (leaf/helper — see body)_

```c
extern char g_420705;
extern unsigned int g_420880;

int sub_408dae(void)
{
    unsigned long v2;  // ldt
    unsigned long v3;  // gdt
    unsigned short v4;  // fs
    unsigned long v5;  // 4154
    unsigned int v6;  // 4105
    unsigned long v7;  // 4158
    unsigned int v8;  // 4119
    unsigned long v9;  // 4118
    unsigned int v0;  // [bp-0x10]

    v5 = _ccall(v2, v3, (unsigned int)v4, 0);
    v6 = *((int *)v5);
    v0 = *((int *)v5);
    v7 = _ccall(v2, v3, (unsigned int)v4, 0);
    *((unsigned int **)v7) = &v0;
    v8 = g_420880;
    g_420880 = g_420880 - 1;
    if (v8 < 1)
    {
        sub_4037bc(v6, sub_408e18, &/* unsupported instruction */, /* unsupported instruction */);
        sub_4037e4();
        if (g_420705)
            sub_403a64();
        sub_40803c();
        sub_40812c();
        sub_4088f4();
        sub_40855c();
    }
    v9 = _ccall(v2, v3, (unsigned int)v4, 0);
    *((unsigned int *)v9) = v6;
    return sub_408e17();
}
```

## `sub_00408e17` `0x00408e17`

_1 bytes. (leaf/helper — see body)_

```c
void sub_408e17(void)
{
    return;
}
```

## `sub_00408e18` `0x00408e18`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_408e18(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00408e1d` `0x00408e1d`

_2 bytes. (leaf/helper — see body)_

```c
void sub_408e1d(void)
{
    sub_408e17();
    return;
}
```

## `sub_00408e1f` `0x00408e1f`

_2 bytes. (leaf/helper — see body)_

```c
void sub_408e1f(unsigned int a0)
{
    return;
}
```

## `sub_00408e34` `0x00408e34`

_54 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[97];
    unsigned int field_61;
} struct_0;

typedef struct struct_1 {
    char padding_0[97];
    char field_61;
} struct_1;

extern char g_61;

void sub_408e34(unsigned int a0)
{
    unsigned int *v6;  // ebx
    unsigned int v7;  // 4098
    unsigned int v16;  // 4164
    struct_1 *idx;  // ebp
    char v18;  // 4118
    unsigned int v19;  // 4172
    char v20;  // 4128
    unsigned int v8;  // cc_op
    unsigned int v9;  // cc_dep1
    unsigned int v10;  // cc_dep2
    unsigned int v11;  // cc_ndep
    unsigned int v12;  // 4162
    unsigned int v13;  // 4163
    char *v14;  // eax
    char v15;  // cl
    struct_0 *v0;  // [bp+0x1]
    char *v2;  // [bp+0xd]
    unsigned int v3;  // [bp+0x15]
    char *v4;  // [bp+0x19]
    char v5;  // [bp+0x1d]

    v7 = *(v6);
    v12 = _ccall(v8, v9, v10, v11);
    *(v6) = *(v6) + a0 + (v12 & 1);
    v13 = _ccall(9, v7, a0 ^ v12 & 1, v12 & 1);
    v14 = v4;
    v15 = v3;
    v16 = _ccall(2, 18, v6 + 1, 0, v13);
    if ((char)v16)
    {
        *(v14) = *(v14) + *((char *)&v14);
        *(v14) = *(v14) + *((char *)&v14);
        *(v14) = *(v14) + *((char *)&v14);
        *(v14) = *(v14) | *((char *)&v14);
        *(v14) = *(v14) + *((char *)&v14);
    }
    idx = *((int *)&(v0->padding_0)[1]) * 1132;
    *(v14) = *(v14) + *((char *)&v14);
    *(v14) = *(v14) + *((char *)&v14);
    *(v2) = *(v2) + *((char *)&v14);
    *(v14) = *(v14) + *((char *)&v14);
    v18 = *(v14);
    *(v14) = *(v14) + *((char *)&v14);
    v19 = _ccall(1, (unsigned int)v18, (unsigned int)*((char *)(void*)&v14), 0);
    *(v14) = *(v14) + *((char *)&v14) + ((char)v19 & 1);
    v20 = idx->field_61;
    idx->field_61 = v20 | v15;
    v4 = &v5;
    if ((v20 | v15) >= 0)
        goto LABEL_0x408ec8;
    if ((v20 | v15) < 0)
        goto LABEL_0x408e5b;
    else
        goto LABEL_0x408de6;
}
```

## `sub_00408e7e` `0x00408e7e`

_10 bytes. (leaf/helper — see body)_

```c
int sub_408e7e(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6)
{
    unsigned int v1;  // cc_op
    unsigned int v2;  // cc_dep1
    unsigned int v3;  // cc_dep2
    unsigned int v4;  // cc_ndep
    unsigned int v5;  // 4121
    unsigned int v6;  // 4101
    char v0;  // [bp+0x20]

    v5 = _ccall(8, v1, v2, v3, v4);
    if (!((char)v5))
        return sub_408ef4(&v0);
    v6 = _ccall(2, v1, v2, v3, v4);
    if (!((char)v6))
        goto LABEL_0x408e13;
}
```

## `sub_00408ed4` `0x00408ed4`

_39 bytes. (leaf/helper — see body)_

```c
int sub_408ed4(void)
{
    unsigned short v5;  // cs
    char *v6;  // eax
    char *v7;  // ecx
    char v8;  // 4116
    char v9;  // bl
    unsigned int v10;  // 4198
    char *v11;  // eax
    unsigned int v12;  // 4201
    unsigned int v0;  // [bp-0x4]
    unsigned int v1;  // [bp+0x4]
    char *v2;  // [bp+0x14]
    unsigned int *v3;  // [bp+0x18]
    unsigned int *v4;  // [bp+0x1c]

    *((unsigned short *)&v0) = v5;
    *(v6) = *(v6) + *((char *)&v6);
    *(v6) = *(v6) + *((char *)&v6);
    *(v7) = *(v7) + *((char *)&v6);
    *(v6) = *(v6) + *((char *)&v6);
    v8 = *(v6);
    *(v6) = *(v6) + v9;
    v10 = _ccall(1, (unsigned int)v8, (unsigned int)v9, 0);
    *(v6) = *(v6) + *((char *)&v6) + ((char)v10 & 1);
    v11 = _INSERT(v6, 0, *((char *)&v6));
    *(v11) = *(v11) + *((char *)&v6);
    v12 = _ccall(8, 18, v1 + 1, 0, 0);
    if ((char)v12)
    {
        *(v3) = *(v4);
        sub_408f54();
        return;
    }
    else if (!((char)(v1 == 2147483647 ? 1 : 0)))
    {
        __unsupported_jumpkind_Ijk_NoDecode()
    }
    else
    {
        *(v2) = *(v2) + *((char *)&v3);
        return;
    }
}
```

## `sub_00408ef4` `0x00408ef4`

_58 bytes. (leaf/helper — see body)_

```c
int sub_408ef4(void)
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

## `sub_00408f2e` `0x00408f2e`

_34 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420890;

int sub_408f2e(void)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4147
    unsigned long v8;  // 4156
    unsigned long v9;  // 4172
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v2 = &/* unsupported instruction */;
    v1 = sub_408f55;
    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v0 = *((int *)v7);
    v8 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v8) = &v0;
    g_420890 = g_420890 + 1;
    v9 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v9) = v0;
}
```

## `sub_00408f54` `0x00408f54`

_1 bytes. (leaf/helper — see body)_

```c
void sub_408f54(void)
{
    return;
}
```

## `sub_00408f55` `0x00408f55`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_408f55(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00408f5a` `0x00408f5a`

_2 bytes. (leaf/helper — see body)_

```c
void sub_408f5a(void)
{
    sub_408f54();
    return;
}
```

