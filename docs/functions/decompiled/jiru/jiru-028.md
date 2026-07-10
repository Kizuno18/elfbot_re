# elfbot.dll decompiled — jiru 0x1032264a..0x1032301e

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1032264a` `0x1032264a`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1032264a(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10322674` `0x10322674`

_5 bytes. (leaf/helper — see body)_

```c
int sub_10322674(void)
{
    char *v1;  // eax

    *(v1) = *(v1) + *((char *)&v1);
}
```

## `sub_1032267a` `0x1032267a`

_66 bytes. (leaf/helper — see body)_

```c
int sub_1032267a(unsigned int a0, unsigned int a1)
{
    unsigned int idx;  // eax
    unsigned int v13;  // ecx
    unsigned int v14;  // 4103
    unsigned int v15;  // ecx
    unsigned int v16;  // 4222
    unsigned int v17;  // id
    unsigned int v18;  // ac
    unsigned int v19;  // ebx
    unsigned int v20;  // esi
    unsigned int v21;  // edi
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    char *v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    unsigned int v7;  // [bp-0x4]
    unsigned int v8;  // [bp-0x4]
    unsigned int v10;  // [bp+0xff4cc]
    unsigned int v11;  // [bp+0xff6e8]

    idx = v11;
    v13 = *((int *)(a0 + idx * 4)) ^ *((int *)(/* unsupported instruction */ + a1 * 4 - 2288));
    v14 = v10;
    v15 = v13 + v10;
    v10 = v15;
    v7 = v15;
    v6 = idx;
    v16 = _ccall(3, v13, v14, 0);
    v8 = v16 | 0x202 | v17 * 0x200000 & 0x200000 | v18 * 0x40000 & 0x40000;
    v5 = v7;
    v4 = a1;
    v3 = v19;
    v2 = &v8;
    v1 = v20;
    v0 = v21;
    if (!(1))
        goto LABEL_0x103226b6;
    if (!(1))
        goto LABEL_103226bd;
LABEL_103226bd:
}
```

## `sub_103226b8` `0x103226b8`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103226b8(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103226ea` `0x103226ea`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103226ea(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10322731` `0x10322731`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10322731(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10322745` `0x10322745`

_14 bytes. (leaf/helper — see body)_

```c
int sub_10322745(void)
{
}
```

