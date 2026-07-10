# elfbot.dll decompiled — loader 0x004024dd..0x00402dee

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_004024dd` `0x004024dd`

_20 bytes. (leaf/helper — see body)_

```c
typedef struct LIST_ENTRY {
    void* Flink;
    void* Blink;
} LIST_ENTRY;

typedef struct CRITICAL_SECTION_DEBUG {
    unsigned short Type;
    unsigned short CreatorBackTraceIndex;
    void* CriticalSection;
    LIST_ENTRY ProcessLocksList;
    unsigned int EntryCount;
    unsigned int ContentionCount;
    unsigned int Flags;
    unsigned short CreatorBackTraceIndexHigh;
    unsigned short Identifier;
} CRITICAL_SECTION_DEBUG;

typedef struct CRITICAL_SECTION {
    struct CRITICAL_SECTION_DEBUG *DebugInfo;
    int LockCount;
    int RecursionCount;
    HANDLE OwningThread;
    HANDLE LockSemaphore;
    UIntPtr SpinCount;
} CRITICAL_SECTION;

extern char g_420045;
extern CRITICAL_SECTION g_4205c0;

void sub_4024dd(void)
{
    if (g_420045)
        LeaveCriticalSection(&g_4205c0.DebugInfo);
    return;
}
```

## `sub_004024f1` `0x004024f1`

_5 bytes. (leaf/helper — see body)_

```c
void sub_4024f1(unsigned int a0, unsigned int a1)
{
    sub_403374();
    return;
}
```

## `sub_004024f6` `0x004024f6`

_2 bytes. (leaf/helper — see body)_

```c
void sub_4024f6(void)
{
    sub_4024dd();
    return;
}
```

## `sub_00402501` `0x00402501`

_3 bytes. (leaf/helper — see body)_

```c
int sub_402501(void)
{
    sub_402504();
    return;
}
```

## `sub_00402504` `0x00402504`

_32 bytes. (leaf/helper — see body)_

```c
int sub_402504(void)
{
    int v2;  // eax
    int v0;  // [bp-0x4]

    if (v2 <= 0)
    {
        return;
    }
    else if (!sub_401f3c(v0))
    {
        sub_4025ec();
        return;
    }
    else
    {
        return;
    }
}
```

## `sub_00402524` `0x00402524`

_32 bytes. (leaf/helper — see body)_

```c
int sub_402524(void)
{
    unsigned int v2;  // eax
    int v0;  // [bp-0x4]

    if (!v2)
    {
        return;
    }
    else if (sub_4020cc(v0))
    {
        sub_4025ec();
        return;
    }
    else
    {
        return;
    }
}
```

## `sub_00402544` `0x00402544`

_77 bytes. (leaf/helper — see body)_

```c
int sub_402544(void)
{
    int *v1;  // eax
    unsigned int v2;  // edx
    int v3;  // eax
    unsigned int v4;  // edx
    int v5;  // eax

    if (*(v1))
    {
        if (v2)
        {
            v3 = sub_402440(v1);
            if (!v3)
            {
                sub_4025ec();
                return;
            }
            *(v1) = v3;
            return;
        }
        else
        {
            *(v1) = 0;
            if (!sub_4020cc())
                return;
            sub_4025ec();
            return;
        }
    }
    else
    {
        if (v4)
        {
            v5 = sub_401f3c(v1);
            if (v5)
            {
                *(v1) = v5;
                return;
            }
            sub_4025ec();
            return;
        }
        else
        {
            return;
        }
    }
}
```

## `sub_00402591` `0x00402591`

_3 bytes. (leaf/helper — see body)_

```c
int sub_402591(unsigned int a0, unsigned int a1)
{
    return sub_402594();
}
```

## `sub_00402594` `0x00402594`

_12 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_41e004;

void sub_402594(unsigned int a0, unsigned int a1)
{
    g_41e004 = a1;
    sub_4039f8();
    return;
}
```

