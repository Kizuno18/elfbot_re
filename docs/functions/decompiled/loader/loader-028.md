# elfbot.dll decompiled — loader 0x0041a329..0x0041c621

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_0041a329` `0x0041a329`

_10 bytes. (leaf/helper — see body)_

```c
int sub_41a329(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // [bp+0xffffc]

    return v0;
}
```

## `sub_0041a333` `0x0041a333`

_1 bytes. (leaf/helper — see body)_

```c
int sub_41a333(void)
{
    sub_41a334();
    return;
}
```

## `sub_0041a334` `0x0041a334`

_195 bytes. calls WriteProcessMemory_

```c
int sub_41a334(void)
{
    unsigned int v6;  // esi
    unsigned int v7;  // eax
    unsigned int v8;  // edi
    Byte v0[271];  // [bp-0x33d]
    WCHAR v1[271];  // [bp-0x22e]
    void* v2;  // [bp-0x10], Other Possible Types: enum WIN32_ERROR
    int v3;  // [bp-0xc], Other Possible Types: unsigned int
    PWSTR v4;  // [bp+0x4]
    PSTR v5;  // [bp+0x8]

    v3 = 0;
    if (v4)
        lstrcpyW(v1, v4);
    if (v5)
        lstrcpyA(v0, v5);
    v6 = sub_41a158();
    if (!v6)
        return;
    v8 = sub_40e970(814, v7);
    if (!v8)
    {
        return;
    }
    else if (WriteProcessMemory(v7, v8, &/* unsupported instruction */, 0x32e, &v2))
    {
        v3 = sub_40f474(v7, NULL, 0, v6, v8, 0, &v2);
        if (v3)
            return;
        v2 = GetLastError();
        sub_40ea58(v8, v7);
        SetLastError(v2);
        return;
    }
    else
    {
        return;
    }
}
```

## `sub_0041a3f7` `0x0041a3f7`

_1 bytes. (leaf/helper — see body)_

```c
int sub_41a3f7(void)
{
    sub_41a3f8();
    return;
}
```

## `sub_0041a3f8` `0x0041a3f8`

_115 bytes. (leaf/helper — see body)_

```c
int sub_41a3f8(void)
{
    int v4;  // edx
    int v5;  // ecx
    int v7;  // ebx
    HANDLE v8;  // eax
    enum WIN32_ERROR v9;  // eax, Other Possible Types: unsigned int
    int v0;  // [bp-0xc]
    int v1;  // [bp-0x8]
    int v2;  // [bp-0x4]

    v7 = (v4 == -1 ? 0 : sub_40afb4(v5, v0, v1, v2));
    if (v7 >= v4)
    {
        v9 = (enum WIN32_ERROR)(!v4 ? 0 : ERROR_TIMEOUT);
    }
    else if (!WaitForSingleObject(v8, v4 - v7))
    {
        GetExitCodeThread(v8, &v9);
    }
    else
    {
        v9 = GetLastError();
        v9 = v9;
    }
    CloseHandle(v8);
    if (v9)
        SetLastError(v9);
    return;
}
```

## `sub_0041a46b` `0x0041a46b`

_1 bytes. (leaf/helper — see body)_

```c
int sub_41a46b(void)
{
    sub_41a46c();
    return;
}
```

## `sub_0041a46c` `0x0041a46c`

_112 bytes. (leaf/helper — see body)_

```c
int sub_41a46c(void)
{
    int v6;  // ebx
    int v7;  // eax
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4126
    unsigned int v12;  // 4103
    unsigned long v13;  // 4135
    unsigned long v14;  // 4118
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v2 = 0;
    sub_403e68(v6, 0, 0, v7, &v4);
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v12 = *((int *)v11);
    v0 = *((int *)v11);
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v13) = &v0;
    sub_409eac(v12, sub_41a4ea, &v3);
    v14 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v14) = v12;
    v1 = sub_41a4f1;
    sub_41a4dc();
    return;
}
```

## `sub_0041a4dc` `0x0041a4dc`

_14 bytes. (leaf/helper — see body)_

```c
int sub_41a4dc(void)
{
    return sub_403a34();
}
```

## `sub_0041a4ea` `0x0041a4ea`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_41a4ea(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041a4ef` `0x0041a4ef`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41a4ef(void)
{
    return sub_41a4dc();
}
```

## `sub_0041a4f1` `0x0041a4f1`

_7 bytes. (leaf/helper — see body)_

```c
int sub_41a4f1(void)
{
    unsigned int v1;  // ebx

    return v1;
}
```

## `sub_0041a4f8` `0x0041a4f8`

_43 bytes. calls ReadProcessMemory_

```c
int sub_41a4f8(void)
{
    HANDLE v2;  // eax
    void* v3;  // edx
    void* count;  // ecx
    UIntPtr v0;  // [bp-0x8]
    UIntPtr v1;  // [bp+0x4]

    ReadProcessMemory(v2, v3, count, v1, &v0);
    return;
}
```

## `sub_0041a523` `0x0041a523`

_1 bytes. (leaf/helper — see body)_

```c
int sub_41a523(void)
{
    sub_41a524();
    return;
}
```

## `sub_0041a524` `0x0041a524`

_43 bytes. calls ReadProcessMemory_

```c
int sub_41a524(void)
{
    HANDLE v2;  // eax
    void* v3;  // edx
    void* count;  // ecx
    UIntPtr v0;  // [bp-0x8]
    UIntPtr v1;  // [bp+0x4]

    ReadProcessMemory(v2, v3, count, v1, &v0);
    return;
}
```

## `sub_0041a54f` `0x0041a54f`

_1 bytes. (leaf/helper — see body)_

```c
int sub_41a54f(void)
{
    sub_41a550();
    return;
}
```

## `sub_0041a550` `0x0041a550`

_78 bytes. calls WriteProcessMemory_

```c
int sub_41a550(void)
{
    HANDLE v3;  // eax
    void* v4;  // edx
    void* v5;  // ecx
    unsigned int v0;  // [bp-0xc]
    char v1;  // [bp+0x4]
    UIntPtr v2;  // [bp+0x8]

    if ((!v1 || VirtualProtectEx(v3, v4, v2, PAGE_EXECUTE_READWRITE, &v0)) && WriteProcessMemory(v3, v4, v5, v2, &v0))
        return;
    return;
}
```

## `sub_0041a59e` `0x0041a59e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41a59e(void)
{
    sub_41a5a0();
    return;
}
```

## `sub_0041a5a0` `0x0041a5a0`

_339 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[44];
    unsigned int field_2c;
    char padding_30[32];
    struct struct_2 *field_50;
} struct_1;

typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
} struct_0;

typedef struct struct_2 {
    struct struct_0 *field_0;
} struct_2;

int sub_41a5a0(void)
{
    unsigned int v11;  // ebx
    unsigned int v12;  // esi
    unsigned int v21;  // edx
    unsigned int *v22;  // ebx
    unsigned int v23;  // edi
    unsigned int v24;  // esi
    unsigned int v25;  // edi
    unsigned int v26;  // eax
    unsigned int v27;  // edi
    struct_1 *v28;  // ebx
    struct_0 **v29;  // ebx
    struct_0 *v30;  // eax
    unsigned int v13;  // edi
    struct_0 *v31;  // ebx
    unsigned long v32;  // 4116
    char v33;  // al
    int v14;  // ecx
    unsigned int v15;  // eax
    unsigned long v16;  // ldt
    unsigned long v17;  // gdt
    unsigned short v18;  // fs
    unsigned long v19;  // 4168
    unsigned long v20;  // 4172
    unsigned int v0;  // [bp-0x2c]
    unsigned int v1;  // [bp-0x28]
    char *v2;  // [bp-0x24]
    unsigned int v3;  // [bp-0x20]
    unsigned int v4;  // [bp-0x1c]
    unsigned int v5;  // [bp-0x18]
    int v6;  // [bp-0x14]
    unsigned int v7;  // [bp-0x10]
    char v8;  // [bp-0x9]
    char v9;  // [bp-0x4]
    void* v10;  // [bp+0x4]

    v5 = v11;
    v4 = v12;
    v3 = v13;
    if ((GetVersion() & 0x80000000))
    {
        v8 = 0;
        v15 = sub_40dc38(v14);
        v2 = &v9;
        v1 = sub_41a6b8;
        v19 = _ccall(v16, v17, (unsigned int)v18, 0);
        v0 = *((int *)v19);
        v20 = _ccall(v16, v17, (unsigned int)v18, 0);
        *((unsigned int **)v20) = &v0;
        v22 = *((int *)((v15 ^ v21) + 0x44));
        v6 = 0;
        v23 = *(v22);
        if (*(v22) > 0)
        {
            v24 = 1;
            do
            {
                v25 = v23;
            } while ((!v22[2 * v24] || (v26 = sub_40dc38(v14), sub_40dc38(v14) == v22[2 * v24] || (*((char *)((char *)&v22[2 * v24] + 1)) & 128) || (v6 = (int)(v6 + 1), v6 <= 1))) && (v24 += 1, v27 = v25 - 1, v23 = v25 - 1, v25 != 1));
        }
        if (v6 <= 1)
        {
            v28 = sub_40dc38(v14) ^ v21;
            if (v28->field_2c == 65537 && (!sub_40dd00() || !*((int *)&v28[1].padding_30[20])) && (sub_40dd00() || !*((int *)&v28[1].padding_30[24])))
            {
                v29 = v28->field_50;
                v30 = *(v29);
                if (v30 == v29[1] && v30 == v29[2])
                {
                    v31 = v30;
                    if (!*((int *)&v31->padding_0[0]) && !*((int *)&v31->padding_0[4]) && (sub_40dd00() && *((int *)(v31->field_8 + 440)) > 0 || !sub_40dd00() && *((int *)(v31->field_8 + 528)) > 0))
                        v8 = 1;
                }
            }
        }
        v32 = _ccall(v16, v17, (unsigned int)v18, 0);
        *((unsigned int *)v32) = v0;
        return;
    }
    else
    {
        if (!(int)v10[4] || !(char)sub_41a524(4) || v7)
            v33 = 0;
        else
            v33 = 1;
        v8 = v33;
        return;
    }
}
```

