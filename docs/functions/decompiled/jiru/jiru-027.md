# elfbot.dll decompiled — jiru 0x10321672..0x103225a3

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10321672` `0x10321672`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10321672(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10321679` `0x10321679`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10321679(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103216a7` `0x103216a7`

_31 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038c8ac;

void sub_103216a7(void)
{
    unsigned int v5;  // cc_op
    unsigned int v6;  // cc_dep1
    unsigned int v7;  // cc_dep2
    unsigned int v8;  // cc_ndep
    unsigned int v9;  // 4111
    char v0;  // [bp-0xcb8b3c]
    unsigned int v1;  // [bp-0x8]
    unsigned int v2;  // [bp-0x4]
    unsigned int v4;  // [bp+0xffb94]

    v2 = v4;
    v1 = g_1038c8ac->field_0;
    v9 = _ccall(v5, v6, v7, v8);
    v0 = v0 + 56 + ((char)v9 & 1);
    __unsupported_jumpkind_Ijk_Privileged()
}
```

## `sub_103216d0` `0x103216d0`

_62 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a2914;
extern unsigned int g_103a2928;

int sub_103216d0(void)
{
    unsigned int v10;  // edx
    unsigned int v11;  // cc_dep2
    unsigned int v20;  // edi
    unsigned int v21;  // cc_op
    unsigned int v22;  // 4104
    unsigned int v23;  // cc_dep1
    unsigned int v25;  // 4101
    unsigned int v12;  // edx
    unsigned int v13;  // eax
    unsigned int v14;  // 4110
    unsigned int v15;  // id
    unsigned int v16;  // ac
    unsigned int v17;  // ecx
    unsigned int v18;  // ebx
    unsigned int v19;  // esi
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    char *v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    unsigned int v7;  // [bp-0x4]
    unsigned int v8;  // [bp-0x4]

    v10 = g_103a2928 * 0x1000;
    v11 = g_103a2914;
    v12 = v10 + g_103a2914;
    g_103a2914 = v12;
    v7 = v13;
    if (v10 + v11 >= 0)
        goto LABEL_103216ed;
LABEL_103216ed:
    v14 = _ccall(3, v10, v11, 0);
    v8 = v14 | 0x202 | v15 * 0x200000 & 0x200000 | v16 * 0x40000 & 0x40000;
    v6 = v7;
    v5 = v17;
    v4 = v12;
    v3 = v18;
    v2 = &v8;
    v1 = v19;
    v0 = v20;
    v21 = 6;
    v22 = _ccall(0, 6, v12, v12, 0);
    v23 = v12;
    if (!((char)v22))
    {
        if (!(1))
            goto LABEL_103216fa;
LABEL_103216fa:
        v21 = 15;
        v23 = 3;
        v12 = 0;
        if (0)
            goto LABEL_0x10321692;
        else
            goto LABEL_10321702;
    }
LABEL_10321702:
    v25 = _ccall(2, v21, v23, v12, 0);
    if ((char)v25)
        goto LABEL_0x1032170b;
    else
        goto LABEL_0x10321705;
}
```

## `sub_10321704` `0x10321704`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10321704(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10321718` `0x10321718`

_14 bytes. (leaf/helper — see body)_

```c
int sub_10321718(void)
{
}
```

## `sub_1032171c` `0x1032171c`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032171c(void)
{
}
```

## `sub_1032171e` `0x1032171e`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1032171e(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10321754` `0x10321754`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10321754(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103217f1` `0x103217f1`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103217f1(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103217f8` `0x103217f8`

_3 bytes. (leaf/helper — see body)_

```c
void sub_103217f8(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032188f` `0x1032188f`

_19 bytes. (leaf/helper — see body)_

```c
int sub_1032188f(void)
{
    int v2;  // edx
    int v1;  // [bp+0xffb88]

    sub_10322f60(v1 - 1, v2);
}
```

## `sub_103218c1` `0x103218c1`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103218c1(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103218d5` `0x103218d5`

_174 bytes. (leaf/helper — see body)_

```c
extern char g_103a2928;

int sub_103218d5(void)
{
    void* v10;  // ebp
    unsigned int v11;  // eax
    unsigned int v20;  // 4101
    unsigned int v12;  // ecx
    unsigned int v13;  // 4101
    unsigned int v14;  // 4103
    unsigned int v15;  // 4101
    unsigned int v16;  // 4101
    unsigned int v17;  // 4101
    unsigned int v18;  // 4101
    unsigned int v19;  // 4101
    unsigned int v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x4]
    void* v2;  // [bp+0x8], Other Possible Types: unsigned int
    void* v3;  // [bp+0xc]
    char *v4;  // [bp+0x10], Other Possible Types: unsigned int
    unsigned int v5;  // [bp+0x14]
    unsigned int v6;  // [bp+0x18]
    unsigned int v7;  // [bp+0x1c]
    unsigned int v8;  // [bp+0x20]
    char v9;  // [bp+0x24]

    v10 = v2;
    v11 = v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff;
    v12 = (int)v10[1148] + 1;
    if (v12 < *((int *)&g_103a2928))
    {
        sub_10321960(1);
        return;
    }
    v8 = v11 * 0x1000000 | v11 * 0x100 & 0xff0000 | v11 >> 8 & 0xff00 | v11 >> 24 & 0xff;
    v7 = v12;
    v6 = v5;
    v5 = v4;
    v4 = &v9;
    v3 = v10;
    v2 = v1;
    v1 = v0;
LABEL_1032198f:
    v13 = _ccall(0, 15, 0, 0, 0);
    if ((char)v13)
        goto LABEL_10321991;
    else
        goto LABEL_10321992;
    while (true)
    {
LABEL_10321991:
        __unsupported_jumpkind_Ijk_NoDecode()
        while (true)
        {
LABEL_10321992:
            v14 = _ccall(10, 15, 0, 0, 0);
            if (!((char)v14))
                __unsupported_jumpkind_Ijk_NoDecode()
            v15 = _ccall(8, 15, 0, 0, 0);
            if (!((char)v15))
            {
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
                        goto LABEL_1032198f;
                    else
                        goto LABEL_0x10321998;
                }
            }
            else
            {
                __unsupported_jumpkind_Ijk_NoDecode()
                v19 = _ccall(8, 15, 0, 0, 0);
                if ((char)v19)
                    goto LABEL_1032198f;
                else
                    goto LABEL_0x10321998;
            }
LABEL_1032198f:
            if ((v20 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v20))
                break;
        }
    }
}
```

## `sub_103218d9` `0x103218d9`

_2 bytes. (leaf/helper — see body)_

```c
void sub_103218d9(void)
{
}
```

## `sub_103218db` `0x103218db`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103218db(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10321960` `0x10321960`

_19 bytes. (leaf/helper — see body)_

```c
int sub_10321960(void)
{
    int v2;  // edx
    int v1;  // [bp+0xffb88]

    sub_10322f60(v1 + 1, v2);
}
```

## `sub_10321985` `0x10321985`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10321985(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032199e` `0x1032199e`

_252 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
} struct_0;

typedef struct struct_1 {
    char padding_0[92];
    unsigned int field_5c;
} struct_1;

extern char g_10390234;
extern char g_10390236;
extern unsigned int g_103a2910;

int sub_1032199e(void)
{
    unsigned int *v14;  // eax
    unsigned int v15;  // 4096
    char *v24;  // 4098
    char *v25;  // edi
    unsigned int v26;  // edx
    unsigned int v27;  // eax
    unsigned int v28;  // edi
    unsigned int v29;  // esi
    unsigned int v30;  // eax
    unsigned int v31;  // edx
    unsigned int v32;  // ecx
    unsigned int v33;  // 4101
    unsigned int v16;  // cc_op
    unsigned int v34;  // 4103
    unsigned int v35;  // 4101
    unsigned int v36;  // 4101
    unsigned int v37;  // 4101
    unsigned int v38;  // 4101
    unsigned int v39;  // 4101
    unsigned int v40;  // 4101
    unsigned int v17;  // cc_dep1
    unsigned int v18;  // cc_dep2
    unsigned int v19;  // cc_ndep
    unsigned int v20;  // 4103
    unsigned int v21;  // 4109
    char v22;  // cl
    struct_0 **v23;  // edx
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    char *v3;  // [bp-0x14]
    struct_0 **v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    unsigned int v7;  // [bp-0x4]
    char v8;  // [bp+0x0]
    int v10;  // [bp+0xffb88]
    unsigned int v11;  // [bp+0xffb90]
    struct_1 *v12;  // [bp+0xffe8c]

    v15 = *(v14);
    *(v14) = *(v14) + 1;
    v20 = _ccall(v16, v17, v18, v19);
    v21 = _ccall(12, 18, v15 + 1, 0, v20);
    if (!((char)v21))
    {
        v22 = v10;
        v24 = &*(v23)->field_0;
        *(v23) = *(v23) - v25;
        *(v25) = *(v25) + v22 + (v24 < v25);
        *(v14) = *(v14) + (char *)v14;
        v7 = 0;
        v26 = v10 & 2147483655;
        if ((v10 & 2147483655) < 0)
            v26 = (v26 - 1 | 0xfffffff8) + 1;
        v27 = v10 & 2147483655;
        if ((v10 & 2147483655) < 0)
            v27 = (v27 - 1 | 0xfffffff8) + 1;
        v28 = (*((int *)(272156632 + 4 * (&g_10390234)[v26])) ^ *((int *)(272156632 + 4 * (&g_10390236)[v27]))) >> ((char)(v10 % 28) & 31) & 15;
        v29 = v10 * 16 + v28;
        v30 = sub_10322f60(v10, g_103a2910 + v29 * 4);
        v31 = (char)v30;
        if (v31)
        {
            v7 = v30;
            v6 = v32;
            v5 = v31;
            v4 = v23;
            v3 = &v8;
            v2 = /* unsupported instruction */;
            v1 = v29;
            v0 = v28;
LABEL_10321a78:
            v33 = _ccall(0, 15, 0, 0, 0);
            if ((char)v33)
                goto LABEL_10321a7a;
            else
                goto LABEL_10321a7b;
            while (true)
            {
LABEL_10321a7a:
                __unsupported_jumpkind_Ijk_NoDecode()
                while (true)
                {
LABEL_10321a7b:
                    v34 = _ccall(10, 15, 0, 0, 0);
                    if (!((char)v34))
                        __unsupported_jumpkind_Ijk_NoDecode()
                    v35 = _ccall(8, 15, 0, 0, 0);
                    if (!((char)v35))
                    {
                        v36 = _ccall(10, 15, 0, 0, 0);
                        if (!((char)v36))
                        {
                            v37 = _ccall(0, 15, 0, 0, 0);
                            if ((char)v37)
                                break;
                            else
                                continue;
                        }
                        else
                        {
                            v38 = _ccall(8, 15, 0, 0, 0);
                            if ((char)v38)
                                goto LABEL_10321a78;
                            else
                                goto LABEL_0x10321a81;
                        }
                    }
                    else
                    {
                        __unsupported_jumpkind_Ijk_NoDecode()
                        v39 = _ccall(8, 15, 0, 0, 0);
                        if ((char)v39)
                            goto LABEL_10321a78;
                        else
                            goto LABEL_0x10321a81;
                    }
LABEL_10321a78:
                    if ((v40 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v40))
                        break;
                }
            }
        }
    }
    if (!v12->field_5c)
        v11 = 1;
}
```

## `sub_10321a6e` `0x10321a6e`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10321a6e(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10321a91` `0x10321a91`

_38 bytes. (leaf/helper — see body)_

```c
void sub_10321a91(unsigned int a0, unsigned int a1)
{
    unsigned int v23;  // cc_op
    unsigned int v24;  // cc_dep1
    unsigned int v25;  // cc_dep2
    unsigned int v26;  // cc_ndep

    if (!(1))
        goto LABEL_10321aa1;
LABEL_10321aa1:
    v23 = 15;
    v24 = 3;
    v25 = 0;
    v26 = 0;
}
```

## `sub_10321aab` `0x10321aab`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10321aab(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10321abf` `0x10321abf`

_16 bytes. (leaf/helper — see body)_

```c
int sub_10321abf(void)
{
}
```

## `sub_10321ac3` `0x10321ac3`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10321ac3(void)
{
}
```

## `sub_10321ac5` `0x10321ac5`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10321ac5(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10321b1f` `0x10321b1f`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10321b1f(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10321e64` `0x10321e64`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10321e64(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10321e6b` `0x10321e6b`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10321e6b(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10321e99` `0x10321e99`

_172 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
} struct_0;

extern struct_0 *g_103a2924;
extern unsigned int g_103a2940;

int sub_10321e99(void)
{
    char *v12;  // eax
    struct_0 *v13;  // edx
    unsigned int v22;  // 4110
    unsigned int v15;  // 4157
    unsigned int v16;  // id
    unsigned int v17;  // ac
    unsigned int v18;  // edx
    unsigned int v19;  // ebx
    unsigned int v20;  // esi
    unsigned int v21;  // edi
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    char *v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    struct_0 *v5;  // [bp-0xc]
    char *v6;  // [bp-0x8]
    struct_0 *v7;  // [bp-0x4], Other Possible Types: unsigned int
    unsigned int v10;  // [bp+0xfefc0]
    unsigned int v11;  // [bp+0xff70c]

    *(v12) = *(v12) + *((char *)&v12);
    if (g_103a2924->field_c)
    {
        __unsupported_jumpkind_Ijk_NoDecode()
        v7 = v13->field_c;
        v10 = sub_1034fef0(v13->field_c);
        g_103a2940 = v10;
        v11 = 0;
        sub_10321ef3(/* unsupported instruction */ - 2296); /* do not return */
    }
    v7 = g_103a2924;
    v6 = v12;
    v15 = _ccall(6, g_103a2924->field_c, 0, 0);
    v7 = v15 | 0x202 | v16 * 0x200000 & 0x200000 | v17 * 0x40000 & 0x40000;
    v5 = g_103a2924;
    v4 = v18;
    v3 = v19;
    v2 = &v7;
    v1 = v20;
    v0 = v21;
    if (!(1))
        goto LABEL_1032231c;
LABEL_1032231c:
    for (; (v22 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v22 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
}
```

## `sub_10321ed5` `0x10321ed5`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10321ed5(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10321ef3` `0x10321ef3`

_184 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

typedef struct struct_1 {
    char padding_0[8];
    unsigned int field_8;
} struct_1;

extern struct_0 *g_1038b0c0;
extern struct_0 *g_1038c8ac;
extern struct_1 *g_103a2924;
extern unsigned int g_103a2940;

void sub_10321ef3(void)
{
    unsigned int v9;  // ecx
    unsigned int v10;  // edx
    unsigned int v19;  // 4101
    unsigned int v20;  // 4101
    unsigned int v21;  // 4101
    unsigned int v11;  // ebx
    unsigned int v12;  // esi
    unsigned int v13;  // edi
    unsigned int v14;  // 4101
    unsigned int v15;  // 4103
    unsigned int v16;  // 4101
    unsigned int v17;  // 4101
    unsigned int v18;  // 4101
    unsigned int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x2c]
    char *v2;  // [bp-0x24]
    unsigned int v3;  // [bp-0x20]
    unsigned int v4;  // [bp-0x1c]
    unsigned int v5;  // [bp-0x18]
    unsigned int v6;  // [bp-0x14]
    unsigned int v7;  // [bp-0x10]

    v7 = g_1038c8ac->field_0;
    v6 = g_1038b0c0(g_1038c8ac->field_0, g_103a2924->field_8, g_103a2940, v9);
    v5 = v9;
    v4 = v10;
    v3 = v11;
    v2 = &v7;
    v1 = v12;
    v0 = v13;
LABEL_10321f2f:
    v14 = _ccall(0, 15, 0, 0, 0);
    if ((char)v14)
        goto LABEL_10321f31;
    else
        goto LABEL_10321f32;
    while (true)
    {
LABEL_10321f31:
        __unsupported_jumpkind_Ijk_NoDecode()
        while (true)
        {
LABEL_10321f32:
            v15 = _ccall(10, 15, 0, 0, 0);
            if (!((char)v15))
            {
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_10321f37:
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_10321f38:
                964084309();
            }
            v16 = _ccall(8, 15, 0, 0, 0);
            if (!((char)v16))
            {
                if (!(1))
                    goto LABEL_10321f37;
                v17 = _ccall(10, 15, 0, 0, 0);
                if (!((char)v17))
                {
                    v18 = _ccall(0, 15, 0, 0, 0);
                    if ((char)v18)
                        break;
                    else
                        continue;
                }
                v19 = _ccall(8, 15, 0, 0, 0);
                if ((char)v19)
                    goto LABEL_10321f2f;
                goto LABEL_10321f38;
            }
            __unsupported_jumpkind_Ijk_NoDecode()
            v20 = _ccall(8, 15, 0, 0, 0);
            if (!((char)v20))
                goto LABEL_10321f38;
LABEL_10321f2f:
            if ((v21 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v21))
                break;
        }
    }
}
```

## `sub_10321f25` `0x10321f25`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10321f25(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10321fac` `0x10321fac`

_22 bytes. (leaf/helper — see body)_

```c
void sub_10321fac(void)
{
    unsigned int v0;  // [bp-0x904]
    unsigned int v1;  // [bp-0x8fc]

    v1 = 0;
    v0 = 0;
}
```

## `sub_10321ff0` `0x10321ff0`

_309 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[664833300];
    unsigned int field_27a08d14;
} struct_0;

extern unsigned int g_103a26c0;
extern unsigned int g_103a2730;
extern unsigned int g_103a2820[4];
extern unsigned int g_103a2890;

void sub_10321ff0(unsigned int a0, void* a1, unsigned int a2, void* a3)
{
    unsigned int v9;  // cc_op
    unsigned int v10;  // cc_dep1
    unsigned int v19;  // 4101
    unsigned int v20;  // 4101
    unsigned int v21;  // 4101
    unsigned int v22;  // 4101
    unsigned int v23;  // 4103
    unsigned int v24;  // 4101
    unsigned int v25;  // 4101
    unsigned int v26;  // 4101
    unsigned int v27;  // 4101
    void* v28;  // ebx
    unsigned int v11;  // cc_dep2
    struct_0 *idx;  // ecx
    unsigned int index;  // eax
    unsigned int v31;  // ecx
    unsigned int v32;  // 4110
    unsigned int v33;  // id
    unsigned int v34;  // ac
    unsigned int v35;  // edx
    unsigned int v36;  // cc_op
    unsigned int v37;  // 4104
    unsigned int v38;  // cc_dep1
    unsigned int v12;  // cc_ndep
    unsigned int v39;  // cc_dep2
    unsigned int v43;  // 4101
    unsigned int v13;  // 4101
    unsigned int v14;  // 4101
    unsigned int v15;  // cc_op
    unsigned int v16;  // cc_dep1
    unsigned int v17;  // cc_dep2
    unsigned int v18;  // cc_ndep
    unsigned int v0;  // [bp-0x4]
    unsigned int v1;  // [bp+0x0]
    unsigned int v2;  // [bp+0x0]
    char *v3;  // [bp+0x8]
    unsigned int v4;  // [bp+0x14]
    unsigned int v5;  // [bp+0x18]
    unsigned int v6;  // [bp+0x1c]
    unsigned int v7;  // [bp+0x1c]
    char v8;  // [bp+0x24]

    __unsupported_jumpkind_Ijk_NoDecode()
    v13 = _ccall(2, v9, v10, v11, v12);
    if (!((char)v13))
    {
        v14 = _ccall(8, v9, v10, v11, v12);
        if ((char)v14)
            goto LABEL_10321ff5;
LABEL_10321fe6:
        v15 = 15;
        v16 = 0;
        v17 = 0;
        v18 = 0;
        if (!(1))
            goto LABEL_10322002;
        while (true)
        {
            v19 = _ccall(10, 15, 0, 0, 0);
            if (!((char)v19))
            {
LABEL_10321fec:
                v20 = _ccall(0, 15, 0, 0, 0);
                if (!((char)v20))
                    goto LABEL_10321ffd;
            }
            else
            {
                v21 = _ccall(8, 15, 0, 0, 0);
                if (!((char)v21))
                    break;
LABEL_10321fec:
                v22 = _ccall(0, v15, v16, v17, v18);
                if (!((char)v22))
                    goto LABEL_10321ffd;
            }
LABEL_10321ffc:
            __unsupported_jumpkind_Ijk_NoDecode()
LABEL_10321ffd:
            v23 = _ccall(10, v15, v16, v17, v18);
            if (!((char)v23) || !((v24 = (unsigned int)_ccall(2, v15, v16, v17, v18), !((char)v24))))
                goto LABEL_10322001;
            v25 = _ccall(8, v15, v16, v17, v18);
            if (!((char)v25))
                goto LABEL_10321fe6;
LABEL_10321ff5:
            __unsupported_jumpkind_Ijk_NoDecode()
            v26 = _ccall(8, v15, v16, v17, v18);
            if (!((char)v26))
                break;
            v27 = _ccall(4, v15, v16, v17, v18);
            if ((char)v27)
                goto LABEL_10321fec;
            else
                goto LABEL_10321ffc;
        }
    }
    else
    {
LABEL_10322001:
        __unsupported_jumpkind_Ijk_NoDecode()
LABEL_10322002:
        __unsupported_jumpkind_Ijk_NoDecode()
    }
    v28 = a3;
    *((unsigned int *)&a1[4168]) = sub_1034fef0(-((g_103a2820[a1[2308]] >= 0x20000000 ? 1 : 0) & 1) | g_103a2820[a1[2308]] * 4);
    (&g_103a26c0)[a1[2308]] = (int)a1[4168];
    *((unsigned int *)&a1[4172]) = sub_1034fef0(-((g_103a2820[a1[2308]] >= 0x20000000 ? 1 : 0) & 1) | g_103a2820[a1[2308]] * 4);
    (&g_103a2730)[a1[2308]] = (int)a1[4172];
    sub_1034fef0(g_103a2820[a1[2308]]);
    do
    {
        *((unsigned int *)&v28[590707]) = (int)v28[590707] - 1;
        *((unsigned int *)&v28[1068907]) = (int)v28[1068907] - 1;
        idx->field_27a08d14 = idx->field_27a08d14 - 1;
        *((unsigned int *)&a1[4180]) = sub_1034fef0(-((g_103a2820[a1[2308]] >= 0x20000000 ? 1 : 0) & 1) | g_103a2820[a1[2308]] * 4);
        index = (int)a1[2308];
        v31 = (int)a1[4180];
        (&g_103a2890)[index] = v31;
        v6 = index;
        if (&v8 >= NULL)
            goto LABEL_103220f8;
LABEL_103220f8:
        v32 = _ccall(3, &v6, 4, 0);
        v7 = v32 | 0x202 | v33 * 0x200000 & 0x200000 | v34 * 0x40000 & 0x40000;
        v5 = v6;
        v4 = v31;
        a3 = v35;
        a2 = v28;
        v3 = &v7;
        a0 = a1;
        v1 = a0;
        v0 = v2;
        v36 = 6;
        v37 = _ccall(0, 6, v35, v35, 0);
        v38 = v35;
        v39 = v35;
        if ((char)v37)
            break;
        if (!(1))
            goto LABEL_10322105;
LABEL_10322105:
        v28 = NULL;
        v36 = 15;
        v38 = 3;
        v39 = 0;
    } while (false);
    v43 = _ccall(2, v36, v38, v39, 0);
    if ((char)v43)
        goto LABEL_0x10322116;
}
```

## `sub_1032210f` `0x1032210f`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1032210f(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10322123` `0x10322123`

_436 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    unsigned int field_0;
    char field_1;
    char padding_2[2];
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
} struct_0;

