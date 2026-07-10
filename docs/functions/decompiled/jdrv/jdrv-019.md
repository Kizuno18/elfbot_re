# elfbot.dll decompiled — jdrv 0x1003c9a6..0x10040a76

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1003c9a6` `0x1003c9a6`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003c9a6(void)
{
}
```

## `sub_1003c9bd` `0x1003c9bd`

_70 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
} struct_0;

extern unsigned int g_10052768;
extern unsigned int g_1005276c;
extern int g_10052770;

struct_0 ** sub_1003c9bd(int a0, int a1)
{
    struct_0 **v0;  // eax

    if (a0 - g_10052768 + 8 >= 18)
    {
        return NULL;
    }
    else if (a1 - g_1005276c + 6 >= 14)
    {
        return NULL;
    }
    else
    {
        v0 = sub_1003a03f(a0, a1, g_10052770);
        if (!v0)
            return v0;
        return *(v0);
    }
}
```

## `sub_1003ca03` `0x1003ca03`

_1460 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    char field_3;
    char padding_4[32];
    char padding_25[1];
    unsigned short field_24;
    char padding_26[2];
    unsigned short field_28;
    char padding_2a[2];
    char field_2c;
} struct_0;

extern unsigned int g_10052768;
extern unsigned int g_1005276c;
extern char g_10052770;
extern char g_10053200;
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern void* g_10080bb3;
extern unsigned int g_10080bb7;
extern void* g_10080bcb;
extern unsigned int g_10080bcf;
extern unsigned int g_100f9328;
extern unsigned int g_100f94cb;
extern char g_1014f41e;
extern char g_1014f41f;

int sub_1003ca03(void)
{
    unsigned int i[13];  // ebx
    unsigned int v38[13];  // ebx
    unsigned long v47;  // ldt
    unsigned long v48;  // gdt
    unsigned short v49;  // ss
    unsigned long v50;  // 4121
    int v51;  // ecx
    int v52;  // ecx
    int v53;  // ecx
    int v54;  // eax
    int v55;  // ebx
    unsigned long v56;  // 4121
    unsigned int v39[13];  // ebx
    unsigned int v57;  // ebx
    unsigned int v58;  // esi
    unsigned int v59;  // ebx
    unsigned int v60;  // eax
    unsigned int v61;  // edi
    unsigned int v62;  // edx
    unsigned int v63;  // eax
    unsigned int v64;  // ecx
    unsigned int v65;  // eax
    unsigned int v66;  // ecx
    unsigned int idx[13];  // ebx
    unsigned int v67;  // ebx
    unsigned long v68;  // 4166
    unsigned long v69;  // 4170
    unsigned int v70;  // eax
    unsigned int v71;  // eax
    unsigned int v41;  // eax
    unsigned int v42;  // ecx
    unsigned int index[13];  // ebx
    unsigned int v44;  // eax
    unsigned int v45;  // ecx
    int v46;  // ecx
    unsigned int v0;  // [bp-0x8ec]
    unsigned int v1;  // [bp-0x8e8]
    char *v2;  // [bp-0x8e4]
    char *v3;  // [bp-0x8e0]
    unsigned int v4;  // [bp-0x8dc]
    unsigned int v5;  // [bp-0x8d8]
    unsigned int v6;  // [bp-0x8d4]
    unsigned int v7[13];  // [bp-0x8d0], Other Possible Types: int, unsigned int
    unsigned int v8;  // [bp-0x8cc]
    struct_0 v9;  // [bp-0x8c4]
    unsigned int v10;  // [bp-0x8a0]
    unsigned int v11;  // [bp-0x89c]
    unsigned int v12;  // [bp-0x898]
    unsigned int v13;  // [bp-0x81c]
    unsigned int v14;  // [bp-0x818]
    unsigned int v15;  // [bp-0x814]
    unsigned int v16;  // [bp-0x814]
    unsigned int v17;  // [bp-0x810]
    unsigned int v18;  // [bp-0x810]
    unsigned int v19;  // [bp-0x80c]
    unsigned int v20;  // [bp-0x808]
    unsigned int v21;  // [bp-0x804]
    unsigned int iter1;  // [bp-0x800]
    unsigned int iter;  // [bp-0x7fc]
    unsigned int node;  // [bp-0x7f8]
    unsigned int m;  // [bp-0x7f4]
    unsigned int iter2;  // [bp-0x7f0]
    char v27[506];  // [bp-0x7ec]
    char v28[506];  // [bp-0x5f2]
    char v29[253];  // [bp-0x3f8]
    char v30[253];  // [bp-0x2fb]
    char v31[116];  // [bp-0x1fe]
    char v32;  // [bp-0x18a]
    char v33[116];  // [bp-0x101]
    char v34;  // [bp-0x8d]
    char v35;  // [bp-0x4]

    sub_10024fae();
    if (g_10080bcb && g_10080bcf && g_1014f41f && sub_1003bc09(g_10080bcb))
    {
        g_100f9328 = 1;
        sub_1003a60a(g_10080bcb, g_100f94cb);
        return;
    }
    if (g_10080bb7 && g_10080bb3 && g_1014f41e && sub_1003bc09(g_10080bb3))
    {
        g_100f9328 = 1;
        sub_1003a60a(g_10080bb3, g_100f94cb);
        return;
    }
    sub_1002ae81(v33, 253);
    sub_1002ae81(v31, 253);
    sub_1002ae81(v30, 253);
    sub_1002ae81(v29, 253);
    sub_1002ae81(v28, 506);
    v8 = 506;
    sub_1002ae81(v27, 506);
    for (i = 0x63fef8; i < 0x64a308; i = &v38[3 + 3])
    {
        v38 = i;
        if ((char)v38[2 + 10])
        {
            v38 = i;
            if (v38[11] == *((int *)&g_10052770))
            {
                v7 = i;
                v39 = i;
                v38 = v39;
                if (!sub_10011a89(i[9], i[10]))
                {
                    idx = &v39[1];
                    if (sub_1003a320((unsigned int [13])&v39[1], v39))
                    {
                        v41 = idx[9] - g_1005f854 + 8;
                        v42 = idx[10] - g_1005f858 + 6;
                        v38 = idx;
                        if (v41 < 18)
                        {
                            v38 = idx;
                            if (v42 < 14)
                            {
                                v34 += 1;
                                v38 = idx;
                            }
                        }
                    }
                    else
                    {
                        index = &idx[1];
                        v38 = index;
                        if (sub_1003a494((unsigned int [13])&idx[1], idx))
                        {
                            v44 = index[9] - g_1005f854 + 8;
                            v45 = index[10] - g_1005f858 + 6;
                            v38 = index;
                            if (v44 < 18)
                            {
                                v38 = index;
                                if (v45 < 14)
                                {
                                    v32 += 1;
                                    v38 = index;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    for (iter = 0; iter < 14; iter += 1)
    {
        v46 = g_1005276c - 6 + iter;
        node = 0;
        while (node < 18)
        {
            v7 = v46;
            if (sub_1003c87c(g_10052768 - 8 + node, v46))
            {
                v50 = _ccall(v47, v48, (unsigned int)v49, v29 + iter * 18 + node);
                *((char *)v50) = 1;
                node += 1;
            }
            else
            {
                node += 1;
            }
        }
    }
    for (iter = 0; iter < 14; iter += 1)
    {
        v51 = g_1005276c - 6 + iter;
        node = 0;
        while (true)
        {
            v52 = v51;
            if (node >= 18)
                break;
            v7 = v52;
            v53 = v52;
            if (sub_10011678(g_10052768 - 8 + node, v52, v29))
            {
                v54 = node + g_10052768 - 8;
                v55 = iter + g_1005276c - 6;
                v7 = v53;
                v6 = node + g_10052768 - 8;
                v5 = iter + g_1005276c - 6;
                v51 = v53;
                if (sub_1003c9bd(v54, v55))
                {
                    v7 = v51;
                    if (!sub_10011a89(v54, v55))
                    {
                        v56 = _ccall(v47, v48, (unsigned int)v49, v30 + iter * 18 + node);
                        *((char *)v56) = 1;
                        node += 1;
                    }
                    else
                    {
                        node += 1;
                    }
                }
                else
                {
                    node += 1;
                }
            }
            else
            {
                node += 1;
                v51 = v53;
            }
        }
    }
    v19 = 0;
    v13 = 0;
    for (iter = 0; iter < 14; iter += 1)
    {
        iter1 = 0;
        while (iter1 < 15)
        {
            node = iter1 + 1;
            if (v30[18 * iter + node])
            {
                v21 = 0;
                v20 = 0;
                v14 = 0;
                for (m = 0; m < 7; m += 1)
                {
                    v57 = m;
                    v58 = v57;
                    if (v58 > 3)
                        v58 = 6 - v57;
                    v59 = v57 * 7;
                    iter2 = 0;
                    while (iter2 < 7)
                    {
                        v60 = iter2;
                        v61 = v60;
                        if (v61 > 3)
                            v61 = 6 - v60;
                        v62 = v59 + v60;
                        if ((&g_10053200)[v62])
                        {
                            v63 = v60 + node;
                            if (v63 < 3)
                            {
                                iter2 += 1;
                            }
                            else if (v63 < 21)
                            {
                                v64 = iter + m;
                                if (v64 < 3)
                                {
                                    iter2 += 1;
                                }
                                else if (v64 < 0x11)
                                {
                                    v7 = v63 - 3;
                                    v6 = v64;
                                    v5 = v62;
                                    v4 = v59;
                                    v3 = &v8;
                                    v2 = &v35;
                                    v1 = v58;
                                    v0 = v61;
                                    if (sub_100117ef(node, iter, v29, iter2, m))
                                    {
                                        v58 = v1;
                                        v65 = v63 - 3 + (v64 - 3) * 18;
                                        v21 += v33[v65];
                                        v66 = v31[v65];
                                        v20 += v66;
                                        if (v66)
                                        {
                                            v14 += v66 * (v0 + v58);
                                            iter2 += 1;
                                        }
                                        else
                                        {
                                            iter2 += 1;
                                        }
                                    }
                                    else
                                    {
                                        v58 = v1;
                                        iter2 += 1;
                                    }
                                }
                                else
                                {
                                    iter2 += 1;
                                }
                            }
                            else
                            {
                                iter2 += 1;
                            }
                        }
                        else
                        {
                            iter2 += 1;
                        }
                    }
                }
                v67 = iter * 18 + node;
                v68 = _ccall(v47, v48, (unsigned int)v49, v28 + v67);
                *((char *)v68) = v21;
                v69 = _ccall(v47, v48, (unsigned int)v49, v27 + v67);
                *((char *)v69) = v20;
                if (!v21)
                {
                    if (v20 <= v19)
                    {
                        if (v20 != v19)
                        {
                            iter1 += 1;
                            continue;
                        }
                        else if (v14 <= v13)
                        {
                            iter1 += 1;
                            continue;
                        }
                    }
                    v19 = v20;
                    v7 = node;
                    v18 = node;
                    v7 = iter;
                    v16 = iter;
                    v7 = v14;
                    v13 = v14;
                    iter1 += 1;
                }
                else
                {
                    iter1 += 1;
                }
            }
            else
            {
                iter1 += 1;
            }
        }
    }
    if (v19)
    {
        v10 = v17 + g_10052768 - 8;
        v11 = v15 + g_1005276c - 6;
        v12 = *((int *)&g_10052770);
        g_100f9328 = 1;
        sub_1003a60a(&v9, v70);
        return;
    }
    v71 = sub_1002355e();
    if (!v71)
        return;
    g_100f9328 = 1;
    sub_1003a60a(v71, g_100f94cb);
    return;
}
```

## `sub_1003d19a` `0x1003d19a`

_1141 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1003cfb7[4];
extern unsigned int g_1003cfbb[4];
extern unsigned int g_1003cff7[4];
extern unsigned int g_1003cffb[4];
extern unsigned int g_1003d037[4];
extern unsigned int g_1003d03b[4];
extern unsigned int g_1003d077[4];
extern unsigned int g_1003d07b[4];
extern unsigned int g_1003d0b7[4];
extern unsigned int g_1003d0bb[4];
extern unsigned int g_1003d0f7[4];
extern unsigned int g_1003d0fb[4];
extern unsigned int g_1003d137[4];
extern unsigned int g_1003d13b[4];
extern unsigned int g_1003d177[4];
extern unsigned int g_1003d17b[4];
extern unsigned short g_10043482;
extern char g_10043487;
extern char g_10043489;
extern unsigned short g_1004348a;
extern char g_1004348c;
extern unsigned short g_1004348d;
extern unsigned short g_1004348f;
extern char g_10043491;
extern unsigned int g_10052768;
extern unsigned int g_1005276c;
extern char g_10052770;
extern char g_100fa97a;

