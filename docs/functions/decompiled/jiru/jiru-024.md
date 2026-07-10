# elfbot.dll decompiled — jiru 0x1031ddea..0x1031fb60

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1031ddea` `0x1031ddea`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1031ddea(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1031ddfe` `0x1031ddfe`

_14 bytes. (leaf/helper — see body)_

```c
int sub_1031ddfe(void)
{
}
```

## `sub_1031de02` `0x1031de02`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1031de02(void)
{
}
```

## `sub_1031de04` `0x1031de04`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1031de04(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_1031de58` `0x1031de58`

_72 bytes. refs "(Error code %d)"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b07c;
extern unsigned int g_103a24e8;
extern int g_103a24f0;

int sub_1031de58(void)
{
    char v1;  // al

    if (!v1)
    {
        g_103a24e8 = 6;
        sub_10353127(&g_103a24f0, "(Error code %d)", g_1038b07c());
    }
    else
    {
        sub_1031df50(0);
    }
}
```

## `sub_1031de8c` `0x1031de8c`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1031de8c(void)
{
}
```

## `sub_1031df50` `0x1031df50`

_74 bytes. refs "KERNEL32.DLL", "RegisterServiceProcess"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b078;
extern struct_0 *g_1038b080;
extern unsigned int g_103a2630;
extern struct_0 *g_103a2634;

int sub_1031df50(char a0)
{
    unsigned int v0;  // eax

    if (!g_103a2634)
    {
        g_103a2630 = g_1038b080("KERNEL32.DLL");
        v0 = g_1038b078(g_103a2630, "RegisterServiceProcess");
        g_103a2634 = v0;
    }
    if (g_103a2634)
        v0 = g_103a2634(0, a0);
    return v0;
}
```

## `sub_1031dfa0` `0x1031dfa0`

_10 bytes. (leaf/helper — see body)_

```c
int sub_1031dfa0(void)
{
    return sub_1031d680();
}
```

## `sub_1031dfb0` `0x1031dfb0`

_182 bytes. refs "Kernel32", "IsDebuggerPresent", "%X:DAF"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b078;
extern struct_0 *g_1038b080;
extern struct_0 *g_1038b098;
extern struct_0 *g_1038b1c8;
extern unsigned int g_1038e180;
extern char g_103a22a8;
extern struct_0 *g_103a22d0;

int sub_1031dfb0(void)
{
    char v0;  // [bp-0x114]
    unsigned int v1;  // [bp-0x14]
    unsigned int *v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v1 = g_1038e180 ^ &v5;
    v4 = g_1038b080("Kernel32");
    if (v4)
    {
        v2 = g_1038b078(v4, "IsDebuggerPresent");
        if (v2 && v2())
        {
            sub_10353127(&v0, "%X:DAF", g_1038b1c8());
            g_1038b098(0, 0, &v0);
        }
    }
    sub_103540b9(sub_1031c040);
    v3 = sub_1031c400();
    sub_103540b9(0);
    if (v3 == 1)
        g_103a22d0(&g_103a22a8);
    return sub_10351225();
}
```

## `sub_1031e070` `0x1031e070`

_40 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_103a22cc;
extern unsigned int g_103a24dc;
extern struct_0 *g_103a24e0;

int sub_1031e070(void)
{
    char v0;  // [bp+0x0]

    sub_103540b9(sub_1031c040, &v0);
    g_103a22cc(&v0);
    return g_103a24e0(g_103a24dc, 0, 0);
}
```

## `sub_1031e0a0` `0x1031e0a0`

_290 bytes. refs "INITIALIZEDLLADDR"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b064;
extern struct_0 *g_1038b0a0;
extern struct_0 *g_1038b30c;
extern unsigned int g_1038e180;
extern int g_103a2234;
extern unsigned int g_103a22c8;
extern struct_0 *g_103a24d8;
extern int g_103a24f0;

int sub_1031e0a0(void)
{
    char v0;  // [bp-0x114]
    unsigned int v1;  // [bp-0x10]
    unsigned int *v2;  // [bp-0xc]
    int v3;  // [bp-0x8], Other Possible Types: unsigned int
    char v4;  // [bp-0x4]

    v1 = g_1038e180 ^ &v4;
    g_1038b064("INITIALIZEDLLADDR", 0);
    if (!g_103a24d8 || (v2 = (unsigned int *)g_103a24d8, g_103a24d8 = (struct_0 *)0, v2()))
    {
        v3 = sub_1031dfb0();
        if (v3 == 1)
        {
            if (g_103a22c8)
            {
                v3 = _start(g_103a2234, 1, &g_103a24f0);
                if (!v3)
                    sub_1031e070();
            }
        }
        else
        {
            if (!v3)
            {
                sub_10352cb0(&v0, sub_1031c010());
                if (sub_10352f20(sub_1031c030()))
                {
                    sub_10352cc0(&v0, "\n");
                    sub_10352cc0(&v0, sub_1031c030());
                }
                g_1038b30c(0, &v0, 0, 262160);
            }
            else
            {
                g_1038b0a0(3);
            }
        }
    }
    return sub_10351225();
}
```

## `sub_1031e129` `0x1031e129`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1031e129(void)
{
    sub_1031e135();
    return;
}
```

## `sub_1031e135` `0x1031e135`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1031e135(void)
{
    sub_1031e13e();
    return;
}
```

## `sub_1031e13e` `0x1031e13e`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1031e13e(void)
{
}
```

## `sub_1031e1b0` `0x1031e1b0`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1031e1b0(void)
{
}
```

## `sub_1031e1d0` `0x1031e1d0`

