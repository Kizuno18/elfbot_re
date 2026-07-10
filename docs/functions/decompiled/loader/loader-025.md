# elfbot.dll decompiled — loader 0x00416ee0..0x00417675

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_00416ee0` `0x00416ee0`

_8 bytes. (leaf/helper — see body)_

```c
int sub_416ee0(void)
{
    return;
}
```

## `sub_00416ee8` `0x00416ee8`

_41 bytes. (leaf/helper — see body)_

```c
int sub_416ee8(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4)
{
    int v5;  // ebx
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4141
    unsigned long v10;  // 4150
    unsigned long v11;  // 4161
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char *v2;  // [bp-0xc], Other Possible Types: unsigned int
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    sub_403e68(v5, &v4);
    v2 = &v3;
    v1 = sub_416f1a;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v0 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v0;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v0;
    v2 = sub_416f21;
    return sub_416f11(v5, &v4);
}
```

## `sub_00416f11` `0x00416f11`

_9 bytes. (leaf/helper — see body)_

```c
int sub_416f11(void)
{
    return sub_403a10();
}
```

## `sub_00416f1a` `0x00416f1a`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_416f1a(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00416f1f` `0x00416f1f`

_2 bytes. (leaf/helper — see body)_

```c
int sub_416f1f(void)
{
    return sub_416f11();
}
```

## `sub_00416f21` `0x00416f21`

_7 bytes. (leaf/helper — see body)_

```c
int sub_416f21(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // ebx

    return v0;
}
```

## `sub_00416f28` `0x00416f28`

_8 bytes. (leaf/helper — see body)_

```c
extern char g_fffbd9e9;

void sub_416f28(void)
{
    g_fffbd9e9 = 255;
    return;
}
```

## `sub_00416f30` `0x00416f30`

_39 bytes. (leaf/helper — see body)_

```c
int sub_416f30(void)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4150
    unsigned long v10;  // 4159
    unsigned long v11;  // 4170
    int v12;  // ebx
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char *v2;  // [bp-0xc], Other Possible Types: unsigned int
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v2 = &v3;
    v1 = sub_416f58;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v0 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v0;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v0;
    v2 = sub_416f5f;
    return sub_416f57(v12, &v4);
}
```

## `sub_00416f57` `0x00416f57`

_1 bytes. (leaf/helper — see body)_

```c
void sub_416f57(void)
{
    return;
}
```

## `sub_00416f58` `0x00416f58`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_416f58(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00416f5d` `0x00416f5d`

_2 bytes. (leaf/helper — see body)_

```c
void sub_416f5d(void)
{
    sub_416f57();
    return;
}
```

## `sub_00416f5f` `0x00416f5f`

_5 bytes. (leaf/helper — see body)_

```c
int sub_416f5f(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // ebx

    return v0;
}
```

## `sub_00416f64` `0x00416f64`

_167 bytes. (leaf/helper — see body)_

```c
int sub_416f64(void)
{
    int v6;  // ebx
    int v7;  // eax
    unsigned int v16;  // cc_dep2
    unsigned int v17;  // cc_ndep
    unsigned int v18;  // 4101
    unsigned int v19;  // 4101
    unsigned int v20;  // 4101
    unsigned int v21;  // 4101
    unsigned long v22;  // 4152
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4126
    unsigned int v12;  // 4103
    unsigned long v13;  // 4135
    unsigned int v14;  // cc_op
    unsigned int v15;  // cc_dep1
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v2 = 0;
    sub_403e68(v6, 0, 0, 0, 0, v7, &v4);
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v12 = *((int *)v11);
    v0 = *((int *)v11);
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v13) = &v0;
    sub_409eac(v12, sub_417019, &v3);
    sub_403dc4(v12, sub_417019, &v3);
    v18 = _ccall(4, v14, v15, v16, v17);
    if (!((char)v18))
    {
        sub_409eac();
        sub_403dc4();
        v19 = _ccall(4, v14, v15, v16, v17);
        if ((char)v19)
            goto LABEL_416ff4;
        sub_409eac();
        sub_403dc4();
        v20 = _ccall(4, v14, v15, v16, v17);
        if ((char)v20)
            goto LABEL_416ff4;
        sub_409eac();
        sub_403dc4();
        v21 = _ccall(4, v14, v15, v16, v17);
        if ((char)v21)
            goto LABEL_416ff4;
    }
    else
    {
LABEL_416ff4:
    }
    v22 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v22) = v12;
    v1 = sub_417020;
    sub_41700b();
    return;
}
```

