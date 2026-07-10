# elfbot.dll decompiled — jdrv 0x1002f158..0x10030c4c

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1002f158` `0x1002f158`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1002f158(void)
{
}
```

## `sub_1002f179` `0x1002f179`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002f179(void)
{
}
```

## `sub_1002f193` `0x1002f193`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002f193(void)
{
}
```

## `sub_1002f1ad` `0x1002f1ad`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002f1ad(void)
{
}
```

## `sub_1002f1c7` `0x1002f1c7`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002f1c7(void)
{
}
```

## `sub_1002f269` `0x1002f269`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1002f269(void)
{
}
```

## `sub_1002f294` `0x1002f294`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1002f294(void)
{
}
```

## `sub_1002f2bf` `0x1002f2bf`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1002f2bf(void)
{
}
```

## `sub_1002f2f3` `0x1002f2f3`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1002f2f3(void)
{
}
```

## `sub_1002f324` `0x1002f324`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1002f324(void)
{
}
```

## `sub_1002f349` `0x1002f349`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1002f349(void)
{
}
```

## `sub_1002f374` `0x1002f374`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002f374(void)
{
}
```

## `sub_1002f39c` `0x1002f39c`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002f39c(void)
{
}
```

## `sub_1002f3c4` `0x1002f3c4`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002f3c4(void)
{
}
```

## `sub_1002f442` `0x1002f442`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002f442(void)
{
}
```

## `sub_1002ff85` `0x1002ff85`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002ff85(void)
{
    return;
}
```

## `sub_1002ff87` `0x1002ff87`

_27 bytes. (leaf/helper — see body)_

```c
void sub_1002ff87(void)
{
    char *iter;  // esi
    char v2;  // cl

    v2 = *(iter);
    if (*(iter) >= 65 && v2 <= 90)
    {
        *(iter) = v2 | 32;
    }
    else if (!v2)
    {
        return;
    }
}
```

## `sub_1002ffa2` `0x1002ffa2`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1002ffa2(void)
{
    return;
}
```

## `sub_1002ffa3` `0x1002ffa3`

_81 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_100433e9;
extern unsigned short g_100433f1;
extern char g_100433f6;
extern unsigned short g_100433f9;

unsigned int sub_1002ffa3(unsigned short a0)
{
    unsigned int v0;  // [bp-0x4]

    g_100433f1 = a0;
    if (*((int *)0x64ccb0))
    {
        g_100433f6 = 3;
        g_100433f9 = *((int *)0x64ccb0);
    }
    else if (*((int *)0x64cd04))
    {
        g_100433f6 = 10;
        g_100433f9 = *((int *)0x64cd04);
    }
    else
    {
        return 0;
    }
    v0 = 19;
    sub_1002ade7(&g_100433e9);
    return 1;
}
```

## `sub_1002fff4` `0x1002fff4`

_87 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
    char padding_1[35];
    unsigned int field_24;
} struct_0;

extern struct_0 g_100ec0b6;

int sub_1002fff4(void)
{
    int v2;  // ebx
    int len;  // eax
    struct_0 *i;  // ebx
    unsigned int v5;  // ecx
    int v6;  // eax
    unsigned int v0;  // [bp-0xc]

    len = lstrlen(v2);
    if (len && *((char *)(len + v2 - 1)) == 115)
        *((char *)(len + v2 - 1)) = 0;
    i = &g_100ec0b6.field_0;
    v5 = 0;
    for (v6 = 0; v5 < 0x100; i += 1)
    {
        if (!i->field_0)
            return 0;
        v0 = v5;
        v6 = lstrcmpi(i, v2);
        if (!v6)
            return i->field_24;
        v5 += 1;
    }
    return v6;
}
```

## `sub_10030027` `0x10030027`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10030027(void)
{
}
```

## `sub_1003004d` `0x1003004d`

_129 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

int sub_1003004d(void)
{
    unsigned int v2[17];  // ebx
    unsigned int j;  // edx
    unsigned int v4[17];  // esi
    unsigned int v5;  // eax
    unsigned int v6;  // ebx
    struct_0 *v7;  // ebx
    unsigned int iter;  // [bp-0x8]

    iter = 0;
    while (iter < 16)
    {
        v2 = iter * 492 + 6606096;
        if (v2[0])
        {
            j = 0;
            for (v4 = &v2[15]; j < v2[14]; j += 1)
            {
                v4 = &v4[3];
            }
            iter += 1;
        }
        else
        {
            iter += 1;
        }
    }
    if (v6)
        return;
    iter = 1;
    while (iter <= 10)
    {
        v7 = iter * 12 + 6605976;
        if (v7->padding_0 == v5)
            iter += 1;
        else
            iter += 1;
    }
    return;
}
```

## `sub_100300ce` `0x100300ce`

_337 bytes. (leaf/helper — see body)_

```c
unsigned int sub_100300ce(void)
{
    char iter[2];  // edi
    void* v5;  // ebx
    char v14[2];  // edi
    char v15;  // cl
    char v16[2];  // edi
    char i;  // cl
    void* iter1;  // ebx
    char v8;  // cl
    char v9;  // cl
    char v10[2];  // edi
    void* node;  // ebx
    char v12;  // cl
    char v13[2];  // edi
    unsigned int v0;  // [bp-0x7dc]
    unsigned int v1;  // [bp-0x7d8]
    char v2;  // [bp-0x7d4]

    iter = &v2;
    for (i = *((char *)v5); i == 32; i = *((char *)iter1))
    {
        iter1 += 1;
    }
    v8 = i;
    if (!i)
        return 0;
    if (v8 != 36 && v8 != 91)
    {
        if (v8 != 39 && v8 != 0x22)
        {
            while (true)
            {
                v9 = v8;
                if (!v8)
                    break;
                if (v9 == 32)
                {
                    for (; *((char *)iter1) == 32; iter1 += 1);
                    *((char *)&iter1[1]) = 0;
                    break;
                }
                else
                {
                    if (v9 == 46 && *((short *)iter1) == 0x2e2e)
                    {
                        iter[0] = 0;
                        v10 = &iter[1];
                        node = iter1 + 2;
                        v12 = *((char *)node);
                        v13 = v10;
                        while (true)
                        {
                            v14 = v13;
                            v15 = v12;
                            if (!v12)
                                break;
                            if (v15 == 32)
                            {
                                for (; *((char *)node) == 32; node += 1);
                                *((char *)&node[1]) = 0;
                                break;
                            }
                            else
                            {
                                v14[0] = v15;
                                node += 1;
                                v16 = &v14[1];
                                v12 = *((char *)node);
                                v13 = v16;
                            }
                        }
                        v14[0] = 0;
                        v1 = sub_10040900(v10);
                        v0 = sub_10040900(&v2);
                        return (v1 < v0 ? sub_10040a30(v0 - v1 + 1) + v1 : sub_10040a30(v1 - v0 + 1) + v0);
                    }
                    iter[0] = v9;
                    iter1 += 1;
                    iter = &iter[1];
                    v8 = *((char *)iter1);
                }
            }
            iter[0] = 0;
            return sub_10040900(&v2);
        }
        sub_10030225();
        return sub_10040900(&v2);
    }
    sub_1002c228();
    return sub_10040900(&v2);
}
```

