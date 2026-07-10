# elfbot.dll decompiled — jiru 0x10320cb9..0x10321639

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10320cb9` `0x10320cb9`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10320cb9(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10320cec` `0x10320cec`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10320cec(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10320cf3` `0x10320cf3`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10320cf3(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10320d27` `0x10320d27`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10320d27(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10320d35` `0x10320d35`

_38 bytes. (leaf/helper — see body)_

```c
void sub_10320d35(unsigned int a0, unsigned int a1)
{
    unsigned int v11;  // cc_op
    unsigned int v12;  // cc_dep1
    unsigned int v21;  // edi
    unsigned int v23;  // 4104
    unsigned int v24;  // cc_dep1
    unsigned int v26;  // 4101
    unsigned int v13;  // cc_dep2
    unsigned int v14;  // cc_ndep
    unsigned int v15;  // 4104
    unsigned int v16;  // 4110
    unsigned int v17;  // id
    unsigned int v18;  // ac
    unsigned int v19;  // ebx
    unsigned int v20;  // esi
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    unsigned int v6;  // [bp-0x4]
    unsigned int v7;  // [bp+0x0]
    unsigned int v8;  // [bp+0x0]

    v15 = _ccall(2, v11, v12, v13, v14);
    if (!((char)v15))
        goto LABEL_10320d38;
LABEL_10320d38:
    v16 = _ccall(v11, v12, v13, v14);
    v7 = v16 | 0x202 | v17 * 0x200000 & 0x200000 | v18 * 0x40000 & 0x40000;
    v6 = v8;
    v5 = a0;
    v4 = a1;
    v3 = v19;
    v2 = /* unsupported instruction */;
    v1 = v20;
    v0 = v21;
    v23 = _ccall(0, 6, a1, a1, 0);
    v24 = a1;
    if (!((char)v23))
    {
        if (!(1))
            goto LABEL_10320d45;
LABEL_10320d45:
        if (0)
            goto LABEL_0x10320cdd;
        v26 = _ccall(2, 15, 3, 0, 0);
        if ((char)v26)
            goto LABEL_0x10320d56;
    }
    else
    {
        v26 = _ccall(2, 6, v24, a1, 0);
        if ((char)v26)
            goto LABEL_0x10320d56;
    }
}
```

## `sub_10320d4f` `0x10320d4f`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10320d4f(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10320d63` `0x10320d63`

_28 bytes. (leaf/helper — see body)_

```c
int sub_10320d63(void)
{
    void* v1;  // [bp+0x8]

    *((unsigned int *)&v1[12]) = (int)v1[12] + 1;
}
```

## `sub_10320d67` `0x10320d67`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10320d67(void)
{
}
```

## `sub_10320d69` `0x10320d69`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10320d69(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10320d90` `0x10320d90`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern unsigned int g_1039ae80;

int sub_10320d90(int a0, int a1)
{
    unsigned long v11;  // ldt
    unsigned long v12;  // gdt
    unsigned short v13;  // fs
    unsigned long v14;  // 4149
    unsigned int v15;  // ebx
    unsigned int v16;  // esi
    unsigned int v17;  // edi
    unsigned long v18;  // 4171
    unsigned int v0;  // [bp-0x34]
    unsigned int v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x28]
    char v4;  // [bp-0x1d]
    char *v5;  // [bp-0x1c]
    unsigned int v6;  // [bp-0x14]
    unsigned int v7;  // [bp-0x10]
    unsigned int v8;  // [bp-0xc]
    unsigned int v9;  // [bp-0x8]
    char v10;  // [bp-0x4]

    v9 = 4294967294;
    v8 = &g_1039ae80;
    v7 = sub_10354150;
    v14 = _ccall(v11, v12, (unsigned int)v13, 0);
    v6 = *((int *)v14);
    v3 = v15;
    v2 = v16;
    v1 = v17;
    v8 ^= g_1038e180;
    v0 = g_1038e180 ^ &v10;
    v18 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int **)v18) = &v6;
    v5 = &v0;
    v4 = 0;
    v9 = 0;
    sub_10320e40(a0, a1); /* do not return */
}
```

## `sub_10320ddb` `0x10320ddb`

_55 bytes. (leaf/helper — see body)_

```c
int sub_10320ddb(void)
{
    char v4;  // al
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4119
    char v1;  // [bp+0xfffe7]
    unsigned int v2;  // [bp+0xffff4]
    unsigned int v3;  // [bp+0x100000]

    if (!v4)
    {
        v1 = 0;
        v3 = 4294967294;
    }
    else
    {
        v3 = 4294967294;
    }
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v8) = v2;
    return;
}
```

## `sub_10320dfe` `0x10320dfe`

_12 bytes. (leaf/helper — see body)_

```c
int sub_10320dfe(void)
{
    char v1;  // [bp+0xfffeb]

    return -(0 < v1) + 1;
}
```

## `sub_10320e0a` `0x10320e0a`

_24 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1b4;

void sub_10320e0a(void)
{
    char v1;  // [bp+0xfffeb]
    void* v2;  // [bp+0xfffec]
    unsigned int v3;  // [bp+0x100000]

    *((unsigned int *)&v2[4]) = 100;
    g_1038b1b4();
    v1 = 1;
    v3 = 4294967294;
}
```

