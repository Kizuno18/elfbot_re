# elfbot.dll decompiled — jiru 0x10312d20..0x10313bd0

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10312d20` `0x10312d20`

_13 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10312d20(unsigned int a0)
{
    return 0;
}
```

## `sub_10312d30` `0x10312d30`

_16 bytes. (leaf/helper — see body)_

```c
void sub_10312d30(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1032fd20(a0, &v1);
    return;
}
```

## `sub_10312d40` `0x10312d40`

_93 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[16];
    struct struct_1 *field_10;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

unsigned int sub_10312d40(struct_0 **a0)
{
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v2 = *(a0)->field_10();
    v1 = sub_1032fd20();
    v0 = (!(char)sub_10312db0(&v1, &v2) ? sub_10312da0(sub_10313220()) : sub_1032fd20());
    return v0;
}
```

## `sub_10312da0` `0x10312da0`

_11 bytes. (leaf/helper — see body)_

```c
int sub_10312da0(char *a0)
{
    return *(a0);
}
```

## `sub_10312db0` `0x10312db0`

_20 bytes. (leaf/helper — see body)_

```c
int sub_10312db0(unsigned int *a0, unsigned int a1)
{
    return *(a0) == *((int *)a1);
}
```

## `sub_10312dd0` `0x10312dd0`

_36 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[28];
    struct struct_1 *field_1c;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_10312dd0(struct_0 **a0, unsigned int a1, unsigned int a2)
{
    struct_0 **v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return *(a0)->field_1c(a1, 4294967295, a2, a0, &v1);
}
```

## `sub_10312e00` `0x10312e00`

_240 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    struct struct_1 *field_14;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

unsigned int sub_10312e00(struct_0 **a0, char *iter, int a2, int node)
{
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    int v2;  // [bp-0x10]
    int v3;  // [bp-0xc]
    unsigned int iter1;  // [bp-0x8]

    iter1 = 0;
    while (node > 0)
    {
        v3 = sub_10313270();
        if (v3 > 0)
        {
            v2 = v3;
            if (node < v2)
                v2 = node;
            sub_10313350(iter, a2, sub_103131a0(v2));
            iter = &iter[v2];
            iter1 += v2;
            node -= v2;
            sub_103131e0(v2);
        }
        else
        {
            v1 = *(a0)->field_14();
            v0 = sub_1032fd20();
            if ((char)sub_10312db0(&v0, &v1))
                return iter1;
            *(iter) = sub_10312f00(&v1);
            iter += 1;
            iter1 += 1;
            node -= 1;
        }
    }
    return iter1;
}
```

## `sub_10312eb6` `0x10312eb6`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10312eb6(void)
{
}
```

## `sub_10312f00` `0x10312f00`

_10 bytes. (leaf/helper — see body)_

```c
int sub_10312f00(char *a0)
{
    return _INSERT(a0, 0, *(a0));
}
```

## `sub_10312f10` `0x10312f10`

_236 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    struct struct_1 *field_4;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

unsigned int sub_10312f10(struct_0 **a0, unsigned int iter, int node)
{
    int v6;  // eax
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    int v2;  // [bp-0x10]
    int v3;  // [bp-0xc]
    unsigned int iter1;  // [bp-0x8]

    iter1 = 0;
    while (node > 0)
    {
        v3 = sub_103132e0();
        if (v3 > 0)
        {
            v2 = v3;
            if (node < v2)
                v2 = node;
            sub_10313350(sub_103131c0(v3, iter, v2));
            iter += v2;
            iter1 += v2;
            node -= v2;
            sub_103132a0(v2);
        }
        else
        {
            v6 = sub_10312da0(iter);
            v1 = *(a0)->field_4(v6);
            v0 = sub_1032fd20(v6);
            if ((char)sub_10312db0(&v0, &v1))
                return iter1;
            iter += 1;
            iter1 += 1;
            node -= 1;
        }
    }
    return iter1;
}
```

## `sub_10312fd3` `0x10312fd3`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10312fd3(void)
{
}
```

## `sub_10313000` `0x10313000`

_30 bytes. (leaf/helper — see body)_

```c
extern int g_10394428;

int sub_10313000(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10313310(g_10394428, a0, &v1);
    return a1;
}
```

## `sub_10313020` `0x10313020`

_30 bytes. (leaf/helper — see body)_

```c
extern int g_10394428;

int sub_10313020(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10313310(g_10394428, a0, &v1);
    return a1;
}
```

## `sub_10313040` `0x10313040`

_16 bytes. (leaf/helper — see body)_

