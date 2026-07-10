# elfbot.dll decompiled — loader 0x004034e9..0x00403c88

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_004034e9` `0x004034e9`

_3 bytes. (leaf/helper — see body)_

```c
int sub_4034e9(void)
{
    return sub_4034ec();
}
```

## `sub_004034ec` `0x004034ec`

_47 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

void sub_4034ec(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int a10, unsigned int *a11)
{
    struct_0 **v0;  // eax
    unsigned long v1;  // ldt
    unsigned long v2;  // gdt
    unsigned short v3;  // fs
    unsigned long v4;  // 4122
    unsigned int v5;  // edx

    v0 = sub_404fdc();
    *(v0) = *(v0)->field_0;
    sub_402e1c();
    v4 = _ccall(v1, v2, (unsigned int)v3, 0);
    *((unsigned int *)v4) = *(a11);
    sub_403084();
    goto v5;
}
```

## `sub_0040351b` `0x0040351b`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40351b(void)
{
    return;
}
```

## `sub_0040351c` `0x0040351c`

_21 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[5];
    unsigned int field_5;
} struct_0;

int sub_40351c(unsigned int a0, struct_0 *a1)
{
    unsigned long v0;  // ldt
    unsigned long v1;  // gdt
    unsigned short v2;  // fs
    unsigned long v3;  // 4120

    v3 = _ccall(v0, v1, (unsigned int)v2, 0);
    *((unsigned int *)v3) = a0;
    return (struct struct_0 *)(a1->padding_0)[1]();
}
```

## `sub_00403531` `0x00403531`

_1 bytes. (leaf/helper — see body)_

```c
void sub_403531(void)
{
    return;
}
```

## `sub_00403532` `0x00403532`

_2 bytes. (leaf/helper — see body)_

```c
int sub_403532(unsigned int a0)
{
    return sub_403534();
}
```

## `sub_00403534` `0x00403534`

_160 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    int field_0;
    char padding_4[8];
    unsigned int field_c;
} struct_0;

void sub_403534(unsigned int a0, struct_0 *a1)
{
    int v0;  // eax
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v3;  // eax

    v0 = a1->field_0;
    if (v0 <= -1073741678)
    {
        if (v0 == -1073741678)
        {
            sub_402594(a0, a1->field_c);
            return;
        }
        else if (v0 > -1073741682)
        {
            v2 = v0 + 0x3fffff71;
            if (v2 < 2)
            {
                sub_402594(a0, a1->field_c);
                return;
            }
            if (v2 == 2)
            {
                sub_402594(a0, a1->field_c);
                return;
            }
        }
        else if (v0 != -1073741682)
        {
            v1 = v0 + 0x3ffffffb;
            if (v0 == -1073741819)
            {
                sub_402594(a0, a1->field_c);
                return;
            }
            else if (v1 == 135)
            {
                sub_402594(a0, a1->field_c);
                return;
            }
            else if (v1 == 0x88)
            {
                sub_402594(a0, a1->field_c);
                return;
            }
        }
        else
        {
            sub_402594(a0, a1->field_c);
            return;
        }
    }
    else
    {
        if (v0 <= -1073741674)
        {
            if (v0 != -1073741674)
            {
                v3 = v0 + 0x3fffff6d;
                if (v0 == -1073741677)
                {
                    sub_402594(a0, a1->field_c);
                    return;
                }
                else if (v3 == 1)
                {
                    sub_402594(a0, a1->field_c);
                    return;
                }
                else if (v3 == 2)
                {
                    sub_402594(a0, a1->field_c);
                    return;
                }
            }
            else
            {
                sub_402594(a0, a1->field_c);
                return;
            }
        }
        else
        {
            if (v0 == -1073741571)
            {
                sub_402594(a0, a1->field_c);
                return;
            }
            else if (v0 == -1073741510)
            {
                sub_402594(a0, a1->field_c);
                return;
            }
        }
    }
    sub_402594(a0, a1->field_c);
    return;
}
```

## `sub_004035d4` `0x004035d4`

_141 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern char g_41e010;
extern struct_1 *g_420004;
extern struct_1 *g_420010;
extern struct_1 *g_420018;

int sub_4035d4(struct_0 *a0, struct_0 *a1)
{
    unsigned int v1;  // eax
    unsigned int v2;  // ecx
    unsigned int v3;  // ecx
    unsigned int *v0;  // [bp-0xc]

    if (((char)a0->field_4 & 6))
        return 0;
    if (g_41e010 <= 0 && !UnhandledExceptionFilter(&/* unsupported instruction */))
        return 0;
    v1 = (unsigned int)sub_402db4();
    g_420018(a1, v0, v1, 0);
    if (*(v0) != 250477278)
    {
        if (!g_420010)
        {
            return (unsigned int)sub_403534(v3, a1);
        }
        else if (!g_420010())
        {
            return (unsigned int)sub_403534(v2, a1);
        }
    }
    sub_4030a0();
    if (!g_420004)
        return sub_40365e();
    g_420004();
    return sub_40365e();
}
```

