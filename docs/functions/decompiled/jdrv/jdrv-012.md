# elfbot.dll decompiled — jdrv 0x10030d0e..0x100322d1

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10030d0e` `0x10030d0e`

_66 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f9328;

int sub_10030d0e(void)
{
    int v1;  // eax

    g_100f9328 = 0;
    sub_10030225();
    v1 = sub_10038eb3(/* unsupported instruction */ - 2032, 0, 0);
    if (!v1)
        return v1;
    g_100f9328 = 1;
    return sub_1003a60a(v1, 4);
}
```

## `sub_10030d50` `0x10030d50`

_80 bytes. (leaf/helper — see body)_

```c
extern char g_100f0e41;
extern unsigned int g_100f0e54;
extern unsigned int g_100f0e5c;
extern unsigned int g_100f0e60;
extern unsigned int g_100f0e64;
extern unsigned int g_100f0e70;
extern unsigned int g_100f0e74;

void sub_10030d50(void)
{
    if (!g_100f0e41)
    {
        g_100f0e60 = 0;
        g_100f0e64 = 0;
        g_100f0e70 = 0;
        g_100f0e74 = 0;
        g_100f0e5c = 0;
        g_100f0e54 = 4294967295;
    }
    g_100f0e41 = 10;
    return;
}
```

## `sub_10030da0` `0x10030da0`

_80 bytes. (leaf/helper — see body)_

```c
extern char g_100f0e40;
extern unsigned int g_100f0e54;
extern unsigned int g_100f0e5c;
extern unsigned int g_100f0e60;
extern unsigned int g_100f0e64;
extern unsigned int g_100f0e70;
extern unsigned int g_100f0e74;

void sub_10030da0(void)
{
    if (!g_100f0e40)
    {
        g_100f0e60 = 0;
        g_100f0e64 = 0;
        g_100f0e70 = 0;
        g_100f0e74 = 0;
        g_100f0e5c = 0;
        g_100f0e54 = 4294967295;
    }
    g_100f0e40 = 10;
    return;
}
```

## `sub_10030df0` `0x10030df0`

_66 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f9328;

int sub_10030df0(void)
{
    int v1;  // eax

    g_100f9328 = 0;
    sub_10030225();
    v1 = sub_10038eb3(/* unsupported instruction */ - 2032, 0, 0);
    if (!v1)
        return v1;
    g_100f9328 = 1;
    return sub_1003a60a(v1, 1);
}
```

## `sub_10030e32` `0x10030e32`

_66 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f9328;

int sub_10030e32(void)
{
    int v1;  // eax

    g_100f9328 = 0;
    sub_10030225();
    v1 = sub_10038eb3(/* unsupported instruction */ - 2032, 0, 0);
    if (!v1)
        return v1;
    g_100f9328 = 1;
    return sub_1003a60a(v1, 14);
}
```

## `sub_10030e74` `0x10030e74`

_66 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f9328;

int sub_10030e74(void)
{
    int v1;  // eax

    g_100f9328 = 0;
    sub_10030225();
    v1 = sub_10038eb3(/* unsupported instruction */ - 2032, 0, 0);
    if (!v1)
        return v1;
    g_100f9328 = 1;
    return sub_1003a60a(v1, 3);
}
```

## `sub_10030eb6` `0x10030eb6`

_66 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f9328;

int sub_10030eb6(void)
{
    int v1;  // eax

    g_100f9328 = 0;
    sub_10030225();
    v1 = sub_10038eb3(/* unsupported instruction */ - 2032, 0, 0);
    if (!v1)
        return v1;
    g_100f9328 = 1;
    return sub_1003a60a(v1, 2);
}
```

## `sub_10030ef8` `0x10030ef8`

_70 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f9328;
extern int g_100f94cb;

int sub_10030ef8(void)
{
    int v1;  // eax

    g_100f9328 = 0;
    sub_10030225();
    v1 = sub_10038eb3(/* unsupported instruction */ - 2032, 0, 0);
    if (!v1)
        return v1;
    g_100f9328 = 1;
    return sub_1003a60a(v1, g_100f94cb);
}
```

## `sub_10030f3e` `0x10030f3e`

_66 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f9328;

int sub_10030f3e(void)
{
    int v1;  // eax

    g_100f9328 = 0;
    sub_10030225();
    v1 = sub_10038eb3(/* unsupported instruction */ - 2032, 0, 0);
    if (!v1)
        return v1;
    g_100f9328 = 1;
    return sub_1003a60a(v1, 5);
}
```

## `sub_10030f80` `0x10030f80`

_56 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f9328;
extern int g_100f94cb;

int sub_10030f80(void)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax

    g_100f9328 = 0;
    v1 = sub_100235e8(1);
    if (!v1)
        return v1;
    v2 = sub_1002355e();
    if (!v2)
        return v2;
    g_100f9328 = 1;
    return sub_1003a60a(v2, g_100f94cb);
}
```

## `sub_10030fb8` `0x10030fb8`

_109 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100432ba;
extern unsigned int g_100432be;
extern unsigned int g_100f9328;
extern unsigned int g_63da40;
extern unsigned int g_63fe60;
extern unsigned int g_63fe64;

unsigned int * sub_10030fb8(void)
{
    unsigned int *v2;  // eax
    unsigned int v3;  // eax
    unsigned int v0;  // [bp-0x10]

    g_100f9328 = 0;
    sub_10030225();
    v2 = sub_10038eb3(/* unsupported instruction */ - 2032, 200, 0);
    if (!v2)
        return v2;
    g_100432ba = *(v2);
    v3 = g_63da40;
    g_63da40 = g_63da40 + 1;
    g_100432be = v3;
    g_63fe64 = 0;
    g_63fe60 = g_100432ba;
    g_100f9328 = 1;
    v0 = 11;
    return sub_1002ade7("\t");
}
```

## `sub_10031025` `0x10031025`

_115 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100432af;
extern unsigned int g_100432b3;
extern unsigned int g_1008b89f;
extern unsigned int g_100f9328;
extern unsigned int g_63da40;
extern unsigned int g_63fe60;
extern unsigned int g_63fe64;