## `sub_100300f3` `0x100300f3`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100300f3(void)
{
}
```

## `sub_10030121` `0x10030121`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10030121(void)
{
}
```

## `sub_10030164` `0x10030164`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10030164(void)
{
}
```

## `sub_10030225` `0x10030225`

_244 bytes. (leaf/helper — see body)_

```c
void sub_10030225(void)
{
    char *v3;  // edi
    char *v4;  // ebx
    char *iter;  // edi
    char *node;  // ebx
    char v7;  // cl
    char *v9;  // edi
    char v0;  // [bp-0x9]
    unsigned int v1;  // [bp-0x8]

    *(v3) = 0;
    if (!*(v4))
    {
        return;
    }
    else if (*(v4) == 36)
    {
        sub_1002c228();
        return;
    }
    else if (*(v4) == 91)
    {
        sub_1002c228();
        return;
    }
    else
    {
        v1 = 0;
        v0 = 0;
        iter = v3;
        while (true)
        {
            v7 = *(node);
            if (!*(node))
                break;
            if (v7 == 39 || v7 == 0x22)
            {
                if (v0 == v7)
                    break;
                if (!v0)
                {
                    v0 = v7;
                }
                else
                {
                    *(iter) = v7;
                    iter += 1;
                }
                node += 1;
            }
            else if (v7 == 36)
            {
                v1 = 1;
                if (node[1] == 36)
                {
                    *(iter) = 36;
                    node += 2;
                }
                else
                {
                    sub_10030225();
                    for (; *(iter); iter += 1);
                    if (!v0)
                        break;
                }
            }
            else if (v7 == 91)
            {
                v1 = 1;
                if (node[1] == 91)
                {
                    *(iter) = 91;
                    node += 2;
                }
                else
                {
                    sub_10030225();
                    for (; *(iter); iter += 1);
                }
            }
            else if (v7 == 32 && !v1)
            {
                node += 1;
            }
            else
            {
                v1 = 1;
                *(iter) = v7;
                node += 1;
                iter += 1;
            }
        }
        v9 = iter;
        if (!v1)
            v9 = v3;
        *(v9) = 0;
        return;
    }
}
```

## `sub_10030236` `0x10030236`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10030236(void)
{
}
```

## `sub_10030285` `0x10030285`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10030285(void)
{
}
```

## `sub_100302bc` `0x100302bc`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100302bc(void)
{
}
```

## `sub_100302eb` `0x100302eb`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100302eb(void)
{
}
```

## `sub_100302fe` `0x100302fe`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100302fe(void)
{
}
```

## `sub_10030326` `0x10030326`

_148 bytes. (leaf/helper — see body)_

```c
int sub_10030326(void)
{
    char *v4;  // ebx
    char *v5;  // edi
    unsigned int v14;  // eax
    char i;  // cl
    char *iter;  // ebx
    int v9;  // edi
    unsigned int v10;  // eax
    char *v11;  // edi
    char *node;  // edi
    char v13;  // cl
    char *v0;  // [bp-0x10]
    char v1;  // [bp-0x9]
    unsigned int v2;  // [bp-0x8]

    if (!*(v4))
    {
        *(v5) = 0;
        return v14;
    }
    else if (*(v4) == 36)
    {
        v0 = v4;
        for (i = *(v4); i != 32 && i; i = *(iter))
        {
            iter += 1;
        }
        *(iter) = 0;
        lstrcpy(v9, v0);
        return v10;
    }
    else
    {
        v0 = v11;
        v2 = 0;
        v1 = 0;
        while (true)
        {
            v13 = *(iter);
            if (!*(iter))
                break;
            if (v13 == 39 || v13 == 0x22)
            {
                if (v1 == v13)
                    break;
                if (!v1)
                {
                    v1 = v13;
                }
                else
                {
                    *(node) = v13;
                    node += 1;
                }
                iter += 1;
            }
            else
            {
                if (v13 != 32)
                    v2 = 1;
                *(node) = v13;
                node += 1;
                iter += 1;
            }
        }
        if (!v2)
            node = v0;
        *(node) = 0;
        return v14;
    }
}
```

## `sub_10030337` `0x10030337`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10030337(void)
{
}
```

## `sub_10030396` `0x10030396`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10030396(void)
{
}
```

## `sub_100303be` `0x100303be`

_130 bytes. (leaf/helper — see body)_

```c
extern char g_10134e6b;

unsigned int sub_100303be(int a0)
{
    char *node;  // esi
    void* iter;  // edi
    unsigned int v4;  // ecx
    char v5;  // dl
    int v6;  // eax
    int v1;  // [bp-0x88]

    if (!g_10134e6b)
        return 0;
    node = &g_10134e6b;
    while (true)
    {
        iter = &v1 - 4;
        v4 = 1;
        while (true)
        {
            v5 = *(node);
            if (*(node) == 44)
            {
                node += 1;
                break;
            }
            else if (v5 == 32 && v4)
            {
                node += 1;
            }
            else
            {
                if (!v5)
                    break;
                *((char *)iter) = v5;
                v4 = 0;
                node += 1;
                iter += 1;
            }
        }
        for (*((char *)iter) = 0; iter > &v1 - 4 && (char)iter[1] == 32; iter -= 1)
        {
            *((char *)&iter[1]) = 0;
        }
        if (iter == &v1 - 4)
            return 0;
        *((char **)&v1) = node;
        v6 = lstrcmpi(a0, &v1 - 4);
        if (!v6)
            return _INSERT(v6, 0, 1);
        node = *((unsigned int *)&v1);
        if (!*(node))
            return 0;
    }
}
```

## `sub_100303f1` `0x100303f1`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100303f1(void)
{
}
```

## `sub_10030442` `0x10030442`

_4493 bytes. refs "gotolabel", "islocation", "isdistance"_

```c
typedef struct struct_0 {
    int field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
} struct_0;