## `sub_0040365e` `0x0040365e`

_16 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    int field_14;
} struct_0;

int sub_40365e(struct_0 *a0)
{
    return sub_403a04(a0->field_14);
}
```

## `sub_00403671` `0x00403671`

_3 bytes. (leaf/helper — see body)_

```c
int sub_403671(void)
{
    return sub_403674();
}
```

## `sub_00403674` `0x00403674`

_29 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420630;

int sub_403674(void)
{
    unsigned int v4;  // eax
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4121
    unsigned int v9;  // 4125
    unsigned long v10;  // 4129
    unsigned int v1;  // [bp+0xffff8]
    unsigned int v2;  // [bp+0xffffc]
    unsigned int v3;  // [bp+0x100000]

    v4 = /* unsupported instruction */ - 12;
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v9 = *((int *)v8);
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v10) = v4;
    v1 = v9;
    v2 = sub_4035d4;
    v3 = /* unsupported instruction */;
    g_420630 = v4;
    return v4;
}
```

## `sub_00403691` `0x00403691`

_3 bytes. (leaf/helper — see body)_

```c
int sub_403691(void)
{
    return sub_403694();
}
```

## `sub_00403694` `0x00403694`

_40 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
} struct_0;

extern struct_0 *g_420630;

struct_0 ** sub_403694(void)
{
    unsigned long v1;  // ldt
    unsigned long v2;  // gdt
    unsigned short v3;  // fs
    unsigned long v4;  // 4120
    struct_0 **i;  // ecx
    struct_0 **v6;  // eax
    unsigned long v7;  // 4108
    struct_0 **v8;  // eax

    if (!g_420630)
        return g_420630;
    v4 = _ccall(v1, v2, (unsigned int)v3, 0);
    if (g_420630 == *((int *)v4))
    {
        v6 = g_420630->field_0;
        v7 = _ccall(v1, v2, (unsigned int)v3, 0);
        *((struct_0 ***)v7) = v6;
        return v6;
    }
    for (i = *((int *)v4); i != 0xffffffff; i = *(i))
    {
        if (*(i) == g_420630)
        {
            v8 = g_420630->field_0;
            *(i) = v8;
            return v8;
        }
    }
    return g_420630;
}
```

## `sub_004036bc` `0x004036bc`

_75 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern struct_0 *g_420634;
extern int g_420638;

struct_0 * sub_4036bc(void)
{
    int i;  // ebx
    unsigned int v6;  // esi
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4155
    unsigned long v11;  // 4159
    unsigned long v12;  // 4116
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    char *v2;  // [bp-0x14]
    char v3;  // [bp-0x4]

    if (!g_420634)
        return g_420634;
    i = g_420638;
    v6 = g_420634->field_4;
    v2 = &v3;
    v1 = sub_403702;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v0 = *((int *)v10);
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v0;
    if (g_420638 > NULL)
    {
        do
        {
            i -= 1;
            g_420638 = i;
            if (*((int *)(v6 + i * 8 + 4)))
                (*((int *)(v6 + i * 8 + 4)))();
        } while (i > NULL);
    }
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v0;
    return NULL;
}
```

## `sub_00403702` `0x00403702`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
    char padding_8[4];
    void* field_c;
    char padding_10[4];
    void* field_14;
    void* field_18;
} struct_1;

