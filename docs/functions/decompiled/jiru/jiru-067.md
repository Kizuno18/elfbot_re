# elfbot.dll decompiled — jiru 0x10360e09..0x10365096

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10360e09` `0x10360e09`

_94 bytes. (leaf/helper — see body)_

```c
extern char g_103a3b70;
extern unsigned int g_103a3b80[4];

unsigned int sub_10360e09(int a0)
{
    unsigned int v6;  // esi
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    unsigned int v5;  // [bp-0x4]

    if (a0 == -2)
    {
        *((unsigned int *)sub_103575e0()) = 9;
        return 0;
    }
    v5 = v6;
    if (a0 >= 0 && a0 < *((int *)&g_103a3b70))
        return *((char *)(g_103a3b80[a0 >> 5] + (a0 & 31) * 56 + 4)) & 64;
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    *((unsigned int *)sub_103575e0()) = 9;
    sub_103535f2();
    return 0;
}
```

## `sub_10360e67` `0x10360e67`

_45 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

unsigned int sub_10360e67(struct_0 *a0)
{
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    if (a0)
        return a0->field_10;
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    *((unsigned int *)sub_103575e0()) = 22;
    sub_103535f2();
    return 4294967295;
}
```

## `sub_10360e94` `0x10360e94`

_22 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103a3a4c;

int sub_10360e94(void)
{
    return *((int *)&g_103a3a4c) == (g_1038e180 | 1);
}
```

## `sub_10360eaa` `0x10360eaa`

_351 bytes. (leaf/helper — see body)_

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

extern struct_0 *g_1038b040;
extern struct_0 *g_1038b07c;

unsigned int sub_10360eaa(unsigned int *a0, char *a1, unsigned int a2, unsigned short a3, unsigned int *a4)
{
    unsigned int v17;  // ebx
    unsigned int v18;  // esi
    unsigned int v19;  // edi
    unsigned int v21;  // eax
    unsigned int v22;  // eax
    unsigned int v0;  // [bp-0x54]
    unsigned int v1;  // [bp-0x50]
    unsigned int v2;  // [bp-0x4c]
    unsigned int v3;  // [bp-0x48]
    unsigned int v4;  // [bp-0x44]
    unsigned int v5;  // [bp-0x34]
    unsigned int v6;  // [bp-0x30]
    unsigned int v7;  // [bp-0x2c]
    unsigned int v8;  // [bp-0x28]
    unsigned int v9;  // [bp-0x24]
    unsigned int v10;  // [bp-0x20]
    unsigned int v11;  // [bp-0x1c]
    unsigned int v12;  // [bp-0x18]
    unsigned int v13[6];  // [bp-0x14]
    struct_1 *idx;  // [bp-0xc]
    char v15;  // [bp-0x8]
    unsigned int v16;  // [bp+0x8]

    v12 = v17;
    v11 = v18;
    v10 = v19;
    if (!a1 && a2 > NULL)
    {
        if (!a0)
            return 0;
        *(a0) = 0;
        return 0;
    }
    if (a0)
        *(a0) = 4294967295;
    if (a2 > 2147483647)
    {
        v9 = 22;
        v9 = 0;
        v8 = 0;
        v7 = 0;
        v6 = 0;
        v5 = 0;
        *((unsigned int *)sub_103575e0()) = 22;
        sub_103535f2();
        return 22;
    }
    sub_103536a7(&v13, a4);
    if (v13[5])
    {
        v16 = 0;
        v21 = g_1038b040(v13[1], 0, &/* unsupported instruction */, 1, a1, a2, 0, &a1);
        if (v21)
        {
            if (!v16)
            {
                if (a0)
                    *(a0) = v21;
LABEL_10360f93:
                if (!v15)
                    return 0;
                idx->field_70 = idx->field_70 & 4294967293;
                return 0;
            }
        }
        else
        {
            if (g_1038b07c() == 122)
            {
                if (a1 && a2 > NULL)
                    sub_10350ad0(a1, 0, a2);
LABEL_10360f5c:
                v4 = 0x22;
                v4 = 0;
                v3 = 0;
                v2 = 0;
                v1 = 0;
                v0 = 0;
                *((unsigned int *)sub_103575e0()) = 0x22;
                sub_103535f2();
                if (v15)
                {
                    idx->field_70 = idx->field_70 & 4294967293;
                    return 0x22;
                }
                return 0x22;
            }
        }
    }
    else if (a3 <= 0xff)
    {
        if (a1)
        {
            if (a2 <= 0)
                goto LABEL_10360f5c;
            *(a1) = a3;
        }
        if (a0)
        {
            *(a0) = 1;
            goto LABEL_10360f93;
        }
    }
    else if (a1 && a2 > NULL)
    {
        sub_10350ad0(a1, 0, a2);
    }
    *((unsigned int *)sub_103575e0()) = 42;
    v22 = *((int *)sub_103575e0());
    if (!v15)
        return v22;
    idx->field_70 = idx->field_70 & 4294967293;
    return v22;
}
```

## `sub_10361009` `0x10361009`

_27 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10361009(unsigned int *a0, char *a1, unsigned int a2, unsigned short a3)
{
    return sub_10360eaa(a0, a1, a2, a3, NULL);
}
```

## `sub_10361024` `0x10361024`

_74 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
    char field_c;
} struct_0;

int sub_10361024(void)
{
    struct_0 *v1;  // edi
    unsigned int *v3;  // eax
    int v0;  // [bp+0x4]

    if ((v1->field_c & 64) && !v1->field_8)
    {
        *(v3) = *(v3) + v0;
        return;
    }
    while (true)
    {
        do
        {
            if (v0 <= 0)
                return;
        } while ((v0 = (int)(v0 - 1), sub_1035931c(), *(v3) != 4294967295));
        if (*((int *)sub_103575e0()) != 42)
            break;
        sub_1035931c();
    }
    return;
}
```

## `sub_1036106e` `0x1036106e`

_2447 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    char field_c;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
    char padding_10[20];
    char field_24;
} struct_1;

typedef struct struct_2 {
    char padding_0[112];
    unsigned int field_70;
} struct_2;

extern unsigned int g_1038e180;
extern void* g_1038e470;
extern void* g_1038e474;
extern unsigned int g_1038ec98;
extern unsigned int g_1038eca0;
extern unsigned int g_1038eca4;
extern struct_1 g_1038f0d0;
extern char g_10396020;
extern char g_10396040;
extern struct_1 g_103a3b80;

