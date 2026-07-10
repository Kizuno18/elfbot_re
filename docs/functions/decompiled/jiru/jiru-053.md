# elfbot.dll decompiled — jiru 0x103433e0..0x10345220

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_103433e0` `0x103433e0`

_117 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390b1c;

unsigned int [5] sub_103433e0(unsigned int *a0, unsigned int *index)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4154
    unsigned long v11;  // 4160
    unsigned int v0;  // [bp-0x18]
    unsigned int idx[5];  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_103709e8;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    idx = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    idx = a0;
    sub_1033fe70(idx, index);
    idx[0] = &g_10390b1c;
    idx[3] = index[3];
    idx[4] = index[4];
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return idx;
}
```

## `sub_10343460` `0x10343460`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10343460(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_103407b0(v0);
    if (((char)a1 & 1))
        sub_10350abd(v0);
    return v0;
}
```

## `sub_10343490` `0x10343490`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10343490(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10343700(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_103434c0` `0x103434c0`

_44 bytes. (leaf/helper — see body)_

```c
int sub_103434c0(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10343670(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_103434f0` `0x103434f0`

_77 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

int sub_103434f0(struct_0 *a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4)
{
    unsigned int v8[2];  // eax
    int v9[2];  // eax
    unsigned int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x2c]
    unsigned int v2;  // [bp-0x28]
    unsigned int v3;  // [bp-0x24]
    unsigned int v4;  // [bp-0x20]
    unsigned int v5;  // [bp-0x1c]
    char v6;  // [bp-0x14]
    char v7;  // [bp-0xc]

    v5 = a4;
    v4 = a3;
    v3 = a2;
    v2 = a1;
    v8 = sub_1031b790(a0, &v7);
    v1 = v8[1];
    v0 = v8[0];
    v9 = sub_1031b790(a0, &v6);
    return sub_10343860(v9[0], v9[1]);
}
```

## `sub_10343540` `0x10343540`

_27 bytes. (leaf/helper — see body)_

```c
int sub_10343540(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10343990(a1, 0, a0, &v1);
}
```

## `sub_10343560` `0x10343560`

_134 bytes. (leaf/helper — see body)_

```c
int sub_10343560(unsigned int a0, int a1, char a2)
{
    int v7;  // eax
    int v9;  // eax
    char v0;  // [bp-0x48]
    char v1;  // [bp-0x40]
    char v2;  // [bp-0x38]
    unsigned int v3;  // [bp-0x34]
    unsigned int v4;  // [bp-0x30]
    char v5;  // [bp-0x28]
    char v6;  // [bp-0x1c]

    v7 = sub_10336b20(a0);
    if (v7 < a1)
    {
        v4 = _INSERT(v7, 0, a2);
        v3 = a1 - sub_10336b20(a0);
        sub_103439d0(&v1);
        return sub_10343ab0(&v1);
    }
    v9 = sub_10336b20(a0);
    if (a1 >= v9)
        return v9;
    sub_103439d0(&v2);
    sub_103412a0(sub_10340ca0(a0, &v6), &v0, a1);
    return sub_10343a10(&v5);
}
```

## `sub_103435f0` `0x103435f0`

_29 bytes. (leaf/helper — see body)_

```c
int sub_103435f0(int a0, int a1, int a2)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10343b30(a1, a2, a0, &v1);
}
```

## `sub_10343610` `0x10343610`

_35 bytes. (leaf/helper — see body)_

```c
int sub_10343610(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return -(0 < (sub_10343c10(a1, a0, &v1) & 0xff)) + 1;
}
```

## `sub_10343640` `0x10343640`

_35 bytes. (leaf/helper — see body)_

```c
int sub_10343640(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return -(0 < (sub_10343c60(a1, a0, &v1) & 0xff)) + 1;
}
```

## `sub_10343670` `0x10343670`

_132 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390c00;
extern char g_10390c08;

unsigned int sub_10343670(int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4188
    unsigned long v11;  // 4192
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x1c]
    int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_10370a3f;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    *((char **)a0) = &g_10390c08;
    *((char **)(a0 + 20)) = &g_10390c00;
    v4 = 1;
    v4 = 0;
    v1 = (!a0 ? 0 : a0 + 20);
    sub_10313d70(v1);
    v4 = 4294967295;
    v12 = sub_103404b0(a0);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_10343700` `0x10343700`

_142 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390bdc;
extern char g_10390bec;
extern char g_10390bf4;

unsigned int sub_10343700(unsigned int idx)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4195
    unsigned long v11;  // 4199
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_10370a8f;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    *((char **)idx) = &g_10390bf4;
    *((char **)(idx + 20)) = &g_10390bec;
    *((char **)(idx + 40)) = &g_10390bdc;
    v4 = 1;
    v4 = 0;
    v1 = (!idx ? 0 : idx + 40);
    sub_10313bb0(v1);
    v4 = 4294967295;
    v12 = sub_10343670(idx);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_10343790` `0x10343790`

_148 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10343790(int a0)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4137
    unsigned long v13;  // 4151
    unsigned long v14;  // 4117
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_10370abb;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v4 = *((int *)v12);
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v4;
    v2 = sub_10350a53(44, g_1038e180 ^ &v7);
    v6 = 0;
    v1 = (!v2 ? 0 : sub_103432a0(v2, a0 - 40));
    v3 = v1;
    v6 = 4294967295;
    v0 = (!v3 ? 0 : v3 + 40);
    v14 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v14) = v4;
    return v0;
}
```

## `sub_10343830` `0x10343830`

_42 bytes. (leaf/helper — see body)_

```c
extern int g_1039fe84;

int sub_10343830(int a0)
{
    char v0;  // [bp-0x30]

    sub_103432a0(&v0, a0 - 40);
    return sub_103533ea(&v0, &g_1039fe84);
}
```

