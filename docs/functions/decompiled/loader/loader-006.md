# elfbot.dll decompiled — loader 0x0040448c..0x00404ee6

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_0040448c` `0x0040448c`

_7 bytes. (leaf/helper — see body)_

```c
char sub_40448c(void)
{
    return sub_4025ec();
}
```

## `sub_00404493` `0x00404493`

_1 bytes. (leaf/helper — see body)_

```c
void sub_404493(void)
{
    return;
}
```

## `sub_00404494` `0x00404494`

_35 bytes. (leaf/helper — see body)_

```c
int sub_404494(void)
{
    return;
}
```

## `sub_004044b7` `0x004044b7`

_1 bytes. (leaf/helper — see body)_

```c
void sub_4044b7(void)
{
    return;
}
```

## `sub_004044b8` `0x004044b8`

_120 bytes. (leaf/helper — see body)_

```c
int sub_4044b8(void)
{
    unsigned int v3;  // edi
    unsigned int v4;  // ebx
    int v13;  // ebp
    unsigned int v14;  // ecx
    int v15;  // edi
    unsigned int v16;  // esi
    unsigned int v17;  // ecx
    unsigned int v18;  // 4160
    unsigned long long v19;  // 4161
    unsigned long long v20;  // 4164
    unsigned int v21;  // esi
    int v5;  // edx
    unsigned long v22;  // 4167
    unsigned int v24;  // ecx
    int v6;  // edx
    int v7;  // edx
    unsigned int v8;  // eax
    unsigned int v9;  // eax
    unsigned int v11;  // ebx
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp+0x4]
    int v2;  // [bp+0x8]

    v3 = 0;
    v4 = v1;
    if (!v2 && (!v5 || !v4))
        return;
    v7 = v6;
    v9 = v8;
    if (v6 < 0)
    {
        v7 = -(v7) - (0 < v8);
        v3 = 1;
        v9 = -(v8);
    }
    v11 = v4;
    if (v2 < 0)
    {
        v2 = -(v2) - (0 < v4);
        v3 ^= 1;
        v11 = -(v4);
    }
    v13 = v2;
    v14 = 64;
    v0 = v3;
    v15 = 0;
    v16 = 0;
    do
    {
        v17 = v14;
        v9 *= 2;
        v18 = _ccall(24, v9 * 2, v9, 0);
        v19 = _ccall(v7, 1, v18, 4);
        v7 = v19;
        v20 = _ccall(v16, 1, (unsigned int)(v19 >> 32) & 2261, 4);
        v21 = v20;
        v22 = _ccall(v15, 1, (unsigned int)(v20 >> 32) & 2261, 4);
        v15 = v22;
        v16 = v21;
        if (v15 >= v13 && (v15 > v13 || (v16 = v21, v21 >= v11)))
        {
            v15 = v15 - v13 - (v21 < v11);
            v9 += 1;
            v16 = v21 - v11;
        }
    } while ((v24 = v17 - 1, v14 = v17 - 1, v17 != 1));
    return;
}
```

## `sub_00404534` `0x00404534`

_73 bytes. (leaf/helper — see body)_

```c
int sub_404534(void)
{
    unsigned int v2;  // ebx
    unsigned int v3;  // edx
    unsigned int v9;  // 4160
    unsigned long long v10;  // 4161
    unsigned long long v11;  // 4164
    unsigned int v12;  // esi
    unsigned long v13;  // 4167
    unsigned int v14;  // esi
    unsigned int v16;  // ecx
    unsigned int v4;  // edx
    unsigned int v5;  // ecx
    unsigned int v6;  // edi
    unsigned int v7;  // eax
    unsigned int v8;  // ecx
    unsigned int v0;  // [bp+0x4]
    unsigned int v1;  // [bp+0x8]

    v2 = v0;
    if (!v1 && (!v3 || !v2))
        return;
    v5 = 64;
    v6 = 0;
    v14 = 0;
    do
    {
        v8 = v5;
        v7 *= 2;
        v9 = _ccall(24, v7 * 2, v7, 0);
        v10 = _ccall(v4, 1, v9, 4);
        v4 = v10;
        v11 = _ccall(v14, 1, (unsigned int)(v10 >> 32) & 2261, 4);
        v12 = v11;
        v13 = _ccall(v6, 1, (unsigned int)(v11 >> 32) & 2261, 4);
        v6 = v13;
        v14 = v12;
        if (v6 >= v1 && (v6 > v1 || (v14 = v12, v12 >= v2)))
        {
            v6 = v6 - v1 - (v12 < v2);
            v7 += 1;
            v14 = v12 - v2;
        }
    } while ((v16 = v8 - 1, v5 = v8 - 1, v8 != 1));
    return;
}
```

## `sub_0040457d` `0x0040457d`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40457d(void)
{
    return;
}
```

