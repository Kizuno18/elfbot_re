# elfbot.dll decompiled — jdrv 0x10021e74..0x1002653b

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10021e74` `0x10021e74`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10021e74(void)
{
}
```

## `sub_10021ed2` `0x10021ed2`

_52 bytes. (leaf/helper — see body)_

```c
int sub_10021ed2(unsigned int a0)
{
    return _INSERT(*((char *)(1 + (a0 - *((int *)*((int *)0x7998dc))) * 80 + *((int *)(*((int *)0x7998dc) + 8)) + 36)), 0, *((char *)(1 + (a0 - *((int *)*((int *)0x7998dc))) * 80 + *((int *)(*((int *)0x7998dc) + 8)) + 36)) & 25);
}
```

## `sub_10021f06` `0x10021f06`

_52 bytes. (leaf/helper — see body)_

```c
int sub_10021f06(unsigned int a0)
{
    return _INSERT(*((char *)(1 + (a0 - *((int *)*((int *)0x7998dc))) * 80 + *((int *)(*((int *)0x7998dc) + 8)) + 35)), 0, *((char *)(1 + (a0 - *((int *)*((int *)0x7998dc))) * 80 + *((int *)(*((int *)0x7998dc) + 8)) + 35)) & 32);
}
```

## `sub_10021f3a` `0x10021f3a`

_50 bytes. (leaf/helper — see body)_

```c
int sub_10021f3a(void)
{
    long long v0;  // [bp-0x20]
    long long v1;  // [bp-0x18]
    unsigned long v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0x8]

    QueryPerformanceFrequency(&v0);
    QueryPerformanceCounter(&v1);
    v3 = 1000;
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
    v2 = (/* unsupported instruction */ ? /* unsupported instruction */ : nan);
    /* unsupported instruction */
    return v2;
}
```

## `sub_10021f6c` `0x10021f6c`

_1516 bytes. calls CreateFileA, GetAsyncKeyState, ReadFile, SendDlgItemMessageA, SendMessageA; refs "Lighthack - ", "Off"_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
} struct_0;

extern char g_1002206e;
extern char g_100222d3;
extern char g_100224e2;
extern int g_10042d7b;
extern void g_100432a4;
extern unsigned int g_100432a8;
extern unsigned int g_10043956;
extern unsigned int g_100580f8;
extern unsigned int g_100580fc;
extern unsigned int g_1005db8c;
extern unsigned int g_1005db90;
extern unsigned int g_1005db94;
extern unsigned int g_1005db98;
extern char g_1005dc48;
extern char g_1005dd90;
extern char g_1005f609;
extern unsigned int g_1005f622;
extern HWND g_1005f626;
extern char g_1005f888;
extern HWND g_10072f8c;
extern HWND g_10072f94;
extern unsigned int g_10072fb0;
extern char g_100ee8bb;
extern char g_100f0d3a;
extern char g_100f0d3b;
extern char g_100f0e42;
extern char g_100f4a09;
extern char g_100f4a89;
extern char g_100f4b09;
extern char g_100f4b89;
extern char g_100f4c09;
extern unsigned int g_100f9359;
extern unsigned int g_100f935d;
extern unsigned int g_100f9361;
extern char g_100f94ca;
extern char g_101d5e20;
extern unsigned int g_10291cd2;
extern unsigned int g_10291cd6;
extern unsigned int g_10291cda;
extern unsigned int g_102922f6;
extern unsigned int g_102922fa;
extern unsigned int g_102922fe;

void sub_10021f6c(void)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    struct_0 **ch;  // eax
    unsigned int idx[24];  // eax
    unsigned int v20;  // ftop
    unsigned int v21;  // ftop
    unsigned int v22[24];  // eax
    HANDLE v23;  // ebx
    HANDLE v24;  // eax
    unsigned short v11;  // fs
    unsigned long v12;  // 4124
    unsigned int v13;  // 4103
    unsigned long v14;  // 4132
    unsigned int v15;  // ftop
    void* v0;  // [bp-0xa0]
    char *v1;  // [bp-0x9c], Other Possible Types: unsigned int
    struct_0 **v2;  // [bp-0x98]
    unsigned int v3;  // [bp-0x94]
    unsigned int v4;  // [bp-0x8c]
    char v5;  // [bp-0x88]
    struct_0 **v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v13 = *((int *)v12);
    v3 = *((int *)v12);
    v14 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v14) = &v3;
    g_10291cd2 = &v3;
    g_10291cd6 = &v7;
    while (true)
    {
        g_1005db98 = &v7;
        g_1005db94 = &v3;
        g_1005db8c = 1;
        g_1005db90 = &g_1002206e;
        if (g_1005dc48)
            g_1005dc48 = g_1005dc48 - 1;
        if (g_100580f8)
        {
            sub_10009452();
            g_100580f8 = 0;
        }
        if (g_100580fc)
        {
            g_100580fc = 0;
            if (g_100f0d3b)
            {
                g_100f0d3b = 0;
                SendDlgItemMessageA(g_10072f8c, 1046, 241, NULL, NULL);
            }
            if (g_100f0e42)
            {
                g_100f0e42 = 0;
                SendDlgItemMessageA(g_10072f94, 1012, 241, NULL, NULL);
            }
        }
        if (g_1005dd90)
        {
            SetWindowTextA(sub_10039b62(), &g_1005dd90);
            g_1005dd90 = 0;
        }
        g_1005db98 = &v7;
        g_1005db94 = &v3;
        g_1005db8c = 10;
        g_1005db90 = &g_100222d3;
        v2 = &v6;
        GetWindowThreadProcessId(GetForegroundWindow(), &v6);
        ch = GetCurrentProcessId();
        if (ch == v6)
            g_10291cda = 1;
        else
            g_10291cda = 0;
        if (g_100ee8bb || !((v2 = v2, !g_100f94ca)))
        {
            v2 = ch;
            if (ch == v6)
            {
                v2 = ch;
                if (!g_102922fe)
                    goto LABEL_10022171;
                v1 = g_102922f6;
                *((unsigned int *)&g_100432a4) = g_102922f6;
                v1 = g_102922fa;
                g_100432a8 = g_102922fa;
                g_102922fe = 0;
            }
            else
            {
                if (!g_102922fe)
                {
                    idx = 5384848() + 88;
                    v1 = idx[0];
                    g_102922f6 = idx[0];
                    v1 = idx[1];
                    g_102922fa = idx[1];
                    g_102922fe = 1;
                }
                v4 = 35;
                v20 = v15 - 1;
                if (/* unsupported instruction */)
                {
                    v21 = v20 - 1;
                    /* unsupported instruction */
                    /* unsupported instruction */
                }
                else
                {
                    v21 = v20 - 1;
                    /* unsupported instruction */
                    /* unsupported instruction */
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
                if (/* unsupported instruction */)
                {
                    *((int *)&g_100432a4) = /* unsupported instruction */;
                    /* unsupported instruction */
                    v15 = v21 + 1;
                }
                else
                {
                    *((unsigned long long *)&g_100432a4) = nan;
                    /* unsupported instruction */
                    v15 = v21 + 1;
                }
            }
            v22 = 5384848() + 88;
            v22[0] = *((int *)&g_100432a4);
            v22[1] = g_100432a8;
            v2 = ch;
        }
LABEL_10022171:
        if (ch == v6)
        {
            if (g_1005f609)
                ShowWindow(g_1005f626, SW_SHOW);
            SendMessageA(g_1005f626, 1337, 0x1, NULL);
            g_100f9359 = GetAsyncKeyState(0x11);
            g_100f9361 = GetAsyncKeyState(18);
            v1 = 0x10;
            g_100f935d = GetAsyncKeyState(16);
            if (g_1005f888)
            {
                g_1005f888 = g_1005f888 - 1;
            }
            else
            {
                if (g_100f935d)
                {
                    v1 = 0x7a;
                    if (GetAsyncKeyState(122))
                    {
                        lstrcpy(&v5, "Lighthack - ");
                        if (g_10043956 != 0xff)
                        {
                            lstrcat(&v5, "On");
                            g_10043956 = 0xff;
                        }
                        else
                        {
                            lstrcat(&v5, "Off");
                            g_10043956 = *((int *)0x79c31c);
                        }
                        v1 = &v5;
                        sub_10039374(&v5);
                        g_1005f888 = 1;
                    }
                    if (GetAsyncKeyState(123))
                    {
                        if (g_1005f609)
                        {
                            ShowWindow(g_1005f626, SW_HIDE);
                            g_1005f609 = 0;
                        }
                        else
                        {
                            ShowWindow(g_1005f626, SW_SHOW);
                            g_1005f609 = 1;
                        }
                        g_1005f888 = 1;
                    }
                }
            }
        }
        else
        {
            if (g_1005f609)
                ShowWindow(g_1005f626, SW_HIDE);
            v1 = NULL;
            SendMessageA(g_1005f626, 1337, NULL, NULL);
        }
        g_1005db98 = &v7;
        g_1005db94 = &v1;
        g_1005db8c = 20;
        sub_10023ea2(v1, v2, v13, sub_1000264c);
        if (g_101d5e20)
        {
            g_1005db98 = &v7;
            g_1005db94 = &v1;
            g_1005db8c = 30;
            sub_10022566();
        }
        g_1005db98 = &v7;
        g_1005db94 = &v1;
        g_1005db8c = 40;
        sub_100240b1();
        g_1005db98 = &v7;
        g_1005db94 = &v1;
        g_1005db8c = 50;
        g_1005db90 = &g_100224e2;
        if (g_100f4a09)
        {
            g_100f0d3a = 1;
            sub_10015b79(&g_100f4a09, 0);
            sub_100160d6();
            g_100f0d3a = 0;
            sub_100188bf(g_10072f94, 0x404, 390, NULL, NULL);
            sub_100188bf(g_10072f94, 1035, 390, NULL, NULL);
            g_100f4a09 = 0;
        }
        if (g_100f4a89)
        {
            g_100f0d3a = 1;
            sub_10015843(&g_100f4a89, 0);
            sub_10015267(v1, v2);
            g_100f0d3a = 0;
            sub_100188bf(g_10072f8c, 0x404, 390, NULL, NULL);
            sub_100188bf(g_10072f8c, 1040, 390, NULL, NULL);
            g_100f4a89 = 0;
        }
        if (g_100f4b09)
        {
            sub_1001f5bd();
            g_100f4b09 = 0;
        }
        if (g_100f4b89)
        {
            lstrcpy(&g_100f4c09, &g_10042d7b);
            lstrcat(&g_100f4c09, &g_100f4b89);
            v23 = CreateFileA(&g_100f4c09, 0xc0000000, 3, NULL, OPEN_ALWAYS, FILE_ATTRIBUTE_ARCHIVE, NULL);
            if (v23 != 0xffffffff)
            {
                v0 = HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, 0x200000);
                ReadFile(v23, HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, 0x200000), 0x200000, &g_1005f622, NULL);
                CloseHandle(v23);
                g_10072fb0 = 0;
                sub_1001686c();
                v24 = GetProcessHeap();
                HeapFree(v24, HEAP_NONE, HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, 0x200000));
            }
            g_100f4b89 = 0;
        }
        g_1005db98 = &v7;
        g_1005db94 = &v1;
        g_1005db8c = 60;
        sub_1002af69();
        g_1005db98 = &v7;
        g_1005db94 = &v1;
        g_1005db8c = 70;
        sub_100394a7();
        g_1005db98 = &v7;
        g_1005db94 = &v1;
        g_1005db8c = 80;
        Sleep(100);
    }
}
```

## `sub_10022558` `0x10022558`

_14 bytes. (leaf/helper — see body)_

```c
void sub_10022558(void)
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

## `sub_10022566` `0x10022566`

_599 bytes. calls CreateFileA, ReadFile, WriteFile; refs "%s\r\n%d\r\n%s", "%s\\playerinfo\\%c\\%s.txt", "%s\\playerinfo\\%c\\%s.txt"_

```c
typedef struct struct_0 {
    char field_0;
    char padding_1[71];
    unsigned int field_48;
    char field_4c;
    char field_4d;
    char field_4e;
    char field_4f;
    char field_50;
} struct_0;

extern unsigned int g_10042f83;
extern unsigned int g_1005f622;
extern struct_0 g_10077175;
extern struct_0 g_100809cd;
extern char g_101d5e21;

void sub_10022566(void)
{
    struct_0 *iter;  // ebx
    unsigned int v9;  // ecx
    char *v19;  // ecx
    char *v20;  // ecx
    char *v21;  // ecx
    HANDLE v10;  // eax
    unsigned int v12;  // ecx
    HANDLE v13;  // eax
    char *node;  // ecx
    unsigned int k;  // edx
    char *v16;  // ecx
    char *iter1;  // ecx
    unsigned int v0;  // [bp-0x274]
    unsigned int v1;  // [bp-0x270]
    struct_0 *v2;  // [bp-0x26c]
    HANDLE v3;  // [bp-0x260]
    Byte v4[299];  // [bp-0x25c]
    char v5;  // [bp-0x131]
    Byte v6[300];  // [bp-0x130]

    for (iter = &g_10077175.field_0; iter < &g_100809cd.field_0; iter = (char *)&iter[1].field_48 + 3)
    {
        if (iter->field_4e == 1 && !iter->field_50)
        {
            iter->field_50 = 1;
            v2 = &iter->padding_1[31];
            v1 = iter->field_48;
            v0 = 0x10058100 + 4 * iter->field_4c;
            wsprintfA(v4, "%s\r\n%d\r\n%s");
            v9 = iter->field_0;
            if (v9 < 65 || v9 > 90)
                v9 = 64;
            v2 = iter;
            v1 = v9;
            v0 = &g_10042f83;
            wsprintfA(v6, "%s\\playerinfo\\%c\\%s.txt");
            v10 = CreateFileA(v6, 0xc0000000, 3, NULL, OPEN_ALWAYS, FILE_ATTRIBUTE_ARCHIVE, NULL);
            if (v10 != 0xffffffff)
            {
                v3 = v10;
                WriteFile(v3, v4, lstrlen(v4), &g_1005f622, NULL);
                CloseHandle(v3);
            }
        }
        else if (iter->field_4f && iter->field_4d)
        {
            v12 = iter->field_0;
            if (v12 < 65 || v12 > 90)
                v12 = 64;
            v2 = iter;
            v1 = v12;
            v0 = &g_10042f83;
            wsprintfA(v6, "%s\\playerinfo\\%c\\%s.txt");
            v13 = CreateFileA(v6, 0xc0000000, 3, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_ARCHIVE, NULL);
            if (v13 != 0xffffffff)
            {
                v3 = v13;
                sub_1002ae81(v4, 300);
                ReadFile(v3, v4, 300, &g_1005f622, NULL);
                CloseHandle(v3);
                v5 = 0;
                if (v4)
                {
                    for (node = &v4[0]; *(node); node += 1)
                    {
                        if (*(node) == 13 || *(node) == 10)
                        {
                            *(node) = 0;
                            node += 2;
                            break;
                        }
                    }
                    for (k = 0; k < 9; k += 1)
                    {
                        if (*((short *)&v4[0]) == *((int *)(0x10058100 + 4 * k)))
                        {
                            iter->field_4c = k;
                            break;
                        }
                    }
                    if (*(node))
                    {
                        v16 = node;
                        while (true)
                        {
                            iter1 = v16;
                            if (!*(iter1))
                                break;
                            if (*(iter1) == 13 || *(iter1) == 10)
                            {
                                *(iter1) = 0;
                                iter1 += 2;
                                break;
                            }
                            else
                            {
                                v16 = iter1 + 1;
                            }
                        }
                        iter->field_48 = sub_10040900(node, iter1);
                        v19 = node;
                        if (*(v19))
                        {
                            v20 = v19;
                            while (true)
                            {
                                v21 = v20;
                                if (!*(v21))
                                    break;
                                if (*(v21) == 13 || *(v21) == 10)
                                {
                                    *(v21) = 0;
                                    break;
                                }
                                else
                                {
                                    v20 = v21 + 1;
                                }
                            }
                            lstrcpyn(&iter->padding_1[31], v19, 32);
                        }
                        iter->field_50 = 1;
                        if (!g_101d5e21)
                            iter->field_4d = 0;
                    }
                }
            }
            iter->field_4f = 0;
        }
    }
    return;
}
```

## `sub_100227bd` `0x100227bd`

_3467 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[48];
    struct struct_1 *field_30;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

typedef struct struct_9 {
    char padding_0[64];
    struct struct_8 *field_40;
    char padding_44[20];
    unsigned short field_58;
    unsigned short field_5a;
    char padding_5c[50];
    char field_8e;
    char field_8f;
} struct_9;

typedef struct struct_8 {
    char padding_0[144];
    unsigned int field_90;
} struct_8;

typedef struct struct_6 {
    struct struct_0 *field_0;
} struct_6;

extern char g_100227eb;
extern char g_100228af;
extern char g_10022955;
extern char g_100229a0;
extern char g_10022a0d;
extern char g_10022ace;
extern char g_10022e5d;
extern char g_10022e6f;
extern char g_10022ef4;
extern char g_10022f51;
extern char g_10022fd0;
extern char g_10023047;
extern char g_1002309c;
extern char g_10023119;
extern char g_10023166;
extern char g_100232dd;
extern char g_100233f0;
extern char g_1002343b;
extern char g_100234d9;
extern char g_10023524;
extern char g_10023533;
extern unsigned int g_10043956;
extern struct_6 *g_10052674;
extern unsigned int g_100580e4;
extern unsigned int g_100580f0;
extern unsigned int g_100580f8;
extern unsigned int g_10058160;
extern unsigned int g_10058164;
extern unsigned int g_10058168;
extern void* g_1005816c;
extern unsigned int g_10058170;
extern unsigned int g_10058174;
extern unsigned int g_10058178;
extern unsigned int g_1005817c;
extern char g_1005db74;
extern unsigned int g_1005db78;
extern unsigned int g_1005db7c;
extern char g_1005db80;
extern unsigned int g_1005db84;
extern unsigned int g_1005db88;
extern unsigned int g_1005dbbc;
extern unsigned int g_1005dbc0;
extern unsigned int g_1005dbc4;
extern unsigned int g_1005dbc8;
extern unsigned int g_1005dbd4;
extern unsigned int g_1005e1a0;
extern unsigned int g_1005e6a0;
extern char g_1005f538;
extern unsigned int g_1005f539;
extern unsigned int g_1005f549;
extern unsigned int g_1005f54d;
extern unsigned int g_1005f551;
extern unsigned int g_1005f55d;
extern unsigned int g_1005f561;
extern unsigned int g_1005f565;
extern unsigned int g_1005f569;
extern unsigned int g_1005f633;
extern unsigned int g_1005f637;
extern unsigned int g_1005f63b;
extern unsigned int g_1005f63f;
extern unsigned int g_1005f643;
extern char g_1005f88e;
extern char g_10077174;
extern struct_9 g_10077175;
extern struct_9 g_10080b05;
extern unsigned int g_10080b45;
extern unsigned int g_10080b49;
extern char g_10080b6e;
extern unsigned int g_10080bb7;
extern unsigned int g_10080bbb;
extern unsigned int g_10080bbf;
extern unsigned int g_10080bc3;
extern unsigned int g_10080bcf;
extern unsigned int g_10080bd3;
extern unsigned int g_10080bd7;
extern unsigned int g_10084bff;
extern unsigned int g_10084c03;
extern unsigned int g_1008b897;
extern unsigned int g_1008b8dc;
extern unsigned int g_1008b8e0;
extern unsigned int g_1008b8e4;
extern unsigned int g_1008b8e8;
extern unsigned int g_1008b8ec;
extern unsigned int g_1008b8f0;
extern unsigned int g_1008b941;
extern unsigned int g_1008b945[4];
extern unsigned int g_1009a52e;
extern unsigned int g_1009a532;
extern char g_100f0d35;
extern char g_100f0d37;
extern char g_100f0d3c;
extern unsigned int g_100f0d40;
extern char g_100f0e40;
extern char g_100f0e41;
extern unsigned int g_100f49fd;
extern unsigned int g_100f4a01;
extern char g_100f9316;
extern char g_100f9317;
extern unsigned short g_100f9324;
extern char g_100f9330;
extern char g_100f9335;
extern char g_100f933a;
extern char g_100f933b;
extern char g_100f933c;
extern unsigned int g_100f9355;
extern char g_100f94c8;
extern unsigned int g_100f94cb;
extern char g_1013526d;
extern unsigned int g_1013f320;
extern char g_1014f40b;
extern char g_1014f41f;
extern char g_10207f21;
extern char g_10207f23;
extern unsigned int g_10287f40;
extern char g_102898c8;
extern unsigned int g_102e2614;
extern unsigned int g_102e2a0c;
extern char g_799cfd;

