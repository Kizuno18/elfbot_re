# elfbot.dll decompiled — jdrv 0x1003472d..0x1003567f

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1003472d` `0x1003472d`

_40 bytes. (leaf/helper — see body)_

```c
void* sub_1003472d(void)
{
    void* v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    v4 = sub_100300ce() * 100;
    if (*((int *)0x63fe68) < v4)
        return v4;
    return sub_10030442(v1, v2, v3);
}
```

## `sub_10034755` `0x10034755`

_33 bytes. (leaf/helper — see body)_

```c
int sub_10034755(void)
{
    unsigned int v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    v4 = sub_100300ce();
    if (*((int *)0x63fe94) >= v4)
        return v4;
    return sub_10030442(v1, v2, v3);
}
```

## `sub_10034776` `0x10034776`

_58 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1008ab9f;

int sub_10034776(void)
{
    unsigned int v4;  // eax
    unsigned int v5;  // eax
    void* v1;  // [bp+0x100000]
    void* idx;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    v4 = sub_100300ce();
    if (!v4)
    {
        *((unsigned int *)(0x4 * idx + (char *)&g_1008ab9f)) = 0;
        return v4;
    }
    v5 = sub_10030442(v1, idx, v3);
    *((unsigned int *)(0x4 * idx + (char *)&g_1008ab9f)) = 1;
    return v5;
}
```

## `sub_100347b0` `0x100347b0`

_45 bytes. (leaf/helper — see body)_

```c
int sub_100347b0(void)
{
    unsigned int v4;  // eax
    char v1;  // [bp+0xff814]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    v4 = (unsigned int)sub_10030225();
    if (!v1)
        return v4;
    return sub_10030442(/* unsupported instruction */ - 2032, v2, v3);
}
```

## `sub_100347dd` `0x100347dd`

_58 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1008ab9f;

int sub_100347dd(void)
{
    unsigned int v4;  // eax
    unsigned int v5;  // eax
    void* v1;  // [bp+0x100000]
    void* idx;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    v4 = sub_100300ce();
    if (v4)
    {
        *((unsigned int *)(0x4 * idx + (char *)&g_1008ab9f)) = 0;
        return v4;
    }
    v5 = sub_10030442(v1, idx, v3);
    *((unsigned int *)(0x4 * idx + (char *)&g_1008ab9f)) = 1;
    return v5;
}
```

## `sub_10034817` `0x10034817`

_31 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1008ab9f[4];

void* sub_10034817(void)
{
    void* v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    if (!*((int *)(0x4 * v2 + (char *)&g_1008ab9f[0])))
        v4 = sub_10030442(v1, v2, v3);
    return v4;
}
```

## `sub_10034836` `0x10034836`

_42 bytes. (leaf/helper — see body)_

```c
int sub_10034836(void)
{
    unsigned int v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    v4 = sub_100300ce();
    if (*((int *)0x63fe90) - *((int *)0x63fe94) >= v4)
        return v4;
    return sub_10030442(v1, v2, v3);
}
```

## `sub_10034860` `0x10034860`

_42 bytes. (leaf/helper — see body)_

```c
int sub_10034860(void)
{
    unsigned int v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    v4 = sub_100300ce();
    if (*((int *)0x63fe90) - *((int *)0x63fe94) < v4)
        return v4;
    return sub_10030442(v1, v2, v3);
}
```

## `sub_1003488a` `0x1003488a`

_42 bytes. (leaf/helper — see body)_

```c
int sub_1003488a(void)
{
    unsigned int v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    v4 = sub_100300ce();
    if (*((int *)0x63fe74) - *((int *)0x63fe78) >= v4)
        return v4;
    return sub_10030442(v1, v2, v3);
}
```

## `sub_100348b4` `0x100348b4`

_42 bytes. (leaf/helper — see body)_

```c
int sub_100348b4(void)
{
    unsigned int v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    v4 = sub_100300ce();
    if (*((int *)0x63fe74) - *((int *)0x63fe78) < v4)
        return v4;
    return sub_10030442(v1, v2, v3);
}
```

## `sub_100348de` `0x100348de`

_33 bytes. (leaf/helper — see body)_

```c
int sub_100348de(void)
{
    unsigned int v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    v4 = sub_100300ce();
    if (*((int *)0x63fe94) < v4)
        return v4;
    return sub_10030442(v1, v2, v3);
}
```

## `sub_100348ff` `0x100348ff`

_138 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_10043344;
extern char g_10043349;
extern char g_1004334b;
extern unsigned short g_1004334c;
extern char g_1004334e;
extern unsigned short g_10043454;
extern unsigned short g_1004345c;
extern char g_10043461;
extern char g_1008baed;

