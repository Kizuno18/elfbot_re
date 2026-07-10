# elfbot.dll decompiled — loader 0x0041891a..0x0041a327

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_0041891a` `0x0041891a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41891a(void)
{
    return sub_418907();
}
```

## `sub_0041891c` `0x0041891c`

_7 bytes. (leaf/helper — see body)_

```c
int sub_41891c(void)
{
    unsigned int v1;  // ebx

    return v1;
}
```

## `sub_00418923` `0x00418923`

_1 bytes. (leaf/helper — see body)_

```c
int sub_418923(void)
{
    sub_418924();
    return;
}
```

## `sub_00418924` `0x00418924`

_399 bytes. (leaf/helper — see body)_

```c
typedef struct struct_3 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned short *field_c;
} struct_3;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_420b2c;
extern struct_0 *g_420b34;
extern struct_0 *g_420b3c;
extern struct_0 *g_420b40;
extern struct_0 *g_420b4c;
extern struct_0 *g_420b50;

int sub_418924(void)
{
    unsigned int v18;  // ebx
    unsigned int v19;  // esi
    unsigned int v28;  // edi
    unsigned int v29;  // ecx
    unsigned short *v30;  // edx
    char v31;  // bl
    unsigned long v32;  // 4118
    unsigned int v20;  // edi
    unsigned long v21;  // ldt
    unsigned long v22;  // gdt
    unsigned short v23;  // fs
    unsigned long v24;  // 4166
    unsigned long v25;  // 4175
    unsigned int v26;  // esi
    unsigned int v27;  // eax
    unsigned int v0;  // [bp-0x98]
    unsigned int v1;  // [bp-0x94]
    unsigned int v2;  // [bp-0x5c]
    unsigned int v3;  // [bp-0x54]
    unsigned int v4;  // [bp-0x50]
    unsigned int v5;  // [bp-0x4c]
    char *v6;  // [bp-0x48]
    unsigned int v7;  // [bp-0x44]
    unsigned int v8;  // [bp-0x40]
    unsigned int v9;  // [bp-0x3c]
    unsigned int v10;  // [bp-0x38]
    unsigned int v11;  // [bp-0x34]
    char v12;  // [bp-0x30]
    unsigned int v13;  // [bp-0x2c]
    struct_3 *v14;  // [bp-0x14]
    unsigned int v15;  // [bp-0x10]
    char v16;  // [bp-0x4]

    v9 = v18;
    v8 = v19;
    v7 = v20;
    v11 = 0;
    v10 = 0;
    v6 = &v16;
    v5 = sub_418ac1;
    v24 = _ccall(v21, v22, (unsigned int)v23, 0);
    v4 = *((int *)v24);
    v25 = _ccall(v21, v22, (unsigned int)v23, 0);
    *((unsigned int **)v25) = &v4;
    if ((char)sub_418748())
    {
        v2 = 0;
        v26 = g_420b3c(0, 0, 983103);
        if (v26)
        {
            v28 = g_420b40(v26, v27, 0x1ff);
            if (v28)
            {
                v15 = 0;
                g_420b50(v28, 0, 0, &v15);
                if (v15)
                {
                    v14 = sub_40536c(0x40, v15 * 2);
                    if (g_420b50(v28, v14, v15 * 2, &v15))
                    {
                        if (!g_420b34(v28, &v12))
                            v13 = 1;
                        if (v14->field_0 == 1 && v14->field_4 == 1 && v14->field_8 == 1)
                        {
                            v1 = 2147483647;
                            sub_403c18(v29, v14->field_c);
                            v0 = v11;
                            sub_403c18(v29, v30);
                            if (sub_40936c() > 0)
                                goto LABEL_418a66;
                        }
                        if (!g_420b4c(v28, 1, 1, 1, v30, 0, 0, 0, 0, 0, v29) || v13 != 1)
                        {
                            v31 = 0;
                        }
                        else
                        {
LABEL_418a66:
                            v31 = 1;
                        }
                    }
                    LocalFree(v14);
                }
                g_420b2c(v28);
            }
            g_420b2c(v26);
        }
    }
    v32 = _ccall(v21, v22, (unsigned int)v23, 0);
    *((unsigned int *)v32) = v2;
    v3 = sub_418ac8;
    sub_418ab3();
    return;
}
```

## `sub_00418ab3` `0x00418ab3`

_14 bytes. (leaf/helper — see body)_

```c
int sub_418ab3(void)
{
    return sub_403a34();
}
```

## `sub_00418ac1` `0x00418ac1`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_418ac1(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00418ac6` `0x00418ac6`

_2 bytes. (leaf/helper — see body)_

```c
int sub_418ac6(void)
{
    return sub_418ab3();
}
```

## `sub_00418ac8` `0x00418ac8`

_11 bytes. (leaf/helper — see body)_

```c
int sub_418ac8(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // ebx

    return v0;
}
```

## `sub_00418ad3` `0x00418ad3`

_1 bytes. (leaf/helper — see body)_

```c
int sub_418ad3(void)
{
    sub_418ad4();
    return;
}
```

## `sub_00418ad4` `0x00418ad4`

_185 bytes. (leaf/helper — see body)_

```c
int sub_418ad4(void)
{
    unsigned int v7;  // edx
    int v8;  // esi
    unsigned int i;  // ebx
    unsigned long v19;  // 4118
    int v9;  // ebx
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // fs
    unsigned long v13;  // 4131
    unsigned int v14;  // 4103
    unsigned long v15;  // 4140
    HKEY v16;  // eax
    unsigned int v0;  // [bp-0x12c]
    unsigned int v1;  // [bp-0x124]
    Byte v2[261];  // [bp-0x111]
    HKEY v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]
    int v6;  // [bp+0x4]

    v4 = v7;
    sub_403e68(v8, v9, 0);
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v14 = *((int *)v13);
    v0 = *((int *)v13);
    v15 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v15) = &v0;
    if (!RegOpenKeyExA(v16, sub_403e78(0, 983103, &v3, v14, sub_418ba1, &v5), 0, KEY_ALL_ACCESS, &v3))
    {
        for (i = 0; !RegEnumKeyA(v3, i, v2, 260); i += 1)
        {
            sub_403c54(v6);
            sub_418ad4(v6);
        }
        RegCloseKey(v3);
    }
    RegDeleteKeyA(v16, sub_403e78());
    v19 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v19) = v14;
    v1 = sub_418ba8;
    sub_418b8d();
    return;
}
```

## `sub_00418b8d` `0x00418b8d`

_20 bytes. (leaf/helper — see body)_

```c
int sub_418b8d(void)
{
    sub_403a10();
    return sub_403a10();
}
```

## `sub_00418ba1` `0x00418ba1`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_418ba1(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00418ba6` `0x00418ba6`

_2 bytes. (leaf/helper — see body)_

```c
int sub_418ba6(void)
{
    return sub_418b8d();
}
```

## `sub_00418ba8` `0x00418ba8`

_6 bytes. (leaf/helper — see body)_

```c
void sub_418ba8(unsigned int a0)
{
    return;
}
```

## `sub_00418bae` `0x00418bae`

_2 bytes. (leaf/helper — see body)_

```c
int sub_418bae(void)
{
    return sub_418bb0();
}
```

## `sub_00418bb0` `0x00418bb0`

