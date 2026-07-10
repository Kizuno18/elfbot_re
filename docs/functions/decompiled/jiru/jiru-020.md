# elfbot.dll decompiled — jiru 0x10316590..0x103189a0

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10316590` `0x10316590`

_36 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

int sub_10316590(struct_0 *idx, unsigned int a1)
{
    unsigned int v0;  // [bp-0x8]

    v0 = idx->field_14;
    idx->field_14 = a1;
    return v0;
}
```

## `sub_103165c0` `0x103165c0`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_103165c0(unsigned int a0, int a1)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4138
    unsigned int v8;  // eax
    unsigned int v9;  // ecx
    unsigned long v10;  // 4154
    unsigned long v11;  // 4131
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v8 = *((int *)v7);
    v1 = *((int *)v7);
    v0 = v9;
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v10) = &v1;
    sub_10316770(a1, g_1038e180 ^ &v2, 0, v8, sub_1036a8d9, -1, &v3);
    v11 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v11) = v8;
    return a0;
}
```

## `sub_10316620` `0x10316620`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10316620(unsigned int a0, int a1)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4138
    unsigned int v8;  // eax
    unsigned int v9;  // ecx
    unsigned long v10;  // 4154
    unsigned long v11;  // 4131
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v8 = *((int *)v7);
    v1 = *((int *)v7);
    v0 = v9;
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v10) = &v1;
    sub_10316870(a1, g_1038e180 ^ &v2, 0, v8, sub_1036a919, -1, &v3);
    v11 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v11) = v8;
    return a0;
}
```

## `sub_10316680` `0x10316680`

_233 bytes. refs "bad cast"_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
    char padding_c[8];
    char field_14;
} struct_0;

extern unsigned int g_1038e180;
extern int g_103999a0;
extern unsigned int g_103a2260;
extern unsigned int g_103a2268;

unsigned int sub_10316680(struct_0 **a0)
{
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // fs
    unsigned long v13;  // 4137
    unsigned long v14;  // 4151
    unsigned long v15;  // 4117
    unsigned int v0;  // [bp-0x34]
    char v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x24]
    unsigned int v3;  // [bp-0x20]
    unsigned int v4;  // [bp-0x18]
    unsigned int v5;  // [bp-0x14]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]
    char v9;  // [bp-0x4]

    v8 = 4294967295;
    v7 = sub_1036a948;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v6 = *((int *)v13);
    v14 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v14) = &v6;
    sub_10350060(0, g_1038e180 ^ &v9);
    v8 = 0;
    v3 = g_103a2260;
    v4 = sub_10314f00(&g_103a2268);
    v5 = sub_10314fb0(a0, v4);
    if (!v5)
    {
        if (v3)
        {
            v5 = v3;
        }
        else if (sub_10316a20(&v3) == 4294967295)
        {
            sub_103532f5("bad cast");
            sub_103533ea(&v1, &g_103999a0);
        }
        else
        {
            v5 = v3;
            g_103a2260 = v3;
            v2 = v3;
            sub_10313500(v2);
            sub_10314f90(v2);
        }
    }
    v0 = v5;
    v8 = 4294967295;
    sub_10350081();
    v15 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v15) = v6;
    return v0;
}
```

## `sub_10316770` `0x10316770`

_118 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fa9c;
extern char g_1038faa4;

int sub_10316770(unsigned int a0, unsigned int *a1)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4138
    unsigned int v9;  // eax
    unsigned long v10;  // 4154
    unsigned long v11;  // 4135
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v2 = 4294967295;
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v9 = *((int *)v8);
    v1 = *((int *)v8);
    v0 = a0;
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v10) = &v1;
    sub_10313dd0(a0, a1);
    sub_103167f0(g_1038e180 ^ &v3, a0, v9, sub_1036a983, 0, &v4, v4);
    *((char **)a0) = &g_1038faa4;
    *((char **)(a0 + 20)) = &g_1038fa9c;
    v11 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v11) = v9;
    return a0;
}
```

## `sub_103167f0` `0x103167f0`

_120 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fa60;

unsigned int [5] sub_103167f0(unsigned int *idx)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4140
    unsigned int v9;  // eax
    unsigned long v10;  // 4156
    unsigned long v11;  // 4144
    unsigned int v0[5];  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v9 = *((int *)v8);
    v1 = *((int *)v8);
    v0 = idx;
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v10) = &v1;
    *(idx) = &g_1038fa60;
    sub_10338af0(g_1038e180 ^ &v2, idx, v9, sub_1036a9ab, -1, &v3);
    idx[2] = 0;
    idx[3] = 0;
    idx[4] = 4294967295;
    v11 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v11) = v9;
    return idx;
}
```

## `sub_10316870` `0x10316870`

_194 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fa78;
extern char g_1038fa88;
extern char g_1038fa90;

unsigned int * sub_10316870(unsigned int *idx, unsigned int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4139
    unsigned long v10;  // 4153
    unsigned long v11;  // 4123
    unsigned int *v0;  // [bp-0x1c], Other Possible Types: int
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036a9e3;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_10313cd0(idx, a1);
    v4 = 0;
    sub_10316a00(g_1038e180 ^ &v5, v0);
    v4 = 1;
    *(idx) = &g_1038fa90;
    idx[5] = &g_1038fa88;
    idx[10] = &g_1038fa78;
    v1 = (!a1 ? 0 : a1 + 20);
    v0 = (!idx ? NULL : idx + 5);
    v0 = (!idx ? NULL : idx + 5);
    sub_10316940((!idx ? NULL : idx + 5), v1);
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return idx;
}
```

## `sub_10316940` `0x10316940`

_17 bytes. (leaf/helper — see body)_

```c
int sub_10316940(unsigned int a0, int a1)
{
    char v0;  // [bp+0x0]

    return sub_10316960(a1, &v0);
}
```

## `sub_10316960` `0x10316960`

_70 bytes. (leaf/helper — see body)_

```c
unsigned int [5] sub_10316960(unsigned int *idx, unsigned int *index)
{
    unsigned int v0[5];  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = idx;
    sub_103169b0(index + 1, idx, &v1);
    idx[2] = index[2];
    idx[3] = index[3];
    idx[4] = index[4];
    return idx;
}
```

## `sub_103169b0` `0x103169b0`

_30 bytes. (leaf/helper — see body)_

```c
int sub_103169b0(int a0, int *a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_103169d0(*(a1), a0, &v1);
    return a0;
}
```

## `sub_103169d0` `0x103169d0`

_37 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    struct struct_1 *field_c;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

struct_0 *** sub_103169d0(unsigned int *a0, unsigned int a1)
{
    unsigned int *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_10313b30(v0);
    *(v0) = a1;
    return sub_10313c00(v0);
}
```

## `sub_10316a00` `0x10316a00`

_23 bytes. (leaf/helper — see body)_

```c
extern char g_1038fa68;

int sub_10316a00(unsigned int a0)
{
    *((char **)a0) = &g_1038fa68;
    return a0;
}
```

## `sub_10316a20` `0x10316a20`

_140 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10316a20(unsigned int *a0)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4166
    unsigned long v12;  // 4170
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036aa0b;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v0 = g_1038e180 ^ &v7;
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    if (a0 && !*(a0))
    {
        v2 = sub_10350a53(16);
        v6 = 0;
        v1 = (!v2 ? 0 : sub_10316ab0(0));
        v3 = v1;
        v6 = 4294967295;
        *(a0) = v3;
    }
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v13) = v4;
    return 4;
}
```

## `sub_10316ab0` `0x10316ab0`

_176 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern unsigned int g_1038e180;
extern char g_1038fb7c;

