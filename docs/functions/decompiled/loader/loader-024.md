# elfbot.dll decompiled — loader 0x00415e79..0x00416ede

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_00415e79` `0x00415e79`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_415e79(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00415e7e` `0x00415e7e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_415e7e(void)
{
    return sub_415e52();
}
```

## `sub_00415e80` `0x00415e80`

_7 bytes. (leaf/helper — see body)_

```c
void sub_415e80(unsigned int a0, unsigned int a1)
{
    return;
}
```

## `sub_00415e93` `0x00415e93`

_1332 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    char field_4;
    char padding_5[3];
    unsigned int field_8;
    char padding_c[8];
    struct struct_1 *field_14;
    unsigned int field_18;
    unsigned int field_1c;
    UIntPtr field_20;
    char padding_24[4];
    unsigned int field_28;
    char field_2c;
    char field_2d;
    char padding_2e[7];
    char field_35;
} struct_0;

typedef struct struct_2 {
    unsigned int field_0;
    char padding_4[4];
    HANDLE field_8;
    void* field_c;
    unsigned int field_10;
    unsigned short field_14;
    char padding_16[14];
    unsigned int field_24;
} struct_2;

typedef struct struct_3 {
    unsigned int field_0;
    char padding_4[4];
    unsigned int field_8;
    void* field_c;
    unsigned int field_10;
    unsigned short field_14;
    char padding_16[14];
    unsigned int field_24;
} struct_3;

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

typedef struct MEMORY_BASIC_INFORMATION {
    void* BaseAddress;
    void* AllocationBase;
    enum PAGE_PROTECTION_FLAGS AllocationProtect;
    UIntPtr RegionSize;
    enum VIRTUAL_ALLOCATION_TYPE State;
    enum PAGE_PROTECTION_FLAGS Protect;
    enum PAGE_TYPE Type;
} MEMORY_BASIC_INFORMATION;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

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

extern unsigned int g_4161c3;
extern unsigned int g_4161e1;

