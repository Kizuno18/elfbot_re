# elfbot.dll decompiled — jiru 0x10315330..0x10316570

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10315330` `0x10315330`

_93 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fb60;

int sub_10315330(int a0, int a1)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4138
    unsigned int v8;  // eax
    unsigned long v9;  // 4154
    unsigned long v10;  // 4128
    int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v8 = *((int *)v7);
    v1 = *((int *)v7);
    v0 = a0;
    v9 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v9) = &v1;
    sub_103153b0(a1, g_1038e180 ^ &v2, a0, v8, sub_1036a5e8, -1, &v3);
    *((char **)a0) = &g_1038fb60;
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v10) = v8;
    return a0;
}
```

## `sub_10315390` `0x10315390`

_20 bytes. (leaf/helper — see body)_

```c
extern char g_1038fb68;

int sub_10315390(unsigned int a0)
{
    *((char **)a0) = &g_1038fb68;
    return a0;
}
```

## `sub_103153b0` `0x103153b0`

_34 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern char g_1038fb68;

struct_0 * sub_103153b0(struct_0 *a0, unsigned int a1)
{
    *((char **)&a0->padding_0[0]) = &g_1038fb68;
    a0->field_4 = a1;
    return a0;
}
```

## `sub_103153e0` `0x103153e0`

_44 bytes. (leaf/helper — see body)_

```c
int sub_103153e0(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_10315390(v0);
    if (((char)a1 & 1))
        sub_10350abd(v0);
    return v0;
}
```

## `sub_10315410` `0x10315410`

_84 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fb60;

int sub_10315410(unsigned int a0)
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
    v3 = sub_1036a618;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    *((char **)v1) = &g_1038fb60;
    v4 = 0;
    v4 = 4294967295;
    v12 = sub_10315390(v1);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_10315470` `0x10315470`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10315470(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_10315410(v0);
    if (((char)a1 & 1))
        sub_10350abd(v0);
    return v0;
}
```

## `sub_103154a0` `0x103154a0`

_55 bytes. (leaf/helper — see body)_

```c
unsigned int sub_103154a0(unsigned int *a0, unsigned int a1)
{
    unsigned int index[4];  // eax
    unsigned int idx[6];  // ecx
    unsigned int v3;  // eax
    char v0;  // [bp-0x14]

    index = sub_103154e0(&v0, a0);
    idx = a0 + 2;
    idx[0] = index[0];
    idx[1] = index[1];
    idx[2] = index[2];
    v3 = index[3];
    idx[3] = v3;
    return v3;
}
```

## `sub_103154e0` `0x103154e0`

_79 bytes. (leaf/helper — see body)_

```c
unsigned int [4] sub_103154e0(unsigned int *index)
{
    int v5;  // ecx
    unsigned int idx[4];  // eax
    char v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    idx = sub_1035052b(&v0, v5);
    v1 = idx[0];
    v2 = idx[1];
    v3 = idx[2];
    v4 = idx[3];
    *(index) = v1;
    index[1] = v2;
    index[2] = v3;
    index[3] = v4;
    return index;
}
```

## `sub_10315530` `0x10315530`

_69 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
    int field_14;
} struct_0;

struct_0 * sub_10315530(struct_0 *a0)
{
    unsigned int v0;  // [bp-0x8]

    if (a0->field_14 > 0)
    {
        return sub_1035345e(a0->field_10);
    }
    else if (a0->field_14 < 0)
    {
        v0 = a0->field_10;
        return sub_10350eb5(v0);
    }
    else
    {
        return a0;
    }
}
```

## `sub_10315580` `0x10315580`

_33 bytes. (leaf/helper — see body)_

```c
int sub_10315580(int a0, char a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_1035041c(a1, a0 + 8, a0, &v1);
}
```

## `sub_103155b0` `0x103155b0`

_64 bytes. (leaf/helper — see body)_

```c
char * sub_103155b0(int a0, char *iter, char *a2)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    for (v0 = a0; iter != a2; iter += 1)
    {
        *(iter) = sub_1035041c(*(iter), v0 + 8);
    }
    return iter;
}
```