_114 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1031e1d0(int a0, int a1)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4138
    unsigned int v9;  // eax
    unsigned long v10;  // 4154
    unsigned long v11;  // 4123
    int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x8], Other Possible Types: unsigned int
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v9 = *((int *)v8);
    v1 = *((int *)v8);
    v0 = a0;
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v10) = &v1;
    sub_1031e640(a1, g_1038e180 ^ &v3, a0, v9, sub_1036b78e, -1, &v4);
    v2 = 0;
    sub_10319ff0(a0 + 32);
    v2 = 1;
    sub_1031a090(a0 + 64);
    v11 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v11) = v9;
    return a0;
}
```

## `sub_1031e250` `0x1031e250`

_114 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_1031e250(int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4140
    unsigned long v11;  // 4156
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036b7d7;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    v4 = 2;
    v4 = 1;
    sub_10319f00(v1 + 260);
    v4 = 0;
    sub_10319f00(v1 + 164);
    v4 = 4294967295;
    v12 = sub_10319f00(v1 + 0x44);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_1031e2d0` `0x1031e2d0`

_63 bytes. (leaf/helper — see body)_

```c
int sub_1031e2d0(void* a0)
{
    unsigned int v6[2];  // eax
    int v7[2];  // eax
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    char v2;  // [bp-0x1c]
    char v3;  // [bp-0x14]
    char v4;  // [bp-0xc]

    v6 = sub_1031b790(a0, &v4);
    v1 = v6[1];
    v0 = v6[0];
    v7 = sub_1031b6e0(a0, &v3);
    return sub_1031e3f0(&v2, v7[0], v7[1]);
}
```

## `sub_1031e310` `0x1031e310`

_50 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

int sub_1031e310(struct_0 *a0, char a1)
{
    int v4[2];  // eax
    unsigned int v0;  // [bp-0x1c]
    char v1;  // [bp-0x14]
    char v2;  // [bp-0xc]

    *((char *)&v0) = a1;
    v4 = sub_1031b790(a0, &v2);
    return sub_1031e370(&v1, v4[0], v4[1]);
}
```

## `sub_1031e350` `0x1031e350`

_29 bytes. (leaf/helper — see body)_

```c
int sub_1031e350(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return -(0 < (sub_103315c0(a0, &v1) & 0xff)) + 1;
}
```

## `sub_1031e370` `0x1031e370`

_125 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

int sub_1031e370(struct_0 *a0, int a1, unsigned int a2, unsigned int a3, char a4)
{
    unsigned int v7[2];  // eax
    unsigned int v0;  // [bp-0x34]
    unsigned int v1;  // [bp-0x30]
    char v2;  // [bp-0x28]
    char v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v7 = sub_1031b6e0(a0, &v3);
    v4 = v7[0];
    v5 = v7[1];
    v1 = v5;
    v0 = v4;
    v6 = sub_1031b9f0(a2, a3);
    sub_1031e4a0(v6, 1, _INSERT(v6, 0, a4));
    sub_1031b6e0(a0, &v2);
    sub_1031e560(a1, v6, v6);
    return a1;
}
```

## `sub_1031e3f0` `0x1031e3f0`

_165 bytes. (leaf/helper — see body)_

```c
int sub_1031e3f0(unsigned int a0, int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5)
{
    unsigned int v10[2];  // eax
    unsigned int v0;  // [bp-0x3c]
    unsigned int v1;  // [bp-0x38]
    unsigned int v2;  // [bp-0x28]
    unsigned int v3;  // [bp-0x24]
    unsigned int v4;  // [bp-0x20]
    unsigned int v5;  // [bp-0x1c]
    char v6;  // [bp-0x18]
    unsigned int v7;  // [bp-0x10]
    unsigned int v8;  // [bp-0xc]
    unsigned int v9;  // [bp-0x8]

    v10 = sub_1031b6e0(a0, &v6);
    v7 = v10[0];
    v8 = v10[1];
    v4 = a2;
    v5 = a3;
    v1 = v8;
    v0 = v7;
    v9 = sub_1031b9f0(v4, v5);
    v2 = a2;
    v3 = a3;
    v1 = v3;
    v0 = v2;
    sub_103148c0(a0, v9, sub_1031b9f0(a4, a5));
    sub_1031b710(a1, &sub_10314a50(a0)->padding_0[v9], a0);
    return a1;
}
```

## `sub_1031e4a0` `0x1031e4a0`

_184 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
    unsigned int field_18;
} struct_0;

extern unsigned int g_1038fb14;

struct_0 * sub_1031e4a0(struct_0 *a0, unsigned int a1, unsigned int a2, char a3)
{
    struct_0 *v2;  // eax
    struct_0 *v3;  // eax
    unsigned int v4;  // eax
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0x8]

    if (a0->field_14 < a1)
    {
        sub_103503dd(a0);
    }
    else if (g_1038fb14 - a0->field_14 <= a2)
    {
        sub_1035039e();
    }
    else if (a2 > 0)
    {
        v1 = a0->field_14 + a2;
        if (!(char)sub_103149b0(a0, v1, 0))
            return a0;
        v2 = sub_10314a50(a0);
        v3 = sub_10314a50(a0);
        v4 = _INSERT(sub_103159d0(&v3->padding_0[a1 + a2], a0->field_18 - a1 - a2, &v2->padding_0[a1], a0->field_14 - a1) CONCAT 0, 0, a3);
        v0 = v4;
        sub_10317170(a0, a1, a2);
        sub_10314960(a0, v1);
        return a0;
    }
    else
    {
        return a0;
    }
}
```

## `sub_1031e560` `0x1031e560`

_57 bytes. (leaf/helper — see body)_

```c
unsigned int [2] sub_1031e560(int *a0, unsigned int *a1, int a2)
{
    unsigned int v1[2];  // eax
    unsigned int v2;  // edx
    char v0;  // [bp+0x0]

    v1 = sub_1031e5a0(a2, a0, *(a0), a0[1], &v0);
    v2 = v1[1];
    *(a1) = v1[0];
    a1[1] = v2;
    return a1;
}
```

## `sub_1031e5a0` `0x1031e5a0`

_28 bytes. (leaf/helper — see body)_

```c
int sub_1031e5a0(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1031e5c0(a1, a0, &v1);
    return a0;
}
```

## `sub_1031e5c0` `0x1031e5c0`

_113 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
    unsigned int field_4;
} struct_1;

typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

struct_1 * sub_1031e5c0(struct_1 *a0, unsigned int a1)
{
    struct_0 *v1;  // eax
    struct_0 *v2;  // eax
    struct_1 *idx;  // [bp-0x8]

    idx = a0;
    idx = a0;
    if (idx->field_0 != 0xfffffffe)
    {
        if (!idx->field_0)
            sub_10353616();
        v1 = sub_10314a50(idx->field_0);
        if (idx->field_4 + a1 > &v1->padding_0[idx->field_0->field_14] || (v2 = (struct_0 *)sub_10314a50(idx->field_0), idx->field_4 + a1 < sub_10314a50(idx->field_0)))
            sub_10353616();
    }
    idx->field_4 = idx->field_4 + a1;
    return idx;
}
```

