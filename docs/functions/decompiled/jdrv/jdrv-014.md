# elfbot.dll decompiled — jdrv 0x100336d9..0x10034705

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_100336d9` `0x100336d9`

_159 bytes. (leaf/helper — see body)_

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
extern unsigned int g_1005f85c;

int sub_100336d9(void)
{
    unsigned short v3;  // bx
    unsigned int v4;  // eax
    int v5;  // edx
    char v6;  // cl
    unsigned int v7;  // eax
    unsigned int v8;  // eax
    unsigned int v0;  // [bp-0x8]
    unsigned int v2;  // [bp+0x100000]

    v3 = v2;
    g_1004341c = sub_100300ce();
    v4 = sub_1002be32(sub_100300ce());
    if (!v4)
        return v4;
    g_1004341f = v4;
    g_10043421 = v3;
    g_10043423 = g_1005f85c;
    g_10043424 = v5;
    g_10043426 = v6;
    v7 = sub_1003c4fa(v5);
    if (v7 == 0x30003000 || v7 == 536879112)
    {
        v8 = sub_1002ae92(g_1004341c, 0, NULL);
        if (!v8)
            return v8;
        g_10043419 = v8;
        g_1004341b = v5;
        g_1004341e = v5;
    }
    else if (((char)v7 & 16))
    {
        g_10043426 = 1;
    }
    v0 = 19;
    return sub_1002ade7(&g_10043414);
}
```

## `sub_10033778` `0x10033778`

_133 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_1004343a;
extern unsigned short g_10043442;
extern char g_10043447;
extern char g_10043449;
extern unsigned short g_1004344a;
extern char g_1004344c;

int sub_10033778(void)
{
    unsigned int v2;  // eax
    unsigned int i;  // ecx
    unsigned int v4;  // edx
    unsigned int v5;  // eax
    char v6;  // dl
    unsigned int v0;  // [bp-0x4]

    g_10043442 = sub_100300ce();
    v2 = sub_100300ce();
    g_1004344a = v2;
    i = 1;
    for (v4 = 6605976; i <= 10; i += 1)
    {
        if (*((int *)v4) == v2)
        {
            g_10043447 = i;
            g_10043449 = 0;
            g_1004344c = 0;
            v0 = 19;
            return sub_1002ade7(&g_1004343a);
        }
        v4 += 12;
    }
    v5 = sub_1002ae92(v2, 0, NULL);
    if (!v5)
        return v5;
    g_10043447 = v5;
    g_10043449 = v6;
    g_1004344c = v6;
    v0 = 19;
    return sub_1002ade7(&g_1004343a);
}
```

## `sub_100337fd` `0x100337fd`

_162 bytes. (leaf/helper — see body)_

```c
extern void g_100432e5;
extern char g_100432e7;
extern unsigned short g_100432e8;
extern char g_100432ea;
extern unsigned int g_100432eb;
extern unsigned int g_100f9328;
extern char g_100fa4f0;

unsigned int * sub_100337fd(void)
{
    unsigned int v3;  // ebx
    unsigned int *v4;  // eax
    unsigned int *v5;  // ebx
    unsigned int *v6;  // eax
    char v7;  // dl
    unsigned int *v0;  // [bp-0x10], Other Possible Types: unsigned int

    g_100f9328 = 0;
    sub_100300ce();
    v3 = /* unsupported instruction */ - 2032;
    v4 = sub_10038eb3(/* unsupported instruction */ - 2032, 0, 0, (unsigned int)sub_10030225());
    if (!v4)
        return v4;
    g_100432e8 = v3;
    if (!g_100fa4f0)
    {
        v0 = v4;
        v5 = v4;
        v6 = sub_1002ae92(v3, 0, NULL);
        if (!v6)
            return v6;
        g_100432e5 = *((char *)&v6);
        g_100432e7 = v7;
        g_100432ea = v7;
    }
    else
    {
        v5 = v4;
        *((unsigned short *)&g_100432e5) = 0;
        g_100432e7 = 0;
        g_100432ea = 0;
    }
    g_100432eb = *(v5);
    g_100f9328 = 1;
    v0 = 15;
    return sub_1002ade7("\r");
}
```

## `sub_1003389f` `0x1003389f`

_9 bytes. (leaf/helper — see body)_

```c
void sub_1003389f(void)
{
    sub_1003867e();
    return;
}
```

## `sub_100338a8` `0x100338a8`

_195 bytes. (leaf/helper — see body)_

```c
extern void g_100432e5;
extern char g_100432e7;
extern unsigned short g_100432e8;
extern char g_100432ea;
extern unsigned int g_100432eb;
extern unsigned int g_100f9328;
extern char g_100fa4f0;