unsigned int sub_403702(int a0)
{
    struct_1 *v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x8]

    return sub_4030c0(v0, a0, v1);
}
```

## `sub_00403707` `0x00403707`

_15 bytes. (leaf/helper — see body)_

```c
void sub_403707(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int a10)
{
    unsigned int v0;  // [bp+0x0]

    sub_4036bc();
    sub_403498(v0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10);
    sub_4034ec(v0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10);
}
```

## `sub_0040371b` `0x0040371b`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40371b(void)
{
    sub_40371c();
    return;
}
```

## `sub_0040371c` `0x0040371c`

_75 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    int field_0;
    unsigned int field_4;
} struct_0;

extern struct_0 *g_420634;
extern unsigned int g_420638;

unsigned int [2] sub_40371c(void)
{
    int i;  // esi
    int idx;  // ebx
    unsigned int v7;  // edi
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4156
    unsigned long v12;  // 4160
    unsigned int *v13;  // eax
    unsigned long v14;  // 4116
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    char *v2;  // [bp-0x14]
    char v3;  // [bp-0x4]

    if (!g_420634)
        return g_420634;
    i = g_420634->field_0;
    idx = 0;
    v7 = g_420634->field_4;
    v2 = &v3;
    v1 = sub_403762;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v0 = *((int *)v11);
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v0;
    if (i > NULL)
    {
        do
        {
            v13 = *((int *)(v7 + idx * 8));
            idx += 1;
            g_420638 = idx;
            if (v13)
                v13();
        } while (i > idx);
    }
    v14 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v14) = v0;
    return NULL;
}
```

## `sub_00403762` `0x00403762`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
    char padding_8[4];
    void* field_c;
    char padding_10[4];
    void* field_14;
    void* field_18;
} struct_1;

unsigned int sub_403762(int a0)
{
    struct_1 *v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x8]

    return sub_4030c0(v0, a0, v1);
}
```

## `sub_00403767` `0x00403767`

_15 bytes. (leaf/helper — see body)_

```c
void sub_403767(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int a10)
{
    unsigned int v0;  // [bp+0x0]

    sub_4036bc();
    sub_403498(v0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10);
    sub_4034ec(v0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10);
}
```

## `sub_0040377b` `0x0040377b`

_1 bytes. (leaf/helper — see body)_

```c
int sub_40377b(void)
{
    sub_40377c();
    return;
}
```

## `sub_0040377c` `0x0040377c`

_64 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern char g_401080;
extern char g_401088;
extern unsigned int g_420014;
extern unsigned int g_420018;
extern unsigned int g_42002c;
extern char g_420034;
extern unsigned int g_420634;
extern unsigned int g_420638;
extern unsigned int g_42063c;

int sub_40377c(void)
{
    unsigned int v1;  // eax
    struct_0 *v2;  // edx

    g_420014 = &g_401080;
    g_420018 = &g_401088;
    g_420634 = v1;
    g_420638 = 0;
    g_42063c = v2;
    g_42002c = v2->field_4;
    sub_403674();
    g_420034 = 0;
    sub_40371c();
    return;
}
```

## `sub_004037bc` `0x004037bc`

_37 bytes. (leaf/helper — see body)_

```c
int sub_4037bc(void)
{
    unsigned int *v4;  // eax
    unsigned int v5;  // edi
    unsigned int i;  // edi
    unsigned int v7;  // edi
    int v0;  // [bp-0xc]
    int v1;  // [bp-0x8]
    int v2;  // [bp-0x4]

    v5 = *(v4);
    do
    {
        i = v5;
        sub_404e44(v0, v1, v2);
        v7 = i - 1;
        v5 = v7;
    } while (i != 1);
    return;
}
```

## `sub_004037e1` `0x004037e1`

_3 bytes. (leaf/helper — see body)_

```c
int sub_4037e1(void)
{
    sub_4037e4();
    return;
}
```

## `sub_004037e4` `0x004037e4`

_36 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    struct struct_1 *field_4;
    struct struct_1 *field_8;
    unsigned int field_c;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_4037e4(void)
{
    struct_0 *v1;  // eax
    unsigned int i;  // edi
    struct_0 *idx;  // esi

    i = v1->field_0;
    idx = &v1->field_4;
    do
    {
        *((struct struct_1 **)idx->field_0) = idx->field_4->field_0 + (char *)idx->field_8;
        idx = &idx->field_c;
        i -= 1;
    } while (i != 1);
    return;
}
```

