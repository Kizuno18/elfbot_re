# elfbot.dll decompiled — jiru 0x103189d0..0x1031a884

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_103189d0` `0x103189d0`

_24 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    struct struct_1 *field_8;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_103189d0(struct_0 **a0)
{
    struct_0 **v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return *(a0)->field_8(a0, &v1);
}
```

## `sub_103189f0` `0x103189f0`

_100 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    struct struct_1 *field_c;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern unsigned int g_1038e180;

int sub_103189f0(struct_0 **a0, unsigned int a1)
{
    unsigned long v3;  // ldt
    unsigned long v4;  // gdt
    unsigned short v5;  // fs
    unsigned long v6;  // 4144
    unsigned int v7;  // eax
    unsigned long v8;  // 4158
    unsigned long v9;  // 4131
    unsigned int v0;  // [bp-0x10]
    char v1;  // [bp-0x4]
    char v2;  // [bp+0x0]

    v6 = _ccall(v3, v4, (unsigned int)v5, 0);
    v7 = *((int *)v6);
    v0 = *((int *)v6);
    v8 = _ccall(v3, v4, (unsigned int)v5, 0);
    *((unsigned int **)v8) = &v0;
    *(a0)->field_c(a1, g_1038e180 ^ &v1, a0, 0, v7, sub_1036af69, 4294967295, &v2);
    v9 = _ccall(v3, v4, (unsigned int)v5, 0);
    *((unsigned int *)v9) = v7;
    return a1;
}
```

## `sub_10318a60` `0x10318a60`

_8 bytes. (leaf/helper — see body)_

```c
char sub_10318a60(char a0)
{
    return a0;
}
```

## `sub_10318a70` `0x10318a70`

_1933 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
    char padding_c[8];
    char field_14;
} struct_0;

typedef struct struct_1 {
    char field_0;
} struct_1;

extern unsigned int g_1038e180;

int sub_10318a70(unsigned int a0, char *a1, int a2, int a3, struct_0 **a4)
{
    unsigned long v23;  // ldt
    unsigned long v24;  // gdt
    char v33;  // al
    struct_1 **v34;  // eax
    char v35;  // al
    char v36;  // al
    char v37;  // al
    char v38;  // al
    unsigned long v39;  // 4120
    unsigned short v25;  // fs
    unsigned long v26;  // 4140
    unsigned int v27;  // esi
    unsigned long v28;  // 4159
    char v29;  // al
    char v30;  // al
    char *v31;  // eax
    char *v32;  // eax
    unsigned int v0;  // [bp-0x88]
    unsigned int v1;  // [bp-0x84]
    unsigned int v2;  // [bp-0x80]
    unsigned int v3;  // [bp-0x7c]
    char *v4;  // [bp-0x78]
    int v5;  // [bp-0x74]
    struct_0 *v6;  // [bp-0x70]
    unsigned int node;  // [bp-0x6c]
    char v8;  // [bp-0x68]
    char v9;  // [bp-0x4a]
    char v10;  // [bp-0x49]
    char v11;  // [bp-0x48]
    unsigned int v12;  // [bp-0x2c]
    char v13;  // [bp-0x25]
    int iter1;  // [bp-0x24]
    int iter2;  // [bp-0x20]
    char v16;  // [bp-0x19]
    char iter[3];  // [bp-0x18]
    unsigned int v18;  // [bp-0x14]
    unsigned int v19;  // [bp-0x10]
    unsigned int v20;  // [bp-0xc]
    char v21;  // [bp-0x8], Other Possible Types: unsigned int
    char v22;  // [bp-0x4]

    v21 = 4294967295;
    v20 = sub_1036afa0;
    v26 = _ccall(v23, v24, (unsigned int)v25, 0);
    v19 = *((int *)v26);
    v12 = g_1038e180 ^ &v22;
    v3 = v27;
    v2 = v12;
    v28 = _ccall(v23, v24, (unsigned int)v25, 0);
    *((unsigned int **)v28) = &v19;
    v18 = sub_10316fe0(a4);
    sub_103189f0(v18, &v11);
    v21 = 0;
    v1 = a0 + 8;
    v0 = 0;
    v16 = sub_10318a60(48);
    iter = a1;
    v13 = 0;
    if (!(char)sub_10319590(a2, a3))
    {
        v29 = sub_10319230();
        v1 = a0 + 8;
        v0 = 0;
        if (v29 == sub_10318a60(43))
        {
            iter[0] = 43;
            iter = &iter[1];
            sub_10319260();
        }
        else
        {
            v30 = sub_10319230();
            v1 = a0 + 8;
            v0 = 0;
            if (v30 == sub_10318a60(45))
            {
                iter[0] = 45;
                iter = &iter[1];
                sub_10319260();
            }
        }
    }
    v10 = 0;
    iter1 = 0;
    iter2 = 0;
    if (*((char *)(unsigned int)sub_102ec9a0(&v11)) == 127 || *((char *)(unsigned int)sub_102ec9a0(&v11)) <= 0)
    {
        while ((char)sub_103195b0(a2, a3) && v16 <= (char)sub_10319230() && (char)sub_10319230() <= v16 + 9)
        {
            if (iter1 >= 36)
            {
                iter2 += 1;
            }
            else if ((char)sub_10319230() != v16 || iter1)
            {
                iter[0] = (char)sub_10319230() - v16 + 48;
                iter = &iter[1];
                iter1 += 1;
            }
            v10 = 1;
            sub_10319260();
        }
    }
    else
    {
        v9 = sub_103189d0(v18);
        sub_10317800(&v8, 1, 0);
        v21 = 1;
        node = 0;
        while ((char)sub_103195b0(a2, a3))
        {
            if (v16 <= (char)sub_10319230() && (char)sub_10319230() <= v16 + 9)
            {
                v10 = 1;
                if (iter1 >= 36)
                {
                    iter2 += 1;
                }
                else
                {
                    if ((char)sub_10319230() != v16 || iter1)
                    {
                        iter[0] = (char)sub_10319230() - v16 + 48;
                        iter = &iter[1];
                        iter1 += 1;
                    }
                }
                if (*((char *)sub_103189a0(&v8, node)) != 127)
                {
                    v4 = sub_103189a0(&v8, node);
                    *(v4) = *(v4) + 1;
                }
            }
            else if (!*((char *)sub_103189a0(&v8, node)) || !v9 || (char)sub_10319230() != v9)
            {
                break;
            }
            else
            {
                sub_103170f0(&v8, 1, 0);
                node += 1;
            }
            sub_10319260();
        }
        if (node)
        {
            if (*((char *)sub_103189a0(&v8, node)) > 0)
                node += 1;
            else
                v13 = 1;
        }
        v6 = (unsigned int)sub_102ec9a0(&v11);
        while (true)
        {
            if (v13 || node <= 0 || v6->padding_0[0] == 127)
                break;
            node -= 1;
            if (node != 1 && !((v31 = (char *)sub_103189a0(&v8, node), (int)(char)v6->padding_0[0] == (int)*((char *)sub_103189a0(&v8, node)))) || !node && !((v32 = (char *)sub_103189a0(&v8, node), (int)(char)v6->padding_0[0] >= (int)*((char *)sub_103189a0(&v8, node)))))
            {
                v13 = 1;
            }
            else if (v6->padding_0[1] > 0)
            {
                v6 = &v6->padding_0[1];
            }
        }
        v21 = 0;
        sub_10314610(&v8);
    }
    if (v10 && !iter1)
    {
        iter[0] = 48;
        iter = &iter[1];
    }
    if ((char)sub_103195b0(a2, a3))
    {
        v33 = sub_10319230();
        if (v33 == (char)sub_10319210())
        {
            v34 = sub_10353681();
            iter[0] = *(v34)->field_0;
            iter = &iter[1];
            sub_10319260();
        }
    }
    if (!iter1)
    {
        while ((char)sub_103195b0(a2, a3) && (char)sub_10319230() == v16)
        {
            iter2 -= 1;
            v10 = 1;
            sub_10319260();
        }
        if (iter2 < 0)
        {
            iter[0] = 48;
            iter = &iter[1];
            iter2 += 1;
        }
    }
    while ((char)sub_103195b0(a2, a3) && v16 <= (char)sub_10319230() && (char)sub_10319230() <= v16 + 9)
    {
        if (iter1 < 36)
        {
            iter[0] = (char)sub_10319230() - v16 + 48;
            iter = &iter[1];
            iter1 += 1;
        }
        v10 = 1;
        sub_10319260();
    }
    if (v10 && (char)sub_103195b0(a2, a3))
    {
        v35 = sub_10319230();
        v1 = a0 + 8;
        v0 = 0;
        if (v35 == sub_10318a60(101) || (v36 = (char)sub_10319230(), v1 = a0 + 8, v0 = 0, (int)(char)(char)sub_10319230() == (int)sub_10318a60(69)))
        {
            iter[0] = 101;
            iter = &iter[1];
            sub_10319260();
            v10 = 0;
            iter1 = 0;
            if (!(char)sub_10319590(a2, a3))
            {
                v37 = sub_10319230();
                v1 = a0 + 8;
                v0 = 0;
                if (v37 == sub_10318a60(43))
                {
                    iter[0] = 43;
                    iter = &iter[1];
                    sub_10319260();
                }
                else
                {
                    v38 = sub_10319230();
                    v1 = a0 + 8;
                    v0 = 0;
                    if (v38 == sub_10318a60(45))
                    {
                        iter[0] = 45;
                        iter = &iter[1];
                        sub_10319260();
                    }
                }
            }
            while ((char)sub_103195b0(a2, a3) && (char)sub_10319230() == v16)
            {
                v10 = 1;
                sub_10319260();
            }
            if (v10)
            {
                iter[0] = 48;
                iter = &iter[1];
            }
            while ((char)sub_103195b0(a2, a3) && v16 <= (char)sub_10319230() && (char)sub_10319230() <= v16 + 9)
            {
                if (iter1 < 8)
                {
                    iter[0] = (char)sub_10319230() - v16 + 48;
                    iter = &iter[1];
                    iter1 += 1;
                }
                v10 = 1;
                sub_10319260();
            }
        }
    }
    if (v13 || !v10)
        iter = a1;
    iter[0] = 0;
    v5 = iter2;
    v21 = 4294967295;
    sub_10314610(&v11);
    v39 = _ccall(v23, v24, (unsigned int)v25, 0);
    *((unsigned int *)v39) = v19;
    return sub_10351225();
}
```