int sub_415e93(void)
{
    char v36;  // dl
    unsigned int i;  // ecx
    unsigned long v46;  // 4135
    unsigned int v47;  // 4105
    unsigned long v48;  // 4144
    unsigned long v49;  // 4128
    unsigned long v50;  // 4137
    unsigned long v51;  // 4127
    unsigned int v52;  // 4103
    unsigned long v53;  // 4136
    unsigned int v54;  // eax
    unsigned long v55;  // 4134
    unsigned int v38;  // ecx
    unsigned long v56;  // 4143
    unsigned long v57;  // 4158
    unsigned int v58;  // 4103
    unsigned long v59;  // 4162
    struct_3 *index;  // edi
    int v61;  // esi
    int v62;  // esi
    int v64;  // ebx
    int v65;  // eax
    int v39;  // edi
    unsigned int j;  // eax
    void* v68;  // eax
    struct_2 **v69;  // eax
    unsigned long v70;  // 4118
    unsigned long v71;  // 4118
    unsigned long v72;  // 4118
    unsigned int v73;  // edi
    unsigned long v74;  // 4123
    unsigned int v75;  // 4103
    int v40;  // esi
    unsigned long v76;  // 4132
    int v77;  // esi
    int v78;  // esi
    unsigned int v79;  // ebx
    int v80;  // esi
    unsigned int v82;  // ebx
    unsigned long v83;  // 4118
    unsigned long v84;  // 4118
    int v41;  // ebx
    struct_0 *v42;  // eax
    unsigned long v43;  // ldt
    unsigned long v44;  // gdt
    unsigned short v45;  // fs
    unsigned int v0;  // [bp-0x70]
    unsigned int v1;  // [bp-0x6c]
    unsigned int v2;  // [bp-0x68]
    unsigned int v3;  // [bp-0x64]
    unsigned int v4;  // [bp-0x60]
    unsigned int v5;  // [bp-0x5c]
    unsigned int v6;  // [bp-0x50]
    unsigned int v7;  // [bp-0x4c]
    unsigned int v8;  // [bp-0x40]
    unsigned int v9;  // [bp-0x3c]
    unsigned int v10;  // [bp-0x38]
    unsigned int v11;  // [bp-0x30]
    unsigned int v12;  // [bp-0x24]
    unsigned int v13;  // [bp-0x8]
    unsigned int v14;  // [bp-0x4]
    unsigned int v16;  // [bp+0xffeac]
    int v17;  // [bp+0xffee0]
    int v18;  // [bp+0xffee8]
    CONTEXT v19;  // [bp+0xffef0]
    char v20;  // [bp+0xfff8f]
    unsigned int v21;  // [bp+0xfffa8]
    MEMORY_BASIC_INFORMATION v22;  // [bp+0xfffbc]
    unsigned int v23;  // [bp+0xfffd8]
    struct_3 *v24;  // [bp+0xfffdc], Other Possible Types: unsigned int
    void* v25;  // [bp+0xfffe0], Other Possible Types: unsigned int
    char v26;  // [bp+0xfffe6]
    char v27;  // [bp+0xfffe7]
    int v28;  // [bp+0xfffe8]
    unsigned int v29;  // [bp+0xfffec]
    struct_2 **v30;  // [bp+0xffff0]
    unsigned int v31;  // [bp+0xffff4]
    unsigned int v32;  // [bp+0xffff8]
    char v33;  // [bp+0xfffff]
    struct_0 *idx;  // [bp+0x100000]

    v20 += v36;
    i = 44;
    do
    {
        v14 = 0;
        v13 = 0;
        i -= 1;
    } while (i != 1);
    v42 = sub_402fac(v39, v40, v41, v38);
    v33 = v36;
    idx = v42;
    v46 = _ccall(v43, v44, (unsigned int)v45, 0);
    v47 = *((int *)v46);
    v12 = *((int *)v46);
    v48 = _ccall(v43, v44, (unsigned int)v45, 0);
    *((unsigned int **)v48) = &v12;
    idx->field_2c = 1;
    sub_404814(v47, sub_416489, /* unsupported instruction */);
    if (idx->field_4)
    {
        v25 = NULL;
        v24 = 0;
        if (idx->padding_c[0] && !idx->padding_24[0])
        {
            GetCurrentProcessId();
            sub_413798();
        }
        sub_4115d0(/* unsupported instruction */ - 24);
        sub_409eac(/* unsupported instruction */ - 24);
        sub_403d40(v29, ", ", v18);
        v32 = sub_411214(sub_403e78(v29, ", ", v18));
        if (v32)
        {
            v10 = /* unsupported instruction */;
            v9 = sub_416216;
            v49 = _ccall(v43, v44, (unsigned int)v45, 0);
            v8 = *((int *)v49);
            v50 = _ccall(v43, v44, (unsigned int)v45, 0);
            *((unsigned int **)v50) = &v8;
            WaitForSingleObject(v32, 4294967295);
            v51 = _ccall(v43, v44, (unsigned int)v45, 0);
            v52 = *((int *)v51);
            v7 = *((int *)v51);
            v53 = _ccall(v43, v44, (unsigned int)v45, 0);
            *((unsigned int **)v53) = &v7;
            sub_409eac(-1, v52, sub_4161f8, /* unsupported instruction */);
            sub_403d40(v29, ", ", v17);
            v54 = sub_403e78(v29, ", ", v17);
            v31 = sub_4114f0(v54, v29);
            if (!v31)
            {
                v72 = _ccall(v43, v44, (unsigned int)v45, 0);
                *((char **)v72) = ", ";
                v6 = sub_4161ff;
                sub_4161ee();
                return;
            }
            v5 = /* unsupported instruction */;
            v4 = sub_4161da;
            v55 = _ccall(v43, v44, (unsigned int)v45, 0);
            v3 = *((int *)v55);
            v56 = _ccall(v43, v44, (unsigned int)v45, 0);
            *((unsigned int **)v56) = &v3;
            *((struct MEMORY_MAPPED_VIEW_ADDRESS *)&v30) = MapViewOfFile(v31, FILE_MAP_ALL_ACCESS, 0, 0, NULL);
            if (!v30)
            {
                v71 = _ccall(v43, v44, (unsigned int)v45, 0);
                *((unsigned int *)v71) = v3;
                v5 = &g_4161e1;
                sub_4161d0();
                return;
            }
            v2 = /* unsupported instruction */;
            v1 = sub_4161bc;
            v57 = _ccall(v43, v44, (unsigned int)v45, 0);
            v58 = *((int *)v57);
            v0 = *((int *)v57);
            v59 = _ccall(v43, v44, (unsigned int)v45, 0);
            *((unsigned int **)v59) = &v0;
            index = *(v30);
            v61 = index->field_0 - 2;
            if (v61 > 0)
            {
                v28 = 1;
                do
                {
                    v62 = v61;
                    if ((idx->padding_c[0] && !idx->padding_24[0] && *((int *)&index->padding_16[6 + 8 * v28]) == idx->field_1c || (!idx->padding_c[0] || idx->padding_24[0]) && *((int *)&index->padding_16[6 + 8 * v28]) == *((int *)&idx->padding_c[4])) && *((int *)&index->padding_16[10 + 8 * v28]) == *((int *)((char *)idx->field_20 + 2)))
                    {
                        v64 = v28;
                        v65 = index->field_0 - 2;
                        if (v65 >= v64)
                        {
                            j = v65 - v64 + 1;
                            do
                            {
                                *((unsigned int *)&index->padding_16[6 + 8 * v64]) = (&index->field_24)[2 * v64];
                                *((unsigned int *)&index->padding_16[10 + 8 * v64]) = (&index[1].field_0)[2 * v64];
                                v64 += 1;
                                j -= 1;
                            } while (j != 1);
                        }
                        *((int *)*((int *)&index->padding_16[2 + 8 * v28])) = *((int *)&index->padding_16[6 + 8 * v28]);
                        index->field_0 = index->field_0 - 1;
                        if (index->field_0 == 2 && index->field_8)
                        {
                            if (!IsBadReadPtr(index->field_c, 0x6) && *((char *)index->field_c) == index->padding_16[0] && (char)index->field_c[1] == index->padding_16[1] && (int)index->field_c[2] == *((int *)&index->padding_16[2]))
                            {
                                v27 = sub_40eb40();
                                if ((char)sub_40ec20())
                                {
                                    if (!(char)sub_410f64())
                                    {
                                        v68 = index->field_c;
                                        *((unsigned int *)v68) = index->field_10;
                                        *((unsigned short *)&v68[4]) = index->field_14;
                                    }
                                    sub_415658();
                                    if (v27)
                                        sub_40ecb0();
                                    v25 = index->field_24;
                                }
                            }
                            v69 = v30;
                            v24 = *(v69);
                            *(v69) = NULL;
                            CloseHandle(index->field_8);
                            break;
                        }
                    }
                } while ((v28 = (int)(v28 + 1), v61 = (int)(v62 - 1), v62 != 1));
            }
            v70 = _ccall(v43, v44, (unsigned int)v45, 0);
            *((unsigned int *)v70) = v58;
            v2 = &g_4161c3;
            sub_4161b2();
            return;
        }
        else
        {
            if (idx->field_14)
                idx->field_14->field_0 = idx->field_8;
            if (idx->field_28)
            {
                if (!idx->field_35 && !(GetVersion() & 0x80000000))
                {
                    sub_41541c();
                    sub_40d8e0();
                    v73 = v16 + 3920;
                }
                else
                {
                    v73 = 0;
                }
                v10 = /* unsupported instruction */;
                v74 = _ccall(v43, v44, (unsigned int)v45, 0);
                v75 = *((int *)v74);
                v8 = *((int *)v74);
                v76 = _ccall(v43, v44, (unsigned int)v45, 0);
                *((unsigned int **)v76) = &v8;
                v27 = 0;
                while (true)
                {
                    v26 = 1;
                    v77 = sub_404654();
                    if (v77 >= 0)
                    {
                        v78 = v77 + 1;
                        v79 = 0;
                        do
                        {
                            v80 = v78;
                            v19 = 65537;
                            if (GetThreadContext(*((int *)(v23 + v79 * 4)), /* unsupported instruction */ - 276) && idx->field_28 <= v21 && idx->field_28 + v73 > v21)
                            {
                                v26 = 0;
                                break;
                            }
                        } while ((v79 += 1, v78 = (int)(v80 - 1), v80 != 1));
                    }
                    v82 = 0;
                    do
                    {
                        if (*((int *)(idx->field_28 + v82 * 14 + 1)))
                        {
                            v26 = 0;
                            break;
                        }
                    } while ((v82 += 1, v82 != 280));
                    if (v26)
                    {
                        v83 = _ccall(v43, v44, (unsigned int)v45, 0);
                        *((unsigned int *)v83) = v75;
                        v10 = sub_41636a;
                        sub_416341();
                        return;
                    }
                    v27 = 1;
                    if (idx->field_2d)
                    {
                        sub_40351c(v75, sub_416363);
                        v10 = /* unsupported instruction */;
                        v84 = _ccall(v43, v44, (unsigned int)v45, 0);
                        *((unsigned int *)v84) = v10;
                        v11 = sub_416490;
                        sub_416451();
                        return;
                    }
                    Sleep(500);
                }
            }
            else
            {
                if (v25)
                {
                    if ((GetVersion() & 0x80000000) || VirtualQuery(v25, /* unsupported instruction */ - 72, 0x1c) != 0x1c || v22.BaseAddress != 64)
                        LocalFree(v25);
                    else
                        sub_4053fc(v25, 0, 0x8000);
                }
                if (v24)
                {
                    if (idx->padding_c[0])
                        sub_40ea58(v24, NULL);
                    else
                        sub_4053fc(v24, 0, 0x8000);
                }
                if (idx->field_1c)
                {
                    sub_40ea58(idx->field_1c, NULL);
                    idx->field_1c = 0;
                }
                if (idx->field_18)
                {
                    sub_40ea58(idx->field_18, NULL);
                    idx->field_18 = 0;
                }
            }
        }
    }
    v10 = 0x8000;
    sub_4053fc(idx->field_20, 0, 0x8000);
    idx->field_28 = 0;
    idx->field_20 = NULL;
    v84 = _ccall(v43, v44, (unsigned int)v45, 0);
    *((unsigned int *)v84) = v10;
    v11 = sub_416490;
    sub_416451();
    return;
}
```

## `sub_004161b2` `0x004161b2`

_10 bytes. (leaf/helper — see body)_

```c
int sub_4161b2(void)
{
    void* v1;  // [bp+0xffff0]

    return UnmapViewOfFile(v1);
}
```

## `sub_004161bc` `0x004161bc`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4161bc(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004161c1` `0x004161c1`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4161c1(void)
{
    return sub_4161b2();
}
```

## `sub_004161d0` `0x004161d0`

_10 bytes. (leaf/helper — see body)_

```c
int sub_4161d0(void)
{
    HANDLE v1;  // [bp+0xffff4]

    return CloseHandle(v1);
}
```

## `sub_004161da` `0x004161da`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4161da(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004161df` `0x004161df`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4161df(void)
{
    return sub_4161d0();
}
```

## `sub_004161ee` `0x004161ee`

_10 bytes. (leaf/helper — see body)_

```c
int sub_4161ee(void)
{
    HANDLE v1;  // [bp+0xffff8]

    return ReleaseMutex(v1);
}
```

## `sub_004161f8` `0x004161f8`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4161f8(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004161fd` `0x004161fd`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4161fd(void)
{
    return sub_4161ee();
}
```

## `sub_004161ff` `0x004161ff`

_13 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_41621d;

int sub_4161ff(unsigned int a0, unsigned int a1)
{
    unsigned long v1;  // ldt
    unsigned long v2;  // gdt
    unsigned short v3;  // fs
    unsigned long v4;  // 4118
    unsigned int v0;  // [bp+0x0]

    v4 = _ccall(v1, v2, (unsigned int)v3, 0);
    *((unsigned int *)v4) = v0;
    a1 = &g_41621d;
    return sub_41620c();
}
```

