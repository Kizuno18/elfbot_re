# elfbot.dll decompiled — loader 0x004135b4..0x004143ad

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_004135b4` `0x004135b4`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4135b4(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004135b9` `0x004135b9`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4135b9(void)
{
    return sub_4135aa();
}
```

## `sub_004135bb` `0x004135bb`

_9 bytes. (leaf/helper — see body)_

```c
int sub_4135bb(unsigned int a0)
{
    HANDLE v0;  // [bp+0xffff4]

    CloseHandle(v0);
}
```

## `sub_004135d1` `0x004135d1`

_10 bytes. (leaf/helper — see body)_

```c
int sub_4135d1(void)
{
    HANDLE v1;  // [bp+0xffff8]

    return CloseHandle(v1);
}
```

## `sub_004135db` `0x004135db`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4135db(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004135e0` `0x004135e0`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4135e0(void)
{
    return sub_4135d1();
}
```

## `sub_004135ef` `0x004135ef`

_14 bytes. (leaf/helper — see body)_

```c
int sub_4135ef(void)
{
    return sub_403a34();
}
```

## `sub_004135fd` `0x004135fd`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4135fd(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00413602` `0x00413602`

_2 bytes. (leaf/helper — see body)_

```c
int sub_413602(void)
{
    return sub_4135ef();
}
```

## `sub_00413604` `0x00413604`

_7 bytes. (leaf/helper — see body)_

```c
void sub_413604(unsigned int a0, unsigned int a1)
{
    return;
}
```

## `sub_0041360b` `0x0041360b`

_1 bytes. (leaf/helper — see body)_

```c
void sub_41360b(void)
{
    sub_41360c();
    return;
}
```

## `sub_0041360c` `0x0041360c`

_339 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
} struct_0;

int sub_41360c(void)
{
    unsigned int v14;  // ecx
    unsigned int v15;  // edx
    int v24;  // esi
    int v25;  // ebx
    unsigned long v26;  // 4127
    unsigned int v27;  // 4103
    unsigned long v28;  // 4136
    unsigned int v29;  // edi
    enum WIN32_ERROR v30;  // eax
    struct_0 **v31;  // esi
    unsigned long v32;  // 4118
    unsigned long v33;  // 4118
    unsigned int v16;  // eax
    unsigned long v17;  // ldt
    unsigned long v18;  // gdt
    unsigned short v19;  // fs
    unsigned long v20;  // 4176
    unsigned int v21;  // 4124
    unsigned long v22;  // 4185
    int v23;  // edi
    struct_0 **v0;  // [bp-0x50]
    unsigned int v1;  // [bp-0x4c]
    unsigned int v2;  // [bp-0x48]
    unsigned int v3;  // [bp-0x40]
    unsigned int v4;  // [bp-0x38]
    unsigned int v5;  // [bp-0x24]
    unsigned int v6;  // [bp-0x1c]
    unsigned int v7;  // [bp-0x18]
    unsigned int v8;  // [bp-0x14]
    unsigned int v9;  // [bp-0x10]
    unsigned int v10;  // [bp-0xc]
    unsigned int v11[2];  // [bp-0x8]
    char v12;  // [bp-0x4]

    v5 = 0;
    v6 = 0;
    v8 = v14;
    v10 = v15;
    v9 = v16;
    v20 = _ccall(v17, v18, (unsigned int)v19, 0);
    v21 = *((int *)v20);
    v3 = *((int *)v20);
    v22 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((unsigned int **)v22) = &v3;
    sub_409eac(v21, sub_413787, &v12, v23, v24, v25, 0, 0, 0, 0);
    sub_409eac(&v6);
    sub_403c88();
    v7 = sub_411214(sub_403e78());
    if (!v7)
    {
        v33 = _ccall(v17, v18, (unsigned int)v19, 0);
        *((unsigned int *)v33) = v21;
        v4 = sub_41378e;
        return sub_413779();
    }
    WaitForSingleObject(v7, 4294967295);
    v26 = _ccall(v17, v18, (unsigned int)v19, 0);
    v27 = *((int *)v26);
    v1 = *((int *)v26);
    v28 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((unsigned int **)v28) = &v1;
    v0 = 0x4;
    sub_409eac(4, v27, sub_41375c, &v12);
    sub_409eac(&v5);
    sub_403c88();
    v29 = sub_4113d8(sub_403e78(), 4);
    if (v29)
    {
        v30 = GetLastError();
        v0 = NULL;
        v31 = (struct_0 **)MapViewOfFile(v29, FILE_MAP_ALL_ACCESS, 0, 0, NULL);
        if (v31)
        {
            if (v30 != ERROR_ALREADY_EXISTS)
            {
                v11 = sub_40e970(8, NULL);
                v11[0] = 0;
                v11[1] = 0;
                *(v31) = v11;
                sub_40e878(v27, sub_41375c);
            }
            else
            {
                v11 = *(v31);
            }
            sub_4130b0(&v12);
            sub_412f9c(&v12);
            UnmapViewOfFile(v31);
            v0 = v31;
        }
        CloseHandle(v29);
    }
    v32 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((struct_0 ***)v32) = v0;
    v2 = sub_413763;
    return sub_413752();
}
```

## `sub_00413752` `0x00413752`

_10 bytes. (leaf/helper — see body)_

```c
int sub_413752(void)
{
    HANDLE v1;  // [bp+0xffff0]

    return ReleaseMutex(v1);
}
```

## `sub_0041375c` `0x0041375c`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_41375c(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00413761` `0x00413761`