```c
int sub_10313040(unsigned int a0)
{
    return a0;
}
```

## `sub_10313050` `0x10313050`

_13 bytes. (leaf/helper — see body)_

```c
void sub_10313050(unsigned int a0)
{
    return;
}
```

## `sub_10313060` `0x10313060`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10313060(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_10312c70(v0);
    if (((char)a1 & 1))
        sub_10350abd(v0);
    return v0;
}
```

## `sub_10313090` `0x10313090`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10313090(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_103130c0(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_103130c0` `0x103130c0`

_72 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

struct_1 ** sub_103130c0(struct_1 **a0)
{
    struct_1 **v0;  // [bp-0x14], Other Possible Types: unsigned int
    struct_1 **v1;  // [bp-0xc]
    struct_1 **v2;  // [bp-0x8]

    if (!*(a0))
        return a0;
    v1 = sub_10313110();
    v2 = v1;
    if (!v2)
    {
        v0 = 0;
        return v1;
    }
    v0 = *(v2)->field_0(1);
    return v0;
}
```

## `sub_10313110` `0x10313110`

_141 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern unsigned int g_1038e180;

unsigned int sub_10313110(struct_0 *idx)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4152
    unsigned long v11;  // 4117
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]
    char v4;  // [bp-0x4]

    v3 = 4294967295;
    v2 = sub_10369fc8;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v1 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v1;
    sub_10350060(0, g_1038e180 ^ &v4, idx);
    v3 = 0;
    if (idx->field_4 > 0 && idx->field_4 < 4294967295)
        idx->field_4 = idx->field_4 - 1;
    v0 = ~(-(0 < idx->field_4)) & idx;
    v3 = 4294967295;
    sub_10350081();
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v1;
    return v0;
}
```

## `sub_103131a0` `0x103131a0`

_19 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[32];
    struct struct_1 *field_20;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_103131a0(struct_0 *a0)
{
    return a0->field_20->field_0;
}
```

## `sub_103131c0` `0x103131c0`

_19 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[36];
    struct struct_1 *field_24;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_103131c0(struct_0 *a0)
{
    return a0->field_24->field_0;
}
```

## `sub_103131e0` `0x103131e0`

_51 bytes. (leaf/helper — see body)_

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

unsigned int * sub_103131e0(struct_0 *idx, unsigned int a1)
{
    unsigned int *v0;  // eax

    idx->field_30->field_0 = idx->field_30->field_0 - a1;
    v0 = &idx->field_20->field_0;
    *(v0) = idx->field_20->field_0 + a1;
    return v0;
}
```

## `sub_10313220` `0x10313220`

_65 bytes. (leaf/helper — see body)_

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

int sub_10313220(struct_0 *idx)
{
    unsigned int v0;  // [bp-0xc]

    idx->field_30->field_0 = idx->field_30->field_0 - 1;
    v0 = idx->field_20->field_0;
    idx->field_20->field_0 = idx->field_20->field_0 + 1;
    return v0;
}
```

## `sub_10313270` `0x10313270`

_47 bytes. (leaf/helper — see body)_

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

unsigned int sub_10313270(struct_0 *a0)
{
    unsigned int v0;  // [bp-0xc]

    v0 = (!a0->field_20->field_0 ? 0 : a0->field_30->field_0);
    return v0;
}
```

## `sub_103132a0` `0x103132a0`

_51 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[36];
    struct struct_1 *field_24;
    char padding_28[12];
    struct struct_1 *field_34;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

unsigned int * sub_103132a0(struct_0 *idx, unsigned int a1)
{
    unsigned int *v0;  // eax

    idx->field_34->field_0 = idx->field_34->field_0 - a1;
    v0 = &idx->field_24->field_0;
    *(v0) = idx->field_24->field_0 + a1;
    return v0;
}
```

## `sub_103132e0` `0x103132e0`

_47 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[36];
    struct struct_1 *field_24;
    char padding_28[12];
    struct struct_1 *field_34;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

unsigned int sub_103132e0(struct_0 *a0)
{
    unsigned int v0;  // [bp-0xc]

    v0 = (!a0->field_24->field_0 ? 0 : a0->field_34->field_0);
    return v0;
}
```

## `sub_10313310` `0x10313310`

_53 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038fa04;

unsigned int [5] sub_10313310(unsigned int *idx, unsigned int a1)
{
    *(idx) = a1;
    idx[2] = 0;
    idx[3] = 0;
    idx[4] = g_1038fa04;
    return idx;
}
```

## `sub_10313350` `0x10313350`