## `sub_0041620c` `0x0041620c`

_10 bytes. (leaf/helper — see body)_

```c
int sub_41620c(void)
{
    HANDLE v1;  // [bp+0xffff8]

    return CloseHandle(v1);
}
```

## `sub_00416216` `0x00416216`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_416216(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041621b` `0x0041621b`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41621b(void)
{
    return sub_41620c();
}
```

## `sub_00416341` `0x00416341`

_34 bytes. (leaf/helper — see body)_

```c
int sub_416341(void)
{
    int v2;  // esi
    int v3;  // esi
    unsigned int v4;  // ebx
    int i;  // esi
    int v6;  // eax
    int v7;  // esi
    unsigned int v1;  // [bp+0xfffd8]

    v2 = sub_404654();
    if (v2 < 0)
        return v2;
    v3 = v2 + 1;
    v4 = 0;
    do
    {
        i = v3;
        v6 = CloseHandle(*((int *)(v1 + v4 * 4)));
        v4 += 1;
        v7 = i - 1;
        v3 = v7;
    } while (i != 1);
    return v6;
}
```

## `sub_00416363` `0x00416363`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_416363(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00416368` `0x00416368`

_2 bytes. (leaf/helper — see body)_

```c
int sub_416368(void)
{
    return sub_416341();
}
```

