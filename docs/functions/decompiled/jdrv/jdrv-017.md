# elfbot.dll decompiled — jdrv 0x10038d20..0x1003a70a

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10038d20` `0x10038d20`

_28 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10038d20(void)
{
    unsigned int v1;  // eax
    unsigned int *i;  // ecx

    v1 = 0;
    for (i = 0x64cd10; v1 < 16; i += 123)
    {
        if (!*(i))
            return v1;
        v1 += 1;
    }
    return v1;
}
```

## `sub_10038d3c` `0x10038d3c`

_237 bytes. calls SendDlgItemMessageA; refs "## Scram ##"_

```c
extern char g_1005f535;
extern HWND g_1005f626;

LRESULT sub_10038d3c(void)
{
    LRESULT v7;  // eax
    char v8[4];  // ebx
    char iter[4];  // ebx
    char node[4];  // ebx
    char iter1[4];  // ebx
    char iter2[4];  // ebx
    LRESULT count;  // eax
    char v0[4];  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    if (g_1005f535 != 1)
        return v7;
    for (v0 = v8; iter[0] != 32; iter = &iter[1]);
    iter[0] = 0;
    node = &iter[1];
    v5 = sub_10040900(v0);
    for (v0 = node; node[0] != 32; node = &node[1]);
    node[0] = 0;
    iter1 = &node[1];
    v4 = sub_10040900(v0);
    for (v0 = iter1; iter1[0] != 32; iter1 = &iter1[1]);
    iter1[0] = 0;
    iter2 = &iter1[1];
    v3 = sub_10040900(v0);
    for (v0 = iter2; iter2[0] != 32; iter2 = &iter2[1]);
    iter2[0] = 0;
    v2 = sub_10040900(v0);
    v1 = sub_10040900(&iter2[1]);
    count = 0x1;
    while (true)
    {
        do
        {
            if (!count)
                return count;
        } while ((count = (int *)sub_1003bfec(), !count));
        if (count[11] == v1 && count[9] >= v5 && count[9] <= v4 && count[10] >= v3 && count[10] <= v2)
            break;
    }
    if (g_1005f535 == 1)
    {
        g_1005f535 = 2;
        count = SendDlgItemMessageA(g_1005f626, 0x404, 12, NULL, "## Scram ##");
    }
    return count;
}
```

## `sub_10038e29` `0x10038e29`

_138 bytes. (leaf/helper — see body)_

```c
int sub_10038e29(unsigned int a0, unsigned int a1)
{
    unsigned int len;  // eax
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // ss
    unsigned long v11;  // 4127
    unsigned int v12;  // eax
    unsigned int v0;  // [bp-0x20c]
    unsigned int len1;  // [bp-0x208]
    unsigned int v2;  // [bp-0x208]
    unsigned int v3;  // [bp-0x204], Other Possible Types: unsigned short
    unsigned short v4;  // [bp-0x200]
    char v5[2];  // [bp-0x1fe]
    char v6;  // [bp-0x1fc]

    v3 = 110493709;
    len1 = lstrlen(a0);
    v4 = len1;
    sub_1002ae6f(v5, a0, len1);
    len = lstrlen(a1);
    v2 = len1 + len;
    v11 = _ccall(v8, v9, (unsigned int)v10, v5 + len1);
    *((unsigned short *)v11) = len;
    sub_1002ae6f(&(&v6)[len1], a1, len);
    v12 = v2 + 6;
    v3 = v12;
    v0 = v12 + 2;
    return sub_1002ade7(&v3);
}
```

## `sub_10038eb3` `0x10038eb3`

_743 bytes. refs "enemy", "subenemy", "anyenemy"_

```c
typedef struct struct_1 {
    char padding_0[136];
    unsigned int field_88;
} struct_1;

typedef struct struct_0 {
    char padding_0[144];
    unsigned int field_90;
} struct_0;

typedef struct struct_3 {
    char padding_0[36];
    int field_24;
    int field_28;
    char padding_2c[92];
    unsigned int field_88;
} struct_3;

extern struct_1 *g_1005f7ed;
extern int g_1008b89b;
extern char g_100fa97a;

struct_1 * sub_10038eb3(char *a0, unsigned int a1, int a2)
{
    struct_0 *v3;  // eax
    struct_1 *v4;  // eax
    struct_1 *v5;  // eax
    struct_1 *v6;  // eax
    struct_1 *v7;  // eax
    struct_0 *v8;  // eax
    struct_1 *v9;  // eax
    struct_1 *v10;  // eax
    struct_1 *v11;  // eax
    struct_3 *v12;  // eax
    unsigned int v0;  // [bp-0x10]
    struct_1 *v1;  // [bp-0xc]
    struct_1 *v2;  // [bp-0x8]

    if (*(a0) >= 48 && *(a0) <= 57)
    {
        v3 = sub_1003997e(sub_10040900(a0));
        if (!v3 || !v3->field_90)
            return NULL;
        v4 = sub_1003c23e(v3);
        if (v4 && a2)
            v4 = sub_1003bbc1(v4, a2);
        return v4;
        return NULL;
    }
    if (!lstrcmpi(a0, "enemy"))
    {
        return sub_1003bc54();
    }
    else if (!lstrcmpi(a0, "subenemy"))
    {
        return sub_1003bc54();
    }
    else if (!lstrcmpi(a0, "anyenemy"))
    {
        v5 = sub_1003bc54();
        if (v5)
            return v5;
        return sub_1003bc54();
    }
    else if (!lstrcmpi(a0, "friend"))
    {
        return sub_1003bec5();
    }
    else if (!lstrcmpi(a0, "subfriend"))
    {
        return sub_1003bec5();
    }
    else if (!lstrcmpi(a0, "anyfriend"))
    {
        v6 = sub_1003bec5();
        if (v6)
            return v6;
        return sub_1003bec5();
    }
    else if (!lstrcmpi(a0, "self"))
    {
        return g_1005f7ed;
    }
    else
    {
        v7 = lstrcmpi(a0, "target");
        if (!v7)
        {
            if (g_1008b89b)
            {
                v8 = sub_1003997e(g_1008b89b);
                if (!v8 || !v8->field_90)
                    return NULL;
                v9 = sub_1003c23e(v8);
                if (!v9)
                {
                    return v9;
                }
                else if (a2)
                {
                    return sub_1003bbc1(v9, a2);
                }
                else
                {
                    return v9;
                }
                return NULL;
            }
            else
            {
                return v7;
            }
        }
        else
        {
            if (!a1)
            {
                v10 = sub_1003c23e(sub_100399af(a0));
                if (v10 && a2)
                {
                    v10 = sub_1003bbc1(v10, a2);
                    if (v10 && !v10->field_88)
                        v10 = NULL;
                }
                return v10;
            }
            else
            {
                v1 = NULL;
                v0 = 110;
                while (true)
                {
                    v11 = sub_100399af(a0);
                    if (!v11)
                        break;
                    v2 = v11;
                    v12 = sub_1003c23e(v2);
                    if (v12 && v12->field_88 && v12->field_88 < a1 && v12->field_88 < v0 && (!g_100fa97a || sub_10011678(v12->field_24, v12->field_28, 0)) && (!a2 || sub_1003bbc1(v2, a2)))
                    {
                        v1 = v2;
                        v0 = v1->field_88;
                    }
                }
                return v1;
            }
        }
    }
}
```

## `sub_1003919a` `0x1003919a`

_223 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned int field_28;
    unsigned int field_2c;
    char padding_30[96];
    char field_90;
} struct_0;