## `sub_0041a6b8` `0x0041a6b8`

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

unsigned int sub_41a6b8(int a0)
{
    struct_1 *v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x8]

    return sub_4030c0(v0, a0, v1);
}
```

## `sub_0041a6bd` `0x0041a6bd`

_9 bytes. (leaf/helper — see body)_

```c
void sub_41a6bd(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int *a10)
{
    unsigned int v0;  // [bp+0x0]
    char v1;  // [bp+0xfffff]

    v1 = 1;
    sub_4034ec(v0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10);
}
```

## `sub_0041a6c6` `0x0041a6c6`

_2 bytes. (leaf/helper — see body)_

```c
void sub_41a6c6(void)
{
}
```

## `sub_0041a703` `0x0041a703`

_1 bytes. (leaf/helper — see body)_

```c
void sub_41a703(unsigned int a0)
{
    sub_41a704();
    return;
}
```

## `sub_0041a704` `0x0041a704`

_190 bytes. (leaf/helper — see body)_

```c
unsigned int sub_41a704(void* a0)
{
    unsigned int v1;  // eax
    unsigned short v0;  // [bp-0x6]

    if (!*((int *)(int)a0[4]) || !(char)sub_41a524(2) || v0 != 23117 || !(char)sub_41a524(4) || !(char)sub_41a524(248) || *((int *)(int)a0[12]) != 17744 || (*((char *)((int)a0[12] + 23)) & 32))
        v1 = 0;
    else
        v1 = _INSERT((int)a0[12], 0, 1);
    if ((char)v1)
        *((unsigned int *)(int)a0[8]) = *((int *)(int)a0[4]) + v0 + 120;
    return v1;
}
```

## `sub_0041a7c2` `0x0041a7c2`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41a7c2(void)
{
    sub_41a7c4();
    return;
}
```

## `sub_0041a7c4` `0x0041a7c4`

_160 bytes. (leaf/helper — see body)_

```c
int sub_41a7c4(void)
{
    unsigned int v7;  // ebx
    unsigned int v8;  // esi
    unsigned int v9;  // edi
    unsigned int v10;  // ecx
    void* i;  // edi
    unsigned int v12;  // esi
    HANDLE v13;  // eax
    unsigned int *v14;  // edx
    unsigned int v0;  // [bp-0x38]
    unsigned int v1;  // [bp-0x34]
    unsigned int v2;  // [bp-0x30]
    int v3;  // [bp-0x2c]
    unsigned int v4;  // [bp-0x10]
    char v5;  // [bp-0x4]

    v2 = v7;
    v1 = v8;
    v0 = v9;
    v4 = v10;
    if ((GetVersion() & 0x80000000))
    {
        i = NULL;
        for (v12 = 0; VirtualQueryEx(v13, i, &v3, 0x1c) == 0x1c; i += *((unsigned int *)(&v3 + 12)))
        {
            if (v12 != *((unsigned int *)(&v3 + 4)))
            {
                *(v14) = *((unsigned int *)(&v3 + 4));
                if (*((unsigned int *)(&v3 + 16)) == 0x1000 && (char)sub_41a704(&v5))
                    return;
                v12 = *((unsigned int *)(&v3 + 4));
            }
        }
        return;
    }
    else
    {
        if (!(char)sub_41a524(4) || !(char)sub_41a704(&v5))
            return;
        return;
        return;
    }
}
```

## `sub_0041a864` `0x0041a864`

_624 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[8];
    struct struct_0 *field_8;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    PSTR field_18;
} struct_0;

extern unsigned int g_41f028;
extern void g_41f150;
extern void g_41f3e4;

int sub_41a864(void)
{
    unsigned int v44;  // ebx
    unsigned int *v45;  // esi
    unsigned int v54;  // ecx
    void* k;  // esi
    void* iter;  // edi
    unsigned int v57;  // ecx
    unsigned int v58;  // ebx
    unsigned int v59;  // eax
    unsigned int v60;  // eax
    int v61;  // edi
    unsigned int v46;  // edi
    char iter1[4];  // edi
    unsigned int v48;  // ecx
    unsigned int v49;  // ecx
    unsigned int v50;  // edx
    HANDLE v51;  // eax
    void* j;  // esi
    void* node;  // edi
    unsigned int v0;  // [bp-0x3d4]
    unsigned int v1;  // [bp-0x3d0]
    unsigned int v2;  // [bp-0x3c8]
    HANDLE v3;  // [bp-0x3c4], Other Possible Types: unsigned int
    unsigned int v4;  // [bp-0x3c0]
    unsigned int *v5;  // [bp-0x3bc]
    unsigned int v6;  // [bp-0x3b8]
    unsigned long v7;  // [bp-0x3b2]
    unsigned int v8;  // [bp-0x3aa]
    unsigned long v9;  // [bp-0x3a6]
    unsigned int v10;  // [bp-0x39e]
    int <0x41a864[is_10]|Stack bp-0x39a, 1 B>;  // [bp-0x39a]
    unsigned long v12;  // [bp-0x39a]
    unsigned int v13;  // [bp-0x392]
    char v14;  // [bp-0x38e], Other Possible Types: unsigned long
    unsigned int v15;  // [bp-0x386]
    unsigned int v16;  // [bp-0x382]
    unsigned int v17;  // [bp-0x37e]
    unsigned int v18;  // [bp-0x379]
    unsigned int v19;  // [bp-0x373]
    unsigned int v20;  // [bp-0x36c]
    unsigned int v21;  // [bp-0x365]
    unsigned int v22;  // [bp-0x35e]
    unsigned int v23;  // [bp-0x357]
    unsigned int v24;  // [bp-0x350]
    unsigned int v25;  // [bp-0x349]
    unsigned int v26;  // [bp-0x342]
    unsigned int v27;  // [bp-0x33b]
    unsigned int v28;  // [bp-0x334]
    unsigned int v29;  // [bp-0x32d]
    unsigned int v30;  // [bp-0x326]
    unsigned int v31;  // [bp-0x31f]
    unsigned int v32;  // [bp-0x318]
    int v33;  // [bp-0x312]
    Byte v34[520];  // [bp-0x30e]
    char v35;  // [bp-0x106]
    unsigned int v36;  // [bp-0xde]
    char v37;  // [bp-0xe]
    unsigned int v38;  // [bp-0xd]
    char v39;  // [bp-0x9]
    unsigned int v40;  // [bp-0x8]
    unsigned int *i;  // [bp+0x8]
    struct_1 *v43;  // [bp+0xc]

    v6 = v44;
    v5 = v45;
    v4 = v46;
    iter1 = &v35;
    v3 = v48;
    for (v49 = 62; v49; i += 1)
    {
        v49 -= 1;
        *((unsigned int *)&iter1[0]) = *(i);
        iter1 += 1;
    }
    v40 = v50;
    sub_40e8c8();
    v3 = v51;
    v2 = v48;
    j = &g_41f150;
    node = (char *)&<0x41a864[is_10]|Stack bp-0x39a, 1 B> + 2;
    for (v54 = 164; v54; j += 4)
    {
        v54 -= 1;
        *((int *)node) = *((int *)j);
        node += 4;
    }
    *((short *)node) = *((short *)j);
    v3 = v51;
    v2 = v48;
    k = &g_41f3e4;
    iter = &v7;
    for (v57 = 6; v57; k += 4)
    {
        v57 -= 1;
        *((int *)iter) = *((int *)k);
        iter += 4;
    }
    *((short *)iter) = *((short *)k);
    v33 = sub_40d994();
    *((int *)((char *)&v7 + 1)) = sub_40d994();
    *((unsigned int *)((char *)&v9 + 1)) = g_41f028;
    v10 = v36 + v48;
    if (!(char)sub_41a4f8(5))
        return;
    v58 = sub_40e970(658, v51);
    v39 = 1;
    v8 = v58;
    lstrcpyA(v34, v43->field_8->field_18);
    v59 = v10;
    v12 = _INSERT(<0x41a864[is_10]|Stack bp-0x39a, 1 B>, 4, v59);
    v14 = _INSERT(v14 CONCAT 0, 6, v14);
    *((char *)&v14) = 198;
    *((unsigned int *)((char *)&v14 + 2)) = v59 + 4;
    v15 = v58 + 138;
    v18 = v58 + 134;
    v19 = v7;
    v20 = *((unsigned int *)((void*)&v7 + 4));
    v21 = v8;
    v22 = v9;
    v23 = *((unsigned int *)((void*)&v9 + 4));
    v24 = v10;
    v25 = v12;
    v26 = *((unsigned int *)((void*)&v12 + 4));
    v27 = v13;
    v28 = v14;
    v29 = *((unsigned int *)((void*)&v14 + 4));
    v30 = v15;
    v31 = v16;
    v32 = v17;
    if ((char)sub_41a550(0, 658))
    {
        v37 = 233;
        v1 = 0;
        v0 = v58;
        v60 = v10;
        v0 = v58 - v60;
        v1 = -(v58 < v60);
        v38 = v58 - v60 - 5;
        if (!(char)sub_41a5a0(v43->field_8))
        {
            v61 = 1;
        }
        else if ((char)sub_41a550(1, 5))
        {
            v61 = (!(char)sub_41a5a0(v43->field_8) ? 1 : 2);
            v39 = 0;
        }
        else
        {
            v61 = 0;
        }
    }
    else
    {
        v61 = 0;
    }
    if (!(v61 < 2 & v39))
        return;
    sub_40ea58(v58, v51);
    return;
}
```

## `sub_0041aad4` `0x0041aad4`

_194 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
    struct struct_0 *field_1c;
    unsigned int field_20;
    char field_24;
    unsigned short field_25;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
    char field_4;
} struct_0;

typedef struct struct_3 {
    unsigned int field_0;
} struct_3;

extern struct_3 *g_41f148;
extern struct_3 *g_41f14c;

int sub_41aad4(void)
{
    struct_1 *idx;  // eax
    unsigned int v10;  // esi
    struct_1 *v19;  // eax
    struct_1 *v20;  // eax
    unsigned int v21;  // esi
    unsigned int v11;  // ebx
    struct_0 *v12;  // eax
    unsigned int v13;  // esi
    unsigned int v14;  // esi
    struct_1 *v15;  // ebx
    unsigned int i;  // esi
    unsigned int v17;  // edx
    struct_1 *v18;  // eax
    struct_0 *v0;  // [bp-0x18]
    unsigned short v1;  // [bp-0x14]
    unsigned short v2;  // [bp-0x12]
    struct_1 *v3;  // [bp-0x10]
    char v4;  // [bp-0xc], Other Possible Types: unsigned int
    char *v5;  // [bp-0x8], Other Possible Types: unsigned int
    unsigned long v6;  // [bp-0x4]
    int <0x41aad4[is_1]|Stack bp, 1 B>;  // [bp+0x0]
    struct_0 *v7;  // [bp+0x0]

    v6 = &<0x41aad4[is_1]|Stack bp, 1 B>;
    v5 = &v6;
    v7 = idx->field_1c;
    v0 = idx->field_1c;
    v5 = 5;
    g_41f14c(4294967295, &v0, &v5, 64, &v4, v10, v11, idx->field_1c);
    v12 = idx->field_1c;
    v12->field_0 = idx->field_20;
    v12->field_4 = idx->field_24;
    v5 = 5;
    g_41f14c(4294967295, &v0, &v5, v4, &v4);
    v13 = idx->field_18 - 1;
    if (v13 < 0)
        return;
    v14 = v13 + 1;
    v15 = &(&idx->field_24)[1];
    do
    {
        i = v14;
        v17 = 0;
        v18 = v15;
        do
        {
            v19 = v18;
        } while (*((short *)&v19->padding_0[0]) && (v17 += 1, v20 = v19 + 2, v18 = v19 + 2, v17 != 259));
        v1 = (unsigned short)v17 * 2;
        v2 = v1 + 2;
        v3 = v15;
        g_41f148(0, 0, &v1, &v5);
        v15 += 13;
        v21 = i - 1;
        v14 = v21;
    } while (i != 1);
    return;
}
```