unsigned int * sub_10031025(void)
{
    unsigned int *v2;  // eax
    unsigned int v3;  // edx
    unsigned int v4;  // eax
    unsigned int v0;  // [bp-0x10]

    g_100f9328 = 0;
    sub_10030225();
    v2 = sub_10038eb3(/* unsupported instruction */ - 2032, 200, 0);
    if (!v2)
        return v2;
    v3 = *(v2);
    g_1008b89f = v3;
    g_100432af = v3;
    v4 = g_63da40;
    g_63da40 = g_63da40 + 1;
    g_100432b3 = v4;
    g_63fe64 = v3;
    g_63fe60 = 0;
    g_100f9328 = 1;
    v0 = 11;
    return sub_1002ade7("\t");
}
```

## `sub_10031098` `0x10031098`

_48 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
} struct_0;

extern unsigned int g_100f9355;

struct_0 ** sub_10031098(void)
{
    struct_0 **v1;  // eax

    sub_10030225();
    v1 = sub_10038eb3(/* unsupported instruction */ - 2032, 200, 0);
    if (v1)
        v1 = *(v1);
    g_100f9355 = v1;
    return v1;
}
```

## `sub_100310c8` `0x100310c8`

_125 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
} struct_0;

extern unsigned int g_100432af;
extern unsigned int g_100432b3;
extern unsigned int g_1008b89f;
extern unsigned int g_63da40;
extern unsigned int g_63fe60;
extern unsigned int g_63fe64;

struct_0 ** sub_100310c8(void)
{
    struct_0 **v2;  // eax
    unsigned int v3;  // eax
    unsigned int v0;  // [bp-0x10]

    sub_10030225();
    v2 = sub_10038eb3(/* unsupported instruction */ - 2032, 200, 0);
    if (!v2)
        return v2;
    *((char *)(sub_10023861(v2) + 139)) = 1;
    if (g_63fe64 != *(v2))
        return *(v2);
    g_63fe64 = 0;
    g_63fe60 = 0;
    g_100432af = 0;
    v3 = g_63da40;
    g_63da40 = g_63da40 + 1;
    g_100432b3 = v3;
    g_1008b89f = 0;
    v0 = 11;
    return sub_1002ade7("\t");
}
```

## `sub_10031145` `0x10031145`

_99 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100432af;
extern unsigned int g_100432b3;
extern unsigned int g_1008b89f;
extern unsigned int g_100f9328;
extern unsigned int g_63da40;
extern unsigned int g_63fe60;
extern unsigned int g_63fe64;

int sub_10031145(void)
{
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x4]

    g_100f9328 = 0;
    g_100432af = 0;
    v2 = g_63da40;
    g_63da40 = g_63da40 + 1;
    g_100432b3 = v2;
    g_1008b89f = 0;
    if (!g_63fe64 && !g_63fe60)
        return &g_63fe64;
    g_63fe64 = 0;
    g_63fe60 = 0;
    g_100f9328 = 1;
    v0 = 11;
    return sub_1002ade7("\t");
}
```

## `sub_100311a8` `0x100311a8`

_272 bytes. refs "offensive", "balanced", "defensive"_

```c
extern unsigned int g_799ce8;
extern unsigned int g_799cec;

int sub_100311a8(void)
{
    unsigned int v9;  // eax
    unsigned int v10;  // ebx
    unsigned int v0;  // [bp-0x4]
    unsigned short v2;  // [bp+0xff814]
    char v3;  // [bp+0xff816]
    char v4;  // [bp+0xff817]
    char v5;  // [bp+0xff818]
    char v6;  // [bp+0xff819]
    unsigned int v7;  // [bp+0xffff8]
    unsigned int v8;  // [bp+0xffffc]

    sub_10030225();
    v8 = g_799cec;
    if (!lstrcmpi(/* unsupported instruction */ - 2032, "offensive"))
        v8 = 1;
    if (!lstrcmpi(/* unsupported instruction */ - 2032, "balanced"))
        v8 = 2;
    if (!lstrcmpi(/* unsupported instruction */ - 2032, "defensive"))
        v8 = 3;
    sub_10030225();
    v7 = g_799ce8;
    if (!lstrcmpi(/* unsupported instruction */ - 2032, "stand"))
        v7 = 0;
    if (!lstrcmpi(/* unsupported instruction */ - 2032, "chase"))
        v7 = 1;
    v9 = v8;
    v10 = v7;
    if (v9 == g_799cec)
        return g_799cec;
    v2 = 4;
    v3 = 160;
    v4 = v9;
    v5 = v10;
    g_799cec = v9;
    g_799ce8 = v10;
    v6 = *((int *)0x799ce4);
    v0 = 6;
    return sub_1002ade7(/* unsupported instruction */ - 2032);
}
```

## `sub_100312b8` `0x100312b8`

_160 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[136];
    char field_88;
} struct_0;

extern char g_1005f7d1;
extern char g_1005f7d5;
extern struct_0 *g_1005f7ed;
extern unsigned int g_100f9328;
extern unsigned int g_100f9495;
extern unsigned int g_100f9499;
extern char g_100fa4f1;
extern char g_100fa531;
extern unsigned int g_100fa571;
extern char g_100fa575;

int sub_100312b8(void)
{
    unsigned int v1;  // ecx
    char v2;  // dl

    g_100f9328 = 0;
    if (g_1005f7ed->field_88 >= 95)
        return;
    if (g_100fa4f1 && g_100f9499 && *((int *)&g_1005f7d1) >= g_100f9499 && g_100f9495 && *((int *)&g_1005f7d5) >= g_100f9495)
    {
        sub_10039413(&g_100fa4f1);
    }
    else if (g_100fa531 && g_100fa571 && *((int *)&g_100fa575) && *((int *)&g_1005f7d5) >= *((int *)&g_100fa575))
    {
        sub_10039413(&g_100fa531);
    }
    else
    {
        sub_10024f39(v1, v2);
    }
    g_100f9328 = 1;
    return;
}
```

## `sub_10031358` `0x10031358`

_70 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_10043333;
extern char g_10043338;
extern char g_1004333a;
extern unsigned short g_1004333b;
extern char g_1004333d;

int sub_10031358(void)
{
    unsigned int v2;  // eax
    unsigned int v3;  // eax
    char v4;  // dl
    unsigned int v0;  // [bp-0x4]

    v2 = sub_100300ce();
    if (*((int *)6605988) == v2)
        return v2;
    g_1004333b = v2;
    v3 = sub_1002ae92(v2, 0, NULL);
    if (!v3)
        return v3;
    g_1004333a = v4;
    g_1004333d = v4;
    g_10043338 = v3;
    v0 = 0x11;
    return sub_1002ade7(&g_10043333);
}
```

## `sub_1003139e` `0x1003139e`

_61 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_10043333;
extern char g_10043338;
extern char g_1004333a;
extern unsigned short g_1004333b;
extern char g_1004333d;

