# elfbot.dll decompiled — jiru 0x10368630..0x10369e4c

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10368630` `0x10368630`

_28 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10368630(unsigned int a0, unsigned int *a1, unsigned int a2)
{
    unsigned int v0;  // [bp-0x8]

    v0 = a2;
    sub_10368470(a0, a1);
    return a0;
}
```

## `sub_10368650` `0x10368650`

_28 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10368650(unsigned int a0, unsigned int *a1, unsigned int a2)
{
    unsigned int v0;  // [bp-0x8]

    v0 = a2;
    sub_10368550(a0, a1);
    return a0;
}
```

## `sub_10368670` `0x10368670`

_174 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b07c;
extern struct_0 *g_1038b168;
extern unsigned int g_103a3ad8;
extern unsigned int g_103a3adc;
extern unsigned int g_103a3ae0;

unsigned int [4] sub_10368670(unsigned int a0, unsigned int *a1)
{
    unsigned int v4;  // edi
    unsigned int v5;  // esi
    unsigned int v6;  // eax
    unsigned int idx[4];  // eax
    unsigned int index[4];  // eax
    unsigned int idx1[4];  // esi
    int v10;  // eax
    unsigned int v11;  // edx
    char v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3[4];  // [bp-0x8]

    if (!g_1038b168((a1[6] < 8 ? a1 + 1 : a1[1]), 0, &v0, v4, v5))
    {
        v6 = g_1038b07c();
        idx = v3;
        idx[2] = 0;
        idx[3] = 0;
        idx[1] = g_103a3ad8;
        idx[0] = v6;
        return idx;
    }
    else if ((*((char *)&&v0) & 16))
    {
        index = v3;
        index[2] = 0;
        index[3] = 0;
        index[0] = 2;
        index[1] = g_103a3ad8;
        return index;
    }
    else
    {
        idx1 = v3;
        idx1[0] = g_103a3adc;
        idx1[1] = g_103a3ae0;
        v10 = sub_103544a0(v1, 0, 0, 1);
        idx1[2] = v10 + v2;
        idx1[3] = v11 + (v10 + v2 < v10);
        return idx1;
    }
}
```

## `sub_10368720` `0x10368720`

_174 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b07c;
extern struct_0 *g_1038b164;
extern unsigned int g_103a3ad8;
extern unsigned int g_103a3adc;
extern unsigned int g_103a3ae0;

unsigned int [4] sub_10368720(unsigned int a0, unsigned int *a1)
{
    unsigned int v4;  // edi
    unsigned int v5;  // esi
    unsigned int v6;  // eax
    unsigned int idx[4];  // eax
    unsigned int index[4];  // eax
    unsigned int idx1[4];  // esi
    int v10;  // eax
    unsigned int v11;  // edx
    char v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3[4];  // [bp-0x8]

    if (!g_1038b164((a1[6] < 16 ? a1 + 1 : a1[1]), 0, &v0, v4, v5))
    {
        v6 = g_1038b07c();
        idx = v3;
        idx[2] = 0;
        idx[3] = 0;
        idx[1] = g_103a3ad8;
        idx[0] = v6;
        return idx;
    }
    else if ((*((char *)&&v0) & 16))
    {
        index = v3;
        index[2] = 0;
        index[3] = 0;
        index[0] = 2;
        index[1] = g_103a3ad8;
        return index;
    }
    else
    {
        idx1 = v3;
        idx1[0] = g_103a3adc;
        idx1[1] = g_103a3ae0;
        v10 = sub_103544a0(v1, 0, 0, 1);
        idx1[2] = v10 + v2;
        idx1[3] = v11 + (v10 + v2 < v10);
        return idx1;
    }
}
```

## `sub_103687d0` `0x103687d0`

_23 bytes. (leaf/helper — see body)_

```c
unsigned int sub_103687d0(unsigned int a0, unsigned int *a1)
{
    sub_10368670(a0, a1);
    return a0;
}
```

## `sub_103687f0` `0x103687f0`

_23 bytes. (leaf/helper — see body)_

```c
unsigned int sub_103687f0(unsigned int a0, unsigned int *a1)
{
    sub_10368720(a0, a1);
    return a0;
}
```

## `sub_10368810` `0x10368810`

_40 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

struct_0 * sub_10368810(struct_0 *a0, unsigned short *a1)
{
    unsigned short *v0;  // eax
    unsigned short *v1;  // eax
    unsigned short *v2;  // eax

    v0 = a1;
    do
    {
        v2 = v0 + 1;
        v0 = v2;
    } while (*(v1));
    return sub_1031fcc0(a0, a1, v1 + 1 - (a1 + 1) >> 1);
}
```

## `sub_1036881d` `0x1036881d`

_3 bytes. (leaf/helper — see body)_

```c
void sub_1036881d(void)
{
}
```

## `sub_10368840` `0x10368840`

_406 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    struct struct_0 *field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

typedef struct struct_4 {
    struct struct_4 *field_0;
} struct_4;

typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

extern struct_2 *g_1038b07c;
extern struct_2 *g_1038b160;
extern unsigned int g_1038e180;
extern unsigned int g_103a3ad8;
extern unsigned int g_103a3adc;
extern unsigned int g_103a3ae0;