## `sub_1031e640` `0x1031e640`

_108 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_1031e640(unsigned int a0, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4139
    unsigned long v10;  // 4153
    unsigned long v12;  // 4120
    unsigned int v0;  // [bp-0x1c]
    char v1;  // [bp-0x11]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036b80b;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_1031a280(a0 + 4);
    v4 = 0;
    v1 = 0;
    sub_1031e6b0(a1, 1, _INSERT(0, 0, v1));
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v2;
    return a0;
}
```

## `sub_1031e6b0` `0x1031e6b0`

_46 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_1031e6b0(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v1 = a0;
    v1 = a0;
    v0 = a1;
    return sub_1031ac50(v1, sub_1031e6e0(sub_1031a280(v1 + 4)));
}
```

## `sub_1031e6e0` `0x1031e6e0`

_124 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_1031e6e0(unsigned int a0, int a1)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4139
    unsigned long v11;  // 4153
    unsigned long v12;  // 4124
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036b841;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v0 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    v2 = sub_1031acf0(28, a0);
    v5 = 0;
    if (v2)
        v1 = sub_1031e760(a1);
    else
        v1 = 0;
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v3;
    return 2;
}
```

## `sub_1031e760` `0x1031e760`

_61 bytes. (leaf/helper — see body)_

```c
extern int g_1039011c;

int sub_1031e760(unsigned int a0, int a1)
{
    unsigned int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1031e860(a1, a0, &v1);
    sub_1031a3c0(a0, 0, 0);
    sub_1031e7a0(a1, 0, g_1039011c);
    return a0;
}
```

## `sub_1031e7a0` `0x1031e7a0`

_185 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

extern int g_1039011c;

struct_0 * sub_1031e7a0(struct_0 *a0, struct_0 *a1, int a2, unsigned int a3)
{
    struct_0 *v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x8]

    if (sub_1031e920(a0) < a2)
        sub_103503dd();
    v0 = sub_1031e920() - a2;
    if (a3 < v0)
        v0 = a3;
    if (a0 == a1)
    {
        sub_1031e880(a2 + v0, g_1039011c);
        sub_1031e880(0, a2);
        return a0;
    }
    if (!(char)sub_1031e940(v0, 0))
        return a0;
    v1 = sub_1031a4a0(a1);
    v2 = sub_1031a4a0(a0);
    sub_1031a9b0(v2, a0->field_18, &v1->padding_0[2 * a2], v0);
    sub_1031a440(a0, v0);
    return a0;
}
```

## `sub_1031e860` `0x1031e860`

_28 bytes. (leaf/helper — see body)_

```c
int sub_1031e860(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1033f400(a1, a0, &v1);
    return a0;
}
```

## `sub_1031e880` `0x1031e880`

_157 bytes. (leaf/helper — see body)_

```c
unsigned int [7] sub_1031e880(unsigned int *idx, unsigned int a1, unsigned int a2)
{
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0x8]

    if (idx[5] < a1)
        sub_103503dd(idx);
    if (idx[5] - a1 < a2)
        a2 = idx[5] - a1;
    if (a2 <= 0)
        return idx;
    v2 = idx[5] - a1 - a2;
    v1 = &sub_1031a4a0(idx)->padding_0[2 * a1 + 2 * a2];
    v0 = idx[6] - a1;
    sub_1031ebf0(&sub_1031a4a0(idx)->padding_0[2 * a1]);
    v3 = idx[5] - a2;
    sub_1031a440(idx, v3);
    return idx;
}
```

## `sub_1031e920` `0x1031e920`

_17 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

int sub_1031e920(struct_0 *a0)
{
    return a0->field_14;
}
```

## `sub_1031e940` `0x1031e940`

_148 bytes. (leaf/helper — see body)_

```c
int sub_1031e940(void* a0, int a1, char a2)
{
    int v0;  // [bp-0xc]

    if (sub_1031e9e0() < a1)
        sub_1035039e();
    if ((int)a0[24] < a1)
    {
        sub_1031ea20(a1, (int)a0[20]);
    }
    else if (a2 && a1 < 8)
    {
        v0 = (a1 < (int)a0[20] ? a1 : (int)a0[20]);
        sub_1031a3c0(a0, 1, v0);
    }
    else if (!a1)
    {
        sub_1031a440(a0, 0);
    }
    return -(-(0 < a1));
}
```

## `sub_1031e9e0` `0x1031e9e0`

_51 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1031e9e0(unsigned int a0)
{
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v1 = a0;
    v2 = sub_1031ebc0();
    v0 = (v2 <= 1 ? 1 : v2 - 1);
    return v0;
}
```

## `sub_1031ea20` `0x1031ea20`

