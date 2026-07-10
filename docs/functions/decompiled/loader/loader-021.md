# elfbot.dll decompiled — loader 0x004120a0..0x004135aa

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_004120a0` `0x004120a0`

_239 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420aec;

int sub_4120a0(void)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    void* v19;  // eax
    unsigned int v20;  // edi
    int v21;  // esi
    int v22;  // esi
    unsigned int v23;  // ebx
    int v24;  // esi
    unsigned int ch;  // eax
    int v26;  // esi
    int idx;  // edi
    unsigned int ch1;  // eax
    unsigned short v11;  // fs
    unsigned long v29;  // 4118
    unsigned long v12;  // 4159
    unsigned int v13;  // 4118
    unsigned long v14;  // 4168
    int v15;  // edi
    int v16;  // esi
    int v17;  // ebx
    char v18;  // dl
    int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x28]
    unsigned int v2;  // [bp-0x24]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]
    char v7;  // [bp+0x0]

    v5 = 0;
    v4 = 0;
    v3 = 0;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v13 = *((int *)v12);
    v1 = *((int *)v12);
    v14 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v14) = &v1;
    sub_409eac(v13, sub_41219d, &v6, v15, v16, v17, 0, 0, v18 * 0x1000000, &v7);
    GetCurrentProcessId();
    sub_409b54(&v3, &v4);
    sub_403c88();
    *((int *)v19) = sub_411214(sub_403e78());
    if (*((int *)v19))
        WaitForSingleObject(*((int *)v19), 4294967295);
    v20 = 4294967295;
    v21 = sub_404654();
    if (v21 >= 0)
    {
        v22 = v21 + 1;
        v23 = 0;
        do
        {
            v24 = v22;
            ch = GetCurrentThreadId();
            if (ch == *((int *)(g_420aec + v23 * 18)))
            {
                v20 = v23;
                break;
            }
        } while ((v23 += 1, v26 = (int)(v24 - 1), v22 = (int)(v24 - 1), v24 != 1));
    }
    if ((v20 == 4294967295 & *((char *)((void*)&v18 * 0x1000000 + 3))))
    {
        idx = sub_40464c();
        v0 = idx + 1;
        sub_404808();
        ch1 = GetCurrentThreadId();
        *((unsigned int *)(g_420aec + idx * 18)) = ch1;
    }
    v29 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v29) = &v4;
    v2 = sub_4121a4;
    sub_41218f();
    return;
}
```

## `sub_0041218f` `0x0041218f`

_14 bytes. (leaf/helper — see body)_

```c
int sub_41218f(void)
{
    return sub_403a34();
}
```

## `sub_0041219d` `0x0041219d`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_41219d(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004121a2` `0x004121a2`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4121a2(void)
{
    return sub_41218f();
}
```

## `sub_004121a4` `0x004121a4`

_9 bytes. (leaf/helper — see body)_

```c
int sub_4121a4(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // edi

    return v0;
}
```

## `sub_004121ad` `0x004121ad`

_3 bytes. (leaf/helper — see body)_

```c
int sub_4121ad(void)
{
    sub_4121b0();
    return;
}
```

## `sub_004121b0` `0x004121b0`

_21 bytes. (leaf/helper — see body)_

```c
int sub_4121b0(void)
{
    HANDLE v1;  // eax

    if (v1)
    {
        ReleaseMutex(v1);
        CloseHandle(v1);
    }
    return;
}
```

## `sub_004121c5` `0x004121c5`

_3 bytes. (leaf/helper — see body)_

```c
void sub_4121c5(void)
{
    sub_4121c8();
    return;
}
```

## `sub_004121c8` `0x004121c8`

_54 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420aec;

int sub_4121c8(void)
{
    int v6;  // ecx
    int v7;  // eax
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4143
    unsigned long v12;  // 4152
    unsigned long v13;  // 4178
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char *v2;  // [bp-0xc], Other Possible Types: unsigned int
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v7 = sub_4120a0(v6, &v4);
    v2 = &v3;
    v1 = sub_412207;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v0 = *((int *)v11);
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v0;
    *((unsigned int *)(g_420aec + v7 * 18 + 4)) = *((int *)(g_420aec + v7 * 18 + 4)) + 1;
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v13) = v0;
    v2 = sub_41220e;
    return sub_4121fe(v6, &v4);
}
```

## `sub_004121fe` `0x004121fe`

_9 bytes. (leaf/helper — see body)_

```c
int sub_4121fe(void)
{
    return sub_4121b0();
}
```

## `sub_00412207` `0x00412207`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_412207(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041220c` `0x0041220c`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41220c(void)
{
    return sub_4121fe();
}
```

## `sub_0041220e` `0x0041220e`

_3 bytes. (leaf/helper — see body)_

```c
void sub_41220e(unsigned int a0, unsigned int a1)
{
    return;
}
```

## `sub_00412211` `0x00412211`

_3 bytes. (leaf/helper — see body)_

```c
int sub_412211(void)
{
    sub_412214();
    return;
}
```

## `sub_00412214` `0x00412214`

_77 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420aec;

int sub_412214(void)
{
    int v6;  // ebx
    int v7;  // ecx
    unsigned long v16;  // 4192
    int v8;  // eax
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4148
    unsigned long v13;  // 4157
    unsigned int v14;  // edx
    char v15;  // al
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    char *v2;  // [bp-0x10], Other Possible Types: unsigned int
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v8 = sub_4120a0(v6, v7, &v4);
    v2 = &v3;
    v1 = sub_41226a;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v0 = *((int *)v12);
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v0;
    v14 = v8 * 9;
    *((char *)(g_420aec + v14 * 2 + 8)) = 1;
    *((char *)(g_420aec + v14 * 2 + 9)) = v15 | *((char *)(g_420aec + v14 * 2 + 9));
    v16 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v16) = v0;
    v2 = sub_412271;
    sub_412261(v6, v7, &v4);
    return;
}
```

## `sub_00412261` `0x00412261`

_9 bytes. (leaf/helper — see body)_

```c
int sub_412261(void)
{
    return sub_4121b0();
}
```

