# elfbot.dll decompiled — jdrv 0x10035685..0x10038bef

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10035685` `0x10035685`

_6 bytes. (leaf/helper — see body)_

```c
void sub_10035685(void)
{
    char v1;  // [bp+0xffffe]

    v1 = 111;
}
```

## `sub_1003568b` `0x1003568b`

_6 bytes. (leaf/helper — see body)_

```c
void sub_1003568b(void)
{
    char v1;  // [bp+0xffffe]

    v1 = 112;
}
```

## `sub_10035691` `0x10035691`

_6 bytes. (leaf/helper — see body)_

```c
void sub_10035691(void)
{
    char v1;  // [bp+0xffffe]

    v1 = 113;
}
```

## `sub_10035697` `0x10035697`

_6 bytes. (leaf/helper — see body)_

```c
void sub_10035697(void)
{
    char v1;  // [bp+0xffffe]

    v1 = 114;
}
```

## `sub_100356b2` `0x100356b2`

_212 bytes. calls WriteProcessMemory_

```c
typedef struct struct_0 {
    char padding_0[80];
    unsigned int field_50;
} struct_0;

extern HANDLE g_1005f612;
extern struct_0 *g_1005f7ed;
extern unsigned int g_100ee8d0;
extern unsigned int g_100ee8d4;

struct_0 * sub_100356b2(void)
{
    unsigned int v2;  // ebx
    char v1;  // [bp+0xffffc]

    if (!g_1005f7ed)
        return g_1005f7ed;
    v2 = g_1005f7ed->field_50;
    if (v2 == 1 || v2 == 3)
    {
        if (g_100ee8d0 == 64 || g_100ee8d0 == 0xffffffe0)
        {
            g_100ee8d0 = 0;
        }
        else if (v2 == 1)
        {
            g_100ee8d0 = 64;
        }
        else
        {
            g_100ee8d0 = 0xffffffe0;
        }
    }
    else
    {
        if (g_100ee8d4 == 64 || g_100ee8d4 == 0xffffffe0)
        {
            g_100ee8d4 = 0;
        }
        else if (v2 == 2)
        {
            g_100ee8d4 = 64;
        }
        else
        {
            g_100ee8d4 = 0xffffffe0;
        }
    }
    v1 = g_100ee8d0 + 32;
    WriteProcessMemory(g_1005f612, 0x4f4693, /* unsupported instruction */ - 8, 0x1, NULL);
    v1 = g_100ee8d4 + 32;
    return WriteProcessMemory(g_1005f612, 0x4f46a3, /* unsupported instruction */ - 8, 0x1, NULL);
}
```

## `sub_10035786` `0x10035786`

_129 bytes. calls SendDlgItemMessageA; refs "off", "toggle"_

```c
extern HWND g_10072f8c;
extern char g_100f0d3b;
extern unsigned int g_100f0de0;

LRESULT sub_10035786(void)
{
    int v0;  // [bp-0xa]
    int v2;  // [bp+0x100000]

    if (!lstrcmpi(v2, "on"))
    {
        g_100f0d3b = 1;
        g_100f0de0 = GetTickCount();
    }
    if (!lstrcmpi(v2, "off"))
        g_100f0d3b = 0;
    if (!lstrcmpi(v2, "toggle"))
        g_100f0d3b = !g_100f0d3b;
    *((unsigned int *)&(&v0)[6]) = 0;
    *((unsigned int *)&(&v0)[2]) = 0;
    *((unsigned short *)&v0) = g_100f0d3b;
    return SendDlgItemMessageA(g_10072f8c, 1046, 241, *((unsigned int *)&v0), *((unsigned int *)(&v0 + 4)));
}
```

## `sub_10035807` `0x10035807`

_11 bytes. (leaf/helper — see body)_

```c
extern char g_100f0d3c;

void sub_10035807(void)
{
    g_100f0d3c = 2;
    return;
}
```

## `sub_10035812` `0x10035812`

_108 bytes. calls SendDlgItemMessageA; refs "off", "toggle"_

```c
extern HWND g_10072f94;
extern char g_100f0e42;

int sub_10035812(void)
{
    WPARAM v3;  // ebx
    WPARAM v0;  // [bp-0x4]
    int v2;  // [bp+0x100000]

    if (!lstrcmpi(v2, "on"))
        v3 = 0x1;
    if (!lstrcmpi(v2, "off"))
        v3 = NULL;
    if (!lstrcmpi(v2, "toggle"))
        v3 = !g_100f0e42;
    v0 = v3;
    SendDlgItemMessageA(g_10072f94, 1012, 241, v3, NULL);
    return sub_100163d8();
}
```

## `sub_1003587e` `0x1003587e`

_107 bytes. calls SendDlgItemMessageA; refs "off", "toggle"_

```c
extern HWND g_10072f94;
extern char g_10207f35;

LRESULT sub_1003587e(void)
{
    WPARAM v2;  // ebx
    int v1;  // [bp+0x100000]

    if (!lstrcmpi(v1, "on"))
        v2 = 0x1;
    if (!lstrcmpi(v1, "off"))
        v2 = NULL;
    if (!lstrcmpi(v1, "toggle"))
        v2 = !g_10207f35;
    g_10207f35 = *((char *)&v2);
    return SendDlgItemMessageA(g_10072f94, 1037, 241, v2, NULL);
}
```

## `sub_100358e9` `0x100358e9`

_233 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
} struct_0;

extern struct_0 *g_100f49d1;

int sub_100358e9(void)
{
    unsigned int v4;  // eax
    char iter[2];  // esi
    char v6;  // dl
    char v7;  // cl
    char *i;  // ebx
    char *v9;  // edi
    char *v0;  // [bp-0x4]
    char v3;  // [bp+0xff814]

    sub_10030326();
    v4 = (unsigned int)sub_10030225();
    iter = /* unsupported instruction */ - 0x1000;
    v6 = 0;
    while (true)
    {
        v7 = iter[0];
        if (iter[0])
        {
            if (v7 == 46)
            {
                if (iter[1] != 46)
                    break;
                v6 |= 2;
                iter = &iter[1];
            }
            else
            {
                if (v7 < 48 || v7 > 57)
                    break;
            }
            v6 |= 1;
            iter = &iter[1];
        }
        else if (v6 == 3)
        {
            v4 = sub_10040940(sub_100300ce(), /* unsupported instruction */ - 0x1000);
            break;
        }
    }
    if (v3 != 36)
        return v4;
    i = &g_100f49d1->field_0;
    for (v9 = &g_100f49d1[0x40000].field_0; i < v9; i += 0x200)
    {
        if (!*(i))
        {
            lstrcpyn(i, /* unsupported instruction */ - 2031, 32);
            return lstrcpyn(i + 32, /* unsupported instruction */ - 0x1000, 0x200);
        }
        v0 = v9;
        v4 = lstrcmpi(i, /* unsupported instruction */ - 2031);
        if (!v4)
            return lstrcpyn(i + 32, /* unsupported instruction */ - 0x1000, 0x200);
    }
    return v4;
}
```

## `sub_10035923` `0x10035923`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10035923(void)
{
}
```

## `sub_10035937` `0x10035937`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10035937(void)
{
}
```

## `sub_100359a0` `0x100359a0`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100359a0(void)
{
}
```

## `sub_100359d8` `0x100359d8`

_106 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
    char padding_1[31];
    char field_20;
    char padding_21[479];
    char field_200;
} struct_0;

extern struct_0 *g_100f49d1;

int sub_100359d8(void)
{
    int v3;  // eax
    char iter[513];  // ebx
    char v5[513];  // edi
    int dst;  // eax
    char v0[513];  // [bp-0x4]
    char v2;  // [bp+0xff814]

    v3 = sub_10030326();
    if (v2 != 36)
        return v3;
    iter = g_100f49d1;
    for (v5 = g_100f49d1[0x1ff].padding_1; iter < v5; iter = &iter[0x200])
    {
        if (!iter[0])
        {
            dst = lstrcpy(iter, /* unsupported instruction */ - 2031);
            iter[32] = 0;
            return dst;
        }
        v0 = v5;
        v3 = lstrcmpi(iter, /* unsupported instruction */ - 2031);
        if (!v3)
        {
            iter[32] = 0;
            return v3;
        }
    }
    return v3;
}
```

## `sub_10035a1f` `0x10035a1f`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10035a1f(void)
{
}
```

## `sub_10035a44` `0x10035a44`

_132 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
    char padding_1[31];
    unsigned short field_20;
    char padding_22[478];
    char field_200;
} struct_0;

extern struct_0 *g_100f49d1;

int sub_10035a44(void)
{
    int v4;  // eax
    struct_0 *iter;  // ebx
    struct_0 *v6;  // edi
    int dst;  // eax
    unsigned int v0;  // [bp-0x8]
    struct_0 *v1;  // [bp-0x4]
    char v3;  // [bp+0xff814]

    v4 = sub_10030326();
    if (v3 != 36)
        return v4;
    iter = g_100f49d1;
    for (v6 = g_100f49d1[0x1ff].padding_1; iter < v6; iter = &iter->field_200)
    {
        if (!iter->field_0)
        {
            dst = lstrcpy(iter, /* unsupported instruction */ - 2031);
            iter->field_20 = 49;
            return dst;
        }
        v1 = v6;
        v4 = lstrcmpi(iter, /* unsupported instruction */ - 2031);
        if (!v4)
        {
            v0 = sub_10040900(&iter->field_20) + 1;
            return wsprintfA(&iter->field_20, "%d");
        }
    }
    return v4;
}
```

## `sub_10035aa3` `0x10035aa3`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10035aa3(void)
{
}
```

## `sub_10035aca` `0x10035aca`

_111 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
} struct_0;

extern struct_0 *g_100f49d1;

int sub_10035aca(void)
{
    int v4;  // eax
    char *i;  // ebx
    char *v6;  // edi
    unsigned int v0;  // [bp-0x8]
    char *v1;  // [bp-0x4]
    char v3;  // [bp+0xff814]

    v4 = sub_10030326();
    if (v3 != 36)
        return v4;
    i = &g_100f49d1->field_0;
    for (v6 = &g_100f49d1[0x40000].field_0; i < v6; i += 0x200)
    {
        if (!*(i))
            return v4;
        v1 = v6;
        v4 = lstrcmpi(i, /* unsupported instruction */ - 2031);
        if (!v4)
        {
            v0 = sub_10040900(i + 32) - 1;
            return wsprintfA(i + 32, "%d");
        }
    }
    return v4;
}
```

