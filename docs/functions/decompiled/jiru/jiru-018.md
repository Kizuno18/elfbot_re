# elfbot.dll decompiled — jiru 0x10313c00..0x10315290

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10313c00` `0x10313c00`

_36 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    struct struct_0 *field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[12];
    struct struct_1 *field_c;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

struct_2 ** sub_10313c00(struct_2 **a0)
{
    struct_2 **v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    if (*(a0))
        a0 = *(a0)->field_0->field_c(a0, &v1);
    return a0;
}
```

## `sub_10313c30` `0x10313c30`

_158 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fa78;
extern char g_1038fa88;
extern char g_1038fa90;

unsigned int sub_10313c30(unsigned int idx, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4139
    unsigned long v10;  // 4153
    unsigned long v11;  // 4142
    int v0;  // [bp-0x24]
    int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036a153;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_10313cd0(a1, g_1038e180 ^ &v5);
    v4 = 0;
    v1 = (!a1 ? 0 : a1 + 40);
    v0 = v1;
    sub_10313b60(idx + 40);
    *((char **)idx) = &g_1038fa90;
    *((char **)(idx + 20)) = &g_1038fa88;
    *((char **)(idx + 40)) = &g_1038fa78;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return idx;
}
```

## `sub_10313cd0` `0x10313cd0`

_148 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fa9c;
extern char g_1038faa4;

unsigned int * sub_10313cd0(unsigned int *a0, unsigned int a1)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4139
    unsigned long v9;  // 4153
    unsigned long v10;  // 4135
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]
    char v4;  // [bp-0x4]

    v3 = 4294967295;
    v2 = sub_1036a183;
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v1 = *((int *)v8);
    v9 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v9) = &v1;
    sub_10313dd0(a1, g_1038e180 ^ &v4);
    v3 = 0;
    v0 = (!a1 ? 0 : a1 + 20);
    sub_10313a80(a0 + 5, v0);
    *(a0) = &g_1038faa4;
    a0[5] = &g_1038fa9c;
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v10) = v1;
    return a0;
}
```

## `sub_10313d70` `0x10313d70`

_87 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fa60;

void sub_10313d70(int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4142
    unsigned long v11;  // 4158
    unsigned long v12;  // 4113
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036a1ab;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    *((char **)v1) = &g_1038fa60;
    v4 = 0;
    v4 = 4294967295;
    sub_10313b10(v1 + 4);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v2;
    return;
}
```

## `sub_10313dd0` `0x10313dd0`

_117 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038f968;

unsigned int [5] sub_10313dd0(unsigned int *idx, unsigned int *index)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4138
    unsigned int v8;  // eax
    unsigned long v9;  // 4154
    unsigned long v10;  // 4160
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
    sub_1035330e(index, g_1038e180 ^ &v2, idx, v8, sub_1036a1d8, -1, &v3);
    *(idx) = &g_1038f968;
    idx[3] = index[3];
    idx[4] = index[4];
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v10) = v8;
    return idx;
}
```

## `sub_10313e50` `0x10313e50`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10313e50(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10316380(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_10313e80` `0x10313e80`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10313e80(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_103162f0(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_10313eb0` `0x10313eb0`

_170 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
    unsigned int field_4;
} struct_1;

typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern unsigned int g_1038e180;
extern char g_1038fa58;
extern struct_0 g_1038faac;

