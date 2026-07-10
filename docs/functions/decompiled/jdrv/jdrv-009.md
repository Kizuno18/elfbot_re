# elfbot.dll decompiled — jdrv 0x1002d984..0x1002e30e

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## cmd_rand `0x1002d984`

Named — see [doc 11](../../11-*.md). _87 bytes. (leaf/helper — see body)_

```c
int sub_1002d984(void)
{
    int v4;  // eax
    int v5;  // ebx
    int v6;  // eax
    int v7;  // eax
    int v8;  // ecx
    int v9;  // eax
    int v11;  // eax
    int v12;  // eax
    unsigned int v1;  // [bp+0xfd7a4]
    unsigned int v2;  // [bp+0xfd7b0]
    unsigned short *v3;  // [bp+0xffffc]

    *(v3) = 48;
    v4 = 0;
    if (v2)
    {
        v6 = sub_100300ce(v5);
        v7 = 0;
        if (v1)
            v7 = sub_100300ce(v6);
        v8 = v6;
        v9 = v7;
        if (v9 < v8)
        {
            v8 = v7;
            v9 = v8;
        }
        v11 = v9 - v8;
        v12 = v11;
        if (v12)
        {
            v8 = v11 + 1;
            v12 = sub_10040a30(v11 + 1, v8);
        }
        v4 = v12 + v8;
    }
    sub_10040940(v4, v3);
}
```

## cmd_fileline `0x1002d9db`

Named — see [doc 11](../../11-*.md). _56 bytes. (leaf/helper — see body)_

```c
int sub_1002d9db(void)
{
    int v4;  // eax
    int v0;  // [bp-0x4]
    unsigned int v2;  // [bp+0xfd7a4]
    char *v3;  // [bp+0xffffc]

    *(v3) = 0;
    if (v2)
    {
        sub_10030225(v0);
        v4 = sub_100300ce();
        sub_10025646(v3, v4);
    }
}
```

## cmd_token `0x1002da13`

Named — see [doc 11](../../11-*.md). _203 bytes. (leaf/helper — see body)_

```c
int sub_1002da13(void)
{
    unsigned int v6;  // eax
    unsigned int v7;  // ecx
    char *iter;  // esi
    char *node;  // ebx
    char v10;  // dl
    int v0;  // [bp-0x4]
    unsigned int v2;  // [bp+0xfd7a4]
    char v3;  // [bp+0xfd7d2]
    char *v5;  // [bp+0xffffc]

    *(v5) = 0;
    if (v2)
    {
        sub_10030225(v0);
        v6 = sub_100300ce();
        if (!v6)
            v6 += 1;
        v7 = 0;
        for (iter = /* unsupported instruction */ - 4264; *(iter) == 32; iter += 1);
        node = iter;
        v3 = 0;
        while (true)
        {
            v10 = *(iter);
            if (*(iter) == 0x22 || v10 == 39)
            {
                if (!v3)
                {
                    v3 = v10;
                    node += 1;
                }
                else if (v3 == v10)
                {
                    goto LABEL_1002da97;
                }
            }
            else
            {
                if (v10 == 32 && !v3)
                {
LABEL_1002da97:
                    v7 += 1;
                    if (v7 == v6)
                    {
                        *(iter) = 0;
                        lstrcpy(v5, node);
                        break;
                    }
                    else
                    {
                        for (iter += 1; *(iter) == 32; iter += 1);
                        node = iter;
                        v3 = 0;
                        continue;
                    }
                }
                else if (!v10)
                {
                    if (v7 + 1 == v6)
                    {
                        *(iter) = 0;
                        lstrcpy(v5, node);
                    }
                    break;
                }
            }
            iter += 1;
        }
    }
}
```

