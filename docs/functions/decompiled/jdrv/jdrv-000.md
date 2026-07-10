# elfbot.dll decompiled — jdrv 0x10001000..0x10002d08

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10001000` `0x10001000`

_54 bytes. calls CreateThread_

```c
extern unsigned int g_10042000;

unsigned int sub_10001000(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0x10]
    char v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v0 = a0;
    g_10042000 = a0;
    if (a1 == 1)
        CreateThread(NULL, NULL, sub_10002041, &v1, THREAD_CREATE_RUN_IMMEDIATELY, &v2);
    return 1;
}
```

## `sub_10001036` `0x10001036`

_33 bytes. (leaf/helper — see body)_

```c
int sub_10001036(int a0)
{
    int v2;  // edi
    int v3;  // esi
    int v4;  // ebx
    int v5;  // edx
    int v6;  // ecx
    int v7;  // eax
    Byte v0[32];  // [bp-0x24]
    char v1;  // [bp-0x4]

    sub_10040940(a0, v0, v2, v3, &v1, v0, v4, v5, v6, v7);
    OutputDebugStringA(v0);
    return v5;
}
```

## `sub_10001057` `0x10001057`

_52 bytes. (leaf/helper — see body)_

```c
int sub_10001057(unsigned int a0)
{
    return _INSERT(*((char *)(1 + (a0 - *((int *)*((int *)0x785db4))) * 76 + *((int *)(*((int *)0x785db4) + 8)) + 36)), 0, *((char *)(1 + (a0 - *((int *)*((int *)0x785db4))) * 76 + *((int *)(*((int *)0x785db4) + 8)) + 36)) & 8);
}
```

## `sub_1000108b` `0x1000108b`

_52 bytes. (leaf/helper — see body)_

```c
int sub_1000108b(unsigned int a0)
{
    return _INSERT(*((char *)(1 + (a0 - *((int *)*((int *)0x785db4))) * 76 + *((int *)(*((int *)0x785db4) + 8)) + 36)), 0, *((char *)(1 + (a0 - *((int *)*((int *)0x785db4))) * 76 + *((int *)(*((int *)0x785db4) + 8)) + 36)) & 144);
}
```

## `sub_100010bf` `0x100010bf`

_161 bytes. calls CreateThread_

```c
typedef struct struct_1 {
    char padding_0[12];
    struct struct_2 *field_c;
} struct_1;

typedef struct struct_2 {
    struct struct_0 *field_0;
} struct_2;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern char g_1005a291;
extern unsigned int g_1005a292;
extern unsigned int g_1005a296;
extern unsigned int g_1005db5c;
extern unsigned int g_1005db60;
extern unsigned int g_1005db68;

HANDLE sub_100010bf(char *a0, int a1, unsigned int a2, int a3)
{
    struct_1 *v3;  // eax
    unsigned int v0;  // [bp-0x134]
    char v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    g_1005db68 = GetCurrentProcess();
    v0 = a2;
    g_1005db5c = a2;
    g_1005a296 = sub_10040900(a1);
    g_1005db60 = sub_10040900(a3);
    g_1005a292 = 0;
    if (*(a0))
    {
        if (*(a0) >= 48 && *(a0) <= 57)
        {
            g_1005a292 = inet_addr(a0);
        }
        else
        {
            v3 = gethostbyname(a0);
            if (v3 && v3->field_c->field_0)
                g_1005a292 = v3->field_c->field_0->field_0;
        }
    }
    g_1005a291 = 0;
    return CreateThread(NULL, NULL, sub_10002041, &v1, THREAD_CREATE_RUN_IMMEDIATELY, &v2);
}
```

## `sub_10001160` `0x10001160`

_16 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005db5c;

void sub_10001160(unsigned int a0)
{
    g_1005db5c = a0;
    return;
}
```

## `sub_10001170` `0x10001170`

_178 bytes. calls WriteProcessMemory_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
    char padding_4[8];
    struct struct_1 *field_c;
} struct_0;

typedef struct struct_1 {
    struct struct_0 *field_0;
} struct_1;

extern char g_100420a4;
extern unsigned int g_1005a29a;
extern unsigned int g_1005a29e;
extern unsigned int g_1005d89b;
extern char g_1005db66;
extern HANDLE g_1005db68;

struct_0 * sub_10001170(struct_0 *a0, int a1)
{
    struct_0 *v1;  // eax
    struct_0 *v2;  // eax
    struct_0 *v3;  // eax
    struct_0 *count;  // eax
    unsigned int v0;  // [bp-0x24]

    g_1005db68 = GetCurrentProcess();
    g_1005a29e = sub_10040900(a1);
    v1 = a0;
    g_1005a29a = 0;
    if ((char)v1->field_0)
    {
        if ((char)v1->field_0 >= 48 && (char)v1->field_0 <= 57)
        {
            v1 = inet_addr(a0);
            g_1005a29a = v1;
        }
        else
        {
            v2 = gethostbyname(a0);
            v1 = v2;
            if (v1)
            {
                v3 = v2->field_c->field_0;
                v1 = v3;
                if (v2->field_c->field_0)
                {
                    v1 = v3->field_0;
                    g_1005a29a = v1;
                }
            }
        }
    }
    if (g_1005db66)
        return v1;
    count = 0x571aaf;
    if (*(0x571aaf) == 255)
    {
        g_1005d89b = *((int *)0x571ab1);
        v0 = &g_100420a4;
        count = WriteProcessMemory(g_1005db68, 0x571ab1, &v0, 0x4, NULL);
    }
    g_1005db66 = 1;
    return count;
}
```

## `sub_10001222` `0x10001222`

_76 bytes. (leaf/helper — see body)_

```c
extern char g_1005a291;
extern SOCKET g_1005da3d;
extern unsigned int g_1005da85[4];

SOCKET * sub_10001222(void)
{
    SOCKET *sock;  // eax
    unsigned int i;  // ecx
    SOCKET *v0;  // [bp-0x8]
    unsigned int v1;  // [bp-0x4]

    g_1005a291 = 1;
    sock = closesocket(g_1005da3d);
    for (i = 0; i < 16; i += 1)
    {
        sock = &g_1005da85[i];
        v1 = i;
        if (*(sock))
        {
            v0 = sock;
            shutdown(*(sock), SD_BOTH);
            closesocket(*(v0));
            sock = v0;
            *(sock) = 0;
            sock[16] = 0;
        }
    }
    return sock;
}
```

## `sub_1000126e` `0x1000126e`

_209 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned short field_0;
    unsigned int field_2;
    struct struct_1 *field_6;
} struct_0;

typedef struct struct_1 {
    unsigned short field_0;
} struct_1;

extern unsigned int g_1005d48f;
extern unsigned int g_1005d877;

void* sub_1000126e(unsigned short *a0)
{
    struct_0 *idx;  // ebx
    int len;  // eax
    void* idx1;  // ebx
    unsigned short v5;  // cx
    void* iter;  // ebx
    void* idx2;  // [bp-0x8]

    idx->field_0 = 97;
    *((unsigned int *)&(&idx->field_0)[1]) = 0;
    *((unsigned short **)((char *)&idx->field_2 + 2)) = a0;
    (&g_1005d48f)[g_1005d877] = a0;
    g_1005d877 = g_1005d877 + 1;
    idx2 = sub_1003997e(a0, (char *)&idx->field_6 + 2);
    len = lstrlen(idx2 + 4);
    *(a0) = len;
    idx1 = 2 + (char *)a0 + len;
    sub_1002ae6f(a0 + 1, idx2 + 4, len);
    *((char *)idx1) = (char)idx2[0x88];
    *((char *)&idx1[1]) = (char)idx2[80];
    v5 = (short)idx2[96];
    *((unsigned short *)&idx1[2]) = v5;
    iter = idx1 + 1;
    if (v5)
    {
        *((char *)&iter[3]) = (char)idx2[100];
        *((char *)&iter[4]) = (char)idx2[104];
        *((char *)&iter[5]) = (char)idx2[108];
        *((char *)&iter[6]) = (char)idx2[112];
        *((char *)&iter[7]) = (char)idx2[116];
    }
    else
    {
        *((short *)&iter[3]) = (short)idx2[100];
        iter -= 3;
    }
    *((char *)&iter[8]) = (char)idx2[120];
    *((char *)&iter[9]) = (char)idx2[124];
    *((short *)&iter[10]) = (short)idx2[140];
    *((char *)&iter[12]) = (char)idx2[148];
    *((char *)&iter[13]) = (char)idx2[152];
    return idx2;
}
```

## `sub_1000133f` `0x1000133f`

_524 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    char field_c;
} struct_0;

extern unsigned int g_1005d47b;
extern unsigned int g_1005d47f;
extern unsigned int g_1005d483;
extern unsigned int g_1005d487;
extern unsigned int g_1005d48f;
extern unsigned int g_1005d877;
extern unsigned int g_1005d88b;

