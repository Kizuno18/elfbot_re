# elfbot.dll decompiled — jiru 0x103544e0..0x10356f88

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_103544e0` `0x103544e0`

_170 bytes. (leaf/helper — see body)_

```c
unsigned int sub_103544e0(unsigned int a0, unsigned int a1, unsigned long long a2, unsigned int a3)
{
    unsigned int v0;  // edi
    unsigned int i;  // eax
    unsigned int v10;  // edx
    unsigned int v11;  // 4169
    unsigned long v12;  // 4170
    unsigned int v13;  // eax
    unsigned int v14;  // ecx
    unsigned int v15;  // edx
    unsigned int v16;  // edx
    unsigned int iter;  // eax
    unsigned int v3;  // eax
    unsigned int v4;  // edx
    unsigned long long v5;  // ecx
    unsigned int v7;  // 4166
    unsigned long v8;  // 4167
    unsigned int v9;  // ecx

    v0 = 0;
    if (a1 < 0)
    {
        v0 = 1;
        a1 = -(a1) - (0 < a0);
        a0 = -(a0);
    }
    i = a3;
    if (a3 < 0)
    {
        v0 += 1;
        i = -(i) - (0 < a2);
        a3 = i;
        a2 = -(a2);
    }
    if (!i)
    {
        iter = (a1 % a2 CONCAT a0) / a2;
    }
    else
    {
        v3 = a0;
        v4 = a1;
        v5 = a2;
        do
        {
            v7 = _ccall(27, i >> 1, i, 0);
            v8 = _ccall(v5, 1, v7, 4);
            v11 = _ccall(27, v4 >> 1, v4, 0);
            v12 = _ccall(v3, 1, v11, 4);
            i >>= 1;
            v3 = v12;
            v4 >>= 1;
            v5 = v8;
        } while (i);
        iter = (v10 CONCAT v13) / v9;
        v14 = iter * a3;
        v15 = a2 * iter >> 32;
        v16 = v15 + v14;
        if (v15 + v14 < 0)
        {
            iter -= 1;
        }
        else if (v16 > a1)
        {
            iter -= 1;
        }
        else if (v16 >= a1 && (unsigned int)(a2 * iter) > a0)
        {
            iter -= 1;
        }
    }
    if (v0 == 1)
        iter = -(iter);
    return iter;
}
```

## `sub_1035458a` `0x1035458a`

_572 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    int field_4;
} struct_0;

extern unsigned int g_1038efb0;
extern unsigned int g_1038efe4;

unsigned int sub_1035458a(void* idx, struct_0 *a1)
{
    int v9;  // edi
    int v10;  // esi
    unsigned int v19;  // eax
    unsigned int v20;  // edi
    unsigned int v21;  // ecx
    unsigned int v22;  // 4101
    unsigned int v23;  // eax
    unsigned int v24;  // 4101
    unsigned int v25;  // eax
    int v26;  // eax
    unsigned int v27;  // edi
    unsigned int *v28;  // edx
    unsigned int v11;  // ebx
    unsigned int i;  // eax
    unsigned int v30;  // ecx
    unsigned int index;  // ecx
    unsigned int v32;  // eax
    int v33;  // eax
    unsigned int v34;  // edi
    unsigned int v35;  // eax
    unsigned int v12;  // ecx
    int v13;  // eax
    int v14;  // eax
    unsigned int v15;  // edx
    int v16;  // eax
    unsigned int v17;  // edi
    unsigned int v18;  // edi
    unsigned int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x2c]
    unsigned int v2;  // [bp-0x28]
    unsigned int v3;  // [bp-0x24]
    unsigned int v4;  // [bp-0x20]
    unsigned int v5;  // [bp-0x14]
    int iter;  // [bp-0x10], Other Possible Types: unsigned int
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]

    v8 = 0;
    if (idx)
    {
        sub_10350ad0(idx, 255, 36);
        if (a1)
        {
            v5 = a1->field_0;
            iter = a1->field_4;
            if (iter <= NULL && (iter < NULL || v5 < NULL))
            {
                v4 = 22;
                *((unsigned int *)sub_103575e0()) = 22;
                return 22;
            }
            if (iter < 7 || iter <= 7 && v5 <= 2470473727)
            {
                v12 = sub_103544e0(v5, iter, 31536000, 0, v11) + 70;
                v2 = 100;
                v7 = v12 - 1;
                idx = v12;
                v13 = (int)((v12 + 299) / 400) - v7 / 100 + (v7 + (v7 >> 31 & 3) >> 2) - 0x11;
                v14 = sub_103544a0(v12 - 70, v12 - 70 >> 31, 4294966931, 4294967295);
                v16 = sub_103544a0(v14 - v13, v15 - (v13 >> 31) - (v14 < v13), 86400, 0);
                v17 = v5;
                v18 = v17 + v16;
                iter = iter + v15 + (v17 + v16 < v17);
                if (iter <= NULL && (iter < NULL || v18 < NULL))
                {
                    v19 = v7;
                    v20 = v18 + 31536000;
                    iter += v18 + 31536000 < v18;
                    v21 = v19;
                    idx = v19;
                    if ((v21 & 2147483651) < NULL)
                    {
                        v22 = _ccall(4, 18, ((v21 & 2147483651) - 1 | 0xfffffffc) + 1, 0, 0);
                        v23 = v19;
                        if ((char)v22)
                            goto LABEL_103546a8;
                    }
                    else
                    {
                        v23 = v19;
                        if (!(v21 & 2147483651))
                        {
LABEL_103546a8:
                            v2 = 100;
                            if (v19 % 100)
                                goto LABEL_103546c6;
                            v23 = idx;
                        }
                    }
                    v18 = v20;
                    if ((int)((v23 + 1900) % 400))
                        goto LABEL_10354707;
LABEL_103546c6:
                    v18 = v20 + 86400;
                    iter += v20 + 86400 < v20;
                    goto LABEL_10354700;
                }
                else
                {
                    if ((idx & 2147483651) < NULL)
                        v24 = _ccall(4, 18, ((idx & 2147483651) - 1 | 0xfffffffc) + 1, 0, 0);
                    if (!(idx & 2147483651) && !((v2 = 100, !idx % 100)) || (v18 = v18, !(int)((long long)(int)(idx + 1900) % 400)))
                    {
LABEL_10354700:
                        v8 = 1;
                    }
                }
LABEL_10354707:
                *((unsigned int *)&idx[20]) = idx;
                v25 = sub_103544e0(v18, iter, 86400, 0, 0);
                *((unsigned int *)&idx[28]) = v25;
                v26 = sub_103544a0(v25, v25 >> 31, 4294880896, 4294967295);
                v27 = v18 + v26;
                iter = iter + v15 + (v18 + v26 < v18);
                v28 = &g_1038efb0;
                if (!v8)
                    v28 = &g_1038efe4;
                i = (int)idx[28];
                v30 = 1;
                if (v28[1] < i)
                {
                    do
                    {
                        v30 += 1;
                    } while (v28[v30] < i);
                }
                index = v30 - 1;
                *((unsigned int *)&idx[16]) = index;
                *((unsigned int *)&idx[12]) = i - v28[index];
                v0 = 7;
                *((unsigned int *)&idx[24]) = (sub_103544e0(a1->field_0, a1->field_4, 86400, 0, 0) + 4) % 7;
                v32 = sub_103544e0(v27, iter, 3600, 0, 0);
                *((unsigned int *)&idx[8]) = v32;
                v33 = sub_103544a0(v32, v32 >> 31, 4294963696, 4294967295);
                v34 = v27 + v33;
                iter = iter + v15 + (v27 + v33 < v27);
                v35 = sub_103544e0(v34, iter, 60, 0, 0);
                *((unsigned int *)&idx[4]) = v35;
                *((unsigned int *)&idx[32]) = 0;
                *((unsigned int *)idx) = v34 - v35 * 60;
                return 0;
            }
        }
    }
    v4 = 22;
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    *((unsigned int *)sub_103575e0(v9, v10)) = 22;
    sub_103535f2();
    return 22;
}
```

## `sub_103547c6` `0x103547c6`

_36 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    int field_4;
} struct_0;

int sub_103547c6(struct_0 *a0)
{
    unsigned int v1;  // esi
    int v0;  // [bp-0x4]

    v1 = sub_1035d478(v0);
    if (v1)
        return ~(-(0 < sub_1035458a(v1, a0))) & v1;
    return v1;
}
```

## `sub_103547f0` `0x103547f0`

_117 bytes. (leaf/helper — see body)_

```c
int sub_103547f0(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v0;  // ebx
    unsigned int v1;  // eax
    unsigned long v10;  // 4170
    unsigned int v11;  // eax
    unsigned long long v12;  // eax
    unsigned int v13;  // ecx
    unsigned int v14;  // edx
    unsigned int v15;  // eax
    unsigned int i;  // ecx
    unsigned int v3;  // edx
    unsigned int v5;  // 4166
    unsigned long v6;  // 4167
    unsigned int v7;  // ebx
    unsigned int v8;  // edx
    unsigned int v9;  // 4169

    if (!a3)
        return (a1 % a2 CONCAT a0) % a2;
    v0 = a2;
    v1 = a0;
    i = a3;
    v3 = a1;
    do
    {
        v5 = _ccall(27, i >> 1, i, 0);
        v6 = _ccall(v0, 1, v5, 4);
        v9 = _ccall(27, v3 >> 1, v3, 0);
        v10 = _ccall(v1, 1, v9, 4);
        v0 = v6;
        v1 = v10;
        i >>= 1;
        v3 >>= 1;
    } while (i);
    v12 = (unsigned int)((v8 CONCAT v11) / v7);
    v13 = v12 * a3;
    v14 = v12 * a2 >> 32;
    v15 = v12 * a2;
    if (v14 + v13 < 0 || v14 + v13 > a1 || v14 + v13 >= a1 && v15 > a0)
        v15 -= a2;
    return -(v15 - a0);
}
```

## `sub_10354870` `0x10354870`

_104 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10354870(unsigned int a0, unsigned int a1, unsigned long long a2, unsigned int a3)
{
    unsigned long long v0;  // ebx
    unsigned int v1;  // eax
    unsigned long v10;  // 4170
    unsigned int v11;  // eax
    unsigned int iter;  // esi
    unsigned int v13;  // ecx
    unsigned int v14;  // edx
    unsigned int v15;  // edx
    unsigned int i;  // ecx
    unsigned int v3;  // edx
    unsigned int v5;  // 4166
    unsigned long v6;  // 4167
    unsigned int v7;  // ebx
    unsigned int v8;  // edx
    unsigned int v9;  // 4169

    if (!a3)
        return (a1 % a2 CONCAT a0) / a2;
    v0 = a2;
    v1 = a0;
    i = a3;
    v3 = a1;
    do
    {
        v5 = _ccall(27, i >> 1, i, 0);
        v6 = _ccall(v0, 1, v5, 4);
        v9 = _ccall(27, v3 >> 1, v3, 0);
        v10 = _ccall(v1, 1, v9, 4);
        v0 = v6;
        v1 = v10;
        i >>= 1;
        v3 >>= 1;
    } while (i);
    iter = (v8 CONCAT v11) / v7;
    v13 = iter * a3;
    v14 = a2 * iter >> 32;
    v15 = v14 + v13;
    if (v14 + v13 < 0)
    {
        iter -= 1;
    }
    else if (v15 > a1)
    {
        iter -= 1;
    }
    else if (v15 >= a1 && (unsigned int)(a2 * iter) > a0)
    {
        iter -= 1;
    }
    return iter;
}
```

## `sub_103548d8` `0x103548d8`

_27 bytes. (leaf/helper — see body)_

```c
void* sub_103548d8(void* a0)
{
    void* v1;  // eax
    void* v0;  // [bp-0x4]

    if (!a0)
        return a0;
    v1 = a0 - 8;
    if (*((int *)v1) != 0xdddd)
        return v0;
    v0 = v1;
    return (unsigned int)sub_1035345e();
}
```

## `sub_103548f3` `0x103548f3`

_32 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
} struct_0;

int sub_103548f3(void)
{
    char *v2;  // edx
    char *v3;  // esi
    unsigned int *v4;  // eax
    unsigned int v5;  // edi
    struct_0 **v6;  // ecx
    unsigned int v0;  // [bp-0x8]

    v3 = v2;
    if (!*(v4))
        return;
    v0 = v5;
    do
    {
    } while (*(v3) && (*(v6)->field_0 = *(v3), *(v6) = *(v6) + 1, v3 += 1, *(v4) = *(v4) - 1, *(v4)));
    return;
}
```

## `sub_10354913` `0x10354913`

_121 bytes. (leaf/helper — see body)_

```c
int sub_10354913(void)
{
    unsigned int *v3;  // ecx
    void* *v4;  // edi
    unsigned int j;  // esi
    unsigned int v13;  // eax
    unsigned int *v14;  // edi
    void* node;  // esi
    unsigned int v15;  // eax
    unsigned int v6;  // eax
    unsigned int v7;  // eax
    void* iter;  // eax
    void* iter1;  // esi
    char v10;  // 4106
    unsigned int v11;  // edx
    unsigned int v0;  // [bp-0x14]
    unsigned int *iter2;  // [bp-0x8], Other Possible Types: unsigned int
    unsigned int v2;  // [bp+0x4]

    iter2 = v3;
    iter2 = 0;
    if (v2)
    {
        node = *(v4);
        if (*(v3) > 1)
        {
            do
            {
                v0 = 10;
                v7 = v6 / v0;
                *((char *)node) = (char)(v6 % v0) + 48;
                node += 1;
                *(v3) = *(v3) - 1;
            } while (v7 > 0 && (v15 = v7, *(v3) > 1));
        }
        iter = *(v4);
        *(v4) = node;
        iter1 = node - 1;
        do
        {
            v10 = *((char *)iter1);
            *((char *)iter1) = *((char *)iter);
            iter1 -= 1;
            *((char *)iter) = v10;
            iter += 1;
        } while (iter < iter1);
        return;
    }
    else if (v11 < *(v3))
    {
        j = v11 - 1;
        if (j != 4294967295)
        {
            do
            {
                v0 = 10;
                v13 = v6 / v0;
                iter2 += 1;
                *((char *)(j + *(v14))) = (char)(v6 % v0) + 48;
                j -= 1;
                v6 = v13;
            } while (j != 4294967295);
        }
        *(v14) = *(v14) + iter2;
        *(v3) = *(v3) - iter2;
        return;
    }
    else
    {
        *(v3) = 0;
        return;
    }
}
```

## `sub_1035498c` `0x1035498c`

_998 bytes. (leaf/helper — see body)_

```c
typedef struct struct_7 {
    char field_0;
} struct_7;