void sub_100227bd(int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4)
{
    char *count;  // ebx
    unsigned int i;  // ecx
    unsigned int count1;  // eax
    unsigned int v103;  // ebx
    unsigned int v104;  // ebp
    unsigned int v105;  // esi
    unsigned int v106;  // edi
    unsigned int idx;  // ecx
    struct_0 *v108;  // edx
    int v109;  // eax
    unsigned int v13;  // edi
    unsigned int v14;  // ecx
    unsigned int v15;  // edx
    unsigned int count2;  // eax
    unsigned int v17;  // ebx
    unsigned int v18;  // ebp
    unsigned int v19;  // esi
    unsigned int v20;  // edi
    unsigned int v21;  // ebp
    unsigned long v6;  // ldt
    unsigned int v22;  // esi
    unsigned int v23;  // edi
    unsigned int v24;  // ebx
    unsigned int v25;  // eax
    unsigned int v26;  // ebx
    unsigned int v27;  // ebp
    unsigned int v28;  // esi
    unsigned int v29;  // edi
    unsigned int v30;  // ebx
    unsigned int v31;  // ebp
    unsigned long v7;  // gdt
    unsigned int v32;  // esi
    unsigned int v33;  // edi
    unsigned int v34;  // eax
    unsigned int v35;  // ebx
    unsigned int v36;  // ebp
    unsigned int v37;  // esi
    unsigned int v38;  // edi
    unsigned int v39;  // ebp
    unsigned int node;  // esi
    unsigned int v41;  // edi
    unsigned short v8;  // fs
    unsigned int v42;  // eax
    unsigned int v43;  // ebx
    unsigned int j;  // ecx
    unsigned int v45;  // eax
    unsigned int v46;  // ebx
    unsigned int v47;  // ebp
    unsigned int v48;  // esi
    unsigned int v49;  // edi
    unsigned int v50;  // eax
    unsigned int v51;  // eax
    unsigned long v9;  // 4123
    unsigned int v52;  // ebx
    unsigned int v53;  // ebp
    unsigned int v54;  // esi
    unsigned int v55;  // edi
    unsigned int v56;  // ecx
    struct_9 *iter;  // esi
    unsigned int v58;  // ecx
    struct_9 *iter1;  // esi
    unsigned int iter2;  // ecx
    unsigned int v61;  // ebx
    unsigned long v10;  // 4131
    unsigned int v62;  // eax
    unsigned int v63;  // ebx
    unsigned int v64;  // ebp
    unsigned int v65;  // esi
    unsigned int v66;  // edi
    unsigned int v67;  // eax
    unsigned int v68;  // eax
    unsigned int v69;  // ebx
    unsigned int v70;  // ebp
    unsigned int v71;  // esi
    unsigned int v11;  // eax
    unsigned int v72;  // edi
    unsigned int v73;  // ebx
    unsigned int v74;  // ebp
    unsigned int v75;  // esi
    unsigned int v76;  // edi
    unsigned int v77;  // eax
    unsigned int v78;  // ebx
    unsigned int v79;  // ebp
    unsigned int v80;  // esi
    unsigned int v81;  // edi
    unsigned int v82;  // eax
    unsigned int v83;  // eax
    unsigned int v84;  // ebx
    unsigned int v85;  // ebp
    unsigned int v86;  // esi
    unsigned int v87;  // edi
    unsigned int v88;  // ebx
    unsigned int v89;  // ebp
    unsigned int v90;  // eax
    unsigned int v91;  // ebx
    struct_0 **v12;  // esi
    unsigned int v92;  // ebp
    unsigned int v93;  // esi
    unsigned int v94;  // edi
    unsigned int v95;  // eax
    unsigned int v96;  // ebx
    unsigned int v97;  // ebp
    unsigned int v98;  // esi
    unsigned int v99;  // edi
    unsigned int v100;  // eax
    unsigned int v101;  // eax
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]
    char v2;  // [bp-0x4]
    unsigned int v3;  // [bp+0x0]

    count = &v2;
    for (i = 0; i < 512000; i += 4)
    {
        v0 = 0;
    }
    g_10058164 = &v2;
    g_10058168 = &v2;
    g_10058160 = &g_100227eb;
    v1 = sub_100026a6;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v0 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v0;
    g_1005816c = &v0;
    g_10058170 = &v2;
    v11 = GetTickCount() - 10;
    g_10058178 = v11;
    while (true)
    {
        g_1005dbc8 = &v2;
        g_1005dbc4 = g_1005816c;
        g_1005dbbc = 0;
        g_1005dbc0 = 0;
        *((unsigned int *)&g_1005816c[4]) = v11;
        *((unsigned int *)&g_1005816c[8]) = v14;
        *((unsigned int *)&g_1005816c[12]) = v15;
        *((char **)&g_1005816c[16]) = count;
        *((void* *)&g_1005816c[20]) = g_1005816c;
        *((char **)&g_1005816c[24]) = &v2;
        *((struct_0 ***)&g_1005816c[28]) = v12;
        *((unsigned int *)&g_1005816c[32]) = v13;
        /* unsupported instruction */ = g_1005816c - 36;
        g_1005dbd4 = GetTickCount();
        count2 = *((int *)(/* unsupported instruction */ + 28));
        v17 = *((int *)(/* unsupported instruction */ + 16));
        v18 = *((int *)(/* unsupported instruction */ + 8));
        v19 = *((int *)(/* unsupported instruction */ + 4));
        v20 = *((int *)/* unsupported instruction */);
        /* unsupported instruction */ = /* unsupported instruction */ + 32;
        if (g_102e2614)
        {
            g_102e2614 = 0;
            *((unsigned int *)(/* unsupported instruction */ - 4)) = 1;
            /* unsupported instruction */ = /* unsupported instruction */ - 8;
            count2 = (unsigned int)ExitThread(v3);
        }
        g_1005db84 = v18;
        *((int *)&g_1005db80) = /* unsupported instruction */;
        g_1005db78 = 4294967295;
        g_1005db7c = &g_100228af;
        *((unsigned int *)(/* unsupported instruction */ - 4)) = count2;
        *((unsigned int *)(/* unsupported instruction */ - 8)) = v14;
        *((unsigned int *)(/* unsupported instruction */ - 12)) = v15;
        *((unsigned int *)(/* unsupported instruction */ - 16)) = v17;
        *((int *)(/* unsupported instruction */ - 20)) = /* unsupported instruction */;
        *((unsigned int *)(/* unsupported instruction */ - 24)) = g_1005db84;
        *((unsigned int *)(/* unsupported instruction */ - 28)) = v19;
        *((unsigned int *)(/* unsupported instruction */ - 32)) = v20;
        /* unsupported instruction */ = /* unsupported instruction */ - 36;
        g_1005db88 = GetTickCount();
        v21 = *((int *)(/* unsupported instruction */ + 8));
        v22 = *((int *)(/* unsupported instruction */ + 4));
        v23 = *((int *)/* unsupported instruction */);
        /* unsupported instruction */ = /* unsupported instruction */ + 32;
        if (g_102e2614)
        {
            g_102e2614 = 0;
            *((unsigned int *)(/* unsupported instruction */ - 4)) = 1;
            /* unsupported instruction */ = /* unsupported instruction */ - 8;
            ExitThread(v3);
        }
        g_1005db78 = 4294967286;
        /* unsupported instruction */ = /* unsupported instruction */ - 4;
        g_100580e4 = GetTickCount();
        g_10058174 = 1;
        *((unsigned int *)(/* unsupported instruction */ - 4)) = 10;
        Sleep(v3);
        /* unsupported instruction */ = /* unsupported instruction */ - 12;
        v24 = GetTickCount();
        v25 = v24 - g_10084c03;
        g_10084c03 = v24;
        g_10084bff = v25;
        g_1005db78 = 4294967282;
        g_1005db84 = v21;
        *((int *)&g_1005db80) = /* unsupported instruction */;
        g_1005db78 = 10;
        g_1005db7c = &g_10022955;
        *((unsigned int *)(/* unsupported instruction */ - 4)) = g_10084bff;
        *((unsigned int *)(/* unsupported instruction */ - 8)) = v14;
        *((unsigned int *)(/* unsupported instruction */ - 12)) = v15;
        *((unsigned int *)(/* unsupported instruction */ - 16)) = g_10084c03;
        *((int *)(/* unsupported instruction */ - 20)) = /* unsupported instruction */;
        *((unsigned int *)(/* unsupported instruction */ - 24)) = v21;
        *((unsigned int *)(/* unsupported instruction */ - 28)) = v22;
        *((unsigned int *)(/* unsupported instruction */ - 32)) = v23;
        /* unsupported instruction */ = /* unsupported instruction */ - 36;
        g_1005db88 = GetTickCount();
        v26 = *((int *)(/* unsupported instruction */ + 16));
        v27 = *((int *)(/* unsupported instruction */ + 8));
        v28 = *((int *)(/* unsupported instruction */ + 4));
        v29 = *((int *)/* unsupported instruction */);
        /* unsupported instruction */ = /* unsupported instruction */ + 32;
        if (g_102e2614)
        {
            g_102e2614 = 0;
            *((unsigned int *)(/* unsupported instruction */ - 4)) = 1;
            /* unsupported instruction */ = /* unsupported instruction */ - 8;
            ExitThread(v3);
        }
        g_1005db74 = 1;
        /* unsupported instruction */ = /* unsupported instruction */ - 4;
        g_1005817c = sub_10021f3a();
        g_1005db84 = v27;
        *((int *)&g_1005db80) = /* unsupported instruction */;
        g_1005db78 = 30;
        g_1005db7c = &g_100229a0;
        *((unsigned int *)(/* unsupported instruction */ - 4)) = g_1005817c;
        *((unsigned int *)(/* unsupported instruction */ - 8)) = v14;
        *((unsigned int *)(/* unsupported instruction */ - 12)) = v15;
        *((unsigned int *)(/* unsupported instruction */ - 16)) = v26;
        *((int *)(/* unsupported instruction */ - 20)) = /* unsupported instruction */;
        *((unsigned int *)(/* unsupported instruction */ - 24)) = v27;
        *((unsigned int *)(/* unsupported instruction */ - 28)) = v28;
        *((unsigned int *)(/* unsupported instruction */ - 32)) = v29;
        /* unsupported instruction */ = /* unsupported instruction */ - 36;
        g_1005db88 = GetTickCount();
        v30 = *((int *)(/* unsupported instruction */ + 16));
        v31 = *((int *)(/* unsupported instruction */ + 8));
        v32 = *((int *)(/* unsupported instruction */ + 4));
        v33 = *((int *)/* unsupported instruction */);
        /* unsupported instruction */ = /* unsupported instruction */ + 32;
        if (g_102e2614)
        {
            g_102e2614 = 0;
            *((unsigned int *)(/* unsupported instruction */ - 4)) = 1;
            /* unsupported instruction */ = /* unsupported instruction */ - 8;
            ExitThread(v3);
        }
        /* unsupported instruction */ = /* unsupported instruction */ - 4;
        v34 = sub_10024fae();
        g_1005db84 = v31;
        *((int *)&g_1005db80) = /* unsupported instruction */;
        g_1005db78 = 50;
        g_1005db7c = &g_10022a0d;
        *((unsigned int *)(/* unsupported instruction */ - 4)) = v34;
        *((unsigned int *)(/* unsupported instruction */ - 8)) = v14;
        *((unsigned int *)(/* unsupported instruction */ - 12)) = v15;
        *((unsigned int *)(/* unsupported instruction */ - 16)) = v30;
        *((int *)(/* unsupported instruction */ - 20)) = /* unsupported instruction */;
        *((unsigned int *)(/* unsupported instruction */ - 24)) = v31;
        *((unsigned int *)(/* unsupported instruction */ - 28)) = v32;
        *((unsigned int *)(/* unsupported instruction */ - 32)) = v33;
        /* unsupported instruction */ = /* unsupported instruction */ - 36;
        g_1005db88 = GetTickCount();
        v35 = *((int *)(/* unsupported instruction */ + 16));
        v36 = *((int *)(/* unsupported instruction */ + 8));
        v37 = *((int *)(/* unsupported instruction */ + 4));
        v38 = *((int *)/* unsupported instruction */);
        /* unsupported instruction */ = /* unsupported instruction */ + 32;
        if (g_102e2614)
        {
            g_102e2614 = 0;
            *((unsigned int *)(/* unsupported instruction */ - 4)) = 1;
            /* unsupported instruction */ = /* unsupported instruction */ - 8;
            ExitThread(v3);
        }
        if (g_10043956 != 0xff)
            g_10043956 = *((int *)0x79c31c);
        *((unsigned int *)*((int *)0x4eafa5)) = g_10043956;
        g_1005db84 = v36;
        *((int *)&g_1005db80) = /* unsupported instruction */;
        g_1005db78 = 60;
        g_1005db7c = &g_10022e6f;
        *((int *)(/* unsupported instruction */ - 4)) = *((int *)0x4eafa5);
        *((unsigned int *)(/* unsupported instruction */ - 8)) = g_10043956;
        *((unsigned int *)(/* unsupported instruction */ - 12)) = v15;
        *((unsigned int *)(/* unsupported instruction */ - 16)) = v35;
        *((int *)(/* unsupported instruction */ - 20)) = /* unsupported instruction */;
        *((unsigned int *)(/* unsupported instruction */ - 24)) = v36;
        *((unsigned int *)(/* unsupported instruction */ - 28)) = v37;
        *((unsigned int *)(/* unsupported instruction */ - 32)) = v38;
        /* unsupported instruction */ = /* unsupported instruction */ - 36;
        g_1005db88 = GetTickCount();
        v39 = *((int *)(/* unsupported instruction */ + 8));
        node = *((int *)(/* unsupported instruction */ + 4));
        v41 = *((int *)/* unsupported instruction */);
        /* unsupported instruction */ = /* unsupported instruction */ + 32;
        if (g_102e2614)
        {
            g_102e2614 = 0;
            *((unsigned int *)(/* unsupported instruction */ - 4)) = 1;
            /* unsupported instruction */ = /* unsupported instruction */ - 8;
            ExitThread(v3);
        }
        /* unsupported instruction */ = /* unsupported instruction */ - 4;
        v42 = GetTickCount();
        v43 = g_1005f633;
        if (v42 - v43 > 1000)
        {
            v43 = v42;
            g_1005f633 = v42;
        }
        for (j = v42 - v43; j >= 100; j = v42 - (*((int *)/* unsupported instruction */) + 100))
        {
            /* unsupported instruction */ = /* unsupported instruction */ - 4;
            *((unsigned int *)(/* unsupported instruction */ - 4)) = v43;
            *((unsigned int *)(/* unsupported instruction */ - 4)) = v42;
            /* unsupported instruction */ = /* unsupported instruction */ - 8;
            v45 = sub_1002997f(v3, a0);
            g_1005db84 = v39;
            *((int *)&g_1005db80) = /* unsupported instruction */;
            g_1005db78 = 61;
            g_1005db7c = &g_10022ace;
            *((unsigned int *)(/* unsupported instruction */ - 4)) = v45;
            *((unsigned int *)(/* unsupported instruction */ - 8)) = v14;
            *((unsigned int *)(/* unsupported instruction */ - 12)) = v15;
            *((unsigned int *)(/* unsupported instruction */ - 16)) = v43;
            *((int *)(/* unsupported instruction */ - 20)) = /* unsupported instruction */;
            *((unsigned int *)(/* unsupported instruction */ - 24)) = v39;
            *((unsigned int *)(/* unsupported instruction */ - 28)) = node;
            *((unsigned int *)(/* unsupported instruction */ - 32)) = v41;
            /* unsupported instruction */ = /* unsupported instruction */ - 36;
            g_1005db88 = GetTickCount();
            v46 = *((int *)(/* unsupported instruction */ + 16));
            v47 = *((int *)(/* unsupported instruction */ + 8));
            v48 = *((int *)(/* unsupported instruction */ + 4));
            v49 = *((int *)/* unsupported instruction */);
            /* unsupported instruction */ = /* unsupported instruction */ + 32;
            if (g_102e2614)
            {
                g_102e2614 = 0;
                *((unsigned int *)(/* unsupported instruction */ - 4)) = 1;
                /* unsupported instruction */ = /* unsupported instruction */ - 8;
                ExitThread(v3);
            }
            /* unsupported instruction */ = /* unsupported instruction */ - 4;
            v50 = sub_1002994d();
            g_1005db84 = v47;
            *((int *)&g_1005db80) = /* unsupported instruction */;
            g_1005db78 = 60;
            g_1005db7c = &g_10022e6f;
            *((unsigned int *)(/* unsupported instruction */ - 4)) = v50;
            *((unsigned int *)(/* unsupported instruction */ - 8)) = v14;
            *((unsigned int *)(/* unsupported instruction */ - 12)) = v15;
            *((unsigned int *)(/* unsupported instruction */ - 16)) = v46;
            *((int *)(/* unsupported instruction */ - 20)) = /* unsupported instruction */;
            *((unsigned int *)(/* unsupported instruction */ - 24)) = v47;
            *((unsigned int *)(/* unsupported instruction */ - 28)) = v48;
            *((unsigned int *)(/* unsupported instruction */ - 32)) = v49;
            /* unsupported instruction */ = /* unsupported instruction */ - 36;
            g_1005db88 = GetTickCount();
            v51 = *((int *)(/* unsupported instruction */ + 28));
            v52 = *((int *)(/* unsupported instruction */ + 16));
            v53 = *((int *)(/* unsupported instruction */ + 8));
            v54 = *((int *)(/* unsupported instruction */ + 4));
            v55 = *((int *)/* unsupported instruction */);
            /* unsupported instruction */ = /* unsupported instruction */ + 32;
            if (g_102e2614)
            {
                g_102e2614 = 0;
                *((unsigned int *)(/* unsupported instruction */ - 4)) = 1;
                /* unsupported instruction */ = /* unsupported instruction */ - 8;
                v51 = (unsigned int)ExitThread(v3);
            }
            if (g_100f933c)
            {
                g_100f933c = g_100f933c - 1;
                if (!g_100f933c && *((int *)&g_102898c8) && g_100f0d37)
                {
                    /* unsupported instruction */ = /* unsupported instruction */ - 4;
                    v51 = sub_10026340();
                }
            }
            if (g_100f933b)
                g_100f933b = g_100f933b - 1;
            if (g_1005f551)
                g_1005f551 = g_1005f551 - 1;
            if (g_100f933a)
                g_100f933a = g_100f933a - 1;
            if (g_100f9335)
                g_100f9335 = g_100f9335 - 1;
            if (g_100f9330)
                g_100f9330 = g_100f9330 - 1;
            if (g_10287f40)
                g_10287f40 = g_10287f40 - 1;
            if (g_100f49fd)
            {
                v51 = 6606060;
                if (*((int *)0x64ccec) == 3549)
                    g_100f49fd = g_100f49fd - 100;
            }
            if (g_100f4a01)
                g_100f4a01 = g_100f4a01 - 100;
            if (g_102e2a0c)
                g_102e2a0c = g_102e2a0c - 1;
            if (g_1008b897)
                g_1008b897 = g_1008b897 - 1;
            if (g_1008b8dc)
                g_1008b8dc = g_1008b8dc - 1;
            if (g_1008b8e0)
                g_1008b8e0 = g_1008b8e0 - 1;
            if (g_1008b8e4)
                g_1008b8e4 = g_1008b8e4 - 1;
            if (g_1008b8e8)
                g_1008b8e8 = g_1008b8e8 - 1;
            if (g_1008b8ec)
                g_1008b8ec = g_1008b8ec - 1;
            if (g_1008b8f0)
                g_1008b8f0 = g_1008b8f0 - 1;
            if (g_1008b941)
                g_1008b941 = g_1008b941 + 1;
            if (g_1005f54d)
                g_1005f54d = g_1005f54d - 1;
            if (g_10080bb7)
                g_10080bb7 = g_10080bb7 - 1;
            if (g_10080bbb)
                g_10080bbb = g_10080bbb - 1;
            if (g_10080bcf)
                g_10080bcf = g_10080bcf - 1;
            if (g_1005f561)
                g_1005f561 = g_1005f561 - 1;
            if (g_1005f565)
                g_1005f565 = g_1005f565 - 1;
            if (g_1005f569)
                g_1005f569 = g_1005f569 - 1;
            g_1005db84 = v53;
            *((int *)&g_1005db80) = /* unsupported instruction */;
            g_1005db78 = 8;
            g_1005db7c = &g_10022e5d;
            *((unsigned int *)(/* unsupported instruction */ - 4)) = v51;
            *((unsigned int *)(/* unsupported instruction */ - 8)) = v14;
            *((unsigned int *)(/* unsupported instruction */ - 12)) = v15;
            *((unsigned int *)(/* unsupported instruction */ - 16)) = v52;
            *((int *)(/* unsupported instruction */ - 20)) = /* unsupported instruction */;
            *((unsigned int *)(/* unsupported instruction */ - 24)) = v53;
            *((unsigned int *)(/* unsupported instruction */ - 28)) = v54;
            *((unsigned int *)(/* unsupported instruction */ - 32)) = v55;
            /* unsupported instruction */ = /* unsupported instruction */ - 36;
            g_1005db88 = GetTickCount();
            v39 = *((int *)(/* unsupported instruction */ + 8));
            v41 = *((int *)/* unsupported instruction */);
            /* unsupported instruction */ = /* unsupported instruction */ + 32;
            if (g_102e2614)
            {
                g_102e2614 = 0;
                *((unsigned int *)(/* unsupported instruction */ - 4)) = 1;
                /* unsupported instruction */ = /* unsupported instruction */ - 8;
                ExitThread(v3);
            }
            if (g_100f0d35)
            {
                g_100f0d35 = g_100f0d35 - 1;
                if (!g_100f0d35 && g_100f0d40)
                {
                    *((unsigned int *)(/* unsupported instruction */ - 4)) = g_100f0d40;
                    /* unsupported instruction */ = /* unsupported instruction */ - 8;
                    CloseHandle(v3);
                    g_100f0d40 = 0;
                }
            }
            g_10080b49 = g_10080b49 + 1;
            if (g_10080b49 >= 3)
            {
                g_10080b49 = 0;
                v56 = g_10080b45 + 1;
                if (v56 >= 10)
                    v56 = 0;
                for (iter = &g_10077175.padding_0[0]; iter < &g_10080b05.padding_0[0]; iter = &iter[1].padding_0[12])
                {
                    *((unsigned short *)&iter->padding_5c[2 * v56]) = 0;
                    if (iter->field_5a < 5)
                    {
                        iter->field_5a = 0;
                        iter->field_58 = 0;
                    }
                    else if (iter->field_5a)
                    {
                        iter->field_5a = iter->field_5a - 1;
                        if (iter->field_58 && iter->field_40 && !iter->field_40->field_90)
                        {
                            if (iter->field_58 > 40)
                                iter->field_58 = iter->field_58 - 40;
                            else
                                iter->field_58 = 0;
                        }
                    }
                }
                g_10080b45 = v56;
            }
            v58 = g_10077174 + 1;
            if (v58 >= 20)
                v58 = 0;
            for (iter1 = &g_10077175.padding_0[0]; iter1 < &g_10080b05.padding_0[0]; iter1 = &iter1[1].padding_0[12])
            {
                iter1->padding_5c[20 + v58] = 0;
                if (iter1->field_8e)
                    iter1->field_8e = iter1->field_8e - 1;
                if (iter1->field_8f)
                    iter1->field_8f = iter1->field_8f - 1;
            }
            g_10077174 = v58;
            iter2 = 0;
            while (iter2 < 10)
            {
                if (g_1008b945[iter2])
                {
                    g_1008b945[iter2] = g_1008b945[iter2] - 1;
                    iter2 += 1;
                }
                else
                {
                    iter2 += 1;
                }
            }
            for (node = &g_1005e1a0; node < &g_1005e6a0; node += 16)
            {
                if (*((short *)(node + 6)))
                {
                    *((unsigned short *)(node + 6)) = *((short *)(node + 6)) - 1;
                    *((char *)(node + 4)) = *((char *)(node + 4)) + 1;
                }
            }
            /* unsupported instruction */ = /* unsupported instruction */ + 4;
            v42 = *((int *)/* unsupported instruction */);
            /* unsupported instruction */ = /* unsupported instruction */ + 4;
        }
        g_1005f633 = v43;
        /* unsupported instruction */ = /* unsupported instruction */ - 4;
        v61 = GetTickCount();
        v62 = v61 - g_1005f637;
        g_1005f63b = 0;
        if (v62 >= 100)
        {
            g_1005f637 = g_1005f637 + 100;
            if (v62 > 400)
                g_1005f637 = v61;
            g_1005db84 = v39;
            *((int *)&g_1005db80) = /* unsupported instruction */;
            g_1005db78 = 20;
            g_1005db7c = &g_10022ef4;
            *((unsigned int *)(/* unsupported instruction */ - 4)) = v62;
            *((unsigned int *)(/* unsupported instruction */ - 8)) = v14;
            *((unsigned int *)(/* unsupported instruction */ - 12)) = v15;
            *((unsigned int *)(/* unsupported instruction */ - 16)) = v61;
            *((int *)(/* unsupported instruction */ - 20)) = /* unsupported instruction */;
            *((unsigned int *)(/* unsupported instruction */ - 24)) = v39;
            *((unsigned int *)(/* unsupported instruction */ - 28)) = node;
            *((unsigned int *)(/* unsupported instruction */ - 32)) = v41;
            /* unsupported instruction */ = /* unsupported instruction */ - 36;
            g_1005db88 = GetTickCount();
            v63 = *((int *)(/* unsupported instruction */ + 16));
            v64 = *((int *)(/* unsupported instruction */ + 8));
            v65 = *((int *)(/* unsupported instruction */ + 4));
            v66 = *((int *)/* unsupported instruction */);
            /* unsupported instruction */ = /* unsupported instruction */ + 32;
            if (g_102e2614)
            {
                g_102e2614 = 0;
                *((unsigned int *)(/* unsupported instruction */ - 4)) = 1;
                /* unsupported instruction */ = /* unsupported instruction */ - 8;
                ExitThread(v3);
            }
            /* unsupported instruction */ = /* unsupported instruction */ - 4;
            v67 = sub_100205bf();
            g_1005db84 = v64;
            *((int *)&g_1005db80) = /* unsupported instruction */;
            g_1005db78 = 40;
            g_1005db7c = &g_10022f51;
            *((unsigned int *)(/* unsupported instruction */ - 4)) = v67;
            *((unsigned int *)(/* unsupported instruction */ - 8)) = v14;
            *((unsigned int *)(/* unsupported instruction */ - 12)) = v15;
            *((unsigned int *)(/* unsupported instruction */ - 16)) = v63;
            *((int *)(/* unsupported instruction */ - 20)) = /* unsupported instruction */;
            *((unsigned int *)(/* unsupported instruction */ - 24)) = v64;
            *((unsigned int *)(/* unsupported instruction */ - 28)) = v65;
            *((unsigned int *)(/* unsupported instruction */ - 32)) = v66;
            /* unsupported instruction */ = /* unsupported instruction */ - 36;
            g_1005db88 = GetTickCount();
            v68 = *((int *)(/* unsupported instruction */ + 28));
            v69 = *((int *)(/* unsupported instruction */ + 16));
            v70 = *((int *)(/* unsupported instruction */ + 8));
            v71 = *((int *)(/* unsupported instruction */ + 4));
            v72 = *((int *)/* unsupported instruction */);
            /* unsupported instruction */ = /* unsupported instruction */ + 32;
            if (g_102e2614)
            {
                g_102e2614 = 0;
                *((unsigned int *)(/* unsupported instruction */ - 4)) = 1;
                /* unsupported instruction */ = /* unsupported instruction */ - 8;
                v68 = (unsigned int)ExitThread(v3);
            }
            if (g_1013f320 || g_100f9355)
            {
                /* unsupported instruction */ = /* unsupported instruction */ - 4;
                v68 = sub_10023a45();
            }
            if (g_1009a52e)
                g_1009a52e = g_1009a52e - 1;
            if (g_1009a532)
                g_1009a532 = g_1009a532 - 1;
            if (g_1005f55d)
            {
                *((unsigned int *)(/* unsupported instruction */ - 4)) = 64;
                /* unsupported instruction */ = /* unsupported instruction */ - 8;
                v68 = MessageBeep(v3);
                g_1005f55d = g_1005f55d - 1;
            }
            g_1005db84 = v70;
            *((int *)&g_1005db80) = /* unsupported instruction */;
            g_1005db78 = 90;
            g_1005db7c = &g_10022fd0;
            *((unsigned int *)(/* unsupported instruction */ - 4)) = v68;
            *((unsigned int *)(/* unsupported instruction */ - 8)) = v14;
            *((unsigned int *)(/* unsupported instruction */ - 12)) = v15;
            *((unsigned int *)(/* unsupported instruction */ - 16)) = v69;
            *((int *)(/* unsupported instruction */ - 20)) = /* unsupported instruction */;
            *((unsigned int *)(/* unsupported instruction */ - 24)) = v70;
            *((unsigned int *)(/* unsupported instruction */ - 28)) = v71;
            *((unsigned int *)(/* unsupported instruction */ - 32)) = v72;
            /* unsupported instruction */ = /* unsupported instruction */ - 36;
            g_1005db88 = GetTickCount();
            v73 = *((int *)(/* unsupported instruction */ + 16));
            v74 = *((int *)(/* unsupported instruction */ + 8));
            v75 = *((int *)(/* unsupported instruction */ + 4));
            v76 = *((int *)/* unsupported instruction */);
            /* unsupported instruction */ = /* unsupported instruction */ + 32;
            if (g_102e2614)
            {
                g_102e2614 = 0;
                *((unsigned int *)(/* unsupported instruction */ - 4)) = 1;
                /* unsupported instruction */ = /* unsupported instruction */ - 8;
                ExitThread(v3);
            }
            /* unsupported instruction */ = /* unsupported instruction */ - 4;
            v77 = sub_10023e42();
            g_1005db84 = v74;
            *((int *)&g_1005db80) = /* unsupported instruction */;
            g_1005db78 = 190;
            g_1005db7c = &g_10023047;
            *((unsigned int *)(/* unsupported instruction */ - 4)) = v77;
            *((unsigned int *)(/* unsupported instruction */ - 8)) = v14;
            *((unsigned int *)(/* unsupported instruction */ - 12)) = v15;
            *((unsigned int *)(/* unsupported instruction */ - 16)) = v73;
            *((int *)(/* unsupported instruction */ - 20)) = /* unsupported instruction */;
            *((unsigned int *)(/* unsupported instruction */ - 24)) = v74;
            *((unsigned int *)(/* unsupported instruction */ - 28)) = v75;
            *((unsigned int *)(/* unsupported instruction */ - 32)) = v76;
            /* unsupported instruction */ = /* unsupported instruction */ - 36;
            g_1005db88 = GetTickCount();
            v62 = *((int *)(/* unsupported instruction */ + 28));
            v61 = *((int *)(/* unsupported instruction */ + 16));
            v39 = *((int *)(/* unsupported instruction */ + 8));
            node = *((int *)(/* unsupported instruction */ + 4));
            v41 = *((int *)/* unsupported instruction */);
            /* unsupported instruction */ = /* unsupported instruction */ + 32;
            if (g_102e2614)
            {
                g_102e2614 = 0;
                *((unsigned int *)(/* unsupported instruction */ - 4)) = 1;
                /* unsupported instruction */ = /* unsupported instruction */ - 8;
                v62 = (unsigned int)ExitThread(v3);
            }
            if (g_1005f539 && g_1005f549)
            {
                /* unsupported instruction */ = /* unsupported instruction */ - 4;
                v62 = sub_1003ffdf();
                if (!g_1005f54d)
                {
                    g_1005f54d = 10;
                    g_1005f538 = 1;
                }
            }
            g_1005f63b = 1;
        }
        g_1005db84 = v39;
        *((int *)&g_1005db80) = /* unsupported instruction */;
        g_1005db78 = 100;
        g_1005db7c = &g_1002309c;
        *((unsigned int *)(/* unsupported instruction */ - 4)) = v62;
        *((unsigned int *)(/* unsupported instruction */ - 8)) = v14;
        *((unsigned int *)(/* unsupported instruction */ - 12)) = v15;
        *((unsigned int *)(/* unsupported instruction */ - 16)) = v61;
        *((int *)(/* unsupported instruction */ - 20)) = /* unsupported instruction */;
        *((unsigned int *)(/* unsupported instruction */ - 24)) = v39;
        *((unsigned int *)(/* unsupported instruction */ - 28)) = node;
        *((unsigned int *)(/* unsupported instruction */ - 32)) = v41;
        /* unsupported instruction */ = /* unsupported instruction */ - 36;
        g_1005db88 = GetTickCount();
        v78 = *((int *)(/* unsupported instruction */ + 16));
        v79 = *((int *)(/* unsupported instruction */ + 8));
        v80 = *((int *)(/* unsupported instruction */ + 4));
        v81 = *((int *)/* unsupported instruction */);
        /* unsupported instruction */ = /* unsupported instruction */ + 32;
        if (g_102e2614)
        {
            g_102e2614 = 0;
            *((unsigned int *)(/* unsupported instruction */ - 4)) = 1;
            /* unsupported instruction */ = /* unsupported instruction */ - 8;
            ExitThread(v3);
        }
        /* unsupported instruction */ = /* unsupported instruction */ - 4;
        v82 = sub_1002bc68();
        g_1005db84 = v79;
        *((int *)&g_1005db80) = /* unsupported instruction */;
        g_1005db78 = 110;
        g_1005db7c = &g_10023119;
        *((unsigned int *)(/* unsupported instruction */ - 4)) = v82;
        *((unsigned int *)(/* unsupported instruction */ - 8)) = v14;
        *((unsigned int *)(/* unsupported instruction */ - 12)) = v15;
        *((unsigned int *)(/* unsupported instruction */ - 16)) = v78;
        *((int *)(/* unsupported instruction */ - 20)) = /* unsupported instruction */;
        *((unsigned int *)(/* unsupported instruction */ - 24)) = v79;
        *((unsigned int *)(/* unsupported instruction */ - 28)) = v80;
        *((unsigned int *)(/* unsupported instruction */ - 32)) = v81;
        /* unsupported instruction */ = /* unsupported instruction */ - 36;
        g_1005db88 = GetTickCount();
        v83 = *((int *)(/* unsupported instruction */ + 28));
        v84 = *((int *)(/* unsupported instruction */ + 16));
        v85 = *((int *)(/* unsupported instruction */ + 8));
        v86 = *((int *)(/* unsupported instruction */ + 4));
        v87 = *((int *)/* unsupported instruction */);
        /* unsupported instruction */ = /* unsupported instruction */ + 32;
        if (g_102e2614)
        {
            g_102e2614 = 0;
            *((unsigned int *)(/* unsupported instruction */ - 4)) = 1;
            /* unsupported instruction */ = /* unsupported instruction */ - 8;
            v83 = (unsigned int)ExitThread(v3);
        }
        g_1005dbc0 = 0;
        if (g_100f0e41)
            g_100f0e41 = g_100f0e41 - 1;
        if (g_100f0e40)
            g_100f0e40 = g_100f0e40 - 1;
        if (g_100f0d3c)
            g_100f0d3c = g_100f0d3c - 1;
        g_1005db84 = v85;
        *((int *)&g_1005db80) = /* unsupported instruction */;
        g_1005db78 = 120;
        g_1005db7c = &g_10023166;
        *((unsigned int *)(/* unsupported instruction */ - 4)) = v83;
        *((unsigned int *)(/* unsupported instruction */ - 8)) = v14;
        *((unsigned int *)(/* unsupported instruction */ - 12)) = v15;
        *((unsigned int *)(/* unsupported instruction */ - 16)) = v84;
        *((int *)(/* unsupported instruction */ - 20)) = /* unsupported instruction */;
        *((unsigned int *)(/* unsupported instruction */ - 24)) = v85;
        *((unsigned int *)(/* unsupported instruction */ - 28)) = v86;
        *((unsigned int *)(/* unsupported instruction */ - 32)) = v87;
        /* unsupported instruction */ = /* unsupported instruction */ - 36;
        g_1005db88 = GetTickCount();
        v88 = *((int *)(/* unsupported instruction */ + 16));
        v89 = *((int *)(/* unsupported instruction */ + 8));
        v12 = *((int *)(/* unsupported instruction */ + 4));
        v13 = *((int *)/* unsupported instruction */);
        /* unsupported instruction */ = /* unsupported instruction */ + 32;
        if (g_102e2614)
        {
            g_102e2614 = 0;
            *((unsigned int *)(/* unsupported instruction */ - 4)) = 1;
            /* unsupported instruction */ = /* unsupported instruction */ - 8;
            ExitThread(v3);
        }
        v90 = *((int *)0x64a9c0);
        if (*((int *)0x64a9c0) == 31)
        {
            g_1005f88e = 1;
            if (g_100f9317 > 2)
            {
                v90 = g_1005f63b;
                g_100f9317 = g_100f9317 - (char)g_1005f63b;
            }
            if (g_1005f63b)
            {
                g_1005db84 = v89;
                *((int *)&g_1005db80) = /* unsupported instruction */;
                g_1005db78 = 140;
                g_1005db7c = &g_100232dd;
                *((unsigned int *)(/* unsupported instruction */ - 4)) = v90;
                *((unsigned int *)(/* unsupported instruction */ - 8)) = v14;
                *((unsigned int *)(/* unsupported instruction */ - 12)) = v15;
                *((unsigned int *)(/* unsupported instruction */ - 16)) = v88;
                *((int *)(/* unsupported instruction */ - 20)) = /* unsupported instruction */;
                *((unsigned int *)(/* unsupported instruction */ - 24)) = v89;
                *((struct_0 ***)(/* unsupported instruction */ - 28)) = v12;
                *((unsigned int *)(/* unsupported instruction */ - 32)) = v13;
                /* unsupported instruction */ = /* unsupported instruction */ - 36;
                g_1005db88 = GetTickCount();
                v91 = *((int *)(/* unsupported instruction */ + 16));
                v92 = *((int *)(/* unsupported instruction */ + 8));
                v93 = *((int *)(/* unsupported instruction */ + 4));
                v94 = *((int *)/* unsupported instruction */);
                /* unsupported instruction */ = /* unsupported instruction */ + 32;
                if (g_102e2614)
                {
                    g_102e2614 = 0;
                    *((unsigned int *)(/* unsupported instruction */ - 4)) = 1;
                    /* unsupported instruction */ = /* unsupported instruction */ - 8;
                    ExitThread(v3);
                }
                /* unsupported instruction */ = /* unsupported instruction */ - 4;
                v95 = sub_1002492d();
                g_1005db84 = v92;
                *((int *)&g_1005db80) = /* unsupported instruction */;
                g_1005db78 = 150;
                g_1005db7c = &g_100233f0;
                *((unsigned int *)(/* unsupported instruction */ - 4)) = v95;
                *((unsigned int *)(/* unsupported instruction */ - 8)) = v14;
                *((unsigned int *)(/* unsupported instruction */ - 12)) = v15;
                *((unsigned int *)(/* unsupported instruction */ - 16)) = v91;
                *((int *)(/* unsupported instruction */ - 20)) = /* unsupported instruction */;
                *((unsigned int *)(/* unsupported instruction */ - 24)) = v92;
                *((unsigned int *)(/* unsupported instruction */ - 28)) = v93;
                *((unsigned int *)(/* unsupported instruction */ - 32)) = v94;
                /* unsupported instruction */ = /* unsupported instruction */ - 36;
                g_1005db88 = GetTickCount();
                v96 = *((int *)(/* unsupported instruction */ + 16));
                v97 = *((int *)(/* unsupported instruction */ + 8));
                v98 = *((int *)(/* unsupported instruction */ + 4));
                v99 = *((int *)/* unsupported instruction */);
                /* unsupported instruction */ = /* unsupported instruction */ + 32;
                if (g_102e2614)
                {
                    g_102e2614 = 0;
                    *((unsigned int *)(/* unsupported instruction */ - 4)) = 1;
                    /* unsupported instruction */ = /* unsupported instruction */ - 8;
                    ExitThread(v3);
                }
                *((unsigned int *)(/* unsupported instruction */ - 4)) = g_1014f40b;
                /* unsupported instruction */ = /* unsupported instruction */ - 8;
                v100 = sub_100235e8(v3);
                if (v100)
                {
                    if (g_10080bd7 && !((g_10080bd7 = g_10080bd7 - 1, !g_10080bd3 || !g_1014f41f || (*((unsigned int *)(/* unsupported instruction */ - 4)) = g_10080bd3, /* unsupported instruction */ = (int)(/* unsupported instruction */ - 8), v100 = sub_1003bc09(v3), !v100))))
                    {
                        if (g_10080bc3)
                            g_10080bc3 = g_10080bc3 - 1;
                        if (g_10080bd7 && !g_100f933b)
                        {
                            /* unsupported instruction */ = /* unsupported instruction */ - 4;
                            *((unsigned int *)(/* unsupported instruction */ - 4)) = g_100f94cb;
                            *((unsigned int *)(/* unsupported instruction */ - 4)) = g_10080bd3;
                            sub_1003a60a(v3, a0);
                            /* unsupported instruction */ = /* unsupported instruction */ - 12;
                            v100 = sub_10023797(v3, a0);
                        }
                    }
                    else
                    {
                        if (g_10080bc3)
                        {
                            g_10080bc3 = g_10080bc3 - 1;
                            if (g_10080bbf)
                            {
                                *((unsigned int *)(/* unsupported instruction */ - 4)) = g_10080bbf;
                                /* unsupported instruction */ = /* unsupported instruction */ - 8;
                                v100 = sub_1003bc09(v3);
                                if (v100 && g_10080bc3 && !g_100f933b)
                                {
                                    /* unsupported instruction */ = /* unsupported instruction */ - 4;
                                    *((unsigned int *)(/* unsupported instruction */ - 4)) = g_100f94cb;
                                    *((unsigned int *)(/* unsupported instruction */ - 4)) = g_10080bbf;
                                    sub_1003a60a(v3, a0);
                                    /* unsupported instruction */ = /* unsupported instruction */ - 12;
                                    v100 = sub_10023797(v3, a0);
                                }
                            }
                        }
                    }
                }
                g_1005db84 = v97;
                *((int *)&g_1005db80) = /* unsupported instruction */;
                g_1005db78 = 0xaa;
                g_1005db7c = &g_1002343b;
                *((unsigned int *)(/* unsupported instruction */ - 4)) = v100;
                *((unsigned int *)(/* unsupported instruction */ - 8)) = v14;
                *((unsigned int *)(/* unsupported instruction */ - 12)) = v15;
                *((unsigned int *)(/* unsupported instruction */ - 16)) = v96;
                *((int *)(/* unsupported instruction */ - 20)) = /* unsupported instruction */;
                *((unsigned int *)(/* unsupported instruction */ - 24)) = v97;
                *((unsigned int *)(/* unsupported instruction */ - 28)) = v98;
                *((unsigned int *)(/* unsupported instruction */ - 32)) = v99;
                /* unsupported instruction */ = /* unsupported instruction */ - 36;
                g_1005db88 = GetTickCount();
                v89 = *((int *)(/* unsupported instruction */ + 8));
                v12 = *((int *)(/* unsupported instruction */ + 4));
                v13 = *((int *)/* unsupported instruction */);
                /* unsupported instruction */ = /* unsupported instruction */ + 32;
                if (g_102e2614)
                {
                    g_102e2614 = 0;
                    *((unsigned int *)(/* unsupported instruction */ - 4)) = 1;
                    /* unsupported instruction */ = /* unsupported instruction */ - 8;
                    ExitThread(v3);
                }
                /* unsupported instruction */ = /* unsupported instruction */ - 4;
                sub_10023a8f();
            }
            /* unsupported instruction */ = /* unsupported instruction */ - 4;
            count = GetTickCount();
            v101 = &count[-1 * g_1005f63f];
            if (v101 > g_1005f643)
            {
                g_1005f63f = count;
                g_1005db84 = v89;
                *((int *)&g_1005db80) = /* unsupported instruction */;
                g_1005db78 = 160;
                g_1005db7c = &g_100234d9;
                *((unsigned int *)(/* unsupported instruction */ - 4)) = v101;
                *((unsigned int *)(/* unsupported instruction */ - 8)) = v14;
                *((unsigned int *)(/* unsupported instruction */ - 12)) = v15;
                *((char **)(/* unsupported instruction */ - 16)) = count;
                *((int *)(/* unsupported instruction */ - 20)) = /* unsupported instruction */;
                *((unsigned int *)(/* unsupported instruction */ - 24)) = v89;
                *((struct_0 ***)(/* unsupported instruction */ - 28)) = v12;
                *((unsigned int *)(/* unsupported instruction */ - 32)) = v13;
                /* unsupported instruction */ = /* unsupported instruction */ - 36;
                g_1005db88 = GetTickCount();
                count1 = *((int *)(/* unsupported instruction */ + 28));
                v103 = *((int *)(/* unsupported instruction */ + 16));
                v104 = *((int *)(/* unsupported instruction */ + 8));
                v105 = *((int *)(/* unsupported instruction */ + 4));
                v106 = *((int *)/* unsupported instruction */);
                /* unsupported instruction */ = /* unsupported instruction */ + 32;
                if (g_102e2614)
                {
                    g_102e2614 = 0;
                    *((unsigned int *)(/* unsupported instruction */ - 4)) = 1;
                    /* unsupported instruction */ = /* unsupported instruction */ - 8;
                    count1 = (unsigned int)ExitThread(v3);
                }
                if (!g_100f94c8)
                {
                    g_10080b6e = 0;
                    count1 = &g_799cfd;
                    g_799cfd = 1;
                }
                else if (g_10080b6e)
                {
                    g_10080b6e = g_10080b6e - 1;
                }
                else if (g_1013526d)
                {
                    /* unsupported instruction */ = /* unsupported instruction */ - 4;
                    count1 = sub_1003bb22();
                }
                g_1005db84 = v104;
                *((int *)&g_1005db80) = /* unsupported instruction */;
                g_1005db78 = 200;
                g_1005db7c = &g_10023524;
                *((unsigned int *)(/* unsupported instruction */ - 4)) = count1;
                *((unsigned int *)(/* unsupported instruction */ - 8)) = v14;
                *((unsigned int *)(/* unsupported instruction */ - 12)) = v15;
                *((unsigned int *)(/* unsupported instruction */ - 16)) = v103;
                *((int *)(/* unsupported instruction */ - 20)) = /* unsupported instruction */;
                *((unsigned int *)(/* unsupported instruction */ - 24)) = v104;
                *((unsigned int *)(/* unsupported instruction */ - 28)) = v105;
                *((unsigned int *)(/* unsupported instruction */ - 32)) = v106;
                /* unsupported instruction */ = /* unsupported instruction */ - 36;
                g_1005db88 = GetTickCount();
                count = *((int *)(/* unsupported instruction */ + 16));
                v12 = *((int *)(/* unsupported instruction */ + 4));
                v13 = *((int *)/* unsupported instruction */);
                /* unsupported instruction */ = /* unsupported instruction */ + 32;
                if (g_102e2614)
                {
                    g_102e2614 = 0;
                    *((unsigned int *)(/* unsupported instruction */ - 4)) = 1;
                    /* unsupported instruction */ = /* unsupported instruction */ - 8;
                    ExitThread(v3);
                }
                sub_10023893();
                *((unsigned int *)(/* unsupported instruction */ - 8)) = 100;
                g_1005f643 = sub_10040a30(v3) + 50;
            }
        }
        else
        {
            g_1005db84 = v89;
            *((int *)&g_1005db80) = /* unsupported instruction */;
            g_1005db78 = 130;
            g_1005db7c = &g_10023533;
            *((int *)(/* unsupported instruction */ - 4)) = *((int *)0x64a9c0);
            *((unsigned int *)(/* unsupported instruction */ - 8)) = v14;
            *((unsigned int *)(/* unsupported instruction */ - 12)) = v15;
            *((unsigned int *)(/* unsupported instruction */ - 16)) = v88;
            *((int *)(/* unsupported instruction */ - 20)) = /* unsupported instruction */;
            *((unsigned int *)(/* unsupported instruction */ - 24)) = v89;
            *((struct_0 ***)(/* unsupported instruction */ - 28)) = v12;
            *((unsigned int *)(/* unsupported instruction */ - 32)) = v13;
            /* unsupported instruction */ = /* unsupported instruction */ - 36;
            g_1005db88 = GetTickCount();
            count = *((int *)(/* unsupported instruction */ + 16));
            v12 = *((int *)(/* unsupported instruction */ + 4));
            v13 = *((int *)/* unsupported instruction */);
            /* unsupported instruction */ = /* unsupported instruction */ + 32;
            if (g_102e2614)
            {
                g_102e2614 = 0;
                *((unsigned int *)(/* unsupported instruction */ - 4)) = 1;
                /* unsupported instruction */ = /* unsupported instruction */ - 8;
                ExitThread(v3);
            }
            g_1005f88e = 0;
            for (idx = 0; idx < 10; idx += 1)
            {
                g_1008b945[idx] = 0;
            }
            g_1008b941 = 0;
            if (g_100f9317 > 2)
                g_100f9317 = 0;
            if (g_100f9317 && !g_100f9316)
            {
                if (g_10207f21)
                {
                    v12 = g_10052674;
                    if (g_10052674)
                    {
                        v108 = g_10052674->field_0;
                        /* unsupported instruction */ = /* unsupported instruction */ - 4;
                        *((unsigned int *)(/* unsupported instruction */ - 4)) = 0;
                        /* unsupported instruction */ = /* unsupported instruction */ - 4;
                        *((unsigned int *)(/* unsupported instruction */ - 4)) = 0;
                        /* unsupported instruction */ = /* unsupported instruction */ - 4;
                        *((unsigned int *)(/* unsupported instruction */ - 4)) = 0;
                        *((struct_6 **)(/* unsupported instruction */ - 4)) = g_10052674;
                        /* unsupported instruction */ = /* unsupported instruction */ - 8;
                        v108->field_30(v3, a0, a1, a2);
                    }
                    g_100580f8 = 1;
                }
                if (g_10207f23)
                {
                    if (!g_100f9324)
                    {
                        sub_10039bbb();
                        *((unsigned int *)(/* unsupported instruction */ - 8)) = 100;
                        g_100f9324 = (sub_10040a30(v3) & 0xffff) + 200;
                    }
                    else
                    {
                        g_100f9324 = g_100f9324 - (unsigned short)g_1005f63b;
                    }
                }
            }
        }
        v109 = sub_10021f3a();
        v11 = v109 - g_1005817c;
        g_100580f0 = v11;
    }
}
```

## `sub_10023548` `0x10023548`

_22 bytes. (leaf/helper — see body)_

```c
void sub_10023548(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8)
{
    unsigned long v1;  // ldt
    unsigned long v2;  // gdt
    unsigned short v3;  // fs
    unsigned long v4;  // 4113
    unsigned int v0;  // [bp+0x0]

    v4 = _ccall(v1, v2, (unsigned int)v3, 0);
    *((unsigned int *)v4) = v0;
    ExitThread(1);
    return;
}
```

## `sub_1002355e` `0x1002355e`

_138 bytes. (leaf/helper — see body)_

```c
extern int g_10080bb3;
extern unsigned int g_10080bb7;
extern int g_10080bcb;
extern unsigned int g_10080bcf;
extern char g_1013f27f;
extern char g_1014f41e;
extern char g_1014f41f;