int sub_1036106e(struct_0 *a0, char *a1, struct_0 *a2, void* a3)
{
    unsigned int v42;  // ebx
    char v43[3];  // ebx
    struct_1 *v52;  // eax
    char v53;  // 4105
    char v54;  // dl
    char v55[3];  // ebx
    unsigned int v56;  // eax
    unsigned int v57;  // eax
    unsigned int v58;  // eax
    unsigned int v59;  // eax
    unsigned int v60;  // eax
    char v61;  // al
    unsigned int v44;  // esi
    unsigned int v62;  // eax
    unsigned int v63;  // eax
    unsigned int v64;  // eax
    char v66;  // dl
    unsigned int v67;  // eax
    unsigned int v68;  // eax
    unsigned int v69;  // eax
    void* v70;  // eax
    void* v71;  // ebx, Other Possible Types: unsigned int
    unsigned int v45;  // edi
    void* v72;  // esi
    void* v73;  // eax
    void* v74;  // edi
    void* v78;  // ecx
    void* iter;  // edi
    void* iter1;  // ecx
    void* v81;  // eax
    void* v82;  // eax
    void* v84;  // eax
    void* v85;  // eax
    unsigned int v87;  // eax
    short v88;  // cx
    void* v89;  // edi
    unsigned int v47;  // eax
    unsigned int v90;  // eax
    unsigned int v91;  // edx
    unsigned int v92;  // eax
    unsigned int v94;  // edi
    unsigned int v95;  // eax
    void* iter2;  // esi
    int v97;  // ecx
    int v98;  // ecx
    unsigned int v48;  // eax
    unsigned int v99;  // edx
    short v100;  // ax
    int v101;  // ebx
    void* v102;  // esi
    void* v103;  // esi
    struct_1 *v49;  // eax
    unsigned int v50;  // eax
    unsigned int v51;  // eax
    unsigned int v0;  // [bp-0x2ac]
    unsigned int v1;  // [bp-0x2a0]
    unsigned int v2;  // [bp-0x29c]
    unsigned int v3;  // [bp-0x298]
    unsigned int v4;  // [bp-0x294]
    struct_0 *v5;  // [bp-0x28c]
    unsigned int v6;  // [bp-0x288]
    unsigned int v7;  // [bp-0x284]
    unsigned int v8;  // [bp-0x280]
    unsigned int v9;  // [bp-0x27c]
    unsigned int v10;  // [bp-0x278]
    unsigned int v11;  // [bp-0x274]
    unsigned int v12;  // [bp-0x270]
    void* v13;  // [bp-0x268], Other Possible Types: unsigned int
    unsigned int v14;  // [bp-0x264]
    unsigned int v15;  // [bp-0x260]
    void* v16;  // [bp-0x25c]
    struct_0 v17;  // [bp-0x258]
    struct_2 *idx;  // [bp-0x250]
    char v19;  // [bp-0x24c]
    char v20[3];  // [bp-0x248]
    unsigned int v21;  // [bp-0x244]
    unsigned int v22;  // [bp-0x240]
    void* v23;  // [bp-0x23c]
    unsigned int v24;  // [bp-0x238]
    char v25;  // [bp-0x234]
    char v26;  // [bp-0x233]
    int v27;  // [bp-0x230]
    struct_0 *v28;  // [bp-0x22c]
    void* v29;  // [bp-0x228]
    void* v30;  // [bp-0x224], Other Possible Types: unsigned long long
    void* node;  // [bp-0x220]
    void* v32;  // [bp-0x21c]
    char v33;  // [bp-0x215]
    unsigned int v34;  // [bp-0x214]
    char v35[20];  // [bp-0x210]
    char v36[20];  // [bp-0x210]
    char v37[20];  // [bp-0x210]
    char v38;  // [bp-0x1fc]
    char v40[20];  // [bp-0x12]
    unsigned int v41;  // [bp-0x8]

    v41 = g_1038e180 ^ &v38;
    v8 = v42;
    v43 = a1;
    v7 = v44;
    v6 = v45;
    iter = a3;
    v28 = a0;
    v15 = 0;
    v34 = 0;
    v23 = NULL;
    v32 = NULL;
    v24 = 0;
    v14 = 0;
    v22 = 0;
    sub_103536a7(&v17, a2);
    if (!v28)
    {
LABEL_103610ce:
        v71 = 0;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        *((unsigned int *)sub_103575e0()) = 22;
        v1 = 0;
LABEL_103610de:
        sub_103535f2();
        if (v19)
            idx->field_70 = idx->field_70 & 4294967293;
    }
    else
    {
        if (!(v28->field_c & 64))
        {
            if (sub_10360e67(v28) != 0xffffffff && sub_10360e67(v28) != 4294967294)
            {
                v47 = sub_10360e67(v28);
                v48 = sub_10360e67(v28);
                v49 = (v48 & 31) * 56 + (&g_103a3b80.field_0)[v47 >> 5];
            }
            else
            {
                v49 = &g_1038f0d0.field_0;
            }
            if (!(v49->field_24 & 127))
            {
                v5 = v28;
                if (sub_10360e67(v5) != 0xffffffff && !((v5 = v28, sub_10360e67(v5) == 4294967294)))
                {
                    v50 = sub_10360e67(v28);
                    v51 = sub_10360e67(v28);
                    v52 = (v51 & 31) * 56 + (&g_103a3b80.field_0)[v50 >> 5];
                    v5 = v28;
                }
                else
                {
                    v52 = &g_1038f0d0.field_0;
                }
                a2 = v5;
                if (!(v52->field_24 & 128))
                    goto LABEL_103611ac;
                goto LABEL_103610ce;
            }
        }
LABEL_103611ac:
        if (!v43)
            goto LABEL_103610ce;
        v53 = v43[0];
        v54 = v53;
        v27 = 0;
        v30 = NULL;
        v21 = 0;
        v16 = NULL;
        v33 = v53;
        if (v53)
        {
            while (true)
            {
                iter = v29;
                v55 = &v43[1];
                v56 = 0;
                v20 = v55;
                if (v27 < NULL)
                    break;
                if (v54 - 32 <= 88)
                    v56 = *(&(&g_10396020)[v54]) & 15;
                v71 = 8;
                v21 = (&g_10396040)[9 * v56 + v21] >> 4;
                if (v21 != 8)
                {
                    v71 = 7;
                    switch (v21)
                    {
                    case 1:
                        v32 = 0xffffffff;
                        v12 = 0;
                        v14 = 0;
                        v23 = NULL;
                        v24 = 0;
                        v34 = 0;
                        v22 = 0;
                        goto LABEL_10361997;
                    case 2:
                        v57 = v54;
                        v58 = v57 - 32;
                        if (v57 != 32)
                        {
                            v59 = v58 - 3;
                            if (v58 == 3)
                            {
                                v34 |= 128;
                                goto LABEL_10361997;
                            }
                            else if (v59 != 8)
                            {
                                v60 = v59 - 9;
                                if (v60 == 1)
                                {
                                    v34 |= 4;
                                    goto LABEL_10361997;
                                }
                                else if (v60 == 4)
                                {
                                    v34 |= 8;
                                    goto LABEL_10361997;
                                }
                            }
                            else
                            {
                                v34 |= 1;
                                goto LABEL_10361997;
                            }
                        }
                        else
                        {
                            v34 |= 2;
                            goto LABEL_10361997;
                        }
                    case 3:
                        if (v54 == 42)
                        {
                            iter += 4;
                            v23 = (int)iter[4];
                            if ((int)iter[4] < NULL)
                            {
                                v34 |= 4;
                                v23 = -(v23);
                                goto LABEL_10361997;
                            }
                        }
                        else
                        {
                            v23 = v23 * 10 + v54 - 48;
                            goto LABEL_10361997;
                        }
                    case 4:
                        v32 = NULL;
                        goto LABEL_10361997;
                    case 5:
                        if (v54 == 42)
                        {
                            iter += 4;
                            v32 = (int)iter[4];
                            if ((int)iter[4] < NULL)
                            {
                                v32 = 0xffffffff;
                                goto LABEL_10361997;
                            }
                        }
                        else
                        {
                            v32 = v32 * 10 + v54 - 48;
                            goto LABEL_10361997;
                        }
                    case 7:
                        v62 = v54;
                        if (v62 > 100)
                        {
                            if (v62 > 112)
                            {
                                if (v62 != 115)
                                {
                                    v87 = v62 - 116;
                                    if (v87 != 1)
                                    {
                                        if (v87 != 4)
                                            break;
                                        v15 = 39;
LABEL_1036172c:
                                        v30 = 16;
                                        if (((char)v34 & 128))
                                        {
                                            v25 = 48;
                                            v26 = (char)v15 + 81;
                                            v24 = 2;
                                        }
LABEL_10361608:
                                        v88 = v34;
                                        if (v88 < 0 || (v88 & 0x1000))
                                        {
                                            v89 = iter + 8;
                                            v90 = (int)v89[8];
                                            v91 = (int)v89[4];
                                        }
                                        else
                                        {
                                            v89 = iter + 4;
                                            if (((char)v88 & 32))
                                            {
                                                iter = v89;
                                                v90 = (!((char)v88 & 64) ? (short)v89[4] : (short)v89[4]);
                                                v91 = v90 >> 31;
                                                goto LABEL_1036178d;
                                            }
                                            else
                                            {
                                                v90 = (int)v89[4];
                                                v91 = (!((char)v88 & 64) ? 0 : v90 >> 31);
                                            }
                                        }
                                        iter = v89;
LABEL_1036178d:
                                        v92 = v90;
                                        if (((char)v88 & 64))
                                        {
                                            v92 = v90;
                                            if (v91 <= NULL && (v91 < NULL || (v92 = v90, v92 < 0)))
                                            {
                                                v91 = -(v91 + (0 < v90));
                                                v34 |= 0x100;
                                                v92 = -(v90);
                                            }
                                        }
                                        v94 = v92;
                                        if (!((unsigned short)v34 & 0x9000))
                                            v91 = 0;
                                        if (v32 < NULL)
                                        {
                                            v32 = 0x1;
                                        }
                                        else
                                        {
                                            v34 &= 4294967287;
                                            if (v32 > 0x200)
                                                v32 = 0x200;
                                        }
                                        v95 = v94;
                                        if (!v95 && !v91)
                                            v24 &= v95 | v91;
                                        iter2 = &v40[1];
                                        while (true)
                                        {
                                            v32 -= 1;
                                            if (v32 <= NULL && !v94 && !v91)
                                                break;
                                            v98 = v97 + 48;
                                            v13 = v91;
                                            v94 = sub_1035b8a0(v94, v91, v30, v30 >> 31, a2);
                                            v91 = v99;
                                            if (v98 > 57)
                                                v98 += v15;
                                            *((char *)iter2) = v98;
                                            iter2 -= 1;
                                        }
                                        v30 = &v40[1] - iter2;
                                        node = iter2 + 1;
                                        if (!((unsigned short)v34 & 0x200) || v30 && *((char *)node) == 48)
                                            break;
                                        node -= 1;
                                        *((char *)node) = 48;
                                        v70 = v30 + 1;
LABEL_1036187c:
                                        v30 = v70;
                                        if (v14)
                                        {
LABEL_10361984:
                                            if (v16)
                                            {
                                                v71 = v16;
                                                sub_1035345e();
                                                v16 = NULL;
                                                goto LABEL_10361997;
                                            }
                                        }
                                        v100 = v34;
                                        if (((char)v100 & 64))
                                        {
                                            if ((v100 & 0x100))
                                            {
                                                v25 = 45;
                                            }
                                            else if (((char)v100 & 1))
                                            {
                                                v25 = 43;
                                            }
                                            else
                                            {
                                                if (!((char)v100 & 2))
                                                    goto LABEL_103618b5;
                                                v25 = 32;
                                            }
                                            v24 = 1;
                                        }
LABEL_103618b5:
                                        v101 = v23 - v30 - v24;
                                        if (!((char)v34 & 12))
                                            sub_1035934f(32, v101, v28);
                                        sub_10361024(v24);
                                        if (((char)v34 & 8) && !((char)v34 & 4))
                                            sub_1035934f(48, v101, v28);
                                        if (v22 && v30 > NULL)
                                        {
                                            v13 = v30;
                                            do
                                            {
                                                v102 = node;
                                                v13 -= 1;
                                                v103 = v102 + 2;
                                                if (sub_10361009(&v11, &v40[2], 6, *((short *)v102)) || !v11)
                                                {
                                                    v27 = -1;
                                                    break;
                                                }
                                            } while ((sub_10361024(v11), node = v103, v13));
                                        }
                                        else
                                        {
                                            sub_10361024(v30);
                                        }
                                        if (v27 >= NULL && ((char)v34 & 4))
                                        {
                                            sub_1035934f(32, v101, v28);
                                            goto LABEL_10361984;
                                        }
                                    }
LABEL_10361601:
                                    v30 = 10;
                                    goto LABEL_10361608;
                                }
LABEL_10361489:
                                v78 = v32;
                                if (v78 == 0xffffffff)
                                    v78 = 0x7fffffff;
                                iter1 = v78;
                                iter += 4;
                                node = (int)iter[4];
                                if (((unsigned short)v34 & 2064))
                                {
                                    if (!node)
                                        node = g_1038e474;
                                    v22 = 1;
                                    v81 = node;
                                    while (true)
                                    {
                                        v82 = v81;
                                        if (!iter1 || !((iter1 -= 1, *((short *)v82))))
                                            break;
                                        v81 = v82 + 2;
                                    }
                                    v70 = v82 - node >> 1;
                                    goto LABEL_1036187c;
                                }
                                else
                                {
                                    if (!node)
                                        node = g_1038e470;
                                    v84 = node;
                                    while (true)
                                    {
                                        v85 = v84;
                                        if (!iter1 || !((iter1 -= 1, *((char *)v85))))
                                            break;
                                        v84 = v85 + 1;
                                    }
                                    v70 = v85 - node;
                                    goto LABEL_1036187c;
                                }
                            }
                            if (v62 == 112)
                            {
                                v32 = 0x8;
LABEL_10361706:
                                v15 = 7;
                                goto LABEL_1036172c;
                            }
                            if (v62 < 101)
                                break;
                            v66 = v54;
                            if (v62 > 103)
                            {
                                if (v62 != 105)
                                {
                                    if (v62 == 110)
                                    {
                                        iter += 4;
                                        if (!sub_10360e94())
                                            goto LABEL_103619ad;
                                        if (((char)v34 & 32))
                                            *((unsigned short *)*((int *)iter)) = v27;
                                        else
                                            *((int *)*((int *)iter)) = v27;
                                        v14 = 1;
                                        goto LABEL_10361984;
                                    }
                                    if (v62 != 111)
                                        break;
                                    v30 = 8;
                                    if (((char)v34 & 128))
                                    {
                                        v34 |= 0x200;
                                        goto LABEL_10361608;
                                    }
                                }
LABEL_103615fd:
                                v34 |= 64;
                                goto LABEL_10361601;
                            }
LABEL_10361441:
                            v34 |= 64;
                            v71 = v35;
                            node = v35;
                            v13 = 0x200;
                            if (v32 < NULL)
                            {
                                v32 = 0x6;
                            }
                            else if (v32)
                            {
                                if (v32 > 0x200)
                                    v32 = 0x200;
                                if (v32 > 0xa3)
                                {
                                    v72 = v32 + 349;
                                    v73 = sub_10357482(v72);
                                    v66 = v33;
                                    v16 = v73;
                                    v71 = 8;
                                    if (v73)
                                    {
                                        node = v73;
                                        v13 = v72;
                                        v71 = v73;
                                    }
                                    else
                                    {
                                        v32 = 0xa3;
                                    }
                                }
                            }
                            else if (v66 == 103)
                            {
                                v32 = 0x1;
                            }
                            v74 = iter + 8;
                            v9 = (int)v74[8];
                            v10 = (int)v74[4];
                            iter = v74;
                            v0 = g_1038ec98;
                            sub_10358b8c()(&v9, v71, v13, v66, v32, v12, &v17);
                            if (((char)v34 & 128) && !v32)
                            {
                                v3 = g_1038eca4;
                                sub_10358b8c()(v71, &v17);
                            }
                            if (v33 == 103 && !((char)v34 & 128))
                            {
                                v3 = g_1038eca0;
                                sub_10358b8c()(v71, &v17);
                            }
                            if (*((char *)v71) == 45)
                            {
                                v34 |= 0x100;
                                v71 += 1;
                                node = v71;
                            }
                            goto LABEL_10361577;
                        }
                        if (v62 == 100)
                            goto LABEL_103615fd;
                        if (v62 <= 83)
                        {
                            if (v62 == 83 && !((unsigned short)v34 & 2096))
                            {
                                v34 |= 0x800;
                                goto LABEL_10361489;
                            }
                            if (v62 != 65)
                            {
                                v63 = v62 - 66;
                                if (v63 != 1)
                                {
                                    v64 = v63 - 2;
                                    if (v64 != 1 && v64 != 3)
                                        break;
                                }
                                else if (!((unsigned short)v34 & 2096))
                                {
                                    v34 |= 0x800;
                                    goto LABEL_103614e6;
                                }
                            }
                            v12 = 1;
                            v33 = v54 + 32;
                            v66 = v54 + 32;
                            goto LABEL_10361441;
                        }
                        else
                        {
                            if (v62 == 88)
                                goto LABEL_10361706;
                            v67 = v62 - 89;
                            v68 = v67 - 1;
                            if (v67 == 1)
                            {
                                v69 = *((int *)iter);
                                iter += 4;
                                if (v69 && *((int *)(v69 + 4)))
                                {
                                    v70 = *((short *)v69);
                                    node = *((int *)(v69 + 4));
                                    if (((unsigned short)v34 & 0x800))
                                    {
                                        v70 = &v70;
                                        v22 = 1;
                                        goto LABEL_1036187c;
                                    }
                                    else
                                    {
                                        v22 = 0;
                                        goto LABEL_1036187c;
                                    }
                                }
                                else
                                {
                                    node = g_1038e470;
                                    v71 = g_1038e470;
                                }
LABEL_10361577:
                                v70 = sub_10352f20(v71);
                                goto LABEL_1036187c;
                            }
                            v66 = v54;
                            if (v68 == 7)
                                goto LABEL_10361441;
                            if (v68 != 9)
                                break;
LABEL_103614e6:
                            iter += 4;
                            if (((unsigned short)v34 & 2064))
                            {
                                v36 = v35;
                                if (sub_10361009(&v30, v36, 0x200, (short)iter[4]))
                                {
                                    v14 = 1;
                                    v36 = v35;
                                }
                            }
                            else
                            {
                                v37 = (char[20])_INSERT(v35, 0, (char)iter[4]);
                                v30 = 0x1;
                                v36 = v37;
                            }
                            node = v36;
                            break;
                        }
                    case 6:
                        if (v54 != 73)
                        {
                            if (v54 == 104)
                            {
                                v34 |= 32;
                                goto LABEL_10361997;
                            }
                            else if (v54 != 108)
                            {
                                if (v54 == 0x77)
                                {
                                    v34 |= 0x800;
                                    goto LABEL_10361997;
                                }
                            }
                            else
                            {
                                if (v55[0] == 108)
                                {
                                    v34 |= 0x1000;
                                    v20 = &v55[1];
                                    goto LABEL_10361997;
                                }
                                else
                                {
                                    v34 |= 16;
                                    goto LABEL_10361997;
                                }
                            }
                        }
                        v61 = v55[0];
                        if (v55[0] == 54 && v55[1] == 52)
                        {
                            v34 |= 0x8000;
                            v20 = &v55[2];
                            goto LABEL_10361997;
                        }
                        if (v61 == 0x33 && v55[1] == 50)
                        {
                            v34 &= 4294934527;
                            v20 = &v55[2];
                            goto LABEL_10361997;
                        }
                        if (v61 == 100 || v61 == 105 || v61 == 111 || v61 == 117 || v61 == 120 || v61 == 88)
                            goto LABEL_10361997;
                        v21 = 0;
                    case 0:
                        v22 = 0;
                        if (sub_1035de48(v54, &v17) && !((sub_1035931c(), v20 = v55 + 1, v55[0])))
                            goto LABEL_103619ad;
                        sub_1035931c();
                        goto LABEL_10361997;
                    default:
LABEL_10361997:
                        iter = v29;
                        v43 = v20;
                        v54 = v43[0];
                        v33 = v54;
                        if (!v54)
                            goto LABEL_103619c4;
                        continue;
                    }
                }
                else
                {
LABEL_103619ad:
                    *((unsigned int *)sub_103575e0()) = 22;
                    v71 = 0;
                    v4 = 0;
                    v3 = 0;
                    v2 = 0;
                    v1 = 0;
                    goto LABEL_103610de;
                }
            }
LABEL_103619c4:
            if (!v21 || v21 == 7)
                goto LABEL_103619d5;
            goto LABEL_103610ce;
        }
        else
        {
LABEL_103619d5:
            if (v19)
                idx->field_70 = idx->field_70 & 4294967293;
        }
    }
    return sub_10351225();
}
```

## `sub_10361a1e` `0x10361a1e`

_445 bytes. refs "USER32.DLL", "MessageBoxA", "GetActiveWindow"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b078;
extern struct_0 *g_1038b080;
extern unsigned int g_103a3a8c;
extern unsigned int g_103a3a90;
extern unsigned int g_103a3a94;
extern unsigned int g_103a3a98;
extern unsigned int g_103a3a9c;

unsigned int sub_10361a1e(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v22;  // ebx
    unsigned int v23;  // esi
    unsigned int *v32;  // eax
    unsigned int *v33;  // eax
    unsigned int v24;  // edi
    unsigned int v25;  // edi
    unsigned int v26;  // eax
    unsigned int *v27;  // eax
    unsigned int *v28;  // esi
    unsigned int *v29;  // edi
    unsigned int v30;  // eax
    unsigned int *v31;  // eax
    unsigned int v0;  // [bp-0x74]
    unsigned int v1;  // [bp-0x70]
    unsigned int v2;  // [bp-0x6c]
    unsigned int v3;  // [bp-0x68]
    unsigned int v4;  // [bp-0x64]
    unsigned int v5;  // [bp-0x60]
    unsigned int v6;  // [bp-0x5c]
    unsigned int v7;  // [bp-0x58]
    unsigned int v8;  // [bp-0x54]
    unsigned int v9;  // [bp-0x50]
    unsigned int v10;  // [bp-0x48]
    unsigned int v11;  // [bp-0x40]
    unsigned int v12;  // [bp-0x30]
    unsigned int v13;  // [bp-0x2c]
    unsigned int v14;  // [bp-0x28]
    char v15;  // [bp-0x24]
    char v16;  // [bp-0x1c]
    char v17;  // [bp-0x18]
    unsigned int v18;  // [bp-0x14]
    unsigned int v19;  // [bp-0x10]
    unsigned int v20;  // [bp-0xc]
    unsigned int v21;  // [bp-0x8]

    v14 = v22;
    v13 = v23;
    v12 = v24;
    v20 = sub_10358b83();
    v21 = 0;
    v19 = 0;
    v18 = 0;
    if (!g_103a3a8c)
    {
        v25 = g_1038b080("USER32.DLL");
        if (!v25)
            return 0;
        v26 = g_1038b078(v25, "MessageBoxA");
        if (!v26)
            return 0;
        v11 = v26;
        g_103a3a8c = sub_10358b15();
        v10 = g_1038b078(v25, "GetActiveWindow");
        g_103a3a90 = sub_10358b15();
        v9 = g_1038b078(v25, "GetLastActivePopup");
        g_103a3a94 = sub_10358b15();
        if (sub_10353d3b(&v19))
        {
            v9 = 0;
            v8 = 0;
            v7 = 0;
            v6 = 0;
            v5 = 0;
            sub_103534f6();
        }
        if (v19 == 2)
        {
            v7 = g_1038b078(v25, "GetUserObjectInformationA");
            g_103a3a9c = sub_10358b15();
            if (g_103a3a9c)
            {
                v5 = g_1038b078(v25, "GetProcessWindowStation");
                g_103a3a98 = sub_10358b15();
            }
        }
    }
    if (g_103a3a98 != v20 && g_103a3a9c != v20)
    {
        v9 = g_103a3a98;
        v27 = sub_10358b8c();
        v8 = g_103a3a9c;
        v28 = v27;
        v29 = sub_10358b8c();
        if (!v28 || !v29 || (v30 = v28(), v30 && v29(v30, 1, &v15, 12, &v17) && (v16 & 1)))
            goto LABEL_10361b79;
        if (sub_10353d72(&v18))
        {
            v4 = 0;
            v3 = 0;
            v2 = 0;
            v1 = 0;
            v0 = 0;
            sub_103534f6();
        }
        a2 = (v18 < 4 ? a2 | 0x40000 : a2 | 0x200000);
    }
    else
    {
LABEL_10361b79:
        if (g_103a3a90 != v20)
        {
            v4 = g_103a3a90;
            v31 = sub_10358b8c();
            if (v31)
            {
                v21 = v31();
                if (v21 && g_103a3a94 != v20)
                {
                    v4 = g_103a3a94;
                    v32 = sub_10358b8c();
                    if (v32)
                        v21 = v32(v21);
                }
            }
        }
    }
    v3 = g_103a3a8c;
    v33 = sub_10358b8c();
    if (!v33)
        return 0;
    return v33(v21, a0, a1, a2);
}
```

## `sub_10361bdb` `0x10361bdb`

_70 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a3050;

unsigned int sub_10361bdb(int a0)
{
    unsigned int v5;  // eax
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    if (a0 >= 0)
    {
        if (a0 <= 2)
        {
            v5 = g_103a3050;
            g_103a3050 = a0;
            return v5;
        }
        else if (a0 == 3)
        {
            return g_103a3050;
        }
    }
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    *((unsigned int *)sub_103575e0()) = 22;
    sub_103535f2();
    return 4294967295;
}
```

## `sub_10361c21` `0x10361c21`

_315 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    char padding_0[4];
    unsigned int field_4;
} struct_2;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b07c;
extern struct_0 *g_1038b104;
extern struct_0 *g_1038b198;
extern struct_0 *g_1038b1e4;
extern unsigned int g_1038e180;
extern unsigned int g_103a3aa0;

int sub_10361c21(unsigned int a0, unsigned int a1, struct_2 **a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7)
{
    unsigned int v12;  // eax
    unsigned int v13;  // ebx
    unsigned int v14;  // esi
    unsigned int v15;  // edi
    unsigned int v16;  // ebx
    unsigned int v17;  // 4101
    unsigned int v18;  // eax
    unsigned int *v19;  // esi
    unsigned int *iter;  // eax
    unsigned int v0;  // [bp-0x50]
    unsigned int v1;  // [bp-0x4c]
    unsigned int v2;  // [bp-0x3c]
    unsigned int v3;  // [bp-0x38]
    unsigned int v4;  // [bp-0x30]
    unsigned int v5;  // [bp-0x2c]
    unsigned int v6;  // [bp-0x18]
    unsigned int v7;  // [bp-0x14]
    unsigned int v8;  // [bp-0x10]
    unsigned int v9;  // [bp-0xc]
    unsigned int v10;  // [bp-0x8]
    char v11;  // [bp-0x4]

    v10 = a0;
    v9 = a0;
    v10 = g_1038e180 ^ &v11;
    v12 = g_103a3aa0;
    v8 = v13;
    v7 = v14;
    v6 = v15;
    if (!v12)
    {
        if (g_1038b198(0, 1, 0, 0))
        {
            g_103a3aa0 = 1;
            g_1038b198(a3, a4, a5, a6);
            return sub_10351225();
        }
        if (g_1038b07c() == 120)
        {
            v5 = 2;
            v12 = 2;
            g_103a3aa0 = 2;
        }
        else
        {
            v12 = g_103a3aa0;
        }
    }
    if (v12 == 1)
    {
        g_1038b198(a3, a4, a5, a6);
        return sub_10351225();
    }
    if (v12 == 2 || !v12)
    {
        v9 = 0;
        if (!a7)
            a7 = *(a2)->field_4;
        v4 = 0;
        v3 = a3;
        v16 = g_1038b1e4(a3, a4, 0, 0);
        if (v16)
        {
            v17 = _ccall(14, 15, v16, 0, 0);
            if ((char)v17 || (v2 = 0xffffffe0, 0xffffffe0 / v16 < 1))
            {
                v19 = NULL;
                goto LABEL_10361d0c;
            }
            v18 = v16 + 8;
            if (v18 <= 0x400)
            {
                sub_1035de90();
                if (&v3)
                {
                    v3 = 0xcccc;
                    v19 = &v4;
LABEL_10361d0c:
                    if (v19)
                    {
                        if (g_1038b1e4(a3, a4, v19, v16))
                        {
                            if (!a6)
                            {
                                v1 = 0;
                                v0 = 0;
                            }
                            else
                            {
                                v1 = a6;
                                v0 = a5;
                            }
                            v9 = g_1038b104(a7, 1, v19, 4294967295);
                        }
                        sub_103548d8(v19);
                        return sub_10351225();
                    }
                }
            }
            else
            {
                iter = sub_10355a15(v18);
                if (iter)
                {
                    *(iter) = 0xdddd;
                    iter += 2;
                }
                v19 = iter;
                goto LABEL_10361d0c;
            }
        }
    }
    return sub_10351225();
}
```

## `sub_10361d5c` `0x10361d5c`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