## `sub_0040457e` `0x0040457e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40457e(unsigned int a0, unsigned int a1)
{
    return sub_404580();
}
```

## `sub_00404580` `0x00404580`

_122 bytes. (leaf/helper — see body)_

```c
int sub_404580(void)
{
    unsigned int v3;  // edi
    unsigned int v4;  // ebx
    int v13;  // ebp
    unsigned int v14;  // ecx
    int v15;  // edi
    unsigned int v16;  // esi
    unsigned int v17;  // ecx
    unsigned int v18;  // 4160
    unsigned long long v19;  // 4161
    unsigned long long v20;  // 4164
    unsigned int v21;  // esi
    int v5;  // edx
    unsigned long v22;  // 4167
    unsigned int v24;  // ecx
    int v6;  // edx
    int v7;  // edx
    unsigned int v8;  // eax
    unsigned int v9;  // eax
    unsigned int v11;  // ebx
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp+0x4]
    int v2;  // [bp+0x8]

    v3 = 0;
    v4 = v1;
    if (!v2 && (!v5 || !v4))
        return;
    v7 = v6;
    v9 = v8;
    if (v6 < 0)
    {
        v7 = -(v7) - (0 < v8);
        v3 = 1;
        v9 = -(v8);
    }
    v11 = v4;
    if (v2 < 0)
    {
        v2 = -(v2) - (0 < v4);
        v11 = -(v4);
    }
    v13 = v2;
    v14 = 64;
    v0 = v3;
    v15 = 0;
    v16 = 0;
    do
    {
        v17 = v14;
        v9 *= 2;
        v18 = _ccall(24, v9 * 2, v9, 0);
        v19 = _ccall(v7, 1, v18, 4);
        v7 = v19;
        v20 = _ccall(v16, 1, (unsigned int)(v19 >> 32) & 2261, 4);
        v21 = v20;
        v22 = _ccall(v15, 1, (unsigned int)(v20 >> 32) & 2261, 4);
        v15 = v22;
        v16 = v21;
        if (v15 >= v13 && (v15 > v13 || (v16 = v21, v21 >= v11)))
        {
            v15 = v15 - v13 - (v21 < v11);
            v9 += 1;
            v16 = v21 - v11;
        }
    } while ((v24 = v17 - 1, v14 = v17 - 1, v17 != 1));
    return;
}
```

## `sub_004045fa` `0x004045fa`

_1 bytes. (leaf/helper — see body)_

```c
void sub_4045fa(void)
{
    return;
}
```

## `sub_004045fb` `0x004045fb`

_1 bytes. (leaf/helper — see body)_

```c
void sub_4045fb(unsigned int a0, unsigned int a1)
{
    sub_4045fc();
    return;
}
```

## `sub_004045fc` `0x004045fc`

_78 bytes. (leaf/helper — see body)_

```c
int sub_4045fc(void)
{
    unsigned int v2;  // ebx
    unsigned int v3;  // edx
    unsigned int v9;  // 4160
    unsigned long long v10;  // 4161
    unsigned long long v11;  // 4164
    unsigned int v12;  // esi
    unsigned long v13;  // 4167
    unsigned int v14;  // esi
    unsigned int v16;  // ecx
    unsigned int v4;  // edx
    unsigned int v5;  // ecx
    unsigned int v6;  // edi
    unsigned int v7;  // eax
    unsigned int v8;  // ecx
    unsigned int v0;  // [bp+0x4]
    unsigned int v1;  // [bp+0x8]

    v2 = v0;
    if (!v1 && (!v3 || !v2))
        return;
    v5 = 64;
    v6 = 0;
    v14 = 0;
    do
    {
        v8 = v5;
        v7 *= 2;
        v9 = _ccall(24, v7 * 2, v7, 0);
        v10 = _ccall(v4, 1, v9, 4);
        v4 = v10;
        v11 = _ccall(v14, 1, (unsigned int)(v10 >> 32) & 2261, 4);
        v12 = v11;
        v13 = _ccall(v6, 1, (unsigned int)(v11 >> 32) & 2261, 4);
        v6 = v13;
        v14 = v12;
        if (v6 >= v1 && (v6 > v1 || (v14 = v12, v12 >= v2)))
        {
            v6 = v6 - v1 - (v12 < v2);
            v7 += 1;
            v14 = v12 - v2;
        }
    } while ((v16 = v8 - 1, v5 = v8 - 1, v8 != 1));
    return;
}
```

## `sub_0040464a` `0x0040464a`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40464a(void)
{
    return;
}
```