extern unsigned int g_1038c7e4;
extern unsigned int g_1038c85c;
extern unsigned int g_103a26c0[4];
extern struct_0 g_103a2730;
extern void g_103a27a0;
extern struct_1 g_103a2820;
extern unsigned int g_103a2890[4];

int sub_10322123(void)
{
    void* v10;  // ebp
    unsigned int v11;  // esi
    unsigned int v20;  // edx
    unsigned int v12;  // 4097
    unsigned int v13;  // eax
    unsigned int v14;  // eax
    struct_1 *v15;  // edx
    unsigned int v16;  // 4163
    unsigned int v17;  // 4110
    void* v18;  // ebp
    unsigned int v19;  // eax
    unsigned int v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x4]
    void* v2;  // [bp+0x8], Other Possible Types: unsigned int
    char *v3;  // [bp+0xc], Other Possible Types: void*
    char *v4;  // [bp+0x10], Other Possible Types: unsigned int
    struct_1 *v5;  // [bp+0x14], Other Possible Types: unsigned int
    unsigned int v6;  // [bp+0x18]
    unsigned int v7;  // [bp+0x1c]
    unsigned int v8;  // [bp+0x20]
    char v9;  // [bp+0x24]

    v10 = v2;
    v11 = v1;
    v12 = v8;
    v13 = v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff;
    v14 = v13 * 0x1000000 | v13 * 0x100 & 0xff0000 | v13 >> 8 & 0xff00 | v13 >> 24 & 0xff;
    *((struct_1 **)&v10[2312]) = NULL;
    while (true)
    {
        v15 = (int)v10[2312];
        if (v15 >= (&g_103a2820.field_0)[v10[2308]])
            break;
        *((unsigned int *)(g_103a26c0[v10[2308]] + (int)v10[2312] * 4)) = *((int *)(int)v10[2292]) + (int)v10[8] ^ g_1038c7e4 ^ g_1038c85c;
        *((unsigned int *)&v10[2292]) = (int)v10[2292] + 4;
        *((int *)((&g_103a2730.field_0)[v10[2308]] + (int)v10[2312] * 4)) = *((int *)(int)v10[2292]);
        *((unsigned int *)&v10[2292]) = (int)v10[2292] + 4;
        *((char *)(*((int *)&(&g_103a27a0)[4 * v10[2308]]) + (int)v10[2312])) = *((char *)(int)v10[2292]);
        *((unsigned int *)&v10[2292]) = (int)v10[2292] + 1;
        v11 = 23;
        *((unsigned int *)(g_103a2890[v10[2308]] + (int)v10[2312] * 4)) = g_1038c7e4 ^ g_1038c85c ^ *((int *)(int)v10[2292]) ^ *((int *)(-2288 + (char *)v10 + 4 * (int)v10[2312] % 23));
        *((unsigned int *)&v10[2292]) = (int)v10[2292] + 4;
        *((unsigned int *)&v10[2312]) = (int)v10[2312] + 1;
        v14 = (int)v10[2300] + 1;
        *((unsigned int *)&v10[2300]) = v14;
    }
    v8 = (int)v10[2308];
    v7 = v14;
    v16 = _ccall(6, v15, (&g_103a2820.field_0)[v8], 0);
    v8 = v16 | 0x202 | ((char)(v12 >> 10) ? 4294967295 : 1) & 0x400 | ((char)(v12 >> 21) ? 1 : 0) * 0x200000 & 0x200000 | ((char)(v12 >> 18) ? 1 : 0) * 0x40000 & 0x40000;
    v6 = v8;
    v5 = v15;
    v3 = &v8;
    v2 = v10;
    v1 = v11;
    if (!(1))
        goto LABEL_1032228a;
