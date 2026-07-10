# elfbot.dll decompiled — jiru 0x1033e060..0x1033f430

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1033e060` `0x1033e060`

_138 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

void sub_1033e060(int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4140
    unsigned int v10;  // eax
    unsigned long v11;  // 4156
    unsigned long v12;  // 4113
    int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x8], Other Possible Types: unsigned int
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v2 = 4294967295;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v10 = *((int *)v9);
    v1 = *((int *)v9);
    v0 = a0;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v1;
    v2 = 4;
    sub_1033e0f0(g_1038e180 ^ &v3, a0, v10, sub_1036fef7, 3, &v4);
    sub_1033e1c0(g_1038e180 ^ &v3, a0, v10, sub_1036fef7, 2, &v4);
    v2 = 1;
    sub_10314610(a0 + 52);
    v2 = 0;
    sub_1033e140();
    v2 = 4294967295;
    sub_1033e1a0();
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v10;
    return;
}
```

## `sub_1033e0f0` `0x1033e0f0`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_1033e0f0(int a0)
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
    v12 = sub_1033e250(g_1038e180 ^ &v3, a0, v10, sub_1036ff28, -1, &v4);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v10;
    return v12;
}
```

## `sub_1033e140` `0x1033e140`

_87 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_1033e140(unsigned int *a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4142
    unsigned int v10;  // eax
    unsigned long v11;  // 4158
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    unsigned int *v0;  // [bp-0x14]
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
    *(a0) = 0;
    v12 = sub_1033e270(g_1038e180 ^ &v3, a0, v10, sub_1036ff5b, -1, &v4);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v10;
    return v12;
}
```

## `sub_1033e1a0` `0x1033e1a0`

_19 bytes. (leaf/helper — see body)_

```c
void sub_1033e1a0(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1033e290(a0, &v1);
    return;
}
```

## `sub_1033e1c0` `0x1033e1c0`

_92 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390a2c;

unsigned int sub_1033e1c0(unsigned int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned int v10;  // eax
    unsigned long v11;  // 4154
    unsigned int v12;  // eax
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
    *((char **)a0) = &g_10390a2c;
    sub_1033edf0(g_1038e180 ^ &v3, a0, v10, sub_1036ff88, 0, &v4);
    v2 = 4294967295;
    v12 = sub_10312c70(a0);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v10;
    return v12;
}
```

## `sub_1033e220` `0x1033e220`

_44 bytes. (leaf/helper — see body)_

```c
int sub_1033e220(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_1033e1c0(v0);
    if (((char)a1 & 1))
        sub_10350abd(v0);
    return v0;
}
```

## `sub_1033e250` `0x1033e250`

_19 bytes. (leaf/helper — see body)_

```c
void sub_1033e250(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1033e300(a0, &v1);
    return;
}
```

## `sub_1033e270` `0x1033e270`

_19 bytes. (leaf/helper — see body)_

```c
void sub_1033e270(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1033e330(a0, &v1);
    return;
}
```

## `sub_1033e290` `0x1033e290`

_110 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    int field_8;
    unsigned int field_c;
} struct_0;

struct_0 * sub_1033e290(struct_0 *a0)
{
    struct_0 *idx;  // [bp-0x8]

    idx = a0;
    idx = a0;
    if (idx->field_4)
    {
        sub_1033e3a0(idx->field_4, idx->field_8);
        sub_1033e3d0(idx->field_4, (idx->field_c - idx->field_4) / 100);
    }
    idx->field_4 = 0;
    idx->field_8 = 0;
    idx->field_c = 0;
    return idx;
}
```

## `sub_1033e300` `0x1033e300`

_35 bytes. (leaf/helper — see body)_

```c
char * sub_1033e300(char *a0)
{
    char *v2;  // eax
    char v0;  // [bp-0x6]

    v2 = a0;
    if (*(v2))
        v2 = sub_1033e3f0(_INSERT(0, 0, v0));
    return v2;
}
```

## `sub_1033e330` `0x1033e330`

_103 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    int field_8;
    unsigned int field_c;
} struct_0;