int sub_10368840(unsigned int *idx, struct_0 *a1, struct_0 *a2)
{
    unsigned long v15;  // ldt
    unsigned long v16;  // gdt
    unsigned int v25;  // edi
    struct_4 **v26;  // edi
    struct_4 **v27;  // eax
    unsigned int idx1;  // eax
    struct_0 **v29;  // eax
    struct_0 **v30;  // eax
    unsigned long v31;  // 4123
    unsigned short v17;  // fs
    unsigned long v18;  // 4209
    unsigned int v19;  // ebx
    unsigned int v20;  // esi
    unsigned long v21;  // 4213
    struct_0 *v22;  // eax
    unsigned int index;  // ebp
    unsigned int v24;  // eax
    unsigned int v0;  // [bp-0x158]
    unsigned int v1;  // [bp-0x148]
    unsigned int v2;  // [bp-0x134]
    unsigned int v3;  // [bp-0x12c]
    unsigned int v4;  // [bp-0x124]
    struct_0 *v5;  // [bp-0x120]
    int <0x10368840[is_4]|Stack bp-0x120, 1 B>;  // [bp-0x120]
    struct_0 *v6;  // [bp-0x11c]
    char v7;  // [bp-0x118]
    struct_0 v8;  // [bp-0x110]
    unsigned int v9;  // [bp-0x2c]
    unsigned int v10;  // [bp-0x14]
    unsigned int v11;  // [bp-0x10]
    unsigned int v12;  // [bp-0xc]
    unsigned int v13;  // [bp-0x8]
    unsigned int v14;  // [bp-0x4]

    v14 = 4294967295;
    v13 = sub_1037173b;
    v18 = _ccall(v15, v16, (unsigned int)v17, 0);
    v12 = *((int *)v18);
    v11 = g_1038e180 ^ &<0x10368840[is_4]|Stack bp-0x120, 1 B>;
    v4 = v19;
    v3 = v20;
    v2 = g_1038e180 ^ &v26;
    v21 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int **)v21) = &v12;
    v22 = &a1->field_4;
    v6 = a2;
    v5 = v22;
    if (a1->field_18 >= 8)
        v22 = (struct_0 *)v22->padding_0;
    index = g_1038b160(v22, 128, &v8, &v7);
    if (!index)
    {
        *(idx) = g_1038b07c();
        idx[1] = g_103a3ad8;
    }
    else if (index > 128)
    {
        v24 = index;
        v1 = -((v24 >= 0x40000000 ? 1 : 0) & 1) | v24 * 2;
        v25 = (unsigned int)sub_1034fef0();
        v4 = v25;
        v27 = v26;
        v10 = 0;
        if (a1->field_18 >= 8)
            v27 = *(v27);
        idx1 = g_1038b160(v27, index, v25, &/* unsupported instruction */);
        if (!idx1)
        {
            v0 = v25;
            *(idx) = g_1038b07c();
            idx[1] = g_103a3ad8;
            sub_10350eb5();
        }
        else
        {
            *((unsigned short *)(v25 + idx1 * 2)) = 0;
            sub_10368810(&v8, v25);
            *(idx) = g_103a3adc;
            v0 = v25;
            idx[1] = g_103a3ae0;
            sub_10350eb5();
        }
    }
    else
    {
        v29 = &v5;
        *((unsigned short *)((char *)&v5 + 2 * index)) = 0;
        do
        {
            v29 = (char *)v29 + 2;
        } while (*((short *)v29));
        sub_1031fcc0(a2, &v5, v30 - ((char *)&v5 + 2) >> 1);
        *(idx) = g_103a3adc;
        idx[1] = g_103a3ae0;
    }
    v31 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int *)v31) = v9;
    return sub_10351225();
}
```

## `sub_103689e0` `0x103689e0`

_402 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    struct struct_0 *field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

typedef struct struct_4 {
    struct struct_4 *field_0;
} struct_4;

typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

extern struct_2 *g_1038b07c;
extern struct_2 *g_1038b15c;
extern unsigned int g_1038e180;
extern unsigned int g_103a3ad8;
extern unsigned int g_103a3adc;
extern unsigned int g_103a3ae0;

int sub_103689e0(unsigned int *idx, struct_0 *a1, struct_0 *a2)
{
    unsigned long v14;  // ldt
    unsigned long v15;  // gdt
    struct_4 **v24;  // edi
    struct_4 **v25;  // eax
    unsigned int v26;  // eax
    char *v27;  // eax
    char *v28;  // eax
    char *v29;  // eax
    struct_0 **v30;  // eax
    struct_0 **v31;  // eax
    unsigned long v32;  // 4123
    unsigned short v16;  // fs
    unsigned long v17;  // 4209
    unsigned int v18;  // ebx
    unsigned int v19;  // esi
    unsigned long v20;  // 4213
    struct_0 *v21;  // eax
    unsigned int v22;  // ebp
    char *v23;  // esi
    char *v0;  // [bp-0xd8]
    unsigned int v1;  // [bp-0xb4]
    unsigned int v2;  // [bp-0xac]
    char *v3;  // [bp-0xa4], Other Possible Types: unsigned int
    struct_0 *v4;  // [bp-0xa0]
    int <0x103689e0[is_4]|Stack bp-0xa0, 1 B>;  // [bp-0xa0]
    struct_0 *v5;  // [bp-0x9c]
    char v6;  // [bp-0x98]
    struct_0 v7;  // [bp-0x90]
    unsigned int v8;  // [bp-0x2c]
    unsigned int v9;  // [bp-0x14]
    unsigned int v10;  // [bp-0x10]
    unsigned int v11;  // [bp-0xc]
    unsigned int v12;  // [bp-0x8]
    unsigned int v13;  // [bp-0x4]

    v13 = 4294967295;
    v12 = sub_1037177b;
    v17 = _ccall(v14, v15, (unsigned int)v16, 0);
    v11 = *((int *)v17);
    v10 = g_1038e180 ^ &<0x103689e0[is_4]|Stack bp-0xa0, 1 B>;
    v3 = v18;
    v2 = v19;
    v1 = g_1038e180 ^ &v24;
    v20 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int **)v20) = &v11;
    v21 = &a1->field_4;
    v5 = a2;
    v4 = v21;
    if (a1->field_18 >= 16)
        v21 = (struct_0 *)v21->padding_0;
    v22 = g_1038b15c(v21, 128, &v7, &v6);
    if (!v22)
    {
        *(idx) = g_1038b07c();
        idx[1] = g_103a3ad8;
    }
    else if (v22 > 128)
    {
        v23 = (unsigned int)sub_1034fef0();
        v3 = v23;
        v25 = v24;
        v9 = 0;
        if (a1->field_18 >= 16)
            v25 = *(v25);
        v26 = g_1038b15c(v25, v22, v23, &/* unsupported instruction */);
        if (!v26)
        {
            v0 = v23;
            *(idx) = g_1038b07c();
            idx[1] = g_103a3ad8;
            sub_10350eb5();
        }
        else
        {
            v23[v26] = 0;
            v27 = v23;
            v28 = v27;
            do
            {
                v28 += 1;
            } while (*(v28));
            sub_10314830(&v7, v23, v29 - (v27 + 1));
            *(idx) = g_103a3adc;
            v0 = v23;
            idx[1] = g_103a3ae0;
            sub_10350eb5();
        }
    }
    else
    {
        v30 = &v4;
        *((char *)&v4 + v22) = 0;
        do
        {
            v30 = (char *)v30 + 1;
        } while (*((char *)v30));
        sub_10314830(a2, &v4, v31 - ((char *)&v4 + 1));
        *(idx) = g_103a3adc;
        idx[1] = g_103a3ae0;
    }
    v32 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int *)v32) = v8;
    return sub_10351225();
}
```

## `sub_10368b80` `0x10368b80`

_28 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

unsigned int * sub_10368b80(unsigned int *a0, struct_0 *a1, struct_0 *a2)
{
    sub_10368840(a0, a1, a2);
    return a0;
}
```

## `sub_10368ba0` `0x10368ba0`

_28 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

unsigned int * sub_10368ba0(unsigned int *a0, struct_0 *a1, struct_0 *a2)
{
    sub_103689e0(a0, a1, a2);
    return a0;
}
```

## `sub_10368bc0` `0x10368bc0`

_16 bytes. (leaf/helper — see body)_

```c
unsigned int [2] sub_10368bc0(unsigned int a0, unsigned int *a1, unsigned int a2)
{
    *(a1) = a2;
    a1[1] = a0;
    return a1;
}
```

## `sub_10368bd0` `0x10368bd0`

_9 bytes. (leaf/helper — see body)_

```c
void sub_10368bd0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    sub_10368bd9();
    return;
}
```

## `sub_10368bd9` `0x10368bd9`

_48 bytes. (leaf/helper — see body)_

```c
int sub_10368bd9(void)
{
    unsigned int v3;  // edx
    unsigned int *v4;  // eax
    unsigned int v5[2];  // eax
    char v0;  // [bp-0x8]
    unsigned int v1;  // [bp+0x0]

    v5 = v4(&v0, v3);
    if (v5[1] != *((int *)(v1 + 4)))
        return;
    return;
}
```