## `sub_10035b29` `0x10035b29`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10035b29(void)
{
}
```

## `sub_10035b3b` `0x10035b3b`

_58 bytes. (leaf/helper — see body)_

```c
void sub_10035b3b(void)
{
    sub_10030225();
    sub_10030225();
    sub_10036bb2(sub_10036bb2());
    sub_10036e69();
    return;
}
```

## `sub_10035b75` `0x10035b75`

_160 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_10043377;
extern char g_1004337c;
extern unsigned short g_1004337f;
extern char g_10043381;
extern char g_10043384;
extern char g_10043386;
extern char g_10043387;

int sub_10035b75(void)
{
    int v4;  // eax
    int v5;  // ebx
    int v6;  // eax
    unsigned int v7[2];  // edx
    char v8;  // cl
    char v9;  // bl
    unsigned int v0;  // [bp-0x4]
    unsigned int v2;  // [bp+0xffffc]
    int v3;  // [bp+0x100000]

    sub_10030225();
    v4 = sub_10036bb2(v3);
    v2 = v4 * 12 + 6605964;
    sub_10030225();
    sub_10036daf(v4);
    v5 = v4;
    v6 = sub_10036c87();
    if (!v6)
        return v6;
    v7 = v5 * 12 + 6605964;
    if (!v7[0])
        return v6;
    g_1004337c = v5;
    g_1004337f = v7[0];
    g_10043384 = v6;
    g_10043386 = v8;
    g_10043381 = 0;
    v9 = v7[1];
    if (!v7[1])
        v9 = (char)v7[1] + 1;
    g_10043387 = v9;
    v0 = 0x11;
    return sub_1002ade7(&g_10043377);
}
```

## `sub_10035c15` `0x10035c15`

_18 bytes. (leaf/helper — see body)_

```c
void sub_10035c15(void)
{
    sub_10030225();
    return;
}
```

## `sub_10035c27` `0x10035c27`

_39 bytes. (leaf/helper — see body)_

```c
int sub_10035c27(void)
{
    unsigned int v0;  // [bp-0x4]

    v0 = sub_100300ce();
    sub_10030225();
    return sub_10036eb6();
}
```

## `sub_10035c4e` `0x10035c4e`

_4 bytes. (leaf/helper — see body)_

```c
void sub_10035c4e(void)
{
    return;
}
```

## `sub_10036bae` `0x10036bae`

_4 bytes. (leaf/helper — see body)_

```c
void sub_10036bae(void)
{
    return;
}
```

## `sub_10036bb2` `0x10036bb2`

_213 bytes. refs "helmet", "amulet", "backpack"_

```c
unsigned int sub_10036bb2(void)
{
    int v1;  // ebx

    if (!lstrcmpi(v1, "helmet"))
    {
        return 1;
    }
    else if (!lstrcmpi(v1, "amulet"))
    {
        return 2;
    }
    else if (!lstrcmpi(v1, "backpack"))
    {
        return 3;
    }
    else if (!lstrcmpi(v1, "chest"))
    {
        return 4;
    }
    else if (!lstrcmpi(v1, "lhand"))
    {
        return 5;
    }
    else if (!lstrcmpi(v1, "rhand"))
    {
        return 6;
    }
    else if (!lstrcmpi(v1, "legs"))
    {
        return 7;
    }
    else if (!lstrcmpi(v1, "boots"))
    {
        return 8;
    }
    else if (!lstrcmpi(v1, "ring"))
    {
        return 9;
    }
    else if (!lstrcmpi(v1, "belt"))
    {
        return 10;
    }
    else
    {
        return 0;
    }
}
```

## `sub_10036c87` `0x10036c87`

_290 bytes. (leaf/helper — see body)_

```c
int sub_10036c87(void)
{
    unsigned int v4;  // eax
    unsigned int v5[17];  // ebx
    unsigned int v6[17];  // ecx
    unsigned int v7[17];  // esi
    unsigned int v8[17];  // edx
    unsigned int v9[17];  // ebx
    unsigned int v10[17];  // ebx
    unsigned int v11[17];  // edx
    unsigned int v12[17];  // esi
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0x8]

    if (v4 == 4294967294)
        return;
    v1 = v4;
    v0 = 0;
    if (v4 < 16)
    {
        v0 = 1;
        v2 = v4;
        v1 = 4294967295;
    }
    else if (v4 == 98)
    {
        v2 = 1;
        v1 = 4294967295;
    }
    else if (v4 == 99)
    {
        v2 = 0;
        v1 = 4294967295;
    }
    else if (v4)
    {
        v2 = 0;
        goto LABEL_10036d9c;
    }
    else
    {
        return;
    }
    while (true)
    {
        v5 = v2 * 492 + 6606096;
        if (v5[0] && (v5[1] == v1 || v1 == 4294967295))
        {
            if (v6)
            {
                v7 = &v5[15];
                v8 = NULL;
                while (true)
                {
                    v9 = v5;
                    if (v8 >= v9[14])
                        break;
                    v10 = v9;
                    v11 = v8;
                    v12 = v7;
                    if (v12[0] == v6)
                    {
                        v10 = v9;
                        v11 = v8;
                        v12 = v7;
                        if (v12[1])
                        {
                            v10 = v9;
                            v11 = v8;
                            v12 = v7;
                            if (v12[1] < 100)
                            {
                                v10 = v6;
                                v11 = v7;
                                v12 = v9;
                                if (sub_1003c52a(v10, v12, v11, v8))
                                    return;
                            }
                        }
                    }
                    v8 = (char *)&v11[0] + 1;
                    v7 = &v12[3];
                    v5 = v10;
                }
                if (v9[14] != v9[12])
                    return;
            }
            else if (v5[14] < v5[12])
            {
                return;
            }
        }
        if (v0)
            return;
        v2 += 1;
LABEL_10036d9c:
        if (v2 >= 16)
            return;
    }
}
```

## `sub_10036cbb` `0x10036cbb`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10036cbb(void)
{
}
```

## `sub_10036cd2` `0x10036cd2`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10036cd2(void)
{
}
```

## `sub_10036d7d` `0x10036d7d`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10036d7d(void)
{
}
```

## `sub_10036daf` `0x10036daf`

_179 bytes. refs "empty", "empty1"_

```c
unsigned int sub_10036daf(void)
{
    char *i;  // ebx
    unsigned int v0;  // [bp-0x8c]
    char v1;  // [bp-0x88]
    unsigned int j;  // [bp-0x8]

    for (; *(i) == 32; i += 1);
    if (*(i) >= 48 && *(i) <= 57)
        return sub_10040900(i);
    if (!lstrcmpi(i, "empty"))
    {
        return 99;
    }
    else if (!lstrcmpi(i, "empty1"))
    {
        return 98;
    }
    else if (!lstrcmpi(i, "dp"))
    {
        return 4294967295;
    }
    else
    {
        sub_10030225();
        for (j = 0; j < 16; j += 1)
        {
            v0 = j * 492 + 6606096;
            if (!lstrcmpi(&v1, j * 492 + 6606112))
                return *((int *)(j * 492 + 6606100));
        }
        return 4294967294;
    }
}
```

## `sub_10036dd2` `0x10036dd2`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10036dd2(void)
{
}
```

## `sub_10036e19` `0x10036e19`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10036e19(void)
{
}
```

## `sub_10036e69` `0x10036e69`

_77 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_10043366;
extern char g_1004336b;
extern unsigned short g_1004336e;
extern char g_10043373;
extern char g_10043376;

int sub_10036e69(void)
{
    unsigned int v2;  // eax
    unsigned int v3;  // ebx
    unsigned int v4[2];  // ebx
    char v5;  // cl
    unsigned int v0;  // [bp-0x4]

    if (*((int *)(v2 * 12 + 6605964)))
        return;
    g_10043373 = v2;
    g_1004336b = v3;
    v4 = v3 * 12 + 6605964;
    if (!v4[0])
        return;
    g_1004336e = v4[0];
    v5 = v4[1];
    if (!v4[1])
        v5 = (char)v4[1] + 1;
    g_10043376 = v5;
    v0 = 0x11;
    sub_1002ade7(&g_10043366);
    return;
}
```

## `sub_10036eb6` `0x10036eb6`

_586 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_10043388;
extern char g_1004338d;
extern char g_1004338f;
extern unsigned short g_10043390;
extern char g_10043392;
extern unsigned short g_10043454;
extern unsigned short g_1004345c;
extern char g_10043461;
extern char g_10043463;
extern unsigned int g_1005f7d5;
extern unsigned int g_100f0e18;
extern char g_100f0e42;
extern unsigned int g_102e2604;
extern unsigned int g_102e2608;