## `sub_0040464b` `0x0040464b`

_1 bytes. (leaf/helper — see body)_

```c
int sub_40464b(void)
{
    sub_40464c();
    return;
}
```

## `sub_0040464c` `0x0040464c`

_8 bytes. (leaf/helper — see body)_

```c
int sub_40464c(void)
{
    return;
}
```

## `sub_00404654` `0x00404654`

_7 bytes. (leaf/helper — see body)_

```c
int sub_404654(void)
{
    return sub_40464c() - 1;
}
```

## `sub_0040465b` `0x0040465b`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40465b(unsigned int a0)
{
    sub_40465c();
    return;
}
```

## `sub_0040465c` `0x0040465c`

_15 bytes. (leaf/helper — see body)_

```c
void sub_40465c(int a0)
{
    char v0;  // [bp+0x0]

    sub_404338(a0, &v0);
    return;
}
```

## `sub_0040466b` `0x0040466b`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40466b(void)
{
    sub_40466c();
    return;
}
```

## `sub_0040466c` `0x0040466c`

_5 bytes. (leaf/helper — see body)_

```c
void sub_40466c(unsigned int a0)
{
    sub_404124();
    return;
}
```

## `sub_00404671` `0x00404671`

_1 bytes. (leaf/helper — see body)_

```c
void sub_404671(void)
{
    return;
}
```

## `sub_00404672` `0x00404672`

_2 bytes. (leaf/helper — see body)_

```c
int sub_404672(void)
{
    return sub_404674();
}
```

## `sub_00404674` `0x00404674`

_6 bytes. (leaf/helper — see body)_

```c
void sub_404674(void)
{
    sub_404814();
    return;
}
```