struct_0 * sub_1033e330(struct_0 *a0)
{
    struct_0 *idx;  // [bp-0x8]

    idx = a0;
    idx = a0;
    if (idx->field_4)
    {
        sub_1033e420(idx->field_4, idx->field_8);
        sub_1033e3d0(idx->field_4, idx->field_c - idx->field_4 >> 2);
    }
    idx->field_4 = 0;
    idx->field_8 = 0;
    idx->field_c = 0;
    return idx;
}
```

## `sub_1033e3a0` `0x1033e3a0`

_33 bytes. (leaf/helper — see body)_

```c
int sub_1033e3a0(int a0, int a1, int a2)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_1033f030(a1, a2, a0, a0, &v1);
}
```

## `sub_1033e3d0` `0x1033e3d0`

_25 bytes. (leaf/helper — see body)_

```c
int sub_1033e3d0(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10350abd(a1, a0, &v1);
}
```

## `sub_1033e3f0` `0x1033e3f0`

_34 bytes. (leaf/helper — see body)_

```c
char * sub_1033e3f0(char *a0)
{
    char *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_103130c0(sub_10331570(v0));
    *(v0) = 0;
    return v0;
}
```

## `sub_1033e420` `0x1033e420`

_33 bytes. (leaf/helper — see body)_

```c
int sub_1033e420(int a0, int a1, int a2)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_1033f070(a1, a2, a0, a0, &v1);
}
```

## `sub_1033e450` `0x1033e450`

_502 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[60];
    int field_3c;
} struct_0;

unsigned int * sub_1033e450(struct_0 *a0, unsigned int *a1, unsigned int a2, unsigned int a3, unsigned int a4)
{
    int v1;  // eax
    int v2;  // eax
    int v11;  // eax
    unsigned int v3;  // eax
    unsigned int v4;  // eax
    int v5;  // eax
    int v6;  // eax
    unsigned int v7;  // esi
    int v8;  // eax
    unsigned int v9;  // eax
    unsigned int v10;  // eax
    struct_0 *idx;  // [bp-0x8]

    idx = a0;
    idx = a0;
    if (sub_103131c0(idx))
    {
        v1 = sub_103131c0(idx);
        if (idx->field_3c < v1)
            idx->field_3c = sub_103131c0(idx);
    }
    if (((char)a4 & 1) && sub_103131a0(idx))
    {
        if (a3 == 2)
        {
            v2 = sub_103131a0(idx);
            a2 += idx->field_3c - v2;
        }
        else
        {
            if (!a3)
            {
                v3 = sub_1033e650();
                a2 += v3 - sub_103131a0(idx);
            }
            else
            {
                if (a3 != 1 || ((char)a4 & 2))
                {
                    sub_10313310(a1, 4294967295);
                    return a1;
                }
            }
        }
        v4 = sub_1033e650();
        if (v4 <= sub_103131a0(idx) + a2 && !((v5 = sub_103131a0(idx), sub_103131a0(idx) + a2 > idx->field_3c)))
        {
            sub_103131e0(idx, a2);
            if (((char)a4 & 2) && sub_103131c0(idx))
            {
                v6 = sub_103131a0(idx);
                v7 = v6 - sub_103131c0(idx);
                sub_103132a0(idx, v7);
            }
        }
        else
        {
            a2 = 4294967295;
        }
    }
    else if (((char)a4 & 2) && sub_103131c0(idx))
    {
        if (a3 == 2)
        {
            v8 = sub_103131c0(idx);
            a2 += idx->field_3c - v8;
        }
        else if (!a3)
        {
            v9 = sub_1033e670();
            a2 += v9 - sub_103131c0(idx);
        }
        else if (a3)
        {
            sub_10313310(a1, 4294967295);
            return a1;
        }
        v10 = sub_1033e670();
        if (v10 <= sub_103131c0(idx) + a2 && !((v11 = sub_103131c0(idx), sub_103131c0(idx) + a2 > idx->field_3c)))
            sub_103132a0(idx, a2);
        else
            a2 = 4294967295;
    }
    else
    {
        a2 = 4294967295;
    }
    sub_10313310(a1, a2);
    return a1;
}
```