struct_1 * sub_10313eb0(struct_1 *a0, int a1, char a2, unsigned int a3)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4173
    unsigned int v9;  // eax
    unsigned long v10;  // 4177
    unsigned int v11;  // ecx
    unsigned long v13;  // 4120
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v9 = *((int *)v8);
    v1 = *((int *)v8);
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v10) = &v1;
    if (a3)
    {
        a0->field_0 = &g_1038faac.padding_0[0];
        sub_10313f60(g_1038e180 ^ &v3, a0, 0, v9, sub_1036a21c, -1, &v4);
        v2 = 0;
        v0 = 1;
    }
    v11 = a0->field_0->field_4;
    *((char **)((char *)a0 + v11)) = &g_1038fa58;
    a0->field_4 = 0;
    sub_10313fe0(a1, _INSERT(v11, 0, a2));
    v13 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v13) = v9;
    return a0;
}
```

## `sub_10313f60` `0x10313f60`

_87 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fa48;

int sub_10313f60(int a0)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4135
    unsigned int v9;  // eax
    unsigned long v10;  // 4151
    unsigned long v11;  // 4128
    int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v9 = *((int *)v8);
    v1 = *((int *)v8);
    v0 = a0;
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v10) = &v1;
    sub_10313fc0(g_1038e180 ^ &v2, a0, v9, sub_1036a248, -1, &v3);
    *((char **)a0) = &g_1038fa48;
    v11 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v11) = v9;
    return a0;
}
```

## `sub_10313fc0` `0x10313fc0`

_23 bytes. (leaf/helper — see body)_

```c
extern char g_1038fa50;

int sub_10313fc0(unsigned int a0)
{
    *((char **)a0) = &g_1038fa50;
    return a0;
}
```

## `sub_10313fe0` `0x10313fe0`

_109 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
    char padding_8[32];
    unsigned int field_28;
    unsigned int field_2c;
    char field_30;
} struct_0;

int sub_10313fe0(struct_0 *idx, unsigned int a1, char a2)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = idx;
    sub_10314050(idx, &v1);
    idx->field_28 = a1;
    idx->field_2c = 0;
    idx->field_30 = sub_10314ca0(32);
    if (!idx->field_28)
        sub_10314630(4, 0);
    if (!a2)
    {
        idx->field_4 = 0;
        return a2;
    }
    return sub_1034ff7a(idx);
}
```

## `sub_10314050` `0x10314050`

_141 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
    unsigned int field_10;
    unsigned int field_14;
    char padding_18[12];
    unsigned int *field_24;
} struct_0;

unsigned int * sub_10314050(struct_0 *idx)
{
    unsigned int *v3;  // eax
    unsigned int *v0;  // [bp-0x10]
    unsigned int *v1;  // [bp-0x8]

    idx->field_24 = NULL;
    idx->field_c = 0;
    idx->field_10 = 513;
    idx->field_14 = 6;
    memset(idx->padding_18, 0, 12);
    sub_103140e0(0);
    v3 = sub_10350a53(4);
    v1 = v3;
    if (v1)
    {
        v3 = sub_103134d0(v1);
        v0 = v3;
    }
    else
    {
        v0 = NULL;
    }
    idx->field_24 = v0;
    return v3;
}
```

## `sub_103140e0` `0x103140e0`

_27 bytes. (leaf/helper — see body)_

```c
int sub_103140e0(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10314100(a1, 0, a0, &v1);
}
```

## `sub_10314100` `0x10314100`

_385 bytes. refs "ios_base::badbit set", "ios_base::failbit set", "ios_base::eofbit set"_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
    unsigned int field_c;
} struct_0;

extern unsigned int g_1038e180;
extern int g_10399708;