int sub_10361d5c(unsigned int *a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5)
{
    unsigned int v3;  // ecx
    unsigned int v4;  // edx
    int v5;  // eax
    struct_0 v0;  // [bp-0x14]
    struct_0 *idx;  // [bp-0xc]
    char v2;  // [bp-0x8]

    sub_103536a7(&v0, a0);
    v5 = sub_10361c21(v3, v4, &v0, a1, a2, a3, a4, a5);
    if (v2)
        idx[8].field_8 = idx[8].field_8 & 4294967293;
    return v5;
}
```

## `sub_10361d97` `0x10361d97`

_317 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    char padding_0[4];
    unsigned int field_4;
} struct_2;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b040;
extern struct_0 *g_1038b07c;
extern struct_0 *g_1038b198;
extern struct_0 *g_1038b1e4;
extern unsigned int g_1038e180;
extern unsigned int g_103a3aa4;

int sub_10361d97(unsigned int a0, unsigned int a1, struct_2 **a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7)
{
    unsigned int v14;  // eax
    unsigned int v15;  // ebx
    unsigned int v16;  // esi
    unsigned int v17;  // edi
    unsigned int v18;  // eax
    unsigned int *v19;  // edi
    unsigned int *iter;  // eax
    unsigned int v0;  // [bp-0x58]
    unsigned int v1;  // [bp-0x54]
    unsigned int v2;  // [bp-0x50]
    unsigned int v3;  // [bp-0x4c]
    unsigned int v4;  // [bp-0x3c]
    unsigned int v5;  // [bp-0x38]
    unsigned int v6;  // [bp-0x30]
    unsigned int v7;  // [bp-0x2c]
    unsigned int v8;  // [bp-0x18]
    unsigned int v9;  // [bp-0x14]
    unsigned int v10;  // [bp-0x10]
    unsigned int v11;  // [bp-0xc]
    unsigned int v12;  // [bp-0x8]
    char v13;  // [bp-0x4]

    v12 = a0;
    v11 = a0;
    v12 = g_1038e180 ^ &v13;
    v14 = g_103a3aa4;
    v10 = v15;
    v9 = v16;
    v8 = v17;
    if (!v14)
    {
        if (!g_1038b198(0, 1, 0, 0))
        {
            if (g_1038b07c() == 120)
            {
                v7 = 2;
                v14 = 2;
                g_103a3aa4 = 2;
                goto LABEL_10361de9;
            }
            else
            {
                v14 = g_103a3aa4;
                goto LABEL_10361de9;
            }
        }
        g_103a3aa4 = 1;
LABEL_10361dfe:
        if (!a7)
            a7 = *(a2)->field_4;
        v6 = 0;
        v5 = a3;
        v11 = g_1038b198(a3, a4, 0, 0);
        if (v11)
        {
            if (v11 <= 0 || (v4 = 0xffffffe0, 0xffffffe0 / v11 < 2))
            {
                v19 = NULL;
                goto LABEL_10361e71;
            }
            v18 = v11 * 2 + 8;
            if (v18 <= 0x400)
            {
                sub_1035de90();
                if (&v5)
                {
                    v5 = 0xcccc;
                    v19 = &v6;
LABEL_10361e71:
                    if (v19)
                    {
                        if (g_1038b198(a3, a4, v19, v11))
                        {
                            v3 = 0;
                            v2 = 0;
                            if (!a6)
                            {
                                v1 = 0;
                                v0 = 0;
                            }
                            else
                            {
                                v1 = a6;
                                v0 = a5;
                            }
                            g_1038b040(a7, 0, v19, 4294967295);
                        }
                        sub_103548d8(v19);
                        return sub_10351225();
                    }
                }
            }
            else
            {
                iter = sub_10355a15(v18);
                if (iter)
                {
                    *(iter) = 0xdddd;
                    iter += 2;
                }
                v19 = iter;
                goto LABEL_10361e71;
            }
        }
    }
    else
    {
LABEL_10361de9:
        if (v14 == 2 || !v14)
        {
            g_1038b1e4(a3, a4, a5, a6);
            return sub_10351225();
        }
        if (v14 == 1)
            goto LABEL_10361dfe;
    }
    return sub_10351225();
}
```

## `sub_10361ed4` `0x10361ed4`

_59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

int sub_10361ed4(unsigned int *a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5)
{
    unsigned int v3;  // ecx
    unsigned int v4;  // edx
    int v5;  // eax
    struct_0 v0;  // [bp-0x14]
    struct_0 *idx;  // [bp-0xc]
    char v2;  // [bp-0x8]

    sub_103536a7(&v0, a0);
    v5 = sub_10361d97(v3, v4, &v0, a1, a2, a3, a4, a5);
    if (v2)
        idx[8].field_8 = idx[8].field_8 & 4294967293;
    return v5;
}
```

## `sub_10361f0f` `0x10361f0f`

_166 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

extern unsigned int g_1038e180;

int sub_10361f0f(int a0, int a1, unsigned int *a2)
{
    unsigned int v12;  // ebx
    unsigned int v13;  // esi
    unsigned int v14;  // edi
    unsigned int v15;  // eax
    unsigned int v0;  // [bp-0x3c]
    unsigned int v1;  // [bp-0x38]
    unsigned int v2;  // [bp-0x34]
    unsigned int v3;  // [bp-0x30]
    char v4;  // [bp-0x2c]
    struct_0 v5;  // [bp-0x28]
    struct_0 *idx;  // [bp-0x20]
    char v7;  // [bp-0x1c]
    unsigned int v8;  // [bp-0x18]
    char v9;  // [bp-0x14]
    unsigned int v10;  // [bp-0x8]
    char v11;  // [bp-0x4]

    v10 = g_1038e180 ^ &v11;
    v3 = v12;
    v2 = v13;
    v1 = v14;
    sub_103536a7(&v5, a2);
    v8 = sub_10364959(&v9, &v4, a1, 0, 0, 0, 0, &v5);
    v15 = sub_10363ed5(&v9, a0);
    if (!((char)v8 & 3))
    {
        if (v15 == 1)
            goto LABEL_10361f66;
        if (v15 != 2)
            goto LABEL_10361f98;
LABEL_10361f7c:
        if (v7)
            idx[8].field_8 = idx[8].field_8 & 4294967293;
        v0 = 4;
        goto LABEL_10361f74;
    }
    else
    {
        if (((char)v8 & 1))
            goto LABEL_10361f7c;
        if (((char)v8 & 2))
        {
LABEL_10361f66:
            if (v7)
                idx[8].field_8 = idx[8].field_8 & 4294967293;
            v0 = 3;
LABEL_10361f74:
        }
        else
        {
LABEL_10361f98:
            if (v7)
                idx[8].field_8 = idx[8].field_8 & 4294967293;
        }
    }
    return sub_10351225();
}
```

## `sub_10361fb5` `0x10361fb5`

_166 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

extern unsigned int g_1038e180;

int sub_10361fb5(int a0, int a1, unsigned int *a2)
{
    unsigned int v12;  // ebx
    unsigned int v13;  // esi
    unsigned int v14;  // edi
    unsigned int v15;  // eax
    unsigned int v0;  // [bp-0x3c]
    unsigned int v1;  // [bp-0x38]
    unsigned int v2;  // [bp-0x34]
    unsigned int v3;  // [bp-0x30]
    char v4;  // [bp-0x2c]
    struct_0 v5;  // [bp-0x28]
    struct_0 *idx;  // [bp-0x20]
    char v7;  // [bp-0x1c]
    unsigned int v8;  // [bp-0x18]
    char v9;  // [bp-0x14]
    unsigned int v10;  // [bp-0x8]
    char v11;  // [bp-0x4]

    v10 = g_1038e180 ^ &v11;
    v3 = v12;
    v2 = v13;
    v1 = v14;
    sub_103536a7(&v5, a2);
    v8 = sub_10364959(&v9, &v4, a1, 0, 0, 0, 0, &v5);
    v15 = sub_10364417(&v9, a0);
    if (!((char)v8 & 3))
    {
        if (v15 == 1)
            goto LABEL_1036200c;
        if (v15 != 2)
            goto LABEL_1036203e;
LABEL_10362022:
        if (v7)
            idx[8].field_8 = idx[8].field_8 & 4294967293;
        v0 = 4;
        goto LABEL_1036201a;
    }
    else
    {
        if (((char)v8 & 1))
            goto LABEL_10362022;
        if (((char)v8 & 2))
        {
LABEL_1036200c:
            if (v7)
                idx[8].field_8 = idx[8].field_8 & 4294967293;
            v0 = 3;
LABEL_1036201a:
        }
        else
        {
LABEL_1036203e:
            if (v7)
                idx[8].field_8 = idx[8].field_8 & 4294967293;
        }
    }
    return sub_10351225();
}
```

## `sub_1036205b` `0x1036205b`

_189 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
    char padding_8[4];
    struct struct_1 *field_c;
} struct_0;

typedef struct struct_2 {
    char field_0;
    char field_1;
} struct_2;

typedef struct struct_1 {
    char field_0;
} struct_1;

unsigned int sub_1036205b(struct_2 *a0, unsigned int a1, int a2, struct_0 *a3)
{
    struct_0 *idx;  // ecx
    char *node;  // edi
    unsigned int v7;  // esi
    int v8;  // edx
    struct_2 *iter;  // eax
    char v10;  // cl
    struct_2 *v11;  // edi
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x14]

    idx = a3;
    node = &idx->field_c->field_0;
    if (!a0 || a1 <= 0)
    {
        v4 = 22;
        v7 = 22;
        *((unsigned int *)sub_103575e0()) = 22;
    }
    else
    {
        v8 = a2;
        a0->field_0 = 0;
        if (a1 <= (v8 <= 0 ? v8 : 0) + 1)
        {
            v4 = 0x22;
            *((unsigned int *)sub_103575e0()) = 0x22;
            v7 = 0x22;
        }
        else
        {
            a0->field_0 = 48;
            iter = &a0->field_1;
            if (v8 > 0)
            {
                do
                {
                    if (*(node))
                    {
                        v10 = *(node);
                        node += 1;
                    }
                    else
                    {
                        v4 = 48;
                        v10 = 48;
                    }
                } while ((iter->field_0 = v10, iter += 1, v8 = (int)(v8 - 1), v8 > 0));
                idx = a3;
            }
            iter->field_0 = 0;
            if (v8 >= 0 && *(node) >= 53)
            {
                while (true)
                {
                    iter = &iter->field_1;
                    if (iter->field_0 != 57)
                        break;
                    iter->field_0 = 48;
                }
                iter->field_0 = iter->field_0 + 1;
            }
            if (a0->field_0 == 49)
            {
                idx->field_4 = idx->field_4 + 1;
            }
            else
            {
                v11 = &a0->field_1;
                sub_10350ec0(a0, v11, sub_10352f20(v11) + 1);
            }
            return 0;
        }
    }
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    sub_103535f2();
    return v7;
}
```

## `sub_10362118` `0x10362118`

_187 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned short field_8;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
    unsigned short field_4[2];
    char field_6;
} struct_0;

struct_1 * sub_10362118(struct_1 *a0, struct_0 *a1)
{
    unsigned int v2;  // ecx
    unsigned int v3;  // eax
    unsigned int v12;  // ecx
    unsigned int v13;  // edx
    unsigned int v14;  // ecx
    unsigned short v4;  // cx
    unsigned int v5;  // edx
    unsigned int v6;  // ebx
    unsigned int v7;  // eax
    unsigned short v8;  // cx
    unsigned int v9;  // edi
    struct_1 *idx;  // eax
    unsigned short v11;  // cx
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp+0x8]

    v0 = v2;
    v3 = a1->field_4[1];
    v4 = (unsigned short)(v3 >> 4) & 0x7ff;
    v1 = v3 & 0x8000;
    v5 = a1->field_0;
    v6 = v4;
    v7 = (unsigned int)(a1->field_4 & 0xfffff);
    v0 = 0x80000000;
    if (v6)
    {
        if (v6 != 0x7ff)
        {
            v8 = v4 + 0x3c00;
LABEL_10362187:
            v9 = v8;
        }
        else
        {
            v9 = 0x7fff;
        }
        v12 = v5 >> 21 | v7 * 0x800 | v0;
        idx = a0;
        idx->field_4 = v12;
        idx->field_0 = v5 * 0x800;
        if (!(v12 & 0x80000000))
        {
            do
            {
                v13 = idx->field_4 * 2 | idx->field_0 >> 31;
                v14 = idx->field_0 * 2;
                v9 += 0xffff;
                idx->field_4 = v13;
                idx->field_0 = v14;
            } while (!(v13 & 0x80000000));
        }
        v11 = (unsigned short)v1 | (unsigned short)v9;
    }
    else if (!v7 && !v5)
    {
        idx = a0;
        v11 = v1;
        idx->field_4 = 0;
        idx->field_0 = 0;
    }
    else
    {
        v8 = v4 + 15361;
        v0 = 0;
        goto LABEL_10362187;
    }
    idx->field_8 = v11;
    return idx;
}
```

## `sub_103621d3` `0x103621d3`

_142 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned short field_8;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    char *field_c;
} struct_0;

extern unsigned int g_1038e180;

int sub_103621d3(char a0, unsigned int a0, struct_0 *idx, char *a2, unsigned int a3)
{
    unsigned int v17;  // ebx
    unsigned int v18;  // esi
    unsigned int v19;  // edi
    unsigned int v0;  // [bp-0x54]
    unsigned int v1;  // [bp-0x50], Other Possible Types: unsigned short
    unsigned int v2;  // [bp-0x4c]
    unsigned int v3;  // [bp-0x48]
    char *v4;  // [bp-0x44], Other Possible Types: unsigned int
    unsigned int v5;  // [bp-0x40]
    unsigned int v6;  // [bp-0x3c]
    unsigned int v7;  // [bp-0x38]
    unsigned short v8;  // [bp-0x30]
    char v9;  // [bp-0x2e]
    char v10[24];  // [bp-0x2c]
    struct_1 v11;  // [bp-0x14]
    unsigned int v12;  // [bp-0x10]
    unsigned short v13;  // [bp-0xc]
    unsigned int v14;  // [bp-0x8]
    char v15;  // [bp-0x4]

    v14 = g_1038e180 ^ &v15;
    v7 = v17;
    v6 = v18;
    v5 = v19;
    sub_10362118(&v11, &/* unsupported instruction */);
    v4 = &v8;
    v3 = 0;
    v2 = 0x11;
    v0 = v12;
    v1 = v13;
    idx->field_8 = sub_10365829(v11);
    idx->field_0 = v9;
    idx->field_4 = v8;
    if (sub_10359f58(a2, a3, v10))
    {
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        sub_103534f6();
    }
    idx->field_c = a2;
    return sub_10351225();
}
```

## `sub_10362270` `0x10362270`

_223 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10362270(unsigned int a0, unsigned int a1, unsigned long long a2, unsigned int a3)
{
    unsigned int v0;  // edi
    int v1;  // ebp
    unsigned int v10;  // ecx
    unsigned int v11;  // edx
    unsigned int v12;  // 4169
    unsigned long v13;  // 4170
    unsigned int v14;  // eax
    unsigned int v15;  // ecx
    unsigned int v16;  // edx
    unsigned int v18;  // eax
    unsigned int i;  // eax
    unsigned int v3;  // esi
    unsigned int v4;  // eax
    unsigned int v5;  // edx
    unsigned long long v6;  // ecx
    unsigned int v8;  // 4166
    unsigned long v9;  // 4167

    v0 = 0;
    v1 = 0;
    if (a1 < 0)
    {
        v0 = 1;
        v1 = 1;
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
        v3 = (a1 % a2 CONCAT a0) / a2;
    }
    else
    {
        v4 = a0;
        v5 = a1;
        v6 = a2;
        do
        {
            v8 = _ccall(27, i >> 1, i, 0);
            v9 = _ccall(v6, 1, v8, 4);
            v12 = _ccall(27, v5 >> 1, v5, 0);
            v13 = _ccall(v4, 1, v12, 4);
            v4 = v13;
            v5 >>= 1;
            i >>= 1;
            v6 = v9;
        } while (i);
        v3 = (v11 CONCAT v14) / v10;
        v15 = v3 * a3;
        v16 = a2 * v3 >> 32;
        if (v16 + v15 < 0 || v16 + v15 > a1 || v16 + v15 >= a1 && (unsigned int)(a2 * v3) > a0)
            v3 -= 1;
    }
    v18 = v3;
    if (v0 == 1)
        v18 = -(v18);
    return v18;
}
```

## `sub_10362350` `0x10362350`

_31 bytes. (leaf/helper — see body)_

```c
int sub_10362350(void)
{
    char v1;  // cl

    if (v1 >= 64)
    {
        return;
    }
    else if (v1 >= 32)
    {
        return;
    }
    else if ((v1 & 31))
    {
        return;
    }
    else
    {
        return;
    }
}
```

## `sub_1036236f` `0x1036236f`

_9 bytes. (leaf/helper — see body)_

```c
void sub_1036236f(void)
{
    sub_10353c92(2);
    return;
}
```

## `sub_10362378` `0x10362378`

_106 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10362378(unsigned int *a0, int a1, unsigned int a2)
{
    unsigned int v6;  // eax
    unsigned int v7;  // edi
    unsigned int *v8;  // edi
    unsigned int *v9;  // esi
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]

    v6 = a2 & 4294443007;
    if ((a1 & v6 & 4243651808))
    {
        v5 = v7;
        v8 = a0;
        if (v8)
            *(v8) = sub_1036621d(0, 0);
        v4 = 22;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        *((unsigned int *)sub_103575e0()) = 22;
        sub_103535f2();
        return 22;
    }
    else
    {
        v9 = a0;
        if (v9)
            *(v9) = sub_1036621d(a1, v6);
        else
            sub_1036621d(a1, v6);
        return 0;
    }
}
```

## `sub_103623e2` `0x103623e2`

_150 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    char field_c;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b1f8;
extern unsigned int g_103a1460;
extern unsigned int g_103a3c80;
extern char g_103a4ca0;

void sub_103623e2(unsigned int a0)
{
    unsigned int v5;  // ecx
    unsigned int v6;  // edx
    int v7;  // edi
    unsigned int v8;  // esi
    struct_0 **v9;  // eax
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp+0x0]
    int v2;  // [bp+0xfffe4]
    unsigned int v3;  // [bp+0xfffe8]
    unsigned int v4;  // [bp+0x100000]

    sub_1035b0cc(&g_103a1460, 16);
    v3 = 0;
    sub_1035a599(v5, v6, 1);
    v4 = 0;
    v7 = 3;
    while (true)
    {
        v2 = v7;
        if (v7 >= *((int *)&g_103a4ca0))
            break;
        v8 = v7 * 4;
        v9 = g_103a3c80 + v8;
        if (*(v9))
        {
            if ((*(v9)->field_c & 131) && sub_10366592(*(v9)) != 4294967295)
                v3 += 1;
            if (v7 >= 20)
            {
                g_1038b1f8(*((int *)(v8 + g_103a3c80)) + 32);
                v0 = *((int *)(v8 + g_103a3c80));
                sub_1035345e();
                *((unsigned int *)(v8 + g_103a3c80)) = 0;
            }
        }
        v7 += 1;
    }
    v4 = 4294967294;
    sub_10362478();
    sub_1035b111(3, &g_103a1460, 16, v1);
    return;
}
```

## `sub_10362478` `0x10362478`

_9 bytes. (leaf/helper — see body)_

```c
int sub_10362478(void)
{
    return sub_1035a4c1(1);
}
```

## `sub_10362481` `0x10362481`

_98 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

unsigned int sub_10362481(struct_0 *idx)
{
    unsigned int v3;  // ebx
    unsigned int v4;  // edi
    unsigned int v5;  // edi
    unsigned int v6;  // eax
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]

    v3 = 0;
    if (((char)*((int *)&idx->padding_0[12]) & 3) == 2 && ((unsigned short)*((int *)&idx->padding_0[12]) & 264))
    {
        v2 = v4;
        v5 = *((int *)&idx->padding_0[0]) - *((int *)&idx->padding_0[8]);
        if (v5 > 0)
        {
            v1 = v5;
            v0 = *((int *)&idx->padding_0[8]);
            if ((unsigned int)sub_10360ce9(sub_10360e67(idx)) != v1)
            {
                *((unsigned int *)&idx->padding_0[12]) = *((int *)&idx->padding_0[12]) | 32;
                v3 = 4294967295;
            }
            else if ((char)*((int *)&idx->padding_0[12]) < 0)
            {
                *((unsigned int *)&idx->padding_0[12]) = *((int *)&idx->padding_0[12]) & 4294967293;
            }
        }
    }
    v6 = *((int *)&idx->padding_0[8]);
    *((unsigned int *)&idx->padding_0[4]) = 0;
    *((unsigned int *)&idx->padding_0[0]) = v6;
    return v3;
}
```

