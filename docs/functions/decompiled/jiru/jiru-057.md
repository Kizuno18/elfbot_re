# elfbot.dll decompiled — jiru 0x1034af89..0x1034ffca

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1034af89` `0x1034af89`

_141 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
    char padding_8[12];
    unsigned int field_14;
    unsigned int field_18;
    char padding_1c[132];
    unsigned int field_a0;
    char padding_a4[20];
    struct struct_1 *field_b8;
} struct_0;

typedef struct struct_1 {
    unsigned short field_0;
} struct_1;

extern unsigned int g_1034af79;

int sub_1034af89(void)
{
    void* v3;  // ebp
    void* v0;  // [bp-0x18]
    unsigned int *v1;  // [bp+0x4]
    struct_0 *idx;  // [bp+0xc]

    if (*(v1) != 2147483652)
    {
        if (*(v1) != 3221225501)
        {
            v3 = v0;
        }
        else
        {
            *((unsigned int *)&v3[12]) = 1;
            if (idx->field_b8->field_0 == 53263)
            {
                idx->field_14 = 0;
                idx->field_4 = &g_1034af79;
                idx->field_18 = 1281;
                idx->field_b8 = idx->field_b8 + 1;
                return;
            }
        }
        *((unsigned int *)&v3[4]) = 1;
        return;
    }
    else
    {
        *((unsigned int *)&v3[8]) = 1;
        if (((char)idx->field_14 & 1) == 1)
        {
            idx->field_a0 = 1;
            idx->field_b8 = sub_1034af7b;
        }
        idx->field_4 = 0;
        idx->field_14 = 0;
        idx->field_18 = 0x400;
        return;
    }
}
```

## `sub_1034b03f` `0x1034b03f`

_34 bytes. (leaf/helper — see body)_

```c
int sub_1034b03f(void)
{
    unsigned int idx[6];  // eax
    unsigned int v2;  // edx

    *((char *)(idx[2] + idx[5])) = v2 >> 8;
    idx[5] = idx[5] + 1;
    *((char *)(idx[5] + idx[2])) = v2;
    idx[5] = idx[5] + 1;
    return;
}
```

## `sub_1034b061` `0x1034b061`

_77 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    int field_c;
    int field_10;
    unsigned int field_14;
    char padding_18[4];
    struct struct_1 *field_1c;
} struct_0;

typedef struct struct_1 {
    char padding_0[8];
    unsigned int field_8;
    char padding_c[4];
    unsigned int field_10;
    unsigned int field_14;
} struct_1;

int sub_1034b061(void)
{
    struct_0 *idx;  // eax
    unsigned int v2[6];  // eax
    int v3;  // ecx
    unsigned int v4;  // edi
    unsigned int v5;  // edi
    unsigned int idx1[6];  // eax
    unsigned int index[6];  // esi

    v2 = idx->field_1c;
    v3 = idx->field_10;
    v4 = v2[5];
    v5 = v4;
    if (v2[5] > idx->field_10)
        v5 = v3;
    if (!v5)
        return;
    sub_10350b50(idx->field_c, v2[4], v5);
    idx1 = idx->field_1c;
    idx->field_c = idx->field_c + v5;
    idx1[4] = idx1[4] + v5;
    idx->field_14 = idx->field_14 + v5;
    idx->field_10 = idx->field_10 - v5;
    idx->field_1c->field_14 = idx->field_1c->field_14 - v5;
    index = idx->field_1c;
    if (index[5])
        return;
    index[4] = index[2];
    return;
}
```

## `sub_1034b0ae` `0x1034b0ae`

_1903 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_1 *field_0;
    unsigned int field_4;
    int field_8;
    unsigned int field_c;
    char padding_10[4];
    unsigned int field_14;
    int field_18;
    void* field_1c;
    unsigned int field_20;
    char padding_24[4];
    int field_28;
    char padding_2c[24];
    int field_44;
    char padding_48[4];
    unsigned int field_4c;
    char padding_50[28];
    unsigned int field_6c;
    char padding_70[4];
    unsigned int field_74;
    char padding_78[12];
    int field_84;
    int field_88;
} struct_0;

typedef struct struct_1 {
} struct_1;

extern unsigned int g_10390d38[4];
extern unsigned int g_103942e0;
extern unsigned int g_103942ec;

unsigned int sub_1034b0ae(unsigned int a0, unsigned int a1, void* index, int a3)
{
    struct_0 *idx;  // esi
    int v4;  // ecx
    unsigned int v13;  // eax
    unsigned int v14;  // eax
    unsigned int v15;  // edx
    unsigned int v16;  // eax
    unsigned int v17;  // edx
    int v18;  // ecx
    unsigned int v19;  // eax
    unsigned int v5;  // eax
    int v6;  // edx
    int v7;  // ecx
    void* v8;  // eax
    char v9;  // al
    char v10;  // al
    unsigned int v11;  // ecx
    void* i;  // eax
    unsigned int v0;  // [bp-0x1c]
    int v1;  // [bp-0xc], Other Possible Types: unsigned int
    unsigned int j;  // [bp-0x8]

    j = a0;
    v1 = a0;
    if (index)
    {
        idx = (int)index[28];
        if (idx)
        {
            v4 = a3;
            if (v4 <= 4)
            {
                if ((int)index[12] && (*((int *)index) || !(int)index[4]))
                {
                    v5 = idx->field_4;
                    if (v5 != 666 || v4 == 4)
                    {
                        if ((int)index[16])
                        {
                            v6 = idx->field_28;
                            idx->field_0 = index;
                            v1 = v6;
                            idx->field_28 = v4;
                            if (v5 == 42)
                            {
                                if (idx->field_18 == 2)
                                {
                                    *((unsigned int *)&index[48]) = sub_1034ddc8(0, 0, 0);
                                    *((char *)(idx->field_8 + idx->field_14)) = 31;
                                    v7 = idx->field_8;
                                    idx->field_14 = idx->field_14 + 1;
                                    *((char *)(idx->field_14 + v7)) = 139;
                                    idx->field_14 = idx->field_14 + 1;
                                    *((char *)(idx->field_14 + idx->field_8)) = 8;
                                    idx->field_14 = idx->field_14 + 1;
                                    v8 = idx->field_1c;
                                    if (!v8)
                                    {
                                        *((char *)(idx->field_14 + idx->field_8)) = 0;
                                        idx->field_14 = idx->field_14 + 1;
                                        *((char *)(idx->field_14 + idx->field_8)) = 0;
                                        idx->field_14 = idx->field_14 + 1;
                                        *((char *)(idx->field_14 + idx->field_8)) = 0;
                                        idx->field_14 = idx->field_14 + 1;
                                        *((char *)(idx->field_14 + idx->field_8)) = 0;
                                        idx->field_14 = idx->field_14 + 1;
                                        *((char *)(idx->field_14 + idx->field_8)) = 0;
                                        idx->field_14 = idx->field_14 + 1;
                                        if (idx->field_84 == 9)
                                        {
                                            v0 = 2;
                                            goto LABEL_1034b1d7;
                                        }
                                        else if (idx->field_88 < 2 && idx->field_84 >= 2)
                                        {
                                            v9 = 0;
                                        }
                                        else
                                        {
                                            v0 = 4;
LABEL_1034b1d7:
                                            v9 = v0;
                                        }
                                        *((char *)(idx->field_14 + idx->field_8)) = v9;
                                        idx->field_14 = idx->field_14 + 1;
                                        *((char *)(idx->field_14 + idx->field_8)) = 11;
                                        idx->field_14 = idx->field_14 + 1;
                                        idx->field_4 = 113;
                                    }
                                    else
                                    {
                                        *((char *)(idx->field_14 + idx->field_8)) = (char)((unsigned int)((!(int)v8[36]) + 1) & 16) + ((char)((!(int)v8[44]) + 1) & 2) + ((char)((!(int)v8[28]) + 1) & 8) + (char)((unsigned int)((!(int)v8[16]) + 1) & 4) + (*((int *)v8));
                                        idx->field_14 = idx->field_14 + 1;
                                        *((char *)(idx->field_14 + idx->field_8)) = (char)idx->field_1c[4];
                                        idx->field_14 = idx->field_14 + 1;
                                        *((char *)(idx->field_14 + idx->field_8)) = (char)idx->field_1c[5];
                                        idx->field_14 = idx->field_14 + 1;
                                        *((char *)(idx->field_14 + idx->field_8)) = (char)idx->field_1c[6];
                                        idx->field_14 = idx->field_14 + 1;
                                        *((char *)(idx->field_14 + idx->field_8)) = (char)idx->field_1c[7];
                                        idx->field_14 = idx->field_14 + 1;
                                        if (idx->field_84 == 9)
                                        {
                                            v0 = 2;
                                            goto LABEL_1034b2ae;
                                        }
                                        else if (idx->field_88 < 2 && idx->field_84 >= 2)
                                        {
                                            v10 = 0;
                                        }
                                        else
                                        {
                                            v0 = 4;
LABEL_1034b2ae:
                                            v10 = v0;
                                        }
                                        *((char *)(idx->field_14 + idx->field_8)) = v10;
                                        idx->field_14 = idx->field_14 + 1;
                                        *((char *)(idx->field_14 + idx->field_8)) = (char)idx->field_1c[12];
                                        idx->field_14 = idx->field_14 + 1;
                                        v11 = idx->field_14;
                                        if ((int)idx->field_1c[16])
                                        {
                                            *((char *)(v11 + idx->field_8)) = (char)idx->field_1c[20];
                                            idx->field_14 = idx->field_14 + 1;
                                            *((char *)(idx->field_14 + idx->field_8)) = (char)idx->field_1c[21];
                                            idx->field_14 = idx->field_14 + 1;
                                            v11 = idx->field_14;
                                        }
                                        if ((int)idx->field_1c[44])
                                            *((unsigned int *)&index[48]) = sub_1034ddc8((int)index[48], idx->field_8, v11);
                                        idx->field_20 = 0;
                                        idx->field_4 = 69;
                                    }
                                }
                                else
                                {
                                    v0 = 31;
                                    idx->field_4 = 113;
                                    sub_1034b03f();
                                    if (idx->field_6c)
                                    {
                                        sub_1034b03f();
                                        sub_1034b03f();
                                    }
                                    *((unsigned int *)&index[48]) = sub_1034dde2(0, 0, 0);
                                }
                            }
                            if (idx->field_4 == 69)
                            {
                                i = idx->field_1c;
                                if ((int)i[16])
                                {
                                    for (index = idx->field_14; idx->field_20 < (short)i[20]; i = idx->field_1c)
                                    {
                                        v13 = idx->field_14;
                                        if (v13 == idx->field_c)
                                        {
                                            if ((int)idx->field_1c[44] && v13 > index)
                                                *((unsigned int *)&index[48]) = sub_1034ddc8((int)index[48], idx->field_8 + index, v13 - index);
                                            sub_1034b061();
                                            v13 = idx->field_14;
                                            index = v13;
                                            if (v13 == idx->field_c)
                                                break;
                                        }
                                        *((char *)(v13 + idx->field_8)) = *((char *)((int)idx->field_1c[16] + idx->field_20));
                                        idx->field_14 = idx->field_14 + 1;
                                        idx->field_20 = idx->field_20 + 1;
                                    }
                                    if ((int)idx->field_1c[44] && idx->field_14 > index)
                                        *((unsigned int *)&index[48]) = sub_1034ddc8((int)index[48], idx->field_8 + index, idx->field_14 - index);
                                    if (idx->field_20 != (int)idx->field_1c[20])
                                        goto LABEL_1034b471;
                                    idx->field_20 = 0;
                                }
                                idx->field_4 = 73;
                            }
LABEL_1034b471:
                            if (idx->field_4 == 73)
                            {
                                if ((int)idx->field_1c[28])
                                {
                                    index = idx->field_14;
                                    do
                                    {
                                        v14 = idx->field_14;
                                        if (v14 != idx->field_c)
                                            continue;
                                        if ((int)idx->field_1c[44] && v14 > index)
                                            *((unsigned int *)&index[48]) = sub_1034ddc8((int)index[48], idx->field_8 + index, v14 - index);
                                        sub_1034b061();
                                        v14 = idx->field_14;
                                        index = v14;
                                        if (v14 == idx->field_c)
                                        {
                                            j = 1;
                                            break;
                                        }
                                        v15 = *((char *)((int)idx->field_1c[28] + idx->field_20));
                                        idx->field_20 = idx->field_20 + 1;
                                        *((char *)(v14 + idx->field_8)) = v15;
                                        idx->field_14 = idx->field_14 + 1;
                                        j = v15;
                                    } while (j);
                                    if ((int)idx->field_1c[44] && idx->field_14 > index)
                                        *((unsigned int *)&index[48]) = sub_1034ddc8((int)index[48], idx->field_8 + index, idx->field_14 - index);
                                    if (j)
                                        goto LABEL_1034b52f;
                                    idx->field_20 = 0;
                                }
                                idx->field_4 = 91;
                            }
LABEL_1034b52f:
                            if (idx->field_4 == 91)
                            {
                                if ((int)idx->field_1c[36])
                                {
                                    index = idx->field_14;
                                    do
                                    {
                                        v16 = idx->field_14;
                                        if (v16 != idx->field_c)
                                            continue;
                                        if ((int)idx->field_1c[44] && v16 > index)
                                            *((unsigned int *)&index[48]) = sub_1034ddc8((int)index[48], idx->field_8 + index, v16 - index);
                                        sub_1034b061();
                                        v16 = idx->field_14;
                                        index = v16;
                                        if (v16 == idx->field_c)
                                        {
                                            j = 1;
                                            break;
                                        }
                                        v17 = *((char *)((int)idx->field_1c[36] + idx->field_20));
                                        idx->field_20 = idx->field_20 + 1;
                                        *((char *)(v16 + idx->field_8)) = v17;
                                        idx->field_14 = idx->field_14 + 1;
                                        j = v17;
                                    } while (j);
                                    if ((int)idx->field_1c[44] && idx->field_14 > index)
                                        *((unsigned int *)&index[48]) = sub_1034ddc8((int)index[48], idx->field_8 + index, idx->field_14 - index);
                                    if (j)
                                        goto LABEL_1034b5ea;
                                }
                                idx->field_4 = 103;
                            }
LABEL_1034b5ea:
                            if (idx->field_4 == 103)
                            {
                                if ((int)idx->field_1c[44])
                                {
                                    if (idx->field_14 + 2 > idx->field_c)
                                        sub_1034b061();
                                    if (idx->field_14 + 2 > idx->field_c)
                                        goto LABEL_1034b644;
                                    *((char *)(idx->field_14 + idx->field_8)) = (char)index[48];
                                    idx->field_14 = idx->field_14 + 1;
                                    *((char *)(idx->field_14 + idx->field_8)) = (char)index[49];
                                    idx->field_14 = idx->field_14 + 1;
                                    *((unsigned int *)&index[48]) = sub_1034ddc8(0, 0, 0);
                                }
                                idx->field_4 = 113;
                            }
LABEL_1034b644:
                            if (idx->field_14)
                            {
                                sub_1034b061();
                                if (!(int)index[16])
                                {
                                    idx->field_28 = -1;
                                    return 0;
                                }
LABEL_1034b677:
                                v18 = a3;
LABEL_1034b67a:
                                if (idx->field_4 != 666)
                                {
                                    if (!(int)index[4])
                                    {
LABEL_1034b693:
                                        if (!idx->field_74 && (!v18 || idx->field_4 == 666))
                                            goto LABEL_1034b736;
                                    }
                                    v19 = g_10390d38[3 * idx->field_84](idx, a3);
                                    if (v19 == 2 || v19 == 3)
                                        idx->field_4 = 666;
                                    if (v19 && v19 != 2)
                                    {
                                        if (v19 == 1)
                                        {
                                            if (a3 == 1)
                                            {
                                                sub_1034f357(idx);
                                            }
                                            else
                                            {
                                                sub_1034f2cc(idx, 0, 0, 0);
                                                if (a3 == 3)
                                                {
                                                    *((unsigned short *)(idx->field_44 + idx->field_4c * 2 - 2)) = 0;
                                                    sub_10350ad0(idx->field_44, 0, idx->field_4c * 2 - 2);
                                                }
                                            }
                                            sub_1034b061();
                                            if (!(int)index[16])
                                            {
                                                idx->field_28 = -1;
                                                return 0;
                                            }
                                        }
                                    }
                                    else
                                    {
                                        if (!(int)index[16])
                                        {
                                            idx->field_28 = -1;
                                            return 0;
                                        }
                                        return 0;
                                    }
LABEL_1034b736:
                                    if (a3 != 4)
                                        return 0;
                                    if (idx->field_18 <= NULL)
                                        return 1;
                                    if (idx->field_18 == 2)
                                    {
                                        *((char *)(idx->field_8 + idx->field_14)) = (char)index[48];
                                        idx->field_14 = idx->field_14 + 1;
                                        *((char *)(idx->field_14 + idx->field_8)) = (char)index[49];
                                        idx->field_14 = idx->field_14 + 1;
                                        *((char *)(idx->field_14 + idx->field_8)) = (char)index[50];
                                        idx->field_14 = idx->field_14 + 1;
                                        *((char *)(idx->field_14 + idx->field_8)) = (char)index[0x33];
                                        idx->field_14 = idx->field_14 + 1;
                                        *((char *)(idx->field_14 + idx->field_8)) = (char)index[8];
                                        idx->field_14 = idx->field_14 + 1;
                                        *((char *)(idx->field_14 + idx->field_8)) = (char)index[9];
                                        idx->field_14 = idx->field_14 + 1;
                                        *((char *)(idx->field_14 + idx->field_8)) = (char)index[10];
                                        idx->field_14 = idx->field_14 + 1;
                                        *((char *)(idx->field_14 + idx->field_8)) = (char)index[11];
                                        idx->field_14 = idx->field_14 + 1;
                                    }
                                    else
                                    {
                                        sub_1034b03f();
                                        sub_1034b03f();
                                    }
                                    sub_1034b061();
                                    if (idx->field_18 <= NULL)
                                        return !idx->field_14;
                                    idx->field_18 = -(idx->field_18);
                                    return !idx->field_14;
                                }
                                else if (!(int)index[4])
                                {
                                    goto LABEL_1034b693;
                                }
                            }
                            else
                            {
                                if ((int)index[4])
                                    goto LABEL_1034b677;
                                v18 = a3;
                                if (v18 > v1 || v18 == 4)
                                    goto LABEL_1034b67a;
                            }
                        }
                        *((unsigned int *)&index[24]) = g_103942ec;
                        v0 = 4294967291;
                        return v0;
                    }
                }
                *((unsigned int *)&index[24]) = g_103942e0;
            }
        }
    }
    v0 = 4294967294;
    return v0;
}
```

## `sub_1034b81d` `0x1034b81d`

_173 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[28];
    struct struct_1 *field_1c;
    char padding_20[4];
    struct struct_2 *field_24;
    unsigned int field_28;
} struct_0;

typedef struct struct_1 {
    char padding_0[4];
    unsigned int field_4;
    unsigned int field_8;
    char padding_c[44];
    unsigned int field_38;
    char padding_3c[4];
    unsigned int field_40;
    unsigned int field_44;
} struct_1;

typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

unsigned int sub_1034b81d(struct_0 *idx)
{
    unsigned int v1[18];  // eax
    unsigned int v2;  // edi
    unsigned int v0;  // [bp-0xc]

    if (idx && !((v1 = (unsigned int [18])idx->field_1c, !v1 || (v2 = v1[1], v2 != 42 && v2 != 69 && v2 != 73 && v2 != 91 && v2 != 103 && v2 != 113 && v2 != 666))))
    {
        if (v1[2])
            idx->field_24(idx->field_28, v1[2]);
        if (idx->field_1c->field_44)
            idx->field_24(idx->field_28, idx->field_1c->field_44);
        if (idx->field_1c->field_40)
            idx->field_24(idx->field_28, idx->field_1c->field_40);
        if (idx->field_1c->field_38)
            idx->field_24(idx->field_28, idx->field_1c->field_38);
        idx->field_24(idx->field_28, idx->field_1c);
        idx->field_1c = NULL;
        if (v2 != 113)
            return 0;
        v0 = 4294967293;
    }
    else
    {
        v0 = 4294967294;
    }
    return v0;
}
```

## `sub_1034b8ca` `0x1034b8ca`

_99 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    int field_0;
    int field_4;
    unsigned int field_8;
    char padding_c[16];
    struct struct_0 *field_1c;
    char padding_20[16];
    int field_30;
} struct_1;

typedef struct struct_0 {
    char padding_0[24];
    unsigned int field_18;
} struct_0;

int sub_1034b8ca(int a0, int a1)
{
    struct_1 *idx;  // esi
    int v2;  // edi
    unsigned int v3;  // eax

    v2 = idx->field_4;
    if (idx->field_4 > a1)
        v2 = a1;
    if (!v2)
        return 0;
    idx->field_4 = idx->field_4 - v2;
    if (idx->field_1c->field_18 == 1)
    {
        v3 = sub_1034dde2(idx->field_30, idx->field_0, v2);
    }
    else if (idx->field_1c->field_18 == 2)
    {
        v3 = sub_1034ddc8(idx->field_30, idx->field_0, v2);
    }
    else
    {
        sub_10350b50(a0, idx->field_0, v2);
        idx->field_0 = idx->field_0 + v2;
        idx->field_8 = idx->field_8 + v2;
        return v2;
    }
    idx->field_30 = v3;
    sub_10350b50(a0, idx->field_0, v2);
    idx->field_0 = idx->field_0 + v2;
    idx->field_8 = idx->field_8 + v2;
    return v2;
}
```

## `sub_1034b92d` `0x1034b92d`

_126 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[44];
    unsigned int field_2c;
    char padding_30[12];
    unsigned int field_3c;
    char padding_40[4];
    int field_44;
    unsigned int field_48;
    unsigned int field_4c;
    char padding_50[12];
    unsigned int field_5c;
    unsigned int field_60;
    char padding_64[4];
    unsigned int field_68;
    unsigned int field_6c;
    char padding_70[4];
    unsigned int field_74;
    unsigned int field_78;
    unsigned int field_7c;
    unsigned int field_80;
    unsigned int field_84;
    char padding_88[4];
    unsigned int field_8c;
    unsigned int field_90;
} struct_0;

extern unsigned short g_10390d30[4];
extern unsigned short g_10390d32[4];
extern unsigned short g_10390d34[4];
extern unsigned short g_10390d36[4];