_1054 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_4208d8;

int sub_418bb0(void)
{
    HKEY i;  // ecx
    HKEY v28;  // ecx
    int v37;  // ebx
    unsigned long v42;  // 4118
    unsigned long v29;  // ldt
    unsigned long v30;  // gdt
    unsigned short v31;  // fs
    unsigned long v32;  // 4146
    unsigned int v33;  // 4111
    unsigned long v34;  // 4155
    int v35;  // edi
    int v36;  // esi
    unsigned int v0;  // [bp-0x494]
    int v1;  // [bp-0x490]
    int v2;  // [bp-0x48c]
    unsigned int v3;  // [bp-0x468]
    unsigned int v4;  // [bp-0x464]
    int v5;  // [bp-0x450]
    WCHAR v6[10];  // [bp-0x44a]
    unsigned short v7;  // [bp-0x436]
    unsigned short v8;  // [bp-0x434]
    unsigned short v9;  // [bp-0x432]
    unsigned short v10;  // [bp-0x430]
    unsigned short v11;  // [bp-0x42e]
    WCHAR v12[252];  // [bp-0x22c]
    unsigned int v13;  // [bp-0x34]
    unsigned int v14;  // [bp-0x30]
    unsigned int v15;  // [bp-0x2c]
    unsigned short v16;  // [bp-0x21]
    unsigned short v17;  // [bp-0x1f]
    char *v18;  // [bp-0x1d]
    char v19;  // [bp-0x19]
    HKEY v20;  // [bp-0x18]
    HKEY v21;  // [bp-0x14]
    Byte v22[4];  // [bp-0x10], Other Possible Types: unsigned int
    Byte v23[4];  // [bp-0xc]
    Byte v24[4];  // [bp-0x8]
    char v25;  // [bp-0x4]

    i = 0x92;
    do
    {
        v22 = 0;
        v21 = NULL;
        i = (char *)i + 1;
    } while (i != 0x1);
    v20 = v28;
    v32 = _ccall(v29, v30, (unsigned int)v31, 0);
    v33 = *((int *)v32);
    v14 = *((int *)v32);
    v34 = _ccall(v29, v30, (unsigned int)v31, 0);
    *((unsigned int **)v34) = &v14;
    if ((char)sub_4184a4(v33, sub_418fdf, &v25, v35, v36, v37, v28))
    {
        v13 = 1;
        sub_409eac(1);
        sub_409ee0(1);
        sub_409eac(v5);
        sub_409ee0(v5);
        if (!(char)sub_418924())
        {
            v7 = 92;
            v8 = 63;
            v9 = 63;
            v10 = 92;
            v11 = 0;
            lstrcatW(&v7, v12);
            sub_409eac(0, 983103, &v21);
            sub_409eac("\\", v4);
            sub_403d40(v3);
            if (!RegOpenKeyExA(0x80000002, sub_403e78(v3), v3, "\\", v4))
            {
                sub_409eac(0, 0, 0, 0);
                v19 = RegQueryValueExA(v21, sub_403e78(0, 0, 0, 0), NULL, NULL, NULL, NULL);
                RegCloseKey(v21);
            }
            else
            {
                v19 = 1;
            }
            sub_409eac(0, 983103, &v21);
            if (!RegOpenKeyExA(0x80000002, sub_403e78(0, 983103, &v21), 0, KEY_ALL_ACCESS, &v21))
            {
                sub_409eac(0, 0, 0, 983103, 0, &v20, 0);
                if (!RegCreateKeyExA(v21, sub_403e78(0, 0, 0, 983103, 0, &v20, 0), 0, NULL, REG_OPTION_NON_VOLATILE, KEY_ALL_ACCESS, NULL, &v20, NULL))
                {
                    v24 = 1;
                    v23 = 0;
                    v22 = 4;
                    sub_409eac(v6);
                    sub_410c34(sub_403e78(v6), v6);
                    sub_409eac(0, 4, v24, 4);
                    if (!RegSetValueExA(v28, sub_403e78(0, 4, v24, 4), 0, REG_DWORD_LITTLE_ENDIAN, v24, 4))
                    {
                        sub_409eac(0, 4, v23, 4);
                        if (!RegSetValueExA(v28, sub_403e78(0, 4, v23, 4), 0, REG_DWORD_LITTLE_ENDIAN, v23, 4))
                        {
                            sub_409eac(0, 4, v22, 4);
                            if (!RegSetValueExA(v28, sub_403e78(0, 4, v22, 4), 0, REG_DWORD_LITTLE_ENDIAN, v22, 4) && !RegSetValueExW(v28, v6, 0, REG_SZ, &v7, lstrlenW(&v7) * 2 + 2))
                            {
                                sub_409eac("\\", &v7);
                                sub_409eac("\\", v2);
                                sub_409eac("\\", v1);
                                sub_403d40(v0);
                                sub_410c34(sub_403e78(v0), v0);
                                v18 = &v7;
                                v16 = (short)lstrlenW(&v7) * 2;
                                v17 = v16 + 2;
                                sub_40da7c("\\")(&v16);
                            }
                        }
                    }
                    RegCloseKey(v28);
                }
                if (v19)
                {
                    sub_409eac(&v25);
                    sub_418ad4(&v25);
                }
                RegCloseKey(v21);
            }
            if (!g_4208d8)
                DeleteFileW(v12);
        }
    }
    v42 = _ccall(v29, v30, (unsigned int)v31, 0);
    *((unsigned int *)v42) = v13;
    v15 = sub_418fe6;
    return sub_418fce();
}
```

## `sub_00418fce` `0x00418fce`

_17 bytes. (leaf/helper — see body)_

```c
int sub_418fce(void)
{
    return sub_403a34();
}
```

## `sub_00418fdf` `0x00418fdf`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_418fdf(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00418fe4` `0x00418fe4`

_2 bytes. (leaf/helper — see body)_

```c
int sub_418fe4(void)
{
    return sub_418fce();
}
```

## `sub_00418fe6` `0x00418fe6`

_9 bytes. (leaf/helper — see body)_

```c
int sub_418fe6(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // ebx

    return v0;
}
```

## `sub_00418ffc` `0x00418ffc`

_372 bytes. (leaf/helper — see body)_

