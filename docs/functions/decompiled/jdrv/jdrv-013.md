# elfbot.dll decompiled — jdrv 0x100322dc..0x10033619

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_100322dc` `0x100322dc`

_11 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_100433a3;

void sub_100322dc(void)
{
    g_100433a3 = 7643;
}
```

## `sub_100322e7` `0x100322e7`

_11 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_100433a3;

void sub_100322e7(void)
{
    g_100433a3 = 7642;
}
```

## `sub_10032372` `0x10032372`

_145 bytes. (leaf/helper — see body)_

```c
extern int g_10084bf7;
extern unsigned int g_10084bfb;
extern unsigned int g_100f9328;
extern int g_100f94cb;

int sub_10032372(void)
{
    int v1;  // eax
    int v2;  // eax
    int v3;  // ecx

    g_100f9328 = 0;
    v1 = *(0x63fe64);
    if (!*((int *)0x63fe64))
        v1 = g_10084bf7;
    v2 = sub_1003c23e(sub_1003997e(v1));
    if (!v2)
    {
        return v2;
    }
    else if (*((int *)0x63fe64))
    {
        return sub_1003a60a(v2, g_100f94cb);
    }
    else
    {
        v3 = 0;
        if (g_10084bfb == 3198)
        {
            v3 = 1;
        }
        else if (g_10084bfb == 3155)
        {
            v3 = 4;
        }
        else if (g_10084bfb == 3200)
        {
            v3 = 5;
        }
        if (!v3)
            return v2;
        g_100f9328 = 1;
        sub_1003a60a(v2, v3);
        return v2;
    }
}
```

## `sub_10032403` `0x10032403`

_48 bytes. (leaf/helper — see body)_

```c
int sub_10032403(void)
{
    sub_10030225();
    sub_10030225();
    return sub_10038e29(/* unsupported instruction */ - 2032, /* unsupported instruction */ - 1904);
}
```

## `sub_10032433` `0x10032433`

_246 bytes. refs "Auto Off: ", "Auto On: "_

```c
extern unsigned int g_10084c0b[4];
extern unsigned int g_1008578b;
extern unsigned int g_1008630b;
extern unsigned int g_10086e8b;
extern unsigned int g_10087a0b;
extern unsigned int g_1008858b;

int sub_10032433(void)
{
    unsigned int v4;  // eax
    unsigned int v5;  // eax
    unsigned int idx;  // ebx
    unsigned int v7;  // esi
    unsigned int v8;  // edi
    unsigned int iter;  // eax
    int v1;  // [bp+0xffffc]
    int v2;  // [bp+0x100000]
    unsigned int v3;  // [bp+0x100010]

    if (v3 == 4294967295)
        return v4;
    v5 = sub_100300ce();
    v1 = v2;
    idx = v3;
    if (g_10084c0b[idx])
    {
        g_10084c0b[idx] = 0;
        (&g_1008578b)[idx] = 0;
        (&g_1008630b)[idx] = 0;
        (&g_1008858b)[idx] = 0;
        (&g_10087a0b)[idx] = 0;
        lstrcpy(/* unsupported instruction */ - 0x1000, "Auto Off: ");
        lstrcat(/* unsupported instruction */ - 0x1000, v1);
        return sub_10039374(/* unsupported instruction */ - 0x1000);
    }
    (&g_1008578b)[idx] = v7;
    (&g_1008630b)[idx] = v8;
    iter = v5;
    if (!v5)
    {
        if (v7)
        {
            iter += 1;
        }
        else if (v8)
        {
            iter += 1;
        }
    }
    g_10084c0b[idx] = iter;
    (&g_10086e8b)[idx] = iter;
    (&g_1008858b)[idx] = 0;
    (&g_10087a0b)[idx] = 0;
    lstrcpy(/* unsupported instruction */ - 0x1000, "Auto On: ");
    lstrcat(/* unsupported instruction */ - 0x1000, v1);
    return sub_10039374(/* unsupported instruction */ - 0x1000);
}
```

## `sub_10032529` `0x10032529`

_48 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_10087a0b;
extern unsigned int g_1008ab93;
extern unsigned int g_1008ab97;

void sub_10032529(void)
{
    unsigned int idx;  // [bp+0x100010]

    if (idx == 4294967295)
    {
        g_1008ab97 = 1;
    }
    else
    {
        g_1008ab93 = 1;
        (&g_10087a0b)[idx] = 4294967295;
    }
    return;
}
```

## `sub_10032559` `0x10032559`

_32 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1008ab93;
extern unsigned int g_1008ab97;

void sub_10032559(void)
{
    unsigned int v1;  // [bp+0x100010]

    if (v1 != 4294967295)
    {
        g_1008ab93 = 1;
        return;
    }
    g_1008ab97 = 1;
    return;
}
```

## `sub_10032579` `0x10032579`

_28 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_10084c0b;

void sub_10032579(void)
{
    unsigned int idx;  // [bp+0x100010]

    if (idx != 4294967295)
        (&g_10084c0b)[idx] = 0;
    return;
}
```

## `sub_10032595` `0x10032595`

_9 bytes. (leaf/helper — see body)_

```c
void sub_10032595(void)
{
    sub_10039bbb();
    return;
}
```

## `sub_1003259e` `0x1003259e`

_255 bytes. calls GetPrivateProfileStringA; refs "serverlist.txt", "Servers"_