int sub_1002355e(void)
{
    int v1;  // eax

    if (g_10080bcb && g_10080bcf && g_1014f41f && sub_1003bc09(g_10080bcb))
        return g_10080bcb;
    if (g_10080bb7 && g_10080bb3 && g_1014f41e && sub_1003bc09(g_10080bb3))
        return g_10080bb3;
    v1 = sub_1003bc54();
    if (v1)
    {
        return v1;
    }
    else if (g_1013f27f)
    {
        return sub_1003bc54();
    }
    else
    {
        return v1;
    }
}
```

## `sub_100235e8` `0x100235e8`

_431 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f9328;
extern int g_100f932c;
extern char g_100f9330;
extern int g_100f9331;
extern char g_100f9335;
extern int g_100f9336;
extern char g_100f933a;
extern char g_100f933b;
extern int g_100f94cb;
extern char g_1014f40c;

unsigned int sub_100235e8(unsigned int a0)
{
    unsigned int v0;  // eax
    unsigned int v2;  // eax
    unsigned int v4;  // eax

    if (g_100f933a)
    {
        v0 = sub_100237a4(g_100f9336);
        if (v0)
        {
            if (a0)
            {
                if (g_100f933a < 4)
                {
                    if (!g_100f933a || g_100f933b)
                        return 0;
                    if (g_100f9335)
                    {
                        if (*((int *)0x63fe78) >= 1200)
                        {
                            g_100f9328 = 1;
                            sub_1003a60a(g_100f9336, 42);
                            sub_10023797(g_100f9336, 42);
                        }
                    }
                    else
                    {
                        g_100f9328 = 1;
                        sub_1003a60a(g_100f9336, g_100f94cb);
                        sub_10023797(g_100f9336, g_100f94cb);
                    }
                    return 0;
                }
                else
                {
                    return 0;
                }
            }
            else
            {
                return 0;
            }
        }
        else
        {
            if (g_1014f40c)
                return _INSERT(v0, 0, 1);
            return 0;
        }
    }
    else if (g_100f9335)
    {
        v2 = sub_100237a4(g_100f9331);
        if (v2)
        {
            if (g_100f9335)
            {
                if (a0)
                {
                    if (g_100f9335 > 4)
                    {
                        if (!g_100f933b)
                        {
                            if (*((int *)0x63fe78) < 1200)
                                return 0;
                            g_100f9328 = 1;
                            sub_1003a60a(g_100f9331, 42);
                            sub_10023797(g_100f9331, 42);
                            return 0;
                        }
                        else
                        {
                            return 0;
                        }
                    }
                    else
                    {
                        return 0;
                    }
                }
                else
                {
                    return 0;
                }
            }
            else
            {
                return 0;
            }
        }
        else
        {
            if (g_1014f40c)
                return _INSERT(v2, 0, 1);
            return 0;
        }
    }
    else if (g_100f9330)
    {
        v4 = sub_100237a4(g_100f932c);
        if (v4)
        {
            if (!g_100f9330)
            {
                return 0;
            }
            else if (!a0)
            {
                return 0;
            }
            else if (!g_100f933b)
            {
                g_100f9328 = 1;
                sub_1003a60a(g_100f932c, g_100f94cb);
                sub_10023797(g_100f932c, g_100f94cb);
                return 0;
            }
            else
            {
                return 0;
            }
        }
        else
        {
            if (g_1014f40c)
                return _INSERT(v4, 0, 1);
            return 0;
        }
    }
    else
    {
        return _INSERT(0, 0, 1);
    }
}
```