extern unsigned int g_1003445e;
extern unsigned int g_1005dbcc;
extern unsigned int g_10087a0b[4];
extern unsigned int g_1008858b[4];
extern char g_10292302;
extern struct_0 g_10292304;

void* sub_10030442(void* iter, void* a1, int a2)
{
    void* iter1;  // eax
    void* iter2;  // eax
    unsigned int v13;  // eax
    unsigned int l;  // ecx
    void* v15;  // esi
    void* v17;  // eax
    void* v18;  // eax
    char v5;  // cl
    void* idx;  // edx
    void* index;  // edx
    void* idx1;  // edx
    void* v9;  // eax
    void* v10;  // eax
    void* node;  // eax
    void* v0;  // [bp-0x10c4]
    unsigned int v1;  // [bp-0x10c0]
    void* v2;  // [bp-0x8]

    if (!g_10292302)
    {
        sub_1002c1b6("gotolabel", sub_1003068a);
        sub_1002c1b6("islocation", sub_1003070e);
        sub_1002c1b6("isdistance", sub_10030754);
        sub_1002c1b6("isnotdistance", sub_100307b9);
        sub_1002c1b6("isnotlocation", sub_1003081e);
        sub_1002c1b6("skip", sub_10030864);
        sub_1002c1b6("wait", sub_10030878);
        sub_1002c1b6("refillammo", sub_100308bf);
        sub_1002c1b6("countolditems", sub_100309b8);
        sub_1002c1b6("countitems", sub_10030a5b);
        sub_1002c1b6("sspecial", sub_10030a3e);
        sub_1002c1b6("getcount", sub_10030b5c);
        sub_1002c1b6("countitemsvisible", sub_10030b7e);
        sub_1002c1b6("uh", sub_10030b97);
        sub_1002c1b6("ihpc", sub_10030c4c);
        sub_1002c1b6("sd", sub_10030d0e);
        sub_1002c1b6("displaymap", sub_10030d50);
        sub_1002c1b6("altnavdisplay", sub_10030da0);
        sub_1002c1b6("hmm", sub_10030df0);
        sub_1002c1b6("lmm", sub_10030e32);
        sub_1002c1b6("icicle", sub_10030e74);
        sub_1002c1b6("stalagmite", sub_10030eb6);
        sub_1002c1b6("aimtype", sub_10030ef8);
        sub_1002c1b6("explo", sub_10030f3e);
        sub_1002c1b6("autoaim", sub_10030f80);
        sub_1002c1b6("follow", sub_10030fb8);
        sub_1002c1b6("attack", sub_10031025);
        sub_1002c1b6("whitebox", sub_10031098);
        sub_1002c1b6("ignoretarget", sub_100310c8);
        sub_1002c1b6("stopattack", sub_10031145);
        sub_1002c1b6("setattackmode", sub_100311a8);
        sub_1002c1b6("autoheal", sub_100312b8);
        sub_1002c1b6("equipammy", sub_10031358);
        sub_1002c1b6("fastequipammy", sub_1003139e);
        sub_1002c1b6("equipring", sub_100313db);
        sub_1002c1b6("equipsring", sub_10031457);
        sub_1002c1b6("equipboots", sub_100314b7);
        sub_1002c1b6("equiphelm", sub_1003152a);
        sub_1002c1b6("equipchest", sub_10031582);
        sub_1002c1b6("equiphead", sub_100315da);
        sub_1002c1b6("equiplegs", sub_10031632);
        sub_1002c1b6("equiprhand", sub_1003168a);
        sub_1002c1b6("equiplhand", sub_10031706);
        sub_1002c1b6("equipbelt", sub_10031782);
        sub_1002c1b6("equipback", sub_100317fe);
        sub_1002c1b6("say", sub_10031856);
        sub_1002c1b6("allowwalk", sub_100318a5);
        sub_1002c1b6("disallowwalk", sub_100318c4);
        sub_1002c1b6("setalarm", sub_100318e3);
        sub_1002c1b6("flash", sub_100319da);
        sub_1002c1b6("copyscreen", "j");
        sub_1002c1b6("savescreen", sub_100319f5);
        sub_1002c1b6("changestance", sub_10031a20);
        sub_1002c1b6("npcsay", sub_10031b41);
        sub_1002c1b6("gamesay", sub_10031b90);
        sub_1002c1b6("tradesay", sub_10031be1);
        sub_1002c1b6("rlsay", sub_10031c32);
        sub_1002c1b6("helpsay", sub_10031c83);
        sub_1002c1b6("guildsay", sub_10031cd4);
        sub_1002c1b6("sayin", sub_10031d25);
        sub_1002c1b6("navsay", sub_10031db8);
        sub_1002c1b6("setautocombo", sub_10031e05);
        sub_1002c1b6("statusmessage", sub_10031e7c);
        sub_1002c1b6("settradeoptions", sub_10031e9a);
        sub_1002c1b6("buyitems", sub_10031f6a);
        sub_1002c1b6("buyitemsupto", sub_10032023);
        sub_1002c1b6("sellitemsdownto", sub_10032102);
        sub_1002c1b6("sellitems", sub_1003219a);
        sub_1002c1b6("mana", sub_1003220e);
        sub_1002c1b6("smana", sub_10032219);
        sub_1002c1b6("gmana", sub_10032224);
        sub_1002c1b6("gsmana", sub_1003222f);
        sub_1002c1b6("health", sub_100322bb);
        sub_1002c1b6("shealth", sub_100322c6);
        sub_1002c1b6("ghealth", sub_100322d1);
        sub_1002c1b6("uhealth", sub_100322dc);
        sub_1002c1b6("gshealth", sub_100322e7);
        sub_1002c1b6("retarget", sub_10032372);
        sub_1002c1b6("pm", sub_10032403);
        sub_1002c1b6("auto", sub_10032433);
        sub_1002c1b6("end", sub_10032529);
        sub_1002c1b6("break", sub_10032559);
        sub_1002c1b6("turnoff", sub_10032579);
        sub_1002c1b6("reconnect", sub_10032595);
        sub_1002c1b6("connect", sub_1003259e);
        sub_1002c1b6("setpos", sub_1003269d);
        sub_1002c1b6("listboxsetup", sub_100326d5);
        sub_1002c1b6("listboxaddline", sub_10032766);
        sub_1002c1b6("setcolor", sub_10032803);
        sub_1002c1b6("displaytext", sub_1003284d);
        sub_1002c1b6("listas", sub_1003287c);
        sub_1002c1b6("dontlist", sub_100328af);
        sub_1002c1b6("sio", sub_100328c7);
        sub_1002c1b6("usegrounditem", sub_1003295a);
        sub_1002c1b6("opengrounditem", sub_100329a7);
        sub_1002c1b6("playsound", sub_10032a08);
        sub_1002c1b6("useitem", sub_10032a26);
        sub_1002c1b6("usegroundxyz", sub_10032a6b);
        sub_1002c1b6("opengroundxyz", sub_10032acb);
        sub_1002c1b6("reachgrounditem", sub_10032b2e);
        sub_1002c1b6("skin", sub_10032b80);
        sub_1002c1b6("stake", sub_10032bf6);
        sub_1002c1b6("moveto", sub_10032c6c);
        sub_1002c1b6("seticontext", sub_10032ccc);
        sub_1002c1b6("seticonactive", sub_10032d31);
        sub_1002c1b6("setoutfitcolor", sub_10032dad);
        sub_1002c1b6("setoutfit", sub_10032e85);
        sub_1002c1b6("setitemoutfit", sub_10032f46);
        sub_1002c1b6("setrelation", sub_10032fb1);
        sub_1002c1b6("goinvisible", sub_1003311b);
        sub_1002c1b6("moveitems", sub_10033139);
        sub_1002c1b6("movenitems", sub_100331b4);
        sub_1002c1b6("moveitemsonto", sub_100331ed);
        sub_1002c1b6("openitem", sub_100332b7);
        sub_1002c1b6("openbpitem", sub_100332e9);
        sub_1002c1b6("openbeltitem", sub_10033325);
        sub_1002c1b6("closeallwindows", sub_10033361);
        sub_1002c1b6("reopenwindows", sub_100333bb);
        sub_1002c1b6("loadcavebot", sub_1003342d);
        sub_1002c1b6("loadtargeting", sub_1003343e);
        sub_1002c1b6("loadsetting", sub_1003344f);
        sub_1002c1b6("loadscript", sub_10033460);
        sub_1002c1b6("openitemnew", sub_10033471);
        sub_1002c1b6("useitemsonground", sub_100334a6);
        sub_1002c1b6("useongroundxyz", sub_10033567);
        sub_1002c1b6("repeatuseongroundxyz", sub_10033619);
        sub_1002c1b6("useongrounditem", sub_100336d9);
        sub_1002c1b6("useoninventoryitem", sub_10033778);
        sub_1002c1b6("useoncreature", sub_100337fd);
        sub_1002c1b6("eatfood", sub_1003389f);
        sub_1002c1b6("uhpc", sub_100338a8);
        sub_1002c1b6("soulf", sub_1003396b);
        sub_1002c1b6("fish", sub_10033b23);
        sub_1002c1b6("safe", sub_10033b38);
        sub_1002c1b6("filewrite", sub_10033b53);
        sub_1002c1b6("filewriteline", sub_10033b85);
        sub_1002c1b6("log", sub_10033bb7);
        sub_1002c1b6("filedelete", sub_10033bd5);
        sub_1002c1b6("while", sub_10033bfc);
        sub_1002c1b6("loop", sub_10033c87);
        sub_1002c1b6("foreach", sub_10033d17);
        sub_1002c1b6("ifgm", sub_10034264);
        sub_1002c1b6("ifnogm", sub_1003427f);
        sub_1002c1b6("ifplayeronscreen", sub_1003429a);
        sub_1002c1b6("ifnoplayeronscreen", sub_100342b5);
        sub_1002c1b6("ifdefaultmessage", sub_100342d0);
        sub_1002c1b6("ifprivatemessage", sub_100342eb);
        sub_1002c1b6("ifplayerattacking", sub_10034306);
        sub_1002c1b6("isposz", sub_10034321);
        sub_1002c1b6("istargetname", sub_10034341);
        sub_1002c1b6("isattackedname", sub_1003439c);
        sub_1002c1b6("isattacking", sub_100343f4);
        sub_1002c1b6("isnotattacking", sub_10034410);
        sub_1002c1b6("istargeting", sub_1003442c);
        sub_1002c1b6("isnottargeting", sub_10034447);
        sub_1002c1b6("isonscreen", &g_1003445e);
        sub_1002c1b6("isnotonscreen", sub_100344ba);
        sub_1002c1b6("ifpoisoned", sub_1003451a);
        sub_1002c1b6("ifdrunk", sub_10034535);
        sub_1002c1b6("ifhasted", sub_10034550);
        sub_1002c1b6("ifparalyzed", sub_1003456b);
        sub_1002c1b6("ifnotparalyzed", sub_10034586);
        sub_1002c1b6("ifnothasted", sub_100345a1);
        sub_1002c1b6("ifmanashielded", sub_100345bc);
        sub_1002c1b6("ifnotmanashielded", sub_100345d7);
        sub_1002c1b6("haste", sub_100345f2);
        sub_1002c1b6("stronghaste", sub_10034609);
        sub_1002c1b6("charge", sub_10034620);
        sub_1002c1b6("swiftfoot", sub_10034637);
        sub_1002c1b6("manashield", sub_1003464e);
        sub_1002c1b6("ewave", sub_10034677);
        sub_1002c1b6("wave", sub_1003469d);
        sub_1002c1b6("countlower", sub_100346c1);
        sub_1002c1b6("counthigher", sub_100346e3);
        sub_1002c1b6("caplower", sub_10034705);
        sub_1002c1b6("caphigher", sub_1003472d);
        sub_1002c1b6("hplower", sub_10034755);
        sub_1002c1b6("if", sub_10034776);
        sub_1002c1b6("exec", sub_100347b0);
        sub_1002c1b6("ifnot", sub_100347dd);
        sub_1002c1b6("else", sub_10034817);
        sub_1002c1b6("hpmissinglower", sub_10034836);
        sub_1002c1b6("hpmissinghigher", sub_10034860);
        sub_1002c1b6("mpmissinglower", sub_1003488a);
        sub_1002c1b6("mpmissinghigher", sub_100348b4);
        sub_1002c1b6("hphigher", sub_100348de);
        sub_1002c1b6("exivalast", sub_10034989);
        sub_1002c1b6("exivatarget", sub_100349bb);
        sub_1002c1b6("lootitems", sub_100349ed);
        sub_1002c1b6("stackitems", sub_100349f6);
        sub_1002c1b6("pickupitems", sub_10034c89);
        sub_1002c1b6("pickupitemsamount", sub_10034ba7);
        sub_1002c1b6("collectitems", sub_10034a2c);
        sub_1002c1b6("moveitemonground", sub_10034ddf);
        sub_1002c1b6("dropitemsxyz", sub_10034e5b);
        sub_1002c1b6("dropitemsxyzamount", sub_10034e86);
        sub_1002c1b6("dropitems", sub_10034ef4);
        sub_1002c1b6("gfbsd", sub_10034f9a);
        sub_1002c1b6("aimgfb", sub_10034f9a);
        sub_1002c1b6("aimavalanche", sub_10034fb2);
        sub_1002c1b6("aimthunderstorm", sub_10034fca);
        sub_1002c1b6("aimstoneshower", sub_10034fe2);
        sub_1002c1b6("logout", sub_10034ffa);
        sub_1002c1b6("crosshair", sub_10035023);
        sub_1002c1b6("xlog", sub_10035078);
        sub_1002c1b6("throwpot", sub_10035090);
        sub_1002c1b6("pickuppot", sub_100350bb);
        sub_1002c1b6("surroundpot", sub_100350c4);
        sub_1002c1b6("magwall", sub_100350cd);
        sub_1002c1b6("mwallcover", sub_1003510c);
        sub_1002c1b6("mwallshield", sub_10035141);
        sub_1002c1b6("mplower", sub_10035167);
        sub_1002c1b6("mphigher", sub_10035188);
        sub_1002c1b6("exorihur", sub_100351a9);
        sub_1002c1b6("exoricon", sub_10035238);
        sub_1002c1b6("exorigran", sub_100352c7);
        sub_1002c1b6("targethplower", sub_10035365);
        sub_1002c1b6("spydown", sub_100353a6);
        sub_1002c1b6("spyup", sub_100353f6);
        sub_1002c1b6("refillmana", sub_10035446);
        sub_1002c1b6("refilldepletedmana", sub_10035446);
        sub_1002c1b6("refillhealth", sub_100354ab);
        sub_1002c1b6("healparalysis", sub_1003550e);
        sub_1002c1b6("paralyze", sub_10035549);
        sub_1002c1b6("keepmagwall", sub_1003559c);
        sub_1002c1b6("dashchase", sub_100355ec);
        sub_1002c1b6("dash", sub_10035619);
        sub_1002c1b6("race", sub_10035619);
        sub_1002c1b6("moven", sub_10035655);
        sub_1002c1b6("movee", sub_1003565b);
        sub_1002c1b6("moves", sub_10035661);
        sub_1002c1b6("movew", sub_10035667);
        sub_1002c1b6("movene", sub_1003566d);
        sub_1002c1b6("movese", sub_10035673);
        sub_1002c1b6("movesw", sub_10035679);
        sub_1002c1b6("movenw", sub_1003567f);
        sub_1002c1b6("turnn", sub_10035685);
        sub_1002c1b6("turne", sub_1003568b);
        sub_1002c1b6("turns", sub_10035691);
        sub_1002c1b6("turnw", sub_10035697);
        sub_1002c1b6("scrollview", sub_100356b2);
        sub_1002c1b6("settargeting", sub_10035786);
        sub_1002c1b6("runtargeting", sub_10035807);
        sub_1002c1b6("setcavebot", sub_10035812);
        sub_1002c1b6("setfollowwaypoints", sub_10035812);
        sub_1002c1b6("setopennextbp", sub_1003587e);
        sub_1002c1b6("set", sub_100358e9);
        sub_1002c1b6("clear", sub_100359d8);
        sub_1002c1b6("inc", sub_10035a44);
        sub_1002c1b6("dec", sub_10035aca);
        sub_1002c1b6("swapequip", sub_10035b3b);
        sub_1002c1b6("unequip", sub_10035b75);
        sub_1002c1b6("setcaption", sub_10035c15);
        sub_1002c1b6("makerune", sub_10035c27);
        sub_1002c1b6("addloot", sub_10032c9e);
        sub_1002c1b6("setammy", sub_10032cb9);
        sub_1002c1b6("setdebug", sub_1003308d);
        sub_1002c1b6("getproperties", sub_1003309e);
        sub_1002c1b6("gettile", sub_100330d2);
        sub_1002c1b6("annisd", sub_10033a86);
        sub_1002c1b6("ringattacking", sub_100348ff);
        g_10292302 = 1;
    }
    for (; *((char *)iter) == 32; iter += 1);
    if (!*((char *)iter))
        return iter;
    if (a1 != 0xffffffff)
        g_1005dbcc = iter;
    for (iter = iter; *((char *)iter); iter += 1);
    for (iter1 = iter - 1; *((char *)iter1) == 32 && iter1 >= iter; iter1 -= 1)
    {
        *((char *)iter1) = 0;
    }
    if (*((char *)iter) == 123)
    {
        iter2 = iter + 1;
        v1 = 1;
        iter = iter2;
        while (true)
        {
            while (true)
            {
                while (true)
                {
                    while (true)
                    {
                        v5 = *((char *)iter2);
                        if (*((char *)iter2) != 123)
                            break;
                        v1 += 1;
                        iter2 += 1;
                    }
                    if (v5 != 125)
                        break;
                    v1 -= 1;
                    if (v1)
                    {
                        *((char *)&iter2[1]) = 0;
                        v0 = iter2 + 2;
                        sub_10030442(iter, a1, a2);
                        iter2 += 2;
                        idx = a1;
                        if (*((int *)(0x4 * idx + (char *)&g_10087a0b[0])) == 0xffffffff)
                        {
                            return iter2;
                        }
                        else if (*((int *)(0x4 * idx + (char *)&g_10087a0b[0])))
                        {
                            if (*((int *)(0x4 * idx + (char *)&g_1008858b[0])))
                                return iter2;
                            *((void* *)(0x4 * idx + (char *)&g_1008858b[0])) = iter2;
                            return iter2;
                        }
                    }
                    else
                    {
                        *((char *)iter2) = 0;
                        v0 = iter2 + 1;
                        sub_10030442(iter, a1, a2);
                        idx1 = a1;
                        if (*((int *)(0x4 * idx1 + (char *)&g_10087a0b[0])) == 0xffffffff)
                        {
                            return iter2 + 1;
                        }
                        else if (*((int *)(0x4 * idx1 + (char *)&g_10087a0b[0])))
                        {
                            if (*((int *)(0x4 * idx1 + (char *)&g_1008858b[0])))
                                return iter2 + 1;
                            *((void* *)(0x4 * idx1 + (char *)&g_1008858b[0])) = iter2 + 1;
                            return iter2 + 1;
                        }
                        else
                        {
                            return iter2 + 1;
                        }
                    }
                }
                if (v1 != 1 || v5 != 124 || (char)iter2[1] == 124 || (char)iter2[1] == 124)
                    break;
                *((char *)iter2) = 0;
                v0 = iter2 + 1;
                sub_10030442(iter, a1, a2);
                iter2 += 1;
                index = a1;
                if (*((int *)(0x4 * index + (char *)&g_10087a0b[0])) == 0xffffffff)
                    return iter2;
                if (*((int *)(0x4 * index + (char *)&g_10087a0b[0])))
                {
                    if (*((int *)(0x4 * index + (char *)&g_1008858b[0])))
                        return iter2;
                    *((void* *)(0x4 * index + (char *)&g_1008858b[0])) = iter2;
                    return iter2;
                }
                iter = iter2;
            }
            if (!v5)
                break;
            iter2 += 1;
        }
        sub_10030442(iter, a1, a2);
    }
    v9 = iter;
    while (true)
    {
        v10 = v9;
        if (*((char *)v10) == 32 || !*((char *)v10))
            break;
        v9 = v10 + 1;
    }
    if (*((char *)v10))
    {
        *((char *)v10) = 0;
        if ((char)v10[1])
        {
            for (node = v10 + 1; *((char *)node) == 32; node += 1);
            for (v2 = node; *((char *)node); node += 1);
            for (*((char *)node) = 0; *((char *)node) == 32; node -= 1);
            *((char *)node) = 0;
        }
        else
        {
            v2 = v10;
        }
    }
    else
    {
        v2 = v10;
    }
    v0 = iter;
    sub_1002ff87();
    v13 = 0;
    l = 0;
    v15 = iter;
    do
    {
        l = _INSERT(l, 0, *((char *)v15));
        v13 = v13 * 5 + l;
        v15 += 1;
    } while (l);
    v17 = v13 & 0x3fff;
    if (!*((int *)((char *)&g_10292304.field_0 + 0x8 * v17)))
        return v17;
    v18 = lstrcmp(*((int *)((char *)&g_10292304.field_0 + 0x8 * v17)), iter);
    if (v18)
        return v18;
    goto *((int *)(4 + (char *)&g_10292304.field_0 + 0x8 * v17));
}
```

## `sub_100304be` `0x100304be`

_5 bytes. (leaf/helper — see body)_

```c
void sub_100304be(void)
{
}
```

## `sub_10030503` `0x10030503`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10030503(void)
{
}
```