## `sub_0041700b` `0x0041700b`

_14 bytes. (leaf/helper — see body)_

```c
int sub_41700b(void)
{
    return sub_403a34();
}
```

## `sub_00417019` `0x00417019`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_417019(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041701e` `0x0041701e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41701e(void)
{
    return sub_41700b();
}
```

## `sub_00417020` `0x00417020`

_7 bytes. (leaf/helper — see body)_

```c
int sub_417020(void)
{
    unsigned int v1;  // ebx

    return v1;
}
```

## `sub_00417027` `0x00417027`

_1 bytes. (leaf/helper — see body)_

```c
void sub_417027(unsigned int a0, unsigned int a1)
{
    sub_417028();
    return;
}
```

## `sub_00417028` `0x00417028`

_45 bytes. (leaf/helper — see body)_

```c
extern char g_416ee6;
extern char g_416f2800;
extern char g_41704d;

int sub_417028(unsigned int a0, int a1)
{
    unsigned int v1;  // 4109
    unsigned int v2;  // eax

    if (!a1)
    {
        v1 = _ccall(6, a1, 0, 0);
        g_416f2800 = g_416f2800 - 0 - ((char)v1 & 1);
        return v2;
    }
    else if (!sub_416f64(a1))
    {
        return &g_416ee6;
    }
    else
    {
        return *((int *)&(&g_41704d)[a1]);
    }
}
```

## `sub_00417055` `0x00417055`

_3 bytes. (leaf/helper — see body)_

```c
int sub_417055(void)
{
    sub_417058();
    return;
}
```

## `sub_00417058` `0x00417058`

_21 bytes. (leaf/helper — see body)_

```c
int sub_417058(void)
{
    unsigned int v1;  // eax

    if (!v1)
        sub_416ee0();
    return;
}
```

## `sub_0041706d` `0x0041706d`

_8 bytes. (leaf/helper — see body)_

```c
extern char g_417028b8;

void sub_41706d(void)
{
    g_417028b8 = g_417028b8;
    return;
}
```

## `sub_00417075` `0x00417075`

_3 bytes. (leaf/helper — see body)_

```c
int sub_417075(void)
{
    sub_417078();
    return;
}
```

## `sub_00417078` `0x00417078`

_11 bytes. (leaf/helper — see body)_

```c
int sub_417078(void)
{
    return;
}
```

## `sub_00417083` `0x00417083`

_1 bytes. (leaf/helper — see body)_

```c
void sub_417083(void)
{
    sub_417084();
    return;
}
```

## `sub_00417084` `0x00417084`

_6 bytes. (leaf/helper — see body)_

```c
void sub_417084(void)
{
    sub_417078();
    return;
}
```

## `sub_0041708a` `0x0041708a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41708a(void)
{
    sub_41708c();
    return;
}
```

## `sub_0041708c` `0x0041708c`

_128 bytes. (leaf/helper — see body)_

```c
int sub_41708c(void)
{
    unsigned int v11;  // ecx
    unsigned int v12;  // edx
    unsigned long v22;  // 4119
    int v13;  // esi
    int v14;  // ebx
    unsigned long v15;  // ldt
    unsigned long v16;  // gdt
    unsigned short v17;  // fs
    unsigned long v18;  // 4129
    unsigned int v19;  // 4103
    unsigned long v20;  // 4138
    unsigned int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x24]
    int <0x41708c[is_4]|Stack bp-0x10, 1 B>;  // [bp-0x10]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]
    unsigned int v6;  // [bp+0x4]
    unsigned int v7;  // [bp+0x8]
    unsigned int v8;  // [bp+0xc]
    int v9;  // [bp+0x10]
    int v10;  // [bp+0x14]

    v3 = v11;
    v4 = v12;
    sub_403e68(v13, v14);
    sub_403e68(v13, v14);
    v18 = _ccall(v15, v16, (unsigned int)v17, 0);
    v19 = *((int *)v18);
    v1 = *((int *)v18);
    v20 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int **)v20) = &v1;
    v2 = &<0x41708c[is_4]|Stack bp-0x10, 1 B> ^ sub_417058;
    ((unsigned int)sub_417084()(v19, sub_41711d, &v5) + 2)(v6, v7, v8, v9, v10);
    v22 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int *)v22) = v6;
    v0 = sub_417124;
    sub_41710c(v9, v10);
    return;
}
```

## `sub_0041710c` `0x0041710c`

_17 bytes. (leaf/helper — see body)_

```c
int sub_41710c(void)
{
    sub_403a10();
    return sub_403a10();
}
```

## `sub_0041711d` `0x0041711d`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_41711d(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00417122` `0x00417122`