typedef struct struct_11 {
    char padding_0[32];
    unsigned int field_20;
} struct_11;

int sub_1035498c(void)
{
    struct_7 **v10;  // ecx
    char v11;  // al
    struct_11 *idx;  // edx
    unsigned int v18;  // eax
    unsigned int v19;  // eax
    unsigned int v20;  // ecx
    unsigned int v21;  // eax
    unsigned int v22;  // eax
    unsigned int v23;  // eax
    unsigned int v24;  // ecx
    unsigned int v12;  // eax
    unsigned int v25;  // eax
    unsigned int v26;  // eax
    int v27;  // eax
    unsigned int v28;  // eax
    unsigned int v29;  // eax
    unsigned int v13;  // eax
    unsigned int v30;  // eax
    unsigned int v31;  // eax
    unsigned int *v32;  // eax
    unsigned int v14;  // eax
    unsigned int v33;  // eax
    unsigned int v34;  // eax
    unsigned int v35;  // eax
    unsigned int v15;  // eax
    int v36;  // esi
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    struct_7 **v2;  // [bp-0x20], Other Possible Types: unsigned int
    unsigned int *v3;  // [bp-0x1c], Other Possible Types: unsigned int
    unsigned int v4;  // [bp-0x18]
    struct_7 **v5;  // [bp-0x8], Other Possible Types: unsigned int
    int v6;  // [bp+0x4]
    unsigned int *v7;  // [bp+0x8]
    unsigned int v8;  // [bp+0xc]
    unsigned int v9;  // [bp+0x10]

    v5 = v10;
    v12 = v11;
    if (v12 <= 89)
    {
        if (v12 == 89)
        {
            if (*((int *)&idx->padding_0[20]) < -1900)
            {
                v4 = 0;
                v3 = 0;
                v2 = 0;
                v1 = 0;
                v0 = 0;
                *((unsigned int *)sub_103575e0()) = 22;
                sub_103535f2();
                return;
            }
            if (*((int *)&idx->padding_0[20]) <= 8099)
            {
                v4 = 100;
                v4 = v9;
                v3 = 4;
                sub_10354913();
                return;
            }
            goto LABEL_10354b3f;
        }
        if (v12 <= 73)
        {
            if (v12 != 73)
            {
                v13 = v12 - 4;
                if (v12 == 4)
                    return;
                v14 = v13 - 9;
                if (v13 == 9)
                    return;
                v15 = v14 - 24;
                if (v14 == 24)
                {
                    *(v10)->field_0 = 37;
                    *(v10) = *(v10) + 1;
                    *(v7) = *(v7) - 1;
                    return;
                }
                v16 = v15 - 28;
                if (v15 != 28)
                {
                    if (v16 != 1)
                    {
                        if (v16 != 7)
                            return;
                        if (*((int *)&idx->padding_0[8]) >= 0 && *((int *)&idx->padding_0[8]) <= 23)
                            goto LABEL_10354c9a;
                    }
                    else
                    {
                        if (*((int *)&idx->padding_0[16]) >= 0 && *((int *)&idx->padding_0[16]) <= 11)
                        {
                            sub_103548f3();
                            return;
                        }
                    }
                }
                else
                {
                    if (*((int *)&idx->padding_0[24]) >= 0 && *((int *)&idx->padding_0[24]) <= 6)
                    {
                        sub_103548f3();
                        return;
                    }
                }
            }
            else
            {
                v18 = *((int *)&idx->padding_0[8]);
                if (v18 >= 0 && v18 <= 23)
                {
                    v4 = 12;
                    if (!v18 % v4)
                        goto LABEL_10354c9a;
                }
            }
        }
        else
        {
            v19 = v12 - 77;
            if (v12 != 77)
            {
                v4 = 6;
                v20 = v4;
                if (v19 == v20)
                {
                    v27 = *((int *)&idx->padding_0[0]);
                    goto LABEL_10354b17;
                }
                v21 = v19 - v20 - 1;
                if (v21 != 1)
                {
                    v22 = v21 - 2;
                    if (v22 != 1)
                    {
                        if (v22 == 2)
                        {
                            v4 = v8;
                            v3 = v7;
                            goto LABEL_10354c1e;
                        }
                    }
                    else
                    {
                        v23 = *((int *)&idx->padding_0[24]);
                        if (v23 >= 0 && v23 <= v20)
                        {
                            v24 = v20;
                            if (v23)
                                v24 = v23 - 1;
                        }
                    }
                }
                else
                {
                    v25 = *((int *)&idx->padding_0[24]);
                    if (v25 >= 0 && v25 <= v20 && (v24 = v25, v26 = (unsigned int)*((int *)&idx->padding_0[28]), v26 >= 0 && v26 <= 365))
                    {
                        if (v26 < v24)
                        {
                            goto LABEL_10354c9a;
                        }
                        else
                        {
                            v4 = 7;
                            if (v26 % v4 >= v24)
                                goto LABEL_10354c9a;
                        }
                    }
                }
            }
            else
            {
                v27 = *((int *)&idx->padding_0[4]);
LABEL_10354b17:
                if (v27 >= 0 && v27 <= 59)
                    goto LABEL_10354c9a;
            }
        }
    }
    else if (v12 > 109)
    {
        v33 = v12 - 112;
        if (v12 != 112)
        {
            v34 = v33 - 7;
            if (v33 != 7)
            {
                v35 = v34 - 1;
                if (v34 == 1)
                {
                    v4 = v8;
                    v3 = v7;
                    v2 = v10;
                    v1 = idx;
                    if (v9)
                        v0 = 1;
                    else
                        v0 = 0;
LABEL_10354c22:
                    if (sub_10354d72(v6))
                        return;
                    return;
                }
                if (v35 != 1)
                {
                    if (v35 == 2)
                    {
LABEL_10354cb9:
                        sub_1035dc60();
                        sub_1035d56e();
                        v5 = idx->field_20;
                        sub_103548f3();
                        return;
                    }
                    return;
                }
                else
                {
                    if (*((int *)&idx->padding_0[20]) >= 0)
                    {
                        v4 = v9;
                        v3 = 100;
                        v3 = 2;
                        sub_10354913();
                        return;
                    }
                }
            }
            else
            {
                if (*((int *)&idx->padding_0[24]) >= 0 && *((int *)&idx->padding_0[24]) <= 6)
                {
                    v4 = v9;
                    sub_10354913();
                    return;
                }
            }
        }
        else
        {
            v36 = *((int *)&idx->padding_0[8]);
            if (v36 >= 0 && v36 <= 23)
            {
                if (v36 <= 11)
                {
                    sub_103548f3();
                    return;
                }
                sub_103548f3();
                return;
            }
        }
    }
    else if (v12 != 109)
    {
        v28 = v12 - 90;
        if (v12 == 90)
            goto LABEL_10354cb9;
        v29 = v28 - 7;
        if (v28 != 7)
        {
            v30 = v29 - 1;
            if (v29 != 1)
            {
                v31 = v30 - 1;
                if (v30 == 1)
                {
                    v4 = v8;
                    v3 = v7;
                    v2 = v10;
                    v1 = idx;
                    if (v9)
                        v0 = 1;
                    else
                        v0 = 0;
                    if (sub_10354d72(v6) && *(v7))
                    {
                        v4 = v8;
                        *(v10)->field_0 = 32;
                        *(v10) = *(v10) + 1;
                        *(v7) = *(v7) - 1;
                        v3 = v7;
LABEL_10354c1e:
                        v2 = v10;
                        v1 = idx;
                        v0 = 2;
                        goto LABEL_10354c22;
                    }
                }
                if (v31 != 1)
                {
                    if (v31 == 7)
                    {
                        if (*((int *)&idx->padding_0[28]) >= 0 && *((int *)&idx->padding_0[28]) <= 365)
                        {
                            v4 = v9;
                            v3 = 3;
                            sub_10354913();
                            return;
                        }
                    }
                    else
                    {
                        return;
                    }
                }
                else
                {
                    if (*((int *)&idx->padding_0[12]) < 1 || *((int *)&idx->padding_0[12]) > 31)
                    {
LABEL_10354b3f:
                        v4 = 0;
                        v3 = 0;
                        v2 = 0;
                        v1 = 0;
                        v0 = 0;
                        *((unsigned int *)sub_103575e0()) = 22;
                        sub_103535f2();
                        return;
                    }
                    goto LABEL_10354c9a;
                    goto LABEL_10354c9a;
                }
            }
            else
            {
                if (*((int *)&idx->padding_0[16]) >= 0 && *((int *)&idx->padding_0[16]) <= 11)
                {
                    sub_103548f3();
                    return;
                }
            }
        }
        else
        {
            if (*((int *)&idx->padding_0[24]) >= 0 && *((int *)&idx->padding_0[24]) <= 6)
            {
                sub_103548f3();
                return;
            }
        }
    }
    else if (*((int *)&idx->padding_0[16]) >= 0 && *((int *)&idx->padding_0[16]) <= 11)
    {
LABEL_10354c9a:
        v4 = v9;
        v3 = 2;
        sub_10354913();
        return;
    }
    v32 = sub_103575e0();
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    *(v32) = 22;
    sub_103535f2();
    return;
}
```

## `sub_10354d72` `0x10354d72`

_1117 bytes. refs "am/pm", "a/p"_

```c
typedef struct struct_0 {
    char padding_0[152];
    struct struct_1 *field_98;
    struct struct_1 *field_9c;
    struct struct_2 *field_a0;
    unsigned int field_a4;
    unsigned int field_a8;
    unsigned int field_ac;
    unsigned int field_b0;
} struct_0;

typedef struct struct_2 {
    char field_0;
} struct_2;

typedef struct struct_1 {
    char field_0;
    char field_1;
} struct_1;

typedef struct struct_4 {
    unsigned int field_0;
} struct_4;

extern struct_4 *g_1038b218;
extern struct_4 *g_1038b21c;
extern unsigned int g_1038e180;

