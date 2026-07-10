# elfbot.dll decompiled — jdrv 0x1002ad79..0x1002ccf6

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1002ad79` `0x1002ad79`

_51 bytes. (leaf/helper — see body)_

```c
extern int g_10291cf6;
extern int g_10291ef6;
extern int g_102920f6;

int sub_1002ad79(int a0, int a1, int a2)
{
    char v0;  // [bp+0x0]

    lstrcpy(&g_10291cf6, a1);
    lstrcpy(&g_10291ef6, a2);
    lstrcpy(&g_102920f6, a0);
    return sub_10039bbb(&v0, v0);
}
```

## `sub_1002adac` `0x1002adac`

_42 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_100428c9;

void sub_1002adac(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4)
{
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v1 = a4;
    v0 = a3;
    g_100428c9(a0, a1, a2);
    return;
}
```

## `sub_1002adc0` `0x1002adc0`

_17 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_10291cf6;
extern unsigned int g_10291ef6;
extern unsigned int g_102920f6;

void sub_1002adc0(void)
{
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]
    unsigned int v2;  // [bp-0x4]

    v2 = &g_10291ef6;
    v1 = &g_10291cf6;
    v0 = &g_102920f6;
}
```

## `sub_1002ade7` `0x1002ade7`

_136 bytes. (leaf/helper — see body)_

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

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

typedef struct CRITICAL_SECTION {
    struct CRITICAL_SECTION_DEBUG *DebugInfo;
    int LockCount;
    int RecursionCount;
    HANDLE OwningThread;
    HANDLE LockSemaphore;
    UIntPtr SpinCount;
} CRITICAL_SECTION;

typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    char field_8;
} struct_0;

extern struct_1 *g_10042668;
extern struct_0 *g_1004266c;
extern unsigned int g_10042670;
extern unsigned int g_10042674;
extern char g_1004287c;
extern CRITICAL_SECTION g_1004287d;
extern char g_100f0d36;

int sub_1002ade7(unsigned short *a0)
{
    char v0;  // [bp+0x0]

    if (g_100f0d36)
    {
        return 6597056;
    }
    else if (*((int *)0x64a9c0) == 31)
    {
        EnterCriticalSection(&g_1004287d.DebugInfo);
        sub_10024feb(&v0);
        g_10042674 = *(a0) + 8;
        g_10042670 = 0x800;
        g_1004266c->field_0 = 0;
        g_1004266c->field_4 = 0;
        sub_1002ae6f(&g_1004266c->field_8, a0 + 1, g_10042674 - 8);
        g_1004287c = 1;
        g_10042668(1);
        g_1004287c = 0;
        return (unsigned int)LeaveCriticalSection(&g_1004287d.DebugInfo);
    }
    else
    {
        return 6597056;
    }
}
```

## `sub_1002ae6f` `0x1002ae6f`

_18 bytes. (leaf/helper — see body)_

```c
void sub_1002ae6f(char *iter, char *i, unsigned int a2)
{
    for (; a2; i += 1)
    {
        a2 -= 1;
        *(iter) = *(i);
        iter += 1;
    }
    return;
}
```

## `sub_1002ae81` `0x1002ae81`

_17 bytes. (leaf/helper — see body)_

```c
char sub_1002ae81(char *iter, unsigned int a1)
{
    for (; a1; iter += 1)
    {
        a1 -= 1;
        *(iter) = 0;
    }
    return 0;
}
```

## `sub_1002ae92` `0x1002ae92`

_176 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    char padding_4[44];
    unsigned int field_30;
    char padding_34[8];
    unsigned int field_3c;
    struct struct_0 *field_40;
} struct_0;

unsigned int sub_1002ae92(unsigned int a0, unsigned int node, struct_0 *a2)
{
    struct_0 *v1;  // ebx
    struct_0 *v2;  // ebx
    unsigned int v3;  // ecx
    struct_0 *iter;  // esi
    struct_0 *v5;  // ebx
    struct_0 *v6;  // ebx
    unsigned int v0;  // [bp-0x1f8]

    v0 = 0;
    if (node >= 16)
    {
        node -= 16;
        v0 = 1;
    }
    for (v1 = node * 492 + 6606096; node < 16; node += 1)
    {
        v2 = v1;
        if (v2->field_0)
        {
            if (!a0 && *((int *)&v1->padding_34[4]) < v1->field_30)
                return node + 64;
            v3 = 0;
            iter = &v1->field_3c;
            v5 = v1;
            while (true)
            {
                v6 = v5;
                v2 = v6;
                if (v3 >= *((int *)&v1->padding_34[4]))
                    break;
                if (iter->field_0 == a0)
                {
                    v6 = *((int *)&iter->padding_4[0]);
                    if (!a2 || *((int *)&iter->padding_4[0]) == a2)
                        return node + 64;
                }
                iter = &iter->padding_4[8];
                v3 += 1;
                v5 = v6;
            }
        }
        if (v0)
            return 0;
        v1 = &v2[7].padding_4[12];
    }
    return 0;
}
```

## `sub_1002af42` `0x1002af42`

_39 bytes. calls GetAsyncKeyState_

```c
extern unsigned int g_1005f120;

short sub_1002af42(void)
{
    int i;  // ecx
    unsigned short v3;  // ax
    int idx;  // [bp-0x4]

    for (i = 0; i < 0x100; i = idx + 1)
    {
        idx = i;
        GetAsyncKeyState(i);
        idx = idx;
        (&g_1005f120)[idx] = GetAsyncKeyState(idx);
    }
    return v3;
}
```

## `sub_1002af69` `0x1002af69`

_194 bytes. calls GetAsyncKeyState, SendDlgItemMessageA; refs "lmouse"_

```c
extern int g_100445f0;
extern unsigned int g_1005f120[4];
extern int g_1005f524;
extern HWND g_10072f84;
extern char g_100faa3c;

int sub_1002af69(void)
{
    unsigned int count;  // eax
    int i;  // ecx
    int idx;  // ecx
    LPARAM v7;  // esi
    LPARAM v8;  // edi
    unsigned int v9;  // eax
    int v0;  // [bp-0x4c]
    char v1;  // [bp-0x40]
    char v2;  // [bp-0x3f]

    if (!g_1005f524)
        return v9;
    count = IsWindow(g_10072f84);
    if (!count)
        return count;
    i = 0;
    while (i < 0x100)
    {
        v0 = i;
        count = GetAsyncKeyState(i);
        idx = v0;
        if (idx == 0xff)
        {
            i = idx + 1;
        }
        else if (idx == 1)
        {
            i = idx + 1;
        }
        else if (idx == 2)
        {
            i = idx + 1;
        }
        else if (g_1005f120[idx] != count)
        {
            g_1005f120[idx] = count;
            v0 = idx;
            (&g_100faa3c)[(g_1005f524 - 5000) * 0x202] = idx;
            v7 = "lmouse";
            v8 = NULL;
            while (true)
            {
                if (v7 >= &g_100445f0)
                {
                    v1 = 35;
                    sub_10040940(idx, &v2);
                    break;
                }
                else if (*((char *)&v7[3] + 3) == (char)idx)
                {
                    v8 = v7;
                    break;
                }
                else
                {
                    v7 += 4;
                }
            }
            count = SendDlgItemMessageA(g_10072f84, g_1005f524, 12, NULL, v8);
            i = v0 + 1;
        }
        else
        {
            i = idx + 1;
        }
    }
    return count;
}
```

## `sub_1002b02b` `0x1002b02b`

_115 bytes. calls RegisterHotKey_

```c
extern HWND g_1005f626;