int sub_1003139e(void)
{
    unsigned int v2;  // eax
    unsigned int v3;  // eax
    char v4;  // dl
    unsigned int v0;  // [bp-0x4]

    v2 = sub_100300ce();
    g_1004333b = v2;
    v3 = sub_1002ae92(v2, 0, NULL);
    if (!v3)
        return v3;
    g_1004333a = v4;
    g_1004333d = v4;
    g_10043338 = v3;
    v0 = 0x11;
    return sub_1002ade7(&g_10043333);
}
```

## `sub_100313db` `0x100313db`

_124 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_10008a26;
extern unsigned int g_10008a7e;
extern unsigned short g_10043344;
extern char g_10043349;
extern char g_1004334b;
extern unsigned short g_1004334c;
extern char g_1004334e;
extern char g_10043351;
extern char g_10043354;

int sub_100313db(void)
{
    unsigned int v2;  // eax
    unsigned int iter;  // ecx
    unsigned int v4;  // eax
    unsigned int v5;  // eax
    unsigned int v6;  // eax
    char v7;  // dl
    unsigned int v8;  // ecx
    unsigned int v9;  // ecx
    unsigned int v0;  // [bp-0x4]

    v2 = sub_100300ce();
    iter = &g_10008a26;
    while (true)
    {
        v4 = v2;
        if (iter >= &g_10008a7e)
            break;
        if (v2 == *((int *)iter) || v2 == *((int *)(iter + 4)))
        {
            v4 = *((int *)iter);
            v2 = *((int *)(iter + 4));
            break;
        }
        else
        {
            iter += 8;
        }
    }
    v5 = v4;
    if (*((int *)6606072) == v2)
        return v5;
    g_10043351 = 9;
    g_1004334c = v5;
    v6 = sub_1002ae92(v5, 0, NULL);
    if (!v6)
        return v6;
    g_1004334b = v7;
    g_1004334e = v7;
    g_10043349 = v6;
    v9 = v8;
    if (!v8)
        v9 += 1;
    g_10043354 = v9;
    v0 = 0x11;
    return sub_1002ade7(&g_10043344);
}
```

## `sub_10031457` `0x10031457`

_96 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_10043344;
extern char g_10043349;
extern char g_1004334b;
extern unsigned short g_1004334c;
extern char g_1004334e;
extern char g_10043351;
extern char g_10043354;

int sub_10031457(void)
{
    unsigned int v2;  // eax
    unsigned int v3;  // ebx
    unsigned int v4;  // eax
    char v5;  // dl
    unsigned int v6;  // ecx
    unsigned int v7;  // ecx
    unsigned int v0;  // [bp-0x4]

    v0 = sub_100300ce();
    v2 = sub_100300ce();
    v3 = sub_100300ce();
    if (*((int *)6606072) == v2)
        return v2;
    g_10043351 = 9;
    g_1004334c = v3;
    v4 = sub_1002ae92(v3, 0, NULL);
    if (!v4)
        return v4;
    g_1004334b = v5;
    g_1004334e = v5;
    g_10043349 = v4;
    v7 = v6;
    if (!v6)
        v7 += 1;
    g_10043354 = v7;
    v0 = 0x11;
    return sub_1002ade7(&g_10043344);
}
```

## `sub_100314b7` `0x100314b7`

_115 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_10043344;
extern char g_10043349;
extern char g_1004334b;
extern unsigned short g_1004334c;
extern char g_1004334e;
extern char g_10043351;
extern char g_10043354;

int sub_100314b7(void)
{
    unsigned int v2;  // eax
    unsigned int v3;  // eax
    char v4;  // dl
    unsigned int v5;  // ecx
    unsigned int v6;  // ecx
    unsigned int v0;  // [bp-0x4]

    v2 = sub_100300ce();
    if (v2 == 3549)
        v2 = 6529;
    if (*((int *)6606060) == v2)
        return v2;
    if (v2 == 6529 && *((int *)0x64ccec) == 3549)
        return v2;
    g_10043351 = 8;
    g_1004334c = v2;
    v3 = sub_1002ae92(v2, 0, NULL);
    if (!v3)
        return v3;
    g_1004334b = v4;
    g_1004334e = v4;
    g_10043349 = v3;
    v6 = v5;
    if (!v5)
        v6 += 1;
    g_10043354 = v6;
    v0 = 0x11;
    return sub_1002ade7(&g_10043344);
}
```

## `sub_1003152a` `0x1003152a`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_10043344;
extern char g_10043349;
extern char g_1004334b;
extern unsigned short g_1004334c;
extern char g_1004334e;
extern char g_10043351;
extern char g_10043354;

int sub_1003152a(void)
{
    unsigned int v2;  // eax
    unsigned int v3;  // eax
    char v4;  // dl
    unsigned int v5;  // ecx
    unsigned int v6;  // ecx
    unsigned int v0;  // [bp-0x4]

    v2 = sub_100300ce();
    if (*((int *)6605976) == v2)
        return v2;
    g_10043351 = 1;
    g_1004334c = v2;
    v3 = sub_1002ae92(v2, 0, NULL);
    if (!v3)
        return v3;
    g_1004334b = v4;
    g_1004334e = v4;
    g_10043349 = v3;
    v6 = v5;
    if (!v5)
        v6 += 1;
    g_10043354 = v6;
    v0 = 0x11;
    return sub_1002ade7(&g_10043344);
}
```

## `sub_10031582` `0x10031582`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_10043344;
extern char g_10043349;
extern char g_1004334b;
extern unsigned short g_1004334c;
extern char g_1004334e;
extern char g_10043351;
extern char g_10043354;

int sub_10031582(void)
{
    unsigned int v2;  // eax
    unsigned int v3;  // eax
    char v4;  // dl
    unsigned int v5;  // ecx
    unsigned int v6;  // ecx
    unsigned int v0;  // [bp-0x4]

    v2 = sub_100300ce();
    if (*((int *)6606012) == v2)
        return v2;
    g_10043351 = 4;
    g_1004334c = v2;
    v3 = sub_1002ae92(v2, 0, NULL);
    if (!v3)
        return v3;
    g_1004334b = v4;
    g_1004334e = v4;
    g_10043349 = v3;
    v6 = v5;
    if (!v5)
        v6 += 1;
    g_10043354 = v6;
    v0 = 0x11;
    return sub_1002ade7(&g_10043344);
}
```

## `sub_100315da` `0x100315da`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_10043344;
extern char g_10043349;
extern char g_1004334b;
extern unsigned short g_1004334c;
extern char g_1004334e;
extern char g_10043351;
extern char g_10043354;

