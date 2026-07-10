# elfbot.dll decompiled — loader 0x00408f5c..0x00409eac

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_00408f5c` `0x00408f5c`

_2 bytes. (leaf/helper — see body)_

```c
void sub_408f5c(unsigned int a0)
{
    return;
}
```

## `sub_00408f5e` `0x00408f5e`

_6 bytes. (leaf/helper — see body)_

```c
int sub_408f5e(void)
{
}
```

## `sub_00408f68` `0x00408f68`

_36 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420894;

int sub_408f68(void)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4146
    unsigned long v10;  // 4155
    unsigned long v11;  // 4171
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    char *v2;  // [bp-0x8], Other Possible Types: unsigned int
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v2 = &v3;
    v1 = sub_408f8d;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v0 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v0;
    g_420894 = g_420894 + 1;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v0;
    v2 = sub_408f94;
    return sub_408f8c(&v4);
}
```

## `sub_00408f8c` `0x00408f8c`

_1 bytes. (leaf/helper — see body)_

```c
void sub_408f8c(void)
{
    return;
}
```

## `sub_00408f8d` `0x00408f8d`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_408f8d(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00408f92` `0x00408f92`

_2 bytes. (leaf/helper — see body)_

```c
void sub_408f92(void)
{
    sub_408f8c();
    return;
}
```

## `sub_00408f94` `0x00408f94`

_2 bytes. (leaf/helper — see body)_

```c
void sub_408f94(unsigned int a0)
{
    return;
}
```

## `sub_00408f96` `0x00408f96`

_10 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420894;

int sub_408f96(void)
{
    unsigned int v1;  // eax

    g_420894 = g_420894 - 1;
    return v1;
}
```

## `sub_00408fb4` `0x00408fb4`

_78 bytes. (leaf/helper — see body)_

```c
int sub_408fb4(void)
{
    int v1;  // esi
    int v2;  // ebx

    if (sub_409614(2147483647, v1, v2))
    {
        sub_409614(1);
        sub_4092fc(1);
    }
    else
    {
        sub_403a10();
    }
    return;
}
```

## `sub_00409024` `0x00409024`

_659 bytes. (leaf/helper — see body)_

```c
int sub_409024(void)
{
    unsigned int v14;  // ecx
    unsigned int v15;  // edx
    int node;  // edi
    int v24;  // eax
    int v26;  // eax
    int v27;  // eax
    int v28;  // eax
    unsigned int j;  // ebx
    int v32;  // eax
    int v16;  // edi
    int v33;  // eax
    int v34;  // eax
    int v17;  // esi
    int v18;  // ebx
    int i;  // ebx
    unsigned int v21;  // eax
    int v22;  // eax
    int v0;  // [bp-0x34]
    int v1;  // [bp-0x30]
    int v2;  // [bp-0x2c]
    int v3;  // [bp-0x28]
    int v4;  // [bp-0x24]
    int v5;  // [bp-0x20]
    int v6;  // [bp-0x1c]
    int iter1;  // [bp-0x18], Other Possible Types: unsigned int
    int iter;  // [bp-0x14], Other Possible Types: unsigned int
    char v9;  // [bp-0xd]
    unsigned int v10;  // [bp-0xc]
    unsigned int v11;  // [bp-0x8]
    char v12;  // [bp+0x4]
    char v13;  // [bp+0x8]

    v10 = v14;
    v11 = v15;
    v3 = sub_403c80(v16, v17, v18);
    v2 = sub_403c80(v16, v17, v18);
    v1 = v2 - v3;
    if (v1 <= 0)
    {
        sub_403ec8();
        v6 = sub_403e78();
        node = sub_403c80();
        v5 = sub_403e78();
        i = sub_4093d8(2147483647, 0, _INSERT(v5, 0, v12), node);
        v9 = i != -1;
        if (!v9)
            return;
        iter = sub_403e78();
        v4 = sub_403e78();
        if (v13)
        {
            do
            {
                node -= i;
                iter += i;
                v21 = sub_402628();
                if (v1)
                {
                    v21 = sub_402628();
                    node += v1;
                }
            } while ((v22 = (int)_INSERT(v21, 0, v12), i = (int)sub_4093d8(2147483647, 0, _INSERT(v21, 0, v12), node), i != -1));
            sub_403f60();
            return;
        }
        else
        {
            iter1 = iter;
            do
            {
                node = node - i - v3;
                iter += i;
                iter1 += i;
                sub_402628();
                iter += v2;
                v24 = v3;
                iter1 += v24;
                i = sub_4093d8(2147483647, 0, _INSERT(v24, 0, v12), node);
                if (i > 0)
                    sub_402628();
            } while (i != -1);
            if (node > 0)
                sub_402628();
            sub_403f60();
            return;
        }
    }
    else
    {
        v26 = sub_403c80();
        v27 = _INSERT(v26, 0, v12);
        v28 = sub_403e78(sub_403c80(2147483647, 0, v27, v26));
        sub_403e78(v28);
        j = sub_4093d8() + 1;
        v9 = j;
        if (!v9)
            return;
        v0 = (!v13 ? v2 : 1);
        sub_403c80();
        do
        {
            sub_403f60();
            sub_403ed0(sub_403ed0() + v1 + j - 1);
            sub_402628();
            sub_403e78(sub_403ed0() + j - 1);
            sub_402628();
            v32 = sub_403c80();
            v33 = _INSERT(v32, 0, v12);
            v34 = sub_403e78(sub_403c80(2147483647, j + v0 - 1, v33, v32));
            sub_403e78(v34);
            j = sub_4093d8() + 1;
        } while (j);
        return;
    }
}
```

## `sub_004092b7` `0x004092b7`

_1 bytes. (leaf/helper — see body)_

```c
void sub_4092b7(char a0)
{
    sub_4092b8();
    return;
}
```

## `sub_004092b8` `0x004092b8`

_20 bytes. (leaf/helper — see body)_

```c
void sub_4092b8(char a0)
{
    int v1;  // ebx
    char v0;  // [bp+0x0]

    sub_409024(0, _INSERT(v1, 0, a0), v1, &v0);
    return;
}
```

## `sub_004092cc` `0x004092cc`

_46 bytes. (leaf/helper — see body)_

```c
int sub_4092cc(void)
{
    int v0;  // [bp-0x14]
    int v1;  // [bp-0x10]
    int v2;  // [bp-0xc]
    int v3;  // [bp-0x8]
    char v4;  // [bp+0x0]

    sub_403a64(v0, v1, v2, v3, &v4);
    sub_403f18(v0, v1, v2, v3, &v4);
    return;
}
```

## `sub_004092fa` `0x004092fa`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4092fa(void)
{
    sub_4092fc();
    return;
}
```