int sub_10036eb6(void)
{
    unsigned int v2;  // ebx
    unsigned int v3;  // eax
    char v4;  // dl
    int v5;  // eax
    unsigned int v6;  // ecx
    unsigned int v0;  // [bp-0x18]

    while (true)
    {
        if (g_1005f7d5 >= v2)
        {
            if (g_102e2604 < 2 && !sub_1002ae92(3147, 0, NULL))
                return;
            if (!g_102e2604)
            {
                if (!*((int *)0x64ccd4))
                {
                    g_102e2604 = 2;
                }
                else if (*((int *)0x64ccd4) == 3147)
                {
                    g_102e2604 = 3;
                }
                else if (*((int *)0x64ccd4) && !*((int *)0x64cd04))
                {
                    sub_10036e69();
                }
            }
            else
            {
                if (g_102e2604 == 2)
                {
                    if (*((int *)0x64ccd4) == 3147)
                    {
                        g_102e2604 = 3;
                    }
                    else
                    {
                        v3 = sub_1002ae92(3147, 0, NULL);
                        if (v3)
                        {
                            g_1004338f = v4;
                            g_10043392 = v4;
                            g_10043390 = 3147;
                            g_1004338d = v3;
                            g_102e2608 = v3;
                            v0 = 0x11;
                            sub_1002ade7(&g_10043388);
                        }
                    }
                }
                else
                {
                    if (g_102e2604 == 3)
                    {
                        if (*((int *)0x64ccd4) == 3147)
                        {
                            sub_10039413(v5);
                        }
                        else if (!*((int *)0x64ccd4))
                        {
                            g_102e2604 = 2;
                        }
                        else
                        {
                            g_102e2604 = 5;
                        }
                        if (v6 != 4294967295)
                        {
                            return;
                        }
                        else if (g_100f0e42)
                        {
                            Sleep(350);
                            g_100f0e18 = 0;
                            continue;
                        }
                        else
                        {
                            return;
                        }
                    }
                }
            }
        }
        if (g_102e2604 == 3)
        {
            if (*((int *)0x64ccd4) != 3147)
            {
                if (!*((int *)0x64ccd4))
                    g_102e2604 = 2;
                else
                    g_102e2604 = 5;
            }
        }
        else
        {
            if (g_102e2604 == 5)
            {
                if (!*((int *)0x64ccd4))
                {
                    g_102e2604 = 7;
                }
                else if (*((int *)0x64ccd4) != 3147)
                {
                    g_1004345c = *((int *)0x64ccd4);
                    g_10043461 = g_102e2608;
                    g_10043463 = *((int *)((g_102e2608 - 64) * 492 + 6606152));
                    v0 = 0x11;
                    sub_1002ade7(&g_10043454);
                }
            }
            else
            {
                if (g_102e2604 == 7)
                {
                    if (*((int *)0x64cd04))
                    {
                        sub_10036e69();
                    }
                    else
                    {
                        g_102e2604 = 0;
                        return;
                    }
                }
            }
        }
        if (v6 != 4294967295)
        {
            return;
        }
        else if (g_100f0e42)
        {
            Sleep(350);
            g_100f0e18 = 0;
        }
        else
        {
            return;
        }
    }
}
```

## `sub_10037100` `0x10037100`

_251 bytes. (leaf/helper — see body)_

```c
extern char g_100434d7;
extern char g_100434d9;
extern unsigned short g_100434da;
extern char g_100434dc;
extern char g_100434dd;

int sub_10037100(void)
{
    char *v4;  // ebx
    char *v5;  // ebx
    char *v14;  // ecx
    char *v15;  // edi
    char *v16;  // esi
    char *v17;  // ecx
    char *v18;  // ecx
    char *v19;  // esi
    char *v20;  // edi
    unsigned int v21;  // edx
    char *v6;  // ebx
    unsigned int v7;  // eax
    unsigned int v8;  // eax
    char *v9;  // ecx
    char *v10;  // esi
    char *v11;  // edi
    char *v12;  // edi
    char *v13;  // edx
    unsigned int v0;  // [bp-0x24]
    unsigned int iter;  // [bp-0x14]
    char *v2;  // [bp-0x10]

    v5 = v4;
    if (!v4)
        v5 += 1;
    v2 = v5;
    iter = 0;
    while (iter < 16)
    {
        v6 = iter * 492 + 6606096;
        v7 = *((int *)&v6[4]);
        if (*((int *)&v6))
        {
            if (iter != v8 && v7 != v8)
            {
                if (v8 != 4294967295)
                {
                    iter += 1;
                    continue;
                }
                else if (v7 < 3497)
                {
                    iter += 1;
                    continue;
                }
                else if (v7 > 3500)
                {
                    iter += 1;
                    continue;
                }
            }
            v9 = NULL;
            v10 = v6 + 60;
            v11 = v2;
            while (true)
            {
                v12 = v11;
                if (v9 >= *((int *)&v6[56]))
                {
                    iter += 1;
                    break;
                }
                v13 = *((int *)&v10);
                if (!v14)
                {
                    v15 = v13;
                    v16 = v12;
                    v17 = v10;
                    v18 = v17;
                    v19 = v16;
                    v20 = v15;
                    if (((char)sub_1003c4fa(v13, v12, v10, v9) & 16))
                    {
                        v13 = *((int *)&v16);
                        v18 = v17;
                        v19 = v16;
                        v20 = v15;
                        goto LABEL_1003719b;
                    }
                }
                else
                {
                    v18 = v9;
                    v19 = v10;
                    v20 = v12;
                    if (v13 == v14)
                    {
LABEL_1003719b:
                        v20 += 1;
                        if (!v20)
                        {
                            g_100434dd = iter;
                            g_100434d7 = g_100434dd + 64;
                            g_100434d9 = *((char *)&v18);
                            g_100434dc = *((char *)&v18);
                            g_100434da = *((unsigned short *)&v13);
                            if (v21)
                            {
                                g_100434dd = sub_10038d20(v13);
                                v0 = 12;
                                sub_1002ade7("\n");
                            }
                            else
                            {
                                v0 = 12;
                                sub_1002ade7("\n");
                            }
                            return;
                        }
                    }
                }
                v10 = v19 + 12;
                v9 = v18 + 1;
                v11 = v20;
            }
        }
        else
        {
            iter += 1;
        }
    }
    return;
}
```

## `sub_10037194` `0x10037194`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10037194(void)
{
}
```

## `sub_100371fd` `0x100371fd`

_391 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[48];
    unsigned int field_30;
} struct_0;

extern unsigned short g_10043465;
extern char g_1004346a;
extern char g_1004346c;
extern unsigned short g_1004346d;
extern char g_1004346f;
extern char g_10043472;
extern char g_10043474;
extern char g_10043475;

int sub_100371fd(void)
{
    unsigned int v5[17];  // ebx
    unsigned int v6;  // eax
    unsigned int v15;  // eax
    unsigned int v16;  // ecx
    unsigned int v7;  // eax
    unsigned int j;  // ecx
    unsigned int iter[17];  // esi
    unsigned int v10;  // ebx
    struct_0 *idx;  // ebx
    unsigned int v12;  // eax
    unsigned int l;  // edi
    struct_0 *v14;  // esi
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x18]
    unsigned int node;  // [bp-0x14]
    unsigned int iter1;  // [bp-0x10]

    iter1 = 0;
    while (iter1 < 16)
    {
        v5 = iter1 * 492 + 6606096;
        v6 = v5[1];
        if (!v5[0])
        {
            iter1 += 1;
        }
        else if (iter1 == v7)
        {
            iter1 += 1;
        }
        else if (v6 == v7)
        {
            iter1 += 1;
        }
        else if (v7 != 4294967295 || v6 < 3497 || v6 > 3500)
        {
            j = 0;
            for (iter = &v5[15]; j < v5[14]; j += 1)
            {
                if (iter[0] == v10)
                {
                    v0 = iter[1];
                    v1 = v0;
                    node = 0;
                    while (node < 16)
                    {
                        idx = node * 492 + 6606096;
                        v12 = *((int *)&idx->padding_0[4]);
                        if (*((int *)&idx->padding_0[0]))
                        {
                            if (node != v7 && v12 != v7)
                            {
                                if (v7 != 4294967295)
                                {
                                    node += 1;
                                    continue;
                                }
                                else if (v12 < 3497)
                                {
                                    node += 1;
                                    continue;
                                }
                                else if (v12 > 3500)
                                {
                                    node += 1;
                                    continue;
                                }
                            }
                            l = 0;
                            for (v14 = &idx[1].padding_0[8]; l < *((int *)&idx[1].padding_0[4]); l += 1)
                            {
                                if (*((int *)&v14->padding_0[0]) == v10 && *((int *)&v14->padding_0[4]) && *((int *)&v14->padding_0[4]) < 100)
                                    goto LABEL_100372e6;
                                v14 = &v14->padding_0[12];
                            }
                            if (*((int *)&idx[1].padding_0[4]) < idx->field_30)
                            {
                                l = idx->field_30 - 1;
LABEL_100372e6:
                                g_1004346a = iter1 + 64;
                                g_1004346c = j;
                                g_1004346f = j;
                                v15 = v1;
                                if (v16 && v16 < v15)
                                    v15 = v16;
                                g_10043475 = v15;
                                g_1004346d = v10;
                                g_10043472 = node + 64;
                                g_10043474 = l;
                                v0 = 0x11;
                                sub_1002ade7(&g_10043465);
                                return;
                            }
                            node += 1;
                        }
                        else
                        {
                            node += 1;
                        }
                    }
                    return;
                }
                iter = &iter[3];
            }
            iter1 += 1;
        }
        else
        {
            iter1 += 1;
        }
    }
    return;
}
```

## `sub_10037384` `0x10037384`

_310 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[60];
    unsigned int field_3c;
} struct_0;

extern unsigned short g_10043465;
extern char g_1004346a;
extern char g_1004346c;
extern unsigned short g_1004346d;
extern char g_1004346f;
extern char g_10043472;
extern char g_10043474;
extern char g_10043475;

int sub_10037384(void)
{
    unsigned int v6[17];  // ebx
    unsigned int j;  // ecx
    unsigned int v16;  // edx
    unsigned int node[17];  // esi
    unsigned int v9;  // eax
    struct_0 *v10;  // ebx
    unsigned int v11;  // eax
    unsigned int v12;  // ebx
    unsigned int l;  // edi
    struct_0 *v14;  // esi
    unsigned int v15;  // ecx
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x18]
    unsigned int iter;  // [bp-0x14]
    unsigned int iter1;  // [bp-0x10]

    v1 = 0;
    iter1 = 0;
    while (iter1 < 16)
    {
        v6 = iter1 * 492 + 6606096;
        if (v6[0])
        {
            j = 0;
            for (node = &v6[15]; j < v6[14]; j += 1)
            {
                if (node[0] == v9)
                {
                    v0 = node[1];
                    v2 = v0;
                    iter = 0;
                    while (iter < 16)
                    {
                        v10 = iter * 492 + 6606096;
                        v11 = *((int *)&v10->padding_0[4]);
                        if (*((int *)&v10->padding_0[0]))
                        {
                            if (v11 != v12)
                            {
                                if (v12 != 4294967295)
                                {
                                    iter += 1;
                                    continue;
                                }
                                else if (v11 < 3497)
                                {
                                    iter += 1;
                                    continue;
                                }
                                else if (v11 > 3500)
                                {
                                    iter += 1;
                                    continue;
                                }
                            }
                            l = 0;
                            for (v14 = &v10->field_3c; l < *((int *)&v10->padding_0[56]); l += 1)
                            {
                                if (*((int *)&v14->padding_0[0]) == v15)
                                {
                                    if (v1 != v16)
                                    {
                                        v1 += 1;
                                    }
                                    else
                                    {
                                        g_1004346a = iter1 + 64;
                                        g_1004346c = j;
                                        g_1004346f = j;
                                        g_10043475 = v2;
                                        g_1004346d = v9;
                                        g_10043472 = iter + 64;
                                        g_10043474 = l;
                                        v0 = 0x11;
                                        sub_1002ade7(&g_10043465);
                                        return;
                                    }
                                }
                                v14 = &v14->padding_0[12];
                            }
                            iter += 1;
                        }
                        else
                        {
                            iter += 1;
                        }
                    }
                    return;
                }
                node = &node[3];
            }
            iter1 += 1;
        }
        else
        {
            iter1 += 1;
        }
    }
    return;
}
```