## `sub_10023797` `0x10023797`

_13 bytes. (leaf/helper — see body)_

```c
extern char g_100f933b;
extern char g_101d5e2a;

char sub_10023797(void)
{
    char v1;  // al

    v1 = g_101d5e2a + 2;
    g_100f933b = g_101d5e2a + 2;
    return v1;
}
```

## `sub_100237a4` `0x100237a4`

_189 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[36];
    int field_24;
    int field_28;
    unsigned int field_2c;
    char padding_30[96];
    unsigned int field_90;
    unsigned int field_94;
    char padding_98[8];
    unsigned int field_a0;
} struct_0;

extern char g_1005f85c;
extern char g_100fa97a;
extern char g_1014f40d;
extern char g_1014f40e;
extern char g_1014f40f;

unsigned int sub_100237a4(struct_0 *a0)
{
    unsigned int v0;  // eax
    unsigned int v1;  // eax

    if (a0->field_2c != *((int *)&g_1005f85c))
    {
        return 0;
    }
    else if (!a0->field_90)
    {
        return 0;
    }
    else
    {
        v0 = sub_1003a494(&a0->padding_0[4]);
        if (!v0)
        {
            v0 = sub_1003a550(&a0->padding_0[4]);
            if (v0)
            {
                if (g_1014f40e && !a0->field_94 && a0->field_a0 != 2)
                    return 0;
            }
            else
            {
                if (g_1014f40f && !a0->field_94 && a0->field_a0 != 2)
                    return 0;
            }
        }
        else if (g_1014f40d && !a0->field_94 && a0->field_a0 != 2)
        {
            return 0;
        }
        v1 = _INSERT(v0, 0, 1);
        if (!g_100fa97a)
            return v1;
        sub_10011678(a0->field_24, a0->field_28, 0);
        return v1;
    }
}
```

## `sub_10023861` `0x10023861`

_26 bytes. (leaf/helper — see body)_

```c
int sub_10023861(void)
{
    return;
}
```

## `sub_1002387b` `0x1002387b`

_24 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1008b7c7;
extern unsigned int g_1008b7cb;

unsigned int sub_1002387b(void)
{
    unsigned int v0;  // [bp-0x4]

    g_1008b7cb = GetTickCount();
    v0 = *((int *)0x63fe8c);
    g_1008b7c7 = v0;
    return 0x63fe8c;
}
```

## `sub_10023893` `0x10023893`

_434 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    char padding_4[44];
    struct struct_0 *field_30;
    char padding_34[4];
    unsigned int field_38;
    struct struct_0 *field_3c;
} struct_0;

extern char g_100434d7;
extern char g_100434d9;
extern unsigned short g_100434da;
extern char g_100434dc;
extern char g_100434dd;
extern unsigned int g_100f0df8;
extern char g_100f45bc;
extern unsigned int g_100f45bd;
extern unsigned int g_100f45c1;
extern unsigned int g_100f9318;
extern char g_100f9326;
extern char g_1014f418;
extern char g_10207f35;

unsigned int sub_10023893(void)
{
    unsigned int v3;  // eax
    unsigned int v4;  // eax
    unsigned int v12;  // eax
    struct_0 *v13;  // ebx
    struct_0 *v14;  // ecx
    struct_0 *v15;  // esi
    unsigned int v16;  // eax
    unsigned int v5;  // eax
    unsigned int v7;  // eax
    struct_0 *v8;  // ebx
    struct_0 *v9;  // ecx
    struct_0 *v10;  // esi
    struct_0 *v11;  // ebx
    unsigned int v0;  // [bp-0xc]
    unsigned int iter;  // [bp-0x8]

    if (g_100f45bc)
    {
        g_100f45bc = g_100f45bc - 1;
        return v3;
    }
    if ((g_100f9326 || g_1014f418) && g_100f9318 != 4294967295)
    {
        g_100f0df8 = 5;
        if (!g_100f9318)
        {
            g_100434d7 = 3;
            g_100434d9 = 0;
            g_100434dc = 0;
            if (!*((int *)0x64ccb0))
            {
                g_100f9318 = 4294967295;
                return *((int *)0x64ccb0);
            }
            g_100f45c1 = *((int *)0x64ccb0);
            g_100434da = *((int *)0x64ccb0);
            g_100434dd = 0;
            v4 = sub_1002ade7("\n", 12);
            g_100f45bc = 10;
            g_100f45bd = 0;
            return v4;
        }
        else
        {
            v5 = sub_10037100();
            if (!v5)
            {
                g_100f9318 = 4294967295;
                g_100f9326 = 0;
                return g_100f45c1;
            }
            g_100f45c1 = v5;
            g_100f45bd = sub_10038d20();
            g_100f45bc = 10;
            return g_100f45bd;
        }
    }
    if (!g_10207f35)
        return v3;
    iter = 0;
    while (iter < 16)
    {
        v8 = iter * 492 + 6606096;
        v7 = v8->field_38;
        if (!v8->field_0)
        {
            iter += 1;
        }
        else if (v7 == v8->field_30)
        {
            v9 = NULL;
            v10 = &v8->field_3c;
            v0 = 0;
            while (true)
            {
                v11 = v8;
                if (v9 < v11->field_30)
                {
                    v12 = sub_1003c4fa(v10->field_0, v11, v9, v10);
                    v13 = v10->field_0;
                    v14 = v11;
                    v15 = v9;
                    v7 = v12 & 16;
                    if (v7)
                    {
                        if (!v0)
                        {
                            g_100434dd = iter;
                            v7 = iter + 64;
                            g_100434d7 = v7;
                            g_100434d9 = *((char *)&v14);
                            g_100434dc = *((char *)&v14);
                            g_100434da = v15->field_0;
                            v0 += 1;
                        }
                        else
                        {
                            iter += 1;
                            break;
                        }
                    }
                    v10 = &v15->padding_4[8];
                    v9 = (char *)&v14->field_0 + 1;
                    v8 = v13;
                }
                else
                {
                    if (v0 == 1)
                    {
                        v16 = sub_1002ade7("\n", 12);
                        g_100f45bc = 6;
                        g_100f45bd = iter;
                        return v16;
                    }
                    iter += 1;
                    break;
                }
            }
        }
        else
        {
            iter += 1;
        }
    }
    return v7;
}
```

## `sub_10023a45` `0x10023a45`

_74 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    struct struct_1 *field_0;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern unsigned int g_1005e19c;
extern struct_0 *g_100f9355;

unsigned int * sub_10023a45(void)
{
    unsigned int *v1;  // eax
    struct_1 **v2;  // ecx
    struct_1 **v3;  // ecx
    unsigned int *v4;  // eax

    if (g_100f9355)
    {
        g_1005e19c = g_100f9355;
        return g_100f9355;
    }
    v1 = sub_100235e8(0);
    if (!v1)
    {
        v3 = v2;
        if (v2)
            v3 = *(v3);
        g_1005e19c = v3;
        return v1;
    }
    else
    {
        v4 = sub_1002355e();
        if (!v4)
        {
            g_1005e19c = 0;
            return v4;
        }
        g_1005e19c = *(v4);
        return v4;
    }
}
```