int sub_100315da(void)
{
    unsigned int v2;  // eax
    unsigned int v3;  // eax
    char v4;  // dl
    unsigned int v5;  // ecx
    unsigned int v6;  // ecx
    unsigned int v0;  // [bp-0x4]

    v2 = sub_100300ce();
    if (*((int *)6605976) == v2)
        return v2;
    g_10043351 = 1;
    g_1004334c = v2;
    v3 = sub_1002ae92(v2, 0, NULL);
    if (!v3)
        return v3;
    g_1004334b = v4;
    g_1004334e = v4;
    g_10043349 = v3;
    v6 = v5;
    if (!v5)
        v6 += 1;
    g_10043354 = v6;
    v0 = 0x11;
    return sub_1002ade7(&g_10043344);
}
```

## `sub_10031632` `0x10031632`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_10043344;
extern char g_10043349;
extern char g_1004334b;
extern unsigned short g_1004334c;
extern char g_1004334e;
extern char g_10043351;
extern char g_10043354;

int sub_10031632(void)
{
    unsigned int v2;  // eax
    unsigned int v3;  // eax
    char v4;  // dl
    unsigned int v5;  // ecx
    unsigned int v6;  // ecx
    unsigned int v0;  // [bp-0x4]

    v2 = sub_100300ce();
    if (*((int *)6606048) == v2)
        return v2;
    g_10043351 = 7;
    g_1004334c = v2;
    v3 = sub_1002ae92(v2, 0, NULL);
    if (!v3)
        return v3;
    g_1004334b = v4;
    g_1004334e = v4;
    g_10043349 = v3;
    v6 = v5;
    if (!v5)
        v6 += 1;
    g_10043354 = v6;
    v0 = 0x11;
    return sub_1002ade7(&g_10043344);
}
```

## `sub_1003168a` `0x1003168a`

_124 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_10043344;
extern char g_10043349;
extern char g_1004334b;
extern unsigned short g_1004334c;
extern char g_1004334e;
extern char g_10043351;
extern char g_10043354;

int sub_1003168a(void)
{
    unsigned int v3;  // eax
    unsigned int v4;  // eax
    char v5;  // dl
    unsigned int v6;  // ecx
    unsigned int v7;  // ecx
    unsigned int v0;  // [bp-0x4]
    unsigned int v2;  // [bp+0xffffc]

    v0 = sub_100300ce();
    v2 = sub_100300ce();
    v3 = sub_100300ce();
    if (*((int *)6606036) == v3)
    {
        if (*((int *)0x64ccd8) <= 0)
        {
            return v3;
        }
        else if (*((int *)0x64ccd8) >= 100)
        {
            return v3;
        }
    }
    g_10043351 = 6;
    g_1004334c = v3;
    v4 = sub_1002ae92(v3, 0, NULL);
    if (!v4)
        return v4;
    g_1004334b = v5;
    g_1004334e = v5;
    g_10043349 = v4;
    v7 = v6;
    if (!v6)
        v7 += 1;
    if (v2 && v7 > v2)
        v7 = v2;
    g_10043354 = v7;
    v0 = 0x11;
    return sub_1002ade7(&g_10043344);
}
```

## `sub_10031706` `0x10031706`

_124 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_10043344;
extern char g_10043349;
extern char g_1004334b;
extern unsigned short g_1004334c;
extern char g_1004334e;
extern char g_10043351;
extern char g_10043354;

int sub_10031706(void)
{
    unsigned int v3;  // eax
    unsigned int v4;  // eax
    char v5;  // dl
    unsigned int v6;  // ecx
    unsigned int v7;  // ecx
    unsigned int v0;  // [bp-0x4]
    unsigned int v2;  // [bp+0xffffc]

    v0 = sub_100300ce();
    v2 = sub_100300ce();
    v3 = sub_100300ce();
    if (*((int *)6606024) == v3)
    {
        if (*((int *)0x64cccc) <= 0)
        {
            return v3;
        }
        else if (*((int *)0x64cccc) >= 100)
        {
            return v3;
        }
    }
    g_10043351 = 5;
    g_1004334c = v3;
    v4 = sub_1002ae92(v3, 0, NULL);
    if (!v4)
        return v4;
    g_1004334b = v5;
    g_1004334e = v5;
    g_10043349 = v4;
    v7 = v6;
    if (!v6)
        v7 += 1;
    if (v2 && v7 > v2)
        v7 = v2;
    g_10043354 = v7;
    v0 = 0x11;
    return sub_1002ade7(&g_10043344);
}
```

## `sub_10031782` `0x10031782`

_124 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_10043344;
extern char g_10043349;
extern char g_1004334b;
extern unsigned short g_1004334c;
extern char g_1004334e;
extern char g_10043351;
extern char g_10043354;

int sub_10031782(void)
{
    unsigned int v3;  // eax
    unsigned int v4;  // eax
    char v5;  // dl
    unsigned int v6;  // ecx
    unsigned int v7;  // ecx
    unsigned int v0;  // [bp-0x4]
    unsigned int v2;  // [bp+0xffffc]

    v0 = sub_100300ce();
    v2 = sub_100300ce();
    v3 = sub_100300ce();
    if (*((int *)6606084) == v3)
    {
        if (*((int *)0x64cd08) <= 0)
        {
            return v3;
        }
        else if (*((int *)0x64cd08) >= 100)
        {
            return v3;
        }
    }
    g_10043351 = 10;
    g_1004334c = v3;
    v4 = sub_1002ae92(v3, 0, NULL);
    if (!v4)
        return v4;
    g_1004334b = v5;
    g_1004334e = v5;
    g_10043349 = v4;
    v7 = v6;
    if (!v6)
        v7 += 1;
    if (v2 && v7 > v2)
        v7 = v2;
    g_10043354 = v7;
    v0 = 0x11;
    return sub_1002ade7(&g_10043344);
}
```

## `sub_100317fe` `0x100317fe`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_10043344;
extern char g_10043349;
extern char g_1004334b;
extern unsigned short g_1004334c;
extern char g_1004334e;
extern char g_10043351;
extern char g_10043354;

int sub_100317fe(void)
{
    unsigned int v2;  // eax
    unsigned int v3;  // eax
    char v4;  // dl
    unsigned int v5;  // ecx
    unsigned int v6;  // ecx
    unsigned int v0;  // [bp-0x4]

    v2 = sub_100300ce();
    if (*((int *)6606000) == v2)
        return v2;
    g_10043351 = 3;
    g_1004334c = v2;
    v3 = sub_1002ae92(v2, 0, NULL);
    if (!v3)
        return v3;
    g_1004334b = v4;
    g_1004334e = v4;
    g_10043349 = v3;
    v6 = v5;
    if (!v5)
        v6 += 1;
    g_10043354 = v6;
    v0 = 0x11;
    return sub_1002ade7(&g_10043344);
}
```

