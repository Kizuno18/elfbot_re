# elfbot.dll decompiled — loader 0x004143b0..0x00415e52

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_004143b0` `0x004143b0`

_3849 bytes. refs ", v10);
    v68 = sub_403e78(v40, ", ";
        sub_403d40(v69, ", ", v8);
    v75 = sub_403e78(v40, "_

```c
typedef struct struct_9 {
    char padding_0[5];
    char field_5;
} struct_9;

typedef struct struct_7 {
    char padding_0[5];
    char field_5;
    char padding_6[2];
    void* field_8;
    char field_c;
    char padding_d[3];
    int field_10;
    struct struct_3 *field_14;
    void* field_18;
    void* field_1c;
    void* field_20;
    char field_24;
    char padding_25[3];
    unsigned int field_28;
    char padding_2c[4];
    unsigned int field_30;
    char field_34;
    char field_35;
    char field_36;
    char padding_37[1];
    void* field_38;
    void* field_3c;
    unsigned int field_40;
    unsigned short field_44;
    unsigned int field_46;
    unsigned short field_4a;
} struct_7;

typedef struct struct_0 {
    char padding_0[5];
    char padding_5[3];
    unsigned int field_5;
} struct_0;

typedef struct struct_11 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    char padding_c[10];
    char field_16;
    char field_17;
} struct_11;

typedef struct struct_4 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    void* field_c;
    unsigned int field_10;
    unsigned short field_14;
    char field_16[6];
    struct struct_3 *field_18;
    char field_1a;
    char padding_1b[5];
    struct struct_3 *field_20;
    void* field_24;
} struct_4;

typedef struct struct_10 {
    char field_0;
    unsigned int field_1;
    char field_5;
    unsigned short field_6;
    struct struct_10 *field_8;
    char field_c;
    char field_d;
} struct_10;

typedef struct struct_3 {
    void* field_0;
} struct_3;

extern char g_4117b4;
extern char g_41eda0;
extern void g_41f0c8;
extern unsigned int g_41f57c;