_44 bytes. (leaf/helper — see body)_

```c
char sub_10313350(int a0, int a1, int a2, int a3)
{
    int v2;  // ecx
    int v3;  // eax
    char v0;  // [bp-0x5]
    char v1;  // [bp+0x0]

    v0 = sub_10337970(v2, &v1);
    v3 = _INSERT(v0, 0, v0);
    return sub_10313380(a0, a1, a2, a3, v3);
}
```

## `sub_10313380` `0x10313380`

_29 bytes. (leaf/helper — see body)_

```c
int sub_10313380(int a0, int a1, int a2, int a3)
{
    char v0;  // [bp+0x0]

    return sub_103133a0(a0, a1, a2, a3, &v0);
}
```

## `sub_103133a0` `0x103133a0`

_32 bytes. (leaf/helper — see body)_

```c
int sub_103133a0(int a0, int a1, int a2, int a3)
{
    char v0;  // [bp+0x0]

    sub_1035336f(a0, a1, a2, a3, &v0);
    return a0;
}
```

## `sub_103133c0` `0x103133c0`

_107 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fa0c;

unsigned int [17] sub_103133c0(unsigned int *idx, unsigned int a1, unsigned int a2)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4135
    unsigned int v8;  // eax
    unsigned long v9;  // 4151
    unsigned long v10;  // 4152
    unsigned int v0[17];  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v8 = *((int *)v7);
    v1 = *((int *)v7);
    v0 = idx;
    v9 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v9) = &v1;
    sub_10313430(g_1038e180 ^ &v2, idx, v8, sub_10369ff8, -1, &v3);
    *(idx) = &g_1038fa0c;
    idx[15] = a1;
    idx[16] = a2;
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v10) = v8;
    return idx;
}
```

## `sub_10313430` `0x10313430`

_148 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[56];
    unsigned int field_38;
} struct_0;

extern unsigned int g_1038e180;
extern char g_1038f9cc;

struct_0 * sub_10313430(struct_0 *a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4141
    unsigned long v11;  // 4155
    unsigned long v12;  // 4120
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036a02b;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    *((char **)&a0->padding_0[0]) = &g_1038f9cc;
    sub_1034fef5(g_1038e180 ^ &v5);
    v4 = 0;
    v1 = sub_10350a53(4);
    v0 = (!v1 ? 0 : sub_103134d0());
    a0->field_38 = v0;
    sub_10313570();
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v2;
    return a0;
}
```

## `sub_103134d0` `0x103134d0`

_36 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_103134d0(unsigned int *a0)
{
    unsigned int *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    *(a0) = sub_103502ba(a0, &v1);
    sub_103500ee(a0, &v1);
    sub_10313500();
    return a0;
}
```

## `sub_10313500` `0x10313500`

_111 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern unsigned int g_1038e180;

unsigned int sub_10313500(struct_0 *idx)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4138
    unsigned long v9;  // 4152
    unsigned int v10;  // eax
    unsigned long v11;  // 4113
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]

    v2 = 4294967295;
    v1 = sub_1036a058;
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v0 = *((int *)v8);
    v9 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v9) = &v0;
    sub_10350060(0, g_1038e180 ^ &v3, idx);
    v2 = 0;
    if (idx->field_4 < 4294967295)
        idx->field_4 = idx->field_4 + 1;
    v2 = 4294967295;
    v10 = sub_10350081();
    v11 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v11) = v0;
    return v10;
}
```

## `sub_10313570` `0x10313570`

_109 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[16];
    struct struct_0 *field_10;
    struct struct_0 *field_14;
    char padding_18[8];
    struct struct_0 *field_20;
    struct struct_0 *field_24;
    char padding_28[8];
    struct struct_0 *field_30;
    struct struct_0 *field_34;
} struct_0;

int sub_10313570(struct_0 *idx)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = idx;
    idx->field_10 = &idx->padding_0[8];
    idx->field_14 = &idx->padding_0[12];
    idx->field_20 = idx->padding_18;
    idx->field_24 = &idx->padding_18[4];
    idx->field_30 = idx->padding_28;
    idx->field_34 = &idx->padding_28[4];
    sub_10313620(0, 0, idx, &v1);
    return sub_103135e0(0, 0, 0);
}
```

## `sub_103135e0` `0x103135e0`

_49 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[16];
    struct struct_1 *field_10;
    char padding_14[12];
    struct struct_1 *field_20;
    char padding_24[12];
    struct struct_1 *field_30;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_103135e0(struct_0 *idx, unsigned int a1, unsigned int a2, unsigned int a3)
{
    idx->field_10->field_0 = a1;
    idx->field_20->field_0 = a2;
    idx->field_30->field_0 = a3 - a2;
    return a3 - a2;
}
```

