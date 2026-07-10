# elfbot.dll decompiled — loader 0x0040f90a..0x004113cc

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_0040f90a` `0x0040f90a`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40f90a(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0040f90f` `0x0040f90f`

_2 bytes. (leaf/helper — see body)_

```c
char sub_40f90f(void)
{
    return sub_40f8fe();
}
```

## `sub_0040fb27` `0x0040fb27`

_40 bytes. (leaf/helper — see body)_

```c
int sub_40fb27(void)
{
    sub_404124();
    return sub_4040f0();
}
```

## `sub_0040fb4f` `0x0040fb4f`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40fb4f(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0040fb54` `0x0040fb54`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40fb54(void)
{
    return sub_40fb27();
}
```

## `sub_0040fb56` `0x0040fb56`

_12 bytes. (leaf/helper — see body)_

```c
int sub_40fb56(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // [bp+0x100000]

    return v0;
}
```

## `sub_0040fb62` `0x0040fb62`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40fb62(void)
{
    return sub_40fb64();
}
```

## `sub_0040fb64` `0x0040fb64`

_437 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_41ed94;

unsigned int sub_40fb64(unsigned int a0)
{
    unsigned int v12;  // ebx
    unsigned int v13;  // esi
    int v22;  // ecx
    unsigned int *v23;  // ebx
    unsigned long v24;  // 4123
    unsigned int v26;  // esi
    int v27;  // edx
    unsigned long v28;  // 4154
    unsigned int v29;  // 4103
    unsigned long v30;  // 4158
    unsigned int ch;  // eax
    unsigned int v14;  // edi
    unsigned int v32;  // eax
    unsigned int v33;  // eax
    unsigned long v34;  // 4116
    HANDLE ch1;  // eax
    HANDLE ch2;  // eax
    enum WIN32_ERROR v37;  // esi
    unsigned long v15;  // ldt
    unsigned long v16;  // gdt
    unsigned short v17;  // fs
    unsigned long v18;  // 4123
    unsigned int v19;  // 4103
    unsigned long v20;  // 4132
    unsigned int v21;  // eax
    unsigned int v0;  // [bp-0x40]
    unsigned int v1;  // [bp-0x3c]
    unsigned int v2;  // [bp-0x38]
    char *v3;  // [bp-0x34], Other Possible Types: unsigned int
    unsigned int v4;  // [bp-0x30]
    unsigned int v5;  // [bp-0x2c]
    unsigned int v6;  // [bp-0x28]
    char v7;  // [bp-0x24]
    unsigned int v8;  // [bp-0x14]
    HANDLE v9;  // [bp-0xc]
    unsigned int v10;  // [bp-0x8]
    char v11;  // [bp-0x4]

    v6 = v12;
    v5 = v13;
    v4 = v14;
    v10 = 0;
    if (GetCurrentProcess() == a0)
    {
        v10 = GetCurrentProcessId();
        return v10;
    }
    else if ((GetVersion() & 0x80000000))
    {
        v3 = &v11;
        v2 = sub_40fbc2;
        v18 = _ccall(v15, v16, (unsigned int)v17, 0);
        v19 = *((int *)v18);
        v1 = *((int *)v18);
        v20 = _ccall(v15, v16, (unsigned int)v17, 0);
        *((unsigned int **)v20) = &v1;
        v21 = GetCurrentProcessId();
        v23 = *((int *)((v21 ^ sub_40dc38(v22)) + 0x44));
        v24 = _ccall(v15, v16, (unsigned int)v17, 0);
        *((unsigned int *)v24) = v19;
        if (!v23)
            return v10;
        v26 = (!sub_40dd00() ? a0 >> 2 : a0);
        v3 = 0;
        v2 = v26;
        v27 = *(v23) >> 31;
        if (!v27)
        {
            if (*(v23) <= v26)
            {
                SetLastError(ERROR_INVALID_PARAMETER);
                return v10;
            }
        }
        else
        {
            if (v27 <= 0)
            {
                SetLastError(ERROR_INVALID_PARAMETER);
                return v10;
            }
        }
        v3 = &v11;
        v2 = sub_40fc49;
        v28 = _ccall(v15, v16, (unsigned int)v17, 0);
        v29 = *((int *)v28);
        v1 = *((int *)v28);
        v30 = _ccall(v15, v16, (unsigned int)v17, 0);
        *((unsigned int **)v30) = &v1;
        if (v23[2 + 2 * v26])
        {
            ch = GetCurrentProcessId();
            v0 = ch;
            v32 = sub_40dc38(v22);
            if (*((char *)(ch ^ v32)) == *((char *)v23[2 + 2 * v26]))
            {
                v33 = sub_40dc38(v22);
                v10 = v33 ^ v23[2 + 2 * v26];
            }
        }
        v34 = _ccall(v15, v16, (unsigned int)v17, 0);
        *((unsigned int *)v34) = v29;
        return v10;
    }
    else
    {
        ch1 = GetCurrentProcess();
        if (!DuplicateHandle(GetCurrentProcess(), a0, ch1, &v9, 0x400, 0, 0))
        {
            ch2 = GetCurrentProcess();
            if (!DuplicateHandle(GetCurrentProcess(), a0, ch2, &v9, 0x1000, 0, 0))
                v9 = a0;
        }
        sub_4054b4();
        if (!g_41ed94)
            g_41ed94 = sub_40da7c();
        if (g_41ed94)
        {
            v37 = (enum WIN32_ERROR)g_41ed94(v9, 0, &v7, 24, 0);
            if (!v37)
                v10 = v8;
            else
                SetLastError(v37);
        }
        else
        {
            SetLastError(ERROR_CALL_NOT_IMPLEMENTED);
        }
        if (v9 == a0)
            return v10;
        CloseHandle(v9);
        return v10;
    }
}
```

## `sub_0040fbc2` `0x0040fbc2`

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

unsigned int sub_40fbc2(int a0)
{
    struct_1 *v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x8]

    return sub_4030c0(v0, a0, v1);
}
```