## `sub_1033e650` `0x1033e650`

_19 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[16];
    struct struct_1 *field_10;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_1033e650(struct_0 *a0)
{
    return a0->field_10->field_0;
}
```

## `sub_1033e670` `0x1033e670`

_19 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    struct struct_1 *field_14;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_1033e670(struct_0 *a0)
{
    return a0->field_14->field_0;
}
```

## `sub_1033e690` `0x1033e690`

_350 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[60];
    int field_3c;
} struct_0;

unsigned int * sub_1033e690(struct_0 *a0, unsigned int *a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8)
{
    int v2;  // eax
    int v3;  // eax
    int v4;  // eax
    unsigned int v5;  // esi
    int v6;  // eax
    unsigned int v7;  // esi
    int v8;  // eax
    int v9;  // eax
    unsigned int v10;  // esi
    int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0x8]

    v1 = sub_1033e7f0(v0, a0);
    if (sub_103131c0(a0))
    {
        v2 = sub_103131c0(a0);
        if (a0->field_3c < v2)
            a0->field_3c = sub_103131c0(a0);
    }
    if (v1 == 4294967295)
    {
        sub_10313310(a1, 4294967295);
        return a1;
    }
    if (((char)a8 & 1) && sub_103131a0(a0))
    {
        if (v1 >= 0 && !((v3 = sub_1033e650(a0), v1 > a0->field_3c - sub_1033e650(a0))))
        {
            v4 = sub_1033e650(a0);
            v5 = v4 - sub_103131a0(a0) + v1;
            sub_103131e0(a0, v5);
            if (((char)a8 & 2) && sub_103131c0(a0))
            {
                v6 = sub_103131a0(a0);
                v7 = v6 - sub_103131c0(a0);
                sub_103132a0(a0, v7);
            }
        }
        else
        {
            v1 = 4294967295;
        }
    }
    else if (((char)a8 & 2) && sub_103131c0(a0))
    {
        if (v1 >= 0 && !((v8 = sub_1033e650(a0), v1 > a0->field_3c - sub_1033e650(a0))))
        {
            v9 = sub_1033e650(a0);
            v10 = v9 - sub_103131c0(a0) + v1;
            sub_103132a0(a0, v10);
        }
        else
        {
            v1 = 4294967295;
        }
    }
    else
    {
        v1 = 4294967295;
    }
    sub_10313310(a1, v1);
    return a1;
}
```

## `sub_1033e7da` `0x1033e7da`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1033e7da(void)
{
}
```

## `sub_1033e7f0` `0x1033e7f0`

_22 bytes. (leaf/helper — see body)_

```c
int sub_1033e7f0(unsigned int *a0)
{
    return a0[2] + *(a0);
}
```

## `sub_1033e810` `0x1033e810`

_231 bytes. (leaf/helper — see body)_

```c
int sub_1033e810(void* a0)
{
    int v2;  // eax
    int v3;  // eax
    unsigned int v4;  // eax
    unsigned int v5;  // eax
    unsigned int v6;  // eax
    unsigned int v7;  // eax
    void* v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    if (!sub_103131a0(v0))
        return sub_1032fd20();
    v2 = sub_103131a0(v0);
    if (v2 < sub_1033e910())
        return sub_10312da0(sub_103131a0(v0));
    if (!((char)(int)v0[0x44] & 1) || !sub_103131c0(v0))
        return sub_1032fd20();
    v3 = sub_103131a0(v0);
    if (v3 < sub_103131c0(v0) || !((v4 = (unsigned int)sub_103131a0(v0), sub_103131a0(v0) >= (int)v0[60])))
    {
        v5 = sub_103131c0(v0);
        if ((int)v0[60] < v5)
            *((int *)&v0[60]) = sub_103131c0(v0);
        v6 = sub_103131a0(v0);
        v7 = sub_1033e650(v0);
        sub_103135e0(v0, v7, v6, (int)v0[60]);
        return sub_10312da0(sub_103131a0(v0));
    }
    return sub_1032fd20();
}
```

