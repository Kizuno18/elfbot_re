# elfbot.dll decompiled — jdrv 0x1002cd09..0x1002d92b

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## cmd_screenleft `0x1002cd09`

Named — see [doc 11](../../11-*.md). _37 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    int field_14;
} struct_0;

extern struct_0 *g_10080b84;

int sub_1002cd09(void)
{
    int v2;  // eax
    int v1;  // [bp+0xffffc]

    if (g_10080b84 && *((int *)0x64a9c0) == 31)
        v2 = g_10080b84->field_14;
    sub_10040940(v2, v1);
}
```

## cmd_screenright `0x1002cd2e`

Named — see [doc 11](../../11-*.md). _40 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
    char padding_18[4];
    unsigned int field_1c;
} struct_0;

extern struct_0 *g_10080b84;

int sub_1002cd2e(void)
{
    int v2;  // eax
    int v1;  // [bp+0xffffc]

    if (g_10080b84 && *((int *)0x64a9c0) == 31)
        v2 = g_10080b84->field_14 + g_10080b84->field_1c;
    sub_10040940(v2, v1);
}
```

## cmd_screentop `0x1002cd56`

Named — see [doc 11](../../11-*.md). _37 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

extern struct_0 *g_10080b84;

int sub_1002cd56(void)
{
    int v2;  // eax
    int v1;  // [bp+0xffffc]

    if (g_10080b84 && *((int *)0x64a9c0) == 31)
        v2 = g_10080b84->field_18;
    sub_10040940(v2, v1);
}
```

## cmd_screenbottom `0x1002cd7b`

Named — see [doc 11](../../11-*.md). _40 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
    char padding_1c[4];
    unsigned int field_20;
} struct_0;

extern struct_0 *g_10080b84;

int sub_1002cd7b(void)
{
    int v2;  // eax
    int v1;  // [bp+0xffffc]

    if (g_10080b84 && *((int *)0x64a9c0) == 31)
        v2 = g_10080b84->field_18 + g_10080b84->field_20;
    sub_10040940(v2, v1);
}
```

## `sub_1002cda3` `0x1002cda3`

_27 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f7ed;

int sub_1002cda3(void)
{
    int v1;  // [bp+0xffffc]

    if (g_1005f7ed)
        lstrcpy(v1, g_1005f7ed + 4);
}
```

## cmd_time `0x1002cdbe`

Named — see [doc 11](../../11-*.md). _28 bytes. (leaf/helper — see body)_

```c
int sub_1002cdbe(void)
{
    unsigned int count;  // eax
    int v1;  // [bp+0xffffc]

    count = GetTickCount();
    sub_10040940(count / 1000, v1);
}
```

## cmd_timems `0x1002cdda`

Named — see [doc 11](../../11-*.md). _19 bytes. (leaf/helper — see body)_

```c
int sub_1002cdda(void)
{
    unsigned int count;  // eax
    int v1;  // [bp+0xffffc]

    count = GetTickCount();
    sub_10040940(count, v1);
}
```

## cmd_deltatime `0x1002cded`

Named — see [doc 11](../../11-*.md). _34 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1008b7cb;

int sub_1002cded(void)
{
    unsigned int count;  // eax
    int v1;  // [bp+0xffffc]

    count = GetTickCount();
    sub_10040940((count - g_1008b7cb) / 1000, v1);
}
```

## cmd_deltatimems `0x1002ce0f`

Named — see [doc 11](../../11-*.md). _25 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1008b7cb;

int sub_1002ce0f(void)
{
    unsigned int count;  // eax
    int v1;  // [bp+0xffffc]

    count = GetTickCount();
    sub_10040940(count - g_1008b7cb, v1);
}
```

## cmd_return `0x1002ce28`

Named — see [doc 11](../../11-*.md). _18 bytes. (leaf/helper — see body)_

```c
extern int g_100f0e80;