## `sub_004092fc` `0x004092fc`

_25 bytes. (leaf/helper — see body)_

```c
int sub_4092fc(void)
{
    int v1;  // eax
    int v2;  // edi
    int v3;  // esi
    int v4;  // ebx

    sub_403ed8(v1, v2, v3, v4);
    return;
}
```

## `sub_00409315` `0x00409315`

_3 bytes. (leaf/helper — see body)_

```c
int sub_409315(void)
{
    sub_409318();
    return;
}
```

## `sub_00409318` `0x00409318`

_84 bytes. (leaf/helper — see body)_

```c
extern char g_41e28c;

int sub_409318(void)
{
    int v5;  // ebx
    int v6;  // edx
    unsigned int v7;  // eax
    int v8;  // edx
    unsigned int v9;  // eax
    unsigned int v10;  // edx
    int v0;  // [bp-0x10]
    int v1;  // [bp-0xc]
    int v2;  // [bp-0x8]
    int v3;  // [bp-0x4]

    v5 = sub_403c80(v0, v1, v2, v3);
    if (v5 != sub_403c80(v0, v1, v2, v3))
        return;
    v6 = v5;
    if (!v6)
        return;
    v7 = 1;
    while (true)
    {
        v8 = v6;
        if (*(&(&g_41e28c)[*((char *)(v9 + v7 - 1))]) != *(&(&g_41e28c)[*((char *)(v10 + v7 - 1))]))
            return;
        v7 += 1;
        v6 = v8 - 1;
        if (v8 == 1)
            return;
    }
}
```

## `sub_0040936c` `0x0040936c`

_84 bytes. (leaf/helper — see body)_

```c
int sub_40936c(void)
{
    int v5;  // ecx
    unsigned int v6;  // ebx
    unsigned int v7;  // esi
    unsigned int v8;  // edi
    unsigned int v9;  // edx
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    int v3;  // [bp-0x8], Other Possible Types: unsigned int
    int v4;  // [bp+0x4]

    v3 = v5;
    v2 = v6;
    v1 = v7;
    v0 = v8;
    v3 = v9;
    if (v5 && v4)
    {
        sub_403e78(sub_403e78(sub_403c80(v4 - 1, v5 - 1, 1, sub_403c80())));
        sub_4093d8();
        return;
    }
    return;
}
```

## `sub_004093c0` `0x004093c0`

_23 bytes. (leaf/helper — see body)_

```c
int sub_4093c0(void)
{
    char *v1;  // edi

    do
    {
        if (false)
            break;
    } while (*(v1));
    return;
}
```

## `sub_004093d7` `0x004093d7`

_1 bytes. (leaf/helper — see body)_

```c
int sub_4093d7(void)
{
    sub_4093d8();
    return;
}
```

## `sub_004093d8` `0x004093d8`

_569 bytes. (leaf/helper — see body)_