## `sub_00403808` `0x00403808`

_90 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_41e000;
extern unsigned int g_41e004;

unsigned int sub_403808(void)
{
    unsigned int v1;  // ecx
    unsigned int i;  // ebx
    unsigned int v3;  // ecx
    unsigned int j;  // eax

    v1 = _INSERT(0, 0, 16);
    i = g_41e000;
    do
    {
        *((char *)(4317260 + (char)v1)) = (char)(i % 10) + 48;
        i /= 10;
        v1 -= 1;
    } while (i);
    v3 = _INSERT(v1, 0, 28);
    j = g_41e004;
    do
    {
        *((char *)(4317260 + (char)v3)) = *((char *)(4317300 + (j & 15)));
        j >>= 4;
        v3 -= 1;
    } while (j);
    return 0;
}
```

## `sub_00403862` `0x00403862`

_2 bytes. (leaf/helper — see body)_

```c
int sub_403862(void)
{
    return sub_403864();
}
```

## `sub_00403864` `0x00403864`

_45 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern char g_41e000;
extern struct_0 *g_42062c;
extern unsigned int g_420648;
extern unsigned int g_42064c;

unsigned int sub_403864(void)
{
    struct_0 **iter;  // edi
    unsigned int *i;  // esi
    unsigned int v5;  // ecx
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp-0x4]

    InterlockedExchange(&g_41e000, 0);
    iter = &g_42062c;
    v1 = g_420648;
    v0 = g_42064c;
    i = &g_42062c->field_0;
    for (v5 = 11; v5; i += 1)
    {
        v5 -= 1;
        *(iter) = *(i);
        iter += 1;
    }
    return 0;
}
```

## `sub_00403891` `0x00403891`

_1 bytes. (leaf/helper — see body)_

```c
void sub_403891(void)
{
    return;
}
```

## `sub_00403892` `0x00403892`

_2 bytes. (leaf/helper — see body)_

```c
int sub_403892(void)
{
    return sub_403894();
}
```

## `sub_00403894` `0x00403894`

_127 bytes. calls MessageBoxA, WriteFile; refs "Runtime error     at 00000000", "\r\n", "Runtime error     at 00000000"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern char g_41e018;
extern char g_420044;
extern unsigned short g_420218;
extern unsigned int g_420220;
extern struct_0 *g_420230;

int sub_403894(unsigned int a0)
{
    unsigned int v3;  // eax
    unsigned int v0;  // [bp-0x4]

    v0 = a0;
    if (g_420044)
    {
        if (g_420218 == 55218 && g_420220 > 0)
            g_420230();
        WriteFile(GetStdHandle(STD_OUTPUT_HANDLE), "Runtime error     at 00000000", 30, &v0, NULL);
        return WriteFile(GetStdHandle(STD_OUTPUT_HANDLE), "\r\n", 2, &v0, NULL);
    }
    else
    {
        if (!g_41e018)
            v3 = (unsigned int)MessageBoxA(NULL, "Runtime error     at 00000000", "Error", MB_APPLMODAL);
        return v3;
    }
}
```

## `sub_00403920` `0x00403920`

_211 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern unsigned int g_41e000;
extern unsigned int g_41e004;
extern struct_0 *g_420024;
extern struct_0 *g_420040;
extern struct_0 *g_42062c;
extern unsigned int g_420638;
extern char g_42063c;
extern struct_0 *g_420650;
extern char g_420654;

void sub_403920(void)
{
    unsigned int v5;  // ebx
    unsigned int v6;  // esi
    unsigned int v7;  // edi
    struct_0 **v8;  // ebx
    unsigned int *v9;  // edx
    unsigned int v10;  // ecx
    unsigned int v11;  // eax
    unsigned int *i;  // eax
    unsigned int v13;  // ecx
    struct_0 **iter;  // edi
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    unsigned int v3;  // [bp-0x4]

    v3 = v5;
    v2 = v6;
    v1 = v7;
    v8 = &g_42062c;
    if (!g_420654 && g_420040)
    {
        do
        {
            v9 = &g_420040->field_0;
            g_420040 = 0;
            v9();
        } while (g_420040);
    }
    if (g_41e004)
    {
        sub_403808();
        sub_403894(v10);
        g_41e004 = 0;
    }
    while (true)
    {
        if (g_420654 == 2 && !g_41e000)
            g_420638 = 0;
        sub_4036bc();
        if ((g_420654 <= 1 || g_41e000) && *((int *)&g_42063c))
        {
            sub_404d90();
            v11 = *((int *)(*((int *)&g_42063c) + 16));
            if (v11 != *((int *)(*((int *)&g_42063c) + 4)) && v11)
                FreeLibrary(v11);
        }
        sub_403694();
        if (g_420654 == 1)
            g_420650();
        if (g_420654)
            sub_403864();
        if (!g_42062c)
            break;
        i = &g_42062c->field_0;
        v0 = &g_41e000;
        v13 = 11;
        for (iter = v8; v13; i += 1)
        {
            v13 -= 1;
            *(iter) = *(i);
            iter += 1;
        }
    }
    if (g_420024)
        g_420024();
    ExitProcess(g_41e000); /* do not return */
}
```