int sub_4143b0(void)
{
    unsigned int v52;  // ecx
    unsigned int i;  // ecx
    unsigned long v62;  // 4132
    unsigned long v63;  // 4141
    unsigned long v64;  // 4119
    unsigned long v65;  // 4127
    void* idx;  // ebx
    void* idx1;  // eax, Other Possible Types: int
    unsigned int v68;  // eax
    unsigned int v69;  // edi
    unsigned long v70;  // 4145
    unsigned long v71;  // 4149
    unsigned int v54;  // ecx
    unsigned long v72;  // 4123
    unsigned int v73;  // 4100
    unsigned long v74;  // 4131
    unsigned int v75;  // eax
    unsigned long v76;  // 4151
    unsigned int v77;  // 4100
    unsigned long v78;  // 4155
    unsigned int v79;  // ebx
    char v80;  // al
    unsigned int v81;  // eax
    unsigned int v55;  // ebx
    int v82;  // eax
    int v83;  // eax
    unsigned long v84;  // 4126
    unsigned int v85;  // 4103
    unsigned long v86;  // 4135
    unsigned long v87;  // 4116
    char v88;  // al
    int v89;  // esi
    int v90;  // esi
    unsigned int v91;  // ebx
    struct_9 *v56;  // esi
    int v92;  // esi
    struct_0 *v93;  // ecx
    char *v94;  // eax
    int v95;  // esi
    unsigned long v96;  // 4118
    int v97;  // esi
    int v98;  // esi
    unsigned int v99;  // ebx
    int v100;  // esi
    char v57;  // dl
    struct_0 *v101;  // edi
    int v102;  // esi
    unsigned long v103;  // 4163
    unsigned long v104;  // 4167
    void* v105;  // ebx
    void* iter;  // esi
    struct_11 *index;  // eax
    unsigned int v108;  // edx
    struct_11 *v109;  // esi
    struct_7 *v58;  // eax
    struct_4 *v111;  // ebx
    unsigned int j;  // ebx
    struct_10 *idx2;  // eax
    int v114;  // ebx
    int v115;  // eax
    int v116;  // eax
    void* node;  // eax
    void* k;  // esi
    unsigned int v119;  // ecx
    int v120;  // eax
    unsigned long v59;  // ldt
    unsigned int ch;  // eax
    void* v122;  // ebx
    struct_11 *v123;  // eax
    struct_7 *v124;  // edx
    struct_7 *v125;  // edx
    unsigned int v126;  // edx
    unsigned long v127;  // 4118
    unsigned long v60;  // gdt
    unsigned short v61;  // fs
    int v0;  // [bp-0x130]
    PSTR v1;  // [bp-0x128]
    PWSTR v2;  // [bp-0x120]
    unsigned int v3;  // [bp-0x11c]
    unsigned int v4;  // [bp-0x114]
    PWSTR v5;  // [bp-0x10c]
    unsigned int ch1;  // [bp-0x108]
    void* v7;  // [bp-0x104]
    unsigned int v8;  // [bp-0x100]
    unsigned int v9;  // [bp-0xf8]
    int v10;  // [bp-0xf0]
    int v11;  // [bp-0xdc]
    char *v12;  // [bp-0xd8]
    unsigned int v13;  // [bp-0xd4]
    char *v14;  // [bp-0xd0], Other Possible Types: unsigned int *, unsigned int
    char *v15;  // [bp-0xcc], Other Possible Types: unsigned int
    int *v16;  // [bp-0xbc]
    unsigned int v17;  // [bp-0xb8]
    unsigned int v18;  // [bp-0xb0]
    struct_0 *v19;  // [bp-0xac]
    unsigned int v20;  // [bp-0xa8]
    unsigned int v21;  // [bp-0x9c]
    unsigned int v22;  // [bp-0x98]
    struct_9 *v23;  // [bp-0x94]
    unsigned int v24;  // [bp-0x84]
    unsigned int v25;  // [bp-0x78]
    unsigned int v26;  // [bp-0x74]
    char *v27;  // [bp-0x70]
    unsigned int v28;  // [bp-0x68]
    unsigned int v29;  // [bp-0x64]
    unsigned int v30;  // [bp-0x4c]
    void* v31;  // [bp-0x48]
    char *v32;  // [bp-0x44]
    char v33;  // [bp-0x41]
    int v34;  // [bp-0x40], Other Possible Types: unsigned int
    unsigned int v35;  // [bp-0x3c]
    char *v36;  // [bp-0x38], Other Possible Types: unsigned int *
    void* v37;  // [bp-0x30], Other Possible Types: int
    struct_11 *v38;  // [bp-0x2c], Other Possible Types: int
    int *v39;  // [bp-0x28], Other Possible Types: struct_0
    struct_9 *v40;  // [bp-0x20]
    int *v41;  // [bp-0x1c], Other Possible Types: void* *, unsigned int
    int *v42;  // [bp-0x18], Other Possible Types: unsigned int
    unsigned int v43;  // [bp-0x14]
    unsigned int v44;  // [bp-0x10]
    char v45;  // [bp-0x9]
    struct_7 *v46;  // [bp-0x8], Other Possible Types: unsigned int
    char v47;  // [bp-0x4]
    unsigned int v48;  // [bp+0x4]
    void* *v49;  // [bp+0x8]
    int v50;  // [bp+0xc]
    void* v51;  // [bp+0x10]

    v46 = v52;
    i = 37;
    do
    {
        v43 = 0;
        v42 = 0;
        i -= 1;
    } while (i != 1);
    InterlockedExchange(&v46, v54);
    v41 = v55;
    v40 = v56;
    if (v57)
        v58 = sub_402f44();
    v45 = v57;
    v46 = v58;
    sub_403e68(idx1, v37, v38);
    sub_40402c();
    v36 = &v47;
    v35 = sub_4153d5;
    v62 = _ccall(v59, v60, (unsigned int)v61, 0);
    v34 = *((int *)v62);
    v63 = _ccall(v59, v60, (unsigned int)v61, 0);
    *((unsigned int **)v63) = &v34;
    v35 = 0;
    v46->field_20 = NULL;
    sub_4121c8();
    v32 = &v47;
    v31 = sub_415385;
    v64 = _ccall(v59, v60, (unsigned int)v61, 0);
    v30 = *((int *)v64);
    v65 = _ccall(v59, v60, (unsigned int)v61, 0);
    *((unsigned int **)v65) = &v30;
    if ((GetVersion() & -0x80000000))
        sub_40e8c8();
    *(v49) = v51;
    v46->field_30 = v52;
    v46->field_34 = ((char)v48 & 32);
    v46->field_35 = ((char)v48 & 64);
    v46->field_28 = 0;
    sub_40d8e0();
    v34 = v11;
    idx = sub_4119e8();
    v46->field_20 = idx;
    *((char *)idx) = 255;
    *((char *)&idx[1]) = 37;
    *((void* *)&idx[2]) = idx + 6;
    idx1 = v51;
    v46->field_8 = idx1;
    v46->field_10 = v50;
    v46->field_14 = v49;
    v33 = 0;
    sub_4115d0(&v40);
    sub_4115d0(&v69);
    if (!(GetVersion() & -0x80000000))
    {
        sub_403a10();
    }
    else if (v46->field_8 >= -0x80000000)
    {
        sub_403aa8();
        sub_403a10();
    }
    sub_409eac();
    sub_403d40(v40, ", ", v10);
    v68 = sub_403e78(v40, ", ", v10);
    v44 = sub_411214(v68);
    if (v69)
    {
        sub_409eac();
        v28 = ", ";
        sub_403d40(v69, ", ", v9);
        v43 = sub_411214(sub_403e78(v69, ", ", v9));
        v29 = v9;
    }
    else
    {
        v43 = 0;
        v29 = v68;
    }
    v27 = &v47;
    v26 = sub_415362;
    v70 = _ccall(v59, v60, (unsigned int)v61, 0);
    v25 = *((int *)v70);
    v71 = _ccall(v59, v60, (unsigned int)v61, 0);
    *((unsigned int **)v71) = &v25;
    if (v44)
        WaitForSingleObject(v44, 4294967295);
    if (v43)
        WaitForSingleObject(v43, 4294967295);
    v72 = _ccall(v59, v60, (unsigned int)v61, 0);
    v73 = *((int *)v72);
    v24 = *((int *)v72);
    v74 = _ccall(v59, v60, (unsigned int)v61, 0);
    *((unsigned int **)v74) = &v24;
    sub_409eac(-1, v73, sub_41532f, &v47);
    sub_403d40(v40, ", ", v8);
    v75 = sub_403e78(v40, ", ", v8);
    v42 = sub_4114f0(v75, v40);
    v46->field_5 = (char)sub_41411c(", ") ^ 1;
    v23 = v40;
    v22 = v75;
    if (v46->field_5)
    {
        v23 = v40;
        v22 = v75;
        if (v69)
        {
            v23 = 0xffffffff;
            sub_409eac(-1);
            v21 = ", ";
            sub_403d40(v69, ", ", ch1);
            v42 = sub_4114f0(sub_403e78(v69, ", ", ch1), v69);
            v46->field_5 = (char)sub_41411c(", ") ^ 1;
            v22 = ch1;
            if (!v46->field_5)
            {
                sub_403aa8();
                v22 = ch1;
            }
        }
    }
    v76 = _ccall(v59, v60, (unsigned int)v61, 0);
    v77 = *((int *)v76);
    v20 = *((int *)v76);
    v78 = _ccall(v59, v60, (unsigned int)v61, 0);
    *((unsigned int **)v78) = &v20;
    if (!v46->field_5)
    {
        v46->field_c = v40->field_5 == 83;
        goto LABEL_414b91;
    }
    if ((char)sub_413f08(v77, sub_4152fc, &v47))
    {
        v35 = 7798785;
        sub_40351c(v77, sub_4152fc);
        sub_40351c(&v47, v21);
        sub_40351c(v22, v23);
        sub_40351c(", ", v8);
    }
    else
    {
        if (!((char)v48 & 2))
        {
            if ((char)sub_413e48())
            {
                v48 |= 2;
            }
            else
            {
                sub_40d8e0();
                if (!(char)v77)
                {
                    v48 |= 2;
                }
                else if (!g_41eda0 && (char)sub_414264())
                {
                    v48 |= 2;
                    v35 = 7798788;
                }
            }
        }
        if (!((char)v48 & 2))
        {
            v46->field_c = sub_4140a0();
            if (v46->field_c && v69)
            {
                sub_403aa8();
                goto LABEL_414b91;
            }
        }
        else if (!((char)v48 & 16))
        {
            if (v52)
            {
                if (!(GetVersion() & -0x80000000))
                {
                    sub_409eac();
                    sub_409ee0();
                    v46->field_36 = v52 == GetModuleHandleW(v5);
                }
                else
                {
                    sub_409eac();
                    v46->field_36 = v52 == sub_4052c4(v4);
                }
            }
            if (v46->field_36 && ((char)v48 & 128))
                v79 = sub_411a74();
            else
                v79 = 0;
            if (!v46->field_36 || v79)
            {
                if (!(GetVersion() & -0x80000000) || v46->field_8 < -0x80000000 && (!v52 || (sub_40a6ec(), !(char)sub_4140a0())))
                    v80 = 0;
                else
                    v80 = 1;
                v46->field_c = v80;
                if (v46->field_c)
                {
                    if (v69)
                        sub_403aa8();
                    idx1 = sub_40e970(10, NULL);
                    v37 = idx1;
                }
                else
                {
                    idx1 = sub_4119e8();
                    v37 = idx1;
                }
                *((char *)idx1) = 255;
                *((char *)&idx1[1]) = 37;
                *((void* *)&idx1[2]) = idx1 + 6;
                *((void* *)&idx1[6]) = v46->field_8;
                *((char **)g_41f57c) = &g_4117b4;
                v19 = &v39;
                sub_4115d0(&v39);
                v18 = 4;
                sub_409eac(4);
                v17 = ", ";
                sub_403d40(v39, ", ", v3);
                v81 = sub_403e78(v39, ", ", v3);
                v42 = sub_4113d8(v81, v39);
                v16 = v39;
                if (v42)
                {
                    v81 = 0;
                    v41 = (int *)MapViewOfFile(v42, FILE_MAP_ALL_ACCESS, 0, 0, NULL);
                    if (v41)
                    {
                        *(v41) = v46->field_8;
                        UnmapViewOfFile(v41);
                        v16 = v41;
                    }
                    else
                    {
                        CloseHandle(v42);
                        v42 = NULL;
                        v16 = v42;
                    }
                }
                v79 = v81;
                if (v42 && ((char)sub_411bc4(v79) || (v82 = sub_411dd4(), v79 = v79, sub_411dd4() == v46->field_8 && !((v79 = v79, !(char)sub_411df8())))))
                {
                    if (v46->field_c)
                    {
                        sub_40e878();
                        CloseHandle(v42);
                        v83 = sub_411dd4();
                        if (v83 != v46->field_8)
                        {
                            sub_411e50();
                            sub_412214();
                        }
                    }
                    if (v46->field_36)
                    {
                        if (!(GetVersion() & -0x80000000))
                        {
                            sub_409eac();
                            sub_409ee0();
                            LoadLibraryW(v2);
                        }
                        else
                        {
                            sub_409eac();
                            LoadLibraryA(v1);
                        }
                    }
                    v84 = _ccall(v59, v60, (unsigned int)v61, 0);
                    v85 = *((int *)v84);
                    v15 = *((int *)v84);
                    v86 = _ccall(v59, v60, (unsigned int)v61, 0);
                    *((unsigned int **)v86) = &v15;
                    sub_411dac(v85, sub_414ac8, &v47);
                    v87 = _ccall(v59, v60, (unsigned int)v61, 0);
                    *((unsigned int *)v87) = v85;
                    v33 = 1;
                    v35 = 0;
LABEL_414b91:
                    if (!v46->field_c || !((char)v48 & 4))
                        v88 = 0;
                    else
                        v88 = 1;
                    v46->field_24 = v88;
                    if (!v88)
                    {
LABEL_414d7e:
                        v41 = NULL;
                        v15 = &v47;
                        v14 = sub_4152c6;
                        v103 = _ccall(v59, v60, (unsigned int)v61, 0);
                        v13 = *((int *)v103);
                        v104 = _ccall(v59, v60, (unsigned int)v61, 0);
                        *((unsigned int **)v104) = &v13;
                        if (v46->field_5)
                        {
                            if (v46->field_c)
                            {
                                v46->field_38 = sub_40e970(0x22, NULL);
                            }
                            else
                            {
                                if ((GetVersion() & -0x80000000))
                                    v46->field_38 = sub_40536c(0x40, 0x22);
                                else
                                    v46->field_38 = sub_4119e8();
                            }
                            v105 = idx1;
                            iter = v46->field_38;
                            do
                            {
                                sub_40c63c();
                                if (*((char *)((void*)&v29 + 3)))
                                {
                                    if (&v69 == 1)
                                    {
                                        if (*((unsigned short *)((void*)&v28 + 2)) != 235)
                                        {
                                            *((char *)iter) = 15;
                                            *((char *)&iter[1]) = (*((char *)((void*)&v28 + 2)) & 15) + 128;
                                            iter += 6;
                                        }
                                        else
                                        {
                                            *((char *)iter) = 233;
                                            iter += 5;
                                        }
                                    }
                                    else
                                    {
                                        if (&v69 == 2)
                                        {
                                            sub_402628();
                                            iter = v31 - v105 + iter + 1;
                                        }
                                        else
                                        {
                                            sub_402628();
                                            iter += v31 - v105;
                                        }
                                    }
                                    *((unsigned long *)&iter[4]) = v40 - iter;
                                }
                                else
                                {
                                    sub_402628();
                                    iter += v31 - v105;
                                }
                            } while ((v105 = v31, v105 - idx1 < 6));
                            *((char *)iter) = 233;
                            *((unsigned long *)&iter[1]) = v105 - (iter + 5);
                            sub_409eac(4);
                            sub_403d40(v40, ", ", v0);
                            v42 = sub_4113d8(sub_403e78(v40, ", ", v0), v40);
                            if (v42)
                            {
                                if (v46->field_c)
                                    sub_40e878();
                                v41 = (void* *)MapViewOfFile(v42, FILE_MAP_ALL_ACCESS, 0, 0, NULL);
                                if (v41)
                                {
                                    if (v46->field_c)
                                        *(v41) = sub_40e970(92, NULL);
                                    else
                                        *(v41) = sub_4119e8();
                                    index = *(v41);
                                    index->field_0 = 2;
                                    index->field_4 = 8;
                                    *((void* *)&index->padding_c[0]) = idx1;
                                    v108 = *((int *)&index->padding_c[0]);
                                    *((int *)&index->padding_c[4]) = *((int *)v108);
                                    *((short *)&index->padding_c[8]) = *((short *)(v108 + 4));
                                    index->field_16 = 255;
                                    index->field_17 = 37;
                                    index[1].field_0 = v46->field_38 + 30;
                                    *((void* *)index[1].field_0) = v46->field_38;
                                    if (!v46->field_c && !v33)
                                        index->field_8 = v42;
                                    else
                                        index->field_8 = 0;
                                    index[1].field_4 = 0;
                                    index[1].field_8 = v46->field_38 + 30;
                                    *((void* *)&index[1].padding_c[0]) = v46->field_38;
                                    *((unsigned int *)&index[1].padding_c[4]) = 0;
                                }
                            }
                        }
                        else
                        {
                            v41 = (void* *)MapViewOfFile(v42, FILE_MAP_ALL_ACCESS, 0, 0, NULL);
                            v109 = *(v41);
                            v46->field_38 = *((int *)&v109->padding_c[8 + 8 * v109->field_0]);
                            if (v109->field_4 == v109->field_0)
                            {
                                v111 = (!v46->field_c ? sub_4119e8() : sub_40e970(v109->field_4 * 16 + 28, NULL));
                                sub_402628();
                                v111->field_4 = v109->field_4 * 2;
                                v38 = *(v41);
                                *(v41) = v111;
                                if (v46->field_c)
                                    sub_40ea58(*(v41), NULL);
                                else
                                    sub_4053fc(*(v41), 0, 0x8000);
                            }
                        }
                        if (!v46->field_24)
                        {
                            if (!((char)v48 & 1))
                            {
                                v46->field_28 = v46->field_20 + 10;
                                j = 0;
                                do
                                {
                                    idx2 = v46->field_28 + j * 14;
                                    idx2->field_0 = 104;
                                    *((unsigned int *)&(&idx2->field_0)[1]) = 0;
                                    *((char *)&idx2->field_1 + 1) = 240;
                                    *((unsigned short *)((char *)&idx2->field_1 + 2)) = 9603;
                                    *((struct_10 **)&idx2->field_5) = &(&idx2->field_0)[1];
                                    *((char *)&idx2->field_8) = 0;
                                    *((char *)&idx2->field_8 + 1) = 195;
                                    j += 1;
                                } while (j != 280);
                                v114 = v46->field_28 + 3920;
                                sub_402628();
                                v115 = sub_4093d8(2147483647, 0, 0, v34);
                                *((unsigned int *)(v115 + v114)) = v46->field_28;
                                v8 = 2147483647;
                                v116 = sub_4093d8(2147483647, 0, 0, v34);
                                *((int *)(v116 + v114)) = v46->field_10 - v114 - v34;
                                v46->field_10 = v114;
                            }
                            if (v46->field_c)
                            {
                                v46->field_1c = sub_40e970(0x22, NULL);
                                node = v46->field_1c;
                                k = &g_41f0c8;
                                for (v119 = 8; v119; k += 4)
                                {
                                    v119 -= 1;
                                    *((int *)node) = *((int *)k);
                                    node += 4;
                                }
                                *((short *)node) = *((short *)k);
                                v120 = sub_40d994();
                                *((void* *)&v46->field_1c[2]) = v120 - (v46->field_1c + 6);
                                ch = GetCurrentProcessId();
                                v122 = v46->field_1c;
                                *((unsigned int *)&v122[7]) = ch;
                                *((void* *)&v122[16]) = v122 + 20;
                                *((int *)&v122[20]) = v46->field_10;
                                *((void* *)&v122[26]) = v122 + 30;
                                *((void* *)&v46->field_20[2]) = v122 + 30;
                                v7 = v46->field_1c;
                                ch1 = GetCurrentProcessId();
                                GetCurrentProcess();
                                sub_41360c();
                            }
                        }
                        v46->field_14->field_0 = v46->field_20;
                        v123 = *(v41);
                        v46->field_3c = *((int *)&v123->padding_c[0]);
                        v124 = v46;
                        v124->field_40 = *((int *)&v123->field_16);
                        v124->field_44 = *((short *)((char *)&v123[1].field_0 + 2));
                        v125 = v46;
                        *((int *)&(&v125->field_44)[1]) = *((int *)&v123->padding_c[4]);
                        *((short *)((char *)&v125->field_46 + 2)) = *((short *)&v123->padding_c[8]);
                        v126 = v123->field_0;
                        (&v123[1].field_4)[2 * v126] = *((int *)&v123->padding_c[8 + 8 * v126]);
                        (&v123[1].field_8)[2 * v126] = (&v123[1].field_0)[2 * v126];
                        if (v46->field_c && !v46->field_24)
                            *((void* *)&v123->padding_c[8 + 8 * v123->field_0]) = v46->field_1c;
                        else
                            *((int *)&v123->padding_c[8 + 8 * v123->field_0]) = v46->field_10;
                        (&v123[1].field_0)[2 * v123->field_0] = (int)v46->field_20[2];
                        *((unsigned int *)(&v123[1].field_0)[2 * v123->field_0]) = (&v123[1].field_4)[2 * v123->field_0];
                        *((int *)*((int *)&v123->padding_c[4 + 8 * v123->field_0])) = *((int *)&v123->padding_c[8 + 8 * v123->field_0]);
                        v123->field_0 = v123->field_0 + 1;
                        v46->padding_0[4] = 1;
                        sub_4159cc();
                        v127 = _ccall(v59, v60, (unsigned int)v61, 0);
                        *((unsigned int *)v127) = v8;
                        v9 = sub_4152cd;
                        sub_4152b6();
                        return;
                    }
                    else if (v46->field_10 < -0x80000000)
                    {
                        v46->field_10 = sub_40ecb8(&v20, (struct struct_7 *)&v46->field_18);
                        if (!v46->field_10)
                        {
                            v35 = 7798787;
                            sub_40351c(&v20, &v46->field_18);
                            sub_40351c(v79, v16);
                            sub_40351c(v17, v3);
                            sub_40351c(v18, v19);
                        }
                        else
                        {
                            v89 = sub_404654();
                            if (v89 >= 0)
                            {
                                v90 = v89 + 1;
                                v91 = 0;
                                do
                                {
                                    v92 = v90;
                                    v93 = 4294967295 + v91 * 28;
                                    if (!v93[1].padding_0[4] && *((int *)&v93[2].padding_0[0]) && *((int *)*((int *)&v93[2].padding_0[0])) == v46->field_14)
                                    {
                                        v15 = 0;
                                        v14 = *((int *)&v93[2].padding_0[0]);
                                        v13 = 0;
                                        v12 = &v47;
                                        v12 = &v47 - v46->field_18;
                                        v13 = v13 - 0 - (&v47 < v46->field_18);
                                        v94 = &v47 - v46->field_18;
                                        v14 -= v94;
                                        v15 = -(v13) - (v14 < v94);
                                        v36 = v14;
                                        if (v46->field_24 || (char)sub_40ec20())
                                            *(v36) = v46->field_18 + v21;
                                    }
                                } while ((v91 += 1, v95 = (int)(v92 - 1), v90 = (int)(v92 - 1), v92 != 1));
                            }
                            *((void* *)&v46->field_20[2]) = v46->field_18 + v21;
                            goto LABEL_414d7e;
                        }
                    }
                    else
                    {
                        sub_40d8e0();
                        if (!(char)v77)
                        {
                            v35 = 7798787;
                            sub_40351c(v79, v16);
                            sub_40351c(v17, v3);
                            sub_40351c(v18, v19);
                            sub_40351c(v77, sub_4152fc);
                        }
                        else
                        {
                            v97 = sub_404654();
                            if (v97 >= 0)
                            {
                                v98 = v97 + 1;
                                v99 = 0;
                                do
                                {
                                    v100 = v98;
                                    v101 = 4294967295 + v99 * 28;
                                    if (!v101[1].padding_0[4] && *((int *)&v101[2].padding_0[0]) && *((int *)*((int *)&v101[2].padding_0[0])) == v46->field_14)
                                    {
                                        if (!v46->field_18)
                                        {
                                            v46->field_18 = sub_40e970(4, NULL);
                                            *((void* *)&v46->field_20[2]) = v46->field_18;
                                        }
                                        *((void* *)*((int *)&v101[2].padding_0[0])) = v46->field_18;
                                    }
                                } while ((v99 += 1, v102 = (int)(v100 - 1), v98 = (int)(v100 - 1), v100 != 1));
                            }
                            goto LABEL_414d7e;
                        }
                    }
                }
                else
                {
                    if (v42)
                        CloseHandle(v42);
                    if (v46->field_c)
                        sub_40ea58(idx1, NULL);
                    else
                        sub_4053fc(idx1, 0, 0x8000);
                    if (!v35)
                        v35 = 7798786;
                    sub_40351c(v79, v16);
                    sub_40351c(", ", v3);
                    sub_40351c(4, &v39);
                    sub_40351c(v77, sub_4152fc);
                }
            }
            else
            {
                v35 = 7798786;
                sub_40351c(v77, sub_4152fc);
                sub_40351c(&v47, v21);
                sub_40351c(v22, v23);
                sub_40351c(", ", v8);
            }
        }
        else
        {
            v35 = 7798786;
            sub_40351c(v77, sub_4152fc);
            sub_40351c(&v47, v21);
            sub_40351c(v22, v23);
            sub_40351c(", ", v8);
        }
    }
    v96 = _ccall(v59, v60, (unsigned int)v61, 0);
    *((char **)v96) = &v47;
    v22 = sub_4153dc;
    sub_415399();
    return;
}
```

## `sub_00414ac8` `0x00414ac8`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
    char padding_8[4];
    void* field_c;
    char padding_10[4];
    void* field_14;
    void* field_18;
} struct_1;

unsigned int sub_414ac8(int a0)
{
    struct_1 *v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x8]

    return sub_4030c0(v0, a0, v1);
}
```