## `sub_10031856` `0x10031856`

_79 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f0e18;
extern char g_100f0e42;

int sub_10031856(void)
{
    unsigned int v2;  // eax
    unsigned int i;  // ebx
    unsigned int v1;  // [bp+0x100010]

    sub_10030225();
    v2 = sub_10039413(/* unsupported instruction */ - 2032);
    if (v1 != 4294967295)
        return v2;
    for (i = 0; i < 1100; i += 100)
    {
        if (!g_100f0e42)
            return v2;
        v2 = (unsigned int)Sleep(100);
        g_100f0e18 = 0;
    }
    return v2;
}
```

## `sub_100318a5` `0x100318a5`

_31 bytes. (leaf/helper — see body)_

```c
int sub_100318a5(void)
{
    unsigned int v2;  // ebx
    unsigned int v3;  // ebx
    unsigned int v4;  // eax
    unsigned int v1;  // [bp+0x100000]

    v2 = v1;
    while (true)
    {
        v3 = v2;
        v4 = sub_100300ce();
        if (!v4)
        {
            return v4;
        }
        else if (v4 >= 100)
        {
            sub_1003c496(v4, v3);
            v2 = v4;
        }
        else
        {
            return v4;
        }
    }
}
```

## `sub_100318c4` `0x100318c4`

_31 bytes. (leaf/helper — see body)_

```c
int sub_100318c4(void)
{
    unsigned int v2;  // ebx
    unsigned int v3;  // ebx
    unsigned int v4;  // eax
    unsigned int v1;  // [bp+0x100000]

    v2 = v1;
    while (true)
    {
        v3 = v2;
        v4 = sub_100300ce();
        if (!v4)
        {
            return v4;
        }
        else if (v4 >= 100)
        {
            sub_1003c4c8(v4, v3);
            v2 = v4;
        }
        else
        {
            return v4;
        }
    }
}
```

## `sub_100318e3` `0x100318e3`

_247 bytes. calls SendDlgItemMessageA; refs "defaultmessages", "playeronscreen", "gmdetected"_

```c
extern HWND g_10072f94;
extern char g_10207ac6;
extern char g_10207f12[3];
extern char g_10207f15[3];
extern char g_10207f18[3];
extern char g_10207f1b[3];
extern char g_10207f1e[3];

int sub_100318e3(void)
{
    unsigned int v2;  // eax
    char v3;  // al
    char v4;  // al
    unsigned int count;  // eax
    int i;  // ebx
    char idx[3];  // [bp+0xffffc]

    sub_10030225();
    if (!lstrcmpi(/* unsupported instruction */ - 2032, "defaultmessages"))
    {
        *((char **)&idx) = &g_10207f1b[0];
    }
    else if (!lstrcmpi(/* unsupported instruction */ - 2032, "playeronscreen"))
    {
        *((char **)&idx) = &g_10207f12[0];
    }
    else if (!lstrcmpi(/* unsupported instruction */ - 2032, "gmdetected"))
    {
        *((char **)&idx) = &g_10207f15[0];
    }
    else if (!lstrcmpi(/* unsupported instruction */ - 2032, "playerattacking"))
    {
        *((char **)&idx) = &g_10207f18[0];
    }
    else
    {
        v2 = lstrcmpi(/* unsupported instruction */ - 2032, "privatemessages");
        if (v2)
            return v2;
        *((char **)&idx) = &g_10207f1e[0];
    }
    v3 = sub_100300ce();
    idx[0] = v3;
    v4 = sub_100300ce();
    idx[1] = v4;
    count = sub_100300ce();
    idx[2] = count;
    for (i = 1100; i <= 1114; i += 1)
    {
        count = SendDlgItemMessageA(g_10072f94, i, 241, (&g_10207ac6)[i], NULL);
    }
    return count;
}
```

## `sub_100319da` `0x100319da`

_14 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100580f8;

void sub_100319da(void)
{
    g_100580f8 = 1;
    return;
}
```

## `sub_100319ea` `0x100319ea`

_11 bytes. (leaf/helper — see body)_

```c
void sub_100319ea(void)
{
    sub_10040318(1);
    return;
}
```

## `sub_100319f5` `0x100319f5`

_43 bytes. (leaf/helper — see body)_

```c
void sub_100319f5(void)
{
    char v1;  // [bp+0xff814]

    sub_10030225();
    if (v1)
        sub_10040318(0, /* unsupported instruction */ - 2032);
    else
        sub_10040318(0, 0);
    return;
}
```

## `sub_10031a20` `0x10031a20`

_289 bytes. refs "No change", "Any"_

```c
typedef struct struct_0 {
    char padding_0[33];
    char field_21;
} struct_0;

typedef struct struct_1 {
    char padding_0[16];
    char field_10;
} struct_1;

extern char g_10008a16;
extern int g_100424d2;
extern HWND g_10072f8c;
extern char g_100f4a05;
extern struct_0 g_101d5e78;
extern struct_0 g_101dfe78;

unsigned int sub_10031a20(void)
{
    int *i;  // ebx
    unsigned int v8;  // eax
    unsigned int v9;  // eax
    unsigned int j;  // ebx
    struct_0 *iter;  // ebx
    struct_1 *v12;  // ebx
    unsigned int v13;  // eax
    unsigned int v0;  // [bp-0x4]
    char v2;  // [bp+0xff004]
    unsigned int v3;  // [bp+0xffff4]
    unsigned int v4;  // [bp+0xffff8]
    unsigned int v5;  // [bp+0xffffc]
    unsigned int v6;  // [bp+0x100000]

    sub_10030225();
    sub_10030225();
    v0 = v6;
    v5 = 0;
    for (i = &g_100424d2; i < "No change"; i += 1)
    {
        if (!lstrcmpi(/* unsupported instruction */ - 0x1000, *(i)))
        {
            v5 = i - &g_100424d2 >> 2;
            break;
        }
    }
    v8 = sub_100300ce();
    if (!v8)
        v8 += 1;
    v3 = v8;
    v9 = (unsigned int)sub_10030225();
    v4 = 0;
    if (v2)
    {
        for (j = "Any"; j < &g_10008a16; j += 4)
        {
            if (!lstrcmpi(/* unsupported instruction */ - 0x1000, j))
            {
                v4 = (char *)(-268470766 + j) >> 2;
                break;
            }
        }
    }
    iter = &g_101d5e78.padding_0[0];
    while (true)
    {
        if (iter >= &g_101dfe78.padding_0[0])
            return v9;
        v9 = iter->field_21;
        if (iter->padding_0[0] && v9 == v4 && (v9 = (unsigned int)lstrcmpi(/* unsupported instruction */ - 2032, iter), !v9 && (v9 = v3 - 1, v9 < 4)))
            break;
        iter = &iter[9].padding_0[14];
    }
    v12 = 96 + (char *)iter + 56 * v9;
    v13 = v5;
    *((unsigned int *)&v12->field_10) = v13;
    if (v12 == *((int *)&g_100f4a05))
        v13 = sub_100188bf(g_10072f8c, 1040, 392, NULL, NULL);
    return v13;
}
```