## `sub_10313620` `0x10313620`

_49 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    struct struct_1 *field_14;
    char padding_18[12];
    struct struct_1 *field_24;
    char padding_28[12];
    struct struct_1 *field_34;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_10313620(struct_0 *idx, unsigned int a1, unsigned int a2)
{
    idx->field_14->field_0 = a1;
    idx->field_24->field_0 = a1;
    idx->field_34->field_0 = a2 - a1;
    return a2 - a1;
}
```

## `sub_10313660` `0x10313660`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10313660(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_10312c20(v0);
    if (((char)a1 & 1))
        sub_10350abd(v0);
    return v0;
}
```

## `sub_10313690` `0x10313690`

_48 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[60];
    int field_3c;
    unsigned int field_40;
} struct_0;

int sub_10313690(struct_0 *idx, int a1)
{
    unsigned int v2;  // eax
    unsigned int v3;  // eax
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = idx;
    idx->field_3c = a1;
    v2 = sub_103136c0(a1, idx, &v1);
    v3 = v2 + idx->field_3c;
    idx->field_40 = v3;
    return _INSERT(v3, 0, 1);
}
```

## `sub_103136c0` `0x103136c0`

_17 bytes. (leaf/helper — see body)_

```c
int sub_103136c0(int a0)
{
    char v0;  // [bp+0x0]

    return sub_10352f20(a0, &v0);
}
```

## `sub_103136e0` `0x103136e0`

_276 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

char sub_103136e0(unsigned int *a0, int a1)
{
    unsigned long v11;  // ldt
    unsigned long v12;  // gdt
    unsigned short v13;  // fs
    unsigned long v14;  // 4171
    unsigned int v15;  // esi
    unsigned long v16;  // 4175
    char v17;  // al
    unsigned int v18;  // eax
    unsigned long v19;  // 4115
    unsigned int v0;  // [bp-0x68]
    unsigned int v1;  // [bp-0x64]
    unsigned int v2;  // [bp-0x60]
    int v3;  // [bp-0x5c]
    unsigned int v4;  // [bp-0x54]
    char v5;  // [bp-0x4d]
    char v6;  // [bp-0x4c]
    unsigned int v7;  // [bp-0x10]
    unsigned int v8;  // [bp-0xc]
    unsigned int v9;  // [bp-0x8]
    char v10;  // [bp-0x4]

    v9 = 4294967295;
    v8 = sub_1036a088;
    v14 = _ccall(v11, v12, (unsigned int)v13, 0);
    v7 = *((int *)v14);
    v1 = v15;
    v0 = g_1038e180 ^ &v10;
    v16 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int **)v16) = &v7;
    sub_103135e0(a0, a0[15], a0[15], a0[16]);
    sub_10313eb0(a0, 0, 1);
    v9 = 0;
    sub_10313860(1);
    v3 = (!&v6 ? NULL : &(&v6)[*((int *)(v6 + 4))]);
    sub_10316570(v3, 0);
    v4 = sub_10315a40(a1);
    if (sub_10313800() && !((v18 = sub_103161b0(), sub_103161b0() != sub_1032fd20())))
        v2 = 1;
    else
        v2 = 0;
    v5 = v2;
    v9 = 4294967295;
    sub_10313880();
    v17 = v5;
    v19 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int *)v19) = v7;
    return v17;
}
```

## `sub_10313800` `0x10313800`

_31 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10313800(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return ~(-(0 < (sub_10313820(a0, &v1) & 0xff))) & a0;
}
```

## `sub_10313820` `0x10313820`

_28 bytes. (leaf/helper — see body)_

```c
int sub_10313820(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return -(-(0 < (sub_10313840(a0, &v1) & 6)));
}
```

## `sub_10313840` `0x10313840`

_17 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
} struct_0;

int sub_10313840(struct_0 *a0)
{
    return a0->field_8;
}
```

## `sub_10313860` `0x10313860`

_30 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

unsigned int sub_10313860(struct_0 *idx, unsigned int a1)
{
    unsigned int v0;  // eax

    v0 = ~(a1) & idx->field_10;
    idx->field_10 = v0;
    return v0;
}
```

## `sub_10313880` `0x10313880`

_33 bytes. (leaf/helper — see body)_

```c
void sub_10313880(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10313960(a0, &v1);
    sub_103138b0(a0, &v1);
    return;
}
```

## `sub_103138b0` `0x103138b0`

_84 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fa48;

unsigned int sub_103138b0(int a0)
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
    *((char **)a0) = &g_1038fa48;
    v2 = 0;
    v12 = sub_10313910(g_1038e180 ^ &v3, a0, v10, sub_1036a0b8, -1, &v4);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v10;
    return v12;
}
```