## `sub_0041226a` `0x0041226a`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_41226a(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041226f` `0x0041226f`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41226f(void)
{
    return sub_412261();
}
```

## `sub_00412271` `0x00412271`

_4 bytes. (leaf/helper — see body)_

```c
void sub_412271(unsigned int a0, unsigned int a1, unsigned int a2)
{
    return;
}
```

## `sub_00412275` `0x00412275`

_3 bytes. (leaf/helper — see body)_

```c
int sub_412275(void)
{
    sub_412278();
    return;
}
```

## `sub_00412278` `0x00412278`

_170 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420aec;

int sub_412278(void)
{
    int v9;  // eax
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // fs
    unsigned long v13;  // 4171
    unsigned long v14;  // 4175
    unsigned int v15;  // edx
    unsigned int v16;  // eax
    unsigned long v17;  // 4118
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    char *v2;  // [bp-0x20], Other Possible Types: unsigned int
    int v3;  // [bp-0x1c]
    int v4;  // [bp-0x18]
    unsigned int v5;  // [bp-0x14]
    unsigned int v6;  // [bp-0xc]
    char v7;  // [bp-0x4]

    v6 = 0;
    if (!g_420aec)
        return;
    v9 = sub_4120a0(v3, v4);
    if (v9 == -1)
        return;
    v5 = 0;
    v2 = &v7;
    v1 = sub_412322;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v0 = *((int *)v13);
    v14 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v14) = &v0;
    v15 = v9 * 9;
    if (*((int *)(g_420aec + v15 * 2 + 10)) == v16)
    {
        v6 = *((int *)(g_420aec + v15 * 2 + 14));
    }
    else if (*((int *)(g_420aec + v15 * 2 + 10)))
    {
        v5 = *((int *)(g_420aec + v15 * 2 + 14));
        *((unsigned int *)(g_420aec + v15 * 2 + 10)) = 0;
        *((unsigned int *)(g_420aec + v15 * 2 + 14)) = 0;
    }
    v17 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v17) = v0;
    v2 = sub_412329;
    sub_412319();
    return;
}
```

## `sub_00412319` `0x00412319`

_9 bytes. (leaf/helper — see body)_

```c
int sub_412319(void)
{
    return sub_4121b0();
}
```

## `sub_00412322` `0x00412322`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_412322(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00412327` `0x00412327`

_2 bytes. (leaf/helper — see body)_

```c
int sub_412327(void)
{
    return sub_412319();
}
```

## `sub_00412329` `0x00412329`

_117 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420aec;

int sub_412329(void)
{
    int v8;  // eax
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4145
    unsigned long v13;  // 4154
    unsigned int v14;  // edx
    unsigned long v15;  // 4189
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]
    unsigned int v2;  // [bp-0x4]
    unsigned int v4;  // [bp+0xffff4]
    unsigned int v5;  // [bp+0xffffc]
    unsigned int v6;  // [bp+0x100000]

    if (v4)
        UnmapViewOfFile(v4);
    if (v5)
        goto LABEL_0x4123b6;
    v4 = sub_40a83c();
    if (!v4)
        goto LABEL_0x4123b6;
    v8 = sub_4120a0();
    if (v8 != -1)
    {
        v2 = /* unsupported instruction */;
        v1 = sub_41239e;
        v12 = _ccall(v9, v10, (unsigned int)v11, 0);
        v0 = *((int *)v12);
        v13 = _ccall(v9, v10, (unsigned int)v11, 0);
        *((unsigned int **)v13) = &v0;
        v14 = v8 * 9;
        *((unsigned int *)(g_420aec + v14 * 2 + 10)) = v6;
        *((unsigned int *)(g_420aec + v14 * 2 + 14)) = v4;
        v15 = _ccall(v9, v10, (unsigned int)v11, 0);
        *((unsigned int *)v15) = v0;
        v2 = sub_4123a5;
        return sub_412395();
    }
    UnmapViewOfFile(v4);
}
```

## `sub_00412395` `0x00412395`

_9 bytes. (leaf/helper — see body)_

```c
int sub_412395(void)
{
    return sub_4121b0();
}
```

## `sub_0041239e` `0x0041239e`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_41239e(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004123a3` `0x004123a3`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4123a3(void)
{
    return sub_412395();
}
```

## `sub_004123a5` `0x004123a5`

_8 bytes. (leaf/helper — see body)_

```c
int sub_4123a5(void)
{
    unsigned int v1;  // [bp+0xffff4]
    unsigned int v2;  // [bp+0xffffc]

    v2 = v1;
}
```

## `sub_004123bf` `0x004123bf`

_1 bytes. (leaf/helper — see body)_

```c
void sub_4123bf(void)
{
    sub_4123c0();
    return;
}
```

## `sub_004123c0` `0x004123c0`

_232 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
    unsigned short field_10;
} struct_0;

extern unsigned int g_420aec;

int sub_4123c0(void)
{
    unsigned long v13;  // ldt
    unsigned long v14;  // gdt
    unsigned long v23;  // 4158
    unsigned int v24;  // ebx
    int v25;  // eax
    struct_0 *v26;  // esi
    struct_0 *v27;  // edi
    struct_0 *v28;  // edi
    struct_0 *v29;  // esi
    struct_0 *v30;  // edi
    struct_0 *v31;  // esi
    struct_0 *v32;  // edi
    unsigned short v15;  // fs
    struct_0 *v33;  // esi
    unsigned long v34;  // 4118
    unsigned long v16;  // 4164
    unsigned int v17;  // 4119
    unsigned long v18;  // 4173
    int v19;  // edi
    int v20;  // esi
    int v21;  // ebx
    unsigned long v22;  // 4154
    int v0;  // [bp-0x180]
    unsigned int v1;  // [bp-0x17c]
    unsigned int v2;  // [bp-0x178]
    char *v3;  // [bp-0x174], Other Possible Types: unsigned int
    unsigned int v4;  // [bp-0x170]
    unsigned int v5;  // [bp-0x30]
    int v6;  // [bp-0x28]
    unsigned int v7;  // [bp-0x24]
    unsigned int v8;  // [bp-0x1c]
    char v9;  // [bp-0xa]
    char v10;  // [bp-0x9]
    char v11;  // [bp-0x4]

    v7 = 0;
    v5 = 0;
    v16 = _ccall(v13, v14, (unsigned int)v15, 0);
    v17 = *((int *)v16);
    v4 = *((int *)v16);
    v18 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int **)v18) = &v4;
    v10 = 0;
    v9 = 0;
    v8 = 0;
    v6 = sub_4120a0(v17, sub_4127e0, &v11, v19, v20, v21);
    v3 = &v11;
    v2 = sub_4124b1;
    v22 = _ccall(v13, v14, (unsigned int)v15, 0);
    v1 = *((int *)v22);
    v23 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int **)v23) = &v1;
    if (v6 != -1)
    {
        v24 = v6 * 9;
        *((unsigned int *)(g_420aec + v24 * 2 + 4)) = *((int *)(g_420aec + v24 * 2 + 4)) - 1;
        if (!*((int *)(g_420aec + v24 * 2 + 4)))
        {
            v10 = *((char *)(g_420aec + v24 * 2 + 8));
            v9 = *((char *)(g_420aec + v24 * 2 + 9));
            v8 = *((int *)(g_420aec + v24 * 2 + 14));
            v25 = sub_404654();
            v26 = g_420aec + v25 * 18;
            v27 = g_420aec + v24 * 2;
            v27->field_0 = v26->field_0;
            v28 = &v27->field_4;
            v29 = &v26->field_4;
            v28->field_0 = v29->field_0;
            v30 = &v28->field_4;
            v31 = &v29->field_4;
            v30->field_0 = v31->field_0;
            v32 = &v30->field_4;
            v33 = &v31->field_4;
            v32->field_0 = v33->field_0;
            *((short *)&v32->field_4) = v33->field_4;
            v0 = sub_404654();
            sub_404808();
        }
    }
    v34 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int *)v34) = v1;
    v3 = sub_4124b8;
    return sub_4124a8();
}
```