## `sub_10368c10` `0x10368c10`

_30 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10368c10(unsigned int a0, unsigned int *a1, unsigned int a2)
{
    if (a0 != a1[1])
    {
        return 0;
    }
    else if (*(a1) == a2)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
```

## `sub_10368c30` `0x10368c30`

_6 bytes. refs "error: should never be called"_

```c
int sub_10368c30(void)
{
    return "error: should never be called";
}
```

## `sub_10368c40` `0x10368c40`

_6 bytes. refs "generic"_

```c
int sub_10368c40(void)
{
    return "generic";
}
```

## `sub_10368c50` `0x10368c50`

_6 bytes. refs "system"_

```c
int sub_10368c50(void)
{
    return "system";
}
```

## `sub_10368c60` `0x10368c60`

_31 bytes. (leaf/helper — see body)_

```c
extern char g_1039684c;

unsigned int sub_10368c60(unsigned int a0, char a1)
{
    unsigned int v0;  // [bp-0x8]

    *((char **)a0) = &g_1039684c;
    if ((a1 & 1))
    {
        v0 = a0;
        sub_10350abd();
    }
    return a0;
}
```

## `sub_10368c80` `0x10368c80`

_103 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10396888;
extern unsigned int g_103a3aec;
extern void g_103a3af0;

unsigned int * sub_10368c80(void)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4157
    unsigned long v9;  // 4161
    unsigned long v10;  // 4114
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    unsigned int v3;  // [bp-0x4]

    v3 = 4294967295;
    v2 = sub_103717be;
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v1 = *((int *)v8);
    v0 = g_1038e180 ^ &v1;
    v9 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v9) = &v1;
    if (!(1 & g_103a3af0))
    {
        *((unsigned int *)&g_103a3af0) = *((int *)&g_103a3af0) | 1;
        v3 = 0;
        g_103a3aec = &g_10396888;
        sub_10353c80(sub_10373e60);
    }
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v10) = v1;
    return &g_103a3aec;
}
```

## `sub_10368cf0` `0x10368cf0`

_103 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103968b4;
extern unsigned int g_103a3af4;
extern void g_103a3af8;

unsigned int * sub_10368cf0(void)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4157
    unsigned long v9;  // 4161
    unsigned long v10;  // 4114
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    unsigned int v3;  // [bp-0x4]

    v3 = 4294967295;
    v2 = sub_103717ee;
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v1 = *((int *)v8);
    v0 = g_1038e180 ^ &v1;
    v9 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v9) = &v1;
    if (!(1 & g_103a3af8))
    {
        *((unsigned int *)&g_103a3af8) = *((int *)&g_103a3af8) | 1;
        v3 = 0;
        g_103a3af4 = &g_103968b4;
        sub_10353c80(sub_10373e70);
    }
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v10) = v1;
    return &g_103a3af4;
}
```

## `sub_10368d60` `0x10368d60`

_1216 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    int field_0;
    unsigned int *field_4;
} struct_0;

extern unsigned int g_103a3b4c;

struct_0 * sub_10368d60(struct_0 *a0, int a1)
{
    unsigned int *v0;  // eax
    struct_0 *v1;  // eax
    unsigned int *v10;  // eax
    struct_0 *v11;  // eax
    unsigned int *v12;  // eax
    struct_0 *v13;  // eax
    unsigned int *v14;  // eax
    struct_0 *v15;  // eax
    unsigned int *v16;  // eax
    struct_0 *v17;  // eax
    unsigned int *v18;  // eax
    struct_0 *v19;  // eax
    unsigned int *v2;  // eax
    unsigned int *v20;  // eax
    struct_0 *v21;  // eax
    unsigned int *v22;  // eax
    struct_0 *v23;  // eax
    unsigned int *v24;  // eax
    struct_0 *v25;  // eax
    unsigned int *v26;  // eax
    struct_0 *v27;  // eax
    unsigned int *v28;  // eax
    struct_0 *v29;  // eax
    struct_0 *v3;  // eax
    unsigned int *v30;  // eax
    struct_0 *v31;  // eax
    int v32;  // eax
    unsigned int *v33;  // eax
    struct_0 *v34;  // eax
    unsigned int *v35;  // eax
    struct_0 *v36;  // eax
    unsigned int *v37;  // eax
    struct_0 *v38;  // eax
    unsigned int *v39;  // eax
    unsigned int *v4;  // eax
    struct_0 *v40;  // eax
    unsigned int *v41;  // eax
    struct_0 *v42;  // eax
    unsigned int *v43;  // eax
    struct_0 *v44;  // eax
    unsigned int *v45;  // eax
    struct_0 *v46;  // eax
    unsigned int *v47;  // eax
    struct_0 *v48;  // eax
    unsigned int *v49;  // eax
    struct_0 *v5;  // eax
    struct_0 *v50;  // eax
    unsigned int *v51;  // eax
    struct_0 *v52;  // eax
    unsigned int *v53;  // eax
    struct_0 *v54;  // eax
    unsigned int *v55;  // eax
    struct_0 *v56;  // eax
    unsigned int *v57;  // eax
    struct_0 *v58;  // eax
    unsigned int *v59;  // eax
    unsigned int *v6;  // eax
    struct_0 *v60;  // eax
    unsigned int *v61;  // eax
    struct_0 *v62;  // eax
    unsigned int *v63;  // eax
    struct_0 *v64;  // eax
    unsigned int *v65;  // eax
    struct_0 *v66;  // eax
    unsigned int *v67;  // eax
    struct_0 *v68;  // eax
    unsigned int *v69;  // eax
    struct_0 *v7;  // eax
    struct_0 *v70;  // eax
    unsigned int *v71;  // eax
    struct_0 *v72;  // eax
    unsigned int *v73;  // eax
    struct_0 *v74;  // eax
    unsigned int *v75;  // eax
    struct_0 *v76;  // eax
    unsigned int *v77;  // eax
    struct_0 *v78;  // eax
    unsigned int *v79;  // eax
    unsigned int *v8;  // eax
    struct_0 *v80;  // eax
    unsigned int *v81;  // eax
    struct_0 *v82;  // eax
    unsigned int *v83;  // eax
    struct_0 *v84;  // eax
    unsigned int *v85;  // eax
    struct_0 *v86;  // eax
    unsigned int *v87;  // eax
    struct_0 *v88;  // eax
    unsigned int *v89;  // eax
    struct_0 *v9;  // eax
    struct_0 *v90;  // eax
    struct_0 *v91;  // eax

    if (a1 <= 267)
    {
        if (a1 == 267)
            goto LABEL_10368e48;
        switch (a1)
        {
        case 0:
            v0 = sub_10368cf0();
            v1 = a0;
            v1->field_0 = 0;
            v1->field_4 = v0;
            return v1;
        case 1:
            v14 = sub_10368cf0();
            v15 = a0;
            v15->field_0 = 40;
            v15->field_4 = v14;
            return v15;
        case 2: case 3:
            v12 = sub_10368cf0();
            v13 = a0;
            v13->field_0 = 2;
            v13->field_4 = v12;
            return v13;
        case 4:
LABEL_10368ebb:
            v22 = sub_10368cf0();
            v23 = a0;
            v23->field_0 = 24;
            v23->field_4 = v22;
            return v23;
        case 5: case 12: case 16: case 19: case 32: case 82:
LABEL_10368fa1:
            v24 = sub_10368cf0();
            v25 = a0;
            v25->field_0 = 13;
            v25->field_4 = v24;
            return v25;
        case 6: case 123: case 131:
LABEL_10368e48:
            v26 = sub_10368cf0();
            v27 = a0;
            v27->field_0 = 22;
            v27->field_4 = v26;
            return v27;
        case 8: case 14:
            v18 = sub_10368cf0();
            v19 = a0;
            v19->field_0 = 12;
            v19->field_4 = v18;
            return v19;
        case 15: case 20: case 55:
            v4 = sub_10368cf0();
            v5 = a0;
            v5->field_0 = 19;
            v5->field_4 = v4;
            return v5;
        case 17:
            v20 = sub_10368cf0();
            v21 = a0;
            v21->field_0 = 18;
            v21->field_4 = v20;
            return v21;
        case 21:
LABEL_10368e8d:
            v33 = sub_10368cf0();
            v34 = a0;
            v34->field_0 = 11;
            v34->field_4 = v33;
            return v34;
        case 25: case 29: case 30: case 110:
            v30 = sub_10368cf0();
            v31 = a0;
            v31->field_0 = 5;
            v31->field_4 = v30;
            return v31;
        case 33: case 212:
            v16 = sub_10368cf0();
            v17 = a0;
            v17->field_0 = 39;
            v17->field_4 = v16;
            return v17;
        case 39: case 112:
            v10 = sub_10368cf0();
            v11 = a0;
            v11->field_0 = 28;
            v11->field_4 = v10;
            return v11;
        case 80: case 183:
            v2 = sub_10368cf0();
            v3 = a0;
            v3->field_0 = 0x11;
            v3->field_4 = v2;
            return v3;
        case 111:
            v6 = sub_10368cf0();
            v7 = a0;
            v7->field_0 = 38;
            v7->field_4 = v6;
            return v7;
        case 142: case 170:
LABEL_10368f56:
            v35 = sub_10368cf0();
            v36 = a0;
            v36->field_0 = 16;
            v36->field_4 = v35;
            return v36;
        case 145:
            v8 = sub_10368cf0();
            v9 = a0;
            v9->field_0 = 41;
            v9->field_4 = v8;
            return v9;
        }
    }
    else
    {
        if (a1 > 10004)
        {
            switch (a1)
            {
            case 10009:
                v47 = sub_10368cf0();
                v48 = a0;
                v48->field_0 = 9;
                v48->field_4 = v47;
                return v48;
            case 10014:
                v57 = sub_10368cf0();
                v58 = a0;
                v58->field_0 = 14;
                v58->field_4 = v57;
                return v58;
            case 10035:
                v89 = sub_10368cf0();
                v90 = a0;
                v90->field_0 = 9930;
                v90->field_4 = v89;
                return v90;
            case 10036:
                v61 = sub_10368cf0();
                v62 = a0;
                v62->field_0 = 9928;
                v62->field_4 = v61;
                return v62;
            case 10037:
                v45 = sub_10368cf0();
                v46 = a0;
                v46->field_0 = 9907;
                v46->field_4 = v45;
                return v46;
            case 10038:
                v79 = sub_10368cf0();
                v80 = a0;
                v80->field_0 = 9923;
                v80->field_4 = v79;
                return v80;
            case 10039:
                v55 = sub_10368cf0();
                v56 = a0;
                v56->field_0 = 9910;
                v56->field_4 = v55;
                return v56;
            case 10040:
                v65 = sub_10368cf0();
                v66 = a0;
                v66->field_0 = 9913;
                v66->field_4 = v65;
                return v66;
            case 10041:
                v85 = sub_10368cf0();
                v86 = a0;
                v86->field_0 = 9941;
                v86->field_4 = v85;
                return v86;
            case 10042:
                v75 = sub_10368cf0();
                v76 = a0;
                v76->field_0 = 9921;
                v76->field_4 = v75;
                return v76;
            case 10043:
                v83 = sub_10368cf0();
                v84 = a0;
                v84->field_0 = 9933;
                v84->field_4 = v83;
                return v84;
            case 10045:
                v81 = sub_10368cf0();
                v82 = a0;
                v82->field_0 = 9929;
                v82->field_4 = v81;
                return v82;
            case 10047:
                v43 = sub_10368cf0();
                v44 = a0;
                v44->field_0 = 9901;
                v44->field_4 = v43;
                return v44;
            case 10048:
                v39 = sub_10368cf0();
                v40 = a0;
                v40->field_0 = 9902;
                v40->field_4 = v39;
                return v40;
            case 10049:
                v41 = sub_10368cf0();
                v42 = a0;
                v42->field_0 = 9903;
                v42->field_4 = v41;
                return v42;
            case 10050:
                v67 = sub_10368cf0();
                v68 = a0;
                v68->field_0 = 9914;
                v68->field_4 = v67;
                return v68;
            case 10051:
                v71 = sub_10368cf0();
                v72 = a0;
                v72->field_0 = 9916;
                v72->field_4 = v71;
                return v72;
            case 10052:
                v69 = sub_10368cf0();
                v70 = a0;
                v70->field_0 = 9915;
                v70->field_4 = v69;
                return v70;
            case 10053:
                v49 = sub_10368cf0();
                v50 = a0;
                v50->field_0 = 9906;
                v50->field_4 = v49;
                return v50;
            case 10054:
                v53 = sub_10368cf0();
                v54 = a0;
                v54->field_0 = 9909;
                v54->field_4 = v53;
                return v54;
            case 10055:
                v73 = sub_10368cf0();
                v74 = a0;
                v74->field_0 = 9917;
                v74->field_4 = v73;
                return v74;
            case 10056:
                v63 = sub_10368cf0();
                v64 = a0;
                v64->field_0 = 9904;
                v64->field_4 = v63;
                return v64;
            case 10057:
                v77 = sub_10368cf0();
                v78 = a0;
                v78->field_0 = 9925;
                v78->field_4 = v77;
                return v78;
            case 10060:
                v87 = sub_10368cf0();
                v88 = a0;
                v88->field_0 = 9938;
                v88->field_4 = v87;
                return v88;
            case 10061:
                v51 = sub_10368cf0();
                v52 = a0;
                v52->field_0 = 9908;
                v52->field_4 = v51;
                return v52;
            case 10065:
                v59 = sub_10368cf0();
                v60 = a0;
                v60->field_0 = 9911;
                v60->field_4 = v59;
                return v60;
            case 10010: case 10011: case 10012: case 10015: case 10016: case 10017: case 10018: case 10019: case 10020: case 10021: case 10023: case 10025: case 10026: case 10027: case 10028: case 10029: case 10030: case 10031: case 10032: case 10033: case 10034: case 10044: case 10046: case 10058: case 10059: case 10062: case 10064:
                goto LABEL_1036920e;
            case 10013:
                goto LABEL_10368fa1;
            case 10022:
                goto LABEL_10368e48;
            case 10024:
                goto LABEL_10368ebb;
            case 10063:
                break;
            default:
LABEL_1036920e:
                v91 = a0;
                v91->field_0 = a1;
                v91->field_4 = g_103a3b4c;
                return v91;
            }
        }
        if (a1 == 10004)
        {
            v37 = sub_10368cf0();
            v38 = a0;
            v38->field_0 = 4;
            v38->field_4 = v37;
            return v38;
        }
        if (a1 > 1013)
        {
            v32 = a1 - 1237;
            if (a1 == 1237)
                goto LABEL_10368e8d;
            if (v32 != 1164)
                if (v32 == 1167)
                    goto LABEL_10368f56;
                else
                    goto LABEL_1036920e;
        }
        else if (a1 != 1013)
        {
            switch (a1)
            {
            case 0:
                v28 = sub_10368cf0();
                v29 = a0;
                v29->field_0 = 9927;
                v29->field_4 = v28;
                return v29;
            case 1: case 2: case 4: case 5: case 6: case 7: case 8: case 9: case 10: case 11: case 12: case 13: case 14: case 15:
                goto LABEL_1036920e;
            case 3:
                goto LABEL_10368fa1;
            case 16: case 17:
                break;
            }
        }
    }
}
```