## `sub_10023a8f` `0x10023a8f`

_947 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[96];
    unsigned int field_60;
    char field_64;
    char padding_65[3];
    char field_68;
    char padding_69[3];
    char field_6c;
    char padding_6d[3];
    char field_70;
} struct_0;

extern char g_1005f7ed;
extern char g_1005f85c;
extern void g_10077175;
extern char g_100ee8c8;
extern unsigned int g_100f49c9;
extern unsigned int g_100f49cd;
extern char g_100f94c7;
extern char g_10135278;
extern unsigned int g_10207f12;
extern unsigned int g_10207f15;

unsigned int sub_10023a8f(void)
{
    void* iter;  // ebx
    struct_0 *iter1;  // ebx
    unsigned int v8;  // eax
    void* index;  // ebx
    void* idx;  // esi
    void* idx1;  // esi
    void* idx2;  // ebx
    void* v13;  // esi
    void* v14;  // esi
    void* iter2;  // esi
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    void* node;  // [bp-0x8]

    v2 = 0;
    v3 = 0;
    node = &g_10077175;
    for (iter = 0x63fef8; iter < 0x64a308; iter += 168)
    {
        if ((char)iter[144])
        {
            if ((short)iter[4] == 19783)
            {
                v2 += 1;
            }
            else if ((short)iter[4] == 19779)
            {
                v2 += 1;
            }
            else if ((int)iter[96] == 75)
            {
                v2 += 1;
            }
            *((char *)&node[81]) = 0;
            v4 = 0;
            index = iter + 4;
            if (sub_1003a320(iter + 4, iter))
            {
                v4 = 1;
                if (g_100f94c7)
                    *((char *)&node[81]) = 1;
                if (g_10135278 && (int)index[96] && ((int)index[100] != 106 || (int)index[104] != 106 || (int)index[108] != 106 || (int)index[112] != 106))
                {
                    idx = node;
                    *((char *)&idx[132]) = (char)index[100];
                    *((char *)&idx[133]) = (char)index[104];
                    *((char *)&idx[134]) = (char)index[108];
                    *((char *)&idx[135]) = (char)index[112];
                    *((char *)&idx[0x88]) = 1;
                    *((char *)&index[100]) = 106;
                    *((char *)&index[104]) = 106;
                    *((char *)&index[108]) = 106;
                    *((char *)&index[112]) = 106;
                    g_100ee8c8 = 1;
                }
            }
            iter = index + 4;
            v8 = sub_1003a3da(index + 4, index);
            if (v8)
            {
                if (g_100f94c7)
                    *((char *)&node[81]) = 3;
                if (g_10135278 && (int)iter[96] && ((int)iter[100] != 87 || (int)iter[104] != 87 || (int)iter[108] != 87 || (int)iter[112] != 87))
                {
                    idx1 = node;
                    *((char *)&idx1[132]) = (char)iter[100];
                    *((char *)&idx1[133]) = (char)iter[104];
                    *((char *)&idx1[134]) = (char)iter[108];
                    v8 = _INSERT(v8, 0, (char)iter[112]);
                    *((char *)&idx1[135]) = (char)iter[112];
                    *((char *)&idx1[0x88]) = 1;
                    *((char *)&iter[100]) = 87;
                    *((char *)&iter[104]) = 87;
                    *((char *)&iter[108]) = 87;
                    *((char *)&iter[112]) = 87;
                    g_100ee8c8 = 1;
                }
            }
            else if (!v4 && *((int *)iter) < 0x40000000 && iter != *((int *)&g_1005f7ed))
            {
                v8 = *((int *)&g_1005f85c);
                if (*((int *)&g_1005f85c) == (int)iter[44])
                    v3 += 1;
            }
            if (g_100f94c7 || g_10135278)
            {
                idx2 = iter + 4;
                if (sub_1003a494(iter + 4, iter))
                {
                    if (g_100f94c7)
                        *((char *)&node[81]) = 2;
                    if (g_10135278 && (int)idx2[96] && ((int)idx2[100] != 96 || (int)idx2[104] != 96 || (int)idx2[108] != 96 || (int)idx2[112] != 96))
                    {
                        v13 = node;
                        *((char *)&v13[132]) = (char)idx2[100];
                        *((char *)&v13[133]) = (char)idx2[104];
                        *((char *)&v13[134]) = (char)idx2[108];
                        *((char *)&v13[135]) = (char)idx2[112];
                        *((char *)&v13[0x88]) = 1;
                        *((char *)&idx2[100]) = 96;
                        *((char *)&idx2[104]) = 96;
                        *((char *)&idx2[108]) = 96;
                        *((char *)&idx2[112]) = 96;
                        g_100ee8c8 = 1;
                    }
                }
                iter = idx2 + 4;
                v8 = sub_1003a550(idx2 + 4, idx2);
                if (v8)
                {
                    if (g_100f94c7)
                        *((char *)&node[81]) = 4;
                    if (g_10135278 && (int)iter[96] && ((int)iter[100] != 77 || (int)iter[104] != 77 || (int)iter[108] != 77 || (int)iter[112] != 77))
                    {
                        v14 = node;
                        *((char *)&v14[132]) = (char)iter[100];
                        *((char *)&v14[133]) = (char)iter[104];
                        *((char *)&v14[134]) = (char)iter[108];
                        v8 = _INSERT(v8, 0, (char)iter[112]);
                        *((char *)&v14[135]) = (char)iter[112];
                        *((char *)&v14[0x88]) = 1;
                        *((char *)&iter[100]) = 77;
                        *((char *)&iter[104]) = 77;
                        *((char *)&iter[108]) = 77;
                        *((char *)&iter[112]) = 77;
                        g_100ee8c8 = 1;
                    }
                }
            }
        }
        node += 156;
    }
    if (v2)
    {
        v8 = g_10207f15 & 0xffffff;
        if (v8)
            v8 = sub_10009489(1);
    }
    v1 = v2;
    g_100f49c9 = v2;
    if (v3)
    {
        v8 = g_10207f12 & 0xffffff;
        if (v8)
            v8 = sub_10009489(0);
    }
    v0 = v3;
    g_100f49cd = v3;
    if (!g_100ee8c8)
    {
        return v8;
    }
    else if (!g_10135278)
    {
        iter2 = &g_10077175;
        for (iter1 = 0x63fef8; iter1 < 0x64a308; iter1 = &iter1[1].padding_0[55])
        {
            if ((char)iter2[0x88] && iter1->field_60)
            {
                iter1->field_64 = (int)iter2[132];
                iter1->field_68 = (int)iter2[133];
                iter1->field_6c = (int)iter2[134];
                v8 = (int)iter2[135];
                iter1->field_70 = v8;
                *((char *)&iter2[0x88]) = 0;
            }
            iter2 += 156;
        }
        g_100ee8c8 = 0;
        return v8;
    }
    else
    {
        return v8;
    }
}
```

## `sub_10023e42` `0x10023e42`

_96 bytes. (leaf/helper — see body)_

```c
extern int g_100439ec;
extern int g_100580f0;
extern unsigned int g_1008b8a8;
extern unsigned int g_1008b8ac[4];
extern unsigned int g_1008b8d4;
extern unsigned int g_1008b8d8;

int sub_10023e42(void)
{
    unsigned int idx;  // ecx
    unsigned int v2[4];  // eax

    g_1008b8d4 = g_1008b8d4 + 1;
    if (g_1008b8d4 == 10)
        g_1008b8d4 = 0;
    g_1008b8ac[g_1008b8d4] = g_1008b8a8;
    idx = 0;
    v2 = NULL;
    for (g_1008b8a8 = 0; idx < 10; idx += 1)
    {
        v2 = (char *)v2 + g_1008b8ac[idx];
    }
    g_1008b8d8 = v2;
    return sub_10040940(g_100580f0, &g_100439ec);
}
```

## `sub_10023ea2` `0x10023ea2`

_527 bytes. refs "   CiroScript.com   ", " - %s - ", " - Slot %d - "_

```c
extern int g_10042905;
extern int g_10043998;
extern int g_100439c1;
extern unsigned int g_100445f1;
extern char g_1005dc8c;
extern unsigned int g_1005e190;
extern HWND g_1005f626;
extern int g_1005f7b1;
extern unsigned int g_1008b71f;
extern unsigned int g_1008b727;
extern unsigned int g_1008b72f;
extern unsigned int g_1008b733;
extern unsigned int g_1008b737;
extern unsigned int g_1008b73b;
extern unsigned int g_1008b73f;
extern unsigned int g_1008b7c7;
extern unsigned int g_1008b7cb;
extern unsigned int g_1008b7ef;

int sub_10023ea2(void)
{
    unsigned int count;  // eax
    unsigned int v5;  // eax
    int len;  // eax
    char *node;  // ecx
    unsigned int iter;  // ecx
    unsigned int v9;  // eax
    unsigned int v10;  // esi
    char *v0;  // [bp-0x128], Other Possible Types: unsigned int
    Byte v1[256];  // [bp-0x124]
    char v2;  // [bp-0x24]

    if (!g_1008b7c7)
    {
        v0 = *((int *)0x63fe8c);
        g_1008b7c7 = *((int *)0x63fe8c);
        g_1008b7cb = GetTickCount();
    }
    count = GetTickCount();
    v5 = count - g_1008b7cb;
    if (v5)
    {
        g_1008b7ef = *((int *)0x63fe8c) - g_1008b7c7;
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
        g_1008b7ef = v5;
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
        g_1008b7ef = 3600000;
        /* unsupported instruction */
        /* unsupported instruction */
        g_1008b7ef = (/* unsupported instruction */ ? /* unsupported instruction */ : nan);
        /* unsupported instruction */
    }
    lstrcpy(v1, "   CiroScript.com   ");
    lstrcat(v1, &g_1005f7b1);
    len = lstrlen(v1);
    if (g_1005dc8c)
    {
        for (node = &g_1005dc8c; *(node); node += 1);
        for (; *(node) != 92 && node > &g_1005dc8c; node += 1);
        v0 = node + 1;
        wsprintfA(&v1[len], " - %s - ");
    }
    else
    {
        v0 = g_100445f1;
        wsprintfA(&v1[len], " - Slot %d - ");
    }
    if (g_1008b727)
    {
        v0 = g_1008b73b;
        g_1008b73f = g_1008b73b;
        v0 = g_1008b737;
        g_1008b73b = g_1008b737;
        v0 = g_1008b733;
        g_1008b737 = g_1008b733;
        v0 = g_1008b72f;
        g_1008b733 = g_1008b72f;
        v0 = g_1008b727;
        g_1008b72f = g_1008b727;
        g_1008b727 = 0;
    }
    iter = 0;
    v9 = 0;
    for (v10 = 0; iter < 20; iter += 4)
    {
        if (*((int *)(iter + (char *)&g_1008b72f)))
        {
            v9 += *((int *)(iter + (char *)&g_1008b72f));
            v10 += 1;
        }
    }
    if (v10)
        v9 /= v10;
    g_1008b71f = v9;
    sub_10040940(v9, &v2);
    lstrcpy(&g_10043998, &v2);
    lstrcat(v1, &v2);
    lstrcat(v1, &g_10042905);
    sub_10040940(g_1008b7ef, &v2);
    g_1005e190 = g_1008b7ef;
    lstrcpy(&g_100439c1, &v2);
    lstrcat(v1, &v2);
    lstrcat(v1, " exp/hour");
    return SetWindowTextA(g_1005f626, v1);
}
```

## `sub_100240b1` `0x100240b1`

_287 bytes. calls SendMessageA; refs "TibiaClient"_

```c
extern HWND g_1005f61e;
extern unsigned int g_1005f89f;
extern char g_100f0d38;
extern unsigned int g_100f0dac;
extern char g_100f94ca;
extern char g_1013f326;

int sub_100240b1(void)
{
    int v4;  // eax
    int v5;  // eax
    unsigned int i;  // [bp-0x8]

    if (g_1013f326 && *((int *)0x64a9c0) != 31)
        SendMessageA(SendMessageA(sub_10039b62(), 0x100, 0x22, NULL), 0x101, 0x22, NULL);
    if (!g_100f94ca && *((int *)0x64a9c0) == 31)
    {
        g_1005f89f = 0;
        if (!g_100f0d38)
            return sub_10039357(4562856, -1958457089);
        g_100f0d38 = 0;
        return sub_10039357(4562856, -1958457089);
    }
    g_1005f89f = 100;
    if (!g_1005f61e)
    {
        g_1005f61e = 0;
        do
        {
            g_1005f61e = FindWindowExA(NULL, g_1005f61e, "TibiaClient", NULL);
            GetWindowThreadProcessId(g_1005f61e, &i);
        } while (GetCurrentProcessId() != i);
    }
    if (IsIconic(g_1005f61e))
    {
        v5 = sub_10039357(4562856, -1962097533);
        g_100f0d38 = 1;
        return v5;
    }
    v4 = sub_10039357(4562856, -1958457089);
    g_100f0d38 = 0;
    if (g_100f0dac != 4294967295)
        return v4;
    return ShowWindow(g_1005f61e, SW_MINIMIZE);
}
```

## `sub_100241d0` `0x100241d0`

_57 bytes. refs "%lu", "%lu%.9lu"_

```c
int sub_100241d0(unsigned int a0, unsigned int a1)
{
    unsigned int v3;  // eax
    PSTR v4;  // edi
    unsigned short *v5;  // edi
    unsigned int v6;  // eax
    int v7;  // eax
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp-0x4]

    if (!a1)
    {
        v1 = v3;
        return wsprintfA(v4, "%lu");
    }
    *(v5) = 48;
    if (a1 >= 1000000000)
        return v7;
    v1 = (a1 CONCAT v6) % 1000000000;
    v0 = (a1 CONCAT v6) / 1000000000;
    return wsprintfA(v5, "%lu%.9lu");
}
```

## `sub_10024209` `0x10024209`

_45 bytes. (leaf/helper — see body)_

```c
int sub_10024209(char *a0)
{
    unsigned int v0;  // ecx
    char v1;  // al
    char iter[2];  // esi

    v0 = 0;
    v1 = *(a0);
    for (iter = a0 + 1; v1; iter = &iter[1])
    {
        v0 = _INSERT(v1 CONCAT 0, 0, v1 - 48) + v0 * 10;
        v1 = iter[0];
    }
    return v0 ^ 0;
}
```

## `sub_10024236` `0x10024236`

_159 bytes. (leaf/helper — see body)_

```c
int sub_10024236(void)
{
    void* v3;  // esi
    int len;  // eax
    int v5;  // esi
    unsigned long long v6;  // eax
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    len = lstrlen(v3);
    if (...)
    {
        v5 = len - 9;
        v1 = *((int *)(v5 + (char *)v3));
        *(v5 + (char *)v3) = 0;
        v6 = sub_10024209(v3);
        *((int *)(v5 + (char *)v3)) = *((int *)(v5 + (char *)v3));
        v1 = v6 * 1000000000 >> 32;
        v0 = v6 * 1000000000;
        return sub_10024209(v5 + v3) + (unsigned int)(v6 * 1000000000);
    }
    return sub_10024209(v3);
}
```

## `sub_1002424e` `0x1002424e`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002424e(void)
{
}
```

## `sub_100244e1` `0x100244e1`

_788 bytes. calls CreateThread, GetPrivateProfileStringA; refs "localhost", "7177", "7177"_

```c
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

extern void g_1003faa1;
extern CRITICAL_SECTION g_1004287d;
extern unsigned int g_100428b5;
extern char g_1004292d;
extern Byte g_100429fa;
extern int g_10042d7b;
extern unsigned int g_10052774;
extern char g_1005dc48;
extern unsigned int g_1005f62e;
extern unsigned int g_1005f884;
extern unsigned int g_100ba736;
extern unsigned int g_100ec0b6;
extern unsigned int g_100f0dac;
extern unsigned int g_100f49d1;
extern unsigned int g_100f49d5;
extern unsigned int g_100f49dd;
extern unsigned int g_100f49e1;
extern unsigned int g_100f49ed;
extern unsigned int g_100f49f1;
extern Byte g_100f4d09;
extern Byte g_100f78e9;
extern char g_100fa4f0;
extern unsigned int g_10134d61;
extern unsigned int g_10134d65;
extern int g_10134dc3;
extern int g_10134e03;
extern int g_10134e43;
extern int g_1013f280;
extern int g_1013f2a0;
extern int g_1013f2e0;
extern unsigned int g_1013f31c;
extern char g_102898cd;

HANDLE sub_100244e1(void)
{
    unsigned int i;  // ecx
    char *iter;  // esi
    LPArray v14;  // ebx
    int i2;  // ecx
    struct_1 *v6;  // eax
    char *iter1;  // esi
    struct_1 *v8;  // eax
    void* ch;  // eax
    void* l;  // eax
    int n;  // ebx
    int i0;  // ebx
    unsigned int iter2;  // ebx
    Byte v0[402];  // [bp-0x344]
    char v1;  // [bp-0x1b2], Other Possible Types: unsigned int
    WSADATA v2;  // [bp-0x192]

    for (i = 0; i < 30; i += 1);
    InitializeCriticalSection(&g_1004287d.DebugInfo);
    sub_1002a433(v0);
    sub_10002992();
    g_10134d61 = 808988724;
    g_10134d65 = 0x4646;
    g_1013f31c = 7175;
    g_100f49d5 = 4294967295;
    g_100fa4f0 = 1;
    lstrcpy(&g_10134e03, "localhost");
    lstrcpy(&g_10134dc3, "7177");
    lstrcpy(&g_10134e43, "7177");
    lstrcpy(&g_1013f280, "7180");
    lstrcpy(&g_1013f2a0, "localhost");
    lstrcpy(&g_1013f2e0, "7180");
    g_1005dc48 = 50;
    CreateThread(NULL, NULL, sub_10021f6c, NULL, THREAD_CREATE_RUN_IMMEDIATELY, &g_1005f62e);
    WSAStartup(0x202, &v2);
    for (iter = &g_1004292d; *(iter); iter += 1)
    {
        *(iter) = *(iter) - 80;
    }
    v6 = gethostbyname(&g_1004292d);
    for (iter1 = &g_1004292d; *(iter1); iter1 += 1)
    {
        *(iter1) = *(iter1) + 80;
    }
    v8 = v6;
    if (v6 && v8->field_c->field_0)
        g_100428b5 = v8->field_c->field_0->field_0 + 976325;
    ch = GetCommandLineA();
    if (ch && *((char *)ch) == 0x22)
    {
        for (l = ch + 1; *((char *)l) != 0x22; l += 1);
        for (ch = l + 1; *((char *)ch) == 32; ch += 1);
    }
    else
    {
        if (!ch)
            goto LABEL_10024684;
        for (; *((char *)ch) != 32; ch += 1);
        for (; *((char *)ch) == 32; ch += 1);
    }
    if (*((int *)ch) == 2020569712 && (short)ch[4] == 8313)
    {
        g_100f0dac = sub_10040900(ch + 6);
        g_102898cd = 1;
        CreateThread(NULL, NULL, sub_100209d5, NULL, THREAD_CREATE_RUN_IMMEDIATELY, &g_1005f884);
    }
LABEL_10024684:
    g_10052774 = HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, 0x8c6180);
    g_100f49d1 = HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, 0x40000);
    g_100f49dd = 2000;
    g_100f49e1 = 2000;
    g_100f49ed = HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, 0xa2030);
    g_100f49f1 = HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, 0x82380);
    sub_100092b0();
    sub_1002489c();
    sub_1002040d();
    sub_100247f7();
    for (n = 2118; n <= 2127; n += 1)
    {
        sub_1003c496(n, n);
    }
    for (i0 = 6754; i0 <= 6756; i0 += 1)
    {
        sub_1003c4c8(i0, i0);
    }
    for (iter2 = &g_100ba736; iter2 < &g_100ec0b6; iter2 += 276)
    {
        *((unsigned int *)(iter2 + 264)) = 228;
        *((unsigned int *)(iter2 + 268)) = 179;
        *((unsigned int *)(iter2 + 272)) = 27;
    }
    lstrcpy(&v0[2], &g_10042d7b);
    lstrcat(&v0[2], "outfits.txt");
    v14 = &g_100f4d09;
    for (i2 = 0; v14 <= &g_100f78e9; i2 += 1)
    {
        sub_10040940(i2, &v1, i2);
        GetPrivateProfileStringA("Outfits", &v1, &g_100429fa, v14, 32, &v0[2]);
        v14 += 32;
    }
    sub_10040a30(GetTickCount());
    return CreateThread(NULL, NULL, &g_1003faa1, NULL, THREAD_CREATE_RUN_IMMEDIATELY, &v1);
}
```

