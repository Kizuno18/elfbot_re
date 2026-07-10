# elfbot.dll decompiled — jdrv 0x100204af..0x10021e4e

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_100204af` `0x100204af`

_265 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1008baee;
extern unsigned int g_1008c2ee;

int sub_100204af(void)
{
    unsigned int v5;  // ebx
    char node[2];  // eax
    char iter[2];  // ebx
    char v0;  // [bp-0x15]
    unsigned int idx;  // [bp-0x14]
    unsigned short v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]

    idx = 0;
    v3 = v5;
    v0 = 0;
    iter = node;
    while (true)
    {
        if (v0)
        {
            if (iter[0] == 13 || iter[0] == 10)
            {
                v0 = 0;
                iter = &iter[1];
            }
            else if (iter[0])
            {
                iter = &iter[1];
            }
            else
            {
                (&g_1008baee)[idx] = node;
                return;
            }
        }
        else
        {
            if (iter[0] >= 48 && iter[0] <= 57)
            {
                for (node = NULL; iter[0] >= 48 && iter[0] <= 57 && node < 0x20; iter = &iter[1])
                {
                    if (iter[0])
                    {
                        *((char *)(&v2 + node)) = iter[0];
                        node = &node[1];
                    }
                    else
                    {
                        (&g_1008baee)[idx] = node;
                        return;
                    }
                }
                *((unsigned int *)(&v2 + node)) = 0;
                iter = &iter[1];
                (&g_1008baee)[idx] = sub_10040900(&v2);
                for (node = NULL; iter[0] >= 48 && iter[0] <= 57 && node < 0x20; iter = &iter[1])
                {
                    if (iter[0])
                    {
                        *((char *)(&v2 + node)) = iter[0];
                        node = &node[1];
                    }
                    else
                    {
                        (&g_1008baee)[idx] = node;
                        return;
                    }
                }
                *((unsigned int *)(&v2 + node)) = 0;
                node = sub_10040900(&v2);
                (&g_1008c2ee)[idx] = node;
                idx += 1;
                if (idx >= 0x200)
                    return;
                v0 = 1;
            }
            else
            {
                v0 = 1;
            }
        }
    }
}
```

## `sub_100204ea` `0x100204ea`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100204ea(void)
{
}
```

## `sub_100204ef` `0x100204ef`

_5 bytes. (leaf/helper — see body)_

```c
void sub_100204ef(void)
{
}
```

## `sub_100205bf` `0x100205bf`

_838 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    SOCKET field_0;
    struct struct_0 *field_4;
    unsigned int field_8;
    char padding_c[2];
    unsigned short field_e;
    unsigned short field_10;
    unsigned short field_12;
    char padding_14[16];
    unsigned int field_24;
    unsigned int field_28;
    char padding_2c[4];
    unsigned short field_30;
    unsigned short field_32;
    unsigned short field_34;
    unsigned short field_36;
    unsigned short field_38;
    unsigned short field_3a;
    unsigned short field_3c;
    unsigned short field_3e;
} struct_0;

extern char g_100208f9;
extern unsigned short g_1004339b;
extern unsigned short g_100433a0;
extern char g_100433a2;
extern unsigned short g_100433a3;
extern char g_100433a5;
extern unsigned int g_100433a6;
extern unsigned int g_10043782[4];
extern unsigned int g_100445f8[4];
extern unsigned int g_10044610[4];
extern int g_10057ee8;
extern unsigned int g_1005dc14;
extern unsigned int g_1005dc1c;
extern unsigned int g_1005dc20;
extern struct_0 g_102898ce;
extern char g_10291cce;

unsigned int sub_100205bf(void)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned int v18;  // ecx
    unsigned long v19;  // 4113
    unsigned short v11;  // fs
    unsigned long v12;  // 4128
    unsigned long v13;  // 4136
    unsigned int v14;  // ecx
    struct_0 *iter;  // ebx
    unsigned int sock;  // eax
    unsigned int v17;  // ecx
    struct_0 *v0;  // [bp-0x234]
    struct_0 *v1;  // [bp-0x234]
    struct_0 *v2;  // [bp-0x220], Other Possible Types: unsigned int
    unsigned int v3;  // [bp-0x218]
    unsigned int v4;  // [bp-0x214]
    unsigned int v5;  // [bp-0x20c]
    unsigned int v6;  // [bp-0x208]
    char v7;  // [bp-0x204]

    v6 = sub_10020d0b;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v5 = *((int *)v12);
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v5;
    g_1005dc14 = &v5;
    g_1005dc1c = 1;
    g_1005dc20 = &g_100208f9;
    v14 = 0;
    for (iter = &g_102898ce.field_0; v14 < *((int *)&g_10291cce); iter = (char *)&iter[1].field_0 + 2)
    {
        v3 = v14;
        g_1005dc14 = &v3;
        g_1005dc1c = 2;
        g_1005dc20 = &g_100208f9;
        if (iter->field_0 && !((iter->field_24 = iter->field_24 + 1, iter->field_24 <= 600)))
        {
            shutdown(iter->field_0, SD_BOTH);
            closesocket(iter->field_0);
            iter->field_0 = 0;
            sock = sub_10020950(iter, &g_10057ee8);
            v2 = iter;
        }
        else
        {
            g_1005dc14 = &v3;
            g_1005dc1c = 3;
            g_1005dc20 = &g_100208f9;
            if (iter->field_4)
            {
                iter->field_28 = iter->field_28 + 1;
                g_1005dc14 = &v3;
                g_1005dc1c = 4;
                g_1005dc20 = &g_100208f9;
                if (!iter->field_0)
                {
                    iter->field_24 = iter->field_24 + 1;
                    sock = iter->field_24 & 15;
                    if (!sock)
                    {
                        sock = sub_10020950(iter, &g_10057ee8);
                        v2 = iter;
                    }
                }
                g_1005dc14 = &v3;
                g_1005dc1c = 5;
                g_1005dc20 = &g_100208f9;
                if (iter->field_28 > 600)
                {
                    v2 = iter->field_4;
                    shutdown(iter->field_4, SD_BOTH);
                    sock = closesocket(iter->field_4);
                    iter->field_4 = 0;
                }
                else
                {
                    g_1005dc14 = &v3;
                    g_1005dc1c = 6;
                    g_1005dc20 = &g_100208f9;
                    if (iter->padding_c)
                    {
                        v2 = v2;
                        if ((unsigned int)iter->padding_c < iter->field_30)
                        {
                            v2 = v2;
                            if ((unsigned int)iter->padding_c < iter->field_10)
                            {
                                sub_10020905(iter, g_10043782[iter->field_36]);
                                v2 = iter;
                            }
                        }
                        g_1005dc14 = &v2;
                        g_1005dc1c = 7;
                        g_1005dc20 = &g_100208f9;
                        v0 = v1;
                        if ((unsigned int)iter->padding_c < iter->field_32)
                        {
                            v0 = v1;
                            if ((unsigned int)iter->padding_c < iter->field_10)
                            {
                                v17 = iter->field_3a;
                                if (v17)
                                {
                                    iter->field_3a = v17 - 1;
                                    v0 = v1;
                                }
                                else
                                {
                                    g_1005dc14 = &v2;
                                    g_1005dc1c = 8;
                                    g_1005dc20 = &g_100208f9;
                                    iter->field_3a = 3;
                                    g_100433a6 = iter->field_8;
                                    g_100433a3 = g_100445f8[iter->field_38];
                                    g_100433a0 = 0;
                                    g_100433a2 = 0;
                                    g_100433a5 = 0;
                                    g_1005dc14 = &v2;
                                    g_1005dc1c = 9;
                                    g_1005dc20 = &g_100208f9;
                                    sub_1002ae6f(&v7, &g_1004339b, g_1004339b + 2);
                                    sub_10020950(iter, &v7);
                                    v0 = iter;
                                }
                            }
                        }
                        v1 = v0;
                        g_1005dc14 = &v1;
                        g_1005dc1c = 10;
                        g_1005dc20 = &g_100208f9;
                        sock = iter->field_e;
                        if ((unsigned short)sock < iter->field_34)
                        {
                            v2 = v2;
                            if ((unsigned short)sock < iter->field_12)
                            {
                                v18 = iter->field_3c;
                                if (v18)
                                {
                                    iter->field_3c = v18 - 1;
                                }
                                else
                                {
                                    g_1005dc14 = &v1;
                                    g_1005dc1c = 11;
                                    g_1005dc20 = &g_100208f9;
                                    iter->field_3c = 3;
                                    g_100433a6 = iter->field_8;
                                    g_100433a3 = g_10044610[iter->field_3e];
                                    g_100433a0 = 0;
                                    g_100433a2 = 0;
                                    g_100433a5 = 0;
                                    g_1005dc14 = &v1;
                                    g_1005dc1c = 12;
                                    g_1005dc20 = &g_100208f9;
                                    sub_1002ae6f(&v7, &g_1004339b, g_1004339b + 2);
                                    sock = sub_10020950(iter, &v7);
                                }
                            }
                        }
                    }
                }
            }
        }
        v14 = v3 + 1;
    }
    v19 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v19) = v4;
    return sock;
}
```

