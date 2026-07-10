# elfbot.dll decompiled — jiru 0x103248d6..0x103255a0

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_103248d6` `0x103248d6`

_2 bytes. (leaf/helper — see body)_

```c
void sub_103248d6(void)
{
}
```

## `sub_103248d8` `0x103248d8`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103248d8(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1032492f` `0x1032492f`

_305 bytes. refs "_RS"_

```c
typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    char padding_c[20];
    unsigned int field_20;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b064;
extern struct_0 *g_1038b0f4;
extern struct_0 *g_1038b0f8;
extern struct_0 *g_1038b1c8;
extern unsigned int g_1038c7e4;
extern unsigned int g_1038c7fc;
extern unsigned int g_1038c818;
extern unsigned int g_1038c848;
extern unsigned int g_1038c85c;
extern char g_103a22d4;
extern struct_1 *g_103a2924;

int sub_1032492f(void)
{
    unsigned int v16;  // edx
    unsigned int v17;  // eax
    unsigned int v26;  // ebx
    unsigned int v27;  // esi
    unsigned int v28;  // edi
    unsigned int v29;  // 4110
    unsigned int v18;  // ecx
    unsigned int v19;  // cc_op
    unsigned int v20;  // cc_dep1
    unsigned int v21;  // cc_dep2
    unsigned int v22;  // cc_ndep
    unsigned int v23;  // 4193
    unsigned int v24;  // id
    unsigned int v25;  // ac
    unsigned int v0;  // [bp-0x50]
    unsigned int v1;  // [bp-0x4c]
    unsigned int v2;  // [bp-0x48]
    char *v3;  // [bp-0x44]
    unsigned int v4;  // [bp-0x40]
    unsigned int v5;  // [bp-0x3c]
    unsigned int v6;  // [bp-0x38]
    unsigned int v7;  // [bp-0x34]
    unsigned int v8;  // [bp-0x30]
    unsigned int v10;  // [bp+0xffdf4]
    unsigned int v11;  // [bp+0xfff28]
    unsigned int v12;  // [bp+0xfff2c]
    unsigned int v13;  // [bp+0xfffd4]
    int v14;  // [bp+0x100000]

    g_1038b0f8(v12, v12, v12, v16);
    g_103a2924 = g_1038b0f4(v14, 2, 0, 0, 0x1000);
    if (g_103a22d4)
        v10 = sub_102eb870(/* unsupported instruction */ - 492);
    else
        v10 = v13;
    g_103a2924->field_0 = v10 ^ g_1038c7fc ^ g_1038c818 ^ g_1038c7e4 ^ g_1038c848 ^ g_1038c85c;
    g_103a2924->field_4 = v11;
    v17 = g_1038b1c8();
    g_103a2924->field_8 = v17;
    g_103a2924->field_20 = 0;
    sub_10353127(/* unsupported instruction */ - 488, "%u", v14);
    v8 = v18;
    v7 = g_1038b064("_RS", /* unsupported instruction */ - 488);
    v23 = _ccall(v19, v20, v21, v22);
    v8 = v23 | 0x202 | v24 * 0x200000 & 0x200000 | v25 * 0x40000 & 0x40000;
    v6 = v18;
    v5 = v16;
    v4 = v26;
    v3 = &v8;
    v2 = /* unsupported instruction */;
    v1 = v27;
    v0 = v28;
    if (!(1))
        goto LABEL_10324a34;
LABEL_10324a34:
    for (; (v29 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v29 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
}
```

## `sub_10324a2f` `0x10324a2f`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10324a2f(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324a36` `0x10324a36`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10324a36(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324a64` `0x10324a64`

_301 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a290c;
extern unsigned int g_103a2910;
extern char g_103a2928;
extern unsigned int g_103a2930;
extern unsigned int g_103a2934;
extern unsigned int g_103a2938;
extern unsigned int g_103a293c;