## `sub_103624e3` `0x103624e3`

_66 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

unsigned int sub_103624e3(struct_0 *a0)
{
    if (!a0)
    {
        return sub_10362525(0);
    }
    else if (sub_10362481(a0))
    {
        return 4294967295;
    }
    else if ((*((short *)&a0->padding_0[12]) & 0x4000))
    {
        return -(0 < sub_1036660e(sub_10360e67(a0)));
    }
    else
    {
        return 0;
    }
}
```

## `sub_10362525` `0x10362525`

_187 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    char field_c;
} struct_0;

typedef struct struct_1 {
    char padding_0[12];
    unsigned int field_c;
} struct_1;

extern unsigned int g_103a1480;
extern unsigned int g_103a3c80;
extern char g_103a4ca0;

void sub_10362525(unsigned int a0)
{
    unsigned int v6;  // ecx
    unsigned int v7;  // edx
    unsigned int idx;  // esi
    struct_0 **v9;  // eax
    struct_1 *v10;  // eax
    unsigned int v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0xfffe0]
    unsigned int v2;  // [bp+0xfffe4]
    unsigned int v3;  // [bp+0xfffe8]
    unsigned int v4;  // [bp+0x100000]
    unsigned int v5;  // [bp+0x10000c]

    sub_1035b0cc(&g_103a1480, 20);
    v3 = 0;
    v1 = 0;
    sub_1035a599(v6, v7, 1);
    v4 = 0;
    idx = 0;
    while (true)
    {
        v2 = idx;
        if (idx >= *((int *)&g_103a4ca0))
            break;
        v9 = g_103a3c80 + idx * 4;
        if (*(v9) && (*(v9)->field_c & 131))
        {
            sub_1035cd8e(v6, v7, idx, *(v9));
            v4 = 1;
            v10 = *((int *)(g_103a3c80 + idx * 4));
            if (((char)v10->field_c & 131))
            {
                if (v5 == 1)
                {
                    if (sub_103624e3(v10) != 4294967295)
                        v3 += 1;
                }
                else
                {
                    if (!v5 && ((char)v10->field_c & 2) && sub_103624e3(v10) == 4294967295)
                        v1 = 4294967295;
                }
            }
            v4 = 0;
            sub_103625c7();
        }
        idx += 1;
    }
    v4 = 4294967294;
    sub_103625f6();
    if (v5 != 1)
        sub_1035b111(&g_103a1480, 20, v0, a0);
    else
        sub_1035b111(&g_103a1480, 20, v0, a0);
    return;
}
```

## `sub_103625c2` `0x103625c2`

_5 bytes. (leaf/helper — see body)_

```c
void sub_103625c2(void)
{
    sub_103625c7();
    return;
}
```

## `sub_103625c7` `0x103625c7`

_17 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a3c80;

int sub_103625c7(void)
{
    unsigned int v1;  // esi

    return sub_1035cdf2(v1, *((int *)(g_103a3c80 + v1 * 4)));
}
```

## `sub_103625f6` `0x103625f6`

_9 bytes. (leaf/helper — see body)_

```c
int sub_103625f6(void)
{
    return sub_1035a4c1(1);
}
```

## `sub_103625ff` `0x103625ff`

_9 bytes. (leaf/helper — see body)_

```c
void sub_103625ff(void)
{
    sub_10362525(1);
    return;
}
```

## `sub_10362608` `0x10362608`

_1881 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[4];
    char field_4;
} struct_1;

typedef struct struct_6 {
    char padding_0[36];
    char field_24;
} struct_6;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern char g_10000000;
extern struct_0 *g_1038b07c;
extern struct_0 *g_1038b120;
extern struct_0 *g_1038b128;
extern struct_0 *g_1038b274;
extern unsigned int g_103a2ff8;
extern unsigned int g_103a3b80[4];

int sub_10362608(void)
{
    unsigned int v32;  // ebx
    unsigned int v33;  // esi
    unsigned int v43;  // eax
    void* v44;  // eax
    unsigned int v45;  // eax
    unsigned int v46;  // eax
    struct_1 *v47;  // eax
    unsigned int v49;  // eax
    struct_1 *v50;  // eax
    unsigned int v34;  // edi
    unsigned int *v51;  // esi
    char v52;  // 4167
    unsigned int v53;  // eax
    unsigned int v54;  // eax
    unsigned int v55;  // eax
    unsigned int v56;  // eax
    unsigned int v57;  // edx
    unsigned int v58;  // ecx
    unsigned int v59;  // eax
    unsigned int v60;  // eax
    unsigned int v35;  // ecx
    unsigned int v61;  // eax
    unsigned int v62;  // eax
    unsigned int v36;  // eax
    int v63;  // edi
    unsigned int v64;  // eax
    struct_6 *v65;  // eax
    struct_6 *v66;  // eax
    struct_1 *v67;  // eax
    unsigned int v68;  // eax
    struct_1 *v70;  // eax
    unsigned int v37;  // eax
    unsigned int v38;  // eax
    unsigned int v39;  // eax
    unsigned int v40;  // eax
    unsigned int v41;  // eax
    char *v0;  // [bp-0x88]
    unsigned int v1;  // [bp-0x84]
    unsigned int v2;  // [bp-0x58]
    unsigned int v3;  // [bp-0x54]
    unsigned int v4;  // [bp-0x50]
    unsigned int v5;  // [bp-0x4c]
    unsigned int v6;  // [bp-0x48]
    unsigned int v7;  // [bp-0x44]
    unsigned int v8;  // [bp-0x40]
    unsigned int v9;  // [bp-0x3c]
    unsigned int v10;  // [bp-0x38]
    unsigned int v11;  // [bp-0x34]
    unsigned int v12;  // [bp-0x30]
    unsigned int v13;  // [bp-0x2c]
    unsigned int v14;  // [bp-0x28]
    unsigned int v15;  // [bp-0x24]
    int v16;  // [bp-0x20]
    int v17;  // [bp-0x1c], Other Possible Types: unsigned int
    int v18;  // [bp-0x18], Other Possible Types: unsigned int
    unsigned int v19;  // [bp-0x14]
    unsigned int v20;  // [bp-0x10]
    unsigned int v21;  // [bp-0xc]
    char v22;  // [bp-0x8]
    char v23;  // [bp-0x7]
    char v24;  // [bp-0x7]
    char v25;  // [bp-0x6]
    char v26;  // [bp-0x5]
    unsigned int *v27;  // [bp+0x4]
    unsigned int v28;  // [bp+0x8]
    unsigned int v29;  // [bp+0xc]
    unsigned int v30;  // [bp+0x10]
    unsigned int v31;  // [bp+0x14]

    v9 = v32;
    v8 = v33;
    v7 = v34;
    v14 = 0;
    v13 = 0;
    v25 = 0;
    v10 = 12;
    v11 = 0;
    if (((char)v29 & 128))
    {
        v12 = 0;
        v26 = 16;
    }
    else
    {
        v12 = 1;
        v26 = 0;
    }
    if (sub_103670f3(&v14))
    {
        v6 = 0;
        v5 = 0;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        sub_103534f6();
    }
    if (sub_10353d3b(&v13))
    {
        v6 = 0;
        v5 = 0;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        sub_103534f6();
    }
    v35 = v29;
    if (!((unsigned short)v35 & 0x8000) && ((v35 & 0x74000) || v14 != 0x8000))
        v26 |= 128;
    v36 = v35 & 3;
    v37 = v36 - 0;
    if (v36)
    {
        if (v37 != 1)
        {
            if (v37 == 2)
                goto LABEL_103626d3;
            goto LABEL_103626ad;
        }
        else if (((char)v35 & 8) && (v35 & 0x70000))
        {
LABEL_103626d3:
            v21 = 0xc0000000;
            goto LABEL_103626f1;
        }
        else
        {
            v21 = 0x40000000;
            goto LABEL_103626f1;
        }
    }
    v21 = 0x80000000;
LABEL_103626f1:
    v6 = 16;
    v38 = v30 - 16;
    if (v30 != 16)
    {
        v39 = v38 - 16;
        if (v38 != 16)
        {
            v40 = v39 - 16;
            if (v39 != 16)
            {
                v41 = v40 - 16;
                if (v40 != 16)
                {
                    if (v41 != 64)
                        goto LABEL_103626ad;
                    v19 = _INSERT(v41 - 64, 0, v21 == 0x80000000);
                }
                else
                {
                    v19 = 3;
                }
            }
            else
            {
                v19 = 2;
            }
        }
        else
        {
            v19 = 1;
        }
    }
    else
    {
        v19 = 0;
    }
    v43 = v29 & 0x700;
    if (v43 <= 0x400)
    {
        if (!(v43 != 0x400 && v43))
        {
            v18 = 3;
        }
        else if (v43 != 0x100)
        {
            if (v43 == 0x200)
                goto LABEL_103627fb;
            if (v43 != 0x300)
                goto LABEL_103626ad;
            v18 = 2;
        }
        else
        {
            v18 = 4;
        }
    }
    else
    {
        if (v43 != 0x500)
        {
            if (v43 != 0x600)
            {
                if (v43 == 0x700)
                    goto LABEL_1036279e;
LABEL_103626ad:
                *((unsigned int *)sub_103575f3()) = 0;
                *((unsigned int *)v44) = 4294967295;
                v6 = 22;
                v6 = 0;
                v5 = 0;
                v4 = 0;
                v3 = 0;
                v2 = 0;
                *((unsigned int *)sub_103575e0()) = 22;
                sub_103535f2();
                return;
            }
LABEL_103627fb:
            v18 = 5;
        }
        else
        {
LABEL_1036279e:
            v18 = 1;
        }
    }
    v45 = v29;
    v20 = 128;
    if (((unsigned short)v45 & 0x100) && (char)(~(g_103a2ff8) & v31) >= 0)
        v20 = 1;
    if (((char)v45 & 64))
    {
        v20 |= 0x4000000;
        v21 |= 0x10000;
        if (v13 == 2)
            v19 |= 4;
    }
    if (((unsigned short)v45 & 0x1000))
        v20 |= 0x100;
    if (((char)v45 & 32))
    {
        v20 |= 0x8000000;
    }
    else if (((char)v45 & 16))
    {
        v20 |= &g_10000000;
    }
    v46 = sub_1036524a();
    *((unsigned int *)v44) = v46;
    if (v46 == 4294967295)
    {
        *((unsigned int *)sub_103575f3()) = 0;
        *((unsigned int *)v44) = 4294967295;
        *((unsigned int *)sub_103575e0()) = 24;
        sub_103575e0();
        return;
    }
    *(v27) = 1;
    v16 = g_1038b120(v28, v21, v19, &v10, v18, v20, 0);
    if (v16 == 4294967295 && ((v21 & 0xc0000000) != 0xc0000000 || !((char)v29 & 1) || !((v21 &= 2147483647, v16 = (int)g_1038b120(v28, v21, v19, &v10, v18, v20, 0), v16 != -1))))
    {
        v47 = g_103a3b80[*((int *)v44) >> 5] + (*((int *)v44) & 31) * 56 + 4;
        v47->padding_0[0] = v47->padding_0[0] & 254;
        sub_10357606(g_1038b07c());
        sub_103575e0();
        return;
    }
    v49 = g_1038b274(v16);
    if (!v49)
    {
        v50 = g_103a3b80[*((int *)v44) >> 5] + (*((int *)v44) & 31) * 56 + 4;
        v50->padding_0[0] = v50->padding_0[0] & 254;
        v51 = g_1038b07c();
        sub_10357606(v51);
        g_1038b128(v16);
        if (!v51)
        {
            *((unsigned int *)sub_103575e0()) = 13;
            sub_103575e0();
            return;
        }
        sub_103575e0();
        return;
    }
    else
    {
        if (v49 == 2)
        {
            v26 |= 64;
        }
        else if (v49 == 3)
        {
            v26 |= 8;
        }
        sub_10365019(*((int *)v44), v16);
        v52 = v26;
        *((char *)(g_103a3b80[*((int *)v44) >> 5] + (*((int *)v44) & 31) * 56 + 4)) = v52 | 1;
        v53 = *((int *)v44) & 31;
        *((char *)(g_103a3b80[*((int *)v44) >> 5] + v53 * 56 + 36)) = *((char *)(g_103a3b80[*((int *)v44) >> 5] + v53 * 56 + 36)) & 128;
        v23 = v52 | 1;
        v24 = v23 & 72;
        v26 = v52 | 1;
        if ((v23 & 72))
        {
LABEL_10362a09:
            if ((v26 & 128))
            {
                if (!(0x74000 & v29))
                    v29 = (!(v14 & 0x74000) ? v29 | 0x4000 : v29 | v14 & 0x74000);
                v54 = v29 & 0x74000;
                if (v54 != 0x4000)
                {
                    if (v54 != 0x10000 && v54 != 0x14000)
                    {
                        if (v54 == 0x20000 || v54 == 0x24000)
                            goto LABEL_10362a78;
                        if (v54 == 0x40000 || v54 == 0x44000)
                            v25 = 1;
                    }
                    else
                    {
                        if (((unsigned short)v29 & 769) == 769)
                        {
LABEL_10362a78:
                            v25 = 2;
                        }
                    }
                }
                else
                {
                    v25 = 0;
                }
                if ((v29 & 0x70000) && (v17 = 0, !(v26 & 64)))
                {
                    v55 = v21 & 0xc0000000;
                    if (v55 != 0x40000000)
                    {
                        if (v55 != 0x80000000)
                        {
                            if (v55 == 0xc0000000 && (v56 = v18, v56 > 0) && v56 > 2)
                            {
                                if (v56 > 4)
                                    goto LABEL_10362ad0;
                                if (sub_10360587(0xc0000000, v57, *((int *)v44), 0, 0, 2) || v57)
                                {
                                    if ((sub_10360587(v58, v57, *((int *)v44), 0, 0, 0) & v57) == 4294967295)
                                    {
                                        sub_10366e64(*((int *)v44));
                                        sub_103575e0();
                                        return;
                                    }
                                    goto LABEL_10362bfa;
                                }
                            }
                        }
                        else
                        {
LABEL_10362bfa:
                            v59 = sub_103668a3(*((int *)v44), &v17, 3);
                            if (v59 == 4294967295)
                            {
LABEL_103629bc:
                                sub_10366e64(*((int *)v44));
                                sub_103575e0();
                                return;
                            }
                            if (v59 != 2)
                            {
                                if (v59 != 3)
                                    goto LABEL_10362ccd;
                                if (v17 != 12565487)
                                    goto LABEL_10362c7f;
                                v25 = 1;
                            }
                            else
                            {
LABEL_10362c7f:
                                v60 = v17 & 0xffff;
                                if (v60 == 0xfffe)
                                {
                                    sub_10366e64(*((int *)v44));
                                    v1 = 22;
                                    *((unsigned int *)sub_103575e0()) = 22;
                                    return;
                                }
                                if (v60 == 0xfeff)
                                {
                                    if (sub_10366fc5(*((int *)v44), 2, 0) == 4294967295)
                                    {
                                        sub_10366e64(*((int *)v44));
                                        sub_103575e0();
                                        return;
                                    }
                                    v25 = 2;
                                }
                                else
                                {
LABEL_10362ccd:
                                    v61 = sub_10366fc5(*((int *)v44), 0, 0);
LABEL_10362c71:
                                    if (v61 == 4294967295)
                                    {
                                        sub_10366e64(*((int *)v44));
                                        sub_103575e0();
                                        return;
                                    }
                                }
                            }
                        }
                    }
                    else
                    {
                        v56 = v18;
                        if (v56 > 0)
                        {
                            if (v56 > 2)
                            {
                                if (v56 > 4)
                                {
LABEL_10362ad0:
                                    if (v56 == 5)
                                        goto LABEL_10362cdb;
                                }
                                else
                                {
                                    if (sub_10360587(0xc0000000, v57, *((int *)v44), 0, 0, 2) || v57)
                                    {
                                        v61 = sub_10360587(v58, v57, *((int *)v44), 0, 0, 0) & v57;
                                        goto LABEL_10362c71;
                                    }
                                }
                            }
                            else
                            {
LABEL_10362cdb:
                                v62 = v25;
                                v63 = 0;
                                if (v62 != 1)
                                {
                                    if (v62 != 2)
                                        goto LABEL_10362ad9;
                                    v17 = 0xfeff;
                                    v18 = 2;
                                }
                                else
                                {
                                    v17 = 12565487;
                                    v18 = 3;
                                }
                                do
                                {
                                    v1 = v18 - v63;
                                    v0 = (char *)&v17 + v63;
                                    if ((unsigned int)sub_10360ce9(*((int *)v44)) == 4294967295)
                                    {
                                        sub_10366e64(*((int *)v44));
                                        v15 = *((int *)sub_103575e0());
                                        return;
                                    }
                                } while ((v63 = (int)(v63 + v64), v18 > v63));
                            }
                        }
                    }
                }
            }
        }
        else if (((v52 | 1) & 128))
        {
            if (((char)v29 & 2))
            {
                v17 = sub_10366fc5(*((int *)v44), -1, 2);
                if (v17 != 4294967295)
                {
                    v22 = 0;
                    if (!sub_103668a3(*((int *)v44), &v22, 1) && v22 == 26 && sub_103666ef(*((int *)v44), v17, v17 >> 31) == 4294967295 || sub_10366fc5(*((int *)v44), 0, 0) == 4294967295)
                        goto LABEL_103629bc;
                    goto LABEL_10362a09;
                }
                else if (*((int *)sub_103575f3()) != 131)
                {
                    sub_10366e64(*((int *)v44));
                    sub_103575e0();
                    return;
                }
            }
            goto LABEL_10362a09;
        }
LABEL_10362ad9:
        v65 = g_103a3b80[*((int *)v44) >> 5] + (*((int *)v44) & 31) * 56 + 36;
        v65->padding_0[0] = v65->padding_0[0] ^ (v65->padding_0[0] ^ v25) & 127;
        v66 = g_103a3b80[*((int *)v44) >> 5] + (*((int *)v44) & 31) * 56 + 36;
        v66->padding_0[0] = (char)(v29 >> 16) * 128 | v66->padding_0[0] & 127;
        if (!v24 && ((char)v29 & 8))
        {
            v67 = g_103a3b80[*((int *)v44) >> 5] + (*((int *)v44) & 31) * 56 + 4;
            v67->padding_0[0] = v67->padding_0[0] | 32;
        }
        if ((v21 & 0xc0000000) != 0xc0000000)
        {
            return;
        }
        else if (((char)v29 & 1))
        {
            g_1038b128(v16);
            v68 = g_1038b120(v28, v21 & 2147483647, v19, &v10, 3, v20, 0);
            if (v68 != 4294967295)
            {
                *((unsigned int *)((*((int *)v44) & 31) * 56 + g_103a3b80[*((int *)v44) >> 5])) = v68;
                return;
            }
            sub_10357606(g_1038b07c());
            v70 = g_103a3b80[*((int *)v44) >> 5] + (*((int *)v44) & 31) * 56 + 4;
            v70->padding_0[0] = v70->padding_0[0] & 254;
            sub_10365096(*((int *)v44));
            sub_103575e0();
            return;
        }
        else
        {
            return;
        }
    }
}
```