```c
typedef struct struct_0 {
    char padding_0[30];
    char field_1e;
    char padding_1f[29];
    unsigned int field_3c;
    char field_40;
    char padding_41[15];
    unsigned int field_50;
} struct_0;

extern Byte g_100429fa;
extern int g_10042d7b;
extern unsigned int g_100f0e18;
extern int g_10291cf6;
extern int g_10291ef6;
extern int g_102920f6;
extern unsigned int g_79ced8;
extern unsigned int g_79cedc;
extern unsigned int g_79cee0;

int sub_1003259e(void)
{
    struct_0 *v2;  // eax
    struct_0 *idx;  // ebx
    int v0;  // [bp+0x0]
    int v1;  // [bp+0x4]

    sub_10030225();
    sub_10030225();
    sub_10030225();
    sub_10030225();
    v2 = g_79cedc;
    if (!g_79cedc)
    {
        v2 = HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, 0x1000);
        g_79cedc = v2;
    }
    g_79cee0 = 1;
    g_79ced8 = 0;
    idx = v2;
    lstrcpy(idx, &g_10291cf6);
    lstrcpy(&idx->field_1e, /* unsupported instruction */ - 2032);
    idx->field_50 = 7171;
    lstrcpy(/* unsupported instruction */ - 0x1000, &g_10042d7b);
    lstrcat(/* unsupported instruction */ - 0x1000, "serverlist.txt");
    GetPrivateProfileStringA("Servers", &idx->field_1e, &g_100429fa, &idx->field_40, 20, /* unsupported instruction */ - 0x1000);
    idx->field_3c = inet_addr(&idx->field_40);
    lstrcpy(7982820, &g_10291ef6);
    lstrcpy(7982852, &g_102920f6);
    g_100f0e18 = 0;
    return sub_10039bbb(v0, v1);
}
```

## `sub_1003269d` `0x1003269d`

_56 bytes. (leaf/helper — see body)_

```c
extern char g_100ba736;

unsigned int sub_1003269d(void)
{
    unsigned int v3;  // eax
    unsigned int v4;  // eax
    unsigned int v5;  // ecx
    unsigned int v6;  // eax
    unsigned int v0;  // [bp-0x4]
    unsigned int v2;  // [bp+0x100010]

    if (v2 != 4294967295)
    {
        v4 = sub_100300ce();
        v5 = &(&g_100ba736)[276 * v2];
        *((unsigned int *)(v5 + 0x100)) = v4;
        v0 = v5;
        v6 = sub_100300ce();
        *((unsigned int *)(v0 + 260)) = v6;
        return v6;
    }
    return v3;
}
```

## `sub_100326d5` `0x100326d5`

_145 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
    unsigned int field_10;
    unsigned int field_14;
} struct_0;

extern unsigned int g_100f49f1;

unsigned int sub_100326d5(void)
{
    unsigned int v2;  // eax
    unsigned int v3;  // eax
    unsigned int v4;  // eax
    unsigned int v5;  // eax
    unsigned int v6;  // eax
    struct_0 *idx;  // ebx
    unsigned int count;  // eax
    unsigned int v9;  // ecx
    struct_0 *index;  // [bp+0xffffc]

    v2 = sub_100300ce();
    if (v2 >= 32)
        return v2;
    index = v2 * 16668 + g_100f49f1;
    v3 = sub_100300ce();
    index->field_0 = v3;
    v4 = sub_100300ce();
    index->field_4 = v4;
    v5 = sub_100300ce();
    index->field_14 = v5;
    v6 = sub_100300ce();
    index->field_c = v6;
    sub_10030225();
    idx = index;
    idx->field_10 = 0;
    if (!lstrcmpi(/* unsupported instruction */ - 2032, "up"))
        idx->field_10 = 1;
    count = GetTickCount();
    v9 = idx->field_c * idx->field_14;
    idx->field_8 = count + v9;
    return count + v9;
}
```

## `sub_10032766` `0x10032766`

_157 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f49f1;

unsigned int sub_10032766(void)
{
    unsigned int v4;  // eax
    unsigned int v5;  // eax
    unsigned int v6;  // eax
    unsigned int v7;  // eax
    unsigned int idx[7];  // edi
    unsigned int v9;  // ecx
    unsigned int v10[137];  // ecx
    unsigned int count;  // eax
    unsigned int index[7];  // ebx
    unsigned int v13;  // eax
    unsigned int v0[137];  // [bp-0x4]
    unsigned int v2;  // [bp+0xffff8]
    unsigned int v3[7];  // [bp+0xffffc]

    v4 = sub_100300ce();
    if (v4 >= 32)
        return v4;
    v3[0] = v4 * 16668 + g_100f49f1;
    v5 = sub_100300ce();
    if (v5 <= 0xffffff)
    {
        v2 = v5;
        v6 = sub_100300ce();
        v2 |= v6 * 0x100;
        v7 = sub_100300ce();
        v5 = v7 * 0x10000 | v2;
    }
    idx = v3;
    v9 = idx[6];
    idx[6] = idx[6] + 1;
    if (idx[6] > 31)
        idx[6] = 0;
    v10 = 28 + 520 * v9 + (char *)idx;
    v10[128] = v5 & 0xffffff;
    v0 = v10;
    sub_10030225();
    count = GetTickCount();
    index = v3;
    v13 = count + index[3];
    v0[129] = v13;
    index[2] = count + index[3] * index[5];
    return v13;
}
```

## `sub_10032803` `0x10032803`

_74 bytes. (leaf/helper — see body)_

```c
extern char g_100ba736;

unsigned int sub_10032803(void)
{
    unsigned int v3;  // eax
    unsigned int v4;  // eax
    unsigned int v5[69];  // ecx
    unsigned int v6;  // eax
    unsigned int v7;  // eax
    unsigned int idx[69];  // [bp+0xffffc]
    unsigned int v2;  // [bp+0x100010]

    if (v2 != 4294967295)
    {
        v4 = sub_100300ce();
        v5 = &(&g_100ba736)[276 * v2];
        idx[0] = v5;
        v5[66] = v4;
        v6 = sub_100300ce();
        idx[67] = v6;
        v7 = sub_100300ce();
        idx[0x44] = v7;
        return v7;
    }
    return v3;
}
```