## `sub_100374ba` `0x100374ba`

_287 bytes. (leaf/helper — see body)_

```c
extern char g_10052784;
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern void g_1005f85c;

int sub_100374ba(void)
{
    unsigned int *v11;  // ebx
    unsigned int v12;  // eax
    unsigned int v13;  // eax
    unsigned int v14;  // edx
    unsigned int v15;  // eax
    unsigned int *v0;  // [bp-0x44], Other Possible Types: int
    unsigned int *v1;  // [bp-0x28]
    unsigned int v2;  // [bp-0x24]
    unsigned int *v3;  // [bp-0x20]
    unsigned int v4;  // [bp-0x20]
    int v5;  // [bp-0x1c]
    int v6;  // [bp-0x14]
    unsigned int *v7;  // [bp-0x10]
    unsigned int i;  // [bp-0xc]
    unsigned int iter;  // [bp-0x8]

    v2 = 4294967295;
    sub_10013f16();
    i = 0;
    while (i < 14)
    {
        v11 = g_1005f858 - 6 + i;
        v7 = v11;
        iter = 0;
        while (true)
        {
            if (iter < 18)
            {
                v6 = g_1005f854 - 8 + iter;
                v12 = sub_1003a065(v6, v7, *((int *)&g_1005f85c));
                if (v12)
                {
                    if (v12 != v13)
                    {
                        if (v13 != 4294967295)
                        {
                            iter += 1;
                            continue;
                        }
                        else if (v12 < 3497)
                        {
                            iter += 1;
                            continue;
                        }
                        else if (v12 > 3500)
                        {
                            iter += 1;
                            continue;
                        }
                        else if (*(v11) != 3)
                        {
                            iter += 1;
                            continue;
                        }
                    }
                    g_10052784 = 1;
                    if (!sub_1000d9b8(iter, i, 0))
                    {
                        iter += 1;
                    }
                    else if (v14 < v2)
                    {
                        v0 = v6;
                        v5 = v6;
                        v0 = v7;
                        v3 = v7;
                        v2 = v14;
                        v1 = v11;
                        v11 = 1 + (char *)v3 - g_1005f858;
                        if (v5 - g_1005f854 + 1 <= 2)
                        {
                            if (v11 <= 2)
                                return;
                            iter += 1;
                        }
                        else
                        {
                            iter += 1;
                        }
                    }
                    else
                    {
                        iter += 1;
                    }
                }
                else
                {
                    iter += 1;
                }
            }
            else
            {
                i += 1;
                break;
            }
        }
    }
    if (!v2)
    {
        return;
    }
    else if (v2 != 4294967295)
    {
        v15 = sub_10037973();
        sub_100147eb(v15, v4, *((int *)&g_1005f85c));
        return;
    }
    else
    {
        return;
    }
}
```

## `sub_100375d9` `0x100375d9`

_187 bytes. (leaf/helper — see body)_

```c
extern char g_10052784;
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;

unsigned int sub_100375d9(void)
{
    unsigned int idx[11];  // esi
    unsigned int v3;  // eax
    unsigned int v4;  // ebx
    unsigned int v5;  // eax
    unsigned int v6;  // ecx
    unsigned int v0[11];  // [bp-0x4]

    v0 = idx;
    sub_10013f16();
    v3 = idx[9] - g_1005f854 + 8;
    v4 = idx[10] - g_1005f858 + 6;
    if (v3 >= 7 && v3 <= 9 && v4 >= 5 && v4 <= 7)
        return v3;
    g_10052784 = 1;
    v5 = sub_1000d9b8(v3, v4, 0);
    if (!v5)
        return v5;
    v6 = g_1005f858;
    if (v5 == 1)
    {
        v6 = 3;
    }
    else if (v5 == 2)
    {
        v6 = 4;
    }
    else if (v5 == 3)
    {
        v6 = 1;
    }
    else if (v5 == 4)
    {
        v6 = 2;
    }
    else if (v5 == 5)
    {
        v6 = 7;
    }
    else if (v5 == 6)
    {
        v6 = 8;
    }
    else if (v5 == 7)
    {
        v6 = 5;
    }
    else if (v5 == 8)
    {
        v6 = 6;
    }
    return sub_10014825(v6);
}
```

## `sub_10037694` `0x10037694`

_309 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern void g_1005f85c;
extern char g_100fa97a;

int sub_10037694(void)
{
    struct_0 *v18;  // eax
    unsigned int v19;  // ecx
    unsigned int v20;  // ecx
    unsigned int v0;  // [bp-0x64]
    unsigned int node;  // [bp-0x38]
    unsigned short v2;  // [bp-0x34]
    char v3;  // [bp-0x32]
    unsigned short v4;  // [bp-0x31]
    unsigned int v5;  // [bp-0x2f]
    unsigned short v6;  // [bp-0x2c]
    char v7;  // [bp-0x2a]
    unsigned short v8;  // [bp-0x29]
    unsigned short v9;  // [bp-0x27]
    char v10;  // [bp-0x25]
    unsigned short v11;  // [bp-0x24]
    char v12;  // [bp-0x22]
    int v13;  // [bp-0x14]
    int v14;  // [bp-0x10]
    unsigned int i;  // [bp-0xc]
    unsigned int iter;  // [bp-0x8]

    for (i = 0; i < 14; i += 1)
    {
        v14 = i - 6 + g_1005f858;
        iter = 0;
        while (true)
        {
            if (iter >= 18)
                break;
            v13 = iter - 8 + g_1005f854;
            if (!sub_1003c2e3(v13, v14, *((int *)&g_1005f85c)))
            {
                iter += 1;
            }
            else if (g_100fa97a && !sub_10011678(v13, v14, 0))
            {
                iter += 1;
            }
            else
            {
                v18 = sub_1003a0f8(v13, v14, *((int *)&g_1005f85c));
                if (v18)
                {
                    v19 = v18->field_4;
                    if (v19 >= 4597 && v19 <= 0x1200 && !v20 || v19 == v20)
                    {
                        if (!node)
                        {
                            v11 = v19;
                            v12 = 0;
                            if (v20)
                                v12 = 1;
                            v2 = 0x11;
                            v3 = 131;
                            v4 = 65535;
                            v5 = 0;
                            v6 = 3483;
                            v7 = 0;
                            v8 = v13;
                            v9 = v14;
                            v10 = g_1005f85c;
                            v0 = 32;
                            sub_1002ade7(&v2);
                            return;
                        }
                        node += 1;
                        iter += 1;
                    }
                    else
                    {
                        iter += 1;
                    }
                }
                else
                {
                    iter += 1;
                }
            }
        }
    }
    return;
}
```

## `sub_100377a6` `0x100377a6`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100377a6(void)
{
}
```

## `sub_100377cb` `0x100377cb`

_424 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern int g_1005f85c;

int sub_100377cb(void)
{
    char *v15;  // ebx
    unsigned int v16;  // ebx
    unsigned int v17;  // eax
    unsigned int *v18;  // ebx
    unsigned int v19;  // ecx
    unsigned int v20;  // eax
    unsigned int v21;  // ecx
    unsigned int *v22;  // esi
    unsigned int v23;  // ecx
    unsigned int v24;  // edx
    unsigned int v0;  // [bp-0x154]
    unsigned int *v1;  // [bp-0x150], Other Possible Types: int, unsigned int
    unsigned int v2;  // [bp-0x134]
    unsigned int *v3;  // [bp-0x12c]
    unsigned int v4;  // [bp-0x128]
    unsigned int *v5;  // [bp-0x124]
    int v6;  // [bp-0x120]
    unsigned int idx;  // [bp-0x11c]
    unsigned int v8;  // [bp-0x118]
    char v9;  // [bp-0x114]
    int v10;  // [bp-0x14]
    unsigned int *v11;  // [bp-0x10]
    unsigned int node;  // [bp-0xc]
    unsigned int iter;  // [bp-0x8]

    for (idx = 0; *(v15) && idx < 63; idx += 1)
    {
        *((unsigned int *)&(&v9)[4 * idx]) = sub_100300ce();
    }
    v4 = 4294967295;
    sub_10013f16();
    node = 0;
    while (node < 14)
    {
        v16 = node - 6;
        if ((v16 ^ v16 >> 31) - (v16 >> 31) <= v17)
        {
            v18 = v16 + g_1005f858;
            v11 = v18;
            iter = 0;
            while (iter < 18)
            {
                v19 = iter - 8;
                if ((v19 ^ v19 >> 31) - (v19 >> 31) <= v17)
                {
                    v10 = v19 + g_1005f854;
                    v20 = sub_1003a065(v10, v11, g_1005f85c);
                    if (v20)
                    {
                        v21 = *(v18);
                        v22 = v18 + 1;
                        if (*(v22) == 386 || *(v22) == 421 || *(v22) == 7762)
                        {
                            iter += 1;
                        }
                        else
                        {
                            while (true)
                            {
                                if (!v21)
                                {
                                    v23 = 0;
                                    while (true)
                                    {
                                        if (v23 < idx)
                                        {
                                            if (v20 != *((int *)&(&v9)[4 * v23]))
                                            {
                                                v23 += 1;
                                            }
                                            else
                                            {
                                                v1 = v20;
                                                v0 = v23;
                                                if (sub_1000d9b8(iter, node, 0))
                                                {
                                                    if (v24 < v4)
                                                    {
                                                        v1 = v10;
                                                        v6 = v1;
                                                        v1 = v11;
                                                        v5 = v1;
                                                        v8 = v1;
                                                        v2 = v0;
                                                        v4 = v24;
                                                        v3 = v18;
                                                        iter += 1;
                                                        break;
                                                    }
                                                    else
                                                    {
                                                        iter += 1;
                                                        break;
                                                    }
                                                }
                                                else
                                                {
                                                    iter += 1;
                                                    break;
                                                }
                                            }
                                        }
                                        else
                                        {
                                            iter += 1;
                                            break;
                                        }
                                    }
                                }
                                else if (*(v22) == 99 || *(v22) == 1948 || *(v22) == 1968)
                                {
                                    iter += 1;
                                    break;
                                }
                                else
                                {
                                    v21 -= 1;
                                    v22 += 3;
                                }
                            }
                        }
                    }
                    else
                    {
                        iter += 1;
                    }
                }
                else
                {
                    iter += 1;
                }
            }
            node += 1;
        }
        else
        {
            node += 1;
        }
    }
    if (v4 == 4294967295)
        return;
    return;
}
```

## `sub_10037973` `0x10037973`

_67 bytes. (leaf/helper — see body)_

```c
int sub_10037973(void)
{
    char v1;  // cl

    if (v1 == 1)
    {
        return;
    }
    else if (v1 == 2)
    {
        return;
    }
    else if (v1 == 3)
    {
        return;
    }
    else if (v1 == 4)
    {
        return;
    }
    else if (v1 == 5)
    {
        return;
    }
    else if (v1 == 6)
    {
        return;
    }
    else if (v1 == 7)
    {
        return;
    }
    else
    {
        return;
    }
}
```

## `sub_100379b6` `0x100379b6`

_89 bytes. refs "Level spy off.", "Spying on level +%d.", "Spying on level -%d."_

```c
extern unsigned int g_102e2a08;