## `sub_10024632` `0x10024632`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10024632(void)
{
}
```

## `sub_100247f7` `0x100247f7`

_165 bytes. (leaf/helper — see body)_

```c
void sub_100247f7(void)
{
    int i;  // ebx

    sub_1003c496(2319);
    sub_1003c496(2981);
    sub_1003c496(2983);
    sub_1003c496(2984);
    sub_1003c496(2985);
    sub_1003c496(2431);
    sub_1003c496(2432);
    sub_1003c496(2433);
    sub_1003c496(2434);
    sub_1003c496(2472);
    sub_1003c496(3503);
    sub_1003c496(3504);
    sub_1003c496(2471);
    sub_1003c496(2473);
    for (i = 2354; i <= 2385; i += 1)
    {
        sub_1003c496(i, i);
    }
    return;
}
```

## `sub_1002489c` `0x1002489c`

_145 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1008caee;

void sub_1002489c(void)
{
    unsigned int *iter;  // ebx
    unsigned int i;  // ecx
    unsigned int j;  // ecx
    unsigned int node;  // ecx
    unsigned int l;  // ecx
    unsigned int m;  // ecx

    iter = &g_1008caee;
    for (i = 3577; i <= 3602; i += 1)
    {
        *(iter) = i;
        iter += 1;
    }
    for (j = 3606; j <= 3607; j += 1)
    {
        *(iter) = j;
        iter += 1;
    }
    node = 3620;
    while (node <= 3729)
    {
        if (node == 3661)
        {
            node += 1;
        }
        else if (node != 3658)
        {
            *(iter) = node;
            iter += 1;
            node += 1;
        }
        else
        {
            node += 1;
        }
    }
    for (l = 3900; l <= 3904; l += 1)
    {
        *(iter) = l;
        iter += 1;
    }
    for (m = 3910; m <= 3917; m += 1)
    {
        *(iter) = m;
        iter += 1;
    }
    *(iter) = 3731;
    iter[1] = 5678;
    return;
}
```

## `sub_1002492d` `0x1002492d`

_897 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[136];
    unsigned int field_88;
} struct_0;

extern int g_10043315;
extern int g_1004339b;
extern unsigned short g_100433a0;
extern char g_100433a2;
extern unsigned short g_100433a3;
extern char g_100433a5;
extern unsigned int g_100433a6;
extern unsigned int g_100445f8[4];
extern unsigned int g_10044610[4];
extern unsigned int g_1005f7e5;
extern struct_0 *g_1005f7ed;
extern unsigned int g_10080b94;
extern unsigned int g_10080b98;
extern unsigned int g_10080b9c;
extern char g_10080ba0;
extern char g_10080ba1;
extern unsigned int g_10080ba2;
extern char g_10080ba6;
extern unsigned int g_10080ba7;
extern unsigned int g_10080bab;
extern char g_100f9495;
extern unsigned int g_100f9499;
extern unsigned int g_100f949d;
extern unsigned int g_100f94c1;
extern char g_100fa4f1;
extern char g_100fa531;
extern unsigned int g_100fa571;
extern char g_100fa575;
extern char g_10134e63;
extern unsigned int g_10134e66;
extern unsigned int g_1014f410;
extern char g_1014f419;
extern unsigned int g_1014f41a;

unsigned int sub_1002492d(void)
{
    unsigned int v6;  // eax
    int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x14]

    g_10080ba6 = 0;
    if (g_10080ba2)
        g_10080ba2 = g_10080ba2 - 1;
    if (g_10080b98)
        g_10080b98 = g_10080b98 - 1;
    if (g_10080b9c)
        g_10080b9c = g_10080b9c - 1;
    if (g_10080ba0)
        g_10080ba0 = g_10080ba0 - 1;
    if (g_10080ba1)
        g_10080ba1 = g_10080ba1 - 1;
    if (!*((int *)0x63fe94))
        return *((int *)0x63fe94);
    v4 = *((int *)0x63fe94);
    v3 = *((int *)0x63fe90);
    v2 = *((int *)0x63fe78);
    if (*((int *)0x63fe94) != *((int *)0x63fe90) && g_10134e66 && *((int *)0x63fe94) < g_10134e66)
    {
        if (!g_10080ba1 && !g_10080b9c)
        {
            g_10080b94 = g_100445f8[g_10134e63];
            g_10080bab = g_10080bab + 1;
            g_100433a3 = g_10080b94;
            g_100433a6 = g_1005f7e5;
            if (g_1005f7ed && g_1005f7ed->field_88 < 100)
            {
                g_100433a0 = 0;
                g_100433a2 = 0;
                g_100433a5 = 0;
                v1 = 15;
                v0 = &g_1004339b;
                sub_1002ade7(&g_1004339b, 15);
                g_10080ba1 = g_1014f410 + 1;
            }
        }
        g_10080ba6 = 1;
    }
    else if (*((int *)0x63fe78) != *((int *)0x63fe74) && g_1014f41a && *((int *)0x63fe78) < g_1014f41a)
    {
        if (!g_10080ba1 && !g_10080b9c)
        {
            g_10080b94 = g_10044610[g_1014f419];
            g_10080bab = g_10080bab + 1;
            g_100433a3 = g_10080b94;
            g_100433a6 = g_1005f7e5;
            if (g_1005f7ed)
            {
                g_100433a0 = 0;
                g_100433a2 = 0;
                g_100433a5 = 0;
                v1 = 15;
                v0 = &g_1004339b;
                sub_1002ade7(&g_1004339b, 15);
                g_10080ba1 = g_1014f410 + 1;
            }
        }
        g_10080ba6 = 1;
    }
    else if (g_10080bab)
    {
        if (g_10080bab > 1 && !sub_1002ffa3())
        {
            v1 = 4;
            v0 = &g_10043315;
            sub_1002ade7(&g_10043315, 4);
        }
        g_10080bab = 0;
    }
    else
    {
        v1 = g_100f94c1;
        g_10080b9c = g_100f94c1;
    }
    v6 = *((int *)0x63fe78);
    if (*((int *)0x63fe78) != v1 && g_100fa531 && g_100fa571 && *((int *)0x63fe78) < g_100fa571 && v0 >= *((int *)&g_100fa575))
    {
        if (!g_10080ba0 && !g_10080ba2 && !g_10080b98)
        {
            sub_10039413(&g_100fa531);
            g_10080ba2 = 3;
            g_10080ba7 = 0;
            v6 = g_1014f410 + 1;
            g_10080ba0 = v6;
        }
        g_10080ba6 = 2;
        return v6;
    }
    if (*((int *)0x63fe78) != v1 && g_100f949d && *((int *)0x63fe78) < g_100f949d)
    {
        if (!g_10080ba0 && !g_10080b98)
        {
            sub_10024f39();
            g_10080ba7 = g_10080ba7 + 1;
            v6 = g_1014f410 + 1;
            g_10080ba0 = v6;
        }
        g_10080ba6 = 2;
        return v6;
    }
    if (*((int *)0x63fe78) != v1 && g_100fa4f1 && g_100f9499 && *((int *)0x63fe78) < g_100f9499 && v0 >= *((int *)&g_100f9495))
    {
        if (!g_10080ba0 && !g_10080ba2 && !g_10080b98)
        {
            sub_10039413(&g_100fa4f1);
            g_10080ba2 = 3;
            g_10080ba7 = 0;
            v6 = g_1014f410 + 1;
            g_10080ba0 = v6;
        }
        g_10080ba6 = 2;
        return v6;
    }
    if (!g_10080ba7)
    {
        v2 = g_100f94c1;
        g_10080b98 = g_100f94c1;
        return *((int *)0x63fe78);
    }
    if (g_10080ba7 > 1)
    {
        v6 = sub_1002ffa3();
        if (!v6)
            v6 = sub_1002ade7(&g_10043315, 4);
    }
    g_10080ba7 = 0;
    return v6;
}
```

## `sub_10024cae` `0x10024cae`

_184 bytes. refs "health", "shealth", "ghealth"_

```c
typedef struct struct_0 {
    char padding_0[136];
    unsigned int field_88;
} struct_0;

extern int g_1004339b;
extern unsigned short g_100433a0;
extern char g_100433a2;
extern unsigned short g_100433a3;
extern char g_100433a5;
extern unsigned int g_100433a6;
extern unsigned int g_1005f7e5;
extern struct_0 *g_1005f7ed;
extern unsigned int g_10080b98;
extern unsigned int g_10080ba7;

unsigned int sub_10024cae(int a0)
{
    unsigned int v0;  // eax

    if (!lstrcmpi(a0, "health"))
    {
        v0 = 266;
    }
    else if (!lstrcmpi(a0, "shealth"))
    {
        v0 = 236;
    }
    else if (!lstrcmpi(a0, "ghealth"))
    {
        v0 = 239;
    }
    else
    {
        return 0;
    }
    if (g_10080b98)
        return v0;
    g_10080ba7 = 1;
    g_100433a3 = v0;
    g_100433a6 = g_1005f7e5;
    if (!g_1005f7ed || g_1005f7ed->field_88 >= 100)
        return 1;
    g_100433a0 = 0;
    g_100433a2 = 0;
    g_100433a5 = 0;
    sub_1002ade7(&g_1004339b, 15);
    return 1;
}
```

## `sub_10024d66` `0x10024d66`

_467 bytes. refs "exevo vis hur"_

```c
typedef struct struct_0 {
    char padding_0[80];
    char field_50;
} struct_0;

typedef struct struct_2 {
    char padding_0[44];
    unsigned int field_2c;
} struct_2;

extern struct_0 *g_1005f7ed;
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern char g_1005f85c;
extern char g_1008b89b;
extern unsigned int g_1008b8e8;
extern char g_100ee8dc;

struct_0 * sub_10024d66(void)
{
    char v6;  // 4103
    char v7;  // dl
    struct_2 *iter;  // ecx
    struct_0 *v9;  // eax
    unsigned int v10;  // esi
    unsigned int v11;  // edi
    struct_0 *v12;  // eax
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x5]

    if (!g_1005f7ed)
        return g_1005f7ed;
    v6 = g_1005f7ed->field_50;
    v4 = v6;
    v7 = v6;
    if (!v6)
    {
        v3 = g_1005f854 - 1;
        v2 = g_1005f854 + 1;
        v1 = g_1005f858 - 5;
        v0 = g_1005f858 - 3;
    }
    else if (v7 == 1)
    {
        v3 = g_1005f854 + 3;
        v2 = g_1005f854 + 5;
        v1 = g_1005f858 - 1;
        v0 = g_1005f858 + 1;
    }
    else if (v7 == 2)
    {
        v3 = g_1005f854 - 1;
        v2 = g_1005f854 + 1;
        v1 = g_1005f858 + 3;
        v0 = g_1005f858 + 5;
    }
    else if (v7 == 3)
    {
        v3 = g_1005f854 - 5;
        v2 = g_1005f854 - 3;
        v1 = g_1005f858 - 1;
        v0 = g_1005f858 + 1;
    }
    iter = 0x63fef8;
    v9 = *((int *)&g_1008b89b);
    while (true)
    {
        if (iter >= 0x64a308)
            return v9;
        if (*((int *)&iter->padding_0[0]) == v9 || !((v9 = (struct_0 *)sub_1003a494(iter + 4, iter), iter += 4, !v9)))
        {
            if (iter[3].padding_0[0] && iter->field_2c == *((int *)&g_1005f85c) && (v10 = (unsigned int)*((int *)&iter->padding_0[36]), v11 = (unsigned int)*((int *)&iter->padding_0[40]), *((int *)&iter->padding_0[36]) >= v3 && *((int *)&iter->padding_0[36]) <= v2 && *((int *)&iter->padding_0[40]) >= v1 && *((int *)&iter->padding_0[40]) <= v0 || !v4 && *((int *)&iter->padding_0[36]) == g_1005f854 && *((int *)&iter->padding_0[40]) < g_1005f858 && *((int *)&iter->padding_0[40]) >= v1 || v4 == 2 && *((int *)&iter->padding_0[36]) == g_1005f854 && *((int *)&iter->padding_0[40]) > g_1005f858 && *((int *)&iter->padding_0[40]) <= v0 || v4 == 1 && *((int *)&iter->padding_0[40]) == g_1005f858 && *((int *)&iter->padding_0[36]) > g_1005f854 && *((int *)&iter->padding_0[36]) <= v2 || v4 == 3 && *((int *)&iter->padding_0[40]) == g_1005f858 && *((int *)&iter->padding_0[36]) < g_1005f854 && *((int *)&iter->padding_0[36]) >= v3))
                break;
        }
        else
        {
            v9 = *((int *)&g_1008b89b);
        }
        iter = &iter[3].padding_0[24];
    }
    if (!g_100ee8dc)
        return sub_10039413("exevo vis hur");
    v12 = sub_10039413(&g_100ee8dc);
    g_1008b8e8 = 8;
    return v12;
}
```

## `sub_10024f39` `0x10024f39`

_117 bytes. (leaf/helper — see body)_

```c
extern void g_100432e5;
extern char g_100432e7;
extern unsigned short g_100432e8;
extern char g_100432ea;
extern unsigned int g_100432eb;
extern unsigned int g_1005f7e5;
extern char g_10080ba6;
extern char g_100fa4f0;

unsigned int sub_10024f39(unsigned int a0, char a1)
{
    unsigned int v1;  // eax
    char v2;  // dl

    v1 = sub_1002ae92(3160, 0, 0);
    if (!v1 && !g_100fa4f0)
        return v1;
    g_10080ba6 = 3;
    if (!g_100fa4f0)
    {
        g_100432e5 = v1;
        g_100432e7 = v2;
        g_100432ea = v2;
    }
    else
    {
        *((unsigned short *)&g_100432e5) = 0;
        g_100432e7 = 0;
        g_100432ea = 0;
    }
    g_100432e8 = 3160;
    g_100432eb = g_1005f7e5;
    return sub_1002ade7("\r", 15);
}
```

## `sub_10024fae` `0x10024fae`

_61 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_10052768;
extern unsigned int g_1005276c;
extern unsigned int g_10052770;
extern unsigned int g_1005f7d1;
extern unsigned int g_1005f7d5;

int sub_10024fae(void)
{
    g_1005f7d1 = *((int *)0x63fe94);
    g_1005f7d5 = *((int *)0x63fe78);
    g_10052768 = *((int *)0x64f608);
    g_1005276c = *((int *)0x64f604);
    g_10052770 = *((int *)0x64f600);
    return *((int *)0x64f600);
}
```

## `sub_10024feb` `0x10024feb`

_391 bytes. refs "None", "None", "None"_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned short field_8;
    char padding_a[1];
    int field_b;
} struct_0;

typedef struct struct_1 {
    char padding_0[36];
    unsigned short field_24;
    char padding_26[2];
    unsigned short field_28;
    char padding_2a[2];
    char field_2c;
} struct_1;

extern int g_10042cbb;
extern int g_100432ef;
extern int g_100432f2;
extern unsigned short g_100432fa;
extern unsigned short g_100432fc;
extern char g_100432fe;
extern unsigned short g_100432ff;
extern unsigned int g_10043324;
extern unsigned short g_1005f854;
extern unsigned short g_1005f858;
extern char g_1005f85c;
extern unsigned int g_10084bf7;
extern unsigned int g_10084bfb;
extern unsigned int g_1008b723;
extern unsigned int g_1008b89b;
extern char g_100f0d35;
extern char g_1013526b;

int sub_10024feb(void)
{
    void* v19;  // eax
    unsigned int v20;  // ecx
    unsigned int v29;  // eax
    unsigned int v30;  // edi
    int v31;  // eax
    unsigned int v21;  // edx
    unsigned int v22;  // ebx
    unsigned int v23;  // esi
    struct_0 *v24;  // eax
    struct_1 *v25;  // eax
    unsigned short v26;  // dx
    unsigned short v27;  // dx
    struct_1 *idx;  // eax
    int v0;  // [bp-0x17c]
    unsigned int v1;  // [bp-0x174]
    unsigned int v2;  // [bp-0x170]
    char *v3;  // [bp-0x16c]
    unsigned int v4;  // [bp-0x168]
    unsigned int v5;  // [bp-0x164]
    unsigned int v6;  // [bp-0x160]
    unsigned int v7;  // [bp-0x15c]
    unsigned int v8;  // [bp-0x158]
    unsigned int v9;  // [bp-0x150]
    char *v10;  // [bp-0x14c]
    char *v11;  // [bp-0x148]
    unsigned int v12;  // [bp-0x144]
    unsigned int v13;  // [bp-0x140]
    unsigned int v14;  // [bp-0x13c]
    void* v15;  // [bp-0x138]
    char v16;  // [bp-0x134]
    char v17;  // [bp-0x4]

    v15 = v19;
    v14 = v20;
    v13 = v21;
    v12 = v22;
    v11 = &v16;
    v10 = &v17;
    v9 = v23;
    if ((char)v19[2] == 132)
    {
        v24 = sub_1002ae6f("\r", v19, 15);
        g_10084bf7 = g_10043324;
        g_10084bfb = v24->field_8;
        if (g_1013526b)
        {
            v25 = sub_1003997e(*((int *)(v24->padding_a)[1]));
            if (v25 && v25->field_2c == g_1005f85c)
            {
                v26 = g_1005f854 - 7;
                if (v25->field_24 >= v26 && v25->field_24 - v26 < 15)
                {
                    v27 = g_1005f858 - 5;
                    if (v25->field_28 < v27 || v25->field_28 - v27 >= 11)
                    {
                        idx = sub_1002ae6f(&g_100432f2, v19 + 3, 8);
                        g_100432fa = idx->field_24;
                        g_100432fc = idx->field_28;
                        g_100432fe = idx->field_2c;
                        g_100432ff = 99;
                        sub_1002ae6f(v19, &g_100432ef, 19);
                    }
                }
            }
        }
    }
    else if ((char)v19[2] == 150 && (char)v19[3] == 1)
    {
        sub_10025f0c();
    }
    else if ((char)v19[2] == 161)
    {
        v29 = (int)v19[3];
        g_1008b89b = v29;
        v8 = v29;
        v7 = v20;
        v6 = v21;
        v5 = v22;
        v4 = &/* unsupported instruction */;
        v3 = &v17;
        v2 = v23;
        v1 = v30;
        if (g_1008b89b)
        {
            v31 = sub_1003997e(v8);
            if (v31)
            {
                v0 = v31;
                lstrcpy("None", v0 + 4);
                lstrcpy(&g_10042cbb, v0 + 4);
            }
        }
        else
        {
            lstrcpy("None", "None");
        }
    }
    else if ((char)v19[2] >= 100 && (char)v19[2] <= 104)
    {
        g_1008b723 = GetTickCount();
    }
    if (g_100f0d35)
        sub_1002592f();
    return;
}
```

## `sub_10025172` `0x10025172`

_328 bytes. calls CreateFileA, WriteFile; refs "elferrors459.log", "HH':'mm':'ss", "%s.%03d %s\r\n"_

```c
extern int g_10042d7b;
extern unsigned int g_1005f622;
extern unsigned int g_10291ce6;