int sub_1003d19a(void)
{
    void* v9;  // ecx
    char *v10;  // eax
    unsigned int v19;  // esi
    unsigned int v20;  // edi
    unsigned int index;  // edx
    int v22;  // ecx
    int v23;  // ebx
    unsigned int idx;  // edx
    int v25;  // ecx
    int v26;  // ebx
    unsigned int idx1;  // edx
    int v28;  // ecx
    unsigned short v11;  // dx
    int v29;  // ebx
    unsigned int idx2;  // edx
    int v31;  // ecx
    int v32;  // ebx
    unsigned int v33;  // edx
    int v34;  // ecx
    int v35;  // ebx
    unsigned int v36;  // edx
    int v37;  // ecx
    int v38;  // ebx
    unsigned int v39;  // edx
    int v40;  // ecx
    int v41;  // ebx
    unsigned int v42;  // edx
    int v43;  // ecx
    int v44;  // ebx
    unsigned int v13;  // eax
    unsigned int v14[21];  // eax
    unsigned int v15;  // ebx
    unsigned int v16;  // ecx
    unsigned int v17;  // ebx
    unsigned int v18;  // ecx
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    char v3;  // [bp+0xfff8f]
    unsigned int v4;  // [bp+0xffff0]
    unsigned int i;  // [bp+0xffff4]
    unsigned int v6;  // [bp+0xffff8]
    unsigned int v7;  // [bp+0xffffc]
    unsigned int v8[21];  // [bp+0x100000]

    *((unsigned int *)v9) = *((int *)v9) + 1;
    *(v10) = *(v10) + *((char *)&v10);
    *((char *)v9) = *((char *)v9) + *((char *)&v10);
    *(v10) = *(v10) + *((char *)&v10);
    *(v10) = *(v10) + *((char *)&v10);
    *(v10) = *(v10) + *((char *)&v10);
    *(v10) = *(v10) + *((char *)&v10);
    *(v10) = *(v10) + *((char *)&v10);
    *((char *)v9) = *((char *)v9) + *((char *)&v10);
    *(v10) = *(v10) + *((char *)&v10);
    *((char *)v9) = *((char *)v9) + *((char *)&v10);
    *(v10) = *(v10) + *((char *)&v10);
    *((char *)v9) = *((char *)v9) + *((char *)&v10);
    *(v10) = *(v10) + *((char *)&v10);
    v3 += (char)v11;
    v8[0] = _INSERT(v10, 0, x86g_dirtyhelper_IN(Conv(16I->32I, vvar_342{r16|2b}), 0x1<32>));
    v13 = sub_1002ae92(3465, 0, NULL);
    if (!v13)
        return;
    g_10043487 = v13;
    g_10043489 = v11;
    g_1004348c = v11;
    g_1004348a = 3465;
    g_10043491 = g_10052770;
    v14 = v8;
    v15 = v14[9];
    v7 = v15;
    v16 = v14[10];
    v6 = v16;
    v4 = v14[20];
    v17 = v15 - g_10052768;
    v18 = v16 - g_1005276c;
    v19 = (v17 ^ v17 >> 31) - (v17 >> 31);
    v20 = (v18 ^ v18 >> 31) - (v18 >> 31);
    if (v17 < 40)
    {
        if (v18 < 40)
        {
            if ((v19 > v20 || v4 == 1) && v4 != 2)
            {
                i = 0;
                while (i < 8)
                {
                    index = i * 8;
                    v1 = v7 + *((int *)(index + (char *)&g_1003cfb7[0]));
                    v0 = v6 + *((int *)(index + (char *)&g_1003cfbb[0]));
                    v22 = v6 + *((int *)(index + (char *)&g_1003cfbb[0]));
                    v23 = v7 + *((int *)(index + (char *)&g_1003cfb7[0]));
                    if (sub_1003c936(v23, v22))
                    {
                        g_1004348d = v23;
                        g_1004348f = v22;
                        if (!g_100fa97a)
                        {
                            v1 = 0x11;
                            sub_1002ade7(&g_10043482);
                            return;
                        }
                        if (sub_10011678(v23, v22, 0))
                        {
                            v1 = 0x11;
                            sub_1002ade7(&g_10043482);
                            return;
                        }
                        *((unsigned int *)(/* unsupported instruction */ - 16)) = i + 1;
                    }
                    else
                    {
                        i += 1;
                    }
                }
                return;
            }
            i = 0;
            while (i < 8)
            {
                idx = i * 8;
                v1 = v7 + *((int *)(idx + (char *)&g_1003cff7[0]));
                v0 = v6 + *((int *)(idx + (char *)&g_1003cffb[0]));
                v25 = v6 + *((int *)(idx + (char *)&g_1003cffb[0]));
                v26 = v7 + *((int *)(idx + (char *)&g_1003cff7[0]));
                if (sub_1003c936(v26, v25))
                {
                    g_1004348d = v26;
                    g_1004348f = v25;
                    if (!g_100fa97a)
                    {
                        v1 = 0x11;
                        sub_1002ade7(&g_10043482);
                        return;
                    }
                    if (sub_10011678(v26, v25, 0))
                    {
                        v1 = 0x11;
                        sub_1002ade7(&g_10043482);
                        return;
                    }
                    *((unsigned int *)(/* unsupported instruction */ - 16)) = i + 1;
                }
                else
                {
                    i += 1;
                }
            }
            return;
        }
        else
        {
            if ((v19 > v20 || v4 == 1) && v4)
            {
                i = 0;
                while (i < 8)
                {
                    idx1 = i * 8;
                    v1 = v7 + *((int *)(idx1 + (char *)&g_1003d037[0]));
                    v0 = v6 + *((int *)(idx1 + (char *)&g_1003d03b[0]));
                    v28 = v6 + *((int *)(idx1 + (char *)&g_1003d03b[0]));
                    v29 = v7 + *((int *)(idx1 + (char *)&g_1003d037[0]));
                    if (sub_1003c936(v29, v28))
                    {
                        g_1004348d = v29;
                        g_1004348f = v28;
                        if (!g_100fa97a)
                        {
                            v1 = 0x11;
                            sub_1002ade7(&g_10043482);
                            return;
                        }
                        if (sub_10011678(v29, v28, 0))
                        {
                            v1 = 0x11;
                            sub_1002ade7(&g_10043482);
                            return;
                        }
                        *((unsigned int *)(/* unsupported instruction */ - 16)) = i + 1;
                    }
                    else
                    {
                        i += 1;
                    }
                }
            }
            else
            {
                i = 0;
                while (i < 8)
                {
                    idx2 = i * 8;
                    v1 = v7 + *((int *)(idx2 + (char *)&g_1003d077[0]));
                    v0 = v6 + *((int *)(idx2 + (char *)&g_1003d07b[0]));
                    v31 = v6 + *((int *)(idx2 + (char *)&g_1003d07b[0]));
                    v32 = v7 + *((int *)(idx2 + (char *)&g_1003d077[0]));
                    if (sub_1003c936(v32, v31))
                    {
                        g_1004348d = v32;
                        g_1004348f = v31;
                        if (!g_100fa97a)
                        {
                            v1 = 0x11;
                            sub_1002ade7(&g_10043482);
                            return;
                        }
                        if (sub_10011678(v32, v31, 0))
                        {
                            v1 = 0x11;
                            sub_1002ade7(&g_10043482);
                            return;
                        }
                        *((unsigned int *)(/* unsupported instruction */ - 16)) = i + 1;
                    }
                    else
                    {
                        i += 1;
                    }
                }
            }
            return;
        }
    }
    else
    {
        if (v18 < 40)
        {
            if ((v19 > v20 || v4 == 3) && v4 != 2)
            {
                i = 0;
                while (i < 8)
                {
                    v33 = i * 8;
                    v1 = v7 + *((int *)(v33 + (char *)&g_1003d0b7[0]));
                    v0 = v6 + *((int *)(v33 + (char *)&g_1003d0bb[0]));
                    v34 = v6 + *((int *)(v33 + (char *)&g_1003d0bb[0]));
                    v35 = v7 + *((int *)(v33 + (char *)&g_1003d0b7[0]));
                    if (sub_1003c936(v35, v34))
                    {
                        g_1004348d = v35;
                        g_1004348f = v34;
                        if (!g_100fa97a)
                        {
                            v1 = 0x11;
                            sub_1002ade7(&g_10043482);
                            return;
                        }
                        if (sub_10011678(v35, v34, 0))
                        {
                            v1 = 0x11;
                            sub_1002ade7(&g_10043482);
                            return;
                        }
                        *((unsigned int *)(/* unsupported instruction */ - 16)) = i + 1;
                    }
                    else
                    {
                        i += 1;
                    }
                }
                return;
            }
            i = 0;
            while (i < 8)
            {
                v36 = i * 8;
                v1 = v7 + *((int *)(v36 + (char *)&g_1003d0f7[0]));
                v0 = v6 + *((int *)(v36 + (char *)&g_1003d0fb[0]));
                v37 = v6 + *((int *)(v36 + (char *)&g_1003d0fb[0]));
                v38 = v7 + *((int *)(v36 + (char *)&g_1003d0f7[0]));
                if (sub_1003c936(v38, v37))
                {
                    g_1004348d = v38;
                    g_1004348f = v37;
                    if (!g_100fa97a)
                    {
                        v1 = 0x11;
                        sub_1002ade7(&g_10043482);
                        return;
                    }
                    if (sub_10011678(v38, v37, 0))
                    {
                        v1 = 0x11;
                        sub_1002ade7(&g_10043482);
                        return;
                    }
                    *((unsigned int *)(/* unsupported instruction */ - 16)) = i + 1;
                }
                else
                {
                    i += 1;
                }
            }
            return;
        }
        else
        {
            if ((v19 > v20 || v4 == 3) && v4)
            {
                i = 0;
                while (i < 8)
                {
                    v39 = i * 8;
                    v1 = v7 + *((int *)(v39 + (char *)&g_1003d137[0]));
                    v0 = v6 + *((int *)(v39 + (char *)&g_1003d13b[0]));
                    v40 = v6 + *((int *)(v39 + (char *)&g_1003d13b[0]));
                    v41 = v7 + *((int *)(v39 + (char *)&g_1003d137[0]));
                    if (sub_1003c936(v41, v40))
                    {
                        g_1004348d = v41;
                        g_1004348f = v40;
                        if (!g_100fa97a)
                        {
                            v1 = 0x11;
                            sub_1002ade7(&g_10043482);
                            return;
                        }
                        if (sub_10011678(v41, v40, 0))
                        {
                            v1 = 0x11;
                            sub_1002ade7(&g_10043482);
                            return;
                        }
                        *((unsigned int *)(/* unsupported instruction */ - 16)) = i + 1;
                    }
                    else
                    {
                        i += 1;
                    }
                }
                return;
            }
            i = 0;
            while (i < 8)
            {
                v42 = i * 8;
                v1 = v7 + *((int *)(v42 + (char *)&g_1003d177[0]));
                v0 = v6 + *((int *)(v42 + (char *)&g_1003d17b[0]));
                v43 = v6 + *((int *)(v42 + (char *)&g_1003d17b[0]));
                v44 = v7 + *((int *)(v42 + (char *)&g_1003d177[0]));
                if (sub_1003c936(v44, v43))
                {
                    g_1004348d = v44;
                    g_1004348f = v43;
                    if (!g_100fa97a)
                    {
                        v1 = 0x11;
                        sub_1002ade7(&g_10043482);
                        return;
                    }
                    if (sub_10011678(v44, v43, 0))
                    {
                        v1 = 0x11;
                        sub_1002ade7(&g_10043482);
                        return;
                    }
                    *((unsigned int *)(/* unsupported instruction */ - 16)) = i + 1;
                }
                else
                {
                    i += 1;
                }
            }
            return;
        }
    }
}
```

## `sub_1003d60f` `0x1003d60f`

_289 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[80];
    unsigned int field_50;
} struct_0;

extern unsigned short g_10043493;
extern unsigned short g_10043496;
extern unsigned short g_10043498;
extern char g_1004349a;
extern unsigned short g_1004349b;
extern char g_1004349d;
extern char g_100434a0;
extern char g_100434a2;
extern int g_10052768;
extern int g_1005276c;
extern void g_10052770;
extern struct_0 *g_1005f7ed;

int sub_1003d60f(void)
{
    unsigned int v5;  // eax
    char v6;  // dl
    int v7;  // ebx
    int v8;  // ecx
    char v9;  // dl
    unsigned int v10;  // eax
    int v11;  // ebx
    int v12;  // ecx
    unsigned int v0;  // [bp-0x34]
    unsigned int v1;  // [bp-0x1c]
    unsigned int i;  // [bp-0xc]
    unsigned int iter;  // [bp-0x8]

    v5 = sub_1002ae92(0, 0, NULL);
    if (!v5)
        return v5;
    g_100434a0 = v5;
    g_100434a2 = v6;
    g_1004349d = 1;
    g_1004349b = 3465;
    g_1004349a = g_10052770;
    v7 = g_10052768;
    v8 = g_1005276c;
    v9 = g_1005f7ed->field_50;
    if (!(char)g_1005f7ed->field_50)
    {
        v8 = g_1005276c - 1;
    }
    else if (v9 == 1)
    {
        v7 = g_10052768 + 1;
    }
    else if (v9 == 2)
    {
        v8 = g_1005276c + 1;
    }
    else
    {
        v7 = g_10052768 - 1;
    }
    g_10043496 = v7;
    g_10043498 = v8;
    v10 = sub_1003a03f(v7, v8, *((int *)&g_10052770));
    if (v10)
    {
        v10 = sub_1003d730(v10, 3465, 0);
        if (v10)
        {
            v1 = 0x11;
            return sub_1002ade7(&g_10043493);
        }
    }
    for (i = 0; i < 3; i += 1)
    {
        iter = 0;
        while (iter < 3)
        {
            v11 = g_10052768 - 1 + iter;
            v12 = g_1005276c - 1 + i;
            g_10043496 = v11;
            g_10043498 = v12;
            v10 = sub_1003a03f(v11, v12, *((int *)&g_10052770));
            if (v10)
            {
                if (sub_1003d730(v10, 3465, 0))
                {
                    v0 = 0x11;
                    return sub_1002ade7(&g_10043493);
                }
                iter += 1;
            }
            else
            {
                iter += 1;
            }
        }
    }
    return v10;
}
```

## `sub_1003d730` `0x1003d730`

_64 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1003d730(unsigned int *a0, unsigned int a1, unsigned int a2)
{
    unsigned int v0[3];  // esi
    unsigned int i;  // ecx

    v0 = a0 + 1;
    for (i = 0; i < *(a0); i += 1)
    {
        if ((!a2 || a2 == v0[1]) && a1 == v0[0])
            return 1;
        v0 += 1;
    }
    return 0;
}
```

## `sub_1003d770` `0x1003d770`

_212 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1003d770(int a0, int a1, unsigned int a2, int a3, int a4)
{
    unsigned int v21;  // eax
    unsigned int v22;  // eax
    unsigned int v23;  // eax
    int v24;  // eax
    unsigned int v0;  // [bp-0x58]
    int v1;  // [bp-0x54]
    int v2;  // [bp-0x50]
    int v3;  // [bp-0x4c]
    unsigned int v4;  // [bp-0x48]
    unsigned int v5;  // [bp-0x44]
    unsigned int v6;  // [bp-0x40]
    unsigned int v7;  // [bp-0x3c]
    unsigned int v8;  // [bp-0x38]
    unsigned int v9;  // [bp-0x34]
    int v10;  // [bp-0x30]
    int v11;  // [bp-0x2c]
    int v12;  // [bp-0x28]
    int v13;  // [bp-0x24]
    unsigned int v14;  // [bp-0x20]
    unsigned int v15;  // [bp-0x1c]
    unsigned int v16;  // [bp-0x18]
    unsigned int v17;  // [bp-0x14]
    unsigned int v18;  // [bp-0x10]
    unsigned int v19;  // [bp-0xc]
    unsigned int v20;  // [bp-0x8]

    v21 = a2;
    if (v21 > 60000)
    {
        v22 = ~(v21) + 1;
        if (v22 < 2)
            return v22;
        if (v22 <= 351)
        {
            v20 = v22;
            v19 = v22;
            v23 = 5259024();
            if (v23 != 4)
                return v23;
            v24 = a3;
            if (!v24)
            {
                v19 = v20;
                v24 = 5257296();
            }
            return sub_1003d844(a0, a1, v20, v24, a4, 0);
        }
        else
        {
            return v22;
        }
    }
    else if (v21 < 100)
    {
        return v21;
    }
    else if (v21 > 10477)
    {
        return v21;
    }
    else
    {
        if (!a3)
        {
            v19 = a2;
            a3 = 5251648();
        }
        v19 = 0;
        v18 = 2;
        v17 = 192;
        v16 = 192;
        v15 = 192;
        v14 = 2;
        v13 = a3;
        v12 = a3;
        v11 = a1;
        v10 = a0;
        v9 = *((char *)((void*)&a4 + 2));
        v8 = *((char *)((void*)&a4 + 1));
        v7 = (char)a4;
        v6 = 0;
        v5 = 0;
        v4 = a2;
        v3 = a3;
        v2 = a1;
        v1 = a0;
        v0 = 1;
        return 4938128();
    }
}
```

## `sub_1003d844` `0x1003d844`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f7ed;

int sub_1003d844(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v0;  // [bp-0x50]
    unsigned int v1;  // [bp-0x4c]
    unsigned int v2;  // [bp-0x48]
    unsigned int v3;  // [bp-0x44]
    unsigned int v4;  // [bp-0x40]
    unsigned int v5;  // [bp-0x3c]
    unsigned int v6;  // [bp-0x38]
    unsigned int v7;  // [bp-0x34]
    unsigned int v8;  // [bp-0x30]
    unsigned int v9;  // [bp-0x2c]
    unsigned int v10;  // [bp-0x28]
    unsigned int v11;  // [bp-0x24]
    unsigned int v12;  // [bp-0x20]
    unsigned int v13;  // [bp-0x1c]
    unsigned int v14;  // [bp-0x18]
    unsigned int v15;  // [bp-0x14]
    unsigned int v16;  // [bp-0x10]
    unsigned int v17;  // [bp-0xc]
    unsigned int v18;  // [bp-0x8]

    v18 = 2;
    v17 = 192;
    v16 = 192;
    v15 = 192;
    v14 = 2;
    v13 = 64;
    v12 = 156;
    v11 = a1;
    v10 = a0;
    v9 = 71;
    v8 = 71;
    v7 = 71;
    v6 = 0;
    v5 = g_1005f7ed + 100;
    v4 = a2;
    v3 = a3;
    v2 = a1;
    v1 = a0;
    v0 = 1;
    return 4939408();
}
```

## `sub_1003d89c` `0x1003d89c`

_259 bytes. refs "Locked on hotkey: Error #%d %d ms"_

```c
typedef struct FLOATING_SAVE_AREA {
    unsigned int ControlWord;
    unsigned int StatusWord;
    unsigned int TagWord;
    unsigned int ErrorOffset;
    unsigned int ErrorSelector;
    unsigned int DataOffset;
    unsigned int DataSelector;
    Byte RegisterArea[80];
    unsigned int Spare0;
} FLOATING_SAVE_AREA;

typedef struct CONTEXT {
    enum CONTEXT_FLAGS ContextFlags;
    unsigned int Dr0;
    unsigned int Dr1;
    unsigned int Dr2;
    unsigned int Dr3;
    unsigned int Dr6;
    unsigned int Dr7;
    FLOATING_SAVE_AREA FloatSave;
    unsigned int SegGs;
    unsigned int SegFs;
    unsigned int SegEs;
    unsigned int SegDs;
    unsigned int Edi;
    unsigned int Esi;
    unsigned int Ebx;
    unsigned int Edx;
    unsigned int Ecx;
    unsigned int Eax;
    unsigned int Ebp;
    unsigned int Eip;
    unsigned int SegCs;
    unsigned int EFlags;
    unsigned int Esp;
    unsigned int SegSs;
    Byte ExtendedRegisters[512];
} CONTEXT;

extern unsigned int g_1005db78;
extern unsigned int g_1005db80;
extern unsigned int g_1005db84;
extern unsigned int g_1005db88;
extern unsigned int g_1005dbbc;
extern unsigned int g_1005dbc0;
extern unsigned int g_1005dbc4;
extern unsigned int g_1005dbc8;
extern unsigned int g_1005dbcc;
extern unsigned int g_1005dbd0;
extern unsigned int g_1005dbd4;
extern HANDLE g_102e2610;
extern CONTEXT g_102e2720;
extern unsigned int g_102e27d8;