unsigned int sub_1034b92d(void)
{
    struct_0 *idx;  // esi
    int v3;  // ecx
    unsigned int v4;  // eax
    int v0;  // [bp-0x4]

    v3 = idx->field_44;
    idx->field_3c = idx->field_2c * 2;
    *((unsigned short *)(v3 + idx->field_4c * 2 - 2)) = 0;
    sub_10350ad0(idx->field_44, 0, idx->field_4c * 2 - 2, v0);
    v4 = idx->field_84 * 12;
    idx->field_80 = *((short *)(v4 + (char *)&g_10390d32[0]));
    idx->field_8c = *((short *)(v4 + (char *)&g_10390d30[0]));
    idx->field_90 = *((short *)(v4 + (char *)&g_10390d34[0]));
    idx->field_7c = *((short *)(v4 + (char *)&g_10390d36[0]));
    idx->field_6c = 0;
    idx->field_5c = 0;
    idx->field_74 = 0;
    idx->field_68 = 0;
    idx->field_48 = 0;
    idx->field_78 = 2;
    idx->field_60 = 2;
    return 2;
}
```

## `sub_1034b9ab` `0x1034b9ab`

_325 bytes. (leaf/helper — see body)_

```c
int sub_1034b9ab(unsigned int *idx, unsigned int a1, unsigned int a2)
{
    unsigned int v6;  // esi
    void* v7;  // edx
    char *v16;  // esi
    char *v17;  // esi
    char *v18;  // esi
    char *v19;  // esi
    char *v20;  // esi
    char *v21;  // esi
    unsigned int v22;  // eax
    void* v23;  // esi
    unsigned int v24;  // eax
    unsigned int v8;  // edi
    unsigned int v9;  // eax
    char *v10;  // esi
    char *v11;  // esi
    void* v12;  // ebx
    void* iter;  // edx
    char *v14;  // esi
    char *v15;  // esi
    void* v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int node;  // [bp-0xc]
    char v4;  // [bp-0x6]
    char v5;  // [bp-0x5]

    node = idx[31];
    v6 = idx[27];
    v2 = idx[36];
    v7 = idx[14] + v6;
    v8 = idx[30];
    v1 = (v6 <= idx[11] - 262 ? 0 : v6 - idx[11] + 262);
    v0 = v7 + 258;
    v5 = *(-1 + v8 + (char *)v7);
    v4 = *(v8 + (char *)v7);
    if (v8 >= idx[35])
        node >>= 2;
    if (v2 > idx[29])
        v2 = idx[29];
    v9 = a2;
    do
    {
        v10 = idx[14] + v9;
        if (v10[v8] != v4 || v10[1 + v8] != v5 || *(v10) != *((char *)v7) || (v11 = v10 + 1, *(v11) != (char)v7[1]))
            continue;
        v12 = v0;
        iter = v7 + 2;
        v14 = v11 + 1;
        do
        {
            iter += 1;
            v15 = v14 + 1;
        } while (...);
        v22 = iter - v12 + 258;
        v7 = v12 - 258;
        if (v22 <= v8)
            continue;
        idx[28] = a2;
        v8 = v22;
        if (v8 >= v2)
            break;
        v23 = v8 + v7;
        v5 = (char)v23[1];
        v4 = *((char *)v23);
        v9 = *((short *)(idx[16] + (idx[13] & a2) * 2));
        a2 = v9;
    } while (v9 > v1 && (node -= 1, node = node, node != 1));
    v24 = idx[29];
    if (v8 <= idx[29])
        v24 = v8;
    return v24;
}
```

## `sub_1034baf0` `0x1034baf0`

_138 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[56];
    unsigned int field_38;
    char padding_3c[48];
    unsigned int field_6c;
    unsigned int field_70;
    int field_74;
} struct_0;

int sub_1034baf0(void)
{
    struct_0 *idx;  // eax
    char v3[3];  // eax
    unsigned int v12;  // ecx
    unsigned int v13;  // ecx
    unsigned int v14;  // ecx
    unsigned int v15;  // ecx
    unsigned int v4;  // edi
    unsigned int v5;  // ecx
    char v6[3];  // edx
    char iter[3];  // eax
    unsigned int v8;  // ecx
    unsigned int v9;  // ecx
    unsigned int v10;  // ecx
    unsigned int v11;  // ecx
    unsigned int v0;  // [bp-0xc]

    v3 = idx->field_6c + idx->field_38;
    v5 = idx->field_38 + v4;
    v6 = v3 + 86;
    if (*((char *)v5) == v3[0] && *((char *)(v5 + 1)) == v3[1])
    {
        iter = &v3[2];
        v8 = v5 + 2;
        do
        {
            iter = &iter[1];
            v9 = v8 + 1;
        } while (...);
        if (iter - v6 + 258 >= 3)
        {
            idx->field_70 = v4;
            return;
        }
    }
    v0 = 2;
    return;
}
```

## `sub_1034bb7a` `0x1034bb7a`

_228 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

typedef struct struct_1 {
    struct struct_0 *field_0;
    char padding_4[40];
    unsigned int field_2c;
    char padding_30[8];
    int field_38;
    unsigned int field_3c;
    unsigned int field_40;
    unsigned int field_44;
    struct struct_0 *field_48;
    unsigned int field_4c;
    char padding_50[4];
    unsigned int field_54;
    unsigned int field_58;
    unsigned int field_5c;
    char padding_60[12];
    unsigned int field_6c;
    unsigned int field_70;
    unsigned int field_74;
} struct_1;

struct_0 * sub_1034bb7a(void)
{
    unsigned int v2;  // ecx
    struct_1 *idx;  // edi
    struct_0 *v12;  // eax
    unsigned int v13;  // esi
    char v14[2];  // edx
    struct_0 *v15;  // eax
    char v16;  // cl
    unsigned int v4;  // ebx
    int v5;  // esi
    unsigned int v6;  // eax
    unsigned int v7;  // ecx
    unsigned short *iter;  // eax
    unsigned int v9;  // ecx
    unsigned short *node;  // eax
    unsigned int v11;  // ecx
    unsigned int iter1;  // [bp-0x8]

    iter1 = v2;
    v4 = idx->field_2c;
    while (true)
    {
        v5 = idx->field_3c - idx->field_74 - idx->field_6c;
        if (idx->field_6c >= v4 + idx->field_2c - 262)
        {
            sub_10350b50(idx->field_38, idx->field_38 + v4, v4);
            v6 = idx->field_4c;
            v7 = idx->field_44;
            idx->field_70 = idx->field_70 - v4;
            idx->field_6c = idx->field_6c - v4;
            idx->field_5c = idx->field_5c - v4;
            iter1 = v6;
            iter = v7 + iter1 * 2;
            do
            {
                iter += 1;
                v9 = *(iter);
                iter1 -= 1;
                *(iter) = ~(-(v9 < v4)) & v9 - v4;
            } while (iter1 != 1);
            iter1 = v4;
            node = idx->field_40 + v4 * 2;
            do
            {
                node += 1;
                v11 = *(node);
                iter1 -= 1;
                *(node) = ~(-(v11 < v4)) & v11 - v4;
            } while (iter1 != 1);
            v5 += v4;
        }
        if (!idx->field_0->field_4)
            return idx->field_0;
        v12 = sub_1034b8ca(idx->field_74 + idx->field_6c + idx->field_38, v5);
        idx->field_74 = &v12->padding_0[idx->field_74];
        v13 = idx->field_74;
        if (v13 >= 3)
        {
            v14 = idx->field_6c + idx->field_38;
            v15 = v14[0];
            v16 = idx->field_58;
            idx->field_48 = v15;
            v12 = (v15 << (v16 & 31) ^ v14[1]) & idx->field_54;
            idx->field_48 = v12;
        }
        if (v13 >= 262)
        {
            return v12;
        }
        else if (!idx->field_0->field_4)
        {
            return idx->field_0;
        }
    }
}
```

## `sub_1034bc5e` `0x1034bc5e`

_296 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
    char padding_4[8];
    unsigned int field_c;
    char padding_10[28];
    unsigned int field_2c;
    char padding_30[8];
    unsigned int field_38;
    char padding_3c[32];
    int field_5c;
    char padding_60[12];
    int field_6c;
    char padding_70[4];
    unsigned int field_74;
} struct_1;

typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

unsigned int sub_1034bc5e(struct_1 *idx, unsigned int a1)
{
    unsigned int v1;  // ecx
    int v11;  // ecx
    unsigned int v3;  // ebx
    unsigned int v4;  // eax
    unsigned int v5;  // 4098
    int v6;  // edx
    unsigned int v7;  // ecx
    unsigned int v8;  // eax
    int v9;  // ecx
    unsigned int v10;  // edx
    unsigned int v0;  // [bp-0x10]

    v1 = idx->field_c - 5;
    v3 = 0xffff;
    if (v1 < 0xffff)
        v3 = v1;
    do
    {
        v4 = idx->field_74;
        if (idx->field_74 > 1 || !((sub_1034bb7a(), v4 = idx->field_74, !v4)))
        {
            v5 = idx->field_6c;
            idx->field_6c = idx->field_6c + v4;
            v6 = idx->field_5c;
            v7 = idx->field_6c;
            idx->field_74 = 0;
            v8 = v6 + v3;
            if (v5 + v4 && v7 < v8)
                continue;
            idx->field_74 = v7 - v8;
            idx->field_6c = v8;
            sub_1034f51e(idx, (v6 < 0 ? 0 : idx->field_38 + v6), v8 - v6, 0);
            idx->field_5c = idx->field_6c;
            sub_1034b061();
            if (!idx->field_0->field_10)
                break;
        }
        else if (a1)
        {
            v11 = idx->field_5c;
            sub_1034f51e(idx, (v11 < 0 ? 0 : idx->field_38 + v11), idx->field_6c - v11, a1 == 4);
            idx->field_5c = idx->field_6c;
            sub_1034b061();
            if (idx->field_0->field_10)
            {
                return (a1 == 4) * 2 + 1;
            }
            else if (a1 == 4)
            {
                v0 = 2;
                return 2;
            }
        }
        v9 = idx->field_5c;
        v10 = idx->field_6c - v9;
        if (v10 < idx->field_2c - 262)
            continue;
        sub_1034f51e(idx, (v9 < 0 ? 0 : idx->field_38 + v9), v10, 0);
        idx->field_5c = idx->field_6c;
        sub_1034b061();
    } while (idx->field_0->field_10);
    return 0;
}
```

## `sub_1034bd86` `0x1034bd86`

_750 bytes. (leaf/helper — see body)_

```c
extern char g_10393e60;
extern char g_10393f60;
extern char g_1039405d;

unsigned int sub_1034bd86(void* idx, unsigned int a1)
{
    unsigned int v1;  // ebp
    unsigned int v2;  // eax
    unsigned short v11;  // cx
    unsigned int v12;  // eax
    unsigned short v13;  // cx
    unsigned int v14;  // eax
    unsigned int v15;  // eax
    unsigned int v16;  // eax
    unsigned int v17;  // ecx
    unsigned int v18;  // edx
    unsigned int v19;  // ecx
    unsigned int index;  // eax
    unsigned int v3;  // edx
    unsigned int v21;  // ebp
    unsigned int i;  // 4138
    unsigned int v23;  // eax
    unsigned int v24;  // ecx
    char v25[2];  // edx
    unsigned int v26;  // eax
    char v27;  // cl
    char v28;  // 4138
    unsigned int v29;  // ecx
    int v30;  // ecx
    unsigned int v4;  // edi
    int v31;  // ecx
    unsigned int idx1;  // eax
    unsigned int v6;  // ecx
    unsigned int v7;  // eax
    unsigned int v8;  // edx
    int v9;  // eax
    char v10;  // 4137
    unsigned int v0;  // [bp-0x14]

    v1 = 0;
    while (true)
    {
        v2 = (int)idx[116];
        if ((int)idx[116] < 262)
        {
            sub_1034bb7a();
            v2 = (int)idx[116];
            if (v2 < 262 && !a1)
                break;
            if (!v2)
            {
                v31 = (int)idx[92];
                sub_1034f51e(idx, (v31 < 0 ? 0 : (int)idx[56] + v31), (int)idx[108] - v31, a1 == 4);
                *((int *)&idx[92]) = (int)idx[108];
                sub_1034b061();
                if (*((int *)(*((int *)idx) + 16)))
                    return (a1 == 4) * 2 + 1;
                if (a1 == 4)
                {
                    v0 = 2;
                    return 2;
                }
                break;
            }
        }
        if (v2 >= 3)
        {
            v3 = (int)idx[108];
            v4 = (int)idx[52];
            idx1 = ((int)idx[72] << ((char)(int)idx[88] & 31) ^ *((char *)((int)idx[56] + v3 + 2))) & (int)idx[84];
            v6 = (int)idx[0x44];
            *((unsigned int *)&idx[72]) = idx1;
            *((short *)((int)idx[64] + (v4 & v3) * 2)) = *((short *)(v6 + idx1 * 2));
            v1 = *((short *)((int)idx[64] + ((int)idx[108] & (int)idx[52]) * 2));
            *((short *)((int)idx[0x44] + (int)idx[72] * 2)) = (short)idx[108];
        }
        if (v1 && (v7 = (int)idx[108] - v1, v7 <= (int)idx[44] - 262))
        {
            if ((int)idx[0x88] != 2)
            {
                if ((int)idx[0x88] != 3)
                {
                    v9 = sub_1034b9ab(idx, v8, v1);
                    goto LABEL_1034be4d;
                }
            }
            else
            {
                if (false && v7 == 1)
                {
                    v9 = sub_1034baf0();
LABEL_1034be4d:
                    *((int *)&idx[96]) = v9;
                }
            }
        }
        if ((int)idx[96] >= 3)
        {
            v10 = (char)idx[96];
            v11 = (short)idx[108] - (short)idx[112];
            *((unsigned short *)((int)idx[5796] + (int)idx[5792] * 2)) = v11;
            *((char *)((int)idx[5784] + (int)idx[5792])) = v10 - 3;
            *((unsigned int *)&idx[5792]) = (int)idx[5792] + 1;
            v12 = *(&(&g_1039405d)[v10]);
            v13 = v11 + 65535;
            *((unsigned short *)(1176 + (char *)idx + 4 * v12)) = *((short *)(1176 + (char *)idx + 4 * v12)) + 1;
            v14 = v13;
            v15 = (v13 < 0x100 ? (&g_10393e60)[v14] : (&g_10393f60)[v14 >> 7]);
            *((unsigned short *)(2440 + (char *)idx + 4 * v15)) = *((short *)(2440 + (char *)idx + 4 * v15)) + 1;
            v16 = (int)idx[96];
            v17 = (int)idx[5792] == (int)idx[5788] - 1;
            *((unsigned int *)&idx[116]) = (int)idx[116] - v16;
            if (v16 <= (int)idx[128] && (int)idx[116] >= 3)
            {
                *((unsigned int *)&idx[96]) = v16 - 1;
                do
                {
                    *((unsigned int *)&idx[108]) = (int)idx[108] + 1;
                    v18 = (int)idx[108];
                    v19 = (int)idx[0x44];
                    index = (*((char *)(v18 + (int)idx[56] + 2)) ^ (int)idx[72] << ((char)(int)idx[88] & 31)) & (int)idx[84];
                    v21 = (int)idx[52];
                    *((unsigned int *)&idx[72]) = index;
                    *((short *)((int)idx[64] + (v21 & v18) * 2)) = *((short *)(v19 + index * 2));
                    v1 = *((short *)((int)idx[64] + ((int)idx[108] & (int)idx[52]) * 2));
                    *((short *)((int)idx[0x44] + (int)idx[72] * 2)) = (short)idx[108];
                    i = (int)idx[96];
                    *((unsigned int *)&idx[96]) = (int)idx[96] - 1;
                } while (i != 1);
                *((unsigned int *)&idx[108]) = (int)idx[108] + 1;
            }
            else
            {
                *((unsigned int *)&idx[108]) = (int)idx[108] + v16;
                v23 = (int)idx[108];
                v24 = (int)idx[56];
                *((unsigned int *)&idx[96]) = 0;
                v25 = v23 + v24;
                v26 = v25[0];
                v27 = (int)idx[88];
                *((unsigned int *)&idx[72]) = v26;
                *((unsigned int *)&idx[72]) = (v26 << (v27 & 31) ^ v25[1]) & (int)idx[84];
            }
        }
        else
        {
            v28 = *((char *)((int)idx[108] + (int)idx[56]));
            *((unsigned short *)((int)idx[5796] + (int)idx[5792] * 2)) = 0;
            *((char *)((int)idx[5784] + (int)idx[5792])) = v28;
            *((unsigned int *)&idx[5792]) = (int)idx[5792] + 1;
            *((unsigned short *)(148 + (char *)idx + 4 * v28)) = *((short *)(148 + (char *)idx + 4 * v28)) + 1;
            v29 = (int)idx[5792] == (int)idx[5788] - 1;
            *((unsigned int *)&idx[116]) = (int)idx[116] - 1;
            v17 = v29;
            *((unsigned int *)&idx[108]) = (int)idx[108] + 1;
        }
        if (!v17)
            continue;
        v30 = (int)idx[92];
        sub_1034f51e(idx, (v30 < 0 ? 0 : (int)idx[56] + v30), (int)idx[108] - v30, 0);
        *((int *)&idx[92]) = (int)idx[108];
        sub_1034b061();
        if (!*((int *)(*((int *)idx) + 16)))
            break;
    }
    return 0;
}
```

## `sub_1034c074` `0x1034c074`

_971 bytes. (leaf/helper — see body)_

```c
extern char g_10393e60;
extern char g_10393f60;
extern char g_1039405d;

unsigned int sub_1034c074(void* idx, unsigned int a1)
{
    unsigned int v2;  // eax
    unsigned int v3;  // edx
    char v12;  // 4155
    unsigned short v13;  // cx
    unsigned int v14;  // eax
    unsigned short v15;  // cx
    unsigned int v16;  // eax
    unsigned int v17;  // eax
    unsigned int v18;  // eax
    unsigned int v19;  // ebp
    unsigned int v20;  // edx
    unsigned int v21;  // ebx
    unsigned int v4;  // edi
    unsigned int idx1;  // eax
    unsigned int v23;  // ecx
    unsigned int v24;  // 4096
    unsigned int v25;  // eax
    int v26;  // edx
    char v27;  // 4129
    int v28;  // ecx
    char v29;  // 4125
    void* v30;  // eax
    int v31;  // ecx
    unsigned int index;  // eax
    unsigned int v6;  // ecx
    unsigned int v7;  // edx
    unsigned int v8;  // eax
    unsigned int v9;  // ecx
    unsigned int v10;  // eax
    unsigned int v11;  // edi
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x4]

    v1 = 0;
    while (true)
    {
        v2 = (int)idx[116];
        if ((int)idx[116] < 262)
        {
            sub_1034bb7a();
            v2 = (int)idx[116];
            if (v2 < 262 && !a1)
                return 0;
            if (!v2)
                break;
        }
        if (v2 >= 3)
        {
            v3 = (int)idx[108];
            v4 = (int)idx[52];
            index = ((int)idx[72] << ((char)(int)idx[88] & 31) ^ *((char *)((int)idx[56] + v3 + 2))) & (int)idx[84];
            v6 = (int)idx[0x44];
            *((unsigned int *)&idx[72]) = index;
            *((short *)((int)idx[64] + (v4 & v3) * 2)) = *((short *)(v6 + index * 2));
            v1 = *((short *)((int)idx[64] + ((int)idx[108] & (int)idx[52]) * 2));
            *((short *)((int)idx[0x44] + (int)idx[72] * 2)) = (short)idx[108];
        }
        v7 = v1;
        v0 = 2;
        *((int *)&idx[120]) = (int)idx[96];
        *((int *)&idx[100]) = (int)idx[112];
        *((unsigned int *)&idx[96]) = 2;
        if (v7 && (int)idx[120] < (int)idx[128] && (v8 = (int)idx[108] - v7, v8 <= (int)idx[44] - 262))
        {
            v9 = (int)idx[0x88];
            if (v9 != 2)
            {
                if (v9 != 3)
                {
                    v10 = sub_1034b9ab(idx, v7, v7);
                    goto LABEL_1034c166;
                }
            }
            else
            {
                if (v9 != 3)
                    goto LABEL_1034c169;
            }
            if (v8 == 1)
            {
                v10 = sub_1034baf0();
                v0 = 2;
LABEL_1034c166:
                *((unsigned int *)&idx[96]) = v10;
            }
LABEL_1034c169:
            if ((int)idx[96] <= 5 && ((int)idx[0x88] == 1 || (int)idx[96] == 3 && (int)idx[108] - (int)idx[112] > 0x1000))
            {
                *((unsigned int *)&idx[96]) = 2;
                goto LABEL_1034c18f;
            }
        }
        else
        {
LABEL_1034c18f:
            if ((int)idx[120] >= 3 && (int)idx[96] <= (int)idx[120])
            {
                v11 = (int)idx[108] + (int)idx[116] - 3;
                v12 = (char)idx[120];
                v13 = (short)idx[108] - (short)idx[100] - 1;
                *((unsigned short *)((int)idx[5796] + (int)idx[5792] * 2)) = v13;
                *((char *)((int)idx[5784] + (int)idx[5792])) = v12 - 3;
                *((unsigned int *)&idx[5792]) = (int)idx[5792] + 1;
                v14 = *(&(&g_1039405d)[v12]);
                v15 = v13 + 65535;
                *((unsigned short *)(1176 + (char *)idx + 4 * v14)) = *((short *)(1176 + (char *)idx + 4 * v14)) + 1;
                v16 = v15;
                v17 = (v15 < 0x100 ? (&g_10393e60)[v16] : (&g_10393f60)[v16 >> 7]);
                *((unsigned short *)(2440 + (char *)idx + 4 * v17)) = *((short *)(2440 + (char *)idx + 4 * v17)) + 1;
                v18 = (int)idx[120];
                v19 = (int)idx[5792] == (int)idx[5788] - 1;
                *((unsigned int *)&idx[116]) = (int)idx[116] + 1 - v18;
                *((unsigned int *)&idx[120]) = v18 - 2;
                do
                {
                    *((unsigned int *)&idx[108]) = (int)idx[108] + 1;
                    v20 = (int)idx[108];
                    if (v20 <= v11)
                    {
                        v21 = (int)idx[52];
                        idx1 = ((int)idx[72] << ((char)(int)idx[88] & 31) ^ *((char *)((int)idx[56] + v20 + 2))) & (int)idx[84];
                        v23 = (int)idx[0x44];
                        *((unsigned int *)&idx[72]) = idx1;
                        *((short *)((int)idx[64] + (v21 & v20) * 2)) = *((short *)(v23 + idx1 * 2));
                        v1 = *((short *)((int)idx[64] + ((int)idx[108] & (int)idx[52]) * 2));
                        *((short *)((int)idx[0x44] + (int)idx[72] * 2)) = (short)idx[108];
                    }
                } while ((v24 = (unsigned int)(int)idx[120], *((unsigned int *)&idx[120]) = (int)idx[120] - 1, v24 != 1));
                *((unsigned int *)&idx[108]) = (int)idx[108] + 1;
                v25 = (int)idx[108];
                *((unsigned int *)&idx[104]) = 0;
                *((unsigned int *)&idx[96]) = 2;
                if (!v19)
                    continue;
                v26 = (int)idx[92];
                sub_1034f51e(idx, (v26 < 0 ? 0 : (int)idx[56] + v26), v25 - v26, 0);
                *((int *)&idx[92]) = (int)idx[108];
                sub_1034b061();
                goto LABEL_1034c377;
            }
            else if ((int)idx[104])
            {
                v27 = *((char *)((int)idx[108] + (int)idx[56] - 1));
                *((unsigned short *)((int)idx[5796] + (int)idx[5792] * 2)) = 0;
                *((char *)((int)idx[5784] + (int)idx[5792])) = v27;
                *((unsigned int *)&idx[5792]) = (int)idx[5792] + 1;
                *((unsigned short *)(148 + (char *)idx + 4 * v27)) = *((short *)(148 + (char *)idx + 4 * v27)) + 1;
                if ((int)idx[5792] == (int)idx[5788] - 1)
                {
                    v28 = (int)idx[92];
                    sub_1034f51e(idx, (v28 < 0 ? 0 : (int)idx[56] + v28), (int)idx[108] - v28, 0);
                    *((int *)&idx[92]) = (int)idx[108];
                    sub_1034b061();
                }
                *((unsigned int *)&idx[108]) = (int)idx[108] + 1;
                *((unsigned int *)&idx[116]) = (int)idx[116] - 1;
LABEL_1034c377:
                if (!*((int *)(*((int *)idx) + 16)))
                    return 0;
            }
            else
            {
                *((unsigned int *)&idx[108]) = (int)idx[108] + 1;
                *((unsigned int *)&idx[116]) = (int)idx[116] - 1;
                *((unsigned int *)&idx[104]) = 1;
            }
        }
    }
    if ((int)idx[104])
    {
        v29 = *((char *)((int)idx[108] + (int)idx[56] - 1));
        v30 = idx + 5792;
        *((unsigned short *)((int)idx[5796] + *((int *)v30) * 2)) = 0;
        *((char *)((int)idx[5784] + *((int *)v30))) = v29;
        *((unsigned int *)v30) = *((int *)v30) + 1;
        *((unsigned short *)(148 + (char *)idx + 4 * v29)) = *((short *)(148 + (char *)idx + 4 * v29)) + 1;
        *((unsigned int *)&idx[104]) = 0;
    }
    v31 = (int)idx[92];
    sub_1034f51e(idx, (v31 < 0 ? 0 : (int)idx[56] + v31), (int)idx[108] - v31, a1 == 4);
    *((int *)&idx[92]) = (int)idx[108];
    sub_1034b061();
    if (*((int *)(*((int *)idx) + 16)))
    {
        return (a1 == 4) * 2 + 1;
    }
    else if (a1 != 4)
    {
        return 0;
    }
    else
    {
        v0 = 2;
        return 2;
    }
}
```

## `sub_1034c43f` `0x1034c43f`

_135 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[8];
    unsigned int field_8;
    char padding_c[8];
    unsigned int field_14;
    unsigned int field_18;
    struct struct_0 *field_1c;
    unsigned int field_20;
    unsigned int field_24;
    char padding_28[4];
    unsigned int field_2c;
    unsigned int field_30;
} struct_1;

typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
    unsigned int field_8;
    char padding_c[4];
    unsigned int field_10;
    unsigned int field_14;
    int field_18;
    char padding_1c[12];
    unsigned int field_28;
} struct_0;