## `sub_0041ab96` `0x0041ab96`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41ab96(unsigned int a0, unsigned int a1)
{
    return sub_41ab98();
}
```

## `sub_0041ab98` `0x0041ab98`

_794 bytes. calls ReadProcessMemory, WriteProcessMemory; refs "E#qw"_

```c
typedef struct struct_1 {
    char padding_0[8];
    struct struct_0 *field_8;
} struct_1;

typedef struct struct_0 {
    char padding_0[20];
    PWSTR field_14;
} struct_0;

extern char g_41eda4;
extern char g_41f13c;
extern unsigned int g_41f148;
extern unsigned int g_41f14c;

int sub_41ab98(void)
{
    unsigned int v28;  // ebx
    unsigned int *v29;  // esi
    unsigned int v38;  // edi
    unsigned int v30;  // edi
    char iter[4];  // edi
    unsigned int v32;  // ecx
    unsigned int v33;  // edx
    unsigned int v34;  // esi
    unsigned int v35;  // ecx
    HANDLE v36;  // eax
    int v37;  // eax
    unsigned int v0;  // [bp-0x354]
    unsigned int *v1;  // [bp-0x350]
    unsigned int v2;  // [bp-0x34c]
    WCHAR v3[260];  // [bp-0x346]
    char v4;  // [bp-0x13d]
    unsigned int v5;  // [bp-0x13c]
    char v6;  // [bp-0x138]
    int v7;  // [bp-0x137]
    unsigned short v8;  // [bp-0x133]
    unsigned int v9;  // [bp-0x131]
    char v10[4];  // [bp-0x12d]
    int v11;  // [bp-0x129], Other Possible Types: unsigned int
    int v12;  // [bp-0x125]
    unsigned int v13;  // [bp-0x121]
    char v14;  // [bp-0x11d]
    char v15;  // [bp-0x118]
    unsigned int v16;  // [bp-0xf0]
    int v17;  // [bp-0x20]
    int j;  // [bp-0x20]
    char v19;  // [bp-0x19]
    unsigned int v20;  // [bp-0x18]
    unsigned int v21;  // [bp-0x14]
    enum PAGE_PROTECTION_FLAGS v22;  // [bp-0x10]
    unsigned int v23;  // [bp-0xc]
    unsigned int v24;  // [bp-0x8]
    unsigned int *i;  // [bp+0x8]
    struct_1 *v27;  // [bp+0xc]

    v2 = v28;
    v1 = v29;
    v0 = v30;
    iter = &v15;
    for (v32 = 62; v32; i += 1)
    {
        v32 -= 1;
        *((unsigned int *)&iter[0]) = *(i);
        iter += 1;
    }
    v24 = v33;
    if (!g_41f148)
        g_41f148 = sub_40da7c();
    if (!g_41f14c)
        g_41f14c = sub_40da7c();
    if (g_41eda4 || g_41f13c)
        v34 = (!v16 ? 0 : v35 + v16);
    else
        v34 = sub_40da7c();
    if (!v34)
        return;
    if (ReadProcessMemory(v36, v34, &v19, 0x5, &v23) && v19 == 233 && ReadProcessMemory(v36, v34 + 5 + v20, &v4, 0x25, &v23))
    {
        if (v10 == 2003903301)
        {
            if (v9 == 2882398071)
                goto LABEL_41acf5;
        }
        else
        {
            if (v10 == 2003903301)
                goto LABEL_41acf5;
        }
    }
    v4 = 184;
    v5 = 0;
    v6 = 185;
    v7 = sub_40ecb8(0, 0);
    v8 = 53759;
    v9 = 2882398071;
    strncpy(v10, "E#qw", 4);
    v11 = 0;
    v12 = 0;
    v13 = v34;
    ReadProcessMemory(v36, v13, &v14, 0x5, &v23);
LABEL_41acf5:
    if (!v7)
        return;
    if (v11 == v12)
    {
        v21 = v5;
        v11 = (!v11 ? 32 : v11 * 2);
        v5 = sub_40e970(v11 * 528 + 37, v36);
        WriteProcessMemory(v36, v5, &v4, 0x25, &v23);
        v37 = v12 - 1;
        if (v37 >= 0)
        {
            v17 = v37 + 1;
            v38 = 0;
            do
            {
                j = v17;
                ReadProcessMemory(v36, v21 + v38 * 520 + 37, v3, 0x208, &v23);
                WriteProcessMemory(v36, v5 + v38 * 520 + 37, v3, 0x208, &v23);
                v38 += 1;
                v17 = j - 1;
            } while (j != 1);
        }
        v19 = 233;
        v20 = v5 - v34 - 5;
        if (VirtualProtectEx(v36, v34, 0x5, PAGE_EXECUTE_READWRITE, &v22))
        {
            WriteProcessMemory(v36, v34, &v19, 0x5, &v23);
            VirtualProtectEx(v36, v34, 0x5, v22, &v23);
        }
        sub_40ea58(v21, NULL);
    }
    lstrcpyW(v3, v27->field_8->field_14);
    WriteProcessMemory(v36, v5 + v12 * 520 + 37, v3, 0x208, &v23);
    v12 += 1;
    WriteProcessMemory(v36, v5, &v4, 0x25, &v23);
    if (!(char)sub_41a5a0(v27->field_8))
        return;
    return;
}
```

## `sub_0041aeb2` `0x0041aeb2`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41aeb2(void)
{
    sub_41aeb4();
    return;
}
```