## `sub_0040467a` `0x0040467a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40467a(void)
{
    sub_40467c();
    return;
}
```

## `sub_0040467c` `0x0040467c`

_396 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[1];
    char field_1;
    unsigned int field_2;
    struct struct_1 *field_6;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_40467c(void)
{
    unsigned int v11;  // ebx
    unsigned int v12;  // esi
    unsigned int v21;  // esi
    void* v22;  // eax
    void* v23;  // ebx
    unsigned int v24;  // edi
    int v25;  // edi
    int i;  // edi
    unsigned int v27;  // edi
    unsigned int v13;  // edi
    int v14;  // ecx
    void* *v15;  // eax
    void* v16;  // ebx
    int v17;  // edi
    unsigned int v18;  // ebx
    struct_0 *v19;  // edx
    struct_0 *v20;  // eax
    unsigned int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x2c]
    unsigned int v2;  // [bp-0x28]
    void* v3;  // [bp-0x24]
    unsigned int v4;  // [bp-0x20]
    unsigned int v5;  // [bp-0x1c]
    int v6;  // [bp-0x18]
    int v7;  // [bp-0x14]
    unsigned int v8;  // [bp-0x10]
    int v9;  // [bp-0xc]
    int *iter;  // [bp+0x4]

    v2 = v11;
    v1 = v12;
    v0 = v13;
    v9 = v14;
    v16 = *(v15);
    v17 = *(iter);
    if (v17 <= 0)
    {
        if (v17 < 0)
            sub_4025ec();
        sub_404674();
        return;
    }
    else
    {
        v7 = 0;
        if (v16)
        {
            v18 = v16 - 4;
            v7 = *((int *)v18);
            v16 = v18 - 4;
        }
        v20 = &(v19->padding_0)[v19->field_1];
        v5 = *((int *)&(&v20->field_1)[1]);
        v21 = (!*((int *)((char *)&v20->field_2 + 2)) ? NULL : *((int *)*((int *)((char *)&v20->field_2 + 2))));
        v4 = v17 * v5;
        if (v4 / v17 != v5)
            sub_4025ec();
        v4 += 8;
        if (!v16 || *((int *)v16) == 1)
        {
            v3 = v16;
            if (v17 < v7 && v21)
                sub_40466c(v7 - v17);
            sub_402544();
            v22 = v3;
        }
        else
        {
            *((unsigned int *)v16) = *((int *)v16) - 1;
            v22 = sub_402504();
            v6 = v7;
            if (v17 < v6)
                v6 = v17;
            if (v21)
            {
                sub_4028d0();
                sub_40465c(v6);
            }
            else
            {
                sub_402628();
            }
        }
        *((unsigned int *)v22) = 1;
        v23 = v22 + 4;
        *((int *)v23) = v17;
        sub_4028d0();
        if (v9 > 1)
        {
            iter += 1;
            v9 -= 1;
            v24 = v17 - 1;
            if (v24 >= 0)
            {
                v25 = v24 + 1;
                v8 = 0;
                do
                {
                    i = v25;
                    sub_40467c(iter);
                    v8 += 1;
                    v27 = i - 1;
                    v25 = v27;
                } while (i != 1);
            }
        }
        *(v15) = v23 + 4;
        return;
    }
}
```

## `sub_00404808` `0x00404808`

_11 bytes. (leaf/helper — see body)_

```c
void sub_404808(void)
{
    char v0;  // [bp+0x0]

    sub_40467c(&v0 + 4);
    return;
}
```

## `sub_00404813` `0x00404813`

_1 bytes. (leaf/helper — see body)_

```c
int sub_404813(void)
{
    sub_404814();
    return;
}
```

## `sub_00404814` `0x00404814`

_58 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[1];
    char field_1;
} struct_0;