## `sub_1003284d` `0x1003284d`

_47 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100ee8b6;

void sub_1003284d(void)
{
    unsigned int v1;  // [bp+0x100010]

    if (v1 != 4294967295)
    {
        sub_10030225();
        g_100ee8b6 = 1;
    }
    return;
}
```

## `sub_1003287c` `0x1003287c`

_51 bytes. (leaf/helper — see body)_

```c
extern char g_100ba736;
extern unsigned int g_100ee8b6;

void sub_1003287c(void)
{
    unsigned int idx;  // [bp+0x100010]

    if (idx != 4294967295)
    {
        (&g_100ba736)[276 * idx] = 3;
        sub_10030225();
        g_100ee8b6 = 3;
    }
    return;
}
```

## `sub_100328af` `0x100328af`

_24 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100ee8b6;

void sub_100328af(void)
{
    unsigned int v1;  // [bp+0x100010]

    if (v1 != 4294967295)
        g_100ee8b6 = 2;
    return;
}
```

## `sub_100328c7` `0x100328c7`

_147 bytes. refs "exura sio \"_

```c
typedef struct struct_0 {
    char padding_0[136];
    unsigned int field_88;
} struct_0;

extern char g_10080ba6;
extern unsigned int g_100f9328;

struct_0 * sub_100328c7(void)
{
    unsigned int v4;  // eax
    struct_0 *v5;  // eax
    struct_0 *v6;  // eax
    struct_0 *v0;  // [bp-0x10]
    unsigned int v2;  // [bp+0xffffc]
    unsigned int v3;  // [bp+0x100000]

    g_100f9328 = 0;
    sub_100300ce();
    v4 = (unsigned int)sub_10030225();
    v5 = sub_10038eb3(/* unsupported instruction */ - 2032, v4, 0, v4);
    v2 = v3;
    if (g_10080ba6 == 2 && v2 != 3)
        return v5;
    if (!v5)
        return v6;
    v6 = v5;
    if (!v6)
    {
        return v6;
    }
    else if (v6->field_88 < /* unsupported instruction */ - 2032)
    {
        v0 = v6;
        lstrcpy(/* unsupported instruction */ - 2032, "exura sio \"");
        lstrcat(/* unsupported instruction */ - 2032, &v6->padding_0[4]);
        g_100f9328 = 1;
        return sub_10039413(/* unsupported instruction */ - 2032);
    }
    else
    {
        return v6;
    }
}
```

## `sub_1003295a` `0x1003295a`

_77 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_100433ff;
extern unsigned short g_10043401;
extern char g_10043403;
extern unsigned short g_10043404;
extern char g_10043406;
extern char g_10043407;
extern unsigned int g_1005f85c;

int sub_1003295a(void)
{
    unsigned short v3;  // bx
    unsigned int v4;  // eax
    unsigned short v5;  // dx
    char v6;  // cl
    unsigned int v0;  // [bp-0x4]
    unsigned int v2;  // [bp+0x100000]

    v3 = v2;
    v4 = sub_1002be32(sub_100300ce());
    if (!v4)
        return v4;
    g_100433ff = v4;
    g_10043401 = v3;
    g_10043403 = g_1005f85c;
    g_10043404 = v5;
    g_10043406 = v6;
    g_10043407 = 1;
    v0 = 12;
    return sub_1002ade7("\n");
}
```

## `sub_100329a7` `0x100329a7`

_97 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_100433ff;
extern unsigned short g_10043401;
extern char g_10043403;
extern unsigned short g_10043404;
extern char g_10043406;
extern char g_10043407;
extern unsigned int g_1005f85c;

int sub_100329a7(void)
{
    unsigned int v2;  // eax
    unsigned short v3;  // dx
    char v4;  // cl
    unsigned int v0;  // [bp-0x4]

    sub_10030225();
    v2 = sub_1002be32(sub_10036daf());
    if (!v2)
        return v2;
    g_100433ff = v2;
    *((int *)&g_10043401) = /* unsupported instruction */ - 2032;
    g_10043403 = g_1005f85c;
    g_10043404 = v3;
    g_10043406 = v4;
    g_10043407 = sub_10038d20();
    v0 = 12;
    return sub_1002ade7("\n");
}
```

## `sub_10032a08` `0x10032a08`

_30 bytes. (leaf/helper — see body)_

```c
int sub_10032a08(void)
{
    sub_10030225();
    return sub_1000954e(/* unsupported instruction */ - 2032);
}
```

## `sub_10032a26` `0x10032a26`

_69 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_1004340b;
extern unsigned short g_1004340d;
extern char g_1004340f;
extern unsigned short g_10043410;
extern char g_10043412;
extern char g_10043413;

int sub_10032a26(void)
{
    unsigned short v2;  // ax
    unsigned int v0;  // [bp-0x4]

    v2 = sub_100300ce();
    g_1004340b = 65535;
    g_1004340d = 0;
    g_1004340f = 0;
    g_10043410 = v2;
    g_10043412 = 0;
    g_10043413 = 1;
    v0 = 12;
    return sub_1002ade7("\n");
}
```

## `sub_10032a6b` `0x10032a6b`

_96 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_100433ff;
extern unsigned short g_10043401;
extern char g_10043403;
extern unsigned short g_10043404;
extern char g_10043406;
extern char g_10043407;

int sub_10032a6b(void)
{
    unsigned int v2;  // eax
    int v3;  // eax
    char v4;  // dl
    unsigned int v0;  // [bp-0x10]

    g_100433ff = sub_100300ce();
    g_10043401 = sub_100300ce();
    v2 = sub_100300ce();
    g_10043403 = v2;
    v3 = sub_1003a065(g_100433ff, g_10043401, v2);
    if (!v3)
        return v3;
    g_10043404 = v3;
    g_10043406 = v4;
    g_10043407 = 1;
    v0 = 12;
    return sub_1002ade7("\n");
}
```