## `sub_0040fbc7` `0x0040fbc7`

_7 bytes. (leaf/helper — see body)_

```c
void sub_40fbc7(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int *a10)
{
    unsigned int v0;  // [bp+0x0]

    sub_4034ec(v0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10);
}
```

## `sub_0040fc49` `0x0040fc49`

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

unsigned int sub_40fc49(int a0)
{
    struct_1 *v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x8]

    return sub_4030c0(v0, a0, v1);
}
```

## `sub_0040fc4e` `0x0040fc4e`

_10 bytes. (leaf/helper — see body)_

```c
void sub_40fc4e(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int *a10)
{
    unsigned int v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x100000]

    v1 = 0;
    sub_4034ec(v0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10);
}
```

## `sub_0040fc58` `0x0040fc58`

_5 bytes. (leaf/helper — see body)_

```c
void sub_40fc58(void)
{
}
```

## `sub_0040fd39` `0x0040fd39`

_395 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_4208d0;

int sub_40fd39(void)
{
    unsigned long v3;  // ldt
    unsigned long v4;  // gdt
    unsigned short v5;  // fs
    unsigned long v6;  // 4160
    unsigned int v7;  // 4106
    unsigned long v8;  // 4164
    unsigned int v9;  // 4118
    unsigned int v10;  // 4167
    unsigned long v11;  // 4118
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0x8]

    v6 = _ccall(v3, v4, (unsigned int)v5, 0);
    v7 = *((int *)v6);
    v0 = *((int *)v6);
    v8 = _ccall(v3, v4, (unsigned int)v5, 0);
    *((unsigned int **)v8) = &v0;
    v9 = g_4208d0;
    g_4208d0 = g_4208d0 + 1;
    v10 = _ccall(4, 18, v9 + 1, 0, 0);
    if ((char)v10)
    {
        sub_403a10(v7, sub_40fec5, &/* unsupported instruction */, /* unsupported instruction */);
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
    }
    v11 = _ccall(v3, v4, (unsigned int)v5, 0);
    *((unsigned int *)v11) = v7;
    v1 = sub_40fecc;
    return sub_40fec4(/* unsupported instruction */);
}
```

## `sub_0040fec4` `0x0040fec4`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40fec4(void)
{
    return;
}
```

## `sub_0040fec5` `0x0040fec5`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40fec5(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0040feca` `0x0040feca`

_2 bytes. (leaf/helper — see body)_

```c
void sub_40feca(void)
{
    sub_40fec4();
    return;
}
```

## `sub_0040fecc` `0x0040fecc`

_2 bytes. (leaf/helper — see body)_

```c
void sub_40fecc(unsigned int a0)
{
    return;
}
```