## `sub_004025ea` `0x004025ea`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4025ea(void)
{
    sub_4025ec();
    return;
}
```

## `sub_004025ec` `0x004025ec`

_85 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_420008;

int sub_4025ec(void)
{
    char v2;  // al
    char v3;  // bl
    unsigned int v4;  // esi
    unsigned int v5;  // ebx
    unsigned int v6;  // ecx
    unsigned int v7;  // ecx
    unsigned int v0;  // [bp+0x0]

    v3 = v2 & 127;
    if (g_420008)
        g_420008(v4, v5);
    if (v3)
    {
        sub_402594(v7, v0);
        return;
    }
    sub_404fdc();
    sub_402594(v6, v0);
    return;
}
```

## `sub_004025f7` `0x004025f7`

_1 bytes. (leaf/helper — see body)_

```c
void sub_4025f7(void)
{
    return;
}
```

## `sub_004025f8` `0x004025f8`

_16 bytes. (leaf/helper — see body)_

```c
int sub_4025f8(void)
{
    unsigned int v2;  // eax
    int v0;  // [bp-0x4]

    *((unsigned int *)(sub_404fdc(v0) + 4)) = v2;
    return;
}
```

## `sub_00402608` `0x00402608`

_29 bytes. (leaf/helper — see body)_

```c
unsigned int sub_402608(void)
{
    unsigned int v2;  // ebx
    int v0;  // [bp-0x4]

    v2 = *((int *)(sub_404fdc(v0) + 4));
    *((unsigned int *)(sub_404fdc(v0) + 4)) = 0;
    return v2;
}
```

## `sub_00402625` `0x00402625`

_3 bytes. (leaf/helper — see body)_

```c
int sub_402625(void)
{
    sub_402628();
    return;
}
```

## `sub_00402628` `0x00402628`

_64 bytes. (leaf/helper — see body)_

```c
int sub_402628(void)
{
    void* v1;  // eax
    void* iter;  // esi
    void* node;  // edi
    int v12;  // ecx
    unsigned int v13;  // 4131
    unsigned int v14;  // ecx
    void* k;  // esi
    void* iter1;  // edi
    void* v3;  // edx
    void* iter2;  // edi
    int v5;  // ecx
    int v6;  // ecx
    unsigned int v7;  // 4119
    unsigned int v8;  // ecx
    int v9;  // ecx
    void* j;  // esi

    iter = v1;
    iter2 = v3;
    if (iter2 > iter)
    {
        j = v9 + iter - 4;
        node = v9 + iter2 - 4;
        v12 = v9 >> 2;
        if ((char)v13)
            return;
        for (v13 = _ccall(8, 27, v9 >> 2, v9 >> 1, 0); v12; j += 0xfffffffc)
        {
            v12 -= 1;
            *((int *)node) = *((int *)j);
            node += 0xfffffffc;
        }
        v14 = v5 & 3;
        k = j + 3;
        for (iter1 = node + 3; v14; k += 4294967295)
        {
            v14 -= 1;
            *((char *)iter1) = *((char *)k);
            iter1 += 4294967295;
        }
        return;
    }
    else if (iter2 != iter)
    {
        v6 = v5 >> 2;
        if ((char)v7)
            return;
        for (v7 = _ccall(8, 27, v5 >> 2, v5 >> 1, 0); v6; iter += 4)
        {
            v6 -= 1;
            *((int *)iter2) = *((int *)iter);
            iter2 += 4;
        }
        for (v8 = v5 & 3; v8; iter += 1)
        {
            v8 -= 1;
            *((char *)iter2) = *((char *)iter);
            iter2 += 1;
        }
        return;
    }
    else
    {
        return;
    }
}
```

## `sub_00402668` `0x00402668`

_234 bytes. (leaf/helper — see body)_