unsigned int sub_1034c43f(struct_1 *index)
{
    struct_0 *idx;  // esi
    int v2;  // eax
    int v3;  // eax
    unsigned int v0;  // [bp-0x10]

    if (index)
    {
        idx = index->field_1c;
        if (idx && index->field_20 && index->field_24)
        {
            v0 = 2;
            index->field_14 = 0;
            index->field_8 = 0;
            index->field_18 = 0;
            index->field_2c = 2;
            idx->field_10 = idx->field_8;
            v2 = idx->field_18;
            idx->field_14 = 0;
            if (v2 < NULL)
                idx->field_18 = -(v2);
            v3 = idx->field_18;
            idx->field_4 = (-(0 < v3) & 4294967225) + 113;
            index->field_30 = (v3 == 2 ? sub_1034ddc8(0, 0, 0) : sub_1034dde2(0, 0, 0));
            idx->field_28 = 0;
            sub_1034efa8(idx);
            sub_1034b92d();
            return 0;
        }
    }
    v0 = 4294967294;
    return 4294967294;
}
```

## `sub_1034c4c6` `0x1034c4c6`

_464 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
    struct struct_0 *field_1c;
    struct struct_2 *field_20;
    unsigned int field_24;
    unsigned int field_28;
} struct_1;

typedef struct struct_0 {
    struct struct_1 *field_0;
    char padding_4[4];
    unsigned int field_8;
    unsigned int field_c;
    char padding_10[8];
    unsigned int field_18;
    unsigned int field_1c;
    char padding_20[12];
    unsigned int field_2c;
    unsigned int field_30;
    unsigned int field_34;
    unsigned int field_38;
    char padding_3c[4];
    unsigned int field_40;
    unsigned int field_44;
    char padding_48[4];
    unsigned int field_4c;
    unsigned int field_50;
    unsigned int field_54;
    unsigned int field_58;
    char padding_5c[40];
    unsigned int field_84;
    unsigned int field_88;
    char padding_8c[5644];
    unsigned int field_1698;
    unsigned int field_169c;
    char padding_16a0[4];
    unsigned int field_16a4;
} struct_0;

typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

extern unsigned int g_103942e8;

unsigned int sub_1034c4c6(struct_1 *index, unsigned int a1, unsigned int a2, int a3, unsigned int a4, unsigned int a5, char *a6, unsigned int a7)
{
    unsigned int v1;  // ebx
    unsigned int *v2;  // 4098
    unsigned int v11;  // 4113
    struct_0 *idx;  // esi
    unsigned int v4;  // ebx
    unsigned int v5;  // ecx
    unsigned int v6;  // eax
    unsigned int v7;  // eax
    struct_0 *v8;  // ebx
    unsigned int v9;  // eax
    unsigned int v10;  // ecx
    unsigned int v0;  // [bp-0x14]

    v1 = 1;
    if (!(a6 && *(a6) == 49 && a7 == 56))
    {
        v0 = 4294967290;
    }
    else if (!index)
    {
LABEL_1034c4f6:
        v0 = 4294967294;
    }
    else
    {
        v2 = &index->field_20->field_0;
        index->field_18 = 0;
        if (!v2)
        {
            index->field_20 = sub_1034f713;
            index->field_28 = 0;
        }
        if (!index->field_24)
            index->field_24 = sub_1034f724;
        if (a1 == 4294967295)
            a1 = 6;
        if (a3 < NULL)
        {
            v1 = 0;
            a3 = -(a3);
        }
        else if (a3 > 15)
        {
            a3 -= 16;
            v0 = 2;
            v1 = 2;
        }
        if (a4 - 1 > 8 || a2 != 8 || a3 - 8 > 7 || (v0 = 9, a1 > 9 || a5 > 4))
            goto LABEL_1034c4f6;
        if (a3 == 8)
            a3 = 9;
        idx = index->field_20(index->field_28, 1, 5824);
        if (idx)
        {
            index->field_1c = idx;
            idx->field_1c = 0;
            idx->field_18 = v1;
            idx->field_30 = a3;
            v4 = 1 << ((char)a3 & 31);
            v5 = a4 + 7;
            v0 = 3;
            idx->field_34 = v4 - 1;
            v6 = 1 << ((char)v5 & 31);
            idx->field_50 = v5;
            idx->field_0 = index;
            idx->field_4c = v6;
            idx->field_54 = v6 - 1;
            idx->field_2c = v4;
            idx->field_58 = (v5 + 2) / 3;
            idx->field_38 = index->field_20(index->field_28, v4, 2);
            idx->field_40 = index->field_20(index->field_28, idx->field_2c, 2);
            idx->field_44 = index->field_20(index->field_28, idx->field_4c, 2);
            v7 = 1 << ((char)((a4 & 0xff) + 6) & 31);
            v8 = &idx->field_169c;
            v8->field_0 = v7;
            v9 = index->field_20(index->field_28, v7, 4);
            v10 = v8->field_0;
            idx->field_c = v10 * 4;
            v11 = idx->field_38;
            idx->field_8 = v9;
            if (v11 && idx->field_40 && idx->field_44 && v9)
            {
                idx->field_84 = a1;
                idx->field_16a4 = v9 + (v10 >> 1) * 2;
                idx->field_1698 = v10 * 3 + v9;
                idx->field_88 = a5;
                idx->padding_20[4] = 8;
                return sub_1034c43f(index);
            }
            *((unsigned int *)&idx->padding_4[0]) = 666;
            index->field_18 = g_103942e8;
            sub_1034b81d(index);
        }
        v0 = 0xfffffffc;
    }
    return v0;
}
```

## `sub_1034c696` `0x1034c696`

_33 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[24];
    unsigned int field_18;
    struct struct_0 *field_1c;
    struct struct_2 *field_20;
    unsigned int field_24;
    unsigned int field_28;
} struct_1;

typedef struct struct_0 {
    void* field_0;
    char padding_4[4];
    unsigned int field_8;
    unsigned int field_c;
    char padding_10[8];
    unsigned int field_18;
    unsigned int field_1c;
    char padding_20[12];
    unsigned int field_2c;
    unsigned int field_30;
    unsigned int field_34;
    unsigned int field_38;
    char padding_3c[4];
    unsigned int field_40;
    unsigned int field_44;
    char padding_48[4];
    unsigned int field_4c;
    unsigned int field_50;
    unsigned int field_54;
    unsigned int field_58;
    char padding_5c[40];
    unsigned int field_84;
    unsigned int field_88;
    char padding_8c[5644];
    unsigned int field_1698;
    unsigned int field_169c;
    char padding_16a0[4];
    unsigned int field_16a4;
} struct_0;

typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

unsigned int sub_1034c696(struct_1 *a0, unsigned int a1, char *a2, unsigned int a3)
{
    return sub_1034c4c6(a0, a1, 8, 15, 8, 0, a2, a3);
}
```

## `sub_1034c6b7` `0x1034c6b7`

_91 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[8];
    unsigned int field_8;
    char padding_c[8];
    unsigned int field_14;
    unsigned int field_18;
    struct struct_0 *field_1c;
    char padding_20[16];
    unsigned int field_30;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    char padding_8[4];
    unsigned int field_c;
    char padding_10[4];
    unsigned int field_14;
    char padding_18[4];
    unsigned int field_1c;
    unsigned int field_20;
    char padding_24[4];
    unsigned int field_28;
    unsigned int field_2c;
    unsigned int field_30;
    char padding_34[4];
    unsigned int field_38;
    unsigned int field_3c;
    char padding_40[12];
    unsigned int field_4c;
    unsigned int field_50;
    char padding_54[24];
    unsigned int field_6c;
    char padding_70[1216];
    char field_530;
} struct_0;

unsigned int sub_1034c6b7(struct_1 *index)
{
    struct_0 *idx;  // eax
    unsigned int v2;  // ecx
    unsigned int v0;  // [bp-0x4]

    if (!index)
    {
        v0 = 4294967294;
        return v0;
    }
    idx = index->field_1c;
    if (!idx)
    {
        v0 = 4294967294;
        return v0;
    }
    idx->field_1c = 0;
    index->field_14 = 0;
    index->field_8 = 0;
    index->field_18 = 0;
    index->field_30 = 1;
    v2 = &idx->field_530;
    idx->field_0 = 0;
    idx->field_4 = 0;
    idx->field_c = 0;
    idx->field_14 = 0x8000;
    idx->field_20 = 0;
    idx->field_28 = 0;
    idx->field_2c = 0;
    idx->field_30 = 0;
    idx->field_38 = 0;
    idx->field_3c = 0;
    idx->field_6c = v2;
    idx->field_50 = v2;
    idx->field_4c = v2;
    return 0;
}
```

## `sub_1034c712` `0x1034c712`

_186 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[8];
    unsigned int field_8;
    char padding_c[8];
    unsigned int field_14;
    unsigned int field_18;
    struct struct_0 *field_1c;
    char padding_20[16];
    unsigned int field_30;
} struct_1;

typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
    char padding_c[24];
    int field_24;
    char padding_28[12];
    unsigned int field_34;
} struct_0;

typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    char padding_8[4];
    unsigned int field_c;
    char padding_10[4];
    unsigned int field_14;
    char padding_18[4];
    unsigned int field_1c;
    unsigned int field_20;
    char padding_24[4];
    unsigned int field_28;
    unsigned int field_2c;
    unsigned int field_30;
    char padding_34[4];
    unsigned int field_38;
    unsigned int field_3c;
    char padding_40[12];
    unsigned int field_4c;
    unsigned int field_50;
    char padding_54[24];
    unsigned int field_6c;
    char padding_70[1216];
    char field_530;
} struct_0;

unsigned int sub_1034c712(struct_1 *idx, unsigned int a1, char *a2, unsigned int a3)
{
    unsigned int *v1;  // 4098
    struct_0 *index;  // eax
    unsigned int v3;  // ecx
    unsigned int v0;  // [bp-0xc]

    if (!(a2 && *(a2) == 49 && a3 == 56))
    {
        v0 = 4294967290;
    }
    else if (!idx)
    {
LABEL_1034c73e:
        v0 = 4294967294;
    }
    else
    {
        v1 = *((int *)&idx->padding_20[0]);
        idx->field_18 = 0;
        if (!v1)
        {
            *((void* *)&idx->padding_20[0]) = sub_1034f713;
            *((unsigned int *)&idx->padding_20[8]) = 0;
        }
        if (!*((int *)&idx->padding_20[4]))
            *((void* *)&idx->padding_20[4]) = sub_1034f724;
        index = (*((int *)&idx->padding_20[0]))(*((int *)&idx->padding_20[8]), 1, 9520);
        if (!index)
        {
            v0 = 0xfffffffc;
        }
        else
        {
            v3 = a1;
            idx->field_1c = index;
            if (v3 < NULL)
            {
                index->field_8 = 0;
                v3 = -(v3);
            }
            else
            {
                index->field_8 = (v3 >> 4) + 1;
                if (v3 < 48)
                    v3 &= 15;
            }
            if (v3 - 8 <= 7)
            {
                index->field_24 = v3;
                index->field_34 = 0;
                return sub_1034c6b7(idx);
            }
            (*((int *)&idx->padding_20[4]))(*((int *)&idx->padding_20[8]), index);
            idx->field_1c = NULL;
            goto LABEL_1034c73e;
            goto LABEL_1034c73e;
        }
    }
    return v0;
}
```

## `sub_1034c7cc` `0x1034c7cc`

_23 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[8];
    unsigned int field_8;
    char padding_c[8];
    unsigned int field_14;
    unsigned int field_18;
    struct struct_0 *field_1c;
    char padding_20[16];
    unsigned int field_30;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    char padding_8[4];
    unsigned int field_c;
    char padding_10[4];
    unsigned int field_14;
    char padding_18[4];
    unsigned int field_1c;
    unsigned int field_20;
    char padding_24[4];
    unsigned int field_28;
    unsigned int field_2c;
    unsigned int field_30;
    char padding_34[4];
    unsigned int field_38;
    unsigned int field_3c;
    char padding_40[12];
    unsigned int field_4c;
    unsigned int field_50;
    char padding_54[24];
    unsigned int field_6c;
    char padding_70[1216];
    char field_530;
} struct_0;

unsigned int sub_1034c7cc(struct_1 *a0, char *a1, unsigned int a2)
{
    return sub_1034c712(a0, 15, a1, a2);
}
```

## `sub_1034c7e3` `0x1034c7e3`

_29 bytes. (leaf/helper — see body)_

```c
extern char g_10390db0;
extern char g_103915b0;

int sub_1034c7e3(void)
{
    unsigned int idx[23];  // eax

    idx[19] = &g_10390db0;
    idx[21] = 9;
    idx[20] = &g_103915b0;
    idx[22] = 5;
    return;
}
```

## `sub_1034c800` `0x1034c800`

_216 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[12];
    unsigned int field_c;
    unsigned int field_10;
    char padding_14[8];
    struct struct_0 *field_1c;
    struct struct_2 *field_20;
    char padding_24[4];
    unsigned int field_28;
} struct_1;

typedef struct struct_0 {
    char padding_0[36];
    unsigned int field_24;
    int field_28;
    int field_2c;
    int field_30;
    int field_34;
} struct_0;

typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

int sub_1034c800(void)
{
    unsigned int v2;  // ecx
    struct_1 *index;  // edi
    struct_0 *idx;  // esi
    unsigned int v5;  // eax
    char v6;  // cl
    unsigned int v7;  // eax
    int v8;  // ebx
    int v9;  // eax
    int v10;  // ebx
    int v11;  // edx
    int v0;  // [bp-0x8], Other Possible Types: unsigned int

    v0 = v2;
    idx = index->field_1c;
    if (!idx->field_34)
    {
        v5 = index->field_20(index->field_28, 1 << ((char)idx->field_24 & 31), 1);
        idx->field_34 = v5;
        if (!v5)
            return;
    }
    if (!idx->field_28)
    {
        v6 = idx->field_24;
        idx->field_30 = 0;
        idx->field_2c = 0;
        idx->field_28 = 1 << (v6 & 31);
    }
    v8 = v7 - index->field_10;
    v9 = idx->field_28;
    if (v8 >= v9)
    {
        sub_10350b50(idx->field_34, index->field_c - v9, v9);
        idx->field_30 = 0;
        goto LABEL_1034c8ad;
    }
    else
    {
        v0 = v9 - idx->field_30;
        if (v0 > v8)
            v0 = v8;
        sub_10350b50(idx->field_34 + idx->field_30, index->field_c - v8, v0);
        v10 = v8 - v0;
        if (v8 != v0)
        {
            sub_10350b50(idx->field_34, index->field_c - v10, v10);
            idx->field_30 = v10;
LABEL_1034c8ad:
            idx->field_2c = idx->field_28;
        }
        else
        {
            idx->field_30 = idx->field_30 + v0;
            v11 = idx->field_28;
            if (idx->field_30 == v11)
                idx->field_30 = 0;
            if (idx->field_2c < v11)
                idx->field_2c = idx->field_2c + v0;
        }
    }
    return;
}
```

## `sub_1034c8d8` `0x1034c8d8`

_4593 bytes. refs "incorrect header check", "unknown compression method", "invalid window size"_

```c
typedef struct struct_1 {
    struct struct_2 *field_0;
    unsigned int field_4;
    unsigned int field_8;
    struct struct_2 *field_c;
    unsigned int field_10;
    unsigned int field_14;
    char padding_18[4];
    void* field_1c;
    char padding_20[12];
    unsigned int field_2c;
    unsigned int field_30;
} struct_1;

typedef struct struct_2 {
    char field_0;
} struct_2;

extern unsigned short g_10391630[4];

