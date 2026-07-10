# elfbot.dll decompiled — jiru 0x10310d20..0x10312d00

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10310d20` `0x10310d20`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10310d20(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 231;
    v7 = 223;
    v8 = 26;
    v9 = 214;
    v10 = 171;
    v11 = 2;
    v12 = 217;
    v13 = 183;
    v0 = 2;
    v14 = 7;
    idx = (&v6)[a0 >> 2 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_10310e30` `0x10310e30`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10310e30(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 160;
    v7 = 250;
    v8 = 52;
    v9 = 113;
    v10 = 18;
    v11 = 40;
    v12 = 50;
    v13 = 84;
    v0 = 13;
    v14 = 7;
    idx = (&v6)[a0 >> 13 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_10310f40` `0x10310f40`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10310f40(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 226;
    v7 = 101;
    v8 = 0x22;
    v9 = 58;
    v10 = 182;
    v11 = 26;
    v12 = 180;
    v13 = 41;
    v0 = 0x11;
    v14 = 7;
    idx = (&v6)[a0 >> 0x11 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_10311050` `0x10311050`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10311050(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 28;
    v7 = 207;
    v8 = 2;
    v9 = 77;
    v10 = 245;
    v11 = 47;
    v12 = 98;
    v13 = 194;
    v0 = 10;
    v14 = 7;
    idx = (&v6)[a0 >> 10 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_10311160` `0x10311160`

_981 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned int field_28;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b1c4;
extern struct_1 *g_1038b1c8;
extern struct_1 *g_1038b1cc;
extern struct_1 *g_1038b1d0;
extern struct_1 *g_1038b1d4;
extern struct_1 *g_1038b1dc;
extern unsigned int g_1038e180;
extern char g_1038f8e4;
extern unsigned short g_1038f8e8;

int sub_10311160(struct_0 *ptr)
{
    char *v0;  // [bp-0x33c]
    char *v1;  // [bp-0x338]
    char *v2;  // [bp-0x334]
    char *v3;  // [bp-0x330]
    char *v4;  // [bp-0x328]
    char v5;  // [bp-0x324]
    char v6;  // [bp-0x323]
    char *v7;  // [bp-0x218], Other Possible Types: unsigned short *
    unsigned short v8;  // [bp-0x214]
    char v9;  // [bp-0x212]
    unsigned int v10;  // [bp-0x8]
    char v11;  // [bp-0x4]

    v10 = g_1038e180 ^ &v11;
    memset(ptr, 0, 16);
    g_1038b1c4(&ptr->padding_0[16]);
    ptr->field_28 = g_1038b1c8(&ptr->padding_0[16]);
    if ((char)sub_10311540())
    {
        v8 = g_1038f8e8;
        sub_10350ad0(&v9, 0, 518);
        g_1038b1cc(0, &v8, 260);
        v7 = sub_103124e0(&v8, 92);
        v3 = (!v7 ? &v8 : v7 + 2);
        sub_10352da8(&ptr[12].padding_0[36], v3);
        v7 = sub_103124c0(&ptr[12].padding_0[36], 46);
        if (v7)
            *(v7) = 0;
        g_1038b1cc(0, &ptr[24].padding_0[28], 260);
        if (g_1038b1d0(&ptr[24].padding_0[28], &v8, 260))
        {
            v7 = sub_103124e0(&v8, 92);
            v2 = (!v7 ? &v8 : v7 + 2);
            sub_10352da8(&ptr[24].padding_0[28], v2);
            v7 = sub_103124c0(&ptr[24].padding_0[28], 46);
            if (v7)
                *(v7) = 0;
        }
        else
        {
            sub_10352da8(&ptr[24].padding_0[28], &g_1038f8e8);
        }
    }
    else
    {
        v5 = g_1038f8e4;
        sub_10350ad0(&v6, 0, 259);
        g_1038b1d4(0, &v5, 260);
        v4 = sub_103124a0(&v5, 92);
        v1 = (!v4 ? &v5 : v4 + 1);
        sub_10352cb0(ptr + 1, v1);
        v4 = sub_10312480(ptr + 1, 46);
        if (v4)
            *(v4) = 0;
        g_1038b1d4(0, &ptr[6].field_28, 260);
        if (g_1038b1dc(&ptr[6].field_28, &v5, 260))
        {
            v4 = sub_103124a0(&v5, 92);
            v0 = (!v4 ? &v5 : v4 + 1);
            sub_10352cb0(&ptr[6].field_28, v0);
            v4 = sub_10312480(&ptr[6].field_28, 46);
            if (v4)
                *(v4) = 0;
        }
        else
        {
            sub_10352cb0(&ptr[6].field_28, &g_1038f8e4);
        }
    }
    return sub_10351225();
}
```

## `sub_10311540` `0x10311540`

_97 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1c0;
extern unsigned int g_1038e180;
extern char g_103a1bc8;
extern char g_103a1bc9;

char sub_10311540(void)
{
    unsigned int v0;  // [bp-0xa4]
    unsigned int v1;  // [bp-0x94]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]

    v2 = g_1038e180 ^ &v3;
    if (!g_103a1bc9)
    {
        v0 = 148;
        g_1038b1c0(&v0);
        g_103a1bc8 = v1 == 2;
        g_103a1bc9 = 1;
    }
    return sub_10351225();
}
```

## `sub_103115b0` `0x103115b0`

_208 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    struct struct_0 *field_8;
} struct_0;

typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

extern struct_2 *g_1038b1b8;
extern struct_2 *g_1038b1bc;
extern unsigned int g_1038e180;

unsigned int sub_103115b0(struct_0 **idx, int a1)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4143
    unsigned long v12;  // 4157
    unsigned int v13;  // eax
    unsigned long v14;  // 4113
    struct_0 *v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x1c]
    struct_0 *v2;  // [bp-0x18]
    struct_0 *v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_10369e0b;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    g_1038b1b8(idx + 4, g_1038e180 ^ &v7);
    v1 = sub_10350a53(12);
    v6 = 0;
    v0 = (!v1 ? 0 : sub_10312500(a1));
    v2 = v0;
    v6 = 4294967295;
    v3 = v2;
    if (!idx[3])
    {
        idx[3] = v3;
        idx[2] = v3;
    }
    else
    {
        idx[3]->field_8 = v3;
        idx[3] = idx[3]->field_8;
    }
    v13 = g_1038b1bc(idx + 4);
    v14 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v14) = v4;
    return v13;
}
```

## `sub_10311680` `0x10311680`

_189 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[8];
    struct struct_0 *field_8;
    unsigned int field_c;
} struct_1;

typedef struct struct_0 {
    int field_0;
    char padding_4[4];
    unsigned int field_8;
} struct_0;

typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

extern struct_2 *g_1038b1b8;
extern struct_2 *g_1038b1bc;

char sub_10311680(struct_1 *idx, int a1, int a2)
{
    unsigned int v0;  // [bp-0x1c]
    struct_0 *v1;  // [bp-0x14]
    struct_0 *v2;  // [bp-0x10]
    struct_0 *v3;  // [bp-0xc]
    char v4;  // [bp-0x5]

    g_1038b1b8(idx + 1);
    v4 = 0;
    if (!idx->field_8)
    {
        g_1038b1bc(idx + 1);
        return v4;
    }
    v3 = idx->field_8;
    idx->field_8 = v3->field_8;
    if (!idx->field_8)
        idx->field_c = 0;
    if (a1 && a2 > NULL)
    {
        sub_10352fb0(a1, v3->field_0, a2);
        *((char *)(a1 + a2 - 1)) = 0;
    }
    v1 = v3;
    v2 = v1;
    if (v2)
        v0 = sub_10312560(1);
    else
        v0 = 0;
    v4 = 1;
    g_1038b1bc(idx + 1);
    return v4;
}
```

## `sub_10311740` `0x10311740`

_208 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    struct struct_0 *field_8;
} struct_0;

typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

extern struct_2 *g_1038b1b8;
extern struct_2 *g_1038b1bc;
extern unsigned int g_1038e180;

unsigned int sub_10311740(struct_0 **idx, int a1)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4143
    unsigned long v12;  // 4157
    unsigned int v13;  // eax
    unsigned long v14;  // 4113
    struct_0 *v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x1c]
    struct_0 *v2;  // [bp-0x18]
    struct_0 *v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_10369e31;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    g_1038b1b8(idx + 4, g_1038e180 ^ &v7);
    v1 = sub_10350a53(12);
    v6 = 0;
    v0 = (!v1 ? 0 : sub_103125d0(a1));
    v2 = v0;
    v6 = 4294967295;
    v3 = v2;
    if (!idx[3])
    {
        idx[3] = v3;
        idx[2] = v3;
    }
    else
    {
        idx[3]->field_8 = v3;
        idx[3] = idx[3]->field_8;
    }
    v13 = g_1038b1bc(idx + 4);
    v14 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v14) = v4;
    return v13;
}
```

## `sub_10311810` `0x10311810`

_193 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[8];
    struct struct_0 *field_8;
    unsigned int field_c;
} struct_1;

typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    unsigned int field_8;
} struct_0;

typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

extern struct_2 *g_1038b1b8;
extern struct_2 *g_1038b1bc;

char sub_10311810(struct_1 *idx, int a1, int a2)
{
    unsigned int v0;  // [bp-0x1c]
    struct_0 *v1;  // [bp-0x14]
    struct_0 *v2;  // [bp-0x10]
    struct_0 *v3;  // [bp-0xc]
    char v4;  // [bp-0x5]

    g_1038b1b8(idx + 1);
    v4 = 0;
    if (!idx->field_8)
    {
        g_1038b1bc(idx + 1);
        return v4;
    }
    v3 = idx->field_8;
    idx->field_8 = v3->field_8;
    if (!idx->field_8)
        idx->field_c = 0;
    if (a1 && a2 > NULL)
    {
        sub_103530ea(a1, v3->field_4, a2);
        *((unsigned short *)(a1 + a2 * 2 - 2)) = 0;
    }
    v1 = v3;
    v2 = v1;
    if (v2)
        v0 = sub_10312560(1);
    else
        v0 = 0;
    v4 = 1;
    g_1038b1bc(idx + 1);
    return v4;
}
```

## `sub_103118e0` `0x103118e0`

_93 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b02c;
extern struct_0 *g_1038b128;
extern struct_0 *g_1038b1b4;
extern struct_0 *g_1038b294;
extern unsigned int g_103a1be8;

char sub_103118e0(void)
{
    char v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v1 = g_1038b02c(0, 0, sub_10311940, 0, 0, &v0);
    g_1038b128(v1);
    if (!v1)
        return 0;
    while (!g_1038b294(g_103a1be8))
    {
        g_1038b1b4(1);
    }
    g_1038b1b4(100);
    return 1;
}
```

## `sub_10311940` `0x10311940`

_833 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b030;
extern struct_0 *g_1038b034;
extern struct_0 *g_1038b038;
extern struct_0 *g_1038b03c;
extern struct_0 *g_1038b1b4;
extern struct_0 *g_1038b294;
extern struct_0 *g_1038b298;
extern struct_0 *g_1038b344;
extern struct_0 *g_1038b348;
extern struct_0 *g_1038b34c;
extern struct_0 *g_1038b350;
extern struct_0 *g_1038b354;
extern struct_0 *g_1038b35c;
extern unsigned int g_1038e180;
extern unsigned int g_103a1be8;
extern unsigned int g_103a1bec;

unsigned int sub_10311940(void)
{
    unsigned long v13;  // ldt
    unsigned long v14;  // gdt
    unsigned int v24;  // eax
    unsigned int v25;  // eax
    unsigned int v27;  // eax
    unsigned short v15;  // fs
    unsigned long v16;  // 4134
    unsigned long v17;  // 4148
    unsigned int v18;  // eax
    unsigned int v20;  // eax
    unsigned int v22;  // eax
    int v0;  // [bp-0x50]
    int v1;  // [bp-0x4c]
    int v2;  // [bp-0x48]
    int v3;  // [bp-0x44]
    int v4;  // [bp-0x40]
    int v5;  // [bp-0x3c]
    char v6;  // [bp-0x30]
    unsigned int v7;  // [bp-0x14]
    unsigned int v8;  // [bp-0x10]
    unsigned int v9;  // [bp-0xc]
    char v10;  // [bp-0x8], Other Possible Types: unsigned int
    char v11;  // [bp-0x4]

    v10 = 4294967295;
    v9 = sub_10369e5c;
    v16 = _ccall(v13, v14, (unsigned int)v15, 0);
    v8 = *((int *)v16);
    v17 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int **)v17) = &v8;
    g_103a1be8 = sub_10311dd0(g_1038e180 ^ &v11);
    v7 = g_1038b03c(g_1038e180 ^ &v11);
    while (true)
    {
        if (g_1038b344(&v6, g_103a1be8, 0, 0, 1))
        {
            g_1038b348(&v6);
            g_1038b34c(&v6);
        }
        else if ((char)sub_10312640() && g_1038b03c() > v7 + 500)
        {
            v7 = g_1038b03c();
            if (!g_103a1bec)
            {
                g_1038b350(sub_10311cd0, 0);
            }
            else if (g_1038b294(g_103a1bec))
            {
                sub_10312680();
                v10 = 0;
                sub_103126f0();
                v10 = 1;
                if (sub_10311540())
                {
                    while (sub_10311810(&g_103a1be8, sub_10336b20(0x10000), 0x10000))
                    {
                        if (g_1038b354(g_103a1bec))
                        {
                            v18 = sub_103530d4(sub_10336b20());
                            v4 = g_1038b038(8194, v18 * 2 + 1);
                            v5 = g_1038b034(v4);
                            sub_10352da8(v5, sub_10336b20(v4));
                            g_1038b030(v4);
                            v20 = sub_1034fede(1000, 0, v4);
                            g_1038b35c(g_103a1bec, 1000, g_103a1be8, v20);
                        }
                        else
                        {
                            sub_10311c90(sub_10336b20(sub_10336b20(0x10000)));
                            v22 = sub_10352f20(sub_10336b20());
                            v2 = g_1038b038(8194, v22 + 1);
                            v3 = g_1038b034(v2);
                            sub_10352cb0(v3, sub_10336b20(v2));
                            g_1038b030(v2);
                            v24 = sub_1034fede(1000, 0, v2);
                            g_1038b298(g_103a1bec, 1000, g_103a1be8, v24);
                        }
                    }
                }
                else
                {
                    while (sub_10311680(&g_103a1be8, sub_10336b20(0x10000), 0x10000))
                    {
                        v25 = sub_10352f20(sub_10336b20());
                        v0 = g_1038b038(8194, v25 + 1);
                        v1 = g_1038b034(v0);
                        sub_10352cb0(v1, sub_10336b20(v0));
                        g_1038b030(v0);
                        v27 = sub_1034fede(1000, 0, v0);
                        g_1038b298(g_103a1bec, 1000, g_103a1be8, v27);
                    }
                }
                v10 = 0;
                sub_103126c0();
                v10 = 4294967295;
                sub_103126c0();
            }
            else
            {
                g_103a1bec = 0;
            }
        }
        else
        {
            g_1038b1b4(1);
        }
    }
}
```

## `sub_10311c90` `0x10311c90`

_57 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b040;
extern struct_0 *g_1038b044;

int sub_10311c90(unsigned int a0, unsigned int a1, unsigned int a2)
{
    char v0;  // [bp+0x0]

    if (!g_1038b044(a0, 1, &v0))
    {
        g_1038b040(0, 0, a0, 4294967295, a1, a2, 0, 0);
        return a1;
    }
    return a0;
}
```