## `sub_1002dabe` `0x1002dabe`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002dabe(void)
{
}
```

## cmd_filerandomline `0x1002dae0`

Named — see [doc 11](../../11-*.md). _31 bytes. (leaf/helper — see body)_

```c
int sub_1002dae0(void)
{
    int v0;  // [bp-0x4]
    char *v2;  // [bp+0xffffc]

    sub_10030225(v0);
    sub_10025646(v2, -1);
}
```

## cmd_connected `0x1002daff`

Named — see [doc 11](../../11-*.md). _35 bytes. (leaf/helper — see body)_

```c
int sub_1002daff(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940((*((int *)0x64a9c0) == 31 ? 1 : 0), v1);
}
```

## cmd_pkname `0x1002db22`

Named — see [doc 11](../../11-*.md). _18 bytes. (leaf/helper — see body)_

```c
extern int g_1005f56d;

int sub_1002db22(void)
{
    int v1;  // [bp+0xffffc]

    lstrcpy(v1, &g_1005f56d);
}
```

## cmd_ping `0x1002db34`

Named — see [doc 11](../../11-*.md). _19 bytes. (leaf/helper — see body)_

```c
extern int g_1008b71f;

void sub_1002db34(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(g_1008b71f, v1);
}
```

## cmd_fps `0x1002db47`

Named — see [doc 11](../../11-*.md). _39 bytes. (leaf/helper — see body)_

```c
int sub_1002db47(void)
{
    unsigned int v4;  // ebx
    unsigned int v0;  // [bp-0x4]
    int v2;  // [bp+0xfd7d8]
    int v3;  // [bp+0xffffc]

    v0 = v4;
    5384848();
    /* unsupported instruction */
    /* unsupported instruction */
    v2 = (/* unsupported instruction */ ? /* unsupported instruction */ : nan);
    /* unsupported instruction */
    sub_10040940(v2, v3);
}
```

## cmd_enemycount `0x1002db6e`

Named — see [doc 11](../../11-*.md). _90 bytes. (leaf/helper — see body)_

```c
extern char g_1005f85c;

void sub_1002db6e(void)
{
    unsigned int i[37];  // ecx
    unsigned int v5[37];  // ecx
    unsigned int v0[37];  // [bp-0x8]
    int v2;  // [bp+0xfd7d8]
    int v3;  // [bp+0xffffc]

    v2 = 0;
    for (i = 0x63fef8; i < 0x64a308; i = &v5[1 + 5])
    {
        v5 = i;
        if (v5[36])
        {
            v5 = i;
            if (v5[11] == *((int *)&g_1005f85c))
            {
                v0 = &i[1];
                v5 = v0;
                if (sub_1003a494(&i[1], i))
                {
                    v2 += 1;
                    v5 = v0;
                }
            }
        }
    }
    sub_10040940(v2, v3);
}
```

## cmd_friendcount `0x1002dbc8`

Named — see [doc 11](../../11-*.md). _90 bytes. (leaf/helper — see body)_

```c
extern char g_1005f85c;

void sub_1002dbc8(void)
{
    unsigned int i[37];  // ecx
    unsigned int v5[37];  // ecx
    unsigned int v0[37];  // [bp-0x8]
    int v2;  // [bp+0xfd7d8]
    int v3;  // [bp+0xffffc]

    v2 = 0;
    for (i = 0x63fef8; i < 0x64a308; i = &v5[1 + 5])
    {
        v5 = i;
        if (v5[36])
        {
            v5 = i;
            if (v5[11] == *((int *)&g_1005f85c))
            {
                v0 = &i[1];
                v5 = v0;
                if (sub_1003a320(&i[1], i))
                {
                    v2 += 1;
                    v5 = v0;
                }
            }
        }
    }
    sub_10040940(v2, v3);
}
```

## cmd_fishspots `0x1002dc22`

Named — see [doc 11](../../11-*.md). _26 bytes. (leaf/helper — see body)_

```c
int sub_1002dc22(void)
{
    int v2;  // eax
    int v1;  // [bp+0xffffc]

    v2 = sub_10037694();
    sub_10040940(v2, v1);
}
```

## cmd_caveboton `0x1002dc3c`

Named — see [doc 11](../../11-*.md). _21 bytes. (leaf/helper — see body)_

```c
extern char g_100f0e42;

int sub_1002dc3c(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(g_100f0e42, v1);
}
```

## cmd_targetingon `0x1002dc51`

Named — see [doc 11](../../11-*.md). _21 bytes. (leaf/helper — see body)_

```c
extern char g_100f0d3b;

