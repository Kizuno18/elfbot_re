# elfbot.dll decompiled — loader 0x00417678..0x00418915

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_00417678` `0x00417678`

_394 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[1];
    void* field_1;
} struct_0;

extern unsigned int g_4177fe;
extern char g_41f110;
extern unsigned int g_420b10;
extern unsigned int g_420b28;

unsigned int sub_417678(void)
{
    int v13;  // ebx
    unsigned long v14;  // ldt
    unsigned long v15;  // gdt
    unsigned short v16;  // fs
    unsigned long v17;  // 4124
    unsigned long v18;  // 4133
    int v19;  // ebx
    unsigned int v20;  // eax
    unsigned long v21;  // 4118
    unsigned int v0;  // [bp-0x64]
    unsigned int v1;  // [bp-0x60]
    unsigned int v2;  // [bp-0x5c]
    char *v3;  // [bp-0x58]
    int v4;  // [bp-0x44]
    unsigned int v5;  // [bp-0x1c]
    enum WIN32_ERROR v6;  // [bp-0x18]
    unsigned short v7;  // [bp-0x12]
    struct_0 *v8;  // [bp-0x10]
    unsigned int v9;  // [bp-0xc]
    char *v10;  // [bp-0x8]
    char v11;  // [bp-0x4]

    v10 = &v11;
    v9 = 0;
    v6 = GetLastError();
    if (!(char)sub_410b90(v13))
    {
        SetLastError(v6);
        return v9;
    }
    if ((char)sub_40ddd8(0) && (char)sub_40ddd8(0))
    {
        if (!(VirtualQuery(v8, &v4, 0x1c) != 0x1c || !(char)sub_40ddd8(0) || v7 != 23117))
        {
            v9 = *((unsigned int *)(&v4 + 4));
        }
        else if (g_41f110)
        {
            sub_40520c(&g_420b10);
            v3 = &v11;
            v2 = sub_4177f1;
            v17 = _ccall(v14, v15, (unsigned int)v16, 0);
            v1 = *((int *)v17);
            v18 = _ccall(v14, v15, (unsigned int)v16, 0);
            *((unsigned int **)v18) = &v1;
            v19 = sub_404654();
            if (v19 >= 0)
            {
                do
                {
                    v20 = *((int *)(g_420b28 + v19 * 40 + 24));
                    if (v20 && *((int *)(v20 + 40)) && *((int *)(v20 + 40)) <= v8 && *((int *)(v20 + 40)) + 3920 > v8)
                    {
                        v0 = 28;
                        if (VirtualQuery(*((int *)(v8->padding_0)[1]), &v4, 0x1c) == 0x1c)
                        {
                            v0 = 0;
                            if ((char)sub_40ddd8(0) && v7 == 23117)
                            {
                                v9 = *((unsigned int *)(&v4 + 4));
                                break;
                            }
                        }
                    }
                } while ((v19 = (int)(v19 - 1), v19 != -1));
            }
            v21 = _ccall(v14, v15, (unsigned int)v16, 0);
            *((unsigned int *)v21) = v0;
            v2 = &g_4177fe;
            return sub_4177e6();
        }
    }
    v5 = 0;
    SetLastError(v6);
    return v9;
}
```

## `sub_004177e6` `0x004177e6`

_11 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420b10;

void sub_4177e6(void)
{
    sub_40534c(&g_420b10);
    return;
}
```

## `sub_004177f1` `0x004177f1`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4177f1(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004177f6` `0x004177f6`

_2 bytes. (leaf/helper — see body)_

```c
void sub_4177f6(void)
{
    sub_4177e6();
    return;
}
```

## `sub_00417814` `0x00417814`

_191 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[1];
    char field_1;
} struct_0;

int sub_417814(void)
{
    int v6;  // edi
    int v7;  // esi
    struct_0 *v16;  // edx
    unsigned int v17;  // cc_op
    unsigned int v18;  // cc_dep1
    unsigned int v19;  // cc_dep2
    unsigned int v20;  // cc_ndep
    unsigned int v21;  // 4103
    unsigned int v22;  // 4109
    unsigned long v23;  // 4118
    int v8;  // ebx
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4123
    unsigned int v13;  // 4103
    unsigned long v14;  // 4132
    enum WIN32_ERROR v15;  // eax
    unsigned int v0;  // [bp-0x34]
    unsigned int v1;  // [bp-0x2c]
    unsigned int v2;  // [bp-0x10]
    struct_0 **v3;  // [bp-0xc]
    char v4;  // [bp-0x4]

    sub_403e68(v6, v7, v8);
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v13 = *((int *)v12);
    v0 = *((int *)v12);
    v14 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v14) = &v0;
    v15 = GetLastError();
    if ((char)sub_410b90(v13, sub_4178dc, &v4))
    {
        v3 = NULL;
        if (!(GetVersion() & 0x80000000) && (v16 || (char)sub_410f9c()))
        {
            v21 = _ccall(v17, v18, v19, v20);
            v22 = _ccall(14, 21, sub_403c80() - 1, 0, v21);
            if (v3)
                LocalFree(v3);
        }
        v2 = 0;
    }
    SetLastError(v15);
    v23 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v23) = v13;
    v1 = sub_4178e3;
    sub_4178d3();
    return;
}
```

## `sub_004178d3` `0x004178d3`

_9 bytes. (leaf/helper — see body)_

```c
int sub_4178d3(void)
{
    return sub_403a10();
}
```

## `sub_004178dc` `0x004178dc`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4178dc(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004178e1` `0x004178e1`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4178e1(void)
{
    return sub_4178d3();
}
```

## `sub_004178e3` `0x004178e3`

_9 bytes. (leaf/helper — see body)_

```c
int sub_4178e3(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // ebx

    return v0;
}
```

## `sub_004178ec` `0x004178ec`

_59 bytes. (leaf/helper — see body)_

```c
int sub_4178ec(void)
{
    unsigned int v4;  // ebx
    unsigned int v5;  // esi
    unsigned int *v6;  // ebx
    unsigned int v7;  // eax
    char v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x8]
    unsigned int v2;  // [bp-0x4]

    v2 = v4;
    v1 = v5;
    v6 = sub_40da7c();
    if (v6 && !v6(v7, 0, &v0, 24, 0))
        return;
    return;
}
```

## `sub_00417927` `0x00417927`

_1 bytes. (leaf/helper — see body)_

```c
int sub_417927(void)
{
    sub_417928();
    return;
}
```

## `sub_00417928` `0x00417928`

_87 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_41f134;
extern char g_41f138;
extern char g_41f13c;

int sub_417928(void)
{
    unsigned int v2;  // ebx
    unsigned int v3;  // eax
    unsigned int v0;  // [bp-0x4]

    v0 = v2;
    if (!g_41f13c)
        return;
    if (!g_41f138)
    {
        g_41f134 = sub_40d994();
        g_41f138 = 1;
    }
    if (!g_41f134)
        return;
    if (!g_41f134(v3, &/* unsupported instruction */))
    {
        return;
    }
    else if (!v3)
    {
        return;
    }
    return;
}
```

## `sub_0041797f` `0x0041797f`

_1 bytes. (leaf/helper — see body)_

```c
int sub_41797f(void)
{
    sub_417980();
    return;
}
```

## `sub_00417980` `0x00417980`

_93 bytes. (leaf/helper — see body)_

```c
int sub_417980(void)
{
    unsigned int v7;  // ebx
    unsigned int v8;  // esi
    unsigned int v9;  // edi
    enum WIN32_ERROR v10;  // eax
    unsigned int *v11;  // esi
    unsigned int v12;  // eax
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    unsigned int v5;  // [bp-0x4]

    v5 = v7;
    v4 = v8;
    v3 = v9;
    v10 = GetLastError();
    v1 = 0;
    if (!(char)sub_410b90(0))
    {
        SetLastError(v10);
        return;
    }
    v11 = sub_40d994();
    if (!v11 || !v11(v12, &v1))
        v0 = 0;
    v2 = 0;
    SetLastError(v10);
    return;
}
```

## `sub_004179dd` `0x004179dd`

_3 bytes. (leaf/helper — see body)_

```c
int sub_4179dd(void)
{
    return sub_4179e0();
}
```

## `sub_004179e0` `0x004179e0`

_11 bytes. (leaf/helper — see body)_

```c
int sub_4179e0(void)
{
    GetCurrentProcessId();
    return sub_417980();
}
```

## `sub_004179eb` `0x004179eb`

_1 bytes. (leaf/helper — see body)_

```c
int sub_4179eb(void)
{
    sub_4179ec();
    return;
}
```

## `sub_004179ec` `0x004179ec`

_183 bytes. (leaf/helper — see body)_

```c
int sub_4179ec(void)
{
    int v7;  // esi
    int v8;  // ebx
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4123
    unsigned long v13;  // 4132
    PSID v14;  // edx
    unsigned long v15;  // 4118
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    char *v2;  // [bp-0x1c], Other Possible Types: unsigned int
    PSID *v3;  // [bp-0x10]
    unsigned int *v4;  // [bp-0xc]
    char v5;  // [bp-0x4]

    sub_403e68(v7, v8);
    v2 = &v5;
    v1 = sub_417aac;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v0 = *((int *)v12);
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v0;
    v4 = NULL;
    if (!(GetVersion() & 0x80000000) && (v14 || (char)sub_410f9c()))
    {
        GetCurrentProcess();
        if ((char)sub_410f9c())
        {
            if (v14)
                EqualSid(v14, *(v3));
            else
                EqualSid(*(v4), *(v3));
            LocalFree(v3);
        }
        if (v4)
            LocalFree(v4);
    }
    v15 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v15) = v0;
    v2 = sub_417ab3;
    sub_417aa3();
    return;
}
```

## `sub_00417aa3` `0x00417aa3`

_9 bytes. (leaf/helper — see body)_

```c
int sub_417aa3(void)
{
    return sub_403a10();
}
```