unsigned int sub_1034c8d8(struct_1 *idx, unsigned int a1)
{
    struct_1 *index;  // edx
    void* idx1;  // esi
    unsigned int v22;  // ecx
    char *v90;  // eax
    unsigned int v91;  // ecx
    char *v92;  // eax
    unsigned int v93;  // 4102
    int v94;  // eax
    unsigned int v96;  // eax
    struct_1 *v97;  // ecx
    unsigned int v98;  // eax
    unsigned int v23;  // eax
    struct_1 *idx2;  // eax
    unsigned int v100;  // 4107
    struct_1 *v101;  // edi
    unsigned int v102;  // eax
    int v103;  // ebx
    unsigned int v105;  // eax
    unsigned int v24;  // edi
    unsigned int v25;  // edi
    unsigned int v26;  // edi
    unsigned int v27[13];  // eax
    unsigned int v28[13];  // ecx
    unsigned int v29;  // eax
    unsigned int v30;  // eax
    unsigned int v18;  // ecx
    unsigned int v31;  // ecx
    unsigned int v32;  // eax
    unsigned int v33[13];  // ecx
    unsigned int v34;  // ecx
    unsigned int v35;  // ecx
    unsigned int v36;  // eax
    unsigned int v37[13];  // ecx
    unsigned int v38;  // ecx
    unsigned int node;  // edi
    unsigned int iter;  // ebx
    unsigned int v40;  // eax
    unsigned int v41;  // edi
    unsigned int v42;  // eax
    unsigned int v43;  // eax
    unsigned int v44;  // ecx
    unsigned int v45;  // ebx
    unsigned int v46;  // eax
    unsigned int v47;  // eax
    unsigned int v48;  // ecx
    unsigned int v49;  // eax
    unsigned int v50;  // eax
    unsigned int v51;  // ebx
    unsigned int v20;  // eax
    unsigned int v52;  // ebx
    unsigned int v53;  // 4140
    unsigned int v54;  // eax
    unsigned int v55;  // ecx
    unsigned int v56;  // eax
    unsigned int v57;  // eax
    unsigned int v58;  // ecx
    unsigned int v59;  // ecx
    unsigned int v60;  // eax
    unsigned int v61;  // eax
    unsigned int v62;  // edx
    unsigned int v63;  // ebx
    unsigned int v64;  // ebx
    unsigned int v65;  // eax
    unsigned int v66;  // ecx
    unsigned int v67;  // eax
    unsigned int v68;  // ecx
    unsigned int v69;  // eax
    struct_1 *v70;  // eax
    struct_1 *v71;  // eax
    unsigned int v72;  // eax
    unsigned int v73;  // edi
    unsigned int v74;  // edx
    char v75;  // cl
    unsigned int v76;  // ecx
    unsigned int v77;  // ecx
    unsigned int v78;  // eax
    char v79;  // cl
    unsigned int v80;  // eax
    unsigned int v81;  // edi
    unsigned int v82;  // edx
    char v83;  // cl
    unsigned int v84;  // ecx
    unsigned int v21[13];  // eax
    unsigned int v85;  // ecx
    unsigned int v86;  // ecx
    unsigned int v87;  // eax
    unsigned int v88;  // ecx
    unsigned int v89;  // ecx
    unsigned int v0;  // [bp-0x44]
    unsigned int v1;  // [bp-0x34]
    unsigned int v2;  // [bp-0x30]
    unsigned int v3;  // [bp-0x2c]
    unsigned int v4;  // [bp-0x28]
    int v5;  // [bp-0x24], Other Possible Types: unsigned int
    char *v6;  // [bp-0x20]
    char v7;  // [bp-0x1c]
    char v8;  // [bp-0x1b]
    char v9;  // [bp-0x1a]
    char v10;  // [bp-0x19]
    unsigned int iter1;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int iter2;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    char *v15;  // [bp-0x8]

    index = idx;
    if (index && !((idx1 = index->field_1c, !idx1 || !index->field_c || !index->field_0 && index->field_4)))
    {
        if (*((int *)idx1) == 11)
            *((unsigned int *)idx1) = 12;
        v18 = index->field_10;
        iter = (int)idx1[56];
        v4 = 0;
        node = (int)idx1[60];
        v6 = &index->field_c->field_0;
        v15 = &index->field_0->field_0;
        v14 = index->field_4;
        v2 = index->field_4;
        v20 = *((int *)idx1);
        while (true)
        {
            iter1 = v18;
            v12 = iter;
            v5 = v18;
            switch (v20)
            {
            case 0:
                if (!(int)idx1[8])
                {
                    *((unsigned int *)idx1) = 12;
                    goto LABEL_1034d999;
                }
                else
                {
                    for (; node < 16; node += 8)
                    {
                        if (!v14)
                            goto LABEL_1034d9e7;
                        v14 -= 1;
                        v15 += 1;
                        v12 = iter + (*(v15) << ((char)node & 31));
                    }
                    if (((char)(int)idx1[8] & 2) && iter == 35615)
                    {
                        node = 0;
                        *((unsigned int *)&idx1[24]) = sub_1034ddc8(0, 0, 0);
                        v7 = 31;
                        v8 = 139;
                        iter = 0;
                        *((unsigned int *)&idx1[24]) = sub_1034ddc8((int)idx1[24], &v7, 2);
                        v12 = 0;
                        *((unsigned int *)idx1) = 1;
                        goto LABEL_1034d999;
                    }
                    v21 = (int)idx1[32];
                    *((unsigned int *)&idx1[16]) = 0;
                    if (v21)
                        v21[12] = 4294967295;
                    if (!(((char)idx1[8] & 1) && !((v0 = 31, ((unsigned int)(char)iter * 0x100 + (iter >> 8)) % 31))))
                    {
                        *((char **)&idx->padding_18[0]) = "incorrect header check";
                        goto LABEL_1034d993;
                    }
                    else if (((char)iter & 15) != 8)
                    {
                        *((char **)&idx->padding_18[0]) = "unknown compression method";
                        goto LABEL_1034d993;
                    }
                    else
                    {
                        iter >>= 4;
                        v22 = (iter & 15) + 8;
                        node -= 4;
                        v12 = iter;
                        if (v22 > (int)idx1[36])
                        {
                            *((char **)&idx->padding_18[0]) = "invalid window size";
                            goto LABEL_1034d993;
                        }
                        else
                        {
                            node = 0;
                            *((unsigned int *)&idx1[20]) = 1 << ((char)v22 & 31);
                            v23 = sub_1034dde2(0, 0, 0);
                            *((unsigned int *)&idx1[24]) = v23;
                            idx->field_30 = v23;
                            *((unsigned int *)idx1) = ~(iter >> 8) & 2 | 9;
                            iter = 0;
                            v12 = 0;
                            goto LABEL_1034d999;
                        }
                    }
                }
            case 1:
                if (node < 16)
                {
                    do
                    {
                        if (!v14)
                            goto LABEL_1034d9e7;
                        v14 -= 1;
                        node += 8;
                        iter += *(v15) << ((char)node & 31);
                        v15 += 1;
                        v12 = iter;
                    } while (node < 16);
                    index = idx;
                }
                *((unsigned int *)&idx1[16]) = iter;
                if ((char)iter != 8)
                {
                    *((char **)&index->padding_18[0]) = "unknown compression method";
                    goto LABEL_1034d993;
                }
                if (((unsigned short)iter & 0xe000))
                {
                    *((char **)&index->padding_18[0]) = "unknown header flags set";
                    goto LABEL_1034d993;
                }
                else
                {
                    if ((int)idx1[32])
                        *((unsigned int *)(int)idx1[32]) = iter >> 8 & 1;
                    if (((short)idx1[16] & 0x200))
                    {
                        v7 = iter;
                        v8 = iter >> 8;
                        index = idx;
                        *((unsigned int *)&idx1[24]) = sub_1034ddc8((int)idx1[24], &v7, 2);
                    }
                    iter = 0;
                    node = 0;
                    *((unsigned int *)idx1) = 2;
                    goto LABEL_1034cb15;
                }
            case 2:
LABEL_1034cb15:
                if (node < 32)
                {
                    do
                    {
                        if (!v14)
                            goto LABEL_1034d9e7;
                    } while ((v14 -= 1, v24 = node + 8, iter += (unsigned int)*(v15) << ((char)node & 31), v15 += 1, node += 8, node < 32));
                    index = idx;
                }
                if ((int)idx1[32])
                    *((unsigned int *)((int)idx1[32] + 4)) = iter;
                if (((short)idx1[16] & 0x200))
                {
                    v8 = iter >> 8;
                    v9 = iter >> 16;
                    v7 = iter;
                    v10 = iter >> 24;
                    index = idx;
                    *((unsigned int *)&idx1[24]) = sub_1034ddc8((int)idx1[24], &v7, 4);
                }
                iter = 0;
                node = 0;
                *((unsigned int *)idx1) = 3;
            case 3:
                if (node < 16)
                {
                    do
                    {
                        if (!v14)
                            goto LABEL_1034d9e7;
                    } while ((v14 -= 1, v25 = node + 8, iter += (unsigned int)*(v15) << ((char)node & 31), v15 += 1, node += 8, node < 16));
                    index = idx;
                }
                if ((int)idx1[32])
                {
                    *((unsigned int *)((int)idx1[32] + 8)) = iter & 0xff;
                    *((unsigned int *)((int)idx1[32] + 12)) = iter >> 8;
                }
                if (((short)idx1[16] & 0x200))
                {
                    v7 = iter;
                    v8 = iter >> 8;
                    index = idx;
                    *((unsigned int *)&idx1[24]) = sub_1034ddc8((int)idx1[24], &v7, 2);
                }
                iter = 0;
                v12 = 0;
                node = 0;
                *((unsigned int *)idx1) = 4;
            case 4:
                if (((short)idx1[16] & 0x400))
                {
                    if (node < 16)
                    {
                        do
                        {
                            if (!v14)
                                goto LABEL_1034d9e7;
                        } while ((v14 -= 1, v26 = node + 8, iter += (unsigned int)*(v15) << ((char)node & 31), v15 += 1, node += 8, node < 16));
                        index = idx;
                    }
                    v27 = (int)idx1[32];
                    *((unsigned int *)&idx1[64]) = iter;
                    if (v27)
                        v27[5] = iter;
                    if (((short)idx1[16] & 0x200))
                    {
                        v7 = iter;
                        v8 = iter >> 8;
                        index = idx;
                        *((unsigned int *)&idx1[24]) = sub_1034ddc8((int)idx1[24], &v7, 2);
                    }
                    iter = 0;
                    v12 = 0;
                    node = 0;
                }
                else if ((int)idx1[32])
                {
                    *((unsigned int *)((int)idx1[32] + 16)) = 0;
                }
                *((unsigned int *)idx1) = 5;
            case 5:
                if (((short)idx1[16] & 0x400))
                {
                    iter2 = (int)idx1[64];
                    if (iter2 > v14)
                        iter2 = v14;
                    if (iter2)
                    {
                        v28 = (int)idx1[32];
                        if (v28)
                        {
                            v3 = v28[4];
                            if (v28[4])
                            {
                                v29 = v28[5] - iter2;
                                sub_10350b50(v3 + v29, v15, (iter2 + v29 <= v28[6] ? iter2 : v28[6] - v29));
                            }
                        }
                        if (((short)idx1[16] & 0x200))
                            *((unsigned int *)&idx1[24]) = sub_1034ddc8((int)idx1[24], v15, iter2);
                        v30 = iter2;
                        v14 -= v30;
                        v15 = &v15[v30];
                        *((unsigned int *)&idx1[64]) = (int)idx1[64] - v30;
                    }
                    if ((int)idx1[64])
                        goto LABEL_1034d9e7;
                    index = idx;
                }
                *((unsigned int *)&idx1[64]) = 0;
                *((unsigned int *)idx1) = 6;
            case 6:
                if (((short)idx1[16] & 0x800))
                {
                    if (!v14)
                        goto LABEL_1034d9e7;
                    v31 = 0;
                    do
                    {
                        v32 = v15[v31];
                        iter2 = v31 + 1;
                        v33 = (int)idx1[32];
                        v3 = v32;
                        if (v33)
                        {
                            v1 = v33[7];
                            if (v33[7] && (int)idx1[64] < v33[8])
                            {
                                *((char *)(v1 + (int)idx1[64])) = v32;
                                *((unsigned int *)&idx1[64]) = (int)idx1[64] + 1;
                            }
                        }
                    } while (v32 && (v31 = iter2, v31 < v14));
                    if (((short)idx1[16] & 0x200))
                    {
                        *((unsigned int *)&idx1[24]) = sub_1034ddc8((int)idx1[24], v15, iter2);
                        v32 = v3;
                    }
                    v34 = iter2;
                    v14 -= v34;
                    v15 = &v15[v34];
                    if (v32)
                        goto LABEL_1034d9e7;
                    index = idx;
                }
                else if ((int)idx1[32])
                {
                    *((unsigned int *)((int)idx1[32] + 28)) = 0;
                }
                *((unsigned int *)&idx1[64]) = 0;
                *((unsigned int *)idx1) = 7;
            case 7:
                if (((short)idx1[16] & 0x1000))
                {
                    if (!v14)
                        goto LABEL_1034d9e7;
                    v35 = 0;
                    do
                    {
                        v36 = v15[v35];
                        iter2 = v35 + 1;
                        v37 = (int)idx1[32];
                        v3 = v36;
                        if (v37)
                        {
                            v1 = v37[9];
                            if (v37[9] && (int)idx1[64] < v37[10])
                            {
                                *((char *)(v1 + (int)idx1[64])) = v36;
                                *((unsigned int *)&idx1[64]) = (int)idx1[64] + 1;
                            }
                        }
                    } while (v36 && (v35 = iter2, v35 < v14));
                    if (((short)idx1[16] & 0x200))
                    {
                        *((unsigned int *)&idx1[24]) = sub_1034ddc8((int)idx1[24], v15, iter2);
                        v36 = v3;
                    }
                    v38 = iter2;
                    v14 -= v38;
                    v15 = &v15[v38];
                    if (v36)
                        goto LABEL_1034d9e7;
                    index = idx;
                }
                else if ((int)idx1[32])
                {
                    *((unsigned int *)((int)idx1[32] + 36)) = 0;
                }
                *((unsigned int *)idx1) = 8;
            case 8:
                if (((short)idx1[16] & 0x200))
                {
                    if (node < 16)
                    {
                        do
                        {
                            if (!v14)
                                goto LABEL_1034d9e7;
                            v14 -= 1;
                            node += 8;
                            iter += *(v15) << ((char)node & 31);
                            v15 += 1;
                            v12 = iter;
                        } while (node < 16);
                        index = idx;
                    }
                    if (iter != (short)idx1[24])
                    {
                        *((char **)&index->padding_18[0]) = "header crc mismatch";
                        goto LABEL_1034d993;
                    }
                    else
                    {
                        iter = 0;
                        v12 = 0;
                        node = 0;
                    }
                }
                if ((int)idx1[32])
                {
                    *((unsigned int *)((int)idx1[32] + 44)) = (int)idx1[16] >> 9 & 1;
                    *((unsigned int *)((int)idx1[32] + 48)) = 1;
                }
                v40 = sub_1034ddc8(0, 0, 0);
                *((unsigned int *)&idx1[24]) = v40;
                idx->field_30 = v40;
                goto LABEL_1034d5f4;
            case 9:
                if (node < 32)
                {
                    do
                    {
                        if (!v14)
                            goto LABEL_1034d9e7;
                        v14 -= 1;
                        v41 = node + 8;
                        iter += *(v15) << ((char)node & 31);
                        v15 += 1;
                        v12 = iter;
                        node = v41;
                    } while (node < 32);
                    index = idx;
                }
                v42 = ((iter & 0xff00) + iter * 0x10000) * 0x100 + *((char *)((void*)&v12 + 2)) * 0x100 + (iter >> 24);
                *((unsigned int *)&idx1[24]) = v42;
                index->field_30 = v42;
                iter = 0;
                node = 0;
                *((unsigned int *)idx1) = 10;
            case 13:
                v48 = node & 7;
                iter >>= (char)v48 & 31;
                node -= v48;
                v12 = iter;
                if (node < 32)
                {
                    do
                    {
                        if (!v14)
                            goto LABEL_1034d9e7;
                        v14 -= 1;
                        node += 8;
                        iter += *(v15) << ((char)node & 31);
                        v15 += 1;
                        v12 = iter;
                    } while (node < 32);
                    index = idx;
                }
                v49 = iter & 0xffff;
                if (v49 != ~(iter) >> 16)
                {
                    *((char **)&index->padding_18[0]) = "invalid stored block lengths";
                    goto LABEL_1034d993;
                }
                else
                {
                    iter = 0;
                    *((unsigned int *)&idx1[64]) = v49;
                    v12 = 0;
                    node = 0;
                    *((unsigned int *)idx1) = 14;
                    goto LABEL_1034d07a;
                }
            case 14:
LABEL_1034d07a:
                iter2 = (int)idx1[64];
                if ((int)idx1[64])
                {
                    if (iter2 > v14)
                        iter2 = v14;
                    if (iter2 > iter1)
                        iter2 = iter1;
                    if (!iter2)
                        goto LABEL_1034d9e7;
                    sub_10350b50(v6, v15, iter2);
                    v50 = iter2;
                    v14 -= v50;
                    v15 = &v15[v50];
                    iter1 -= v50;
                    v6 = &v6[v50];
                    *((unsigned int *)&idx1[64]) = (int)idx1[64] - v50;
                    goto LABEL_1034d999;
                }
                break;
            case 17:
                while ((int)idx1[104] < (int)idx1[100] + (int)idx1[96])
                {
                    while (true)
                    {
                        v57 = *((int *)((int)idx1[76] + ((1 << ((char)(int)idx1[84] & 31)) - 1 & iter) * 4));
                        v3 = v57;
                        if ((char)(v57 >> 8) <= node)
                            break;
                        if (!v14)
                            goto LABEL_1034d9e7;
                        v14 -= 1;
                        iter += *(v15) << ((char)node & 31);
                        v15 += 1;
                        node += 8;
                    }
                    if ((unsigned short)(v57 >> 16) < 16)
                    {
                        v58 = (char)(v57 >> 8);
                        while (true)
                        {
                            if (node >= v58)
                            {
                                v59 = *((char *)((void*)&v57 + 1));
                                iter >>= (char)v59 & 31;
                                node -= v59;
                                *((unsigned short *)(112 + (char *)idx1 + 2 * idx1[104])) = *((unsigned short *)((void*)&v3 + 2));
                                *((unsigned int *)&idx1[104]) = (int)idx1[104] + 1;
                                v12 = iter;
                            }
                            if (!v14)
                                break;
                            v14 -= 1;
                            v58 = *((char *)((void*)&v57 + 1));
                            iter += *(v15) << ((char)node & 31);
                            v15 += 1;
                            node += 8;
                        }
                        goto LABEL_1034d9e7;
                    }
                    if (*((unsigned short *)((void*)&v3 + 2)) == 16)
                    {
                        v60 = *((char *)((void*)&v57 + 1));
                        while (true)
                        {
                            if (node >= v60 + 2)
                            {
                                iter >>= (char)v60 & 31;
                                node -= v60;
                                v12 = iter;
                                if ((int)idx1[104])
                                {
                                    v3 = *((short *)(110 + (char *)idx1 + 2 * idx1[104]));
                                    v61 = (iter & 3) + 3;
                                    iter >>= 2;
                                    node -= 2;
                                    goto LABEL_1034d38f;
                                }
                                else
                                {
                                    *((char **)&idx->padding_18[0]) = "invalid bit length repeat";
                                    goto LABEL_1034d993;
                                }
                            }
                            if (!v14)
                                break;
                            v14 -= 1;
                            iter += *(v15) << ((char)node & 31);
                            v15 += 1;
                            node += 8;
                        }
                        goto LABEL_1034d9e7;
                    }
                    if (*((unsigned short *)((void*)&v3 + 2)) == 0x11)
                    {
                        while (true)
                        {
                            if (node >= v62 + 3)
                            {
                                v63 = iter >> ((char)v62 & 31);
                                v0 = 4294967293;
                                v61 = (v63 & 7) + 3;
                                iter = v63 >> 3;
                                goto LABEL_1034d386;
                            }
                            if (!v14)
                                break;
                            v14 -= 1;
                            iter += *(v15) << ((char)node & 31);
                            v15 += 1;
                            node += 8;
                        }
                        goto LABEL_1034d9e7;
                    }
                    else
                    {
                        for (v62 = *((char *)((void*)&v57 + 1)); node < v62 + 7; node += 8)
                        {
                            if (!v14)
                                goto LABEL_1034d9e7;
                            v14 -= 1;
                            iter += *(v15) << ((char)node & 31);
                            v15 += 1;
                        }
                        v64 = iter >> ((char)v62 & 31);
                        v0 = 4294967289;
                        v61 = (v64 & 127) + 11;
                        iter = v64 >> 7;
LABEL_1034d386:
                        v3 = 0;
                        node += v0 - v62;
LABEL_1034d38f:
                        if ((int)idx1[104] + v61 > (int)idx1[100] + (int)idx1[96])
                        {
                            *((char **)&idx->padding_18[0]) = "invalid bit length repeat";
                            *((unsigned int *)idx1) = 27;
                            break;
                        }
                        else
                        {
                            for (v12 = iter; v61; *((unsigned int *)&idx1[104]) = (int)idx1[104] + 1)
                            {
                                v61 -= 1;
                                *((unsigned short *)(112 + (char *)idx1 + 2 * idx1[104])) = v3;
                            }
                        }
                    }
                }
                if (*((int *)idx1) == 27)
                    goto LABEL_1034d999;
                v65 = idx1 + 1328;
                v66 = idx1 + 108;
                *((unsigned int *)v66) = v65;
                *((unsigned int *)&idx1[76]) = v65;
                v67 = idx1 + 84;
                *((unsigned int *)v67) = 9;
                v4 = sub_1034fb0b(1, idx1 + 112, (int)idx1[96], v66, v67, idx1 + 752);
                if (v4)
                {
                    *((char **)&idx->padding_18[0]) = "invalid literal/lengths set";
                    goto LABEL_1034d993;
                }
                v68 = idx1 + 108;
                *((int *)&idx1[80]) = *((int *)v68);
                v69 = idx1 + 88;
                *((unsigned int *)v69) = 6;
                v4 = sub_1034fb0b(2, idx1 + (int)idx1[96] * 2 + 112, (int)idx1[100], v68, v69, idx1 + 752);
                if (v4)
                {
                    *((char **)&idx->padding_18[0]) = "invalid distances set";
                    goto LABEL_1034d993;
                }
                else
                {
                    *((unsigned int *)idx1) = 18;
                    goto LABEL_1034d480;
                }
            case 18:
LABEL_1034d480:
                if (v14 >= 6 && iter1 >= 258)
                {
                    v70 = idx;
                    v70->field_c = v6;
                    v70->field_10 = iter1;
                    v70->field_0 = v15;
                    v70->field_4 = v14;
                    *((unsigned int *)&idx1[56]) = iter;
                    *((unsigned int *)&idx1[60]) = node;
                    sub_1034f72f(v70, v5);
                    v71 = idx;
                    iter = (int)idx1[56];
                    node = (int)idx1[60];
                    v6 = &v71->field_c->field_0;
                    iter1 = v71->field_10;
                    v15 = &v71->field_0->field_0;
                    v14 = v71->field_4;
                    v12 = iter;
                    goto LABEL_1034d999;
                }
                v72 = *((int *)((int)idx1[76] + ((1 << ((char)(int)idx1[84] & 31)) - 1 & iter) * 4));
                while (true)
                {
                    if ((char)(v72 >> 8) <= node)
                        break;
                    if (!v14)
                        goto LABEL_1034d9e7;
                    v14 -= 1;
                    v73 = node + 8;
                    iter += *(v15) << ((char)node & 31);
                    v15 += 1;
                    v72 = *((int *)((int)idx1[76] + ((1 << ((char)(int)idx1[84] & 31)) - 1 & iter) * 4));
                    node = v73;
                }
                if ((char)v72 && !((char)v72 & 240))
                {
                    v12 = v72;
                    v12 >>= 8;
                    iter2 = (char)v12;
                    v3 = v72;
                    v72 = *((int *)((int)idx1[76] + ((((1 << ((char)((char)v72 + iter2) & 31)) - 1 & iter) >> ((char)iter2 & 31)) + (v72 >> 16)) * 4));
                    v74 = (char)v12;
                    while (true)
                    {
                        if ((char)(v72 >> 8) + v74 <= node)
                        {
                            v76 = *((char *)((void*)&v3 + 1));
                            iter >>= (char)v76 & 31;
                            node -= v76;
                            goto LABEL_1034d5ca;
                        }
                        if (!v14)
                            break;
                        v14 -= 1;
                        v75 = v3;
                        v74 = v75;
                        iter += *(v15) << ((char)node & 31);
                        v15 += 1;
                        node += 8;
                        v72 = *((int *)((int)idx1[76] + ((((1 << ((char)(v75 + v74) & 31)) - 1 & iter) >> ((char)v74 & 31)) + *((unsigned short *)((void*)&v3 + 2))) * 4));
                    }
                    goto LABEL_1034d9e7;
                }
LABEL_1034d5ca:
                v77 = (char)(v72 >> 8);
                iter >>= (char)v77 & 31;
                node -= v77;
                v12 = iter;
                *((unsigned int *)&idx1[64]) = v72 >> 16;
                if (!(char)v72)
                {
                    *((unsigned int *)idx1) = 23;
                    goto LABEL_1034d999;
                }
                if (!((char)v72 & 32))
                {
                    if (((char)v72 & 64))
                    {
                        *((char **)&idx->padding_18[0]) = "invalid literal/length code";
                        goto LABEL_1034d993;
                    }
                    else
                    {
                        *((unsigned int *)&idx1[72]) = v72 & 15;
                        *((unsigned int *)idx1) = 19;
                        goto LABEL_1034d61e;
                    }
                }
LABEL_1034d5f4:
                *((unsigned int *)idx1) = 11;
                goto LABEL_1034d999;
            case 19:
LABEL_1034d61e:
                v78 = (int)idx1[72];
                if (v78)
                {
                    if (node < v78)
                    {
                        do
                        {
                            if (!v14)
                                goto LABEL_1034d9e7;
                        } while ((v14 -= 1, node += 8, iter += (unsigned int)*(v15) << ((char)node & 31), v15 += 1, node = node, node < (int)idx1[72]));
                    }
                    v79 = v78;
                    *((unsigned int *)&idx1[64]) = (int)idx1[64] + ((1 << (v79 & 31)) - 1 & iter);
                    iter >>= v79 & 31;
                    node -= v78;
                }
                *((unsigned int *)idx1) = 20;
            case 20:
                v80 = *((int *)((int)idx1[80] + ((1 << ((char)(int)idx1[88] & 31)) - 1 & iter) * 4));
                while (true)
                {
                    if ((char)(v80 >> 8) <= node)
                        break;
                    if (!v14)
                        goto LABEL_1034d9e7;
                    v14 -= 1;
                    v81 = node + 8;
                    iter += *(v15) << ((char)node & 31);
                    v15 += 1;
                    v80 = *((int *)((int)idx1[80] + ((1 << ((char)(int)idx1[88] & 31)) - 1 & iter) * 4));
                    node = v81;
                }
                if (!((char)v80 & 240))
                {
                    v12 = v80;
                    v12 >>= 8;
                    iter2 = (char)v12;
                    v3 = v80;
                    v80 = *((int *)((int)idx1[80] + ((((1 << ((char)((char)v80 + iter2) & 31)) - 1 & iter) >> ((char)iter2 & 31)) + (v80 >> 16)) * 4));
                    v82 = (char)v12;
                    while (true)
                    {
                        if ((char)(v80 >> 8) + v82 <= node)
                        {
                            v84 = *((char *)((void*)&v3 + 1));
                            iter >>= (char)v84 & 31;
                            node -= v84;
                            goto LABEL_1034d744;
                        }
                        if (!v14)
                            break;
                        v14 -= 1;
                        v83 = v3;
                        v82 = v83;
                        iter += *(v15) << ((char)node & 31);
                        v15 += 1;
                        node += 8;
                        v80 = *((int *)((int)idx1[80] + ((((1 << ((char)(v83 + v82) & 31)) - 1 & iter) >> ((char)v82 & 31)) + *((unsigned short *)((void*)&v3 + 2))) * 4));
                    }
                    goto LABEL_1034d9e7;
                }
LABEL_1034d744:
                v85 = (char)(v80 >> 8);
                iter >>= (char)v85 & 31;
                node -= v85;
                v12 = iter;
                if (((char)v80 & 64))
                {
                    *((char **)&idx->padding_18[0]) = "invalid distance code";
                    goto LABEL_1034d993;
                }
                else
                {
                    index = idx;
                    *((unsigned int *)&idx1[0x44]) = v80 >> 16;
                    *((unsigned int *)&idx1[72]) = v80 & 15;
                    *((unsigned int *)idx1) = 21;
                    goto LABEL_1034d77d;
                }
            case 21:
LABEL_1034d77d:
                if ((int)idx1[72])
                {
                    if (node < (int)idx1[72])
                    {
                        do
                        {
                            if (!v14)
                                goto LABEL_1034d9e7;
                        } while ((v14 -= 1, node += 8, iter += (unsigned int)*(v15) << ((char)node & 31), v15 += 1, node = node, node < (int)idx1[72]));
                        index = idx;
                    }
                    v86 = (int)idx1[72];
                    *((unsigned int *)&idx1[0x44]) = (int)idx1[0x44] + ((1 << ((char)v86 & 31)) - 1 & iter);
                    iter >>= (char)v86 & 31;
                    node -= v86;
                    v12 = iter;
                }
                if ((int)idx1[0x44] > (int)idx1[44] - iter1 + v5)
                {
                    *((char **)&index->padding_18[0]) = "invalid distance too far back";
                    goto LABEL_1034d993;
                }
                else
                {
                    *((unsigned int *)idx1) = 22;
                    goto LABEL_1034d7e4;
                }
            case 22:
LABEL_1034d7e4:
                if (!iter1)
                    goto LABEL_1034d9e7;
                v87 = v5 - iter1;
                v88 = (int)idx1[0x44];
                if (v88 > v87)
                {
                    iter2 = v88 - v87;
                    v89 = (int)idx1[48];
                    if (iter2 > v89)
                    {
                        iter2 -= v89;
                        v90 = (int)idx1[52] + (int)idx1[40] - iter2;
                    }
                    else
                    {
                        v90 = (int)idx1[52] - iter2 + v89;
                    }
                    v91 = (int)idx1[64];
                    v3 = v91;
                    if (iter2 <= v91)
                        goto LABEL_1034d836;
                }
                else
                {
                    v90 = &v6[-1 * v88];
                    v91 = (int)idx1[64];
                    v3 = v91;
                }
                iter2 = v91;
LABEL_1034d836:
                if (iter2 > iter1)
                    iter2 = iter1;
                iter1 = iter2 - iter2;
                *((unsigned int *)&idx1[64]) = v3 - iter2;
                do
                {
                    v6 += 1;
                    v92 = v90 + 1;
                    v93 = iter2;
                    iter2 = v93 - 1;
                    *(v6) = *(v90);
                    v90 = v92;
                } while (v93 != 1);
                if ((int)idx1[64])
                    goto LABEL_1034d999;
                goto LABEL_1034d884;
            case 23:
                if (!iter1)
                    goto LABEL_1034d9e7;
                v6 += 1;
                iter1 -= 1;
                *(v6) = (char)idx1[64];
LABEL_1034d884:
                *((unsigned int *)idx1) = 18;
                goto LABEL_1034d999;
            case 24:
                if ((int)idx1[8])
                {
                    if (node < 32)
                    {
                        do
                        {
                            if (!v14)
                                goto LABEL_1034d9e7;
                            v14 -= 1;
                            node += 8;
                            iter += *(v15) << ((char)node & 31);
                            v15 += 1;
                            v12 = iter;
                        } while (node < 32);
                        index = idx;
                    }
                    v94 = v5 - iter1;
                    index->field_14 = index->field_14 + v94;
                    *((int *)&idx1[28]) = (int)idx1[28] + v94;
                    v5 = v94;
                    if (v5)
                    {
                        v96 = (!(int)idx1[16] ? sub_1034dde2((int)idx1[24], &v6[-1 * v5], v5) : sub_1034ddc8((int)idx1[24], &v6[-1 * v5], v5));
                        v97 = idx;
                        *((unsigned int *)&idx1[24]) = v96;
                        v97->field_30 = v96;
                        index = v97;
                    }
                    v5 = iter1;
                    v98 = iter;
                    if (!(int)idx1[16])
                        v98 = ((v98 & 0xff00) + iter * 0x10000) * 0x100 + *((char *)((void*)&v12 + 2)) * 0x100 + (iter >> 24);
                    if (v98 != (int)idx1[24])
                    {
                        *((char **)&index->padding_18[0]) = "incorrect data check";
                        goto LABEL_1034d993;
                    }
                    else
                    {
                        iter = 0;
                        v12 = 0;
                        node = 0;
                    }
                }
                *((unsigned int *)idx1) = 25;
            case 25:
                if ((int)idx1[8] && (int)idx1[16])
                {
                    if (node < 32)
                    {
                        do
                        {
                            if (!v14)
                                goto LABEL_1034d9e7;
                            v14 -= 1;
                            node += 8;
                            iter += *(v15) << ((char)node & 31);
                            v15 += 1;
                            v12 = iter;
                        } while (node < 32);
                        index = idx;
                    }
                    if (iter != (int)idx1[28])
                    {
                        *((char **)&index->padding_18[0]) = "incorrect length check";
                    }
                    else
                    {
                        iter = 0;
                        node = 0;
                        goto LABEL_1034d9d1;
                    }
                }
                else
                {
LABEL_1034d9d1:
                    *((unsigned int *)idx1) = 26;
                    goto LABEL_1034d9d7;
                }
LABEL_1034d993:
                *((unsigned int *)idx1) = 27;
LABEL_1034d999:
                v20 = *((int *)idx1);
                if (v20 > 28)
                    break;
                index = idx;
                continue;
            case 26:
LABEL_1034d9d7:
                v4 = 1;
                goto LABEL_1034d9e7;
            case 10:
                if ((int)idx1[12])
                {
                    v43 = sub_1034dde2(0, 0, 0);
                    *((unsigned int *)&idx1[24]) = v43;
                    idx->field_30 = v43;
                    *((unsigned int *)idx1) = 11;
                    goto LABEL_1034cf64;
                }
                else
                {
                    index->field_c = v6;
                    index->field_10 = iter1;
                    index->field_0 = v15;
                    index->field_4 = v14;
                    *((unsigned int *)&idx1[56]) = iter;
                    *((unsigned int *)&idx1[60]) = node;
                    v0 = 2;
                    goto LABEL_1034c93d;
                }
            case 11:
LABEL_1034cf64:
                if (a1 == 5)
                    goto LABEL_1034d9e7;
                index = idx;
                goto LABEL_1034cf71;
            case 12:
LABEL_1034cf71:
                if ((int)idx1[4])
                {
                    v44 = node & 7;
                    iter >>= (char)v44 & 31;
                    node -= v44;
                    *((unsigned int *)idx1) = 24;
                    v12 = iter;
                    goto LABEL_1034d999;
                }
                else
                {
                    if (node < 3)
                    {
                        do
                        {
                            if (!v14)
                                goto LABEL_1034d9e7;
                        } while ((v14 -= 1, node += 8, iter += (unsigned int)*(v15) << ((char)node & 31), v15 += 1, node = node, node < 3));
                        index = idx;
                    }
                    v45 = iter >> 1;
                    *((unsigned int *)&idx1[4]) = iter & 1;
                    v46 = v45 & 3;
                    if (v46)
                    {
                        v47 = v46 - 1;
                        if (v46 == 1)
                        {
                            sub_1034c7e3();
                            *((unsigned int *)idx1) = 18;
                        }
                        else if (v47 == 1)
                        {
                            *((unsigned int *)idx1) = 15;
                        }
                        else if (v47 == 2)
                        {
                            *((char **)&index->padding_18[0]) = "invalid block type";
                            *((unsigned int *)idx1) = 27;
                        }
                    }
                    else
                    {
                        *((unsigned int *)idx1) = 13;
                    }
                    iter = v45 >> 2;
                    v12 = iter;
                    node -= 3;
                    goto LABEL_1034d999;
                }
            case 15:
                if (node < 14)
                {
                    do
                    {
                        if (!v14)
                            goto LABEL_1034d9e7;
                    } while ((v14 -= 1, node += 8, iter += (unsigned int)*(v15) << ((char)node & 31), v15 += 1, node = node, node < 14));
                    index = idx;
                }
                *((unsigned int *)&idx1[96]) = (iter & 31) + 0x101;
                v51 = iter >> 5;
                v52 = v51 >> 5;
                *((unsigned int *)&idx1[100]) = (v51 & 31) + 1;
                iter = v52 >> 4;
                node -= 14;
                v53 = (int)idx1[96];
                *((unsigned int *)&idx1[92]) = (v52 & 15) + 4;
                v12 = iter;
                if (v53 <= 286 && (int)idx1[100] <= 30)
                {
                    *((unsigned int *)&idx1[104]) = 0;
                    *((unsigned int *)idx1) = 16;
                }
                else
                {
                    *((char **)&index->padding_18[0]) = "too many length or distance symbols";
                    goto LABEL_1034d993;
                }
            case 16:
                for (; (int)idx1[104] < (int)idx1[92]; node -= 3)
                {
                    for (; node < 3; node += 8)
                    {
                        if (!v14)
                            goto LABEL_1034d9e7;
                        v14 -= 1;
                        iter += *(v15) << ((char)node & 31);
                        v15 += 1;
                    }
                    iter >>= 3;
                    *((unsigned short *)(112 + (char *)idx1 + 2 * g_10391630[idx1[104]])) = (char)iter & 7;
                    *((unsigned int *)&idx1[104]) = (int)idx1[104] + 1;
                    v12 = iter;
                }
                for (; (int)idx1[104] < 19; *((unsigned int *)&idx1[104]) = (int)idx1[104] + 1)
                {
                    *((unsigned short *)(112 + (char *)idx1 + 2 * g_10391630[idx1[104]])) = 0;
                }
                v54 = idx1 + 1328;
                v55 = idx1 + 108;
                *((unsigned int *)v55) = v54;
                *((unsigned int *)&idx1[76]) = v54;
                v56 = idx1 + 84;
                *((unsigned int *)v56) = 7;
                v4 = sub_1034fb0b(0, idx1 + 112, 19, v55, v56, idx1 + 752);
                if (v4)
                {
                    *((char **)&idx->padding_18[0]) = "invalid code lengths set";
                    goto LABEL_1034d993;
                }
                else
                {
                    *((unsigned int *)&idx1[104]) = 0;
                    *((unsigned int *)idx1) = 0x11;
                }
            case 27:
                v4 = 4294967293;
LABEL_1034d9e7:
                idx2 = idx;
                idx2->field_c = v6;
                idx2->field_10 = iter1;
                idx2->field_0 = v15;
                idx2->field_4 = v14;
                v100 = (int)idx1[40];
                *((unsigned int *)&idx1[56]) = iter;
                *((unsigned int *)&idx1[60]) = node;
                if ((v100 || *((int *)idx1) < 24 && v5 != idx->field_10) && sub_1034c800())
                {
                    *((unsigned int *)idx1) = 28;
                    goto LABEL_1034da32;
                }
                else
                {
                    v101 = idx;
                    v102 = v2 - v101->field_4;
                    v103 = v5 - v101->field_10;
                    v101->field_8 = v101->field_8 + v102;
                    v101->field_14 = v101->field_14 + v103;
                    *((int *)&idx1[28]) = (int)idx1[28] + v103;
                    v2 = v102;
                    if ((int)idx1[8] && v103)
                    {
                        v105 = (!(int)idx1[16] ? sub_1034dde2((int)idx1[24], &v101->field_c[-1 * v103], v103) : sub_1034ddc8((int)idx1[24], &v101->field_c[-1 * v103], v103));
                        *((unsigned int *)&idx1[24]) = v105;
                        v101->field_30 = v105;
                        v102 = v2;
                    }
                    v101->field_2c = (-(0 < (int)idx1[4]) & 64) + (*((int *)idx1) == 11 ? 128 : 0) + (int)idx1[60];
                    if ((!v102 && !v103 || a1 == 4) && !v4)
                        v4 = 4294967291;
                    return v4;
                }
            case 28:
LABEL_1034da32:
                v0 = 0xfffffffc;
                goto LABEL_1034c93d;
            }
        }
        goto LABEL_1034c93d;
    }
    v0 = 4294967294;
LABEL_1034c93d:
    return v0;
}
```

## `sub_1034db40` `0x1034db40`

_62 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[28];
    struct struct_0 *field_1c;
    char padding_20[4];
    struct struct_2 *field_24;
    unsigned int field_28;
} struct_1;

typedef struct struct_0 {
    char padding_0[52];
    unsigned int field_34;
} struct_0;

typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

unsigned int sub_1034db40(struct_1 *a0)
{
    if (!a0)
    {
        return 4294967294;
    }
    else if (!a0->field_1c)
    {
        return 4294967294;
    }
    else if (a0->field_24)
    {
        if (a0->field_1c->field_34)
            a0->field_24(a0->field_28, a0->field_1c->field_34);
        a0->field_24(a0->field_28, a0->field_1c);
        a0->field_1c = NULL;
        return 0;
    }
    else
    {
        return 4294967294;
    }
}
```