unsigned int sub_1000133f(void)
{
    void* v15;  // ebx
    unsigned int v16;  // ebx
    void* v22;  // ebx
    unsigned int v23;  // edx
    unsigned int v24;  // ecx
    void* iter;  // ebx
    unsigned int i;  // eax
    struct_0 *v18;  // eax
    unsigned int l;  // ecx
    struct_0 *node;  // eax
    void* v21;  // ebx
    struct_0 *v0;  // [bp-0x54]
    void* v1;  // [bp-0x50]
    struct_0 *v2;  // [bp-0x4c]
    int v3;  // [bp-0x48], Other Possible Types: unsigned int
    unsigned int v4;  // [bp-0x38]
    unsigned int v5;  // [bp-0x2c]
    unsigned int v6;  // [bp-0x28]
    unsigned int v7;  // [bp-0x24]
    unsigned int v8;  // [bp-0x20]
    unsigned int v9;  // [bp-0x1c]
    void* v10;  // [bp-0x14]
    unsigned int v11;  // [bp-0x10]
    int iter1;  // [bp-0xc]
    int j;  // [bp-0x8]

    v9 = 4294967295;
    g_1005d877 = 0;
    v10 = v15;
    g_1005d487 = 0;
    if (g_1005d88b > 7)
    {
        v8 = g_1005d88b - 2;
        v16 = v8 + 4;
        if (v16 > 15)
            v16 = 15;
        v7 = v16;
        v6 = 1;
    }
    else
    {
        v8 = 7;
        v7 = 0;
        v6 = 4294967295;
    }
    v5 = v8;
    v11 = v5;
    for (i = v7 + v6; v11 != i; i = v4)
    {
        v4 = i;
        for (j = 0; j < 18; j += 1)
        {
            iter1 = 0;
            while (iter1 < 14)
            {
                v18 = sub_1003a176(j, iter1, (g_1005d88b <= 7 ? 7 - v11 : g_1005d88b - v11 + 2));
                if (v18)
                {
                    l = v18->field_0;
                    node = &v18->field_4;
                    if (!g_1005d487 && g_1005d88b == v11 && !j && !iter1)
                    {
                        g_1005d487 = 1;
                        v3 = j;
                        g_1005d47b = v3;
                        v3 = iter1;
                        g_1005d47f = v3;
                        v3 = v11;
                        g_1005d483 = v3;
                        while (true)
                        {
                            if (!l)
                                break;
                            v3 = l;
                            if (node->field_0 == 99)
                            {
                                v2 = node;
                                (&g_1005d48f)[g_1005d877] = node->field_4;
                                g_1005d877 = g_1005d877 + 1;
                                node = v2;
                            }
                            node = &node->field_c;
                            l = v3 - 1;
                        }
                    }
                    if (l)
                    {
                        if (v9 != 4294967295)
                        {
                            v21 = v10;
                            *((char *)v21) = v9;
                            *((char *)&v21[1]) = 255;
                            v10 = v21 + 2;
                        }
                        v9 = 0;
                    }
                    else
                    {
                        v9 += 1;
                        if (v9 == 0xff)
                        {
                            v22 = v10;
                            *((unsigned short *)v22) = 65535;
                            v10 = v22 + 2;
                            v9 = 4294967295;
                        }
                    }
                    for (; l; l = v3 - 1)
                    {
                        v3 = l;
                        v23 = node->field_0;
                        v24 = node->field_4;
                        iter = v10;
                        v2 = node;
                        if (v23 == 99)
                        {
                            sub_1000126e(v24);
                        }
                        else if (v24)
                        {
                            *((unsigned short *)iter) = v23;
                            *((char *)&iter[2]) = v24;
                            iter += 3;
                        }
                        else
                        {
                            *((unsigned short *)iter) = v23;
                            v1 = iter + 2;
                            v0 = node;
                            iter = v1;
                            if (sub_10001057(v23))
                            {
                                *((char *)iter) = v0->field_8;
                                iter += 1;
                            }
                        }
                        v10 = iter;
                        node = &v2->field_c;
                    }
                    iter1 += 1;
                }
                else
                {
                    iter1 += 1;
                }
            }
        }
        v11 += v6;
    }
    if (v9 != 4294967295)
    {
        i = _INSERT(i, 0, v9);
        *((char *)v10) = v9;
        *((char *)&v10[1]) = 255;
    }
    return i;
}
```

## `sub_1000154b` `0x1000154b`

_83 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    char field_8;
} struct_0;

typedef struct struct_1 {
    char field_0;
    char field_1;
    unsigned short field_2;
    char field_4;
} struct_1;

struct_0 * sub_1000154b(void)
{
    unsigned int i;  // ecx
    struct_0 *v5;  // eax
    struct_1 *iter;  // ebx
    unsigned int v7;  // edx
    unsigned int v8;  // esi
    struct_1 *v9;  // ebx
    struct_0 *v0;  // [bp-0xc]
    struct_1 *v1;  // [bp-0x8]
    unsigned int v2;  // [bp-0x4]

    i = 1;
    while (i <= 10)
    {
        v5 = i * 12 + 6525284;
        v7 = v5->field_4;
        v8 = v5->field_0;
        if (v5->field_0)
        {
            v2 = i;
            iter->field_0 = 120;
            iter->field_1 = i;
            iter->field_2 = v8;
            v9 = &iter->field_2;
            if (v7)
            {
                *((char *)&v9->field_2) = v7;
                iter = (char *)&v9->field_2 + 1;
            }
            else
            {
                v1 = &v9->field_2;
                v0 = v5;
                iter = v1;
                v5 = sub_10001057(v8);
                if (v5)
                {
                    v5 = _INSERT(v5, 0, v0->field_8);
                    iter->field_0 = v0->field_8;
                    iter = &iter->field_1;
                }
            }
            i = v2 + 1;
        }
        else
        {
            i += 1;
        }
    }
    return v5;
}
```

## `sub_1000159e` `0x1000159e`

_362 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    char field_c;
} struct_0;

typedef struct struct_1 {
    char field_0[3];
    char field_1[2];
    char field_2;
    unsigned short field_3;
    char field_5;
    char padding_6[1];
    unsigned short field_7;
    unsigned short field_9;
    char field_b;
    char field_c;
} struct_1;

extern unsigned int g_1005d483;
extern unsigned int g_1005d487;
extern unsigned int g_1005d48f[4];
extern char g_1005d877;
extern unsigned int g_1005d883;
extern unsigned int g_1005d887;
extern unsigned int g_1005d88b;

struct_0 * sub_1000159e(void)
{
    struct_0 *v13;  // eax
    unsigned int v14;  // ebx
    unsigned int v23;  // edx
    struct_1 *iter;  // ebx
    unsigned int node;  // ecx
    unsigned int v17;  // eax
    unsigned int v18[4];  // esi
    unsigned int v19;  // edx
    struct_1 *index;  // ebx
    unsigned int i;  // ecx
    struct_0 *v22;  // eax
    struct_0 *v0;  // [bp-0x38]
    struct_1 *v1;  // [bp-0x34]
    unsigned int v2;  // [bp-0x30]
    struct_0 *v3;  // [bp-0x30]
    unsigned int v4;  // [bp-0x2c]
    unsigned int v5;  // [bp-0x24]
    unsigned int v6;  // [bp-0x20]
    struct_0 *v7;  // [bp-0x1c]
    unsigned int v8;  // [bp-0x18]
    unsigned int v9;  // [bp-0x14]
    unsigned int v10;  // [bp-0x10]
    unsigned int v11;  // [bp-0xc]

    if (!g_1005d487)
        return v13;
    v6 = v14;
    v10 = g_1005d883 - 8;
    v9 = g_1005d887 - 6;
    v5 = g_1005d483;
    v8 = g_1005d483;
    v7 = sub_1003a176(0, 0, (g_1005d88b <= 7 ? 7 - g_1005d483 : g_1005d88b - g_1005d483 + 2));
    v11 = 0;
    iter = NULL;
    node = 0;
    while (node < 250 && (v17 = node * 160, v18 = (unsigned int [4])*((int *)(v17 + 6475152)), *((int *)(v17 + 6475152))))
    {
        v19 = 0;
        while (true)
        {
            if (v19 >= *((int *)&g_1005d877))
            {
                v4 = node;
                iter->field_0[0] = 106;
                *((unsigned short *)&iter->field_0[1]) = v10;
                *((unsigned short *)&iter->field_1[0]) = v9;
                iter->field_2 = v8;
                index = &iter->field_3;
                sub_1000126e(v18);
                index->field_0[0] = 108;
                *((unsigned short *)&index->field_0[1]) = v10;
                *((unsigned short *)&index->field_1[0]) = v9;
                index->field_2 = v8;
                *((char *)&index->field_3) = v11;
                iter = (char *)&index->field_3 + 1;
                node += 1;
                break;
            }
            else if (g_1005d48f[v19] != v18)
            {
                v19 += 1;
            }
            else
            {
                node += 1;
                break;
            }
        }
    }
    i = v7->field_0;
    for (v22 = &v7->field_4; i; i -= 1)
    {
        v4 = i;
        v23 = v22->field_0;
        v2 = v22->field_4;
        iter->field_0[0] = 106;
        *((unsigned short *)&iter->field_0[1]) = v10;
        *((unsigned short *)&iter->field_1[0]) = v9;
        iter->field_2 = v8;
        iter = &iter->field_3;
        v3 = v22;
        if (v23 == 99)
        {
            sub_1000126e(v2);
        }
        else if (v2)
        {
            *((unsigned short *)&iter->field_0[0]) = v23;
            iter->field_0[2] = v2;
            iter = iter->field_1;
        }
        else
        {
            *((unsigned short *)&iter->field_0[0]) = v23;
            v1 = &iter->field_0[2];
            v0 = v22;
            iter = v1;
            if (sub_10001057(v23))
            {
                iter->field_0[0] = v0->field_8;
                iter = &iter->field_0[1];
            }
        }
        v22 = &v3->field_c;
    }
    return v22;
}
```

## `sub_10001708` `0x10001708`

_217 bytes. (leaf/helper — see body)_

```c
void* sub_10001708(void)
{
    void* v7;  // ebx
    unsigned int i;  // ecx
    void* v15;  // ebx
    unsigned int v16;  // edx
    void* iter;  // ebx
    void* node;  // esi
    void* v19;  // ecx
    unsigned int v20;  // eax
    char v21;  // dl
    void* v9;  // eax
    int len;  // ecx
    void* v11;  // ebx
    void* v12;  // ebx
    void* index;  // ebx
    void* v14;  // ecx
    void* v0;  // [bp-0x34]
    void* v1;  // [bp-0x30]
    void* v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x28]
    void* v4;  // [bp-0xc]
    void* v5;  // [bp-0x8]

    v5 = v7;
    for (i = 0; i < 16; i = v3 + 1)
    {
        v3 = i;
        v9 = i * 492 + 6525416;
        if (*((int *)v9))
        {
            v4 = iter;
            *((char *)iter) = 110;
            *((char *)&iter[1]) = i;
            *((unsigned short *)&iter[2]) = (int)v9[4];
            v2 = iter;
            v1 = v9;
            len = lstrlen(v9 + 16);
            v11 = iter;
            *((unsigned short *)&v11[4]) = len;
            v12 = v11 + 6;
            index = v12 + len;
            sub_1002ae6f(v12, v9 + 16, len, v9);
            v9 = v12;
            *((unsigned short *)index) = (int)v9[48];
            v14 = (int)v9[56];
            if (v14 > 0x4)
            {
                *((char *)&index[2]) = 0;
                v15 = index + 3;
                v9 = sub_1002ae6f(v15, v4, v15 - v4, v14);
                v14 = v15;
                index = v15 + v16 - 3;
            }
            *((char *)&index[2]) = *((char *)&v14);
            iter = index + 3;
            node = v9 + 60;
            while (true)
            {
                v19 = v14;
                if (!v14)
                    break;
                v20 = *((int *)node);
                v21 = (int)node[4];
                if ((int)node[4])
                {
                    *((unsigned short *)iter) = v20;
                    *((char *)&iter[2]) = v21;
                    iter += 3;
                }
                else
                {
                    *((unsigned short *)iter) = v20;
                    v2 = iter + 2;
                    v1 = node;
                    v0 = v19;
                    iter += 2;
                    if (sub_10001057(v20))
                    {
                        *((char *)iter) = (char)node[8];
                        iter += 1;
                    }
                }
                node += 12;
                v14 = v19 - 1;
            }
        }
    }
    return v9;
}
```

## `sub_100017e1` `0x100017e1`

_50 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
    char padding_1[4];
    unsigned short field_5;
} struct_0;

extern char g_1005a2a3[4];

struct_0 * sub_100017e1(void)
{
    int i;  // ecx
    struct_0 *v2;  // eax
    int v3;  // ebx
    unsigned int v4;  // edx
    int v5;  // esi

    i = 0;
    while (i < 150)
    {
        v2 = &g_1005a2a3[40 * i];
        if (v2->field_0)
        {
            v4 = *((short *)&(v2->padding_1)[1]) + 8;
            v5 = v3;
            v3 += v4;
            v2 = sub_1002ae6f(v5, v2, v4, i);
            i = v5 + 1;
        }
        else
        {
            i += 1;
        }
    }
    return v2;
}
```