## `sub_1033e82e` `0x1033e82e`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1033e82e(void)
{
}
```

## `sub_1033e85f` `0x1033e85f`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1033e85f(void)
{
}
```

## `sub_1033e8f7` `0x1033e8f7`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1033e8f7(void)
{
}
```

## `sub_1033e910` `0x1033e910`

_29 bytes. (leaf/helper — see body)_

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

int sub_1033e910(struct_0 *a0)
{
    return a0->field_20->field_0 + a0->field_30->field_0;
}
```

## `sub_1033e930` `0x1033e930`

_233 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[32];
    struct struct_1 *field_20;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

unsigned int sub_1033e930(struct_0 *a0)
{
    int v4;  // eax
    char v5;  // al
    unsigned int v0;  // [bp-0x10]
    char v1;  // [bp-0x9]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp+0x4]

    if (sub_103131a0(a0))
    {
        v4 = sub_1033e650(a0);
        if (v4 < sub_103131a0(a0) && (((char)a0[1].field_20 & 2) || !((v2 = sub_1032fd20(), !(char)sub_10312db0(&v2, &v3) && (v1 = (char)sub_10312f00(&v3), !(char)sub_10338830(&v1, sub_103131a0(a0) - 1))))))
        {
            sub_103131e0(a0, 4294967295);
            v0 = sub_1032fd20();
            if ((char)sub_10312db0(&v0, &v3))
                return sub_1033ea20(&v3);
            v5 = sub_10312f00(&v3);
            *((char *)sub_103131a0(a0)) = v5;
            return sub_1033ea20(&v3);
        }
    }
    return sub_1032fd20();
}
```

## `sub_1033ea0c` `0x1033ea0c`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1033ea0c(void)
{
}
```

## `sub_1033ea20` `0x1033ea20`

_48 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1033ea20(unsigned int a0)
{
    unsigned int v1;  // ecx
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    v0 = v1;
    v2 = sub_1032fd20();
    v0 = (*((int *)a0) == v2 ? -(0 < sub_1032fd20()) + 1 : *((int *)a0));
    return v0;
}
```

## `sub_1033ea50` `0x1033ea50`

_672 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1033ea50(void* idx, unsigned int a1)
{
    unsigned int v11;  // esi
    int v12;  // eax
    unsigned int v14;  // eax
    int v15;  // eax
    int v16;  // eax
    unsigned int v0;  // [bp-0x3c]
    unsigned int v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x24]
    unsigned int v4;  // [bp-0x20]
    unsigned int v5;  // [bp-0x1c]
    unsigned int v6;  // [bp-0x18]
    unsigned int i;  // [bp-0x14]
    unsigned int v8;  // [bp-0x10]
    int v9;  // [bp-0xc]
    unsigned int v10;  // [bp-0x8]

    v1 = v11;
    v3 = sub_1032fd20();
    if ((char)sub_10312db0(&v3, &/* unsupported instruction */))
        return sub_1033ea20(&/* unsupported instruction */);
    if (sub_103131c0(idx))
    {
        v12 = sub_103131c0(idx);
        if (v12 < sub_1033ed80())
        {
            sub_1033ed20(sub_10312f00(&/* unsupported instruction */));
            return a1;
        }
    }
    if (!((char)(int)idx[0x44] & 2))
        return sub_1032fd20();
    if (!sub_103131c0(idx))
    {
        v2 = 0;
    }
    else
    {
        v14 = sub_1033ed80();
        v2 = v14 - sub_1033e650(idx);
    }
    v6 = v2;
    v8 = v6;
    i = v8 >> 1;
    if (i < 0x100)
        i = 0x100;
    v10 = 0;
    for (v9 = sub_1033e650(idx); i > 0 && sub_1032fd20() - i < v8; i >>= 1);
    if (i > 0)
    {
        v8 += i;
        v10 = sub_1033f0b0(v8, -(0 < (char)idx[64]) & v9);
    }
    if (v6 > 0)
        sub_1033ed00(v10, v9, v6);
    if ((char)idx[64])
    {
        v0 = v6;
        sub_1033e3d0(idx + 72, v9);
    }
    *((char *)&idx[64]) = 1;
    if (!v6)
    {
        *((unsigned int *)&idx[60]) = v10;
        sub_10313620(idx, v10, v10 + v8);
        if (((char)(int)idx[0x44] & 1))
            sub_103135e0(idx, v10, v10, v10 + 1);
        else
            sub_103135e0(idx, v10, 0, v10);
    }
    else
    {
        *((unsigned int *)&idx[60]) = (int)idx[60] - v9 + v10;
        v15 = sub_103131c0(idx);
        v5 = v15 - sub_1033e670(idx);
        v16 = sub_103131a0(idx);
        v4 = v16 - sub_1033e650(idx);
        sub_10313620(idx, sub_1033e670(idx) - v9 + v10, v10 + v8);
        sub_103132a0(idx, v5);
        if (((char)(int)idx[0x44] & 1))
            sub_103135e0(idx, v10, v10 + v4, sub_103131c0(idx) + 1);
        else
            sub_103135e0(idx, v10, 0, v10);
    }
    sub_1033ed20(sub_10312f00(&/* unsupported instruction */));
    return a1;
}
```