## `sub_00414acd` `0x00414acd`

_5 bytes. (leaf/helper — see body)_

```c
void sub_414acd(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int *a10)
{
    unsigned int v0;  // [bp+0x0]

    sub_4034ec(v0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10);
}
```

## `sub_004152b6` `0x004152b6`

_16 bytes. (leaf/helper — see body)_

```c
int sub_4152b6(void)
{
    int v2;  // eax
    unsigned int v1;  // [bp+0xfffec]

    if (v1)
        v2 = UnmapViewOfFile(v1);
    return v2;
}
```

## `sub_004152c6` `0x004152c6`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4152c6(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004152cb` `0x004152cb`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4152cb(void)
{
    return sub_4152b6();
}
```

## `sub_004152cd` `0x004152cd`

_13 bytes. (leaf/helper — see body)_

```c
int sub_4152cd(unsigned int a0, unsigned int a1)
{
    unsigned long v1;  // ldt
    unsigned long v2;  // gdt
    unsigned short v3;  // fs
    unsigned long v4;  // 4118
    unsigned int v0;  // [bp+0x0]

    v4 = _ccall(v1, v2, (unsigned int)v3, 0);
    *((unsigned int *)v4) = v0;
    a1 = sub_415303;
    return sub_4152da();
}
```

## `sub_004152da` `0x004152da`

_34 bytes. (leaf/helper — see body)_

```c
char [13] sub_4152da(void)
{
    char v3[13];  // eax
    HANDLE v1;  // [bp+0xffff0]
    char v2[13];  // [bp+0x100000]

    if (!v1)
        return v3;
    if (!v2[5] || v2[12])
        return CloseHandle(v1);
    return v2;
    return CloseHandle(v1);
}
```

## `sub_004152fc` `0x004152fc`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4152fc(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00415301` `0x00415301`