## `sub_10032acb` `0x10032acb`

_99 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_100433ff;
extern unsigned short g_10043401;
extern char g_10043403;
extern unsigned short g_10043404;
extern char g_10043406;
extern char g_10043407;

int sub_10032acb(void)
{
    unsigned int v2;  // eax
    int v3;  // eax
    char v4;  // dl
    unsigned int v0;  // [bp-0x10]

    g_100433ff = sub_100300ce();
    g_10043401 = sub_100300ce();
    v2 = sub_100300ce();
    g_10043403 = v2;
    v3 = sub_1003a065(g_100433ff, g_10043401, v2);
    if (!v3)
        return v3;
    g_10043404 = v3;
    g_10043406 = v4;
    g_10043407 = sub_10038d20();
    v0 = 12;
    return sub_1002ade7("\n");
}
```

## `sub_10032b2e` `0x10032b2e`

_82 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f0e18;
extern char g_100f0e42;

unsigned int sub_10032b2e(void)
{
    unsigned int v3;  // eax
    unsigned int v1;  // [bp+0xffffc]
    unsigned int v2;  // [bp+0x100010]

    sub_10030225();
    v1 = sub_10036daf();
    while (true)
    {
        v3 = sub_100374ba();
        if (v3 != 2)
        {
            return v3;
        }
        else if (v2 != 4294967295)
        {
            return v3;
        }
        else if (g_100f0e42)
        {
            Sleep(300);
            g_100f0e18 = 0;
        }
        else
        {
            return v3;
        }
    }
}
```

## `sub_10032b80` `0x10032b80`

_118 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_10043414;
extern unsigned short g_1004341c;
extern unsigned short g_1004341f;
extern unsigned short g_10043421;
extern char g_10043423;
extern unsigned short g_10043424;
extern char g_10043426;
extern unsigned int g_1005f85c;
extern unsigned int g_100f0dfc;

int sub_10032b80(void)
{
    unsigned short v3;  // bx
    int v4;  // eax
    int v5;  // eax
    int v6;  // ecx
    char v7;  // dl
    unsigned int v0;  // [bp-0x8]
    unsigned int v2;  // [bp+0x100000]

    v3 = v2;
    sub_100300ce();
    v4 = sub_100377cb();
    g_100f0dfc = 0;
    v5 = v4;
    if (!v5)
        return v5;
    g_100f0dfc = 12;
    g_1004341c = 5908;
    g_1004341f = v5;
    g_10043421 = v3;
    g_10043423 = g_1005f85c;
    g_10043424 = v6;
    g_10043426 = v7;
    if (((char)sub_1003c4fa(v6) & 16))
        g_10043426 = 1;
    v0 = 19;
    return sub_1002ade7(&g_10043414);
}
```

## `sub_10032bf6` `0x10032bf6`

_118 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_10043414;
extern unsigned short g_1004341c;
extern unsigned short g_1004341f;
extern unsigned short g_10043421;
extern char g_10043423;
extern unsigned short g_10043424;
extern char g_10043426;
extern unsigned int g_1005f85c;
extern unsigned int g_100f0dfc;

int sub_10032bf6(void)
{
    unsigned short v3;  // bx
    int v4;  // eax
    int v5;  // eax
    int v6;  // ecx
    char v7;  // dl
    unsigned int v0;  // [bp-0x8]
    unsigned int v2;  // [bp+0x100000]

    v3 = v2;
    sub_100300ce();
    v4 = sub_100377cb();
    g_100f0dfc = 0;
    v5 = v4;
    if (!v5)
        return v5;
    g_100f0dfc = 12;
    g_1004341c = 5942;
    g_1004341f = v5;
    g_10043421 = v3;
    g_10043423 = g_1005f85c;
    g_10043424 = v6;
    g_10043426 = v7;
    if (((char)sub_1003c4fa(v6) & 16))
        g_10043426 = 1;
    v0 = 19;
    return sub_1002ade7(&g_10043414);
}
```

## `sub_10032c6c` `0x10032c6c`

_50 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1028987c;

unsigned int sub_10032c6c(void)
{
    unsigned int v3;  // eax
    unsigned int v1;  // [bp+0xffff8]
    unsigned int v2;  // [bp+0xffffc]

    v2 = sub_100300ce();
    v1 = sub_100300ce();
    v3 = sub_100300ce();
    g_1028987c = 0;
    return sub_100147eb(v2, v1, v3);
}
```

## `sub_10032c9e` `0x10032c9e`

_27 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern unsigned int g_1005f85c;

unsigned int sub_10032c9e(void)
{
    return sub_100265d3(g_1005f854, g_1005f858, g_1005f85c);
}
```

## `sub_10032cb9` `0x10032cb9`

_19 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_64cca4;

int sub_10032cb9(void)
{
    g_64cca4 = sub_100300ce();
    return g_64cca4;
}
```

## `sub_10032ccc` `0x10032ccc`

_101 bytes. (leaf/helper — see body)_

```c
extern char g_1014f420;
extern char g_101d5e20;