int sub_10354d72(int a0, unsigned int a1, unsigned short *idx, struct_2 **a3, unsigned int *a4, struct_0 *a5)
{
    unsigned int v16;  // ebx
    unsigned int v17;  // esi
    struct_2 **v26;  // ecx
    char j;  // al
    unsigned int *v28;  // ebx
    struct_2 **v29;  // esi
    unsigned int v30;  // edx
    char *v31;  // ecx
    char *v32;  // ecx
    int v33;  // ecx
    unsigned int v35;  // eax
    unsigned int v18;  // edi
    unsigned int v36;  // eax
    unsigned int v37;  // eax
    unsigned int v38;  // eax
    char *v39;  // edi
    char v40;  // al
    char *v41;  // eax
    unsigned int v42;  // eax
    unsigned int v43;  // eax
    unsigned int v44;  // eax
    int v45;  // eax
    char *iter;  // edi
    unsigned int v46;  // eax
    unsigned int v47;  // eax
    unsigned int v48;  // eax
    unsigned int v49;  // eax
    char k[2];  // edi
    char v51[2];  // eax
    char v52[2];  // eax
    unsigned int v53;  // eax
    unsigned int v54;  // eax
    unsigned int v55;  // eax
    unsigned int *v20;  // ecx
    char *v56;  // eax
    int v21;  // eax
    void* node;  // eax
    void* iter1;  // ebx
    int i;  // eax
    unsigned int *v25;  // esi
    int v0;  // [bp-0x48]
    unsigned int v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x28]
    unsigned short v4;  // [bp-0x24]
    unsigned short v5;  // [bp-0x22]
    unsigned short v6;  // [bp-0x1e]
    unsigned short v7;  // [bp-0x1c]
    unsigned short v8;  // [bp-0x1a]
    unsigned short v9;  // [bp-0x18]
    unsigned short v10;  // [bp-0x16]
    int v11;  // [bp-0x14]
    unsigned int *v12;  // [bp-0x10], Other Possible Types: char *
    void* v13;  // [bp-0xc], Other Possible Types: int
    unsigned int v14;  // [bp-0x8]
    char v15;  // [bp-0x4]

    v14 = g_1038e180 ^ &v15;
    v3 = v16;
    v2 = v17;
    v1 = v18;
    iter = &(!a1 ? a5->field_a0 : (a1 == 1 ? a5->field_a4 : a5->field_a8))->field_0;
    if (a5->field_b0 != 1)
    {
        v20 = &g_1038b21c->field_0;
        if (a1 == 2)
            v20 = &g_1038b218->field_0;
        v4 = idx[10] + 1900;
        v5 = idx[8] + 1;
        v6 = idx[6];
        v7 = idx[4];
        v9 = *(idx);
        *((unsigned short **)&(&v0)[8]) = &v4;
        *((unsigned int *)&(&v0)[4]) = 0;
        *((unsigned int *)&v0) = a5->field_ac;
        v12 = v20;
        v8 = idx[2];
        v10 = 0;
        v11 = v20(*((unsigned int *)&v0), *((unsigned int *)(&v0 + 4)), *((unsigned int *)(&v0 + 8)), iter, 0, 0);
        if (v11)
        {
            v21 = v11 + 8;
            if (v21 <= 0x400)
            {
                sub_1035de90();
                node = &v0;
                if (!&v0)
                    goto LABEL_10354e55;
                *((unsigned int *)&v0) = 0xcccc;
                goto LABEL_10354e52;
            }
            else
            {
                node = sub_10355a15(v21);
                if (node)
                {
                    *((unsigned int *)node) = 0xdddd;
LABEL_10354e52:
                    node += 8;
                }
            }
LABEL_10354e55:
            v13 = node;
            if (node)
            {
                iter1 = node;
                i = v12(a5->field_ac, 0, &v4, iter, iter1, v11) - 1;
                if (i > 0)
                {
                    v25 = a4;
                    v26 = a3;
                    do
                    {
                        if (*(v25) <= 0)
                            break;
                        v11 = i;
                        *(v26)->field_0 = *((char *)iter1);
                        *(v26) = *(v26) + 1;
                        iter1 += 1;
                        *(v25) = *(v25) - 1;
                        i = v11 - 1;
                    } while (i > 0);
                }
                sub_103548d8(v13);
                return sub_10351225();
            }
        }
    }
    j = *(iter);
    if (!*(iter))
        return sub_10351225();
    v28 = a4;
    v29 = a3;
    do
    {
        if (!*(v28))
            break;
        v30 = 0;
        v13 = 0;
        v31 = iter;
        do
        {
            v30 += 1;
            v31 += 1;
        } while (*(v31) == j);
        v12 = v32;
        v33 = j;
        if (v33 <= 100)
        {
            if (v45 == 100)
            {
                v42 = v30;
                v43 = v42 - 1;
                if (v42 != 1)
                {
                    v44 = v43 - 1;
                    if (v43 != 1)
                    {
                        if (v44 == 1)
                        {
                            goto LABEL_103551a5;
                        }
                        else if (v44 == 2)
                        {
                            goto LABEL_103551a5;
                        }
                    }
                }
                else
                {
                    v13 = 1;
                }
                goto LABEL_103551a5;
            }
            if (v45 == 39)
            {
                iter = &iter[v30];
                if (!((char)v30 & 1))
                    continue;
                v40 = *(iter);
                if (!*(iter))
                    break;
                do
                {
                    if (!*(v28))
                        break;
                    if (v40 == 39)
                    {
                        iter += 1;
                        break;
                    }
                    if (sub_1035de48(v40, a0) && *(v28) > 1)
                    {
                        v41 = iter + 1;
                        if (!*(v41))
                            return sub_10351225();
                        *(v29)->field_0 = *(iter);
                        *(v29) = *(v29) + 1;
                        *(v28) = *(v28) - 1;
                        iter = v41;
                    }
                    *(v29)->field_0 = *(iter);
                    *(v29) = *(v29) + 1;
                    iter += 1;
                    *(v28) = *(v28) - 1;
                    v40 = *(iter);
                } while (*(iter));
            }
            if (v45 != 65)
            {
                if (v45 == 72)
                {
                    v38 = v30;
                    if (v38 == 1)
                    {
                        v13 = 1;
                    }
                    else if (!(v38 == 2))
                    {
                        goto LABEL_10354f0e;
                    }
                    goto LABEL_103551a5;
                }
                if (v45 == 77)
                {
                    v35 = v30;
                    v36 = v35 - 1;
                    if (v35 != 1)
                    {
                        v37 = v36 - 1;
                        if (v36 != 1)
                        {
                            if (v37 != 1)
                            {
                                if (v37 == 2)
                                    goto LABEL_103551a5;
                            }
                            else
                            {
                                goto LABEL_103551a5;
                            }
                        }
                    }
                    else
                    {
                        v13 = 1;
                    }
                    goto LABEL_103551a5;
                }
                else if (!(v45 == 97))
                {
                    goto LABEL_10354f0e;
                }
            }
            if (!sub_1035dcf0(iter, "am/pm"))
            {
                v39 = iter + 5;
            }
            else
            {
                if (sub_1035dcf0(iter, "a/p"))
                    goto LABEL_10354fc3;
                v39 = iter + 3;
            }
            v12 = v39;
LABEL_10354fc3:
            goto LABEL_103551a5;
        }
        else
        {
            v45 = v33;
            v46 = v45 - 104;
            if (v45 != 104)
            {
                v47 = v46 - 5;
                if (v46 != 5)
                {
                    v48 = v47 - 6;
                    if (v47 != 6)
                    {
                        if (v48 == 1)
                        {
                            if (v30 == 1 && *(v28) > 0)
                            {
                                if (sub_1035de48(k[0], a0) && *(v28) > 1)
                                {
                                    v51 = &k[1];
                                    if (!v51[0])
                                        return sub_10351225();
                                    *(v29)->field_0 = k[0];
                                    *(v29) = *(v29) + 1;
                                    *(v28) = *(v28) - 1;
                                    k = v51;
                                }
                                *(v29)->field_0 = k[0];
                                *(v29) = *(v29) + 1;
                                *(v28) = *(v28) - 1;
                                goto LABEL_103551c0;
                            }
                            else
                            {
                                for (k = (*((int *)&idx[4]) <= 11 ? a5->field_98 : a5->field_9c); k[0] && *(v28) > 0; *(v28) = *(v28) - 1)
                                {
                                    if (sub_1035de48(k[0], a0) && *(v28) > 1)
                                    {
                                        v52 = &k[1];
                                        if (!v52[0])
                                            return sub_10351225();
                                        *(v29)->field_0 = k[0];
                                        *(v29) = *(v29) + 1;
                                        *(v28) = *(v28) - 1;
                                        k = v52;
                                    }
                                    *(v29)->field_0 = k[0];
                                    *(v29) = *(v29) + 1;
                                    k = &k[1];
                                }
                            }
                        }
                        if (v48 == 6)
                        {
                            v49 = v30 - 1;
                            if (v49 == 1)
                            {
                                goto LABEL_103551a5;
                            }
                            else if (v49 == 3)
                            {
                                goto LABEL_103551a5;
                            }
                        }
                    }
                    else
                    {
                        v53 = v30;
                        if (v53 == 1)
                        {
                            v13 = 1;
                        }
                        else if (!(v53 == 2))
                        {
                            goto LABEL_10354f0e;
                        }
                        goto LABEL_103551a5;
                    }
                }
                else
                {
                    v54 = v30;
                    if (v54 == 1)
                    {
                        v13 = 1;
                    }
                    else if (!(v54 == 2))
                    {
                        goto LABEL_10354f0e;
                    }
                    goto LABEL_103551a5;
                }
            }
            else
            {
                v55 = v30;
                if (v55 != 1)
                {
                    if (v55 == 2)
                        goto LABEL_103551a3;
LABEL_10354f0e:
                    if (sub_1035de48(v45, a0) && *(v28) > 1)
                    {
                        v56 = iter + 1;
                        if (!*(v56))
                            return sub_10351225();
                        *(v29)->field_0 = *(iter);
                        *(v29) = *(v29) + 1;
                        *(v28) = *(v28) - 1;
                        iter = v56;
                    }
                    *(v29)->field_0 = *(iter);
                    *(v29) = *(v29) + 1;
                    iter += 1;
                    *(v28) = *(v28) - 1;
                }
                else
                {
                    v13 = 1;
LABEL_103551a3:
LABEL_103551a5:
                    if (!sub_1035498c(a0, v28, a5, v13))
                        return sub_10351225();
LABEL_103551c0:
                    iter = v12;
                }
            }
        }
    } while ((j = *(iter), *(iter)));
    return sub_10351225();
}
```

## `sub_103551cf` `0x103551cf`

_431 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

unsigned int sub_103551cf(char *iter, unsigned int a1, unsigned int a2, unsigned int a3, int a4, unsigned int *a5)
{
    int v13;  // edi
    unsigned int v14;  // eax
    unsigned int v15;  // esi
    unsigned int v16;  // eax
    unsigned int v17;  // esi
    int v18;  // eax
    int v19;  // esi
    unsigned int v0;  // [bp-0x44]
    unsigned int v1;  // [bp-0x40]
    unsigned int v2;  // [bp-0x3c]
    unsigned int v3;  // [bp-0x38]
    unsigned int v4;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    struct_0 v7;  // [bp-0x24]
    struct_0 *idx;  // [bp-0x1c]
    char v9;  // [bp-0x18]
    int v10;  // [bp-0x10]
    unsigned int v11;  // [bp-0xc]
    unsigned int node;  // [bp-0x8]

    v11 = 0;
    sub_103536a7(&v7, a5);
    if (!iter)
    {
        v6 = 0;
        v5 = 0;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        *((unsigned int *)sub_103575e0()) = 22;
        sub_103535f2();
        if (!v9)
            return 0;
        idx[8].field_8 = idx[8].field_8 & 4294967293;
        return 0;
    }
    else
    {
        if (!a1)
        {
            v5 = 0;
            v4 = 0;
            v3 = 0;
            v2 = 0;
            v1 = 0;
            *((unsigned int *)sub_103575e0(v13)) = 22;
            sub_103535f2();
            if (v9)
                idx[8].field_8 = idx[8].field_8 & 4294967293;
            v14 = 0;
        }
        else
        {
            v15 = a2;
            *(iter) = 0;
            if (v15)
            {
                if (!a4)
                    a4 = *((int *)(v7 + 212));
                v10 = a4;
                node = a1;
                if (a1 > NULL)
                {
                    while (true)
                    {
                        if (!*((char *)v15))
                        {
LABEL_103552fc:
                            if (node <= 0)
                                goto LABEL_1035531c;
                            *(iter) = 0;
                            v14 = a1 - node;
                            if (v9)
                            {
                                idx[8].field_8 = idx[8].field_8 & 4294967293;
                                goto LABEL_10355379;
                            }
                        }
                        if (*((char *)v15) != 37)
                        {
                            if (sub_1035de48(*((char *)v15), &v7) && node > 1)
                            {
                                v16 = v15 + 1;
                                if (*((char *)v16))
                                {
                                    *(iter) = *((char *)v15);
                                    iter += 1;
                                    node -= 1;
                                    v15 = v16;
                                }
                                else
                                {
                                    v11 = 1;
                                    goto LABEL_1035531c;
                                }
                            }
                            *(iter) = *((char *)v15);
                            iter += 1;
                            v15 += 1;
                            node -= 1;
                            goto LABEL_103552f7;
                        }
                        if (!a3)
                            break;
                        v17 = v15 + 1;
                        v18 = 0;
                        if (*((char *)v17) == 35)
                        {
                            v18 = 1;
                            v17 += 1;
                        }
                        if (sub_1035498c(&v7, &node, v10, v18))
                        {
                            v15 = v17 + 1;
LABEL_103552f7:
                            if (node <= 0)
                                goto LABEL_103552fc;
                        }
                        else if (node > NULL)
                        {
                            v11 = 1;
                            goto LABEL_1035531c;
                        }
                    }
                    *((unsigned int *)sub_103575e0()) = 22;
                }
                else
                {
LABEL_1035531c:
                    *(iter) = 0;
                    if (v11 || node > 0)
                        goto LABEL_10355353;
                    *((unsigned int *)sub_103575e0()) = 0x22;
                }
            }
            else
            {
LABEL_10355353:
                v4 = 0;
                v3 = 0;
                v2 = 0;
                v1 = 0;
                v0 = 0;
                *((unsigned int *)sub_103575e0(v19)) = 22;
                sub_103535f2();
            }
            if (v9)
                idx[8].field_8 = idx[8].field_8 & 4294967293;
            v14 = 0;
LABEL_10355379:
        }
        return v14;
    }
}
```

## `sub_1035537e` `0x1035537e`