struct_0 * sub_10314100(struct_0 *a0, unsigned int a1, char a2)
{
    unsigned long v11;  // ldt
    unsigned long v12;  // gdt
    unsigned short v13;  // fs
    unsigned long v14;  // 4197
    unsigned long v15;  // 4201
    struct_0 *v16;  // eax
    unsigned long v17;  // 4113
    unsigned int v0;  // [bp-0xe4]
    char v1;  // [bp-0xdc]
    char v2;  // [bp-0xc0]
    char v3;  // [bp-0x98]
    char v4;  // [bp-0x7c]
    char v5;  // [bp-0x54]
    char v6;  // [bp-0x38]
    unsigned int v7;  // [bp-0x10]
    unsigned int v8;  // [bp-0xc]
    unsigned int v9;  // [bp-0x8]
    char v10;  // [bp-0x4]

    v9 = 4294967295;
    v8 = sub_1036a28e;
    v14 = _ccall(v11, v12, (unsigned int)v13, 0);
    v7 = *((int *)v14);
    v0 = g_1038e180 ^ &v10;
    v15 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int **)v15) = &v7;
    a0->field_8 = a1 & 23;
    v16 = a0;
    if ((a0->field_8 & v16->field_c))
    {
        if (a2)
        {
            v16 = sub_103533ea(0, 0);
        }
        else if (((char)a0->field_8 & (char)a0->field_c & 4))
        {
            sub_10314590("ios_base::badbit set");
            v9 = 0;
            sub_103143d0(&v5);
            sub_103533ea(&v6, &g_10399708);
            v9 = 4294967295;
            v16 = sub_10314610(&v6, &g_10399708);
        }
        else if (((char)a0->field_8 & (char)a0->field_c & 2))
        {
            sub_10314590("ios_base::failbit set");
            v9 = 1;
            sub_103143d0(&v3);
            sub_103533ea(&v4, &g_10399708);
            v9 = 4294967295;
            v16 = sub_10314610(&v4, &g_10399708);
        }
        else
        {
            sub_10314590("ios_base::eofbit set");
            v9 = 2;
            sub_103143d0(&v1);
            sub_103533ea(&v2, &g_10399708);
            v9 = 4294967295;
            v16 = sub_10314610(&v2, &g_10399708);
        }
    }
    v17 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int *)v17) = v7;
    return v16;
}
```

## `sub_10314290` `0x10314290`

_115 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fb00;

int sub_10314290(int a0, int a1)
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
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v9 = *((int *)v8);
    v1 = *((int *)v8);
    v0 = a0;
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v10) = &v1;
    sub_1035327a(a1, g_1038e180 ^ &v3, a0, v9, sub_1036a2c3, -1, &v4);
    v2 = 0;
    *((char **)a0) = &g_1038fb00;
    sub_103145d0(a1 + 12);
    v11 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v11) = v9;
    return a0;
}
```

## `sub_10314310` `0x10314310`

_22 bytes. (leaf/helper — see body)_

```c
void sub_10314310(int a0)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_102ec9a0(v0 + 12);
    return;
}
```

## `sub_10314330` `0x10314330`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10314330(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10314360(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_10314360` `0x10314360`

_99 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fb00;

unsigned int sub_10314360(int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4142
    unsigned int v10;  // eax
    unsigned long v11;  // 4158
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
    *((char **)a0) = &g_1038fb00;
    v2 = 1;
    sub_10314610(g_1038e180 ^ &v3, a0, v10, sub_1036a2f3, 0, &v4);
    v12 = sub_103532d2(g_1038e180 ^ &v3, a0, v10, sub_1036a2f3, -1, &v4);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v10;
    return v12;
}
```

## `sub_103143d0` `0x103143d0`

_93 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fb0c;

int sub_103143d0(int a0, int a1)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4138
    unsigned int v8;  // eax
    unsigned long v9;  // 4154
    unsigned long v10;  // 4128
    int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v8 = *((int *)v7);
    v1 = *((int *)v7);
    v0 = a0;
    v9 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v9) = &v1;
    sub_10314430(a1, g_1038e180 ^ &v2, a0, v8, sub_1036a318, -1, &v3);
    *((char **)a0) = &g_1038fb0c;
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v10) = v8;
    return a0;
}
```

## `sub_10314430` `0x10314430`

_108 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fb00;

int sub_10314430(int a0, int a1)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4135
    unsigned int v9;  // eax
    unsigned long v10;  // 4151
    unsigned long v11;  // 4123
    int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v9 = *((int *)v8);
    v1 = *((int *)v8);
    v0 = a0;
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v10) = &v1;
    sub_10353203(g_1038e180 ^ &v3, a0, v9, sub_1036a353, -1, &v4);
    v2 = 0;
    *((char **)a0) = &g_1038fb00;
    sub_103145d0(a1);
    v11 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v11) = v9;
    return a0;
}
```

## `sub_103144a0` `0x103144a0`

_84 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fb0c;

unsigned int sub_103144a0(int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4139
    unsigned long v11;  // 4155
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036a378;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    *((char **)v1) = &g_1038fb0c;
    v4 = 0;
    v4 = 4294967295;
    v12 = sub_10314360(v1);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_10314500` `0x10314500`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10314500(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_103144a0(v0);
    if (((char)a1 & 1))
        sub_10350abd(v0);
    return v0;
}
```

## `sub_10314530` `0x10314530`

_93 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fb0c;

int sub_10314530(int a0, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4154
    unsigned long v11;  // 4128
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036a3a8;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_10314290(v1, a1);
    *((char **)v1) = &g_1038fb0c;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_10314590` `0x10314590`