int sub_10032ccc(void)
{
    unsigned int v2;  // eax
    char *i;  // ebx
    char v1;  // [bp+0xff023]

    sub_10030225();
    v2 = (unsigned int)sub_10030225();
    for (i = &g_1014f420; i < &g_101d5e20; i += 4308)
    {
        if (!*(i))
            return v2;
        v2 = lstrcmpi(/* unsupported instruction */ - 2032, i);
        if (!v2)
        {
            v1 = 0;
            return lstrcpy(i + 32, /* unsupported instruction */ - 0x1000);
        }
    }
    return v2;
}
```

## `sub_10032d31` `0x10032d31`

_124 bytes. (leaf/helper — see body)_

```c
extern char g_1008a90b;
extern char g_1008a98b;
extern char g_1014f420;
extern char g_101d5e20;

int sub_10032d31(void)
{
    int v3;  // eax
    char *i;  // ebx
    int idx;  // eax
    char v6;  // cl
    int v1;  // [bp+0xffff8]
    int v2;  // [bp+0xffffc]

    sub_10030225();
    v3 = sub_100300ce() / 100;
    if (v3 > 250)
        v3 = 250;
    v1 = v3;
    v2 = 0;
    for (i = &g_1014f420; i < &g_101d5e20; i += 4308)
    {
        if (!*(i))
            return v3;
        v3 = lstrcmpi(/* unsupported instruction */ - 2032, i);
        if (!v3)
        {
            idx = v2;
            v6 = v1;
            (&g_1008a90b)[idx] = v6;
            (&g_1008a98b)[idx] = v6;
            return idx;
        }
        v2 += 1;
    }
    return v3;
}
```

## `sub_10032dad` `0x10032dad`

_211 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[96];
    unsigned int field_60;
    unsigned int field_64;
    unsigned int field_68;
    unsigned int field_6c;
    unsigned int field_70;
    unsigned int field_74;
} struct_0;

extern struct_0 *g_1005f7ed;

struct_0 * sub_10032dad(void)
{
    unsigned int v10;  // edi
    struct_0 *v11;  // eax
    unsigned int v12;  // eax
    unsigned int v13;  // eax
    unsigned int v14;  // eax
    unsigned int v15;  // eax
    struct_0 *v16;  // eax
    struct_0 *idx;  // ebx
    unsigned int v18;  // edx
    unsigned int v0;  // [bp-0x4]
    unsigned int v1;  // [bp-0x2]
    char v3;  // [bp+0xff814]
    unsigned int v4;  // [bp+0xfffec]
    unsigned int v5;  // [bp+0xffff0]
    unsigned int v6;  // [bp+0xffff4]
    unsigned int v7;  // [bp+0xffff8]
    struct_0 *v8;  // [bp+0xffffc]
    int v9;  // [bp+0x100000]

    sub_10030225();
    v10 = /* unsupported instruction */ - 2032;
    if (!v3 || v3 >= 48 && v3 <= 57)
    {
        v8 = g_1005f7ed;
    }
    else
    {
        v11 = sub_100399af(/* unsupported instruction */ - 2032, v9);
        if (!v11)
            return v11;
        v8 = v11;
    }
    v12 = sub_100300ce();
    if (v12 > 132)
        v12 = 132;
    v7 = v12;
    v13 = sub_100300ce();
    if (v13 > 132)
        v13 = 132;
    v6 = v13;
    v14 = sub_100300ce();
    if (v14 > 132)
        v14 = 132;
    v5 = v14;
    v15 = sub_100300ce();
    if (v15 > 132)
        v15 = 132;
    v4 = v15;
    v16 = sub_100300ce();
    if (v16 > 0x3)
        return sub_10032e52();
    idx = v8;
    if (!idx->field_60)
        return v16;
    v0 = v7;
    idx->field_64 = v7;
    v0 = v6;
    idx->field_68 = v6;
    v0 = v5;
    idx->field_6c = v5;
    v0 = v4;
    idx->field_70 = v4;
    if (v18)
    {
        v1 = _INSERT(v4, 0, *((unsigned short *)&v16));
        idx->field_74 = v1;
    }
    return v16;
}
```

## `sub_10032e52` `0x10032e52`

_5 bytes. (leaf/helper — see body)_

```c
int sub_10032e52(void)
{
}
```

## `sub_10032e85` `0x10032e85`

_188 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[96];
    struct struct_0 *field_60;
} struct_0;

extern struct_0 *g_1005f7ed;
extern int g_100f4d09;
extern int g_100f78e9;

struct_0 * sub_10032e85(void)
{
    char *v6;  // edi
    struct_0 *v7;  // eax
    int v8;  // ebx
    struct_0 *v9;  // ecx
    struct_0 *v10;  // eax
    struct_0 *v11;  // eax
    char *v0;  // [bp-0x8], Other Possible Types: struct_0 *
    struct_0 *v1;  // [bp-0x4]
    char v3;  // [bp+0xff004]
    struct_0 *v5;  // [bp+0xffffc]

    sub_10030225();
    sub_10030225();
    if (!v3)
    {
        v6 = /* unsupported instruction */ - 2032;
        v7 = g_1005f7ed;
        if (!g_1005f7ed)
            return g_1005f7ed;
    }
    else
    {
        v7 = sub_100399af(/* unsupported instruction */ - 2032);
        if (!v7)
            return v7;
        v6 = /* unsupported instruction */ - 0x1000;
    }
    v5 = v7;
    if (!*(v6) || *(v6) >= 48 && *(v6) <= 57)
    {
        v10 = sub_10040900(v6);
    }
    else
    {
        v8 = &g_100f4d09;
        v9 = NULL;
        while (true)
        {
            if (v8 > &g_100f78e9)
                return v7;
            v1 = v9;
            v0 = v6;
            v7 = lstrcmpi(v8, v6);
            v6 = v0;
            if (!v7)
                break;
            v8 += 32;
            v9 = &v9->padding_0[1];
        }
        v10 = v9;
    }
    if (v10 <= NULL)
    {
        return v10;
    }
    else if (v10 <= 0x15f)
    {
        v1 = v10;
        v0 = v10;
        v11 = 5259024();
        if (v11 != 0x4)
            return v11;
        v5->field_60 = v10;
        return v11;
    }
    else
    {
        return v10;
    }
}
```

## `sub_10032ebc` `0x10032ebc`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10032ebc(void)
{
}
```

