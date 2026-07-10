# elfbot.dll decompiled — jiru 0x1033f450..0x103411c0

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1033f450` `0x1033f450`

_113 bytes. refs "vector<T> too long"_

```c
extern unsigned int g_1038e180;
extern int g_1039ce9c;

void sub_1033f450(void)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4137
    unsigned long v12;  // 4151
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x58]
    char v1;  // [bp-0x54]
    char v2;  // [bp-0x38]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_10370118;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v3 = *((int *)v11);
    v0 = g_1038e180 ^ &v6;
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v3;
    sub_10314590(&v1, "vector<T> too long");
    v5 = 0;
    sub_10331a40(&v2, &v1);
    sub_103533ea(&v2, &g_1039ce9c);
    v5 = 4294967295;
    sub_10314610(&v1);
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v13) = v3;
    return;
}
```

## `sub_1033f4d0` `0x1033f4d0`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1033f4d0(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10340760(a1, 0, a0, &v1);
}
```

## `sub_1033f4f0` `0x1033f4f0`

_44 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1033f4f0(void)
{
    unsigned int v4;  // ecx
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v1 = v4;
    v2 = 42949672;
    v0 = (v2 <= 0 ? 1 : v2);
    return v0;
}
```

## `sub_1033f520` `0x1033f520`

_44 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1033f520(void)
{
    unsigned int v4;  // ecx
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v1 = v4;
    v2 = 0x3fffffff;
    v0 = (v2 <= 0 ? 1 : v2);
    return v0;
}
```

## `sub_1033f550` `0x1033f550`

_1233 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[36];
    unsigned int field_24;
    char padding_28[4];
    int field_2c;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern unsigned int g_1038e180;