int sub_1002ce28(void)
{
    int v1;  // [bp+0xffffc]

    lstrcpy(v1, &g_100f0e80);
}
```

## cmd_exptnl `0x1002ce3a`

Named — see [doc 11](../../11-*.md). _36 bytes. (leaf/helper — see body)_

```c
int sub_1002ce3a(void)
{
    unsigned int v3;  // ebx
    int v4;  // eax
    unsigned int v0;  // [bp-0x4]
    int v2;  // [bp+0xffffc]

    v0 = v3;
    v4 = sub_1002bed7();
    sub_10040940(v4 - *((int *)0x63fe8c), v2);
}
```

## cmd_exph `0x1002ce5e`

Named — see [doc 11](../../11-*.md). _19 bytes. (leaf/helper — see body)_

```c
extern int g_1005e190;

void sub_1002ce5e(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(g_1005e190, v1);
}
```

## cmd_expgained `0x1002ce71`

Named — see [doc 11](../../11-*.md). _39 bytes. (leaf/helper — see body)_

```c
extern char g_1008b7c7;

int sub_1002ce71(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940((*((int *)0x63fe8c) <= *((int *)&g_1008b7c7) ? 0 : *((int *)0x63fe8c) - *((int *)&g_1008b7c7)), v1);
}
```

## cmd_timetnl `0x1002ce98`

Named — see [doc 11](../../11-*.md). _96 bytes. refs "Inf"_

```c
extern unsigned int g_1005e190;

int sub_1002ce98(void)
{
    unsigned int v3;  // ebx
    int v4;  // eax
    unsigned long long v5;  // eax
    unsigned int v6;  // edx
    unsigned int v0;  // [bp-0x4]
    unsigned short *v2;  // [bp+0xffffc]

    if (g_1005e190)
    {
        v0 = v3;
        v4 = sub_1002bed7();
        v5 = v4 - *((int *)0x63fe8c);
        v6 = v5 * 3600 >> 32;
        if (v6 >= g_1005e190)
            *(v2) = 0;
        sub_10040940((v6 CONCAT (unsigned int)(v5 * 3600)) / g_1005e190, v2);
    }
    else
    {
        lstrcpy(v2, "Inf");
    }
}
```

## cmd_exptolevel `0x1002cef8`

Named — see [doc 11](../../11-*.md). _52 bytes. (leaf/helper — see body)_

```c
int sub_1002cef8(void)
{
    int v2;  // ebx
    unsigned int v3;  // eax
    int v4;  // eax
    int v5;  // eax
    int v1;  // [bp+0xffffc]

    v3 = sub_100300ce(v2);
    if (v3 > *((int *)0x63fe88))
    {
        v4 = sub_1002bed7();
        v5 = v4 - *((int *)0x63fe8c);
    }
    else
    {
        v5 = 0;
    }
    sub_10040940(v5, v1);
}
```

## cmd_timetolevel `0x1002cf2c`

Named — see [doc 11](../../11-*.md). _112 bytes. refs "Inf"_

```c
extern unsigned int g_1005e190;

int sub_1002cf2c(void)
{
    int v2;  // ebx
    unsigned int v3;  // eax
    int v4;  // eax
    unsigned long long v5;  // eax
    unsigned int v6;  // edx
    unsigned short *v1;  // [bp+0xffffc]

    if (g_1005e190)
    {
        v3 = sub_100300ce(v2);
        if (v3 > *((int *)0x63fe88))
        {
            v4 = sub_1002bed7();
            v5 = v4 - *((int *)0x63fe8c);
        }
        else
        {
            v5 = 0;
        }
        v6 = v5 * 3600 >> 32;
        if (v6 >= g_1005e190)
            *(v1) = 0;
        sub_10040940((v6 CONCAT (unsigned int)(v5 * 3600)) / g_1005e190, v1);
    }
    else
    {
        lstrcpy(v1, "Inf");
    }
}
```

## cmd_screencount `0x1002cf9c`

Named — see [doc 11](../../11-*.md). _116 bytes. (leaf/helper — see body)_

```c
extern char g_1005f85c;