## `sub_10313910` `0x10313910`

_32 bytes. (leaf/helper — see body)_

```c
extern char g_1038fa50;

int sub_10313910(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    *((char **)a0) = &g_1038fa50;
    return sub_1034ffca(a0, a0, &v1);
}
```

## `sub_10313930` `0x10313930`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10313930(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_10313910(v0);
    if (((char)a1 & 1))
        sub_10350abd(v0);
    return v0;
}
```

## `sub_10313960` `0x10313960`

_31 bytes. (leaf/helper — see body)_

```c
extern char g_1038fa58;

void* sub_10313960(void* a0)
{
    *((char **)(-0x8 + (char *)a0 + *((int *)((int)a0[8] + 4)))) = &g_1038fa58;
    return a0;
}
```

## `sub_10313980` `0x10313980`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10313980(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_103138b0(v0);
    if (((char)a1 & 1))
        sub_10350abd(v0);
    return v0;
}
```

## `sub_103139b0` `0x103139b0`

_53 bytes. (leaf/helper — see body)_

```c
int sub_103139b0(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_10313880(v0 - 8);
    if (((char)a1 & 1))
        sub_10350abd(v0 - 8);
    return v0 - 8;
}
```

## `sub_103139f0` `0x103139f0`

_141 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern int g_103994a4;

unsigned int sub_103139f0(int a0)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4137
    unsigned long v12;  // 4151
    unsigned int v13;  // eax
    unsigned long v14;  // 4113
    int v0;  // [bp-0x6c]
    int v1;  // [bp-0x68]
    char v2;  // [bp-0x64]
    char v3;  // [bp-0x38]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036a0e8;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    sub_10334530(a0, g_1038e180 ^ &v7);
    v1 = sub_103165c0(&v3, a0);
    v0 = v1;
    v6 = 0;
    sub_10316620(&v2, v0);
    sub_103533ea(&v2, &g_103994a4);
    v6 = 4294967295;
    v13 = sub_103162f0(&v2, &g_103994a4);
    v14 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v14) = v4;
    return v13;
}
```

## `sub_10313a80` `0x10313a80`

_135 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fa60;

unsigned int [5] sub_10313a80(unsigned int *idx, unsigned int *index)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4146
    unsigned int v8;  // eax
    unsigned long v9;  // 4162
    unsigned long v10;  // 4171
    unsigned int v0[5];  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v8 = *((int *)v7);
    v1 = *((int *)v7);
    v0 = idx;
    v9 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v9) = &v1;
    *(idx) = &g_1038fa60;
    sub_10313bd0(index + 1, g_1038e180 ^ &v2, idx, v8, sub_1036a11b, -1, &v3);
    idx[2] = index[2];
    idx[3] = index[3];
    idx[4] = index[4];
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v10) = v8;
    return idx;
}
```

## `sub_10313b10` `0x10313b10`

_19 bytes. (leaf/helper — see body)_

```c
void sub_10313b10(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10313b30(a0, &v1);
    return;
}
```

## `sub_10313b30` `0x10313b30`

_36 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    struct struct_0 *field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[16];
    struct struct_1 *field_10;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

struct_2 ** sub_10313b30(struct_2 **a0)
{
    struct_2 **v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    if (*(a0))
        a0 = *(a0)->field_0->field_10(a0, &v1);
    return a0;
}
```

## `sub_10313b60` `0x10313b60`

_25 bytes. (leaf/helper — see body)_

```c
extern char g_1038fa68;

int sub_10313b60(unsigned int a0)
{
    *((char **)a0) = &g_1038fa68;
    return a0;
}
```

## `sub_10313b80` `0x10313b80`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10313b80(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10313bb0(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_10313bb0` `0x10313bb0`

_20 bytes. (leaf/helper — see body)_

```c
extern char g_1038fa68;

int sub_10313bb0(unsigned int a0)
{
    *((char **)a0) = &g_1038fa68;
    return a0;
}
```

## `sub_10313bd0` `0x10313bd0`

_34 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_10313bd0(unsigned int *a0, unsigned int *a1)
{
    unsigned int *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    *(a0) = *(a1);
    sub_10313c00(a0, &v1);
    return a0;
}
```