## `sub_10001813` `0x10001813`

_93 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
    char padding_1[2];
    unsigned short field_3;
} struct_0;

extern char g_1005c9b3[4];
extern char g_1005cf17[4];

struct_0 * sub_10001813(void)
{
    int i;  // ecx
    struct_0 *v2;  // eax
    int iter;  // ebx
    unsigned int v4;  // edx
    int v5;  // esi
    int j;  // ecx
    unsigned int v7;  // edx
    int v8;  // esi

    i = 0;
    while (i < 20)
    {
        v2 = &g_1005cf17[69 * i];
        if (v2->field_0)
        {
            v4 = (unsigned int)((v2->padding_1)[1] + 5);
            v5 = iter;
            iter += v4;
            v2 = sub_1002ae6f(v5, v2, v4, i);
            i = v5 + 1;
        }
        else
        {
            i += 1;
        }
    }
    j = 0;
    while (j < 20)
    {
        v2 = &g_1005c9b3[69 * j];
        if (v2->field_0)
        {
            v7 = (unsigned int)((v2->padding_1)[1] + 5);
            v8 = iter;
            iter += v7;
            v2 = sub_1002ae6f(v8, v2, v7, j);
            j = v8 + 1;
        }
        else
        {
            j += 1;
        }
    }
    return v2;
}
```

## `sub_10001870` `0x10001870`

_27 bytes. (leaf/helper — see body)_

```c
extern char g_10042079;
extern char g_1004207a;
extern char g_1004207b;

int sub_10001870(void)
{
    g_10042079 = 130;
    g_1004207a = *((int *)0x63bab8);
    g_1004207b = 215;
    return *((int *)0x63bab8);
}
```

## `sub_1000188b` `0x1000188b`

_158 bytes. (leaf/helper — see body)_

```c
extern char g_10042051;
extern unsigned short g_10042052;
extern unsigned short g_10042054;
extern unsigned int g_10042056;
extern unsigned int g_1004205a;
extern unsigned short g_1004205e;
extern char g_10042060;
extern unsigned short g_10042061;
extern unsigned short g_10042063;
extern char g_10042065;
extern char g_10042066;
extern char g_10042067;
extern unsigned short g_10042068;

int sub_1000188b(void)
{
    g_10042051 = 160;
    g_10042052 = *((int *)0x62cd2c);
    g_10042054 = *((int *)0x62cd28);
    g_10042056 = *((int *)0x62cd00);
    g_1004205a = *((int *)0x62cd24);
    g_1004205e = *((int *)0x62cd20);
    g_10042060 = *((int *)0x62cd18);
    g_10042061 = *((int *)0x62cd10);
    g_10042063 = *((int *)0x62cd0c);
    g_10042065 = *((int *)0x62cd1c);
    g_10042066 = *((int *)0x62cd14);
    g_10042067 = *((int *)0x62cd08);
    g_10042068 = *((int *)0x62cd04);
    return *((int *)0x62cd04);
}
```

## `sub_10001929` `0x10001929`

_55 bytes. (leaf/helper — see body)_

```c
extern char g_1004206a;
extern char g_1004206b;
extern char g_1004206c;

unsigned int sub_10001929(void)
{
    unsigned int node;  // ecx
    unsigned int iter;  // edx
    unsigned int v3;  // eax

    g_1004206a = 161;
    node = 0;
    for (iter = 0; node < 28; iter += 2)
    {
        (&g_1004206b)[iter] = *((int *)(6474968 + node));
        v3 = *((int *)(6474940 + node));
        (&g_1004206c)[iter] = v3;
        node += 4;
    }
    return v3;
}
```

## `sub_10001960` `0x10001960`

_310 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned short field_0;
    char padding_2[4];
    unsigned short field_6;
    char field_8;
    unsigned int field_9;
    unsigned int field_d;
    unsigned short field_11;
    unsigned short field_13;
    char field_15;
    char padding_16[20];
    unsigned short field_2a;
} struct_0;

extern char g_1004203f;
extern char g_10042051;
extern int g_1004206a;
extern char g_10042079;
extern struct_0 *g_1005d48b;
extern unsigned int g_1005d883;
extern unsigned int g_1005d887;
extern unsigned int g_1005d88b;
extern char g_1005db41;
extern char g_1005db43;
extern char g_1005db44;
extern char g_1005db45;
extern char g_1005db46;

unsigned int sub_10001960(struct_0 *a0)
{
    struct_0 *idx;  // ebx
    struct_0 *v1;  // ebx
    struct_0 *v2;  // ebx
    struct_0 *v3;  // ebx
    unsigned int v4;  // ebx

    if (!a0)
    {
        g_1005d48b = GlobalLock(GlobalAlloc(GMEM_MOVEABLE, 0xc350));
        a0 = g_1005d48b;
    }
    idx = &a0->field_8;
    sub_1002ae6f(idx, &g_1004203f, 14);
    if (!g_1004203f)
    {
        *((char *)&idx->field_0) = 10;
        *((int *)((char *)&idx->field_0 + 1)) = *((int *)0x62cd30);
        *((unsigned int *)&idx->padding_2[3]) = 1677721650;
    }
    *((unsigned short *)&(&idx->field_8)[1]) = g_1005d883;
    *((unsigned short *)&(&idx->field_8)[3]) = g_1005d887;
    *((char *)&idx->field_9 + 1) = g_1005d88b;
    v1 = (char *)&idx->field_9 + 2;
    sub_1000133f();
    if (!g_1005db46)
        sub_1000154b();
    if (!g_10042051)
        sub_1000188b();
    sub_1002ae6f(v1, &g_10042051, 25);
    if (g_1005db45)
        v1->field_11 = 0;
    v2 = v1->padding_16;
    if (!g_10042079)
        sub_10001870();
    sub_1002ae6f(v2, &g_10042079, 3);
    v3 = &v2->padding_2[1];
    sub_10001929();
    if (!g_1005db45)
    {
        sub_1002ae6f(v3, &g_1004206a, 15);
        v3 = (char *)&v3->field_9 + 3;
    }
    if (!g_1005db43)
        sub_100017e1();
    sub_1000159e();
    if (!g_1005db44)
        sub_10001708();
    if (!g_1005db41)
        sub_10001813();
    v4 = &v3->field_8 - a0;
    a0->field_6 = v4;
    a0->field_0 = v4 + 6;
    return v4 + 8;
}
```

## hook_captureRenderCtx `0x10001a96`

Named — see [doc 08](../../08-*.md). _34 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1005d88f;
extern unsigned int g_1005db05;