## `sub_004039f3` `0x004039f3`

_5 bytes. (leaf/helper — see body)_

```c
void sub_4039f3(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    return;
}
```

## `sub_004039f8` `0x004039f8`

_11 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_41e000;

int sub_4039f8(void)
{
    unsigned int v1;  // eax

    g_41e000 = v1;
    sub_403920(); /* do not return */
}
```

## `sub_00403a03` `0x00403a03`

_1 bytes. (leaf/helper — see body)_

```c
void sub_403a03(void)
{
    sub_403a04();
    return;
}
```

## `sub_00403a04` `0x00403a04`

_11 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_41e004;

int sub_403a04(void)
{
    unsigned int v0;  // [bp+0x0]

    g_41e004 = v0;
    sub_4039f8();
    return;
}
```

## `sub_00403a0f` `0x00403a0f`

_1 bytes. (leaf/helper — see body)_

```c
void sub_403a0f(void)
{
    return;
}
```

## `sub_00403a10` `0x00403a10`

_35 bytes. (leaf/helper — see body)_

```c
int sub_403a10(void)
{
    void* *v1;  // eax
    void* v2;  // edx
    unsigned int v3;  // 4108
    unsigned int v4;  // 4114

    v2 = *(v1);
    if (!v2)
        return;
    *(v1) = NULL;
    v3 = _ccall(15, v2, 0, 0);
    v4 = _ccall(12, 21, (int)v2[8] - 1, 0, v3);
    if ((char)v4)
        return;
    InterlockedDecrement(v2 - 8);
    if ((int)v2[8] != 1)
        return;
    sub_402524(v1);
    return;
}
```

## `sub_00403a33` `0x00403a33`

_1 bytes. (leaf/helper — see body)_

```c
int sub_403a33(void)
{
    sub_403a34();
    return;
}
```

## `sub_00403a34` `0x00403a34`

_47 bytes. (leaf/helper — see body)_

```c
int sub_403a34(void)
{
    void* *v1;  // eax
    void* *iter;  // ebx
    unsigned int v3;  // edx
    unsigned int v4;  // esi
    unsigned int v5;  // esi
    void* v6;  // edx
    unsigned int v7;  // 4108
    unsigned int v8;  // 4114
    unsigned int v9;  // esi

    iter = v1;
    v4 = v3;
    do
    {
        v5 = v4;
        v6 = *(iter);
        if (v6)
        {
            *(iter) = NULL;
            v7 = _ccall(15, v6, 0, 0);
            v8 = _ccall(12, 21, (int)v6[8] - 1, 0, v7);
            if (!((char)v8))
            {
                InterlockedDecrement(v6 - 8);
                if ((int)v6[8] == 1)
                    sub_402524();
            }
        }
    } while ((iter += 4, v9 = v5 - 1, v4 = v5 - 1, v5 != 1));
    return;
}
```

## `sub_00403a63` `0x00403a63`

_1 bytes. (leaf/helper — see body)_

```c
void sub_403a63(unsigned int a0, unsigned int a1)
{
    sub_403a64();
    return;
}
```

## `sub_00403a64` `0x00403a64`

_67 bytes. (leaf/helper — see body)_