## `sub_00417aac` `0x00417aac`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_417aac(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00417ab1` `0x00417ab1`

_2 bytes. (leaf/helper — see body)_

```c
int sub_417ab1(void)
{
    return sub_417aa3();
}
```

## `sub_00417ab3` `0x00417ab3`

_8 bytes. (leaf/helper — see body)_

```c
int sub_417ab3(unsigned int a0)
{
    unsigned int v0;  // ebx

    return v0;
}
```

## `sub_00417b26` `0x00417b26`

_5 bytes. (leaf/helper — see body)_

```c
int sub_417b26(void)
{
    void* v1;  // eax

    (int)v1[47]();
}
```

## `sub_00417b2c` `0x00417b2c`

_3 bytes. (leaf/helper — see body)_

```c
int sub_417b2c(void)
{
    void* v1;  // eax

    (int)v1[47]();
}
```

## `sub_00417b30` `0x00417b30`

_3 bytes. (leaf/helper — see body)_

```c
int sub_417b30(void)
{
    void* v1;  // eax

    (int)v1[47]();
}
```

## `sub_00417b3b` `0x00417b3b`

_3 bytes. (leaf/helper — see body)_

```c
void sub_417b3b(void)
{
    return;
}
```

## `sub_00417b3e` `0x00417b3e`

_40 bytes. (leaf/helper — see body)_

```c
extern char g_19555510;

void sub_417b3e(void)
{
    unsigned int v4;  // eax
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp-0x4]
    unsigned int *v3;  // [bp+0xfffe1]

    v3();
    v4 = v3();
    g_19555510 = g_19555510 | (char)v4;
    v1 = &/* unsupported instruction */;
    v0 = v4;
    __unsupported_jumpkind_Ijk_Privileged()
}
```

## `sub_00417bb8` `0x00417bb8`

_478 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[88];
    unsigned int field_58;
} struct_1;

typedef struct struct_2 {
    char padding_0[2];
    unsigned int field_2;
    char padding_6[80];
    char field_56[5];
    unsigned int field_57;
} struct_2;

typedef struct struct_3 {
    char padding_0[2];
    unsigned int field_2;
    char padding_6[80];
    char field_56[5];
    char field_57;
} struct_3;

typedef struct struct_0 {
    void* field_0;
} struct_0;

extern char g_137e0f19;
extern char g_ced00101;
extern char g_d6555452;
extern char g_ff2e7c06;
extern char g_ffa97c06;