struct_1 * sub_1033f550(struct_1 *idx, unsigned int a1)
{
    unsigned long v39;  // ldt
    unsigned long v40;  // gdt
    int v49;  // eax
    unsigned long v51;  // 4119
    unsigned short v41;  // fs
    unsigned long v42;  // 4141
    unsigned long v43;  // 4157
    int v44;  // esi
    int v45;  // edx
    char *v46;  // eax
    char *v47;  // eax
    struct_0 *v48;  // eax
    char v0;  // [bp-0x144]
    unsigned int v1;  // [bp-0xb8]
    unsigned int v2;  // [bp-0xb4]
    int v3;  // [bp-0xb0]
    int v4;  // [bp-0xac]
    struct_1 *v5;  // [bp-0xa8]
    struct_1 *v6;  // [bp-0xa4]
    unsigned int v7;  // [bp-0xa0]
    unsigned int v8;  // [bp-0x9c]
    char *v9;  // [bp-0x94]
    struct_1 *v10;  // [bp-0x7c]
    char v11;  // [bp-0x78]
    char v12;  // [bp-0x70]
    char v13;  // [bp-0x68]
    char v14;  // [bp-0x60]
    struct_1 *v15;  // [bp-0x58]
    struct_0 **v16;  // [bp-0x54]
    int i;  // [bp-0x50]
    int v18;  // [bp-0x4c]
    struct_1 *v19;  // [bp-0x48]
    struct_1 *v20;  // [bp-0x44]
    int v21;  // [bp-0x40]
    char v22;  // [bp-0x39]
    int v23;  // [bp-0x38]
    int v24;  // [bp-0x38]
    unsigned int v25;  // [bp-0x34]
    char v26;  // [bp-0x2e]
    char v27;  // [bp-0x2d]
    unsigned int v28;  // [bp-0x2c]
    char v29;  // [bp-0x25]
    int v30;  // [bp-0x24]
    unsigned int iter;  // [bp-0x20]
    int v32;  // [bp-0x1c]
    unsigned int v33;  // [bp-0x18]
    unsigned int v34;  // [bp-0x14]
    unsigned int v35;  // [bp-0x10]
    unsigned int v36;  // [bp-0xc]
    unsigned int v37;  // [bp-0x8]
    char v38;  // [bp-0x4]

    v37 = 4294967295;
    v36 = sub_1037015e;
    v42 = _ccall(v39, v40, (unsigned int)v41, 0);
    v35 = *((int *)v42);
    v43 = _ccall(v39, v40, (unsigned int)v41, 0);
    *((unsigned int **)v43) = &v35;
    v8 = sub_103419c0(&v16, g_1038e180 ^ &v38, v44);
    v7 = v8;
    v37 = 0;
    v25 = sub_10314e10(v7);
    v37 = 4294967295;
    sub_103130c0(&v16);
    v26 = sub_10314d20(sub_10337e90(v25), 37);
    v27 = 1;
    v32 = -1;
    v45 = _INSERT(0, 0, v26);
    v23 = sub_10341df0(a1, v45, v25, sub_10341c30());
    sub_10341c50(v23);
    v24 = 0;
    v28 = 0;
    iter = 0;
    sub_10340a20(v23);
    v29 = 0;
    v30 = 0;
    while (true)
    {
        iter = sub_10338710(a1, v26, iter);
        if (iter == 4294967295)
            break;
        v6 = (!v30 ? (struct struct_1 *)&idx[1].padding_0[4] : sub_103409d0(v30 - 1) + 32);
        v15 = v6;
        v20 = v15;
        v46 = sub_103189a0(a1, iter + 1);
        v47 = sub_103189a0(a1, iter);
        if (*(v46) == *(v47))
        {
            sub_10341fa0(v20, a1, v28, iter + 1);
            iter += 2;
            v28 = iter;
        }
        else
        {
            if (iter != v28)
            {
                sub_10341fa0(v20, a1, v28, iter);
                v28 = iter;
            }
            iter += 1;
            sub_10340120(&v14, &v13, iter);
            v48 = sub_10340a40(&v14, &v13, iter);
            v33 = v48->field_0;
            v34 = v48[1].field_0;
            v49 = sub_103409d0(v30, v25, iter, sub_10341c30());
            v22 = sub_10342000(&v33, sub_10340150(&v12, v49));
            iter = sub_1031ba20(&v33, sub_10340120(&v11));
            if (v22)
            {
                v28 = iter;
                sub_103409d0(v30);
                sub_10342b70(v30);
                v21 = *((int *)sub_103409d0(v30));
                if (v21 != -3)
                {
                    if (v21 == 4294967295)
                    {
                        v27 = 0;
                    }
                    else if (v21 == -2)
                    {
                        v29 = 1;
                    }
                    else if (v21 > v32)
                    {
                        v32 = v21;
                    }
                    v24 += 1;
                    v30 += 1;
                }
            }
        }
    }
    v5 = (!v30 ? (struct struct_1 *)&idx[1].padding_0[4] : sub_103409d0(v30 - 1) + 32);
    v10 = v5;
    v19 = v10;
    sub_10341fa0(v19, a1, v28, sub_1031e920(a1));
    if (!v27)
    {
        if (v32 >= 0 && ((char)sub_10341c30() & 1))
        {
            v4 = sub_1033fa30(v32, 0);
            v3 = v4;
            v37 = 1;
            sub_1033fc20(v3);
            v37 = 4294967295;
            sub_1033fbd0();
        }
        v18 = 0;
        for (i = 0; i < v24; i += 1)
        {
            if (*((int *)sub_103409d0(i)) == 4294967295)
            {
                *((int *)sub_103409d0(i)) = v18;
                v18 += 1;
            }
        }
        v32 = v18 - 1;
    }
    v9 = &v0;
    v2 = sub_10340a80(sub_10314d20(sub_10337e90(v25), 32));
    v1 = v2;
    v37 = 2;
    v37 = 4294967295;
    sub_103408b0(v24);
    if (v29)
        idx->field_24 = idx->field_24 | 4;
    idx->field_2c = v32 + 1;
    if (v27)
        idx->field_24 = idx->field_24 | 1;
    else
        idx->field_24 = idx->field_24 & 4294967294;
    v51 = _ccall(v39, v40, (unsigned int)v41, 0);
    *((unsigned int *)v51) = v35;
    return idx;
}
```

## `sub_1033fa30` `0x1033fa30`

_107 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390a68;

unsigned int [5] sub_1033fa30(unsigned int *idx, unsigned int a1, unsigned int a2)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4135
    unsigned int v8;  // eax
    unsigned long v9;  // 4151
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
    sub_1033faa0(g_1038e180 ^ &v2, idx, v8, sub_10370188, -1, &v3);
    *(idx) = &g_10390a68;
    idx[3] = a1;
    idx[4] = a2;
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v10) = v8;
    return idx;
}
```

## `sub_1033faa0` `0x1033faa0`

_87 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390a74;