void sub_1002cf9c(void)
{
    int v4;  // ebx
    unsigned int i[37];  // ecx
    unsigned int v0[37];  // [bp-0x8]
    int v2;  // [bp+0xfd7d8]
    int v3;  // [bp+0xffffc]

    sub_10030225(v4);
    v2 = 0;
    for (i = 0x63fef8; i < 0x64a308; i = &i[1 + 5])
    {
        if (i[36] && *((int *)&g_1005f85c) == i[11])
        {
            v0 = i;
            if (!lstrcmpi(&i[1], /* unsupported instruction */ - 4264))
                v2 += 1;
        }
    }
    sub_10040940(v2, v3);
}
```

## cmd_mcount `0x1002d010`

Named — see [doc 11](../../11-*.md). _272 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[44];
    unsigned int field_2c;
} struct_0;

extern char g_1005f85c;
extern void* g_100f49d1;

void sub_1002d010(void)
{
    unsigned int v7;  // ebx
    void* iter;  // ebx
    void* v9;  // edi
    void* node;  // edi
    struct_0 *k;  // ebx
    struct_0 *v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0x4]
    void* v3;  // [bp+0xfd7ac]
    int v4;  // [bp+0xfd7d4]
    void* v5;  // [bp+0xfd7d8]
    unsigned short *v6;  // [bp+0xffffc]

    v1 = v7;
    iter = g_100f49d1;
    v9 = g_100f49d1 + 0x40000;
    for (v5 = NULL; iter < v9; iter += 0x200)
    {
        if (!*((char *)iter))
        {
            *((unsigned short *)iter) = 109;
            *((char *)&iter[32]) = 0;
            v5 = iter;
            break;
        }
        else if (*((short *)iter) == 109 || *((short *)iter) == 77)
        {
            *((char *)&iter[32]) = 0;
            v5 = iter;
            break;
        }
    }
    if (v5)
    {
        for (*((char *)v3) = 91; *((char *)node); node += 1);
        *((char *)&node[1]) = 93;
        v4 = 0;
        for (k = 0x63fef8; k < 0x64a308; k = &k[3].padding_0[24])
        {
            if (k->field_2c == *((int *)&g_1005f85c) && *((int *)&k[3].padding_0[0]) && k->padding_0[3] == 64)
            {
                v0 = k;
                wsprintfA(v5 + 32, "%d");
                sub_1002c228(k);
                if (sub_10040900(/* unsupported instruction */ - 4264))
                    v4 += 1;
            }
        }
        sub_10040940(v4, v6);
    }
    else
    {
        *(v6) = 0;
    }
}
```

## `sub_1002d049` `0x1002d049`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002d049(void)
{
}
```

## cmd_pcount `0x1002d122`

Named — see [doc 11](../../11-*.md). _272 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[44];
    unsigned int field_2c;
} struct_0;

extern char g_1005f85c;
extern void* g_100f49d1;

void sub_1002d122(void)
{
    unsigned int v7;  // ebx
    void* iter;  // ebx
    void* v9;  // edi
    void* node;  // edi
    struct_0 *k;  // ebx
    struct_0 *v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0x4]
    void* v3;  // [bp+0xfd7ac]
    int v4;  // [bp+0xfd7d4]
    void* v5;  // [bp+0xfd7d8]
    unsigned short *v6;  // [bp+0xffffc]

    v1 = v7;
    iter = g_100f49d1;
    v9 = g_100f49d1 + 0x40000;
    for (v5 = NULL; iter < v9; iter += 0x200)
    {
        if (!*((char *)iter))
        {
            *((unsigned short *)iter) = 112;
            *((char *)&iter[32]) = 0;
            v5 = iter;
            break;
        }
        else if (*((short *)iter) == 112 || *((short *)iter) == 80)
        {
            *((char *)&iter[32]) = 0;
            v5 = iter;
            break;
        }
    }
    if (v5)
    {
        for (*((char *)v3) = 91; *((char *)node); node += 1);
        *((char *)&node[1]) = 93;
        v4 = 0;
        for (k = 0x63fef8; k < 0x64a308; k = &k[3].padding_0[24])
        {
            if (k->field_2c == *((int *)&g_1005f85c) && *((int *)&k[3].padding_0[0]) && k->padding_0[3] != 64)
            {
                v0 = k;
                wsprintfA(v5 + 32, "%d");
                sub_1002c228(k);
                if (sub_10040900(/* unsupported instruction */ - 4264))
                    v4 += 1;
            }
        }
        sub_10040940(v4, v6);
    }
    else
    {
        *(v6) = 0;
    }
}
```