unsigned int [35] sub_100338a8(void)
{
    unsigned int v2[35];  // eax
    unsigned int v3[35];  // eax
    unsigned int v4[35];  // eax
    char v5;  // dl
    unsigned int v0[35];  // [bp-0x10], Other Possible Types: unsigned int

    g_100f9328 = 0;
    sub_100300ce();
    v2 = sub_10038eb3(/* unsupported instruction */ - 2032, 0, 0, (unsigned int)sub_10030225());
    if (!v2)
        return v3;
    v3 = v2;
    if (!v3)
    {
        return v3;
    }
    else if (v3[0x22] < /* unsupported instruction */ - 2032)
    {
        v0 = v3;
        v4 = sub_1002ae92(3160, 0, NULL);
        if (!v4 && !g_100fa4f0)
            return v4;
        if (!g_100fa4f0)
        {
            g_100432e5 = *((char *)&v4);
            g_100432e7 = v5;
            g_100432ea = v5;
        }
        else
        {
            *((unsigned short *)&g_100432e5) = 0;
            g_100432e7 = 0;
            g_100432ea = 0;
        }
        g_100432e8 = 3160;
        g_100432eb = v3[0];
        g_100f9328 = 1;
        v0 = 15;
        return sub_1002ade7("\r");
    }
    else
    {
        return v3;
    }
}
```

## `sub_1003396b` `0x1003396b`

_275 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern unsigned int g_1008b7f3[2];
extern unsigned int g_1008b893[2];
extern unsigned int g_1008b897;
extern unsigned int g_100f9328;

struct_0 * sub_1003396b(void)
{
    struct_0 *v4;  // eax
    struct_0 *v5;  // eax
    unsigned int v6[2];  // ecx
    unsigned int count;  // eax
    struct_0 *v0;  // [bp-0x10]
    unsigned int v2;  // [bp+0xffffc]
    unsigned int v3;  // [bp+0x100000]

    g_100f9328 = 0;
    sub_10030225();
    v4 = sub_10038eb3(/* unsupported instruction */ - 2032, 0, 0);
    v2 = v3;
    while (true)
    {
        v5 = v4;
        if (!v4)
            return v5;
        v6 = &g_1008b7f3[0];
        while (true)
        {
            if (v6 >= &g_1008b893[0])
            {
                g_1008b893[0] = v5->field_4;
                g_1008b897 = 8;
                g_100f9328 = 1;
                return sub_1003a60a(v5, 40);
            }
            if (v6[0] == v5->field_4)
                break;
            if (!v6[0])
            {
                g_1008b893[0] = v5->field_4;
                g_1008b897 = 8;
                g_100f9328 = 1;
                return sub_1003a60a(v5, 40);
            }
            v6 += 1;
        }
        v0 = v5;
        count = GetTickCount();
        if (count - v6[1] >= 20000)
        {
            g_1008b893[0] = v5->field_4;
            g_1008b897 = 8;
            g_100f9328 = 1;
            return sub_1003a60a(v5, 40);
        }
        else if (v2 == 1)
        {
            v4 = sub_1003bc54();
        }
        else if (v2 == 6)
        {
            v4 = sub_1003bc54();
        }
        else if (v2 == 2)
        {
            v4 = sub_1003bec5();
        }
        else if (v2 == 7)
        {
            v4 = sub_1003bec5();
        }
        else
        {
            return v5;
        }
    }
}
```

## `sub_100339e0` `0x100339e0`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100339e0(void)
{
}
```

## `sub_100339fa` `0x100339fa`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100339fa(void)
{
}
```

## `sub_10033a1c` `0x10033a1c`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10033a1c(void)
{
}
```

## `sub_10033a45` `0x10033a45`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10033a45(void)
{
}
```

## `sub_10033a86` `0x10033a86`

_155 bytes. refs "Demon"_

```c
typedef struct struct_0 {
    char padding_0[36];
    unsigned int field_24;
} struct_0;

typedef struct struct_1 {
    char padding_0[40];
    unsigned int field_28;
    unsigned int field_2c;
    char padding_30[96];
    char field_90;
} struct_1;

extern char g_1005f858;
extern char g_1005f85c;
extern int g_100f94cb;

int sub_10033a86(void)
{
    struct_1 *iter;  // ebx
    int v4;  // eax
    unsigned int v5;  // ecx
    unsigned int v1;  // [bp+0xff000]
    struct_1 *v2;  // [bp+0xffffc], Other Possible Types: struct_0 *

    v1 = 50000;
    v2 = NULL;
    iter = 0x63fef8;
    while (true)
    {
        if (!iter->field_90)
        {
            if (iter >= 0x64a308)
                break;
            iter = &iter[1].padding_0[23];
        }
        else
        {
            v4 = lstrcmpi("Demon", &iter->padding_0[4]);
            if (!v4 && iter->field_28 == *((int *)&g_1005f858) && iter->field_2c == *((int *)&g_1005f85c))
            {
                v5 = *((int *)&iter->padding_0[36]);
                if (v5 < v1)
                {
                    v2 = iter;
                    v1 = v5;
                }
            }
            if (iter >= 0x64a308)
                break;
            iter = &iter[1].padding_0[23];
        }
    }
    if (!v2)
        return v4;
    sub_1003a60a(v2, g_100f94cb);
    return v2->field_24;
}
```