int sub_1003d89c(PSTR a0)
{
    unsigned int count;  // eax
    int v9;  // eax
    unsigned int count1;  // eax
    unsigned int v0;  // [bp-0xbd8]
    unsigned int v1;  // [bp-0xbd4]
    unsigned int v2;  // [bp-0xbd0]
    unsigned int v3;  // [bp-0xbcc]
    unsigned int v4;  // [bp-0xbc8]
    unsigned int v5;  // [bp-0xbc4]
    unsigned int v6;  // [bp-0xbc0]
    Byte v7[3000];  // [bp-0xbbc]

    *((unsigned int *)&g_102e2720.ContextFlags) = 65537;
    GetThreadContext(g_102e2610, &g_102e2720.ContextFlags);
    count = GetTickCount();
    v6 = count - g_1005db88;
    v5 = g_1005db80;
    v4 = g_1005db84;
    v3 = g_102e27d8 - sub_10002430;
    v2 = g_1005db78;
    wsprintfA(v7, a0);
    v9 = sub_100253d9(v7);
    if (!g_1005dbc0)
        return v9;
    count1 = GetTickCount();
    if (g_1005dbd0 && g_1005dbcc)
    {
        v6 = g_1005dbc4;
        v5 = g_1005dbc8;
        v4 = g_102e27d8 - sub_10002430;
        v3 = g_1005dbbc;
        v2 = count1 - g_1005dbd4;
        v1 = g_1005dbcc;
        v0 = g_1005dbd0;
        wsprintfA(v7, "Locked on hotkey: '%s' on command '%s' %d ms Error: %d %lX %lX %lX");
    }
    else
    {
        v6 = count1 - g_1005dbd4;
        v5 = g_1005dbbc;
        wsprintfA(v7, "Locked on hotkey: Error #%d %d ms");
    }
    return sub_100253d9(v7);
}
```

## `sub_1003d99f` `0x1003d99f`

_2304 bytes. calls CreateThread_

```c
typedef struct struct_1 {
    char padding_0[4];
    struct struct_2 *field_4;
} struct_1;

typedef struct struct_3 {
    struct struct_3 *field_0;
    char padding_4[132];
    unsigned int field_88;
    char padding_8c[4];
    unsigned int field_90;
} struct_3;

typedef struct struct_2 {
    char padding_0[8];
    unsigned int field_8;
    char padding_c[20];
    unsigned int field_20;
    char padding_24[24];
    unsigned int field_3c;
    char padding_40[28];
    unsigned int field_5c;
    char padding_60[32];
    unsigned int field_80;
    char padding_84[20];
    unsigned int field_98;
    char padding_9c[16];
    unsigned int field_ac;
    char padding_b0[4];
    unsigned int field_b4;
    char padding_b8[20];
    unsigned int field_cc;
    char padding_d0[4];
    unsigned int field_d4;
} struct_2;

typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
    unsigned int field_18;
    unsigned int field_1c;
    unsigned int field_20;
} struct_0;

extern char g_1003dc78;
extern char g_1003df3d;
extern char g_1003dfaf;
extern char g_1003e019;
extern char g_1003e0bc;
extern char g_1003e215;
extern char g_1003e243;
extern unsigned int g_100432af;
extern unsigned int g_100432b3;
extern unsigned short g_100434ef;
extern char g_100434f1;
extern unsigned int g_100580e4;
extern unsigned int g_100580e8;
extern unsigned int g_100580ec;
extern unsigned int g_10058160;
extern unsigned int g_10058164;
extern unsigned int g_10058168;
extern unsigned int g_10058174;
extern int g_1005a070[4];
extern unsigned int g_1005a078;
extern unsigned int g_1005a07c;
extern char g_1005db75;
extern unsigned int g_1005db9c;
extern unsigned int g_1005dba0;
extern unsigned int g_1005dba4;
extern unsigned int g_1005dba8;
extern char g_1005dc48;
extern char g_1005f854;
extern char g_1005f858;
extern char g_1005f85c;
extern unsigned int g_1005f860;
extern unsigned int g_1005f864;
extern unsigned int g_1005f868;
extern unsigned int g_1005f86c;
extern char g_1005f878;
extern unsigned int g_1005f889;
extern char g_1005f88d;
extern char g_1005f89f;
extern char g_10080b6f;
extern struct_0 *g_10080b84;
extern struct_1 *g_10080b88;
extern char g_1008b743;
extern char g_1008b747;
extern unsigned int g_1008b7bf;
extern unsigned int g_1008b7c3;
extern char g_100ee8bb;
extern unsigned int g_100ee8d8;
extern char g_100f0d3b;
extern char g_100f0d3c;
extern unsigned int g_100f0db8;
extern unsigned int g_100f0dbc;
extern struct_3 *g_100f0dc0;
extern unsigned int g_100f0dd8;
extern unsigned int g_100f0ddc;
extern unsigned int g_100f0de0;
extern unsigned int g_100f0e20;
extern char g_100f0e42;
extern char g_100f9327;
extern char g_100f94ca;
extern unsigned int g_101d5e22;
extern char g_101d5e23;
extern char g_101d5e24;
extern char g_101d5e25;
extern char g_101d5e27;
extern char g_101dfea4;
extern unsigned int g_102e260c;
extern HANDLE g_102e2610;
extern unsigned int g_102e2614;
extern unsigned int g_102e2618;
extern unsigned int g_102e261c;
extern unsigned int g_102e2620;
extern unsigned int g_102e2624;
extern unsigned int g_102e2628;
extern unsigned int g_102e262c;
extern unsigned int g_102e2630;
extern unsigned int g_102e2634;
extern unsigned int g_102e2638;
extern unsigned int g_102e263c;
extern char g_102e2640;
extern unsigned int g_102e2720;
extern unsigned int g_102e27d4;
extern unsigned int g_102e27d8;
extern unsigned int g_102e27e4;
extern unsigned int g_63da40;
extern unsigned int g_63fe60;
extern unsigned int g_63fe64;

void sub_1003d99f(void)
{
    unsigned int v21;  // eax
    unsigned int v22;  // ecx
    unsigned long v31;  // 4169
    unsigned int v32[9];  // esi
    unsigned int v33;  // eax
    unsigned int v34;  // ebx
    unsigned int v35;  // ecx
    unsigned int v36;  // edx
    unsigned int iter;  // eax
    unsigned int iter1;  // ecx
    unsigned int node;  // edx
    unsigned int iter2;  // ebx
    unsigned int v23;  // edx
    unsigned int index[9];  // esi
    unsigned int count;  // eax
    unsigned int v43;  // eax
    unsigned int i;  // ecx
    unsigned int v45;  // eax
    unsigned int v46;  // esi
    unsigned int v47;  // eax
    unsigned int count1;  // ebx
    unsigned int v49;  // eax
    unsigned int count2;  // eax
    unsigned int v24;  // ebx
    HWND v51;  // eax
    unsigned int v52;  // eax
    unsigned int v53;  // eax
    unsigned int v54;  // eax
    struct_3 *v55;  // ebx
    unsigned long v56;  // 4111
    unsigned int v25;  // esi
    unsigned int v26;  // edi
    unsigned long v27;  // ldt
    unsigned long v28;  // gdt
    unsigned short v29;  // fs
    unsigned long v30;  // 4165
    unsigned int idx[54];  // [bp-0x50], Other Possible Types: unsigned int
    unsigned int v1[9];  // [bp-0x4c]
    char *v2;  // [bp-0x48], Other Possible Types: unsigned int
    char *v3;  // [bp-0x44], Other Possible Types: unsigned int
    unsigned int v4;  // [bp-0x40]
    unsigned int v5;  // [bp-0x3c]
    unsigned int v6;  // [bp-0x38]
    unsigned int v7;  // [bp-0x34]
    unsigned int v8;  // [bp-0x30]
    unsigned int v9;  // [bp-0x2c]
    unsigned int v10;  // [bp-0x28]
    unsigned int v11;  // [bp-0x24]
    char *v12;  // [bp-0x20]
    char *v13;  // [bp-0x1c]
    unsigned int v14;  // [bp-0x18]
    unsigned int v15;  // [bp-0x14]
    unsigned int v16;  // [bp-0x10]
    unsigned int v17;  // [bp-0xc]
    unsigned int v18;  // [bp-0x8]
    char v19;  // [bp-0x4]

    v18 = 4294967295;
    v17 = v21;
    v16 = v22;
    v15 = v23;
    v14 = v24;
    v13 = &v18;
    v12 = &v19;
    v11 = v25;
    v10 = v26;
    v9 = sub_10002731;
    v30 = _ccall(v27, v28, (unsigned int)v29, 0);
    v8 = *((int *)v30);
    v31 = _ccall(v27, v28, (unsigned int)v29, 0);
    *((unsigned int **)v31) = &v8;
    if (*((int *)0x64a9c0) != 31)
    {
        g_10080b84 = 0;
        g_10080b88 = 0;
        g_102e2618 = 0;
    }
    g_1005dba8 = &v19;
    g_1005dba4 = &v8;
    g_1005db9c = 4294967294;
    g_1005dba0 = &g_1003dc78;
    if (g_10080b84 && g_10080b88)
    {
        if (g_101d5e22)
        {
            v32 = g_10080b84;
            v33 = g_10080b84->field_14;
            v34 = g_10080b84->field_1c;
            v35 = g_10080b84->field_18;
            v36 = g_10080b84->field_20;
            if (g_102e2618 && g_101d5e22 != g_102e263c)
            {
                v33 = g_102e262c;
                v34 = g_102e2630;
                v35 = g_102e2634;
                v36 = g_102e2638;
            }
            else
            {
                if (v33 == g_102e261c && v34 == g_102e2620 && v35 == g_102e2624 && v36 == g_102e2628)
                    goto LABEL_1003dc78;
                g_102e262c = v33;
                g_102e2630 = v34;
                g_102e2634 = v35;
                g_102e2638 = v36;
                v7 = v33;
                v6 = v35;
                v5 = v36;
                v4 = v34;
                v3 = &v8;
                v2 = &v19;
                v1 = g_10080b84;
                idx = g_101d5e22;
                sub_1002ae6f(&g_102e2640, g_10080b88->field_4, 224);
                v32 = g_10080b84;
            }
            v7 = v33;
            v6 = v35;
            v5 = v36;
            v4 = v34;
            v3 = &v8;
            v2 = &v19;
            v1 = v32;
            idx = g_10080b88->field_4;
            sub_1002ae6f(g_10080b88->field_4, &g_102e2640, 224);
            iter = v33;
            iter1 = v35;
            node = v36;
            iter2 = v34;
            index = v32;
            g_102e2618 = 1;
            v7 = g_101d5e22;
            g_102e263c = g_101d5e22;
            if ((char)g_101d5e22 && node > 36)
            {
                iter1 += 32;
                node -= 32;
                idx[32] = idx[32] + 32;
                idx[2] = idx[2] + 32;
                iter += 22;
                iter2 -= 44;
                idx[38] = idx[38] + 22;
                idx[43] = idx[43] - 22;
                idx[45] = idx[45] + 22;
                idx[8] = idx[8] + 22;
                idx[15] = idx[15] - 22;
            }
            if (g_101d5e24 && node > 36)
            {
                node -= 32;
                idx[0x33] = idx[0x33] - 32;
                idx[53] = idx[53] + 32;
                idx[23] = idx[23] - 32;
                iter += 22;
                iter2 -= 44;
                idx[38] = idx[38] + 22;
                idx[43] = idx[43] - 22;
                idx[45] = idx[45] + 22;
                idx[8] = idx[8] + 22;
                idx[15] = idx[15] - 22;
            }
            if (g_101d5e23 && node > 70)
            {
                iter1 += 64;
                node -= 64;
                idx[32] = idx[32] + 64;
                idx[2] = idx[2] + 64;
                iter += 44;
                iter2 -= 88;
                idx[38] = idx[38] + 44;
                idx[43] = idx[43] - 44;
                idx[45] = idx[45] + 44;
                idx[8] = idx[8] + 44;
                idx[15] = idx[15] - 44;
            }
            if (g_101d5e25 && node > 70)
            {
                node -= 64;
                idx[0x33] = idx[0x33] - 64;
                idx[53] = idx[53] + 64;
                idx[23] = idx[23] - 64;
                iter += 44;
                iter2 -= 88;
                idx[38] = idx[38] + 44;
                idx[43] = idx[43] - 44;
                idx[45] = idx[45] + 44;
                idx[8] = idx[8] + 44;
                idx[15] = idx[15] - 44;
            }
            index[5] = iter;
            index[7] = iter2;
            index[6] = iter1;
            index[8] = node;
            g_102e261c = iter;
            g_102e2620 = iter2;
            g_102e2624 = iter1;
            g_102e2628 = node;
        }
        else if (g_102e2618)
        {
            g_102e2618 = 0;
            g_10080b84->field_14 = g_102e262c;
            g_10080b84->field_1c = g_102e2630;
            g_10080b84->field_18 = g_102e2634;
            g_10080b84->field_20 = g_102e2638;
            sub_1002ae6f(g_10080b88->field_4, &g_102e2640, 224);
        }
    }
LABEL_1003dc78:
    g_1005dba8 = &v19;
    g_1005dba4 = &v8;
    g_1005db9c = 4294967295;
    g_1005dba0 = &g_1003df3d;
    if (g_1005f860 != *((int *)&g_1005f854) || g_1005f864 != *((int *)&g_1005f858) || g_1005f868 != *((int *)&g_1005f85c))
    {
        v7 = *((int *)&g_1005f854);
        g_1005f860 = *((int *)&g_1005f854);
        v7 = *((int *)&g_1005f858);
        g_1005f864 = *((int *)&g_1005f858);
        v7 = *((int *)&g_1005f85c);
        g_1005f868 = *((int *)&g_1005f85c);
        count = GetTickCount();
        v43 = count - g_100580e8;
        g_100580e8 = g_100580e8 + v43;
        if (v43 >= 5000)
        {
            sub_1002ae81(&g_1008b743, 128);
            g_1008b7c3 = 0;
        }
        else
        {
            g_1008b7bf = (unsigned int)sub_1002ae6f(&g_1008b743, &g_1008b747, 124);
            i = 0;
            v45 = 0;
            for (v46 = 0; i < 128; i += 4)
            {
                if (*((int *)&(&g_1008b743)[i]))
                {
                    v45 += *((int *)&(&g_1008b743)[i]);
                    v46 += 1;
                }
            }
            if (v46)
                v45 /= v46;
            g_1008b7c3 = v45;
        }
        v7 = g_100580e8;
        g_1005f86c = g_100580e8;
    }
    v7 = GetTickCount();
    v47 = GetTickCount() - g_100580ec;
    if (*((int *)&g_1005f878) && v47 > *((int *)&g_1005f878))
    {
        g_100580ec = g_100580ec + v47;
        if (g_100ee8d8)
        {
            g_100434ef = 1;
            g_100434f1 = g_100ee8d8;
            v6 = 3;
            sub_1002ade7(&g_100434ef);
        }
        GetTickCount();
    }
    count1 = GetTickCount();
    v49 = count1 - g_100580e4;
    if (v49 >= 700 || g_1005db75)
    {
        g_100580e4 = count1;
        if (g_102e2610)
        {
            if (g_1005dc48 || g_101d5e27 == 1)
                goto LABEL_1003df3d;
            if (g_1005db75)
                sub_1003d89c("TimerThread stack overflowed... Restarting. Error: %d %lX %lX %lX %d ms");
            else
                sub_1003d89c("TimerThread not responding...   Restarting. Error: %d %lX %lX %lX %d ms");
            g_102e2614 = 1;
            Sleep(30);
            TerminateThread(g_102e2610, 1);
            CloseHandle(g_102e2610);
        }
        g_102e2614 = 0;
        g_1005db75 = 0;
        g_102e2610 = CreateThread(NULL, NULL, sub_100227bd, NULL, THREAD_CREATE_RUN_IMMEDIATELY, &g_102e260c);
    }
    else if (v49 >= 500 && !g_1005dc48 && g_102e2610 && g_101d5e27 != 1 && g_10058174)
    {
        sub_1003d89c("TimerThread locked up...        Redirecting. Error: %d %lX %lX %lX %d ms");
        g_102e2720 = 65537;
        SuspendThread(g_102e2610);
        if (GetThreadContext(g_102e2610, &g_102e2720))
        {
            g_102e27e4 = g_10058164;
            g_102e27d4 = g_10058168;
            g_102e27d8 = g_10058160;
            g_102e2720 = 65537;
            SetThreadContext(g_102e2610, &g_102e2720);
        }
        ResumeThread(g_102e2610);
        g_10058174 = 0;
    }
LABEL_1003df3d:
    g_1005dba8 = &v19;
    g_1005dba4 = &v7;
    g_1005db9c = 1;
    g_1005dba0 = &g_1003dfaf;
    sub_10024fae();
    if (!g_10080b6f)
    {
        g_1005f88d = 1;
    }
    else
    {
        g_10080b6f = g_10080b6f - 1;
        v6 = g_100580e4;
        count2 = GetTickCount();
        if (count2 - g_1005f889 > *((int *)&g_1005f89f) || !g_100f94ca)
        {
            g_1005f88d = 1;
            g_1005f889 = count2;
        }
        else
        {
            g_1005f88d = 0;
        }
    }
    g_1005dba8 = &v19;
    g_1005dba4 = &v7;
    g_1005db9c = 2;
    g_1005dba0 = &g_1003e019;
    if (g_100ee8bb && (v51 = sub_10039b62(), v51))
    {
        GetClientRect(v51, &g_1005a070[0]);
        if (g_10080b84)
        {
            g_10080b84->field_14 = 0;
            g_10080b84->field_18 = 0;
            g_10080b84->field_1c = g_1005a078;
            g_10080b84->field_20 = g_1005a07c;
        }
LABEL_1003e080:
        v6 = 214205412;
        sub_10039357(0x4d04ea);
        v5 = 214205269;
        sub_10039357(0x4d050b);
        v4 = 214205269;
        sub_10039357(0x4d052c);
        v3 = 214205390;
        v2 = 5047661;
        sub_10039357(0x4d056d);
    }
    else
    {
        g_1005dba8 = &v19;
        g_1005dba4 = &v7;
        g_1005db9c = 3;
        g_1005dba0 = &g_1003e0bc;
        if (!g_1005f88d)
            goto LABEL_1003e080;
        v6 = 1146159076;
        sub_10039357(0x4d04ea);
        v5 = 1146290000;
        sub_10039357(0x4d050b);
        v4 = 1146290000;
        sub_10039357(0x4d052c);
        v3 = 1146290126;
        v2 = 5047661;
        sub_10039357(0x4d056d);
    }
    g_1005dba8 = &v19;
    g_1005dba4 = &v3;
    g_1005db9c = 4;
    g_1005dba0 = &g_1003e215;
    v52 = GetTickCount();
    v53 = v52 - g_100f0de0;
    if (v53 >= 100)
    {
        g_100f9327 = 0;
        if (g_100f0ddc)
            g_100f0ddc = g_100f0ddc - 1;
        if (g_100f0dd8)
            g_100f0dd8 = g_100f0dd8 - 1;
        g_100f0de0 = g_100f0de0 + 100;
        if (v53 >= 1000)
            g_100f0de0 = GetTickCount();
        if (g_101dfea4)
        {
            if (g_100f0dc0 && g_100f0dc0->field_90 && *((int *)&g_100f0dc0->padding_4[40]) == *((int *)&g_1005f85c) && g_100f0dc0->field_0 == g_100f0db8)
            {
                g_100f0dbc = g_100f0dbc + 1;
                if (g_100f0dbc > 200 && g_100f0dc0->field_88 > 90)
                {
                    *((char *)(sub_10023861() + 139)) = 1;
                    if (g_63fe64 == g_100f0dc0->field_0)
                    {
                        g_63fe64 = 0;
                        g_63fe60 = 0;
                        g_100432af = 0;
                        v54 = g_63da40;
                        g_63da40 = g_63da40 + 1;
                        g_100432b3 = v54;
                        v2 = 11;
                        sub_1002ade7("\t");
                    }
                }
            }
            else
            {
                v55 = g_100f0dc0;
                if (g_100f0dc0)
                    v55 = g_100f0dc0->field_0;
                g_100f0db8 = v55;
                g_100f0dbc = 0;
            }
        }
    }
    else if (!g_100f9327)
    {
        goto LABEL_1003e215;
    }
    if (g_100f0d3b || g_100f0d3c)
        sub_10012edb(v22, v23);
    else
        g_100f0e20 = 0;
    g_100f9327 = 0;
LABEL_1003e215:
    g_1005dba8 = &v19;
    g_1005dba4 = &v2;
    g_1005db9c = 5;
    g_1005dba0 = &g_1003e243;
    if (g_100f0e42)
        sub_1003ecf9();
    g_1005dba8 = &v19;
    g_1005dba4 = &v2;
    g_1005db9c = 6;
    sub_100388ae();
    g_1005dba8 = &v19;
    g_1005dba4 = &v2;
    g_1005db9c = 7;
    sub_1003e2a0();
    v56 = _ccall(v27, v28, (unsigned int)v29, 0);
    *((unsigned int *)v56) = v2;
}
```

## `sub_1003e29f` `0x1003e29f`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1003e29f(void)
{
    return;
}
```