int sub_417bb8(void)
{
    unsigned short v86;  // es
    void* iter;  // ebp
    unsigned int v96;  // esi
    unsigned int v185;  // eax
    unsigned int v186;  // 4359
    unsigned int v187;  // 4361
    unsigned short v188;  // ax
    unsigned int v189;  // 4364
    unsigned int v191;  // 4374
    unsigned long long v192;  // 4375
    char v97;  // al
    unsigned int v98;  // eax
    unsigned int v99;  // 4153
    char v100;  // al
    unsigned int v101;  // 4167
    struct_2 *v102;  // ebx
    char v103;  // al
    unsigned int v104;  // edi
    unsigned int v88;  // edx
    void* v106;  // eax
    unsigned int v107;  // 4206
    struct_2 *node;  // ebx
    unsigned int v109;  // 4212
    struct_2 *v110;  // ebx
    unsigned int v111;  // 4123
    unsigned int v112;  // 4124
    char v113;  // al
    unsigned int v115;  // eax
    void* v89;  // edx
    unsigned int v116;  // 4169
    char v117;  // 4098
    unsigned int v118;  // cc_dep1
    unsigned int v119;  // cc_dep2
    void* v120;  // edi
    void* v121;  // eax
    unsigned int v122;  // 4117
    void* v123;  // eax
    void* idx;  // ecx
    struct_1 *v90;  // ebx
    unsigned int v125;  // 4175
    unsigned long long v126;  // 4176
    char v127;  // 4104
    unsigned int v128;  // 4496
    unsigned short v129;  // ax
    char v130;  // dl
    char v131;  // 4112
    unsigned int v132;  // 4500
    char v133;  // 4118
    unsigned int v134;  // 4504
    unsigned int v91;  // 4107
    char v135;  // 4124
    unsigned int v136;  // 4508
    char v137;  // 4130
    unsigned int v138;  // 4512
    unsigned int v139;  // 4516
    char v140;  // 4142
    char v141;  // 4146
    unsigned int v142;  // 4520
    unsigned int v143;  // 4525
    unsigned long v144;  // 4526
    unsigned short v92;  // cs
    unsigned int v145;  // 4162
    unsigned int v146;  // 4529
    unsigned int v147;  // 4531
    unsigned int v148;  // eax
    unsigned int v149;  // 4173
    unsigned int v150;  // 4544
    unsigned int v151;  // 4546
    void* v152;  // edi
    unsigned long long v153;  // 4555
    unsigned int v154;  // 4567
    char v93;  // al
    unsigned int v155;  // 4569
    unsigned int v156;  // eax
    void* v157;  // edi
    unsigned int v158;  // eax
    void* v159;  // eax
    void* v160;  // edi
    unsigned int v161;  // 4269
    unsigned long long v162;  // 4270
    void* v163;  // eax
    unsigned int v164;  // cc_ndep
    char v94;  // al
    void* v165;  // cc_dep1
    void* v166;  // eax
    unsigned short v168;  // ax
    void* v169;  // ebp
    unsigned int v170;  // 4297
    unsigned int v171;  // 4309
    unsigned long v172;  // 4310
    unsigned int v173;  // 4113
    void* v174;  // ebp
    void* v95;  // ecx
    unsigned int v175;  // 4122
    unsigned long long v176;  // 4123
    unsigned int v177;  // 4334
    unsigned long v178;  // 4335
    unsigned int v179;  // 4345
    unsigned long v180;  // 4346
    char v181;  // al
    unsigned short v182;  // ax
    unsigned int v183;  // 4355
    unsigned int v184;  // 4357
    unsigned int v0;  // [bp-0x163]
    unsigned int v1;  // [bp-0x15f]
    unsigned int v2;  // [bp-0x15b]
    unsigned int v3;  // [bp-0x157]
    unsigned int v4;  // [bp-0x153]
    unsigned int v5;  // [bp-0x14f]
    unsigned int v6;  // [bp-0x14b]
    unsigned int v7;  // [bp-0x147]
    unsigned int v8;  // [bp-0x143]
    unsigned int v9;  // [bp-0x13f]
    void* v10;  // [bp-0x13b], Other Possible Types: unsigned int
    char *v11;  // [bp-0x137]
    void* v12;  // [bp-0x133]
    unsigned int v13;  // [bp-0x133]
    void* v14;  // [bp-0x12f]
    unsigned int v15;  // [bp-0x12b]
    void* v16;  // [bp-0x127]
    void* *v17;  // [bp-0x123]
    void* v18;  // [bp-0x11f]
    void* v19;  // [bp-0x11b]
    void* *v20;  // [bp-0x117]
    void* v21;  // [bp-0x113]
    unsigned int v22;  // [bp-0x10f]
    void* v23;  // [bp-0xe7]
    void* v24;  // [bp-0xe4]
    struct_0 **v25;  // [bp-0xe3]
    void* *v26;  // [bp-0xe0]
    void* v27;  // [bp-0xdc]
    void* *v28;  // [bp-0xd8]
    void* v29;  // [bp-0xd4]
    void* v30;  // [bp-0xd0]
    struct_3 **v31;  // [bp-0xcc]
    struct_2 *v32;  // [bp-0xc8]
    void* v33;  // [bp-0xc4]
    char *v34;  // [bp-0xc0]
    void* v35;  // [bp-0xbc]
    void* *v36;  // [bp-0xb8]
    void* v37;  // [bp-0xb4]
    void* v38;  // [bp-0xb0]
    unsigned int v39;  // [bp-0xac]
    unsigned short v40;  // [bp-0xa8]
    void* v41;  // [bp-0xa4]
    void* v42;  // [bp-0xa0]
    unsigned short v43;  // [bp-0x9c]
    void* v44;  // [bp-0x98]
    void* v45;  // [bp-0x94]
    void* v46;  // [bp-0x90]
    void* v47;  // [bp-0x8c]
    void* v48;  // [bp-0x88]
    void* v49;  // [bp-0x84]
    void* v50;  // [bp-0x80]
    void* v51;  // [bp-0x7c]
    void* v52;  // [bp-0x78]
    unsigned short v53;  // [bp-0x74]
    void* v54;  // [bp-0x70], Other Possible Types: unsigned int
    void* v55;  // [bp-0x6c]
    void* v56;  // [bp-0x60]
    char *v57;  // [bp-0x5c], Other Possible Types: void*
    void* v58;  // [bp-0x58], Other Possible Types: char
    void* v59;  // [bp-0x54]
    void* v60;  // [bp-0x50]
    void* v61;  // [bp-0x44], Other Possible Types: unsigned short
    void* v62;  // [bp-0x40]
    void* v63;  // [bp-0x3c]
    void* v64;  // [bp-0x38]
    void* v65;  // [bp-0x2c]
    unsigned short v66;  // [bp-0x28]
    void* v67;  // [bp-0x24]
    void* v68;  // [bp-0x20]
    void* v69;  // [bp-0x1c]
    void* v70;  // [bp-0x18]
    void* v71;  // [bp-0x14]
    void* v72;  // [bp-0x12]
    unsigned short v73;  // [bp-0x10]
    void* v74;  // [bp-0xe]
    void* v75;  // [bp-0xc]
    struct_1 *idx1;  // [bp-0xa]
    unsigned int v77;  // [bp-0x8]
    void* v78;  // [bp-0x6]
    void* v79;  // [bp-0x2]
    char v81;  // [bp+0xfffdc]
    unsigned int v85;  // [bp+0x10005b]

    v77 = /* unsupported instruction */;
    v75 = /* unsupported instruction */ + 1;
    v73 = v86;
    iter = v75 + 1;
    v71 = iter;
    v89 = v88 | iter;
    v70 = v89;
    v69 = iter;
    v68 = iter;
    if ((v88 | iter) < 0)
    {
        v67 = iter;
        v79 = iter;
        v78 = iter;
        idx1 = &v90->padding_0[2];
        v74 = iter;
        v72 = iter;
    }
    v91 = _ccall(15, v88 | iter, 0, 0);
    v67 = iter;
    v66 = v92;
    v94 = (v93 + 69) * 84 + 0x55 + ((char)v91 & 1);
    *((unsigned int *)v95) = *((int *)v95) ^ v96;
    v65 = iter;
    v63 = iter;
    *((unsigned int *)&idx1->padding_0[86]) = *((int *)&idx1->padding_0[86]) + (v94 ^ 0x55);
    v61 = iter;
    v64 = iter;
    v97 = ((v94 ^ 0x55) + 82) * 0x44;
    v63 = iter;
    v98 = _INSERT(v97 CONCAT 0, 0, v97 + 82);
    v99 = _ccall(1, (unsigned int)v97, 82, 0);
    v62 = iter;
    v61 = v92;
    v100 = (char)v98 + 0x55 + ((char)v99 & 1);
    v101 = _ccall(9, v98, 480073045 ^ v99 & 1, v99 & 1);
    v102 = &idx1->padding_0[2 + -1 * *((int *)(480073045 + (char *)v95 + v98 + (v99 & 1))) + -1 * (v101 & 1) + 1];
    v59 = iter;
    v57 = &v58;
    v60 = iter;
    v59 = iter;
    v103 = (v100 - 59) * 83;
    v58 = iter;
    v57 = iter;
    v56 = iter;
    v54 = v104;
    v52 = iter;
    v55 = iter;
    v106 = _INSERT(_INSERT(v103 CONCAT 0, 1, 0), 0, v103);
    v107 = _ccall(1, (unsigned int)v100, 197, 0);
    node = &v102->padding_0[1];
    v54 = iter;
    v53 = v92;
    v109 = _ccall(4, 18, v102 + 1, 0, v107);
    if ((char)v109)
    {
        v52 = iter;
        v110 = _INSERT(node, 1, 123);
        v111 = _ccall(18, v102 + 1, 0, v107);
        v112 = _ccall((unsigned short)v111 CONCAT *((unsigned short *)(void*)&v106), 39);
        *((char *)v95) = *((char *)v95) ^ 123;
        v51 = iter;
        v50 = iter;
        v49 = iter;
        v48 = iter;
        v47 = iter;
        v113 = (char)v112 * 93;
        v46 = iter;
        v45 = iter;
        v115 = _INSERT(_INSERT(v113 CONCAT 0, 1, 0), 0, v113);
        v116 = _ccall(6, v85, v89, 0);
        node = &v110->padding_0[1];
        v44 = iter;
        v43 = v92;
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
        v117 = v81;
        v81 = v117 + *((char *)&node);
        v118 = v117;
        v119 = *((char *)&node);
        v120 = v115 + 1529173 + (v116 & 1);
        v42 = v95;
        v121 = *((unsigned short *)&v120);
        v122 = _ccall(10, 1, (unsigned int)v117, (unsigned int)*((char *)(void*)&node), 0);
        v106 = v121;
        if ((char)v122)
        {
            v123 = v120;
            v120 = v121;
            iter -= 1;
            v41 = iter;
            node = &node->padding_0[1];
            v40 = v92;
            v118 = *((char *)((void*)&v123 >> 31 + 1));
            v119 = *((char *)&node);
            v106 = v123;
        }
        idx = 0xd679b9d6;
        v39 = 1431589397;
        v38 = iter;
        v89 = v38;
        v125 = _ccall(1, v118, v119, 0);
        v126 = _ccall((unsigned int)(char)(char)v120[1839901355], 1, v125, 1);
        *((char *)&v120[1839901355]) = v126;
        g_137e0f19 = g_137e0f19 + 214 + ((char)(v126 >> 32) & 1);
        v38 = iter;
        v37 = v89;
        v36 = &v37;
        v35 = iter;
    }
    v34 = &v35;
    v33 = iter;
    v127 = (char)iter[1431655757];
    v128 = _ccall(3, v106, 1405960362, 0);
    *((char *)&iter[1431655757]) = (char)iter[1431655757] + *((char *)((void*)&node + 1)) + ((char)v128 & 1);
    v129 = (unsigned short)v106 + 16554;
    v130 = (char)v89;
    v131 = (char)idx[0x27fbaabd];
    v132 = _ccall(7, (unsigned int)v127, (unsigned int)(*((char *)((void*)&node + 1)) ^ (char)v128 & 1), v128 & 1);
    *((char *)&idx[0x27fbaabd]) = (char)idx[0x27fbaabd] + *((char *)((void*)&node + 1)) + ((char)v132 & 1);
    v133 = (char)iter[1834673956];
    v134 = _ccall(7, (unsigned int)v131, (unsigned int)(*((char *)((void*)&node + 1)) ^ (char)v132 & 1), v132 & 1);
    *((char *)&iter[1834673956]) = (char)iter[1834673956] - v130 - ((char)v134 & 1);
    v135 = (char)idx[1845209789];
    v136 = _ccall(10, (unsigned int)v133, (unsigned int)(v130 ^ (char)v134 & 1), v134 & 1);
    *((char *)&idx[1845209789]) = (char)idx[1845209789] + (char)v129 + ((char)v136 & 1);
    v137 = (char)iter[1845209789];
    v138 = _ccall(7, (unsigned int)v135, (unsigned int)((char)v129 ^ (char)v136 & 1), v136 & 1);
    *((char *)&iter[1845209789]) = (char)iter[1845209789] + *((char *)((void*)&idx + 1)) + ((char)v138 & 1);
    v139 = _ccall(7, (unsigned int)v137, (unsigned int)(*((char *)((void*)&idx + 1)) ^ (char)v138 & 1), v138 & 1);
    *((char *)&idx[0x27fbaabd]) = (char)idx[0x27fbaabd] + *((char *)((void*)&idx + 1)) + ((char)v139 & 1);
    v140 = (char)iter[665764089];
    *((char *)&iter[665764089]) = (char)iter[665764089] + *((char *)((void*)&node + 1));
    v141 = (char)iter[1052726779];
    v142 = _ccall(1, (unsigned int)v140, (unsigned int)*((char *)((void*)&node + 1)), 0);
    *((char *)&iter[1052726779]) = (char)iter[1052726779] + *((char *)&idx) + ((char)v142 & 1);
    v32 = node;
    v31 = &v32;
    v30 = iter;
    v143 = _ccall(7, (unsigned int)v141, (unsigned int)(*((char *)(void*)&idx) ^ (char)v142 & 1), v142 & 1);
    v144 = _ccall((unsigned int)(char)(char)iter[278012448], 1, v143, 1);
    *((char *)&iter[278012448]) = v144;
    v145 = *((int *)&node->padding_6[77]);
    *((unsigned int *)&node->padding_6[77]) = *((int *)&node->padding_6[77]) + 1062682372;
    v29 = iter;
    v146 = _ccall(3, v145, 1062682372, 0);
    v147 = _ccall((unsigned short)v146 CONCAT v129, 63);
    v148 = _INSERT(v129, 0, v147);
    v28 = &v29;
    /* unsupported instruction */
    v149 = *((int *)(v120 * 2));
    *((unsigned int *)(v120 * 2)) = *((int *)(v120 * 2)) + 1062551381;
    v27 = iter;
    /* unsupported instruction */
    /* unsupported instruction */
    *((unsigned int *)v120) = v148;
    v150 = _ccall(3, v149, 1062551381, 0);
    v151 = _ccall((unsigned short)v150 CONCAT (unsigned short)v148, 63);
    *((char *)v120) = v151;
    v152 = v120 + 1;
    v26 = &v27;
    v24 = iter;
    v153 = _ccall((unsigned int)(char)(char)iter[1430198048], 1, v151 >> 16 & 2261, 1);
    *((char *)&iter[1430198048]) = v153;
    /* unsupported instruction */
    v154 = _ccall(18, &v26 - 2, 0, (unsigned int)(v153 >> 32) & 1);
    v155 = _ccall((unsigned short)v154 CONCAT 16554, 63);
    v156 = v155 & 0xffff | 0x53c50000;
    v25 = (char *)&v26 + 1;
    *((char *)v152) = v156;
    v157 = v152 + 1;
    v158 = v156 + 1;
    *((int *)&node->padding_6[76]) = (/* unsupported instruction */ ? /* unsupported instruction */ : nan);
    v23 = iter;
    g_d6555452 = ~(g_d6555452);
    do
    {
        v22 = 1431589397;
        v21 = iter;
        *((unsigned long *)&iter[0x22]) = (int)iter[0x22] & idx;
        *((char *)&idx[570139170]) = (char)idx[570139170] + *((char *)&idx);
        *((char *)&idx[1377170439]) = (char)idx[1377170439] + *((char *)&idx);
        v20 = &v21;
        v19 = iter;
        v18 = iter;
        v159 = idx;
        /* unsupported instruction */
        *((void* *)(v157 * 2)) = v159;
        *((char *)v157) = *((char *)&v159);
        v160 = v157 + 1;
        *((char *)v160) = *((char *)&v159);
        v161 = _ccall(18, v159 + 1, 0, (unsigned int)(char)(v158 + 1431827389 < v158));
        v162 = _ccall(*((int *)&node->padding_6[76]), 1, v161, 4);
        *((unsigned int *)&node->padding_6[76]) = v162;
        v18 = iter;
        /* unsupported instruction */
        /* unsupported instruction */
        v163 = v160 + 1;
        *((char *)v163) = *((char *)&v163);
        v157 = v163 + 1;
        v164 = (unsigned int)(v162 >> 32) & 1;
        v165 = v163 + 1;
        v166 = v163 + 1;
        v168 = _INSERT(_INSERT(*((unsigned short *)((void*)&v166 + 1)), 1, 0), 0, *((char *)&v166) + *((char *)((void*)&v166 + 1)) * 83);
        v17 = &v18;
        v16 = iter;
        v169 = _INSERT(iter, 0, v168);
        v170 = _ccall(18, v165, 0, v164);
        v158 = _INSERT(*((unsigned short *)&iter) CONCAT 0, 0, (char)v170 & 1);
        v15 = 1431589397;
        v10 = v169;
        v171 = _ccall(18, v165, 0, v164);
        v172 = _ccall((unsigned int)(char)(char)v169[1777815330], 0x99, v171, 1);
        *((char *)&v169[1777815330]) = v172;
        idx = 0x5a7db9d6;
        v173 = _ccall(1, (unsigned int)*((char *)((void*)&v158 >> 31 + 1)), (unsigned int)*((char *)(void*)&node), 0);
        v174 = v169 + 1;
        v175 = _ccall(18, v169 + 1, 0, v173);
        v176 = _ccall((unsigned int)(char)(char)v174[1420415322], 1, v175, 1);
        *((char *)&v174[1420415322]) = v176;
        v14 = v174;
        v12 = v174;
        iter = 0xaaaaabac;
    } while (false);
    v177 = _ccall(0, (unsigned int)(v176 >> 32), 0, 0);
    v178 = _ccall((unsigned int)(char)*((char *)(1431615953 + (char *)v12 + 0x2 * (unsigned int)node)), 1, v177, 1);
    *(1431615953 + (char *)v12 + 0x2 * node) = v178;
    v13 = 2863311788;
    /* unsupported instruction */
    /* unsupported instruction */
    v11 = &v13;
    v10 = 2863311788;
    v179 = _ccall(3, v158, 1409106090, 0);
    v180 = _ccall((unsigned int)g_ff2e7c06, 1, v179, 1);
    g_ff2e7c06 = v180;
    v9 = 2863311788;
    v8 = 2863311788;
    /* unsupported instruction */
    v181 = *((int *)node->padding_0);
    v182 = _INSERT(v181, 0, v181 + 63);
    v7 = 2863311788;
    v183 = _ccall(1, (unsigned int)v181, 63, 0);
    v184 = _ccall((unsigned short)v183 CONCAT v182, 63);
    v185 = _INSERT(v182, 0, v184);
    v6 = 2863311788;
    v186 = _ccall(6, v185, 1430936234, 0);
    v187 = _ccall((unsigned short)v186 CONCAT (unsigned short)v185, 63);
    v188 = v187;
    v5 = 2863311788;
    v189 = _ccall((unsigned short)(v187 >> 16) & 2261 CONCAT v188, 63);
    v4 = 2863311788;
    /* unsupported instruction */
    /* unsupported instruction */
    v3 = 2863311788;
    v2 = 2863311788;
    v191 = _ccall(15, _INSERT(v188 CONCAT 0, 0, (unsigned short)v189) & 1467727111, 0, 0);
    v192 = _ccall((unsigned int)g_ffa97c06, 1, v191, 1);
    g_ffa97c06 = v192;
    v1 = 2863311788;
    v0 = 2863311788;
    g_ced00101 = g_ced00101 + *((char *)((void*)&v12 + 1)) + ((char)(v192 >> 32) & 1);
    __debugbreak();
}
```

## `sub_00417bd9` `0x00417bd9`

_52 bytes. (leaf/helper — see body)_

```c
extern char g_55555521;
extern unsigned int g_55556d55;