_2 bytes. (leaf/helper — see body)_

```c
int sub_413761(void)
{
    return sub_413752();
}
```

## `sub_00413763` `0x00413763`

_9 bytes. (leaf/helper — see body)_

```c
int sub_413763(unsigned int a0)
{
    HANDLE v0;  // [bp+0xffff0]

    CloseHandle(v0);
}
```

## `sub_00413779` `0x00413779`

_14 bytes. (leaf/helper — see body)_

```c
int sub_413779(void)
{
    return sub_403a34();
}
```

## `sub_00413787` `0x00413787`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_413787(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041378c` `0x0041378c`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41378c(void)
{
    return sub_413779();
}
```

## `sub_0041378e` `0x0041378e`

_9 bytes. (leaf/helper — see body)_

```c
void sub_41378e(unsigned int a0, unsigned int a1)
{
    return;
}
```

## `sub_00413797` `0x00413797`

_1 bytes. (leaf/helper — see body)_

```c
void sub_413797(void)
{
    sub_413798();
    return;
}
```

## `sub_00413798` `0x00413798`

_501 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_41f028;

int sub_413798(void)
{
    unsigned long v17;  // ldt
    unsigned long v18;  // gdt
    unsigned int v27;  // 4103
    unsigned long v28;  // 4136
    unsigned int v29;  // eax
    unsigned int idx;  // ebx
    char v31;  // dl
    int v32;  // esi
    int v33;  // esi
    unsigned int idx1;  // eax
    int v35;  // esi
    unsigned int v36[3];  // edi
    unsigned short v19;  // fs
    unsigned int v37;  // edx
    unsigned int v38;  // eax
    unsigned int v39;  // ecx
    int v40;  // esi
    unsigned long v41;  // 4118
    unsigned long v42;  // 4118
    unsigned long v20;  // 4176
    unsigned int v21;  // 4124
    unsigned long v22;  // 4185
    int v23;  // edi
    int v24;  // esi
    int v25;  // ebx
    unsigned long v26;  // 4127
    struct_0 **v0;  // [bp-0x6c]
    unsigned int v1;  // [bp-0x64]
    unsigned int v2;  // [bp-0x60]
    unsigned int v3;  // [bp-0x54]
    unsigned int v4;  // [bp-0x4c]
    unsigned int v5;  // [bp-0x38]
    unsigned int v6;  // [bp-0x30]
    unsigned int v7;  // [bp-0x2c]
    unsigned int i;  // [bp-0x2c]
    unsigned int *index;  // [bp-0x28]
    unsigned int v10;  // [bp-0x24]
    char v11;  // [bp-0x1d]
    struct_0 **v12;  // [bp-0x1c]
    unsigned int v13;  // [bp-0x18]
    unsigned int v14;  // [bp-0x14]
    char v15;  // [bp-0x4]

    v5 = 0;
    v6 = 0;
    v20 = _ccall(v17, v18, (unsigned int)v19, 0);
    v21 = *((int *)v20);
    v3 = *((int *)v20);
    v22 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((unsigned int **)v22) = &v3;
    sub_409eac(v21, sub_4139b5, &v15, v23, v24, v25, 0, 0, 0, 0);
    sub_409eac(&v6);
    sub_403c88();
    v14 = sub_411300(sub_403e78());
    if (!v14)
    {
        v42 = _ccall(v17, v18, (unsigned int)v19, 0);
        *((unsigned int *)v42) = v21;
        v4 = sub_4139bc;
        sub_4139a7();
        return;
    }
    WaitForSingleObject(v14, 4294967295);
    v26 = _ccall(v17, v18, (unsigned int)v19, 0);
    v27 = *((int *)v26);
    v2 = *((int *)v26);
    v28 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((unsigned int **)v28) = &v2;
    sub_409eac(-1, v27, sub_41398a, &v15);
    sub_409eac(&v5);
    sub_403c88();
    v13 = sub_4114f0(sub_403e78(), 4294967295);
    if (v13)
    {
        v0 = NULL;
        v12 = (struct_0 **)MapViewOfFile(v13, FILE_MAP_ALL_ACCESS, 0, 0, NULL);
        if (v12)
        {
            index = &*(v12)->field_0;
            v11 = 1;
            v29 = *(index) - 1;
            if (v29 >= 0)
            {
                v7 = v29 + 1;
                v10 = 0;
                do
                {
                    i = v7;
                    idx = index[1] + v10 * 24;
                    v31 = 1;
                    v32 = *((int *)(idx + 16)) - 1;
                    if (v32 >= 0)
                    {
                        v33 = v32 + 1;
                        idx1 = 0;
                        do
                        {
                            v35 = v33;
                            v36 = *((int *)(idx + 20)) + idx1 * 12;
                            if (*((int *)idx) == v37 && v36[0] == v38 && v36[2] == v39)
                            {
                                *((unsigned int *)(*((int *)(idx + 20)) + idx1 * 12)) = 0;
                            }
                            else if (*((int *)(*((int *)(idx + 20)) + idx1 * 12)))
                            {
                                v31 = 0;
                            }
                        } while ((idx1 += 1, v40 = (int)(v35 - 1), v33 = (int)(v35 - 1), v35 != 1));
                    }
                    if (v31)
                    {
                        if (*((int *)(idx + 20)))
                            g_41f028(*((int *)(idx + 20)));
                        *((unsigned int *)(idx + 16)) = 0;
                        *((unsigned int *)(idx + 20)) = 0;
                    }
                    else if (*((int *)(idx + 16)) > 0)
                    {
                        v11 = 0;
                    }
                    v10 += 1;
                    v7 = i - 1;
                } while (i != 1);
            }
            if (v11)
            {
                if (index[1])
                    g_41f028(index[1]);
                *(index) = 0;
                index[1] = 0;
            }
            UnmapViewOfFile(v12);
            v0 = v12;
        }
        CloseHandle(v13);
    }
    v41 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((struct_0 ***)v41) = v0;
    v1 = sub_413991;
    sub_413980();
    return;
}
```