```c
int sub_402668(void)
{
    unsigned int node;  // esi
    char l[2];  // eax
    char k[2];  // eax
    char iter[2];  // ebx
    char v2[2];  // ebx
    char v3[2];  // ebx
    char j[2];  // eax
    unsigned int *v7;  // edx
    unsigned int v8;  // edi

    while (true)
    {
        for (; iter[0] && iter[0] <= 32; iter = CharNextA(iter));
        if (iter[0] != 0x22 || iter[1] != 0x22)
            break;
        iter += 1;
    }
    v2 = iter;
    while (true)
    {
        v3 = v2;
        if (v3[0] <= 32)
        {
            sub_403f60();
            v8 = *(v7);
            for (node = 0; iter[0] > 32; iter = CharNextA(iter))
            {
                if (iter[0] == 0x22)
                {
                    iter = CharNextA(iter);
                    while (iter[0] && iter[0] != 0x22)
                    {
                        l = CharNextA(iter);
                        if (l <= iter)
                            continue;
                        do
                        {
                            *((char *)(v8 + node)) = iter[0];
                            iter = &iter[1];
                            node += 1;
                        } while (l > iter);
                    }
                }
                else
                {
                    k = CharNextA(iter);
                    if (k > iter)
                    {
                        do
                        {
                            *((char *)(v8 + node)) = iter[0];
                            iter = &iter[1];
                            node += 1;
                        } while (k > iter);
                    }
                }
            }
            return;
        }
        else if (v3[0] == 0x22)
        {
            for (j = CharNextA(v3); j[0] && j[0] != 0x22; j = CharNextA(j));
            v2 = j;
            if (v2[0])
                v2 = CharNextA(j);
        }
        else
        {
            v2 = CharNextA(v3);
        }
    }
}
```

## `sub_00402752` `0x00402752`

_2 bytes. (leaf/helper — see body)_

```c
int sub_402752(void)
{
    sub_402754();
    return;
}
```

## `sub_00402754` `0x00402754`

_94 bytes. (leaf/helper — see body)_

```c
int sub_402754(void)
{
    unsigned int v4;  // eax
    unsigned int v5;  // esi
    unsigned int *v6;  // edx
    Byte v0[4];  // [bp-0x114]
    int v1;  // [bp-0x110]
    int v2;  // [bp-0x10c]

    v5 = v4;
    sub_403a10();
    if (!v5)
    {
        GetModuleFileNameA(NULL, v0, 261);
        sub_403b00(v0, v1, v2);
        return;
    }
    GetCommandLineA();
    while (true)
    {
        sub_402668();
        if (!v5)
        {
            return;
        }
        else if (*(v6))
        {
            v5 -= 1;
        }
        else
        {
            return;
        }
    }
}
```

## `sub_004027b2` `0x004027b2`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4027b2(void)
{
    sub_4027b4();
    return;
}
```

## `sub_004027b4` `0x004027b4`

_69 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned short field_4;
} struct_0;

extern struct_0 g_420214;
extern struct_0 g_4203e0;

int sub_4027b4(void)
{
    struct_0 *v1;  // eax
    unsigned int *v2;  // edx
    unsigned int v3;  // eax

    if (v1->field_4 == 55217)
    {
        v3 = 0;
    }
    else if (v1->field_4 - -10318 < 2)
    {
        v3 = v2();
    }
    else if (v1 == &g_420214.padding_0[0] || v1 == &g_4203e0.padding_0[0])
    {
        v3 = 0;
    }
    else
    {
        v3 = 103;
    }
    if (v3)
        sub_4025f8();
    return;
}
```

## `sub_004027f9` `0x004027f9`

_3 bytes. (leaf/helper — see body)_

```c
int sub_4027f9(void)
{
    sub_4027fc();
    return;
}
```

## `sub_004027fc` `0x004027fc`

_9 bytes. (leaf/helper — see body)_

```c
int sub_4027fc(void)
{
    sub_4027b4();
    return;
}
```

## `sub_00402805` `0x00402805`

_3 bytes. (leaf/helper — see body)_

```c
int sub_402805(void)
{
    sub_402808();
    return;
}
```

## `sub_00402808` `0x00402808`

_86 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned short field_4;
    char padding_6[22];
    struct struct_1 *field_1c;
    char padding_20[4];
    struct struct_1 *field_24;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_0 g_420048;