_58 bytes. (leaf/helper — see body)_

```c
int sub_10314590(int a0, int a1)
{
    sub_1031a280(a0, a0);
    sub_103147d0(a0, a0);
    sub_10314750(0, 0);
    sub_10314720(a1);
    return a0;
}
```

## `sub_103145d0` `0x103145d0`

_61 bytes. (leaf/helper — see body)_

```c
extern int g_1038fb14;

int sub_103145d0(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1031e860(a1, a0, &v1);
    sub_10314750(0, 0);
    sub_10314660(a1, 0, g_1038fb14);
    return a0;
}
```

## `sub_10314610` `0x10314610`

_23 bytes. (leaf/helper — see body)_

```c
void sub_10314610(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10314750(1, 0, a0, &v1);
    return;
}
```

## `sub_10314630` `0x10314630`

_43 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
} struct_0;

int sub_10314630(struct_0 *a0, unsigned int a1, char a2)
{
    unsigned int v3;  // eax
    unsigned int v0;  // [bp-0xc]
    struct_0 *v1;  // [bp-0x8]

    v1 = a0;
    v1 = a0;
    if (!a1)
        return v3;
    *((char *)&v0) = a2;
    return sub_103147f0(sub_10313840(v1) | a1);
}
```

## `sub_10314660` `0x10314660`

_182 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

extern int g_1038fb14;

struct_0 * sub_10314660(struct_0 *a0, struct_0 *a1, int a2, int a3)
{
    unsigned int v1;  // eax
    int v2;  // eax
    int v0;  // [bp-0x8]

    if (sub_1031e920(a0) < a2)
        sub_103503dd();
    v0 = sub_1031e920() - a2;
    if (a3 < v0)
        v0 = a3;
    if (a0 == a1)
    {
        sub_103148c0(a2 + v0, g_1038fb14);
        sub_103148c0(0, a2);
        return a0;
    }
    if (!(char)sub_103149b0(v0, 0))
        return a0;
    v1 = sub_10314a50(v0);
    v2 = sub_10314a50(a0->field_18, v1 + a2);
    sub_10313350(v2, a0->field_18, v1 + a2, v0);
    sub_10314960(v0);
    return a0;
}
```

## `sub_10314720` `0x10314720`

_38 bytes. (leaf/helper — see body)_

```c
int sub_10314720(unsigned int a0, int a1)
{
    unsigned int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_10314830(a1, sub_103136c0(a1));
}
```

## `sub_10314750` `0x10314750`

_118 bytes. (leaf/helper — see body)_

```c
int sub_10314750(unsigned int *idx, char a1, int a2)
{
    unsigned int v0;  // [bp-0x8]

    if (a1 && idx[6] >= 16)
    {
        v0 = idx[1];
        if (a2 > 0)
            sub_10313350(idx + 1, 16, v0, a2);
        sub_1033e3d0(v0, idx[6] + 1);
    }
    idx[6] = 15;
    return sub_10314960(a2);
}
```

## `sub_103147d0` `0x103147d0`

_28 bytes. (leaf/helper — see body)_

```c
int sub_103147d0(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]
    unsigned int v2;  // [bp+0x4]

    v0 = a0;
    sub_1033f400(&v2, a0, &v1);
    return a0;
}
```

## `sub_103147f0` `0x103147f0`

_57 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
    unsigned int field_c;
} struct_0;