## `sub_10369420` `0x10369420`

_178 bytes. refs "error: should never be called"_

```c
typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

extern unsigned int g_1038e180;
extern struct_0 g_103a3afc;
extern char g_103a3b00;
extern unsigned int g_103a3b10;
extern unsigned int g_103a3b14;
extern void g_103a3b18;

struct_0 * sub_10369420(struct_0 *idx)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4176
    unsigned int v10;  // ecx
    unsigned long v11;  // 4180
    unsigned long v12;  // 4119
    unsigned int v0;  // [bp-0x1c]
    char v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    unsigned int v5;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1037181e;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v3 = *((int *)v9);
    v2 = v10;
    v0 = g_1038e180 ^ &v1;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v3;
    v2 = 0;
    if (!(1 & g_103a3b18))
    {
        *((unsigned int *)&g_103a3b18) = *((int *)&g_103a3b18) | 1;
        v5 = 0;
        g_103a3b14 = 15;
        g_103a3b10 = 0;
        g_103a3b00 = 0;
        sub_10314830(&g_103a3afc.padding_0[0], "error: should never be called", 29);
        sub_10353c80(sub_10373e80);
        v5 = 4294967295;
    }
    idx->field_18 = 15;
    *((unsigned int *)&idx->padding_0[20]) = 0;
    idx->padding_0[4] = 0;
    sub_10314660(idx, &g_103a3afc.padding_0[0], 0, -1);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v3;
    return idx;
}
```