## `sub_10031b41` `0x10031b41`

_79 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f0e18;
extern char g_100f0e42;

int sub_10031b41(void)
{
    unsigned int v2;  // eax
    unsigned int i;  // ebx
    unsigned int v1;  // [bp+0x100010]

    sub_10030225();
    v2 = sub_1003945d(/* unsupported instruction */ - 2032);
    if (v1 != 4294967295)
        return v2;
    for (i = 0; i < 1100; i += 100)
    {
        if (!g_100f0e42)
            return v2;
        v2 = (unsigned int)Sleep(100);
        g_100f0e18 = 0;
    }
    return v2;
}
```

## `sub_10031b90` `0x10031b90`

_81 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f0e18;
extern char g_100f0e42;

int sub_10031b90(void)
{
    unsigned int v2;  // eax
    unsigned int i;  // ebx
    unsigned int v1;  // [bp+0x100010]

    sub_10030225();
    v2 = sub_100393c2(/* unsupported instruction */ - 2032, 5);
    if (v1 != 4294967295)
        return v2;
    for (i = 0; i < 1100; i += 100)
    {
        if (!g_100f0e42)
            return v2;
        v2 = (unsigned int)Sleep(100);
        g_100f0e18 = 0;
    }
    return v2;
}
```

## `sub_10031be1` `0x10031be1`

_81 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f0e18;
extern char g_100f0e42;

int sub_10031be1(void)
{
    unsigned int v2;  // eax
    unsigned int i;  // ebx
    unsigned int v1;  // [bp+0x100010]

    sub_10030225();
    v2 = sub_100393c2(/* unsupported instruction */ - 2032, 6);
    if (v1 != 4294967295)
        return v2;
    for (i = 0; i < 1100; i += 100)
    {
        if (!g_100f0e42)
            return v2;
        v2 = (unsigned int)Sleep(100);
        g_100f0e18 = 0;
    }
    return v2;
}
```

## `sub_10031c32` `0x10031c32`

_81 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f0e18;
extern char g_100f0e42;

int sub_10031c32(void)
{
    unsigned int v2;  // eax
    unsigned int i;  // ebx
    unsigned int v1;  // [bp+0x100010]

    sub_10030225();
    v2 = sub_100393c2(/* unsupported instruction */ - 2032, 8);
    if (v1 != 4294967295)
        return v2;
    for (i = 0; i < 1100; i += 100)
    {
        if (!g_100f0e42)
            return v2;
        v2 = (unsigned int)Sleep(100);
        g_100f0e18 = 0;
    }
    return v2;
}
```

## `sub_10031c83` `0x10031c83`

_81 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f0e18;
extern char g_100f0e42;

int sub_10031c83(void)
{
    unsigned int v2;  // eax
    unsigned int i;  // ebx
    unsigned int v1;  // [bp+0x100010]

    sub_10030225();
    v2 = sub_100393c2(/* unsupported instruction */ - 2032, 9);
    if (v1 != 4294967295)
        return v2;
    for (i = 0; i < 1100; i += 100)
    {
        if (!g_100f0e42)
            return v2;
        v2 = (unsigned int)Sleep(100);
        g_100f0e18 = 0;
    }
    return v2;
}
```

## `sub_10031cd4` `0x10031cd4`

_81 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f0e18;
extern char g_100f0e42;

int sub_10031cd4(void)
{
    unsigned int v2;  // eax
    unsigned int i;  // ebx
    unsigned int v1;  // [bp+0x100010]

    sub_10030225();
    v2 = sub_100393c2(/* unsupported instruction */ - 2032, 0);
    if (v1 != 4294967295)
        return v2;
    for (i = 0; i < 1100; i += 100)
    {
        if (!g_100f0e42)
            return v2;
        v2 = (unsigned int)Sleep(100);
        g_100f0e18 = 0;
    }
    return v2;
}
```

## `sub_10031d25` `0x10031d25`

_147 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[36];
    struct struct_0 *field_24;
    char padding_28[4];
    int field_2c;
} struct_1;

typedef struct struct_0 {
    char padding_0[44];
    int field_2c;
} struct_0;

typedef struct struct_2 {
    struct struct_1 *field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
} struct_2;

extern unsigned int g_100f0e18;
extern char g_100f0e42;
extern struct_2 g_100f9109;

int sub_10031d25(void)
{
    unsigned int v3;  // eax
    unsigned int idx;  // ecx
    struct_1 *v5;  // ebx
    struct_1 *v6;  // ebx
    unsigned int v7;  // eax
    unsigned int i;  // ebx
    unsigned int v0;  // [bp-0x4]
    unsigned int v2;  // [bp+0x100010]

    sub_10030225();
    v3 = (unsigned int)sub_10030225();
    idx = 0;
    v5 = g_100f9109.field_0;
    while (true)
    {
        v6 = v5;
        if (!v5)
            return v3;
        v0 = idx;
        v3 = lstrcmpi(/* unsupported instruction */ - 0x1000, v6->field_2c);
        if (!v3)
            break;
        idx += 1;
        v5 = (&g_100f9109.field_0)[idx];
    }
    v7 = sub_100393c2(/* unsupported instruction */ - 2032, v6->field_24->field_2c);
    if (v2 != 4294967295)
        return v7;
    for (i = 0; i < 1100; i += 100)
    {
        if (!g_100f0e42)
            return v7;
        v7 = (unsigned int)Sleep(100);
        g_100f0e18 = 0;
    }
    return v7;
}
```

## `sub_10031db8` `0x10031db8`

_77 bytes. (leaf/helper — see body)_

```c
extern SOCKET g_1005f539;