int sub_1002dc51(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(g_100f0d3b, v1);
}
```

## cmd_autocomboon `0x1002dc66`

Named — see [doc 11](../../11-*.md). _21 bytes. (leaf/helper — see body)_

```c
extern char g_100fa4ef;

int sub_1002dc66(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(g_100fa4ef, v1);
}
```

## cmd_mshieldtime `0x1002dc7b`

Named — see [doc 11](../../11-*.md). _26 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1008b8dc;

int sub_1002dc7b(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(g_1008b8dc * 100, v1);
}
```

## cmd_hastetime `0x1002dc95`

Named — see [doc 11](../../11-*.md). _26 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1008b8ec;

int sub_1002dc95(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(g_1008b8ec * 100, v1);
}
```

## cmd_strengthtime `0x1002dcaf`

Named — see [doc 11](../../11-*.md). _26 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1008b8f0;

int sub_1002dcaf(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(g_1008b8f0 * 100, v1);
}
```

## cmd_invistime `0x1002dcc9`

Named — see [doc 11](../../11-*.md). _26 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1008b8e0;

int sub_1002dcc9(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(g_1008b8e0 * 100, v1);
}
```

## cmd_invisible `0x1002dce3`

Named — see [doc 11](../../11-*.md). _34 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[96];
    unsigned int field_60;
} struct_0;

extern struct_0 *g_1005f7ed;

void sub_1002dce3(void)
{
    unsigned short *v2;  // ecx
    unsigned short *v1;  // [bp+0xffffc]

    v2 = v1;
    *(v2) = 48;
    if (g_1005f7ed && !g_1005f7ed->field_60)
        *(v2) = 49;
}
```

## cmd_dmgs `0x1002dd05`

Named — see [doc 11](../../11-*.md). _19 bytes. (leaf/helper — see body)_

```c
extern int g_1008b8d8;

void sub_1002dd05(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(g_1008b8d8, v1);
}
```

## cmd_lastdmg `0x1002dd18`

Named — see [doc 11](../../11-*.md). _19 bytes. (leaf/helper — see body)_

```c
extern int g_1005f5f1;

void sub_1002dd18(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(g_1005f5f1, v1);
}
```

## cmd_lastdmgtype `0x1002dd2b`

Named — see [doc 11](../../11-*.md). _19 bytes. (leaf/helper — see body)_

```c
extern int g_1005f5f9;

void sub_1002dd2b(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(g_1005f5f9, v1);
}
```

## cmd_idlerecvtime `0x1002dd3e`

Named — see [doc 11](../../11-*.md). _25 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1008b72b;

int sub_1002dd3e(void)
{
    unsigned int count;  // eax
    int v1;  // [bp+0xffffc]

    count = GetTickCount();
    sub_10040940(count - g_1008b72b, v1);
}
```

## cmd_standtime `0x1002dd57`

Named — see [doc 11](../../11-*.md). _25 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f86c;

int sub_1002dd57(void)
{
    unsigned int count;  // eax
    int v1;  // [bp+0xffffc]

    count = GetTickCount();
    sub_10040940(count - g_1005f86c, v1);
}
```

## cmd_lastdmgtime `0x1002dd70`

Named — see [doc 11](../../11-*.md). _36 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f5f5;

int sub_1002dd70(void)
{
    int v2;  // eax
    unsigned int count;  // eax
    int v1;  // [bp+0xffffc]

    v2 = 0;
    if (g_1005f5f5)
    {
        count = GetTickCount();
        v2 = count - g_1005f5f5;
    }
    sub_10040940(v2, v1);
}
```

## cmd_islooting `0x1002dd94`

Named — see [doc 11](../../11-*.md). _30 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f0dcc;

int sub_1002dd94(void)
{
    int v2;  // eax
    int v1;  // [bp+0xffffc]

    v2 = 0;
    if (g_100f0dcc)
        v2 = 1;
    sub_10040940(v2, v1);
}
```

## cmd_lastdmgername `0x1002ddb2`

Named — see [doc 11](../../11-*.md). _20 bytes. (leaf/helper — see body)_