## `sub_10318d8b` `0x10318d8b`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10318d8b(void)
{
}
```

## `sub_10318df7` `0x10318df7`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10318df7(void)
{
}
```

## `sub_10319210` `0x10319210`

_24 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    struct struct_1 *field_4;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

int sub_10319210(struct_0 **a0)
{
    struct_0 **v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return *(a0)->field_4(a0, &v1);
}
```

## `sub_10319230` `0x10319230`

_36 bytes. (leaf/helper — see body)_

```c
char sub_10319230(char *a0)
{
    char v0[10];  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    if (!a0[8])
        sub_103192e0(a0, &v1);
    return a0[9];
}
```

## `sub_10319260` `0x10319260`

_22 bytes. (leaf/helper — see body)_

```c
int sub_10319260(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10319280(a0, &v1);
    return a0;
}
```

## `sub_10319280` `0x10319280`

_93 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    struct struct_0 *field_4;
    char field_8;
} struct_0;

typedef struct struct_0 {
    char padding_0[32];
    struct struct_1 *field_20;
    char padding_24[12];
    struct struct_1 *field_30;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

struct_0 * sub_10319280(struct_0 *idx)
{
    struct_0 *v3;  // eax
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    if (idx->field_4)
    {
        v1 = sub_103160c0(idx->field_4);
        v0 = sub_1032fd20();
        v3 = sub_10312db0(&v0, &v1);
        if (!*((char *)&v3))
        {
            idx->field_8 = 0;
            return v3;
        }
    }
    idx->field_4 = NULL;
    idx->field_8 = 1;
    return idx;
}
```