int sub_10025172(unsigned int a0)
{
    unsigned int v12;  // eax
    char *v0;  // [bp-0x284]
    unsigned int v1;  // [bp-0x280]
    unsigned int v2;  // [bp-0x27c]
    char *v3;  // [bp-0x270]
    char *v4;  // [bp-0x26c]
    void* v5;  // [bp-0x258], Other Possible Types: char
    HANDLE v6;  // [bp-0x254]
    Byte v7[256];  // [bp-0x230]
    Byte v8[300];  // [bp-0x130]
    char v9;  // [bp-0x4]

    v4 = &v5;
    v3 = &v9;
    v5 = HeapAlloc(GetProcessHeap(), HEAP_NONE, 0x1000);
    lstrcpy(v8, &g_10042d7b);
    lstrcat(v8, "elferrors459.log");
    if (!g_10291ce6)
    {
        GetDateFormatA(0x400, 0, NULL, "'Elfbot NG 4.5.9 - Entry Started on 'dddd' 'MMMM' 'dd', 'yyyy", v7, 500);
        g_10291ce6 = 1;
        sub_10025172(v7);
    }
    v6 = CreateFileA(v8, 0xc0000000, 3, NULL, OPEN_ALWAYS, FILE_ATTRIBUTE_ARCHIVE, NULL);
    if (v6 != 0xffffffff)
    {
        SetFilePointer(v6, 0, NULL, FILE_END);
        GetTimeFormatA(0x400, 0, NULL, "HH':'mm':'ss", v7, 500);
        v2 = a0;
        v1 = GetTickCount() % 1000;
        v0 = &v7[0];
        WriteFile(v6, v5, wsprintfA(v5, "%s.%03d %s\r\n"), &g_1005f622, NULL);
        CloseHandle(v6);
    }
    HeapFree(GetProcessHeap(), HEAP_NONE, v5);
    return v12;
}
```

## `sub_100252ba` `0x100252ba`

_287 bytes. calls CreateFileA, WriteFile; refs "elfscript.log", "HH':'mm':'ss", "%s.%03d %s\r\n"_

```c
extern int g_10042d7b;
extern unsigned int g_1005f622;
extern unsigned int g_10291cde;

int sub_100252ba(unsigned int a0)
{
    unsigned int v11;  // eax
    char *v0;  // [bp-0xc44]
    unsigned int v1;  // [bp-0xc40]
    unsigned int v2;  // [bp-0xc3c]
    char *v3;  // [bp-0xc30]
    char *v4;  // [bp-0xc2c]
    HANDLE v5;  // [bp-0xc18], Other Possible Types: char
    Byte v6[256];  // [bp-0xbf4]
    Byte v7[2500];  // [bp-0xaf4]
    Byte v8[300];  // [bp-0x130]
    char v9;  // [bp-0x4]

    v4 = &v5;
    v3 = &v9;
    if (!g_10291cde)
    {
        GetDateFormatA(0x400, 0, NULL, "'Elfbot NG 4.5.9 - Entry Started on 'dddd' 'MMMM' 'dd', 'yyyy", v6, 0x100);
        g_10291cde = 1;
        sub_100252ba(v6);
    }
    lstrcpy(v8, &g_10042d7b);
    lstrcat(v8, "elfscript.log");
    v5 = CreateFileA(v8, 0xc0000000, 3, NULL, OPEN_ALWAYS, FILE_ATTRIBUTE_ARCHIVE, NULL);
    if (v5 != 0xffffffff)
    {
        SetFilePointer(v5, 0, NULL, FILE_END);
        GetTimeFormatA(0x400, 0, NULL, "HH':'mm':'ss", v6, 500);
        v2 = a0;
        v1 = GetTickCount() % 1000;
        v0 = &v6[0];
        WriteFile(v5, v7, wsprintfA(v7, "%s.%03d %s\r\n"), &g_1005f622, NULL);
        CloseHandle(v5);
    }
    return v11;
}
```

## `sub_100253d9` `0x100253d9`

_287 bytes. calls CreateFileA, WriteFile; refs "elflock459.log", "HH':'mm':'ss", "%s.%03d %s\r\n"_

```c
extern int g_10042d7b;
extern unsigned int g_1005f622;
extern unsigned int g_10291ce2;

int sub_100253d9(unsigned int a0)
{
    unsigned int v11;  // eax
    char *v0;  // [bp-0xc44]
    unsigned int v1;  // [bp-0xc40]
    unsigned int v2;  // [bp-0xc3c]
    char *v3;  // [bp-0xc30]
    char *v4;  // [bp-0xc2c]
    HANDLE v5;  // [bp-0xc18], Other Possible Types: char
    Byte v6[256];  // [bp-0xbf4]
    Byte v7[2500];  // [bp-0xaf4]
    Byte v8[300];  // [bp-0x130]
    char v9;  // [bp-0x4]

    v4 = &v5;
    v3 = &v9;
    if (!g_10291ce2)
    {
        GetDateFormatA(0x400, 0, NULL, "'Elfbot NG 4.5.9 - Entry Started on 'dddd' 'MMMM' 'dd', 'yyyy", v6, 0x100);
        g_10291ce2 = 1;
        sub_100253d9(v6);
    }
    lstrcpy(v8, &g_10042d7b);
    lstrcat(v8, "elflock459.log");
    v5 = CreateFileA(v8, 0xc0000000, 3, NULL, OPEN_ALWAYS, FILE_ATTRIBUTE_ARCHIVE, NULL);
    if (v5 != 0xffffffff)
    {
        SetFilePointer(v5, 0, NULL, FILE_END);
        GetTimeFormatA(0x400, 0, NULL, "HH':'mm':'ss", v6, 500);
        v2 = a0;
        v1 = GetTickCount() % 1000;
        v0 = &v6[0];
        WriteFile(v5, v7, wsprintfA(v7, "%s.%03d %s\r\n"), &g_1005f622, NULL);
        CloseHandle(v5);
    }
    return v11;
}
```

## `sub_100254f8` `0x100254f8`

_328 bytes. calls CreateFileA, ReadFile_

```c
extern int g_10042d7b;
extern unsigned int g_1005f622;

unsigned int sub_100254f8(int a0, int a1)
{
    char *v6;  // eax
    char *iter;  // ebx
    unsigned int v0;  // [bp-0x144]
    char *i;  // [bp-0x140]
    char *v2;  // [bp-0x13c]
    unsigned int size;  // [bp-0x138]
    HANDLE v4;  // [bp-0x134]
    Byte v5[300];  // [bp-0x130]

    lstrcpy(v5, &g_10042d7b);
    lstrcat(v5, a0);
    v4 = CreateFileA(v5, 0xc0000000, 3, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_ARCHIVE, NULL);
    if (v4 != 0xffffffff)
    {
        size = GetFileSize(v4, NULL);
        v6 = HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, size + 1);
        if (v6)
        {
            v2 = v6;
            if (ReadFile(v4, v2, size, &g_1005f622, NULL))
            {
                CloseHandle(v4);
                while (true)
                {
                    for (i = v2; *(iter) == 13 || *(iter) == 10; i = iter)
                    {
                        *(iter) = 0;
                        iter += 1;
                        if (*(iter) == 13)
                        {
                            iter += 1;
                        }
                        else if (*(iter) == 10)
                        {
                            iter += 1;
                        }
                        if (!lstrcmpi(i, a1))
                        {
                            v0 = 1;
                            HeapFree(GetProcessHeap(), HEAP_NONE, v2);
                            return 1;
                        }
                    }
                    if (!*(iter))
                        break;
                    iter += 1;
                }
                if (!lstrcmpi(i, a1))
                {
                    v0 = 1;
                    HeapFree(GetProcessHeap(), HEAP_NONE, v2);
                    return 1;
                }
            }
            else
            {
                CloseHandle(v4);
            }
        }
    }
    v0 = 0;
    HeapFree(GetProcessHeap(), HEAP_NONE, v2);
    return 0;
}
```

## `sub_100255fa` `0x100255fa`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100255fa(void)
{
}
```

## `sub_10025619` `0x10025619`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10025619(void)
{
}
```

## `sub_1002561e` `0x1002561e`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002561e(void)
{
}
```

## `sub_10025646` `0x10025646`

_496 bytes. calls CreateFileA, ReadFile_

```c
extern int g_10042d7b;
extern unsigned int g_1005f622;

int sub_10025646(char *a0, int a1)
{
    char *v7;  // eax
    char *node;  // ebx
    int v9;  // eax
    char *iter;  // ebx
    int v0;  // [bp-0x148]
    int iter1;  // [bp-0x144]
    char *v2;  // [bp-0x140]
    char *v3;  // [bp-0x13c]
    unsigned int size;  // [bp-0x138]
    HANDLE v5;  // [bp-0x134]
    Byte v6[300];  // [bp-0x130]

    lstrcpy(v6, &g_10042d7b);
    lstrcat(v6, a0);
    v5 = CreateFileA(v6, 0xc0000000, 3, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_ARCHIVE, NULL);
    if (v5 != 0xffffffff)
    {
        size = GetFileSize(v5, NULL);
        v7 = HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, size + 1);
        if (v7)
        {
            v3 = v7;
            if (ReadFile(v5, v3, size, &g_1005f622, NULL))
            {
                CloseHandle(v5);
                v2 = v3;
                while (true)
                {
                    for (iter1 = 0; *(node) == 13 || *(node) == 10; iter1 += 1)
                    {
                        node += 1;
                        if (*(node) == 13)
                        {
                            node += 1;
                        }
                        else if (*(node) == 10)
                        {
                            node += 1;
                        }
                        v2 = node;
                    }
                    if (!*(node))
                        break;
                    node += 1;
                }
                if (node != v2)
                    iter1 += 1;
                if (!iter1)
                    iter1 += 1;
                if (a1 == 0xffffffff)
                {
                    v9 = sub_10040a30(iter1);
                }
                else if (a1 > iter1)
                {
                    *(a0) = 0;
                    return HeapFree(GetProcessHeap(), HEAP_NONE, v3);
                }
                else
                {
                    v9 = a1;
                    if (a1)
                        v9 -= 1;
                }
                v0 = v9;
                iter1 = 0;
                iter = v3;
                v2 = iter;
                while (true)
                {
                    if (*(iter) == 13 || *(iter) == 10)
                    {
                        *(iter) = 0;
                        iter += 1;
                        if (*(iter) != 13)
                        {
                            if (*(iter) == 10)
                                iter += 1;
                        }
                        else
                        {
                            iter += 1;
                        }
                        if (iter1 == v0)
                        {
                            lstrcpy(a0, v2);
                            break;
                        }
                        else
                        {
                            v2 = iter;
                            iter1 += 1;
                        }
                    }
                    else if (!*(iter))
                    {
                        lstrcpy(a0, v2);
                        break;
                    }
                    else
                    {
                        iter += 1;
                    }
                }
                goto LABEL_10025827;
            }
            else
            {
                CloseHandle(v5);
            }
        }
    }
    *(a0) = 0;
LABEL_10025827:
    return HeapFree(GetProcessHeap(), HEAP_NONE, v3);
}
```

## `sub_10025740` `0x10025740`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10025740(void)
{
}
```

## `sub_100257f9` `0x100257f9`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100257f9(void)
{
}
```

## `sub_1002580f` `0x1002580f`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002580f(void)
{
}
```

## `sub_10025814` `0x10025814`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10025814(void)
{
}
```

## `sub_1002583e` `0x1002583e`

_241 bytes. calls CreateFileA, WriteFile; refs "\r\n"_

```c
extern int g_10042d7b;
extern unsigned int g_1005f622;

int sub_1002583e(int a0, int a1, unsigned int a2)
{
    unsigned int len;  // eax
    Byte *v4;  // ecx
    unsigned int v0;  // [bp-0x33c]
    char v1;  // [bp-0x338]
    Byte v2[300];  // [bp-0x130]

    lstrcpy(v2, &g_10042d7b);
    lstrcat(v2, a0);
    if (a2 == 2)
        return DeleteFileA(v2);
    v0 = CreateFileA(v2, 0xc0000000, 3, NULL, OPEN_ALWAYS, FILE_ATTRIBUTE_ARCHIVE, NULL);
    if (v0 == 4294967295)
        return v0;
    len = SetFilePointer(v0, 0, NULL, FILE_END);
    if (!a2)
    {
        len = lstrlen(a1);
    }
    else if (a2 == 1)
    {
        lstrcpyn(&v1, a1, 0x200);
        lstrcat(&v1, "\r\n");
        len = lstrlen(&v1);
    }
    WriteFile(v0, v4, len, &g_1005f622, NULL);
    return CloseHandle(v0);
}
```

## `sub_1002592f` `0x1002592f`