_2 bytes. (leaf/helper — see body)_

```c
int sub_417122(void)
{
    return sub_41710c();
}
```

## `sub_00417124` `0x00417124`

_10 bytes. (leaf/helper — see body)_

```c
int sub_417124(unsigned int a0)
{
    unsigned int v0;  // ebx

    return v0;
}
```

## `sub_0041712e` `0x0041712e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41712e(unsigned int a0)
{
    return sub_417130();
}
```

## `sub_00417130` `0x00417130`

_183 bytes. (leaf/helper — see body)_

```c
extern char g_41f110;
extern unsigned int g_420b10;
extern unsigned int g_420b28;

unsigned int sub_417130(unsigned int a0)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4124
    unsigned long v13;  // 4133
    int v14;  // eax
    unsigned int v15;  // edx
    unsigned long v16;  // 4118
    unsigned int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x2c]
    char *v2;  // [bp-0x28], Other Possible Types: unsigned int
    int v3;  // [bp-0x24]
    unsigned int v4;  // [bp-0x14]
    enum WIN32_ERROR v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]
    char v8;  // [bp-0x4]

    v7 = 0;
    v5 = GetLastError();
    if (!(char)sub_410b90(v3))
    {
        SetLastError(v5);
        return v7;
    }
    else if (g_41f110)
    {
        v6 = 0;
        sub_40520c(&g_420b10);
        v2 = &v8;
        v1 = sub_4171da;
        v12 = _ccall(v9, v10, (unsigned int)v11, 0);
        v0 = *((int *)v12);
        v13 = _ccall(v9, v10, (unsigned int)v11, 0);
        *((unsigned int **)v13) = &v0;
        v14 = sub_404654();
        if (v14 >= 0)
        {
            do
            {
                v15 = v14 * 5;
                if (*((int *)(g_420b28 + v15 * 8 + 28)) == a0)
                {
                    v7 = 4294967295;
                    v6 = *((int *)(g_420b28 + v15 * 8 + 24));
                    break;
                }
            } while ((v14 = (int)(v14 - 1), v14 != -1));
        }
        v16 = _ccall(v9, v10, (unsigned int)v11, 0);
        *((unsigned int *)v16) = v0;
        v2 = sub_4171e1;
        return sub_4171cf();
    }
    else
    {
        v4 = 0;
        SetLastError(v5);
        return v7;
    }
}
```

## `sub_004171cf` `0x004171cf`

_11 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420b10;

void sub_4171cf(void)
{
    sub_40534c(&g_420b10);
    return;
}
```

## `sub_004171da` `0x004171da`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4171da(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004171df` `0x004171df`

_2 bytes. (leaf/helper — see body)_

```c
void sub_4171df(void)
{
    sub_4171cf();
    return;
}
```

## `sub_004171e1` `0x004171e1`

_14 bytes. (leaf/helper — see body)_

```c
int sub_4171e1(void)
{
    unsigned int v1;  // [bp+0xffffc]

    if (!v1)
        goto LABEL_0x4171ef;
    sub_4159cc();
}
```

## `sub_00417207` `0x00417207`

_1 bytes. (leaf/helper — see body)_

```c
int sub_417207(void)
{
    sub_417208();
    return;
}
```

## `sub_00417208` `0x00417208`