## `sub_10020905` `0x10020905`

_75 bytes. (leaf/helper — see body)_

```c
int sub_10020905(int a0, int a1)
{
    unsigned int v5;  // ebx
    int len;  // edx
    unsigned int v0;  // [bp-0x120]
    unsigned short v1;  // [bp-0x116]
    unsigned short v2;  // [bp-0x114]
    unsigned short v3;  // [bp-0x112]
    char v4;  // [bp-0x110]

    v0 = v5;
    len = lstrlen(a1);
    v1 = len + 4;
    v2 = 406;
    v3 = len;
    sub_1002ae6f(&v4, a1, len);
    return sub_10020950(a0, &v1);
}
```

## `sub_10020950` `0x10020950`

_133 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    SOCKET field_4;
} struct_0;

int sub_10020950(struct_0 *a0, unsigned short *a1)
{
    int v5;  // ebx
    int v6;  // eax
    unsigned int v7;  // esi
    char *v0;  // [bp-0x42c]
    unsigned int v1;  // [bp-0x428]
    Byte v2[2];  // [bp-0x408]
    unsigned int v3;  // [bp-0x406]
    char v4;  // [bp-0x402]

    sub_1002ae6f(&v4, a1, *(a1) + 2, v5);
    v6 = sub_100212d7(&a0[2].field_4, &v4);
    v7 = (unsigned int)(v2 - 4);
    if (v7 <= 4)
    {
        return v6;
    }
    else if (v7 < 1000)
    {
        v1 = v7;
        v0 = &v4;
        v3 = 5564688();
        return send(a0->field_4, v2, (unsigned int)(v2 + 2), 0);
    }
    else
    {
        return v6;
    }
}
```

## `sub_100209d5` `0x100209d5`

_463 bytes. calls CreateThread_

```c
typedef struct SOCKADDR {
    enum ADDRESS_FAMILY sa_family;
    CHAR sa_data[14];
} SOCKADDR;

extern unsigned int g_1005dc00;
extern unsigned int g_1005dc04;
extern unsigned int g_1005dc08;
extern unsigned int g_1005dc0c;
extern unsigned int g_1005dc10;
extern unsigned int g_1005f884;
extern unsigned int g_100f0da8;
extern unsigned int g_100f0dac;
extern int g_1013f280;
extern SOCKADDR g_10289898;
extern unsigned short g_1028989a;
extern unsigned int g_1028989c;
extern char g_102898a8;
extern unsigned int g_102898b8;
extern char g_102898cd;
extern void g_102898ce;
extern unsigned int g_10291cce;

int sub_100209d5(void)
{
    void* v7;  // ebp
    unsigned short v8;  // ax
    int v15;  // edi
    unsigned int sock;  // eax
    int v17;  // ecx
    void* v18;  // edx
    int v19;  // esi
    PSTR v20;  // eax
    void* v21;  // edx
    unsigned int v9;  // eax
    unsigned int v10;  // eax
    unsigned int v11;  // eax
    unsigned int v12;  // eax
    unsigned int v13;  // eax
    int v14;  // ebx
    PSTR v1;  // [bp-0x158]
    unsigned int v2;  // [bp-0x12c]
    unsigned int v3;  // [bp-0x128]
    int v4;  // [bp-0x118]
    char v5;  // [bp-0x114]

    *((char **)&(&v4)[276]) = &v5 + 276;
    v7 = &v4 - 276;
    g_100f0da8 = socket(2, SOCK_STREAM, 6);
    *((unsigned short *)&g_10289898.sa_family) = 2;
    v8 = sub_10040900(&g_1013f280);
    if (g_100f0dac)
    {
        v8 = g_100f0dac;
        g_100f0dac = 4294967295;
    }
    g_1028989a = htons(v8);
    g_1028989c = 0;
    v3 = g_100f0da8;
    if (bind(g_100f0da8, &g_10289898.sa_family, 16) == -1)
        return 4294967295;
    listen(g_100f0da8, 5);
    g_102898b8 = 16;
    v9 = TlsAlloc();
    if (v9 != -1)
        g_1005dc04 = v9;
    v10 = TlsAlloc();
    if (v10 != -1)
        g_1005dc00 = v10;
    v11 = TlsAlloc();
    if (v11 != -1)
        g_1005dc08 = v11;
    v12 = TlsAlloc();
    if (v12 != -1)
        g_1005dc0c = v12;
    v13 = TlsAlloc();
    if (v13 != -1)
        g_1005dc10 = v13;
    while (true)
    {
        sock = accept(g_100f0da8, &g_102898a8, &g_102898b8);
        if (!g_102898cd)
            break;
        v17 = 0;
        v18 = &g_102898ce;
        while (true)
        {
            if (v17 >= 0x200)
            {
                v2 = sock;
                shutdown(sock, SD_BOTH);
                closesocket(sock);
                break;
            }
            else if (!*((int *)v18) && !(int)v18[4])
            {
                v19 = v17 + 1;
                if (v19 > g_10291cce)
                    g_10291cce = v19;
                sub_1002ae81(v18, 66, sock, v15, g_10291cce, v7, &v3, v14, v18, v17, sock);
                *((unsigned int *)&v7[276]) = 16;
                if (!getpeername(v18, v7 - 272, v7 - 276))
                {
                    v20 = inet_ntoa((char)(int)v7[268], *((char *)((void*)&(int)v7[268] + 1)), *((char *)((void*)&(int)v7[268] + 2)), *((char *)((void*)&(int)v7[268] + 3)));
                    if (v20)
                    {
                        v1 = v20;
                        wsprintfA(v7 - 0x100, "Proxy::Establishing connection with %s...");
                        sub_10025172(v7 - 0x100);
                    }
                }
                v21 = v18;
                v2 = sock;
                *((unsigned int *)v21) = sock;
                CreateThread(NULL, 0x10000, sub_10020d53, v21, THREAD_CREATE_RUN_IMMEDIATELY, &g_1005f884);
                break;
            }
            else
            {
                v17 += 1;
                v18 += 66;
            }
        }
    }
    return sock;
}
```

## `sub_10020ba4` `0x10020ba4`

_164 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[2];
    unsigned short field_2;
    unsigned int field_4;
} struct_0;

typedef struct struct_2 {
    char padding_0[12];
    struct struct_3 *field_c;
} struct_2;

typedef struct struct_3 {
    struct struct_1 *field_0;
} struct_3;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern char g_100f0d37;
extern char g_100f933c;
extern char g_1013f2a0;
extern int g_1013f2e0;
extern struct_3 *g_102898c0;
extern unsigned int g_102898c4;
extern unsigned int g_102898c8;

unsigned int sub_10020ba4(unsigned int a0, struct_0 *idx, unsigned int a2)
{
    unsigned int v4;  // eax
    int v5;  // edi
    int v6;  // esi
    int v7;  // ebx
    int v8;  // edx
    int v9;  // ecx
    struct_2 *v10;  // eax
    unsigned int v11;  // eax
    int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]

    v2 = a2;
    v1 = a0;
    if (g_100f0d37)
    {
        g_102898c8 = idx->field_2;
        v4 = idx->field_4;
        g_102898c4 = v4;
        idx->field_2 = htons(sub_10040900(&g_1013f2e0, v5, v6, &v3, &v1, v7, v8, v9, v4));
        if (g_1013f2a0 >= 48 && g_1013f2a0 <= 57)
        {
            idx->field_4 = inet_addr(&g_1013f2a0);
        }
        else
        {
            v10 = gethostbyname(&g_1013f2a0);
            if (!v10)
            {
                idx->field_4 = 0;
            }
            else if (v10->field_c->field_0)
            {
                idx->field_4 = v10->field_c->field_0->field_0;
            }
        }
    }
    v11 = g_102898c0->field_0(v0, v4, a0, idx);
    g_100f933c = 20;
    return v11;
}
```