## `sub_0040fece` `0x0040fece`

_10 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_4208d0;

int sub_40fece(void)
{
    unsigned int v1;  // eax

    g_4208d0 = g_4208d0 - 1;
    return v1;
}
```

## `sub_00410963` `0x00410963`

_2 bytes. (leaf/helper — see body)_

```c
int sub_410963(void)
{
    unsigned int *v1;  // eax

    goto *(v1);
}
```

## `sub_00410a47` `0x00410a47`

_2 bytes. (leaf/helper — see body)_

```c
void sub_410a47(unsigned int *a0)
{
    goto *(a0);
}
```

## `sub_00410b6b` `0x00410b6b`

_25 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

char sub_410b6b(unsigned int a0, char a1)
{
    struct_0 **v2;  // ebx
    char *v3;  // eax
    char v4;  // dl
    char *v5;  // edi
    char *v6;  // esi
    unsigned short v7;  // es
    unsigned int *v8;  // ecx
    int v0;  // [bp-0x4]

    v3 = (*(v2))();
    *(v3) = *(v3) + *((char *)&v3);
    *(v3) = *(v3) + v4;
    *(v5) = *(v5) ^ *((char *)((void*)&v3 + 1));
    *(v6) = *(v6) ^ *((char *)((void*)&v3 + 1));
    *((unsigned short *)&v0) = v7;
    *(v8) = *(v8) & v6;
    *(v6) = *(v6) & *((char *)((void*)&v3 + 1));
    return sub_410b84(v0);
}
```

## `sub_00410b84` `0x00410b84`

_3 bytes. (leaf/helper — see body)_

```c
int sub_410b84(void)
{
    return /* unsupported instruction */;
}
```

## `sub_00410b87` `0x00410b87`

_1 bytes. (leaf/helper — see body)_

```c
void sub_410b87(void)
{
    sub_410b88();
    return;
}
```

## `sub_00410b88` `0x00410b88`

_8 bytes. (leaf/helper — see body)_

```c
int sub_410b88(void)
{
    unsigned long v1;  // ldt
    unsigned long v2;  // gdt
    unsigned short v3;  // fs
    unsigned long v4;  // 4105

    v4 = _ccall(v1, v2, (unsigned int)v3, 4);
    return *((int *)v4);
}
```

## `sub_00410b90` `0x00410b90`

_161 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    char padding_4[4];
    unsigned int field_8;
    unsigned int field_c;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
    struct struct_1 *field_4;
    unsigned int field_8;
    unsigned int field_c;
} struct_1;

int sub_410b90(void)
{
    struct_0 *i;  // ebx
    struct_0 *v4;  // esi
    struct_0 *v5;  // eax
    unsigned int v6;  // eax
    struct_1 *idx;  // edx
    char v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]

    i = sub_410b84();
    v4 = sub_410b88();
    v1 = 0;
    if (v4 > i + 1 && !IsBadReadPtr(i, v4 - i))
    {
        for (v0 = 1; v4 > i + 1; i = i->padding_4)
        {
            v5 = i;
            if (v5->field_0 == 0x77777777 && i == v5->padding_4 && v6 == v5->field_8 && v5->field_c == (v6 ^ i))
            {
                if (v4 == i)
                    break;
                v1 += 1;
                if (v1 == 7)
                {
                    v0 = 0;
                    break;
                }
            }
        }
    }
    if (v0)
    {
        idx->field_0 = 0x77777777;
        idx->field_4 = idx;
        idx->field_8 = v6;
        idx->field_c = idx->field_4 ^ v6;
    }
    return;
}
```

## `sub_00410c31` `0x00410c31`

_3 bytes. (leaf/helper — see body)_

```c
int sub_410c31(void)
{
    return sub_410c34();
}
```

## `sub_00410c34` `0x00410c34`

_127 bytes. (leaf/helper — see body)_

```c
int sub_410c34(unsigned int a0, unsigned int a1)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4146
    unsigned int v9;  // 4115
    unsigned long v10;  // 4155
    enum WIN32_ERROR v11;  // eax
    int v12;  // ebx
    unsigned long v14;  // 4118
    unsigned int v0;  // [bp-0x2c]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]
    char v4;  // [bp-0x4]

    v3 = 0;
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v9 = *((int *)v8);
    v0 = *((int *)v8);
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v10) = &v0;
    v11 = GetLastError();
    if ((char)sub_410b90(v9, sub_410cc4, &v4, v12, 0))
    {
        sub_403be8();
        sub_409ee0();
        sub_403e78(sub_403c80());
        sub_402628();
        v2 = 0;
    }
    SetLastError(v11);
    v14 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v14) = v9;
    v1 = sub_410ccb;
    return sub_410cb3();
}
```

## `sub_00410cb3` `0x00410cb3`

_17 bytes. (leaf/helper — see body)_

```c
int sub_410cb3(void)
{
    sub_403a10();
    return sub_403a10();
}
```

## `sub_00410cc4` `0x00410cc4`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_410cc4(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00410cc9` `0x00410cc9`