```c
extern int g_1005f5ad;

int sub_1002ddb2(void)
{
    int v1;  // [bp+0xffffc]

    lstrcpy(v1, &g_1005f5ad);
}
```

## cmd_squaretime `0x1002ddc6`

Named — see [doc 11](../../11-*.md). _19 bytes. (leaf/helper — see body)_

```c
extern int g_1008b7c3;

void sub_1002ddc6(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(g_1008b7c3, v1);
}
```

## `sub_1002ddef` `0x1002ddef`

_10 bytes. (leaf/helper — see body)_

```c
int sub_1002ddef(unsigned int a0, unsigned short *a1, PSTR a2, LPArray a3, int a4)
{
    unsigned int v0;  // [bp+0x0]

    GetTimeFormatA(v0, a0, a1, a2, a3, a4);
}
```

## `sub_1002de0f` `0x1002de0f`

_10 bytes. (leaf/helper — see body)_

```c
int sub_1002de0f(unsigned int a0, unsigned short *a1, PSTR a2, LPArray a3, int a4)
{
    unsigned int v0;  // [bp+0x0]

    GetDateFormatA(v0, a0, a1, a2, a3, a4);
}
```

## cmd_cutstr `0x1002de19`

Named — see [doc 11](../../11-*.md). _20 bytes. (leaf/helper — see body)_

```c
void sub_1002de19(void)
{
    unsigned int v1;  // [bp+0xfd7a8]
    char *v2;  // [bp+0xffffc]

    *(v2) = 0;
    if (v1)
    {
        sub_1002de28();
        return;
    }
}
```

## `sub_1002de28` `0x1002de28`

_126 bytes. (leaf/helper — see body)_

```c
void sub_1002de28(void)
{
    unsigned int v5;  // eax
    unsigned int v6;  // eax
    unsigned int v7;  // esi
    unsigned int v8;  // edi
    unsigned int i;  // ecx
    int v0;  // [bp-0x4]
    unsigned int v2;  // [bp+0xfd7a0]
    unsigned int v3;  // [bp+0xfd7d8]
    unsigned int v4;  // [bp+0xffffc]

    sub_10030225(v0);
    v5 = 0;
    if (v2)
        v5 = sub_100300ce();
    v3 = v5;
    v6 = sub_100300ce();
    if (v6)
        v6 -= 1;
    v7 = v6 + /* unsupported instruction */ - 4264;
    v8 = v4;
    for (i = 0; (i < v3 || !v3) && *((char *)(i + v7)); i += 1)
    {
        *((char *)(i + v8)) = *((char *)(i + v7));
    }
    *((char *)(i + v8)) = 0;
}
```

## cmd_creature `0x1002deab`

Named — see [doc 11](../../11-*.md). _64 bytes. (leaf/helper — see body)_

```c
int sub_1002deab(void)
{
    int v3;  // ebx
    unsigned int v4;  // eax
    unsigned int v0;  // [bp-0xc]
    unsigned int *v2;  // [bp+0xffffc]

    sub_10030225(v3);
    v4 = sub_100399af(/* unsupported instruction */ - 4264);
    *(v2) = v4;
    if (v4)
    {
        v0 = v4;
        wsprintfA(v2, "%d");
    }
}
```

## cmd_mostexposed `0x1002deeb`

Named — see [doc 11](../../11-*.md). _52 bytes. (leaf/helper — see body)_

```c
int sub_1002deeb(void)
{
    unsigned int v0;  // [bp-0x8]
    int v1;  // [bp-0x4]
    PSTR v3;  // [bp+0xffffc]

    sub_10030225(v1);
    v0 = sub_100380dd(v1);
    wsprintfA(v3, "%d");
}
```

## cmd_mostexposedcount `0x1002df1f`

Named — see [doc 11](../../11-*.md). _54 bytes. (leaf/helper — see body)_

```c
void sub_1002df1f(unsigned int a0, unsigned int a1)
{
    int v2;  // ebx
    unsigned short *v3;  // ecx
    int v4;  // edx
    unsigned short *v1;  // [bp+0xffffc]

    sub_10030225(v2);
    sub_100380dd(v2);
    v3 = v1;
    *(v3) = 48;
    if (v4)
        sub_10040940(v4, v3);
}
```