## `sub_10322749` `0x10322749`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10322749(void)
{
}
```

## `sub_1032274b` `0x1032274b`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1032274b(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10322778` `0x10322778`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10322778(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032277f` `0x1032277f`

_3 bytes. (leaf/helper — see body)_

```c
void sub_1032277f(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103227c8` `0x103227c8`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103227c8(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103227ee` `0x103227ee`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103227ee(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10322843` `0x10322843`

_655 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    int field_0;
    char padding_4[12];
    unsigned short field_10[2];
    char field_12;
    char padding_13[1];
    unsigned int field_14;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b128;
extern unsigned int g_1038c7e4;
extern unsigned int g_1038c7fc;
extern unsigned int g_1038c818;
extern unsigned int g_1038c848;
extern unsigned int g_1038c85c;
extern char g_1038ccb8;
extern unsigned int g_103a2910;
extern unsigned int g_103a2928;

int sub_10322843(void)
{
    struct_0 *v19;  // edx
    unsigned int v20;  // eax
    unsigned int v29;  // 4104
    struct_0 *v30;  // cc_dep1
    unsigned int v32;  // 4101
    unsigned int v33;  // eax
    unsigned int v34;  // ecx
    unsigned int v35;  // ebx
    unsigned int v36;  // esi
    unsigned int v37;  // edi
    unsigned int v38;  // 4101
    unsigned int v21;  // 4110
    unsigned int v39;  // 4103
    unsigned int v40;  // 4101
    unsigned int v41;  // 4101
    unsigned int v42;  // 4101
    unsigned int v43;  // 4101
    unsigned int v44;  // 4101
    unsigned int v45;  // 4101
    unsigned int v46;  // ecx
    unsigned int v47;  // 4193
    unsigned int v48;  // id
    unsigned int v22;  // id
    unsigned int v49;  // ac
    unsigned int v50;  // ebx
    unsigned int v51;  // esi
    unsigned int v52;  // edi
    unsigned int v53;  // 4110
    unsigned int v54;  // cc_dep1
    unsigned int v55;  // 4101
    unsigned int v56;  // eax
    unsigned int v57;  // edx
    unsigned int v58;  // 4110
    unsigned int v23;  // ac
    unsigned int v59;  // cc_op
    unsigned int v60;  // 4104
    unsigned int v61;  // cc_dep1
    unsigned int v24;  // ecx
    unsigned int v63;  // 4101
    void* v64;  // ecx
    unsigned int v65;  // edx
    unsigned int v66;  // ebx
    unsigned int v25;  // ebx
    unsigned int v67;  // esi
    unsigned int v68;  // eax
    unsigned int v69;  // 4101
    unsigned int v70;  // ebx
    unsigned int v71;  // 4103
    unsigned int v72;  // 4101
    unsigned int v73;  // 4101
    unsigned int v74;  // 4101
    unsigned int v75;  // 4101
    unsigned int v76;  // 4101
    unsigned int v26;  // esi
    unsigned int v77;  // 4101
    unsigned int *v78;  // edi
    unsigned int idx;  // edx
    unsigned int v80;  // 4101
    unsigned int v81;  // ecx
    unsigned int v82;  // cc_dep1
    unsigned int v83;  // eax
    unsigned int v84;  // eax
    unsigned int v85;  // ecx
    unsigned int v86;  // 4193
    unsigned int v27;  // edi
    unsigned int v87;  // id
    unsigned int v88;  // ac
    unsigned int v89;  // 4110
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    char *v2;  // [bp-0x1c], Other Possible Types: unsigned int
    char *v3;  // [bp-0x18], Other Possible Types: unsigned int
    char *v4;  // [bp-0x14], Other Possible Types: unsigned int
    void* v5;  // [bp-0x10], Other Possible Types: struct_0 *, unsigned int
    struct_0 *v6;  // [bp-0xc], Other Possible Types: unsigned int
    struct_0 *v7;  // [bp-0x8], Other Possible Types: unsigned int
    unsigned int v8;  // [bp-0x4]
    char v9;  // [bp+0x0]
    unsigned int v10;  // [bp+0x4]
    unsigned int v11;  // [bp+0xfefa8]
    unsigned int v12;  // [bp+0xff3ec]
    int v13;  // [bp+0xff3f0]
    unsigned int v14;  // [bp+0xff3f4]
    unsigned int v15;  // [bp+0xffe88]
    struct_0 *v16;  // [bp+0xffe8c]
    int v18;  // [bp+0x100010]

    v19 = v16;
    if (v19->field_0 == 2)
    {
        v8 = v20;
        if (v19->field_0 >= 2)
            goto LABEL_10322856;
LABEL_10322856:
        v21 = _ccall(6, v19->field_0, 2, 0);
        v8 = v21 | 0x202 | v22 * 0x200000 & 0x200000 | v23 * 0x40000 & 0x40000;
        v7 = v20;
        v6 = v24;
        v5 = v19;
        v4 = v25;
        v3 = &v8;
        v1 = v26;
        v0 = v27;
        v29 = _ccall(0, 6, v19, v19, 0);
        v30 = v19;
        if (!((char)v29))
        {
            if (!(1))
                goto LABEL_10322863;
LABEL_10322863:
            if (0)
                goto LABEL_0x103227fb;
            v32 = _ccall(2, 15, 0x3, NULL, 0);
            if ((char)v32)
                goto LABEL_0x10322874;
        }
        else
        {
            v32 = _ccall(2, 6, v30, v19, 0);
            if ((char)v32)
                goto LABEL_0x10322874;
        }
    }
    else if (v16->field_0 == 4)
    {
        v8 = v33;
        v7 = v34;
        v6 = v16;
        v5 = v35;
        v4 = &v9;
        v3 = /* unsupported instruction */;
        v2 = v36;
        v1 = v37;
LABEL_103228f1:
        v38 = _ccall(0, 15, 0, 0, 0);
        if ((char)v38)
            goto LABEL_103228f3;
        else
            goto LABEL_103228f4;
        while (true)
        {
LABEL_103228f3:
            __unsupported_jumpkind_Ijk_NoDecode()
            while (true)
            {
LABEL_103228f4:
                v39 = _ccall(10, 15, 0, 0, 0);
                if (!((char)v39))
                    __unsupported_jumpkind_Ijk_NoDecode()
                v40 = _ccall(8, 15, 0, 0, 0);
                if (!((char)v40))
                {
                    v41 = _ccall(10, 15, 0, 0, 0);
                    if (!((char)v41))
                    {
                        v42 = _ccall(0, 15, 0, 0, 0);
                        if ((char)v42)
                            break;
                        else
                            continue;
                    }
                    else
                    {
                        v43 = _ccall(8, 15, 0, 0, 0);
                        if ((char)v43)
                            goto LABEL_103228f1;
                        else
                            goto LABEL_0x103228fa;
                    }
                }
                else
                {
                    __unsupported_jumpkind_Ijk_NoDecode()
                    v44 = _ccall(8, 15, 0, 0, 0);
                    if ((char)v44)
                        goto LABEL_103228f1;
                    else
                        goto LABEL_0x103228fa;
                }
LABEL_103228f1:
                if ((v45 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v45))
                    break;
            }
        }
    }
    else if (v16->field_0 == 5)
    {
        v8 = v46;
        v7 = v16;
        v47 = _ccall(6, v16->field_0, 5, 0);
        v8 = v47 | 0x202 | v48 * 0x200000 & 0x200000 | v49 * 0x40000 & 0x40000;
        v6 = v46;
        v5 = v6;
        v4 = v50;
        v3 = &v8;
        v2 = /* unsupported instruction */;
        v1 = v51;
        v0 = v52;
        if (!(1))
            goto LABEL_1032295b;
LABEL_1032295b:
        for (; (v53 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v53 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
        v15 = 65538;
    }
    else
    {
        v54 = v16->field_0;
        if (v16->field_0 == 8)
        {
            v55 = _ccall(0, 6, v54, 8, 0);
            v13 = v16->field_10[1];
            v56 = sub_1034fef0(v13 + 2);
            v11 = v56;
            v57 = v11;
            v14 = v57;
            v8 = v56;
            if (&v10 >= NULL)
                goto LABEL_103229e5;
LABEL_103229e5:
            v58 = _ccall(3, &v8, 4, 0);
            v8 = v58 | 0x202 | v48 * 0x200000 & 0x200000 | v49 * 0x40000 & 0x40000;
            v7 = v8;
            v6 = v46;
            v5 = v57;
            v4 = v50;
            v3 = &v8;
            v2 = /* unsupported instruction */;
            v1 = v51;
            v0 = v52;
            v59 = 6;
            v60 = _ccall(0, 6, v57, v57, 0);
            v61 = v57;
            if (!((char)v60))
            {
                if (!(1))
                    goto LABEL_103229f2;
LABEL_103229f2:
                v59 = 15;
                v61 = 3;
                v57 = 0;
            }
            v63 = _ccall(2, v59, v61, v57, 0);
            if ((char)v63)
                goto LABEL_0x10322a03;
        }
        else if (v16->field_0 != 9)
        {
            if (v16->field_0 != 3)
            {
                sub_10322c6a();
                return;
            }
            else if (g_1038ccb8)
            {
                g_1038ccb8 = 0;
                sub_10322aef();
                return;
            }
            else
            {
                g_1038b128(v16->field_10);
                v7 = *((int *)&v16->field_12);
                v6 = g_1038b128(*((int *)&v16->field_12));
                v5 = v64;
                v4 = v65;
                v3 = v66;
                v2 = &v7;
                v1 = /* unsupported instruction */;
                v0 = v67;
                v68 = 0;
LABEL_10322b8b:
                v69 = _ccall(0, 15, 0, 0, 0);
                if ((char)v69)
                    goto LABEL_10322b8d;
                else
                    goto LABEL_10322b8e;
                while (true)
                {
LABEL_10322b8d:
                    __unsupported_jumpkind_Ijk_NoDecode()
                    while (true)
                    {
LABEL_10322b8e:
                        v71 = _ccall(10, 15, 0, 0, 0);
                        if ((char)v71)
                        {
                            v72 = _ccall(8, 15, 0, 0, 0);
                            if (!((char)v72))
                            {
                                v68 = 0;
                                if (!(1))
                                    goto LABEL_10322b93;
                                v73 = _ccall(10, 15, 0, 0, 0);
                                if (!((char)v73))
                                {
                                    v74 = _ccall(0, 15, 0, 0, 0);
                                    if ((char)v74)
                                        break;
                                    else
                                        continue;
                                }
                                else
                                {
                                    v75 = _ccall(8, 15, 0, 0, 0);
                                    if ((char)v75)
                                        goto LABEL_10322b8b;
                                    else
                                        goto LABEL_0x10322b94;
                                }
                            }
                            else
                            {
                                __unsupported_jumpkind_Ijk_NoDecode()
                                v76 = _ccall(8, 15, 0, 0, 0);
                                if ((char)v76)
                                    goto LABEL_10322b8b;
                                else
                                    goto LABEL_0x10322b94;
                            }
LABEL_10322b8b:
                            if ((v77 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v77))
                                break;
                        }
                        else
                        {
                            __unsupported_jumpkind_Ijk_NoDecode()
LABEL_10322b93:
                            /* unsupported instruction */ = &/* unsupported instruction */ ^ (int)v64[24];
                            *(v78) = *(v78) - 1;
                            idx = _INSERT(v65, 1, 208);
                            if (idx)
                            {
                                v80 = _ccall(0, 15, idx, 0, 0);
                                v12 = 0;
                                while (true)
                                {
                                    v81 = g_103a2928 * 16;
                                    v82 = v12;
                                    if (v12 >= v81)
                                        break;
                                    /* unsupported instruction */ = /* unsupported instruction */ - 4;
                                    v83 = sub_102eb870(v18);
                                    idx = v12;
                                    *((unsigned int *)(g_103a2910 + idx * 4)) = v83 ^ g_1038c7fc ^ g_1038c818 ^ g_1038c7e4 ^ g_1038c848 ^ g_1038c85c;
                                    v68 = v12 + 1;
                                    v12 = v68;
                                }
                                /* unsupported instruction */ = /* unsupported instruction */ - 4;
                                *((unsigned int *)(/* unsupported instruction */ - 4)) = v81;
                                /* unsupported instruction */ = /* unsupported instruction */ - 4;
                                *((unsigned int *)(/* unsupported instruction */ - 4)) = v68;
                                /* unsupported instruction */ = /* unsupported instruction */ + 4;
                                v84 = *((int *)/* unsupported instruction */);
                                /* unsupported instruction */ = /* unsupported instruction */ + 4;
                                v85 = *((int *)/* unsupported instruction */);
                                /* unsupported instruction */ = /* unsupported instruction */ - 4;
                                v86 = _ccall(6, v82, v81, 0);
                                *((unsigned int *)(/* unsupported instruction */ - 4)) = v86 | 0x202 | v87 * 0x200000 & 0x200000 | v88 * 0x40000 & 0x40000;
                                *((unsigned int *)(/* unsupported instruction */ - 4)) = v84;
                                *((unsigned int *)(/* unsupported instruction */ - 8)) = v85;
                                *((unsigned int *)(/* unsupported instruction */ - 12)) = idx;
                                *((unsigned int *)(/* unsupported instruction */ - 16)) = v70;
                                *((int *)(/* unsupported instruction */ - 20)) = /* unsupported instruction */;
                                *((int *)(/* unsupported instruction */ - 24)) = /* unsupported instruction */;
                                *((unsigned int *)(/* unsupported instruction */ - 28)) = v67;
                                *((unsigned int **)(/* unsupported instruction */ - 32)) = v78;
                                if (!(1))
                                    goto LABEL_10322c3a;
LABEL_10322c3a:
                                for (; (v89 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v89 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
                            }
                        }
                    }
                }
            }
        }
    }
}
```

## `sub_1032286d` `0x1032286d`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1032286d(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10322881` `0x10322881`

_36 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c8b0;

int sub_10322881(void)
{
    g_1038c8b0 = g_1038c8b0 + 1;
    sub_103228a8();
    return;
}
```

## `sub_10322885` `0x10322885`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10322885(void)
{
}
```

## `sub_10322887` `0x10322887`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10322887(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103228a8` `0x103228a8`

_34 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    int field_8;
} struct_0;

int sub_103228a8(void)
{
    int v3;  // edx
    unsigned int v1;  // [bp+0xffe88]
    struct_0 *v2;  // [bp+0xffe8c]

    sub_103242b0(v2->field_8, v3);
    v1 = 65538;
}
```

## `sub_103228e7` `0x103228e7`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103228e7(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103228fe` `0x103228fe`

_43 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    int field_8;
} struct_0;

extern unsigned int g_1038c8b0;

int sub_103228fe(void)
{
    unsigned int v3;  // eax
    unsigned int v1;  // [bp+0xffe88]
    struct_0 *v2;  // [bp+0xffe8c]

    g_1038c8b0 = v3 - 1;
    sub_10324420(v2->field_8);
    v1 = 65538;
}
```

## `sub_10322956` `0x10322956`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10322956(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032295d` `0x1032295d`

_3 bytes. (leaf/helper — see body)_

```c
void sub_1032295d(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103229a4` `0x103229a4`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103229a4(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103229fc` `0x103229fc`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103229fc(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10322a10` `0x10322a10`

_25 bytes. (leaf/helper — see body)_

```c
int sub_10322a10(void)
{
    sub_10322a2c(0);
    return;
}
```

## `sub_10322a14` `0x10322a14`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10322a14(void)
{
}
```

## `sub_10322a16` `0x10322a16`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10322a16(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10322a2c` `0x10322a2c`

_135 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[12];
    unsigned int field_c;
    unsigned short field_10;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b0c0;
extern struct_0 *g_1038b0d0;
extern struct_0 *g_1038b0d4;
extern struct_0 *g_1038c8ac;

int sub_10322a2c(void)
{
    unsigned int v5;  // eax
    int v1;  // [bp+0xfefa4]
    int v2;  // [bp+0xff3f4]
    unsigned int v3;  // [bp+0xffe88]
    struct_1 *v4;  // [bp+0xffe8c]

    g_1038b0c0(g_1038c8ac->field_0, v4->field_c, v2, v5);
    if (v4->field_10)
    {
        if (g_1038b0d4)
            g_1038b0d4(v2);
    }
    else
    {
        if (g_1038b0d0)
            g_1038b0d0(v2);
    }
    v1 = v2;
    sub_10350eb5(v1);
    v3 = 65538;
}
```

## `sub_10322aef` `0x10322aef`

_96 bytes. refs "%X::DA%08X"_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
    int field_8;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b07c;
extern struct_1 *g_1038b098;
extern struct_1 *g_1038b0cc;
extern struct_0 *g_1038c8ac;

int sub_10322aef(void)
{
    int v3;  // eax
    unsigned int v4;  // ecx
    char *v5;  // edx
    unsigned int v1;  // [bp+0xffe88]

    sub_10353127(/* unsupported instruction */ - 368, "%X::DA%08X", g_1038c8ac->field_8, v3);
    v4 = /* unsupported instruction */ - 368;
    *(v5) = *(v5) + *((char *)((void*)&v4 + 1));
    g_1038b098(v4);
    if (g_1038b07c() != 183)
    {
        v1 = 65538;
        g_1038b0cc(g_1038c8ac->field_4);
    }
}
```

## `sub_10322b81` `0x10322b81`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10322b81(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10322bab` `0x10322bab`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10322bab(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10322c35` `0x10322c35`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10322c35(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10322c3c` `0x10322c3c`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10322c3c(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10322c6a` `0x10322c6a`

_102 bytes. (leaf/helper — see body)_

```c
extern char g_1038f8e4;

int sub_10322c6a(void)
{
    unsigned int *v5;  // edx
    unsigned int v6;  // ecx
    unsigned int v15;  // 4110
    void* v7;  // ecx
    unsigned int v8;  // eax
    unsigned int *v9;  // esi
    unsigned int v10;  // eax
    unsigned int v11;  // 4138
    unsigned long v12;  // 4139
    unsigned int v13;  // ebx
    unsigned int v14;  // edi
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp-0x4]
    unsigned int v3;  // [bp+0xffe88]
    unsigned int v4;  // [bp+0x100070]

    if (*(v5) == 6)
    {
        v1 = v6;
        v7 = ~(v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff);
        v0 = v8;
        /* unsupported instruction */ = v4 * 3235821969;
        v10 = *(v9);
        v11 = _ccall(39, v4, 3235821969, 0);
        v12 = _ccall((int)v7[100], 1, v11, 4);
        *((unsigned int *)&v7[100]) = v12;
        *((unsigned int *)(/* unsupported instruction */ - 4)) = v10;
        *((void* *)(/* unsupported instruction */ - 8)) = v7;
        *((unsigned int **)(/* unsupported instruction */ - 12)) = v5;
        *((unsigned int *)(/* unsupported instruction */ - 16)) = v13;
        *((int *)(/* unsupported instruction */ - 20)) = /* unsupported instruction */;
        *((int *)(/* unsupported instruction */ - 24)) = /* unsupported instruction */;
        *((unsigned int **)(/* unsupported instruction */ - 28)) = v9 + 1;
        *((unsigned int *)(/* unsupported instruction */ - 32)) = v14;
        if (!(1))
            goto LABEL_10322c9a;
LABEL_10322c9a:
        for (; (v15 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v15 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
        *((char *)(*((int *)(/* unsupported instruction */ - 24)) - 3360)) = g_1038f8e4;
        sub_10322cca();
        return;
    }
    v3 = 65538;
}
```

## `sub_10322c95` `0x10322c95`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10322c95(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10322c9c` `0x10322c9c`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10322c9c(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10322cca` `0x10322cca`

_254 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
    char padding_10[12];
    unsigned int field_1c;
    unsigned short field_20;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b0c0;
extern struct_1 *g_1038c8ac;
extern char g_1038f8e4;
extern char g_8;

int sub_10322cca(void)
{
    unsigned int v17;  // eax
    struct_0 *v18;  // ecx
    unsigned int v27;  // 4101
    unsigned int v28;  // 4101
    unsigned int v29;  // 4101
    unsigned int v30;  // 4101
    void* v31;  // eax
    unsigned int v32;  // 4110
    unsigned int v33;  // id
    unsigned int v34;  // ac
    unsigned int v35;  // ebx
    unsigned int v36;  // esi
    unsigned int v19;  // edx
    unsigned int v37;  // edi
    unsigned int v40;  // 4104
    unsigned int v41;  // 4101
    unsigned int v20;  // ebx
    unsigned int v21;  // esi
    unsigned int v22;  // edi
    unsigned int v23;  // 4101
    unsigned int v24;  // 4103
    unsigned int v25;  // 4101
    unsigned int v26;  // 4101
    char v0;  // [bp-0x3777]
    unsigned int v1;  // [bp-0x38]
    unsigned int v2;  // [bp-0x34]
    unsigned int v3;  // [bp-0x30]
    char *v4;  // [bp-0x2c], Other Possible Types: unsigned int
    char *v5;  // [bp-0x28], Other Possible Types: unsigned int
    unsigned int v6;  // [bp-0x24]
    struct_0 *v7;  // [bp-0x20], Other Possible Types: unsigned int
    struct_0 *v8;  // [bp-0x1c], Other Possible Types: unsigned int
    unsigned int v9;  // [bp-0x18]
    unsigned int v10;  // [bp-0x14]
    unsigned int v11;  // [bp-0x4]
    unsigned int v13;  // [bp+0xff1d8]
    char v14;  // [bp+0xff1dc]
    struct_0 *idx;  // [bp+0xffe8c]

    sub_10350ad0(/* unsupported instruction */ - 3359, 0, 259);
    v14 = g_1038f8e4;
    sub_10350ad0(/* unsupported instruction */ - 3623, 0, 259);
    v13 = idx->field_1c;
    if (v13)
    {
        v10 = g_1038c8ac->field_0;
        v17 = g_1038b0c0(g_1038c8ac->field_0, v13, /* unsupported instruction */ - 3628, 4, 0);
        if (v13)
        {
            v18 = idx;
            v19 = v18->field_20;
            if (v19)
            {
                v9 = v17;
                v8 = v18;
                v7 = v19;
                v6 = v20;
                v5 = &v10;
                v4 = /* unsupported instruction */;
                v3 = v21;
                v2 = v22;
LABEL_10322d7a:
                v23 = _ccall(0, 15, 0, 0, 0);
                if ((char)v23)
                    goto LABEL_10322d7c;
                else
                    goto LABEL_10322d7d;
                while (true)
                {
LABEL_10322d7c:
                    __unsupported_jumpkind_Ijk_NoDecode()
                    while (true)
                    {
LABEL_10322d7d:
                        v24 = _ccall(10, 15, 0, 0, 0);
                        if (!((char)v24))
                        {
                            __unsupported_jumpkind_Ijk_NoDecode()
                            g_8 = g_8 + *((char *)((void*)&v18 + 1));
                            v31 = 0 + *(NULL);
                            v0 += *((char *)&v18);
                            (int)v31[117]();
                        }
                        v25 = _ccall(8, 15, 0, 0, 0);
                        if (!((char)v25))
                        {
                            if (false)
                            {
                                g_8 = g_8 + *((char *)((void*)&v18 + 1));
                                v31 = 0 + *(NULL);
                                v0 += *((char *)&v18);
                                (int)v31[117]();
                            }
                            v26 = _ccall(10, 15, 0, 0, 0);
                            if (!((char)v26))
                            {
                                v27 = _ccall(0, 15, 0, 0, 0);
                                if ((char)v27)
                                    break;
                                else
                                    continue;
                            }
                            else
                            {
                                v28 = _ccall(8, 15, 0, 0, 0);
                                if ((char)v28)
                                    goto LABEL_10322d7a;
                                else
                                    goto LABEL_0x10322d83;
                            }
                        }
                        else
                        {
                            __unsupported_jumpkind_Ijk_NoDecode()
                            v29 = _ccall(8, 15, 0, 0, 0);
                            if ((char)v29)
                                goto LABEL_10322d7a;
                            else
                                goto LABEL_0x10322d83;
                        }
LABEL_10322d7a:
                        if ((v30 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v30))
                            break;
                    }
                }
            }
            else
            {
                v9 = v17;
                if (v7 >= 0)
                    goto LABEL_10322e34;
LABEL_10322e34:
                v32 = _ccall(15, v7, 0, 0);
                v9 = v32 | 0x202 | v33 * 0x200000 & 0x200000 | v34 * 0x40000 & 0x40000;
                v8 = v9;
                v7 = v18;
                v6 = 0;
                v5 = v35;
                v4 = &v9;
                v3 = /* unsupported instruction */;
                v2 = v36;
                v1 = v37;
                v40 = _ccall(0, 6, 0, 0, 0);
                if (!((char)v40))
                {
                    if (!(1))
                        goto LABEL_10322e41;
LABEL_10322e41:
                    if (0)
                        goto LABEL_0x10322dd9;
                    v41 = _ccall(2, 15, 3, 0, 0);
                    if ((char)v41)
                        goto LABEL_0x10322e52;
                }
                else
                {
                    v41 = _ccall(2, 6, 0, 0, 0);
                    if ((char)v41)
                        goto LABEL_0x10322e52;
                }
            }
        }
    }
    v11 = idx->field_c;
}
```

## `sub_10322d70` `0x10322d70`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10322d70(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10322d9a` `0x10322d9a`

_50 bytes. refs "(Unicode) "_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b0c0;

int sub_10322d9a(void)
{
    unsigned int *v5;  // edx
    unsigned int v6;  // 4101
    char *v0;  // [bp-0x103c]
    char v1;  // [bp-0x1038]
    char v2;  // [bp-0xd20]
    char *v3;  // [bp-0xc]
    unsigned int v4;  // [bp+0x4]

    g_1038b0c0(*(v5));
    v0 = &v1;
    v3 = &v2;
    sub_10352cb0(&v2, "(Unicode) ");
    if ((char)(&v4 >= 0x80000000 ? 1 : 0))
        goto LABEL_0x10322dd1;
    v6 = _ccall(12, 3, &v3, 8, 0);
    if ((char)v6)
        goto LABEL_0x10322dcf;
    else
        goto LABEL_0x10322dcc;
}
```

## `sub_10322dce` `0x10322dce`

_9 bytes. (leaf/helper — see body)_

```c
void sub_10322dce(void)
{
    unsigned int v0;  // [bp-0x4]

    __unsupported_jumpkind_Ijk_NoDecode()
    v0 = 0;
}
```

## `sub_10322dda` `0x10322dda`

_82 bytes. (leaf/helper — see body)_

```c
int sub_10322dda(void)
{
    void* v3;  // eax
    void* v4;  // ebx
    char *v1;  // [bp+0xfefc4]
    void* v2;  // [bp+0xfefc8]

    (int)v3[24]();
    for (*((unsigned int *)&v4[2054616892]) = (int)v4[2054616892] + 1; *((short *)v2); v2 += 2)
    {
        *(v1) = *((char *)v2);
        v1 += 1;
    }
}
```

## `sub_10322e4b` `0x10322e4b`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10322e4b(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10322e5f` `0x10322e5f`

_27 bytes. (leaf/helper — see body)_

```c
int sub_10322e5f(void)
{
    sub_10322e7d(260, 0);
    return;
}
```

## `sub_10322e63` `0x10322e63`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10322e63(void)
{
}
```

## `sub_10322e65` `0x10322e65`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10322e65(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10322e7d` `0x10322e7d`

_95 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b0c0;
extern struct_0 *g_1038c8ac;

int sub_10322e7d(void)
{
    unsigned int v11;  // ecx
    unsigned int v12;  // edx
    unsigned int v21;  // esi
    unsigned int v22;  // edi
    unsigned int v23;  // 4110
    unsigned int v13;  // cc_op
    unsigned int v14;  // cc_dep1
    unsigned int v15;  // cc_dep2
    unsigned int v16;  // cc_ndep
    unsigned int v17;  // 4193
    unsigned int v18;  // id
    unsigned int v19;  // ac
    unsigned int v20;  // ebx
    unsigned int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x2c]
    char *v2;  // [bp-0x24]
    unsigned int v3;  // [bp-0x20]
    unsigned int v4;  // [bp-0x1c]
    unsigned int v5;  // [bp-0x18]
    unsigned int v6;  // [bp-0x14]
    unsigned int v7;  // [bp-0x10]
    unsigned int v8;  // [bp-0x10]
    unsigned int v10;  // [bp+0xff1d8]

    v7 = v11;
    v6 = g_1038b0c0(g_1038c8ac->field_0, v10, v12);
    v17 = _ccall(v13, v14, v15, v16);
    v8 = v17 | 0x202 | v18 * 0x200000 & 0x200000 | v19 * 0x40000 & 0x40000;
    v5 = v7;
    v4 = v12;
    v3 = v20;
    v2 = &v8;
    v1 = v21;
    v0 = v22;
    if (!(1))
        goto LABEL_10322ebb;
LABEL_10322ebb:
    for (; (v23 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v23 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
}
```

## `sub_10322eb6` `0x10322eb6`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10322eb6(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10322ebd` `0x10322ebd`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10322ebd(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10322eeb` `0x10322eeb`

_5 bytes. (leaf/helper — see body)_

```c
int sub_10322eeb(void)
{
}
```

## `sub_10322f1d` `0x10322f1d`

_42 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b0c8;
extern struct_0 *g_1038b1bc;
extern char g_103a26a4;

int sub_10322f1d(void)
{
    unsigned int v1[3];  // [bp+0xffe8c]

    g_1038b0c8(v1[1], v1[2], 65538);
    g_1038b1bc(&g_103a26a4);
}
```

## `sub_10322f60` `0x10322f60`

_51 bytes. (leaf/helper — see body)_

```c
int sub_10322f60(void)
{
    unsigned int v13;  // esi
    unsigned int v14;  // eax
    unsigned int v23;  // 4104
    unsigned int v24;  // cc_dep1
    unsigned int v25;  // cc_dep2
    unsigned int v27;  // 4101
    unsigned int v15;  // 4110
    unsigned int v16;  // id
    unsigned int v17;  // ac
    unsigned int v18;  // ecx
    unsigned int v19;  // edx
    unsigned int v20;  // ebx
    unsigned int v21;  // edi
    unsigned int v0;  // [bp-0x44]
    unsigned int v1;  // [bp-0x40]
    char *v2;  // [bp-0x3c]
    char *v3;  // [bp-0x38]
    unsigned int v4;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x24]
    unsigned int v10;  // [bp-0x1c]
    char v11;  // [bp-0x4]

    v10 = v13;
    v8 = v14;
    if (&/* unsupported instruction */ >= 20)
        goto LABEL_10322f70;
LABEL_10322f70:
    v15 = _ccall(6, &v11, 20, 0);
    v9 = v15 | 0x202 | v16 * 0x200000 & 0x200000 | v17 * 0x40000 & 0x40000;
    v7 = v8;
    v6 = v18;
    v5 = v19;
    v4 = v20;
    v3 = &v9;
    v2 = &v11;
    v1 = v13;
    v0 = v21;
    v23 = _ccall(0, 6, v19, v19, 0);
    v24 = v19;
    if (!((char)v23))
    {
        if (!(1))
            goto LABEL_10322f7d;
LABEL_10322f7d:
        if (0)
            goto LABEL_0x10322f15;
        v27 = _ccall(2, 15, 3, 0, 0);
        if ((char)v27)
            goto LABEL_0x10322f8e;
    }
    else
    {
        v27 = _ccall(2, 6, v24, v25, 0);
        if ((char)v27)
            goto LABEL_0x10322f8e;
    }
}
```

## `sub_10322f87` `0x10322f87`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10322f87(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10322f9b` `0x10322f9b`

_151 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
    struct struct_1 *field_c;
    char padding_10[839349698];
    char field_320775d2;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern unsigned int g_103a2934;

int sub_10322f9b(void)
{
    unsigned int v10;  // 4097
    unsigned int v11;  // eax
    struct_0 *idx;  // ebp
    unsigned int v21;  // edx
    unsigned int v22;  // cc_dep1
    unsigned int v23;  // edx
    unsigned int v24;  // 4110
    unsigned int v25;  // cc_op
    unsigned int v26;  // 4104
    unsigned int v27;  // cc_dep1
    unsigned int v29;  // 4101
    unsigned int v12;  // 4101
    void* v30;  // eax
    void* v31;  // eax
    unsigned int v13;  // 4103
    unsigned int v14;  // 4101
    unsigned int v15;  // 4101
    unsigned int v16;  // 4101
    unsigned int v17;  // 4101
    unsigned int v18;  // 4101
    unsigned int v19;  // 4101
    char *v0;  // [bp+0x0]
    char *v1;  // [bp+0x4], Other Possible Types: unsigned int
    struct_0 *v2;  // [bp+0x8], Other Possible Types: unsigned int
    char *v3;  // [bp+0xc], Other Possible Types: struct_0 *
    char *v4;  // [bp+0x10], Other Possible Types: void*
    void* v5;  // [bp+0x14], Other Possible Types: unsigned int
    unsigned int v6;  // [bp+0x18]
    unsigned int *v7;  // [bp+0x1c], Other Possible Types: unsigned int
    unsigned int v8;  // [bp+0x20]
    char v9;  // [bp+0x24]

    v10 = v8;
    v11 = v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff;
    v8 = v11 * 0x1000000 | v11 * 0x100 & 0xff0000 | v11 >> 8 & 0xff00 | v11 >> 24 & 0xff;
    v7 = ~(~(v6));
    v6 = v5;
    v5 = v4;
    v4 = &v9;
    v3 = v2;
    v2 = v1;
    v1 = v0;
LABEL_10322fc8:
    v12 = _ccall(0, 15, 0, 0, 0);
    if ((char)v12)
        goto LABEL_10322fca;
    else
        goto LABEL_10322fcb;
    while (true)
    {
LABEL_10322fca:
        __unsupported_jumpkind_Ijk_NoDecode()
        while (true)
        {
LABEL_10322fcb:
            v13 = _ccall(10, 15, 0, 0, 0);
            if ((char)v13)
            {
                v14 = _ccall(8, 15, 0, 0, 0);
                if (!((char)v14))
                {
                    if (!(1))
                        goto LABEL_10322fd0;
                    v15 = _ccall(10, 15, 0, 0, 0);
                    if (!((char)v15))
                    {
                        v16 = _ccall(0, 15, 0, 0, 0);
                        if ((char)v16)
                            break;
                        else
                            continue;
                    }
                    v17 = _ccall(8, 15, 0, 0, 0);
                    if ((char)v17)
                        goto LABEL_10322fc8;
                    goto LABEL_10322fd1;
                }
                __unsupported_jumpkind_Ijk_NoDecode()
                v18 = _ccall(8, 15, 0, 0, 0);
                if (!((char)v18))
                    goto LABEL_10322fd1;
LABEL_10322fc8:
                if ((v19 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v19))
                    break;
            }
            else
            {
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_10322fd0:
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_10322fd1:
                idx = v3;
                v21 = *((int *)(g_103a2934 + idx->field_8 * 4));
                v22 = v21 & 1;
                v23 = v21 & 1;
                if (!((char)v21 & 1))
                {
                    v8 = 0;
                    v7 = &idx->field_c->field_0;
                    v6 = idx->field_8;
                    v30 = (char *)v7 + *(v7);
                    *((char *)&v5[1240527677]) = (char)v5[1240527677] + *((char *)&v30);
                    idx->field_320775d2 = idx->field_320775d2 * 2 | idx->field_320775d2 >> 7;
                    v31 = v30 + *((int *)v30);
                    *((char *)&v31[9]) = (char)v31[9] + (char)v23;
                    *(v1) = *(v1) >> 1 | *(v1) * 128;
                }
                v8 = idx->field_8;
                if (v22 >= 0)
                    goto LABEL_10322fef;
LABEL_10322fef:
                v24 = _ccall(15, v22, 0, 0);
                v8 = v24 | 0x202 | ((char)(v10 >> 10) ? 4294967295 : 1) & 0x400 | ((char)(v10 >> 21) ? 1 : 0) * 0x200000 & 0x200000 | ((char)(v10 >> 18) ? 1 : 0) * 0x40000 & 0x40000;
                v7 = v8;
                v6 = g_103a2934;
                v5 = v23;
                v4 = v5;
                v3 = &v8;
                v2 = idx;
                v1 = v2;
                v0 = v1;
                v25 = 6;
                v26 = _ccall(0, 6, v23, v23, 0);
                v27 = v23;
                if (!((char)v26))
                {
                    if (!(1))
                        goto LABEL_10322ffc;
LABEL_10322ffc:
                    v25 = 15;
                    v27 = 3;
                    v23 = 0;
                    if (0)
                        goto LABEL_0x10322f94;
                    else
                        goto LABEL_10323004;
                }
LABEL_10323004:
                v29 = _ccall(2, v25, v27, v23, 0);
                if ((char)v29)
                    goto LABEL_0x1032300d;
            }
        }
    }
}
```

## `sub_10322f9f` `0x10322f9f`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10322f9f(void)
{
}
```

## `sub_10322fa1` `0x10322fa1`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10322fa1(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10322fbe` `0x10322fbe`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10322fbe(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323006` `0x10323006`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323006(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032301a` `0x1032301a`

_310 bytes. (leaf/helper — see body)_

```c
extern char g_103a2909;
extern unsigned int g_103a2914;

int sub_1032301a(void)
{
    unsigned int v17;  // edx
    unsigned int v18;  // ebx
    unsigned int v27;  // cc_dep1
    unsigned int v28;  // 4101
    unsigned int v29;  // 4193
    unsigned int v30;  // 4110
    unsigned int v31;  // cc_dep1
    unsigned int v32;  // 4101
    unsigned int v33;  // 4103
    unsigned int v34;  // 4101
    unsigned int v35;  // 4101
    unsigned int v36;  // 4101
    void* v19;  // ebp
    unsigned int v37;  // 4101
    unsigned int v38;  // 4101
    unsigned int v39;  // 4101
    unsigned int v40;  // edx
    unsigned int v41;  // ebx
    void* v42;  // ebp
    void* v43;  // esi
    void* v44;  // edi
    unsigned int v45;  // 4157
    void* v20;  // esi
    unsigned int v46;  // 4110
    unsigned int v47;  // 4097
    unsigned int v48;  // eax
    unsigned int v49;  // edx
    unsigned int v50;  // 4112
    unsigned int v51;  // edx
    unsigned int v52;  // 4110
    unsigned int v53;  // cc_op
    unsigned int v54;  // 4104
    void* v21;  // edi
    unsigned int v56;  // 4101
    unsigned int v22;  // 4097
    unsigned int v23;  // d
    unsigned int v24;  // id
    unsigned int v25;  // ac
    unsigned int v26;  // eax
    void* v0;  // [bp-0x1c]
    void* v1;  // [bp-0x18]
    void* v2;  // [bp-0x14]
    void* *v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    void* v6;  // [bp-0x4]
    void* v7;  // [bp+0x0]
    void* v8;  // [bp+0x4]
    void* v9;  // [bp+0x8]
    void* v10;  // [bp+0xc], Other Possible Types: char *
    char *v11;  // [bp+0x10], Other Possible Types: unsigned int
    unsigned int v12;  // [bp+0x14]
    unsigned int v13;  // [bp+0x18]
    unsigned int v14;  // [bp+0x1c]
    unsigned int v15;  // [bp+0x20]
    char v16;  // [bp+0x24]

    v17 = v12;
    v18 = v11;
    v19 = v9;
    v20 = v8;
    v21 = v7;
    v22 = v15;
    v23 = ((char)(v22 >> 10) ? 4294967295 : 1);
    v24 = ((char)(v22 >> 21) ? 1 : 0);
    v25 = ((char)(v22 >> 18) ? 1 : 0);
    v26 = (char)v19[16];
    v27 = v26;
    if (v26)
    {
        v28 = _ccall(0, 15, v27, 0, 0);
        v15 = ~(~(v13));
        v14 = v26;
        v29 = _ccall(15, v27, 0, 0);
        v15 = v29 | 0x202 | v23 & 0x400 | v24 * 0x200000 & 0x200000 | v25 * 0x40000 & 0x40000;
        v13 = v15;
        v12 = v17;
        v11 = v18;
        v10 = &v15;
        v9 = v19;
        v8 = v20;
        v7 = v21;
        if (!(1))
            goto LABEL_10323069;
LABEL_10323069:
        for (; (v30 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v30 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
        *((unsigned int *)&v9[8]) = 0;
    }
    else if (g_103a2909)
    {
        return;
    }
    else
    {
        v15 = 0;
        v14 = 0;
        v13 = v17;
        v12 = v18;
        v11 = &v16;
        v10 = v19;
        v9 = v20;
        v8 = v21;
        v31 = 0;
LABEL_10323219:
        v32 = _ccall(0, 15, 0, 0, 0);
        if ((char)v32)
            goto LABEL_1032321b;
        else
            goto LABEL_1032321c;
        while (true)
        {
LABEL_1032321b:
            __unsupported_jumpkind_Ijk_NoDecode()
            while (true)
            {
LABEL_1032321c:
                v33 = _ccall(10, 15, 0, 0, 0);
                if ((char)v33)
                {
                    v34 = _ccall(8, 15, 0, 0, 0);
                    if (!((char)v34))
                    {
                        v31 = 0;
                        if (!(1))
                            goto LABEL_10323221;
                        v35 = _ccall(10, 15, 0, 0, 0);
                        if (!((char)v35))
                        {
                            v36 = _ccall(0, 15, 0, 0, 0);
                            if ((char)v36)
                                break;
                            else
                                continue;
                        }
                        v37 = _ccall(8, 15, 0, 0, 0);
                        if ((char)v37)
                            goto LABEL_10323219;
                        goto LABEL_10323222;
                    }
                    __unsupported_jumpkind_Ijk_NoDecode()
                    v38 = _ccall(8, 15, 0, 0, 0);
                    if (!((char)v38))
                        goto LABEL_10323222;
LABEL_10323219:
                    if ((v39 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v39))
                        break;
                }
                else
                {
                    __unsupported_jumpkind_Ijk_NoDecode()
LABEL_10323221:
                    __unsupported_jumpkind_Ijk_NoDecode()
LABEL_10323222:
                    v40 = v13;
                    v41 = v12;
                    v42 = v10;
                    v43 = v9;
                    v44 = v8;
                    v15 = v14;
                    v14 = v15;
                    do
                    {
                        v45 = _ccall(15, v31, 0, 0);
                        v8 = v45 | 0x202 | v23 & 0x400 | v24 * 0x200000 & 0x200000 | v25 * 0x40000 & 0x40000;
                        v6 = v8;
                        v5 = v40;
                        v4 = v41;
                        v3 = &v8;
                        v2 = v42;
                        v1 = v43;
                        v0 = v44;
                        if (!(1))
                            goto LABEL_1032324a;
LABEL_1032324a:
                        for (; (v46 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v46 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
                        v42 = v9;
                        v43 = v8;
                        v44 = v7;
                        v47 = v15;
                        v23 = ((char)(v47 >> 10) ? 4294967295 : 1);
                        v24 = ((char)(v47 >> 21) ? 1 : 0);
                        v25 = ((char)(v47 >> 18) ? 1 : 0);
                        v48 = _INSERT((unsigned short)v12 CONCAT 0, 0, v14);
                        v49 = (int)v42[8] * 0x1000;
                        v50 = g_103a2914;
                        v51 = v49 + v50;
                        *((unsigned int *)&v42[16]) = v51;
                        v15 = v48;
                        if (v49 + v50 >= 0)
                            goto LABEL_10323286;
LABEL_10323286:
                        v52 = _ccall(3, v49, v50, 0);
                        v15 = v52 | 0x202 | v23 & 0x400 | v24 * 0x200000 & 0x200000 | v25 * 0x40000 & 0x40000;
                        v14 = v15;
                        v12 = v51;
                        v10 = &v15;
                        v9 = v42;
                        v8 = v43;
                        v7 = v44;
                        v53 = 6;
                        v40 = 0;
                        v54 = _ccall(0, 6, v51, v51, 0);
                        v31 = v51;
                        if ((char)v54)
                            break;
                        if (!(1))
                            goto LABEL_10323293;
LABEL_10323293:
                        v41 = 0;
                        v53 = 15;
                        v31 = 3;
                        v51 = 0;
                    } while (false);
                    v56 = _ccall(2, v53, v31, v51, 0);
                    if ((char)v56)
                        goto LABEL_0x103232a4;
                }
            }
        }
    }
}
```

## `sub_1032301e` `0x1032301e`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032301e(void)
{
}
```