_2 bytes. (leaf/helper — see body)_

```c
char [13] sub_415301(void)
{
    return sub_4152da();
}
```

## `sub_00415303` `0x00415303`

_13 bytes. (leaf/helper — see body)_

```c
int sub_415303(unsigned int a0, unsigned int a1)
{
    unsigned long v1;  // ldt
    unsigned long v2;  // gdt
    unsigned short v3;  // fs
    unsigned long v4;  // 4118
    unsigned int v0;  // [bp+0x0]

    v4 = _ccall(v1, v2, (unsigned int)v3, 0);
    *((unsigned int *)v4) = v0;
    a1 = sub_415336;
    return sub_415310();
}
```

## `sub_00415310` `0x00415310`

_31 bytes. (leaf/helper — see body)_

```c
int sub_415310(void)
{
    int v3;  // eax
    HANDLE v1;  // [bp+0xffff4]
    HANDLE v2;  // [bp+0xffff8]

    if (v2)
        v3 = ReleaseMutex(v2);
    if (v1)
        v3 = ReleaseMutex(v1);
    return v3;
}
```

## `sub_0041532f` `0x0041532f`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_41532f(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00415334` `0x00415334`

_2 bytes. (leaf/helper — see body)_

```c
int sub_415334(void)
{
    return sub_415310();
}
```