```c
int sub_403a64(void)
{
    void* v2;  // edx
    void* v3;  // edx
    unsigned int v4;  // 4107
    unsigned int v5;  // 4113
    void* *v6;  // eax
    void* *v7;  // eax
    void* v8;  // edx
    unsigned int v9;  // 4107
    unsigned int v10;  // 4113
    void* v0;  // [bp-0x8]

    v3 = v2;
    if (v3)
    {
        v4 = _ccall(15, v2, 0, 0);
        v5 = _ccall(14, 18, (int)v2[8] + 1, 0, v4);
        if ((char)v5)
        {
            v0 = sub_403ad4(v2, v6);
            sub_402628(sub_403ad4(v2, v6));
            v3 = v0;
        }
        else
        {
            InterlockedIncrement(v2 - 8);
            v3 = v2;
        }
    }
    InterlockedExchange(v7, v3);
    v8 = *(v7);
    if (v8)
    {
        v9 = _ccall(15, v8, 0, 0);
        v10 = _ccall(12, 21, (int)v8[8] - 1, 0, v9);
        if (!((char)v10))
        {
            InterlockedDecrement(v8 - 8);
            if ((int)v8[8] == 1)
                sub_402524();
        }
    }
    return;
}
```

## `sub_00403aa7` `0x00403aa7`

_1 bytes. (leaf/helper — see body)_

```c
void sub_403aa7(unsigned int a0, unsigned int a1)
{
    sub_403aa8();
    return;
}
```

## `sub_00403aa8` `0x00403aa8`

_41 bytes. (leaf/helper — see body)_

```c
int sub_403aa8(void)
{
    void* v1;  // edx
    unsigned int v2;  // 4107
    unsigned int v3;  // 4113
    void* *v4;  // eax
    void* v5;  // edx
    unsigned int v6;  // 4107
    unsigned int v7;  // 4113

    if (v1)
    {
        v2 = _ccall(15, v1, 0, 0);
        v3 = _ccall(14, 18, (int)v1[8] + 1, 0, v2);
        if (!((char)v3))
            InterlockedIncrement(v1 - 8);
    }
    InterlockedExchange(v4, v1);
    v5 = *(v4);
    if (v5)
    {
        v6 = _ccall(15, v5, 0, 0);
        v7 = _ccall(12, 21, (int)v5[8] - 1, 0, v6);
        if (!((char)v7))
        {
            InterlockedDecrement(v5 - 8);
            if ((int)v5[8] == 1)
                sub_402524();
        }
    }
    return;
}
```

## `sub_00403ad1` `0x00403ad1`

_3 bytes. (leaf/helper — see body)_

```c
int sub_403ad1(void)
{
    sub_403ad4();
    return;
}
```

## `sub_00403ad4` `0x00403ad4`

_43 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    int field_4;
} struct_0;