int sub_100379b6(void)
{
    unsigned int v0;  // [bp-0x88]
    Byte v1[128];  // [bp-0x84]

    if (!g_102e2a08)
        return sub_10039374("Level spy off.");
    if (g_102e2a08 > 50)
    {
        v0 = ~(g_102e2a08) + 1;
        wsprintfA(v1, "Spying on level +%d.");
    }
    else
    {
        v0 = g_102e2a08;
        wsprintfA(v1, "Spying on level -%d.");
    }
    return sub_10039374(v1);
}
```

## `sub_10037a0f` `0x10037a0f`

_89 bytes. (leaf/helper — see body)_

```c
int sub_10037a0f(void)
{
    unsigned int idx[21];  // eax
    unsigned int iter;  // ebx
    unsigned int node;  // esi
    unsigned int v8;  // ecx
    char v0;  // [bp-0xac]
    unsigned int v1;  // [bp-0x88]
    unsigned int v2;  // [bp-0x84]
    unsigned int v3;  // [bp-0x80]

    iter = idx[9];
    node = idx[10];
    v8 = idx[20];
    if (!idx[20])
    {
        node -= 2;
    }
    else if (v8 == 1)
    {
        iter += 2;
    }
    else if (v8 == 2)
    {
        node += 2;
    }
    else if (v8 == 3)
    {
        iter -= 2;
    }
    v1 = iter;
    v2 = node;
    v3 = idx[11];
    sub_1003a60a(&v0, 41);
    return;
}
```

## `sub_10037a68` `0x10037a68`

_164 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    struct struct_1 *field_4;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern int g_10052770;

unsigned int sub_10037a68(int a0, int a1)
{
    struct_0 *idx;  // eax
    unsigned int v1;  // eax
    unsigned int *i;  // esi
    unsigned int *v3;  // ebx
    unsigned int v4;  // eax

    if (sub_10011a89(a0, a1))
        return 0;
    idx = sub_1003a03f(a0, a1, g_10052770);
    if (!idx)
    {
        return 0;
    }
    else if (!idx->field_0)
    {
        return 0;
    }
    else
    {
        v1 = sub_1003c4fa(idx->field_4, idx);
        if (!((char)v1 & 1))
            return v1 & 1;
        i = &idx->field_4[1].field_0;
        for (v3 = &i[3 * idx->field_4->field_0]; i < v3; i = *(v3) + 12)
        {
            if (*(i) == 0x63)
                return 0;
            v4 = sub_1003c3fc(*(i), i, v3);
            v3 = *(i);
            if (v4)
                return 0;
            if (sub_1003c462(*(v3), v3))
                return 0;
        }
        return 1;
    }
}
```

## `sub_10037b0c` `0x10037b0c`

_358 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[36];
    struct struct_0 *field_24;
    int field_28;
    unsigned int field_2c;
    char padding_30[96];
    unsigned int field_90;
} struct_0;

typedef struct struct_1 {
    char padding_0[36];
    int field_24;
    int field_28;
} struct_1;

extern unsigned int g_10052768;
extern unsigned int g_1005276c;
extern struct_1 *g_1005f7ed;
extern char g_1005f85c;
extern unsigned int g_100f9328;

int sub_10037b0c(void)
{
    struct_0 *i;  // ebx
    struct_0 *v15;  // ebx
    int v16[11];  // eax
    unsigned int node;  // esi
    char *iter;  // eax
    unsigned int v19;  // edi
    int v20;  // eax
    int v21;  // ebx
    int v22;  // eax
    unsigned int v0;  // [bp-0x1e4]
    unsigned int v1;  // [bp-0x1e0]
    unsigned int v2;  // [bp-0x1dc]
    unsigned int v3;  // [bp-0x1d8]
    char *v4;  // [bp-0x1d4]
    unsigned int v5;  // [bp-0x1b8]
    unsigned int v6;  // [bp-0x1b4]
    unsigned int v7;  // [bp-0x1b0]
    char v8[252];  // [bp-0x1ac]
    char v9;  // [bp-0xb0]
    unsigned int v10;  // [bp-0x8c]
    unsigned int v11;  // [bp-0x88]
    unsigned int v12;  // [bp-0x84]

    sub_1002ae81(v8, 252);
    for (i = 0x63fef8; i < 0x64a308; i = &v15[1].padding_0[20])
    {
        v15 = i;
        if (v15->field_90)
        {
            v15 = i;
            if (*((int *)&g_1005f85c) == v15->field_2c)
            {
                v15 = i;
                if (sub_1003a494(&v15->padding_0[4]))
                {
                    v3 = i->field_24;
                    sub_1003c55d(i->field_24, i->field_28, v16[9], v16[10], v8, i);
                    v15 = v3;
                }
            }
        }
    }
    node = 0;
    v7 = 0;
    v6 = 0;
    v5 = 0;
    for (iter = &v8[0]; node < 14; node += 1)
    {
        for (v19 = 0; v19 < 18; iter += 1)
        {
            node = node;
            if (*(iter) > v5)
            {
                v4 = iter;
                v3 = v19;
                v2 = node;
                v20 = g_10052768 - 8 + v19;
                v21 = g_1005276c - 6 + node;
                v1 = g_10052768 - 8 + v19;
                v0 = g_1005276c - 6 + node;
                if (!sub_10037a68(v20, v21))
                {
                    node = v2;
                }
                else
                {
                    v22 = v20;
                    if (v16 != g_1005f7ed)
                        v22 = sub_1003c55d(v16[9], v16[10], v22, v21, 0);
                    node = v2;
                    if (v22)
                    {
                        v5 = *(iter);
                        v7 = v19;
                        v6 = node;
                    }
                }
            }
            v19 += 1;
        }
    }
    if (v5)
    {
        g_100f9328 = 1;
        v10 = g_1005f7ed->field_24 - 8 + v7;
        v11 = g_1005f7ed->field_28 - 6 + v6;
        v12 = *((int *)&g_1005f85c);
        sub_1003a60a(&v9, 41);
    }
    return;
}
```

## `sub_10037c72` `0x10037c72`

_786 bytes. refs "enemy", "subenemy", "friend"_

```c
typedef struct struct_0 {
    char padding_0[36];
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
    char padding_30[96];
    unsigned int field_90;
} struct_0;

extern char g_1005f85c;
extern char g_10077174;
extern struct_0 *g_100f9349;
extern unsigned int g_100f934d;
extern unsigned int g_100f9351;