```c
typedef struct struct_4 {
    char padding_0[12];
    unsigned int field_c;
} struct_4;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_41efc0;
extern struct_0 *g_41efc4;
extern struct_0 *g_41eff4;
extern struct_0 *g_41eff8;
extern struct_0 *g_41f000;
extern struct_0 *g_41f004;
extern struct_0 *g_41f010;
extern struct_0 *g_41f014;
extern struct_0 *g_420b54;

unsigned int sub_418ffc(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v15;  // edi
    unsigned int v16;  // esi
    struct_4 *j;  // esi
    unsigned int v25;  // ecx
    unsigned int *iter;  // edi
    unsigned int v17;  // ebx
    unsigned int *v18;  // edi
    unsigned int v19;  // ebx
    unsigned int v20;  // esi
    unsigned int v21;  // cc_dep1
    int v23;  // eax
    unsigned int v0;  // [bp-0xa8]
    unsigned int v1;  // [bp-0xa4]
    unsigned int *v2;  // [bp-0x74]
    unsigned int v3;  // [bp-0x70]
    int node;  // [bp-0x2c]
    char v5;  // [bp-0x25]
    unsigned int v6;  // [bp-0x24]
    unsigned int v7;  // [bp-0x20]
    unsigned int idx[2];  // [bp-0x1c]
    unsigned int v9;  // [bp-0x16]
    unsigned int v10;  // [bp-0x12]
    char v11;  // [bp-0xe]
    char v12;  // [bp-0xd]
    unsigned int v13;  // [bp-0xc]
    unsigned int v14;  // [bp-0x8]

    v13 = g_420b54(a0, a1, a2, v15, v16, v17);
    if (a1 != 1)
        return v13;
    v14 = *((int *)(NtGetCurrentPeb() + 32));
    if ((v14 & 813695000))
        return v13;
    v18 = NULL;
    *((char *)&v9) = 109;
    *((char *)&v9 + 1) = 99;
    *((char *)&v9 + 2) = 50;
    *((char *)&v9 + 3) = 83;
    *((char *)&v10) = 87;
    *((char *)&v10 + 1) = 0x44;
    *((char *)&v10 + 2) = 73;
    *((char *)&v10 + 3) = 74;
    v12 = 0;
    v19 = 1;
    do
    {
        v5 = 1;
        v11 = (char)v19 + 48;
        v20 = g_41eff4(4, 0, &v9);
        if (v20)
        {
            idx = g_41eff8(v20, 4, 0, 0, 0);
            if (idx)
            {
                v1 = idx[1];
                v0 = idx[0];
                v21 = v10;
                if (v21 == v1)
                {
                    v1 = v0;
                    v21 = v9;
                }
                if (v21 == v1)
                {
                    v5 = 0;
                    v23 = idx[1] - 1;
                    if (v23 >= 0)
                    {
                        node = v23 + 1;
                        v7 = 0;
                        do
                        {
                            if (!v18)
                                v18 = g_41f010(64, 624);
                            v3 = v20;
                            v2 = v18;
                            j = &idx[78 * v7 + 3];
                            v25 = 156;
                            for (iter = v18; v25; j = &j->padding_0[4])
                            {
                                v25 -= 1;
                                *(iter) = *((int *)&j->padding_0[0]);
                                iter += 1;
                            }
                            v18 = v18;
                            v20 = v20;
                            if (!*((char *)v18))
                            {
                                v5 = 1;
                                break;
                            }
                            v6 = g_41efc0(1);
                            g_41efc4(v18);
                            g_41efc0(v6);
                            v7 += 1;
                            node -= 1;
                        } while (node != 1);
                    }
                }
                g_41f000(idx);
            }
            g_41f004(v20);
        }
    } while (!v5 && (v19 += 1, v19 != 10));
    if (!v18)
        return v13;
    g_41f014(v18);
    return v13;
}
```

## `sub_00419198` `0x00419198`

_247 bytes. (leaf/helper — see body)_

```c
extern char g_41f110;
extern unsigned int g_420b10;
extern unsigned int g_420b28;

int sub_419198(void)
{
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    int v20;  // esi
    unsigned int v21;  // ebx
    int v22;  // esi
    char v23;  // dl
    int v24;  // esi
    unsigned long v25;  // 4118
    unsigned long v26;  // 4118
    int v27;  // edi
    int v28;  // esi
    int v29;  // ebx
    unsigned short v12;  // fs
    unsigned long v13;  // 4179
    unsigned long v14;  // 4183
    unsigned int v15;  // eax
    unsigned long v16;  // 4124
    unsigned int v17;  // 4103
    unsigned long v18;  // 4133
    int v19;  // esi
    int v0;  // [bp-0x38]
    unsigned int v1;  // [bp-0x34]
    unsigned int v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x28]
    unsigned int v4;  // [bp-0x24]
    char *v5;  // [bp-0x20], Other Possible Types: unsigned int
    unsigned int idx;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    char v8;  // [bp-0x4]

    v7 = 0;
    v5 = &v8;
    v4 = sub_4192cf;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v3 = *((int *)v13);
    v14 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v14) = &v3;
    if (v15 && g_41f110)
    {
        sub_40520c(&g_420b10);
        v16 = _ccall(v10, v11, (unsigned int)v12, 0);
        v17 = *((int *)v16);
        v1 = *((int *)v16);
        v18 = _ccall(v10, v11, (unsigned int)v12, 0);
        *((unsigned int **)v18) = &v1;
        v0 = sub_40464c(v17, sub_41928d, &v8);
        sub_404808();
        idx = 0;
        v19 = sub_404654();
        if (v19 >= 0)
        {
            v20 = v19 + 1;
            v21 = 0;
            do
            {
                v22 = v20;
                if ((v15 == 4294967295 && !v23 || v15 == *((int *)(g_420b28 + v21 * 40))) && (!*((int *)(g_420b28 + v21 * 40 + 24)) || !*((char *)(*((int *)(g_420b28 + v21 * 40 + 24)) + 36))))
                {
                    *((int *)(v7 + idx * 4)) = *((int *)(g_420b28 + v21 * 40 + 28));
                    idx += 1;
                }
            } while ((v21 += 1, v24 = (int)(v22 - 1), v20 = (int)(v22 - 1), v22 != 1));
        }
        v25 = _ccall(v10, v11, (unsigned int)v12, 0);
        *((unsigned int *)v25) = v17;
        v2 = sub_419294;
        sub_419282();
        return;
    }
    v26 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v26) = v3;
    v5 = sub_4192d6;
    sub_4192c0(v27, v28, v29);
    return;
}
```

## `sub_00419282` `0x00419282`

_11 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420b10;

void sub_419282(void)
{
    sub_40534c(&g_420b10);
    return;
}
```

## `sub_0041928d` `0x0041928d`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_41928d(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00419292` `0x00419292`

_2 bytes. (leaf/helper — see body)_

```c
void sub_419292(void)
{
    sub_419282();
    return;
}
```

## `sub_00419294` `0x00419294`

_31 bytes. (leaf/helper — see body)_

```c
int sub_419294(void)
{
    int v2;  // esi
    int v3;  // esi
    int v4;  // esi
    int v5;  // esi
    int v1;  // [bp+0xffff8]

    v2 = v1 - 1;
    if (v2 < 0)
        goto LABEL_0x4192b3;
    v3 = v2 + 1;
    while (true)
    {
        v4 = v3;
        sub_417208();
        v5 = v4 - 1;
        v3 = v5;
    }
}
```

## `sub_004192c0` `0x004192c0`

_15 bytes. (leaf/helper — see body)_

```c
int sub_4192c0(void)
{
    return sub_404814();
}
```