```c
extern char g_41e28c;

int sub_4093d8(void)
{
    int v8;  // ecx
    int v9;  // edi
    char *v17;  // eax
    char *iter;  // eax
    char v19[2];  // edx
    char *node;  // eax
    char iter1[2];  // edx
    char v22[2];  // ecx
    char *v23;  // eax
    char v24[2];  // edx
    char *v25;  // eax
    char v26[2];  // edx
    char v10[2];  // eax
    char *v11;  // edx
    unsigned int v12;  // eax
    char iter2[2];  // edx
    char v14[2];  // ecx
    char *v15;  // eax
    char v16[2];  // edx
    char v0;  // [bp-0x15]
    char v1[2];  // [bp-0x14]
    char *v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]
    unsigned int v4;  // [bp+0x4]
    unsigned int v5;  // [bp+0x8]
    char v6;  // [bp+0xc]
    int v7;  // [bp+0x10]

    v9 = v8;
    v3 = 4294967295;
    if (!v10)
        return;
    if (!v9 && !v10[0])
        return;
    if (!v11)
        return;
    if (!v7 && !*(v11))
        return;
    if (!v9)
        v9 = sub_4093c0();
    if (!v7)
        v7 = sub_4093c0();
    if (v9 > v7)
        return;
    v12 = v7 - v9;
    v0 = (!v6 ? v10[0] : *(&(&g_41e28c)[v10[0]]));
    v0 = v0;
    if (v5 > v4)
    {
        if (v12 >= v4)
        {
            if (v12 < v5)
                v5 = v12;
            iter = &v11[v5];
            v2 = &v11[v4];
            iter2 = &v10[1];
            v14 = &v10[v9 + 1];
            v1 = iter2;
            if (v6)
            {
                if (iter >= v2)
                {
                    while (true)
                    {
                        if (*(&(&g_41e28c)[*(iter)]) == v0)
                        {
                            for (node = iter + 1; v14 >= iter2 && *(&(&g_41e28c)[*(v15)]) == *(&(&g_41e28c)[iter2[0]]); iter2 = &iter2[1])
                            {
                                v15 += 1;
                            }
                            if (v14 < iter2)
                            {
                                v3 = node - v11 - 1;
                                return;
                            }
                            iter = node + 2;
                            v16 = v1;
                        }
                        else
                        {
                            iter += 1;
                            v16 = iter2;
                        }
                        iter2 = v16;
                        if (iter < v2)
                            return;
                    }
                }
                else
                {
                    return;
                }
            }
            else
            {
                if (iter >= v2)
                {
                    while (true)
                    {
                        if (*(iter) == v0)
                        {
                            for (node = iter + 1; v14 >= iter2 && *(v17) == iter2[0]; iter2 = &iter2[1])
                            {
                                v17 += 1;
                            }
                            if (v14 < iter2)
                            {
                                v3 = node - v11 - 1;
                                return;
                            }
                            iter = node + 2;
                            v19 = v1;
                        }
                        else
                        {
                            iter += 1;
                            v19 = iter2;
                        }
                        iter2 = v19;
                        if (iter < v2)
                            return;
                    }
                }
                else
                {
                    return;
                }
            }
        }
        else
        {
            return;
        }
    }
    else
    {
        if (v12 >= v5)
        {
            if (v12 < v4)
                v4 = v12;
            node = &v11[v5];
            v2 = &v11[v4];
            iter1 = &v10[1];
            v22 = &v10[v9 + 1];
            v1 = iter1;
            if (v6)
            {
                if (node <= v2)
                {
                    while (true)
                    {
                        if (*(&(&g_41e28c)[*(node)]) == v0)
                        {
                            for (node += 1; v22 >= iter1 && *(&(&g_41e28c)[*(v23)]) == *(&(&g_41e28c)[iter1[0]]); iter1 = &iter1[1])
                            {
                                v23 += 1;
                            }
                            if (v22 < iter1)
                            {
                                v3 = node - v11 - 1;
                                return;
                            }
                            v24 = v1;
                        }
                        else
                        {
                            node += 1;
                            v24 = iter1;
                        }
                        iter1 = v24;
                        if (node > v2)
                            return;
                    }
                }
                else
                {
                    return;
                }
            }
            else
            {
                if (node <= v2)
                {
                    while (true)
                    {
                        if (*(node) == v0)
                        {
                            for (node += 1; v22 >= iter1 && *(v25) == iter1[0]; iter1 = &iter1[1])
                            {
                                v25 += 1;
                            }
                            if (v22 < iter1)
                            {
                                v3 = node - v11 - 1;
                                return;
                            }
                            v26 = v1;
                        }
                        else
                        {
                            node += 1;
                            v26 = iter1;
                        }
                        iter1 = v26;
                        if (node > v2)
                            return;
                    }
                }
                else
                {
                    return;
                }
            }
        }
        else
        {
            return;
        }
    }
}
```

## `sub_00409611` `0x00409611`

_3 bytes. (leaf/helper — see body)_

```c
int sub_409611(void)
{
    sub_409614();
    return;
}
```

## `sub_00409614` `0x00409614`

_139 bytes. (leaf/helper — see body)_