int sub_10316ab0(struct_0 *a0, unsigned int a1)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4140
    unsigned long v11;  // 4157
    unsigned long v12;  // 4121
    unsigned int v0;  // [bp-0x98]
    char v1;  // [bp-0x90]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char v5;  // [bp-0x8], Other Possible Types: unsigned int
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036aa46;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v2 = g_1038e180 ^ &v6;
    v0 = v2;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    sub_103153b0(a0, a1);
    v5 = 0;
    *((char **)&a0->padding_0[0]) = &g_1038fb7c;
    sub_103151b0(&v1, "C");
    v5 = 1;
    sub_10319640(&v1);
    v5 = 0;
    sub_10315290(&v1);
    v5 = 4294967295;
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v3;
    return sub_10351225();
}
```

## `sub_10316b60` `0x10316b60`

_633 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern unsigned int g_1038e180;

int sub_10316b60(int a0, unsigned int *idx, unsigned int a2, unsigned int a3, unsigned int a4, char a5, unsigned int a6, unsigned int a7, void* a8, unsigned int *a9)
{
    unsigned long v28;  // ldt
    unsigned long v29;  // gdt
    unsigned short v30;  // fs
    unsigned long v31;  // 4138
    unsigned long v32;  // 4155
    unsigned long v33;  // 4144
    int v0;  // [bp-0xd4]
    char *v1;  // [bp-0xd0]
    unsigned int v2;  // [bp-0xcc]
    int v3;  // [bp-0xc8]
    int v4;  // [bp-0xc4]
    int v5;  // [bp-0xc0]
    int v6;  // [bp-0xbc]
    int v7;  // [bp-0xb8]
    int v8;  // [bp-0xb4]
    int v9;  // [bp-0xb0]
    int v10;  // [bp-0xac]
    struct_0 **v11;  // [bp-0xa4]
    char v12;  // [bp-0xa0]
    char v13;  // [bp-0x84]
    struct_0 **v14;  // [bp-0x68]
    unsigned int v15;  // [bp-0x64]
    int v16;  // [bp-0x60]
    char *v17;  // [bp-0x5c], Other Possible Types: char
    char v18;  // [bp-0x58]
    char v19;  // [bp-0x38]
    unsigned int v20;  // [bp-0x1c]
    unsigned int v21;  // [bp-0x18]
    int v22;  // [bp-0x14]
    unsigned int v23;  // [bp-0x10]
    unsigned int v24;  // [bp-0xc]
    char v25;  // [bp-0x8], Other Possible Types: unsigned int
    char v26;  // [bp-0x4]
    char *v27;  // [bp+0x28]

    v25 = 4294967295;
    v24 = sub_1036aa9e;
    v31 = _ccall(v28, v29, (unsigned int)v30, 0);
    v23 = *((int *)v31);
    v20 = g_1038e180 ^ &v26;
    v2 = v20;
    v32 = _ccall(v28, v29, (unsigned int)v30, 0);
    *((unsigned int **)v32) = &v23;
    v22 = -1;
    if (((short)sub_10315ef0(a8) & 0x4000))
    {
        v10 = sub_10314d40(a8, &v14);
        v9 = v10;
        v25 = 0;
        v21 = sub_10316fe0(v9);
        v25 = 4294967295;
        sub_103130c0(&v14);
        sub_10317800(1, 0);
        v25 = 1;
        v8 = sub_10316f00(&v13);
        v7 = v8;
        v25 = 2;
        sub_10316de0(v7);
        v25 = 1;
        sub_10314610(&v13);
        sub_103170d0(0);
        v6 = sub_10316f70(&v12);
        v5 = v6;
        v25 = 3;
        sub_10316de0(v5);
        v25 = 1;
        sub_10314610(&v12);
        v22 = sub_10319350(&/* unsupported instruction */, &/* unsupported instruction */, 2, (unsigned int)sub_102ec9a0(&v19));
        v25 = 4294967295;
        sub_10314610(&v19);
    }
    else
    {
        v15 = 0;
        v1 = &v15;
        v4 = sub_10314d40(a8, &v11);
        v3 = v4;
        v25 = 4;
        v0 = v3;
        v16 = sub_1035069a(&v18, &v17, sub_103184e0(a0, &v18, &/* unsupported instruction */, &/* unsupported instruction */, sub_10315ef0(a8)));
        v25 = 4294967295;
        sub_103130c0(&v11);
        if (v17 != &v18 && !v15 && v16 <= 1)
            v22 = v16;
    }
    if ((char)sub_10319590(&/* unsupported instruction */, &/* unsupported instruction */))
        *(a9) = *(a9) | 1;
    if (v22 < 0)
        *(a9) = *(a9) | 2;
    else
        *(v27) = v22;
    *(idx) = a2;
    idx[1] = a3;
    idx[2] = a4;
    v33 = _ccall(v28, v29, (unsigned int)v30, 0);
    *((unsigned int *)v33) = v23;
    return sub_10351225();
}
```

## `sub_10316de0` `0x10316de0`

_25 bytes. (leaf/helper — see body)_

```c
int sub_10316de0(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10316e00(a1, a0, &v1);
}
```

## `sub_10316e00` `0x10316e00`

_33 bytes. (leaf/helper — see body)_

```c
extern int g_1038fb14;

int sub_10316e00(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10316e30(a1, 0, g_1038fb14, a0, &v1);
}
```

## `sub_10316e30` `0x10316e30`

_205 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

extern unsigned int g_1038fb14;

unsigned int [7] sub_10316e30(unsigned int *a0, struct_0 *a1, unsigned int a2, int a3)
{
    struct_0 *v1;  // eax
    struct_0 *v2;  // eax
    int v0;  // [bp-0x8], Other Possible Types: unsigned int

    if (sub_1031e920(a0) < a2)
        sub_103503dd();
    v0 = sub_1031e920() - a2;
    if (v0 < a3)
        a3 = v0;
    if (g_1038fb14 - a0[5] > a3 && a0[5] + a3 >= a0[5])
    {
        if (a3 > 0)
        {
            v0 = a0[5] + a3;
            if (!(char)sub_103149b0(a0, v0, 0))
                return a0;
            v1 = sub_10314a50(a1);
            v2 = sub_10314a50(a0);
            sub_10313350(&v2->padding_0[a0[5]], a0[6] - a0[5], &v1->padding_0[a2], a3);
            sub_10314960(a0, v0);
            return a0;
        }
        else
        {
            return a0;
        }
    }
    sub_1035039e();
}
```

## `sub_10316f00` `0x10316f00`

_100 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[16];
    struct struct_1 *field_10;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern unsigned int g_1038e180;

int sub_10316f00(struct_0 **a0, unsigned int a1)
{
    unsigned long v3;  // ldt
    unsigned long v4;  // gdt
    unsigned short v5;  // fs
    unsigned long v6;  // 4144
    unsigned int v7;  // eax
    unsigned long v8;  // 4158
    unsigned long v9;  // 4131
    unsigned int v0;  // [bp-0x10]
    char v1;  // [bp-0x4]
    char v2;  // [bp+0x0]

    v6 = _ccall(v3, v4, (unsigned int)v5, 0);
    v7 = *((int *)v6);
    v0 = *((int *)v6);
    v8 = _ccall(v3, v4, (unsigned int)v5, 0);
    *((unsigned int **)v8) = &v0;
    *(a0)->field_10(a1, g_1038e180 ^ &v1, a0, 0, v7, sub_1036aae9, 4294967295, &v2);
    v9 = _ccall(v3, v4, (unsigned int)v5, 0);
    *((unsigned int *)v9) = v7;
    return a1;
}
```

## `sub_10316f70` `0x10316f70`

_100 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    struct struct_1 *field_14;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern unsigned int g_1038e180;