## `sub_103155f0` `0x103155f0`

_33 bytes. (leaf/helper — see body)_

```c
int sub_103155f0(int a0, char a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10350586(a1, a0 + 8, a0, &v1);
}
```

## `sub_10315620` `0x10315620`

_64 bytes. (leaf/helper — see body)_

```c
char * sub_10315620(int a0, char *iter, char *a2)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    for (v0 = a0; iter != a2; iter += 1)
    {
        *(iter) = sub_10350586(*(iter), v0 + 8);
    }
    return iter;
}
```

## `sub_10315660` `0x10315660`

_16 bytes. (leaf/helper — see body)_

```c
char sub_10315660(unsigned int a0, char a1)
{
    return a1;
}
```

## `sub_10315670` `0x10315670`

_45 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[28];
    struct struct_1 *field_1c;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_10315670(struct_0 **a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    struct_0 **v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return *(a0)->field_1c(a1, a2, a3, a2 - a1, a0, &v1);
}
```

## `sub_103156a0` `0x103156a0`

_59 bytes. (leaf/helper — see body)_

```c
int sub_103156a0(int a0, int a1, unsigned int a2, int a3, int a4)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    if (a4 < a2 - a1)
        sub_10353616(a0, &v1);
    sub_1035336f(a3, a4, a1, a2 - a1);
    return a2;
}
```

## `sub_103156e0` `0x103156e0`

_16 bytes. (leaf/helper — see body)_

```c
char sub_103156e0(unsigned int a0, char a1)
{
    return a1;
}
```

## `sub_103156f0` `0x103156f0`

_49 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[40];
    struct struct_1 *field_28;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_103156f0(struct_0 **a0, unsigned int a1, unsigned int a2, char a3, unsigned int a4)
{
    unsigned int v2;  // edx
    struct_0 **v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    v2 = _INSERT(0, 0, a3);
    return *(a0)->field_28(a1, a2, v2, a4, a2 - a1, a0, &v1);
}
```

## `sub_10315730` `0x10315730`

_59 bytes. (leaf/helper — see body)_

```c
int sub_10315730(int a0, int a1, unsigned int a2, unsigned int a3, int a4, int a5)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    if (a5 < a2 - a1)
        sub_10353616(a0, &v1);
    sub_1035336f(a4, a5, a1, a2 - a1);
    return a2;
}
```

## `sub_10315770` `0x10315770`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10315770(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_103157a0(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_103157a0` `0x103157a0`

_92 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fb20;

int sub_103157a0(unsigned int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4138
    unsigned long v11;  // 4154
    int v12;  // eax
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036a648;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    *((char **)v1) = &g_1038fb20;
    v4 = 0;
    sub_10315530(v1);
    v4 = 4294967295;
    v12 = sub_10315410(v1);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_10315800` `0x10315800`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10315800(unsigned int a0)
{
    sub_1031a280(a0, a0);
    sub_103147d0(a0);
    sub_10314750(a0, 0, 0);
    return a0;
}
```

## `sub_10315830` `0x10315830`

_74 bytes. (leaf/helper — see body)_

```c
extern int g_10399bb4;

int sub_10315830(int a0)
{
    char v0;  // [bp-0x10]

    if (a0 <= 0)
    {
        a0 = 0;
    }
    else if ((unsigned int)(4294967295 / a0) < 1)
    {
        sub_10315880(0);
        sub_103533ea(&v0, &g_10399bb4);
    }
    return sub_10350a53(a0);
}
```

## `sub_10315880` `0x10315880`

_93 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fb70;

int sub_10315880(int a0)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4138
    unsigned int v9;  // eax
    unsigned long v10;  // 4154
    unsigned long v11;  // 4128
    int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]
    unsigned int v4;  // [bp+0x4]

    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v9 = *((int *)v8);
    v1 = *((int *)v8);
    v0 = a0;
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v10) = &v1;
    sub_10353214(&v4, g_1038e180 ^ &v2, a0, v9, sub_1036a678, -1, &v3);
    *((char **)a0) = &g_1038fb70;
    v11 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v11) = v9;
    return a0;
}
```

## `sub_103158e0` `0x103158e0`

_84 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fb70;

unsigned int sub_103158e0(int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4139
    unsigned int v10;  // eax
    unsigned long v11;  // 4155
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    int v0;  // [bp-0x14]
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
    *((char **)a0) = &g_1038fb70;
    v2 = 0;
    v12 = sub_103532d2(g_1038e180 ^ &v3, a0, v10, sub_1036a6a8, -1, &v4);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v10;
    return v12;
}
```