int sub_100348ff(void)
{
    unsigned int v2;  // eax
    unsigned int v3;  // eax
    char v4;  // dl
    unsigned int v5;  // eax
    unsigned int v0;  // [bp-0x4]

    if (*((int *)0x63fe64))
    {
        v2 = sub_100300ce();
        if (*((int *)6606072) == v2)
            return v2;
        g_1004334c = v2;
        v3 = sub_1002ae92(v2, 0, NULL);
        if (v3)
        {
            g_1004334b = v4;
            g_1004334e = v4;
            g_10043349 = v3;
            g_1008baed = v3;
            v0 = 0x11;
            v3 = sub_1002ade7(&g_10043344);
        }
        return v3;
    }
    else
    {
        v5 = sub_100300ce();
        if (!*((int *)0x64ccf8))
        {
            return v5;
        }
        else if (*((int *)6606072) == v5)
        {
            g_1004345c = v5;
            g_10043461 = g_1008baed;
            v0 = 0x11;
            return sub_1002ade7(&g_10043454);
        }
        else
        {
            return v5;
        }
    }
}
```

## `sub_10034989` `0x10034989`

_50 bytes. refs "exiva "_

```c
extern int g_10042c7b;

int sub_10034989(void)
{
    lstrcpy(/* unsupported instruction */ - 2032, "exiva ");
    lstrcat(/* unsupported instruction */ - 2032, &g_10042c7b);
    return sub_10039413(/* unsupported instruction */ - 2032);
}
```

## `sub_100349bb` `0x100349bb`

_50 bytes. refs "exiva \"_

```c
extern int g_10042cbb;

int sub_100349bb(void)
{
    lstrcpy(/* unsupported instruction */ - 2032, "exiva \"");
    lstrcat(/* unsupported instruction */ - 2032, &g_10042cbb);
    return sub_10039413(/* unsupported instruction */ - 2032);
}
```

## `sub_100349ed` `0x100349ed`

_9 bytes. (leaf/helper — see body)_

```c
void sub_100349ed(void)
{
    sub_10038725();
    return;
}
```

## `sub_100349f6` `0x100349f6`

_54 bytes. (leaf/helper — see body)_

```c
unsigned int sub_100349f6(void)
{
    unsigned int v2;  // eax

    v2 = sub_100384fb();
    if (!v2)
        return v2;
}
```

## `sub_10034a2c` `0x10034a2c`

_379 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_100434b5;
extern unsigned short g_100434b8;
extern unsigned short g_100434ba;
extern char g_100434bc;
extern unsigned short g_100434bd;
extern char g_100434c2;
extern char g_100434c4;
extern char g_100434c5;
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern int g_1005f85c;

int sub_10034a2c(void)
{
    int v13;  // ebx
    unsigned int k;  // eax
    unsigned int v15;  // ecx
    char v16;  // cl
    unsigned int v17;  // eax
    unsigned int v18[16];  // eax
    unsigned int v0;  // [bp-0x10]
    unsigned int i;  // [bp+0xfeffc]
    unsigned int j;  // [bp+0xff000]
    unsigned int v5;  // [bp+0xfffe4]
    unsigned int v6;  // [bp+0xfffe8]
    unsigned int v7;  // [bp+0xfffec]
    int v8;  // [bp+0xffff0]
    unsigned int v9;  // [bp+0xffff4]
    int v10;  // [bp+0xffff8]
    int v11;  // [bp+0xffffc]
    int v12;  // [bp+0x100000]

    v13 = v12;
    k = (unsigned int)sub_10030225();
    v12 = v13;
    v6 = 0;
    v5 = 0;
    for (i = 0; i < 3; i += 1)
    {
        j = 0;
        while (j < 3)
        {
            lstrcpy(/* unsupported instruction */ - 0x1000, v12);
            v11 = g_1005f854 + j - 1;
            v10 = g_1005f858 + i - 1;
            k = sub_1003a065(v11, v10, g_1005f85c);
            if (k)
            {
                v9 = k;
                v8 = v13;
                v7 = v15;
                v13 = /* unsupported instruction */ - 0x1000;
                while (k)
                {
                    k = sub_100300ce();
                    if (k == v9)
                    {
                        g_100434b8 = v11;
                        g_100434ba = v10;
                        g_100434bc = g_1005f85c;
                        g_100434bd = k;
                        v16 = v7;
                        if (!v7)
                            v16 = (char)v7 + 1;
                        g_100434c5 = v16;
                        sub_10036daf();
                        v17 = sub_10036c87();
                        if (!v17)
                            return v17;
                        g_100434c2 = v17;
                        if (v15 == 4294967295)
                        {
                            v18 = (v17 - 64) * 492 + 6606096;
                            if ((unsigned short)v18[15] == g_100434bd)
                                g_100434c4 = 0;
                            else
                                g_100434c4 = v18[12] - 1;
                        }
                        else
                        {
                            g_100434c4 = v15;
                        }
                        v0 = 0x11;
                        return sub_1002ade7(&g_100434b5);
                    }
                }
                j += 1;
            }
            else
            {
                if ((vvar_45{r20|4b} == 0x0<32>)) { Goto None } else { Goto None }
                *((unsigned int *)(/* unsupported instruction */ - 4100)) = j + 1;
            }
        }
    }
    return k;
}
```