## `sub_10343860` `0x10343860`

_298 bytes. (leaf/helper — see body)_

```c
int sub_10343860(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4)
{
    unsigned int v25[2];  // eax
    unsigned int v26;  // eax
    unsigned int v28[2];  // eax
    unsigned int v0;  // [bp-0x70]
    unsigned int v1;  // [bp-0x6c]
    unsigned int v2;  // [bp-0x68]
    int v3;  // [bp-0x64], Other Possible Types: unsigned int
    int v4;  // [bp-0x60], Other Possible Types: unsigned int
    unsigned int v5;  // [bp-0x54]
    unsigned int v6;  // [bp-0x50]
    char v7;  // [bp-0x4c]
    unsigned int v8;  // [bp-0x44]
    unsigned int v9;  // [bp-0x40]
    unsigned int v10;  // [bp-0x3c]
    unsigned int v11;  // [bp-0x38]
    unsigned int v12;  // [bp-0x34]
    unsigned int v13;  // [bp-0x30]
    unsigned int v14;  // [bp-0x2c]
    unsigned int v15;  // [bp-0x28]
    char v16;  // [bp-0x24]
    unsigned int v17;  // [bp-0x1c]
    unsigned int v18;  // [bp-0x18]
    unsigned int v19;  // [bp-0x14]
    unsigned int v20;  // [bp-0x10]
    unsigned int v21;  // [bp-0xc]
    unsigned int v22;  // [bp-0x8]
    char v23;  // [bp+0x14]
    unsigned int v24;  // [bp+0x1c]

    if (!(char)sub_10343c10(&v24, a0))
    {
        v12 = a1;
        v13 = a2;
        v10 = a3;
        v11 = a4;
        v28 = sub_1031b6e0(a0, &v7);
        v8 = v28[0];
        v9 = v28[1];
        v5 = a1;
        v6 = a2;
        v4 = sub_1031ba20(&v24, &v23);
        v3 = sub_10334250(&v23);
        v2 = v13;
        v1 = v12;
        v2 = sub_1031b9f0(v10, v11);
        v1 = v9;
        v0 = v8;
        sub_10343ca0(sub_1031b9f0(v5, v6));
        return a0;
    }
    v21 = a1;
    v22 = a2;
    v19 = a3;
    v20 = a4;
    v25 = sub_1031b6e0(a0, &v16);
    v17 = v25[0];
    v18 = v25[1];
    v14 = a1;
    v15 = a2;
    v4 = v22;
    v3 = v21;
    v26 = sub_1031b9f0(v19, v20);
    v3 = v18;
    v2 = v17;
    sub_103148c0(a0, sub_1031b9f0(v14, v15), v26);
    return a0;
}
```

## `sub_10343990` `0x10343990`

_62 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

void* sub_10343990(struct_0 *a0, unsigned int a1, char a2)
{
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    if (a1 > v0->field_14)
        return sub_103170f0(v0, a1 - v0->field_14, a2);
    return sub_103148c0(v0, a1, 4294967295);
}
```

## `sub_103439d0` `0x103439d0`

_64 bytes. (leaf/helper — see body)_

```c
int sub_103439d0(int *a0, int a1)
{
    char v0;  // [bp-0x10]

    sub_10340ca0(a0, &v0);
    if (*(a0) > 0)
    {
        sub_10341660(&v0, *(a0));
        sub_103413d0(a1, &v0);
    }
    else
    {
        sub_103413d0(a1, &v0);
    }
    return a1;
}
```

## `sub_10343a10` `0x10343a10`

_151 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10343a10(unsigned int a0, unsigned int a1)
{
    char v0;  // [bp-0x70]
    char v1;  // [bp-0x64]
    char v2;  // [bp-0x58]
    char v3;  // [bp-0x44]
    char v4;  // [bp-0x38]
    char v5;  // [bp-0x20]
    int v6;  // [bp-0x14]
    char v7;  // [bp-0x10]
    char v8;  // [bp+0x8]
    char v9;  // [bp+0x14]

    v6 = sub_10344040(sub_10340ca0(a0, &v5));
    sub_103413d0(&v2, &v8);
    sub_103439d0(a0, &v1);
    sub_103413d0(&v0, &v9);
    sub_10346540(&v7);
    sub_10343f30(sub_10344040(sub_10340ca0(a0, &v4)));
    sub_103412a0(sub_10340ca0(a0, &v3), a1, v6);
    return a1;
}
```

## `sub_10343ab0` `0x10343ab0`

_117 bytes. (leaf/helper — see body)_

```c
int sub_10343ab0(int a0, char a1, unsigned int a1, unsigned int a2, unsigned int a3)
{
    char *v0;  // [bp-0x5c]
    char v1;  // [bp-0x50]
    char *v2;  // [bp-0x44]
    char v3;  // [bp-0x40]
    unsigned int v4;  // [bp-0x34]
    char v5;  // [bp-0x2c]
    char v6;  // [bp-0x1c]
    int v7;  // [bp-0x8]
    char v9;  // [bp+0x14]

    v4 = a3;
    sub_103413d0(&v3, &/* unsupported instruction */);
    v7 = sub_10343e30(v3);
    v2 = &v9;
    v0 = &v6;
    sub_103412a0(sub_10340ca0(a0, &v6), &v1, v7 + a3);
    sub_103412a0(sub_10340ca0(a0, &v5), &v0, v7);
    return sub_103465c0();
}
```

## `sub_10343b30` `0x10343b30`

_222 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    int field_4;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
    int field_4;
} struct_1;

extern unsigned int g_1038e180;