int sub_1002b02b(unsigned int a0)
{
    unsigned int i;  // ebx
    int j;  // ebx

    if (a0)
    {
        for (i = 166; i <= 183; i += 1)
        {
            RegisterHotKey(g_1005f626, i + 123, 0, i);
        }
        return RegisterHotKey(g_1005f626, 218, 0, i);
    }
    else
    {
        for (j = 166; j <= 183; j += 1)
        {
            UnregisterHotKey(g_1005f626, j + 123);
        }
        return UnregisterHotKey(g_1005f626, 218);
    }
}
```

## `sub_1002b09e` `0x1002b09e`

_2979 bytes. calls GetAsyncKeyState_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
} struct_0;

extern char g_1002b6fb;
extern char g_1002b7cd;
extern char g_1002bb7e;
extern char g_1002bc66;
extern unsigned int g_1005dbbc;
extern unsigned int g_1005dbc0;
extern unsigned int g_1005dbc4;
extern unsigned int g_1005dbc8;
extern unsigned int g_1005dbcc;
extern unsigned int g_1005dbd0;
extern unsigned int g_1005dbd4;
extern unsigned int g_1005f63b;
extern unsigned int g_1005f878;
extern char g_1005f87c;
extern char g_10084bff;
extern unsigned int g_10084c07;
extern unsigned int g_10084c0b[4];
extern unsigned int g_1008578b[4];
extern unsigned int g_1008630b[4];
extern unsigned int g_10086e8b[4];
extern unsigned int g_10087a0b[4];
extern void g_1008858b;
extern unsigned int g_1008910b[4];
extern unsigned int g_10089c8b;
extern char g_1008a80b;
extern char g_1008a90b;
extern unsigned int g_1008aa0b[4];
extern char g_1009a536;
extern char g_100ba736;
extern void* g_100ee8b6;
extern char g_100f0e42;
extern char g_100f49d5;
extern unsigned int g_100f9341;
extern unsigned int g_100f934d;
extern char g_100f94c5;
extern char g_100faa3c;
extern char g_10106b02;
extern char g_10135279;
extern char g_1013f32b;
extern char g_1014f420;
extern char g_101d5e26;
extern unsigned int g_102e2614;

int sub_1002b09e(void)
{
    void* v9;  // ebp
    char v10;  // al
    void* v17;  // edi
    unsigned int v18;  // eax
    unsigned int v19;  // eax
    unsigned int v20;  // ecx
    unsigned int v21;  // ebx
    unsigned int v22;  // eax
    unsigned int idx;  // edx
    unsigned int v24;  // eax
    unsigned int v25;  // edx
    unsigned int iter;  // ebx
    void* count;  // eax
    void* v27;  // eax
    char *v28;  // eax
    unsigned int index;  // edx
    unsigned int v30;  // ecx
    void* v31;  // eax
    unsigned int v32;  // eax
    void* v33;  // edi
    void* v34;  // edi
    void* v35;  // esi
    unsigned int v12;  // ecx
    unsigned int v38;  // eax
    void* v39;  // esi
    unsigned int idx1;  // edx
    unsigned int v41;  // eax
    unsigned int v42;  // ecx
    unsigned int count1;  // eax
    unsigned int v44;  // ebx
    unsigned int v13;  // edx
    void* iter1;  // ecx
    struct_0 **v46;  // eax
    struct_0 **v47;  // ecx
    unsigned int idx2;  // edx
    unsigned int v49;  // edx
    void* iter2;  // ebx
    unsigned int v51;  // esi
    unsigned int v52;  // edi
    void* v14;  // ebx
    unsigned int v53;  // edx
    unsigned int v54;  // edi
    unsigned int v55;  // edi
    unsigned int v56;  // esi
    unsigned int v59;  // eax
    unsigned int v60;  // edx
    unsigned int l;  // ecx
    unsigned int v15;  // esi
    unsigned int v62;  // ecx
    struct_0 **v64;  // eax
    struct_0 **v65;  // ecx
    unsigned int v66;  // edx
    unsigned int v16;  // edi
    int v1;  // [bp-0xfc0]
    int v2;  // [bp-0xfb9]
    unsigned int v3;  // [bp-0x80c]
    void* v4;  // [bp-0x808], Other Possible Types: unsigned int
    unsigned int v5;  // [bp-0x7f8]
    int v6;  // [bp-0x7e4]
    char v7;  // [bp+0x0]

    v6 = (int)_INSERT(*((uint16160_t *)(&v1 + 2016)), 2016, &v7);
    v9 = &v6 - 2016;
    v2 = (int)_INSERT(*((uint32200_t *)(&v1 + 2016)), 2016, v10);
    g_1005dbd0 = 0;
    g_1005dbcc = 0;
    g_100f9341 = 0;
    g_100f934d = 0;
    count = GetTickCount();
    *((void* *)&(&v1)[2000]) = count;
    if (!g_100f94c5)
    {
        v6 = (int)_INSERT(*((uint16160_t *)(&v1 + 2012)), 2012, 96);
    }
    else
    {
        v6 = (int)_INSERT(*((uint16160_t *)(&v1 + 2012)), 2012, 0);
        goto LABEL_1002b7c0;
    }
    while (true)
    {
        if ((int)v9[4] == 96)
        {
            *((void* *)&v9[4]) = 0xe0;
            if (!g_100f0e42)
                *((void* *)&v9[4]) = 0x160;
        }
        if ((int)v9[4] == 0x160 && !g_1013f32b)
            *((void* *)&v9[4]) = 0x1e0;
        if ((int)v9[4] == 480 && !g_101d5e26)
            *((void* *)&v9[4]) = 0x2e0;
LABEL_1002b7c0:
        if ((int)v9[4] >= 0x2e0)
            break;
        g_1005dbc8 = v9;
        g_1005dbc4 = &v1 - 1984;
        g_1005dbbc = 501;
        g_1005dbc0 = &g_1002b7cd;
        v2 = (int)_INSERT(*((uint32200_t *)(&v1 + 1973)), 1973, count);
        *((unsigned int *)&(&v2)[1969]) = v12;
        *((unsigned int *)&(&v2)[1965]) = v13;
        *((void* *)&(&v2)[1961]) = v14;
        *((void* *)&(&v2)[1957]) = &v2 - 1977;
        *((void* *)&(&v2)[1953]) = v9;
        *((unsigned int *)&(&v2)[1949]) = v15;
        *((unsigned int *)&(&v2)[1945]) = v16;
        g_1005dbd4 = GetTickCount();
        v9 = *((unsigned int *)(&v2 + 1953));
        v39 = *((unsigned int *)(&v2 + 1949));
        v17 = *((unsigned int *)(&v2 + 1945));
        if (g_102e2614)
        {
            g_102e2614 = 0;
            *((unsigned int *)&(&v2)[1973]) = 1;
            ExitThread(*((unsigned int *)(&v2 + 1973)));
        }
        *((unsigned int *)&v9[2016]) = 0;
        g_100ee8b6 = 0;
        g_1005dbcc = 0;
        g_1005dbd0 = 0;
        v18 = (int)v9[4];
        if (v18 < 96)
        {
            v19 = &(&g_100faa3c)[v18 * 0x202];
        }
        else if (v18 < 480)
        {
            v19 = &(&g_1009a536)[(v18 - 224) * 0x202];
        }
        else
        {
            *((char *)&v9[2017]) = 1;
            v27 = v18 - 480;
            v17 = v27;
            v39 = 0x4c;
            if (v27 >= 128)
            {
                v27 -= 128;
                v39 = 0x81c;
            }
            v28 = &(&g_1014f420)[v27 * 4308];
            if (*((int *)&v28[0x44]) && *((char *)(v39 + v28)))
            {
                g_10084c07 = (int)v9[4];
                iter = v39 + v28;
                v22 = *((char *)(v17 + &g_1008a80b));
                *((char *)(v17 + &g_1008a80b)) = 0;
                goto LABEL_1002b2bd;
            }
            else
            {
                *((char *)&v9[2017]) = 0;
                goto LABEL_1002b70f;
            }
        }
        if (!*((char *)(v19 + 1)) || !*((char *)(v19 + 2)) || !*((char *)v19))
            goto LABEL_1002b70f;
        g_10084c07 = (int)v9[4];
        v20 = *((char *)v19);
        v21 = v19;
        v22 = 0;
        if ((int)v9[4] < 96)
        {
            idx = (int)v9[4];
            v24 = (int)v9[2028] - g_1008aa0b[idx];
            if (v24 >= 100)
            {
                if (v24 < 150)
                    g_1008aa0b[idx] = g_1008aa0b[idx] + 100;
                else
                    g_1008aa0b[idx] = (int)v9[2028];
                *((unsigned int *)&(&v2)[1973]) = v20;
                v22 = GetAsyncKeyState(*((unsigned int *)(&v2 + 1973)));
                if (*((int *)&g_1005f87c) == (int)v9[4] && !v22)
                    g_1005f878 = 0;
            }
            else
            {
                v25 = idx * 4;
                v22 = (!*((int *)(v25 + (char *)&g_10084c0b[0])) ? *((int *)&(&g_1008858b)[v25]) | *((int *)(v25 + (char *)&g_10087a0b[0])) : 0);
            }
        }
        else if (*((char *)(v21 + 1)) == 255)
        {
            *((unsigned int *)&v9[2016]) = v21;
            iter = v21 + 2;
            goto LABEL_1002b421;
        }
        iter = v21 + 2;
LABEL_1002b2bd:
        if (v22)
        {
            if ((char)v9[2005])
                goto LABEL_1002b421;
            goto LABEL_1002b41c;
        }
        index = (int)v9[4] * 4;
        v30 = *((int *)(index + (char *)&g_10084c0b[0]));
        if (*((int *)(index + (char *)&g_10084c0b[0])))
        {
            *((char *)&v9[2017]) = 255;
            v31 = *((int *)(index + (char *)&g_10087a0b[0]));
            if (*((int *)(index + (char *)&g_10087a0b[0])))
            {
                g_100ee8b6 = 1;
                if (v31 > *((int *)&g_10084bff))
                {
                    *((int *)(index + (char *)&g_10087a0b[0])) = *((int *)(index + (char *)&g_10087a0b[0])) - *((int *)&g_10084bff);
                    goto LABEL_1002b41c;
                }
                *((unsigned int *)(index + (char *)&g_10087a0b[0])) = 0;
                if (!*((int *)&(&g_1008858b)[index]))
                    goto LABEL_1002b41c;
                *((char *)&v9[2017]) = 1;
            }
            else
            {
                v32 = *((int *)(index + (char *)&g_10086e8b[0])) + *((int *)&g_10084bff);
                if (v32 < v30)
                {
                    *((unsigned int *)(index + (char *)&g_10086e8b[0])) = v32;
                    g_100ee8b6 = 1;
                    sub_1002b3d7();
                    return;
                }
                v33 = *((int *)(index + (char *)&g_1008630b[0]));
                v39 = *((int *)(index + (char *)&g_1008578b[0]));
                v34 = v33;
                if (*((int *)(index + (char *)&g_1008578b[0])) || (v17 = v33, v34 = v17, v33))
                {
                    *((unsigned int *)&(&v2)[1973]) = index;
                    v35 = v39;
                    if (v35 < v34)
                    {
                        v34 = v39;
                        v35 = v34;
                    }
                    v39 = v35 - v34 + 1;
                    *((void* *)&(&v2)[1969]) = v34;
                    *((void* *)&(&v2)[1965]) = v39;
                    v17 = *((unsigned int *)(&v2 + 1965));
                    index = *((unsigned int *)(&v2 + 1969));
                    v38 = sub_10040a30(*((unsigned int *)(&v2 + 1965)), *((unsigned int *)(&v2 + 1969))) + v17;
                    if (!v38)
                        v38 += 1;
                    *((unsigned int *)(index + (char *)&g_10084c0b[0])) = v38;
                }
                *((unsigned int *)(index + (char *)&g_10086e8b[0])) = 0;
            }
            for (; *((char *)iter) == 32 && *((char *)iter); iter += 1);
            for (; *((char *)iter) != 32 && *((char *)iter); iter += 1);
            for (; *((char *)iter) == 32 && *((char *)iter); iter += 1);
            for (; *((char *)iter) != 32 && *((char *)iter); iter += 1);
            goto LABEL_1002b421;
        }
        else if (!*((int *)&(&g_1008858b)[index]) || (int)v9[4] < 480 || (int)v9[4] >= 0x2e0)
        {
            *((char *)&v9[2017]) = 0;
            *((unsigned int *)(index + (char *)&g_10087a0b[0])) = 0;
            *((unsigned int *)&(&g_1008858b)[index]) = 0;
            *((int *)&(&v2)[1973]) = *((int *)&g_100f49d5);
            *((unsigned int *)(index + (char *)&g_1008910b[0])) = *((unsigned int *)(&v2 + 1973));
LABEL_1002b41c:
            goto LABEL_1002b70f;
        }
        else
        {
LABEL_1002b421:
            g_1005dbd0 = iter;
            *((unsigned int *)&(&v2)[1985]) = iter;
            *((void* *)&(&v2)[1981]) = v9 - 2004;
            lstrcpy(*((unsigned int *)(&v2 + 1981)), *((unsigned int *)(&v2 + 1985)));
            if (((int)v9[2004] | 0x20202020) == 0x6f747561 && (char)v9[2000] == 32)
            {
                *((char *)&v9[2017]) = 1;
                v5 = *((int *)&g_100f49d5);
                g_1008910b[v9[4]] = *((int *)&g_100f49d5);
                *((unsigned int *)&(&v2)[1985]) = 0;
                *((unsigned int *)&(&v2)[1981]) = g_10084c07;
                *((void* *)&(&v2)[1977]) = v9 - 2004;
                sub_10030442(*((unsigned int *)(&v2 + 1977)), *((unsigned int *)(&v2 + 1981)), *((unsigned int *)(&v2 + 1985)));
            }
            else
            {
                *((char *)&v9[2017]) = 10;
                idx1 = (int)v9[4] * 4;
                if (!*((int *)(idx1 + (char *)&g_10087a0b[0])))
                {
                    v41 = *((int *)&(&g_1008858b)[idx1]);
                    *((unsigned int *)&(&g_1008858b)[idx1]) = 0;
                    if (!v41)
                    {
                        v41 = v9 - 2004;
                        *((int *)&(&v2)[1985]) = *((int *)(idx1 + (char *)&g_1008910b[0]));
                        *((unsigned int *)(idx1 + (char *)&g_10089c8b)) = *((unsigned int *)(&v2 + 1985));
                        v42 = *((int *)&g_100f49d5);
                        if (*((int *)(idx1 + (char *)&g_1008910b[0])) != *((int *)&g_100f49d5))
                        {
                            *((unsigned int *)(idx1 + (char *)&g_1008910b[0])) = *((int *)(idx1 + (char *)&g_1008910b[0])) + 1;
                            if (*((int *)(idx1 + (char *)&g_1008910b[0])) >= 2000)
                                *((unsigned int *)(idx1 + (char *)&g_1008910b[0])) = 0;
                        }
                    }
                    else
                    {
                        v42 = v9 - 2004;
                    }
                    *((unsigned int *)&v9[2012]) = 0;
                    g_1005dbc8 = v9;
                    g_1005dbc4 = &v2 - 1989;
                    g_1005dbbc = 502;
                    g_1005dbc0 = &g_1002b6fb;
                    *((unsigned int *)&(&v1)[1992]) = v41;
                    *((unsigned int *)&(&v1)[1988]) = v42;
                    *((unsigned int *)&(&v1)[1984]) = idx1;
                    *((unsigned int *)&(&v1)[1980]) = v41;
                    *((void* *)&(&v1)[1976]) = &v1 - 1996;
                    *((void* *)&(&v1)[1972]) = v9;
                    *((void* *)&(&v1)[1968]) = v39;
                    *((void* *)&(&v1)[1964]) = v17;
                    g_1005dbd4 = GetTickCount();
                    count1 = *((unsigned int *)(&v1 + 1992));
                    v44 = *((unsigned int *)(&v1 + 1980));
                    v9 = *((unsigned int *)(&v1 + 1972));
                    if (g_102e2614)
                    {
                        g_102e2614 = 0;
                        *((unsigned int *)&(&v1)[1992]) = 1;
                        count1 = (unsigned int)ExitThread(*((unsigned int *)(&v1 + 1992)));
                    }
                    iter1 = NULL;
                    while (iter1 < 0x200)
                    {
                        g_1005dbcc = v44;
                        if (*((char *)iter1 + count1) == 123)
                        {
                            *((unsigned int *)&v9[2012]) = (int)v9[2012] + 1;
                            iter1 += 1;
                            continue;
                        }
                        if (*((char *)iter1 + count1) == 125)
                        {
                            *((unsigned int *)&v9[2012]) = (int)v9[2012] - 1;
                            if ((int)v9[2012] == 4294967295)
                            {
                                *((unsigned int *)&v9[2024]) = 1;
                                *((unsigned int *)&v9[2012]) = 0;
                                goto LABEL_1002b611;
                            }
                            else
                            {
                                if (!(int)v9[2012])
                                {
                                    *((unsigned int *)&v9[2024]) = 0;
                                    iter1 += 1;
                                    goto LABEL_1002b611;
                                }
                                else
                                {
                                    iter1 += 1;
                                }
                            }
                        }
                        else
                        {
                            if (!(int)v9[2012] && *((char *)iter1 + count1) == 124 && *(1 + (char *)iter1 + count1) != 124 && *(-1 + (char *)iter1 + count1) != 124)
                            {
                                *((unsigned int *)&v9[2024]) = 1;
LABEL_1002b611:
                                *((int *)&(&v1)[1980]) = *((int *)((char *)iter1 + count1));
                                *((char *)iter1 + count1) = 0;
                                *((void* *)&(&v1)[1976]) = iter1;
                                *((unsigned int *)&(&v1)[1972]) = count1;
                                *((unsigned int *)&(&v1)[1968]) = 0;
                                *((unsigned int *)&(&v1)[1964]) = g_10084c07;
                                *((unsigned int *)&(&v1)[1960]) = v44;
                                sub_10030442(*((unsigned int *)(&v1 + 1960)), *((unsigned int *)(&v1 + 1964)), *((unsigned int *)(&v1 + 1968)), *((unsigned int *)(&v1 + 1972)), *((unsigned int *)(&v1 + 1976)), *((unsigned int *)(&v1 + 1980)));
                                v46 = *((unsigned int *)(&v1 + 1960));
                                v47 = *((unsigned int *)(&v1 + 1964));
                                *((unsigned int *)(v47 + v46)) = *((unsigned int *)(&v1 + 1968));
                                count1 = v46 + v47 + (int)v9[2024];
                                v44 = count1;
                                idx2 = (int)v9[4];
                                if (g_10087a0b[idx2] == 4294967295)
                                {
                                    g_10087a0b[idx2] = 0;
                                    *((unsigned int *)&(&g_1008858b)[4 * idx2]) = 0;
                                    break;
                                }
                                else
                                {
                                    if (g_10087a0b[idx2])
                                    {
                                        if (!*((int *)&(&g_1008858b)[4 * idx2]))
                                            *((unsigned int *)&(&g_1008858b)[4 * idx2]) = count1;
                                        break;
                                    }
                                    else
                                    {
                                        iter1 = NULL;
                                    }
                                }
                            }
                            else
                            {
                                if (!*((char *)iter1 + count1))
                                {
                                    *((unsigned int *)&(&v1)[1980]) = 0;
                                    *((unsigned int *)&(&v1)[1976]) = g_10084c07;
                                    *((unsigned int *)&(&v1)[1972]) = v44;
                                    sub_10030442(*((unsigned int *)(&v1 + 1972)), *((unsigned int *)(&v1 + 1976)), *((unsigned int *)(&v1 + 1980)));
                                    if ((int)v9[2016])
                                    {
                                        v49 = (int)v9[4];
                                        if (g_10087a0b[v49])
                                        {
                                            g_10087a0b[v49] = 0;
                                            *((unsigned int *)&(&g_1008858b)[4 * v49]) = 0;
                                            *((char *)((int)v9[2016] + 1)) = 0;
                                        }
                                    }
                                    break;
                                }
                                else
                                {
                                    iter1 += 1;
                                }
                            }
                        }
                    }
                    if ((int)v9[2016] && !g_10087a0b[v9[4]])
                        *((char *)((int)v9[2016] + 1)) = 0;
                }
                else if (*((int *)(idx1 + (char *)&g_10087a0b[0])) > *((int *)&g_10084bff))
                {
                    *((char *)&v9[2017]) = 1;
                    *((int *)(idx1 + (char *)&g_10087a0b[0])) = *((int *)(idx1 + (char *)&g_10087a0b[0])) - *((int *)&g_10084bff);
                }
                else
                {
                    *((unsigned int *)(idx1 + (char *)&g_10087a0b[0])) = 0;
                }
                g_1005dbcc = 0;
                g_1005dbd0 = 0;
            }
LABEL_1002b70f:
            if (g_100ee8b6 != 0x1)
                (&g_100ba736)[276 * v9[4]] = *((char *)&g_100ee8b6);
            count = (int)v9[4];
            if (count < 480)
            {
                *((unsigned int *)&v9[4]) = (int)v9[4] + 1;
            }
            else if (count < 0x2e0)
            {
                count -= 480;
                if ((char)v9[2017])
                {
                    *((char *)(count + &g_1008a90b)) = (char)v9[2017];
                    *((unsigned int *)&v9[4]) = (int)v9[4] + 1;
                }
                else if (!g_1005f63b)
                {
                    *((unsigned int *)&v9[4]) = (int)v9[4] + 1;
                }
                else if (*((char *)(count + &g_1008a90b)))
                {
                    *((char *)(count + &g_1008a90b)) = *((char *)(count + &g_1008a90b)) - 1;
                    *((unsigned int *)&v9[4]) = (int)v9[4] + 1;
                }
                else
                {
                    *((unsigned int *)&v9[4]) = (int)v9[4] + 1;
                }
            }
            else
            {
                *((unsigned int *)&v9[4]) = (int)v9[4] + 1;
            }
        }
    }
    if (!g_10135279)
        return;
    *((void* *)&v9[4]) = NULL;
    while ((int)v9[4] < 128)
    {
        g_1005dbc8 = v9;
        g_1005dbc4 = &v1 - 1980;
        g_1005dbbc = 551;
        g_1005dbc0 = &g_1002bc66;
        v4 = count;
        v3 = v12;
        *((unsigned int *)&(&v1)[1968]) = v13;
        *((void* *)&(&v1)[1964]) = iter2;
        *((void* *)&(&v1)[1960]) = &v1 - 1980;
        *((void* *)&(&v1)[1956]) = v9;
        *((unsigned int *)&(&v1)[1952]) = v51;
        *((unsigned int *)&(&v1)[1948]) = v52;
        g_1005dbd4 = GetTickCount();
        v9 = *((unsigned int *)(&v1 + 1956));
        v51 = *((unsigned int *)(&v1 + 1952));
        v52 = *((unsigned int *)(&v1 + 1948));
        if (g_102e2614)
        {
            g_102e2614 = 0;
            ExitThread(1);
        }
        g_100ee8b6 = 0;
        g_1005dbcc = 0;
        g_1005dbd0 = 0;
        iter2 = &(&g_10106b02)[546 * v9[4]];
        g_10084c07 = (int)v9[4] + 96;
        v53 = g_10084c07 * 4;
        if (*((int *)(v53 + (char *)&g_10084c0b[0])) && (char)iter2[33])
        {
            iter2 += 0x22;
            count = *((int *)(v53 + (char *)&g_10087a0b[0]));
            if (*((int *)(v53 + (char *)&g_10087a0b[0])))
            {
                g_100ee8b6 = 1;
                if (count > *((int *)&g_10084bff))
                {
                    *((int *)(v53 + (char *)&g_10087a0b[0])) = *((int *)(v53 + (char *)&g_10087a0b[0])) - *((int *)&g_10084bff);
                    goto LABEL_1002bc34;
                }
                else
                {
                    *((unsigned int *)(v53 + (char *)&g_10087a0b[0])) = 0;
                    if (!*((int *)&(&g_1008858b)[v53]))
                        goto LABEL_1002bc34;
                }
            }
            else
            {
                count = *((int *)(v53 + (char *)&g_10086e8b[0])) + *((int *)&g_10084bff);
                if (count < *((int *)(v53 + (char *)&g_10084c0b[0])))
                {
                    g_100ee8b6 = 1;
                    *((void* *)(v53 + (char *)&g_10086e8b[0])) = count;
LABEL_1002bba4:
                    goto LABEL_1002bc34;
                }
            }
            v54 = *((int *)(v53 + (char *)&g_1008630b[0]));
            v51 = *((int *)(v53 + (char *)&g_1008578b[0]));
            v55 = v54;
            if (*((int *)(v53 + (char *)&g_1008578b[0])) || (v52 = v54, v55 = v52, v54))
            {
                v4 = v53;
                v56 = v51;
                if (v56 < v55)
                {
                    v55 = v51;
                    v56 = v55;
                }
                v51 = v56 - v55 + 1;
                *((unsigned int *)&(&v1)[1968]) = v51;
                v52 = *((unsigned int *)(&v1 + 1968));
                v53 = *((unsigned int *)(&v1 + 1972));
                v59 = sub_10040a30(*((unsigned int *)(&v1 + 1968)), *((unsigned int *)(&v1 + 1972))) + v52;
                if (!v59)
                    v59 += 1;
                *((unsigned int *)(v53 + (char *)&g_10084c0b[0])) = v59;
            }
            for (*((unsigned int *)(v53 + (char *)&g_10086e8b[0])) = 0; *((char *)iter2) == 32 && *((char *)iter2); iter2 += 1);
            for (; *((char *)iter2) != 32 && *((char *)iter2); iter2 += 1);
            for (; *((char *)iter2) == 32 && *((char *)iter2); iter2 += 1);
            for (; *((char *)iter2) != 32 && *((char *)iter2); iter2 += 1);
            g_1005dbd0 = iter2;
            *((void* *)&(&v1)[1976]) = iter2;
            *((void* *)&(&v1)[1972]) = v9 - 2004;
            lstrcpy(*((unsigned int *)(&v1 + 1972)), *((unsigned int *)(&v1 + 1976)));
            count = (int)v9[2004] | 0x20202020;
            if (count == 0x6f747561 && (char)v9[2000] == 32)
                goto LABEL_1002bba4;
            goto LABEL_1002b982;
        }
        else
        {
            count = (int)iter2[0x22] | 0x20202020;
            if (count == 0x6f747561 && (char)iter2[38] == 32)
            {
                *((unsigned int *)(v53 + (char *)&g_10087a0b[0])) = 0;
                *((unsigned int *)&(&g_1008858b)[v53]) = 0;
                goto LABEL_1002bc34;
            }
            if (*((int *)&(&g_1008858b)[v53]) && (char)iter2[33])
            {
                count = *((int *)(v53 + (char *)&g_10087a0b[0]));
                if (count > *((int *)&g_10084bff))
                {
                    *((int *)(v53 + (char *)&g_10087a0b[0])) = *((int *)(v53 + (char *)&g_10087a0b[0])) - *((int *)&g_10084bff);
                    goto LABEL_1002bc34;
                }
                else
                {
                    *((unsigned int *)(v53 + (char *)&g_10087a0b[0])) = 0;
                    v2 = (int)_INSERT(*((uint32200_t *)(&v1 + 1969)), 1969, iter2 + 0x22);
                    *((void* *)&(&v2)[1965]) = v9 - 2004;
                    lstrcpy(*((unsigned int *)(&v2 + 1965)), *((unsigned int *)(&v2 + 1969)));
                }
LABEL_1002b982:
                v60 = ((int)v9[4] + 96) * 4;
                if (!*((int *)&(&g_1008858b)[v60]))
                {
                    *((int *)&(&v2)[1969]) = *((int *)(v60 + (char *)&g_1008910b[0]));
                    *((unsigned int *)(v60 + (char *)&g_10089c8b)) = *((unsigned int *)(&v2 + 1969));
                    if (*((int *)(v60 + (char *)&g_1008910b[0])) != *((int *)&g_100f49d5))
                    {
                        *((unsigned int *)(v60 + (char *)&g_1008910b[0])) = *((int *)(v60 + (char *)&g_1008910b[0])) + 1;
                        if (*((int *)(v60 + (char *)&g_1008910b[0])) >= 2000)
                            *((unsigned int *)(v60 + (char *)&g_1008910b[0])) = 0;
                    }
                }
                count = v9 - 2004 + *((int *)&(&g_1008858b)[v60]);
                *((unsigned int *)&(&g_1008858b)[v60]) = 0;
                *((unsigned int *)&v9[2012]) = 0;
                iter2 = count;
                l = 0;
                while (l < 0x200)
                {
                    g_1005dbc8 = v9;
                    g_1005dbc4 = &v2 - 1961;
                    g_1005dbbc = 552;
                    g_1005dbc0 = &g_1002bb7e;
                    *((void* *)&(&v1)[1964]) = count;
                    *((unsigned int *)&(&v1)[1960]) = l;
                    *((unsigned int *)&(&v1)[1956]) = v13;
                    *((void* *)&(&v1)[1952]) = iter2;
                    *((void* *)&(&v1)[1948]) = &v1 - 1968;
                    *((void* *)&(&v1)[1944]) = v9;
                    *((unsigned int *)&(&v1)[1940]) = v51;
                    *((unsigned int *)&(&v1)[1936]) = v52;
                    g_1005dbd4 = GetTickCount();
                    count = *((unsigned int *)(&v1 + 1964));
                    iter2 = *((unsigned int *)(&v1 + 1952));
                    v9 = *((unsigned int *)(&v1 + 1944));
                    v51 = *((unsigned int *)(&v1 + 1940));
                    v52 = *((unsigned int *)(&v1 + 1936));
                    if (g_102e2614)
                    {
                        g_102e2614 = 0;
                        *((unsigned int *)&(&v1)[1964]) = 1;
                        count = (unsigned int)ExitThread(*((unsigned int *)(&v1 + 1964)));
                    }
                    g_1005dbcc = iter2;
                    if (*(v12 + (char *)count) == 123)
                    {
                        *((unsigned int *)&v9[2012]) = (int)v9[2012] + 1;
                        l = v12 + 1;
                        continue;
                    }
                    if (*(v12 + (char *)count) == 125)
                    {
                        *((unsigned int *)&v9[2012]) = (int)v9[2012] - 1;
                        if ((int)v9[2012] == 4294967295)
                        {
                            *((unsigned int *)&v9[2024]) = 1;
                            *((unsigned int *)&v9[2012]) = 0;
                            v62 = v12;
                            goto LABEL_1002bad6;
                        }
                        else
                        {
                            if (!(int)v9[2012])
                            {
                                *((unsigned int *)&v9[2024]) = 0;
                                v62 = v12 + 1;
                                goto LABEL_1002bad6;
                            }
                            else
                            {
                                l = v12 + 1;
                            }
                        }
                    }
                    else if (!(int)v9[2012] && *(v12 + (char *)count) == 124 && *(1 + v12 + (char *)count) != 124 && *(-1 + v12 + (char *)count) != 124)
                    {
                        *((unsigned int *)&v9[2024]) = 1;
                        v62 = v12;
LABEL_1002bad6:
                        *((int *)&(&v1)[1964]) = *((int *)(v62 + (char *)count));
                        *(v62 + (char *)count) = 0;
                        *((unsigned int *)&(&v1)[1960]) = v62;
                        *((void* *)&(&v1)[1956]) = count;
                        *((unsigned int *)&(&v1)[1952]) = 0;
                        *((unsigned int *)&(&v1)[1948]) = (int)v9[4] + 96;
                        *((void* *)&(&v1)[1944]) = iter2;
                        sub_10030442(*((unsigned int *)(&v1 + 1944)), *((unsigned int *)(&v1 + 1948)), *((unsigned int *)(&v1 + 1952)), *((unsigned int *)(&v1 + 1956)), *((unsigned int *)(&v1 + 1960)), *((unsigned int *)(&v1 + 1964)));
                        v64 = *((unsigned int *)(&v1 + 1944));
                        v65 = *((unsigned int *)(&v1 + 1948));
                        *((unsigned int *)(v65 + v64)) = *((unsigned int *)(&v1 + 1952));
                        count = v64 + v65 + (int)v9[2024];
                        iter2 = count;
                        v66 = (int)v9[4] + 96;
                        if (g_10087a0b[v66] == 4294967295)
                        {
                            g_10087a0b[v66] = 0;
                            *((unsigned int *)&(&g_1008858b)[4 * v66]) = 0;
                            break;
                        }
                        else
                        {
                            if (g_10087a0b[v66])
                            {
                                if (*((int *)&(&g_1008858b)[4 * v66]))
                                    count = *((int *)&(&g_1008858b)[4 * v66]);
                                count -= v9 - 2004;
                                *((void* *)&(&g_1008858b)[4 * v66]) = count;
                                break;
                            }
                            else
                            {
                                l = 0;
                            }
                        }
                    }
                    else if (!*(v12 + (char *)count))
                    {
                        *((unsigned int *)&(&v1)[1964]) = 0;
                        *((unsigned int *)&(&v1)[1960]) = (int)v9[4] + 96;
                        *((void* *)&(&v1)[1956]) = iter2;
                        count = sub_10030442(*((unsigned int *)(&v1 + 1956)), *((unsigned int *)(&v1 + 1960)), *((unsigned int *)(&v1 + 1964)));
                        break;
                    }
                    else
                    {
                        l = v12 + 1;
                    }
                }
                g_1005dbcc = 0;
                g_1005dbd0 = 0;
                goto LABEL_1002bba4;
            }
            else
            {
                *((unsigned int *)(v53 + (char *)&g_10087a0b[0])) = 0;
                *((unsigned int *)&(&g_1008858b)[v53]) = 0;
LABEL_1002bc34:
                if (g_100ee8b6 != 0x1)
                {
                    count = g_100ee8b6;
                    (&g_100ba736)[26496 + 276 * v9[4]] = *((char *)&g_100ee8b6);
                    *((unsigned int *)&v9[4]) = (int)v9[4] + 1;
                }
                else
                {
                    *((unsigned int *)&v9[4]) = (int)v9[4] + 1;
                }
            }
        }
    }
    return;
}
```