void sub_10001a96(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    g_1005db05 = a0;
    g_1005d88f(a0, a1, a2, a3, &v1);
    return;
}
```

## `sub_10001ab8` `0x10001ab8`

_134 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[2];
    char field_2;
} struct_0;

extern void* g_1005d48b;
extern unsigned int g_1005da85[4];
extern unsigned int g_1005dac5[4];
extern int g_1005db09;
extern SOCKET g_1005db0d;

int sub_10001ab8(void)
{
    struct_0 *v3;  // ecx
    unsigned int v4;  // eax
    unsigned int idx;  // ecx
    unsigned int *v6;  // edx
    unsigned int v7[4];  // eax
    unsigned int len;  // eax
    unsigned int v0;  // [bp-0x24]
    struct_0 *v2;  // [bp+0x100010]

    v3 = v2;
    g_1005db09 = v4;
    if (!v4)
    {
        return;
    }
    else if (v3->field_2 != 20)
    {
        idx = 0;
        while (idx < 16)
        {
            v6 = &g_1005dac5[idx];
            v7 = g_1005da85[idx];
            if (g_1005da85[idx])
            {
                v0 = idx;
                if (*(v6) == 2)
                {
                    *(v6) = 1;
                    g_1005db0d = &v7[0];
                    sub_10001c38(v6, v7);
                    len = sub_10001960(g_1005d48b);
                    send(g_1005db0d, g_1005d48b, len, 0);
                }
                if (*(v6) == 1)
                    send(v7, v2, g_1005db09, 0);
                idx = v0 + 1;
            }
            else
            {
                idx += 1;
            }
        }
        return;
    }
    else
    {
        return;
    }
}
```

## `sub_10001b3e` `0x10001b3e`

_12 bytes. (leaf/helper — see body)_

```c
void sub_10001b3e(void)
{
    char v0;  // [bp+0x0]

    sub_10001b4a(&v0);
    return;
}
```

## `sub_10001b4a` `0x10001b4a`

_82 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005d893;
extern char g_1005db65;

int sub_10001b4a(void)
{
    unsigned int v10;  // eax
    unsigned int v11;  // ecx
    unsigned int v12;  // edx
    unsigned int v13;  // ebx
    unsigned int v14;  // esi
    unsigned int v15;  // edi
    unsigned int v16;  // esi
    int v17;  // ecx
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    unsigned int v7;  // [bp-0x4]

    if (!g_1005db65)
    {
        v7 = v10;
        v6 = v11;
        v5 = v12;
        v4 = v13;
        v2 = v14;
        v1 = v15;
        if (*((int *)0x785d80) > 8)
        {
            v16 = *((int *)0x785d78) + 6;
            v17 = _INSERT(v11, 0, *((short *)v16));
            *((unsigned short *)v16) = *((int *)0x785d80) - 8;
            v0 = v16;
            sub_10001b9f(v0, v17);
            *((unsigned short *)v0) = v17;
        }
    }
    if (g_1005d893 && g_1005d893 != sub_10001b4a)
        goto g_1005d893;
    v7 = v3;
    v6 = 4294967295;
}
```

## `sub_10001b9a` `0x10001b9a`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10001b9a(void)
{
    sub_10001b9e();
    return;
}
```

## `sub_10001b9e` `0x10001b9e`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10001b9e(void)
{
    return;
}
```

## `sub_10001b9f` `0x10001b9f`

_151 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[2];
    char field_2;
} struct_0;

typedef struct struct_1 {
    char field_0;
    unsigned short field_1;
} struct_1;

extern char g_1005c9b3[4];
extern char g_1005cf17[4];
extern unsigned int g_1005db54;

int sub_10001b9f(void)
{
    struct_0 *v15;  // esi
    struct_0 *v16;  // esi
    unsigned short v25;  // bx
    char *v26;  // eax
    unsigned int iter;  // ecx
    struct_1 *v28;  // eax
    unsigned int count;  // eax
    struct_0 *v23;  // esi
    unsigned int node;  // ecx
    unsigned int v0;  // [bp-0x34]
    struct_0 *v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x30]
    char *v3;  // [bp-0x2c], Other Possible Types: struct_0 *
    char *v4;  // [bp-0x28]
    unsigned int v5;  // [bp-0x24]
    unsigned int v6;  // [bp-0x20]
    unsigned int v7;  // [bp-0x20]
    unsigned int v8;  // [bp-0x1c]
    unsigned int v9;  // [bp-0x1c]
    struct_0 *v10;  // [bp-0x18]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    char v13;  // [bp-0x4]

    v16 = v15;
    if (g_1005db54)
    {
        v5 = &v15;
        v4 = &v13;
        v3 = v15;
        if (v15->field_2 == 135)
        {
            count = GetTickCount();
            if (count - g_1005db54 < 1000)
                return;
            g_1005db54 = 0;
        }
        v16 = v3;
    }
    v23 = v16;
    if (v15->field_2 != 0x99)
        return;
    v10 = v15;
    v8 = v11;
    v6 = v9;
    v5 = v7;
    v4 = &v12;
    v3 = &v13;
    v1 = v23;
    v0 = v2;
    node = 0;
    v25 = (unsigned short)v10[1].padding_0;
    while (node < 20)
    {
        v26 = &g_1005cf17[69 * node];
        if (!*(v26))
        {
            node += 1;
        }
        else if (*((short *)&v26[1]) == v25)
        {
            *(v26) = 0;
            break;
        }
        else
        {
            node += 1;
        }
    }
    iter = 0;
    while (iter < 20)
    {
        v28 = &g_1005c9b3[69 * iter];
        if (!v28->field_0)
        {
            iter += 1;
        }
        else if (*((short *)&(&v28->field_0)[1]) == v25)
        {
            v28->field_0 = 0;
            break;
        }
        else
        {
            iter += 1;
        }
    }
    return;
}
```

## `sub_10001bd0` `0x10001bd0`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10001bd0(void)
{
}
```

## `sub_10001c38` `0x10001c38`

_82 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
} struct_0;

extern unsigned int g_1005d87b;
extern struct_0 *g_1005d87f;
extern int g_1005d883;

struct_0 ** sub_10001c38(void)
{
    struct_0 **v1;  // eax

    v1 = g_1005d87f;
    if (g_1005d87f)
        v1 = g_1005d87f->field_0;
    if (*((int *)6475056) != g_1005d87b || v1 != g_1005d87b)
    {
        g_1005d87b = *((int *)0x62cd30);
        v1 = sub_1003997e(*(0x62cd30));
        if (v1)
            g_1005d87f = v1;
    }
    if (g_1005d87f)
        v1 = sub_1002ae6f(&g_1005d883, g_1005d87f + 9, 12);
    return v1;
}
```

## `sub_10001c8a` `0x10001c8a`

_30 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[6];
    unsigned short field_6;
} struct_0;

extern struct_0 *g_1005db2a;
extern unsigned int g_1005db50;

