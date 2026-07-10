# elfbot.dll decompiled — jiru 0x10323f0d..0x103248d2

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10323f0d` `0x10323f0d`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323f0d(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323f21` `0x10323f21`

_38 bytes. (leaf/helper — see body)_

```c
int sub_10323f21(void)
{
    unsigned int v3;  // cc_dep1
    unsigned int v4;  // 4177
    void* v1;  // [bp+0x8]
    unsigned int v2;  // [bp+0x20]

    v3 = v2 & 2261;
    *((int *)&v1[48]) = *((int *)((int)v1[48] + 12));
    v4 = _ccall(0, 0, v2 & 2261, 0, 0);
}
```

## `sub_10323f25` `0x10323f25`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10323f25(void)
{
}
```

## `sub_10323f27` `0x10323f27`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323f27(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323f41` `0x10323f41`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323f41(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10323f4b` `0x10323f4b`

_91 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a290c;

int sub_10323f4b(unsigned int a0, unsigned int idx)
{
    unsigned int v4[4];  // eax
    unsigned int v0;  // [bp-0x3c]
    unsigned int v1;  // [bp-0x34]
    unsigned int v2;  // [bp-0x4]
    int v3;  // [bp+0x0]

    v1 = *((int *)(g_103a290c + idx * 4));
    if (!v1)
        *((unsigned int *)(g_103a290c + idx * 4)) = 0;
    __unsupported_jumpkind_Ijk_NoDecode()
    sub_10350abd(v3);
    v1 = v4[3];
    v0 = v4[0];
    v2 = v0;
    sub_10350abd();
}
```

## `sub_10323fcd` `0x10323fcd`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10323fcd(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324025` `0x10324025`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10324025(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032402c` `0x1032402c`

_3 bytes. (leaf/helper — see body)_

```c
void sub_1032402c(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032405a` `0x1032405a`

_25 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a2934;

int sub_1032405a(unsigned int a0)
{
    unsigned int i;  // cc_dep1
    unsigned int v3;  // 4116
    unsigned int idx;  // [bp+0x10000c]

    i = a0 | 4;
    *((unsigned int *)(g_103a2934 + idx * 4)) = a0 | 4;
    v3 = _ccall(0, 15, a0 | 4, 0, 0);
    if (!((char)v3) && i < 0)
        if (!i)
            goto LABEL_1032406c;
        else
            goto LABEL_10324071;
    while (true)
    {
        do
        {
LABEL_1032406c:
            __unsupported_jumpkind_Ijk_NoDecode()
            __unsupported_jumpkind_Ijk_NoDecode()
        } while (!i);
LABEL_10324071:
    }
}
```

## `sub_103240bc` `0x103240bc`

_150 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b0e4;
extern struct_0 *g_1038c8ac;

int sub_103240bc(void)
{
    unsigned int v12;  // eax
    unsigned int v13;  // eax
    unsigned int v22;  // edi
    unsigned int v24;  // 4104
    unsigned int v25;  // cc_dep1
    unsigned int v26;  // cc_dep2
    unsigned int v28;  // 4101
    unsigned int v29;  // ecx
    unsigned int v30;  // 4193
    unsigned int v31;  // id
    unsigned int v14;  // cc_dep1
    unsigned int v32;  // ac
    unsigned int v33;  // edx
    unsigned int v34;  // ebx
    unsigned int v35;  // esi
    unsigned int v36;  // edi
    unsigned int v37;  // 4110
    void* v38;  // ebp
    unsigned int v15;  // 4110
    unsigned int v16;  // id
    unsigned int v17;  // ac
    unsigned int v18;  // ecx
    unsigned int v19;  // edx
    unsigned int v20;  // ebx
    unsigned int v21;  // esi
    unsigned int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x2c]
    void* v2;  // [bp-0x28], Other Possible Types: unsigned int
    char *v3;  // [bp-0x24]
    unsigned int v4;  // [bp-0x20]
    unsigned int v5;  // [bp-0x1c]
    unsigned int v6;  // [bp-0x18]
    unsigned int v7;  // [bp-0x14]
    void* v8;  // [bp-0x10], Other Possible Types: unsigned int
    unsigned int v10;  // [bp+0xffff4]

    v13 = g_1038b0e4(g_1038c8ac->field_0, v10, v12);
    v14 = v13;
    if (!v13)
    {
        v8 = 0;
        if (v14 >= 0)
            goto LABEL_103240dc;
LABEL_103240dc:
        v15 = _ccall(15, v14, 0, 0);
        v8 = v15 | 0x202 | v16 * 0x200000 & 0x200000 | v17 * 0x40000 & 0x40000;
        v7 = v8;
        v6 = v18;
        v5 = v19;
        v4 = v20;
        v3 = &v8;
        v2 = /* unsupported instruction */;
        v1 = v21;
        v0 = v22;
        v24 = _ccall(0, 6, v19, v19, 0);
        v25 = v19;
        if (!((char)v24))
        {
            if (!(1))
                goto LABEL_103240e9;
LABEL_103240e9:
            if (0)
                goto LABEL_0x10324081;
            v28 = _ccall(2, 15, 3, 0, 0);
            if ((char)v28)
                goto LABEL_0x103240fa;
        }
        else
        {
            v28 = _ccall(2, 6, v25, v26, 0);
            if ((char)v28)
                goto LABEL_0x103240fa;
        }
    }
    else
    {
        v8 = v29;
        v7 = v13;
        v30 = _ccall(15, v14, 0, 0);
        v8 = v30 | 0x202 | v31 * 0x200000 & 0x200000 | v32 * 0x40000 & 0x40000;
        v6 = v8;
        v5 = v33;
        v4 = v34;
        v3 = &v8;
        v1 = v35;
        v0 = v36;
        if (!(1))
            goto LABEL_10324146;
LABEL_10324146:
        for (; (v37 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v37 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
        v38 = v2;
        v8 = v38 - 8;
        v7 = (int)v38[20];
    }
}
```

## `sub_103240f3` `0x103240f3`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103240f3(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324107` `0x10324107`

_21 bytes. (leaf/helper — see body)_

```c
int sub_10324107(void)
{
}
```

## `sub_1032410b` `0x1032410b`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032410b(void)
{
}
```

## `sub_1032410d` `0x1032410d`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1032410d(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324141` `0x10324141`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10324141(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324176` `0x10324176`

_84 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b0c4;
extern struct_0 *g_1038c8ac;

int sub_10324176(void)
{
    char *v10;  // eax
    int v11;  // eax
    unsigned int v20;  // 4103
    unsigned int v21;  // 4101
    unsigned int v22;  // 4101
    unsigned int v23;  // 4101
    unsigned int v24;  // 4101
    unsigned int v25;  // 4101
    unsigned int v26;  // 4101
    unsigned int v12;  // 4101
    unsigned int v13;  // ecx
    unsigned int v14;  // edx
    void* v15;  // ebx
    unsigned int v16;  // esi
    unsigned int v17;  // edi
    unsigned int v18;  // 4101
    void* v19;  // ebx
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    char *v2;  // [bp-0x1c]
    void* v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]
    unsigned int v9;  // [bp+0xffff4]

    *(v10) = *(v10) + *((char *)&v10);
    v7 = g_1038c8ac->field_0;
    v11 = g_1038b0c4(g_1038c8ac->field_0, v9);
    if (!v11)
    {
        v12 = _ccall(0, 15, v11, 0, 0);
    }
    else
    {
        v6 = v11;
        v5 = v13;
        v4 = v14;
        v3 = v15;
        v2 = &v7;
        v1 = v16;
        v0 = v17;
LABEL_103241ba:
        v18 = _ccall(0, 15, 0, 0, 0);
        if ((char)v18)
            goto LABEL_103241bc;
        else
            goto LABEL_103241bd;
        while (true)
        {
LABEL_103241bc:
            __unsupported_jumpkind_Ijk_NoDecode()
            while (true)
            {
LABEL_103241bd:
                v20 = _ccall(10, 15, 0, 0, 0);
                if (!((char)v20))
                {
                    __unsupported_jumpkind_Ijk_NoDecode()
LABEL_103241c2:
                    *((unsigned int *)&v19[859611675]) = (int)v19[859611675] + v13;
                    __debugbreak();
                }
                v21 = _ccall(8, 15, 0, 0, 0);
                if (!((char)v21))
                {
                    if (!(1))
                        goto LABEL_103241c2;
                    v22 = _ccall(10, 15, 0, 0, 0);
                    if (!((char)v22))
                    {
                        v23 = _ccall(0, 15, 0, 0, 0);
                        if ((char)v23)
                            break;
                        else
                            continue;
                    }
                    else
                    {
                        v24 = _ccall(8, 15, 0, 0, 0);
                        if ((char)v24)
                            goto LABEL_103241ba;
                        else
                            goto LABEL_0x103241c3;
                    }
                }
                else
                {
                    __unsupported_jumpkind_Ijk_NoDecode()
                    v25 = _ccall(8, 15, 0, 0, 0);
                    if ((char)v25)
                        goto LABEL_103241ba;
                    else
                        goto LABEL_0x103241c3;
                }
LABEL_103241ba:
                if ((v26 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v26))
                    break;
            }
        }
    }
}
```

## `sub_10324195` `0x10324195`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10324195(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103241b0` `0x103241b0`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103241b0(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103241d0` `0x103241d0`

_51 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a26a0;

unsigned int sub_103241d0(int a0)
{
    int v2;  // ecx
    unsigned int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = sub_10324210(a0, 0, v2, &v1);
    return (sub_10324210(a0, 0, v2, &v1) < 0 ? 4294967295 : *((int *)(*((int *)(g_103a26a0 + sub_10324210(a0, 0, v2, &v1) * 4)) + 4)));
}
```

## `sub_103241f0` `0x103241f0`

_2 bytes. (leaf/helper — see body)_

```c
void sub_103241f0(void)
{
}
```

## `sub_10324210` `0x10324210`

_151 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a26a0;
extern char g_103a2948;

int sub_10324210(unsigned int a0, char a1)
{
    int v0;  // [bp-0x10]
    int i;  // [bp-0xc]
    int v2;  // [bp-0x8]

    i = 0;
    v2 = *((int *)&g_103a2948);
    while (i < v2)
    {
        v0 = (v2 - i) / 2 + i;
        if (a0 > *((int *)*((int *)(g_103a26a0 + v0 * 4))))
            i = v0 + 1;
        else
            v2 = v0;
    }
    if (i < *((int *)&g_103a2948) && a0 == *((int *)*((int *)(g_103a26a0 + i * 4))))
    {
        if (a1)
            return -1;
        return i;
    }
    if (!a1)
        return -1;
    return i;
}
```

## `sub_1032428e` `0x1032428e`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032428e(void)
{
    sub_10324295();
    return;
}
```

## `sub_10324295` `0x10324295`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10324295(void)
{
}
```

## `sub_103242a4` `0x103242a4`

_2 bytes. (leaf/helper — see body)_

```c
void sub_103242a4(void)
{
}
```

## `sub_103242b0` `0x103242b0`

_358 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern unsigned int g_103a26a0;
extern unsigned int g_103a2948;
extern unsigned int g_103a294c;

int sub_103242b0(unsigned int a0, unsigned int a1)
{
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    unsigned short v14;  // fs
    unsigned long v15;  // 4139
    unsigned long v16;  // 4153
    unsigned int v17;  // eax
    unsigned int v18;  // edx
    unsigned int v19;  // 4123
    unsigned long v20;  // 4113
    unsigned int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x2c]
    unsigned int *v2;  // [bp-0x28]
    unsigned int v3;  // [bp-0x24]
    unsigned int v4;  // [bp-0x20]
    unsigned int v5;  // [bp-0x1c]
    unsigned int v6;  // [bp-0x18]
    unsigned int idx;  // [bp-0x14]
    unsigned int v8;  // [bp-0x10]
    unsigned int v9;  // [bp-0xc]
    unsigned int v10;  // [bp-0x8]
    char v11;  // [bp-0x4]

    v10 = 4294967295;
    v9 = sub_1036b977;
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    v8 = *((int *)v15);
    v0 = g_1038e180 ^ &v11;
    v16 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v16) = &v8;
    v17 = sub_10324210(a0, 1);
    idx = v17;
    if (idx >= 0)
    {
        if (g_103a2948 == g_103a294c)
        {
            v18 = g_103a294c;
            g_103a294c = v18 * 2;
            v19 = _ccall(4, 24, v18 * 2, v18, 0);
            if ((char)v19)
                g_103a294c = 0x100;
            v6 = g_103a26a0;
            v5 = sub_1034fef0(-((g_103a294c >= 0x20000000 ? 1 : 0) & 1) | g_103a294c * 4);
            g_103a26a0 = v5;
            sub_10350b50(g_103a26a0, v6, g_103a2948 * 4);
            v4 = v6;
            sub_10350eb5(v4);
        }
        sub_10350ec0(g_103a26a0 + idx * 4 + 4, g_103a26a0 + idx * 4, (g_103a2948 - idx) * 4);
        v2 = sub_10350a53(8);
        v10 = 0;
        v1 = (!v2 ? NULL : sub_1031b260(v2, a0, a1));
        v3 = v1;
        v10 = 4294967295;
        v17 = v3;
        *((unsigned int *)(g_103a26a0 + idx * 4)) = v17;
        g_103a2948 = g_103a2948 + 1;
    }
    v20 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int *)v20) = v8;
    return v17;
}
```

## `sub_10324420` `0x10324420`

_122 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a26a0;
extern unsigned int g_103a2948;

int sub_10324420(unsigned int a0)
{
    unsigned int v0;  // [bp-0xc]
    int idx;  // [bp-0x8]

    idx = sub_10324210(a0, 1);
    if (idx < 0)
        return idx;
    v0 = *((int *)(g_103a26a0 + idx * 4));
    sub_10350abd(v0);
    g_103a2948 = g_103a2948 - 1;
    return sub_10350ec0(g_103a26a0 + idx * 4, g_103a26a0 + idx * 4 + 4, (g_103a2948 - idx) * 4);
}
```