int sub_10324a64(void)
{
    char v17;  // bh
    char v18;  // dh
    unsigned int v27;  // eax
    unsigned int v28;  // 4110
    unsigned int v29;  // id
    unsigned int v30;  // ac
    unsigned int v32;  // esi
    unsigned int v33;  // cc_op
    unsigned int v34;  // 4104
    unsigned int v35;  // cc_dep1
    unsigned int v36;  // cc_dep2
    unsigned int v19;  // ebx
    unsigned int v40;  // 4101
    unsigned int v20;  // ecx
    unsigned int v21;  // edi
    unsigned int v22;  // edi
    unsigned int v23;  // eax
    unsigned int v24;  // eax
    unsigned int v25;  // eax
    unsigned int v26;  // eax
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    char *v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]
    unsigned int v8;  // [bp-0x4]
    unsigned int v9;  // [bp+0x4]
    unsigned int v10;  // [bp+0xffdf8]
    unsigned int v11;  // [bp+0xffdfc]
    unsigned int v12;  // [bp+0xffe00]
    unsigned int v13;  // [bp+0xffe04]
    unsigned int v14;  // [bp+0xffe08]
    unsigned int v15;  // [bp+0xffe0c]

    v19 = _INSERT(0, 1, v17 + v18);
    if (v20 == 1)
    {
        v22 = v21 * 0x2000000;
        v24 = sub_1034fef0(v20 - 1 | v23);
    }
    v15 = v24;
    g_103a2930 = v15;
    v25 = *((int *)&g_103a2928) * 16;
    v14 = sub_1034fef0(-((v25 >= 0x20000000 ? 1 : 0) & 1) | v25 * 4);
    g_103a2910 = v14;
    v13 = sub_1034fef0(-((*((int *)&g_103a2928) >= 0x20000000 ? 1 : 0) & 1) | *((int *)&g_103a2928) * 4);
    g_103a2934 = v13;
    v12 = sub_1034fef0(-((*((int *)&g_103a2928) >= 0x20000000 ? 1 : 0) & 1) | *((int *)&g_103a2928) * 4);
    v26 = v12;
    do
    {
        g_103a2938 = v26;
        v11 = sub_1034fef0(0x1000);
        g_103a293c = v11;
        v10 = sub_1034fef0(-((*((int *)&g_103a2928) >= 0x20000000 ? 1 : 0) & 1) | *((int *)&g_103a2928) * 4);
        v27 = v10;
        g_103a290c = v27;
        v8 = v27;
        v26 = v8;
        if (&v9 >= NULL)
            goto LABEL_10324b6e;
LABEL_10324b6e:
        v28 = _ccall(3, &v8, 4, 0);
        v8 = v28 | 0x202 | v29 * 0x200000 & 0x200000 | v30 * 0x40000 & 0x40000;
        v7 = v26;
        v6 = v20;
        v5 = v18;
        v4 = v19;
        v3 = &v8;
        v2 = /* unsupported instruction */;
        v1 = v32;
        v0 = v22;
        v33 = 6;
        v34 = _ccall(0, 6, (unsigned int)v18, (unsigned int)v18, 0);
        v35 = v18;
        v36 = v18;
        if ((char)v34)
            break;
        if (!(1))
            goto LABEL_10324b7b;
LABEL_10324b7b:
        v19 = 0;
        v33 = 15;
        v35 = 3;
        v36 = 0;
    } while (false);
    v40 = _ccall(2, v33, v35, v36, 0);
    if ((char)v40)
        goto LABEL_0x10324b8c;
}
```

## `sub_10324b85` `0x10324b85`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10324b85(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324b99` `0x10324b99`

_165 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e4;
extern unsigned int g_1038c7fc;
extern unsigned int g_1038c818;
extern unsigned int g_1038c848;
extern unsigned int g_1038c85c;
extern unsigned int g_103a2910;
extern unsigned int g_103a2928;