unsigned int sub_10001c8a(void)
{
    unsigned int v1;  // eax

    v1 = g_1005db50;
    if (g_1005db50)
    {
        g_1005db2a->field_6 = v1;
        g_1005db50 = 0;
    }
    return v1;
}
```

## hook_incomingPacketParser `0x10001ca8`

Named — see [doc 08](../../08-*.md). _696 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char field_0;
    unsigned short field_1;
} struct_1;

typedef struct struct_2 {
    char padding_0[1];
    unsigned int field_1;
    unsigned short field_5;
} struct_2;

typedef struct struct_3 {
    char padding_0[5];
    unsigned short field_5;
} struct_3;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern char g_1005a2a3[4];
extern char g_1005c9b3[4];
extern char g_1005cf17[4];
extern void* g_1005d48b;
extern struct_0 *g_1005d897;
extern unsigned int g_1005da85[4];
extern unsigned int g_1005dac5[4];
extern int g_1005db09;
extern SOCKET g_1005db0d;
extern char g_1005db41;
extern char g_1005db43;
extern unsigned int g_1005db4c;

int sub_10001ca8(unsigned int a0, unsigned int a1)
{
    unsigned int v14;  // ecx
    unsigned int v15;  // esi
    unsigned int iter;  // ecx
    struct_1 *v25;  // eax
    unsigned int m;  // ecx
    char *v27;  // eax
    unsigned int n;  // ecx
    char *v29;  // eax
    unsigned int i0;  // ecx
    struct_2 *v31;  // eax
    unsigned int i1;  // ecx
    struct_3 *v33;  // eax
    unsigned int v16;  // edi
    unsigned int i2;  // ecx
    unsigned int v35;  // eax
    void* v36;  // eax
    unsigned int idx;  // ecx
    unsigned int *v38;  // edx
    unsigned int v39[4];  // eax
    unsigned int len;  // eax
    unsigned int v41;  // ebx
    unsigned int v42;  // ebx
    unsigned int v43;  // ebx
    unsigned short v17[3];  // edx
    unsigned int v44;  // ebx
    unsigned int i;  // ecx
    unsigned int v19;  // eax
    unsigned int node;  // ecx
    char *v21;  // eax
    unsigned int k;  // ecx
    char *v23;  // eax
    unsigned int *v0;  // [bp-0x4c]
    unsigned int v1[4];  // [bp-0x48]
    unsigned int v2;  // [bp-0x44]
    void* v3;  // [bp-0x38]
    unsigned int v4;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    char *v6;  // [bp-0x2c]
    char *v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x1c]
    unsigned int v9;  // [bp-0x18]
    char v10;  // [bp-0x14]
    unsigned int v11;  // [bp-0x8]
    char v12;  // [bp-0x4]

    v11 = g_1005d897();
    v9 = v11;
    v8 = v14;
    v7 = &v10;
    v6 = &v12;
    v5 = v15;
    v4 = v16;
    v17 = *((int *)0x785d84) + *((int *)0x785d8c);
    if (v11 == 10)
    {
        for (i = 0; i < 150; i += 1)
        {
            v19 = &g_1005a2a3[40 * i];
            *((char *)v19) = 0;
            *((unsigned int *)(v19 + 1)) = 0;
        }
    }
    else if (v11 == 172)
    {
        if (g_1005db41)
            g_1005db4c = 1;
        node = 0;
        while (node < 20)
        {
            v21 = &g_1005cf17[69 * node];
            if (*(v21))
            {
                if (*((short *)&v21[1]) == v17[0])
                    goto LABEL_10001d61;
                node += 1;
            }
            else
            {
                node += 1;
            }
        }
        k = 0;
        while (k < 20)
        {
            v23 = &g_1005cf17[69 * k];
            if (!*(v23))
            {
                *(v23) = 172;
                v3 = v17[1] + 4;
                sub_1002ae6f(v23 + 1, v17, v17[1] + 4);
                goto LABEL_10001eaf;
            }
            else
            {
                k += 1;
            }
        }
LABEL_10001d61:
    }
    else if (v11 == 178)
    {
        iter = 0;
        while (iter < 20)
        {
            v25 = &g_1005c9b3[69 * iter];
            if (v25->field_0)
            {
                if (*((short *)&(&v25->field_0)[1]) == v17[0])
                    goto LABEL_10001dc2;
                iter += 1;
            }
            else
            {
                iter += 1;
            }
        }
        m = 0;
        while (m < 20)
        {
            v27 = &g_1005c9b3[69 * m];
            if (!*(v27))
            {
                *(v27) = 178;
                v3 = v17[1] + 4;
                sub_1002ae6f(v27 + 1, v17, v17[1] + 4);
                goto LABEL_10001eaf;
            }
            else
            {
                m += 1;
            }
        }
LABEL_10001dc2:
    }
    else if (v11 == 210)
    {
        if (g_1005db43)
            g_1005db4c = 1;
        for (n = 0; n < 150; n += 1)
        {
            v29 = &g_1005a2a3[40 * n];
            if (!*(v29))
            {
                *(v29) = 210;
                v3 = v17[2] + 7;
                sub_1002ae6f(v29 + 1, v17, v17[2] + 7);
                break;
            }
        }
    }
    else if (v11 == 211)
    {
        for (i0 = 0; i0 < 150; i0 += 1)
        {
            v31 = &g_1005a2a3[40 * i0];
            if (*((int *)(v31->padding_0)[1]) == *((int *)&v17[0]))
            {
                *(&v31->padding_0[*((short *)((char *)&v31->field_1 + 1)) + 7]) = 1;
                break;
            }
        }
    }
    else if (v11 == 212)
    {
        for (i1 = 0; i1 < 150; i1 += 1)
        {
            v33 = &g_1005a2a3[40 * i1];
            if (*((int *)&v33->padding_0[1]) == *((int *)&v17[0]))
            {
                *(&v33->padding_0[*((short *)&(v33->padding_0)[1]) + 7]) = 0;
                break;
            }
        }
    }
    else if (v11 == 0xdd)
    {
        for (i2 = 0; i2 < 150; i2 += 1)
        {
            v35 = &g_1005a2a3[40 * i2];
            if (*((int *)(v35 + 1)) == *((int *)&v17[0]))
            {
                *((char *)v35) = 0;
                *((unsigned int *)(v35 + 1)) = 0;
                break;
            }
        }
    }
LABEL_10001eaf:
    v4 = &/* unsupported instruction */;
    if (*((int *)0x785d8c) != 9)
        return v44;
    v36 = *((int *)0x785d84) + *((int *)0x785d8c) - 9;
    *((void* *)&v3[16]) = v36;
    g_1005db09 = *((short *)v36) + 2;
    if (!g_1005db09)
    {
        return v43;
    }
    else if ((int)v3[4] != 20)
    {
        idx = 0;
        while (idx < 16)
        {
            v38 = &g_1005dac5[idx];
            v39 = g_1005da85[idx];
            if (g_1005da85[idx])
            {
                v2 = idx;
                if (*(v38) == 2)
                {
                    v1 = v39;
                    v0 = v38;
                    *(v38) = 1;
                    if (*((int *)0x636fe0) == 30)
                    {
                        g_1005db0d = &v39[0];
                        sub_10001c38();
                        len = sub_10001960(g_1005d48b);
                        send(g_1005db0d, g_1005d48b, len, 0);
                    }
                }
                if (*(v38) == 1)
                    send(v39, (int)v3[16], g_1005db09, 0);
                idx = v2 + 1;
            }
            else
            {
                idx += 1;
            }
        }
        return v41;
    }
    else
    {
        return v42;
    }
}
```

## `sub_10001f75` `0x10001f75`

_202 bytes. calls SendMessageA; refs "TibiaClient"_

```c
extern unsigned int g_63ba9c;
extern unsigned int g_7893f8;

unsigned int sub_10001f75(void)
{
    unsigned int ch;  // eax
    unsigned int v5;  // esi
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    HWND v2;  // [bp-0x8]

    v2 = NULL;
    while (true)
    {
        v2 = FindWindowExA(NULL, v2, "TibiaClient", NULL);
        GetWindowThreadProcessId(v2, &v1);
        ch = GetCurrentProcessId();
        if (!v2)
        {
            return ch;
        }
        else if (ch == v1)
        {
            SendMessageA(v2, 258, 0x1b, NULL);
            SendMessageA(v2, 258, 0x1b, NULL);
            SendMessageA(v2, 258, 0x1b, NULL);
            v5 = g_7893f8;
            g_7893f8 = 8;
            v0 = 0;
            g_63ba9c = 4827488();
            g_7893f8 = v5;
            SendMessageA(v2, 258, 0xd, NULL);
            Sleep(600);
            return SendMessageA(v2, 258, 0xd, NULL);
        }
    }
}
```

## `sub_10001fb0` `0x10001fb0`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10001fb0(void)
{
}
```

## installClientHooks_proxyServer `0x10002041`

Named — see [doc 08](../../08-*.md). _387 bytes. calls CreateThread, VirtualProtect, WriteProcessMemory_

```c
typedef struct SOCKADDR {
    enum ADDRESS_FAMILY sa_family;
    CHAR sa_data[14];
} SOCKADDR;

typedef struct WSADATA {
    unsigned short wVersion;
    unsigned short wHighVersion;
    CHAR szDescription[257];
    CHAR szSystemStatus[129];
    unsigned short iMaxSockets;
    unsigned short iMaxUdpDg;
    char padding_18a[2];
    PSTR lpVendorInfo;
} WSADATA;

extern char g_1005a290;
extern char g_1005a291;
extern unsigned int g_1005a296;
extern unsigned int g_1005d88f;
extern unsigned int g_1005d893;
extern unsigned int g_1005d897;
extern WSADATA g_1005d89f;
extern SOCKADDR g_1005da2d;
extern unsigned short g_1005da2f;
extern unsigned int g_1005da31;
extern SOCKET g_1005da3d;
extern char g_1005da41;
extern unsigned int g_1005da51;
extern void* g_1005da55;
extern HANDLE g_1005db68;

int sub_10002041(void)
{
    SOCKET sock;  // eax
    enum PAGE_PROTECTION_FLAGS v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    if (!g_1005a290)
    {
        VirtualProtect(0x5ab000, 0x604, PAGE_READWRITE, &v0);
        g_1005d88f = *((int *)0x5ab5d4);
        v0 = (enum PAGE_PROTECTION_FLAGS)sub_10001a96;
        WriteProcessMemory(g_1005db68, 0x5ab5d4, &v0, 0x4, NULL);
        if (*(0x4f30c0) == 233)
            g_1005d893 = *((int *)0x4f30c1) + 5189829;
        v0 = (enum PAGE_PROTECTION_FLAGS)233;
        WriteProcessMemory(g_1005db68, 0x4f30c0, &v0, 0x1, NULL);
        g_1005d897 = *((int *)0x45acd6) + 4566234;
        v0 = (enum PAGE_PROTECTION_FLAGS)263876558;
        WriteProcessMemory(g_1005db68, 0x45acd6, &v0, 0x4, NULL);
        WSAStartup(2, &g_1005d89f.wVersion);
        g_1005a290 = 1;
    }
    g_1005da3d = socket(2, SOCK_STREAM, 6);
    *((unsigned short *)&g_1005da2d.sa_family) = 2;
    g_1005da2f = htons(g_1005a296);
    g_1005da31 = 0;
    if (bind(g_1005da3d, &g_1005da2d.sa_family, 16) == -1)
        return -1;
    listen(g_1005da3d, 5);
    g_1005da51 = 16;
    while (true)
    {
        sock = accept(g_1005da3d, &g_1005da41, &g_1005da51);
        if (g_1005a291)
            break;
        g_1005da55 = sock;
        CreateThread(NULL, NULL, sub_10002235, g_1005da55, THREAD_CREATE_RUN_IMMEDIATELY, &v1);
    }
    return WSACleanup();
}
```

## `sub_100021c4` `0x100021c4`

_113 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[2];
    unsigned short field_2;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

typedef struct struct_2 {
    struct struct_1 *field_0;
} struct_2;

extern char g_1004203a;
extern unsigned int g_1005a29a;
extern unsigned int g_1005a29e;
extern struct_2 *g_1005d89b;

int sub_100021c4(unsigned int a0, struct_0 *a1, unsigned int a2)
{
    int v9;  // edi
    int v10;  // esi
    int v11;  // ebx
    int v12;  // edx
    int v13;  // ecx
    int v0;  // [bp-0x28]
    char *v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x20]
    struct_0 *v3;  // [bp-0x1c]
    unsigned int v4;  // [bp-0x18]
    char v5;  // [bp-0x14], Other Possible Types: unsigned short
    unsigned short v6;  // [bp-0x12]
    unsigned int v7;  // [bp-0x10]
    char v8;  // [bp-0x4]

    g_1004203a = 1;
    if (a1->field_2 == 796)
        g_1004203a = 0;
    if (g_1005a29a)
    {
        v2 = a0;
        v1 = &v5;
        sub_1002ae81(&v5, 16, v9, v10, &v8, &v2, v11, v12, v13, &v5, a0, &v5, 16);
        v6 = htons(g_1005a29e);
        v5 = 2;
        v7 = g_1005a29a;
    }
    else
    {
        v4 = a2;
        v3 = a1;
        v2 = a0;
    }
    return g_1005d89b->field_0(v0, v1, a0);
}
```