## `sub_0041636a` `0x0041636a`

_16 bytes. (leaf/helper — see body)_

```c
void sub_41636a(void)
{
    char v1;  // [bp+0xfffe7]

    if (!v1)
        goto LABEL_0x41637a;
    Sleep(500);
}
```

## `sub_00416451` `0x00416451`

_56 bytes. (leaf/helper — see body)_

```c
int sub_416451(void)
{
    sub_4040f0();
    sub_403a34();
    sub_404814();
    return sub_403a10();
}
```

## `sub_00416489` `0x00416489`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_416489(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041648e` `0x0041648e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41648e(void)
{
    return sub_416451();
}
```

## `sub_00416490` `0x00416490`

_21 bytes. (leaf/helper — see body)_

```c
int sub_416490(unsigned int a0, unsigned int a1)
{
    unsigned int v1;  // eax
    char v0;  // [bp+0xfffff]

    if (v0 > 0)
        v1 = sub_402f94();
    return v1;
}
```

## `sub_0041650c` `0x0041650c`

_92 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_41f114;

HMODULE sub_41650c(unsigned int a0)
{
    unsigned int v8;  // ecx
    unsigned int v9;  // ebx
    unsigned long v18;  // 4117
    HMODULE v19;  // eax
    unsigned int v10;  // esi
    unsigned int v11;  // edi
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    unsigned short v14;  // fs
    unsigned long v15;  // 4130
    unsigned long v16;  // 4139
    HMODULE v17;  // eax
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    char *v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    enum WIN32_ERROR v6;  // [bp-0x8], Other Possible Types: unsigned int
    char v7;  // [bp-0x4]

    v6 = v8;
    v5 = v9;
    v4 = v10;
    v3 = v11;
    v6 = GetLastError();
    v2 = &v7;
    v1 = sub_41653e;
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    v0 = *((int *)v15);
    v16 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v16) = &v0;
    v17 = sub_4052c4(a0);
    v18 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int *)v18) = v0;
    SetLastError(v6);
    v19 = g_41f114(a0);
    if (v17 != v19)
        sub_417388();
    return v19;
}
```

## `sub_0041653e` `0x0041653e`

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

unsigned int sub_41653e(int a0)
{
    struct_1 *v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x8]

    return sub_4030c0(v0, a0, v1);
}
```

## `sub_00416543` `0x00416543`

_7 bytes. (leaf/helper — see body)_

```c
void sub_416543(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int *a10)
{
    unsigned int v0;  // [bp+0x0]

    sub_4034ec(v0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10);
}
```

## `sub_00416574` `0x00416574`

_110 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_41f118;

HMODULE sub_416574(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v8;  // ecx
    unsigned int v9;  // ebx
    HMODULE v18;  // eax
    unsigned long v19;  // 4117
    HMODULE v20;  // ebx
    unsigned int v10;  // esi
    unsigned int v11;  // edi
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    unsigned short v14;  // fs
    unsigned long v15;  // 4130
    unsigned int v16;  // 4104
    unsigned long v17;  // 4139
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    char *v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    enum WIN32_ERROR v6;  // [bp-0x8], Other Possible Types: unsigned int
    char v7;  // [bp-0x4]

    v6 = v8;
    v5 = v9;
    v4 = v10;
    v3 = v11;
    v6 = GetLastError();
    v2 = &v7;
    v1 = sub_4165a6;
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    v16 = *((int *)v15);
    v0 = *((int *)v15);
    v17 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v17) = &v0;
    v18 = sub_4052c4(a0);
    v19 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int *)v19) = v16;
    SetLastError(v6);
    v20 = g_41f118(a0, a1, a2);
    if (!v20)
    {
        return v20;
    }
    else if (v18 != v20)
    {
        if (((char)a2 & 2))
            return v20;
        sub_417388();
        return v20;
    }
    else
    {
        return v20;
    }
}
```