## `sub_10033ab5` `0x10033ab5`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10033ab5(void)
{
}
```

## `sub_10033b23` `0x10033b23`

_21 bytes. (leaf/helper — see body)_

```c
int sub_10033b23(void)
{
    sub_100300ce();
    return sub_10037694();
}
```

## `sub_10033b38` `0x10033b38`

_27 bytes. (leaf/helper — see body)_

```c
extern char g_10080ba6;

void* sub_10033b38(void)
{
    void* v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    if (!g_10080ba6)
        v4 = sub_10030442(v1, v2, v3);
    return v4;
}
```

## `sub_10033b53` `0x10033b53`

_50 bytes. (leaf/helper — see body)_

```c
int sub_10033b53(void)
{
    sub_10030225();
    sub_10030225();
    return sub_1002583e(/* unsupported instruction */ - 2032, /* unsupported instruction */ - 0x1000, 0);
}
```

## `sub_10033b85` `0x10033b85`

_50 bytes. (leaf/helper — see body)_

```c
int sub_10033b85(void)
{
    sub_10030225();
    sub_10030225();
    return sub_1002583e(/* unsupported instruction */ - 2032, /* unsupported instruction */ - 0x1000, 1);
}
```

## `sub_10033bb7` `0x10033bb7`

_30 bytes. (leaf/helper — see body)_

```c
int sub_10033bb7(void)
{
    sub_10030225();
    return sub_100252ba(/* unsupported instruction */ - 0x1000);
}
```

## `sub_10033bd5` `0x10033bd5`

_39 bytes. (leaf/helper — see body)_

```c
int sub_10033bd5(void)
{
    sub_10030225();
    return sub_1002583e(/* unsupported instruction */ - 2032, /* unsupported instruction */ - 0x1000, 2);
}
```

## `sub_10033bfc` `0x10033bfc`

_137 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1008ab93;
extern unsigned int g_1008ab97;
extern unsigned int g_100f0e30;

int sub_10033bfc(void)
{
    unsigned int v5;  // eax
    unsigned int v6;  // eax
    unsigned int v1;  // [bp+0xffffc]
    int v2;  // [bp+0x100000]
    void* v3;  // [bp+0x100010]
    int v4;  // [bp+0x100014]

    v1 = 0;
    if (v3 == 0xffffffff)
        g_1008ab97 = 0;
    else
        g_1008ab93 = 0;
    while (true)
    {
        v5 = sub_100300ce();
        if (!v5)
            return v5;
        lstrcpy(/* unsupported instruction */ - 2032, v2);
        v6 = sub_10030442(/* unsupported instruction */ - 2032, v3, v4);
        if (v3 == 0xffffffff)
        {
            if (g_1008ab97)
            {
                return v6;
            }
            else if (g_100f0e30)
            {
                return v6;
            }
        }
        else
        {
            if (g_1008ab93)
                return v6;
        }
        v1 += 1;
        if (v1 >= 1000)
            return v6;
    }
}
```

## `sub_10033c66` `0x10033c66`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10033c66(void)
{
}
```

## `sub_10033c87` `0x10033c87`

_142 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1008ab93;
extern unsigned int g_1008ab97;
extern unsigned int g_100f0e30;

unsigned int sub_10033c87(void)
{
    int v6;  // ebx
    unsigned int v7;  // eax
    int v0;  // [bp-0x8]
    unsigned int i;  // [bp+0xffffc]
    int v3;  // [bp+0x100000]
    void* v4;  // [bp+0x100010]
    int v5;  // [bp+0x100014]

    i = 0;
    if (v4 == 0xffffffff)
        g_1008ab97 = 0;
    else
        g_1008ab93 = 0;
    v6 = v3;
    v7 = sub_100300ce();
    while (i < v7)
    {
        lstrcpy(/* unsupported instruction */ - 2032, v6);
        v0 = v6;
        sub_10030442(/* unsupported instruction */ - 2032, v4, v5);
        if (v4 == 0xffffffff)
        {
            if (g_1008ab97)
            {
                return v7;
            }
            else if (g_100f0e30)
            {
                return v7;
            }
        }
        else
        {
            if (g_1008ab93)
                return v7;
        }
        i += 1;
        if (i >= 1000)
            return v7;
    }
    return v7;
}
```