## `sub_00413980` `0x00413980`

_10 bytes. (leaf/helper — see body)_

```c
int sub_413980(void)
{
    HANDLE v1;  // [bp+0xffff4]

    return ReleaseMutex(v1);
}
```

## `sub_0041398a` `0x0041398a`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_41398a(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041398f` `0x0041398f`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41398f(void)
{
    return sub_413980();
}
```

## `sub_00413991` `0x00413991`

_9 bytes. (leaf/helper — see body)_

```c
int sub_413991(unsigned int a0)
{
    HANDLE v0;  // [bp+0xffff4]

    CloseHandle(v0);
}
```

## `sub_004139a7` `0x004139a7`

_14 bytes. (leaf/helper — see body)_

```c
int sub_4139a7(void)
{
    return sub_403a34();
}
```

## `sub_004139b5` `0x004139b5`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4139b5(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004139ba` `0x004139ba`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4139ba(void)
{
    return sub_4139a7();
}
```

## `sub_004139bc` `0x004139bc`

_7 bytes. (leaf/helper — see body)_

```c
void sub_4139bc(unsigned int a0, unsigned int a1)
{
    return;
}
```

## `sub_00413a19` `0x00413a19`

_52 bytes. (leaf/helper — see body)_

```c
void sub_413a19(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v0;  // edi
    unsigned int v1;  // ecx
    unsigned int v2;  // ecx
    unsigned int v3;  // ecx

    v0 = 0x11111111;
    v1 = 280;
    do
    {
        v2 = v1;
        if (!InterlockedCompareExchange(v0 + 1, a3, 0))
        {
            a3 = v0;
            break;
        }
    } while ((v0 += 14, v3 = v2 - 1, v1 = v2 - 1, v2 != 1));
}
```

## `sub_00413a4d` `0x00413a4d`

_1 bytes. (leaf/helper — see body)_

```c
void sub_413a4d(void)
{
    return;
}
```

## `sub_00413a78` `0x00413a78`

_892 bytes. refs ";
            sub_403d40(v14, "_

```c
typedef struct struct_0 {
    char padding_0[20];
    int field_14;
} struct_0;