int sub_10316f70(struct_0 **a0, unsigned int a1)
{
    unsigned long v3;  // ldt
    unsigned long v4;  // gdt
    unsigned short v5;  // fs
    unsigned long v6;  // 4144
    unsigned int v7;  // eax
    unsigned long v8;  // 4158
    unsigned long v9;  // 4131
    unsigned int v0;  // [bp-0x10]
    char v1;  // [bp-0x4]
    char v2;  // [bp+0x0]

    v6 = _ccall(v3, v4, (unsigned int)v5, 0);
    v7 = *((int *)v6);
    v0 = *((int *)v6);
    v8 = _ccall(v3, v4, (unsigned int)v5, 0);
    *((unsigned int **)v8) = &v0;
    *(a0)->field_14(a1, g_1038e180 ^ &v1, a0, 0, v7, sub_1036ab29, 4294967295, &v2);
    v9 = _ccall(v3, v4, (unsigned int)v5, 0);
    *((unsigned int *)v9) = v7;
    return a1;
}
```

## `sub_10316fe0` `0x10316fe0`

_233 bytes. refs "bad cast"_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
    char padding_c[8];
    char field_14;
} struct_0;

extern unsigned int g_1038e180;
extern int g_103999a0;
extern unsigned int g_103a17ac;
extern unsigned int g_103a2264;

unsigned int sub_10316fe0(struct_0 **a0)
{
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // fs
    unsigned long v13;  // 4137
    unsigned long v14;  // 4151
    unsigned long v15;  // 4117
    unsigned int v0;  // [bp-0x34]
    char v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x24]
    unsigned int v3;  // [bp-0x20]
    unsigned int v4;  // [bp-0x18]
    unsigned int v5;  // [bp-0x14]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]
    char v9;  // [bp-0x4]

    v8 = 4294967295;
    v7 = sub_1036ab58;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v6 = *((int *)v13);
    v14 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v14) = &v6;
    sub_10350060(0, g_1038e180 ^ &v9);
    v8 = 0;
    v3 = g_103a2264;
    v4 = sub_10314f00(&g_103a17ac);
    v5 = sub_10314fb0(a0, v4);
    if (!v5)
    {
        if (v3)
        {
            v5 = v3;
        }
        else if (sub_103171e0(&v3) == 4294967295)
        {
            sub_103532f5("bad cast");
            sub_103533ea(&v1, &g_103999a0);
        }
        else
        {
            v5 = v3;
            g_103a2264 = v3;
            v2 = v3;
            sub_10313500(v2);
            sub_10314f90(v2);
        }
    }
    v0 = v5;
    v8 = 4294967295;
    sub_10350081();
    v15 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v15) = v6;
    return v0;
}
```

## `sub_103170d0` `0x103170d0`

_27 bytes. (leaf/helper — see body)_

```c
char sub_103170d0(int a0, char a1)
{
    int v2;  // eax
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    v2 = _INSERT(0, 0, a1);
    return sub_103170f0(1, v2, a0, &v1);
}
```

## `sub_103170f0` `0x103170f0`

_114 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    int field_14;
} struct_0;

extern unsigned int g_1038fb14;

struct_0 * sub_103170f0(struct_0 *a0, int a1, char a2)
{
    char v1;  // al
    int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (g_1038fb14 - a0->field_14 <= a1)
    {
        sub_1035039e(a0);
    }
    else if (a1 > 0)
    {
        v0 = a0->field_14 + a1;
        v1 = sub_103149b0(a0, v0, 0);
        if (!v1)
            return a0;
        v2 = _INSERT(v1, 0, a2);
        sub_10317170(a0->field_14, a1, v2);
        sub_10314960(a0, v0);
        return a0;
    }
    else
    {
        return a0;
    }
}
```

## `sub_10317170` `0x10317170`

_73 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

char * sub_10317170(struct_0 *a0, unsigned int a1, unsigned int a2)
{
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    struct_0 *v2;  // [bp-0x8]
    char v3;  // [bp+0xc]

    v2 = a0;
    v2 = a0;
    if (a2 != 1)
    {
        v1 = _INSERT(a0, 0, v3);
        v0 = a2;
        return sub_103171c0(&sub_10314a50(v2)->padding_0[a1]);
    }
    return sub_103149a0(&sub_10314a50(v2)->padding_0[a1], &v3);
}
```

## `sub_103171c0` `0x103171c0`

_26 bytes. (leaf/helper — see body)_

```c
int sub_103171c0(int a0, int a1, char a2)
{
    char v0;  // [bp+0x0]

    return sub_10350ad0(a0, a2, a1, &v0);
}
```

## `sub_103171e0` `0x103171e0`

_140 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_103171e0(unsigned int *a0)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4166
    unsigned long v12;  // 4170
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036ab8b;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v0 = g_1038e180 ^ &v7;
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    if (a0 && !*(a0))
    {
        v2 = sub_10350a53(24);
        v6 = 0;
        v1 = (!v2 ? 0 : sub_10317270(0));
        v3 = v1;
        v6 = 4294967295;
        *(a0) = v3;
    }
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v13) = v4;
    return 4;
}
```

## `sub_10317270` `0x10317270`

_230 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern unsigned int g_1038e180;
extern char g_1038fbb0;

int sub_10317270(struct_0 *a0, unsigned int a1)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4140
    unsigned long v12;  // 4157
    unsigned long v13;  // 4121
    unsigned int v0;  // [bp-0xa0]
    char v1;  // [bp-0x98]
    char v2;  // [bp-0x90]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    char v6;  // [bp-0x8], Other Possible Types: unsigned int
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036abc6;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v3 = g_1038e180 ^ &v7;
    v0 = v3;
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    sub_103153b0(a0, a1);
    v6 = 0;
    *((char **)&a0->padding_0[0]) = &g_1038fbb0;
    sub_103151b0(&v2, "C");
    v6 = 1;
    sub_10317600(&v2);
    if (!*((char *)&a0[1].field_4 + 1))
        *((char *)&a0[1].field_4 + 1) = sub_10318a60(44, 0, sub_10317360(&v1));
    v6 = 0;
    sub_10315290(&v2);
    v6 = 4294967295;
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v13) = v4;
    return sub_10351225();
}
```

## `sub_10317360` `0x10317360`

_43 bytes. (leaf/helper — see body)_

```c
int sub_10317360(void)
{
    int v2;  // ecx
    unsigned int v3;  // edx
    unsigned int v0;  // [bp-0xc]
    unsigned int v1[2];  // [bp+0x4]

    v0 = sub_10350830(v2);
    v1[0] = v0;
    v1[1] = v3;
    return;
}
```

## `sub_10317390` `0x10317390`

_17 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    char field_c;
} struct_0;

int sub_10317390(struct_0 *a0)
{
    return _INSERT(a0, 0, a0->field_c);
}
```

## `sub_103173b0` `0x103173b0`

_17 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[13];
    char field_d;
} struct_0;

int sub_103173b0(struct_0 *a0)
{
    return _INSERT(a0, 0, a0->field_d);
}
```

## `sub_103173d0` `0x103173d0`

_98 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    int field_8;
} struct_0;

extern unsigned int g_1038e180;

int sub_103173d0(struct_0 *a0, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4141
    unsigned long v10;  // 4155
    unsigned long v11;  // 4131
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036ac09;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = 0;
    sub_10314590(a1, a0->field_8);
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return a1;
}
```

## `sub_10317440` `0x10317440`

_98 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[16];
    int field_10;
} struct_0;

extern unsigned int g_1038e180;

int sub_10317440(struct_0 *a0, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4141
    unsigned long v10;  // 4155
    unsigned long v11;  // 4131
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036ac49;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = 0;
    sub_10314590(a1, a0->field_10);
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return a1;
}
```

## `sub_103174b0` `0x103174b0`

_98 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    int field_14;
} struct_0;

extern unsigned int g_1038e180;

int sub_103174b0(struct_0 *a0, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4141
    unsigned long v10;  // 4155
    unsigned long v11;  // 4131
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036ac89;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = 0;
    sub_10314590(a1, a0->field_14);
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return a1;
}
```

## `sub_10317520` `0x10317520`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10317520(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10317550(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_10317550` `0x10317550`

_92 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fbb0;