## `sub_1003e2a0` `0x1003e2a0`

_173 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f49d5;
extern unsigned int g_100f49d9;
extern unsigned int g_100f49dd;
extern unsigned int g_100f49e1;
extern unsigned int g_100f49e5;
extern unsigned int g_100f49e9;
extern unsigned int g_100f49ed;

void* sub_1003e2a0(void)
{
    unsigned int i;  // ebx
    void* v3;  // eax
    char *j;  // esi
    char *iter;  // edi
    unsigned int v6;  // ecx
    unsigned int v7;  // ebx
    unsigned int v0;  // [bp-0x4]

    if (g_100f49dd < 2000 || g_100f49dd > 2100)
    {
        g_100f49dd = 2000;
        g_100f49e1 = 2000;
    }
    for (i = g_100f49e1; i != g_100f49dd; i = v0)
    {
        j = i * 316 + g_100f49ed;
        g_100f49d5 = g_100f49d9;
        iter = g_100f49d9 * 316 + g_100f49ed;
        g_100f49e5 = iter;
        g_100f49e9 = iter;
        g_100f49d9 = g_100f49d9 + 1;
        if (g_100f49d9 >= 2000)
            g_100f49d9 = 0;
        for (v6 = 316; v6; j += 1)
        {
            v6 -= 1;
            *(iter) = *(j);
            iter += 1;
        }
        v7 = i + 1;
        if (v7 >= 2100)
            v7 = 2000;
        v0 = v7;
        v3 = sub_10026724();
    }
    g_100f49e1 = i;
    return v3;
}
```

## `sub_1003e34d` `0x1003e34d`

_460 bytes. refs "%s: %d %d %d", "Cursor: %d %d %d", "Bryant likes to kiss boys on the mouth!"_

```c
typedef struct struct_0 {
    char padding_0[68];
    struct struct_1 *field_44;
} struct_0;

typedef struct struct_2 {
    char padding_0[68];
    unsigned int field_44;
} struct_2;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern unsigned int g_10042294;
extern char g_1005a014;
extern unsigned int g_1005f7b1;
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern unsigned int g_1005f85c;
extern unsigned int g_10080b84;
extern unsigned int g_1008b8f4;
extern unsigned int g_1008b8f8;
extern unsigned int g_1008b8fc;
extern char g_100f0e41;
extern unsigned int g_100f0e54;
extern unsigned int g_100f0e68;
extern unsigned int g_100f0e6c;
extern unsigned int g_100f9355;
extern char g_100fa579;
extern char g_10135277;
extern unsigned int g_1013f320;
extern char g_101d5e26;
extern unsigned int g_102e29ec;
extern unsigned int g_102e29f0;
extern char g_102e2a10;

int sub_1003e34d(void)
{
    unsigned int v12;  // ecx
    struct_0 *v13;  // edx
    unsigned int v14;  // eax
    unsigned int v15;  // ebx
    struct_2 *v16;  // esi
    unsigned int v17;  // edi
    unsigned int v18;  // ecx
    int i;  // ecx
    unsigned int v20;  // eax
    unsigned int v0;  // [bp-0x34]
    unsigned int v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x28]
    unsigned int v4;  // [bp-0x24]
    unsigned int v5;  // [bp-0x20]
    unsigned int v6;  // [bp-0x18]
    unsigned int v7;  // [bp-0x14]
    struct_0 *v8;  // [bp-0x10]
    unsigned int v9;  // [bp-0xc]
    unsigned int v10;  // [bp-0x8]

    if (g_1013f320)
    {
        sub_1003e35f();
        return;
    }
    else if (!g_100f9355)
    {
        g_102e29ec = v12;
        g_102e29f0 = v13;
        v10 = v13->field_44(v14);
        v9 = v12;
        v8 = v13;
        v7 = v15;
        v6 = &/* unsupported instruction */;
        v5 = v16->field_44;
        v4 = v17;
        if (!g_1005a014 && g_100fa579 && g_10080b84)
            sub_1003b22b();
        if (g_100f0e41 && g_10080b84)
        {
            sub_1003f3a0();
            g_1008b8f4 = 0xff;
            g_1008b8f8 = 0xff;
            g_1008b8fc = 0xff;
            v3 = g_1005f85c;
            v2 = g_1005f858;
            v1 = g_1005f854;
            v0 = &g_1005f7b1;
            wsprintfA(&g_102e2a10, "%s: %d %d %d");
            sub_1003b127(425, 16, &g_102e2a10);
            v18 = g_100f0e54;
            if (g_100f0e54 == 4294967295)
                v18 = g_1005f85c;
            v3 = v18;
            v2 = g_100f0e6c;
            v1 = g_100f0e68;
            wsprintfA(&g_102e2a10, "Cursor: %d %d %d");
            sub_1003b127(425, 28, &g_102e2a10);
        }
        if (g_10135277 && !g_1005a014 && g_100fa579 && g_10080b84)
            sub_10029010();
        if (*((int *)0x64a9c0) == 31 && g_10080b84 && g_101d5e26)
            sub_1003e7aa();
        if (g_10042294)
        {
            for (i = 0; i < 100; i = 2001)
            {
                g_1008b8f4 = sub_10040a30(0x100, i);
                g_1008b8f8 = sub_10040a30(0x100);
                g_1008b8fc = sub_10040a30(0x100);
                v20 = sub_10040a30(2000);
                sub_1003b127(v20, sub_10040a30(2000), "Bryant likes to kiss boys on the mouth!");
            }
            g_10042294 = g_10042294 - 1;
        }
    }
    else
    {
        sub_1003e35f();
        return;
    }
}
```

## `sub_1003e35f` `0x1003e35f`

_17 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005e19c;
extern unsigned int g_63fe5c;

int sub_1003e35f(void)
{
    g_63fe5c = g_1005e19c;
}
```

## `sub_1003e392` `0x1003e392`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_102e2a04;
extern unsigned int g_102e2a08;
extern unsigned int g_64f600;

int sub_1003e392(void)
{
    unsigned int v1;  // eax

    v1 = g_64f600;
    g_102e2a04 = g_64f600;
    if (g_102e2a08 == 1)
    {
        if (g_64f600 < 7)
            v1 = g_64f600 + 1;
    }
    else
    {
        if (g_102e2a08 == 2 && g_64f600 && g_64f600 <= 7)
            v1 = g_64f600 - 1;
    }
    g_64f600 = v1;
    return sub_1003e3e1();
}
```

## `sub_1003e3bf` `0x1003e3bf`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003e3bf(void)
{
}
```

## `sub_1003e3c6` `0x1003e3c6`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003e3c6(void)
{
}
```

## `sub_1003e3e1` `0x1003e3e1`

_121 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
    unsigned int field_18;
    unsigned int field_1c;
    unsigned int field_20;
} struct_0;

typedef struct struct_1 {
    char padding_0[68];
    struct struct_2 *field_44;
} struct_1;

extern struct_0 *g_10080b84;
extern struct_1 *g_102e29f0;
extern unsigned int g_102e29f4;
extern unsigned int g_102e29f8;
extern unsigned int g_102e29fc;
extern unsigned int g_102e2a00;
extern unsigned int g_102e2a04;
extern unsigned int g_64f600;

int sub_1003e3e1(void)
{
    g_102e29f4 = g_10080b84->field_14;
    g_102e29f8 = g_10080b84->field_18;
    g_102e29fc = g_10080b84->field_1c;
    g_102e2a00 = g_10080b84->field_20;
    g_10080b84->field_1c = 320;
    g_10080b84->field_20 = 240;
    g_102e29f0->field_44();
    g_64f600 = g_102e2a04;
    g_10080b84->field_14 = g_102e29f4;
    g_10080b84->field_18 = g_102e29f8;
    g_10080b84->field_1c = g_102e29fc;
    g_10080b84->field_20 = g_102e2a00;
}
```

## `sub_1003e5f2` `0x1003e5f2`

_440 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
} struct_0;

typedef struct struct_1 {
    char padding_0[32];
    char field_20;
} struct_1;

extern unsigned int g_1008b8f4;
extern unsigned int g_1008b8f8;
extern unsigned int g_1008b8fc;

int sub_1003e5f2(int a0, int iter, unsigned int node, struct_0 *a3, unsigned int a4, int a5)
{
    unsigned int v5;  // eax
    unsigned int v6;  // eax
    unsigned int v7;  // eax
    int v8;  // ecx
    char v9;  // al
    unsigned int v10;  // ecx
    unsigned int v11;  // eax
    unsigned int v12;  // eax
    int v0;  // [bp-0x18], Other Possible Types: unsigned int
    int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]
    struct_1 *v4;  // [bp+0x1c]

    if (a4 == 2 && a0 == 64)
    {
        sub_1003d770(iter, node, a3->field_0, 0, a5);
        iter += 32;
        sub_1003d770(iter, node, a3->field_4, 0, a5);
        node += 32;
        sub_1003d770(iter, node, a3->field_c, 0, a5);
        iter -= 32;
        return sub_1003d770(iter, node, a3->field_8, 0, a5);
    }
    v5 = a3->field_0;
    if (v5 > 60000)
    {
        v6 = ~(v5) + 1;
        if (v6 < 2)
            return v6;
        if (v6 <= 351)
        {
            v2 = v6;
            v0 = v6;
            v7 = 5259024();
            if (v7 != 4)
                return v7;
            v0 = v2;
            v1 = 5257296();
            v3 = 1;
        }
        else
        {
            return v6;
        }
    }
    else if (v5 < 100)
    {
        return v5;
    }
    else if (v5 <= 10477)
    {
        v0 = v5;
        v1 = 5251648();
        v3 = 0;
    }
    else
    {
        return v5;
    }
    v8 = a0 - v1 >> 1;
    v9 = a4;
    if (v9 != 1)
    {
        if (v9 == 3)
        {
            iter += v8;
            node += v8;
        }
        else if (v9 == 4)
        {
            iter += v8;
        }
        else if (v9 == 5)
        {
            node += v8;
        }
        else
        {
            v10 = 10;
            if (a0 == 32)
                v10 = 5;
            if (v9 == 6)
            {
                iter -= v10;
            }
            else if (v9 == 7)
            {
                iter += v10;
            }
            else if (v9 == 8)
            {
                node -= v10;
            }
            else if (v9 == 9)
            {
                node += v10;
            }
        }
        v0 = v1;
        a0 = v1;
    }
    v11 = sub_1003d770(iter, node, a3->field_0, a0, a5);
    if (!v4)
    {
        return v11;
    }
    else if (v4->field_20)
    {
        v12 = sub_10028cf5();
        g_1008b8f4 = 0xcc;
        g_1008b8f8 = 0xcc;
        g_1008b8fc = 0xcc;
        return sub_1003b127(iter + a0 - v12, node, &v4->field_20);
    }
    else
    {
        return v11;
    }
}
```

## `sub_1003e7aa` `0x1003e7aa`

_473 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    unsigned int field_14;
    unsigned int field_18;
    unsigned int field_1c;
    unsigned int field_20;
} struct_0;

extern char g_1005f88d;
extern struct_0 *g_10080b84;
extern char g_1008a90b;
extern char g_1008a98b;
extern char g_1008b8f4;
extern char g_1008b8f8;
extern char g_1008b8fc;
extern void g_1014f420;
extern void g_101d5e20;
extern void* g_10291cf2;

void sub_1003e7aa(void)
{
    void* i;  // ebx
    void* v14;  // ebx
    unsigned int v15;  // edx
    void* idx;  // ebx
    unsigned int iter;  // eax
    unsigned int node;  // ecx
    char v19;  // dl
    char v20;  // dl
    void* index;  // edx
    void* v0;  // [bp-0x3c]
    unsigned int v1;  // [bp-0x38]
    unsigned int v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x28]
    void* v4;  // [bp-0x24]
    unsigned int v5;  // [bp-0x20]
    unsigned int v6;  // [bp-0x1c]
    unsigned int v7;  // [bp-0x18]
    unsigned int v8;  // [bp-0x14]
    unsigned int v9;  // [bp-0x10]
    unsigned int v10;  // [bp-0xc]
    int v11;  // [bp-0x8]

    v10 = 0;
    v9 = 0;
    v8 = 0;
    v7 = 0;
    v6 = 0;
    v5 = 0;
    v3 = 0;
    for (i = &g_1014f420; i < &g_101d5e20; i = v14 + 4308)
    {
        if (!*((char *)i))
            return;
        v14 = i;
        if ((int)v14[0x44])
        {
            v4 = i;
            v11 = 32;
            if ((int)i[64])
                v11 = 64;
            v15 = 4076;
            v2 = 0;
            if ((&g_1008a90b)[v3] || (&g_1008a98b)[v3])
            {
                v15 = 4176;
                v2 = 1;
            }
            idx = i + v15;
            iter = (int)idx[52];
            node = (int)idx[60];
            v19 = (int)idx[48];
            if (v19 == 1)
            {
                iter += v10;
            }
            else if (v19 == 2)
            {
                iter += g_10080b84->field_14;
            }
            else if (v19 == 3)
            {
                iter = iter + g_10080b84->field_14 + g_10080b84->field_1c;
            }
            else if (v19 == 4)
            {
                iter += v8;
            }
            else if (v19 == 5)
            {
                iter += v6;
            }
            v20 = (int)idx[56];
            if (v20 == 1)
            {
                node += v9;
            }
            else if (v20 == 2)
            {
                node += g_10080b84->field_18;
            }
            else if (v20 == 3)
            {
                node = node + g_10080b84->field_18 + g_10080b84->field_20;
            }
            else if (v20 == 4)
            {
                node += v7;
            }
            else if (v20 == 5)
            {
                node += v5;
            }
            v10 = iter;
            v9 = node;
            if (v2)
            {
                v8 = iter;
                v7 = node;
            }
            else
            {
                v6 = iter;
                v5 = node;
            }
            if (!(int)v4[72] || g_1005f88d)
            {
                v1 = 0;
                sub_1003e5f2(v11, v10, v9, idx + 32, (int)idx[24], 0x383838);
                v0 = v4;
                sub_1003e5f2(v11, v10, v9, idx + 8, *((int *)idx), 0x383838);
                if ((char)idx[64])
                {
                    index = idx + 96;
                    if (v4 == g_10291cf2)
                        index = idx + 4;
                    g_1008b8f4 = *((char *)index);
                    g_1008b8f8 = (char)index[1];
                    g_1008b8fc = (char)index[2];
                    sub_1003b127(v10, v9 + v11 - 10, idx + 64);
                }
            }
            v14 = v4;
        }
        v3 += 1;
    }
    return;
}
```