void sub_10343b30(void* a0, unsigned int a1, unsigned int *a2)
{
    unsigned long v13;  // ldt
    unsigned long v14;  // gdt
    unsigned short v15;  // fs
    unsigned long v16;  // 4140
    unsigned long v17;  // 4157
    struct_0 *v18;  // eax
    struct_0 *v19;  // eax
    int v20[2];  // eax
    unsigned long v21;  // 4114
    unsigned int v0;  // [bp-0xb0]
    char *v1;  // [bp-0xac]
    unsigned int v2;  // [bp-0xa8]
    char v3;  // [bp-0xa0]
    struct_1 v4;  // [bp-0x98]
    char v5;  // [bp-0x90]
    char v6;  // [bp-0x88]
    unsigned int v7[27];  // [bp-0x80]
    unsigned int v8;  // [bp-0x14]
    unsigned int v9;  // [bp-0x10]
    unsigned int v10;  // [bp-0xc]
    unsigned int v11;  // [bp-0x8]
    char v12;  // [bp-0x4]

    v11 = 4294967295;
    v10 = sub_10370ae8;
    v16 = _ccall(v13, v14, (unsigned int)v15, 0);
    v9 = *((int *)v16);
    v8 = g_1038e180 ^ &v12;
    v2 = v8;
    v17 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int **)v17) = &v9;
    sub_10341320(v7, a2);
    v11 = 0;
    v18 = sub_10330670(a0, &v6);
    v19 = sub_103414f0(a0, &v5);
    sub_10340ce0(a0, &v4, v19->field_0, v19->field_4, v18->field_0, v18->field_4);
    v1 = v7;
    v0 = a1;
    v20 = sub_103414f0(a0, &v3);
    sub_10344010(v20[0], v20[1]);
    v11 = 4294967295;
    sub_103407b0(v7);
    v21 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int *)v21) = v9;
    sub_10351225();
    return;
}
```

## `sub_10343c10` `0x10343c10`

_65 bytes. (leaf/helper — see body)_

```c
int sub_10343c10(unsigned int *a0, unsigned int a1)
{
    unsigned int v0[2];  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    if (v0[0] != 4294967294 && (!v0[0] || v0[0] != *((int *)a1)))
        sub_10353616();
    return _INSERT(a1, 0, v0[1] == *((int *)(a1 + 4)));
}
```

## `sub_10343c60` `0x10343c60`

_62 bytes. (leaf/helper — see body)_

```c
int sub_10343c60(unsigned int *a0, unsigned int a1)
{
    unsigned int v0[2];  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    if (v0[0] != 4294967294 && (!v0[0] || v0[0] != *((int *)a1)))
        sub_10353616();
    return -(-(v0[1] < *((int *)(a1 + 4))));
}
```

## `sub_10343ca0` `0x10343ca0`

_389 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

struct_0 * sub_10343ca0(struct_0 *idx, unsigned int a1, int a2, unsigned int a3, int a4)
{
    struct_0 *v2;  // eax
    struct_0 *v3;  // eax
    struct_0 *v4;  // eax
    struct_0 *v5;  // eax
    struct_0 *v6;  // eax
    unsigned int v0;  // [bp-0xc]
    int v1;  // [bp-0x8]

    if (sub_10314c60(idx, a3))
        return sub_1031ba90(idx, a1, a2, idx, a3 - (char *)sub_10314a50(idx), a4);
    if (*((int *)&idx->padding_8[12]) < a1)
        sub_103503dd();
    if (*((int *)&idx->padding_8[12]) - a1 < a2)
        a2 = *((int *)&idx->padding_8[12]) - a1;
    if (4294967295 - a4 <= *((int *)&idx->padding_8[12]) - a2)
        sub_1035039e();
    v1 = *((int *)&idx->padding_8[12]) - a2 - a1;
    if (a4 < a2)
    {
        v2 = sub_10314a50(idx);
        v3 = sub_10314a50(idx);
        sub_103159d0(&v3->padding_0[a1 + a4], idx->field_18 - a1 - a4, &v2->padding_0[a1 + a2], v1);
    }
    if (a4 > 0 || a2 > 0)
    {
        v0 = *((int *)&idx->padding_8[12]) + a4 - a2;
        if ((char)sub_103149b0(idx, v0, 0))
        {
            if (a2 < a4)
            {
                v4 = sub_10314a50(idx);
                v5 = sub_10314a50(idx);
                sub_103159d0(&v5->padding_0[a1 + a4], idx->field_18 - a1 - a4, &v4->padding_0[a1 + a2], v1);
            }
            v6 = sub_10314a50(idx);
            sub_10313350(&v6->padding_0[a1], idx->field_18 - a1, a3, a4);
            sub_10314960(idx, v0);
        }
    }
    return idx;
}
```

## `sub_10343e30` `0x10343e30`

_246 bytes. (leaf/helper — see body)_

```c
int sub_10343e30(unsigned int *a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4)
{
    unsigned int v10;  // esi
    unsigned int v11;  // eax
    char v0;  // [bp-0x7c]
    char v1;  // [bp-0x70]
    char v2;  // [bp-0x64]
    unsigned int v3;  // [bp-0x54]
    unsigned int v4;  // [bp-0x4c]
    char v5;  // [bp-0x44]
    char v6;  // [bp-0x38]
    char v7;  // [bp-0x20]
    char v8;  // [bp-0x14]
    int v9;  // [bp-0x8]

    v4 = v10;
    v9 = sub_10344040(sub_10340ca0(a0, &v7));
    if (!a4)
        return v9;
    v11 = sub_10344060();
    if (v11 - sub_10336b20(a0) < a4)
    {
        sub_103440b0();
        return v9;
    }
    v3 = 0;
    sub_10344130(sub_103440a0(sub_10336b20(a0) + a4));
    if (sub_10336b20(a0))
    {
        sub_103439d0(a0, &v8);
        *(a0) = *(a0) + a4;
        sub_103439d0(a0, &v2);
        sub_103413d0(&v1, &v8);
        sub_103412a0(sub_10340ca0(a0, &v6), &v0, v9);
        sub_10346600(&v5);
        return v9;
    }
    *(a0) = *(a0) + a4;
    return v9;
}
```