## `sub_1002b2d3` `0x1002b2d3`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1002b2d3(void)
{
}
```

## `sub_1002b3c5` `0x1002b3c5`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002b3c5(void)
{
    sub_1002b3d7();
    return;
}
```

## `sub_1002b3d7` `0x1002b3d7`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002b3d7(void)
{
}
```

## `sub_1002b5ba` `0x1002b5ba`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1002b5ba(void)
{
}
```

## `sub_1002b5d9` `0x1002b5d9`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1002b5d9(void)
{
}
```

## `sub_1002b661` `0x1002b661`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002b661(void)
{
}
```

## `sub_1002b680` `0x1002b680`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002b680(void)
{
}
```

## `sub_1002ba7b` `0x1002ba7b`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1002ba7b(void)
{
}
```

## `sub_1002ba9a` `0x1002ba9a`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1002ba9a(void)
{
}
```

## `sub_1002bb2a` `0x1002bb2a`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002bb2a(void)
{
}
```

## `sub_1002bb58` `0x1002bb58`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002bb58(void)
{
}
```

## `sub_1002bc1e` `0x1002bc1e`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002bc1e(void)
{
}
```

## `sub_1002bc68` `0x1002bc68`

_458 bytes. calls GetAsyncKeyState_

```c
extern char g_1002bcdb;
extern char g_1002bd2e;
extern char g_1002bddb;
extern char g_1002be26;
extern unsigned int g_1005dbbc;
extern unsigned int g_1005dbc0;
extern unsigned int g_1005dbc4;
extern unsigned int g_1005dbc8;
extern unsigned int g_1005dbcc;
extern unsigned int g_1005dbd0;
extern unsigned int g_1005dbd4;
extern unsigned int g_100ee8d8;
extern unsigned int g_10291cda;
extern unsigned int g_102e2614;

int sub_1002bc68(void)
{
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    unsigned int v22;  // edi
    unsigned int count;  // eax
    unsigned int count1;  // eax
    unsigned long v25;  // 4113
    unsigned short v14;  // fs
    unsigned long v15;  // 4129
    unsigned long v16;  // 4137
    unsigned int v17;  // eax
    unsigned int v18;  // ecx
    unsigned int v19;  // edx
    unsigned int v20;  // ebx
    unsigned int v21;  // esi
    unsigned int v0;  // [bp-0x6c]
    unsigned int v1;  // [bp-0x68]
    char *v2;  // [bp-0x64]
    char *v3;  // [bp-0x60]
    unsigned int v4;  // [bp-0x5c]
    unsigned int v5;  // [bp-0x58]
    unsigned int v6;  // [bp-0x54]
    unsigned int v7;  // [bp-0x50]
    unsigned int v8;  // [bp-0x4c]
    unsigned int v9;  // [bp-0x48]
    char v10;  // [bp-0x4]

    v9 = sub_10002509;
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    v8 = *((int *)v15);
    v16 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v16) = &v8;
    g_1005dbc8 = &v10;
    g_1005dbc4 = &v8;
    g_1005dbbc = 1;
    g_1005dbc0 = &g_1002bcdb;
    v7 = v17;
    v6 = v18;
    v5 = v19;
    v4 = v20;
    v3 = &v8;
    v2 = &v10;
    v1 = v21;
    v0 = v22;
    g_1005dbd4 = GetTickCount();
    if (g_102e2614)
    {
        g_102e2614 = 0;
        count = (unsigned int)ExitThread(1);
    }
    g_1005dbcc = 0;
    g_1005dbd0 = 0;
    g_1005dbc8 = &v10;
    g_1005dbc4 = &v8;
    g_1005dbbc = 2;
    g_1005dbc0 = &g_1002bd2e;
    v7 = count;
    v6 = v18;
    v5 = v19;
    v3 = &v8;
    v2 = &v10;
    g_1005dbd4 = GetTickCount();
    if (g_102e2614)
    {
        g_102e2614 = 0;
        ExitThread(1);
    }
    count1 = (!g_10291cda ? 0 : 1);
    g_1005dbc8 = &v10;
    g_1005dbc4 = &v8;
    g_1005dbbc = 4;
    g_1005dbc0 = &g_1002bddb;
    v7 = count1;
    v6 = v18;
    v5 = v19;
    v3 = &v8;
    v2 = &v10;
    g_1005dbd4 = GetTickCount();
    if (g_102e2614)
    {
        g_102e2614 = 0;
        count1 = (unsigned int)ExitThread(1);
    }
    v7 = count1;
    if (GetAsyncKeyState(38))
        g_100ee8d8 = 101;
    if (GetAsyncKeyState(39))
        g_100ee8d8 = 0x66;
    if (GetAsyncKeyState(40))
        g_100ee8d8 = 103;
    if (GetAsyncKeyState(37))
        g_100ee8d8 = 104;
    g_1005dbc8 = &v10;
    g_1005dbc4 = &v8;
    g_1005dbbc = 5;
    g_1005dbc0 = &g_1002be26;
    v6 = v18;
    v5 = v19;
    v3 = &v8;
    v2 = &v10;
    g_1005dbd4 = GetTickCount();
    if (g_102e2614)
    {
        g_102e2614 = 0;
        ExitThread(1);
    }
    sub_1002b09e();
    v25 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int *)v25) = v8;
    return;
}
```