_285 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1031ea20(void* idx, unsigned int a1, unsigned int a2)
{
    unsigned long v11;  // ldt
    unsigned long v12;  // gdt
    int v21;  // eax
    unsigned long v22;  // 4119
    unsigned short v13;  // fs
    unsigned long v14;  // 4150
    unsigned int v15;  // ebx
    unsigned int v16;  // esi
    unsigned int v17;  // edi
    unsigned long v18;  // 4172
    unsigned int v19;  // eax
    unsigned int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x2c]
    unsigned int v2;  // [bp-0x28]
    unsigned int v3;  // [bp-0x24]
    unsigned int v4;  // [bp-0x1c]
    int v5;  // [bp-0x18], Other Possible Types: unsigned int
    char *v6;  // [bp-0x14], Other Possible Types: void*
    unsigned int v7;  // [bp-0x10]
    unsigned int v8;  // [bp-0xc]
    unsigned int v9;  // [bp-0x8]
    char v10;  // [bp-0x4]

    v9 = 4294967295;
    v8 = sub_1036b860;
    v14 = _ccall(v11, v12, (unsigned int)v13, 0);
    v7 = *((int *)v14);
    v6 = idx;
    v3 = v15;
    v2 = v16;
    v1 = v17;
    v0 = g_1038e180 ^ &v10;
    v18 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int **)v18) = &v7;
    v6 = &v0;
    v4 = a1 | 7;
    if (sub_1031e9e0(idx) < v4)
    {
        v4 = a1;
    }
    else if ((unsigned int)(v4 / 3) < (int)idx[24] >> 1)
    {
        v19 = sub_1031e9e0(idx);
        if ((int)idx[24] <= v19 - ((int)idx[24] >> 1))
            v4 = ((int)idx[24] >> 1) + (int)idx[24];
    }
    v5 = 0;
    v9 = 0;
    v5 = sub_1031eba0(v4 + 1);
    v9 = 4294967295;
    if (a2 > 0)
        sub_1031a9b0(v5, v4 + 1, sub_1031a4a0(idx), a2);
    sub_1031a3c0(idx, 1, 0);
    *((int *)&idx[4]) = v5;
    *((unsigned int *)&idx[24]) = v4;
    v21 = sub_1031a440(idx, a2);
    v22 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int *)v22) = v7;
    return v21;
}
```

## `sub_1031ead2` `0x1031ead2`

_19 bytes. (leaf/helper — see body)_

```c
void sub_1031ead2(void)
{
    char v0;  // [bp+0x0]
    unsigned int v2;  // [bp+0xfffec]
    char *v3;  // [bp+0xffff4]
    char v4;  // [bp+0x100000]
    unsigned int v5;  // [bp+0x10000c]

    v3 = &v0;
    v2 = v5;
    v4 = 2;
    sub_1031eae5();
    return;
}
```

## `sub_1031eae5` `0x1031eae5`

_34 bytes. (leaf/helper — see body)_

```c
extern char g_1031eb30;

int sub_1031eae5(void)
{
    int v3;  // edx
    unsigned int v1;  // [bp+0xffff0]
    unsigned int v2;  // [bp+0x100000]

    v1 = sub_1031eba0(v3);
    v2 = 1;
    v2 = 1;
    return &g_1031eb30;
}
```

## `sub_1031eaf3` `0x1031eaf3`

_34 bytes. (leaf/helper — see body)_

```c
extern char g_1031eb1c;

int sub_1031eaf3(void)
{
    unsigned int *v1;  // [bp+0xfffe8]
    unsigned int v2;  // [bp+0x100000]

    sub_1031a3c0(v1, 1, 0);
    sub_103533ea(0, 0);
    v2 = 1;
    return &g_1031eb1c;
}
```

## `sub_1031eba0` `0x1031eba0`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1031eba0(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_1031ec20(a1, 0, a0, &v1);
}
```

## `sub_1031ebc0` `0x1031ebc0`

_44 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1031ebc0(void)
{
    unsigned int v4;  // ecx
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v1 = v4;
    v2 = 2147483647;
    v0 = (v2 <= 0 ? 1 : v2);
    return v0;
}
```

## `sub_1031ebf0` `0x1031ebf0`

_44 bytes. (leaf/helper — see body)_

```c
char sub_1031ebf0(int a0, int a1, int a2, int a3)
{
    int v2;  // ecx
    int v3;  // eax
    char v0;  // [bp-0x5]
    char v1;  // [bp+0x0]

    v0 = sub_10337970(v2, &v1);
    v3 = _INSERT(v0, 0, v0);
    return sub_1031ec70(a0, a1, a2, a3, v3);
}
```

## `sub_1031ec20` `0x1031ec20`

_76 bytes. (leaf/helper — see body)_

```c
extern int g_10399bb4;

int sub_1031ec20(unsigned int a0)
{
    unsigned int v0;  // [bp-0x14]
    char v1;  // [bp-0x10]

    if (a0 <= 0)
    {
        a0 = 0;
    }
    else if ((unsigned int)(4294967295 / a0) < 2)
    {
        v0 = 0;
        sub_10315880(&v1);
        sub_103533ea(&v1, &g_10399bb4);
    }
    return sub_10350a53(a0 * 2);
}
```

## `sub_1031ec70` `0x1031ec70`

_29 bytes. (leaf/helper — see body)_

```c
int sub_1031ec70(int a0, int a1, int a2, int a3)
{
    char v0;  // [bp+0x0]

    return sub_1031ec90(a0, a1, a2, a3, &v0);
}
```

## `sub_1031ec90` `0x1031ec90`

_32 bytes. (leaf/helper — see body)_

```c
int sub_1031ec90(int a0, int a1, int a2, int a3)
{
    char v0;  // [bp+0x0]

    sub_1031ecb0(a0, a1, a2, a3, &v0);
    return a0;
}
```

## `sub_1031ecb0` `0x1031ecb0`

_33 bytes. (leaf/helper — see body)_

```c
int sub_1031ecb0(int a0, unsigned int a1, int a2, unsigned int a3)
{
    char v0;  // [bp+0x0]

    return sub_10353626(a0, a1 * 2, a2, a3 * 2, &v0);
}
```

## `sub_1031ece0` `0x1031ece0`

_133 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b07c;
extern struct_0 *g_1038b2ec;
extern struct_0 *g_1038b2f0;
extern struct_0 *g_1038b2f4;
extern unsigned int g_103a2234;

unsigned int sub_1031ece0(int a0)
{
    int v0;  // [bp-0x14]
    int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v1 = sub_1031edd0(a0);
    v3 = 0;
    v2 = 0;
    if (!a0)
    {
        v3 = g_1038b2ec(g_103a2234, v1, 0, sub_1031ed70, 0);
        v2 = g_1038b07c(g_103a2234, v1, 0, sub_1031ed70, 0);
    }
    v0 = v1;
    sub_10350eb5(v0);
    g_1038b2f0(v3, 5);
    g_1038b2f4(v3);
    return v3;
}
```