## `sub_103694e0` `0x103694e0`

_300 bytes. refs "Unknown error"_

```c
typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

extern unsigned int g_1038e180;
extern struct_0 g_103a3b1c;
extern char g_103a3b20;
extern unsigned int g_103a3b30;
extern unsigned int g_103a3b34;
extern void g_103a3b38;

struct_0 * sub_103694e0(struct_0 *idx, int a1)
{
    unsigned long v11;  // ldt
    unsigned long v12;  // gdt
    struct_0 *v21;  // eax
    unsigned long v22;  // 4119
    unsigned short v13;  // fs
    unsigned long v14;  // 4175
    unsigned long v15;  // 4179
    char v16;  // bl
    char *v17;  // eax
    char *v18;  // ecx
    char *v19;  // ecx
    char *v20;  // ecx
    unsigned int v0;  // [bp-0x3c]
    unsigned int v1;  // [bp-0x38]
    char v2;  // [bp-0x34]
    unsigned int v3;  // [bp-0x2c]
    struct_0 v4;  // [bp-0x28]
    unsigned int v5;  // [bp-0x24]
    unsigned int v6;  // [bp-0x14]
    unsigned int v7;  // [bp-0x10]
    unsigned int v8;  // [bp-0xc]
    unsigned int v9;  // [bp-0x8]
    char v10;  // [bp-0x4], Other Possible Types: unsigned int

    v10 = 4294967295;
    v9 = sub_10371880;
    v14 = _ccall(v11, v12, (unsigned int)v13, 0);
    v8 = *((int *)v14);
    v1 = g_1038e180 ^ &v2;
    v15 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int **)v15) = &v8;
    v16 = 0;
    v3 = 0;
    if (!(g_103a3b38 & 1))
    {
        *((unsigned int *)&g_103a3b38) = *((int *)&g_103a3b38) | 1;
        v10 = 1;
        g_103a3b34 = 15;
        g_103a3b30 = 0;
        g_103a3b20 = 0;
        sub_10314830(&g_103a3b1c.padding_0[0], "Unknown error", 13);
        sub_10353c80(sub_10373eb0);
        v10 = 0;
    }
    v17 = sub_10369d4f(a1);
    if (v17)
    {
        v18 = v17;
        v7 = 15;
        v6 = 0;
        *((char *)&v5) = 0;
        v19 = v18;
        do
        {
            v19 += 1;
        } while (*(v19));
        sub_10314830(&v4, v17, v20 - (v18 + 1));
        v16 = 1;
        v21 = &v4;
        v10 = 2;
        v3 = 1;
    }
    else
    {
        v21 = &g_103a3b1c.padding_0[0];
    }
    idx->field_18 = 15;
    *((unsigned int *)&idx->padding_0[20]) = 0;
    idx->padding_0[4] = 0;
    sub_10314660(idx, v21, 0, -1);
    if (((char)(v16 | 2) & 1) && v7 >= 16)
    {
        v0 = v5;
        sub_10350abd();
    }
    v22 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int *)v22) = v8;
    return idx;
}
```

## `sub_10369610` `0x10369610`

_450 bytes. refs "Unknown error"_

