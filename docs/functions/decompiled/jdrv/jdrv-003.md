# elfbot.dll decompiled — jdrv 0x10015fdc..0x1002040d

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10015fdc` `0x10015fdc`

_151 bytes. refs "T 00%d: %s", "T 0%d: %s", "T %d: %s"_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    char field_c;
    char padding_d[31];
    unsigned short field_2c;
} struct_0;

extern char g_100f0e44;
extern unsigned int g_101e6ea8[4];

char sub_10015fdc(char *a0, unsigned int a1)
{
    struct_0 *index;  // ebx
    unsigned int idx;  // ebx
    char v7;  // al
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    struct_0 *v4;  // [bp-0x8], Other Possible Types: unsigned int

    index = &g_101e6ea8[12 * a1];
    if (g_100f0e44 && index->field_c)
    {
        v4 = &index->field_c;
        v3 = a1;
        v2 = (v3 < 10 ? "T 00%d: %s" : (v3 < 100 ? "T 0%d: %s" : "T %d: %s"));
        wsprintfA(a0, (v3 < 10 ? "T 00%d: %s" : (v3 < 100 ? "T 0%d: %s" : "T %d: %s")));
    }
    else
    {
        v4 = index->field_8;
        v3 = index->field_4;
        v2 = index->field_0;
        v1 = a1;
        v0 = (a1 < 10 ? "T 00%d: %d %d %d" : (a1 < 100 ? "T 0%d: %d %d %d" : "T %d: %d %d %d"));
        wsprintfA(a0, (a1 < 10 ? "T 00%d: %d %d %d" : (a1 < 100 ? "T 0%d: %d %d %d" : "T %d: %d %d %d")));
    }
    idx = index->field_2c;
    v7 = *((char *)(268524954 + idx));
    *(a0) = *((char *)(268524954 + idx));
    return v7;
}
```

## `sub_10016073` `0x10016073`

_99 bytes. refs ";
        v1 = v5;
        v0 = ", ";
        v1 = v5;
        v0 = ", ";
        v1 = v5;
        v0 = "_

```c
typedef struct struct_0 {
    unsigned short field_0;
    char field_2;
} struct_0;


int sub_10016073(PSTR a0, struct_0 *a1)
{
    unsigned int v4;  // eax
    unsigned int v5;  // ecx
    PSTR v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    struct_0 *v3;  // [bp-0x8]

    v3 = a1 + 1;
    v4 = a1->field_2;
    v5 = a1->field_0;
    if (v4 == 0xff)
    {
        v2 = " e";
        v1 = v5;
        v0 = "%05d %s %s";
    }
    else if (v4 == 253)
    {
        v2 = "g";
        v1 = v5;
        v0 = "%05d %s %s";
    }
    else if (v4 == 254)
    {
        v2 = "e1";
        v1 = v5;
        v0 = "%05d %s %s";
    }
    else
    {
        v2 = v4;
        v1 = v5;
        v0 = "%05d %02d %s";
    }
    return wsprintfA(a0, v0);
}
```

## `sub_100160d6` `0x100160d6`

_525 bytes. calls SendDlgItemMessageA; refs "<Delete if unused>", "<New Entry>"_

```c
typedef struct struct_0 {
    unsigned short field_0;
    char field_2;
} struct_0;

extern HWND g_10072f94;
extern char g_10202f06;
extern struct_0 g_10202f0a;
extern char g_10207ac6;
extern WPARAM g_10207f0a;
extern WPARAM g_10207f0e;
extern char g_10207f33;
extern char g_10207f34;
extern char g_10207f35;
extern WPARAM g_10207f36;

LRESULT sub_100160d6(void)
{
    unsigned int i;  // ecx
    int j;  // ebx
    unsigned int v7;  // ecx
    struct_0 *k;  // ebx
    struct_0 *v9;  // ebx
    unsigned int l;  // ecx
    struct_0 *v0;  // [bp-0x90]
    unsigned int v1;  // [bp-0x8c]
    unsigned int v2;  // [bp-0x88]
    char v3;  // [bp-0x84]

    SendDlgItemMessageA(g_10072f94, 0x404, 388, NULL, NULL);
    for (i = 0; i < *((int *)&g_10202f06); i += 1)
    {
        v1 = i;
        sub_10015fdc(&v3, i);
        SendDlgItemMessageA(g_10072f94, 0x404, 385, 0xffffffff, &v3);
    }
    SendDlgItemMessageA(g_10072f94, 1015, 390, g_10207f0a, NULL);
    SendDlgItemMessageA(g_10072f94, 1016, 390, g_10207f0e, NULL);
    SendDlgItemMessageA(g_10072f94, 1042, 390, g_10207f36, NULL);
    for (j = 1100; j <= 1117; j += 1)
    {
        SendDlgItemMessageA(g_10072f94, j, 241, (&g_10207ac6)[j], NULL);
    }
    SendDlgItemMessageA(g_10072f94, 1035, 388, NULL, NULL);
    v7 = 0;
    v2 = 0;
    for (k = &g_10202f0a.field_0; v7 < 500; k = &k[6].field_2)
    {
        v7 += 1;
        if (k->field_0 || k->field_2 || (char)k[1].field_0)
            v2 = v7;
    }
    v9 = &g_10202f0a.field_0;
    for (l = 0; l < v2; l += 1)
    {
        v1 = l;
        if (v9->field_0 || v9->field_2 || (char)v9[1].field_0)
        {
            v0 = v9;
            sub_10016073(&v3, v9);
            SendDlgItemMessageA(g_10072f94, 1035, 385, 0xffffffff, &v3);
        }
        else
        {
            SendDlgItemMessageA(g_10072f94, 1035, 385, 0xffffffff, "<Delete if unused>");
        }
        v9 = &v9[6].field_2;
    }
    SendDlgItemMessageA(g_10072f94, 1035, 385, 0xffffffff, "<New Entry>");
    SendDlgItemMessageA(g_10072f94, 0x400, 241, g_10207f33, NULL);
    SendDlgItemMessageA(g_10072f94, 1036, 241, g_10207f34, NULL);
    return SendDlgItemMessageA(g_10072f94, 1037, 241, g_10207f35, NULL);
}
```

## `sub_100162e3` `0x100162e3`

_245 bytes. calls SendDlgItemMessageA; refs "scripts\\*.elfc"_

```c
extern int g_10042f83;
extern HWND g_10072f94;

void* sub_100162e3(void)
{
    void* count;  // eax
    void* v5;  // ecx
    void* v6;  // eax
    void* v7;  // eax
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // ss
    unsigned long v11;  // 4121
    char *v0;  // [bp-0x20c]
    void* v1;  // [bp-0x208]
    char v2;  // [bp-0x204]

    lstrcpy(&v2, &g_10042f83);
    lstrcat(&v2, "scripts\\*.elfc");
    DlgDirListA(g_10072f94, &v2, 1009, 0, DDL_READONLY);
    count = SendDlgItemMessageA(g_10072f94, 1009, 395, NULL, NULL);
    v5 = NULL;
    v6 = count;
    while (true)
    {
        v7 = v6;
        if (v5 >= count)
            break;
        v1 = v5;
        SendDlgItemMessageA(g_10072f94, 1009, 393, v1, &v2);
        v0 = &v2;
        v11 = _ccall(v8, v9, (unsigned int)v10, &v0 - 3 + lstrlen(&v2));
        *((char *)v11) = 0;
        SendDlgItemMessageA(g_10072f94, 1009, 386, v1, NULL);
        v5 = v1 + 1;
        v6 = SendDlgItemMessageA(g_10072f94, 1009, 385, v1, &v2);
    }
    return v7;
}
```

## `sub_100163d8` `0x100163d8`

_96 bytes. calls SendDlgItemMessageA_

```c
extern HWND g_10072f94;
extern unsigned int g_100f0df8;
extern unsigned int g_100f0e00;
extern unsigned int g_100f0e04;
extern char g_100f0e42;
extern char g_100f0e45;
extern int g_100f45c5;

int sub_100163d8(void)
{
    unsigned int v2;  // eax
    LRESULT count;  // eax
    unsigned int v0;  // [bp-0x4]

    v0 = v2;
    count = SendDlgItemMessageA(g_10072f94, 0x404, 392, NULL, NULL);
    g_100f0e00 = 4294967295;
    if (count != 0xffffffff)
        g_100f0e00 = (char *)count + 1;
    g_100f0e42 = v2;
    g_100f0e45 = 0;
    g_100f0df8 = 0;
    sub_1002ae81(&g_100f45c5, 0x400);
    g_100f0e04 = GetTickCount();
    return g_100f0e04;
}
```

## `sub_10016438` `0x10016438`

_947 bytes. refs "Delay_%dsec", "wait %d000"_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    char padding_c[32];
    unsigned short field_2c;
    unsigned short field_2e;
    unsigned int field_30;
    unsigned int field_34;
    unsigned int field_38;
    char field_3c;
    char padding_3d[31];
    unsigned short field_5c;
    unsigned short field_5e;
} struct_0;

extern unsigned int g_101e6ea8;
extern unsigned int g_10202f06;
extern char g_10207f3b;

char * sub_10016438(char *a0, char *a1)
{
    char node[2];  // ebx
    char *v13;  // ecx
    char *v20;  // ecx
    char *iter;  // edi
    char *iter1;  // ecx
    char *v23;  // ecx
    char *iter2;  // edi
    char *v25;  // ecx
    unsigned int v26;  // ebx
    struct_0 *v27;  // ebx
    struct_0 *index;  // ebx
    int i;  // ecx
    unsigned int v30;  // edx
    int len;  // eax
    int v32;  // ecx
    char *dst;  // eax
    char *v15;  // edi
    char *v16;  // ecx
    char *v17;  // ecx
    char *v18;  // edi
    char *v19;  // ecx
    unsigned int v0;  // [bp-0x2040]
    char v1[2];  // [bp-0x203c]
    char *v2;  // [bp-0x2038]
    char *j;  // [bp-0x2014]
    unsigned int v4;  // [bp-0x2010]
    unsigned int v5;  // [bp-0x200c]
    unsigned int v6;  // [bp-0x2008]
    Byte v7[2048];  // [bp-0x2004]
    char v8;  // [bp-0x1804]
    char v9;  // [bp-0x1004]
    char v10;  // [bp-0x804]
    char v11;  // [bp-0x803]

    node = a0;
    v13 = a1;
    while (true)
    {
        do
        {
            if (!v13)
                return dst;
            v15 = &v10;
            while (true)
            {
                v16 = v13;
                if (!v13)
                    break;
                if (node[0] == 13 || node[0] == 10)
                {
                    v16 += 1;
                    node = &node[1];
                    if (node[0] == 13 || node[0] == 10)
                    {
                        v16 += 1;
                        node = &node[1];
                    }
                    break;
                }
                else
                {
                    *(v15) = node[0];
                    node = &node[1];
                    v15 += 1;
                    v13 = v16 + 1;
                }
            }
            *(v15) = 0;
            v6 = sub_10040900(&v10, v16);
            v17 = &v10;
            v18 = &v9;
            while (true)
            {
                v19 = v17;
                if (!v17)
                    break;
                if (node[0] == 13 || node[0] == 10)
                {
                    v19 += 1;
                    node = &node[1];
                    if (node[0] == 13 || node[0] == 10)
                    {
                        v19 += 1;
                        node = &node[1];
                    }
                    break;
                }
                else
                {
                    *(v18) = node[0];
                    node = &node[1];
                    v18 += 1;
                    v17 = v19 + 1;
                }
            }
            *(v18) = 0;
            v5 = sub_10040900(&v9, v19);
            v20 = &v9;
            iter = &v8;
            while (true)
            {
                iter1 = v20;
                if (!v20)
                    break;
                if (node[0] == 13 || node[0] == 10)
                {
                    iter1 += 1;
                    node = &node[1];
                    if (node[0] == 13 || node[0] == 10)
                    {
                        iter1 += 1;
                        node = &node[1];
                    }
                    break;
                }
                else
                {
                    *(iter) = node[0];
                    node = &node[1];
                    iter += 1;
                    v20 = iter1 + 1;
                }
            }
            *(iter) = 0;
            v4 = sub_10040900(&v8, iter1);
            v23 = &v8;
            iter2 = &v7[0];
            while (true)
            {
                v25 = v23;
                if (!v23)
                    break;
                if (node[0] == 13 || node[0] == 10)
                {
                    v25 += 1;
                    node = &node[1];
                    if (node[0] == 13 || node[0] == 10)
                    {
                        v25 += 1;
                        node = &node[1];
                    }
                    break;
                }
                else
                {
                    *(iter2) = node[0];
                    node = &node[1];
                    iter2 += 1;
                    v23 = v25 + 1;
                }
            }
            *(iter2) = 0;
            dst = sub_10040900(v7, v25);
            j = dst;
            v13 = &v7[0];
        } while (!j);
        if (g_10202f06 >= 998)
            break;
        v2 = v13;
        v1 = node;
        v26 = g_10202f06;
        g_10202f06 = g_10202f06 + 1;
        v27 = &(&g_101e6ea8)[12 * v26];
        v0 = v6;
        v27->field_0 = v6;
        v0 = v5;
        v27->field_4 = v5;
        v0 = v4;
        v27->field_8 = v4;
        v27->field_2e = 0;
        v27->padding_c[0] = 0;
        if (j == 0x1 || j == 0x2 || j == 0x7)
        {
            v27->field_2c = 4;
            if (j == 0x7 && v27->field_8)
                v27->field_8 = v27->field_8 - 1;
            v27 = &v27->field_30;
            g_10202f06 = g_10202f06 + 1;
            v0 = v6;
            v27->field_0 = v6;
            v0 = v5;
            v27->field_4 = v5;
            v0 = v4;
            v27->field_8 = v4;
            v27->field_2e = 0;
            v27->padding_c[0] = 0;
        }
        if (j == 0x6)
        {
            v27->field_2c = 7;
        }
        else if (j == 0x5)
        {
            v27->field_2c = 4;
            if (v27->field_8)
                v27->field_8 = v27->field_8 - 1;
        }
        else if (j == 0x2)
        {
            v27->field_2c = 3;
        }
        else if (j == 0x1)
        {
            v27->field_2c = 2;
        }
        else if (j == 0x7)
        {
            v27->field_2c = 6;
            if (v27->field_8)
                v27->field_8 = v27->field_8 - 1;
            index = &v27->field_30;
            g_10202f06 = g_10202f06 + 1;
            index->field_2c = 4;
            v0 = v6;
            index->field_0 = v6;
            v0 = v5;
            index->field_4 = v5;
            v0 = v4;
            index->field_8 = v4;
            index->field_2e = 0;
            index->padding_c[0] = 0;
            if (index->field_8)
                index->field_8 = index->field_8 - 1;
        }
        else if (j == 0x8)
        {
            v27->field_2c = 4;
        }
        else if (j == 0x3)
        {
            v27->field_2c = 4;
            v27->field_4 = v27->field_4 + 1;
            if (v27->field_8 < 15)
                v27->field_8 = v27->field_8 + 1;
        }
        else if (j == 0x4)
        {
            v27->field_2c = 4;
            v27->field_4 = v27->field_4 - 1;
            if (v27->field_8)
                v27->field_8 = v27->field_8 - 1;
        }
        else if (j == 0x9)
        {
            v27->field_2c = 5;
            v27->field_0 = 0;
            v0 = v6;
            wsprintfA(v7, "Delay_%dsec");
            lstrcpy(v27->padding_c, v7);
            v0 = v6;
            dst = wsprintfA(v7, "wait %d000");
            i = 0;
            for (v30 = 0; i < 0x80000; i += 0x1000)
            {
                if (!(&g_10207f3b)[i])
                {
                    v27->field_2e = v30 + 1;
                    dst = lstrcpy(&(&g_10207f3b)[i], v7);
                    break;
                }
                else
                {
                    v30 += 1;
                }
            }
        }
        else if (j == 0xa)
        {
            v27->field_2c = 5;
            v27->field_0 = 0;
            len = lstrlen(&v10);
            dst = &v10;
            while (true)
            {
                v32 = len;
                if (!len)
                    break;
                if ((&v10)[v32] == 92)
                {
                    dst = lstrcpyn(v27->padding_c, &(&v11)[v32], 32);
                    break;
                }
                else
                {
                    len = v32 - 1;
                }
            }
        }
        else
        {
            g_10202f06 = g_10202f06 - 1;
        }
        node = v1;
    }
    return dst;
}
```

## `sub_100167eb` `0x100167eb`

_129 bytes. calls CreateFileA, ReadFile_

```c
extern unsigned int g_1005f622;

int sub_100167eb(PSTR a0)
{
    unsigned int size;  // [bp-0x10]
    void* v1;  // [bp-0xc]
    HANDLE v2;  // [bp-0x8]

    v1 = HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, 0x200000);
    v2 = CreateFileA(a0, 0x80000000, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_ARCHIVE, NULL);
    if (v2 != 0xffffffff)
    {
        size = GetFileSize(v2, NULL);
        ReadFile(v2, v1, size, &g_1005f622, NULL);
        CloseHandle(v2);
    }
    sub_10016438(v1, size);
    return HeapFree(GetProcessHeap(), HEAP_NONE, v1);
}
```

## `sub_1001686c` `0x1001686c`

_1066 bytes. calls MessageBoxA; refs "Waypoints", "Looting", "CavebotOptions"_

```c
extern unsigned int g_10017882;
extern unsigned int g_10017c37;
extern unsigned int g_10017e99;
extern void g_10072f8c;
extern HWND g_10072f90;
extern void g_10072f94;
extern HWND g_10072fb0;
extern char g_100f0d39;
extern char g_100f0d3a;
extern int g_100f45c5;
extern int g_101d5e78;
extern int g_101e6ea8;
extern int g_101f2ea8;
extern unsigned int g_10202f06;
extern int g_10202f0a;
extern int g_10207f3b;