## `sub_103192e0` `0x103192e0`

_110 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    struct struct_0 **field_4;
    char field_8;
    char field_9;
} struct_0;

int sub_103192e0(struct_0 *idx)
{
    unsigned int v0;  // [bp-0xc]
    char v1[4];  // [bp-0x8]

    if (idx->field_4)
    {
        v1 = (char[4])sub_10315f80(idx->field_4);
        v0 = sub_1032fd20();
        if ((char)sub_10312db0(&v0, v1))
            goto LABEL_1031931f;
        idx->field_9 = sub_10312f00(v1);
    }
    else
    {
LABEL_1031931f:
        idx->field_4 = NULL;
    }
    idx->field_8 = 1;
    return _INSERT(idx, 0, idx->field_9);
}
```

## `sub_10319350` `0x10319350`

_565 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

extern unsigned int g_1038e180;

int sub_10319350(unsigned int a0, int a1, unsigned int a2, char *a3)
{
    unsigned long v17;  // ldt
    unsigned long v18;  // gdt
    unsigned short v19;  // fs
    unsigned long v20;  // 4137
    unsigned int v21;  // esi
    unsigned long v22;  // 4156
    char v23;  // al
    unsigned long v24;  // 4120
    unsigned int v0;  // [bp-0x5c]
    unsigned int v1;  // [bp-0x58]
    unsigned int v2;  // [bp-0x54]
    unsigned int v3;  // [bp-0x50]
    unsigned int v4;  // [bp-0x4c]
    unsigned int iter;  // [bp-0x48]
    char v6;  // [bp-0x41]
    unsigned int j;  // [bp-0x40]
    unsigned int v8;  // [bp-0x3c]
    unsigned int i;  // [bp-0x38]
    struct_0 v10;  // [bp-0x34]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]
    char v16;  // [bp-0x4]

    v15 = 4294967295;
    v14 = sub_1036afd8;
    v20 = _ccall(v17, v18, (unsigned int)v19, 0);
    v13 = *((int *)v20);
    v11 = g_1038e180 ^ &v16;
    v1 = v21;
    v0 = v11;
    v22 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((unsigned int **)v22) = &v13;
    for (i = 0; a3[i]; i += 1)
    {
        if (a3[i] == *(a3))
            a2 += 1;
    }
    sub_10317800(&v10, a2, 0);
    v15 = 0;
    v12 = 4294967294;
    v8 = 1;
    while (true)
    {
        v6 = 0;
        for (iter = 0; j < a2; j += 1)
        {
            for (j = 0; a3[iter] && a3[iter] != *(a3); iter += 1);
            if (*((char *)sub_103189a0(&v10, j)))
            {
                iter += *((char *)sub_103189a0(&v10, j));
            }
            else
            {
                iter += v8;
                if (a3[iter] == *(a3) || !a3[iter])
                {
                    v3 = (v8 < 127 ? v8 : 127);
                    *((char *)sub_103189a0(&v10, j)) = v3;
                    v12 = j;
                }
                else if ((char)sub_10319590(a0, a1) || (v23 = sub_10319230(a0), (int)(char)a3[iter] != (int)sub_10319230(a0)))
                {
                    v2 = (v8 < 127 ? v8 : 127);
                    *((char *)sub_103189a0(&v10, j)) = v2;
                }
                else
                {
                    v6 = 1;
                }
            }
        }
        if (!v6 || (char)sub_10319590(a0, a1))
            break;
        v8 += 1;
        sub_10319260(a0);
        v12 = 4294967295;
    }
    v4 = v12;
    v15 = 4294967295;
    sub_10314610(&v10);
    v24 = _ccall(v17, v18, (unsigned int)v19, 0);
    *((unsigned int *)v24) = v13;
    return sub_10351225();
}
```

## `sub_10319590` `0x10319590`

_17 bytes. (leaf/helper — see body)_

```c
int sub_10319590(unsigned int a0, int a1)
{
    char v0;  // [bp+0x0]

    return sub_103195d0(a1, &v0);
}
```

## `sub_103195b0` `0x103195b0`

_31 bytes. (leaf/helper — see body)_

```c
int sub_103195b0(unsigned int a0, int a1)
{
    return -(0 < (sub_10319590(a0, a1) & 0xff)) + 1;
}
```

## `sub_103195d0` `0x103195d0`

_108 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    struct struct_0 **field_4;
    char field_8;
    char field_9;
} struct_0;