```c
typedef struct struct_0 {
    char padding_0[24];
    int field_18;
} struct_0;

typedef struct struct_2 {
    struct struct_2 *field_0;
} struct_2;

extern struct_0 *g_1038b154;
extern struct_0 *g_1038b158;
extern unsigned int g_1038e180;

int sub_10369610(struct_0 *idx, unsigned int a1)
{
    unsigned long v14;  // ldt
    unsigned long v15;  // gdt
    char *v24;  // eax
    unsigned int v25;  // eax
    unsigned int v26;  // esi
    struct_2 **v27;  // ecx
    unsigned int v29;  // esi
    struct_2 **v30;  // ecx
    unsigned int v32;  // esi
    unsigned short v16;  // fs
    unsigned long v33;  // 4121
    unsigned long v17;  // 4164
    unsigned int v18;  // edi
    unsigned long v19;  // 4188
    unsigned int v20;  // esi
    unsigned int v21;  // ebx
    char *v22;  // eax
    char *v23;  // eax
    unsigned int v0;  // [bp-0x6c]
    struct_0 v1;  // [bp-0x4c]
    struct_2 **v2;  // [bp-0x48]
    char v3;  // [bp-0x44]
    unsigned int v4;  // [bp-0x44]
    char v5;  // [bp-0x38]
    struct_0 *v6;  // [bp-0x34], Other Possible Types: unsigned int
    unsigned int v7;  // [bp-0x30]
    unsigned int v8;  // [bp-0x2c]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x10]
    unsigned int v11;  // [bp-0xc]
    unsigned int v12;  // [bp-0x8]
    unsigned int v13;  // [bp-0x4]

    v13 = 4294967295;
    v12 = sub_103718c1;
    v17 = _ccall(v14, v15, (unsigned int)v16, 0);
    v11 = *((int *)v17);
    v10 = g_1038e180 ^ &v5;
    v4 = v18;
    v2 = g_1038e180 ^ &v4;
    v19 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int **)v19) = &v11;
    v1 = (struct_0)0;
    v6 = idx;
    v7 = 0;
    if (!g_1038b154(0x1300, 0, a1, 0x400, &v5, 0, 0, g_1038e180 ^ &v4, v18, v20, v21))
    {
        idx->field_18 = 15;
        *((unsigned int *)&idx->padding_0[20]) = 0;
        idx->padding_0[4] = 0;
        sub_10314830(idx, "Unknown error", 13);
    }
    else
    {
        v22 = &v5;
        v7 = 15;
        v6 = 0;
        v3 = 0;
        v23 = v22;
        do
        {
            v23 += 1;
        } while (*(v23));
        sub_10314830(&v2, v22, v24 - (v22 + 1));
        v9 = 1;
        g_1038b158(&v5);
        v25 = v5;
        if (v25)
        {
            do
            {
                v26 = v25 - 1;
                if (v26 > v25)
                {
                    sub_10353616();
                    v25 = v5;
                }
                v27 = v2;
                if (v6 < 16)
                    v27 = &v2;
                if (*((char *)v27 + v26) == 10)
                    continue;
                v29 = v25 - 1;
                if (v29 > v25)
                {
                    sub_10353616();
                    v25 = v5;
                }
                v30 = v2;
                if (v6 < 16)
                    v30 = &v2;
                if (*((char *)v30 + v29) != 13 && v25)
                {
                    v32 = v25 - 1;
                    if (v32 > v25)
                    {
                        sub_10353616();
                        v25 = v5;
                    }
                    if (v6 < 16)
                        v2 = &v2;
                    if (*((char *)v2 + v32) == 46)
                    {
                        sub_103148c0(&v1, v25 - 1, 4294967295);
                        break;
                    }
                }
            } while ((sub_103148c0(&v1, v25 - 1, 4294967295), v25 = (unsigned int)v5, v25));
        }
        idx->field_18 = 15;
        *((unsigned int *)&idx->padding_0[20]) = 0;
        idx->padding_0[4] = 0;
        sub_10314660(idx, &v1, 0, -1);
        if (v6 >= 16)
        {
            v0 = g_1038e180 ^ &v3;
            sub_10350abd();
        }
    }
    v33 = _ccall(v14, v15, (unsigned int)v16, 0);
    *((unsigned int *)v33) = v8;
    return sub_10351225();
}
```

## `sub_103697e0` `0x103697e0`

_11 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    unsigned int field_8;
} struct_0;

extern char g_103905f0;

void sub_103697e0(struct_0 *a0)
{
    *((char **)&a0->padding_0[0]) = &g_103905f0;
    sub_103532d2(a0);
    return;
}
```

## `sub_103697f0` `0x103697f0`

_25 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
} struct_0;

extern char g_10390664;

struct_0 * sub_103697f0(struct_0 *a0)
{
    sub_10353203(a0);
    a0->field_c = 0;
    *((char **)&a0->padding_0[0]) = &g_10390664;
    return a0;
}
```

## `sub_10369810` `0x10369810`

_6 bytes. refs "boost::lock_error"_

```c
int sub_10369810(void)
{
    return "boost::lock_error";
}
```

## `sub_10369820` `0x10369820`

_25 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
} struct_0;

extern char g_103905e4;

struct_0 * sub_10369820(struct_0 *a0)
{
    sub_10353203(a0);
    a0->field_c = 0;
    *((char **)&a0->padding_0[0]) = &g_103905e4;
    return a0;
}
```

## `sub_10369840` `0x10369840`

_6 bytes. refs "boost::thread_resource_error"_

```c
int sub_10369840(void)
{
    return "boost::thread_resource_error";
}
```

## `sub_10369850` `0x10369850`

_13 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10369850(void)
{
    return 0;
}
```

## `sub_10369860` `0x10369860`

_21 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10369860(void)
{
    sub_10353c80(sub_10369d20);
    sub_10369920();
    return 0;
}
```

## `sub_10369880` `0x10369880`

_8 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10369880(void)
{
    sub_10369930();
    return 0;
}
```

## `sub_10369890` `0x10369890`

_15 bytes. (leaf/helper — see body)_

```c
void sub_10369890(unsigned int a0, unsigned int a1)
{
    if (a1 == 3)
        sub_10369d20();
    return;
}
```

## `sub_103698a0` `0x103698a0`

_39 bytes. (leaf/helper — see body)_

```c
unsigned int sub_103698a0(unsigned int a0, unsigned int a1)
{
    if (!a1)
    {
        sub_10369930();
        return 1;
    }
    if (a1 != 3)
        return 1;
    sub_10369d20();
    return 1;
}
```

## `sub_103698d0` `0x103698d0`

_19 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b128;

unsigned int sub_103698d0(unsigned int *a0)
{
    unsigned int v1;  // eax

    v1 = *(a0);
    if (v1 && v1 != 4294967295)
        v1 = g_1038b128(v1);
    return v1;
}
```

## `sub_103698f0` `0x103698f0`

_10 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b090;

int sub_103698f0(unsigned int *a0)
{
    return g_1038b090(*(a0));
}
```

## `sub_10369900` `0x10369900`

_17 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b238;
extern unsigned int g_103a3b5c;

void sub_10369900(void)
{
    sub_10369920();
    g_103a3b5c = g_1038b238();
    return;
}
```

## `sub_10369920` `0x10369920`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10369920(void)
{
    return;
}
```

## `sub_10369930` `0x10369930`

_27 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b240;
extern unsigned int g_103a3b5c;