int sub_10031db8(void)
{
    unsigned int v3;  // eax
    int len;  // eax
    char v1;  // [bp+0xff814]
    char v2;  // [bp+0xff914]

    v3 = (unsigned int)sub_10030225();
    if (!g_1005f539)
        return v3;
    v1 = 7;
    v2 = 0;
    len = lstrlen(/* unsupported instruction */ - 2031);
    return send(g_1005f539, /* unsupported instruction */ - 2032, len + 2, 0);
}
```

## `sub_10031e05` `0x10031e05`

_119 bytes. calls SendDlgItemMessageA; refs "off", "toggle"_

```c
extern HWND g_10072fbc;
extern char g_100fa4ef;

LRESULT sub_10031e05(void)
{
    int v0;  // [bp-0xa]
    int v2;  // [bp+0x100000]

    if (!lstrcmpi(v2, "on"))
        g_100fa4ef = 1;
    if (!lstrcmpi(v2, "off"))
        g_100fa4ef = 0;
    if (!lstrcmpi(v2, "toggle"))
        g_100fa4ef = !g_100fa4ef;
    *((unsigned int *)&(&v0)[6]) = 0;
    *((unsigned int *)&(&v0)[2]) = 0;
    *((unsigned short *)&v0) = g_100fa4ef;
    return SendDlgItemMessageA(g_10072fbc, 1010, 241, *((unsigned int *)&v0), *((unsigned int *)(&v0 + 4)));
}
```

## `sub_10031e7c` `0x10031e7c`

_30 bytes. (leaf/helper — see body)_

```c
int sub_10031e7c(void)
{
    sub_10030225();
    return sub_10039374(/* unsupported instruction */ - 2032);
}
```

## `sub_10031e9a` `0x10031e9a`

_208 bytes. refs "buywithbps", "buynobps", "considercap"_

```c
extern char g_100f9311;
extern char g_100f9312;
extern char g_100f9313;

int sub_10031e9a(void)
{
    int v1;  // eax

    sub_10030225();
    if (!lstrcmpi(/* unsupported instruction */ - 2032, "buywithbps"))
        g_100f9311 = 1;
    if (!lstrcmpi(/* unsupported instruction */ - 2032, "buynobps"))
        g_100f9311 = 0;
    sub_10030225();
    if (!lstrcmpi(/* unsupported instruction */ - 2032, "considercap"))
        g_100f9312 = 1;
    if (!lstrcmpi(/* unsupported instruction */ - 2032, "ignorecap"))
        g_100f9312 = 0;
    sub_10030225();
    if (!lstrcmpi(/* unsupported instruction */ - 2032, "sellequipped"))
        g_100f9313 = 0;
    v1 = lstrcmpi(/* unsupported instruction */ - 2032, "ignoreequipped");
    if (!v1)
        g_100f9313 = 1;
    return v1;
}
```

## `sub_10031f6a` `0x10031f6a`

_185 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0[4];
    char field_2;
} struct_0;

extern unsigned int g_100f0e18;
extern struct_0 g_100f8d09;
extern struct_0 g_100f9109;
extern char g_100f9311;
extern char g_100f9312;

int sub_10031f6a(void)
{
    unsigned int v10;  // eax
    unsigned short v11;  // bx
    struct_0 *iter;  // esi
    unsigned int v13;  // ecx
    unsigned int v14;  // eax
    unsigned int v15;  // eax
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x4]
    unsigned short v2;  // [bp+0xff814]
    char v3;  // [bp+0xff816]
    unsigned short v4;  // [bp+0xff817]
    char v5;  // [bp+0xff819]
    char v6;  // [bp+0xff81a]
    char v7;  // [bp+0xff81b]
    char v8;  // [bp+0xff81c]
    unsigned int v9;  // [bp+0x100010]

    v0 = sub_100300ce();
    v10 = sub_100300ce();
    v11 = v0;
    if (v10 > 100)
        v10 = 100;
    v2 = 7;
    v3 = 122;
    v4 = v11;
    v5 = 0;
    v6 = v10;
    iter = &g_100f8d09.field_0[0];
    while (true)
    {
        if (!(iter->field_0 && iter < &g_100f9109.field_0[0]))
        {
LABEL_10031fe1:
            v7 = g_100f9312;
            v8 = g_100f9311;
            v0 = 9;
            v15 = sub_1002ade7(/* unsupported instruction */ - 2032);
            if (v9 != 4294967295)
                return v15;
            v16 = (unsigned int)Sleep(220);
            g_100f0e18 = 0;
            break;
        }
        else if (*((short *)&iter->field_0[0]) == v11)
        {
            v13 = iter->field_0[2];
            v5 = v13;
            v14 = v10 / v13;
            v6 = v14;
            if (!v14)
                return v14;
            goto LABEL_10031fe1;
        }
        else
        {
            iter = &iter->field_2;
        }
    }
    return v16;
}
```

## `sub_10032023` `0x10032023`

_223 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0[4];
    char field_2;
} struct_0;

extern unsigned int g_100f0e18;
extern char g_100f0e7c;
extern struct_0 g_100f8d09;
extern struct_0 g_100f9109;
extern char g_100f9311;
extern char g_100f9312;