_29 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1035537e(char *a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    return sub_103551cf(a0, a1, a2, a3, 0, NULL);
}
```

## `sub_1035539b` `0x1035539b`

_709 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    int field_4;
} struct_0;

unsigned int sub_1035539b(void* idx, struct_0 *index)
{
    int v12;  // edi
    int v13;  // esi
    unsigned int v22;  // edx
    struct_0 v23;  // eax
    unsigned int v24;  // eax
    unsigned int v25;  // ebx
    unsigned int v27;  // ebx
    unsigned int v28;  // ebx
    unsigned int v29;  // eax
    unsigned int v30;  // ebx
    int v31;  // edx
    int v14;  // eax
    unsigned int v32;  // eax
    unsigned int v33;  // ebx
    unsigned int v35;  // ebx
    unsigned int v36;  // eax
    unsigned int v37;  // ebx
    unsigned int v38;  // eax
    unsigned int v39;  // ebx
    unsigned int v41;  // ecx
    int v15;  // ecx
    unsigned int v42;  // eax
    unsigned int v43;  // eax
    int v44;  // eax
    struct_0 v16;  // ebx
    struct_0 v17;  // eax
    unsigned int v18;  // eax
    struct_0 v19;  // eax
    struct_0 v20;  // ecx
    unsigned int v21;  // ebx
    unsigned int v0;  // [bp-0x38]
    unsigned int v1;  // [bp-0x34]
    unsigned int v2;  // [bp-0x30]
    unsigned int v3;  // [bp-0x2c]
    unsigned int v4;  // [bp-0x28]
    unsigned int v5;  // [bp-0x24]
    struct_0 v6;  // [bp-0x18]
    struct_0 v7;  // [bp-0x18]
    unsigned int v8;  // [bp-0x14]
    struct_0 v9;  // [bp-0x10]
    unsigned int v10;  // [bp-0xc]
    struct_0 v11;  // [bp-0x8]

    v10 = 0;
    v9 = (struct_0)0;
    v11 = (struct_0)0;
    if (!idx)
    {
        v5 = 22;
        v5 = 0;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        *((unsigned int *)sub_103575e0(v12, v13)) = 22;
        sub_103535f2();
        return 22;
    }
    sub_10350ad0(idx, 255, 36);
    if (!index)
    {
LABEL_10355415:
        v4 = 22;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        *((unsigned int *)sub_103575e0()) = 22;
        sub_103535f2();
        goto LABEL_1035542c;
    }
    v14 = index->field_4;
    if (v14 <= NULL && (v14 < NULL || index->field_0 < NULL))
    {
        v4 = 22;
        *((unsigned int *)sub_103575e0()) = 22;
LABEL_1035542c:
        v18 = 22;
    }
    else
    {
        if (v14 >= 7 && (v14 > 7 || index->field_0 > 0x93406fff))
            goto LABEL_10355415;
        sub_1035dc60();
        if (sub_1035d4c0(&v10))
        {
            v4 = 0;
            v3 = 0;
            v2 = 0;
            v1 = 0;
            v0 = 0;
            sub_103534f6();
        }
        if (sub_1035d4f4(&v9))
        {
            v4 = 0;
            v3 = 0;
            v2 = 0;
            v1 = 0;
            v0 = 0;
            sub_103534f6();
        }
        if (sub_1035d528(&v11))
        {
            v4 = 0;
            v3 = 0;
            v2 = 0;
            v1 = 0;
            v0 = 0;
            sub_103534f6();
        }
        v15 = index->field_4;
        v16 = (struct_0)index->field_0;
        if (v15 >= NULL && (v15 > NULL || v16 > 259200))
        {
            v17 = v11;
            v6 = v16 - v17;
            v8 = (unsigned int)(v15 - (v17 >> 31) - (v16 < v17));
            v18 = sub_1035458a(idx, &v6);
            if (!v18)
            {
                if (!v10 || !sub_1035dcaf(idx))
                    goto LABEL_1035561a;
                v19 = v9;
                v7 = v6 - v19;
                v8 = (unsigned int)(v8 - (v19 >> 31) - (v6 < v19));
                v18 = sub_1035458a(idx, &v7);
                if (!v18)
                {
                    *((unsigned int *)&idx[32]) = 1;
LABEL_1035561a:
                    v18 = 0;
                }
            }
        }
        else
        {
            v18 = sub_1035458a(idx, index);
            if (v18)
                return v18;
            if (v10 && sub_1035dcaf(idx))
            {
                v20 = v11 + v9;
                idx = (int)(v20 >> 31);
                v21 = (unsigned int)(*((int *)idx) - v20);
                v22 = (*((int *)idx) >> 31) - idx - (*((int *)idx) < v20);
                v8 = v22;
                *((unsigned int *)&idx[32]) = 1;
            }
            else
            {
                v23 = v11;
                v21 = (unsigned int)(*((int *)idx) - v23);
                v8 = (unsigned int)((*((int *)idx) >> 31) - (v23 >> 31) - (*((int *)idx) < v23));
                v22 = v8;
            }
            v24 = sub_10353fd0(v21, v22, 60, 0);
            *((unsigned int *)idx) = v24;
            v25 = v21;
            if (v24 < NULL)
            {
                v8 = v8 - 1 + (v21 - 60 < v21);
                *((unsigned int *)idx) = v24 + 60;
                v25 = v21 - 60;
            }
            v28 = sub_103544e0(v25, v8, 60, 0, v27);
            v29 = (int)idx[4];
            v30 = v28 + v29;
            v8 = v31 + (v29 >> 31) + (v28 + v29 < v28);
            v32 = sub_10353fd0(v30, v8, 60, 0);
            *((unsigned int *)&idx[4]) = v32;
            v33 = v30;
            if (v32 < NULL)
            {
                v8 = v8 - 1 + (v30 - 60 < v30);
                *((unsigned int *)&idx[4]) = v32 + 60;
                v33 = v30 - 60;
            }
            v35 = sub_103544e0(v33, v8, 60, 0, 0);
            v36 = (int)idx[8];
            v37 = v35 + v36;
            v8 = v31 + (v36 >> 31) + (v35 + v36 < v35);
            v38 = sub_10353fd0(v37, v8, 24, 0);
            *((unsigned int *)&idx[8]) = v38;
            v39 = v37;
            if (v38 < NULL)
            {
                v8 = v8 - 1 + (v37 - 24 < v37);
                *((unsigned int *)&idx[8]) = v38 + 24;
                v39 = v37 - 24;
            }
            v41 = sub_103544e0(v39, v8, 24, 0, 0);
            if (v31 < NULL)
            {
LABEL_1035562b:
                v43 = (int)idx[24] + v41 + 7;
                v1 = 7;
                *((unsigned int *)&idx[12]) = (int)idx[12] + v41;
                v44 = (int)idx[12];
                *((unsigned int *)&idx[24]) = v43 % 7;
                if (v44 > 0)
                    goto LABEL_10355617;
                *((unsigned int *)&idx[28]) = (int)idx[28] + v41 + 365;
                *((unsigned int *)&idx[20]) = (int)idx[20] - 1;
                *((unsigned int *)&idx[12]) = v44 + 31;
                *((unsigned int *)&idx[16]) = 11;
                goto LABEL_1035561a;
            }
            else if (v31 > NULL || v41 > NULL)
            {
                v42 = (int)idx[24] + v41;
                v1 = 7;
                *((unsigned int *)&idx[12]) = (int)idx[12] + v41;
                *((unsigned int *)&idx[24]) = v42 % 7;
LABEL_10355617:
                *((unsigned int *)&idx[28]) = (int)idx[28] + v41;
                goto LABEL_1035561a;
            }
            else
            {
                if (v31 <= 0 && (v31 < 0 || v41 < 0))
                    goto LABEL_1035562b;
                goto LABEL_1035561a;
            }
        }
    }
    return v18;
}
```

## `sub_10355660` `0x10355660`

_36 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    int field_4;
} struct_0;

int sub_10355660(struct_0 *a0)
{
    unsigned int v1;  // esi
    int v0;  // [bp-0x4]

    v1 = sub_1035d478(v0);
    if (v1)
        return ~(-(0 < sub_1035539b(v1, a0))) & v1;
    return v1;
}
```

## `sub_10355690` `0x10355690`

_70 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10355690(char *a0, char *a1)
{
    int v8;  // eax
    char *v9;  // edx
    unsigned int v10;  // ecx
    unsigned int v11;  // ecx
    unsigned int v12;  // ecx
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x1c]
    unsigned int v4;  // [bp-0x18]
    unsigned int v5;  // [bp-0x14]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]

    v8 = 0;
    v7 = 0;
    v6 = 0;
    v5 = 0;
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    v9 = a1;
    while (true)
    {
        v8 = _INSERT(v8, 0, *(v9));
        if (!*(v9))
            break;
        v9 += 1;
        *((char *)&v0 + (v8 >> 3)) = *((char *)&v0 + (v8 >> 3)) | 1 << ((char)v8 & 7);
    }
    v10 = 4294967295;
    do
    {
        v12 = v10 + 1;
        v8 = _INSERT(v8, 0, *(a0));
    } while (*(a0) && (a0 += 1, v10 = v12, (*((char *)((char *)&v0 + (v8 >> 3))) >> (unsigned int)(char)((char)v8 & 7) & 1) != 1));
    return v11 + 1;
}
```

## `sub_103556d6` `0x103556d6`

_473 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b0a4;
extern struct_0 *g_1038b13c;
extern struct_0 *g_1038b1c0;
extern struct_0 *g_1038b204;
extern struct_0 *g_1038b220;
extern struct_0 *g_1038b224;
extern int g_1038e468;
extern unsigned int g_103a2ffc;
extern unsigned int g_103a3000;
extern unsigned int g_103a3004;
extern unsigned int g_103a3008;
extern unsigned int g_103a300c;
extern unsigned int g_103a3038;
extern unsigned int g_103a3044;
extern unsigned int g_103a3048;
extern int g_103a3394;
extern unsigned int g_103a4ccc;

unsigned int sub_103556d6(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v5;  // ecx
    unsigned int v6;  // ebx
    unsigned int *v15;  // eax
    unsigned int v16;  // eax
    unsigned int v7;  // esi
    unsigned int v8;  // edi
    unsigned int v9;  // eax
    unsigned int idx[5];  // esi
    unsigned int v11;  // eax
    unsigned int v12;  // edi
    unsigned int v13;  // eax
    unsigned int v14[2];  // esi
    unsigned int v0[2];  // [bp-0x20]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v4 = v5;
    v3 = v6;
    v2 = v7;
    v1 = v8;
    if (a1 == 1)
    {
        v9 = g_1038b224(0, 148);
        idx = g_1038b220(v9);
        if (idx)
        {
            idx[0] = 148;
            if (!g_1038b1c0(idx))
            {
                v11 = g_1038b224(0, idx);
                g_1038b204(v11);
            }
            else
            {
                a1 = idx[4];
                a2 = idx[1];
                v4 = idx[2];
                v12 = idx[3] & 0x7fff;
                v13 = g_1038b224(0, idx);
                g_1038b204(v13);
                if (a1 != 2)
                    v12 |= 0x8000;
                g_103a2ffc = a1;
                g_103a3004 = a2 * 0x100 + v4;
                g_103a3008 = a2;
                g_103a300c = v4;
                g_103a3000 = v12;
                if (sub_1035a355(1))
                {
                    if (sub_10358f4a())
                    {
                        sub_1035c533();
                        g_103a4ccc = g_1038b13c();
                        g_103a3048 = sub_1035e474();
                        if (sub_1035debc() >= 0)
                        {
                            if (sub_1035e3bb() >= 0 && sub_1035e148() >= 0 && !sub_10353dae(0))
                            {
                                g_103a3044 = g_103a3044 + 1;
                                return 1;
                            }
                            sub_1035e0fc();
                        }
                        sub_10358c35();
                    }
                    sub_1035a3af();
                }
            }
        }
    }
    else if (!a1)
    {
        if (g_103a3044 > 0)
        {
            g_103a3044 = g_103a3044 - 1;
            if (!g_103a3038)
                sub_10353f44();
            if (!a2)
            {
                sub_1035e0fc();
                sub_10358c35();
                sub_1035a3af();
                return 1;
            }
            goto LABEL_103558a5;
        }
    }
    else
    {
        if (a1 == 2)
        {
            sub_10358c03();
            v14 = sub_103574c2(1, 532);
            if (v14)
            {
                v15 = sub_10358b8c(g_103a3394, g_1038e468, v14);
                if (v15(g_1038e468, v14))
                {
                    sub_10358c72(v14, 0);
                    v16 = g_1038b0a4();
                    v14[1] = 4294967295;
                    v14[0] = v16;
                    return 1;
                }
                v0 = v14;
                sub_1035345e();
            }
        }
        else
        {
            if (a1 == 3)
                sub_10358ee1(0);
LABEL_103558a5:
            return 1;
        }
    }
    return 0;
}
```

## `sub_103558af` `0x103558af`

_226 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_10396910;
extern int g_103a0fa0;
extern char g_103a3044;

int sub_103558af(unsigned int a0, unsigned int a1)
{
    unsigned int v4;  // ebx
    unsigned int v5;  // edx
    unsigned int v6;  // ecx
    unsigned int v7;  // eax
    int v8;  // eax
    int v1;  // [bp+0xfffe8], Other Possible Types: unsigned int
    unsigned int v2;  // [bp+0x100000]
    unsigned int v3;  // [bp+0x10000c]

    sub_1035b0cc(&g_103a0fa0, 12);
    v4 = v3;
    v1 = 1;
    if (v5 || *((int *)&g_103a3044) != v5)
    {
        v2 = 0;
        if (v5 == 1 || v5 == 2)
        {
            if (g_10396910)
                v1 = sub_103698a0(v4, v5, v6);
            if (v1 && !((v7 = sub_103556d6(v4, v5, v6), v1 = v7, !v7)))
                goto LABEL_10355913;
            v2 = 4294967294;
        }
        else
        {
LABEL_10355913:
            v8 = sub_10312730(v4, v5, v6);
            v1 = v8;
            if (v5 == 1 && !v8)
            {
                sub_10312730(v4, 0, v6);
                sub_103556d6(v4, 0, v6);
                if (g_10396910)
                    sub_103698a0(v4, 0, v6);
            }
            if (!v5 || v5 == 3)
            {
                if (!sub_103556d6(v4, v5, v6))
                    v1 = 0;
                if (v1 && g_10396910)
                    v1 = sub_103698a0(v4, v5, v6);
            }
            v2 = 4294967294;
            return sub_1035b111();
        }
    }
    return sub_1035b111();
}
```