int sub_1033faa0(int a0)
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
    sub_10353203(g_1038e180 ^ &v2, a0, v9, sub_103701b8, -1, &v3);
    *((char **)a0) = &g_10390a74;
    v11 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v11) = v9;
    return a0;
}
```

## `sub_1033fb00` `0x1033fb00`

_16 bytes. (leaf/helper — see body)_

```c
int sub_1033fb00(unsigned int a0)
{
    return "boost::format_error: format generic failure";
}
```

## `sub_1033fb10` `0x1033fb10`

_44 bytes. (leaf/helper — see body)_

```c
int sub_1033fb10(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1033fb40(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_1033fb40` `0x1033fb40`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_1033fb40(int a0)
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
    v12 = sub_103532d2(g_1038e180 ^ &v3, a0, v10, sub_103701e8, -1, &v4);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v10;
    return v12;
}
```

## `sub_1033fb90` `0x1033fb90`

_16 bytes. (leaf/helper — see body)_

```c
int sub_1033fb90(unsigned int a0)
{
    return "boost::bad_format_string: format-string is ill-formed";
}
```

## `sub_1033fba0` `0x1033fba0`

_44 bytes. (leaf/helper — see body)_

```c
int sub_1033fba0(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1033fbd0(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_1033fbd0` `0x1033fbd0`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_1033fbd0(int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4137
    unsigned long v11;  // 4153
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_10370218;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    v4 = 0;
    v4 = 4294967295;
    v12 = sub_1033fb40(v1);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_1033fc20` `0x1033fc20`

_141 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern int g_1039f824;

unsigned int sub_1033fc20(int a0)
{
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // fs
    unsigned long v13;  // 4137
    unsigned long v14;  // 4151
    unsigned int v15;  // eax
    unsigned long v16;  // 4113
    int v0;  // [bp-0x74]
    unsigned int v1;  // [bp-0x70]
    int v2;  // [bp-0x6c]
    int v3;  // [bp-0x68]
    char v4;  // [bp-0x64]
    char v5;  // [bp-0x38]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]
    char v9;  // [bp-0x4]

    v8 = 4294967295;
    v7 = sub_10370248;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v6 = *((int *)v13);
    v1 = g_1038e180 ^ &v9;
    v14 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v14) = &v6;
    v0 = a0;
    sub_10334530();
    v3 = sub_10340180(&v5, a0);
    v2 = v3;
    v8 = 0;
    sub_103401e0(&v4, v2);
    sub_103533ea(&v4, &g_1039f824);
    v8 = 4294967295;
    v15 = sub_1033ff30(&v4, &g_1039f824);
    v16 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v16) = v6;
    return v15;
}
```

## `sub_1033fcb0` `0x1033fcb0`

_158 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390ae4;
extern char g_10390af4;
extern char g_10390afc;

unsigned int sub_1033fcb0(unsigned int idx, int a1)
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
    v3 = sub_10370283;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_1033fd50(a1, g_1038e180 ^ &v5);
    v4 = 0;
    v1 = (!a1 ? 0 : a1 + 40);
    v0 = v1;
    sub_10313b60(idx + 40);
    *((char **)idx) = &g_10390afc;
    *((char **)(idx + 20)) = &g_10390af4;
    *((char **)(idx + 40)) = &g_10390ae4;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return idx;
}
```

## `sub_1033fd50` `0x1033fd50`

_148 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390b08;
extern char g_10390b10;

unsigned int * sub_1033fd50(unsigned int *a0, unsigned int a1)
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
    v2 = sub_103702b3;
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v1 = *((int *)v8);
    v9 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v9) = &v1;
    sub_1033fdf0(a1, g_1038e180 ^ &v4);
    v3 = 0;
    v0 = (!a1 ? 0 : a1 + 20);
    sub_10313a80(a0 + 5, v0);
    *(a0) = &g_10390b10;
    a0[5] = &g_10390b08;
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v10) = v1;
    return a0;
}
```

## `sub_1033fdf0` `0x1033fdf0`

_117 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390a68;

unsigned int [5] sub_1033fdf0(unsigned int *idx, unsigned int *index)
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
    sub_1033fe70(index, g_1038e180 ^ &v2, idx, v8, sub_103702d8, -1, &v3);
    *(idx) = &g_10390a68;
    idx[3] = index[3];
    idx[4] = index[4];
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v10) = v8;
    return idx;
}
```

## `sub_1033fe70` `0x1033fe70`

_93 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390a74;

int sub_1033fe70(int a0, int a1)
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
    sub_1035327a(a1, g_1038e180 ^ &v2, a0, v8, sub_10370308, -1, &v3);
    *((char **)a0) = &g_10390a74;
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v10) = v8;
    return a0;
}
```

## `sub_1033fed0` `0x1033fed0`

_44 bytes. (leaf/helper — see body)_

```c
int sub_1033fed0(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1033ffc0(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_1033ff00` `0x1033ff00`

_44 bytes. (leaf/helper — see body)_

```c
int sub_1033ff00(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1033ff30(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_1033ff30` `0x1033ff30`

_132 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390b08;
extern char g_10390b10;

unsigned int sub_1033ff30(int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4188
    unsigned long v11;  // 4192
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x1c]
    int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1037035f;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    *((char **)a0) = &g_10390b10;
    *((char **)(a0 + 20)) = &g_10390b08;
    v4 = 1;
    v4 = 0;
    v1 = (!a0 ? 0 : a0 + 20);
    sub_10313d70(v1);
    v4 = 4294967295;
    v12 = sub_1033fbd0(a0);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_1033ffc0` `0x1033ffc0`

_142 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390ae4;
extern char g_10390af4;
extern char g_10390afc;

unsigned int sub_1033ffc0(unsigned int idx)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4195
    unsigned long v11;  // 4199
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_103703af;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    *((char **)idx) = &g_10390afc;
    *((char **)(idx + 20)) = &g_10390af4;
    *((char **)(idx + 40)) = &g_10390ae4;
    v4 = 1;
    v4 = 0;
    v1 = (!idx ? 0 : idx + 40);
    sub_10313bb0(v1);
    v4 = 4294967295;
    v12 = sub_1033ff30(idx);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_10340050` `0x10340050`