int sub_1001686c(void)
{
    char *v14;  // ebx
    char *node;  // ebx
    unsigned int v16;  // eax
    char *iter;  // esi
    char v18;  // cl
    void* iter1;  // esi
    unsigned int v20;  // eax
    char *v0;  // [bp-0x950]
    unsigned int v1;  // [bp-0x934]
    unsigned int v2;  // [bp-0x930]
    unsigned int v3;  // [bp-0x92c]
    unsigned int v4;  // [bp-0x928]
    unsigned int v5;  // [bp-0x91c]
    unsigned int v6;  // [bp-0x918]
    Byte v7[256];  // [bp-0x914]
    unsigned int v8;  // [bp-0x814]
    unsigned int v9;  // [bp-0x810]
    unsigned int v10;  // [bp-0x80c]
    char v11;  // [bp-0x808]
    char *v12;  // [bp-0x8]

    v2 = 0;
    v1 = 0;
    v3 = 0;
    v12 = v14;
    v10 = 0;
    while (*(node))
    {
        iter = &v11;
        while (true)
        {
            v18 = *(node);
            if (*(node) == 13 || v18 == 10)
            {
                *(iter) = 0;
                node += 1;
                if (*(node) == 13 || *(node) == 10)
                {
                    node += 1;
                    break;
                }
            }
            else if (!v18)
            {
                *(iter) = 0;
                break;
            }
            else
            {
                *(iter) = v18;
                node += 1;
                iter += 1;
            }
        }
        if (*(&v11) == 91)
        {
            for (iter1 = &v11 + 1; *((char *)iter1) != 93 && *((char *)iter1); iter1 += 1);
            *((char *)iter1) = 0;
            if (!lstrcmpi(&v11 + 1, "Waypoints"))
            {
                v10 = sub_10016baf;
                v9 = 0;
                v8 = 0;
                sub_1002ae81(&g_100f45c5, 0x400);
                sub_1002ae81(&g_101e6ea8, 0xc000);
                v16 = sub_1002ae81(&g_10207f3b, 0x80000);
                g_10202f06 = 0;
                v2 = 1;
            }
            else
            {
                if (!lstrcmpi(&v11 + 1, "Looting"))
                {
                    v10 = sub_10016de4;
                    v8 = 0;
                    v16 = sub_1002ae81(&g_10202f0a, 0x2800);
                    v2 = 1;
                }
                else
                {
                    if (!lstrcmpi(&v11 + 1, "CavebotOptions"))
                    {
                        v10 = sub_10016ef2;
                        v2 = 1;
                    }
                    else
                    {
                        if (!lstrcmpi(&v11 + 1, "Alerts"))
                        {
                            v10 = sub_10017106;
                            v2 = 1;
                        }
                        else
                        {
                            if (!lstrcmpi(&v11 + 1, "CavebotHotkeys"))
                            {
                                v10 = sub_10017289;
                                v16 = sub_1002ae81(&g_101f2ea8, 65630);
                                v2 = 1;
                            }
                            else
                            {
                                if (!lstrcmpi(&v11 + 1, "TargetingMonsters"))
                                {
                                    v10 = sub_100172b0;
                                    v16 = sub_1002ae81(&g_101d5e78, 0xa000);
                                    v6 = 0;
                                    v5 = 0;
                                    v4 = 1;
                                    v3 = 1;
                                }
                                else
                                {
                                    if (!lstrcmpi(&v11 + 1, "TargetSelection"))
                                    {
                                        v10 = &g_10017882;
                                        v3 = 1;
                                    }
                                    else
                                    {
                                        if (!lstrcmpi(&v11 + 1, "StanceOptions"))
                                        {
                                            v10 = &g_10017c37;
                                            v3 = 1;
                                        }
                                        else
                                        {
                                            v16 = lstrcmpi(&v11 + 1, "Icons");
                                            if (!v16)
                                            {
                                                v10 = &g_10017e99;
                                                v6 = 0;
                                                v5 = 0;
                                                v1 = 1;
                                            }
                                            else
                                            {
                                                if (g_10072fb0)
                                                {
                                                    v0 = &v11 + 1;
                                                    wsprintfA(v7, "Unknown section: %s\r\n\r\nAborting...");
                                                    v16 = (unsigned int)MessageBoxA(g_10072fb0, v7, "Error when loading script!", MB_APPLMODAL);
                                                }
                                                break;
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
        else if (*(&v11))
        {
            if (!v10)
                return v16;
            goto v10;
        }
    }
    if (v1)
    {
        v16 = IsWindow(g_10072f90);
        if (v16)
            v16 = sub_1001b815();
    }
    if (v2)
    {
        if (IsWindow(*((int *)&g_10072f94)))
        {
            g_100f0d3a = 1;
            sub_100160d6();
            g_100f0d3a = 0;
            sub_100188bf(*((int *)&g_10072f94), 0x404, 390, 0, 0);
            sub_100188bf(*((int *)&g_10072f94), 1035, 390, 0, 0);
        }
        v16 = (unsigned int)sub_10008152();
    }
    if (!v3)
        return v16;
    v20 = IsWindow(*((int *)&g_10072f8c));
    if (!v20)
        return v20;
    g_100f0d39 = 1;
    sub_10015267();
    g_100f0d39 = 0;
    sub_100188bf(*((int *)&g_10072f8c), 0x404, 390, 0, 0);
    return sub_100188bf(*((int *)&g_10072f8c), 1040, 390, 0, 0);
}
```

## `sub_10016b8e` `0x10016b8e`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10016b8e(void)
{
}
```

## `sub_10016baf` `0x10016baf`

_565 bytes. refs "\r\n"_

```c
extern unsigned int g_101e6ea8;
extern unsigned int g_10202f06;
extern unsigned short g_10207f3b;

int sub_10016baf(void)
{
    unsigned int v8;  // ebx
    int idx;  // ebx
    char *node;  // edi
    char *iter;  // esi
    unsigned int v18;  // eax
    char *iter1;  // edi
    char v10;  // al
    char v11;  // al
    int v12;  // eax
    unsigned int v13;  // eax
    char *iter2;  // edi
    unsigned int v15;  // eax
    unsigned int v0;  // [bp-0x4]
    char v2;  // [bp+0xff6f4]
    unsigned int v3;  // [bp+0xff7f4]
    int v4;  // [bp+0xff7f8], Other Possible Types: unsigned int
    char v5;  // [bp+0xff800]
    char v6;  // [bp+0xff801]

    if (v5 != 32 && v6 == 32)
    {
        v0 = v8;
        v4 = 0;
        idx = &(&g_101e6ea8)[12 * g_10202f06];
        g_10202f06 = g_10202f06 + 1;
        v10 = v5 | 32;
        if ((v5 | 32) == 0x77)
        {
            v11 = 1;
        }
        else
        {
            if (v10 == 114)
            {
                v11 = 2;
            }
            else
            {
                if (v10 == 108)
                {
                    v11 = 3;
                }
                else
                {
                    if (v10 == 115)
                    {
                        v11 = 4;
                    }
                    else
                    {
                        if (v10 == 97)
                        {
                            v12 = &(&g_10207f3b)[0x800 * v3];
                            *((unsigned short *)v12) = 32;
                            v4 = v12;
                            v3 += 1;
                            *((short *)(idx + 46)) = v3;
                            v11 = 5;
                        }
                        else
                        {
                            if (v10 == 104)
                            {
                                v11 = 6;
                            }
                            else
                            {
                                if (v10 == 110)
                                {
                                    v11 = 7;
                                }
                                else
                                {
                                    if (v10 == 117)
                                        v11 = 8;
                                }
                            }
                        }
                    }
                }
            }
        }
        *((char *)(idx + 44)) = v11;
        for (iter = /* unsupported instruction */ - 2050; *(iter) == 32; iter += 1);
        if ((*(iter) < 48 || *(iter) > 57) && *(iter) != 45)
        {
            v13 = 0;
        }
        else
        {
            for (iter2 = /* unsupported instruction */ - 2320; *(iter) && *(iter) != 32; iter2 += 1)
            {
                *(iter2) = *(iter);
                iter += 1;
            }
            *(iter2) = 0;
            v13 = (v2 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
        }
        for (*((unsigned int *)idx) = v13; *(iter) == 32; iter += 1);
        if ((*(iter) < 48 || *(iter) > 57) && *(iter) != 45)
        {
            v15 = 0;
        }
        else
        {
            for (node = /* unsupported instruction */ - 2320; *(iter) && *(iter) != 32; node += 1)
            {
                *(node) = *(iter);
                iter += 1;
            }
            *(node) = 0;
            v15 = (v2 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
        }
        for (*((unsigned int *)(idx + 4)) = v15; *(iter) == 32; iter += 1);
        if ((*(iter) < 48 || *(iter) > 57) && *(iter) != 45)
        {
            v18 = 0;
        }
        else
        {
            for (iter1 = /* unsupported instruction */ - 2320; *(iter) && *(iter) != 32; iter1 += 1)
            {
                *(iter1) = *(iter);
                iter += 1;
            }
            *(iter1) = 0;
            v18 = (v2 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
        }
        for (*((unsigned int *)(idx + 8)) = v18; *(iter) == 32; iter += 1);
        lstrcpyn(idx + 12, iter, 32);
    }
    else if (v4)
    {
        if (*((short *)v4) == 32)
            *((char *)v4) = 0;
        else
            lstrcat(v4, "\r\n");
        lstrcat(v4, /* unsupported instruction */ - 2052);
    }
}
```

## `sub_10016de4` `0x10016de4`

_270 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_10202f0a;

int sub_10016de4(void)
{
    unsigned int v5;  // ebx
    int idx;  // ebx
    char *iter;  // esi
    unsigned short v8;  // ax
    char *node;  // edi
    unsigned int iter1;  // edi
    char v11;  // cl
    unsigned short v12;  // ax
    char *iter2;  // edi
    unsigned int v0;  // [bp-0x4]
    char v2;  // [bp+0xff6f4]
    unsigned int v3;  // [bp+0xff7f4]

    v0 = v5;
    idx = &(&g_10202f0a)[10 * v3];
    for (iter = /* unsupported instruction */ - 2052; *(iter) == 32; iter += 1);
    if ((*(iter) < 48 || *(iter) > 57) && *(iter) != 45)
    {
        v8 = 0;
    }
    else
    {
        for (node = /* unsupported instruction */ - 2320; *(iter) && *(iter) != 32; node += 1)
        {
            *(node) = *(iter);
            iter += 1;
        }
        *(node) = 0;
        v8 = (v2 == 45 ? (unsigned short)~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : (unsigned short)sub_10040900(/* unsupported instruction */ - 2320));
    }
    for (*((unsigned short *)idx) = v8; *(iter) == 32; iter += 1);
    iter1 = /* unsupported instruction */ - 2320;
    do
    {
        v11 = *(iter);
    } while (*(iter) && v11 != 32 && (*((char *)iter1) = v11, iter += 1, iter1 += 1, v11 != 58));
    *((char *)iter1) = 0;
    v12 = _INSERT(*((short *)&v2), 0, (char)*((short *)&v2) | 32);
    if (v12 == 12645)
    {
        *((char *)(idx + 2)) = 254;
    }
    else if ((char)v12 == 103)
    {
        *((char *)(idx + 2)) = 253;
    }
    else if ((char)v12 == 101)
    {
        *((char *)(idx + 2)) = 255;
    }
    else
    {
        *((char *)(idx + 2)) = sub_10040900(/* unsupported instruction */ - 2320);
    }
    for (; *(iter) == 32; iter += 1);
    for (iter2 = /* unsupported instruction */ - 2320; *(iter); iter2 += 1)
    {
        *(iter2) = *(iter);
        iter += 1;
    }
    *(iter2) = 0;
    lstrcpyn(idx + 3, /* unsupported instruction */ - 2320, 0x11);
    v3 += 1;
}
```

## `sub_10016ef2` `0x10016ef2`

_532 bytes. refs "Rope:", "Elvenhair rope", "Shovel:"_

```c
extern unsigned int g_10207f0a;
extern unsigned int g_10207f0e;
extern char g_10207f33;
extern char g_10207f34;
extern char g_10207f35;
extern unsigned int g_10207f36;

int sub_10016ef2(void)
{
    char *iter;  // esi
    char *node;  // edi
    char *iter1;  // edi
    char v5;  // cl
    char *iter2;  // edi
    char *k;  // edi
    unsigned int v8;  // eax
    char v1;  // [bp+0xff6f4]

    for (iter = /* unsupported instruction */ - 2052; *(iter) == 32; iter += 1);
    node = /* unsupported instruction */ - 2320;
    do
    {
        v5 = *(iter);
    } while (*(iter) && v5 != 32 && (*(node) = v5, iter += 1, node += 1, v5 != 58));
    if (!lstrcmpi(/* unsupported instruction */ - 2320, "Rope:"))
    {
        for (*(node) = 0; *(iter) == 32; iter += 1);
        for (iter2 = /* unsupported instruction */ - 2320; *(iter); iter2 += 1)
        {
            *(iter2) = *(iter);
            iter += 1;
        }
        *(iter2) = 0;
        g_10207f0a = 0;
        if (!lstrcmpi(/* unsupported instruction */ - 2320, "Elvenhair rope"))
            g_10207f0a = 1;
    }
    else if (!lstrcmpi(/* unsupported instruction */ - 2320, "Shovel:"))
    {
        for (; *(iter) == 32; iter += 1);
        for (k = /* unsupported instruction */ - 2320; *(iter); k += 1)
        {
            *(k) = *(iter);
            iter += 1;
        }
        *(k) = 0;
        g_10207f0e = 0;
        if (!lstrcmpi(/* unsupported instruction */ - 2320, "Light Shovel"))
            g_10207f0e = 1;
    }
    else if (!lstrcmpi(/* unsupported instruction */ - 2320, "SkipNearbyNodes:"))
    {
        for (; *(iter) == 32; iter += 1);
        if ((*(iter) < 48 || *(iter) > 57) && *(iter) != 45)
        {
            v8 = 0;
        }
        else
        {
            for (iter1 = /* unsupported instruction */ - 2320; *(iter) && *(iter) != 32; iter1 += 1)
            {
                *(iter1) = *(iter);
                iter += 1;
            }
            *(iter1) = 0;
            v8 = (v1 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
        }
        g_10207f36 = v8;
    }
    else if (!lstrcmpi(/* unsupported instruction */ - 2320, "OpenNextBp:"))
    {
        for (; *(iter) == 32; iter += 1);
        g_10207f35 = ((*(iter) | 32) == 121 ? 1 : 0);
    }
    else if (!lstrcmpi(/* unsupported instruction */ - 2320, "LootNearbyTargets:"))
    {
        for (; *(iter) == 32; iter += 1);
        g_10207f34 = ((*(iter) | 32) == 121 ? 1 : 0);
    }
    else if (!lstrcmpi(/* unsupported instruction */ - 2320, "LootDistantTargets:"))
    {
        for (; *(iter) == 32; iter += 1);
        g_10207f33 = ((*(iter) | 32) == 121 ? 1 : 0);
    }
}
```

## `sub_10017106` `0x10017106`

_387 bytes. calls MessageBoxA; refs "PlayerOnScreen:", "GmDetected:", "PlayerAttacking:"_

```c
extern void g_10207f12;
extern void g_10207f15;
extern void g_10207f18;
extern void g_10207f1b;
extern void g_10207f1e;
extern void g_10207f21;

int sub_10017106(void)
{
    char *iter;  // esi
    char *node;  // edi
    char v5;  // cl
    void* v6;  // ebx
    void* ptr;  // ebx
    char *iter1;  // edi
    char v9;  // cl
    unsigned int v10;  // edi
    char v11;  // cl
    unsigned int v1;  // [bp+0xff6f4]

    for (iter = /* unsupported instruction */ - 2052; *(iter) == 32; iter += 1);
    node = /* unsupported instruction */ - 2320;
    do
    {
        v5 = *(iter);
    } while (*(iter) && v5 != 32 && (*(node) = v5, iter += 1, node += 1, v5 != 58));
    *(node) = 0;
    v6 = NULL;
    if (!lstrcmpi(/* unsupported instruction */ - 2320, "PlayerOnScreen:"))
        v6 = &g_10207f12;
    if (!lstrcmpi(/* unsupported instruction */ - 2320, "GmDetected:"))
        v6 = &g_10207f15;
    if (!lstrcmpi(/* unsupported instruction */ - 2320, "PlayerAttacking:"))
        v6 = &g_10207f18;
    if (!lstrcmpi(/* unsupported instruction */ - 2320, "DefaultMessage:"))
        v6 = &g_10207f1b;
    if (!lstrcmpi(/* unsupported instruction */ - 2320, "PrivateMessage:"))
        v6 = &g_10207f1e;
    if (!lstrcmpi(/* unsupported instruction */ - 2320, "Disconnected:"))
        v6 = &g_10207f21;
    ptr = v6;
    if (!v6)
    {
        MessageBoxA(NULL, "Invalid alert name specified!", NULL, MB_APPLMODAL);
    }
    else
    {
        for (v1 = 0; *(iter) == 32; iter += 1);
        iter1 = /* unsupported instruction */ - 2320;
        do
        {
            v9 = *(iter);
        } while (*(iter) && v9 != 32 && (*(iter1) = v9, iter += 1, iter1 += 1, v9 != 58));
        *(iter1) = 0;
        v10 = /* unsupported instruction */ - 2320;
        v1 |= 0x202020;
        memset(ptr, 0, 3);
        if ((char)v1 == 115 || *((char *)&v1 + 1) == 115 || *((char *)&v1 + 2) == 115)
            *((char *)ptr) = 1;
        if (ptr != &g_10207f21 && ((char)v1 == 112 || *((char *)&v1 + 1) == 112 || *((char *)&v1 + 2) == 112))
            *((char *)&ptr[1]) = 1;
        v11 = 120;
        if (ptr == &g_10207f21)
            v11 = 114;
        if ((char)v1 == v11 || *((char *)&v1 + 1) == v11 || *((char *)&v1 + 2) == v11)
            *((char *)&ptr[2]) = 1;
    }
}
```

## `sub_10017289` `0x10017289`

_39 bytes. refs "\r\n"_

```c
extern int g_101f2ea8;

int sub_10017289(void)
{
    lstrcat(/* unsupported instruction */ - 2052, "\r\n");
    lstrcat(&g_101f2ea8, /* unsupported instruction */ - 2052);
}
```

## `sub_100172b0` `0x100172b0`

_5399 bytes. refs "Name:", "Count:", "Any"_

```c
typedef struct struct_1 {
    char padding_0[64];
    unsigned int field_40;
    unsigned int field_44;
    unsigned int field_48;
} struct_1;

typedef struct struct_2 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
    unsigned int field_10;
    unsigned int field_14;
    unsigned int field_18;
    char padding_1c[4];
    unsigned int field_20;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
    unsigned int field_30;
    unsigned int field_34;
    unsigned int field_38;
    unsigned int field_3c;
    char padding_40[32];
    unsigned int field_60;
} struct_2;

typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
    unsigned int field_10;
    unsigned int field_14;
    char field_18;
    char field_19;
} struct_0;

extern char g_10008a16;
extern int g_10042322;
extern int g_1004233a;
extern int g_10042394;
extern int g_100423c8;
extern int g_100424d2;
extern int g_100425a1;
extern int g_1004263d;
extern int g_1004350a;
extern int g_10043538;
extern int g_10043544;
extern int g_100435c8;
extern char g_1014f420;
extern char g_101d5e20;
extern char g_101d5e78;
extern unsigned int g_101dfe78;
extern unsigned int g_101dfe7c;
extern unsigned int g_101dfe80;
extern unsigned int g_101dfe84;
extern unsigned int g_101dfe88;
extern unsigned int g_101dfe8c;
extern unsigned int g_101dfe90;
extern unsigned int g_101dfe94;
extern char g_101dfe9c;
extern char g_101dfe9d;
extern char g_101dfe9e;
extern unsigned int g_101dfe9f;
extern char g_101dfea3;

int sub_100172b0(void)
{
    char v9[36];  // edi
    char *node;  // esi
    char *iter;  // edi
    char *iter1;  // esi
    unsigned int v76;  // eax
    char *iter2;  // edi
    unsigned int v78;  // eax
    char *i24;  // edi
    unsigned int v80;  // ebx
    int *i25;  // ebx
    unsigned int v82;  // eax
    char *i26;  // edi
    unsigned int v84;  // eax
    char *i27;  // edi
    unsigned int v86;  // eax
    char *i28;  // edi
    unsigned int v88;  // eax
    char *i29;  // edi
    unsigned int v90;  // ebx
    int *i30;  // ebx
    unsigned int v92;  // eax
    char *i31;  // edi
    unsigned int v94;  // ebx
    int *i32;  // ebx
    unsigned int v96;  // eax
    unsigned int v19;  // eax
    char *i33;  // edi
    unsigned int v98;  // eax
    char *i34;  // edi
    unsigned int v100;  // eax
    char *i35;  // edi
    unsigned int v20;  // eax
    char *l;  // edi
    unsigned int v22;  // eax
    char *m;  // edi
    char *v11;  // edi
    unsigned int v24;  // ebx
    int *n;  // ebx
    unsigned int v26;  // eax
    char *i0;  // edi
    unsigned int v28;  // ebx
    int *i1;  // ebx
    unsigned int v30;  // ebx
    int *i2;  // ebx
    char v12;  // cl
    unsigned int v32;  // ebx
    int *i3;  // ebx
    unsigned int v34;  // ebx
    int *i4;  // ebx
    unsigned int v36;  // ebx
    int *i5;  // ebx
    char *i6;  // esi
    char *v39;  // edi
    char v40;  // cl
    unsigned int v41;  // eax
    char *i7;  // edi
    unsigned int v43;  // eax
    char *i8;  // edi
    unsigned int v45;  // eax
    char *i9;  // edi
    char *v13;  // edi
    unsigned int v47;  // eax
    char *i10;  // edi
    unsigned int v49;  // eax
    char *i11;  // edi
    char v14;  // cl
    unsigned int v51;  // eax
    char *i12;  // edi
    char *i13;  // esi
    char *v54;  // edi
    char v55;  // cl
    unsigned int v56;  // eax
    unsigned int v15;  // ebx
    char *i14;  // edi
    unsigned int v58;  // eax
    char *i15;  // edi
    unsigned int v60;  // eax
    unsigned int v61;  // eax
    unsigned int j;  // ebx
    char *i16;  // edi
    char *v63;  // edi
    char v64;  // cl
    unsigned int v65;  // ebx
    char *i18;  // ebx
    unsigned int v67;  // ebx
    unsigned int v17;  // eax
    int *i19;  // ebx
    unsigned int v69;  // ebx
    int *i20;  // ebx
    unsigned int v71;  // eax
    char *i21;  // edi
    unsigned int v73;  // eax
    char *i22;  // edi
    unsigned int v0;  // [bp-0x4]
    unsigned int v2;  // [bp+0xff6e0]
    struct_0 *index;  // [bp+0xff6e4]
    char idx1[36];  // [bp+0xff6e8]
    char *idx;  // [bp+0xff6ec], Other Possible Types: struct_1 *
    struct_2 *idx2;  // [bp+0xff6f0], Other Possible Types: struct_1 *, unsigned int
    char v7;  // [bp+0xff6f4]

    if (idx < 0x7f)
    {
        v9 = 0x140 * idx + &g_101d5e78;
        *((char *[36])&idx1[0]) = v9;
        index = 96 + 0x38 * idx2 + (char *)v9;
        for (node = /* unsupported instruction */ - 2052; *(node) == 32; node += 1);
        v11 = /* unsupported instruction */ - 2320;
        do
        {
            v12 = *(node);
        } while (*(node) && v12 != 32 && (*(v11) = v12, node += 1, v11 += 1, v12 != 58));
        if (!lstrcmpi(/* unsupported instruction */ - 2320, "Name:"))
        {
            if (!v2)
            {
                idx = &idx->padding_0[1];
                *((char *[36])&idx1[0]) = &idx1[8 + 32];
            }
            for (v2 = 0; *(node) == 32; node += 1);
            lstrcpyn(idx1, node, 32);
        }
        else if (!lstrcmpi(/* unsupported instruction */ - 2320, "Count:"))
        {
            for (*(v11) = 0; *(node) == 32; node += 1);
            v13 = /* unsupported instruction */ - 2320;
            do
            {
                v14 = *(node);
            } while (*(node) && v14 != 32 && (*(v13) = v14, node += 1, v13 += 1, v14 != 58));
            *(v13) = 0;
            v0 = v15;
            for (j = "Any"; j < &g_10008a16; j += 4)
            {
                if (!lstrcmpi(/* unsupported instruction */ - 2320, j))
                {
                    idx1[33] = (char *)(-268470766 + j) >> 2;
                    break;
                }
            }
        }
        else if (!lstrcmpi(/* unsupported instruction */ - 2320, "LootMonster:"))
        {
            for (; *(node) == 32; node += 1);
            idx1[32] = ((*(node) | 32) == 121 ? 1 : 0);
        }
        else if (!lstrcmpi(/* unsupported instruction */ - 2320, "PlayAlarm:"))
        {
            for (; *(node) == 32; node += 1);
            idx1[35] = ((*(node) | 32) == 121 ? 1 : 0);
        }
        else if (!lstrcmpi(/* unsupported instruction */ - 2320, "Setting:"))
        {
            for (; *(node) == 32; node += 1);
            if ((*(node) < 48 || *(node) > 57) && *(node) != 45)
            {
                v17 = 0;
            }
            else
            {
                for (iter = /* unsupported instruction */ - 2320; *(node) && *(node) != 32; iter += 1)
                {
                    *(iter) = *(node);
                    node += 1;
                }
                *(iter) = 0;
                v17 = (v7 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
            }
            v19 = v17;
            if (!v17 || v19 > 4)
                v19 = 1;
            idx2 = v19 - 1;
        }
        else if (!lstrcmpi(/* unsupported instruction */ - 2320, "Hpmin:"))
        {
            for (; *(node) == 32; node += 1);
            if ((*(node) < 48 || *(node) > 57) && *(node) != 45)
            {
                v20 = 0;
            }
            else
            {
                for (l = /* unsupported instruction */ - 2320; *(node) && *(node) != 32; l += 1)
                {
                    *(l) = *(node);
                    node += 1;
                }
                *(l) = 0;
                v20 = (v7 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
            }
            if (v20 > 100)
                return sub_10017559();
            index->field_c = v20;
        }
        else if (!lstrcmpi(/* unsupported instruction */ - 2320, "Hpmax:"))
        {
            for (; *(node) == 32; node += 1);
            if ((*(node) < 48 || *(node) > 57) && *(node) != 45)
            {
                v22 = 0;
            }
            else
            {
                for (m = /* unsupported instruction */ - 2320; *(node) && *(node) != 32; m += 1)
                {
                    *(m) = *(node);
                    node += 1;
                }
                *(m) = 0;
                v22 = (v7 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
            }
            if (v22 > 100)
                return sub_100175e1();
            index->field_8 = v22;
        }
        else if (!lstrcmpi(/* unsupported instruction */ - 2320, "MonsterAttacks:"))
        {
            for (; *(node) == 32; node += 1);
            v0 = v24;
            for (n = &g_10043538; n < &g_10043544; n += 1)
            {
                if (!lstrcmpi(node, *(n)))
                {
                    index->field_4 = n - &g_10043538 >> 2;
                    break;
                }
            }
        }
        else if (!lstrcmpi(/* unsupported instruction */ - 2320, "Danger:"))
        {
            for (; *(node) == 32; node += 1);
            if ((*(node) < 48 || *(node) > 57) && *(node) != 45)
            {
                v26 = 0;
            }
            else
            {
                for (i0 = /* unsupported instruction */ - 2320; *(node) && *(node) != 32; i0 += 1)
                {
                    *(i0) = *(node);
                    node += 1;
                }
                *(i0) = 0;
                v26 = (v7 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
            }
            if (v26 > 10)
                return sub_100176bf();
            index->field_0 = v26;
        }
        else if (!lstrcmpi(/* unsupported instruction */ - 2320, "Stance:"))
        {
            for (; *(node) == 32; node += 1);
            v0 = v28;
            for (i1 = &g_100424d2; i1 < "No change"; i1 += 1)
            {
                if (!lstrcmpi(node, *(i1)))
                {
                    index->field_10 = i1 - &g_100424d2 >> 2;
                    break;
                }
            }
        }
        else if (!lstrcmpi(/* unsupported instruction */ - 2320, "ActionAttack:"))
        {
            for (; *(node) == 32; node += 1);
            v0 = v30;
            for (i2 = &g_1004350a; i2 < "Don't avoid"; i2 += 1)
            {
                if (!lstrcmpi(node, *(i2)))
                {
                    index->field_14 = index->field_14 | (i2 - &g_1004350a >> 2) * 64;
                    break;
                }
            }
        }
        else if (!lstrcmpi(/* unsupported instruction */ - 2320, "ActionSpell:"))
        {
            for (; *(node) == 32; node += 1);
            v0 = v32;
            for (i3 = &g_10043544; i3 < &g_100435c8; i3 += 1)
            {
                if (!lstrcmpi(node, *(i3)))
                {
                    index->field_14 = index->field_14 | i3 - &g_10043544 >> 2;
                    break;
                }
            }
        }
        else if (!lstrcmpi(/* unsupported instruction */ - 2320, "AttackMode:"))
        {
            for (; *(node) == 32; node += 1);
            v0 = v34;
            for (i4 = &g_1004263d; i4 < "\r\n"; i4 += 1)
            {
                if (!lstrcmpi(node, *(i4)))
                {
                    index->field_19 = i4 - &g_1004263d >> 2;
                    break;
                }
            }
        }
        else if (!lstrcmpi(/* unsupported instruction */ - 2320, "Ring:"))
        {
            for (; *(node) == 32; node += 1);
            v0 = v36;
            for (i5 = &g_100425a1; i5 < "No change"; i5 += 1)
            {
                if (!lstrcmpi(node, *(i5)))
                {
                    index->field_18 = i5 - &g_100425a1 >> 2;
                    break;
                }
            }
        }
    }
    for (i6 = /* unsupported instruction */ - 2052; *(i6) == 32; i6 += 1);
    v39 = /* unsupported instruction */ - 2320;
    do
    {
        v40 = *(i6);
    } while (*(i6) && v40 != 32 && (*(v39) = v40, i6 += 1, v39 += 1, v40 != 58));
    if (!lstrcmpi(/* unsupported instruction */ - 2320, "ListOrder:"))
    {
        for (*(v39) = 0; *(i6) == 32; i6 += 1);
        if ((*(i6) < 48 || *(i6) > 57) && *(i6) != 45)
        {
            v41 = 0;
        }
        else
        {
            for (i7 = /* unsupported instruction */ - 2320; *(i6) && *(i6) != 32; i7 += 1)
            {
                *(i7) = *(i6);
                i6 += 1;
            }
            *(i7) = 0;
            v41 = (v7 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
        }
        if (v41 > 100)
            v41 = 100;
        g_101dfe78 = v41;
    }
    else if (!lstrcmpi(/* unsupported instruction */ - 2320, "Health:"))
    {
        for (; *(i6) == 32; i6 += 1);
        if ((*(i6) < 48 || *(i6) > 57) && *(i6) != 45)
        {
            v43 = 0;
        }
        else
        {
            for (i8 = /* unsupported instruction */ - 2320; *(i6) && *(i6) != 32; i8 += 1)
            {
                *(i8) = *(i6);
                i6 += 1;
            }
            *(i8) = 0;
            v43 = (v7 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
        }
        if (v43 > 100)
            v43 = 100;
        g_101dfe7c = v43;
    }
    else if (!lstrcmpi(/* unsupported instruction */ - 2320, "Proximity:"))
    {
        for (; *(i6) == 32; i6 += 1);
        if ((*(i6) < 48 || *(i6) > 57) && *(i6) != 45)
        {
            v45 = 0;
        }
        else
        {
            for (i9 = /* unsupported instruction */ - 2320; *(i6) && *(i6) != 32; i9 += 1)
            {
                *(i9) = *(i6);
                i6 += 1;
            }
            *(i9) = 0;
            v45 = (v7 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
        }
        if (v45 > 100)
            v45 = 100;
        g_101dfe80 = v45;
    }
    else if (!lstrcmpi(/* unsupported instruction */ - 2320, "Danger:"))
    {
        for (; *(i6) == 32; i6 += 1);
        if ((*(i6) < 48 || *(i6) > 57) && *(i6) != 45)
        {
            v47 = 0;
        }
        else
        {
            for (i10 = /* unsupported instruction */ - 2320; *(i6) && *(i6) != 32; i10 += 1)
            {
                *(i10) = *(i6);
                i6 += 1;
            }
            *(i10) = 0;
            v47 = (v7 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
        }
        if (v47 > 100)
            v47 = 100;
        g_101dfe84 = v47;
    }
    else if (!lstrcmpi(/* unsupported instruction */ - 2320, "Random:"))
    {
        for (; *(i6) == 32; i6 += 1);
        if ((*(i6) < 48 || *(i6) > 57) && *(i6) != 45)
        {
            v49 = 0;
        }
        else
        {
            for (i11 = /* unsupported instruction */ - 2320; *(i6) && *(i6) != 32; i11 += 1)
            {
                *(i11) = *(i6);
                i6 += 1;
            }
            *(i11) = 0;
            v49 = (v7 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
        }
        if (v49 > 100)
            v49 = 100;
        g_101dfe88 = v49;
    }
    else if (!lstrcmpi(/* unsupported instruction */ - 2320, "Stick:"))
    {
        for (; *(i6) == 32; i6 += 1);
        if ((*(i6) < 48 || *(i6) > 57) && *(i6) != 45)
        {
            v51 = 0;
        }
        else
        {
            for (i12 = /* unsupported instruction */ - 2320; *(i6) && *(i6) != 32; i12 += 1)
            {
                *(i12) = *(i6);
                i6 += 1;
            }
            *(i12) = 0;
            v51 = (v7 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
        }
        if (v51 > 100)
            v51 = 100;
        g_101dfe8c = v51;
    }
    else if (!lstrcmpi(/* unsupported instruction */ - 2320, "TargetReachable:"))
    {
        for (; *(i6) == 32; i6 += 1);
        g_101dfe9d = ((*(i6) | 32) == 121 ? 1 : 0);
    }
    else if (!lstrcmpi(/* unsupported instruction */ - 2320, "TargetShootable:"))
    {
        for (; *(i6) == 32; i6 += 1);
        g_101dfe9c = ((*(i6) | 32) == 121 ? 1 : 0);
    }
    else
    {
        for (i13 = /* unsupported instruction */ - 2052; *(i13) == 32; i13 += 1);
        v54 = /* unsupported instruction */ - 2320;
        do
        {
            v55 = *(i13);
        } while (*(i13) && v55 != 32 && (*(v54) = v55, i13 += 1, v54 += 1, v55 != 58));
        if (!lstrcmpi(/* unsupported instruction */ - 2320, "RangeDistance:"))
        {
            for (*(v54) = 0; *(i13) == 32; i13 += 1);
            if ((*(i13) < 48 || *(i13) > 57) && *(i13) != 45)
            {
                v56 = 0;
            }
            else
            {
                for (i14 = /* unsupported instruction */ - 2320; *(i13) && *(i13) != 32; i14 += 1)
                {
                    *(i14) = *(i13);
                    i13 += 1;
                }
                *(i14) = 0;
                v56 = (v7 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
            }
            if (v56 < 2)
                v56 = 2;
            if (v56 > 9)
                v56 = 9;
            g_101dfe90 = v56 - 2;
        }
        else if (!lstrcmpi(/* unsupported instruction */ - 2320, "AttackFrequency:"))
        {
            for (; *(i13) == 32; i13 += 1);
            if ((*(i13) < 48 || *(i13) > 57) && *(i13) != 45)
            {
                v58 = 0;
            }
            else
            {
                for (i15 = /* unsupported instruction */ - 2320; *(i13) && *(i13) != 32; i15 += 1)
                {
                    *(i15) = *(i13);
                    i13 += 1;
                }
                *(i15) = 0;
                v58 = (v7 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
            }
            v60 = (unsigned int)(v58 / 100) - 1;
            if (v60 > 299)
                v60 = 299;
            g_101dfe94 = v60;
        }
        else if (!lstrcmpi(/* unsupported instruction */ - 2320, "IgnoreMonsters:"))
        {
            for (; *(i13) == 32; i13 += 1);
            if (!lstrcmpi(i13, "Don't"))
                g_101dfe9f = 0;
            for (; *(i13) == 32; i13 += 1);
            if ((*(i13) < 48 || *(i13) > 57) && *(i13) != 45)
            {
                v61 = 0;
            }
            else
            {
                for (i16 = /* unsupported instruction */ - 2320; *(i13) && *(i13) != 32; i16 += 1)
                {
                    *(i16) = *(i13);
                    i13 += 1;
                }
                *(i16) = 0;
                v61 = (v7 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
            }
            g_101dfe9f = v61;
        }
        else if (!lstrcmpi(/* unsupported instruction */ - 2320, "SyncSpell:"))
        {
            for (; *(i13) == 32; i13 += 1);
            g_101dfea3 = ((*(i13) | 32) == 121 ? 1 : 0);
        }
        else if (!lstrcmpi(/* unsupported instruction */ - 2320, "AllowDiagonal:"))
        {
            for (; *(i13) == 32; i13 += 1);
            g_101dfe9e = ((*(i13) | 32) == 121 ? 1 : 0);
        }
        else
        {
            for (iter1 = /* unsupported instruction */ - 2052; *(iter1) == 32; iter1 += 1);
            v63 = /* unsupported instruction */ - 2320;
            do
            {
                v64 = *(iter1);
            } while (*(iter1) && v64 != 32 && (*(v63) = v64, iter1 += 1, v63 += 1, v64 != 58));
            if (!lstrcmpi(/* unsupported instruction */ - 2320, "Name:"))
            {
                for (*(v63) = 0; *(iter1) == 32; iter1 += 1);
                v0 = v65;
                for (i18 = &g_1014f420; i18 < &g_101d5e20; i18 += 4308)
                {
                    if (!*(i18))
                    {
                        lstrcpyn(i18, iter1, 32);
                        idx = i18;
                        break;
                    }
                    else
                    {
                        if (!lstrcmpi(i18, iter1))
                        {
                            idx = i18;
                            break;
                        }
                    }
                }
                idx2 = 0;
            }
            else if (idx)
            {
                if (!lstrcmpi(/* unsupported instruction */ - 2320, "Enabled:"))
                {
                    for (; *(iter1) == 32; iter1 += 1);
                    idx->field_44 = ((*(iter1) | 32) == 121 ? 1 : 0);
                }
                else if (!lstrcmpi(/* unsupported instruction */ - 2320, "DrawAsBackground:"))
                {
                    for (; *(iter1) == 32; iter1 += 1);
                    idx->field_48 = ((*(iter1) | 32) == 121 ? 1 : 0);
                }
                else if (!lstrcmpi(/* unsupported instruction */ - 2320, "Size:"))
                {
                    for (; *(iter1) == 32; iter1 += 1);
                    v0 = v67;
                    for (i19 = &g_100423c8; i19 < "No Movement"; i19 += 1)
                    {
                        if (!lstrcmpi(iter1, *(i19)))
                        {
                            idx->field_40 = i19 - &g_100423c8 >> 2;
                            break;
                        }
                    }
                }
                else if (!lstrcmpi(/* unsupported instruction */ - 2320, "LeftCommand:"))
                {
                    for (; *(iter1) == 32; iter1 += 1);
                    lstrcpyn(idx + 1, iter1, 2000);
                }
                else if (!lstrcmpi(/* unsupported instruction */ - 2320, "RightCommand:"))
                {
                    for (; *(iter1) == 32; iter1 += 1);
                    lstrcpyn(&idx[27].padding_0[24], iter1, 2000);
                }
                else if (!lstrcmpi(/* unsupported instruction */ - 2320, "State:"))
                {
                    for (; *(iter1) == 32; iter1 += 1);
                    if (!lstrcmpi(iter1, "Inactive"))
                        idx2 = &idx[53].padding_0[48];
                    if (!lstrcmpi(iter1, "Active"))
                        idx2 = &idx[54].field_48;
                }
                else if (idx2)
                {
                    if (!lstrcmpi(/* unsupported instruction */ - 2320, "IconType:"))
                    {
                        for (; *(iter1) == 32; iter1 += 1);
                        v0 = v69;
                        for (i20 = &g_10042394; i20 < "Small"; i20 += 1)
                        {
                            if (!lstrcmpi(iter1, *(i20)))
                            {
                                idx2->field_0 = i20 - &g_10042394 >> 2;
                                break;
                            }
                        }
                    }
                    else if (!lstrcmpi(/* unsupported instruction */ - 2320, "IconIds:"))
                    {
                        for (; *(iter1) == 32; iter1 += 1);
                        if ((*(iter1) < 48 || *(iter1) > 57) && *(iter1) != 45)
                        {
                            v71 = 0;
                        }
                        else
                        {
                            for (i21 = /* unsupported instruction */ - 2320; *(iter1) && *(iter1) != 32; i21 += 1)
                            {
                                *(i21) = *(iter1);
                                iter1 += 1;
                            }
                            *(i21) = 0;
                            v71 = (v7 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
                        }
                        for (idx2->field_8 = v71; *(iter1) == 32; iter1 += 1);
                        if ((*(iter1) < 48 || *(iter1) > 57) && *(iter1) != 45)
                        {
                            v73 = 0;
                        }
                        else
                        {
                            for (i22 = /* unsupported instruction */ - 2320; *(iter1) && *(iter1) != 32; i22 += 1)
                            {
                                *(i22) = *(iter1);
                                iter1 += 1;
                            }
                            *(i22) = 0;
                            v73 = (v7 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
                        }
                        for (idx2->field_c = v73; *(iter1) == 32; iter1 += 1);
                        if ((*(iter1) < 48 || *(iter1) > 57) && *(iter1) != 45)
                        {
                            v76 = 0;
                        }
                        else
                        {
                            for (iter2 = /* unsupported instruction */ - 2320; *(iter1) && *(iter1) != 32; iter2 += 1)
                            {
                                *(iter2) = *(iter1);
                                iter1 += 1;
                            }
                            *(iter2) = 0;
                            v76 = (v7 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
                        }
                        for (idx2->field_10 = v76; *(iter1) == 32; iter1 += 1);
                        if ((*(iter1) < 48 || *(iter1) > 57) && *(iter1) != 45)
                        {
                            v78 = 0;
                        }
                        else
                        {
                            for (i24 = /* unsupported instruction */ - 2320; *(iter1) && *(iter1) != 32; i24 += 1)
                            {
                                *(i24) = *(iter1);
                                iter1 += 1;
                            }
                            *(i24) = 0;
                            v78 = (v7 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
                        }
                        idx2->field_14 = v78;
                    }
                    else if (!lstrcmpi(/* unsupported instruction */ - 2320, "BkgType:"))
                    {
                        for (; *(iter1) == 32; iter1 += 1);
                        v0 = v80;
                        for (i25 = &g_10042394; i25 < "Small"; i25 += 1)
                        {
                            if (!lstrcmpi(iter1, *(i25)))
                            {
                                idx2->field_18 = i25 - &g_10042394 >> 2;
                                break;
                            }
                        }
                    }
                    else if (!lstrcmpi(/* unsupported instruction */ - 2320, "BkgIds:"))
                    {
                        for (; *(iter1) == 32; iter1 += 1);
                        if ((*(iter1) < 48 || *(iter1) > 57) && *(iter1) != 45)
                        {
                            v82 = 0;
                        }
                        else
                        {
                            for (i26 = /* unsupported instruction */ - 2320; *(iter1) && *(iter1) != 32; i26 += 1)
                            {
                                *(i26) = *(iter1);
                                iter1 += 1;
                            }
                            *(i26) = 0;
                            v82 = (v7 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
                        }
                        for (idx2->field_20 = v82; *(iter1) == 32; iter1 += 1);
                        if ((*(iter1) < 48 || *(iter1) > 57) && *(iter1) != 45)
                        {
                            v84 = 0;
                        }
                        else
                        {
                            for (i27 = /* unsupported instruction */ - 2320; *(iter1) && *(iter1) != 32; i27 += 1)
                            {
                                *(i27) = *(iter1);
                                iter1 += 1;
                            }
                            *(i27) = 0;
                            v84 = (v7 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
                        }
                        for (idx2->field_24 = v84; *(iter1) == 32; iter1 += 1);
                        if ((*(iter1) < 48 || *(iter1) > 57) && *(iter1) != 45)
                        {
                            v86 = 0;
                        }
                        else
                        {
                            for (i28 = /* unsupported instruction */ - 2320; *(iter1) && *(iter1) != 32; i28 += 1)
                            {
                                *(i28) = *(iter1);
                                iter1 += 1;
                            }
                            *(i28) = 0;
                            v86 = (v7 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
                        }
                        for (idx2->field_28 = v86; *(iter1) == 32; iter1 += 1);
                        if ((*(iter1) < 48 || *(iter1) > 57) && *(iter1) != 45)
                        {
                            v88 = 0;
                        }
                        else
                        {
                            for (i29 = /* unsupported instruction */ - 2320; *(iter1) && *(iter1) != 32; i29 += 1)
                            {
                                *(i29) = *(iter1);
                                iter1 += 1;
                            }
                            *(i29) = 0;
                            v88 = (v7 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
                        }
                        idx2->field_2c = v88;
                    }
                    else if (!lstrcmpi(/* unsupported instruction */ - 2320, "AlignX:"))
                    {
                        for (; *(iter1) == 32; iter1 += 1);
                        v0 = v90;
                        for (i30 = &g_10042322; i30 < &g_1004233a; i30 += 1)
                        {
                            if (!lstrcmpi(iter1, *(i30)))
                            {
                                idx2->field_30 = i30 - &g_10042322 >> 2;
                                break;
                            }
                        }
                    }
                    else if (!lstrcmpi(/* unsupported instruction */ - 2320, "PositionX:"))
                    {
                        for (; *(iter1) == 32; iter1 += 1);
                        if ((*(iter1) < 48 || *(iter1) > 57) && *(iter1) != 45)
                        {
                            v92 = 0;
                        }
                        else
                        {
                            for (i31 = /* unsupported instruction */ - 2320; *(iter1) && *(iter1) != 32; i31 += 1)
                            {
                                *(i31) = *(iter1);
                                iter1 += 1;
                            }
                            *(i31) = 0;
                            v92 = (v7 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
                        }
                        idx2->field_34 = v92;
                    }
                    else if (!lstrcmpi(/* unsupported instruction */ - 2320, "AlignY:"))
                    {
                        for (; *(iter1) == 32; iter1 += 1);
                        v0 = v94;
                        for (i32 = &g_1004233a; i32 < "Normal"; i32 += 1)
                        {
                            if (!lstrcmpi(iter1, *(i32)))
                            {
                                idx2->field_38 = i32 - &g_1004233a >> 2;
                                break;
                            }
                        }
                    }
                    else if (!lstrcmpi(/* unsupported instruction */ - 2320, "PositionY:"))
                    {
                        for (; *(iter1) == 32; iter1 += 1);
                        if ((*(iter1) < 48 || *(iter1) > 57) && *(iter1) != 45)
                        {
                            v96 = 0;
                        }
                        else
                        {
                            for (i33 = /* unsupported instruction */ - 2320; *(iter1) && *(iter1) != 32; i33 += 1)
                            {
                                *(i33) = *(iter1);
                                iter1 += 1;
                            }
                            *(i33) = 0;
                            v96 = (v7 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
                        }
                        idx2->field_3c = v96;
                    }
                    else if (!lstrcmpi(/* unsupported instruction */ - 2320, "Text:"))
                    {
                        if (*(iter1) == 32)
                            iter1 += 1;
                        lstrcpyn(idx2->padding_40, iter1, 32);
                    }
                    else if (!lstrcmpi(/* unsupported instruction */ - 2320, "TextColor:"))
                    {
                        for (; *(iter1) == 32; iter1 += 1);
                        if ((*(iter1) < 48 || *(iter1) > 57) && *(iter1) != 45)
                        {
                            v98 = 0;
                        }
                        else
                        {
                            for (i34 = /* unsupported instruction */ - 2320; *(iter1) && *(iter1) != 32; i34 += 1)
                            {
                                *(i34) = *(iter1);
                                iter1 += 1;
                            }
                            *(i34) = 0;
                            v98 = (v7 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
                        }
                        idx2->field_60 = v98;
                    }
                    else
                    {
                        if (lstrcmpi(/* unsupported instruction */ - 2320, "HoverColor:"))
                            goto LABEL_0x100187d6;
                        for (; *(iter1) == 32; iter1 += 1);
                        if ((*(iter1) < 48 || *(iter1) > 57) && *(iter1) != 45)
                        {
                            v100 = 0;
                        }
                        else
                        {
                            for (i35 = /* unsupported instruction */ - 2320; *(iter1) && *(iter1) != 32; i35 += 1)
                            {
                                *(i35) = *(iter1);
                                iter1 += 1;
                            }
                            *(i35) = 0;
                            v100 = (v7 == 45 ? ~(sub_10040900(/* unsupported instruction */ - 2319)) + 1 : sub_10040900(/* unsupported instruction */ - 2320));
                        }
                        idx2->field_4 = v100;
                    }
                }
            }
        }
    }
}
```

## `sub_10017559` `0x10017559`

_5 bytes. (leaf/helper — see body)_

```c
int sub_10017559(void)
{
}
```

## `sub_100175e1` `0x100175e1`

_5 bytes. (leaf/helper — see body)_

```c
int sub_100175e1(void)
{
}
```

## `sub_100176bf` `0x100176bf`

_5 bytes. (leaf/helper — see body)_

```c
int sub_100176bf(void)
{
}
```

## `sub_100188bf` `0x100188bf`

_58 bytes. calls SendDlgItemMessageA, SendMessageA_

```c
LRESULT sub_100188bf(HWND a0, int a1, unsigned int len, WPARAM a3, LPARAM a4)
{
    SendDlgItemMessageA(a0, a1, len, a3, a4);
    return SendMessageA(a0, 273, a1 & 0xffff | 0x10000, a4);
}
```

## `sub_100188f9` `0x100188f9`

_1169 bytes. calls SendDlgItemMessageA; refs "[Waypoints]\r\n", "%c %d %d %d", "\r\n"_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    char padding_c[32];
    unsigned short field_2c;
    unsigned short field_2e;
} struct_0;

extern char g_10054e34;
extern char g_10054e54;
extern HWND g_10072fa4;
extern unsigned int g_101e6ea8[4];
extern char g_101f2ea8;
extern unsigned int g_10202f06;
extern struct_0 g_10202f0a;
extern unsigned int g_10207f0a;
extern unsigned int g_10207f0e;
extern char g_10207f12;
extern char g_10207f13;
extern char g_10207f14;
extern char g_10207f15;
extern char g_10207f16;
extern char g_10207f17;
extern char g_10207f18;
extern char g_10207f19;
extern char g_10207f1a;
extern char g_10207f1b;
extern char g_10207f1c;
extern char g_10207f1d;
extern char g_10207f1e;
extern char g_10207f1f;
extern char g_10207f20;
extern char g_10207f21;
extern char g_10207f23;
extern char g_10207f33;
extern char g_10207f34;
extern char g_10207f35;
extern int g_10207f36;
extern char g_10207f3b;

HGLOBAL sub_100188f9(void)
{
    unsigned int i;  // ebx
    struct_0 *idx;  // ebx
    char v20;  // cl
    char v22;  // cl
    char v24;  // cl
    char v26;  // cl
    unsigned short *v28;  // ebx
    unsigned int v13;  // ecx
    unsigned int v14;  // ecx
    struct_0 *j;  // ebx
    struct_0 *v16;  // ebx
    unsigned int k;  // ecx
    char v18;  // cl
    unsigned int v0;  // [bp-0xa4]
    unsigned int v1;  // [bp-0xa0]
    unsigned int v2;  // [bp-0x9c]
    struct_0 *v3;  // [bp-0x98], Other Possible Types: unsigned int
    unsigned int v4;  // [bp-0x94]
    HGLOBAL v5;  // [bp-0x90]
    unsigned int v6;  // [bp-0x8c]
    Byte v7;  // [bp-0x88]
    char v8;  // [bp-0x87]
    unsigned short *v9;  // [bp-0x8]

    v5 = GlobalAlloc(GMEM_FIXED, 0x200000);
    v9 = GlobalLock(v5);
    if (g_10202f06)
    {
        lstrcpy(v9, "[Waypoints]\r\n");
        for (i = 0; i < g_10202f06; i += 1)
        {
            v4 = i;
            idx = &g_101e6ea8[12 * i];
            v3 = idx->field_8;
            v2 = idx->field_4;
            v1 = idx->field_0;
            v0 = *((char *)(idx->field_2c + sub_10015d9a));
            wsprintfA(&v7, "%c %d %d %d");
            if (idx->padding_c[0])
            {
                lstrcat(&v7, " ");
                lstrcat(&v7, idx->padding_c);
            }
            lstrcat(&v7, "\r\n");
            lstrcat(v9, &v7);
            if (idx->field_2c == 5)
            {
                v13 = idx->field_2e;
                if (v13)
                {
                    v3 = (v13 - 1) * 0x1000;
                    lstrcat(v9, "\r\n");
                    lstrcat(v9, &(&g_10207f3b)[0x1000 + 0x1000 * v13]);
                    lstrcat(v9, "\r\n\r\n");
                }
            }
        }
    }
    v14 = 0;
    v6 = 0;
    for (j = &g_10202f0a.field_0; v14 < 500; j = &j->padding_c[8])
    {
        v14 += 1;
        if ((short)j->field_0 || *((char *)&j->field_0 + 2) || *((char *)&j->field_0 + 3))
            v6 = v14;
    }
    if (v6)
    {
        lstrcat(v9, "\r\n[Looting]\r\n");
        v16 = &g_10202f0a.field_0;
        for (k = 0; k < v6; k += 1)
        {
            v4 = k;
            if ((short)v16->field_0 || *((char *)&v16->field_0 + 2) || *((char *)&v16->field_0 + 3))
            {
                v3 = v16;
                sub_10016073(&v7, v16);
                if (v7 == 48)
                    lstrcat(v9, &v8);
                else
                    lstrcat(v9, &v7);
                lstrcat(v9, "\r\n");
            }
            v16 = &v16->padding_c[8];
        }
    }
    lstrcat(v9, "\r\n[CavebotOptions]\r\n");
    lstrcat(v9, "Rope: ");
    if (!g_10207f0a)
        lstrcat(v9, "Rope");
    else
        lstrcat(v9, "Elvenhair rope");
    lstrcat(v9, "\r\nShovel: ");
    if (!g_10207f0e)
        lstrcat(v9, "Shovel");
    else
        lstrcat(v9, "Light Shovel");
    lstrcat(v9, "\r\nSkipNearbyNodes: ");
    sub_10040940(g_10207f36, &v7);
    lstrcat(v9, &v7);
    lstrcat(v9, "\r\nOpenNextBp: ");
    if (g_10207f35)
        lstrcat(v9, "yes");
    else
        lstrcat(v9, "no");
    lstrcat(v9, "\r\nLootNearbyTargets: ");
    if (g_10207f34)
        lstrcat(v9, "yes");
    else
        lstrcat(v9, "no");
    lstrcat(v9, "\r\nLootDistantTargets: ");
    if (g_10207f33)
        lstrcat(v9, "yes");
    else
        lstrcat(v9, "no");
    lstrcat(v9, "\r\n\r\n[Alerts]\r\n");
    lstrcat(v9, "PlayerOnScreen: ");
    v18 = (char)(g_10207f12 * 2) | g_10207f13;
    lstrcat(v9, &(&g_10054e34)[4 * _INSERT(v18 * 2, 0, (char)(v18 * 2) | g_10207f14)]);
    lstrcat(v9, "\r\nGmDetected: ");
    v20 = (char)(g_10207f15 * 2) | g_10207f16;
    lstrcat(v9, &(&g_10054e34)[4 * _INSERT(v20 * 2, 0, (char)(v20 * 2) | g_10207f17)]);
    lstrcat(v9, "\r\nPlayerAttacking: ");
    v22 = (char)(g_10207f18 * 2) | g_10207f19;
    lstrcat(v9, &(&g_10054e34)[4 * _INSERT(v22 * 2, 0, (char)(v22 * 2) | g_10207f1a)]);
    lstrcat(v9, "\r\nDefaultMessage: ");
    v24 = (char)(g_10207f1b * 2) | g_10207f1c;
    lstrcat(v9, &(&g_10054e34)[4 * _INSERT(v24 * 2, 0, (char)(v24 * 2) | g_10207f1d)]);
    lstrcat(v9, "\r\nPrivateMessage: ");
    v26 = (char)(g_10207f1e * 2) | g_10207f1f;
    lstrcat(v9, &(&g_10054e34)[4 * _INSERT(v26 * 2, 0, (char)(v26 * 2) | g_10207f20)]);
    lstrcat(v9, "\r\nDisconnected: ");
    lstrcat(v9, &(&g_10054e54)[4 * (g_10207f21 * 4 | g_10207f23)]);
    if (g_101f2ea8)
    {
        lstrcat(v9, "\r\n\r\n[CavebotHotkeys]\r\n");
        lstrcat(v9, &g_101f2ea8);
        lstrcat(v9, "\r\n");
    }
    v28 = v9;
    if (*(v28) == 2573)
        v28 += 1;
    SendDlgItemMessageA(g_10072fa4, 1002, 12, NULL, v28);
    GlobalUnlock(v5);
    return GlobalFree(v5);
}
```

## `sub_10018d8a` `0x10018d8a`

_1559 bytes. calls SendDlgItemMessageA; refs "[TargetingMonsters]", "\r\nName: ", "\r\nCount: "_

```c
extern unsigned int g_100424d2[4];
extern unsigned int g_100425a1[4];
extern unsigned int g_1004263d[4];
extern unsigned int g_1004350a[4];
extern unsigned int g_10043538[4];
extern unsigned int g_10043544[4];
extern HWND g_10072fa8;
extern void g_101d5e78;
extern void g_101dfe78;
extern int g_101dfe7c;
extern int g_101dfe80;
extern int g_101dfe84;
extern int g_101dfe88;
extern int g_101dfe8c;
extern unsigned int g_101dfe90;
extern unsigned int g_101dfe94;
extern char g_101dfe9c;
extern char g_101dfe9d;
extern char g_101dfe9e;
extern int g_101dfe9f;
extern char g_101dfea3;

HGLOBAL sub_10018d8a(void)
{
    void* i;  // ebx
    unsigned int idx;  // ebx
    unsigned int v0[4];  // [bp-0x11c], Other Possible Types: unsigned int
    void* v1;  // [bp-0x118]
    HGLOBAL v2;  // [bp-0x114]
    unsigned int v3;  // [bp-0x110]
    unsigned int iter;  // [bp-0x10c]
    Byte v5[256];  // [bp-0x108]
    unsigned int v6;  // [bp-0x8]

    v2 = GlobalAlloc(GMEM_FIXED, 0x200000);
    v6 = GlobalLock(v2);
    v3 = 0;
    for (i = &g_101d5e78; i < &g_101dfe78; i += 320)
    {
        if (*((char *)i))
        {
            if (!v3)
                lstrcpy(v6, "[TargetingMonsters]");
            v3 = 1;
            lstrcat(v6, "\r\nName: ");
            lstrcat(v6, i);
            lstrcat(v6, "\r\nCount: ");
            lstrcat(v6, 268470766 + 4 * (char)i[33]);
            lstrcat(v6, "\r\nLootMonster: ");
            if ((char)i[32])
                lstrcat(v6, "yes");
            else
                lstrcat(v6, "no");
            lstrcat(v6, "\r\nPlayAlarm: ");
            if ((char)i[35])
                lstrcat(v6, "yes");
            else
                lstrcat(v6, "no");
            lstrcat(v6, "\r\n");
            iter = 0;
            while (iter < 4)
            {
                v1 = i;
                idx = i + iter * 56 + 96;
                if (!*((int *)(idx + 8)) && !*((int *)(idx + 12)) && !*((int *)idx) && !*((int *)(idx + 4)) && !*((int *)(idx + 16)) && !*((int *)(idx + 20)) && !*((char *)(idx + 24)) && !*((char *)(idx + 25)))
                {
                    iter += 1;
                }
                else
                {
                    v0 = iter + 1;
                    wsprintfA(v5, "\r\nSetting: %d");
                    lstrcat(v6, v5);
                    v0 = *((int *)(idx + 12));
                    wsprintfA(v5, "\r\nHpmin: %d");
                    lstrcat(v6, v5);
                    v0 = *((int *)(idx + 8));
                    wsprintfA(v5, "\r\nHpmax: %d");
                    lstrcat(v6, v5);
                    v0 = g_10043538[*((int *)(idx + 4))];
                    wsprintfA(v5, "\r\nMonsterAttacks: %s");
                    lstrcat(v6, v5);
                    v0 = *((int *)idx);
                    wsprintfA(v5, "\r\nDanger: %d");
                    lstrcat(v6, v5);
                    v0 = g_100424d2[*((int *)(idx + 16))];
                    wsprintfA(v5, "\r\nStance: %s");
                    lstrcat(v6, v5);
                    v0 = g_1004350a[*((int *)(idx + 20)) >> 6];
                    wsprintfA(v5, "\r\nActionAttack: %s");
                    lstrcat(v6, v5);
                    v0 = g_10043544[*((int *)(idx + 20)) & 63];
                    wsprintfA(v5, "\r\nActionSpell: %s");
                    lstrcat(v6, v5);
                    v0 = g_1004263d[*((char *)(idx + 25))];
                    wsprintfA(v5, "\r\nAttackMode: %s");
                    lstrcat(v6, v5);
                    v0 = g_100425a1[*((char *)(idx + 24))];
                    wsprintfA(v5, "\r\nRing: %s");
                    lstrcat(v6, v5);
                    lstrcat(v6, "\r\n");
                    iter += 1;
                }
            }
        }
    }
    if (v3)
        lstrcat(v6, "\r\n");
    lstrcat(v6, "[TargetSelection]");
    lstrcat(v6, "\r\nListOrder: ");
    sub_10040940(*((int *)&g_101dfe78), v5);
    lstrcat(v6, v5);
    lstrcat(v6, "\r\nHealth: ");
    sub_10040940(g_101dfe7c, v5);
    lstrcat(v6, v5);
    lstrcat(v6, "\r\nProximity: ");
    sub_10040940(g_101dfe80, v5);
    lstrcat(v6, v5);
    lstrcat(v6, "\r\nDanger: ");
    sub_10040940(g_101dfe84, v5);
    lstrcat(v6, v5);
    lstrcat(v6, "\r\nRandom: ");
    sub_10040940(g_101dfe88, v5);
    lstrcat(v6, v5);
    lstrcat(v6, "\r\nStick: ");
    sub_10040940(g_101dfe8c, v5);
    lstrcat(v6, v5);
    lstrcat(v6, "\r\nTargetReachable: ");
    if (g_101dfe9d)
        lstrcat(v6, "yes");
    else
        lstrcat(v6, "no");
    lstrcat(v6, "\r\nTargetShootable: ");
    if (g_101dfe9c)
        lstrcat(v6, "yes");
    else
        lstrcat(v6, "no");
    lstrcat(v6, "\r\n\r\n[StanceOptions]");
    lstrcat(v6, "\r\nRangeDistance: ");
    sub_10040940(g_101dfe90 + 2, v5);
    lstrcat(v6, v5);
    lstrcat(v6, "\r\nAttackFrequency: ");
    sub_10040940((g_101dfe94 + 1) * 100, v5);
    lstrcat(v6, v5);
    lstrcat(v6, "\r\nIgnoreMonsters: ");
    sub_10040940(g_101dfe9f, v5);
    lstrcat(v6, v5);
    lstrcat(v6, "\r\nSyncSpell: ");
    if (g_101dfea3)
        lstrcat(v6, "yes");
    else
        lstrcat(v6, "no");
    lstrcat(v6, "\r\nAllowDiagonal: ");
    if (g_101dfe9e)
        lstrcat(v6, "yes");
    else
        lstrcat(v6, "no");
    SendDlgItemMessageA(g_10072fa8, 1002, 12, NULL, v6);
    GlobalUnlock(v2);
    return GlobalFree(v2);
}
```

## `sub_100193a1` `0x100193a1`

_944 bytes. calls SendDlgItemMessageA; refs "[Icons]", "\r\nName: ", "\r\nEnabled: "_

```c
typedef struct struct_0 {
    char field_0;
    char padding_1[63];
    unsigned int field_40;
    unsigned int field_44;
    unsigned int field_48;
    char padding_4c[4000];
    unsigned int field_fec;
    unsigned int field_ff0;
    unsigned int field_ff4;
    unsigned int field_ff8;
    unsigned int field_ffc;
    unsigned int field_1000;
    unsigned int field_1004;
    char padding_1008[4];
    unsigned int field_100c;
    unsigned int field_1010;
    unsigned int field_1014;
    unsigned int field_1018;
    unsigned int field_101c;
    unsigned int field_1020;
    unsigned int field_1024;
    unsigned int field_1028;
    char padding_102c[32];
    unsigned int field_104c;
} struct_0;

extern unsigned int g_10042322[4];
extern unsigned int g_1004233a[4];
extern unsigned int g_10042394[4];
extern unsigned int g_100423c8[4];
extern HWND g_10072fac;
extern struct_0 g_1014f420;
extern struct_0 g_101d5e20;

HGLOBAL sub_100193a1(void)
{
    struct_0 *i;  // ebx
    struct_0 *iter;  // ebx
    unsigned int v0;  // [bp-0x12c]
    unsigned int v1;  // [bp-0x128]
    unsigned int v2;  // [bp-0x124]
    struct_0 *v3;  // [bp-0x120], Other Possible Types: unsigned int [4], unsigned int
    struct_0 *v4;  // [bp-0x11c], Other Possible Types: unsigned int [4]
    unsigned int v5;  // [bp-0x118]
    unsigned int v6;  // [bp-0x114]
    HGLOBAL v7;  // [bp-0x110]
    Byte v8[256];  // [bp-0x108]
    unsigned int v9;  // [bp-0x8]

    v6 = 0;
    v7 = GlobalAlloc(GMEM_FIXED, 0x200000);
    v9 = GlobalLock(v7);
    for (i = &g_1014f420.field_0; i < &g_101d5e20.field_0; i = &i[1].padding_4c[56])
    {
        if (i->field_0)
        {
            if (!v6)
            {
                lstrcpy(v9, "[Icons]");
                v6 = 1;
            }
            lstrcat(v9, "\r\nName: ");
            lstrcat(v9, i);
            lstrcat(v9, "\r\nEnabled: ");
            if (i->field_44)
                lstrcat(v9, "yes");
            else
                lstrcat(v9, "no");
            lstrcat(v9, "\r\nDrawAsBackground: ");
            if (i->field_48)
                lstrcat(v9, "yes");
            else
                lstrcat(v9, "no");
            v4 = g_100423c8[i->field_40];
            wsprintfA(v8, "\r\nSize: %s");
            lstrcat(v9, v8);
            lstrcat(v9, "\r\nLeftCommand: ");
            lstrcat(v9, i->padding_4c);
            lstrcat(v9, "\r\nRightCommand: ");
            lstrcat(v9, &i->padding_4c[2000]);
            lstrcat(v9, "\r\n");
            v5 = 0;
            v4 = i;
            iter = &i->field_fec;
            lstrcat(v9, "\r\nState: Inactive");
            while (true)
            {
                v3 = g_10042394[*((int *)&iter->field_0)];
                wsprintfA(v8, "\r\nIconType: %s");
                lstrcat(v9, v8);
                v3 = *((int *)&iter->padding_1[19]);
                v2 = *((int *)&iter->padding_1[15]);
                v1 = *((int *)&iter->padding_1[11]);
                v0 = *((int *)&iter->padding_1[7]);
                wsprintfA(v8, "\r\nIconIds: %d %d %d %d");
                lstrcat(v9, v8);
                v3 = g_10042394[*((int *)&iter->padding_1[23])];
                wsprintfA(v8, "\r\nBkgType: %s");
                lstrcat(v9, v8);
                v3 = *((int *)&iter->padding_1[43]);
                v2 = *((int *)&iter->padding_1[39]);
                v1 = *((int *)&iter->padding_1[35]);
                v0 = *((int *)&iter->padding_1[31]);
                wsprintfA(v8, "\r\nBkgIds: %d %d %d %d");
                lstrcat(v9, v8);
                v3 = g_10042322[*((int *)&iter->padding_1[47])];
                wsprintfA(v8, "\r\nAlignX: %s");
                lstrcat(v9, v8);
                v3 = *((int *)&iter->padding_1[0x33]);
                wsprintfA(v8, "\r\nPositionX: %d");
                lstrcat(v9, v8);
                v3 = g_1004233a[*((int *)&iter->padding_1[55])];
                wsprintfA(v8, "\r\nAlignY: %s");
                lstrcat(v9, v8);
                v3 = *((int *)&iter->padding_1[59]);
                wsprintfA(v8, "\r\nPositionY: %d");
                lstrcat(v9, v8);
                v3 = &iter->field_40;
                wsprintfA(v8, "\r\nText: %s");
                lstrcat(v9, v8);
                v3 = *((int *)&iter->padding_4c[20]);
                wsprintfA(v8, "\r\nTextColor: %d");
                lstrcat(v9, v8);
                v3 = *((int *)&iter->padding_1[3]);
                wsprintfA(v8, "\r\nHoverColor: %d");
                lstrcat(v9, v8);
                lstrcat(v9, "\r\n");
                if (v5)
                    break;
                lstrcat(v9, "\r\nState: Active");
                iter = &iter->padding_4c[24];
                v5 = 1;
            }
        }
    }
    SendDlgItemMessageA(g_10072fac, 1002, 12, NULL, v9);
    GlobalUnlock(v7);
    return GlobalFree(v7);
}
```

## dlgProc_Cavebot `0x10019751`

Named — see [doc 10](../../10-*.md). _4014 bytes. calls SendDlgItemMessageA; refs "<NewEntry>"_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    char field_c;
    char padding_d[31];
    unsigned short field_2c;
    unsigned short field_2e;
} struct_0;

typedef struct struct_1 {
    unsigned short field_0;
    char field_2;
} struct_1;

extern unsigned int g_10052768;
extern unsigned int g_1005276c;
extern unsigned int g_10052770;
extern HWND g_10072f94;
extern int g_10072f98;
extern int g_10072f9c;
extern int g_10072fa4;
extern unsigned int g_10072fb4;
extern char g_100f0d3a;
extern char g_100f0e44;
extern int g_100f42a8;
extern int g_100f45c5;
extern int g_101e6ea8;
extern LRESULT g_10202f06;
extern unsigned short g_10202f0a[4];
extern char g_10202f1e;
extern char g_10207ac6;
extern unsigned int g_10207f0a;
extern unsigned int g_10207f0e;
extern char g_10207f33;
extern char g_10207f34;
extern char g_10207f35;
extern unsigned int g_10207f36;
extern char g_10207f3b[4];

int sub_10019751(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    int len;  // eax
    struct_0 *v19;  // eax
    LRESULT count;  // eax
    unsigned int v21;  // esi
    unsigned int v22;  // edi
    struct_0 *idx;  // eax
    void* count1;  // eax
    void* count2;  // eax
    int v26;  // ebx
    LRESULT v27;  // eax
    int v28;  // ebx
    unsigned long v11;  // ldt
    void* v29;  // eax
    unsigned int v30;  // ebx
    unsigned short v31[24];  // eax
    unsigned int v32;  // ecx
    LRESULT v33;  // eax
    LRESULT v34;  // eax
    struct_1 *v35;  // ebx
    unsigned int v36;  // ecx
    LRESULT v37;  // eax
    void* v38;  // eax
    unsigned long v12;  // gdt
    void* index;  // ebx
    unsigned int v40;  // eax
    void* v41;  // eax
    unsigned int v42;  // ebx
    LRESULT v43;  // eax
    unsigned short v44[24];  // ebx
    HWND v45;  // eax
    unsigned int v46;  // eax
    char *v47;  // eax
    unsigned int v48;  // eax
    unsigned short v13;  // ss
    LRESULT v49;  // eax
    unsigned short idx1[24];  // ebx
    unsigned int v51;  // eax
    char *v52;  // eax
    unsigned int i;  // ecx
    unsigned int v54;  // eax
    void* v55;  // eax
    LRESULT v56;  // eax
    LRESULT v57;  // eax
    LRESULT v58;  // eax
    unsigned long v14;  // 4131
    unsigned long v15;  // 4125
    int v16;  // ebx
    LRESULT v17;  // eax
    unsigned int v18;  // ecx
    unsigned int v0;  // [bp-0x24c]
    struct_0 *v1;  // [bp-0x248], Other Possible Types: unsigned int
    unsigned short v2;  // [bp-0x246]
    unsigned int v3;  // [bp-0x240]
    void* v4;  // [bp-0x23c]
    char v5;  // [bp-0x238]
    char v6;  // [bp-0x209]
    LRESULT v7;  // [bp-0x208], Other Possible Types: void*
    int <0x10019751[is_3]|Stack bp-0x208, 1 B>;  // [bp-0x208]
    int v8[128];  // [bp-0x204], Other Possible Types: void*, int *, unsigned int, char, unsigned short

    if (a1 == 272)
    {
        v3 = a0;
        g_10072f94 = a0;
        sub_10015da3();
        sub_100160d6();
        sub_100162e3();
        ShowWindow(GetDlgItem(g_10072f94, 1011), SW_SHOW);
        SendDlgItemMessageA(g_10072f94, 1011, 12, NULL, "A new bot for Tibia called\r\nNeoBot has been developed\r\nby the maker of ElfBot.\r\nVisit www.tibianeobot.com\r\nfor more information!");
        SendDlgItemMessageA(g_10072f94, 0x404, 390, NULL, NULL);
        SendDlgItemMessageA(g_10072f94, 1035, 390, NULL, NULL);
        return 0;
    }
    else if (a1 == 563)
    {
        DragQueryFile(a2, 0, &v8, 0x200);
        len = lstrlen(&v8);
        if (len <= 0x5)
            return 0;
        v14 = _ccall(v11, v12, (unsigned int)v13, &<0x10019751[is_3]|Stack bp-0x208, 1 B> + len);
        if ((*((int *)v14) | 0x20202020) == 1667656805 && !((v15 = (unsigned long)_ccall(v11, v12, (unsigned int)v13, &v6 + len), *((char *)(unsigned int)v15) != 46)))
        {
            g_100f0d3a = 1;
            sub_10015b79(&v8, 1);
            sub_100160d6();
            g_100f0d3a = 0;
            sub_100188bf(g_10072f94, 0x404, 390, NULL, NULL);
            sub_100188bf(g_10072f94, 1035, 390, NULL, NULL);
        }
        else
        {
            if ((*((int *)v14) | 0x20202000) == 1953527598)
            {
                g_100f0d3a = 1;
                sub_100167eb(&v8);
                sub_100160d6();
                g_100f0d3a = 0;
                sub_100188bf(g_10072f94, 0x404, 390, NULL, NULL);
                sub_100188bf(g_10072f94, 1035, 390, NULL, NULL);
            }
        }
        return 0;
    }
    else if (a1 == 273)
    {
        if ((unsigned short)a2 == 1048)
        {
            g_10072fb4 = 2;
            return sub_1001f57d(g_10072fa4, 16000, sub_100083b6);
        }
        else if (g_100f0d3a)
        {
            return 273;
        }
        else
        {
            v16 = (unsigned short)a2;
            if (v16 >= 1001 && v16 <= 1008)
            {
                if (g_10202f06 < 0x3e8)
                {
                    sub_1002ae81(&g_100f45c5, 0x400);
                    v7 = (char *)SendDlgItemMessageA(g_10072f94, 0x404, 398, NULL, NULL) + 1;
                    v17 = (char *)SendDlgItemMessageA(g_10072f94, 0x404, 392, NULL, NULL) + 1;
                    v8 = v17;
                    if (v17 <= g_10202f06)
                    {
                        v18 = (g_10202f06 - v17) * 48;
                        v19 = 0x30 * v17 + (char *)&g_101e6ea8;
                        while (true)
                        {
                            *(48 + v18 + (char *)v19) = *(v18 + (char *)v19);
                            if (!v18)
                                break;
                            v18 -= 1;
                        }
                    }
                    else
                    {
                        v19 = 0x30 * g_10202f06 + (char *)&g_101e6ea8;
                    }
                    v1 = v19;
                    count = SendDlgItemMessageA(g_10072f94, 1040, 392, NULL, NULL);
                    v21 = g_10052768;
                    v22 = g_1005276c;
                    if (count == 1)
                    {
                        v22 = g_1005276c - 1;
                    }
                    else if (count == 0x2)
                    {
                        v21 = g_10052768 + 1;
                    }
                    else if (count == 0x3)
                    {
                        v22 = g_1005276c + 1;
                    }
                    else if (count == 0x4)
                    {
                        v21 = g_10052768 - 1;
                    }
                    else if (count == 0x5)
                    {
                        v21 = g_10052768 - 1;
                        v22 = g_1005276c - 1;
                    }
                    else if (count == 0x6)
                    {
                        v21 = g_10052768 + 1;
                        v22 = g_1005276c - 1;
                    }
                    else if (count == 0x7)
                    {
                        v21 = g_10052768 + 1;
                        v22 = g_1005276c + 1;
                    }
                    else if (count == 0x8)
                    {
                        v21 = g_10052768 - 1;
                        v22 = g_1005276c + 1;
                    }
                    idx = v19;
                    v1 = v21;
                    idx->field_0 = v21;
                    v1 = v22;
                    idx->field_4 = v22;
                    v1 = g_10052770;
                    idx->field_8 = g_10052770;
                    v2 = v16 - 1000;
                    idx->field_2c = v2;
                    idx->field_2e = 0;
                    idx->field_c = 0;
                    g_100f0d3a = 1;
                    g_10202f06 = (char *)g_10202f06 + 1;
                    sub_100160d6();
                    SendDlgItemMessageA(g_10072f94, 0x404, 407, v7, NULL);
                    SendDlgItemMessageA(g_10072f94, 0x404, 390, v8, NULL);
                    g_100f0d3a = 0;
                    goto LABEL_1001a459;
                }
                else
                {
                    return 273;
                }
            }
            if (v16 == 1033)
            {
                count1 = SendDlgItemMessageA(g_10072f94, 1035, 392, NULL, NULL);
                if (count1 != 0xffffffff)
                {
                    v4 = count1;
                    count2 = SendDlgItemMessageA(g_10072f94, 1035, 395, NULL, NULL);
                    if (v4 + 1 < count2)
                    {
                        sub_1002ae6f(0x14 * v4 + (char *)&g_10202f0a[0], 0x14 * v4 + &g_10202f1e, (0x1ff - count2) * 20);
                        g_100f0d3a = 1;
                        SendDlgItemMessageA(g_10072f94, 1035, 386, v4, NULL);
                        g_100f0d3a = 0;
                        SendDlgItemMessageA(g_10072f94, 1035, 390, v4, NULL);
                    }
                }
            }
            else if (v16 == 1035)
            {
LABEL_10019bb5:
                v33 = SendDlgItemMessageA(g_10072f94, 1035, 395, NULL, NULL);
                if (v33 && v33 != 0xffffffff)
                {
                    v34 = SendDlgItemMessageA(g_10072f94, 1035, 392, NULL, NULL);
                    if (v34 != 0xffffffff)
                    {
                        g_100f0d3a = 1;
                        if ((char *)v33 + 1 == v34)
                        {
                            v8 = 0;
                            SendDlgItemMessageA(g_10072f94, 1032, 12, NULL, v8);
                            SendDlgItemMessageA(g_10072f94, 1031, 12, NULL, v8);
                            SendDlgItemMessageA(g_10072f94, 1029, 12, NULL, v8);
                        }
                        else
                        {
                            v35 = 0x14 * v34 + (char *)&g_10202f0a[0];
                            sub_10040940(v35->field_0, v8);
                            SendDlgItemMessageA(g_10072f94, 1032, 12, NULL, &v8);
                            v36 = v35->field_2;
                            if (v36 == 0xff)
                            {
                                v8 = 101;
                            }
                            else
                            {
                                if (v36 == 253)
                                {
                                    v8 = 103;
                                }
                                else
                                {
                                    if (v36 == 254)
                                        v8 = 12645;
                                    else
                                        sub_10040940(v36, &v8);
                                }
                            }
                            SendDlgItemMessageA(g_10072f94, 1031, 12, NULL, &v8);
                            SendDlgItemMessageA(g_10072f94, 1029, 12, NULL, v35 + 1);
                        }
                        g_100f0d3a = 0;
                    }
                }
            }
            else if (v16 == 1032 || v16 == 1031 || v16 == 1029)
            {
                v38 = SendDlgItemMessageA(g_10072f94, 1035, 392, NULL, NULL);
                if (v38 != 0xffffffff)
                {
                    g_100f0d3a = 1;
                    v4 = v38;
                    index = 0x14 * v38 + (char *)&g_10202f0a[0];
                    SendDlgItemMessageA(g_10072f94, 1032, 13, 0x20, &v8);
                    *((unsigned short *)index) = sub_10040900(&v8);
                    SendDlgItemMessageA(g_10072f94, 1031, 13, 0x20, &v8);
                    if (v8 == 101 || v8 == 69)
                    {
                        *((char *)&index[2]) = 255;
                    }
                    else
                    {
                        if (v8 == 103 || v8 == 71)
                        {
                            *((char *)&index[2]) = 253;
                        }
                        else
                        {
                            if (v8 == 12645 || v8 == 12613)
                            {
                                *((char *)&index[2]) = 254;
                            }
                            else
                            {
                                v40 = sub_10040900(&v8);
                                if (v40 > 15)
                                    v40 = 15;
                                *((char *)&index[2]) = v40;
                            }
                        }
                    }
                    SendDlgItemMessageA(g_10072f94, 1029, 13, 0x11, index + 3);
                    SendDlgItemMessageA(g_10072f94, 1035, 386, v4, NULL);
                    sub_10016073(&v8, index);
                    SendDlgItemMessageA(g_10072f94, 1035, 385, v4, &v8);
                    SendDlgItemMessageA(g_10072f94, 1035, 390, v4, NULL);
                    v41 = SendDlgItemMessageA(g_10072f94, 1035, 395, NULL, NULL);
                    if (v41 != 0xffffffff && v41 - 1 == v4)
                        SendDlgItemMessageA(g_10072f94, 1035, 385, 0xffffffff, "<NewEntry>");
                    g_100f0d3a = 0;
                }
            }
            else if (v16 == 1027)
            {
                v8 = SendDlgItemMessageA(g_10072f94, 0x404, 392, NULL, NULL);
                if (v8 != 0xffffffff && v8)
                {
                    v26 = 0x30 * v8 + (char *)&g_101e6ea8;
                    sub_1002ae6f(&v5, v26, 48);
                    sub_1002ae6f(v26, v26 - 48, 48);
                    sub_1002ae6f(v26 - 48, &v5, 48);
                    g_100f0d3a = 1;
                    sub_100160d6();
                    v8 = (char *)v8 + 1;
                    SendDlgItemMessageA(g_10072f94, 0x404, 390, v8, NULL);
                    g_100f0d3a = 0;
                    sub_1002ae81(&g_100f45c5, 0x400);
                }
            }
            else if (v16 == 1026)
            {
                v27 = SendDlgItemMessageA(g_10072f94, 0x404, 392, NULL, NULL);
                v8 = (char *)v27 + 1;
                if (v27 != 0xffffffff && v8 < g_10202f06)
                {
                    v28 = 0x30 * v27 + (char *)&g_101e6ea8;
                    sub_1002ae6f(&v5, v28, 48);
                    sub_1002ae6f(v28, v28 + 48, 48);
                    sub_1002ae6f(v28 + 48, &v5, 48);
                    g_100f0d3a = 1;
                    sub_100160d6();
                    SendDlgItemMessageA(g_10072f94, 0x404, 390, v8, NULL);
                    g_100f0d3a = 0;
                    sub_1002ae81(&g_100f45c5, 0x400);
                }
            }
            else if (v16 == 1038)
            {
                v8 = SendDlgItemMessageA(g_10072f94, 0x404, 392, NULL, NULL);
                if (v8 != 0xffffffff)
                {
                    v29 = v8;
                    if (v8)
                        v8 -= 1;
                    v30 = (g_10202f06 - v29 - 1) * 48;
                    v31 = 0x30 * v29 + (char *)&g_101e6ea8;
                    v32 = v31[23];
                    if (v31[22] == 5 && v32)
                    {
                        g_10207f3b[0x1000 + 0x1000 * v32] = 0;
                        v31[23] = 0;
                    }
                    sub_1002ae6f(v31, v31 + 1, v30);
                    g_10202f06 = (char *)g_10202f06 + 1;
                    g_100f0d3a = 1;
                    sub_100160d6();
                    SendDlgItemMessageA(g_10072f94, 0x404, 390, v8, NULL);
                    g_100f0d3a = 0;
                    sub_1002ae81(&g_100f45c5, 0x400);
                    goto LABEL_1001a459;
                }
            }
            else if (v16 == 1050)
            {
                SendDlgItemMessageA(g_10072f94, 1041, 13, 0x80, &v8);
                sub_100159fd(&v8);
                sub_100162e3();
            }
            else if (v16 == 1075)
            {
                sub_1002ae81(&g_100f45c5, 0x400);
                SendDlgItemMessageA(g_10072f94, 1041, 13, 0x80, &v8);
                sub_10015b79(&v8, 0);
                g_100f0d3a = 1;
                sub_100160d6();
                g_100f0d3a = 0;
                sub_100188bf(g_10072f94, 0x404, 390, NULL, NULL);
                sub_100188bf(g_10072f94, 1035, 390, NULL, NULL);
                sub_100162e3();
            }
            else if ((unsigned short)v16 == 1012)
            {
                SendDlgItemMessageA(g_10072f94, 1012, 240, NULL, NULL);
                sub_100163d8();
            }
            else if ((unsigned short)v16 == 0x3fc)
            {
                g_100f0e44 = (char)SendDlgItemMessageA(g_10072f94, 0x3fc, 240, NULL, NULL);
                v7 = SendDlgItemMessageA(g_10072f94, 0x404, 398, NULL, NULL);
                v8 = SendDlgItemMessageA(g_10072f94, 0x404, 392, NULL, NULL);
                sub_100160d6();
                SendDlgItemMessageA(g_10072f94, 0x404, 407, v7, NULL);
                SendDlgItemMessageA(g_10072f94, 0x404, 390, v8, NULL);
            }
            else if ((unsigned short)v16 == 1051)
            {
                sub_1002ae81(&g_100f45c5, 0x400);
                sub_1002ae81(&g_101e6ea8, 0xc000);
                sub_1002ae81(&g_10207f3b[0], 0x80000);
                g_10202f06 = 0;
                g_100f0d3a = 1;
                sub_100160d6();
                g_100f0d3a = 0;
                goto LABEL_10019bb5;
            }
            else if ((unsigned short)v16 == 1018)
            {
                sub_1001f57d(g_10072f98, 15000, sub_1000802f);
            }
            else if ((unsigned short)v16 == 1047)
            {
                g_10072fb4 = 0;
                sub_1001f57d(g_10072f9c, 16000, sub_100083b6);
            }
            else if ((unsigned short)v16 >= 1100 && (unsigned short)v16 <= 1117)
            {
                (&g_10207ac6)[v16] = (char)SendDlgItemMessageA(g_10072f94, v16, 240, NULL, NULL);
            }
            else if ((unsigned short)v16 == 0x400)
            {
                v37 = SendDlgItemMessageA(g_10072f94, 0x400, 240, NULL, NULL);
                g_10207f33 = *((char *)&v37);
                if (v37)
                    sub_1002ae81(&g_100f42a8, 0x300);
            }
            else if ((unsigned short)v16 == 1036)
            {
                g_10207f34 = (char)SendDlgItemMessageA(g_10072f94, 1036, 240, NULL, NULL);
            }
            else if ((unsigned short)v16 == 1037)
            {
                g_10207f35 = (char)SendDlgItemMessageA(g_10072f94, 1037, 240, NULL, NULL);
            }
            v42 = a2 >> 16;
            if ((unsigned short)a2 != 0x404 || v42 != 1)
            {
                if ((unsigned short)a2 == 1011 && v42 == 0x300)
                {
                    v49 = SendDlgItemMessageA(g_10072f94, 0x404, 392, NULL, NULL);
                    if (v49 == 0xffffffff)
                        return 0;
                    idx1 = 0x30 * v49 + (char *)&g_101e6ea8;
                    if (idx1[22] != 5)
                        return 0;
                    v51 = idx1[23];
                    if (v51)
                    {
                        v52 = &g_10207f3b[0x1000 + 0x1000 * v51];
                        v0 = &g_10207f3b[0x1000 + 0x1000 * v51];
                        SendDlgItemMessageA(g_10072f94, 1011, 13, 0x1000, v52);
                        if (!*(v52))
                            idx1[23] = 0;
                    }
                    else
                    {
                        for (i = 0; i < 0x80000; i += 0x1000)
                        {
                            if (!g_10207f3b[i])
                            {
                                v0 = i;
                                v54 = SendDlgItemMessageA(g_10072f94, 1011, 13, 0x1000, &g_10207f3b[i]);
                                idx1[23] = (i >> 12) + 1;
                                return v54;
                            }
                        }
                    }
                    return 0;
                }
                if ((unsigned short)a2 == 1009 && v42 == 1)
                {
                    v55 = SendDlgItemMessageA(g_10072f94, 1009, 392, NULL, NULL);
                    if (v55 == 0xffffffff)
                        return 0;
                    SendDlgItemMessageA(g_10072f94, 1009, 393, v55, &v8);
                    SendDlgItemMessageA(g_10072f94, 1041, 12, NULL, &v8);
                    return 0;
                }
                if ((unsigned short)a2 == 1015 && v42 == 1)
                {
                    v56 = SendDlgItemMessageA(g_10072f94, 1015, 392, NULL, NULL);
                    if (v56 == 0xffffffff)
                        return 0;
                    g_10207f0a = v56;
                    return 0;
                }
                if ((unsigned short)a2 == 1016 && v42 == 1)
                {
                    v57 = SendDlgItemMessageA(g_10072f94, 1016, 392, NULL, NULL);
                    if (v57 == 0xffffffff)
                        return 0;
                    g_10207f0e = v57;
                    return 0;
                }
                if ((unsigned short)a2 != 1042)
                {
                    return 0;
                }
                else if (v42 == 1)
                {
                    v58 = SendDlgItemMessageA(g_10072f94, 1042, 392, NULL, NULL);
                    if (v58 == 0xffffffff)
                        return 0;
                    g_10207f36 = v58;
                    return 0;
                }
                else
                {
                    return 0;
                }
            }
LABEL_1001a459:
            g_100f0d3a = 1;
            v43 = SendDlgItemMessageA(g_10072f94, 0x404, 392, NULL, NULL);
            if (v43 != 0xffffffff)
            {
                v44 = 0x30 * v43 + (char *)&g_101e6ea8;
                v45 = GetDlgItem(g_10072f94, 1011);
                if (v44[22] == 5)
                {
                    ShowWindow(v45, SW_SHOW);
                    v46 = v44[23];
                    if (v46)
                    {
                        v47 = &g_10207f3b[0x1000 + 0x1000 * v46];
                    }
                    else
                    {
                        v47 = &v8;
                        v8 = 0;
                    }
                    v48 = SendDlgItemMessageA(g_10072f94, 1011, 12, NULL, v47);
                }
                else
                {
                    v48 = ShowWindow(v45, SW_HIDE);
                }
            }
            else
            {
                v48 = ShowWindow(GetDlgItem(g_10072f94, 1011), SW_HIDE);
            }
            g_100f0d3a = 0;
            return v48;
        }
    }
    else
    {
        if (a1 == 16)
        {
            ShowWindow(a0, SW_HIDE);
            return 0;
        }
        return (unsigned int)sub_10002c6e(a0, a1, a2, a3);
    }
}
```

## `sub_100199eb` `0x100199eb`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100199eb(void)
{
}
```

## `sub_10019adf` `0x10019adf`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10019adf(void)
{
}
```

## `sub_1001a136` `0x1001a136`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1001a136(void)
{
}
```

## `sub_1001a338` `0x1001a338`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1001a338(void)
{
}
```

## `sub_1001a50a` `0x1001a50a`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1001a50a(void)
{
}
```

## dlgProc_Targeting `0x1001a715`

Named — see [doc 10](../../10-*.md). _4037 bytes. calls SendDlgItemMessageA; refs "%d %d %d %s", "<New Monster>", "<New Monster>"_

```c
typedef struct struct_0 {
    char field_0;
    char padding_1[31];
    char field_20;
    char field_21;
    char padding_22[1];
    char field_23;
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
    char padding_30[48];
    WPARAM field_60;
    WPARAM field_64;
    int field_68;
    int field_6c;
    WPARAM field_70;
    unsigned int field_74;
    char field_78;
    char field_79;
} struct_0;

typedef struct struct_1 {
    char padding_0[96];
    LRESULT field_60;
    LRESULT field_64;
    unsigned int field_68;
    unsigned int field_6c;
    LRESULT field_70;
    unsigned int field_74;
    char field_78;
    char field_79;
} struct_1;

extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern unsigned int g_1005f85c;
extern HWND g_10072f8c;
extern int g_10072fa8;
extern unsigned int g_10072fb4;
extern char g_100f0d39;
extern char g_100f0d3b;
extern unsigned int g_100f0db0;
extern unsigned int g_100f0de0;
extern unsigned int g_100f4a05;
extern char g_101d5e78;
extern unsigned int g_101dfe78;
extern unsigned int g_101dfe7c;
extern unsigned int g_101dfe80;
extern unsigned int g_101dfe84;
extern unsigned int g_101dfe88;
extern unsigned int g_101dfe8c;
extern unsigned int g_101dfe90;
extern unsigned int g_101dfe94;
extern unsigned int g_101dfe98;
extern char g_101dfe9c;
extern char g_101dfe9d;
extern char g_101dfe9e;
extern unsigned int g_101dfe9f;
extern char g_101dfea3;
extern char g_101dfea4;
extern unsigned int g_101dfea5[3];
extern unsigned int g_101e6ea5[3];

int sub_1001a715(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    int len;  // eax
    unsigned long v16;  // ldt
    unsigned int v25;  // ecx
    struct_0 *v26;  // ebx
    struct_0 *idx;  // ebx
    struct_0 *count;  // eax
    struct_0 *v29;  // edi
    struct_0 *v30;  // esi
    struct_0 *v31;  // ebx
    struct_0 *v32;  // ebx
    LRESULT count1;  // eax
    struct_0 *v34;  // ebx
    unsigned long v17;  // gdt
    LRESULT count2;  // eax
    LRESULT v36;  // eax
    LRESULT v37;  // eax
    LRESULT v38;  // eax
    LRESULT v39;  // eax
    LRESULT v40;  // eax
    LRESULT v41;  // eax
    unsigned int v42;  // ebx
    struct_0 *idx1;  // ebx
    struct_0 *v44;  // ebx
    unsigned short v18;  // ss
    LRESULT v45;  // eax
    LRESULT v46;  // eax
    LRESULT v47;  // eax
    LRESULT v48;  // eax
    LRESULT v49;  // eax
    void* v50;  // eax
    unsigned int v51;  // ecx
    unsigned long v19;  // 4127
    unsigned long v20;  // 4125
    unsigned int iter[3];  // ebx
    void* v22;  // eax
    void* v23;  // eax
    LRESULT v24;  // eax
    struct_0 *v0;  // [bp-0x368]
    unsigned int v1;  // [bp-0x364]
    int v2;  // [bp-0x360], Other Possible Types: unsigned int
    int v3;  // [bp-0x35c], Other Possible Types: unsigned int
    unsigned int v4[3];  // [bp-0x358], Other Possible Types: unsigned int
    void* v5;  // [bp-0x354]
    char v6;  // [bp-0x350]
    struct_0 *v7;  // [bp-0x210], Other Possible Types: struct_1 *
    struct_0 *idx2;  // [bp-0x20c]
    char v9;  // [bp-0x209]
    struct_0 *v10;  // [bp-0x208]
    int <0x1001a715[is_3]|Stack bp-0x208, 1 B>;  // [bp-0x208]
    char v11;  // [bp-0x204], Other Possible Types: unsigned int
    unsigned int v12;  // [bp-0x200]
    unsigned int v13;  // [bp-0x1fc]
    unsigned int v14;  // [bp-0x1f8]

    if (a1 == 272)
    {
        v4 = a0;
        g_10072f8c = a0;
        268470910();
        sub_10015267();
        sub_100188bf(g_10072f8c, 0x404, 390, NULL, NULL);
        sub_100188bf(g_10072f8c, 1040, 390, NULL, NULL);
        sub_100188bf(g_10072f8c, 1057, 390, NULL, NULL);
        return 0;
    }
    else if (a1 == 563)
    {
        DragQueryFile(a2, 0, &v11, 0x200);
        len = lstrlen(&v11);
        if (len <= 5)
            return 0;
        v19 = _ccall(v16, v17, (unsigned int)v18, &<0x1001a715[is_3]|Stack bp-0x208, 1 B> + len);
        if ((*((int *)v19) | 0x20202020) != 1952869477)
            return 0;
        v20 = _ccall(v16, v17, (unsigned int)v18, &v9 + len);
        if (*((char *)v20) == 46)
        {
            sub_10015843(&v11, 1);
            sub_10015267(a2, 0);
            sub_100188bf(g_10072f8c, 0x404, 390, NULL, NULL);
            sub_100188bf(g_10072f8c, 1040, 390, NULL, NULL);
        }
        return 0;
    }
    else if (a1 == 273)
    {
        if ((unsigned short)a2 == 1071)
        {
            g_10072fb4 = 3;
            return sub_1001f57d(g_10072fa8, 16000, sub_100083b6);
        }
        else if (g_100f0d39)
        {
            return 0;
        }
        else
        {
            if ((unsigned short)a2 == 1050 && g_1005f854)
            {
                for (iter = &g_101dfea5[0]; iter < &g_101e6ea5[0]; iter = &iter[2 + 1])
                {
                    if (!iter[0])
                    {
                        v4 = g_1005f854;
                        iter[0] = g_1005f854;
                        v4 = g_1005f858;
                        iter[1] = g_1005f858;
                        v4 = g_1005f85c;
                        iter[2] = g_1005f85c;
                        SendDlgItemMessageA(g_10072f8c, 1064, 13, 0x10, iter + 1);
                        v4 = iter + 1;
                        v3 = iter[2];
                        v2 = iter[1];
                        v1 = iter[0];
                        wsprintfA(&v11, "%d %d %d %s");
                        return SendDlgItemMessageA(g_10072f8c, 1062, 385, 0xffffffff, &v11);
                    }
                }
                return a1;
            }
            if ((unsigned short)a2 == 1065)
            {
                v3 = 0;
                v2 = 392;
                v22 = SendDlgItemMessageA(g_10072f8c, 1062, 392, NULL, NULL);
                if (v22 != 0xffffffff)
                {
                    v5 = v22;
                    v3 = 0;
                    v2 = 395;
                    v23 = SendDlgItemMessageA(g_10072f8c, 1062, 395, NULL, NULL);
                    if (v5 + 1 <= v23)
                    {
                        v2 = 0x1c * v5 + (char *)&g_101dfea5[0];
                        v3 = v2 + 28;
                        sub_1002ae6f(v2, v3, (0x3ff - v23) * 28);
                        SendDlgItemMessageA(g_10072f8c, 1062, 386, v5, NULL);
                        SendDlgItemMessageA(g_10072f8c, 1062, 390, v5, NULL);
                    }
                }
            }
            g_100f0db0 = (char *)SendDlgItemMessageA(g_10072f8c, 0x404, 395, NULL, NULL) + 1;
            v10 = SendDlgItemMessageA(g_10072f8c, 0x404, 392, NULL, NULL);
            idx2 = 0x140 * v10 + &g_101d5e78;
            v1 = 0;
            v0 = NULL;
            v24 = SendDlgItemMessageA(g_10072f8c, 1040, 392, NULL, NULL);
            if (v24 == 0xffffffff)
            {
                v1 = 0;
                v0 = NULL;
                SendDlgItemMessageA(g_10072f8c, 1040, 390, NULL, NULL);
                v24 = NULL;
            }
            v7 = 96 + (char *)idx2 + 0x38 * v24;
            if (v10 != 0xffffffff)
            {
                v25 = (unsigned short)a2;
                if ((unsigned short)v25 == 1029)
                {
                    g_100f0d39 = 1;
                    v26 = idx2;
                    SendDlgItemMessageA(g_10072f8c, 1029, 13, 0x20, v26);
                    SendDlgItemMessageA(g_10072f8c, 0x404, 386, v10, NULL);
                    sub_10015228(&v11, v26);
                    SendDlgItemMessageA(g_10072f8c, 0x404, 385, v10, &v11);
                    SendDlgItemMessageA(g_10072f8c, 0x404, 390, v10, NULL);
                    v1 = 0;
                    v0 = NULL;
                    if ((char *)SendDlgItemMessageA(g_10072f8c, 0x404, 395, NULL, NULL) + 1 == v10)
                    {
                        v1 = "<New Monster>";
                        v0 = 0xffffffff;
                        SendDlgItemMessageA(g_10072f8c, 0x404, 385, 0xffffffff, "<New Monster>");
                    }
                    g_100f0d39 = 0;
                }
                else if ((unsigned short)v25 == 1075)
                {
                    v1 = 16;
                    v0 = &v11;
                    sub_1002ae81(&v11, 16);
                    SendDlgItemMessageA(g_10072f8c, 1075, 13, 0xd, &v11);
                    idx = idx2;
                    idx->field_24 = v11;
                    idx->field_28 = v12;
                    idx->field_2c = v13;
                }
                else if ((unsigned short)v25 == 1038)
                {
                    v1 = 0;
                    v0 = NULL;
                    count = SendDlgItemMessageA(g_10072f8c, 0x404, 395, NULL, NULL);
                    v0 = v0;
                    if (v10->padding_1 < count)
                    {
                        v29 = idx2;
                        v30 = &v29[2].padding_30[28];
                        v1 = (struct struct_0 *)(127 + -0x1 * count) * 320;
                        sub_1002ae6f(v29, v30, (struct struct_0 *)(127 + -0x1 * count) * 320);
                        SendDlgItemMessageA(g_10072f8c, 0x404, 386, v10, NULL);
                        g_100f0d39 = 1;
                        sub_10015267(v29, v30, (struct struct_0 *)(127 + -0x1 * count) * 320, v2, v3);
                        g_100f0d39 = 0;
                        v0 = v30;
                    }
                }
                else if ((unsigned short)v25 == 1026)
                {
                    v1 = 0;
                    v0 = NULL;
                    v0 = v0;
                    if (v10 < (char *)SendDlgItemMessageA(g_10072f8c, 0x404, 395, NULL, NULL) + 2)
                    {
                        v31 = idx2;
                        v1 = 320;
                        sub_1002ae6f(&v6, v31, 320);
                        sub_1002ae6f(v31, &v31[2].padding_30[28], 320);
                        sub_1002ae6f(&v31[2].padding_30[28], &v6, 320);
                        g_100f0d39 = 1;
                        sub_10015267((struct struct_0 *)&v31[2].padding_30[28], &v6, 320);
                        SendDlgItemMessageA(g_10072f8c, 0x404, 390, v10->padding_1, NULL);
                        g_100f0d39 = 0;
                        v0 = v31;
                    }
                }
                else if ((unsigned short)v25 == 1027)
                {
                    v1 = 0;
                    v0 = NULL;
                    v0 = v0;
                    if (v10 < (char *)SendDlgItemMessageA(g_10072f8c, 0x404, 395, NULL, NULL) + 1)
                    {
                        v0 = v0;
                        if (v10)
                        {
                            v32 = idx2;
                            v1 = 320;
                            sub_1002ae6f(&v6, v32, 320);
                            sub_1002ae6f(v32, &v32[2].padding_30[28], 320);
                            sub_1002ae6f(&v32[2].padding_30[28], &v6, 320);
                            g_100f0d39 = 1;
                            sub_10015267((struct struct_0 *)&v32[2].padding_30[28], &v6, 320);
                            SendDlgItemMessageA(g_10072f8c, 0x404, 390, v10->padding_1, NULL);
                            g_100f0d39 = 0;
                            v0 = v32;
                        }
                    }
                }
                else if ((unsigned short)v25 == 1032)
                {
                    v0 = 0x20;
                    SendDlgItemMessageA(g_10072f8c, 1032, 13, 0x20, &v11);
                    v1 = &v11;
                    *((unsigned int *)&v7->padding_0[12]) = sub_10040900(&v11);
                }
                else if ((unsigned short)v25 == 1034)
                {
                    v0 = 0x20;
                    SendDlgItemMessageA(g_10072f8c, 1034, 13, 0x20, &v11);
                    v1 = &v11;
                    *((unsigned int *)&v7->padding_0[8]) = sub_10040900(&v11);
                }
                else if ((unsigned short)v25 == 1057)
                {
                    v1 = 0;
                    v0 = NULL;
                    count1 = SendDlgItemMessageA(g_10072f8c, v25, 392, NULL, NULL);
                    v0 = v0;
                    if (count1 != 0xffffffff)
                    {
                        v34 = idx2;
                        v34->field_21 = *((char *)&count1);
                        SendDlgItemMessageA(g_10072f8c, 0x404, 386, v10, NULL);
                        sub_10015228(&v11, v34);
                        SendDlgItemMessageA(g_10072f8c, 0x404, 385, v10, &v11);
                        v1 = 0;
                        SendDlgItemMessageA(g_10072f8c, 0x404, 390, v10, NULL);
                        v0 = v10;
                    }
                }
                else if ((unsigned short)v25 == 1042)
                {
                    v1 = 0;
                    v0 = NULL;
                    count2 = SendDlgItemMessageA(g_10072f8c, v25, 392, NULL, NULL);
                    if (count2 != 0xffffffff)
                        *((LRESULT *)&v7->padding_0[4]) = count2;
                }
                else if ((unsigned short)v25 == 1058)
                {
                    v1 = 0;
                    v0 = NULL;
                    v36 = SendDlgItemMessageA(g_10072f8c, v25, 392, NULL, NULL);
                    if (v36 != 0xffffffff)
                        v7->padding_0[24] = *((char *)&v36);
                }
                else if ((unsigned short)v25 == 1070)
                {
                    v1 = 0;
                    v0 = NULL;
                    v37 = SendDlgItemMessageA(g_10072f8c, v25, 392, NULL, NULL);
                    if (v37 != 0xffffffff)
                        v7->padding_0[25] = *((char *)&v37);
                }
                else if ((unsigned short)v25 == 1017)
                {
                    v1 = 0;
                    v0 = NULL;
                    v38 = SendDlgItemMessageA(g_10072f8c, v25, 392, NULL, NULL);
                    if (v38 != 0xffffffff)
                        *((LRESULT *)&v7->padding_0[0]) = v38;
                }
                else if ((unsigned short)v25 == 1025)
                {
                    v1 = 0;
                    v0 = NULL;
                    v39 = SendDlgItemMessageA(g_10072f8c, v25, 392, NULL, NULL);
                    if (v39 != 0xffffffff)
                        *((LRESULT *)&v7->padding_0[16]) = v39;
                }
                else if ((unsigned short)v25 == 1041)
                {
                    v1 = 0;
                    v0 = NULL;
                    v40 = SendDlgItemMessageA(g_10072f8c, v25, 392, NULL, NULL);
                    if (v40 != 0xffffffff)
                    {
                        *((unsigned int *)&v7->padding_0[20]) = *((int *)&v7->padding_0[20]) & 63;
                        *((unsigned long *)&v7->padding_0[20]) = *((int *)&v7->padding_0[20]) | v40 * 64;
                    }
                }
                else if ((unsigned short)v25 == 1054)
                {
                    v1 = 0;
                    v0 = NULL;
                    v41 = SendDlgItemMessageA(g_10072f8c, v25, 392, NULL, NULL);
                    if (v41 != 0xffffffff)
                    {
                        *((unsigned int *)&v7->padding_0[20]) = *((int *)&v7->padding_0[20]) & 0xffffffc0;
                        *((unsigned long *)&v7->padding_0[20]) = *((int *)&v7->padding_0[20]) | v41;
                    }
                }
                else if ((unsigned short)v25 == 1053)
                {
                    v1 = 0;
                    v0 = NULL;
                    idx2->field_20 = (char)SendDlgItemMessageA(g_10072f8c, v25, 240, NULL, NULL);
                }
                else
                {
                    v0 = v0;
                    if ((unsigned short)v25 == 1060)
                    {
                        v1 = 0;
                        v0 = NULL;
                        idx2->field_23 = (char)SendDlgItemMessageA(g_10072f8c, v25, 240, NULL, NULL);
                    }
                }
            }
            v42 = a2 >> 16;
            if ((unsigned short)a2 == 0x404 && v42 == 1)
            {
                g_100f0d39 = 1;
                idx1 = idx2;
                SendDlgItemMessageA(g_10072f8c, 1029, 12, NULL, idx1);
                v11 = idx1->field_24;
                v12 = idx1->field_28;
                v13 = idx1->field_2c;
                v14 = 0;
                SendDlgItemMessageA(g_10072f8c, 1075, 12, NULL, &v11);
                SendDlgItemMessageA(g_10072f8c, 1040, 390, NULL, NULL);
                SendDlgItemMessageA(g_10072f8c, 1057, 390, idx1->field_21, NULL);
                SendDlgItemMessageA(g_10072f8c, 1053, 241, idx1->field_20, NULL);
                SendDlgItemMessageA(g_10072f8c, 1060, 241, idx1->field_23, NULL);
                v44 = &idx1->field_60;
            }
            else if ((unsigned short)a2 == 1040 && v42 == 1)
            {
                v45 = SendDlgItemMessageA(g_10072f8c, 1040, 392, NULL, NULL);
                if (v45 == 0xffffffff)
                    return 0;
                v44 = 96 + (char *)idx2 + 0x38 * v45;
                v7 = v44;
                g_100f0d39 = 1;
            }
            else
            {
                if ((unsigned short)a2 == 1013 && v42 == 1)
                {
                    v46 = SendDlgItemMessageA(g_10072f8c, 1013, 392, NULL, NULL);
                    if (v46 == 0xffffffff)
                        return 0;
                    g_101dfe90 = v46;
                    return 0;
                }
                if ((unsigned short)a2 == 1052 && v42 == 1)
                {
                    v47 = SendDlgItemMessageA(g_10072f8c, 1052, 392, NULL, NULL);
                    if (v47 == 0xffffffff)
                        return 0;
                    g_101dfe98 = v47;
                    return 0;
                }
                if ((unsigned short)a2 == 1047 && v42 == 1)
                {
                    v48 = SendDlgItemMessageA(g_10072f8c, 1047, 392, NULL, NULL);
                    if (v48 == 0xffffffff)
                        return 0;
                    g_101dfe94 = v48;
                    return 0;
                }
                if ((unsigned short)a2 == 1069 && v42 == 1)
                {
                    v49 = SendDlgItemMessageA(g_10072f8c, 1069, 392, NULL, NULL);
                    if (v49 == 0xffffffff)
                        return 0;
                    g_101dfe9f = v49;
                    return 0;
                }
                if ((unsigned short)a2 == 1009 && v42 == 1)
                {
                    v50 = SendDlgItemMessageA(g_10072f8c, 1009, 392, NULL, NULL);
                    if (v50 == 0xffffffff)
                        return 0;
                    SendDlgItemMessageA(g_10072f8c, 1009, 393, v50, &v11);
                    SendDlgItemMessageA(g_10072f8c, 1007, 12, NULL, &v11);
                    return 0;
                }
                if ((unsigned short)a2 == 1005)
                {
                    SendDlgItemMessageA(g_10072f8c, 1007, 13, 0x80, &v11);
                    sub_100156ce(&v11);
                    sub_10015267(v0);
                    return 0;
                }
                else if ((unsigned short)a2 == 1006)
                {
                    SendDlgItemMessageA(g_10072f8c, 1007, 13, 0x80, &v11);
                    sub_10015843(&v11, 0);
                    sub_10015267(v0, v1);
                    sub_100188bf(g_10072f8c, 0x404, 390, NULL, NULL);
                    sub_100188bf(g_10072f8c, 1040, 390, NULL, NULL);
                    return 0;
                }
                else if ((unsigned short)a2 == 1011)
                {
                    g_101dfe9c = (char)SendDlgItemMessageA(g_10072f8c, 1011, 240, NULL, NULL);
                    return 0;
                }
                else if ((unsigned short)a2 == 1073)
                {
                    g_101dfea3 = (char)SendDlgItemMessageA(g_10072f8c, 1073, 240, NULL, NULL);
                    return 0;
                }
                else if ((unsigned short)a2 == 1074)
                {
                    g_101dfea4 = (char)SendDlgItemMessageA(g_10072f8c, 1074, 240, NULL, NULL);
                    return 0;
                }
                else if ((unsigned short)a2 == 1012)
                {
                    g_101dfe9d = (char)SendDlgItemMessageA(g_10072f8c, 1012, 240, NULL, NULL);
                    return 0;
                }
                else if ((unsigned short)a2 == 1061)
                {
                    g_101dfe9e = (char)SendDlgItemMessageA(g_10072f8c, 1061, 240, NULL, NULL);
                    return 0;
                }
                else if ((unsigned short)a2 == 1046)
                {
                    if (SendDlgItemMessageA(g_10072f8c, 1046, 240, NULL, NULL))
                        g_100f0d3b = 1;
                    else
                        g_100f0d3b = 0;
                    g_100f0de0 = GetTickCount();
                    return 0;
                }
                else
                {
                    return 0;
                }
            }
            sub_10040940(*((int *)&v44->padding_1[11]), &v11);
            SendDlgItemMessageA(g_10072f8c, 1032, 12, NULL, &v11);
            sub_10040940(*((int *)&v44->padding_1[7]), &v11);
            SendDlgItemMessageA(g_10072f8c, 1034, 12, NULL, &v11);
            SendDlgItemMessageA(g_10072f8c, 1042, 390, *((int *)&v44->padding_1[3]), NULL);
            SendDlgItemMessageA(g_10072f8c, 1017, 390, *((int *)&v44->field_0), NULL);
            SendDlgItemMessageA(g_10072f8c, 1025, 390, *((int *)&v44->padding_1[15]), NULL);
            SendDlgItemMessageA(g_10072f8c, 1058, 390, v44->padding_1[23], NULL);
            SendDlgItemMessageA(g_10072f8c, 1070, 390, v44->padding_1[24], NULL);
            SendDlgItemMessageA(g_10072f8c, 1041, 390, *((int *)&v44->padding_1[19]) >> 6, NULL);
            SendDlgItemMessageA(g_10072f8c, 1054, 390, *((int *)&v44->padding_1[19]) & 63, NULL);
            g_100f4a05 = v44;
            g_100f0d39 = 0;
            return 0;
        }
    }
    else
    {
        if (a1 == 78)
        {
            v51 = (unsigned short)a2;
            if ((unsigned short)v51 == 1001)
            {
                g_101dfe78 = SendDlgItemMessageA(g_10072f8c, v51, 0x400, NULL, NULL);
                return 0;
            }
            if ((unsigned short)v51 == 1002)
            {
                g_101dfe7c = SendDlgItemMessageA(g_10072f8c, v51, 0x400, NULL, NULL);
                return 0;
            }
            if ((unsigned short)v51 == 1003)
            {
                g_101dfe80 = SendDlgItemMessageA(g_10072f8c, v51, 0x400, NULL, NULL);
                return 0;
            }
            if ((unsigned short)v51 == 1004)
            {
                g_101dfe84 = SendDlgItemMessageA(g_10072f8c, v51, 0x400, NULL, NULL);
                return 0;
            }
            if ((unsigned short)v51 == 1039)
            {
                g_101dfe88 = SendDlgItemMessageA(g_10072f8c, v51, 0x400, NULL, NULL);
                return 0;
            }
            if ((unsigned short)v51 == 1044)
            {
                g_101dfe8c = SendDlgItemMessageA(g_10072f8c, v51, 0x400, NULL, NULL);
                return 0;
            }
            return 0;
        }
        else if (a1 == 16)
        {
            ShowWindow(a0, SW_HIDE);
            return 0;
        }
        else
        {
            return (unsigned int)sub_10002c6e(a0, a1, a2, a3);
        }
    }
}
```

## `sub_1001b2af` `0x1001b2af`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1001b2af(void)
{
}
```

## `sub_1001b6df` `0x1001b6df`

_310 bytes. calls SendDlgItemMessageA_

```c
extern char g_10042322;
extern char g_1004233a;
extern char g_10042394;
extern char g_100423c8;
extern HWND g_10072f90;

LRESULT sub_1001b6df(void)
{
    unsigned int i;  // ebx
    LRESULT count;  // eax
    unsigned int j;  // ebx
    unsigned int k;  // ebx
    unsigned int l;  // ebx

    for (i = 0; i < 8; i += 4)
    {
        count = SendDlgItemMessageA(g_10072f90, 1057, 385, 0xffffffff, *((int *)&(&g_100423c8)[i]));
    }
    for (j = 0; j < 40; j += 4)
    {
        SendDlgItemMessageA(g_10072f90, 1006, 385, 0xffffffff, *((int *)&(&g_10042394)[j]));
        SendDlgItemMessageA(g_10072f90, 1058, 385, 0xffffffff, *((int *)&(&g_10042394)[j]));
        SendDlgItemMessageA(g_10072f90, 1011, 385, 0xffffffff, *((int *)&(&g_10042394)[j]));
        count = SendDlgItemMessageA(g_10072f90, 1049, 385, 0xffffffff, *((int *)&(&g_10042394)[j]));
    }
    for (k = 0; k < 24; k += 4)
    {
        SendDlgItemMessageA(g_10072f90, 1014, 385, 0xffffffff, *((int *)&(&g_10042322)[k]));
        count = SendDlgItemMessageA(g_10072f90, 1046, 385, 0xffffffff, *((int *)&(&g_10042322)[k]));
    }
    for (l = 0; l < 24; l += 4)
    {
        SendDlgItemMessageA(g_10072f90, 0x3fc, 385, 0xffffffff, *((int *)&(&g_1004233a)[l]));
        count = SendDlgItemMessageA(g_10072f90, 1042, 385, 0xffffffff, *((int *)&(&g_1004233a)[l]));
    }
    return count;
}
```

## `sub_1001b815` `0x1001b815`

_134 bytes. calls SendDlgItemMessageA; refs "<New Icon>"_

```c
extern HWND g_10072f90;
extern char g_1014f420;
extern char g_101d5e20;

LRESULT sub_1001b815(void)
{
    char *i;  // ebx

    SendDlgItemMessageA(g_10072f90, 0x404, 388, NULL, NULL);
    for (i = &g_1014f420; i < &g_101d5e20 && *(i); i += 4308)
    {
        SendDlgItemMessageA(g_10072f90, 0x404, 385, 0xffffffff, i);
    }
    SendDlgItemMessageA(g_10072f90, 0x404, 385, 0xffffffff, "<New Icon>");
    return sub_100188bf(g_10072f90, 0x404, 390, NULL, NULL);
}
```

## `sub_1001b89b` `0x1001b89b`

_35 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1001b89b(char *a0)
{
    return (*(a0) == 45 ? ~(sub_10040900(a0 + 1)) + 1 : sub_10040900(a0));
}
```

## dlgProc_SkinEditor `0x1001b8be`

Named — see [doc 10](../../10-*.md). _5096 bytes. calls SendDlgItemMessageA; refs "<New Icon>"_

```c
typedef struct struct_0 {
    char padding_0[64];
    WPARAM field_40;
    WPARAM field_44;
    WPARAM field_48;
    char padding_4c[4000];
    WPARAM field_fec;
    unsigned int field_ff0;
    int field_ff4;
    int field_ff8;
    int field_ffc;
    int field_1000;
    WPARAM field_1004;
    char padding_1008[4];
    int field_100c;
    int field_1010;
    int field_1014;
    int field_1018;
    WPARAM field_101c;
    int field_1020;
    WPARAM field_1024;
    int field_1028;
    char padding_102c[32];
    unsigned int field_104c;
    WPARAM field_1050;
    unsigned int field_1054;
    int field_1058;
    int field_105c;
    int field_1060;
    int field_1064;
    WPARAM field_1068;
    char padding_106c[4];
    int field_1070;
    int field_1074;
    int field_1078;
    int field_107c;
    WPARAM field_1080;
    int field_1084;
    WPARAM field_1088;
    int field_108c;
    char padding_1090[32];
    unsigned int field_10b0;
} struct_0;

extern unsigned int g_1005f60a;
extern HWND g_10072f90;
extern int g_10072fac;
extern unsigned int g_10072fb4;
extern char g_100f0d39;
extern unsigned int g_100f0d44;
extern unsigned int g_100f0d48;
extern unsigned int g_100f0d4c;
extern unsigned int g_100f0d50;
extern unsigned int g_100f0d54;
extern unsigned int g_100f0d58;
extern char g_100f0d68;
extern unsigned int g_100f0db4;
extern int g_1014f420;
extern char g_101d5e22;
extern char g_101d5e23;
extern char g_101d5e24;
extern char g_101d5e25;
extern char g_101d5e26;
extern unsigned int g_10289888;
extern unsigned int g_1028988c;
extern unsigned int g_10289890;
extern unsigned int g_10289894;

int sub_1001b8be(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v9;  // ecx
    unsigned int count;  // eax
    struct_0 *v19;  // ebx
    struct_0 *v20;  // ebx
    LRESULT count1;  // eax
    LRESULT count2;  // eax
    LRESULT v23;  // eax
    LRESULT v24;  // eax
    LRESULT v25;  // eax
    LRESULT v26;  // eax
    LRESULT v27;  // eax
    LRESULT v28;  // eax
    unsigned int v11;  // eax
    LRESULT v29;  // eax
    struct_0 *idx;  // ebx
    struct_0 *idx1;  // ebx
    struct_0 *idx2;  // ebx
    struct_0 *v33;  // ebx
    struct_0 *v34;  // ebx
    struct_0 *v35;  // ebx
    struct_0 *v36;  // ebx
    unsigned int v37;  // eax
    unsigned int v38;  // ecx
    unsigned int v12;  // eax
    unsigned int v39;  // eax
    unsigned int v40;  // eax
    unsigned int v41;  // eax
    unsigned int v13;  // eax
    unsigned int v14;  // eax
    struct_0 *v15;  // eax
    unsigned int v16;  // ecx
    struct_0 *v17;  // ebx
    void* v18;  // eax
    unsigned int v0;  // [bp-0x1398]
    unsigned int v1;  // [bp-0x1348]
    unsigned int v2;  // [bp-0x12ec]
    struct_0 *v3;  // [bp-0x12e8]
    struct_0 *index;  // [bp-0x12e4]
    char v5;  // [bp-0x12e0]
    struct_0 *v6;  // [bp-0x20c]
    void* v7;  // [bp-0x208]
    int v8[128];  // [bp-0x204], Other Possible Types: char

    if (a1 == 272)
    {
        v2 = a0;
        g_10072f90 = a0;
        sub_1001b6df();
        sub_1001b815();
        return 0;
    }
    else if (a1 != 273)
    {
        if (a1 == 307)
        {
            v37 = GetDlgItem(a0, 1069);
            v38 = g_10289888;
            if (a3 == v37 || !((v39 = (unsigned int)GetDlgItem(a0, 0x400), v38 = g_1028988c, a3 != GetDlgItem(a0, 0x400) && (v40 = (unsigned int)GetDlgItem(a0, 1070), v38 = g_10289890, a3 != GetDlgItem(a0, 1070) && (v41 = (unsigned int)GetDlgItem(a0, 1036), v38 = g_10289894, a3 != GetDlgItem(a0, 1036))))))
            {
                v2 = v38;
                SetTextColor(a2, 0xff0000);
                SetBkMode(a2, 1);
                SetBkColor(a2, 0);
                SelectObject(a2, CreateSolidBrush(v38));
                return 0;
            }
        }
        else
        {
            if (a1 == 16)
            {
                ShowWindow(a0, SW_HIDE);
                return 0;
            }
        }
        return (unsigned int)sub_10002c6e(a0, a1, a2, a3);
    }
    else if (g_100f0d39)
    {
        return 273;
    }
    else
    {
        v9 = (unsigned short)a2;
        if ((unsigned short)v9 == 0x3ff)
        {
            count = SendDlgItemMessageA(g_10072f90, v9, 240, NULL, NULL);
            g_101d5e22 = count;
            return count;
        }
        else if ((unsigned short)v9 == 1037)
        {
            v11 = SendDlgItemMessageA(g_10072f90, v9, 240, NULL, NULL);
            g_101d5e24 = v11;
            return v11;
        }
        else if ((unsigned short)v9 == 1068)
        {
            v12 = SendDlgItemMessageA(g_10072f90, v9, 240, NULL, NULL);
            g_101d5e23 = v12;
            return v12;
        }
        else if ((unsigned short)v9 == 1071)
        {
            v13 = SendDlgItemMessageA(g_10072f90, v9, 240, NULL, NULL);
            g_101d5e25 = v13;
            return v13;
        }
        else if ((unsigned short)v9 == 1074)
        {
            v14 = SendDlgItemMessageA(g_10072f90, v9, 240, NULL, NULL);
            g_101d5e26 = v14;
            return v14;
        }
        else
        {
            g_100f0db4 = (char *)SendDlgItemMessageA(g_10072f90, 0x404, 395, NULL, NULL) + 1;
            v7 = SendDlgItemMessageA(g_10072f90, 0x404, 392, NULL, NULL);
            v15 = 0x10d4 * v7 + (char *)&g_1014f420;
            v6 = v15;
            v3 = &v15->field_fec;
            g_10289888 = *((int *)&v3->padding_0[4]);
            g_1028988c = *((int *)&v3->padding_4c[20]);
            index = &v15->field_1050;
            g_10289890 = *((int *)&index->padding_0[4]);
            g_10289894 = *((int *)&index->padding_4c[20]);
            if (v7 != 0xffffffff)
            {
                v16 = (unsigned short)a2;
                if ((unsigned short)v16 == 1073)
                {
                    sub_1002ae6f(index, v3, 100);
                    sub_100188bf(a0, 0x404, 390, v7, NULL);
                }
                else if ((unsigned short)v16 == 1029)
                {
                    g_100f0d39 = 1;
                    v17 = v6;
                    SendDlgItemMessageA(g_10072f90, 1029, 13, 0x20, v17);
                    SendDlgItemMessageA(g_10072f90, 0x404, 386, v7, NULL);
                    SendDlgItemMessageA(g_10072f90, 0x404, 385, v7, v17);
                    SendDlgItemMessageA(g_10072f90, 0x404, 390, v7, NULL);
                    if ((char *)SendDlgItemMessageA(g_10072f90, 0x404, 395, NULL, NULL) + 1 == v7)
                        SendDlgItemMessageA(g_10072f90, 0x404, 385, 0xffffffff, "<New Icon>");
                    g_100f0d39 = 0;
                }
                else if ((unsigned short)v16 == 1038)
                {
                    v18 = SendDlgItemMessageA(g_10072f90, 0x404, 395, NULL, NULL);
                    if (v7 + 1 < v18)
                    {
                        sub_1002ae6f(v6, &v6[1].padding_0[32], (127 - v18) * 4308);
                        SendDlgItemMessageA(g_10072f90, 0x404, 386, v7, NULL);
                        g_100f0d39 = 1;
                        sub_1001b815();
                        g_100f0d39 = 0;
                    }
                }
                else if ((unsigned short)v16 == 1075)
                {
                    sub_1002ae81(&g_1014f420, 0x86a00);
                    sub_1001b815();
                }
                else if ((unsigned short)v16 == 1076)
                {
                    g_10072fb4 = 4;
                    sub_1001f57d(g_10072fac, 16000, sub_100083b6);
                }
                else if ((unsigned short)v16 == 1026)
                {
                    if (v7 < (char *)SendDlgItemMessageA(g_10072f90, 0x404, 395, NULL, NULL) + 2)
                    {
                        v19 = v6;
                        sub_1002ae6f(&v5, v19, 4308);
                        sub_1002ae6f(v19, &v19[1].padding_0[32], 4308);
                        sub_1002ae6f(&v19[1].padding_0[32], &v5, 4308);
                        g_100f0d39 = 1;
                        sub_1001b815();
                        SendDlgItemMessageA(g_10072f90, 0x404, 390, v7 + 1, NULL);
                        g_100f0d39 = 0;
                    }
                }
                else
                {
                    if ((unsigned short)v16 == 1027)
                    {
                        if (v7 < (char *)SendDlgItemMessageA(g_10072f90, 0x404, 395, NULL, NULL) + 1 && v7)
                        {
                            v20 = v6;
                            sub_1002ae6f(&v5, v20, 4308);
                            sub_1002ae6f(v20, &v20[1].padding_0[32], 4308);
                            sub_1002ae6f(&v20[1].padding_0[32], &v5, 4308);
                            g_100f0d39 = 1;
                            sub_1001b815();
                            SendDlgItemMessageA(g_10072f90, 0x404, 390, v7 - 1, NULL);
                            g_100f0d39 = 0;
                        }
                    }
                    else
                    {
                        if ((unsigned short)v16 == 1032)
                        {
                            SendDlgItemMessageA(g_10072f90, v16, 13, 0x20, &v8);
                            *((unsigned int *)&v3->padding_0[8]) = sub_1001b89b(&v8);
                        }
                        else if ((unsigned short)v16 == 1002)
                        {
                            SendDlgItemMessageA(g_10072f90, v16, 13, 0x20, &v8);
                            *((unsigned int *)&v3->padding_0[12]) = sub_1001b89b(&v8);
                        }
                        else if ((unsigned short)v16 == 1003)
                        {
                            SendDlgItemMessageA(g_10072f90, v16, 13, 0x20, &v8);
                            *((unsigned int *)&v3->padding_0[16]) = sub_1001b89b(&v8);
                        }
                        else if ((unsigned short)v16 == 1004)
                        {
                            SendDlgItemMessageA(g_10072f90, v16, 13, 0x20, &v8);
                            *((unsigned int *)&v3->padding_0[20]) = sub_1001b89b(&v8);
                        }
                        else if ((unsigned short)v16 == 1010)
                        {
                            SendDlgItemMessageA(g_10072f90, v16, 13, 0x20, &v8);
                            *((unsigned int *)&v3->padding_0[32]) = sub_1001b89b(&v8);
                        }
                        else if ((unsigned short)v16 == 1009)
                        {
                            SendDlgItemMessageA(g_10072f90, v16, 13, 0x20, &v8);
                            *((unsigned int *)&v3->padding_0[36]) = sub_1001b89b(&v8);
                        }
                        else if ((unsigned short)v16 == 1008)
                        {
                            SendDlgItemMessageA(g_10072f90, v16, 13, 0x20, &v8);
                            *((unsigned int *)&v3->padding_0[40]) = sub_1001b89b(&v8);
                        }
                        else if ((unsigned short)v16 == 1007)
                        {
                            SendDlgItemMessageA(g_10072f90, v16, 13, 0x20, &v8);
                            *((unsigned int *)&v3->padding_0[44]) = sub_1001b89b(&v8);
                        }
                        else if ((unsigned short)v16 == 1065)
                        {
                            SendDlgItemMessageA(g_10072f90, v16, 13, 0x20, &v8);
                            *((unsigned int *)&index->padding_0[8]) = sub_1001b89b(&v8);
                        }
                        else if ((unsigned short)v16 == 1064)
                        {
                            SendDlgItemMessageA(g_10072f90, v16, 13, 0x20, &v8);
                            *((unsigned int *)&index->padding_0[12]) = sub_1001b89b(&v8);
                        }
                        else if ((unsigned short)v16 == 1062)
                        {
                            SendDlgItemMessageA(g_10072f90, v16, 13, 0x20, &v8);
                            *((unsigned int *)&index->padding_0[16]) = sub_1001b89b(&v8);
                        }
                        else if ((unsigned short)v16 == 1061)
                        {
                            SendDlgItemMessageA(g_10072f90, v16, 13, 0x20, &v8);
                            *((unsigned int *)&index->padding_0[20]) = sub_1001b89b(&v8);
                        }
                        else if ((unsigned short)v16 == 1050)
                        {
                            SendDlgItemMessageA(g_10072f90, v16, 13, 0x20, &v8);
                            *((unsigned int *)&index->padding_0[32]) = sub_1001b89b(&v8);
                        }
                        else if ((unsigned short)v16 == 1051)
                        {
                            SendDlgItemMessageA(g_10072f90, v16, 13, 0x20, &v8);
                            *((unsigned int *)&index->padding_0[36]) = sub_1001b89b(&v8);
                        }
                        else if ((unsigned short)v16 == 1052)
                        {
                            SendDlgItemMessageA(g_10072f90, v16, 13, 0x20, &v8);
                            *((unsigned int *)&index->padding_0[40]) = sub_1001b89b(&v8);
                        }
                        else if ((unsigned short)v16 == 1054)
                        {
                            SendDlgItemMessageA(g_10072f90, v16, 13, 0x20, &v8);
                            *((unsigned int *)&index->padding_0[44]) = sub_1001b89b(&v8);
                        }
                        else if ((unsigned short)v16 == 1018)
                        {
                            SendDlgItemMessageA(g_10072f90, v16, 13, 0x20, &v8);
                            *((unsigned int *)&v3->padding_0[52]) = sub_1001b89b(&v8);
                        }
                        else if ((unsigned short)v16 == 1019)
                        {
                            SendDlgItemMessageA(g_10072f90, v16, 13, 0x20, &v8);
                            *((unsigned int *)&v3->padding_0[60]) = sub_1001b89b(&v8);
                        }
                        else if ((unsigned short)v16 == 1044)
                        {
                            SendDlgItemMessageA(g_10072f90, v16, 13, 0x20, &v8);
                            *((unsigned int *)&index->padding_0[52]) = sub_1001b89b(&v8);
                        }
                        else if ((unsigned short)v16 == 1043)
                        {
                            SendDlgItemMessageA(g_10072f90, v16, 13, 0x20, &v8);
                            *((unsigned int *)&index->padding_0[60]) = sub_1001b89b(&v8);
                        }
                        else if ((unsigned short)v16 == 1006)
                        {
                            count1 = SendDlgItemMessageA(g_10072f90, v16, 392, NULL, NULL);
                            if (count1 != 0xffffffff)
                                *((LRESULT *)&v3->padding_0[0]) = count1;
                        }
                        else if ((unsigned short)v16 == 1011)
                        {
                            count2 = SendDlgItemMessageA(g_10072f90, v16, 392, NULL, NULL);
                            if (count2 != 0xffffffff)
                                *((LRESULT *)&v3->padding_0[24]) = count2;
                        }
                        else if ((unsigned short)v16 == 1014)
                        {
                            v23 = SendDlgItemMessageA(g_10072f90, v16, 392, NULL, NULL);
                            if (v23 != 0xffffffff)
                                *((LRESULT *)&v3->padding_0[48]) = v23;
                        }
                        else if ((unsigned short)v16 == 0x3fc)
                        {
                            v24 = SendDlgItemMessageA(g_10072f90, v16, 392, NULL, NULL);
                            if (v24 != 0xffffffff)
                                *((LRESULT *)&v3->padding_0[56]) = v24;
                        }
                        else if ((unsigned short)v16 == 1058)
                        {
                            v25 = SendDlgItemMessageA(g_10072f90, v16, 392, NULL, NULL);
                            if (v25 != 0xffffffff)
                                *((LRESULT *)&index->padding_0[0]) = v25;
                        }
                        else if ((unsigned short)v16 == 1049)
                        {
                            v26 = SendDlgItemMessageA(g_10072f90, v16, 392, NULL, NULL);
                            if (v26 != 0xffffffff)
                                *((LRESULT *)&index->padding_0[24]) = v26;
                        }
                        else if ((unsigned short)v16 == 1046)
                        {
                            v27 = SendDlgItemMessageA(g_10072f90, v16, 392, NULL, NULL);
                            if (v27 != 0xffffffff)
                                *((LRESULT *)&index->padding_0[48]) = v27;
                        }
                        else if ((unsigned short)v16 == 1042)
                        {
                            v28 = SendDlgItemMessageA(g_10072f90, v16, 392, NULL, NULL);
                            if (v28 != 0xffffffff)
                                *((LRESULT *)&index->padding_0[56]) = v28;
                        }
                        else if ((unsigned short)v16 == 1016)
                        {
                            SendDlgItemMessageA(g_10072f90, v16, 13, 0x20, &v3->field_40);
                        }
                        else if ((unsigned short)v16 == 1040)
                        {
                            SendDlgItemMessageA(g_10072f90, v16, 13, 0x20, &index->field_40);
                        }
                        else if ((unsigned short)v16 == 1057)
                        {
                            v29 = SendDlgItemMessageA(g_10072f90, v16, 392, NULL, NULL);
                            if (v29 != 0xffffffff)
                                v6->field_40 = v29;
                        }
                        else if ((unsigned short)v16 == 1001)
                        {
                            v6->field_48 = SendDlgItemMessageA(g_10072f90, v16, 240, NULL, NULL);
                        }
                        else if ((unsigned short)v16 == 1072)
                        {
                            v6->field_44 = SendDlgItemMessageA(g_10072f90, v16, 240, NULL, NULL);
                        }
                        else if ((unsigned short)v16 == 1025)
                        {
                            SendDlgItemMessageA(g_10072f90, v16, 13, 0x7d0, v6->padding_4c);
                        }
                        else if ((unsigned short)v16 == 1033)
                        {
                            SendDlgItemMessageA(g_10072f90, v16, 13, 0x7d0, &v6->padding_4c[2000]);
                        }
                        else if ((unsigned short)(a2 >> 16) == 0x100)
                        {
                            g_100f0d44 = 36;
                            v2 = a0;
                            g_100f0d48 = a0;
                            v2 = g_1005f60a;
                            g_100f0d4c = g_1005f60a;
                            g_100f0d54 = &g_100f0d68;
                            g_100f0d58 = 3;
                            v8 = 0;
                            if ((unsigned short)v16 == 1069)
                            {
                                idx = v3;
                                g_100f0d50 = *((int *)&idx->padding_0[4]);
                                ChooseColorA(&g_100f0d44);
                                *((unsigned int *)&idx->padding_0[4]) = g_100f0d50;
                                SendDlgItemMessageA(g_10072f90, 1069, 12, NULL, v8);
                            }
                            else if ((unsigned short)v16 == 0x400)
                            {
                                idx1 = v3;
                                g_100f0d50 = *((int *)&idx1->padding_4c[20]);
                                ChooseColorA(&g_100f0d44);
                                *((unsigned int *)&idx1->padding_4c[20]) = g_100f0d50;
                                SendDlgItemMessageA(g_10072f90, 0x400, 12, NULL, v8);
                            }
                            else if ((unsigned short)v16 == 1070)
                            {
                                idx2 = index;
                                g_100f0d50 = *((int *)&idx2->padding_0[4]);
                                ChooseColorA(&g_100f0d44);
                                *((unsigned int *)&idx2->padding_0[4]) = g_100f0d50;
                                SendDlgItemMessageA(g_10072f90, 1070, 12, NULL, v8);
                            }
                            else if ((unsigned short)v16 == 1036)
                            {
                                v33 = index;
                                g_100f0d50 = *((int *)&v33->padding_4c[20]);
                                ChooseColorA(&g_100f0d44);
                                *((unsigned int *)&v33->padding_4c[20]) = g_100f0d50;
                                SendDlgItemMessageA(g_10072f90, 1036, 12, NULL, v8);
                            }
                        }
                    }
                }
            }
            if ((unsigned short)a2 != 0x404)
            {
                return 0;
            }
            else if ((a2 & 0xffff0000) == 0x10000)
            {
                g_100f0d39 = 1;
                v34 = v6;
                SendDlgItemMessageA(g_10072f90, 1029, 12, NULL, v34);
                SendDlgItemMessageA(g_10072f90, 1001, 241, v34->field_48, NULL);
                SendDlgItemMessageA(g_10072f90, 1072, 241, v34->field_44, NULL);
                SendDlgItemMessageA(g_10072f90, 1057, 390, v34->field_40, NULL);
                SendDlgItemMessageA(g_10072f90, 1025, 12, NULL, v34->padding_4c);
                SendDlgItemMessageA(g_10072f90, 1033, 12, NULL, &v34->padding_4c[2000]);
                v35 = v3;
                sub_10040940(*((int *)&v35->padding_0[8]), v8);
                SendDlgItemMessageA(g_10072f90, 1032, 12, NULL, v8);
                sub_10040940(*((int *)&v35->padding_0[12]), v8);
                SendDlgItemMessageA(g_10072f90, 1002, 12, NULL, v8);
                sub_10040940(*((int *)&v35->padding_0[16]), v8);
                SendDlgItemMessageA(g_10072f90, 1003, 12, NULL, v8);
                sub_10040940(*((int *)&v35->padding_0[20]), v8);
                SendDlgItemMessageA(g_10072f90, 1004, 12, NULL, v8);
                sub_10040940(*((int *)&v35->padding_0[32]), v8);
                SendDlgItemMessageA(g_10072f90, 1010, 12, NULL, v8);
                sub_10040940(*((int *)&v35->padding_0[36]), v8);
                SendDlgItemMessageA(g_10072f90, 1009, 12, NULL, v8);
                sub_10040940(*((int *)&v35->padding_0[40]), v8);
                SendDlgItemMessageA(g_10072f90, 1008, 12, NULL, v8);
                sub_10040940(*((int *)&v35->padding_0[44]), v8);
                SendDlgItemMessageA(g_10072f90, 1007, 12, NULL, v8);
                sub_10040940(*((int *)&v35->padding_0[52]), v8);
                SendDlgItemMessageA(g_10072f90, 1018, 12, NULL, v8);
                sub_10040940(*((int *)&v35->padding_0[60]), v8);
                SendDlgItemMessageA(g_10072f90, 1019, 12, NULL, v8);
                SendDlgItemMessageA(g_10072f90, 1016, 12, NULL, &v35->field_40);
                SendDlgItemMessageA(g_10072f90, 1006, 390, *((int *)&v35->padding_0[0]), NULL);
                SendDlgItemMessageA(g_10072f90, 1011, 390, *((int *)&v35->padding_0[24]), NULL);
                SendDlgItemMessageA(g_10072f90, 1014, 390, *((int *)&v35->padding_0[48]), NULL);
                SendDlgItemMessageA(g_10072f90, 0x3fc, 390, *((int *)&v35->padding_0[56]), NULL);
                v1 = *((int *)&v35->padding_0[4]);
                g_10289888 = *((int *)&v35->padding_0[4]);
                v1 = *((int *)&v35->padding_4c[20]);
                g_1028988c = *((int *)&v35->padding_4c[20]);
                v36 = index;
                sub_10040940(*((int *)&v36->padding_0[8]), v8);
                SendDlgItemMessageA(g_10072f90, 1065, 12, NULL, v8);
                sub_10040940(*((int *)&v36->padding_0[12]), v8);
                SendDlgItemMessageA(g_10072f90, 1064, 12, NULL, v8);
                sub_10040940(*((int *)&v36->padding_0[16]), v8);
                SendDlgItemMessageA(g_10072f90, 1062, 12, NULL, v8);
                sub_10040940(*((int *)&v36->padding_0[20]), v8);
                SendDlgItemMessageA(g_10072f90, 1061, 12, NULL, v8);
                sub_10040940(*((int *)&v36->padding_0[32]), v8);
                SendDlgItemMessageA(g_10072f90, 1050, 12, NULL, v8);
                sub_10040940(*((int *)&v36->padding_0[36]), v8);
                SendDlgItemMessageA(g_10072f90, 1051, 12, NULL, v8);
                sub_10040940(*((int *)&v36->padding_0[40]), v8);
                SendDlgItemMessageA(g_10072f90, 1052, 12, NULL, v8);
                sub_10040940(*((int *)&v36->padding_0[44]), v8);
                SendDlgItemMessageA(g_10072f90, 1054, 12, NULL, v8);
                sub_10040940(*((int *)&v36->padding_0[52]), v8);
                SendDlgItemMessageA(g_10072f90, 1044, 12, NULL, v8);
                sub_10040940(*((int *)&v36->padding_0[60]), v8);
                SendDlgItemMessageA(g_10072f90, 1043, 12, NULL, v8);
                SendDlgItemMessageA(g_10072f90, 1040, 12, NULL, &v36->field_40);
                SendDlgItemMessageA(g_10072f90, 1058, 390, *((int *)&v36->padding_0[0]), NULL);
                SendDlgItemMessageA(g_10072f90, 1049, 390, *((int *)&v36->padding_0[24]), NULL);
                SendDlgItemMessageA(g_10072f90, 1046, 390, *((int *)&v36->padding_0[48]), NULL);
                SendDlgItemMessageA(g_10072f90, 1042, 390, *((int *)&v36->padding_0[56]), NULL);
                v0 = *((int *)&v36->padding_0[4]);
                g_10289890 = *((int *)&v36->padding_0[4]);
                v0 = *((int *)&v36->padding_4c[20]);
                g_10289894 = *((int *)&v36->padding_4c[20]);
                v8 = 0;
                SendDlgItemMessageA(g_10072f90, 1069, 12, NULL, v8);
                SendDlgItemMessageA(g_10072f90, 0x400, 12, NULL, v8);
                SendDlgItemMessageA(g_10072f90, 1070, 12, NULL, v8);
                SendDlgItemMessageA(g_10072f90, 1036, 12, NULL, v8);
                g_100f0d39 = 0;
                return 0;
            }
            else
            {
                return 0;
            }
        }
    }
}
```

## `sub_1001b92a` `0x1001b92a`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1001b92a(void)
{
}
```

## `sub_1001b954` `0x1001b954`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1001b954(void)
{
}
```

## `sub_1001b97b` `0x1001b97b`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1001b97b(void)
{
}
```

## `sub_1001b9a2` `0x1001b9a2`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1001b9a2(void)
{
}
```

## `sub_1001ccb1` `0x1001ccb1`

_542 bytes. calls SendDlgItemMessageA; refs " {creature}", " {num}", " {hp%}"_

```c
extern HWND g_10072fc8;
extern int g_100f091c;

LRESULT sub_1001ccb1(void)
{
    unsigned int v3[265];  // ebx
    unsigned int i;  // ecx
    char v5;  // 4119
    char v6;  // al
    char v7;  // cl
    char v8;  // cl
    unsigned int v0;  // [bp-0x208]
    int v1[128];  // [bp-0x204]

    lstrcpy(v1, v3);
    if (v3[264] == 7 && v3[0] == 1663070030)
        v1 = (int (32 bits)[128])0;
    for (i = 0; i < 4; i += 1)
    {
        v0 = i;
        v5 = *(1060 + i + (char *)v3);
        v6 = v5 & 15;
        v7 = v5 >> 4;
        if ((v5 & 15) == 1)
        {
            lstrcat(v1, " {creature}");
        }
        else if (v6 == 2)
        {
            v8 = v7;
            if (!v7)
            {
                lstrcat(v1, " {num}");
            }
            else
            {
                if (v8 == 1)
                {
                    lstrcat(v1, " {hp%}");
                }
                else
                {
                    if (v8 == 2)
                    {
                        lstrcat(v1, " {hp}");
                    }
                    else
                    {
                        if (v8 == 3)
                        {
                            lstrcat(v1, " {mp}");
                        }
                        else
                        {
                            if (v8 == 4)
                            {
                                lstrcat(v1, " {itemid}");
                            }
                            else
                            {
                                if (v8 == 5)
                                {
                                    lstrcat(v1, " {distance}");
                                }
                                else
                                {
                                    if (v8 == 6)
                                    {
                                        lstrcat(v1, " {amount}");
                                    }
                                    else
                                    {
                                        if (v8 == 7)
                                        {
                                            lstrcat(v1, " {index}");
                                        }
                                        else
                                        {
                                            if (v8 == 8)
                                            {
                                                lstrcat(v1, " {x}");
                                            }
                                            else
                                            {
                                                if (v8 == 9)
                                                {
                                                    lstrcat(v1, " {y}");
                                                }
                                                else
                                                {
                                                    if (v8 == 10)
                                                        lstrcat(v1, " {z}");
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
        else if (v6 == 3)
        {
            if (v7 == 3)
                lstrcat(v1, " {window}");
            else
                lstrcat(v1, " {text}");
        }
        else
        {
            if (v6 == 4)
                lstrcat(v1, " {switch}");
        }
    }
    if (v3[264] == 7)
    {
        lstrcat(v1, " ");
        lstrcat(v1, &g_100f091c);
    }
    return SendDlgItemMessageA(g_10072fc8, 1005, 12, NULL, v1);
}
```

## `sub_1001cecf` `0x1001cecf`

_103 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f0d1c;
extern unsigned int g_100f0d20;
extern char g_100f0d34;

unsigned int sub_1001cecf(void)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax

    v1 = g_100f0d20;
    g_100f0d20 = g_100f0d20 + 1;
    if (v1 < 4 && *((char *)(v1 + g_100f0d1c + 1060)))
    {
        g_100f0d34 = *((char *)(v1 + g_100f0d1c + 1060));
        v2 = sub_1001f57d(0, 9002, sub_1001d5fd);
        if ((char)v2 == 1)
        {
            return v2;
        }
        else if ((char)v2 == 2)
        {
            return v2;
        }
        else if ((char)v2 != 3)
        {
            return v2;
        }
        else
        {
            return v2;
        }
    }
    return sub_1001f57d(0, 9003, sub_1001d2e0);
}
```

## `sub_1001cf36` `0x1001cf36`

_539 bytes. calls SendDlgItemMessageA; refs " {creature}", " {num}", " {hp%}"_

```c
extern HWND g_10072fc8;
extern unsigned int g_100f0d1c;
extern unsigned int g_100f0d20;

LRESULT sub_1001cf36(PSTR a0)
{
    char v5;  // 4116
    char v6;  // al
    char v7;  // cl
    char v8;  // cl
    char *v0;  // [bp-0x32c]
    char *v1;  // [bp-0x328]
    char v2;  // [bp-0x324]
    char v3;  // [bp-0x124]
    unsigned int v4;  // [bp-0x24]

    v4 = (g_100f0d20 == 1 ? 7631665 : (g_100f0d20 == 2 ? 6581810 : (g_100f0d20 == 3 ? 6582835 : 6845492)));
    v5 = *((char *)(g_100f0d20 + g_100f0d1c + 1059));
    v3 = 0;
    v6 = v5 & 15;
    v7 = v5 >> 4;
    if ((v5 & 15) == 1)
    {
        lstrcat(&v3, " {creature}");
    }
    else if (v6 == 2)
    {
        v8 = v7;
        if (!v7)
        {
            lstrcat(&v3, " {num}");
        }
        else
        {
            if (v8 == 1)
            {
                lstrcat(&v3, " {hp%}");
            }
            else
            {
                if (v8 == 2)
                {
                    lstrcat(&v3, " {hp}");
                }
                else
                {
                    if (v8 == 3)
                    {
                        lstrcat(&v3, " {mp}");
                    }
                    else
                    {
                        if (v8 == 4)
                        {
                            lstrcat(&v3, " {itemid}");
                        }
                        else
                        {
                            if (v8 == 5)
                            {
                                lstrcat(&v3, " {distance}");
                            }
                            else
                            {
                                if (v8 == 6)
                                {
                                    lstrcat(&v3, " {amount}");
                                }
                                else
                                {
                                    if (v8 == 7)
                                    {
                                        lstrcat(&v3, " {index}");
                                    }
                                    else
                                    {
                                        if (v8 == 8)
                                        {
                                            lstrcat(&v3, " {x}");
                                        }
                                        else
                                        {
                                            if (v8 == 9)
                                            {
                                                lstrcat(&v3, " {y}");
                                            }
                                            else
                                            {
                                                if (v8 == 10)
                                                    lstrcat(&v3, " {z}");
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
    else if (v6 == 3)
    {
        if (v7 == 3)
            lstrcat(&v3, " {window}");
        else
            lstrcat(&v3, " {text}");
    }
    else
    {
        if (v6 == 4)
            lstrcat(&v3, " {switch}");
    }
    v1 = &v3;
    v0 = &v4;
    wsprintfA(&v2, a0);
    return SendDlgItemMessageA(g_10072fc8, 1002, 12, NULL, &v2);
}
```

## dlgProc_CommandBuilder `0x1001d151`

Named — see [doc 10](../../10-*.md). _399 bytes. calls SendDlgItemMessageA; refs " | "_

```c
extern unsigned int g_10072fc8;
extern char g_100ee91c;
extern int g_100f091c;
extern unsigned int g_100f0d24;
extern void* g_100f0d28;

int sub_1001d151(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    void* v1;  // eax
    void* v0;  // [bp-0x428], Other Possible Types: unsigned int

    if (a1 == 272)
    {
        v0 = a0;
        g_10072fc8 = a0;
        if (!g_100f0d24 && g_100ee91c)
            lstrcat(&g_100ee91c, " | ");
        g_100f0d24 = 0;
        lstrcat(&g_100ee91c, &g_100f091c);
        SendDlgItemMessageA(a0, 1005, 12, NULL, &g_100ee91c);
        SendDlgItemMessageA(a0, 1006, 241, 0x1, NULL);
        return 0;
    }
    else if (a1 != 273)
    {
        return (unsigned int)sub_10002c6e(a0, a1, a2, a3);
    }
    else if (a2 == 1007)
    {
        if (SendDlgItemMessageA(a0, 1004, 240, NULL, NULL))
        {
            sub_1001f57d(0, 9001, sub_1001df05);
        }
        else
        {
            OpenClipboard(NULL);
            EmptyClipboard();
            if (g_100f0d28)
                GlobalFree(g_100f0d28);
            g_100f0d28 = GlobalAlloc(8194, 0x2800);
            v0 = GlobalLock(g_100f0d28);
            SendDlgItemMessageA(a0, 1005, 13, 0x2000, &g_100ee91c);
            v1 = GlobalLock(g_100f0d28);
            lstrcpy(GlobalLock(g_100f0d28), &g_100ee91c);
            GlobalUnlock(g_100f0d28);
            SetClipboardData(1, g_100f0d28);
            CloseClipboard();
        }
        DestroyWindow(a0);
        return 0;
    }
    else if (a2 == 1008)
    {
        DestroyWindow(a0);
        return 0;
    }
    else
    {
        return 0;
    }
}
```

## dlgProc_CommandParamBuilder `0x1001d2e0`

Named — see [doc 10](../../10-*.md). _797 bytes. calls MessageBoxA, SendDlgItemMessageA, SendMessageA; refs "%s'%s' "_

```c
typedef struct struct_0 {
    char field_0;
    char padding_1[1055];
    unsigned int field_420;
    char padding_424[4];
    char field_428;
} struct_0;

typedef struct struct_1 {
    char padding_0[1060];
    char field_424;
} struct_1;

extern struct_0 *g_1005e198;
extern unsigned int g_10072fc8;
extern int g_100f091c;

int sub_1001d2e0(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v11;  // eax
    struct_0 *i;  // ebx
    struct_1 *v21;  // ebx
    LRESULT count;  // eax
    unsigned int v23;  // ecx
    unsigned int v24;  // edx
    unsigned int v25;  // esi
    unsigned int v26;  // edi
    LRESULT count1;  // eax
    void* v15;  // eax
    struct_1 *v16;  // eax
    struct_1 *v17;  // ebx
    HWND v18;  // eax
    void* v19;  // eax
    struct_1 *v20;  // eax
    unsigned int v0;  // [bp-0x444]
    unsigned int v1;  // [bp-0x440]
    char *v2;  // [bp-0x43c]
    char *v3;  // [bp-0x438]
    struct_1 *v4;  // [bp-0x434]
    unsigned int v5;  // [bp-0x430]
    char *v6;  // [bp-0x42c], Other Possible Types: unsigned int
    char *v7;  // [bp-0x428], Other Possible Types: int *, unsigned int
    Byte v8[1024];  // [bp-0x424]
    int v9[8];  // [bp-0x24]
    char v10;  // [bp-0x4]

    v11 = a1;
    if (v11 == 272)
    {
        v7 = a0;
        g_10072fc8 = a0;
        for (i = g_1005e198; i->field_0; i = &i->field_428)
        {
            if (i->field_420 == 7)
            {
                v7 = v11;
                SendDlgItemMessageA(a0, 1004, 410, SendDlgItemMessageA(a0, 1004, 385, 0xffffffff, i), i);
            }
        }
        SendDlgItemMessageA(a0, 1004, 390, NULL, NULL);
        SendMessageA(a0, 273, 0x103ec, NULL);
        EnableWindow(GetDlgItem(a0, 1003), 0);
        return 0;
    }
    else if (v11 == 273)
    {
        if ((unsigned short)a2 == 1004 && (a2 & 0xffff0000) == 0x10000)
        {
            v15 = SendDlgItemMessageA(a0, 1004, 392, NULL, NULL);
            if (v15 == 0xffffffff)
                return 0;
            v16 = SendDlgItemMessageA(a0, 1004, 409, v15, NULL);
            if (!v16 || v16 == 0xffffffff)
                return 0;
            v17 = v16;
            v18 = GetDlgItem(a0, 1003);
            if ((v17->field_424 & 15) == 2 || (v17->field_424 & 15) == 3)
                EnableWindow(v18, 1);
            else
                EnableWindow(v18, 0);
            sub_1001ccb1();
            SendDlgItemMessageA(a0, 1006, 12, NULL, &v17->padding_0[32]);
            return 0;
        }
        if (a2 == 1007)
        {
            v19 = SendDlgItemMessageA(a0, 1004, 392, NULL, NULL);
            if (v19 == 0xffffffff)
                return 0;
            if (!v19)
            {
                DestroyWindow(a0);
                sub_1001f57d(0, 9004, sub_1001d151);
            }
            else
            {
                v20 = SendDlgItemMessageA(a0, 1004, 409, v19, NULL);
                if (v20 && v20 != 0xffffffff)
                {
                    v21 = v20;
                    lstrcpy(v8, v21);
                    lstrcat(v8, " ");
                    if ((v21->field_424 & 15) == 2)
                    {
                        count = SendDlgItemMessageA(a0, 1003, 13, 0x20, v9);
                        if (!v9)
                        {
                            v7 = count;
                            v6 = v23;
                            v5 = v24;
                            v4 = v21;
                            v3 = &v8[0];
                            v2 = &v10;
                            v1 = v25;
                            v0 = v26;
                            MessageBoxA(a0, "Please specify the amount in the edit control before proceeding!", NULL, MB_APPLMODAL);
                        }
                        else
                        {
                            lstrcat(v8, v9);
                            lstrcat(v8, " ");
                            goto LABEL_1001d592;
                        }
                    }
                    else
                    {
                        if ((v21->field_424 & 15) != 3)
                            goto LABEL_1001d592;
                        count1 = SendDlgItemMessageA(a0, 1003, 13, 0x20, v9);
                        if (!v9)
                        {
                            v7 = count1;
                            v6 = v23;
                            v5 = v24;
                            v4 = v21;
                            v3 = &v8[0];
                            v2 = &v10;
                            v1 = v25;
                            v0 = v26;
                            MessageBoxA(a0, "Please specify a name in the edit control before proceeding!", NULL, MB_APPLMODAL);
                        }
                        else
                        {
                            v7 = v9;
                            v6 = &v8[0];
                            wsprintfA(v8, "%s'%s' ");
LABEL_1001d592:
                            lstrcat(v8, &g_100f091c);
                            lstrcpy(&g_100f091c, v8);
                            sub_1001f57d(0, 9003, sub_1001d2e0);
                            DestroyWindow(a0);
                        }
                    }
                }
            }
            return 0;
        }
        else if (a2 == 1008)
        {
            DestroyWindow(a0);
            return 0;
        }
        else
        {
            return 0;
        }
    }
    else
    {
        return (unsigned int)sub_10002c6e(a0, a1, a2, a3);
    }
}
```

## dlgProc_CommandParamPicker `0x1001d5fd`

Named — see [doc 10](../../10-*.md). _2310 bytes. calls MessageBoxA, SendDlgItemMessageA, SendMessageA; refs "anyenemy", "anyfriend", "enemy"_

```c
extern unsigned int g_10072fc8;
extern int g_100f091c;
extern char g_100f0d34;

int sub_1001d5fd(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    char v10;  // al
    WPARAM v21;  // ebx
    LRESULT count;  // eax
    unsigned int v23;  // ecx
    unsigned int v24;  // edx
    unsigned int v25;  // esi
    unsigned int v26;  // edi
    void* count1;  // eax
    LRESULT count2;  // eax
    char v12;  // al
    char v13;  // al
    unsigned short v15;  // bx
    LRESULT v17;  // eax
    LRESULT v18;  // eax
    unsigned int v0;  // [bp-0x424]
    unsigned int v1;  // [bp-0x420]
    char *v2;  // [bp-0x41c]
    char *v3;  // [bp-0x418]
    WPARAM v4;  // [bp-0x414]
    unsigned int v5;  // [bp-0x410]
    unsigned int v6;  // [bp-0x40c]
    LRESULT v7;  // [bp-0x408], Other Possible Types: unsigned int
    int v8[256];  // [bp-0x404]
    char v9;  // [bp-0x4]

    if (a1 == 272)
    {
        v7 = a0;
        g_10072fc8 = a0;
        v10 = g_100f0d34 & 15;
        if ((g_100f0d34 & 15) == 1)
        {
            SendDlgItemMessageA(a0, 1004, 385, NULL, "anyenemy");
            SendDlgItemMessageA(a0, 1004, 385, 0x1, "anyfriend");
            SendDlgItemMessageA(a0, 1004, 385, 0x2, "enemy");
            SendDlgItemMessageA(a0, 1004, 385, 0x3, "friend");
            SendDlgItemMessageA(a0, 1004, 385, 0x4, "self");
            SendDlgItemMessageA(a0, 1004, 385, 0x5, "subenemy");
            SendDlgItemMessageA(a0, 1004, 385, 0x6, "subfriend");
            SendDlgItemMessageA(a0, 1004, 385, 0x7, "target");
            SendDlgItemMessageA(a0, 1004, 385, 0x8, "creature name");
            SendDlgItemMessageA(a0, 1004, 390, NULL, NULL);
            SendMessageA(a0, 273, 0x103ec, NULL);
            sub_1001cf36("Choose a value for the %s parameter%s to the command. It can be any of the predefined creature groups listed or a custom creature name.");
            EnableWindow(GetDlgItem(a0, 1003), 0);
        }
        else
        {
            if (v10 == 2)
            {
                v12 = g_100f0d34 >> 4;
                if (!(g_100f0d34 & 240))
                {
                    SendDlgItemMessageA(a0, 1004, 385, NULL, "general number");
                    SendDlgItemMessageA(a0, 1006, 12, NULL, "a general number of unknown type. Follow the description of the command to know what you must input.");
                }
                else
                {
                    if (v12 == 1)
                    {
                        SendDlgItemMessageA(a0, 1004, 385, NULL, "hp percentage");
                        SendDlgItemMessageA(a0, 1006, 12, NULL, "enter a hp percentage, ranging from 0 to 100. Do not include the '%' sign in your input.");
                    }
                    else
                    {
                        if (v12 == 2)
                        {
                            SendDlgItemMessageA(a0, 1004, 385, NULL, "hp absolute");
                            SendDlgItemMessageA(a0, 1006, 12, NULL, "enter the exact hp amount (not as percentage)");
                        }
                        else
                        {
                            if (v12 == 3)
                            {
                                SendDlgItemMessageA(a0, 1004, 385, NULL, "mp absolute");
                                SendDlgItemMessageA(a0, 1006, 12, NULL, "enter the exact mp amount (not as percentage)");
                            }
                            else
                            {
                                if (v12 == 4)
                                {
                                    SendDlgItemMessageA(a0, 1004, 385, NULL, "item id");
                                    SendDlgItemMessageA(a0, 1006, 12, NULL, "enter the id of the item for this command to use. If you look at the item in the client, its id appears as a white status message (bottom of the screen).");
                                }
                                else
                                {
                                    if (v12 == 5)
                                    {
                                        SendDlgItemMessageA(a0, 1004, 385, NULL, "distance");
                                        SendDlgItemMessageA(a0, 1006, 12, NULL, "enter the distance in squares as required by the command");
                                    }
                                    else
                                    {
                                        if (v12 == 6)
                                        {
                                            SendDlgItemMessageA(a0, 1004, 385, NULL, "amount");
                                            SendDlgItemMessageA(a0, 1006, 12, NULL, "enter the amount as required by the command");
                                        }
                                        else
                                        {
                                            if (v12 == 7)
                                            {
                                                SendDlgItemMessageA(a0, 1004, 385, NULL, "index");
                                                SendDlgItemMessageA(a0, 1006, 12, NULL, "enter the index as required by the command");
                                            }
                                            else
                                            {
                                                if (v12 == 8)
                                                {
                                                    SendDlgItemMessageA(a0, 1004, 385, NULL, "x");
                                                    SendDlgItemMessageA(a0, 1006, 12, NULL, "enter the x coordinate");
                                                }
                                                else
                                                {
                                                    if (v12 == 9)
                                                    {
                                                        SendDlgItemMessageA(a0, 1004, 385, NULL, "y");
                                                        SendDlgItemMessageA(a0, 1006, 12, NULL, "enter the y coordinate");
                                                    }
                                                    else
                                                    {
                                                        if (v12 == 10)
                                                        {
                                                            SendDlgItemMessageA(a0, 1004, 385, NULL, "z");
                                                            SendDlgItemMessageA(a0, 1006, 12, NULL, "enter the z coordinate");
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
                SendDlgItemMessageA(a0, 1004, 390, NULL, NULL);
                sub_1001cf36("Choose a value for the %s parameter%s to the command. It is a number to which more information is specified below.");
            }
            else
            {
                if (v10 == 3)
                {
                    v13 = g_100f0d34 >> 4;
                    if (!(g_100f0d34 & 240))
                    {
                        SendDlgItemMessageA(a0, 1004, 385, NULL, "general text");
                        SendDlgItemMessageA(a0, 1006, 12, NULL, "general text of unkown type. Refer to the description of the command to know what you must input.");
                    }
                    else
                    {
                        if (v13 == 1)
                        {
                            SendDlgItemMessageA(a0, 1004, 385, NULL, "text to say");
                            SendDlgItemMessageA(a0, 1006, 12, NULL, "enter the text to say in default chat. It could be a phrase or even a spell.");
                        }
                        else
                        {
                            if (v13 == 2)
                            {
                                SendDlgItemMessageA(a0, 1004, 385, NULL, "spell");
                                SendDlgItemMessageA(a0, 1006, 12, NULL, "enter the spell that you wish this command to cast");
                            }
                            else
                            {
                                if (v13 == 3)
                                {
                                    SendDlgItemMessageA(a0, 1004, 385, NULL, "window");
                                    SendDlgItemMessageA(a0, 1006, 12, NULL, "enter the window name or item id of window");
                                }
                            }
                        }
                    }
                    SendDlgItemMessageA(a0, 1004, 390, NULL, NULL);
                    sub_1001cf36("Choose a value for the %s parameter%s to the command. It is of type 'text' to which more information is specified below.");
                }
                else
                {
                    if (v10 == 4)
                    {
                        SendDlgItemMessageA(a0, 1004, 385, NULL, "on");
                        SendDlgItemMessageA(a0, 1004, 385, 0x1, "off");
                        SendDlgItemMessageA(a0, 1004, 385, 0x2, "toggle");
                        SendDlgItemMessageA(a0, 1004, 390, NULL, NULL);
                        sub_1001cf36("Choose whether to turn this bot setting on or off.");
                        EnableWindow(GetDlgItem(a0, 1003), 0);
                    }
                }
            }
        }
        sub_1001ccb1();
        return 0;
    }
    else if (a1 == 273)
    {
        v15 = a2 >> 16;
        if (a2 == 1003)
        {
            EnableWindow(GetDlgItem(a0, 1006), 0);
            return 0;
        }
        if ((unsigned short)a2 == 1004 && v15 == 1)
        {
            v17 = SendDlgItemMessageA(a0, 1004, 392, NULL, NULL);
            if (v17 == 0xffffffff)
            {
                return 0;
            }
            else if ((g_100f0d34 & 15) == 1)
            {
                v18 = v17;
                if (!v17)
                {
                    SendDlgItemMessageA(a0, 1006, 12, NULL, "picks an enemy out of both the enemy and subenemy lists. If a potential enemy is found in the enemy list, it is chosen right away without considering the subenemy list.  If no target is picked from the enemy list, one will attempt to be chosen from the subenemy list. You can look at this as some sort of priority list.");
                }
                else if (v18 == 0x1)
                {
                    SendDlgItemMessageA(a0, 1006, 12, NULL, "picks a friend out of both the friend and subfriend lists. If a potential friend is found in the friend list, it is chosen right away without considering the subfriend list.  If no target is picked from the friend list, one will attempt to be chosen from the subfriend list. You can look at this as some sort of priority list.");
                }
                else if (v18 == 0x2)
                {
                    SendDlgItemMessageA(a0, 1006, 12, NULL, "picks the first enemy out of your list or the one with the least hp% if the bot option 'Choose targets with least hp' is checked. If 'Discount protection zones' is enabled, people standing in key protection zones will be exluded from the selection. If 'Trace shots' is enabled, people that can't be reached by projectiles will be excluded from the selection.");
                }
                else if (v18 == 0x3)
                {
                    SendDlgItemMessageA(a0, 1006, 12, NULL, "picks the first friend out of your list or the one with the least hp% if the bot option 'Choose targets with least hp' is checked. If 'Discount protection zones' is enabled, people standing in key protection zones will be exluded from the selection. If 'Trace shots' is enabled, people that can't be reached by projectiles will be excluded from the selection.");
                }
                else if (v18 == 0x4)
                {
                    SendDlgItemMessageA(a0, 1006, 12, NULL, "yourself, regardless of your name");
                }
                else if (v18 == 0x5)
                {
                    SendDlgItemMessageA(a0, 1006, 12, NULL, "picks the first subenemy out of your list or the one with the least hp% if the bot option 'Choose targets with least hp' is checked. Subenemies can be used as a secondary list for less important people. It's up to you how to use it. If 'Discount protection zones' is enabled, people standing in key protection zones will be exluded from the selection. If 'Trace shots' is enabled, people that can't be reached by projectiles will be excluded from the selection.");
                }
                else if (v18 == 0x6)
                {
                    SendDlgItemMessageA(a0, 1006, 12, NULL, "picks the first subfriend out of your list or the one with the least hp% if the bot option 'Choose targets with least hp' is checked. Subenfriends can be used as a secondary list for less important people. It's up to you how to use it. If 'Discount protection zones' is enabled, people standing in key protection zones will be exluded from the selection. If 'Trace shots' is enabled, people that can't be reached by projectiles will be excluded from the selection.");
                }
                else if (v18 == 0x7)
                {
                    SendDlgItemMessageA(a0, 1006, 12, NULL, "the last red boxed target (attacking someone in Tibia). It is remembered even if the creature leaves the screen and loses the box. Using this as parameter can make commands such as 'sd target' sd the person that is currently being attacked. It is an easy and convenient target selection method.");
                }
                else if (v18 == 0x8)
                {
                    SendDlgItemMessageA(a0, 1006, 12, NULL, "a custom name of any other player or monster, such as 'Rat', without the single quotes");
                    EnableWindow(GetDlgItem(a0, 1003), 1);
                    return 0;
                }
                EnableWindow(GetDlgItem(a0, 1003), 0);
                return 0;
            }
            else
            {
                return 0;
            }
        }
        if (a2 == 1007)
        {
            v21 = _INSERT(v15, 0, g_100f0d34 & 15);
            if ((g_100f0d34 & 15) == 1 || *((char *)&v21) == 4)
            {
                count1 = SendDlgItemMessageA(a0, 1004, 392, NULL, NULL);
                if (count1 == 0xffffffff)
                    return 0;
                if (count1 != 0x8 || *((char *)&v21) == 4)
                {
                    SendDlgItemMessageA(a0, 1004, 393, count1, v8);
LABEL_1001ddf0:
                    lstrcat(&g_100f091c, " ");
                    lstrcat(&g_100f091c, v8);
                    DestroyWindow(a0);
                    sub_1001cecf();
                    return 0;
                }
                count2 = SendDlgItemMessageA(a0, 1003, 13, 0x20, v8);
                if (v8)
                    goto LABEL_1001ddf0;
                v7 = count2;
                v6 = v23;
                v5 = v24;
                v4 = v21;
                v3 = v8;
                v2 = &v9;
                v1 = v25;
                v0 = v26;
                MessageBoxA(a0, "Please specify the creature name in the edit control before proceeding!", NULL, MB_APPLMODAL);
            }
            else
            {
                count = SendDlgItemMessageA(a0, 1003, 13, 0x20, v8);
                if (!v8)
                {
                    v7 = count;
                    v6 = v23;
                    v5 = v24;
                    v4 = v21;
                    v3 = v8;
                    v2 = &v9;
                    v1 = v25;
                    v0 = v26;
                    MessageBoxA(a0, "Please specify a value in the edit control before proceeding!", NULL, MB_APPLMODAL);
                }
                else
                {
                    SendDlgItemMessageA(a0, 1004, 393, v21, v8);
                    if (*((char *)&v21) == 3)
                    {
                        lstrcat(&g_100f091c, " '");
                        lstrcat(&g_100f091c, v8);
                        lstrcat(&g_100f091c, "'");
                    }
                    else
                    {
                        lstrcat(&g_100f091c, " ");
                        lstrcat(&g_100f091c, v8);
                    }
                    DestroyWindow(a0);
                    sub_1001cecf();
                }
            }
            return 0;
        }
        else if (a2 == 1008)
        {
            DestroyWindow(a0);
            return 0;
        }
        else
        {
            return 0;
        }
    }
    else
    {
        return (unsigned int)sub_10002c6e(a0, a1, a2, a3);
    }
}
```

## `sub_1001ddd2` `0x1001ddd2`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1001ddd2(void)
{
}
```

## dlgProc_CommandPicker `0x1001df05`

Named — see [doc 10](../../10-*.md). _724 bytes. calls SendDlgItemMessageA, SendMessageA; refs "Attack", "Miscellaneous", "Movement"_

```c
typedef struct struct_0 {
    char field_0;
} struct_0;

extern struct_0 *g_1005e194;
extern unsigned int g_10072fc8;
extern int g_100f091c;
extern unsigned int g_100f0d1c;
extern unsigned int g_100f0d20;

int sub_1001df05(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned short v1;  // bx
    LRESULT count;  // eax
    char *i;  // ebx
    void* count2;  // eax
    LRESULT v6;  // eax
    void* v7;  // eax
    LRESULT v8;  // eax
    LRESULT v9;  // ebx
    LRESULT v0;  // [bp-0x28], Other Possible Types: unsigned int

    if (a1 == 272)
    {
        v0 = a0;
        g_10072fc8 = a0;
        SendDlgItemMessageA(a0, 1003, 330, NULL, "Attack");
        SendDlgItemMessageA(a0, 1003, 330, 0x1, "Miscellaneous");
        SendDlgItemMessageA(a0, 1003, 330, 0x2, "Movement");
        SendDlgItemMessageA(a0, 1003, 330, 0x3, "Inventory");
        SendDlgItemMessageA(a0, 1003, 330, 0x4, "Restoration");
        SendDlgItemMessageA(a0, 1003, 330, 0x5, "Cavebot");
        SendDlgItemMessageA(a0, 1003, 330, 0x6, "Settings");
        SendDlgItemMessageA(a0, 1003, 334, NULL, NULL);
        SendMessageA(a0, 273, 0x103eb, NULL);
        return 0;
    }
    else if (a1 == 273)
    {
        v1 = a2 >> 16;
        if ((unsigned short)a2 == 1003 && v1 == 1)
        {
            SendDlgItemMessageA(a0, 1004, 388, NULL, NULL);
            if (SendDlgItemMessageA(a0, 1003, 327, NULL, NULL) != 0xffffffff)
            {
                for (i = &g_1005e194->field_0; *(i); i += 1064)
                {
                    if (*((int *)&i[1056]) == count)
                    {
                        v0 = count;
                        SendDlgItemMessageA(a0, 1004, 410, SendDlgItemMessageA(a0, 1004, 385, 0xffffffff, i), i);
                    }
                }
            }
            SendDlgItemMessageA(a0, 1004, 390, NULL, NULL);
            SendMessageA(a0, 273, 0x103ec, NULL);
            return 0;
        }
        if ((unsigned short)a2 == 1004 && v1 == 1)
        {
            count2 = SendDlgItemMessageA(a0, 1004, 392, NULL, NULL);
            if (count2 == 0xffffffff)
                return 0;
            v6 = SendDlgItemMessageA(a0, 1004, 409, count2, NULL);
            if (!v6 || v6 == 0xffffffff)
                return 0;
            sub_1001ccb1();
            SendDlgItemMessageA(a0, 1006, 12, NULL, v6 + 8);
            return 0;
        }
        if (a2 == 1007)
        {
            v7 = SendDlgItemMessageA(a0, 1004, 392, NULL, NULL);
            if (v7 == 0xffffffff)
                return 0;
            v8 = SendDlgItemMessageA(a0, 1004, 409, v7, NULL);
            if (!v8 || v8 == 0xffffffff)
                return 0;
            v9 = v8;
            lstrcpy(&g_100f091c, v9);
            g_100f0d1c = v9;
            g_100f0d20 = 0;
            DestroyWindow(a0);
            sub_1001cecf();
            return 0;
        }
        else if (a2 == 1008)
        {
            DestroyWindow(a0);
            return 0;
        }
        else
        {
            return 0;
        }
    }
    else
    {
        return (unsigned int)sub_10002c6e(a0, a1, a2, a3);
    }
}
```

## dlgProc_HotkeyActionPicker `0x1001e1d9`

Named — see [doc 10](../../10-*.md). _314 bytes. calls SendDlgItemMessageA_

```c
extern unsigned int g_10072fc8;
extern void g_100ee91c;
extern char g_100ee920;
extern int g_100ee921;
extern unsigned int g_100f0d24;

int sub_1001e1d9(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v0;  // [bp-0x28]

    if (a1 == 272)
    {
        v0 = a0;
        g_10072fc8 = a0;
        SendDlgItemMessageA(a0, 1003, 241, 0x1, NULL);
        g_100f0d24 = 1;
        return 0;
    }
    else if (a1 != 273)
    {
        return (unsigned int)sub_10002c6e(a0, a1, a2, a3);
    }
    else if (a2 == 1003)
    {
        EnableWindow(GetDlgItem(a0, 1006), 0);
        return 0;
    }
    else if (a2 == 1004)
    {
        EnableWindow(GetDlgItem(a0, 1006), 1);
        return 0;
    }
    else if (a2 == 1007)
    {
        if (SendDlgItemMessageA(a0, 1003, 240, NULL, NULL))
        {
            g_100ee91c = 0;
        }
        else
        {
            *((unsigned int *)&g_100ee91c) = 1869903201;
            g_100ee920 = 32;
            SendDlgItemMessageA(a0, 1006, 13, 0x20, &g_100ee921);
            lstrcat(&g_100ee91c, " ");
        }
        sub_1001f57d(0, 9001, sub_1001df05);
        DestroyWindow(a0);
        return 0;
    }
    else if (a2 == 1008)
    {
        DestroyWindow(a0);
        return 0;
    }
    else
    {
        return 0;
    }
}
```

## dlgProc_FriendsEnemies `0x1001e313`

Named — see [doc 10](../../10-*.md). _210 bytes. refs ");
        sub_1000307e(a0, 1002, ", ");
        sub_1000307e(a0, 1011, ", ");
        sub_1000307e(a0, 1008, "_

```c
extern unsigned int g_10072fb8;

int sub_1001e313(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v0;  // [bp-0x18]

    if (a1 == 272)
    {
        v0 = a0;
        g_10072fb8 = a0;
        sub_1000307e(a0, 1003, "List of names of each character that should be considered an enemy. Enter them one per line.");
        sub_1000307e(a0, 1002, "List of names of each character that should be considered a friend. Enter them one per line.");
        sub_1000307e(a0, 1011, "List of names of each character that should be considered a subenemy. Enter them one per line. This is a less important class of enemies that in some cases you may not want the bot to consider (when using key binds).");
        sub_1000307e(a0, 1008, "List of names of each character that should be considered a subfriend. Enter them one per line. This is a less important class of friends that in some cases you may not want the bot to consider (when using key binds).");
        sub_1000307e(a0, 1006, "For easy recognition, enemies will have a red E next to their name whereas friends will display a blue F. Subenemies will display a red SE and subfriends a blue SF.");
        sub_1000307e(a0, 1007, "For easy recognition, enemy outfits will be painted red whereas friend outfits will be painted blue. Subenemy outfits will be painted with a lighter red and subfriend outfits with a lighter blue.");
        sub_1000307e(a0, 1014, "If you want to auto-invite people into your party or a private chat channel that you've made, enter a keyword to do so here. For example, if your keyword is 'inv', people that message you saying 'inv party' or 'inv channel' will be invited there.");
        return 0;
    }
    else if (a1 == 273)
    {
        return 0;
    }
    else if (a1 == 16)
    {
        ShowWindow(a0, SW_HIDE);
        return 0;
    }
    else
    {
        return (unsigned int)sub_10002c6e(a0, a1, a2, a3);
    }
}
```

## dlgProc_Healer `0x1001e3e5`

Named — see [doc 10](../../10-*.md). _990 bytes. calls SendDlgItemMessageA; refs "Light", "Strong", "Great"_

```c
extern HWND g_10072f80;

int sub_1001e3e5(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    int i;  // ebx
    unsigned int v0;  // [bp-0x28]
    int v1[8];  // [bp-0x24]

    if (a1 == 272)
    {
        v0 = a0;
        g_10072f80 = a0;
        SendDlgItemMessageA(g_10072f80, 1003, 385, NULL, "Light");
        SendDlgItemMessageA(g_10072f80, 1003, 385, 0x1, "Strong");
        SendDlgItemMessageA(g_10072f80, 1003, 385, 0x2, "Great");
        SendDlgItemMessageA(g_10072f80, 1003, 385, 0x3, "Ultimate");
        SendDlgItemMessageA(g_10072f80, 1003, 385, 0x4, "Spirit");
        SendDlgItemMessageA(a0, 1026, 385, NULL, "Light Potion");
        SendDlgItemMessageA(a0, 1026, 385, 0x1, "Strong Potion");
        SendDlgItemMessageA(a0, 1026, 385, 0x2, "Great Potion");
        SendDlgItemMessageA(a0, 1026, 385, 0x3, "Ultimate Potion");
        SendDlgItemMessageA(a0, 1026, 385, 0x4, "Spirit Potion");
        SendDlgItemMessageA(a0, 1026, 385, 0x5, "UH Rune");
        SendDlgItemMessageA(a0, 0x400, 385, NULL, "Light Potion");
        SendDlgItemMessageA(a0, 0x400, 385, 0x1, "Strong Potion");
        SendDlgItemMessageA(a0, 0x400, 385, 0x2, "Great Potion");
        SendDlgItemMessageA(a0, 0x400, 385, 0x3, "Spirit Potion");
        SendDlgItemMessageA(a0, 1032, 385, NULL, "Light");
        SendDlgItemMessageA(a0, 1032, 385, 0x1, "Strong");
        SendDlgItemMessageA(a0, 1032, 385, 0x2, "Great");
        SendDlgItemMessageA(a0, 1032, 385, 0x3, "Spirit");
        sub_1000307e(a0, 0x3ff, "The healing spell to use when having high amount of health (receiving low damage). Usually this will be 'exura' or 'exura gran' and is used for hunting.");
        sub_1000307e(a0, 1009, "The healing spell to use first when being low on health (receiveing high damage). Usually this will be 'exura vita' or 'exura sio name'. This has priority over Spell Hi and Uh Rune.");
        sub_1000307e(a0, 0x3fc, "The minimum amount of mana needed for the Spell Hi healing method. Can be set as more than the spell cost to keep some mana in reserve.");
        sub_1000307e(a0, 1011, "The minimum amount of mana needed for the Spell Lo healing method. Can be set as more than the spell cost to keep some mana in reserve.");
        sub_1000307e(a0, 1018, "The amount of hitpoints needed to trigger the Spell Hi healing method.");
        sub_1000307e(a0, 1013, "The amount of hitpoints needed to trigger the Spell Lo healing method.");
        sub_1000307e(a0, 1016, "The amount of hitpoints needed to trigger the UH Rune healing method. The response on the healing is very fast and double uhing is avoided. This method has priority over Spell Hi.");
        sub_1000307e(a0, 1006, "The amount of hitpoints needed to trigger the Potion healing method. This method is independant of the other healing methods and can trigger at the same time as them.");
        sub_1000307e(a0, 1003, "The type of health potion to use for this healing method.");
        sub_1000307e(a0, 1032, "The type of mana potion to use for this mana restoration method.");
        sub_1000307e(a0, 1029, "The amount of mana needed to trigger Mana potion restoration.");
        sub_1000307e(a0, 1034, "The delay in milliseconds to wait before executing any method of healing to prevent suspicious bot-like healing behavior. You will probably want to leave this at 0.");
        sub_1000307e(a0, 1014, "The time to wait in milliseconds after executing any method of healing to prevent spamming it. It's best to keep this low for pvp, higher for hunting.");
        sub_1000307e(a0, 1026, "Selects the type of health potion to be used in some hotkeys such as 'refillhealth'.");
        sub_1000307e(a0, 0x400, "Selects the type of mana potion to be used in some hotkeys such as 'refillmana'.");
        SendDlgItemMessageA(a0, 1034, 385, 0xffffffff, "0 ms");
        for (i = 100; i <= 3000; i += 100)
        {
            sub_10040940(i, v1);
            lstrcat(v1, " ms");
            SendDlgItemMessageA(a0, 1034, 385, 0xffffffff, v1);
            SendDlgItemMessageA(a0, 1014, 385, 0xffffffff, v1);
        }
        SendDlgItemMessageA(a0, 1014, 390, NULL, NULL);
        return 0;
    }
    else if (a1 == 273)
    {
        return 0;
    }
    else if (a1 == 16)
    {
        ShowWindow(a0, SW_HIDE);
        return 0;
    }
    else
    {
        return (unsigned int)sub_10002c6e(a0, a1, a2, a3);
    }
}
```

## dlgProc_NavNet `0x1001e7c3`

Named — see [doc 10](../../10-*.md). _880 bytes. calls SendDlgItemMessageA; refs "Disconnect", "Connect", ");
        sub_1000307e(a0, 1006, "_

```c
typedef struct CHOOSECOLORA {
    unsigned int lStructSize;
    HWND hwndOwner;
    HWND hInstance;
    unsigned int rgbResult;
    unsigned int *lpCustColors;
    enum CHOOSECOLOR_FLAGS Flags;
    LPARAM lCustData;
    void* lpfnHook;
    PSTR lpTemplateName;
} CHOOSECOLORA;

extern char g_1005f537;
extern unsigned int g_1005f60a;
extern int g_1005f651;
extern char g_1005f653;
extern HWND g_10072f7c;
extern CHOOSECOLORA g_100f0d44;
extern unsigned int g_100f0d48;
extern unsigned int g_100f0d4c;
extern unsigned int g_100f0d50;
extern unsigned int g_100f0d54;
extern unsigned int g_100f0d58;
extern char g_100f0d68;
extern int g_100fa97c;
extern int g_100fa9bc;
extern int g_100fa9fc;
extern void g_10134d61;
extern char g_10134d81;
extern int g_1013f31c;
extern char g_1014f414;
extern char g_101d5e28;

int sub_1001e7c3(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    void* i;  // esi
    void* iter;  // esi
    unsigned int v13;  // eax
    unsigned int v14;  // ecx
    unsigned int v5;  // ecx
    unsigned int v6;  // eax
    unsigned int v7;  // ecx
    char v8;  // dl
    unsigned int v9;  // edx
    unsigned int v11;  // eax
    unsigned int v0;  // [bp-0x60]
    unsigned int v1;  // [bp-0x58]
    int v2[20];  // [bp-0x54]

    if (a1 == 272)
    {
        if (g_1005f537 == 1)
            SendDlgItemMessageA(a0, 1007, 12, NULL, "Disconnect");
        else
            SendDlgItemMessageA(a0, 1007, 12, NULL, "Connect");
        SendDlgItemMessageA(a0, 1004, 12, NULL, &g_100fa97c);
        sub_10040940(g_1013f31c, v2);
        SendDlgItemMessageA(a0, 1012, 12, NULL, v2);
        SendDlgItemMessageA(a0, 1006, 12, NULL, &g_100fa9bc);
        SendDlgItemMessageA(a0, 1003, 12, NULL, &g_100fa9fc);
        SendDlgItemMessageA(a0, 1009, 12, NULL, &g_10134d61);
        if (g_10134d81)
            SendDlgItemMessageA(a0, 1011, 241, 0x1, NULL);
        if (g_1014f414)
            SendDlgItemMessageA(a0, 1013, 241, 0x1, NULL);
        if (g_101d5e28)
            SendDlgItemMessageA(a0, 1014, 241, 0x1, NULL);
        v0 = a0;
        g_10072f7c = a0;
        sub_1000307e(a0, 1004, "The person that will be hosting the server must run navserv.exe (port 7175) provided with the bot and give out his ip to the clients which is to be entered here.");
        sub_1000307e(a0, 1006, "The desired name that you wish other players to see you as. This is determined solely by you.");
        sub_1000307e(a0, 1003, "Insert here the password that the person running the server chose when starting it up.");
        sub_1000307e(a0, 1009, "If you want a custom color for your name, you can click in this field to choose one through a color dialog.");
        sub_1000307e(a0, 1011, "If you are annoyed by the fact that people use too many flashy colors, you can reduce it to the usual blue for friend and red for enemy with this option.");
        sub_1000307e(a0, 1007, "This button connects you to the navigation server with all the specified above settings. It will also keep reconnecting every few seconds in case the server is down.");
        return 0;
    }
    else if (a1 != 273)
    {
        return (unsigned int)sub_10002c6e(a0, a1, a2, a3);
    }
    else if (a2 == 1007)
    {
        sub_10007a08();
        return 0;
    }
    else if ((unsigned short)a2 == 1009)
    {
        if ((a2 & 0xffff0000) == 0x1000000)
        {
            g_100f0d44.lStructSize = 36;
            v1 = a0;
            g_100f0d48 = a0;
            v1 = g_1005f60a;
            g_100f0d4c = g_1005f60a;
            g_100f0d54 = &g_100f0d68;
            g_100f0d58 = 3;
            for (i = &g_10134d61; *((char *)i); i += 1);
            iter = i - 1;
            v5 = 0;
            v6 = 0;
            while (true)
            {
                v7 = v5;
                if (iter >= &g_10134d61)
                {
                    v8 = *((char *)iter);
                    iter -= 1;
                    if (v8 >= 97 && v8 <= 122)
                    {
                        v9 = _INSERT(v8, 0, v8 - 87);
                    }
                    else if (v8 >= 65 && v8 <= 90)
                    {
                        v9 = _INSERT(v8, 0, v8 - 55);
                    }
                    else if (v8 >= 48 && v8 <= 57)
                    {
                        v9 = _INSERT(v8, 0, v8 - 48);
                    }
                    else
                    {
                        break;
                    }
                    v6 += v9 << ((char)v7 & 31);
                    v5 = v7 + 4;
                }
                else
                {
                    v11 = v6 >> 8;
                    v7 = _INSERT(_INSERT((char)v6 * 0x100, 0, v11) * 0x100, 0, v11 >> 8);
                    break;
                }
            }
            g_100f0d50 = v7;
            ChooseColorA(&g_100f0d44.lStructSize);
            v13 = g_100f0d50 >> 8;
            v14 = _INSERT((char)g_100f0d50 * 0x100, 0, v13);
            sub_100409a8(_INSERT(v14 * 0x100, 0, v13 >> 8), &g_1005f651);
            lstrcpy(&g_10134d61, &g_1005f653);
            SendDlgItemMessageA(a0, 1009, 12, NULL, &g_1005f653);
            return 0;
        }
        else
        {
            return 0;
        }
    }
    else
    {
        if ((unsigned short)a2 == 1011)
        {
            g_10134d81 = (char)SendDlgItemMessageA(g_10072f7c, 1011, 240, NULL, NULL);
            return 0;
        }
        else if ((unsigned short)a2 == 1013)
        {
            g_1014f414 = (char)SendDlgItemMessageA(g_10072f7c, 1013, 240, NULL, NULL);
            return 0;
        }
        else if ((unsigned short)a2 == 1014)
        {
            g_101d5e28 = (char)SendDlgItemMessageA(g_10072f7c, 1014, 240, NULL, NULL);
            return 0;
        }
        else
        {
            return 0;
        }
    }
}
```

## dlgProc_LinksNavNet `0x1001eb33`

Named — see [doc 10](../../10-*.md). _985 bytes. calls MessageBoxA, SendDlgItemMessageA, WriteProcessMemory; refs "Stop Links", "Run Links", ");
        sub_1000307e(a0, 1006, "_

```c
extern unsigned int g_10042668;
extern char g_1005f536;
extern HANDLE g_1005f612;
extern char g_1005f8a4;
extern unsigned int g_10072f74;
extern char g_10134d82;
extern void g_10134d83;
extern char g_10134dc3;
extern char g_10134de3;
extern char g_10134e03;
extern char g_10134e43;

int sub_1001eb33(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int count;  // eax
    unsigned int count1;  // eax
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]

    if (a1 == 272)
    {
        if (g_1005f536 == 1)
            SendDlgItemMessageA(a0, 1007, 12, NULL, "Stop Links");
        else
            SendDlgItemMessageA(a0, 1007, 12, NULL, "Run Links");
        SendDlgItemMessageA(a0, 1004, 12, NULL, &g_10134d83);
        SendDlgItemMessageA(a0, 1006, 12, NULL, &g_10134dc3);
        SendDlgItemMessageA(a0, 1014, 12, NULL, &g_10134de3);
        SendDlgItemMessageA(a0, 1009, 12, NULL, &g_10134e03);
        SendDlgItemMessageA(a0, 1010, 12, NULL, &g_10134e43);
        if (g_10134d82)
            SendDlgItemMessageA(a0, 1003, 241, 0x1, NULL);
        v0 = a0;
        g_10072f74 = a0;
        sub_1000307e(a0, 1004, "Normally your IP address will be filled in automatically but if you use a proxy or router you might need to set this manually. Leave this field blank if you don't use any. The other clients will use this IP address to connect.");
        sub_1000307e(a0, 1006, "This is the server port that will be opened to listen for incomming connections. If you're behind a proxy or router, then you may need to use port forwarding. Look for information on google on how to do this for your specific router.");
        sub_1000307e(a0, 1014, "The account number to use by other clients when loggin in. The password is always 'elfbot'.");
        sub_1000307e(a0, 1003, "If this option is enabled, the clients that connect to you will be able to control your character. If not they will only be able to watch and cannot control your character. This takes effect as soon as it's checked/unchecked and can be done so during a session.");
        sub_1000307e(a0, 1007, "This activates the link server, or shuts it down if it is active.");
        sub_1000307e(a0, 1009, "The IP address of the Links server to be used when connecting.");
        sub_1000307e(a0, 1010, "The port to use when connecting to the Links server.");
        sub_1000307e(a0, 1008, "Click this button to set these client settings to be used when pressing the 'Enter Game' button.");
        return 0;
    }
    else if (a1 != 273)
    {
        return (unsigned int)sub_10002c6e(a0, a1, a2, a3);
    }
    else if (a2 == 1007)
    {
        if (g_1005f536)
        {
            g_1005f536 = 0;
            sub_10001222();
            SendDlgItemMessageA(a0, 1007, 12, NULL, "Run Links");
            return 0;
        }
        else if (g_1005f8a4)
        {
            return 273;
        }
        else
        {
            SendDlgItemMessageA(a0, 1004, 13, 0x40, &g_10134d83);
            SendDlgItemMessageA(a0, 1006, 13, 0x20, &g_10134dc3);
            SendDlgItemMessageA(a0, 1014, 13, 0x20, &g_10134de3);
            count = SendDlgItemMessageA(a0, 1003, 240, NULL, NULL);
            g_10134d82 = count;
            sub_100010bf(&g_10134d83, &g_10134dc3, count, &g_10134de3);
            SendDlgItemMessageA(a0, 1007, 12, NULL, "Stop Links");
            g_1005f536 = 1;
            return 0;
        }
    }
    else
    {
        if (a2 == 1008)
        {
            if (*((int *)0x64a9c0) == 31)
            {
                MessageBoxA(a0, "You must be logged off before setting links for client use.", "Logout first!", MB_ICONSTOP);
                return 0;
            }
            SendDlgItemMessageA(a0, 1009, 13, 0x40, &g_10134e03);
            SendDlgItemMessageA(a0, 1010, 13, 0x20, &g_10134e43);
            sub_10001170(&g_10134e03, &g_10134e43);
            v1 = 44009;
            WriteProcessMemory(g_1005f612, 0x4f3649, &v1, 0x3, NULL);
            v1 = 42985;
            WriteProcessMemory(g_1005f612, 0x4f371e, &v1, 0x3, NULL);
            v1 = 0xebebebeb;
            WriteProcessMemory(g_1005f612, 0x4f358a, &v1, 0x1, NULL);
            v1 = 137193;
            WriteProcessMemory(g_1005f612, 0x4f3102, &v1, 0x4, NULL);
            v1 = 137193;
            WriteProcessMemory(g_1005f612, g_10042668 + 66, &v1, 0x4, NULL);
            v1 = 1218;
            WriteProcessMemory(g_1005f612, 0x549f80, &v1, 0x3, NULL);
            return 0;
        }
        else
        {
            if (a2 == 1003)
            {
                count1 = SendDlgItemMessageA(a0, 1003, 240, NULL, NULL);
                g_10134d82 = count1;
                sub_10001160(count1);
                return 0;
            }
            return 0;
        }
    }
}
```

## dlgProc_LinksProxy `0x1001ef0c`

Named — see [doc 10](../../10-*.md). _1649 bytes. calls CreateThread, SendDlgItemMessageA; refs "Stop Proxy", "Run Proxy", "exura"_

```c
extern LPARAM g_10043544;
extern LPARAM g_100435c8;
extern char g_1005f651;
extern unsigned int g_1005f884;
extern unsigned int g_10072f78;
extern char g_100f0d37;
extern SOCKET g_100f0da8;
extern int g_1013f280;
extern int g_1013f2a0;
extern int g_1013f2e0;
extern int g_1013f300;
extern int g_1013f304;
extern WPARAM g_1013f308;
extern WPARAM g_1013f30c;
extern int g_1013f310;
extern WPARAM g_1013f314;
extern unsigned int g_1013f318;
extern unsigned int g_102898c4;
extern unsigned int g_102898c8;
extern char g_102898cd;

int sub_1001ef0c(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    LPARAM *i;  // ebx
    LRESULT count;  // eax
    LRESULT count1;  // eax
    LRESULT count2;  // eax
    LRESULT v5;  // eax
    LRESULT v6;  // eax
    unsigned int v0;  // [bp-0x30]

    if (a1 == 272)
    {
        if (g_102898cd == 1)
            SendDlgItemMessageA(a0, 1007, 12, NULL, "Stop Proxy");
        else
            SendDlgItemMessageA(a0, 1007, 12, NULL, "Run Proxy");
        SendDlgItemMessageA(a0, 1006, 12, NULL, &g_1013f280);
        SendDlgItemMessageA(a0, 1009, 12, NULL, &g_1013f2a0);
        SendDlgItemMessageA(a0, 1010, 12, NULL, &g_1013f2e0);
        sub_10040940(g_1013f300, &g_1005f651);
        SendDlgItemMessageA(a0, 1004, 12, NULL, &g_1005f651);
        sub_10040940(g_1013f304, &g_1005f651);
        SendDlgItemMessageA(a0, 1017, 12, NULL, &g_1005f651);
        sub_10040940(g_1013f310, &g_1005f651);
        SendDlgItemMessageA(a0, 0x3fd, 12, NULL, &g_1005f651);
        SendDlgItemMessageA(a0, 1001, 385, NULL, "exura");
        SendDlgItemMessageA(a0, 1001, 385, 0x1, "exura gran");
        SendDlgItemMessageA(a0, 1001, 385, 0x2, "exura vita");
        SendDlgItemMessageA(a0, 1001, 385, 0x3, "exana mort");
        SendDlgItemMessageA(a0, 1001, 385, 0x4, "exura san");
        SendDlgItemMessageA(a0, 1001, 390, g_1013f308, NULL);
        SendDlgItemMessageA(a0, 1015, 385, NULL, "Light");
        SendDlgItemMessageA(a0, 1015, 385, 0x1, "Strong");
        SendDlgItemMessageA(a0, 1015, 385, 0x2, "Great");
        SendDlgItemMessageA(a0, 1015, 385, 0x3, "Ultimate");
        SendDlgItemMessageA(a0, 1015, 385, 0x4, "Spirit");
        SendDlgItemMessageA(a0, 1015, 385, 0x5, "UH Rune");
        SendDlgItemMessageA(a0, 1015, 390, g_1013f30c, NULL);
        SendDlgItemMessageA(a0, 1019, 385, NULL, "Light");
        SendDlgItemMessageA(a0, 1019, 385, 0x1, "Strong");
        SendDlgItemMessageA(a0, 1019, 385, 0x2, "Great");
        SendDlgItemMessageA(a0, 1019, 385, 0x3, "Spirit");
        SendDlgItemMessageA(a0, 1019, 390, g_1013f314, NULL);
        SendDlgItemMessageA(a0, 0x3ff, 385, NULL, "No Action");
        SendDlgItemMessageA(a0, 0x3ff, 385, 0x1, "Attack");
        SendDlgItemMessageA(a0, 0x3ff, 385, 0x2, "Follow");
        for (i = &g_10043544; i < &g_100435c8; i += 1)
        {
            SendDlgItemMessageA(a0, 1026, 385, 0xffffffff, *(i));
        }
        SendDlgItemMessageA(a0, 0x3ff, 390, g_1013f318 >> 6, NULL);
        SendDlgItemMessageA(a0, 1026, 390, g_1013f318 & 63, NULL);
        v0 = a0;
        g_10072f78 = a0;
        sub_1000307e(a0, 1004, "Normally your IP address will be filled in automatically but if you use a proxy or router you might need to set this manually. Leave this field blank if you don't use any. The other clients will use this IP address to connect.");
        sub_1000307e(a0, 1006, "This is the server port that will be opened to listen for incomming connections. If you're behind a proxy or router, then you may need to use port forwarding. Look for information on google on how to do this for your specific router.");
        sub_1000307e(a0, 1014, "The account number to use by other clients when loggin in. The password is always 'elfbot'.");
        sub_1000307e(a0, 1003, "If this option is enabled, the clients that connect to you will be able to control your character. If not they will only be able to watch and cannot control your character. This takes effect as soon as it's checked/unchecked and can be done so during a session.");
        sub_1000307e(a0, 1007, "This activates the link server, or shuts it down if it is active.");
        sub_1000307e(a0, 1009, "The IP address of the Links server to be used when connecting.");
        sub_1000307e(a0, 1010, "The port to use when connecting to the Links server.");
        sub_1000307e(a0, 1008, "Click this button to set these client settings to be used when pressing the 'Enter Game' button.");
        return 0;
    }
    else if (a1 != 273)
    {
        return (unsigned int)sub_10002c6e(a0, a1, a2, a3);
    }
    else if (a2 == 1007)
    {
        if (!g_102898cd)
        {
            SendDlgItemMessageA(a0, 1006, 13, 0x20, &g_1013f280);
            SendDlgItemMessageA(a0, 1007, 12, NULL, "Stop Proxy");
            g_102898cd = 1;
            CreateThread(NULL, NULL, sub_100209d5, NULL, THREAD_CREATE_RUN_IMMEDIATELY, &g_1005f884);
            return 0;
        }
        g_102898cd = 0;
        if (g_100f0da8)
        {
            shutdown(g_100f0da8, SD_BOTH);
            closesocket(g_100f0da8);
            g_100f0da8 = 0;
        }
        SendDlgItemMessageA(a0, 1007, 12, NULL, "Run Proxy");
        return 0;
    }
    else
    {
        if (a2 == 1008)
        {
            SendDlgItemMessageA(a0, 1009, 13, 0x40, &g_1013f2a0);
            SendDlgItemMessageA(a0, 1010, 13, 0x20, &g_1013f2e0);
            SendDlgItemMessageA(a0, 1004, 13, 0x20, &g_1005f651);
            g_1013f300 = sub_10040900(&g_1005f651);
            SendDlgItemMessageA(a0, 1017, 13, 0x20, &g_1005f651);
            g_1013f304 = sub_10040900(&g_1005f651);
            SendDlgItemMessageA(a0, 0x3fd, 13, 0x20, &g_1005f651);
            g_1013f310 = sub_10040900(&g_1005f651);
            count = SendDlgItemMessageA(a0, 1001, 392, NULL, NULL);
            if (count != 0xffffffff)
                g_1013f308 = count;
            count1 = SendDlgItemMessageA(a0, 1015, 392, NULL, NULL);
            if (count1 != 0xffffffff)
                g_1013f30c = count1;
            count2 = SendDlgItemMessageA(a0, 1019, 392, NULL, NULL);
            if (count2 != 0xffffffff)
                g_1013f314 = count2;
            v5 = SendDlgItemMessageA(a0, 0x3ff, 392, NULL, NULL);
            if (v5 != 0xffffffff)
            {
                g_1013f318 = g_1013f318 & 63;
                g_1013f318 = g_1013f318 | v5 * 64;
            }
            v6 = SendDlgItemMessageA(a0, 1026, 392, NULL, NULL);
            if (v6 != 0xffffffff)
            {
                g_1013f318 = g_1013f318 & 0xffffffc0;
                g_1013f318 = g_1013f318 | v6;
            }
            g_100f0d37 = 1;
            return 0;
        }
        else
        {
            if (a2 != 1025)
                return 0;
            g_100f0d37 = 0;
            g_102898c8 = 0;
            g_102898c4 = 0;
            return 0;
        }
    }
}
```

## `sub_1001f57d` `0x1001f57d`

_64 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f60a;
extern unsigned int g_1005f626;

LRESULT sub_1001f57d(HWND a0, int a1, unsigned int a2)
{
    unsigned int v0;  // [bp-0x8]

    if (!IsWindow(a0))
    {
        v0 = 0;
        return sub_10002c87(g_1005f60a, a1, g_1005f626, a2);
    }
    ShowWindow(a0, SW_SHOW);
    return SetFocus(a0);
}
```

## `sub_1001f5bd` `0x1001f5bd`

_2882 bytes. calls SendDlgItemMessageA, SendMessageA_

```c
extern char g_1005f537;
extern char g_1005f651;
extern HWND g_10072f80;
extern HWND g_10072f84;
extern HWND g_10072f88;
extern HWND g_10072f90;
extern HWND g_10072fb8;
extern HWND g_10072fbc;
extern HWND g_10072fc4;
extern HWND g_10072fcc;
extern int g_100f9495;
extern int g_100f9499;
extern int g_100f949d;
extern WPARAM g_100f94c1;
extern char g_100f94c6;
extern char g_100f94c7;
extern char g_100f94c8;
extern char g_100f94c9;
extern char g_100f94ca;
extern unsigned int g_100f94cb;
extern char g_100fa4ef;
extern char g_100fa4f0;
extern int g_100fa4f1;
extern int g_100fa531;
extern int g_100fa571;
extern int g_100fa575;
extern char g_100fa579;
extern char g_100fa97a;
extern char g_100fa97b;
extern int g_1012ad5f;
extern int g_1012fd60;
extern char g_10134e63;
extern char g_10134e64;
extern char g_10134e65;
extern int g_10134e66;
extern char g_10134e6a;
extern int g_10134e6b;
extern char g_1013526c;
extern char g_1013526d;
extern char g_1013526e;
extern char g_1013526f;
extern char g_10135270;
extern char g_10135271;
extern char g_10135272;
extern char g_10135273;
extern char g_10135274;
extern char g_10135275;
extern char g_10135276;
extern char g_10135277;
extern char g_10135278;
extern char g_1013527a;
extern int g_1013527b;
extern int g_1013a27c;
extern char g_1013f27d;
extern char g_1013f27e;
extern char g_1013f27f;
extern WPARAM g_1013f320;
extern char g_1013f324;
extern char g_1013f325;
extern char g_1013f326;
extern int g_1014f38a;
extern int g_1014f3aa;
extern int g_1014f3ca;
extern int g_1014f3ea;
extern char g_1014f40a;
extern char g_1014f40b;
extern char g_1014f40c;
extern char g_1014f40d;
extern char g_1014f40e;
extern char g_1014f40f;
extern WPARAM g_1014f410;
extern char g_1014f415;
extern char g_1014f416;
extern char g_1014f417;
extern char g_1014f418;
extern char g_1014f419;
extern int g_1014f41a;
extern char g_1014f41e;
extern char g_1014f41f;
extern char g_101d5e20;
extern char g_101d5e21;
extern char g_101d5e22;
extern char g_101d5e23;
extern char g_101d5e24;
extern char g_101d5e25;
extern char g_101d5e26;
extern char g_101d5e27;
extern char g_101d5e29;
extern char g_101d5e2a;
extern int g_101d5e2c;
extern int g_101d5e4c;
extern char g_101d5e6c;
extern char g_101d5e6d;
extern char g_101d5e6e;
extern char g_101d5e6f;
extern char g_101d5e70;
extern char g_101d5e71;
extern char g_101d5e72;
extern char g_101d5e73;

int sub_1001f5bd(void)
{
    WPARAM v1;  // ebx
    WPARAM v2;  // ebx
    WPARAM v11;  // ebx
    WPARAM v12;  // ebx
    WPARAM v13;  // ebx
    WPARAM v14;  // ebx
    WPARAM v15;  // ebx
    WPARAM v16;  // ebx
    WPARAM v17;  // ebx
    WPARAM v18;  // ebx
    WPARAM v19;  // ebx
    WPARAM v20;  // ebx
    WPARAM v3;  // ebx
    WPARAM v21;  // ebx
    WPARAM v22;  // ebx
    WPARAM v23;  // ebx
    WPARAM v24;  // ebx
    WPARAM v25;  // ebx
    WPARAM v26;  // ebx
    WPARAM v27;  // ebx
    WPARAM v28;  // ebx
    WPARAM v29;  // ebx
    WPARAM v30;  // ebx
    WPARAM v4;  // ebx
    int v31;  // eax
    WPARAM v5;  // ebx
    WPARAM v6;  // ebx
    WPARAM v7;  // ebx
    WPARAM v8;  // ebx
    WPARAM v9;  // ebx
    WPARAM v10;  // ebx

    if (IsWindow(g_10072f84))
    {
        SendMessageA(g_10072f84, 16, NULL, NULL);
        DestroyWindow(g_10072f84);
    }
    if (IsWindow(g_10072fcc))
    {
        SendMessageA(g_10072fcc, 16, NULL, NULL);
        DestroyWindow(g_10072fcc);
    }
    sub_100201d3();
    SendDlgItemMessageA(g_10072fbc, 1011, 241, g_100f94c9, NULL);
    SendDlgItemMessageA(g_10072fbc, 1003, 241, g_1013f27d, NULL);
    SendDlgItemMessageA(g_10072fbc, 1010, 241, g_100fa4ef, NULL);
    SendDlgItemMessageA(g_10072fbc, 1008, 241, g_100fa97a, NULL);
    SendDlgItemMessageA(g_10072fbc, 1002, 241, g_10134e6a, NULL);
    SendDlgItemMessageA(g_10072fbc, 1001, 241, g_1013f320, NULL);
    SendDlgItemMessageA(g_10072fbc, 1007, 241, g_100fa97b, NULL);
    v1 = _INSERT(g_100fa97b, 0, g_1014f40a);
    SendDlgItemMessageA(g_10072fbc, 1027, 241, v1, NULL);
    v2 = _INSERT(v1, 0, g_1014f40b);
    SendDlgItemMessageA(g_10072fbc, 1033, 241, v2, NULL);
    v3 = _INSERT(v2, 0, g_1014f40c);
    SendDlgItemMessageA(g_10072fbc, 0x404, 241, v3, NULL);
    v4 = _INSERT(v3, 0, g_1014f40d);
    SendDlgItemMessageA(g_10072fbc, 1009, 241, v4, NULL);
    v5 = _INSERT(v4, 0, g_1014f40e);
    SendDlgItemMessageA(g_10072fbc, 1025, 241, v5, NULL);
    v6 = _INSERT(v5, 0, g_1014f40f);
    SendDlgItemMessageA(g_10072fbc, 1026, 241, v6, NULL);
    v7 = _INSERT(v6, 0, g_101d5e6c);
    SendDlgItemMessageA(g_10072fbc, 1040, 241, v7, NULL);
    SendDlgItemMessageA(g_10072fbc, 1015, 12, NULL, &g_10134e6b);
    SendDlgItemMessageA(g_10072fbc, 1017, 12, NULL, &g_1014f38a);
    SendDlgItemMessageA(g_10072fbc, 0x3fe, 12, NULL, &g_1014f3ca);
    SendDlgItemMessageA(g_10072fbc, 0x3fc, 12, NULL, &g_1014f3aa);
    SendDlgItemMessageA(g_10072fbc, 1037, 12, NULL, &g_101d5e2c);
    SendDlgItemMessageA(g_10072fbc, 1039, 12, NULL, &g_101d5e4c);
    SendDlgItemMessageA(g_10072fbc, 1012, 390, g_100f94cb >> 6, NULL);
    SendDlgItemMessageA(g_10072fbc, 1006, 390, g_100f94cb & 63, NULL);
    SendDlgItemMessageA(g_10072fbc, 1004, 241, g_1013f27f, NULL);
    SendDlgItemMessageA(g_10072fbc, 1036, 241, g_1014f41e, NULL);
    SendDlgItemMessageA(g_10072fbc, 0x400, 241, g_1014f41f, NULL);
    SendDlgItemMessageA(g_10072fbc, 1042, 390, g_101d5e2a, NULL);
    SendDlgItemMessageA(g_10072f88, 1004, 241, g_100f94ca, NULL);
    SendDlgItemMessageA(g_10072f88, 1006, 241, g_100f94c6, NULL);
    SendDlgItemMessageA(g_10072f88, 1003, 241, g_1013f27e, NULL);
    SendDlgItemMessageA(g_10072f88, 1005, 241, g_1013f324, NULL);
    SendDlgItemMessageA(g_10072f88, 1007, 241, g_1013f325, NULL);
    SendDlgItemMessageA(g_10072f88, 1008, 241, g_1013f326, NULL);
    SendDlgItemMessageA(g_10072f88, 1009, 241, ~(g_100fa4f0) & 1, NULL);
    SendDlgItemMessageA(g_10072f88, 1010, 241, g_1014f416, NULL);
    SendDlgItemMessageA(g_10072f88, 1011, 241, g_1014f417, NULL);
    SendDlgItemMessageA(g_10072f88, 1012, 241, g_1014f418, NULL);
    SendDlgItemMessageA(g_10072f88, 1014, 241, g_101d5e27, NULL);
    SendDlgItemMessageA(g_10072f88, 1015, 241, g_101d5e29, NULL);
    SendDlgItemMessageA(g_10072f88, 1016, 241, g_101d5e6d, NULL);
    SendDlgItemMessageA(g_10072f88, 1017, 241, g_101d5e73, NULL);
    SendDlgItemMessageA(g_10072f88, 1018, 241, g_101d5e72, NULL);
    SendDlgItemMessageA(g_10072fc4, 1003, 241, g_100fa579, NULL);
    SendDlgItemMessageA(g_10072fc4, 1005, 241, g_100f94c8, NULL);
    v8 = _INSERT(g_100f94c8, 0, g_1013526d);
    SendDlgItemMessageA(g_10072fc4, 1012, 241, v8, NULL);
    v9 = _INSERT(v8, 0, g_1013526e);
    SendDlgItemMessageA(g_10072fc4, 1011, 241, v9, NULL);
    v10 = _INSERT(v9, 0, g_1013526f);
    SendDlgItemMessageA(g_10072fc4, 1014, 241, v10, NULL);
    v11 = _INSERT(v10, 0, g_10135270);
    SendDlgItemMessageA(g_10072fc4, 1013, 241, v11, NULL);
    v12 = _INSERT(v11, 0, g_10135271);
    SendDlgItemMessageA(g_10072fc4, 1010, 241, v12, NULL);
    v13 = _INSERT(v12, 0, g_10135272);
    SendDlgItemMessageA(g_10072fc4, 1004, 241, v13, NULL);
    v14 = _INSERT(v13, 0, g_10135273);
    SendDlgItemMessageA(g_10072fc4, 1002, 241, v14, NULL);
    v15 = _INSERT(v14, 0, g_10135274);
    SendDlgItemMessageA(g_10072fc4, 1006, 241, v15, NULL);
    v16 = _INSERT(v15, 0, g_10135275);
    SendDlgItemMessageA(g_10072fc4, 1008, 241, v16, NULL);
    v17 = _INSERT(v16, 0, g_10135276);
    SendDlgItemMessageA(g_10072fc4, 1009, 241, v17, NULL);
    v18 = _INSERT(v17, 0, g_10135277);
    SendDlgItemMessageA(g_10072fc4, 1015, 241, v18, NULL);
    v19 = _INSERT(v18, 0, g_1013527a);
    SendDlgItemMessageA(g_10072fc4, 1016, 241, v19, NULL);
    v20 = _INSERT(v19, 0, g_101d5e20);
    SendDlgItemMessageA(g_10072fc4, 1017, 241, v20, NULL);
    v21 = _INSERT(v20, 0, g_101d5e21);
    SendDlgItemMessageA(g_10072fc4, 1018, 241, v21, NULL);
    sub_1002b02b(1);
    SendDlgItemMessageA(g_10072f80, 0x3ff, 12, NULL, &g_100fa4f1);
    sub_10040940(g_100f9495, &g_1005f651);
    SendDlgItemMessageA(g_10072f80, 0x3fc, 12, NULL, &g_1005f651);
    sub_10040940(g_100f9499, &g_1005f651);
    SendDlgItemMessageA(g_10072f80, 1018, 12, NULL, &g_1005f651);
    SendDlgItemMessageA(g_10072f80, 1009, 12, NULL, &g_100fa531);
    sub_10040940(g_100fa575, &g_1005f651);
    SendDlgItemMessageA(g_10072f80, 1011, 12, NULL, &g_1005f651);
    sub_10040940(g_100fa571, &g_1005f651);
    SendDlgItemMessageA(g_10072f80, 1013, 12, NULL, &g_1005f651);
    sub_10040940(g_100f949d, &g_1005f651);
    SendDlgItemMessageA(g_10072f80, 1016, 12, NULL, &g_1005f651);
    sub_10040940(g_10134e66, &g_1005f651);
    SendDlgItemMessageA(g_10072f80, 1006, 12, NULL, &g_1005f651);
    sub_10040940(g_1014f41a, &g_1005f651);
    SendDlgItemMessageA(g_10072f80, 1029, 12, NULL, &g_1005f651);
    SendDlgItemMessageA(g_10072f80, 1034, 390, g_100f94c1, NULL);
    SendDlgItemMessageA(g_10072f80, 1014, 390, g_1014f410, NULL);
    SendDlgItemMessageA(g_10072f80, 1003, 390, g_10134e63, NULL);
    SendDlgItemMessageA(g_10072f80, 1032, 390, g_1014f419, NULL);
    SendDlgItemMessageA(g_10072f80, 1026, 390, g_10134e64, NULL);
    SendDlgItemMessageA(g_10072f80, 0x400, 390, g_10134e65, NULL);
    SendDlgItemMessageA(g_10072f80, 1032, 390, g_1014f415, NULL);
    SendDlgItemMessageA(g_10072fb8, 1003, 12, NULL, &g_1012ad5f);
    SendDlgItemMessageA(g_10072fb8, 1002, 12, NULL, &g_1012fd60);
    SendDlgItemMessageA(g_10072fb8, 1011, 12, NULL, &g_1013527b);
    SendDlgItemMessageA(g_10072fb8, 1008, 12, NULL, &g_1013a27c);
    SendDlgItemMessageA(g_10072fb8, 1014, 12, NULL, &g_1014f3ea);
    SendDlgItemMessageA(g_10072fb8, 1006, 241, g_100f94c7, NULL);
    v22 = _INSERT(g_100f94c7, 0, g_10135278);
    SendDlgItemMessageA(g_10072fb8, 1007, 241, v22, NULL);
    v23 = _INSERT(v22, 0, g_101d5e6e);
    SendDlgItemMessageA(g_10072fb8, 1017, 241, v23, NULL);
    v24 = _INSERT(v23, 0, g_101d5e6f);
    SendDlgItemMessageA(g_10072fb8, 1018, 241, v24, NULL);
    v25 = _INSERT(v24, 0, g_101d5e70);
    SendDlgItemMessageA(g_10072fb8, 0x3fc, 241, v25, NULL);
    v26 = _INSERT(v25, 0, g_101d5e71);
    SendDlgItemMessageA(g_10072fb8, 1019, 241, v26, NULL);
    SendDlgItemMessageA(g_10072f90, 0x3ff, 241, g_101d5e22, NULL);
    v27 = _INSERT(g_101d5e22, 0, g_101d5e24);
    SendDlgItemMessageA(g_10072f90, 1037, 241, v27, NULL);
    v28 = _INSERT(v27, 0, g_101d5e23);
    SendDlgItemMessageA(g_10072f90, 1068, 241, v28, NULL);
    v29 = _INSERT(v28, 0, g_101d5e25);
    SendDlgItemMessageA(g_10072f90, 1071, 241, v29, NULL);
    v30 = _INSERT(v29, 0, g_101d5e26);
    SendDlgItemMessageA(g_10072f90, 1074, 241, v30, NULL);
    sub_10039d8a(g_1014f41a, &g_1005f651, g_10134e66, &g_1005f651, g_100f949d);
    v31 = sub_1002387b();
    if (g_1005f537)
    {
        return v31;
    }
    else if (g_1013526c)
    {
        return sub_10007a08();
    }
    else
    {
        return v31;
    }
}
```

## `sub_100200ff` `0x100200ff`

_207 bytes. calls CreateFileA, WriteFile_

```c
extern int g_10042d7b;
extern int g_100445f1;
extern char g_1005dc8c;
extern unsigned int g_1005f622;
extern char g_1005f7b1;
extern Byte g_100f9494;

int sub_100200ff(void)
{
    unsigned int v4;  // eax
    char v0;  // [bp-0x154]
    Byte v1[300];  // [bp-0x134]
    HANDLE v2;  // [bp-0x8]

    if (g_1005dc8c)
    {
        lstrcpy(v1, &g_1005dc8c);
    }
    else if (g_1005f7b1)
    {
        lstrcpy(v1, &g_10042d7b);
        lstrcat(v1, &g_1005f7b1);
        if (g_100445f1 != 1)
        {
            sub_10040940(g_100445f1, &v0);
            lstrcat(v1, &v0);
        }
    }
    else
    {
        return v4;
    }
    v2 = CreateFileA(v1, 0xc0000000, 3, NULL, OPEN_ALWAYS, FILE_ATTRIBUTE_ARCHIVE, NULL);
    if (v2 == 0xffffffff)
        return sub_100159d8();
    WriteFile(v2, &g_100f9494, 903650, &g_1005f622, NULL);
    return CloseHandle(v2);
}
```

## `sub_10020124` `0x10020124`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10020124(void)
{
}
```

## `sub_100201d3` `0x100201d3`

_560 bytes. calls CreateFileA; refs "Default"_

```c
extern int g_10042d7b;
extern int g_100445f1;
extern char g_1005dc8c;
extern char g_1005f7b1;
extern unsigned int g_1008b941;
extern unsigned int g_1008b945;
extern unsigned int g_100f49fd;
extern char g_100f4b09;
extern int g_100f9494;
extern char g_100f94a1;
extern char g_100f94ef;
extern int g_100f9cef;
extern int g_100fa4f1;
extern int g_1012ad5f;
extern int g_1012fd60;
extern void g_10134d61;
extern unsigned int g_10134d65;

LRESULT sub_100201d3(void)
{
    unsigned int v8;  // eax
    unsigned int v9;  // eax
    unsigned int idx;  // ecx
    unsigned int v0;  // [bp-0x164]
    char v1;  // [bp-0x160]
    Byte v2[300];  // [bp-0x140]
    unsigned int v3;  // [bp-0x14]
    unsigned int size;  // [bp-0x10]
    HANDLE v5;  // [bp-0xc]
    HANDLE v6;  // [bp-0x8]

    v0 = 0;
    if (g_100f4b09)
    {
        lstrcpy(v2, &g_10042d7b);
        lstrcat(v2, &g_100f4b09);
    }
    else if (g_1005dc8c)
    {
        lstrcpy(v2, &g_1005dc8c);
    }
    else
    {
        if (!g_1005f7b1)
            goto LABEL_10020367;
        lstrcpy(v2, &g_10042d7b);
        lstrcat(v2, &g_1005f7b1);
        if (g_100445f1 != 1)
        {
            sub_10040940(g_100445f1, &v1);
            lstrcat(v2, &v1);
        }
    }
    while (true)
    {
        v6 = CreateFileA(v2, 0x80000000, FILE_SHARE_NONE, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_ARCHIVE, NULL);
        if (v6 != 0xffffffff)
        {
            v5 = CreateFileMappingA(v6, NULL, PAGE_READONLY, 0, 0, NULL);
            size = GetFileSize(v6, &v3);
            v8 = (unsigned int)MapViewOfFile(v5, FILE_MAP_READ, 0, 0, NULL);
            if (size > 903648)
                size = 903648;
            v9 = sub_1002ae6f(&g_100f9494, v8, size);
            UnmapViewOfFile(v9);
            CloseHandle(v5);
            CloseHandle(v6);
            break;
        }
        else
        {
            if (g_1005dc8c || v0)
                break;
            v0 = 1;
            lstrcpy(v2, &g_10042d7b);
            lstrcat(v2, "Default");
        }
    }
LABEL_10020367:
    if (g_100f94a1)
    {
        sub_1002ae6f(&g_100fa4f1, &g_100f94a1, 32);
        g_100f94a1 = 0;
    }
    if (g_100f94ef)
    {
        lstrcpy(&g_1012ad5f, &g_100f94ef);
        lstrcpy(&g_1012fd60, &g_100f9cef);
        g_100f94ef = 0;
    }
    for (idx = 0; idx < 10; idx += 1)
    {
        (&g_1008b945)[idx] = 0;
    }
    if (!g_10134d61)
    {
        *((unsigned int *)&g_10134d61) = 808988724;
        g_10134d65 = 0x4646;
    }
    sub_1002040d();
    g_1008b941 = 0;
    g_100f49fd = 0;
    sub_10008284();
    return sub_1001b815();
}
```

## `sub_10020216` `0x10020216`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10020216(void)
{
}
```

## `sub_10020237` `0x10020237`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10020237(void)
{
}
```

## `sub_1002040d` `0x1002040d`

_162 bytes. calls CreateFileA; refs "lootitems.txt"_

```c
extern int g_10042d7b;

int sub_1002040d(void)
{
    Byte v0[4];  // [bp-0x140], Other Possible Types: int
    int v1;  // [bp-0x13c]
    int v2;  // [bp-0x138]
    int v3;  // [bp-0x134]
    int v4;  // [bp-0x130]
    unsigned int v5;  // [bp-0x14]
    unsigned int size;  // [bp-0x10]
    HANDLE v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]

    lstrcpy(v0, &g_10042d7b);
    lstrcat(v0, "lootitems.txt");
    v8 = CreateFileA(v0, 0x80000000, FILE_SHARE_NONE, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_ARCHIVE, NULL);
    if (v8 == 4294967295)
        return v8;
    v7 = CreateFileMappingA(v8, NULL, PAGE_READONLY, 0, 0, NULL);
    size = GetFileSize(v8, &v5);
    MapViewOfFile(v7, FILE_MAP_READ, 0, 0, NULL);
    UnmapViewOfFile(sub_100204af(v0, v1, v2, v3, v4));
    CloseHandle(v7);
    return CloseHandle(v8);
}
```