## `sub_1002be32` `0x1002be32`

_165 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern int g_1005f85c;

unsigned int sub_1002be32(unsigned int a0)
{
    unsigned int v2[2];  // eax
    unsigned int v3;  // ecx
    unsigned int iter[2];  // esi
    unsigned int i;  // [bp-0xc]
    unsigned int node;  // [bp-0x8]

    for (i = 0; i < 3; i += 1)
    {
        node = 0;
        while (node < 3)
        {
            v2 = sub_1003a03f(g_1005f854 - 1 + node, g_1005f858 - 1 + i, g_1005f85c);
            if (v2)
            {
                v3 = v2[0];
                for (iter = &v2[1]; v3; iter = &iter[1 + 1])
                {
                    if (iter[0] == a0 || a0 == 4294967295 && iter[0] >= 3497 && iter[0] <= 3500)
                        return g_1005f854 - 1 + node;
                    v3 -= 1;
                }
                node += 1;
            }
            else
            {
                node += 1;
            }
        }
    }
    return 0;
}
```

## `sub_1002bed7` `0x1002bed7`

_97 bytes. (leaf/helper — see body)_

```c
int sub_1002bed7(void)
{
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    v0 = v2;
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
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    v0 = (/* unsupported instruction */ ? /* unsupported instruction */ : nan);
    /* unsupported instruction */
    /* unsupported instruction */
    return v0 - 200 - v2 * v2 * 100;
}
```

## `sub_1002bf38` `0x1002bf38`

_159 bytes. refs "%02d:%02d:%02d", "%02dh%02dm%02ds", "%02d:%02d:%02d:%02d"_

```c
extern char g_1013f325;