## cmd_mostshot `0x1002df55`

Named — see [doc 11](../../11-*.md). _52 bytes. (leaf/helper — see body)_

```c
int sub_1002df55(void)
{
    unsigned int v0;  // [bp-0x8]
    int v1;  // [bp-0x4]
    PSTR v3;  // [bp+0xffffc]

    sub_10030225(v1);
    v0 = sub_10037c72(v1);
    wsprintfA(v3, "%d");
}
```

## cmd_mostshotcount `0x1002df89`

Named — see [doc 11](../../11-*.md). _54 bytes. (leaf/helper — see body)_

```c
void sub_1002df89(unsigned int a0, unsigned int a1)
{
    int v2;  // ebx
    unsigned short *v3;  // ecx
    int v4;  // edx
    unsigned short *v1;  // [bp+0xffffc]

    sub_10030225(v2);
    sub_10037c72(v2);
    v3 = v1;
    *(v3) = 48;
    if (v4)
        sub_10040940(v4, v3);
}
```

## cmd_ctrl `0x1002dfbf`

Named — see [doc 11](../../11-*.md). _27 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f9359;

void sub_1002dfbf(void)
{
    unsigned short *v2;  // ecx
    unsigned short *v1;  // [bp+0xffffc]

    v2 = v1;
    *(v2) = 48;
    if (g_100f9359)
        *(v2) = 49;
}
```

## cmd_shift `0x1002dfda`

Named — see [doc 11](../../11-*.md). _27 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f935d;

void sub_1002dfda(void)
{
    unsigned short *v2;  // ecx
    unsigned short *v1;  // [bp+0xffffc]

    v2 = v1;
    *(v2) = 48;
    if (g_100f935d)
        *(v2) = 49;
}
```

## cmd_alt `0x1002dff5`

Named — see [doc 11](../../11-*.md). _27 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f9361;

void sub_1002dff5(void)
{
    unsigned short *v2;  // ecx
    unsigned short *v1;  // [bp+0xffffc]

    v2 = v1;
    *(v2) = 48;
    if (g_100f9361)
        *(v2) = 49;
}
```

## cmd_key `0x1002e010`

Named — see [doc 11](../../11-*.md). _43 bytes. calls GetAsyncKeyState_

```c
char sub_1002e010(void)
{
    unsigned int v3;  // eax
    unsigned short *v4;  // ecx
    int v0;  // [bp-0x4]
    unsigned short *v2;  // [bp+0xffffc]

    v3 = _INSERT(GetAsyncKeyState(sub_100300ce(v0)) CONCAT 0, 0, 0);
    v4 = v2;
    *(v4) = 48;
    if (v3)
        *(v4) = 49;
}
```

## cmd_skill `0x1002e03b`

Named — see [doc 11](../../11-*.md). _66 bytes. (leaf/helper — see body)_

```c
int sub_1002e03b(void)
{
    unsigned int *v5;  // ebx
    unsigned int v0;  // [bp-0x8]
    int v1;  // [bp-0x4]
    unsigned int *v3;  // [bp+0xfd7ac]
    unsigned short *v4;  // [bp+0xffffc]

    v5 = v3;
    sub_10030225(v1);
    sub_1002c0cb(/* unsupported instruction */ - 4264);
    *(v4) = 48;
    if (v5)
    {
        v0 = *(v5);
        wsprintfA(v4, "%d");
    }
}
```

## cmd_skillpc `0x1002e07d`

Named — see [doc 11](../../11-*.md). _80 bytes. (leaf/helper — see body)_

```c
int sub_1002e07d(void)
{
    void* v5;  // ebx
    void* v6;  // ebx
    void* v7;  // esi
    unsigned int v0;  // [bp-0x8]
    int v1;  // [bp-0x4]
    void* v3;  // [bp+0xfd7ac]
    unsigned short *v4;  // [bp+0xffffc]

    v5 = v3;
    sub_10030225(v1);
    sub_1002c0cb(/* unsupported instruction */ - 4264);
    *(v4) = 48;
    v6 = v5;
    if (v5)
    {
        v7 = v6 - 28;
        if (v6 == 0x63fe84)
            v7 = 0x63fe7c;
        v0 = *((int *)v7);
        wsprintfA(v4, "%d");
    }
}
```

## cmd_skilltime `0x1002e0cd`

Named — see [doc 11](../../11-*.md). _168 bytes. (leaf/helper — see body)_

```c
extern char g_1005f801;
extern char g_1005f809;
extern unsigned int g_1005f811[4];
extern unsigned int g_1005f831[4];