## `sub_10343f30` `0x10343f30`

_214 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10343f30(int *a0, int a1)
{
    int v6[2];  // eax
    int v7[2];  // eax
    unsigned int *v8;  // eax
    unsigned int v9;  // eax
    unsigned int *v0;  // [bp-0x30], Other Possible Types: int
    char v1;  // [bp-0x28]
    char v2;  // [bp-0x20]
    char v3;  // [bp-0x18]
    char v4;  // [bp-0x10]
    int v5;  // [bp-0x8]

    if (sub_10344060() < a1)
        sub_103440b0();
    v5 = sub_103440a0(a1);
    if (v5 < sub_103441d0())
    {
        v6 = sub_10330670(a0 + 1, &v4);
        sub_103414f0(a0 + 1, &v3);
        v7 = sub_103442e0(&v2, v5, v6[0], v6[1], v0);
        sub_10344240(&v1, v7[0], v7[1]);
    }
    *(a0) = a1;
    a1 = a1 % 32;
    if (a1 <= 0)
        return a1 / 32;
    v8 = sub_10344210(v5 - 1);
    v0 = v8;
    v9 = (1 << ((char)a1 & 31)) - 1 & *(v0);
    *(v8) = v9;
    return v9;
}
```

## `sub_10344010` `0x10344010`

_37 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    unsigned int field_8;
    unsigned int field_c;
} struct_0;

void sub_10344010(struct_0 *a0, unsigned int a1, int a2, int a3, int a4)
{
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_10340d50(v0, a1, a2, a3, a4);
    return;
}
```

## `sub_10344040` `0x10344040`

_25 bytes. (leaf/helper — see body)_

```c
int sub_10344040(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_103442b0(a1, a0, &v1);
}
```

## `sub_10344060` `0x10344060`

_57 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10344060(int a0)
{
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0x8]

    v1 = (unsigned int)sub_1033f430(a0 + 4);
    v0 = (v1 < 0x7ffffff ? v1 * 32 : 4294967295);
    return v0;
}
```

## `sub_103440a0` `0x103440a0`

_14 bytes. (leaf/helper — see body)_

```c
unsigned int sub_103440a0(unsigned int a0)
{
    return a0 + 31 >> 5;
}
```

## `sub_103440b0` `0x103440b0`

_116 bytes. refs "vector<bool> too long"_

```c
extern unsigned int g_1038e180;
extern int g_1039ce9c;

void sub_103440b0(void)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4138
    unsigned long v13;  // 4152
    unsigned int v14;  // ecx
    unsigned long v15;  // 4113
    unsigned int v0;  // [bp-0x5c]
    unsigned int v1;  // [bp-0x58]
    char v2;  // [bp-0x54]
    char v3;  // [bp-0x38]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_10370b18;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v4 = *((int *)v12);
    v0 = g_1038e180 ^ &v7;
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v4;
    v1 = v14;
    sub_10314590(&v2, "vector<bool> too long");
    v6 = 0;
    sub_10331a40(&v3, &v2);
    sub_103533ea(&v3, &g_1039ce9c);
    v6 = 4294967295;
    sub_10314610(&v2);
    v15 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v15) = v4;
    return;
}
```

## `sub_10344130` `0x10344130`

_153 bytes. (leaf/helper — see body)_

```c
int sub_10344130(unsigned int a0, int a1)
{
    int v7[2];  // eax
    int v8;  // eax
    int v9[2];  // eax
    int v10[2];  // eax
    unsigned int v0;  // [bp-0x38]
    char v1;  // [bp-0x2c]
    char v2;  // [bp-0x24]
    char v3;  // [bp-0x1c]
    char v4;  // [bp-0x14]
    char v5;  // [bp-0xc]
    char v6;  // [bp+0x8]

    if (sub_103441d0(a0) < a1)
    {
        v0 = a1 - sub_103441d0(&v6);
        v7 = sub_10330670(a0, &v5);
        return sub_10344320(v7[0], v7[1]);
    }
    v8 = sub_103441d0();
    if (a1 >= v8)
        return v8;
    v9 = sub_10330670(a0, &v4);
    sub_103414f0(a0, &v3);
    v10 = sub_103442e0(&v2, a1, v9[0], v9[1], a0);
    return sub_10344240(&v1, v10[0], v10[1]);
}
```

## `sub_103441d0` `0x103441d0`

_52 bytes. (leaf/helper — see body)_

```c
int sub_103441d0(unsigned int *a0)
{
    int v0;  // [bp-0xc]

    v0 = (!a0[1] ? 0 : a0[2] - a0[1] >> 2);
    return v0;
}
```

## `sub_10344210` `0x10344210`

_43 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

int sub_10344210(struct_0 *a0, int a1)
{
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    if (a1 >= sub_103441d0(v0))
        sub_10353616();
    return v0->field_4 + a1 * 4;
}
```

## `sub_10344240` `0x10344240`

_105 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    unsigned int field_0;
    int field_4;
} struct_1;

typedef struct struct_0 {
    char padding_0[8];
    int field_8;
} struct_0;