## `sub_004165a6` `0x004165a6`

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

unsigned int sub_4165a6(int a0)
{
    struct_1 *v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x8]

    return sub_4030c0(v0, a0, v1);
}
```

## `sub_004165ab` `0x004165ab`

_7 bytes. (leaf/helper — see body)_

```c
void sub_4165ab(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int *a10)
{
    unsigned int v0;  // [bp+0x0]

    sub_4034ec(v0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10);
}
```

## `sub_004165ee` `0x004165ee`

_2 bytes. (leaf/helper — see body)_

```c
void sub_4165ee(void)
{
    sub_4165f0();
    return;
}
```

## `sub_004165f0` `0x004165f0`

_110 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_41f11c;

HMODULE sub_4165f0(PWSTR a0, unsigned int a1, unsigned int a2)
{
    unsigned int v8;  // ecx
    unsigned int v9;  // ebx
    HMODULE v18;  // eax
    unsigned long v19;  // 4117
    HMODULE v20;  // ebx
    unsigned int v10;  // esi
    unsigned int v11;  // edi
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    unsigned short v14;  // fs
    unsigned long v15;  // 4130
    unsigned int v16;  // 4104
    unsigned long v17;  // 4139
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    char *v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    enum WIN32_ERROR v6;  // [bp-0x8], Other Possible Types: unsigned int
    char v7;  // [bp-0x4]

    v6 = v8;
    v5 = v9;
    v4 = v10;
    v3 = v11;
    v6 = GetLastError();
    v2 = &v7;
    v1 = sub_416622;
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    v16 = *((int *)v15);
    v0 = *((int *)v15);
    v17 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v17) = &v0;
    v18 = GetModuleHandleW(a0);
    v19 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int *)v19) = v16;
    SetLastError(v6);
    v20 = g_41f11c(a0, a1, a2);
    if (!v20)
    {
        return v20;
    }
    else if (v18 != v20)
    {
        if (((char)a2 & 2))
            return v20;
        sub_417388();
        return v20;
    }
    else
    {
        return v20;
    }
}
```

## `sub_00416622` `0x00416622`

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

unsigned int sub_416622(int a0)
{
    struct_1 *v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x8]

    return sub_4030c0(v0, a0, v1);
}
```

## `sub_00416627` `0x00416627`

_7 bytes. (leaf/helper — see body)_

```c
void sub_416627(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int *a10)
{
    unsigned int v0;  // [bp+0x0]

    sub_4034ec(v0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10);
}
```

## `sub_0041666a` `0x0041666a`

_2 bytes. (leaf/helper — see body)_

```c
void sub_41666a(void)
{
    sub_41666c();
    return;
}
```

## `sub_0041666c` `0x0041666c`

_121 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    PWSTR field_4;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_41f120;

unsigned int sub_41666c(unsigned int a0, unsigned int a1, struct_0 *a2, unsigned int a3)
{
    unsigned int v8;  // ecx
    unsigned int v9;  // ebx
    HMODULE v18;  // eax
    unsigned long v19;  // 4117
    unsigned int v20;  // eax
    unsigned int v10;  // esi
    unsigned int v11;  // edi
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    unsigned short v14;  // fs
    unsigned long v15;  // 4131
    unsigned int v16;  // 4104
    unsigned long v17;  // 4140
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    char *v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    enum WIN32_ERROR v6;  // [bp-0x8], Other Possible Types: unsigned int
    char v7;  // [bp-0x4]

    v6 = v8;
    v5 = v9;
    v4 = v10;
    v3 = v11;
    v6 = GetLastError();
    v2 = &v7;
    v1 = sub_4166a1;
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    v16 = *((int *)v15);
    v0 = *((int *)v15);
    v17 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v17) = &v0;
    v18 = GetModuleHandleW(a2->field_4);
    v19 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int *)v19) = v16;
    SetLastError(v6);
    v20 = g_41f120(a0, a1, a2, a3);
    if (!*((int *)a3))
        return v20;
    if (v18 == *((int *)a3))
        return v20;
    sub_417388();
    return v20;
}
```

## `sub_004166a1` `0x004166a1`

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