```c
int sub_409614(void)
{
    unsigned int v5;  // ecx
    unsigned int v6;  // ebx
    unsigned int v15;  // 4119
    unsigned int v17;  // 4120
    unsigned int v18;  // eax
    unsigned int v19;  // edx
    unsigned int v20;  // edx
    unsigned int v21;  // ecx
    unsigned int v7;  // edx
    int v8;  // eax
    unsigned int v9;  // eax
    unsigned int v10;  // ebx
    unsigned int v11;  // eax
    unsigned int v12;  // edx
    unsigned int v13;  // edx
    unsigned int v14;  // ecx
    int v0;  // [bp-0x14]
    int v1;  // [bp-0x10]
    int v2;  // [bp-0xc]
    char v3;  // [bp+0x0]
    unsigned int v4;  // [bp+0x4]

    v6 = v5;
    if (!v7)
        return;
    v9 = sub_403c80(v0, v1, v2, v8, &v3);
    if (v6 > v4)
    {
        if (v9 >= v4)
        {
            v10 = v6;
            if (v9 < v10)
                v10 = v9;
            v11 = v10;
            if (v4 > v11)
                return;
            v12 = v4 - v11 - 1;
            while (true)
            {
                v13 = v12;
                v14 = *((char *)(v7 + v11 - 1));
                if ((*((char *)(v8 + (v14 >> 3))) >> ((char)v14 & 7) & 1) == 1)
                    return;
                v15 = _ccall(0, (unsigned int)(char)*((char *)(v8 + (v14 >> 3))) >> ((char)v14 & 7) & 1, 0, 0);
                v11 -= 1;
                v17 = _ccall(4, 18, v13 + 1, 0, v15);
                v12 = v13 + 1;
                if ((char)v17)
                    return;
            }
        }
        else
        {
            return;
        }
    }
    else
    {
        if (v9 >= v6)
        {
            if (v9 < v4)
                v4 = v9;
            v18 = v6;
            if (v4 < v18)
                return;
            v19 = v4 - v18 + 1;
            while (true)
            {
                v20 = v19;
                v21 = *((char *)(v7 + v18 - 1));
                if ((*((char *)(v8 + (v21 >> 3))) >> ((char)v21 & 7) & 1) == 1)
                    return;
                v18 += 1;
                v19 = v20 - 1;
                if (v20 == 1)
                    return;
            }
        }
        else
        {
            return;
        }
    }
}
```

## `sub_0040969f` `0x0040969f`

_1 bytes. (leaf/helper — see body)_

```c
int sub_40969f(void)
{
    sub_4096a0();
    return;
}
```

## `sub_004096a0` `0x004096a0`