int sub_417bd9(void)
{
    unsigned int v17;  // ecx
    unsigned int v18;  // ebp
    unsigned int v19;  // esi
    unsigned int v20;  // 4173
    unsigned short v21;  // cs
    unsigned int v22;  // ebx
    unsigned int v23;  // 4179
    unsigned int idx;  // edx
    unsigned int v0;  // [bp-0x40]
    unsigned int v1;  // [bp-0x3c]
    unsigned int v2;  // [bp-0x38]
    unsigned int v3;  // [bp-0x34]
    unsigned int v4;  // [bp-0x30]
    unsigned int v5;  // [bp-0x2c]
    unsigned short v6;  // [bp-0x28]
    unsigned int v7;  // [bp-0x24]
    unsigned int v8;  // [bp-0x20]
    unsigned int v9;  // [bp-0x14]
    unsigned int v10;  // [bp-0x10]
    unsigned int v11;  // [bp-0xc]
    unsigned int v12;  // [bp-0x8]
    unsigned int v13;  // [bp-0x4]
    unsigned int v14;  // [bp+0x0]
    unsigned int v16;  // [bp+0x100004]

    g_55555521 = g_55555521 ^ *((char *)((void*)&v17 + 1));
    v18 = v16;
    v14 = v19;
    v13 = v18;
    v12 = v18;
    v11 = v18;
    v10 = v18;
    v9 = v18;
    v7 = v17;
    v5 = v18;
    v8 = v18;
    v20 = _ccall(13, (unsigned int)(g_55555521 ^ *((char *)((void*)&v17 + 1))), 0, 0);
    v7 = v18;
    v6 = v21;
    v23 = _ccall(4, 18, v22 + 2, 0, v20);
    if (!((char)v23))
        goto LABEL_0x417c4c;
    v5 = v18;
    *((unsigned int *)(2 * idx + (char *)&g_55556d55)) = *((int *)(2 * idx + (char *)&g_55556d55)) & v19;
    v4 = v18;
    v3 = v18;
    v2 = v18;
    v1 = v18;
    v0 = v18;
}
```

## `sub_00417dcb` `0x00417dcb`

_137 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    char field_4;
} struct_0;

int sub_417dcb(void)
{
    unsigned int v12;  // cc_op
    unsigned int v13;  // cc_dep1
    unsigned int v22;  // 4339
    unsigned short v23;  // ax
    unsigned int v24;  // 4340
    unsigned int v25;  // ebx
    unsigned long long v26;  // 4342
    unsigned int v27;  // 4347
    unsigned int v29;  // 4357
    unsigned int v30;  // eax
    unsigned int v31;  // 4360
    unsigned int v14;  // cc_dep2
    unsigned int v32;  // 4361
    unsigned long v33;  // 4363
    struct_0 *v34;  // edi
    unsigned int *v35;  // esi
    unsigned int v36;  // eax
    unsigned int v37;  // edx
    unsigned int v38;  // 4245
    unsigned long v39;  // 4246
    unsigned int v15;  // cc_ndep
    unsigned int v16;  // 4110
    void* idx;  // ebp
    unsigned int v18;  // eax
    unsigned int v19;  // 4135
    unsigned int v20;  // 4336
    unsigned int v21;  // eax
    void* v0;  // [bp-0x2c]
    void* v1;  // [bp-0x28]
    void* v2;  // [bp-0x24]
    unsigned int v3;  // [bp-0x20]
    void* v4;  // [bp-0x18]
    void* v5;  // [bp-0x14]
    void* v6;  // [bp-0x10], Other Possible Types: unsigned int
    void* v7;  // [bp-0xc], Other Possible Types: void* *
    char *v8;  // [bp-0x8], Other Possible Types: void*
    char *v9;  // [bp-0x4], Other Possible Types: unsigned int
    void* v10;  // [bp+0x0], Other Possible Types: unsigned int

    v16 = _ccall(v12, v13, v14, v15);
    idx = v10;
    /* unsupported instruction */
    v19 = _ccall(4, 9, v18, 3730134098 ^ v16 & 1, v16 & 1);
    if ((char)v19)
    {
        v10 = idx;
        /* unsupported instruction */
        /* unsupported instruction */
        v20 = _ccall(9, v18, 3730134098 ^ v16 & 1, v16 & 1);
        *((char *)&idx[1390879227]) = (char)idx[1390879227] + *((char *)((void*)&*((int *)0xd8553f07) + 1)) + ((char)v20 & 1);
        v21 = _INSERT(*((int *)0xd8553f07), 0, (char)*((int *)0xd8553f07) - 86);
        v22 = _ccall(1, (unsigned int)(char)*((int *)0xd8553f07), 0xaa, 0);
        v23 = (unsigned short)v21 + 1;
        v24 = _ccall(18, v21 + 1, 0, v22);
        v9 = v25;
        v8 = &v9;
        v26 = _ccall((unsigned int)(char)(char)idx[1413009498], 1, (v24 ^ 1) & 2261, 1);
        *((char *)&idx[1413009498]) = v26;
        v6 = idx;
        v5 = idx;
        v27 = _ccall((unsigned short)(v26 >> 32) & 2261 CONCAT v23, 63);
        v4 = idx;
        /* unsupported instruction */
        /* unsupported instruction */
        v29 = _ccall(9, _INSERT((unsigned int)v23, 0, (unsigned short)v27), 1430607165 ^ v27 >> 16 & 2261 & 1, v27 >> 16 & 2261 & 1);
        *((char *)&idx[1390879227]) = (char)idx[1390879227] + *((char *)((void*)&*((int *)0xd8553f07) + 1)) + ((char)v29 & 1);
        v30 = _INSERT(*((int *)0xd8553f07), 0, (char)*((int *)0xd8553f07) - 86);
        v31 = _ccall(1, (unsigned int)(char)*((int *)0xd8553f07), 0xaa, 0);
        v32 = _ccall(18, v30 + 1, 0, v31);
        v3 = &/* unsupported instruction */;
        v2 = idx;
        v33 = _ccall((unsigned int)(char)(char)idx[1411371098], 1, (v32 ^ 1) & 2261, 1);
        *((char *)&idx[1411371098]) = v33;
        v1 = idx;
        v0 = idx;
        /* unsupported instruction */
        /* unsupported instruction */
        __debugbreak();
    }
    v34->field_0 = *(v35);
    v36 = *((int *)0x553d153f) + 78452958;
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
    v10 = v37;
    v9 = &v10;
    v8 = idx;
    v34->field_4 = v36 - 1431617347;
    v38 = _ccall(3, v36, 2863349949, 0);
    v39 = _ccall((unsigned int)(char)(char)idx[1414385754], 1, v38, 1);
    *((char *)&idx[1414385754]) = v39;
    v8 = idx;
    v7 = idx;
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    v7 = &v8;
    v6 = 1377170439;
    /* unsupported instruction */
    __debugbreak();
}
```