## `sub_10020c48` `0x10020c48`

_67 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005dc00;
extern unsigned int g_1005dc04;
extern unsigned int g_1005dc08;
extern unsigned int g_1005dc0c;
extern unsigned int g_1005dc10;

int sub_10020c48(void)
{
    void* v2;  // eax
    void* v3;  // ecx
    void* v4;  // ebx
    char v1;  // [bp+0x24]

    TlsSetValue(g_1005dc04, v2);
    TlsSetValue(g_1005dc10, v3);
    TlsSetValue(g_1005dc00, v4);
    TlsSetValue(g_1005dc0c, /* unsupported instruction */);
    TlsSetValue(g_1005dc08, &v1);
    return;
}
```

## `sub_10020c8b` `0x10020c8b`

_128 bytes. refs "ProxyException Error #%d Chunk: "_

```c
extern unsigned int g_1005dc00;
extern unsigned int g_1005dc04;
extern unsigned int g_1005dc08;
extern unsigned int g_1005dc0c;
extern unsigned int g_1005dc10;

unsigned int sub_10020c8b(unsigned int a0, unsigned int a1, void* *idx)
{
    void* v0;  // [bp-0x8c]
    void* v1;  // [bp-0x88]
    Byte v2[128];  // [bp-0x84]

    v1 = TlsGetValue(g_1005dc04);
    v1 = TlsGetValue(g_1005dc10);
    v0 = TlsGetValue(g_1005dc04);
    wsprintfA(v2, "ProxyException Error #%d Chunk: ");
    sub_10025172(v2);
    v0 = TlsGetValue(g_1005dc08);
    idx[49] = TlsGetValue(g_1005dc08);
    v0 = TlsGetValue(g_1005dc0c);
    idx[45] = TlsGetValue(g_1005dc0c);
    idx[46] = TlsGetValue(g_1005dc00);
    return 0;
}
```

## `sub_10020d0b` `0x10020d0b`

_72 bytes. refs "ProxyException4 Error #%d"_

```c
extern unsigned int g_1005dc14;
extern unsigned int g_1005dc1c;
extern unsigned int g_1005dc20;

unsigned int sub_10020d0b(unsigned int a0, unsigned int a1, unsigned int *idx)
{
    unsigned int v0;  // [bp-0x88]
    Byte v1[128];  // [bp-0x84]

    v0 = g_1005dc1c;
    wsprintfA(v1, "ProxyException4 Error #%d");
    sub_10025172(v1);
    idx[46] = g_1005dc20;
    idx[49] = g_1005dc14;
    return 0;
}
```

## `sub_10020d53` `0x10020d53`

_742 bytes. calls CreateThread_

```c
typedef struct struct_0 {
    unsigned int field_0;
    SOCKET field_4;
    char padding_8[12];
    unsigned int field_14;
    unsigned int field_18;
    unsigned int field_1c;
    unsigned int field_20;
    char padding_24[12];
    unsigned short field_30;
    unsigned short field_32;
    unsigned short field_34;
    unsigned short field_36;
    unsigned short field_38;
    char padding_3a[4];
    unsigned short field_3e;
    unsigned short field_40;
} struct_0;

extern unsigned short g_10057ee8;
extern unsigned int g_1005f884;