struct_1 * sub_10344240(struct_0 *a0, struct_1 *a1, unsigned int a2, int a3, char a4, int a5)
{
    int v0;  // [bp-0x8]

    if ((char)sub_103416a0(&a2, &/* unsupported instruction */))
    {
        v0 = sub_10346680(a5, a0->field_8, a3);
        sub_1033e420(a0, v0, a0->field_8);
        a0->field_8 = v0;
    }
    a1->field_0 = a2;
    a1->field_4 = a3;
    return a1;
}
```

## `sub_103442b0` `0x103442b0`

_43 bytes. (leaf/helper — see body)_

```c
int sub_103442b0(unsigned int *a0, unsigned int *a1)
{
    return (a0[1] - a1[1] >> 2) * 32 + a0[2] - a1[2];
}
```

## `sub_103442e0` `0x103442e0`

_57 bytes. (leaf/helper — see body)_

```c
unsigned int [2] sub_103442e0(int *a0, unsigned int *a1, int a2)
{
    unsigned int v1[2];  // eax
    unsigned int v2;  // edx
    char v0;  // [bp+0x0]

    v1 = sub_10344660(a2, a0, *(a0), a0[1], &v0);
    v2 = v1[1];
    *(a1) = v1[0];
    a1[1] = v2;
    return a1;
}
```

## `sub_10344320` `0x10344320`

_711 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    unsigned int field_8;
    unsigned int field_c;
} struct_0;

extern unsigned int g_1038e180;

struct_0 * sub_10344320(struct_0 *idx, unsigned int a1, int a2, int a3, unsigned int *a4)
{
    unsigned long v13;  // ldt
    unsigned long v14;  // gdt
    unsigned long v23;  // 4119
    unsigned short v15;  // fs
    unsigned long v16;  // 4148
    unsigned long v17;  // 4170
    int v18;  // edi
    int v19;  // esi
    int v20;  // ebx
    struct_0 *v21;  // eax
    unsigned int v22;  // eax
    int v0;  // [bp-0x68]
    unsigned int v1;  // [bp-0x40]
    int v2;  // [bp-0x30]
    unsigned int v3;  // [bp-0x28]
    int v4;  // [bp-0x24]
    int v5;  // [bp-0x20]
    struct_0 *v6;  // [bp-0x1c], Other Possible Types: int
    unsigned int v7;  // [bp-0x18]
    char *v8;  // [bp-0x14], Other Possible Types: struct_0 *
    unsigned int v9;  // [bp-0x10]
    unsigned int v10;  // [bp-0xc]
    unsigned int v11;  // [bp-0x8]
    char v12;  // [bp-0x4]

    v11 = 4294967295;
    v10 = sub_10370b40;
    v16 = _ccall(v13, v14, (unsigned int)v15, 0);
    v9 = *((int *)v16);
    v8 = idx;
    v1 = g_1038e180 ^ &v12;
    v17 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int **)v17) = &v9;
    v8 = &v1;
    v7 = *(a4);
    v21 = sub_10344680(g_1038e180 ^ &v12, v18, v19, v20);
    v6 = v21;
    if (a3)
    {
        v22 = (unsigned int)sub_1033f430(idx);
        if (v22 - sub_103441d0(idx) < a3)
        {
            v21 = (unsigned int)sub_1033f450();
        }
        else if (v6 < sub_103441d0(idx) + a3)
        {
            v2 = ((unsigned int)sub_1033f430(idx) - (v6 >> 1) < v6 ? 0 : (struct struct_0 *)&v6->padding_0[v6 >> 1]);
            v6 = v2;
            if (v6 < sub_103441d0(idx) + a3)
                v6 = sub_103441d0(idx) + a3;
            v4 = sub_1033f4d0(idx, v6);
            v5 = v4;
            v11 = 0;
            v5 = sub_103466f0(idx->field_4, a2, v4);
            v5 = sub_103446c0(v5, a3, &v7);
            sub_103466f0(a2, idx->field_8, v5);
            v11 = 4294967295;
            a3 += sub_103441d0(idx);
            if (idx->field_4)
            {
                sub_1033e420(idx, idx->field_4, idx->field_8);
                v0 = idx->field_c - idx->field_4 >> 2;
                sub_1033e3d0(idx, idx->field_4);
            }
            idx->field_c = v4 + v6 * 4;
            v21 = idx;
            v21->field_8 = v4 + a3 * 4;
            idx->field_4 = v4;
        }
        else if (idx->field_8 - a2 >> 2 < a3)
        {
            sub_103466f0(a2, idx->field_8, a2 + a3 * 4);
            v11 = 2;
            sub_103446c0(idx->field_8, a3 - (idx->field_8 - a2 >> 2), &v7);
            v11 = 4294967295;
            idx->field_8 = idx->field_8 + a3 * 4;
            v21 = sub_10346720(a2, idx->field_8 - a3 * 4, &v7);
        }
        else
        {
            v3 = idx->field_8;
            idx->field_8 = sub_103466f0(v3 - a3 * 4, v3, idx->field_8);
            sub_10346750(a2, v3 - a3 * 4, v3);
            v21 = sub_10346720(a2, a2 + a3 * 4, &v7);
        }
    }
    v23 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int *)v23) = v9;
    return v21;
}
```

## `sub_10344456` `0x10344456`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10344456(void)
{
    sub_10344459();
    return;
}
```

## `sub_10344459` `0x10344459`

_51 bytes. (leaf/helper — see body)_

```c
int sub_10344459(void)
{
    int v6;  // eax
    unsigned int v0;  // [bp-0x4]
    int v2;  // [bp+0xfffdc]
    int v3;  // [bp+0xfffe4]
    unsigned int v4;  // [bp+0xfffec]
    unsigned int v5;  // [bp+0x100000]

    sub_1033e420(v2, v3, v6);
    v0 = v4;
    sub_1033e3d0(v2, v3);
    sub_103533ea(0, 0);
    v5 = 4294967295;
    return;
}
```

## `sub_1034456b` `0x1034456b`

_53 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
} struct_0;

extern char g_103445a7;

int sub_1034456b(void)
{
    struct_0 *v1;  // [bp+0xfffdc]
    unsigned int v2;  // [bp+0x100000]
    unsigned int v3;  // [bp+0x100010]
    unsigned int v4;  // [bp+0x100014]

    sub_1033e420(v1, v3 + v4 * 4, v1->field_8 + v4 * 4);
    sub_103533ea(0, 0);
    v2 = 4294967295;
    return &g_103445a7;
}
```