int sub_402808(void)
{
    unsigned int v1;  // esi
    struct_0 *v2;  // eax
    unsigned short v3;  // ax

    v1 = 0;
    v3 = v2->field_4;
    if (v3 >= 55217 && v3 <= 55219)
    {
        if ((v3 & 55218) == 55218)
            v1 = v2->field_1c();
        if (!v1)
            v1 = v2->field_24();
        if (!v1)
            return;
        sub_4025f8();
        return;
    }
    if (v2 != &g_420048.padding_0[0])
        sub_4025f8();
    return;
}
```

## `sub_0040285e` `0x0040285e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40285e(void)
{
    return sub_402860();
}
```

## `sub_00402860` `0x00402860`

_111 bytes. (leaf/helper — see body)_

```c
int sub_402860(void)
{
    unsigned int v1;  // ecx
    unsigned int v2;  // esi
    void* iter;  // eax
    unsigned int node;  // edx
    unsigned int v5;  // ecx
    unsigned int v6;  // ebx
    unsigned int v7;  // esi
    unsigned int v8;  // esi

    v2 = v1 >> 2;
    if ((v1 & 0xfffffffc))
    {
        do
        {
            v5 = *((int *)iter);
            v6 = *((int *)node);
            if (*((int *)iter) != *((int *)node))
            {
LABEL_4028b7:
                return;
            }
            v7 = v2 - 1;
            if (v2 == 1)
            {
                iter += 4;
                node += 4;
                break;
            }
            v5 = (int)iter[4];
            v6 = *((int *)(node + 4));
            if ((int)iter[4] != *((int *)(node + 4)))
                goto LABEL_4028b7;
        } while ((iter += 8, node += 8, v2 = v7 - 1, v7 != 1));
    }
    v8 = v1 & 3;
    if (!((char)v1 & 3))
    {
        return;
    }
    else if (*((char *)iter) != *((char *)node))
    {
        return;
    }
    else if (v8 == 1)
    {
        return;
    }
    else if ((char)iter[1] != *((char *)(node + 1)))
    {
        return;
    }
    else if (v8 != 2)
    {
        return;
    }
    else
    {
        return;
    }
}
```

## `sub_004028cf` `0x004028cf`

_1 bytes. (leaf/helper — see body)_

```c
int sub_4028cf(void)
{
    sub_4028d0();
    return;
}
```

## `sub_004028d0` `0x004028d0`

_31 bytes. (leaf/helper — see body)_

```c
int sub_4028d0(void)
{
    char v1;  // cl
    unsigned int v2;  // eax
    int v3;  // edx
    int v4;  // ecx
    unsigned int v5;  // 4146
    void* iter;  // edi
    unsigned int v7;  // ecx

    v2 = _INSERT((_INSERT(v1, 1, v1) & 0xffff) * 0x10000, 0, _INSERT(v1, 1, v1));
    v4 = v3 >> 2;
    if ((char)v5)
        return;
    for (v5 = _ccall(8, 27, v3 >> 2, v3 >> 1, 0); v4; iter += 4)
    {
        v4 -= 1;
        *((unsigned int *)iter) = v2;
    }
    for (v7 = v3 & 3; v7; iter += 1)
    {
        v7 -= 1;
        *((char *)iter) = v2;
    }
    return;
}
```

## `sub_004028ef` `0x004028ef`

_1 bytes. (leaf/helper — see body)_

```c
int sub_4028ef(void)
{
    sub_4028f0();
    return;
}
```

## `sub_004028f0` `0x004028f0`

_203 bytes. (leaf/helper — see body)_

```c
int sub_4028f0(void)
{
    char v1[2];  // eax
    char v2[2];  // esi
    unsigned int v9;  // ebx
    char v10[2];  // esi
    int v11;  // eax
    unsigned int v12;  // ebx
    unsigned int v13;  // 4102
    unsigned int v14;  // 4109
    unsigned int v15;  // 4101
    unsigned int v16;  // esi
    unsigned int *v17;  // edx
    char v3;  // bl
    char iter[2];  // esi
    char v5;  // ch
    char v6[2];  // esi
    unsigned int v7;  // cc_dep1
    char v8;  // bl

    v2 = v1;
    if (v1)
    {
        v11 = 0;
        do
        {
            v3 = v2[0];
            v2 = &v2[1];
        } while (v2[0] == 32);
        v5 = 0;
        if (v3 != 45)
        {
            if (v3 == 43)
                goto LABEL_402976;
            v6 = iter;
            if (v3 != 36 && (v6 = iter, v3 != 120 && (v6 = iter, v3 != 88)))
            {
                if (v3 != 48)
                    goto LABEL_40293e;
                v3 = iter[0];
                iter = &iter[1];
                v6 = iter;
                if (iter[0] != 120 && (v6 = iter, v3 != 88))
                {
                    v7 = v3;
                    if (!v3)
                        goto LABEL_40295c;
                    goto LABEL_402942;
                }
            }
            v8 = v6[0];
            v2 = &v6[1];
            if (!v6[0])
                goto LABEL_402966;
            do
            {
                iter = v2;
                if (v8 >= 97)
                    v8 -= 32;
                v9 = _INSERT(v8 CONCAT 0, 0, v8 - 48);
                if (v8 - 48 > 9)
                {
                    if ((char)v9 - 0x11 > 5)
                        goto LABEL_40296f;
                    v9 = _INSERT((char)v9 - 0x11 CONCAT 0, 0, (char)v9 - 7);
                }
                if (v11 > 0xfffffff)
                    goto LABEL_40296f;
            } while ((v11 = (int)(v11 * 16 + v9), v8 = iter[0], v10 = iter + 1, v2 = iter + 1, iter[0]));
        }
        v5 = 1;
LABEL_402976:
        v3 = iter[0];
        iter = &iter[1];
LABEL_40293e:
        if (!v3)
            goto LABEL_40296f;
        do
        {
LABEL_402942:
            v12 = _INSERT(v3 CONCAT 0, 0, v3 - 48);
            if (v3 - 48 > 9 || v11 > 214748364)
                goto LABEL_40296f;
        } while ((v11 = (int)(v11 * 10 + v12), v3 = iter[0], iter += 1, v7 = (unsigned int)v3, v3));
LABEL_40295c:
        v13 = _ccall(13, v7, 0, 0);
        v14 = _ccall(4, 19, (unsigned int)(v5 - 1), 0, v13);
        if (!((char)v14))
        {
            if (v11 >= 0)
                goto LABEL_4029b2;
            goto LABEL_40296f;
        }
        else
        {
            if (0 > v11 && !((v15 = (unsigned int)_ccall(8, 6, 0, v11, 0), (char)v15)))
                goto LABEL_40296f;
LABEL_4029b2:
            v16 = 0;
        }
    }
    else
    {
LABEL_402966:
        iter = &v2[1];
LABEL_40296f:
        v16 = iter - v1;
    }
    *(v17) = v16;
    return;
}
```

## `sub_004029bb` `0x004029bb`

_1 bytes. (leaf/helper — see body)_

```c
int sub_4029bb(void)
{
    sub_4029bc();
    return;
}
```

## `sub_004029bc` `0x004029bc`

_17 bytes. (leaf/helper — see body)_

```c
int sub_4029bc(void)
{
    char v1;  // cl
    unsigned int v2;  // ecx
    char *v3;  // esi
    unsigned int v4;  // edi

    v2 = v1;
    do
    {
        if (!v2)
            break;
    } while (*(v3) == *((char *)v4));
    return;
}
```

## `sub_004029cd` `0x004029cd`

_3 bytes. (leaf/helper — see body)_

```c
int sub_4029cd(void)
{
    return sub_4029d0();
}
```

## `sub_004029d0` `0x004029d0`

_5 bytes. (leaf/helper — see body)_

```c
int sub_4029d0(void)
{
    sub_4029d8();
    return;
}
```

## `sub_004029d5` `0x004029d5`

_1 bytes. (leaf/helper — see body)_

```c
void sub_4029d5(void)
{
    return;
}
```

## `sub_004029d6` `0x004029d6`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4029d6(void)
{
    sub_4029d8();
    return;
}
```