_330 bytes. calls CreateFileA, WriteFile; refs "elflog.txt", ");
    else
        lstrcat(v9, ", "\r\n"_

```c
extern int g_10042d7b;
extern unsigned int g_1005f622;
extern HANDLE g_100f0d40;

int sub_1002592f(void)
{
    void* v16;  // eax
    unsigned int v17;  // ecx
    unsigned int v18;  // edx
    unsigned int v19;  // ebx
    unsigned int v20;  // esi
    unsigned int v21;  // edi
    unsigned int v23;  // ebx
    char *i;  // ebx
    unsigned int len;  // eax
    unsigned int v0;  // [bp-0x97c]
    unsigned int v1;  // [bp-0x978]
    char *v2;  // [bp-0x974]
    unsigned int v3;  // [bp-0x970]
    unsigned int v4;  // [bp-0x96c]
    unsigned int v5;  // [bp-0x968]
    unsigned int v6;  // [bp-0x964]
    void* v7;  // [bp-0x960]
    void* v8;  // [bp-0x958]
    Byte v9[2047];  // [bp-0x954]
    char v11;  // [bp-0x154]
    char v12;  // [bp-0x14e]
    Byte v13[304];  // [bp-0x134]
    char v14;  // [bp-0x4]

    v8 = v16;
    v7 = v16;
    v6 = v17;
    v5 = v18;
    v4 = v19;
    v3 = &v17;
    v2 = &v14;
    v1 = v20;
    v0 = v21;
    if (!g_100f0d40)
    {
        lstrcpy(v13, &g_10042d7b);
        lstrcat(v13, "elflog.txt");
        g_100f0d40 = CreateFileA(v13, 0xc0000000, 3, NULL, OPEN_ALWAYS, FILE_ATTRIBUTE_ARCHIVE, NULL);
    }
    if (g_100f0d40 == 0xffffffff)
        return;
    sub_10040940(GetTickCount(), v9);
    if (!v17)
        lstrcat(v9, "c ");
    else
        lstrcat(v9, "b ");
    v23 = *((short *)v8);
    if (v23 > 300)
        v23 = 300;
    for (i = v23 + 2; i; i = &v11 + 1)
    {
        sub_100409a8(*((int *)v8), &v11, v8, i);
        lstrcat(v9, &v12);
        lstrcat(v9, " ");
        v8 = *((int *)v8) + 1;
    }
    SetFilePointer(g_100f0d40, 0, NULL, FILE_END);
    lstrcat(v9, "\r\n");
    len = lstrlen(v9);
    WriteFile(g_100f0d40, v9, len, &g_1005f622, NULL);
    return;
}
```

## `sub_10025a79` `0x10025a79`

_1171 bytes. refs ";
        wsprintfA(v15, ", "None", "None"_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned short field_8;
    char padding_a[1];
    int field_b;
} struct_0;

typedef struct struct_1 {
    char padding_0[36];
    unsigned short field_24;
    char padding_26[2];
    unsigned short field_28;
    char padding_2a[2];
    char field_2c;
} struct_1;

typedef struct struct_3 {
    unsigned int field_0;
    char padding_4[32];
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
    char padding_30[96];
    char field_90;
} struct_3;

extern char g_10025b03;
extern char g_10025c0b;
extern char g_10025cf0;
extern char g_10025e11;
extern char g_10025e8d;
extern char g_10025ed3;
extern char g_10025f0a;
extern int g_10042cbb;
extern int g_100432ef;
extern int g_100432f2;
extern unsigned short g_100432fa;
extern unsigned short g_100432fc;
extern char g_100432fe;
extern unsigned short g_100432ff;
extern unsigned int g_10043324;
extern unsigned int g_1005277c;
extern unsigned int g_10052780;
extern unsigned int g_1005dbd8;
extern unsigned int g_1005dbdc;
extern unsigned int g_1005dbe0;
extern unsigned int g_1005dbe4;
extern void g_1005f854;
extern void g_1005f858;
extern unsigned int g_1005f85c;
extern char g_1005f8a4;
extern char g_10080b6e;
extern unsigned int g_10084bf7;
extern unsigned int g_10084bfb;
extern unsigned int g_1008b723;
extern unsigned int g_1008b89b;
extern unsigned int g_1008b89f;
extern unsigned int g_1008b8e4;
extern unsigned int g_100ee8bc;
extern unsigned int g_100ee8c0;
extern unsigned int g_100ee8c4;
extern char g_100f0d35;
extern char g_100f9317;
extern char g_100f94c6;
extern char g_1013526b;
extern unsigned int g_1028987c;
extern unsigned int g_10289880;
extern unsigned int g_10289884;

int sub_10025a79(void)
{
    void* v18;  // eax
    unsigned int v19;  // ecx
    unsigned int v27;  // edi
    unsigned int v28;  // edx
    unsigned int v29;  // edi
    unsigned int v30;  // edi
    void* index;  // eax
    struct_0 *v32;  // eax
    struct_1 *v33;  // eax
    unsigned short v34;  // dx
    unsigned short v35;  // dx
    struct_1 *idx;  // eax
    unsigned int v20;  // edx
    unsigned int v37;  // ebx
    struct_3 *iter;  // ebx
    unsigned int v39;  // ecx
    unsigned int v40;  // eax
    int v41;  // eax
    void* v42;  // ecx
    int v21;  // ebx
    unsigned int v22;  // esi
    unsigned int v23;  // edi
    unsigned int v24;  // edi
    unsigned int v25;  // edi
    unsigned int v26;  // esi
    int v0;  // [bp-0x19c]
    unsigned int v1;  // [bp-0x198]
    unsigned int v2;  // [bp-0x190]
    char *v3;  // [bp-0x18c]
    unsigned int v4;  // [bp-0x188]
    int v5;  // [bp-0x184]
    unsigned int v6;  // [bp-0x180]
    void* v7;  // [bp-0x178], Other Possible Types: unsigned int
    unsigned int v8;  // [bp-0x170]
    char *v9;  // [bp-0x16c]
    char *v10;  // [bp-0x168]
    int v11;  // [bp-0x164]
    unsigned int v12;  // [bp-0x160]
    unsigned int v13;  // [bp-0x15c]
    void* v14;  // [bp-0x158]
    Byte v15[336];  // [bp-0x154]
    char v16;  // [bp-0x4]

    v14 = v18;
    v13 = v19;
    v12 = v20;
    v11 = v21;
    v10 = &v15[0];
    v9 = &v16;
    v8 = v22;
    v42 = (char)v18[2];
    g_1005dbe4 = &v16;
    g_1005dbe0 = &/* unsupported instruction */;
    g_1005dbd8 = 201;
    g_1005dbdc = &g_10025b03;
    if ((char)v18[2] == 131 || (v24 = v23, (char)v18[2] == 132))
    {
        v25 = v23;
        if ((short)v18[8] == 3180)
        {
            g_1008b8e4 = 200;
            v26 = (short)v18[11];
            v27 = (short)v18[13];
            v28 = (char)v18[15];
            g_100ee8bc = v26;
            g_100ee8c0 = v27;
            g_100ee8c4 = v28;
            v25 = v27;
        }
        v29 = v25;
        v24 = v29;
        if (g_100f94c6)
        {
            g_100f94c6 = 2;
            v24 = v29;
        }
    }
    v30 = v24;
    if ((char)v18[2] == 20)
        g_100f9317 = 50;
    index = v18;
    if ((char)index[2] == 132)
    {
        g_1005dbe4 = &v16;
        g_1005dbe0 = &/* unsupported instruction */;
        g_1005dbd8 = 202;
        g_1005dbdc = &g_10025c0b;
        v32 = sub_1002ae6f("\r", index, 15);
        g_10084bf7 = g_10043324;
        g_10084bfb = v32->field_8;
        v42 = index;
        if (g_1013526b)
        {
            v33 = sub_1003997e(*((int *)(v32->padding_a)[1]));
            if (v33)
            {
                if (v33->field_2c == (char)g_1005f85c)
                {
                    v34 = *((short *)&g_1005f854) - 7;
                    if (v33->field_24 >= v34 && v33->field_24 - v34 < 15)
                    {
                        v35 = *((short *)&g_1005f858) - 5;
                        if (v33->field_28 < v35 || v33->field_28 - v35 >= 11)
                        {
                            idx = sub_1002ae6f(&g_100432f2, v18 + 3, 8);
                            g_100432fa = idx->field_24;
                            g_100432fc = idx->field_28;
                            g_100432fe = idx->field_2c;
                            g_100432ff = 99;
                            v30 = 19;
                            sub_1002ae6f(v18, &g_100432ef, 19);
                        }
                    }
                }
            }
            v42 = index;
        }
    }
    else if ((char)index[2] == 121)
    {
        g_10080b6e = 50;
        v7 = (short)index[3];
        v42 = "%d";
        wsprintfA(v15, "%d");
        sub_10039374(v15);
    }
    else if ((char)index[2] == 140)
    {
        g_1005dbe4 = &v16;
        g_1005dbe0 = &/* unsupported instruction */;
        g_1005dbd8 = 203;
        g_1005dbdc = &g_10025cf0;
        g_10080b6e = 50;
        if (!g_1005f8a4)
        {
            v7 = index;
            v6 = v28;
            v5 = v21;
            v4 = &/* unsupported instruction */;
            v3 = &v16;
            v2 = v26;
            v37 = (short)index[8];
            if (v37 == 99)
            {
                iter = 0x63fef8;
                while (iter < 0x64a308)
                {
                    if (iter->field_90 && (short)index[3] == iter->field_24 && (short)index[5] == iter->field_28 && (char)index[7] == iter->field_2c)
                    {
                        v37 = iter->field_0;
                        goto LABEL_10025cce;
                    }
                    else
                    {
                        iter = &iter[1].padding_4[19];
                    }
                }
            }
LABEL_10025cce:
            v1 = v37;
            wsprintfA(v15, "%d");
            sub_10039374(v15);
            v42 = v42;
        }
    }
    else if ((char)index[2] >= 100 && (char)index[2] <= 104)
    {
        if (g_1005277c == 2)
        {
            if ((char)index[2] == 100)
            {
                v39 = (char)index[4];
                if ((char)v39 == 1)
                {
                    v39 = _INSERT(v39, 0, 2);
                }
                else if ((char)v39 == 2)
                {
                    v39 = _INSERT(v39, 0, 5);
                }
                else if ((char)v39 == 3)
                {
                    v39 = _INSERT(v39, 0, 1);
                }
                else if ((char)v39 == 4)
                {
                    v39 = _INSERT(v39, 0, 8);
                }
                else if ((char)v39 == 5)
                {
                    v39 = _INSERT(v39, 0, 4);
                }
                else if ((char)v39 == 6)
                {
                    v39 = _INSERT(v39, 0, 7);
                }
                else if ((char)v39 == 7)
                {
                    v39 = _INSERT(v39, 0, 3);
                }
                else if ((char)v39 == 8)
                {
                    v39 = _INSERT(v39, 0, 6);
                }
            }
            else
            {
                v39 = (char)index[2] - 100;
            }
            *((unsigned int *)index) = 0;
            g_10052780 = v39;
        }
        else
        {
            if ((char)index[2] == 100)
            {
                if (g_1005277c == 1 && (char)index[3] > 1)
                {
                    *((char *)&index[3]) = 2;
                    *((unsigned short *)index) = 4;
                }
                v42 = (char)index[4];
            }
            else
            {
                v7 = index;
                g_1028987c = *((int *)&g_1005f854);
                g_10289880 = *((int *)&g_1005f858);
                g_10289884 = g_1005f85c;
            }
            v7 = index;
            v6 = v28;
            v5 = v21;
            v4 = &/* unsupported instruction */;
            v3 = &v16;
            v2 = v26;
            g_1008b723 = GetTickCount();
        }
    }
    else
    {
        if ((char)index[2] == 150 && (char)index[3] == 1)
        {
            g_1005dbe4 = &v16;
            g_1005dbe0 = &/* unsupported instruction */;
            g_1005dbd8 = 0xcc;
            g_1005dbdc = &g_10025e11;
            if (!sub_10025f0c(index))
                *((unsigned short *)index) = 0;
        }
        else if ((char)index[2] == 161)
        {
            g_1005dbe4 = &v16;
            g_1005dbe0 = &/* unsupported instruction */;
            g_1005dbd8 = 205;
            g_1005dbdc = &g_10025e8d;
            v40 = (int)index[3];
            g_1008b89b = v40;
            g_1008b89f = v40;
            v7 = v40;
            v6 = v28;
            v5 = v21;
            v4 = &/* unsupported instruction */;
            v3 = &v16;
            v2 = v26;
            if (g_1008b89b)
            {
                v41 = sub_1003997e(v7);
                if (v41)
                {
                    v0 = v41;
                    lstrcpy("None", v0 + 4);
                    lstrcpy(&g_10042cbb, v0 + 4);
                }
            }
            else
            {
                lstrcpy("None", "None");
            }
            v42 = v42;
        }
        else if ((char)index[2] == 0xdd)
        {
            g_1005dbe4 = &v16;
            g_1005dbe0 = &/* unsupported instruction */;
            g_1005dbd8 = 206;
            g_1005dbdc = &g_10025ed3;
            sub_10040940((int)index[3], v15, v30, v26, &v16, &/* unsupported instruction */, v21, v28, v42, index);
            sub_10039374(v15);
            v42 = v42;
        }
    }
    g_1005dbe4 = v30;
    g_1005dbe0 = &v42;
    g_1005dbd8 = 207;
    g_1005dbdc = &g_10025f0a;
    if (g_100f0d35)
        sub_1002592f();
    return;
}
```

## `sub_10025f0c` `0x10025f0c`

_1052 bytes. (leaf/helper — see body)_

```c
extern char g_10026285;
extern char g_1002628e;
extern char g_100262c5;
extern char g_10026339;
extern char g_10042c7b;
extern unsigned int g_1005dbd8;
extern unsigned int g_1005dbdc;
extern unsigned int g_1005dbe0;
extern unsigned int g_1005dbe4;
extern unsigned int g_1005dbe8;
extern unsigned int g_10084c0b;
extern unsigned int g_10087a0b[4];
extern char g_1008858b[4][4];
extern unsigned int g_1008910b;
extern char g_100f0d35;
extern unsigned int g_100f49d5;
extern unsigned short g_10106b02;
extern unsigned short g_101179e0;
extern char g_10117a01;
extern char g_10117a02;
extern char g_10135279;
extern char g_1013f327;

int sub_10025f0c(void)
{
    void* v21;  // ebp
    void* v22;  // eax
    unsigned short *v31;  // ebx
    unsigned int v32;  // ecx
    void* index;  // edx
    char v34[4][4];  // eax
    char v35[4][4];  // ebx
    int node;  // ecx
    unsigned int v37;  // ecx
    char v38[4][4];  // eax
    void* v39;  // ecx
    void* idx;  // edx
    unsigned int v23;  // ebx
    void* v41;  // eax
    unsigned int v42;  // ecx
    unsigned int j;  // esi
    char *iter;  // edi
    unsigned int v24;  // ebx
    unsigned int v25;  // ecx
    unsigned int v26;  // edx
    unsigned int v27;  // esi
    unsigned int v28;  // edi
    unsigned int v29;  // ebx
    unsigned short v30;  // cx
    char *v1;  // [bp-0x250]
    void* v2;  // [bp-0x24c]
    unsigned short *v3;  // [bp-0x248], Other Possible Types: unsigned int
    unsigned int v4;  // [bp-0x244]
    char *v5;  // [bp-0x23c], Other Possible Types: unsigned int
    unsigned int v6;  // [bp-0x238]
    char *v7;  // [bp-0x234]
    char *v8;  // [bp-0x230]
    void* v9;  // [bp-0x22c], Other Possible Types: unsigned int
    unsigned int v10;  // [bp-0x228]
    unsigned int v11;  // [bp-0x224]
    void* v12;  // [bp-0x220]
    char v13;  // [bp-0x21c], Other Possible Types: unsigned int
    unsigned int v14;  // [bp-0x218]
    unsigned int iter1;  // [bp-0x214]
    int v16;  // [bp-0x210]
    int v17;  // [bp-0x20c]
    void* v18;  // [bp-0x8], Other Possible Types: unsigned int
    char v19;  // [bp+0x0]

    *((char **)&(&v16)[524]) = &v19;
    v21 = &v16 - 524;
    *((void* *)&v16) = v22;
    v24 = v23;
    if (g_10135279)
    {
        g_1005dbe4 = &v16 - 524;
        g_1005dbe0 = &v13;
        g_1005dbd8 = 2001;
        g_1005dbdc = &g_100262c5;
        g_1005dbe8 = 0;
        v12 = v22;
        v11 = v25;
        v10 = v26;
        v9 = v23;
        v8 = &v13;
        v7 = &v16 - 524;
        v6 = v27;
        v5 = v28;
        v14 = (short)v22[4];
        v29 = _INSERT(v23, 0, *(6 + v14 + (char *)v22));
        *(6 + v14 + (char *)v22) = 0;
        v4 = v29;
        v18 = v22 + 6;
        v30 = *((char *)v18);
        if (g_1013f327 && (char)v30 == g_1013f327)
        {
            v17 = (int)_INSERT(*((uint1872_t *)&v16), 0, 127);
            v31 = &g_101179e0;
            g_10117a01 = 1;
            g_101179e0 = v30;
            v1 = &g_10117a02;
            lstrcpyn(&g_10117a02, v18 + 1, 0x200);
LABEL_10026029:
            v3 = g_100f49d5;
            (&g_1008910b)[96 + *((unsigned int *)&v17)] = g_100f49d5;
            v3 = v31 + 0x11;
            v2 = &v17 - 4;
            lstrcpy(&v17 - 4, v31 + 0x11);
            if (*((unsigned int *)(&v17 + 4)) == 1869903201 && *((char *)(&v17 + 8)) == 32)
            {
                g_1005dbe4 = &v16 - 524;
                g_1005dbe0 = &v4;
                g_1005dbd8 = 2004;
                g_1005dbe8 = &v17 - 4;
                v3 = NULL;
                v2 = *((unsigned int *)&v17) + 96;
                v1 = &v17 - 4;
                sub_10030442(&v17 - 4, *((unsigned int *)&v17) + 96, 0);
            }
            else
            {
                index = *((unsigned int *)&v17) + 96;
                if (!*((int *)(0x4 * index + &g_1008858b[0])) && !*((int *)(0x4 * index + (char *)&g_10087a0b[0])) || (*((unsigned int *)(0x4 * (unsigned int)index + (char *)&g_1008858b[0])) = 0, *((unsigned int *)(0x4 * (unsigned int)index + (char *)&g_10087a0b[0])) = 0, *((unsigned int *)(void*)&v17) == 127))
                {
                    *((unsigned int *)(0x4 * index + (char *)&g_10084c0b)) = 0;
                    v34 = &v17 - 4;
                    v35 = &v17 - 4;
                    iter1 = 0;
                    node = 0;
                    while (node < 0x200)
                    {
                        g_1005dbe4 = &v16 - 524;
                        g_1005dbe0 = &v1;
                        g_1005dbd8 = 2003;
                        g_1005dbdc = &g_10026285;
                        g_1005dbe8 = v35;
                        if (v34[node] == 123)
                        {
                            iter1 += 1;
                            node += 1;
                            continue;
                        }
                        if (v34[node] == 125)
                        {
                            iter1 -= 1;
                            if (iter1 == 4294967295)
                            {
                                v13 = 1;
                                iter1 = 0;
                                goto LABEL_100261d4;
                            }
                            else
                            {
                                if (!iter1)
                                {
                                    v13 = 0;
                                    node += 1;
                                    goto LABEL_100261d4;
                                }
                                else
                                {
                                    node += 1;
                                }
                            }
                        }
                        else if (!iter1 && v34[node] == 124 && v34[1 + node] != 124 && v34[1 + node] != 124)
                        {
                            v13 = 1;
LABEL_100261d4:
                            v34[node] = 0;
                            v37 = *((unsigned int *)&v17);
                            sub_10030442(v35, v37 + 96, 0, v34, node, v34[node]);
                            v38 = v35;
                            v39 = v37 + 96;
                            *((unsigned int *)(v39 + v38)) = 0;
                            v34 = v38 + v39 + v13;
                            v35 = v34;
                            idx = *((unsigned int *)&v17) + 96;
                            if (*((int *)(0x4 * idx + (char *)&g_10087a0b[0])) == 4294967295)
                            {
                                *((unsigned int *)(0x4 * idx + (char *)&g_10087a0b[0])) = 0;
                                *((unsigned int *)(0x4 * idx + &g_1008858b[0])) = 0;
                                break;
                            }
                            else
                            {
                                if (*((int *)(0x4 * idx + (char *)&g_10087a0b[0])))
                                {
                                    if (*((int *)(0x4 * idx + &g_1008858b[0])))
                                        v34 = *((int *)(0x4 * idx + &g_1008858b[0]));
                                    *((unsigned long *)(0x4 * idx + &g_1008858b[0])) = v34 - (&v17 - 4);
                                    break;
                                }
                                else
                                {
                                    node = 0;
                                }
                            }
                        }
                        else if (!v34[node])
                        {
                            sub_10030442(v35, *((unsigned int *)&v17) + 96, 0);
                            break;
                        }
                        else
                        {
                            node += 1;
                        }
                    }
                }
            }
            v18 = 1;
        }
        else
        {
            v31 = &g_10106b02;
            v32 = 0;
            v17 = v16;
            while (true)
            {
                if (v32 >= 128)
                    break;
                g_1005dbe4 = &v16 - 524;
                g_1005dbe0 = &v4;
                g_1005dbd8 = 2002;
                g_1005dbdc = &g_1002628e;
                g_1005dbe8 = 0;
                *((unsigned int *)&v17) = v32;
                if (*((char *)&v31[16] + 1) && (v3 = v3, v2 = v2, *((char *)v31) && (v3 = v3, v2 = v2, (char)v31[0x11] && (v3 = v31, v2 = v18, !lstrcmp(v2, v3)))))
                    goto LABEL_10026029;
                v32 = *((unsigned int *)&v17) + 1;
                v31 += 273;
            }
            *((unsigned int *)&(&v16)[520]) = 0;
        }
        *(6 + v14 + (char *)v2) = *((char *)&v1);
        v21 = v22;
        v24 = v6;
        if ((int)v21[4])
            return;
    }
    g_1005dbe4 = v21;
    g_1005dbe0 = &v10;
    g_1005dbd8 = 2005;
    g_1005dbdc = &g_10026339;
    g_1005dbe8 = 0;
    v41 = (int)v21[524];
    if ((int)v41[6] == 1986623589 && (short)v41[10] == 8289)
    {
        v9 = v41;
        v6 = v24;
        v5 = &v10;
        v42 = (short)v41[4] - 6;
        if (v42 >= 64)
            return;
        j = v41 + 12;
        for (iter = &g_10042c7b; v42; j += 1)
        {
            v42 -= 1;
            *(iter) = *((char *)j);
            iter += 1;
        }
        *(iter) = 0;
        return;
    }
    if ((short)v41[4] == 4 && (short)v41[6] == 27694)
        g_100f0d35 = 20;
    return;
}
```

## `sub_10025fb8` `0x10025fb8`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10025fb8(void)
{
}
```

## `sub_100260ee` `0x100260ee`

_5 bytes. (leaf/helper — see body)_

```c
void sub_100260ee(void)
{
}
```

## `sub_10026179` `0x10026179`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10026179(void)
{
}
```

## `sub_10026198` `0x10026198`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10026198(void)
{
}
```

## `sub_1002622e` `0x1002622e`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002622e(void)
{
}
```

## `sub_1002625c` `0x1002625c`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002625c(void)
{
}
```

## `sub_10026340` `0x10026340`

_219 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_1005dc4c;
extern unsigned int g_1005dc4e;
extern unsigned int g_1005dc52;
extern unsigned int g_1005dc56;
extern unsigned int g_1005dc5a;
extern unsigned int g_1005dc5e;
extern unsigned int g_1005dc62;
extern unsigned short g_1005dc66;
extern unsigned short g_1005dc68;
extern unsigned short g_1005dc6a;
extern unsigned short g_1005dc6c;
extern unsigned short g_1005dc6e;
extern unsigned short g_1005dc70;
extern unsigned short g_1005dc72;
extern unsigned short g_1013f300;
extern unsigned short g_1013f304;
extern unsigned short g_1013f308;
extern unsigned short g_1013f30c;
extern unsigned short g_1013f310;
extern unsigned short g_1013f314;
extern unsigned short g_1013f318;
extern unsigned int g_102898c4;
extern unsigned int g_102898c8;

int sub_10026340(void)
{
    unsigned int v3;  // eax
    unsigned int v0;  // [bp-0x24]
    unsigned short v1;  // [bp-0x22]

    g_1005dc4c = 0;
    v0 = g_102898c4;
    g_1005dc4e = g_102898c4;
    v0 = g_102898c8;
    g_1005dc52 = g_102898c8;
    g_102898c8 = 0;
    v0 = *((int *)0x7998bc);
    g_1005dc56 = *((int *)0x7998bc);
    v0 = *((int *)0x7998c0);
    g_1005dc5a = *((int *)0x7998c0);
    v0 = *((int *)0x7998c4);
    g_1005dc5e = *((int *)0x7998c4);
    v0 = *((int *)0x7998c8);
    g_1005dc62 = *((int *)0x7998c8);
    v1 = g_1013f300;
    g_1005dc66 = v1;
    v1 = g_1013f304;
    g_1005dc68 = v1;
    v1 = g_1013f310;
    g_1005dc6a = v1;
    v1 = g_1013f308;
    g_1005dc6c = v1;
    v1 = g_1013f30c;
    g_1005dc6e = v1;
    v1 = g_1013f314;
    g_1005dc70 = v1;
    v1 = g_1013f318;
    g_1005dc72 = v1;
    send(*((int *)(*((int *)0x799890) + 4)), &g_1005dc4c, 40, 0);
    Sleep(400);
    return v3;
}
```

## `sub_1002641f` `0x1002641f`

_284 bytes. (leaf/helper — see body)_

```c
extern char g_1002646f;
extern char g_10026531;
extern char g_1004287c;
extern unsigned int g_1005dbd8;
extern unsigned int g_1005dbdc;
extern unsigned int g_1005dbe0;
extern char g_1005dbe4;
extern unsigned int g_1005dbe8;
extern char g_100f0d36;
extern char g_100f0d37;
extern unsigned int g_102898c8;
extern char g_35;
extern unsigned int g_7998a8;

int sub_1002641f(void)
{
    unsigned int v10;  // cc_op
    unsigned int v11;  // cc_dep1
    unsigned long v20;  // 4166
    int v21;  // eax
    unsigned int v22;  // ecx
    unsigned int v23;  // edx
    unsigned int v24;  // ebx
    unsigned int v25;  // esi
    unsigned int v26;  // esi
    int v27;  // ecx
    unsigned long v28;  // 4109
    unsigned int v12;  // cc_dep2
    unsigned int v13;  // cc_ndep
    unsigned int v14;  // 4161
    unsigned int idx;  // edi
    char *v16;  // eax
    unsigned long v17;  // ldt
    unsigned long v18;  // gdt
    unsigned short v19;  // fs
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    int v6;  // [bp-0x4]
    unsigned int v7;  // [bp+0x0]

    v14 = _ccall(v10, v11, v12, v13);
    *((char *)(idx * 9 + 53)) = *((char *)(idx * 9 + 53)) + *((char *)((void*)&v16 + 1)) + ((char)v14 & 1);
    *(v16) = *(v16) + *((char *)&v16);
    *(v16) = *(v16) + *((char *)&v16);
    v20 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((unsigned int **)v20) = &v7;
    *((int *)&g_1005dbe4) = /* unsupported instruction */;
    g_1005dbe0 = &v7;
    g_1005dbd8 = 1;
    g_1005dbdc = &g_1002646f;
    g_1005dbe8 = 0;
    if (g_102898c8 && g_100f0d37)
        v21 = sub_10026340();
    *((int *)&g_1005dbe4) = /* unsupported instruction */;
    g_1005dbe0 = &v7;
    g_1005dbd8 = 2;
    g_1005dbdc = &g_10026531;
    if (!g_1004287c)
    {
        v6 = v21;
        v5 = v22;
        v4 = v23;
        v3 = v24;
        v2 = /* unsupported instruction */;
        v1 = v25;
        *((int *)&g_1005dbe4) = /* unsupported instruction */;
        g_1005dbe0 = &/* unsupported instruction */;
        g_1005dbd8 = 3;
        g_1005dbdc = "a";
        if (g_7998a8 > 8)
        {
            v26 = *((int *)0x7998a0) + 6;
            v27 = _INSERT(v22, 0, *((short *)v26));
            *((unsigned short *)v26) = g_7998a8 - 8;
            v0 = v26;
            sub_10025a79(g_1005dbdc, g_1005dbd8, g_1005dbe0, v0, v27);
            g_1005dbdc = g_1005dbdc;
            g_1005dbd8 = g_1005dbd8;
            g_1005dbe0 = g_1005dbe0;
            g_7998a8 = *((short *)v0) + 8;
            *((short *)v0) = v27;
            if (g_100f0d36)
            {
                g_7998a8 = 4;
                *((unsigned short *)v0) = 0;
            }
        }
    }
    v28 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((unsigned int *)v28) = v7;
    sub_1002653b(); /* do not return */
}
```

## `sub_1002653b` `0x1002653b`

_10 bytes. (leaf/helper — see body)_

```c
void sub_1002653b(void)
{
}
```