## `sub_1031ed70` `0x1031ed70`

_83 bytes. refs "Loading..."_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b2e4;
extern struct_0 *g_1038b2e8;
extern char g_103a23d8;

unsigned int sub_1031ed70(unsigned int a0, unsigned int a1)
{
    unsigned int v1;  // eax
    unsigned int v0;  // [bp-0x8]

    v0 = "Loading...";
    if (a1 != 272)
        return 0;
    g_1038b2e4(a0, &g_103a23d8);
    v1 = g_1038b2e8(a0, 1002, v0);
    g_1038b2e4(v1);
    return 0;
}
```

## `sub_1031edd0` `0x1031edd0`

_574 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c8a0;

void* sub_1031edd0(unsigned int a0)
{
    void* v0;  // [bp-0x18]
    void* v1;  // [bp-0x14]
    void* v2;  // [bp-0x10]
    void* iter;  // [bp-0xc]
    unsigned int idx;  // [bp-0x8]

    v1 = sub_1034fef0(0x400);
    v2 = v1;
    iter = v2;
    if (a0)
    {
        v0 = v2;
        sub_10350eb5(v0);
        return NULL;
    }
    *((unsigned int *)iter) = 2428504772;
    iter += 4;
    *((unsigned int *)iter) = 128;
    iter += 4;
    *((unsigned short *)iter) = 1;
    iter += 2;
    *((unsigned short *)iter) = 0;
    iter += 2;
    *((unsigned short *)iter) = 0;
    iter += 2;
    *((unsigned short *)iter) = 123;
    iter += 2;
    *((unsigned short *)iter) = 0x22;
    iter += 2;
    *((unsigned short *)iter) = 0;
    iter += 2;
    *((unsigned short *)iter) = 0;
    iter += 2;
    *((unsigned short *)iter) = 0;
    iter += 2;
    *((unsigned short *)iter) = 8;
    iter += 2;
    for (idx = 0; *((short *)(g_1038c8a0 + idx * 2)); idx += 1)
    {
        *((short *)iter) = *((short *)(g_1038c8a0 + idx * 2));
        iter += 2;
    }
    *((unsigned short *)iter) = 0;
    for (iter += 2; (unsigned int)((unsigned long long)iter % 4); iter += 1)
    {
        *((char *)iter) = 0;
    }
    *((unsigned int *)iter) = 1350570625;
    iter += 4;
    *((unsigned int *)iter) = 0;
    iter += 4;
    *((unsigned short *)iter) = 0;
    iter += 2;
    *((unsigned short *)iter) = 0;
    iter += 2;
    *((unsigned short *)iter) = 123;
    iter += 2;
    *((unsigned short *)iter) = 0x22;
    iter += 2;
    *((unsigned short *)iter) = 1002;
    iter += 2;
    *((unsigned short *)iter) = 65535;
    iter += 2;
    *((unsigned short *)iter) = 130;
    iter += 2;
    *((unsigned short *)iter) = 0;
    iter += 2;
    *((unsigned short *)iter) = 0;
    iter += 2;
    return v2;
}
```

## `sub_1031f010` `0x1031f010`

_120 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b0a4;
extern struct_0 *g_1038b1b4;
extern struct_0 *g_1038b294;
extern struct_0 *g_1038b298;
extern struct_0 *g_1038b308;
extern unsigned int g_103a2664;
extern char g_103a2674;