void sub_10020d53(int a0, int a1, struct_0 *a2)
{
    unsigned long v23;  // ldt
    unsigned long v24;  // gdt
    unsigned int count;  // eax
    int v34;  // ebx
    int v35;  // esi
    int v36;  // edi
    int v37;  // edx
    int v38;  // ecx
    int v39;  // ebx
    int v40;  // esi
    int v41;  // edi
    unsigned int count1;  // eax
    unsigned short v25;  // fs
    int v43;  // ebx
    int v44;  // esi
    int v45;  // edi
    unsigned int count2;  // eax
    struct_0 *v47;  // edx
    struct_0 *v48;  // edx
    int v49;  // ebx
    int v50;  // esi
    int v51;  // edi
    struct_0 *idx;  // edx
    unsigned long v26;  // 4125
    int v53;  // ebx
    int v54;  // esi
    int v55;  // edi
    int v56;  // eax
    unsigned int v27;  // 4103
    unsigned long v28;  // 4133
    int v29;  // edi
    int v30;  // esi
    int v31;  // ebx
    int v32;  // eax
    SOCKET v0;  // [bp-0xf044], Other Possible Types: unsigned int
    unsigned short v1;  // [bp-0xf042]
    unsigned int v2;  // [bp-0xf040]
    unsigned int v3;  // [bp-0xf038]
    int v4;  // [bp-0xf034]
    SOCKET sock;  // [bp-0xf024]
    int v6;  // [bp-0xf00c]
    int v7;  // [bp-0xf008]
    Byte v8[2];  // [bp-0xf004]
    int v9;  // [bp-0xf002]
    int v10;  // [bp-0xeffe]
    unsigned int v11;  // [bp-0xeffa]
    unsigned int v12;  // [bp-0xeff6]
    unsigned int v13;  // [bp-0xeff2]
    unsigned int v14;  // [bp-0xefee]
    unsigned short v15;  // [bp-0xefea]
    unsigned short v16;  // [bp-0xefe8]
    unsigned short v17;  // [bp-0xefe6]
    unsigned short v18;  // [bp-0xefe4]
    unsigned short v19;  // [bp-0xefe2]
    unsigned short v20;  // [bp-0xefe0]
    unsigned short v21;  // [bp-0xefde]
    char v22;  // [bp-0x4]

    v26 = _ccall(v23, v24, (unsigned int)v25, 0);
    v27 = *((int *)v26);
    v2 = *((int *)v26);
    v28 = _ccall(v23, v24, (unsigned int)v25, 0);
    *((unsigned int **)v28) = &v2;
    sub_10020c48(v29, v30, &v22, &v2, v31, a1, a0, v32, v27, sub_10020c8b);
    count = a2->field_0;
    v3 = count;
    sock = NULL;
    while (true)
    {
        sub_10020c48(v36, v35, &v22, &v2, v34, v37, v38, count);
        v39 = v34;
        v40 = v35;
        v41 = v36;
        count1 = recv(v3, v8, 0xf000, 0);
        sub_10020c48(v41, v40, &v22, &v2, v39, v37, v38, count1);
        v43 = v39;
        v44 = v40;
        v45 = v41;
        count2 = count1;
        if (!count1 || count2 == 4294967295)
        {
            sub_10020c48(v45, v44, &v22, &v2, v43, v37, v38, count2);
            shutdown(v3, SD_BOTH);
            closesocket(v3);
            v47 = a2;
            v47->field_0 = 0;
            sub_10020950(v47, &g_10057ee8);
            count2 = (unsigned int)ExitThread(0);
        }
        sub_10020c48(v45, v44, &v22, &v2, v43, v37, v38, count2);
        count = count2;
        v34 = v43;
        v35 = v44;
        v36 = v45;
        v48 = a2;
        *((unsigned int *)&v48->padding_24[0]) = 0;
        if (!v8)
        {
            sub_10020c48(v36, v35, &v22, &v2, v34, v48, v38, count);
            v49 = v34;
            v50 = v35;
            v51 = v36;
            v6 = v9;
            v7 = v10;
            idx = a2;
            v0 = v11;
            idx->field_14 = v11;
            v0 = v12;
            idx->field_18 = v12;
            v0 = v13;
            idx->field_1c = v13;
            v0 = v14;
            idx->field_20 = v14;
            v1 = v15;
            idx->field_30 = v1;
            v1 = v16;
            idx->field_32 = v1;
            v1 = v17;
            idx->field_34 = v1;
            v1 = v18;
            idx->field_36 = v1;
            v1 = v19;
            idx->field_38 = v1;
            v1 = v20;
            idx->field_3e = v1;
            v1 = v21;
            idx->field_40 = v1;
            sub_10020c48(v51, v50, &v22, &v2, v49, idx, v38, v10);
            v53 = v49;
            v54 = v50;
            v55 = v51;
            *((unsigned short *)&v4) = 2;
            sock = socket(2, SOCK_STREAM, 6);
            *((unsigned short *)&(&v4)[2]) = v7;
            *((int *)&(&v4)[4]) = v6;
            *((unsigned int *)&(&v4)[8]) = 0;
            *((unsigned int *)&(&v4)[12]) = 0;
            sub_10020c48(v55, v54, &v22, &v2, v53, v37, v38, v6);
            v34 = v53;
            v35 = v54;
            v36 = v55;
            v56 = connect(sock, &v4, 16);
            if (!v56)
            {
                sub_10020c48(v36, v35, &v22, &v2, v34, v37, v38, v56);
                v0 = sock;
                a2->field_4 = sock;
                count = CreateThread(NULL, 0x10000, sub_10021047, a2, THREAD_CREATE_RUN_IMMEDIATELY, &g_1005f884);
            }
            else
            {
                sub_10020c48(v36, v35, &v22, &v2, v34, v37, v38, v56);
                closesocket(sock);
                closesocket(v3);
                count = (unsigned int)ExitThread(0);
            }
        }
        else if (sock)
        {
            sub_10020c48(v36, v35, &v22, &v2, v34, v48, v38, count);
            count = send(sock, v8, count, 0);
        }
    }
}
```

## `sub_10021039` `0x10021039`

_14 bytes. (leaf/helper — see body)_

```c
void sub_10021039(void)
{
    unsigned long v2;  // ldt
    unsigned long v3;  // gdt
    unsigned short v4;  // fs
    unsigned long v5;  // 4113
    unsigned int v0;  // [bp+0x0]

    v5 = _ccall(v2, v3, (unsigned int)v4, 0);
    *((unsigned int *)v5) = v0;
    return;
}
```

## `sub_10021047` `0x10021047`

_590 bytes. (leaf/helper — see body)_

```c
int sub_10021047(void)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    int v18;  // ecx
    unsigned int v19;  // eax
    unsigned int v20[12];  // edx
    unsigned int count;  // eax
    unsigned int v22[12];  // edx
    unsigned int i;  // ebx
    int v24;  // esi
    int v25;  // edi
    void* idx;  // ebp
    unsigned int v27;  // ebx
    unsigned short v10;  // fs
    void* v28;  // ebp
    int v29;  // esi
    int v30;  // edi
    unsigned int count1;  // eax
    unsigned int count2;  // eax
    unsigned int v33;  // edx
    int v34;  // ecx
    int v35;  // edx
    unsigned int v36;  // edx
    unsigned int v37;  // ebx
    unsigned long v11;  // 4125
    void* v38;  // ebp
    int v39;  // esi
    int v40;  // edi
    int v41;  // eax
    void* v42;  // ebp
    int v43;  // esi
    int v44;  // edi
    unsigned int v45;  // ebx
    void* v46;  // ebp
    unsigned int v12;  // 4103
    unsigned long v13;  // 4133
    int v14;  // edi
    int v15;  // esi
    unsigned int v16;  // ebx
    int v17;  // edx
    unsigned int v1;  // [bp-0xf044]
    unsigned int v2;  // [bp-0xf03c]
    unsigned int v3;  // [bp-0xf034]
    unsigned int v4;  // [bp-0xf020]
    unsigned int v5;  // [bp-0xf01c]
    int v6;  // [bp-0xf014]

    *((void* *)&(&v6)[61456]) = &v6 - 61460;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v12 = *((int *)v11);
    v5 = *((int *)v11);
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v13) = &v5;
    sub_10020c48(v14, v15, &v6 - 61456, &v5, v16, v17, v18, v19, v12, sub_10020c8b);
    v20 = *((unsigned int *)(&v6 + 61464));
    v20[11] = 0;
    sub_10020c48(v14, v15, &v6 - 61456, &v5, v16, v20, v18, v19);
    count = v19;
    v22 = v20;
    i = v16;
    v24 = v15;
    v25 = v14;
    v4 = v22[1];
    *((unsigned int *)&(&v6)[8]) = v22[1];
    v4 = v22[0];
    *((unsigned int *)&(&v6)[12]) = v22[0];
    v4 = v19;
    sub_10020c48(v25, v24, &v6 - 61456, &v5, i, v22, v18, count);
    idx = &v6 - 61456;
    while (true)
    {
        *((int *)&idx[61456]) = 0;
        while (true)
        {
            sub_10020c48(v25, v24, idx, &v4, i, v17, v18, count);
            v27 = i;
            v28 = idx;
            v29 = v24;
            v30 = v25;
            count1 = recv((int)v28[61448], v28 + (int)v28[61456] - 0xf000, 0xf000 - (int)v28[61456], 0);
            *((unsigned int *)&v28[61452]) = count1;
            count2 = count1;
            if (!count2 || count2 == 4294967295)
            {
                sub_10020c48(v30, v29, v28, &v4, v27, v17, v18, count2);
                shutdown((int)v28[61448], SD_BOTH);
                closesocket((int)v28[61448]);
                shutdown((int)v28[61444], SD_BOTH);
                closesocket((int)v28[61444]);
                v33 = (int)v28[8];
                *((unsigned int *)(v33 + 4)) = 0;
                *((unsigned int *)v33) = 0;
                count2 = (unsigned int)ExitThread(0);
            }
            sub_10020c48(v30, v29, v28, &v4, v27, v17, v18, count2);
            i = v27;
            idx = v28;
            v24 = v29;
            v25 = v30;
            count = send((int)idx[61444], idx + (int)idx[61456] - 0xf000, count2, 0);
            v34 = (short)idx[0xf000] + 2;
            v35 = (int)idx[61456] + (int)idx[61452];
            if (v34 <= v35)
                break;
            *((int *)&idx[61456]) = v35;
            count = sub_10025172("Fragmented or corrupted recv packet. Stored lenght is larger than received lenght.");
        }
        sub_10020c48(v25, v24, idx, &v4, i, v35, v34, count);
        *((unsigned int *)((int)idx[8] + 40)) = 0;
        for (i = 0; i < (int)idx[61452]; i = v46 + v45 - 0xf000 + v34)
        {
            v3 = i;
            sub_10020c48(v25, v24, idx, &v3, i, (int)idx[8], v34, count, i);
            v36 = (int)idx[8];
            v37 = i;
            v38 = idx;
            v39 = v24;
            v40 = v25;
            v2 = (int)idx[8] + 20;
            v41 = sub_100212a3(v36 + 20, v38 + v37 - 0xf000);
            sub_10020c48(v40, v39, v38, &v2, v37, v17, v18, v41);
            v42 = v38;
            v43 = v39;
            v44 = v40;
            v2 = v36 + 20;
            sub_10020c48(v44, v43, v42, &v2, v2, v17, v18, v41, v2);
            v45 = v36 + 20;
            v46 = v42;
            v24 = v43;
            v25 = v44;
            v1 = v46 + v45 - 0xf000;
            sub_10020c48(v25, v24, v46, &v1, v45, v17, v18, sub_1002131f(v46 + v45 - 0xf000, (int)v46[8]));
            idx = v46;
            v34 = *((short *)(idx + v46 + v45 - 0xf000 - 0xf000)) + 2;
        }
    }
}
```

## `sub_10021295` `0x10021295`

_14 bytes. (leaf/helper — see body)_

```c
void sub_10021295(void)
{
    unsigned long v2;  // ldt
    unsigned long v3;  // gdt
    unsigned short v4;  // fs
    unsigned long v5;  // 4113
    unsigned int v0;  // [bp+0x0]

    v5 = _ccall(v2, v3, (unsigned int)v4, 0);
    *((unsigned int *)v5) = v0;
    return;
}
```

## `sub_100212a3` `0x100212a3`

_52 bytes. (leaf/helper — see body)_

```c
unsigned int sub_100212a3(unsigned int a0, unsigned short *a1)
{
    int i;  // edi
    unsigned int v2;  // eax
    unsigned short *v0;  // [bp-0xc]

    for (i = 6; i < *(a1) + 2; i += 8)
    {
        v0 = (char *)a1 + i;
        v2 = 5547296();
    }
    return v2;
}
```

## `sub_100212d7` `0x100212d7`

_72 bytes. (leaf/helper — see body)_

```c
int sub_100212d7(unsigned int a0, void* a1)
{
    unsigned int v1;  // edi
    int v2;  // edi
    int i;  // esi
    unsigned int v4;  // eax
    unsigned int v5;  // eax
    unsigned int v0;  // [bp-0xc]

    v1 = *((short *)a1);
    if (!v1)
        return v5;
    v2 = (v1 - -1 | 7) + 1;
    *((unsigned short *)&a1[6]) = v2;
    *((unsigned short *)&a1[6]) = (short)a1[6] + 4;
    for (i = 2; i < v2 + 2; i += 8)
    {
        v0 = i + a1 - 2;
        0x54a500();
    }
    return v4;
}
```

## `sub_1002131f` `0x1002131f`

_2228 bytes. refs "Error occured in the following packet: "_

```c
typedef struct struct_0 {
    char padding_0[8];
    struct struct_1 *field_8;
    unsigned short field_c;
    unsigned short field_e;
    unsigned short field_10;
    unsigned short field_12;
    char padding_14[24];
    unsigned int field_2c;
    char padding_30[16];
    unsigned short field_40;
} struct_0;