_167 bytes. refs ";
            sub_4092cc(&v3, 0, "_

```c
typedef struct struct_0 {
    char field_0;
} struct_0;

int sub_4096a0(void)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    char v17;  // cl
    struct_0 **v18;  // eax
    unsigned long v19;  // 4118
    unsigned short v9;  // fs
    unsigned long v10;  // 4175
    unsigned int v11;  // 4115
    unsigned long v12;  // 4179
    int v13;  // edx
    int v14;  // edi
    int v15;  // esi
    int v16;  // ebx
    unsigned int v0;  // [bp-0x2c]
    int v1;  // [bp-0x28]
    unsigned int v2;  // [bp-0x24]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x4]
    char v5;  // [bp+0x0]
    char v6;  // [bp+0x4]

    v3 = 0;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v11 = *((int *)v10);
    v2 = *((int *)v10);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v12) = &v2;
    if (v13 > 0)
    {
        sub_403f60(v11, sub_409755, &v4, v14, v15, v16, 0, 0, &v5);
        sub_4028d0();
        if (!v17)
        {
            sub_403c88();
        }
        else if (v6 - 48 < 10 && *(v18) && *(v18)->field_0 == 45)
        {
            v1 = "-";
            sub_4092cc(&v3, 0, "-");
            sub_403d40(0);
        }
        else
        {
            sub_403ccc();
        }
    }
    v19 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v19) = v3;
    v0 = sub_40975c;
    sub_409747(v1, v11, sub_409755, &v4, v14, v15);
    return;
}
```

## `sub_00409747` `0x00409747`

_14 bytes. (leaf/helper — see body)_

```c
int sub_409747(void)
{
    return sub_403a34();
}
```

## `sub_00409755` `0x00409755`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_409755(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0040975a` `0x0040975a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40975a(void)
{
    return sub_409747();
}
```

## `sub_0040975c` `0x0040975c`

_9 bytes. (leaf/helper — see body)_

```c
void sub_40975c(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5)
{
    return;
}
```

## `sub_00409774` `0x00409774`

_70 bytes. (leaf/helper — see body)_

```c
int sub_409774(void)
{
    unsigned int v4;  // ecx
    int v5;  // edi
    int v6;  // esi
    int v7;  // ebx
    int v8;  // eax
    int v0;  // [bp-0x1c]
    int v1;  // [bp-0x8], Other Possible Types: unsigned int
    char v2;  // [bp+0x0]

    v1 = v4;
    v1 = _INSERT(v4, 3, v4);
    v8 = _INSERT(sub_403a64(v5, v6, v7, v1, &v2), 0, *((char *)((void*)&v1 + 3)));
    v0 = sub_403c80(v8);
    sub_4096a0(v8);
    return;
}
```

## `sub_004097ba` `0x004097ba`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4097ba(void)
{
    sub_4097bc();
    return;
}
```

## `sub_004097bc` `0x004097bc`

_176 bytes. (leaf/helper — see body)_

```c
int sub_4097bc(void)
{
    int v6;  // eax
    int i;  // ebx
    unsigned int v8;  // ecx
    int iter;  // esi
    int v10;  // ebx
    int v11;  // ebx
    int v13;  // ecx
    int v0;  // [bp-0x14]
    int v1;  // [bp-0x10]
    int v2;  // [bp-0xc]
    int v3;  // [bp-0x8]
    int v4;  // [bp-0x4]

    i = v6;
    if (!i)
    {
        sub_403a64(v13, v1, v2, v3, v4);
        return;
    }
    v0 = _INSERT(v8, 0, i < 0);
    sub_403f60(v0);
    iter = 11;
    do
    {
        v10 = i;
        v11 = v10 / 10;
        *((char *)(sub_403ed0() + iter - 1)) = (char)(((int)(v10 % 10) ^ (int)(v10 % 10) >> 31) - ((int)(v10 % 10) >> 31)) + 48;
        iter -= 1;
        i = v11;
    } while (i);
    if ((char)v0)
    {
        *((char *)(sub_403ed0() + iter - 1)) = 45;
        iter -= 1;
    }
    if (iter <= 0)
        return;
    sub_403ed0(sub_403ed0());
    sub_402628();
    sub_403f60();
    return;
}
```

## `sub_00409878` `0x00409878`

_227 bytes. (leaf/helper — see body)_

```c
int sub_409878(void)
{
    unsigned int v7;  // ecx
    unsigned int v8;  // ebx
    unsigned int v9;  // esi
    unsigned int v10;  // edi
    int iter;  // ebx
    unsigned int v12;  // eax
    int v13;  // edx
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]
    char v4;  // [bp-0x5]
    int i;  // [bp+0x4], Other Possible Types: unsigned int
    int j;  // [bp+0x8]

    v3 = v7;
    v2 = v8;
    v1 = v9;
    v0 = v10;
    if (!j)
    {
        if (!i)
        {
            sub_403a64();
            return;
        }
    }
    else
    {
        if (!j)
        {
            sub_403a64();
            return;
        }
    }
    v4 = (!j ? i < 0 : j < 0);
    sub_403f60();
    iter = 20;
    do
    {
        do
        {
            v12 = sub_404580(10, 0);
            if (v13 < 0)
                v12 = -(v12);
            i = sub_4044b8(10, 0);
            j = v13;
            *((char *)(sub_403ed0(10, 0) + iter - 1)) = (char)v12 + 48;
            iter -= 1;
        } while (j);
    } while (i);
    if (v4)
    {
        *((char *)(sub_403ed0() + iter - 1)) = 45;
        iter -= 1;
    }
    if (iter <= 0)
        return;
    sub_403ed0(sub_403ed0());
    sub_402628();
    sub_403f60();
    return;
}
```

## `sub_00409968` `0x00409968`

_161 bytes. (leaf/helper — see body)_

```c
int sub_409968(void)
{
    unsigned int v6;  // ecx
    unsigned int v7;  // eax
    unsigned int v8;  // ebx
    unsigned int v9;  // edi
    unsigned int v10;  // esi
    unsigned int v0;  // [bp-0x14]
    int v1;  // [bp-0x10]
    int v2;  // [bp-0xc]
    int v3;  // [bp-0x8]
    int v4;  // [bp-0x4]

    v0 = v6;
    if (!v7)
    {
        sub_403a64(v7, v1, v2, v3, v4);
        return;
    }
    v8 = v7;
    sub_403f60(v7, v1, v2, v3, v4);
    v9 = 8;
    do
    {
        v10 = v8 & 15;
        v8 >>= 4;
        if (v10 > 9)
            *((char *)(sub_403ed0() + v9 - 1)) = (char)v10 - -87;
        else
            *((char *)(sub_403ed0() + v9 - 1)) = (char)v10 - -48;
    } while ((v9 -= 1, v8));
    if (!v9)
        return;
    sub_403ed0(sub_403ed0() + v9);
    sub_402628();
    sub_403f60();
    return;
}
```

## `sub_00409a18` `0x00409a18`

_124 bytes. (leaf/helper — see body)_

```c
int sub_409a18(void)
{
    unsigned int v11;  // ebx
    unsigned int v12;  // esi
    unsigned long v13;  // ldt
    unsigned long v14;  // gdt
    unsigned short v15;  // fs
    unsigned long v16;  // 4172
    unsigned long v17;  // 4176
    unsigned long v18;  // 4118
    char *v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    char *v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]
    char v8;  // [bp-0x4]
    unsigned int v9;  // [bp+0x4]
    unsigned int v10;  // [bp+0x8]

    v7 = 0;
    v6 = 0;
    v5 = v11;
    v4 = v12;
    v3 = &v8;
    v2 = sub_409aa2;
    v16 = _ccall(v13, v14, (unsigned int)v15, 0);
    v1 = *((int *)v16);
    v17 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int **)v17) = &v1;
    if (!v10)
    {
        if (!v9)
            goto LABEL_409a7b;
LABEL_409a3d:
        sub_409968();
        if (v10)
        {
            v0 = &v7;
            sub_409774(&v7);
            sub_409968(v7);
            sub_403ccc();
        }
    }
    else
    {
        if (v10)
            goto LABEL_409a3d;
LABEL_409a7b:
        sub_403a64();
    }
    v18 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((char **)v18) = v0;
    v2 = sub_409aa9;
    sub_409a94();
    return;
}
```

## `sub_00409a94` `0x00409a94`

_14 bytes. (leaf/helper — see body)_

```c
int sub_409a94(void)
{
    return sub_403a34();
}
```

## `sub_00409aa2` `0x00409aa2`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_409aa2(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00409aa7` `0x00409aa7`

_2 bytes. (leaf/helper — see body)_

```c
int sub_409aa7(void)
{
    return sub_409a94();
}
```

## `sub_00409aa9` `0x00409aa9`

_8 bytes. (leaf/helper — see body)_

```c
void sub_409aa9(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4)
{
    return;
}
```

## `sub_00409ac0` `0x00409ac0`

_70 bytes. (leaf/helper — see body)_

```c
int sub_409ac0(void)
{
    unsigned int v4;  // ecx
    int v5;  // edi
    int v6;  // esi
    int v7;  // ebx
    int v8;  // eax
    int v0;  // [bp-0x1c]
    int v1;  // [bp-0x8], Other Possible Types: unsigned int
    char v2;  // [bp+0x0]

    v1 = v4;
    v1 = _INSERT(v4, 3, v4);
    v8 = _INSERT(sub_4097bc(v5, v6, v7, v1, &v2), 0, *((char *)((void*)&v1 + 3)));
    v0 = sub_403c80(v8);
    sub_4096a0(v8);
    return;
}
```

## `sub_00409b06` `0x00409b06`

_2 bytes. (leaf/helper — see body)_

```c
int sub_409b06(void)
{
    sub_409b08();
    return;
}
```

## `sub_00409b08` `0x00409b08`

_74 bytes. (leaf/helper — see body)_

```c
int sub_409b08(void)
{
    unsigned int v4;  // ecx
    int v5;  // eax
    int v6;  // edi
    int v7;  // esi
    int v8;  // ebx
    int v9;  // eax
    int v0;  // [bp-0x24]
    int v1;  // [bp-0x8], Other Possible Types: unsigned int
    char v2;  // [bp+0x0]

    v1 = v4;
    v1 = _INSERT(v4, 3, v4);
    v9 = _INSERT(sub_409878(v5, 0, v6, v7, v8, v1, &v2), 0, *((char *)((void*)&v1 + 3)));
    v0 = sub_403c80(v9);
    sub_4096a0(v9);
    return;
}
```

## `sub_00409b52` `0x00409b52`

_2 bytes. (leaf/helper — see body)_

```c
int sub_409b52(void)
{
    sub_409b54();
    return;
}
```

## `sub_00409b54` `0x00409b54`

_157 bytes. (leaf/helper — see body)_

```c
int sub_409b54(void)
{
    int v4;  // ecx
    int v5;  // eax
    int v6;  // edi
    int v7;  // esi
    int v8;  // ebx
    int v9;  // edx
    char v10;  // al
    char v11;  // al
    int v0;  // [bp-0x24]
    int v1;  // [bp-0x8]
    char v2;  // [bp+0x0]

    v1 = v4;
    sub_409a18(v5, 0, v6, v7, v8, v5, &v2);
    if (v9 >= 0)
    {
        v10 = v4;
        v11 = v10 - 58;
        if (v10 - 48 >= 10 && v11 - 7 >= 6 && v11 - 39 >= 6)
        {
            sub_403ccc();
            v0 = sub_403c80(v4);
            sub_4096a0(v4);
            return;
        }
    }
    v0 = sub_403c80(v4);
    sub_4096a0(v4);
    sub_403ccc();
    return;
}
```

## `sub_00409c00` `0x00409c00`

_119 bytes. (leaf/helper — see body)_

```c
int sub_409c00(void)
{
    int v2;  // ecx
    char v3;  // al
    char *v4;  // edx
    char v5;  // 4104
    int i;  // eax
    int j;  // eax
    char v0;  // [bp-0x10], Other Possible Types: int

    v0 = v2;
    v0 = v3;
    if (!v4)
        return;
    v5 = *(v4);
    if (v0)
    {
        i = v2 - 1;
        if (i > NULL)
        {
            do
            {
                i -= 1;
            } while (i != 1);
        }
    }
    else
    {
        j = v2 - 1;
        if (j > NULL)
        {
            do
            {
                j -= 1;
            } while (j != 1);
        }
    }
    return;
}
```

## `sub_00409caf` `0x00409caf`

_343 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[1860760645];
    char field_6ee8f445;
} struct_0;