## `sub_004192cf` `0x004192cf`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4192cf(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004192d4` `0x004192d4`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4192d4(void)
{
    return sub_4192c0();
}
```

## `sub_004192d6` `0x004192d6`

_7 bytes. (leaf/helper — see body)_

```c
void sub_4192d6(unsigned int a0, unsigned int a1)
{
    return;
}
```

## `sub_004192dd` `0x004192dd`

_454 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
} struct_0;

int sub_4192dd(unsigned int a0)
{
    unsigned long v14;  // ldt
    unsigned long v15;  // gdt
    unsigned int v24;  // ecx
    unsigned int v25;  // esi
    unsigned int v26;  // edx
    int v27;  // eax
    unsigned int iter;  // edi
    struct_0 *i;  // esi
    char iter1[4];  // edi
    unsigned int v31;  // ecx
    unsigned short v16;  // fs
    HMODULE v32;  // eax
    struct_0 *j;  // esi
    char node[4];  // edi
    unsigned int v35;  // ecx
    unsigned long v36;  // 4118
    unsigned long v17;  // 4165
    unsigned int v18;  // 4122
    unsigned long v19;  // 4174
    int v20;  // edi
    int v21;  // esi
    int v22;  // ebx
    unsigned int v0;  // [bp-0x730]
    unsigned int v1;  // [bp-0x72c]
    int v2;  // [bp-0x728]
    unsigned int v3;  // [bp-0x724]
    unsigned int v4;  // [bp-0x720]
    unsigned int v5;  // [bp-0x708]
    WCHAR v6[572];  // [bp-0x704]
    char v7;  // [bp-0x28c]
    int iter2;  // [bp-0x1c]
    unsigned int v9[2];  // [bp-0x18]
    unsigned int *idx;  // [bp-0x14]
    char v11;  // [bp-0xd]
    unsigned int v12;  // [bp-0xc]

    v5 = 0;
    v9 = NULL;
    v17 = _ccall(v14, v15, (unsigned int)v16, 0);
    v18 = *((int *)v17);
    v3 = *((int *)v17);
    v19 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int **)v19) = &v3;
    v11 = 0;
    iter = 1;
    sub_409eac(v2, v18, sub_4194b3, &/* unsupported instruction */, v20, v21, v22, 0);
    v1 = v5;
    sub_403bd8(v24, _INSERT(iter, 0, (char)iter + 48));
    sub_403ccc();
    v25 = sub_4114f0(sub_403e78(0), 0);
    if (v25)
    {
        idx = (unsigned int *)MapViewOfFile(v25, FILE_MAP_READ, 0, 0, NULL);
        if (idx)
        {
            v1 = idx[1];
            v0 = *(idx);
            v26 = v9[1];
            if (v9[1] == idx[1])
            {
                v26 = v9[0];
                v1 = *(idx);
            }
            if (v26 == v1)
            {
                v27 = idx[2] - 1;
                if (v27 >= 0)
                {
                    iter2 = v27 + 1;
                    v12 = 0;
                    do
                    {
                        if (!(GetVersion() & 0x80000000))
                        {
                            v1 = v25;
                            v0 = iter;
                            i = &idx[286 * v12 + 3];
                            iter1 = v6;
                            for (v31 = 286; v31; i = &i->padding_0[4])
                            {
                                v31 -= 1;
                                *((int *)&iter1[0]) = *((int *)&i->padding_0[0]);
                                iter1 += 1;
                            }
                            iter = iter;
                            v25 = v25;
                            if (!*((unsigned short *)v6))
                            {
                                break;
                            }
                            else
                            {
                                if (GetModuleHandleW(v6) != v32)
                                    continue;
                                v11 = 1;
                                break;
                            }
                        }
                        else
                        {
                            v1 = v25;
                            v0 = iter;
                            j = &idx[156 * v12 + 3];
                            node = &v7;
                            for (v35 = 156; v35; j = &j->padding_0[4])
                            {
                                v35 -= 1;
                                *((int *)&node[0]) = *((int *)&j->padding_0[0]);
                                node += 1;
                            }
                            iter = iter;
                            v25 = v25;
                            if (!*(&v7))
                            {
                                break;
                            }
                            else if (sub_4052c4(&v7) == v32)
                            {
                                v11 = 1;
                                break;
                            }
                        }
                    } while ((v12 += 1, iter2 = (int)(iter2 - 1), iter2 = iter2, iter2 != 1));
                }
            }
            UnmapViewOfFile(idx);
        }
        CloseHandle(v25);
    }
    if (!v11)
        sub_419198();
    v36 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((int *)v36) = v2;
    v4 = sub_4194ba;
    return sub_41949a();
}
```

## `sub_0041949a` `0x0041949a`

_16 bytes. (leaf/helper — see body)_

```c
int sub_41949a(void)
{
    sub_403a34();
}
```

## `sub_004194b3` `0x004194b3`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4194b3(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004194b8` `0x004194b8`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4194b8(void)
{
    return sub_41949a();
}
```

## `sub_004194ba` `0x004194ba`

_7 bytes. (leaf/helper — see body)_

```c
void sub_4194ba(unsigned int a0, unsigned int a1)
{
    return;
}
```

## `sub_004194c1` `0x004194c1`

_370 bytes. (leaf/helper — see body)_

```c
typedef struct struct_3 {
    char padding_0[12];
    unsigned int field_c;
} struct_3;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_41efd0;
extern struct_0 *g_41eff4;
extern struct_0 *g_41eff8;
extern struct_0 *g_41f000;
extern struct_0 *g_41f004;
extern struct_0 *g_41f00c;
extern struct_0 *g_41f010;
extern struct_0 *g_41f014;
extern struct_0 *g_41f144;