## `sub_10315940` `0x10315940`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10315940(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_103158e0(v0);
    if (((char)a1 & 1))
        sub_10350abd(v0);
    return v0;
}
```

## `sub_10315970` `0x10315970`

_93 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fb70;

int sub_10315970(int a0, int a1)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4138
    unsigned int v8;  // eax
    unsigned long v9;  // 4154
    unsigned long v10;  // 4128
    int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v8 = *((int *)v7);
    v1 = *((int *)v7);
    v0 = a0;
    v9 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v9) = &v1;
    sub_1035327a(a1, g_1038e180 ^ &v2, a0, v8, sub_1036a6d8, -1, &v3);
    *((char **)a0) = &g_1038fb70;
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v10) = v8;
    return a0;
}
```

## `sub_103159d0` `0x103159d0`

_44 bytes. (leaf/helper — see body)_

```c
char sub_103159d0(int a0, int a1, int a2, int a3)
{
    int v2;  // ecx
    int v3;  // eax
    char v0;  // [bp-0x5]
    char v1;  // [bp+0x0]

    v0 = sub_10337970(v2, &v1);
    v3 = _INSERT(v0, 0, v0);
    return sub_10315a00(a0, a1, a2, a3, v3);
}
```

## `sub_10315a00` `0x10315a00`

_29 bytes. (leaf/helper — see body)_

```c
int sub_10315a00(int a0, int a1, int a2, int a3)
{
    char v0;  // [bp+0x0]

    return sub_10315a20(a0, a1, a2, a3, &v0);
}
```

## `sub_10315a20` `0x10315a20`

_32 bytes. (leaf/helper — see body)_

```c
int sub_10315a20(int a0, int a1, int a2, int a3)
{
    char v0;  // [bp+0x0]

    sub_10353626(a0, a1, a2, a3, &v0);
    return a0;
}
```

## `sub_10315a40` `0x10315a40`

_365 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
    int field_4;
    int field_8;
} struct_1;

extern unsigned int g_1038e180;