unsigned int sub_1031f010(void)
{
    unsigned int v3;  // ecx
    unsigned int v4;  // eax
    unsigned int v5;  // eax
    unsigned int v6;  // eax
    unsigned int v7;  // eax
    int i;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v4 = g_1038b0a4(v3, &v1);
    if (*((int *)&g_103a2674) == v4)
    {
        v5 = g_1038b308(g_103a2664);
        g_103a2664 = 0;
        return v5;
    }
    v6 = g_1038b298(g_103a2664, 1034, 0, 0);
    for (i = 0; i < 20; i += 1)
    {
        v7 = g_1038b294(g_103a2664);
        if (!v7)
            return v7;
        v6 = g_1038b1b4(100);
    }
    return v6;
}
```

## `sub_1031f090` `0x1031f090`

_889 bytes. refs "DISPLAY"_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned short field_c;
    short field_e;
    unsigned int field_10;
    unsigned int field_14;
    unsigned int field_18;
    unsigned int field_1c;
    int field_20;
    unsigned int field_24;
    char field_28;
    char field_29;
    char field_2a;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b00c;
extern struct_1 *g_1038b010;
extern struct_1 *g_1038b014;
extern struct_1 *g_1038b018;
extern struct_1 *g_1038b01c;
extern struct_1 *g_1038b020;
extern unsigned int g_103a266c;

unsigned int sub_1031f090(int a0, unsigned int *a1, unsigned int *a2)
{
    unsigned int v31;  // eax
    struct_0 *v0;  // [bp-0x80]
    unsigned short v1[2];  // [bp-0x7c]
    unsigned short v2[2];  // [bp-0x78]
    struct_0 *v3;  // [bp-0x74]
    struct_0 *idx1;  // [bp-0x70]
    unsigned int v5;  // [bp-0x6c]
    struct_0 *index;  // [bp-0x68]
    unsigned int v7;  // [bp-0x64]
    unsigned short v8[2];  // [bp-0x60]
    char v9;  // [bp-0x5c], Other Possible Types: unsigned short
    unsigned int v10;  // [bp-0x5a]
    unsigned int v11;  // [bp-0x52]
    unsigned int v12;  // [bp-0x4c]
    char v13;  // [bp-0x48]
    unsigned int v14;  // [bp-0x44]
    unsigned int v15;  // [bp-0x40]
    unsigned short v16;  // [bp-0x3c]
    short v17;  // [bp-0x3a]
    unsigned int v18;  // [bp-0x38]
    unsigned int v19;  // [bp-0x34]
    unsigned int v20;  // [bp-0x30]
    unsigned int v21;  // [bp-0x2c]
    int v22;  // [bp-0x28]
    unsigned int v23;  // [bp-0x24]
    struct_0 *idx;  // [bp-0x20]
    unsigned int v25;  // [bp-0x1c]
    int v26;  // [bp-0x18]
    int v27;  // [bp-0x14], Other Possible Types: unsigned int
    unsigned int iter;  // [bp-0x10], Other Possible Types: int
    int v29;  // [bp-0xc], Other Possible Types: unsigned int
    unsigned int v30;  // [bp-0x8]

    iter = a0;
    sub_10350b50(&v9, iter, 14);
    iter += 14;
    if (v9 != 19778)
        return 0;
    sub_10350b50(&v13, iter, 40);
    iter += 40;
    v29 = 40;
    if (!v22)
        v22 = 1 << ((char)v17 & 31);
    if (!v23)
        v23 = 1 << ((char)v17 & 31);
    v29 = (v17 <= 8 ? v29 + (1 << ((char)v17 & 31)) * 4 : v29 + v22 * 2);
    v3 = sub_1034fef0(v29);
    idx = v3;
    idx->field_0 = 40;
    idx->field_4 = v14;
    idx->field_8 = v15;
    idx->field_c = v16;
    idx->field_e = v17;
    idx->field_10 = v18;
    idx->field_14 = v19;
    idx->field_18 = v20;
    idx->field_1c = v21;
    idx->field_20 = v22;
    idx->field_24 = v23;
    if (v17 <= 8)
    {
        v27 = v22 * (unsigned int)((idx->field_0 == 40) + 3);
        sub_10350b50(&idx->field_28, iter, v27);
        iter += v27;
        v31 = v22 * 4 + 8;
        v2 = sub_1034fef0(-((v31 >= 0x20000000 ? 1 : 0) & 1) | v31 * 4);
        v8 = v2;
        v8[0] = 0x300;
        v8[1] = v22;
        if (idx->field_0 == 40)
        {
            index = &idx->field_28;
            for (v7 = 0; v7 < v8[1]; index = &index->field_4)
            {
                *((char *)&v8[1 + v7]) = *((char *)&index->field_0 + 2);
                *((char *)&v8[1 + v7] + 1) = *((char *)&index->field_0 + 1);
                *((char *)&v8[1 + v7 + 1]) = index->field_0;
                *((char *)&v8[1 + v7 + 1] + 1) = 0;
                v7 += 1;
            }
        }
        else
        {
            idx1 = &idx->field_28;
            for (v5 = 0; v5 < v8[1]; idx1 = (char *)&idx1->field_0 + 3)
            {
                *((char *)&v8[1 + v5]) = *((char *)&idx1->field_0 + 2);
                *((char *)&v8[1 + v5] + 1) = *((char *)&idx1->field_0 + 1);
                *((char *)&v8[1 + v5 + 1]) = idx1->field_0;
                *((char *)&v8[1 + v5 + 1] + 1) = 0;
                v5 += 1;
            }
        }
        g_103a266c = g_1038b00c(v8);
        v1 = v8;
        sub_10350eb5(v1);
    }
    v27 = v10 - v11;
    v26 = iter;
    iter += v27;
    v12 = g_1038b010("DISPLAY", 0, 0, 0);
    v30 = 0;
    if (g_103a266c)
    {
        v30 = g_1038b014(v12, g_103a266c, 0);
        g_1038b018(v12);
    }
    v25 = g_1038b01c(v12, &v13, 4, v26, idx, 0);
    if (v30)
        g_1038b014(v12, v30, 0);
    g_1038b020(v12);
    v0 = idx;
    sub_10350eb5(v0);
    if (a1)
        *(a1) = v14;
    if (!a2)
        return v25;
    *(a2) = v15;
    return v25;
}
```

## `sub_1031f410` `0x1031f410`

_81 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a2668;

char sub_1031f410(int a0, char a1, char a2)
{
    int v0;  // [bp-0xc], Other Possible Types: unsigned int
    int v1;  // [bp-0x8], Other Possible Types: unsigned int

    sub_1031f010();
    g_103a2668 = sub_1031f090(a0, &v0, &v1);
    if (!g_103a2668)
        return 0;
    sub_1031f470(v0, v1, _INSERT(0, 0, a1), _INSERT(g_103a2668, 0, a2), 1);
    return 1;
}
```

## `sub_1031f45b` `0x1031f45b`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1031f45b(void)
{
}
```

## `sub_1031f470` `0x1031f470`