## `sub_1003e983` `0x1003e983`

_177 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[48];
    unsigned int field_30;
    unsigned int field_34;
    char padding_38[20];
    unsigned int field_4c;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_1 *g_1005f7ed;
extern unsigned int g_100f0df8;
extern char g_100f0e45;
extern char g_100f0e46;
extern struct_0 *g_100f45a8;
extern unsigned int g_7e07b0;

unsigned int * sub_1003e983(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int *v7;  // eax
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v5 = g_7e07b0;
    g_7e07b0 = 0;
    v4 = 0;
    v3 = 1;
    v2 = a2;
    v1 = a1;
    v0 = a0;
    v7 = 4604016();
    v4 = g_7e07b0;
    v6 = v4;
    if (!v6)
        g_7e07b0 = v5;
    if (v7 == 0x2)
    {
        return 4288784();
    }
    else if (v7 == 0x1)
    {
        return 4288032();
    }
    else if (v6)
    {
        if (g_1005f7ed)
        {
            v7 = g_1005f7ed->field_4c | g_1005f7ed->field_30 | g_1005f7ed->field_34;
            if (v7)
                return v7;
        }
        if (g_100f0e45)
            g_100f0e45 = 0;
        if (g_100f0e46 && g_100f45a8 != 0xffffffff)
        {
            v7 = &g_100f45a8->field_0;
            g_100f45a8->field_0 = 0;
        }
        g_100f0df8 = 0;
        return v7;
    }
    else
    {
        return v7;
    }
}
```

## `sub_1003ea34` `0x1003ea34`

_480 bytes. (leaf/helper — see body)_

```c
extern char g_1003ebff;
extern unsigned int g_1005dbec;
extern unsigned int g_1005dbf0;
extern unsigned int g_1005dbf4;
extern unsigned int g_1005dbf8;
extern unsigned int g_1005dbfc;
extern unsigned int g_100f0e10;
extern unsigned int g_100f0e30;
extern char g_100f0e42;
extern char g_10207f3b;

void sub_1003ea34(unsigned int a0)
{
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned int v20;  // edx
    unsigned long v21;  // 4113
    unsigned short v12;  // fs
    unsigned long v13;  // 4140
    unsigned long v14;  // 4148
    char *v15;  // esi
    unsigned int node;  // ecx
    char *iter;  // edi
    unsigned int v18;  // edx
    char v19;  // dl
    unsigned int v0;  // [bp-0x201c]
    unsigned int v1;  // [bp-0x2018]
    char *v2;  // [bp-0x2014]
    unsigned int v3;  // [bp-0x2010]
    unsigned int v4;  // [bp-0x200c]
    char v5;  // [bp-0x2008], Other Possible Types: unsigned long, unsigned long long
    char v6;  // [bp-0x1004]
    char v7;  // [bp-0x1003]
    char v8;  // [bp-0xe05]
    char v9;  // [bp-0x4]

    v4 = sub_100025bd;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v3 = *((int *)v13);
    v14 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v14) = &v3;
    g_1005dbf8 = &v9;
    g_1005dbf4 = &v3;
    g_1005dbec = 1;
    g_1005dbf0 = &g_1003ebff;
    g_1005dbfc = 0;
    lstrcpy(&v5 + 4, &(&g_10207f3b)[0x1000 * a0]);
    v15 = &v5 + 1;
    node = 0;
    iter = &v6;
    *((unsigned int *)&v5) = 0;
    g_1005dbfc = &v6;
    while (node < 0x1000)
    {
        v18 = _INSERT(0, 0, v15[node]);
        if (v15[node] == 123)
        {
            *((unsigned int *)&v5) = (unsigned int)v5 + 1;
            *(iter) = v18;
            iter += 1;
            node += 1;
            continue;
        }
        if ((char)v18 == 125)
        {
            *((unsigned int *)&v5) = (unsigned int)v5 - 1;
            *(iter) = v18;
            iter += 1;
            if ((unsigned int)v5 == 4294967295)
            {
                *((unsigned int *)&v5) = 0;
                goto LABEL_1003eb41;
            }
            else if ((unsigned int)v5)
            {
                node += 1;
            }
        }
        else
        {
            if ((char)v18 == 35)
            {
                while (true)
                {
                    v19 = v18;
                    if (!(char)v18 || v19 == 13)
                        break;
                    node += 1;
                    v18 = _INSERT(v19 CONCAT 0, 0, v15[node]);
                }
                continue;
            }
            if (!(unsigned int)v5 && (char)v18 == 124 && v15[1 + node] != 124 && v15[1 + node] != 124)
            {
LABEL_1003eb41:
                *(iter) = 0;
                v2 = v15;
                v1 = node;
                v0 = v18;
                g_100f0e30 = 0;
                v8 = 0;
                sub_10030442(&v6, 0xffffffff, 0);
                if (!(char)v0 || !g_100f0e42 || g_100f0e30)
                {
                    break;
                }
                else
                {
                    iter = &v6;
                    node += 1;
                }
            }
            else
            {
                v20 = _INSERT(v18, 0, v18);
                if (!(char)v18 || (char)v0 == 13)
                {
                    v7 = 0;
                    v2 = v15;
                    v1 = node;
                    v0 = v20;
                    g_100f0e30 = 0;
                    v8 = 0;
                    sub_10030442(&v6, 0xffffffff, 0);
                    if (!(char)v0 || !g_100f0e42 || g_100f0e30)
                    {
                        break;
                    }
                    else
                    {
                        *((unsigned int *)&v5) = 0;
                        iter = &v6;
                        node += 2;
                    }
                }
                else
                {
                    v6 = v0;
                    iter += 1;
                    node += 1;
                }
            }
        }
    }
    v21 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v21) = v3;
    g_100f0e10 = 0;
    ExitThread(0);
    return;
}
```

## `sub_1003eaf2` `0x1003eaf2`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1003eaf2(void)
{
}
```

## `sub_1003eb06` `0x1003eb06`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1003eb06(void)
{
}
```

## `sub_1003ec1e` `0x1003ec1e`

_174 bytes. (leaf/helper — see body)_

```c
extern char g_10052784;
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;

unsigned int sub_1003ec1e(unsigned int *a0)
{
    unsigned int v0;  // eax
    unsigned int v1;  // ebx
    unsigned int v2;  // eax
    unsigned int v3;  // ecx

    sub_10013f16();
    v0 = *(a0) - g_1005f854;
    v1 = a0[1] - g_1005f858 + 6;
    g_10052784 = 1;
    v2 = sub_1000d9b8(v0 + 8, v1, 0);
    if (!v2)
        return v2;
    v3 = g_1005f858;
    if (v2 == 1)
    {
        v3 = 3;
    }
    else if (v2 == 2)
    {
        v3 = 4;
    }
    else if (v2 == 3)
    {
        v3 = 1;
    }
    else if (v2 == 4)
    {
        v3 = 2;
    }
    else if (v2 == 5)
    {
        v3 = 7;
    }
    else if (v2 == 6)
    {
        v3 = 8;
    }
    else if (v2 == 7)
    {
        v3 = 5;
    }
    else if (v2 == 8)
    {
        v3 = 6;
    }
    sub_10014825(v3);
    return 2;
}
```

## `sub_1003eccc` `0x1003eccc`

_45 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern unsigned int g_1005f85c;

unsigned int sub_1003eccc(void)
{
    unsigned int v2;  // eax
    unsigned int v3;  // eax
    struct_0 *v1;  // [bp+0x10000c]

    if (!v2)
        return v2;
    v3 = sub_10037973();
    sub_100147eb(v3, v1->field_4, g_1005f85c);
    return 2;
}
```

## `sub_1003ecf9` `0x1003ecf9`

_1679 bytes. calls CreateThread_

```c
typedef struct struct_0 {
    char padding_0[44];
    unsigned short field_2c;
} struct_0;

typedef struct struct_1 {
    int field_0;
    int field_4;
    char padding_8[36];
    unsigned short field_2c;
    unsigned short field_2e;
} struct_1;

typedef struct struct_3 {
    char padding_0[48];
    unsigned int field_30;
    unsigned int field_34;
} struct_3;

extern char g_1003efa1;
extern char g_1003f05a;
extern char g_1003f259;
extern char g_1003f391;
extern unsigned int g_10042218;
extern unsigned short g_100434c9;
extern unsigned short g_100434cb;
extern char g_100434cd;
extern unsigned short g_100434ce;
extern char g_100434d0;
extern char g_100434d1;
extern unsigned int g_10044620[4];
extern unsigned int g_10044628[4];
extern unsigned int g_10052778;
extern unsigned int g_1005277c;
extern unsigned int g_1005db9c;
extern unsigned int g_1005dba0;
extern unsigned int g_1005dba4;
extern unsigned int g_1005dba8;
extern struct_3 *g_1005f7ed;
extern void g_1005f854;
extern void g_1005f858;
extern char g_1005f85c;
extern HWND g_10072f94;
extern unsigned int g_100f0dcc;
extern unsigned int g_100f0dd0;
extern unsigned int g_100f0df8;
extern unsigned int g_100f0dfc;
extern unsigned int g_100f0e00;
extern unsigned int g_100f0e04;
extern unsigned int g_100f0e0c;
extern unsigned int g_100f0e10;
extern unsigned int g_100f0e14;
extern unsigned int g_100f0e18;
extern unsigned int g_100f0e1c;
extern unsigned int g_100f0e20;
extern unsigned int g_100f0e3c;
extern char g_100f0e45;
extern char g_100f0e46;
extern struct_0 *g_100f45a8;
extern char g_100f45c5;
extern unsigned int g_100f49c5;
extern unsigned int g_101e6ea8[4];
extern char g_10202f06;
extern unsigned int g_10207f0a;
extern unsigned int g_10207f0e;
extern char g_10207f33;
extern char g_10207f36;

struct_0 * sub_1003ecf9(void)
{
    unsigned int count;  // eax
    struct_1 *iter;  // ebx
    unsigned int v14;  // ebx
    struct_0 *v15;  // eax
    char v16;  // dl
    struct_1 *v17;  // ebx
    struct_0 *v18;  // eax
    unsigned int v19;  // ebx
    struct_0 *count1;  // eax
    unsigned int v21;  // esi
    unsigned int v22;  // esi
    int v23;  // eax
    struct_0 *count2;  // eax
    int v24;  // eax
    struct_0 *v25;  // eax
    struct_0 *v26;  // eax
    unsigned int node;  // ecx
    unsigned int v9[2];  // esi
    int v10;  // eax
    int v11;  // eax
    struct_1 *v12;  // esi
    unsigned int v13;  // eax
    struct_0 *v0;  // [bp-0x10]
    struct_1 *v1;  // [bp-0xc], Other Possible Types: unsigned int
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x4]

    count = GetTickCount();
    v2 = 0;
    iter = NULL;
    count2 = count - g_100f0e04;
    if (count2 >= 0x64)
    {
        g_100f0e04 = g_100f0e04 + 100;
        iter = 0x1;
    }
    else
    {
        v2 = 1;
    }
    if (g_100f0e10)
    {
        g_100f0e18 = g_100f0e18 + (char *)iter;
        if (g_100f0e18 > 20)
        {
            count2 = TerminateThread(g_100f0e14, 0);
            g_100f0e10 = 0;
        }
        v2 = 1;
    }
    if (!*((int *)&g_10202f06) || g_100f0e20)
        v2 = 1;
    if (g_100f0e3c)
        v2 = 1;
    if (g_100f0df8)
        g_100f0df8 = g_100f0df8 - (char *)iter;
    if (g_100f0dfc)
    {
        g_100f0dfc = g_100f0dfc - (char *)iter;
        v2 = 1;
    }
    if (g_100f0dcc)
        v2 = 1;
    if (*((int *)&g_10207f36) && *((int *)&g_10202f06))
    {
        iter = g_100f0e00;
        node = 0;
        while (node < 6)
        {
            v9 = 0x30 * iter + (char *)&g_101e6ea8[0];
            count2 = *((int *)&g_1005f85c);
            if (!*((char *)(iter + &g_100f45c5)) && v9[1] == *((int *)&g_1005f85c) && (short)v9[5 + 1] == 7)
            {
                v10 = *((int *)&g_1005f854) - v9[0];
                v11 = *((int *)&g_1005f858) - v9[1];
                count2 = (v11 ^ v11 >> 31) - (v11 >> 31);
                if ((v10 ^ v10 >> 31) - (v10 >> 31) <= *((int *)&g_10207f36) && count2 <= *((int *)&g_10207f36))
                {
                    count2 = (unsigned short)v9[5 + 1];
                    *((char *)(iter + &g_100f45c5)) = 1;
                }
            }
            iter = (char *)&iter->field_0 + 1;
            if (iter >= *((int *)&g_10202f06))
            {
                iter = NULL;
                node += 1;
            }
            else
            {
                node += 1;
            }
        }
    }
    if (v2)
        return count2;
    g_1005277c = 0;
    if (!g_100f0df8)
    {
        g_1005dba8 = &v3;
        g_1005dba4 = &v2;
        g_1005db9c = 500;
        g_1005dba0 = &g_1003efa1;
        g_100f0e1c = 0;
        g_100f0e46 = 0;
        if (g_10207f33 && (sub_10026571(), iter))
        {
            v12 = iter;
            if (v12->field_0 - *((int *)&g_1005f854) + 1 <= 2 && v12->field_4 - *((int *)&g_1005f858) + 1 <= 2)
            {
                v13 = v12->field_0;
                v14 = v12->field_4;
                g_100434c9 = v13;
                g_100434cb = v14;
                g_100434cd = *((int *)&g_1005f85c);
                v1 = v12;
                v0 = *((int *)&g_1005f85c);
                v15 = sub_1003a065(v13, v14, *((int *)&g_1005f85c));
                if (v15)
                {
                    g_100434ce = *((unsigned short *)&v15);
                    g_100434d0 = v16;
                    g_100434d1 = sub_10038d20();
                    v0 = 0xc;
                    v15 = sub_1002ade7("\n");
                    g_100f0dcc = 15;
                    g_100f0dd0 = 4294967295;
                }
                else
                {
                    g_100f0df8 = 0;
                }
                *((unsigned int *)&v0->padding_0[0]) = 0;
                return v15;
            }
            v1 = v12;
            g_100f45a8 = v12;
            v1 = v12;
            v17 = v12;
            if (sub_1003c291(v12))
            {
                v1 = v17;
                v18 = sub_1003ec1e(v17);
                if (v18)
                {
                    g_100f0e46 = 2;
                    return v18;
                }
                g_100f0e45 = 1;
                g_100f0e46 = 1;
                goto LABEL_1003f0a1;
            }
            else
            {
                g_100f0e45 = 1;
                g_100f0e46 = 1;
                goto LABEL_1003f0a1;
            }
        }
        else
        {
            g_1005dba8 = &v3;
            g_1005dba4 = &v2;
            g_1005db9c = 501;
            g_1005dba0 = &g_1003f05a;
            g_100f45a8 = 4294967295;
            while (true)
            {
                if (!g_100f0e45)
                    g_100f0e00 = g_100f0e00 + 1;
                g_100f0e45 = 0;
                v19 = g_100f0e00;
                if (v19 >= *((int *)&g_10202f06))
                {
                    v19 = NULL;
                    g_100f0e00 = 0;
                }
                if (!*((int *)&g_10207f36))
                    break;
                if (g_100f49c5 != *((int *)&g_1005f85c))
                {
                    g_100f49c5 = *((int *)&g_1005f85c);
                    sub_1002ae81(&g_100f45c5, 0x400);
                }
                if (!(&g_100f45c5)[v19])
                    break;
                (&g_100f45c5)[v19] = 0;
            }
            count1 = sub_100188bf(g_10072f94, 0x404, 390, g_100f0e00, NULL);
            g_10042218 = 4294967295;
            g_1005dba8 = &v3;
            g_1005dba4 = &v2;
            g_1005db9c = 502;
            g_1005dba0 = &g_1003f259;
            v17 = &g_101e6ea8[12 * v19];
            g_10042218 = v17->field_2c;
            if ((unsigned short)g_10042218 == 1)
            {
                count1 = *((int *)&g_1005f85c);
                if (*((int *)&g_1005f85c) == *((int *)&v17->padding_8[0]))
                    goto LABEL_1003f0a1;
            }
            else
            {
                if ((unsigned short)g_10042218 == 2)
                {
                    count1 = *((int *)&g_1005f85c);
                    if (*((int *)&g_1005f85c) == *((int *)&v17->padding_8[0]))
                    {
                        count1 = sub_10040272(v17->field_0, v17->field_4, *((int *)&v17->padding_8[0]), g_10044620[g_10207f0a]);
                        g_100f0e1c = 1;
                        g_100f0df8 = 100;
                    }
                }
                else
                {
                    if ((unsigned short)g_10042218 == 3)
                    {
                        count1 = *((int *)&g_1005f85c);
                        if (*((int *)&g_1005f85c) == *((int *)&v17->padding_8[0]))
                        {
                            count1 = sub_100401f7(v17->field_0, v17->field_4, *((int *)&v17->padding_8[0]));
                            g_100f0e1c = 1;
                            g_100f0df8 = 100;
                        }
                    }
                    else
                    {
                        if ((unsigned short)g_10042218 == 4 || (unsigned short)g_10042218 == 7)
                        {
                            count1 = *((int *)&g_1005f85c);
                            if (*((int *)&g_1005f85c) == *((int *)&v17->padding_8[0]))
                            {
                                g_100f0e45 = 1;
LABEL_1003f0a1:
                                v23 = *((int *)&g_1005f854) - v17->field_0;
                                g_100f0df8 = g_100f0df8 + (v23 ^ v23 >> 31) - (v23 >> 31);
                                v24 = *((int *)&g_1005f858) - v17->field_4;
                                g_100f0df8 = ((v24 ^ v24 >> 31) - (v24 >> 31) + g_100f0df8) * 10 + 30;
                                count1 = sub_1003e983(v17->field_0, v17->field_4, *((int *)&v17->padding_8[0]));
                            }
                        }
                        else
                        {
                            if ((unsigned short)g_10042218 == 5)
                            {
                                v21 = v17->field_2e;
                                if (v21)
                                {
                                    v22 = v21 - 1;
                                    if (g_100f0e14)
                                    {
                                        v1 = v22;
                                        CloseHandle(g_100f0e14);
                                    }
                                    g_100f0e18 = 0;
                                    count1 = CreateThread(NULL, 0x40000, sub_1003ea34, v22, THREAD_CREATE_RUN_IMMEDIATELY, &g_100f0e10);
                                    g_100f0e14 = count1;
                                }
                            }
                            else
                            {
                                if ((unsigned short)g_10042218 == 6)
                                {
                                    count1 = *((int *)&g_1005f85c);
                                    if (*((int *)&g_1005f85c) == *((int *)&v17->padding_8[0]))
                                    {
                                        if (*((int *)&g_1005f854) == v17->field_0 && *((int *)&g_1005f858) == v17->field_4)
                                        {
                                            count1 = sub_10014825(sub_10040a30(4) + 1);
                                            g_100f0e45 = 1;
                                            g_100f0df8 = 4;
                                        }
                                        else
                                        {
                                            count1 = sub_10040272(v17->field_0, v17->field_4, *((int *)&v17->padding_8[0]), g_10044628[g_10207f0e]);
                                            g_100f0df8 = 5;
                                        }
                                    }
                                }
                                else
                                {
                                    if ((unsigned short)g_10042218 == 8)
                                        g_10052778 = v17;
                                }
                            }
                        }
                    }
                }
            }
            g_100f0e0c = 0;
            return count1;
        }
    }
    else if (g_100f0df8 > 1)
    {
        g_1005dba8 = &v3;
        g_1005dba4 = &v2;
        g_1005db9c = 503;
        g_1005dba0 = &g_1003f391;
        v25 = (!g_100f0e1c ? sub_1003f393() : g_1005f7ed->field_30 | g_1005f7ed->field_34);
        if (v25)
        {
            g_100f0e0c = 0;
            return v25;
        }
        if (g_100f45a8 == 0xffffffff)
        {
            v26 = &g_101e6ea8[12 * g_100f0e00];
            if (v26->field_2c == 6)
                return v26;
        }
        else
        {
            v26 = g_100f45a8;
        }
        if (!g_100f0e1c)
        {
            if (*((int *)&g_1005f854) == *((int *)&v26->padding_0[0]) && *((int *)&g_1005f858) == *((int *)&v26->padding_0[4]) && *((int *)&g_1005f85c) == *((int *)&v26->padding_0[8]))
            {
                g_100f0e45 = 0;
                g_100f0df8 = 1;
                return v26;
            }
            if (g_100f0e46 == 2)
            {
                g_100f0df8 = 0;
                return v26;
            }
            g_100f0e0c = g_100f0e0c + 1;
            if (g_100f0e0c <= 2)
                return v26;
            g_100f0df8 = 1;
            return v26;
        }
        else if (*((int *)&g_1005f85c) != *((int *)&v26->padding_0[8]))
        {
            g_100f0e45 = 0;
            g_100f0df8 = 1;
            return v26;
        }
        else
        {
            g_100f0e0c = g_100f0e0c + 1;
            if (g_100f0e0c <= 20)
                return v26;
            g_100f0e45 = 0;
            g_100f0df8 = 1;
            return v26;
        }
    }
    else
    {
        return count2;
    }
}
```