int sub_10317550(unsigned int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned int v10;  // eax
    unsigned long v11;  // 4154
    int v12;  // eax
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v2 = 4294967295;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v10 = *((int *)v9);
    v1 = *((int *)v9);
    v0 = a0;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v1;
    *((char **)a0) = &g_1038fbb0;
    sub_103175b0(g_1038e180 ^ &v3, a0, v10, sub_1036acb8, 0, &v4);
    v2 = 4294967295;
    v12 = sub_10315390(a0);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v10;
    return v12;
}
```

## `sub_103175b0` `0x103175b0`

_76 bytes. (leaf/helper — see body)_

```c
int sub_103175b0(unsigned int *idx)
{
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v2 = idx[2];
    sub_10350eb5(v2, idx);
    v1 = idx[4];
    sub_10350eb5(v1);
    v0 = idx[5];
    return sub_10350eb5(v0);
}
```

## `sub_10317600` `0x10317600`

_311 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
    char field_c;
    char field_d;
    char padding_e[2];
    unsigned int field_10;
    unsigned int field_14;
} struct_0;

typedef struct struct_1 {
    struct struct_2 *field_0;
    struct struct_2 *field_4;
    int field_8;
} struct_1;

typedef struct struct_2 {
    char field_0;
} struct_2;

extern unsigned int g_1038e180;

unsigned int sub_10317600(struct_0 *idx, unsigned int a1)
{
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    int v22;  // edx
    int v23;  // eax
    unsigned int v25;  // eax
    unsigned long v26;  // 4130
    unsigned short v14;  // fs
    unsigned long v15;  // 4145
    unsigned long v16;  // 4167
    int v17;  // edi
    int v18;  // esi
    int v19;  // ebx
    int v20;  // eax
    int v21;  // eax
    unsigned int v0;  // [bp-0x54]
    char v1;  // [bp-0x40]
    char v2;  // [bp-0x38]
    char v3;  // [bp-0x30]
    char v4;  // [bp-0x28]
    char v5;  // [bp-0x20]
    struct_1 *v6;  // [bp-0x18]
    char *v7;  // [bp-0x14], Other Possible Types: struct_0 *
    unsigned int v8;  // [bp-0x10]
    unsigned int v9;  // [bp-0xc]
    unsigned int v10;  // [bp-0x8]
    char v11;  // [bp-0x4]

    v10 = 4294967295;
    v9 = sub_1036ace0;
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    v8 = *((int *)v15);
    v7 = idx;
    v0 = g_1038e180 ^ &v11;
    v16 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v16) = &v8;
    v7 = &v0;
    v6 = sub_10317760(g_1038e180 ^ &v11, v17, v18, v19, idx);
    idx->field_8 = 0;
    idx->field_10 = 0;
    idx->field_14 = 0;
    v10 = 0;
    v20 = sub_10317360(&v5);
    idx->field_8 = sub_10317790(v6->field_8, 0, v20);
    idx->field_10 = sub_10317790(sub_10317770(0, sub_10317360(&v4)));
    idx->field_14 = sub_10317790(sub_10317780(0, sub_10317360(&v3)));
    v10 = 4294967295;
    v21 = sub_10317360(&v2);
    v22 = _INSERT(0, 0, v6->field_0->field_0);
    idx->field_c = sub_10318a60(v22, 0, v21);
    v23 = sub_10317360(&v1);
    v25 = sub_10318a60(_INSERT(0, 0, v6->field_4->field_0), 0, v23);
    idx->field_d = v25;
    v26 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int *)v26) = v8;
    return v25;
}
```

## `sub_103176d1` `0x103176d1`

_30 bytes. (leaf/helper — see body)_

```c
extern char g_103176f6;

int sub_103176d1(void)
{
    unsigned int *v1;  // [bp+0xfffc4]
    unsigned int v2;  // [bp+0x100000]

    sub_103175b0(v1);
    sub_103533ea(0, 0);
    v2 = 4294967295;
    return &g_103176f6;
}
```

## `sub_10317760` `0x10317760`

_16 bytes. (leaf/helper — see body)_

```c
void sub_10317760(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10353681(a0, &v1);
    return;
}
```

## `sub_10317770` `0x10317770`

_16 bytes. refs "false"_

```c
int sub_10317770(unsigned int a0)
{
    return "false";
}
```

## `sub_10317780` `0x10317780`

_16 bytes. refs "true"_

```c
int sub_10317780(unsigned int a0)
{
    return "true";
}
```

## `sub_10317790` `0x10317790`

_105 bytes. (leaf/helper — see body)_

```c
char * sub_10317790(char *i)
{
    char *v0;  // [bp-0x14]
    char *iter;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    char *v3;  // [bp-0x8]

    v2 = sub_10352f20(i) + 1;
    v0 = sub_1034fef0(v2);
    v3 = v0;
    for (iter = v3; v2 > 0; i += 1)
    {
        *(iter) = *(i);
        v2 -= 1;
        iter += 1;
    }
    return v3;
}
```

## `sub_10317800` `0x10317800`

_62 bytes. (leaf/helper — see body)_

```c
int sub_10317800(unsigned int a0, int a1, char a2)
{
    sub_1031a280(a0, a0);
    sub_103147d0(a0);
    sub_10317840(a1, _INSERT(sub_10314750(a0, 0, 0), 0, a2));
    return a0;
}
```

## `sub_10317840` `0x10317840`

_78 bytes. (leaf/helper — see body)_

```c
int sub_10317840(unsigned int a0, unsigned int a1, char a2)
{
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]
    char v2;  // [bp+0x0]

    v1 = a0;
    if (a1 == 4294967295)
        sub_1035039e(a0, &v2);
    if (!(char)sub_103149b0(a0, a1, 0))
        return a0;
    *((char *)&v0) = a2;
    sub_10317170(a0, 0, a1);
    sub_10314960(a0, a1);
    return a0;
}
```

## `sub_10317890` `0x10317890`

_348 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern unsigned int g_1038e180;