typedef struct struct_4 {
    char padding_0[5];
    unsigned short field_5;
} struct_4;

typedef struct struct_5 {
    char padding_0[2];
    unsigned short field_2;
} struct_5;

typedef struct struct_1 {
    char field_0;
    char padding_1[1];
    char field_2;
    char padding_3[1];
    char field_4;
} struct_1;

extern unsigned short g_10057eed;

int sub_1002131f(void)
{
    int v11;  // edi
    int v12;  // esi
    int v21;  // esi
    int v22;  // edi
    unsigned int v23;  // ecx
    unsigned int v24;  // ecx
    char v25[5];  // ebx
    struct_0 *v26;  // edx
    struct_0 *idx;  // edx
    char v28[5];  // ebx
    unsigned int v29;  // ebx
    unsigned int v30;  // ebx
    int v13;  // ebx
    unsigned int j;  // ecx
    char v32[5];  // ebx
    unsigned int k;  // ecx
    unsigned int l;  // ecx
    struct_4 *v35;  // ebx
    char v36;  // cl
    struct_4 *node;  // ebx
    char v38[5];  // ebx
    int v39;  // edx
    int v40;  // edx
    int v14;  // edx
    int v41;  // edx
    int v42;  // edx
    struct_0 *v43;  // eax
    int v44;  // edx
    int v45;  // edx
    int v46;  // edx
    int v47;  // edx
    char v48[5];  // ebx
    unsigned int i0;  // ecx
    struct_5 *v50;  // ebx
    int v15;  // ecx
    struct_5 *v51;  // ebx
    int v52;  // edx
    int v53;  // edx
    int v54;  // edx
    int v55;  // edx
    int v56;  // edx
    int v57;  // edx
    int v58;  // edx
    int v59;  // edx
    char v60[5];  // ebx
    int v16;  // eax
    unsigned int m;  // ecx
    unsigned int v62;  // edx
    void* i;  // ebx
    void* idx1;  // ebp
    unsigned int v18;  // ebx
    char iter[5];  // ebx
    struct_0 *index;  // eax
    int v1;  // [bp-0x85c]
    int v2;  // [bp-0x858]
    void* v3;  // [bp-0x854]
    unsigned int v4;  // [bp-0x850]
    char v5[5];  // [bp-0x84c]
    unsigned int v6;  // [bp-0x844]
    struct_0 *v7;  // [bp-0x840]
    unsigned short v8;  // [bp-0x83e]
    int v9;  // [bp-0x830]

    v9 = (int)_INSERT(*((uint16768_t *)(&v9 + 2092)), 2092, &v9 - 2096);
    v9 = (int)_INSERT(v9 CONCAT 0, 0, 4294967295);
    sub_10020c48(v11, v12, &v9 - 2092, &v9, v13, v14, v15, v16, *((unsigned int *)&v9));
    idx1 = &v9 - 2092;
    v18 = *((unsigned int *)(&v9 + 2100)) + 6;
    iter = v18 + 2;
    index = &iter[*((short *)v18)];
    v9 = (int)_INSERT(*((uint16768_t *)(&v9 + 2088)), 2088, index);
    while (true)
    {
        if (iter >= (int)idx1[4])
            return;
        v23 = iter[0];
        *((unsigned int *)&idx1[2092]) = v23;
        sub_10020c48(v22, v21, idx1, &/* unsupported instruction */, (char [5])&iter[1], v14, v23, index);
        v24 = v23;
        iter = &iter[1];
        if ((char)v24 == 173)
        {
            iter = &iter[1 + *((short *)&iter[1]) + 2];
        }
        else
        {
            if ((char)v24 == 20)
                return;
            if ((char)v24 == 142)
            {
                v25 = &iter[4];
                iter = (!*((short *)&v25[0]) ? (char [5])&v25[4] : (char [5])&v25[1 + 2]);
            }
            else if ((char)v24 == 141)
            {
                iter = &iter[1 + 1];
            }
            else if ((char)v24 == 130)
            {
                iter = &iter[2];
            }
            else if ((char)v24 == 144)
            {
                iter += 1;
            }
            else if ((char)v24 == 145)
            {
                iter += 1;
            }
            else if ((char)v24 == 134)
            {
                if (iter[3] == 64)
                {
                    v26 = (int)idx1[12];
                    if (!*((int *)&v26->padding_0[0]) || *((int *)&v26->padding_14[16]) > 450)
                    {
                        index = sub_10021c2d(*((int *)&iter[0]), v26->field_40, v26, iter);
                        iter = *((int *)&iter[0]);
                    }
                }
                iter += 1;
            }
            else if ((char)v24 == 160)
            {
                idx = (int)idx1[12];
                v8 = *((short *)&iter[0]);
                idx->field_c = v8;
                v28 = &iter[2];
                v8 = *((short *)&v28[0]);
                idx->field_10 = v8;
                v29 = &v28[2 + 3];
                v8 = *((short *)v29);
                idx->field_e = v8;
                index = *((short *)v29);
                v30 = v29 + 2;
                v8 = *((short *)v30);
                idx->field_12 = v8;
                iter = v30 + 7;
            }
            else if ((char)v24 == 180)
            {
                iter = &iter[1 + *((short *)&iter[1]) + 2];
            }
            else if ((char)v24 == 179)
            {
                iter = &iter[2];
            }
            else if ((char)v24 == 178)
            {
                iter = &iter[2 + *((short *)&iter[2]) + 2];
            }
            else if ((char)v24 == 171)
            {
                j = iter[0];
                for (iter = &iter[1]; j; j -= 1)
                {
                    iter = &iter[2 + *((short *)&iter[2]) + 2];
                }
            }
            else if ((char)v24 == 172)
            {
                iter = &iter[2 + *((short *)&iter[2]) + 2];
            }
            else if ((char)v24 == 162)
            {
                iter = &iter[2];
            }
            else if ((char)v24 == 110)
            {
                v32 = &iter[3 + *((short *)&iter[3]) + 4];
                k = v32[0];
                for (iter = &v32[1]; k; k -= 1)
                {
                    index = sub_10021e4e(k);
                }
            }
            else if ((char)v24 == 123)
            {
                iter = &iter[4];
            }
            else if ((char)v24 == 112)
            {
                iter = &iter[2];
            }
            else if ((char)v24 == 113)
            {
                iter = &iter[4];
            }
            else if ((char)v24 == 114)
            {
                iter = &iter[2];
            }
            else if ((char)v24 == 122)
            {
                l = iter[0];
                for (iter = &iter[1]; l; l -= 1)
                {
                    iter = &iter[3 + *((short *)&iter[3]) + 14];
                }
            }
            else if ((char)v24 == 125 || (char)v24 == 126)
            {
                v60 = &iter[*((short *)&iter[0]) + 2];
                m = v60[0];
                for (iter = &v60[1]; m; m -= 1)
                {
                    index = sub_10021e4e(m);
                }
            }
            else if ((char)v24 != 127)
            {
                if ((char)v24 == 111)
                {
                    iter = &iter[1];
                }
                else if ((char)v24 == 107)
                {
                    iter = &iter[1 + 1];
                    index = sub_10021e4e();
                }
                else if ((char)v24 == 0xaa)
                {
                    v35 = &iter[4 + *((short *)&iter[4]) + 4];
                    v36 = v35->padding_0[0];
                    node = &v35->padding_0[1];
                    if (v36 == 1 || v36 == 2 || v36 == 3 || v36 == 5 || v36 == 16 || v36 == 0x11 || v36 == 19)
                    {
                        node = (node->padding_0)[1];
                    }
                    else
                    {
                        if (v36 != 6 && v36 != 11 && v36 != 13 && (v36 == 7 || v36 == 10 || v36 == 14 || v36 == 12 || v36 == 16))
                            node = &node->padding_0[2];
                    }
                    iter = &node->padding_0[*((short *)&node->padding_0[0]) + 2];
                }
                else if ((char)v24 != 163)
                {
                    if ((char)v24 == 143)
                    {
                        iter = &iter[1 + 1];
                    }
                    else if ((char)v24 == 181)
                    {
                        iter = &iter[1];
                    }
                    else if ((char)v24 == 161)
                    {
                        iter = &iter[2 + 4];
                    }
                    else if ((char)v24 == 30)
                    {
                        if (!*((int *)(int)idx1[12]) || *((int *)((int)idx1[12] + 36)) > 450)
                            index = sub_10020950((int)idx1[12], &g_10057eed);
                    }
                    else
                    {
                        if ((char)v24 == 133)
                        {
                            iter = &iter[2 + 1];
                        }
                        else if ((char)v24 == 131)
                        {
                            iter = &iter[1 + 1];
                        }
                        else if ((char)v24 == 132)
                        {
                            iter = &iter[1 + 1 + *((short *)&iter[1 + 1]) + 2];
                        }
                        else if ((char)v24 == 140)
                        {
                            iter += 1;
                        }
                        else if ((char)v24 == 106)
                        {
                            iter += 1;
                            index = sub_10021e4e();
                        }
                        else if ((char)v24 == 107)
                        {
                            iter = &iter[1 + 1];
                            index = sub_10021e4e();
                        }
                        else if ((char)v24 == 108)
                        {
                            iter = &iter[1 + 1];
                        }
                        else if ((char)v24 == 105)
                        {
                            for (v38 = iter + 1; *((short *)&v38[0]) != 0xff00 && *((short *)&v38[0]) != 65281; index = sub_10021e4e());
                            iter = &v38[2];
                        }
                        else if ((char)v24 == 10)
                        {
                            index = (int)idx1[12];
                            index->field_8 = *((int *)&iter[0]);
                            iter = &iter[1 + 2];
                        }
                        else if ((char)v24 == 100)
                        {
                            *((unsigned int *)((int)idx1[12] + 44)) = iter[4];
                            iter += 1;
                            index = (int)idx1[12];
                            if (index->field_2c <= 7)
                            {
                                v39 = 0;
                                while (true)
                                {
                                    if (*((short *)&iter[0]) >= 0xff00)
                                    {
                                        v39 = v39 + iter[0] + 1;
                                        iter = &iter[2];
                                        if (v39 == 2016)
                                            break;
                                    }
                                    else
                                    {
                                        index = sub_10021e4e(v39);
                                    }
                                }
                            }
                            else
                            {
                                if (index->field_2c == 14)
                                {
                                    v40 = 0;
                                    while (true)
                                    {
                                        if (*((short *)&iter[0]) >= 0xff00)
                                        {
                                            v40 = v40 + iter[0] + 1;
                                            iter = &iter[2];
                                            if (v40 == 1008)
                                                break;
                                        }
                                        else
                                        {
                                            index = sub_10021e4e(v40);
                                        }
                                    }
                                }
                                else
                                {
                                    if (index->field_2c == 15)
                                    {
                                        v41 = 0;
                                        while (true)
                                        {
                                            if (*((short *)&iter[0]) >= 0xff00)
                                            {
                                                v41 = v41 + iter[0] + 1;
                                                iter = &iter[2];
                                                if (v41 == 756)
                                                    break;
                                            }
                                            else
                                            {
                                                index = sub_10021e4e(v41);
                                            }
                                        }
                                    }
                                    else
                                    {
                                        v42 = 0;
                                        while (true)
                                        {
                                            if (*((short *)&iter[0]) >= 0xff00)
                                            {
                                                v42 = v42 + iter[0] + 1;
                                                iter = &iter[2];
                                                if (v42 == 1260)
                                                    break;
                                            }
                                            else
                                            {
                                                index = sub_10021e4e(v42);
                                            }
                                        }
                                    }
                                }
                            }
                        }
                        else if ((char)v24 == 101 || (char)v24 == 103)
                        {
                            index = (int)idx1[12];
                            if (index->field_2c <= 7)
                            {
                                v56 = 0;
                                while (true)
                                {
                                    if (*((short *)&iter[0]) >= 0xff00)
                                    {
                                        v56 = v56 + iter[0] + 1;
                                        iter = &iter[2];
                                        if (v56 == 144)
                                            break;
                                    }
                                    else
                                    {
                                        index = sub_10021e4e(v56);
                                    }
                                }
                            }
                            else
                            {
                                if (index->field_2c == 14)
                                {
                                    v57 = 0;
                                    while (true)
                                    {
                                        if (*((short *)&iter[0]) >= 0xff00)
                                        {
                                            v57 = v57 + iter[0] + 1;
                                            iter = &iter[2];
                                            if (v57 == 72)
                                                break;
                                        }
                                        else
                                        {
                                            index = sub_10021e4e(v57);
                                        }
                                    }
                                }
                                else
                                {
                                    if (index->field_2c == 15)
                                    {
                                        v58 = 0;
                                        while (true)
                                        {
                                            if (*((short *)&iter[0]) >= 0xff00)
                                            {
                                                v58 = v58 + iter[0] + 1;
                                                iter = &iter[2];
                                                if (v58 == 54)
                                                    break;
                                            }
                                            else
                                            {
                                                index = sub_10021e4e(v58);
                                            }
                                        }
                                    }
                                    else
                                    {
                                        v59 = 0;
                                        while (true)
                                        {
                                            if (*((short *)&iter[0]) >= 0xff00)
                                            {
                                                v59 = v59 + iter[0] + 1;
                                                iter = &iter[2];
                                                if (v59 == 90)
                                                    break;
                                            }
                                            else
                                            {
                                                index = sub_10021e4e(v59);
                                            }
                                        }
                                    }
                                }
                            }
                        }
                        else if ((char)v24 == 0x66 || (char)v24 == 104)
                        {
                            index = (int)idx1[12];
                            if (index->field_2c <= 7)
                            {
                                v52 = 0;
                                while (true)
                                {
                                    if (*((short *)&iter[0]) >= 0xff00)
                                    {
                                        v52 = v52 + iter[0] + 1;
                                        iter = &iter[2];
                                        if (v52 == 112)
                                            break;
                                    }
                                    else
                                    {
                                        index = sub_10021e4e(v52);
                                    }
                                }
                            }
                            else
                            {
                                if (index->field_2c == 14)
                                {
                                    v53 = 0;
                                    while (true)
                                    {
                                        if (*((short *)&iter[0]) >= 0xff00)
                                        {
                                            v53 = v53 + iter[0] + 1;
                                            iter = &iter[2];
                                            if (v53 == 56)
                                                break;
                                        }
                                        else
                                        {
                                            index = sub_10021e4e(v53);
                                        }
                                    }
                                }
                                else
                                {
                                    if (index->field_2c == 15)
                                    {
                                        v54 = 0;
                                        while (true)
                                        {
                                            if (*((short *)&iter[0]) >= 0xff00)
                                            {
                                                v54 = v54 + iter[0] + 1;
                                                iter = &iter[2];
                                                if (v54 == 42)
                                                    break;
                                            }
                                            else
                                            {
                                                index = sub_10021e4e(v54);
                                            }
                                        }
                                    }
                                    else
                                    {
                                        v55 = 0;
                                        while (true)
                                        {
                                            if (*((short *)&iter[0]) >= 0xff00)
                                            {
                                                v55 = v55 + iter[0] + 1;
                                                iter = &iter[2];
                                                if (v55 == 70)
                                                    break;
                                            }
                                            else
                                            {
                                                index = sub_10021e4e(v55);
                                            }
                                        }
                                    }
                                }
                            }
                        }
                        else if ((char)v24 == 191)
                        {
                            v43 = (int)idx1[12];
                            if (v43->field_2c == 7)
                            {
                                v44 = 0;
                                while (true)
                                {
                                    if (*((short *)&iter[0]) >= 0xff00)
                                    {
                                        v44 = v44 + iter[0] + 1;
                                        iter = &iter[2];
                                        if (v44 == 756)
                                            break;
                                    }
                                    else
                                    {
                                        sub_10021e4e(v44);
                                    }
                                }
                            }
                            else
                            {
                                if (v43->field_2c > 7 && v43->field_2c < 13)
                                {
                                    v45 = 0;
                                    while (true)
                                    {
                                        if (*((short *)&iter[0]) >= 0xff00)
                                        {
                                            v45 = v45 + iter[0] + 1;
                                            iter = &iter[2];
                                            if (v45 == 252)
                                                break;
                                        }
                                        else
                                        {
                                            sub_10021e4e(v45);
                                        }
                                    }
                                }
                            }
                            index = (int)idx1[12];
                            index->field_2c = index->field_2c + 1;
                        }
                        else if ((char)v24 == 190)
                        {
                            if (*((int *)((int)idx1[12] + 44)) == 8)
                            {
                                v46 = 0;
                                while (true)
                                {
                                    if (*((short *)&iter[0]) >= 0xff00)
                                    {
                                        v46 = v46 + iter[0] + 1;
                                        iter = &iter[2];
                                        if (v46 == 1512)
                                            break;
                                    }
                                    else
                                    {
                                        sub_10021e4e(v46);
                                    }
                                }
                            }
                            else
                            {
                                if (*((int *)((int)idx1[12] + 44)) > 8)
                                {
                                    v47 = 0;
                                    while (true)
                                    {
                                        if (*((short *)&iter[0]) >= 0xff00)
                                        {
                                            v47 = v47 + iter[0] + 1;
                                            iter = &iter[2];
                                            if (v47 == 252)
                                                break;
                                        }
                                        else
                                        {
                                            sub_10021e4e(v47);
                                        }
                                    }
                                }
                            }
                            index = (int)idx1[12];
                            index->field_2c = index->field_2c - 1;
                        }
                        else if ((char)v24 == 121)
                        {
                            iter = &iter[1];
                        }
                        else if ((char)v24 == 120)
                        {
                            iter = &iter[1];
                            index = sub_10021e4e();
                        }
                        else if ((char)v24 == 200)
                        {
                            v48 = (!*((short *)&iter[0]) ? (char [5])&iter[4] : (char [5])&iter[1 + 2]);
                            i0 = v48[0];
                            for (iter = &v48[1]; i0; i0 -= 1)
                            {
                                iter = &iter[2 + *((short *)&iter[2]) + 3];
                            }
                        }
                        else if ((char)v24 == 211)
                        {
                            iter = &iter[4];
                        }
                        else if ((char)v24 == 212)
                        {
                            iter = &iter[4];
                        }
                        else if ((char)v24 == 210)
                        {
                            iter = &iter[4 + *((short *)&iter[4]) + 3];
                        }
                        else if ((char)v24 == 109)
                        {
                            iter = &iter[2 + 1];
                        }
                        else if ((char)v24 == 112)
                        {
                            iter = &iter[1];
                            index = sub_10021e4e();
                        }
                        else if ((char)v24 == 113)
                        {
                            iter = &iter[2];
                            index = sub_10021e4e();
                        }
                        else if ((char)v24 == 114)
                        {
                            iter = &iter[2];
                        }
                        else if ((char)v24 == 150)
                        {
                            v50 = &iter[1 + 3 + *((short *)&iter[1 + 3]) + 2];
                            v51 = 2 + v50->padding_0 + (char *)v50;
                            iter = 2 + v51->padding_0 + (char *)v51;
                        }
                        else if ((char)v24 == 151)
                        {
                            iter = &iter[1 + *((short *)&iter[1]) + 2];
                        }
                        else if ((char)v24 != 40)
                        {
                            break;
                        }
                    }
                }
            }
        }
    }
    v7 = index;
    v6 = v24;
    v5 = iter;
    v4 = &/* unsupported instruction */;
    v3 = idx1;
    v2 = v21;
    v1 = v22;
    lstrcpy(idx1 - 2084, "Error occured in the following packet: ");
    v62 = (int)idx1[8] + 2;
    i = *((short *)v62) + 2;
    if (i > 0x1f4)
        i = 0x1f4;
    for (; i; i = idx1 - 37)
    {
        sub_100409a8(*((int *)v62), idx1 - 36, v62, i);
        lstrcat(idx1 - 2084, idx1 - 30);
        lstrcat(idx1 - 2084, " ");
        v62 = *((int *)v62) + 1;
    }
    sub_10025172(idx1 - 2084);
    return;
}
```

## `sub_100213a0` `0x100213a0`

_5 bytes. (leaf/helper — see body)_

```c
void sub_100213a0(void)
{
}
```

## `sub_10021792` `0x10021792`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10021792(void)
{
}
```