unsigned int sub_4194c1(void)
{
    unsigned int v18;  // ebx
    unsigned int v19;  // esi
    struct_3 *i;  // esi
    unsigned int v28;  // ecx
    unsigned int *iter;  // edi
    unsigned int v20;  // edi
    unsigned int *v21;  // edi
    unsigned int v22;  // ebx
    unsigned int v23;  // esi
    unsigned int v24;  // cc_dep1
    int v26;  // eax
    unsigned int v0;  // [bp-0x8c]
    unsigned int v1;  // [bp-0x88]
    unsigned int *v2;  // [bp-0x60]
    unsigned int v3;  // [bp-0x5c]
    unsigned int v4;  // [bp-0x30]
    unsigned int v5;  // [bp-0x2c]
    unsigned int v6;  // [bp-0x28]
    int node;  // [bp-0x24]
    char v8;  // [bp-0x1e]
    char v9;  // [bp-0x1d]
    unsigned int v10;  // [bp-0x1c]
    unsigned int idx[2];  // [bp-0x18]
    unsigned int v12;  // [bp-0x12]
    unsigned int v13;  // [bp-0xe]
    char v14;  // [bp-0xa]
    char v15;  // [bp-0x9]
    unsigned int v16;  // [bp-0x8]
    unsigned int v17;  // [bp+0x4]

    v6 = v18;
    v5 = v19;
    v4 = v20;
    v16 = *((int *)(NtGetCurrentPeb() + 32));
    v8 = 0;
    if (!(v16 & 0x30800000))
    {
        v21 = NULL;
        *((char *)&v12) = 109;
        *((char *)&v12 + 1) = 99;
        *((char *)&v12 + 2) = 50;
        *((char *)&v12 + 3) = 83;
        *((char *)&v13) = 87;
        *((char *)&v13 + 1) = 0x44;
        *((char *)&v13 + 2) = 73;
        *((char *)&v13 + 3) = 74;
        v15 = 0;
        v22 = 1;
        do
        {
            v9 = 1;
            v14 = (char)v22 + 48;
            v23 = g_41eff4(4, 0, &v12);
            if (v23)
            {
                idx = g_41eff8(v23, 4, 0, 0, 0);
                if (idx)
                {
                    v1 = idx[1];
                    v0 = idx[0];
                    v24 = v13;
                    if (v24 == v1)
                    {
                        v1 = v0;
                        v24 = v12;
                    }
                    if (v24 == v1)
                    {
                        v9 = 0;
                        v26 = idx[1] - 1;
                        if (v26 >= 0)
                        {
                            node = v26 + 1;
                            v10 = 0;
                            do
                            {
                                if (!v21)
                                    v21 = g_41f010(64, 624);
                                v3 = v23;
                                v2 = v21;
                                i = &idx[78 * v10 + 3];
                                v28 = 156;
                                for (iter = v21; v28; i = &i->padding_0[4])
                                {
                                    v28 -= 1;
                                    *(iter) = *((int *)&i->padding_0[0]);
                                    iter += 1;
                                }
                                v21 = v21;
                                v23 = v23;
                                if (!*((char *)v21))
                                {
                                    v9 = 1;
                                    break;
                                }
                                else if (g_41efd0(v21) == v17)
                                {
                                    v8 = 1;
                                    break;
                                }
                            } while ((v10 += 1, node = (int)(node - 1), node = node, node != 1));
                        }
                    }
                    g_41f000(idx);
                }
                g_41f004(v23);
            }
        } while (!v9 && !v8 && (v22 += 1, v22 != 10));
        if (v21)
            g_41f014(v21);
    }
    if (!v8)
        return g_41f144(v17);
    g_41f00c(5);
    return 0;
}
```

## `sub_00419633` `0x00419633`

_1 bytes. (leaf/helper — see body)_

```c
void sub_419633(unsigned int a0, unsigned int a1)
{
    sub_419634();
    return;
}
```

## `sub_00419634` `0x00419634`

_1024 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    int field_8;
} struct_0;

int sub_419634(void)
{
    unsigned long v18;  // ldt
    unsigned long v19;  // gdt
    unsigned int v28;  // 4103
    unsigned long v29;  // 4133
    unsigned int v31;  // ecx
    enum WIN32_ERROR v33;  // eax
    struct_0 *v34;  // esi
    unsigned int v35;  // edi
    unsigned short v20;  // fs
    unsigned int v36;  // edi
    unsigned int v37;  // ebx
    unsigned int v38;  // edi
    unsigned int v39;  // edi
    unsigned int v40;  // edi
    int v41;  // edi
    unsigned int v42;  // ebx
    int v43;  // edi
    unsigned int v44;  // eax
    unsigned int v45;  // eax
    unsigned long v21;  // 4194
    unsigned int v46;  // edi
    HMODULE v47;  // eax
    unsigned int v48;  // edi
    unsigned int v49;  // edi
    PSTR v50;  // edx
    unsigned long v51;  // 4118
    unsigned long v52;  // 4118
    unsigned int v22;  // 4127
    unsigned long v23;  // 4203
    int v24;  // edi
    int v25;  // esi
    int v26;  // ebx
    unsigned long v27;  // 4124
    int v0;  // [bp-0x6c]
    unsigned int v1;  // [bp-0x68]
    unsigned int v2;  // [bp-0x64]
    char *v3;  // [bp-0x60]
    unsigned int v4;  // [bp-0x5c]
    unsigned int v5;  // [bp-0x54]
    unsigned int v6;  // [bp-0x28]
    unsigned int v7;  // [bp-0x24]
    unsigned int v8;  // [bp-0x20]
    struct_0 *idx;  // [bp-0x1c]
    unsigned int v10;  // [bp-0x18]
    char v11;  // [bp-0x11]
    char v12;  // [bp-0x4]
    char *v13;  // [bp+0x4]
    unsigned int *v14;  // [bp+0x8]
    char v15;  // [bp+0xc]
    unsigned int v16;  // [bp+0x10]
    PSID v17;  // [bp+0x14]

    v21 = _ccall(v18, v19, (unsigned int)v20, 0);
    v22 = *((int *)v21);
    v4 = *((int *)v21);
    v23 = _ccall(v18, v19, (unsigned int)v20, 0);
    *((unsigned int **)v23) = &v4;
    v11 = 0;
    *(v14) = 0;
    sub_409eac(v22, sub_419ac2, &v12, v24, v25, v26, 0, 0, 0, 0, 0, 0, 0);
    sub_409eac(v22, sub_419ac2, &v12, v24, v25, v26, 0, 0, 0, 0, 0, 0, 0);
    sub_403ccc();
    v10 = sub_411214(sub_403e78());
    if (!v10)
    {
        v52 = _ccall(v18, v19, (unsigned int)v20, 0);
        *((unsigned int *)v52) = v22;
        v5 = sub_419ac9;
        sub_419ab4();
        return;
    }
    *(v13) = GetLastError() != ERROR_ALREADY_EXISTS;
    WaitForSingleObject(v10, 4294967295);
    v3 = &v12;
    v2 = sub_419a31;
    v27 = _ccall(v18, v19, (unsigned int)v20, 0);
    v28 = *((int *)v27);
    v1 = *((int *)v27);
    v29 = _ccall(v18, v19, (unsigned int)v20, 0);
    *((unsigned int **)v29) = &v1;
    v6 = 1;
    v7 = 1;
    do
    {
        v6 *= 4;
        if (!(GetVersion() & 0x80000000))
        {
            sub_403bd8(v31, _INSERT(0, 0, (char)v7 + 48));
            sub_403ccc(v6 * 1144 + 12);
            v8 = sub_4113d8(sub_403e78(), v6 * 1144 + 12);
        }
        else
        {
            sub_403bd8(v31, _INSERT(0, 0, (char)v7 + 48));
            sub_403ccc(v6 * 624 + 12);
            v8 = sub_4113d8(sub_403e78(), v6 * 624 + 12);
        }
        if (!v8)
            break;
        v33 = GetLastError();
        v34 = (struct_0 *)MapViewOfFile(v8, FILE_MAP_ALL_ACCESS, 0, 0, NULL);
        if (!v34)
        {
            CloseHandle(v8);
            break;
        }
        idx = v34;
        if (v33 != ERROR_ALREADY_EXISTS)
        {
            *(v14) = v7;
            idx->field_8 = v6;
            v35 = v6 - 1;
            if (v35 >= 0)
            {
                v36 = v35 + 1;
                v37 = 0;
                do
                {
                    v38 = v36;
                    if (!(GetVersion() & 0x80000000))
                        *((unsigned short *)&idx->padding_0[1144 * v37 + 12]) = 0;
                    else
                        idx[1 + 52 * v37].padding_0[0] = 0;
                } while ((v37 += 1, v39 = v38 - 1, v36 = v38 - 1, v38 != 1));
            }
            sub_410f64();
            sub_40e878();
        }
        v40 = idx->field_8 - 1;
        if (v40 >= 0)
        {
            v41 = v40 + 1;
            v42 = 0;
            do
            {
                v43 = v41;
                if (!(GetVersion() & 0x80000000))
                {
                    v44 = v42 * 143;
                    if (*((short *)&(idx[1].padding_0)[v44]))
                        continue;
                    v11 = 1;
                    GetModuleFileNameW(v47, &(idx->padding_0)[v44 + 532], 260);
                    if (!(GetVersion() & 0x80000000) && v17 && IsValidSid(v17))
                    {
                        GetLengthSid(v17);
                        sub_402628(v0);
                    }
                    else
                    {
                        sub_4054b4();
                    }
                    v48 = v42 * 143;
                    (idx[95].padding_0)[v48 + 3] = v15;
                    *((unsigned int *)&(idx[95].padding_0)[v48 + 4]) = 0;
                    (&idx[95].field_8)[2 * v48] = 0;
                    *((unsigned int *)&(idx[96].padding_0)[v48]) = v16;
                    lstrcpyW(&(idx->padding_0)[v48 + 14], v31 + 2);
                    sub_410f64(v0, v28);
                    break;
                }
                else
                {
                    v45 = v42 * 78;
                    if (!(idx[1].padding_0)[v45])
                    {
                        v11 = 1;
                        sub_4052ac(v47, &(idx->padding_0)[v45 + 272], 260);
                        if (!(GetVersion() & 0x80000000) && v17 && IsValidSid(v17))
                        {
                            GetLengthSid(v17);
                            sub_402628(v0);
                        }
                        else
                        {
                            sub_4054b4();
                        }
                        v49 = v42 * 78;
                        *((char *)&(&idx[0x33].field_8)[2 * v49] + 3) = v15;
                        *((unsigned int *)&(idx[52].padding_0)[v49]) = 0;
                        *((unsigned int *)&(idx[52].padding_0)[v49 + 4]) = 0;
                        (&idx[52].field_8)[2 * v49] = v16;
                        lstrcpyA(&(idx->padding_0)[v49 + 13], v50 + 1);
                        sub_410f64(v0, v28);
                        break;
                    }
                }
            } while ((v42 += 1, v46 = v43 - 1, v41 = (int)(v43 - 1), v43 != 1));
        }
        UnmapViewOfFile(idx);
        CloseHandle(v8);
    } while (!v11 && (v7 += 1, v7 != 10));
    v51 = _ccall(v18, v19, (unsigned int)v20, 0);
    *((int *)v51) = v0;
    v2 = sub_419a38;
    sub_419a27();
    return;
}
```