int sub_10317890(int a0, unsigned int *idx, unsigned int a2, unsigned int a3, unsigned int a4, char a5, unsigned int a6, unsigned int a7, void* a8, unsigned int *a9, unsigned short *a10)
{
    unsigned long v19;  // ldt
    unsigned long v20;  // gdt
    unsigned short v21;  // fs
    unsigned long v22;  // 4141
    unsigned long v23;  // 4158
    unsigned long v24;  // 4144
    int v0;  // [bp-0x68]
    unsigned int v1;  // [bp-0x64]
    unsigned int v2;  // [bp-0x60]
    char *v3;  // [bp-0x5c]
    int v4;  // [bp-0x58]
    int v5;  // [bp-0x54]
    struct_0 **v6;  // [bp-0x4c]
    int v7;  // [bp-0x48]
    unsigned int v8;  // [bp-0x44]
    unsigned int v9;  // [bp-0x40]
    char *v10;  // [bp-0x3c], Other Possible Types: char
    char *v11;  // [bp-0x38]
    char v12;  // [bp-0x34]
    char v13;  // [bp-0x33]
    unsigned int v14;  // [bp-0x14]
    unsigned int v15;  // [bp-0x10]
    unsigned int v16;  // [bp-0xc]
    unsigned int v17;  // [bp-0x8]
    char v18;  // [bp-0x4]

    v17 = 4294967295;
    v16 = sub_1036ad08;
    v22 = _ccall(v19, v20, (unsigned int)v21, 0);
    v15 = *((int *)v22);
    v14 = g_1038e180 ^ &v18;
    v1 = v14;
    v23 = _ccall(v19, v20, (unsigned int)v21, 0);
    *((unsigned int **)v23) = &v15;
    v8 = 0;
    v5 = sub_10314d40(a8, &v6);
    v4 = v5;
    v17 = 0;
    v0 = v4;
    v7 = sub_103184e0(a0, &v12, &/* unsupported instruction */, &/* unsupported instruction */, sub_10315ef0(a8));
    v17 = 4294967295;
    sub_103130c0(&v6);
    v3 = (v12 == 45 ? &v13 : &v12);
    v11 = v3;
    v9 = sub_1035069a(v11, &v10, v7, &v8);
    if ((char)sub_10319590(&/* unsupported instruction */, &/* unsupported instruction */))
        *(a9) = *(a9) | 1;
    if (v10 == v11 || v8 || v9 > 0xffff)
    {
        *(a9) = *(a9) | 2;
    }
    else
    {
        v2 = (v12 == 45 ? -(v9) : v9);
        *(a10) = v2;
    }
    *(idx) = a2;
    idx[1] = a3;
    idx[2] = a4;
    v24 = _ccall(v19, v20, (unsigned int)v21, 0);
    *((unsigned int *)v24) = v15;
    return sub_10351225();
}
```

## `sub_103179f0` `0x103179f0`

_343 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern unsigned int g_1038e180;

int sub_103179f0(int a0, unsigned int *idx, unsigned int a2, unsigned int a3, unsigned int a4, char a5, unsigned int a6, unsigned int a7, void* a8, unsigned int *a9, unsigned int *a10)
{
    unsigned long v19;  // ldt
    unsigned long v20;  // gdt
    unsigned short v21;  // fs
    unsigned long v22;  // 4141
    unsigned long v23;  // 4158
    unsigned long v24;  // 4144
    int v0;  // [bp-0x68]
    unsigned int v1;  // [bp-0x64]
    unsigned int v2;  // [bp-0x60]
    char *v3;  // [bp-0x5c]
    int v4;  // [bp-0x58]
    int v5;  // [bp-0x54]
    struct_0 **v6;  // [bp-0x4c]
    int v7;  // [bp-0x48]
    unsigned int v8;  // [bp-0x44]
    unsigned int v9;  // [bp-0x40]
    char *v10;  // [bp-0x3c], Other Possible Types: char
    char *v11;  // [bp-0x38]
    char v12;  // [bp-0x34]
    char v13;  // [bp-0x33]
    unsigned int v14;  // [bp-0x14]
    unsigned int v15;  // [bp-0x10]
    unsigned int v16;  // [bp-0xc]
    unsigned int v17;  // [bp-0x8]
    char v18;  // [bp-0x4]

    v17 = 4294967295;
    v16 = sub_1036ad38;
    v22 = _ccall(v19, v20, (unsigned int)v21, 0);
    v15 = *((int *)v22);
    v14 = g_1038e180 ^ &v18;
    v1 = v14;
    v23 = _ccall(v19, v20, (unsigned int)v21, 0);
    *((unsigned int **)v23) = &v15;
    v8 = 0;
    v5 = sub_10314d40(a8, &v6);
    v4 = v5;
    v17 = 0;
    v0 = v4;
    v7 = sub_103184e0(a0, &v12, &/* unsupported instruction */, &/* unsupported instruction */, sub_10315ef0(a8));
    v17 = 4294967295;
    sub_103130c0(&v6);
    v3 = (v12 == 45 ? &v13 : &v12);
    v11 = v3;
    v9 = sub_1035069a(v11, &v10, v7, &v8);
    if ((char)sub_10319590(&/* unsupported instruction */, &/* unsupported instruction */))
        *(a9) = *(a9) | 1;
    if (v10 == v11 || v8 || v9 > 4294967295)
    {
        *(a9) = *(a9) | 2;
    }
    else
    {
        v2 = (v12 == 45 ? -(v9) : v9);
        *(a10) = v2;
    }
    *(idx) = a2;
    idx[1] = a3;
    idx[2] = a4;
    v24 = _ccall(v19, v20, (unsigned int)v21, 0);
    *((unsigned int *)v24) = v15;
    return sub_10351225();
}
```

## `sub_10317b50` `0x10317b50`

_279 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern unsigned int g_1038e180;

int sub_10317b50(int a0, unsigned int *idx, unsigned int a2, unsigned int a3, unsigned int a4, char a5, unsigned int a6, unsigned int a7, void* a8, unsigned int *a9, unsigned int *a10)
{
    unsigned long v15;  // ldt
    unsigned long v16;  // gdt
    unsigned short v17;  // fs
    unsigned long v18;  // 4144
    unsigned long v19;  // 4161
    unsigned long v20;  // 4144
    int v0;  // [bp-0x5c]
    char *v1;  // [bp-0x58]
    unsigned int v2;  // [bp-0x54]
    int v3;  // [bp-0x50]
    int v4;  // [bp-0x4c]
    struct_0 **v5;  // [bp-0x44]
    unsigned int v6;  // [bp-0x40]
    unsigned int v7;  // [bp-0x3c]
    char *v8;  // [bp-0x38], Other Possible Types: char
    char v9;  // [bp-0x34]
    unsigned int v10;  // [bp-0x14]
    unsigned int v11;  // [bp-0x10]
    unsigned int v12;  // [bp-0xc]
    unsigned int v13;  // [bp-0x8]
    char v14;  // [bp-0x4]

    v13 = 4294967295;
    v12 = sub_1036ad68;
    v18 = _ccall(v15, v16, (unsigned int)v17, 0);
    v11 = *((int *)v18);
    v10 = g_1038e180 ^ &v14;
    v2 = v10;
    v19 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int **)v19) = &v11;
    v6 = 0;
    v1 = &v6;
    v4 = sub_10314d40(a8, &v5);
    v3 = v4;
    v13 = 0;
    v0 = v3;
    v7 = sub_10350844(&v9, &v8, sub_103184e0(a0, &v9, &/* unsupported instruction */, &/* unsupported instruction */, sub_10315ef0(a8)));
    v13 = 4294967295;
    sub_103130c0(&v5);
    if ((char)sub_10319590(&/* unsupported instruction */, &/* unsupported instruction */))
        *(a9) = *(a9) | 1;
    if (v8 == &v9 || v6)
        *(a9) = *(a9) | 2;
    else
        *(a10) = v7;
    *(idx) = a2;
    idx[1] = a3;
    idx[2] = a4;
    v20 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int *)v20) = v11;
    return sub_10351225();
}
```

## `sub_10317c70` `0x10317c70`

_279 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern unsigned int g_1038e180;

int sub_10317c70(int a0, unsigned int *idx, unsigned int a2, unsigned int a3, unsigned int a4, char a5, unsigned int a6, unsigned int a7, void* a8, unsigned int *a9, unsigned int *a10)
{
    unsigned long v15;  // ldt
    unsigned long v16;  // gdt
    unsigned short v17;  // fs
    unsigned long v18;  // 4144
    unsigned long v19;  // 4161
    unsigned long v20;  // 4144
    int v0;  // [bp-0x5c]
    char *v1;  // [bp-0x58]
    unsigned int v2;  // [bp-0x54]
    int v3;  // [bp-0x50]
    int v4;  // [bp-0x4c]
    struct_0 **v5;  // [bp-0x44]
    unsigned int v6;  // [bp-0x40]
    unsigned int v7;  // [bp-0x3c]
    char *v8;  // [bp-0x38], Other Possible Types: char
    char v9;  // [bp-0x34]
    unsigned int v10;  // [bp-0x14]
    unsigned int v11;  // [bp-0x10]
    unsigned int v12;  // [bp-0xc]
    unsigned int v13;  // [bp-0x8]
    char v14;  // [bp-0x4]

    v13 = 4294967295;
    v12 = sub_1036ad98;
    v18 = _ccall(v15, v16, (unsigned int)v17, 0);
    v11 = *((int *)v18);
    v10 = g_1038e180 ^ &v14;
    v2 = v10;
    v19 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int **)v19) = &v11;
    v6 = 0;
    v1 = &v6;
    v4 = sub_10314d40(a8, &v5);
    v3 = v4;
    v13 = 0;
    v0 = v3;
    v7 = sub_1035069a(&v9, &v8, sub_103184e0(a0, &v9, &/* unsupported instruction */, &/* unsupported instruction */, sub_10315ef0(a8)));
    v13 = 4294967295;
    sub_103130c0(&v5);
    if ((char)sub_10319590(&/* unsupported instruction */, &/* unsupported instruction */))
        *(a9) = *(a9) | 1;
    if (v8 == &v9 || v6)
        *(a9) = *(a9) | 2;
    else
        *(a10) = v7;
    *(idx) = a2;
    idx[1] = a3;
    idx[2] = a4;
    v20 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int *)v20) = v11;
    return sub_10351225();
}
```