## `sub_10344660` `0x10344660`

_28 bytes. (leaf/helper — see body)_

```c
int sub_10344660(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_103446f0(a1, a0, &v1);
    return a0;
}
```

## `sub_10344680` `0x10344680`

_52 bytes. (leaf/helper — see body)_

```c
int sub_10344680(unsigned int *a0)
{
    int v0;  // [bp-0xc]

    v0 = (!a0[1] ? 0 : a0[3] - a0[1] >> 2);
    return v0;
}
```

## `sub_103446c0` `0x103446c0`

_46 bytes. (leaf/helper — see body)_

```c
int sub_103446c0(int a0, int a1, int a2, int a3)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_103467c0(a1, a2, a3, a0, a0, &v1);
    return a1 + a2 * 4;
}
```

## `sub_103446f0` `0x103446f0`

_96 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_1 *field_0;
    unsigned int field_4;
} struct_0;

typedef struct struct_1 {
    char padding_0[4];
    unsigned int field_4;
    unsigned int field_8;
} struct_1;

struct_0 * sub_103446f0(struct_0 *idx, unsigned int a1)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = idx;
    if (!idx->field_0)
        sub_10353616(idx, &v1);
    if (idx->field_4 + a1 * 4 > idx->field_0->field_8 || idx->field_4 + a1 * 4 < idx->field_0->field_4)
        sub_10353616();
    idx->field_4 = idx->field_4 + a1 * 4;
    return idx;
}
```

## `sub_10344750` `0x10344750`

_45 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_10344750(unsigned int *a0, unsigned int *a1)
{
    unsigned int *v0;  // [bp-0xc]
    unsigned int *v1;  // [bp-0x8]

    v0 = (*(a0) < *(a1) ? a1 : a0);
    v1 = v0;
    return v1;
}
```

## `sub_10344780` `0x10344780`

_84 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    char padding_4[88];
    char field_5c;
    char padding_5d[3];
    unsigned int field_60;
} struct_0;

char sub_10344780(struct_0 *a0, char a1)
{
    struct_0 *idx;  // [bp-0x8]

    idx = a0;
    idx = a0;
    idx->field_0 = 4294967295;
    *((unsigned int *)&idx->field_5c) = (unsigned int)sub_103411a0();
    idx->field_60 = 0;
    sub_10343540(idx->padding_4, 0);
    return sub_103430c0(&idx->padding_4[56], a1);
}
```

## `sub_103447e0` `0x103447e0`

_83 bytes. (leaf/helper — see body)_

```c
unsigned int [2] sub_103447e0(unsigned int *a0, int a1, unsigned int a2, unsigned int a3)
{
    int v1;  // edx
    char v0;  // [bp+0x14]

    while ((char)sub_10343610(&a2, &v0) && (v1 = (int)_INSERT(0, 0, *((char *)sub_10334250(&a2))), (char)sub_10344840(a1, _INSERT(0, 0, *((char *)sub_10334250(&a2))))))
    {
        sub_10342b10(&a2);
    }
    *(a0) = a2;
    a0[1] = a3;
    return a0;
}
```

## `sub_10344840` `0x10344840`

_19 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

int sub_10344840(struct_0 *a0, char a1)
{
    return sub_10315ea0(a0, 4, a1);
}
```

## `sub_10344860` `0x10344860`

_178 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int [2] sub_10344860(unsigned int *a0, unsigned int *a1, int a2, unsigned int *a3, unsigned int a4)
{
    char *v4;  // eax
    int v5;  // eax
    unsigned int v0;  // [bp-0x14]
    char v1;  // [bp-0xd]
    struct_0 v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    sub_10340a20(&v2);
    *(a3) = 0;
    v2 = (struct_0)*(a1);
    v3 = a1[1];
    while ((char)sub_10343610(&v2, a2) && (char)sub_10344840(a4, *((char *)sub_10334250(&v2))))
    {
        v0 = 0;
        v4 = sub_10334250(&v2);
        v5 = _INSERT(v4, 0, *(v4));
        v1 = sub_10344920(a4, v5);
        *(a3) = *(a3) * 10;
        *(a3) = v1 + *(a3) - 48;
        sub_10342b10(&v2);
    }
    *((struct struct_0 *)&a0) = v2;
    a0[1] = v3;
    return a0;
}
```

## `sub_10344920` `0x10344920`

_32 bytes. (leaf/helper — see body)_

```c
int sub_10344920(unsigned int a0, char a1, char a2)
{
    int v1;  // eax
    int v2;  // ecx
    char v0;  // [bp+0x0]

    v1 = _INSERT(0, 0, a2);
    v2 = _INSERT(0, 0, a1);
    sub_10337e90(a0);
    return sub_10344940(v2, v1, &v0);
}
```

## `sub_10344940` `0x10344940`

_34 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[36];
    struct struct_1 *field_24;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

char sub_10344940(struct_0 **a0, char a1, char a2)
{
    unsigned int v2;  // eax
    unsigned int v3;  // ecx
    struct_0 **v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    v2 = _INSERT(0, 0, a2);
    v3 = _INSERT(a0, 0, a1);
    return *(a0)->field_24(v3, v2, a0, &v1);
}
```

## `sub_10344970` `0x10344970`