## `sub_10032f46` `0x10032f46`

_105 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[96];
    unsigned int field_60;
    struct struct_0 *field_64;
} struct_0;

extern struct_0 *g_1005f7ed;

struct_0 * sub_10032f46(void)
{
    int v3;  // edi
    struct_0 *v4;  // eax
    struct_0 *idx;  // ebx
    struct_0 *v6;  // eax
    char v1;  // [bp+0xff004]

    sub_10030225();
    sub_10030225();
    if (!v1)
    {
        v3 = /* unsupported instruction */ - 2032;
        v4 = g_1005f7ed;
    }
    else
    {
        v4 = sub_100399af(/* unsupported instruction */ - 2032);
        v3 = /* unsupported instruction */ - 0x1000;
    }
    if (!v4)
        return v4;
    idx = v4;
    v6 = sub_10040900(v3);
    if (v6 < 0x64)
        return v6;
    if (v6 > 0x28ed)
        return v6;
    idx->field_60 = 0;
    idx->field_64 = v6;
    return v6;
}
```

## `sub_10032f75` `0x10032f75`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10032f75(void)
{
}
```

## `sub_10032fb1` `0x10032fb1`

_220 bytes. refs "enemy", "subenemy", "friend"_

```c
int sub_10032fb1(void)
{
    unsigned int v2;  // eax
    int v3;  // eax
    char idx[142];  // ebx
    char v5;  // al
    int v6;  // eax
    int v7;  // eax
    int v8;  // eax
    int v9;  // eax
    unsigned int v1;  // [bp+0xffffc]

    sub_10030225();
    sub_10030225();
    v2 = sub_100300ce();
    if (v2 > 2)
        v2 = 2;
    v1 = v2;
    v3 = sub_100399af(/* unsupported instruction */ - 2032);
    if (!v3)
        return v3;
    idx = sub_10023861();
    v5 = v1;
    idx[140] = 0;
    idx[141] = v5;
    v6 = lstrcmpi(/* unsupported instruction */ - 0x1000, "enemy");
    if (!v6)
    {
        idx[140] = 1;
        return v6;
    }
    v7 = lstrcmpi(/* unsupported instruction */ - 0x1000, "subenemy");
    if (!v7)
    {
        idx[140] = 2;
        return v7;
    }
    v8 = lstrcmpi(/* unsupported instruction */ - 0x1000, "friend");
    if (!v8)
    {
        idx[140] = 3;
        return v8;
    }
    v9 = lstrcmpi(/* unsupported instruction */ - 0x1000, "subfriend");
    if (v9)
        return v9;
    idx[140] = 4;
    return v9;
}
```

## `sub_1003308d` `0x1003308d`

_17 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f931c;

int sub_1003308d(void)
{
    g_100f931c = sub_100300ce();
    return g_100f931c;
}
```

## `sub_1003309e` `0x1003309e`

_52 bytes. refs "%lX %lX"_

```c
int sub_1003309e(void)
{
    unsigned int v3;  // ecx
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v1 = v3;
    v0 = sub_1003c4fa(sub_100300ce());
    wsprintfA(/* unsupported instruction */ - 2032, "%lX %lX");
    return sub_10039374(/* unsupported instruction */ - 2032);
}
```

## `sub_100330d2` `0x100330d2`

_73 bytes. refs "%lX"_

```c
int sub_100330d2(void)
{
    unsigned int v4;  // eax
    unsigned int v0;  // [bp-0x10]
    unsigned int v2;  // [bp+0xffff8]
    unsigned int v3;  // [bp+0xffffc]

    v3 = sub_100300ce();
    v2 = sub_100300ce();
    v4 = sub_100300ce();
    v0 = sub_1003a03f(v3, v2, v4);
    wsprintfA(/* unsupported instruction */ - 2032, "%lX");
    return sub_10039374(/* unsupported instruction */ - 2032);
}
```

## `sub_1003311b` `0x1003311b`

_30 bytes. refs "utana vid"_

```c
typedef struct struct_0 {
    char padding_0[96];
    unsigned int field_60;
} struct_0;

extern struct_0 *g_1005f7ed;

void sub_1003311b(void)
{
    if (g_1005f7ed && g_1005f7ed->field_60)
        sub_10039413("utana vid");
    return;
}
```

## `sub_10033139` `0x10033139`

_123 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f0e18;
extern char g_100f0e42;
extern unsigned int g_100f49f9;

int sub_10033139(void)
{
    unsigned int v4;  // eax
    unsigned int v5;  // eax
    unsigned int v6;  // eax
    unsigned int v7;  // eax
    unsigned int v1;  // [bp+0xffff8]
    unsigned int v2;  // [bp+0xffffc]
    unsigned int v3;  // [bp+0x100010]

    v4 = sub_100300ce();
    v2 = v4;
    sub_10030225();
    v5 = sub_10036daf(v4);
    if (v5 == 4294967294)
        return v5;
    v2 = v5;
    v1 = v4;
    while (true)
    {
        g_100f49f9 = 0;
        v6 = sub_100371fd();
        if (!v6)
        {
            return v6;
        }
        else if (v3 != 4294967295)
        {
            return v6;
        }
        else if (g_100f0e42)
        {
            v7 = (unsigned int)Sleep(300);
            g_100f0e18 = 0;
            if (g_100f49f9)
                return v7;
        }
        else
        {
            return v6;
        }
    }
}
```