struct_0 * sub_103147f0(struct_0 *a0, unsigned int a1, char a2)
{
    unsigned int v0;  // [bp-0xc]

    v0 = (!a0[2].field_8 ? a1 | 4 : a1);
    return sub_10314100(a0, v0, a2);
}
```

## `sub_10314830` `0x10314830`

_132 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

struct_0 * sub_10314830(struct_0 *a0, int a1, int a2)
{
    int v2;  // eax
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    if ((char)sub_10314c60(a1, a0, &v1))
        return sub_10314660(a0, a0, a1 - sub_10314a50(a2), a2);
    if (!(char)sub_103149b0(a2, 0))
        return a0;
    v2 = sub_10314a50(a0->field_18, a1, a2);
    sub_10313350(v2, a0->field_18, a1, a2);
    sub_10314960(a2);
    return a0;
}
```

## `sub_103148c0` `0x103148c0`

_148 bytes. (leaf/helper — see body)_

```c
unsigned int [7] sub_103148c0(unsigned int *idx, unsigned int a1, unsigned int a2)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    int v0;  // [bp-0x8]

    if (idx[5] < a1)
        sub_103503dd(idx);
    if (idx[5] - a1 < a2)
        a2 = idx[5] - a1;
    if (a2 <= 0)
        return idx;
    v1 = sub_10314a50(idx[5] - a1 - a2);
    v2 = sub_10314a50(idx[6] - a1, v1 + a1 + a2);
    sub_103159d0(v2 + a1);
    v0 = idx[5] - a2;
    sub_10314960(v0);
    return idx;
}
```

## `sub_10314960` `0x10314960`

_52 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

int sub_10314960(struct_0 *a0, unsigned int a1)
{
    char v0;  // [bp-0x5]

    v0 = 0;
    a0->field_14 = a1;
    return sub_103149a0(sub_10314a50(&v0, a0) + a1);
}
```

## `sub_103149a0` `0x103149a0`

_15 bytes. (leaf/helper — see body)_

```c
char * sub_103149a0(char *a0, char *a1)
{
    *(a0) = *(a1);
    return a0;
}
```

## `sub_103149b0` `0x103149b0`

_148 bytes. (leaf/helper — see body)_

```c
int sub_103149b0(void* a0, int a1, char a2)
{
    int v0;  // [bp-0xc]

    if (sub_10314a80() < a1)
        sub_1035039e();
    if ((int)a0[24] < a1)
    {
        sub_10314ac0(a1, (int)a0[20]);
    }
    else if (a2 && a1 < 16)
    {
        v0 = (a1 < (int)a0[20] ? a1 : (int)a0[20]);
        sub_10314750(a0, 1, v0);
    }
    else if (!a1)
    {
        sub_10314960(a0, 0);
    }
    return -(-(0 < a1));
}
```

## `sub_10314a50` `0x10314a50`

_45 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    struct struct_0 *field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

struct_0 * sub_10314a50(struct_0 *a0)
{
    struct_0 *v0;  // [bp-0xc]

    v0 = (a0->field_18 < 16 ? (struct struct_0 *)&a0->field_4 : a0->field_4);
    return v0;
}
```

## `sub_10314a80` `0x10314a80`

_51 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10314a80(unsigned int a0)
{
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v1 = a0;
    v2 = sub_10314de0();
    v0 = (v2 <= 1 ? 1 : v2 - 1);
    return v0;
}
```

## `sub_10314ac0` `0x10314ac0`

_285 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10314ac0(void* idx, unsigned int a1, unsigned int a2)
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
    v8 = sub_1036a3d0;
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
    v4 = a1 | 15;
    if (sub_10314a80(idx) < v4)
    {
        v4 = a1;
    }
    else if ((unsigned int)(v4 / 3) < (int)idx[24] >> 1)
    {
        v19 = sub_10314a80(idx);
        if ((int)idx[24] <= v19 - ((int)idx[24] >> 1))
            v4 = ((int)idx[24] >> 1) + (int)idx[24];
    }
    v5 = 0;
    v9 = 0;
    v5 = sub_10314c40(v4 + 1);
    v9 = 4294967295;
    if (a2 > 0)
        sub_10313350(v5, v4 + 1, sub_10314a50(idx), a2);
    sub_10314750(idx, 1, 0);
    *((int *)&idx[4]) = v5;
    *((unsigned int *)&idx[24]) = v4;
    v21 = sub_10314960(idx, a2);
    v22 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int *)v22) = v7;
    return v21;
}
```