int sub_404814(void)
{
    void* *v1;  // eax
    void* v2;  // ecx
    struct_0 *v3;  // edx

    v2 = *(v1);
    if (!v2)
        return;
    *(v1) = NULL;
    InterlockedDecrement(v2 - 8);
    if ((int)v2[8] != 1)
        return;
    if (*((int *)&(v3[3].padding_0)[v3->field_1]) && (int)v2[4])
        sub_404124();
    sub_402524(v1);
    return;
}
```

## `sub_0040484e` `0x0040484e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40484e(void)
{
    sub_404850();
    return;
}
```

## `sub_00404850` `0x00404850`

_39 bytes. (leaf/helper — see body)_

```c
int sub_404850(void)
{
    void* *v1;  // eax
    void* v2;  // ebx
    int v3;  // edx
    void* *v4;  // eax
    int v5;  // edx

    v2 = *(v1);
    if (v3)
        InterlockedIncrement(v3 - 8);
    if (v2)
    {
        InterlockedDecrement(v2 - 8);
        if ((int)v2[8] == 1)
        {
            *((unsigned int *)&v2[8]) = (int)v2[8] + 1;
            sub_404814(v3, v1);
        }
    }
    *(v4) = v5;
    return;
}
```

## `sub_00404877` `0x00404877`

_1 bytes. (leaf/helper — see body)_

```c
int sub_404877(void)
{
    sub_404878();
    return;
}
```

## `sub_00404878` `0x00404878`

_71 bytes. (leaf/helper — see body)_

```c
int sub_404878(void)
{
    HMODULE idx[5];  // eax
    unsigned int v5;  // esi
    Byte v0[4];  // [bp-0x110]
    int v1;  // [bp-0x10c]
    int v2;  // [bp-0x108]

    if (idx[4])
        return;
    GetModuleFileNameA(idx[1], v0, 261);
    v5 = sub_404ab4(v0, v1, v2);
    idx[4] = v5;
    if (v5)
        return;
    idx[4] = idx[1];
    return;
}
```

## `sub_004048bf` `0x004048bf`

_1 bytes. (leaf/helper — see body)_

```c
void sub_4048bf(void)
{
    sub_4048c0();
    return;
}
```

## `sub_004048c0` `0x004048c0`

_40 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
    char padding_4[8];
    unsigned int field_c;
} struct_0;

extern struct_0 *g_41e01c;

int sub_4048c0(void)
{
    struct_0 *v1;  // edx
    struct_0 *v2;  // edx
    unsigned int v3;  // eax

    v1 = g_41e01c;
    if (!g_41e01c)
        return;
    while (true)
    {
        v2 = v1;
        if (v3 == *((int *)&v2->padding_4[0]))
        {
            sub_404878();
            return;
        }
        else if (v3 == *((int *)&v2->padding_4[4]))
        {
            sub_404878();
            return;
        }
        else if (v3 == v2->field_c)
        {
            sub_404878();
            return;
        }
        else
        {
            v1 = v2->field_0;
            if (!v2->field_0)
                return;
        }
    }
}
```

## `sub_004048e8` `0x004048e8`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4048e8(void)
{
    sub_4048f0();
    return;
}
```

## `sub_004048f0` `0x004048f0`

_18 bytes. (leaf/helper — see body)_

```c
int sub_4048f0(void)
{
    PSTR v1;  // eax
    char *i;  // eax

    for (; *(i); i = CharNextA(v1))
    {
        if (*(i) == 92)
            return;
    }
    return;
}
```

## `sub_004048fc` `0x004048fc`

_404 bytes. refs "kernel32.dll", "GetLongPathNameA"_

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

int sub_4048fc(void)
{
    unsigned int v8;  // ebx
    unsigned int v9;  // esi
    char v18[2];  // edi
    int v19;  // eax
    HANDLE v20;  // esi
    int v21;  // edx
    unsigned int v10;  // edi
    char v11[2];  // eax
    void* v12;  // esi
    unsigned int *v13;  // ebx
    char v15[2];  // esi
    char v16[2];  // ebx
    char v17[2];  // esi
    unsigned int v0;  // [bp-0x260]
    unsigned int v1;  // [bp-0x25c]
    unsigned int v2;  // [bp-0x258]
    Byte v3;  // [bp-0x253]
    char v4;  // [bp-0x252]
    WIN32_FIND_DATAA v5;  // [bp-0x14e]
    char v6[2];  // [bp-0x10]

    v2 = v8;
    v1 = v9;
    v0 = v10;
    v6 = v11;
    v12 = sub_4010e8("kernel32.dll");
    if (v12)
    {
        v13 = sub_4010f0(v12, "GetLongPathNameA");
        if (v13 && v13(v11, &v3, 261))
        {
            lstrcpynA(v11, &v3, v21);
            return;
        }
    }
    if (v11[0] != 92)
    {
        v15 = v11 + 1;
    }
    else if (v11[1] != 92)
    {
        return;
    }
    else if (*((char *)sub_4048e8()))
    {
        v15 = sub_4048e8();
        if (!v15[0])
            return;
    }
    else
    {
        return;
    }
    v16 = v15 - v11;
    lstrcpynA(&v3, v11, &v16[1]);
    while (true)
    {
        v17 = v15;
        if (!v17[0])
        {
            lstrcpynA(v11, &v3, v21);
            return;
        }
        v18 = sub_4048e8();
        v19 = v18 - v17;
        if (&v16[v19 + 1] > 261)
            return;
        lstrcpynA(&v3 + v16, v17, v19 + 1);
        v20 = FindFirstFileA(&v3, &v5);
        if (v20 == 0xffffffff)
            return;
        FindClose(v20);
        if (&v16[sub_401120(v5.cFileName) + 2] > 261)
            return;
        *((char *)(&v3 + v16)) = 92;
        lstrcpynA(&v4 + v16, v5.cFileName, 260 + -0x1 * v16);
        v16 = &v16[1 + sub_401120(v5.cFileName)];
        v15 = v18;
    }
}
```