## `sub_1002d15b` `0x1002d15b`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1002d15b(void)
{
}
```

## cmd_monstersaround `0x1002d234`

Named — see [doc 11](../../11-*.md). _140 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[3];
    char field_3;
    char padding_4[32];
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
    char padding_30[96];
    unsigned int field_90;
} struct_0;

extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern char g_1005f85c;

void sub_1002d234(void)
{
    int v3;  // ebx
    unsigned int v4;  // edi
    struct_0 *iter;  // ecx
    int v6;  // eax
    int v1;  // [bp+0xfd7d8]
    int v2;  // [bp+0xffffc]

    v4 = sub_100300ce(v3);
    if (!v4)
        v4 += 1;
    v1 = 0;
    for (iter = 0x63fef8; iter < 0x64a308; iter = &iter[1].padding_4[16])
    {
        if (iter->field_90 && iter->field_3 == 64 && iter->field_2c == *((int *)&g_1005f85c))
        {
            v6 = iter->field_24 - g_1005f854;
            if ((iter->field_28 - g_1005f858 ^ iter->field_28 - g_1005f858 >> 31) - (iter->field_28 - g_1005f858 >> 31) <= v4 && (v6 ^ v6 >> 31) - (v6 >> 31) <= v4)
                v1 += 1;
        }
    }
    sub_10040940(v1, v2);
}
```

## cmd_playersaround `0x1002d2c0`

Named — see [doc 11](../../11-*.md). _148 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[3];
    char field_3;
    char padding_4[32];
    unsigned int field_24;
    unsigned int field_28;
    unsigned int field_2c;
    char padding_30[96];
    unsigned int field_90;
} struct_0;

extern char g_1005f7ed;
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern char g_1005f85c;

void sub_1002d2c0(void)
{
    int v3;  // ebx
    unsigned int v4;  // edi
    struct_0 *iter;  // ecx
    int v6;  // eax
    int v1;  // [bp+0xfd7d8]
    int v2;  // [bp+0xffffc]

    v4 = sub_100300ce(v3);
    if (!v4)
        v4 += 1;
    v1 = 0;
    for (iter = 0x63fef8; iter < 0x64a308; iter = &iter[1].padding_4[16])
    {
        if (iter->field_90 && iter->field_3 < 64 && iter != *((int *)&g_1005f7ed) && iter->field_2c == *((int *)&g_1005f85c))
        {
            v6 = iter->field_24 - g_1005f854;
            if ((iter->field_28 - g_1005f858 ^ iter->field_28 - g_1005f858 >> 31) - (iter->field_28 - g_1005f858 >> 31) <= v4 && (v6 ^ v6 >> 31) - (v6 >> 31) <= v4)
                v1 += 1;
        }
    }
    sub_10040940(v1, v2);
}
```

## `sub_1002d354` `0x1002d354`

_53 bytes. (leaf/helper — see body)_

```c
int sub_1002d354(void)
{
    int v2;  // ebx
    unsigned int v3;  // eax
    unsigned short *v4;  // ecx
    unsigned short *v1;  // [bp+0xffffc]

    sub_10030225(v2);
    v3 = sub_100303be(/* unsupported instruction */ - 4264);
    v4 = v1;
    *(v4) = 48;
    if (v3)
        *(v4) = 49;
}
```

## `sub_1002d389` `0x1002d389`

_53 bytes. (leaf/helper — see body)_

```c
int sub_1002d389(void)
{
    int v2;  // ebx
    unsigned int v3;  // eax
    unsigned short *v4;  // ecx
    unsigned short *v1;  // [bp+0xffffc]

    sub_10030225(v2);
    v3 = sub_1003a320(/* unsupported instruction */ - 4264);
    v4 = v1;
    *(v4) = 48;
    if (v3)
        *(v4) = 49;
}
```

## `sub_1002d3be` `0x1002d3be`

_53 bytes. (leaf/helper — see body)_

```c
int sub_1002d3be(void)
{
    int v2;  // ebx
    unsigned int v3;  // eax
    unsigned short *v4;  // ecx
    unsigned short *v1;  // [bp+0xffffc]

    sub_10030225(v2);
    v3 = sub_1003a3da(/* unsupported instruction */ - 4264);
    v4 = v1;
    *(v4) = 48;
    if (v3)
        *(v4) = 49;
}
```

## `sub_1002d3f3` `0x1002d3f3`

_53 bytes. (leaf/helper — see body)_

```c
int sub_1002d3f3(void)
{
    int v2;  // ebx
    unsigned int v3;  // eax
    unsigned short *v4;  // ecx
    unsigned short *v1;  // [bp+0xffffc]

    sub_10030225(v2);
    v3 = sub_1003a494(/* unsupported instruction */ - 4264);
    v4 = v1;
    *(v4) = 48;
    if (v3)
        *(v4) = 49;
}
```

## `sub_1002d428` `0x1002d428`

_53 bytes. (leaf/helper — see body)_

```c
int sub_1002d428(void)
{
    int v2;  // ebx
    unsigned int v3;  // eax
    unsigned short *v4;  // ecx
    unsigned short *v1;  // [bp+0xffffc]

    sub_10030225(v2);
    v3 = sub_1003a550(/* unsupported instruction */ - 4264);
    v4 = v1;
    *(v4) = 48;
    if (v3)
        *(v4) = 49;
}
```

## cmd_sbtime `0x1002d45d`

Named — see [doc 11](../../11-*.md). _28 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f49fd;

int sub_1002d45d(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(g_100f49fd / 1000, v1);
}
```