## `sub_004124a8` `0x004124a8`

_9 bytes. (leaf/helper — see body)_

```c
int sub_4124a8(void)
{
    return sub_4121b0();
}
```

## `sub_004124b1` `0x004124b1`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4124b1(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004124b6` `0x004124b6`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4124b6(void)
{
    return sub_4124a8();
}
```

## `sub_004124b8` `0x004124b8`

_460 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    int field_8;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

typedef struct struct_2 {
    struct struct_1 *field_0;
} struct_2;

extern struct_2 *g_41f45c;

int sub_4124b8(unsigned int a0, unsigned int a1)
{
    HANDLE v15;  // esi
    char v16;  // bl
    unsigned int j;  // ebx
    unsigned long v26;  // ldt
    unsigned long v27;  // gdt
    unsigned short v28;  // fs
    unsigned long v29;  // 4118
    unsigned int v17;  // 4096
    unsigned int v18[2];  // ecx
    int v19;  // eax
    unsigned long v20;  // ldt
    unsigned long v21;  // gdt
    unsigned short v22;  // fs
    unsigned long v23;  // 4152
    unsigned long v24;  // 4156
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp+0x0]
    unsigned int v4;  // [bp+0xffeb0]
    unsigned int v5[2];  // [bp+0xfffd8]
    unsigned int v6;  // [bp+0xfffdc]
    int i;  // [bp+0xfffe0], Other Possible Types: unsigned int
    LPArray v8;  // [bp+0xfffe4]
    int v9;  // [bp+0xfffe8], Other Possible Types: unsigned int
    struct_0 *idx;  // [bp+0xfffec], Other Possible Types: unsigned int
    unsigned int v11;  // [bp+0xffff8]
    char v12;  // [bp+0xffffe]
    char v13;  // [bp+0xfffff]

    if (idx)
        UnmapViewOfFile(idx);
    if (v13)
    {
        v9 = 0;
        sub_409eac();
        v15 = CreateFileMappingA(0xffffffff, NULL, PAGE_READWRITE, 0, 12, sub_403e78());
        if (v15)
        {
            v16 = GetLastError() != ERROR_ALREADY_EXISTS;
            *((struct MEMORY_MAPPED_VIEW_ADDRESS *)&idx) = MapViewOfFile(v15, FILE_MAP_ALL_ACCESS, 0, 0, NULL);
            if (idx)
            {
                i = 50;
                do
                { } while (!v16 && (*((int *)&idx->padding_0[4]) != v5[1] || *((int *)&idx->padding_0[0]) != v5[0]) && (Sleep(50), v17 = i, i -= 1, v17 != 1));
                if (!v16)
                {
                    v18 = v5;
                    if (*((int *)&idx->padding_0[4]) == v18[1])
                    {
                        if (*((int *)&idx->padding_0[0]) == v18[0])
                            goto LABEL_4125a2;
                    }
                    else
                    {
                        if (*((int *)&idx->padding_0[4]) == v18[1])
                            goto LABEL_4125a2;
                    }
                }
                v19 = sub_40ecb8(0, 0);
                idx->field_8 = v19;
                sub_410f64(0, 0);
                sub_40e878();
LABEL_4125a2:
                v9 = idx->field_8;
                UnmapViewOfFile(idx);
            }
            CloseHandle(v15);
        }
        if (v9)
        {
            sub_40e278();
            i = 0;
            v11 = g_41f45c->field_0(2, 0);
            if (v11 != 4294967295)
            {
                v2 = /* unsupported instruction */;
                v1 = sub_412731;
                v23 = _ccall(v20, v21, (unsigned int)v22, 0);
                v0 = *((int *)v23);
                v24 = _ccall(v20, v21, (unsigned int)v22, 0);
                *((unsigned int **)v24) = &v0;
                if (v12)
                    v6 = 0;
                else
                    v6 = 500;
                v4 = 296;
                return sub_41261a();
            }
            else if (i > 0)
            {
                do
                {
                    if (i <= 32)
                    {
                        v2 = 4294967295;
                        v1 = 4294967295;
                        return sub_41278f();
                    }
                    WaitForMultipleObjects(32, v8, -1, 4294967295);
                    j = 0;
                    do
                    {
                        CloseHandle(v8[j]);
                        j += 1;
                    } while (j != 32);
                    sub_402628();
                    i -= 32;
                } while (i > 0);
            }
        }
    }
    v29 = _ccall(v26, v27, (unsigned int)v28, 0);
    *((unsigned int *)v29) = v3;
    a1 = sub_4127e7;
    return sub_4127c9();
}
```

## `sub_0041261a` `0x0041261a`

_252 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

typedef struct struct_1 {
    struct struct_0 *field_0;
} struct_1;

extern unsigned int g_4126fe;
extern unsigned int g_412738;
extern struct_1 *g_41f518;
extern struct_1 *g_41f5a4;