## `sub_0041aeb4` `0x0041aeb4`

_182 bytes. (leaf/helper — see body)_

```c
typedef struct OSVERSIONINFOA {
    unsigned int dwOSVersionInfoSize;
    unsigned int dwMajorVersion;
    unsigned int dwMinorVersion;
    unsigned int dwBuildNumber;
    unsigned int dwPlatformId;
    CHAR szCSDVersion[128];
} OSVERSIONINFOA;

int sub_41aeb4(void)
{
    int v5;  // esi
    int v6;  // ebx
    OSVERSIONINFOA v0;  // [bp-0x198]
    char v1;  // [bp-0x104]
    char v2;  // [bp-0xc], Other Possible Types: int
    char v3;  // [bp-0x4]
    int v4;  // [bp+0x4]

    if (!(char)sub_41a5a0(v4, v5, v6))
    {
        return;
    }
    else if ((char)sub_41a7c4(&v2, v4))
    {
        sub_4054b4();
        v0.dwOSVersionInfoSize = 148;
        GetVersionExA(&v0);
        if (v0.dwPlatformId != 2)
        {
            sub_41a864(v2, &v1, &v3);
            return;
        }
        sub_41ab98(v2, &v1, &v3);
        return;
    }
    else
    {
        return;
    }
}
```

## `sub_0041af6a` `0x0041af6a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41af6a(void)
{
    sub_41af6c();
    return;
}
```

## `sub_0041af6c` `0x0041af6c`

_213 bytes. (leaf/helper — see body)_

```c
int sub_41af6c(void)
{
    int *v5;  // ecx
    unsigned int v6;  // ebx
    unsigned int v7;  // esi
    unsigned int v8;  // edi
    unsigned int v9;  // edx
    int v10;  // eax
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    int *v3;  // [bp-0x8], Other Possible Types: unsigned int
    void* v4;  // [bp+0x4]

    v3 = v5;
    v2 = v6;
    v1 = v7;
    v0 = v8;
    v3 = v9;
    *(v5) = 0;
    if (!(GetVersion() & 0x80000000))
        *((int *)&v4[4]) = sub_4178ec();
    if (!(char)sub_41a5a0(v4))
    {
        if ((char)v4[8])
            *(v5) = sub_41a334((int)v4[20], (int)v4[24]);
        else
            *(v5) = 0;
        return;
    }
    else if ((char)v4[12])
    {
        v10 = sub_41aeb4(v4);
        if (v10 < 1)
        {
            return;
        }
        else if (v10 == 1)
        {
            if ((char)v4[8])
                *(v5) = sub_41a334((int)v4[20], (int)v4[24]);
            else
                *(v5) = 0;
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
```

## `sub_0041b047` `0x0041b047`

_21 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

int sub_41b047(void)
{
    struct_0 **v1;  // eax
    char *v2;  // eax
    char v3;  // ch
    char *v4;  // eax

    v2 = (*(v1))();
    *(v2) = *(v2) + *((char *)&v2);
    v4 = _INSERT(v2, 0, *((char *)&v2) + v3);
    *(v4) = *(v4) + *((char *)&v2) + v3;
    *(v4) = *(v4) + *((char *)&v2) + v3;
    4304988();
}
```

## `sub_0041b063` `0x0041b063`

_30 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_41b000;

int sub_41b063(void)
{
    unsigned int *v6;  // ebx
    char *v7;  // eax
    char v8;  // dl
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]
    unsigned int v2;  // [bp-0x4]
    char v4;  // [bp+0xfff8d]
    unsigned int v5;  // [bp+0x10000c]

    v2 = *(v6);
    *(v7) = *(v7) + *((char *)&v7);
    v4 += v8;
    v1 = &g_41b000;
    v0 = v5;
    sub_41b081();
}
```

## `sub_0041b081` `0x0041b081`

_26 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

int sub_41b081(void)
{
    unsigned int v2;  // eax
    struct_0 **v3;  // ebx
    unsigned int v1;  // [bp+0x10000c]

    if (!v2)
        return;
    (*(v3))(v1);
    return;
}
```

## `sub_0041b09b` `0x0041b09b`

_1269 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[32];
    struct struct_1 *field_20;
    unsigned int field_24;
    unsigned int field_28;
    char padding_2c[67];
    struct struct_2 *field_6f;
    struct struct_2 *field_73;
    char padding_77[4];
    struct struct_2 *field_7b;
    struct struct_2 *field_7f;
    struct struct_2 *field_83;
    struct struct_2 *field_87;
    struct struct_2 *field_8b;
    struct struct_2 *field_8f;
    unsigned short field_93;
    char padding_95[92];
    unsigned int field_f1;
    unsigned int field_f5;
    char padding_f9[4];
    struct struct_2 *field_fd;
    struct struct_2 *field_101;
    struct struct_2 *field_105;
    struct struct_2 *field_109;
    char padding_10d[32];
    struct struct_2 *field_12d;
    char padding_131[4];
    struct struct_2 *field_135;
    char padding_139[12];
    struct struct_2 *field_145;
} struct_0;

typedef struct struct_17 {
    char padding_0[4];
    unsigned int field_4;
} struct_17;

typedef struct struct_18 {
    char padding_0[1];
    char field_1;
} struct_18;

typedef struct struct_19 {
    char padding_0[8];
    int field_8;
} struct_19;

typedef struct struct_20 {
    char padding_0[12];
    unsigned int field_c;
} struct_20;

typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
} struct_1;

typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