unsigned int [37] sub_10037c72(void)
{
    unsigned int v12;  // eax
    unsigned int j[37];  // ebx
    unsigned int v14[37];  // ebx
    char v15;  // dl
    unsigned int v16[37];  // ebx
    unsigned int v17;  // eax
    unsigned int k;  // ecx
    unsigned int v19;  // edi
    unsigned int v20;  // edx
    unsigned int v21;  // eax
    char *iter;  // esi
    char *node;  // edi
    char v9;  // cl
    char *iter1;  // edi
    char v11;  // cl
    unsigned int v0[37];  // [bp-0x58]
    unsigned int v1;  // [bp-0x50]
    unsigned int v2[37];  // [bp-0x4c]
    char v3;  // [bp-0x46]
    char v4;  // [bp-0x45]
    int v5;  // [bp-0x44], Other Possible Types: char

    v4 = 0;
    for (v3 = 0; *(iter) == 32; iter += 1);
    node = &v5;
    do
    {
        v9 = *(iter);
    } while (*(iter) && v9 != 32 && (*(node) = v9, iter += 1, node += 1, v9 != 58));
    *(node) = 0;
    if (!lstrcmpi(&v5, "enemy"))
    {
        v4 = 1;
    }
    else if (!lstrcmpi(&v5, "subenemy"))
    {
        v4 = 2;
    }
    else if (!lstrcmpi(&v5, "friend"))
    {
        v4 = 3;
    }
    else if (!lstrcmpi(&v5, "subfriend"))
    {
        v4 = 4;
    }
    else
    {
        return NULL;
    }
    for (; *(iter) == 32; iter += 1);
    iter1 = &v5;
    do
    {
        v11 = *(iter);
    } while (*(iter) && v11 != 32 && (*(iter1) = v11, iter += 1, iter1 += 1, v11 != 58));
    *(iter1) = 0;
    if (*((char *)&v5))
    {
        if (!lstrcmpi(&v5, "sorcerer"))
        {
            v3 = 3;
        }
        else if (!lstrcmpi(&v5, "druid"))
        {
            v3 = 4;
        }
        else if (!lstrcmpi(&v5, "knight"))
        {
            v3 = 5;
        }
        else if (!lstrcmpi(&v5, "paladin"))
        {
            v3 = 6;
        }
        else if (!lstrcmpi(&v5, "mage"))
        {
            v3 = 7;
        }
        else if (!lstrcmpi(&v5, "nonmage"))
        {
            v3 = 8;
        }
        else
        {
            return NULL;
        }
    }
    v12 = _INSERT(v4 * 0x100, 0, v3);
    if (g_100f934d == v12)
        return g_100f9349;
    g_100f934d = v12;
    v2 = NULL;
    v1 = 0;
    for (j = 0x63fef8; j < 0x64a308; j = &v14[1 + 5])
    {
        v14 = j;
        if (v14[36] && (v14 = j, *((int *)&g_1005f85c) == v14[11]))
        {
            if (v4 == 1)
            {
                v14 = j;
                if (!sub_1003a494(&v14[1]))
                    goto LABEL_10037f53;
            }
            else if (v4 == 2)
            {
                v14 = j;
                if (!sub_1003a550(&v14[1]))
                    goto LABEL_10037f53;
            }
            else if (v4 == 3)
            {
                v14 = j;
                if (!sub_1003a320(&v14[1]))
                    goto LABEL_10037f53;
            }
            else if (v4 == 4 && (v14 = j, !sub_1003a3da(v14 + 4)))
            {
                goto LABEL_10037f53;
            }
            if (v3)
            {
                v15 = *((char *)(sub_10023861() + 76));
                if ((v3 != 3 || v15 != 3 && v15 != 7) && (v3 != 4 || v15 != 4 && v15 != 8) && (v3 != 5 || v15 != 1 && v15 != 5) && (v3 != 6 || v15 != 2 && v15 != 6) && (v3 != 7 || v15 != 3 && v15 != 7 && v15 != 4 && v15 != 8) && (v3 != 8 || v15 != 1 && v15 != 5 && v15 != 2 && v15 != 6))
                {
                    v14 = j;
                    goto LABEL_10037f53;
                }
            }
            v0 = j;
            v16 = j;
            v14 = v16;
            if (!sub_10011a89(j[9], j[10]))
            {
                v17 = sub_10023861();
                k = 0;
                for (v19 = 0; k < 20; k += 1)
                {
                    v20 = g_10077174 + k + 1;
                    if (v20 > 20)
                        v20 -= 20;
                    v19 += (k + 20) * *((char *)(v20 + v17 + 112));
                }
                v14 = v16;
                if (v19 > v1)
                {
                    v1 = v19;
                    v2 = v16;
                    v14 = v16;
                }
            }
        }
LABEL_10037f53:
    }
    v21 = 0;
    if (v2)
        v21 = sub_10037f84();
    g_100f9351 = v21;
    g_100f9349 = v2;
    return v2;
}
```

## `sub_10037f84` `0x10037f84`

_29 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10037f84(void)
{
    unsigned int v1;  // eax
    unsigned int i;  // ecx
    unsigned int v3;  // edx

    v1 = sub_10023861();
    i = 0;
    for (v3 = 0; i < 20; i += 1)
    {
        v3 += *((char *)(i + v1 + 112));
    }
    return v3;
}
```

## `sub_10037fa1` `0x10037fa1`

_316 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[36];
    struct struct_0 *field_24;
    int field_28;
} struct_0;

extern unsigned int g_10052768;
extern unsigned int g_1005276c;
extern struct_0 *g_1005f7ed;
extern unsigned int g_1005f85c;

unsigned int sub_10037fa1(void)
{
    struct_0 *v7;  // ebx
    int v8;  // ecx
    int v9;  // ecx
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // ss
    unsigned long v13;  // 4121
    struct_0 *j;  // ebx
    struct_0 *v15;  // ebx
    unsigned int v0;  // [bp-0x138]
    int v1;  // [bp-0x128]
    unsigned int v2;  // [bp-0x114]
    unsigned int i;  // [bp-0x10c]
    unsigned int iter;  // [bp-0x108]
    char v5[253];  // [bp-0x101]

    if (g_1005f85c != *((int *)&v7[1].padding_0[0]))
    {
        return 0;
    }
    else if (sub_10011a89(*((unsigned short *)&v7->field_24), v7->field_28))
    {
        return 0;
    }
    else
    {
        sub_1002ae81(v5, 253);
        for (i = 0; i < 14; i += 1)
        {
            v8 = g_1005276c - 6 + i;
            iter = 0;
            while (true)
            {
                v9 = v8;
                if (iter >= 18)
                    break;
                v1 = g_10052768 - 8 + iter;
                if (sub_1003c87c(g_10052768 - 8 + iter, v9, v9))
                {
                    v13 = _ccall(v10, v11, (unsigned int)v12, v5 + i * 18 + iter);
                    *((char *)v13) = 1;
                    iter += 1;
                    v8 = v1;
                }
                else
                {
                    iter += 1;
                    v8 = v1;
                }
            }
        }
        v2 = 0;
        for (j = 0x63fef8; j < 0x64a308; j = &v15[3].field_24)
        {
            v15 = j;
            if (*((int *)&v15[3].padding_0[12]))
            {
                v15 = j;
                if (g_1005f85c == *((int *)&v15[1].padding_0[0]))
                {
                    v15 = j;
                    if (v15 != v7 && (j == g_1005f7ed || (v15 = j, sub_1003a320(v15 + 4))))
                    {
                        v0 = j->field_24;
                        v15 = v0;
                        if (sub_1003c718(j->field_24, j->field_28, v7->field_24, v7->field_28, v5, j))
                        {
                            v2 += 1;
                            v15 = v0;
                        }
                    }
                }
            }
        }
        return v2;
    }
}
```

## `sub_100380dd` `0x100380dd`

_876 bytes. refs "enemy", "subenemy", "sorcerer"_

```c
typedef struct struct_0 {
    char padding_0[36];
    unsigned int field_24;
    struct struct_0 *field_28;
    unsigned int field_2c;
    char padding_30[96];
    unsigned int field_90;
} struct_0;

extern unsigned int g_10052768;
extern unsigned int g_1005276c;
extern char g_1005f7ed;
extern char g_1005f85c;
extern unsigned int g_100f933d;
extern unsigned int g_100f9341;
extern unsigned int g_100f9345;

unsigned int sub_100380dd(void)
{
    int v11;  // ebx
    unsigned int v12;  // eax
    unsigned long v21;  // gdt
    unsigned short v22;  // ss
    unsigned long v23;  // 4121
    struct_0 *iter;  // ebx
    int v25;  // ecx
    unsigned int v26;  // eax
    unsigned int index;  // ecx
    int node;  // ecx
    unsigned int v29;  // edx
    unsigned int v30;  // eax
    unsigned int i[11];  // ebx
    unsigned int v14[11];  // ebx
    char v15;  // cl
    char v16;  // dl
    unsigned int v17[11];  // ebx
    int v18;  // ecx
    int v19;  // ecx
    unsigned long v20;  // ldt
    unsigned int v0;  // [bp-0x920]
    int v1;  // [bp-0x8fc]
    unsigned int v2[11];  // [bp-0x8f0]
    unsigned int v3;  // [bp-0x8e4]
    int idx;  // [bp-0x8e0]
    char v5;  // [bp-0x8dc]
    char v6;  // [bp-0x4f4]
    unsigned int j;  // [bp-0x10c]
    unsigned int iter1;  // [bp-0x108]
    char v9[253];  // [bp-0x101]

    if (!lstrcmpi(v11, "enemy"))
    {
        v12 = 1;
    }
    else if (!lstrcmpi(v11, "subenemy"))
    {
        v12 = 2;
    }
    else if (!lstrcmpi(v11, "sorcerer"))
    {
        v12 = 3;
    }
    else if (!lstrcmpi(v11, "druid"))
    {
        v12 = 4;
    }
    else if (!lstrcmpi(v11, "knight"))
    {
        v12 = 5;
    }
    else if (!lstrcmpi(v11, "paladin"))
    {
        v12 = 6;
    }
    else if (!lstrcmpi(v11, "mage"))
    {
        v12 = 7;
    }
    else if (!lstrcmpi(v11, "nonmage"))
    {
        v12 = 8;
    }
    else
    {
        return 0;
    }
    if (g_100f9341 == v12)
        return g_100f933d;
    v3 = v12;
    idx = 0;
    sub_1002ae81(v9, 253);
    for (i = 0x63fef8; i < 0x64a308; i = &v14[3 + 9])
    {
        v14 = i;
        if (v14[3 + 3] && (v14 = i, *((int *)&g_1005f85c) == v14[1]))
        {
            if ((char)v3 == 1)
            {
                v14 = i;
                if (!sub_1003a494(&v14[1]))
                    goto LABEL_10038305;
            }
            else if ((char)v3 == 2)
            {
                v14 = i;
                if (!sub_1003a550(&v14[1]))
                    goto LABEL_10038305;
            }
            else
            {
                v14 = i;
                if (!sub_1003a494(&v14[1]))
                    goto LABEL_10038305;
                v15 = v3;
                v16 = *((char *)(sub_10023861() + 76));
                if ((v15 != 3 || v16 != 3 && v16 != 7) && (v15 != 4 || v16 != 4 && v16 != 8) && (v15 != 5 || v16 != 1 && v16 != 5) && (v15 != 6 || v16 != 2 && v16 != 6) && (v15 != 7 || v16 != 3 && v16 != 7 && v16 != 4 && v16 != 8) && (v15 != 8 || v16 != 1 && v16 != 5 && v16 != 2 && v16 != 6))
                {
                    v14 = i;
                    goto LABEL_10038305;
                }
            }
            v2 = i;
            v17 = v2;
            v14 = v17;
            if (!sub_10011a89(i[9], i[10]))
            {
                *((unsigned int *[11])&(&v6)[4 * idx]) = v17;
                *((unsigned int *)&(&v5)[4 * idx]) = 0;
                idx += 1;
                v14 = v17;
            }
        }
LABEL_10038305:
    }
    for (j = 0; j < 14; j += 1)
    {
        v18 = g_1005276c - 6 + j;
        iter1 = 0;
        while (true)
        {
            v19 = v18;
            if (iter1 >= 18)
                break;
            v1 = g_10052768 - 8 + iter1;
            if (sub_1003c87c(g_10052768 - 8 + iter1, v19, v19))
            {
                v23 = _ccall(v20, v21, (unsigned int)v22, v9 + j * 18 + iter1);
                *((char *)v23) = 1;
                iter1 += 1;
                v18 = v1;
            }
            else
            {
                iter1 += 1;
                v18 = v1;
            }
        }
    }
    for (iter = 0x63fef8; iter < 0x64a308; iter = &iter[1].padding_0[20])
    {
        if (iter->field_90 && *((int *)&g_1005f85c) == iter->field_2c && (iter == *((int *)&g_1005f7ed) || sub_1003a320(&iter->padding_0[4])))
        {
            v25 = 0;
            while (true)
            {
                if (v25 >= idx)
                    break;
                v0 = iter->field_28;
                v26 = sub_1003c718(iter->field_24, iter->field_28, *((int *)(*((int *)&(&v6)[4 * v25]) + 36)), *((int *)(*((int *)&(&v6)[4 * v25]) + 40)), v9, v25, iter);
                index = iter->field_24;
                if (v26)
                {
                    *((unsigned int *)&(&v5)[4 * index]) = *((int *)&(&v5)[4 * index]) + 1;
                    v25 = index + 1;
                    iter = v0;
                }
                else
                {
                    v25 = index + 1;
                    iter = v0;
                }
            }
        }
    }
    node = 0;
    v29 = 0;
    v30 = 0;
    while (node < idx)
    {
        if (*((int *)&(&v5)[4 * node]) > v29)
        {
            v29 = *((int *)&(&v5)[4 * node]);
            v30 = *((int *)&(&v6)[4 * node]);
            node += 1;
        }
        else
        {
            node += 1;
        }
    }
    g_100f933d = v30;
    g_100f9345 = v29;
    g_100f9341 = v3;
    return v30;
}
```

## `sub_10038449` `0x10038449`

_178 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_10043482;
extern char g_10043487;
extern char g_10043489;
extern unsigned short g_1004348a;
extern char g_1004348c;
extern unsigned short g_1004348d;
extern unsigned short g_1004348f;
extern char g_10043491;
extern unsigned int g_10052768;
extern unsigned int g_1005276c;
extern char g_10052770;

int sub_10038449(void)
{
    unsigned int v5;  // eax
    unsigned int v6;  // eax
    char v7;  // dl
    unsigned int v8;  // eax
    int v9;  // ebx
    int v10;  // ecx
    unsigned int v0;  // [bp-0x2c]
    unsigned int i;  // [bp-0x10]
    unsigned int iter;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v3 = v5;
    v6 = sub_1002ae92(3465, 0, NULL);
    if (!v6)
        return v6;
    g_10043487 = v6;
    g_10043489 = v7;
    g_1004348c = v7;
    g_1004348a = 3465;
    v8 = _INSERT(v6, 0, g_10052770);
    g_10043491 = g_10052770;
    for (i = 0; i < 3; i += 1)
    {
        iter = 0;
        while (iter < 3)
        {
            if (iter != 1 || i != 1)
            {
                v9 = g_10052768 - 1 + iter;
                v10 = g_1005276c - 1 + i;
                g_1004348d = v9;
                g_1004348f = v10;
                if (sub_1003c936(v9, v10))
                {
                    v0 = 0x11;
                    return sub_1002ade7(&g_10043482);
                }
                iter += 1;
            }
            else
            {
                iter += 1;
            }
        }
    }
    return v8;
}
```