## `sub_10311ca8` `0x10311ca8`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10311ca8(void)
{
}
```

## `sub_10311cd0` `0x10311cd0`

_254 bytes. refs "dll loader", "System", "System"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b048;
extern struct_0 *g_1038b04c;
extern struct_0 *g_1038b338;
extern struct_0 *g_1038b33c;
extern struct_0 *g_1038b340;
extern char g_103a1be8;
extern unsigned int g_103a1bec;
extern char g_103a1c10;
extern char g_103a1c14;

unsigned int sub_10311cd0(unsigned int a0)
{
    unsigned short v0;  // [bp-0x18]
    unsigned short v1;  // [bp-0x14]
    unsigned short v2;  // [bp-0x10]
    unsigned short v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int

    g_1038b338(a0, &v4);
    if (v4 == *((int *)&g_103a1c10) && a0 != *((int *)&g_103a1be8))
    {
        if (sub_10311540())
        {
            v3 = g_1038b04c(L"dll loader");
            v2 = g_1038b04c(L"System");
            g_1038b33c(a0, 992, *((int *)&g_103a1be8), v3 | v2 * 0x10000);
        }
        else
        {
            v1 = g_1038b048(&g_103a1c14);
            v0 = g_1038b048("System");
            g_1038b340(a0, 992, *((int *)&g_103a1be8), v1 | v0 * 0x10000);
        }
    }
    return (!g_103a1bec ? 1 : 0);
}
```