_280 bytes. (leaf/helper — see body)_

```c
extern char g_41f110;
extern unsigned int g_420b10;
extern unsigned int g_420b28;

int sub_417208(void)
{
    char v10;  // cl
    unsigned long v11;  // ldt
    char v20;  // dl
    char v21;  // al
    int v22;  // eax
    int v23;  // eax
    unsigned int v24;  // ebx
    int v25;  // eax
    int v26;  // eax
    unsigned long v27;  // 4118
    unsigned long v12;  // gdt
    unsigned short v13;  // fs
    unsigned long v14;  // 4128
    unsigned long v15;  // 4137
    int v16;  // ebx
    unsigned int v17;  // edi
    unsigned int v18;  // eax
    int v19;  // eax
    int v0;  // [bp-0x2c]
    unsigned int v1;  // [bp-0x28]
    unsigned int v2;  // [bp-0x24]
    char *v3;  // [bp-0x20], Other Possible Types: unsigned int
    char v4;  // [bp-0xd]
    unsigned int v5;  // [bp-0xc]
    char v6;  // [bp-0x7]
    char v7;  // [bp-0x6]
    char v8;  // [bp-0x4]

    v7 = v10;
    v6 = 0;
    if (!g_41f110)
        return;
    sub_40520c(&g_420b10);
    v3 = &v8;
    v2 = sub_417321;
    v14 = _ccall(v11, v12, (unsigned int)v13, 0);
    v1 = *((int *)v14);
    v15 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int **)v15) = &v1;
    v5 = 0;
    v16 = sub_404654();
    if (v16 >= 0)
    {
        do
        {
            v17 = v16 * 5;
            if (*((int *)(g_420b28 + v17 * 8 + 28)) == v18)
            {
                v6 = 1;
                v5 = *((int *)(g_420b28 + v17 * 8 + 24));
                v19 = sub_404654();
                sub_40421c();
                v0 = v19;
                sub_404808();
                break;
            }
        } while ((v16 = (int)(v16 - 1), v16 != -1));
    }
    if (!v6 || v20)
        v21 = 0;
    else
        v21 = 1;
    v4 = v21;
    if (v4)
    {
        v22 = sub_404654();
        if (v22 >= 0)
        {
            v23 = v22 + 1;
            v24 = 0;
            do
            {
                v25 = v23;
                if (*((int *)(g_420b28 + v24 * 40)))
                {
                    v4 = 0;
                    break;
                }
            } while ((v24 += 1, v26 = (int)(v25 - 1), v23 = (int)(v25 - 1), v25 != 1));
        }
    }
    v27 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int *)v27) = v1;
    v3 = sub_417328;
    sub_417316();
    return;
}
```

## `sub_00417316` `0x00417316`

_11 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420b10;

void sub_417316(void)
{
    sub_40534c(&g_420b10);
    return;
}
```

## `sub_00417321` `0x00417321`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_417321(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00417326` `0x00417326`

_2 bytes. (leaf/helper — see body)_

```c
void sub_417326(void)
{
    sub_417316();
    return;
}
```

## `sub_00417328` `0x00417328`

_45 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[45];
    char field_2d;
} struct_0;

char sub_417328(unsigned int a0, unsigned int a1)
{
    char v0;  // [bp+0xffffb]
    struct_0 *v1;  // [bp+0xffffc]
    char v2;  // [bp+0x100001]
    char v3;  // [bp+0x100002]

    if (!v2)
        goto LABEL_0x417355;
    if (v1)
    {
        v1->field_2d = v3 ^ 1;
        sub_402e1c();
    }
    if (!v0)
        goto LABEL_0x417355;
    sub_416a94();
}
```

## `sub_00417388` `0x00417388`

_282 bytes. (leaf/helper — see body)_

```c
extern char g_41f110;
extern unsigned int g_420b10;
extern unsigned int g_420b28;