## `sub_10317d90` `0x10317d90`

_284 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern unsigned int g_1038e180;

int sub_10317d90(int a0, unsigned int *idx, unsigned int a2, unsigned int a3, unsigned int a4, char a5, unsigned int a6, unsigned int a7, void* a8, unsigned int *a9, unsigned int *a10)
{
    unsigned long v14;  // ldt
    unsigned long v15;  // gdt
    unsigned short v16;  // fs
    unsigned long v17;  // 4141
    unsigned long v18;  // 4158
    unsigned int v19;  // edx
    unsigned long v20;  // 4144
    int v0;  // [bp-0x5c]
    unsigned int v1;  // [bp-0x58]
    int v2;  // [bp-0x54]
    int v3;  // [bp-0x50]
    struct_0 **v4;  // [bp-0x48]
    unsigned int v5;  // [bp-0x44]
    unsigned int v6;  // [bp-0x40]
    char *v7;  // [bp-0x38], Other Possible Types: char
    char v8;  // [bp-0x34]
    unsigned int v9;  // [bp-0x14]
    unsigned int v10;  // [bp-0x10]
    unsigned int v11;  // [bp-0xc]
    unsigned int v12;  // [bp-0x8]
    char v13;  // [bp-0x4]

    v12 = 4294967295;
    v11 = sub_1036adc8;
    v17 = _ccall(v14, v15, (unsigned int)v16, 0);
    v10 = *((int *)v17);
    v9 = g_1038e180 ^ &v13;
    v1 = v9;
    v18 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int **)v18) = &v10;
    v5 = 0;
    v3 = sub_10314d40(a8, &v4);
    v2 = v3;
    v12 = 0;
    v0 = v2;
    v6 = sub_103539bd(&v8, &v7, sub_103184e0(a0, &v8, &/* unsupported instruction */, &/* unsupported instruction */, sub_10315ef0(a8)));
    v12 = 4294967295;
    sub_103130c0(&v4);
    if ((char)sub_10319590(&/* unsupported instruction */, &/* unsupported instruction */))
        *(a9) = *(a9) | 1;
    if (v7 == &v8 || v5)
    {
        *(a9) = *(a9) | 2;
    }
    else
    {
        *(a10) = v6;
        a10[1] = v19;
    }
    *(idx) = a2;
    idx[1] = a3;
    idx[2] = a4;
    v20 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int *)v20) = v10;
    return sub_10351225();
}
```

## `sub_10317eb0` `0x10317eb0`

_284 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern unsigned int g_1038e180;

int sub_10317eb0(int a0, unsigned int *idx, unsigned int a2, unsigned int a3, unsigned int a4, char a5, unsigned int a6, unsigned int a7, void* a8, unsigned int *a9, unsigned int *a10)
{
    unsigned long v14;  // ldt
    unsigned long v15;  // gdt
    unsigned short v16;  // fs
    unsigned long v17;  // 4141
    unsigned long v18;  // 4158
    unsigned int v19;  // edx
    unsigned long v20;  // 4144
    int v0;  // [bp-0x5c]
    unsigned int v1;  // [bp-0x58]
    int v2;  // [bp-0x54]
    int v3;  // [bp-0x50]
    struct_0 **v4;  // [bp-0x48]
    unsigned int v5;  // [bp-0x44]
    unsigned int v6;  // [bp-0x40]
    char *v7;  // [bp-0x38], Other Possible Types: char
    char v8;  // [bp-0x34]
    unsigned int v9;  // [bp-0x14]
    unsigned int v10;  // [bp-0x10]
    unsigned int v11;  // [bp-0xc]
    unsigned int v12;  // [bp-0x8]
    char v13;  // [bp-0x4]

    v12 = 4294967295;
    v11 = sub_1036adf8;
    v17 = _ccall(v14, v15, (unsigned int)v16, 0);
    v10 = *((int *)v17);
    v9 = g_1038e180 ^ &v13;
    v1 = v9;
    v18 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int **)v18) = &v10;
    v5 = 0;
    v3 = sub_10314d40(a8, &v4);
    v2 = v3;
    v12 = 0;
    v0 = v2;
    v6 = sub_103539e6(&v8, &v7, sub_103184e0(a0, &v8, &/* unsupported instruction */, &/* unsupported instruction */, sub_10315ef0(a8)));
    v12 = 4294967295;
    sub_103130c0(&v4);
    if ((char)sub_10319590(&/* unsupported instruction */, &/* unsupported instruction */))
        *(a9) = *(a9) | 1;
    if (v7 == &v8 || v5)
    {
        *(a9) = *(a9) | 2;
    }
    else
    {
        *(a10) = v6;
        a10[1] = v19;
    }
    *(idx) = a2;
    idx[1] = a3;
    idx[2] = a4;
    v20 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int *)v20) = v10;
    return sub_10351225();
}
```

## `sub_10317fd0` `0x10317fd0`

_270 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[36];
    int field_24;
} struct_0;

extern unsigned int g_1038e180;