int sub_413a78(void)
{
    unsigned int i;  // ecx
    unsigned int v18;  // ecx
    unsigned int v27;  // 4103
    unsigned long v28;  // 4134
    HMODULE v29;  // eax
    unsigned int *v30;  // edx
    unsigned int v31;  // ebx
    unsigned int v32;  // ebx
    unsigned int v33;  // ebx
    unsigned int v34;  // ecx
    struct_0 *idx;  // eax
    unsigned int v36;  // esi
    int v19;  // eax
    unsigned int v37;  // esi
    unsigned int j;  // esi
    unsigned int v39;  // esi
    int v40;  // esi
    int v41;  // esi
    unsigned int v42;  // ebx
    int k;  // esi
    unsigned int v44;  // eax
    int v45;  // eax
    int v46;  // eax
    int v20;  // edi
    int v47;  // esi
    int v48;  // esi
    int v49;  // esi
    unsigned int v50;  // ebx
    int v51;  // esi
    int v52;  // esi
    unsigned long v53;  // 4118
    int v21;  // esi
    int v22;  // ebx
    unsigned long v23;  // ldt
    unsigned long v24;  // gdt
    unsigned short v25;  // fs
    unsigned long v26;  // 4125
    unsigned int v0;  // [bp-0x40]
    int iter;  // [bp-0x3c]
    int v2;  // [bp-0x38]
    int v3;  // [bp-0x38]
    struct_0 *v4;  // [bp-0x34], Other Possible Types: unsigned int
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    char v7;  // [bp-0x25]
    HANDLE v8;  // [bp-0x24]
    char v9;  // [bp-0x1d]
    unsigned int index;  // [bp-0x18]
    unsigned int v11;  // [bp-0x14]
    unsigned int v12;  // [bp-0x10]
    char v13;  // [bp-0x9]
    int v14;  // [bp-0x8]
    char v15;  // [bp-0x4]
    void* v16;  // [bp+0x4]

    i = 15;
    do
    {
        v12 = 0;
        v11 = 0;
        i -= 1;
    } while (i != 1);
    v14 = v19;
    sub_403e68(v20, v21, v22, v18);
    v26 = _ccall(v23, v24, (unsigned int)v25, 0);
    v27 = *((int *)v26);
    v5 = *((int *)v26);
    v28 = _ccall(v23, v24, (unsigned int)v25, 0);
    *((unsigned int **)v28) = &v5;
    v13 = 0;
    v29 = sub_4052c4(sub_403e78(v27, sub_413e29, &v15));
    if (v29 == (int)v16[4])
    {
        iter = iter;
        if (!*(v30))
        {
            sub_409eac();
            v3 = ".";
            sub_403d40(v14, ".", *((int *)v26));
            v8 = CreateFileMappingA(0xffffffff, NULL, PAGE_READWRITE, 0, 16, sub_403e78(v14, ".", *((int *)v26)));
            iter = v14;
            if (CreateFileMappingA(0xffffffff, NULL, PAGE_READWRITE, 0, 16, sub_403e78(iter, ".", *((int *)v26))))
            {
                v7 = GetLastError() != ERROR_ALREADY_EXISTS;
                v6 = (unsigned int)MapViewOfFile(CreateFileMappingA(0xffffffff, NULL, PAGE_READWRITE, 0, 16, sub_403e78(v14, ".", *((int *)v26))), FILE_MAP_ALL_ACCESS, 0, 0, NULL);
                iter = v14;
                if (MapViewOfFile(CreateFileMappingA(0xffffffff, NULL, PAGE_READWRITE, 0, 16, sub_403e78(iter, ".", *((int *)v26))), FILE_MAP_ALL_ACCESS, 0, 0, NULL))
                {
                    v31 = 50;
                    do
                    {
                        v32 = v31;
                    } while (!v7 && (*((int *)(MapViewOfFile(CreateFileMappingA(0xffffffff, NULL, PAGE_READWRITE, 0, 16, sub_403e78(v14, ".", *((int *)v26))), FILE_MAP_ALL_ACCESS, 0, 0, NULL) + PAGE_READWRITE)) != *((int *)(v27 + PAGE_READWRITE)) || *((int *)MapViewOfFile(CreateFileMappingA(0xffffffff, NULL, PAGE_READWRITE, 0, 16, sub_403e78(v14, ".", *((int *)v26))), FILE_MAP_ALL_ACCESS, 0, 0, NULL)) != *((int *)v27)) && (Sleep(50), v33 = v32 - 1, v31 = v32 - 1, v32 != 1));
                    if (!v7)
                    {
                        v34 = v27;
                        if (*((int *)(MapViewOfFile(CreateFileMappingA(0xffffffff, NULL, PAGE_READWRITE, 0, 16, sub_403e78(v14, ".", *((int *)v26))), FILE_MAP_ALL_ACCESS, 0, 0, NULL) + PAGE_READWRITE)) == *((int *)(v34 + PAGE_READWRITE)))
                        {
                            if (*((int *)MapViewOfFile(CreateFileMappingA(0xffffffff, NULL, PAGE_READWRITE, 0, 16, sub_403e78(v14, ".", *((int *)v26))), FILE_MAP_ALL_ACCESS, 0, 0, NULL)) == *((int *)v34))
                                goto LABEL_413d78;
                            goto LABEL_413b8d;
                        }
                        else
                        {
                            if (*((int *)(MapViewOfFile(CreateFileMappingA(0xffffffff, NULL, PAGE_READWRITE, 0, 16, sub_403e78(v14, ".", *((int *)v26))), FILE_MAP_ALL_ACCESS, 0, 0, NULL) + PAGE_READWRITE)) != *((int *)(v34 + PAGE_READWRITE)))
                                goto LABEL_413b8d;
LABEL_413d78:
                            iter = v14;
                            if (*((int *)(MapViewOfFile(CreateFileMappingA(0xffffffff, NULL, PAGE_READWRITE, 0, 16, sub_403e78(iter, ".", *((int *)v26))), FILE_MAP_ALL_ACCESS, 0, 0, NULL) + 8)) > 0)
                            {
                                v0 = *((int *)(MapViewOfFile(CreateFileMappingA(0xffffffff, NULL, PAGE_READWRITE, 0, 16, sub_403e78(v14, ".", *((int *)v26))), FILE_MAP_ALL_ACCESS, 0, 0, NULL) + 8));
                                sub_404808();
                                sub_402628();
                                iter = v14;
                            }
                        }
                    }
                    else
                    {
LABEL_413b8d:
                        index = 0;
                        idx = (unsigned int)sub_40a6ec();
                        iter = v14;
                        if (idx)
                        {
                            v4 = idx;
                            v0 = idx->field_14;
                            sub_404808();
                            v0 = idx->field_14;
                            sub_404808();
                            v36 = idx->field_14 - 1;
                            if (v36 >= 0)
                            {
                                v37 = v36 + 1;
                                do
                                {
                                    j = v37;
                                    sub_40d8e0();
                                    sub_40421c();
                                    v39 = j - 1;
                                    v37 = v39;
                                } while (j != 1);
                            }
                            v40 = sub_404654();
                            iter = v14;
                            if (v40 >= 0)
                            {
                                v41 = v40 + 1;
                                v42 = 0;
                                iter = v14;
                                do
                                {
                                    k = v41;
                                    v44 = v42 * 8;
                                    if (*((char *)(v22 + v44 * 8)) && *((char *)(v22 + v44 * 8 + 40)))
                                    {
                                        v9 = 0;
                                        v45 = sub_404654();
                                        if (v45 >= 0)
                                        {
                                            v3 = v45 + 1;
                                            v12 = 0;
                                            do
                                            {
                                                if (v42 == v12)
                                                    continue;
                                                v46 = sub_404654();
                                                if (v46 >= 0)
                                                {
                                                    iter = v46 + 1;
                                                    v11 = 0;
                                                    do
                                                    {
                                                        if (*((int *)(*((int *)(v22 + v12 * 64 + 28)) + v11 * 48)) > *((int *)(v22 + v42 * 64 + 4)) && *((int *)(*((int *)(v22 + v12 * 64 + 28)) + v11 * 48)) < *((int *)(v22 + v42 * 64 + 4)) + 6)
                                                        {
                                                            *((int *)(*(v30) + index * 4)) = *((int *)(v22 + v42 * 64 + 4));
                                                            index += 1;
                                                            break;
                                                        }
                                                    } while ((v11 += 1, iter = (int)(iter - 1), iter = iter, iter != 1));
                                                }
                                                if (v9)
                                                    break;
                                            } while ((v12 += 1, v2 = (int)(v3 - 1), v3 = v2, v3 != 1));
                                        }
                                    }
                                    v42 += 1;
                                    v47 = k - 1;
                                    v41 = v47;
                                } while (k != 1);
                            }
                        }
                        v0 = index;
                        sub_404808();
                        *((unsigned int *)(MapViewOfFile(CreateFileMappingA(0xffffffff, NULL, PAGE_READWRITE, 0, 16, sub_403e78(v14, ".", *((int *)v26))), FILE_MAP_ALL_ACCESS, 0, 0, NULL) + 8)) = index;
                        *((unsigned int *)(MapViewOfFile(CreateFileMappingA(0xffffffff, NULL, PAGE_READWRITE, 0, 16, sub_403e78(v14, ".", *((int *)v26))), FILE_MAP_ALL_ACCESS, 0, 0, NULL) + 12)) = sub_40e970(index * PAGE_READWRITE, NULL);
                        sub_402628(iter, v3);
                        sub_410f64();
                        sub_40e878();
                        iter = iter;
                    }
                    UnmapViewOfFile(MapViewOfFile(CreateFileMappingA(0xffffffff, NULL, PAGE_READWRITE, 0, 16, sub_403e78(v14, ".", *((int *)v26))), FILE_MAP_ALL_ACCESS, 0, 0, NULL));
                }
                CloseHandle(CreateFileMappingA(0xffffffff, NULL, PAGE_READWRITE, 0, 16, sub_403e78(v14, ".", *((int *)v26))));
            }
        }
        v48 = sub_404654();
        if (v48 >= 0)
        {
            v49 = v48 + 1;
            v50 = 0;
            do
            {
                v51 = v49;
                if (*((int *)(*(v30) + v50 * 4)) == (int)v16[8])
                {
                    v13 = 1;
                    break;
                }
            } while ((v50 += 1, v52 = (int)(v51 - 1), v49 = (int)(v51 - 1), v51 != 1));
        }
    }
    v53 = _ccall(v23, v24, (unsigned int)v25, 0);
    *((int *)v53) = iter;
    v4 = sub_413e30;
    sub_413df4();
    return;
}
```

## `sub_00413df4` `0x00413df4`

_53 bytes. (leaf/helper — see body)_

```c
int sub_413df4(void)
{
    sub_4040f0();
    sub_403a10();
    sub_403a10();
    sub_404814();
    return sub_403a10();
}
```

## `sub_00413e29` `0x00413e29`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_413e29(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00413e2e` `0x00413e2e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_413e2e(void)
{
    return sub_413df4();
}
```