## `sub_10311dc3` `0x10311dc3`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10311dc3(void)
{
}
```

## `sub_10311dd0` `0x10311dd0`

_361 bytes. refs "SwPDDE", "DDE Processing", "SwPDDE"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b050;
extern struct_0 *g_1038b324;
extern struct_0 *g_1038b328;
extern struct_0 *g_1038b32c;
extern struct_0 *g_1038b330;
extern struct_0 *g_1038b334;

unsigned int sub_10311dd0(void)
{
    unsigned int v25;  // eax
    unsigned int v26;  // eax
    unsigned int v0;  // [bp-0x64]
    unsigned int v1;  // [bp-0x60]
    unsigned int v2;  // [bp-0x5c]
    unsigned int v3;  // [bp-0x58]
    unsigned int v4;  // [bp-0x54]
    unsigned int v5;  // [bp-0x50]
    unsigned int v6;  // [bp-0x4c]
    unsigned int v7;  // [bp-0x48]
    unsigned int v8;  // [bp-0x44]
    unsigned int v9;  // [bp-0x40]
    unsigned int v10;  // [bp-0x3c]
    unsigned int v11;  // [bp-0x38]
    unsigned int v12;  // [bp-0x34]
    unsigned int v13;  // [bp-0x30]
    unsigned int v14;  // [bp-0x2c]
    unsigned int v15;  // [bp-0x28]
    unsigned int v16;  // [bp-0x24]
    unsigned int v17;  // [bp-0x20]
    unsigned int v18;  // [bp-0x1c]
    unsigned int v19;  // [bp-0x18]
    unsigned int v20;  // [bp-0x14]
    unsigned int v21;  // [bp-0x10]
    unsigned int v22;  // [bp-0xc]
    unsigned int v23;  // [bp-0x8]

    if (!sub_10311540())
    {
        v11 = "SwPDDE";
        v1 = 11;
        v2 = sub_10311f40;
        v3 = 0;
        v4 = 0;
        v5 = g_1038b050(0);
        v6 = 0;
        v7 = g_1038b324(0, 0x7f00);
        v8 = 6;
        v9 = 0;
        v10 = v11;
        g_1038b330(&v1);
        v26 = g_1038b050(0, 0);
        v0 = g_1038b334(0x40300, v11, "DDE Processing", 0x2cf0000, 0x80000000, 0x80000000, 0x80000000, 0x80000000, 0, 0, v26);
        return v0;
    }
    v23 = L"SwPDDE";
    v13 = 11;
    v14 = sub_10311f40;
    v15 = 0;
    v16 = 0;
    v17 = g_1038b050(0);
    v18 = 0;
    v19 = g_1038b324(0, 0x7f00);
    v20 = 6;
    v21 = 0;
    v22 = v23;
    g_1038b328(&v13);
    v25 = g_1038b050(0, 0);
    v12 = g_1038b32c(0x40300, v23, L"DDE Processing", 0x2cf0000, 0x80000000, 0x80000000, 0x80000000, 0x80000000, 0, 0, v25);
    return v12;
}
```