## `sub_10034ba7` `0x10034ba7`

_226 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_100434b5;
extern unsigned short g_100434b8;
extern unsigned short g_100434ba;
extern char g_100434bc;
extern unsigned short g_100434bd;
extern char g_100434c2;
extern char g_100434c4;
extern char g_100434c5;
extern int g_1005f854;
extern int g_1005f858;
extern int g_1005f85c;

unsigned int * sub_10034ba7(void)
{
    unsigned int *v2;  // eax
    unsigned int v3;  // eax
    unsigned int *v4;  // eax
    unsigned int v5;  // ecx
    unsigned int v6[16];  // eax
    unsigned int v0;  // [bp-0x10]

    v2 = sub_1003a03f(g_1005f854, g_1005f858, g_1005f85c);
    if (!v2)
    {
        return v2;
    }
    else if (*(v2) > 1)
    {
        g_100434b8 = g_1005f854;
        g_100434ba = g_1005f858;
        g_100434bc = g_1005f85c;
        g_100434bd = sub_100300ce();
        v3 = sub_100300ce();
        if (!v3)
            v3 += 1;
        g_100434c5 = v3;
        sub_10030225();
        sub_10036daf();
        v4 = sub_10036c87();
        if (!v4)
            return v4;
        g_100434c2 = *((char *)&v4);
        if (v5 == 4294967295)
        {
            v6 = (v4 + 16) * 492 + 6606096;
            if ((unsigned short)v6[15] == g_100434bd)
                g_100434c4 = 0;
            else
                g_100434c4 = v6[12] - 1;
        }
        else
        {
            g_100434c4 = v5;
        }
        v0 = 0x11;
        return sub_1002ade7(&g_100434b5);
    }
    else
    {
        return v2;
    }
}
```

## `sub_10034c89` `0x10034c89`

_340 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_100434b5;
extern unsigned short g_100434b8;
extern unsigned short g_100434ba;
extern char g_100434bc;
extern unsigned short g_100434bd;
extern char g_100434c2;
extern char g_100434c4;
extern char g_100434c5;
extern int g_1005f854;
extern int g_1005f858;
extern int g_1005f85c;
extern unsigned int g_100f0e18;
extern char g_100f0e42;

unsigned int * sub_10034c89(void)
{
    unsigned int *v5;  // eax
    unsigned int v6;  // ecx
    unsigned int *v15;  // eax
    unsigned int v7;  // edx
    unsigned int v8[3];  // ecx
    unsigned short v9;  // ax
    unsigned int v10;  // ebx
    unsigned int v11;  // ebx
    unsigned int *v12;  // eax
    unsigned int v13;  // ecx
    unsigned int v14[16];  // eax
    unsigned int v0;  // [bp-0x10]
    unsigned int v2;  // [bp+0xffff8]
    unsigned int v3;  // [bp+0xffffc]
    unsigned int v4;  // [bp+0x100010]

    v3 = 0;
    v2 = 0;
    while (true)
    {
        v5 = sub_1003a03f(g_1005f854, g_1005f858, g_1005f85c);
        if (!v5)
            return v5;
        v6 = *(v5);
        if (v6 <= 1)
            return v5;
        if (v3 == v6)
        {
            v2 += 1;
            if (v2 > 3)
                return v5;
        }
        else
        {
            v3 = v6;
            v2 = 0;
        }
        v7 = 0;
        while (true)
        {
            if (!v6)
                return v5;
            if (*((int *)(4 + (char *)v5 + v7)) == 99)
                break;
            v7 += 12;
            v6 -= 1;
        }
        v8 = 16 + (char *)v5 + v7;
        v9 = v8[0];
        v10 = v8[1];
        g_100434b8 = g_1005f854;
        g_100434ba = g_1005f858;
        g_100434bc = g_1005f85c;
        g_100434bd = v9;
        v11 = v10;
        if (!v11)
            v11 += 1;
        g_100434c5 = v11;
        sub_10030225();
        sub_10036daf();
        v12 = sub_10036c87();
        if (!v12)
            return v12;
        g_100434c2 = *((char *)&v12);
        if (v13 == 4294967295)
        {
            v14 = (v12 + 16) * 492 + 6606096;
            if ((unsigned short)v14[15] == g_100434bd)
                g_100434c4 = 0;
            else
                g_100434c4 = v14[12] - 1;
        }
        else
        {
            g_100434c4 = v13;
        }
        v0 = 0x11;
        v15 = sub_1002ade7(&g_100434b5);
        if (v4 != 4294967295)
            return v15;
        if (!g_100f0e42)
            return v15;
        Sleep(300);
        g_100f0e18 = 0;
    }
}
```