char sub_103195d0(struct_0 *a0, struct_0 *a1)
{
    unsigned int v0;  // [bp-0xc]

    if (!a0->field_8)
        sub_103192e0(a0);
    if (!a1->field_8)
        sub_103192e0(a1);
    if ((a0->field_4 || a1->field_4) && (!a0->field_4 || !a1->field_4))
        v0 = 0;
    else
        v0 = 1;
    return v0;
}
```

## `sub_10319640` `0x10319640`

_41 bytes. (leaf/helper — see body)_

```c
unsigned int [4] sub_10319640(unsigned int *idx, unsigned int a1)
{
    unsigned int v1[2];  // eax
    unsigned int v2;  // edx
    char v0;  // [bp-0xc]

    v1 = sub_10317360(&v0, idx);
    v2 = v1[1];
    idx[2] = v1[0];
    idx[3] = v2;
    return idx;
}
```

## `sub_10319670` `0x10319670`

_10 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10319670(void)
{
    return 6;
}
```

## `sub_10319680` `0x10319680`

_8 bytes. (leaf/helper — see body)_

```c
int sub_10319680(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_10313e50(a0 - 40, v0);
}
```

## `sub_10319690` `0x10319690`

_8 bytes. (leaf/helper — see body)_

```c
int sub_10319690(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_10313e50(a0 - 20, v0);
}
```

## `sub_103196a0` `0x103196a0`

_8 bytes. (leaf/helper — see body)_

```c
int sub_103196a0(int a0)
{
    unsigned int v0;  // [bp+0x0]

    return sub_10313e80(a0 - 20, v0);
}
```

## `sub_103196b0` `0x103196b0`

_428 bytes. refs "Last recorded checkpoint was '", "', ", " line "_

```c
extern unsigned int g_1038e180;

void sub_103196b0(int a0, int a1, int a2)
{
    unsigned long v22;  // ldt
    unsigned long v23;  // gdt
    unsigned short v24;  // fs
    unsigned long v25;  // 4140
    unsigned long v26;  // 4154
    unsigned long v27;  // 4113
    int v0;  // [bp-0xe8]
    int v1;  // [bp-0xe4]
    int v2;  // [bp-0xe0]
    int v3;  // [bp-0xdc]
    int v4;  // [bp-0xd8]
    int v5;  // [bp-0xd4]
    int v6;  // [bp-0xd0]
    int v7;  // [bp-0xcc]
    int v8;  // [bp-0xc8]
    int v9;  // [bp-0xc4]
    int v10;  // [bp-0xc0]
    int v11;  // [bp-0xbc]
    char v12;  // [bp-0xb8]
    char v13;  // [bp-0x9c]
    char v14;  // [bp-0x80]
    char v15;  // [bp-0x64]
    char v16;  // [bp-0x48]
    char v17;  // [bp-0x2c]
    unsigned int v18;  // [bp-0x10]
    unsigned int v19;  // [bp-0xc]
    unsigned int v20;  // [bp-0x8], Other Possible Types: char
    char v21;  // [bp-0x4]

    v20 = 4294967295;
    v19 = sub_1036b036;
    v25 = _ccall(v22, v23, (unsigned int)v24, 0);
    v18 = *((int *)v25);
    v26 = _ccall(v22, v23, (unsigned int)v24, 0);
    *((unsigned int **)v26) = &v18;
    v11 = sub_1031a810(&v17, a2, g_1038e180 ^ &v21);
    v10 = v11;
    v20 = 0;
    v9 = sub_1031a540(&v16, "Last recorded checkpoint was '", a0, "', ", a1, " line ", v10);
    v8 = v9;
    v20 = 1;
    v7 = sub_1031a5d0(&v15, v8);
    v6 = v7;
    v20 = 2;
    v5 = sub_1031a780(&v14, v6);
    v4 = v5;
    v20 = 3;
    v3 = sub_1031a5d0(&v13, v4);
    v2 = v3;
    v20 = 4;
    v1 = sub_1031a780(&v12, v2);
    v0 = v1;
    v20 = 5;
    sub_10319f70(v0);
    v20 = 4;
    sub_10314610(&v12);
    v20 = 3;
    sub_10314610(&v13);
    v20 = 2;
    sub_10314610(&v14);
    v20 = 1;
    sub_10314610(&v15);
    v20 = 0;
    sub_10314610(&v16);
    v20 = 4294967295;
    sub_10314610(&v17);
    v27 = _ccall(v22, v23, (unsigned int)v24, 0);
    *((unsigned int *)v27) = v18;
    return;
}
```

## `sub_10319860` `0x10319860`

_275 bytes. refs "Unhandled Exception", "\n\n"_

```c
extern unsigned int g_1038e180;
extern int g_103a2288;

void sub_10319860(int a0)
{
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    unsigned short v14;  // fs
    unsigned long v15;  // 4137
    unsigned long v16;  // 4151
    unsigned long v17;  // 4113
    int v0;  // [bp-0x118]
    int v1;  // [bp-0x114]
    int v2;  // [bp-0x110]
    int v3;  // [bp-0x10c]
    char v4;  // [bp-0x108]
    char v5;  // [bp-0xec]
    char v6;  // [bp-0xd0]
    char v7;  // [bp-0x70]
    unsigned int v8;  // [bp-0x10]
    unsigned int v9;  // [bp-0xc]
    unsigned int v10;  // [bp-0x8], Other Possible Types: char
    char v11;  // [bp-0x4]

    v10 = 4294967295;
    v9 = sub_1036b07d;
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    v8 = *((int *)v15);
    v16 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int **)v16) = &v8;
    sub_103266a0("Unhandled Exception", g_1038e180 ^ &v11);
    v10 = 0;
    v3 = sub_1031a5d0(&v5, a0, "\n\n", &g_103a2288);
    v2 = v3;
    v10 = 1;
    v1 = sub_1031a780(&v4, v2);
    v0 = v1;
    v10 = 2;
    sub_10319e80(v0);
    v10 = 3;
    sub_1032a610(0, &v6, &v7, 16);
    v10 = 2;
    sub_10319f00();
    v10 = 1;
    sub_10314610(&v4);
    v10 = 0;
    sub_10314610(&v5);
    v10 = 4294967295;
    sub_10319f00();
    v17 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int *)v17) = v8;
    return;
}
```