## `sub_004029d8` `0x004029d8`

_165 bytes. (leaf/helper — see body)_

```c
int sub_4029d8(void)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v3;  // eax
    unsigned int v4;  // eax

    if (v1 < 0)
    {
        v3 = -(v1);
        if (v3 >= 0x1400)
        {
            /* unsupported instruction */
            /* unsupported instruction */
            return;
        }
        if (/* unsupported instruction */)
        {
            /* unsupported instruction */
            /* unsupported instruction */
        }
        else
        {
            /* unsupported instruction */
            /* unsupported instruction */
        }
        /* unsupported instruction */
        /* unsupported instruction */
        /* unsupported instruction */
        v4 = v3 >> 5;
        if (!(v3 & 0xffffffe0))
            return;
        if (((char)v4 & 15))
        {
            if (/* unsupported instruction */)
            {
                /* unsupported instruction */
                /* unsupported instruction */
            }
            else
            {
                /* unsupported instruction */
                /* unsupported instruction */
            }
            /* unsupported instruction */
            /* unsupported instruction */
            /* unsupported instruction */
        }
        if (!(v4 & 0xfffffff0))
            return;
        if (/* unsupported instruction */)
        {
            /* unsupported instruction */
            /* unsupported instruction */
        }
        else
        {
            /* unsupported instruction */
            /* unsupported instruction */
        }
        /* unsupported instruction */
        /* unsupported instruction */
        /* unsupported instruction */
        return;
    }
    else if (!v1)
    {
        return;
    }
    else if (v1 < 0x1400)
    {
        if (/* unsupported instruction */)
        {
            /* unsupported instruction */
            /* unsupported instruction */
        }
        else
        {
            /* unsupported instruction */
            /* unsupported instruction */
        }
        /* unsupported instruction */
        /* unsupported instruction */
        /* unsupported instruction */
        v2 = v1 >> 5;
        if (!(v1 & 0xffffffe0))
            return;
        if (((char)v2 & 15))
        {
            if (/* unsupported instruction */)
            {
                /* unsupported instruction */
                /* unsupported instruction */
            }
            else
            {
                /* unsupported instruction */
                /* unsupported instruction */
            }
            /* unsupported instruction */
            /* unsupported instruction */
            /* unsupported instruction */
        }
        if (!(v2 & 0xfffffff0))
            return;
        if (/* unsupported instruction */)
        {
            /* unsupported instruction */
            /* unsupported instruction */
        }
        else
        {
            /* unsupported instruction */
            /* unsupported instruction */
        }
        /* unsupported instruction */
        /* unsupported instruction */
        /* unsupported instruction */
        return;
    }
    else
    {
        if (/* unsupported instruction */)
        {
            /* unsupported instruction */
            /* unsupported instruction */
        }
        else
        {
            /* unsupported instruction */
            /* unsupported instruction */
        }
        return;
    }
}
```