## `sub_10311e90` `0x10311e90`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10311e90(void)
{
}
```

## `sub_10311f40` `0x10311f40`

_1265 bytes. refs "dll loader", "DLLLOA~1", "System"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b030;
extern struct_0 *g_1038b034;
extern struct_0 *g_1038b048;
extern struct_0 *g_1038b04c;
extern struct_0 *g_1038b054;
extern struct_0 *g_1038b058;
extern struct_0 *g_1038b05c;
extern struct_0 *g_1038b060;
extern struct_0 *g_1038b298;
extern struct_0 *g_1038b310;
extern struct_0 *g_1038b31c;
extern struct_0 *g_1038b320;
extern struct_0 *g_1038b33c;
extern struct_0 *g_1038b340;
extern unsigned int g_1038e180;
extern char g_1038f8e4;
extern unsigned short g_1038f8e8;
extern struct_0 *g_103a1be8;
extern unsigned int g_103a1bec;
extern int g_103a1c14;
extern int g_103a1d18;

int sub_10311f40(int v2, unsigned int a0, int a1, unsigned int a2)
{
    unsigned int v22;  // eax
    unsigned int v23;  // edx
    unsigned int v24;  // ecx
    unsigned int v25;  // edx
    unsigned int v26;  // ecx
    unsigned int v27;  // eax
    unsigned int v28;  // edx
    unsigned int v29;  // eax
    unsigned int v30;  // eax
    unsigned int v31;  // eax
    int v0;  // [bp-0x668]
    int v1;  // [bp-0x664]
    unsigned int v3;  // [bp-0x65c]
    int v4;  // [bp-0x62c]
    int v5;  // [bp-0x628]
    char v6;  // [bp-0x624], Other Possible Types: unsigned int
    char v7;  // [bp-0x620], Other Possible Types: unsigned int
    int v8;  // [bp-0x61c]
    int v9;  // [bp-0x618]
    char v10;  // [bp-0x614]
    char v11;  // [bp-0x613]
    char v12;  // [bp-0x514]
    char v13;  // [bp-0x513]
    unsigned short v14;  // [bp-0x414]
    char v15;  // [bp-0x412]
    unsigned short v16;  // [bp-0x214]
    char v17;  // [bp-0x212]
    unsigned int v18;  // [bp-0x14]
    unsigned short v19;  // [bp-0x10]
    unsigned short v20;  // [bp-0xc]
    char v21;  // [bp-0x4]

    v18 = g_1038e180 ^ &v21;
    switch (a0)
    {
    case 992:
        v0 = a1;
        v20 = a2;
        v19 = a2 >> 16;
        if (sub_10311540())
        {
            v16 = g_1038f8e8;
            sub_10350ad0(&v17, 0, 0x1fe);
            v14 = g_1038f8e8;
            v22 = _INSERT(sub_10350ad0(&v15, 0, 0x1fe), 0, v20);
            g_1038b060(v22, &v16, 0x100);
            v23 = _INSERT(0, 0, v19);
            g_1038b060(v23, &v14, 0x100);
            if (sub_103530d4(&v16) && (!sub_10363b4b(&v16, L"dll loader") || !sub_10363b4b(&v16, L"DLLLOA~1")) && !sub_10363b4b(&v14, L"System"))
            {
                v24 = _INSERT(0, 0, v20);
                g_1038b05c(v24);
                v25 = _INSERT(0, 0, v19);
                g_1038b05c(v25);
                v20 = g_1038b04c(&v16);
                v19 = g_1038b04c(&v14);
                v3 = v20 | v19 * 0x10000;
                v1 = 996;
                g_1038b33c(v0, 996, v2, v20 | v19 * 0x10000);
            }
        }
        else
        {
            v12 = g_1038f8e4;
            sub_10350ad0(&v13, 0, 0xff);
            v10 = g_1038f8e4;
            sub_10350ad0(&v11, 0, 0xff);
            v26 = _INSERT(0, 0, v20);
            v27 = _INSERT(g_1038b058(v26, &v12, 0x100), 0, v19);
            g_1038b058(v27, &v10, 0x100);
            if (sub_10352f20(&v12) && (!sub_1035ddf8(&v12, &g_103a1c14) || !sub_1035ddf8(&v12, &g_103a1d18)) && !sub_1035ddf8(&v10, "System"))
            {
                v28 = _INSERT(0, 0, v20);
                v29 = _INSERT(g_1038b05c(v28), 0, v19);
                g_1038b05c(v29);
                v20 = g_1038b048(&v12);
                v19 = g_1038b048(&v10);
                v3 = v20 | v19 * 0x10000;
                v1 = 996;
                g_1038b340(v0, 996, v2, v20 | v19 * 0x10000);
            }
        }
        break;
    case 993:
        v31 = sub_1034fede(993, v2, 0, 0);
        g_1038b298(a1, 993, v31);
        break;
    case 996:
        if (g_1038b310())
        {
            g_103a1bec = a1;
            g_1038b05c(a2 & 0xffff);
            g_1038b05c(a2 >> 16);
        }
        else
        {
            sub_1034feea(996, a2, &v6, &v7);
            if (!((unsigned short)v6 & 0x8000))
            {
                if (sub_10311540())
                {
                    v5 = g_1038b034(v7);
                    sub_10311740(&g_103a1be8, v5);
                    g_1038b030(v7);
                }
                else
                {
                    v4 = g_1038b034(v7);
                    sub_103115b0(&g_103a1be8, v4);
                    g_1038b030(v7);
                }
            }
            sub_1034fee4(996, a2);
            g_1038b054(v7);
        }
        break;
    case 1000:
        if (sub_10311540())
        {
            v9 = g_1038b034(a2);
            sub_10311740(&g_103a1be8, v9);
            g_1038b030(a2);
        }
        else
        {
            v8 = g_1038b034(a2);
            sub_103115b0(&g_103a1be8, v8);
            g_1038b030(a2);
        }
        v30 = sub_1034fede(996, 0x8000, a2);
        g_1038b298(a1, 996, v2, v30);
        break;
    default:
        if (sub_10311540())
            g_1038b31c(v2, a0, a1, a2);
        g_1038b320(v2, a0, a1, a2);
    }
    return sub_10351225(v0, v1, v2, v3);
}
```