int sub_41261a(void)
{
    unsigned int v17;  // eax
    unsigned int ch;  // eax
    unsigned long v27;  // gdt
    unsigned short v28;  // fs
    unsigned long v29;  // 4118
    unsigned long v19;  // ldt
    unsigned long v20;  // gdt
    unsigned short v21;  // fs
    unsigned long v22;  // 4141
    unsigned int v23;  // 4103
    unsigned long v24;  // 4150
    unsigned long v25;  // 4118
    unsigned long v26;  // ldt
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0x8]
    unsigned int v7;  // [bp+0xffeb8]
    unsigned int v8;  // [bp+0xfffdc]
    unsigned int idx;  // [bp+0xfffe0]
    unsigned int v10;  // [bp+0xfffe4]
    unsigned int v11;  // [bp+0xfffe8]
    unsigned int v12;  // [bp+0xffff0]
    unsigned int v13;  // [bp+0xffff4]
    unsigned int v14;  // [bp+0xffff8]
    char v15;  // [bp+0xffffe]

    if (g_41f5a4->field_0(v14, v17))
    {
        do
        {
            ch = GetCurrentProcessId();
            if (ch != v7)
            {
                v13 = OpenProcess(0x1f0fff, 0, v7);
                if (v13)
                {
                    v3 = /* unsupported instruction */;
                    v2 = sub_4126f7;
                    v22 = _ccall(v19, v20, (unsigned int)v21, 0);
                    v23 = *((int *)v22);
                    v1 = *((int *)v22);
                    v24 = _ccall(v19, v20, (unsigned int)v21, 0);
                    *((unsigned int **)v24) = &v1;
                    v12 = sub_40f474(v13, NULL, 0, v11, v8, 0, /* unsupported instruction */ - 20);
                    if (v12)
                    {
                        if (v15)
                        {
                            v0 = idx + 1;
                            sub_404808();
                            *((unsigned int *)(v10 + idx * 4)) = v12;
                            idx += 1;
                        }
                        else
                        {
                            SetThreadPriority(v12, 4294967281);
                            CloseHandle(v12);
                            v8 += 500;
                        }
                    }
                    v25 = _ccall(v19, v20, (unsigned int)v21, 0);
                    *((unsigned int *)v25) = v23;
                    v3 = &g_4126fe;
                    return sub_4126ed();
                }
            }
        } while (g_41f518->field_0(v14, /* unsupported instruction */ - 340));
    }
    v29 = _ccall(v26, v27, (unsigned int)v28, 0);
    *((unsigned int *)v29) = v4;
    v5 = &g_412738;
    return sub_412727();
}
```

## `sub_004126ed` `0x004126ed`

_10 bytes. (leaf/helper — see body)_

```c
int sub_4126ed(void)
{
    HANDLE v1;  // [bp+0xffff4]

    return CloseHandle(v1);
}
```

## `sub_004126f7` `0x004126f7`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4126f7(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004126fc` `0x004126fc`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4126fc(void)
{
    return sub_4126ed();
}
```

## `sub_00412727` `0x00412727`

_10 bytes. (leaf/helper — see body)_

```c
int sub_412727(void)
{
    HANDLE v1;  // [bp+0xffff8]

    return CloseHandle(v1);
}
```

## `sub_00412731` `0x00412731`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_412731(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00412736` `0x00412736`

_2 bytes. (leaf/helper — see body)_

```c
int sub_412736(void)
{
    return sub_412727();
}
```

## `sub_0041278f` `0x0041278f`

_39 bytes. (leaf/helper — see body)_

```c
int sub_41278f(void)
{
    LPArray v4;  // eax
    unsigned int v5;  // esi
    unsigned int v6;  // esi
    unsigned int v7;  // ebx
    unsigned int i;  // esi
    unsigned int v9;  // esi
    int v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x4]
    unsigned int v2;  // [bp+0xfffe0]
    unsigned int v3;  // [bp+0xfffe4]

    WaitForMultipleObjects(v2, v4, v0, v1);
    v5 = v2 - 1;
    if (v5 < 0)
        goto LABEL_0x4127bc;
    v6 = v5 + 1;
    v7 = 0;
    do
    {
        i = v6;
        CloseHandle(*((int *)(v3 + v7 * 4)));
        v7 += 1;
        v9 = i - 1;
        v6 = v9;
    } while (i != 1);
}
```

## `sub_004127c9` `0x004127c9`

_23 bytes. (leaf/helper — see body)_

```c
int sub_4127c9(void)
{
    sub_403a10();
    return sub_404814();
}
```