int sub_41b09b(void)
{
    unsigned short v44;  // dx
    struct_0 *v54;  // eax
    unsigned short *iter;  // edx
    unsigned int iter1;  // esi
    struct_0 *v58;  // ecx
    unsigned int v59;  // edi
    int v60;  // edi
    void* node;  // ecx
    struct_20 *k;  // esi
    unsigned int v63;  // ecx
    unsigned int v46;  // ebx
    int j;  // edi
    unsigned short v65;  // ax
    unsigned int v47;  // esi
    unsigned int v48;  // edi
    struct_0 *idx;  // ebx
    unsigned int v50[2];  // eax
    unsigned int *v51;  // eax
    char v52;  // al
    unsigned int i;  // esi
    int v0;  // [bp-0x194]
    unsigned int v1;  // [bp-0x190]
    unsigned int v2;  // [bp-0x94]
    unsigned int v3;  // [bp-0x90]
    unsigned int v4;  // [bp-0x8c]
    unsigned short v6;  // [bp+0xfff7c]
    unsigned short v7;  // [bp+0xfff7e]
    unsigned short v8;  // [bp+0xfff80]
    unsigned short v9;  // [bp+0xfff82]
    unsigned short v10;  // [bp+0xfff84]
    unsigned short v11;  // [bp+0xfff86]
    unsigned short v12;  // [bp+0xfff88]
    unsigned short v13;  // [bp+0xfff8a]
    unsigned short v14;  // [bp+0xfff8c]
    unsigned short v15;  // [bp+0xfff8e]
    char v16;  // [bp+0xfff8f]
    unsigned short v17;  // [bp+0xfff90]
    unsigned short v18;  // [bp+0xfff92]
    unsigned short v19;  // [bp+0xfff94]
    unsigned short v20;  // [bp+0xfffb0]
    unsigned short v21;  // [bp+0xfffb2]
    unsigned int v22;  // [bp+0xfffb4]
    unsigned int v23;  // [bp+0xfffb8]
    unsigned int v24;  // [bp+0xfffbc]
    unsigned int v25;  // [bp+0xfffc0]
    unsigned int v26;  // [bp+0xfffc4]
    unsigned int v27;  // [bp+0xfffc8]
    unsigned short v28;  // [bp+0xfffcc]
    unsigned short v29;  // [bp+0xfffce]
    void* v30;  // [bp+0xfffd0], Other Possible Types: unsigned int
    unsigned int v31;  // [bp+0xfffd4]
    char v32;  // [bp+0xfffda]
    char v33;  // [bp+0xfffdb]
    struct_18 *v34;  // [bp+0xfffdc], Other Possible Types: unsigned int
    unsigned int *v35;  // [bp+0xfffe0], Other Possible Types: unsigned int
    unsigned int v36;  // [bp+0xfffe4]
    unsigned int v37;  // [bp+0xfffe8]
    unsigned int v38;  // [bp+0xfffec]
    unsigned int v39;  // [bp+0xffff0]
    void* v40;  // [bp+0xffff4]
    struct_19 *v41;  // [bp+0xffff8]
    unsigned int v42;  // [bp+0xffffc]
    struct_17 *v43;  // [bp+0x100000], Other Possible Types: unsigned int

    v16 += (char)v44;
    v4 = v46;
    v3 = v47;
    v2 = v48;
    idx = _INSERT(0, 0, x86g_dirtyhelper_IN(Conv(16I->32I, vvar_308{r16|2b}), 0x1<32>));
    v43 = /* unsupported instruction */;
    if (idx->field_20)
    {
        v43->field_4 = idx->field_20;
        v31 = idx->field_20;
        v43 = 8;
        if (!(*((int *)&idx->padding_131[1]))(4294967295, /* unsupported instruction */ - 48, /* unsupported instruction */ - 4, 64, /* unsupported instruction */ - 28))
        {
            v50 = idx->field_20;
            v50[0] = idx->field_24;
            v50[1] = idx->field_28;
            v31 = v50;
            v43 = 8;
            (*((int *)&idx->padding_131[1]))(4294967295, /* unsupported instruction */ - 48, /* unsupported instruction */ - 4, v37, /* unsupported instruction */ - 28);
        }
        v42 = 4294967295;
    }
    else
    {
        v42 = 0;
    }
    if (!idx->field_20)
        return;
    v43 = 0;
    v28 = 24;
    v29 = 26;
    v30 = /* unsupported instruction */ - 0x88;
    v6 = 107;
    v7 = 101;
    v8 = 114;
    v9 = 110;
    v10 = 101;
    v11 = 108;
    v12 = 0x33;
    v13 = 50;
    v14 = 46;
    v15 = 100;
    v17 = 108;
    v18 = 108;
    v19 = 0;
    if ((*((int *)((char *)&idx->field_6f + 3)))(0, 0, /* unsupported instruction */ - 56, /* unsupported instruction */ - 4))
    {
        return;
    }
    else if (*((int *)((char *)&idx->field_73 + 3)) == v43)
    {
        if (*((int *)&idx->padding_139[9]) && *((char *)(*((int *)&idx->padding_139[9]) - 1)) == 232)
        {
            v31 = *((int *)&idx->padding_139[9]);
            v43 = 4;
            if (!(*((int *)&idx->padding_131[1]))(4294967295, /* unsupported instruction */ - 48, /* unsupported instruction */ - 4, 64, /* unsupported instruction */ - 28))
            {
                v51 = *((int *)&idx->padding_139[9]);
                *(v51) = &idx->padding_2c[16 + -1 * *((int *)&idx->padding_139[9]) + 4];
                v31 = v51;
                v43 = 4;
                (*((int *)&idx->padding_131[1]))(4294967295, /* unsupported instruction */ - 48, /* unsupported instruction */ - 4, v37, /* unsupported instruction */ - 28);
            }
        }
        v34 = NULL;
        v35 = NULL;
        if ((*((int *)((char *)&idx->field_fd + 1)))(4294967295, 8, /* unsupported instruction */ - 32) >= 0)
        {
            v43 = 0;
            (*((int *)&idx->padding_f9[1]))(v36, 1, 0, 0, /* unsupported instruction */ - 4);
            v43 *= 2;
            if (!(*((int *)&idx->padding_10d[29]))(4294967295, /* unsupported instruction */ - 36, 0, /* unsupported instruction */ - 4, 0x1000, 64) && v35)
            {
                if ((*((int *)&idx->padding_f9[1]))(v36, 1, v35, v43, /* unsupported instruction */ - 4) < 0)
                {
                    v43 = 0;
                    (*((int *)((char *)&idx->field_7b + 3)))(4294967295, /* unsupported instruction */ - 36, /* unsupported instruction */ - 4, 0x8000);
                    v35 = 0;
                }
                else
                {
                    v34 = *(v35);
                }
            }
            (*((int *)&idx->padding_77[3]))(v36);
        }
        if (v34 && v34->field_1 > 1)
            v52 = 0;
        else
            v52 = 1;
        v32 = v52;
        v40 = NULL;
        i = 26;
        v54 = (char *)&idx->field_8f + 3;
        iter = /* unsupported instruction */ - 0x88;
        do
        {
            *(iter) = *((short *)&v54->padding_0[0]);
            iter += 1;
            v54 = &v54->padding_0[2];
            i -= 1;
        } while (i != 1);
        iter1 = 1;
        do
        {
            v33 = 1;
            v20 = (unsigned short)iter1 + 48;
            v21 = 0;
            v22 = 24;
            v23 = 0;
            v24 = /* unsupported instruction */ - 56;
            v25 = 0;
            v26 = 0;
            v27 = 0;
            v28 = 54;
            v29 = 56;
            v30 = /* unsupported instruction */ - 0x88;
            if (!(*((int *)((char *)&idx->field_83 + 3)))(/* unsupported instruction */ - 20, 4, /* unsupported instruction */ - 80))
            {
                v43 = 0;
                v41 = NULL;
                if (!(*((int *)((char *)&idx->field_87 + 3)))(v39, 4294967295, /* unsupported instruction */ - 12, 0, 0, 0, /* unsupported instruction */ - 4, 1, 0, 2))
                {
                    v58 = &idx->padding_95[91];
                    if (*((int *)&v41->padding_0[4]) == *((int *)&v58->padding_0[4]) && *((int *)&v41->padding_0[0]) == *((int *)&v58->padding_0[0]))
                    {
                        v33 = 0;
                        v59 = v41->field_8 - 1;
                        if (v59 >= 0)
                        {
                            v60 = v59 + 1;
                            v38 = 0;
                            do
                            {
                                if (!v40 && (v43 = 1144, (*((int *)&idx->padding_10d[29]))(4294967295, /* unsupported instruction */ - 16, 0, /* unsupported instruction */ - 4, 0x1000, 64) || !v40))
                                {
                                    v33 = 1;
                                    break;
                                }
                                else
                                {
                                    node = v40;
                                    v1 = iter1;
                                    v0 = v60;
                                    k = 12 + (char *)v41 + 1144 * v38;
                                    for (v63 = 286; v63; k = &k->padding_0[4])
                                    {
                                        v63 -= 1;
                                        *((int *)node) = *((int *)&k->padding_0[0]);
                                        node += 4;
                                    }
                                    j = v60;
                                    if (!*((short *)v40))
                                    {
                                        v33 = 1;
                                        break;
                                    }
                                }
                                if ((!(char)(*((int *)((char *)&idx->field_101 + 1)))(v40 + 1040) || !v34 || v34 && (char)(*((int *)((char *)&idx->field_105 + 1)))(v40 + 1040, v34)) && ((char)v40[1131] || !v32) && ((int)v40[1140] == 4294967295 || (*((int *)((char *)&idx->field_7f + 3)))(4294967295, 24, /* unsupported instruction */ - 4, 4, 0) || (int)v40[1140] == v43))
                                {
                                    v43 = 0;
                                    do
                                    { } while (*((short *)((char *)v40 + 2 * v43)) && (v43 += 1, v43 != 260));
                                    v65 = (short)v43 * 2;
                                    v28 = v65;
                                    v29 = v65 + 2;
                                    v30 = v40;
                                    (*((int *)&(idx->padding_2c)[1]))(0, 0, /* unsupported instruction */ - 56, /* unsupported instruction */ - 4);
                                }
                                v38 += 1;
                                v60 = j - 1;
                            } while (j != 1);
                        }
                    }
                    (*((int *)((char *)&idx->field_8b + 3)))(4294967295, v41);
                }
                (*((int *)&idx->padding_77[3]))(v39);
            }
        } while (!v33 && (iter1 += 1, iter1 != 10));
        if (v40)
        {
            v43 = 0;
            (*((int *)((char *)&idx->field_7b + 3)))(4294967295, /* unsupported instruction */ - 16, /* unsupported instruction */ - 4, 0x8000);
        }
        if (!v35)
            return;
        v43 = 0;
        (*((int *)((char *)&idx->field_7b + 3)))(4294967295, /* unsupported instruction */ - 36, /* unsupported instruction */ - 4, 0x8000);
        return;
    }
    else
    {
        return;
    }
}
```

## `sub_0041b590` `0x0041b590`

_820 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    char padding_0[123];
    struct struct_3 *field_7b;
    struct struct_3 *field_7f;
    struct struct_3 *field_83;
    struct struct_3 *field_87;
    struct struct_3 *field_8b;
    struct struct_3 *field_8f;
    unsigned short field_93;
    char padding_95[92];
    unsigned int field_f1;
    unsigned int field_f5;
    char padding_f9[4];
    struct struct_3 *field_fd;
    struct struct_3 *field_101;
    struct struct_3 *field_105;
    struct struct_3 *field_109;
    char padding_10d[12];
    struct struct_3 *field_119;
    char padding_11d[16];
    struct struct_3 *field_12d;
} struct_2;

typedef struct struct_0 {
    char padding_0[1];
    char field_1;
} struct_0;

typedef struct struct_15 {
    char padding_0[8];
    unsigned int field_8;
} struct_15;

typedef struct struct_16 {
    char padding_0[12];
    unsigned int field_c;
} struct_16;

typedef struct struct_3 {
    unsigned int field_0;
} struct_3;

char sub_41b590(unsigned int a0, struct_2 *a1)
{
    struct_2 *v25;  // esi
    unsigned int v26;  // edi
    struct_2 *v35;  // ecx
    unsigned int v36;  // edi
    unsigned int v37;  // edi
    struct_16 *j;  // esi
    unsigned int v39;  // ecx
    unsigned int *iter;  // edi
    unsigned int v41;  // edi
    unsigned int v27;  // esi
    unsigned int v28;  // ebx
    char v29;  // al
    unsigned int i;  // ebx
    struct_2 *v31;  // eax
    char node[2];  // edx
    unsigned int v34;  // ebx
    unsigned int v0;  // [bp-0x144]
    struct_2 *v1;  // [bp-0x140]
    char v2;  // [bp-0x82]
    unsigned short v3;  // [bp-0x4e]
    unsigned short v4;  // [bp-0x4c]
    unsigned int v5;  // [bp-0x4a]
    unsigned int v6;  // [bp-0x46]
    char *v7;  // [bp-0x42]
    unsigned int v8;  // [bp-0x3e]
    unsigned int v9;  // [bp-0x3a]
    unsigned int v10;  // [bp-0x36]
    unsigned short v11;  // [bp-0x32]
    unsigned short v12;  // [bp-0x30]
    char *v13;  // [bp-0x2e]
    char v14;  // [bp-0x2a]
    char v15;  // [bp-0x29]
    struct_0 *v16;  // [bp-0x28]
    struct_0 **v17;  // [bp-0x24]
    char v18;  // [bp-0x20], Other Possible Types: unsigned int
    unsigned int v19;  // [bp-0x1c]
    unsigned int v20;  // [bp-0x18]
    char v21;  // [bp-0x14], Other Possible Types: unsigned int
    unsigned int *v22;  // [bp-0x10]
    struct_15 *v23;  // [bp-0xc]
    char v24;  // [bp-0x5]

    v25 = a1;
    v24 = 1;
    v16 = NULL;
    v17 = NULL;
    if ((*((int *)((char *)&v25->field_fd + 1)))(4294967295, 8, &v18, v26, v27, v28) >= NULL)
    {
        v19 = 0;
        (*((int *)&v25->padding_f9[1]))(v18, 1, 0, 0, &v19);
        v19 *= 2;
        if (!(*((int *)&v25->padding_11d[13]))(4294967295, &v17, 0, &v19, 0x1000, 64) && v17)
        {
            if ((*((int *)&v25->padding_f9[1]))(v18, 1, v17, v19, &v19) < NULL)
            {
                v19 = 0;
                (*((int *)((char *)&v25->field_7b + 3)))(4294967295, &v17, &v19, 0x8000);
                v17 = NULL;
            }
            else
            {
                v16 = *(v17);
            }
        }
        (*((int *)&(v25->padding_0)[1]))(v18);
    }
    if (v16 && v16->field_1 > 1)
        v29 = 0;
    else
        v29 = 1;
    v14 = v29;
    v22 = NULL;
    i = 26;
    v31 = (char *)&v25->field_8f + 3;
    node = &v2;
    do
    {
        *((short *)&node[0]) = *((short *)&v31->padding_0[0]);
        node += 1;
        v31 = &v31->padding_0[2];
        i -= 1;
    } while (i != 1);
    v34 = 1;
    do
    {
        v15 = 1;
        v3 = (unsigned short)v34 + 48;
        v4 = 0;
        v5 = 24;
        v6 = 0;
        v7 = &v11;
        v8 = 0;
        v9 = 0;
        v10 = 0;
        v11 = 54;
        v12 = 56;
        v13 = &v2;
        if (!(*((int *)((char *)&v25->field_83 + 3)))(&v21, 4, &v5))
        {
            v19 = 0;
            v23 = NULL;
            if (!(*((int *)((char *)&v25->field_87 + 3)))(v21, 4294967295, &v23, 0, 0, 0, &v19, 1, 0, 2))
            {
                v35 = &v25->padding_95[91];
                if (*((int *)&v23->padding_0[4]) == *((int *)&v35->padding_0[4]) && *((int *)&v23->padding_0[0]) == *((int *)&v35->padding_0[0]))
                {
                    v15 = 0;
                    v36 = v23->field_8 - 1;
                    if (v36 >= NULL)
                    {
                        v37 = v36 + 1;
                        v20 = 0;
                        do
                        {
                            if (!v22 && (v19 = 1144, (*((int *)&v25->padding_11d[13]))(4294967295, &v22, 0, &v19, 0x1000, 64) || !v22))
                            {
                                v15 = 1;
                                break;
                            }
                            else
                            {
                                v1 = v25;
                                v0 = v37;
                                j = 12 + (char *)v23 + 1144 * v20;
                                v39 = 286;
                                for (iter = v22; v39; j = &j->padding_0[4])
                                {
                                    v39 -= 1;
                                    *(iter) = *((int *)&j->padding_0[0]);
                                    iter += 1;
                                }
                                v41 = v37;
                                if (!*((short *)v22))
                                {
                                    v15 = 1;
                                    break;
                                }
                                else if ((!(char)(*((int *)((char *)&v25->field_101 + 1)))(v22 + 260) || !v16 || v16 && (char)(*((int *)((char *)&v25->field_105 + 1)))(v22 + 260, v16)) && (*((char *)&v22[282] + 3) || !v14) && (v22[285] == 4294967295 || (*((int *)((char *)&v25->field_7f + 3)))(4294967295, 24, &v19, 4, 0) || v22[285] == v19) && (*((int *)&v25->padding_10d[9]))(v22) == a0)
                                {
                                    v24 = 0;
                                    v15 = 1;
                                    break;
                                }
                            }
                        } while ((v20 += 1, v37 = v41 - 1, v41 != 1));
                    }
                }
                (*((int *)((char *)&v25->field_8b + 3)))(4294967295, v23);
            }
            (*((int *)&(v25->padding_0)[1]))(v21);
        }
    } while (!v15 && (v34 += 1, v34 != 10));
    if (v22)
    {
        v19 = 0;
        (*((int *)((char *)&v25->field_7b + 3)))(4294967295, &v22, &v19, 0x8000);
    }
    if (v17)
    {
        v19 = 0;
        (*((int *)((char *)&v25->field_7b + 3)))(4294967295, &v17, &v19, 0x8000);
    }
    return v24;
}
```