## `sub_100384fb` `0x100384fb`

_387 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    char padding_8[8];
    unsigned int field_10;
    char padding_14[36];
    struct struct_0 *field_38;
    struct struct_0 *field_3c;
    unsigned int field_40;
} struct_0;

extern unsigned short g_10043465;
extern char g_1004346a;
extern char g_1004346c;
extern unsigned short g_1004346d;
extern char g_1004346f;
extern char g_10043472;
extern char g_10043474;
extern char g_10043475;
extern char g_100f45ac;

unsigned int sub_100384fb(void)
{
    struct_0 *v8;  // ebx
    unsigned int v9;  // eax
    struct_0 *v10;  // esi
    struct_0 *j;  // ecx
    struct_0 *v12;  // ecx
    struct_0 *v13;  // esi
    struct_0 *v14;  // ecx
    struct_0 *v15;  // esi
    unsigned int k;  // edx
    struct_0 *v0;  // [bp-0x82c]
    unsigned int v1;  // [bp-0x824]
    unsigned int idx;  // [bp-0x818]
    char v3;  // [bp-0x814]
    char v4;  // [bp-0x812]
    char v5;  // [bp-0x811]
    unsigned int iter;  // [bp-0x8]

    idx = 0;
    iter = 0;
    while (iter < 16)
    {
        v8 = iter * 492 + 6606096;
        v9 = v8->field_10;
        if (v8->field_0)
        {
            if ((&g_100f45ac)[iter])
            {
                if (v9 == 1684104516)
                {
                    iter += 1;
                    continue;
                }
                else if (v9 == 1767992403)
                {
                    iter += 1;
                    continue;
                }
                else if (v9 == 1634559314)
                {
                    iter += 1;
                    continue;
                }
                else if (v9 == 1768714323)
                {
                    iter += 1;
                    continue;
                }
                else if (v9 == 1835363397)
                {
                    iter += 1;
                    continue;
                }
                else if (v9 == 543516756)
                {
                    iter += 1;
                    continue;
                }
                else if (v8->field_10 == 6775106 && (&g_100f45ac)[iter] >= 2)
                {
                    iter += 1;
                    continue;
                }
            }
            v10 = &v8->field_3c;
            for (j = NULL; j < v8->field_38; j = (char *)&v12->field_0 + 1)
            {
                v12 = j;
                v13 = v10;
                if (v13->field_4 > 0)
                {
                    v12 = j;
                    v13 = v10;
                    if (v13->field_4 < 100)
                    {
                        v0 = v10->field_0;
                        v14 = v8;
                        v15 = j;
                        v8 = v0;
                        v12 = v14;
                        v13 = v15;
                        if (sub_1003c52a(v10->field_0, v8, j, v10))
                        {
                            for (k = 0; k < idx; k += 1)
                            {
                                if ((unsigned short)v15->field_0 == *((short *)&(&v3)[4 * k]))
                                {
                                    g_1004346a = iter + 64;
                                    g_1004346c = *((char *)&v14);
                                    g_1004346f = *((char *)&v14);
                                    g_10043475 = v15->field_4;
                                    g_1004346d = v15->field_0;
                                    g_10043472 = v4 + 64;
                                    g_10043474 = v5;
                                    v1 = 0x11;
                                    sub_1002ade7(&g_10043465);
                                    return 1;
                                }
                            }
                            *((unsigned short *)&(&v3)[4 * idx]) = v15->field_0;
                            (&v4)[4 * idx] = iter;
                            (&v5)[4 * idx] = *((char *)&v14);
                            idx += 1;
                            v8 = v0;
                            v12 = v14;
                            v13 = v15;
                        }
                    }
                }
                v10 = &v13->padding_8[4];
            }
            iter += 1;
        }
        else
        {
            iter += 1;
        }
    }
    return 0;
}
```

## `sub_1003867e` `0x1003867e`

_165 bytes. (leaf/helper — see body)_

```c
extern char g_1004347b;
extern char g_1004347d;
extern unsigned short g_1004347e;
extern char g_10043480;
extern char g_10043481;
extern unsigned int g_1008caee[4];

unsigned int * sub_1003867e(void)
{
    unsigned int *v5;  // eax
    char v6;  // dl
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int iter;  // [bp-0x8]

    for (iter = 0; iter < 16; iter += 1)
    {
        if (*((int *)(iter * 492 + 6606096)))
        {
            v2 = 0;
            while (true)
            {
                if (v2 < 0x200)
                {
                    v5 = &g_1008caee[v2];
                    v1 = *(v5);
                    if (v1)
                    {
                        v5 = sub_1002ae92(v1, iter + 16, NULL);
                        if (v5)
                        {
                            g_1004347e = v1;
                            g_1004347b = *((char *)&v5);
                            g_1004347d = v6;
                            g_10043480 = v6;
                            g_10043481 = 1;
                            v0 = 12;
                            return sub_1002ade7("\n");
                        }
                        v2 += 1;
                    }
                    else
                    {
                        iter += 1;
                        break;
                    }
                }
                else
                {
                    iter += 1;
                    break;
                }
            }
        }
    }
    return v5;
}
```

## `sub_10038706` `0x10038706`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10038706(void)
{
}
```

## `sub_10038725` `0x10038725`

_393 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[2048];
    unsigned int field_800;
} struct_0;

typedef struct struct_1 {
    char padding_0[48];
    unsigned int field_30;
} struct_1;

extern unsigned short g_10043465;
extern char g_1004346a;
extern char g_1004346c;
extern unsigned short g_1004346d;
extern char g_1004346f;
extern char g_10043472;
extern char g_10043475;
extern char g_1004347b;
extern char g_1004347d;
extern unsigned short g_1004347e;
extern char g_10043480;
extern char g_10043481;
extern unsigned int g_1008baee[4];