int sub_1002bf38(void)
{
    unsigned int v5;  // eax
    unsigned int v6;  // eax
    PSTR v7;  // edi
    PSTR v8;  // edi
    unsigned int v9;  // eax
    unsigned int v10;  // eax
    PSTR v11;  // edi
    PSTR v12;  // edi
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    unsigned int v3;  // [bp-0x4]

    if (v5 < 86400)
    {
        v6 = v5 % 3600;
        if (!g_1013f325)
        {
            wsprintfA(v8, "%02d:%02d:%02d");
            return;
        }
        v3 = v6 % 60;
        v2 = v6 / 60;
        v1 = v5 / 3600;
        wsprintfA(v7, "%02dh%02dm%02ds");
        return;
    }
    else
    {
        v9 = v5 % 86400;
        v10 = v9 % 3600;
        if (!g_1013f325)
        {
            wsprintfA(v12, "%02d:%02d:%02d:%02d");
            return;
        }
        v3 = v10 % 60;
        v2 = v10 / 60;
        v1 = v9 / 3600;
        v0 = v5 / 86400;
        wsprintfA(v11, "%02dd%02dh%02dm%02ds");
        return;
    }
}
```

## `sub_1002bfd7` `0x1002bfd7`

_160 bytes. refs "%d,%03d,%03d,%03d", "%d,%03d,%03d", "%d,%03d"_

```c
int sub_1002bfd7(void)
{
    unsigned int v5;  // eax
    unsigned int v6;  // eax
    unsigned int v7;  // eax
    PSTR v8;  // edi
    unsigned int v9;  // eax
    PSTR v10;  // edi
    PSTR v11;  // edi
    PSTR v12;  // edi
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    unsigned int v3;  // [bp-0x4]

    if (v5 >= 1000000000)
    {
        v6 = v5 % 1000000000;
        v7 = v6 % 1000000;
        v3 = v7 % 1000;
        v2 = v7 / 1000;
        v1 = v6 / 1000000;
        v0 = v5 / 1000000000;
        wsprintfA(v8, "%d,%03d,%03d,%03d");
        return;
    }
    else if (v5 >= 1000000)
    {
        v9 = v5 % 1000000;
        v3 = v9 % 1000;
        v2 = v9 / 1000;
        v1 = v5 / 1000000;
        wsprintfA(v10, "%d,%03d,%03d");
        return;
    }
    else if (v5 >= 1000)
    {
        v3 = v5 % 1000;
        v2 = v5 / 1000;
        wsprintfA(v11, "%d,%03d");
        return;
    }
    else
    {
        v3 = v5;
        wsprintfA(v12, "%d");
        return;
    }
}
```

## `sub_1002c077` `0x1002c077`

_84 bytes. (leaf/helper — see body)_

```c
int sub_1002c077(void)
{
    char v0;  // [bp-0x88]

    sub_10030225();
    if (lstrcmpi(&v0, "id"))
        return;
    return;
}
```

## `sub_1002c0cb` `0x1002c0cb`

_235 bytes. refs "fist", "club", "sword"_

```c
unsigned int sub_1002c0cb(int a0)
{
    int v0;  // eax
    int v10;  // eax
    int v12;  // eax
    int v14;  // eax
    int v2;  // eax
    int v4;  // eax
    int v6;  // eax
    int v8;  // eax

    v0 = lstrcmpi(a0, "fist");
    if (!v0)
        return _INSERT(v0, 0, 0);
    v2 = lstrcmpi(a0, "club");
    if (!v2)
        return _INSERT(v2, 0, 1);
    v4 = lstrcmpi(a0, "sword");
    if (!v4)
        return _INSERT(v4, 0, 2);
    v6 = lstrcmpi(a0, "axe");
    if (!v6)
        return _INSERT(v6, 0, 3);
    v8 = lstrcmpi(a0, "distance");
    if (!v8)
        return _INSERT(v8, 0, 4);
    v10 = lstrcmpi(a0, "shielding");
    if (!v10)
        return _INSERT(v10, 0, 5);
    v12 = lstrcmpi(a0, "fishing");
    if (!v12)
        return _INSERT(v12, 0, 6);
    v14 = lstrcmpi(a0, "mlevel");
    if (v14)
        return 0;
    return _INSERT(v14, 0, 7);
}
```

## `sub_1002c1b6` `0x1002c1b6`

_114 bytes. calls MessageBoxA_

```c
extern char g_10292304;
extern char g_102b2404;
extern char g_102d2504;

unsigned int sub_1002c1b6(char *a0, unsigned int a1)
{
    unsigned int idx;  // eax
    unsigned int i;  // ecx
    char *v3;  // esi
    unsigned int v5;  // ebx
    char v0;  // [bp+0x0]

    sub_1002ff87(a0, &v0);
    idx = 0;
    i = 0;
    v3 = a0;
    do
    {
        i = _INSERT(i, 0, *(v3));
        idx = idx * 5 + i;
        v3 += 1;
    } while (i);
    if (v5 == &g_10292304)
    {
        idx &= 0x3fff;
    }
    else if (v5 == &g_102b2404)
    {
        idx &= 0x3fff;
    }
    else if (v5 == &g_102d2504)
    {
        idx &= 0x1fff;
    }
    if (!*((int *)(v5 + idx * 8)))
    {
        *((char **)(v5 + idx * 8)) = a0;
        *((unsigned int *)(v5 + idx * 8 + 4)) = a1;
        return idx;
    }
    return MessageBoxA(NULL, a0, *((int *)(v5 + idx * 8)), MB_APPLMODAL);
}
```

## `sub_1002c228` `0x1002c228`

_7792 bytes. refs "name", "posx", "distance"_

```c
typedef struct struct_0 {
    char padding_0[1];
    char field_1;
} struct_0;

typedef struct struct_4 {
    char field_0;
    char padding_1[291];
    unsigned short field_124;
    unsigned short field_126;
    unsigned int field_128;
    unsigned int field_12c;
} struct_4;

typedef struct struct_5 {
    char padding_0[36];
    unsigned int field_24;
    char padding_28[4];
    int field_2c;
} struct_5;

typedef struct struct_2 {
    char field_0;
    char padding_1[31];
    char field_20;
    char padding_21[479];
    char field_200;
} struct_2;

typedef struct struct_6 {
    struct struct_5 *field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
} struct_6;

typedef struct struct_1 {
    int field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
} struct_1;

extern struct_2 *g_100f49d1;
extern char g_100f49ed;
extern struct_6 g_100f9109;
extern char g_10292303;
extern struct_1 g_102b2404;
extern struct_1 g_102d2504;