unsigned int sub_4166a1(int a0)
{
    struct_1 *v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x8]

    return sub_4030c0(v0, a0, v1);
}
```

## `sub_004166a6` `0x004166a6`

_7 bytes. (leaf/helper — see body)_

```c
void sub_4166a6(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int *a10)
{
    unsigned int v0;  // [bp+0x0]

    sub_4034ec(v0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10);
}
```

## `sub_004166f1` `0x004166f1`

_3 bytes. (leaf/helper — see body)_

```c
int sub_4166f1(void)
{
    return sub_4166f4();
}
```

## `sub_004166f4` `0x004166f4`

_875 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
    struct struct_0 *field_8;
} struct_1;

typedef struct struct_0 {
    char field_0;
    char field_1;
    struct struct_0 *field_2;
    unsigned int field_6;
} struct_0;

extern int g_41f114;
extern int g_41f118;
extern int g_41f11c;
extern int g_41f120;
extern char g_41f124;
extern char g_41f128;
extern int g_41f12c;

int sub_4166f4(void)
{
    int v15;  // edi
    int v16;  // esi
    HANDLE v26;  // esi
    struct_1 *idx;  // edi
    unsigned int v28;  // ebx
    unsigned int v29;  // ebx
    unsigned int v30;  // edx
    unsigned int v31;  // ebx
    unsigned int v32[2];  // ecx
    int v33;  // eax
    int v34;  // eax
    int v17;  // ebx
    unsigned int v35;  // ebx
    int v36;  // eax
    int v37;  // eax
    unsigned int v38;  // esi
    unsigned int v39[2];  // eax
    unsigned long v41;  // 4118
    unsigned long v18;  // ldt
    unsigned long v19;  // gdt
    unsigned short v20;  // fs
    unsigned long v21;  // 4150
    unsigned int v22;  // 4103
    unsigned long v23;  // 4154
    unsigned int v0;  // [bp-0xa4]
    unsigned int v1;  // [bp-0x9c]
    unsigned int v2;  // [bp-0x88]
    unsigned int v3;  // [bp-0x84]
    unsigned int v4;  // [bp-0x7c]
    unsigned int v5;  // [bp-0x64]
    unsigned int v6;  // [bp-0x3c]
    char v7;  // [bp-0x19]
    int v8;  // [bp-0x18]
    unsigned int v9;  // [bp-0x14]
    unsigned int v10[2];  // [bp-0x10]
    struct_0 *index;  // [bp-0xc]
    char v12;  // [bp-0x5]
    char v13;  // [bp-0x4]

    v5 = 0;
    v10 = NULL;
    sub_40402c(v15, v16, v17, 0, 0);
    v21 = _ccall(v18, v19, (unsigned int)v20, 0);
    v22 = *((int *)v21);
    v4 = *((int *)v21);
    v23 = _ccall(v18, v19, (unsigned int)v20, 0);
    *((unsigned int **)v23) = &v4;
    if (!g_41f124)
    {
        if ((GetVersion() & 0x80000000))
        {
            sub_40d994(0);
            sub_41708c(0, &g_41f114, sub_41650c, sub_411978(0));
            sub_40d994(0);
            v0 = 0;
            sub_41708c(0, &g_41f118, sub_416574, sub_411978(0));
        }
        else
        {
            if (!g_41f128)
            {
                g_41f128 = 1;
                sub_409eac();
                GetCurrentProcessId();
                sub_409b54(&v5);
                sub_403ccc();
                v26 = CreateFileMappingA(0xffffffff, NULL, PAGE_READWRITE, 0, 12, sub_403e78());
                if (v26)
                {
                    v12 = GetLastError() != ERROR_ALREADY_EXISTS;
                    idx = (struct_1 *)MapViewOfFile(v26, FILE_MAP_ALL_ACCESS, 0, 0, NULL);
                    if (idx)
                    {
                        v28 = 50;
                        do
                        {
                            v29 = v28;
                            if (v12)
                                break;
                            v3 = idx->field_4;
                            v2 = idx->field_0;
                            v30 = v10[1];
                            if (v10[1] == idx->field_4)
                            {
                                v30 = v10[0];
                                v3 = idx->field_0;
                            }
                        } while (v30 != v3 && (Sleep(50), v31 = v29 - 1, v28 = v29 - 1, v29 != 1));
                        if (!v12)
                        {
                            v32 = v10;
                            if (idx->field_4 == v32[1])
                            {
                                if (idx->field_0 == v32[0])
                                    goto LABEL_4169de;
                                goto LABEL_416873;
                            }
                            else
                            {
                                if (idx->field_4 != v32[1])
                                    goto LABEL_416873;
LABEL_4169de:
                                g_41f12c = idx->field_8;
                                UnmapViewOfFile(idx);
                            }
                        }
                        else
                        {
LABEL_416873:
                            index = sub_4053f4(NULL, 10, PAGE_GRAPHICS_READONLY, 64);
                            v8 = sub_40da7c(&v5, v22, sub_416a83, &v13);
                            sub_40d994();
                            sub_40d8e0();
                            v33 = sub_404654();
                            if (v33 >= 0)
                            {
                                v34 = v33 + 1;
                                v35 = 0;
                                do
                                {
                                    v36 = v34;
                                    if (*((int *)(v6 + v35 * 28 + 12)) == v8 && *((int *)(v6 + v35 * 28 + 20)))
                                    {
                                        idx->field_8 = index;
                                        index->field_0 = 255;
                                        index->field_1 = 37;
                                        *((struct_0 **)&(&index->field_1)[1]) = (char *)&index->field_2 + 2;
                                        *((int *)((char *)&index->field_2 + 2)) = v8;
                                        v7 = sub_40eb40();
                                        if (!v7 || (char)sub_40ec20())
                                        {
                                            v38 = v35 * 7;
                                            v9 = &(&index->field_0)[-1 * *((int *)(v6 + v38 * 4 + 4)) + 5];
                                            if (!(char)sub_410f64())
                                                *((unsigned int *)*((int *)(v6 + v38 * 4 + 20))) = v9;
                                            if (v7)
                                                sub_40ecb0();
                                            g_41f12c = index;
                                            v26 = NULL;
                                            break;
                                        }
                                    }
                                } while ((v35 += 1, v37 = (int)(v36 - 1), v34 = (int)(v36 - 1), v36 != 1));
                            }
                            if (!g_41f12c)
                            {
                                UnmapViewOfFile(idx);
                                sub_4053fc(index, 0, 0x8000);
                            }
                            else
                            {
                                v39 = v10;
                                idx->field_0 = v39[0];
                                idx->field_4 = v39[1];
                            }
                        }
                    }
                    if (v26)
                        CloseHandle(v26);
                }
            }
            if (g_41f12c)
            {
                sub_41708c(0, &g_41f120, sub_41666c, g_41f12c, 0);
            }
            else
            {
                sub_40d994(0);
                sub_41708c(0, &g_41f11c, sub_4165f0, sub_411978(0));
            }
        }
        g_41f124 = 1;
    }
    v41 = _ccall(v18, v19, (unsigned int)v20, 0);
    *((unsigned int *)v41) = v0;
    v1 = sub_416a8a;
    return sub_416a5f();
}
```