## `sub_00413e30` `0x00413e30`

_10 bytes. (leaf/helper — see body)_

```c
char sub_413e30(unsigned int a0, unsigned int a1)
{
    char v0;  // [bp+0xfffff]

    return v0;
}
```

## `sub_00413e48` `0x00413e48`

_164 bytes. (leaf/helper — see body)_

```c
int sub_413e48(void)
{
    unsigned int v11;  // ebx
    unsigned int v12;  // edx
    unsigned int v13;  // eax
    unsigned long v14;  // ldt
    unsigned long v15;  // gdt
    unsigned short v16;  // fs
    unsigned long v17;  // 4163
    unsigned long v18;  // 4172
    unsigned long v19;  // 4118
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    char *v2;  // [bp-0x20], Other Possible Types: unsigned int
    unsigned int v3;  // [bp-0x1c]
    unsigned int v4;  // [bp-0x18]
    unsigned int v5;  // [bp-0x14]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]
    char v9;  // [bp-0x4]

    v8 = 0;
    v7 = 0;
    v6 = 0;
    v5 = 0;
    v4 = 0;
    v3 = v11;
    v7 = v12;
    v8 = v13;
    v2 = &v9;
    v1 = sub_413efa;
    v17 = _ccall(v14, v15, (unsigned int)v16, 0);
    v0 = *((int *)v17);
    v18 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int **)v18) = &v0;
    v19 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int *)v19) = v0;
    v2 = sub_413f01;
    sub_413eec();
    return;
}
```