## `sub_10319980` `0x10319980`

_217 bytes. refs ", '"_

```c
typedef struct struct_0 {
    char padding_0[4];
    struct struct_1 *field_4;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern unsigned int g_1038e180;

void sub_10319980(int a0, struct_0 **a1)
{
    unsigned long v13;  // ldt
    unsigned long v14;  // gdt
    unsigned short v15;  // fs
    unsigned long v16;  // 4141
    unsigned long v17;  // 4155
    unsigned long v18;  // 4113
    int v0;  // [bp-0x7c]
    int v1;  // [bp-0x78]
    int v2;  // [bp-0x74]
    int v3;  // [bp-0x70]
    int v4;  // [bp-0x6c]
    int v5;  // [bp-0x68]
    char v6;  // [bp-0x64]
    char v7;  // [bp-0x48]
    char v8;  // [bp-0x2c]
    unsigned int v9;  // [bp-0x10]
    unsigned int v10;  // [bp-0xc]
    unsigned int v11;  // [bp-0x8], Other Possible Types: char
    char v12;  // [bp-0x4]

    v11 = 4294967295;
    v10 = sub_1036b0b3;
    v16 = _ccall(v13, v14, (unsigned int)v15, 0);
    v9 = *((int *)v16);
    v17 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int **)v17) = &v9;
    v5 = sub_1031a5d0(&v8, a0, ", '", *(a1)->field_4("'", g_1038e180 ^ &v12));
    v4 = v5;
    v11 = 0;
    v3 = sub_1031a5d0(&v7, v4);
    v2 = v3;
    v11 = 1;
    v1 = sub_1031a5d0(&v6, v2);
    v0 = v1;
    v11 = 2;
    sub_10319860(v0);
    v11 = 1;
    sub_10314610(&v6);
    v11 = 0;
    sub_10314610(&v7);
    v11 = 4294967295;
    sub_10314610(&v8);
    v18 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int *)v18) = v9;
    return;
}
```

## `sub_10319a60` `0x10319a60`

_18 bytes. (leaf/helper — see body)_

```c
void sub_10319a60(void)
{
    char v0;  // [bp+0x0]

    sub_10353b3d(sub_10319a80, &v0);
    return;
}
```

## `sub_10319a80` `0x10319a80`

_705 bytes. refs "EXCEPTION_IN_PAGE_ERROR", "EXCEPTION_ILLEGAL_INSTRUCTION", "EXCEPTION_NONCONTINUABLE_EXCEPTION"_

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[1345428862];
    char field_50319d7e;
} struct_0;

extern unsigned int g_1038e180;
extern int g_1039a690;