## `sub_00419a27` `0x00419a27`

_10 bytes. (leaf/helper — see body)_

```c
int sub_419a27(void)
{
    HANDLE v1;  // [bp+0xffff0]

    return ReleaseMutex(v1);
}
```

## `sub_00419a31` `0x00419a31`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_419a31(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00419a36` `0x00419a36`

_2 bytes. (leaf/helper — see body)_

```c
int sub_419a36(void)
{
    return sub_419a27();
}
```

## `sub_00419a38` `0x00419a38`

_111 bytes. (leaf/helper — see body)_

```c
extern int g_4194c4;
extern int g_41f144;
extern int g_420b54;

int sub_419a38(unsigned int a0)
{
    unsigned int v0;  // [bp-0x4]
    HANDLE v1;  // [bp+0xffff0]
    char *v2;  // [bp+0x10000c]

    if (*(v2))
    {
        sub_40e878();
        if ((GetVersion() & 0x80000000))
        {
            v0 = 0;
            sub_41708c(4, &g_420b54, sub_418ffc, sub_411dd4());
            sub_40d994(0);
            sub_41708c(4, &g_41f144, &g_4194c4, sub_411978(0));
        }
    }
    CloseHandle(v1);
}
```

## `sub_00419ab4` `0x00419ab4`

_14 bytes. (leaf/helper — see body)_

```c
int sub_419ab4(void)
{
    return sub_403a34();
}
```

## `sub_00419ac2` `0x00419ac2`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_419ac2(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00419ac7` `0x00419ac7`

_2 bytes. (leaf/helper — see body)_

```c
int sub_419ac7(void)
{
    return sub_419ab4();
}
```

## `sub_00419ac9` `0x00419ac9`

_12 bytes. (leaf/helper — see body)_

```c
char sub_419ac9(unsigned int a0, unsigned int a1)
{
    char v0;  // [bp+0xffff7]

    return v0;
}
```

## `sub_00419ad5` `0x00419ad5`

_3 bytes. (leaf/helper — see body)_

```c
int sub_419ad5(void)
{
    return sub_419ad8();
}
```

## `sub_00419ad8` `0x00419ad8`

_669 bytes. (leaf/helper — see body)_

```c
int sub_419ad8(void)
{
    unsigned int v11;  // ecx
    unsigned int i;  // ecx
    unsigned long v21;  // 4158
    int len;  // edx
    int idx;  // eax
    char v24;  // bl
    PSTR v25;  // eax
    int len1;  // edx
    int v27;  // eax
    int v28;  // ebx
    char v29;  // bl
    unsigned long v30;  // 4118
    unsigned int v13;  // ecx
    unsigned int v14;  // esi
    char v15;  // bl
    PWSTR v16;  // edx
    unsigned long v17;  // ldt
    unsigned long v18;  // gdt
    unsigned short v19;  // fs
    unsigned long v20;  // 4149
    unsigned int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x2c]
    char *v2;  // [bp-0x28], Other Possible Types: unsigned int
    unsigned int v3;  // [bp-0x24]
    unsigned int v4;  // [bp-0x1c]
    unsigned int v5;  // [bp-0x18]
    int v6;  // [bp-0x14]
    int v7;  // [bp-0xc]
    PWSTR v8;  // [bp-0x8], Other Possible Types: unsigned int
    char v9;  // [bp-0x4]
    void* v10;  // [bp+0x4]

    v8 = v11;
    i = 4;
    do
    {
        v6 = 0;
        v5 = 0;
        i -= 1;
    } while (i != 1);
    v4 = v13;
    InterlockedExchange(&v8, v13);
    v3 = v14;
    v15 = v8;
    v8 = v16;
    v2 = &v9;
    v1 = sub_419d83;
    v20 = _ccall(v17, v18, (unsigned int)v19, 0);
    v0 = *((int *)v20);
    v21 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((unsigned int **)v21) = &v0;
    if (!(GetVersion() & 0x80000000))
    {
        len = lstrlenW(v8);
        if (v15)
        {
            idx = len - 2;
            if (idx >= 1)
            {
                do
                {
                    if (v8[idx] == 92)
                    {
                        *((unsigned short *)&v8[idx]) = 0;
                        len = idx;
                        break;
                    }
                } while ((idx = (int)(idx - 1), idx));
            }
        }
        if (len > 0 && v8[1 + len] != 92)
        {
            *((unsigned short *)&v8[len]) = 92;
            *((unsigned short *)&v8[1 + len]) = 0;
        }
        if (!*((int *)(int)v10[4]))
        {
            sub_410cd4();
            sub_410cd4(v7);
            sub_403ccc();
        }
        else
        {
            sub_403be8();
            sub_409ee0();
            sub_410cd4(v6);
            sub_403ccc();
        }
        if (sub_403c80() <= 6 || *((char *)(*((int *)(int)v10[8]) + 2)) != 58 && (*((char *)*((int *)(int)v10[8])) != 92 || *((char *)(*((int *)(int)v10[8]) + 2)) != 92) || GetFileAttributesW(*((int *)(int)v10[8])) == 4294967295)
            v24 = 0;
        else
            v24 = 1;
        if (v24)
            *((int *)(int)v10[8]) = *((int *)(int)v10[8]);
    }
    else
    {
        len1 = lstrlenA(v25);
        if (v15)
        {
            v27 = len1 - 2;
            if (v27 >= 1)
            {
                do
                {
                    if (v25[v27] == 92)
                    {
                        v25[v27] = 0;
                        len1 = v27;
                        break;
                    }
                } while ((v27 = (int)(v27 - 1), v27));
            }
        }
        if (len1 > 0 && v25[1 + len1] != 92)
        {
            v25[len1] = 92;
            v25[1 + len1] = 0;
        }
        if (!*((int *)(int)v10[4]))
        {
            sub_409f44();
            sub_403be8(v28);
            sub_403ccc();
        }
        else
        {
            sub_403be8();
            sub_403be8(v2);
            sub_403ccc();
        }
        if (sub_403c80() <= 3 || *((char *)(*((int *)(int)v10[12]) + 1)) != 58 && (*((char *)*((int *)(int)v10[12])) != 92 || *((char *)(*((int *)(int)v10[12]) + 1)) != 92) || GetFileAttributesA(sub_403e78()) == 4294967295)
            v29 = 0;
        else
            v29 = 1;
        if (v29)
            *((int *)(int)v10[4]) = *((int *)(int)v10[12]);
    }
    v30 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((unsigned int *)v30) = v0;
    v2 = sub_419d8a;
    sub_419d75();
    return;
}
```