## `sub_100331b4` `0x100331b4`

_57 bytes. (leaf/helper — see body)_

```c
void sub_100331b4(void)
{
    unsigned int v0;  // [bp-0x4]
    unsigned int v2;  // [bp+0xffffc]

    v0 = sub_100300ce();
    v2 = sub_100300ce();
    sub_10030225();
    if (sub_10036daf() != 4294967294)
        sub_100371fd();
    return;
}
```

## `sub_100331ed` `0x100331ed`

_200 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f0e18;
extern char g_100f0e42;
extern unsigned int g_100f49f5;

int sub_100331ed(void)
{
    unsigned int v7;  // eax
    unsigned int v8;  // eax
    unsigned int v9;  // eax
    unsigned int v10;  // eax
    unsigned int v11;  // eax
    unsigned int v1;  // [bp+0xfffec]
    unsigned int v2;  // [bp+0xffff0]
    unsigned int v3;  // [bp+0xffff4]
    unsigned int v4;  // [bp+0xffff8]
    unsigned int v5;  // [bp+0xffffc]
    unsigned int v6;  // [bp+0x100010]

    v5 = sub_100300ce();
    v3 = sub_100300ce();
    v7 = sub_100300ce();
    v1 = v7;
    v8 = v7;
    if (v8)
        v8 -= 1;
    v2 = v8;
    sub_10030225();
    v9 = sub_10036daf();
    if (v9 == 4294967294)
        return v9;
    v4 = v9;
    g_100f49f5 = 0;
    while (true)
    {
        v10 = sub_10037384();
        if (!v10)
        {
            return v10;
        }
        else if (v6 != 4294967295)
        {
            return v10;
        }
        else if (g_100f0e42)
        {
            v11 = (unsigned int)Sleep(300);
            g_100f0e18 = 0;
            if (g_100f49f5 && g_100f0e42)
            {
                if (!v1)
                {
                    v2 += 1;
                    Sleep(500);
                    g_100f0e18 = 0;
                    g_100f49f5 = 0;
                }
                else
                {
                    return v11;
                }
            }
        }
        else
        {
            return v10;
        }
    }
}
```

## `sub_100332af` `0x100332af`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100332af(void)
{
}
```

## `sub_100332b7` `0x100332b7`

_50 bytes. (leaf/helper — see body)_

```c
void sub_100332b7(void)
{
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x4]

    v0 = sub_100300ce();
    v2 = sub_100300ce();
    sub_10030225();
    sub_10036daf(v2);
    sub_10037100();
    return;
}
```

## `sub_100332e9` `0x100332e9`

_60 bytes. (leaf/helper — see body)_

```c
extern char g_100434d7;
extern char g_100434d9;
extern unsigned short g_100434da;
extern char g_100434dc;
extern char g_100434dd;

int sub_100332e9(void)
{
    unsigned int v0;  // [bp-0x4]

    g_100434d7 = 3;
    g_100434d9 = 0;
    g_100434dc = 0;
    g_100434da = *((int *)0x64ccb0);
    g_100434dd = sub_10038d20();
    v0 = 12;
    return sub_1002ade7("\n");
}
```

## `sub_10033325` `0x10033325`

_60 bytes. (leaf/helper — see body)_

```c
extern char g_100434d7;
extern char g_100434d9;
extern unsigned short g_100434da;
extern char g_100434dc;
extern char g_100434dd;

int sub_10033325(void)
{
    unsigned int v0;  // [bp-0x4]

    g_100434d7 = 10;
    g_100434d9 = 0;
    g_100434dc = 0;
    g_100434da = *((int *)0x64cd04);
    g_100434dd = sub_10038d20();
    v0 = 12;
    return sub_1002ade7("\n");
}
```

## `sub_10033361` `0x10033361`

_90 bytes. (leaf/helper — see body)_

```c
int sub_10033361(void)
{
    int v5;  // eax
    unsigned int v0;  // [bp-0x4]
    unsigned int i;  // [bp+0xfef4c]
    unsigned int v3;  // [bp+0xff814]
    char v4;  // [bp+0xff817]

    i = 0;
    while (i < 16)
    {
        if (*((int *)(i * 492 + 6606096)))
        {
            v3 = 8847362;
            v4 = i;
            v0 = 4;
            v5 = sub_1002ade7(/* unsupported instruction */ - 2032);
            *((unsigned int *)(/* unsupported instruction */ - 4280)) = i + 1;
        }
        else
        {
            i += 1;
        }
    }
    return v5;
}
```

## `sub_100333bb` `0x100333bb`

_114 bytes. (leaf/helper — see body)_

```c
extern char g_100f45bc;
extern unsigned int g_100f9318;
extern char g_100f9326;

int sub_100333bb(void)
{
    int v5;  // eax
    unsigned int v0;  // [bp-0x4]
    unsigned int i;  // [bp+0xfef4c]
    unsigned int v3;  // [bp+0xff814]
    char v4;  // [bp+0xff817]

    i = 0;
    while (i < 16)
    {
        if (*((int *)(i * 492 + 6606096)))
        {
            v3 = 8847362;
            v4 = i;
            v0 = 4;
            v5 = sub_1002ade7(/* unsupported instruction */ - 2032);
            *((unsigned int *)(/* unsupported instruction */ - 4280)) = i + 1;
        }
        else
        {
            i += 1;
        }
    }
    g_100f9318 = 0;
    g_100f45bc = 6;
    g_100f9326 = 1;
    return v5;
}
```