## `sub_1033ea8a` `0x1033ea8a`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1033ea8a(void)
{
}
```

## `sub_1033eace` `0x1033eace`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1033eace(void)
{
}
```

## `sub_1033eae8` `0x1033eae8`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1033eae8(void)
{
}
```

## `sub_1033ed00` `0x1033ed00`

_29 bytes. (leaf/helper — see body)_

```c
int sub_1033ed00(int a0, int a1, int a2)
{
    return sub_103133a0(a0, a2, a1, a2);
}
```

## `sub_1033ed20` `0x1033ed20`

_95 bytes. (leaf/helper — see body)_

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

int sub_1033ed20(struct_0 *a0)
{
    int v3;  // eax
    int v0;  // [bp-0x10]
    char *v1;  // [bp-0x8]
    char v2;  // [bp+0x4], Other Possible Types: unsigned int

    if (sub_103132e0(a0) <= 0)
    {
        v3 = sub_10312da0(&v2);
        v0 = (*((int *)(*((int *)&a0->padding_0[0]) + 4)))(v3);
        return v0;
    }
    v1 = sub_1033eda0();
    *(v1) = v2;
    v0 = sub_10312da0(v1);
    return v0;
}
```

## `sub_1033ed80` `0x1033ed80`

_29 bytes. (leaf/helper — see body)_

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

int sub_1033ed80(struct_0 *a0)
{
    return a0->field_24->field_0 + a0->field_34->field_0;
}
```

## `sub_1033eda0` `0x1033eda0`

_65 bytes. (leaf/helper — see body)_

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

int sub_1033eda0(struct_0 *idx)
{
    unsigned int v0;  // [bp-0xc]

    idx->field_34->field_0 = idx->field_34->field_0 - 1;
    v0 = idx->field_24->field_0;
    idx->field_24->field_0 = idx->field_24->field_0 + 1;
    return v0;
}
```

## `sub_1033edf0` `0x1033edf0`

_137 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[60];
    unsigned int field_3c;
    char field_40;
} struct_0;