## `sub_1034db7e` `0x1034db7e`

_586 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_10391818[4];
extern unsigned int g_10391c18[4];
extern unsigned int g_10392018[4];
extern unsigned int g_10392418[4];

int sub_1034db7e(void)
{
    unsigned int v3;  // ecx
    unsigned int v4;  // eax
    void* v10;  // esi
    unsigned int v11;  // edx
    void* v12;  // esi
    unsigned int v13;  // eax
    void* v14;  // esi
    unsigned int v15;  // edx
    void* v16;  // esi
    unsigned int v17;  // eax
    void* v18;  // esi
    unsigned int v19;  // edx
    unsigned int v5;  // eax
    void* v20;  // esi
    unsigned int v21;  // eax
    void* v22;  // esi
    unsigned int v23;  // edx
    unsigned int v24;  // eax
    void* v6;  // edx
    void* node;  // esi
    unsigned int v8;  // edi
    unsigned int v9;  // eax
    unsigned int v0;  // [bp-0x18]
    unsigned int iter1;  // [bp-0x8]
    unsigned int iter;  // [bp+0x4]

    iter1 = v3;
    v5 = ~(v4);
    if (iter)
    {
        do
        {
        } while ((*((char *)&v6) & 3) && (v5 = v5 >> 8 ^ g_10391818[((unsigned int)(char)*((char *)v6) ^ v5) & 0xff], v6 += 1, iter -= 1, iter = iter, iter != 1));
    }
    v0 = 4;
    node = v6;
    v8 = v0;
    if (iter >= 32)
    {
        iter1 = iter >> 5;
        do
        {
            v9 = v5 ^ *((int *)node);
            v10 = node + v8;
            v11 = g_10391c18[v9 >> 16 & 0xff] ^ g_10392018[*((char *)((void*)&v9 + 1))] ^ g_10391818[v9 >> 24] ^ g_10392418[v9 & 0xff] ^ *((int *)v10);
            v12 = v10 + v8;
            v13 = g_10391c18[v11 >> 16 & 0xff] ^ g_10392018[*((char *)((void*)&v11 + 1))] ^ g_10391818[v11 >> 24] ^ g_10392418[v11 & 0xff] ^ *((int *)v12);
            v14 = v12 + v8;
            v15 = g_10391c18[v13 >> 16 & 0xff] ^ g_10392018[*((char *)((void*)&v13 + 1))] ^ g_10391818[v13 >> 24] ^ g_10392418[v13 & 0xff] ^ *((int *)v14);
            v16 = v14 + v8;
            v17 = g_10391c18[v15 >> 16 & 0xff] ^ g_10392018[*((char *)((void*)&v15 + 1))] ^ g_10391818[v15 >> 24] ^ g_10392418[v15 & 0xff] ^ *((int *)v16);
            v18 = v16 + v8;
            v19 = g_10391c18[v17 >> 16 & 0xff] ^ g_10392018[*((char *)((void*)&v17 + 1))] ^ g_10391818[v17 >> 24] ^ g_10392418[v17 & 0xff] ^ *((int *)v18);
            v20 = v18 + v8;
            v21 = g_10391c18[v19 >> 16 & 0xff] ^ g_10392018[*((char *)((void*)&v19 + 1))] ^ g_10391818[v19 >> 24] ^ g_10392418[v19 & 0xff] ^ *((int *)v20);
            v22 = v20 + v8;
            iter -= 32;
            v23 = g_10391c18[v21 >> 16 & 0xff] ^ g_10392018[*((char *)((void*)&v21 + 1))] ^ g_10391818[v21 >> 24] ^ g_10392418[v21 & 0xff] ^ *((int *)v22);
            node = v22 + v8;
        } while ((v5 = g_10391c18[v23 >> 16 & 0xff] ^ g_10392018[*((char *)((void*)&v23 + 1))] ^ g_10391818[v23 >> 24] ^ g_10392418[v23 & 0xff], iter1 -= 1, iter1 = iter1, iter1 != 1));
    }
    if (iter >= v8)
    {
        iter1 = iter >> 2;
        do
        {
            v24 = v5 ^ *((int *)node);
            iter -= v8;
            v5 = g_10391c18[v24 >> 16 & 0xff] ^ g_10392018[*((char *)((void*)&v24 + 1))] ^ g_10391818[v24 >> 24] ^ g_10392418[v24 & 0xff];
            node += v8;
            iter1 -= 1;
        } while (iter1 != 1);
    }
    if (iter)
    {
        do
        {
            iter -= 1;
        } while (iter != 1);
    }
    return;
}
```

## `sub_1034ddc8` `0x1034ddc8`

_26 bytes. (leaf/helper — see body)_

```c
int sub_1034ddc8(unsigned int a0, unsigned int a1, int a2)
{
    if (a1)
        return sub_1034db7e(a2);
    return 0;
}
```

## `sub_1034dde2` `0x1034dde2`

_544 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1034dde2(unsigned int iter, char *a1, unsigned int iter1)
{
    unsigned int iter2;  // edi
    unsigned int node;  // esi
    unsigned int v10;  // esi
    unsigned int v11;  // esi
    unsigned int v12;  // edi
    unsigned int v13;  // esi
    unsigned int v14;  // esi
    unsigned int v15;  // esi
    unsigned int v16;  // esi
    unsigned int v17;  // esi
    unsigned int v18;  // esi
    unsigned int v19;  // esi
    char v2[16];  // ecx
    unsigned int j;  // eax
    unsigned int v22;  // esi
    unsigned int v23;  // esi
    unsigned int v24;  // esi
    unsigned int v25;  // esi
    unsigned int v26;  // esi
    unsigned int v27;  // esi
    unsigned int v28;  // esi
    unsigned int v29;  // esi
    unsigned int l;  // eax
    unsigned int v30;  // edi
    unsigned int v31;  // esi
    unsigned int v32;  // esi
    unsigned int v33;  // esi
    unsigned int v34;  // esi
    unsigned int v35;  // esi
    unsigned int v36;  // esi
    unsigned int v37;  // esi
    unsigned int v4;  // esi
    unsigned int v5;  // esi
    unsigned int v6;  // esi
    unsigned int v7;  // esi
    unsigned int v8;  // esi
    unsigned int v9;  // esi

    iter2 = iter >> 16;
    node = iter & 0xffff;
    if (iter1 == 1)
    {
        node += *(a1);
        if (node >= 0xfff1)
            node -= 0xfff1;
        iter2 += node;
        if (iter2 >= 0xfff1)
        {
            iter2 -= 0xfff1;
            goto LABEL_1034dff6;
        }
    }
    else
    {
        v2 = a1;
        if (!v2)
            return 1;
        if (iter1 >= 16)
        {
            if (iter1 >= 5552)
            {
                iter = iter1 / 5552;
                do
                {
                    iter1 -= 5552;
                    l = 347;
                    do
                    {
                        v4 = node + v2[0];
                        v5 = v4 + v2[1];
                        v6 = v5 + v2[2];
                        v7 = v6 + v2[3];
                        v8 = v7 + v2[4];
                        v9 = v8 + v2[5];
                        v10 = v9 + v2[6];
                        v11 = v10 + v2[7];
                        v12 = iter2 + v4 + v5 + v6 + v7 + v8 + v9 + v10 + v11;
                        v13 = v11 + v2[8];
                        v14 = v13 + v2[9];
                        v15 = v14 + v2[10];
                        v16 = v15 + v2[11];
                        v17 = v16 + v2[12];
                        v18 = v17 + v2[13];
                        v19 = v18 + v2[14];
                        node = v19 + v2[15];
                        iter2 = v12 + v13 + v14 + v15 + v16 + v17 + v18 + v19 + node;
                        v2 += 1;
                        l -= 1;
                    } while (l != 1);
                    node = node % 0xfff1;
                    iter -= 1;
                    iter2 = iter2 % 0xfff1;
                } while (iter != 1);
            }
            if (iter1)
            {
                if (iter1 >= 16)
                {
                    j = iter1 >> 4;
                    do
                    {
                        v22 = node + v2[0];
                        v23 = v22 + v2[1];
                        v24 = v23 + v2[2];
                        v25 = v24 + v2[3];
                        v26 = v25 + v2[4];
                        v27 = v26 + v2[5];
                        v28 = v27 + v2[6];
                        v29 = v28 + v2[7];
                        v30 = iter2 + v22 + v23 + v24 + v25 + v26 + v27 + v28 + v29;
                        v31 = v29 + v2[8];
                        v32 = v31 + v2[9];
                        v33 = v32 + v2[10];
                        v34 = v33 + v2[11];
                        v35 = v34 + v2[12];
                        v36 = v35 + v2[13];
                        v37 = v36 + v2[14];
                        node = v37 + v2[15];
                        iter1 -= 16;
                        iter2 = v30 + v31 + v32 + v33 + v34 + v35 + v36 + v37 + node;
                        v2 += 1;
                        j -= 1;
                    } while (j != 1);
                }
                for (; iter1; iter2 += node + v2[0])
                {
                    iter1 -= 1;
                    v2 = &v2[1];
                }
                node = node % 0xfff1;
                iter2 = iter2 % 0xfff1;
            }
LABEL_1034dff6:
        }
        else
        {
            for (; iter1; iter2 += node + v2[0])
            {
                iter1 -= 1;
                v2 = &v2[1];
            }
            if (node >= 0xfff1)
                node -= 0xfff1;
            iter2 = iter2 % 0xfff1;
        }
        return iter2 * 0x10000 | node;
    }
}
```

## `sub_1034e002` `0x1034e002`

_94 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[148];
    unsigned short field_94;
    char padding_96[1022];
    unsigned short field_494;
    char padding_496[1266];
    unsigned short field_988;
    char padding_98a[242];
    unsigned short field_a7c;
    char padding_a7e[3106];
    unsigned int field_16a0;
    char padding_16a4[4];
    unsigned int field_16a8;
    unsigned int field_16ac;
    unsigned int field_16b0;
} struct_0;

int sub_1034e002(void)
{
    struct_0 *idx;  // eax
    struct_0 *iter;  // ecx
    unsigned int i;  // edx
    struct_0 *node;  // ecx
    struct_0 *iter1;  // ecx
    unsigned int j;  // [bp-0x8]

    iter = &idx->field_94;
    i = 286;
    do
    {
        *((unsigned short *)&iter->padding_0[0]) = 0;
        iter = &iter->padding_0[4];
        i -= 1;
    } while (i != 1);
    j = 30;
    node = &idx->field_988;
    do
    {
        *((unsigned short *)&node->padding_0[0]) = 0;
        node = &node->padding_0[4];
        j -= 1;
    } while (j != 1);
    j = 19;
    iter1 = &idx->field_a7c;
    do
    {
        *((unsigned short *)&iter1->padding_0[0]) = 0;
        iter1 = &iter1->padding_0[4];
        j -= 1;
    } while (j != 1);
    idx->field_16ac = 0;
    idx->field_16a8 = 0;
    idx->field_16b0 = 0;
    idx->field_16a0 = 0;
    idx->field_494 = 1;
    return;
}
```

## `sub_1034e060` `0x1034e060`

_176 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[5200];
    int field_1450;
} struct_0;

int sub_1034e060(void)
{
    unsigned int v4;  // ecx
    struct_0 *v5;  // eax
    unsigned int iter;  // ecx
    unsigned int v7;  // ebx
    unsigned int v8;  // esi
    unsigned int v9;  // edi
    unsigned int v10;  // esi
    unsigned int v11;  // ecx
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    unsigned int v3;  // [bp+0x4]

    v4 = v3;
    v2 = *((int *)&v5->padding_0[2908 + 4 * v4]);
    iter = v4 * 2;
    if (iter > v5->field_1450)
    {
        *((unsigned int *)&v5->padding_0[2908 + 4 * v3]) = v11;
        return;
    }
    v1 = v7;
    v0 = v8;
    if (iter >= v5->field_1450)
        goto LABEL_1034e0ba;
    while (true)
    {
        if (*((short *)(v9 + *((int *)&v5->padding_0[2912 + 4 * iter]) * 4)) < *((short *)(v9 + *((int *)&v5->padding_0[2908 + 4 * iter]) * 4)))
        {
            iter += 1;
        }
        else if (*((short *)(v9 + *((int *)&v5->padding_0[2912 + 4 * iter]) * 4)) == *((short *)(v9 + *((int *)&v5->padding_0[2908 + 4 * iter]) * 4)) && v5[1].padding_0[4 + *((int *)&v5->padding_0[2912 + 4 * iter])] <= v5[1].padding_0[4 + *((int *)&v5->padding_0[2908 + 4 * iter])])
        {
            iter += 1;
        }
        do
        {
LABEL_1034e0ba:
            v10 = *((int *)&v5->padding_0[2908 + 4 * iter]);
            if (*((short *)(v9 + v2 * 4)) < *((short *)(v9 + v10 * 4)) || *((short *)(v9 + v2 * 4)) == *((short *)(v9 + v10 * 4)) && v5[1].padding_0[4 + v2] <= v5[1].padding_0[4 + v10] || !((*((unsigned int *)&v5->padding_0[2908 + 4 * v3]) = v10, v3 = iter, iter *= 2, iter <= v5->field_1450)))
            {
                *((unsigned int *)&v5->padding_0[2908 + 4 * v3]) = v11;
                return;
            }
        } while (iter >= v5->field_1450);
    }
}
```

## `sub_1034e110` `0x1034e110`

_445 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    unsigned int field_0;
    int field_4;
    struct struct_0 *field_8;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    char padding_8[8];
    int field_10;
} struct_0;

typedef struct struct_2 {
    char padding_0[2876];
    unsigned short field_b3c;
} struct_2;