_2 bytes. (leaf/helper — see body)_

```c
int sub_410cc9(void)
{
    return sub_410cb3();
}
```

## `sub_00410ccb` `0x00410ccb`

_7 bytes. (leaf/helper — see body)_

```c
void sub_410ccb(void)
{
    return;
}
```

## `sub_00410cd2` `0x00410cd2`

_2 bytes. (leaf/helper — see body)_

```c
int sub_410cd2(void)
{
    sub_410cd4();
    return;
}
```

## `sub_00410cd4` `0x00410cd4`

_69 bytes. (leaf/helper — see body)_

```c
int sub_410cd4(void)
{
    PWSTR v5;  // eax
    unsigned int *v6;  // ecx
    char v7;  // dl
    int v0;  // [bp-0xc]
    int v1;  // [bp-0x8]
    int v2;  // [bp-0x4]
    int v3;  // [bp+0x0]

    lstrlenW(v5);
    sub_403f60(v0, v1, v2, v3);
    if (*(v6))
    {
        sub_403c80();
        sub_402628();
    }
    if (v7)
        sub_403c88();
    return;
}
```

## `sub_00410d28` `0x00410d28`

_451 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_41efc0;
extern unsigned int g_41efc4;
extern unsigned int g_41efc8;
extern unsigned int g_41efcc;
extern unsigned int g_41efd0;
extern unsigned int g_41efd4;
extern unsigned int g_41efd8;
extern unsigned int g_41efdc;
extern unsigned int g_41efe0;
extern unsigned int g_41efe4;
extern unsigned int g_41efe8;
extern unsigned int g_41efec;
extern unsigned int g_41eff0;
extern unsigned int g_41eff4;
extern unsigned int g_41eff8;
extern unsigned int g_41effc;
extern unsigned int g_41f000;
extern unsigned int g_41f004;
extern unsigned int g_41f008;
extern unsigned int g_41f00c;
extern unsigned int g_41f010;
extern unsigned int g_41f014;
extern unsigned int g_41f018;
extern unsigned int g_41f01c;
extern unsigned int g_41f020;