extern unsigned int g_10052768;
extern unsigned int g_1005276c;
extern char g_10052770;
extern char g_10077175;
extern char g_100f94c8;

struct_0 * sub_1003919a(unsigned int a0)
{
    struct_0 *i;  // ebx
    struct_0 *v4;  // ebx
    struct_0 *idx;  // ebx
    unsigned int v6;  // eax
    unsigned int v7;  // ebx
    unsigned int v8;  // eax
    unsigned short v9[43];  // eax
    unsigned int v10;  // edx
    unsigned int v0;  // [bp-0x14]
    struct_0 *v1;  // [bp-0xc]

    if (!g_100f94c8)
        return NULL;
    v0 = 0;
    v1 = NULL;
    for (i = 0x63fef8; i < 0x64a308; i = &v4[1].padding_0[23])
    {
        v4 = i;
        if (v4->field_90)
        {
            idx = &i->padding_0[4];
            v4 = idx;
            if (sub_1003a320(&i->padding_0[4], i))
            {
                v4 = idx;
                if (v4->field_2c == *((int *)&g_10052770))
                {
                    v6 = *((int *)&idx->padding_0[36]) - g_10052768;
                    if (*((int *)&idx->padding_0[36]) - g_10052768 < NULL)
                        v6 = ~(v6) + 1;
                    v4 = idx;
                    if (v6 <= v7)
                    {
                        v8 = idx->field_28 - g_1005276c;
                        if (idx->field_28 - g_1005276c < NULL)
                            v8 = ~(v8) + 1;
                        v4 = idx;
                        if (v8 <= v7)
                        {
                            v9 = &(&g_10077175)[156 * (unsigned long long)(struct struct_0 *)&idx[45195].padding_30[13] / 168];
                            v4 = idx;
                            if (*((int *)&v9[32]) == v4)
                            {
                                v10 = v9[41] - v9[42];
                                v4 = idx;
                                if (v10)
                                {
                                    v4 = idx;
                                    if (v10 >= a0)
                                    {
                                        v4 = idx;
                                        if (v10 > v0)
                                        {
                                            v0 = v10;
                                            v1 = idx;
                                            v4 = idx;
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
    if (!v1)
        return NULL;
    return v1;
}
```

## `sub_10039279` `0x10039279`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10039279(void)
{
    return;
}
```

## `sub_1003927b` `0x1003927b`

_191 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
    char padding_4[32];
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
    char padding_30[96];
    char field_90;
} struct_0;

typedef struct struct_1 {
    char padding_0[86];
    unsigned int field_56;
    char padding_5a[8];
    unsigned short field_62;
    unsigned short field_64;
} struct_1;

extern unsigned int g_10052768;
extern unsigned int g_1005276c;
extern char g_10052770;

int sub_1003927b(void)
{
    struct_0 *iter;  // ebx
    unsigned int v4;  // eax
    unsigned int v5;  // ebx
    unsigned int v6;  // eax
    struct_1 *v7;  // eax
    struct_1 *v8;  // eax
    unsigned int v9;  // eax
    unsigned int v10;  // edx
    unsigned int v11;  // ecx
    unsigned int v0;  // [bp-0x18]
    struct_0 *v1;  // [bp-0xc]

    v0 = 0;
    v1 = NULL;
    for (iter = 0x63fef8; iter < 0x64a308; iter = &iter[1].padding_4[19])
    {
        if (iter->field_90 && iter->field_2c == *((int *)&g_10052770))
        {
            v4 = iter->field_24 - g_10052768;
            if (iter->field_24 - g_10052768 < NULL)
                v4 = ~(v4) + 1;
            if (v4 <= v5)
            {
                v6 = iter->field_28 - g_1005276c;
                if (iter->field_28 - g_1005276c < NULL)
                    v6 = ~(v6) + 1;
                if (v6 <= v5)
                {
                    v7 = sub_1003b0f0(iter->field_0, iter);
                    iter = iter->field_0;
                    v8 = v7;
                    if (v8 && (!v9 || ((char)*((int *)&(v8->padding_0)[1]) & 2)))
                    {
                        v10 = v8->field_62 - *((short *)&v8->padding_5a[6]);
                        if (v10 && v10 >= v11 && v10 > v0)
                        {
                            v0 = v10;
                            v1 = iter;
                        }
                    }
                }
            }
        }
    }
    return;
}
```

## `sub_1003933a` `0x1003933a`

_29 bytes. calls ReadProcessMemory_

```c
extern HANDLE g_1005f612;

int sub_1003933a(void* a0)
{
    char v0;  // [bp+0x8]

    return ReadProcessMemory(g_1005f612, a0, &v0, 0x4, NULL);
}
```

## `sub_10039357` `0x10039357`

_29 bytes. calls WriteProcessMemory_

```c
extern HANDLE g_1005f612;

int sub_10039357(void* a0)
{
    char v0;  // [bp+0x8]

    return WriteProcessMemory(g_1005f612, a0, &v0, 0x4, NULL);
}
```

## `sub_10039374` `0x10039374`

_78 bytes. calls WriteProcessMemory_

```c
extern HANDLE g_1005f612;
extern UIntPtr g_1005f622;

int sub_10039374(unsigned int count)
{
    unsigned int len;  // eax
    unsigned int v0;  // [bp-0x8]

    len = lstrlen(count);
    WriteProcessMemory(g_1005f612, 0x7e07b0, count, len + 1, &g_1005f622);
    v0 = 60;
    return WriteProcessMemory(g_1005f612, 0x7e07ac, &v0, 0x4, &g_1005f622);
}
```

## `sub_100393c2` `0x100393c2`

_81 bytes. (leaf/helper — see body)_

```c
int sub_100393c2(unsigned int a0, unsigned short a1)
{
    unsigned int len;  // edx
    unsigned int v7;  // edx
    unsigned int v0;  // [bp-0x118]
    unsigned short v1;  // [bp-0x112]
    unsigned short v2;  // [bp-0x110]
    unsigned short v3;  // [bp-0x10e]
    unsigned short v4;  // [bp-0x10c]
    char v5[262];  // [bp-0x10a]

    len = lstrlen(a0);
    v1 = len + 6;
    v2 = 1942;
    v3 = a1;
    v4 = len;
    sub_1002ae6f(v5, a0, len);
    v0 = v7 + 8;
    return sub_1002ade7(&v1);
}
```

## `sub_10039413` `0x10039413`

_74 bytes. (leaf/helper — see body)_

```c
int sub_10039413(unsigned int a0)
{
    unsigned int len;  // edx
    unsigned int v6;  // edx
    unsigned int v0;  // [bp-0x118]
    unsigned short v1;  // [bp-0x112]
    unsigned short v2;  // [bp-0x110]
    unsigned short v3;  // [bp-0x10e]
    char v4[264];  // [bp-0x10c]

    len = lstrlen(a0);
    v1 = len + 4;
    v2 = 406;
    v3 = len;
    sub_1002ae6f(v4, a0, len);
    v0 = v6 + 6;
    return sub_1002ade7(&v1);
}
```

## `sub_1003945d` `0x1003945d`

_74 bytes. (leaf/helper — see body)_

```c
int sub_1003945d(unsigned int a0)
{
    unsigned int len;  // edx
    unsigned int v6;  // edx
    unsigned int v0;  // [bp-0x118]
    unsigned short v1;  // [bp-0x112]
    unsigned short v2;  // [bp-0x110]
    unsigned short v3;  // [bp-0x10e]
    char v4[264];  // [bp-0x10c]

    len = lstrlen(a0);
    v1 = len + 4;
    v2 = 1174;
    v3 = len;
    sub_1002ae6f(v4, a0, len);
    v0 = v6 + 6;
    return sub_1002ade7(&v1);
}
```

## `sub_100394a7` `0x100394a7`

_676 bytes. calls SendDlgItemMessageA_

```c
typedef struct struct_0 {
    unsigned int field_0;
    char padding_4[28];
    unsigned int field_20;
    char padding_24[8];
    unsigned int field_2c;
    void* field_30;
    unsigned int field_34;
} struct_0;

extern void* g_10052770;
extern struct_0 g_1006f8ac;
extern struct_0 g_10072f5c;
extern char g_10072f60;
extern HWND g_10072f70;
extern unsigned int g_10072fd0;
extern unsigned short g_10072fd4[4];
extern void g_101fcbd4;

void* sub_100394a7(void)
{
    unsigned int v17;  // ebx
    struct_0 *idx;  // edx
    void* count;  // eax
    struct_0 *v26;  // edx
    void* node;  // eax
    void* iter;  // eax
    unsigned int v20;  // esi
    unsigned int v21;  // edi
    unsigned int v22;  // ecx
    unsigned int len;  // eax
    struct_0 *index;  // edx
    unsigned int v0;  // [bp-0x9c]
    unsigned int v1;  // [bp-0x98]
    char *v2;  // [bp-0x94]
    struct_0 *v3;  // [bp-0x90], Other Possible Types: void*, void* *
    unsigned int v4;  // [bp-0x8c]
    struct_0 *v5;  // [bp-0x88]
    unsigned int v6;  // [bp-0x84]
    void* v7;  // [bp-0x80], Other Possible Types: unsigned int
    void* v8;  // [bp-0x7c]
    unsigned int v9;  // [bp-0x78]
    char v10;  // [bp-0x71]
    void* j;  // [bp-0x70]
    void* v12;  // [bp-0x6c], Other Possible Types: unsigned int
    WPARAM iter1;  // [bp-0x68]
    char v14;  // [bp-0x64]
    char v15;  // [bp-0x4]

    v8 = IsWindow(g_10072f70);
    if (!v8)
        return v8;
    sub_1002ae81(&g_10072f5c.field_0, 20);
    v17 = 0;
    iter1 = NULL;
    g_10072fd0 = 0;
    idx = &g_1006f8ac.field_0;
    iter = 0x63fef8;
    do
    {
        if ((char)iter[144])
        {
            g_10072f5c.field_0 = g_10072f5c.field_0 + 1;
            v7 = iter;
            v6 = v22;
            v5 = idx;
            v4 = v17;
            v3 = &v8;
            v2 = &v15;
            v1 = v20;
            v0 = v21;
            idx->field_30 = iter;
            idx->field_34 = (int)iter[140];
            len = lstrlen(iter + 4);
            if (len > g_10072fd0)
                g_10072fd0 = len;
            v17 = v4;
            iter = (unsigned int)sub_1002ae6f(index->padding_24, (unsigned int)sub_1002ae6f(idx, iter + 4, 32) + 36, 12);
            v7 = (int)iter[0x88];
            index->field_20 = (int)iter[0x88];
            v20 = index->field_2c;
            if (v20 < 0x10)
                (&g_10072f60)[v20] = 1;
            idx = index + 1;
        }
        iter += 168;
    } while (iter < 0x64a308);
    if (!v8)
        return iter;
    j = g_10052770;
    v10 = 1;
    do
    {
        count = j;
        if (*((char *)(count + &g_10072f60)))
        {
            *((char *)(count + &g_10072f60)) = 0;
            sub_1003974b(j, &v14);
            v12 = 0x60 * iter1 + (char *)&g_10072fd4[0];
            if (lstrcmp(v12, &v14))
            {
                lstrcpy(v12, &v14);
                SendDlgItemMessageA(g_10072f70, 1901, 386, iter1, NULL);
                SendDlgItemMessageA(g_10072f70, 1901, 385, iter1, v12);
            }
            iter1 = (char *)iter1 + 1;
            v26 = &g_1006f8ac.field_0;
            v9 = 0;
            while (true)
            {
                v3 = v26;
                if (v9 < g_10072f5c.field_0 && v26->field_2c == j)
                {
                    sub_100397a0(v26, &v14);
                    v12 = 0x60 * iter1 + (char *)&g_10072fd4[0];
                    if (lstrcmp(v12, &v14))
                    {
                        lstrcpy(v12, &v14);
                        SendDlgItemMessageA(g_10072f70, 1901, 386, iter1, NULL);
                        SendDlgItemMessageA(g_10072f70, 1901, 385, iter1, v12);
                        iter1 = (char *)iter1 + 1;
                    }
                    else
                    {
                        iter1 = (char *)iter1 + 1;
                    }
                }
                if (v26 >= &g_10072f5c.field_0)
                    break;
                v26 += 1;
                v9 += 1;
            }
            count = 0x60 * iter1 + (char *)&g_10072fd4[0];
            v12 = count;
            if (*((short *)count) != 32)
            {
                *((unsigned short *)count) = 32;
                SendDlgItemMessageA(g_10072f70, 1901, 386, iter1, NULL);
                count = SendDlgItemMessageA(g_10072f70, 1901, 385, iter1, v12);
                iter1 = (char *)iter1 + 1;
            }
            else
            {
                iter1 = (char *)iter1 + 1;
            }
        }
        if (v10)
        {
            v10 = 0;
            j = NULL;
        }
        else
        {
            j += 1;
        }
    } while (j < 0x10);
    if (!iter1)
        return count;
    for (node = 0x60 * iter1 + (char *)&g_10072fd4[0]; *((char *)node); node += 96)
    {
        if (node >= &g_101fcbd4)
            return node;
        *((char *)node) = 0;
        v3 = node;
        SendDlgItemMessageA(g_10072f70, 1901, 386, iter1, NULL);
    }
    return node;
}
```

## `sub_1003974b` `0x1003974b`

_85 bytes. refs "***Level ", "***"_

```c
extern unsigned int g_10052770;

int sub_1003974b(int a0, int a1)
{
    int v1;  // ebx
    char v0;  // [bp-0x44]

    lstrcpy(a1, "***Level ");
    v1 = g_10052770 - a0;
    if (!v1)
        sub_10040940(a0, &v0);
    else
        sub_10039951(v1, &v0);
    lstrcat(a1, &v0);
    return lstrcat(a1, "***");
}
```

## `sub_100397a0` `0x100397a0`

_433 bytes. refs "Pos: (", ");
    lstrcat(v1, ", "%  "_

```c
typedef struct struct_0 {
    char padding_0[32];
    int field_20;
    unsigned int field_24;
    unsigned int field_28;
    char padding_2c[4];
    struct struct_1 *field_30;
    int field_34;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern unsigned int g_10052768;
extern unsigned int g_1005276c;
extern int g_1005f7b1;
extern unsigned int g_10072fd0;

unsigned int * sub_100397a0(struct_0 *a0, char *a1)
{
    unsigned int v3;  // eax
    unsigned int i;  // ecx
    char *iter;  // edi
    struct_0 *idx;  // edx
    struct_0 *index;  // edx
    unsigned int *v8;  // eax
    unsigned int v0;  // [bp-0x6c]
    char *v1;  // [bp-0x48], Other Possible Types: struct_0 *
    char v2;  // [bp-0x44]

    v1 = a0;
    v3 = (unsigned int)sub_1002ae6f(a1, v1, lstrlen(v1));
    i = g_10072fd0 + 2 - v3;
    for (iter = &a1[v3]; i; i -= 1)
    {
        *(iter) = 32;
        iter += 1;
    }
    *(iter) = 0;
    v1 = iter;
    lstrcat(iter, "Pos: (");
    idx = a0;
    if (!lstrcmp(&g_1005f7b1, a0))
    {
        idx->field_24 = g_10052768;
        idx->field_28 = g_1005276c;
    }
    sub_10039951(idx->field_24 - g_10052768, &v2);
    lstrcat(v1, &v2);
    lstrcat(v1, ",");
    sub_10039951(g_1005276c - a0->field_28, &v2);
    lstrcat(v1, &v2);
    lstrcat(v1, ")");
    lstrcat(v1, "  Health: ");
    sub_10040940(a0->field_20, &v2);
    lstrcat(v1, &v2);
    if (a0->field_20 == 100)
    {
        lstrcat(v1, "%");
    }
    else if (a0->field_20 < 10)
    {
        lstrcat(v1, "%  ");
    }
    else
    {
        lstrcat(v1, "% ");
    }
    lstrcat(v1, "  Speed: ");
    sub_10040940(a0->field_34, &v2);
    lstrcat(v1, &v2);
    index = a0;
    if (!index->field_30)
        return index->field_30;
    v8 = index->field_30->field_0 >> 24;
    if (*((char *)&v8) == 64)
        return v8;
    v0 = index->field_34 - 218 >> 1;
    lstrcat(v1, " (");
    sub_10040940(index->field_34 - 218 >> 1, &v2);
    lstrcat(v1, &v2);
    return lstrcat(v1, ")");
}
```

## `sub_10039951` `0x10039951`

_45 bytes. (leaf/helper — see body)_

```c
int sub_10039951(int a0, char *a1)
{
    if (a0 > 2147483647)
    {
        a0 = -(a0);
        *(a1) = 45;
    }
    else
    {
        *(a1) = 43;
    }
    return sub_10040940(a0, a1 + 1);
}
```

## `sub_1003997e` `0x1003997e`

_49 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_1003997e(unsigned int *a0)
{
    unsigned int *i;  // ecx

    if (!a0)
        return a0;
    for (i = 0x63fef8; i < 0x64a308; i += 42)
    {
        if (a0 == *(i))
            return i;
    }
    return NULL;
}
```

## `sub_100399af` `0x100399af`

_65 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[144];
    char field_90;
} struct_0;

struct_0 * sub_100399af(int a0)
{
    unsigned int v0;  // ebx
    struct_0 *i;  // ebx

    if (!v0)
        i = 0x63fef8;
    for (; i < 0x64a308; i = &i[1].padding_0[23])
    {
        if (i->field_90 && !lstrcmpi(a0, &i->padding_0[4]))
            return i;
    }
    return NULL;
}
```

## `sub_100399f0` `0x100399f0`

_98 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[144];
    char field_90;
} struct_0;

int sub_100399f0(void)
{
    struct_0 *i;  // ebx
    unsigned int v10;  // ecx
    unsigned int v11;  // esi
    unsigned int v12;  // edi
    struct_0 *v15;  // ebx
    char *v0;  // [bp-0x20]
    char *v1;  // [bp-0x1c]
    struct_0 *v2;  // [bp-0x18]
    int v3;  // [bp-0x8]
    char v4;  // [bp-0x4]
    unsigned short v5;  // [bp+0x4]
    unsigned short v6;  // [bp+0x8]
    char v7;  // [bp+0xc]
    int v8;  // [bp+0x10]

    i = 0x63fef8;
    v10 = v5;
    v11 = v6;
    for (v12 = v7; i < 0x64a308; i = &v15[1].padding_0[23])
    {
        v15 = i;
        if (v15->field_90)
        {
            v15 = i;
            if (v10 == *((int *)&v15->padding_0[36]))
            {
                v15 = i;
                if (v11 == *((int *)&v15->padding_0[40]))
                {
                    v15 = i;
                    if (v12 == *((int *)&v15->padding_0[44]))
                    {
                        v2 = i;
                        v1 = &v3;
                        v0 = &v4;
                        v3 = lstrcmpi(&i->padding_0[4], v8);
                        v15 = v2;
                        if (!v3)
                            return;
                    }
                }
            }
        }
    }
    return;
}
```

## `sub_10039a52` `0x10039a52`

_103 bytes. (leaf/helper — see body)_

```c
extern char g_1005f7ed;

int sub_10039a52(void)
{
    char *v7;  // ebp
    char v8[145];  // ebx
    char v15[145];  // ebx
    char v16[145];  // ecx
    unsigned int v17;  // esi
    int v18;  // eax
    char v19[145];  // edx
    char v20[145];  // ebx
    char v9[145];  // ecx
    unsigned int v10;  // esi
    char v11[145];  // edi
    int v12;  // eax
    char v13[145];  // edx
    char v14[145];  // ecx
    char v0[145];  // [bp-0x30]
    char v1;  // [bp-0xc]
    unsigned long v2;  // [bp-0x8]
    char v3;  // [bp+0x0]
    unsigned short v4;  // [bp+0x4]
    unsigned short v5;  // [bp+0x8]
    char v6;  // [bp+0xc]

    (&v2)[1] = &v3;
    v7 = &v2 + 1;
    v8 = 0x63fef8;
    v9 = v4;
    v10 = v5;
    v11 = v6;
    while (true)
    {
        v14 = v9;
        if (v8 >= 0x64a308)
            return;
        v15 = v8;
        v16 = v14;
        v17 = v10;
        v18 = v12;
        v19 = v13;
        if (v15[144])
        {
            v15 = v8;
            v16 = v14;
            v17 = v10;
            v18 = v12;
            v19 = v13;
            if (v16 == *((int *)&v15[36]))
            {
                v15 = v8;
                v16 = v14;
                v17 = v10;
                v18 = v12;
                v19 = v13;
                if (v17 == *((int *)&v15[40]))
                {
                    v15 = v8;
                    v16 = v14;
                    v17 = v10;
                    v18 = v12;
                    v19 = v13;
                    if (v11 == *((int *)&v15[44]))
                    {
                        v0 = &v8[4];
                        *((unsigned int *)&v7[4]) = sub_1003a320(&v8[4], v11, v10, v7, &v1, v8, v13, v14, v12);
                        v20 = &v1;
                        v7 = v10;
                        v15 = v20;
                        v16 = v13;
                        v17 = v11;
                        v11 = v0;
                        v18 = v14;
                        v19 = v8;
                        if (*((int *)&v7[4]))
                        {
                            v15 = v20;
                            v16 = v13;
                            v17 = v11;
                            v11 = v0;
                            v18 = v14;
                            v19 = v8;
                            if (v15 != *((int *)&g_1005f7ed))
                                return;
                        }
                    }
                }
            }
        }
        v13 = v19;
        v12 = v18;
        v10 = v17;
        v8 = &v15[1 + 23];
        v9 = v16;
    }
}
```

## `sub_10039ab9` `0x10039ab9`

_169 bytes. (leaf/helper — see body)_

```c
int sub_10039ab9(void)
{
    char *v12;  // ebp
    char *i;  // ebx
    char *v20;  // ebx
    char *v21;  // ebx
    char *v22;  // ebx
    char *v14;  // ecx
    unsigned int v15;  // esi
    char *v16;  // edi
    unsigned int v17;  // eax
    char *v18;  // edx
    char *v19;  // ebx
    unsigned long v0;  // [bp-0x20]
    unsigned long v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x14]
    char v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned long v7;  // [bp-0x8]
    char v8;  // [bp+0x0]
    unsigned short v9;  // [bp+0x4]
    unsigned short v10;  // [bp+0x8]
    char v11;  // [bp+0xc]

    (&v7)[1] = &v8;
    v12 = &v7 + 1;
    i = 0x63fef8;
    v6 = 0;
    v14 = v9;
    v15 = v10;
    for (v16 = v11; i < 0x64a308; i = v19 + 168)
    {
        v19 = i;
        if (v19[144])
        {
            v19 = i;
            if (v14 == *((int *)&v19[36]))
            {
                v19 = i;
                if (v15 == *((int *)&v19[40]))
                {
                    v19 = i;
                    if (v16 == *((int *)&v19[44]))
                    {
                        v4 = v17;
                        v0 = _INSERT(v1, 4, v18);
                        *((unsigned int *)&v12[4]) = sub_1003a320(i + 4, v16, v15, v12, &v5, i, *((unsigned int *)((void*)&v0 + 4)), v14, v17);
                        v17 = v14;
                        v14 = *((unsigned int *)((void*)&v0 + 4));
                        v18 = i;
                        v20 = &v5;
                        v12 = v15;
                        v15 = v16;
                        v16 = i + 4;
                        v19 = v20;
                        if (!*((int *)&v12[4]))
                        {
                            v3 = v17;
                            *((unsigned int *)&v12[4]) = sub_1003a3da(v20 + 4, v16, v15, v12, &v4, v20, v18, v14, v17);
                            v17 = v14;
                            v14 = v18;
                            v18 = v20;
                            v21 = &v4;
                            v12 = v15;
                            v15 = v16;
                            v16 = v20 + 4;
                            v19 = v21;
                            if (!*((int *)&v12[4]))
                            {
                                v2 = v17;
                                *((unsigned int *)&v12[4]) = sub_1003a494(v21 + 4, v16, v15, v12, &v3, v21, v18, v14, v17);
                                v17 = v14;
                                v14 = v18;
                                v18 = v21;
                                v22 = &v3;
                                v12 = v15;
                                v15 = v16;
                                v16 = v21 + 4;
                                v19 = v22;
                                if (!*((int *)&v12[4]))
                                {
                                    *((unsigned int *)&v12[4]) = sub_1003a550(v22 + 4, v16, v15, v12, &v2, v22, v18, v14, v17);
                                    v17 = v14;
                                    v14 = v18;
                                    v18 = v22;
                                    v12 = v15;
                                    v15 = v16;
                                    v16 = v22 + 4;
                                    v19 = &v2;
                                }
                                if (*((int *)&v12[4]))
                                    return;
                                *((char **)&v12[8]) = v19;
                            }
                        }
                    }
                }
            }
        }
    }
    return;
}
```

## `sub_10039b62` `0x10039b62`

_89 bytes. refs "TibiaClient"_

```c
extern unsigned int g_10059ed0;

HWND sub_10039b62(void)
{
    unsigned int ch;  // eax
    unsigned int v0;  // [bp-0xc]
    HWND v1;  // [bp-0x8]

    if (g_10059ed0)
        return g_10059ed0;
    v1 = NULL;
    do
    {
        v1 = FindWindowExA(NULL, v1, "TibiaClient", NULL);
        GetWindowThreadProcessId(v1, &v0);
        ch = GetCurrentProcessId();
    } while (v1 && ch != v0);
    g_10059ed0 = v1;
    return v1;
}
```

## `sub_10039bbb` `0x10039bbb`

_196 bytes. calls SendMessageA; refs "TibiaClient"_

```c
extern unsigned int g_64f5c4;
extern unsigned int g_79cf28;
extern unsigned int g_79cf88;

unsigned int sub_10039bbb(void)
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
            v5 = g_79cf28;
            g_79cf28 = 8;
            v0 = 300;
            g_64f5c4 = 4849728();
            g_79cf28 = v5;
            g_79cf88 = 4294967295;
            Sleep(20);
            return SendMessageA(v2, 258, 0xd, NULL);
        }
    }
}
```

## `sub_10039bf6` `0x10039bf6`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10039bf6(void)
{
}
```

## `sub_10039c81` `0x10039c81`

_265 bytes. calls SendMessageA, VirtualProtect_

```c
extern HWND g_1005f626;
extern char g_100ee8bb;

LRESULT sub_10039c81(void)
{
    LRESULT v7;  // eax
    LRESULT v8;  // ebx
    LPARAM v9;  // ecx
    unsigned int v0;  // [bp-0x44]
    unsigned int v1;  // [bp-0x40]
    unsigned int v2;  // [bp-0x3c]
    unsigned int v3;  // [bp-0x38]
    enum PAGE_PROTECTION_FLAGS v4[8];  // [bp-0x34]
    int v5[4];  // [bp-0x14]

    v7 = sub_10039b62();
    if (!v7)
        return v8;
    v8 = v7;
    VirtualProtect(0x401000, 0x1b7000, PAGE_EXECUTE_READWRITE, v4);
    if (g_100ee8bb)
    {
        v3 = 400;
        sub_10039357(0x4cd5d7);
        v2 = 349;
        sub_10039357(0x4cd5df);
        v1 = 400;
        sub_10039357(0x4cd825);
        v0 = 349;
        sub_10039357(0x4cd82c);
        SetWindowPos(v8, 0xffffffff, 0, 0, 0, 0, 3);
        SetWindowPos(g_1005f626, 0xffffffff, 0, 0, 0, 0, 3);
    }
    else
    {
        v3 = 550;
        sub_10039357(0x4cd5d7);
        v2 = 450;
        sub_10039357(0x4cd5df);
        v1 = 550;
        sub_10039357(0x4cd825);
        v0 = 450;
        sub_10039357(0x4cd82c);
        SetWindowPos(v8, 0xfffffffe, 0, 0, 0, 0, 3);
    }
    GetClientRect(v8, v5);
    v9 = _INSERT(*((unsigned int *)((void*)v5 + 12)) * 0x10000, 0, *((unsigned short *)((void*)v5 + 8)));
    return SendMessageA(v8, 5, NULL, v9);
}
```

## `sub_10039d8a` `0x10039d8a`

_368 bytes. (leaf/helper — see body)_

```c
extern char g_1005f8a8;
extern char g_100638a8;
extern char g_100678a8;
extern char g_1006b8a8;
extern char g_1012ad5f;
extern char g_1012fd60;
extern char g_1013527b;
extern char g_1013a27c;

unsigned int sub_10039d8a(void)
{
    unsigned int iter;  // eax
    char *iter1;  // ebx
    unsigned int v4;  // ecx
    char *iter2;  // ebx
    unsigned int v6;  // ecx
    char *k;  // ebx
    unsigned int v8;  // ecx
    char *l;  // ebx
    unsigned int v10;  // ecx
    unsigned int node;  // [bp-0x8]

    sub_1002ae81(&g_1005f8a8, 0x4000);
    sub_1002ae81(&g_100638a8, 0x4000);
    sub_1002ae81(&g_100678a8, 0x4000);
    iter = sub_1002ae81(&g_1006b8a8, 0x4000);
    node = 0;
    for (iter1 = &g_1012ad5f; node < 0x200; *((char *)iter) = 0)
    {
        iter = &(&g_1005f8a8)[32 * node];
        v4 = 0;
        while (true)
        {
            if (!*(iter1))
            {
                *((char *)iter) = 0;
                goto LABEL_10039e19;
            }
            if (v4 >= 31 || *(iter1) == 13)
                break;
            *((char *)iter) = *(iter1);
            iter += 1;
            v4 += 1;
            iter1 += 1;
        }
        iter1 += 2;
        node += 1;
    }
LABEL_10039e19:
    node = 0;
    for (iter2 = &g_1012fd60; node < 0x200; *((char *)iter) = 0)
    {
        iter = &(&g_100638a8)[32 * node];
        v6 = 0;
        while (true)
        {
            if (!*(iter2))
            {
                *((char *)iter) = 0;
                goto LABEL_10039e66;
            }
            if (v6 >= 31 || *(iter2) == 13)
                break;
            *((char *)iter) = *(iter2);
            iter += 1;
            v6 += 1;
            iter2 += 1;
        }
        iter2 += 2;
        node += 1;
    }
LABEL_10039e66:
    node = 0;
    for (k = &g_1013527b; node < 0x200; *((char *)iter) = 0)
    {
        iter = &(&g_100678a8)[32 * node];
        v8 = 0;
        while (true)
        {
            if (!*(k))
            {
                *((char *)iter) = 0;
                goto LABEL_10039eb3;
            }
            if (v8 >= 31 || *(k) == 13)
                break;
            *((char *)iter) = *(k);
            iter += 1;
            v8 += 1;
            k += 1;
        }
        k += 2;
        node += 1;
    }
LABEL_10039eb3:
    node = 0;
    for (l = &g_1013a27c; node < 0x200; *((char *)iter) = 0)
    {
        iter = &(&g_1006b8a8)[32 * node];
        v10 = 0;
        while (true)
        {
            if (!*(l))
            {
                *((char *)iter) = 0;
                return iter;
            }
            if (v10 >= 31 || *(l) == 13)
                break;
            *((char *)iter) = *(l);
            iter += 1;
            v10 += 1;
            l += 1;
        }
        l += 2;
        node += 1;
    }
    return iter;
}
```

## `sub_10039df9` `0x10039df9`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10039df9(void)
{
}
```

## `sub_10039e46` `0x10039e46`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10039e46(void)
{
}
```

## `sub_10039e93` `0x10039e93`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10039e93(void)
{
}
```

## `sub_10039ee0` `0x10039ee0`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10039ee0(void)
{
}
```

## `sub_10039f02` `0x10039f02`

_101 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10039f02(unsigned int *a0, unsigned int *a1, unsigned int *a2)
{
    unsigned int v0;  // esi
    unsigned int v1;  // eax

    v0 = *((int *)0x64f600) - *(a2);
    *(a0) = *(a0) + 8 - *((int *)0x64f608) - v0;
    *(a1) = *(a1) + 6 - *((int *)0x64f604) - v0;
    v1 = (*(0x64f600) <= 7 ? 7 - *(0x64f600) : 2);
    *(a2) = v1 + v0;
    return v1 + v0;
}
```

## `sub_10039f67` `0x10039f67`

_97 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern int g_1005f85c;

unsigned int sub_10039f67(unsigned int *a0, unsigned int *a1, unsigned int *a2)
{
    unsigned int v0;  // esi
    unsigned int v1;  // eax

    v0 = g_1005f85c - *(a2);
    *(a0) = *(a0) + 8 - g_1005f854 - v0;
    *(a1) = *(a1) + 6 - g_1005f858 - v0;
    v1 = (g_1005f85c <= 7 ? 7 - g_1005f85c : 2);
    *(a2) = v1 + v0;
    return v1 + v0;
}
```

## `sub_10039fc8` `0x10039fc8`

_38 bytes. (leaf/helper — see body)_

```c
int sub_10039fc8(int a0, int a1, int a2)
{
    sub_10039f67(&/* unsupported instruction */, &/* unsupported instruction */, &/* unsupported instruction */);
    return sub_1003a176(a0, a1, a2);
}
```

## `sub_10039fee` `0x10039fee`

_81 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    char padding_c[4];
    char field_10;
    char padding_11[151];
    char field_a8;
} struct_0;

struct_0 * sub_10039fee(unsigned int a0)
{
    struct_0 *v1;  // esi
    unsigned int i;  // edi
    unsigned int j;  // ecx
    unsigned int v4;  // esi
    struct_0 *v0;  // [bp-0x8]

    v1 = *((int *)0x654118);
    if (!*((int *)0x654118))
        return NULL;
    for (i = 0; i < 0x52b00; i += 168)
    {
        v0 = v1;
        j = v1->field_0;
        for (v4 = &v1->field_4; j; j -= 1)
        {
            if (*((int *)v4) == 99 && *((int *)(v4 + 4)) == *((int *)a0))
                return v0;
            v4 += 12;
        }
        v1 = &v0->field_a8;
    }
    return NULL;
}
```

## `sub_1003a03f` `0x1003a03f`

_38 bytes. (leaf/helper — see body)_

```c
int sub_1003a03f(int a0, int a1, int a2)
{
    sub_10039f02(&/* unsupported instruction */, &/* unsupported instruction */, &/* unsupported instruction */);
    return sub_1003a176(a0, a1, a2);
}
```

## `sub_1003a065` `0x1003a065`

_147 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    int field_0;
    struct struct_0 *field_4;
    unsigned int field_8;
} struct_0;

struct_0 * sub_1003a065(int a0, int a1, int a2)
{
    struct_0 *v4;  // eax
    int v5;  // ebx
    struct_0 *idx;  // esi
    int v7;  // ecx
    int v8;  // ebx
    struct_0 *v9;  // eax
    int v10;  // ebx
    struct_0 *v11;  // esi
    int v12;  // ecx
    unsigned int v13;  // eax
    unsigned int v0;  // [bp-0x24]
    struct_0 *v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    struct_0 *v3;  // [bp-0x8]

    v4 = sub_1003a0f8(a0, a1, a2);
    if (!v4)
        return v4;
    v1 = v4;
    v3 = NULL;
    v5 = v4->field_0;
    idx = &v4->field_4;
    v7 = 0;
    while (true)
    {
        v8 = v5;
        if (v7 >= v8)
            return v3;
        v9 = idx->field_0;
        v10 = v8;
        v11 = idx;
        v12 = v7;
        if (v9 != 0x63)
        {
            v10 = v8;
            v11 = idx;
            v12 = v7;
            if (v9 != 0x184a)
            {
                v3 = v9;
                v0 = idx->field_4;
                v2 = idx->field_4;
                v13 = sub_1003c4fa(v9, idx, v8, v7);
                if (((char)v13 & 16))
                {
                    return v3;
                }
                else if (!(v13 & 0x200000))
                {
                    v10 = idx;
                    v11 = v9;
                    v12 = v8;
                    if (!((unsigned short)v13 & 0x2000))
                        return v3;
                }
                else
                {
                    return v3;
                }
            }
        }
        v7 = v12 + 1;
        idx = v11 + 1;
        v5 = v10;
    }
}
```

## `sub_1003a0f8` `0x1003a0f8`

_80 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_10052768;
extern unsigned int g_1005276c;

unsigned int sub_1003a0f8(int a0, int a1, int a2)
{
    if (a0 - g_10052768 + 8 >= 18)
    {
        return 0;
    }
    else if (a1 - g_1005276c + 6 < 14)
    {
        sub_10039f02(&/* unsupported instruction */, &/* unsupported instruction */, &/* unsupported instruction */);
        return sub_1003a176(a0, a1, a2);
    }
    else
    {
        return 0;
    }
}
```

## `sub_1003a148` `0x1003a148`

_46 bytes. (leaf/helper — see body)_

```c
int sub_1003a148(int a0, int a1, int a2)
{
    a2 = (a2 <= 7 ? 7 - a2 : 2);
    return sub_1003a176(a0, a1, a2);
}
```

## `sub_1003a176` `0x1003a176`

_52 bytes. (leaf/helper — see body)_

```c
int sub_1003a176(int a0, int a1, int a2)
{
    unsigned int *v1;  // eax
    char v0;  // [bp+0x0]

    v1 = sub_1003a1aa(a0, a1, a2, &v0);
    return (*(v1) - *((int *)0x654110)) * 168 + *((int *)0x654118);
}
```

## `sub_1003a1aa` `0x1003a1aa`

_59 bytes. (leaf/helper — see body)_

```c
int sub_1003a1aa(unsigned int a0, unsigned int a1, unsigned int a2)
{
    return *((int *)0x654134) + (*((int *)0x654128) * ((a2 - *((int *)0x654124)) * *((int *)0x65412c) + a1 - *((int *)0x654120)) + a0 - *((int *)0x65411c)) * 4;
}
```

## `sub_1003a1e5` `0x1003a1e5`

_303 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[156];
    unsigned int field_9c;
} struct_0;

extern char g_101d5e6e;
extern char g_101d5e6f;
extern char g_101d5e70;
extern char g_101d5e71;

int sub_1003a1e5(void)
{
    struct_0 *v2;  // eax
    struct_0 *v3;  // eax
    unsigned int v4;  // ebx
    struct_0 *v5;  // eax
    unsigned int v0;  // [bp-0x4]

    if (v2 >= 0x63fef8 && v2 < 0x64a308)
    {
        v3 = &v2->padding_0[4];
        if (g_101d5e6e && *((int *)&v3[1].padding_0[0]) == 2)
            return;
        if (g_101d5e6f && *((int *)&v3[1].padding_0[0]) == 2)
            return;
        if (g_101d5e70 && *((int *)&v3[1].padding_0[0]) == 1)
            return;
        if (g_101d5e71 && *((int *)&v3[1].padding_0[0]) == 1)
            return;
        sub_10023861();
        return;
    }
    v0 = v4;
    v5 = sub_100399af(v2);
    if (!v5)
        return;
    if (g_101d5e6e && *((int *)&v5[1].padding_0[0]) == 2)
        return;
    if (g_101d5e6f && *((int *)&v5[1].padding_0[0]) == 2)
        return;
    if (g_101d5e70 && *((int *)&v5[1].padding_0[0]) == 1)
        return;
    if (g_101d5e71 && *((int *)&v5[1].padding_0[0]) == 1)
        return;
    sub_10023861();
    return;
}
```

## `sub_1003a218` `0x1003a218`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003a218(void)
{
}
```

## `sub_1003a234` `0x1003a234`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003a234(void)
{
}
```

## `sub_1003a250` `0x1003a250`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003a250(void)
{
}
```

## `sub_1003a2b6` `0x1003a2b6`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003a2b6(void)
{
}
```

## `sub_1003a2d2` `0x1003a2d2`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003a2d2(void)
{
}
```

## `sub_1003a2ee` `0x1003a2ee`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003a2ee(void)
{
}
```

## `sub_1003a320` `0x1003a320`

_184 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[32];
    char field_20;
} struct_0;

extern char g_100638a8[4];

int sub_1003a320(void)
{
    void* v2;  // eax
    struct_0 *v3;  // edx
    unsigned int i;  // [bp-0x8]
    int v1;  // [bp+0x4]

    if ((char)sub_1003a1e5() == 3)
        return;
    for (i = 0; i < 0x200; i += 1)
    {
        v2 = &g_100638a8[32 * i];
        if (!*((char *)v2))
            return;
        if (*((char *)v2) == 42)
        {
            if (v3 && v3->field_20)
                v2 = lstrcmpi(&v3->field_20, v2 + 1);
        }
        else
        {
            v2 = (*((short *)v2) == 0x2b2b ? lstrcmpi(v1, v2 + 2) : (*((char *)v2) == 43 ? lstrcmpi(v1, v2 + 1) : lstrcmpi(v1, v2)));
        }
        if (!v2)
            return;
    }
    return;
}
```

## `sub_1003a3c0` `0x1003a3c0`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003a3c0(void)
{
}
```

## `sub_1003a3da` `0x1003a3da`

_184 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[32];
    char field_20;
} struct_0;

extern char g_1006b8a8[4];

int sub_1003a3da(void)
{
    void* v2;  // eax
    struct_0 *v3;  // edx
    unsigned int i;  // [bp-0x8]
    int v1;  // [bp+0x4]

    if ((char)sub_1003a1e5() == 4)
        return;
    for (i = 0; i < 0x200; i += 1)
    {
        v2 = &g_1006b8a8[32 * i];
        if (!*((char *)v2))
            return;
        if (*((char *)v2) == 42)
        {
            if (v3 && v3->field_20)
                v2 = lstrcmpi(&v3->field_20, v2 + 1);
        }
        else
        {
            v2 = (*((short *)v2) == 0x2b2b ? lstrcmpi(v1, v2 + 2) : (*((char *)v2) == 43 ? lstrcmpi(v1, v2 + 1) : lstrcmpi(v1, v2)));
        }
        if (!v2)
            return;
    }
    return;
}
```

## `sub_1003a47a` `0x1003a47a`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003a47a(void)
{
}
```

## `sub_1003a494` `0x1003a494`

_186 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[32];
    char field_20;
} struct_0;

extern char g_1005f8a8[4];

int sub_1003a494(void)
{
    void* v2;  // eax
    struct_0 *v3;  // edx
    unsigned int i;  // [bp-0x8]
    int v1;  // [bp+0x4]

    if ((char)sub_1003a1e5() == 1)
        return;
    for (i = 0; i < 0x200; i += 1)
    {
        v2 = &g_1005f8a8[32 * i];
        if (!*((char *)v2))
            return;
        if (*((char *)v2) == 42)
        {
            if (v3 && v3->field_20)
                v2 = lstrcmpi(&v3->field_20, v2 + 1);
        }
        else
        {
            v2 = (*((short *)v2) == 0x2b2b ? lstrcmpi(v1, v2 + 2) : (*((char *)v2) == 43 ? lstrcmpi(v1, v2 + 1) : lstrcmpi(v1, v2)));
        }
        if (!v2)
            return;
    }
    return;
}
```

## `sub_1003a534` `0x1003a534`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003a534(void)
{
}
```

## `sub_1003a550` `0x1003a550`

_184 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[32];
    char field_20;
} struct_0;

extern char g_100678a8[4];

int sub_1003a550(void)
{
    void* v2;  // eax
    struct_0 *v3;  // edx
    unsigned int i;  // [bp-0x8]
    int v1;  // [bp+0x4]

    if ((char)sub_1003a1e5() == 2)
        return;
    for (i = 0; i < 0x200; i += 1)
    {
        v2 = &g_100678a8[32 * i];
        if (!*((char *)v2))
            return;
        if (*((char *)v2) == 42)
        {
            if (v3 && v3->field_20)
                v2 = lstrcmpi(&v3->field_20, v2 + 1);
        }
        else
        {
            v2 = (*((short *)v2) == 0x2b2b ? lstrcmpi(v1, v2 + 2) : (*((char *)v2) == 43 ? lstrcmpi(v1, v2 + 1) : lstrcmpi(v1, v2)));
        }
        if (!v2)
            return;
    }
    return;
}
```

## `sub_1003a5f0` `0x1003a5f0`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003a5f0(void)
{
}
```

## `sub_1003a60a` `0x1003a60a`

_1103 bytes. refs "exori vis", "exori mort", "exori flam"_

```c
typedef struct struct_0 {
    unsigned int field_0;
    char field_3;
    char padding_4[32];
    unsigned short field_24;
    char padding_26[2];
    unsigned short field_28;
    char padding_2a[2];
    char field_2c;
} struct_0;

extern unsigned int g_100432af;
extern unsigned int g_100432b3;
extern unsigned int g_100432ba;
extern unsigned int g_100432be;
extern char g_100432c4;
extern void g_100432c7;
extern char g_100432c9;
extern unsigned short g_100432ca;
extern char g_100432cc;
extern unsigned int g_100432cd;
extern unsigned short g_100432ef;
extern void g_100432f4;
extern char g_100432f6;
extern unsigned short g_100432f7;
extern char g_100432f9;
extern unsigned short g_100432fa;
extern unsigned short g_100432fc;
extern char g_100432fe;
extern char g_100ee8ba;
extern char g_100fa4f0;
extern unsigned int g_63da40;
extern unsigned int g_63fe60;
extern unsigned int g_63fe64;

struct_0 * sub_1003a60a(struct_0 *a0, unsigned int a1)
{
    struct_0 *v2;  // eax
    unsigned int v3;  // edx
    char v12;  // dl
    unsigned int v4;  // ebx
    unsigned int v5;  // eax
    unsigned int v6;  // eax
    struct_0 *v7;  // eax
    unsigned int v8;  // edx
    unsigned int v9;  // ebx
    char v10;  // dl
    struct_0 *idx;  // eax
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0x8]

    while (true)
    {
        v2 = a0;
        v3 = v2->field_0;
        if (*((char *)&v2->field_0 + 3) != 64)
            g_100ee8ba = g_100ee8ba | 1;
        if (v2->field_0 == 1073741825)
            break;
        v4 = a1 & 0xffffffc0;
        if (v4 == 64)
        {
            g_100432af = v3;
            v5 = g_63da40;
            g_63da40 = g_63da40 + 1;
            g_100432b3 = v5;
            if (v3 != g_63fe64)
            {
                g_63fe64 = v3;
                g_63fe60 = 0;
                v0 = 11;
                sub_1002ade7("\t");
                break;
            }
            else
            {
                if (sub_10040a30(100) <= 95)
                    break;
                g_63fe64 = 0;
            }
        }
        else if (v4 == 128)
        {
            g_100432ba = v3;
            v6 = g_63da40;
            g_63da40 = g_63da40 + 1;
            g_100432be = v6;
            g_63fe64 = 0;
            g_63fe60 = v3;
            v0 = 11;
            sub_1002ade7("\t");
            break;
        }
    }
    v7 = a0;
    v8 = v7->field_0;
    v9 = a1 & 63;
    if (v9 == 1)
    {
        v1 = 3198;
    }
    else if (v9 == 14)
    {
        v1 = 3174;
    }
    else if (v9 == 4)
    {
        v1 = 3155;
    }
    else if (v9 == 5)
    {
        v1 = 3200;
    }
    else if (v9 == 40)
    {
        v1 = 3195;
    }
    else if (v9 == 15)
    {
        v1 = 3191;
    }
    else if (v9 == 32)
    {
        v1 = 3200;
    }
    else if (v9 == 41)
    {
        v1 = 3180;
    }
    else if (v9 == 18)
    {
        v1 = 3202;
    }
    else if (v9 == 16)
    {
        v1 = 3161;
    }
    else if (v9 == 0x11)
    {
        v1 = 3175;
    }
    else if (v9 == 3)
    {
        v1 = 3158;
    }
    else if (v9 == 2)
    {
        v1 = 3179;
    }
    else
    {
        if (v9 == 6)
            return sub_10039413("exori vis");
        if (v9 == 7)
            return sub_10039413("exori mort");
        if (v9 == 8)
            return sub_10039413("exori flam");
        if (v9 == 9)
            return sub_10039413("exori frigo");
        if (v9 == 10)
            return sub_10039413("exori tera");
        if (v9 == 12)
            return sub_10039413("exori san");
        if (v9 == 13)
            return sub_10039413("exori con");
        if (v9 == 11)
            return sub_10039413("exori hur");
        if (v9 == 19)
            return sub_10039413("exevo mas san");
        if (v9 == 20)
            return sub_10039413("exori mas");
        if (v9 == 21)
            return sub_10039413("exori gran");
        if (v9 == 22)
            return sub_10039413("exevo gran mas flam");
        if (v9 == 23)
            return sub_10039413("exevo gran mas vis");
        if (v9 == 24)
            return sub_10039413("exevo gran mas frigo");
        if (v9 == 25)
            return sub_10039413("exevo gran mas tera");
        if (v9 == 26)
            return sub_10039413("exevo vis lux");
        if (v9 == 27)
            return sub_10039413("exevo gran vis lux");
        if (v9 == 28)
            return sub_10039413("exevo flam hur");
        if (v9 == 29)
            return sub_10039413("exevo frigo hur");
        if (v9 == 30)
            return sub_10039413("exevo vis hur");
        if (v9 == 31)
            return sub_10039413("exevo tera hur");
        if (v9 != 42)
            return v7;
        v1 = 3165;
    }
    if ((v9 < 15 || v9 > 18) && v9 != 32 && v1 != 3180)
    {
        g_100432c2 = 13;
        g_100432c4 = 132;
        g_100432cd = v8;
        if (!g_100fa4f0)
            v7 = sub_1002ae92(v1, 0, NULL);
        if (!v7 && !g_100fa4f0)
            return v7;
        if (!g_100fa4f0)
        {
            g_100432c7 = *((char *)&v7);
            g_100432c9 = v10;
        }
        else
        {
            *((unsigned short *)&g_100432c7) = 0;
            g_100432c9 = 0;
        }
        g_100432ca = v1;
        g_100432cc = v10;
        v0 = 15;
        return sub_1002ade7("\r");
    }
    if (!g_100fa4f0)
        v7 = sub_1002ae92(v1, 0, NULL);
    idx = v7;
    if (!v7 && !g_100fa4f0)
        return idx;
    if (!g_100fa4f0)
    {
        g_100432f4 = *((char *)&idx);
        g_100432f6 = v12;
    }
    else
    {
        *((unsigned short *)&g_100432f4) = 0;
        g_100432f6 = 0;
    }
    g_100432f7 = v1;
    g_100432f9 = v12;
    g_100432fa = *((short *)&a0->padding_4[31]);
    *((char [2])&g_100432fc) = idx->padding_26;
    g_100432fe = idx->padding_2a[0];
    v0 = 15;
    return sub_1002ade7(&g_100432ef);
}
```

## `sub_1003a6de` `0x1003a6de`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1003a6de(void)
{
}
```

## `sub_1003a6f4` `0x1003a6f4`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1003a6f4(void)
{
}
```

## `sub_1003a70a` `0x1003a70a`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1003a70a(void)
{
}
```