int sub_1034e110(void)
{
    struct_1 *idx;  // eax
    unsigned int v14;  // ebx
    int v23;  // ecx
    struct_2 *v24;  // esi
    unsigned int v25;  // ecx
    struct_2 *l;  // edi
    unsigned int iter;  // esi
    unsigned short v28[2];  // ecx
    int v29;  // esi
    struct_0 *index;  // eax
    unsigned int idx1[1452];  // edx
    unsigned int iter1[1452];  // edi
    unsigned int v18[1452];  // eax
    unsigned int v19;  // eax
    unsigned int v20;  // esi
    unsigned int v21;  // eax
    int v22;  // esi
    unsigned int v0;  // [bp-0x38]
    unsigned int v1;  // [bp-0x2c]
    unsigned int v2;  // [bp-0x28]
    int v3;  // [bp-0x24]
    unsigned int v4;  // [bp-0x20]
    unsigned int j;  // [bp-0x20]
    unsigned int v6;  // [bp-0x1c]
    int v7;  // [bp-0x18]
    unsigned int m;  // [bp-0x14]
    struct_2 *node;  // [bp-0x10], Other Possible Types: unsigned int
    int v10;  // [bp-0xc]
    int iter2;  // [bp-0x8]

    iter2 = 0;
    v3 = idx->field_4;
    v14 = idx->field_0;
    index = idx->field_8;
    v1 = index->field_0;
    v2 = index->field_4;
    v7 = *((int *)&index->padding_8[0]);
    v10 = index->field_10;
    v0 = 8;
    for (iter1 = &idx1[719]; v0; iter1 = &iter1[1])
    {
        v0 -= 1;
        iter1[0] = 0;
    }
    v18 = &idx1[1301];
    *((unsigned short *)(v14 + idx1[727 + v18[0]] * 4 + 2)) = 0;
    v19 = v18[0] + 1;
    if (v19 >= 573)
        return;
    v0 = v20;
    m = &idx1[v19 + 727];
    v4 = 573 - v19;
    v21 = v19 + v4;
    do
    {
        j = v4;
        v22 = *((int *)m);
        v6 = v22 * 4;
        v23 = *((short *)(v14 + *((short *)(v6 + v14 + 2)) * 4 + 2)) + 1;
        if (v23 > v10)
        {
            v23 = v10;
            iter2 += 1;
        }
        *((unsigned short *)(v6 + v14 + 2)) = v23;
        if (v22 <= v3)
        {
            *((unsigned short *)(2876 + (char *)idx1 + 2 * v23)) = *((short *)(2876 + (char *)idx1 + 2 * v23)) + 1;
            node = 0;
            if (v22 >= v7)
                node = *((int *)(v2 + (v22 - v7) * 4));
            v6 = *((short *)(v6 + v14));
            idx1[1450] = idx1[1450] + v6 * (node + v23);
            if (v1)
                idx1[1451] = idx1[1451] + v6 * (*((short *)(v6 + v1 + 2)) + node);
        }
        m += 4;
        v4 = j - 1;
    } while (j != 1);
    if (!iter2)
        return;
    v24 = 2876 + (char *)idx1 + 2 * v10;
    do
    {
        for (l = 2874 + (char *)idx1 + 2 * v10; !*((short *)&l->padding_0[0]); l = &l->padding_0[2])
        {
            v25 -= 1;
        }
        *((unsigned short *)(2876 + (char *)idx1 + 2 * v25)) = *((short *)(2876 + (char *)idx1 + 2 * v25)) - 1;
        iter2 -= 2;
        *((unsigned short *)(2878 + (char *)idx1 + 2 * v25)) = *((short *)(2878 + (char *)idx1 + 2 * v25)) + 2;
        *((unsigned short *)&v24->padding_0[0]) = *((short *)&v24->padding_0[0]) - 1;
    } while (iter2 > 0);
    iter2 = v10;
    if (iter2)
    {
        node = v24;
        do
        {
            m = *((short *)&node->padding_0[0]);
            if (m)
            {
                iter = &idx1[v21 + 727];
                do
                {
                    iter -= 4;
                    v21 -= 1;
                    v1 = iter;
                    if (*((int *)iter) <= v3)
                    {
                        v28 = v14 + *((int *)iter) * 4;
                        v29 = v28[1];
                        if (v29 != iter2)
                        {
                            idx1[1450] = idx1[1450] + v28[0] * (iter2 - v29);
                            v28[1] = iter2;
                        }
                        m -= 1;
                        iter = v1;
                    }
                } while (m);
            }
        } while ((iter2 = (int)(iter2 - 1), node -= 2, iter2));
    }
    return;
}
```

## `sub_1034e2cd` `0x1034e2cd`

_188 bytes. (leaf/helper — see body)_

```c
int sub_1034e2cd(void)
{
    int v4;  // ecx
    unsigned short v5[4];  // eax
    unsigned int v6;  // ecx
    int v7;  // ebx
    int v8;  // esi
    int i;  // esi
    unsigned int v10;  // eax
    int v11;  // esi
    int v0;  // [bp-0x1c]
    int v1;  // [bp-0xc], Other Possible Types: unsigned int
    unsigned short iter[4];  // [bp-0x8], Other Possible Types: int
    unsigned short idx[1379];  // [bp+0x4]

    iter = v4;
    v1 = v4;
    v1 = 4294967295;
    v0 = 7;
    v6 = v5[1];
    v7 = 0;
    v0 = 4;
    if (!v6)
    {
        v0 = 3;
        v0 = 138;
    }
    v5[3 + 2 * v4] = 65535;
    if (v4 < 0)
        return;
    iter = &v5[3];
    v8 = v4 + 1;
    do
    {
        i = v8;
        v10 = v6;
        v6 = iter[0];
        v7 += 1;
        if (v7 < v0 && v10 == v6)
            continue;
        if (v7 < v0)
        {
            idx[1342 + 2 * v10] = idx[1342 + 2 * v10] + (unsigned short)v7;
        }
        else if (v10)
        {
            if (v10 != v1)
                idx[1342 + 2 * v10] = idx[1342 + 2 * v10] + 1;
            idx[1374] = idx[1374] + 1;
        }
        else if (v7 <= 10)
        {
            idx[1376] = idx[1376] + 1;
        }
        else
        {
            idx[1378] = idx[1378] + 1;
        }
        v7 = 0;
        v1 = v10;
        if (!v6)
        {
            v0 = 138;
            goto LABEL_1034e36a;
        }
        else if (v10 == v6)
        {
            v0 = 6;
LABEL_1034e36a:
            v0 = 3;
            goto LABEL_1034e37c;
        }
        else
        {
            v0 = 7;
            v0 = 4;
LABEL_1034e37c:
        }
        iter = &iter[2];
        v11 = i - 1;
        v8 = v11;
    } while (i != 1);
    return;
}
```

## `sub_1034e389` `0x1034e389`

_1178 bytes. (leaf/helper — see body)_

```c
int sub_1034e389(void)
{
    unsigned short v8[4];  // ecx
    int iter;  // esi
    int v12;  // edx
    void* idx;  // eax
    unsigned int v14;  // edi
    int v15;  // ecx
    unsigned short v16;  // si
    unsigned int v17;  // ecx
    int v18;  // edx
    char v19;  // cl
    int v20;  // ecx
    int v21;  // ecx
    int v10;  // edx
    unsigned int v22;  // edi
    unsigned int v23;  // ecx
    unsigned short v24;  // si
    unsigned int v25;  // ecx
    unsigned int v26;  // edx
    char v27;  // cl
    int v28;  // ecx
    unsigned int v29;  // ecx
    unsigned int v30;  // ecx
    unsigned short v31;  // si
    unsigned int v32;  // ecx
    unsigned int v33;  // ebx
    char v34;  // cl
    int v35;  // ecx
    unsigned short v36;  // si
    unsigned int v37;  // ecx
    unsigned int v38;  // ebx
    unsigned short v39;  // si
    unsigned int v40;  // ebx
    unsigned int v11;  // ebx, Other Possible Types: int
    int v41;  // ecx
    int v42;  // ecx
    unsigned short v43;  // si
    unsigned int v44;  // ecx
    int v45;  // ebx
    char v46;  // cl
    int v47;  // ecx
    unsigned short v48;  // si
    unsigned int v49;  // ecx
    int v50;  // ebx
    unsigned short v51;  // si
    unsigned int v52;  // ecx
    int v53;  // ebx
    char v54;  // cl
    int v55;  // ecx
    unsigned short v56;  // si
    unsigned int v57;  // ecx
    int v58;  // ebx
    int v0;  // [bp-0x1c]
    int i;  // [bp-0x1c]
    int v2;  // [bp-0x18]
    int v3;  // [bp-0x14], Other Possible Types: unsigned int
    unsigned short node[4];  // [bp-0x10]
    int v5;  // [bp-0xc]
    int v6;  // [bp-0x8]

    v2 = -1;
    v11 = 7;
    v5 = v8[1];
    iter = 0;
    v11 = 4;
    if (!v5)
    {
        v11 = 3;
        v11 = 138;
    }
    if (v10 < 0)
        return;
    node = &v8[3];
    v0 = v10 + 1;
    do
    {
        i = v0;
        v12 = v5;
        iter += 1;
        v3 = v12;
        v5 = node[0];
        v6 = iter;
        if (iter < v11 && v12 == v5)
            continue;
        if (iter < v11)
        {
            do
            {
                v14 = *((short *)(2686 + (char *)idx + 4 * v12));
                v15 = (int)idx[5820];
                v11 = 16;
                if (v15 > v11 - v14)
                {
                    v16 = *((short *)(2684 + (char *)idx + 4 * v12));
                    v17 = (int)idx[8];
                    *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v16 << ((char)v15 & 31));
                    *((char *)(v17 + (int)idx[20])) = (char)idx[5816];
                    *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
                    *((char *)((int)idx[20] + (int)idx[8])) = (char)idx[5817];
                    v18 = (int)idx[5820];
                    *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
                    v19 = 16 - (char)v18;
                    v20 = v18 + v14 - 16;
                    v12 = v3;
                    *((unsigned short *)&idx[5816]) = ((16 - (char)v18 & 31) ? v16 >> (v19 & 31) : v16 >> (v19 & 31));
                    iter = v6;
                }
                else
                {
                    v21 = (int)idx[5820];
                    *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(*((short *)(2684 + (char *)idx + 4 * v12)) << ((char)v15 & 31));
                    v20 = v21 + v14;
                }
                iter -= 1;
                *((int *)&idx[5820]) = v20;
                v6 = iter;
            } while (iter != 1);
            goto LABEL_1034e7ee;
        }
        if (v12)
        {
            if (v12 != v2)
            {
                v22 = *((short *)(2686 + (char *)idx + 4 * v12));
                v23 = (int)idx[5820];
                v11 = 16;
                if (v23 > v11 - v22)
                {
                    v24 = *((short *)(2684 + (char *)idx + 4 * v12));
                    v25 = (int)idx[8];
                    *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v24 << ((char)v23 & 31));
                    *((char *)(v25 + (int)idx[20])) = (char)idx[5816];
                    *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
                    *((char *)((int)idx[20] + (int)idx[8])) = (char)idx[5817];
                    v26 = (int)idx[5820];
                    *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
                    v27 = 16 - (char)v26;
                    v28 = v26 + v22 - 16;
                    v12 = v3;
                    *((unsigned short *)&idx[5816]) = ((16 - (char)v26 & 31) ? v24 >> (v27 & 31) : v24 >> (v27 & 31));
                    iter = v6;
                }
                else
                {
                    v29 = (int)idx[5820];
                    *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(*((short *)(2684 + (char *)idx + 4 * v12)) << ((char)v23 & 31));
                    v28 = v29 + v22;
                }
                iter -= 1;
                *((int *)&idx[5820]) = v28;
                v6 = iter;
            }
            v30 = (int)idx[5820];
            v11 = 16;
            v3 = (short)idx[2750];
            if (v30 > v11 - v3)
            {
                v31 = (short)idx[2748];
                v32 = (int)idx[8];
                *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v31 << ((char)v30 & 31));
                *((char *)(v32 + (int)idx[20])) = (char)idx[5816];
                *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
                *((char *)((int)idx[20] + (int)idx[8])) = (char)idx[5817];
                v33 = (int)idx[5820];
                *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
                v34 = 16 - (char)v33;
                v35 = v33 + v3 - 16;
                *((unsigned short *)&idx[5816]) = ((16 - (char)v33 & 31) ? v31 >> (v34 & 31) : v31 >> (v34 & 31));
                iter = v6;
            }
            else
            {
                *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)((short)idx[2748] << ((char)v30 & 31));
                v35 = v30 + v3;
            }
            v36 = iter - 3;
            *((int *)&idx[5820]) = v35;
            if (v35 > 14)
            {
                v37 = (int)idx[8];
                *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v36 << ((char)v35 & 31));
                *((char *)(v37 + (int)idx[20])) = (char)idx[5816];
                *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
                *((char *)((int)idx[20] + (int)idx[8])) = (char)idx[5817];
                v38 = (int)idx[5820];
                *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
                v39 = v36 >> (16 - (char)v38 & 31);
                v40 = v38 - 14;
                goto LABEL_1034e7cd;
            }
            else
            {
                *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v36 << ((char)v35 & 31));
                v41 = v35 + 2;
                goto LABEL_1034e7e8;
            }
        }
        v42 = (int)idx[5820];
        v11 = 16;
        if (iter <= 10)
        {
            v3 = (short)idx[2754];
            if (v42 > v11 - v3)
            {
                v43 = (short)idx[2752];
                v44 = (int)idx[8];
                *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v43 << ((char)v42 & 31));
                *((char *)(v44 + (int)idx[20])) = (char)idx[5816];
                *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
                *((char *)((int)idx[20] + (int)idx[8])) = (char)idx[5817];
                v45 = (int)idx[5820];
                *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
                v46 = 16 - (char)v45;
                v47 = v45 + v3 - 16;
                *((unsigned short *)&idx[5816]) = ((16 - (char)v45 & 31) ? v43 >> (v46 & 31) : v43 >> (v46 & 31));
                iter = v6;
            }
            else
            {
                *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)((short)idx[2752] << ((char)v42 & 31));
                v47 = v42 + v3;
            }
            v48 = iter - 3;
            *((int *)&idx[5820]) = v47;
            if (v47 > 13)
            {
                v49 = (int)idx[8];
                *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v48 << ((char)v47 & 31));
                *((char *)(v49 + (int)idx[20])) = (char)idx[5816];
                *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
                *((char *)((int)idx[20] + (int)idx[8])) = (char)idx[5817];
                v50 = (int)idx[5820];
                *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
                v39 = v48 >> (16 - (char)v50 & 31);
                v40 = v50 - 13;
                goto LABEL_1034e7cd;
            }
            else
            {
                *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v48 << ((char)v47 & 31));
                v41 = v47 + 3;
                goto LABEL_1034e7e8;
            }
        }
        else
        {
            v3 = (short)idx[2758];
            if (v42 > v11 - v3)
            {
                v51 = (short)idx[2756];
                v52 = (int)idx[8];
                *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v51 << ((char)v42 & 31));
                *((char *)(v52 + (int)idx[20])) = (char)idx[5816];
                *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
                *((char *)((int)idx[20] + (int)idx[8])) = (char)idx[5817];
                v53 = (int)idx[5820];
                *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
                v54 = 16 - (char)v53;
                v55 = v53 + v3 - 16;
                *((unsigned short *)&idx[5816]) = ((16 - (char)v53 & 31) ? v51 >> (v54 & 31) : v51 >> (v54 & 31));
                iter = v6;
            }
            else
            {
                *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)((short)idx[2756] << ((char)v42 & 31));
                v55 = v42 + v3;
            }
            v56 = iter - 11;
            *((int *)&idx[5820]) = v55;
            if (v55 > 9)
            {
                v57 = (int)idx[8];
                *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v56 << ((char)v55 & 31));
                *((char *)(v57 + (int)idx[20])) = (char)idx[5816];
                *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
                *((char *)((int)idx[20] + (int)idx[8])) = (char)idx[5817];
                v58 = (int)idx[5820];
                *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
                v39 = v56 >> (16 - (char)v58 & 31);
                v40 = v58 - 9;
LABEL_1034e7cd:
                *((unsigned short *)&idx[5816]) = v39;
                *((unsigned int *)&idx[5820]) = v40;
                goto LABEL_1034e7ee;
            }
            else
            {
                *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v56 << ((char)v55 & 31));
                v41 = v55 + 7;
LABEL_1034e7e8:
                *((int *)&idx[5820]) = v41;
LABEL_1034e7ee:
                iter = 0;
                v2 = v12;
                if (!v5)
                {
                    v11 = 138;
                    goto LABEL_1034e7fd;
                }
                else if (v12 == v5)
                {
                    v11 = 6;
LABEL_1034e7fd:
                    v11 = 3;
                    goto LABEL_1034e810;
                }
                else
                {
                    v11 = 7;
                    v11 = 4;
LABEL_1034e810:
                }
            }
        }
        node = &node[2];
        v0 = i - 1;
    } while (i != 1);
    return;
}
```

## `sub_1034e823` `0x1034e823`

_566 bytes. (leaf/helper — see body)_

```c
extern char g_1039388c;

int sub_1034e823(void)
{
    unsigned int v4;  // ecx
    void* idx;  // eax
    int v14;  // edx
    int v15;  // ecx
    unsigned short v16;  // si
    unsigned int v17;  // ecx
    int v18;  // edx
    int iter;  // edi
    int v20;  // ecx
    unsigned int v21;  // edx
    unsigned short v22;  // si
    unsigned int v23;  // ecx
    int v6;  // ecx
    int v24;  // edx
    int v7;  // ebx
    unsigned short v8;  // si
    unsigned int v9;  // ecx
    int v10;  // edx
    int v11;  // ecx
    unsigned short v12;  // si
    unsigned int v13;  // ecx
    unsigned int v0;  // [bp-0x8], Other Possible Types: int
    unsigned int v1;  // [bp+0x4]
    unsigned int v2;  // [bp+0x8]
    int v3;  // [bp+0xc]

    v0 = v4;
    v6 = (int)idx[5820];
    v7 = v3;
    if (v6 > 11)
    {
        v8 = v1 - 0x101;
        v9 = (int)idx[20];
        *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v8 << ((char)v6 & 31));
        *((char *)(v9 + (int)idx[8])) = (char)idx[5816];
        *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
        *((char *)((int)idx[20] + (int)idx[8])) = (char)idx[5817];
        v10 = (int)idx[5820];
        *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
        v7 = v3;
        *((unsigned int *)&idx[5820]) = v10 - 11;
        *((unsigned short *)&idx[5816]) = v8 >> (16 - (char)v10 & 31);
    }
    else
    {
        *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v1 - 0x101 << ((char)v6 & 31));
        *((unsigned int *)&idx[5820]) = v6 + 5;
    }
    v11 = (int)idx[5820];
    if (v11 > 11)
    {
        v12 = v2 - 1;
        v13 = (int)idx[20];
        v0 = v7;
        *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v12 << ((char)v11 & 31));
        *((char *)(v13 + (int)idx[8])) = (char)idx[5816];
        *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
        *((char *)((int)idx[20] + (int)idx[8])) = (char)idx[5817];
        v14 = (int)idx[5820];
        *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
        v7 = v0;
        *((unsigned int *)&idx[5820]) = v14 - 11;
        *((unsigned short *)&idx[5816]) = v12 >> (16 - (char)v14 & 31);
    }
    else
    {
        *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v2 - 1 << ((char)v11 & 31));
        *((unsigned int *)&idx[5820]) = v11 + 5;
    }
    v15 = (int)idx[5820];
    if (v15 > 12)
    {
        v16 = v7 - 4;
        v17 = (int)idx[20];
        v0 = v7;
        *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v16 << ((char)v15 & 31));
        *((char *)(v17 + (int)idx[8])) = (char)idx[5816];
        *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
        *((char *)((int)idx[20] + (int)idx[8])) = (char)idx[5817];
        v18 = (int)idx[5820];
        *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
        v7 = v0;
        *((unsigned int *)&idx[5820]) = v18 - 12;
        *((unsigned short *)&idx[5816]) = v16 >> (16 - (char)v18 & 31);
    }
    else
    {
        *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v7 - 4 << ((char)v15 & 31));
        *((unsigned int *)&idx[5820]) = v15 + 4;
    }
    iter = 0;
    if (v7 <= 0)
    {
        sub_1034e389();
        sub_1034e389();
        return;
    }
    do
    {
        v20 = (int)idx[5820];
        v21 = (&g_1039388c)[iter];
        if (v20 > 13)
        {
            v22 = *((short *)(2686 + (char *)idx + 4 * v21));
            v23 = (int)idx[20];
            *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v22 << ((char)v20 & 31));
            *((char *)(v23 + (int)idx[8])) = (char)idx[5816];
            *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
            *((char *)((int)idx[20] + (int)idx[8])) = (char)idx[5817];
            v24 = (int)idx[5820];
            *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
            v7 = v3;
            *((unsigned int *)&idx[5820]) = v24 - 13;
            *((unsigned short *)&idx[5816]) = v22 >> (16 - (char)v24 & 31);
        }
        else
        {
            *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(*((short *)(2686 + (char *)idx + 4 * v21)) << ((char)v20 & 31));
            *((unsigned int *)&idx[5820]) = v20 + 3;
        }
    } while ((iter = (int)(iter + 1), iter < v7));
    sub_1034e389();
    sub_1034e389();
    return;
}
```

## `sub_1034ea59` `0x1034ea59`

_946 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned short field_0;
    unsigned short field_2;
    char padding_4[1020];
    unsigned short field_400;
    unsigned short field_402;
} struct_0;

extern unsigned int g_10393818[4];
extern char g_103938a0;
extern char g_10393e60;
extern char g_10393f60;
extern char g_10394060;
extern unsigned int g_10394160[4];
extern char g_103941d8;

int sub_1034ea59(void)
{
    struct_0 *v7;  // ebx
    unsigned int v8;  // ecx
    int v17;  // edx
    char v18;  // cl
    int v19;  // ecx
    unsigned int v20;  // edx
    unsigned int v21;  // ecx
    int v22;  // ecx
    unsigned short v23;  // di
    unsigned int v24;  // ecx
    int v25;  // edx
    char v26;  // cl
    void* idx;  // eax
    int v27;  // ecx
    unsigned int v28;  // ecx
    unsigned short v29;  // si
    int v30;  // ecx
    unsigned int v31;  // ecx
    int v32;  // edx
    char v33;  // cl
    int v34;  // ecx
    unsigned int v35;  // edi
    unsigned int v36;  // esi
    unsigned int v10;  // edi
    unsigned short v37[2];  // edx
    unsigned int v38;  // ecx
    int v39;  // ecx
    unsigned short v40;  // si
    unsigned int v41;  // ecx
    int v42;  // edx
    char v43;  // cl
    int v44;  // ecx
    unsigned short v45;  // di
    unsigned int v46;  // ecx
    unsigned int v11;  // esi
    int v47;  // edx
    char v48;  // cl
    int v49;  // ecx
    unsigned short v50;  // si
    unsigned int v51;  // ecx
    int v52;  // edx
    char v53;  // cl
    int v54;  // ecx
    int v12;  // ecx
    struct_0 *v13;  // esi
    unsigned int v14;  // edi
    unsigned short v15;  // si
    unsigned int v16;  // ecx
    unsigned int v0;  // [bp-0x24]
    struct_0 *v1;  // [bp-0x14], Other Possible Types: unsigned int
    struct_0 *v2;  // [bp-0x10], Other Possible Types: unsigned int
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    struct_0 *v5;  // [bp+0x4], Other Possible Types: unsigned int
    unsigned int v6;  // [bp+0x8]

    v7 = v5;
    v8 = 0;
    if ((int)idx[5792])
    {
        do
        {
            v10 = *((short *)((int)idx[5796] + v8 * 2));
            v11 = *((char *)(v8 + (int)idx[5784]));
            v2 = v10;
            v1 = v8 + 1;
            v0 = 16;
            if (!v10)
            {
                v12 = (int)idx[5820];
                v13 = &(&v7->field_0)[2 * v11];
                v14 = v13->field_2;
                if (v12 > v0 - v14)
                {
                    v15 = v13->field_0;
                    v16 = (int)idx[8];
                    *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v15 << ((char)v12 & 31));
                    *((char *)(v16 + (int)idx[20])) = (char)idx[5816];
                    *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
                    *((char *)((int)idx[20] + (int)idx[8])) = (char)idx[5817];
                    v17 = (int)idx[5820];
                    *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
                    v7 = v5;
                    v18 = 16 - (char)v17;
                    v19 = v17 + v14 - 16;
                    *((unsigned short *)&idx[5816]) = ((16 - (char)v17 & 31) ? v15 >> (v18 & 31) : v15 >> (v18 & 31));
                }
                else
                {
                    *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v13->field_0 << ((char)v12 & 31));
                    v19 = v12 + v14;
                }
            }
            else
            {
                v20 = (&g_10394060)[v11];
                v4 = v20 * 4;
                v21 = *((short *)(1030 + v4 + (char *)v7));
                v3 = v21;
                v22 = (int)idx[5820];
                if (v22 > v0 - v21)
                {
                    v23 = (&v5[1].field_0)[2 * v20];
                    v24 = (int)idx[8];
                    *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v23 << ((char)v22 & 31));
                    *((char *)(v24 + (int)idx[20])) = (char)idx[5816];
                    *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
                    *((char *)((int)idx[20] + (int)idx[8])) = (char)idx[5817];
                    v25 = (int)idx[5820];
                    *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
                    v26 = 16 - (char)v25;
                    v27 = v25 + v3 - 16;
                    *((unsigned short *)&idx[5816]) = ((16 - (char)v25 & 31) ? v23 >> (v26 & 31) : v23 >> (v26 & 31));
                    v10 = v2;
                }
                else
                {
                    *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)((&v5[1].field_0)[2 * v20] << ((char)v22 & 31));
                    v27 = v22 + v3;
                }
                *((int *)&idx[5820]) = v27;
                v28 = v4;
                v4 = *((int *)(v28 + (char *)&g_10393818[0]));
                if (v4)
                {
                    v29 = v11 - *((int *)(v28 + (char *)&g_10394160[0]));
                    v30 = (int)idx[5820];
                    v0 = 16;
                    if (v30 > v0 - v4)
                    {
                        v31 = (int)idx[8];
                        *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v29 << ((char)v30 & 31));
                        *((char *)(v31 + (int)idx[20])) = (char)idx[5816];
                        *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
                        *((char *)((int)idx[20] + (int)idx[8])) = (char)idx[5817];
                        v32 = (int)idx[5820];
                        *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
                        v33 = 16 - (char)v32;
                        v34 = v32 + v4 - 16;
                        *((unsigned short *)&idx[5816]) = ((16 - (char)v32 & 31) ? v29 >> (v33 & 31) : v29 >> (v33 & 31));
                    }
                    else
                    {
                        *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v29 << ((char)v30 & 31));
                        v34 = v30 + v4;
                    }
                    *((int *)&idx[5820]) = v34;
                }
                v35 = v10 - 1;
                v36 = (v35 < 0x100 ? (&g_10393e60)[v35] : (&g_10393f60)[v35 >> 7]) * 4;
                v37 = v36 + v6;
                v38 = v37[1];
                v0 = 16;
                v3 = v38;
                v39 = (int)idx[5820];
                v4 = v36;
                if (v39 > v0 - v38)
                {
                    v40 = v37[0];
                    v41 = (int)idx[8];
                    *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v40 << ((char)v39 & 31));
                    *((char *)(v41 + (int)idx[20])) = (char)idx[5816];
                    *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
                    *((char *)((int)idx[20] + (int)idx[8])) = (char)idx[5817];
                    v42 = (int)idx[5820];
                    *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
                    v43 = 16 - (char)v42;
                    v44 = v42 + v3 - 16;
                    *((unsigned short *)&idx[5816]) = ((16 - (char)v42 & 31) ? v40 >> (v43 & 31) : v40 >> (v43 & 31));
                    v36 = v4;
                }
                else
                {
                    *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v37[0] << ((char)v39 & 31));
                    v44 = v39 + v3;
                }
                v7 = v5;
                *((int *)&idx[5820]) = v44;
                v4 = *((int *)&(&g_103938a0)[v36]);
                if (!v4)
                    continue;
                v45 = v35 - *((int *)&(&g_103941d8)[v36]);
                v0 = 16;
                if (v44 > v0 - v4)
                {
                    v46 = (int)idx[8];
                    v2 = v7;
                    *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v45 << ((char)v44 & 31));
                    *((char *)(v46 + (int)idx[20])) = (char)idx[5816];
                    *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
                    v7 = v2;
                    *((char *)((int)idx[20] + (int)idx[8])) = (char)idx[5817];
                    v47 = (int)idx[5820];
                    *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
                    v48 = 16 - (char)v47;
                    v19 = v47 + v4 - 16;
                    *((unsigned short *)&idx[5816]) = ((16 - (char)v47 & 31) ? v45 >> (v48 & 31) : v45 >> (v48 & 31));
                }
                else
                {
                    *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v45 << ((char)v44 & 31));
                    v19 = v44 + v4;
                }
            }
            *((int *)&idx[5820]) = v19;
        } while ((v8 = v1, v8 < (int)idx[5792]));
    }
    v49 = (int)idx[5820];
    v0 = 16;
    v5 = v7->field_402;
    if (v49 > v0 - v5)
    {
        v50 = v7->field_400;
        v51 = (int)idx[8];
        v1 = v7;
        *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v50 << ((char)v49 & 31));
        *((char *)(v51 + (int)idx[20])) = (char)idx[5816];
        *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
        v7 = v1;
        *((char *)((int)idx[20] + (int)idx[8])) = (char)idx[5817];
        v52 = (int)idx[5820];
        *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
        v53 = 16 - (char)v52;
        v54 = v52 + v5 - 16;
        *((unsigned short *)&idx[5816]) = ((16 - (char)v52 & 31) ? v50 >> (v53 & 31) : v50 >> (v53 & 31));
    }
    else
    {
        *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v7->field_400 << ((char)v49 & 31));
        v54 = v49 + v5;
    }
    *((int *)&idx[5820]) = v54;
    *((unsigned int *)&idx[5812]) = v7->field_402;
    return;
}
```