## `sub_10030526` `0x10030526`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10030526(void)
{
}
```

## `sub_10030550` `0x10030550`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10030550(void)
{
}
```

## `sub_10030575` `0x10030575`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10030575(void)
{
}
```

## `sub_100305b9` `0x100305b9`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100305b9(void)
{
}
```

## `sub_100305e2` `0x100305e2`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100305e2(void)
{
}
```

## cmd_gotolabel `0x1003068a`

Named — see [doc 11](../../11-*.md). _132 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f0df8;
extern unsigned int g_100f0e00;
extern unsigned int g_100f0e04;
extern unsigned int g_100f0e30;
extern char g_100f0e45;
extern char g_100f45c5;
extern int g_101e6ea8;
extern char g_10202f06;

int sub_1003068a(void)
{
    unsigned int v3;  // eax
    unsigned int v4;  // ecx
    int v5;  // ebx
    unsigned int v0;  // [bp-0x4]
    unsigned int v2;  // [bp+0x100010]

    v3 = (unsigned int)sub_10030225();
    v4 = 0;
    v5 = &g_101e6ea8;
    while (true)
    {
        if (v4 >= *((int *)&g_10202f06))
            return v3;
        v0 = v4;
        v3 = lstrcmpi(/* unsupported instruction */ - 2032, v5 + 12);
        if (!v3)
            break;
        v5 += 48;
        v4 += 1;
    }
    g_100f0e00 = v4;
    g_100f0e45 = 1;
    g_100f0df8 = 0;
    if (v2 == 4294967295)
        g_100f0e30 = 1;
    else
        g_100f0e04 = GetTickCount();
    return sub_1002ae81(&g_100f45c5, 0x400);
}
```