## `sub_00419d75` `0x00419d75`

_14 bytes. (leaf/helper — see body)_

```c
int sub_419d75(void)
{
    return sub_403a34();
}
```

## `sub_00419d83` `0x00419d83`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_419d83(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00419d88` `0x00419d88`

_2 bytes. (leaf/helper — see body)_

```c
int sub_419d88(void)
{
    return sub_419d75();
}
```

## `sub_00419d8a` `0x00419d8a`

_8 bytes. (leaf/helper — see body)_

```c
int sub_419d8a(unsigned int a0)
{
    unsigned int v0;  // ebx

    return v0;
}
```

## `sub_00419d92` `0x00419d92`

_2 bytes. (leaf/helper — see body)_

```c
int sub_419d92(void)
{
    sub_419d94();
    return;
}
```

## `sub_00419d94` `0x00419d94`

_305 bytes. (leaf/helper — see body)_

```c
extern void* g_420710;

int sub_419d94(void)
{
    unsigned int v8;  // ecx
    unsigned int v9;  // edx
    unsigned int v10;  // eax
    unsigned int v11;  // ebx
    int v12;  // ebx
    int v0;  // [bp-0x324]
    Char v1[523];  // [bp-0x320]
    Byte v2[261];  // [bp-0x115]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]

    v3 = v8;
    v4 = v9;
    v5 = v10;
    v12 = _INSERT(v11, 0, 1);
    if ((char)sub_419ad8(&v6, v0))
        return v12;
    sub_4052ac(NULL, v2, 260);
    GetModuleFileNameW(NULL, v1, 260);
    if ((char)sub_419ad8(&v6))
        return v12;
    sub_4052ac(g_420710, v2, 260);
    GetModuleFileNameW(g_420710, v1, 260);
    if ((char)sub_419ad8(&v6))
        return v12;
    GetCurrentDirectoryA(260, v2);
    GetCurrentDirectoryW(260, v1);
    if ((char)sub_419ad8(&v6))
        return v12;
    GetSystemDirectoryA(v2, 260);
    GetSystemDirectoryW(v1, 260);
    return sub_419ad8(&v6);
}
```

## `sub_00419ec5` `0x00419ec5`

_658 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_41efc0;
extern struct_0 *g_41efc4;
extern struct_0 *g_41efc8;
extern struct_0 *g_41efcc;
extern struct_0 *g_41efd0;
extern struct_0 *g_41efd4;
extern struct_0 *g_41efd8;
extern struct_0 *g_41efdc;
extern struct_0 *g_41efe0;
extern struct_0 *g_41eff0;
extern struct_0 *g_41eff4;
extern struct_0 *g_41eff8;
extern struct_0 *g_41f000;
extern struct_0 *g_41f004;
extern struct_0 *g_41f028;