## `sub_1034ee0b` `0x1034ee0b`

_66 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[44];
    unsigned int field_2c;
} struct_0;

typedef struct struct_2 {
    struct struct_0 *field_0;
    char padding_4[144];
    unsigned short field_94;
    char padding_96[54];
    unsigned short field_cc;
} struct_2;

struct_0 * sub_1034ee0b(unsigned int a0, struct_2 *a1)
{
    int iter;  // eax
    struct_2 *v2;  // ecx
    struct_2 *v3;  // ecx
    struct_0 *v4;  // eax

    iter = 0;
    v2 = &a1->field_94;
    do
    {
    } while (!(short)v2->field_0 && (iter = (int)(iter + 1), v2 += 4, iter < 9));
    if (iter == 9)
    {
        iter = 14;
        v3 = &a1->field_cc;
        do
        {
        } while (!(short)v3->field_0 && (iter = (int)(iter + 1), v3 += 4, iter < 32));
    }
    v4 = a1->field_0;
    v4->field_2c = iter == 32;
    return v4;
}
```

## `sub_1034ee4d` `0x1034ee4d`

_31 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1034ee4d(unsigned int a0, int i)
{
    unsigned int v0;  // eax
    unsigned int v1;  // eax
    unsigned int v2;  // eax

    v0 = 0;
    do
    {
        a0 >>= 1;
        v2 = (v0 | a0 & 1) * 2;
        i -= 1;
        v0 = v2;
    } while (i > 0);
    return (v1 | a0 & 1) & 2147483647;
}
```

## `sub_1034ee6c` `0x1034ee6c`

_109 bytes. (leaf/helper — see body)_

```c
int sub_1034ee6c(void)
{
    void* idx;  // eax
    void* v3;  // ecx
    unsigned int v4;  // esi
    unsigned short v5;  // dx
    unsigned int v0;  // [bp-0x8]

    if ((int)idx[5820] == 16)
    {
        *((char *)((int)idx[8] + (int)idx[20])) = (char)idx[5816];
        *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
        *((char *)((int)idx[20] + (int)idx[8])) = (char)idx[5817];
        *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
        *((unsigned short *)&idx[5816]) = 0;
        *((int *)&idx[5820]) = 0;
        return;
    }
    if ((int)idx[5820] < 8)
        return;
    v3 = idx + 5816;
    v0 = v4;
    *((char *)((int)idx[8] + (int)idx[20])) = *((char *)v3);
    v5 = (char)v3[1];
    *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
    *((unsigned int *)&idx[5820]) = (int)idx[5820] - 8;
    *((unsigned short *)v3) = v5;
    return;
}
```

## `sub_1034eed9` `0x1034eed9`

_87 bytes. (leaf/helper — see body)_

```c
int sub_1034eed9(void)
{
    void* idx;  // eax
    unsigned int v3;  // esi
    void* v4;  // ecx
    unsigned int v0;  // [bp-0x8]

    if ((int)idx[5820] > 8)
    {
        v0 = v3;
        v4 = idx + 5816;
        *((char *)((int)idx[8] + (int)idx[20])) = *((char *)v4);
        *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
        *((char *)((int)idx[20] + (int)idx[8])) = (char)v4[1];
        *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
    }
    else if ((int)idx[5820] > 0)
    {
        *((char *)((int)idx[8] + (int)idx[20])) = (char)idx[5816];
        *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
    }
    *((unsigned short *)&idx[5816]) = 0;
    *((int *)&idx[5820]) = 0;
    return;
}
```

## `sub_1034ef30` `0x1034ef30`

_120 bytes. (leaf/helper — see body)_

```c
void sub_1034ef30(unsigned int a0, char *i, unsigned int a2)
{
    unsigned int v4;  // ebx
    unsigned int idx[1454];  // eax
    unsigned int v6;  // esi
    unsigned int v0;  // [bp-0x10]
    int v1;  // [bp-0xc]
    int v2;  // [bp-0x8]
    char v3;  // [bp+0x0]

    v4 = a0;
    idx = sub_1034eed9(v1, v2, &v3);
    idx[1453] = 8;
    if (a2)
    {
        *((char *)(idx[5] + idx[2])) = v4;
        idx[5] = idx[5] + 1;
        *((char *)(idx[5] + idx[2])) = *((char *)((void*)&v4 + 1));
        idx[5] = idx[5] + 1;
        v0 = v6;
        *((char *)(idx[5] + idx[2])) = ~((char)v4);
        idx[5] = idx[5] + 1;
        *((char *)(idx[5] + idx[2])) = *((char *)((void*)&~(v4) + 1));
        idx[5] = idx[5] + 1;
    }
    for (; v4; i += 1)
    {
        a2 = v4 - 1;
        *((char *)(idx[5] + idx[2])) = *(i);
        idx[5] = idx[5] + 1;
        v4 = a2;
    }
    return;
}
```

## `sub_1034efa8` `0x1034efa8`

_100 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[2840];
    struct struct_0 *field_b18;
    char padding_b1c[8];
    struct struct_0 *field_b24;
    char padding_b28[8];
    struct struct_0 *field_b30;
    char padding_b34[2944];
    unsigned int field_16b4;
    unsigned short field_16b8;
    char padding_16ba[2];
    unsigned int field_16bc;
} struct_0;

extern char g_1038df4c;
extern char g_1038df60;
extern char g_1038df74;

int sub_1034efa8(struct_0 *idx)
{
    idx->field_16b8 = 0;
    idx->field_16bc = 0;
    idx->field_b18 = &idx->padding_0[148];
    idx->field_b24 = &idx->padding_0[2440];
    *((char **)&idx->padding_b1c[4]) = &g_1038df4c;
    *((char **)&idx->padding_b28[4]) = &g_1038df60;
    idx->field_b30 = &idx->padding_0[2684];
    *((char **)&idx->padding_b34[4]) = &g_1038df74;
    idx->field_16b4 = 8;
    return sub_1034e002();
}
```

## `sub_1034f00c` `0x1034f00c`

_119 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_1034f00c(unsigned int a0, unsigned int a1, int a2)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // edi
    int index;  // ebx
    unsigned short v9;  // ax
    int idx;  // ecx
    unsigned int v11;  // esi
    unsigned int v12;  // ecx
    char v13[2];  // eax
    unsigned short v14;  // dx
    unsigned int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x2c]
    char v2;  // [bp-0x28]
    char v3;  // [bp-0x26]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = g_1038e180 ^ &v5;
    v1 = v6;
    v0 = v7;
    index = 0;
    v9 = 0;
    idx = 1;
    do
    {
        v9 = (*((short *)(&v2 + a1 - &v3 + 2 * idx)) + v9) * 2;
        *((unsigned short *)&(&v2)[2 * idx]) = v9;
        idx += 1;
    } while (idx <= 15);
    if (a2 >= 0)
    {
        do
        {
            v12 = *((short *)(v11 + index * 4 + 2));
            if (v12)
            {
                v13 = &(&v2)[2 * v12];
                v14 = (unsigned short)*(v13);
                *((unsigned short *)&v13[0]) = v14 + 1;
                *((unsigned short *)(v11 + index * 4)) = sub_1034ee4d(v14, v12);
            }
        } while ((index = (int)(index + 1), index <= a2));
    }
    return sub_10351225();
}
```

## `sub_1034f083` `0x1034f083`

_488 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    unsigned int field_0;
    int field_4;
    struct struct_0 *field_8;
} struct_1;

typedef struct struct_2 {
    char padding_0[2912];
    int field_b60;
    char padding_b64[2284];
    unsigned int field_1450;
    unsigned int field_1454;
    char padding_1458[592];
    unsigned int field_16a8;
    unsigned int field_16ac;
} struct_2;

typedef struct struct_0 {
    unsigned int field_0;
    char padding_4[8];
    int field_c;
} struct_0;

int sub_1034f083(struct_1 *index)
{
    unsigned int v5;  // edx
    int v6;  // eax
    unsigned short v15[2];  // ecx
    int idx;  // ecx
    unsigned short v17;  // ax
    unsigned int v18;  // ecx
    unsigned int v7;  // edi
    struct_2 *idx1;  // ebx
    int v9;  // eax
    unsigned int v10;  // ecx
    int i;  // esi
    int v12;  // ecx
    int v13;  // esi
    int v14;  // eax
    unsigned short v0[2];  // [bp-0x18]
    unsigned short v1[2];  // [bp-0x14]
    int v2;  // [bp-0x10]
    int iter;  // [bp-0xc]
    int v4;  // [bp-0x8]

    iter = -1;
    v5 = index->field_8->field_0;
    v6 = 0;
    v7 = index->field_0;
    v4 = index->field_8->field_c;
    idx1->field_1450 = 0;
    idx1->field_1454 = 573;
    if (v4 > 0)
    {
        do
        {
            if (*((short *)(v7 + v6 * 4)))
            {
                idx1->field_1450 = idx1->field_1450 + 1;
                *((int *)&idx1->padding_0[2908 + 4 * idx1->field_1450]) = v6;
                iter = v6;
                idx1->padding_1458[v6] = 0;
            }
            else
            {
                *((unsigned short *)(v7 + v6 * 4 + 2)) = 0;
            }
        } while ((v6 = (int)(v6 + 1), v6 < v4));
    }
    for (; idx1->field_1450 < 2; idx1->field_16ac = idx1->field_16ac - *((short *)(v10 + v5 + 2)))
    {
        if (iter < 2)
        {
            iter += 1;
            v9 = iter;
        }
        else
        {
            v9 = 0;
        }
        idx1->field_1450 = idx1->field_1450 + 1;
        *((int *)&idx1->padding_0[2908 + 4 * idx1->field_1450]) = v9;
        v10 = v9 * 4;
        *((unsigned short *)(v10 + v7)) = 1;
        idx1->padding_1458[v9] = 0;
        idx1->field_16a8 = idx1->field_16a8 - 1;
    }
    index->field_4 = iter;
    for (i = idx1->field_1450 / 2; i >= 1; i -= 1)
    {
        sub_1034e060(i);
    }
    v2 = v4;
    do
    {
        v12 = *((int *)&idx1->padding_0[2908 + 4 * idx1->field_1450]);
        v13 = idx1->field_b60;
        idx1->field_1450 = idx1->field_1450 - 1;
        idx1->field_b60 = v12;
        sub_1034e060(1);
        idx1->field_1454 = idx1->field_1454 - 1;
        v14 = idx1->field_b60;
        *((int *)&idx1->padding_0[2908 + 4 * idx1->field_1454]) = v13;
        idx1->field_1454 = idx1->field_1454 - 1;
        *((int *)&idx1->padding_0[2908 + 4 * idx1->field_1454]) = v14;
        v15 = v7 + v14 * 4;
        v1 = v15;
        v0 = v7 + v13 * 4;
        idx = v2;
        *((unsigned short *)(v7 + idx * 4)) = v15[0] + v0[0];
        idx1->padding_1458[idx] = (idx1->padding_1458[v13] < idx1->padding_1458[v14] ? idx1->padding_1458[v14] : idx1->padding_1458[v13]) + 1;
        v17 = idx;
        v1[1] = v17;
        v0[1] = v17;
        idx1->field_b60 = idx;
        v2 = idx + 1;
        sub_1034e060(1);
    } while (idx1->field_1450 >= 2);
    idx1->field_1454 = idx1->field_1454 - 1;
    *((int *)&idx1->padding_0[2908 + 4 * idx1->field_1454]) = idx1->field_b60;
    sub_1034e110();
    return sub_1034f00c(v18, &idx1->padding_0[2876], iter);
}
```

## `sub_1034f26b` `0x1034f26b`

_97 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[5800];
    unsigned int field_16a8;
} struct_0;

extern char g_1039388c;

int sub_1034f26b(void)
{
    struct_0 *idx;  // eax
    int v0;  // [bp-0x8]
    int v1;  // [bp-0x4]

    sub_1034e2cd(idx, v1);
    sub_1034e2cd(idx);
    sub_1034f083(&idx->padding_0[2864]);
    v0 = 18;
    do
    {
    } while (!*((short *)&idx->padding_0[2686 + 4 * (&g_1039388c)[v0]]) && (v0 = (int)(v0 - 1), v0 >= 3));
    idx->field_16a8 = idx->field_16a8 + v0 * 3 + 0x11;
    return;
}
```

## `sub_1034f2cc` `0x1034f2cc`

_139 bytes. (leaf/helper — see body)_

```c
void sub_1034f2cc(void* idx, char *a1, unsigned int a2, unsigned short a3)
{
    int v2;  // ecx
    unsigned int v3;  // ebx
    unsigned int v4;  // esi
    unsigned int v5;  // ecx
    int v6;  // edx
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v2 = (int)idx[5820];
    if (v2 <= 13)
    {
        *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(a3 << ((char)v2 & 31));
        *((unsigned int *)&idx[5820]) = v2 + 3;
        sub_1034ef30(a2, a1, 1);
        return;
    }
    v1 = v3;
    v0 = v4;
    v5 = (int)idx[8];
    *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(a3 << ((char)v2 & 31));
    *((char *)(v5 + (int)idx[20])) = (char)idx[5816];
    *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
    *((char *)((int)idx[20] + (int)idx[8])) = (char)idx[5817];
    v6 = (int)idx[5820];
    *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
    *((unsigned int *)&idx[5820]) = v6 - 13;
    *((unsigned short *)&idx[5816]) = a3 >> (16 - (char)v6 & 31);
    sub_1034ef30(a2, a1, 1);
    return;
}
```

## `sub_1034f357` `0x1034f357`

_455 bytes. (leaf/helper — see body)_

```c
void sub_1034f357(void* index)
{
    int v1;  // ecx
    int v2;  // edx
    int v3;  // ecx
    int v4;  // edx
    void* idx;  // eax
    int v6;  // ecx
    int v7;  // edx
    int v8;  // ecx
    int v9;  // edx
    unsigned int v0;  // [bp-0xc]

    v1 = (int)index[5820];
    v0 = 2;
    *((unsigned short *)&index[5816]) = (short)index[5816] | (unsigned short)(v0 << ((char)v1 & 31));
    if (v1 > 13)
    {
        *((char *)((int)index[8] + (int)index[20])) = (char)index[5816];
        *((unsigned int *)&index[20]) = (int)index[20] + 1;
        *((char *)((int)index[20] + (int)index[8])) = (char)index[5817];
        v2 = (int)index[5820];
        *((unsigned int *)&index[20]) = (int)index[20] + 1;
        *((unsigned int *)&index[5820]) = v2 - 13;
        *((unsigned short *)&index[5816]) = 2 >> (16 - (char)v2 & 31);
    }
    else
    {
        *((unsigned int *)&index[5820]) = v1 + 3;
    }
    v3 = (int)index[5820];
    *((unsigned short *)&index[5816]) = (short)index[5816] | (unsigned short)(0 << ((char)v3 & 31));
    if (v3 > 9)
    {
        *((char *)((int)index[8] + (int)index[20])) = (char)index[5816];
        *((unsigned int *)&index[20]) = (int)index[20] + 1;
        *((char *)((int)index[20] + (int)index[8])) = (char)index[5817];
        v4 = (int)index[5820];
        *((unsigned int *)&index[20]) = (int)index[20] + 1;
        *((unsigned int *)&index[5820]) = v4 - 9;
        *((unsigned short *)&index[5816]) = 0 >> (16 - (char)v4 & 31);
    }
    else
    {
        *((unsigned int *)&index[5820]) = v3 + 7;
    }
    idx = sub_1034ee6c();
    v6 = (int)idx[5820];
    if ((int)idx[5812] - v6 + 11 < 9)
    {
        v0 = 2;
        *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v0 << ((char)v6 & 31));
        if (v6 > 13)
        {
            *((char *)((int)idx[8] + (int)idx[20])) = (char)idx[5816];
            *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
            *((char *)((int)idx[20] + (int)idx[8])) = (char)idx[5817];
            v7 = (int)idx[5820];
            *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
            *((unsigned int *)&idx[5820]) = v7 - 13;
            *((unsigned short *)&idx[5816]) = 2 >> (16 - (char)v7 & 31);
        }
        else
        {
            *((unsigned int *)&idx[5820]) = v6 + 3;
        }
        v8 = (int)idx[5820];
        *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(0 << ((char)v8 & 31));
        if (v8 > 9)
        {
            *((char *)((int)idx[8] + (int)idx[20])) = (char)idx[5816];
            *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
            *((char *)((int)idx[20] + (int)idx[8])) = (char)idx[5817];
            v9 = (int)idx[5820];
            *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
            *((unsigned int *)&idx[5820]) = v9 - 9;
            *((unsigned short *)&idx[5816]) = 0 >> (16 - (char)v9 & 31);
        }
        else
        {
            *((unsigned int *)&idx[5820]) = v8 + 7;
        }
        idx = sub_1034ee6c();
    }
    *((unsigned int *)&idx[5812]) = 7;
    return;
}
```

## `sub_1034f51e` `0x1034f51e`

_501 bytes. (leaf/helper — see body)_

```c
extern int g_10393968;
extern int g_10393de8;

int sub_1034f51e(unsigned int a0, unsigned int a1, void* idx, char *a3, unsigned int a4, unsigned int a5)
{
    unsigned int v3;  // ebx
    unsigned int v4;  // esi
    unsigned short v11;  // si
    unsigned int v12;  // ecx
    int v13;  // edx
    int v14;  // ecx
    unsigned short v15;  // si
    unsigned int v16;  // ecx
    int v17;  // eax
    unsigned int v18;  // eax
    unsigned int v5;  // edi
    int v6;  // edi
    int v7;  // eax
    unsigned int v8;  // ecx
    unsigned int v9;  // ecx
    int v10;  // ecx
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v2 = v3;
    v1 = v4;
    v0 = v5;
    v6 = 0;
    if ((int)idx[132] > 0)
    {
        if (a4 > 0 && *((int *)(*((int *)idx) + 44)) == 2)
            sub_1034ee0b(a0, idx);
        sub_1034f083(idx + 2840);
        sub_1034f083(idx + 2852);
        v7 = sub_1034f26b();
        v8 = (int)idx[5800] + 10 >> 3;
        v8 = (int)idx[5804] + 10 >> 3;
        v6 = v7;
        if (v8 > v8)
            goto LABEL_1034f58d;
    }
    else
    {
        v8 = a4 + 5;
    }
LABEL_1034f58d:
    v9 = v8;
    if (a4 + 4 <= v8 && a3)
    {
        sub_1034f2cc(idx, a3, a4, a5);
    }
    else if ((int)idx[0x88] != 4 && v9 != v8)
    {
        v10 = (int)idx[5820];
        if (v10 > 13)
        {
            v11 = (unsigned short)a5 + 4;
            v12 = (int)idx[20];
            *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v11 << ((char)v10 & 31));
            *((char *)((int)idx[8] + v12)) = (char)idx[5816];
            *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
            *((char *)((int)idx[20] + (int)idx[8])) = (char)idx[5817];
            v13 = (int)idx[5820];
            *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
            *((unsigned int *)&idx[5820]) = v13 - 13;
            *((unsigned short *)&idx[5816]) = v11 >> (16 - (char)v13 & 31);
        }
        else
        {
            *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(a5 + 4 << ((char)v10 & 31));
            *((unsigned int *)&idx[5820]) = v10 + 3;
        }
        sub_1034e823((int)idx[2844] + 1, (int)idx[2856] + 1, v6 + 1);
        sub_1034ea59(idx + 148, idx + 2440);
    }
    else
    {
        v14 = (int)idx[5820];
        if (v14 > 13)
        {
            v15 = (unsigned short)a5 + 2;
            v16 = (int)idx[20];
            *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(v15 << ((char)v14 & 31));
            *((char *)((int)idx[8] + v16)) = (char)idx[5816];
            *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
            *((char *)((int)idx[20] + (int)idx[8])) = (char)idx[5817];
            v17 = (int)idx[5820];
            *((unsigned int *)&idx[20]) = (int)idx[20] + 1;
            *((unsigned int *)&idx[5820]) = v17 - 13;
            *((unsigned short *)&idx[5816]) = v15 >> (16 - (char)v17 & 31);
        }
        else
        {
            *((unsigned short *)&idx[5816]) = (short)idx[5816] | (unsigned short)(a5 + 2 << ((char)v14 & 31));
            *((unsigned int *)&idx[5820]) = v14 + 3;
        }
        sub_1034ea59(&g_10393968, &g_10393de8);
    }
    v18 = sub_1034e002();
    if (!a5)
        return v18;
    return sub_1034eed9();
}
```

## `sub_1034f713` `0x1034f713`

_17 bytes. (leaf/helper — see body)_

```c
int sub_1034f713(unsigned int a0, unsigned int a1, int a2)
{
    return sub_10355a15(a2 * a1);
}
```

## `sub_1034f724` `0x1034f724`

_11 bytes. (leaf/helper — see body)_

```c
void sub_1034f724(unsigned int a0, int a1)
{
    sub_1035345e(a1);
    return;
}
```

## `sub_1034f72f` `0x1034f72f`

_988 bytes. refs "invalid distance code", "invalid distance too far back", "invalid literal/length code"_