_148 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10340050(int a0)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4137
    unsigned long v13;  // 4151
    unsigned long v14;  // 4117
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_103703db;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v4 = *((int *)v12);
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v4;
    v2 = sub_10350a53(44, g_1038e180 ^ &v7);
    v6 = 0;
    v1 = (!v2 ? 0 : sub_1033fcb0(v2, a0 - 40));
    v3 = v1;
    v6 = 4294967295;
    v0 = (!v3 ? 0 : v3 + 40);
    v14 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v14) = v4;
    return v0;
}
```

## `sub_103400f0` `0x103400f0`

_42 bytes. (leaf/helper — see body)_

```c
extern int g_1039f824;

int sub_103400f0(int a0)
{
    char v0;  // [bp-0x30]

    sub_1033fcb0(&v0, a0 - 40);
    return sub_103533ea(&v0, &g_1039f824);
}
```

## `sub_10340120` `0x10340120`

_37 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

struct_0 ** sub_10340120(struct_0 *a0, struct_0 **a1)
{
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_1031b730(a1, sub_10314a50(v0), v0);
    return a1;
}
```

## `sub_10340150` `0x10340150`

_43 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

struct_0 ** sub_10340150(struct_0 *a0, struct_0 **a1)
{
    struct_0 *v1;  // eax
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    v1 = sub_10314a50(v0);
    sub_1031b730(a1, &v1->padding_0[*((int *)&v0->padding_8[12])], v0);
    return a1;
}
```

## `sub_10340180` `0x10340180`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10340180(unsigned int a0, int a1)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4138
    unsigned int v8;  // eax
    unsigned int v9;  // ecx
    unsigned long v10;  // 4154
    unsigned long v11;  // 4131
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v8 = *((int *)v7);
    v1 = *((int *)v7);
    v0 = v9;
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v10) = &v1;
    sub_10340b20(a1, g_1038e180 ^ &v2, 0, v8, sub_10370419, -1, &v3);
    v11 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v11) = v8;
    return a0;
}
```

## `sub_103401e0` `0x103401e0`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_103401e0(unsigned int a0, int a1)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4138
    unsigned int v8;  // eax
    unsigned int v9;  // ecx
    unsigned long v10;  // 4154
    unsigned long v11;  // 4131
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v8 = *((int *)v7);
    v1 = *((int *)v7);
    v0 = v9;
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v10) = &v1;
    sub_10340ba0(a1, g_1038e180 ^ &v2, 0, v8, sub_10370459, -1, &v3);
    v11 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v11) = v8;
    return a0;
}
```

## `sub_10340240` `0x10340240`

_444 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[40];
    int field_28;
} struct_0;

typedef struct struct_1 {
    char padding_0[60];
    unsigned int field_3c;
    char padding_40[4];
    char field_44;
} struct_1;

extern unsigned int g_1038e180;

int sub_10340240(struct_0 *a0, int a1)
{
    unsigned long v11;  // ldt
    unsigned long v12;  // gdt
    unsigned short v13;  // fs
    unsigned long v14;  // 4138
    unsigned long v15;  // 4155
    unsigned int v17;  // eax
    int v18;  // eax
    unsigned long v19;  // 4114
    int v0;  // [bp-0x5c]
    int v1;  // [bp-0x58]
    unsigned int v2;  // [bp-0x50]
    struct_1 *v3;  // [bp-0x38]
    int i;  // [bp-0x34]
    char v5;  // [bp-0x30]
    int v6;  // [bp-0x14]
    unsigned int v7;  // [bp-0x10]
    unsigned int v8;  // [bp-0xc]
    char v9;  // [bp-0x8], Other Possible Types: unsigned int
    char v10;  // [bp-0x4]

    v9 = 4294967295;
    v8 = sub_103704a9;
    v14 = _ccall(v11, v12, (unsigned int)v13, 0);
    v7 = *((int *)v14);
    v6 = g_1038e180 ^ &v10;
    v15 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int **)v15) = &v7;
    v2 = 0;
    if (!sub_10340990(v6))
    {
        sub_103145d0(a1, &a0[1].padding_0[8]);
        v9 = 0;
        v2 |= 1;
    }
    else
    {
        if (a0->field_28 < *((int *)&a0[1].padding_0[0]) && ((char)sub_10341c30() & 2))
        {
            v1 = sub_10340400(a0->field_28, *((int *)&a0[1].padding_0[0]));
            v0 = v1;
            v9 = 1;
            sub_10342c00(v0);
            v9 = 0;
            sub_103404b0();
        }
        sub_10315800(&v5);
        v9 = 2;
        sub_1031bf00(&v5, sub_10341b90());
        sub_10316de0(&v5, &a0[1].padding_0[8]);
        for (i = 0; i < sub_10340990(); i += 1)
        {
            v3 = sub_103409d0(i);
            sub_10316de0(&v5, &v3->padding_0[4]);
            if (*((int *)&v3->padding_0[0]) == 4294967294)
            {
                v17 = sub_1031e920(&v5);
                if (v3->field_3c > v17)
                {
                    v18 = sub_1031e920(&v5);
                    sub_103170f0(&v5, v3->field_3c - v18, v3->field_44);
                }
            }
            sub_10316de0(&v5, &v3->padding_0[32]);
        }
        a0[1].padding_0[4] = 1;
        sub_103145d0(a1, &v5);
        v2 |= 1;
        v9 = 0;
        sub_10314610(&v5);
    }
    v19 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int *)v19) = v7;
    return sub_10351225();
}
```