## `sub_103244a0` `0x103244a0`

_312 bytes. refs "kernel32.dll", "SetProcessShutdownParameters"_

```c
typedef struct struct_2 {
    char field_0;
} struct_2;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b078;
extern struct_0 *g_1038b080;
extern struct_0 *g_1038b1c0;
extern unsigned int g_1038c7f4;
extern unsigned int g_1038c808;
extern unsigned int g_1038c834;
extern unsigned int g_1038e180;
extern char g_103a2905;
extern char g_103a2909;

void sub_103244a0(unsigned int a0, unsigned int a1)
{
    int v18;  // esi
    unsigned int *v19;  // eax
    unsigned int v28;  // edx
    unsigned int v29;  // ebx
    unsigned int v30;  // edi
    unsigned int v31;  // 4110
    unsigned int v32;  // 4101
    unsigned int v35;  // eax
    unsigned int v36;  // 4101
    unsigned int v37;  // 4103
    unsigned int *v20;  // ecx
    unsigned int v38;  // 4101
    unsigned int v39;  // 4101
    unsigned int v40;  // 4101
    unsigned int v41;  // 4101
    unsigned int v42;  // 4101
    unsigned int v43;  // 4101
    unsigned int v21;  // cc_op
    unsigned int v22;  // cc_dep1
    unsigned int v23;  // cc_dep2
    unsigned int v24;  // cc_ndep
    unsigned int v25;  // 4193
    unsigned int v26;  // id
    unsigned int v27;  // ac
    unsigned int v0;  // [bp-0x250]
    int v1;  // [bp-0x24c]
    char *v2;  // [bp-0x248]
    char *v3;  // [bp-0x244], Other Possible Types: struct_2 **
    unsigned int v4;  // [bp-0x240]
    unsigned int v5;  // [bp-0x23c]
    unsigned int *v6;  // [bp-0x238]
    unsigned int *v7;  // [bp-0x234], Other Possible Types: unsigned int
    char *v8;  // [bp-0x230], Other Possible Types: unsigned int *, unsigned int
    unsigned int v9;  // [bp-0xd4]
    unsigned int v10;  // [bp-0xd0]
    unsigned int v11;  // [bp-0xcc]
    unsigned int v12;  // [bp-0xc4]
    unsigned int v13;  // [bp-0x3c]
    unsigned int v14;  // [bp-0x18]
    unsigned int *v15;  // [bp-0x10]
    char v16;  // [bp-0x4]

    v13 = g_1038e180 ^ &v16;
    sub_1033de00(0, 3, v18);
    v14 = g_1038b080("kernel32.dll");
    v19 = g_1038b078(v14, "SetProcessShutdownParameters");
    v15 = v19;
    if (v15)
        v19 = v15(0x100, 1);
    v8 = v20;
    v7 = v19;
    v25 = _ccall(v21, v22, v23, v24);
    v8 = v25 | 0x202 | v26 * 0x200000 & 0x200000 | v27 * 0x40000 & 0x40000;
    v6 = v20;
    v5 = v28;
    v4 = v29;
    v3 = &v8;
    v2 = &v16;
    v1 = v18;
    v0 = v30;
    if (!(1))
        goto LABEL_10324517;
LABEL_10324517:
    for (; (v31 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v31 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
    v9 = 148;
    v8 = &v9;
    g_1038b1c0(&v9);
    v32 = _ccall(0, v21, v22, v23, v24);
    if (v12 == 2)
    {
        g_103a2909 = 1;
    }
    else
    {
        if (v10 == 4 && v11 >= 90)
            sub_103255a0();
        sub_10325680();
    }
    __unsupported_jumpkind_Ijk_NoDecode()
    *(v20) = *(v20) | &v16;
    if (!v28)
        __unsupported_jumpkind_Ijk_Privileged()
    v35 = g_1038c7f4 ^ g_1038c834 ^ g_1038c808;
    if (((char)v35 & 4))
        g_103a2905 = 1;
    v7 = v35 & 4;
    v6 = v20;
    v5 = v28;
    v3 = &v8;
    v2 = &v16;
LABEL_103245d6:
    v36 = _ccall(0, 15, 0, 0, 0);
    if ((char)v36)
        goto LABEL_103245d8;
    else
        goto LABEL_103245d9;
    while (true)
    {
LABEL_103245d8:
        __unsupported_jumpkind_Ijk_NoDecode()
        while (true)
        {
LABEL_103245d9:
            v37 = _ccall(10, 15, 0, 0, 0);
            if (!((char)v37))
            {
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_103245de:
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_103245df:
            }
            v38 = _ccall(8, 15, 0, 0, 0);
            if (!((char)v38))
            {
                if (!(1))
                    goto LABEL_103245de;
                v39 = _ccall(10, 15, 0, 0, 0);
                if (!((char)v39))
                {
                    v40 = _ccall(0, 15, 0, 0, 0);
                    if ((char)v40)
                        break;
                    else
                        continue;
                }
                v41 = _ccall(8, 15, 0, 0, 0);
                if ((char)v41)
                    goto LABEL_103245d6;
                goto LABEL_103245df;
            }
            __unsupported_jumpkind_Ijk_NoDecode()
            v42 = _ccall(8, 15, 0, 0, 0);
            if (!((char)v42))
                goto LABEL_103245df;
LABEL_103245d6:
            if ((v43 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v43))
                break;
        }
    }
}
```