```c
typedef struct struct_1 {
    void* field_0;
    unsigned int field_4;
    char padding_8[4];
    void* field_c;
    unsigned int field_10;
    char padding_14[8];
    struct struct_0 *field_1c;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
    char padding_4[36];
    unsigned int field_28;
    unsigned int field_2c;
    unsigned int field_30;
    unsigned int field_34;
    unsigned int field_38;
    unsigned int field_3c;
    char padding_40[12];
    unsigned int field_4c;
    unsigned int field_50;
    unsigned int field_54;
    unsigned int field_58;
} struct_0;


unsigned int sub_1034f72f(struct_1 *a0, unsigned int node)
{
    struct_1 *idx;  // eax
    void* iter;  // ebx
    void* v26;  // ebx
    unsigned int v27;  // ecx
    unsigned int v28;  // edx
    unsigned int v29;  // ecx
    unsigned int v30;  // ecx
    unsigned int v31;  // ecx
    unsigned int v32;  // ecx
    unsigned int v33;  // edx
    unsigned int v34;  // ecx
    unsigned int v35;  // edx
    struct_0 *index;  // esi
    unsigned int v36;  // ecx
    unsigned int v37;  // ecx
    char iter1[3];  // ecx, Other Possible Types: unsigned int
    unsigned int j;  // 4099
    unsigned int k;  // ecx
    unsigned int v42;  // ecx
    void* iter2;  // edi
    unsigned int l;  // 4099
    unsigned int m;  // 4099
    unsigned int n;  // eax
    char v46[3];  // ecx
    void* v47;  // edi
    char v48[3];  // ecx
    unsigned int v49;  // edi
    void* v20;  // ebx
    char v51[3];  // ecx
    void* v52;  // edi
    char v53[3];  // ecx
    unsigned int v54;  // edi
    char v55[3];  // ecx
    unsigned int v56;  // ecx
    unsigned int v21;  // edx
    void* v57;  // ebx
    unsigned int v22;  // ecx
    unsigned int v23;  // ecx
    unsigned int v24;  // ecx
    unsigned int v25;  // ecx
    unsigned int v0;  // [bp-0x54]
    unsigned int v1;  // [bp-0x44]
    unsigned int v2;  // [bp-0x40]
    unsigned int v3;  // [bp-0x3c]
    unsigned int v4;  // [bp-0x38]
    void* v5;  // [bp-0x34]
    void* v6;  // [bp-0x30]
    unsigned int v7;  // [bp-0x2c]
    unsigned int v8;  // [bp-0x28]
    unsigned int v9;  // [bp-0x24]
    unsigned int v10;  // [bp-0x20]
    unsigned int v11;  // [bp-0x1c]
    unsigned int v12;  // [bp-0x18]
    unsigned int i0;  // [bp-0x10]
    unsigned int i;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    idx = a0;
    iter = idx->field_0 - 1;
    v6 = idx->field_4 + iter - 5;
    index = idx->field_1c;
    iter2 = idx->field_c - 1;
    v2 = idx->field_10 - node + iter2;
    v5 = idx->field_10 + iter2 - 0x101;
    v8 = index->field_28;
    v1 = index->field_2c;
    v11 = index->field_30;
    v7 = index->field_34;
    v15 = index->field_38;
    node = index->field_3c;
    v10 = index->field_4c;
    v9 = index->field_50;
    v4 = (1 << ((char)index->field_54 & 31)) - 1;
    v3 = (1 << ((char)index->field_58 & 31)) - 1;
    while (true)
    {
        if (node < 15)
        {
            node += 8;
            v20 = iter + 1;
            v15 += *((char *)v20) << ((char)node & 31);
            iter = v20 + 1;
            v15 += *((char *)iter) << ((char)node & 31);
            node += 8;
        }
        iter1 = *((int *)(v10 + (v4 & v15) * 4));
        v21 = iter1;
        v22 = (char)(*((int *)(v10 + (v4 & v15) * 4)) >> 8);
        v15 >>= (char)v22 & 31;
        node -= v22;
        i = v22;
        i = (char)v21;
        if (i)
        {
            do
            {
                v23 = i;
                if (((char)v23 & 16))
                {
                    i0 = v21 >> 16;
                    i = v23 & 15;
                    if (((char)v23 & 15))
                    {
                        if (node < i)
                        {
                            iter += 1;
                            v15 += *((char *)iter) << ((char)node & 31);
                            node += 8;
                        }
                        v25 = i;
                        v15 >>= (char)v25 & 31;
                        i0 += (1 << ((char)v25 & 31)) - 1 & v15;
                        node -= v25;
                    }
                    if (node < 15)
                    {
                        node += 8;
                        v26 = iter + 1;
                        v15 += *((char *)v26) << ((char)node & 31);
                        iter = v26 + 1;
                        v15 += *((char *)iter) << ((char)node & 31);
                        node += 8;
                    }
                    v27 = *((int *)(v9 + (v3 & v15) * 4));
                    while (true)
                    {
                        iter1 = v27;
                        v29 = (char)(v27 >> 8);
                        v15 >>= (char)v29 & 31;
                        node -= v29;
                        i = v29;
                        v30 = (char)iter1;
                        if (((char)v30 & 16))
                            break;
                        if (((char)v30 & 64))
                        {
                            *((char **)&idx->padding_14[4]) = "invalid distance code";
                            index->field_0 = 27;
                            v56 = node >> 3;
                            v57 = iter - v56;
                            node -= v56 * 8;
                            idx->field_0 = v57 + 1;
                            idx->field_c = iter2 + 1;
                            idx->field_4 = v6 - v57 + 5;
                            idx->field_10 = v5 - iter2 + 0x101;
                            index->field_38 = v15 & (1 << ((char)node & 31)) - 1;
                            index->field_3c = node;
                            return node;
                        }
                        v27 = *((int *)(v9 + (((1 << ((char)v30 & 31)) - 1 & v15) + *((unsigned short *)((void*)&iter1 + 2))) * 4));
                    }
                    v31 = v30 & 15;
                    v12 = v28 >> 16;
                    i = v31;
                    if (node < v31)
                    {
                        node += 8;
                        iter += 1;
                        v31 = i;
                        v15 += *((char *)iter) << ((char)node & 31);
                        if (node < v31)
                        {
                            iter += 1;
                            v31 = i;
                            v15 += *((char *)iter) << ((char)node & 31);
                            node += 8;
                        }
                    }
                    v32 = i;
                    node -= v32;
                    v15 >>= (char)v32 & 31;
                    v12 += (1 << ((char)v31 & 31)) - 1 & v15;
                    v33 = v12;
                    v34 = iter2 - v2;
                    if (v33 <= v34)
                    {
                        iter1 = iter2 - v33;
                        do
                        {
                            i0 -= 3;
                            v51 = &iter1[1];
                            v52 = iter2 + 1;
                            *((char *)v52) = v51[0];
                            v53 = &v51[1];
                            v54 = v52 + 1;
                            iter1 = &v53[1];
                            *((char *)v54) = v53[0];
                            iter2 = v54 + 1;
                            *((char *)iter2) = iter1[0];
                        } while (i0 > 2);
LABEL_1034fa65:
                        if (i0)
                        {
                            v55 = &iter1[1];
                            iter2 += 1;
                            *((char *)iter2) = v55[0];
                            if (i0 > 1)
                            {
                                iter2 += 1;
                                *((char *)iter2) = v55[1];
                                goto LABEL_1034fa7d;
                            }
                        }
                    }
                    v35 = v33 - v34;
                    i = v35;
                    if (v35 > v1)
                    {
                        *((char **)&idx->padding_14[4]) = "invalid distance too far back";
                        index->field_0 = 27;
                        v56 = node >> 3;
                        v57 = iter - v56;
                        node -= v56 * 8;
                        idx->field_0 = v57 + 1;
                        idx->field_c = iter2 + 1;
                        idx->field_4 = v6 - v57 + 5;
                        idx->field_10 = v5 - iter2 + 0x101;
                        index->field_38 = v15 & (1 << ((char)node & 31)) - 1;
                        index->field_3c = node;
                        return node;
                    }
                    iter1 = v7 - 1;
                    v36 = v11;
                    if (!v36)
                    {
                        iter1 = &iter1[v8 + -1 * v35];
                        v37 = v35;
                        if (v37 >= i0)
                            goto LABEL_1034fa0e;
                        i0 -= v37;
                        do
                        {
                            iter1 = &iter1[1];
                            iter2 += 1;
                            j = i;
                            i = j - 1;
                            *((char *)iter2) = iter1[0];
                        } while (j != 1);
                    }
                    else if (v36 < v35)
                    {
                        iter1 = &iter1[v8 + v36 + -1 * v35];
                        k = i - v11;
                        if (k >= i0)
                            goto LABEL_1034fa0e;
                        i0 -= k;
                        do
                        {
                            iter1 = &iter1[1];
                            iter2 += 1;
                            *((char *)iter2) = iter1[0];
                            k -= 1;
                        } while (k != 1);
                        iter1 = v7 - 1;
                        v42 = v11;
                        if (v42 >= i0)
                            goto LABEL_1034fa0e;
                        i0 -= v42;
                        i = v42;
                        do
                        {
                            iter1 = &iter1[1];
                            iter2 += 1;
                            l = i;
                            i = l - 1;
                            *((char *)iter2) = iter1[0];
                        } while (l != 1);
                    }
                    else
                    {
                        iter1 = &iter1[v36 + -1 * v35];
                        if (i < i0)
                        {
                            i0 -= i;
                            do
                            {
                                iter1 = &iter1[1];
                                iter2 += 1;
                                m = i;
                                i = m - 1;
                                *((char *)iter2) = iter1[0];
                            } while (m != 1);
                        }
                        else
                        {
LABEL_1034fa0e:
LABEL_1034fa11:
                            if (i0 > 2)
                            {
                                v0 = 3;
                                n = (i0 - 3) / v0 + 1;
                                do
                                {
                                    i0 -= 3;
                                    v46 = &iter1[1];
                                    v47 = iter2 + 1;
                                    *((char *)v47) = v46[0];
                                    v48 = &v46[1];
                                    v49 = v47 + 1;
                                    iter1 = &v48[1];
                                    *((char *)v49) = v48[0];
                                    iter2 = v49 + 1;
                                    *((char *)iter2) = iter1[0];
                                    n -= 1;
                                } while (n != 1);
                                idx = a0;
                                goto LABEL_1034fa65;
                            }
                        }
                    }
                    iter1 = iter2 - v12;
                    goto LABEL_1034fa11;
                }
                if (((char)v23 & 64))
                {
                    if (((char)v23 & 32))
                    {
                        index->field_0 = 11;
                        v56 = node >> 3;
                        v57 = iter - v56;
                        node -= v56 * 8;
                        idx->field_0 = v57 + 1;
                        idx->field_c = iter2 + 1;
                        idx->field_4 = v6 - v57 + 5;
                        idx->field_10 = v5 - iter2 + 0x101;
                        index->field_38 = v15 & (1 << ((char)node & 31)) - 1;
                        index->field_3c = node;
                        return node;
                    }
                    *((char **)&idx->padding_14[4]) = "invalid literal/length code";
                    index->field_0 = 27;
                    v56 = node >> 3;
                    v57 = iter - v56;
                    node -= v56 * 8;
                    idx->field_0 = v57 + 1;
                    idx->field_c = iter2 + 1;
                    idx->field_4 = v6 - v57 + 5;
                    idx->field_10 = v5 - iter2 + 0x101;
                    index->field_38 = v15 & (1 << ((char)node & 31)) - 1;
                    index->field_3c = node;
                    return node;
                }
                iter1 = *((int *)(v10 + (((1 << ((char)v23 & 31)) - 1 & v15) + (iter1 >> 16)) * 4));
                v21 = iter1;
                v24 = (char)(*((int *)(v10 + (((1 << ((char)v23 & 31)) - 1 & v15) + (iter1 >> 16)) * 4)) >> 8);
                v15 >>= (char)v24 & 31;
                node -= v24;
                i = v24;
                i = (char)v21;
            } while (i);
            goto LABEL_1034fa7d;
        }
        iter2 += 1;
        *((char *)iter2) = v21 >> 16;
LABEL_1034fa7d:
        if (iter >= v6)
        {
            v56 = node >> 3;
            v57 = iter - v56;
            node -= v56 * 8;
            idx->field_0 = v57 + 1;
            idx->field_c = iter2 + 1;
            idx->field_4 = v6 - v57 + 5;
            idx->field_10 = v5 - iter2 + 0x101;
            index->field_38 = v15 & (1 << ((char)node & 31)) - 1;
            index->field_3c = node;
            return node;
        }
        else if (iter2 >= v5)
        {
            v56 = node >> 3;
            v57 = iter - v56;
            node -= v56 * 8;
            idx->field_0 = v57 + 1;
            idx->field_c = iter2 + 1;
            idx->field_4 = v6 - v57 + 5;
            idx->field_10 = v5 - iter2 + 0x101;
            index->field_38 = v15 & (1 << ((char)node & 31)) - 1;
            index->field_3c = node;
            return node;
        }
    }
}
```

## `sub_1034fb0b` `0x1034fb0b`

_979 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern unsigned int g_1038e180;
extern unsigned short g_10394126;
extern unsigned short g_10394166;
extern unsigned short g_103943a8;
extern unsigned short g_103943e8;

int sub_1034fb0b(unsigned int a0, unsigned int a1, unsigned int a2, struct_0 **a3, unsigned int *a4, unsigned short *a5)
{
    unsigned int v23;  // ebx
    unsigned int v24;  // esi
    unsigned int v31;  // ecx
    int v32;  // edi
    unsigned int v33;  // edx
    unsigned int v34;  // edi
    unsigned int v35;  // ecx
    unsigned int v36;  // edi
    char v37[2];  // ecx
    unsigned int v38;  // eax
    unsigned int *iter;  // edi
    unsigned int v40;  // edx
    unsigned int *v25;  // edi
    unsigned int n;  // ebx
    int v42;  // ecx
    unsigned int v43;  // ecx
    unsigned int v44;  // edx
    unsigned int *node;  // ecx
    unsigned int m;  // edx
    unsigned short *v47;  // ecx
    unsigned int v48;  // edx
    unsigned int v49;  // ecx
    unsigned int v50;  // eax
    unsigned int *iter1;  // edi
    unsigned int v51;  // edx
    char v52[2];  // eax
    int v53;  // edx
    unsigned int v54;  // edx
    unsigned int v55;  // edx
    unsigned int i0;  // edx
    unsigned int j;  // ecx
    char v28[2];  // eax
    unsigned int iter2;  // eax
    int v30;  // edi
    unsigned int k;  // [bp-0xa0]
    unsigned int *v1;  // [bp-0x9c]
    unsigned int v2;  // [bp-0x98]
    unsigned int v3;  // [bp-0x94]
    unsigned int v4;  // [bp-0x88]
    unsigned int v5;  // [bp-0x84]
    unsigned short *v6;  // [bp-0x80]
    unsigned short *v7;  // [bp-0x7c]
    unsigned int v8;  // [bp-0x78]
    int v9;  // [bp-0x74]
    unsigned int v10;  // [bp-0x70]
    char v11[2];  // [bp-0x6c], Other Possible Types: unsigned int
    unsigned int v12;  // [bp-0x68]
    int <0x1034fb0b[is_1]|Stack bp-0x64, 1 B>;  // [bp-0x64]
    unsigned int v13;  // [bp-0x64]
    unsigned short *v14;  // [bp-0x60]
    unsigned int v15;  // [bp-0x5c]
    unsigned int v16;  // [bp-0x58]
    unsigned int v17;  // [bp-0x54]
    unsigned short *l;  // [bp-0x50], Other Possible Types: unsigned int
    unsigned int v19;  // [bp-0x4c]
    unsigned long long v20;  // [bp-0x48]
    char v21;  // [bp-0x28]
    unsigned int v22;  // [bp-0x8]

    v22 = g_1038e180 ^ &<0x1034fb0b[is_1]|Stack bp-0x64, 1 B>;
    v3 = v23;
    v2 = v24;
    v1 = v25;
    k = 8;
    l = a5;
    for (iter1 = &v21; k; iter1 += 1)
    {
        k -= 1;
        *(iter1) = 0;
    }
    j = 0;
    if (a2 > 0)
    {
        do
        {
            v28 = &(&v21)[2 * *((short *)(a1 + j * 2))];
            *(v28) = *(v28) + 1;
            j += 1;
        } while (j < a2);
    }
    k = 15;
    iter2 = k;
    v15 = *(a4);
    v10 = iter2;
    do
    {
    } while (!*((short *)&(&v21)[2 * iter2]) && (iter2 -= 1, v10 = iter2, iter2 >= 1));
    if (*(a4) > iter2)
        v15 = iter2;
    if (!iter2)
    {
        *((char *)&v19) = 64;
        *((char *)&v19 + 1) = 1;
        *((unsigned short *)((char *)&v19 + 2)) = 0;
        *(a3)->field_0 = v19;
        *(a3) = *(a3) + 1;
        *(a3)->field_0 = v19;
        *(a3) = *(a3) + 1;
        *(a4) = 1;
    }
    else
    {
        v30 = 1;
        v31 = 1;
        v16 = 1;
        do
        {
        } while (!*((short *)&(&v21)[2 * v31]) && (v31 += 1, v16 = v31, v31 <= 15));
        if (v15 < v31)
            v15 = v31;
        v32 = 1;
        do
        {
            v33 = *((short *)&(&v21)[2 * v30]);
            v34 = v32 * 2;
            v32 = v34 - v33;
            if (v34 - v33 < 0)
                return sub_10351225();
        } while ((v30 = (int)(v30 + 1), v30 <= 15));
        if (v32 > 0)
        {
            if (!a0)
            {
                return sub_10351225();
            }
            else if (iter2 != 1)
            {
                return sub_10351225();
            }
        }
        k = 2;
        *((unsigned short *)((char *)&v20 + 2)) = 0;
        do
        {
            v35 = k + 1;
            *((short *)(-1 + (char *)&v20 + v35)) = *((short *)((char *)&v20 + k)) + *((short *)&(&v21)[k]);
            k = v35 + 1;
        } while (k < 30);
        v36 = 0;
        if (a2 > 0)
        {
            do
            {
                if (*((short *)(a1 + v36 * 2)))
                {
                    l[*((short *)((char *)&v20 + 2 * *((short *)(a1 + v36 * 2))))] = v36;
                    v37 = (char *)&v20 + 2 * *((short *)(a1 + v36 * 2));
                    *(v37) = *(v37) + 1;
                }
            } while ((v36 += 1, v36 < a2));
        }
        if (!a0)
        {
            v7 = l;
            v6 = v7;
            v9 = 19;
        }
        else if (a0 != 1)
        {
            v9 = -1;
            v6 = &g_103943a8;
            v7 = &g_103943e8;
        }
        else
        {
            v6 = &g_10394126;
            v7 = &g_10394166;
            v9 = 0x100;
        }
        v38 = v16;
        v8 = 4294967295;
        iter = &*(a3)->field_0;
        v17 = 0;
        v40 = 1 << ((char)v15 & 31);
        n = 0;
        v12 = 0;
        v5 = v38;
        v11 = v40;
        v13 = v40;
        v4 = v40 - 1;
        if (a0 == 1 && v40 >= 1456)
            return sub_10351225();
        v14 = l;
        while (true)
        {
            *((char *)&v19 + 1) = (char)v38 - (char)v17;
            v42 = *(v14);
            if (v42 < v9)
            {
                *((char *)&v19) = 0;
                *((unsigned short *)((char *)&v19 + 2)) = *(v14);
            }
            else if (v42 > v9)
            {
                v43 = *(v14) * 2;
                *((char *)&v19) = *(v43 + (char *)v7);
                *((short *)((char *)&v19 + 2)) = *((short *)(v43 + (char *)v6));
            }
            else
            {
                *((unsigned short *)((char *)&v19 + 2)) = 0;
                *((char *)&v19) = 96;
            }
            v44 = 1 << ((char)(v38 - v17) & 31);
            l = v11;
            v16 = l;
            node = &iter[l + (n >> ((char)v17 & 31))];
            do
            {
                l -= v44;
                node = &node[-1 * v44];
                *(node) = v19;
            } while (l);
            for (m = 1 << ((char)(v38 - 1) & 31); (m & v12); m >>= 1);
            n = (!m ? 0 : (m - 1 & v12) + m);
            v14 += 1;
            v47 = &(&v21)[2 * v38];
            *(v47) = *(v47) - 1;
            v12 = n;
            if (!*(v47))
            {
                if (v38 != v10)
                {
                    v38 = *((short *)(a1 + *(v14) * 2));
                    v5 = v38;
                }
                else
                {
                    *((unsigned short *)((char *)&v19 + 2)) = 0;
                    *((char *)&v19) = 64;
                    for (*((char *)&v19 + 1) = (char)v38 - (char)v17; n; n = (!i0 ? 0 : (i0 - 1 & n) + i0))
                    {
                        if (v17 && (v4 & n) != v8)
                        {
                            v38 = v15;
                            v17 = 0;
                            iter = &*(a3)->field_0;
                            *((char *)&v19 + 1) = v38;
                        }
                        iter[n >> ((char)v17 & 31)] = v19;
                        for (i0 = 1 << ((char)(v38 - 1) & 31); (i0 & n); i0 >>= 1);
                    }
                    *(a3) = &(*(a3))[v13];
                    *(a4) = v15;
                    break;
                }
            }
            v48 = v15;
            if (v38 > v48 && (l = v4 & n, l != v8))
            {
                if (!v17)
                    v17 = v48;
                iter = &iter[v16];
                v49 = v38 - v17;
                v50 = v17 + v49;
                v51 = 1 << ((char)v49 & 31);
                if (v50 < v10)
                {
                    v16 = v50;
                    v52 = &(&v21)[2 * v16];
                    while (true)
                    {
                        v53 = v51 - (unsigned int)*(v52);
                        if (v53 <= 0 || !((v49 += 1, v16 += 1, v11 = v52 + 2, v51 = v53 * 2, v16 < v10)))
                            break;
                        v52 = v11;
                    }
                }
                v54 = 1 << ((char)v49 & 31);
                v13 += v54;
                v11 = v54;
                if (a0 == 1 && v13 >= 1456)
                    return sub_10351225();
                n = v12;
                v8 = l;
                v55 = l * 4;
                *(v55 + (char *)*(a3)) = v49;
                *(1 + v55 + (char *)*(a3)) = v15;
                *((unsigned short *)(2 + v55 + (char *)*(a3))) = iter - *(a3) >> 2;
                v38 = v5;
            }
        }
    }
    return sub_10351225();
}
```

## `sub_1034fede` `0x1034fede`

_6 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038b358;

void sub_1034fede(void)
{
    goto g_1038b358;
}
```

## `sub_1034fee4` `0x1034fee4`

_6 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038b318;

void sub_1034fee4(void)
{
    goto g_1038b318;
}
```

## `sub_1034feea` `0x1034feea`

_6 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038b314;

void sub_1034feea(void)
{
    goto g_1038b314;
}
```

## `sub_1034fef0` `0x1034fef0`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1034fef0(void)
{
    sub_10350a53();
    return;
}
```

## `sub_1034fef5` `0x1034fef5`

_24 bytes. (leaf/helper — see body)_

```c
int * sub_1034fef5(int *a0)
{
    int v2;  // eax
    int v0;  // [bp-0x4]

    v2 = sub_10350a53(24, v0);
    *(a0) = v2;
    sub_10350978(v2);
    return a0;
}
```

## `sub_1034ff0d` `0x1034ff0d`

_21 bytes. (leaf/helper — see body)_

```c
void sub_1034ff0d(int *a0)
{
    int v0;  // [bp-0x4]

    sub_10350983(*(a0), v0);
    sub_10350abd(*(a0));
    return;
}
```

## `sub_1034ff22` `0x1034ff22`

_9 bytes. (leaf/helper — see body)_

```c
void sub_1034ff22(int *a0)
{
    sub_1035098e(*(a0));
    return;
}
```

## `sub_1034ff2b` `0x1034ff2b`

_9 bytes. (leaf/helper — see body)_

```c
void sub_1034ff2b(int *a0)
{
    sub_10350999(*(a0));
    return;
}
```

## `sub_1034ff34` `0x1034ff34`

_70 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
} struct_0;

struct_0 ** sub_1034ff34(struct_0 *idx)
{
    struct_0 **v0;  // eax
    struct_0 **v1;  // eax
    struct_0 **v2;  // edi
    struct_0 **v3;  // eax
    struct_0 **v4;  // eax

    sub_103475c0(idx, 0);
    v0 = idx[7].field_0;
    if (idx[7].field_0)
    {
        do
        {
            v1 = v0;
            v2 = *(v1);
            sub_10350abd(v1);
            v0 = v2;
        } while (*(v1));
    }
    v3 = idx[8].field_0;
    idx[7].field_0 = NULL;
    if (v3)
    {
        do
        {
            v4 = v3;
            sub_10350abd(v4);
            v3 = *(v4);
        } while (*(v4));
    }
    idx[8].field_0 = NULL;
    return v3;
}
```

## `sub_1034ff7a` `0x1034ff7a`

_80 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a2db4[4];
extern char g_103a2ddc;

int sub_1034ff7a(unsigned int *idx)
{
    int v1;  // ecx
    char v0;  // [bp+0x0]

    sub_10350060(2, v1, &v0);
    idx[1] = 1;
    do
    { } while (g_103a2db4[idx[1]] && g_103a2db4[idx[1]] != idx && (idx[1] = idx[1] + 1, idx[1] < 8));
    g_103a2db4[idx[1]] = idx;
    (&g_103a2ddc)[idx[1]] = (&g_103a2ddc)[idx[1]] + 1;
    return sub_10350081();
}
```

## `sub_1034ffca` `0x1034ffca`

_62 bytes. (leaf/helper — see body)_

```c
extern char g_103a2ddc;

void* ** sub_1034ffca(void* *idx)
{
    void* **v0;  // eax
    unsigned int v1;  // esi

    if (idx[1] > NULL)
    {
        *((char *)(idx[1] + &g_103a2ddc)) = *((char *)(idx[1] + &g_103a2ddc)) - 1;
        if (*((char *)(idx[1] + &g_103a2ddc)) > 0)
            return idx[1];
    }
    v0 = sub_1034ff34(idx);
    v1 = idx[9];
    if (!v1)
        return v0;
    sub_103130c0(v1);
    return sub_10350abd(v1);
}
```