int sub_10317fd0(int a0, unsigned int *idx, unsigned int a2, unsigned int a3, unsigned int a4, char a5, unsigned int a6, unsigned int a7, struct_0 *a8, unsigned int *a9, unsigned int *a10)
{
    unsigned long v14;  // ldt
    unsigned long v15;  // gdt
    unsigned short v16;  // fs
    unsigned long v17;  // 4144
    unsigned long v18;  // 4161
    unsigned long v20;  // 4144
    char *v0;  // [bp-0x74]
    unsigned int v1;  // [bp-0x70]
    int v2;  // [bp-0x6c]
    int v3;  // [bp-0x68]
    struct_0 **v4;  // [bp-0x60]
    unsigned int v5;  // [bp-0x5c]
    unsigned int v6;  // [bp-0x58]
    char *v7;  // [bp-0x54], Other Possible Types: char
    char v8;  // [bp-0x50]
    unsigned int v9;  // [bp-0x14]
    unsigned int v10;  // [bp-0x10]
    unsigned int v11;  // [bp-0xc]
    unsigned int v12;  // [bp-0x8]
    char v13;  // [bp-0x4]

    v12 = 4294967295;
    v11 = sub_1036ae28;
    v17 = _ccall(v14, v15, (unsigned int)v16, 0);
    v10 = *((int *)v17);
    v9 = g_1038e180 ^ &v13;
    v1 = v9;
    v18 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int **)v18) = &v10;
    v5 = 0;
    v0 = &v5;
    v3 = sub_10314d40(a8, &v4);
    v2 = v3;
    v12 = 0;
    sub_103508e7(&v8, &v7, sub_10318a70(a0, &v8, &/* unsupported instruction */, &/* unsupported instruction */, v2));
    if (/* unsupported instruction */)
    {
        v6 = /* unsupported instruction */;
        /* unsupported instruction */
    }
    else
    {
        v6 = nan;
        /* unsupported instruction */
    }
    v12 = 4294967295;
    sub_103130c0(&v4);
    if ((char)sub_10319590(&/* unsupported instruction */, &/* unsupported instruction */))
        *(a9) = *(a9) | 1;
    if (v7 == &v8 || v5)
    {
        *(a9) = *(a9) | 2;
    }
    else
    {
        if (/* unsupported instruction */)
        {
            /* unsupported instruction */
            /* unsupported instruction */
        }
        else
        {
            /* unsupported instruction */
            /* unsupported instruction */
        }
        *(a10) = (/* unsupported instruction */ ? /* unsupported instruction */ : nan);
        /* unsupported instruction */
    }
    *(idx) = a2;
    idx[1] = a3;
    idx[2] = a4;
    v20 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int *)v20) = v10;
    return sub_10351225();
}
```

## `sub_103180e0` `0x103180e0`

_270 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[36];
    int field_24;
} struct_0;

extern unsigned int g_1038e180;

int sub_103180e0(int a0, unsigned int *idx, unsigned int a2, unsigned int a3, unsigned int a4, char a5, unsigned int a6, unsigned int a7, struct_0 *a8, unsigned int *a9, unsigned long long *a10)
{
    unsigned long v14;  // ldt
    unsigned long v15;  // gdt
    unsigned short v16;  // fs
    unsigned long v17;  // 4144
    unsigned long v18;  // 4161
    unsigned long v20;  // 4144
    char *v0;  // [bp-0x7c]
    unsigned int v1;  // [bp-0x78]
    int v2;  // [bp-0x74]
    int v3;  // [bp-0x70]
    struct_0 **v4;  // [bp-0x68]
    unsigned int v5;  // [bp-0x64]
    double v6;  // [bp-0x60], Other Possible Types: unsigned long
    char *v7;  // [bp-0x54], Other Possible Types: char
    char v8;  // [bp-0x50]
    unsigned int v9;  // [bp-0x14]
    unsigned int v10;  // [bp-0x10]
    unsigned int v11;  // [bp-0xc]
    unsigned int v12;  // [bp-0x8]
    char v13;  // [bp-0x4]

    v12 = 4294967295;
    v11 = sub_1036ae58;
    v17 = _ccall(v14, v15, (unsigned int)v16, 0);
    v10 = *((int *)v17);
    v9 = g_1038e180 ^ &v13;
    v1 = v9;
    v18 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int **)v18) = &v10;
    v5 = 0;
    v0 = &v5;
    v3 = sub_10314d40(a8, &v4);
    v2 = v3;
    v12 = 0;
    sub_10350907(&v8, &v7, sub_10318a70(a0, &v8, &/* unsupported instruction */, &/* unsupported instruction */, v2));
    if (/* unsupported instruction */)
    {
        v6 = /* unsupported instruction */;
        /* unsupported instruction */
    }
    else
    {
        v6 = (double)nan;
        /* unsupported instruction */
    }
    v12 = 4294967295;
    sub_103130c0(&v4);
    if ((char)sub_10319590(&/* unsupported instruction */, &/* unsupported instruction */))
        *(a9) = *(a9) | 1;
    if (v7 == &v8 || v5)
    {
        *(a9) = *(a9) | 2;
    }
    else
    {
        if (/* unsupported instruction */)
        {
            /* unsupported instruction */
            /* unsupported instruction */
        }
        else
        {
            /* unsupported instruction */
            /* unsupported instruction */
        }
        *((int *)a10) = (/* unsupported instruction */ ? /* unsupported instruction */ : nan);
        /* unsupported instruction */
    }
    *(idx) = a2;
    idx[1] = a3;
    idx[2] = a4;
    v20 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int *)v20) = v10;
    return sub_10351225();
}
```

## `sub_103181f0` `0x103181f0`

_270 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[36];
    int field_24;
} struct_0;

extern unsigned int g_1038e180;

int sub_103181f0(int a0, unsigned int *idx, unsigned int a2, unsigned int a3, unsigned int a4, char a5, unsigned int a6, unsigned int a7, struct_0 *a8, unsigned int *a9, unsigned long long *a10)
{
    unsigned long v14;  // ldt
    unsigned long v15;  // gdt
    unsigned short v16;  // fs
    unsigned long v17;  // 4144
    unsigned long v18;  // 4161
    unsigned long v20;  // 4144
    char *v0;  // [bp-0x7c]
    unsigned int v1;  // [bp-0x78]
    int v2;  // [bp-0x74]
    int v3;  // [bp-0x70]
    struct_0 **v4;  // [bp-0x68]
    unsigned int v5;  // [bp-0x64]
    double v6;  // [bp-0x60], Other Possible Types: unsigned long
    char *v7;  // [bp-0x54], Other Possible Types: char
    char v8;  // [bp-0x50]
    unsigned int v9;  // [bp-0x14]
    unsigned int v10;  // [bp-0x10]
    unsigned int v11;  // [bp-0xc]
    unsigned int v12;  // [bp-0x8]
    char v13;  // [bp-0x4]

    v12 = 4294967295;
    v11 = sub_1036ae88;
    v17 = _ccall(v14, v15, (unsigned int)v16, 0);
    v10 = *((int *)v17);
    v9 = g_1038e180 ^ &v13;
    v1 = v9;
    v18 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int **)v18) = &v10;
    v5 = 0;
    v0 = &v5;
    v3 = sub_10314d40(a8, &v4);
    v2 = v3;
    v12 = 0;
    sub_1035096e(&v8, &v7, sub_10318a70(a0, &v8, &/* unsupported instruction */, &/* unsupported instruction */, v2));
    if (/* unsupported instruction */)
    {
        v6 = /* unsupported instruction */;
        /* unsupported instruction */
    }
    else
    {
        v6 = (double)nan;
        /* unsupported instruction */
    }
    v12 = 4294967295;
    sub_103130c0(&v4);
    if ((char)sub_10319590(&/* unsupported instruction */, &/* unsupported instruction */))
        *(a9) = *(a9) | 1;
    if (v7 == &v8 || v5)
    {
        *(a9) = *(a9) | 2;
    }
    else
    {
        if (/* unsupported instruction */)
        {
            /* unsupported instruction */
            /* unsupported instruction */
        }
        else
        {
            /* unsupported instruction */
            /* unsupported instruction */
        }
        *((int *)a10) = (/* unsupported instruction */ ? /* unsupported instruction */ : nan);
        /* unsupported instruction */
    }
    *(idx) = a2;
    idx[1] = a3;
    idx[2] = a4;
    v20 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int *)v20) = v10;
    return sub_10351225();
}
```

## `sub_10318300` `0x10318300`

_335 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[36];
    int field_24;
} struct_0;

extern unsigned int g_1038e180;

int sub_10318300(int a0, unsigned int *idx, unsigned int a2, unsigned int a3, unsigned int a4, char a5, unsigned int a6, unsigned int a7, struct_0 *a8, unsigned int *a9, unsigned int *a10)
{
    unsigned long v17;  // ldt
    unsigned long v18;  // gdt
    unsigned short v19;  // fs
    unsigned long v20;  // 4141
    unsigned long v21;  // 4158
    unsigned long v23;  // 4144
    unsigned int v0;  // [bp-0x64]
    unsigned int v1;  // [bp-0x60]
    unsigned int v2;  // [bp-0x5c]
    int v3;  // [bp-0x58]
    int v4;  // [bp-0x54]
    struct_0 **v5;  // [bp-0x4c]
    int v6;  // [bp-0x48]
    unsigned int v7;  // [bp-0x44]
    unsigned int v8;  // [bp-0x40]
    unsigned int v9;  // [bp-0x3c]
    char *v10;  // [bp-0x38], Other Possible Types: char
    char v11;  // [bp-0x34]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]
    char v16;  // [bp-0x4]

    v15 = 4294967295;
    v14 = sub_1036aeb8;
    v20 = _ccall(v17, v18, (unsigned int)v19, 0);
    v13 = *((int *)v20);
    v12 = g_1038e180 ^ &v16;
    v0 = v12;
    v21 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((unsigned int **)v21) = &v13;
    v7 = 0;
    v4 = sub_10314d40(a8, &v5);
    v3 = v4;
    v15 = 0;
    v6 = sub_103184e0(a0, &v11, &/* unsupported instruction */, &/* unsupported instruction */, 0x800, v3);
    v15 = 4294967295;
    sub_103130c0(&v5);
    v1 = sub_1035069a(&v11, &v10, v6, &v7);
    v2 = 0;
    v8 = v1;
    v9 = v2;
    if ((char)sub_10319590(&/* unsupported instruction */, &/* unsupported instruction */))
        *(a9) = *(a9) | 1;
    if (v10 == &v11 || v7)
        *(a9) = *(a9) | 2;
    else
        *(a10) = v8;
    *(idx) = a2;
    idx[1] = a3;
    idx[2] = a4;
    v23 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((unsigned int *)v23) = v13;
    return sub_10351225();
}
```