int sub_1033edf0(struct_0 *idx)
{
    int v4;  // eax
    unsigned int v0;  // [bp-0x10]
    int v1;  // [bp-0xc]

    if (idx->field_40)
    {
        v1 = (!sub_103131c0(idx) ? sub_1033e910(idx) : sub_1033ed80(idx));
        v0 = v1 - sub_1033e650(idx);
        sub_1033e3d0(&idx[1].padding_0[7], sub_1033e650(idx));
    }
    idx->field_40 = 0;
    sub_103135e0(idx, 0, 0, 0);
    v4 = sub_10313620(idx, 0, 0);
    idx->field_3c = 0;
    return v4;
}
```

## `sub_1033ee80` `0x1033ee80`

_237 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[80];
    char field_50;
} struct_0;

extern unsigned int g_1038e180;

struct_0 * sub_1033ee80(struct_0 *a0, int a1)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4136
    unsigned long v9;  // 4150
    unsigned long v10;  // 4120
    char v0;  // [bp-0x2c]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8], Other Possible Types: char
    char v4;  // [bp-0x4]

    v3 = 4294967295;
    v2 = sub_1036ffef;
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v1 = *((int *)v8);
    v9 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v9) = &v1;
    sub_1033f180(g_1038e180 ^ &v4, a0);
    v3 = 0;
    sub_1033f120(g_1038e180 ^ &v4, a0);
    v3 = 1;
    memset(&a0->padding_0[36], 0, 13);
    sub_10315800(&a0->padding_0[52]);
    v3 = 2;
    a0->field_50 = 255;
    sub_1033f1b0(3);
    v3 = 3;
    sub_1033f0d0(3);
    v3 = 4;
    if (a1)
    {
        sub_10314590(&v0, a1);
        v3 = 5;
        sub_1033f550(&v0);
        v3 = 4;
        sub_10314610(&v0);
    }
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v10) = v1;
    return a0;
}
```

## `sub_1033ef70` `0x1033ef70`

_29 bytes. (leaf/helper — see body)_

```c
int sub_1033ef70(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10340500(a0, a1, a0, &v1);
}
```

## `sub_1033ef90` `0x1033ef90`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1033ef90(int a0, unsigned int a1)
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
    sub_10340240(a0, g_1038e180 ^ &v2, 0, v8, sub_10370029, -1, &v3);
    v11 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v11) = v8;
    return a0;
}
```

## `sub_1033eff0` `0x1033eff0`

_29 bytes. (leaf/helper — see body)_

```c
int sub_1033eff0(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_103405a0(a0, a1, a0, &v1);
}
```

## `sub_1033f010` `0x1033f010`

_29 bytes. (leaf/helper — see body)_

```c
int sub_1033f010(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10340640(a0, a1, a0, &v1);
}
```

## `sub_1033f030` `0x1033f030`

_51 bytes. (leaf/helper — see body)_

```c
int sub_1033f030(int a0, int a1, int a2)
{
    unsigned int v4;  // ecx
    int v5;  // edx
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x5]

    v2 = v4;
    v1 = &/* unsupported instruction */;
    v0 = &/* unsupported instruction */;
    v3 = sub_10337970();
    v5 = _INSERT(0, 0, v3);
    return sub_103406e0(a0, a1, a2, v5);
}
```

## `sub_1033f070` `0x1033f070`

_51 bytes. (leaf/helper — see body)_

```c
void sub_1033f070(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v6;  // ecx
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x5]

    v4 = v6;
    v3 = &a1;
    v2 = &a0;
    v5 = sub_10337970();
    *((char *)&v3) = v5;
    v2 = a2;
    v1 = a1;
    v0 = a0;
    sub_10334530();
    return;
}
```

## `sub_1033f0b0` `0x1033f0b0`

_25 bytes. (leaf/helper — see body)_

```c
int sub_1033f0b0(int a0, int a1)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_10314c40(v0, a1);
}
```

## `sub_1033f0d0` `0x1033f0d0`

_78 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

char * sub_1033f0d0(char *a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4135
    unsigned long v11;  // 4151
    unsigned long v12;  // 4123
    unsigned int v0;  // [bp-0x18]
    char *v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_10370058;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    sub_1031a1d0(v1);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v2;
    return v1;
}
```

## `sub_1033f120` `0x1033f120`