## cmd_sstime `0x1002d479`

Named — see [doc 11](../../11-*.md). _28 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f4a01;

int sub_1002d479(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(g_100f4a01 / 1000, v1);
}
```

## cmd_exectime `0x1002d495`

Named — see [doc 11](../../11-*.md). _19 bytes. (leaf/helper — see body)_

```c
extern int g_100580f0;

void sub_1002d495(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(g_100580f0, v1);
}
```

## cmd_synctime `0x1002d4a8`

Named — see [doc 11](../../11-*.md). _24 bytes. (leaf/helper — see body)_

```c
extern char g_100f933a;

int sub_1002d4a8(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(g_100f933a * 100, v1);
}
```

## cmd_fired `0x1002d4c0`

Named — see [doc 11](../../11-*.md). _19 bytes. (leaf/helper — see body)_

```c
extern int g_100f9328;

void sub_1002d4c0(void)
{
    int v1;  // [bp+0xffffc]

    sub_10040940(g_100f9328, v1);
}
```

## cmd_formattime `0x1002d4d3`

Named — see [doc 11](../../11-*.md). _99 bytes. refs "99h99m99s", "99:99:99"_

```c
extern char g_1013f325;

int sub_1002d4d3(void)
{
    int v3;  // ebx
    char v1;  // [bp+0xfef5c]
    int v2;  // [bp+0xffffc]

    sub_10030225(v3);
    if (v1 >= 48 && v1 <= 57)
    {
        sub_10040900(/* unsupported instruction */ - 4264);
        sub_1002bf38(/* unsupported instruction */ - 4264);
    }
    else if (g_1013f325)
    {
        lstrcpy(v2, "99h99m99s");
    }
    else
    {
        lstrcpy(v2, "99:99:99");
    }
}
```

## cmd_formatnum `0x1002d536`

Named — see [doc 11](../../11-*.md). _26 bytes. (leaf/helper — see body)_

```c
void sub_1002d536(void)
{
    int v0;  // [bp-0x4]

    sub_100300ce(v0);
    sub_1002bfd7(v0);
}
```

## cmd_ringslot `0x1002d550`

Named — see [doc 11](../../11-*.md). _32 bytes. (leaf/helper — see body)_

```c
int sub_1002d550(void)
{
    int v2;  // ebx
    int v3;  // eax
    int v1;  // [bp+0xffffc]

    v3 = sub_1002c077(v2);
    sub_10040940(v3, v1);
}
```

## cmd_beltslot `0x1002d570`

Named — see [doc 11](../../11-*.md). _32 bytes. (leaf/helper — see body)_

```c
int sub_1002d570(void)
{
    int v2;  // ebx
    int v3;  // eax
    int v1;  // [bp+0xffffc]

    v3 = sub_1002c077(v2);
    sub_10040940(v3, v1);
}
```

## cmd_backslot `0x1002d590`

Named — see [doc 11](../../11-*.md). _32 bytes. (leaf/helper — see body)_

```c
int sub_1002d590(void)
{
    int v2;  // ebx
    int v3;  // eax
    int v1;  // [bp+0xffffc]

    v3 = sub_1002c077(v2);
    sub_10040940(v3, v1);
}
```

## cmd_rhandslot `0x1002d5b0`

Named — see [doc 11](../../11-*.md). _32 bytes. (leaf/helper — see body)_

```c
int sub_1002d5b0(void)
{
    int v2;  // ebx
    int v3;  // eax
    int v1;  // [bp+0xffffc]

    v3 = sub_1002c077(v2);
    sub_10040940(v3, v1);
}
```

## cmd_lhandslot `0x1002d5d0`

Named — see [doc 11](../../11-*.md). _32 bytes. (leaf/helper — see body)_

```c
int sub_1002d5d0(void)
{
    int v2;  // ebx
    int v3;  // eax
    int v1;  // [bp+0xffffc]

    v3 = sub_1002c077(v2);
    sub_10040940(v3, v1);
}
```

## cmd_amuletslot `0x1002d5f0`

Named — see [doc 11](../../11-*.md). _32 bytes. (leaf/helper — see body)_

```c
int sub_1002d5f0(void)
{
    int v2;  // ebx
    int v3;  // eax
    int v1;  // [bp+0xffffc]

    v3 = sub_1002c077(v2);
    sub_10040940(v3, v1);
}
```

## cmd_bootsslot `0x1002d610`

Named — see [doc 11](../../11-*.md). _32 bytes. (leaf/helper — see body)_

```c
int sub_1002d610(void)
{
    int v2;  // ebx
    int v3;  // eax
    int v1;  // [bp+0xffffc]

    v3 = sub_1002c077(v2);
    sub_10040940(v3, v1);
}
```

## cmd_headslot `0x1002d630`

Named — see [doc 11](../../11-*.md). _32 bytes. (leaf/helper — see body)_

```c
int sub_1002d630(void)
{
    int v2;  // ebx
    int v3;  // eax
    int v1;  // [bp+0xffffc]

    v3 = sub_1002c077(v2);
    sub_10040940(v3, v1);
}
```

## cmd_chestslot `0x1002d650`

Named — see [doc 11](../../11-*.md). _32 bytes. (leaf/helper — see body)_

```c
int sub_1002d650(void)
{
    int v2;  // ebx
    int v3;  // eax
    int v1;  // [bp+0xffffc]

    v3 = sub_1002c077(v2);
    sub_10040940(v3, v1);
}
```

## cmd_legsslot `0x1002d670`

Named — see [doc 11](../../11-*.md). _32 bytes. (leaf/helper — see body)_

```c
int sub_1002d670(void)
{
    int v2;  // ebx
    int v3;  // eax
    int v1;  // [bp+0xffffc]

    v3 = sub_1002c077(v2);
    sub_10040940(v3, v1);
}
```

## cmd_topitem `0x1002d690`

Named — see [doc 11](../../11-*.md). _99 bytes. (leaf/helper — see body)_

```c
void sub_1002d690(void)
{
    int v7;  // ebx
    int v8;  // eax
    int v9;  // eax
    unsigned int v1;  // [bp+0xfd79c]
    unsigned int v2;  // [bp+0xfd7a8]
    unsigned int v3;  // [bp+0xfd7b0]
    int v4;  // [bp+0xfd7d4]
    int v5;  // [bp+0xfd7d8]
    unsigned short *v6;  // [bp+0xffffc]

    *(v6) = 48;
    if (v3)
    {
        v5 = sub_100300ce(v7);
        if (v2)
        {
            v4 = sub_100300ce();
            if (v1)
            {
                v8 = sub_100300ce();
                v9 = sub_1003a065(v5, v4, v8);
                sub_10040940(v9, v6);
            }
        }
    }
}
```

## cmd_istileitem `0x1002d6f3`

Named — see [doc 11](../../11-*.md). _140 bytes. (leaf/helper — see body)_

```c
int sub_1002d6f3(void)
{
    int v8;  // ebx
    int v9;  // eax
    unsigned int v10[2];  // eax
    unsigned int v11;  // eax
    unsigned int i[2];  // esi
    unsigned int v13;  // ecx
    unsigned int v1;  // [bp+0xfd794]
    unsigned int v2;  // [bp+0xfd7a0]
    unsigned int v3;  // [bp+0xfd7a8]
    unsigned int v4;  // [bp+0xfd7b0]
    int v5;  // [bp+0xfd7d4]
    int v6;  // [bp+0xfd7d8]
    unsigned short *v7;  // [bp+0xffffc]

    *(v7) = 48;
    if (v4)
    {
        v6 = sub_100300ce(v8);
        if (v3)
        {
            v5 = sub_100300ce();
            if (v2)
            {
                v9 = sub_100300ce();
                v10 = sub_1003a0f8(v6, v5, v9);
                if (v1 && v10)
                {
                    v11 = sub_100300ce(v10);
                    i = &v10[1];
                    for (v13 = v10[0]; v13; i = &i[1 + 1])
                    {
                        if (i[0] == v11)
                        {
                            *(v7) = 49;
                            break;
                        }
                        else
                        {
                            v13 -= 1;
                        }
                    }
                }
            }
        }
    }
}
```

## cmd_poisoned `0x1002d77f`

Named — see [doc 11](../../11-*.md). _25 bytes. (leaf/helper — see body)_

```c
extern char g_1005f7de;