## `sub_10355982` `0x10355982`

_17 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    int field_0;
} struct_0;

int sub_10355982(void)
{
    struct_0 **v1;  // [bp+0xffff0]

    return sub_1035c81a(*(v1)->field_0, v1);
}
```

## `sub_10355993` `0x10355993`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10355993(void)
{
}
```

## `sub_103559a5` `0x103559a5`

_33 bytes. (leaf/helper — see body)_

```c
int sub_103559a5(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v0;  // [bp-0x4]

    if (a1 == 1)
        sub_1035e5a9();
    v0 = a0;
    return sub_103558af(a2, a1);
}
```

## `sub_103559c6` `0x103559c6`

_70 bytes. (leaf/helper — see body)_

```c
extern int g_103a0fc0;
extern char g_103a4cb0;

int sub_103559c6(void)
{
    int v4;  // esi
    unsigned int v1;  // [bp+0xfffe8]
    unsigned int v2;  // [bp+0x100000]
    int v3;  // [bp+0x10000c]

    sub_1035b0cc(&g_103a0fc0, 12);
    v1 = 0;
    v4 = v3;
    if (v4 <= *((int *)&g_103a4cb0))
    {
        sub_1035a599(4);
        v2 = 0;
        v1 = sub_1035ade6(v4);
        v2 = 4294967294;
        sub_10355a0c();
    }
    return sub_1035b111();
}
```

## `sub_10355a0c` `0x10355a0c`

_9 bytes. (leaf/helper — see body)_

```c
void sub_10355a0c(void)
{
    sub_1035a4c1(4);
    return;
}
```

## `sub_10355a15` `0x10355a15`

_193 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b220;
extern unsigned int g_103a36c8;
extern char g_103a3a44;
extern unsigned int g_103a4cc0;

int sub_10355a15(unsigned int a0)
{
    unsigned int v4;  // ebp
    unsigned int v5;  // ebx
    unsigned int v6;  // esi
    unsigned int v7;  // edi
    unsigned int v8;  // eax
    int v10;  // eax
    unsigned int v11;  // edi
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v4 = a0;
    if (v4 > 0xffffffe0)
    {
        sub_103540ea(v4);
        *((unsigned int *)sub_103575e0()) = 12;
        return 0;
    }
    v3 = v5;
    v2 = v6;
    v1 = v7;
    do
    {
        if (!g_103a36c8)
        {
            sub_1035a15d();
            sub_10359fbd(30);
            sub_10353cdc(0xff); /* do not return */
        }
        if (g_103a4cc0 == 1)
        {
            if (v4)
                v8 = v4;
            else
                v8 = 1;
            v0 = v8;
        }
        else
        {
            if (g_103a4cc0 == 3 && !((v0 = v4, v10 = sub_103559c6(), !v10)))
                goto LABEL_10355a8f;
            v11 = v4;
            if (!v11)
                v11 = 1;
            v0 = v11 + 15 & 0xfffffff0;
        }
        v10 = g_1038b220(g_103a36c8, 0);
LABEL_10355a8f:
        if (v10)
            return v10;
        v0 = 12;
        if (*((int *)&g_103a3a44) == v10)
        {
            *((unsigned int *)sub_103575e0()) = 12;
            break;
        }
    } while (sub_103540ea(v4));
    *((unsigned int *)sub_103575e0()) = 12;
    return v10;
}
```

## `sub_10355a4e` `0x10355a4e`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10355a4e(unsigned int a0)
{
}
```

## `sub_10355ad8` `0x10355ad8`

_51 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

char * sub_10355ad8(unsigned int a0)
{
    unsigned long v2;  // ldt
    unsigned long v3;  // gdt
    unsigned short v4;  // fs
    unsigned long v5;  // 4139
    unsigned int v6;  // ebx
    unsigned int v7;  // esi
    unsigned int v8;  // edi
    unsigned long v9;  // 4170
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp+0x0]

    v5 = _ccall(v2, v3, (unsigned int)v4, 0);
    v0 = *((int *)v5);
    /* unsupported instruction */ = (char *)&v0 - a0;
    /* unsupported instruction */ = /* unsupported instruction */ - 4;
    *((unsigned int *)(/* unsupported instruction */ - 4)) = v6;
    /* unsupported instruction */ = /* unsupported instruction */ - 4;
    *((unsigned int *)(/* unsupported instruction */ - 4)) = v7;
    /* unsupported instruction */ = /* unsupported instruction */ - 4;
    *((unsigned int *)(/* unsupported instruction */ - 4)) = v8;
    *((unsigned long *)(/* unsupported instruction */ - 4)) = g_1038e180 ^ &/* unsupported instruction */;
    *((unsigned int *)(/* unsupported instruction */ - 8)) = v1;
    v9 = _ccall(v2, v3, (unsigned int)v4, 0);
    *((unsigned int **)v9) = &v0;
    return &v0;
}
```

## `sub_10355b0b` `0x10355b0b`

_54 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

char * sub_10355b0b(unsigned int a0)
{
    unsigned long v2;  // ldt
    unsigned long v3;  // gdt
    unsigned short v4;  // fs
    unsigned long v5;  // 4140
    unsigned int v6;  // ebx
    unsigned int v7;  // esi
    unsigned int v8;  // edi
    unsigned long v9;  // 4174
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp+0x0]

    v5 = _ccall(v2, v3, (unsigned int)v4, 0);
    v0 = *((int *)v5);
    /* unsupported instruction */ = (char *)&v0 - a0;
    /* unsupported instruction */ = /* unsupported instruction */ - 4;
    *((unsigned int *)(/* unsupported instruction */ - 4)) = v6;
    /* unsupported instruction */ = /* unsupported instruction */ - 4;
    *((unsigned int *)(/* unsupported instruction */ - 4)) = v7;
    /* unsupported instruction */ = /* unsupported instruction */ - 4;
    *((unsigned int *)(/* unsupported instruction */ - 4)) = v8;
    *((unsigned long *)(/* unsupported instruction */ - 4)) = g_1038e180 ^ &/* unsupported instruction */;
    *((unsigned int *)(/* unsupported instruction */ - 8)) = v1;
    v9 = _ccall(v2, v3, (unsigned int)v4, 0);
    *((unsigned int **)v9) = &v0;
    return &v0;
}
```

## `sub_10355b41` `0x10355b41`

_20 bytes. (leaf/helper — see body)_

```c
void sub_10355b41(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned long v1;  // ldt
    unsigned long v2;  // gdt
    unsigned short v3;  // fs
    unsigned long v4;  // 4123
    unsigned int v0;  // [bp+0xffff8]

    v4 = _ccall(v1, v2, (unsigned int)v3, 0);
    *((unsigned int *)v4) = v0;
    return;
}
```

## `sub_10355b55` `0x10355b55`

_320 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[72];
    unsigned int field_48;
    unsigned int field_4c;
    struct struct_2 *field_50;
    struct struct_2 *field_54;
    char padding_58[88];
    struct struct_2 *field_b0;
    struct struct_2 *field_b4;
    struct struct_2 *field_b8;
    unsigned int field_bc;
    struct struct_2 *field_c0;
    unsigned int field_c4;
    char padding_c8[4];
    unsigned int field_cc;
    unsigned int field_d0;
    struct struct_0 *field_d4;
} struct_1;

typedef struct struct_0 {
    char padding_0[180];
    unsigned int field_b4;
} struct_0;

typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

extern char g_1038e1b4;
extern struct_0 g_1038e200;

void sub_10355b55(struct_1 *idx)
{
    unsigned int *v4;  // eax
    unsigned int *v5;  // eax
    struct_1 *v6;  // edi
    struct_0 *v7;  // eax
    struct_1 *iter;  // edi
    unsigned int i;  // ebx
    unsigned int *v10;  // eax
    unsigned int *v11;  // eax
    unsigned int v12;  // ebx
    unsigned int *v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    struct_0 *v2;  // [bp-0x18], Other Possible Types: unsigned int
    struct_1 *v3;  // [bp-0x14], Other Possible Types: unsigned int *, unsigned int

    if (idx->field_bc && idx->field_bc != &g_1038e1b4 && idx->field_b0 && !idx->field_b0->field_0)
    {
        v4 = &idx->field_b8->field_0;
        if (v4 && !*(v4))
        {
            v3 = v4;
            sub_1035345e();
            sub_1035ee61(idx->field_bc);
        }
        v5 = &idx->field_b4->field_0;
        if (v5 && !*(v5))
        {
            v3 = v5;
            sub_1035345e();
            sub_1035ec59(idx->field_bc);
        }
        v3 = &idx->field_b0->field_0;
        sub_1035345e();
        v2 = idx->field_bc;
        sub_1035345e();
    }
    if (idx->field_c0 && !idx->field_c0->field_0)
    {
        v3 = idx->field_c4 - 254;
        sub_1035345e();
        v2 = idx->field_cc - 128;
        sub_1035345e();
        v1 = idx->field_d0 - 128;
        sub_1035345e();
        v0 = &idx->field_c0->field_0;
        sub_1035345e();
    }
    v6 = &idx->field_d4;
    v7 = *((int *)&v6->padding_0[0]);
    if (v7 != &g_1038e200.padding_0[0] && !v7->field_b4)
    {
        sub_1035ea56(v7);
        v2 = *((int *)&v6->padding_0[0]);
        sub_1035345e();
    }
    v3 = 6;
    iter = &idx->field_50;
    do
    {
        i = v3;
        if (*((int *)&iter->padding_0[8]) != "C")
        {
            v10 = *((int *)&iter->padding_0[0]);
            if (v10 && !*(v10))
            {
                v3 = v10;
                sub_1035345e();
            }
        }
        if (*((int *)&iter->padding_0[4]))
        {
            v11 = *((int *)&iter->padding_0[4]);
            if (v11 && !*(v11))
            {
                v3 = v11;
                sub_1035345e();
            }
        }
        iter = &iter->padding_0[16];
        v12 = i - 1;
        v3 = v12;
    } while (i != 1);
    v3 = idx;
    sub_1035345e();
    return;
}
```

## `sub_10355c95` `0x10355c95`

_134 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1ec;

int sub_10355c95(unsigned int *a0)
{
    unsigned int v1;  // edi
    unsigned int v2;  // esi
    unsigned int v3;  // ebx
    unsigned int v4[54];  // ebx
    unsigned int i;  // ebp
    unsigned int v6;  // ebp
    unsigned int v0;  // [bp-0x28]

    g_1038b1ec(a0, v1, v2, /* unsupported instruction */, v3);
    if (a0[44])
        g_1038b1ec(a0[44]);
    if (a0[46])
        g_1038b1ec(a0[46]);
    if (a0[45])
        g_1038b1ec(a0[45]);
    if (a0[48])
        g_1038b1ec(a0[48]);
    v0 = 6;
    v4 = a0 + 20;
    do
    {
        i = v0;
        if (v4[2] != "C" && v4[0])
            g_1038b1ec(v4[0]);
        if (v4[1] && v4[1])
            g_1038b1ec(v4[1]);
        v4 = &v4[4];
        v6 = i - 1;
        v0 = v6;
    } while (i != 1);
    return g_1038b1ec(a0[53] + 180);
}
```

## `sub_10355d1b` `0x10355d1b`

_140 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1f0;

unsigned int [54] sub_10355d1b(unsigned int *a0)
{
    unsigned int v2;  // esi
    unsigned int v3;  // edi
    unsigned int v4;  // ebx
    unsigned int v5[54];  // ebx
    unsigned int i;  // ebp
    unsigned int v7;  // ebp
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x4]

    v1 = v2;
    if (!a0)
        return a0;
    g_1038b1f0(a0, v3, /* unsupported instruction */, v4);
    if (a0[44])
        g_1038b1f0(a0[44]);
    if (a0[46])
        g_1038b1f0(a0[46]);
    if (a0[45])
        g_1038b1f0(a0[45]);
    if (a0[48])
        g_1038b1f0(a0[48]);
    v0 = 6;
    v5 = a0 + 20;
    do
    {
        i = v0;
        if (v5[2] != "C" && v5[0])
            g_1038b1f0(v5[0]);
        if (v5[1] && v5[1])
            g_1038b1f0(v5[1]);
        v5 = &v5[4];
        v7 = i - 1;
        v0 = v7;
    } while (i != 1);
    g_1038b1f0(a0[53] + 180);
    return a0;
}
```

## `sub_10355da7` `0x10355da7`

_36 bytes. (leaf/helper — see body)_

```c
int sub_10355da7(void)
{
    unsigned int *v3;  // ecx
    unsigned int *i;  // esi
    unsigned int *v5;  // eax
    unsigned int v6;  // edi
    unsigned int *iter;  // edi
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    i = v3;
    if (!i)
    {
        return;
    }
    else if (!v5)
    {
        return;
    }
    else if (v5 != i)
    {
        v1 = v6;
        v0 = 54;
        for (iter = v5; v0; i += 1)
        {
            v0 -= 1;
            *(iter) = *(i);
            iter += 1;
        }
        *(v5) = 0;
        sub_10355c95(v5);
        return;
    }
    else
    {
        return;
    }
}
```

## `sub_10355dcb` `0x10355dcb`

_62 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern unsigned int g_1038e670;

int sub_10355dcb(void)
{
    unsigned int *v2;  // edi
    struct_0 **v3;  // eax
    unsigned int v4;  // esi
    unsigned int *v5;  // esi
    unsigned int v0;  // [bp-0x4]

    if (!v2)
    {
        return;
    }
    else if (v3)
    {
        v0 = v4;
        v5 = &*(v3)->field_0;
        if (v5 == v2)
            return;
        *(v3) = v2;
        sub_10355c95(v2);
        if (!v5)
            return;
        sub_10355d1b(v5);
        if (*(v5))
            return;
        if (v5 == &g_1038e670)
            return;
        sub_10355b55(v5);
        return;
    }
    else
    {
        return;
    }
}
```