## `sub_00416a5f` `0x00416a5f`

_36 bytes. (leaf/helper — see body)_

```c
int sub_416a5f(void)
{
    sub_403a34();
    sub_4040f0();
    return sub_403a10();
}
```

## `sub_00416a83` `0x00416a83`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_416a83(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00416a88` `0x00416a88`

_2 bytes. (leaf/helper — see body)_

```c
int sub_416a88(void)
{
    return sub_416a5f();
}
```

## `sub_00416a8a` `0x00416a8a`

_7 bytes. (leaf/helper — see body)_

```c
void sub_416a8a(unsigned int a0, unsigned int a1)
{
    return;
}
```

## `sub_00416a91` `0x00416a91`

_3 bytes. (leaf/helper — see body)_

```c
int sub_416a91(void)
{
    sub_416a94();
    return;
}
```

## `sub_00416a94` `0x00416a94`

_113 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_41f114;
extern unsigned int g_41f118;
extern unsigned int g_41f11c;
extern unsigned int g_41f120;
extern char g_41f124;

int sub_416a94(void)
{
    if (!g_41f124)
        return;
    if (g_41f114)
        sub_417208();
    if (g_41f118)
        sub_417208();
    if (g_41f11c)
        sub_417208();
    if (g_41f120)
        sub_417208();
    g_41f124 = 0;
    return;
}
```

## `sub_00416b05` `0x00416b05`

_673 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    char field_4;
} struct_0;

extern char g_41f110;
extern char g_41f124;
extern unsigned int g_420b10;
extern unsigned int g_420b28;

int sub_416b05(unsigned int a0)
{
    unsigned int v17;  // edx
    int v18;  // edi
    unsigned int v27;  // 4103
    unsigned long v28;  // 4154
    struct_0 *v29;  // ebx
    unsigned long v30;  // 4116
    unsigned long v31;  // 4118
    unsigned long v32;  // 4124
    unsigned int v33;  // 4103
    unsigned long v34;  // 4133
    unsigned int v35;  // eax
    char v36;  // al
    int v19;  // esi
    unsigned long v37;  // 4122
    int v20;  // ebx
    unsigned long v21;  // ldt
    unsigned long v22;  // gdt
    unsigned short v23;  // fs
    unsigned long v24;  // 4124
    unsigned long v25;  // 4133
    unsigned long v26;  // 4150
    int v0;  // [bp-0x6c]
    unsigned int v1;  // [bp-0x68], Other Possible Types: int
    unsigned int v2;  // [bp-0x60]
    int v3;  // [bp-0x5c]
    unsigned int v4;  // [bp-0x54]
    unsigned int v5;  // [bp-0x48]
    unsigned int v6;  // [bp-0x44]
    unsigned int v7;  // [bp-0x40]
    char v8;  // [bp-0x19]
    enum WIN32_ERROR idx;  // [bp-0x18], Other Possible Types: int
    char v10;  // [bp-0x11]
    unsigned int v11;  // [bp-0xc]
    int v12;  // [bp+0x4]
    int v13;  // [bp+0x8]
    int v14;  // [bp+0xc]
    int v15;  // [bp+0x10]
    int v16;  // [bp+0x14]

    v11 = v17;
    sub_403e68(v18, v19, v20, 0, 0, 0, 0, 0);
    sub_403e68(v18, v19, v20, 0, 0, 0, 0, 0);
    v7 = &/* unsupported instruction */;
    v6 = sub_416ecb;
    v24 = _ccall(v21, v22, (unsigned int)v23, 0);
    v5 = *((int *)v24);
    v25 = _ccall(v21, v22, (unsigned int)v23, 0);
    *((unsigned int **)v25) = &v5;
    v10 = 0;
    sub_410d28();
    SetLastError(DNS_ERROR_RCODE_NO_ERROR);
    sub_40ead4();
    if (v15)
    {
        v26 = _ccall(v21, v22, (unsigned int)v23, 0);
        v27 = *((int *)v26);
        v4 = *((int *)v26);
        v28 = _ccall(v21, v22, (unsigned int)v23, 0);
        *((unsigned int **)v28) = &v4;
        if (!v11)
        {
            sub_40a54c(v27, sub_416c05, &/* unsupported instruction */);
            v29 = sub_4143b0(v12, v13, v14, v15, v16);
            v3 = v15;
            v1 = v12;
        }
        else
        {
            v29 = sub_4143b0(v12, v13, v14, v15, v16);
            v3 = v15;
            v1 = v12;
        }
        if (!v29->field_4)
        {
            idx = GetLastError();
            sub_402e1c();
            SetLastError(idx);
            v29 = NULL;
            v11 = 0;
        }
        v30 = _ccall(v21, v22, (unsigned int)v23, 0);
        *((int *)v30) = v1;
    }
    else
    {
        v29 = NULL;
    }
    if (!v29 && (v15 || !a0))
    {
        if (v10)
            SetLastError(DNS_ERROR_RCODE_NO_ERROR);
        v31 = _ccall(v21, v22, (unsigned int)v23, 0);
        *((int *)v31) = v3;
        v4 = sub_416ed2;
        return sub_416ead();
    }
    v10 = 1;
    if (!g_41f110)
    {
        sub_40533c(&g_420b10);
        g_41f110 = 1;
    }
    sub_40520c(&g_420b10);
    v32 = _ccall(v21, v22, (unsigned int)v23, 0);
    v33 = *((int *)v32);
    v1 = *((int *)v32);
    v34 = _ccall(v21, v22, (unsigned int)v23, 0);
    *((unsigned int **)v34) = &v1;
    idx = sub_40464c(v33, sub_416d93, &/* unsupported instruction */);
    v0 = idx + 1;
    sub_404808();
    *((unsigned int *)(g_420b28 + idx * 40)) = v35;
    *((unsigned int *)(g_420b28 + idx * 40 + 4)) = v11;
    sub_403a64();
    sub_409ee0();
    sub_403a64();
    sub_403a64();
    *((int *)(g_420b28 + idx * 40 + 20)) = v15;
    *((struct_0 **)(g_420b28 + idx * 40 + 24)) = v29;
    *((int *)(g_420b28 + idx * 40 + 28)) = v13;
    *((int *)(g_420b28 + idx * 40 + 32)) = v14;
    *((int *)(g_420b28 + idx * 40 + 36)) = v12;
    if (!v35 || g_41f124)
        v36 = 0;
    else
        v36 = 1;
    v8 = v36;
    v37 = _ccall(v21, v22, (unsigned int)v23, 0);
    *((unsigned int *)v37) = v33;
    v2 = sub_416d9a;
    return sub_416d88();
}
```