## `sub_10340400` `0x10340400`

_107 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390b1c;

unsigned int [5] sub_10340400(unsigned int *a0, unsigned int a1, unsigned int a2)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4135
    unsigned long v10;  // 4151
    unsigned long v11;  // 4152
    unsigned int v0;  // [bp-0x18]
    unsigned int idx[5];  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_103704d8;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    idx = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    idx = a0;
    sub_1033faa0(idx);
    idx[0] = &g_10390b1c;
    idx[3] = a1;
    idx[4] = a2;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return idx;
}
```

## `sub_10340470` `0x10340470`

_16 bytes. (leaf/helper — see body)_

```c
int sub_10340470(unsigned int a0)
{
    return "boost::too_few_args: format-string referred to more arguments than were passed";
}
```

## `sub_10340480` `0x10340480`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10340480(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_103404b0(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_103404b0` `0x103404b0`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_103404b0(int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4137
    unsigned long v11;  // 4153
    unsigned int v12;  // eax
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_10370508;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    v4 = 0;
    v4 = 4294967295;
    v12 = sub_1033fb40(v1);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_10340500` `0x10340500`

_145 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[40];
    int field_28;
    char padding_2c[4];
    char field_30;
} struct_0;

struct_0 * sub_10340500(struct_0 *idx, int a1)
{
    char v0;  // [bp-0x10]

    if (idx->field_30)
        sub_10341a90();
    sub_10342c90(idx, a1);
    if (!sub_10336b20(&idx->padding_0[16]))
        return idx;
    for (idx->field_28 = idx->field_28 + 1; idx->field_28 < idx->padding_2c; idx->field_28 = idx->field_28 + 1)
    {
        sub_10340870(&v0, idx->field_28);
        if (!(char)sub_10340c70(&v0, idx->field_28))
            return idx;
    }
    return idx;
}
```

## `sub_103405a0` `0x103405a0`

_145 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[40];
    int field_28;
    char padding_2c[4];
    char field_30;
} struct_0;

struct_0 * sub_103405a0(struct_0 *idx, int a1)
{
    char v0;  // [bp-0x10]

    if (idx->field_30)
        sub_10341a90();
    sub_10342ea0(idx, a1);
    if (!sub_10336b20(&idx->padding_0[16]))
        return idx;
    for (idx->field_28 = idx->field_28 + 1; idx->field_28 < idx->padding_2c; idx->field_28 = idx->field_28 + 1)
    {
        sub_10340870(&v0, idx->field_28);
        if (!(char)sub_10340c70(&v0, idx->field_28))
            return idx;
    }
    return idx;
}
```

## `sub_10340640` `0x10340640`

_145 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[40];
    int field_28;
    char padding_2c[4];
    char field_30;
} struct_0;

struct_0 * sub_10340640(struct_0 *idx, int a1)
{
    char v0;  // [bp-0x10]

    if (idx->field_30)
        sub_10341a90();
    sub_10342fb0(idx, a1);
    if (!sub_10336b20(&idx->padding_0[16]))
        return idx;
    for (idx->field_28 = idx->field_28 + 1; idx->field_28 < idx->padding_2c; idx->field_28 = idx->field_28 + 1)
    {
        sub_10340870(&v0, idx->field_28);
        if (!(char)sub_10340c70(&v0, idx->field_28))
            return idx;
    }
    return idx;
}
```

## `sub_103406e0` `0x103406e0`

_38 bytes. (leaf/helper — see body)_

```c
int sub_103406e0(int i, int a1, unsigned int a2)
{
    int v0;  // eax

    for (; i != a1; i += 100)
    {
        sub_10340a00(i);
    }
    return v0;
}
```

## `sub_10340710` `0x10340710`

_77 bytes. (leaf/helper — see body)_

```c
extern int g_10399bb4;

int sub_10340710(unsigned int a0)
{
    unsigned int v0;  // [bp-0x14]
    char v1;  // [bp-0x10]

    if (a0 <= 0)
    {
        a0 = 0;
    }
    else if ((unsigned int)(4294967295 / a0) < 100)
    {
        v0 = 0;
        sub_10315880(&v1);
        sub_103533ea(&v1, &g_10399bb4);
    }
    return sub_10350a53(a0 * 100);
}
```

## `sub_10340760` `0x10340760`

_77 bytes. (leaf/helper — see body)_