## `sub_00417e1f` `0x00417e1f`

_16 bytes. (leaf/helper — see body)_

```c
int sub_417e1f(void)
{
}
```

## `sub_00417e64` `0x00417e64`

_43 bytes. (leaf/helper — see body)_

```c
int sub_417e64(void)
{
    unsigned int v4;  // cc_op
    unsigned int v5;  // cc_dep1
    unsigned long long v14;  // 4225
    unsigned int v15;  // 4236
    unsigned int v16;  // 4246
    unsigned int v6;  // cc_dep2
    unsigned int v7;  // cc_ndep
    unsigned int v8;  // 4220
    unsigned int v9;  // eax
    unsigned int v10;  // 4221
    unsigned short v11;  // ax
    char *v12;  // edi
    unsigned int v13;  // 4224
    char v0;  // [bp-0x2a312fa2]
    unsigned int v1;  // [bp-0x8]

    v8 = _ccall(v4, v5, v6, v7);
    v10 = _ccall(9, v9, 3730134098 ^ v8 & 1, v8 & 1);
    v11 = v9 - 564833198 + (v8 & 1) + 1111686051 - (v10 & 1);
    *(v12) = v11;
    v13 = _ccall(13, (unsigned int)((char)v11 & 0xaa), 0, 0);
    v14 = _ccall((unsigned int)v0, 1, v13, 1);
    v0 = v14;
    v1 = /* unsupported instruction */;
    /* unsupported instruction */
    /* unsupported instruction */
    v15 = _ccall((unsigned short)(v14 >> 32) & 2261 CONCAT v11, 63);
    v16 = _ccall(0, 0, v15 >> 16 & 2261, 0, 0);
    if ((char)v16)
    {
        /* unsupported instruction */
        /* unsupported instruction */
    }
    __debugbreak();
}
```

## `sub_00417e8f` `0x00417e8f`

_110 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[1572147346];
    char field_5db51092;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
    char padding_4[358145720];
    char field_1558debc;
} struct_0;

extern unsigned int g_4ad18de;

int sub_417e8f(void)
{
    unsigned int v19;  // cc_op
    unsigned int v20;  // cc_dep1
    void* v29;  // edi
    unsigned int v30;  // 4149
    unsigned long long v31;  // 4150
    unsigned int v32;  // cc_dep1
    unsigned int v33;  // 4127
    struct_1 *idx;  // ecx
    char v35;  // 4098
    unsigned int v36;  // 4347
    unsigned int v37;  // 4356
    unsigned int v38;  // eax
    unsigned int v21;  // cc_dep2
    char v39;  // al
    unsigned int v40;  // 4376
    unsigned long long v41;  // 4377
    struct_0 *index;  // esi
    unsigned int v43;  // ebx
    unsigned int v22;  // cc_ndep
    unsigned int v23;  // 4126
    unsigned int v24;  // eax
    unsigned int v25;  // 4135
    char v26;  // al
    void* v27;  // edi
    unsigned int v28;  // d
    char v0;  // [bp-0x43df6cf7]
    char v1;  // [bp-0x2a5a2fa2]
    char v2;  // [bp-0x2a1e2fa2]
    struct_0 *v3;  // [bp-0x48]
    unsigned int v4;  // [bp-0x44]
    unsigned int v5;  // [bp-0x40]
    unsigned int v6;  // [bp-0x38]
    unsigned int v7;  // [bp-0x34]
    struct_1 *v8;  // [bp-0x30]
    unsigned int v9;  // [bp-0x2c]
    unsigned int v10;  // [bp-0x28]
    unsigned int v11;  // [bp-0x20]
    unsigned int v12;  // [bp-0x1c]
    unsigned int v13;  // [bp-0x18]
    unsigned int v14;  // [bp-0x14]
    unsigned int v15;  // [bp-0x10]
    unsigned int v16;  // [bp-0x8]

    v23 = _ccall(v19, v20, v21, v22);
    v25 = _ccall(9, v24, 3730134098 ^ v23 & 1, v23 & 1);
    v26 = v24 - 564833198 + (v23 & 1) + 390265767 - (v25 & 1);
    *((char *)v27) = v26;
    v29 = v27 + v28;
    v30 = _ccall(13, (unsigned int)(v26 & 0xaa), 0, 0);
    v31 = _ccall((unsigned int)v1, 1, v30, 1);
    v32 = v31 >> 32;
    v1 = v31;
    v16 = /* unsupported instruction */;
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
    v15 = &/* unsupported instruction */;
    v14 = /* unsupported instruction */;
    v33 = _ccall(4, 0, v32, 0, 0);
    if (!((char)v33))
        goto LABEL_0x417e8a;
    v35 = idx->field_5db51092;
    v36 = _ccall(0, v32, 0, 0);
    idx->field_5db51092 = idx->field_5db51092 + *((char *)&idx) + ((char)v36 & 1);
    v13 = /* unsupported instruction */;
    v12 = /* unsupported instruction */;
    v11 = /* unsupported instruction */;
    /* unsupported instruction */
    v37 = _ccall(7, (unsigned int)v35, (unsigned int)(*((char *)(void*)&idx) ^ (char)v36 & 1), v36 & 1);
    v38 = v29 * 2 + 129302744 + (v37 & 1);
    g_4ad18de = v38;
    /* unsupported instruction */
    /* unsupported instruction */
    v10 = &/* unsupported instruction */;
    v9 = /* unsupported instruction */;
    v8 = idx;
    v39 = v38 - 1431776067;
    *((char *)v29) = v39;
    v40 = _ccall(3, v38, 2863191229, 0);
    v41 = _ccall((unsigned int)v2, 1, v40, 1);
    v2 = v41;
    v7 = /* unsupported instruction */;
    v6 = /* unsupported instruction */;
    v0 = v0 + v39 + ((char)(v41 >> 32) & 1);
    index->field_1558debc = index->field_1558debc + *((char *)((void*)&v43 + 96407699 + 1)) + (v43 + 96407699 < v43);
    v5 = &/* unsupported instruction */;
    v4 = /* unsupported instruction */;
    /* unsupported instruction */
    /* unsupported instruction */
    *((unsigned int *)((char *)v29 + v28)) = index->field_0;
    v3 = &(&index->field_0)[v28];
    __debugbreak();
}
```

## `sub_00417efd` `0x00417efd`

_37 bytes. (leaf/helper — see body)_

```c
int sub_417efd(void)
{
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    __debugbreak();
}
```

## `sub_00417f22` `0x00417f22`

_267 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[1572147346];
    char field_5db51092;
} struct_0;

typedef struct struct_1 {
    void* field_0;
} struct_1;

typedef struct struct_2 {
    char field_0;
} struct_2;

int sub_417f22(void)
{
    unsigned int v42;  // cc_op
    unsigned int v43;  // cc_dep1
    unsigned int v51;  // d
    void* v52;  // edi
    unsigned int v53;  // 4252
    struct_0 *idx;  // ecx
    void* *v55;  // esi
    unsigned int index;  // ebx
    char v57;  // al
    void* iter;  // edi
    char v59;  // al
    unsigned int v44;  // cc_dep2
    int v61;  // eax
    char *v62;  // eax
    char v63;  // al
    char *v64;  // edx
    unsigned int v65;  // 4362
    void* *v66;  // ebx
    unsigned int v67;  // 4378
    unsigned short v68;  // ax
    char *v69;  // eax
    char *v70;  // ebp
    unsigned int v45;  // cc_ndep
    unsigned int v71;  // cc_dep1
    char *v72;  // edx
    unsigned int v73;  // 4153
    unsigned short v74;  // ax
    unsigned int v75;  // 4171
    unsigned int v76;  // 4172
    unsigned int v46;  // 4118
    unsigned int v47;  // 4127
    char v48;  // al
    unsigned int v49;  // cc_dep1
    void* v50;  // edi
    char v0;  // [bp-0x2dda0bf5]
    char *v23;  // [bp-0x60]
    char *v24;  // [bp-0x5c]
    char *v25;  // [bp-0x58]
    struct_1 **v26;  // [bp-0x58]
    struct_2 **v27;  // [bp-0x54]
    char *v28;  // [bp-0x50]
    void* v29;  // [bp-0x3c], Other Possible Types: unsigned int
    unsigned int v30;  // [bp-0x38]
    struct_1 **v31;  // [bp-0x34]
    void* *v32;  // [bp-0x30]
    unsigned int v33;  // [bp-0x2c]
    unsigned int v34;  // [bp-0x28]
    char *v35;  // [bp-0x20], Other Possible Types: unsigned int
    unsigned int v36;  // [bp-0x1c]
    unsigned int v37;  // [bp-0x14]
    unsigned int v38;  // [bp-0x10]
    unsigned int v39;  // [bp-0x8]

    v46 = _ccall(v42, v43, v44, v45);
    v47 = _ccall(9, v69, 3730134098 ^ v46 & 1, v46 & 1);
    v48 = (char)&v69[564833198 + (v46 & 1) + 2143093849 + -1 * (v47 & 1)];
    v49 = v48 & 0xaa;
    *((char *)v50) = v48;
    v52 = v50 + v51;
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
    v39 = &/* unsupported instruction */;
    if (v49)
        goto LABEL_0x417f15;
    v53 = _ccall(13, v49, 0, 0);
    idx->field_5db51092 = idx->field_5db51092 + *((char *)&idx) + ((char)v53 & 1);
    v38 = /* unsupported instruction */;
    v37 = /* unsupported instruction */;
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    v55[2 * index] = v52;
    v0 += 5;
    v36 = &/* unsupported instruction */;
    v35 = /* unsupported instruction */;
    /* unsupported instruction */
    v57 = (char)*(v55);
    *((char *)v52) = v57;
    iter = v52 + v51;
    v59 = v57 + 1;
    v61 = _INSERT(_INSERT(v59, 1, 0), 0, v59 * 84);
    v35 = &v36;
    /* unsupported instruction */
    v34 = &/* unsupported instruction */;
    v30 = /* unsupported instruction */;
    /* unsupported instruction */
    /* unsupported instruction */
    v62 = _INSERT(v61, 0, v61);
    /* unsupported instruction */
    /* unsupported instruction */
    /* unsupported instruction */
    v63 = v61 >> 31;
    v64 = v62 + 72696653;
    v65 = _ccall(9, v62, 72696653, 0);
    v33 = /* unsupported instruction */;
    v66 = &v55[v51];
    v67 = _ccall(1, (unsigned int)(v63 + 73 + ((char)v65 & 1)), 103, 0);
    *((char *)&v29[86]) = (char)v29[86] - *((char *)&v66) - ((char)v67 & 1);
    v68 = (unsigned short)_INSERT(v63, 0, v63 + 73 + ((char)v65 & 1) + 103) + 1;
    v32 = v66;
    v31 = &v32;
    v29 = /* unsupported instruction */;
    v69 = _INSERT(v68, 0, /* unsupported instruction */);
    v70 = _INSERT(/* unsupported instruction */, 0, v68);
    *((char *)&iter[1723640483]) = (char)iter[1723640483] | *((char *)&v64);
    *(v69) = *(v69) | *((char *)&v69);
    v71 = *(v69) | *((char *)&v69);
    /* unsupported instruction */
    /* unsupported instruction */
    v28 = v69;
    v27 = &v28;
    v25 = v70;
    /* unsupported instruction */
    v72 = v69;
    v73 = _ccall(13, v71, 0, 0);
    v74 = x86g_dirtyhelper_IN(0x50<32>, 0x4<32>);
    v26 = &v27;
    v24 = v25;
    v75 = _ccall(7, (unsigned int)*((char *)(void*)&v64), (unsigned int)(21 ^ (char)v73 & 1), v73 & 1);
    v76 = _ccall((unsigned short)v75 CONCAT v74, 63);
    v69 = _INSERT(v74, 0, v76);
    v23 = v24;
    v70 = 0x55555546;
}
```