## `sub_1002179d` `0x1002179d`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1002179d(void)
{
}
```

## `sub_100217c7` `0x100217c7`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100217c7(void)
{
}
```

## `sub_100217d2` `0x100217d2`

_5 bytes. (leaf/helper — see body)_

```c
void sub_100217d2(void)
{
}
```

## `sub_100217fc` `0x100217fc`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100217fc(void)
{
}
```

## `sub_10021807` `0x10021807`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10021807(void)
{
}
```

## `sub_10021828` `0x10021828`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10021828(void)
{
}
```

## `sub_1002186e` `0x1002186e`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002186e(void)
{
}
```

## `sub_10021879` `0x10021879`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10021879(void)
{
}
```

## `sub_100218a0` `0x100218a0`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100218a0(void)
{
}
```

## `sub_100218ab` `0x100218ab`

_5 bytes. (leaf/helper — see body)_

```c
void sub_100218ab(void)
{
}
```

## `sub_100218d2` `0x100218d2`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100218d2(void)
{
}
```

## `sub_100218dd` `0x100218dd`

_5 bytes. (leaf/helper — see body)_

```c
void sub_100218dd(void)
{
}
```

## `sub_100218fb` `0x100218fb`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100218fb(void)
{
}
```

## `sub_1002193e` `0x1002193e`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002193e(void)
{
}
```

## `sub_10021949` `0x10021949`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10021949(void)
{
}
```