## `sub_00402a84` `0x00402a84`

_41 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[64];
    char field_40;
} struct_0;

int sub_402a84(void)
{
    char idx[16387];  // eax
    char v2;  // cl
    struct_0 *v4;  // eax

    idx[0] = idx[0] + *((char *)&idx);
    idx[0] = idx[0] + *((char *)&idx);
    idx[0] = idx[0] + *((char *)&idx);
    idx[0x3fff] = idx[0x3fff] + *((char *)&idx);
    idx[0] = idx[0] + *((char *)&idx);
    idx[0] = idx[0] + *((char *)&idx);
    idx[16386] = idx[16386] + *((char *)((void*)&idx + 1));
    idx[0] = idx[0] + *((char *)&idx);
    idx[0] = idx[0] + *((char *)&idx);
    v4 = _INSERT(idx, 0, *((char *)&idx) + v2) + 64;
    v4->padding_0[0] = v4->padding_0[0] + *((char *)&v4);
    v4->padding_0[0] = v4->padding_0[0] + *((char *)&v4);
    __unsupported_jumpkind_Ijk_Privileged()
}
```

## `sub_00402aad` `0x00402aad`

_20 bytes. (leaf/helper — see body)_

```c
int sub_402aad(void)
{
    void* v1;  // eax
    char *v2;  // eax

    *((char *)v1) = *((char *)v1) | *((char *)&v1);
    *((char *)v1) = *((char *)v1) + *((char *)&v1);
    *((char *)v1) = *((char *)v1) + *((char *)&v1);
    *((char *)&v1[100]) = (char)v1[100] + *((char *)&v1);
    v2 = _INSERT(v1, 0, *((char *)&v1) | 64);
    *(v2) = *(v2) + (*((char *)&v1) | 64);
    *(v2) = *(v2) + (*((char *)&v1) | 64);
    *(v2) = *(v2) + (*((char *)&v1) | 64);
    return;
}
```

## `sub_00402b54` `0x00402b54`

_2 bytes. (leaf/helper — see body)_

```c
void sub_402b54(void)
{
}
```

## `sub_00402bfe` `0x00402bfe`

_57 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[1122470482];
    struct struct_1 *field_42e78a52;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_402bfe(void)
{
    unsigned int v1;  // edx
    void* v2;  // eax
    unsigned int v11;  // eax
    unsigned int v12;  // ebx
    unsigned int v13;  // 4116
    unsigned int v14;  // ecx
    unsigned int v15;  // 4101
    char v3;  // al
    unsigned int v4;  // cc_op
    unsigned int v5;  // cc_dep1
    unsigned int v6;  // cc_dep2
    unsigned int v7;  // cc_ndep
    unsigned int v8;  // 4113
    struct_0 *v9;  // esi

    v3 = (v1 CONCAT v2) / (int)v2[32];
    v8 = _ccall(12, v4, v5, v6, v7);
    if (!((char)v8))
    {
        (*((int *)&(v9->padding_0)[1]))();
        __unsupported_jumpkind_Ijk_Privileged()
    }
    v11 = _INSERT(_INSERT(v3, 1, v3 / 243), 0, v3 % 243);
    v13 = _ccall(4, 39, v11, v12, 0);
    if (!(v14 != 1 & (char)v13))
    {
        v15 = _ccall(10, 39, v11, v12, 0);
        if (!((char)v15))
            return;
        x86g_dirtyhelper_OUT(0x7f<32>, Conv(8I->32I, Extract(Conv(64I->32I, (vvar_22{r8|4b} Mull (signed) vvar_3{r20|4b})), 8bits@0x0<64>)), 0x1<32>)
    }
}
```

