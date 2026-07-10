# elfbot.dll decompiled — jdrv 0x1001193c..0x10015da3

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1001193c` `0x1001193c`

_333 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1001193c(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5)
{
    unsigned int v8;  // eax
    unsigned int v9;  // eax
    unsigned int v10;  // eax
    unsigned int iter;  // esi
    unsigned int node;  // edi
    unsigned int v13;  // ecx
    unsigned int v14;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int i;  // [bp-0x40]
    unsigned int v2;  // [bp-0x3c]
    unsigned int v3;  // [bp-0x38]
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]

    v8 = a3 - a5;
    if (v8 < 40)
    {
        v7 = 1;
        v5 = v8;
    }
    else
    {
        v7 = 4294967295;
        v5 = ~(v5) + 1;
    }
    v9 = a4 - a5;
    if (v9 < 40)
    {
        v6 = 1;
        v4 = v9;
    }
    else
    {
        v6 = 4294967295;
        v4 = ~(v4) + 1;
    }
    v3 = 0;
    if (v5 != v4)
    {
        if (v7 == 1 && v6 == 4294967295)
        {
            if (v4 <= v5)
                v3 = 1;
        }
        else
        {
            if (v7 == 4294967295 && v6 == 4294967295)
            {
                v3 = 1;
            }
            else if (v7 == 4294967295 && v6 == 1 && v4 > v5)
            {
                v3 = 1;
            }
        }
    }
    if (v3)
    {
        v2 = a0 + a3 - a5;
        i = a1 + a4 - a5;
        v7 = ~(v7) + 1;
        v6 = ~(v6) + 1;
    }
    else
    {
        v2 = a0;
        i = a1;
    }
    v10 = v5;
    if (v10 < v4)
        v10 = v4;
    v0 = v10;
    iter = 0;
    node = 0;
    v13 = 0;
    if (v3)
        v13 = 4294967295;
    for (; !*((char *)(a2 + i * 18 + v2)); i += v6)
    {
        v13 += 1;
        if (v13 >= v0)
            return 1;
        iter += v5;
        node += v4;
        v14 = v0;
        if (iter >= v14)
        {
            iter -= v14;
            v2 += v7;
        }
        if (node >= v14)
            node -= v14;
    }
    return 0;
}
```

## `sub_10011a89` `0x10011a89`

_105 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_10052770;
extern unsigned short g_1005398a[5];
extern unsigned short g_10053d68[5];
extern char g_100fa97b;

unsigned int sub_10011a89(unsigned short a0, unsigned short a1)
{
    unsigned short i[5];  // ebx

    if (!g_100fa97b)
        return g_100fa97b;
    for (i = &g_1005398a[0]; i < &g_10053d68[0]; i += 1)
    {
        if ((i[0] & (unsigned short)(1 << ((char)g_10052770 & 31))) && a0 >= i[1] && a0 <= i[2] && a1 >= i[3] && a1 <= i[4])
            return 1;
    }
    return 0;
}
```

## `sub_10011af2` `0x10011af2`

_2356 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[27];
    unsigned short field_1b;
    unsigned short field_1d;
    char field_1f;
} struct_0;

extern unsigned int g_10052768;
extern unsigned int g_1005276c;
extern unsigned int g_10052770;
extern unsigned int g_1005e6a0[12];
extern unsigned int g_1005f120[12];
extern char g_1005f7ed;
extern char g_101d5e29;

unsigned int sub_10011af2(int a0, unsigned int a1, struct_0 *index, unsigned int a3, unsigned int a4, unsigned int a5)
{
    int v39;  // ebx
    unsigned int i[12];  // ebx
    int v49;  // ecx
    int v50;  // ecx
    unsigned long v51;  // ldt
    unsigned long v52;  // gdt
    unsigned short v53;  // ss
    unsigned long v54;  // 4121
    int v55;  // ecx
    int v56;  // ecx
    int v57;  // ecx
    int v58;  // eax
    unsigned int v41[12];  // ebx
    int v59;  // ecx
    unsigned long v60;  // 4121
    unsigned int v61;  // ebx
    unsigned int v62;  // esi
    unsigned int v63;  // ebx
    unsigned int v64;  // eax
    unsigned int v65;  // edi
    char *v66;  // edx
    unsigned int v67;  // eax
    unsigned int v68;  // ecx
    unsigned int idx[12];  // ebx
    unsigned int v69;  // eax
    unsigned int v70;  // ecx
    unsigned int v71;  // ebx
    unsigned long v72;  // 4166
    unsigned long v73;  // 4170
    unsigned int v74;  // ebx
    unsigned int v75;  // esi
    unsigned int v76;  // ebx
    unsigned int v77;  // eax
    unsigned int v78;  // edi
    unsigned int v43;  // eax
    char *v79;  // edx
    unsigned int v80;  // eax
    unsigned int v81;  // ecx
    unsigned int v82;  // eax
    unsigned int v83;  // ecx
    unsigned int v84;  // edx
    unsigned int iter;  // ecx
    unsigned int v86;  // ebx
    unsigned int v87;  // esi
    unsigned int v88;  // ebx
    unsigned int v44;  // ecx
    unsigned int v89;  // eax
    unsigned int v90;  // edi
    unsigned int v91;  // edx
    unsigned int v92;  // eax
    unsigned int v93;  // ecx
    unsigned int v94;  // eax
    unsigned int v95;  // ecx
    unsigned int v96;  // ebx
    unsigned long v97;  // 4169
    unsigned long v98;  // 4173
    unsigned int v45;  // esi
    unsigned int v99;  // eax
    unsigned short v100;  // bx
    unsigned int n;  // ecx
    unsigned int v47;  // eax
    unsigned int v48;  // ecx
    unsigned int v0;  // [bp-0x8a0]
    unsigned int v1;  // [bp-0x89c]
    char *v2;  // [bp-0x898]
    char *v3;  // [bp-0x894]
    unsigned int v4;  // [bp-0x890]
    char *v5;  // [bp-0x88c], Other Possible Types: int, unsigned int
    unsigned int v6;  // [bp-0x888]
    int v7;  // [bp-0x884], Other Possible Types: unsigned int
    char v8;  // [bp-0x880]
    unsigned int v9[12];  // [bp-0x874]
    unsigned int v10;  // [bp-0x83c]
    unsigned int v11;  // [bp-0x838]
    unsigned int v12;  // [bp-0x834]
    unsigned int v13;  // [bp-0x830]
    unsigned int v14;  // [bp-0x82c]
    unsigned int v15;  // [bp-0x828]
    unsigned int v16;  // [bp-0x824]
    unsigned int v17;  // [bp-0x820]
    unsigned int v18;  // [bp-0x81c]
    unsigned int v19;  // [bp-0x818]
    unsigned int v20;  // [bp-0x814]
    unsigned int v21;  // [bp-0x810]
    unsigned int v22;  // [bp-0x80c]
    unsigned int idx1;  // [bp-0x808]
    unsigned int m;  // [bp-0x804]
    unsigned int i1;  // [bp-0x800]
    unsigned int iter2;  // [bp-0x7fc]
    unsigned int node;  // [bp-0x7f8]
    unsigned int k;  // [bp-0x7f4]
    unsigned int iter1;  // [bp-0x7f0]
    char v30;  // [bp-0x7ec]
    char v31;  // [bp-0x5f2]
    char v32;  // [bp-0x3f8]
    char v33;  // [bp-0x2fb]
    char v34;  // [bp-0x1fe]
    char v35;  // [bp-0x18a]
    char v36;  // [bp-0x101]
    char v37;  // [bp-0x8d]
    char v38;  // [bp-0x4]

    if (!a0 && !a1)
        return 4294967295;
    sub_1002ae81(&v32, 253, v39);
    sub_1002ae81(&v31, 506);
    sub_1002ae81(&v30, 506);
    sub_1002ae81(&v36, 253);
    sub_1002ae81(&v34, 253);
    sub_1002ae81(&v33, 253);
    sub_10024fae(&v33, 253);
    i = 0x63fef8;
    while (i < &g_1005f120[0])
    {
        v41 = i;
        if ((char)v41[3] && !((v41 = i, v41[11] != g_10052770 || (v9 = i, idx = i, v41 = idx, sub_10011a89((unsigned short)i[9], (unsigned short)i[10])))))
        {
            if (*((char *)&idx[0] + 3) < 64)
            {
                v41 = idx;
                if (!g_101d5e29)
                {
                    v41 = idx;
                    if (v41 != *((int *)&g_1005f7ed))
                    {
                        v43 = idx[9] - g_10052768 + 8;
                        v44 = idx[10] - g_1005276c + 6;
                        if (v43 < 18 && v44 < 14)
                            v37 += 1;
                        v41 = idx;
                        goto LABEL_10011c80;
                    }
                }
            }
            if (a0)
            {
                if (!lstrcmpi(a0, &idx[1]))
                    goto LABEL_10011c52;
                i = &idx[3 + 6];
            }
            else
            {
                v45 = sub_10023861() + 144;
                n = 12;
                while (n)
                {
                    if (*((char *)v45) != (char)a1)
                    {
                        n -= 1;
                        v45 += 1;
                    }
                    else
                    {
LABEL_10011c52:
                        v47 = idx[9] - g_10052768 + 8;
                        v48 = idx[10] - g_1005276c + 6;
                        v41 = idx;
                        if (v47 < 18)
                        {
                            v41 = idx;
                            if (v48 < 14)
                            {
                                v35 += 1;
                                v41 = idx;
                                goto LABEL_10011c80;
                            }
                        }
                    }
                }
                i = &idx[3 + 6];
            }
        }
        else
        {
LABEL_10011c80:
            if (v41 == 6595168)
                i = &g_1005e6a0[0];
        }
    }
    for (iter2 = 0; iter2 < 14; iter2 += 1)
    {
        v49 = g_1005276c - 6 + iter2;
        node = 0;
        while (true)
        {
            v50 = v49;
            if (node >= 18)
                break;
            v7 = g_10052768 - 8 + node;
            if (sub_1003c87c(g_10052768 - 8 + node, v50, v50))
            {
                v54 = _ccall(v51, v52, (unsigned int)v53, &v32 + iter2 * 18 + node);
                *((char *)v54) = 1;
                node += 1;
                v49 = v7;
            }
            else
            {
                node += 1;
                v49 = v7;
            }
        }
    }
    for (iter2 = 0; iter2 < 14; iter2 += 1)
    {
        v55 = g_1005276c - 6 + iter2;
        node = 0;
        while (true)
        {
            v56 = v55;
            if (node >= 18)
                break;
            v7 = v56;
            v57 = v56;
            if (sub_10011678(g_10052768 - 8 + node, v56, &v32))
            {
                v58 = node + g_10052768 - 8;
                v59 = iter2 + g_1005276c - 6;
                if (sub_1003c9bd(v58, v59, v59, v58, v57))
                {
                    v5 = v59;
                    if (!sub_10011a89(v59, v58))
                    {
                        v60 = _ccall(v51, v52, (unsigned int)v53, &v33 + iter2 * 18 + node);
                        *((char *)v60) = 1;
                        node += 1;
                        v55 = v59;
                    }
                    else
                    {
                        node += 1;
                        v55 = v59;
                    }
                }
                else
                {
                    node += 1;
                    v55 = v59;
                }
            }
            else
            {
                node += 1;
                v55 = v57;
            }
        }
    }
    v14 = 0;
    v10 = 0;
    if (a3)
    {
        v19 = 0;
        v15 = 0;
        v11 = 0;
        node = 8;
        iter2 = 6;
        for (k = 0; k < 13; k += 1)
        {
            v61 = k;
            v62 = v61;
            if (v62 > 6)
                v62 = 12 - v61;
            v63 = v61 * 13;
            iter1 = 0;
            while (iter1 < 13)
            {
                v64 = iter1;
                v65 = v64;
                if (v65 > 6)
                    v65 = 12 - v64;
                v66 = v63 + v64 + a3;
                if (*(v66))
                {
                    v67 = v64 + node;
                    if (v67 < 6)
                    {
                        iter1 += 1;
                    }
                    else if (v67 < 24)
                    {
                        v68 = iter2 + k;
                        if (v68 < 6)
                        {
                            iter1 += 1;
                        }
                        else if (v68 < 20)
                        {
                            v7 = v67 - 6;
                            v6 = v68;
                            v5 = v66;
                            v4 = v63;
                            v3 = &v8;
                            v2 = &v38;
                            v1 = v62;
                            v0 = v65;
                            if (sub_1001193c(node, iter2, &v32, iter1, k, 6))
                            {
                                v62 = v1;
                                v69 = v67 - 6 + (v68 - 6) * 18;
                                v19 += (&v36)[v69];
                                v70 = (&v34)[v69];
                                v15 += v70;
                                if (v70)
                                {
                                    v11 += v70 * (v0 + v62);
                                    iter1 += 1;
                                }
                                else
                                {
                                    iter1 += 1;
                                }
                            }
                            else
                            {
                                v62 = v1;
                                iter1 += 1;
                            }
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
                else
                {
                    iter1 += 1;
                }
            }
        }
        v71 = iter2 * 18 + node;
        v72 = _ccall(v51, v52, (unsigned int)v53, &v31 + v71);
        *((char *)v72) = v19;
        v73 = _ccall(v51, v52, (unsigned int)v53, &v30 + v71);
        *((char *)v73) = v15;
        if (!v19 && (v15 > v14 || v15 == v14 && v11 > v10))
        {
            v14 = v15;
            v7 = node;
            v13 = node;
            v7 = iter2;
            v12 = iter2;
            v7 = v11;
            v10 = v11;
        }
    }
    else
    {
        if (a4)
        {
            v19 = 0;
            v20 = 0;
            v21 = 0;
            v22 = 0;
            v15 = 0;
            v16 = 0;
            v17 = 0;
            v18 = 0;
            v11 = 0;
            node = 8;
            iter2 = 6;
            for (k = 0; k < 0x11; k += 1)
            {
                v74 = k;
                v75 = v74;
                if (v75 > 8)
                    v75 = 16 - v74;
                v76 = v74 * 0x11;
                iter1 = 0;
                while (iter1 < 0x11)
                {
                    v77 = iter1;
                    v78 = v77;
                    if (v78 > 8)
                        v78 = 16 - v77;
                    v79 = v76 + v77 + a4;
                    if (*(v79))
                    {
                        idx1 = *(v79);
                        v80 = v77 + node;
                        if (v80 < 8)
                        {
                            iter1 += 1;
                        }
                        else if (v80 < 26)
                        {
                            v81 = iter2 + k;
                            if (v81 < 8)
                            {
                                iter1 += 1;
                            }
                            else if (v81 < 22)
                            {
                                v7 = v80 - 8;
                                v6 = v81;
                                v5 = idx1;
                                v4 = v76;
                                v3 = &v8;
                                v2 = &v38;
                                v1 = v75;
                                v0 = v78;
                                if (sub_1001193c(node, iter2, &v32, iter1, k, 8))
                                {
                                    v75 = v1;
                                    v82 = v80 - 8 + (v81 - 8) * 18;
                                    (&v18)[idx1] = (&v18)[idx1] + (&v36)[v82];
                                    v83 = (&v34)[v82];
                                    (&v14)[idx1] = (&v14)[idx1] + v83;
                                    if (v83)
                                    {
                                        v11 += v83 * (v0 + v75);
                                        iter1 += 1;
                                    }
                                    else
                                    {
                                        iter1 += 1;
                                    }
                                }
                                else
                                {
                                    v75 = v1;
                                    iter1 += 1;
                                }
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
                    else
                    {
                        iter1 += 1;
                    }
                }
            }
            v84 = 0;
            iter = 0;
            while (iter < 4)
            {
                if ((&v19)[iter])
                {
                    iter += 1;
                }
                else if ((&v15)[iter] > v84)
                {
                    v84 = (&v15)[iter];
                    idx1 = iter + 1;
                    iter += 1;
                }
                else
                {
                    iter += 1;
                }
            }
            if (!v84)
                return 4294967295;
            *((char *)&index->field_1d + 1) = idx1;
            return v84;
        }
        for (m = 0; m < 11; m += 1)
        {
            iter2 = m + 1;
            i1 = 0;
            while (i1 < 15)
            {
                node = i1 + 1;
                if ((&v33)[18 * iter2 + node])
                {
                    v19 = 0;
                    v15 = 0;
                    v11 = 0;
                    for (k = 0; k < 7; k += 1)
                    {
                        v86 = k;
                        v87 = v86;
                        if (v87 > 3)
                            v87 = 6 - v86;
                        v88 = v86 * 7;
                        iter1 = 0;
                        while (iter1 < 7)
                        {
                            v89 = iter1;
                            v90 = v89;
                            if (v90 > 3)
                                v90 = 6 - v89;
                            v91 = v88 + v89 + a5;
                            if (*((char *)v91))
                            {
                                v92 = v89 + node;
                                if (v92 < 3)
                                {
                                    iter1 += 1;
                                }
                                else if (v92 < 21)
                                {
                                    v93 = iter2 + k;
                                    if (v93 < 3)
                                    {
                                        iter1 += 1;
                                    }
                                    else if (v93 < 0x11)
                                    {
                                        v7 = v92 - 3;
                                        v6 = v93;
                                        v5 = v91;
                                        v4 = v88;
                                        v3 = &v8;
                                        v2 = &v38;
                                        v1 = v87;
                                        v0 = v90;
                                        if (sub_100117ef(node, iter2, &v32, iter1, k))
                                        {
                                            v87 = v1;
                                            v94 = v92 - 3 + (v93 - 3) * 18;
                                            v19 += (&v36)[v94];
                                            v95 = (&v34)[v94];
                                            v15 += v95;
                                            if (v95)
                                            {
                                                v11 += v95 * (v0 + v87);
                                                iter1 += 1;
                                            }
                                            else
                                            {
                                                iter1 += 1;
                                            }
                                        }
                                        else
                                        {
                                            v87 = v1;
                                            iter1 += 1;
                                        }
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
                            else
                            {
                                iter1 += 1;
                            }
                        }
                    }
                    v96 = iter2 * 18 + node;
                    v97 = _ccall(v51, v52, (unsigned int)v53, &v31 + v96);
                    *((char *)v97) = v19;
                    v98 = _ccall(v51, v52, (unsigned int)v53, &v30 + v96);
                    *((char *)v98) = v15;
                    if ((vvar_1586{s-2088|4b} == 0x0<32>)) { Goto None } else { Goto None }
                    if (!v19)
                    {
                        if (v15 <= v14)
                        {
                            if (v15 != v14)
                            {
                                i1 += 1;
                                continue;
                            }
                            else if (v11 <= v10)
                            {
                                i1 += 1;
                                continue;
                            }
                        }
                        v14 = v15;
                        v7 = node;
                        v13 = node;
                        v7 = iter2;
                        v12 = iter2;
                        v7 = v11;
                        v10 = v11;
                        i1 += 1;
                    }
                    else
                    {
                        i1 += 1;
                    }
                }
                else
                {
                    i1 += 1;
                }
            }
        }
    }
    v99 = 4294967295;
    if (v14)
    {
        v100 = (unsigned short)v12 + (unsigned short)g_1005276c;
        *((unsigned short *)&(index->padding_0)[1]) = v13 + g_10052768 - 8;
        *((unsigned short *)((char *)&index->field_1b + 1)) = v100 - 6;
        *((char *)&index->field_1d + 1) = g_10052770;
        v99 = v14;
    }
    return v99;
}
```