## `sub_10314b72` `0x10314b72`

_19 bytes. (leaf/helper — see body)_

```c
void sub_10314b72(void)
{
    char v0;  // [bp+0x0]
    unsigned int v2;  // [bp+0xfffec]
    char *v3;  // [bp+0xffff4]
    char v4;  // [bp+0x100000]
    unsigned int v5;  // [bp+0x10000c]

    v3 = &v0;
    v2 = v5;
    v4 = 2;
    sub_10314b85();
    return;
}
```

## `sub_10314b85` `0x10314b85`

_34 bytes. (leaf/helper — see body)_

```c
extern char g_10314bd0;

int sub_10314b85(void)
{
    int v3;  // edx
    unsigned int v1;  // [bp+0xffff0]
    unsigned int v2;  // [bp+0x100000]

    v1 = sub_10314c40(v3);
    v2 = 1;
    v2 = 1;
    return &g_10314bd0;
}
```

## `sub_10314b93` `0x10314b93`

_34 bytes. (leaf/helper — see body)_

```c
extern char g_10314bbc;

int sub_10314b93(void)
{
    unsigned int *v1;  // [bp+0xfffe8]
    unsigned int v2;  // [bp+0x100000]

    sub_10314750(v1, 1, 0);
    sub_103533ea(0, 0);
    v2 = 1;
    return &g_10314bbc;
}
```

## `sub_10314c40` `0x10314c40`

_27 bytes. (leaf/helper — see body)_

```c
int sub_10314c40(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10315830(a1, 0, a0, &v1);
}
```

## `sub_10314c60` `0x10314c60`

_51 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

char sub_10314c60(struct_0 *a0, struct_0 *a1)
{
    struct_0 *v1;  // eax
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    if (a1 >= sub_10314a50(v0))
    {
        v1 = sub_10314a50(v0);
        if (&v1->padding_0[*((int *)&v0->padding_8[12])] > a1)
            return 1;
    }
    return 0;
}
```

## `sub_10314c8b` `0x10314c8b`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10314c8b(void)
{
}
```

## `sub_10314ca0` `0x10314ca0`

_127 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern unsigned int g_1038e180;

char sub_10314ca0(unsigned int a0, char a1)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4139
    unsigned long v13;  // 4153
    int v14;  // eax
    char v15;  // al
    unsigned long v16;  // 4113
    int v0;  // [bp-0x24]
    int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    struct_0 **v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]
    char v8;  // [bp-0x4]

    v7 = 4294967295;
    v6 = sub_1036a3f8;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v5 = *((int *)v12);
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v5;
    v2 = a0;
    v1 = sub_10314d40(&v3, g_1038e180 ^ &v8);
    v0 = v1;
    v7 = 0;
    v4 = sub_10314e10(v0);
    v7 = 4294967295;
    v14 = _INSERT(sub_103130c0(&v3), 0, a1);
    v15 = sub_10314d20(v14);
    v16 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v16) = v5;
    return v15;
}
```

## `sub_10314d20` `0x10314d20`

_30 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[24];
    struct struct_1 *field_18;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

char sub_10314d20(struct_0 **a0, char a1)
{
    unsigned int v2;  // eax
    struct_0 **v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    v2 = _INSERT(0, 0, a1);
    return *(a0)->field_18(v2, a0, &v1);
}
```

## `sub_10314d40` `0x10314d40`

_98 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[36];
    int field_24;
} struct_0;

extern unsigned int g_1038e180;