## `sub_00415336` `0x00415336`

_13 bytes. (leaf/helper — see body)_

```c
int sub_415336(unsigned int a0, unsigned int a1)
{
    unsigned long v1;  // ldt
    unsigned long v2;  // gdt
    unsigned short v3;  // fs
    unsigned long v4;  // 4118
    unsigned int v0;  // [bp+0x0]

    v4 = _ccall(v1, v2, (unsigned int)v3, 0);
    *((unsigned int *)v4) = v0;
    a1 = sub_415369;
    return sub_415343();
}
```

## `sub_00415343` `0x00415343`

_31 bytes. (leaf/helper — see body)_

```c
int sub_415343(void)
{
    int v3;  // eax
    HANDLE v1;  // [bp+0xffff4]
    HANDLE v2;  // [bp+0xffff8]

    if (v2)
        v3 = CloseHandle(v2);
    if (v1)
        v3 = CloseHandle(v1);
    return v3;
}
```

## `sub_00415362` `0x00415362`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_415362(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00415367` `0x00415367`

_2 bytes. (leaf/helper — see body)_

```c
int sub_415367(void)
{
    return sub_415343();
}
```

## `sub_00415369` `0x00415369`

_13 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_41538c;

int sub_415369(unsigned int a0, unsigned int a1)
{
    unsigned long v1;  // ldt
    unsigned long v2;  // gdt
    unsigned short v3;  // fs
    unsigned long v4;  // 4118
    unsigned int v0;  // [bp+0x0]

    v4 = _ccall(v1, v2, (unsigned int)v3, 0);
    *((unsigned int *)v4) = v0;
    a1 = &g_41538c;
    return sub_415376();
}
```

## `sub_00415376` `0x00415376`

_15 bytes. (leaf/helper — see body)_

```c
void sub_415376(void)
{
    enum WIN32_ERROR v1;  // [bp+0xfffcc]

    sub_4123c0();
    SetLastError(v1);
    return;
}
```

## `sub_00415385` `0x00415385`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_415385(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041538a` `0x0041538a`

_2 bytes. (leaf/helper — see body)_

```c
void sub_41538a(void)
{
    sub_415376();
    return;
}
```

## `sub_00415399` `0x00415399`

_60 bytes. (leaf/helper — see body)_

```c
int sub_415399(void)
{
    sub_403a34();
    sub_404124();
    sub_403a34();
    return sub_403a10();
}
```

## `sub_004153d5` `0x004153d5`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4153d5(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004153da` `0x004153da`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4153da(void)
{
    return sub_415399();
}
```

## `sub_004153dc` `0x004153dc`

_36 bytes. (leaf/helper — see body)_

```c
int sub_4153dc(unsigned int a0, unsigned int a1)
{
    unsigned long v3;  // ldt
    unsigned long v4;  // gdt
    unsigned short v5;  // fs
    unsigned long v6;  // 4109
    unsigned int v0;  // [bp+0x0]
    char v1;  // [bp+0xfffff]
    unsigned int v2;  // [bp+0x100000]

    if (v1)
    {
        sub_402f9c();
        v6 = _ccall(v3, v4, (unsigned int)v5, 0);
        *((unsigned int *)v6) = v0;
    }
    return v2;
}
```

## `sub_0041541c` `0x0041541c`

_526 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    unsigned int field_0;
    int field_4;
    char padding_8[60];
    unsigned int field_44;
} struct_2;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern char g_400000;
extern unsigned int g_41562e;
extern struct_0 *g_41f0ec;
extern struct_0 *g_41f0f4;
extern char g_41f0f8;

int sub_41541c(void)
{
    unsigned int i;  // ecx
    unsigned int v15;  // ecx
    int v24;  // ebx
    unsigned long v25;  // 4157
    unsigned long v26;  // 4161
    unsigned int v27;  // eax
    struct_2 *v28;  // ebx
    unsigned int ch;  // eax
    unsigned int v30;  // esi
    int v31;  // esi
    unsigned int v32;  // edi
    int j;  // esi
    unsigned long v16;  // ldt
    int idx;  // eax
    unsigned int *v35;  // eax
    unsigned int v36;  // esi
    unsigned long v37;  // 4118
    unsigned long v38;  // 4118
    unsigned long v17;  // gdt
    unsigned short v18;  // fs
    unsigned long v19;  // 4145
    unsigned int v20;  // 4112
    unsigned long v21;  // 4154
    int v22;  // edi
    int v23;  // esi
    int v0;  // [bp-0x90]
    unsigned int v1;  // [bp-0x7c]
    unsigned int v2;  // [bp-0x74]
    unsigned int v3;  // [bp-0x4c]
    unsigned int v4;  // [bp-0x48]
    char *v5;  // [bp-0x44]
    unsigned int v6;  // [bp-0x30]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x18]
    unsigned int v9;  // [bp-0x14]
    struct_2 *v10;  // [bp-0x10], Other Possible Types: unsigned int
    unsigned int v11;  // [bp-0xc]
    char v12;  // [bp-0x4]

    i = 6;
    do
    {
        v10 = 0;
        v9 = 0;
        i -= 1;
    } while (i != 1);
    v19 = _ccall(v16, v17, (unsigned int)v18, 0);
    v20 = *((int *)v19);
    v6 = *((int *)v19);
    v21 = _ccall(v16, v17, (unsigned int)v18, 0);
    *((unsigned int **)v21) = &v6;
    sub_404814(v20, sub_41564a, &v12, v22, v23, v24, v15);
    if (!g_41f0ec)
        g_41f0ec = sub_40da7c();
    if (!g_41f0f4)
        g_41f0f4 = sub_40da7c();
    if (g_41f0ec && g_41f0f4)
    {
        v11 = 0;
        g_41f0ec(5, 0, 0, &v11);
        v10 = NULL;
        v5 = &v12;
        v4 = sub_415627;
        v25 = _ccall(v16, v17, (unsigned int)v18, 0);
        v3 = *((int *)v25);
        v26 = _ccall(v16, v17, (unsigned int)v18, 0);
        *((unsigned int **)v26) = &v3;
        if (!v11)
        {
            v11 = 0x10000;
            do
            {
                v11 *= 2;
                LocalFree(v10);
                v10 = sub_40536c(0x40, v11);
                v27 = g_41f0ec(5, v10, v11, 0);
            } while (v27 && v11 != &g_400000);
        }
        else
        {
            v11 *= 2;
            v10 = sub_40536c(0x40, v11);
            v27 = g_41f0ec(5, v10, v11, 0);
        }
        if (!v27)
        {
            v28 = v10;
            while (true)
            {
                ch = GetCurrentProcessId();
                if (ch == v28->field_44)
                {
                    v30 = v28->field_4 - 1;
                    if (v30 >= NULL)
                    {
                        v31 = v30 + 1;
                        v32 = 0;
                        do
                        {
                            j = v31;
                            sub_40a0d8();
                            v11 = (*((char *)((void*)&&v12 + 3)) <= 8 ? *((int *)&(&v28->field_0)[16 * v32 + 43]) : (&v28[3].field_4)[16 * v32]);
                            v11 = v11;
                            if (GetCurrentThreadId() != v11)
                            {
                                v8 = 0;
                                v9 = v11;
                                if (!g_41f0f4(&v11, 0x1f03ff, &g_41f0f8, &v8))
                                {
                                    v0 = sub_40464c() + 1;
                                    sub_404808();
                                    idx = sub_404654();
                                    *((unsigned int *)(*(v35) + idx * 4)) = v11;
                                }
                            }
                            v32 += 1;
                            v36 = j - 1;
                            v31 = v36;
                        } while (j != 1);
                    }
                }
                if (!v28->field_0)
                    break;
                v28 = v28->field_0 + (char *)v28;
            }
        }
        v37 = _ccall(v16, v17, (unsigned int)v18, 0);
        *((unsigned int *)v37) = v1;
        v2 = &g_41562e;
        sub_41561d();
        return;
    }
    v38 = _ccall(v16, v17, (unsigned int)v18, 0);
    *((unsigned int *)v38) = v20;
    v7 = sub_415651;
    sub_41563b();
    return;
}
```