## `sub_00416c05` `0x00416c05`

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

unsigned int sub_416c05(int a0)
{
    struct_1 *v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x8]

    return sub_4030c0(v0, a0, v1);
}
```

## `sub_00416c0a` `0x00416c0a`

_7 bytes. (leaf/helper — see body)_

```c
void sub_416c0a(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int *a10)
{
    unsigned int v0;  // [bp+0x0]

    sub_4034ec(v0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10);
}
```

## `sub_00416c11` `0x00416c11`

_2 bytes. (leaf/helper — see body)_

```c
void sub_416c11(void)
{
}
```

## `sub_00416d88` `0x00416d88`

_10 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420b10;

void sub_416d88(void)
{
    sub_40534c(&g_420b10);
}
```

## `sub_00416d93` `0x00416d93`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_416d93(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00416d98` `0x00416d98`

_2 bytes. (leaf/helper — see body)_

```c
void sub_416d98(void)
{
    sub_416d88();
    return;
}
```

## `sub_00416d9a` `0x00416d9a`

_249 bytes. (leaf/helper — see body)_

```c
extern char g_4192e0;
extern char g_41ed98;
extern unsigned int g_41f130;

int sub_416d9a(void)
{
    int v3;  // ebx
    int v4;  // ebx
    unsigned int v5;  // eax
    int v1;  // [bp+0xfffe0]
    char v2;  // [bp+0xfffef]

    if (!v2)
        goto LABEL_0x416e93;
    sub_4166f4();
    GetCurrentProcessId();
    sub_409b54(/* unsupported instruction */ - 36);
    sub_409eac(v1);
    sub_403ccc();
    if (g_41ed98)
    {
        v3 = sub_403c80();
        sub_403f60();
        *((char *)(sub_403ed0() + v3)) = 36;
        *((char *)(sub_403ed0() + v3 + 1)) = 109;
        *((char *)(sub_403ed0() + v3 + 2)) = 99;
        *((char *)(sub_403ed0() + v3 + 3)) = 104;
    }
    else
    {
        sub_409b54(/* unsupported instruction */ - 44);
        sub_403c88(/* unsupported instruction */ - 44);
    }
    v4 = sub_4113d8(sub_403e78(4), 4);
    if (!v4)
        goto LABEL_0x416e93;
    v5 = (unsigned int)MapViewOfFile(v4, FILE_MAP_ALL_ACCESS, 0, 0, NULL);
    if (!v5)
        CloseHandle(v4);
    *((char **)v5) = &g_4192e0;
    UnmapViewOfFile(v5);
    g_41f130 = v4;
}
```

## `sub_00416ead` `0x00416ead`

_13 bytes. (leaf/helper — see body)_

```c
int sub_416ead(void)
{
    sub_403a34();
}
```

## `sub_00416ecb` `0x00416ecb`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_416ecb(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00416ed0` `0x00416ed0`

_2 bytes. (leaf/helper — see body)_

```c
int sub_416ed0(void)
{
    return sub_416ead();
}
```

## `sub_00416ed2` `0x00416ed2`

_12 bytes. (leaf/helper — see body)_

```c
char sub_416ed2(unsigned int a0, unsigned int a1)
{
    char v0;  // [bp+0xffff7]

    return v0;
}
```

## `sub_00416ede` `0x00416ede`

_2 bytes. (leaf/helper — see body)_

```c
int sub_416ede(void)
{
    sub_416ee0();
    return;
}
```