## `sub_10324512` `0x10324512`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10324512(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324519` `0x10324519`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10324519(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324559` `0x10324559`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10324559(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324598` `0x10324598`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10324598(void)
{
    __unsupported_jumpkind_Ijk_Privileged()
}
```

## `sub_103245cc` `0x103245cc`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103245cc(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103245e5` `0x103245e5`

_32 bytes. (leaf/helper — see body)_

```c
void sub_103245e5(unsigned int a0, unsigned int a1)
{
    unsigned int v23;  // cc_op
    unsigned int v24;  // cc_dep1
    unsigned int v25;  // cc_dep2
    unsigned int v26;  // cc_ndep

    if (!(1))
        goto LABEL_103245f5;
LABEL_103245f5:
    __unsupported_jumpkind_Ijk_NoDecode()
    __unsupported_jumpkind_Ijk_NoDecode()
    v23 = 15;
    v24 = 3;
    v25 = 0;
    v26 = 0;
}
```

## `sub_103245ff` `0x103245ff`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103245ff(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324607` `0x10324607`

_6 bytes. (leaf/helper — see body)_

```c
void sub_10324607(void)
{
}
```

## `sub_10324613` `0x10324613`

_200 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern unsigned int g_1038c7f4;
extern unsigned int g_1038c808;
extern unsigned int g_1038c834;
extern unsigned int g_1038c83c;
extern char g_103a2907;
extern unsigned int g_103a2914;