## `sub_10312460` `0x10312460`

_19 bytes. (leaf/helper — see body)_

```c
int sub_10312460(int a0)
{
    char v0;  // [bp+0x0]

    return sub_10312660(a0, &v0);
}
```

## `sub_10312480` `0x10312480`

_21 bytes. (leaf/helper — see body)_

```c
int sub_10312480(int a0, int a1)
{
    char v0;  // [bp+0x0]

    return sub_10352de0(a0, a1, &v0);
}
```

## `sub_103124a0` `0x103124a0`

_21 bytes. (leaf/helper — see body)_

```c
int sub_103124a0(int a0, int a1)
{
    char v0;  // [bp+0x0]

    return sub_10352ea0(a0, a1, &v0);
}
```

## `sub_103124c0` `0x103124c0`

_22 bytes. (leaf/helper — see body)_

```c
short sub_103124c0(int a0, unsigned short a1)
{
    int v1;  // eax
    char v0;  // [bp+0x0]

    v1 = _INSERT(0, 0, a1);
    return sub_10352ecd(a0, v1, &v0);
}
```

## `sub_103124e0` `0x103124e0`

_22 bytes. (leaf/helper — see body)_

```c
short sub_103124e0(int a0, unsigned short a1)
{
    int v1;  // eax
    char v0;  // [bp+0x0]

    v1 = _INSERT(0, 0, a1);
    return sub_10352eef(a0, v1, &v0);
}
```