unsigned int sub_10369930(void)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax

    v1 = g_103a3b5c;
    if (!v1)
        return v1;
    v2 = g_1038b240(v1);
    g_103a3b5c = 0;
    return v2;
}
```

## `sub_10369950` `0x10369950`

_117 bytes. (leaf/helper — see body)_

```c
int sub_10369950(int a0, char *idx)
{
    char v0;  // al
    unsigned int v1;  // eax

    *(idx) = ((char)a0 & 15) + 65;
    idx[1] = ((char)(a0 >> 4) & 15) + 65;
    idx[2] = ((char)(a0 >> 8) & 15) + 65;
    idx[3] = ((char)(a0 >> 12) & 15) + 65;
    idx[4] = ((char)(a0 >> 16) & 15) + 65;
    idx[5] = ((char)(a0 >> 20) & 15) + 65;
    v0 = a0 >> 28;
    v1 = _INSERT(v0, 0, (v0 & 15) + 65);
    idx[6] = ((char)(a0 >> 24) & 15) + 65;
    idx[7] = (v0 & 15) + 65;
    idx[8] = 0;
    return v1;
}
```

## `sub_103699d0` `0x103699d0`

_117 bytes. (leaf/helper — see body)_

```c
int sub_103699d0(unsigned int a0, char *idx)
{
    char v0;  // al
    unsigned int v1;  // eax

    *(idx) = ((char)a0 & 15) + 65;
    idx[1] = ((char)(a0 >> 4) & 15) + 65;
    idx[2] = ((char)(a0 >> 8) & 15) + 65;
    idx[3] = ((char)(a0 >> 12) & 15) + 65;
    idx[4] = ((char)(a0 >> 16) & 15) + 65;
    idx[5] = ((char)(a0 >> 20) & 15) + 65;
    v0 = a0 >> 28;
    v1 = _INSERT(v0, 0, (v0 & 15) + 65);
    idx[6] = ((char)(a0 >> 24) & 15) + 65;
    idx[7] = (v0 & 15) + 65;
    idx[8] = 0;
    return v1;
}
```

## `sub_10369a50` `0x10369a50`

_103 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b098;
extern struct_0 *g_1038b1c8;
extern unsigned int g_1038e180;

int sub_10369a50(int a0)
{
    unsigned int v6;  // esi
    unsigned int v7;  // edi
    unsigned int v8;  // ecx
    void* i;  // esi
    void* iter;  // edi
    unsigned int v0;  // [bp-0x50]
    unsigned int v1;  // [bp-0x4c]
    char v2;  // [bp-0x48]
    char v3[8];  // [bp-0x18]
    char v4[12];  // [bp-0x10]
    unsigned int v5;  // [bp-0x4]

    v5 = g_1038e180 ^ &v2;
    v1 = v6;
    v0 = v7;
    v8 = 12;
    i = "{C15730E2-145C-4c5e-B005-3BC753F42475}-once-flag";
    for (iter = &v2; v8; i += 4)
    {
        v8 -= 1;
        *((int *)iter) = *((int *)i);
        iter += 4;
    }
    *((char *)iter) = *((char *)i);
    sub_10369950(a0, v3);
    sub_103699d0(g_1038b1c8(v4), v4);
    g_1038b098(0, 0, &v2);
    return sub_10351225(&v2);
}
```

## `sub_10369ac0` `0x10369ac0`

_47 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    struct struct_2 *field_0;
    unsigned int field_4;
} struct_1;

typedef struct struct_2 {
    struct struct_0 *field_0;
} struct_2;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b204;
extern struct_0 *g_1038b224;

unsigned int sub_10369ac0(struct_1 **a0)
{
    unsigned int v2;  // esi
    struct_1 *v3;  // esi
    unsigned int v4;  // eax
    unsigned int v5;  // eax
    unsigned int v6;  // eax
    unsigned int v0;  // [bp-0x4]

    v0 = v2;
    v3 = *(a0);
    if (!v3)
        return v6;
    v4 = &v3->field_4;
    InterlockedExchangeAdd(v4, 4294967295);
    if (*((int *)v4) != 1)
        return v4;
    v3->field_0->field_0(0);
    v5 = g_1038b224(0, v3);
    return g_1038b204(v5);
}
```

## `sub_10369af0` `0x10369af0`

_162 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b090;
extern struct_0 *g_1038b094;
extern struct_0 *g_1038b128;
extern unsigned int g_1038e180;

unsigned int sub_10369af0(unsigned int *a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned int v17;  // edi
    unsigned short v9;  // fs
    unsigned long v10;  // 4173
    unsigned int v11;  // ecx
    unsigned int v12;  // esi
    unsigned long v13;  // 4177
    unsigned int v14;  // eax
    int v15;  // esi
    unsigned long v16;  // 4118
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x14]
    int v2;  // [bp-0x10], Other Possible Types: unsigned int
    unsigned int v3;  // [bp-0xc], Other Possible Types: char
    unsigned int v4;  // [bp-0x8]
    unsigned int v5;  // [bp-0x4]
    unsigned int *v6;  // [bp+0x0]

    v5 = 4294967295;
    v4 = sub_10371900;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v2 = v11;
    v1 = v12;
    v0 = g_1038e180 ^ &v17;
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v13) = &v3;
    v14 = *(a0);
    if (*(a0) != 3243716834)
    {
        v15 = sub_10369a50(a0);
        a0 = v15;
        v5 = 0;
        v2 = v15;
        g_1038b094(v15, 4294967295);
        v3 = 1;
        if (*(a0) != 3243716834)
        {
            v6();
            InterlockedExchange(a0, 3243716834);
        }
        v3 = 0;
        v14 = g_1038b090(v15);
        v2 = 4294967295;
        if (v15 && v15 != -1)
            v14 = g_1038b128(v15);
    }
    v16 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v16) = v17;
    return v14;
}
```

## `sub_10369ba0` `0x10369ba0`

_370 bytes. (leaf/helper — see body)_