struct_0 ** sub_10315a40(struct_0 **a0, int a1)
{
    unsigned long v15;  // ldt
    unsigned long v16;  // gdt
    unsigned long v25;  // 4123
    unsigned short v17;  // fs
    unsigned long v18;  // 4151
    unsigned long v19;  // 4173
    int v20;  // edi
    int v21;  // esi
    int v22;  // ebx
    int v23[3];  // eax
    struct_1 *v24;  // eax
    char *v0;  // [bp-0xa8]
    unsigned int v1;  // [bp-0xa4]
    unsigned int v2;  // [bp-0x70]
    int v3;  // [bp-0x60]
    int v4;  // [bp-0x5c]
    int v5;  // [bp-0x58]
    char v6;  // [bp-0x4c]
    struct_0 **v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x18]
    char *v10;  // [bp-0x14], Other Possible Types: struct_0 **
    unsigned int v11;  // [bp-0x10]
    unsigned int v12;  // [bp-0xc]
    char v13;  // [bp-0x8], Other Possible Types: unsigned int
    char v14;  // [bp-0x4]

    v13 = 4294967295;
    v12 = sub_1036a710;
    v18 = _ccall(v15, v16, (unsigned int)v17, 0);
    v11 = *((int *)v18);
    v10 = a0;
    v2 = g_1038e180 ^ &v14;
    v19 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int **)v19) = &v11;
    v10 = &v2;
    v9 = 0;
    sub_10315c40(a0, 0, g_1038e180 ^ &v14, v20, v21, v22);
    v13 = 0;
    if ((char)sub_103455c0(a0, 0, g_1038e180 ^ &v14, v20, v21, v22))
    {
        v5 = sub_10314d40((char *)a0 + *(a0)->field_4, &v7);
        v4 = v5;
        v13 = 1;
        v8 = sub_10316680(v4);
        v13 = 0;
        sub_103130c0(&v7);
        v13 = 2;
        v3 = (!a0 ? NULL : (struct_0 **)((char *)a0 + *(a0)->field_4));
        v23 = sub_10316540(0, v3, &v9, a1);
        v24 = sub_10316540(sub_10315c20(v23[0], v23[1], v23[2]));
        v1 = v24->field_0;
        v0 = &v6;
        sub_103164e0(&v6, v24->field_0, v24->field_4, v24->field_8);
        v13 = 0;
    }
    sub_10314630((char *)a0 + *(a0)->field_4, v9, 0);
    v13 = 4294967295;
    sub_10315bd0(v0, v1);
    v25 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int *)v25) = v11;
    return a0;
}
```

## `sub_10315b64` `0x10315b64`

_33 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

int sub_10315b64(void)
{
    struct_0 **v1;  // [bp+0xfffb4]
    unsigned int v2;  // [bp+0x100000]

    sub_10314630((char *)v1 + *(v1)->field_4, 4, 1);
    v2 = 0;
    return "j";
}
```

## `sub_10315bd0` `0x10315bd0`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10315bd0(int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4137
    unsigned int v10;  // eax
    unsigned long v11;  // 4153
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    int v0;  // [bp-0x14]
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
    v2 = 0;
    v12 = sub_10345660(g_1038e180 ^ &v3, a0, v10, sub_1036a738, -1, &v4);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v10;
    return v12;
}
```

## `sub_10315c20` `0x10315c20`

_17 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned int field_28;
} struct_0;

int sub_10315c20(struct_0 *a0)
{
    return a0->field_28;
}
```

## `sub_10315c40` `0x10315c40`

_104 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    char field_4;
} struct_0;

extern unsigned int g_1038e180;

struct_0 * sub_10315c40(struct_0 *a0, int a1, char a2)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4138
    unsigned int v9;  // eax
    unsigned long v10;  // 4154
    int v11;  // ecx
    unsigned long v12;  // 4128
    struct_0 *v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v9 = *((int *)v8);
    v1 = *((int *)v8);
    v0 = a0;
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v10) = &v1;
    sub_10316050(a1, g_1038e180 ^ &v3, a0, v9, sub_1036a768, -1, &v4);
    v2 = 0;
    v11 = _INSERT(0, 0, a2);
    a0->field_4 = sub_10315cb0(v11);
    v12 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v12) = v9;
    return a0;
}
```

## `sub_10315cb0` `0x10315cb0`

_452 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern unsigned int g_1038e180;

char sub_10315cb0(struct_0 **a0, char a1)
{
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    unsigned short v14;  // fs
    unsigned long v15;  // 4151
    unsigned long v16;  // 4173
    int v17;  // edi
    int v18;  // esi
    int v19;  // ebx
    char v20;  // al
    unsigned long v21;  // 4119
    unsigned int v0;  // [bp-0x40]
    unsigned int v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x24]
    struct_0 **v4;  // [bp-0x20]
    unsigned int v5;  // [bp-0x1c]
    unsigned int v6;  // [bp-0x18]
    char *v7;  // [bp-0x14], Other Possible Types: struct_0 **
    unsigned int v8;  // [bp-0x10]
    unsigned int v9;  // [bp-0xc]
    unsigned int v10;  // [bp-0x8]
    char v11;  // [bp-0x4]

    v10 = 4294967295;
    v9 = sub_1036a798;
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    v8 = *((int *)v15);
    v7 = a0;
    v0 = g_1038e180 ^ &v11;
    v16 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v16) = &v8;
    v7 = &v0;
    if ((char)sub_10315ed0(g_1038e180 ^ &v11, v17, v18, v19))
    {
        if (sub_10316170())
        {
            sub_10316170();
            sub_10315f10();
        }
        if (!a1 && ((char)sub_10315ef0() & 1))
        {
            v2 = sub_10314d40((char *)a0 + *(a0)->field_4, &v4);
            v1 = v2;
            v10 = 0;
            v6 = sub_10314e10(v1);
            v10 = 4294967295;
            sub_103130c0(&v4);
            v10 = 1;
            sub_10315c20((char *)a0 + *(a0)->field_4);
            v5 = sub_10315f80();
            while (true)
            {
                v3 = sub_1032fd20();
                if ((char)sub_10312db0(&v3, &v5))
                {
                    sub_10314630((char *)a0 + *(a0)->field_4, 1, 0);
                    break;
                }
                else
                {
                    if (!(char)sub_10315ea0(72, sub_10312f00(&v5)))
                        break;
                    sub_10315c20((char *)a0 + *(a0)->field_4);
                    v5 = sub_10315fd0();
                }
            }
            v10 = 4294967295;
        }
        if (!(char)sub_10315ed0())
            goto LABEL_10315e6d;
        v20 = 1;
    }
    else
    {
LABEL_10315e6d:
        sub_10314630((char *)a0 + *(a0)->field_4, 2, 0);
        v20 = 0;
    }
    v21 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int *)v21) = v8;
    return v20;
}
```