## cmd_islocation `0x1003070e`

Named — see [doc 11](../../11-*.md). _70 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f854;
extern char g_1005f858;
extern char g_1005f85c;
extern unsigned int g_100f0e00;
extern unsigned int g_101e6ea8[4];

unsigned int sub_1003070e(void)
{
    unsigned int v4[3];  // ebx
    unsigned int v5;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    if (v2 == 0xffffffff)
    {
        v4 = &g_101e6ea8[12 * g_100f0e00];
        v5 = g_1005f854;
        if (g_1005f854 == v4[0] && *((int *)&g_1005f858) == v4[1] && *((int *)&g_1005f85c) == v4[2])
            v5 = sub_10030442(v1, v2, v3);
    }
    return v5;
}
```

## cmd_isdistance `0x10030754`

Named — see [doc 11](../../11-*.md). _101 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern char g_1005f85c;
extern unsigned int g_100f0e00;
extern unsigned int g_101e6ea8[4];

void* sub_10030754(void)
{
    void* v6;  // ebx
    unsigned int v7[3];  // ebx
    int v8;  // eax
    int v9;  // eax
    void* v10;  // eax
    void* v1;  // [bp+0xffff8]
    unsigned int v2;  // [bp+0xffffc]
    void* v3;  // [bp+0x100000]
    void* v4;  // [bp+0x100010]
    int v5;  // [bp+0x100014]

    if (v4 != 0xffffffff)
        return v10;
    v6 = v3;
    v2 = sub_100300ce();
    v1 = v6;
    v7 = &g_101e6ea8[12 * g_100f0e00];
    v8 = g_1005f858 - v7[1];
    v9 = g_1005f854 - v7[0];
    if ((v9 ^ v9 >> 31) - (v9 >> 31) > v2)
    {
        return (v9 ^ v9 >> 31) - (v9 >> 31);
    }
    else if ((v8 ^ v8 >> 31) - (v8 >> 31) > v2)
    {
        return (v9 ^ v9 >> 31) - (v9 >> 31);
    }
    else if (*((int *)&g_1005f85c) == v7[2])
    {
        return sub_10030442(v1, v4, v5);
    }
    else
    {
        return (v9 ^ v9 >> 31) - (v9 >> 31);
    }
}
```