```c
typedef struct struct_14 {
    struct struct_5 *field_0;
    char padding_4[12];
    struct struct_4 *field_10;
    struct struct_11 *field_14;
} struct_14;

typedef struct struct_5 {
    struct struct_1 *field_0;
} struct_5;

typedef struct struct_4 {
    struct struct_5 *field_0;
    unsigned int field_4;
} struct_4;

typedef struct struct_11 {
    char padding_0[4];
    struct struct_5 *field_4;
    struct struct_5 *field_8;
    unsigned int field_c;
    unsigned int field_10;
} struct_11;

typedef struct struct_1 {
    struct struct_0 *field_0;
    struct struct_0 *field_4;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b204;
extern struct_0 *g_1038b224;
extern struct_0 *g_1038b234;
extern struct_0 *g_1038b23c;
extern unsigned int g_1038e180;
extern unsigned int g_103a3b58;
extern struct_14 *g_103a3b5c;

struct_14 * sub_10369ba0(void)
{
    unsigned long v11;  // ldt
    unsigned long v12;  // gdt
    unsigned int v21;  // ebx
    unsigned int v22;  // eax
    unsigned int v23;  // eax
    unsigned int index;  // edi
    unsigned int v25;  // ebx
    unsigned int v26;  // eax
    unsigned int v27;  // ecx
    unsigned int v28;  // eax
    struct_14 *v29;  // ecx
    unsigned int v30;  // eax
    unsigned short v13;  // fs
    unsigned long v31;  // 4122
    unsigned long v14;  // 4177
    unsigned int v15;  // ecx
    unsigned int v16;  // ebx
    unsigned int v17;  // esi
    unsigned long v18;  // 4181
    struct_14 *v19;  // eax
    struct_14 *idx;  // esi
    unsigned int v0;  // [bp-0x48]
    unsigned int v1;  // [bp-0x44]
    unsigned int v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x24]
    unsigned int v4;  // [bp-0x1c]
    struct_14 *v5;  // [bp-0x14], Other Possible Types: unsigned int
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]
    unsigned int v9;  // [bp-0x4]

    v9 = 4294967295;
    v8 = sub_10371928;
    v14 = _ccall(v11, v12, (unsigned int)v13, 0);
    v7 = *((int *)v14);
    v6 = v15;
    v5 = v16;
    v4 = v17;
    v3 = g_1038e180 ^ &/* unsupported instruction */;
    v18 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int **)v18) = &v7;
    v19 = g_103a3b5c;
    if (!g_103a3b5c)
    {
        idx = NULL;
    }
    else
    {
        v19 = g_1038b234(g_103a3b5c);
        idx = v19;
    }
    v5 = idx;
    v8 = 0;
    if (idx)
    {
        while (true)
        {
            if (idx->field_14)
                if (!idx->field_10)
                    goto LABEL_10369ca5;
                else
                    goto LABEL_10369c65;
            do
            {
                if (!idx->field_10)
                {
                    v0 = sub_10369900;
                    sub_10369af0(&g_103a3b58);
                    v19 = g_1038b23c(g_103a3b5c, 0);
                    goto LABEL_10369c1d;
                }
                do
                {
LABEL_10369c65:
                    v21 = idx->field_10;
                    idx->field_10 = *((int *)(v21 + 4));
                    if (*((int *)v21))
                    {
                        (*((int *)(*((int *)*((int *)v21)) + 4)))();
                        (*((int *)*((int *)*((int *)v21))))(0);
                        v22 = g_1038b224(0, *((int *)v21));
                        g_1038b204(v22);
                    }
                    v23 = g_1038b224(0, v21);
                    g_1038b204(v23);
                } while (idx->field_10);
LABEL_10369ca5:
            } while (!idx->field_14);
            do
            {
                index = idx->field_14;
                idx->field_14 = *((int *)(index + 16));
                if (*((int *)(index + 4)))
                    (*((int *)(*((int *)*((int *)(index + 4))) + 4)))(*((int *)(index + 12)));
                v25 = *((int *)(index + 8));
                if (v25)
                {
                    v26 = v25 + 4;
                    InterlockedExchangeAdd(v26, 4294967295);
                    if (*((int *)v26) == 1)
                    {
                        (*((int *)(*((int *)v25) + 4)))();
                        v27 = v25 + 8;
                        InterlockedExchangeAdd(v27, 4294967295);
                        if (*((int *)v27) == 1)
                            (*((int *)(*((int *)v25) + 8)))();
                    }
                }
                v28 = g_1038b224(0, index);
                g_1038b204(v28);
            } while (idx->field_14);
        }
    }
LABEL_10369c1d:
    v2 = 4294967295;
    if (idx)
    {
        v29 = idx->padding_4;
        InterlockedExchangeAdd(v29, 4294967295);
        if (v29->field_0 == 1)
        {
            idx->field_0->field_0(0);
            v30 = g_1038b224(0, idx);
            v19 = g_1038b204(v30);
        }
    }
    v31 = _ccall(v11, v12, (unsigned int)v13, 0);
    *((unsigned int *)v31) = v1;
    return v19;
}
```

## `sub_10369d20` `0x10369d20`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_14 {
    struct struct_5 *field_0;
    char padding_4[12];
    struct struct_4 *field_10;
    struct struct_11 *field_14;
} struct_14;

typedef struct struct_5 {
    struct struct_1 *field_0;
} struct_5;

typedef struct struct_4 {
    struct struct_5 *field_0;
    unsigned int field_4;
} struct_4;

typedef struct struct_11 {
    char padding_0[4];
    struct struct_5 *field_4;
    struct struct_5 *field_8;
    unsigned int field_c;
    unsigned int field_10;
} struct_11;

typedef struct struct_1 {
    struct struct_0 *field_0;
    struct struct_0 *field_4;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

struct_14 * sub_10369d20(void)
{
    return sub_10369ba0();
}
```

## `sub_10369d26` `0x10369d26`

_6 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038b1fc;

void sub_10369d26(void)
{
    goto g_1038b1fc;
}
```

## `sub_10369d2c` `0x10369d2c`

_35 bytes. (leaf/helper — see body)_

```c
int sub_10369d2c(int a0)
{
    int v1;  // esi
    int v0;  // [bp-0x4]

    v1 = a0;
    if (v1 < 0 || v1 >= *((int *)sub_10369db6(v0)))
        v1 = *((int *)sub_10369db6(v0));
    return *((int *)(sub_10369dbc() + v1 * 4));
}
```

## `sub_10369d4f` `0x10369d4f`

_103 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10369d4f(int a0)
{
    void* idx;  // esi
    unsigned int v7;  // edi
    unsigned int v8;  // eax
    unsigned int v9;  // eax
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]

    idx = sub_10358d31();
    if (!idx)
        return "Visual C++ CRT: Not enough memory to complete call to strerror.";
    v5 = v7;
    if (!(int)idx[36] && !((v8 = sub_103574c2(134, 1), *((unsigned int *)&idx[36]) = v8, v8)))
    {
        v9 = "Visual C++ CRT: Not enough memory to complete call to strerror.";
    }
    else
    {
        if (sub_10359f58((int)idx[36], 134, sub_10369d2c(a0)))
        {
            v4 = 0;
            v3 = 0;
            v2 = 0;
            v1 = 0;
            v0 = 0;
            sub_103534f6();
        }
        v9 = (int)idx[36];
    }
    return v9;
}
```

## `sub_10369db6` `0x10369db6`

_6 bytes. (leaf/helper — see body)_

```c
int sub_10369db6(void)
{
    return "+";
}
```

## `sub_10369dbc` `0x10369dbc`

_6 bytes. (leaf/helper — see body)_

```c
extern char g_1038f638;

int sub_10369dbc(void)
{
    return &g_1038f638;
}
```

## `sub_10369dd0` `0x10369dd0`

_8 bytes. (leaf/helper — see body)_

```c
int sub_10369dd0(void)
{
    return sub_102ee0a0(/* unsupported instruction */ - 40);
}
```

## `sub_10369dd8` `0x10369dd8`

_27 bytes. (leaf/helper — see body)_

```c
int sub_10369dd8(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_10369e00` `0x10369e00`

_11 bytes. (leaf/helper — see body)_

```c
void sub_10369e00(void)
{
    unsigned int v0;  // [bp-0x4]
    unsigned int v2;  // [bp+0xfffec]

    v0 = v2;
    sub_10350abd();
    return;
}
```

## `sub_10369e0b` `0x10369e0b`

_27 bytes. (leaf/helper — see body)_

```c
int sub_10369e0b(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_10369e26` `0x10369e26`

_11 bytes. (leaf/helper — see body)_

```c
void sub_10369e26(void)
{
    unsigned int v0;  // [bp-0x4]
    unsigned int v2;  // [bp+0xfffec]

    v0 = v2;
    sub_10350abd();
    return;
}
```

## `sub_10369e31` `0x10369e31`

_27 bytes. (leaf/helper — see body)_

```c
int sub_10369e31(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_10369e4c` `0x10369e4c`

_8 bytes. (leaf/helper — see body)_

```c
int sub_10369e4c(void)
{
    return sub_103126c0(/* unsupported instruction */ - 48);
}
```