extern unsigned int g_409e53;
extern void* g_41e490;

int sub_409caf(void)
{
    unsigned int v11;  // eax
    char *v12;  // eax
    unsigned short v21;  // ax
    unsigned int v22;  // 4142
    void* v23;  // eax
    char v24;  // 4098
    unsigned int v25;  // 4122
    unsigned int v26;  // 4123
    char *v27;  // eax
    char v28;  // cl
    enum FORMAT_MESSAGE_OPTIONS v29;  // edi
    unsigned long v30;  // ldt
    unsigned int v13;  // ebx
    unsigned long v31;  // gdt
    unsigned short v32;  // fs
    unsigned long v33;  // 4139
    unsigned long v34;  // 4148
    unsigned long v35;  // 4124
    unsigned int v36;  // 4103
    unsigned long v37;  // 4133
    int v38;  // ebx
    unsigned long v39;  // 4118
    unsigned long v40;  // 4118
    char *v14;  // edi
    struct_0 *idx;  // ebx
    unsigned int *v16;  // edx
    void* v17;  // esi
    char v18;  // 4109
    unsigned int v19;  // 4137
    unsigned int v20;  // 4139
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    unsigned int v5;  // [bp-0x4]
    int v7;  // [bp+0xfffe8]
    int v8;  // [bp+0xfffec]
    void* v9;  // [bp+0xffffc]

    v12 = (*((int *)(v11 * 2)))();
    *(v12) = *(v12) + *((char *)&v12);
    idx = _INSERT(v13, 1, *((char *)((void*)&v13 + 1)) + v14[v13]);
    *(v16) = *(v16) ^ v14;
    v18 = *((char *)v17);
    if (!(*((char *)((void*)&v12 + 1)) & v18))
    {
        v19 = _ccall(13, (unsigned int)(*((char *)((void*)&v12 + 1)) & v18), 0, 0);
        v20 = _ccall((unsigned short)v19 CONCAT (unsigned short)_INSERT(v12, 1, *((char *)((void*)&v12 + 1)) & v18), 39);
        v21 = v20;
        v22 = _ccall((unsigned short)(v20 >> 16) & 2261 CONCAT v21, 39);
        v23 = _INSERT(v21 CONCAT 0, 0, v22);
        if (*((char *)((void*)&v23 + 1)) == *(v14))
        {
            v24 = *((char *)v23);
            *((char *)v23) = *((char *)v23) & *((char *)((void*)&idx + 1));
            v25 = _ccall(13, (unsigned int)(v24 & *((char *)((void*)&idx + 1))), 0, 0);
            v26 = _ccall((unsigned short)v25 CONCAT *((unsigned short *)(void*)&v23), 55);
            v27 = _INSERT(v23, 0, v26);
            *(v14) = *(v14) ^ *((char *)((void*)&v27 + 1));
            *(v27) = *(v27) + *((char *)&v27);
            *(v27) = *(v27) + *((char *)&v27);
            sub_409ccc();
            return;
        }
    }
    else if ((idx & 0xc0000000))
    {
        v23 = g_41e490;
    }
    else
    {
        v29 = 0x1300;
        if (idx >= 0x834 && idx <= 0xbb7)
        {
            sub_409eac(0, 2);
            v9 = LoadLibraryExA(sub_403e78(0, 2), NULL, LOAD_LIBRARY_AS_DATAFILE);
            if (v9)
                v29 = 0x1b00;
        }
        else
        {
            v9 = NULL;
        }
        v5 = /* unsupported instruction */;
        v4 = sub_409e70;
        v33 = _ccall(v30, v31, (unsigned int)v32, 0);
        v3 = *((int *)v33);
        v34 = _ccall(v30, v31, (unsigned int)v32, 0);
        *((unsigned int **)v34) = &v3;
        if (!FormatMessageA(v29, v9, idx, 0x400, /* unsupported instruction */ - 4, 0, NULL))
        {
            sub_409eac();
            sub_409b54(/* unsupported instruction */ - 28, " ", v8);
            sub_403d40(v7);
            v40 = _ccall(v30, v31, (unsigned int)v32, 0);
            *((int *)v40) = v7;
            v1 = sub_409e77;
            sub_409e60();
            return;
        }
        v35 = _ccall(v30, v31, (unsigned int)v32, 0);
        v36 = *((int *)v35);
        v0 = *((int *)v35);
        v37 = _ccall(v30, v31, (unsigned int)v32, 0);
        *((unsigned int **)v37) = &v0;
        sub_403be8(v36, sub_409e16, /* unsupported instruction */);
        v38 = sub_403c80(v36, sub_409e16, /* unsupported instruction */);
        if (v38)
        {
            do
            {
                if (*((char *)(*((int *)v17) + v38 - 1)) == 13)
                {
                    *((char *)(sub_403ed0() + v38 - 1)) = 32;
                }
                else if (*((char *)(*((int *)v17) + v38 - 1)) == 10)
                {
                    sub_403f18();
                }
            } while ((v38 = (int)(v38 - 1), v38));
        }
        v39 = _ccall(v30, v31, (unsigned int)v32, 0);
        *((unsigned int *)v39) = v36;
        v2 = &g_409e53;
        sub_409e0c();
        return;
    }
    *(v14) = *((char *)&v23);
    *((void* *)v23) = *((int *)v23) + v23;
    idx->field_6ee8f445 = idx->field_6ee8f445 + v28;
}
```

## `sub_00409ccc` `0x00409ccc`

_33 bytes. (leaf/helper — see body)_

```c
int sub_409ccc(void)
{
    unsigned int v15;  // ebx
    unsigned int v16;  // esi
    unsigned int v17;  // edi
    unsigned long v18;  // ldt
    unsigned long v19;  // gdt
    unsigned short v20;  // fs
    unsigned long v21;  // 4172
    unsigned long v22;  // 4181
    unsigned int v0;  // [bp-0x38]
    unsigned int v1;  // [bp-0x34]
    char *v2;  // [bp-0x30]
    unsigned int v3;  // [bp-0x2c]
    unsigned int v4;  // [bp-0x28]
    unsigned int v5;  // [bp-0x24]
    unsigned int v6;  // [bp-0x20]
    unsigned int v7;  // [bp-0x1c]
    unsigned int v8;  // [bp-0x18]
    unsigned int v9;  // [bp-0x14]
    unsigned int v10;  // [bp-0x10]
    unsigned int v11;  // [bp-0xc]
    unsigned int v12;  // [bp-0x8]
    char v13;  // [bp-0x4]

    v12 = 0;
    v11 = 0;
    v10 = 0;
    v9 = 0;
    v8 = 0;
    v7 = 0;
    v6 = 0;
    v5 = v15;
    v4 = v16;
    v3 = v17;
    v2 = &v13;
    v1 = sub_409e92;
    v21 = _ccall(v18, v19, (unsigned int)v20, 0);
    v0 = *((int *)v21);
    v22 = _ccall(v18, v19, (unsigned int)v20, 0);
    *((unsigned int **)v22) = &v0;
}
```

## `sub_00409d18` `0x00409d18`

_29 bytes. (leaf/helper — see body)_

```c
int sub_409d18(void)
{
    unsigned int *v2;  // eax
    unsigned int v3;  // ebx
    PSTR v0;  // [bp+0x0]

    v2 = GetProcAddress(sub_4052c4(sub_403e78()), v0);
    if (!v2)
        goto LABEL_0x409d35;
    v2(v3);
}
```

## `sub_00409e0c` `0x00409e0c`

_10 bytes. (leaf/helper — see body)_

```c
HLOCAL sub_409e0c(void)
{
    HLOCAL v1;  // [bp+0x100000]

    return LocalFree(v1);
}
```

## `sub_00409e16` `0x00409e16`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_409e16(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00409e1b` `0x00409e1b`