## `sub_10355e09` `0x10355e09`

_106 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e660;
extern int g_103a0fe0;

int sub_10355e09(void)
{
    unsigned int v3[29];  // esi
    int v1;  // [bp+0xfffe8]
    unsigned int v2;  // [bp+0x100000]

    sub_1035b0cc(&g_103a0fe0, 12);
    v3 = sub_10358da8(&g_103a0fe0, 12);
    if ((g_1038e660 & v3[28]) && v3[27])
    {
        v3 = *((int *)(sub_10358da8() + 108));
    }
    else
    {
        sub_1035a599(12);
        v2 = 0;
        v1 = sub_10355dcb();
        v2 = 4294967294;
        sub_10355e73();
    }
    if (!v3)
        sub_10353c92(32);
    return sub_1035b111();
}
```

## `sub_10355e73` `0x10355e73`

_12 bytes. (leaf/helper — see body)_

```c
void sub_10355e73(void)
{
    sub_1035a4c1(12);
    return;
}
```

## `sub_10355e7f` `0x10355e7f`

_83 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
    unsigned int field_8;
    char padding_c[156];
    unsigned int field_a8;
    unsigned int field_ac;
    char padding_b0[12];
    unsigned int field_bc;
    char padding_c0[8];
    unsigned int field_c8;
    char padding_cc[8];
    unsigned int field_d4;
} struct_0;

extern unsigned int g_1038e1e4;
extern unsigned int g_1038e2b8;
extern unsigned int g_1038e2c4;
extern struct_0 *g_1038e748;
extern unsigned int g_1038e74c;
extern unsigned int g_1038f108;
extern unsigned int g_103a383c;
extern unsigned int g_103a3840;

int sub_10355e7f(void)
{
    g_103a383c = g_1038e748->field_4;
    g_103a3840 = g_1038e748->field_8;
    g_1038e74c = g_1038e748->field_a8;
    g_1038e2b8 = g_1038e748->field_d4;
    g_1038e1e4 = g_1038e748->field_bc;
    g_1038e2c4 = g_1038e748->field_c8;
    g_1038f108 = g_1038e748->field_ac;
    return g_1038f108;
}
```

## `sub_10355ed2` `0x10355ed2`

_138 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
    unsigned int field_4;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1f0;
extern unsigned int g_1038e670;
extern char g_1038e758;
extern int g_103a1000;

void sub_10355ed2(void)
{
    struct_1 *idx;  // esi
    unsigned int *v5;  // eax
    struct_1 *v0;  // [bp-0x10], Other Possible Types: unsigned int
    unsigned int v2;  // [bp+0x100000]
    struct_1 *v3;  // [bp+0x10000c]

    sub_1035b0cc(&g_103a1000, 8);
    idx = v3;
    if (!idx)
    {
        sub_1035b111();
        return;
    }
    if (idx->field_4 && !g_1038b1f0(idx->field_4) && idx->field_4 != &g_1038e758)
    {
        v0 = idx->field_4;
        sub_1035345e();
    }
    if (idx->field_0)
    {
        sub_1035a599(12);
        v2 = 0;
        sub_10355d1b(idx->field_0);
        v5 = &idx->field_0->field_0;
        if (v5 && !*(v5) && v5 != &g_1038e670)
            sub_10355b55(v5);
        v2 = 4294967294;
        sub_10355f5f();
    }
    idx->field_0 = 0xbaadf00d;
    idx->field_4 = 0xbaadf00d;
    v0 = idx;
    sub_1035345e();
    sub_1035b111();
    return;
}
```

## `sub_10355f5c` `0x10355f5c`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10355f5c(void)
{
    sub_10355f5f();
    return;
}
```

## `sub_10355f5f` `0x10355f5f`

_9 bytes. (leaf/helper — see body)_

```c
void sub_10355f5f(void)
{
    sub_1035a4c1(12);
    return;
}
```

## `sub_10355f68` `0x10355f68`

_62 bytes. (leaf/helper — see body)_

```c
void sub_10355f68(int a0, int a1, int a2, unsigned int a3)
{
    unsigned int v6;  // edi
    unsigned int v7;  // esi
    int *v8;  // esi
    unsigned int v9;  // edi
    unsigned int v10;  // edi
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]

    v6 = *((unsigned int *)&a2);
    if (v6 <= 0)
        return;
    v5 = v7;
    v8 = &a2;
    do
    {
        v9 = v6;
        v8 += 1;
        if (sub_1035f1b1(a0, a1, *(v8)))
        {
            v4 = 0;
            v3 = 0;
            v2 = 0;
            v1 = 0;
            v0 = 0;
            sub_103534f6();
        }
    } while ((v10 = v9 - 1, v6 = v9 - 1, v9 != 1));
    return;
}
```

## `sub_10355fa6` `0x10355fa6`

_297 bytes. refs "_.,", "_.,"_

```c
typedef struct struct_0 {
    char padding_0[143];
    char field_8f;
} struct_0;

unsigned int sub_10355fa6(struct_0 *a0, char *a1)
{
    struct_0 *v3;  // edi
    char v4[2];  // esi, Other Possible Types: unsigned int
    unsigned int v12;  // eax
    char v5[2];  // eax
    unsigned int v6;  // cc_op
    unsigned int v7;  // cc_dep1
    unsigned int v8;  // 4107
    char v9[2];  // edi
    char v10;  // bl
    struct_0 *v11;  // eax
    unsigned int v0;  // [bp-0x24]
    struct_0 *v1;  // [bp-0x20], Other Possible Types: unsigned int
    int v2;  // [bp-0x1c], Other Possible Types: unsigned int

    v3 = a0;
    sub_10350ad0(v3, 0, 144);
    v4 = a1;
    if (!v4[0])
        return 0;
    if (v4[0] == 46 && !((v5 = v4 + 1, !v5[0])))
    {
        if (sub_1035f222(&v3->padding_0[128], 16, v5, 15))
        {
            v12 = 0;
            v4 = 0;
            v2 = 0;
            v1 = 0;
            v0 = 0;
            sub_103534f6();
        }
        v3->field_8f = 0;
    }
    else
    {
        a1 = 0;
        v12 = sub_10355690(v4, "_.,");
        v6 = 6;
        v7 = v12;
        while (true)
        {
            v8 = _ccall(4, v6, v7, 0, 0);
            if ((char)v8)
            {
LABEL_103560c7:
                return 4294967295;
            }
            v9 = &v4[v12];
            v10 = v9[0];
            if (!a1 && v12 < 64 && v10 != 46)
            {
                v2 = 64;
                v1 = a0;
                v1 = a0;
                goto LABEL_10356080;
            }
            if (a1 == 1 && v12 < 64 && v10 != 95)
            {
                v2 = 64;
                v11 = &a0->padding_0[64];
                goto LABEL_1035607f;
            }
            if (a1 != 2)
                return 4294967295;
            if (v12 >= 16)
                return 4294967295;
            if (v10 && v10 != 44)
                goto LABEL_103560c7;
            v2 = 16;
            v11 = &a0->padding_0[128];
LABEL_1035607f:
            v1 = v11;
            v1 = v11;
LABEL_10356080:
            if (sub_1035f222(v1, v2, v4, v12))
            {
                v12 = 0;
                v4 = 0;
                v2 = 0;
                v1 = 0;
                v0 = 0;
                sub_103534f6();
            }
            if (v10 == 44 || !v10)
                break;
            a1 += 1;
            v4 = &v9[1];
            v12 = sub_10355690(v4, "_.,");
            v6 = 15;
            v7 = v12;
        }
    }
    return 0;
}
```

## `sub_103560cf` `0x103560cf`

_107 bytes. (leaf/helper — see body)_

```c
char [129] sub_103560cf(int a0, int a1, char *a2)
{
    int v7;  // esi
    int v8;  // ebx
    char v9[129];  // eax
    char v10[129];  // eax
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    char v4[129];  // [bp-0x10], Other Possible Types: unsigned int
    char v5[129];  // [bp-0x8]
    char v6;  // [bp+0x0]

    if (sub_10359f58(a0, a1, a2, v7, v8, &v6))
    {
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        sub_103534f6();
    }
    v9 = a2 + 64;
    if (v9[0])
    {
        v4 = v9;
        sub_10355f68(a0, a1, 2, "_");
    }
    v10 = a2 + 128;
    if (!v10[0])
        return v5;
    v5 = v10;
    return (unsigned int)sub_10355f68(a0, a1, 2, ".");
}
```

## `sub_1035613a` `0x1035613a`

_369 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    char field_4;
} struct_0;

typedef struct struct_1 {
    char padding_0[72];
    struct struct_0 *field_48;
    unsigned int field_4c;
    unsigned int field_50;
    unsigned int field_54;
    unsigned int field_58;
    char padding_5c[12];
    struct struct_0 *field_68;
} struct_1;

typedef struct struct_3 {
    unsigned int field_0;
} struct_3;

extern struct_3 *g_1038b1f0;
extern unsigned int g_103947ac;
extern unsigned int g_103947dc;

struct_0 * sub_1035613a(void)
{
    int v11;  // ebx
    unsigned int v12;  // edi
    struct_0 *v13;  // edi
    struct_1 *idx;  // esi
    struct_1 *v15;  // ebp
    struct_1 *v16;  // ebx
    struct_0 *v17;  // eax
    unsigned int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x2c]
    unsigned int v2;  // [bp-0x28]
    unsigned int v3;  // [bp-0x24]
    struct_0 *v4;  // [bp-0x20], Other Possible Types: unsigned int
    unsigned int v5;  // [bp-0x1c]
    unsigned int *i;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]
    struct_0 *v9;  // [bp-0x4]

    v8 = 1;
    v9 = sub_10357482(853, v11);
    if (!v9)
        return v9;
    v5 = v12;
    v13 = &v9->field_4;
    *((char *)&v13->field_0) = 0;
    v9->field_0 = 1;
    v15 = &idx->padding_0[16];
    v7 = 1;
    v16 = &v15->field_48;
    v4 = *((int *)&v16->padding_0[0]);
    v3 = "=";
    sub_10355f68(v13, 849, 3, g_103947ac);
    i = &g_103947ac;
    do
    {
        if (sub_1035f1b1(v13, 849, ";"))
        {
            v4 = 0;
            v3 = 0;
            v2 = 0;
            v1 = 0;
            v0 = 0;
            sub_103534f6();
        }
        if (sub_10359ed0(*((int *)&v16->padding_0[0]), v15->field_58))
            v8 = 0;
        v7 += 1;
        i += 3;
        v15 = &idx->padding_0[16 * v7];
        v16 = &v15->field_48;
        v4 = *((int *)&v16->padding_0[0]);
        v3 = "=";
        sub_10355f68(v13, 849, 3, *(i));
    } while (i < &g_103947dc);
    if (!v8)
    {
        if (idx->field_50 && !g_1038b1f0(idx->field_50))
        {
            v3 = idx->field_50;
            sub_1035345e();
        }
        if (idx->field_54 && !g_1038b1f0(idx->field_54))
        {
            v2 = idx->field_54;
            sub_1035345e();
        }
        idx->field_50 = v7;
        idx->field_48 = v13;
        v17 = v13;
    }
    else
    {
        v4 = v9;
        sub_1035345e();
        if (idx->field_50 && !g_1038b1f0(idx->field_50))
        {
            v3 = idx->field_50;
            sub_1035345e();
        }
        if (idx->field_54 && !g_1038b1f0(idx->field_54))
        {
            v2 = idx->field_54;
            sub_1035345e();
        }
        v17 = idx->field_68;
        idx->field_50 = 0;
        idx->field_48 = NULL;
    }
    idx->field_4c = 0;
    idx->field_54 = 0;
    return v17;
}
```

## `sub_103562ab` `0x103562ab`

_468 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[192];
    unsigned short field_c0;
    char padding_c2[2];
    unsigned int field_c4;
} struct_0;

extern unsigned int g_1038e180;
extern char g_1038f8e4[2];

int sub_103562ab(char *a0, int a1, int a2, void* a3, void* a4)
{
    char v13[2];  // esi
    int v14;  // edi
    int v15;  // esi
    int v16;  // ebx
    struct_0 *v17;  // eax
    struct_0 *v18;  // ebx
    int v19;  // eax
    unsigned int v0;  // [bp-0xd8]
    unsigned int v1;  // [bp-0xd4]
    unsigned int v2;  // [bp-0xd0]
    unsigned int v3;  // [bp-0xcc]
    unsigned int v4;  // [bp-0xc8]
    int v5;  // [bp-0xb8]
    int v6;  // [bp-0xb4]
    struct_0 *v7;  // [bp-0xb0]
    struct_0 *v8;  // [bp-0xac]
    struct_0 *v9;  // [bp-0x9c]
    struct_0 v10;  // [bp-0x98]
    char v11;  // [bp-0x64]
    unsigned int v12;  // [bp-0x8]

    v12 = g_1038e180 ^ &v11;
    v13 = a0;
    v17 = sub_10358da8(v14, v15, v16) + 156;
    v7 = &v17->padding_0[40];
    v18 = &v17->padding_0[32];
    v8 = &v17->padding_0[44];
    v9 = &v17->padding_0[175];
    if (!(v13 && a1 && a2))
    {
LABEL_1035646b:
    }
    else if (v13[0] == 67 && !v13[1])
    {
        if (sub_10359f58(a1, a2, "C"))
        {
            v4 = 0;
            v3 = 0;
            v2 = 0;
            v1 = 0;
            v0 = 0;
            sub_103534f6();
        }
        if (a3)
            memset(a3, 0, 6);
        if (a4)
            *((unsigned int *)a4) = 0;
    }
    else
    {
        v6 = sub_10352f20(v13);
        if (v6 >= 131 || sub_10359ed0(v9, v13) && sub_10359ed0(v8, v13))
        {
            v5 = 0;
            if (sub_10355fa6(&v10, v13) || !sub_1035f84f(&v10, v18, &v10))
                goto LABEL_1035646b;
            *((unsigned int *)&v7->padding_0[0]) = *((short *)&v18->padding_0[4]);
            sub_103560cf(v9, 131, &v10);
            if (!v13[0] || (v19 = v6, v19 >= 131))
            {
                v19 = v5;
                v13 = &g_1038f8e4[0];
            }
            if (!sub_1035f222(v8, 131, v13, v19 + 1))
                goto LABEL_1035641a;
            v4 = 0;
            v3 = 0;
            v2 = 0;
            v1 = 0;
            v0 = 0;
            sub_103534f6();
        }
        else
        {
LABEL_1035641a:
        }
        if (a3)
            sub_10350b50(a3, v18, 6);
        if (a4)
            sub_10350b50(a4, v7, 4);
        if (sub_10359f58(a1, a2, v9))
        {
            v4 = 0;
            v3 = 0;
            v2 = 0;
            v1 = 0;
            v0 = 0;
            sub_103534f6();
        }
    }
    return sub_10351225();
}
```