## `sub_0041561d` `0x0041561d`

_10 bytes. (leaf/helper — see body)_

```c
HLOCAL sub_41561d(void)
{
    HLOCAL v1;  // [bp+0xffff8]

    return LocalFree(v1);
}
```

## `sub_00415627` `0x00415627`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_415627(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041562c` `0x0041562c`

_2 bytes. (leaf/helper — see body)_

```c
HLOCAL sub_41562c(void)
{
    return sub_41561d();
}
```

## `sub_0041563b` `0x0041563b`

_15 bytes. (leaf/helper — see body)_

```c
int sub_41563b(void)
{
    return sub_4040f0();
}
```

## `sub_0041564a` `0x0041564a`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_41564a(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041564f` `0x0041564f`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41564f(void)
{
    return sub_41563b();
}
```

## `sub_00415651` `0x00415651`

_7 bytes. (leaf/helper — see body)_

```c
void sub_415651(unsigned int a0, unsigned int a1)
{
    return;
}
```

## `sub_00415658` `0x00415658`

_70 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_41f0f0;

int sub_415658(void)
{
    unsigned int v5;  // ebx
    unsigned int v6;  // esi
    unsigned int v7;  // edx
    unsigned int v8;  // eax
    HANDLE ch;  // eax
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    unsigned int v3;  // [bp-0x4]

    v3 = v5;
    v2 = v6;
    if ((GetVersion() & 0x80000000))
        return;
    if (!g_41f0f0)
        g_41f0f0 = sub_40d994();
    if (!g_41f0f0)
        return;
    v1 = v7;
    v0 = v8;
    ch = GetCurrentProcess();
    g_41f0f0(ch);
    return;
}
```

## `sub_0041569e` `0x0041569e`

_83 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    struct struct_2 *field_0;
    struct struct_0 *field_4;
} struct_1;

typedef struct struct_2 {
    unsigned int field_0;
    char padding_4[16];
    unsigned int field_14;
    unsigned int field_18;
} struct_2;

typedef struct struct_0 {
    char padding_0[184];
    unsigned int field_b8;
} struct_0;

extern char g_420afc;
extern unsigned int g_420b00;

unsigned int sub_41569e(struct_1 *a0)
{
    unsigned int v0[7];  // edx

    if (a0->field_4->field_b8 == *((int *)&g_420afc) && (a0->field_0->field_0 == 3221225622 || !((v0 = (unsigned int [7])a0->field_0, v0[0] != 3221225477 || v0[5] || v0[6] != 4294967295))))
    {
        a0->field_4->field_b8 = g_420b00;
        return 4294967295;
    }
    return 0;
}
```

## `sub_004156f1` `0x004156f1`

_82 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[184];
    unsigned int field_b8;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern char g_420afc;
extern unsigned int g_420b00;
extern struct_1 *g_420b04;

unsigned int sub_4156f1(unsigned int *a0, struct_0 *a1)
{
    if (a1->field_b8 == *((int *)&g_420afc) && (*(a0) == 3221225622 || *(a0) == 3221225477 && !a0[5] && a0[6] == 4294967295))
    {
        a1->field_b8 = g_420b00;
        return 4294967295;
    }
    return g_420b04(a0, a1);
}
```

## `sub_00415743` `0x00415743`

_1 bytes. (leaf/helper — see body)_

```c
int sub_415743(void)
{
    sub_415744();
    return;
}
```

## `sub_00415744` `0x00415744`

_473 bytes. calls VirtualProtect_

```c
typedef struct struct_1 {
    unsigned int field_0;
    char field_4[4];
    char field_7;
    char field_8;
    char field_9;
    unsigned int field_a;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern char g_4156a0;
extern char g_4156f4;
extern unsigned int g_420afc;
extern unsigned int g_420b00;
extern unsigned int g_420b04;
extern struct_0 *g_420b08;
extern unsigned int g_420b0c;

int sub_415744(void)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned int v18;  // eax
    unsigned int v19;  // edx
    struct_1 *v20;  // esi
    struct_1 *v21;  // eax
    unsigned long v22;  // 4118
    unsigned short v10;  // fs
    unsigned long v11;  // 4168
    unsigned int v12;  // 4122
    unsigned long v13;  // 4177
    char v14;  // bl
    int v15;  // edi
    int v16;  // esi
    int v17;  // ebx
    enum PAGE_PROTECTION_FLAGS v0;  // [bp-0x48], Other Possible Types: enum PAGE_PROTECTION_FLAGS[2]
    unsigned int v1;  // [bp-0x40]
    unsigned int v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x14]
    enum PAGE_PROTECTION_FLAGS v4[2];  // [bp-0x8]
    char v5;  // [bp-0x4]
    char v6;  // [bp+0x0]
    void* v7;  // [bp+0x4]

    v3 = 0;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v12 = *((int *)v11);
    v2 = *((int *)v11);
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v13) = &v2;
    v14 = 0;
    g_420b08 = sub_40d994(v12, sub_41592b, &v5, v15, v16, v17, 0, 0, 0, 0, &v6);
    g_420b0c = sub_40d994(v12, sub_41592b, &v5, v15, v16, v17, 0, 0, 0, 0, &v6);
    sub_403f60();
    *((char *)sub_403ed0()) = 114;
    *((char *)(sub_403ed0() + 1)) = 100;
    *((char *)(sub_403ed0() + 2)) = 101;
    *((char *)(sub_403ed0() + 3)) = 99;
    *((char *)(sub_403ed0() + 4)) = 32;
    sub_409eac();
    GetCurrentProcessId();
    sub_409b54(&v3, 0, ", ", 0);
    sub_403d40(0);
    v0 = 0;
    *((HANDLE *)&v7[4]) = sub_4051ac(NULL, 0, sub_403e78(NULL));
    if ((int)v7[4])
    {
        v0 = (enum PAGE_PROTECTION_FLAGS)(int)v7[4];
        WaitForSingleObject((int)v7[4], 4294967295);
        g_420afc = v18;
        g_420b00 = v19;
        if (!g_420b08 || !g_420b0c)
        {
            v20 = sub_40da7c();
            if (v20->field_0 == 69487755)
            {
                v0 = (enum PAGE_PROTECTION_FLAGS[2])v0;
                if ((unsigned int)v20->field_4 == 2366603)
                {
                    v0 = (enum PAGE_PROTECTION_FLAGS[2])v0;
                    if (v20->field_4[3] == 81)
                    {
                        v0 = (enum PAGE_PROTECTION_FLAGS[2])v0;
                        if (v20->field_7 == 83)
                        {
                            v0 = (enum PAGE_PROTECTION_FLAGS[2])v0;
                            if (v20->field_8 == 232)
                            {
                                v0 = 64;
                                v0 = v0;
                                if (VirtualProtect(&v20->field_9, 0x4, PAGE_EXECUTE_READWRITE, v4))
                                {
                                    v21 = &v20->field_9;
                                    g_420b04 = 2 + (char *)&v20->field_a + v21->field_0;
                                    v21->field_0 = &g_4156f4 - v20 - 14;
                                    VirtualProtect(v21, 0x4, v4, v4);
                                    v14 = 1;
                                    v0 = v4;
                                }
                            }
                        }
                    }
                }
            }
        }
        else
        {
            v0 = 1;
            v14 = g_420b08(1, &g_4156a0);
        }
        if (!v14)
        {
            ReleaseMutex((int)v7[4]);
            CloseHandle((int)v7[4]);
        }
    }
    v22 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((enum PAGE_PROTECTION_FLAGS [2])v22) = v0;
    v1 = sub_415932;
    sub_41591d();
    return;
}
```