## `sub_10362d61` `0x10362d61`

_153 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a14a8;

void sub_10362d61(unsigned int a0)
{
    unsigned int *v15;  // edi
    unsigned int v16;  // eax
    unsigned int v17;  // 4138
    unsigned int v18;  // 4139
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp+0x0]
    int v6;  // [bp+0xfffe4]
    unsigned int v7;  // [bp+0xfffe8]
    unsigned int v8;  // [bp+0x100000]
    int v9;  // [bp+0x10000c]
    int v10;  // [bp+0x100010]
    int v11;  // [bp+0x100014]
    int v12;  // [bp+0x100018]
    unsigned int *v13;  // [bp+0x10001c]
    unsigned int v14;  // [bp+0x100020]

    sub_1035b0cc(&g_103a14a8, 20);
    v7 = 0;
    v15 = v13;
    if (v15)
    {
        *(v15) = 4294967295;
        if (v9 && (!v14 || !((v16 = v12 & 4294966911, v17 = (unsigned int)_ccall(12, 0, (unsigned int)(char)(0 < v16), (unsigned int)(char)(0 < v16)), v18 = (unsigned int)_ccall(4, 18, -((unsigned int)(char)(0 < v16)) + 1, 0, v17), (char)v18))))
        {
            v8 = 0;
            v6 = sub_10362608(/* unsupported instruction */ - 28, v9, v10, v11, v12);
            v8 = 4294967294;
            sub_10362dff();
            if (v6)
            {
                *(v15) = 4294967295;
                sub_1035b111(&g_103a14a8, 20, v5, a0);
            }
            else
            {
                sub_1035b111(&g_103a14a8, 20, v5, a0);
            }
            return;
        }
    }
    v4 = 22;
    *((unsigned int *)sub_103575e0()) = 22;
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    sub_103535f2();
    sub_1035b111(&g_103a14a8, 20, v5, a0);
    return;
}
```

## `sub_10362dfa` `0x10362dfa`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10362dfa(void)
{
    sub_10362dff();
    return;
}
```

## `sub_10362dff` `0x10362dff`

_46 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a3b80[4];

int sub_10362dff(void)
{
    unsigned int v3;  // esi
    int *v4;  // edi
    unsigned int v5;  // eax
    unsigned int v6;  // eax
    unsigned int v1;  // [bp+0xfffe4]
    unsigned int v2;  // [bp+0xfffe8]

    if (v2 == v3)
        return v6;
    if (v1 == v3)
        return sub_10365228(*(v4));
    v5 = *(v4) & 31;
    *((char *)(g_103a3b80[*(v4) >> 5] + v5 * 56 + 4)) = *((char *)(g_103a3b80[*(v4) >> 5] + v5 * 56 + 4)) & 254;
    return sub_10365228(*(v4));
}
```

## `sub_10362e2d` `0x10362e2d`

_30 bytes. (leaf/helper — see body)_

```c
void sub_10362e2d(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4)
{
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v4 = 1;
    v3 = a0;
    v2 = a4;
    v1 = a3;
    v0 = a2;
    sub_10362d61(a1);
    return;
}
```

## `sub_10362e4b` `0x10362e4b`

_538 bytes. (leaf/helper — see body)_

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

int sub_10362e4b(char *iter, char *a0, unsigned int *a1)
{
    unsigned int v13;  // ebx
    unsigned int v22;  // edx
    struct_0 *v23;  // ecx
    struct_0 *v24;  // eax
    unsigned short v25;  // cx
    unsigned short v26;  // cx
    struct_0 *v27;  // eax
    int v28;  // eax
    unsigned int v29;  // edx
    struct_0 *v30;  // ecx
    char *node;  // ebx
    unsigned int v31;  // 4136
    int v15;  // eax
    struct_0 *v16;  // eax
    unsigned int v17;  // edi
    unsigned short v18;  // cx
    unsigned short v19;  // si
    struct_0 *v20;  // eax
    int v21;  // eax
    unsigned int v0;  // [bp-0x34]
    unsigned int v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x28]
    unsigned int v4;  // [bp-0x24]
    unsigned int v5;  // [bp-0x20]
    struct_0 v6;  // [bp-0x18]
    struct_0 *v7;  // [bp-0x14]
    struct_1 *idx;  // [bp-0x10]
    char v9;  // [bp-0xc]
    char v10;  // [bp-0x8]
    char v11;  // [bp-0x7]

    sub_103536a7(&v6, a1);
    iter = iter;
    if (!iter)
    {
        v5 = 0;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        *((unsigned int *)sub_103575e0()) = 22;
        sub_103535f2();
        if (!v9)
            return 2147483647;
        idx->field_70 = idx->field_70 & 4294967293;
        return 2147483647;
    }
    else
    {
        v5 = v13;
        node = a0;
        if (!node)
        {
            v4 = 0;
            v3 = 0;
            v2 = 0;
            v1 = 0;
            v0 = 0;
            *((unsigned int *)sub_103575e0()) = 22;
            sub_103535f2();
            if (v9)
                idx->field_70 = idx->field_70 & 4294967293;
            v15 = 2147483647;
        }
        else
        {
            v16 = v7;
            if (!v16->field_8)
            {
                v15 = sub_1035dd25(iter, node, &v6);
                if (v9)
                    idx->field_70 = idx->field_70 & 4294967293;
            }
            else
            {
                v4 = v17;
                while (true)
                {
                    v18 = *(iter);
                    iter += 1;
                    if (!(*(29 + v18 + (char *)v16) & 4))
                    {
                        v22 = v18;
                        v23 = v22 + (char *)v16;
                        v19 = (!(*((char *)&v23[2].field_0 + 3) & 16) ? (unsigned short)v22 : v23[21].field_c);
                        v20 = v16;
                    }
                    else if (!*(iter))
                    {
                        v19 = 0;
                        v20 = v16;
                    }
                    else
                    {
                        v21 = sub_10356e55(&v6, *((int *)&v16->field_c), 0x200, iter + 1, 2, &v10, 2, v16->field_4, 1);
                        if (v21 == 1)
                        {
                            v19 = v10;
                        }
                        else
                        {
                            if (v21 != 2)
                                goto LABEL_1036301d;
                            v19 = v10 * 0x100 + v11;
                        }
                        iter += 1;
                        v20 = v7;
                    }
                    v24 = v20;
                    v25 = *(node);
                    node += 1;
                    if (!(*(29 + v25 + (char *)v24) & 4))
                    {
                        v29 = v25;
                        v30 = v29 + (char *)v24;
                        v26 = (!(*((char *)&v30[2].field_0 + 3) & 16) ? (unsigned short)v29 : v30[21].field_c);
                        v27 = v24;
                    }
                    else if (!*(node))
                    {
                        v26 = 0;
                        v27 = v24;
                    }
                    else
                    {
                        v28 = sub_10356e55(&v6, *((int *)&v24->field_c), 0x200, node + 1, 2, &v10, 2, v24->field_4, 1);
                        if (v28 == 1)
                        {
                            v26 = v10;
                        }
                        else if (v28 == 2)
                        {
                            v26 = v10 * 0x100 + v11;
                        }
                        else
                        {
LABEL_1036301d:
                            *((unsigned int *)sub_103575e0()) = 22;
                            if (v9)
                                idx->field_70 = idx->field_70 & 4294967293;
                            v15 = 2147483647;
                            break;
                        }
                        node += 1;
                        v27 = v7;
                    }
                    v16 = v27;
                    if (v26 != v19)
                    {
                        v31 = _ccall(5, (unsigned int)v26, (unsigned int)v19, 0);
                        v15 = (-(v31 & 1) & 2) - 1;
                        if (v9)
                        {
                            idx->field_70 = idx->field_70 & 4294967293;
                            break;
                        }
                    }
                    else if (!v19)
                    {
                        if (v9)
                            idx->field_70 = idx->field_70 & 4294967293;
                        v15 = 0;
                        break;
                    }
                }
            }
        }
        return v15;
    }
}
```

## `sub_10363065` `0x10363065`

_19 bytes. (leaf/helper — see body)_

```c
int sub_10363065(char *a0, char *a1)
{
    return sub_10362e4b(a0, a1, NULL);
}
```

## `sub_10363078` `0x10363078`

_361 bytes. (leaf/helper — see body)_

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

unsigned int sub_10363078(struct_0 *iter, char *a1, unsigned int node, unsigned int *a3)
{
    unsigned int v11;  // edi
    unsigned int v12;  // eax
    char *v21;  // esi
    unsigned short v22;  // bx
    unsigned int v23;  // 4136
    unsigned int v13;  // esi
    char *v14;  // esi
    struct_0 *v15;  // eax
    unsigned int v16;  // ecx
    unsigned int v17;  // eax
    unsigned int v18;  // eax
    unsigned short v19;  // dx
    char *v20;  // esi
    unsigned int v0;  // [bp-0x34]
    unsigned int v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x28]
    unsigned int v4;  // [bp-0x24]
    unsigned int v5;  // [bp-0x20]
    unsigned int v6;  // [bp-0x1c]
    struct_0 v7;  // [bp-0x14]
    struct_0 *v8;  // [bp-0x10]
    struct_1 *idx;  // [bp-0xc]
    char v10;  // [bp-0x8]

    if (!node)
        return 0;
    v6 = v11;
    sub_103536a7(&v7, a3);
    if (!v8->field_8)
    {
        v12 = sub_1035fc2a(iter, a1, node);
        if (v10)
            idx->field_70 = idx->field_70 & 4294967293;
    }
    else if (!iter)
    {
        v5 = 0;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        *((unsigned int *)sub_103575e0()) = 22;
        sub_103535f2();
        if (v10)
            idx->field_70 = idx->field_70 & 4294967293;
        v12 = 2147483647;
    }
    else
    {
        v5 = v13;
        v14 = a1;
        if (!v14)
        {
            v4 = 0;
            v3 = 0;
            v2 = 0;
            v1 = 0;
            v0 = 0;
            *((unsigned int *)sub_103575e0()) = 22;
            sub_103535f2();
            if (v10)
                idx->field_70 = idx->field_70 & 4294967293;
            v12 = 2147483647;
        }
        else
        {
            do
            {
                v15 = iter;
                node -= 1;
                v16 = (char)v15->field_0;
                iter = (char *)&v15->field_0 + 1;
                if ((*(29 + v16 + (char *)v8) & 4))
                {
                    if (!node)
                    {
                        v17 = *(v14);
                        v16 = 0;
                        if ((*(29 + v17 + (char *)v8) & 4))
                            break;
                        v18 = (unsigned short)v17;
                        goto LABEL_103631a7;
                    }
                    else if (!(char)iter->field_0)
                    {
                        v16 = 0;
                    }
                    else
                    {
                        iter = (char *)&iter->field_0 + 1;
                        v19 = _INSERT((char)v16 * 0x100, 0, iter->field_0);
                        v16 = v19;
                    }
                }
                v18 = *(v14);
                v20 = v14 + 1;
                v14 = v20;
                if ((*(29 + v18 + (char *)v8) & 4))
                {
                    if (!node || (node -= 1, !*(v20)))
                    {
                        v18 = 0;
                        v14 = v20;
                    }
                    else
                    {
                        v21 = v20 + 1;
                        v22 = _INSERT((char)v18 * 0x100, 0, *(v20));
                        v18 = v22;
                        v14 = v21;
                    }
                }
LABEL_103631a7:
                if ((unsigned short)v18 != (unsigned short)v16)
                {
                    v23 = _ccall(5, (unsigned int)(unsigned short)v18, (unsigned int)(unsigned short)v16, 0);
                    v12 = (-(v23 & 1) & 2) - 1;
                    if (v10)
                    {
                        idx->field_70 = idx->field_70 & 4294967293;
                        goto LABEL_103631c8;
                    }
                }
            } while ((unsigned short)v16 && node);
            if (v10)
                idx->field_70 = idx->field_70 & 4294967293;
            v12 = 0;
        }
LABEL_103631c8:
    }
    return v12;
}
```

## `sub_103631e1` `0x103631e1`

_23 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

unsigned int sub_103631e1(struct_0 *a0, char *a1, unsigned int a2)
{
    return sub_10363078(a0, a1, a2, NULL);
}
```

## `sub_103631f8` `0x103631f8`

_1882 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[4];
    char field_4;
} struct_1;

typedef struct struct_6 {
    char padding_0[36];
    char field_24;
} struct_6;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern char g_10000000;
extern struct_0 *g_1038b07c;
extern struct_0 *g_1038b128;
extern struct_0 *g_1038b194;
extern struct_0 *g_1038b274;
extern unsigned int g_103a2ff8;
extern unsigned int g_103a3b80[4];