_90 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int * sub_1033f120(unsigned int *a0)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4140
    unsigned int v9;  // eax
    unsigned long v10;  // 4156
    unsigned long v11;  // 4123
    unsigned int *v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v9 = *((int *)v8);
    v1 = *((int *)v8);
    v0 = a0;
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v10) = &v1;
    *(a0) = 0;
    sub_1033f230(g_1038e180 ^ &v2, a0, v9, sub_1037008b, -1, &v3);
    v11 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v11) = v9;
    return a0;
}
```

## `sub_1033f180` `0x1033f180`

_42 bytes. (leaf/helper — see body)_

```c
int sub_1033f180(unsigned int a0)
{
    unsigned int v0;  // [bp-0x10]

    v0 = a0;
    sub_1031a280(&v0);
    sub_103147d0(a0);
    sub_1033f260(0);
    return a0;
}
```

## `sub_1033f1b0` `0x1033f1b0`

_126 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[60];
    unsigned int field_3c;
    char field_40;
    char padding_41[3];
    unsigned int field_44;
} struct_0;

extern unsigned int g_1038e180;
extern char g_10390a2c;

struct_0 * sub_1033f1b0(struct_0 *a0, unsigned int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4135
    unsigned long v10;  // 4151
    unsigned long v11;  // 4120
    unsigned int v0;  // [bp-0x18]
    struct_0 *idx;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_103700b8;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    idx = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    idx = a0;
    sub_10313430(idx);
    v4 = 0;
    *((char **)&idx->padding_0[0]) = &g_10390a2c;
    idx->field_3c = 0;
    idx->field_40 = 0;
    idx->field_44 = a1;
    sub_1031a280(idx + 1);
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return idx;
}
```

## `sub_1033f230` `0x1033f230`

_42 bytes. (leaf/helper — see body)_

```c
int sub_1033f230(unsigned int a0)
{
    unsigned int v0;  // [bp-0x10]

    v0 = a0;
    sub_1031a280(&v0);
    sub_103147d0(a0);
    sub_1033f2e0(0);
    return a0;
}
```

## `sub_1033f260` `0x1033f260`

_123 bytes. (leaf/helper — see body)_

```c
char sub_1033f260(unsigned int *idx, int a1)
{
    unsigned int v0[4];  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = idx;
    memset(idx + 1, 0, 12);
    if (!a1)
        return 0;
    if (sub_1033f360(idx, &v1) < a1)
    {
        sub_1033f380();
    }
    else
    {
        idx[1] = sub_1033f410(a1);
        idx[2] = idx[1];
        idx[3] = a1 * 100 + idx[1];
    }
    return 1;
}
```

## `sub_1033f28f` `0x1033f28f`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1033f28f(void)
{
}
```

## `sub_1033f2e0` `0x1033f2e0`

_123 bytes. (leaf/helper — see body)_

```c
char sub_1033f2e0(unsigned int *idx, int a1)
{
    unsigned int v0[4];  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = idx;
    memset(idx + 1, 0, 12);
    if (!a1)
        return 0;
    if (sub_1033f430(idx, &v1) < a1)
    {
        sub_1033f450();
    }
    else
    {
        idx[1] = sub_1033f4d0(a1);
        idx[2] = idx[1];
        idx[3] = idx[1] + a1 * 4;
    }
    return 1;
}
```

## `sub_1033f30f` `0x1033f30f`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1033f30f(void)
{
}
```

## `sub_1033f360` `0x1033f360`

_19 bytes. (leaf/helper — see body)_

```c
void sub_1033f360(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1033f4f0(a0, &v1);
    return;
}
```

## `sub_1033f380` `0x1033f380`

_113 bytes. refs "vector<T> too long"_

```c
extern unsigned int g_1038e180;
extern int g_1039ce9c;

void sub_1033f380(void)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4137
    unsigned long v12;  // 4151
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x58]
    char v1;  // [bp-0x54]
    char v2;  // [bp-0x38]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_103700e8;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v3 = *((int *)v11);
    v0 = g_1038e180 ^ &v6;
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v3;
    sub_10314590(&v1, "vector<T> too long");
    v5 = 0;
    sub_10331a40(&v2, &v1);
    sub_103533ea(&v2, &g_1039ce9c);
    v5 = 4294967295;
    sub_10314610(&v1);
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v13) = v3;
    return;
}
```

## `sub_1033f400` `0x1033f400`

_16 bytes. (leaf/helper — see body)_

```c
int sub_1033f400(unsigned int a0)
{
    return a0;
}
```

## `sub_1033f410` `0x1033f410`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1033f410(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10340710(a1, 0, a0, &v1);
}
```

## `sub_1033f430` `0x1033f430`

_19 bytes. (leaf/helper — see body)_

```c
void sub_1033f430(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1033f520(a0, &v1);
    return;
}
```