## `sub_10312500` `0x10312500`

_91 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    int field_0;
    unsigned int field_4;
    unsigned int field_8;
} struct_0;

struct_0 * sub_10312500(struct_0 *idx, int a1)
{
    unsigned int v0;  // [bp-0x8]

    idx->field_4 = 0;
    v0 = sub_1034fef0(sub_10352f20(a1, idx) + 1);
    idx->field_0 = v0;
    sub_10352cb0(idx->field_0, a1);
    idx->field_8 = 0;
    return idx;
}
```

## `sub_10312560` `0x10312560`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10312560(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10312590(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_10312590` `0x10312590`

_54 bytes. (leaf/helper — see body)_

```c
int sub_10312590(unsigned int *a0)
{
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v1 = *(a0);
    sub_10350eb5(v1, a0);
    v0 = a0[1];
    return sub_10350eb5(v0);
}
```

## `sub_103125d0` `0x103125d0`

_108 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    int field_4;
    unsigned int field_8;
} struct_0;

struct_0 * sub_103125d0(struct_0 *idx, int a1)
{
    unsigned int v1;  // eax
    unsigned int v0;  // [bp-0x8]

    idx->field_0 = 0;
    v1 = sub_103530d4(a1, idx) + 1;
    v0 = sub_1034fef0(-((v1 >= 0x40000000 ? 1 : 0) & 1) | v1 * 2);
    idx->field_4 = v0;
    sub_10352da8(idx->field_4, a1);
    idx->field_8 = 0;
    return idx;
}
```

## `sub_10312640` `0x10312640`

_25 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
} struct_0;

int sub_10312640(struct_0 *a0)
{
    return _INSERT(a0, 0, a0->field_8);
}
```

## `sub_10312660` `0x10312660`

_22 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned int field_28;
} struct_0;

struct_0 * sub_10312660(struct_0 *a0, unsigned int a1)
{
    a0->field_28 = a1;
    return a0;
}
```

## `sub_10312680` `0x10312680`

_61 bytes. (leaf/helper — see body)_

```c
int * sub_10312680(int *a0)
{
    unsigned int v0;  // [bp-0x8]

    v0 = sub_1034fef0(0x20000, a0);
    *(a0) = v0;
    sub_10350ad0(*(a0), 0, 0x20000);
    return a0;
}
```

## `sub_103126c0` `0x103126c0`

_33 bytes. (leaf/helper — see body)_

```c
int sub_103126c0(int *a0)
{
    char v0;  // [bp+0x0]

    return sub_10350eb5(*(a0), a0, *(a0), &v0);
}
```

## `sub_103126f0` `0x103126f0`

_61 bytes. (leaf/helper — see body)_

```c
int * sub_103126f0(int *a0)
{
    unsigned int v0;  // [bp-0x8]

    v0 = sub_1034fef0(0x10000, a0);
    *(a0) = v0;
    sub_10350ad0(*(a0), 0, 0x10000);
    return a0;
}
```

## `sub_10312730` `0x10312730`

_474 bytes. refs "INITIALIZEDLLADDR", ", sub_1031e0a0);
            g_1038b064(", "INITIALIZEDLLADDR"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b064;
extern struct_0 *g_1038b068;
extern unsigned int g_1038c7f4;
extern unsigned int g_1038c808;
extern unsigned int g_1038c834;
extern unsigned int g_1038e180;
extern char g_1038f8e4;
extern unsigned int g_103a2234;
extern unsigned int g_103a22a8;
extern unsigned int g_103a22c4;
extern unsigned int g_103a22c8;
extern unsigned int g_103a24d8;

int sub_10312730(unsigned int a0, int a1, int a2)
{
    unsigned long v14;  // ldt
    unsigned long v15;  // gdt
    unsigned short v16;  // fs
    unsigned long v17;  // 4190
    unsigned int v18;  // ecx
    unsigned int v19;  // ebx
    unsigned int v20;  // esi
    unsigned int v21;  // edi
    unsigned long v22;  // 4194
    unsigned long v23;  // 4120
    unsigned int v0;  // [bp-0x78]
    unsigned int v1;  // [bp-0x74]
    unsigned int v2;  // [bp-0x70]
    unsigned int v3;  // [bp-0x6c]
    unsigned int v4;  // [bp-0x64]
    unsigned int v5;  // [bp-0x60]
    char v6;  // [bp-0x5c]
    char v7;  // [bp-0x5b]
    unsigned int v8;  // [bp-0x18]
    char *v9;  // [bp-0x14], Other Possible Types: unsigned int
    unsigned int v10;  // [bp-0x10]
    unsigned int v11;  // [bp-0xc]
    char v12;  // [bp-0x8], Other Possible Types: unsigned int
    char v13;  // [bp-0x4]

    v12 = 4294967295;
    v11 = sub_10369e80;
    v17 = _ccall(v14, v15, (unsigned int)v16, 0);
    v10 = *((int *)v17);
    v9 = v18;
    v8 = g_1038e180 ^ &v13;
    v3 = v19;
    v2 = v20;
    v1 = v21;
    v0 = v8;
    v22 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int **)v22) = &v10;
    v9 = &v0;
    if (a1 == 1)
    {
        sub_10350ad0(&g_103a22a8, 0, 36);
        g_103a22c4 = a0;
        g_103a2234 = g_103a22c4;
        g_103a22a8 = 2;
        sub_1033de00(a0, 2);
        if (((g_1038c7f4 ^ g_1038c834 ^ g_1038c808) & 0x40000))
        {
            v6 = g_1038f8e4;
            sub_10350ad0(&v7, 0, 63);
            if (g_1038b068("INITIALIZEDLLADDR", &v6, 64))
                g_103a24d8 = sub_10312960(&v6);
            sub_10353127(&v6, "%u", sub_1031e0a0);
            g_1038b064("INITIALIZEDLLADDR", &v6);
        }
        else
        {
            sub_1031e0a0();
        }
    }
    else if (a1)
    {
        v4 = 1;
        if (g_103a22c8)
        {
            v12 = 4;
            v4 = _start(a0, a1, a2);
            v12 = 4294967295;
        }
    }
    else if (((g_1038c7f4 ^ g_1038c834 ^ g_1038c808) & 0x40000))
    {
        g_1038b064("INITIALIZEDLLADDR", 0);
    }
    else
    {
        v12 = 0;
        v5 = 1;
        if (g_103a22c8)
        {
            v12 = 1;
            v5 = _start(a0, a1, a2);
            v12 = 0;
        }
        sub_1031e070();
    }
    v23 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int *)v23) = v10;
    return sub_10351225();
}
```