int sub_10314d40(struct_0 *a0, unsigned int a1)
{
    unsigned long v3;  // ldt
    unsigned long v4;  // gdt
    unsigned short v5;  // fs
    unsigned long v6;  // 4141
    unsigned int v7;  // eax
    unsigned long v8;  // 4155
    unsigned long v9;  // 4131
    unsigned int v0;  // [bp-0x10]
    char v1;  // [bp-0x4]
    char v2;  // [bp+0x0]

    v6 = _ccall(v3, v4, (unsigned int)v5, 0);
    v7 = *((int *)v6);
    v0 = *((int *)v6);
    v8 = _ccall(v3, v4, (unsigned int)v5, 0);
    *((unsigned int **)v8) = &v0;
    sub_10314db0(a0->field_24, g_1038e180 ^ &v1, a0, 0, v7, sub_1036a439, -1, &v2);
    v9 = _ccall(v3, v4, (unsigned int)v5, 0);
    *((unsigned int *)v9) = v7;
    return a1;
}
```

## `sub_10314db0` `0x10314db0`

_36 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

struct_0 ** sub_10314db0(struct_0 **a0, unsigned int *a1)
{
    struct_0 **v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    *(v0) = *(a1);
    sub_10313500(*(v0));
    return v0;
}
```

## `sub_10314de0` `0x10314de0`

_44 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10314de0(void)
{
    unsigned int v4;  // ecx
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v1 = v4;
    v2 = 4294967295;
    v0 = (v2 <= 0 ? 1 : v2);
    return v0;
}
```

## `sub_10314e10` `0x10314e10`

_233 bytes. refs "bad cast"_

```c
extern unsigned int g_1038e180;
extern int g_103999a0;
extern unsigned int g_103a225c;

unsigned int sub_10314e10(unsigned int a0)
{
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // fs
    unsigned long v13;  // 4137
    unsigned long v14;  // 4151
    unsigned long v15;  // 4117
    unsigned int v0;  // [bp-0x34]
    char v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x24]
    unsigned int v3;  // [bp-0x20]
    int v4;  // [bp-0x18]
    unsigned int v5;  // [bp-0x14]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]
    char v9;  // [bp-0x4]

    v8 = 4294967295;
    v7 = sub_1036a468;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v6 = *((int *)v13);
    v14 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v14) = &v6;
    sub_10350060(0, g_1038e180 ^ &v9);
    v8 = 0;
    v3 = g_103a225c;
    v4 = sub_10314f00(0, g_1038e180 ^ &v9);
    v5 = sub_10314fb0(v4);
    if (!v5)
    {
        if (v3)
        {
            v5 = v3;
        }
        else if (sub_10315040(&v3) == 4294967295)
        {
            sub_103532f5("bad cast");
            sub_103533ea(&v1, &g_103999a0);
        }
        else
        {
            v5 = v3;
            g_103a225c = v3;
            v2 = v3;
            sub_10313500(v2);
            sub_10314f90();
        }
    }
    v0 = v5;
    v8 = 4294967295;
    sub_10350081();
    v15 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v15) = v6;
    return v0;
}
```

## `sub_10314f00` `0x10314f00`

_134 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern unsigned int g_103a2e58;

unsigned int sub_10314f00(unsigned int *a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4172
    unsigned long v10;  // 4176
    unsigned int v11;  // eax
    unsigned long v12;  // 4119
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]
    char v4;  // [bp-0x4]

    v3 = 4294967295;
    v2 = sub_1036a498;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v1 = *((int *)v9);
    v0 = g_1038e180 ^ &v4;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v1;
    if (!*(a0))
    {
        sub_10350060(0);
        v3 = 0;
        if (!*(a0))
        {
            g_103a2e58 = g_103a2e58 + 1;
            *(a0) = g_103a2e58;
        }
        v3 = 4294967295;
        sub_10350081();
    }
    v11 = *(a0);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v1;
    return v11;
}
```

## `sub_10314f90` `0x10314f90`

_23 bytes. (leaf/helper — see body)_

