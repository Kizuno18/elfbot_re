# elfbot.dll decompiled — jiru 0x10323020..0x10323704

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10323020` `0x10323020`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323020(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032303d` `0x1032303d`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1032303d(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323064` `0x10323064`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323064(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032306b` `0x1032306b`

_3 bytes. (leaf/helper — see body)_

```c
void sub_1032306b(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323099` `0x10323099`

_58 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
} struct_0;

extern char g_103a292c;

int sub_10323099(void)
{
    struct_0 **v6;  // ecx
    struct_0 **v7;  // eax
    struct_0 **v0;  // [bp-0x8]
    int v1;  // [bp-0x4]
    int v3;  // [bp+0xffffc]
    struct_0 **v4;  // [bp+0x100000]
    struct_0 **v5;  // [bp+0x10000c]

    for (v4 = v6; v3 < *((int *)&g_103a292c) && (v7 = (struct_0 **)*(v4), v7 != v5); v4 += 1)
    {
        v3 += 1;
    }
    v1 = v3;
    v0 = v7;
}
```

## `sub_103230d8` `0x103230d8`

_150 bytes. (leaf/helper — see body)_

```c
extern char g_103a292c;

int sub_103230d8(unsigned int a0, unsigned int a1, int a2)
{
    unsigned int v8;  // cc_op
    unsigned int v9;  // cc_dep1
    int v18;  // ecx
    void* v19;  // ebp
    unsigned short v20;  // ax
    unsigned short v21;  // dx
    unsigned int v22;  // eax
    unsigned int v23;  // edx
    int v24;  // cc_dep1
    unsigned int v25;  // edi
    unsigned int v26;  // 4101
    unsigned int v27;  // 4103
    unsigned int v10;  // cc_dep2
    unsigned int v28;  // 4101
    unsigned int v29;  // 4101
    unsigned int v30;  // 4101
    unsigned int v31;  // 4101
    unsigned int v32;  // 4101
    unsigned int v33;  // 4101
    unsigned int v34;  // 4101
    unsigned int v35;  // 4101
    unsigned int v11;  // cc_ndep
    unsigned int v12;  // 4165
    unsigned int v13;  // id
    unsigned int v14;  // ac
    unsigned int v15;  // ebx
    unsigned int v16;  // esi
    unsigned int v17;  // 4110
    unsigned int v0;  // [bp-0x18]
    void* v1;  // [bp-0x14], Other Possible Types: unsigned int
    char *v2;  // [bp-0x10], Other Possible Types: void*
    char *v3;  // [bp-0xc], Other Possible Types: unsigned int
    unsigned int v4;  // [bp-0x8]
    int v5;  // [bp-0x4], Other Possible Types: unsigned int
    int v6;  // [bp+0x0], Other Possible Types: unsigned int
    char v7;  // [bp+0x8]

    v12 = _ccall(v8, v9, v10, v11);
    a2 = v12 | 0x202 | v13 * 0x200000 & 0x200000 | v14 * 0x40000 & 0x40000;
    v5 = a2;
    v4 = a1;
    v3 = v15;
    v2 = &a2;
    v0 = v16;
    if (!(1))
        goto LABEL_103230f2;
LABEL_103230f2:
    for (; (v17 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v17 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
    v18 = v5;
    v19 = v1;
    v20 = v4;
    v21 = v6;
    v22 = _INSERT(v20 CONCAT 0, 0, v21);
    v23 = _INSERT(v21 CONCAT 0, 0, v20);
    v24 = (int)v19[8];
    if ((int)v19[8] > 0)
    {
        __unsupported_jumpkind_Ijk_NoDecode()
        if (v18 < *((int *)&g_103a292c))
        {
            a2 = v22;
            v6 = v18;
            v5 = v23;
            v4 = v3;
            v3 = &v7;
            v2 = v19 - 1;
            v1 = v0;
            v0 = v25;
            v26 = _ccall(0, 15, 0, 0, 0);
            if ((char)v26)
                goto LABEL_1032314e;
            else
                goto LABEL_1032314f;
            while (true)
            {
LABEL_1032314e:
                __unsupported_jumpkind_Ijk_NoDecode()
                while (true)
                {
LABEL_1032314f:
                    v27 = _ccall(10, 15, 0, 0, 0);
                    if (!((char)v27))
                    {
                        __unsupported_jumpkind_Ijk_NoDecode()
                        __unsupported_jumpkind_Ijk_NoDecode()
                        return sub_10323162((int)v2[8] * 4);
                    }
                    v28 = _ccall(8, 15, 0, 0, 0);
                    if (!((char)v28))
                    {
                        if (false)
                        {
                            __unsupported_jumpkind_Ijk_NoDecode()
                            return sub_10323162((int)v2[8] * 4);
                        }
                        v29 = _ccall(10, 15, 0, 0, 0);
                        if (!((char)v29))
                        {
                            v30 = _ccall(0, 15, 0, 0, 0);
                            if ((char)v30)
                                break;
                            else
                                continue;
                        }
                        else
                        {
                            v31 = _ccall(8, 15, 0, 0, 0);
                            if (!((char)v31))
                                return sub_10323162((int)v2[8] * 4);
                        }
                    }
                    else
                    {
                        __unsupported_jumpkind_Ijk_NoDecode()
                        v32 = _ccall(8, 15, 0, 0, 0);
                        if (!((char)v32))
                            return sub_10323162((int)v2[8] * 4);
                    }
                    if ((v33 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v33))
                        break;
                }
            }
        }
        v34 = _ccall(0, 6, v18, *((int *)&g_103a292c), 0);
        if ((char)v34 || v18 < *((int *)&g_103a292c) && v18 != *((int *)&g_103a292c))
            goto LABEL_103231d8;
    }
    else
    {
        v35 = _ccall(0, 6, v24, 0, 0);
        if ((char)v35 || v24 < 0 && v24)
LABEL_103231d8:
    }
}
```

## `sub_103230ed` `0x103230ed`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103230ed(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103230f4` `0x103230f4`

_3 bytes. (leaf/helper — see body)_

```c
void sub_103230f4(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323142` `0x10323142`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323142(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323162` `0x10323162`

_46 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a2930;

int sub_10323162(void)
{
    unsigned int v12;  // eax
    unsigned int v13;  // 4110
    unsigned int v14;  // id
    unsigned int v15;  // ac
    unsigned int v16;  // ecx
    unsigned int v17;  // edx
    unsigned int v18;  // ebx
    unsigned int v19;  // esi
    unsigned int v20;  // edi
    unsigned int v21;  // 4104
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    unsigned int v6;  // [bp-0x4]
    unsigned int v7;  // [bp+0x0]
    unsigned int v8;  // [bp+0x0]
    char v10;  // [bp+0x10]

    v6 = v12;
    v5 = g_103a2930 + 4;
    v7 = sub_10350ec0(g_103a2930 + 4);
    if (&v10 >= NULL)
        goto LABEL_1032317d;
LABEL_1032317d:
    v13 = _ccall(3, &v5, 12, 0);
    v8 = v13 | 0x202 | v14 * 0x200000 & 0x200000 | v15 * 0x40000 & 0x40000;
    v6 = v7;
    v5 = v16;
    v4 = v17;
    v3 = v18;
    v2 = /* unsupported instruction */;
    v1 = v19;
    v0 = v20;
    v21 = _ccall(0, 6, v17, v17, 0);
    if (!((char)v21))
    {
        __unsupported_jumpkind_Ijk_NoDecode()
        if (v16 == 1)
            goto LABEL_0x103231a6;
    }
    if (0)
        goto LABEL_0x1032319b;
}
```

## `sub_10323186` `0x10323186`

_17 bytes. (leaf/helper — see body)_

```c
void sub_10323186(void)
{
    if (!(1))
        goto LABEL_1032318a;
LABEL_1032318a:
}
```

## `sub_10323194` `0x10323194`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323194(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103231a8` `0x103231a8`

_35 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[8];
    unsigned int field_8;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_103a2930;

int sub_103231a8(void)
{
    unsigned int v3;  // cc_dep1
    unsigned int v4;  // 4173
    struct_1 *v1;  // [bp+0x8]
    unsigned int v2;  // [bp+0x20]

    v3 = v2 & 2261;
    g_103a2930->field_0 = v1->field_8;
    v4 = _ccall(0, 0, v2 & 2261, 0, 0);
}
```

## `sub_103231ac` `0x103231ac`

_2 bytes. (leaf/helper — see body)_

```c
void sub_103231ac(void)
{
}
```

## `sub_103231ae` `0x103231ae`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103231ae(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103231ca` `0x103231ca`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103231ca(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103231d5` `0x103231d5`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103231d5(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103231e1` `0x103231e1`

_5 bytes. (leaf/helper — see body)_

```c
void sub_103231e1(void)
{
}
```

## `sub_103231f8` `0x103231f8`

_5 bytes. (leaf/helper — see body)_

```c
void sub_103231f8(void)
{
}
```

## `sub_1032320f` `0x1032320f`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1032320f(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323245` `0x10323245`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323245(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032324c` `0x1032324c`

_3 bytes. (leaf/helper — see body)_

```c
void sub_1032324c(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032329d` `0x1032329d`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1032329d(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103232b1` `0x103232b1`

_124 bytes. (leaf/helper — see body)_

```c
int sub_103232b1(void)
{
    unsigned int v6;  // 4097
    unsigned int v7;  // d
    unsigned int v8;  // id
    unsigned int v9;  // ac
    unsigned int v10;  // eax
    unsigned int v11;  // 4110
    unsigned int v12;  // cc_dep1
    unsigned int v13;  // 4140
    unsigned int v14;  // 4101
    unsigned int v15;  // 4101
    void* v1;  // [bp+0x8]
    char *v2;  // [bp+0xc]
    unsigned int v3;  // [bp+0x18]
    unsigned int v4;  // [bp+0x1c]
    unsigned int v5;  // [bp+0x20]

    v6 = v5;
    v7 = ((char)(v6 >> 10) ? 4294967295 : 1);
    v8 = ((char)(v6 >> 21) ? 1 : 0);
    v9 = ((char)(v6 >> 18) ? 1 : 0);
    v10 = v4 * 0x1000000 | v4 * 0x100 & 0xff0000 | v4 >> 8 & 0xff00 | v4 >> 24 & 0xff;
    *((unsigned int *)&v1[12]) = 0;
    *((unsigned int *)&v1[20]) = 0;
    v5 = ~(~(v3));
    v4 = v10 * 0x1000000 | v10 * 0x100 & 0xff0000 | v10 >> 8 & 0xff00 | v10 >> 24 & 0xff;
    v5 = v6 & 2261 | 0x202 | ((char)(v6 >> 10) ? 4294967295 : 1) & 0x400 | ((char)(v6 >> 21) ? 1 : 0) * 0x200000 & 0x200000 | ((char)(v6 >> 18) ? 1 : 0) * 0x40000 & 0x40000;
    v3 = ~(~(v3));
    v2 = &v5;
    if (!(1))
        goto LABEL_103232f7;
LABEL_103232f7:
    for (; (v11 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v11 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
    v12 = (v6 & 2261 | 0x202 | v7 & 0x400 | v8 * 0x200000 & 0x200000 | v9 * 0x40000 & 0x40000) & 2261;
    v13 = _ccall(0, 0, (v6 & 2261 | 0x202 | v7 & 0x400 | v8 * 0x200000 & 0x200000 | v9 * 0x40000 & 0x40000) & 2261, 0, 0);
    if (!((char)v13))
    {
        v14 = _ccall(12, 0, v12, 0, 0);
        if (!((char)v14))
        {
            sub_10323335(0x1000, 4, v1 - 12);
            return;
        }
        v15 = _ccall(4, 0, v12, 0, 0);
        if ((char)v15)
        {
            sub_10323335(0x1000, 4, v1 - 12);
            return;
        }
    }
    sub_10323335(0x1000, 4, v1 - 12);
    return;
}
```

## `sub_103232b5` `0x103232b5`

_2 bytes. (leaf/helper — see body)_

```c
void sub_103232b5(void)
{
}
```

## `sub_103232b7` `0x103232b7`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103232b7(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103232f9` `0x103232f9`

_3 bytes. (leaf/helper — see body)_

```c
void sub_103232f9(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323322` `0x10323322`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323322(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323335` `0x10323335`

_60 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b0c4;

int sub_10323335(void)
{
    unsigned int v11;  // ecx
    unsigned int *v12;  // edx
    unsigned int v21;  // ebx
    unsigned int v22;  // esi
    unsigned int v23;  // edi
    unsigned int v24;  // cc_op
    unsigned int v25;  // 4104
    unsigned int *v26;  // cc_dep1
    unsigned int v27;  // cc_dep2
    unsigned int v29;  // 4101
    unsigned int v13;  // cc_op
    unsigned int v14;  // cc_dep1
    unsigned int v15;  // cc_dep2
    unsigned int v16;  // cc_ndep
    unsigned int v17;  // 4123
    unsigned int v18;  // 4110
    unsigned int v19;  // id
    unsigned int v20;  // ac
    unsigned int v0;  // [bp-0x2c]
    unsigned int v1;  // [bp-0x28]
    char *v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x1c]
    unsigned int *v4;  // [bp-0x18]
    unsigned int v5;  // [bp-0x14]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0xc]
    unsigned int v9;  // [bp-0x4]

    v9 = v11;
    v7 = g_1038b0c4(*(v12));
    v17 = _ccall(2, v13, v14, v15, v16);
    if (!((char)v17))
        goto LABEL_1032334d;
LABEL_1032334d:
    v18 = _ccall(v13, v14, v15, v16);
    v8 = v18 | 0x202 | v19 * 0x200000 & 0x200000 | v20 * 0x40000 & 0x40000;
    v6 = v7;
    v5 = v11;
    v4 = v12;
    v3 = v21;
    v2 = &v8;
    v1 = v22;
    v0 = v23;
    v24 = 6;
    v25 = _ccall(0, 6, v12, v12, 0);
    v26 = v12;
    if (!((char)v25))
    {
        if (!(1))
            goto LABEL_1032335a;
LABEL_1032335a:
        v24 = 15;
        v26 = 0x3;
        v27 = 0;
    }
    v29 = _ccall(2, v24, v26, v27, 0);
    if ((char)v29)
        goto LABEL_0x1032336b;
}
```

## `sub_10323364` `0x10323364`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323364(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323378` `0x10323378`

_17 bytes. (leaf/helper — see body)_

```c
int sub_10323378(void)
{
    sub_1032338c();
    return;
}
```

## `sub_1032337c` `0x1032337c`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032337c(void)
{
}
```

## `sub_1032337e` `0x1032337e`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1032337e(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032338c` `0x1032338c`

_73 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b0c4;
extern struct_0 *g_1038c8ac;

int sub_1032338c(void)
{
    unsigned int v11;  // ecx
    unsigned int v12;  // edx
    unsigned int v21;  // 4101
    unsigned int v22;  // 4101
    unsigned int v23;  // 4101
    unsigned int v13;  // ebx
    unsigned int v14;  // esi
    unsigned int v15;  // edi
    unsigned int v16;  // 4101
    unsigned int v17;  // 4103
    unsigned int v18;  // 4101
    unsigned int v19;  // 4101
    unsigned int v20;  // 4101
    unsigned int v0;  // [bp-0x34]
    unsigned int v1;  // [bp-0x30]
    char *v2;  // [bp-0x28]
    unsigned int v3;  // [bp-0x24]
    unsigned int v4;  // [bp-0x20]
    unsigned int v5;  // [bp-0x1c]
    unsigned int v6;  // [bp-0x18]
    unsigned int v7;  // [bp-0x14]
    unsigned int v9;  // [bp+0xffff4]
    unsigned int v10;  // [bp+0xffff8]

    v7 = g_1038c8ac->field_0;
    v6 = g_1038b0c4(g_1038c8ac->field_0, v9, 0x1000, v10, v11);
    v5 = v11;
    v4 = v12;
    v3 = v13;
    v2 = &v7;
    v1 = v14;
    v0 = v15;
    v16 = _ccall(0, 15, 0, 0, 0);
    if ((char)v16)
        goto LABEL_103233c7;
    else
        goto LABEL_103233c8;
    while (true)
    {
LABEL_103233c7:
        __unsupported_jumpkind_Ijk_NoDecode()
        while (true)
        {
LABEL_103233c8:
            v17 = _ccall(10, 15, 0, 0, 0);
            if (!((char)v17))
            {
                __unsupported_jumpkind_Ijk_NoDecode()
                __unsupported_jumpkind_Ijk_NoDecode()
            }
            v18 = _ccall(8, 15, 0, 0, 0);
            if (!((char)v18))
            {
                if (false)
                    __unsupported_jumpkind_Ijk_NoDecode()
                v19 = _ccall(10, 15, 0, 0, 0);
                if (!((char)v19))
                {
                    v20 = _ccall(0, 15, 0, 0, 0);
                    if ((char)v20)
                        break;
                    else
                        continue;
                }
                else
                {
                    v21 = _ccall(8, 15, 0, 0, 0);
                }
            }
            else
            {
                __unsupported_jumpkind_Ijk_NoDecode()
                v22 = _ccall(8, 15, 0, 0, 0);
            }
            if ((v23 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v23))
                break;
        }
    }
}
```

## `sub_103233bb` `0x103233bb`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103233bb(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103233fe` `0x103233fe`

_33 bytes. (leaf/helper — see body)_

```c
void sub_103233fe(unsigned int a0, unsigned int a1)
{
    unsigned int v9;  // cc_op
    unsigned int v10;  // cc_dep1
    unsigned int v19;  // edi
    unsigned int v20;  // cc_op
    unsigned int v21;  // 4104
    unsigned int v22;  // cc_dep1
    unsigned int v24;  // 4101
    unsigned int v11;  // cc_dep2
    unsigned int v12;  // cc_ndep
    unsigned int v13;  // 4110
    unsigned int v14;  // id
    unsigned int v15;  // ac
    unsigned int v16;  // eax
    unsigned int v17;  // ebx
    unsigned int v18;  // esi
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    char *v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    unsigned int v7;  // [bp-0x4]

    v13 = _ccall(v9, v10, v11, v12);
    v7 = v13 | 0x202 | v14 * 0x200000 & 0x200000 | v15 * 0x40000 & 0x40000;
    v6 = v16;
    v5 = a0;
    v4 = a1;
    v3 = v17;
    v2 = &v7;
    v1 = v18;
    v0 = v19;
    v20 = 6;
    v21 = _ccall(0, 6, a1, a1, 0);
    v22 = a1;
    if (!((char)v21))
    {
        if (!(1))
            goto LABEL_1032340b;
LABEL_1032340b:
        v20 = 15;
        v22 = 3;
        a1 = 0;
        if (0)
            goto LABEL_0x103233a3;
        else
            goto LABEL_10323413;
    }
LABEL_10323413:
    v24 = _ccall(2, v20, v22, a1, 0);
    if ((char)v24)
        goto LABEL_0x1032341c;
    else
        goto LABEL_0x10323416;
}
```

## `sub_10323415` `0x10323415`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10323415(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323429` `0x10323429`

_93 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[748880320];
    char field_2ca301c0;
} struct_0;

extern unsigned int g_103a2928;

int sub_10323429(void)
{
    unsigned int *v10;  // edx
    struct_0 *idx;  // ebx
    unsigned int v20;  // 4101
    char v21;  // 4117
    unsigned int v22;  // 4099
    unsigned int v23;  // 4109
    unsigned int v24;  // 4101
    unsigned int v12;  // eax
    unsigned int v13;  // 4101
    unsigned int v14;  // 4103
    unsigned int v15;  // 4101
    unsigned int v16;  // 4101
    unsigned int v17;  // 4101
    unsigned int v18;  // 4101
    unsigned int v19;  // 4101
    unsigned int v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x4]
    unsigned int v2;  // [bp+0x8]
    unsigned int v3;  // [bp+0xc]
    char *v4;  // [bp+0x10], Other Possible Types: struct_0 *
    struct_0 *v5;  // [bp+0x14], Other Possible Types: unsigned int *
    unsigned int *v6;  // [bp+0x18], Other Possible Types: unsigned int
    unsigned int v7;  // [bp+0x1c]
    unsigned int v8;  // [bp+0x20]
    char v9;  // [bp+0x24]

    v10 = v5;
    idx = v4;
    v12 = v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff;
    v8 = v12 * 0x1000000 | v12 * 0x100 & 0xff0000 | v12 >> 8 & 0xff00 | v12 >> 24 & 0xff;
    v7 = ~(~(v6));
    v6 = v10;
    v5 = idx;
    v4 = &v9;
    v3 = v2;
    v2 = v1;
    v1 = v0;
LABEL_10323456:
    v13 = _ccall(0, 15, 0, 0, 0);
    if ((char)v13)
        goto LABEL_10323458;
    else
        goto LABEL_10323459;
    while (true)
    {
LABEL_10323458:
        __unsupported_jumpkind_Ijk_NoDecode()
        while (true)
        {
LABEL_10323459:
            v14 = _ccall(10, 15, 0, 0, 0);
            if (!((char)v14))
            {
                v21 = *(0x2ca16133);
                v22 = *(v10);
                *(v10) = *(v10) - v1;
                idx->field_2ca301c0 = idx->field_2ca301c0 + v21 + (v22 < v1);
                v23 = *(v10);
                *(v10) = v23 - v1;
                *((char *)(*(0x2ca16133) + 7)) = *((char *)(*(0x2ca16133) + 7)) + *((char *)((void*)&v10 + 1)) + (v23 < v1);
                v24 = _ccall(12, 7, (unsigned int)(char)*((char *)(unsigned int)(char)(*((char *)0x2ca16133) + 7)), (unsigned int)(*((char *)((void*)&v10 + 1)) ^ (char)(char)(v23 < v1)), (unsigned int)(char)(v23 < v1));
                sub_1032348b(g_103a2928 * 4 - 4);
                return;
            }
            v15 = _ccall(8, 15, 0, 0, 0);
            if (!((char)v15))
            {
                if (!(1))
                    goto LABEL_0x1032345e;
                v16 = _ccall(10, 15, 0, 0, 0);
                if (!((char)v16))
                {
                    v17 = _ccall(0, 15, 0, 0, 0);
                    if ((char)v17)
                        break;
                    else
                        continue;
                }
                else
                {
                    v18 = _ccall(8, 15, 0, 0, 0);
                    if ((char)v18)
                        goto LABEL_10323456;
                    else
                        goto LABEL_0x1032345f;
                }
            }
            else
            {
                __unsupported_jumpkind_Ijk_NoDecode()
                v19 = _ccall(8, 15, 0, 0, 0);
                if ((char)v19)
                    goto LABEL_10323456;
                else
                    goto LABEL_0x1032345f;
            }
LABEL_10323456:
            if ((v20 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v20))
                break;
        }
    }
}
```

## `sub_1032342d` `0x1032342d`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032342d(void)
{
}
```

## `sub_1032342f` `0x1032342f`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1032342f(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032344c` `0x1032344c`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1032344c(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323473` `0x10323473`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323473(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032348b` `0x1032348b`

_102 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a2930;

int sub_1032348b(void)
{
    unsigned int v11;  // ecx
    int v12;  // eax
    unsigned int v13;  // 4196
    unsigned int v14;  // id
    unsigned int v15;  // ac
    unsigned int v16;  // edx
    unsigned int v17;  // ebx
    unsigned int v18;  // esi
    unsigned int v19;  // edi
    unsigned int v20;  // 4110
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    unsigned int v6;  // [bp-0x4]
    unsigned int v7;  // [bp+0x0]
    unsigned int v8;  // [bp+0x0]
    unsigned int v9;  // [bp+0x4]

    v7 = v11;
    v6 = sub_10350ec0(g_103a2930 + 4, v12);
    v13 = _ccall(3, &v9, 12, 0);
    v8 = v13 | 0x202 | v14 * 0x200000 & 0x200000 | v15 * 0x40000 & 0x40000;
    v5 = v7;
    v4 = v16;
    v3 = v17;
    v2 = /* unsupported instruction */;
    v1 = v18;
    v0 = v19;
    if (!(1))
        goto LABEL_103234c5;
LABEL_103234c5:
    for (; (v20 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v20 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
}
```

## `sub_103234c0` `0x103234c0`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103234c0(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103234c7` `0x103234c7`

_3 bytes. (leaf/helper — see body)_

```c
void sub_103234c7(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103234f5` `0x103234f5`

_122 bytes. (leaf/helper — see body)_

```c
extern char g_1038c8b4;
extern int g_103a292c;

int sub_103234f5(void)
{
    unsigned int v16;  // eax
    unsigned int v17;  // ecx
    unsigned int v26;  // 4101
    unsigned int v27;  // 4101
    unsigned int v28;  // 4101
    unsigned int v29;  // 4101
    unsigned int v30;  // ebp
    unsigned int v32;  // 4101
    int v33;  // edx
    unsigned int v34;  // 4110
    unsigned int v35;  // id
    unsigned int v18;  // edx
    unsigned int v36;  // ac
    unsigned int v38;  // 4104
    int v39;  // cc_dep1
    unsigned int v41;  // 4101
    unsigned int v19;  // ebx
    unsigned int v20;  // esi
    unsigned int v21;  // edi
    unsigned int v22;  // 4101
    unsigned int v23;  // 4103
    unsigned int v24;  // 4101
    unsigned int v25;  // 4101
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x1c]
    unsigned int v4;  // [bp-0x1c]
    char *v5;  // [bp-0x18], Other Possible Types: unsigned int
    unsigned int v6;  // [bp-0x14]
    int v7;  // [bp-0x10]
    unsigned int v8;  // [bp-0x10]
    unsigned int v9;  // [bp-0xc]
    unsigned int v10;  // [bp-0x8]
    unsigned int v11;  // [bp-0x4]
    unsigned int v12;  // [bp-0x4]
    char v15;  // [bp+0x100014]

    v11 = v16;
    v10 = v17;
    v9 = v18;
    v8 = v19;
    v5 = /* unsupported instruction */;
    v4 = v20;
    v2 = v21;
LABEL_10323511:
    v22 = _ccall(0, 15, 0, 0, 0);
    if ((char)v22)
        goto LABEL_10323513;
    else
        goto LABEL_10323514;
    while (true)
    {
LABEL_10323513:
        __unsupported_jumpkind_Ijk_NoDecode()
        while (true)
        {
LABEL_10323514:
            v23 = _ccall(10, 15, 0, 0, 0);
            if ((char)v23)
            {
                v24 = _ccall(8, 15, 0, 0, 0);
                if (!((char)v24))
                {
                    if (!(1))
                        goto LABEL_10323519;
                    v25 = _ccall(10, 15, 0, 0, 0);
                    if (!((char)v25))
                    {
                        v26 = _ccall(0, 15, 0, 0, 0);
                        if ((char)v26)
                            break;
                        else
                            continue;
                    }
                    v27 = _ccall(8, 15, 0, 0, 0);
                    if ((char)v27)
                        goto LABEL_10323511;
                    goto LABEL_1032351a;
                }
                __unsupported_jumpkind_Ijk_NoDecode()
                v28 = _ccall(8, 15, 0, 0, 0);
                if (!((char)v28))
                    goto LABEL_1032351a;
LABEL_10323511:
                if ((v29 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v29))
                    break;
            }
            else
            {
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_10323519:
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_1032351a:
                v30 = v5;
                v32 = _ccall(0, 15, (unsigned int)v15, 0, 0);
                v33 = g_103a292c;
                if (g_103a292c > *((int *)&g_1038c8b4))
                {
                    if (g_103a292c >= *((int *)&g_1038c8b4))
                        goto LABEL_1032354c;
LABEL_1032354c:
                    v34 = _ccall(6, g_103a292c, *((int *)&g_1038c8b4), 0);
                    v12 = v34 | 0x202 | v35 * 0x200000 & 0x200000 | v36 * 0x40000 & 0x40000;
                    v10 = v11;
                    v9 = 0;
                    v7 = g_103a292c;
                    v6 = v8;
                    v5 = &v12;
                    v3 = v30;
                    v1 = v4;
                    v0 = v2;
                    v38 = _ccall(0, 6, g_103a292c, g_103a292c, 0);
                    v39 = g_103a292c;
                    if (!((char)v38))
                    {
                        if (!(1))
                            goto LABEL_10323559;
LABEL_10323559:
                        if (0)
                            goto LABEL_0x103234f1;
                        v41 = _ccall(2, 15, 3, 0, 0);
                        if ((char)v41)
                            goto LABEL_0x1032356a;
                    }
                    else
                    {
                        v41 = _ccall(2, 6, v39, v33, 0);
                        if ((char)v41)
                            goto LABEL_0x1032356a;
                    }
                }
            }
        }
    }
}
```

## `sub_10323507` `0x10323507`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323507(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032352d` `0x1032352d`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1032352d(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323563` `0x10323563`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323563(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323577` `0x10323577`

_110 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a292c;

int sub_10323577(void)
{
    unsigned int v5;  // 4097
    unsigned int v6;  // eax
    unsigned int v7;  // 4272
    unsigned int v8;  // 4110
    char *v1;  // [bp+0xc]
    unsigned int v2;  // [bp+0x18]
    unsigned int v3;  // [bp+0x1c]
    unsigned int v4;  // [bp+0x20]

    v5 = v4;
    v6 = g_103a292c;
    g_103a292c = v6 - 1;
    v4 = ~(~(v2));
    v3 = g_103a292c;
    v7 = _ccall(6, v6, 1, 0);
    v4 = v7 | 0x202 | ((char)(v5 >> 10) ? 4294967295 : 1) & 0x400 | ((char)(v5 >> 21) ? 1 : 0) * 0x200000 & 0x200000 | ((char)(v5 >> 18) ? 1 : 0) * 0x40000 & 0x40000;
    v2 = v4;
    v1 = &v4;
    if (!(1))
        goto LABEL_103235bc;
LABEL_103235bc:
    for (; (v8 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v8 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
    v4 = 1;
}
```

## `sub_1032357b` `0x1032357b`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032357b(void)
{
}
```

## `sub_1032357d` `0x1032357d`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1032357d(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103235b7` `0x103235b7`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103235b7(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103235be` `0x103235be`

_3 bytes. (leaf/helper — see body)_

```c
void sub_103235be(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103235ec` `0x103235ec`

_170 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a292c;
extern unsigned int g_103a2930;

int sub_103235ec(void)
{
    if ((*((int *)(g_103a2930 + g_103a292c * 4)) & 2147483655) >= 0)
        sub_1032369a(); /* do not return */
}
```

## `sub_10323661` `0x10323661`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10323661(unsigned int a0, unsigned int a1)
{
}
```

## `sub_1032369a` `0x1032369a`

_68 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a292c;
extern unsigned int g_103a2930;

void sub_1032369a(void)
{
    int v12;  // eax
    unsigned int v13;  // 4110
    unsigned int v22;  // 4104
    unsigned int v23;  // cc_dep1
    unsigned int v24;  // cc_dep2
    unsigned int v26;  // 4101
    unsigned int v14;  // id
    unsigned int v15;  // ac
    unsigned int v16;  // ecx
    unsigned int v17;  // edx
    unsigned int v18;  // ebx
    unsigned int v19;  // esi
    unsigned int v20;  // edi
    unsigned int v21;  // cc_op
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    unsigned int v6;  // [bp-0x4]
    unsigned int v7;  // [bp+0x0]
    unsigned int v8;  // [bp+0x0]
    char v10;  // [bp+0x10]

    v5 = *((int *)(g_103a2930 + g_103a292c * 4));
    v7 = sub_10323730(*((int *)(g_103a2930 + g_103a292c * 4)), v12);
    if (&v10 >= NULL)
        goto LABEL_103236bb;
LABEL_103236bb:
    v13 = _ccall(3, &v5, 12, 0);
    v8 = v13 | 0x202 | v14 * 0x200000 & 0x200000 | v15 * 0x40000 & 0x40000;
    v6 = v7;
    v5 = v16;
    v4 = v17;
    v3 = v18;
    v2 = /* unsupported instruction */;
    v1 = v19;
    v0 = v20;
    v21 = 6;
    v22 = _ccall(0, 6, v17, v17, 0);
    v23 = v17;
    if (!((char)v22))
    {
        if (!(1))
            goto LABEL_103236c8;
LABEL_103236c8:
        v21 = 15;
        v23 = 3;
        v24 = 0;
        if (0)
            goto LABEL_0x10323660;
        else
            goto LABEL_103236d0;
    }
LABEL_103236d0:
    v26 = _ccall(2, v21, v23, v24, 0);
    if ((char)v26)
        goto LABEL_0x103236d9;
}
```

## `sub_103236d2` `0x103236d2`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103236d2(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103236ea` `0x103236ea`

_2 bytes. (leaf/helper — see body)_

```c
void sub_103236ea(void)
{
}
```

## `sub_10323704` `0x10323704`

_2 bytes. (leaf/helper — see body)_

```c
int sub_10323704(void)
{
}
```