## `sub_004127e0` `0x004127e0`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4127e0(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004127e5` `0x004127e5`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4127e5(void)
{
    return sub_4127c9();
}
```

## `sub_004127e7` `0x004127e7`

_7 bytes. (leaf/helper — see body)_

```c
void sub_4127e7(unsigned int a0, unsigned int a1)
{
    return;
}
```

## `sub_004127ee` `0x004127ee`

_1553 bytes. refs "NamedBuffer, mAH, Shared, API $", "Mutex, mAH, Shared, API "_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    struct struct_1 *field_8;
    unsigned int field_c;
    char padding_10[504];
    unsigned int field_208;
} struct_0;

typedef struct struct_5 {
    char padding_0[16];
    int field_10;
    unsigned int field_14;
} struct_5;

typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
} struct_1;

extern struct_2 *g_41efe4;
extern struct_2 *g_41efec;
extern struct_2 *g_41eff4;
extern struct_2 *g_41eff8;
extern struct_2 *g_41f000;
extern struct_2 *g_41f004;
extern struct_2 *g_41f008;
extern struct_2 *g_41f010;
extern struct_2 *g_41f014;
extern struct_2 *g_41f020;
extern struct_2 *g_41f028;

unsigned int sub_4127ee(void)
{
    unsigned int v30;  // ebx
    unsigned int v31;  // esi
    unsigned int v40;  // eax
    int v41;  // eax
    unsigned int v42;  // ebx
    int v43;  // eax
    unsigned int v44;  // eax
    int v45;  // eax
    struct_5 *index;  // esi
    unsigned int v47;  // eax
    unsigned int v48;  // eax
    unsigned int idx;  // ebx
    unsigned int v32;  // edi
    unsigned int k;  // eax
    unsigned int *iter;  // edi
    unsigned int v52;  // ecx
    unsigned int v53;  // eax
    int v54;  // eax
    unsigned int idx1[4];  // esi
    int v56;  // eax
    int v57;  // ebx
    int v58;  // eax
    int v59;  // eax
    struct_0 *i;  // esi
    int v60;  // eax
    unsigned int m;  // eax
    unsigned int v62[9];  // edx
    unsigned int v63[11];  // edi
    char iter1[4];  // edi
    unsigned int v35;  // ecx
    unsigned int v36;  // ebx
    unsigned int idx2;  // eax
    int v38;  // eax
    struct_5 *v39;  // edx
    unsigned int *l;  // [bp-0x1b8]
    struct_5 *v1;  // [bp-0x1b8]
    unsigned int v2;  // [bp-0x190]
    unsigned int v3;  // [bp-0x18c]
    unsigned int v4;  // [bp-0x188]
    char v5[24];  // [bp-0x182]
    char v6;  // [bp-0x16a]
    unsigned int v7;  // [bp-0x169]
    unsigned int v8;  // [bp-0x165]
    char v9;  // [bp-0x161]
    char v10[31];  // [bp-0x160]
    unsigned int v11;  // [bp-0x141]
    unsigned int v12;  // [bp-0x13d]
    char v13;  // [bp-0x139]
    char v14;  // [bp-0x138]
    unsigned int *v15;  // [bp-0x38]
    unsigned int v16[2];  // [bp-0x34]
    int iter2;  // [bp-0x30]
    struct_2 **v18;  // [bp-0x2c]
    unsigned int v19;  // [bp-0x28]
    unsigned int v20;  // [bp-0x24]
    char v21;  // [bp-0x1e]
    char v22;  // [bp-0x1d]
    unsigned int v23;  // [bp-0x1c]
    unsigned int node;  // [bp-0x18], Other Possible Types: int
    unsigned int v25;  // [bp-0x14]
    unsigned int v26;  // [bp-0x10]
    unsigned int v27;  // [bp-0xc]
    unsigned int v28;  // [bp-0x8]
    struct_0 *v29;  // [bp+0x4]

    v4 = v30;
    v3 = v31;
    v2 = v32;
    strncpy(v10, "NamedBuffer, mAH, Shared, API $", 31);
    strncpy(v5, "Mutex, mAH, Shared, API ", 24);
    v6 = 36;
    v13 = 0;
    v9 = 0;
    v27 = 0;
    if (v27 >= 64)
    {
        v28 = 0;
        return v28;
    }
    do
    {
        if (!v27)
        {
            g_41efec(v29->field_0, 4294967295);
            i = &v29->field_c;
            iter1 = &v14;
            for (v35 = 64; v35; i = &i->field_4)
            {
                v35 -= 1;
                *((unsigned int *)&iter1[0]) = i->field_0;
                iter1 += 1;
            }
            v27 = v29->field_208;
            g_41f008(v29->field_0);
        }
        else
        {
            g_41efec(v29->field_0, 4294967295);
            v26 = *((int *)&v29->padding_10[248 + 4 * v27]);
            v36 = (&v29->field_c)[v27];
            *((int *)&v29->padding_10[248 + 4 * v27]) = *((int *)&v29->padding_10[248 + 4 * v29->field_208]);
            *((unsigned int *)&v29->padding_10[248 + 4 * v29->field_208]) = 0;
            (&v29->field_c)[v27] = (&v29->field_c)[v29->field_208];
            (&v29->field_c)[v29->field_208] = 0;
            idx2 = v29->field_208;
            *((int *)&(&v14)[4 * v27]) = *((int *)&(&v14)[4 * idx2]);
            *((unsigned int *)&(&v14)[4 * idx2]) = 0;
            v29->field_208 = v29->field_208 - 1;
            v27 = v29->field_208;
            g_41f008(v29->field_0);
            g_41f004(v36);
            g_41efec(v29->field_4, 4294967295);
            node = 0;
            v38 = v29->field_8->field_0 - 1;
            if (v38 >= 0)
            {
                iter2 = v38 + 1;
                v25 = 0;
                do
                {
                    v39 = v29->field_8->field_4 + v25 * 24;
                    v40 = v39->field_10 - 1;
                    if (v40 >= 0)
                    {
                        v41 = v40 + 1;
                        v42 = 0;
                        do
                        {
                            v43 = v41;
                            if (*((int *)(v39->field_14 + v42 * 12)) == v26)
                                node += 1;
                        } while ((v42 += 1, v44 = v43 - 1, v41 = (int)(v43 - 1), v43 != 1));
                    }
                } while ((v25 += 1, iter2 = (int)(iter2 - 1), iter2 = iter2, iter2 != 1));
            }
            v23 = g_41f010(64, node * 24);
            node = 0;
            v16 = v29->field_8;
            v22 = 1;
            v45 = v16[0] - 1;
            if (v45 >= 0)
            {
                iter2 = v45 + 1;
                v25 = 0;
                do
                {
                    index = v16[1] + v25 * 24;
                    v21 = 1;
                    v47 = index->field_10 - 1;
                    if (v47 >= 0)
                    {
                        v48 = v47 + 1;
                        idx = 0;
                        do
                        {
                            k = v48;
                            if (*((int *)(index->field_14 + idx * 12)) == v26)
                            {
                                l = v16[1] + v25 * 24;
                                v1 = index;
                                iter = v23 + node * 24;
                                for (v52 = 6; v52; l += 1)
                                {
                                    v52 -= 1;
                                    *(iter) = *(l);
                                    iter += 1;
                                }
                                *((int *)(v23 + node * 24 + 12)) = *((int *)(index->field_14 + idx * 12 + 8));
                                node += 1;
                                *((unsigned int *)(index->field_14 + idx * 12)) = 0;
                            }
                            else if (*((int *)(index->field_14 + idx * 12)))
                            {
                                v21 = 0;
                            }
                            idx += 1;
                            v53 = k - 1;
                            v48 = v53;
                        } while (k != 1);
                    }
                    if (v21)
                    {
                        if (index->field_14)
                            g_41f028(index->field_14);
                        index->field_10 = 0;
                        index->field_14 = 0;
                    }
                    else if (index->field_10 > 0)
                    {
                        v22 = 0;
                    }
                    v25 += 1;
                    iter2 -= 1;
                } while (iter2 != 1);
            }
            if (v22)
            {
                if (v16[1])
                    g_41f028(v16[1]);
                v16[0] = 0;
                v16[1] = 0;
            }
            g_41f008(v29->field_4);
            v54 = node - 1;
            if (v54 >= 0)
            {
                iter2 = v54 + 1;
                v25 = 0;
                do
                {
                    idx1 = v23 + v25 * 24;
                    v11 = idx1[1];
                    v12 = idx1[2];
                    v7 = idx1[1];
                    v8 = idx1[2];
                    v20 = g_41efe4(0, 0, v5);
                    if (v20)
                    {
                        g_41efec(v20, 4294967295);
                        v19 = g_41eff4(983071, 0, v10);
                        if (v19)
                        {
                            v18 = g_41eff8(v19, 983071, 0, 0, 0);
                            if (v18)
                            {
                                v15 = &*(v18)->field_0;
                                v56 = *(v15) - 2;
                                if (v56 > 0)
                                {
                                    v57 = 1;
                                    do
                                    {
                                        v58 = v56;
                                        if (v15[7 + 2 * v57] == idx1[3])
                                        {
                                            v60 = *(v15) - 2;
                                            if (v60 >= v57)
                                            {
                                                m = v60 - v57 + 1;
                                                node = v57;
                                                do
                                                {
                                                    v62 = &v15[2 * node + 7];
                                                    v63 = &v15[2 * node + 9];
                                                    v62[0] = v63[0];
                                                    v62[1] = v63[1];
                                                    node += 1;
                                                    m -= 1;
                                                } while (m != 1);
                                            }
                                            *((unsigned int *)v15[6 + 2 * v57]) = v15[7 + 2 * v57];
                                            *(v15) = *(v15) - 1;
                                            if (idx1[3])
                                            {
                                                g_41f028(idx1[3]);
                                                break;
                                            }
                                        }
                                    } while ((v57 = (int)(v57 + 1), v59 = (int)(v58 - 1), v56 = (int)(v58 - 1), v58 != 1));
                                }
                                g_41f000(v18);
                            }
                            g_41f004(v19);
                        }
                        g_41f008(v20);
                        g_41f004(v20);
                    }
                } while ((v25 += 1, iter2 = (int)(iter2 - 1), iter2 = iter2, iter2 != 1));
            }
            g_41f014(v23);
        }
    } while ((v27 = g_41f020(v27 + 1, &v14, 0, 4294967295), v27 < 64));
    v28 = 0;
    return v28;
}
```

## `sub_00412dff` `0x00412dff`

_1 bytes. (leaf/helper — see body)_

```c
int sub_412dff(void)
{
    sub_412e00();
    return;
}
```