void sub_10319a80(int a0, struct_1 **a1)
{
    unsigned long v23;  // ldt
    unsigned long v24;  // gdt
    unsigned short v25;  // fs
    unsigned long v26;  // 4185
    unsigned long v27;  // 4189
    unsigned long v28;  // 4114
    unsigned int v0;  // [bp-0xdc]
    int v1;  // [bp-0xd8]
    int v2;  // [bp-0xd4]
    int v3;  // [bp-0xd0]
    int v4;  // [bp-0xcc]
    int v5;  // [bp-0xc8]
    int v6;  // [bp-0xc4]
    int v7;  // [bp-0xc0]
    int v8;  // [bp-0xbc]
    struct_0 *v9;  // [bp-0xb8]
    unsigned int v10;  // [bp-0xb4]
    char v11;  // [bp-0xb0]
    char v12;  // [bp-0xa4]
    char v13;  // [bp-0x88]
    char v14;  // [bp-0x6c]
    char v15;  // [bp-0x50]
    int v16;  // [bp-0x34], Other Possible Types: unsigned int
    char v17;  // [bp-0x30]
    unsigned int v18;  // [bp-0x14]
    unsigned int v19;  // [bp-0x10]
    unsigned int v20;  // [bp-0xc]
    unsigned int v21;  // [bp-0x8], Other Possible Types: char
    char v22;  // [bp-0x4]

    v21 = 4294967295;
    v20 = sub_1036b0fc;
    v26 = _ccall(v23, v24, (unsigned int)v25, 0);
    v19 = *((int *)v26);
    v18 = g_1038e180 ^ &v22;
    v0 = v18;
    v27 = _ccall(v23, v24, (unsigned int)v25, 0);
    *((unsigned int **)v27) = &v19;
    v16 = 0;
    v9 = *(a1)->field_0;
    if (v9 > 0xc0000005)
    {
        switch (v9)
        {
        case -1073741818:
            v16 = "EXCEPTION_IN_PAGE_ERROR";
            break;
        case -1073741795:
            v16 = "EXCEPTION_ILLEGAL_INSTRUCTION";
            break;
        case -1073741787:
            v16 = "EXCEPTION_NONCONTINUABLE_EXCEPTION";
            break;
        case -1073741684:
            v16 = "EXCEPTION_ARRAY_BOUNDS_EXCEEDED";
            break;
        case -1073741683:
            v16 = "EXCEPTION_FLT_DENORMAL_OPERAND";
            break;
        case -1073741682:
            v16 = "EXCEPTION_FLT_DIVIDE_BY_ZERO";
            break;
        case -1073741681:
            v16 = "EXCEPTION_FLT_INEXACT_RESULT";
            break;
        case -1073741680:
            v16 = "EXCEPTION_FLT_INVALID_OPERATION";
            break;
        case -1073741679:
            v16 = "EXCEPTION_FLT_OVERFLOW";
            break;
        case -1073741678:
            v16 = "EXCEPTION_FLT_STACK_CHECK";
            break;
        case -1073741677:
            v16 = "EXCEPTION_FLT_UNDERFLOW";
            break;
        case -1073741676:
            v16 = "EXCEPTION_INT_DIVIDE_BY_ZERO";
            break;
        case -1073741675:
            v16 = "EXCEPTION_INT_OVERFLOW";
            break;
        case -1073741674:
            v16 = "EXCEPTION_PRIV_INSTRUCTION";
            break;
        case -1073741571:
            v16 = "EXCEPTION_STACK_OVERFLOW";
            break;
        default:
LABEL_10319bdb:
            v16 = "no further information available";
            break;
        }
    }
    else if (v9 == 0xc0000005)
    {
        v16 = "EXCEPTION_ACCESS_VIOLATION";
    }
    else if (v9 != 0x80000002)
    {
        if (v9 != 0x80000004)
            goto LABEL_10319bdb;
        v16 = "EXCEPTION_SINGLE_STEP";
    }
    else
    {
        v16 = "EXCEPTION_DATATYPE_MISALIGNMENT";
    }
    v8 = sub_1031a8e0(&v15, a0, " (", v16, ")");
    v7 = v8;
    v21 = 0;
    v6 = sub_1031a540(&v14, "C exception ", v7);
    v5 = v6;
    v21 = 1;
    v4 = sub_1031a5d0(&v13, v5);
    v3 = v4;
    v21 = 2;
    v2 = sub_1031a5d0(&v12, v3);
    v1 = v2;
    v21 = 3;
    sub_1031a5d0(&v17, v1);
    v21 = 5;
    sub_10314610(&v12);
    v21 = 6;
    sub_10314610(&v13);
    v21 = 7;
    sub_10314610(&v14);
    v21 = 8;
    sub_10314610(&v15);
    v10 = (unsigned int)sub_102ec9a0(&v17);
    sub_10353214(&v10);
    sub_103533ea(&v11, &g_1039a690);
    v21 = 4294967295;
    sub_10314610(&v17);
    v28 = _ccall(v23, v24, (unsigned int)v25, 0);
    *((unsigned int *)v28) = v19;
    sub_10351225();
    return;
}
```

## `sub_10319e80` `0x10319e80`

_114 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10319e80(int a0, int a1)
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
    char v2;  // [bp-0x8]
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v9 = *((int *)v8);
    v1 = *((int *)v8);
    v0 = a0;
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v10) = &v1;
    sub_1031a4d0(a1, g_1038e180 ^ &v3, a0, v9, sub_1036b14e, -1, &v4);
    sub_10319ff0(a1, g_1038e180 ^ &v3, a0, v9, sub_1036b14e, 0, &v4);
    v2 = 1;
    sub_1031a090();
    v11 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v11) = v9;
    return a0;
}
```

## `sub_10319f00` `0x10319f00`

_105 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10319f00(int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4140
    unsigned int v10;  // eax
    unsigned long v11;  // 4156
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
    v2 = 2;
    sub_1031a0e0(g_1038e180 ^ &v3, a0, v10, sub_1036b18e, 1, &v4);
    sub_1031a040(g_1038e180 ^ &v3, a0, v10, sub_1036b18e, 0, &v4);
    v2 = 4294967295;
    v12 = sub_10319f90();
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v10;
    return v12;
}
```

## `sub_10319f70` `0x10319f70`

_25 bytes. (leaf/helper — see body)_

```c
int sub_10319f70(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_1031a130(a1, a0, &v1);
}
```

## `sub_10319f90` `0x10319f90`

_86 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10319f90(int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4136
    unsigned int v10;  // eax
    unsigned long v11;  // 4152
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
    sub_1031a160(g_1038e180 ^ &v3, a0, v10, sub_1036b1bb, 0, &v4);
    v12 = sub_103388a0(g_1038e180 ^ &v3, a0, v10, sub_1036b1bb, -1, &v4);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v10;
    return v12;
}
```

## `sub_10319ff0` `0x10319ff0`

_78 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10319ff0(int a0)
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
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v9 = *((int *)v8);
    v1 = *((int *)v8);
    v0 = a0;
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v10) = &v1;
    sub_1031a1d0(g_1038e180 ^ &v2, a0, v9, sub_1036b1e8, -1, &v3);
    v11 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v11) = v9;
    return a0;
}
```

## `sub_1031a040` `0x1031a040`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_1031a040(int a0)
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
    v12 = sub_1031a1f0(g_1038e180 ^ &v3, a0, v10, sub_1036b218, -1, &v4);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v10;
    return v12;
}
```

## `sub_1031a090` `0x1031a090`

_78 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1031a090(int a0)
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
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v9 = *((int *)v8);
    v1 = *((int *)v8);
    v0 = a0;
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v10) = &v1;
    sub_1031a1d0(g_1038e180 ^ &v2, a0, v9, sub_1036b248, -1, &v3);
    v11 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v11) = v9;
    return a0;
}
```

## `sub_1031a0e0` `0x1031a0e0`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_1031a0e0(int a0)
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
    v12 = sub_1031a210(g_1038e180 ^ &v3, a0, v10, sub_1036b278, -1, &v4);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v10;
    return v12;
}
```

## `sub_1031a130` `0x1031a130`

_33 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

extern int g_1038fb14;