## cmd_isnotdistance `0x100307b9`

Named — see [doc 11](../../11-*.md). _101 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern char g_1005f85c;
extern unsigned int g_100f0e00;
extern unsigned int g_101e6ea8[4];

void* sub_100307b9(void)
{
    void* v6;  // ebx
    unsigned int v7[3];  // ebx
    int v8;  // eax
    int v9;  // eax
    void* v10;  // eax
    void* v1;  // [bp+0xffff8]
    unsigned int v2;  // [bp+0xffffc]
    void* v3;  // [bp+0x100000]
    void* v4;  // [bp+0x100010]
    int v5;  // [bp+0x100014]

    if (v4 != 0xffffffff)
        return v10;
    v6 = v3;
    v2 = sub_100300ce();
    v1 = v6;
    v7 = &g_101e6ea8[12 * g_100f0e00];
    v8 = g_1005f858 - v7[1];
    v9 = g_1005f854 - v7[0];
    if ((v9 ^ v9 >> 31) - (v9 >> 31) > v2 || (v8 ^ v8 >> 31) - (v8 >> 31) > v2 || *((int *)&g_1005f85c) != v7[2])
        return sub_10030442(v1, v4, v5);
    return (v9 ^ v9 >> 31) - (v9 >> 31);
    return sub_10030442(v1, v4, v5);
}
```

## cmd_isnotlocation `0x1003081e`

Named — see [doc 11](../../11-*.md). _70 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f854;
extern char g_1005f858;
extern char g_1005f85c;
extern unsigned int g_100f0e00;
extern unsigned int g_101e6ea8[4];

void* sub_1003081e(void)
{
    unsigned int v4[3];  // ebx
    void* v5;  // eax
    void* v1;  // [bp+0x100000]
    void* v2;  // [bp+0x100010]
    int v3;  // [bp+0x100014]

    if (v2 != 0xffffffff)
        return v5;
    v4 = &g_101e6ea8[12 * g_100f0e00];
    if (g_1005f854 != v4[0] || *((int *)&g_1005f858) != v4[1] || *((int *)&g_1005f85c) != v4[2])
        return sub_10030442(v1, v2, v3);
    return g_1005f854;
    return sub_10030442(v1, v2, v3);
}
```