## `sub_10034cd3` `0x10034cd3`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10034cd3(void)
{
}
```

## `sub_10034ddf` `0x10034ddf`

_124 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_100434de;
extern unsigned short g_100434e1;
extern unsigned short g_100434e3;
extern char g_100434e5;
extern unsigned short g_100434e6;
extern unsigned short g_100434e9;
extern unsigned short g_100434eb;
extern char g_100434ed;
extern char g_100434ee;

int sub_10034ddf(void)
{
    int v5;  // ebx
    unsigned int v6;  // eax
    unsigned int v7;  // eax
    unsigned int v8;  // eax
    int v9;  // eax
    unsigned int v10;  // ecx
    unsigned int v11;  // ecx
    unsigned int v0;  // [bp-0x10]
    unsigned int v2;  // [bp+0xffff8]
    unsigned int v3;  // [bp+0xffffc]
    int v4;  // [bp+0x100000]

    v5 = v4;
    v6 = sub_100300ce();
    v3 = v6;
    g_100434e1 = v6;
    v7 = sub_100300ce();
    v2 = v7;
    g_100434e3 = v7;
    v8 = sub_100300ce();
    g_100434e5 = v8;
    v9 = sub_1003a065(v3, v2, v8, v5);
    if (!v9)
        return v9;
    g_100434e6 = v9;
    v11 = v10;
    if (!v10)
        v11 += 1;
    g_100434ee = v11;
    g_100434e9 = sub_100300ce();
    g_100434eb = sub_100300ce();
    g_100434ed = sub_100300ce();
    v0 = 0x11;
    return sub_1002ade7(&g_100434de);
}
```

## `sub_10034e5b` `0x10034e5b`

_174 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_100434a4;
extern char g_100434a9;
extern char g_100434ab;
extern unsigned short g_100434ac;
extern char g_100434ae;
extern unsigned short g_100434af;
extern unsigned short g_100434b1;
extern char g_100434b3;
extern char g_100434b4;
extern unsigned int g_100f0e18;
extern char g_100f0e42;

unsigned int sub_10034e5b(void)
{
    unsigned int v7;  // ebx
    unsigned int v8;  // eax
    unsigned int v9;  // eax
    char v10;  // dl
    unsigned int v11;  // ecx
    unsigned int v12;  // ecx
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]
    unsigned int v2;  // [bp-0x4]
    unsigned int v4;  // [bp+0xffffc]
    unsigned int v5;  // [bp+0x100000]
    unsigned int v6;  // [bp+0x100010]

    v7 = v5;
    g_100434af = sub_100300ce();
    g_100434b1 = sub_100300ce();
    g_100434b3 = sub_100300ce();
    v5 = v7;
    v4 = 0;
    while (true)
    {
        v8 = sub_100300ce();
        if (!v8)
            break;
        while (true)
        {
            v2 = v8;
            v1 = v7;
            g_100434ac = v8;
            v9 = sub_1002ae92(v8, 0, NULL);
            if (!v9)
                break;
            g_100434a9 = v9;
            g_100434ab = v10;
            g_100434ae = v10;
            v12 = v11;
            if (!v11)
                v12 += 1;
            g_100434b4 = v12;
            v0 = 0x11;
            sub_1002ade7(&g_100434a4);
            if (v6 != 4294967295)
                return v1;
            if (!g_100f0e42)
                return v1;
            Sleep(300);
            g_100f0e18 = 0;
            v7 = 0x11;
            v8 = v1;
        }
        v7 = v1;
    }
    return v8;
}
```

## `sub_10034e86` `0x10034e86`

_110 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_100434a4;
extern char g_100434a9;
extern char g_100434ab;
extern unsigned short g_100434ac;
extern char g_100434ae;
extern unsigned short g_100434af;
extern unsigned short g_100434b1;
extern char g_100434b3;
extern char g_100434b4;

int sub_10034e86(void)
{
    unsigned int v3;  // ebx
    unsigned int v4;  // eax
    unsigned int v5;  // eax
    char v6;  // dl
    char v7;  // cl
    unsigned int v0;  // [bp-0x4]
    unsigned int v2;  // [bp+0x100000]

    v3 = v2;
    g_100434af = sub_100300ce();
    g_100434b1 = sub_100300ce();
    g_100434b3 = sub_100300ce();
    v4 = sub_100300ce();
    if (!v4)
        return v4;
    v0 = v3;
    g_100434ac = v4;
    v5 = sub_1002ae92(v4, 0, NULL);
    if (!v5)
        return v5;
    g_100434a9 = v5;
    g_100434ab = v6;
    g_100434ae = v6;
    sub_100300ce();
    g_100434b4 = v7;
    v0 = 0x11;
    return sub_1002ade7(&g_100434a4);
}
```