_312 bytes. refs "ArBase Bitmap Window", "ArBase Test Bitmap Window"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b02c;
extern struct_0 *g_1038b03c;
extern struct_0 *g_1038b0a4;
extern struct_0 *g_1038b128;
extern struct_0 *g_1038b1b4;
extern unsigned int g_1038e180;
extern unsigned int g_103a2658;
extern unsigned int g_103a265c;
extern char g_103a2670;
extern char g_103a2671;
extern unsigned int g_103a2674;
extern char g_103a269a;

int sub_1031f470(unsigned int a0, unsigned int a1, char a2, char a3, char a4)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4138
    unsigned long v13;  // 4155
    unsigned int v14;  // eax
    unsigned long v15;  // 4114
    unsigned int v0;  // [bp-0x18c]
    unsigned int v1;  // [bp-0x15c]
    char v2;  // [bp-0x4c]
    char v3;  // [bp-0x30]
    int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    char v7;  // [bp-0x8], Other Possible Types: unsigned int
    char v8;  // [bp-0x4]

    v7 = 4294967295;
    v6 = sub_1036b89b;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v5 = *((int *)v12);
    v4 = g_1038e180 ^ &v8;
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v5;
    sub_1031fc10(L"ArBase Bitmap Window", v4);
    v7 = 0;
    sub_1031fc10(L"ArBase Test Bitmap Window");
    v7 = 1;
    g_103a2670 = a3;
    g_103a2671 = a2;
    g_103a2658 = a0;
    g_103a265c = a1;
    if (a4 && !a3)
    {
        g_103a269a = 1;
        v1 = g_1038b03c() + 250;
        v14 = g_1038b02c(0, 0, sub_1031fa90, 0, 0, &g_103a2674);
        g_1038b128(v14);
        while (g_103a269a && g_1038b03c() < v1)
        {
            g_1038b1b4(1);
        }
        v0 = 1;
        v7 = 0;
        sub_1031a3a0(&v2);
        v7 = 4294967295;
        sub_1031a3a0(&v3);
        v15 = _ccall(v9, v10, (unsigned int)v11, 0);
        *((unsigned int *)v15) = v5;
        return sub_10351225();
    }
    g_103a2674 = g_1038b0a4();
    return sub_1031f591();
}
```

## `sub_1031f584` `0x1031f584`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1031f584(void)
{
    sub_1031f591();
    return;
}
```

## `sub_1031f591` `0x1031f591`

_654 bytes. refs "%08X", "LOADINGWINDOW"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b064;
extern struct_0 *g_1038b2d8;
extern struct_0 *g_1038b2dc;
extern struct_0 *g_1038b2e0;
extern struct_0 *g_1038b2f0;
extern struct_0 *g_1038b2f4;
extern struct_0 *g_1038b324;
extern int g_103a2234;
extern int g_103a2658;
extern int g_103a265c;
extern int g_103a2664;
extern char g_103a2670;
extern char g_103a2699;
extern char g_103a269a;
extern int g_103a2ad0;