## `sub_10033cf6` `0x10033cf6`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10033cf6(void)
{
}
```

## `sub_10033d17` `0x10033d17`

_1254 bytes. refs "allcreatures", "allmonsters", "allplayers"_

```c
typedef struct struct_1 {
    char padding_0[3];
    char field_3;
    char padding_4[32];
    int field_24;
    int field_28;
    char padding_2c[100];
    unsigned int field_90;
} struct_1;

typedef struct struct_0 {
    char field_0;
    char padding_1[31];
    char field_20;
    char padding_21[479];
    char field_200;
} struct_0;

extern void g_1005f85c;
extern unsigned int g_1008910b[4];
extern unsigned int g_10089c8b;
extern unsigned int g_1008ab93;
extern unsigned int g_1008ab97;
extern unsigned int g_100f0e30;
extern struct_0 *g_100f49d1;
extern char g_100f49d5;
extern unsigned int g_100f49ed;

int sub_10033d17(void)
{
    char *i;  // ebx
    unsigned int dst;  // eax
    unsigned int v22;  // eax
    char iter[513];  // ebx
    char v15[513];  // edi
    unsigned int v16;  // eax
    struct_1 *k;  // ebx
    struct_1 *v18;  // ebx
    unsigned int v19;  // eax
    unsigned int idx;  // ebx
    unsigned int v21;  // eax
    struct_1 *v0;  // [bp-0x8]
    char v1[513];  // [bp-0x4], Other Possible Types: unsigned int
    char v3;  // [bp+0xff004]
    unsigned int v4;  // [bp+0xfffec]
    unsigned int v5;  // [bp+0xffff0]
    unsigned int v6;  // [bp+0xffff4]
    unsigned int v7;  // [bp+0xffff8]
    char v8[513];  // [bp+0xffffc]
    char *v9;  // [bp+0x100000]
    void* v10;  // [bp+0x100010]
    int v11;  // [bp+0x100014]

    i = v9;
    sub_10030225();
    for (; *(i) == 32; i += 1);
    dst = sub_10030326();
    v9 = i;
    if (v3 != 36)
        return dst;
    iter = g_100f49d1;
    v15 = g_100f49d1[0x1ff].padding_1;
    for (*((char *[513])&v8[0]) = NULL; iter < v15; iter = &iter[0x200])
    {
        if (iter[0])
        {
            v1 = v15;
            if (!lstrcmpi(iter, /* unsupported instruction */ - 0xfff))
            {
                iter[32] = 0;
                *((char *[513])&v8[0]) = iter;
                break;
            }
        }
        else
        {
            dst = lstrcpy(iter, /* unsupported instruction */ - 0xfff);
            iter[32] = 0;
            *((char *[513])&v8[0]) = iter;
            break;
        }
    }
    if (v10 == 0xffffffff)
        g_1008ab97 = 0;
    else
        g_1008ab93 = 0;
    if (!v8)
        return dst;
    v16 = lstrcmpi(/* unsupported instruction */ - 2032, "allcreatures");
    if (!v16)
    {
        v7 = 1;
        v6 = 1;
        v5 = 4294967295;
        v4 = 0;
    }
    else
    {
        v16 = lstrcmpi(/* unsupported instruction */ - 2032, "allmonsters");
        if (!v16)
        {
            v7 = 1;
            v6 = 0;
            v5 = 4294967295;
            v4 = 0;
        }
        else
        {
            v16 = lstrcmpi(/* unsupported instruction */ - 2032, "allplayers");
            if (!v16)
            {
                v7 = 0;
                v6 = 1;
                v5 = 4294967295;
                v4 = 0;
            }
            else
            {
                v16 = lstrcmpi(/* unsupported instruction */ - 2032, "floormonsters");
                if (!v16)
                {
                    v7 = 1;
                    v6 = 0;
                    v1 = *((int *)&g_1005f85c);
                    v5 = *((int *)&g_1005f85c);
                    v4 = 0;
                }
                else
                {
                    v16 = lstrcmpi(/* unsupported instruction */ - 2032, "floorplayers");
                    if (!v16)
                    {
                        v7 = 0;
                        v6 = 1;
                        v1 = *((int *)&g_1005f85c);
                        v5 = *((int *)&g_1005f85c);
                        v4 = 0;
                    }
                    else
                    {
                        v16 = lstrcmpi(/* unsupported instruction */ - 2032, "floorcreatures");
                        if (!v16)
                        {
                            v7 = 1;
                            v6 = 1;
                            v1 = *((int *)&g_1005f85c);
                            v5 = *((int *)&g_1005f85c);
                            v4 = 0;
                        }
                        else
                        {
                            v16 = lstrcmpi(/* unsupported instruction */ - 2032, "screenplayers");
                            if (!v16)
                            {
                                v7 = 0;
                                v6 = 1;
                                v1 = *((int *)&g_1005f85c);
                                v5 = *((int *)&g_1005f85c);
                                v4 = 1;
                            }
                            else
                            {
                                v16 = lstrcmpi(/* unsupported instruction */ - 2032, "screenmonsters");
                                if (!v16)
                                {
                                    v7 = 1;
                                    v6 = 0;
                                    v1 = *((int *)&g_1005f85c);
                                    v5 = *((int *)&g_1005f85c);
                                    v4 = 1;
                                }
                                else
                                {
                                    v16 = lstrcmpi(/* unsupported instruction */ - 2032, "screencreatures");
                                    if (!v16)
                                    {
                                        v7 = 1;
                                        v6 = 1;
                                        v1 = *((int *)&g_1005f85c);
                                        v5 = *((int *)&g_1005f85c);
                                        v4 = 1;
                                    }
                                    else
                                    {
                                        v16 = lstrcmpi(/* unsupported instruction */ - 2032, "shootableplayers");
                                        if (!v16)
                                        {
                                            v7 = 0;
                                            v6 = 1;
                                            v1 = *((int *)&g_1005f85c);
                                            v5 = *((int *)&g_1005f85c);
                                            v4 = 2;
                                        }
                                        else
                                        {
                                            v16 = lstrcmpi(/* unsupported instruction */ - 2032, "shootablemonsters");
                                            if (!v16)
                                            {
                                                v7 = 1;
                                                v6 = 0;
                                                v1 = *((int *)&g_1005f85c);
                                                v5 = *((int *)&g_1005f85c);
                                                v4 = 2;
                                            }
                                            else
                                            {
                                                v16 = lstrcmpi(/* unsupported instruction */ - 2032, "shootablecreatures");
                                                if (!v16)
                                                {
                                                    v7 = 1;
                                                    v6 = 1;
                                                    v1 = *((int *)&g_1005f85c);
                                                    v5 = *((int *)&g_1005f85c);
                                                    v4 = 2;
                                                }
                                                else
                                                {
                                                    v19 = lstrcmpi(/* unsupported instruction */ - 2032, "newmessages");
                                                    if (v19)
                                                    {
                                                        return v19;
                                                    }
                                                    else if (v10 == 0xffffffff)
                                                    {
                                                        return v19;
                                                    }
                                                    else
                                                    {
                                                        idx = v10 * 4;
                                                        v21 = *((int *)(idx + (char *)&g_1008910b[0]));
                                                        while (true)
                                                        {
                                                            if (v21 == *((int *)(idx + (char *)&g_10089c8b)))
                                                                return v21;
                                                            v1 = *((int *)(idx + (char *)&g_1008910b[0])) * 316 + g_100f49ed;
                                                            wsprintfA(&v8[32], "%d");
                                                            lstrcpy(/* unsupported instruction */ - 2032, v9);
                                                            v22 = sub_10030442(/* unsupported instruction */ - 2032, v10, v11);
                                                            idx = v10 * 4;
                                                            v1 = *((int *)(idx + (char *)&g_1008910b[0]));
                                                            *((int *)(idx + (char *)&g_10089c8b)) = *((int *)(idx + (char *)&g_1008910b[0]));
                                                            if (v10 == 0xffffffff)
                                                            {
                                                                if (g_1008ab97 || g_100f0e30)
                                                                    break;
                                                            }
                                                            else
                                                            {
                                                                if (g_1008ab93)
                                                                    return v22;
                                                            }
                                                            if (*((int *)(idx + (char *)&g_1008910b[0])) != *((int *)&g_100f49d5))
                                                            {
                                                                *((unsigned int *)(idx + (char *)&g_1008910b[0])) = *((int *)(idx + (char *)&g_1008910b[0])) + 1;
                                                                if (*((int *)(idx + (char *)&g_1008910b[0])) >= 2000)
                                                                    *((unsigned int *)(idx + (char *)&g_1008910b[0])) = 0;
                                                            }
                                                            v21 = *((int *)(idx + (char *)&g_1008910b[0]));
                                                        }
                                                        return v22;
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
    k = 0x63fef8;
    while (k < 0x64a308)
    {
        v16 = *((int *)&g_1005f85c);
        if (!(k->field_90 && (v7 && k->field_3 == 64 || v6 && k->field_3 < 64) && (v5 == 0xffffffff || *((int *)&g_1005f85c) == *((int *)&k->padding_2c[0]))))
        {
            k = &k[1].padding_4[16];
        }
        else if (v4)
        {
            v16 = sub_1003c23e(k, k);
            v18 = k;
            if (!v16)
            {
                k = &v18[1].padding_4[16];
            }
            else if (v4 == 2)
            {
                v0 = v18;
                v16 = sub_10011678(v18->field_24, v18->field_28, 0);
                if (v16)
                    return sub_10034107();
                k = &v18[1].padding_4[16];
            }
            else
            {
                return sub_10034107();
            }
        }
        else
        {
            return sub_10034107();
        }
    }
    return v16;
}
```

## `sub_10033d82` `0x10033d82`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10033d82(void)
{
}
```

## `sub_10034107` `0x10034107`

_97 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1008ab93;
extern unsigned int g_1008ab97;
extern unsigned int g_100f0e30;

void* sub_10034107(void)
{
    unsigned int v7;  // ebx
    void* v8;  // eax
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp-0x4]
    PSTR v3;  // [bp+0xffffc]
    int v4;  // [bp+0x100000]
    void* v5;  // [bp+0x100010]
    int v6;  // [bp+0x100014]

    v1 = v7;
    v0 = v7;
    wsprintfA(v3 + 32, "%d");
    lstrcpy(/* unsupported instruction */ - 2032, v4);
    v8 = sub_10030442(/* unsupported instruction */ - 2032, v5, v6);
    if (v5 != 0xffffffff)
    {
        if (!g_1008ab93)
            goto LABEL_0x1003416a;
        return v8;
    }
    if (!g_1008ab97)
        if (!g_100f0e30)
            goto LABEL_0x1003416a;
        else
            goto LABEL_10034157;
LABEL_10034157:
    return v8;
}
```

## `sub_1003415b` `0x1003415b`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003415b(void)
{
}
```

## `sub_10034211` `0x10034211`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10034211(void)
{
}
```

## `sub_10034264` `0x10034264`

_27 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f49c9;

void* sub_10034264(void)
{
    void* v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    if (g_100f49c9)
        v4 = sub_10030442(v1, v2, v3);
    return v4;
}
```

## `sub_1003427f` `0x1003427f`

_27 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f49c9;

void* sub_1003427f(void)
{
    void* v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    if (!g_100f49c9)
        v4 = sub_10030442(v1, v2, v3);
    return v4;
}
```

## `sub_1003429a` `0x1003429a`

_27 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f49cd;

void* sub_1003429a(void)
{
    void* v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    if (g_100f49cd)
        v4 = sub_10030442(v1, v2, v3);
    return v4;
}
```

## `sub_100342b5` `0x100342b5`

_27 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f49cd;

void* sub_100342b5(void)
{
    void* v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    if (!g_100f49cd)
        v4 = sub_10030442(v1, v2, v3);
    return v4;
}
```

## `sub_100342d0` `0x100342d0`

_27 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f561;

void* sub_100342d0(void)
{
    void* v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    if (g_1005f561)
        v4 = sub_10030442(v1, v2, v3);
    return v4;
}
```

## `sub_100342eb` `0x100342eb`

_27 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f565;

void* sub_100342eb(void)
{
    void* v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    if (g_1005f565)
        v4 = sub_10030442(v1, v2, v3);
    return v4;
}
```

## `sub_10034306` `0x10034306`

_27 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f569;

void* sub_10034306(void)
{
    void* v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    if (g_1005f569)
        v4 = sub_10030442(v1, v2, v3);
    return v4;
}
```

## `sub_10034321` `0x10034321`

_32 bytes. (leaf/helper — see body)_

```c
extern char g_1005f85c;

int sub_10034321(void)
{
    unsigned int v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    v4 = sub_100300ce();
    if (v4 != *((int *)&g_1005f85c))
        return v4;
    return sub_10030442(v1, v2, v3);
}
```

## `sub_10034341` `0x10034341`

_91 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[144];
    unsigned int field_90;
} struct_0;

extern int g_1008b89b;

struct_0 * sub_10034341(void)
{
    struct_0 *v4;  // eax
    unsigned int v5;  // eax
    struct_0 *v6;  // eax
    struct_0 *v7;  // eax
    int v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    v4 = (unsigned int)sub_10030225();
    if (!g_1008b89b)
        return v4;
    v5 = sub_1003997e(g_1008b89b, v1);
    v6 = sub_1003c23e(v5);
    if (!v6)
    {
        return v6;
    }
    else if (v6->field_90)
    {
        v7 = lstrcmpi(/* unsupported instruction */ - 2032, &v6->padding_0[4]);
        if (v7)
            return v7;
        return sub_10030442(v5, v2, v3);
    }
    else
    {
        return v6;
    }
}
```

## `sub_1003439c` `0x1003439c`

_88 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[144];
    unsigned int field_90;
} struct_0;

struct_0 * sub_1003439c(void)
{
    unsigned int v4;  // eax
    struct_0 *v5;  // eax
    struct_0 *v6;  // eax
    int v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    sub_10030225();
    if (!*((int *)0x63fe64))
        return *((int *)0x63fe64);
    v4 = sub_1003997e(*(0x63fe64), v1);
    v5 = sub_1003c23e(v4);
    if (!v5)
    {
        return v5;
    }
    else if (v5->field_90)
    {
        v6 = lstrcmpi(/* unsupported instruction */ - 2032, &v5->padding_0[4]);
        if (v6)
            return v6;
        return sub_10030442(v4, v2, v3);
    }
    else
    {
        return v5;
    }
}
```

## `sub_100343f4` `0x100343f4`

_28 bytes. (leaf/helper — see body)_

```c
void* sub_100343f4(void)
{
    void* v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    v4 = 0x63fe64;
    if (*((int *)0x63fe64))
        v4 = sub_10030442(v1, v2, v3);
    return v4;
}
```

## `sub_10034410` `0x10034410`

_28 bytes. (leaf/helper — see body)_

```c
void* sub_10034410(void)
{
    void* v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    v4 = 0x63fe64;
    if (!*((int *)0x63fe64))
        v4 = sub_10030442(v1, v2, v3);
    return v4;
}
```

## `sub_1003442c` `0x1003442c`

_27 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f0e20;

void* sub_1003442c(void)
{
    void* v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    if (g_100f0e20)
        v4 = sub_10030442(v1, v2, v3);
    return v4;
}
```

## `sub_10034447` `0x10034447`

_115 bytes. (leaf/helper — see body)_

```c
extern char g_1005f85c;
extern unsigned int g_100f0e20;

int sub_10034447(void)
{
    unsigned int v5;  // eax
    unsigned int i[37];  // ecx
    unsigned int v7[37];  // ecx
    unsigned int v0[37];  // [bp-0x4]
    void* v2;  // [bp+0x100000]
    void* v3;  // [bp+0x100010]
    int v4;  // [bp+0x100014]

    if (!g_100f0e20)
        sub_10030442(v2, v3, v4);
    v5 = (unsigned int)sub_10030225();
    for (i = 0x63fef8; i < 0x64a308; i = &v7[1 + 5])
    {
        if (i[36])
        {
            v5 = *((int *)&g_1005f85c);
            if (*((int *)&g_1005f85c) == i[11])
            {
                v0 = i;
                v5 = lstrcmpi(&i[1], /* unsupported instruction */ - 2032);
                if (!v5)
                    v5 = sub_10030442(v2, v3, v4);
            }
        }
    }
    return v5;
}
```

## `sub_100344ba` `0x100344ba`

_96 bytes. (leaf/helper — see body)_

```c
extern char g_1005f85c;

int sub_100344ba(void)
{
    unsigned int i[37];  // ecx
    unsigned int v6;  // eax
    unsigned int v0[37];  // [bp-0x4]
    void* v2;  // [bp+0x100000]
    void* v3;  // [bp+0x100010]
    int v4;  // [bp+0x100014]

    sub_10030225();
    for (i = 0x63fef8; i < 0x64a308; i = &i[1 + 5])
    {
        if (i[36] && *((int *)&g_1005f85c) == i[11])
        {
            v0 = i;
            v6 = lstrcmpi(&i[1], /* unsupported instruction */ - 2032);
            if (!v6)
                return v6;
        }
    }
    return sub_10030442(v2, v3, v4);
}
```

## `sub_1003451a` `0x1003451a`

_27 bytes. (leaf/helper — see body)_

```c
extern char g_1005f7de;

void* sub_1003451a(void)
{
    void* v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    if (g_1005f7de)
        v4 = sub_10030442(v1, v2, v3);
    return v4;
}
```

## `sub_10034535` `0x10034535`

_27 bytes. (leaf/helper — see body)_

```c
extern char g_1005f7df;

void* sub_10034535(void)
{
    void* v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    if (g_1005f7df)
        v4 = sub_10030442(v1, v2, v3);
    return v4;
}
```

## `sub_10034550` `0x10034550`

_27 bytes. (leaf/helper — see body)_

```c
extern char g_1005f7dc;

void* sub_10034550(void)
{
    void* v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    if (g_1005f7dc)
        v4 = sub_10030442(v1, v2, v3);
    return v4;
}
```

## `sub_1003456b` `0x1003456b`

_27 bytes. (leaf/helper — see body)_

```c
extern char g_1005f7dd;

void* sub_1003456b(void)
{
    void* v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    if (g_1005f7dd)
        v4 = sub_10030442(v1, v2, v3);
    return v4;
}
```

## `sub_10034586` `0x10034586`

_27 bytes. (leaf/helper — see body)_

```c
extern char g_1005f7dd;

void* sub_10034586(void)
{
    void* v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    if (!g_1005f7dd)
        v4 = sub_10030442(v1, v2, v3);
    return v4;
}
```

## `sub_100345a1` `0x100345a1`

_27 bytes. (leaf/helper — see body)_

```c
extern char g_1005f7dc;

void* sub_100345a1(void)
{
    void* v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    if (!g_1005f7dc)
        v4 = sub_10030442(v1, v2, v3);
    return v4;
}
```

## `sub_100345bc` `0x100345bc`

_27 bytes. (leaf/helper — see body)_

```c
extern char g_1005f7d9;

void* sub_100345bc(void)
{
    void* v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    if (g_1005f7d9)
        v4 = sub_10030442(v1, v2, v3);
    return v4;
}
```

## `sub_100345d7` `0x100345d7`

_27 bytes. (leaf/helper — see body)_

```c
extern char g_1005f7d9;

void* sub_100345d7(void)
{
    void* v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    if (!g_1005f7d9)
        v4 = sub_10030442(v1, v2, v3);
    return v4;
}
```

## `sub_100345f2` `0x100345f2`

_23 bytes. refs "utani hur"_

```c
extern char g_1005f7dc;

void sub_100345f2(void)
{
    if (!g_1005f7dc)
        sub_10039413("utani hur");
    return;
}
```

## `sub_10034609` `0x10034609`

_23 bytes. refs "utani gran hur"_

```c
extern char g_1005f7dc;

void sub_10034609(void)
{
    if (!g_1005f7dc)
        sub_10039413("utani gran hur");
    return;
}
```

## `sub_10034620` `0x10034620`

_23 bytes. refs "utani tempo hur"_

```c
extern char g_1005f7dc;

void sub_10034620(void)
{
    if (!g_1005f7dc)
        sub_10039413("utani tempo hur");
    return;
}
```

## `sub_10034637` `0x10034637`

_23 bytes. refs "utamo tempo san"_

```c
extern char g_1005f7dc;

void sub_10034637(void)
{
    if (!g_1005f7dc)
        sub_10039413("utamo tempo san");
    return;
}
```

## `sub_1003464e` `0x1003464e`

_41 bytes. refs "utamo vita"_

```c
extern char g_1005f7d9;
extern unsigned int g_1008b8dc;

void sub_1003464e(void)
{
    if (g_1005f7d9)
    {
        if (g_1008b8dc >= 50)
        {
            return;
        }
        else if (!g_1008b8dc)
        {
            return;
        }
    }
    sub_10039413("utamo vita");
    return;
}
```

## `sub_10034677` `0x10034677`

_38 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[80];
    char field_50;
} struct_0;

extern unsigned int g_1008b8e8;
extern char g_100ee8dc;

struct_0 * sub_10034677(void)
{
    struct_0 *v1;  // eax

    g_100ee8dc = 0;
    if (*((int *)0x63fe78) >= 250 && !g_1008b8e8)
        v1 = sub_10024d66();
    return v1;
}
```

## `sub_1003469d` `0x1003469d`

_36 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1008b8e8;

int sub_1003469d(void)
{
    unsigned int v1;  // eax

    v1 = (unsigned int)sub_10030225();
    if (g_1008b8e8)
        return v1;
    return sub_10024d66();
}
```

## `sub_100346c1` `0x100346c1`

_34 bytes. (leaf/helper — see body)_

```c
extern char g_100f0e7c;

int sub_100346c1(void)
{
    unsigned int v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    v4 = sub_100300ce();
    if (*((int *)&g_100f0e7c) >= v4)
        return v4;
    return sub_10030442(v1, v2, v3);
}
```

## `sub_100346e3` `0x100346e3`

_34 bytes. (leaf/helper — see body)_

```c
extern char g_100f0e7c;

int sub_100346e3(void)
{
    unsigned int v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    v4 = sub_100300ce();
    if (*((int *)&g_100f0e7c) < v4)
        return v4;
    return sub_10030442(v1, v2, v3);
}
```

## `sub_10034705` `0x10034705`

_40 bytes. (leaf/helper — see body)_

```c
void* sub_10034705(void)
{
    void* v4;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    v4 = sub_100300ce() * 100;
    if (*((int *)0x63fe68) >= v4)
        return v4;
    return sub_10030442(v1, v2, v3);
}
```