char sub_1002d77f(void)
{
    int v2;  // eax
    int v1;  // [bp+0xffffc]

    if (g_1005f7de)
        v2 = _INSERT(0, 0, 1);
    sub_10040940(v2, v1);
}
```

## cmd_poisondmg `0x1002d798`

Named — see [doc 11](../../11-*.md). _34 bytes. (leaf/helper — see body)_

```c
extern char g_1005f7de;
extern int g_1005f7e1;

void sub_1002d798(void)
{
    unsigned short *v2;  // ecx
    unsigned short *v1;  // [bp+0xffffc]

    v2 = v1;
    *(v2) = 48;
    if (g_1005f7de)
        sub_10040940(g_1005f7e1, v2);
}
```

## cmd_manashielded `0x1002d7ba`

Named — see [doc 11](../../11-*.md). _25 bytes. (leaf/helper — see body)_

```c
extern char g_1005f7d9;

char sub_1002d7ba(void)
{
    int v2;  // eax
    int v1;  // [bp+0xffffc]

    if (g_1005f7d9)
        v2 = _INSERT(0, 0, 1);
    sub_10040940(v2, v1);
}
```

## cmd_battlesign `0x1002d7d3`

Named — see [doc 11](../../11-*.md). _25 bytes. (leaf/helper — see body)_

```c
extern char g_1005f7da;