## `sub_0041b8c4` `0x0041b8c4`

_405 bytes. (leaf/helper — see body)_

```c
int sub_41b8c4(void)
{
    unsigned int v16;  // ecx
    int v17;  // edi
    int v26;  // esi
    int v27;  // esi
    unsigned int v28;  // ebx
    int v29;  // esi
    unsigned int v30;  // eax
    unsigned int v31;  // edx
    int v32;  // esi
    unsigned int v33;  // eax
    int v34;  // esi
    int v35;  // esi
    int v18;  // esi
    unsigned int v36;  // ebx
    int v37;  // esi
    int v38;  // esi
    unsigned long v39;  // 4118
    int v19;  // ebx
    unsigned long v20;  // ldt
    unsigned long v21;  // gdt
    unsigned short v22;  // fs
    unsigned long v23;  // 4128
    unsigned int v24;  // 4103
    unsigned long v25;  // 4137
    unsigned int v0;  // [bp-0xc0]
    unsigned int v1;  // [bp-0xbc]
    unsigned int v2;  // [bp-0xb8]
    unsigned int v3;  // [bp-0x9c]
    unsigned int v4;  // [bp-0x80]
    char v5;  // [bp-0x7c]
    char v6;  // [bp-0x77]
    unsigned int v7;  // [bp-0x74]
    unsigned int v8;  // [bp-0x38]
    int v9;  // [bp-0x18]
    unsigned int v10;  // [bp-0x14]
    HMODULE v11;  // [bp-0x10]
    unsigned int v12;  // [bp-0xc]
    unsigned int v13;  // [bp-0x8]
    char v14;  // [bp-0x4]
    char v15;  // [bp+0x4]

    v4 = 0;
    v13 = v16;
    sub_403e68(v17, v18, v19);
    sub_40402c(v17, v18, v19);
    v23 = _ccall(v20, v21, (unsigned int)v22, 0);
    v24 = *((int *)v23);
    v1 = *((int *)v23);
    v25 = _ccall(v20, v21, (unsigned int)v22, 0);
    *((unsigned int **)v25) = &v1;
    v12 = 0;
    sub_40d8e0(v24, sub_41ba78, &v14);
    v26 = sub_404654();
    if (v26 >= 0)
    {
        v27 = v26 + 1;
        v28 = 0;
        do
        {
            v29 = v27;
            v30 = v28 * 7;
            if (v31 == *((int *)(v8 + v30 * 4 + 12)))
            {
                v12 = (!v15 ? *((int *)(v8 + v30 * 4 + 4)) : *((int *)(v8 + v30 * 4 + 20)));
                break;
            }
        } while ((v28 += 1, v32 = (int)(v29 - 1), v27 = (int)(v29 - 1), v29 != 1));
    }
    if (!v12)
    {
        sub_409eac();
        v33 = sub_403e78();
        v11 = sub_4052c4(v33);
        v10 = sub_40a83c(v24);
        v0 = v33;
        if (v10)
        {
            v9 = sub_40a658();
            v34 = sub_404654();
            if (v34 >= 0)
            {
                v35 = v34 + 1;
                v36 = 0;
                do
                {
                    v37 = v35;
                    sub_40a7c0();
                    sub_40c63c();
                    if (v31 == v7 || sub_40a7c0() == v7 - v10 || v5 && v6 && (sub_40c63c(), v31 == v3))
                    {
                        if (v15)
                        {
                            v12 = *((int *)(v8 + v36 * 28 + 20));
                            break;
                        }
                        else
                        {
                            v12 = *((int *)(v8 + v36 * 28 + 4));
                            break;
                        }
                    }
                } while ((v36 += 1, v38 = (int)(v37 - 1), v35 = (int)(v37 - 1), v37 != 1));
            }
            UnmapViewOfFile(v10);
            v0 = v10;
        }
    }
    v39 = _ccall(v20, v21, (unsigned int)v22, 0);
    *((unsigned int *)v39) = v0;
    v2 = sub_41ba7f;
    sub_41ba59();
    return;
}
```