```c
extern int g_10399bb4;

int sub_10340760(unsigned int a0)
{
    unsigned int v0;  // [bp-0x14]
    char v1;  // [bp-0x10]

    if (a0 <= 0)
    {
        a0 = 0;
    }
    else if ((unsigned int)(4294967295 / a0) < 4)
    {
        v0 = 0;
        sub_10315880(&v1);
        sub_103533ea(&v1, &g_10399bb4);
    }
    return sub_10350a53(a0 * 4);
}
```

## `sub_103407b0` `0x103407b0`

_108 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

void sub_103407b0(int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4140
    unsigned int v10;  // eax
    unsigned long v11;  // 4156
    unsigned long v12;  // 4113
    int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x8], Other Possible Types: unsigned int
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v2 = 4294967295;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v10 = *((int *)v9);
    v1 = *((int *)v9);
    v0 = a0;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v1;
    v2 = 2;
    sub_10340820(g_1038e180 ^ &v3, a0, v10, sub_10370551, 1, &v4);
    v2 = 0;
    sub_10314610(a0 + 32);
    v2 = 4294967295;
    sub_10314610(a0 + 4);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v10;
    return;
}
```

## `sub_10340820` `0x10340820`

_78 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10340820(int a0)
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
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1037057b;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    v4 = 0;
    v4 = 4294967295;
    v12 = sub_1033e0f0(v1 + 24);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_10340870` `0x10340870`

_56 bytes. (leaf/helper — see body)_

```c
int sub_10340870(int a0, int a1, int a2)
{
    char v0;  // [bp-0x1c]
    char v1;  // [bp-0x10]

    sub_10340ca0(&v1, &v0, a2, a1, a0);
    sub_103412a0(&v1, &v0, a2, a1, a0);
    sub_10341280();
    return a1;
}
```

## `sub_103408b0` `0x103408b0`

_217 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

void sub_103408b0(unsigned int a0, int a1)
{
    unsigned long v11;  // ldt
    unsigned long v12;  // gdt
    unsigned short v13;  // fs
    unsigned long v14;  // 4137
    unsigned long v15;  // 4151
    int v16[2];  // eax
    int v17[2];  // eax
    int v18[2];  // eax
    unsigned long v19;  // 4113
    unsigned int v0;  // [bp-0x4c]
    char v1;  // [bp-0x3c]
    char v2;  // [bp-0x34]
    char v3;  // [bp-0x2c]
    char v4;  // [bp-0x24]
    char v5;  // [bp-0x1c]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]
    char v9;  // [bp-0x4]
    char v10;  // [bp+0x8]

    v8 = 4294967295;
    v7 = sub_103705a8;
    v14 = _ccall(v11, v12, (unsigned int)v13, 0);
    v6 = *((int *)v14);
    v15 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int **)v15) = &v6;
    v8 = 0;
    if (sub_10340990(g_1038e180 ^ &v9, a0) < a1)
    {
        v0 = a1 - sub_10340990(&v10);
        v16 = sub_10330670(a0, &v5);
        sub_10340d50(v16[0], v16[1]);
    }
    else if (a1 < sub_10340990())
    {
        v17 = sub_10330670(a0, &v4);
        sub_103414f0(&v3, &v2, a1, v17[0], v17[1]);
        v18 = sub_103412e0(&v3, &v2, a1, v17[0], v17[1]);
        sub_10340ce0(&v1, v18[0], v18[1]);
    }
    v8 = 4294967295;
    sub_103407b0(&v10);
    v19 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int *)v19) = v6;
    return;
}
```

## `sub_10340990` `0x10340990`

_57 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10340990(unsigned int *a0)
{
    unsigned int v0;  // [bp-0xc]

    v0 = (!a0[1] ? 0 : (int)((a0[2] - a0[1]) / 100));
    return v0;
}
```

## `sub_103409d0` `0x103409d0`

_43 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

int sub_103409d0(struct_0 *a0, unsigned int a1)
{
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    if (a1 >= sub_10340990(v0))
        sub_10353616();
    return a1 * 100 + v0->field_4;
}
```

## `sub_10340a00` `0x10340a00`

_25 bytes. (leaf/helper — see body)_

```c
int sub_10340a00(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10343110(a1, a0, &v1);
}
```

## `sub_10340a20` `0x10340a20`

_32 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

struct_0 * sub_10340a20(struct_0 *a0)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10341910(a0, &v1);
    a0->field_4 = 0;
    return a0;
}
```

## `sub_10340a40` `0x10340a40`

_57 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct_1 field_0;
    unsigned int field_4;
} struct_0;

typedef struct struct_1 {
    struct struct_0 *field_0;
    unsigned int field_4;
} struct_1;

typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