int sub_10324b99(void)
{
    char v8;  // bl
    void* v9;  // ebp
    unsigned int v18;  // 4101
    unsigned int v19;  // 4101
    unsigned int v20;  // 4101
    unsigned int v21;  // 4101
    unsigned int v22;  // 4101
    unsigned int v23;  // 4101
    unsigned int v10;  // ecx
    void* v11;  // ebx
    unsigned int v12;  // 4106
    unsigned int v13;  // eax
    unsigned int v14;  // eax
    unsigned int v15;  // edx
    unsigned int v16;  // 4101
    unsigned int v17;  // 4103
    void* v1;  // [bp+0x8]
    char *v2;  // [bp+0xc]
    void* v3;  // [bp+0x10], Other Possible Types: unsigned int
    unsigned int v4;  // [bp+0x14]
    unsigned int v5;  // [bp+0x18]
    unsigned int v6;  // [bp+0x1c]
    unsigned int v7;  // [bp+0x20]

    v8 = v3;
    v9 = v1;
    v7 = g_1038c818 ^ (int)v9[48];
    sub_1033a4c0(g_1038c818 ^ (int)v9[48]);
    __unsupported_jumpkind_Ijk_NoDecode()
    v11 = _INSERT(v8, 0, v8 + *((char *)((void*)&v10 + 1)));
    v12 = _ccall(10, 1, (unsigned int)v8, (unsigned int)*((char *)((void*)&v10 + 1)), 0);
    if ((char)v12)
        *((unsigned int *)&v11[1786183230]) = (int)v11[1786183230] + 1;
    v13 = g_103a2928 * 16;
    if ((int)v9[496] < v13)
    {
        v14 = sub_102eb870(v9 - 32);
        *((unsigned int *)(g_103a2910 + (int)v9[496] * 4)) = v14 ^ g_1038c7fc ^ g_1038c818 ^ g_1038c7e4 ^ g_1038c848 ^ g_1038c85c;
    }
    v6 = v13;
    v5 = v10;
    v4 = v15;
    v3 = v11;
    v2 = &v7;
    v1 = v9;
    v16 = _ccall(0, 15, 0, 0, 0);
    if ((char)v16)
        goto LABEL_10324c3c;
    else
        goto LABEL_10324c3d;
    while (true)
    {
LABEL_10324c3c:
        __unsupported_jumpkind_Ijk_NoDecode()
        while (true)
        {
LABEL_10324c3d:
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

## `sub_10324b9d` `0x10324b9d`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10324b9d(void)
{
}
```

## `sub_10324b9f` `0x10324b9f`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10324b9f(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324bd6` `0x10324bd6`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10324bd6(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324c30` `0x10324c30`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10324c30(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324c49` `0x10324c49`

_16 bytes. (leaf/helper — see body)_

```c
int sub_10324c49(void)
{
    void* v1;  // eax

    *((unsigned int *)v1) = *((int *)v1) + 1;
    *((char *)v1) = *((char *)v1) + *((char *)&v1);
}
```

## `sub_10324c5a` `0x10324c5a`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10324c5a(unsigned int a0)
{
}
```

## `sub_10324c65` `0x10324c65`

_167 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a290c;
extern char g_103a2928;
extern unsigned int g_103a2930;
extern unsigned int g_103a2934;
extern unsigned int g_103a2938;

int sub_10324c65(void)
{
    int v11;  // ecx
    unsigned int v12;  // eax
    unsigned int v13;  // 4193
    unsigned int v14;  // id
    unsigned int v15;  // ac
    unsigned int v16;  // edx
    unsigned int v17;  // ebx
    unsigned int v18;  // esi
    unsigned int v19;  // edi
    unsigned int v20;  // 4124
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    char *v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    int v7;  // [bp-0x4]
    unsigned int v8;  // [bp-0x4]
    unsigned int idx;  // [bp+0xffe10]

    if (v11 < *((int *)&g_103a2928))
    {
        *((unsigned int *)(g_103a2930 + idx * 4)) = 4294967295;
        *((unsigned int *)(g_103a2934 + idx * 4)) = 0;
        *((unsigned int *)(g_103a2938 + idx * 4)) = 4294967295;
        *((unsigned int *)(g_103a290c + idx * 4)) = 0;
    }
    v7 = v11;
    v6 = v12;
    v13 = _ccall(6, v11, *((int *)&g_103a2928), 0);
    v8 = v13 | 0x202 | v14 * 0x200000 & 0x200000 | v15 * 0x40000 & 0x40000;
    v5 = v7;
    v4 = v16;
    v3 = v17;
    v2 = &v8;
    v1 = v18;
    v0 = v19;
    if (!(1))
        goto LABEL_10324ce0;
LABEL_10324ce0:
    for (; (__unsupported_jumpkind_Ijk_NoDecode()
, v20 = (unsigned int)_ccall(13, 144, 0, 0), ((char)((v20 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
    sub_10324d10(); /* do not return */
}
```

## `sub_10324cdb` `0x10324cdb`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10324cdb(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324ce2` `0x10324ce2`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10324ce2(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324d10` `0x10324d10`

_127 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c8b4;
extern char g_103a2906;

int sub_10324d10(void)
{
    unsigned int v12;  // eax
    unsigned int v19;  // esi
    unsigned int v20;  // edi
    unsigned int v21;  // cc_op
    unsigned int v22;  // 4104
    unsigned int v23;  // cc_dep1
    unsigned int v24;  // 4101
    unsigned int v25;  // 4101
    unsigned int v26;  // 4103
    unsigned int v27;  // 4101
    unsigned int v28;  // 4101
    unsigned int v29;  // 4101
    unsigned int v30;  // 4101
    unsigned int v31;  // 4101
    unsigned int v32;  // 4101
    unsigned int v34;  // 4101
    unsigned int v13;  // ecx
    unsigned int v14;  // ebx
    unsigned int v15;  // edx
    unsigned int v16;  // 4110
    unsigned int v17;  // id
    unsigned int v18;  // ac
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    char *v3;  // [bp-0x18], Other Possible Types: unsigned int
    char *v4;  // [bp-0x14], Other Possible Types: unsigned int
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]
    unsigned int v8;  // [bp-0x4]
    char v9;  // [bp+0x0]

    __unsupported_jumpkind_Ijk_NoDecode()
    while (true)
    {
        v15 = g_103a2906;
        if (!g_103a2906)
            break;
        v8 = v12;
        v12 = v8;
        if (g_103a2906 >= 0)
            goto LABEL_10324d6f;
LABEL_10324d6f:
        v16 = _ccall(15, (unsigned int)(char)g_103a2906, 0, 0);
        v8 = v16 | 0x202 | v17 * 0x200000 & 0x200000 | v18 * 0x40000 & 0x40000;
        v7 = v12;
        v6 = v13;
        v5 = g_103a2906;
        v4 = v14;
        v3 = &v8;
        v1 = v19;
        v0 = v20;
        v21 = 6;
        v22 = _ccall(0, 6, (unsigned int)(char)g_103a2906, (unsigned int)(char)g_103a2906, 0);
        v23 = v15;
        if (!((char)v22))
        {
            __unsupported_jumpkind_Ijk_NoDecode()
            v14 = 0;
            v21 = 15;
            v23 = 3;
            v15 = 0;
            v13 = 3;
            if (!(0))
                goto LABEL_10324d84;
        }
        else
        {
LABEL_10324d84:
            v34 = _ccall(2, v21, v23, v15, 0);
            if ((char)v34)
                goto LABEL_0x10324d8d;
        }
    }
    v24 = _ccall(0, 15, (unsigned int)(char)g_103a2906, 0, 0);
    if (g_1038c8b4 < 6)
        g_1038c8b4 = 6;
    v8 = v12;
    v7 = v13;
    v6 = 0;
    v5 = v14;
    v4 = &v9;
    v3 = /* unsupported instruction */;
    v2 = v19;
    v1 = v20;
LABEL_10324d5b:
    v25 = _ccall(0, 15, 0, 0, 0);
    if ((char)v25)
        goto LABEL_10324d5d;
    else
        goto LABEL_10324d5e;
    while (true)
    {
LABEL_10324d5d:
        __unsupported_jumpkind_Ijk_NoDecode()
        while (true)
        {
LABEL_10324d5e:
            v26 = _ccall(10, 15, 0, 0, 0);
            if (!((char)v26))
            {
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_10324d63:
            }
            v27 = _ccall(8, 15, 0, 0, 0);
            if (!((char)v27))
            {
                if (!(1))
                    goto LABEL_10324d63;
                v28 = _ccall(10, 15, 0, 0, 0);
                if (!((char)v28))
                {
                    v29 = _ccall(0, 15, 0, 0, 0);
                    if ((char)v29)
                        break;
                    else
                        continue;
                }
                else
                {
                    v30 = _ccall(8, 15, 0, 0, 0);
                    if ((char)v30)
                        goto LABEL_10324d5b;
                    else
                        goto LABEL_0x10324d64;
                }
            }
            else
            {
                __unsupported_jumpkind_Ijk_NoDecode()
                v31 = _ccall(8, 15, 0, 0, 0);
                if ((char)v31)
                    goto LABEL_10324d5b;
                else
                    goto LABEL_0x10324d64;
            }
LABEL_10324d5b:
            if ((v32 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v32))
                break;
        }
    }
}
```

## `sub_10324d27` `0x10324d27`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10324d27(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324d51` `0x10324d51`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10324d51(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324d86` `0x10324d86`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10324d86(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324d9a` `0x10324d9a`

_296 bytes. refs "Kernel32", "OutputDebugStringA", "OutputDebugStringW"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b078;
extern struct_0 *g_1038b080;
extern unsigned int g_1038c808;
extern unsigned int g_1038c814;
extern unsigned int g_1038c834;
extern int g_1038c8b4;

int sub_10324d9a(void)
{
    void* v13;  // ebp
    unsigned int v14;  // 4097
    unsigned int v23;  // 4098
    unsigned int v24;  // eax
    unsigned int v25;  // ecx
    unsigned int v26;  // 4207
    unsigned int v27;  // 4110
    int v15;  // cc_dep1
    unsigned int v16;  // 4101
    unsigned int v17;  // 4101
    char v18;  // al
    int v19;  // eax
    unsigned int v20;  // eax
    unsigned int v21;  // eax
    unsigned int idx[14];  // edx
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    void* v2;  // [bp-0x18]
    char *v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5[14];  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    unsigned int v7;  // [bp-0x4]
    unsigned int v8;  // [bp+0x0]
    unsigned int v9;  // [bp+0x4]
    void* v10;  // [bp+0x8]
    unsigned int v11;  // [bp+0x10]
    unsigned int v12;  // [bp+0x20]

    v13 = v10;
    v14 = v12;
    v15 = g_1038c8b4;
    if (g_1038c8b4 < 18)
    {
        g_1038c8b4 = 18;
        v16 = _ccall(0, 6, v15, 18, 0);
        if ((char)v16 || v15 < 18 && v15 != 18)
            goto LABEL_10324dc7;
    }
    else
    {
        v17 = _ccall(0, 6, v15, 18, 0);
        if ((char)v17 || v15 < 18 && v15 != 18)
LABEL_10324dc7:
    }
    *((unsigned int *)&v13[52]) = g_1038b080("Kernel32");
    *((unsigned int *)&v13[28]) = g_1038b078((int)v13[52], "OutputDebugStringA");
    *((unsigned int *)&v13[36]) = g_1038b078((int)v13[52], "OutputDebugStringW");
    if ((((char)g_1038c814 ^ (char)g_1038c834 ^ (char)g_1038c808) & 2))
        v18 = sub_103118e0();
    v19 = _INSERT(v18 CONCAT 0, 0, (char)v13[8]);
    if ((char)sub_10325310(v19))
    {
        *((unsigned int *)&v13[212]) = g_1038b050(0);
        *((int *)&v13[44]) = (int)v13[212] + *((int *)((int)v13[212] + 60));
        v20 = g_1038b050(0);
        *((unsigned int *)&v13[8]) = v20 + *((int *)((int)v13[44] + 40));
        v21 = g_1038b050(0);
        idx = (int)v13[44];
        v23 = idx[13];
        v24 = v21 - idx[13];
        *((unsigned int *)&v13[24]) = v24;
        v8 = v25;
        v7 = v24;
        v26 = _ccall(6, v21, v23, 0);
        v8 = v26 | 0x202 | ((char)(v14 >> 10) ? 4294967295 : 1) & 0x400 | ((char)(v14 >> 21) ? 1 : 0) * 0x200000 & 0x200000 | ((char)(v14 >> 18) ? 1 : 0) * 0x40000 & 0x40000;
        v6 = v8;
        v5 = idx;
        v4 = v11;
        v3 = &v8;
        v2 = v13;
        v1 = v9;
        v0 = v8;
        if (!(1))
            goto LABEL_10324e9a;
LABEL_10324e9a:
        for (; (v27 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v27 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
        v8 = (int)v2[8];
        v7 = 1;
    }
}
```

## `sub_10324d9e` `0x10324d9e`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10324d9e(void)
{
}
```

## `sub_10324da0` `0x10324da0`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10324da0(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324dc4` `0x10324dc4`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10324dc4(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324e95` `0x10324e95`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10324e95(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324e9c` `0x10324e9c`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10324e9c(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324eca` `0x10324eca`

_107 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b0cc;
extern struct_1 *g_1038b0ec;
extern char g_1038b0f0;
extern struct_0 *g_1038c8ac;

int sub_10324eca(void)
{
    unsigned int v4;  // cc_op
    unsigned int v5;  // cc_dep1
    unsigned int v6;  // cc_dep2
    unsigned int v7;  // cc_ndep
    unsigned int v8;  // 4119
    void* v9;  // ecx
    char v10;  // dl
    unsigned int *v11;  // eax
    unsigned int v12;  // eax
    int v1;  // [bp+0xc]
    unsigned int v2;  // [bp+0xfffdc]
    int v3;  // [bp+0xffffc]

    v8 = _ccall(v4, v5, v6, v7);
    *((char *)&v9[24]) = (char)v9[24] + v10 + ((char)v8 & 1);
    *(v11) = *(v11) + (char *)v11;
    v1 = v3;
    sub_10325270(g_1038c8ac);
    g_1038b0cc(g_1038c8ac->field_4);
    v12 = &g_1038c8ac->padding_0[1];
    *((char *)&v9[1]) = (char)v9[1] | v10;
    v2 = &(&g_1038b0f0)[v12];
    g_1038b0ec(g_1038c8ac->field_4);
    sub_10325030(g_1038c8ac, 0, v3);
    sub_10324f35();
    return;
}
```

## `sub_10324f35` `0x10324f35`

_69 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
} struct_0;

extern struct_0 *g_1038c8ac;

void sub_10324f35(unsigned int a0)
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
    int v6;  // [bp-0x8], Other Possible Types: unsigned int
    int v7;  // [bp-0x4]
    unsigned int v8;  // [bp-0x4]
    char v10;  // [bp+0x8]
    unsigned int v11;  // [bp+0xffff4]

    v6 = g_1038c8ac->field_c;
    v12 = sub_103242b0(g_1038c8ac->field_c, a0);
    v11 = 0;
    v7 = v12;
    if (&v10 >= NULL)
        goto LABEL_10324f57;
LABEL_10324f57:
    v13 = _ccall(3, &v6, 8, 0);
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
            goto LABEL_10324f64;
LABEL_10324f64:
        if (0)
            goto LABEL_0x10324efc;
        v26 = _ccall(2, 15, 3, 0, 0);
        if ((char)v26)
            goto LABEL_0x10324f75;
    }
    else
    {
        v26 = _ccall(2, 6, v23, v24, 0);
        if ((char)v26)
            goto LABEL_0x10324f75;
    }
}
```

## `sub_10324f6e` `0x10324f6e`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10324f6e(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324f82` `0x10324f82`

_79 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[8];
    char field_8;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b02c;
extern struct_0 *g_1038b06c;
extern struct_0 *g_1038b128;
extern struct_0 *g_1038b1c4;
extern struct_0 *g_1038c8ac;
extern int g_103a26a4;

int sub_10324f82(void)
{
    unsigned int v2;  // eax
    struct_1 *v1;  // [bp+0x8]

    v2 = g_1038b02c(0, 0, sub_10320440, g_1038c8ac->field_0, 0, &v1[1].padding_0[7]);
    g_1038b128(v2);
    if (v1->field_8)
        g_1038b06c();
    g_1038b1c4(&g_103a26a4);
    sub_10324fd4(&g_103a26a4); /* do not return */
}
```

## `sub_10324f86` `0x10324f86`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10324f86(void)
{
}
```

## `sub_10324f88` `0x10324f88`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10324f88(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10324fd4` `0x10324fd4`

_10 bytes. (leaf/helper — see body)_

```c
int sub_10324fd4(unsigned int a0, int a1)
{
    int v1;  // [bp+0xfffec]

    sub_10320d90(v1, a1); /* do not return */
}
```

## `sub_10324fde` `0x10324fde`

_56 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b0e8;
extern struct_0 *g_1038b128;
extern unsigned int g_103a2924;

int sub_10324fde(void)
{
    char v2;  // al
    unsigned int v1;  // [bp+0x100000]

    if (v2)
    {
        g_1038b0e8(g_103a2924);
        g_103a2924 = 0;
        g_1038b128(v1);
        v1 = 4294967295;
    }
}
```

## `sub_10325030` `0x10325030`

_355 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b0c0;
extern struct_0 *g_1038b0e4;
extern unsigned int g_1038e180;
extern unsigned short g_10390338;
extern char g_1039033a;
extern char g_103a2974;

int sub_10325030(unsigned int *a0, char a1, int a2)
{
    unsigned int v20;  // 4101
    unsigned int v21;  // ecx
    unsigned int v30;  // 4110
    unsigned short v31;  // ax
    unsigned short v32;  // dx
    unsigned int v35;  // ecx
    unsigned int v36;  // cc_op
    unsigned int v37;  // cc_dep1
    unsigned int v38;  // cc_dep2
    unsigned int v39;  // cc_ndep
    unsigned int v22;  // eax
    unsigned int v40;  // 4193
    unsigned int v41;  // id
    unsigned int v42;  // ac
    unsigned int v43;  // edx
    unsigned int v44;  // ebx
    unsigned int v45;  // esi
    unsigned int v46;  // edi
    unsigned int v47;  // eax
    unsigned int v48;  // 4110
    unsigned int v23;  // 4196
    unsigned int v49;  // 4123
    unsigned int v50;  // 4110
    unsigned int v24;  // id
    unsigned int v51;  // cc_op
    unsigned int v52;  // 4104
    unsigned int v53;  // cc_dep1
    unsigned int v54;  // cc_dep2
    unsigned int v25;  // ac
    unsigned int v26;  // edx
    unsigned int v27;  // ebx
    unsigned int v28;  // esi
    unsigned int v56;  // 4101
    unsigned int v29;  // edi
    unsigned int v0;  // [bp-0x31c]
    unsigned int v1;  // [bp-0x318]
    char *v2;  // [bp-0x314]
    char *v3;  // [bp-0x310]
    unsigned int v4;  // [bp-0x30c]
    unsigned int v5;  // [bp-0x308]
    char *v6;  // [bp-0x304], Other Possible Types: unsigned int
    char *v7;  // [bp-0x300], Other Possible Types: unsigned int
    char *v8;  // [bp-0x2fc], Other Possible Types: unsigned int
    char *v9;  // [bp-0x2f8], Other Possible Types: unsigned int
    unsigned int v10;  // [bp-0x2f4]
    unsigned int v11;  // [bp-0x2f0]
    unsigned int v12;  // [bp-0x2ec]
    unsigned int v13;  // [bp-0x2e8]
    char v14;  // [bp-0x2e4], Other Possible Types: unsigned int
    unsigned int v15;  // [bp-0x10]
    unsigned short v16;  // [bp-0xc]
    char v17;  // [bp-0xa]
    char v18;  // [bp-0x8]
    char v19;  // [bp-0x4]

    v15 = g_1038e180 ^ &v19;
    v16 = g_10390338;
    v17 = g_1039033a;
    if (!a2)
    {
        v20 = _ccall(0, 6, a2, 0, 0);
        v13 = v21;
        v12 = sub_10350ad0(&v14, 0, 716);
        v22 = sub_10350ad0(&v14, 0, 716);
        v23 = _ccall(3, &v14, 12, 0);
        v13 = v23 | 0x202 | v24 * 0x200000 & 0x200000 | v25 * 0x40000 & 0x40000;
        v11 = v21;
        v10 = v26;
        v9 = v27;
        v8 = &v13;
        v7 = &v19;
        v6 = v28;
        v5 = v29;
        if (!(1))
            goto LABEL_103250a8;
LABEL_103250a8:
        for (; (v30 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v30 | 1) >> 6) & 1) != 1); __unsupported_jumpkind_Ijk_NoDecode()
);
        __unsupported_jumpkind_Ijk_NoDecode()
        __unsupported_jumpkind_Ijk_NoDecode()
        v31 = v26;
        v32 = sub_10350ad0(&v14, 0, 716);
        v14 = 65537;
        v13 = _INSERT(v31 CONCAT 0, 0, v32);
        v12 = v21;
        v11 = _INSERT(v32 CONCAT 0, 0, v31);
        v10 = v27;
        v9 = &v14;
        v8 = &v19;
        v7 = v6;
        v6 = v5;
        sub_103250d8(); /* do not return */
    }
    if (!a1)
    {
        v8 = g_1038b0e4(*(a0), a2, &g_103a2974, 2, &v18);
        v47 = v8;
        v49 = _ccall(2, v36, v37, v38, v39);
        if (!((char)v49))
            goto LABEL_1032521b;
LABEL_1032521b:
        v50 = _ccall(v36, v37, v38, v39);
        v8 = v50 | 0x202 | v41 * 0x200000 & 0x200000 | v42 * 0x40000 & 0x40000;
        v7 = v47;
        v6 = v35;
        v5 = v43;
        v4 = v44;
        v3 = &v8;
        v2 = &v19;
        v1 = v45;
        v0 = v46;
        v51 = 6;
        v52 = _ccall(0, 6, v43, v43, 0);
        v53 = v43;
        if (!((char)v52))
        {
            if (!(1))
                goto LABEL_10325228;
LABEL_10325228:
            v51 = 15;
            v53 = 3;
            v54 = 0;
            if (0)
                goto LABEL_103251c0;
        }
        v56 = _ccall(2, v51, v53, v54, 0);
        if ((char)v56)
            goto LABEL_0x10325239;
    }
    v8 = v35;
    v7 = g_1038b0c0(*(a0), a2, &g_103a2974, 2, &v18);
    v40 = _ccall(v36, v37, v38, v39);
    v8 = v40 | 0x202 | v41 * 0x200000 & 0x200000 | v42 * 0x40000 & 0x40000;
    v6 = v8;
    v5 = v43;
    v4 = v44;
    v3 = &v8;
    v2 = &v19;
    v1 = v45;
    v0 = v46;
    if (false)
    {
LABEL_103251a5:
    }
    else
    {
        if (!(1))
            goto LABEL_103251ac;
LABEL_103251ac:
        while (true)
        {
            v47 = 0;
            if (!((v48 = (unsigned int)_ccall(15, 0, 0, 0), ((char)((v48 | 1) >> 6) & 1) != 1)))
                break;
            __unsupported_jumpkind_Ijk_NoDecode()
        }
        __unsupported_jumpkind_Ijk_NoDecode()
LABEL_103251c0:
        if (v47)
            goto LABEL_103251a5;
        __unsupported_jumpkind_Ijk_NoDecode()
    }
    v8 = &v18;
    v7 = 2;
    v6 = &v16;
}
```

## `sub_10325066` `0x10325066`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10325066(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103250a3` `0x103250a3`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103250a3(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103250aa` `0x103250aa`

_3 bytes. (leaf/helper — see body)_

```c
void sub_103250aa(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103250d8` `0x103250d8`

_36 bytes. (leaf/helper — see body)_

```c
void sub_103250d8(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6)
{
    unsigned int v1;  // 4101
    unsigned int v2;  // 4103
    unsigned short v3;  // cs
    unsigned int v4;  // 4101
    unsigned int v5;  // 4101
    unsigned int v6;  // 4101
    unsigned int v7;  // 4101
    unsigned int v8;  // 4101
    unsigned int v9;  // 4101
    unsigned short v0;  // [bp-0x4]

LABEL_103250d8:
    v1 = _ccall(0, 15, 0, 0, 0);
    if ((char)v1)
        goto LABEL_103250f5;
    else
        goto LABEL_103250f6;
    while (true)
    {
LABEL_103250f5:
        __unsupported_jumpkind_Ijk_NoDecode()
        while (true)
        {
LABEL_103250f6:
            v2 = _ccall(10, 15, 0, 0, 0);
            if (!((char)v2))
            {
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_103250fb:
                __unsupported_jumpkind_Ijk_NoDecode()
LABEL_103250fc:
            }
            __unsupported_jumpkind_Ijk_NoDecode()
            v0 = v3;
            v4 = _ccall(8, 15, 0, 0, 0);
            if (!((char)v4))
            {
                if (!(1))
                    goto LABEL_103250fb;
                v5 = _ccall(10, 15, 0, 0, 0);
                if (!((char)v5))
                {
                    v6 = _ccall(0, 15, 0, 0, 0);
                    if ((char)v6)
                        break;
                    else
                        continue;
                }
                v7 = _ccall(8, 15, 0, 0, 0);
                if ((char)v7)
                    goto LABEL_103250d8;
                goto LABEL_103250fc;
            }
            __unsupported_jumpkind_Ijk_NoDecode()
            v8 = _ccall(8, 15, 0, 0, 0);
            if (!((char)v8))
                goto LABEL_103250fc;
            if ((v9 = (unsigned int)_ccall(0, 15, 0, 0, 0), (char)v9))
                break;
        }
    }
}
```

## `sub_103250e9` `0x103250e9`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103250e9(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10325111` `0x10325111`

_4 bytes. (leaf/helper — see body)_

```c
void sub_10325111(void)
{
    unsigned int v2;  // eax
    char *v3;  // edi
    unsigned int v0;  // [bp-0x4]

    v0 = v2;
    *(v3) = *(v3) >> 1 | *(v3) * 128;
}
```

## `sub_10325116` `0x10325116`

_38 bytes. (leaf/helper — see body)_

```c
void sub_10325116(unsigned int a0, unsigned int a1)
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
        goto LABEL_10325119;
LABEL_10325119:
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
            goto LABEL_10325126;
LABEL_10325126:
        if (0)
            goto LABEL_0x103250be;
        v26 = _ccall(2, 15, 3, 0, 0);
        if ((char)v26)
            goto LABEL_0x10325137;
    }
    else
    {
        v26 = _ccall(2, 6, v24, a1, 0);
        if ((char)v26)
            goto LABEL_0x10325137;
    }
}
```

## `sub_10325130` `0x10325130`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10325130(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10325144` `0x10325144`

_23 bytes. (leaf/helper — see body)_

```c
int sub_10325144(void)
{
    void* v1;  // [bp+0x8]

    *((int *)&v1[16]) = (int)v1[552];
}
```

## `sub_10325148` `0x10325148`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10325148(void)
{
}
```

## `sub_1032514a` `0x1032514a`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1032514a(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103251a7` `0x103251a7`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103251a7(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103251ae` `0x103251ae`

_3 bytes. (leaf/helper — see body)_

```c
void sub_103251ae(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_103251dc` `0x103251dc`

_43 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[369053960];
    char field_15ff5108;
} struct_0;

char sub_103251dc(char a0, void* a1)
{
    unsigned int v1;  // cc_op
    unsigned int v2;  // cc_dep1
    unsigned int v3;  // cc_dep2
    unsigned int v4;  // cc_ndep
    unsigned int v5;  // 4124
    struct_0 *idx;  // ebx
    char *v7;  // eax
    unsigned int v8;  // cc_dep1
    unsigned int v10;  // 4101

    v5 = _ccall(v1, v2, v3, v4);
    *((char *)&a1[117]) = (char)a1[117] + *((char *)&a1) + ((char)v5 & 1);
    idx->field_15ff5108 = idx->field_15ff5108 | a0;
    v7 = _INSERT(0, 0, x86g_dirtyhelper_IN(0xb0<32>, 0x1<32>));
    v8 = *(v7);
    v10 = _ccall(0, 4, v8, (unsigned int)*((char *)(void*)&a1), 0);
    return sub_10351225();
}
```

## `sub_103251f1` `0x103251f1`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103251f1(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10325232` `0x10325232`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10325232(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10325246` `0x10325246`

_14 bytes. (leaf/helper — see body)_

```c
int sub_10325246(void)
{
}
```

## `sub_1032524a` `0x1032524a`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1032524a(void)
{
}
```

## `sub_1032524c` `0x1032524c`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1032524c(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_10325270` `0x10325270`

_159 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b0cc;
extern struct_1 *g_1038b0dc;
extern struct_1 *g_1038b0ec;
extern struct_1 *g_1038b1b4;
extern unsigned int g_1038e180;

int sub_10325270(struct_0 *a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0x2dc]
    unsigned int v1;  // [bp-0x224]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]

    v2 = g_1038e180 ^ &v3;
    while ((char)sub_10320780(a0->field_0))
    {
        g_1038b0cc(a0->field_4);
        g_1038b1b4(100);
        g_1038b0ec(a0->field_4);
        sub_10350ad0(&v0, 0, 716);
        v0 = 65537;
        if (g_1038b0dc(a0->field_4, &v0) && v1 == a1)
            break;
    }
    return sub_10351225();
}
```

## `sub_10325310` `0x10325310`

_589 bytes. (leaf/helper — see body)_

```c
extern int g_1038c8ac;
extern unsigned int g_1038e180;
extern int g_103a2818;
extern int g_103a2ad0;

int sub_10325310(char a0)
{
    unsigned long v20;  // ldt
    unsigned long v21;  // gdt
    unsigned short v22;  // fs
    unsigned long v23;  // 4138
    unsigned long v24;  // 4155
    unsigned long v26;  // 4114
    int v0;  // [bp-0x314]
    int v1;  // [bp-0x310]
    int v2;  // [bp-0x30c]
    int v3;  // [bp-0x308]
    char v4;  // [bp-0x301]
    char v5;  // [bp-0x300]
    char v6;  // [bp-0x2a0]
    char v7;  // [bp-0x284]
    char v8;  // [bp-0x222]
    char v9;  // [bp-0x221]
    char v10;  // [bp-0x220]
    char v11;  // [bp-0x200]
    char v12;  // [bp-0x1e0]
    unsigned int v13;  // [bp-0x1d4]
    char v14;  // [bp-0x78]
    int v15;  // [bp-0x14]
    unsigned int v16;  // [bp-0x10]
    unsigned int v17;  // [bp-0xc]
    unsigned int v18;  // [bp-0x8], Other Possible Types: char
    char v19;  // [bp-0x4]

    v18 = 4294967295;
    v17 = sub_1036b9dc;
    v23 = _ccall(v20, v21, (unsigned int)v22, 0);
    v16 = *((int *)v23);
    v15 = g_1038e180 ^ &v19;
    v24 = _ccall(v20, v21, (unsigned int)v22, 0);
    *((unsigned int **)v24) = &v16;
    sub_1032c360(&v12, v15);
    v18 = 0;
    v3 = sub_1031fd90(&v10);
    v2 = v3;
    v18 = 1;
    sub_103268f0(v2);
    v18 = 3;
    sub_1031a0e0(&v10);
    if (a0 && !v13 && !(char)sub_103275b0())
        v13 = sub_10327150();
    sub_1032bd50(&v11, 0);
    v18 = 4;
    if ((char)sub_1031e350(&v11))
    {
        v9 = 0;
        v18 = 3;
        sub_1031a0e0(&v11);
        v18 = 0;
        sub_10319f00(&v14);
        v18 = 4294967295;
        sub_1031e250(&v12);
    }
    else
    {
        v1 = sub_1032c4f0(&v6);
        v0 = v1;
        v18 = 5;
        sub_1031e1d0(&v7, v0);
        v18 = 6;
        sub_1031e1d0(&v5, sub_1032e0e0(v2));
        v18 = 7;
        v8 = -(0 < sub_1032bf70(&v5, &v7, 0, 0, 1, 4, &g_103a2ad0, &g_103a2ad0, &v12, g_1038c8ac)) + 1;
        v18 = 6;
        sub_10319f00(&v5);
        v18 = 5;
        sub_10319f00(&v7);
        v18 = 4;
        sub_1031a3a0(&v6);
        if (!v8)
        {
            sub_10312460(g_103a2818);
            return sub_10325546(g_103a2818);
        }
        v4 = 0;
        v18 = 3;
        sub_1031a0e0(&v11);
        v18 = 0;
        sub_10319f00(&v14);
        v18 = 4294967295;
        sub_1031e250(&v12);
    }
    v26 = _ccall(v20, v21, (unsigned int)v22, 0);
    *((unsigned int *)v26) = v16;
    return sub_10351225();
}
```

## `sub_10325535` `0x10325535`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10325535(void)
{
    sub_10325546();
    return;
}
```

## `sub_10325546` `0x10325546`

_58 bytes. (leaf/helper — see body)_

```c
char sub_10325546(void)
{
    char v1;  // [bp+0xffd06]
    unsigned int v2;  // [bp+0x100000], Other Possible Types: char

    v1 = 1;
    v2 = 3;
    sub_1031a0e0(/* unsupported instruction */ - 508);
    v2 = 0;
    sub_10319f00(/* unsupported instruction */ - 116);
    v2 = 4294967295;
    sub_1031e250(/* unsupported instruction */ - 476);
}
```

## `sub_103255a0` `0x103255a0`

_144 bytes. refs "COMCTL32.DLL", "PropertySheetA"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b078;
extern struct_0 *g_1038b080;

unsigned int * sub_103255a0(void)
{
    unsigned int *v0;  // [bp-0x74]
    char v1;  // [bp-0x70], Other Possible Types: unsigned int
    unsigned int v2;  // [bp-0x6c]
    unsigned int v3;  // [bp-0x58]
    char *v4;  // [bp-0x50]
    unsigned int v5;  // [bp-0x4c]
    char v6;  // [bp-0x3c], Other Possible Types: unsigned int
    unsigned int v7;  // [bp-0x38]
    unsigned int *v8;  // [bp-0x8]

    sub_10350ad0(&v1, 0, 52);
    v1 = 52;
    v2 = 264;
    v3 = 1;
    v4 = &v6;
    v5 = sub_10325630;
    sub_10350ad0(&v6, 0, 52);
    v6 = 52;
    v7 = 0;
    v8 = g_1038b080("COMCTL32.DLL");
    if (!v8)
        return v8;
    v0 = g_1038b078(v8, "PropertySheetA");
    if (!v0)
        return v0;
    return v0(&v1);
}
```