## `sub_10021970` `0x10021970`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10021970(void)
{
}
```

## `sub_1002197b` `0x1002197b`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1002197b(void)
{
}
```

## `sub_100219a2` `0x100219a2`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100219a2(void)
{
}
```

## `sub_100219ad` `0x100219ad`

_5 bytes. (leaf/helper — see body)_

```c
void sub_100219ad(void)
{
}
```

## `sub_100219cb` `0x100219cb`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100219cb(void)
{
}
```

## `sub_10021a05` `0x10021a05`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10021a05(void)
{
}
```

## `sub_10021a10` `0x10021a10`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10021a10(void)
{
}
```

## `sub_10021a3a` `0x10021a3a`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10021a3a(void)
{
}
```

## `sub_10021a7a` `0x10021a7a`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10021a7a(void)
{
}
```

## `sub_10021a85` `0x10021a85`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10021a85(void)
{
}
```

## `sub_10021aa9` `0x10021aa9`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10021aa9(void)
{
}
```

## `sub_10021c29` `0x10021c29`

_4 bytes. (leaf/helper — see body)_

```c
void sub_10021c29(void)
{
    return;
}
```

## `sub_10021c2d` `0x10021c2d`

_490 bytes. refs "exori vis", "exori mort", "exori flam"_

```c
extern unsigned int g_100432af;
extern unsigned int g_100432ba;
extern char g_100432c4;
extern unsigned short g_100432c7;
extern char g_100432c9;
extern unsigned short g_100432ca;
extern char g_100432cc;
extern unsigned int g_100432cd;

int sub_10021c2d(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v1;  // ebx
    int v2;  // eax
    unsigned int v3;  // ebx
    unsigned int v4;  // edx
    unsigned int v0;  // [bp-0x8]

    v1 = a1 & 0xffffffc0;
    if (v1 == 64)
    {
        g_100432af = a0;
        v2 = sub_10020950(a2, "\t");
    }
    else if (v1 == 128)
    {
        g_100432ba = a0;
        v2 = sub_10020950(a2, "\t");
    }
    v3 = a1 & 63;
    if (v3 == 1)
    {
        v0 = 3198;
    }
    else if (v3 == 4)
    {
        v0 = 3155;
    }
    else if (v3 == 5)
    {
        v0 = 3200;
    }
    else if (v3 == 40)
    {
        v0 = 3195;
    }
    else if (v3 == 15)
    {
        v0 = 3191;
    }
    else if (v3 == 41)
    {
        v0 = 3180;
    }
    else if (v3 == 18)
    {
        v0 = 3202;
    }
    else if (v3 == 16)
    {
        v0 = 3161;
    }
    else if (v3 == 0x11)
    {
        v0 = 3175;
    }
    else if (v3 == 3)
    {
        v0 = 3158;
    }
    else if (v3 == 2)
    {
        v0 = 3179;
    }
    else
    {
        if (v3 == 6)
            return sub_10020905(a2, "exori vis");
        if (v3 == 7)
            return sub_10020905(a2, "exori mort");
        if (v3 == 8)
            return sub_10020905(a2, "exori flam");
        if (v3 == 9)
            return sub_10020905(a2, "exori frigo");
        if (v3 == 10)
            return sub_10020905(a2, "exori terra");
        if (v3 == 12)
            return sub_10020905(a2, "exori san");
        if (v3 == 11)
            return sub_10020905(a2, "exori hur");
        if (v3 != 42)
            return v2;
        v0 = 3165;
    }
    g_100432c2 = 13;
    g_100432c4 = 132;
    g_100432cd = v4;
    g_100432c7 = 0;
    g_100432c9 = 0;
    g_100432ca = v0;
    g_100432cc = v4;
    return sub_10020950(a2, "\r");
}
```