## `sub_10320e22` `0x10320e22`

_7 bytes. (leaf/helper — see body)_

```c
void sub_10320e22(void)
{
    unsigned int v1;  // [bp+0x100000]

    v1 = 4294967294;
}
```

## `sub_10320e40` `0x10320e40`

_148 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038c8ac;
extern unsigned int g_1038e180;

void sub_10320e40(unsigned int a0, unsigned int a1)
{
    unsigned int v19;  // esi
    unsigned int v20;  // edi
    unsigned int v21;  // 4185
    unsigned int v22;  // id
    unsigned int v23;  // ac
    unsigned int v24;  // ebx
    unsigned int v25;  // 4110
    unsigned int v26;  // cc_dep1
    unsigned int v27;  // 4143
    unsigned int v0;  // [bp-0x1098]
    unsigned int v1;  // [bp-0x1094]
    char *v2;  // [bp-0x1090]
    char *v3;  // [bp-0x108c]
    unsigned int v4;  // [bp-0x1088]
    unsigned int v5;  // [bp-0x1084]
    unsigned int v6;  // [bp-0x1080]
    char *v7;  // [bp-0x107c]
    unsigned int v8;  // [bp-0x1078]
    unsigned int v9;  // [bp-0x1074]
    unsigned int v10;  // [bp-0x1070]
    char *v11;  // [bp-0x17c]
    unsigned int v12;  // [bp-0x178]
    unsigned int v13;  // [bp-0x6c]
    char v14;  // [bp-0x66]
    char v15;  // [bp-0x65]
    char v16;  // [bp-0x64]
    char v17;  // [bp-0x4]

    v13 = g_1038e180 ^ &v17;
    v10 = v19;
    v9 = v20;
    v15 = 1;
    v12 = 0;
    v11 = &v16;
    v8 = a0;
    v7 = &v16;
    v21 = _ccall(15, g_1038e180 ^ &v17, 0, 0);
    v8 = v21 | 0x202 | v22 * 0x200000 & 0x200000 | v23 * 0x40000 & 0x40000;
    v6 = a0;
    v5 = a1;
    v4 = v24;
    v3 = &v8;
    v2 = &v17;
    v1 = v19;
    v0 = v20;
    if (!(1))
        goto LABEL_10320e97;
LABEL_10320e97:
    for (; (v25 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v25 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
    v26 = (v21 | 0x202 | v22 * 0x200000 & 0x200000 | v23 * 0x40000 & 0x40000) & 2261;
    v14 = 1;
    v27 = _ccall(0, 0, (v21 | 0x202 | v22 * 0x200000 & 0x200000 | v23 * 0x40000 & 0x40000) & 2261, 0, 0);
    sub_10320780(g_1038c8ac->field_0);
}
```

## `sub_10320e92` `0x10320e92`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10320e92(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10320e99` `0x10320e99`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10320e99(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10320ec6` `0x10320ec6`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10320ec6(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10320edb` `0x10320edb`

_170 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[32];
    unsigned int field_20;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b0e0;
extern struct_0 *g_1038b1b8;
extern char g_103a26a4;
extern struct_1 *g_103a2924;

int sub_10320edb(void)
{
    char v17;  // al
    unsigned int v18;  // eax
    unsigned int v27;  // 4101
    unsigned int v28;  // 4101
    unsigned int v29;  // 4101
    unsigned int v30;  // 4101
    unsigned int v31;  // 4101
    unsigned int v32;  // edx
    unsigned int v33;  // 4101
    unsigned int v34;  // 4103
    unsigned int v35;  // 4101
    unsigned int v36;  // 4101
    unsigned int v19;  // edx
    unsigned int v37;  // 4101
    unsigned int v38;  // 4101
    unsigned int v39;  // 4101
    unsigned int v40;  // 4101
    unsigned int v20;  // ecx
    unsigned int v21;  // ebx
    unsigned int v22;  // esi
    unsigned int v23;  // edi
    unsigned int v24;  // 4101
    unsigned int v25;  // 4103
    unsigned int v26;  // 4101
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x20]
    char *v4;  // [bp-0x1c]
    unsigned int v5;  // [bp-0x1c]
    unsigned int v6;  // [bp-0x18]
    unsigned int v7;  // [bp-0x18]
    unsigned int v8;  // [bp-0x14]
    unsigned int v9;  // [bp-0x10]
    unsigned int v10;  // [bp-0x10]
    unsigned int v11;  // [bp-0xc]
    unsigned int v12;  // [bp-0x8]
    unsigned int v13;  // [bp-0x4]
    char v15;  // [bp+0xfffa3]

    v18 = _INSERT(v17 CONCAT 0, 0, v17 + 15);
    v19 = _INSERT(0, 1, 192);
    if (!v18)
    {
        sub_10351225();
        return;
    }
    v13 = v18;
    v12 = v20;
    v11 = v19;
    v10 = v21;
    v7 = /* unsupported instruction */;
    v5 = v22;
    v3 = v23;
LABEL_10320f03:
    v24 = _ccall(0, 15, 0, 0, 0);
    if ((char)v24)
        goto LABEL_10320f05;
    else
        goto LABEL_10320f06;
    while (true)
    {
LABEL_10320f05:
        __unsupported_jumpkind_Ijk_NoDecode()
        while (true)
        {
LABEL_10320f06:
            v25 = _ccall(10, 15, 0, 0, 0);
            if ((char)v25)
            {
                v26 = _ccall(8, 15, 0, 0, 0);
                if (!((char)v26))
                {
                    __unsupported_jumpkind_Ijk_NoDecode()
                    __unsupported_jumpkind_Ijk_NoDecode()
                    v27 = _ccall(10, 15, 0, 0, 0);
                    if (!((char)v27))
                    {
                        v28 = _ccall(0, 15, 0, 0, 0);
                        if ((char)v28)
                            break;
                        else
                            continue;
                    }
                    v29 = _ccall(8, 15, 0, 0, 0);
                    if ((char)v29)
                        goto LABEL_10320f03;
                    goto LABEL_10320f0c;
                }
                __unsupported_jumpkind_Ijk_NoDecode()
                v30 = _ccall(8, 15, 0, 0, 0);
                if (!((char)v30))
                    goto LABEL_10320f0c;
LABEL_10320f03:
                if ((v31 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v31))
                    break;
            }
            else
            {
                __unsupported_jumpkind_Ijk_NoDecode()
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_10320f0c:
                if (g_1038b0e0(1000))
                {
                    if (v15 && g_103a2924->field_20)
                        v15 = 0;
                    v12 = &g_103a26a4;
                    v11 = g_1038b1b8(&g_103a26a4);
                    v9 = v20;
                    v8 = v32;
                    v6 = v10;
                    v4 = &v12;
                    v2 = v7;
                    v1 = v5;
                    v0 = v3;
LABEL_10320f65:
                    v33 = _ccall(0, 15, 0, 0, 0);
                    if ((char)v33)
                        goto LABEL_10320f67;
                    else
                        goto LABEL_10320f68;
                    while (true)
                    {
LABEL_10320f67:
                        __unsupported_jumpkind_Ijk_NoDecode()
                        while (true)
                        {
LABEL_10320f68:
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
                                        goto LABEL_10320f65;
                                    else
                                        goto LABEL_0x10320f6e;
                                }
                            }
                            else
                            {
                                __unsupported_jumpkind_Ijk_NoDecode()
                                v39 = _ccall(8, 15, 0, 0, 0);
                                if ((char)v39)
                                    goto LABEL_10320f65;
                                else
                                    goto LABEL_0x10320f6e;
                            }
LABEL_10320f65:
                            if ((v40 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v40))
                                break;
                        }
                    }
                }
            }
        }
    }
}
```

## `sub_10320ef9` `0x10320ef9`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10320ef9(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10320f5b` `0x10320f5b`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10320f5b(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10320f74` `0x10320f74`

_135 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[952675349];
    unsigned int field_38c8ac15;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b03c;
extern unsigned int g_1038c7f4;
extern unsigned int g_1038c808;
extern unsigned int g_1038c834;
extern char g_103a290b;
extern char g_103a2920;

int sub_10320f74(void)
{
    struct_1 *idx;  // ebx
    struct_1 *v12;  // ebx
    unsigned int v21;  // eax
    unsigned int v22;  // eax
    char *v23;  // cc_dep1
    unsigned int v24;  // 4123
    unsigned int v25;  // 4110
    unsigned int v26;  // id
    unsigned int v27;  // ac
    unsigned int v29;  // edx
    unsigned int v30;  // esi
    char v13;  // al
    unsigned int v31;  // cc_op
    unsigned int v32;  // 4104
    unsigned int v33;  // cc_dep1
    unsigned int v34;  // cc_dep2
    unsigned int v38;  // 4101
    char *v14;  // eax
    char *v15;  // edi
    char v16;  // cl
    unsigned int v17;  // cc_op
    char *v18;  // cc_dep1
    unsigned int v19;  // cc_dep2
    char *v20;  // edx
    char *v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    char *v2;  // [bp-0x18]
    struct_1 *v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    char *v6;  // [bp-0x8]
    char *v7;  // [bp-0x4]
    unsigned int v8;  // [bp-0x4]
    char v10;  // [bp+0xfffa2]

    *((unsigned int *)&(idx->padding_0)[1]) = *((int *)&(idx->padding_0)[1]) - 1;
    do
    {
        v14 = _INSERT(v13, 0, v13 + 59);
        *(v15) = *(v15) | v16;
        *(v14) = *(v14) + *((char *)&v14);
        v17 = 15;
        v18 = g_103a290b;
        v19 = 0;
        if (!g_103a290b)
        {
            v20 = v10;
            v17 = 15;
            v18 = v20;
            v19 = 0;
            if (v20)
            {
                v17 = 6;
                v18 = *((int *)&g_103a2920);
                v19 = 0;
                if (*((int *)&g_103a2920) > NULL)
                {
                    v21 = g_1038c7f4 ^ g_1038c834 ^ g_1038c808;
                    v17 = 15;
                    v18 = v21 & 8;
                    v19 = 0;
                    v14 = v21 & 8;
                    if (((char)v21 & 8))
                    {
                        v22 = g_1038b03c();
                        v14 = v22 - *((int *)&g_103a2920);
                        v17 = 6;
                        v19 = 300000;
                        v18 = v14;
                        if (v18 > 0x493e0)
                        {
                            v10 = 0;
                            v18 = v14;
                        }
                    }
                }
            }
        }
        v23 = v18;
        v7 = v14;
        v24 = _ccall(2, v17, v23, v19, 0);
        if (!((char)v24))
            goto LABEL_10320fd8;
LABEL_10320fd8:
        v25 = _ccall(v17, v23, v19, 0);
        v8 = v25 | 0x202 | v26 * 0x200000 & 0x200000 | v27 * 0x40000 & 0x40000;
        v6 = v7;
        v5 = v16;
        v4 = v29;
        v3 = v12;
        v2 = &v8;
        v1 = v30;
        v0 = v15;
        v31 = 6;
        v32 = _ccall(0, 6, v29, v29, 0);
        v33 = v29;
        v34 = v29;
        if ((char)v32)
            break;
        if (!(1))
            goto LABEL_10320fe5;
LABEL_10320fe5:
        v12 = NULL;
        v31 = 15;
        v33 = 3;
        v34 = 0;
    } while (false);
    v38 = _ccall(2, v31, v33, v34, 0);
    if ((char)v38)
        goto LABEL_0x10320ff6;
}
```

## `sub_10320fef` `0x10320fef`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10320fef(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10321003` `0x10321003`

_62 bytes. (leaf/helper — see body)_

```c
int sub_10321003(void)
{
    unsigned int v10;  // eax
    unsigned int v11;  // 4101
    unsigned int v12;  // 4103
    unsigned int v13;  // 4101
    unsigned int v14;  // 4101
    unsigned int v15;  // 4101
    unsigned int v16;  // 4101
    unsigned int v17;  // 4101
    unsigned int v18;  // 4101
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

    v10 = v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff;
    *((unsigned int *)&v2[380]) = 2147549185;
    v8 = v10 * 0x1000000 | v10 * 0x100 & 0xff0000 | v10 >> 8 & 0xff00 | v10 >> 24 & 0xff;
    v7 = ~(~(v6));
    v6 = v5;
    v5 = v4;
    v4 = &v9;
    v3 = v2;
    v2 = v1;
    v1 = v0;
LABEL_1032103a:
    v11 = _ccall(0, 15, 0, 0, 0);
    if ((char)v11)
        goto LABEL_1032103c;
    else
        goto LABEL_1032103d;
    while (true)
    {
LABEL_1032103c:
        __unsupported_jumpkind_Ijk_NoDecode()
        while (true)
        {
LABEL_1032103d:
            v12 = _ccall(10, 15, 0, 0, 0);
            if (!((char)v12))
            {
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_10321042:
            }
            v13 = _ccall(8, 15, 0, 0, 0);
            if (!((char)v13))
            {
                if (!(1))
                    goto LABEL_10321042;
                v14 = _ccall(10, 15, 0, 0, 0);
                if (!((char)v14))
                {
                    v15 = _ccall(0, 15, 0, 0, 0);
                    if ((char)v15)
                        break;
                    else
                        continue;
                }
                else
                {
                    v16 = _ccall(8, 15, 0, 0, 0);
                    if ((char)v16)
                        goto LABEL_1032103a;
                    else
                        goto LABEL_0x10321043;
                }
            }
            else
            {
                __unsupported_jumpkind_Ijk_NoDecode()
                v17 = _ccall(8, 15, 0, 0, 0);
                if ((char)v17)
                    goto LABEL_1032103a;
                else
                    goto LABEL_0x10321043;
            }
LABEL_1032103a:
            if ((v18 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v18))
                break;
        }
    }
}
```

## `sub_10321007` `0x10321007`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10321007(void)
{
}
```

## `sub_10321009` `0x10321009`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10321009(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10321030` `0x10321030`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10321030(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10321050` `0x10321050`

_1678 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
    char padding_10[8];
    int field_18;
    char padding_1c[4];
    unsigned int field_20;
    int field_24;
    char padding_28[52];
    unsigned int field_5c;
} struct_0;

extern unsigned int g_1038c824;
extern char g_103a2905;

int sub_10321050(void)
{
    char *v51;  // eax
    char v52;  // 4100
    unsigned int v53;  // cc_dep1
    unsigned int v54;  // cc_dep2
    unsigned int v57;  // edx
    unsigned int v44;  // [bp+0xffe84]
    struct_0 *idx;  // [bp+0xffe8c]

    v52 = *(v51);
    *(v51) = v52 + *((char *)&v51);
    v53 = v52;
    v54 = *((char *)&v51);
    v44 = idx->field_c ^ g_1038c824;
    if (g_103a2905 && (v57 = g_1038c824 ^ 2147483649, v44 == v57))
        goto LABEL_0x1032109a;
    else
        goto LABEL_0x10321738;
}
```

## `sub_10321059` `0x10321059`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10321059(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103210bc` `0x103210bc`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103210bc(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103210c3` `0x103210c3`

_3 bytes. (leaf/helper — see body)_

```c
void sub_103210c3(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10321114` `0x10321114`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10321114(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032112a` `0x1032112a`

_17 bytes. (leaf/helper — see body)_

```c
int sub_1032112a(void)
{
    char *v3;  // edx
    char v4;  // ch
    char v0;  // [bp-0x460]
    char *v1;  // [bp-0x4]

    *(v3) = *(v3) + v4;
    v1 = &v0;
    sub_10350ad0();
}
```

## `sub_1032113b` `0x1032113b`

_19 bytes. (leaf/helper — see body)_

```c
int sub_1032113b(void)
{
    unsigned int v0;  // [bp-0x460]

    v0 = 65537;
    return sub_1032114e();
}
```

## `sub_1032114e` `0x1032114e`

_108 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern struct_1 *g_1038b0dc;
extern struct_0 *g_1038c8ac;

int sub_1032114e(void)
{
    unsigned int v10;  // eax
    unsigned int v11;  // eax
    unsigned int v20;  // 4110
    unsigned int v12;  // ecx
    unsigned int v13;  // 4193
    unsigned int v14;  // id
    unsigned int v15;  // ac
    unsigned int v16;  // edx
    unsigned int v17;  // ebx
    unsigned int v18;  // esi
    unsigned int v19;  // edi
    unsigned int v0;  // [bp-0x2c]
    unsigned int v1;  // [bp-0x28]
    char *v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x1c]
    unsigned int v4;  // [bp-0x18]
    unsigned int v5;  // [bp-0x14]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0xc]

    v11 = g_1038b0dc(g_1038c8ac->field_4, v10);
    if (!v11)
        goto LABEL_0x10321267;
    v7 = v12;
    v6 = v11;
    v13 = _ccall(15, v11, 0, 0);
    v8 = v13 | 0x202 | v14 * 0x200000 & 0x200000 | v15 * 0x40000 & 0x40000;
    v5 = v7;
    v4 = v16;
    v3 = v17;
    v2 = &v8;
    v1 = v18;
    v0 = v19;
    if (!(1))
        goto LABEL_1032118e;
LABEL_1032118e:
    for (; (v20 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v20 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
}
```

## `sub_10321189` `0x10321189`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10321189(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10321190` `0x10321190`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10321190(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103211be` `0x103211be`

_90 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a2914;

int sub_103211be(void)
{
    unsigned int v13;  // edx
    unsigned int v14;  // 4110
    unsigned int v23;  // cc_dep1
    unsigned int v25;  // 4101
    unsigned int v15;  // id
    unsigned int v16;  // ac
    unsigned int v17;  // ecx
    unsigned int v18;  // ebx
    unsigned int v19;  // esi
    unsigned int v20;  // edi
    unsigned int v22;  // 4104
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    char *v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    unsigned int v7;  // [bp-0x4]
    unsigned int v8;  // [bp-0x4]
    unsigned int v10;  // [bp+0xffb9c]
    unsigned int v11;  // [bp+0xffba0]
    unsigned int v12;  // [bp+0xffc5c]

    2897713873();
    __unsupported_jumpkind_Ijk_NoDecode()
    __unsupported_jumpkind_Ijk_Privileged()
    v13 = v12 - g_103a2914 >> 12;
    v10 = v13;
    if (v11 == v10)
        goto LABEL_0x10321267;
    v7 = v11;
    if (v7 >= v10)
        goto LABEL_1032120b;
LABEL_1032120b:
    v14 = _ccall(6, v7, v10, 0);
    v8 = v14 | 0x202 | v15 * 0x200000 & 0x200000 | v16 * 0x40000 & 0x40000;
    v6 = v7;
    v5 = v17;
    v4 = v13;
    v3 = v18;
    v2 = &v8;
    v1 = v19;
    v0 = v20;
    v22 = _ccall(0, 6, v13, v13, 0);
    v23 = v13;
    if (!((char)v22))
    {
        if (!(1))
            goto LABEL_10321218;
LABEL_10321218:
        if (0)
            goto LABEL_0x103211b0;
        v25 = _ccall(2, 15, 3, 0, 0);
        if ((char)v25)
            goto LABEL_0x10321229;
    }
    else
    {
        v25 = _ccall(2, 6, v23, v13, 0);
        if ((char)v25)
            goto LABEL_0x10321229;
    }
}
```

## `sub_10321222` `0x10321222`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10321222(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10321236` `0x10321236`

_45 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a2914;
extern unsigned int g_103a2928;

int sub_10321236(void)
{
    unsigned int v1;  // ecx
    unsigned int v2;  // 4114
    unsigned int v3;  // cc_dep2

    v1 = g_103a2928 * 0x1000;
    v2 = g_103a2914;
    v3 = v2;
    g_103a2914 = v1 + v2;
}
```

## `sub_1032123a` `0x1032123a`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032123a(void)
{
}
```

## `sub_1032123c` `0x1032123c`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1032123c(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10321262` `0x10321262`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10321262(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10321279` `0x10321279`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10321279(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10321292` `0x10321292`

_8 bytes. (leaf/helper — see body)_

```c
void sub_10321292(void)
{
    void* v1;  // ebx
    unsigned int v2;  // cc_op
    unsigned int v3;  // cc_dep1
    unsigned int v4;  // cc_dep2
    unsigned int v5;  // cc_ndep
    unsigned int v6;  // 4105
    unsigned int v7;  // 4101

    *((unsigned int *)&v1[2054612926]) = (int)v1[2054612926] - 1;
    v6 = _ccall(v2, v3, v4, v5);
    while (true)
    {
        v7 = _ccall(4, 21, (int)v1[2054612926] - 1, 0, v6);
    }
}
```

## `sub_1032129b` `0x1032129b`

_18 bytes. (leaf/helper — see body)_

```c
int sub_1032129b(void)
{
    void* idx;  // ebx
    char v3;  // cl
    unsigned int v0;  // [bp-0x4]

    *((unsigned int *)&idx[96115]) = (int)idx[96115] - 1;
    v0 = *((int *)idx);
    if (!(v3 & 31))
    {
        *((char *)&idx[251666553]) = (char)idx[251666553] << (v3 & 31 & 7) | (char)idx[251666553] >> 8 - (v3 & 31 & 7);
        return;
    }
    *((char *)&idx[251666553]) = (char)idx[251666553] << (v3 & 31 & 7) | (char)idx[251666553] >> 8 - (v3 & 31 & 7);
    return;
}
```

## `sub_103212ad` `0x103212ad`

_2 bytes. (leaf/helper — see body)_

```c
void sub_103212ad(void)
{
    unsigned int v1;  // cc_op
    unsigned int v2;  // cc_dep1
    unsigned int v3;  // cc_dep2
    unsigned int v4;  // cc_ndep
    unsigned int v5;  // 4101

    do
    {
        v5 = _ccall(14, v1, v2, v3, v4);
    } while (!((char)v5));
    sub_103212ad();
    return;
}
```

## `sub_103212b7` `0x103212b7`

_679 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

extern unsigned int g_1038c7f4;
extern unsigned int g_1038c808;
extern unsigned int g_1038c834;
extern char g_10390233;
extern char g_10390234;
extern char g_10390235;
extern char g_10390236;
extern char g_103a2906;
extern unsigned int g_103a2910;
extern unsigned int g_103a2914;
extern struct_0 *g_103a2924;
extern char g_103a2928;

int sub_103212b7(void)
{
    unsigned int v18;  // eax
    unsigned int v19;  // eax
    void* v28;  // ebx
    void* v29;  // ebp
    unsigned int *v30;  // edi
    unsigned int v31;  // 4097
    unsigned int v32;  // eax
    unsigned int v33;  // edx
    unsigned int v34;  // cc_op
    unsigned int v35;  // cc_dep1
    unsigned int v36;  // cc_dep2
    char v37;  // cl
    unsigned int v20;  // 4193
    unsigned int v38;  // 4110
    unsigned int v39;  // 4104
    unsigned int v40;  // 4143
    unsigned int v42;  // 4101
    unsigned int v43;  // edx
    unsigned int v44;  // eax
    unsigned int v45;  // edx
    unsigned int v46;  // ecx
    unsigned int v21;  // id
    unsigned int v47;  // edi
    unsigned int v48;  // esi
    unsigned int v49;  // eax
    unsigned int v50;  // ecx
    unsigned int v51;  // ebx
    unsigned int v52;  // 4101
    unsigned int v53;  // 4103
    unsigned int v54;  // 4101
    unsigned int v55;  // 4101
    unsigned int v22;  // ac
    unsigned int v56;  // 4101
    unsigned int v57;  // 4101
    unsigned int v58;  // 4101
    unsigned int v59;  // 4101
    unsigned int v23;  // edx
    void* v24;  // ebx
    unsigned int v25;  // esi
    unsigned int *v26;  // edi
    unsigned int v27;  // 4110
    unsigned int *v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    void* v2;  // [bp-0x1c], Other Possible Types: unsigned int
    char *v3;  // [bp-0x18], Other Possible Types: unsigned int
    char *v4;  // [bp-0x14], Other Possible Types: void*
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]
    unsigned int v8;  // [bp-0x4]
    char v9;  // [bp+0x0]
    unsigned short v11;  // [bp+0xffb98]
    unsigned int v12;  // [bp+0xffe78]
    unsigned int v13;  // [bp+0xffe7c]
    unsigned int v14;  // [bp+0xffe88]
    unsigned int v15;  // [bp+0xffe90]
    char v16;  // [bp+0xfffa2]

    v19 = v18 - g_103a2914 >> 12;
    v13 = v19;
    if (g_103a2906)
    {
        v8 = g_103a2906;
        v7 = v19;
        v20 = _ccall(15, (unsigned int)g_103a2906, 0, 0);
        v8 = v20 | 0x202 | v21 * 0x200000 & 0x200000 | v22 * 0x40000 & 0x40000;
        v6 = v8;
        v5 = v23;
        v4 = v24;
        v3 = &v8;
        v1 = v25;
        v0 = v26;
        if (!(1))
            goto LABEL_103212fc;
LABEL_103212fc:
        for (; (v27 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v27 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
        v28 = v4;
        v29 = v2;
        v30 = v26;
        v31 = v8;
        v32 = _INSERT((unsigned short)v5 CONCAT 0, 0, v7);
        v33 = (int)v29[392];
        v35 = v33;
        v36 = v33 - 1;
        if (v33 - 1 >= 0)
        {
            v8 = 1;
            v37 = (&g_10390233)[v29[392]];
            v0 = v26;
            v40 = _ccall(6, v35, 1, 0);
            *((char *)&v28[100211]) = (char)v28[100211] + v37 + ((char)v40 & 1);
            *(v30) = *(v30) - 1;
            /* unsupported instruction */
            /* unsupported instruction */
            sub_10321395(v0);
            return;
        }
        v8 = v32;
        if (v35 >= 1)
            goto LABEL_103213b0;
LABEL_103213b0:
        v38 = _ccall(6, v35, 1, 0);
        v8 = v38 | 0x202 | ((char)(v31 >> 10) ? 4294967295 : 1) & 0x400 | ((char)(v31 >> 21) ? 1 : 0) * 0x200000 & 0x200000 | ((char)(v31 >> 18) ? 1 : 0) * 0x40000 & 0x40000;
        v7 = v8;
        v5 = v36;
        v4 = v28;
        v3 = &v8;
        v2 = v29;
        v0 = v30;
        v34 = 6;
        v39 = _ccall(0, 6, v36, v36, 0);
        v35 = v36;
        if (!((char)v39))
        {
            if (!(1))
                goto LABEL_103213bd;
LABEL_103213bd:
            v34 = 15;
            v35 = 3;
            v36 = 0;
            v0 = v30;
            if (false)
            {
                v40 = _ccall(15, 3, 0, 0);
                *((char *)4294867085) = *((char *)4294867085) + 3 + ((char)v40 & 1);
                *(v30) = *(v30) - 1;
                /* unsupported instruction */
                /* unsupported instruction */
                sub_10321395(v0);
                return;
            }
        }
        v42 = _ccall(2, v34, v35, v36, 0);
        if ((char)v42)
            goto LABEL_0x103213ce;
    }
    else if (v13 >= 0 && v13 < *((int *)&g_103a2928))
    {
        v43 = v16;
        if (v43)
        {
            v8 = 0;
            v44 = v13 & 2147483655;
            if ((v13 & 2147483655) < 0)
                v44 = (v44 - 1 | 0xfffffff8) + 1;
            v45 = v13 & 2147483655;
            if ((v13 & 2147483655) < 0)
                v45 = (v45 - 1 | 0xfffffff8) + 1;
            v46 = v13 & 2147483655;
            if ((v13 & 2147483655) < 0)
                v46 = (v46 - 1 | 0xfffffff8) + 1;
            v47 = (*((int *)(272156632 + 4 * (&g_10390234)[v44])) ^ *((int *)(272156632 + 4 * (&g_10390235)[v45])) ^ *((int *)(272156632 + 4 * (&g_10390236)[v46]))) >> ((char)(v13 % 28) & 31) & 15;
            v48 = v13 * 16 + v47;
            v43 = sub_10322f60(v13, g_103a2910 + v48 * 4) & 0xff;
            if (v43)
                goto LABEL_10321557;
        }
        else
        {
LABEL_10321557:
            if (!v15 && ((g_1038c7f4 ^ g_1038c834 ^ g_1038c808) & 0x200000))
            {
                v43 = g_103a2924->field_10;
                v15 = v43;
            }
            if (v15 && v12 < v15 + 0x10000)
            {
                v43 = g_103a2914;
                v12 = g_103a2914;
            }
            v49 = v12;
            if (v49 < g_103a2914 || v12 > *((int *)&g_103a2928) * 0x1000 + g_103a2914)
            {
                v11 = 0;
                v8 = v49;
                v7 = v50;
                v6 = v43;
                v5 = v51;
                v4 = &v9;
                v3 = /* unsupported instruction */;
                v2 = v48;
                v1 = v47;
LABEL_1032160c:
                v52 = _ccall(0, 15, 0, 0, 0);
                if ((char)v52)
                    goto LABEL_1032160e;
                else
                    goto LABEL_1032160f;
                while (true)
                {
LABEL_1032160e:
                    __unsupported_jumpkind_Ijk_NoDecode()
                    while (true)
                    {
LABEL_1032160f:
                        v53 = _ccall(10, 15, 0, 0, 0);
                        if ((char)v53)
                        {
                            v54 = _ccall(8, 15, 0, 0, 0);
                            if (!((char)v54))
                            {
                                if (!(1))
                                    goto LABEL_10321614;
                                v55 = _ccall(10, 15, 0, 0, 0);
                                if (!((char)v55))
                                {
                                    v56 = _ccall(0, 15, 0, 0, 0);
                                    if ((char)v56)
                                        break;
                                    else
                                        continue;
                                }
                                v57 = _ccall(8, 15, 0, 0, 0);
                                if ((char)v57)
                                    goto LABEL_1032160c;
                                goto LABEL_10321615;
                            }
                            __unsupported_jumpkind_Ijk_NoDecode()
                            v58 = _ccall(8, 15, 0, 0, 0);
                            if (!((char)v58))
                                goto LABEL_10321615;
LABEL_1032160c:
                            if ((v59 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v59))
                                break;
                        }
                        else
                        {
                            __unsupported_jumpkind_Ijk_NoDecode()
LABEL_10321614:
                            __unsupported_jumpkind_Ijk_NoDecode()
LABEL_10321615:
                            while (true)
                            ;
                        }
                    }
                }
            }
            else
            {
                v14 = 65538;
            }
        }
    }
}
```

## `sub_103212f7` `0x103212f7`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103212f7(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103212fe` `0x103212fe`

_3 bytes. (leaf/helper — see body)_

```c
void sub_103212fe(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10321395` `0x10321395`

_19 bytes. (leaf/helper — see body)_

```c
int sub_10321395(void)
{
    int v2;  // edx
    int v1;  // [bp+0xffe7c]

    sub_10322f60(v1 - 1, v2);
}
```

## `sub_103213c7` `0x103213c7`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103213c7(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103213db` `0x103213db`

_146 bytes. (leaf/helper — see body)_

```c
extern char g_103a2928;

int sub_103213db(void)
{
    unsigned int v2;  // ecx
    unsigned int v3;  // 4101
    void* v1;  // [bp+0x8]

    v2 = (int)v1[392] + 1;
    if (v2 < *((int *)&g_103a2928))
    {
        sub_10321466(1);
        return;
    }
    v3 = _ccall(0, 6, v2, *((int *)&g_103a2928), 0);
}
```

## `sub_103213df` `0x103213df`

_2 bytes. (leaf/helper — see body)_

```c
void sub_103213df(void)
{
}
```

## `sub_103213e1` `0x103213e1`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103213e1(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10321466` `0x10321466`

_19 bytes. (leaf/helper — see body)_

```c
int sub_10321466(void)
{
    int v2;  // edx
    int v1;  // [bp+0xffe7c]

    sub_10322f60(v1 + 1, v2);
}
```

## `sub_1032147f` `0x1032147f`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1032147f(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10321602` `0x10321602`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10321602(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10321620` `0x10321620`

_130 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[7];
    unsigned int field_7;
} struct_0;

int sub_10321620(void)
{
    struct_0 *v14;  // eax
    unsigned int v23;  // esi
    unsigned int v24;  // edi
    unsigned int v25;  // 4110
    void* v15;  // ecx
    unsigned int v17;  // edx
    unsigned int v18;  // edx
    unsigned int v19;  // 4204
    unsigned int v20;  // id
    unsigned int v21;  // ac
    unsigned int v22;  // ebx
    unsigned int v0;  // [bp-0x2c]
    unsigned int v1;  // [bp-0x28]
    char *v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x1c]
    unsigned int v4;  // [bp-0x18]
    void* v5;  // [bp-0x14], Other Possible Types: unsigned int
    struct_0 *v6;  // [bp-0x10]
    void* v7;  // [bp-0xc], Other Possible Types: unsigned int
    unsigned int v12;  // [bp+0xffe78]

    v17 = v12;
    v18 = v17 + 0x1000;
    v12 = v18;
    v7 = v15;
    v6 = v14;
    v19 = _ccall(3, v17, 0x1000, 0);
    v7 = v19 | 0x202 | v20 * 0x200000 & 0x200000 | v21 * 0x40000 & 0x40000;
    v5 = v15;
    v4 = v18;
    v3 = v22;
    v2 = &v7;
    v1 = v23;
    v0 = v24;
    if (!(1))
        goto LABEL_10321677;
LABEL_10321677:
    for (; (v25 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v25 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
    /* unsupported instruction */
    v5 = /* unsupported instruction */ - 1132;
    sub_103216a7(2, 0); /* do not return */
}
```

## `sub_10321639` `0x10321639`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10321639(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