int sub_410d28(void)
{
    unsigned int v1;  // eax

    if (g_41efd0)
        return v1;
    g_41efd0 = sub_40d994();
    g_41efd4 = sub_40d994();
    g_41efc0 = sub_40d994();
    g_41efc4 = sub_40d994();
    g_41efc8 = sub_40d994();
    g_41efcc = sub_40d994();
    g_41efd8 = sub_40d994();
    g_41efdc = sub_40d994();
    g_41efe0 = sub_40d994();
    g_41efe4 = sub_40d994();
    g_41efe8 = sub_40d994();
    g_41efec = sub_40d994();
    g_41eff0 = sub_40d994();
    g_41eff4 = sub_40d994();
    g_41eff8 = sub_40d994();
    g_41effc = sub_40d994();
    g_41f000 = sub_40d994();
    g_41f004 = sub_40d994();
    g_41f008 = sub_40d994();
    g_41f00c = sub_40d994();
    g_41f010 = sub_40d994();
    g_41f014 = sub_40d994();
    g_41f018 = sub_40d994();
    g_41f01c = sub_40d994();
    g_41f020 = sub_40d994();
    return g_41f020;
}
```

## `sub_00410eeb` `0x00410eeb`

_1 bytes. (leaf/helper — see body)_

```c
void sub_410eeb(void)
{
    sub_410eec();
    return;
}
```

## `sub_00410eec` `0x00410eec`

_50 bytes. (leaf/helper — see body)_

```c
unsigned int sub_410eec(unsigned int a0, unsigned int a1)
{
    unsigned int v2;  // cc_op
    unsigned int v3;  // cc_dep1
    unsigned int v4;  // cc_dep2
    unsigned int v5;  // cc_ndep
    unsigned int v6;  // 4186
    unsigned int v7;  // id
    unsigned int v8;  // ac
    unsigned int v9;  // 4108
    unsigned int v10;  // eax
    unsigned int v11;  // ebx
    unsigned int v0;  // [bp-0x4]

    v6 = _ccall(v2, v3, v4, v5);
    v0 = v6 | 0x202 | v7 * 0x200000 & 0x200000 | v8 * 0x40000 & 0x40000;
    v0 ^= 0x200000;
    v9 = v0;
    v0 = v9 & 2261 | 0x202 | ((char)(v9 >> 10) ? 4294967295 : 1) & 0x400 | ((char)(v9 >> 21) ? 1 : 0) * 0x200000 & 0x200000 | ((char)(v9 >> 18) ? 1 : 0) * 0x40000 & 0x40000;
    v10 = 0;
    if (v0 != v0)
    {
        v0 = v11;
        x86g_dirtyhelper_CPUID_sse3(unsupported_<class 'pyvex.expr.GSPTR'>())
        /* unsupported instruction */
        v10 = 0;
        if (((unsigned short)a1 & 0x100))
            v10 = 1;
    }
    return v10;
}
```

## `sub_00410f1e` `0x00410f1e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_410f1e(unsigned int a0, unsigned int a1)
{
    return sub_410f20();
}
```

## `sub_00410f20` `0x00410f20`

_66 bytes. (leaf/helper — see body)_

```c
int sub_410f20(char *a0, unsigned int *a1, unsigned int a2)
{
    unsigned int v3;  // cc_op
    char *v4;  // cc_dep1
    unsigned int v15;  // 4141
    unsigned int v5;  // cc_dep2
    unsigned int v6;  // edx
    unsigned int v7;  // eax
    unsigned int v8;  // edx
    unsigned int v9;  // eax
    char *iter;  // edi
    char *i;  // esi
    unsigned int v12;  // ecx
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp-0x4]
    char v2;  // [bp+0x0]

    v3 = 3;
    v4 = &v2;
    v5 = 0xfffffff8;
    v6 = a1[1];
    v7 = *(a1);
    do
    {
        v8 = v6;
        v9 = v7;
        v0 = v9;
        v1 = v8;
        iter = &v0;
        i = a0;
        for (v12 = a2; v12; i += 1)
        {
            v12 -= 1;
            *(iter) = *(i);
            iter += 1;
        }
        vvar_88 .. vvar_87 = CAS(vvar_1, vvar_86{s-4|4b} .. vvar_85{s-8|4b}, vvar_26{r16|4b} .. vvar_25{r8|4b})
        v15 = _ccall(v3, v4, v5, 0);
        v3 = 0;
        v4 = v15 & 4294967231 | CasCmpEQ(/* unsupported instruction */ ^ v8 | /* unsupported instruction */ ^ v9, 0) * 64;
        v5 = 0;
        v7 = (CasCmpEQ(/* unsupported instruction */ ^ v8 | /* unsupported instruction */ ^ v9, 0) ? v9 : /* unsupported instruction */);
        v6 = (CasCmpEQ(/* unsupported instruction */ ^ v8 | /* unsupported instruction */ ^ v9, 0) ? v8 : /* unsupported instruction */);
    } while (((char)((v15 & 4294967231 | CasCmpEQ(/* unsupported instruction */ ^ v8 | /* unsupported instruction */ ^ v9, 0) * 64) >> 6) & 1) != 1);
    return (CasCmpEQ(/* unsupported instruction */ ^ v8 | /* unsupported instruction */ ^ v9, 0) ? v9 : /* unsupported instruction */);
}
```

## `sub_00410f62` `0x00410f62`

_1 bytes. (leaf/helper — see body)_

```c
void sub_410f62(void)
{
    return;
}
```

## `sub_00410f63` `0x00410f63`

_1 bytes. (leaf/helper — see body)_

```c
int sub_410f63(void)
{
    sub_410f64();
    return;
}
```

## `sub_00410f64` `0x00410f64`

_55 bytes. (leaf/helper — see body)_

```c
int sub_410f64(void)
{
    unsigned int v1;  // ecx
    unsigned int v2;  // edx
    char v3;  // bl
    char *v4;  // eax

    if (v1 <= 0 || v1 > 8 || !(char)sub_410eec(v1, v2))
        v3 = 0;
    else
        v3 = 1;
    if (v3)
        sub_410f20(v4, v2, v1);
    return;
}
```

## `sub_00410f9b` `0x00410f9b`

_1 bytes. (leaf/helper — see body)_

```c
int sub_410f9b(void)
{
    sub_410f9c();
    return;
}
```

## `sub_00410f9c` `0x00410f9c`

_128 bytes. (leaf/helper — see body)_

```c
int sub_410f9c(void)
{
    HANDLE v4;  // eax
    HGLOBAL *v5;  // edx
    HANDLE v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0x10]

    if (!OpenProcessToken(v4, TOKEN_QUERY, &v0))
        return;
    v1 = 0;
    GetTokenInformation(v0, TokenUser, NULL, 0, &v2);
    *(v5) = sub_40536c(0x40, v2 * 2);
    if (!GetTokenInformation(v0, TokenUser, *(v5), v2 * 2, &v2))
        LocalFree(*(v5));
    CloseHandle(v0);
    return;
}
```

## `sub_0041101c` `0x0041101c`

_476 bytes. (leaf/helper — see body)_

```c
typedef struct ACL {
    Byte AclRevision;
    Byte Sbz1;
    unsigned short AclSize;
    unsigned short AceCount;
    unsigned short Sbz2;
} ACL;