## `sub_10021c8c` `0x10021c8c`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10021c8c(void)
{
}
```

## `sub_10021ca2` `0x10021ca2`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10021ca2(void)
{
}
```

## `sub_10021cb8` `0x10021cb8`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10021cb8(void)
{
}
```

## `sub_10021cce` `0x10021cce`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10021cce(void)
{
}
```

## `sub_10021ce4` `0x10021ce4`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10021ce4(void)
{
}
```

## `sub_10021cfa` `0x10021cfa`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10021cfa(void)
{
}
```

## `sub_10021d10` `0x10021d10`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10021d10(void)
{
}
```

## `sub_10021d26` `0x10021d26`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10021d26(void)
{
}
```

## `sub_10021d3c` `0x10021d3c`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10021d3c(void)
{
}
```

## `sub_10021d52` `0x10021d52`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10021d52(void)
{
}
```

## `sub_10021d68` `0x10021d68`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10021d68(void)
{
}
```

## `sub_10021e4e` `0x10021e4e`

_130 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10021e4e(void)
{
    unsigned short v1[6];  // ebx
    unsigned short v2[6];  // ebx
    unsigned int v3;  // eax
    unsigned int v4;  // eax
    unsigned int v5;  // eax
    unsigned int v6;  // edx
    unsigned int v7;  // eax

    if (v1[0] == 98)
    {
        v2 = &v1[3];
    }
    else
    {
        if (v1[0] == 99)
            return v3;
        if (v1[0] == 97)
        {
            v2 = 2 + v1[5] + (char *)&v1[5];
        }
        else
        {
            v6 = v1[0];
            v7 = sub_10021ed2(v6, v6, &v1[1]);
            if (!v7)
                return sub_10021f06(v6);
            return v7;
        }
    }
    if (!v2[1])
        return v5;
    return v4;
}
```