## `sub_0041591d` `0x0041591d`

_14 bytes. (leaf/helper — see body)_

```c
int sub_41591d(void)
{
    return sub_403a34();
}
```

## `sub_0041592b` `0x0041592b`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_41592b(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00415930` `0x00415930`

_2 bytes. (leaf/helper — see body)_

```c
int sub_415930(void)
{
    return sub_41591d();
}
```

## `sub_00415932` `0x00415932`

_9 bytes. (leaf/helper — see body)_

```c
int sub_415932(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // ebx

    return v0;
}
```

## `sub_00415948` `0x00415948`

_129 bytes. calls VirtualProtect_

```c
typedef struct struct_1 {
    char padding_0[10];
    unsigned int field_a;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern char g_4156a0;
extern unsigned int g_420b04;
extern unsigned int g_420b08;
extern struct_0 *g_420b0c;

int sub_415948(int a0, unsigned int a1, void* a2)
{
    int v2;  // esi
    int v3;  // ebx
    struct_1 *v4;  // ebx
    struct_1 *v5;  // esi
    enum PAGE_PROTECTION_FLAGS v0[2];  // [bp-0x8]
    char v1;  // [bp+0x0]

    if (g_420b08 && g_420b0c)
        return g_420b0c(&g_4156a0);
    v4 = sub_40da7c(v2, v3, a0, &v1);
    v5 = (v4->padding_0)[1];
    if (VirtualProtect(v5, 0x4, PAGE_EXECUTE_READWRITE, v0))
    {
        *((struct_1 **)&v5->padding_0[0]) = -14 + g_420b04 - (char *)v4;
        VirtualProtect(v5, 0x4, v0, v0);
    }
    ReleaseMutex((int)a2[4]);
    return CloseHandle((int)a2[4]);
}
```

## `sub_004159c9` `0x004159c9`

_3 bytes. (leaf/helper — see body)_

```c
int sub_4159c9(void)
{
    sub_4159cc();
    return;
}
```

## `sub_004159cc` `0x004159cc`

_1077 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[12];
    void* field_c;
    char padding_10[10];
    unsigned short field_1a;
} struct_1;

extern unsigned int g_415da0;
extern unsigned int g_415dbe;