LABEL_1032228a:
    for (; (v17 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v17 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
    v18 = v2;
    v19 = _INSERT(*((unsigned short *)&v5) CONCAT 0, 0, v7);
    v20 = (int)v18[2308] + 1;
    *((unsigned int *)&v18[2308]) = v20;
    if ((int)v18[2308] >= 28)
    {
        sub_103222ba();
        return;
    }
    v8 = v19;
    v7 = v6;
    v6 = v20;
    v5 = v4;
    v4 = &v9;
    v3 = v18;
    v2 = v1;
    v1 = v0;
}
```

## `sub_10322127` `0x10322127`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10322127(void)
{
}
```

## `sub_10322129` `0x10322129`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10322129(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10322285` `0x10322285`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10322285(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032228c` `0x1032228c`

_3 bytes. (leaf/helper — see body)_

```c
void sub_1032228c(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103222ba` `0x103222ba`

_58 bytes. (leaf/helper — see body)_

```c
int sub_103222ba(void)
{
    int v10;  // edx
    unsigned int v11;  // ecx
    unsigned int v20;  // 4101
    unsigned int v21;  // 4101
    unsigned int v22;  // 4101
    unsigned int v12;  // ebx
    unsigned int v13;  // esi
    unsigned int v14;  // edi
    unsigned int v15;  // 4101
    unsigned int v16;  // 4103
    unsigned int v17;  // 4101
    unsigned int v18;  // 4101
    unsigned int v19;  // 4101
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    unsigned int v6;  // [bp-0x4]
    int v8;  // [bp+0xfefac]

    v8 = v10;
    v6 = sub_10350eb5(v8);
    v5 = v11;
    v4 = v10;
    v3 = v12;
    v2 = /* unsupported instruction */;
    v1 = v13;
    v0 = v14;
    v15 = _ccall(0, 15, 0, 0, 0);
    if ((char)v15)
        goto LABEL_103222ed;
    else
        goto LABEL_103222ee;
    while (true)
    {
LABEL_103222ed:
        __unsupported_jumpkind_Ijk_NoDecode()
        while (true)
        {
LABEL_103222ee:
            v16 = _ccall(10, 15, 0, 0, 0);
            if (!((char)v16))
            {
                __unsupported_jumpkind_Ijk_NoDecode()
                __unsupported_jumpkind_Ijk_NoDecode()
            }
            v17 = _ccall(8, 15, 0, 0, 0);
            if (!((char)v17))
            {
                if (false)
                    __unsupported_jumpkind_Ijk_NoDecode()
                v18 = _ccall(10, 15, 0, 0, 0);
                if (!((char)v18))
                {
                    v19 = _ccall(0, 15, 0, 0, 0);
                    if ((char)v19)
                        break;
                    else
                        continue;
                }
                else
                {
                    v20 = _ccall(8, 15, 0, 0, 0);
                }
            }
            else
            {
                __unsupported_jumpkind_Ijk_NoDecode()
                v21 = _ccall(8, 15, 0, 0, 0);
            }
            if ((v22 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v22))
                break;
        }
    }
}
```

## `sub_103222e1` `0x103222e1`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103222e1(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10322317` `0x10322317`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10322317(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032231e` `0x1032231e`

_3 bytes. (leaf/helper — see body)_

```c
void sub_1032231e(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032234c` `0x1032234c`

_45 bytes. (leaf/helper — see body)_

```c
int sub_1032234c(void)
{
    char *v10;  // eax
    unsigned int v11;  // cc_dep1
    unsigned int v20;  // edi
    unsigned int v22;  // 4104
    unsigned int v23;  // cc_dep1
    unsigned int v24;  // cc_dep2
    unsigned int v26;  // 4101
    unsigned int v12;  // cc_dep2
    unsigned int v13;  // 4110
    unsigned int v14;  // id
    unsigned int v15;  // ac
    unsigned int v16;  // ecx
    unsigned int v17;  // edx
    unsigned int v18;  // ebx
    unsigned int v19;  // esi
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    char *v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    char *v6;  // [bp-0x8]
    char *v7;  // [bp-0x4]
    unsigned int v8;  // [bp-0x4]

    *(v10) = *(v10) + *((char *)&v10);
    v11 = *(v10);
    v12 = *((char *)&v10);
    v7 = v10;
    if (v11 + v12 >= 0)
        goto LABEL_10322356;
LABEL_10322356:
    v13 = _ccall(1, v11, v12, 0);
    v8 = v13 | 0x202 | v14 * 0x200000 & 0x200000 | v15 * 0x40000 & 0x40000;
    v6 = v7;
    v5 = v16;
    v4 = v17;
    v3 = v18;
    v2 = &v8;
    v1 = v19;
    v0 = v20;
    v22 = _ccall(0, 6, v17, v17, 0);
    v23 = v17;
    if (!((char)v22))
    {
        if (!(1))
            goto LABEL_10322363;
LABEL_10322363:
        if (0)
            goto LABEL_0x103222fb;
        v26 = _ccall(2, 15, 3, 0, 0);
        if ((char)v26)
            goto LABEL_0x10322374;
    }
    else
    {
        v26 = _ccall(2, 6, v23, v24, 0);
        if ((char)v26)
            goto LABEL_0x10322374;
    }
}
```

## `sub_1032236d` `0x1032236d`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1032236d(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10322385` `0x10322385`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10322385(void)
{
}
```

## `sub_10322397` `0x10322397`

_67 bytes. (leaf/helper — see body)_

```c
int sub_10322397(void)
{
    void* v4;  // ebx
    unsigned int v5;  // 4096
    char *v14;  // eax
    unsigned int v6;  // cc_op
    unsigned int v7;  // cc_dep1
    unsigned int v8;  // cc_dep2
    unsigned int v9;  // cc_ndep
    unsigned int v10;  // 4117
    unsigned int v11;  // 4125
    unsigned short v12;  // ax
    unsigned int v13;  // 4126
    unsigned int v2;  // [bp+0xff414]
    char *v3;  // [bp+0xff6ec]

    v5 = (int)v4[397277103];
    *((unsigned int *)&v4[397277103]) = (int)v4[397277103] - 1;
    v10 = _ccall(v6, v7, v8, v9);
    v11 = _ccall(21, v5 - 1, 0, v10);
    v13 = _ccall((unsigned short)v11 CONCAT v12, 47);
    v14 = _INSERT(v12 CONCAT 0, 0, v13);
    *(v14) = *(v14) + *((char *)&v14);
    v3 = v14;
    sub_10350ad0(/* unsupported instruction */ - 3056, 0, 716);
    v2 = 65537;
    sub_103223db(); /* do not return */
}
```

## `sub_103223b0` `0x103223b0`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103223b0(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103223db` `0x103223db`

_57 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b0dc;

void sub_103223db(unsigned int a0)
{
    unsigned int v11;  // cc_op
    unsigned int v12;  // cc_dep1
    unsigned int v21;  // ebx
    unsigned int v22;  // esi
    unsigned int v23;  // edi
    unsigned int v24;  // cc_op
    unsigned int v25;  // 4104
    unsigned int v26;  // cc_dep1
    unsigned int v27;  // cc_dep2
    unsigned int v29;  // 4101
    unsigned int v13;  // cc_dep2
    unsigned int v14;  // cc_ndep
    unsigned int v15;  // 4123
    unsigned int v16;  // 4110
    unsigned int v17;  // id
    unsigned int v18;  // ac
    unsigned int v19;  // ecx
    unsigned int v20;  // edx
    unsigned int v0;  // [bp-0x2c]
    unsigned int v1;  // [bp-0x28]
    char *v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x1c]
    unsigned int v4;  // [bp-0x18]
    unsigned int v5;  // [bp-0x14]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0xc]
    unsigned int v10;  // [bp+0xff6ec]

    v7 = g_1038b0dc(v10, a0);
    v15 = _ccall(2, v11, v12, v13, v14);
    if (!((char)v15))
        goto LABEL_103223f1;
LABEL_103223f1:
    v16 = _ccall(v11, v12, v13, v14);
    v8 = v16 | 0x202 | v17 * 0x200000 & 0x200000 | v18 * 0x40000 & 0x40000;
    v6 = v7;
    v5 = v19;
    v4 = v20;
    v3 = v21;
    v2 = &v8;
    v1 = v22;
    v0 = v23;
    v24 = 6;
    v25 = _ccall(0, 6, v20, v20, 0);
    v26 = v20;
    if (!((char)v25))
    {
        if (!(1))
            goto LABEL_103223fe;
LABEL_103223fe:
        v24 = 15;
        v26 = 3;
        v27 = 0;
        if (0)
            goto LABEL_0x10322396;
        else
            goto LABEL_10322406;
    }
LABEL_10322406:
    v29 = _ccall(2, v24, v26, v27, 0);
    if ((char)v29)
        goto LABEL_0x1032240f;
}
```

## `sub_10322408` `0x10322408`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10322408(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032241c` `0x1032241c`