int sub_103631f8(void)
{
    unsigned int v32;  // ebx
    unsigned int v33;  // esi
    unsigned int v43;  // eax
    void* v44;  // eax
    unsigned int v45;  // eax
    unsigned int v46;  // eax
    struct_1 *v47;  // eax
    unsigned int v49;  // eax
    struct_1 *v50;  // eax
    unsigned int v34;  // edi
    unsigned int *v51;  // esi
    char v52;  // 4167
    unsigned int v53;  // eax
    unsigned int v54;  // eax
    unsigned int v55;  // eax
    unsigned int v56;  // eax
    unsigned int v57;  // edx
    unsigned int v58;  // ecx
    unsigned int v59;  // eax
    unsigned int v60;  // eax
    unsigned int v35;  // ecx
    unsigned int v61;  // eax
    unsigned int v62;  // eax
    unsigned int v36;  // eax
    int v63;  // edi
    unsigned int v64;  // eax
    struct_6 *v65;  // eax
    struct_6 *v66;  // eax
    struct_1 *v67;  // eax
    unsigned int v68;  // eax
    struct_1 *v70;  // eax
    unsigned int v37;  // eax
    unsigned int v38;  // eax
    unsigned int v39;  // eax
    unsigned int v40;  // eax
    unsigned int v41;  // eax
    char *v0;  // [bp-0x8c]
    unsigned int v1;  // [bp-0x88]
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
    int v17;  // [bp-0x20]
    int v18;  // [bp-0x1c], Other Possible Types: unsigned int
    int v19;  // [bp-0x18], Other Possible Types: unsigned int
    unsigned int v20;  // [bp-0x14]
    unsigned int v21;  // [bp-0x10]
    unsigned int v22;  // [bp-0xc]
    char v23;  // [bp-0x7]
    char v24;  // [bp-0x7]
    char v25;  // [bp-0x6]
    char v26;  // [bp-0x5]
    unsigned int *v27;  // [bp+0x4]
    unsigned int v28;  // [bp+0x8]
    unsigned int v29;  // [bp+0xc]
    unsigned int v30;  // [bp+0x10]
    unsigned int v31;  // [bp+0x14]

    v9 = v32;
    v8 = v33;
    v7 = v34;
    v15 = 0;
    v14 = 0;
    v25 = 0;
    v10 = 12;
    v11 = 0;
    if (((char)v29 & 128))
    {
        v12 = 0;
        v26 = 16;
    }
    else
    {
        v12 = 1;
        v26 = 0;
    }
    if (sub_103670f3(&v15))
    {
        v6 = 0;
        v5 = 0;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        sub_103534f6();
    }
    if (sub_10353d3b(&v14))
    {
        v6 = 0;
        v5 = 0;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        sub_103534f6();
    }
    v35 = v29;
    if (!((unsigned short)v35 & 0x8000) && ((v35 & 0x74000) || v15 != 0x8000))
        v26 |= 128;
    v36 = v35 & 3;
    v37 = v36 - 0;
    if (v36)
    {
        if (v37 != 1)
        {
            if (v37 == 2)
                goto LABEL_103632c3;
            goto LABEL_1036329d;
        }
        else if (((char)v35 & 8) && (v35 & 0x70000))
        {
LABEL_103632c3:
            v22 = 0xc0000000;
            goto LABEL_103632e1;
        }
        else
        {
            v22 = 0x40000000;
            goto LABEL_103632e1;
        }
    }
    v22 = 0x80000000;
LABEL_103632e1:
    v6 = 16;
    v38 = v30 - 16;
    if (v30 != 16)
    {
        v39 = v38 - 16;
        if (v38 != 16)
        {
            v40 = v39 - 16;
            if (v39 != 16)
            {
                v41 = v40 - 16;
                if (v40 != 16)
                {
                    if (v41 != 64)
                        goto LABEL_1036329d;
                    v20 = _INSERT(v41 - 64, 0, v22 == 0x80000000);
                }
                else
                {
                    v20 = 3;
                }
            }
            else
            {
                v20 = 2;
            }
        }
        else
        {
            v20 = 1;
        }
    }
    else
    {
        v20 = 0;
    }
    v43 = v29 & 0x700;
    if (v43 <= 0x400)
    {
        if (!(v43 != 0x400 && v43))
        {
            v19 = 3;
        }
        else if (v43 != 0x100)
        {
            if (v43 == 0x200)
                goto LABEL_103633eb;
            if (v43 != 0x300)
                goto LABEL_1036329d;
            v19 = 2;
        }
        else
        {
            v19 = 4;
        }
    }
    else
    {
        if (v43 != 0x500)
        {
            if (v43 != 0x600)
            {
                if (v43 == 0x700)
                    goto LABEL_1036338e;
LABEL_1036329d:
                *((unsigned int *)sub_103575f3()) = 0;
                *((unsigned int *)v44) = 4294967295;
                v6 = 22;
                v6 = 0;
                v5 = 0;
                v4 = 0;
                v3 = 0;
                v2 = 0;
                *((unsigned int *)sub_103575e0()) = 22;
                sub_103535f2();
                return;
            }
LABEL_103633eb:
            v19 = 5;
        }
        else
        {
LABEL_1036338e:
            v19 = 1;
        }
    }
    v45 = v29;
    v21 = 128;
    if (((unsigned short)v45 & 0x100) && (char)(~(g_103a2ff8) & v31) >= 0)
        v21 = 1;
    if (((char)v45 & 64))
    {
        v21 |= 0x4000000;
        v22 |= 0x10000;
        if (v14 == 2)
            v20 |= 4;
    }
    if (((unsigned short)v45 & 0x1000))
        v21 |= 0x100;
    if (((char)v45 & 32))
    {
        v21 |= 0x8000000;
    }
    else if (((char)v45 & 16))
    {
        v21 |= &g_10000000;
    }
    v46 = sub_1036524a();
    *((unsigned int *)v44) = v46;
    if (v46 == 4294967295)
    {
        *((unsigned int *)sub_103575f3()) = 0;
        *((unsigned int *)v44) = 4294967295;
        *((unsigned int *)sub_103575e0()) = 24;
        sub_103575e0();
        return;
    }
    *(v27) = 1;
    v17 = g_1038b194(v28, v22, v20, &v10, v19, v21, 0);
    if (v17 == 4294967295 && ((v22 & 0xc0000000) != 0xc0000000 || !((char)v29 & 1) || !((v22 &= 2147483647, v17 = (int)g_1038b194(v28, v22, v20, &v10, v19, v21, 0), v17 != -1))))
    {
        v47 = g_103a3b80[*((int *)v44) >> 5] + (*((int *)v44) & 31) * 56 + 4;
        v47->padding_0[0] = v47->padding_0[0] & 254;
        sub_10357606(g_1038b07c());
        sub_103575e0();
        return;
    }
    v49 = g_1038b274(v17);
    if (!v49)
    {
        v50 = g_103a3b80[*((int *)v44) >> 5] + (*((int *)v44) & 31) * 56 + 4;
        v50->padding_0[0] = v50->padding_0[0] & 254;
        v51 = g_1038b07c();
        sub_10357606(v51);
        g_1038b128(v17);
        if (!v51)
        {
            *((unsigned int *)sub_103575e0()) = 13;
            sub_103575e0();
            return;
        }
        sub_103575e0();
        return;
    }
    else
    {
        if (v49 == 2)
        {
            v26 |= 64;
        }
        else if (v49 == 3)
        {
            v26 |= 8;
        }
        sub_10365019(*((int *)v44), v17);
        v52 = v26;
        *((char *)(g_103a3b80[*((int *)v44) >> 5] + (*((int *)v44) & 31) * 56 + 4)) = v52 | 1;
        v53 = *((int *)v44) & 31;
        *((char *)(g_103a3b80[*((int *)v44) >> 5] + v53 * 56 + 36)) = *((char *)(g_103a3b80[*((int *)v44) >> 5] + v53 * 56 + 36)) & 128;
        v23 = v52 | 1;
        v24 = v23 & 72;
        v26 = v52 | 1;
        if ((v23 & 72))
        {
LABEL_103635fa:
            if ((v26 & 128))
            {
                if (!(0x74000 & v29))
                    v29 = (!(v15 & 0x74000) ? v29 | 0x4000 : v29 | v15 & 0x74000);
                v54 = v29 & 0x74000;
                if (v54 != 0x4000)
                {
                    if (v54 != 0x10000 && v54 != 0x14000)
                    {
                        if (v54 == 0x20000 || v54 == 0x24000)
                            goto LABEL_10363669;
                        if (v54 == 0x40000 || v54 == 0x44000)
                            v25 = 1;
                    }
                    else
                    {
                        if (((unsigned short)v29 & 769) == 769)
                        {
LABEL_10363669:
                            v25 = 2;
                        }
                    }
                }
                else
                {
                    v25 = 0;
                }
                if ((v29 & 0x70000) && (v18 = 0, !(v26 & 64)))
                {
                    v55 = v22 & 0xc0000000;
                    if (v55 != 0x40000000)
                    {
                        if (v55 != 0x80000000)
                        {
                            if (v55 == 0xc0000000 && (v56 = v19, v56 > 0) && v56 > 2)
                            {
                                if (v56 > 4)
                                    goto LABEL_103636c1;
                                if (sub_10360587(0xc0000000, v57, *((int *)v44), 0, 0, 2) || v57)
                                {
                                    if ((sub_10360587(v58, v57, *((int *)v44), 0, 0, 0) & v57) == 4294967295)
                                    {
                                        sub_10366e64(*((int *)v44));
                                        sub_103575e0();
                                        return;
                                    }
                                    goto LABEL_103637eb;
                                }
                            }
                        }
                        else
                        {
LABEL_103637eb:
                            v59 = sub_103668a3(*((int *)v44), &v18, 3);
                            if (v59 == 4294967295)
                            {
LABEL_103635ac:
                                sub_10366e64(*((int *)v44));
                                sub_103575e0();
                                return;
                            }
                            if (v59 != 2)
                            {
                                if (v59 != 3)
                                    goto LABEL_103638be;
                                if (v18 != 12565487)
                                    goto LABEL_10363870;
                                v25 = 1;
                            }
                            else
                            {
LABEL_10363870:
                                v60 = v18 & 0xffff;
                                if (v60 == 0xfffe)
                                {
                                    sub_10366e64(*((int *)v44));
                                    v1 = 22;
                                    *((unsigned int *)sub_103575e0()) = 22;
                                    return;
                                }
                                if (v60 == 0xfeff)
                                {
                                    if (sub_10366fc5(*((int *)v44), 2, 0) == 4294967295)
                                    {
                                        sub_10366e64(*((int *)v44));
                                        sub_103575e0();
                                        return;
                                    }
                                    v25 = 2;
                                }
                                else
                                {
LABEL_103638be:
                                    v61 = sub_10366fc5(*((int *)v44), 0, 0);
LABEL_10363862:
                                    if (v61 == 4294967295)
                                    {
                                        sub_10366e64(*((int *)v44));
                                        sub_103575e0();
                                        return;
                                    }
                                }
                            }
                        }
                    }
                    else
                    {
                        v56 = v19;
                        if (v56 > 0)
                        {
                            if (v56 > 2)
                            {
                                if (v56 > 4)
                                {
LABEL_103636c1:
                                    if (v56 == 5)
                                        goto LABEL_103638cc;
                                }
                                else
                                {
                                    if (sub_10360587(0xc0000000, v57, *((int *)v44), 0, 0, 2) || v57)
                                    {
                                        v61 = sub_10360587(v58, v57, *((int *)v44), 0, 0, 0) & v57;
                                        goto LABEL_10363862;
                                    }
                                }
                            }
                            else
                            {
LABEL_103638cc:
                                v62 = v25;
                                v63 = 0;
                                if (v62 != 1)
                                {
                                    if (v62 != 2)
                                        goto LABEL_103636ca;
                                    v18 = 0xfeff;
                                    v19 = 2;
                                }
                                else
                                {
                                    v18 = 12565487;
                                    v19 = 3;
                                }
                                do
                                {
                                    v1 = v19 - v63;
                                    v0 = (char *)&v18 + v63;
                                    if ((unsigned int)sub_10360ce9(*((int *)v44)) == 4294967295)
                                    {
                                        sub_10366e64(*((int *)v44));
                                        v16 = *((int *)sub_103575e0());
                                        return;
                                    }
                                } while ((v63 = (int)(v63 + v64), v19 > v63));
                            }
                        }
                    }
                }
            }
        }
        else if (((v52 | 1) & 128))
        {
            if (((char)v29 & 2))
            {
                v18 = sub_10366fc5(*((int *)v44), -1, 2);
                if (v18 != 4294967295)
                {
                    v13 = 0;
                    if (!sub_103668a3(*((int *)v44), &v13, 1) && (unsigned short)v13 == 26 && sub_103666ef(*((int *)v44), v18, v18 >> 31) == 4294967295 || sub_10366fc5(*((int *)v44), 0, 0) == 4294967295)
                        goto LABEL_103635ac;
                    goto LABEL_103635fa;
                }
                else if (*((int *)sub_103575f3()) != 131)
                {
                    sub_10366e64(*((int *)v44));
                    sub_103575e0();
                    return;
                }
            }
            goto LABEL_103635fa;
        }
LABEL_103636ca:
        v65 = g_103a3b80[*((int *)v44) >> 5] + (*((int *)v44) & 31) * 56 + 36;
        v65->padding_0[0] = v65->padding_0[0] ^ (v65->padding_0[0] ^ v25) & 127;
        v66 = g_103a3b80[*((int *)v44) >> 5] + (*((int *)v44) & 31) * 56 + 36;
        v66->padding_0[0] = (char)(v29 >> 16) * 128 | v66->padding_0[0] & 127;
        if (!v24 && ((char)v29 & 8))
        {
            v67 = g_103a3b80[*((int *)v44) >> 5] + (*((int *)v44) & 31) * 56 + 4;
            v67->padding_0[0] = v67->padding_0[0] | 32;
        }
        if ((v22 & 0xc0000000) != 0xc0000000)
        {
            return;
        }
        else if (((char)v29 & 1))
        {
            g_1038b128(v17);
            v68 = g_1038b194(v28, v22 & 2147483647, v20, &v10, 3, v21, 0);
            if (v68 != 4294967295)
            {
                *((unsigned int *)((*((int *)v44) & 31) * 56 + g_103a3b80[*((int *)v44) >> 5])) = v68;
                return;
            }
            sub_10357606(g_1038b07c());
            v70 = g_103a3b80[*((int *)v44) >> 5] + (*((int *)v44) & 31) * 56 + 4;
            v70->padding_0[0] = v70->padding_0[0] & 254;
            sub_10365096(*((int *)v44));
            sub_103575e0();
            return;
        }
        else
        {
            return;
        }
    }
}
```

## `sub_10363952` `0x10363952`

_153 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a14c8;

void sub_10363952(unsigned int a0)
{
    unsigned int *v15;  // edi
    unsigned int v16;  // eax
    unsigned int v17;  // 4138
    unsigned int v18;  // 4139
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp+0x0]
    int v6;  // [bp+0xfffe4]
    unsigned int v7;  // [bp+0xfffe8]
    unsigned int v8;  // [bp+0x100000]
    int v9;  // [bp+0x10000c]
    int v10;  // [bp+0x100010]
    int v11;  // [bp+0x100014]
    int v12;  // [bp+0x100018]
    unsigned int *v13;  // [bp+0x10001c]
    unsigned int v14;  // [bp+0x100020]

    sub_1035b0cc(&g_103a14c8, 20);
    v7 = 0;
    v15 = v13;
    if (v15)
    {
        *(v15) = 4294967295;
        if (v9 && (!v14 || !((v16 = v12 & 4294966911, v17 = (unsigned int)_ccall(12, 0, (unsigned int)(char)(0 < v16), (unsigned int)(char)(0 < v16)), v18 = (unsigned int)_ccall(4, 18, -((unsigned int)(char)(0 < v16)) + 1, 0, v17), (char)v18))))
        {
            v8 = 0;
            v6 = sub_103631f8(/* unsupported instruction */ - 28, v9, v10, v11, v12);
            v8 = 4294967294;
            sub_103639f0();
            if (v6)
            {
                *(v15) = 4294967295;
                sub_1035b111(&g_103a14c8, 20, v5, a0);
            }
            else
            {
                sub_1035b111(&g_103a14c8, 20, v5, a0);
            }
            return;
        }
    }
    v4 = 22;
    *((unsigned int *)sub_103575e0()) = 22;
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    sub_103535f2();
    sub_1035b111(&g_103a14c8, 20, v5, a0);
    return;
}
```

## `sub_103639eb` `0x103639eb`

_5 bytes. (leaf/helper — see body)_

```c
void sub_103639eb(void)
{
    sub_103639f0();
    return;
}
```

## `sub_103639f0` `0x103639f0`

_46 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a3b80[4];

int sub_103639f0(void)
{
    unsigned int v3;  // esi
    int *v4;  // edi
    unsigned int v5;  // eax
    unsigned int v6;  // eax
    unsigned int v1;  // [bp+0xfffe4]
    unsigned int v2;  // [bp+0xfffe8]

    if (v2 == v3)
        return v6;
    if (v1 == v3)
        return sub_10365228(*(v4));
    v5 = *(v4) & 31;
    *((char *)(g_103a3b80[*(v4) >> 5] + v5 * 56 + 4)) = *((char *)(g_103a3b80[*(v4) >> 5] + v5 * 56 + 4)) & 254;
    return sub_10365228(*(v4));
}
```

## `sub_10363a1e` `0x10363a1e`

_30 bytes. (leaf/helper — see body)_

```c
void sub_10363a1e(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4)
{
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v4 = 1;
    v3 = a0;
    v2 = a4;
    v1 = a3;
    v0 = a2;
    sub_10363952(a1);
    return;
}
```

## `sub_10363a3c` `0x10363a3c`

_271 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

unsigned int sub_10363a3c(unsigned short *a0, unsigned short *a1, unsigned int *a2)
{
    unsigned short *iter;  // ebx
    unsigned int v10;  // edi
    unsigned short *node;  // edi
    unsigned int v12;  // eax
    unsigned int v13;  // eax
    unsigned short v14;  // si
    unsigned int v15;  // eax
    unsigned short v16;  // ax
    unsigned short *v17;  // edi
    unsigned short *v18;  // edi
    unsigned int v0;  // [bp-0x34]
    unsigned int v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x28]
    unsigned int v4;  // [bp-0x24]
    unsigned int v5;  // [bp-0x20]
    struct_0 v6;  // [bp-0x14]
    struct_0 *idx;  // [bp-0xc]
    char v8;  // [bp-0x8]

    sub_103536a7(&v6, a2);
    iter = a0;
    if (!iter)
    {
        v5 = 0;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        *((unsigned int *)sub_103575e0()) = 22;
        sub_103535f2();
        if (!v8)
            return 2147483647;
        idx[8].field_8 = idx[8].field_8 & 4294967293;
        return 2147483647;
    }
    else
    {
        v5 = v10;
        node = a1;
        if (!node)
        {
            v4 = 0;
            v3 = 0;
            v2 = 0;
            v1 = 0;
            v0 = 0;
            *((unsigned int *)sub_103575e0()) = 22;
            sub_103535f2();
            if (v8)
                idx[8].field_8 = idx[8].field_8 & 4294967293;
            v12 = 2147483647;
        }
        else
        {
            if (!*((int *)(v6 + 20)))
            {
                do
                {
                    v13 = *(iter);
                    if ((unsigned short)v13 >= 65 && (unsigned short)v13 <= 90)
                        v13 += 32;
                    v14 = v13;
                    v15 = *(node);
                    if ((unsigned short)v15 >= 65 && (unsigned short)v15 <= 90)
                        v15 += 32;
                    iter += 1;
                    node += 1;
                    v16 = v15;
                } while (v14 && v14 == v16);
            }
            else
            {
                do
                {
                    v17 = node;
                    v14 = sub_10367127(*(iter), &v6);
                    iter += 1;
                    v18 = v17 + 1;
                    v16 = sub_10367127(*(v17), &v6);
                } while (v14 && (node = v18, v14 == v16));
            }
            v12 = v14 - v16;
            if (v8)
                idx[8].field_8 = idx[8].field_8 & 4294967293;
        }
        return v12;
    }
}
```

## `sub_10363b4b` `0x10363b4b`

_145 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a3058;

unsigned int sub_10363b4b(unsigned short *a0, unsigned short *iter)
{
    unsigned short *node;  // edi
    unsigned int v6;  // eax
    unsigned short v7;  // cx
    unsigned int v8;  // eax
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]

    if (g_103a3058)
        return sub_10363a3c(a0, iter, NULL);
    node = a0;
    if (node && iter)
    {
        do
        {
            v6 = *(node);
            if ((unsigned short)v6 >= 65 && (unsigned short)v6 <= 90)
                v6 += 32;
            v7 = v6;
            v8 = *(iter);
            if ((unsigned short)v8 >= 65 && (unsigned short)v8 <= 90)
                v8 += 32;
            node += 1;
            iter += 1;
        } while (v7 && v7 == (unsigned short)v8);
        return v7 - (unsigned short)v8;
    }
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    *((unsigned int *)sub_103575e0()) = 22;
    sub_103535f2();
    return 2147483647;
}
```

## `sub_10363bdc` `0x10363bdc`

_53 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10363bdc(unsigned int a0, unsigned short *a1, unsigned int a2)
{
    unsigned int v0;  // [bp+0xc]

    if (!a2)
        return 0;
    while (true)
    {
        v0 = a2 - 1;
        if (a2 == 1 || !*((short *)a0) || *((short *)a0) != *(a1))
            break;
        a0 += 2;
        a1 += 1;
        a2 = v0;
    }
    return *((short *)a0) - *(a1);
}
```

## `sub_10363c11` `0x10363c11`

_17 bytes. (leaf/helper — see body)_

```c
void sub_10363c11(int a0)
{
    sub_10365800(a0, 0, 10);
    return;
}
```

## `sub_10363c22` `0x10363c22`

_129 bytes. (leaf/helper — see body)_

```c
extern void* g_103a301c;
extern unsigned int g_103a3024;
extern unsigned int g_103a4cd0;

unsigned int sub_10363c22(unsigned int a0)
{
    void* i;  // esi
    unsigned int v3;  // ebx
    unsigned int v4;  // edi
    int v5;  // edi
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    i = g_103a301c;
    if (!g_103a4cd0)
        return 0;
    v1 = v3;
    v0 = v4;
    if (g_103a301c || g_103a3024 && !sub_103672d7() && !((i = g_103a301c, !g_103a301c)))
    {
        if (a0)
        {
            for (v5 = sub_10352f20(a0); *((int *)i); i += 4)
            {
                if (sub_10352f20(*((int *)i)) > v5 && *((char *)(*((int *)i) + v5)) == 61 && !sub_103672c0(*((int *)i), a0, v5))
                    return *((int *)i) + v5 + 1;
            }
        }
    }
    return 0;
}
```