## `sub_10034ef4` `0x10034ef4`

_35 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_100434af;
extern unsigned short g_100434b1;
extern char g_100434b3;
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern unsigned int g_1005f85c;

int sub_10034ef4(void)
{
    g_100434af = g_1005f854;
    g_100434b1 = g_1005f858;
    g_100434b3 = g_1005f85c;
}
```

## `sub_10034f9a` `0x10034f9a`

_24 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f9328;

int sub_10034f9a(void)
{
    g_100f9328 = 0;
    return sub_1003ca03();
}
```

## `sub_10034fb2` `0x10034fb2`

_24 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f9328;

int sub_10034fb2(void)
{
    g_100f9328 = 0;
    return sub_1003ca03();
}
```

## `sub_10034fca` `0x10034fca`

_24 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f9328;

int sub_10034fca(void)
{
    g_100f9328 = 0;
    return sub_1003ca03();
}
```

## `sub_10034fe2` `0x10034fe2`

_24 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f9328;

int sub_10034fe2(void)
{
    g_100f9328 = 0;
    return sub_1003ca03();
}
```

## `sub_10034ffa` `0x10034ffa`

_41 bytes. (leaf/helper — see body)_

```c
extern char g_100f9317;

int sub_10034ffa(void)
{
    int v4;  // eax
    unsigned int v0;  // [bp-0x4]
    unsigned short v2;  // [bp+0xff814]
    char v3;  // [bp+0xff816]

    v2 = 1;
    v3 = 20;
    v0 = 0;
    v4 = sub_1002ade7(/* unsupported instruction */ - 2032);
    g_100f9317 = 50;
    return v4;
}
```

## `sub_10035023` `0x10035023`

_85 bytes. (leaf/helper — see body)_

```c
extern char g_100f94c6;
extern unsigned int g_79cf30;
extern unsigned int g_79cf34;
extern unsigned int g_79cf38;
extern unsigned int g_79cf3c;
extern unsigned int g_79cf88;
extern unsigned int g_79cfe0;
extern unsigned int g_79cfe4;

unsigned int sub_10035023(void)
{
    g_79cfe0 = sub_100300ce();
    g_79cfe4 = 0;
    g_79cf30 = 0;
    g_79cf34 = 0;
    g_79cf38 = 0xffff;
    g_79cf3c = 0;
    g_79cf88 = 7;
    if (g_100f94c6)
        g_100f94c6 = 2;
    return &g_79cf88;
}
```

## `sub_10035078` `0x10035078`

_24 bytes. (leaf/helper — see body)_

```c
extern SOCKET g_100428d5;
extern char g_100f9317;

int sub_10035078(void)
{
    int v1;  // eax

    v1 = shutdown(g_100428d5, SD_BOTH);
    g_100f9317 = 50;
    return v1;
}
```

## `sub_10035090` `0x10035090`

_43 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10035090(void)
{
    unsigned int v1;  // eax

    sub_10030225();
    v1 = sub_10038eb3(/* unsupported instruction */ - 2032, 0, 0);
    if (!v1)
        return v1;
    return 268685751();
}
```

## `sub_100350bb` `0x100350bb`

_9 bytes. (leaf/helper — see body)_

```c
void sub_100350bb(void)
{
    sub_1003d60f();
    return;
}
```

## `sub_100350c4` `0x100350c4`

_9 bytes. (leaf/helper — see body)_

```c
void sub_100350c4(void)
{
    sub_10038449();
    return;
}
```

## `sub_100350cd` `0x100350cd`

_63 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f9328;

unsigned int sub_100350cd(void)
{
    unsigned int v1;  // eax

    g_100f9328 = 0;
    sub_10030225();
    v1 = sub_10038eb3(/* unsupported instruction */ - 2032, 0, 0);
    if (!v1)
        return v1;
    g_100f9328 = 1;
    return sub_10037a0f();
}
```

## `sub_1003510c` `0x1003510c`

_53 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f9328;

unsigned int sub_1003510c(void)
{
    unsigned int v1;  // eax

    g_100f9328 = 0;
    sub_10030225();
    v1 = sub_10038eb3(/* unsupported instruction */ - 2032, 0, 0);
    if (!v1)
        return v1;
    return sub_10037b0c();
}
```

## `sub_10035141` `0x10035141`

_38 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f9328;