## `sub_10318450` `0x10318450`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10318450(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10318480(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_10318480` `0x10318480`

_84 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fb7c;

int sub_10318480(unsigned int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4139
    unsigned long v11;  // 4155
    int v12;  // eax
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036aee8;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    *((char **)v1) = &g_1038fb7c;
    v4 = 0;
    v4 = 4294967295;
    v12 = sub_10315390(v1);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_103184e0` `0x103184e0`

_1212 bytes. refs "0123456789abcdefABCDEF"_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
    char padding_c[8];
    char field_14;
} struct_0;

extern unsigned int g_1038e180;

int sub_103184e0(int a0, unsigned int a1, int a2, int a3, unsigned int a4, struct_0 **a5)
{
    unsigned long v26;  // ldt
    unsigned long v27;  // gdt
    char v36;  // al
    char *v38;  // eax
    char *v39;  // eax
    unsigned long v40;  // 4120
    unsigned short v28;  // fs
    unsigned long v29;  // 4140
    unsigned int v30;  // esi
    unsigned long v31;  // 4159
    char v32;  // al
    char v33;  // al
    char v35;  // al
    unsigned int v0;  // [bp-0x90]
    unsigned int v1;  // [bp-0x8c]
    char *v2;  // [bp-0x88]
    int v3;  // [bp-0x84]
    unsigned int v4;  // [bp-0x80]
    unsigned int v5;  // [bp-0x7c]
    char v6;  // [bp-0x75]
    unsigned int v7;  // [bp-0x74]
    struct_0 *v8;  // [bp-0x70]
    unsigned int v9;  // [bp-0x6c]
    unsigned int v10;  // [bp-0x68]
    char v11;  // [bp-0x61]
    char v12;  // [bp-0x60]
    int node;  // [bp-0x44]
    struct_0 v14;  // [bp-0x40]
    unsigned int v15;  // [bp-0x24]
    char v16;  // [bp-0x1f]
    char v17;  // [bp-0x1e]
    char v18;  // [bp-0x1d]
    unsigned int iter;  // [bp-0x1c]
    unsigned int v20;  // [bp-0x18]
    int v21;  // [bp-0x14]
    unsigned int v22;  // [bp-0x10]
    unsigned int v23;  // [bp-0xc]
    char v24;  // [bp-0x8], Other Possible Types: unsigned int
    char v25;  // [bp-0x4]

    v24 = 4294967295;
    v23 = sub_1036af20;
    v29 = _ccall(v26, v27, (unsigned int)v28, 0);
    v22 = *((int *)v29);
    v15 = g_1038e180 ^ &v25;
    v1 = v30;
    v0 = v15;
    v31 = _ccall(v26, v27, (unsigned int)v28, 0);
    *((unsigned int **)v31) = &v22;
    v20 = sub_10316fe0(a5);
    sub_103189f0(&v12);
    v24 = 0;
    v6 = (!sub_1031e920(&v12) ? 0 : (char)sub_103189d0());
    v16 = v6;
    v18 = sub_10318a60(48, 0, a0 + 8);
    iter = a1;
    if (!(char)sub_10319590(a2, a3))
    {
        v32 = sub_10319230();
        if (v32 == (char)sub_10318a60(43, 0, a0 + 8))
        {
            *((char *)iter) = 43;
            iter += 1;
            sub_10319260();
        }
        else
        {
            v33 = sub_10319230();
            if (v33 == (char)sub_10318a60(45, 0, a0 + 8))
            {
                *((char *)iter) = 45;
                iter += 1;
                sub_10319260();
            }
        }
    }
    a4 &= 0xe00;
    if (a4 == 0x400)
    {
        v5 = 8;
    }
    else
    {
        v4 = (a4 == 0x800 ? 16 : -(0 < a4) & 10);
        v5 = v4;
    }
    v10 = v5;
    v11 = 0;
    v17 = 0;
    if ((sub_103195b0(a2, a3) & 0xff) && (char)sub_10319230() == v18)
    {
        v11 = 1;
        sub_10319260();
        if ((char)sub_103195b0(a2, a3))
        {
            v35 = sub_10319230();
            if (v35 != (char)sub_10318a60(120, 0, a0 + 8))
            {
                v36 = sub_10319230();
                if (v36 == (char)sub_10318a60(88, 0, a0 + 8))
                    goto LABEL_103186ed;
            }
            else
            {
LABEL_103186ed:
                if (!v10 || v10 == 16)
                {
                    v10 = 16;
                    v11 = 0;
                    sub_10319260();
                    goto LABEL_1031871b;
                }
            }
        }
        if (!v10)
            v10 = 8;
    }
LABEL_1031871b:
    if (v10 && v10 != 10)
        v3 = (-(0 < v10 - 8) & 14) + 8;
    else
        v3 = 10;
    v21 = v3;
    sub_10317800(&v14, 1, v11);
    v24 = 1;
    node = 0;
    v9 = a1 + 31;
    while ((char)sub_103195b0(a2, a3))
    {
        *((char *)iter) = sub_10318a60(sub_10319230(a0 + 8));
        if (sub_10353a90("0123456789abcdefABCDEF", *((char *)iter), v21))
        {
            if ((v17 || *((char *)iter) != 48) && iter < v9)
            {
                iter += 1;
                v17 = 1;
            }
            v11 = 1;
            if (*((char *)sub_103189a0(node)) != 127)
            {
                v2 = sub_103189a0(node);
                *(v2) = *(v2) + 1;
            }
        }
        else if (!*((char *)sub_103189a0(node)) || !v16 || (char)sub_10319230() != v16)
        {
            break;
        }
        else
        {
            sub_103170f0(&v14, 1, 0);
            node += 1;
        }
        sub_10319260();
    }
    if (node)
    {
        if (*((char *)sub_103189a0(node)) > 0)
            node += 1;
        else
            v11 = 0;
    }
    v8 = (unsigned int)sub_102ec9a0(&v12);
    while (true)
    {
        if (!v11 || node <= 0 || v8->padding_0[0] == 127)
            break;
        node -= 1;
        if (node != 1 && !((v38 = (char *)sub_103189a0(node), (int)(char)v8->padding_0[0] == (int)*((char *)sub_103189a0(node)))) || !node && !((v39 = (char *)sub_103189a0(node), (int)(char)v8->padding_0[0] >= (int)*((char *)sub_103189a0(node)))))
        {
            v11 = 0;
        }
        else if (v8->padding_0[1] > 0)
        {
            v8 = &v8->padding_0[1];
        }
    }
    if (v11 && !v17)
    {
        *((char *)iter) = 48;
        iter += 1;
    }
    else if (!v11)
    {
        iter = a1;
    }
    *((char *)iter) = 0;
    v7 = v10;
    v24 = 0;
    sub_10314610(&v14);
    v24 = 4294967295;
    sub_10314610(&v12);
    v40 = _ccall(v26, v27, (unsigned int)v28, 0);
    *((unsigned int *)v40) = v22;
    return sub_10351225();
}
```

## `sub_10318860` `0x10318860`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10318860(void)
{
}
```

## `sub_103188cc` `0x103188cc`

_2 bytes. (leaf/helper — see body)_

```c
void sub_103188cc(void)
{
}
```

## `sub_103189a0` `0x103189a0`

_40 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

int sub_103189a0(struct_0 *a0, unsigned int a1)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    if (a1 > a0->field_14)
        sub_10353616(a0, &v1);
    return &sub_10314a50(a0)->padding_0[a1];
}
```