int sub_4159cc(void)
{
    unsigned int v18;  // eax
    unsigned long v19;  // ldt
    unsigned long v28;  // 4128
    unsigned long v29;  // 4137
    unsigned long v30;  // 4127
    unsigned int v31;  // 4103
    unsigned long v32;  // 4136
    unsigned long v33;  // 4134
    unsigned long v34;  // 4143
    unsigned long v35;  // 4163
    unsigned int v36;  // 4103
    unsigned long v37;  // 4167
    unsigned long v20;  // gdt
    struct_1 *idx;  // esi
    char v39;  // al
    int v40;  // eax
    unsigned int v41;  // edi
    void* v42;  // eax
    void* v43;  // ebx
    int v44;  // eax
    unsigned int v45;  // edi
    int v46;  // ecx
    unsigned int v47;  // edx
    unsigned short v21;  // fs
    unsigned long v48;  // 4118
    unsigned long v49;  // 4118
    unsigned int v51;  // eax
    unsigned long v52;  // 4118
    unsigned long v53;  // 4118
    unsigned long v22;  // 4176
    unsigned int v23;  // 4124
    unsigned long v24;  // 4185
    int v25;  // edi
    int v26;  // esi
    int v27;  // ebx
    unsigned int v1;  // [bp-0x194]
    unsigned int v2;  // [bp-0x18c]
    unsigned int v3;  // [bp-0x188]
    unsigned int v4;  // [bp-0x184]
    char *v5;  // [bp-0x180], Other Possible Types: unsigned int
    unsigned int v6;  // [bp-0x178]
    unsigned int v7;  // [bp-0x170]
    unsigned int v8;  // [bp-0x164]
    unsigned int v9;  // [bp-0x160]
    char *v10;  // [bp-0x15c]
    char v11[45];  // [bp-0x158]
    unsigned int v12;  // [bp-0x150]
    unsigned int v13;  // [bp-0x148]
    unsigned int v14;  // [bp-0x104]
    unsigned int v15;  // [bp-0x100]
    int v16;  // [bp-0xfc]

    *((void* *)&(&v16)[248]) = &v16 - 252;
    *((unsigned int *)&(&v16)[236]) = 0;
    *((unsigned int *)&(&v16)[212]) = 0;
    *((unsigned int *)&(&v16)[240]) = v18;
    v22 = _ccall(v19, v20, (unsigned int)v21, 0);
    v23 = *((int *)v22);
    v13 = *((int *)v22);
    v24 = _ccall(v19, v20, (unsigned int)v21, 0);
    *((unsigned int **)v24) = &v13;
    sub_404814(v23, sub_415e79, &v16 - 248, v25, v26, v27, 0, 0, 0, 0);
    if (*((char *)(*((unsigned int *)(&v16 + 240)) + 4)) && !*((char *)(*((unsigned int *)(&v16 + 240)) + 44)))
    {
        *((unsigned int *)&(&v16)[220]) = 0;
        sub_4115d0(&v16 - 236);
        sub_409eac(&v16 - 236);
        v11 = *((unsigned int *)(&v16 + 236));
        sub_403d40(*((unsigned int *)(&v16 + 236)), ", ", 0);
        *((int *)&(&v16)[232]) = sub_411214(sub_403e78(*((unsigned int *)(&v16 + 236)), ", ", 0));
        if (*((unsigned int *)(&v16 + 232)))
        {
            v10 = &v16 - 248;
            v9 = sub_415e3e;
            v28 = _ccall(v19, v20, (unsigned int)v21, 0);
            v8 = *((int *)v28);
            v29 = _ccall(v19, v20, (unsigned int)v21, 0);
            *((unsigned int **)v29) = &v8;
            WaitForSingleObject(*((unsigned int *)(&v16 + 232)), 4294967295);
            v30 = _ccall(v19, v20, (unsigned int)v21, 0);
            v31 = *((int *)v30);
            v7 = *((int *)v30);
            v32 = _ccall(v19, v20, (unsigned int)v21, 0);
            *((unsigned int **)v32) = &v7;
            sub_409eac(-1, v31, sub_415e20, &v16 - 248);
            v5 = *((unsigned int *)(&v16 + 236));
            sub_403d40(*((unsigned int *)(&v16 + 236)), ", ", 0);
            *((int *)&(&v16)[228]) = sub_4114f0(sub_403e78(*((unsigned int *)(&v16 + 236)), ", ", 0), *((unsigned int *)(&v16 + 236)));
            if (*((unsigned int *)(&v16 + 228)))
            {
                v5 = &v16 - 248;
                v4 = sub_415db7;
                v33 = _ccall(v19, v20, (unsigned int)v21, 0);
                v3 = *((int *)v33);
                v34 = _ccall(v19, v20, (unsigned int)v21, 0);
                *((unsigned int **)v34) = &v3;
                *((struct MEMORY_MAPPED_VIEW_ADDRESS *)&(&v16)[224]) = MapViewOfFile(*((unsigned int *)(&v16 + 228)), FILE_MAP_ALL_ACCESS, 0, 0, NULL);
                if (!*((unsigned int *)(&v16 + 224)))
                {
                    v49 = _ccall(v19, v20, (unsigned int)v21, 0);
                    *((unsigned int *)v49) = v3;
                    v5 = &g_415dbe;
                    sub_415dad();
                    return;
                }
                v35 = _ccall(v19, v20, (unsigned int)v21, 0);
                v36 = *((int *)v35);
                v1 = *((int *)v35);
                v37 = _ccall(v19, v20, (unsigned int)v21, 0);
                *((unsigned int **)v37) = &v1;
                idx = *((int *)*((unsigned int *)(&v16 + 224)));
                if (*((int *)idx->field_c) != *((int *)&idx->padding_10[6]) || (short)idx->field_c[4] != idx->field_1a)
                {
                    *((void* *)&(&v16)[220]) = idx->field_c;
                    *((char *)&(&v16)[219]) = sub_40eb40(v36, sub_415d99, &v16 - 248);
                    if (!*((char *)(&v16 + 219)) || (char)sub_40ec20())
                    {
                        sub_40c63c();
                        if (!*((char *)(*((unsigned int *)(&v16 + 240)) + 52)) || (GetVersion() & 0x80000000) || v15 - v14 >= 6 || !(char)sub_415744(&v16 - 248))
                            v39 = 0;
                        else
                            v39 = 1;
                        *((char *)&(&v16)[218]) = v39;
                        if (*((char *)(&v16 + 218)))
                        {
                            *((char *)&(&v16)[217]) = 244;
                            if (!(char)sub_410f64())
                                *((char *)idx->field_c) = *((char *)(&v16 + 217));
                            sub_415658();
                            sub_41541c();
                            v40 = sub_404654();
                            if (v40 >= 0)
                            {
                                *((unsigned int *)&(&v16)[0xcc]) = v40 + 1;
                                v41 = 0;
                                while (true)
                                {
                                    *((unsigned int *)&v16) = 65537;
                                    if (GetThreadContext(*((int *)(*((unsigned int *)(&v16 + 212)) + v41 * 4)), &v16) && idx->field_c < *((unsigned int *)(&v16 + 184)) && idx->field_c + 6 > *((unsigned int *)(&v16 + 184)))
                                    {
                                        Sleep(10);
                                        v16 = v16;
                                    }
                                    else
                                    {
                                        CloseHandle(*((int *)(*((unsigned int *)(&v16 + 212)) + v41 * 4)));
                                        v41 += 1;
                                        *((unsigned int *)&(&v16)[0xcc]) = *((unsigned int *)(&v16 + 0xcc)) - 1;
                                        if (*((unsigned int *)(&v16 + 0xcc)) == 0x1)
                                            break;
                                    }
                                }
                            }
                        }
                        if (!(char)sub_410f64())
                        {
                            v42 = idx->field_c;
                            *((int *)v42) = *((int *)&idx->padding_10[6]);
                            *((unsigned short *)&v42[4]) = idx->field_1a;
                        }
                        sub_415658();
                        if (*((char *)(&v16 + 218)))
                        {
                            v43 = sub_40da7c();
                            *((void* *)&(&v16)[208]) = v43 + 14 + (int)v43[10];
                            sub_41541c();
                            v44 = sub_404654();
                            if (v44 >= 0)
                            {
                                *((unsigned int *)&(&v16)[0xcc]) = v44 + 1;
                                v45 = 0;
                                while (true)
                                {
                                    *((unsigned int *)&v16) = 65537;
                                    if (GetThreadContext(*((int *)(*((unsigned int *)(&v16 + 212)) + v45 * 4)), &v16) && (idx->field_c == *((unsigned int *)(&v16 + 184)) || v43 <= *((unsigned int *)(&v16 + 184)) && v43 + 10 >= *((unsigned int *)(&v16 + 184)) || (*((unsigned int *)(&v16 + 184)) & 0xffff0000) == (*((unsigned int *)(&v16 + 208)) & 0xffff0000)))
                                    {
                                        Sleep(10);
                                        v16 = v16;
                                    }
                                    else
                                    {
                                        CloseHandle(*((int *)(*((unsigned int *)(&v16 + 212)) + v45 * 4)));
                                        v45 += 1;
                                        *((unsigned int *)&(&v16)[0xcc]) = *((unsigned int *)(&v16 + 0xcc)) - 1;
                                        if (*((unsigned int *)(&v16 + 0xcc)) == 0x1)
                                            break;
                                    }
                                }
                            }
                        }
                        if (*((char *)(&v16 + 219)))
                            sub_40ecb0();
                        if (*((char *)(&v16 + 218)))
                            sub_415948(v46, v47, &v16 - 248);
                    }
                }
                v48 = _ccall(v19, v20, (unsigned int)v21, 0);
                *((unsigned int *)v48) = v36;
                v2 = &g_415da0;
                sub_415d8f();
                return;
            }
            else
            {
                v5 = v5;
                if (*((unsigned int *)(&v16 + 220)))
                {
                    v5 = v5;
                    if (*((int *)(*((unsigned int *)(&v16 + 240)) + 8)) != *((unsigned int *)(&v16 + 220)))
                    {
                        v51 = (!*((char *)(*((unsigned int *)(&v16 + 240)) + 54)) ? 0 : sub_411a74());
                        if (!*((char *)(*((unsigned int *)(&v16 + 240)) + 54)) || (v5 = v5, v51))
                        {
                            sub_411bc4(v51);
                            v5 = v51;
                        }
                    }
                }
                v52 = _ccall(v19, v20, (unsigned int)v21, 0);
                *((unsigned int *)v52) = v5;
                v6 = sub_415e27;
                sub_415e16();
                return;
            }
        }
    }
    v53 = _ccall(v19, v20, (unsigned int)v21, 0);
    *((char *[45])v53) = v11;
    v12 = sub_415e80;
    sub_415e52();
    return;
}
```

## `sub_00415d8f` `0x00415d8f`

_10 bytes. (leaf/helper — see body)_

```c
int sub_415d8f(void)
{
    void* v1;  // [bp+0xfffec]

    return UnmapViewOfFile(v1);
}
```

## `sub_00415d99` `0x00415d99`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_415d99(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00415d9e` `0x00415d9e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_415d9e(void)
{
    return sub_415d8f();
}
```

## `sub_00415dad` `0x00415dad`

_10 bytes. (leaf/helper — see body)_

```c
int sub_415dad(void)
{
    HANDLE v1;  // [bp+0xffff0]

    return CloseHandle(v1);
}
```

## `sub_00415db7` `0x00415db7`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_415db7(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00415dbc` `0x00415dbc`

_2 bytes. (leaf/helper — see body)_

```c
int sub_415dbc(void)
{
    return sub_415dad();
}
```

## `sub_00415e16` `0x00415e16`

_10 bytes. (leaf/helper — see body)_

```c
int sub_415e16(void)
{
    HANDLE v1;  // [bp+0xffff4]

    return ReleaseMutex(v1);
}
```

## `sub_00415e20` `0x00415e20`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_415e20(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00415e25` `0x00415e25`

_2 bytes. (leaf/helper — see body)_

```c
int sub_415e25(void)
{
    return sub_415e16();
}
```

## `sub_00415e27` `0x00415e27`

_13 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_415e45;

int sub_415e27(unsigned int a0, unsigned int a1)
{
    unsigned long v1;  // ldt
    unsigned long v2;  // gdt
    unsigned short v3;  // fs
    unsigned long v4;  // 4118
    unsigned int v0;  // [bp+0x0]

    v4 = _ccall(v1, v2, (unsigned int)v3, 0);
    *((unsigned int *)v4) = v0;
    a1 = &g_415e45;
    return sub_415e34();
}
```

## `sub_00415e34` `0x00415e34`

_10 bytes. (leaf/helper — see body)_

```c
int sub_415e34(void)
{
    HANDLE v1;  // [bp+0xffff4]

    return CloseHandle(v1);
}
```

## `sub_00415e3e` `0x00415e3e`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_415e3e(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00415e43` `0x00415e43`

_2 bytes. (leaf/helper — see body)_

```c
int sub_415e43(void)
{
    return sub_415e34();
}
```

## `sub_00415e52` `0x00415e52`

_39 bytes. (leaf/helper — see body)_

```c
int sub_415e52(void)
{
    sub_403a34();
    sub_404814();
    return sub_403a10();
}
```