## `sub_00417ffc` `0x00417ffc`

_90 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[23];
    unsigned int field_17;
    unsigned int field_1a;
    char field_1b;
    char padding_1c[10];
    unsigned int field_26;
    char field_27;
    char padding_28[14];
    char field_36;
    char padding_37[1];
    unsigned int field_38;
    char padding_3c[25];
    unsigned int field_55;
} struct_0;

int sub_417ffc(void)
{
    unsigned int v23;  // cc_op
    unsigned int v24;  // cc_dep1
    struct_0 *idx;  // ebp
    unsigned int v34;  // edx
    unsigned int v35;  // 4177
    unsigned int v36;  // 4444
    unsigned int v37;  // 4446
    unsigned short v38;  // ax
    unsigned int v39;  // 4449
    unsigned int v40;  // eax
    unsigned int v41;  // 4451
    unsigned int v42;  // 4453
    unsigned int v25;  // cc_dep2
    unsigned int v26;  // cc_ndep
    unsigned int v27;  // 4434
    unsigned short v28;  // ax
    unsigned int v29;  // 4436
    unsigned int v30;  // 4439
    unsigned long long v31;  // 4441
    char v32;  // al
    struct_0 *v0;  // [bp-0x54]
    struct_0 *v1;  // [bp-0x50]
    struct_0 *v2;  // [bp-0x4c]
    struct_0 *v3;  // [bp-0x48]
    struct_0 *v4;  // [bp-0x44]
    struct_0 *v5;  // [bp-0x40]
    struct_0 *v6;  // [bp-0x3c]
    struct_0 *v7;  // [bp-0x38]
    struct_0 *v8;  // [bp-0x34]
    struct_0 *v9;  // [bp-0x30]
    struct_0 *v10;  // [bp-0x2c]
    struct_0 *v11;  // [bp-0x28]
    struct_0 *v12;  // [bp-0x24]
    struct_0 *v13;  // [bp-0x20]
    struct_0 *v14;  // [bp-0x1c]
    struct_0 *v15;  // [bp-0x18]
    struct_0 *v16;  // [bp-0x14]
    struct_0 *v17;  // [bp-0x10]
    struct_0 *v18;  // [bp-0xc]
    struct_0 *v19;  // [bp-0x8]
    struct_0 *v20;  // [bp-0x4]
    struct_0 *v21;  // [bp+0x0]

    v20 = v21;
    v20 = v21;
    v27 = _ccall(v23, v24, v25, v26);
    v29 = _ccall((unsigned short)v27 CONCAT v28, 55);
    v19 = v20;
    v30 = _ccall((unsigned short)(v29 >> 16) & 2261 CONCAT (unsigned short)v29, 47);
    v18 = v19;
    v31 = _ccall(*((int *)&v18->padding_3c[13]), 0x55, v30 >> 16 & 2261, 4);
    *((unsigned int *)&v18->padding_3c[13]) = v31;
    v17 = v18;
    v32 = (char)v30 | (((char)(v31 >> 32) & 213 | 1) & 213 | 2) * 0;
    idx = v17;
    v17 = idx;
    v16 = idx;
    v15 = idx;
    *((unsigned int *)&(idx->padding_0)[1]) = *((int *)&(idx->padding_0)[1]) | v34;
    v14 = idx;
    v13 = idx;
    *((char *)&idx->field_17 + 3) = *((char *)&idx->field_17 + 3) ^ (char)v34;
    v12 = idx;
    v11 = idx;
    v35 = *((int *)((char *)&idx->field_17 + 2));
    *((unsigned int *)((char *)&idx->field_17 + 2)) = *((int *)((char *)&idx->field_17 + 2)) ^ v34;
    v10 = idx;
    v36 = _ccall(15, v35 ^ v34, 0, 0);
    v37 = _ccall((unsigned short)v36 CONCAT (unsigned short)_INSERT((unsigned int)v32, 0, v32 ^ 0x55 ^ 0x55), 55);
    v38 = v37;
    v9 = idx;
    v39 = _ccall((unsigned short)(v37 >> 16) & 2261 CONCAT v38, 63);
    v40 = _INSERT(v38 CONCAT 0, 0, v39);
    v8 = idx;
    idx->padding_28[5] = idx->padding_28[5] ^ (char)v34;
    v7 = idx;
    *((unsigned int *)&idx->padding_1c[5]) = *((int *)&idx->padding_1c[5]) & v34;
    v6 = idx;
    *((unsigned int *)&idx->padding_28[7]) = *((int *)&idx->padding_28[7]) | v34;
    v5 = idx;
    v4 = idx;
    v3 = idx;
    v41 = _ccall(6, v40, 995433557, 0);
    v42 = _ccall((unsigned short)v41 CONCAT (unsigned short)v40, 63);
    v2 = idx;
    *((unsigned int *)&idx->padding_1c[6]) = *((int *)&idx->padding_1c[6]) + v34 + (v42 >> 16 & 2261 & 1);
    v1 = idx;
    v0 = idx;
}
```

## `sub_0041807d` `0x0041807d`

_47 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[85];
    unsigned int field_55;
} struct_0;

int sub_41807d(void)
{
    unsigned int v10;  // cc_op
    unsigned int v11;  // cc_dep1
    unsigned short v20;  // es
    unsigned long v21;  // ldt
    unsigned long v22;  // gdt
    unsigned long v23;  // 4283
    char v24;  // dl
    unsigned int v12;  // cc_dep2
    unsigned int v13;  // cc_ndep
    unsigned int v14;  // 4272
    unsigned short v15;  // ax
    unsigned int v16;  // 4274
    unsigned int v17;  // 4277
    unsigned long v18;  // 4279
    struct_0 *v19;  // ebp
    unsigned int v0;  // [bp-0x20]
    unsigned short v1;  // [bp-0x1c]
    struct_0 *v2;  // [bp-0x18]
    struct_0 *v3;  // [bp-0x14]
    struct_0 *v4;  // [bp-0x10]
    struct_0 *v5;  // [bp-0xc]
    struct_0 *v6;  // [bp-0x8]
    struct_0 *v7;  // [bp-0x4]
    struct_0 *v8;  // [bp+0x0]

    v7 = v8;
    v7 = v8;
    v14 = _ccall(v10, v11, v12, v13);
    v16 = _ccall((unsigned short)v14 CONCAT v15, 55);
    v6 = v7;
    v17 = _ccall((unsigned short)(v16 >> 16) & 2261 CONCAT (unsigned short)v16, 47);
    v5 = v6;
    v18 = _ccall(*((int *)&(v5->padding_0)[1]), 0x55, v17 >> 16 & 2261, 4);
    *((unsigned int *)&(v5->padding_0)[1]) = v18;
    v4 = v5;
    v19 = v4;
    v4 = v19;
    v3 = v19;
    v2 = v19;
    v1 = v20;
    v23 = _ccall(v21, v22, (unsigned int)v20, v19 + 12);
    *((char *)v23) = *((char *)v23) ^ v24;
    v0 = *((int *)0x16220f51);
    x86g_dirtyhelper_write_cr0(Load(addr=0x16220f51<32>, size=4, endness=Iend_LE))
    __unsupported_jumpkind_Ijk_Yield()
}
```

## `sub_004181d2` `0x004181d2`

_176 bytes. calls ReadFile_