## `sub_10363ca3` `0x10363ca3`

_130 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

extern unsigned int g_1038e2c8;

unsigned int sub_10363ca3(unsigned short a0, unsigned short a1, unsigned int *a2)
{
    struct_0 v0;  // [bp-0x18]
    struct_0 *idx;  // [bp-0x10]
    char v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    if (a0 == 65535)
    {
        v3 = 0;
    }
    else if (a0 < 0x100)
    {
        v3 = *((short *)(g_1038e2c8 + a0 * 2)) & a1;
    }
    else
    {
        sub_103536a7(&v0, a2);
        if (!sub_10367590(&v0, 1, &/* unsupported instruction */, 1, &v3, *((int *)(v0 + 4)), *((int *)(v0 + 20))))
            v3 = 0;
        if (v2)
            idx[8].field_8 = idx[8].field_8 & 4294967293;
    }
    return (unsigned short)v3 & a1;
}
```

## `sub_10363d25` `0x10363d25`

_81 bytes. (leaf/helper — see body)_

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

unsigned int sub_10363d25(unsigned int *a0, char a1, unsigned int a2, char a3)
{
    unsigned int v4;  // eax
    unsigned int v5;  // eax
    struct_0 v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    struct_1 *idx;  // [bp-0xc]
    char v3;  // [bp-0x8]

    sub_103536a7(&v0, a0);
    v4 = a1;
    if ((a3 & *((char *)(v1 + v4 + 29))) || (v5 = (!a2 ? 0 : (unsigned int)(unsigned short)*((short *)(*((int *)(v0 + 200)) + v4 * 2)) & a2), v5))
        v5 = 1;
    if (v3)
        idx->field_70 = idx->field_70 & 4294967293;
    return v5;
}
```

## `sub_10363d76` `0x10363d76`

_19 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10363d76(char a0)
{
    return sub_10363d25(NULL, a0, 0, 4);
}
```

## `sub_10363d89` `0x10363d89`

_240 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

unsigned int sub_10363d89(char *a0, char *a1, int iter, unsigned int *a3)
{
    char *v8;  // edi
    unsigned int v9;  // eax
    int v10;  // esi
    int v11;  // eax
    unsigned int v0;  // [bp-0x34]
    unsigned int v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x28]
    unsigned int v4;  // [bp-0x24]
    struct_0 v5;  // [bp-0x14]
    struct_0 *idx;  // [bp-0xc]
    char v7;  // [bp-0x8]

    if (!iter)
        return 0;
    sub_103536a7(&v5, a3);
    if (a0)
    {
        v8 = a1;
        if (v8)
        {
            if (iter > 2147483647)
            {
                v4 = 0;
                v3 = 0;
                v2 = 0;
                v1 = 0;
                v0 = 0;
                *((unsigned int *)sub_103575e0()) = 22;
                sub_103535f2();
                if (!v7)
                    return 2147483647;
                idx[8].field_8 = idx[8].field_8 & 4294967293;
                return 2147483647;
            }
            else
            {
                if (!*((int *)(v5 + 20)))
                {
                    v9 = sub_103675d0(a0, v8, iter);
                }
                else
                {
                    do
                    {
                        a0 += 1;
                        v10 = sub_10357624(*(a0), &v5);
                        v11 = sub_10357624(*(v8), &v5);
                        v8 += 1;
                        iter -= 1;
                    } while (iter != 1 && v10 && (iter = iter, a0 = a0, v10 == v11));
                    v9 = v10 - v11;
                }
                if (!v7)
                    return v9;
                idx[8].field_8 = idx[8].field_8 & 4294967293;
                return v9;
            }
        }
    }
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    *((unsigned int *)sub_103575e0()) = 22;
    sub_103535f2();
    if (!v7)
        return 2147483647;
    idx[8].field_8 = idx[8].field_8 & 4294967293;
    return 2147483647;
}
```

## `sub_10363e79` `0x10363e79`

_92 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a3058;

unsigned int sub_10363e79(char *a0, char *a1, int a2)
{
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]

    if (g_103a3058)
        return sub_10363d89(a0, a1, a2, NULL);
    if (a0 && a1 && a2 <= 2147483647)
        return sub_103675d0();
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    *((unsigned int *)sub_103575e0()) = 22;
    sub_103535f2();
    return 2147483647;
}
```

## `sub_10363ed5` `0x10363ed5`

_1346 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned short field_0;
    unsigned int field_2;
    char padding_6[4];
    unsigned short field_a;
} struct_0;

extern char g_1038f140;
extern char g_1038f144;
extern int g_1038f148;
extern int g_1038f14c;
extern unsigned int g_1038f150;
extern unsigned int g_1038f154;

unsigned int sub_10363ed5(struct_0 *iter, unsigned int *a1)
{
    unsigned int v13;  // ecx
    int v14;  // ebx
    int v23;  // eax
    int v24;  // eax
    unsigned int v25;  // ecx
    int iter1;  // eax
    unsigned int v27;  // esi
    unsigned int v28;  // edx
    unsigned int *v29;  // ecx
    int v30;  // eax
    unsigned int *iter2;  // edi
    unsigned int v32;  // ecx
    unsigned int v15;  // ebx
    int v33;  // edx
    int v34;  // eax
    unsigned int v35;  // edx
    unsigned int *v36;  // ebx
    int index;  // edx
    char v38[4];  // ecx
    unsigned int v39;  // esi
    int v40;  // ecx
    int v41;  // eax
    int v42;  // edx
    int v16;  // eax
    unsigned int v43;  // edx
    unsigned int *v44;  // ebx
    unsigned int v45;  // ecx
    int v46;  // eax
    unsigned int v47;  // esi
    unsigned int v48;  // edx
    unsigned int *v49;  // ecx
    unsigned int v50;  // edi
    unsigned int v51;  // ecx
    int v52;  // eax
    unsigned int v17;  // eax
    unsigned int *v53;  // ecx
    unsigned int v54;  // esi
    unsigned int v55;  // edi
    int v56;  // eax
    unsigned int *k;  // edi
    unsigned int v58;  // ecx
    unsigned int v59;  // edx
    int v60;  // eax
    unsigned int v61;  // edx
    unsigned int *v62;  // ebx
    unsigned int v18;  // esi
    int idx;  // edx
    char v64[4];  // ecx
    int v65;  // eax
    unsigned int v66;  // edx
    unsigned int *v67;  // ebx
    int idx1;  // edx
    char v69[4];  // ecx
    int v70;  // eax
    unsigned int v71;  // edx
    int idx2;  // edx
    unsigned int v19;  // esi
    char v73[4];  // ecx
    unsigned int v74;  // ebx
    int v20;  // edx
    unsigned int v21;  // edx
    unsigned int *v22;  // edi
    int v0;  // [bp-0x40], Other Possible Types: unsigned int
    unsigned int v1;  // [bp-0x3c]
    unsigned int v2;  // [bp-0x30]
    unsigned int v3;  // [bp-0x2c]
    unsigned int v4;  // [bp-0x28]
    unsigned int v5;  // [bp-0x24]
    unsigned int v6;  // [bp-0x20]
    unsigned int v7;  // [bp-0x1c]
    unsigned int v8;  // [bp-0x18]
    int v9;  // [bp-0x14], Other Possible Types: unsigned int
    int v10;  // [bp-0x10], Other Possible Types: unsigned int
    unsigned int v11;  // [bp-0xc]
    unsigned int node;  // [bp-0x8]

    v13 = *((short *)&iter->padding_6[2]);
    v8 = v13 & 0x8000;
    v5 = *((int *)((char *)&iter->field_2 + 2));
    v14 = (v13 & 0x7fff) - 0x3fff;
    v6 = *((int *)&(&iter->field_0)[1]);
    v7 = iter->field_0 * 0x10000;
    if (v14 == -16383)
    {
        v15 = 0;
        v16 = 0;
        do
        {
            if ((&v5)[v16])
            {
                v5 = 0;
                v6 = 0;
                v1 = 2;
                v7 = 0;
                v17 = v1;
                goto LABEL_103643d4;
            }
        } while ((v16 = (int)(v16 + 1), v16 < 3));
        v17 = 0;
    }
    else
    {
        iter = 0;
        v1 = v18;
        v2 = v5;
        v3 = v6;
        v4 = v7;
        v19 = g_1038f148 - 1;
        v20 = v19 + 1;
        v21 = v20 & 2147483679;
        v9 = v14;
        v10 = v20 + (v20 >> 31 & 31) >> 5;
        if ((v20 & 2147483679) < 0)
            v21 = (v21 - 1 | 0xffffffe0) + 1;
        v22 = &(&v5)[v10];
        v0 = 31;
        v11 = v0 - v21;
        if ((1 << ((char)v11 & 31) & *(v22)))
        {
            v23 = v10;
            if (!(~(4294967295 << ((char)v11 & 31)) & (&v5)[v23]))
            {
                do
                {
                    if (v23 + 1 >= 3)
                        goto LABEL_1036401d;
                } while ((v23 = v24, !(&v5)[v23]));
            }
            v0 = 31;
            v25 = v0;
            iter1 = v19 + (v19 >> 31 & v25) >> 5;
            v27 = v19 & 2147483679;
            if ((v19 & 2147483679) < 0)
                v27 = (v27 - 1 | 0xffffffe0) + 1;
            node = 0;
            v28 = 1 << ((char)(v25 - v27) & 31);
            v29 = &(&v5)[iter1];
            iter = *(v29) + v28;
            if (iter >= *(v29))
                if (iter < v28)
                    goto LABEL_10364008;
                else
                    goto LABEL_1036400f;
            while (true)
            {
LABEL_10364008:
                node = 1;
                do
                {
LABEL_1036400f:
                    iter1 -= 1;
                    *(v29) = iter;
                    if (iter1 - 1 < 0 || !node)
                    {
                        iter = node;
                        goto LABEL_1036401d;
                    }
                } while ((node = 0, v29 = &v5 + iter1 * 4, iter = *(v29) + 1, iter >= *(v29) && !((iter1 = iter1, iter < 1))));
            }
        }
LABEL_1036401d:
        *(v22) = *(v22) & 4294967295 << ((char)v11 & 31);
        v30 = v10 + 1;
        if (v30 < 3)
        {
            v0 = 3;
            iter2 = &(&v5)[v30];
            for (v32 = v0 - v30; v32; iter2 += 1)
            {
                v32 -= 1;
                *(iter2) = 0;
            }
        }
        if (iter)
            v14 += 1;
        if (v14 < *((int *)&g_1038f144) - g_1038f148)
        {
            v5 = 0;
            v6 = 0;
            v7 = 0;
            goto LABEL_1036426f;
        }
        else if (v14 <= *((int *)&g_1038f144))
        {
            v5 = v2;
            v6 = v3;
            v33 = *((int *)&g_1038f144) - v9;
            v34 = v33 + (v33 >> 31 & 31) >> 5;
            v35 = v33 & 2147483679;
            v7 = v4;
            if ((v33 & 2147483679) < 0)
                v35 = (v35 - 1 | 0xffffffe0) + 1;
            v10 = 0;
            iter = 0;
            node = 32;
            node -= v35;
            do
            {
                v36 = &(&v5)[iter];
                v9 = *(v36) & ~(4294967295 << ((char)v35 & 31));
                *(v36) = *(v36) >> ((char)v35 & 31) | v10;
                iter += 1;
                v10 = v9 << ((char)node & 31);
            } while (iter < 3);
            v0 = 2;
            index = v0;
            v38 = &(&v7)[-1 * v34];
            do
            {
                if (index >= v34)
                    *((char [4])&(&v5)[index]) = *(v38);
                else
                    (&v5)[index] = 0;
            } while ((index = (int)(index - 1), v38 -= 4, index >= 0));
            v39 = g_1038f148 - 1;
            v40 = v39 + 1;
            v41 = v40 + (v40 >> 31 & 31) >> 5;
            v42 = v40;
            v43 = v42 & 2147483679;
            v10 = v41;
            if ((v42 & 2147483679) < 0)
                v43 = (v43 - 1 | 0xffffffe0) + 1;
            v0 = 31;
            v44 = &(&v5)[v41];
            v9 = v0 - v43;
            if ((1 << ((char)v9 & 31) & *(v44)))
            {
                if (!(~(4294967295 << ((char)v9 & 31)) & (&v5)[v41]))
                {
                    do
                    {
                        v41 += 1;
                    } while (!(&v5)[v41]);
                    if (v41 >= 3)
                        goto LABEL_103641c0;
                }
                v0 = 31;
                v45 = v0;
                v46 = v39 + (v39 >> 31 & v45) >> 5;
                v47 = v39 & 2147483679;
                if ((v39 & 2147483679) < 0)
                    v47 = (v47 - 1 | 0xffffffe0) + 1;
                iter = 0;
                v48 = 1 << ((char)(v45 - v47) & 31);
                v49 = &(&v5)[v46];
                v50 = *(v49) + v48;
                if (v50 < *(v49) || v50 < v48)
                    iter = 1;
                *(v49) = v50;
                v51 = iter;
                while (true)
                {
                    v52 = v46 - 1;
                    if (v46 - 1 < 0 || !v51)
                        break;
                    v53 = &(&v5)[v52];
                    v54 = *(v53) + 1;
                    v55 = 0;
                    if (v54 < *(v53) || v54 < 1)
                        v55 = 1;
                    *(v53) = v54;
                    v51 = v55;
                    v46 = v52;
                }
            }
LABEL_103641c0:
            *(v44) = *(v44) & 4294967295 << ((char)v9 & 31);
            v56 = v10 + 1;
            if (v56 < 3)
            {
                v0 = 3;
                k = &(&v5)[v56];
                for (v58 = v0 - v56; v58; k += 1)
                {
                    v58 -= 1;
                    *(k) = 0;
                }
            }
            v59 = g_1038f14c + 1;
            v60 = v59 + (v59 >> 31 & 31) >> 5;
            v61 = v59 & 2147483679;
            if ((v59 & 2147483679) < 0)
                v61 = (v61 - 1 | 0xffffffe0) + 1;
            v10 = 0;
            iter = 0;
            node = 32;
            node -= v61;
            do
            {
                v62 = &(&v5)[iter];
                v9 = *(v62) & ~(4294967295 << ((char)v61 & 31));
                *(v62) = *(v62) >> ((char)v61 & 31) | v10;
                iter += 1;
                v10 = v9 << ((char)node & 31);
            } while (iter < 3);
            v0 = 2;
            idx = v0;
            v64 = &(&v7)[-1 * v60];
            do
            {
                if (idx >= v60)
                    *((char [4])&(&v5)[idx]) = *(v64);
                else
                    (&v5)[idx] = 0;
            } while ((idx = (int)(idx - 1), v64 -= 4, idx >= 0));
LABEL_1036426f:
            v0 = 2;
            v15 = 0;
            v17 = v0;
        }
        else if (v14 >= *((int *)&g_1038f140))
        {
            v5 = 0;
            v6 = 0;
            v7 = 0;
            v5 |= 0x80000000;
            v65 = g_1038f14c + (g_1038f14c >> 31 & 31) >> 5;
            v66 = g_1038f14c & 2147483679;
            if ((g_1038f14c & 2147483679) < 0)
                v66 = (v66 - 1 | 0xffffffe0) + 1;
            v10 = 0;
            iter = 0;
            node = 32;
            node -= v66;
            do
            {
                v67 = &(&v5)[iter];
                v9 = *(v67) & ~(4294967295 << ((char)v66 & 31));
                *(v67) = *(v67) >> ((char)v66 & 31) | v10;
                iter += 1;
                v10 = v9 << ((char)node & 31);
            } while (iter < 3);
            v0 = 2;
            idx1 = v0;
            v69 = &(&v7)[-1 * v65];
            do
            {
                if (idx1 >= v65)
                    *((char [4])&(&v5)[idx1]) = *(v69);
                else
                    (&v5)[idx1] = 0;
            } while ((idx1 = (int)(idx1 - 1), v69 -= 4, idx1 >= 0));
            v15 = g_1038f154 + *((int *)&g_1038f140);
            v17 = 1;
        }
        else
        {
            v5 &= 2147483647;
            v15 = v14 + g_1038f154;
            v70 = g_1038f14c + (g_1038f14c >> 31 & 31) >> 5;
            v71 = g_1038f14c & 2147483679;
            if ((g_1038f14c & 2147483679) < 0)
                v71 = (v71 - 1 | 0xffffffe0) + 1;
            v10 = 0;
            iter = 0;
            node = 32;
            node -= v71;
            do
            {
                v9 = (&v5)[iter] & ~(4294967295 << ((char)v71 & 31));
                (&v5)[iter] = (&v5)[iter] >> ((char)v71 & 31) | v10;
                iter += 1;
                v10 = v9 << ((char)node & 31);
            } while (iter < 3);
            v0 = 2;
            idx2 = v0;
            v73 = &(&v7)[-1 * v70];
            do
            {
                if (idx2 >= v70)
                    *((char [4])&(&v5)[idx2]) = *(v73);
                else
                    (&v5)[idx2] = 0;
            } while ((idx2 = (int)(idx2 - 1), v73 -= 4, idx2 >= 0));
            v17 = 0;
        }
    }
LABEL_103643d4:
    v1 = 31;
    v74 = v15 << ((char)(v1 - g_1038f14c) & 31) | -(0 < v8) & 0x80000000 | v5;
    if (g_1038f150 == 64)
    {
        a1[1] = v74;
        *(a1) = v6;
        return v17;
    }
    if (g_1038f150 != 32)
        return v17;
    *(a1) = v74;
    return v17;
}
```

## `sub_10364417` `0x10364417`

_1346 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned short field_0;
    unsigned int field_2;
    char padding_6[4];
    unsigned short field_a;
} struct_0;

extern char g_1038f158;
extern char g_1038f15c;
extern int g_1038f160;
extern int g_1038f164;
extern unsigned int g_1038f168;
extern unsigned int g_1038f16c;

