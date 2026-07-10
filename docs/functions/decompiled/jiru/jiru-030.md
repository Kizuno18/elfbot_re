# elfbot.dll decompiled — jiru 0x10323709..0x10323ed6

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10323709` `0x10323709`

_16 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[7];
    unsigned int field_7;
} struct_0;

int sub_10323709(void)
{
    struct_0 *v2;  // eax
    unsigned int v3;  // cc_op
    unsigned int v4;  // cc_dep1
    unsigned int v5;  // cc_dep2
    unsigned int v6;  // cc_ndep
    unsigned int v7;  // 4108
    unsigned int v0;  // [bp-0x4]

    v0 = *((int *)&(v2->padding_0)[1]);
    v7 = _ccall(12, v3, v4, v5, v6);
}
```

## `sub_10323710` `0x10323710`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323710(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323730` `0x10323730`

_356 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a2914;
extern unsigned int g_103a2934;
extern unsigned int g_103a293c;

int sub_10323730(unsigned int a0, unsigned int a1, char a2)
{
    unsigned int v16;  // ebx
    unsigned int v17;  // esi
    unsigned int v26;  // 4101
    unsigned int v27;  // esi
    unsigned int v28;  // eax
    unsigned int v29;  // cc_op
    unsigned int v30;  // cc_dep2
    unsigned int v31;  // eax
    unsigned int v33;  // eax
    unsigned int v34;  // 4152
    unsigned int v35;  // id
    unsigned int v18;  // edi
    unsigned int v36;  // ac
    unsigned int v37;  // 4110
    unsigned int v38;  // ebx
    unsigned int v39;  // esi
    unsigned int v40;  // edi
    unsigned int v41;  // 4097
    unsigned int v42;  // cc_dep1
    unsigned int v43;  // d
    unsigned int v44;  // id
    unsigned int v45;  // ac
    unsigned int v19;  // 4101
    unsigned short v46;  // ax
    unsigned short v47;  // dx
    unsigned int v48;  // eax
    unsigned int index;  // edx
    unsigned int v50;  // 4140
    unsigned int v53;  // ecx
    unsigned int v54;  // ecx
    unsigned int v55;  // ecx
    unsigned int v20;  // 4103
    unsigned int v56;  // 4110
    unsigned int v58;  // 4104
    unsigned int v59;  // cc_dep1
    unsigned int v61;  // 4101
    unsigned int v62;  // 4193
    unsigned int v63;  // 4110
    unsigned int v21;  // 4101
    unsigned int v22;  // 4101
    unsigned int v23;  // 4101
    unsigned int v24;  // 4101
    unsigned int v25;  // 4101
    unsigned int v0;  // [bp-0x68]
    unsigned int v1;  // [bp-0x64]
    char *v2;  // [bp-0x60], Other Possible Types: unsigned int
    char *v3;  // [bp-0x5c]
    char *v4;  // [bp-0x58], Other Possible Types: unsigned int
    unsigned int v5;  // [bp-0x54]
    unsigned int v6;  // [bp-0x50]
    unsigned int idx;  // [bp-0x4c]
    unsigned int v8;  // [bp-0x48]
    char v9;  // [bp-0x44]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x14]
    char v12;  // [bp-0xc]
    unsigned int v13;  // [bp-0x8]
    char v14;  // [bp-0x4]
    unsigned int v15;  // [bp+0xe]

    v11 = a0 * 0x1000 + g_103a2914;
    v13 = g_103a293c;
    v10 = g_103a293c + 0x1000;
    v8 = v11;
    idx = g_103a293c;
    v6 = v10;
    v5 = v16;
    v4 = &v9;
    v3 = &v14;
    v2 = v17;
    v1 = v18;
LABEL_10323779:
    v19 = _ccall(0, 15, 0, 0, 0);
    if ((char)v19)
        goto LABEL_1032377b;
    else
        goto LABEL_1032377c;
    while (true)
    {
LABEL_1032377b:
        __unsupported_jumpkind_Ijk_NoDecode()
        while (true)
        {
LABEL_1032377c:
            v20 = _ccall(10, 15, 0, 0, 0);
            if ((char)v20)
            {
                v21 = _ccall(8, 15, 0, 0, 0);
                if (!((char)v21))
                {
                    if (!(1))
                        goto LABEL_10323781;
                    v22 = _ccall(10, 15, 0, 0, 0);
                    if (!((char)v22))
                    {
                        v23 = _ccall(0, 15, 0, 0, 0);
                        if ((char)v23)
                            break;
                        else
                            continue;
                    }
                    v24 = _ccall(8, 15, 0, 0, 0);
                    if ((char)v24)
                        goto LABEL_10323779;
                    goto LABEL_10323782;
                }
                __unsupported_jumpkind_Ijk_NoDecode()
                v25 = _ccall(8, 15, 0, 0, 0);
                if (!((char)v25))
                    goto LABEL_10323782;
LABEL_10323779:
                if ((v26 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v26))
                    break;
            }
            else
            {
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_10323781:
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_10323782:
                v27 = v2;
                v28 = a2;
                v29 = 15;
                v30 = 0;
                v31 = v28;
                if (v31)
                {
                    idx = a0;
                    v6 = g_103a2934;
                    v31 = *((int *)(g_103a2934 + idx * 4));
                    v15 += v27;
                    v29 = 3;
                    v28 = v15;
                    v30 = v27;
                }
                else
                {
                    v33 = v31;
                    v8 = idx;
                    idx = v33;
                    v34 = _ccall(v29, v28, v30, 0);
                    v8 = v34 | 0x202 | v35 * 0x200000 & 0x200000 | v36 * 0x40000 & 0x40000;
                    v6 = idx;
                    v5 = v6;
                    v4 = v5;
                    v3 = &v8;
                    v2 = &v14;
                    v1 = v27;
                    v0 = v1;
                    while (true)
                    {
                        if (!(1))
                            goto LABEL_103237d5;
LABEL_103237d5:
                        for (; (v37 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v37 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
                        v38 = v4;
                        v39 = v1;
                        v40 = v0;
                        v41 = v8;
                        v42 = v41 & 2261;
                        v43 = ((char)(v41 >> 10) ? 4294967295 : 1);
                        v44 = ((char)(v41 >> 21) ? 1 : 0);
                        v45 = ((char)(v41 >> 18) ? 1 : 0);
                        v46 = v5;
                        v47 = v33;
                        v48 = _INSERT(v46 CONCAT 0, 0, v47);
                        index = _INSERT(v47 CONCAT 0, 0, v46);
                        v50 = _ccall(0, 0, v41 & 2261, 0, 0);
                        v54 = a2;
                        if (v54)
                            break;
                        index = a0;
                        v48 = g_103a2934;
                        v55 = *((int *)(g_103a2934 + index * 4));
                        v53 = v55 & 1;
                        v54 = v55 & 1;
                        if (!((char)v55 & 1))
                            break;
                        v8 = g_103a2934;
                        v33 = g_103a2934;
                        if (v53 >= 0)
                            goto LABEL_10323825;
LABEL_10323825:
                        v56 = _ccall(15, v53, 0, 0);
                        v8 = v56 | 0x202 | v43 & 0x400 | v44 * 0x200000 & 0x200000 | v45 * 0x40000 & 0x40000;
                        idx = g_103a2934;
                        v6 = v54;
                        v5 = index;
                        v4 = v38;
                        v3 = &v8;
                        v2 = &v14;
                        v1 = v39;
                        v0 = v40;
                        v58 = _ccall(0, 6, index, index, 0);
                        v59 = index;
                        if (!((char)v58))
                        {
                            if (!(1))
                                goto LABEL_10323832;
LABEL_10323832:
                            v61 = _ccall(2, 15, 3, 0, 0);
                            if ((char)v61)
                                goto LABEL_0x10323843;
                        }
                        else
                        {
                            v61 = _ccall(2, 6, v59, index, 0);
                            if ((char)v61)
                                goto LABEL_0x10323843;
                        }
                    }
                    v8 = v54;
                    idx = v48;
                    v62 = _ccall(15, v53, 0, 0);
                    v8 = v62 | 0x202 | v43 & 0x400 | v44 * 0x200000 & 0x200000 | v45 * 0x40000 & 0x40000;
                    v6 = v54;
                    v5 = index;
                    v4 = v38;
                    v3 = &v8;
                    v2 = &v14;
                    v1 = v39;
                    v0 = v40;
                    if (!(1))
                        goto LABEL_1032388f;
LABEL_1032388f:
                    for (; (v63 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v63 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
                    v6 = 0x1000;
                    return sub_103238bf(4, &v12);
                }
            }
        }
    }
}
```

## `sub_1032376f` `0x1032376f`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1032376f(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103237a2` `0x103237a2`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103237a2(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103237d0` `0x103237d0`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103237d0(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103237d7` `0x103237d7`

_3 bytes. (leaf/helper — see body)_

```c
void sub_103237d7(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323800` `0x10323800`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323800(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032383c` `0x1032383c`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1032383c(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323850` `0x10323850`

_21 bytes. (leaf/helper — see body)_

```c
int sub_10323850(void)
{
}
```

## `sub_10323854` `0x10323854`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10323854(void)
{
}
```

## `sub_10323856` `0x10323856`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323856(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032388a` `0x1032388a`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1032388a(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323891` `0x10323891`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10323891(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103238bf` `0x103238bf`

_106 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b0c4;
extern struct_0 *g_1038c8ac;

int sub_103238bf(void)
{
    unsigned int v13;  // eax
    unsigned int v14;  // ecx
    unsigned int v23;  // ecx
    unsigned int v24;  // edx
    unsigned int v25;  // ebx
    unsigned int v26;  // esi
    unsigned int v27;  // edi
    unsigned int v15;  // 4193
    unsigned int v16;  // id
    unsigned int v17;  // ac
    unsigned int v18;  // edx
    unsigned int v19;  // ebx
    unsigned int v20;  // esi
    unsigned int v21;  // edi
    unsigned int v22;  // 4110
    unsigned int v0;  // [bp-0x2c]
    unsigned int v1;  // [bp-0x28]
    unsigned int v2;  // [bp-0x24]
    char *v3;  // [bp-0x20], Other Possible Types: unsigned int
    char *v4;  // [bp-0x1c], Other Possible Types: unsigned int
    unsigned int v5;  // [bp-0x18]
    unsigned int v6;  // [bp-0x14]
    unsigned int v7;  // [bp-0x10]
    unsigned int v8;  // [bp-0xc]
    unsigned int v9;  // [bp-0x8]
    unsigned int v11;  // [bp+0xffff4]

    v9 = g_1038c8ac->field_0;
    v13 = g_1038b0c4(g_1038c8ac->field_0, v11);
    if (v13)
    {
        v8 = v13;
        v7 = v23;
        v6 = v24;
        v5 = v25;
        v4 = &v9;
        v3 = /* unsupported instruction */;
        v2 = v26;
        v1 = v27;
    }
    v8 = v14;
    v7 = 0;
    v15 = _ccall(15, v13, 0, 0);
    v8 = v15 | 0x202 | v16 * 0x200000 & 0x200000 | v17 * 0x40000 & 0x40000;
    v6 = v8;
    v5 = v18;
    v4 = v19;
    v3 = &v8;
    v1 = v20;
    v0 = v21;
    if (!(1))
        goto LABEL_103238fd;
LABEL_103238fd:
    for (; (v22 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v22 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
}
```

## `sub_103238f8` `0x103238f8`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103238f8(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103238ff` `0x103238ff`

_3 bytes. (leaf/helper — see body)_

```c
void sub_103238ff(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032392d` `0x1032392d`

_53 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a293c;

void sub_1032392d(char a0, unsigned int a1, char a2, void* a2, unsigned int a3, unsigned int a4, unsigned int a5)
{
    unsigned int v3;  // 4101
    unsigned int v4;  // 4101
    unsigned int v5;  // 4101
    unsigned int v6;  // 4101
    unsigned int v7;  // 4103
    unsigned int v8;  // 4101
    unsigned int v9;  // 4101
    unsigned int v1;  // [bp+0x18]
    void* v2;  // [bp+0x1c]

    do
    {
        if (true)
        {
            v3 = _ccall(10, 15, 0, 0, 0);
            if (!((char)v3))
            {
LABEL_10323937:
                v4 = _ccall(0, 15, 0, 0, 0);
                if (!((char)v4))
                    goto LABEL_10323948;
            }
            else
            {
                v5 = _ccall(8, 15, 0, 0, 0);
                if (!((char)v5))
                    goto LABEL_1032394e;
                if (!(1))
                    goto LABEL_10323947;
                goto LABEL_10323937;
            }
LABEL_10323947:
            __unsupported_jumpkind_Ijk_NoDecode()
LABEL_10323948:
            v7 = _ccall(10, 15, 0, 0, 0);
            if (!((char)v7))
            {
                __unsupported_jumpkind_Ijk_NoDecode()
                goto LABEL_1032394d;
            }
        }
        else
        {
LABEL_1032394d:
            __unsupported_jumpkind_Ijk_NoDecode()
            goto LABEL_1032394d;
        }
    } while ((v8 = (unsigned int)_ccall(8, 15, 0, 0, 0), !((char)v8)));
    __unsupported_jumpkind_Ijk_NoDecode()
    v9 = _ccall(8, 15, 0, 0, 0);
    if (!((char)v9))
        goto LABEL_1032394e;
LABEL_10323937:
    v6 = _ccall(0, 15, 0, 0, 0);
    if (!((char)v6))
        goto LABEL_10323948;
    goto LABEL_10323947;
LABEL_1032394e:
    v2 = a2 - 12;
    v1 = 0x1000;
    a5 = g_103a293c;
    a4 = (int)a2[16];
}
```

## `sub_1032393b` `0x1032393b`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1032393b(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323968` `0x10323968`

_632 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[51];
    char field_33;
} struct_1;

typedef struct struct_2 {
    char padding_0[361433165];
    unsigned int field_158b084d;
    char padding_158b0851[939427771];
    char field_4d89900c;
} struct_2;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern char g_0;
extern struct_0 *g_1038b0c0;
extern char g_103a2908;
extern char g_103a2909;
extern void* g_103a290c;
extern unsigned int g_103a2934;

int sub_10323968(void)
{
    unsigned int *v17;  // eax
    int v18;  // eax
    unsigned int v27;  // edi
    unsigned int v28;  // cc_op
    unsigned int v29;  // 4104
    unsigned int v30;  // cc_dep1
    unsigned int v31;  // cc_dep2
    unsigned int v33;  // 4101
    unsigned int v34;  // 4101
    unsigned int i;  // edx
    unsigned int v36;  // ecx
    int v19;  // cc_dep1
    unsigned int v37;  // ebx
    unsigned int v38;  // esi
    unsigned int v39;  // edi
    unsigned int v40;  // 4101
    unsigned int v41;  // 4103
    unsigned int v42;  // 4101
    unsigned int v43;  // 4101
    unsigned int v44;  // 4101
    unsigned int v45;  // 4101
    unsigned int v46;  // 4101
    unsigned int v20;  // 4108
    unsigned int v47;  // 4101
    unsigned int v48;  // ebx
    unsigned int v49;  // esi
    unsigned int v50;  // edi
    unsigned int v51;  // 4101
    unsigned int v52;  // 4103
    unsigned int v53;  // 4101
    unsigned int v54;  // 4101
    unsigned int v55;  // 4101
    unsigned int v56;  // 4101
    unsigned int v21;  // id
    unsigned int v57;  // 4101
    unsigned int v58;  // 4101
    void* idx;  // ebp
    struct_1 *idx1;  // eax
    unsigned int v61;  // cc_op
    unsigned int v62;  // cc_dep1
    unsigned int v63;  // 4101
    struct_2 *index;  // ebx
    unsigned int v22;  // ac
    struct_1 *idx2;  // ecx
    unsigned int v23;  // ecx
    unsigned int v76;  // esi
    unsigned int v77;  // edi
    unsigned int v78;  // 4101
    unsigned int v79;  // 4103
    unsigned int v80;  // 4101
    unsigned int v81;  // 4101
    unsigned int v82;  // 4101
    unsigned int v83;  // 4101
    unsigned int v84;  // 4101
    unsigned int v85;  // 4101
    unsigned int v24;  // edx
    struct_1 *v86;  // ecx
    char v87;  // al
    unsigned int v25;  // ebx
    unsigned int v26;  // esi
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x20]
    char *v3;  // [bp-0x1c], Other Possible Types: void*, unsigned int
    char *v4;  // [bp-0x18], Other Possible Types: unsigned int
    struct_2 *v5;  // [bp-0x14], Other Possible Types: unsigned int
    unsigned int v6;  // [bp-0x10]
    struct_1 *v7;  // [bp-0xc], Other Possible Types: unsigned int
    int v8;  // [bp-0x8], Other Possible Types: unsigned int
    int <0x10323968[is_2]|Stack bp-0x8, 1 B>;  // [bp-0x8]
    unsigned int v9;  // [bp-0x4]
    unsigned int v11;  // [bp+0xffff1]
    unsigned int v12;  // [bp+0xffffd]
    unsigned int v15;  // [bp+0x10000c]
    char v16;  // [bp+0x100014]

    v9 = *(v17);
    /* unsupported instruction */ = &<0x10323968[is_2]|Stack bp-0x8, 1 B>;
    v18 = g_1038b0c0(*(v17));
    v19 = v18;
    if (!v18)
    {
        v8 = 0;
        if (v19 >= 0)
            goto LABEL_1032397d;
LABEL_1032397d:
        v20 = _ccall(15, v19, 0, 0);
        v8 = v20 | 0x202 | v21 * 0x200000 & 0x200000 | v22 * 0x40000 & 0x40000;
        v7 = 0;
        v6 = v23;
        v5 = v24;
        v4 = v25;
        v3 = &v8;
        v1 = v26;
        v0 = v27;
        v28 = 6;
        v29 = _ccall(0, 6, v24, v24, 0);
        v30 = v24;
        if (!((char)v29))
        {
            if (!(1))
                goto LABEL_1032398a;
LABEL_1032398a:
            v28 = 15;
            v30 = 3;
            v31 = 0;
            if (0)
                goto LABEL_0x10323922;
            else
                goto LABEL_10323992;
        }
LABEL_10323992:
        v33 = _ccall(2, v28, v30, v31, 0);
        if ((char)v33)
            goto LABEL_0x1032399b;
    }
    else
    {
        v34 = _ccall(0, 15, v19, 0, 0);
        if (i)
        {
            v8 = v18;
            v7 = v36;
            v6 = i;
            v5 = v37;
            v4 = &v9;
            v3 = /* unsupported instruction */;
            v2 = v38;
            v1 = v39;
LABEL_103239f3:
            v40 = _ccall(0, 15, 0, 0, 0);
            if ((char)v40)
                goto LABEL_103239f5;
            else
                goto LABEL_103239f6;
            while (true)
            {
LABEL_103239f5:
                __unsupported_jumpkind_Ijk_NoDecode()
                while (true)
                {
LABEL_103239f6:
                    v41 = _ccall(10, 15, 0, 0, 0);
                    if (!((char)v41))
                    {
                        __unsupported_jumpkind_Ijk_NoDecode()
LABEL_103239fb:
                        __unsupported_jumpkind_Ijk_NoDecode()
LABEL_103239fc:
                    }
                    v42 = _ccall(8, 15, 0, 0, 0);
                    if (!((char)v42))
                    {
                        if (!(1))
                            goto LABEL_103239fb;
                        v43 = _ccall(10, 15, 0, 0, 0);
                        if (!((char)v43))
                        {
                            v44 = _ccall(0, 15, 0, 0, 0);
                            if ((char)v44)
                                break;
                            else
                                continue;
                        }
                        v45 = _ccall(8, 15, 0, 0, 0);
                        if ((char)v45)
                            goto LABEL_103239f3;
                        goto LABEL_103239fc;
                    }
                    __unsupported_jumpkind_Ijk_NoDecode()
                    v46 = _ccall(8, 15, 0, 0, 0);
                    if (!((char)v46))
                        goto LABEL_103239fc;
LABEL_103239f3:
                    if ((v47 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v47))
                        break;
                }
            }
        }
        else if (!((char)*((int *)(g_103a2934 + v15 * 4)) & 2))
        {
            v8 = g_103a2934;
            v7 = *((int *)(g_103a2934 + v15 * 4)) & 2;
            v6 = v15;
            v5 = v48;
            v4 = &v9;
            v3 = /* unsupported instruction */;
            v2 = v49;
            v1 = v50;
LABEL_10323c6d:
            v51 = _ccall(0, 15, 0, 0, 0);
            if ((char)v51)
                goto LABEL_10323c6f;
            else
                goto LABEL_10323c70;
            while (true)
            {
LABEL_10323c6f:
                __unsupported_jumpkind_Ijk_NoDecode()
                while (true)
                {
LABEL_10323c70:
                    v52 = _ccall(10, 15, 0, 0, 0);
                    if (!((char)v52))
                    {
                        __unsupported_jumpkind_Ijk_NoDecode()
LABEL_10323c75:
                        __unsupported_jumpkind_Ijk_NoDecode()
LABEL_10323c76:
                    }
                    v53 = _ccall(8, 15, 0, 0, 0);
                    if (!((char)v53))
                    {
                        if (!(1))
                            goto LABEL_10323c75;
                        v54 = _ccall(10, 15, 0, 0, 0);
                        if (!((char)v54))
                        {
                            v55 = _ccall(0, 15, 0, 0, 0);
                            if ((char)v55)
                                break;
                            else
                                continue;
                        }
                        v56 = _ccall(8, 15, 0, 0, 0);
                        if ((char)v56)
                            goto LABEL_10323c6d;
                        goto LABEL_10323c76;
                    }
                    __unsupported_jumpkind_Ijk_NoDecode()
                    v57 = _ccall(8, 15, 0, 0, 0);
                    if (!((char)v57))
                        goto LABEL_10323c76;
LABEL_10323c6d:
                    if ((v58 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v58))
                        break;
                }
            }
        }
        else if (g_103a2908)
        {
            g_103a2908 = 0;
            if (g_103a2909)
            {
                __unsupported_jumpkind_Ijk_NoDecode()
                idx = /* unsupported instruction */ + 1;
                v11 = g_103a2934 | 0x100;
            }
            else
            {
                v11 = v12;
            }
            sub_103240bc(0x1000, idx - 12);
            return;
        }
        else
        {
            for (i = v16; (int)idx[4] < (int)idx[24]; *((unsigned int *)&idx[4]) = (int)idx[4] + 4)
            {
                *((int *)(int)idx[4]) = *((int *)(int)idx[4]) ^ (int)idx[44];
            }
            idx1 = (int)idx[8];
            v61 = 6;
            v62 = *((int *)((char *)g_103a290c + 0x4 * idx1));
            if (*((int *)((char *)g_103a290c + 0x4 * idx1)))
            {
                v63 = _ccall(0, 6, v62, 0, 0);
            }
            else
            {
                idx2 = (int)idx[8];
                if (!((char)*((int *)(g_103a2934 + idx2 * 4)) & 4))
                {
                    v8 = *((int *)(g_103a2934 + idx2 * 4)) & 4;
                    v7 = idx2;
                    v6 = g_103a2934;
                    v5 = index;
                    v4 = &v9;
                    v3 = idx;
                    v2 = v76;
                    v1 = v77;
LABEL_10323fd7:
                    v78 = _ccall(0, 15, 0, 0, 0);
                    if ((char)v78)
                        goto LABEL_10323fd9;
                    else
                        goto LABEL_10323fda;
                    while (true)
                    {
LABEL_10323fd9:
                        __unsupported_jumpkind_Ijk_NoDecode()
                        while (true)
                        {
LABEL_10323fda:
                            v79 = _ccall(10, 15, 0, 0, 0);
                            if ((char)v79)
                            {
                                v80 = _ccall(8, 15, 0, 0, 0);
                                if (!((char)v80))
                                {
                                    if (!(1))
                                        goto LABEL_10323fdf;
                                    v81 = _ccall(10, 15, 0, 0, 0);
                                    if (!((char)v81))
                                    {
                                        v82 = _ccall(0, 15, 0, 0, 0);
                                        if ((char)v82)
                                            break;
                                        else
                                            continue;
                                    }
                                    else
                                    {
                                        v83 = _ccall(8, 15, 0, 0, 0);
                                        if ((char)v83)
                                            goto LABEL_10323fd7;
                                        else
                                            goto LABEL_0x10323fe0;
                                    }
                                }
                                else
                                {
                                    __unsupported_jumpkind_Ijk_NoDecode()
                                    v84 = _ccall(8, 15, 0, 0, 0);
                                    if ((char)v84)
                                        goto LABEL_10323fd7;
                                    else
                                        goto LABEL_0x10323fe0;
                                }
LABEL_10323fd7:
                                if ((v85 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v85))
                                    break;
                            }
                            else
                            {
                                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_10323fdf:
                                while (true)
                                ;
                            }
                        }
                    }
                }
                else
                {
                    v86 = (int)idx[8];
                    v87 = *((int *)(g_103a2934 + v86 * 4));
                    *((struct_1 **)&(index->padding_0)[1]) = &v86->padding_0[*((int *)&(index->padding_0)[1])];
                    *((unsigned int *)(g_103a2934 + v86 * 4)) = v87 ^ 41;
                    if (!g_103a2909)
                    {
                        *((unsigned int *)&idx[20]) = 64;
                        sub_103240bc(0x1000, idx - 12);
                        return;
                    }
                    *((unsigned int *)&idx[20]) = (int)idx[8] & 4294967039;
                    sub_103240bc(0x1000, idx - 12);
                    return;
                }
            }
        }
    }
}
```

## `sub_10323994` `0x10323994`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323994(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103239a8` `0x103239a8`

_21 bytes. (leaf/helper — see body)_

```c
int sub_103239a8(void)
{
}
```

## `sub_103239ac` `0x103239ac`

_2 bytes. (leaf/helper — see body)_

```c
void sub_103239ac(void)
{
}
```

## `sub_103239ae` `0x103239ae`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103239ae(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103239c6` `0x103239c6`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103239c6(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103239e9` `0x103239e9`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103239e9(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323a00` `0x10323a00`

_122 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c808;
extern unsigned int g_1038c834;
extern char g_103a290a;
extern unsigned int g_103a2934;
extern unsigned int g_103a2938;
extern int g_103a293c;

int sub_10323a00(void)
{
    unsigned int v10;  // eax
    unsigned int v11;  // eax
    unsigned int v20;  // 4123
    unsigned int v21;  // 4110
    unsigned int v22;  // id
    unsigned int v23;  // ac
    unsigned int v24;  // ebx
    unsigned int v25;  // esi
    unsigned int v26;  // edi
    unsigned int v28;  // 4104
    unsigned int v29;  // cc_dep1
    unsigned int v12;  // cc_op
    unsigned int v31;  // 4101
    unsigned int v13;  // cc_dep1
    unsigned int v14;  // cc_dep2
    unsigned int v15;  // eax
    unsigned int idx;  // ecx
    unsigned int index;  // edx
    unsigned int v18;  // eax
    unsigned int v19;  // eax
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    char *v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    unsigned int v7;  // [bp-0x4]
    unsigned int v9;  // [bp+0x10000c]

    v11 = v10 ^ g_1038c834 ^ g_1038c808;
    v12 = 15;
    v13 = v11 & 8;
    v14 = 0;
    v15 = v11 & 8;
    if (((char)v11 & 8))
    {
        idx = v9;
        index = g_103a2934;
        v18 = *((int *)(g_103a2934 + idx * 4));
        v12 = 15;
        v13 = v18 & 4;
        v14 = 0;
        v15 = v18 & 4;
        if (((char)v18 & 4))
        {
            v13 = sub_102ec930(g_103a293c, 0x1000, 4294967295);
            index = v9;
            idx = g_103a2938;
            v12 = 6;
            v14 = *((int *)(g_103a2938 + index * 4));
            v15 = v13;
            if (v15 != *((int *)(g_103a2938 + index * 4)))
            {
                g_103a290a = 1;
                v15 = v13;
            }
        }
    }
    v19 = v15;
    v7 = v19;
    v20 = _ccall(2, v12, v13, v14, 0);
    if (!((char)v20))
        goto LABEL_10323a57;
LABEL_10323a57:
    v21 = _ccall(v12, v13, v14, 0);
    v7 = v21 | 0x202 | v22 * 0x200000 & 0x200000 | v23 * 0x40000 & 0x40000;
    v6 = v19;
    v5 = idx;
    v4 = index;
    v3 = v24;
    v2 = &v7;
    v1 = v25;
    v0 = v26;
    v28 = _ccall(0, 6, index, index, 0);
    v29 = index;
    if (!((char)v28))
    {
        if (!(1))
            goto LABEL_10323a64;
LABEL_10323a64:
        if (0)
            goto LABEL_0x103239fc;
        v31 = _ccall(2, 15, 3, 0, 0);
        if ((char)v31)
            goto LABEL_0x10323a75;
    }
    else
    {
        v31 = _ccall(2, 6, v29, index, 0);
        if ((char)v31)
            goto LABEL_0x10323a75;
    }
}
```

## `sub_10323a6e` `0x10323a6e`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323a6e(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323a82` `0x10323a82`

_117 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    struct struct_1 *field_c;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern int g_103a2970;

int sub_10323a82(void)
{
    struct_0 *idx;  // ebp
    unsigned int v8;  // 4097
    unsigned int v9;  // eax
    unsigned int *v10;  // edx
    unsigned int v11;  // 4098
    unsigned int v12;  // eax
    unsigned int *v13;  // ecx
    unsigned int v14;  // 4207
    unsigned int v15;  // 4110
    struct_0 *v1;  // [bp+0x8]
    char *v2;  // [bp+0xc]
    unsigned int *v3;  // [bp+0x14]
    unsigned int *v4;  // [bp+0x18]
    unsigned int v5;  // [bp+0x1c]
    unsigned int *v6;  // [bp+0x20], Other Possible Types: unsigned int

    idx = v1;
    v8 = v6;
    v9 = sub_102eb870(&g_103a2970);
    v10 = &idx->field_c->field_0;
    v11 = *(v10);
    v12 = v9 ^ *(v10);
    v13 = &idx->field_c->field_0;
    *(v13) = v12;
    v6 = v13;
    v5 = v12;
    v14 = _ccall(15, v9 ^ v11, 0, 0);
    v6 = v14 | 0x202 | ((char)(v8 >> 10) ? 4294967295 : 1) & 0x400 | ((char)(v8 >> 21) ? 1 : 0) * 0x200000 & 0x200000 | ((char)(v8 >> 18) ? 1 : 0) * 0x40000 & 0x40000;
    v4 = v6;
    v3 = v10;
    v2 = &v6;
    v1 = idx;
    if (!(1))
        goto LABEL_10323ace;
LABEL_10323ace:
    for (; (v15 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v15 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
    sub_10323afe(); /* do not return */
}
```

## `sub_10323a86` `0x10323a86`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10323a86(void)
{
}
```

## `sub_10323a88` `0x10323a88`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323a88(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323ac9` `0x10323ac9`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323ac9(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323ad0` `0x10323ad0`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10323ad0(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323afe` `0x10323afe`

_213 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e4;
extern unsigned int g_1038c818;
extern unsigned int g_1038c848;
extern char g_1038c85c;
extern char g_103a2909;
extern unsigned int g_103a2934;

int sub_10323afe(void)
{
    unsigned int v14;  // eax
    unsigned int v24;  // 4138
    unsigned long v25;  // 4139
    unsigned int v26;  // ebx
    unsigned int v27;  // esi
    unsigned int v28;  // 4110
    void* v29;  // eax
    char *v30;  // edi
    unsigned int *v17;  // cc_dep1
    unsigned int *v18;  // cc_dep2
    unsigned int v19;  // 4101
    unsigned int v20;  // edx
    unsigned int v21;  // edx
    unsigned int index;  // eax
    void* v23;  // ecx
    unsigned int v0;  // [bp-0x20]
    char *v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    void* v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    unsigned int v6;  // [bp-0x4]
    unsigned int v8;  // [bp+0xfffe8]
    unsigned int *v9;  // [bp+0xfffec]
    unsigned int v10;  // [bp+0xffff0]
    unsigned int v11;  // [bp+0xffffc]
    unsigned int *v12;  // [bp+0x100000]
    unsigned int idx;  // [bp+0x10000c]

    v8 = &(&g_1038c85c)[v14 ^ g_1038c818 ^ g_1038c7e4 ^ g_1038c848];
    while (true)
    {
        v17 = v12;
        v18 = v9;
        if (v12 >= v9)
            break;
        *(v12) = *(v12) ^ v8;
        v12 += 1;
    }
    v19 = _ccall(0, 6, v17, v18, 0);
    v20 = *((int *)(g_103a2934 + idx * 4));
    v21 = *((int *)(g_103a2934 + idx * 4)) & 4294967294;
    index = idx;
    *((unsigned int *)(g_103a2934 + index * 4)) = v21;
    v6 = g_103a2934;
    v5 = index;
    v23 = ~(g_103a2934 * 0x1000000 | g_103a2934 * 0x100 & 0xff0000 | g_103a2934 >> 8 & 0xff00 | g_103a2934 >> 24 & 0xff);
    v24 = _ccall(15, v20 & 4294967294, 0, 0);
    v25 = _ccall((int)v23[100], 1, v24, 4);
    *((unsigned int *)&v23[100]) = v25;
    v4 = v23;
    v3 = v21;
    v2 = v26;
    v1 = &v6;
    v0 = v27;
    if (!(1))
        goto LABEL_10323b91;
LABEL_10323b91:
    for (; (v28 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v28 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
    v29 = _INSERT((unsigned short)v3 CONCAT 0, 0, v5);
    if (!g_103a2909)
    {
        __unsupported_jumpkind_Ijk_NoDecode()
        *((char *)&v29[9]) = (char)v29[9];
        *(v30) = *(v30) >> 1 | *(v30) * 128;
    }
    v10 = v11 | 0x100;
}
```

## `sub_10323b1f` `0x10323b1f`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323b1f(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323b4a` `0x10323b4a`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323b4a(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323b8c` `0x10323b8c`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323b8c(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323b93` `0x10323b93`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10323b93(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323bdd` `0x10323bdd`

_33 bytes. (leaf/helper — see body)_

```c
void sub_10323bdd(unsigned int a0, unsigned int a1)
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
            goto LABEL_10323bea;
LABEL_10323bea:
        v20 = 15;
        v22 = 3;
        a1 = 0;
        if (0)
            goto LABEL_0x10323b82;
        else
            goto LABEL_10323bf2;
    }
LABEL_10323bf2:
    v24 = _ccall(2, v20, v22, a1, 0);
    if ((char)v24)
        goto LABEL_0x10323bfb;
    else
        goto LABEL_0x10323bf5;
}
```

## `sub_10323bf4` `0x10323bf4`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10323bf4(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323bf8` `0x10323bf8`

_1 bytes. (leaf/helper — see body)_

```c
int sub_10323bf8(void)
{
    x86g_dirtyhelper_OUT(Conv(16I->32I, vvar_1{r16|2b}), vvar_0{r8|4b}, 0x4<32>)
}
```

## `sub_10323c08` `0x10323c08`

_50 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    struct struct_1 *field_c;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern char g_103a290a;
extern int g_103a2970;

int sub_10323c08(void)
{
    unsigned int v2;  // eax
    struct_0 *idx;  // [bp+0x8]

    if (g_103a290a)
    {
        v2 = sub_102eb870(&g_103a2970);
        idx->field_c->field_0 = v2 ^ idx->field_c->field_0;
    }
}
```

## `sub_10323c0c` `0x10323c0c`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10323c0c(void)
{
}
```

## `sub_10323c0e` `0x10323c0e`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323c0e(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323c63` `0x10323c63`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323c63(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323c8d` `0x10323c8d`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323c8d(void)
{
}
```

## `sub_10323c8f` `0x10323c8f`

_99 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
} struct_0;

extern struct_0 *g_103a293c;

void sub_10323c8f(void)
{
    char *v13;  // eax
    char *v14;  // ecx
    unsigned int v23;  // 4104
    char *v24;  // cc_dep1
    unsigned int v26;  // 4101
    char *v15;  // edx
    unsigned int v16;  // 4110
    unsigned int v17;  // id
    unsigned int v18;  // ac
    unsigned int v19;  // ebx
    unsigned int v20;  // esi
    unsigned int v21;  // edi
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    char *v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    char *v4;  // [bp-0x10]
    char *v5;  // [bp-0xc]
    char *v6;  // [bp-0x8]
    char *v7;  // [bp-0x4]
    unsigned int v8;  // [bp-0x4]
    char v10;  // [bp+0xfffdf]
    char *v11;  // [bp+0xfffe0]
    char *v12;  // [bp+0xfffe4]

    v13 = &g_103a293c->field_0;
    v12 = &g_103a293c->field_0;
    v14 = v12 + 0x1000;
    v11 = v14;
    while (true)
    {
        v15 = v12;
        if (v15 >= v11)
            break;
        v13 = v12;
        *(v13) = *(v12) ^ v10;
        v14 = v12 + 1;
        v12 = v14;
    }
    v7 = v13;
    if (v15 >= v11)
        goto LABEL_10323ccf;
LABEL_10323ccf:
    v16 = _ccall(6, v15, v11, 0);
    v8 = v16 | 0x202 | v17 * 0x200000 & 0x200000 | v18 * 0x40000 & 0x40000;
    v6 = v7;
    v5 = v14;
    v4 = v15;
    v3 = v19;
    v2 = &v8;
    v1 = v20;
    v0 = v21;
    v23 = _ccall(0, 6, v15, v15, 0);
    v24 = v15;
    if (!((char)v23))
    {
        if (!(1))
            goto LABEL_10323cdc;
LABEL_10323cdc:
        if (0)
            goto LABEL_0x10323c74;
        v26 = _ccall(2, 15, 0x3, NULL, 0);
        if ((char)v26)
            goto LABEL_0x10323ced;
    }
    else
    {
        v26 = _ccall(2, 6, v24, v15, 0);
        if ((char)v26)
            goto LABEL_0x10323ced;
    }
}
```

## `sub_10323ce6` `0x10323ce6`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323ce6(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323cfa` `0x10323cfa`

_111 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
} struct_0;

extern unsigned int g_103a2934;

int sub_10323cfa(void)
{
    struct_0 *idx;  // ebp
    unsigned int v8;  // 4097
    unsigned int v9;  // ecx
    unsigned int v10;  // ecx
    unsigned int index;  // edx
    unsigned int v12;  // 4292
    unsigned int v13;  // 4110
    struct_0 *v1;  // [bp+0x8]
    char *v2;  // [bp+0xc]
    unsigned int v3;  // [bp+0x14]
    unsigned int v4;  // [bp+0x18]
    unsigned int v5;  // [bp+0x1c]
    unsigned int v6;  // [bp+0x20]

    idx = v1;
    v8 = v6;
    v9 = *((int *)(g_103a2934 + idx->field_8 * 4));
    v10 = v9 | 2;
    index = idx->field_8;
    *((unsigned int *)(g_103a2934 + index * 4)) = v10;
    v6 = v10;
    v5 = g_103a2934;
    v12 = _ccall(15, v9 | 2, 0, 0);
    v6 = v12 | 0x202 | ((char)(v8 >> 10) ? 4294967295 : 1) & 0x400 | ((char)(v8 >> 21) ? 1 : 0) * 0x200000 & 0x200000 | ((char)(v8 >> 18) ? 1 : 0) * 0x40000 & 0x40000;
    v4 = v6;
    v3 = index;
    v2 = &v6;
    v1 = idx;
    if (!(1))
        goto LABEL_10323d4b;
LABEL_10323d4b:
    for (; (v13 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v13 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
}
```

## `sub_10323cfe` `0x10323cfe`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10323cfe(void)
{
}
```

## `sub_10323d00` `0x10323d00`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323d00(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323d46` `0x10323d46`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323d46(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323d4d` `0x10323d4d`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10323d4d(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323e04` `0x10323e04`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323e04(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323e29` `0x10323e29`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323e29(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323e51` `0x10323e51`

_22 bytes. (leaf/helper — see body)_

```c
int sub_10323e51(void* a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int a10, unsigned int a11, unsigned int a12, unsigned int a13, unsigned int a14, unsigned int a15, unsigned int a16, unsigned int a17, unsigned int a18, unsigned int a19, unsigned int a20, unsigned int a21, unsigned int a22, unsigned int a23, unsigned int a24, unsigned int a25, unsigned int a26, unsigned int a27, unsigned int a28)
{
    unsigned int *v1;  // esi
    unsigned int v2;  // eax
    unsigned int v3;  // 4138
    unsigned long v4;  // 4139
    unsigned int v5;  // ebx
    unsigned int v6;  // d
    unsigned int v7;  // edi
    char v0;  // [bp+0x0]

    /* unsupported instruction */ = a28 * 3235821969;
    v2 = *(v1);
    v3 = _ccall(39, a28, 3235821969, 0);
    v4 = _ccall((int)a0[100], 1, v3, 4);
    *((unsigned int *)&a0[100]) = v4;
    *((unsigned int *)(/* unsupported instruction */ - 4)) = v2;
    *((void* *)(/* unsupported instruction */ - 8)) = a0;
    *((unsigned int *)(/* unsupported instruction */ - 12)) = a1;
    *((unsigned int *)(/* unsupported instruction */ - 16)) = v5;
    *((int *)(/* unsupported instruction */ - 20)) = /* unsupported instruction */;
    *((char **)(/* unsupported instruction */ - 24)) = &v0;
    *((unsigned int **)(/* unsupported instruction */ - 28)) = &v1[v6];
    *((unsigned int *)(/* unsupported instruction */ - 32)) = v7;
    if (1)
        goto LABEL_0x10323e6a;
    else
        goto LABEL_0x10323e67;
}
```

## `sub_10323e69` `0x10323e69`

_107 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

int sub_10323e69(unsigned int a0, void* a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7)
{
    unsigned int v2;  // 4110
    unsigned int v3;  // edx
    unsigned int v12;  // 4101
    unsigned int v13;  // 4101
    struct_0 *v4;  // eax
    unsigned int v5;  // ecx
    unsigned int v6;  // 4101
    unsigned int v7;  // 4103
    unsigned int v8;  // 4101
    unsigned int v9;  // 4101
    unsigned int v10;  // 4101
    unsigned int v11;  // 4101
    unsigned int v0;  // [bp+0x0]
    char v1;  // [bp+0x24]

    __unsupported_jumpkind_Ijk_NoDecode()
    if (!(1))
        goto LABEL_10323e6e;
LABEL_10323e6e:
    for (; (v2 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v2 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
    v3 = (int)a1[8] * 0x1000;
    v4 = (int)a1[48];
    v5 = v4->field_4 - v3;
    *((unsigned int *)&a1[56]) = v5;
    a7 = v4;
    a6 = v5;
    a5 = v3;
    a4 = a3;
    a3 = &v1;
    a2 = a1;
    a1 = a0;
    a0 = v0;
    v6 = _ccall(0, 15, 0, 0, 0);
    if ((char)v6)
        goto LABEL_10323ec8;
    else
        goto LABEL_10323ec9;
    while (true)
    {
LABEL_10323ec8:
        __unsupported_jumpkind_Ijk_NoDecode()
        while (true)
        {
LABEL_10323ec9:
            v7 = _ccall(10, 15, 0, 0, 0);
            if (!((char)v7))
            {
                __unsupported_jumpkind_Ijk_NoDecode()
                __unsupported_jumpkind_Ijk_NoDecode()
                return sub_10323ed6();
            }
            v8 = _ccall(8, 15, 0, 0, 0);
            if (!((char)v8))
            {
                if (false)
                {
                    __unsupported_jumpkind_Ijk_NoDecode()
                    return sub_10323ed6();
                }
                v9 = _ccall(10, 15, 0, 0, 0);
                if (!((char)v9))
                {
                    v10 = _ccall(0, 15, 0, 0, 0);
                    if ((char)v10)
                        break;
                    else
                        continue;
                }
                else
                {
                    v11 = _ccall(8, 15, 0, 0, 0);
                    if (!((char)v11))
                        return sub_10323ed6();
                }
            }
            else
            {
                __unsupported_jumpkind_Ijk_NoDecode()
                v12 = _ccall(8, 15, 0, 0, 0);
                if (!((char)v12))
                    return sub_10323ed6();
            }
            if ((v13 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v13))
                break;
        }
    }
}
```

## `sub_10323e70` `0x10323e70`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10323e70(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323ebc` `0x10323ebc`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323ebc(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323ed6` `0x10323ed6`

_67 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a293c;

void sub_10323ed6(void)
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
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    char *v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    unsigned int v7;  // [bp-0x4]
    char v9;  // [bp+0xc]
    unsigned int v10;  // [bp+0xfffcc]
    int *v11;  // [bp+0xfffd4]

    v5 = g_103a293c + v10;
    v7 = sub_10350b50(g_103a293c + v10, *(v11), v12);
    if (&v9 >= NULL)
        goto LABEL_10323ef6;
LABEL_10323ef6:
    v13 = _ccall(3, &v5, 12, 0);
    v7 = v13 | 0x202 | v14 * 0x200000 & 0x200000 | v15 * 0x40000 & 0x40000;
    v6 = sub_10350b50(g_103a293c + v10, *(v11), v12);
    v5 = v16;
    v4 = v17;
    v3 = v18;
    v2 = &v7;
    v1 = v19;
    v0 = v20;
    v22 = _ccall(0, 6, v17, v17, 0);
    v23 = v17;
    if (!((char)v22))
    {
        if (!(1))
            goto LABEL_10323f03;
LABEL_10323f03:
        if (0)
            goto LABEL_0x10323e9b;
        v26 = _ccall(2, 15, 3, 0, 0);
        if ((char)v26)
            goto LABEL_0x10323f14;
    }
    else
    {
        v26 = _ccall(2, 6, v23, v24, 0);
        if ((char)v26)
            goto LABEL_0x10323f14;
    }
}
```