struct_0 * sub_1031a130(struct_0 *a0, struct_0 *a1)
{
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_10314660(v0, a1, 0, g_1038fb14);
}
```

## `sub_1031a160` `0x1031a160`

_97 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_1031a160(int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4136
    unsigned long v10;  // 4150
    unsigned int v11;  // eax
    unsigned long v12;  // 4113
    char v0;  // [bp-0x11]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]
    char v4;  // [bp-0x4]

    v3 = 4294967295;
    v2 = sub_1036b2a8;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v1 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v1;
    sub_1031a230(g_1038e180 ^ &v4, a0);
    v3 = 0;
    sub_1031a9e0(&v0);
    v3 = 4294967295;
    v11 = sub_1031a290(&v0);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v1;
    return v11;
}
```

## `sub_1031a1d0` `0x1031a1d0`

_20 bytes. (leaf/helper — see body)_

```c
char * sub_1031a1d0(char *a0)
{
    *(a0) = 0;
    return a0;
}
```

## `sub_1031a1f0` `0x1031a1f0`

_19 bytes. (leaf/helper — see body)_

```c
void sub_1031a1f0(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1031a2e0(a0, &v1);
    return;
}
```

## `sub_1031a210` `0x1031a210`

_19 bytes. (leaf/helper — see body)_

```c
void sub_1031a210(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1031a310(a0, &v1);
    return;
}
```

## `sub_1031a230` `0x1031a230`

_78 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1031a230(int a0)
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
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v9 = *((int *)v8);
    v1 = *((int *)v8);
    v0 = a0;
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v10) = &v1;
    sub_1031a280(g_1038e180 ^ &v2, a0, v9, sub_1036b2d8, -1, &v3);
    v11 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v11) = v9;
    return a0;
}
```

## `sub_1031a280` `0x1031a280`

_14 bytes. (leaf/helper — see body)_

```c
int sub_1031a280(unsigned int a0)
{
    return a0;
}
```

## `sub_1031a290` `0x1031a290`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_1031a290(int a0)
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
    v12 = sub_103388a0(g_1038e180 ^ &v3, a0, v10, sub_1036b308, -1, &v4);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v10;
    return v12;
}
```

## `sub_1031a2e0` `0x1031a2e0`

_35 bytes. (leaf/helper — see body)_

```c
char * sub_1031a2e0(char *a0)
{
    char *v2;  // eax
    char v0;  // [bp-0x6]

    v2 = a0;
    if (*(v2))
        v2 = sub_1031a340(_INSERT(0, 0, v0));
    return v2;
}
```

## `sub_1031a310` `0x1031a310`

_35 bytes. (leaf/helper — see body)_

```c
char * sub_1031a310(char *a0)
{
    char *v2;  // eax
    char v0;  // [bp-0x6]

    v2 = a0;
    if (*(v2))
        v2 = sub_1031a370(_INSERT(0, 0, v0));
    return v2;
}
```

## `sub_1031a340` `0x1031a340`

_34 bytes. (leaf/helper — see body)_

```c
char * sub_1031a340(char *a0)
{
    char *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10314610(sub_10331570(a0, &v1));
    *(a0) = 0;
    return a0;
}
```

## `sub_1031a370` `0x1031a370`

_34 bytes. (leaf/helper — see body)_

```c
char * sub_1031a370(char *a0)
{
    char *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10331570(a0, &v1);
    sub_1031a3a0(a0, &v1);
    *(a0) = 0;
    return a0;
}
```

## `sub_1031a3a0` `0x1031a3a0`

_23 bytes. (leaf/helper — see body)_

```c
void sub_1031a3a0(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1031a3c0(1, 0, a0, &v1);
    return;
}
```

## `sub_1031a3c0` `0x1031a3c0`

_118 bytes. (leaf/helper — see body)_

```c
int sub_1031a3c0(unsigned int *idx, char a1, int a2)
{
    unsigned int v0;  // [bp-0x8]

    if (a1 && idx[6] >= 8)
    {
        v0 = idx[1];
        if (a2 > 0)
            sub_1031a9b0(idx + 1, 8, v0, a2);
        sub_1033e3d0(v0, idx[6] + 1);
    }
    idx[6] = 7;
    return sub_1031a440(a2);
}
```

## `sub_1031a440` `0x1031a440`

_57 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
} struct_0;

int sub_1031a440(struct_0 *a0, unsigned int a1)
{
    unsigned short v0;  // [bp-0x6]

    v0 = 0;
    a0->field_14 = a1;
    return sub_1031a480(sub_1031a4a0(&v0, a0) + a1 * 2);
}
```

## `sub_1031a480` `0x1031a480`

_17 bytes. (leaf/helper — see body)_

```c
unsigned short * sub_1031a480(unsigned short *a0, unsigned short *a1)
{
    *(a0) = *(a1);
    return a0;
}
```

## `sub_1031a4a0` `0x1031a4a0`

_45 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    struct struct_0 *field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

struct_0 * sub_1031a4a0(struct_0 *a0)
{
    struct_0 *v0;  // [bp-0xc]

    v0 = (a0->field_18 < 8 ? (struct struct_0 *)&a0->field_4 : a0->field_4);
    return v0;
}
```

## `sub_1031a4d0` `0x1031a4d0`

_108 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_1031a4d0(unsigned int a0, int a1)
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
    v3 = sub_1036b33b;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_1031a280(a0 + 4);
    v4 = 0;
    v1 = 0;
    sub_1031aa70(a1, 1, _INSERT(0, 0, v1));
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v2;
    return a0;
}
```

## `sub_1031a540` `0x1031a540`

_132 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1031a540(int a0, int a1, int a2)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4142
    unsigned long v13;  // 4156
    unsigned long v15;  // 4117
    unsigned int v0;  // [bp-0x3c]
    int v1;  // [bp-0x38]
    int v2;  // [bp-0x34]
    unsigned int v3;  // [bp-0x30]
    char v4;  // [bp-0x2c]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    char v7;  // [bp-0x8], Other Possible Types: unsigned int
    char v8;  // [bp-0x4]

    v7 = 4294967295;
    v6 = sub_1036b381;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v5 = *((int *)v12);
    v0 = g_1038e180 ^ &v8;
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v5;
    v3 = 0;
    v2 = sub_10314590(&v4, a1);
    v1 = v2;
    v7 = 1;
    sub_103145d0(a0, sub_10316de0(v1, a2));
    v3 |= 1;
    v7 = 0;
    sub_10314610(&v4);
    v15 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v15) = v5;
    return a0;
}
```