int sub_417388(void)
{
    unsigned long v14;  // ldt
    unsigned long v15;  // gdt
    unsigned long v24;  // 4151
    unsigned int v25;  // eax
    unsigned long v26;  // 4124
    unsigned int v27;  // 4103
    unsigned long v28;  // 4133
    int v29;  // esi
    int v30;  // esi
    unsigned int v31;  // edi
    int v32;  // esi
    int v33;  // esi
    unsigned short v16;  // fs
    unsigned long v34;  // 4118
    unsigned long v35;  // 4116
    unsigned long v36;  // 4118
    unsigned long v17;  // 4155
    unsigned int v18;  // 4119
    unsigned long v19;  // 4164
    int v20;  // edi
    int v21;  // esi
    int v22;  // ebx
    unsigned long v23;  // 4147
    int v0;  // [bp-0x64]
    unsigned int v1;  // [bp-0x60]
    unsigned int v2;  // [bp-0x58]
    unsigned int v3;  // [bp-0x54]
    unsigned int v4;  // [bp-0x50]
    char *v5;  // [bp-0x4c]
    unsigned int v6;  // [bp-0x48]
    unsigned int v7;  // [bp-0x40]
    unsigned int v8;  // [bp-0x20]
    enum WIN32_ERROR v9;  // [bp-0x18]
    unsigned int v10;  // [bp-0xc]
    unsigned int v11;  // [bp-0x8]
    char v12;  // [bp-0x4]

    v10 = 0;
    v17 = _ccall(v14, v15, (unsigned int)v16, 0);
    v18 = *((int *)v17);
    v6 = *((int *)v17);
    v19 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int **)v19) = &v6;
    v9 = GetLastError();
    if ((char)sub_410b90(v18, sub_417667, &v12, v20, v21, v22, 0))
    {
        v5 = &v12;
        v4 = sub_41762b;
        v23 = _ccall(v14, v15, (unsigned int)v16, 0);
        v3 = *((int *)v23);
        v24 = _ccall(v14, v15, (unsigned int)v16, 0);
        *((unsigned int **)v24) = &v3;
        if (v25 && g_41f110)
        {
            v11 = 0;
            sub_40520c(&g_420b10);
            v26 = _ccall(v14, v15, (unsigned int)v16, 0);
            v27 = *((int *)v26);
            v1 = *((int *)v26);
            v28 = _ccall(v14, v15, (unsigned int)v16, 0);
            *((unsigned int **)v28) = &v1;
            v0 = sub_40464c(v27, sub_417488, &v12);
            sub_404808();
            v29 = sub_404654();
            if (v29 >= 0)
            {
                v30 = v29 + 1;
                v31 = 0;
                do
                {
                    v32 = v30;
                    if (*((int *)(g_420b28 + v31 * 40 + 8)))
                    {
                        sub_40421c();
                        v11 += 1;
                    }
                } while ((v31 += 1, v33 = (int)(v32 - 1), v30 = (int)(v32 - 1), v32 != 1));
            }
            v34 = _ccall(v14, v15, (unsigned int)v16, 0);
            *((unsigned int *)v34) = v27;
            v2 = sub_41748f;
            sub_41747d();
            return;
        }
        v35 = _ccall(v14, v15, (unsigned int)v16, 0);
        *((unsigned int *)v35) = v3;
        v8 = 0;
    }
    SetLastError(v9);
    v36 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int *)v36) = v18;
    v7 = sub_41766e;
    sub_417650();
    return;
}
```

## `sub_0041747d` `0x0041747d`

_11 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420b10;

void sub_41747d(void)
{
    sub_40534c(&g_420b10);
    return;
}
```

## `sub_00417488` `0x00417488`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_417488(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041748d` `0x0041748d`

_2 bytes. (leaf/helper — see body)_

```c
void sub_41748d(void)
{
    sub_41747d();
    return;
}
```

## `sub_0041748f` `0x0041748f`

_351 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    PWSTR field_c;
    char padding_10[8];
    struct struct_1 *field_18;
    unsigned int field_1c;
} struct_0;

typedef struct struct_1 {
    char padding_0[60];
    struct struct_2 *field_3c;
    char padding_40[4];
    unsigned short field_44;
} struct_1;

typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

extern unsigned int g_417621;
extern char g_41edac;