## `sub_10011c25` `0x10011c25`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10011c25(void)
{
}
```

## `sub_100121bd` `0x100121bd`

_5 bytes. (leaf/helper — see body)_

```c
void sub_100121bd(void)
{
}
```

## `sub_1001242d` `0x1001242d`

_831 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_10052785[4];
extern unsigned int g_10052b1d;
extern unsigned int g_10052b2d;
extern unsigned int g_10052c2d;
extern unsigned int g_10052c3d;
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern int g_1005f85c;
extern unsigned int g_100f0dcc;

unsigned int sub_1001242d(int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v8;  // ebx
    unsigned int v9;  // eax
    unsigned int v10;  // ebx
    unsigned int j;  // ecx
    unsigned int v12;  // ecx
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x20]
    unsigned int iter2;  // [bp-0x1c]
    unsigned int iter1;  // [bp-0x18]
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    unsigned int node;  // [bp-0xc]
    unsigned int iter;  // [bp-0x8]

    if (g_100f0dcc)
        return 0;
    v0 = v8;
    node = 0;
    v5 = 0;
    v4 = 0;
    iter1 = 0;
    for (iter2 = 0; node < 5; node += 1)
    {
        iter = 0;
        while (iter < 5)
        {
            if (g_10052785[156 + 36 * node + 2 * iter] != 0xfffffffe)
            {
                iter += 1;
            }
            else if (iter != 2 || node != 2)
            {
                if (!iter || !node || iter == 4 || node == 4)
                    v4 += 1;
                else
                    v5 += 1;
                if (iter < 2)
                {
                    iter1 -= iter + 1;
                }
                else if (iter > 2)
                {
                    iter1 += 5 - iter;
                }
                if (node < 2)
                {
                    iter2 -= node + 1;
                    iter += 1;
                }
                else if (node > 2)
                {
                    iter2 += 5 - node;
                    iter += 1;
                }
                else
                {
                    iter += 1;
                }
            }
            else
            {
                iter += 1;
            }
        }
    }
    if (v5 && v4 + v5 > 2)
    {
        sub_100151f4(3);
        v9 = iter1;
        if (v9 > 1000)
            v9 = -(v9);
        v10 = iter1;
        if (v10 > 1000)
            v10 = -(v10);
        v1 = (v9 <= v10 ? (v10 < v9 ? 0 : sub_10040a30(2)) : 0);
        while (true)
        {
            if (!(unsigned short)v1)
            {
                if (iter1)
                {
                    if (iter1 < 1000)
                    {
                        if (g_10052b1d < 0xfffffffe)
                            return sub_10015204(4294967295 + g_1005f854, 0 + g_1005f858, g_1005f85c);
                        iter = 4294967295;
                    }
                    else
                    {
                        if (g_10052b2d < 0xfffffffe)
                            return sub_10015204(1 + g_1005f854, 0 + g_1005f858, g_1005f85c);
                        iter = 1;
                    }
                }
                if (v1 > 1)
                    break;
                v1 = 65537;
            }
            else
            {
                if ((unsigned short)v1 != 1)
                    break;
                if (iter1)
                {
                    if (iter2 < 1000)
                    {
                        if (g_10052c2d < 0xfffffffe)
                            return sub_10015204(0 + g_1005f854, 4294967295 + g_1005f858, g_1005f85c);
                        node = 4294967295;
                    }
                    else
                    {
                        if (g_10052c3d < 0xfffffffe)
                            return sub_10015204(0 + g_1005f854, 1 + g_1005f858, g_1005f85c);
                        node = 1;
                    }
                }
                if (v1 > 1)
                    break;
                v1 = 0x10000;
            }
        }
        if (!iter)
            iter = 1;
        if (!node)
            node = 1;
        j = 0;
        while (j < 4)
        {
            if (g_10052785[232 + 36 * node + 2 * iter] < 0xfffffffe)
                return sub_10015204(iter + g_1005f854, node + g_1005f858, g_1005f85c);
            v12 = j;
            if (!j)
            {
                iter = ~(iter);
                iter += 1;
                j = v12 + 1;
            }
            else if (v12 == 1)
            {
                iter = ~(iter);
                iter += 1;
                node = ~(node);
                node += 1;
                j = 2;
            }
            else if (v12 == 2)
            {
                iter = ~(iter);
                iter += 1;
                j = 3;
            }
            else
            {
                j = v12 + 1;
            }
        }
        sub_100151f4(0);
        return 4294967295;
    }
    if (!a2)
        return 4294967295;
    sub_10013e4d(a0);
    return 4294967295;
}
```

## `sub_10012609` `0x10012609`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10012609(void)
{
}
```

## `sub_10012771` `0x10012771`

_180 bytes. (leaf/helper — see body)_

```c
int sub_10012771(void* a0, int a1, void* a2)
{
    void* iter;  // esi
    void* v1;  // edi
    void* v3;  // edi
    void* v4;  // edi
    unsigned int v5;  // eax
    void* v6;  // edi
    unsigned int v7;  // eax

    if (*((int *)a2) != 4294966944)
        return sub_1002ae6f(a0, a2, a1);
    sub_1002ae81(a0, a1);
    iter = a2 + 4;
    v1 = a0;
    while (true)
    {
        if (*((char *)iter) >= 192)
        {
            v1 += _INSERT((char)iter[1], 1, *((char *)iter) & 63);
            iter += 2;
        }
        else if (*((char *)iter) >= 128)
        {
            v3 = v1 + (*((char *)iter) & 63);
            *((int *)v3) = (int)iter[1];
            iter += 5;
            v1 = v3 + 4;
        }
        else if (*((char *)iter) >= 64)
        {
            v4 = v1 + (*((char *)iter) & 63);
            *((short *)v4) = (short)iter[1];
            iter += 3;
            v1 = v4 + 2;
        }
        else
        {
            v5 = *((char *)iter) & 63;
            v6 = v1 + v5;
            v7 = _INSERT(v5, 0, (char)iter[1]);
            if (!(char)iter[1])
                break;
            *((char *)v6) = v7;
            iter += 2;
            v1 = v6 + 1;
        }
    }
    return v7;
}
```

## `sub_10012813` `0x10012813`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10012813(void)
{
}
```

## `sub_10012827` `0x10012827`

_647 bytes. refs "others", "invisible"_

```c
extern char g_100544a4;
extern char g_100f0d3b;
extern void g_101d5e78;
extern void g_101dfe78;

void* sub_10012827(unsigned int a0, unsigned int a1, unsigned int a2)
{
    void* iter;  // ebx
    unsigned int v6;  // ecx
    void* node;  // esi
    unsigned int j;  // ecx
    unsigned int idx;  // edx
    unsigned int index[39];  // eax
    unsigned int v7;  // eax
    unsigned int v8;  // esi
    unsigned int v11;  // edx
    unsigned int v12;  // ecx
    unsigned int i;  // esi
    unsigned int v14;  // eax
    void* v0;  // [bp-0x1c], Other Possible Types: unsigned int
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    void* v3;  // [bp-0xc]
    unsigned int iter1;  // [bp-0x8]

    iter1 = 0;
    v3 = NULL;
    v2 = 0;
    v1 = 0;
    iter = &g_101d5e78;
    while (true)
    {
        if (iter >= &g_101dfe78)
            return v3;
        if (*((char *)iter))
        {
            if (g_100f0d3b && !a1)
            {
                v6 = (char)iter[33];
                v7 = (int)iter[116] & 63;
                v8 = (char)iter[0x22];
                if (v7 >= 15 && v7 <= 32 && (v8 = (unsigned int)(char)(char)iter[122], !v8))
                    goto LABEL_10012a2f;
                if (_INSERT(v6, 0, (char)v6 & 1) && v8 != (v6 >> 1) + 1 || !_INSERT(v6, 0, (char)v6 & 1) && v8 < (v6 >> 1) + 1 || v8 == 0xff)
                    goto LABEL_10012a2f;
                if ((*((int *)iter) | 0x20202020) == 1702125923 && ((int)iter[4] | 0x20202020) == 2037542759 && !a2)
                {
                    v11 = (char)iter[8];
                    if ((char)v11 == 32)
                        v11 = _INSERT(v11, 0, (char)iter[9]);
                    if (v11)
                    {
                        v12 = 12;
                        for (i = sub_10023861(v11) + 144; v12; i += 1)
                        {
                            if (*((char *)i) == (char)v11)
                                return iter;
                            v12 -= 1;
                        }
                    }
                    goto LABEL_10012a2f;
                }
            }
            if (*((char *)iter) >= 48 && *((char *)iter) <= 57 && (v14 = sub_10040900(iter), sub_10040900(iter) == *((int *)a0)))
            {
                if (!a1)
                    return iter;
            }
            else
            {
                if (*((int *)(a0 + 148)) && *((char *)(a0 + 3)) != 64 && !lstrcmpi(iter, "pk") && *((char *)(sub_10023861() + 137)))
                {
                    if (!a1)
                        return iter;
                }
                else
                {
                    if (!lstrcmpi(iter, a0 + 4))
                    {
                        if (!a1)
                            return iter;
                    }
                    else
                    {
                        if (*((char *)(a0 + 3)) == 64)
                        {
                            if (!lstrcmpi(iter, "others"))
                            {
                                v0 = iter;
                                iter = iter;
                                if (!sub_1000d287(a0 + 4))
                                {
                                    if (!a1)
                                    {
                                        v3 = iter;
                                        v0 = iter1;
                                        v2 = iter1;
                                    }
                                    else
                                    {
                                        *((char *)&iter[0x22]) = (char)iter[0x22] + 1;
                                    }
                                    goto LABEL_10012a2f;
                                }
                            }
                            else if (!*((int *)(a0 + 96)) && !*((int *)(a0 + 100)) && !lstrcmpi(iter, "invisible"))
                            {
                                if (!a1)
                                    return iter;
                                *((char *)&iter[0x22]) = (char)iter[0x22] + 1;
                                goto LABEL_10012a2f;
                            }
                        }
                    }
                }
            }
            *((char *)&iter[0x22]) = (char)iter[0x22] + 1;
            if (!v1)
            {
                node = iter + 36;
                for (j = 12; j && (idx = (unsigned int)(char)*((char *)node), idx); j -= 1)
                {
                    if ((char)idx != 32)
                        (&g_100544a4)[idx] = (&g_100544a4)[idx] + 1;
                    node += 1;
                }
                index = sub_10023861();
                index[36] = (int)iter[36];
                index[37] = (int)iter[40];
                index[38] = (int)iter[44];
                v1 = 1;
            }
            iter += 320;
            iter1 += 1;
        }
        else
        {
LABEL_10012a2f:
            iter += 320;
            iter1 += 1;
        }
    }
}
```

## `sub_10012aae` `0x10012aae`

_713 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[116];
    unsigned int field_74;
} struct_0;

extern unsigned int g_10053200;
extern unsigned int g_10053231;
extern unsigned int g_10053262;
extern unsigned int g_1005330b;
extern unsigned int g_100533b4;
extern unsigned int g_1005345d;
extern unsigned int g_10053506;
extern unsigned int g_10053627;
extern unsigned int g_10053748;
extern unsigned int g_10053869;
extern char g_100544a4;
extern void g_101d5e78;
extern void g_101dfe78;