## `sub_1003ef4f` `0x1003ef4f`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003ef4f(void)
{
}
```

## `sub_1003ef8c` `0x1003ef8c`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003ef8c(void)
{
}
```

## `sub_1003f189` `0x1003f189`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1003f189(void)
{
}
```

## `sub_1003f2da` `0x1003f2da`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003f2da(void)
{
}
```

## `sub_1003f393` `0x1003f393`

_13 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[76];
    struct struct_0 *field_4c;
} struct_0;

extern struct_0 *g_1005f7ed;

struct_0 * sub_1003f393(void)
{
    struct_0 *v1;  // eax

    v1 = g_1005f7ed;
    if (g_1005f7ed)
        v1 = g_1005f7ed->field_4c;
    return v1;
}
```

## `sub_1003f3a0` `0x1003f3a0`

_567 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[40];
    struct struct_1 *field_28;
    char padding_2c[4];
    struct struct_1 *field_30;
} struct_0;

typedef struct struct_3 {
    char padding_0[20];
    unsigned int field_14;
    unsigned int field_18;
    unsigned int field_1c;
    unsigned int field_20;
} struct_3;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern struct_3 *g_10080b84;
extern unsigned int g_100f0de8;
extern unsigned int g_100f0dec;
extern unsigned int g_100f0df0;
extern unsigned int g_100f0df4;
extern unsigned int g_100f0e60;
extern unsigned int g_100f0e64;
extern unsigned int g_100f0e78;
extern unsigned int g_100f1080;
extern unsigned int g_100f1084;
extern unsigned int g_100f1088;
extern unsigned int g_100f108c;
extern unsigned int g_100f1090;
extern unsigned int g_100f1094;
extern unsigned int g_100f1098;
extern unsigned int g_100f109c;

int sub_1003f3a0(void)
{
    struct_3 *v12;  // ebx
    unsigned int v13;  // eax
    unsigned int v22[9];  // eax
    unsigned int v23;  // edx
    unsigned int i[9];  // esi
    unsigned int v25;  // ebx
    unsigned int v14;  // edi
    unsigned int v15;  // eax
    int v16;  // eax
    unsigned int v17;  // edx
    int j;  // edi
    unsigned int v19;  // eax
    unsigned int v20;  // esi
    unsigned int v21;  // eax
    unsigned int v0;  // [bp-0x78]
    unsigned int v1;  // [bp-0x74]
    unsigned int v2;  // [bp-0x70]
    unsigned int v3;  // [bp-0x6c]
    unsigned int v4;  // [bp-0x68]
    unsigned int v5;  // [bp-0x64]
    unsigned int v6;  // [bp-0x60]
    unsigned int v7;  // [bp-0x5c]
    unsigned int v8;  // [bp-0x44]
    unsigned int v9;  // [bp-0xc]
    struct_0 **v10;  // [bp-0x8]

    v10 = 5384848();
    v12 = g_10080b84;
    v13 = g_1005f854 - g_100f0e60 - (g_10080b84->field_1c >> 1);
    v14 = v13 + g_10080b84->field_1c;
    g_100f1080 = v13 / 100;
    g_100f1088 = v13 % 100;
    v15 = v14;
    v16 = v15 / 100;
    v17 = v15 % 100;
    g_100f1098 = 100;
    if (v17)
    {
        v16 += 1;
        g_100f1098 = v17;
    }
    g_100f1090 = v16;
    j = v16;
    v19 = g_1005f858 - g_100f0e64 - (g_10080b84->field_20 >> 1);
    v20 = v19 + g_10080b84->field_20;
    g_100f1084 = v19 / 100;
    g_100f108c = v19 % 100;
    v21 = v20;
    v22 = (unsigned int)(v21 / 100);
    v23 = v21 % 100;
    g_100f109c = 100;
    if (v23)
    {
        v22 = (char *)&v22[0] + 1;
        g_100f109c = v23;
    }
    g_100f1094 = v22;
    i = v22;
    g_100f0df0 = 0;
    v9 = g_100f1084;
    for (g_100f0df4 = v9; g_100f0df4 < i; g_100f0df4 = g_100f0df4 + 1)
    {
        g_100f0dec = 0;
        v8 = g_100f1080;
        for (g_100f0de8 = g_100f1080; g_100f0de8 < j; g_100f0de8 = g_100f0de8 + 1)
        {
            sub_1003f5d7(j, i);
            *(v10)->field_28(5, 0, 0, 100, 100, v12);
            v7 = 0;
            v6 = 5;
            if (g_100f0df4 == 0xffffffff)
                v5 = g_100f109c;
            else
                v5 = 100;
            if (g_100f0de8 == 4)
                v4 = g_100f1098;
            else
                v4 = 100;
            if (g_100f0df0)
                v3 = 0;
            else
                v3 = g_100f108c;
            if (g_100f0dec)
                v2 = 0;
            else
                v2 = g_100f1088;
            v1 = 5;
            v25 = g_100f0df0 * 100 + g_10080b84->field_18;
            if (g_100f0df0)
                v25 -= g_100f108c;
            v0 = v25;
            v12 = g_100f0dec * 100 + g_10080b84->field_14;
            if (g_100f0dec)
                v12 = &v12->padding_0[-1 * g_100f1088];
            *(v10)->field_30(1, v12);
            j = 1;
            i = v12;
            g_100f0dec = g_100f0dec + 1;
        }
        g_100f0df0 = g_100f0df0 + 1;
    }
    if (!g_100f0e78)
        g_100f0e78 = HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, 0xc000);
    return *(v10)->field_28(5, 0, 0, 106, 106, g_100f0e78);
}
```

## `sub_1003f5d7` `0x1003f5d7`

_1204 bytes. calls CreateFileA, ReadFile, WriteFile; refs "%sminimaps\\%d\\%d.elfm", "%sminimaps\\%d\\blankmaps.elfm", "%sminimaps\\%d\\blankmaps.elfm"_

```c
extern unsigned int g_10042f83;
extern HANDLE g_1005f616;
extern unsigned int g_1005f622;
extern char g_100f10a0;
extern char g_100f20a0;
extern char g_100f30a0;
extern unsigned int g_100f40a0;

int sub_1003f5d7(int a0)
{
    unsigned int v26;  // esi
    unsigned int v27;  // edi
    void* v36;  // edi
    void* iter;  // edi
    void* l;  // esi
    unsigned int v39;  // ecx
    void* v40;  // esi
    unsigned int m;  // ecx
    unsigned int v42;  // ebx
    unsigned int v43;  // ebx
    unsigned int v44;  // ebx
    char v45;  // dl
    unsigned int node;  // ecx
    void* v46;  // edi
    unsigned int v48;  // eax
    unsigned int v49;  // eax
    unsigned int v50;  // eax
    unsigned int v29;  // eax
    unsigned int idx;  // ecx
    void* size;  // ebx
    void* j;  // ecx
    unsigned int i0;  // ecx
    unsigned int k;  // ecx
    void* v35;  // esi
    char *v0;  // [bp-0x1b0]
    unsigned int v1;  // [bp-0x1ac]
    int v2;  // [bp-0x1a8], Other Possible Types: unsigned int
    Byte v3[4];  // [bp-0x1a4], Other Possible Types: unsigned int, int
    unsigned int v4;  // [bp-0x1a0]
    unsigned int v5;  // [bp-0x19c]
    void* v6;  // [bp-0x198]
    Byte v7[4];  // [bp-0x194]
    unsigned int v8;  // [bp-0x190]
    Byte v9[300];  // [bp-0x174]
    HANDLE v10;  // [bp-0x48], Other Possible Types: unsigned int
    Byte v11[4];  // [bp-0x44]
    unsigned int v12;  // [bp-0x40]
    unsigned int v13;  // [bp-0x38]
    unsigned int v14;  // [bp-0x34]
    char v15;  // [bp-0x30]
    char v16;  // [bp-0x2c]
    unsigned int v17;  // [bp-0x28]
    unsigned int v18;  // [bp-0x20]
    unsigned int v19;  // [bp-0x1c]
    unsigned int n;  // [bp-0x18]
    unsigned int iter1;  // [bp-0x14]
    void* v22;  // [bp-0x10]
    unsigned int v23;  // [bp-0xc]
    unsigned int v24;  // [bp-0x8]

    v14 = v26;
    v13 = v27;
    v19 = v26 * 100;
    v18 = v27 * 100;
    node = 0;
    v29 = 4294967295;
    v24 = 4294967295;
    v23 = 4294967295;
    for (v11 = (char[4])(((0 + v26) * 0x4000 + v27) * 16 + a0); node < 0x1000; node += 4)
    {
        if (!*((int *)&(&g_100f10a0)[node]))
        {
            v3 = node;
            v29 = node;
            *((void* *)&(&g_100f10a0)[v29]) = HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, 0x7534);
            break;
        }
        else
        {
            if (*((int *)&(&g_100f20a0)[node]) == v11)
            {
                g_100f40a0 = g_100f40a0 + 1;
                *((unsigned int *)&(&g_100f30a0)[node]) = g_100f40a0;
                return g_100f40a0;
            }
            if (*((int *)&(&g_100f30a0)[node]) < v24)
            {
                v23 = node;
                v24 = *((int *)&(&g_100f30a0)[node]);
            }
        }
    }
    if (v29 == 4294967295)
    {
        <None|const 4294967295> = v23;
        if (v29 == 4294967295)
            return 4294967295;
    }
    idx = v29;
    *((Byte [4])&(&g_100f20a0)[idx]) = v11;
    g_100f40a0 = g_100f40a0 + 1;
    *((unsigned int *)&(&g_100f30a0)[idx]) = g_100f40a0;
    size = *((int *)&(&g_100f10a0)[idx]);
    v22 = *((int *)&(&g_100f10a0)[idx]);
    v3 = v11;
    v2 = a0;
    v1 = &g_10042f83;
    wsprintfA(v9, "%sminimaps\\%d\\%d.elfm");
    v10 = CreateFileA(v9, 0x80000000, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_ARCHIVE, NULL);
    if (v10 != 4294967295)
    {
        ReadFile(v10, v22, 30000, &g_1005f622, NULL);
        return CloseHandle(v10);
    }
    v3 = a0;
    v2 = &g_10042f83;
    wsprintfA(v9, "%sminimaps\\%d\\blankmaps.elfm");
    v10 = CreateFileA(v9, 0x80000000, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_ARCHIVE, NULL);
    if (v10 != 4294967295)
    {
        size = GetFileSize(v10, NULL);
        v6 = HeapAlloc(g_1005f616, HEAP_NONE, size);
        ReadFile(v10, v6, size, &g_1005f622, NULL);
        CloseHandle(v10);
        for (j = NULL; j < size; j += 7)
        {
            if (*((int *)(j + v6)) == v11)
            {
                for (i0 = 0; i0 < 30000; i0 += 3)
                {
                    *((int *)(i0 + (char *)v22)) = *((int *)(j + v6 + 4));
                }
                return HeapFree(g_1005f616, HEAP_NONE, v6);
            }
        }
        HeapFree(g_1005f616, HEAP_NONE, v6);
    }
    if (a0 < 7)
    {
        sub_1003f5d7(a0 + 1);
        k = 7500;
        v35 = size;
        v36 = v22;
        while (k)
        {
            iter = v36;
            l = v35;
            if (!k)
                break;
            k -= 1;
            *((int *)iter) = *((int *)l);
            v36 = iter + 4;
            v35 = l + 4;
            break;
        }
        for (v39 = 0; v39; l += 1)
        {
            v39 -= 1;
            *((char *)iter) = *((char *)l);
            iter += 1;
        }
    }
    if (a0 > 7)
    {
        sub_1003f5d7(7);
        v40 = size;
        m = 0;
        for (v42 = 0; m < 30000; m += 3)
        {
            v43 = _INSERT(v42, 0, *(m + (char *)v40));
            v44 = _INSERT(v43, 0, *(1 + m + (char *)v40));
            v42 = _INSERT(v44, 0, *(2 + m + (char *)v40));
            v45 = (0 + v43 + v44 + v42) / 3;
            *(m + (char *)v22) = v45;
            *(1 + m + (char *)v22) = v45;
            *(2 + m + (char *)v22) = v45;
        }
    }
    v5 = 4294967295;
    v4 = 1;
    for (n = 0; n < 100; n += 1)
    {
        iter1 = 0;
        v12 = 0;
        while (iter1 < 100)
        {
            v3 = a0;
            v2 = v18 + n;
            v1 = v19 + iter1;
            v0 = &v15;
            0x4dcc00();
            v46 = (n * 100 + iter1) * 3 + v22;
            v48 = _INSERT(_INSERT(v17 * 0x100, 0, v16) * 0x100, 0, v15);
            if (a0 != 7)
            {
                if (v48)
                {
                    *((unsigned short *)v46) = v48;
                    *((char *)&v46[2]) = v17;
                }
            }
            else
            {
                if (a0 == 7)
                {
                    *((unsigned int *)v46) = v48;
                    v49 = v48;
                    if (!v48)
                    {
                        if (!v12)
                        {
                            *((unsigned int *)v46) = 13369395;
                        }
                        else if (!(n && v12 == 0x666666))
                        {
                            *((unsigned int *)v46) = v12;
                        }
                        else if ((int)v46[300] == 0x666666)
                        {
                            *((unsigned int *)v46) = 0x666666;
                        }
                        else
                        {
                            *((unsigned int *)v46) = 13369395;
                        }
                    }
                    if (v49 == 13369395)
                    {
                        v12 = 13369395;
                    }
                    else if (v49 == 0x666666 && n)
                    {
                        v12 = 0x666666;
                    }
                }
            }
            v50 = *((int *)v46) & 0xffffff;
            if (v50 == v4)
            {
                iter1 += 1;
            }
            else if (v5 != 4294967295)
            {
                v5 = 0;
                iter1 += 1;
            }
            else
            {
                v4 = v50;
                v5 = 1;
                iter1 += 1;
            }
        }
    }
    if (v5 == 1)
    {
        v3 = a0;
        v2 = &g_10042f83;
        wsprintfA(v9, "%sminimaps\\%d\\blankmaps.elfm");
        v10 = CreateFileA(v9, 4, FILE_SHARE_WRITE, NULL, OPEN_ALWAYS, FILE_ATTRIBUTE_ARCHIVE, NULL);
        if (v10 == 4294967295)
            return v10;
        v3 = v11;
        v7 = v11;
        v3 = v4;
        v8 = v4;
        WriteFile(v10, v7, 7, &g_1005f622, NULL);
        return CloseHandle(v10);
    }
    else
    {
        v3 = v11;
        v2 = a0;
        v1 = &g_10042f83;
        wsprintfA(v9, "%sminimaps\\%d\\%d.elfm");
        v10 = CreateFileA(v9, 0x40000000, FILE_SHARE_WRITE, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_ARCHIVE, NULL);
        if (v10 == 4294967295)
            return v10;
        WriteFile(v10, v22, 30000, &g_1005f622, NULL);
        return CloseHandle(v10);
    }
}
```