## cmd_skip `0x10030864`

Named — see [doc 11](../../11-*.md). _20 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f0e30;

void sub_10030864(void)
{
    unsigned int v1;  // [bp+0x100010]

    if (v1 == 4294967295)
        g_100f0e30 = 1;
    return;
}
```

## cmd_wait `0x10030878`

Named — see [doc 11](../../11-*.md). _71 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_10087a0b;
extern unsigned int g_100f0e18;
extern char g_100f0e42;

unsigned int sub_10030878(void)
{
    unsigned int v2;  // eax
    unsigned int i;  // ebx
    unsigned int idx;  // [bp+0x100010]

    v2 = sub_100300ce();
    if (idx != 4294967295)
    {
        (&g_10087a0b)[idx] = v2;
        return v2;
    }
    for (i = 0; i < v2; i += 100)
    {
        if (!g_100f0e42)
            return v2;
        Sleep(100);
        g_100f0e18 = 0;
    }
    return v2;
}
```

## cmd_refillammo `0x100308bf`

Named — see [doc 11](../../11-*.md). _249 bytes. (leaf/helper — see body)_

```c
extern unsigned short g_100433bd;
extern char g_100433c2;
extern char g_100433c4;
extern unsigned short g_100433c5;
extern char g_100433c7;
extern char g_100433ca;
extern char g_100433cd;
extern void g_100f0e48;
extern void g_100f0e4c;
extern void g_100f0e50;

int sub_100308bf(void)
{
    unsigned int v2;  // eax
    unsigned int v3;  // eax
    char v4;  // dl
    unsigned int v5;  // ecx
    unsigned int v6;  // ecx
    unsigned int v0;  // [bp-0x8]

    if (!*((int *)&g_100f0e48) || (v2 = sub_1003c52a(*((int *)&g_100f0e48)), !v2 || *((int *)0x64cccc) >= 100 || (g_100433c5 = (unsigned short)*((int *)&g_100f0e48), g_100433ca = 5, v2 = sub_1002ae92(*((int *)&g_100f0e48), 0, NULL), !v2)))
    {
        if (!*((int *)&g_100f0e4c) || (v2 = sub_1003c52a(*((int *)&g_100f0e4c)), !v2 || *((int *)0x64ccd8) >= 100 || (g_100433c5 = (unsigned short)*((int *)&g_100f0e4c), g_100433ca = 6, v2 = sub_1002ae92(*((int *)&g_100f0e4c), 0, NULL), !v2)))
        {
            if (!*((int *)&g_100f0e50))
                return v2;
            v3 = sub_1003c52a(*((int *)&g_100f0e50));
            if (!v3)
            {
                return v3;
            }
            else if (*((int *)0x64cd08) < 100)
            {
                g_100433c5 = *((int *)&g_100f0e50);
                g_100433ca = 10;
                v2 = sub_1002ae92(*((int *)&g_100f0e50), 0, NULL);
                if (!v2)
                    return v2;
            }
            else
            {
                return v3;
            }
        }
    }
    g_100433c4 = v4;
    g_100433c7 = v4;
    g_100433c2 = v2;
    v6 = v5;
    if (!v5)
        v6 += 1;
    g_100433cd = v6;
    v0 = 0x11;
    return sub_1002ade7(&g_100433bd);
}
```

## cmd_countolditems `0x100309b8`

Named — see [doc 11](../../11-*.md). _373 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
    char padding_1[31];
    unsigned int field_20;
} struct_0;

extern unsigned short g_100433d6;
extern unsigned short g_100433e9;
extern struct_0 g_100ec0b6;
extern unsigned int g_100f0e18;
extern char g_100f0e42;
extern char g_100f0e7c;