## `sub_00404ab4` `0x00404ab4`

_541 bytes. refs "Software\\Borland\\Locales", "Software\\Borland\\Locales", "Software\\Borland\\Delphi\\Locales"_

```c
extern unsigned int g_404bc0;
extern unsigned int g_404d20;

int sub_404ab4(void)
{
    PSTR v11;  // eax
    unsigned long v21;  // 4134
    unsigned long v22;  // 4121
    HMODULE v13;  // esi
    char *i;  // ebx
    char *v15;  // ebx
    unsigned long v16;  // ldt
    unsigned long v17;  // gdt
    unsigned short v18;  // fs
    unsigned long v19;  // 4125
    unsigned int v20;  // 4103
    unsigned int v0;  // [bp-0x138]
    unsigned int v1;  // [bp-0x130]
    unsigned int v2[65];  // [bp-0x121]
    unsigned int v3;  // [bp-0x1c]
    char v4;  // [bp-0x16]
    char v5;  // [bp-0x12]
    Byte v6[2];  // [bp-0x11]
    char v7;  // [bp-0xf]
    PSTR v8;  // [bp-0xc], Other Possible Types: char
    char v9;  // [bp-0x4]

    GetModuleFileNameA(NULL, v2, 261);
    v4 = 0;
    if (sub_401130(0x80000001, "Software\\Borland\\Locales", 0, 0xf0019, &v8) && sub_401130(0x80000002, "Software\\Borland\\Locales", 0, 0xf0019, &v8) && sub_401130(0x80000001, "Software\\Borland\\Delphi\\Locales", 0, 0xf0019, &v8))
    {
        lstrcpynA(v2, v11, 261);
        GetLocaleInfoA(GetThreadLocale(), 3, v6, 5);
        v13 = NULL;
        if (!v2)
            return;
        if (!v6 && !v4)
            return;
        for (i = sub_401120(v2) + (char *)v2; *(i) != 46 && i != v2; i += 1);
        if (i == v2)
            return;
        v15 = i + 1;
        if (v4)
        {
            lstrcpynA(v15, &v4, 261 - (v15 - v2));
            v13 = sub_401108(v2, 0, 2);
        }
        if (v13)
        {
            return;
        }
        else if (v6)
        {
            lstrcpynA(v15, v6, 261 - (v15 - v2));
            if (sub_401108(v2, 0, 2))
                return;
            v7 = 0;
            lstrcpynA(v15, v6, 261 - (v15 - v2));
            sub_401108(v2, 0, 2);
            return;
        }
        else
        {
            return;
        }
    }
    v19 = _ccall(v16, v17, (unsigned int)v18, 0);
    v20 = *((int *)v19);
    v0 = *((int *)v19);
    v21 = _ccall(v16, v17, (unsigned int)v18, 0);
    *((unsigned int **)v21) = &v0;
    v3 = 5;
    sub_4048fc(v20, sub_404bb9, &v9);
    if (sub_401138(v8, v2, NULL, NULL, &v4, &v3) && sub_401138(v8, &g_404d20, NULL, NULL, &v4, &v3))
        v4 = 0;
    v5 = 0;
    v22 = _ccall(v16, v17, (unsigned int)v18, 0);
    *((unsigned int *)v22) = v20;
    v1 = &g_404bc0;
    sub_404baf();
    return;
}
```