int sub_10038725(void)
{
    unsigned int v6;  // eax
    unsigned int v7[5];  // ebx
    struct_0 *idx;  // eax
    struct_1 *v9;  // edx
    unsigned int v10;  // eax
    char v11;  // dl
    unsigned int v12;  // ecx
    unsigned int v13;  // ecx
    char v14;  // dl
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int node;  // [bp-0xc]
    unsigned int iter;  // [bp-0x8]

    iter = 0;
    while (iter < 16)
    {
        v7 = iter * 492 + 6606096;
        if (!v7[0])
        {
            iter += 1;
        }
        else if (v7[4] == 1684104516 || v7[4] == 1767992403 || v7[4] == 6775106 || v7[4] == 1634559314 || v7[4] == 1768714323 || v7[4] == 1835363397 || v7[4] == 543516756)
        {
            node = 0;
            while (node < 128 && !((idx = (struct_0 *)(node * 4 + &g_1008baee[0]), !*((int *)&idx->padding_0[0]))))
            {
                v2 = *((int *)&idx->padding_0[0]);
                v1 = idx->field_800;
                v9 = idx->field_800 * 492 + 6606096;
                if (*((int *)&v9->padding_0[0]))
                {
                    if (*((int *)&v9[1].padding_0[4]) < v9->field_30 || v2 == *((int *)&v9[1].padding_0[8]) && *((int *)&v9[1].padding_0[12]) > 0 && *((int *)&v9[1].padding_0[12]) < 100)
                    {
                        v10 = sub_1002ae92(v2, iter + 16, NULL);
                        if (v10)
                        {
                            g_1004346c = v11;
                            g_1004346d = v2;
                            g_1004346f = v11;
                            g_1004346a = v10;
                            v13 = v12;
                            if (!v12)
                                v13 += 1;
                            g_10043475 = v13;
                            g_10043472 = v1 + 64;
                            v0 = 0x11;
                            return sub_1002ade7(&g_10043465);
                        }
                    }
                    node += 1;
                }
                else
                {
                    node += 1;
                }
            }
            if (sub_1002ae92(2853, iter + 16, NULL))
            {
                g_1004347d = v14;
                g_10043480 = v14;
                g_1004347e = 2853;
                g_10043481 = iter;
                g_1004347b = g_10043481 + 64;
                v0 = 12;
                return sub_1002ade7("\n");
            }
            iter += 1;
        }
        else
        {
            iter += 1;
        }
    }
    return v6;
}
```

## `sub_100388ae` `0x100388ae`

_1136 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
    char padding_4[44];
    unsigned int field_30;
    char padding_34[12];
    void* field_40;
} struct_1;

typedef struct struct_2 {
    char padding_0[56];
    unsigned int field_38;
} struct_2;

extern unsigned short g_10043465;
extern char g_1004346a;
extern char g_1004346c;
extern unsigned short g_1004346d;
extern char g_1004346f;
extern char g_10043472;
extern char g_10043474;
extern char g_10043475;
extern char g_1004347b;
extern char g_1004347d;
extern unsigned short g_1004347e;
extern char g_10043480;
extern char g_10043481;
extern unsigned short g_100434a4;
extern char g_100434a9;
extern char g_100434ab;
extern unsigned short g_100434ac;
extern char g_100434ae;
extern unsigned short g_100434af;
extern unsigned short g_100434b1;
extern char g_100434b3;
extern char g_100434b4;
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern unsigned int g_1005f85c;
extern unsigned int g_1008caee[4];
extern unsigned int g_100f0dcc;
extern unsigned int g_100f0dd0;
extern unsigned int g_100f0dd4;
extern unsigned int g_100f0e08;
extern unsigned int g_100f0e3c;
extern char g_100f45ac;
extern char g_10202f0a;

void* sub_100388ae(void)
{
    unsigned int count;  // eax
    void* count1;  // eax, Other Possible Types: unsigned int
    unsigned int v14;  // ecx
    unsigned int j;  // ecx
    unsigned int v16[13];  // esi
    unsigned int k;  // ecx
    void* v18;  // eax
    unsigned int v19;  // ecx
    void* v20;  // eax
    struct_2 *v21;  // edx
    void* v22;  // eax
    void* v23;  // eax
    struct_0 *v8;  // ebx
    unsigned int v9;  // ecx
    unsigned int v10;  // edx
    struct_1 *v11;  // edx
    char v12;  // dl
    unsigned int v13;  // ecx
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int iter;  // [bp-0xc]
    void* node;  // [bp-0x8]

    count = GetTickCount();
    count1 = count - g_100f0e08;
    if (count1 >= 0x1f4)
    {
        count1 = GetTickCount();
        g_100f0e08 = count1;
    }
    else if (count1 >= 0x64)
    {
        g_100f0e08 = g_100f0e08 + 100;
    }
    else
    {
        return count1;
    }
    if (g_100f0e3c)
        g_100f0e3c = g_100f0e3c - 1;
    if (g_100f0dcc)
        g_100f0dcc = g_100f0dcc - 1;
    if (g_100f0dd4)
        g_100f0dd4 = g_100f0dd4 - 1;
    if (g_100f0dcc == 3)
    {
        return count1;
    }
    else if (g_100f0dcc == 2)
    {
        return count1;
    }
    else if (!g_100f0dcc)
    {
        return count1;
    }
    else if (g_100f0dd0 == 4294967295)
    {
        return count1;
    }
    else
    {
        for (node = NULL; node < 0x10; node += 1)
        {
            v8 = node * 492 + 6606096;
            count1 = v8->field_10;
            if (*((int *)&v8->padding_0[0]) && *((char *)(node + &g_100f45ac)) && (count1 == 0x64616544 || count1 == 0x69616c53 || count1 == 0x616d6552 || count1 == 0x696c7053 || count1 == 0x6d656c45 || count1 == 0x20656854 || count1 == 0x676142 && *((char *)(node + &g_100f45ac)) >= 2))
            {
                iter = 0;
                while (true)
                {
                    if (iter >= 0x200)
                    {
LABEL_10038c42:
                        if (g_100f0dd0 >= 10)
                        {
                            v2 = 2853;
                            count1 = sub_1002ae92(2853, node + 16, NULL);
                            if (!count1)
                            {
                                v2 = 7343;
                                count1 = sub_1002ae92(7343, node + 16, NULL);
                            }
                            if (count1)
                            {
                                g_1004347d = v12;
                                g_10043480 = v12;
                                g_1004347e = v2;
                                g_10043481 = (char)node;
                                g_1004347b = g_10043481 + 64;
                                v0 = 12;
                                v23 = sub_1002ade7("\n");
                                *((char *)(node + &g_100f45ac)) = 2;
                                g_100f0dd0 = 0;
                                g_100f0dcc = 3;
                                return v23;
                            }
                            node += 1;
                            break;
                        }
                        else
                        {
                            node += 1;
                            break;
                        }
                    }
                    if (g_100f0dd0 < 10)
                    {
                        count1 = &g_1008caee[iter];
                        v2 = *((int *)count1);
                        if (*((int *)count1))
                            goto LABEL_10038a5a;
                    }
                    else
                    {
                        count1 = &(&g_10202f0a)[20 * iter];
                    }
                    v9 = *((short *)count1);
                    if (!v9)
                        goto LABEL_10038c42;
                    v2 = v9;
                    v10 = (char)count1[2];
                    v1 = v10;
                    if (v10 < 253)
                    {
                        count1 = v10;
                        v11 = v10 * 492 + 6606096;
                        if (!v11->field_0)
                        {
                            iter += 1;
                            continue;
                        }
                        if (count1 == node)
                        {
                            iter += 1;
                            continue;
                        }
                        if ((&g_100f45ac)[count1])
                        {
                            iter += 1;
                            continue;
                        }
                        count1 = v11->field_40;
                        if (*((int *)&v11->padding_34[4]) >= v11->field_30 && (v2 != *((int *)&v11->padding_34[8]) || count1 <= NULL || count1 >= 0x64))
                            goto LABEL_10038c2e;
                    }
LABEL_10038a5a:
                    count1 = sub_1002ae92(v2, node + 16, NULL);
                    if (count1)
                    {
                        if (g_100f0dd0 < 10)
                        {
                            g_1004347e = v2;
                            g_1004347b = count1;
                            g_1004347d = v12;
                            g_10043480 = v12;
                            g_10043481 = 1;
                            v0 = 12;
                            v18 = sub_1002ade7("\n");
                            g_100f0dcc = 3;
                            g_100f0dd0 = g_100f0dd0 + 1;
                            if (!g_100f0dd4)
                                return v18;
                            g_100f0dd0 = 10;
                            return v18;
                        }
                        if (v1 == 253)
                        {
                            g_100434ac = v2;
                            g_100434a9 = count1;
                            g_100434ab = v12;
                            g_100434ae = v12;
                            v19 = v13;
                            if (!v13)
                                v19 += 1;
                            g_100434b4 = v19;
                            g_100434af = g_1005f854;
                            g_100434b1 = g_1005f858;
                            g_100434b3 = g_1005f85c;
                            v0 = 0x11;
                            v20 = sub_1002ade7(&g_100434a4);
                            g_100f0dcc = 3;
                            return v20;
                        }
                        g_1004346c = v12;
                        g_1004346d = v2;
                        g_1004346f = v12;
                        g_1004346a = count1;
                        v14 = v13;
                        if (!v13)
                            v14 += 1;
                        g_10043475 = v14;
                        j = 0;
                        if (v1 >= 254)
                        {
                            v16 = 0x64cd10;
                            if (v1 == 254)
                            {
                                j = 1;
                                v16 = 0x64cefc;
                            }
                            for (; j < 0x10; j += 1)
                            {
                                if (v16[0] && !(&g_100f45ac)[j])
                                {
                                    v0 = j;
                                    k = 0;
                                    for (count1 = NULL; k < v16[12]; k += 1)
                                    {
                                        if (k >= v16[1 + 1] || !*((int *)(60 + count1 + (char *)v16)) || *((int *)(60 + count1 + (char *)v16)) == v2 && *((int *)(64 + count1 + (char *)v16)) > 0 && *((int *)(64 + count1 + (char *)v16)) < 0x64)
                                        {
                                            g_10043474 = k;
                                            g_10043472 = j + 64;
                                            v0 = 0x11;
                                            v22 = sub_1002ade7(&g_10043465);
                                            g_100f0dcc = 3;
                                            return v22;
                                        }
                                        count1 += 12;
                                    }
                                }
                                v16 = &v16[9 + 6];
                            }
                            iter += 1;
                            continue;
                        }
                        else
                        {
                            g_10043472 = v1 + 64;
                            if (*((int *)&v21[1].padding_0[0]) != v2)
                            {
                                g_10043474 = v21->field_38;
                                v0 = 0x11;
                                v22 = sub_1002ade7(&g_10043465);
                                g_100f0dcc = 3;
                                return v22;
                            }
                            g_10043474 = 0;
                            v0 = 0x11;
                            v22 = sub_1002ade7(&g_10043465);
                            g_100f0dcc = 3;
                            return v22;
                        }
                    }
LABEL_10038c2e:
                    iter += 1;
                }
            }
            else
            {
                *((char *)(node + &g_100f45ac)) = 0;
            }
        }
        if (g_100f0dd0 >= 10)
        {
            g_100f0dcc = 0;
            return count1;
        }
        g_100f0dd0 = 10;
        g_100f0dcc = 3;
        return count1;
    }
}
```

## `sub_10038bef` `0x10038bef`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10038bef(void)
{
}
```