## `sub_1035647f` `0x1035647f`

_758 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    int field_0;
    unsigned int field_4;
    unsigned int field_8;
    char padding_c[8];
    int field_14;
    char padding_18[48];
    int field_48;
    char padding_4c[8];
    unsigned int field_54;
    char padding_58[80];
    unsigned int field_a8;
} struct_0;

typedef struct struct_1 {
    char padding_0[12];
    unsigned int field_c;
} struct_1;

typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

extern struct_2 *g_1038b1f0;
extern unsigned int g_1038e180;
extern void* g_1038e2c0;
extern unsigned int g_103947a8[4];
extern int g_103947e8;

int sub_1035647f(char *a0, unsigned int a1, unsigned int a2)
{
    int v20;  // edi
    int v21;  // ebx
    unsigned int v30;  // edx
    unsigned int idx[2];  // eax
    unsigned int idx1;  // eax
    struct_0 *v33;  // edi
    unsigned int idx2[126];  // edi
    struct_0 *index;  // esi
    struct_0 *v24;  // ebx
    unsigned int v26;  // ecx
    unsigned int v27;  // ecx
    unsigned int iter[126];  // eax
    unsigned int v29;  // edx
    unsigned int v0;  // [bp-0x1e4]
    unsigned int v1;  // [bp-0x1e0]
    unsigned int v2;  // [bp-0x1dc]
    int v3;  // [bp-0x1d8], Other Possible Types: unsigned int
    int v4;  // [bp-0x1d4], Other Possible Types: unsigned int
    char v5;  // [bp-0x1c8]
    unsigned int v6;  // [bp-0x1c0]
    unsigned int v7;  // [bp-0x1b8]
    char v8;  // [bp-0x1b4], Other Possible Types: unsigned short
    unsigned int v9;  // [bp-0x1ac]
    int v10;  // [bp-0x1a8]
    struct_0 *v11;  // [bp-0x1a0], Other Possible Types: unsigned int
    char v12;  // [bp-0x19c], Other Possible Types: unsigned int
    struct_1 *v13;  // [bp-0x198]
    int v14;  // [bp-0x194]
    int i;  // [bp-0x190]
    char v16;  // [bp-0x18c]
    char v17;  // [bp-0x8c]
    char v18;  // [bp-0x78]
    unsigned int v19;  // [bp-0x8]

    v19 = g_1038e180 ^ &v18;
    v4 = a2;
    idx2 = sub_10358da8(v20, v21) + 464;
    if (!sub_103562ab(a0, &v17, 131, &v8, &v12))
    {
LABEL_103564cc:
    }
    else
    {
        v24 = &(&index->field_0)[4 * a2];
        if (sub_10359ed0(&v17, v24->field_48))
        {
            i = sub_10352f20(&v17) + 5;
            v14 = sub_10357482(i);
            if (v14)
            {
                v26 = a2;
                v10 = v24->field_48;
                v13 = &(&index->field_0)[v26 + 3];
                v9 = *((int *)&v13->padding_0[0]);
                v11 = &index->padding_18[12 + 6 * v26];
                sub_10350b50(&v5, v11, 6);
                v7 = index->field_4;
                if (sub_10359f58(v14 + 4, i - 4, &v17))
                {
                    v4 = 0;
                    v3 = 0;
                    v2 = 0;
                    v1 = 0;
                    v0 = 0;
                    sub_103534f6();
                }
                v24->field_48 = v14 + 4;
                *((unsigned int *)&v13->padding_0[0]) = v8;
                sub_10350b50(v11, &v8, 6);
                if (a2 == 2)
                {
                    i = 0;
                    index->field_4 = v12;
                    v27 = idx2[8];
                    v11 = idx2[9];
                    iter = idx2;
                    do
                    {
                        if (index->field_4 == iter[0] && i)
                        {
                            idx = &idx2[2 * i];
                            idx2[0] = idx[0];
                            idx2[1] = idx[1];
                            idx[0] = v27;
                            idx[1] = v11;
                            break;
                        }
                        v29 = iter[0];
                        i += 1;
                        iter[0] = v27;
                        v6 = v29;
                        v30 = iter[1];
                        iter[1] = v11;
                        v27 = v6;
                        iter = &iter[2];
                        v11 = v30;
                    } while (i < 5);
                    if (i == 5)
                    {
                        if (sub_1035fbea(0, 1, &g_103947e8, 127, &v16, index->field_4, index->field_14, 1))
                        {
                            idx1 = 0;
                            do
                            {
                                *((unsigned short *)&(&v16)[2 * idx1]) = *((short *)&(&v16)[2 * idx1]) & 0x1ff;
                                idx1 += 1;
                            } while (idx1 < 127);
                            idx2[1] = -(0 < sub_10351234(&v16, g_1038e2c0, 254)) + 1;
                        }
                        else
                        {
                            idx2[1] = 0;
                        }
                        idx2[0] = index->field_4;
                    }
                    index->field_a8 = idx2[1];
                }
                if (a2 == 1)
                    index->field_8 = v12;
                if (g_103947a8[3 * a2](index))
                {
                    v4 = v14;
                    v24->field_48 = v10;
                    sub_1035345e();
                    *((unsigned int *)&v13->padding_0[0]) = v9;
                    index->field_4 = v7;
                    goto LABEL_103564cc;
                }
                else
                {
                    if (v10 != "C")
                    {
                        v33 = &(index->padding_4c)[2 * a2 + 4];
                        if (!g_1038b1f0(v33->field_0))
                        {
                            v3 = v33->field_0;
                            sub_1035345e();
                            v2 = v24->field_54;
                            sub_1035345e();
                            *((unsigned int *)&v24->padding_4c[0]) = 0;
                        }
                    }
                    *((unsigned int *)v14) = 1;
                    *((int *)&(index->padding_4c)[2 * a2 + 4]) = v14;
                    goto LABEL_10356761;
                }
            }
        }
        else
        {
LABEL_10356761:
        }
    }
    return sub_10351225();
}
```

## `sub_10356775` `0x10356775`

_462 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[72];
    int field_48;
} struct_0;

extern unsigned int g_1038e180;
extern void g_103947ac;
extern void g_103947dc;

int sub_10356775(char *a0, struct_0 *a1, unsigned int a2)
{
    unsigned int v15;  // ebx
    unsigned int v16;  // esi
    unsigned int v25;  // edx
    char v26[3];  // edi
    struct_0 *v27;  // edi
    unsigned int v17;  // ebx
    unsigned int v18;  // edi
    char v19[3];  // edi
    char v20[3];  // ebx
    char i[3];  // eax
    void* v22;  // esi
    char v23[3];  // ebx
    unsigned int v24;  // edi
    unsigned int v0;  // [bp-0xbc]
    unsigned int v1;  // [bp-0xb8]
    unsigned int v2;  // [bp-0xb4]
    unsigned int v3;  // [bp-0xb0]
    unsigned int v4;  // [bp-0xac]
    unsigned int v5;  // [bp-0xa8]
    unsigned int v6;  // [bp-0xa4]
    unsigned int v7;  // [bp-0xa0]
    struct_0 *v8;  // [bp-0x9c]
    unsigned int v9;  // [bp-0x98]
    char v10[3];  // [bp-0x94], Other Possible Types: unsigned int
    unsigned int iter;  // [bp-0x90]
    char v12[20];  // [bp-0x8c]
    char v13;  // [bp-0x78]
    unsigned int v14;  // [bp-0x8]

    v14 = g_1038e180 ^ &v13;
    v7 = v15;
    v6 = v16;
    v17 = 0;
    v5 = v18;
    v8 = a1;
    if (!a2)
    {
        v10 = 1;
        iter = 0;
        if (a0)
        {
            if (*(a0) == 76 && a0[1] == 67 && a0[2] == 95)
            {
                v19 = a0;
                do
                {
                    v20 = sub_1035fcf0(v19, "=;");
                    if (!v20 || !((i = (char [3])(v20 - v19), v10 = (char [3])(v20 - v19), v20 != v19 && v20[0] != 59)))
                    {
LABEL_103568cc:
                        return sub_10351225();
                    }
                    v9 = 1;
                    for (v22 = &g_103947ac; (sub_1035fc2a(*((int *)v22), v19, i) || v10 != sub_10352f20(*((int *)v22))) && (v9 += 1, v22 += 12, v22 + 12 <= &g_103947dc); i = v10);
                    v23 = &v20[1];
                    v24 = sub_10355690(v23, ";");
                    if (!v24 && v23[0] != 59)
                        goto LABEL_103568cc;
                    if (v9 <= 5)
                    {
                        if (sub_1035f222(v12, 131, v23, v24))
                        {
                            v4 = 0;
                            v3 = 0;
                            v2 = 0;
                            v1 = 0;
                            v0 = 0;
                            sub_103534f6();
                        }
                        v12[v24] = 0;
                        if (sub_1035647f(v12, v25, v9))
                            iter += 1;
                    }
                    v26 = &v23[v24];
                } while (v26[0] && (v19 = v26 + 1, v19[0]));
                if (!iter)
                    return sub_10351225();
            }
            else
            {
                v4 = 0;
                if (!sub_103562ab(a0, v12, 131, NULL, NULL))
                    return sub_10351225();
                v27 = &a1->field_48;
                do
                {
                    if (v17)
                    {
                        if (sub_10359ed0(v12, *((int *)&v27->padding_0[0])))
                        {
                            if (!sub_1035647f(v12, v25, v17))
                                v10 = 0;
                            else
                                iter += 1;
                        }
                        else
                        {
                            iter += 1;
                        }
                    }
                } while ((v17 += 1, v27 += 16, v17 <= 5));
                if (!v10 && !iter)
                    goto LABEL_10356931;
            }
        }
        sub_1035613a();
    }
    else if (a0)
    {
        sub_1035647f(a0, a1, a2);
    }
LABEL_10356931:
    return sub_10351225();
}
```

## `sub_10356943` `0x10356943`

_329 bytes. (leaf/helper — see body)_

```c
extern char g_1038e660;
extern unsigned int g_1038e748;
extern int g_103a1020;
extern unsigned int g_103a3058;
extern void g_103a3824;

int sub_10356943(void)
{
    void* idx;  // esi
    unsigned int *v13;  // edi
    int v14;  // eax
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int *v6;  // [bp+0xfffe0]
    int v7;  // [bp+0xfffe4], Other Possible Types: unsigned int
    void* v8;  // [bp+0xfffe8]
    unsigned int v9;  // [bp+0x100000]
    unsigned int v10;  // [bp+0x10000c]
    unsigned int v11;  // [bp+0x100010]

    sub_1035b0cc(&g_103a1020, 20);
    v7 = 0;
    if (v10 > 5)
    {
        *((unsigned int *)sub_103575e0()) = 22;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        sub_103535f2();
    }
    else
    {
        idx = sub_10358da8();
        v8 = idx;
        sub_10355e09();
        *((unsigned int *)&idx[112]) = (int)idx[112] | 16;
        v9 = 0;
        v13 = sub_103574c2(216, 1);
        v6 = v13;
        if (v13)
        {
            sub_1035a599(12);
            v9 = 1;
            sub_10355da7();
            v9 = 0;
            sub_10356a71();
            v14 = sub_10356775(v11, v13, v10);
            v7 = v14;
            if (v14)
            {
                if (v11 && sub_10359ed0(v11, "C"))
                    g_103a3058 = 1;
                sub_1035a599(12);
                v9 = 2;
                sub_10355dcb();
                sub_10355d1b(v13);
                if (!((char)idx[112] & 2) && !(g_1038e660 & 1))
                {
                    sub_10355dcb();
                    sub_10350b50(&g_103a3824, g_1038e748 + 12, 24);
                    sub_10355e7f();
                }
                v9 = 0;
                sub_10356a7d();
            }
            else
            {
                sub_10355d1b(v13);
                sub_10355b55(v13);
            }
        }
        v9 = 4294967294;
        sub_10356aae();
    }
    return sub_1035b111();
}
```