## `sub_0041ba59` `0x0041ba59`

_31 bytes. (leaf/helper — see body)_

```c
int sub_41ba59(void)
{
    sub_403a10();
    sub_4040f0();
    return sub_403a10();
}
```

## `sub_0041ba78` `0x0041ba78`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_41ba78(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041ba7d` `0x0041ba7d`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41ba7d(void)
{
    return sub_41ba59();
}
```

## `sub_0041ba7f` `0x0041ba7f`

_12 bytes. (leaf/helper — see body)_

```c
int sub_41ba7f(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // [bp+0xffffc]

    return v0;
}
```

## `sub_0041ba8b` `0x0041ba8b`

_1 bytes. (leaf/helper — see body)_

```c
int sub_41ba8b(void)
{
    sub_41ba8c();
    return;
}
```

## `sub_0041ba8c` `0x0041ba8c`

_16 bytes. (leaf/helper — see body)_

```c
int sub_41ba8c(void)
{
    char *v1;  // eax

    if (!v1)
        return;
    return;
}
```

## `sub_0041ba9c` `0x0041ba9c`

_42 bytes. (leaf/helper — see body)_

```c
int sub_41ba9c(void)
{
    sub_40d994(sub_40da7c(1));
    return sub_41b8c4();
}
```

## `sub_0041bac6` `0x0041bac6`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41bac6(void)
{
    return sub_41bac8();
}
```

## `sub_0041bac8` `0x0041bac8`