## `sub_00413eec` `0x00413eec`

_14 bytes. (leaf/helper — see body)_

```c
int sub_413eec(void)
{
    return sub_403a34();
}
```

## `sub_00413efa` `0x00413efa`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_413efa(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00413eff` `0x00413eff`

_2 bytes. (leaf/helper — see body)_

```c
int sub_413eff(void)
{
    return sub_413eec();
}
```

## `sub_00413f01` `0x00413f01`

_7 bytes. (leaf/helper — see body)_

```c
int sub_413f01(void)
{
    unsigned int v1;  // ebx

    return v1;
}
```

## `sub_00413f08` `0x00413f08`

_361 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    int field_14;
    char padding_18[4];
    unsigned int field_1c;
} struct_0;

typedef struct struct_1 {
    unsigned short field_0;
    struct struct_2 *field_2;
} struct_1;

typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

int sub_413f08(void)
{
    int v15;  // edi
    int v16;  // esi
    struct_0 *v25;  // eax
    struct_0 *v26;  // esi
    unsigned int v27;  // eax
    int v28;  // eax
    unsigned int v29;  // edx
    int v30;  // eax
    unsigned int v31;  // ecx
    unsigned int v32;  // eax
    char i[4];  // esi
    char iter[4];  // edi
    int v17;  // ebx
    unsigned int v35;  // ecx
    char j[4];  // esi
    char node[4];  // edi
    unsigned int v38;  // ecx
    unsigned long v39;  // 4152
    unsigned long v40;  // 4156
    unsigned int v41;  // eax
    char v42;  // al
    unsigned long v43;  // 4120
    unsigned long v44;  // 4118
    unsigned long v18;  // ldt
    unsigned long v19;  // gdt
    unsigned short v20;  // fs
    unsigned long v21;  // 4124
    unsigned long v22;  // 4133
    unsigned int v23;  // eax
    unsigned int v24;  // edx
    unsigned int v0;  // [bp-0x84]
    unsigned int v1;  // [bp-0x80]
    char *v2;  // [bp-0x7c]
    unsigned int v3;  // [bp-0x78]
    unsigned int v4;  // [bp-0x74]
    char *v5;  // [bp-0x70], Other Possible Types: unsigned int
    char v6;  // [bp-0x60]
    unsigned int v7;  // [bp-0x3c]
    unsigned int v8;  // [bp-0x38]
    char v9;  // [bp-0x32]
    struct_1 *v10;  // [bp-0x30]
    int v11;  // [bp-0x14]
    char v12;  // [bp-0xd]
    char v13;  // [bp-0x4]

    v7 = 0;
    sub_403e68(v15, v16, v17);
    v5 = &v13;
    v4 = sub_41408c;
    v21 = _ccall(v18, v19, (unsigned int)v20, 0);
    v3 = *((int *)v21);
    v22 = _ccall(v18, v19, (unsigned int)v20, 0);
    *((unsigned int **)v22) = &v3;
    v12 = 0;
    if ((GetVersion() & 0x80000000) && v23 && v24 && (v23 == sub_40d900() || (sub_409eac(), v23 == sub_4052c4(sub_403e78()))))
    {
        v25 = (unsigned int)sub_40a6ec();
        if (v25)
        {
            v26 = v25;
            v11 = 0;
            v27 = v26->field_14 - 1;
            if (v27 >= 0)
            {
                v28 = v27 + 1;
                v29 = 0;
                do
                {
                    v30 = v28;
                    if (*((int *)(v26->field_1c + v23 + v29 * 4)) + v23 == v31 && (v11 = (int)(v11 + 1), v11 > 3))
                    {
                        v12 = 1;
                        break;
                    }
                } while ((v29 += 1, v32 = v30 - 1, v28 = (int)(v30 - 1), v30 != 1));
            }
        }
        if (!v12)
        {
            sub_40c63c();
            sub_40c63c();
            i = &v6;
            iter = &v8;
            for (v35 = 9; v35; i += 1)
            {
                v35 -= 1;
                *(iter) = *(i);
                iter += 1;
            }
            if (*((unsigned short *)((void*)&v8 + 2)) == 177)
            {
                sub_40c63c();
                j = &v6;
                node = &v8;
                for (v38 = 9; v38; j += 1)
                {
                    v38 -= 1;
                    *(node) = *(j);
                    node += 1;
                }
                v2 = &v13;
                v1 = sub_414064;
                v39 = _ccall(v18, v19, (unsigned int)v20, 0);
                v0 = *((int *)v39);
                v40 = _ccall(v18, v19, (unsigned int)v20, 0);
                *((unsigned int **)v40) = &v0;
                if (v9 && v10 && v10->field_0 == 0x25ff)
                {
                    sub_40d900();
                    v41 = sub_40ab08();
                    if (v41 != *((int *)*((int *)&(&v10->field_0)[1])))
                        goto LABEL_414051;
                    v42 = 1;
                }
                else
                {
LABEL_414051:
                    v42 = 0;
                }
                v12 = v42;
                v43 = _ccall(v18, v19, (unsigned int)v20, 0);
                *((unsigned int *)v43) = v0;
            }
        }
    }
    v44 = _ccall(v18, v19, (unsigned int)v20, 0);
    *((unsigned int *)v44) = v3;
    v5 = sub_414093;
    sub_41407b();
    return;
}
```

## `sub_00414064` `0x00414064`

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

unsigned int sub_414064(int a0)
{
    struct_1 *v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x8]

    return sub_4030c0(v0, a0, v1);
}
```