## `sub_10315e04` `0x10315e04`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10315e04(void)
{
}
```

## `sub_10315e2a` `0x10315e2a`

_33 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern char g_10315e52;

int sub_10315e2a(void)
{
    struct_0 **v1;  // [bp+0xfffe0]
    unsigned int v2;  // [bp+0x100000]

    sub_10314630((char *)v1 + *(v1)->field_4, 4, 1);
    v2 = 4294967295;
    return &g_10315e52;
}
```

## `sub_10315ea0` `0x10315ea0`

_39 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

int sub_10315ea0(struct_0 *a0, unsigned short a1, char a2)
{
    return -(-(0 < (*((short *)(a0->field_10 + a2 * 2)) & a1)));
}
```

## `sub_10315ed0` `0x10315ed0`

_26 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
} struct_0;

int sub_10315ed0(struct_0 *a0)
{
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return -(0 < sub_10313840(v0)) + 1;
}
```

## `sub_10315ef0` `0x10315ef0`

_17 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

int sub_10315ef0(struct_0 *a0)
{
    return a0->field_10;
}
```

## `sub_10315f10` `0x10315f10`

_107 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

struct_0 ** sub_10315f10(struct_0 **a0)
{
    unsigned int v0;  // [bp-0x8]

    v0 = 0;
    if ((char)sub_10313820((char *)a0 + *(a0)->field_4))
    {
        sub_10314630((char *)a0 + *(a0)->field_4, v0, 0);
        return a0;
    }
    sub_10315c20((char *)a0 + *(a0)->field_4);
    if (sub_103160a0() == 4294967295)
    {
        v0 |= 4;
        sub_10314630((char *)a0 + *(a0)->field_4, v0, 0);
    }
    else
    {
        sub_10314630((char *)a0 + *(a0)->field_4, v0, 0);
    }
    return a0;
}
```

## `sub_10315f80` `0x10315f80`

_66 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[16];
    struct struct_1 *field_10;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_10315f80(struct_0 **a0)
{
    int v0;  // [bp-0xc]