_76 bytes. (leaf/helper — see body)_

```c
int sub_1032241c(void)
{
    void* v1;  // [bp+0x8]

    *((unsigned int *)&v1[2324]) = 0;
    *((int *)&v1[2320]) = sub_102ec930(v1 - 2872, 4, 4294967295);
    *((unsigned int *)&v1[2336]) = (int)v1[2320] % 28;
    sub_1032246b(); /* do not return */
}
```

## `sub_10322420` `0x10322420`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10322420(void)
{
}
```

## `sub_10322422` `0x10322422`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10322422(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032246b` `0x1032246b`

_141 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103901c0[4];
extern unsigned int g_103a2820[4];

void sub_1032246b(char a0)
{
    unsigned int v15;  // edx
    unsigned int idx;  // edx
    unsigned int v25;  // cc_ndep
    unsigned int v27;  // 4101
    unsigned int v28;  // 4101
    unsigned int v29;  // 4101
    unsigned int v30;  // 4101
    unsigned int v31;  // 4101
    unsigned int v32;  // 4101
    unsigned int v33;  // 4101
    unsigned int v17[4];  // eax
    unsigned int v18;  // ebx
    unsigned int v19;  // esi
    unsigned int v20;  // edi
    unsigned int v21;  // 4101
    unsigned int v22;  // cc_op
    unsigned int v23;  // cc_dep1
    unsigned int v24;  // cc_dep2
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5[4];  // [bp-0x8]
    unsigned int v6[4];  // [bp-0x4]
    unsigned int v8;  // [bp+0x14]
    unsigned int v10;  // [bp+0xff6e4]
    unsigned int v11[4];  // [bp+0xff6e8]
    unsigned int v12;  // [bp+0xff6f0]
    unsigned int v13[4];  // [bp+0xff6f8]

    v12 = g_103901c0[v10](v15);
    v11[0] = NULL;
    idx = v10;
    v17 = g_103a2820[idx];
    v13[0] = v17;
    if (v11 >= v13)
    {
        v6 = v17;
        v5 = v11;
        v4 = idx;
        v3 = v18;
        v2 = /* unsupported instruction */;
        v1 = v19;
        v0 = v20;
LABEL_10322525:
        v21 = _ccall(0, 15, 0, 0, 0);
        if ((char)v21)
            goto LABEL_10322527;
        else
            goto LABEL_10322528;
        v27 = _ccall(8, v22, v23, v24, v25);
        if (!((char)v27))
        {
            v28 = _ccall(10, 15, 0, 0, 0);
            if (!((char)v28))
            {
                v29 = _ccall(0, 15, 0, 0, 0);
                if ((char)v29)
                    goto LABEL_10322527;
                goto LABEL_10322528;
            }
            else
            {
                v30 = _ccall(8, 15, 0, 0, 0);
                if ((char)v30)
                {
LABEL_10322525:
                    v32 = _ccall(4, v22, v23, v24, v25);
                    if (!((char)v32) || (v33 = (unsigned int)_ccall(0, v22, v23, v24, v25), (char)v33))
                    {
LABEL_10322527:
                        __unsupported_jumpkind_Ijk_NoDecode()
                    }
LABEL_10322528:
                    __unsupported_jumpkind_Ijk_NoDecode()
                }
            }
        }
        else
        {
            __unsupported_jumpkind_Ijk_NoDecode()
            v31 = _ccall(8, v22, v23, v24, v25);
            if ((char)v31)
                goto LABEL_10322525;
            goto LABEL_1032252e;
        }
        while (true)
        {
            if (/* unsupported instruction */)
            {
                x86g_dirtyhelper_storeF80le(Sub(vvar_95{r16|4b}, 0x10<32>), Reinterpret(F64->I64, unsupported_<class 'pyvex.expr.GetI'>()))
                /* unsupported instruction */
            }
            else
            {
                x86g_dirtyhelper_storeF80le(Sub(vvar_95{r16|4b}, 0x10<32>), Reinterpret(F64->I64, nan<64>))
                /* unsupported instruction */
            }
            __unsupported_jumpkind_Ijk_NoDecode()
            __unsupported_jumpkind_Ijk_NoDecode()
LABEL_1032252e:
            idx = v8;
        }
    }
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032251b` `0x1032251b`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1032251b(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10322534` `0x10322534`

_507 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char field_0;
} struct_1;