int sub_1002e0cd(void)
{
    void* v6;  // ebx
    unsigned int idx;  // eax
    unsigned int v16;  // ecx
    unsigned int v17;  // edx
    void* v8;  // ebx
    unsigned int v9;  // edi
    unsigned int v10;  // ebx
    unsigned int v11;  // edi
    unsigned int v12[4];  // esi
    unsigned int v13;  // esi
    unsigned int v14;  // edi
    unsigned int count;  // eax
    unsigned int v0;  // [bp-0x8]
    int v1;  // [bp-0x4]
    void* v3;  // [bp+0xfd7ac]
    unsigned int v4[4];  // [bp+0xfd7d8]
    unsigned short *v5;  // [bp+0xffffc]

    v6 = v3;
    sub_10030225(v1);
    idx = sub_1002c0cb(/* unsupported instruction */ - 4264);
    *(v5) = 63;
    v8 = v6;
    if (v6 && (&g_1005f809)[idx] == 2)
    {
        v9 = (int)v8[28];
        if (v8 == 0x63fe84)
            v9 = *((int *)0x63fe7c);
        v10 = v9;
        v11 = v9 - (&g_1005f801)[idx];
        v12 = g_1005f831[idx];
        v4[0] = v12;
        v13 = (char *)v12 - g_1005f811[idx];
        v14 = v11;
        if (v14)
        {
            v0 = (100 - v9) * ((char *)v12 - g_1005f811[idx]) / v11;
            count = GetTickCount();
            v16 = count - (char *)v4;
            v0 = ((100 - v10) * v13 / v14 <= v16 ? 0 : (unsigned int)((v17 CONCAT (100 - v10) * v13 / v14 - v16) / 1000));
            wsprintfA(v5, "%d");
        }
    }
}
```

## cmd_lastmsg `0x1002e175`

Named — see [doc 11](../../11-*.md). _11 bytes. (leaf/helper — see body)_

```c
int sub_1002e175(void)
{
    unsigned int v2;  // ebx
    unsigned int v0;  // [bp-0x4]

    v0 = v2;
}
```

## cmd_lastnavmsg `0x1002e180`

Named — see [doc 11](../../11-*.md). _11 bytes. (leaf/helper — see body)_

```c
int sub_1002e180(void)
{
    unsigned int v2;  // ebx
    unsigned int v0;  // [bp-0x4]

    v0 = v2;
}
```

## cmd_curmsg `0x1002e18b`

Named — see [doc 11](../../11-*.md). _114 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_10084c07;
extern unsigned int g_1008910b[4];
extern unsigned int g_10089c8b[4];
extern char g_100f0e10;
extern unsigned int g_100f49e5;
extern unsigned int g_100f49ed;

int sub_1002e18b(void)
{
    unsigned int v5;  // ebx
    unsigned int ch;  // eax
    unsigned int v7;  // eax
    unsigned int v8;  // edx
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp-0x4]
    char *v3;  // [bp+0xfd7ac]
    PSTR v4;  // [bp+0xffffc]

    v1 = v5;
    ch = GetCurrentThreadId();
    if (ch == *((int *)&g_100f0e10))
    {
        v7 = g_100f49e5;
    }
    else
    {
        v8 = g_10084c07 * 4;
        v7 = (*((int *)(v8 + (char *)&g_1008910b[0])) == *((int *)(v8 + (char *)&g_10089c8b[0])) ? 0 : *((int *)(v8 + (char *)&g_1008910b[0])) * 316 + g_100f49ed);
    }
    if (!*(v3))
    {
        v0 = v7;
        wsprintfA(v4, "%d");
    }
}
```