int sub_10035141(void)
{
    g_100f9328 = 0;
    sub_10030225();
    return sub_10037b0c();
}
```

## `sub_10035167` `0x10035167`

_33 bytes. (leaf/helper — see body)_

```c
int sub_10035167(void)
{
    unsigned int v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    v4 = sub_100300ce();
    if (*((int *)0x63fe78) >= v4)
        return v4;
    return sub_10030442(v1, v2, v3);
}
```

## `sub_10035188` `0x10035188`

_33 bytes. (leaf/helper — see body)_

```c
int sub_10035188(void)
{
    unsigned int v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    v4 = sub_100300ce();
    if (*((int *)0x63fe78) < v4)
        return v4;
    return sub_10030442(v1, v2, v3);
}
```

## `sub_100351a9` `0x100351a9`

_143 bytes. refs "exori hur"_

```c
typedef struct struct_0 {
    char padding_0[36];
    unsigned int field_24;
    unsigned int field_28;
    char padding_2c[92];
    char field_88;
    char padding_89[7];
    unsigned int field_90;
} struct_0;

extern struct_0 *g_1008b89b;
extern unsigned int g_100f9328;
extern char g_100fa97a;

struct_0 * sub_100351a9(void)
{
    struct_0 *v2;  // eax
    struct_0 *v3;  // eax
    struct_0 *v4;  // eax
    struct_0 *v5;  // eax
    struct_0 *v1;  // [bp+0xffffc], Other Possible Types: unsigned int

    g_100f9328 = 0;
    if (*((int *)0x63fe78) < 40)
        return v2;
    v1 = sub_100300ce();
    if (!g_1008b89b)
        return g_1008b89b;
    v3 = sub_1003997e(g_1008b89b);
    if (!v3)
    {
        return v3;
    }
    else if (!v3->field_90)
    {
        return v3;
    }
    else if (v3->field_88 < (v1 & 0xff))
    {
        v4 = sub_1003c23e(v3);
        if (!v4)
            return v4;
        v1 = v4;
        if (g_100fa97a)
        {
            v5 = sub_10011678(v4->field_24, v4->field_28, 0);
            if (!v5)
                return v5;
        }
        g_100f9328 = 1;
        return sub_10039413("exori hur");
    }
    else
    {
        return v3;
    }
}
```

## `sub_10035238` `0x10035238`

_143 bytes. refs "exori con"_

```c
typedef struct struct_0 {
    char padding_0[36];
    unsigned int field_24;
    unsigned int field_28;
    char padding_2c[92];
    char field_88;
    char padding_89[7];
    unsigned int field_90;
} struct_0;

extern struct_0 *g_1008b89b;
extern unsigned int g_100f9328;
extern char g_100fa97a;

struct_0 * sub_10035238(void)
{
    struct_0 *v2;  // eax
    struct_0 *v3;  // eax
    struct_0 *v4;  // eax
    struct_0 *v5;  // eax
    struct_0 *v1;  // [bp+0xffffc], Other Possible Types: unsigned int

    g_100f9328 = 0;
    if (*((int *)0x63fe78) < 35)
        return v2;
    v1 = sub_100300ce();
    if (!g_1008b89b)
        return g_1008b89b;
    v3 = sub_1003997e(g_1008b89b);
    if (!v3)
    {
        return v3;
    }
    else if (!v3->field_90)
    {
        return v3;
    }
    else if (v3->field_88 < (v1 & 0xff))
    {
        v4 = sub_1003c23e(v3);
        if (!v4)
            return v4;
        v1 = v4;
        if (g_100fa97a)
        {
            v5 = sub_10011678(v4->field_24, v4->field_28, 0);
            if (!v5)
                return v5;
        }
        g_100f9328 = 1;
        return sub_10039413("exori con");
    }
    else
    {
        return v3;
    }
}
```

## `sub_100352c7` `0x100352c7`

_158 bytes. refs "exori gran"_

```c
typedef struct struct_0 {
    char padding_0[36];
    unsigned int field_24;
    unsigned int field_28;
    char padding_2c[92];
    char field_88;
    char padding_89[7];
    unsigned int field_90;
} struct_0;

typedef struct struct_2 {
    char padding_0[36];
    unsigned int field_24;
    unsigned int field_28;
} struct_2;

extern struct_2 *g_1005f7ed;
extern struct_0 *g_1008b89b;
extern unsigned int g_100f9328;