## `sub_10356a69` `0x10356a69`

_8 bytes. (leaf/helper — see body)_

```c
void sub_10356a69(void)
{
    sub_10356a71();
    return;
}
```

## `sub_10356a71` `0x10356a71`

_9 bytes. (leaf/helper — see body)_

```c
void sub_10356a71(void)
{
    sub_1035a4c1(12);
    return;
}
```

## `sub_10356a7a` `0x10356a7a`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10356a7a(void)
{
    sub_10356a7d();
    return;
}
```

## `sub_10356a7d` `0x10356a7d`

_9 bytes. (leaf/helper — see body)_

```c
void sub_10356a7d(void)
{
    sub_1035a4c1(12);
    return;
}
```

## `sub_10356a86` `0x10356a86`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10356a86(void)
{
}
```

## `sub_10356aab` `0x10356aab`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10356aab(void)
{
    sub_10356aae();
    return;
}
```

## `sub_10356aae` `0x10356aae`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[112];
    unsigned int field_70;
} struct_0;

void sub_10356aae(void)
{
    struct_0 *idx;  // esi

    idx->field_70 = idx->field_70 & 4294967279;
    return;
}
```

## `sub_10356ab3` `0x10356ab3`

_930 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    char padding_0[4];
    unsigned int field_4;
    char padding_8[12];
    unsigned int field_14;
} struct_2;

typedef struct struct_3 {
    char field_0[4];
} struct_3;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b040;
extern struct_0 *g_1038b07c;
extern struct_0 *g_1038b104;
extern struct_0 *g_1038b228;
extern struct_0 *g_1038b22c;
extern unsigned int g_1038e180;
extern char g_1039487c;
extern unsigned int g_103a305c;

int sub_10356ab3(struct_2 **a0, unsigned int a1, unsigned int a2, unsigned int a3, char *a4, int a5, int a6, unsigned int a7, unsigned int a8, unsigned int a9)
{
    unsigned int v20;  // ebx
    unsigned int v21;  // esi
    unsigned int v30;  // eax
    unsigned int *iter;  // eax
    unsigned int v32;  // eax
    struct_3 **v33;  // esi
    struct_3 **node;  // eax
    unsigned int v35;  // eax
    unsigned int v36;  // eax
    unsigned int *v37;  // edi
    unsigned int *iter1;  // eax
    unsigned int v22;  // edi
    char *v23;  // eax
    int v24;  // ecx
    char *v25;  // eax
    int v26;  // ecx
    char *v27;  // eax
    int v28;  // eax
    unsigned int v29;  // edi
    int v0;  // [bp-0xac], Other Possible Types: unsigned int
    unsigned int v1;  // [bp-0xa8]
    unsigned int v2;  // [bp-0xa4]
    unsigned int v3;  // [bp-0xa0]
    unsigned int v4;  // [bp-0x88]
    unsigned int v5;  // [bp-0x84]
    unsigned int *v6;  // [bp-0x7c]
    int v7;  // [bp-0x70], Other Possible Types: unsigned int
    unsigned int v8;  // [bp-0x58]
    unsigned int v9;  // [bp-0x54]
    unsigned int v10;  // [bp-0x4c]
    unsigned int v11;  // [bp-0x24]
    unsigned int v12;  // [bp-0x20]
    unsigned int v13;  // [bp-0x1c]
    unsigned int v14;  // [bp-0x18]
    int v15;  // [bp-0x14]
    unsigned int *v16;  // [bp-0x10], Other Possible Types: unsigned int
    unsigned int v17;  // [bp-0xc]
    unsigned int v18;  // [bp-0x8]
    char v19;  // [bp-0x4]

    v18 = g_1038e180 ^ &v19;
    v13 = v20;
    v12 = v21;
    v11 = v22;
    if (!g_103a305c)
    {
        if (g_1038b22c(0, 0x100, &g_1039487c, 1, 0, 0))
        {
            g_103a305c = 1;
        }
        else if (g_1038b07c() == 120)
        {
            g_103a305c = 2;
        }
    }
    if (a5 > 0)
    {
        v23 = a4;
        v24 = a5;
        do
        {
            v25 = v23;
            v26 = v24 - 1;
            if (!*(v25))
                goto LABEL_10356b22;
        } while ((v27 = v25 + 1, v23 = v25 + 1, v24 = v26, v24));
        v26 = -1;
LABEL_10356b22:
        v28 = a5 - v26 - 1;
        if (v28 < a5)
            v28 += 1;
        a5 = v28;
    }
    if (!(g_103a305c != 2 && g_103a305c))
    {
        v16 = 0;
        v15 = 0;
        if (!a2)
            a2 = *(a0)->field_14;
        if (!a8)
            a8 = *(a0)->field_4;
        v14 = sub_1035fd30(a2);
        if (v14 != 4294967295)
        {
            if (v14 == a8)
            {
                g_1038b228(a2, a3, a4, a5, a6, a7);
                goto LABEL_10356e20;
            }
            v35 = sub_1035fd77(a8, v14, a4, &a5, 0, 0);
            v16 = v35;
            if (v35)
            {
                v10 = v35;
                v9 = a2;
                v17 = g_1038b228(a2, a3, v35, a5, 0, 0);
                if (!v17)
                {
LABEL_10356d62:
                }
                else
                {
                    if (v17 > 0 && v17 <= 0xffffffe0)
                    {
                        v36 = v17 + 8;
                        if (v36 <= 0x400)
                        {
                            sub_1035de90();
                            if (!&v9)
                                goto LABEL_10356d62;
                            v9 = 0xcccc;
                            v37 = &v10;
                        }
                        else
                        {
                            iter1 = sub_10355a15(v36);
                            if (iter1)
                            {
                                *(iter1) = 0xdddd;
                                iter1 += 2;
                            }
                            v37 = iter1;
                        }
                    }
                    else
                    {
                        v37 = NULL;
                    }
                    if (!v37)
                        goto LABEL_10356d62;
                    sub_10350ad0(v37, 0, v17);
                    v17 = g_1038b228(a2, a3, v16, a5, v37, v17);
                    if (v17)
                        v15 = sub_1035fd77(v14, a8, v37, &v17, a6, a7);
                    sub_103548d8(v37);
                }
LABEL_10356e20:
                if (v16)
                {
                    v7 = v16;
                    sub_1035345e();
                }
                if (v15 && a6 != v15)
                {
                    v7 = v15;
                    sub_1035345e();
                }
            }
        }
    }
    else if (g_103a305c == 1)
    {
        v17 = 0;
        if (!a8)
            a8 = *(a0)->field_4;
        v9 = a8;
        v29 = g_1038b104(a8, (a9) * 8 + 1, a4, a5, 0, 0);
        if (v29)
        {
            if (v29 > 0 && !((v8 = 0xffffffe0, 0xffffffe0 / v29 < 2)))
            {
                v30 = v29 * 2 + 8;
                if (v30 <= 0x400)
                {
                    sub_1035de90();
                    iter = &v9;
                    if (!&v9)
                        goto LABEL_10356bcd;
                    v9 = 0xcccc;
                    goto LABEL_10356bca;
                }
                else
                {
                    iter = sub_10355a15(v30);
                    if (iter)
                    {
                        *(iter) = 0xdddd;
LABEL_10356bca:
                        iter += 2;
                    }
                }
LABEL_10356bcd:
                v16 = iter;
            }
            else
            {
                v16 = NULL;
            }
            if (v16)
            {
                if (g_1038b104(a8, 1, a4, a5, v16, v29))
                {
                    v6 = v16;
                    v5 = a2;
                    v17 = g_1038b22c(a2, a3, v16, v29, 0, 0);
                    if (v17)
                    {
                        if (!((unsigned short)a3 & 0x400))
                        {
                            if (v17 > 0 && !((v4 = 0xffffffe0, 0xffffffe0 / v17 < 2)))
                            {
                                v32 = v17 * 2 + 8;
                                if (v32 <= 0x400)
                                {
                                    sub_1035de90();
                                    if (!&v5)
                                        goto LABEL_10356cd9;
                                    v5 = 0xcccc;
                                    v33 = &v6;
                                }
                                else
                                {
                                    node = sub_10355a15(v32);
                                    if (node)
                                    {
                                        *(node) = 0xdddd;
                                        node += 2;
                                    }
                                    v33 = node;
                                }
                            }
                            else
                            {
                                v33 = NULL;
                            }
                            if (v33)
                            {
                                if (g_1038b22c(a2, a3, v16, v29, v33, v17))
                                {
                                    v3 = 0;
                                    v2 = 0;
                                    if (!a7)
                                    {
                                        v1 = 0;
                                        v0 = 0;
                                    }
                                    else
                                    {
                                        v1 = a7;
                                        v0 = a6;
                                    }
                                    v17 = g_1038b040(a8, 0, v33, v17);
                                }
                                sub_103548d8(v33);
                            }
                        }
                        else if (a7 && v17 <= a7)
                        {
                            g_1038b22c(a2, a3, v16, v29, a6, a7);
                        }
                    }
                }
LABEL_10356cd9:
                sub_103548d8(v16);
            }
        }
    }
    return sub_10351225();
}
```

## `sub_10356e55` `0x10356e55`

_67 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

int sub_10356e55(unsigned int *a0, unsigned int a1, unsigned int a2, char *a3, int a4, int a5, unsigned int a6, unsigned int a7, unsigned int a8)
{
    unsigned int v3;  // edx
    int v4;  // eax
    struct_0 v0;  // [bp-0x14]
    struct_0 *idx;  // [bp-0xc]
    char v2;  // [bp-0x8]

    sub_103536a7(&v0, a0);
    v4 = sub_10356ab3(&v0, v3, a1, a2, a3, a4, a5, a6, a7, a8);
    if (v2)
        idx[8].field_8 = idx[8].field_8 & 4294967293;
    return v4;
}
```

## `sub_10356e98` `0x10356e98`

_41 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[108];
    struct struct_0 *field_6c;
    unsigned int field_70;
} struct_1;

typedef struct struct_0 {
    char padding_0[200];
    unsigned int field_c8;
} struct_0;

extern unsigned int g_1038e660;
extern char g_1038e748;

int sub_10356e98(void)
{
    struct_1 *v1;  // ecx
    struct_0 *v2;  // eax

    v1 = sub_10358da8();
    v2 = v1->field_6c;
    if (v2 != *((int *)&g_1038e748) && !(g_1038e660 & v1->field_70))
        v2 = sub_10355e09();
    return v2->field_c8;
}
```

## `sub_10356ec1` `0x10356ec1`

_79 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

typedef struct struct_1 {
    char padding_0[112];
    unsigned int field_70;
} struct_1;

unsigned int sub_10356ec1(int a0, unsigned int *a1)
{
    unsigned int v3;  // eax
    struct_0 v0;  // [bp-0x14]
    struct_1 *idx;  // [bp-0xc]
    char v2;  // [bp-0x8]

    sub_103536a7(&v0, a1);
    v3 = (*((int *)(v0 + 172)) <= 1 ? *((char *)(*((int *)(v0 + 200)) + a0 * 2)) & 1 : sub_1035b7ea(a0, 1, &v0));
    if (v2)
        idx->field_70 = idx->field_70 & 4294967293;
    return v3;
}
```

## `sub_10356f10` `0x10356f10`

_41 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e738;
extern unsigned int g_103a3058;

unsigned int sub_10356f10(int a0)
{
    if (g_103a3058)
        return sub_10356ec1(a0, NULL);
    return *((char *)(g_1038e738 + a0 * 2)) & 1;
}
```

## `sub_10356f39` `0x10356f39`

_79 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

typedef struct struct_1 {
    char padding_0[112];
    unsigned int field_70;
} struct_1;

unsigned int sub_10356f39(int a0, unsigned int *a1)
{
    unsigned int v3;  // eax
    struct_0 v0;  // [bp-0x14]
    struct_1 *idx;  // [bp-0xc]
    char v2;  // [bp-0x8]

    sub_103536a7(&v0, a1);
    v3 = (*((int *)(v0 + 172)) <= 1 ? *((char *)(*((int *)(v0 + 200)) + a0 * 2)) & 2 : sub_1035b7ea(a0, 2, &v0));
    if (v2)
        idx->field_70 = idx->field_70 & 4294967293;
    return v3;
}
```

## `sub_10356f88` `0x10356f88`

_41 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e738;
extern unsigned int g_103a3058;

unsigned int sub_10356f88(int a0)
{
    if (g_103a3058)
        return sub_10356f39(a0, NULL);
    return *((char *)(g_1038e738 + a0 * 2)) & 2;
}
```