_1279 bytes. refs ", v2);
    sub_409ee0(", ", v0);
    sub_409ee0(", ", v0, v1, "_

```c
typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
} struct_0;

int sub_41bac8(void)
{
    unsigned int i;  // ecx
    unsigned int v12;  // ecx
    int v21;  // ebx
    void* idx;  // eax
    struct_0 *index;  // edx
    struct_0 *v24;  // ecx
    unsigned int v25[2];  // edi
    unsigned int v26;  // eax
    unsigned int v27;  // eax
    unsigned long v28;  // 4118
    unsigned long v13;  // ldt
    unsigned long v14;  // gdt
    unsigned short v15;  // fs
    unsigned long v16;  // 4154
    unsigned int v17;  // 4117
    unsigned long v18;  // 4163
    int v19;  // edi
    int v20;  // esi
    int v0;  // [bp-0xac]
    int v1;  // [bp-0xa8]
    int v2;  // [bp-0x9c]
    int v3;  // [bp-0x98]
    unsigned int v4;  // [bp-0x48]
    unsigned int v5;  // [bp-0x34]
    unsigned int v6;  // [bp-0x18]
    unsigned int v7;  // [bp-0x14]
    unsigned int v8;  // [bp-0xc]
    char v9;  // [bp-0x4]

    i = 21;
    do
    {
        v7 = 0;
        v6 = 0;
        i -= 1;
    } while (i != 1);
    InterlockedExchange(&v24, v12);
    v16 = _ccall(v13, v14, (unsigned int)v15, 0);
    v17 = *((int *)v16);
    v5 = *((int *)v16);
    v18 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int **)v18) = &v5;
    sub_40d8e0(v17, sub_41bfee, &v9, v19, v20, v21, v12);
    sub_40421c(v17, sub_41bfee, &v9, v19, v20, v21, v12);
    sub_40d8e0();
    sub_40421c();
    sub_4054b4();
    *((unsigned int *)idx) = index->field_c + 329 + v24->field_c;
    v25 = sub_40da7c();
    *((unsigned int *[2])&idx[32]) = v25;
    *((unsigned int *)&idx[36]) = v25[0];
    *((unsigned int *)&idx[40]) = v25[1];
    sub_403ed0();
    sub_402628();
    *((int *)&idx[111]) = sub_40da7c();
    *((int *)&idx[115]) = sub_40da7c();
    *((int *)&idx[0x77]) = sub_40d900();
    *((int *)&idx[123]) = sub_40da7c();
    *((int *)&idx[127]) = sub_40da7c();
    *((int *)&idx[131]) = sub_40da7c();
    *((int *)&idx[135]) = sub_40da7c();
    *((int *)&idx[139]) = sub_40da7c();
    *((int *)&idx[143]) = sub_40da7c();
    sub_409eac();
    sub_409eac(v3);
    sub_403d40("0", v2);
    sub_409ee0("0", v2);
    sub_402628();
    *((int *)&idx[237]) = sub_40da7c();
    sub_409eac();
    sub_409eac(v1);
    sub_403d40("0", v0);
    sub_409ee0("0", v0);
    sub_402628();
    sub_409eac();
    sub_402628();
    *((int *)&idx[249]) = sub_40d994();
    *((int *)&idx[253]) = sub_40da7c();
    *((int *)&idx[0x101]) = sub_40da7c();
    *((int *)&idx[261]) = sub_40da7c();
    *((int *)&idx[265]) = sub_40da7c();
    *((int *)&idx[269]) = sub_40d994();
    *((int *)&idx[273]) = sub_40d994();
    *((int *)&idx[277]) = sub_40d994();
    *((int *)&idx[281]) = sub_40d994();
    *((int *)&idx[285]) = sub_40d994();
    *((int *)&idx[289]) = sub_40d994();
    *((int *)&idx[297]) = sub_40d994();
    *((int *)&idx[293]) = sub_40d994();
    *((int *)&idx[301]) = sub_40da7c();
    *((int *)&idx[305]) = sub_40da7c();
    *((int *)&idx[309]) = sub_40da7c();
    *((int *)&idx[313]) = sub_40da7c();
    *((int *)&idx[317]) = sub_40da7c();
    *((int *)&idx[4]) = sub_41ba8c();
    *((int *)&idx[8]) = sub_41ba8c();
    *((int *)&idx[12]) = sub_41ba8c();
    *((unsigned long *)&idx[16]) = idx + 44 - idx;
    *((int *)&idx[321]) = sub_40d994();
    *((int *)&idx[325]) = sub_41ba9c();
    sub_403ed0();
    sub_402628();
    *((unsigned int *)&idx[56]) = idx + 329 - (idx + 56) - 4;
    *((unsigned int *)&idx[81]) = idx + 329 + index->field_c - (idx + 81) - 4;
    *((unsigned long *)&idx[95]) = idx + 237 - idx;
    sub_409eac(*((int *)idx));
    v26 = sub_403e78(*((int *)idx));
    v8 = sub_4113d8(v26, *((int *)idx));
    v27 = (unsigned int)MapViewOfFile(v8, FILE_MAP_ALL_ACCESS, 0, 0, NULL);
    sub_402628("0", v0, v1, "0", v2);
    sub_402628();
    sub_402628();
    UnmapViewOfFile(v27);
    sub_40e878();
    CloseHandle(v8);
    v28 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int *)v28) = v27;
    v4 = sub_41bff5;
    sub_41bfc7();
    return;
}
```

## `sub_0041bfc7` `0x0041bfc7`

_39 bytes. (leaf/helper — see body)_

```c
int sub_41bfc7(void)
{
    sub_403a34();
    return sub_404124();
}
```

## `sub_0041bfee` `0x0041bfee`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_41bfee(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041bff3` `0x0041bff3`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41bff3(void)
{
    return sub_41bfc7();
}
```

## `sub_0041bff5` `0x0041bff5`

_9 bytes. (leaf/helper — see body)_

```c
int sub_41bff5(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // ebx

    return v0;
}
```

## `sub_0041c00c` `0x0041c00c`

_346 bytes. calls ReadProcessMemory, WriteProcessMemory_

```c
typedef struct struct_0 {
    unsigned int field_0;
    char padding_4[28];
    void* field_20;
    char padding_24[289];
    void* field_145;
} struct_0;

typedef struct struct_1 {
    char padding_0[4];
    void* field_4;
    char padding_8[4];
    UIntPtr field_c;
} struct_1;

int sub_41c00c(void)
{
    struct_0 *v7;  // ecx
    HANDLE v8;  // eax
    unsigned int v9;  // edi
    char v0;  // [bp-0x1a]
    enum PAGE_PROTECTION_FLAGS v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x5]
    struct_1 *v5;  // [bp+0x4]
    struct_1 *v6;  // [bp+0x8]

    v4 = 0;
    v9 = sub_40e970(v7->field_0, v8);
    if (!WriteProcessMemory(v8, v9, v7, 0x149, &v3))
    {
        return;
    }
    else if (!WriteProcessMemory(v8, v9 + 329, v6->field_4, v6->field_c, &v3))
    {
        return;
    }
    else if (WriteProcessMemory(v8, 329 + v9 + (char *)v6->field_c, v5->field_4, v5->field_c, &v3))
    {
        if (v7->field_20)
        {
            if (!ReadProcessMemory(v8, v7->field_20, &v0, 0x5, &v3))
            {
                return;
            }
            else if (!WriteProcessMemory(v8, v9 + 36, &v0, 0x5, &v3))
            {
                return;
            }
        }
        v4 = 1;
        if (!*((int *)&(v7->padding_24)[1]))
        {
            return;
        }
        else if (!ReadProcessMemory(v8, *((int *)&(v7->padding_24)[1]) - 1, &v0, 0x5, &v3))
        {
            return;
        }
        else if (v0 == 232)
        {
            v2 = v9 + 60 - *((int *)&(v7->padding_24)[1]) - 4;
            if (!VirtualProtectEx(v8, *((int *)&(v7->padding_24)[1]), 0x4, PAGE_EXECUTE_READWRITE, &v1))
                return;
            WriteProcessMemory(v8, *((int *)&(v7->padding_24)[1]), &v2, 0x4, &v3);
            VirtualProtectEx(v8, *((int *)&(v7->padding_24)[1]), 0x4, v1, &v3);
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
```

## `sub_0041c166` `0x0041c166`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41c166(void)
{
    sub_41c168();
    return;
}
```

## `sub_0041c168` `0x0041c168`

_1121 bytes. (leaf/helper — see body)_

```c
extern char g_41eda8;

int sub_41c168(void)
{
    int v25;  // edx
    int v26;  // edi
    unsigned int v35;  // ecx
    char v37;  // al
    unsigned int v38;  // esi
    int v39;  // eax
    int v40;  // eax
    int v41;  // eax
    unsigned int index;  // ebx
    int v43;  // eax
    int v44;  // eax
    int v27;  // esi
    unsigned int v45;  // edx
    int v46;  // eax
    unsigned int ch;  // eax
    unsigned int idx;  // eax
    int v50;  // eax
    unsigned int v51;  // ebx
    unsigned long v52;  // 4118
    int v28;  // ebx
    unsigned long v29;  // ldt
    unsigned long v30;  // gdt
    unsigned short v31;  // fs
    unsigned long v32;  // 4125
    unsigned int v33;  // 4103
    unsigned long v34;  // 4134
    int v0;  // [bp-0x254]
    char *v1;  // [bp-0x248]
    unsigned int v2;  // [bp-0x240]
    unsigned int v3;  // [bp-0x230]
    char v4;  // [bp-0x218]
    char v5;  // [bp-0x1d8]
    int iter;  // [bp-0x4c]
    unsigned int v7;  // [bp-0x48]
    char v8;  // [bp-0x41]
    unsigned int *v9;  // [bp-0x40]
    unsigned int count;  // [bp-0x3c]
    unsigned int v11;  // [bp-0x38]
    unsigned int v12;  // [bp-0x34]
    char v13;  // [bp-0x2d]
    char v14;  // [bp-0x2c]
    char v15;  // [bp-0x26]
    char v16;  // [bp-0x25]
    HANDLE v17;  // [bp-0x24], Other Possible Types: enum WIN32_ERROR, unsigned int
    unsigned int v18;  // [bp-0x20]
    unsigned int v19;  // [bp-0x1c]
    unsigned int v20;  // [bp-0x18]
    char v21;  // [bp-0x11]
    int v22;  // [bp-0xc]
    char v23;  // [bp-0x4]

    v20 = 0;
    v19 = 0;
    v18 = 0;
    v12 = 0;
    v11 = 0;
    v22 = v25;
    sub_40402c(v26, v27, v28);
    sub_40402c(v26, v27, v28);
    v32 = _ccall(v29, v30, (unsigned int)v31, 0);
    v33 = *((int *)v32);
    v3 = *((int *)v32);
    v34 = _ccall(v29, v30, (unsigned int)v31, 0);
    *((unsigned int **)v34) = &v3;
    sub_404814(v33, sub_41c60e, &v23);
    sub_404814(v33, sub_41c60e, &v23);
    v21 = 0;
    count = 0;
    if ((char)sub_419d94())
    {
        sub_410d28();
        if (((v35 | 8) & 4294967279) == 4294967277 || ((v35 | 8) & 4294967279) == 4294967276 || ((v35 | 8) & 4294967279) == 4294967275)
        {
            if (!(GetVersion() & 0x80000000))
            {
                v17 = sub_40e7a8();
                if (!v17)
                {
                    SetLastError(ERROR_ACCESS_DENIED);
                    v52 = _ccall(v29, v30, (unsigned int)v31, 0);
                    *((char **)v52) = v1;
                    v2 = sub_41c615;
                    sub_41c5c9();
                    return;
                }
                CloseHandle(v17);
            }
            v38 = (v35 | 8) & 4294967279;
            if (v38 != 4294967275 || (GetCurrentProcess(), !(char)sub_410f9c()))
                v9 = NULL;
            if (v38 != 4294967276)
                v22 = -1;
            v39 = v22;
            v40 = _INSERT(v39, 0, ((char)v35 & 16));
            v1 = &v13;
            v21 = sub_419634(&v13, &v14, v40, v39, (!v9 ? NULL : *(v9)));
            if (v9)
                LocalFree(v9);
            if ((!(GetVersion() & 0x80000000) & v13) && !(char)sub_41bac8())
                v13 = 0;
            if (!g_41eda8)
            {
                v8 = 0;
                v7 = 0;
                do
                {
                    if (v8)
                        Sleep(10);
                    v8 = 0;
                    v15 = 1;
                    sub_40e47c();
                    v0 = sub_40464c();
                    sub_404808();
                    v41 = sub_404654();
                    if (v41 >= 0)
                    {
                        iter = v41 + 1;
                        index = 0;
                        do
                        {
                            *((unsigned int *)(v18 + index * 4)) = 0;
                            v16 = sub_41a46c();
                            v43 = sub_404654();
                            if (v43 >= 0)
                            {
                                v44 = v43 + 1;
                                v45 = 0;
                                do
                                {
                                    v46 = v44;
                                    if (*((int *)(v19 + v45 * 16)) == *((int *)(v20 + index * 16)))
                                    {
                                        v16 = 0;
                                        break;
                                    }
                                } while ((v45 += 1, v44 = (int)(v46 - 1), v46 != 1));
                            }
                            if (v16)
                            {
                                ch = GetCurrentProcessId();
                                if (ch != *((int *)(v20 + index * 16)) || ((char)v35 & 8))
                                {
                                    v15 = 0;
                                    v17 = OpenProcess(1146, 0, *((int *)(v20 + index * 16)));
                                    if (v17)
                                    {
                                        if (!(char)sub_417928())
                                        {
                                            if (v13 && !(GetVersion() & 0x80000000))
                                                sub_41c00c(&v4, &v5);
                                            if ((((v35 | 8) & 4294967279) != 4294967275 || (char)sub_4179ec()) && (((char)v35 & 16) || !(char)sub_417814()) && (((v35 | 8) & 4294967279) != 4294967276 || sub_417980() == v22 || !sub_417980() && (char)sub_417814()))
                                                sub_41af6c(&v23);
                                        }
                                        CloseHandle(v17);
                                    }
                                    else
                                    {
                                        v17 = GetLastError();
                                        idx = index * 2;
                                        if (*((int *)(v20 + idx * 8)) && v17 != 5)
                                        {
                                            *((unsigned int *)(v20 + idx * 8)) = 0;
                                            v8 = 1;
                                        }
                                    }
                                }
                            }
                            index += 1;
                            iter -= 1;
                        } while (iter != 1);
                    }
                    if (!count)
                        count = GetTickCount();
                    v50 = sub_404654();
                    if (v50 >= 0)
                    {
                        iter = v50 + 1;
                        v51 = 0;
                        do
                        {
                            if (*((int *)(v18 + v51 * 4)))
                                sub_41a3f8();
                        } while ((v51 += 1, iter = (int)(iter - 1), iter = iter, iter != 1));
                    }
                    sub_404850();
                    v7 += 1;
                } while (!v15 && v7 != 5);
            }
        }
        else
        {
            sub_40fb64(v35);
            if (!(char)sub_41af6c(&v23, &v11) || v17 && !((GetTickCount(), (char)sub_41a3f8())))
                v37 = 0;
            else
                v37 = 1;
            v21 = v37;
        }
    }
    v52 = _ccall(v29, v30, (unsigned int)v31, 0);
    *((char **)v52) = v1;
    v2 = sub_41c615;
    sub_41c5c9();
    return;
}
```

## `sub_0041c5c9` `0x0041c5c9`

_69 bytes. (leaf/helper — see body)_

```c
int sub_41c5c9(void)
{
    sub_404124();
    sub_403a34();
    sub_404814();
    return sub_404124();
}
```

## `sub_0041c60e` `0x0041c60e`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_41c60e(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041c613` `0x0041c613`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41c613(void)
{
    return sub_41c5c9();
}
```

## `sub_0041c615` `0x0041c615`

_12 bytes. (leaf/helper — see body)_

```c
char sub_41c615(unsigned int a0, unsigned int a1)
{
    char v0;  // [bp+0xffff7]

    return v0;
}
```

## `sub_0041c621` `0x0041c621`

_3 bytes. (leaf/helper — see body)_

```c
int sub_41c621(void)
{
    sub_41c624();
    return;
}
```