int sub_10324613(void)
{
    unsigned int v12;  // 4097
    unsigned int v13;  // eax
    unsigned int v22;  // 4101
    char v23;  // al
    unsigned int v24;  // edx
    unsigned int v25;  // ecx
    unsigned int v26;  // eax
    unsigned int v27;  // 4209
    unsigned int v28;  // 4110
    unsigned int v14;  // ecx
    unsigned int v15;  // 4101
    unsigned int v16;  // 4103
    unsigned int v17;  // 4101
    unsigned int v18;  // 4101
    unsigned int v19;  // 4101
    unsigned int v20;  // 4101
    unsigned int v21;  // 4101
    unsigned int v0;  // [bp-0x4]
    unsigned int v1;  // [bp+0x0]
    unsigned int v2;  // [bp+0x4]
    char *v3;  // [bp+0x8], Other Possible Types: unsigned int
    unsigned int v4;  // [bp+0xc]
    unsigned int v5;  // [bp+0xc]
    char *v6;  // [bp+0x10], Other Possible Types: unsigned int
    unsigned int v7;  // [bp+0x14]
    unsigned int v8;  // [bp+0x18]
    unsigned int v9;  // [bp+0x1c]
    unsigned int v10;  // [bp+0x20]
    char v11;  // [bp+0x24]

    v12 = v10;
    v13 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v14 = g_1038c7f4 ^ g_1038c834 ^ g_1038c808;
    if (((unsigned short)v14 & 0x200))
        g_103a2907 = 1;
    v10 = v13 * 0x1000000 | v13 * 0x100 & 0xff0000 | v13 >> 8 & 0xff00 | v13 >> 24 & 0xff;
    v9 = v14 & 0x200;
    v8 = v7;
    v7 = v6;
    v6 = &v11;
    v4 = v3;
    v3 = v2;
    v2 = v1;
LABEL_10324661:
    v15 = _ccall(0, 15, 0, 0, 0);
    if ((char)v15)
        goto LABEL_10324663;
    else
        goto LABEL_10324664;
    while (true)
    {
LABEL_10324663:
        __unsupported_jumpkind_Ijk_NoDecode()
        while (true)
        {
LABEL_10324664:
            v16 = _ccall(10, 15, 0, 0, 0);
            if ((char)v16)
            {
                v17 = _ccall(8, 15, 0, 0, 0);
                if (!((char)v17))
                {
                    if (!(1))
                        goto LABEL_10324669;
                    v18 = _ccall(10, 15, 0, 0, 0);
                    if (!((char)v18))
                    {
                        v19 = _ccall(0, 15, 0, 0, 0);
                        if ((char)v19)
                            break;
                        else
                            continue;
                    }
                    v20 = _ccall(8, 15, 0, 0, 0);
                    if ((char)v20)
                        goto LABEL_10324661;
                    goto LABEL_1032466a;
                }
                __unsupported_jumpkind_Ijk_NoDecode()
                v21 = _ccall(8, 15, 0, 0, 0);
                if (!((char)v21))
                    goto LABEL_1032466a;
LABEL_10324661:
                if ((v22 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v22))
                    break;
            }
            else
            {
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_10324669:
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_1032466a:
                v23 = g_1038b050(0);
                v24 = g_1038c83c ^ g_1038c834;
                v26 = _INSERT(v23, 0, v23 + (char)v25);
                g_103a2914 = v26 + v24;
                v9 = v25;
                v8 = g_103a2914;
                v27 = _ccall(3, v26, v24, 0);
                v9 = v27 | 0x202 | ((char)(v12 >> 10) ? 4294967295 : 1) & 0x400 | ((char)(v12 >> 21) ? 1 : 0) * 0x200000 & 0x200000 | ((char)(v12 >> 18) ? 1 : 0) * 0x40000 & 0x40000;
                v7 = v9;
                v6 = v24;
                v5 = v7;
                v3 = &v9;
                v2 = v4;
                v1 = v3;
                v0 = v2;
                if (!(1))
                    goto LABEL_103246b3;
LABEL_103246b3:
                for (; (v28 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v28 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
                sub_103246e3(); /* do not return */
            }
        }
    }
}
```

## `sub_10324617` `0x10324617`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10324617(void)
{
}
```

## `sub_10324619` `0x10324619`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10324619(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324657` `0x10324657`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10324657(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103246ae` `0x103246ae`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103246ae(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103246b5` `0x103246b5`

_3 bytes. (leaf/helper — see body)_

```c
void sub_103246b5(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103246e3` `0x103246e3`

_142 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b03c;
extern unsigned int g_1038c800;
extern unsigned int g_1038c808;
extern unsigned int g_103a2928;

int sub_103246e3(void)
{
    unsigned int v11;  // eax
    unsigned int v12;  // eax
    unsigned int v21;  // ac
    unsigned int v22;  // edx
    unsigned int v23;  // ebx
    unsigned int v24;  // esi
    unsigned int v25;  // edi
    unsigned int v26;  // 4110
    unsigned int v27;  // eax
    unsigned int v28;  // eax
    unsigned int v13;  // cc_dep1
    unsigned int v14;  // cc_dep2
    unsigned int v15;  // 4101
    unsigned int v18;  // ecx
    unsigned int v19;  // 4150
    unsigned int v20;  // id
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    char *v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    unsigned int v7;  // [bp-0x4]
    unsigned int v9;  // [bp+0xfffd4]
    unsigned int v10;  // [bp+0x100000]

    v12 = (v11 ^ g_1038c808) + 0xfff;
    v13 = v12 >> 12;
    v14 = v12 >> 11;
    g_103a2928 = v12 >> 12;
    v15 = _ccall(0, 27, v13, v14, 0);
    v9 = 0;
    v10 = 4294967295;
    v7 = v18;
    v6 = g_103a2928;
    v19 = _ccall(27, v13, v14, 0);
    v7 = v19 | 0x202 | v20 * 0x200000 & 0x200000 | v21 * 0x40000 & 0x40000;
    v5 = v18;
    v4 = v22;
    v3 = v23;
    v2 = &v7;
    v1 = v24;
    v0 = v25;
    if (!(1))
        goto LABEL_10324736;
LABEL_10324736:
    for (; (v26 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v26 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
    v27 = sub_10320760(0);
    v28 = g_1038b03c();
    v7 = v27 ^ v28 ^ g_1038c800;
}
```

## `sub_103246fc` `0x103246fc`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103246fc(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324731` `0x10324731`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10324731(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324738` `0x10324738`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10324738(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032477c` `0x1032477c`

_42 bytes. (leaf/helper — see body)_

```c
void sub_1032477c(unsigned int a0, unsigned int a1)
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
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    unsigned int v6;  // [bp-0x4]

    v6 = sub_1033a4c0();
    v5 = v9;
    v4 = v10;
    v3 = v11;
    v2 = /* unsupported instruction */;
    v1 = v12;
    v0 = v13;
LABEL_1032479d:
    v14 = _ccall(0, 15, 0, 0, 0);
    if ((char)v14)
        goto LABEL_1032479f;
    else
        goto LABEL_103247a0;
    while (true)
    {
LABEL_1032479f:
        __unsupported_jumpkind_Ijk_NoDecode()
        while (true)
        {
LABEL_103247a0:
            v15 = _ccall(10, 15, 0, 0, 0);
            if (!((char)v15))
            {
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_103247a5:
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_103247a6:
            }
            v16 = _ccall(8, 15, 0, 0, 0);
            if (!((char)v16))
            {
                if (!(1))
                    goto LABEL_103247a5;
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
                    goto LABEL_1032479d;
                goto LABEL_103247a6;
            }
            __unsupported_jumpkind_Ijk_NoDecode()
            v20 = _ccall(8, 15, 0, 0, 0);
            if (!((char)v20))
                goto LABEL_103247a6;
LABEL_1032479d:
            if ((v21 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v21))
                break;
        }
    }
}
```

## `sub_10324793` `0x10324793`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10324793(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103247ad` `0x103247ad`

_136 bytes. (leaf/helper — see body)_

```c
void sub_103247ad(int a0)
{
    unsigned int v10;  // d
    unsigned int v11;  // eax
    unsigned int v20;  // cc_dep2
    unsigned int v21;  // cc_ndep
    unsigned int v22;  // id
    unsigned int v23;  // ac
    unsigned int v24;  // ebx
    unsigned int v25;  // esi
    unsigned int v12;  // cc_op
    unsigned int v26;  // edi
    unsigned int v27;  // ecx
    unsigned int v28;  // 4193
    unsigned int v29;  // edx
    unsigned int v30;  // 4110
    unsigned int v31;  // 4097
    unsigned short v32;  // ax
    unsigned short v33;  // dx
    unsigned int v13;  // cc_dep1
    unsigned int v36;  // 4110
    unsigned int v37;  // 4104
    unsigned int v14;  // cc_dep2
    unsigned int v15;  // cc_ndep
    unsigned int v16;  // 4105
    unsigned int v17;  // 4101
    unsigned int v18;  // cc_op
    unsigned int v19;  // cc_dep1
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    char *v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    unsigned int v7;  // [bp-0x4]
    unsigned int v9;  // [bp+0xfffd4]

    v10 = 1;
    v11 = sub_102eb870(a0);
    v9 = v11;
    v16 = _ccall(0, v12, v13, v14, v15);
    if (!((char)v16))
    {
        v17 = _ccall(12, v12, v13, v14, v15);
        if ((char)v17)
        {
            __unsupported_jumpkind_Ijk_NoDecode()
            __unsupported_jumpkind_Ijk_Privileged()
        }
    }
    do
    {
        v7 = v27;
        v6 = v11;
        v28 = _ccall(v18, v19, v20, v21);
        v7 = v28 | 0x202 | v10 & 0x400 | v22 * 0x200000 & 0x200000 | v23 * 0x40000 & 0x40000;
        v5 = v7;
        v4 = v29;
        v3 = v24;
        v2 = &v7;
        v1 = v25;
        v0 = v26;
        if (!(1))
            goto LABEL_103247e7;
LABEL_103247e7:
        for (; (v30 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v30 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
        v25 = v1;
        v26 = v0;
        v31 = v7;
        v10 = ((char)(v31 >> 10) ? 4294967295 : 1);
        v22 = ((char)(v31 >> 21) ? 1 : 0);
        v23 = ((char)(v31 >> 18) ? 1 : 0);
        v32 = v4;
        v33 = v6;
        v7 = _INSERT(v32 CONCAT 0, 0, v33);
        v11 = v7;
        if ((v31 & 2261 & 1) != 1)
            goto LABEL_10324814;
LABEL_10324814:
        v36 = _ccall(0, v31 & 2261, 0, 0);
        v7 = v36 | 0x202 | v10 & 0x400 | v22 * 0x200000 & 0x200000 | v23 * 0x40000 & 0x40000;
        v6 = v11;
        v4 = _INSERT(v33 CONCAT 0, 0, v32);
        v2 = &v7;
        v1 = v25;
        v0 = v26;
        __unsupported_jumpkind_Ijk_NoDecode()
        v37 = _ccall(0, 6, v4, v4, 0);
        if ((char)v37)
            break;
        if (!(1))
            goto LABEL_10324821;
LABEL_10324821:
        v24 = 0;
        v18 = 15;
        v19 = 3;
        v20 = 0;
        v21 = 0;
    } while (false);
    __unsupported_jumpkind_Ijk_NoDecode()
    x86g_dirtyhelper_OUT(0x0<32>, Add(vvar_51{r8|4b}, 0x7410ebb9<32>), 0x4<32>)
    if (v11 + 1947265977 < 0)
        goto LABEL_0x10324832;
    else
        goto LABEL_0x1032482c;
}
```

## `sub_103247bb` `0x103247bb`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103247bb(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103247e2` `0x103247e2`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103247e2(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103247e9` `0x103247e9`

_3 bytes. (leaf/helper — see body)_

```c
void sub_103247e9(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032483f` `0x1032483f`

_84 bytes. (leaf/helper — see body)_

```c
int sub_1032483f(void)
{
    unsigned int v10;  // cc_dep1
    unsigned int v11;  // eax
    unsigned int v20;  // 4101
    unsigned int v21;  // 4101
    unsigned int v22;  // 4101
    unsigned int v12;  // 4119
    unsigned int v15;  // 4101
    unsigned int v16;  // 4103
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

    v10 = v8 & 2261;
    v11 = v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff;
    *((unsigned int *)&v2[232]) = 12;
    v12 = _ccall(0, 0, v10, 0, 0);
    *((unsigned int *)&v2[228]) = 0;
    v8 = v11 * 0x1000000 | v11 * 0x100 & 0xff0000 | v11 >> 8 & 0xff00 | v11 >> 24 & 0xff;
    v7 = ~(~(v6));
    v6 = v5;
    v5 = v4;
    v4 = &v9;
    v3 = v2;
    v2 = v1;
    v1 = v0;
LABEL_1032488b:
    v15 = _ccall(0, 15, 0, 0, 0);
    if ((char)v15)
        goto LABEL_1032488d;
    else
        goto LABEL_1032488e;
    while (true)
    {
LABEL_1032488d:
        __unsupported_jumpkind_Ijk_NoDecode()
        while (true)
        {
LABEL_1032488e:
            v16 = _ccall(10, 15, 0, 0, 0);
            if (!((char)v16))
            {
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_10324893:
            }
            v17 = _ccall(8, 15, 0, 0, 0);
            if (!((char)v17))
            {
                if (!(1))
                    goto LABEL_10324893;
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
                    if ((char)v20)
                        goto LABEL_1032488b;
                    else
                        goto LABEL_0x10324894;
                }
            }
            else
            {
                __unsupported_jumpkind_Ijk_NoDecode()
                v21 = _ccall(8, 15, 0, 0, 0);
                if ((char)v21)
                    goto LABEL_1032488b;
                else
                    goto LABEL_0x10324894;
            }
LABEL_1032488b:
            if ((v22 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v22))
                break;
        }
    }
}
```

## `sub_10324843` `0x10324843`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10324843(void)
{
}
```

## `sub_10324845` `0x10324845`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10324845(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324860` `0x10324860`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10324860(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324881` `0x10324881`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10324881(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103248a4` `0x103248a4`

_38 bytes. (leaf/helper — see body)_

```c
void sub_103248a4(unsigned int a0, unsigned int a1)
{
    unsigned int v23;  // cc_op
    unsigned int v24;  // cc_dep1
    unsigned int v25;  // cc_dep2
    unsigned int v26;  // cc_ndep

    if (!(1))
        goto LABEL_103248b4;
LABEL_103248b4:
    v23 = 15;
    v24 = 3;
    v25 = 0;
    v26 = 0;
}
```

## `sub_103248be` `0x103248be`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103248be(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103248d2` `0x103248d2`

_105 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b0fc;
extern struct_0 *g_1038b100;

int sub_103248d2(void)
{
    void* v1;  // [bp+0x8]

    *((unsigned int *)&v1[4]) = g_1038b100(4294967295, v1 - 232, 4, 0, 0x1000, 0);
    if ((int)v1[4])
    {
        *((unsigned int *)&v1[216]) = g_1038b0fc();
        *((unsigned int *)&v1[220]) = 0;
        sub_1032492f(0, 1, 2); /* do not return */
    }
    sub_10351225();
    return;
}
```