struct_0 * sub_100352c7(void)
{
    struct_0 *v3;  // eax
    struct_0 *v4;  // eax
    struct_0 *v5;  // eax
    unsigned int v1;  // [bp+0xffffc]
    int v2;  // [bp+0x100000]

    g_100f9328 = 0;
    if (*((int *)0x63fe78) < 340)
        return v3;
    lstrcpy(/* unsupported instruction */ - 2032, v2);
    v1 = sub_100300ce();
    if (!g_1008b89b)
        return g_1008b89b;
    v4 = sub_1003997e(g_1008b89b);
    if (!v4)
    {
        return v4;
    }
    else if (!v4->field_90)
    {
        return v4;
    }
    else if (v4->field_88 < (v1 & 0xff))
    {
        v5 = sub_1003c23e(v4);
        if (!v5)
        {
            return v5;
        }
        else if (g_1005f7ed->field_24 - v5->field_24 + 1 > 2)
        {
            return v5;
        }
        else if (g_1005f7ed->field_28 - v5->field_28 + 1 <= 2)
        {
            g_100f9328 = 1;
            return sub_10039413("exori gran");
        }
        else
        {
            return v5;
        }
    }
    else
    {
        return v4;
    }
}
```

## `sub_10035365` `0x10035365`

_65 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[144];
    unsigned int field_90;
} struct_0;

extern int g_1008b89b;

struct_0 * sub_10035365(void)
{
    struct_0 *v4;  // eax
    struct_0 *v5;  // eax
    int v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    v4 = sub_100300ce();
    if (!g_1008b89b)
        return v4;
    v5 = sub_1003997e(g_1008b89b, v4, v1);
    if (!v5)
    {
        return v5;
    }
    else if (!v5->field_90)
    {
        return v5;
    }
    else if (*((int *)&v5->padding_0[0x88]) < g_1008b89b)
    {
        return sub_10030442(v4, v2, v3);
    }
    else
    {
        return v5;
    }
}
```

## `sub_100353a6` `0x100353a6`

_80 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_102e2a08;

int sub_100353a6(void)
{
    unsigned int v2;  // eax
    int v0;  // [bp+0x0]

    if (g_102e2a08 > 5 && g_102e2a08 < 50)
        return *((int *)0x64f600);
    g_102e2a08 = g_102e2a08 + 1;
    v2 = *((int *)0x64f600) + g_102e2a08;
    if (!v2 || v2 > 50)
        v2 = 1;
    if (v2 > 15)
        v2 = 15;
    sub_10002c01(v2);
    return sub_100379b6(v0);
}
```

## `sub_100353f6` `0x100353f6`

_80 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_102e2a08;

int sub_100353f6(void)
{
    unsigned int v2;  // eax
    int v0;  // [bp+0x0]

    if (g_102e2a08 < 4294967291 && g_102e2a08 > 50)
        return *((int *)0x64f600);
    g_102e2a08 = g_102e2a08 - 1;
    v2 = *((int *)0x64f600) + g_102e2a08;
    if (!v2 || v2 > 50)
        v2 = 1;
    if (v2 > 15)
        v2 = 15;
    sub_10002c01(v2);
    return sub_100379b6(v0);
}
```

## `sub_10035446` `0x10035446`

_101 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_1004339b;
extern unsigned short g_100433a0;
extern char g_100433a2;
extern unsigned short g_100433a3;
extern char g_100433a5;
extern unsigned int g_100433a6;
extern unsigned int g_10044610[4];
extern char g_10134e65;

unsigned int * sub_10035446(void)
{
    unsigned int *v2;  // eax
    unsigned int v0;  // [bp-0x4]

    v0 = sub_100300ce();
    sub_100300ce();
    v2 = sub_1003927b();
    if (!v2)
        return v2;
    g_100433a6 = *(v2);
    g_100433a0 = 0;
    g_100433a2 = 0;
    g_100433a5 = 0;
    g_100433a3 = g_10044610[g_10134e65];
    g_100433a5 = 0;
    v0 = 15;
    return sub_1002ade7(&g_1004339b);
}
```

## `sub_100354ab` `0x100354ab`

_99 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_1004339b;
extern unsigned short g_100433a0;
extern char g_100433a2;
extern unsigned short g_100433a3;
extern char g_100433a5;
extern unsigned int g_100433a6;
extern unsigned int g_100445f8[4];
extern char g_10134e64;

unsigned int * sub_100354ab(void)
{
    unsigned int *v2;  // eax
    unsigned int v0;  // [bp-0x4]

    v0 = sub_100300ce();
    sub_100300ce();
    v2 = sub_1003919a();
    if (!v2)
        return v2;
    g_100433a6 = *(v2);
    g_100433a0 = 0;
    g_100433a2 = 0;
    g_100433a5 = 0;
    g_100433a3 = g_100445f8[g_10134e64];
    g_100433a5 = 0;
    v0 = 15;
    return sub_1002ade7(&g_1004339b);
}
```

## `sub_1003550e` `0x1003550e`

_59 bytes. (leaf/helper — see body)_