unsigned int [2] sub_10340a40(struct_0 *a0, unsigned int *a1, unsigned int a2)
{
    struct_1 *v2;  // eax
    unsigned int v3;  // edx
    struct_1 v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v0 = (struct_1)a0->field_0.field_0;
    v1 = a0->field_0.field_4;
    v2 = sub_1031e5c0(&v0, a2);
    v3 = v2->field_4;
    *(a1) = v2->field_0;
    a1[1] = v3;
    return a1;
}
```

## `sub_10340a80` `0x10340a80`

_147 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int [25] sub_10340a80(unsigned int *a0, char a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4140
    unsigned long v10;  // 4156
    int v11;  // ecx
    unsigned long v12;  // 4135
    unsigned int v0;  // [bp-0x18]
    unsigned int idx[25];  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_103705f1;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    idx = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    idx = a0;
    idx[0] = 4294967295;
    sub_10315800(&idx[1]);
    v4 = 0;
    sub_10315800(&idx[8]);
    v4 = 1;
    v11 = _INSERT(0, 0, a1);
    sub_103411c0(v11);
    v4 = 2;
    idx[23] = sub_103411a0(v11);
    idx[24] = 0;
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v2;
    return idx;
}
```

## `sub_10340b20` `0x10340b20`

_118 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390b08;
extern char g_10390b10;

unsigned int * sub_10340b20(unsigned int *a0, unsigned int *a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4154
    unsigned long v11;  // 4135
    unsigned int v0;  // [bp-0x18]
    unsigned int *v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_10370623;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_1033fdf0(v1, a1);
    v4 = 0;
    sub_103167f0(v1 + 5);
    *(v1) = &g_10390b10;
    v1[5] = &g_10390b08;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_10340ba0` `0x10340ba0`

_194 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390ae4;
extern char g_10390af4;
extern char g_10390afc;

int sub_10340ba0(unsigned int idx, unsigned int a1)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4139
    unsigned long v11;  // 4153
    unsigned long v12;  // 4123
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char v5;  // [bp-0x8], Other Possible Types: unsigned int
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_10370653;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v0 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    sub_1033fd50(idx, a1);
    v5 = 0;
    sub_10316a00(idx + 40);
    v5 = 1;
    *((char **)idx) = &g_10390afc;
    *((char **)(idx + 20)) = &g_10390af4;
    *((char **)(idx + 40)) = &g_10390ae4;
    v2 = (!a1 ? 0 : a1 + 20);
    v1 = (!idx ? 0 : idx + 20);
    sub_10316940(v1, v2);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v3;
    return idx;
}
```

## `sub_10340c70` `0x10340c70`

_39 bytes. (leaf/helper — see body)_

```c
int sub_10340c70(int a0)
{
    unsigned int *v4;  // eax
    unsigned int v5;  // eax
    int v0;  // [bp-0xc]
    int v1;  // [bp-0x8]
    char v2;  // [bp+0x0]

    v1 = a0;
    v4 = sub_10341220(v0, a0, &v2);
    v5 = sub_10341260(v0, a0, &v2);
    return -(-(0 < (v5 & *(v4))));
}
```

## `sub_10340ca0` `0x10340ca0`

_49 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
} struct_0;

int sub_10340ca0(int a0, unsigned int a1)
{
    struct_0 *v1;  // eax
    char v0;  // [bp-0xc]

    v1 = sub_103414f0(&v0, a0, a0);
    sub_10341640(v1->field_4);
    return a1;
}
```

## `sub_10340ce0` `0x10340ce0`

_105 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    unsigned int field_0;
    int field_4;
} struct_1;

typedef struct struct_0 {
    char padding_0[8];
    int field_8;
} struct_0;

struct_1 * sub_10340ce0(struct_0 *a0, struct_1 *a1, unsigned int a2, int a3, char a4, int a5)
{
    int v0;  // [bp-0x8]

    if ((char)sub_103416a0(&/* unsupported instruction */, a0))
    {
        v0 = sub_10343120(a5, a0->field_8, a3);
        sub_1033e3a0(a0, v0, a0->field_8);
        a0->field_8 = v0;
    }
    a1->field_0 = a2;
    a1->field_4 = a3;
    return a1;
}
```

## `sub_10340d50` `0x10340d50`

_971 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    unsigned int field_8;
    unsigned int field_c;
} struct_0;

extern unsigned int g_1038e180;