## `sub_1031282c` `0x1031282c`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1031282c(void)
{
    sub_10312838();
    return;
}
```

## `sub_10312838` `0x10312838`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10312838(void)
{
}
```

## `sub_10312878` `0x10312878`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10312878(void)
{
    sub_103128e4();
    return;
}
```

## `sub_103128ac` `0x103128ac`

_13 bytes. (leaf/helper — see body)_

```c
extern char g_103128c0;

int sub_103128ac(void)
{
    unsigned int v1;  // [bp+0x100000]

    v1 = 0;
    return &g_103128c0;
}
```

## `sub_103128ca` `0x103128ca`

_20 bytes. (leaf/helper — see body)_

```c
int sub_103128ca(void)
{
    unsigned int v1;  // [bp+0xfffa0]
    unsigned int v2;  // [bp+0x100000]

    v1 = 0;
    v2 = 4294967295;
    return sub_103128ed;
}
```

## `sub_103128de` `0x103128de`

_6 bytes. (leaf/helper — see body)_

```c
int sub_103128de(void)
{
    return sub_103128e4;
}
```

## `sub_103128e4` `0x103128e4`

_11 bytes. (leaf/helper — see body)_

```c
void sub_103128e4(void)
{
    unsigned int v1;  // [bp+0x100000]

    v1 = 4294967295;
}
```

## `sub_103128ed` `0x103128ed`

_5 bytes. (leaf/helper — see body)_

```c
int sub_103128ed(void)
{
}
```

## `sub_10312922` `0x10312922`

_13 bytes. (leaf/helper — see body)_

```c
extern char g_10312936;

int sub_10312922(void)
{
    unsigned int v1;  // [bp+0x100000]

    v1 = 4294967295;
    return &g_10312936;
}
```

## `sub_10312960` `0x10312960`

_83 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10312960(void)
{
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // fs
    unsigned long v13;  // 4147
    unsigned int v14;  // ecx
    unsigned long v15;  // 4169
    unsigned int v16;  // eax
    unsigned long v17;  // 4119
    unsigned int v0;  // [bp-0x2c]
    int v1;  // [bp-0x28]
    int v2;  // [bp-0x24]
    int v3;  // [bp-0x20]
    char *v4;  // [bp-0x14], Other Possible Types: unsigned int
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]
    char v8;  // [bp-0x4]
    unsigned int v9;  // [bp+0x4]

    v7 = 4294967295;
    v6 = sub_10369eb0;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v5 = *((int *)v13);
    v4 = v14;
    v0 = g_1038e180 ^ &v8;
    v15 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v15) = &v5;
    v4 = &v0;
    v7 = 0;
    v16 = sub_10312a00(&v9, g_1038e180 ^ &v8, v1, v2, v3);
    v17 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v17) = v5;
    return v16;
}
```

## `sub_103129a1` `0x103129a1`

_20 bytes. (leaf/helper — see body)_

```c
int sub_103129a1(void)
{
    unsigned int v1;  // [bp+0xffff0]
    unsigned int v2;  // [bp+0x100000]

    v1 = 0;
    v2 = 4294967295;
    return sub_103129e5;
}
```

## `sub_103129b5` `0x103129b5`

_6 bytes. (leaf/helper — see body)_

```c
int sub_103129b5(void)
{
    return sub_103129d5;
}
```

## `sub_103129bb` `0x103129bb`

_20 bytes. (leaf/helper — see body)_

```c
int sub_103129bb(void)
{
    unsigned int v1;  // [bp+0xfffec]
    unsigned int v2;  // [bp+0x100000]

    v1 = 0;
    v2 = 4294967295;
    return sub_103129de;
}
```

## `sub_103129cf` `0x103129cf`

_6 bytes. (leaf/helper — see body)_

```c
int sub_103129cf(void)
{
    return sub_103129d5;
}
```

## `sub_103129d5` `0x103129d5`

_11 bytes. (leaf/helper — see body)_