typedef struct struct_0 {
    unsigned int field_0;
    PSECURITY_DESCRIPTOR field_4;
    unsigned int field_8;
} struct_0;

extern char g_41ed9c;
extern Byte g_41f02c[6];
extern Byte g_41f034[6];

int sub_41101c(void)
{
    unsigned int v25;  // ebx
    unsigned int v26;  // esi
    char v35;  // cl
    unsigned int v36;  // eax
    unsigned int *v37;  // edi
    char i[4];  // esi
    char iter[4];  // edi
    unsigned int v40;  // ecx
    char j[4];  // esi
    char node[4];  // edi
    unsigned int v43;  // ecx
    struct_0 *idx;  // eax
    unsigned int v27;  // edi
    unsigned long v45;  // 4118
    PSECURITY_DESCRIPTOR v28;  // edx
    PSECURITY_DESCRIPTOR v29;  // esi
    unsigned long v30;  // ldt
    unsigned long v31;  // gdt
    unsigned short v32;  // fs
    unsigned long v33;  // 4209
    unsigned long v34;  // 4213
    unsigned int v0;  // [bp-0xa4]
    unsigned int *v1;  // [bp-0x9c], Other Possible Types: unsigned int
    PSECURITY_DESCRIPTOR v2;  // [bp-0x98]
    unsigned int v3;  // [bp-0x94]
    unsigned int v4;  // [bp-0x90]
    char *v5;  // [bp-0x8c]
    unsigned int v6;  // [bp-0x88]
    unsigned int v7;  // [bp-0x84]
    unsigned int v8;  // [bp-0x80]
    unsigned int v9;  // [bp-0x7c]
    unsigned int v10;  // [bp-0x78]
    unsigned int v11;  // [bp-0x74], Other Possible Types: unsigned long
    unsigned int v12;  // [bp-0x60]
    unsigned int v13;  // [bp-0x5c]
    PSID v14;  // [bp-0x58]
    char v15;  // [bp-0x54], Other Possible Types: unsigned int
    PSID v16;  // [bp-0x38]
    char v17;  // [bp-0x34], Other Possible Types: unsigned int
    unsigned int v18;  // [bp-0x18]
    unsigned int *v19;  // [bp-0x14]
    ACL *v20;  // [bp-0x10]
    PSID v21;  // [bp-0xc]
    PSID v22;  // [bp-0x8]
    char v23;  // [bp-0x4]

    v8 = v25;
    v7 = v26;
    v6 = v27;
    v10 = 0;
    v9 = 0;
    v29 = v28;
    v5 = &v23;
    v4 = sub_411206;
    v33 = _ccall(v30, v31, (unsigned int)v32, 0);
    v3 = *((int *)v33);
    v34 = _ccall(v30, v31, (unsigned int)v32, 0);
    *((unsigned int **)v34) = &v3;
    v22 = NULL;
    v21 = NULL;
    v19 = NULL;
    v20 = NULL;
    if (v35)
    {
        v22 = v22;
        v21 = v21;
        if (g_41ed9c)
        {
            sub_409eac();
            v36 = sub_403e78();
            sub_409eac(v36);
            v37 = GetProcAddress(sub_4052c4(sub_403e78(v36)), v36);
            if (v37)
            {
                v0 = 0;
                v22 = v22;
                v21 = v21;
                if (AllocateAndInitializeSid(&g_41f02c[0], 1, 0, 0, 0, 0, 0, 0, 0, 0, &v22))
                {
                    v0 = 0;
                    v22 = v22;
                    v21 = v21;
                    if (AllocateAndInitializeSid(&g_41f034[0], 1, 18, 0, 0, 0, 0, 0, 0, 0, &v21))
                    {
                        GetCurrentProcess();
                        v22 = v22;
                        v21 = v21;
                        if ((char)sub_410f9c())
                        {
                            v22 = v22;
                            v21 = v21;
                            if (v19)
                            {
                                sub_4054b4();
                                (&v11)[1] = 1;
                                v12 = 0;
                                v13 = 1;
                                v2 = v29;
                                v1 = v37;
                                i = &v11;
                                iter = &v15;
                                for (v40 = 8; v40; i += 1)
                                {
                                    v40 -= 1;
                                    *(iter) = *(i);
                                    iter += 1;
                                }
                                v2 = v29;
                                v1 = v37;
                                j = &v15;
                                node = &v17;
                                for (v43 = 8; v43; j += 1)
                                {
                                    v43 -= 1;
                                    *(node) = *(j);
                                    node += 1;
                                }
                                v11 = 4;
                                v15 = 0x1fffff;
                                v17 = 0x1fffff;
                                v14 = v22;
                                v16 = v21;
                                v18 = *(v19);
                                v0 = 3;
                                v22 = v22;
                                v21 = v21;
                                if (v37(3, &v11, 0, &v20))
                                    v20 = NULL;
                            }
                        }
                    }
                }
            }
        }
    }
    idx->field_0 = 12;
    idx->field_4 = v29;
    idx->field_8 = 0;
    InitializeSecurityDescriptor(v29, 1);
    SetSecurityDescriptorDacl(v29, -1, v20, 0);
    if (v22)
        FreeSid(v22);
    if (v21)
        FreeSid(v21);
    if (v19)
        LocalFree(v19);
    v45 = _ccall(v30, v31, (unsigned int)v32, 0);
    *((unsigned int *)v45) = v0;
    v1 = sub_41120d;
    sub_4111f8();
    return;
}
```

## `sub_004111f8` `0x004111f8`

_14 bytes. (leaf/helper — see body)_

```c
int sub_4111f8(void)
{
    return sub_403a34();
}
```

## `sub_00411206` `0x00411206`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_411206(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041120b` `0x0041120b`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41120b(void)
{
    return sub_4111f8();
}
```

## `sub_0041120d` `0x0041120d`

_7 bytes. (leaf/helper — see body)_

```c
void sub_41120d(unsigned int a0, unsigned int a1)
{
    return;
}
```

## `sub_00411214` `0x00411214`

_204 bytes. (leaf/helper — see body)_

```c
typedef struct SECURITY_ATTRIBUTES {
    unsigned int nLength;
    void* lpSecurityDescriptor;
    int bInheritHandle;
} SECURITY_ATTRIBUTES;