## `sub_1031a5d0` `0x1031a5d0`

_132 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1031a5d0(int a0, int a1, int a2)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4142
    unsigned long v10;  // 4156
    unsigned long v12;  // 4117
    unsigned int v0;  // [bp-0x30]
    char v1;  // [bp-0x2c]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036b3c1;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_103145d0(&v1, a1);
    v4 = 1;
    sub_103145d0(a0, sub_1031a660(a2, g_1038e180 ^ &v5, sub_103145d0(&v1, a1), sub_103145d0(&v1, a1), 0, v1));
    v0 = 1;
    v4 = 0;
    sub_10314610(&v1);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v2;
    return a0;
}
```

## `sub_1031a660` `0x1031a660`

_25 bytes. (leaf/helper — see body)_

```c
int sub_1031a660(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_1031a680(a1, a0, &v1);
}
```

## `sub_1031a680` `0x1031a680`

_38 bytes. (leaf/helper — see body)_

```c
int sub_1031a680(unsigned int a0, int a1)
{
    unsigned int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_1031a6b0(a1, sub_103136c0(a1));
}
```

## `sub_1031a6b0` `0x1031a6b0`

_206 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

extern unsigned int g_1038fb14;

unsigned int [7] sub_1031a6b0(unsigned int *a0, unsigned int a1, int a2)
{
    struct_0 *v1;  // eax
    unsigned int v0;  // [bp-0x8]

    if (sub_10314c60(a0, a1))
        return sub_10316e30(a0, a0, a1 - (char *)sub_10314a50(a0), a2);
    if (g_1038fb14 - a0[5] > a2 && a0[5] + a2 >= a0[5])
    {
        if (a2 <= 0)
            return a0;
        v0 = a0[5] + a2;
        if ((char)sub_103149b0(a0, v0, 0))
        {
            v1 = sub_10314a50(a0);
            sub_10313350(&v1->padding_0[a0[5]], a0[6] - a0[5], a1, a2);
            sub_10314960(a0, v0);
        }
        return a0;
    }
    sub_1035039e();
}
```

## `sub_1031a780` `0x1031a780`

_132 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1031a780(int a0, int a1, int a2)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4142
    unsigned long v13;  // 4156
    unsigned long v15;  // 4117
    unsigned int v0;  // [bp-0x3c]
    int v1;  // [bp-0x38]
    int v2;  // [bp-0x34]
    unsigned int v3;  // [bp-0x30]
    char v4;  // [bp-0x2c]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    char v7;  // [bp-0x8], Other Possible Types: unsigned int
    char v8;  // [bp-0x4]

    v7 = 4294967295;
    v6 = sub_1036b401;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v5 = *((int *)v12);
    v0 = g_1038e180 ^ &v8;
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v5;
    v3 = 0;
    v2 = sub_103145d0(&v4, a1);
    v1 = v2;
    v7 = 1;
    sub_103145d0(a0, sub_10316de0(v1, a2));
    v3 |= 1;
    v7 = 0;
    sub_10314610(&v4);
    v15 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v15) = v5;
    return a0;
}
```

## `sub_1031a810` `0x1031a810`

_104 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1031a810(unsigned int a0, unsigned int a1, int a2)
{
    unsigned long v11;  // ldt
    unsigned long v12;  // gdt
    unsigned short v13;  // fs
    unsigned long v14;  // 4150
    unsigned int v15;  // eax
    unsigned long v16;  // 4174
    unsigned long v17;  // 4119
    unsigned int v0;  // [bp-0x28]
    int v1;  // [bp-0x24]
    int v2;  // [bp-0x20]
    int v3;  // [bp-0x1c]
    unsigned int v4;  // [bp-0x18]
    unsigned int v5;  // [bp-0x14]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0x8]
    char v8;  // [bp-0x4]
    char v9;  // [bp+0x0]
    char v10;  // [bp+0x8]

    v7 = 4294967295;
    v14 = _ccall(v11, v12, (unsigned int)v13, 0);
    v15 = *((int *)v14);
    v6 = *((int *)v14);
    v5 = a0;
    v4 = a0;
    v0 = g_1038e180 ^ &v8;
    v16 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int **)v16) = &v6;
    sub_1031aaa0(a2, &v10, g_1038e180 ^ &v8, v1, v2, v3, 0, &v0, v15, sub_1036b439, 1, &v9);
    v4 = 1;
    v17 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int *)v17) = v15;
    return a2;
}
```

## `sub_1031a866` `0x1031a866`

_30 bytes. (leaf/helper — see body)_

```c
int sub_1031a866(void)
{
    unsigned int v1;  // [bp+0xffff0]
    unsigned int v2;  // [bp+0x100000]
    unsigned int v3;  // [bp+0x10000c]

    sub_10315800(v3);
    v1 |= 1;
    v2 = 0;
    return sub_1031a8be;
}
```

## `sub_1031a884` `0x1031a884`

_6 bytes. (leaf/helper — see body)_

```c
int sub_1031a884(void)
{
    return sub_1031a8ae;
}
```