```c
int sub_10314f90(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_103501bc(a0, a0, &v1);
}
```

## `sub_10314fb0` `0x10314fb0`

_130 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
    char padding_c[8];
    char field_14;
} struct_0;

typedef struct struct_1 {
    char padding_0[8];
    unsigned int field_8;
} struct_1;

unsigned int sub_10314fb0(struct_0 **a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    struct_1 *v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v1 = (a1 < *((int *)&*(a0)->padding_c[0]) ? *((int *)(*(a0)->field_8 + a1 * 4)) : 0);
    v3 = v1;
    if (!v3 && *(a0)->field_14)
    {
        v2 = sub_103500ee();
        v0 = (a1 < *((int *)&v2[1].padding_0[0]) ? *((int *)(v2->field_8 + a1 * 4)) : 0);
        return v0;
    }
    return v3;
}
```

## `sub_10314ffe` `0x10314ffe`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10314ffe(void)
{
}
```

## `sub_10315040` `0x10315040`

_144 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10315040(unsigned int *a0)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4166
    unsigned long v12;  // 4170
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036a4cb;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v0 = g_1038e180 ^ &v7;
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    if (a0 && !*(a0))
    {
        v2 = sub_10350a53(24);
        v6 = 0;
        v1 = (!v2 ? 0 : sub_103150d0(0, 0, 0));
        v3 = v1;
        v6 = 4294967295;
        *(a0) = v3;
    }
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v13) = v4;
    return 2;
}
```

## `sub_103150d0` `0x103150d0`

_222 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1038fb20;

int sub_103150d0(unsigned int *idx, unsigned int a1, char a2, int a3)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4140
    unsigned long v10;  // 4157
    unsigned long v11;  // 4121
    char v0;  // [bp-0x90]
    int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036a506;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_10315330(a3, v1, idx);
    v4 = 0;
    *(idx) = &g_1038fb20;
    sub_103151b0("C");
    v4 = 1;
    sub_103154a0(&v0);
    v4 = 0;
    sub_10315290(&v0);
    if (a1)
    {
        sub_10315530();
        idx[4] = a1;
        idx[5] = -(0 < a2);
    }
    v4 = 4294967295;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return sub_10351225();
}
```

## `sub_103151b0` `0x103151b0`

_221 bytes. refs "bad locale name"_

```c
extern unsigned int g_1038e180;
extern int g_10399a74;

int sub_103151b0(int a0, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4152
    unsigned long v11;  // 4123
    char v0;  // [bp-0x54]
    char v1;  // [bp-0x38]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8], Other Possible Types: char
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036a56c;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_10350060(0, g_1038e180 ^ &v5, a0);
    v4 = 0;
    sub_10315800(0, g_1038e180 ^ &v5, a0);
    v4 = 1;
    sub_10315800();
    v4 = 2;
    sub_10315800();
    v4 = 3;
    sub_10315800();
    v4 = 4;
    if (!a1)
    {
        sub_10314590(&v0, "bad locale name");
        v4 = 5;
        sub_10314430(&v1, &v0);
        sub_103533ea(&v1, &g_10399a74);
        v4 = 4;
        sub_10314610(&v0);
    }
    sub_10350354(a0, a1);
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return a0;
}
```

## `sub_10315290` `0x10315290`

_147 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

void sub_10315290(int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned int v10;  // eax
    unsigned long v11;  // 4154
    unsigned long v12;  // 4113
    int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0x8], Other Possible Types: char
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v2 = 4294967295;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v10 = *((int *)v9);
    v1 = *((int *)v9);
    v0 = a0;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v1;
    sub_103501f5(a0, g_1038e180 ^ &v3, a0, v10, sub_1036a5c4, 4, &v4);
    v2 = 3;
    sub_10314610(a0 + 88);
    v2 = 2;
    sub_10314610(a0 + 60);
    v2 = 1;
    sub_10314610(a0 + 32);
    v2 = 0;
    sub_10314610(a0 + 4);
    v2 = 4294967295;
    sub_10350081();
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v10;
    return;
}
```