_2 bytes. (leaf/helper — see body)_

```c
HLOCAL sub_409e1b(void)
{
    return sub_409e0c();
}
```

## `sub_00409e60` `0x00409e60`

_16 bytes. (leaf/helper — see body)_

```c
int sub_409e60(void)
{
    int v2;  // eax
    unsigned int v1;  // [bp+0xffffc]

    if (v1)
        v2 = sub_405224(v1);
    return v2;
}
```

## `sub_00409e70` `0x00409e70`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_409e70(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00409e75` `0x00409e75`

_2 bytes. (leaf/helper — see body)_

```c
int sub_409e75(void)
{
    return sub_409e60();
}
```

## `sub_00409e77` `0x00409e77`

_13 bytes. (leaf/helper — see body)_

```c
int sub_409e77(unsigned int a0, unsigned int a1)
{
    unsigned long v1;  // ldt
    unsigned long v2;  // gdt
    unsigned short v3;  // fs
    unsigned long v4;  // 4118
    unsigned int v0;  // [bp+0x0]

    v4 = _ccall(v1, v2, (unsigned int)v3, 0);
    *((unsigned int *)v4) = v0;
    a1 = sub_409e99;
    return sub_409e84();
}
```

## `sub_00409e84` `0x00409e84`

_14 bytes. (leaf/helper — see body)_

```c
int sub_409e84(void)
{
    return sub_403a34();
}
```

## `sub_00409e92` `0x00409e92`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_409e92(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00409e97` `0x00409e97`

_2 bytes. (leaf/helper — see body)_

```c
int sub_409e97(void)
{
    return sub_409e84();
}
```

## `sub_00409e99` `0x00409e99`

_7 bytes. (leaf/helper — see body)_

```c
void sub_409e99(unsigned int a0, unsigned int a1)
{
    return;
}
```

## `sub_00409eac` `0x00409eac`

_52 bytes. (leaf/helper — see body)_

```c
int sub_409eac(void)
{
    int i;  // eax
    unsigned int v4;  // edx
    unsigned int *v5;  // edx
    int v0;  // [bp-0x8]
    int v1;  // [bp-0x4]

    sub_403a64(v0, v1);
    sub_403ec8(v0, v1);
    i = sub_403c80();
    if (i <= 0)
        return;
    v4 = 1;
    do
    {
        *((char *)(*(v5) + v4 - 1)) = *((char *)(*(v5) + v4 - 1)) ^ 0x55;
        v4 += 1;
        i -= 1;
    } while (i != 1);
    return;
}
```