## `sub_1003f644` `0x1003f644`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003f644(void)
{
}
```

## `sub_1003f667` `0x1003f667`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1003f667(void)
{
}
```

## `sub_1003fa8f` `0x1003fa8f`

_1356 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[12];
    struct struct_2 *field_c;
} struct_1;

typedef struct struct_3 {
    char padding_0[144];
    unsigned int field_90;
} struct_3;

typedef struct struct_4 {
    char field_0;
    char padding_1[293];
    unsigned short field_126;
} struct_4;

typedef struct struct_2 {
    struct struct_0 *field_0;
} struct_2;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern char g_1005f537;
extern unsigned int g_1005f539;
extern unsigned int g_1005f53d;
extern unsigned int g_1005f541;
extern unsigned int g_1005f545;
extern unsigned int g_1005f549;
extern unsigned int g_1005f551;
extern unsigned int g_1005f7e5;
extern struct_3 *g_1005f7ed;
extern char g_10093cee[4];
extern char g_10095cee[4];
extern char g_10097cee;
extern unsigned int g_10099cee[4];
extern unsigned int g_1009a0ee[4];
extern unsigned int g_100ee8cc;
extern unsigned int g_100f49dd;
extern unsigned int g_100f49ed;
extern char g_100fa97c;
extern int g_100fa9bc;
extern int g_100fa9fc;
extern void g_10134d61;
extern unsigned int g_1013f31c;

int sub_1003fa8f(void)
{
    void* v1;  // eax
    unsigned short v2;  // ds
    void* i;  // esi
    void* iter;  // esi
    unsigned int v13;  // ecx
    unsigned int v14[4];  // eax
    unsigned int v15;  // ecx
    char v16;  // dl
    unsigned int v17;  // edx
    struct_1 *v19;  // eax
    void* v20;  // ebx
    unsigned int v3;  // cc_op
    int v21;  // ebx
    int v22;  // ebx
    int len;  // eax
    int count;  // eax
    void* j;  // ebx
    char v26;  // cl
    void* v27;  // ebx
    char *node;  // eax
    unsigned int k;  // edx
    unsigned int index;  // eax
    unsigned int v4;  // cc_dep1
    void* v31;  // ebx
    void* v32;  // ebx
    void* iter1;  // ebx
    unsigned int v34;  // eax
    unsigned int iter2;  // eax
    unsigned int v36;  // edx
    char v37;  // cl
    unsigned int v38;  // eax
    unsigned int l;  // edx
    unsigned int idx;  // eax
    unsigned int v5;  // cc_dep2
    void* idx1;  // ebx
    char *v42;  // eax
    char *v43;  // ebx
    char *idx2;  // ebx
    unsigned short v45;  // di
    void* v46;  // ebx
    char *v47;  // eax
    unsigned int v48;  // edi
    void* v49;  // ebx
    char *v50;  // eax
    unsigned int v6;  // cc_ndep
    struct_4 *v51;  // esi
    struct_4 *v52;  // esi
    struct_4 *v53;  // esi
    unsigned int m;  // edx
    void* v56;  // ebx
    void* v57;  // ebx
    void* v58;  // ebx
    unsigned int v7;  // 4122
    unsigned int v8;  // esi
    void* v9;  // ebp
    char v10;  // dl

    *((unsigned short *)&v1[2003480703]) = v2;
    v7 = _ccall(v3, v4, v5, v6);
    v9 = v8 & 4294902015 | (v7 & 213 | 2) * 0x100;
    *((char *)&v9[117]) = (char)v9[117] + v10;
    g_1005f537 = 0;
    while (true)
    {
        while (true)
        {
LABEL_1003fab1:
            g_1005f549 = 0;
            if (g_1005f537)
                break;
            if (g_1005f539)
            {
                shutdown(g_1005f539, SD_BOTH);
                closesocket(g_1005f539);
                g_1005f539 = 0;
            }
            Sleep(100);
        }
        for (i = &g_10134d61; *((char *)i); i += 1);
        iter = i - 1;
        v13 = 0;
        v14 = NULL;
        while (true)
        {
            v15 = v13;
            if (iter < &g_10134d61)
                break;
            v16 = *((char *)iter);
            iter -= 1;
            if (v16 >= 97 && v16 <= 122)
            {
                v17 = _INSERT(v16, 0, v16 - 87);
            }
            else if (v16 >= 65 && v16 <= 90)
            {
                v17 = _INSERT(v16, 0, v16 - 55);
            }
            else if (v16 >= 48 && v16 <= 57)
            {
                v17 = _INSERT(v16, 0, v16 - 48);
            }
            else
            {
                v14 = 0xff;
                break;
            }
            v14 = (char *)v14 + (v17 << ((char)v15 & 31));
            v13 = v15 + 4;
        }
        *((unsigned int *[4])&v9[4704]) = v14;
        g_1005f539 = socket(2, SOCK_STREAM, 6);
        *((unsigned short *)&v9[4624]) = 2;
        *((unsigned short *)&v9[4622]) = htons(g_1013f31c);
        if (g_100fa97c >= 48 && g_100fa97c <= 57)
        {
            *((unsigned int *)&v9[4620]) = inet_addr(&g_100fa97c);
            goto LABEL_1003fbd5;
        }
        else
        {
            v19 = gethostbyname(&g_100fa97c);
            if (v19 && v19->field_c->field_0)
            {
                *((unsigned int *)&v9[4620]) = v19->field_c->field_0->field_0;
LABEL_1003fbd5:
                *((unsigned int *)&v9[4616]) = 0;
                *((unsigned int *)&v9[4612]) = 0;
                if (!connect(g_1005f539, v9 - 4624, 16) && *((int *)0x64a9c0) == 31)
                {
                    Sleep(100);
                    *((char *)&v9[0x1200]) = 1;
                    *((int *)&v9[0x11ff]) = (int)v9[4704];
                    g_100ee8cc = g_1005f7e5;
                    *((unsigned int *)&v9[4603]) = g_1005f7e5;
                    v20 = v9 - 4599;
                    lstrcpy(v20, &g_100fa9bc);
                    v21 = v20 + lstrlen(&g_100fa9bc) + 1;
                    if (g_1005f7ed && g_1005f7ed->field_90)
                    {
                        lstrcpy(v21, &g_1005f7ed->padding_0[4]);
                        v22 = v21 + lstrlen(&g_1005f7ed->padding_0[4]) + 1;
                        lstrcpy(v22, &g_100fa9fc);
                        len = lstrlen(&g_100fa9fc);
                        send(g_1005f539, v9 - 0x1200, v22 + len + 1 - (v9 - 0x1200), 0);
                        g_1005f549 = 1;
                    }
                    while (true)
                    {
                        count = recv(g_1005f539, v9 - 0x1000, 0x1000, 0);
                        if (!count || count == -1 || !g_1005f539 || !g_1005f537)
                        {
                            shutdown(g_1005f539, SD_BOTH);
                            closesocket(g_1005f539);
                            g_1005f539 = 0;
                            Sleep(2000);
                            break;
                        }
                        else
                        {
                            g_1005f551 = 20;
                            *((void* *)&v9[4636]) = count + v9 - 0x1000;
                            while (j < (int)v9[4636])
                            {
                                v26 = *((char *)j);
                                if (*((char *)j) == 1)
                                {
                                    v27 = j + 2;
                                    node = &g_10093cee[32 * (char)j[1]];
                                    for (k = 0; *((char *)v27) && k < 31; k += 1)
                                    {
                                        *(node) = *((char *)v27);
                                        node += 1;
                                        v27 += 1;
                                    }
                                    *(node) = 0;
                                    j = v27 + 1;
                                }
                                else if (v26 == 2)
                                {
                                    index = (char)j[1];
                                    v31 = j + 2;
                                    v32 = v31 + 4;
                                    g_10099cee[index] = *((int *)v31);
                                    iter1 = v32 + 4;
                                    g_1009a0ee[index] = *((int *)v32);
                                    v34 = index * 32;
                                    iter2 = &g_10095cee[v34];
                                    v36 = 0;
                                    while (true)
                                    {
                                        v37 = *((char *)iter1);
                                        if (!*((char *)iter1) || v36 >= 31)
                                            break;
                                        *((char *)iter2) = v37;
                                        iter2 += 1;
                                        iter1 += 1;
                                        v36 += 1;
                                    }
                                    *((char *)iter2) = 0;
                                    if (!v37)
                                    {
                                        v38 = &(&g_10097cee)[v34];
                                        iter1 += 1;
                                        for (l = 0; *((char *)iter1) && l < 31; l += 1)
                                        {
                                            *((char *)v38) = *((char *)iter1);
                                            v38 += 1;
                                            iter1 += 1;
                                        }
                                        *((char *)v38) = 0;
                                    }
                                    j = iter1 + 1;
                                }
                                else if (v26 == 3)
                                {
                                    idx = (char)j[1];
                                    idx1 = j + 2;
                                    *((unsigned int *)&v9[4704]) = g_10099cee[idx];
                                    *((unsigned int *)&v9[4708]) = g_1009a0ee[idx];
                                    v42 = &g_10095cee[32 * idx];
                                    if (*(v42))
                                    {
                                        v43 = v42 + 0x2000;
                                        sub_10029a61(2, v42, v43, *((short *)idx1), (short)idx1[2], (char)idx1[4], (char)idx1[5]);
                                        idx2 = v43;
                                        if (idx2)
                                        {
                                            *((int *)&idx2[90]) = (int)v9[4704];
                                            *((int *)&idx2[0x66]) = (int)v9[4708];
                                            v45 = (short)idx1[8];
                                            *((short *)&idx2[98]) = (short)idx1[6];
                                            *((unsigned short *)&idx2[100]) = v45;
                                        }
                                    }
                                    j = idx1 + 10;
                                }
                                else if (v26 == 4)
                                {
                                    v46 = j + 2;
                                    v47 = &g_10093cee[32 * (char)j[1]];
                                    if (*(v47))
                                    {
                                        idx1 = v46;
                                        sub_10029a61(3, v47, v47, *((short *)v46), (short)v46[2], (char)v46[4], (char)v46[5]);
                                        if (v46)
                                            *((unsigned int *)&v46[0x66]) = 0;
                                    }
                                    j = v46 + 6;
                                }
                                else if (v26 == 7)
                                {
                                    v48 = g_100f49dd;
                                    g_100f49dd = g_100f49dd + 1;
                                    if (g_100f49dd >= 2100)
                                        g_100f49dd = 2000;
                                    v49 = j + 2;
                                    v50 = &(&g_10097cee)[32 * (char)j[1]];
                                    v51 = v48 * 316 + g_100f49ed;
                                    v52 = v51;
                                    while (true)
                                    {
                                        v53 = v52;
                                        if (!*(v50))
                                            break;
                                        v53->field_0 = *(v50);
                                        v50 += 1;
                                        v52 = v53->padding_1;
                                    }
                                    v53->field_0 = 0;
                                    for (m = 0; *((char *)v49) && m < 0xff; m += 1)
                                    {
                                        v51->padding_1[31 + m] = *((char *)v49);
                                        v49 += 1;
                                    }
                                    v51->padding_1[31 + m] = 0;
                                    v51->field_126 = 65529;
                                    j = v49 + 1;
                                }
                                else if (v26 == 8)
                                {
                                    v56 = j + 1;
                                    g_1005f53d = *((char *)v56);
                                    v57 = v56 + 1;
                                    g_1005f541 = *((char *)v57);
                                    v58 = v57 + 1;
                                    g_1005f545 = *((char *)v58);
                                    j = v58 + 1;
                                }
                                else
                                {
                                    shutdown(g_1005f539, SD_BOTH);
                                    closesocket(g_1005f539);
                                    g_1005f539 = 0;
                                    Sleep(2000);
                                    goto LABEL_1003fab1;
                                }
                            }
                        }
                    }
                }
                else
                {
                    shutdown(g_1005f539, SD_BOTH);
                    closesocket(g_1005f539);
                    g_1005f539 = 0;
                    Sleep(2000);
                }
            }
            else
            {
                Sleep(2000);
            }
        }
    }
}
```

## `sub_1003ffdb` `0x1003ffdb`

_4 bytes. (leaf/helper — see body)_

```c
void sub_1003ffdb(void)
{
    return;
}
```

## `sub_1003ffdf` `0x1003ffdf`

_458 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
    char padding_1[3];
    char field_4;
    char field_5;
    unsigned short field_6;
    unsigned short field_8;
    char field_a;
    char padding_b[25];
    unsigned short field_24;
    char padding_26[2];
    unsigned short field_28;
    char padding_2a[2];
    char field_2c;
    char padding_2d[99];
    char field_90;
} struct_0;

extern unsigned int g_10052768;
extern unsigned int g_1005276c;
extern unsigned int g_10052770;
extern char g_1005f538;
extern SOCKET g_1005f539;
extern unsigned int g_1005f53d;
extern unsigned int g_1005f541;
extern unsigned int g_1005f545;
extern char g_1005f7d9;
extern unsigned int g_1005f7e5;
extern char g_1009a4ee;
extern char g_100ee8ba;
extern unsigned int g_100ee8cc;
extern char g_101d5e28;

int sub_1003ffdf(void)
{
    unsigned int v3;  // eax
    struct_0 *v4;  // ecx
    struct_0 *v11;  // esi
    struct_0 *v12;  // ecx
    struct_0 *v13;  // ecx
    struct_0 *v14;  // ecx
    int len;  // ecx
    struct_0 *idx;  // ebx
    unsigned int v6;  // eax
    unsigned int v7;  // eax
    unsigned int v8;  // eax
    struct_0 *v9;  // ecx
    struct_0 *iter;  // ecx
    Byte v0[45];  // [bp-0x2004], Other Possible Types: int, char
    unsigned int v1;  // [bp-0x2003]

    if (g_1005f7e5 != g_100ee8cc)
    {
        g_100ee8cc = g_1005f7e5;
        v0 = 6;
        v1 = g_1005f7e5;
        send(g_1005f539, &v0, 5, 0);
    }
    v0 = (int)_INSERT(v0 CONCAT 0, 0, 2);
    if (g_1005f541 && !g_1005f545)
    {
        *((unsigned short *)&(&v0)[1]) = 0;
        *((unsigned short *)&(&v0)[3]) = 0;
        *((char *)&(&v0)[5]) = 0;
    }
    else
    {
        *((unsigned short *)&(&v0)[1]) = g_10052768;
        *((unsigned short *)&(&v0)[3]) = g_1005276c;
        *((char *)&(&v0)[5]) = g_10052770;
    }
    *((char *)&(&v0)[6]) = g_100ee8ba | g_1005f7d9 * 2;
    *((unsigned short *)&(&v0)[7]) = *((int *)0x63fe78);
    *((unsigned short *)&v0[9]) = *((int *)0x63fe74);
    g_100ee8ba = 0;
    if (!g_1005f538)
    {
        do
        {
            if (false)
                break;
        } while (*(&v0[0]) == g_1009a4ee);
        sub_1002ae6f(&g_1009a4ee, v0, 11);
        return send(g_1005f539, v0, 11, 0);
    }
    else
    {
        send(g_1005f539, v0, 11, 0);
        v3 = (unsigned int)sub_1002ae6f(&g_1009a4ee, v0, 11);
        g_1005f538 = 0;
        if (g_101d5e28)
        {
            return v3;
        }
        else if (!g_1005f53d)
        {
            return v3;
        }
        else
        {
            v4 = v0;
            idx = 0x63fef8;
            v6 = v3;
            while (true)
            {
                v7 = v6;
                if (idx >= 0x64a308)
                    break;
                v4 = v4;
                if (idx->field_90)
                {
                    v8 = sub_1003a494((struct struct_0 *)&idx->field_4, v4, idx);
                    v9 = &idx->field_4;
                    idx = v4;
                    v4 = v9;
                    if (v8)
                    {
                        v9->field_0 = 3;
                        iter = v9->padding_1;
                        for (v11 = &idx->field_4; v11->field_0; iter = iter->padding_1)
                        {
                            iter->field_0 = v11->field_0;
                            v11 = v11->padding_1;
                        }
                        iter->field_0 = v11->field_0;
                        v12 = iter->padding_1;
                        *((unsigned short *)&v12->field_0) = idx->field_24;
                        v13 = &v12->padding_1[1];
                        *((unsigned short *)&v13->field_0) = idx->field_28;
                        v14 = &v13->padding_1[1];
                        v14->field_0 = idx->field_2c;
                        v4 = v14->padding_1;
                    }
                }
                idx = &idx[1].padding_b[12];
                v6 = v8;
            }
            len = v4 - v0;
            if (!len)
                return v7;
            send(g_1005f539, v0, len, 0);
            return v7;
        }
    }
}
```