int sub_100309b8(void)
{
    int v8;  // ebx
    unsigned int len;  // eax
    unsigned int i;  // ebx
    unsigned int v19;  // eax
    unsigned int v20;  // eax
    unsigned int v21;  // ebx
    struct_0 *iter;  // ebx
    unsigned int v11;  // ecx
    unsigned int v12;  // eax
    unsigned int count;  // eax
    unsigned int v14;  // eax
    unsigned int v15;  // eax
    unsigned int v16;  // eax
    unsigned int v17;  // eax
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]
    unsigned int v2;  // [bp-0x4]
    unsigned int v5;  // [bp+0xffff8]
    unsigned int v6;  // [bp+0xffffc]
    unsigned int v7;  // [bp+0x100010]

    v6 = sub_100300ce();
    v5 = sub_100300ce();
    sub_10030225();
    v8 = /* unsupported instruction */ - 2032;
    len = lstrlen(v8);
    if (len && *((char *)(len + v8 - 1)) == 115)
        *((char *)(len + v8 - 1)) = 0;
    iter = &g_100ec0b6.field_0;
    v11 = 0;
    while (true)
    {
        if (v11 >= 0x100)
            return len;
        if (!iter->field_0)
        {
            v12 = v6;
            break;
        }
        else
        {
            v2 = v11;
            len = lstrcmpi(/* unsupported instruction */ - 2032, iter);
            if (!len)
            {
                count = GetTickCount();
                v14 = count - iter->field_20;
                if (v14 <= v5)
                    return v14;
                v12 = v6;
                break;
            }
            else
            {
                v11 += 1;
                iter = &iter[1].padding_1[3];
            }
        }
    }
    v15 = v12;
    if (!v12)
    {
        return v15;
    }
    else if (((char)sub_1003c4fa(v15, v15) & 128))
    {
        v16 = sub_1002ffa3(v15);
        if (v7 != 4294967295)
            return v16;
        Sleep(200);
        g_100f0e18 = 0;
        v1 = 19;
        v17 = sub_1002ade7(&g_100433e9);
        for (i = 0; i < 900; i += 100)
        {
            if (!g_100f0e42 || *((int *)&g_100f0e7c))
            {
                break;
            }
            else
            {
                v17 = (unsigned int)Sleep(100);
                g_100f0e18 = 0;
            }
        }
        return v17;
    }
    else
    {
        g_100433d6 = v15;
        v1 = 12;
        v19 = sub_1002ade7("\n");
        if (v7 != 4294967295)
            return v19;
        Sleep(200);
        g_100f0e18 = 0;
        v0 = 12;
        v20 = sub_1002ade7("\n");
        v21 = 0;
        while (true)
        {
            if (v21 >= 900)
                return v20;
            if (!g_100f0e42 || *((int *)&g_100f0e7c))
                break;
            v20 = (unsigned int)Sleep(100);
            g_100f0e18 = 0;
            v21 += 100;
        }
        return v20;
    }
}
```

## cmd_sspecial `0x10030a3e`

Named — see [doc 11](../../11-*.md). _29 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_10042294;

unsigned int sub_10030a3e(void)
{
    unsigned int v1;  // eax

    v1 = sub_100300ce();
    if (v1 == 137453)
        g_10042294 = 200;
    return v1;
}
```

## cmd_countitems `0x10030a5b`

Named — see [doc 11](../../11-*.md). _18 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f0e7c;

int sub_10030a5b(void)
{
    g_100f0e7c = 0;
    sub_100300ce();
}
```

## cmd_getcount `0x10030b5c`

Named — see [doc 11](../../11-*.md). _34 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f0e7c;

int sub_10030b5c(void)
{
    sub_10030225();
    g_100f0e7c = sub_1002fff4();
    return g_100f0e7c;
}
```

## cmd_countitemsvisible `0x10030b7e`

Named — see [doc 11](../../11-*.md). _25 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f0e7c;

int sub_10030b7e(void)
{
    unsigned int v1;  // eax
    unsigned int v2;  // ecx

    sub_100300ce();
    v1 = sub_1003004d();
    g_100f0e7c = v2;
    return v1;
}
```

## cmd_uh `0x10030b97`

Named — see [doc 11](../../11-*.md). _181 bytes. (leaf/helper — see body)_

```c
extern void g_100432e5;
extern char g_100432e7;
extern unsigned short g_100432e8;
extern char g_100432ea;
extern unsigned int g_100432eb;
extern unsigned int g_100f9328;
extern char g_100fa4f0;

unsigned int [35] sub_10030b97(void)
{
    unsigned int v2[35];  // eax
    unsigned int v3[35];  // eax
    char v4;  // dl
    unsigned int v0[35];  // [bp-0x10], Other Possible Types: unsigned int

    g_100f9328 = 0;
    sub_10030225();
    v2 = sub_10038eb3(/* unsupported instruction */ - 2032, 95, 0);
    if (!v2)
    {
        return v2;
    }
    else if (v2[0x22] < 95)
    {
        v0 = v2;
        v3 = sub_1002ae92(3160, 0, NULL);
        if (!v3 && !g_100fa4f0)
            return v3;
        if (!g_100fa4f0)
        {
            g_100432e5 = *((char *)&v3);
            g_100432e7 = v4;
            g_100432ea = v4;
        }
        else
        {
            *((unsigned short *)&g_100432e5) = 0;
            g_100432e7 = 0;
            g_100432ea = 0;
        }
        g_100432e8 = 3160;
        g_100432eb = v0[0];
        g_100f9328 = 1;
        v0 = 15;
        return sub_1002ade7("\r");
    }
    else
    {
        return v2;
    }
}
```

## cmd_ihpc `0x10030c4c`

Named — see [doc 11](../../11-*.md). _194 bytes. (leaf/helper — see body)_

```c
extern void g_100432e5;
extern char g_100432e7;
extern unsigned short g_100432e8;
extern char g_100432ea;
extern unsigned int g_100432eb;
extern unsigned int g_100f9328;
extern char g_100fa4f0;

unsigned int [35] sub_10030c4c(void)
{
    unsigned int v2;  // eax
    unsigned int v3[35];  // eax
    unsigned int v4[35];  // eax
    unsigned int v5[35];  // eax
    char v6;  // dl
    unsigned int v0[35];  // [bp-0x10], Other Possible Types: unsigned int

    g_100f9328 = 0;
    sub_100300ce();
    v2 = (unsigned int)sub_10030225();
    v3 = sub_10038eb3(/* unsupported instruction */ - 2032, v2, 0, v2);
    if (!v3)
        return v4;
    v4 = v3;
    if (!v4)
    {
        return v4;
    }
    else if (v4[0x22] < /* unsupported instruction */ - 2032)
    {
        v0 = v4;
        v5 = sub_1002ae92(3152, 0, NULL);
        if (!v5 && !g_100fa4f0)
            return v5;
        if (!g_100fa4f0)
        {
            g_100432e5 = *((char *)&v5);
            g_100432e7 = v6;
            g_100432ea = v6;
        }
        else
        {
            *((unsigned short *)&g_100432e5) = 0;
            g_100432e7 = 0;
            g_100432ea = 0;
        }
        g_100432e8 = 3152;
        g_100432eb = v4[0];
        g_100f9328 = 1;
        v0 = 15;
        return sub_1002ade7("\r");
    }
    else
    {
        return v4;
    }
}
```