int sub_10032023(void)
{
    unsigned int v13;  // edx
    unsigned int v14;  // eax
    unsigned short v15;  // bx
    unsigned int v16;  // esi
    unsigned int v17;  // eax
    struct_0 *iter;  // esi
    unsigned int v19;  // ecx
    unsigned int v20;  // eax
    unsigned int v21;  // eax
    unsigned int v22;  // eax
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp-0x4]
    unsigned short v3;  // [bp+0xff814]
    char v4;  // [bp+0xff816]
    unsigned short v5;  // [bp+0xff817]
    char v6;  // [bp+0xff819]
    char v7;  // [bp+0xff81a]
    char v8;  // [bp+0xff81b]
    char v9;  // [bp+0xff81c]
    unsigned int v10;  // [bp+0xffff8]
    unsigned int v11;  // [bp+0xffffc]
    unsigned int v12;  // [bp+0x100010]

    v1 = sub_100300ce();
    v0 = sub_100300ce();
    v11 = sub_100300ce();
    v10 = v13;
    v14 = sub_100300ce();
    v15 = v1;
    v16 = *((int *)&g_100f0e7c);
    if (v10)
        v16 = v11;
    if (v16 >= v14)
        return v14;
    v17 = v14 - v16;
    if (v17 > 100)
        v17 = 100;
    v3 = 7;
    v4 = 122;
    v5 = v15;
    v6 = 0;
    v7 = v17;
    iter = &g_100f8d09.field_0[0];
    while (true)
    {
        if (!(iter->field_0 && iter < &g_100f9109.field_0[0]))
        {
LABEL_100320c0:
            v8 = g_100f9312;
            v9 = g_100f9311;
            v1 = 9;
            v21 = sub_1002ade7(/* unsupported instruction */ - 2032);
            if (v12 != 4294967295)
                return v21;
            v22 = (unsigned int)Sleep(220);
            g_100f0e18 = 0;
            break;
        }
        else if (*((short *)&iter->field_0[0]) == v15)
        {
            v19 = iter->field_0[2];
            v6 = v19;
            v20 = v17 / v19;
            v7 = v20;
            if (!v20)
                return v20;
            goto LABEL_100320c0;
        }
        else
        {
            iter = &iter->field_2;
        }
    }
    return v22;
}
```

## `sub_10032102` `0x10032102`

_152 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f0e18;
extern char g_100f0e7c;
extern char g_100f9313;

int sub_10032102(void)
{
    unsigned int v12;  // edx
    unsigned int v13;  // eax
    unsigned int v14;  // esi
    unsigned int v15;  // ecx
    unsigned int v16;  // eax
    unsigned int v17;  // eax
    unsigned int v18;  // eax
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp-0x4]
    unsigned short v3;  // [bp+0xff814]
    char v4;  // [bp+0xff816]
    unsigned short v5;  // [bp+0xff817]
    char v6;  // [bp+0xff819]
    char v7;  // [bp+0xff81a]
    char v8;  // [bp+0xff81b]
    unsigned int v9;  // [bp+0xffff8]
    unsigned int v10;  // [bp+0xffffc]
    unsigned int v11;  // [bp+0x100010]

    v1 = sub_100300ce();
    v0 = sub_100300ce();
    v10 = sub_100300ce();
    v9 = v12;
    v13 = sub_100300ce();
    v14 = *((int *)&g_100f0e7c);
    if (v9)
        v14 = v10;
    if (v14 <= v13)
        return v13;
    v16 = v15;
    if (v16 > 100)
        v16 = 100;
    v3 = 6;
    v4 = 123;
    v5 = v1;
    v6 = 0;
    v7 = v16;
    v8 = g_100f9313;
    v1 = 8;
    v17 = sub_1002ade7(/* unsupported instruction */ - 2032);
    if (v11 != 4294967295)
        return v17;
    v18 = (unsigned int)Sleep(220);
    g_100f0e18 = 0;
    return v18;
}
```

## `sub_1003219a` `0x1003219a`

_116 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f0e18;
extern char g_100f9313;

int sub_1003219a(void)
{
    unsigned int v9;  // eax
    unsigned int v10;  // eax
    unsigned int v11;  // eax
    unsigned int v0;  // [bp-0x4]
    unsigned short v2;  // [bp+0xff814]
    char v3;  // [bp+0xff816]
    unsigned short v4;  // [bp+0xff817]
    char v5;  // [bp+0xff819]
    char v6;  // [bp+0xff81a]
    char v7;  // [bp+0xff81b]
    unsigned int v8;  // [bp+0x100010]

    v0 = sub_100300ce();
    v9 = sub_100300ce();
    if (v9 > 100)
        v9 = 100;
    v2 = 6;
    v3 = 123;
    v4 = v0;
    v5 = 0;
    v6 = v9;
    v7 = g_100f9313;
    v0 = 8;
    v10 = sub_1002ade7(/* unsupported instruction */ - 2032);
    if (v8 != 4294967295)
        return v10;
    v11 = (unsigned int)Sleep(220);
    g_100f0e18 = 0;
    return v11;
}
```

## `sub_1003220e` `0x1003220e`

_140 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_1004339b;
extern unsigned short g_100433a0;
extern char g_100433a2;
extern unsigned short g_100433a3;
extern char g_100433a5;
extern unsigned int g_100433a6;
extern char g_1005f7ed;
extern unsigned int g_100f9328;

unsigned int * sub_1003220e(void)
{
    unsigned int *v2;  // eax
    unsigned int v0;  // [bp-0x10]

    g_100433a3 = 268;
    g_100f9328 = 0;
    sub_10030225();
    v2 = sub_10038eb3(/* unsupported instruction */ - 2032, 0, 0);
    if (!v2)
        return v2;
    g_100433a6 = *(v2);
    if (v2 == *((int *)&g_1005f7ed) && *((int *)0x63fe74) == *((int *)0x63fe78))
        return v2;
    g_100433a0 = 0;
    g_100433a2 = 0;
    g_100433a5 = 0;
    g_100f9328 = 1;
    v0 = 15;
    return sub_1002ade7(&g_1004339b);
}
```

## `sub_10032219` `0x10032219`

_11 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_100433a3;

void sub_10032219(void)
{
    g_100433a3 = 237;
}
```

## `sub_10032224` `0x10032224`

_11 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_100433a3;

void sub_10032224(void)
{
    g_100433a3 = 0xee;
}
```

## `sub_1003222f` `0x1003222f`

_11 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_100433a3;

void sub_1003222f(void)
{
    g_100433a3 = 7642;
}
```

## `sub_100322bb` `0x100322bb`

_139 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_1004339b;
extern unsigned short g_100433a0;
extern char g_100433a2;
extern unsigned short g_100433a3;
extern char g_100433a5;
extern unsigned int g_100433a6;
extern unsigned int g_100f9328;

unsigned int [35] sub_100322bb(void)
{
    unsigned int v4[35];  // eax
    unsigned int v5[35];  // eax
    unsigned int v0;  // [bp-0x10]
    unsigned int v2;  // [bp+0xffffc]
    unsigned int v3;  // [bp+0x100000]

    g_100433a3 = 266;
    g_100f9328 = 0;
    sub_100300ce();
    v4 = sub_10038eb3(/* unsupported instruction */ - 2032, 0, 1, (unsigned int)sub_10030225());
    v2 = v3;
    v5 = v4;
    if (!v5)
        return v5;
    g_100433a6 = v5[0];
    if (v5[0x22] >= /* unsupported instruction */ - 2032)
        return v5;
    g_100433a0 = 0;
    g_100433a2 = 0;
    g_100433a5 = 0;
    g_100433a5 = 0;
    g_100f9328 = 1;
    v0 = 15;
    return sub_1002ade7(&g_1004339b);
}
```

## `sub_100322c6` `0x100322c6`

_11 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_100433a3;

void sub_100322c6(void)
{
    g_100433a3 = 236;
}
```

## `sub_100322d1` `0x100322d1`

_11 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_100433a3;

void sub_100322d1(void)
{
    g_100433a3 = 239;
}
```