## `sub_100401a9` `0x100401a9`

_78 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    struct struct_0 *field_4;
} struct_0;

struct_0 * sub_100401a9(int a0, int a1, int a2)
{
    struct_0 *v0;  // eax
    struct_0 *iter;  // esi
    unsigned int i;  // ecx
    struct_0 *v3;  // eax

    v0 = sub_1003a0f8(a0, a1, a2);
    if (!v0)
        return v0;
    iter = &v0->field_4;
    for (i = 0; i < v0->field_0; i += 1)
    {
        v3 = iter->field_0;
        if (v3 == 0x79c)
        {
            return v3;
        }
        else if (v3 == 0x7b0)
        {
            return v3;
        }
        else if (v3 != 0x15a6)
        {
            if (v3 == 0x1e5b)
                return v3;
            iter = &iter[1].field_4;
        }
        else
        {
            return v3;
        }
    }
    return NULL;
}
```

## `sub_100401f7` `0x100401f7`

_83 bytes. (leaf/helper — see body)_

```c
int sub_100401f7(int a0, int a1, int a2)
{
    unsigned int v10;  // eax
    unsigned int v0;  // [bp-0x14]
    unsigned short v1;  // [bp-0x12]
    unsigned short v2;  // [bp-0x10]
    char v3;  // [bp-0xe]
    unsigned short v4;  // [bp-0xd]
    unsigned short v5;  // [bp-0xb]
    char v6;  // [bp-0x9]
    unsigned short v7;  // [bp-0x8]
    char v8;  // [bp-0x6]
    char v9;  // [bp-0x5]

    v10 = sub_100401a9(a0, a1, a2);
    if (!v10)
        return v10;
    v7 = v10;
    v2 = 10;
    v3 = 130;
    v1 = a0;
    v4 = v1;
    v1 = a1;
    v5 = v1;
    v6 = a2;
    v8 = 1;
    v9 = 1;
    v0 = 12;
    return sub_1002ade7(&v2);
}
```

## `sub_1004024a` `0x1004024a`

_40 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1004024a(unsigned int *a0)
{
    unsigned int iter[2];  // esi
    unsigned int i;  // ecx
    unsigned int v2;  // edx

    iter = a0 + 1;
    i = 0;
    for (v2 = 0; i < *(a0); i += 1)
    {
        if (iter[0] != 99)
            v2 = iter[0];
        iter = &iter[1 + 1];
    }
    return v2;
}
```

## `sub_10040272` `0x10040272`

_166 bytes. (leaf/helper — see body)_

```c
extern char g_10044628;
extern char g_1004462c;

unsigned int [2] sub_10040272(int a0, int a1, int a2, unsigned int a3)
{
    unsigned int v13[2];  // eax
    unsigned int i;  // ecx
    unsigned int iter[2];  // esi
    unsigned int v16;  // ebx
    unsigned short v17;  // ax
    unsigned int v0;  // [bp-0x1c]
    unsigned short v1;  // [bp-0x1a]
    unsigned short v2;  // [bp-0x17]
    char v3;  // [bp-0x15]
    unsigned short v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x12]
    unsigned short v6;  // [bp-0xf]
    char v7;  // [bp-0xd]
    unsigned short v8;  // [bp-0xc]
    unsigned short v9;  // [bp-0xa]
    char v10;  // [bp-0x8]
    unsigned short v11;  // [bp-0x7]
    char v12;  // [bp-0x5]

    v13 = sub_1003a0f8(a0, a1, a2);
    if (!v13)
        return v13;
    i = v13[0];
    v12 = v13[0];
    if (a3 == *((int *)&g_10044628) || a3 == *((int *)&g_1004462c))
    {
        for (iter = &v13[1]; i; i -= 1)
        {
            v16 = iter[0];
            if (v16 == 867 || v16 == 868)
            {
                v11 = v16;
                v2 = 0x11;
                v3 = 131;
                v4 = 65535;
                v5 = 0;
                v1 = a3;
                v6 = v1;
                v7 = 0;
                v1 = a0;
                v8 = v1;
                v1 = a1;
                v9 = v1;
                v10 = a2;
                v0 = 19;
                return sub_1002ade7(&v2);
            }
            iter = &iter[1 + 1];
        }
    }
    v17 = v13[1];
    v11 = v17;
    v2 = 0x11;
    v3 = 131;
    v4 = 65535;
    v5 = 0;
    v1 = a3;
    v6 = v1;
    v7 = 0;
    v1 = a0;
    v8 = v1;
    v1 = a1;
    v9 = v1;
    v10 = a2;
    v0 = 19;
    return sub_1002ade7(&v2);
}
```

## `sub_10040318` `0x10040318`

_814 bytes. calls BitBlt, CreateFileA; refs ".bmp", "'_'yyMMdd", "'_'HHmmss'.bmp'"_

```c
extern int g_10042f83;
extern int g_1005f7b1;
extern HANDLE g_102e2a94;
extern unsigned int g_102e2a98;
extern unsigned int g_102e2aa0;
extern unsigned int g_102e2aa8;
extern void g_102e2aac;
extern unsigned short g_102e2ac4;
extern unsigned int g_102e2ac6;
extern unsigned short g_102e2aca;
extern unsigned short g_102e2acc;
extern unsigned int g_102e2ace;
extern unsigned int g_102e2ad6;

int sub_10040318(unsigned int a0, int a1)
{
    void* v0;  // [bp-0x62c]
    HGDIOBJ v1;  // [bp-0x628]
    HDC v2;  // [bp-0x624]
    HBITMAP v3;  // [bp-0x620]
    HWND v4;  // [bp-0x61c]
    int v5[4];  // [bp-0x618]
    HDC v6;  // [bp-0x608]
    Byte v7[1024];  // [bp-0x604]
    Byte v8[512];  // [bp-0x204]

    v4 = sub_10039b62();
    SetWindowPos(v4, 0xffffffff, 0, 0, 0, 0, 3);
    GetWindowRect(v4, v5);
    v2 = GetWindowDC(v4);
    v6 = CreateCompatibleDC(v2);
    v3 = CreateCompatibleBitmap(v2, *((unsigned int *)((void*)v5 + 8)) - *((unsigned int *)v5), *((unsigned int *)((void*)v5 + 12)) - *((unsigned int *)((void*)v5 + 4)));
    v1 = SelectObject(v6, v3);
    BitBlt(v6, 0, 0, *((unsigned int *)((void*)v5 + 8)) - *((unsigned int *)v5), *((unsigned int *)((void*)v5 + 12)) - *((unsigned int *)((void*)v5 + 4)), v2, 0, 0, SRCCOPY);
    SelectObject(v6, v1);
    DeleteObject(v6);
    if (a0)
    {
        OpenClipboard(v4);
        EmptyClipboard();
        SetClipboardData(2, v3);
        CloseClipboard();
    }
    else
    {
        RtlZeroMemory(&g_102e2a98, 44);
        g_102e2a98 = 40;
        GetDIBits(v2, v3, 0, 0, NULL, &g_102e2a98, DIB_RGB_COLORS);
        v0 = LocalAlloc(GMEM_FIXED, *((int *)&g_102e2aac));
        g_102e2aa8 = 0;
        GetDIBits(v2, v3, 0, g_102e2aa0, v0, &g_102e2a98, DIB_RGB_COLORS);
        lstrcpy(v7, &g_10042f83);
        if (a1)
        {
            lstrcat(v7, a1);
            lstrcat(v7, ".bmp");
        }
        else
        {
            lstrcat(v7, &g_1005f7b1);
            GetDateFormatA(0x400, 0, NULL, "'_'yyMMdd", v8, 500);
            lstrcat(v7, v8);
            GetTimeFormatA(0x400, 0, NULL, "'_'HHmmss'.bmp'", v8, 500);
            lstrcat(v7, v8);
        }
        g_102e2a94 = CreateFileA(v7, 0xc0000000, 3, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_ARCHIVE, NULL);
        g_102e2aca = 0;
        g_102e2acc = 0;
        g_102e2ac6 = 54;
        g_102e2ac4 = 19778;
        g_102e2ace = 54;
        WriteFile(g_102e2a94, &g_102e2ac4, 14, &g_102e2ad6, NULL);
        WriteFile(g_102e2a94, &g_102e2a98, 40, &g_102e2ad6, NULL);
        WriteFile(g_102e2a94, v0, *((int *)&g_102e2aac), &g_102e2ad6, NULL);
        CloseHandle(g_102e2a94);
        LocalFree(v0);
    }
    ReleaseDC(v4, v2);
    return SetWindowPos(v4, 0xfffffffe, 0, 0, 0, 0, 3);
}
```

## `sub_10040900` `0x10040900`

_54 bytes. (leaf/helper — see body)_

```c
int sub_10040900(char *a0)
{
    unsigned int v0;  // ecx
    unsigned int v1;  // edx
    char v2;  // al
    char iter[2];  // esi

    v0 = 0;
    v1 = 0;
    v2 = *(a0);
    iter = a0 + 1;
    if (*(a0) == 2)
    {
        v2 = iter[0];
        v1 = ~(0);
        iter = &iter[1];
    }
    for (; v2; iter = &iter[1])
    {
        v0 = _INSERT(v2 CONCAT 0, 0, v2 - 48) + v0 * 10;
        v2 = iter[0];
    }
    return v0 + v1 ^ v1;
}
```

## `sub_10040940` `0x10040940`

_101 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10040940(unsigned int a0, void* a1)
{
    unsigned int v0;  // eax
    void* iter;  // edi
    unsigned int v2;  // 4101
    void* node;  // esi
    unsigned int v4;  // eax
    unsigned int v5;  // eax
    char v6;  // 4107

    v0 = a0;
    iter = a1;
    if (!v0)
    {
        *((unsigned short *)iter) = 48;
        return v0;
    }
    v2 = _ccall(8, 15, v0, 0, 0);
    if ((char)v2)
    {
        *((char *)iter) = 45;
        v0 = -(v0);
        iter += 1;
    }
    node = iter;
    while (true)
    {
        v4 = v0;
        if (v4 <= 0)
            break;
        v5 = v4 / 10;
        *((char *)iter) = (char)(v4 - v5 * 10) + 48;
        iter += 1;
        v0 = v5;
    }
    for (*((char *)iter) = 0; node < iter; node += 1)
    {
        iter -= 1;
        v6 = *((char *)iter);
        *((char *)iter) = *((char *)node);
        *((char *)node) = v6;
    }
    return v4;
}
```

## `sub_100409a8` `0x100409a8`

_42 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    char field_8;
} struct_0;

int sub_100409a8(unsigned int a0, struct_0 *a1)
{
    unsigned int v0;  // esi
    int v1;  // ecx
    char v2;  // al
    unsigned short v3;  // ax
    unsigned int v4;  // 4184
    unsigned int v5;  // 4186
    unsigned int v6;  // eax

    v0 = a0;
    a1->field_8 = 0;
    v1 = 7;
    do
    {
        v2 = v0;
        v3 = _INSERT(v2, 0, (v2 & 15) - 105 - ((v2 & 15) < 10));
        v4 = _ccall(10, (unsigned int)(v2 & 15), (unsigned int)(105 ^ (char)(char)((v2 & 15) < 10)), (unsigned int)(char)((v2 & 15) < 10));
        v5 = _ccall((unsigned short)v4 CONCAT v3, 47);
        a1->padding_0[v1] = _INSERT(v3, 0, v5);
        v0 >>= 4;
        v1 -= 1;
    } while (v1 - 1 >= 0);
    return v6;
}
```

## `sub_100409e0` `0x100409e0`

_77 bytes. (leaf/helper — see body)_

```c
int sub_100409e0(unsigned int *a0, unsigned int a1, unsigned int a2)
{
    unsigned int iter[8];  // edx
    unsigned int i;  // ecx
    unsigned int j;  // ecx

    iter = a0;
    i = a1 >> 5;
    if (i)
    {
        do
        {
            iter[0] = a2;
            iter[1] = a2;
            iter[2] = a2;
            iter[3] = a2;
            iter[4] = a2;
            iter[5] = a2;
            iter[6] = a2;
            iter[7] = a2;
            iter += 1;
            i -= 1;
        } while (i != 1);
    }
    a1 &= 31;
    if (!a1)
        return a2;
    j = a1 >> 2;
    do
    {
        iter[0] = a2;
        iter = &iter[1];
        j -= 1;
    } while (j != 1);
    return a2;
}
```

## `sub_10040a30` `0x10040a30`

_70 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005a280;

int sub_10040a30(unsigned int a0)
{
    unsigned int v0;  // eax

    v0 = g_1005a280;
    if ((g_1005a280 & 0x80000000))
        v0 = g_1005a280 + 2147483647;
    g_1005a280 = 16807 * (unsigned int)(v0 % 127773) - 2836 * (unsigned int)(v0 / 127773);
    return (16807 * (unsigned int)(v0 % 127773) - 2836 * (unsigned int)(v0 / 127773)) % a0;
}
```

## `sub_10040a76` `0x10040a76`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005a280;

int sub_10040a76(unsigned int a0)
{
    g_1005a280 = a0;
    return a0;
}
```