## `sub_00402c12` `0x00402c12`

_2 bytes. (leaf/helper — see body)_

```c
void sub_402c12(void)
{
}
```

## `sub_00402c3d` `0x00402c3d`

_1 bytes. (leaf/helper — see body)_

```c
void sub_402c3d(void)
{
    __unsupported_jumpkind_Ijk_Privileged()
}
```

## `sub_00402c3e` `0x00402c3e`

_7 bytes. (leaf/helper — see body)_

```c
char sub_402c3e(void)
{
    unsigned int v2;  // cc_op
    unsigned int v3;  // cc_dep1
    unsigned int v4;  // cc_dep2
    unsigned int v5;  // cc_ndep
    unsigned int v6;  // 4117
    unsigned int v7;  // 4126
    unsigned int v8;  // id
    unsigned int v9;  // ac
    unsigned int v10;  // 4146
    unsigned int v0;  // [bp+0x1]
    unsigned int v1;  // [bp+0x4]

    v6 = _ccall(v2, v3, v4, v5);
    v7 = _ccall(18, &v1, 0, v6);
    v0 = v7 | 0x202 | v8 * 0x200000 & 0x200000 | v9 * 0x40000 & 0x40000;
    v10 = _ccall(18, &v1, 0, v6);
    v0 = v10 | 0x202 | v8 * 0x200000 & 0x200000 | v9 * 0x40000 & 0x40000;
}
```

## `sub_00402cb2` `0x00402cb2`

_6 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_c37bcaae;

void sub_402cb2(void)
{
    unsigned int v1;  // cc_op
    unsigned int v2;  // cc_dep1
    unsigned int v3;  // cc_dep2
    unsigned int v4;  // cc_ndep
    unsigned int v5;  // 4107
    unsigned int v6;  // esi

    v5 = _ccall(v1, v2, v3, v4);
    g_c37bcaae = g_c37bcaae + v6 + (v5 & 1);
    sub_402cb8();
    return;
}
```

## `sub_00402cb8` `0x00402cb8`

_6 bytes. (leaf/helper — see body)_

```c
int sub_402cb8(unsigned int a0)
{
    int v0;  // [bp+0x0]

    return GetKeyboardType(v0);
}
```

## `sub_00402cbe` `0x00402cbe`

_2 bytes. (leaf/helper — see body)_

```c
int sub_402cbe(void)
{
    return sub_402cc0();
}
```

## `sub_00402cc0` `0x00402cc0`

_47 bytes. (leaf/helper — see body)_

```c
unsigned int sub_402cc0(void)
{
    unsigned int v1;  // eax

    if (sub_402cb8(0) != 7)
        return 0;
    v1 = sub_402cb8(1) & 0xff00;
    if (v1 == 0xd00 || v1 == 0x400)
        return 1;
    return 0;
    return 1;
}
```

## `sub_00402cef` `0x00402cef`

_1 bytes. (leaf/helper — see body)_

```c
void sub_402cef(void)
{
    sub_402cf0();
    return;
}
```

## `sub_00402cf0` `0x00402cf0`

_134 bytes. refs "SOFTWARE\\Borland\\Delphi\\RTL", "FPUMaskValue"_

```c
extern unsigned int g_402d68;
extern unsigned short g_41e00c;