    v0 = (sub_10313270(a0) <= 0 ? *(a0)->field_10() : sub_10312da0(sub_103131a0(a0)));
    return v0;
}
```

## `sub_10315fd0` `0x10315fd0`

_120 bytes. (leaf/helper — see body)_

```c
int sub_10315fd0(void* a0)
{
    int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    if (sub_10313270(a0) <= 1)
    {
        v3 = sub_103160c0();
        v2 = sub_1032fd20();
        v0 = (!(char)sub_10312db0(&v2, &v3) ? sub_10315f80(a0) : sub_1032fd20());
        v1 = v0;
        return v1;
    }
    v1 = sub_10312da0(sub_10316130());
    return v1;
}
```

## `sub_10316050` `0x10316050`

_77 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

struct_1 ** sub_10316050(struct_1 **a0, struct_0 **a1)
{
    struct_1 **v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    *(v0) = a1;
    if (sub_10315c20((char *)*(v0) + *(v0)->field_0->field_4))
    {
        sub_10315c20((char *)*(v0) + *(v0)->field_0->field_4);
        sub_10316190();
    }
    return v0;
}
```

## `sub_103160a0` `0x103160a0`

_24 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[48];
    struct struct_1 *field_30;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_103160a0(struct_0 **a0)
{
    struct_0 **v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return *(a0)->field_30(a0, &v1);
}
```

## `sub_103160c0` `0x103160c0`

_66 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[32];
    struct struct_1 *field_20;
    char padding_24[12];
    struct struct_1 *field_30;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_103160c0(struct_0 *a0)
{
    int v0;  // [bp-0xc]

    v0 = (sub_10313270(a0) <= 0 ? (*((int *)(*((int *)&a0->padding_0[0]) + 20)))() : sub_10312da0(sub_10313220(a0)));
    return v0;
}
```

## `sub_10316110` `0x10316110`

_22 bytes. (leaf/helper — see body)_

```c
void sub_10316110(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1034ff2b(a0, &v1);
    return;
}
```

## `sub_10316130` `0x10316130`

_57 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[32];
    struct struct_1 *field_20;
    char padding_24[12];
    struct struct_1 *field_30;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_10316130(struct_0 *idx)
{
    idx->field_30->field_0 = idx->field_30->field_0 - 1;
    idx->field_20->field_0 = idx->field_20->field_0 + 1;
    return idx->field_20->field_0;
}
```

## `sub_10316170` `0x10316170`

_17 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[44];
    unsigned int field_2c;
} struct_0;

int sub_10316170(struct_0 *a0)
{
    return a0->field_2c;
}
```

## `sub_10316190` `0x10316190`

_22 bytes. (leaf/helper — see body)_

```c
void sub_10316190(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1034ff22(a0, &v1);
    return;
}
```

## `sub_103161b0` `0x103161b0`

_282 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
    unsigned int field_4;
} struct_1;

typedef struct struct_0 {
    char padding_0[4];
    char field_4;
} struct_0;

typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern unsigned int g_1038e180;

int sub_103161b0(struct_1 *idx)
{
    unsigned long v15;  // ldt
    unsigned long v16;  // gdt
    unsigned short v17;  // fs
    unsigned long v18;  // 4154
    unsigned long v19;  // 4176
    unsigned long v20;  // 4123
    unsigned int v0;  // [bp-0x40]
    int v1;  // [bp-0x3c]
    int v2;  // [bp-0x38]
    int v3;  // [bp-0x34]
    int v4;  // [bp-0x2c], Other Possible Types: unsigned int
    int v5;  // [bp-0x28], Other Possible Types: unsigned int
    unsigned int v6;  // [bp-0x24]
    struct_0 v7;  // [bp-0x20]
    unsigned int v8;  // [bp-0x18]
    char *v9;  // [bp-0x14], Other Possible Types: struct_1 *
    unsigned int v10;  // [bp-0x10]
    unsigned int v11;  // [bp-0xc]
    char v12;  // [bp-0x8], Other Possible Types: unsigned int
    char v13;  // [bp-0x4]

    v12 = 4294967295;
    v11 = sub_1036a7c8;
    v18 = _ccall(v15, v16, (unsigned int)v17, 0);
    v10 = *((int *)v18);
    v9 = idx;
    v0 = g_1038e180 ^ &v13;
    v19 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int **)v19) = &v10;
    v9 = &v0;
    v6 = 0;
    v8 = 0;
    idx->field_4 = 0;
    sub_10315c40(&v7, idx, 1);
    v12 = 0;
    if (!(char)sub_103455c0(g_1038e180 ^ &v13, v1, v2, v3, idx, v4, v5))
    {
        v6 = sub_1032fd20();
    }
    else
    {
        v12 = 1;
        v6 = sub_103160c0(sub_10315c20((char *)idx + idx->field_0->field_4));
        v5 = sub_1032fd20();
        if ((char)sub_10312db0(&v5, &v6))
            v8 |= 3;
        else
            idx->field_4 = idx->field_4 + 1;
        v12 = 0;
    }
    sub_10314630((char *)idx + idx->field_0->field_4, v8, 0);
    v4 = v6;
    v12 = 4294967295;
    sub_10315bd0(&v7);
    v20 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int *)v20) = v10;
    return v6;
}
```

## `sub_10316283` `0x10316283`

_33 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

int sub_10316283(void)
{
    struct_0 **v1;  // [bp+0xfffd8]
    unsigned int v2;  // [bp+0x100000]

    sub_10314630((char *)v1 + *(v1)->field_4, 4, 1);
    v2 = 0;
    return "j";
}
```