char sub_1002d7d3(void)
{
    int v2;  // eax
    int v1;  // [bp+0xffffc]

    if (g_1005f7da)
        v2 = _INSERT(0, 0, 1);
    sub_10040940(v2, v1);
}
```

## cmd_redbattlesign `0x1002d7ec`

Named — see [doc 11](../../11-*.md). _25 bytes. (leaf/helper — see body)_

```c
extern char g_1005f7db;

char sub_1002d7ec(void)
{
    int v2;  // eax
    int v1;  // [bp+0xffffc]

    if (g_1005f7db)
        v2 = _INSERT(0, 0, 1);
    sub_10040940(v2, v1);
}
```

## cmd_drunk `0x1002d805`

Named — see [doc 11](../../11-*.md). _25 bytes. (leaf/helper — see body)_

```c
extern char g_1005f7df;

char sub_1002d805(void)
{
    int v2;  // eax
    int v1;  // [bp+0xffffc]

    if (g_1005f7df)
        v2 = _INSERT(0, 0, 1);
    sub_10040940(v2, v1);
}
```

## cmd_hasted `0x1002d81e`

Named — see [doc 11](../../11-*.md). _25 bytes. (leaf/helper — see body)_

```c
extern char g_1005f7dc;

char sub_1002d81e(void)
{
    int v2;  // eax
    int v1;  // [bp+0xffffc]

    if (g_1005f7dc)
        v2 = _INSERT(0, 0, 1);
    sub_10040940(v2, v1);
}
```

## cmd_paralyzed `0x1002d837`

Named — see [doc 11](../../11-*.md). _25 bytes. (leaf/helper — see body)_

```c
extern char g_1005f7dd;