## proxyClientThread `0x10002235`

Named — see [doc 09](../../09-*.md). _326 bytes. (leaf/helper — see body)_

```c
typedef struct SOCKADDR {
    enum ADDRESS_FAMILY sa_family;
    CHAR sa_data[14];
} SOCKADDR;

extern Byte g_1004202c;
extern char g_1004203a;
extern unsigned int g_1005a292;
extern int g_1005da51;
extern SOCKET g_1005da55;
extern unsigned int g_1005db58;
extern char g_1005db5c;

void sub_10002235(unsigned int a0)
{
    unsigned int count;  // eax
    unsigned int v0;  // [bp-0x44c]
    Byte v1[4];  // [bp-0x43c]
    Byte v2[4];  // [bp-0x438]
    char v3;  // [bp-0x436]
    Byte v4[28];  // [bp-0x3c]
    unsigned int v5;  // [bp-0x20]
    SOCKADDR v6;  // [bp-0x14]

    sub_1002ae6f(v4, "&", 40);
    if (!g_1005a292)
    {
        getsockname(g_1005da55, &v6, &g_1005da51);
        v0 = *((unsigned int *)((void*)&v6 + 4));
    }
    else
    {
        v0 = g_1005a292;
    }
    v5 = v0;
    if (g_1004203a)
        send(a0, &g_1004202c, 14, 0);
    while (true)
    {
        count = recv(a0, v1, 0x400, 0);
        if (!count || count == 4294967295)
        {
            closesocket(a0);
            sub_1000239b(a0);
            count = (unsigned int)ExitThread(0);
        }
        if (v3 == 1)
        {
            send(a0, v4, 40, 0);
        }
        else if (v3 == 10)
        {
            sub_100023c9(a0);
            if (g_1005db58 && *((int *)0x636fe0) != 30)
                sub_10039bbb();
        }
        else if (v3 != 135)
        {
            if (*((int *)&g_1005db5c))
            {
                v2 = v1 - 4;
                sub_1002ade7(v2, count);
            }
            else if (v3 == 20)
            {
                closesocket(a0);
                sub_1000239b(a0);
                ExitThread(0);
            }
        }
    }
}
```

## `sub_100022e0` `0x100022e0`

_28 bytes. (leaf/helper — see body)_

```c
void sub_100022e0(unsigned int a0)
{
    unsigned int v1;  // [bp+0xffbf0]
    unsigned int v2;  // [bp+0xffbf6]

    if (v1 != a0)
        goto LABEL_0x10002392;
    if (v2 == 1650879589)
        goto LABEL_0x100022fc;
    else
        goto LABEL_0x10002392;
}
```

## `sub_10002397` `0x10002397`

_4 bytes. (leaf/helper — see body)_

```c
void sub_10002397(void)
{
    return;
}
```

## `sub_1000239b` `0x1000239b`

_46 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005da85[4];

unsigned int * sub_1000239b(unsigned int a0)
{
    unsigned int i;  // ecx
    unsigned int *v1;  // eax

    for (i = 0; i < 16; i += 1)
    {
        v1 = &g_1005da85[i];
        if (*(v1) == a0)
        {
            *(v1) = 0;
            v1[16] = 0;
            return v1;
        }
    }
    return v1;
}
```

## `sub_100023c9` `0x100023c9`

_57 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005da85[4];

unsigned int * sub_100023c9(unsigned int a0)
{
    unsigned int i;  // ecx
    unsigned int *idx;  // eax

    for (i = 0; i < 16; i += 1)
    {
        idx = &g_1005da85[i];
        if (*(idx) == a0)
        {
            idx[16] = 2;
            return idx;
        }
        if (!*(idx))
        {
            *(idx) = a0;
            idx[16] = 2;
            return idx;
        }
    }
    return idx;
}
```

## `sub_10002402` `0x10002402`

_35 bytes. calls ReadProcessMemory_

```c
extern HANDLE g_1005db68;

int sub_10002402(void* a0)
{
    unsigned int v0;  // [bp-0x8]

    ReadProcessMemory(g_1005db68, a0, &v0, 0x4, NULL);
    return v0;
}
```

## `sub_10002430` `0x10002430`

_41 bytes. refs "%lX"_

```c
int sub_10002430(void)
{
    unsigned int v0;  // [bp-0x48]
    char *v1;  // [bp-0x3c]
    char *v2;  // [bp-0x38]
    Byte v3[32];  // [bp-0x24]
    char v4;  // [bp-0x4]
    unsigned int v5;  // [bp+0x4]

    v2 = &v3[0];
    v1 = &v4;
    v0 = v5;
    wsprintfA(v3, "%lX");
    OutputDebugStringA(v3);
    return;
}
```

## `sub_10002459` `0x10002459`

_33 bytes. (leaf/helper — see body)_

```c
int sub_10002459(int a0)
{
    int v2;  // edi
    int v3;  // esi
    int v4;  // ebx
    int v5;  // edx
    int v6;  // ecx
    int v7;  // eax
    Byte v0[32];  // [bp-0x24]
    char v1;  // [bp-0x4]

    sub_10040940(a0, v0, v2, v3, &v1, v0, v4, v5, v6, v7);
    OutputDebugStringA(v0);
    return v5;
}
```

## `sub_1000247a` `0x1000247a`

_143 bytes. refs "SendProc Error #%d %lX on hotkey: %s", "SendProc Error #%d %lX"_

```c
extern unsigned int g_1005dbd8;
extern unsigned int g_1005dbdc;
extern unsigned int g_1005dbe0;
extern unsigned int g_1005dbe4;
extern unsigned int g_1005dbe8;

unsigned int sub_1000247a(unsigned int *a0, unsigned int a1, unsigned int *idx)
{
    unsigned int v0;  // [bp-0x940]
    unsigned int v1;  // [bp-0x93c]
    unsigned int v2;  // [bp-0x938]
    Byte v3[2352];  // [bp-0x934]

    if (g_1005dbe8)
    {
        v2 = g_1005dbe8;
        v1 = *(a0);
        v0 = g_1005dbd8;
        wsprintfA(v3, "SendProc Error #%d %lX on hotkey: %s");
    }
    else
    {
        v2 = *(a0);
        v1 = g_1005dbd8;
        wsprintfA(v3, "SendProc Error #%d %lX");
    }
    sub_10025172(v3);
    v1 = g_1005dbdc;
    idx[46] = v1;
    v1 = g_1005dbe0;
    idx[49] = v1;
    v1 = g_1005dbe4;
    idx[45] = v1;
    return 0;
}
```

## `sub_10002509` `0x10002509`

_180 bytes. refs "HkeyProc Error #%d %lX"_

```c
extern char g_1005db75;
extern unsigned int g_1005dbbc;
extern unsigned int g_1005dbc0;
extern unsigned int g_1005dbc4;
extern unsigned int g_1005dbc8;
extern unsigned int g_1005dbcc;
extern unsigned int g_1005dbd0;

unsigned int sub_10002509(unsigned int *a0, unsigned int a1, unsigned int *idx)
{
    unsigned int v0;  // [bp-0x944]
    unsigned int v1;  // [bp-0x940]
    unsigned int v2;  // [bp-0x93c]
    unsigned int v3;  // [bp-0x938]
    Byte v4[2352];  // [bp-0x934]

    if (g_1005dbcc && g_1005dbd0)
    {
        v3 = g_1005dbcc;
        v2 = g_1005dbd0;
        v1 = *(a0);
        v0 = g_1005dbbc;
        wsprintfA(v4, "HkeyProc Error #%d %lX on hotkey: %s command: %s");
    }
    else
    {
        v3 = *(a0);
        v2 = g_1005dbbc;
        wsprintfA(v4, "HkeyProc Error #%d %lX");
    }
    sub_10025172(v4);
    if (*(a0) == 3221225725)
    {
        g_1005db75 = 1;
        ExitThread(1);
    }
    idx[46] = g_1005dbc0;
    idx[49] = g_1005dbc4;
    idx[45] = g_1005dbc8;
    return 0;
}
```

## `sub_100025bd` `0x100025bd`

_143 bytes. refs "ActionProc Error #%d %lX on hotkey: %s", "ActionProc Error #%d %lX"_