unsigned int sub_10364417(struct_0 *iter, unsigned int *a1)
{
    unsigned int v13;  // ecx
    int v14;  // ebx
    int v23;  // eax
    int v24;  // eax
    unsigned int v25;  // ecx
    int iter1;  // eax
    unsigned int v27;  // esi
    unsigned int v28;  // edx
    unsigned int *v29;  // ecx
    int v30;  // eax
    unsigned int *iter2;  // edi
    unsigned int v32;  // ecx
    unsigned int v15;  // ebx
    int v33;  // edx
    int v34;  // eax
    unsigned int v35;  // edx
    unsigned int *v36;  // ebx
    int index;  // edx
    char v38[4];  // ecx
    unsigned int v39;  // esi
    int v40;  // ecx
    int v41;  // eax
    int v42;  // edx
    int v16;  // eax
    unsigned int v43;  // edx
    unsigned int *v44;  // ebx
    unsigned int v45;  // ecx
    int v46;  // eax
    unsigned int v47;  // esi
    unsigned int v48;  // edx
    unsigned int *v49;  // ecx
    unsigned int v50;  // edi
    unsigned int v51;  // ecx
    int v52;  // eax
    unsigned int v17;  // eax
    unsigned int *v53;  // ecx
    unsigned int v54;  // esi
    unsigned int v55;  // edi
    int v56;  // eax
    unsigned int *k;  // edi
    unsigned int v58;  // ecx
    unsigned int v59;  // edx
    int v60;  // eax
    unsigned int v61;  // edx
    unsigned int *v62;  // ebx
    unsigned int v18;  // esi
    int idx;  // edx
    char v64[4];  // ecx
    int v65;  // eax
    unsigned int v66;  // edx
    unsigned int *v67;  // ebx
    int idx1;  // edx
    char v69[4];  // ecx
    int v70;  // eax
    unsigned int v71;  // edx
    int idx2;  // edx
    unsigned int v19;  // esi
    char v73[4];  // ecx
    unsigned int v74;  // ebx
    int v20;  // edx
    unsigned int v21;  // edx
    unsigned int *v22;  // edi
    int v0;  // [bp-0x40], Other Possible Types: unsigned int
    unsigned int v1;  // [bp-0x3c]
    unsigned int v2;  // [bp-0x30]
    unsigned int v3;  // [bp-0x2c]
    unsigned int v4;  // [bp-0x28]
    unsigned int v5;  // [bp-0x24]
    unsigned int v6;  // [bp-0x20]
    unsigned int v7;  // [bp-0x1c]
    unsigned int v8;  // [bp-0x18]
    int v9;  // [bp-0x14], Other Possible Types: unsigned int
    int v10;  // [bp-0x10], Other Possible Types: unsigned int
    unsigned int v11;  // [bp-0xc]
    unsigned int node;  // [bp-0x8]

    v13 = *((short *)&iter->padding_6[2]);
    v8 = v13 & 0x8000;
    v5 = *((int *)((char *)&iter->field_2 + 2));
    v14 = (v13 & 0x7fff) - 0x3fff;
    v6 = *((int *)&(&iter->field_0)[1]);
    v7 = iter->field_0 * 0x10000;
    if (v14 == -16383)
    {
        v15 = 0;
        v16 = 0;
        do
        {
            if ((&v5)[v16])
            {
                v5 = 0;
                v6 = 0;
                v1 = 2;
                v7 = 0;
                v17 = v1;
                goto LABEL_10364916;
            }
        } while ((v16 = (int)(v16 + 1), v16 < 3));
        v17 = 0;
    }
    else
    {
        iter = 0;
        v1 = v18;
        v2 = v5;
        v3 = v6;
        v4 = v7;
        v19 = g_1038f160 - 1;
        v20 = v19 + 1;
        v21 = v20 & 2147483679;
        v9 = v14;
        v10 = v20 + (v20 >> 31 & 31) >> 5;
        if ((v20 & 2147483679) < 0)
            v21 = (v21 - 1 | 0xffffffe0) + 1;
        v22 = &(&v5)[v10];
        v0 = 31;
        v11 = v0 - v21;
        if ((1 << ((char)v11 & 31) & *(v22)))
        {
            v23 = v10;
            if (!(~(4294967295 << ((char)v11 & 31)) & (&v5)[v23]))
            {
                do
                {
                    if (v23 + 1 >= 3)
                        goto LABEL_1036455f;
                } while ((v23 = v24, !(&v5)[v23]));
            }
            v0 = 31;
            v25 = v0;
            iter1 = v19 + (v19 >> 31 & v25) >> 5;
            v27 = v19 & 2147483679;
            if ((v19 & 2147483679) < 0)
                v27 = (v27 - 1 | 0xffffffe0) + 1;
            node = 0;
            v28 = 1 << ((char)(v25 - v27) & 31);
            v29 = &(&v5)[iter1];
            iter = *(v29) + v28;
            if (iter >= *(v29))
                if (iter < v28)
                    goto LABEL_1036454a;
                else
                    goto LABEL_10364551;
            while (true)
            {
LABEL_1036454a:
                node = 1;
                do
                {
LABEL_10364551:
                    iter1 -= 1;
                    *(v29) = iter;
                    if (iter1 - 1 < 0 || !node)
                    {
                        iter = node;
                        goto LABEL_1036455f;
                    }
                } while ((node = 0, v29 = &v5 + iter1 * 4, iter = *(v29) + 1, iter >= *(v29) && !((iter1 = iter1, iter < 1))));
            }
        }
LABEL_1036455f:
        *(v22) = *(v22) & 4294967295 << ((char)v11 & 31);
        v30 = v10 + 1;
        if (v30 < 3)
        {
            v0 = 3;
            iter2 = &(&v5)[v30];
            for (v32 = v0 - v30; v32; iter2 += 1)
            {
                v32 -= 1;
                *(iter2) = 0;
            }
        }
        if (iter)
            v14 += 1;
        if (v14 < *((int *)&g_1038f15c) - g_1038f160)
        {
            v5 = 0;
            v6 = 0;
            v7 = 0;
            goto LABEL_103647b1;
        }
        else if (v14 <= *((int *)&g_1038f15c))
        {
            v5 = v2;
            v6 = v3;
            v33 = *((int *)&g_1038f15c) - v9;
            v34 = v33 + (v33 >> 31 & 31) >> 5;
            v35 = v33 & 2147483679;
            v7 = v4;
            if ((v33 & 2147483679) < 0)
                v35 = (v35 - 1 | 0xffffffe0) + 1;
            v10 = 0;
            iter = 0;
            node = 32;
            node -= v35;
            do
            {
                v36 = &(&v5)[iter];
                v9 = *(v36) & ~(4294967295 << ((char)v35 & 31));
                *(v36) = *(v36) >> ((char)v35 & 31) | v10;
                iter += 1;
                v10 = v9 << ((char)node & 31);
            } while (iter < 3);
            v0 = 2;
            index = v0;
            v38 = &(&v7)[-1 * v34];
            do
            {
                if (index >= v34)
                    *((char [4])&(&v5)[index]) = *(v38);
                else
                    (&v5)[index] = 0;
            } while ((index = (int)(index - 1), v38 -= 4, index >= 0));
            v39 = g_1038f160 - 1;
            v40 = v39 + 1;
            v41 = v40 + (v40 >> 31 & 31) >> 5;
            v42 = v40;
            v43 = v42 & 2147483679;
            v10 = v41;
            if ((v42 & 2147483679) < 0)
                v43 = (v43 - 1 | 0xffffffe0) + 1;
            v0 = 31;
            v44 = &(&v5)[v41];
            v9 = v0 - v43;
            if ((1 << ((char)v9 & 31) & *(v44)))
            {
                if (!(~(4294967295 << ((char)v9 & 31)) & (&v5)[v41]))
                {
                    do
                    {
                        v41 += 1;
                    } while (!(&v5)[v41]);
                    if (v41 >= 3)
                        goto LABEL_10364702;
                }
                v0 = 31;
                v45 = v0;
                v46 = v39 + (v39 >> 31 & v45) >> 5;
                v47 = v39 & 2147483679;
                if ((v39 & 2147483679) < 0)
                    v47 = (v47 - 1 | 0xffffffe0) + 1;
                iter = 0;
                v48 = 1 << ((char)(v45 - v47) & 31);
                v49 = &(&v5)[v46];
                v50 = *(v49) + v48;
                if (v50 < *(v49) || v50 < v48)
                    iter = 1;
                *(v49) = v50;
                v51 = iter;
                while (true)
                {
                    v52 = v46 - 1;
                    if (v46 - 1 < 0 || !v51)
                        break;
                    v53 = &(&v5)[v52];
                    v54 = *(v53) + 1;
                    v55 = 0;
                    if (v54 < *(v53) || v54 < 1)
                        v55 = 1;
                    *(v53) = v54;
                    v51 = v55;
                    v46 = v52;
                }
            }
LABEL_10364702:
            *(v44) = *(v44) & 4294967295 << ((char)v9 & 31);
            v56 = v10 + 1;
            if (v56 < 3)
            {
                v0 = 3;
                k = &(&v5)[v56];
                for (v58 = v0 - v56; v58; k += 1)
                {
                    v58 -= 1;
                    *(k) = 0;
                }
            }
            v59 = g_1038f164 + 1;
            v60 = v59 + (v59 >> 31 & 31) >> 5;
            v61 = v59 & 2147483679;
            if ((v59 & 2147483679) < 0)
                v61 = (v61 - 1 | 0xffffffe0) + 1;
            v10 = 0;
            iter = 0;
            node = 32;
            node -= v61;
            do
            {
                v62 = &(&v5)[iter];
                v9 = *(v62) & ~(4294967295 << ((char)v61 & 31));
                *(v62) = *(v62) >> ((char)v61 & 31) | v10;
                iter += 1;
                v10 = v9 << ((char)node & 31);
            } while (iter < 3);
            v0 = 2;
            idx = v0;
            v64 = &(&v7)[-1 * v60];
            do
            {
                if (idx >= v60)
                    *((char [4])&(&v5)[idx]) = *(v64);
                else
                    (&v5)[idx] = 0;
            } while ((idx = (int)(idx - 1), v64 -= 4, idx >= 0));
LABEL_103647b1:
            v0 = 2;
            v15 = 0;
            v17 = v0;
        }
        else if (v14 >= *((int *)&g_1038f158))
        {
            v5 = 0;
            v6 = 0;
            v7 = 0;
            v5 |= 0x80000000;
            v65 = g_1038f164 + (g_1038f164 >> 31 & 31) >> 5;
            v66 = g_1038f164 & 2147483679;
            if ((g_1038f164 & 2147483679) < 0)
                v66 = (v66 - 1 | 0xffffffe0) + 1;
            v10 = 0;
            iter = 0;
            node = 32;
            node -= v66;
            do
            {
                v67 = &(&v5)[iter];
                v9 = *(v67) & ~(4294967295 << ((char)v66 & 31));
                *(v67) = *(v67) >> ((char)v66 & 31) | v10;
                iter += 1;
                v10 = v9 << ((char)node & 31);
            } while (iter < 3);
            v0 = 2;
            idx1 = v0;
            v69 = &(&v7)[-1 * v65];
            do
            {
                if (idx1 >= v65)
                    *((char [4])&(&v5)[idx1]) = *(v69);
                else
                    (&v5)[idx1] = 0;
            } while ((idx1 = (int)(idx1 - 1), v69 -= 4, idx1 >= 0));
            v15 = g_1038f16c + *((int *)&g_1038f158);
            v17 = 1;
        }
        else
        {
            v5 &= 2147483647;
            v15 = v14 + g_1038f16c;
            v70 = g_1038f164 + (g_1038f164 >> 31 & 31) >> 5;
            v71 = g_1038f164 & 2147483679;
            if ((g_1038f164 & 2147483679) < 0)
                v71 = (v71 - 1 | 0xffffffe0) + 1;
            v10 = 0;
            iter = 0;
            node = 32;
            node -= v71;
            do
            {
                v9 = (&v5)[iter] & ~(4294967295 << ((char)v71 & 31));
                (&v5)[iter] = (&v5)[iter] >> ((char)v71 & 31) | v10;
                iter += 1;
                v10 = v9 << ((char)node & 31);
            } while (iter < 3);
            v0 = 2;
            idx2 = v0;
            v73 = &(&v7)[-1 * v70];
            do
            {
                if (idx2 >= v70)
                    *((char [4])&(&v5)[idx2]) = *(v73);
                else
                    (&v5)[idx2] = 0;
            } while ((idx2 = (int)(idx2 - 1), v73 -= 4, idx2 >= 0));
            v17 = 0;
        }
    }
LABEL_10364916:
    v1 = 31;
    v74 = v15 << ((char)(v1 - g_1038f164) & 31) | -(0 < v8) & 0x80000000 | v5;
    if (g_1038f168 == 64)
    {
        a1[1] = v74;
        *(a1) = v6;
        return v17;
    }
    if (g_1038f168 != 32)
        return v17;
    *(a1) = v74;
    return v17;
}
```

## `sub_10364959` `0x10364959`

_1680 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
} struct_0;

typedef struct struct_1 {
    unsigned short field_0;
    unsigned int field_2;
    unsigned int field_6;
    unsigned short field_a;
} struct_1;

extern unsigned int g_1038e180;

int sub_10364959(struct_1 *idx, struct_0 **a1, char *a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7)
{
    unsigned int v32;  // ebx
    unsigned int iter;  // esi
    unsigned int v34;  // edi
    char *v35;  // edi
    char *v36;  // edx
    char v37;  // al
    unsigned int v0;  // [bp-0xa0]
    unsigned int v1;  // [bp-0x9c]
    unsigned int v2;  // [bp-0x98]
    unsigned int v3;  // [bp-0x94]
    unsigned int v4;  // [bp-0x90]
    unsigned int v5;  // [bp-0x8c]
    unsigned int v6;  // [bp-0x88]
    unsigned int v7;  // [bp-0x84]
    unsigned int v9;  // [bp-0x78]
    struct_0 **v10;  // [bp-0x74]
    unsigned int v11;  // [bp-0x70]
    int v12;  // [bp-0x6c]
    int v13;  // [bp-0x68]
    unsigned int v14;  // [bp-0x64]
    unsigned int v15;  // [bp-0x60]
    unsigned int v16;  // [bp-0x5c]
    char *v17;  // [bp-0x58]
    unsigned int v18;  // [bp-0x54]
    int v19;  // [bp-0x50]
    char v28;  // [bp-0x30]
    unsigned int v30;  // [bp-0x8]
    char v31;  // [bp-0x4]

    v30 = g_1038e180 ^ &v31;
    v7 = v32;
    v6 = iter;
    v5 = v34;
    v10 = a1;
    v35 = &v28 + 12;
    v9 = 0;
    v12 = 1;
    v19 = 0;
    v16 = 0;
    v15 = 0;
    v14 = 0;
    v13 = 0;
    v18 = 0;
    v11 = 0;
    if (!a7)
    {
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        *((unsigned int *)sub_103575e0()) = 22;
        sub_103535f2();
        return sub_10351225();
    }
    v36 = a2;
    v17 = v36;
    while (true)
    {
        v37 = *(v36);
        if (*(v36) != 32 && v37 != 9 && v37 != 10 && v37 != 13)
            break;
        v36 += 1;
    }
    v36 += 1;
}
```

## `sub_10365019` `0x10365019`

_125 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b190;
extern unsigned int g_103a3054;
extern char g_103a3b70;
extern unsigned int g_103a3b80[4];

unsigned int sub_10365019(int a0, unsigned int a1)
{
    unsigned int v5;  // esi
    unsigned int v6;  // edi
    unsigned int v7;  // esi
    unsigned int *v8;  // edi
    unsigned int v9;  // ebx
    unsigned int v10;  // ebx
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]
    unsigned int v4;  // [bp-0x4]

    v4 = v5;
    v3 = v6;
    if (a0 >= 0 && a0 < *((int *)&g_103a3b70))
    {
        v7 = (a0 & 31) * 56;
        v8 = &g_103a3b80[a0 >> 5];
        if (*((int *)(v7 + *(v8))) == 4294967295)
        {
            v2 = v9;
            v10 = a1;
            if (g_103a3054 != 1)
            {
                *((unsigned int *)(v7 + *(v8))) = v10;
                return 0;
            }
            if (!a0)
            {
                v1 = v10;
                v0 = 4294967286;
                v1 = v10;
            }
            else if (a0 == 1)
            {
                v1 = v10;
                v0 = 4294967285;
                v1 = v10;
            }
            else if (a0 == 2)
            {
                v1 = v10;
                v0 = 4294967284;
                v1 = v10;
            }
            else
            {
                *((unsigned int *)(v7 + *(v8))) = v10;
                return 0;
            }
            g_1038b190(v0, v1);
            *((unsigned int *)(v7 + *(v8))) = v10;
            return 0;
        }
    }
    *((unsigned int *)sub_103575e0()) = 9;
    *((unsigned int *)sub_103575f3()) = 0;
    return 4294967295;
}
```

## `sub_10365096` `0x10365096`

_129 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    char field_4;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b190;
extern unsigned int g_103a3054;
extern char g_103a3b70;
extern unsigned int g_103a3b80[4];

unsigned int sub_10365096(int a0)
{
    unsigned int v5;  // ebx
    unsigned int v6;  // esi
    unsigned int v7;  // edi
    unsigned int v8;  // esi
    unsigned int *v9;  // edi
    struct_0 *v10;  // eax
    int v11;  // ecx
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]
    unsigned int v4;  // [bp-0x4]

    v4 = v5;
    v3 = v6;
    v2 = v7;
    if (a0 >= 0 && a0 < *((int *)&g_103a3b70))
    {
        v8 = (a0 & 31) * 56;
        v9 = &g_103a3b80[a0 >> 5];
        v10 = *(v9) + v8;
        if ((v10->field_4 & 1) && v10->field_0 != 4294967295)
        {
            if (g_103a3054 == 1)
            {
                v11 = a0 - 0;
                if (!a0)
                {
                    v1 = 0;
                    v0 = 4294967286;
                }
                else if (v11 == 1)
                {
                    v1 = 0;
                    v0 = 4294967285;
                }
                else if (v11 == 2)
                {
                    v1 = 0;
                    v0 = 4294967284;
                }
                else
                {
                    *((unsigned int *)(v8 + *(v9))) = 4294967295;
                    return 0;
                }
                g_1038b190(v0, v1);
                *((unsigned int *)(v8 + *(v9))) = 4294967295;
                return 0;
            }
            else
            {
                *((unsigned int *)(v8 + *(v9))) = 4294967295;
                return 0;
            }
        }
    }
    *((unsigned int *)sub_103575e0()) = 9;
    *((unsigned int *)sub_103575f3()) = 0;
    return 4294967295;
}
```