## `sub_103162f0` `0x103162f0`

_132 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fa9c;
extern char g_1038faa4;

unsigned int sub_103162f0(int a0)
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
    v3 = sub_1036a81f;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    *((char **)a0) = &g_1038faa4;
    *((char **)(a0 + 20)) = &g_1038fa9c;
    v4 = 1;
    v4 = 0;
    v1 = (!a0 ? 0 : a0 + 20);
    sub_10313d70(v1);
    v4 = 4294967295;
    v12 = sub_10312b90(a0);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_10316380` `0x10316380`

_142 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fa78;
extern char g_1038fa88;
extern char g_1038fa90;

unsigned int sub_10316380(unsigned int idx)
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
    v3 = sub_1036a86f;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    *((char **)idx) = &g_1038fa90;
    *((char **)(idx + 20)) = &g_1038fa88;
    *((char **)(idx + 40)) = &g_1038fa78;
    v4 = 1;
    v4 = 0;
    v1 = (!idx ? 0 : idx + 40);
    sub_10313bb0(v1);
    v4 = 4294967295;
    v12 = sub_103162f0(idx);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_10316410` `0x10316410`

_148 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10316410(int a0)
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
    v5 = sub_1036a89b;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v4 = *((int *)v12);
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v4;
    v2 = sub_10350a53(44, g_1038e180 ^ &v7);
    v6 = 0;
    v1 = (!v2 ? 0 : sub_10313c30(v2, a0 - 40));
    v3 = v1;
    v6 = 4294967295;
    v0 = (!v3 ? 0 : v3 + 40);
    v14 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v14) = v4;
    return v0;
}
```

## `sub_103164b0` `0x103164b0`

_42 bytes. (leaf/helper — see body)_

```c
extern int g_103994a4;

int sub_103164b0(int a0)
{
    char v0;  // [bp-0x30]

    sub_10313c30(&v0, a0 - 40);
    return sub_103533ea(&v0, &g_103994a4);
}
```

## `sub_103164e0` `0x103164e0`

_89 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[36];
    struct struct_1 *field_24;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_103164e0(struct_0 **a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int a10)
{
    struct_0 **v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    *(a0)->field_24(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a0, &v1);
    return a1;
}
```

## `sub_10316540` `0x10316540`

_48 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
    char field_8;
} struct_0;

struct_0 * sub_10316540(struct_0 *idx, unsigned int a1)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = idx;
    sub_10341910(idx, &v1);
    idx->field_4 = a1;
    idx->field_8 = !a1;
    return idx;
}
```

## `sub_10316570` `0x10316570`

_24 bytes. (leaf/helper — see body)_

```c
void sub_10316570(unsigned int a0)
{
    char v0;  // [bp+0x0]

    sub_10316590(sub_10319670(0, &v0));
    return;
}
```