## `sub_1003342d` `0x1003342d`

_17 bytes. (leaf/helper — see body)_

```c
void sub_1003342d(void)
{
    sub_10030225();
    return;
}
```

## `sub_1003343e` `0x1003343e`

_17 bytes. (leaf/helper — see body)_

```c
void sub_1003343e(void)
{
    sub_10030225();
    return;
}
```

## `sub_1003344f` `0x1003344f`

_17 bytes. (leaf/helper — see body)_

```c
void sub_1003344f(void)
{
    sub_10030225();
    return;
}
```

## `sub_10033460` `0x10033460`

_17 bytes. (leaf/helper — see body)_

```c
void sub_10033460(void)
{
    sub_10030225();
    return;
}
```

## `sub_10033471` `0x10033471`

_53 bytes. (leaf/helper — see body)_

```c
void sub_10033471(void)
{
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x4]

    v0 = sub_100300ce();
    v2 = sub_100300ce();
    sub_10030225();
    sub_10036daf(v2);
    sub_10037100();
    return;
}
```

## `sub_100334a6` `0x100334a6`

_193 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_10043427;
extern unsigned short g_1004342a;
extern unsigned short g_1004342c;
extern char g_1004342e;
extern unsigned short g_1004342f;
extern char g_10043431;
extern unsigned short g_10043432;
extern unsigned short g_10043434;
extern char g_10043436;
extern unsigned short g_10043437;
extern char g_10043439;

int sub_100334a6(void)
{
    int v3;  // ebx
    unsigned int v4;  // eax
    char v5;  // dl
    unsigned int v6;  // eax
    int v7;  // eax
    unsigned int v8;  // eax
    unsigned int v0;  // [bp-0x20]
    int v2;  // [bp+0x100000]

    v3 = v2;
    g_1004342a = sub_100300ce();
    g_1004342c = sub_100300ce();
    v4 = sub_100300ce();
    g_1004342e = v4;
    g_1004342f = sub_1003a065(g_1004342a, g_1004342c, v4, v3);
    g_10043431 = v5;
    g_10043432 = sub_100300ce();
    g_10043434 = sub_100300ce();
    v6 = sub_100300ce();
    g_10043436 = v6;
    v7 = sub_1003a065(g_10043432, g_10043434, v6);
    if (!v7)
        return v7;
    g_10043437 = v7;
    g_10043439 = v5;
    v8 = sub_1003c4fa(v7);
    if (v8 != 0x30003000 && v8 != 536879112 && ((char)v8 & 16))
        g_10043439 = 1;
    v0 = 19;
    return sub_1002ade7(&g_10043427);
}
```

## `sub_10033567` `0x10033567`

_178 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_10043414;
extern char g_10043419;
extern char g_1004341b;
extern unsigned short g_1004341c;
extern char g_1004341e;
extern unsigned short g_1004341f;
extern unsigned short g_10043421;
extern char g_10043423;
extern unsigned short g_10043424;
extern char g_10043426;

int sub_10033567(void)
{
    unsigned int v2;  // eax
    unsigned int v3;  // eax
    char v4;  // dl
    unsigned int v5;  // eax
    unsigned int v6;  // eax
    unsigned int v0;  // [bp-0x14]

    g_1004341c = sub_100300ce();
    g_1004341f = sub_100300ce();
    g_10043421 = sub_100300ce();
    v2 = sub_100300ce();
    g_10043423 = v2;
    v3 = sub_1003a065(g_1004341f, g_10043421, v2);
    if (!v3)
        return v3;
    g_10043424 = v3;
    g_10043426 = v4;
    v5 = sub_1003c4fa(v3);
    if (v5 == 0x30003000 || v5 == 536879112)
    {
        v6 = sub_1002ae92(g_1004341c, 0, NULL);
        if (!v6)
            return v6;
        g_10043419 = v6;
        g_1004341b = v4;
        g_1004341e = v4;
    }
    else if (((char)v5 & 16))
    {
        g_10043426 = 1;
    }
    v0 = 19;
    return sub_1002ade7(&g_10043414);
}
```

## `sub_10033619` `0x10033619`

_192 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_10043414;
extern unsigned short g_1004341c;
extern unsigned short g_1004341f;
extern unsigned short g_10043421;
extern char g_10043423;
extern unsigned short g_10043424;
extern char g_10043426;
extern unsigned int g_100f0e18;
extern char g_100f0e42;

int sub_10033619(void)
{
    unsigned int v4;  // eax
    char v5;  // dl
    unsigned int v6;  // eax
    unsigned int i;  // ebx
    unsigned int v0;  // [bp-0x14]
    unsigned int v2;  // [bp+0xffffc]
    unsigned int v3;  // [bp+0x100010]

    g_1004341c = sub_100300ce();
    v2 = sub_100300ce();
    g_1004341f = sub_100300ce();
    g_10043421 = sub_100300ce();
    g_10043423 = sub_100300ce();
    while (true)
    {
        v4 = sub_1003a065(g_1004341f, g_10043421, g_10043423);
        if (v4 != v2)
            return v4;
        g_10043424 = v4;
        g_10043426 = v5;
        if (((char)sub_1003c4fa(v4) & 16))
            g_10043426 = 1;
        v0 = 19;
        v6 = sub_1002ade7(&g_10043414);
        if (v3 != 4294967295)
            return v6;
        for (i = 0; i < 500; i += 100)
        {
            if (!g_100f0e42)
                return v6;
            v6 = (unsigned int)Sleep(100);
            g_100f0e18 = 0;
        }
    }
}
```