char sub_1002d837(void)
{
    int v2;  // eax
    int v1;  // [bp+0xffffc]

    if (g_1005f7dd)
        v2 = _INSERT(0, 0, 1);
    sub_10040940(v2, v1);
}
```

## cmd_inpz `0x1002d850`

Named — see [doc 11](../../11-*.md). _25 bytes. (leaf/helper — see body)_

```c
extern char g_1005f7e0;

char sub_1002d850(void)
{
    int v2;  // eax
    int v1;  // [bp+0xffffc]

    if (g_1005f7e0)
        v2 = _INSERT(0, 0, 1);
    sub_10040940(v2, v1);
}
```

## cmd_navion `0x1002d869`

Named — see [doc 11](../../11-*.md). _25 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f551;

char sub_1002d869(void)
{
    int v2;  // eax
    int v1;  // [bp+0xffffc]

    if (g_1005f551)
        v2 = _INSERT(0, 0, 1);
    sub_10040940(v2, v1);
}
```

## cmd_itemcount `0x1002d882`

Named — see [doc 11](../../11-*.md). _83 bytes. (leaf/helper — see body)_

```c
int sub_1002d882(void)
{
    int v3;  // ebx
    int v4;  // eax
    char v1;  // [bp+0xfef5c]
    int v2;  // [bp+0xffffc]

    sub_10030225(v3);
    if (v1 >= 48 && v1 <= 57)
    {
        sub_10040900(/* unsupported instruction */ - 4264);
        sub_1003004d(/* unsupported instruction */ - 4264);
    }
    else
    {
        v4 = sub_1002fff4();
    }
    sub_10040940(v4, v2);
}
```

## cmd_winitemcount `0x1002d8d5`

Named — see [doc 11](../../11-*.md). _86 bytes. (leaf/helper — see body)_

```c
int sub_1002d8d5(void)
{
    int v3;  // ebx
    int v4;  // eax
    char v1;  // [bp+0xfef5c]
    int v2;  // [bp+0xffffc]

    sub_10030225(v3);
    if (v1 >= 48 && v1 <= 57)
    {
        sub_10040900(/* unsupported instruction */ - 4264);
        sub_1003004d(/* unsupported instruction */ - 4264);
    }
    else
    {
        v4 = sub_1002fff4();
    }
    sub_10040940(v4, v2);
}
```

## cmd_fileisline `0x1002d92b`

Named — see [doc 11](../../11-*.md). _89 bytes. (leaf/helper — see body)_

```c
int sub_1002d92b(void)
{
    int v0;  // [bp-0x4]
    unsigned int v2;  // [bp+0xfd7a4]
    unsigned short *v3;  // [bp+0xffffc]

    *(v3) = 48;
    sub_10030225(v0);
    if (v2)
    {
        sub_10030225();
        if (sub_100254f8(/* unsupported instruction */ - 4264, /* unsupported instruction */ - 6264))
            *(v3) = 49;
    }
}
```