int sub_1002c228(void)
{
    char v41;  // cl
    unsigned int v42;  // eax
    void* iter;  // esi
    unsigned int index;  // ecx
    struct_5 *v136;  // esi
    struct_5 *v137;  // esi
    char v138;  // al
    char v52;  // cl
    unsigned short v53;  // cx
    char v54;  // dl
    char v55;  // dl
    void* iter1;  // esi
    unsigned short v57;  // cx
    char *iter2;  // eax
    char v59;  // cl
    void* v60;  // esi
    struct_0 *v43;  // ebx
    char v61;  // cl
    void* v62;  // esi
    void* v63;  // esi
    char v64;  // cl
    char v65;  // dl
    char v66;  // dl
    void* v67;  // esi
    unsigned short v68;  // cx
    char *v69;  // eax
    struct_0 *v44;  // ebx
    char v70;  // cl
    char *v71;  // eax
    unsigned short v72;  // cx
    char *v73;  // ecx
    char *v74;  // ecx
    char *v75;  // ebx
    unsigned int v76;  // cc_dep1
    char *v77;  // esi
    int v78;  // ecx
    void* v79;  // esi
    void* v45;  // edi
    char *v80;  // ebx
    unsigned int v81;  // eax
    char node[4];  // ebx
    unsigned short *v83;  // edi
    char v84[3];  // esi
    char v85;  // cl
    char v86;  // cl
    char v87;  // cl
    char *v46;  // esi
    char v88[3];  // esi
    char idx[3];  // esi
    char v90;  // cl
    unsigned long v91;  // ldt
    unsigned long v92;  // gdt
    unsigned short v93;  // ss
    unsigned long v94;  // 4131
    char v47;  // cl
    unsigned int v95;  // eax
    unsigned int i;  // ecx
    char *v97;  // esi
    unsigned int v99;  // eax
    char v100[513];  // ebx
    char v101[513];  // edx
    struct_4 *v102;  // eax
    unsigned int v103;  // eax
    unsigned int j;  // ecx
    char v48;  // cl
    char v105[3];  // esi
    unsigned int v107;  // eax
    struct_4 *v108;  // ebx
    unsigned short *v109;  // ecx
    unsigned short *v110;  // ecx
    unsigned short *v111;  // ecx
    unsigned short *v112;  // ecx
    unsigned short *v113;  // ecx
    unsigned short *v114;  // ecx
    char *m;  // esi
    unsigned short *v115;  // ecx
    unsigned short *v116;  // ecx
    unsigned short *v117;  // ecx
    unsigned short *v119;  // ecx
    unsigned short *v120;  // ecx
    unsigned short *v122;  // ecx
    unsigned short *v124;  // ecx
    unsigned int v50;  // eax
    unsigned short *v126;  // ecx
    unsigned short *v128;  // ecx
    unsigned short *v130;  // ecx
    unsigned short *v131;  // ecx
    unsigned short *v132;  // ecx
    unsigned short *v133;  // ecx
    char v134;  // al
    struct_4 *v0;  // [bp-0x2890], Other Possible Types: void*
    int v1;  // [bp-0x288e]
    char *v2;  // [bp-0x288c], Other Possible Types: struct_4 *, void*, unsigned int
    unsigned short *v3;  // [bp-0x2888], Other Possible Types: struct_4 *, unsigned int
    char v4[513];  // [bp-0x2884]
    char v5[3];  // [bp-0x2880], Other Possible Types: struct_0 *, char [4], unsigned int
    unsigned int v6;  // [bp-0x287c]
    char v7[4];  // [bp-0x2878]
    char *v8;  // [bp-0x2874], Other Possible Types: unsigned int
    char v9[3];  // [bp-0x2870], Other Possible Types: unsigned int
    char *v10;  // [bp-0x286c], Other Possible Types: unsigned int
    char v11[3];  // [bp-0x2868]
    char *v12;  // [bp-0x2864], Other Possible Types: unsigned int
    char v13[3];  // [bp-0x2860]
    char v14[3];  // [bp-0x285c]
    char v15[3];  // [bp-0x2858]
    unsigned int v16;  // [bp-0x2854]
    unsigned int v17;  // [bp-0x2854]
    void* v18;  // [bp-0x2850]
    void* v19;  // [bp-0x284c]
    void* v20;  // [bp-0x2848]
    void* v21;  // [bp-0x2844]
    void* v22;  // [bp-0x2840]
    void* v23;  // [bp-0x283c]
    unsigned short v24;  // [bp-0x2836]
    char *len;  // [bp-0x2830], Other Possible Types: char, int
    void* v26;  // [bp-0x282c]
    unsigned int v27;  // [bp-0x2828]
    char *v28;  // [bp-0x2824]
    char *v29;  // [bp-0x2820]
    unsigned short v30;  // [bp-0x281c]
    unsigned short v31;  // [bp-0x281c]
    char v32;  // [bp-0x204d]
    unsigned short v33;  // [bp-0x204c]
    char v34;  // [bp-0x187c]
    char v35;  // [bp-0x10ae]
    char v36;  // [bp-0x10ac]
    char v37;  // [bp-0x8dc]
    unsigned short *k;  // [bp-0xc], Other Possible Types: void*
    char *v39;  // [bp-0x8]

    if (v41 == 91)
    {
        v6 = v42;
        v44 = &v43->field_1;
        k = v45;
        v46 = &v37;
        v47 = (char)v44->padding_0;
        while (true)
        {
            v48 = v47;
            if (!v47 || v48 == 93)
                break;
            *(v46) = v48;
            v46 += 1;
            v44 = &v44->field_1;
            v47 = (char)v44->padding_0;
        }
        if (v48 == 93)
            v44 = &v44->field_1;
        v5 = v44;
        while (true)
        {
            *(v46) = 0;
            v28 = v46;
            v27 = 0;
            m = &v37;
            v29 = &v37;
            while (true)
            {
                while (true)
                {
                    for (v50 = 0; *(m) == 40; m += 1)
                    {
                        v50 += 1;
                        if (v50 >= v27)
                        {
                            v27 = v50;
                            v29 = m;
                        }
                    }
                    if (*(m) != 41)
                        break;
                    m += 1;
                    if (v50 == v27)
                        v28 = m;
                    v50 -= 1;
                }
                if (!*(m))
                    break;
                m += 1;
            }
            if (v27)
            {
                lstrcpy(&v36, v29 + 1);
                *(&v35 + v28 - v29) = 0;
                v17 = v16;
                v31 = v30;
            }
            else
            {
                lstrcpy(&v36, v29);
                v17 = v16;
                v31 = v30;
            }
            while (true)
            {
                iter = &v36;
                v26 = &v36;
                v20 = &v36;
                v19 = &v36;
                v18 = &v36;
                v23 = NULL;
                v22 = NULL;
                v21 = NULL;
                while (true)
                {
                    v52 = *((short *)iter);
                    v53 = _INSERT(v52, 0, v52);
                    if (!v52)
                        break;
                    if ((char)v53 == 42 || (char)v53 == 47 || (char)v53 == 37)
                        goto LABEL_1002c368;
                    if ((char)v53 == 43 || (char)v53 == 45 || (char)v53 == 63)
                    {
                        if (!v23)
                            v23 = iter;
                        iter += 1;
                        v26 = iter;
                    }
                    else
                    {
                        if (v53 == 0x3d3d || v53 == 15678 || v53 == 15676 || v53 == 15649)
                        {
                            if (!v22)
                                v22 = iter;
                            iter += 2;
                            v26 = iter;
                            if (!v23)
                                v20 = iter;
                        }
                        else
                        {
                            if ((char)v53 == 62 || (char)v53 == 60)
                            {
                                if (!v22)
                                    v22 = iter;
                                iter += 1;
                                v26 = iter;
                                if (!v23)
                                    v20 = iter;
                            }
                            else
                            {
                                if (v53 == 0x2626 || v53 == 0x7c7c)
                                {
                                    if (!v21)
                                        v21 = iter;
                                    iter += 2;
                                    v26 = iter;
                                    if (!v23)
                                        v20 = iter;
                                    if (!v22)
                                        v19 = iter;
                                }
                                else
                                {
                                    if ((char)v53 == 39 || (char)v53 == 0x22)
                                    {
                                        iter += 1;
                                        v54 = *((char *)iter);
                                        while (true)
                                        {
                                            if (!v54 || v54 == (char)v53)
                                                break;
                                            iter += 1;
                                            v54 = *((char *)iter);
                                        }
                                        if (v55)
                                            iter += 1;
                                    }
                                    else
                                    {
                                        iter += 1;
                                    }
                                }
                            }
                        }
                    }
                }
                iter = v23;
                if (v23)
                {
                    v2 = v20;
                    v26 = v20;
                    v53 = *((short *)iter);
                    goto LABEL_1002c368;
                }
                iter = v22;
                if (v22)
                {
                    v2 = v19;
                    v26 = v19;
                    v53 = *((short *)iter);
                    goto LABEL_1002c368;
                }
                iter = v21;
                if (!v21)
                    break;
                v2 = v18;
                v26 = v18;
                v53 = *((short *)iter);
LABEL_1002c368:
                v24 = v53;
                *((char *)iter) = 0;
                iter1 = iter + 1;
                if (*((char *)iter1) == 61 || *((char *)iter1) == 124 || *((char *)iter1) == 38)
                {
                    *((char *)iter1) = 0;
                    iter1 += 1;
                }
                v57 = v24;
                if ((char)v57 == 63 || v57 == 0x3d3d || v57 == 15649)
                {
                    sub_10030225(iter1);
                    if (!(char)v33)
                        v33 = 48;
                    v17 = 1;
                    iter2 = &v33;
                    while (true)
                    {
                        v59 = *(iter2);
                        if (!*(iter2))
                            break;
                        if (v59 != 32 && (v59 < 48 || v59 > 57))
                        {
                            v17 = 0;
                            break;
                        }
                        else
                        {
                            iter2 += 1;
                        }
                    }
                }
                len = sub_100300ce();
                v60 = iter1;
                v61 = *((char *)v60);
                v62 = v60;
                while (true)
                {
                    v63 = v62;
                    v64 = v61;
                    if (!v61 || v64 == 42 || v64 == 47 || v64 == 37 || v64 == 43 || v64 == 45 || v64 == 62 || v64 == 60 || v64 == 61 || v64 == 38 || v64 == 124 || v64 == 33 || v64 == 41)
                        break;
                    if (v64 == 39 || v64 == 0x22)
                    {
                        v63 += 1;
                        v65 = *((char *)v63);
                        while (true)
                        {
                            if (!v65 || v65 == v64)
                                break;
                            v63 += 1;
                            v65 = *((char *)v63);
                        }
                        if (!v66)
                            break;
                    }
                    v67 = v63 + 1;
                    v61 = *((char *)v67);
                    v62 = v67;
                }
                v2 = *((int *)v63);
                v0 = v63;
                *((char *)v63) = 0;
                v68 = v24;
                if ((char)v68 == 63 || v68 == 0x3d3d || v68 == 15649)
                {
                    sub_10030225(v60);
                    if (!(char)v31)
                        v31 = 48;
                    if (v17)
                    {
                        v69 = &v31;
                        while (true)
                        {
                            v70 = *(v69);
                            if (!*(v69))
                                break;
                            if (v70 != 32 && (v70 < 48 || v70 > 57))
                            {
                                v17 = 0;
                                break;
                            }
                            else
                            {
                                v69 += 1;
                            }
                        }
                    }
                }
                v71 = sub_100300ce();
                v72 = v24;
                if ((char)v72 == 42)
                {
                    v71 = v71 * len;
                }
                else
                {
                    if ((char)v72 == 47)
                    {
                        v73 = v71;
                        v71 = (!v73 ? NULL : len / v73);
                    }
                    else
                    {
                        if ((char)v72 == 43)
                        {
                            v71 += len;
                        }
                        else
                        {
                            if ((char)v72 == 45)
                            {
                                v71 -= len;
                            }
                            else
                            {
                                if ((char)v72 == 37)
                                {
                                    v74 = v71;
                                    v71 = (!v74 ? NULL : len % v74);
                                }
                                else
                                {
                                    if (v72 == 0x3d3d)
                                    {
                                        if (v17)
                                            v71 = (v71 == len ? 0x1 : NULL);
                                        else
                                            v71 = (!lstrcmpi(&v33, &v31) ? 0x1 : 0);
                                    }
                                    else
                                    {
                                        if (v72 == 15678)
                                        {
                                            v71 = (len < v71 ? NULL : 0x1);
                                        }
                                        else
                                        {
                                            if (v72 == 15676)
                                            {
                                                v71 = (len <= v71 ? 0x1 : NULL);
                                            }
                                            else
                                            {
                                                if (v72 == 15649)
                                                {
                                                    if (v17)
                                                    {
                                                        v71 = (v71 == len ? NULL : 0x1);
                                                    }
                                                    else
                                                    {
                                                        v71 = lstrcmpi(&v33, &v31);
                                                        if (v71)
                                                            v71 = 0x1;
                                                    }
                                                }
                                                else
                                                {
                                                    if ((char)v72 == 63)
                                                    {
                                                        if (!(char)v31)
                                                        {
                                                            v71 = NULL;
                                                        }
                                                        else
                                                        {
                                                            sub_1002ff87();
                                                            sub_1002ff87();
                                                            len = lstrlen(&v31);
                                                            v75 = &v33;
                                                            v71 = NULL;
                                                            while (true)
                                                            {
                                                                v76 = *(v75);
                                                                if (!*(v75))
                                                                    break;
                                                                v77 = v75;
                                                                v78 = len;
                                                                do
                                                                {
                                                                    if (!v78)
                                                                        break;
                                                                } while (*(v77) == (char)v31);
                                                                if (!v76)
                                                                {
                                                                    v71 = -(&v32) + v75;
                                                                    break;
                                                                }
                                                                else
                                                                {
                                                                    v75 += 1;
                                                                }
                                                            }
                                                        }
                                                    }
                                                    else
                                                    {
                                                        if ((char)v72 == 60)
                                                        {
                                                            v71 = (len < v71 ? 0x1 : NULL);
                                                        }
                                                        else
                                                        {
                                                            if ((char)v72 == 62)
                                                            {
                                                                v71 = (len <= v71 ? NULL : 0x1);
                                                            }
                                                            else
                                                            {
                                                                if (v72 == 0x2626)
                                                                {
                                                                    if (len && v71)
                                                                        v71 = 0x1;
                                                                    else
                                                                        v71 = NULL;
                                                                }
                                                                else
                                                                {
                                                                    if (v72 == 0x7c7c)
                                                                    {
                                                                        if (len || v71)
                                                                            v71 = 0x1;
                                                                        else
                                                                            v71 = NULL;
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
                v79 = v63;
                *((int *)v79) = *((int *)v63);
                v2 = v71;
                lstrcpy(&v34, v79);
                sub_10040940(v71, v26);
                lstrcat(v26, &v34);
                v17 = v17;
                v31 = v31;
            }
            v80 = &v36;
            if (v27)
            {
                sub_10030225();
                v80 = &v33;
            }
            lstrcpy(&v34, v28);
            lstrcpy(v29, v80);
            lstrcat(v29, &v34);
            if (v27)
            {
                v46 = &v29[lstrlen(v29)];
            }
            else
            {
                sub_10030225();
                for (; *((char *)k); k += 1);
                for (; (char)k[1] == 32; k -= 1);
                *((char *)k) = 0;
                return;
            }
        }
    }
    else if (v41 == 36)
    {
        v6 = v81;
        node = &node[1];
        k = v83;
        v84 = &v37;
        v39 = &v37;
        v14 = NULL;
        v15 = NULL;
        v13 = NULL;
        v11 = NULL;
        v9 = 0;
        v12 = 0;
        v10 = 0;
        v8 = 0;
        v7 = NULL;
        v85 = node[0];
        while (true)
        {
            v86 = v85;
            if (v86 == 32 || !((v87 = v85, v86 = v87, v85 && (v86 = v87, v87 != 39 && (v86 = v87, v87 != 0x22 && (v87 != 36 || !((v86 = v87, node[1] != 46))))))))
                break;
            v84[0] = v87;
            v84 = &v84[1];
            for (node = &node[1]; node[0] == 46; node = &node[1])
            {
                v88 = &v84[1];
                if (!v14)
                {
                    v15 = v88;
                    v5 = v88;
                    v14 = &v33;
                    lstrcpy(&v33, &node[1]);
                    v7 = node;
                }
                else if (!v13)
                {
                    v13 = v88;
                    v12 = &v33 + node - (char *)v7;
                }
                else if (!v11)
                {
                    v11 = v88;
                    v10 = &v33 + node - (char *)v7;
                }
                else
                {
                    v9 = v88;
                    v8 = &v33 + node - (char *)v7;
                }
                idx = &v88[1];
                idx[0] = 0;
                if (node[1] == 91)
                {
                    len = 93;
                    idx[1] = 91;
                }
                else if (node[1] == 0x22)
                {
                    len = 0x22;
                    idx[1] = 0x22;
                }
                else if (node[1] == 39)
                {
                    len = 39;
                    idx[1] = 39;
                }
                else
                {
                    node = &node[1];
                    v84 = &idx[1];
                    break;
                }
                node = &node[2];
                v84 = &idx[2];
                while (true)
                {
                    v90 = node[0];
                    if (node[0] == len)
                        break;
                    if (!v90)
                        goto LABEL_1002cae0;
                    v84[0] = v90;
                    node = &node[1];
                    v84 = &v84[1];
                }
                v84[0] = v90;
                v84 = &v84[1];
            }
LABEL_1002cae0:
            v85 = node[0];
        }
        if (v7)
        {
            v94 = _ccall(v91, v92, (unsigned int)v93, &v33 + node - v7 - 1);
            *((char *)v94) = 0;
        }
        if (v86 == 36)
            node = &node[1];
        v84[0] = 0;
        if (!v14)
            v14 = v84;
        if (!g_10292303)
        {
            v5 = node;
            sub_1002c1b6("name", sub_1002e460);
            sub_1002c1b6("id", sub_1002e473);
            sub_1002c1b6("posx", sub_1002e48c);
            sub_1002c1b6("distance", sub_1002e4a6);
            sub_1002c1b6("distx", sub_1002e4df);
            sub_1002c1b6("disty", sub_1002e504);
            sub_1002c1b6("posy", sub_1002e529);
            sub_1002c1b6("posz", sub_1002e543);
            sub_1002c1b6("dir", sub_1002e55d);
            sub_1002c1b6("outfit", sub_1002e577);
            sub_1002c1b6("hppc", sub_1002e591);
            sub_1002c1b6("speed", sub_1002e5ae);
            sub_1002c1b6("isparalyzed", sub_1002e5cb);
            sub_1002c1b6("color1", sub_1002e5eb);
            sub_1002c1b6("color2", sub_1002e605);
            sub_1002c1b6("color3", sub_1002e61f);
            sub_1002c1b6("color4", sub_1002e639);
            sub_1002c1b6("skull", sub_1002e653);
            sub_1002c1b6("party", sub_1002e670);
            sub_1002c1b6("warbanner", sub_1002e68d);
            sub_1002c1b6("ismonster", sub_1002e6aa);
            sub_1002c1b6("isnpc", sub_1002e6c4);
            sub_1002c1b6("isplayer", sub_1002e6ed);
            sub_1002c1b6("isonscreen", sub_1002e707);
            sub_1002c1b6("isshootable", sub_1002e725);
            sub_1002c1b6("canshoot", sub_1002e757);
            sub_1002c1b6("isenemy", sub_1002e7b4);
            sub_1002c1b6("isonnavi", sub_1002e7d5);
            sub_1002c1b6("isleader", sub_1002e7f4);
            sub_1002c1b6("isfriend", sub_1002e815);
            sub_1002c1b6("issubenemy", sub_1002e836);
            sub_1002c1b6("issubfriend", sub_1002e857);
            sub_1002c1b6("haslookinfo", sub_1002e878);
            sub_1002c1b6("guild", sub_1002e89f);
            sub_1002c1b6("voc", sub_1002e8b9);
            sub_1002c1b6("vocation", sub_1002e8d7);
            sub_1002c1b6("level", sub_1002e8f8);
            sub_1002c1b6("isknight", sub_1002e911);
            sub_1002c1b6("ispaladin", sub_1002e938);
            sub_1002c1b6("issorcerer", sub_1002e95f);
            sub_1002c1b6("isdruid", sub_1002e986);
            sub_1002c1b6("ismage", sub_1002e9ad);
            sub_1002c1b6("maxhp", sub_1002e9df);
            sub_1002c1b6("hp", sub_1002e9fa);
            sub_1002c1b6("maxmp", sub_1002ea15);
            sub_1002c1b6("mp", sub_1002ea4a);
            sub_1002c1b6("attackedme", sub_1002ea85);
            sub_1002c1b6("exposedcount", sub_1002eaa9);
            sub_1002c1b6("shotcount", sub_1002eaca);
            sub_1002c1b6("mp", sub_1002cb8e);
            sub_1002c1b6("maxmp", sub_1002cba2);
            sub_1002c1b6("hp", sub_1002cbb6);
            sub_1002c1b6("mppc", sub_1002cbca);
            sub_1002c1b6("hppc", sub_1002cbf7);
            sub_1002c1b6("maxhp", sub_1002cc24);
            sub_1002c1b6("cap", sub_1002cc38);
            sub_1002c1b6("exp", sub_1002cc56);
            sub_1002c1b6("level", sub_1002cc6a);
            sub_1002c1b6("mlevel", sub_1002cc7e);
            sub_1002c1b6("posx", sub_1002cc92);
            sub_1002c1b6("posy", sub_1002cca6);
            sub_1002c1b6("posz", sub_1002ccba);
            sub_1002c1b6("soul", sub_1002ccce);
            sub_1002c1b6("stamina", sub_1002cce2);
            sub_1002c1b6("count", sub_1002ccf6);
            sub_1002c1b6("screenleft", sub_1002cd09);
            sub_1002c1b6("screenright", sub_1002cd2e);
            sub_1002c1b6("screentop", sub_1002cd56);
            sub_1002c1b6("screenbottom", sub_1002cd7b);
            sub_1002c1b6("name", sub_1002cda3);
            sub_1002c1b6("time", sub_1002cdbe);
            sub_1002c1b6("timems", sub_1002cdda);
            sub_1002c1b6("deltatime", sub_1002cded);
            sub_1002c1b6("deltatimems", sub_1002ce0f);
            sub_1002c1b6("return", sub_1002ce28);
            sub_1002c1b6("exptnl", sub_1002ce3a);
            sub_1002c1b6("exph", sub_1002ce5e);
            sub_1002c1b6("expgained", sub_1002ce71);
            sub_1002c1b6("timetnl", sub_1002ce98);
            sub_1002c1b6("exptolevel", sub_1002cef8);
            sub_1002c1b6("timetolevel", sub_1002cf2c);
            sub_1002c1b6("monstersaround", sub_1002d234);
            sub_1002c1b6("screencount", sub_1002cf9c);
            sub_1002c1b6("mcount", sub_1002d010);
            sub_1002c1b6("playersaround", sub_1002d2c0);
            sub_1002c1b6("pcount", sub_1002d122);
            sub_1002c1b6("isleader", sub_1002d354);
            sub_1002c1b6("isfriend", sub_1002d389);
            sub_1002c1b6("issubfriend", sub_1002d3be);
            sub_1002c1b6("isenemy", sub_1002d3f3);
            sub_1002c1b6("issubenemy", sub_1002d428);
            sub_1002c1b6("sbtime", sub_1002d45d);
            sub_1002c1b6("sstime", sub_1002d479);
            sub_1002c1b6("exectime", sub_1002d495);
            sub_1002c1b6("synctime", sub_1002d4a8);
            sub_1002c1b6("fired", sub_1002d4c0);
            sub_1002c1b6("formattime", sub_1002d4d3);
            sub_1002c1b6("formatnum", sub_1002d536);
            sub_1002c1b6("ringslot", sub_1002d550);
            sub_1002c1b6("beltslot", sub_1002d570);
            sub_1002c1b6("backslot", sub_1002d590);
            sub_1002c1b6("rhandslot", sub_1002d5b0);
            sub_1002c1b6("lhandslot", sub_1002d5d0);
            sub_1002c1b6("amuletslot", sub_1002d5f0);
            sub_1002c1b6("bootsslot", sub_1002d610);
            sub_1002c1b6("headslot", sub_1002d630);
            sub_1002c1b6("chestslot", sub_1002d650);
            sub_1002c1b6("legsslot", sub_1002d670);
            sub_1002c1b6("topitem", sub_1002d690);
            sub_1002c1b6("istileitem", sub_1002d6f3);
            sub_1002c1b6("poisoned", sub_1002d77f);
            sub_1002c1b6("poisondmg", sub_1002d798);
            sub_1002c1b6("manashielded", sub_1002d7ba);
            sub_1002c1b6("battlesign", sub_1002d7d3);
            sub_1002c1b6("redbattlesign", sub_1002d7ec);
            sub_1002c1b6("drunk", sub_1002d805);
            sub_1002c1b6("hasted", sub_1002d81e);
            sub_1002c1b6("paralyzed", sub_1002d837);
            sub_1002c1b6("inpz", sub_1002d850);
            sub_1002c1b6("navion", sub_1002d869);
            sub_1002c1b6("itemcount", sub_1002d882);
            sub_1002c1b6("winitemcount", sub_1002d8d5);
            sub_1002c1b6("fileisline", sub_1002d92b);
            sub_1002c1b6("rand", sub_1002d984);
            sub_1002c1b6("fileline", sub_1002d9db);
            sub_1002c1b6("token", sub_1002da13);
            sub_1002c1b6("filerandomline", sub_1002dae0);
            sub_1002c1b6("connected", sub_1002daff);
            sub_1002c1b6("pkname", sub_1002db22);
            sub_1002c1b6("ping", sub_1002db34);
            sub_1002c1b6("fps", sub_1002db47);
            sub_1002c1b6("enemycount", sub_1002db6e);
            sub_1002c1b6("friendcount", sub_1002dbc8);
            sub_1002c1b6("fishspots", sub_1002dc22);
            sub_1002c1b6("waypointson", sub_1002dc3c);
            sub_1002c1b6("caveboton", sub_1002dc3c);
            sub_1002c1b6("targetingon", sub_1002dc51);
            sub_1002c1b6("autocomboon", sub_1002dc66);
            sub_1002c1b6("mshieldtime", sub_1002dc7b);
            sub_1002c1b6("hastetime", sub_1002dc95);
            sub_1002c1b6("strengthtime", sub_1002dcaf);
            sub_1002c1b6("invistime", sub_1002dcc9);
            sub_1002c1b6("invisible", sub_1002dce3);
            sub_1002c1b6("dmgs", sub_1002dd05);
            sub_1002c1b6("lastdmg", sub_1002dd18);
            sub_1002c1b6("lastdmgtype", sub_1002dd2b);
            sub_1002c1b6("idlerecvtime", sub_1002dd3e);
            sub_1002c1b6("standtime", sub_1002dd57);
            sub_1002c1b6("lastdmgtime", sub_1002dd70);
            sub_1002c1b6("islooting", sub_1002dd94);
            sub_1002c1b6("lastdmgername", sub_1002ddb2);
            sub_1002c1b6("squaretime", sub_1002ddc6);
            sub_1002c1b6("systime", L"h\x01\uff00\uf875\ue868օ樐樀栀Ѐ");
            sub_1002c1b6("sysdate", L"h\x01\uff00\uf875\uf868օ樐樀栀Ѐ");
            sub_1002c1b6("cutstr", sub_1002de19);
            sub_1002c1b6("creature", sub_1002deab);
            sub_1002c1b6("mostexposed", sub_1002deeb);
            sub_1002c1b6("mostexposedcount", sub_1002df1f);
            sub_1002c1b6("mostshot", sub_1002df55);
            sub_1002c1b6("mostshotcount", sub_1002df89);
            sub_1002c1b6("lastmsg", sub_1002e175);
            sub_1002c1b6("lastnavmsg", sub_1002e180);
            sub_1002c1b6("curmsg", sub_1002e18b);
            sub_1002c1b6("target", sub_1002e1fd);
            sub_1002c1b6("lastdmger", sub_1002e226);
            sub_1002c1b6("self", sub_1002e24a);
            sub_1002c1b6("followed", sub_1002e255);
            sub_1002c1b6("attacked", sub_1002e27c);
            sub_1002c1b6("pk", sub_1002e2a2);
            sub_1002c1b6("pattacker", sub_1002e2b4);
            sub_1002c1b6("mattacker", sub_1002e2c5);
            sub_1002c1b6("attacker", sub_1002e2d6);
            sub_1002c1b6("enemy", "Sj");
            sub_1002c1b6("friend", "Sj");
            sub_1002c1b6("subenemy", "Sj");
            sub_1002c1b6("subfriend", "Sj");
            sub_1002c1b6("anyenemy", "Sj");
            sub_1002c1b6("anyfriend", "Sj");
            sub_1002c1b6("coretarget", sub_1002e353);
            sub_1002c1b6("triggertarget", "Sj");
            sub_1002c1b6("autoaimtarget", "Sj");
            sub_1002c1b6("ctrl", sub_1002dfbf);
            sub_1002c1b6("alt", sub_1002dff5);
            sub_1002c1b6("shift", sub_1002dfda);
            sub_1002c1b6("key", sub_1002e010);
            sub_1002c1b6("skill", sub_1002e03b);
            sub_1002c1b6("skillpc", sub_1002e07d);
            sub_1002c1b6("skilltime", sub_1002e0cd);
            g_10292303 = 1;
        }
        sub_1002ff87(v39);
        v95 = 0;
        i = 0;
        v97 = v39;
        do
        {
            i = _INSERT(i, 0, *(v97));
            v95 = v95 * 5 + i;
            v97 += 1;
        } while (i);
        v99 = v95 & 0x3fff;
        if ((&g_102b2404.field_0)[2 * v99])
        {
            v5 = (&g_102b2404.field_0)[1 + 2 * v99];
            if (!lstrcmp((&g_102b2404.field_0)[2 * v99], v39))
                goto (&g_102b2404.field_0)[1 + 2 * v99];
        }
        v5 = node;
        v100 = g_100f49d1;
        v101 = g_100f49d1[0x1ff].padding_1;
        while (true)
        {
            if (v100 >= v101)
                return;
            if (!v100[0])
            {
                *((char *)k) = 0;
                return;
            }
            v4 = v101;
            if (!lstrcmpi(v100, v39))
                break;
            v100 = &v100[0x200];
        }
        if (v14[0] && v100[32] >= 48 && v100[32] <= 57)
        {
            v102 = sub_10040900(&v100[32]);
            if (v102 >= 0x63fef8 && v102 < 0x64a308)
            {
                if (!v14[0])
                {
                    v3 = v102;
                    wsprintfA(k, "%d");
                    return;
                }
                sub_1002ff87(v15);
                v103 = 0;
                j = 0;
                v105 = v15;
                do
                {
                    j = _INSERT(j, 0, v105[0]);
                    v103 = v103 * 5 + j;
                    v105 = &v105[1];
                } while (j);
                v107 = v103 & 0x1fff;
                if ((&g_102d2504.field_0)[2 * v107])
                {
                    v3 = (&g_102d2504.field_0)[1 + 2 * v107];
                    if (!lstrcmp((&g_102d2504.field_0)[2 * v107], v15))
                        goto (&g_102d2504.field_0)[1 + 2 * v107];
                }
                *((char *)k) = 0;
                return;
            }
            if (v102 >= *((int *)&g_100f49ed) && v102 < *((int *)&g_100f49ed) + 632000)
            {
                v108 = v102;
                if (!lstrcmpi(v14, "sender"))
                {
                    lstrcpy(k, v108);
                    return;
                }
                else if (!lstrcmpi(v14, "content"))
                {
                    lstrcpy(k, &v108->padding_1[31]);
                    return;
                }
                else if (!lstrcmpi(v14, "formatted"))
                {
                    if (v108->field_0)
                    {
                        if (v108->field_124)
                        {
                            v3 = &v108->padding_1[31];
                            v2 = v108->field_124;
                            v0 = v108;
                            wsprintfA(k, "%s [%d]: %s");
                        }
                        else
                        {
                            v3 = &v108->padding_1[31];
                            v2 = v108;
                            wsprintfA(k, "%s: %s");
                        }
                    }
                    else
                    {
                        lstrcpy(k, &v108->padding_1[31]);
                    }
                    return;
                }
                else if (!lstrcmpi(v14, "level"))
                {
                    v3 = k;
                    *((unsigned int *)&(&v1)[2]) = 0;
                    *((unsigned short *)&v1) = v108->field_124;
                    sub_10040940(*((unsigned int *)&v1));
                    return;
                }
                else if (!lstrcmpi(v14, "isdefault"))
                {
                    v109 = k;
                    *(v109) = 48;
                    if (v108->field_126 != 1)
                        return;
                    *(v109) = 49;
                    return;
                }
                else if (!lstrcmpi(v14, "isyell"))
                {
                    v110 = k;
                    *(v110) = 48;
                    if (v108->field_126 != 3)
                        return;
                    *(v110) = 49;
                    return;
                }
                else if (!lstrcmpi(v14, "iswhisper"))
                {
                    v111 = k;
                    *(v111) = 48;
                    if (v108->field_126 != 2)
                        return;
                    *(v111) = 49;
                    return;
                }
                else if (!lstrcmpi(v14, "isprivate"))
                {
                    v112 = k;
                    *(v112) = 48;
                    if (v108->field_126 != 6)
                        return;
                    *(v112) = 49;
                    return;
                }
                else if (!lstrcmpi(v14, "isbroadcast"))
                {
                    v113 = k;
                    *(v113) = 48;
                    if (v108->field_126 == 12 || v108->field_126 == 14 || v108->field_126 == 65533)
                        *(v113) = 49;
                    return;
                }
                else if (!lstrcmpi(v14, "isredtext"))
                {
                    v114 = k;
                    *(v114) = 48;
                    if (v108->field_126 == 12 || v108->field_126 == 13 || v108->field_126 == 14 || v108->field_126 == 0x11 || v108->field_126 == 65533)
                        *(v114) = 49;
                    return;
                }
                else if (!lstrcmpi(v14, "isorangetext"))
                {
                    v115 = k;
                    *(v115) = 48;
                    if (v108->field_126 != 15)
                        return;
                    *(v115) = 49;
                    return;
                }
                else if (!lstrcmpi(v14, "isnpc"))
                {
                    v116 = k;
                    *(v116) = 48;
                    if (v108->field_126 != 5)
                        return;
                    *(v116) = 49;
                    return;
                }
                else if (!lstrcmpi(v14, "ischannel"))
                {
                    v117 = k;
                    *(v117) = 0;
                    if ((char)v108->field_126 != 7 && (char)v108->field_126 != 8 && (char)v108->field_126 != 13 && (char)v108->field_126 != 15 && (char)v108->field_126 != 0x11 || !v108->field_128)
                        return;
                    *(v117) = 49;
                    return;
                }
                else if (!lstrcmpi(v14, "isbotlook"))
                {
                    v119 = k;
                    *(v119) = 0;
                    if (!v108->field_12c)
                        return;
                    *(v119) = 49;
                    return;
                }
                else if (!lstrcmpi(v14, "isguild"))
                {
                    v120 = k;
                    *(v120) = 48;
                    if ((char)v108->field_126 != 7 && (char)v108->field_126 != 13 && (char)v108->field_126 != 15 || v108->field_128)
                        return;
                    *(v120) = 49;
                    return;
                }
                else if (!lstrcmpi(v14, "istrade"))
                {
                    v122 = k;
                    *(v122) = 48;
                    if (((char)v108->field_126 == 7 || (char)v108->field_126 == 14 || (char)v108->field_126 == 15) && (v108->field_128 == 5 || v108->field_128 == 5))
                        *(v122) = 49;
                    return;
                }
                else if (!lstrcmpi(v14, "isrl"))
                {
                    v124 = k;
                    *(v124) = 48;
                    if ((char)v108->field_126 != 7 && (char)v108->field_126 != 13 && (char)v108->field_126 != 15 || v108->field_128 != 7)
                        return;
                    *(v124) = 49;
                    return;
                }
                else if (!lstrcmpi(v14, "isgame"))
                {
                    v126 = k;
                    *(v126) = 48;
                    if ((char)v108->field_126 != 7 && (char)v108->field_126 != 13 && (char)v108->field_126 != 15 || v108->field_128 != 4)
                        return;
                    *(v126) = 49;
                    return;
                }
                else if (!lstrcmpi(v14, "ishelp"))
                {
                    v128 = k;
                    *(v128) = 48;
                    if ((char)v108->field_126 != 7 && (char)v108->field_126 != 13 && (char)v108->field_126 != 15 || v108->field_128 != 8)
                        return;
                    *(v128) = 49;
                    return;
                }
                else if (!lstrcmpi(v14, "isaction"))
                {
                    v130 = k;
                    *(v130) = 48;
                    if (v108->field_126 != 19)
                        return;
                    *(v130) = 49;
                    return;
                }
                else if (!lstrcmpi(v14, "isstatus"))
                {
                    v131 = k;
                    *(v131) = 48;
                    if (v108->field_126 != 65535)
                        return;
                    *(v131) = 49;
                    return;
                }
                else if (!lstrcmpi(v14, "isinfo"))
                {
                    v132 = k;
                    *(v132) = 48;
                    if (v108->field_126 != 65534)
                        return;
                    *(v132) = 49;
                    return;
                }
                else if (!lstrcmpi(v14, "isnavi"))
                {
                    v133 = k;
                    *(v133) = 48;
                    if (v108->field_126 != 65529)
                        return;
                    *(v133) = 49;
                    return;
                }
                else if (!lstrcmpi(v14, "channel"))
                {
                    v134 = v108->field_126;
                    if (v134 == 1)
                    {
                        lstrcpy(k, "Default");
                        return;
                    }
                    if (v134 == 2)
                    {
                        lstrcpy(k, "Whisper");
                        return;
                    }
                    if (v134 == 3)
                    {
                        lstrcpy(k, "Yell");
                        return;
                    }
                    if (v134 == 5)
                    {
                        lstrcpy(k, "NPC");
                        return;
                    }
                    if (v134 == 6)
                    {
                        lstrcpy(k, "Private");
                        return;
                    }
                    if ((v134 == 7 || v134 == 13 || v134 == 15) && !v108->field_128)
                    {
                        lstrcpy(k, "Guild");
                        return;
                    }
                    if (v134 != 12 && v134 != 14)
                    {
                        if (v134 == 19)
                        {
                            lstrcpy(k, "Action");
                            return;
                        }
                        if (v134 == 255)
                        {
                            lstrcpy(k, "Status");
                            return;
                        }
                        if (v134 == 254)
                        {
                            lstrcpy(k, "Info");
                            return;
                        }
                        if (v134 == 249)
                        {
                            lstrcpy(k, "Navi");
                            return;
                        }
                        *((char *)k) = 0;
                        index = 0;
                        v136 = g_100f9109.field_0;
                        while (true)
                        {
                            v137 = v136;
                            if (!v136)
                                break;
                            if (v137->field_24 && v108->field_128 == *((int *)(v137->field_24 + 44)))
                            {
                                lstrcpy(k, v137->field_2c);
                                break;
                            }
                            else
                            {
                                index += 1;
                                v136 = (&g_100f9109.field_0)[index];
                            }
                        }
                        return;
                    }
                    lstrcpy(k, "Broadcast");
                    return;
                }
                else if (!lstrcmpi(v14, "color"))
                {
                    v138 = v108->field_126;
                    if (v108->field_126 <= 3)
                    {
                        v3 = 16838639;
                        wsprintfA(k, "%d");
                        return;
                    }
                    else if (v108->field_126 == 5)
                    {
                        v3 = 0x1fe9f9f;
                        wsprintfA(k, "%d");
                        return;
                    }
                    else if (v108->field_126 == 6)
                    {
                        v3 = 33027935;
                        wsprintfA(k, "%d");
                        return;
                    }
                    else
                    {
                        if (v108->field_126 == 7 && !v108->field_128)
                        {
                            v3 = 0x1ff6aff;
                            wsprintfA(k, "%d");
                            return;
                        }
                        if (v138 != 12 && v138 != 13 && v138 != 14 && v138 != 0x11)
                        {
                            if (v138 == 14)
                            {
                                v3 = 16819354;
                                wsprintfA(k, "%d");
                                return;
                            }
                            else if (v108->field_126 == 19)
                            {
                                v3 = 0x10065fe;
                                wsprintfA(k, "%d");
                                return;
                            }
                            else if (v108->field_126 == 65535)
                            {
                                v3 = 0x1ffffff;
                                wsprintfA(k, "%d");
                                return;
                            }
                            else if (v108->field_126 == 65534)
                            {
                                v3 = 0x100ff00;
                                wsprintfA(k, "%d");
                                return;
                            }
                            else if (v108->field_126 == 65529)
                            {
                                v3 = 0x1ffffff;
                                wsprintfA(k, "%d");
                                return;
                            }
                            else
                            {
                                if (v108->field_128 < 10)
                                {
                                    v3 = 31251676;
                                    wsprintfA(k, "%d");
                                }
                                else
                                {
                                    v3 = 28898347;
                                    wsprintfA(k, "%d");
                                }
                                return;
                            }
                        }
                        v3 = 0x15f5ff7;
                        wsprintfA(k, "%d");
                        return;
                    }
                }
                else
                {
                    *((char *)k) = 0;
                    return;
                }
            }
            *((char *)k) = 0;
            return;
        }
        lstrcpy(k, &v100[32]);
        return;
    }
    else
    {
        return;
    }
}
```

## `sub_1002c29f` `0x1002c29f`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002c29f(void)
{
}
```

## `sub_1002c2b8` `0x1002c2b8`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002c2b8(void)
{
}
```

## `sub_1002c74e` `0x1002c74e`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1002c74e(void)
{
}
```

## `sub_1002c77d` `0x1002c77d`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1002c77d(void)
{
}
```

## `sub_1002c7ca` `0x1002c7ca`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1002c7ca(void)
{
}
```

## `sub_1002c803` `0x1002c803`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002c803(void)
{
}
```

## `sub_1002c84e` `0x1002c84e`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002c84e(void)
{
}
```

## `sub_1002c874` `0x1002c874`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002c874(void)
{
}
```

## `sub_1002ca8f` `0x1002ca8f`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002ca8f(void)
{
}
```

## `sub_1002caa4` `0x1002caa4`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002caa4(void)
{
}
```

## `sub_1002cad0` `0x1002cad0`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002cad0(void)
{
}
```

## `sub_1002cadc` `0x1002cadc`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002cadc(void)
{
}
```

## `sub_1002cb8e` `0x1002cb8e`

_25 bytes. (leaf/helper — see body)_

```c
int sub_1002cb8e(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(*(0x63fe78), v1);
    return *((int *)0x63fe78);
}
```

## `sub_1002cba2` `0x1002cba2`

_20 bytes. (leaf/helper — see body)_

```c
void sub_1002cba2(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(*(0x63fe74), v1);
}
```

## `sub_1002cbb6` `0x1002cbb6`

_20 bytes. (leaf/helper — see body)_

```c
void sub_1002cbb6(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(*(0x63fe94), v1);
}
```

## `sub_1002cbca` `0x1002cbca`

_45 bytes. (leaf/helper — see body)_

```c
int sub_1002cbca(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940((!*((int *)0x63fe74) ? 100 : *((int *)0x63fe78) * 100 / *((int *)0x63fe74)), v1);
}
```

## `sub_1002cbf7` `0x1002cbf7`

_45 bytes. (leaf/helper — see body)_

```c
int sub_1002cbf7(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940((!*((int *)0x63fe90) ? 100 : *((int *)0x63fe94) * 100 / *((int *)0x63fe90)), v1);
}
```

## `sub_1002cc24` `0x1002cc24`

_20 bytes. (leaf/helper — see body)_

```c
void sub_1002cc24(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(*(0x63fe90), v1);
}
```

## `sub_1002cc38` `0x1002cc38`

_30 bytes. (leaf/helper — see body)_

```c
int sub_1002cc38(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(*((int *)0x63fe68) / 100, v1);
}
```

## `sub_1002cc56` `0x1002cc56`

_20 bytes. (leaf/helper — see body)_

```c
void sub_1002cc56(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(*(0x63fe8c), v1);
}
```

## `sub_1002cc6a` `0x1002cc6a`

_20 bytes. (leaf/helper — see body)_

```c
void sub_1002cc6a(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(*(0x63fe88), v1);
}
```

## `sub_1002cc7e` `0x1002cc7e`

_20 bytes. (leaf/helper — see body)_

```c
void sub_1002cc7e(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(*(0x63fe84), v1);
}
```

## `sub_1002cc92` `0x1002cc92`

_20 bytes. (leaf/helper — see body)_

```c
void sub_1002cc92(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(*(0x64f608), v1);
}
```

## `sub_1002cca6` `0x1002cca6`

_20 bytes. (leaf/helper — see body)_

```c
void sub_1002cca6(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(*(0x64f604), v1);
}
```

## `sub_1002ccba` `0x1002ccba`

_20 bytes. (leaf/helper — see body)_

```c
void sub_1002ccba(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(*(0x64f600), v1);
}
```

## `sub_1002ccce` `0x1002ccce`

_20 bytes. (leaf/helper — see body)_

```c
void sub_1002ccce(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(*(0x63fe70), v1);
}
```

## `sub_1002cce2` `0x1002cce2`

_20 bytes. (leaf/helper — see body)_

```c
void sub_1002cce2(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(*(0x63fe6c), v1);
}
```

## `sub_1002ccf6` `0x1002ccf6`

_19 bytes. (leaf/helper — see body)_

```c
extern int g_100f0e7c;

void sub_1002ccf6(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(g_100f0e7c, v1);
}
```