## `sub_00412e00` `0x00412e00`

_274 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[16];
    unsigned int field_10;
    unsigned int field_14;
} struct_1;

int sub_412e00(void)
{
    unsigned int v3;  // eax
    struct_1 *idx;  // ebx
    unsigned int v13;  // eax
    unsigned int idx1[3];  // ecx
    unsigned int idx2[3];  // edi
    unsigned int v17;  // edx
    int v18;  // eax
    int v19;  // edx
    unsigned int j;  // edx
    int v5;  // edx
    unsigned int v6;  // edx
    unsigned int v7;  // eax
    unsigned int v8;  // edx
    unsigned int v9;  // ecx
    int v10;  // edx
    int v11;  // edx
    unsigned int i;  // edx
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]
    void* index;  // [bp+0x4]

    idx = *((int *)((int)index[4] + 4)) + v3 * 24;
    v5 = idx->field_10 - 1;
    if (v5 >= 0)
    {
        v6 = v5 + 1;
        v7 = 0;
        do
        {
            v8 = v6;
            v9 = v7 * 3;
            if (!*((int *)(idx->field_14 + v9 * 4)))
            {
                *((int *)(idx->field_14 + v9 * 4)) = (int)index[8];
                *((int *)(idx->field_14 + v9 * 4 + 4)) = (int)index[12];
                *((int *)(idx->field_14 + v9 * 4 + 8)) = (int)index[8];
                return;
            }
        } while ((v7 += 1, v10 = (int)(v8 - 1), v6 = v8 - 1, v8 != 1));
    }
    v1 = idx->field_10;
    if (!v1)
        idx->field_10 = 16;
    else
        idx->field_10 = v1 * 2;
    v0 = sub_40e970(idx->field_10 * 12, NULL);
    v11 = v1 - 1;
    if (v11 >= 0)
    {
        i = v11 + 1;
        v13 = 0;
        do
        {
            idx1 = v0 + v13 * 12;
            idx2 = idx->field_14 + v13 * 12;
            idx1[0] = idx2[0];
            idx1[1] = idx2[1];
            idx1[2] = idx2[2];
            v13 += 1;
            i -= 1;
        } while (i != 1);
    }
    sub_40ea58(idx->field_14, NULL);
    idx->field_14 = v0;
    v17 = v1 * 3;
    *((int *)(v0 + v17 * 4)) = (int)index[8];
    *((int *)(v0 + v17 * 4 + 4)) = (int)index[12];
    *((int *)(v0 + v17 * 4 + 8)) = (int)index[8];
    v18 = v1 + 1;
    v19 = idx->field_10 - 1;
    if (v19 < v18)
        return;
    j = v19 - v18 + 1;
    do
    {
        *((unsigned int *)(idx->field_14 + v18 * 12)) = 0;
        v18 += 1;
        j -= 1;
    } while (j != 1);
    return;
}
```

## `sub_00412f12` `0x00412f12`

_2 bytes. (leaf/helper — see body)_

```c
int sub_412f12(void)
{
    sub_412f14();
    return;
}
```

## `sub_00412f14` `0x00412f14`

_115 bytes. (leaf/helper — see body)_

```c
int sub_412f14(void)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned long v16;  // 4121
    unsigned short v8;  // fs
    unsigned long v9;  // 4158
    unsigned int v10;  // 4111
    unsigned long v11;  // 4167
    unsigned int v12;  // eax
    unsigned int v13[4];  // ebx
    int v14;  // esi
    int v15;  // ebx
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]
    void* v5;  // [bp+0x4]

    v2 = 0;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v10 = *((int *)v9);
    v0 = *((int *)v9);
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v0;
    v13 = *((int *)((int)v5[4] + 4)) + v12 * 24;
    v13[0] = (int)v5[16];
    v13[3] = 0;
    sub_409b54(&v2, v10, sub_412f90, &v3, v14, v15, 0, &v4);
    sub_402628(&v2, v10, sub_412f90, &v3, v14, v15, 0, &v4);
    sub_412e00(v5);
    v16 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v16) = &v2;
    v1 = sub_412f97;
    sub_412f87();
    return;
}
```

## `sub_00412f87` `0x00412f87`

_9 bytes. (leaf/helper — see body)_

```c
int sub_412f87(void)
{
    return sub_403a10();
}
```

## `sub_00412f90` `0x00412f90`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_412f90(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00412f95` `0x00412f95`

_2 bytes. (leaf/helper — see body)_

```c
int sub_412f95(void)
{
    return sub_412f87();
}
```

## `sub_00412f97` `0x00412f97`

_5 bytes. (leaf/helper — see body)_

```c
void sub_412f97(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    return;
}
```

## `sub_00412f9c` `0x00412f9c`

_273 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    int field_0;
    unsigned int field_4;
} struct_0;

typedef struct struct_1 {
    char padding_0[16];
    int field_10;
} struct_1;