```c
int sub_4181d2(void)
{
    unsigned int *v4;  // edi
    unsigned int v5;  // eax
    unsigned int v15;  // ebx
    unsigned int v16;  // eax
    unsigned int v17;  // eax
    unsigned int v18;  // edx
    unsigned int v19;  // eax
    unsigned int v20;  // eax
    unsigned int v6;  // cc_op
    unsigned int v7;  // cc_dep1
    unsigned int v8;  // cc_dep2
    unsigned int v9;  // cc_ndep
    unsigned int v10;  // 4112
    HANDLE v11;  // esi
    unsigned int size;  // ebx
    void* v13;  // edi
    unsigned long v0;  // [bp-0x7]
    unsigned int v1;  // [bp-0x4]
    int v2;  // [bp+0x1]

    x86g_dirtyhelper_OUT(Conv(16I->32I, vvar_91{r16|2b}), Conv(8I->32I, Extract(vvar_90{r8|4b}, 8bits@0x0<64>)), 0x1<32>)
    *(v4) = v5;
    v10 = _ccall(12, v6, v7, v8, v9);
    if (!((char)v10))
    {
        v1 = 493229926;
    }
    else if (v11 != 0xffffffff)
    {
        size = GetFileSize(v11, NULL);
        v13 = sub_40536c(0x40, size);
        if (v13)
        {
            v1 = 0;
            v0 = _INSERT(64 CONCAT 0, 0, _INSERT(v13, 0, *((char *)&v13) & 4));
            if (ReadFile(v11, v13, size, v0, *((unsigned int *)((void*)&v0 + 4))) && size == *((unsigned int *)&v2))
            {
                v15 = 0;
                v16 = *((unsigned int *)&v2) - 1 >> 1;
                if (v16 >= NULL)
                {
                    v17 = v16 + 1;
                    v18 = 0;
                    do
                    {
                        v19 = v17;
                        v15 += *((short *)((char *)v13 + 2 * v18));
                        if ((v15 & 0xffff0000))
                            v15 = (v15 & 0xffff) + (v15 >> 16);
                    } while ((v18 += 1, v20 = v19 - 1, v17 = v19 - 1, v19 != 1));
                }
            }
            LocalFree(v13);
        }
        CloseHandle(v11);
        return;
    }
    else
    {
        return;
    }
}
```

## `sub_004181ef` `0x004181ef`

_31 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[26];
    unsigned int field_1a;
} struct_0;

typedef struct struct_1 {
    char padding_0[28];
    unsigned int field_1c;
} struct_1;

int sub_4181ef(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, struct_0 *a5, unsigned int a6)
{
    unsigned int v1;  // cc_op
    unsigned int v2;  // cc_dep1
    unsigned int v11;  // ebx
    unsigned int v12;  // ebp
    unsigned int v13;  // esi
    unsigned int v14;  // edi
    unsigned int v15;  // 4190
    unsigned int v3;  // cc_dep2
    unsigned int v4;  // cc_ndep
    unsigned int v5;  // 4165
    unsigned int v6;  // 4099
    unsigned int v7;  // 4100
    struct_1 *v8;  // eax
    unsigned int v9;  // ecx
    unsigned int v10;  // edx
    char v0;  // [bp+0x20]

    a2 = &v0;
    v5 = _ccall(v1, v2, v3, v4);
    /* unsupported instruction */ = &(&v0)[*((int *)&(a5->padding_0)[1]) + (v5 & 1)];
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
    /* unsupported instruction */ = (/* unsupported instruction */ + 32 | *((int *)(*((int *)(/* unsupported instruction */ + 24)) + 43))) + 64;
    /* unsupported instruction */ = /* unsupported instruction */ + 32;
    v6 = *((int *)*((int *)/* unsupported instruction */));
    v7 = *((int *)*((int *)(/* unsupported instruction */ + 4)));
    v8 = *((int *)(/* unsupported instruction */ + 28));
    v9 = *((int *)(/* unsupported instruction */ + 24));
    v10 = *((int *)(/* unsupported instruction */ + 20));
    v11 = *((int *)(/* unsupported instruction */ + 16));
    v12 = *((int *)(/* unsupported instruction */ + 8));
    v13 = *((int *)(/* unsupported instruction */ + 4));
    v14 = *((int *)/* unsupported instruction */);
    /* unsupported instruction */ = /* unsupported instruction */ + 32;
    /* unsupported instruction */ = /* unsupported instruction */ - 1;
    *((struct_1 **)(/* unsupported instruction */ - 4)) = v8;
    *((unsigned int *)(/* unsupported instruction */ - 8)) = v9;
    *((unsigned int *)(/* unsupported instruction */ - 12)) = v10;
    *((unsigned int *)(/* unsupported instruction */ - 16)) = v11;
    *((int *)(/* unsupported instruction */ - 20)) = /* unsupported instruction */;
    *((unsigned int *)(/* unsupported instruction */ - 24)) = v12;
    *((unsigned int *)(/* unsupported instruction */ - 28)) = v13;
    *((unsigned int *)(/* unsupported instruction */ - 32)) = v14;
    v15 = _ccall(0, 21, /* unsupported instruction */ - 1, 0, (unsigned int)(char)(v7 < v6));
    if (!((char)v15))
        goto LABEL_0x418266;
    /* unsupported instruction */ = v8->field_1c * 727715168;
    *((struct_1 **)(/* unsupported instruction */ - 4)) = v8;
    *((unsigned int *)(/* unsupported instruction */ - 8)) = v9;
    *((unsigned int *)(/* unsupported instruction */ - 12)) = v10;
    *((unsigned int *)(/* unsupported instruction */ - 16)) = v11;
    *((int *)(/* unsupported instruction */ - 20)) = /* unsupported instruction */;
    *((unsigned int *)(/* unsupported instruction */ - 24)) = v12;
    *((unsigned int *)(/* unsupported instruction */ - 28)) = v13;
    *((unsigned int *)(/* unsupported instruction */ - 32)) = v14;
}
```

## `sub_0041820f` `0x0041820f`

_2 bytes. (leaf/helper — see body)_

```c
void sub_41820f(void)
{
    return;
}
```

## `sub_00418224` `0x00418224`

_30 bytes. (leaf/helper — see body)_

```c
int sub_418224(void)
{
    unsigned int v5;  // ebx
    unsigned int v6;  // esi
    unsigned int v7;  // edi
    unsigned int v8;  // ecx
    PWSTR v9;  // eax
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    unsigned int v3;  // [bp-0x4]

    v3 = v5;
    v2 = v6;
    v1 = v7;
    v0 = v8;
    CreateFileW(v9, 0x80000000, FILE_SHARE_READ, NULL, OPEN_EXISTING, SECURITY_ANONYMOUS, NULL);
}
```

## `sub_004182d5` `0x004182d5`

_3 bytes. (leaf/helper — see body)_

```c
int sub_4182d5(void)
{
    sub_4182d8();
    return;
}
```

## `sub_004182d8` `0x004182d8`

_249 bytes. refs ", v7);
        sub_409eac("_

```c
extern char g_41f13c;
extern unsigned short g_4208d8;

int sub_4182d8(void)
{
    unsigned int v12;  // ebx
    unsigned long v13;  // ldt
    unsigned short v20[2];  // eax
    unsigned long v21;  // 4118
    unsigned long v14;  // gdt
    unsigned short v15;  // fs
    unsigned long v16;  // 4182
    unsigned long v17;  // 4186
    unsigned int v0;  // [bp-0x6c]
    unsigned int v1;  // [bp-0x60]
    unsigned int v2;  // [bp-0x5c]
    char *v3;  // [bp-0x58]
    unsigned int v4;  // [bp-0x54]
    int v5;  // [bp-0x50]
    int v6;  // [bp-0x4c]
    int v7;  // [bp-0x48]
    WCHAR v8[30];  // [bp-0x44]
    unsigned int v9;  // [bp-0x8]
    char v10;  // [bp-0x4]

    v4 = v12;
    v7 = 0;
    v6 = 0;
    v5 = 0;
    v9 = 0;
    v3 = &v10;
    v2 = sub_4183e7;
    v16 = _ccall(v13, v14, (unsigned int)v15, 0);
    v1 = *((int *)v16);
    v17 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((unsigned int **)v17) = &v1;
    if (!g_4208d8)
    {
        if (!(!g_41f13c ? GetSystemDirectoryW(v20, 260) : GetTempPathW(260, v20)))
        {
            v20[0] = 46;
            v20[1] = 0;
        }
        if (v20[1 + lstrlenW(v20)] != 92)
            lstrcatW(v20, "\\");
        sub_409eac();
        sub_409eac("\\", v7);
        sub_409eac(".", v6);
        sub_403d40(v5);
        sub_410c34(sub_403e78(v8), v8);
        lstrcatW(v20, v8);
    }
    else
    {
        lstrcpyW(v20, &g_4208d8);
    }
    v21 = _ccall(v13, v14, (unsigned int)v15, 0);
    *((int *)v21) = v5;
    v0 = sub_4183ee;
    sub_4183d1();
    return;
}
```

## `sub_004183d1` `0x004183d1`

_22 bytes. (leaf/helper — see body)_

```c
int sub_4183d1(void)
{
    sub_403a34();
    return sub_403a10();
}
```

## `sub_004183e7` `0x004183e7`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4183e7(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004183ec` `0x004183ec`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4183ec(void)
{
    return sub_4183d1();
}
```

## `sub_004183ee` `0x004183ee`

_5 bytes. (leaf/helper — see body)_

```c
void sub_4183ee(void)
{
    return;
}
```

## `sub_00418410` `0x00418410`

_125 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
    char padding_1[5];
    char field_6;
    char field_7;
} struct_0;

typedef struct struct_1 {
    char field_0;
} struct_1;

int sub_418410(void)
{
    int v5;  // edi
    int v6;  // esi
    struct_0 *v15;  // ebx
    struct_1 **v16;  // edx
    char *iter;  // esi
    struct_0 *v18;  // ebx
    unsigned int i;  // eax
    int v21;  // eax
    unsigned long v22;  // 4118
    int v7;  // ebx
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4162
    unsigned int v12;  // 4103
    unsigned long v13;  // 4166
    struct_0 *v14;  // eax
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x1c]
    char v2;  // [bp-0x9]
    char v3;  // [bp-0x4]

    sub_403e68(v5, v6, v7);
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v12 = *((int *)v11);
    v0 = *((int *)v11);
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v13) = &v0;
    v2 = v14->field_0;
    sub_403f60(v12, sub_418496, &v3);
    v15 = &v14->padding_1[4];
    iter = &*(v16)->field_0;
    do
    {
        if (v15->field_0 == v2)
        {
            v18 = v15->padding_1;
            i = v18->padding_1[0];
            if (i > 0)
            {
                do
                {
                    *(iter) = v18->field_0 ^ 0x55;
                    iter += 1;
                    i -= 1;
                } while (i != 1);
            }
            v15 = &v18->padding_1[1];
        }
        else
        {
            *(iter) = v15->field_0 ^ 0x55;
            iter += 1;
            v15 = v15->padding_1;
        }
    } while ((v21 = sub_403c80(), sub_403c80() + *(v16) > iter));
    v22 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v22) = v12;
    v1 = sub_41849d;
    sub_41848d();
    return;
}
```