```c
void sub_103129d5(void)
{
    unsigned int v1;  // [bp+0x100000]

    v1 = 4294967295;
}
```

## `sub_103129de` `0x103129de`

_5 bytes. (leaf/helper — see body)_

```c
int sub_103129de(void)
{
}
```

## `sub_103129e5` `0x103129e5`

_3 bytes. (leaf/helper — see body)_

```c
int sub_103129e5(void)
{
}
```

## `sub_10312a00` `0x10312a00`

_42 bytes. (leaf/helper — see body)_

```c
int sub_10312a00(int *a0)
{
    char v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v1 = 1;
    sub_10334530();
    return sub_10312a30(*(a0), &v0, 1);
}
```

## `sub_10312a30` `0x10312a30`

_222 bytes. (leaf/helper — see body)_

```c
extern int g_1038c350;
extern int g_1038c360;
extern unsigned int g_1038e180;

unsigned int sub_10312a30(int a0, int a1, unsigned int a2)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4145
    unsigned long v13;  // 4159
    unsigned int v14;  // eax
    unsigned long v15;  // 4113
    int v0;  // [bp-0x80]
    int v1;  // [bp-0x7c]
    unsigned int v2;  // [bp-0x78]
    unsigned int v3;  // [bp-0x60]
    char v4;  // [bp-0x5c], Other Possible Types: unsigned int
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    char v7;  // [bp-0x8], Other Possible Types: unsigned int
    char v8;  // [bp-0x4]

    v7 = 4294967295;
    v6 = sub_10369ee0;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v5 = *((int *)v12);
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v5;
    sub_103133c0(a1, a1 + a2, g_1038e180 ^ &v8);
    v7 = 0;
    if ((char)sub_10313690(a0) && (char)sub_103136e0(&v4))
    {
        v3 = v4;
        v7 = 4294967295;
        sub_10312c20();
        v14 = v3;
    }
    else
    {
        v1 = sub_10312b10(&g_1038c350, &g_1038c360);
        v0 = v1;
        v7 = 1;
        sub_103139f0(v0);
        v7 = 0;
        sub_10312b90();
        v2 = 0;
        v7 = 4294967295;
        sub_10312c20();
        v14 = v2;
    }
    v15 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v15) = v5;
    return v14;
}
```

## `sub_10312b10` `0x10312b10`

_112 bytes. refs "bad cast"_

```c
extern unsigned int g_1038e180;
extern char g_1038f968;

unsigned int [5] sub_10312b10(unsigned int *idx, unsigned int a1, unsigned int a2)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4137
    unsigned int v8;  // eax
    unsigned long v9;  // 4153
    unsigned long v10;  // 4152
    unsigned int v0[5];  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v8 = *((int *)v7);
    v1 = *((int *)v7);
    v0 = idx;
    v9 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v9) = &v1;
    sub_103532f5("bad cast", g_1038e180 ^ &v2, idx, v8, sub_10369f08, -1, &v3);
    *(idx) = &g_1038f968;
    idx[3] = a1;
    idx[4] = a2;
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v10) = v8;
    return idx;
}
```

## `sub_10312b80` `0x10312b80`

_16 bytes. (leaf/helper — see body)_

```c
int sub_10312b80(unsigned int a0)
{
    return "bad lexical cast: source type value could not be interpreted as target";
}
```

## `sub_10312b90` `0x10312b90`

_84 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038f968;

unsigned int sub_10312b90(int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4139
    unsigned int v10;  // eax
    unsigned long v11;  // 4155
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v2 = 4294967295;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v10 = *((int *)v9);
    v1 = *((int *)v9);
    v0 = a0;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v1;
    *((char **)a0) = &g_1038f968;
    v2 = 0;
    v12 = sub_10353326(g_1038e180 ^ &v3, a0, v10, sub_10369f38, -1, &v4);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v10;
    return v12;
}
```

## `sub_10312bf0` `0x10312bf0`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10312bf0(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_10312b90(v0);
    if (((char)a1 & 1))
        sub_10350abd(v0);
    return v0;
}
```

## `sub_10312c20` `0x10312c20`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10312c20(int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4137
    unsigned int v10;  // eax
    unsigned long v11;  // 4153
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v2 = 4294967295;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v10 = *((int *)v9);
    v1 = *((int *)v9);
    v0 = a0;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v1;
    v2 = 0;
    v12 = sub_10312c70(g_1038e180 ^ &v3, a0, v10, sub_10369f68, -1, &v4);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v10;
    return v12;
}
```

## `sub_10312c70` `0x10312c70`

_132 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[56];
    unsigned int field_38;
} struct_0;

extern unsigned int g_1038e180;
extern char g_1038f9cc;

unsigned int sub_10312c70(struct_0 *a0)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4198
    unsigned long v13;  // 4202
    unsigned int v14;  // eax
    unsigned long v15;  // 4113
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_10369f9b;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v4 = *((int *)v12);
    v0 = g_1038e180 ^ &v7;
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v4;
    *((char **)&a0->padding_0[0]) = &g_1038f9cc;
    v6 = 0;
    v2 = a0->field_38;
    v3 = v2;
    if (v3)
        v1 = sub_10313090(1);
    else
        v1 = 0;
    v6 = 4294967295;
    v14 = sub_1034ff0d();
    v15 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v15) = v4;
    return v14;
}
```

## `sub_10312d00` `0x10312d00`

_18 bytes. (leaf/helper — see body)_

```c
void sub_10312d00(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1032fd20(a0, &v1);
    return;
}
```