int sub_41748f(void)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    int v19;  // esi
    unsigned long v20;  // 4118
    unsigned short v11;  // fs
    unsigned long v12;  // 4130
    unsigned long v13;  // 4139
    int v14;  // esi
    int v15;  // esi
    unsigned int v16;  // edi
    int v17;  // esi
    struct_0 *v18;  // ebx
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]
    unsigned int v2;  // [bp-0x4]
    char v4;  // [bp+0xfffef]
    int v5;  // [bp+0xffff4]
    HMODULE v6;  // [bp+0xffff8]
    unsigned int v7;  // [bp+0xffffc]
    int v8;  // [bp+0x100000]

    v4 = 0;
    v1 = sub_41761a;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v0 = *((int *)v12);
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v0;
    v14 = v8 - 1;
    if (v14 >= 0)
    {
        v15 = v14 + 1;
        v16 = 0;
        do
        {
            v17 = v15;
            v18 = v7 + v16 * 40;
            if (*((int *)&v18->padding_0[8]) && (!v18->field_18 || IsBadReadPtr(v18->field_18->field_3c, 0x6) || v18->field_18->field_3c->field_0 != v18->field_18->padding_40 || (short)v18->field_18->field_3c[1].field_0 != v18->field_18->field_44))
            {
                if (!v4)
                {
                    v4 = 1;
                    sub_4121c8();
                }
                if ((GetVersion() & 0x80000000))
                    v6 = sub_4052c4(sub_403e78());
                else
                    v6 = GetModuleHandleW(v18->field_c);
                sub_403e78();
                sub_403be8();
                sub_40a918();
                v5 = sub_411978();
                if (!v18->field_18 || *((int *)&v18->padding_10[4]) != v5)
                {
                    sub_417208();
                    return sub_417589();
                }
                else if (!g_41edac || !IsBadReadPtr(v18->field_18->field_3c, 0x6) && v18->field_18->field_3c->field_0 == *((int *)&v18->field_18[1].padding_0[0]) && (short)v18->field_18->field_3c[1].field_0 == *((short *)&v18->field_18[1].padding_0[4]))
                {
                    sub_417130(v18->field_1c);
                }
            }
        } while ((v16 += 1, v19 = (int)(v17 - 1), v15 = (int)(v17 - 1), v17 != 1));
    }
    v20 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v20) = v0;
    v2 = &g_417621;
    return sub_41760e();
}
```

## `sub_00417589` `0x00417589`

_32 bytes. (leaf/helper — see body)_

```c
int sub_417589(void)
{
    int v2[10];  // ebx
    int v3;  // eax
    int v1;  // [bp+0xffff4]

    sub_41708c(v2[9], v2[7], v2[8], v1, v3);
}
```

## `sub_0041760e` `0x0041760e`

_12 bytes. (leaf/helper — see body)_

```c
int sub_41760e(void)
{
    int v2;  // eax
    char v1;  // [bp+0xfffef]

    if (v1)
        v2 = sub_4123c0();
    return v2;
}
```

## `sub_0041761a` `0x0041761a`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_41761a(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041761f` `0x0041761f`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41761f(void)
{
    return sub_41760e();
}
```

## `sub_0041762b` `0x0041762b`

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

unsigned int sub_41762b(int a0)
{
    struct_1 *v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x8]

    return sub_4030c0(v0, a0, v1);
}
```

## `sub_00417630` `0x00417630`

_5 bytes. (leaf/helper — see body)_

```c
void sub_417630(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int *a10)
{
    unsigned int v0;  // [bp+0x0]

    sub_4034ec(v0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10);
}
```

## `sub_00417650` `0x00417650`

_23 bytes. (leaf/helper — see body)_

```c
int sub_417650(void)
{
    sub_403a10();
    return sub_404814();
}
```

## `sub_00417667` `0x00417667`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_417667(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041766c` `0x0041766c`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41766c(void)
{
    return sub_417650();
}
```

## `sub_0041766e` `0x0041766e`

_7 bytes. (leaf/helper — see body)_

```c
void sub_41766e(unsigned int a0, unsigned int a1)
{
    return;
}
```

## `sub_00417675` `0x00417675`

_3 bytes. (leaf/helper — see body)_

```c
int sub_417675(void)
{
    return sub_417678();
}
```