typedef struct struct_0 {
    struct struct_1 *field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
} struct_0;

extern struct_0 g_103a2730;

int sub_10322534(void)
{
    void* idx;  // ebx
    unsigned int v16;  // eax
    unsigned int v25;  // 4140
    unsigned int v28;  // eax
    unsigned long v29;  // ldt
    unsigned long v30;  // gdt
    unsigned long v31;  // 4115
    unsigned int v17;  // edx
    unsigned int v18;  // 4193
    unsigned int v19;  // id
    unsigned int v20;  // ac
    unsigned int v21;  // esi
    unsigned int v22;  // edi
    unsigned int v23;  // 4110
    unsigned int v24;  // cc_dep1
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    char *v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    unsigned int v6;  // [bp-0x4]
    unsigned int v7;  // [bp-0x4]
    char *v9;  // [bp+0xff404]
    unsigned int v10;  // [bp+0xff408]
    unsigned int v11;  // [bp+0xff4d4]
    unsigned int idx1;  // [bp+0xff6e4]
    unsigned int index;  // [bp+0xff6e8]
    unsigned int v14;  // [bp+0xff6f0]

    *((unsigned int *)&idx[650155268]) = (int)idx[650155268] - 1;
    v17 = *((int *)(v16 + index * 4));
    if (v17 != v14)
        goto LABEL_0x103227dc;
    v6 = index;
    v5 = v16;
    v18 = _ccall(6, v17, v14, 0);
    v7 = v18 | 0x202 | v19 * 0x200000 & 0x200000 | v20 * 0x40000 & 0x40000;
    v4 = v6;
    v3 = v17;
    v2 = &v7;
    v1 = v21;
    v0 = v22;
    if (!(1))
        goto LABEL_10322578;
LABEL_10322578:
    for (; (v23 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v23 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
    v24 = v7 & 2261;
    v25 = _ccall(0, 0, v7 & 2261, 0, 0);
    v28 = *((int *)&((&g_103a2730.field_0)[idx1])[4 * index]);
    v9 = v28;
    v10 = v11 & 4055;
    *((char *)v28) = *((char *)v28) + (char)v28;
    v31 = _ccall(v29, v30, 0xfff4, 144017688);
    goto v31;
    *((unsigned int *)&idx[0xbff7b]) = (int)idx[0xbff7b] - 1;
    goto *((int *)0xffffff);
}
```

## `sub_10322573` `0x10322573`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10322573(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032257a` `0x1032257a`

_3 bytes. (leaf/helper — see body)_

```c
void sub_1032257a(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103225a3` `0x103225a3`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103225a3(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