int sub_403ad4(void)
{
    int v1;  // eax
    struct_0 *v2;  // eax
    struct_0 *v3;  // eax

    if (v1 > 0)
    {
        v2 = sub_402504(v1 + 10 & 4294967294, v1);
        *((unsigned short *)(-2 + (v1 + 10 & 4294967294) + (char *)v2)) = 0;
        v3 = v2 + 1;
        v3->field_4 = v1;
        v3[1].field_0 = 1;
    }
    return;
}
```

## `sub_00403aff` `0x00403aff`

_1 bytes. (leaf/helper — see body)_

```c
int sub_403aff(void)
{
    sub_403b00();
    return;
}
```

## `sub_00403b00` `0x00403b00`

_46 bytes. (leaf/helper — see body)_

```c
int sub_403b00(void)
{
    int v4;  // eax
    unsigned int v5;  // edx
    int *v6;  // eax
    int v0;  // [bp-0xc]
    int v1;  // [bp-0x8]
    int v2;  // [bp-0x4]

    v4 = sub_403ad4(v0, v1, v2);
    if (v5)
        sub_402628();
    sub_403a10();
    *(v6) = v4;
    return;
}
```

## `sub_00403b2e` `0x00403b2e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_403b2e(void)
{
    sub_403b30();
    return;
}
```

## `sub_00403b30` `0x00403b30`

_27 bytes. (leaf/helper — see body)_

```c
int sub_403b30(void)
{
    LPArray v1;  // ecx
    PSTR v2;  // eax
    int v3;  // edx
    int v0;  // [bp+0x4]

    WideCharToMultiByte(0, 0, v1, v0, v2, v3, NULL, NULL);
    return;
}
```

## `sub_00403b4b` `0x00403b4b`

_141 bytes. (leaf/helper — see body)_

```c
int sub_403b4b(void)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // esi
    unsigned int v8;  // edi
    int v9;  // ecx
    int v10;  // edx
    int v11;  // eax
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    unsigned int v3;  // [bp-0x4]

    v3 = v6;
    v2 = v7;
    v1 = v8;
    v0 = /* unsupported instruction */;
    if (v9 <= 0)
    {
        sub_403a10(v10, v11);
        return;
    }
    if (v9 + 1 < 0x7ff && sub_403b30(v9) >= 0)
    {
        sub_403b00();
        return;
    }
    sub_403f60();
    sub_403f60();
    return;
}
```

## `sub_00403bd8` `0x00403bd8`

_15 bytes. (leaf/helper — see body)_

```c
void sub_403bd8(unsigned int a0, int a1)
{
    sub_403b00(a1);
    return;
}
```

## `sub_00403be7` `0x00403be7`

_1 bytes. (leaf/helper — see body)_

```c
void sub_403be7(unsigned int a0, unsigned int a1)
{
    sub_403be8();
    return;
}
```

## `sub_00403be8` `0x00403be8`

_44 bytes. (leaf/helper — see body)_

```c
int sub_403be8(void)
{
    char v2[4];  // edx
    char v3[4];  // edx
    char v0[4];  // [bp-0x4]

    if (!v2)
    {
        sub_403b00();
        return;
    }
    v0 = v2;
    while (v3[0])
    {
        if (!v3[1])
            break;
        if (!v3[2])
        {
            break;
        }
        else if (v3[3])
        {
            v3 += 1;
        }
        else
        {
LABEL_403c07:
            goto LABEL_403c07;
        }
    }
    sub_403b00();
    return;
}
```

## `sub_00403c18` `0x00403c18`

_56 bytes. (leaf/helper — see body)_

```c
void sub_403c18(unsigned int a0, unsigned short *a1)
{
    unsigned short v0[4];  // [bp-0x4]

    if (a1)
    {
        v0 = a1;
        while (*(a1))
        {
            if (!a1[1])
            {
LABEL_403c41:
                break;
            }
            if (!a1[2])
            {
LABEL_403c3e:
                goto LABEL_403c41;
            }
            else if (a1[3])
            {
                a1 += 4;
            }
            else
            {
                goto LABEL_403c3e;
            }
        }
    }
}
```

## `sub_00403c54` `0x00403c54`

_23 bytes. (leaf/helper — see body)_

```c
int sub_403c54(void)
{
    unsigned int v3;  // eax
    unsigned int v4;  // ecx
    char *v5;  // edi
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v1 = v3;
    v0 = v4;
    do
    {
        if (!v4)
            break;
    } while (*(v5));
    sub_403b00();
    return;
}
```

## `sub_00403c6b` `0x00403c6b`

_1 bytes. (leaf/helper — see body)_

```c
void sub_403c6b(void)
{
    return;
}
```

## `sub_00403c6c` `0x00403c6c`

_16 bytes. (leaf/helper — see body)_

```c
void sub_403c6c(unsigned int a0, unsigned int a1)
{
}
```

## `sub_00403c80` `0x00403c80`

_8 bytes. (leaf/helper — see body)_

```c
int sub_403c80(void)
{
    return;
}
```

## `sub_00403c88` `0x00403c88`

_68 bytes. (leaf/helper — see body)_

```c
int sub_403c88(void)
{
    unsigned int v1;  // edx
    unsigned int v2;  // eax
    int v3;  // edi
    int v4;  // esi
    int v5;  // ebx
    int v6;  // edi
    int v7;  // esi
    int v8;  // ebx

    if (!v1)
    {
        return;
    }
    else if (!*((int *)v2))
    {
        sub_403a64();
        return;
    }
    else if (v1 != *((int *)v2))
    {
        sub_403f60(v3, v4, v5);
        sub_402628();
        return;
    }
    else
    {
        sub_403f60(v6, v7, v8);
        sub_402628();
        return;
    }
}
```