## cmd_target `0x1002e1fd`

Named — see [doc 11](../../11-*.md). _41 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[144];
    unsigned int field_90;
} struct_0;

extern int g_1008b89b;

int sub_1002e1fd(void)
{
    unsigned int v2;  // ebx
    struct_0 *v3;  // eax
    unsigned int v0;  // [bp-0x4]

    v0 = v2;
    if (g_1008b89b)
        v3 = sub_1003997e(g_1008b89b);
}
```

## cmd_lastdmger `0x1002e226`

Named — see [doc 11](../../11-*.md). _36 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[144];
    unsigned int field_90;
} struct_0;

extern int g_1005f5ed;

int sub_1002e226(void)
{
    unsigned int v2;  // ebx
    struct_0 *v3;  // eax
    unsigned int v0;  // [bp-0x4]

    v0 = v2;
    if (g_1005f5ed)
        v3 = sub_1003997e(g_1005f5ed);
}
```

## cmd_self `0x1002e24a`

Named — see [doc 11](../../11-*.md). _11 bytes. (leaf/helper — see body)_

```c
int sub_1002e24a(void)
{
    unsigned int v2;  // ebx
    unsigned int v0;  // [bp-0x4]

    v0 = v2;
}
```

## cmd_followed `0x1002e255`

Named — see [doc 11](../../11-*.md). _39 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[144];
    unsigned int field_90;
} struct_0;

int sub_1002e255(void)
{
    unsigned int v2;  // ebx
    struct_0 *v3;  // eax
    unsigned int v0;  // [bp-0x4]

    v0 = v2;
    if (*((int *)0x63fe60))
        v3 = sub_1003997e(*(0x63fe60));
}
```

## cmd_attacked `0x1002e27c`

Named — see [doc 11](../../11-*.md). _38 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[144];
    unsigned int field_90;
} struct_0;

int sub_1002e27c(void)
{
    unsigned int v2;  // ebx
    struct_0 *v3;  // eax
    unsigned int v0;  // [bp-0x4]

    v0 = v2;
    if (*((int *)0x63fe64))
        v3 = sub_1003997e(*(0x63fe64));
}
```

## cmd_pk `0x1002e2a2`

Named — see [doc 11](../../11-*.md). _18 bytes. (leaf/helper — see body)_

```c
extern int g_1005f56d;

void sub_1002e2a2(void)
{
    int v1;  // ebx

    sub_100399af(&g_1005f56d, v1);
}
```

## cmd_pattacker `0x1002e2b4`

Named — see [doc 11](../../11-*.md). _17 bytes. (leaf/helper — see body)_

```c
extern int g_1005f601;

void sub_1002e2b4(void)
{
    int v1;  // ebx

    sub_1003997e(g_1005f601, v1);
}
```

## cmd_mattacker `0x1002e2c5`

Named — see [doc 11](../../11-*.md). _17 bytes. (leaf/helper — see body)_

```c
extern int g_1005f5fd;

void sub_1002e2c5(void)
{
    int v1;  // ebx

    sub_1003997e(g_1005f5fd, v1);
}
```

## cmd_attacker `0x1002e2d6`

Named — see [doc 11](../../11-*.md). _17 bytes. (leaf/helper — see body)_

```c
extern int g_1005f605;

void sub_1002e2d6(void)
{
    int v1;  // ebx

    sub_1003997e(g_1005f605, v1);
}
```

## `sub_1002e2ea` `0x1002e2ea`

_15 bytes. (leaf/helper — see body)_

```c
void sub_1002e2ea(void)
{
    int v1;  // [bp+0x100000]

    sub_10038eb3(v1, 0);
}
```

## `sub_1002e2fc` `0x1002e2fc`

_15 bytes. (leaf/helper — see body)_

```c
void sub_1002e2fc(void)
{
    int v1;  // [bp+0x100000]

    sub_10038eb3(v1, 0);
}
```

## `sub_1002e30e` `0x1002e30e`

_15 bytes. (leaf/helper — see body)_

```c
void sub_1002e30e(void)
{
    int v1;  // [bp+0x100000]

    sub_10038eb3(v1, 0);
}
```