## `sub_00404baf` `0x00404baf`

_10 bytes. (leaf/helper — see body)_

```c
enum WIN32_ERROR sub_404baf(void)
{
    unsigned int v1;  // [bp+0xffffc]

    return sub_401128(v1);
}
```

## `sub_00404bb9` `0x00404bb9`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_404bb9(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00404bbe` `0x00404bbe`

_2 bytes. (leaf/helper — see body)_

```c
enum WIN32_ERROR sub_404bbe(void)
{
    return sub_404baf();
}
```

## `sub_00404d24` `0x00404d24`

_80 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
    struct struct_1 *field_4;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_0 *g_41e020;

int sub_404d24(void)
{
    unsigned int v5;  // eax
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4127
    unsigned int v10;  // 4103
    unsigned long v11;  // 4136
    unsigned long v12;  // 4116
    unsigned int v0;  // [bp-0x24]
    struct_0 *v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]

    v2 = v5;
    v1 = g_41e020;
    if (!v1)
        return;
    do
    {
        v9 = _ccall(v6, v7, (unsigned int)v8, 0);
        v10 = *((int *)v9);
        v0 = *((int *)v9);
        v11 = _ccall(v6, v7, (unsigned int)v8, 0);
        *((unsigned int **)v11) = &v0;
        v1->field_4(v10, sub_404d5f, &v3);
        v12 = _ccall(v6, v7, (unsigned int)v8, 0);
        *((unsigned int *)v12) = v10;
    } while ((v1 = (struct_0 *)v1->field_0, v1));
    return;
}
```

## `sub_00404d5f` `0x00404d5f`

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

unsigned int sub_404d5f(int a0)
{
    struct_1 *v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x8]

    return sub_4030c0(v0, a0, v1);
}
```

## `sub_00404d64` `0x00404d64`

_5 bytes. (leaf/helper — see body)_

```c
void sub_404d64(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int *a10)
{
    unsigned int v0;  // [bp+0x0]

    sub_4034ec(v0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10);
}
```

## `sub_00404d7e` `0x00404d7e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_404d7e(void)
{
    sub_404d80();
    return;
}
```

## `sub_00404d80` `0x00404d80`

_14 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_41e01c;

int sub_404d80(void)
{
    unsigned int *v1;  // eax

    *(v1) = g_41e01c;
    g_41e01c = v1;
    return;
}
```

## `sub_00404d8e` `0x00404d8e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_404d8e(void)
{
    sub_404d90();
    return;
}
```

## `sub_00404d90` `0x00404d90`

_45 bytes. (leaf/helper — see body)_

```c
int sub_404d90(void)
{
    unsigned int v6;  // ecx
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4138
    unsigned int v11;  // 4108
    unsigned long v12;  // 4147
    int v13;  // eax
    unsigned long v14;  // 4118
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v2 = v6;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v11 = *((int *)v10);
    v0 = *((int *)v10);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v12) = &v0;
    sub_404d24(v11, sub_404df4, &v3, v13, &v4);
    v14 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v14) = v11;
    v1 = sub_404dfb;
    sub_404dbd(v13, &v4);
    return;
}
```

## `sub_00404dbd` `0x00404dbd`

_55 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_41e01c;

unsigned int * sub_404dbd(void)
{
    unsigned int *v2;  // eax
    unsigned int *i;  // [bp+0x100000]

    if (i == g_41e01c)
    {
        g_41e01c = *(i);
        return g_41e01c;
    }
    v2 = &g_41e01c->field_0;
    if (!g_41e01c)
        return g_41e01c;
    while (*(v2) != i)
    {
        v2 = *(v2);
        if (!v2)
            return v2;
    }
    *(v2) = *(i);
    return v2;
}
```