```c
extern unsigned int g_1005dbec;
extern unsigned int g_1005dbf0;
extern unsigned int g_1005dbf4;
extern unsigned int g_1005dbf8;
extern unsigned int g_1005dbfc;

unsigned int sub_100025bd(unsigned int *a0, unsigned int a1, unsigned int *idx)
{
    unsigned int v0;  // [bp-0x490]
    unsigned int v1;  // [bp-0x48c]
    unsigned int v2;  // [bp-0x488]
    Byte v3[1152];  // [bp-0x484]

    if (g_1005dbfc)
    {
        v2 = g_1005dbfc;
        v1 = *(a0);
        v0 = g_1005dbec;
        wsprintfA(v3, "ActionProc Error #%d %lX on hotkey: %s");
    }
    else
    {
        v2 = *(a0);
        v1 = g_1005dbec;
        wsprintfA(v3, "ActionProc Error #%d %lX");
    }
    sub_10025172(v3);
    v1 = g_1005dbf0;
    idx[46] = v1;
    v1 = g_1005dbf4;
    idx[49] = v1;
    v1 = g_1005dbf8;
    idx[45] = v1;
    return 0;
}
```

## `sub_1000264c` `0x1000264c`

_90 bytes. refs "GuiTimerProc Error #%d %lX"_

```c
extern unsigned int g_1005db8c;
extern unsigned int g_1005db90;
extern unsigned int g_1005db94;
extern unsigned int g_1005db98;

unsigned int sub_1000264c(unsigned int *a0, unsigned int a1, unsigned int *idx)
{
    unsigned int v0;  // [bp-0x8c]
    unsigned int v1;  // [bp-0x88]
    Byte v2[128];  // [bp-0x84]

    v1 = *(a0);
    v0 = g_1005db8c;
    wsprintfA(v2, "GuiTimerProc Error #%d %lX");
    sub_10025172(v2);
    v0 = g_1005db90;
    idx[46] = v0;
    v0 = g_1005db94;
    idx[49] = v0;
    v0 = g_1005db98;
    idx[45] = v0;
    return 0;
}
```

## `sub_100026a6` `0x100026a6`

_139 bytes. refs "TimerProc Error #%d %lX"_

```c
extern unsigned int g_1004265e;
extern char g_1005db75;
extern unsigned int g_1005db78;
extern unsigned int g_1005db7c;
extern unsigned int g_1005db80;
extern unsigned int g_1005db84;

unsigned int sub_100026a6(unsigned int *a0, unsigned int a1, unsigned int *idx)
{
    unsigned int v3;  // ebx
    unsigned int v0;  // [bp-0x20c]
    unsigned int v1;  // [bp-0x208]
    Byte v2[512];  // [bp-0x204]

    v3 = *(a0);
    if (!g_1004265e)
    {
        v1 = *(a0);
        v0 = g_1005db78;
        wsprintfA(v2, "TimerProc Error #%d %lX");
        sub_10025172(v2);
        v0 = g_1005db7c;
        idx[46] = g_1005db7c;
        v0 = g_1005db80;
        idx[49] = g_1005db80;
        v0 = g_1005db84;
        idx[45] = g_1005db84;
    }
    if (v3 == 3221225725 && !g_1004265e)
    {
        g_1005db75 = 1;
        ExitThread(1);
    }
    return 0;
}
```

## `sub_10002731` `0x10002731`

_190 bytes. refs "TickProc Error #%d %d %lX", "TickProc Error #%d %d %lX", "TickProc Error #%d %lX"_

```c
extern unsigned int g_10042218;
extern unsigned int g_1005db9c;
extern unsigned int g_1005dba0;
extern unsigned int g_1005dba4;
extern unsigned int g_1005dba8;
extern unsigned int g_1005dc24;

unsigned int sub_10002731(unsigned int *a0, unsigned int a1, unsigned int *idx)
{
    unsigned int v4;  // ebx
    unsigned int v0;  // [bp-0x90]
    unsigned int v1;  // [bp-0x8c]
    unsigned int v2;  // [bp-0x88]
    Byte v3[128];  // [bp-0x84]

    v4 = *(a0);
    if (g_1005db9c == 400 || g_1005db9c == 418)
    {
        v2 = v4;
        v1 = g_1005dc24;
        v0 = g_1005db9c;
        wsprintfA(v3, "TickProc Error #%d %d %lX");
    }
    else if (g_1005db9c == 502)
    {
        v2 = v4;
        v1 = g_10042218;
        v0 = g_1005db9c;
        wsprintfA(v3, "TickProc Error #%d %d %lX");
    }
    else
    {
        v2 = v4;
        v1 = g_1005db9c;
        wsprintfA(v3, "TickProc Error #%d %lX");
    }
    sub_10025172(v3);
    v1 = g_1005dba0;
    idx[46] = v1;
    v1 = g_1005dba4;
    idx[49] = v1;
    v1 = g_1005dba8;
    idx[45] = v1;
    return 0;
}
```

## `sub_100027ef` `0x100027ef`

_419 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005dbac;
extern unsigned int g_1005dbb0;
extern unsigned int g_1005dbb4;
extern unsigned int g_1005dbb8;
extern void g_1005dc28;
extern char g_1005dc29;
extern char g_1005dc2a;
extern char g_1005dc2b;
extern void g_1005dc2c;
extern char g_1005dc2d;
extern char g_1005dc2e;
extern char g_1005dc2f;
extern void g_1005dc30;
extern char g_1005dc31;
extern char g_1005dc32;
extern char g_1005dc33;
extern void g_1005dc34;
extern char g_1005dc35;
extern char g_1005dc36;
extern char g_1005dc37;
extern void g_1005dc38;
extern char g_1005dc39;
extern char g_1005dc3a;
extern char g_1005dc3b;
extern void g_1005dc3c;
extern char g_1005dc3d;
extern char g_1005dc3e;
extern char g_1005dc3f;
extern void g_1005dc40;
extern char g_1005dc41;
extern char g_1005dc42;
extern char g_1005dc43;
extern void g_1005dc44;
extern char g_1005dc45;
extern char g_1005dc46;
extern char g_1005dc47;

unsigned int sub_100027ef(unsigned int *a0, unsigned int a1, unsigned int *idx)
{
    unsigned int v11;  // ebx
    unsigned int v12;  // eax
    unsigned int v21;  // eax
    unsigned int v22;  // eax
    unsigned int v23;  // eax
    unsigned int v24;  // eax
    unsigned int v25;  // eax
    unsigned int v26;  // eax
    unsigned int v27;  // eax
    unsigned int v28;  // eax
    unsigned int v29;  // eax
    unsigned int v30;  // eax
    unsigned int v13;  // eax
    unsigned int v31;  // eax
    unsigned int v32;  // eax
    unsigned int v33;  // eax
    unsigned int v34;  // eax
    unsigned int v35;  // eax
    unsigned int v36;  // eax
    unsigned int v37;  // eax
    unsigned int v38;  // eax
    unsigned int v39;  // eax
    unsigned int v40;  // eax
    unsigned int v14;  // eax
    unsigned int v41;  // eax
    unsigned int v42;  // eax
    unsigned int v43;  // eax
    unsigned int v15;  // eax
    unsigned int v16;  // eax
    unsigned int v17;  // eax
    unsigned int v18;  // eax
    unsigned int v19;  // eax
    unsigned int v20;  // eax
    unsigned int v0;  // [bp-0x12c]
    unsigned int v1;  // [bp-0x128]
    unsigned int v2;  // [bp-0x124]
    unsigned int v3;  // [bp-0x120]
    unsigned int v4;  // [bp-0x11c]
    unsigned int v5;  // [bp-0x118]
    unsigned int v6;  // [bp-0x114]
    unsigned int v7;  // [bp-0x110]
    unsigned int v8;  // [bp-0x10c]
    unsigned int v9;  // [bp-0x108]
    Byte v10[256];  // [bp-0x104]

    v11 = *(a0);
    v12 = _INSERT(a0, 0, g_1005dc28);
    v13 = _INSERT(v12 * 0x100, 0, g_1005dc29);
    v14 = _INSERT(v13 * 0x100, 0, g_1005dc2a);
    v15 = _INSERT(v14 * 0x100, 0, g_1005dc2b);
    *((unsigned int *)&g_1005dc28) = v15;
    v16 = _INSERT(*((int *)&g_1005dc28), 0, g_1005dc2c);
    v17 = _INSERT(v16 * 0x100, 0, g_1005dc2d);
    v18 = _INSERT(v17 * 0x100, 0, g_1005dc2e);
    v19 = _INSERT(v18 * 0x100, 0, g_1005dc2f);
    *((unsigned int *)&g_1005dc2c) = v19;
    v20 = _INSERT(*((int *)&g_1005dc2c), 0, g_1005dc30);
    v21 = _INSERT(v20 * 0x100, 0, g_1005dc31);
    v22 = _INSERT(v21 * 0x100, 0, g_1005dc32);
    v23 = _INSERT(v22 * 0x100, 0, g_1005dc33);
    *((unsigned int *)&g_1005dc30) = v23;
    v24 = _INSERT(*((int *)&g_1005dc30), 0, g_1005dc34);
    v25 = _INSERT(v24 * 0x100, 0, g_1005dc35);
    v26 = _INSERT(v25 * 0x100, 0, g_1005dc36);
    v27 = _INSERT(v26 * 0x100, 0, g_1005dc37);
    *((unsigned int *)&g_1005dc34) = v27;
    v28 = _INSERT(*((int *)&g_1005dc34), 0, g_1005dc38);
    v29 = _INSERT(v28 * 0x100, 0, g_1005dc39);
    v30 = _INSERT(v29 * 0x100, 0, g_1005dc3a);
    v31 = _INSERT(v30 * 0x100, 0, g_1005dc3b);
    *((unsigned int *)&g_1005dc38) = v31;
    v32 = _INSERT(*((int *)&g_1005dc38), 0, g_1005dc3c);
    v33 = _INSERT(v32 * 0x100, 0, g_1005dc3d);
    v34 = _INSERT(v33 * 0x100, 0, g_1005dc3e);
    v35 = _INSERT(v34 * 0x100, 0, g_1005dc3f);
    *((unsigned int *)&g_1005dc3c) = v35;
    v36 = _INSERT(*((int *)&g_1005dc3c), 0, g_1005dc40);
    v37 = _INSERT(v36 * 0x100, 0, g_1005dc41);
    v38 = _INSERT(v37 * 0x100, 0, g_1005dc42);
    v39 = _INSERT(v38 * 0x100, 0, g_1005dc43);
    *((unsigned int *)&g_1005dc40) = v39;
    v40 = _INSERT(*((int *)&g_1005dc40), 0, g_1005dc44);
    v41 = _INSERT(v40 * 0x100, 0, g_1005dc45);
    v42 = _INSERT(v41 * 0x100, 0, g_1005dc46);
    v43 = _INSERT(v42 * 0x100, 0, g_1005dc47);
    *((unsigned int *)&g_1005dc44) = v43;
    v9 = *((int *)&g_1005dc44);
    v8 = *((int *)&g_1005dc40);
    v7 = *((int *)&g_1005dc3c);
    v6 = *((int *)&g_1005dc38);
    v5 = *((int *)&g_1005dc34);
    v4 = *((int *)&g_1005dc30);
    v3 = *((int *)&g_1005dc2c);
    v2 = *((int *)&g_1005dc28);
    v1 = v11;
    v0 = g_1005dbac;
    wsprintfA(v10, "HprProc Error #%d %lX %08lX%08lX%08lX%08lX%08lX%08lX%08lX%08lX");
    sub_10025172(v10);
    v8 = g_1005dbb0;
    idx[46] = v8;
    v8 = g_1005dbb4;
    idx[49] = v8;
    v8 = g_1005dbb8;
    idx[45] = v8;
    return 0;
}
```

## `sub_10002992` `0x10002992`

_18 bytes. (leaf/helper — see body)_

```c
extern int g_10043598;
extern int g_100435c8;