## `sub_0041848d` `0x0041848d`

_9 bytes. (leaf/helper — see body)_

```c
int sub_41848d(void)
{
    return sub_403a10();
}
```

## `sub_00418496` `0x00418496`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_418496(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0041849b` `0x0041849b`

_2 bytes. (leaf/helper — see body)_

```c
int sub_41849b(void)
{
    return sub_41848d();
}
```

## `sub_0041849d` `0x0041849d`

_7 bytes. (leaf/helper — see body)_

```c
void sub_41849d(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5)
{
    return;
}
```

## `sub_004184a4` `0x004184a4`

_625 bytes. (leaf/helper — see body)_

```c
typedef struct OVERLAPPED {
    UIntPtr Internal;
    UIntPtr InternalHigh;
    char Anonymous;
    char padding_9[7];
    HANDLE hEvent;
} OVERLAPPED;

extern unsigned short g_4208d8;

int sub_4184a4(void)
{
    int i;  // ecx
    int v13;  // ecx
    int v22;  // edi
    PWSTR v23;  // eax
    char v24;  // bl
    char *v25;  // edx
    void* v26;  // esi
    char v27;  // bl
    Byte v14[4];  // ebx
    unsigned long v30;  // 4118
    Byte v15[4];  // esi
    unsigned long v16;  // ldt
    unsigned long v17;  // gdt
    unsigned short v18;  // fs
    unsigned long v19;  // 4141
    unsigned int v20;  // 4111
    unsigned long v21;  // 4150
    unsigned int v0;  // [bp-0x3c]
    unsigned int v1;  // [bp-0x34]
    unsigned int v2;  // [bp-0x30]
    Byte v3[4];  // [bp-0x20]
    Byte v4[4];  // [bp-0x1c]
    unsigned int v5;  // [bp-0x18]
    HKEY v6;  // [bp-0x14]
    unsigned int v7;  // [bp-0x10]
    OVERLAPPED v8;  // [bp-0xc]
    unsigned int v9;  // [bp-0x8]
    char v10;  // [bp-0x4]

    i = 7;
    do
    {
        v7 = 0;
        v6 = NULL;
        i -= 1;
    } while (i != 1);
    v4 = v14;
    v3 = v15;
    v19 = _ccall(v16, v17, (unsigned int)v18, 0);
    v20 = *((int *)v19);
    v2 = *((int *)v19);
    v21 = _ccall(v16, v17, (unsigned int)v18, 0);
    *((unsigned int **)v21) = &v2;
    sub_4182d8(v20, sub_41872b, &v10, v22, v15, v14, v13);
    if (!g_4208d8)
    {
        v24 = GetFileAttributesW(v23) == 4294967295;
        if (v25)
            *(v25) = v24 ^ 1;
        v0 = 0;
        sub_409eac(0, 983103, &v6);
        sub_409eac("\\", sub_41872b);
        sub_403d40(*((int *)v19));
        if (!~(RegOpenKeyExA(0x80000002, sub_403e78(*((int *)v19)), *((int *)v19), "\\", sub_41872b)))
            v6 = NULL;
        v8 = (OVERLAPPED)8;
        v7 = 4;
        if (!v24 && v6 && !((sub_409eac(0, &/* unsupported instruction */, v4, &v8), RegQueryValueExA(v6, sub_403e78(0, &/* unsupported instruction */, v4, &v8), NULL, &/* unsupported instruction */, v4, &v8) || v22 != 3 || v8 != 8 || (sub_409eac(0, &/* unsupported instruction */, v3, &v7), RegQueryValueExA(v6, sub_403e78(0, &/* unsupported instruction */, v3, &v7), NULL, &/* unsupported instruction */, v3, &v7) || v22 != 3 || v7 != 4))))
        {
            if (v13 == 0x10000)
            {
                goto LABEL_41860f;
            }
            else
            {
                if (v13 <= 0x10000 || sub_418224() != v15)
                    goto LABEL_41860f;
            }
        }
        else
        {
LABEL_41860f:
            v26 = CreateFileW(v23, 0xc0000000, FILE_SHARE_NONE, NULL, CREATE_ALWAYS, SECURITY_ANONYMOUS, NULL);
            if (v26 != 0xffffffff)
            {
                sub_418410();
                if (!sub_405434(v26, v9, sub_403c80(&v8, 0), &v8, 0) || sub_403c80() != v8)
                    v27 = 0;
                else
                    v27 = 1;
                CloseHandle(v26);
                if (v27 && v6)
                {
                    v4 = 0x10000;
                    v5 = 0x10000;
                    v3 = (char[4])sub_418224();
                    sub_409eac(0, 3, v4, 8);
                    RegSetValueExA(v6, sub_403e78(0, 3, v4, 8), 0, REG_BINARY, v4, 8);
                    sub_409eac(0, 3, v3, 4);
                    RegSetValueExA(v6, sub_403e78(0, 3, v3, 4), 0, REG_BINARY, v3, 4);
                }
            }
        }
        if (v6)
            RegCloseKey(v6);
    }
    else if (v25)
    {
        *(v25) = 1;
    }
    v30 = _ccall(v16, v17, (unsigned int)v18, 0);
    *((unsigned int *)v30) = v0;
    v1 = sub_418732;
    sub_418715();
    return;
}
```

## `sub_00418715` `0x00418715`

_22 bytes. (leaf/helper — see body)_

```c
int sub_418715(void)
{
    sub_403a34();
    return sub_403a10();
}
```

## `sub_0041872b` `0x0041872b`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_41872b(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00418730` `0x00418730`

_2 bytes. (leaf/helper — see body)_

```c
int sub_418730(void)
{
    return sub_418715();
}
```

## `sub_00418732` `0x00418732`

_9 bytes. (leaf/helper — see body)_

```c
int sub_418732(unsigned int a0, unsigned int a1)
{
    unsigned int v0;  // ebx

    return v0;
}
```

## `sub_00418748` `0x00418748`

_447 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420b2c;
extern unsigned int g_420b30;
extern unsigned int g_420b34;
extern unsigned int g_420b38;
extern unsigned int g_420b3c;
extern unsigned int g_420b40;
extern unsigned int g_420b44;
extern unsigned int g_420b48;
extern unsigned int g_420b4c;
extern unsigned int g_420b50;

int sub_418748(void)
{
    unsigned int v6;  // ecx
    unsigned int i;  // ecx
    unsigned long v16;  // 4118
    int v17;  // ebx
    unsigned int v8;  // ecx
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4168
    unsigned int v13;  // 4107
    unsigned long v14;  // 4172
    HMODULE v15;  // ebx
    unsigned int v0;  // [bp-0x28]
    char *v1;  // [bp-0x20], Other Possible Types: unsigned int
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    char v4;  // [bp-0x4]

    v6 = 5;
    do
    {
        v3 = 0;
        v2 = 0;
        v8 = v6 - 1;
        v6 = v8;
    } while (i != 1);
    v1 = &v4;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v13 = *((int *)v12);
    v0 = *((int *)v12);
    v14 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v14) = &v0;
    if (!g_420b3c && !(GetVersion() & 0x80000000))
    {
        sub_409eac();
        v15 = LoadLibraryA(sub_403e78());
        sub_409eac(v13);
        g_420b2c = GetProcAddress(v15, sub_403e78());
        sub_409eac(v13, sub_418915);
        g_420b30 = GetProcAddress(v15, sub_403e78());
        sub_409eac(v13, sub_418915);
        g_420b34 = GetProcAddress(v15, sub_403e78());
        sub_409eac(v13, sub_418915);
        g_420b38 = GetProcAddress(v15, sub_403e78());
        sub_409eac(v13, sub_418915);
        g_420b3c = GetProcAddress(v15, sub_403e78());
        sub_409eac(v13, sub_418915);
        g_420b40 = GetProcAddress(v15, sub_403e78());
        sub_409eac(v13, sub_418915);
        g_420b44 = GetProcAddress(v15, sub_403e78());
        sub_409eac(v13, sub_418915);
        g_420b48 = GetProcAddress(v15, sub_403e78());
        sub_409eac(v13, sub_418915);
        g_420b4c = GetProcAddress(v15, sub_403e78());
        sub_409eac(v13, sub_418915);
        g_420b50 = GetProcAddress(v15, sub_403e78());
    }
    v16 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v16) = v13;
    v1 = sub_41891c;
    return sub_418907(v17, i - 1);
}
```

## `sub_00418907` `0x00418907`

_14 bytes. (leaf/helper — see body)_

```c
int sub_418907(void)
{
    return sub_403a34();
}
```

## `sub_00418915` `0x00418915`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_418915(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