int sub_412f9c(void* a0)
{
    struct_0 *idx;  // ebx
    unsigned int v4;  // edx
    int v13;  // edx
    unsigned int v14;  // edx
    unsigned int v15;  // edx
    int v16;  // edx
    unsigned int v17;  // eax
    int i;  // edx
    unsigned int *iter;  // ecx
    unsigned int v20;  // ecx
    unsigned int v21;  // edx
    unsigned int v22;  // eax
    int v5;  // edx
    unsigned int v23;  // edx
    unsigned int j;  // edx
    unsigned int v25;  // eax
    unsigned int v26;  // ecx
    unsigned int v6;  // eax
    int v7;  // edx
    struct_1 *v8;  // esi
    unsigned int v9;  // edx
    unsigned int v10;  // edx
    int v11;  // edx
    unsigned int v12;  // eax
    unsigned int *k;  // [bp-0x1c]
    unsigned int v1;  // [bp-0xc]
    int v2;  // [bp-0x8]

    idx = (int)a0[4];
    v4 = idx->field_0 - 1;
    if (v4 >= 0)
    {
        v5 = v4 + 1;
        v6 = 0;
        do
        {
            v7 = v5;
            v8 = idx->field_4 + v6 * 24;
            if (v8->field_10 > 0 && *((int *)&v8->padding_0[0]) == (int)a0[16])
                return sub_412e00(a0);
        } while ((v6 += 1, v9 = v7 - 1, v5 = (int)(v7 - 1), v7 != 1));
    }
    v10 = idx->field_0 - 1;
    if (v10 >= 0)
    {
        v11 = v10 + 1;
        v12 = 0;
        do
        {
            v13 = v11;
            if (!*((int *)(idx->field_4 + v12 * 24 + 16)))
                return sub_412f14(a0);
        } while ((v12 += 1, v14 = v13 - 1, v11 = (int)(v13 - 1), v13 != 1));
    }
    v2 = idx->field_0;
    if (!v2)
        idx->field_0 = 32;
    else
        idx->field_0 = v2 * 2;
    v1 = sub_40e970(idx->field_0 * 24, NULL);
    v15 = v2 - 1;
    if (v15 >= 0)
    {
        v16 = v15 + 1;
        v17 = 0;
        do
        {
            i = v16;
            k = idx->field_4 + v17 * 24;
            iter = v1 + v17 * 24;
            for (v20 = 6; v20; k += 1)
            {
                v20 -= 1;
                *(iter) = *(k);
                iter += 1;
            }
            v17 += 1;
            v21 = i - 1;
            v16 = v21;
        } while (i != 1);
    }
    sub_40ea58(idx->field_4, NULL);
    idx->field_4 = v1;
    sub_412f14(a0);
    v22 = v2 + 1;
    v23 = idx->field_0 - 1;
    if (v23 < v22)
        return v22;
    j = v23 - v22 + 1;
    do
    {
        v25 = v22;
        v26 = v25 * 3;
        *((unsigned int *)(idx->field_4 + v26 * 8 + 16)) = 0;
        *((unsigned int *)(idx->field_4 + v26 * 8 + 20)) = 0;
        v22 = v25 + 1;
        j -= 1;
    } while (j != 1);
    return v25 + 1;
}
```

## `sub_004130ad` `0x004130ad`

_3 bytes. (leaf/helper — see body)_

```c
int sub_4130ad(void)
{
    return sub_4130b0();
}
```

## `sub_004130b0` `0x004130b0`

_1300 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
} struct_0;

typedef struct struct_2 {
    char padding_0[520];
    unsigned int field_208;
} struct_2;

typedef struct struct_4 {
    unsigned int field_0;
    unsigned int field_4;
    struct struct_0 *field_8;
    char field_c;
    char padding_d[3];
    unsigned int field_10;
    char padding_14[248];
    unsigned int field_10c;
    char padding_110[248];
    unsigned int field_208;
} struct_4;

extern unsigned int g_4135e2;

int sub_4130b0(void)
{
    unsigned int i;  // ecx
    unsigned int v25;  // ecx
    unsigned int idx[6];  // ecx
    int v35;  // eax
    unsigned int v36;  // eax
    unsigned int v37;  // edx
    unsigned int v38;  // eax
    unsigned int v39;  // esi
    unsigned long v41;  // 4125
    unsigned int v42;  // 4103
    unsigned long v43;  // 4134
    unsigned int v26;  // ebx
    unsigned long v44;  // 4127
    unsigned int v45;  // 4103
    unsigned long v46;  // 4136
    void* idx1;  // ebx
    int v48;  // esi
    unsigned int v50;  // eax
    struct_2 *idx2;  // esi
    unsigned int v52;  // eax
    unsigned int v53;  // eax
    unsigned int v27;  // esi
    unsigned int v54;  // eax
    HANDLE ch1;  // eax
    unsigned int v57;  // eax
    struct_2 *v58;  // eax
    HANDLE v59;  // edi
    void* v60;  // esi
    HANDLE v61;  // edi
    unsigned int v62;  // eax
    unsigned int j;  // 4105
    unsigned long v28;  // ldt
    unsigned int v64;  // eax
    HANDLE v68;  // eax
    unsigned long v69;  // 4118
    unsigned long v70;  // 4118
    unsigned long v71;  // 4118
    unsigned long v29;  // gdt
    unsigned short v30;  // fs
    unsigned long v31;  // 4151
    unsigned long v32;  // 4160
    unsigned int v33;  // eax
    unsigned int v0;  // [bp-0x64]
    void* v1;  // [bp-0x60]
    void* v2;  // [bp-0x60]
    char *v3;  // [bp-0x5c], Other Possible Types: unsigned int
    int v4;  // [bp-0x58]
    int v5;  // [bp-0x58]
    void* v6;  // [bp-0x50]
    int v7;  // [bp-0x4c]
    unsigned int v8;  // [bp-0x48]
    unsigned int v9;  // [bp-0x3c]
    char *v10;  // [bp-0x34], Other Possible Types: unsigned int
    struct_4 *index;  // [bp-0x30], Other Possible Types: unsigned int
    unsigned int iter;  // [bp-0x2c]
    char *v13;  // [bp-0x28], Other Possible Types: unsigned int [2], unsigned int
    struct_0 **v14;  // [bp-0x20], Other Possible Types: unsigned int
    unsigned int v15;  // [bp-0x1c]
    char v16;  // [bp-0x1a]
    char v17;  // [bp-0x19]
    unsigned int v18;  // [bp-0x18]
    HANDLE v19;  // [bp-0x14], Other Possible Types: unsigned int
    unsigned int v20;  // [bp-0x10]
    unsigned int node;  // [bp-0xc]
    char v22;  // [bp-0x4]
    void* v23;  // [bp+0x4]

    i = 11;
    do
    {
        v20 = 0;
        v19 = 0;
        i -= 1;
    } while (i != 1);
    v18 = v25;
    v15 = v26;
    v14 = v27;
    v13 = &v22;
    iter = sub_4135fd;
    v31 = _ccall(v28, v29, (unsigned int)v30, 0);
    index = *((int *)v31);
    v32 = _ccall(v28, v29, (unsigned int)v30, 0);
    *((unsigned int **)v32) = &index;
    v13 = (int)v23[4];
    v33 = v13[0] - 1;
    if (v33 >= 0)
    {
        iter = v33 + 1;
        node = 0;
        do
        {
            idx = v13[1] + node * 24;
            v35 = idx[4] - 1;
            if (v35 >= 0)
            {
                v36 = v35 + 1;
                v37 = 0;
                do
                {
                    v38 = v36;
                    v39 = v37 * 3;
                    if (*((int *)(idx[5] + v39 * 4)) == (int)v23[8])
                    {
                        *((int *)&v23[12]) = *((int *)(idx[5] + v39 * 4 + 4));
                        v71 = _ccall(v28, v29, (unsigned int)v30, 0);
                        *((unsigned int *)v71) = index;
                        v13 = sub_413604;
                        sub_4135ef();
                        return;
                    }
                } while ((v37 += 1, v36 = v38 - 1, v38 != 1));
            }
        } while ((node += 1, iter -= 1, iter = iter, iter != 1));
    }
    v20 = sub_40e6a4();
    if (!v20)
    {
        v71 = _ccall(v28, v29, (unsigned int)v30, 0);
        *((unsigned int *)v71) = index;
        v13 = sub_413604;
        sub_4135ef();
        return;
    }
    v10 = &v22;
    v41 = _ccall(v28, v29, (unsigned int)v30, 0);
    v42 = *((int *)v41);
    v9 = *((int *)v41);
    v43 = _ccall(v28, v29, (unsigned int)v30, 0);
    *((unsigned int **)v43) = &v9;
    sub_409eac(v42, sub_4135db, &v22);
    sub_409eac(&v10);
    sub_403c88();
    v19 = sub_4051ac(NULL, 0, sub_403e78());
    if (!v19)
    {
        v70 = _ccall(v28, v29, (unsigned int)v30, 0);
        *((unsigned int *)v70) = v42;
        v10 = &g_4135e2;
        sub_4135d1();
        return;
    }
    WaitForSingleObject(v19, 4294967295);
    v44 = _ccall(v28, v29, (unsigned int)v30, 0);
    v45 = *((int *)v44);
    v8 = *((int *)v44);
    v46 = _ccall(v28, v29, (unsigned int)v30, 0);
    *((unsigned int **)v46) = &v8;
    sub_409eac(12, v45, sub_4135b4, &v22);
    sub_409eac(&v9);
    sub_403c88();
    v18 = sub_4113d8(sub_403e78(), 12);
    if (v18)
    {
        v17 = GetLastError() != ERROR_ALREADY_EXISTS;
        v7 = 0;
        v6 = NULL;
        idx1 = (void*)MapViewOfFile(v18, FILE_MAP_ALL_ACCESS, 0, 0, NULL);
        if (idx1)
        {
            if (v17)
            {
                *((unsigned int *)idx1) = 0;
                *((struct_0 ***)&idx1[4]) = NULL;
                v7 = 0;
                v6 = NULL;
                v48 = sub_40ecb8(0, 0);
                *((int *)&idx1[8]) = v48;
                if (v48)
                    DuplicateHandle(GetCurrentProcess(), v18, v20, &/* unsupported instruction */, 0, 0, DUPLICATE_SAME_ACCESS);
            }
            if ((int)idx1[8])
            {
                v16 = 1;
                v50 = *((int *)idx1) - 1;
                if (v50 >= 0)
                {
                    iter = v50 + 1;
                    node = 0;
                    do
                    {
                        idx2 = *((int *)((int)idx1[4] + node * 4));
                        v52 = idx2->field_208 - 1;
                        if (v52 >= 0)
                        {
                            v53 = v52 + 1;
                            do
                            {
                                v54 = v53;
                                if (*((int *)&idx2->padding_0[264 + 4 * idx2->field_208]) == (int)v23[8])
                                {
                                    *((int *)&v23[12]) = *((int *)&idx2->padding_0[12 + 4 * idx2->field_208]);
                                    v16 = 0;
                                    break;
                                }
                            } while ((v53 = v54 - 1, v54 != 1));
                        }
                    } while ((node += 1, iter -= 1, iter = iter, iter != 1));
                }
                if (v16)
                {
                    v4 = 0;
                    v3 = NULL;
                    v1 = v23 - 12;
                    ch1 = GetCurrentProcess();
                    DuplicateHandle(ch1, (int)v23[12], v20, v23 - 12, 0, 0, DUPLICATE_SAME_ACCESS);
                    v57 = *((int *)idx1) - 1;
                    v5 = v4;
                    v2 = v1;
                    if (v57 >= 0)
                    {
                        iter = v57 + 1;
                        node = 0;
                        do
                        {
                            v58 = *((int *)((int)idx1[4] + node * 4));
                            if (v58->field_208 < 63)
                            {
                                v58->field_208 = v58->field_208 + 1;
                                *((int *)&v58->padding_0[264 + 4 * v58->field_208]) = (int)v23[8];
                                *((int *)&v58->padding_0[12 + 4 * v58->field_208]) = (int)v23[12];
                                sub_409eac();
                                sub_409eac(*((int *)v44));
                                v3 = &v6;
                                sub_409ac0(&v6, v7);
                                sub_403d40(v6);
                                v59 = OpenEventA(TIMER_ALL_ACCESS, 0, sub_403e78(v6));
                                if (v59)
                                {
                                    SetEvent(v59);
                                    CloseHandle(v59);
                                }
                                v16 = 0;
                                v5 = v7;
                                v2 = v6;
                                break;
                            }
                        } while ((node += 1, iter -= 1, iter = iter, v5 = v4, v2 = v1, iter != 1));
                    }
                    if (v16)
                    {
                        v60 = idx1;
                        sub_409eac();
                        sub_409eac(v5);
                        sub_409ac0(&v2, v3);
                        sub_403d40(v2);
                        v61 = CreateEventA(NULL, 0, 0, sub_403e78(v2));
                        if (v61)
                        {
                            *((unsigned int *)v60) = *((int *)v60) + 1;
                            v14 = sub_40e970(*((int *)v60) * 4, NULL);
                            v62 = *((int *)v60) - 2;
                            if (v62 >= 0)
                            {
                                iter = v62 + 1;
                                node = 0;
                                do
                                {
                                    v14[node] = *((int *)((int)v60[4] + node * 4));
                                    node += 1;
                                    j = iter;
                                    iter = j - 1;
                                } while (j != 1);
                            }
                            sub_40ea58((int)v60[4], NULL);
                            *((struct_0 ***)&v60[4]) = v14;
                            v64 = sub_40e970(524, NULL);
                            *((unsigned int *)((int)v60[4] + *((int *)v60) * 4 - 4)) = v64;
                            index = *((int *)((int)v60[4] + *((int *)v60) * 4 - 4));
                            index->field_208 = 1;
                            index->field_10c = (int)v23[8];
                            DuplicateHandle(GetCurrentProcess(), v61, v20, &index->field_c, 0, 0, DUPLICATE_SAME_ACCESS);
                            CloseHandle(v61);
                            index->field_10 = (int)v23[12];
                            index->field_8 = (int)v23[4];
                            if (*((int *)v60) == 1)
                            {
                                DuplicateHandle(GetCurrentProcess(), v19, v20, index, 0, 0, DUPLICATE_SAME_ACCESS);
                                DuplicateHandle(GetCurrentProcess(), v68, v20, &index->field_4, 0, 0, DUPLICATE_SAME_ACCESS);
                            }
                            else
                            {
                                index->field_0 = *((int *)*((int *)(int)v60[4]));
                                index->field_4 = *((int *)(*((int *)(int)v60[4]) + 4));
                            }
                            sub_40f474(v20, NULL, 0, (int)v60[8], *((int *)((int)v60[4] + *((int *)v60) * 4 - 4)), 0, &/* unsupported instruction */);
                        }
                    }
                }
            }
            UnmapViewOfFile(idx1);
        }
        CloseHandle(v18);
    }
    v69 = _ccall(v28, v29, (unsigned int)v30, 0);
    *((unsigned int *)v69) = v0;
    v3 = sub_4135bb;
    sub_4135aa();
    return;
}
```

## `sub_004135aa` `0x004135aa`

_10 bytes. (leaf/helper — see body)_

```c
int sub_4135aa(void)
{
    HANDLE v1;  // [bp+0xffff4]

    return ReleaseMutex(v1);
}
```