## `sub_00404df4` `0x00404df4`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_404df4(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00404df9` `0x00404df9`

_2 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_404df9(void)
{
    return sub_404dbd();
}
```

## `sub_00404dfb` `0x00404dfb`

_3 bytes. (leaf/helper — see body)_

```c
void sub_404dfb(unsigned int a0, unsigned int a1)
{
    return;
}
```

## `sub_00404dfe` `0x00404dfe`

_2 bytes. (leaf/helper — see body)_

```c
int sub_404dfe(void)
{
    sub_404e00();
    return;
}
```

## `sub_00404e00` `0x00404e00`

_21 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    struct struct_0 *field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[8];
    struct struct_1 *field_8;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_404e00(void)
{
    struct_2 **v1;  // eax
    struct_0 **v2;  // edx

    v2 = *(v1);
    if (v2)
    {
        *(v1) = NULL;
        *(v2)->field_8(v2, v1);
    }
    return;
}
```

## `sub_00404e15` `0x00404e15`

_3 bytes. (leaf/helper — see body)_

```c
int sub_404e15(unsigned int a0, unsigned int a1)
{
    return sub_404e18();
}
```

## `sub_00404e18` `0x00404e18`

_44 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    struct struct_0 *field_0;
    struct struct_1 *field_4;
} struct_2;

typedef struct struct_10 {
    struct struct_0 *field_0;
} struct_10;

typedef struct struct_0 {
    char padding_0[8];
    struct struct_1 *field_8;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_404e18(void)
{
    struct_2 **v1;  // edx
    struct_2 *v2;  // eax
    struct_2 *v3;  // ecx
    struct_10 **v4;  // eax
    struct_0 **v5;  // ecx

    if (v1)
    {
        *(v1)->field_4(v1, v2, v1);
        v3 = *(v1);
        *(v1) = v2;
        if (!v3)
            return;
        v3->field_0->field_8(v3);
        return;
    }
    else
    {
        v5 = *(v4);
        *(v4) = NULL;
        if (!v5)
            return;
        *(v5)->field_8(v5);
        return;
    }
}
```

## `sub_00404e44` `0x00404e44`

_86 bytes. (leaf/helper — see body)_

```c
int sub_404e44(void)
{
    void* v2;  // eax
    unsigned int v3;  // eax
    Byte v0[1024];  // [bp-0x408]

    if (!v2)
    {
        return;
    }
    else if ((int)v2[4] < 0x10000)
    {
        v3 = sub_4048c0((int)v2[4], v0, 0x400);
        LoadStringA(v3, (int)v2[4], v0, 0x400);
        sub_403b00(v0);
        return;
    }
    else
    {
        sub_403be8();
        return;
    }
}
```

## `sub_00404e9a` `0x00404e9a`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_4205b4;

int sub_404e9a(void)
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
    v9 = g_4205b4;
    g_4205b4 = g_4205b4 + 1;
    v10 = _ccall(4, 18, v9 + 1, 0, 0);
    if ((char)v10)
    {
        sub_402808(v7, sub_404ee6, &/* unsupported instruction */, /* unsupported instruction */);
        sub_402808();
        sub_402808();
        sub_401914();
    }
    v11 = _ccall(v3, v4, (unsigned int)v5, 0);
    *((unsigned int *)v11) = v7;
    v1 = sub_404eed;
    return sub_404ee5(/* unsupported instruction */);
}
```

## `sub_00404ee5` `0x00404ee5`

_1 bytes. (leaf/helper — see body)_

```c
void sub_404ee5(void)
{
    return;
}
```

## `sub_00404ee6` `0x00404ee6`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_404ee6(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