int sub_1031f591(void)
{
    unsigned int v21;  // eax
    unsigned int v22;  // eax
    int v1;  // [bp+0xffe0c]
    unsigned int v2;  // [bp+0xffe10]
    int v3;  // [bp+0xffe14]
    int v4;  // [bp+0xffe18]
    int i;  // [bp+0xffe80]
    unsigned int v6;  // [bp+0xffe84]
    unsigned int v7;  // [bp+0xffe88]
    unsigned int v8;  // [bp+0xffe8c]
    unsigned int v9;  // [bp+0xffe90]
    int v10;  // [bp+0xffe94]
    unsigned int v11;  // [bp+0xffe98]
    unsigned int v12;  // [bp+0xffe9c]
    unsigned int v13;  // [bp+0xffea0]
    unsigned int v14;  // [bp+0xffea4]
    unsigned int v15;  // [bp+0xffea8]
    int v16;  // [bp+0xffeb0]
    int v17;  // [bp+0xffeb4]
    unsigned int v18;  // [bp+0x100000], Other Possible Types: char
    char v19;  // [bp+0x100014]
    char v20;  // [bp+0x100018]

    if (!g_103a2699)
    {
        v6 = 0;
        v7 = sub_1031f840;
        v8 = 0;
        v9 = 0;
        v10 = g_103a2234;
        v11 = 0;
        v12 = g_1038b324(0, (-(0 < g_103a2670) & 4294967294) + 32514);
        v13 = 0;
        v14 = 0;
        if (v20)
            v2 = sub_1031fc50();
        else
            v2 = sub_1031fc50();
        v15 = v2;
        sub_1032af80(/* unsupported instruction */ - 384);
        g_103a2699 = 1;
    }
    if (v20)
    {
        for (i = 0; i < 0x100; i += 1)
        {
            g_1038b2d8(i);
        }
    }
    v21 = g_1038b2dc(0);
    v17 = (v21 - g_103a2658) / 2;
    v22 = g_1038b2dc(1);
    v16 = (v22 - g_103a265c) / 2;
    if (v20)
        v1 = /* unsupported instruction */ - 72;
    else
        v1 = /* unsupported instruction */ - 44;
    v4 = v1;
    sub_1031e1d0(/* unsupported instruction */ - 488, v4);
    v18 = 2;
    g_103a2664 = sub_1032b300((-(0 < v19) & 4294967176) + 128, /* unsupported instruction */ - 488, &g_103a2ad0, (-(0 < g_103a2670) & 0xf8000000) + 0x8000000 | 0x80000000, v17, v16, g_103a2658, g_103a265c, 0, 0, g_103a2234, 0);
    v18 = 1;
    sub_10319f00(/* unsupported instruction */ - 488);
    g_1038b2f0(g_103a2664, 4);
    g_1038b2f4(g_103a2664);
    if (v20)
        g_1038b2e0(g_103a2664, 2, 100, 0);
    sub_10353127(/* unsupported instruction */ - 332, "%08X", g_103a2664);
    g_1038b064("LOADINGWINDOW", /* unsupported instruction */ - 332);
    g_103a269a = 0;
    v3 = g_103a2664;
    v18 = 0;
    sub_1031a3a0(/* unsupported instruction */ - 72);
    v18 = 4294967295;
    sub_1031a3a0(/* unsupported instruction */ - 44);
}
```

## `sub_1031f840` `0x1031f840`

_588 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b000;
extern struct_0 *g_1038b004;
extern struct_0 *g_1038b008;
extern struct_0 *g_1038b014;
extern struct_0 *g_1038b018;
extern struct_0 *g_1038b020;
extern struct_0 *g_1038b024;
extern struct_0 *g_1038b03c;
extern struct_0 *g_1038b2cc;
extern struct_0 *g_1038b2d0;
extern struct_0 *g_1038b2d4;
extern struct_0 *g_1038b2d8;
extern struct_0 *g_1038b308;
extern struct_0 *g_1038b340;
extern unsigned int g_1038e180;
extern unsigned int g_103a2658;
extern unsigned int g_103a265c;
extern unsigned int g_103a2668;
extern unsigned int g_103a266c;
extern char g_103a2670;
extern char g_103a2678;

int sub_1031f840(int a0, int a1, int a2, int a3)
{
    unsigned int v8;  // eax
    unsigned int v0;  // [bp-0x60]
    char v1;  // [bp-0x5c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    int i;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v2 = g_1038e180 ^ &v7;
    if (a1 <= 0x202)
    {
        if (a1 == 0x202)
            goto LABEL_1031f987;
        if (a1 != 2)
        {
            if (a1 != 15)
            {
                if (a1 != 275)
                    goto LABEL_1031fa67;
                if (a2 == 2)
                {
                    for (i = 0; i < 0x100; i += 1)
                    {
                        if (((char)g_1038b2d8(i) & 1))
                        {
                            sub_1031f010();
                            break;
                        }
                    }
                }
                else
                {
                    if (a2 == 1)
                    {
                        v8 = g_1038b03c();
                        if (v8 >= *((int *)&g_103a2678))
                        {
                            g_1038b2d4(a0, 1);
                            g_1038b340(a0, 1034, 0, 0);
                        }
                    }
                }
            }
            else
            {
                v3 = g_1038b2cc(a0, &v1);
                v4 = g_1038b024(v3);
                v0 = g_1038b000(v4, g_103a2668);
                v5 = 0;
                if (g_103a266c)
                {
                    v5 = g_1038b014(v3, g_103a266c, 0);
                    g_1038b018(v3);
                }
                g_1038b004(v3, 0, 0, g_103a2658, g_103a265c, v4, 0, 0, 13369376);
                if (v5)
                    g_1038b014(v3, v5, 0);
                g_1038b000(v4, v0);
                g_1038b020(v4);
                g_1038b2d0(a0, &v1);
            }
        }
        else
        {
            if (g_103a2668)
            {
                g_1038b008(g_103a2668);
                g_103a2668 = 0;
            }
            if (g_103a266c)
            {
                g_1038b008(g_103a266c);
                g_103a266c = 0;
            }
        }
    }
    else if (!(a1 != 517 && a1 != 520))
    {
LABEL_1031f987:
        if (g_103a2670)
            sub_1031f010();
    }
    else if (a1 == 1034)
    {
        g_1038b308(a0);
    }
    else
    {
LABEL_1031fa67:
        sub_1032b700(a0, a1, a2, a3);
    }
    return sub_10351225();
}
```

## `sub_1031fa90` `0x1031fa90`

_197 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b03c;
extern struct_0 *g_1038b1b4;
extern struct_0 *g_1038b294;
extern struct_0 *g_1038b2e0;
extern struct_0 *g_1038b344;
extern struct_0 *g_1038b348;
extern struct_0 *g_1038b34c;
extern unsigned int g_103a2658;
extern unsigned int g_103a265c;
extern unsigned int g_103a2660;
extern char g_103a2670;
extern char g_103a2671;
extern unsigned int g_103a2678;

unsigned int sub_1031fa90(void)
{
    unsigned int v4;  // eax
    int v0;  // [bp-0x24]
    char v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]

    v0 = sub_1031f470(g_103a2658, g_103a265c, g_103a2671, g_103a2670, 0);
    if (!v0)
        return 0;
    if (g_103a2660)
    {
        v4 = g_1038b03c();
        g_103a2678 = v4 + g_103a2660 * 1000;
    }
    g_1038b2e0(v0, 1, 250, 0);
    while (g_1038b294(v0))
    {
        if (g_1038b344(&v1, v0, 0, 0, 3))
        {
            if (v2 == 18)
                break;
            g_1038b348(&v1);
            g_1038b34c(&v1);
        }
        else
        {
            g_1038b1b4(1);
        }
    }
    return 0;
}
```

## `sub_1031fb60` `0x1031fb60`

_175 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b0a8;
extern struct_0 *g_1038b0ac;
extern struct_0 *g_1038b128;

char sub_1031fb60(int a0, char a1, char a2)
{
    int v0;  // [bp-0x20]
    int v1;  // [bp-0x1c]
    int v2;  // [bp-0x18]
    int v3;  // [bp-0x14]
    char v4;  // [bp-0xd]
    unsigned int v5;  // [bp-0xc]
    char v6;  // [bp-0x8]

    v4 = 0;
    v5 = sub_103294e0(a0, -0x80000000, 1, 0, 3, 134217856, 0);
    if (v5 == 4294967295)
        return 0;
    v3 = g_1038b0ac(v5, 0);
    v1 = sub_1034fef0(v3);
    v2 = v1;
    if (g_1038b0a8(v5, v2, v3, &v6, 0))
        v4 = sub_1031f410(v2, a1, a2);
    v0 = v2;
    sub_10350eb5(v0);
    g_1038b128(v5);
    return v4;
}
```