void sub_10002992(void)
{
    sub_1002ae6f(&g_10043598, &g_100435c8, 48);
    return;
}
```

## hook_fullLightDetour `0x100029a4`

Named — see [doc 08](../../08-*.md). _561 bytes. calls WriteProcessMemory_

```c
typedef struct struct_0 {
    char padding_0[10888];
    unsigned int field_2a88;
} struct_0;

extern unsigned int g_1004476b;
extern unsigned int g_1004476f;
extern char g_10044773;
extern void g_1004477b;
extern void g_10044787;
extern HANDLE g_1005f612;

void sub_100029a4(void)
{
    unsigned int v11;  // edi
    unsigned int v12;  // eax
    unsigned int v13;  // ecx
    unsigned int v14;  // edx
    unsigned int v15;  // ebx
    unsigned int v16;  // eax
    unsigned int v17;  // eax
    struct_0 *v18;  // esi
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    unsigned int v5;  // [bp-0x4]
    unsigned int v7;  // [bp+0xfff10]
    unsigned int v8;  // [bp+0xfff14]
    unsigned int v9;  // [bp+0x100000]

    v9 = v11;
    v7 = v11;
    v8 = v11;
    g_1004476f = 4294967295;
    v5 = v12;
    v4 = v13;
    v3 = v14;
    v2 = v15;
    v1 = /* unsupported instruction */;
    v0 = v11;
    if (!g_1004476b && g_10044773 && *((int *)0x64f600) == 7)
    {
        WriteProcessMemory(g_1005f612, 0x4f46ba, &g_1004477b, 0x6, NULL);
        WriteProcessMemory(g_1005f612, 0x4f47bf, &g_1004477b, 0x6, NULL);
        WriteProcessMemory(g_1005f612, 0x4f4840, &g_1004477b, 0x6, NULL);
        g_1004476f = 0;
    }
    else if (g_1004476b)
    {
        WriteProcessMemory(g_1005f612, 0x4f46ba, &g_1004477b, 0x6, NULL);
        WriteProcessMemory(g_1005f612, 0x4f47bf, &g_1004477b, 0x6, NULL);
        WriteProcessMemory(g_1005f612, 0x4f4840, &g_1004477b, 0x6, NULL);
        v16 = *((int *)0x64f600);
        if (g_1004476b != 254)
            v16 = *((int *)0x64f600) - g_1004476b;
        v17 = v16;
        if (!v16)
        {
            g_1004476b = 0;
        }
        else if (!(v17 > 0 && v17 < 100))
        {
            if (*((int *)0x64f600) <= 7)
            {
                g_1004476f = 7;
                g_1004476f = g_1004476f - *((int *)0x64f600);
                g_1004476f = g_1004476f + v17;
            }
            else
            {
                g_1004476f = 2;
                g_1004476f = g_1004476f + v17;
            }
            if (g_1004476f > 100)
                g_1004476f = 0;
        }
        else if (*((int *)0x64f600) <= 7)
        {
            g_1004476f = 7;
            g_1004476f = g_1004476f - *((int *)0x64f600);
            g_1004476f = g_1004476f + v17;
            if (g_1004476f > 7)
                g_1004476f = 7;
        }
        else
        {
            g_1004476f = 2;
            g_1004476f = g_1004476f + v17;
            if (g_1004476f > 4)
                g_1004476f = 4;
        }
    }
    else
    {
        WriteProcessMemory(g_1005f612, 0x4f46ba, &g_10044787, 0x6, NULL);
        WriteProcessMemory(g_1005f612, 0x4f47bf, &g_10044787, 0x6, NULL);
        WriteProcessMemory(g_1005f612, 0x4f4840, &g_10044787, 0x6, NULL);
    }
    if (g_1004476f != 4294967295)
    {
        v5 = g_1004476f;
        v18->field_2a88 = v5;
    }
}
```

## `sub_10002bd5` `0x10002bd5`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10002bd5(void)
{
    return;
}
```

## hook_fullLight_trampoline `0x10002bd6`

Named — see [doc 08](../../08-*.md). _7 bytes. (leaf/helper — see body)_

```c
void sub_10002bd6(void)
{
    sub_100029a4(); /* do not return */
}
```

## installLightHook `0x10002bdd`

Named — see [doc 08](../../08-*.md). _36 bytes. calls WriteProcessMemory_

```c
extern HANDLE g_1005f612;

int sub_10002bdd(void)
{
    g_1005f612 = GetCurrentProcess();
    return WriteProcessMemory(g_1005f612, 0x4f4869, sub_10002bd6, 0x7, NULL);
}
```

## `sub_10002c01` `0x10002c01`

_30 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1004476b;
extern char g_10044773;

unsigned int sub_10002c01(unsigned int a0)
{
    if (a0 == 0xff)
    {
        g_10044773 = ~(g_10044773);
        return a0;
    }
    g_1004476b = a0;
    return a0;
}
```

## DllEntryPoint `0x10002c1f`

Named — see [doc 05](../../05-*.md). _67 bytes. calls CreateThread_

```c
extern unsigned int g_1005f60a;
extern unsigned int g_1005f612;
extern void g_1005f880;
extern unsigned int g_1005f884;

unsigned int _start(unsigned int a0, unsigned int a1)
{
    unsigned int v9;  // eax
    unsigned int v10;  // ecx
    unsigned int v11;  // edx
    unsigned int v12;  // ebx
    unsigned int v13;  // esi
    unsigned int v14;  // edi
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    char *v2;  // [bp-0x1c]
    char *v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]
    char v8;  // [bp-0x4]

    v7 = a0;
    g_1005f60a = v7;
    if (a1 != 1)
        return 1;
    v7 = v9;
    v6 = v10;
    v5 = v11;
    v4 = v12;
    v3 = &v8;
    v2 = &v8;
    v1 = v13;
    v0 = v14;
    g_1005f612 = GetCurrentProcess();
    CreateThread(NULL, NULL, sub_10002d08, &g_1005f880, THREAD_CREATE_RUN_IMMEDIATELY, &g_1005f884);
    return 1;
}
```

## `sub_10002c6e` `0x10002c6e`

_25 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1004478d;

void sub_10002c6e(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    char v0;  // [bp+0x0]

    g_1004478d(a0, a1, a2, a3, &v0);
    return;
}
```

## postBotMessage `0x10002c87`

Named — see [doc 05](../../05-*.md). _55 bytes. calls SendMessageA_

```c
extern HWND g_1005f61a;
extern unsigned int g_1005f626;

LRESULT sub_10002c87(unsigned int a0, int a1, unsigned int a2, unsigned int a3)
{
    int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v0 = a1;
    v1 = g_1005f626;
    v2 = a3;
    return SendMessageA(g_1005f61a, 273, 0x53a, &v0);
}
```

## EcInit `0x10002cbe`

Named — see [doc 05](../../05-*.md). _74 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1004478d;
extern void g_1005f60a;
extern unsigned int g_1005f61a;

LRESULT EcInit(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x8]

    g_1004478d = a0;
    v1 = a1;
    g_1005f61a = a1;
    Sleep(1000);
    sub_10002d46(*((int *)&g_1005f60a), 0, 0, 10);
    v0 = 0;
    return sub_10002c87(*((int *)&g_1005f60a), 17000, 0, sub_100086b3);
}
```

## worker_stub `0x10002d08`

Named — see [doc 05](../../05-*.md). _14 bytes. (leaf/helper — see body)_

```c
void sub_10002d08(void)
{
    ExitThread(1);
    return;
}
```