unsigned int sub_419ec5(void* a0)
{
    unsigned int v37;  // ebx
    unsigned int v38;  // esi
    unsigned int v48;  // esi
    unsigned int v49;  // eax
    unsigned int v50;  // ebx
    char *iter;  // edx
    unsigned int v52;  // ebx
    unsigned int v53;  // eax
    unsigned int v55;  // 4137
    unsigned int v39;  // edi
    unsigned int v57;  // 4138
    unsigned int v58;  // eax
    unsigned int v59;  // ebx
    void* node;  // edx
    unsigned int v61;  // ebx
    unsigned int v62;  // eax
    unsigned int v64;  // 4137
    unsigned int v66;  // 4138
    void* v40;  // ebx
    unsigned int v68;  // ebx
    struct_0 **v69;  // eax
    int j;  // ebx
    void* iter1;  // edi
    unsigned int i;  // ecx
    void* v43;  // esi
    void* v44;  // esi
    unsigned int v45;  // eax
    unsigned int v0;  // [bp-0x370]
    unsigned int v1;  // [bp-0x36c]
    unsigned int v2;  // [bp-0x368]
    int v3;  // [bp-0x361], Other Possible Types: char
    char v4;  // [bp-0x251]
    char v5;  // [bp-0x33]
    char v6;  // [bp-0x32]
    char v7;  // [bp-0x31]
    char v8;  // [bp-0x30]
    char v9;  // [bp-0x2f]
    char v10;  // [bp-0x2e]
    char v11;  // [bp-0x2d]
    char v12;  // [bp-0x2c]
    char v13;  // [bp-0x2b]
    char v14;  // [bp-0x2a]
    char v15;  // [bp-0x29]
    char v16;  // [bp-0x28]
    char v17;  // [bp-0x27]
    char v18;  // [bp-0x26]
    char v19;  // [bp-0x25]
    char v20;  // [bp-0x24]
    char v21;  // [bp-0x23]
    char v22;  // [bp-0x22]
    char v23;  // [bp-0x21]
    char v24;  // [bp-0x20]
    char v25;  // [bp-0x1f]
    char v26;  // [bp-0x17]
    char v27;  // [bp-0x16]
    char v28;  // [bp-0x15]
    char v29;  // [bp-0x14]
    char v30;  // [bp-0x13]
    char v31;  // [bp-0x12]
    char v33;  // [bp-0xf]
    char v34;  // [bp-0xd]
    unsigned int *v35;  // [bp-0xc]
    unsigned int v36;  // [bp-0x8]

    v2 = v37;
    v1 = v38;
    v0 = v39;
    v40 = a0;
    v36 = 0;
    iter1 = &v3;
    i = 203;
    v43 = v40;
    while (i)
    {
        v44 = v43;
        if (!i)
            break;
        i -= 1;
        *((int *)iter1) = *((int *)v44);
        iter1 += 4;
        v43 = v44 + 4;
        break;
    }
    *((short *)iter1) = *((short *)v44);
    if (!(g_41efe0() & 0x80000000))
        g_41efdc(v40, 0, 0x8000);
    else
        g_41f028(v40);
    if (*((char *)&v3))
    {
        v45 = g_41efc0(1);
        if (!(!(g_41efe0(1) & 0x80000000) ? g_41efc8(&v4) : g_41efc4(&v3 + 1)))
            v36 = g_41efd8();
        g_41efc0(v45);
        return v36;
    }
    else
    {
        v48 = (!(g_41efe0() & 0x80000000) ? g_41efd4(&v4) : g_41efd0(&v3 + 1));
        if (!v48)
            return v36;
        v35 = NULL;
        v5 = 71;
        v6 = 108;
        v7 = 111;
        v8 = 98;
        v9 = 97;
        v10 = 108;
        v11 = 92;
        v12 = 65;
        v13 = 117;
        v14 = 116;
        v15 = 111;
        v16 = 0x55;
        v17 = 110;
        v18 = 104;
        v19 = 111;
        v20 = 111;
        v21 = 107;
        v22 = 77;
        v23 = 97;
        v24 = 112;
        v25 = 36;
        v27 = 36;
        v34 = 0;
        v49 = g_41eff0();
        v50 = 0xfffffff8;
        iter = &v26;
        do
        {
            v52 = v50;
            v53 = v49;
            if ((v53 & 15) > 9)
                *(iter) = ((char)v53 & 15) - -87;
            else
                *(iter) = ((char)v53 & 15) + 48;
            v55 = _ccall(27, v53 >> 4, v53 >> 3, 0);
            iter += 1;
            v57 = _ccall(4, 18, v52 + 1, 0, v55);
            v49 = v53 >> 4;
            v50 = v52 + 1;
        } while (!((char)v57));
        v58 = v48;
        v59 = 0xfffffff8;
        node = &v33 + 1;
        do
        {
            v61 = v59;
            v62 = v58;
            if ((v62 & 15) > 9)
                *((char *)node) = ((char)v62 & 15) - -87;
            else
                *((char *)node) = ((char)v62 & 15) + 48;
            v64 = _ccall(27, v62 >> 4, v62 >> 3, 0);
            node -= 1;
            v66 = _ccall(4, 18, v61 + 1, 0, v64);
            v58 = v62 >> 4;
            v59 = v61 + 1;
        } while (!((char)v66));
        v68 = (!(g_41efe0() & 0x80000000) ? g_41eff4(4, 0, &v5) : 0);
        if (!v68)
            v68 = g_41eff4(4, 0, &v12);
        if (!v68)
        {
            v28 = 109;
            v29 = 99;
            v30 = 104;
            v31 = 0;
            if (!(g_41efe0() & 0x80000000))
                v68 = g_41eff4(4, 0, &v5);
            if (!v68)
                v68 = g_41eff4(4, 0, &v12);
        }
        if (v68)
        {
            v69 = g_41eff8(v68, 4, 0, 0, 0);
            if (v69)
            {
                v35 = &*(v69)->field_0;
                g_41f000(v69);
            }
            g_41f004(v68);
        }
        if (v35)
            v35();
        if (!g_41efcc(v48))
        {
            v36 = g_41efd8();
            return v36;
        }
        for (j = 0; g_41efcc(v48) && j < 100; j += 1);
        v36 = 0;
        return v36;
    }
}
```

## `sub_0041a157` `0x0041a157`

_1 bytes. (leaf/helper — see body)_

```c
void sub_41a157(unsigned int a0, unsigned int a1)
{
    sub_41a158();
    return;
}
```

## `sub_0041a158` `0x0041a158`

_436 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    char padding_4[4];
    unsigned int field_8;
    int field_c;
} struct_0;

int sub_41a158(void)
{
    unsigned int v12;  // edx
    unsigned int v13;  // edi
    int v22;  // ebx
    unsigned int v23;  // esi
    struct_0 *idx;  // ebx
    unsigned int v25;  // edx
    unsigned int v26;  // edx
    HANDLE v28;  // eax
    unsigned long v29;  // 4118
    unsigned long v14;  // ldt
    unsigned long v15;  // gdt
    unsigned short v16;  // fs
    unsigned long v17;  // 4169
    unsigned int v18;  // 4121
    unsigned long v19;  // 4178
    int v20;  // edi
    int v21;  // esi
    struct_0 *v0;  // [bp-0x4c]
    unsigned int v1;  // [bp-0x48]
    unsigned int v2;  // [bp-0x44]
    unsigned int v3;  // [bp-0x3c]
    unsigned int v4;  // [bp-0x24]
    HANDLE v5;  // [bp-0x1c]
    unsigned int iter;  // [bp-0x18]
    unsigned int index[2];  // [bp-0x14]
    char v8;  // [bp-0xd]
    unsigned int v9;  // [bp-0xc]
    char v10;  // [bp-0x4]

    v4 = 0;
    index = NULL;
    v13 = v12;
    v17 = _ccall(v14, v15, (unsigned int)v16, 0);
    v18 = *((int *)v17);
    v3 = *((int *)v17);
    v19 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int **)v19) = &v3;
    v9 = 0;
    sub_409eac(v18, sub_41a322, &v10, v20, v21, v22, 0, 0);
    if ((GetVersion() & 0x80000000))
    {
        sub_40e8c8();
        v0 = 0x4;
        v23 = CreateFileMappingA(0xffffffff, NULL, PAGE_READWRITE, 0, 16, sub_403e78());
        v13 = 0;
    }
    else if (v13)
    {
        sub_409b54(&v4, 16);
        sub_403ccc(&v4, 16);
        v23 = sub_4113d8(sub_403e78(), &v4);
    }
    else
    {
        v23 = 0;
    }
    if (v23)
    {
        v8 = GetLastError() != ERROR_ALREADY_EXISTS;
        v0 = NULL;
        idx = (struct_0 *)MapViewOfFile(v23, FILE_MAP_ALL_ACCESS, 0, 0, NULL);
        if (idx)
        {
            iter = 50;
            do
            {
                if (v8)
                    break;
                v2 = (unsigned int)idx->padding_4;
                v1 = idx->field_0;
                v25 = index[1];
                if (index[1] == idx->padding_4)
                {
                    v25 = index[0];
                    v2 = idx->field_0;
                }
            } while ((v25 != v2 || v13 != idx->field_8) && (Sleep(50), iter -= 1, iter = iter, iter != 1));
            if (!v8)
            {
                v2 = (unsigned int)idx->padding_4;
                v1 = idx->field_0;
                v26 = index[1];
                if (index[1] == idx->padding_4)
                {
                    v26 = index[0];
                    v2 = idx->field_0;
                }
                if (v26 == v2 || v13 != idx->field_8)
                    goto LABEL_41a2ed;
            }
            idx->field_c = sub_40ecb8(0, 0);
            idx->field_8 = v13;
            sub_410f64(0, 0);
            if ((GetVersion() & 0x80000000))
                sub_40e878();
            else
                DuplicateHandle(GetCurrentProcess(), v23, v28, &v5, 0, 0, DUPLICATE_SAME_ACCESS);
LABEL_41a2ed:
            v9 = idx->field_c;
            UnmapViewOfFile(idx);
            v0 = idx;
        }
        CloseHandle(v23);
    }
    v29 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((struct_0 **)v29) = v0;
    v2 = sub_41a329;
    sub_41a30c();
    return;
}
```

## `sub_0041a30c` `0x0041a30c`

_22 bytes. (leaf/helper — see body)_

```c
int sub_41a30c(void)
{
    sub_403a34();
    return sub_403a10();
}
```

## `sub_0041a322` `0x0041a322`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_41a322(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041a327` `0x0041a327`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41a327(void)
{
    return sub_41a30c();
}
```