## `sub_00414069` `0x00414069`

_5 bytes. (leaf/helper — see body)_

```c
void sub_414069(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int *a10)
{
    unsigned int v0;  // [bp+0x0]

    sub_4034ec(v0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10);
}
```

## `sub_0041407b` `0x0041407b`

_17 bytes. (leaf/helper — see body)_

```c
int sub_41407b(void)
{
    sub_403a10();
    return sub_403a10();
}
```

## `sub_0041408c` `0x0041408c`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_41408c(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00414091` `0x00414091`

_2 bytes. (leaf/helper — see body)_

```c
int sub_414091(void)
{
    return sub_41407b();
}
```

## `sub_00414093` `0x00414093`

_10 bytes. (leaf/helper — see body)_

```c
char sub_414093(unsigned int a0, unsigned int a1)
{
    char v0;  // [bp+0xffffb]

    return v0;
}
```

## `sub_0041409d` `0x0041409d`

_3 bytes. (leaf/helper — see body)_

```c
void sub_41409d(void)
{
    sub_4140a0();
    return;
}
```

## `sub_004140a0` `0x004140a0`

_121 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[6];
    unsigned short field_6;
    char padding_8[252];
    unsigned int field_104;
    unsigned int field_108;
} struct_0;

int sub_4140a0(void)
{
    unsigned int v2;  // ecx
    unsigned int v3;  // edx
    unsigned int v4;  // eax
    struct_0 *v5;  // edx
    struct_0 *v6;  // ebp
    unsigned int v7;  // edx
    unsigned int v8;  // edx
    unsigned int v9;  // edx
    unsigned int v0;  // [bp-0x14]

    v0 = v2;
    if (!(GetVersion() & 0x80000000))
    {
        return;
    }
    else if (v3 >= 0x80000000)
    {
        return;
    }
    else if (v4)
    {
        v5 = sub_40a658();
        if (!v5)
            return;
        v6 = &v5->padding_8[240];
        v7 = v5->field_6 - 1;
        if (v7 < 0)
            return;
        v8 = v7 + 1;
        while (true)
        {
            v9 = v8;
            if (*((int *)&v6->padding_8[4]) + v4 <= v3 && v3 < *((int *)&v6->padding_8[4]) + v4 + *((int *)&v6->padding_8[8]))
                return;
            v6 = &v6->padding_8[32];
            v8 = v9 - 1;
            if (v9 == 1)
                return;
        }
    }
    else
    {
        return;
    }
}
```

## `sub_00414119` `0x00414119`

_3 bytes. (leaf/helper — see body)_

```c
int sub_414119(void)
{
    sub_41411c();
    return;
}
```

## `sub_0041411c` `0x0041411c`

_80 bytes. (leaf/helper — see body)_

```c
int sub_41411c(void)
{
    unsigned int v3;  // ebx
    unsigned int v4;  // esi
    HANDLE *v5;  // eax
    unsigned int *v6;  // esi
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp-0x4]

    v1 = v3;
    v0 = v4;
    if (!*(v5))
        return;
    v6 = (unsigned int *)MapViewOfFile(*(v5), FILE_MAP_ALL_ACCESS, 0, 0, NULL);
    if (!v6)
    {
        CloseHandle(*(v5));
        *(v5) = NULL;
        return;
    }
    if (!*(v6))
    {
        CloseHandle(*(v5));
        *(v5) = NULL;
    }
    UnmapViewOfFile(v6);
    return;
}
```

## `sub_0041416c` `0x0041416c`

_184 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned short field_8;
} struct_0;

int sub_41416c(void)
{
    unsigned int v5[42];  // eax
    unsigned int v6;  // edx
    struct_0 *iter;  // ecx
    struct_0 *v8;  // edx
    struct_0 *node;  // eax
    unsigned int v10;  // edx
    unsigned int v11;  // edx
    unsigned int v12;  // edi
    unsigned int v13;  // ecx
    unsigned int v14;  // edx
    unsigned int idx[42];  // [bp-0x18]
    struct_0 *v1;  // [bp-0x14]
    char v2;  // [bp-0xd]
    unsigned int v3;  // [bp+0x4]
    unsigned int v4;  // [bp+0x8]

    v2 = 0;
    idx = &v5[6];
    iter = idx[0x22] + v6;
    v1 = idx[35] + (char *)iter;
    while (true)
    {
        v8 = iter;
        if (v8 >= v1)
        {
            return;
        }
        else if (iter->field_0)
        {
            node = &v8->field_8;
            v10 = iter->field_4 - 8 >> 1;
            if (v10 > 0)
            {
                do
                {
                    v11 = v10;
                    if (((short)node->field_0 & 0xf000) == 0x3000)
                    {
                        v12 = iter->field_0 + v6 + ((short)node->field_0 & 0xfff);
                        if (v13 <= v12 && v12 < v13 + v3)
                            *((unsigned int *)(v12 - v13 + v4)) = idx[7] + *((int *)(v12 - v13 + v4)) - v6;
                    }
                } while ((node += 2, v14 = v11 - 1, v10 = v11 - 1, v11 != 1));
            }
            iter = (char *)iter + iter->field_4;
        }
        else
        {
            return;
        }
    }
}
```