int sub_402cf0(void)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4139
    unsigned int v13;  // 4103
    unsigned long v14;  // 4148
    unsigned long v15;  // 4118
    unsigned short v16;  // ax
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    char *v2;  // [bp-0x14], Other Possible Types: unsigned int
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char v5;  // [bp-0x8], Other Possible Types: unsigned int
    char v6;  // [bp-0x4]
    char v7;  // [bp+0x0]
    int v8;  // [bp+0x4]

    v4 = g_41e00c;
    if (sub_401130(0x80000002, "SOFTWARE\\Borland\\Delphi\\RTL", 0, 0x1, &v5))
    {
        v16 = g_41e00c & 65472;
        g_41e00c = v16 | g_41e00c & 63;
        return v16 | g_41e00c & 63;
    }
    v2 = &v6;
    v1 = sub_402d61;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v13 = *((int *)v12);
    v0 = *((int *)v12);
    v14 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v14) = &v0;
    v3 = 4;
    sub_401138(v5, "FPUMaskValue", NULL, NULL, &v4, &v3);
    v15 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v15) = v13;
    v2 = &g_402d68;
    return sub_402d57(4, g_41e00c, v5, &v7, v7, v8);
}
```

## `sub_00402d57` `0x00402d57`

_10 bytes. (leaf/helper — see body)_

```c
enum WIN32_ERROR sub_402d57(void)
{
    unsigned int v1;  // [bp+0x100000]

    return sub_401128(v1);
}
```

## `sub_00402d61` `0x00402d61`

_5 bytes. (leaf/helper — see body)_

```c
void sub_402d61(unsigned int a0, unsigned int a1)
{
    sub_403374();
    return;
}
```

## `sub_00402d66` `0x00402d66`

_2 bytes. (leaf/helper — see body)_

```c
enum WIN32_ERROR sub_402d66(void)
{
    return sub_402d57();
}
```

## `sub_00402db4` `0x00402db4`

_10 bytes. (leaf/helper — see body)_

```c
void sub_402db4(void)
{
    x86g_dirtyhelper_FINIT(unsupported_<class 'pyvex.expr.GSPTR'>())
    return;
}
```

## `sub_00402dbe` `0x00402dbe`

_2 bytes. (leaf/helper — see body)_

```c
int sub_402dbe(void)
{
    sub_402dc0();
    return;
}
```

## `sub_00402dc0` `0x00402dc0`

_17 bytes. (leaf/helper — see body)_

```c
int sub_402dc0(void)
{
    void* v1;  // eax
    char *i;  // esi
    unsigned int v3;  // ecx
    char *iter;  // edi

    i = (int)v1[44];
    for (v3 = *((char *)(int)v1[44]) + 1; v3; i += 1)
    {
        v3 -= 1;
        *(iter) = *(i);
        iter += 1;
    }
    return;
}
```

## `sub_00402dd1` `0x00402dd1`

_3 bytes. (leaf/helper — see body)_

```c
void sub_402dd1(void)
{
    sub_402dd4();
    return;
}
```

## `sub_00402dd4` `0x00402dd4`

_26 bytes. (leaf/helper — see body)_

```c
int sub_402dd4(void)
{
    int v0;  // [bp-0x4]

    sub_402e04(v0);
    sub_402504(v0);
    sub_402e28();
    return;
}
```

## `sub_00402dee` `0x00402dee`

_2 bytes. (leaf/helper — see body)_

```c
void sub_402dee(void)
{
    sub_402df0();
    return;
}
```