```c
extern char g_1005f7dd;
extern unsigned int g_100f9328;

int sub_1003550e(void)
{
    unsigned int v1;  // eax

    g_100f9328 = 0;
    if (!g_1005f7dd)
        return v1;
    sub_10030225();
    g_100f9328 = 1;
    return sub_10039413(/* unsupported instruction */ - 2032);
}
```

## `sub_10035549` `0x10035549`

_83 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f9328;

int sub_10035549(void)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax

    g_100f9328 = 0;
    v1 = (unsigned int)sub_10030225();
    if (*((int *)0x63fe78) < 1200)
        return v1;
    v2 = sub_10038eb3(/* unsupported instruction */ - 2032, 0, 0);
    if (!v2)
        return v2;
    g_100f9328 = 1;
    return sub_1003a60a(v2, 42);
}
```

## `sub_1003559c` `0x1003559c`

_80 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100ee8bc;
extern unsigned int g_100ee8c0;
extern unsigned int g_100ee8c4;
extern unsigned int g_100f9328;

unsigned int sub_1003559c(void)
{
    unsigned int v4;  // eax
    unsigned int v1;  // [bp+0xfef74]
    unsigned int v2;  // [bp+0xfef78]
    unsigned int v3;  // [bp+0xfef7c]

    g_100f9328 = 0;
    if (g_100ee8bc)
    {
        v1 = g_100ee8bc;
        v2 = g_100ee8c0;
        v3 = g_100ee8c4;
        g_100f9328 = 1;
        v4 = sub_1003a60a(/* unsupported instruction */ - 4276, 41);
    }
    return v4;
}
```

## `sub_100355ec` `0x100355ec`

_45 bytes. (leaf/helper — see body)_

```c
unsigned int sub_100355ec(void)
{
    unsigned int v1;  // eax

    sub_10030225();
    v1 = sub_10038eb3(/* unsupported instruction */ - 2032, 0, 0);
    if (!v1)
        return v1;
    return sub_100375d9();
}
```

## `sub_10035619` `0x10035619`

_60 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f878;
extern unsigned int g_1005f87c;
extern unsigned int g_100ee8d8;

int sub_10035619(void)
{
    unsigned int v5;  // eax
    unsigned int v0;  // [bp-0x4]
    unsigned short v2;  // [bp+0xffffc]
    char v3;  // [bp+0xffffe]
    unsigned int v4;  // [bp+0x100010]

    v5 = sub_100300ce();
    v0 = v4;
    g_1005f87c = v0;
    g_1005f878 = v5;
    if (g_1005f878)
    {
        return g_1005f878;
    }
    else if (g_100ee8d8)
    {
        v2 = 1;
        v3 = g_100ee8d8;
        v0 = 3;
        return sub_1002ade7(/* unsupported instruction */ - 8);
    }
    else
    {
        return g_1005f878;
    }
}
```

## `sub_10035655` `0x10035655`

_27 bytes. (leaf/helper — see body)_

```c
int sub_10035655(void)
{
    unsigned int v0;  // [bp-0x4]
    unsigned short v2;  // [bp+0xffffc]
    char v3;  // [bp+0xffffe]

    v3 = 101;
    v2 = 1;
    v0 = 3;
    return sub_1002ade7(/* unsupported instruction */ - 8);
}
```

## `sub_1003565b` `0x1003565b`

_6 bytes. (leaf/helper — see body)_

```c
void sub_1003565b(void)
{
    char v1;  // [bp+0xffffe]

    v1 = 0x66;
}
```

## `sub_10035661` `0x10035661`

_6 bytes. (leaf/helper — see body)_

```c
void sub_10035661(void)
{
    char v1;  // [bp+0xffffe]

    v1 = 103;
}
```

## `sub_10035667` `0x10035667`

_6 bytes. (leaf/helper — see body)_

```c
void sub_10035667(void)
{
    char v1;  // [bp+0xffffe]

    v1 = 104;
}
```

## `sub_1003566d` `0x1003566d`

_6 bytes. (leaf/helper — see body)_

```c
void sub_1003566d(void)
{
    char v1;  // [bp+0xffffe]

    v1 = 106;
}
```

## `sub_10035673` `0x10035673`

_6 bytes. (leaf/helper — see body)_

```c
void sub_10035673(void)
{
    char v1;  // [bp+0xffffe]

    v1 = 107;
}
```

## `sub_10035679` `0x10035679`

_6 bytes. (leaf/helper — see body)_

```c
void sub_10035679(void)
{
    char v1;  // [bp+0xffffe]

    v1 = 108;
}
```

## `sub_1003567f` `0x1003567f`

_6 bytes. (leaf/helper — see body)_

```c
void sub_1003567f(void)
{
    char v1;  // [bp+0xffffe]

    v1 = 109;
}
```