## `sub_00414224` `0x00414224`

_63 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[6];
    unsigned short field_6;
    char padding_8[36];
    unsigned int field_2c;
    unsigned int field_30;
    char padding_34[196];
    char field_f8;
    char field_f9;
    char field_fa;
} struct_0;

int sub_414224(void)
{
    struct_0 *v1;  // eax
    struct_0 *v2;  // ecx
    unsigned int v3;  // edx

    v2 = &v1->field_f8;
    if (*((int *)(v3 + 44)) != v1->field_2c)
    {
        return;
    }
    else if (*((int *)(v3 + 48)) != v1->field_30)
    {
        return;
    }
    else if (*((short *)(v3 + 6)) != v1->field_6)
    {
        return;
    }
    else if (v2->padding_0[0] != 0x55)
    {
        return;
    }
    else if (v2->padding_0[1] == 80)
    {
        return;
    }
    else
    {
        return;
    }
}
```

## `sub_00414263` `0x00414263`

_1 bytes. (leaf/helper — see body)_

```c
int sub_414263(void)
{
    sub_414264();
    return;
}
```

## `sub_00414264` `0x00414264`

_319 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned short field_4;
} struct_0;


int sub_414264(void)
{
    struct_0 *v11;  // eax
    int v12;  // edi
    unsigned long v21;  // 4133
    struct_0 *v22;  // eax
    char v23;  // al
    unsigned long v24;  // 4116
    int v13;  // esi
    int v14;  // ebx
    struct_0 *v15;  // edx
    unsigned long v16;  // ldt
    unsigned long v17;  // gdt
    unsigned short v18;  // fs
    unsigned long v19;  // 4124
    unsigned int v20;  // 4103
    unsigned int v0;  // [bp-0x44]
    unsigned int v1;  // [bp-0x3c]
    char v2;  // [bp-0x22]
    unsigned int v3;  // [bp-0x1e]
    unsigned short v4;  // [bp-0x1a]
    int v5;  // [bp-0x14]
    int v6;  // [bp-0x10]
    int v7;  // [bp-0xc]
    char v8;  // [bp-0x5]

    v8 = 0;
    if (!v11)
    {
        return;
    }
    else if (!sub_40a658(v12, v13, v14))
    {
        return;
    }
    else if (v11 >= v15)
    {
        return;
    }
    else if (sub_40a828() + (char *)v11 > v15)
    {
        v7 = sub_412278();
        if (!v7)
            return;
        v5 = sub_40a7c0();
        v6 = sub_40a658();
        if (!v6)
        {
            return;
        }
        else if (sub_40a828() > v5)
        {
            v19 = _ccall(v16, v17, (unsigned int)v18, 0);
            v20 = *((int *)v19);
            v1 = *((int *)v19);
            v21 = _ccall(v16, v17, (unsigned int)v18, 0);
            *((unsigned int **)v21) = &v1;
            v8 = 0;
            if (v8)
            {
                sub_402628();
                v0 = 10;
                sub_41416c(10, &v2);
                v22 = v7 + v5;
                if (v3 == v22->field_0 && v4 == v22->field_4)
                    v23 = 0;
                else
                    v23 = 1;
                v8 = v23;
            }
            v24 = _ccall(v16, v17, (unsigned int)v18, 0);
            *((unsigned int *)v24) = v0;
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

## `sub_00414399` `0x00414399`

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

unsigned int sub_414399(int a0)
{
    struct_1 *v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x8]

    return sub_4030c0(v0, a0, v1);
}
```

## `sub_0041439e` `0x0041439e`

_5 bytes. (leaf/helper — see body)_

```c
void sub_41439e(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int *a10)
{
    unsigned int v0;  // [bp+0x0]

    sub_4034ec(v0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10);
}
```

## `sub_004143ad` `0x004143ad`

_3 bytes. (leaf/helper — see body)_

```c
int sub_4143ad(void)
{
    return sub_4143b0();
}
```