void sub_10340d50(struct_0 *idx, unsigned int a1, int a2, int a3, int a4)
{
    unsigned long v14;  // ldt
    unsigned long v15;  // gdt
    unsigned long v24;  // 4120
    unsigned short v16;  // fs
    unsigned long v17;  // 4149
    unsigned int v18;  // eax
    unsigned long v19;  // 4174
    int v20;  // edi
    int v21;  // esi
    int v22;  // ebx
    unsigned int v23;  // eax
    unsigned int v0;  // [bp-0xd8]
    unsigned int v1;  // [bp-0xac]
    int v2;  // [bp-0x9c]
    unsigned int v3;  // [bp-0x94]
    int v4;  // [bp-0x90]
    int v5;  // [bp-0x8c]
    int v6;  // [bp-0x88], Other Possible Types: unsigned int
    char v7;  // [bp-0x84]
    unsigned int v8;  // [bp-0x18]
    char *v9;  // [bp-0x14], Other Possible Types: struct_0 *
    unsigned int v10;  // [bp-0x10]
    unsigned int v11;  // [bp-0xc]
    char v12;  // [bp-0x8], Other Possible Types: unsigned int
    char v13;  // [bp-0x4]

    v12 = 4294967295;
    v11 = sub_10370678;
    v17 = _ccall(v14, v15, (unsigned int)v16, 0);
    v10 = *((int *)v17);
    v9 = idx;
    v18 = g_1038e180 ^ &v13;
    v8 = v18;
    v1 = v18;
    v19 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int **)v19) = &v10;
    v9 = &v1;
    sub_10341320(a4, v18, v20, v21, v22);
    v12 = 0;
    v6 = sub_10341520(a4, v18, v20, v21, v22);
    if (a3)
    {
        v23 = (unsigned int)sub_1033f360(idx);
        if (v23 - sub_10340990(idx) < a3)
        {
            sub_1033f380();
        }
        else if (v6 < sub_10340990(idx) + a3)
        {
            v2 = ((unsigned int)sub_1033f360(idx) - (v6 >> 1) < v6 ? 0 : (v6 >> 1) + v6);
            v6 = v2;
            if (v6 < sub_10340990(idx) + a3)
                v6 = sub_10340990(idx) + a3;
            v4 = sub_1033f410(idx, v6);
            v5 = v4;
            v12 = 1;
            v5 = sub_10343190(idx->field_4, a2, v4);
            v5 = sub_10341560(v5, a3, &v7);
            sub_10343190(a2, idx->field_8, v5);
            v12 = 0;
            a3 += sub_10340990(idx);
            if (idx->field_4)
            {
                sub_1033e3a0(idx, idx->field_4, idx->field_8);
                v0 = (idx->field_c - idx->field_4) / 100;
                sub_1033e3d0(idx, idx->field_4);
            }
            idx->field_c = v6 * 100 + v4;
            idx->field_8 = a3 * 100 + v4;
            idx->field_4 = v4;
        }
        else if ((int)((idx->field_8 - a2) / 100) < a3)
        {
            sub_10343190(a2, idx->field_8, a3 * 100 + a2);
            v12 = 3;
            sub_10341560(idx->field_8, a3 - (int)((idx->field_8 - a2) / 100), &v7);
            v12 = 0;
            idx->field_8 = a3 * 100 + idx->field_8;
            sub_103431c0(a2, idx->field_8 - a3 * 100, &v7);
        }
        else
        {
            v3 = idx->field_8;
            idx->field_8 = sub_10343190(v3 - a3 * 100, v3, idx->field_8);
            sub_103431f0(a2, v3 - a3 * 100, v3);
            sub_103431c0(a2, a3 * 100 + a2, &v7);
        }
    }
    v12 = 4294967295;
    sub_103407b0(&v7);
    v24 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int *)v24) = v10;
    sub_10351225();
    return;
}
```

## `sub_10340efd` `0x10340efd`

_72 bytes. (leaf/helper — see body)_

```c
extern char g_10340f4c;

int sub_10340efd(void)
{
    unsigned int v0;  // [bp-0x4]
    int v2;  // [bp+0xfff70]
    int v3;  // [bp+0xfff78]
    int v4;  // [bp+0xfff7c]
    unsigned int v5;  // [bp+0xfff80]
    unsigned int v6;  // [bp+0x100000]

    sub_1033e3a0(v2, v3, v4);
    v0 = v5;
    sub_1033e3d0(v2, v3);
    sub_103533ea(0, 0);
    v6 = 0;
    return &g_10340f4c;
}
```

## `sub_10341074` `0x10341074`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
} struct_0;

extern char g_103410b6;

int sub_10341074(void)
{
    struct_0 *v1;  // [bp+0xfff70]
    unsigned int v2;  // [bp+0x100000]
    unsigned int v3;  // [bp+0x100010]
    unsigned int v4;  // [bp+0x100014]

    sub_1033e3a0(v1, v4 * 100 + v3, v4 * 100 + v1->field_8);
    sub_103533ea(0, 0);
    v2 = 0;
    return &g_103410b6;
}
```

## `sub_103411a0` `0x103411a0`

_10 bytes. (leaf/helper — see body)_

```c
void sub_103411a0(void)
{
    char v0;  // [bp+0x0]

    sub_103411b0(&v0);
    return;
}
```

## `sub_103411b0` `0x103411b0`

_10 bytes. (leaf/helper — see body)_

```c
unsigned int sub_103411b0(void)
{
    return 2147483647;
}
```

## `sub_103411c0` `0x103411c0`

_95 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

char * sub_103411c0(char *a0, char a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4154
    unsigned long v12;  // 4120
    unsigned int v0;  // [bp-0x18]
    char *v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_103706ab;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    v4 = 0;
    sub_103430c0(_INSERT(sub_1033f0d0(v1 + 24), 0, a1));
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v2;
    return v1;
}
```