int sub_411214(PSTR a0)
{
    unsigned int v12;  // ebx
    unsigned int v13;  // esi
    unsigned long v14;  // ldt
    unsigned long v15;  // gdt
    unsigned short v16;  // fs
    unsigned long v17;  // 4166
    unsigned long v18;  // 4175
    unsigned long v19;  // 4118
    unsigned int v0;  // [bp-0x4c]
    unsigned int v1;  // [bp-0x48]
    char *v2;  // [bp-0x44], Other Possible Types: unsigned int
    unsigned int v3;  // [bp-0x40]
    unsigned int v4;  // [bp-0x3c]
    unsigned int v5;  // [bp-0x38]
    PWSTR v6;  // [bp-0x34]
    unsigned int v7;  // [bp-0x30]
    unsigned int v8;  // [bp-0x2c]
    PWSTR v9;  // [bp-0x28]
    SECURITY_ATTRIBUTES v10;  // [bp-0x10]
    char v11;  // [bp-0x4]

    v4 = v12;
    v3 = v13;
    v6 = NULL;
    v5 = 0;
    v9 = NULL;
    v8 = 0;
    v7 = 0;
    v2 = &v11;
    v1 = sub_4112ee;
    v17 = _ccall(v14, v15, (unsigned int)v16, 0);
    v0 = *((int *)v17);
    v18 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int **)v18) = &v0;
    if (!(GetVersion() & 0x80000000))
    {
        sub_41101c();
        sub_409eac();
        sub_403be8(&v8);
        sub_403c88();
        sub_409ee0();
        if (!sub_4051d4(&v10, 0, v9))
        {
            sub_403be8();
            sub_409ee0();
            sub_4051d4(&v10, 0, v6);
        }
    }
    else
    {
        sub_4051ac(NULL, 0, a0);
    }
    v19 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int *)v19) = v0;
    v2 = sub_4112f5;
    return sub_4112e0();
}
```

## `sub_004112e0` `0x004112e0`

_14 bytes. (leaf/helper — see body)_

```c
int sub_4112e0(void)
{
    return sub_403a34();
}
```

## `sub_004112ee` `0x004112ee`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4112ee(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004112f3` `0x004112f3`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4112f3(void)
{
    return sub_4112e0();
}
```

## `sub_004112f5` `0x004112f5`

_10 bytes. (leaf/helper — see body)_

```c
int sub_4112f5(unsigned int a0)
{
    unsigned int v0;  // ebx

    return v0;
}
```

## `sub_004112ff` `0x004112ff`

_1 bytes. (leaf/helper — see body)_

```c
void sub_4112ff(unsigned int a0)
{
    sub_411300();
    return;
}
```

## `sub_00411300` `0x00411300`

_183 bytes. (leaf/helper — see body)_

```c
int sub_411300(PSTR a0)
{
    unsigned int v11;  // ebx
    unsigned int v12;  // esi
    unsigned long v13;  // ldt
    unsigned long v14;  // gdt
    unsigned short v15;  // fs
    unsigned long v16;  // 4163
    unsigned long v17;  // 4172
    unsigned long v18;  // 4118
    unsigned int v0;  // [bp-0x2c]
    unsigned int v1;  // [bp-0x28]
    char *v2;  // [bp-0x24], Other Possible Types: unsigned int
    unsigned int v3;  // [bp-0x20]
    unsigned int v4;  // [bp-0x1c]
    unsigned int v5;  // [bp-0x18]
    PWSTR v6;  // [bp-0x14]
    unsigned int v7;  // [bp-0x10]
    unsigned int v8;  // [bp-0xc]
    PWSTR v9;  // [bp-0x8]
    char v10;  // [bp-0x4]

    v9 = NULL;
    v8 = 0;
    v7 = 0;
    v6 = NULL;
    v5 = 0;
    v4 = v11;
    v3 = v12;
    v2 = &v10;
    v1 = sub_4113c5;
    v16 = _ccall(v13, v14, (unsigned int)v15, 0);
    v0 = *((int *)v16);
    v17 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int **)v17) = &v0;
    if (!(GetVersion() & 0x80000000))
    {
        sub_409eac();
        sub_403be8(&v8);
        sub_403c88();
        sub_409ee0();
        if (!OpenMutexW(SYNCHRONIZATION_SYNCHRONIZE, 0, v9))
        {
            sub_403be8();
            sub_409ee0();
            OpenMutexW(SYNCHRONIZATION_SYNCHRONIZE, 0, v6);
        }
    }
    else
    {
        OpenMutexA(0x100000, 0, a0);
    }
    v18 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int *)v18) = v0;
    v2 = sub_4113cc;
    return sub_4113b7();
}
```

## `sub_004113b7` `0x004113b7`

_14 bytes. (leaf/helper — see body)_

```c
int sub_4113b7(void)
{
    return sub_403a34();
}
```

## `sub_004113c5` `0x004113c5`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4113c5(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004113ca` `0x004113ca`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4113ca(void)
{
    return sub_4113b7();
}
```

## `sub_004113cc` `0x004113cc`

_10 bytes. (leaf/helper — see body)_

```c
int sub_4113cc(unsigned int a0)
{
    unsigned int v0;  // ebx

    return v0;
}
```