_146 bytes. (leaf/helper — see body)_

```c
unsigned int [2] sub_10344970(unsigned int *a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5)
{
    unsigned int v3[2];  // eax
    char *v4;  // eax
    char v5;  // al
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2[2];  // [bp-0xc]

    sub_10342b10(&/* unsupported instruction */);
    v1 = a4;
    v0 = a3;
    v3 = sub_103447e0(v2, a5, a1, a2);
    a1 = v3[0];
    a2 = v3[1];
    if ((char)sub_10343610(&a1, &/* unsupported instruction */))
    {
        v4 = sub_10334250(&a1);
        v5 = sub_10314d20(sub_10337e90(a5), 36);
        if (*(v4) == v5)
            sub_10342b10(&a1);
    }
    *(a0) = a1;
    a0[1] = a2;
    return a0;
}
```

## `sub_10344a10` `0x10344a10`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10344a10(unsigned int a0, int a1)
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
    sub_10346d80(a1, g_1038e180 ^ &v2, 0, v8, sub_10370b79, -1, &v3);
    v11 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v11) = v8;
    return a0;
}
```

## `sub_10344a70` `0x10344a70`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10344a70(unsigned int a0, int a1)
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
    sub_10346e00(a1, g_1038e180 ^ &v2, 0, v8, sub_10370bb9, -1, &v3);
    v11 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v11) = v8;
    return a0;
}
```

## `sub_10344ad0` `0x10344ad0`

_141 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern int g_103a0274;