void sub_10012aae(void)
{
    void* iter;  // ebx
    unsigned int v7;  // edx
    unsigned int v8;  // edx
    unsigned int v9;  // ecx
    unsigned int j;  // ecx
    struct_0 *index;  // esi
    unsigned int v12;  // ecx
    char v13;  // al
    struct_0 *v0;  // [bp-0x18]
    void* v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    void* v4;  // [bp-0x8]

    iter = &g_101d5e78;
    while (iter < &g_101dfe78)
    {
        if (*((char *)iter))
        {
            if ((*((int *)iter) | 0x20202020) == 1702125923 && ((int)iter[4] | 0x20202020) == 2037542759)
            {
                v7 = (char)iter[8];
                if ((char)v7 == 32)
                    v7 = _INSERT(v7, 0, (char)iter[9]);
                v8 = v7;
                if (!v7)
                    goto LABEL_10012b18;
                *((char *)&iter[0x22]) = (&g_100544a4)[v8];
                v3 = v8;
                v4 = NULL;
            }
            else
            {
                v4 = iter;
                v3 = 0;
            }
            v9 = (char)iter[33];
            if (!v9 || (char)iter[0x22] >= v9 + 1 >> 1)
            {
                for (j = 0; j < 4; j = v2 + 1)
                {
                    v2 = j;
                    index = iter + j * 56 + 96;
                    if (*((int *)&index->padding_0[12]) || *((int *)&index->padding_0[8]))
                    {
                        v12 = *((int *)&index->padding_0[20]) & 63;
                        v1 = iter;
                        v0 = index;
                        v13 = 255;
                        if (v12 >= 15 && v12 <= 18)
                        {
                            v13 = sub_10011af2(v4, v3, index, 0, 0, &g_10053200);
                        }
                        else if (v12 == 32)
                        {
                            v13 = sub_10011af2(v4, v3, index, 0, 0, &g_10053231);
                        }
                        else if (v12 == 19 || v12 == 20)
                        {
                            if (*((int *)0x63fe78) >= 160)
                                v13 = sub_10011af2(v4, v3, index, &g_1005345d, 0, 0);
                        }
                        else
                        {
                            if (v12 == 21)
                            {
                                if (*((int *)0x63fe78) >= 340)
                                    v13 = sub_10011af2(v4, v3, index, &g_1005330b, 0, 0);
                            }
                            else
                            {
                                if (v12 == 22 || v12 == 24)
                                {
                                    if (*((int *)0x63fe78) >= 1200)
                                        v13 = sub_10011af2(v4, v3, index, &g_100533b4, 0, 0);
                                }
                                else
                                {
                                    if (v12 == 23 || v12 == 25)
                                    {
                                        if (v12 == 23 && *((int *)0x63fe78) >= 650 || v12 == 25 && *((int *)0x63fe78) >= 770)
                                            v13 = sub_10011af2(v4, v3, index, &g_10053262, 0, 0);
                                    }
                                    else
                                    {
                                        if (v12 == 26)
                                        {
                                            if (*((int *)0x63fe78) >= 40)
                                                v13 = sub_10011af2(v4, v3, index, 0, &g_10053627, 0);
                                        }
                                        else
                                        {
                                            if (v12 == 27)
                                            {
                                                if (*((int *)0x63fe78) >= 110)
                                                    v13 = sub_10011af2(v4, v3, index, 0, &g_10053506, 0);
                                            }
                                            else
                                            {
                                                if (v12 == 28 || v12 == 29)
                                                {
                                                    if (*((int *)0x63fe78) >= 25)
                                                        v13 = sub_10011af2(v4, v3, index, 0, &g_10053869, 0);
                                                }
                                                else
                                                {
                                                    if (!(v12 == 30 || v12 == 31))
                                                    {
                                                        v13 = (char)iter[0x22];
                                                    }
                                                    else if (v12 == 30 && *((int *)0x63fe78) >= 0xaa || v12 == 31 && *((int *)0x63fe78) >= 210)
                                                    {
                                                        v13 = sub_10011af2(v4, v3, index, 0, &g_10053748, 0);
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                        iter = v1;
                        v0->padding_0[26] = v13;
                    }
                    else
                    {
                        index->padding_0[26] = 255;
                    }
                }
                iter += 320;
                continue;
            }
LABEL_10012d4c:
            *((char *)&iter[122]) = 255;
            *((char *)&iter[178]) = 255;
            *((char *)&iter[234]) = 255;
            *((char *)&iter[290]) = 255;
            iter += 320;
        }
        else
        {
LABEL_10012b18:
            goto LABEL_10012d4c;
        }
    }
    return;
}
```

## `sub_10012b08` `0x10012b08`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10012b08(void)
{
}
```

## `sub_10012d79` `0x10012d79`

_196 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[136];
    unsigned int field_88;
} struct_0;

unsigned int sub_10012d79(struct_0 *a0, unsigned int idx)
{
    unsigned int v0;  // eax
    unsigned int v1;  // esi
    unsigned int v2;  // edi
    unsigned int v3;  // esi
    unsigned int v4;  // edi
    unsigned int v5;  // esi
    unsigned int v6;  // edi
    unsigned int v7;  // esi
    unsigned int v8;  // edi

    v0 = a0->field_88;
    v1 = *((int *)(idx + 104));
    v2 = *((int *)(idx + 108));
    if ((v1 <= v2 || v0 > v1 || v0 < v2) && (v1 > v2 || v0 < v1 || v0 > v2))
    {
        v3 = *((int *)(idx + 160));
        v4 = *((int *)(idx + 164));
        if ((v3 <= v4 || v0 > v3 || v0 < v4) && (v3 > v4 || v0 < v3 || v0 > v4))
        {
            v5 = *((int *)(idx + 216));
            v6 = *((int *)(idx + 220));
            if ((v5 <= v6 || v0 > v5 || v0 < v6) && (v5 > v6 || v0 < v5 || v0 > v6))
            {
                v7 = *((int *)(idx + 272));
                v8 = *((int *)(idx + 276));
                if (v7 > v8 && v0 <= v7 && v0 >= v8)
                    return idx + 264;
                if (v7 > v8)
                {
                    return 0;
                }
                else if (v0 < v7)
                {
                    return 0;
                }
                else if (v0 > v8)
                {
                    return 0;
                }
                return idx + 264;
            }
            return idx + 208;
        }
        return idx + 152;
    }
    return idx + 96;
}
```

## `sub_10012e3d` `0x10012e3d`

_158 bytes. (leaf/helper — see body)_

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
extern char g_1005f85c;
extern char g_100771fe[4];
extern char g_101dfe9f;

unsigned int sub_10012e3d(unsigned int *index)
{
    struct_0 *iter;  // ebx
    int v1;  // eax
    int v2;  // eax

    if (g_100771fe[156 * (unsigned long long)(index + 0x18ffbe) / 168])
        return 0;
    for (iter = 0x63fef8; iter < 0x64a308; iter = &iter[1].padding_4[16])
    {
        if (iter->field_90 && iter->field_3 != 64 && iter != *((int *)&g_1005f7ed) && iter->field_2c == *((int *)&g_1005f85c))
        {
            v1 = iter->field_24 - index[9];
            v2 = iter->field_28 - index[10];
            if ((v2 ^ v2 >> 31) - (v2 >> 31) <= *((int *)&g_101dfe9f) && (v1 ^ v1 >> 31) - (v1 >> 31) <= *((int *)&g_101dfe9f))
                return 1;
        }
    }
    return 0;
}
```

## `sub_10012edb` `0x10012edb`

_3941 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[80];
    unsigned int field_50;
} struct_0;

typedef struct struct_7 {
    char padding_0[48];
    struct struct_8 *field_30;
} struct_7;

typedef struct struct_5 {
    struct struct_0 *field_0;
    int field_4;
    int field_8;
} struct_5;

typedef struct struct_8 {
    unsigned int field_0;
} struct_8;

typedef struct struct_9 {
    struct struct_7 *field_0;
} struct_9;

extern unsigned int g_10008a16[4];
extern unsigned int g_10008a1a[4];
extern char g_1001302e;
extern char g_10013542;
extern char g_100135a4;
extern char g_100137a3;
extern char g_1001393c;
extern char g_10013e4b;
extern unsigned int g_100432af;
extern int g_10043344;
extern char g_10043349;
extern char g_1004334b;
extern unsigned short g_1004334c;
extern char g_1004334e;
extern char g_10043351;
extern char g_10043354;
extern int g_10043355;
extern unsigned short g_1004335d;
extern char g_1004335f;
extern char g_10043362;
extern char g_10043364;
extern struct_9 *g_10052678;
extern void* g_10052768;
extern unsigned int g_1005276c;
extern unsigned int g_10052770;
extern struct_5 *g_10052778;
extern unsigned int g_1005277c;
extern unsigned int g_10052780;
extern char g_10052784;
extern int g_100544a4;
extern unsigned int g_1005db9c;
extern unsigned int g_1005dba0;
extern unsigned int g_1005dba4;
extern unsigned int g_1005dba8;
extern void g_1005e5a0;
extern void g_1005e6a0;
extern void g_1005f120;
extern struct_0 *g_1005f7ed;
extern char g_1005f854;
extern char g_1005f858;
extern char g_1005f85c;
extern struct_0 g_10077175;
extern struct_0 g_10080b05;
extern char g_1008b89f;
extern unsigned int g_100f0db0;
extern unsigned int g_100f0dc0;
extern unsigned int g_100f0dc4;
extern unsigned int g_100f0dcc;
extern unsigned int g_100f0dd8;
extern unsigned int g_100f0ddc;
extern unsigned int g_100f0e20;
extern unsigned int g_100f0e24;
extern unsigned int g_100f0e28;
extern unsigned int g_100f0e2c;
extern char g_100f9327;
extern unsigned int g_101d5e78;
extern unsigned int g_101dfe78;
extern unsigned int g_101dfe7c;
extern unsigned int g_101dfe80;
extern unsigned int g_101dfe84;
extern unsigned int g_101dfe88;
extern unsigned int g_101dfe8c;
extern unsigned int g_101dfe94;
extern char g_101dfe9c;
extern char g_101dfe9d;
extern char g_101dfe9e;
extern unsigned int g_101dfe9f;
extern unsigned int g_1028987c;
extern char g_10289880;
extern char g_10289884;
extern unsigned int g_63fe60;
extern unsigned int g_63fe64;
extern unsigned int g_63fed4;
extern unsigned int g_63fed8;
extern unsigned int g_63fedc;
extern unsigned int g_799ce8;
extern unsigned int g_799cec;

void* sub_10012edb(unsigned int a0, char a1)
{
    void* v38;  // eax
    unsigned int *node;  // ebx
    void* idx;  // esi
    int v49;  // eax
    unsigned int v50;  // edi
    int v51;  // eax
    unsigned int v52;  // eax
    unsigned int v53;  // eax
    void* idx1;  // eax
    unsigned int v55;  // eax
    unsigned int v56;  // ecx
    unsigned int v57[4];  // ecx
    struct_0 *iter;  // ebx
    unsigned int v58[4];  // ecx
    unsigned int v59;  // eax
    char v60;  // dl
    unsigned int v61;  // ecx
    unsigned int v62;  // ecx
    void* idx2;  // ecx
    struct_0 *v64;  // eax
    struct_0 *v65;  // eax
    void* v66;  // esi
    void* k;  // esi
    int v67;  // eax
    unsigned int v68;  // ecx
    int v69;  // eax
    unsigned int v70;  // eax
    void* v71;  // ecx
    unsigned int v72;  // edx
    void* v73;  // ecx
    void* iter1;  // edi
    void* v43;  // esi
    void* v44;  // esi
    unsigned int v45;  // eax
    char v46[140];  // eax
    void* v47;  // esi
    unsigned int v0;  // [bp-0x154]
    void* v1;  // [bp-0x150]
    void* v2;  // [bp-0x148]
    struct_0 *v3;  // [bp-0x144]
    void* v4;  // [bp-0x140]
    char *v5;  // [bp-0x130]
    struct_7 **v6;  // [bp-0x128]
    void* v7;  // [bp-0x11c], Other Possible Types: unsigned int
    int <0x10012edb[is_15]|Stack bp-0x118, 1 B>;  // [bp-0x118]
    unsigned int v8;  // [bp-0x118]
    char v9;  // [bp-0x114]
    char v10;  // [bp-0x100]
    unsigned int v11;  // [bp-0xdc]
    unsigned int v12;  // [bp-0xd8]
    unsigned int v13;  // [bp-0xd4]
    struct_0 *v14;  // [bp-0x58]
    unsigned short v15;  // [bp-0x54]
    char v16;  // [bp-0x52]
    char v17;  // [bp-0x51]
    char v18;  // [bp-0x50]
    char v19;  // [bp-0x4f]
    unsigned int v20;  // [bp-0x34]
    unsigned int v21;  // [bp-0x30]
    unsigned int v22;  // [bp-0x2c]
    unsigned int v23;  // [bp-0x2c]
    unsigned int v24;  // [bp-0x2c]
    void* v25;  // [bp-0x28]
    void* v26;  // [bp-0x24]
    void* v27;  // [bp-0x24]
    void* v28;  // [bp-0x24]
    void* v29;  // [bp-0x20]
    unsigned int v30;  // [bp-0x1c]
    unsigned int v31;  // [bp-0x18]
    void* v32;  // [bp-0x14]
    void* v33;  // [bp-0x10]
    unsigned int iter2;  // [bp-0xc]
    void* v35;  // [bp-0x8]
    char v36;  // [bp-0x4]

    if (g_100f0dcc)
        return v38;
    v30 = 0;
    v29 = NULL;
    g_100f0e20 = 0;
    v21 = 1;
    v31 = 0;
    v20 = 0;
    g_1005dba8 = &v36;
    g_1005dba4 = &v10;
    g_1005db9c = 400;
    g_1005dba0 = &g_1001302e;
    for (node = &g_101d5e78; node < &g_101dfe78; node += 80)
    {
        *((char *)&node[8] + 2) = 0;
        *((char *)&node[30] + 2) = 0;
        *((char *)&node[44] + 2) = 0;
        *((char *)&node[58] + 2) = 0;
        *((char *)&node[72] + 2) = 0;
    }
    for (iter = &g_10077175.padding_0[0]; iter < &g_10080b05.padding_0[0]; iter = &iter[1].padding_0[72])
    {
        memset(&iter[1].padding_0[60], 0, 12);
    }
    sub_1002ae81(&g_100544a4, 0x100);
    sub_1002ae81(&g_1005e6a0, 2688);
    k = &g_1005e5a0;
    for (iter1 = &g_1005e6a0; k < &g_1005e6a0; k += 16)
    {
        if ((short)k[6])
        {
            *((short *)&iter1[36]) = *((short *)k);
            *((short *)&iter1[40]) = (short)k[2];
            *((char *)&iter1[44]) = (char)k[5];
            *((unsigned int *)&iter1[144]) = 1;
            *((unsigned int *)&iter1[0x88]) = 100;
            *((unsigned int *)iter1) = 1073741825;
            *((unsigned int *)&iter1[4]) = 1702258002;
            *((unsigned int *)&iter1[8]) = 27745;
            iter1 += 168;
        }
    }
    if (g_101dfe9d)
        sub_10013f16();
    while (true)
    {
        v35 = 0x63fef8;
        v26 = v28;
        v23 = v22;
        while (true)
        {
            v24 = v23;
            v27 = v26;
            if (v35 > &g_1005f120)
                break;
            g_1005dba8 = &v36;
            g_1005dba4 = &<0x10012edb[is_15]|Stack bp-0x118, 1 B>;
            g_1005db9c = 401;
            g_1005dba0 = &g_10013542;
            v43 = v35;
            if ((int)v43[144] && (int)v43[44] == *((int *)&g_1005f85c) && !((g_1005dba8 = (unsigned int)&v36, g_1005dba4 = (unsigned int)&<0x10012edb[is_15]|Stack bp-0x118, 1 B>, g_1005db9c = 492, g_1005dba0 = (unsigned int)&g_10013542, g_101dfe9c && !sub_10011678((int)v35[36], (int)v35[40], 0))))
            {
                g_1005dba8 = &v36;
                g_1005dba4 = &<0x10012edb[is_15]|Stack bp-0x118, 1 B>;
                g_1005db9c = 493;
                g_1005dba0 = &g_10013542;
                if (g_101dfe9d)
                {
                    v44 = v35;
                    iter = (int)v44[40] - *((int *)&g_1005f858) + 6;
                    v45 = sub_1000d2da((int)v44[36] - *((int *)&g_1005f854) + 8, iter, 0);
                    if (!v45)
                        goto LABEL_1001351e;
                    v31 = v45;
                }
                g_1005dba8 = &v36;
                g_1005dba4 = &<0x10012edb[is_15]|Stack bp-0x118, 1 B>;
                g_1005db9c = 403;
                g_1005dba0 = &g_10013542;
                if (v21)
                {
                    g_1005dba8 = &v36;
                    g_1005dba4 = &<0x10012edb[is_15]|Stack bp-0x118, 1 B>;
                    g_1005db9c = 404;
                    sub_10012827(v35, 1, 0);
                }
                else
                {
                    g_1005dba8 = &v36;
                    g_1005dba4 = &<0x10012edb[is_15]|Stack bp-0x118, 1 B>;
                    g_1005db9c = 491;
                    g_1005dba0 = &g_10013542;
                    v14 = iter;
                    iter2 = 0;
                    v33 = sub_10012827(v35, 0, 0);
                    if (v33)
                    {
                        g_1005dba8 = &v36;
                        g_1005dba4 = &<0x10012edb[is_15]|Stack bp-0x118, 1 B>;
                        g_1005db9c = 494;
                        g_1005dba0 = &g_10013542;
                        v32 = sub_10012d79(v35, v33);
                        if (v32)
                        {
                            g_1005dba8 = &v36;
                            g_1005dba4 = &<0x10012edb[is_15]|Stack bp-0x118, 1 B>;
                            g_1005db9c = 410;
                            g_1005dba0 = &g_10013542;
                            if (g_101dfe9f && sub_10012e3d(v35))
                            {
                                if (v35 == g_100f0dc0 && ((int)v32[20] & 0xffffffc0))
                                {
                                    g_100432af = 0;
                                    g_63fe64 = 0;
                                    g_63fe60 = 0;
                                    sub_1002ade7("\t", 7);
                                    g_100f0dc0 = 0;
                                }
                            }
                            else
                            {
                                if ((v35 >= &g_1005e6a0 || (v46 = (char [140])sub_10023861(), !v46[138] && !v46[139])) && ((int)v32[16] >= 3 || sub_1003c23e(v35)))
                                {
                                    if ((char)v33[35])
                                        v20 += 1;
                                    g_1005dba8 = &v36;
                                    g_1005dba4 = &v9;
                                    g_1005db9c = 405;
                                    g_1005dba0 = &g_10013542;
                                    v47 = v35;
                                    if ((int)v47[0x88])
                                    {
                                        g_1005dba8 = &v36;
                                        g_1005dba4 = &v9;
                                        g_1005db9c = 406;
                                        g_1005dba0 = &g_10013542;
                                        if (*((int *)&g_1008b89f) && *((int *)v35) == *((int *)&g_1008b89f))
                                            iter2 += 50000;
                                        if (g_101dfe78 && g_100f0db0)
                                            iter2 += g_101dfe78 * (g_100f0db0 - (char *)v14) * 10 / g_100f0db0;
                                        g_1005dba8 = &v36;
                                        g_1005dba4 = &v9;
                                        g_1005db9c = 407;
                                        g_1005dba0 = &g_10013542;
                                        if (g_101dfe7c)
                                            iter2 += (unsigned int)(g_101dfe7c * (100 - (int)v35[0x88]) / 10);
                                        g_1005dba8 = &v36;
                                        g_1005dba4 = &v9;
                                        g_1005db9c = 408;
                                        g_1005dba0 = &g_10013542;
                                        if (g_101dfe80)
                                        {
                                            idx = v35;
                                            v49 = *((int *)&g_1005f854) - (int)idx[36];
                                            v50 = (v49 ^ v49 >> 31) - (v49 >> 31);
                                            v51 = *((int *)&g_1005f858) - (int)idx[40];
                                            v52 = (v51 ^ v51 >> 31) - (v51 >> 31);
                                            if (v52 != 1 || v50 != 1)
                                                v50 += v52;
                                            v53 = g_101dfe80 * (0x11 - v50);
                                            iter2 += (unsigned int)((v53 * 30 >> 32 CONCAT v53 * 30) / 48);
                                        }
                                        g_1005dba8 = &v36;
                                        g_1005dba4 = &v9;
                                        g_1005db9c = 409;
                                        g_1005dba0 = &g_10013542;
                                        if (g_101dfe84)
                                            iter2 += g_101dfe84 * *((int *)v32);
                                        g_1005dba8 = &v36;
                                        g_1005dba4 = &v9;
                                        g_1005db9c = 411;
                                        g_1005dba0 = &g_10013542;
                                        if (g_101dfe88)
                                        {
                                            v8 = g_101dfe88 * 20;
                                            iter2 += sub_10040a30(g_101dfe88 * 20);
                                        }
                                        g_1005dba8 = &v36;
                                        g_1005dba4 = &v8;
                                        g_1005db9c = 412;
                                        g_1005dba0 = &g_10013542;
                                        if (g_101dfe8c && g_100f0dc0 == v35)
                                            iter2 += g_101dfe8c * 60;
                                        if (iter2 >= v30)
                                        {
                                            v7 = iter2;
                                            v30 = iter2;
                                            v7 = v35;
                                            v29 = v35;
                                            v7 = v32;
                                            v27 = v32;
                                            v7 = v33;
                                            v25 = v33;
                                            v7 = v31;
                                            v24 = v31;
                                        }
                                    }
                                    else if ((char)v33[32])
                                    {
                                        iter = (int)v47[36] - *((int *)&g_1005f854) + 1;
                                        if (iter <= 0x2 && (int)v47[40] - *((int *)&g_1005f858) + 1 <= 0x2)
                                        {
                                            g_100f0e20 = v47;
                                            return v33;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
LABEL_1001351e:
            v35 += 168;
            v26 = v27;
            v23 = v24;
            if (v35 == 0x64a308)
            {
                v35 = &g_1005e6a0;
                v26 = v27;
                v23 = v24;
            }
        }
        if (!v21)
            break;
        v21 = 0;
        sub_10012aae();
    }
    g_1005dba8 = &v36;
    g_1005dba4 = &<0x10012edb[is_15]|Stack bp-0x118, 1 B>;
    g_1005db9c = 477;
    g_1005dba0 = &g_100135a4;
    if (v20 && g_10052678)
    {
        v6 = g_10052678;
        g_10052678->field_0->field_30(g_10052678, 0, 0, 0);
        sub_10009452();
    }
    g_1005dba8 = &v36;
    g_1005dba4 = &v6;
    g_1005db9c = 413;
    g_1005dba0 = &g_10013e4b;
    idx1 = v29;
    if (!v29)
    {
        iter = *((int *)0x64ccf8);
LABEL_10013744:
        if (iter && g_1004335d)
        {
            g_1004335d = *((unsigned short *)&iter);
            idx1 = (g_10043362 - 64) * 492 + 6606096;
            if ((int)idx1[48] && *((int *)idx1) && (int)idx1[56] < (int)idx1[48])
            {
                g_10043364 = (int)idx1[48] - 1;
                g_1004335f = 0;
                return sub_1002ade7(&g_10043355, 0x11);
            }
        }
        if (!v29)
            return idx1;
    }
    else
    {
        g_1005dba8 = &v36;
        g_1005dba4 = &v6;
        g_1005db9c = 414;
        g_1005dba0 = &g_100137a3;
        if (idx1 != g_100f0dc0)
        {
            g_100f0dd8 = 0;
            g_100f0ddc = 0;
            g_100f0e24 = 0;
            g_100f0e28 = 0;
        }
        g_63fedc = 0;
        g_100f0dc0 = idx1;
        g_100f0e20 = idx1;
        v55 = (char)v27[25];
        if (v55)
        {
            if (v55 < 4)
            {
                v56 = 0;
            }
            else
            {
                v56 = 1;
                v55 -= 3;
            }
            if (g_799cec != v55 || g_799ce8 != v56)
            {
                v15 = 4;
                v16 = 160;
                v17 = v55;
                v18 = v56;
                g_799cec = v55;
                g_799ce8 = v56;
                v19 = *((int *)0x799ce4);
                v5 = &v15;
                sub_1002ade7(&v15, 6);
            }
        }
        idx1 = (char)v27[24];
        v57 = *((int *)(0x8 * idx1 + (char *)&g_10008a1a[0]));
        g_1005dba8 = &v36;
        g_1005dba4 = &v5;
        g_1005db9c = 415;
        g_1005dba0 = &g_100137a3;
        if (v57 != 0xffffffff && (iter = (struct_0 *)*((int *)0x64ccf8), *((int *)6606072) != v57))
        {
            if (!v57)
                goto LABEL_10013744;
            v58 = *((int *)(0x8 * idx1 + (char *)&g_10008a16[0]));
            g_10043351 = 9;
            g_1004334c = *((unsigned short *)&v58);
            g_1004335d = *((unsigned short *)&v58);
            v59 = sub_1002ae92(v58, 0, 0);
            if (v59)
            {
                g_1004334b = v60;
                g_1004334e = v60;
                g_10043349 = v59;
                g_10043362 = g_10043349;
                v62 = v61;
                if (!v61)
                    v62 += 1;
                g_10043354 = v62;
                return sub_1002ade7(&g_10043344, 0x11);
            }
        }
    }
    g_1005dba8 = &v36;
    g_1005dba4 = &v58;
    g_1005db9c = 416;
    g_1005dba0 = &g_1001393c;
    idx2 = v27;
    v64 = (int)idx2[20];
    if ((int)idx2[20] && !g_100f9327)
    {
        if ((int)idx2[16] >= 3)
        {
            v4 = v29;
            if (sub_1003c23e(v4))
            {
                idx2 = v27;
                v64 = (int)idx2[20];
                v4 = v29;
                goto LABEL_100137fb;
            }
        }
        else
        {
LABEL_100137fb:
            if (!g_100f0dd8)
            {
                v3 = v64;
                v2 = idx2;
                v65 = v64 & 0xffffffc0;
                if (v65)
                {
                    sub_1003a60a(v29, v65);
                    v0 = g_101dfe94;
                    g_100f0dd8 = g_101dfe94;
                    v1 = v29;
                }
                idx2 = v1;
                v64 = v65;
            }
            if (!g_100f0ddc && (v4 = v4, (int)idx2[16] != 1 && (v4 = v4, (int)idx2[16] != 9 && (v65 = (struct_0 *)(v64 & 63), v4 = v4, v65))))
            {
                if (v65 >= 0x6 && v65 <= 0xd)
                {
                    iter = v65;
                    v66 = v29;
                    v67 = *((int *)&g_1005f854) - (int)v66[36];
                    v68 = (v67 ^ v67 >> 31) - (v67 >> 31);
                    v69 = *((int *)&g_1005f858) - (int)v66[40];
                    v70 = (v69 ^ v69 >> 31) - (v69 >> 31);
                    if (v70 < v68)
                        v70 = v68;
                    if (v70 > 3 && (iter != 0xb || v70 > 5) && (iter != 0xc || v70 > 4))
                    {
                        v4 = v4;
                    }
                    else
                    {
                        v65 = iter;
                        goto LABEL_100138a1;
                    }
                }
                else
                {
LABEL_100138a1:
                    if (v65 >= 0xf && v65 <= 0x12 || v65 == 0x20)
                    {
                        v71 = v27;
                        v11 = (short)v71[27];
                        v12 = (short)v71[29];
                        v13 = (char)v71[31];
                        sub_1003a60a(&v10, v65);
                    }
                    else if (v65 >= 0x1a && v65 <= 0x1f)
                    {
                        v72 = (char)v27[31];
                        iter = g_1005f7ed;
                        if (g_1005f7ed->field_50 + 1 != v72)
                        {
                            v15 = 1;
                            v16 = (char)v72 + 110;
                            sub_1002ade7(&v15, 3, v65);
                            return &v15;
                        }
                        sub_1003a60a(v29, v65);
                    }
                    else
                    {
                        sub_1003a60a(v29, v65);
                    }
                    v0 = g_101dfe94;
                    g_100f0ddc = g_101dfe94;
                }
            }
        }
    }
    g_1005dba8 = &v36;
    g_1005dba4 = &v4;
    g_1005db9c = 417;
    g_1005dba0 = &g_10013e4b;
    if (!(int)v27[16])
        return v27;
    if (g_100f0dc4 > 0 && g_10052768 == g_1028987c && g_1005276c == *((int *)&g_10289880) && g_10052770 == *((int *)&g_10289884))
    {
        g_100f0dc4 = g_100f0dc4 - 1;
        return g_10052768;
    }
    g_1028987c = 0;
    g_1005dba8 = &v36;
    g_1005dba4 = &v4;
    g_1005db9c = 418;
    g_1005dba0 = &g_10013e4b;
    sub_10013f16();
    g_1005dba8 = &v36;
    g_1005dba4 = &v4;
    g_1005db9c = 419;
    g_1005dba0 = &g_10013e4b;
    v73 = v27;
    g_10052780 = 4294967295;
    if (((int)v73[16] == 0xe || (int)v73[16] == 0x10) && g_10052778 && !g_100f0e28 && g_10052778->field_8 == *((int *)&g_1005f85c))
    {
        if (&g_10052778->field_0->padding_0[-1 * *((int *)&g_1005f854)] + 0x2 <= 4 && g_10052778->field_4 - *((int *)&g_1005f858) + 0x2 <= 4)
        {
            g_100f0e28 = 1;
        }
        else if (g_10052778->field_0 != *((int *)&g_1005f854) || g_10052778->field_4 != *((int *)&g_1005f858) || g_10052778->field_8 != *((int *)&g_1005f85c))
        {
            g_63fedc = 0;
            g_63fed8 = 0;
            g_63fed4 = 0;
            g_1005277c = 2;
            v65 = g_10052778->field_0;
            sub_100147eb(g_10052778->field_0, g_10052778->field_4, g_10052778->field_8);
            g_1005277c = 0;
        }
    }
    sub_10010af0();
    g_1005dba8 = &v36;
    g_1005dba4 = &v65;
    g_1005db9c = 420;
    g_1005dba0 = &g_10013e4b;
    g_10052784 = g_101dfe9e;
    if ((int)v27[16] != g_100f0e2c)
    {
        g_100f0e2c = (int)v27[16];
        g_100f0e24 = 0;
    }
    if (g_100f0e2c == 1)
    {
        g_1005dba8 = &v36;
        g_1005dba4 = &v65;
        g_1005db9c = 421;
        g_1005dba0 = &g_10013e4b;
        return sub_10014f10(v29);
    }
    else if (g_100f0e2c == 0x2)
    {
        g_1005dba8 = &v36;
        g_1005dba4 = &v65;
        g_1005db9c = 422;
        g_1005dba0 = &g_10013e4b;
        return sub_1001242d(v29, iter, 0);
    }
    else if (g_100f0e2c == 5)
    {
        g_1005dba8 = &v36;
        g_1005dba4 = &v65;
        g_1005db9c = 425;
        g_1005dba0 = &g_10013e4b;
        return sub_1001242d(v29, v24, 1);
    }
    else if (g_100f0e2c == 3)
    {
        g_1005dba8 = &v36;
        g_1005dba4 = &v65;
        g_1005db9c = 423;
        g_1005dba0 = &g_10013e4b;
        return sub_10014e64(v29);
    }
    else if (g_100f0e2c == 4)
    {
        g_1005dba8 = &v36;
        g_1005dba4 = &v65;
        g_1005db9c = 424;
        g_1005dba0 = &g_10013e4b;
        return sub_10013e4d(v29);
    }
    else if (g_100f0e2c == 0x6)
    {
        g_1005dba8 = &v36;
        g_1005dba4 = &v65;
        g_1005db9c = 426;
        g_1005dba0 = &g_10013e4b;
        return sub_10014a0d(v29);
    }
    else if (g_100f0e2c == 0x7)
    {
        g_1005dba8 = &v36;
        g_1005dba4 = &v65;
        g_1005db9c = 427;
        g_1005dba0 = &g_10013e4b;
        return sub_100148ba(v29);
    }
    else if (g_100f0e2c == 0x8)
    {
        g_1005dba8 = &v36;
        g_1005dba4 = &v65;
        g_1005db9c = 428;
        g_1005dba0 = &g_10013e4b;
        return sub_10014993(v29);
    }
    else if (g_100f0e2c == 9)
    {
        g_1005dba8 = &v36;
        g_1005dba4 = &v65;
        g_1005db9c = 428;
        g_1005dba0 = &g_10013e4b;
        return sub_10014927(v29);
    }
    else if (g_100f0e2c == 0xa)
    {
        g_1005dba8 = &v36;
        g_1005dba4 = &v65;
        g_1005db9c = 429;
        g_1005dba0 = &g_10013e4b;
        return sub_10014afb(v29);
    }
    else if (g_100f0e2c == 0xb)
    {
        g_1005dba8 = &v36;
        g_1005dba4 = &v65;
        g_1005db9c = 430;
        g_1005dba0 = &g_10013e4b;
        return sub_10014aed(v29);
    }
    else if (g_100f0e2c == 0xc)
    {
        g_1005dba8 = &v36;
        g_1005dba4 = &v65;
        g_1005db9c = 431;
        g_1005dba0 = &g_10013e4b;
        return sub_10014a6e(v29);
    }
    else if (g_100f0e2c == 0xd)
    {
        g_1005dba8 = &v36;
        g_1005dba4 = &v65;
        g_1005db9c = 432;
        g_1005dba0 = &g_10013e4b;
        return sub_10014d75(v29);
    }
    else if (g_100f0e2c == 0xe)
    {
        g_1005dba8 = &v36;
        g_1005dba4 = &v65;
        g_1005db9c = 433;
        g_1005dba0 = &g_10013e4b;
        return sub_10014c69(v29);
    }
    else if (g_100f0e2c == 0xf)
    {
        g_1005dba8 = &v36;
        g_1005dba4 = &v65;
        g_1005db9c = 432;
        g_1005dba0 = &g_10013e4b;
        return sub_10014bef(v29);
    }
    else
    {
        if (g_100f0e2c != 0x10)
            return g_100f0e2c;
        g_1005dba8 = &v36;
        g_1005dba4 = &v65;
        g_1005db9c = 433;
        sub_10014b75(v29);
        return g_100f0e2c;
    }
}
```

## `sub_1001330d` `0x1001330d`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1001330d(void)
{
}
```

## `sub_10013314` `0x10013314`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10013314(void)
{
}
```

## `sub_100135d7` `0x100135d7`

_5 bytes. (leaf/helper — see body)_

```c
void sub_100135d7(void)
{
}
```

## `sub_10013742` `0x10013742`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10013742(void)
{
}
```

## `sub_1001391a` `0x1001391a`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1001391a(void)
{
}
```

## `sub_10013e4d` `0x10013e4d`

_201 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern char g_101dfe9d;

int sub_10013e4d(void)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned int v0[11];  // [bp+0x4]

    if (g_1005f854 - v0[9] + 1 <= 2 && g_1005f858 - v0[10] + 1 <= 2)
        return;
    if (!g_101dfe9d)
        v1 = sub_1000d2da(v0[9] - g_1005f854 + 8, v0[10] - g_1005f858 + 6, 0);
    v2 = v1;
    if (!v1)
        return;
    sub_10014825();
    return;
}
```

## `sub_10013f16` `0x10013f16`

_1181 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    struct struct_1 *field_4;
    char padding_8[128];
    unsigned int field_88;
} struct_0;

typedef struct struct_2 {
    struct struct_2 *field_0;
} struct_2;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern int g_10052770;
extern unsigned int g_10052785[4];
extern unsigned int g_10052f65;
extern unsigned int g_10052f69;
extern unsigned int g_10052f6d;
extern unsigned int g_10052f71;
extern unsigned int g_1005dc24;
extern unsigned int g_1005f7e5;
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;

struct_0 * sub_10013f16(void)
{
    struct_0 *v16;  // eax
    struct_0 *v17;  // eax
    struct_0 *v26;  // eax
    unsigned int v27;  // ecx
    unsigned int *v28;  // ecx
    unsigned int *v29;  // ecx
    unsigned int index;  // ecx
    struct_2 **v31;  // eax
    struct_2 **v32;  // eax
    struct_0 *v18;  // edi
    struct_0 *v33;  // eax
    unsigned int *v19;  // ecx
    unsigned int v20;  // eax
    unsigned int *v21;  // ecx
    unsigned int *v22;  // edi
    unsigned int *v23;  // esi
    unsigned int v24;  // ebx
    unsigned int v25;  // ecx
    int v0;  // [bp-0xc08]
    struct_0 *v1;  // [bp-0xbfc]
    unsigned int v2;  // [bp-0xbec]
    unsigned int idx;  // [bp-0xbe0]
    char v4;  // [bp-0xbdc]
    char v5;  // [bp-0x7f4]
    char v6;  // [bp-0x40c]
    unsigned int v7;  // [bp-0x24]
    unsigned int *v8;  // [bp-0x20]
    unsigned int *v9;  // [bp-0x1c]
    unsigned int *v10;  // [bp-0x18]
    int i;  // [bp-0x14]
    int k;  // [bp-0x10]
    unsigned int v13;  // [bp-0xc]
    unsigned int v14;  // [bp-0x8]

    g_1005dc24 = 0;
    v16 = sub_1002ae81(&g_10052785[0], 2032);
    g_1005dc24 = 1;
    v2 = g_1005f854;
    v14 = v2;
    v2 = g_1005f858;
    v13 = v2;
    v14 -= 8;
    v13 -= 6;
    idx = 0;
    for (i = 0; i < 14; i += 1)
    {
        for (k = 0; k < 18; k += 1)
        {
            g_1005dc24 = 2;
            v17 = sub_1003a148(k, i, g_10052770);
            g_1005dc24 = 3;
            v16 = v17;
            if (v16)
            {
                v18 = v16;
                v19 = &g_10052785[36 * i + 2 * k];
                g_1005dc24 = 4;
                if (!v18->field_0)
                {
                    g_1005dc24 = 5;
                    *(v19) = 4294967295;
                    goto LABEL_10014292;
                }
                g_1005dc24 = 6;
                v20 = sub_1003c4fa(v18->field_4, v19, v18);
                v21 = &v18->field_4->field_0;
                v22 = v19;
                g_1005dc24 = 7;
                v16 = v20 & 1;
                if (!v16)
                {
                    g_1005dc24 = 8;
                    *(v10) = 4294967295;
                    goto LABEL_10014292;
                }
                else
                {
                    g_1005dc24 = 9;
                    v23 = v22 + 1;
                    v24 = *(v22) * 12;
                    g_1005dc24 = 1;
                    v9 = v24 + (char *)v23;
                    v10 = v21;
                    g_1005dc24 = 11;
                    while (true)
                    {
                        if (v23 >= v9)
                            break;
                        g_1005dc24 = 12;
                        v8 = v23;
                        v25 = *(v23);
                        g_1005dc24 = 13;
                        if (v25 != 99)
                        {
                            g_1005dc24 = 14;
                            if (v25 >= 2118 && v25 <= 2127)
                            {
                                g_1005dc24 = 15;
                                if (v25 == 2118 || v25 == 2123 || v25 == 2122 || v25 == 2126)
                                {
                                    if (*(v10) < 50)
                                        *(v10) = 700;
                                }
                                else
                                {
                                    if (v25 == 2119 || v25 == 2124 || v25 == 2121 || v25 == 2127)
                                    {
                                        if (*(v10) < 35)
                                            *(v10) = 450;
                                    }
                                    else
                                    {
                                        if (*(v10) < 4294967294)
                                            *(v10) = 0;
                                    }
                                }
                            }
                            else
                            {
                                if (v25 >= 6754 && v25 <= 6756)
                                {
                                    g_1005dc24 = 16;
                                    if (*(v10) != 4294967294)
                                        *(v10) = 4294967295;
                                    goto LABEL_10014292;
                                }
                                else
                                {
                                    g_1005dc24 = 0x11;
                                    v16 = sub_1003c462(v25, v25);
                                    g_1005dc24 = 18;
                                    if (v16)
                                    {
                                        g_1005dc24 = 19;
                                        v28 = v10;
                                        if (*(v28) != 4294967294)
                                        {
                                            g_1005dc24 = 20;
                                            *(v28) = 4294967295;
                                        }
                                        goto LABEL_10014292;
                                    }
                                    else
                                    {
                                        g_1005dc24 = 21;
                                        v26 = sub_1003c3fc(v25);
                                        g_1005dc24 = 22;
                                        v16 = v26;
                                        if (v16)
                                        {
                                            g_1005dc24 = 23;
                                            v29 = v10;
                                            if (*(v29) != 4294967294)
                                            {
                                                g_1005dc24 = 24;
                                                *(v29) = 4294967295;
                                            }
                                            goto LABEL_10014292;
                                        }
                                    }
                                }
                            }
                        }
                        else if (k != 8 || i != 6)
                        {
                            g_1005dc24 = 25;
                            v27 = v23[1];
                            if (v27 != g_1005f7e5)
                            {
                                g_1005dc24 = 26;
                                v16 = sub_1003997e(v27);
                                g_1005dc24 = 27;
                                if (v16->field_88)
                                {
                                    g_1005dc24 = 28;
                                    *((struct_0 **)&(&v6)[4 * idx]) = v16;
                                    v0 = k;
                                    *((int *)&(&v5)[4 * idx]) = k;
                                    v0 = i;
                                    *((int *)&(&v4)[4 * idx]) = i;
                                    idx += 1;
                                    *(v10) = 4294967294;
                                }
                            }
                        }
                        g_1005dc24 = 29;
                        v23 = v8 + 3;
                    }
                    goto LABEL_10014292;
                }
            }
            g_1005dc24 = 30;
            if (!*(v10))
                *(v10) = 1;
LABEL_10014292:
            g_1005dc24 = 31;
        }
    }
    g_1005dc24 = 32;
    for (index = 0; index < idx; index = v14 + 1)
    {
        g_1005dc24 = 33;
        v14 = index;
        v7 = *((int *)&(&v6)[4 * index]);
        g_1005dc24 = 0x22;
        v16 = sub_10012827(v7, 0, 0);
        if (v16)
        {
            g_1005dc24 = 35;
            v1 = v16;
            v31 = sub_10012d79(v7, v16);
            g_1005dc24 = 36;
            v32 = v31;
            if (v32)
                v32 = *(v32);
            g_1005dc24 = 37;
            sub_1000e100(*((int *)&(&v5)[4 * v14]), *((int *)&(&v4)[4 * v14]), v32);
            g_1005dc24 = 38;
            v33 = sub_10012d79(v7, v16);
            g_1005dc24 = 39;
            v16 = v33;
            if (v16)
                v16 = sub_100115bc(*((int *)&(&v5)[4 * v14]), *((int *)&(&v4)[4 * v14]), v16->field_4, v16->field_0);
        }
        g_1005dc24 = 40;
    }
    g_1005dc24 = 41;
    g_10052f69 = g_10052f69 + 1;
    g_10052f65 = g_10052f65 + 1;
    g_10052f71 = g_10052f71 + 1;
    g_10052f6d = g_10052f6d + 1;
    return v16;
}
```

## `sub_10013fe3` `0x10013fe3`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10013fe3(void)
{
}
```

## `sub_10014150` `0x10014150`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10014150(void)
{
}
```

## `sub_100143ba` `0x100143ba`

_353 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_10052785[4];
extern unsigned int g_10052f65;
extern unsigned int g_10052f69;
extern unsigned int g_10052f6d;
extern unsigned int g_10052f71;

void sub_100143ba(int a0, int a1)
{
    unsigned int v9;  // ebx
    unsigned int v10;  // ebx
    int v18;  // esi
    int v19;  // edi
    unsigned int v21;  // eax
    int v22;  // edi
    unsigned int v23;  // esi
    unsigned int v24;  // edi
    unsigned int v11;  // ecx
    unsigned int v12;  // eax
    unsigned int v13;  // ebx
    unsigned int *v14;  // eax
    int v15;  // esi
    int v16;  // edi
    int v17;  // esi
    int v0;  // [bp-0x28]
    int v1;  // [bp-0x24], Other Possible Types: unsigned int
    unsigned int v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x1c]
    unsigned int v4;  // [bp-0x18]
    unsigned int i;  // [bp-0x14]
    unsigned int iter;  // [bp-0x10]
    int v7;  // [bp-0xc]
    int v8;  // [bp-0x8]

    v8 = a0 - 2;
    v7 = a1 - 2;
    for (i = 0; i <= 4; i += 1)
    {
        iter = 0;
        while (iter <= 4)
        {
            v9 = iter;
            v10 = v9;
            if (!i || (v10 = v9, v10 = v10, !v9 || (v10 = v10, i == 4 || (v10 = v10, v10 == 4))))
            {
                v11 = 128;
            }
            else if (i == 2 && v10 == 2)
            {
                v11 = 4294967294;
            }
            else
            {
                v11 = 160;
            }
            v12 = i + v7;
            v13 = v10 + v8;
            if (v12 < 0 || v13 < 0 || v12 >= 14 || v13 >= 18)
            {
                iter += 1;
            }
            else
            {
                v14 = &g_10052785[36 * v12 + 2 * v13];
                if (*(v14) < 4294967294)
                {
                    *(v14) = *(v14) + v11;
                    iter += 1;
                }
                else
                {
                    iter += 1;
                }
            }
        }
    }
    v15 = a0 - 8;
    v16 = a1 - 6;
    v17 = v15;
    if (!v16)
    {
        v17 = v15;
        if (!v17)
            return;
    }
    v18 = v17;
    if (v18 >= 2147483647)
        v18 = ~(v18) + 1;
    v19 = v16;
    if (v19 >= 2147483647)
        v19 = ~(v16) + 1;
    v0 = v19;
    v21 = v18 * v18 + v19 * v19;
    v22 = v0;
    v1 = v18;
    if (/* unsupported instruction */)
    {
        /* unsupported instruction */
        /* unsupported instruction */
    }
    else
    {
        /* unsupported instruction */
        /* unsupported instruction */
    }
    v1 = v21;
    if (/* unsupported instruction */)
    {
        /* unsupported instruction */
        /* unsupported instruction */
    }
    else
    {
        /* unsupported instruction */
        /* unsupported instruction */
    }
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    v1 = 1000;
    /* unsupported instruction */
    /* unsupported instruction */
    v3 = (/* unsupported instruction */ ? /* unsupported instruction */ : nan);
    /* unsupported instruction */
    v1 = v22;
    /* unsupported instruction */
    /* unsupported instruction */
    v1 = v21;
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    v1 = 1000;
    /* unsupported instruction */
    /* unsupported instruction */
    v2 = (/* unsupported instruction */ ? /* unsupported instruction */ : nan);
    /* unsupported instruction */
    v4 = 15 - v18 - v22;
    v23 = v4 * v3;
    v24 = v4 * v2;
    if (v15 >= 0)
        g_10052f69 = g_10052f69 + v23;
    else
        g_10052f71 = g_10052f71 + v23;
    if (v16 < 0)
    {
        g_10052f65 = g_10052f65 + v24;
        return;
    }
    g_10052f6d = g_10052f6d + v24;
    return;
}
```

## `sub_1001451b` `0x1001451b`

_720 bytes. (leaf/helper — see body)_

```c
extern char g_100527e7;
extern char g_100527f8;
extern char g_100527f9;
extern char g_100527fa;
extern char g_1005280b;
extern unsigned int g_10052f65;
extern unsigned int g_10052f69;
extern unsigned int g_10052f6d;
extern unsigned int g_10052f71;
extern int g_1005f854;
extern unsigned int g_1005f858;
extern int g_1005f85c;
extern unsigned int g_100f0dc4;

void sub_1001451b(unsigned int *idx)
{
    int v8;  // ebx
    unsigned int v9;  // ecx
    char v10;  // cl
    unsigned int v11;  // edx
    unsigned int v12;  // ecx
    int v13;  // ebx
    unsigned int v14;  // edx
    char v0;  // [bp-0xc]
    char v1;  // [bp-0xb]
    char v2;  // [bp-0xa]
    char v3;  // [bp-0x9]
    char v4;  // [bp-0x8]
    char v5;  // [bp-0x7]
    char v6;  // [bp-0x6]
    char v7;  // [bp-0x5]

    v3 = 1;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    v6 = g_100527fa;
    g_10052f69 = g_10052f69 * g_100527fa;
    v7 = g_100527e7;
    g_10052f65 = g_10052f65 * g_100527e7;
    v4 = g_100527f8;
    g_10052f71 = g_10052f71 * g_100527f8;
    v5 = g_1005280b;
    g_10052f6d = g_10052f6d * g_1005280b;
    v8 = idx[9] - g_1005f854;
    v9 = idx[10] - g_1005f858;
    if (v8 > 4 && v8 < 20)
    {
        g_10052f71 = 4294967295;
        v4 = 254;
        v3 = 0;
        v1 = 1;
        if (g_100527fa >= 240)
            v0 = 1;
    }
    else if (v8 > 4294967276 && v8 < -0x4)
    {
        g_10052f69 = 4294967295;
        v6 = 254;
        v3 = 0;
        v1 = 1;
        if (g_100527f8 >= 240)
            v0 = 1;
    }
    if (v9 > 3 && v9 < 20)
    {
        g_10052f65 = 4294967295;
        v7 = 254;
        v3 = 0;
        v0 = 1;
        if (g_1005280b >= 240)
            v1 = 1;
    }
    else if (v9 > 4294967276 && v9 < 4294967293)
    {
        g_10052f6d = 4294967295;
        v5 = 254;
        v3 = 0;
        v0 = 1;
        if (g_100527e7 >= 240)
            v1 = 1;
    }
    if (v3)
    {
        v10 = g_100527f9;
        if (v6 < g_100527f9)
        {
            v10 = v6;
            v11 = g_1005f858;
            v8 = g_1005f854 + 1;
            v2 = 1;
        }
        if (v7 < v10)
        {
            v10 = v7;
            v8 = g_1005f854;
            v11 = g_1005f858 - 1;
            v2 = 1;
        }
        if (v4 < v10)
        {
            v10 = v4;
            v11 = g_1005f858;
            v8 = g_1005f854 - 1;
            v2 = 1;
        }
        if (v5 < v10)
        {
            v8 = g_1005f854;
            v11 = g_1005f858 + 1;
            v2 = 1;
        }
        if (!v2)
            return;
        sub_10015204(v8, v11, g_1005f85c);
        g_100f0dc4 = 10;
        return;
    }
    else
    {
        v12 = 4294967295;
        if (v1 && v6 < 254 && g_10052f69 < 4294967295)
            v12 = g_10052f69;
        if (v0 && v7 < 254 && g_10052f65 < v12)
            v12 = g_10052f65;
        if (v1 && v4 < 254 && g_10052f71 < v12)
            v12 = g_10052f71;
        if (v0 && v5 < 254 && g_10052f6d < v12)
            v12 = g_10052f6d;
        v13 = g_1005f854;
        v14 = g_1005f858;
        if (v1 && v6 < 254 && v12 == g_10052f69)
        {
            v13 = g_1005f854 + 1;
            v2 = 1;
        }
        else if (v0 && v7 < 254 && v12 == g_10052f65)
        {
            v14 = g_1005f858 - 1;
            v2 = 1;
        }
        else if (v1 && v4 < 254 && v12 == g_10052f71)
        {
            v13 = g_1005f854 - 1;
            v2 = 1;
        }
        else if (v0 && v5 < 254 && v12 == g_10052f6d)
        {
            v14 = g_1005f858 + 1;
            v2 = 1;
        }
        if (!v2)
            return;
        sub_10015204(v13, v14, g_1005f85c);
        g_100f0dc4 = 10;
        return;
    }
}
```

## `sub_100147eb` `0x100147eb`

_58 bytes. (leaf/helper — see body)_

```c
unsigned int sub_100147eb(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v5;  // eax
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v4 = 0;
    v3 = 0;
    v2 = a2;
    v1 = a1;
    v0 = a0;
    v5 = 4604016();
    if (v5 == 1)
    {
        return 4288032();
    }
    else if (v5 == 2)
    {
        return 4288784();
    }
    else
    {
        return v5;
    }
}
```

## `sub_10014825` `0x10014825`

_149 bytes. (leaf/helper — see body)_

```c
extern int g_1005f854;
extern int g_1005f858;
extern void g_1005f85c;
extern unsigned int g_100f0dc4;
extern unsigned int g_1028987c;

unsigned int sub_10014825(unsigned int a0)
{
    int v1;  // ebx
    int v2;  // edx
    unsigned int v3;  // eax
    unsigned int v4;  // ebx
    unsigned int v5;  // edx
    unsigned int v6;  // eax
    unsigned int v7;  // eax

    v1 = g_1005f854;
    v2 = g_1005f858;
    if (a0 == 1)
    {
        v2 = g_1005f858 - 1;
    }
    else if (a0 == 2)
    {
        v1 = g_1005f854 + 1;
    }
    else if (a0 == 3)
    {
        v2 = g_1005f858 + 1;
    }
    else if (a0 == 4)
    {
        v1 = g_1005f854 - 1;
    }
    else
    {
        if (a0 == 5)
        {
            v4 = g_1005f854 + 1;
            v5 = g_1005f858 - 1;
        }
        else if (a0 == 6)
        {
            v4 = g_1005f854 + 1;
            v5 = g_1005f858 + 1;
        }
        else if (a0 == 7)
        {
            v4 = g_1005f854 - 1;
            v5 = g_1005f858 + 1;
        }
        else if (a0 == 8)
        {
            v4 = g_1005f854 - 1;
            v5 = g_1005f858 - 1;
        }
        else
        {
            return v7;
        }
        g_1028987c = 0;
        v6 = sub_100147eb(v4, v5, *((int *)&g_1005f85c));
        g_100f0dc4 = 10;
        return v6;
    }
    g_1028987c = 0;
    v3 = sub_10015204(v1, v2, *((int *)&g_1005f85c));
    g_100f0dc4 = 10;
    return v3;
}
```

## `sub_100148ba` `0x100148ba`

_109 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern unsigned int g_100f0dcc;

unsigned int sub_100148ba(unsigned int *idx)
{
    unsigned int v5;  // eax
    unsigned int v6;  // ebx
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    if (g_100f0dcc)
        return v5;
    v0 = v6;
    v2 = idx[9] - g_1005f854;
    v4 = (v2 ^ v2 >> 31) - (v2 >> 31);
    v1 = idx[10] - g_1005f858;
    v3 = (v1 ^ v1 >> 31) - (v1 >> 31);
    if (v4 > 1)
    {
        return (v1 ^ v1 >> 31) - (v1 >> 31);
    }
    else if (v3 <= 1)
    {
        v2 += 8;
        v1 += 6;
        sub_1000ffb0(v2, v1, 1);
        return sub_10014825(v6);
    }
    else
    {
        return (v1 ^ v1 >> 31) - (v1 >> 31);
    }
}
```

## `sub_10014927` `0x10014927`

_108 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern unsigned int g_100f0dcc;

int sub_10014927(void)
{
    unsigned int v7;  // ebx
    unsigned int v8;  // eax
    unsigned int idx[11];  // edi
    unsigned int v0;  // [bp-0x1c]
    int v1;  // [bp-0x18]
    int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    unsigned int v6[11];  // [bp+0x4]

    if (g_100f0dcc)
        return;
    v5 = v7;
    v0 = v8;
    idx = v6;
    v2 = idx[9] - g_1005f854;
    v4 = (v2 ^ v2 >> 31) - (v2 >> 31);
    v1 = idx[10] - g_1005f858;
    v3 = (v1 ^ v1 >> 31) - (v1 >> 31);
    if (v4 <= 1 && v3 <= 1)
    {
        sub_10014f10(v6);
        return;
    }
    sub_10013e4d(v6);
    return;
}
```

## `sub_10014993` `0x10014993`

_122 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern unsigned int g_100f0dcc;

int sub_10014993(void)
{
    unsigned int v6;  // eax
    unsigned int idx[11];  // edi
    unsigned int v8;  // ebx
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    unsigned int v5[11];  // [bp+0x4]

    if (g_100f0dcc)
        return;
    v0 = v6;
    idx = v5;
    v2 = idx[9] - g_1005f854;
    v4 = (v2 ^ v2 >> 31) - (v2 >> 31);
    v1 = idx[10] - g_1005f858;
    v3 = (v1 ^ v1 >> 31) - (v1 >> 31);
    if (v4 <= 1 && v3 <= 1)
    {
        v2 += 8;
        v1 += 6;
        sub_1000ffb0(v2, v1, 1);
        sub_10014825(v8);
        return;
    }
    sub_10013e4d(v5);
    return;
}
```

## `sub_10014a0d` `0x10014a0d`

_97 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern unsigned int g_100f0dcc;

unsigned int sub_10014a0d(unsigned int *idx)
{
    unsigned int v5;  // eax
    unsigned int v6;  // ebx
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    if (!g_100f0dcc)
    {
        v0 = v6;
        v2 = idx[9] - g_1005f854;
        v4 = (v2 ^ v2 >> 31) - (v2 >> 31);
        v1 = idx[10] - g_1005f858;
        v3 = (v1 ^ v1 >> 31) - (v1 >> 31);
        v2 += 8;
        v1 += 6;
        sub_1000ffb0(v2, v1, 1);
        return sub_10014825(v6);
    }
    return v5;
}
```

## `sub_10014a6e` `0x10014a6e`

_127 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
} struct_0;

extern struct_0 *g_10052778;
extern unsigned int g_1005277c;
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern unsigned int g_100f0dcc;
extern unsigned int g_101dfe90;

unsigned int [3] sub_10014a6e(unsigned int *idx)
{
    unsigned int v4[3];  // eax
    unsigned int v5;  // esi
    unsigned int v6[3];  // eax
    int v0;  // [bp-0x14]
    int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    if (g_100f0dcc)
        return v4;
    v1 = idx[9] - g_1005f854;
    v3 = (v1 ^ v1 >> 31) - (v1 >> 31);
    v0 = idx[10] - g_1005f858;
    v2 = (v0 ^ v0 >> 31) - (v0 >> 31);
    v5 = g_101dfe90 + 2;
    if (v3 > v5)
    {
        return (v0 ^ v0 >> 31) - (v0 >> 31);
    }
    else if (v2 > v5)
    {
        return (v0 ^ v0 >> 31) - (v0 >> 31);
    }
    else if (g_10052778)
    {
        g_1005277c = 1;
        v6 = sub_100147eb(g_10052778->field_0, g_10052778->field_4, g_10052778->field_8);
        g_1005277c = 0;
        return v6;
    }
    else
    {
        return g_10052778;
    }
}
```

## `sub_10014aed` `0x10014aed`

_14 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10014aed(void)
{
    unsigned int v1;  // ebx

    return sub_10014825(v1);
}
```

## `sub_10014afb` `0x10014afb`

_120 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern unsigned int g_100f0dcc;
extern unsigned int g_100f0e24;
extern unsigned int g_101dfe90;

int sub_10014afb(unsigned int *idx)
{
    unsigned int v5;  // eax
    unsigned int v6;  // ebx
    unsigned int v7;  // esi
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    if (g_100f0dcc)
        return v5;
    if (g_100f0e24)
        return sub_10014e64(idx);
    v0 = v6;
    v2 = idx[9] - g_1005f854;
    v4 = (v2 ^ v2 >> 31) - (v2 >> 31);
    v1 = idx[10] - g_1005f858;
    v3 = (v1 ^ v1 >> 31) - (v1 >> 31);
    v7 = g_101dfe90 + 2;
    if (v4 > v7)
    {
        return (v1 ^ v1 >> 31) - (v1 >> 31);
    }
    else if (v3 <= v7)
    {
        g_100f0e24 = 1;
    }
    else
    {
        return (v1 ^ v1 >> 31) - (v1 >> 31);
    }
    return sub_10014e64(idx);
}
```

## `sub_10014b67` `0x10014b67`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10014b67(void)
{
}
```

## `sub_10014b75` `0x10014b75`

_120 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern unsigned int g_100f0dcc;
extern unsigned int g_100f0e24;
extern unsigned int g_101dfe90;

int sub_10014b75(unsigned int *idx)
{
    unsigned int v5;  // eax
    unsigned int v6;  // ebx
    unsigned int v7;  // esi
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    if (g_100f0dcc)
        return v5;
    if (g_100f0e24)
        return sub_10014c69(idx);
    v0 = v6;
    v2 = idx[9] - g_1005f854;
    v4 = (v2 ^ v2 >> 31) - (v2 >> 31);
    v1 = idx[10] - g_1005f858;
    v3 = (v1 ^ v1 >> 31) - (v1 >> 31);
    v7 = g_101dfe90 + 2;
    if (v4 > v7)
    {
        return (v1 ^ v1 >> 31) - (v1 >> 31);
    }
    else if (v3 <= v7)
    {
        g_100f0e24 = 1;
    }
    else
    {
        return (v1 ^ v1 >> 31) - (v1 >> 31);
    }
    return sub_10014c69(idx);
}
```

## `sub_10014be1` `0x10014be1`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10014be1(void)
{
}
```

## `sub_10014bef` `0x10014bef`

_120 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern unsigned int g_100f0dcc;
extern unsigned int g_100f0e24;
extern unsigned int g_101dfe90;

int sub_10014bef(unsigned int *idx)
{
    unsigned int v5;  // eax
    unsigned int v6;  // ebx
    unsigned int v7;  // esi
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    if (g_100f0dcc)
        return v5;
    if (g_100f0e24)
        return sub_10014d75(idx);
    v0 = v6;
    v2 = idx[9] - g_1005f854;
    v4 = (v2 ^ v2 >> 31) - (v2 >> 31);
    v1 = idx[10] - g_1005f858;
    v3 = (v1 ^ v1 >> 31) - (v1 >> 31);
    v7 = g_101dfe90 + 2;
    if (v4 > v7)
    {
        return (v1 ^ v1 >> 31) - (v1 >> 31);
    }
    else if (v3 <= v7)
    {
        g_100f0e24 = 1;
    }
    else
    {
        return (v1 ^ v1 >> 31) - (v1 >> 31);
    }
    return sub_10014d75(idx);
}
```

## `sub_10014c5b` `0x10014c5b`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10014c5b(void)
{
}
```

## `sub_10014c69` `0x10014c69`

_264 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern unsigned int g_100f0dcc;
extern unsigned int g_100f0e28;
extern unsigned int g_101dfe90;

int sub_10014c69(void)
{
    unsigned int v6;  // eax
    unsigned int idx[11];  // edi
    unsigned int v8;  // esi
    unsigned int v10;  // ebx
    unsigned int v0;  // [bp-0x1c]
    int v1;  // [bp-0x14]
    int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    unsigned int v5[11];  // [bp+0x4]

    if (g_100f0dcc)
    {
        return;
    }
    else if (g_100f0e28)
    {
        sub_10014e64(v5);
        return;
    }
    else
    {
        v0 = v6;
        idx = v5;
        v2 = idx[9] - g_1005f854;
        v4 = (v2 ^ v2 >> 31) - (v2 >> 31);
        v1 = idx[10] - g_1005f858;
        v3 = (v1 ^ v1 >> 31) - (v1 >> 31);
        v8 = g_101dfe90 + 2;
        if (v4 < v8 && v3 < v8)
        {
            sub_10014825(v10);
            return;
        }
        if (v4 <= v8 && v3 <= v8)
        {
            if (v2 > 64)
            {
                if ((char)v10 == 2)
                {
                    return;
                }
                else if ((char)v10 == 5)
                {
                    return;
                }
                else if ((char)v10 == 6)
                {
                    return;
                }
            }
            if (v2 < 64)
            {
                if ((char)v10 == 4)
                {
                    return;
                }
                else if ((char)v10 == 7)
                {
                    return;
                }
                else if ((char)v10 == 8)
                {
                    return;
                }
            }
            if (v1 > 64)
            {
                if ((char)v10 == 3)
                {
                    return;
                }
                else if ((char)v10 == 5)
                {
                    return;
                }
                else if ((char)v10 == 7)
                {
                    return;
                }
            }
            if (v1 < 64)
            {
                if ((char)v10 == 1)
                {
                    return;
                }
                else if ((char)v10 == 5)
                {
                    return;
                }
                else if ((char)v10 == 8)
                {
                    return;
                }
            }
            sub_10014825(v10);
            return;
        }
        v2 += 8;
        v1 += 6;
        sub_10013e4d(v5);
        return;
    }
}
```

## `sub_10014d08` `0x10014d08`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10014d08(void)
{
}
```

## `sub_10014d3c` `0x10014d3c`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10014d3c(void)
{
}
```

## `sub_10014d75` `0x10014d75`

_235 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern unsigned int g_100f0dcc;
extern unsigned int g_101dfe90;

int sub_10014d75(void)
{
    unsigned int v6;  // eax
    unsigned int idx[11];  // edi
    unsigned int v8;  // esi
    unsigned int v10;  // ebx
    unsigned int v0;  // [bp-0x1c]
    int v1;  // [bp-0x14]
    int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    unsigned int v5[11];  // [bp+0x4]

    if (g_100f0dcc)
        return;
    v0 = v6;
    idx = v5;
    v2 = idx[9] - g_1005f854;
    v4 = (v2 ^ v2 >> 31) - (v2 >> 31);
    v1 = idx[10] - g_1005f858;
    v3 = (v1 ^ v1 >> 31) - (v1 >> 31);
    v8 = g_101dfe90 + 2;
    if (v4 < v8 && v3 < v8)
    {
        sub_10014825(v10);
        return;
    }
    if (v4 <= v8 && v3 <= v8)
    {
        if (v2 > 64)
        {
            if ((char)v10 == 2)
            {
                return;
            }
            else if ((char)v10 == 5)
            {
                return;
            }
            else if ((char)v10 == 6)
            {
                return;
            }
        }
        if (v2 < 64)
        {
            if ((char)v10 == 4)
            {
                return;
            }
            else if ((char)v10 == 7)
            {
                return;
            }
            else if ((char)v10 == 8)
            {
                return;
            }
        }
        if (v1 > 64)
        {
            if ((char)v10 == 3)
            {
                return;
            }
            else if ((char)v10 == 5)
            {
                return;
            }
            else if ((char)v10 == 7)
            {
                return;
            }
        }
        if (v1 < 64)
        {
            if ((char)v10 == 1)
            {
                return;
            }
            else if ((char)v10 == 5)
            {
                return;
            }
            else if ((char)v10 == 8)
            {
                return;
            }
        }
        sub_10014825(v10);
        return;
    }
    sub_10013e4d(v5);
    return;
}
```

## `sub_10014dff` `0x10014dff`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10014dff(void)
{
}
```

## `sub_10014e33` `0x10014e33`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10014e33(void)
{
}
```

## `sub_10014e64` `0x10014e64`

_172 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;
extern unsigned int g_100f0dcc;
extern unsigned int g_101dfe90;

unsigned int sub_10014e64(unsigned int *idx)
{
    unsigned int v4;  // eax
    unsigned int v5;  // esi
    unsigned int v6;  // ebx
    unsigned int v7;  // ebx
    unsigned int v8;  // ebx
    int node;  // [bp-0x14]
    int iter;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    if (g_100f0dcc)
        return v4;
    iter = idx[9] - g_1005f854;
    v3 = (iter ^ iter >> 31) - (iter >> 31);
    node = idx[10] - g_1005f858;
    v2 = (node ^ node >> 31) - (node >> 31);
    v5 = g_101dfe90 + 2;
    if (v3 < v5 && v2 < v5)
        return sub_10014825(v6);
    if (v3 <= v5 && v2 <= v5)
    {
        iter += 8;
        node += 6;
        sub_1000e6b9(iter, node, g_101dfe90 + 2);
        return sub_10014825(v7);
    }
    iter += 8;
    node += 6;
    sub_1000f40a(iter, node, v5);
    return sub_10014825(v8);
}
```

## `sub_10014f10` `0x10014f10`

_740 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[80];
    char field_50;
} struct_0;

extern unsigned int g_100432af;
extern unsigned int g_10052a8d;
extern unsigned int g_10052a95;
extern unsigned int g_10052a9d;
extern unsigned int g_10052b1d;
extern unsigned int g_10052b2d;
extern unsigned int g_10052bad;
extern unsigned int g_10052bb5;
extern unsigned int g_10052bbd;
extern unsigned int g_1005f7d5;
extern struct_0 *g_1005f7ed;
extern int g_1005f854;
extern int g_1005f858;
extern int g_1005f85c;
extern unsigned int g_1008b89f;
extern unsigned int g_100f0dc4;
extern unsigned int g_100f0dc8;
extern unsigned int g_100f0dcc;
extern unsigned int g_63fe60;
extern unsigned int g_63fe64;

int sub_10014f10(void)
{
    unsigned int idx[11];  // eax
    int v6;  // eax
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned short v2;  // [bp-0x14]
    char v3;  // [bp-0x12]
    unsigned int v4[11];  // [bp+0x4]

    if (g_100f0dcc)
        return;
    if (g_100f0dc8)
        g_100f0dc8 = g_100f0dc8 - 10;
    idx = v4;
    v1 = idx[9] - g_1005f854;
    v0 = idx[10] - g_1005f858;
    v2 = 1;
    if (v1 == 1 && !v0)
    {
        if (g_1005f7ed->field_50 != 1)
        {
            v3 = 112;
            sub_1002ade7(&v2, 3);
            return;
        }
        else if (g_1005f7d5 < 20)
        {
            return;
        }
    }
    else
    {
        if (!v1 && v0 == 4294967295)
        {
            if (g_1005f7ed->field_50)
            {
                v3 = 111;
                sub_1002ade7(&v2, 3);
                return;
            }
            else if (g_1005f7d5 < 20)
            {
                return;
            }
        }
        else
        {
            if (v1 == 4294967295 && !v0)
            {
                if (g_1005f7ed->field_50 != 3)
                {
                    v3 = 114;
                    sub_1002ade7(&v2, 3);
                    return;
                }
                else if (g_1005f7d5 < 20)
                {
                    return;
                }
            }
            else
            {
                if (!(!v1 && v0 == 1))
                {
                    if ((g_10052a8d == 4294967294 || g_10052a9d == 4294967294) && g_10052a95 < 4294967294 && (!g_100f0dc8 || v1 && v0 == 4294967295))
                    {
                        sub_10015204(g_1005f854, g_1005f858 - 1, g_1005f85c);
                        g_100f0dc4 = 3;
                        return;
                    }
                    if ((g_10052bbd == 4294967294 || g_10052a9d == 4294967294) && g_10052b2d < 4294967294 && (!g_100f0dc8 || v1 == 1 && v0))
                    {
                        sub_10015204(g_1005f854 + 1, g_1005f858, g_1005f85c);
                        g_100f0dc4 = 3;
                        return;
                    }
                    if ((g_10052bad == 4294967294 || g_10052bbd == 4294967294) && g_10052bb5 < 4294967294 && (!g_100f0dc8 || v1 && v0 == 1))
                    {
                        sub_10015204(g_1005f854, g_1005f858 + 1, g_1005f85c);
                        g_100f0dc4 = 3;
                        return;
                    }
                    if (g_10052bad != 4294967294 && g_10052a8d != 4294967294)
                        return;
                    if (g_10052b1d >= 4294967294)
                        return;
                    if (g_100f0dc8)
                    {
                        if (v1 == 4294967295)
                        {
                            if (!v0)
                                return;
                        }
                        else
                        {
                            return;
                        }
                    }
                    sub_10015204(g_1005f854 - 1, g_1005f858, g_1005f85c);
                    g_100f0dc4 = 3;
                    return;
                }
                else if (g_1005f7ed->field_50 != 2)
                {
                    v3 = 113;
                    sub_1002ade7(&v2, 3);
                    return;
                }
                else if (g_1005f7d5 < 20)
                {
                    return;
                }
            }
        }
    }
    if (g_63fe64 && v4[0] != g_63fe64)
    {
        g_100432af = 0;
        g_1008b89f = 0;
        g_63fe64 = 0;
        g_63fe60 = 0;
        sub_1002ade7("\t", 11);
    }
    sub_1003a60a(v4, v6);
    g_100f0dc8 = 100;
    return;
}
```

## `sub_100151f4` `0x100151f4`

_16 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_100f0dc4;

void sub_100151f4(unsigned int a0)
{
    g_100f0dc4 = a0;
    return;
}
```

## `sub_10015204` `0x10015204`

_36 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;

int sub_10015204(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v2 = 0;
    v1 = a1 - g_1005f858;
    v0 = a0 - g_1005f854;
    return 5049888();
}
```

## `sub_10015228` `0x10015228`

_63 bytes. refs " >> ", "%s %s %s"_

```c
typedef struct struct_0 {
    char padding_0[33];
    char field_21;
} struct_0;


int sub_10015228(unsigned int a0, struct_0 *a1)
{
    unsigned int v3;  // eax
    struct_0 *v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v3 = a1->field_21;
    if (!v3)
        return lstrcpy(a0, a1);
    v2 = 268470766 + 4 * v3;
    v1 = " >> ";
    v0 = a1;
    return wsprintfA(a0, "%s %s %s");
}
```

## `sub_10015267` `0x10015267`

_950 bytes. calls SendDlgItemMessageA; refs "<New Monster>", "%d %d %d %s", "scripts\\*.elft"_

```c
typedef struct struct_0 {
    char padding_0[33];
    char field_21;
} struct_0;

extern int g_10042f83;
extern HWND g_10072f8c;
extern char g_100f0d39;
extern struct_0 g_101d5e78;
extern struct_0 g_101dfe78;
extern LPARAM g_101dfe7c;
extern LPARAM g_101dfe80;
extern LPARAM g_101dfe84;
extern LPARAM g_101dfe88;
extern LPARAM g_101dfe8c;
extern WPARAM g_101dfe90;
extern WPARAM g_101dfe94;
extern WPARAM g_101dfe98;
extern char g_101dfe9c;
extern char g_101dfe9d;
extern char g_101dfe9e;
extern WPARAM g_101dfe9f;
extern char g_101dfea3;
extern char g_101dfea4;
extern unsigned int g_101dfea5[3];
extern unsigned int g_101e6ea5[3];

int sub_10015267(void)
{
    unsigned int v7;  // eax
    struct_0 *i;  // ebx
    unsigned int iter[3];  // ebx
    void* count;  // eax
    void* k;  // ecx
    unsigned long v12;  // ldt
    unsigned long v13;  // gdt
    unsigned short v14;  // ss
    unsigned long v15;  // 4121
    unsigned int v0;  // [bp-0x218]
    unsigned int v1;  // [bp-0x214]
    unsigned int v2;  // [bp-0x210]
    char *v3;  // [bp-0x20c], Other Possible Types: unsigned int [3]
    void* v4;  // [bp-0x208]
    char v5;  // [bp-0x204]

    g_100f0d39 = 1;
    if (!v7)
    {
        SendDlgItemMessageA(g_10072f8c, 1001, 1029, 0x1, *((int *)&g_101dfe78.padding_0[0]));
        SendDlgItemMessageA(g_10072f8c, 1002, 1029, 0x1, g_101dfe7c);
        SendDlgItemMessageA(g_10072f8c, 1003, 1029, 0x1, g_101dfe80);
        SendDlgItemMessageA(g_10072f8c, 1004, 1029, 0x1, g_101dfe84);
        SendDlgItemMessageA(g_10072f8c, 1039, 1029, 0x1, g_101dfe88);
        SendDlgItemMessageA(g_10072f8c, 1044, 1029, 0x1, g_101dfe8c);
        SendDlgItemMessageA(g_10072f8c, 1013, 390, g_101dfe90, NULL);
        SendDlgItemMessageA(g_10072f8c, 1052, 390, g_101dfe98, NULL);
        SendDlgItemMessageA(g_10072f8c, 1047, 390, g_101dfe94, NULL);
        SendDlgItemMessageA(g_10072f8c, 1069, 390, g_101dfe9f, NULL);
        SendDlgItemMessageA(g_10072f8c, 1011, 241, g_101dfe9c, NULL);
        SendDlgItemMessageA(g_10072f8c, 1012, 241, g_101dfe9d, NULL);
        SendDlgItemMessageA(g_10072f8c, 1061, 241, g_101dfe9e, NULL);
        SendDlgItemMessageA(g_10072f8c, 1073, 241, g_101dfea3, NULL);
        SendDlgItemMessageA(g_10072f8c, 1074, 241, g_101dfea4, NULL);
        SendDlgItemMessageA(g_10072f8c, 0x404, 388, NULL, NULL);
        for (i = &g_101d5e78.padding_0[0]; i < &g_101dfe78.padding_0[0] && i->padding_0[0]; i = &i[9].padding_0[14])
        {
            sub_10015228(&v5, i);
            SendDlgItemMessageA(g_10072f8c, 0x404, 385, 0xffffffff, &v5);
        }
        SendDlgItemMessageA(g_10072f8c, 0x404, 385, 0xffffffff, "<New Monster>");
        SendDlgItemMessageA(g_10072f8c, 1062, 388, NULL, NULL);
        for (iter = &g_101dfea5[0]; iter < &g_101e6ea5[0] && iter[0]; iter = &iter[2 + 1])
        {
            v3 = iter + 1;
            v2 = iter[2];
            v1 = iter[1];
            v0 = iter[0];
            wsprintfA(&v5, "%d %d %d %s");
            SendDlgItemMessageA(g_10072f8c, 1062, 385, 0xffffffff, &v5);
        }
    }
    lstrcpy(&v5, &g_10042f83);
    lstrcat(&v5, "scripts\\*.elft");
    DlgDirListA(g_10072f8c, &v5, 1009, 0, DDL_READONLY);
    count = SendDlgItemMessageA(g_10072f8c, 1009, 395, NULL, NULL);
    for (k = NULL; k < count; k = v4 + 1)
    {
        v4 = k;
        SendDlgItemMessageA(g_10072f8c, 1009, 393, v4, &v5);
        v3 = &v5;
        v15 = _ccall(v12, v13, (unsigned int)v14, &v3 - 3 + lstrlen(&v5));
        *((char *)v15) = 0;
        SendDlgItemMessageA(g_10072f8c, 1009, 386, v4, NULL);
        SendDlgItemMessageA(g_10072f8c, 1009, 385, v4, &v5);
    }
    g_100f0d39 = 0;
    return;
}
```

## `sub_1001561d` `0x1001561d`

_177 bytes. (leaf/helper — see body)_

```c
int sub_1001561d(void* a0, unsigned int a1, void* a2)
{
    void* node;  // esi
    unsigned int v1;  // ecx
    void* iter;  // edi
    unsigned int iter1;  // ebx
    unsigned int v4;  // ecx
    char v5;  // al

    node = a0;
    v1 = a1;
    *((unsigned int *)a2) = 4294966944;
    iter = a2 + 4;
    iter1 = 0;
    while (true)
    {
        v4 = v1;
        if (!v1)
            break;
        if (*((char *)node))
        {
            for (; iter1 > 0x3fff; iter1 -= 0x3fff)
            {
                *((unsigned short *)iter) = 65535;
                iter += 2;
            }
            if (iter1 > 63)
            {
                v5 = iter1;
                *((char *)&iter[1]) = v5;
                *((char *)iter) = v5;
                *((char *)iter) = *((char *)iter) | 192;
                iter += 2;
                iter1 = 0;
            }
            *((char *)iter) = iter1;
            if (!((char)node[1] && v4 > 1))
            {
                *((char *)&iter[1]) = *((char *)node);
                iter += 2;
                node += 1;
                v1 = v4 - 1;
            }
            else if ((short)node[2] && v4 > 3)
            {
                *((char *)iter) = *((char *)iter) | 128;
                *((int *)&iter[1]) = *((int *)node);
                iter += 5;
                node += 4;
                v1 = v4 - 4;
            }
            else
            {
                *((char *)iter) = *((char *)iter) | 64;
                *((short *)&iter[1]) = *((short *)node);
                iter += 3;
                node += 2;
                v1 = v4 - 2;
            }
            iter1 = 0;
        }
        else
        {
            iter1 += 1;
            node += 1;
            v1 = v4 - 1;
        }
    }
    return iter - a2;
}
```

## `sub_100156ce` `0x100156ce`

_373 bytes. calls CreateFileA, WriteFile; refs "Targeting Files", "Select a Targeting file to save", "scripts\\"_

```c
typedef struct OPENFILENAMEA {
    unsigned int lStructSize;
    HWND hwndOwner;
    HINSTANCE hInstance;
    PSTR lpstrFilter;
    PSTR lpstrCustomFilter;
    unsigned int nMaxCustFilter;
    unsigned int nFilterIndex;
    PSTR lpstrFile;
    unsigned int nMaxFile;
    PSTR lpstrFileTitle;
    unsigned int nMaxFileTitle;
    PSTR lpstrInitialDir;
    PSTR lpstrTitle;
    enum OPEN_FILENAME_FLAGS Flags;
    unsigned short nFileOffset;
    unsigned short nFileExtension;
    PSTR lpstrDefExt;
    LPARAM lCustData;
    void* lpfnHook;
    PSTR lpTemplateName;
    void* pvReserved;
    unsigned int dwReserved;
    enum OPEN_FILENAME_FLAGS_EX FlagsEx;
} OPENFILENAMEA;

extern char g_10042e7f;
extern int g_10042f83;
extern int g_10043094;
extern unsigned int g_1005f60a;
extern unsigned int g_1005f622;
extern unsigned int g_10072f8c;
extern void g_101d5e78;

int sub_100156ce(char *a0)
{
    void* v3;  // eax
    unsigned int count;  // eax
    int v5;  // eax
    unsigned int v0;  // [bp-0x190]
    OPENFILENAMEA v1;  // [bp-0x184]
    HANDLE v2;  // [bp-0x8]

    v3 = HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, 0x200000);
    v1 = (OPENFILENAMEA)_INSERT(v1 CONCAT 0, 76, v3);
    count = sub_1001561d(&g_101d5e78, 69677, v3);
    if (!*(a0))
    {
        sub_1002ae81(&v1, 76);
        v1.lStructSize = 76;
        v0 = g_10072f8c;
        v1.hwndOwner = g_10072f8c;
        v0 = g_1005f60a;
        v1.hInstance = g_1005f60a;
        v1.lpstrFilter = "Targeting Files";
        v1.lpstrFile = &g_10043094;
        v1.nMaxFile = 260;
        *((unsigned int *)&v1.Flags) = 2621444;
        v1.lpstrTitle = "Select a Targeting file to save";
        v1.lpstrInitialDir = &g_10042e7f;
        v5 = GetSaveFileNameA(&v1);
        if (!v5)
            return v5;
        lstrcpy(&v1.dwReserved, &g_10043094);
    }
    else
    {
        lstrcpy(&v1.dwReserved, &g_10042f83);
        lstrcat(&v1.dwReserved, "scripts\\");
        lstrcat(&v1.dwReserved, a0);
        lstrcat(&v1.dwReserved, ".elft");
    }
    v2 = CreateFileA(&v1.dwReserved, 0xc0000000, 3, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_ARCHIVE, NULL);
    if (v2 != 0xffffffff)
    {
        WriteFile(v2, v1.pvReserved, count, &g_1005f622, NULL);
        CloseHandle(v2);
    }
    else
    {
        sub_100159d8();
    }
    return HeapFree(GetProcessHeap(), HEAP_NONE, v1.pvReserved);
}
```

## `sub_10015843` `0x10015843`

_405 bytes. calls CreateFileA, ReadFile; refs "Targeting Files", "Select a Targeting file to open", "scripts\\"_

```c
typedef struct OPENFILENAMEA {
    unsigned int lStructSize;
    HWND hwndOwner;
    HINSTANCE hInstance;
    PSTR lpstrFilter;
    PSTR lpstrCustomFilter;
    unsigned int nMaxCustFilter;
    unsigned int nFilterIndex;
    PSTR lpstrFile;
    unsigned int nMaxFile;
    PSTR lpstrFileTitle;
    unsigned int nMaxFileTitle;
    PSTR lpstrInitialDir;
    PSTR lpstrTitle;
    enum OPEN_FILENAME_FLAGS Flags;
    unsigned short nFileOffset;
    unsigned short nFileExtension;
    PSTR lpstrDefExt;
    LPARAM lCustData;
    void* lpfnHook;
    PSTR lpTemplateName;
    void* pvReserved;
    unsigned int dwReserved;
    enum OPEN_FILENAME_FLAGS_EX FlagsEx;
} OPENFILENAMEA;

extern char g_10042e7f;
extern int g_10042f83;
extern int g_10043094;
extern unsigned int g_1005f60a;
extern unsigned int g_1005f622;
extern unsigned int g_10072f8c;
extern void g_101d5e78;

int sub_10015843(char *a0, unsigned int a1)
{
    int v5;  // eax
    unsigned int v0;  // [bp-0x190]
    OPENFILENAMEA v1;  // [bp-0x184]
    void* v2;  // [bp-0x138]
    Byte v3[300];  // [bp-0x134]
    HANDLE v4;  // [bp-0x8]

    if (a1)
    {
        lstrcpy(v3, a0);
    }
    else if (!*(a0))
    {
        sub_1002ae81(&v1, 76);
        v1 = (OPENFILENAMEA)_INSERT(v1 CONCAT 0, 0, 76);
        v0 = g_10072f8c;
        v1.hwndOwner = g_10072f8c;
        v0 = g_1005f60a;
        v1.hInstance = g_1005f60a;
        v1.lpstrFilter = "Targeting Files";
        v1.lpstrFile = &g_10043094;
        v1.nMaxFile = 260;
        *((unsigned int *)&v1.Flags) = 2621444;
        v1.lpstrTitle = "Select a Targeting file to open";
        v1.lpstrInitialDir = &g_10042e7f;
        v5 = GetOpenFileNameA(&v1);
        if (!v5)
            return v5;
        lstrcpy(&v1.dwReserved, &g_10043094);
    }
    else
    {
        lstrcpy(v3, &g_10042f83);
        lstrcat(v3, "scripts\\");
        lstrcat(v3, a0);
        lstrcat(v3, ".elft");
    }
    v2 = HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, 0x200000);
    v4 = CreateFileA(v3, 0xc0000000, 3, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_ARCHIVE, NULL);
    if (v4 != 0xffffffff)
    {
        ReadFile(v4, v2, GetFileSize(v4, NULL), &g_1005f622, NULL);
        CloseHandle(v4);
    }
    sub_10012771(&g_101d5e78, 69677, v2);
    return HeapFree(GetProcessHeap(), HEAP_NONE, v2);
}
```

## `sub_100159d8` `0x100159d8`

_37 bytes. calls MessageBoxA_

```c
extern char g_1005dc49;
extern HWND g_1005f626;

enum MESSAGEBOX_RESULT sub_100159d8(void)
{
    enum MESSAGEBOX_RESULT v1;  // eax

    if (!g_1005dc49)
    {
        g_1005dc49 = 1;
        v1 = MessageBoxA(g_1005f626, "ElfBot was unable to save your settings. If you are running Vista, make sure that you run both the Tibia Client and ElfBot NG with Administrator privileges, or disable User Account Control (UAC). You can find information on how to do this on the web.", NULL, MB_APPLMODAL);
    }
    return v1;
}
```

## `sub_100159fd` `0x100159fd`

_380 bytes. calls CreateFileA, WriteFile; refs "Cavebot Files", "Select a Cavebot file to save", "scripts\\"_

```c
typedef struct OPENFILENAMEA {
    unsigned int lStructSize;
    HWND hwndOwner;
    HINSTANCE hInstance;
    PSTR lpstrFilter;
    PSTR lpstrCustomFilter;
    unsigned int nMaxCustFilter;
    unsigned int nFilterIndex;
    PSTR lpstrFile;
    unsigned int nMaxFile;
    PSTR lpstrFileTitle;
    unsigned int nMaxFileTitle;
    PSTR lpstrInitialDir;
    PSTR lpstrTitle;
    enum OPEN_FILENAME_FLAGS Flags;
    unsigned short nFileOffset;
    unsigned short nFileExtension;
    PSTR lpstrDefExt;
    LPARAM lCustData;
    void* lpfnHook;
    PSTR lpTemplateName;
    void* pvReserved;
    unsigned int dwReserved;
    enum OPEN_FILENAME_FLAGS_EX FlagsEx;
} OPENFILENAMEA;

extern char g_10042e7f;
extern int g_10042f83;
extern int g_10043198;
extern unsigned int g_1005f60a;
extern unsigned int g_1005f622;
extern unsigned int g_10072f94;
extern void g_101e6ea8;
extern char g_10207f3a;

int sub_100159fd(char *a0)
{
    void* v3;  // eax
    unsigned int count;  // eax
    int v5;  // eax
    unsigned int v0;  // [bp-0x190]
    OPENFILENAMEA v1;  // [bp-0x184]
    HANDLE v2;  // [bp-0x8]

    g_10207f3a = 1;
    v3 = HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, 0x200000);
    v1 = (OPENFILENAMEA)_INSERT(v1 CONCAT 0, 76, v3);
    count = sub_1001561d(&g_101e6ea8, 659603, v3);
    if (!*(a0))
    {
        sub_1002ae81(&v1, 76);
        v1.lStructSize = 76;
        v0 = g_10072f94;
        v1.hwndOwner = g_10072f94;
        v0 = g_1005f60a;
        v1.hInstance = g_1005f60a;
        v1.lpstrFilter = "Cavebot Files";
        v1.lpstrFile = &g_10043198;
        v1.nMaxFile = 260;
        *((unsigned int *)&v1.Flags) = 2621444;
        v1.lpstrTitle = "Select a Cavebot file to save";
        v1.lpstrInitialDir = &g_10042e7f;
        v5 = GetSaveFileNameA(&v1);
        if (!v5)
            return v5;
        lstrcpy(&v1.dwReserved, &g_10043198);
    }
    else
    {
        lstrcpy(&v1.dwReserved, &g_10042f83);
        lstrcat(&v1.dwReserved, "scripts\\");
        lstrcat(&v1.dwReserved, a0);
        lstrcat(&v1.dwReserved, ".elfc");
    }
    v2 = CreateFileA(&v1.dwReserved, 0x40000000, FILE_SHARE_WRITE, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_ARCHIVE, NULL);
    if (v2 != 0xffffffff)
    {
        WriteFile(v2, v1.pvReserved, count, &g_1005f622, NULL);
        CloseHandle(v2);
    }
    else
    {
        sub_100159d8();
    }
    return HeapFree(GetProcessHeap(), HEAP_NONE, v1.pvReserved);
}
```

## `sub_10015b79` `0x10015b79`

_545 bytes. calls CreateFileA, ReadFile; refs "Cavebot Files", "Select a Cavebot file to open", "scripts\\"_

```c
typedef struct OPENFILENAMEA {
    unsigned int lStructSize;
    HWND hwndOwner;
    HINSTANCE hInstance;
    PSTR lpstrFilter;
    PSTR lpstrCustomFilter;
    unsigned int nMaxCustFilter;
    unsigned int nFilterIndex;
    PSTR lpstrFile;
    unsigned int nMaxFile;
    PSTR lpstrFileTitle;
    unsigned int nMaxFileTitle;
    PSTR lpstrInitialDir;
    PSTR lpstrTitle;
    enum OPEN_FILENAME_FLAGS Flags;
    unsigned short nFileOffset;
    unsigned short nFileExtension;
    PSTR lpstrDefExt;
    LPARAM lCustData;
    void* lpfnHook;
    PSTR lpTemplateName;
    void* pvReserved;
    unsigned int dwReserved;
    enum OPEN_FILENAME_FLAGS_EX FlagsEx;
} OPENFILENAMEA;

extern char g_10042e7f;
extern int g_10042f83;
extern char g_10043194;
extern char g_10043198;
extern unsigned int g_1005f60a;
extern unsigned int g_1005f622;
extern unsigned int g_10072f94;
extern void g_101e6ea8;
extern int g_101f2ea8;
extern int g_10202ea8;
extern char g_10207f3a;
extern int g_10207f3b;

int sub_10015b79(char *a0, unsigned int a1)
{
    unsigned int v5;  // eax
    int len;  // eax
    unsigned int v7;  // eax
    int v9;  // ebx
    int i;  // edx
    int v11;  // edx
    unsigned int v0;  // [bp-0x190]
    OPENFILENAMEA v1;  // [bp-0x184]
    void* v2;  // [bp-0x138]
    Byte v3[300];  // [bp-0x134]
    HANDLE v4;  // [bp-0x8]

    if (a1)
    {
        lstrcpy(v3, a0);
    }
    else if (!*(a0))
    {
        sub_1002ae81(&v1, 76);
        v1 = (OPENFILENAMEA)_INSERT(v1 CONCAT 0, 0, 76);
        v0 = g_10072f94;
        v1.hwndOwner = g_10072f94;
        v0 = g_1005f60a;
        v1.hInstance = g_1005f60a;
        v1.lpstrFilter = "Cavebot Files";
        v1.lpstrFile = &g_10043198;
        v1.nMaxFile = 260;
        *((unsigned int *)&v1.Flags) = 2621444;
        v1.lpstrTitle = "Select a Cavebot file to open";
        v1.lpstrInitialDir = &g_10042e7f;
        v5 = GetOpenFileNameA(&v1);
        if (!v5)
            return v5;
        len = lstrlen(&g_10043198);
        if (len > 5 && (*((int *)&(&g_10043194)[len]) | 0x20202000) == 1953527598)
        {
            v7 = sub_100167eb(&g_10043198);
            g_10043198 = 0;
            return v7;
        }
        lstrcpy(&v1.dwReserved, &g_10043198);
    }
    else
    {
        lstrcpy(v3, &g_10042f83);
        lstrcat(v3, "scripts\\");
        lstrcat(v3, a0);
        lstrcat(v3, ".elfc");
    }
    v2 = HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, 0x200000);
    v4 = CreateFileA(v3, 0x80000000, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_ARCHIVE, NULL);
    if (v4 != 0xffffffff)
    {
        ReadFile(v4, v2, GetFileSize(v4, NULL), &g_1005f622, NULL);
        CloseHandle(v4);
    }
    g_10207f3a = 0;
    sub_10012771(&g_101e6ea8, 659603, v2);
    if (!g_10207f3a)
    {
        v9 = &g_101f2ea8;
        for (i = &g_10207f3b; v9 < &g_10202ea8; i = v11 + 0x1000)
        {
            sub_1002ae6f(i, v9, 0x200);
            v9 += 0x200;
        }
        sub_1002ae81(&g_101f2ea8, 1);
        g_10207f3a = 1;
    }
    HeapFree(GetProcessHeap(), HEAP_NONE, v2);
    return (unsigned int)sub_10008152();
}
```

## `sub_10015d9a` `0x10015d9a`

_546 bytes. (leaf/helper — see body)_

```c
int sub_10015d9a(void)
{
    unsigned int v5;  // edi
    unsigned int v6;  // edx
    int v7;  // ebx
    unsigned int v0;  // [bp-0x15]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v2 = v5;
    v1 = v6;
    v0 = /* unsupported instruction */;
    sub_10015da3(v7);
    return;
}
```

## `sub_10015da3` `0x10015da3`

_32 bytes. calls SendDlgItemMessageA_

```c
extern WPARAM g_10042929;
extern HWND g_10072f94;

int sub_10015da3(void)
{
    SendDlgItemMessageA(g_10072f94, 0x404, 48, g_10042929, NULL);
}
```