unsigned int sub_10344ad0(int a0)
{
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // fs
    unsigned long v13;  // 4137
    unsigned long v14;  // 4151
    unsigned int v15;  // eax
    unsigned long v16;  // 4113
    int v0;  // [bp-0x74]
    unsigned int v1;  // [bp-0x70]
    int v2;  // [bp-0x6c]
    int v3;  // [bp-0x68]
    char v4;  // [bp-0x64]
    char v5;  // [bp-0x38]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]
    char v9;  // [bp-0x4]

    v8 = 4294967295;
    v7 = sub_10370be8;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v6 = *((int *)v13);
    v1 = g_1038e180 ^ &v9;
    v14 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v14) = &v6;
    v0 = a0;
    sub_10334530();
    v3 = sub_103476b0(&v5, a0);
    v2 = v3;
    v8 = 0;
    sub_10347710(&v4, v2);
    sub_103533ea(&v4, &g_103a0274);
    v8 = 4294967295;
    v15 = sub_10346ed0(&v4, &g_103a0274);
    v16 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v16) = v6;
    return v15;
}
```

## `sub_10344b60` `0x10344b60`

_13 bytes. (leaf/helper — see body)_

```c
void sub_10344b60(unsigned int a0)
{
    char v0;  // [bp+0x0]

    sub_10346d00(&v0);
    return;
}
```

## `sub_10344b70` `0x10344b70`

_1624 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[96];
    unsigned int field_60;
} struct_0;

extern unsigned int g_1038e180;

void sub_10344b70(int a0, struct_0 *idx, unsigned int a2, unsigned int a3, int a4)
{
    unsigned long v42;  // ldt
    unsigned long v43;  // gdt
    int v53;  // eax
    char v54;  // al
    char v55;  // al
    char *v56;  // eax
    unsigned long v58;  // 4115
    unsigned short v44;  // fs
    unsigned long v45;  // 4142
    unsigned long v46;  // 4158
    int v47;  // esi
    char v48;  // al
    char v49;  // al
    unsigned int *v50;  // eax
    int v51;  // ecx
    char *v0;  // [bp-0x138]
    int v1;  // [bp-0x134]
    char *v2;  // [bp-0x128]
    int v3;  // [bp-0x124]
    char *v4;  // [bp-0x108]
    char *v5;  // [bp-0x104]
    char *v6;  // [bp-0x100]
    char *v7;  // [bp-0xfc]
    int v8;  // [bp-0xf8]
    char *v9;  // [bp-0xf4]
    char *v10;  // [bp-0xf0]
    char v11;  // [bp-0xe9]
    char *v12;  // [bp-0xe8]
    int v13;  // [bp-0xe4]
    unsigned int v14;  // [bp-0xe0]
    unsigned int v15;  // [bp-0xdc]
    unsigned int v16;  // [bp-0xd8]
    unsigned int v17;  // [bp-0xd4]
    unsigned int v18;  // [bp-0xd0]
    unsigned int v19;  // [bp-0xcc]
    int v20;  // [bp-0xc8]
    unsigned int i;  // [bp-0xc4]
    char *v22;  // [bp-0xc0]
    unsigned int v23;  // [bp-0xbc]
    char v24;  // [bp-0xb8]
    char v25;  // [bp-0xb0]
    char v26;  // [bp-0x75]
    char *v27;  // [bp-0x74], Other Possible Types: unsigned int
    unsigned int v28;  // [bp-0x70]
    char v29;  // [bp-0x69]
    char *v30;  // [bp-0x68]
    unsigned int v31;  // [bp-0x64]
    int v32;  // [bp-0x60]
    char v33;  // [bp-0x5a]
    char v34;  // [bp-0x59]
    char v35;  // [bp-0x58]
    char v36;  // [bp-0x50]
    unsigned int v37;  // [bp-0x14]
    unsigned int v38;  // [bp-0x10]
    unsigned int v39;  // [bp-0xc]
    char v40;  // [bp-0x8], Other Possible Types: unsigned int
    char v41;  // [bp-0x4]

    v40 = 4294967295;
    v39 = sub_10370c23;
    v45 = _ccall(v42, v43, (unsigned int)v44, 0);
    v38 = *((int *)v45);
    v46 = _ccall(v42, v43, (unsigned int)v44, 0);
    *((unsigned int **)v46) = &v38;
    sub_103470c0(a3, 1, g_1038e180 ^ &v41, v47);
    v40 = 0;
    v13 = (!&v35 ? NULL : &(&v36)[*((int *)(v36 + 4))]);
    sub_10347290(v13, a4);
    v12 = (!&v35 ? NULL : &v36);
    v3 = a0;
    v2 = v12;
    sub_10334530();
    v32 = sub_10315ef0(&(&v36)[*((int *)(v36 + 4))]);
    v34 = (v32 & 0x100);
    v37 = sub_103451d0();
    if (v34 && v37)
        v11 = 1;
    else
        v11 = 0;
    v33 = v11;
    sub_10343540(a2, 0);
    if (!v33)
    {
        if (v37 > 0)
            sub_103451f0(0);
        v10 = (!&v35 ? NULL : &v36);
        sub_10347770(v10, a0);
        v30 = sub_1033e670(a3);
        v29 = 0;
        if (((char)idx->field_60 & 2) && (!sub_10346d50() || (v48 = sub_10314ca0(&v36 + *((int *)(v36 + 4)), 43), (int)(char)*(v30) != (int)sub_10314ca0(&v36 + *((int *)(v36 + 4)), 43) && !((v49 = sub_10314ca0(&v36 + *((int *)(v36 + 4)), 45), (int)(char)*(v30) == (int)sub_10314ca0(&v36 + *((int *)(v36 + 4)), 45))))))
            v29 = sub_10314ca0(&(&v36)[*((int *)(v36 + 4))], 32);
        v18 = sub_10346d50();
        v17 = *((int *)&idx->padding_0[92]) - -(-(0 < v29));
        v50 = sub_10347830(&v17, &v18);
        v31 = *(v50);
        v51 = _INSERT(*(v50), 0, (idx->field_60 & 4));
        v53 = sub_10345220(v32, _INSERT(idx, 0, v29), v51);
        sub_10347860(a2, v30, v31, v37, v53);
    }
    else
    {
        v9 = (!&v35 ? NULL : &v36);
        sub_10347770(v9, a0);
        v27 = sub_1033e670(a3);
        v28 = sub_10346d50();
        v26 = 0;
        if (((char)idx->field_60 & 2) && (!sub_10346d50() || (v54 = sub_10314ca0(&v36 + *((int *)(v36 + 4)), 43), (int)(char)*(v27) != (int)sub_10314ca0(&v36 + *((int *)(v36 + 4)), 43) && !((v55 = sub_10314ca0(&v36 + *((int *)(v36 + 4)), 45), (int)(char)*(v27) == (int)sub_10314ca0(&v36 + *((int *)(v36 + 4)), 45))))))
            v26 = 1;
        if (v28 == v37 && v37 <= *((int *)&idx->padding_0[92]) && !v26)
        {
            sub_10314830(a2, v27, v28);
        }
        else
        {
            sub_10314830(a2, v27, v28);
            v27 = 0;
            sub_10347790(v13, a4);
            sub_103470c0(a3, 1);
            v40 = 1;
            v8 = (!&v24 ? NULL : &(&v25)[*((int *)(v25 + 4))]);
            sub_10347290(v8, a4);
            v7 = (!&v24 ? NULL : &v25);
            v1 = a0;
            v0 = v7;
            sub_10334530();
            sub_103451f0(0);
            if (v26)
            {
                v6 = (!&v24 ? NULL : &v25);
                sub_10345240(v6, 32);
            }
            v5 = (!&v24 ? NULL : &v25);
            sub_10347770(v5, a0);
            if (!sub_10346d50() && ((char)idx->field_60 & 2))
            {
                v26 = 1;
                v4 = (!&v24 ? NULL : &v25);
                sub_10345240(v4, 32);
            }
            v22 = sub_1033e670(a3);
            v16 = sub_10346d50();
            v15 = *((int *)&idx->padding_0[92]);
            v23 = *((int *)sub_10347830(&v15, &v16));
            if (v37 <= v23)
            {
                sub_10314830(a2, v22, v23);
            }
            else
            {
                v14 = -(-(0 < v26)) + v28;
                v19 = *((int *)sub_10347830(&v14, &v23));
                for (i = v26; i < v19 && (v56 = (char *)sub_103189a0(a2, i - -(-((unsigned int)(char)(0 < (unsigned int)v26)))), (int)(char)v22[i] == (int)*((char *)sub_103189a0(a2, i - -(-((unsigned int)(char)(0 < (unsigned int)v26)))))); i += 1);
                if (i >= v23)
                    i = v26;
                sub_10314830(a2, v22, i);
                v20 = v37 - v23;
                sub_103170f0(a2, v20, sub_10345220(0, v8));
                sub_1031a6b0(a2, &v22[i], v23 - i);
            }
            v40 = 0;
            sub_103469c0();
        }
    }
    sub_10347790();
    v40 = 4294967295;
    sub_103469c0();
    v58 = _ccall(v42, v43, (unsigned int)v44, 0);
    *((unsigned int *)v58) = v38;
    return;
}
```

## `sub_103451d0` `0x103451d0`

_17 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

int sub_103451d0(struct_0 *a0)
{
    return a0->field_18;
}
```

## `sub_103451f0` `0x103451f0`

_36 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

int sub_103451f0(struct_0 *idx, unsigned int a1)
{
    unsigned int v0;  // [bp-0x8]

    v0 = idx->field_18;
    idx->field_18 = a1;
    return v0;
}
```

## `sub_10345220` `0x10345220`

_17 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[48];
    char field_30;
} struct_0;

int sub_10345220(struct_0 *a0)
{
    return _INSERT(a0, 0, a0->field_30);
}
```

