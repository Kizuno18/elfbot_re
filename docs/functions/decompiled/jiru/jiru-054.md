# elfbot.dll decompiled — jiru 0x10345240..0x10347550

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10345240` `0x10345240`

_568 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern unsigned int g_1038e180;

struct_0 ** sub_10345240(struct_0 **a0, char a1)
{
    unsigned long v18;  // ldt
    unsigned long v19;  // gdt
    unsigned long v28;  // 4123
    unsigned short v20;  // fs
    unsigned long v21;  // 4148
    unsigned int v22;  // ecx
    unsigned long v23;  // 4170
    int v24;  // edi
    int v25;  // esi
    int v26;  // ebx
    int v27;  // ecx
    int v0;  // [bp-0x68]
    char *v1;  // [bp-0x64]
    int v2;  // [bp-0x60]
    unsigned int v3;  // [bp-0x54]
    int v4;  // [bp-0x44]
    unsigned int v5;  // [bp-0x3c]
    unsigned int v6;  // [bp-0x38]
    unsigned int v7;  // [bp-0x34]
    unsigned int v8;  // [bp-0x30]
    unsigned int v9;  // [bp-0x2c]
    unsigned int v10;  // [bp-0x28]
    int iter;  // [bp-0x24]
    unsigned int v12;  // [bp-0x18]
    char *v13;  // [bp-0x14], Other Possible Types: unsigned int
    unsigned int v14;  // [bp-0x10]
    unsigned int v15;  // [bp-0xc]
    char v16;  // [bp-0x8], Other Possible Types: unsigned int
    char v17;  // [bp-0x4]

    v16 = 4294967295;
    v15 = sub_10370c58;
    v21 = _ccall(v18, v19, (unsigned int)v20, 0);
    v14 = *((int *)v21);
    v13 = v22;
    v3 = g_1038e180 ^ &v17;
    v23 = _ccall(v18, v19, (unsigned int)v20, 0);
    *((unsigned int **)v23) = &v14;
    v13 = &v3;
    v12 = 0;
    sub_103454a0(a0, g_1038e180 ^ &v17, v24, v25, v26);
    v16 = 0;
    if ((char)sub_103455c0(a0, g_1038e180 ^ &v17, v24, v25, v26))
    {
        v4 = (sub_103451d0((char *)a0 + *(a0)->field_4) <= 1 ? 0 : sub_103451d0((char *)a0 + *(a0)->field_4) - 1);
        iter = v4;
        if (((short)sub_10315ef0((char *)a0 + *(a0)->field_4) & 448) != 64)
        {
            for (v16 = 1; !v12 && iter > 0; iter -= 1)
            {
                v2 = sub_10345220((char *)a0 + *(a0)->field_4);
                v10 = sub_1033ed20(sub_10315c20((char *)a0 + *(a0)->field_4));
                v9 = sub_1032fd20();
                if ((char)sub_10312db0(&v9, &v10))
                    v12 |= 4;
            }
        }
        if (!v12)
        {
            v27 = _INSERT(0, 0, a1);
            v2 = v27;
            v8 = sub_1033ed20(sub_10315c20((char *)a0 + *(a0)->field_4));
            v7 = sub_1032fd20();
            v1 = &v8;
            if ((char)sub_10312db0(&v7, &v8))
                v12 |= 4;
        }
        for (; !v12 && iter > 0; iter -= 1)
        {
            v0 = sub_10345220((char *)a0 + *(a0)->field_4);
            v6 = sub_1033ed20(sub_10315c20((char *)a0 + *(a0)->field_4));
            v5 = sub_1032fd20();
            if ((char)sub_10312db0(&v5, &v6))
                v12 |= 4;
        }
        v16 = 0;
    }
    sub_103451f0((char *)a0 + *(a0)->field_4, 0);
    sub_10314630((char *)a0 + *(a0)->field_4, v12, 0);
    v16 = 4294967295;
    sub_10345550(v1, v27);
    v28 = _ccall(v18, v19, (unsigned int)v20, 0);
    *((unsigned int *)v28) = v14;
    return a0;
}
```

## `sub_1034541d` `0x1034541d`

_33 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

int sub_1034541d(void)
{
    unsigned int v1;  // [bp+0x100000]
    struct_0 **v2;  // [bp+0x10000c]

    sub_10314630((char *)v2 + *(v2)->field_4, 4, 1);
    v1 = 0;
    return "j";
}
```

## `sub_103454a0` `0x103454a0`

_176 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    char field_4;
} struct_0;

typedef struct struct_1 {
    char padding_0[4];
    unsigned int field_4;
} struct_1;

extern unsigned int g_1038e180;

struct_0 * sub_103454a0(struct_0 *a0, struct_1 **a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4154
    unsigned long v12;  // 4128
    unsigned int v0;  // [bp-0x18]
    struct_0 *v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_10370c88;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_10316050(v1, a1);
    v4 = 0;
    if ((char)sub_10315ed0((char *)a1 + *(a1)->field_4) && sub_10316170((char *)a1 + *(a1)->field_4))
        sub_10315f10(sub_10316170((char *)a1 + *(a1)->field_4));
    v1->field_4 = sub_10315ed0((char *)a1 + *(a1)->field_4);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v2;
    return v1;
}
```

## `sub_10345550` `0x10345550`

_97 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10345550(int a0)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4135
    unsigned int v10;  // eax
    unsigned long v11;  // 4151
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
    if (!(char)sub_10350973(g_1038e180 ^ &v3, a0, v10, sub_10370cb8, 0, &v4))
        sub_103455e0();
    v2 = 4294967295;
    v12 = sub_10345660();
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v10;
    return v12;
}
```

## `sub_103455c0` `0x103455c0`

_17 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    char field_4;
} struct_0;

int sub_103455c0(struct_0 *a0)
{
    return _INSERT(a0, 0, a0->field_4);
}
```

## `sub_103455e0` `0x103455e0`

_110 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern unsigned int g_1038e180;

unsigned int sub_103455e0(struct_0 **a0)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4151
    unsigned long v12;  // 4175
    int v13;  // eax
    unsigned int v14;  // eax
    unsigned long v15;  // 4122
    unsigned int v0;  // [bp-0x28]
    struct_0 **v1;  // [bp-0x18]
    char *v2;  // [bp-0x14], Other Possible Types: struct_0 **
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_10370ce0;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v3 = *((int *)v11);
    v2 = a0;
    v1 = a0;
    v0 = g_1038e180 ^ &v6;
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v3;
    v2 = &v0;
    v1 = a0;
    v5 = 0;
    v13 = sub_10315ef0((char *)v1 + *(v1)->field_4);
    v14 = v13 & 2;
    if (((char)v13 & 2))
        v14 = sub_10315f10(v1);
    v15 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v15) = v3;
    return v14;
}
```

## `sub_10345635` `0x10345635`

_13 bytes. (leaf/helper — see body)_

```c
extern char g_10345649;

int sub_10345635(void)
{
    unsigned int v1;  // [bp+0x100000]

    v1 = 4294967295;
    return &g_10345649;
}
```

## `sub_10345660` `0x10345660`

_62 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

int sub_10345660(struct_1 **a0)
{
    unsigned int v2;  // eax
    struct_1 **v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    v2 = sub_10315c20((char *)*(v0) + *(v0)->field_0->field_4);
    if (!v2)
        return v2;
    return (unsigned int)sub_10316110(sub_10315c20((char *)*(v0) + *(v0)->field_0->field_4));
}
```

## `sub_103456a0` `0x103456a0`

_1624 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[92];
    int field_5c;
    unsigned int field_60;
} struct_0;

extern unsigned int g_1038e180;

void sub_103456a0(int a0, struct_0 *idx, unsigned int a2, unsigned int a3, int a4)
{
    unsigned long v43;  // ldt
    unsigned long v44;  // gdt
    char v55;  // al
    char v56;  // al
    char *v57;  // eax
    unsigned long v59;  // 4115
    unsigned short v45;  // fs
    unsigned long v46;  // 4142
    unsigned long v47;  // 4158
    int v48;  // esi
    char v49;  // al
    char v50;  // al
    unsigned int *v51;  // eax
    unsigned int v52;  // ecx
    char *v0;  // [bp-0x138]
    int v1;  // [bp-0x134]
    int v2;  // [bp-0x12c]
    char *v3;  // [bp-0x128], Other Possible Types: unsigned int
    int v4;  // [bp-0x124], Other Possible Types: unsigned int
    char *v5;  // [bp-0x108]
    char *v6;  // [bp-0x104]
    char *v7;  // [bp-0x100]
    char *v8;  // [bp-0xfc]
    int v9;  // [bp-0xf8]
    char *v10;  // [bp-0xf4]
    char *v11;  // [bp-0xf0]
    char v12;  // [bp-0xe9]
    char *v13;  // [bp-0xe8]
    int v14;  // [bp-0xe4]
    unsigned int v15;  // [bp-0xe0]
    int v16;  // [bp-0xdc]
    unsigned int v17;  // [bp-0xd8]
    unsigned int v18;  // [bp-0xd4]
    unsigned int v19;  // [bp-0xd0]
    int v20;  // [bp-0xcc]
    int v21;  // [bp-0xc8]
    int i;  // [bp-0xc4]
    char *v23;  // [bp-0xc0]
    int v24;  // [bp-0xbc]
    char v25;  // [bp-0xb8]
    char v26;  // [bp-0xb0]
    char v27;  // [bp-0x75]
    char *v28;  // [bp-0x74], Other Possible Types: unsigned int
    int v29;  // [bp-0x70]
    char v30;  // [bp-0x69]
    char *v31;  // [bp-0x68]
    unsigned int v32;  // [bp-0x64]
    int v33;  // [bp-0x60]
    char v34;  // [bp-0x5a]
    char v35;  // [bp-0x59]
    char v36;  // [bp-0x58]
    char v37;  // [bp-0x50]
    int v38;  // [bp-0x14]
    unsigned int v39;  // [bp-0x10]
    unsigned int v40;  // [bp-0xc]
    char v41;  // [bp-0x8], Other Possible Types: unsigned int
    char v42;  // [bp-0x4]

    v41 = 4294967295;
    v40 = sub_10370d13;
    v46 = _ccall(v43, v44, (unsigned int)v45, 0);
    v39 = *((int *)v46);
    v47 = _ccall(v43, v44, (unsigned int)v45, 0);
    *((unsigned int **)v47) = &v39;
    sub_103470c0(a3, 1, g_1038e180 ^ &v42, v48);
    v41 = 0;
    v14 = (!&v36 ? NULL : &(&v37)[*((int *)(v37 + 4))]);
    sub_10347290(v14, a4);
    v13 = (!&v36 ? NULL : &v37);
    v4 = a0;
    v3 = v13;
    sub_10334530();
    v33 = sub_10315ef0(&(&v37)[*((int *)(v37 + 4))]);
    v35 = (v33 & 0x100);
    v38 = sub_103451d0(&(&v37)[*((int *)(v37 + 4))]);
    if (v35 && v38)
        v12 = 1;
    else
        v12 = 0;
    v34 = v12;
    sub_10343540(a2, 0);
    if (!v34)
    {
        if (v38 > 0)
            sub_103451f0(&(&v37)[*((int *)(v37 + 4))], 0);
        v11 = (!&v36 ? NULL : &v37);
        sub_10347990(v11, a0);
        v31 = sub_1033e670(a3);
        v30 = 0;
        if (((char)idx->field_60 & 2) && (!sub_10346d50() || (v49 = sub_10314ca0(&v37 + *((int *)(v37 + 4)), 43), (int)(char)*(v31) != (int)sub_10314ca0(&v37 + *((int *)(v37 + 4)), 43) && !((v50 = sub_10314ca0(&v37 + *((int *)(v37 + 4)), 45), (int)(char)*(v31) == (int)sub_10314ca0(&v37 + *((int *)(v37 + 4)), 45))))))
            v30 = sub_10314ca0(&(&v37)[*((int *)(v37 + 4))], 32);
        v19 = sub_10346d50();
        v18 = idx->field_5c - -(-(0 < v30));
        v51 = sub_10347830(&v18, &v19);
        v32 = *(v51);
        v52 = _INSERT(*(v51), 0, (idx->field_60 & 4));
        v4 = v52;
        v3 = _INSERT(idx, 0, v30);
        v2 = v33;
        sub_10347860(a2, v31, v32, v38, sub_10345220(&(&v37)[*((int *)(v37 + 4))]));
    }
    else
    {
        v10 = (!&v36 ? NULL : &v37);
        sub_10347990(v10, a0);
        v28 = sub_1033e670(a3);
        v29 = sub_10346d50();
        v27 = 0;
        if (((char)idx->field_60 & 2) && (!sub_10346d50() || (v55 = sub_10314ca0(&v37 + *((int *)(v37 + 4)), 43), (int)(char)*(v28) != (int)sub_10314ca0(&v37 + *((int *)(v37 + 4)), 43) && !((v56 = sub_10314ca0(&v37 + *((int *)(v37 + 4)), 45), (int)(char)*(v28) == (int)sub_10314ca0(&v37 + *((int *)(v37 + 4)), 45))))))
            v27 = 1;
        if (v29 == v38 && v38 <= idx->field_5c && !v27)
        {
            sub_10314830(a2, v28, v29);
        }
        else
        {
            sub_10314830(a2, v28, v29);
            v28 = 0;
            sub_10347790(v14, a4);
            sub_103470c0(a3, 1);
            v41 = 1;
            v9 = (!&v25 ? NULL : &(&v26)[*((int *)(v26 + 4))]);
            sub_10347290(v9, a4);
            v8 = (!&v25 ? NULL : &v26);
            v1 = a0;
            v0 = v8;
            sub_10334530();
            sub_103451f0(&(&v26)[*((int *)(v26 + 4))], 0);
            if (v27)
            {
                v7 = (!&v25 ? NULL : &v26);
                sub_10345240(v7, 32);
            }
            v6 = (!&v25 ? NULL : &v26);
            sub_10347990(v6, a0);
            if (!sub_10346d50() && ((char)idx->field_60 & 2))
            {
                v27 = 1;
                v5 = (!&v25 ? NULL : &v26);
                sub_10345240(v5, 32);
            }
            v23 = sub_1033e670(a3);
            v17 = sub_10346d50();
            v16 = idx->field_5c;
            v24 = *((int *)sub_10347830(&v16, &v17));
            if (v38 <= v24)
            {
                sub_10314830(a2, v23, v24);
            }
            else
            {
                v15 = -(-(0 < v27)) + v29;
                v20 = *((int *)sub_10347830(&v15, &v24));
                for (i = v27; i < v20 && (v57 = (char *)sub_103189a0(a2, i - -(-((unsigned int)(char)(0 < (unsigned int)v27)))), (int)(char)v23[i] == (int)*((char *)sub_103189a0(a2, i - -(-((unsigned int)(char)(0 < (unsigned int)v27)))))); i += 1);
                if (i >= v24)
                    i = v27;
                sub_10314830(a2, v23, i);
                v21 = v38 - v24;
                sub_103170f0(a2, v21, sub_10345220(&(&v26)[*((int *)(v26 + 4))]));
                sub_1031a6b0(a2, &v23[i], v24 - i);
            }
            v41 = 0;
            sub_103469c0();
        }
    }
    sub_10347790();
    v41 = 4294967295;
    sub_103469c0();
    v59 = _ccall(v43, v44, (unsigned int)v45, 0);
    *((unsigned int *)v59) = v39;
    return;
}
```

## `sub_10345d00` `0x10345d00`

_1624 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[92];
    int field_5c;
    unsigned int field_60;
} struct_0;

extern unsigned int g_1038e180;

void sub_10345d00(int a0, struct_0 *idx, unsigned int a2, unsigned int a3, int a4)
{
    unsigned long v43;  // ldt
    unsigned long v44;  // gdt
    char v55;  // al
    char v56;  // al
    char *v57;  // eax
    unsigned long v59;  // 4115
    unsigned short v45;  // fs
    unsigned long v46;  // 4142
    unsigned long v47;  // 4158
    int v48;  // esi
    char v49;  // al
    char v50;  // al
    unsigned int *v51;  // eax
    unsigned int v52;  // ecx
    char *v0;  // [bp-0x138]
    int v1;  // [bp-0x134]
    int v2;  // [bp-0x12c]
    char *v3;  // [bp-0x128], Other Possible Types: unsigned int
    int v4;  // [bp-0x124], Other Possible Types: unsigned int
    char *v5;  // [bp-0x108]
    char *v6;  // [bp-0x104]
    char *v7;  // [bp-0x100]
    char *v8;  // [bp-0xfc]
    int v9;  // [bp-0xf8]
    char *v10;  // [bp-0xf4]
    char *v11;  // [bp-0xf0]
    char v12;  // [bp-0xe9]
    char *v13;  // [bp-0xe8]
    int v14;  // [bp-0xe4]
    unsigned int v15;  // [bp-0xe0]
    int v16;  // [bp-0xdc]
    unsigned int v17;  // [bp-0xd8]
    unsigned int v18;  // [bp-0xd4]
    unsigned int v19;  // [bp-0xd0]
    int v20;  // [bp-0xcc]
    int v21;  // [bp-0xc8]
    int i;  // [bp-0xc4]
    char *v23;  // [bp-0xc0]
    int v24;  // [bp-0xbc]
    char v25;  // [bp-0xb8]
    char v26;  // [bp-0xb0]
    char v27;  // [bp-0x75]
    char *v28;  // [bp-0x74], Other Possible Types: unsigned int
    int v29;  // [bp-0x70]
    char v30;  // [bp-0x69]
    char *v31;  // [bp-0x68]
    unsigned int v32;  // [bp-0x64]
    int v33;  // [bp-0x60]
    char v34;  // [bp-0x5a]
    char v35;  // [bp-0x59]
    char v36;  // [bp-0x58]
    char v37;  // [bp-0x50]
    int v38;  // [bp-0x14]
    unsigned int v39;  // [bp-0x10]
    unsigned int v40;  // [bp-0xc]
    char v41;  // [bp-0x8], Other Possible Types: unsigned int
    char v42;  // [bp-0x4]

    v41 = 4294967295;
    v40 = sub_10370d53;
    v46 = _ccall(v43, v44, (unsigned int)v45, 0);
    v39 = *((int *)v46);
    v47 = _ccall(v43, v44, (unsigned int)v45, 0);
    *((unsigned int **)v47) = &v39;
    sub_103470c0(a3, 1, g_1038e180 ^ &v42, v48);
    v41 = 0;
    v14 = (!&v36 ? NULL : &(&v37)[*((int *)(v37 + 4))]);
    sub_10347290(v14, a4);
    v13 = (!&v36 ? NULL : &v37);
    v4 = a0;
    v3 = v13;
    sub_10334530();
    v33 = sub_10315ef0(&(&v37)[*((int *)(v37 + 4))]);
    v35 = (v33 & 0x100);
    v38 = sub_103451d0(&(&v37)[*((int *)(v37 + 4))]);
    if (v35 && v38)
        v12 = 1;
    else
        v12 = 0;
    v34 = v12;
    sub_10343540(a2, 0);
    if (!v34)
    {
        if (v38 > 0)
            sub_103451f0(&(&v37)[*((int *)(v37 + 4))], 0);
        v11 = (!&v36 ? NULL : &v37);
        sub_10347c50(v11, a0);
        v31 = sub_1033e670(a3);
        v30 = 0;
        if (((char)idx->field_60 & 2) && (!sub_10346d50() || (v49 = sub_10314ca0(&v37 + *((int *)(v37 + 4)), 43), (int)(char)*(v31) != (int)sub_10314ca0(&v37 + *((int *)(v37 + 4)), 43) && !((v50 = sub_10314ca0(&v37 + *((int *)(v37 + 4)), 45), (int)(char)*(v31) == (int)sub_10314ca0(&v37 + *((int *)(v37 + 4)), 45))))))
            v30 = sub_10314ca0(&(&v37)[*((int *)(v37 + 4))], 32);
        v19 = sub_10346d50();
        v18 = idx->field_5c - -(-(0 < v30));
        v51 = sub_10347830(&v18, &v19);
        v32 = *(v51);
        v52 = _INSERT(*(v51), 0, (idx->field_60 & 4));
        v4 = v52;
        v3 = _INSERT(idx, 0, v30);
        v2 = v33;
        sub_10347860(a2, v31, v32, v38, sub_10345220(&(&v37)[*((int *)(v37 + 4))]));
    }
    else
    {
        v10 = (!&v36 ? NULL : &v37);
        sub_10347c50(v10, a0);
        v28 = sub_1033e670(a3);
        v29 = sub_10346d50();
        v27 = 0;
        if (((char)idx->field_60 & 2) && (!sub_10346d50() || (v55 = sub_10314ca0(&v37 + *((int *)(v37 + 4)), 43), (int)(char)*(v28) != (int)sub_10314ca0(&v37 + *((int *)(v37 + 4)), 43) && !((v56 = sub_10314ca0(&v37 + *((int *)(v37 + 4)), 45), (int)(char)*(v28) == (int)sub_10314ca0(&v37 + *((int *)(v37 + 4)), 45))))))
            v27 = 1;
        if (v29 == v38 && v38 <= idx->field_5c && !v27)
        {
            sub_10314830(a2, v28, v29);
        }
        else
        {
            sub_10314830(a2, v28, v29);
            v28 = 0;
            sub_10347790(v14, a4);
            sub_103470c0(a3, 1);
            v41 = 1;
            v9 = (!&v25 ? NULL : &(&v26)[*((int *)(v26 + 4))]);
            sub_10347290(v9, a4);
            v8 = (!&v25 ? NULL : &v26);
            v1 = a0;
            v0 = v8;
            sub_10334530();
            sub_103451f0(&(&v26)[*((int *)(v26 + 4))], 0);
            if (v27)
            {
                v7 = (!&v25 ? NULL : &v26);
                sub_10345240(v7, 32);
            }
            v6 = (!&v25 ? NULL : &v26);
            sub_10347c50(v6, a0);
            if (!sub_10346d50() && ((char)idx->field_60 & 2))
            {
                v27 = 1;
                v5 = (!&v25 ? NULL : &v26);
                sub_10345240(v5, 32);
            }
            v23 = sub_1033e670(a3);
            v17 = sub_10346d50();
            v16 = idx->field_5c;
            v24 = *((int *)sub_10347830(&v16, &v17));
            if (v38 <= v24)
            {
                sub_10314830(a2, v23, v24);
            }
            else
            {
                v15 = -(-(0 < v27)) + v29;
                v20 = *((int *)sub_10347830(&v15, &v24));
                for (i = v27; i < v20 && (v57 = (char *)sub_103189a0(a2, i - -(-((unsigned int)(char)(0 < (unsigned int)v27)))), (int)(char)v23[i] == (int)*((char *)sub_103189a0(a2, i - -(-((unsigned int)(char)(0 < (unsigned int)v27)))))); i += 1);
                if (i >= v24)
                    i = v27;
                sub_10314830(a2, v23, i);
                v21 = v38 - v24;
                sub_103170f0(a2, v21, sub_10345220(&(&v26)[*((int *)(v26 + 4))]));
                sub_1031a6b0(a2, &v23[i], v24 - i);
            }
            v41 = 0;
            sub_103469c0();
        }
    }
    sub_10347790();
    v41 = 4294967295;
    sub_103469c0();
    v59 = _ccall(v43, v44, (unsigned int)v45, 0);
    *((unsigned int *)v59) = v39;
    return;
}
```

## `sub_10346360` `0x10346360`

_87 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10346360(int a0, int a1, unsigned int a2)
{
    char v0;  // [bp-0xb]
    char v1;  // [bp-0xa]
    char v2;  // [bp-0x9]
    unsigned int v3;  // [bp-0x8]

    v3 = (int)((a1 - a0) / 100) * 100 + a2;
    v2 = 0;
    v1 = 0;
    sub_10349b40(a0, a1, sub_10349d70(&/* unsupported instruction */, v0, v1, v2));
    return v3;
}
```

## `sub_103463c0` `0x103463c0`

_78 bytes. (leaf/helper — see body)_

```c
char sub_103463c0(char a0, char a0, int a1, int a2)
{
    unsigned int v5;  // ecx
    int v6;  // edx
    int v7;  // eax
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]
    char v2;  // [bp-0x6]
    char v3;  // [bp-0x5]

    v1 = v5;
    v3 = 0;
    v0 = &/* unsupported instruction */;
    v2 = sub_10337970();
    v6 = _INSERT(0, 0, v3);
    v7 = _INSERT(v2 CONCAT 0, 0, v2);
    return sub_10349b80(sub_10349d70(&/* unsupported instruction */, sub_10349d70(&/* unsupported instruction */, a1, a2, v7, v6)));
}
```

## `sub_10346410` `0x10346410`

_38 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10346410(unsigned int i, unsigned int a1, int a2)
{
    unsigned int v0;  // eax

    for (; i != a1; i += 100)
    {
        sub_103469f0(a2);
    }
    return v0;
}
```

## `sub_10346440` `0x10346440`

_64 bytes. (leaf/helper — see body)_

```c
char sub_10346440(int a0, int a1, int a2, char a3)
{
    unsigned int v5;  // ecx
    int v6;  // eax
    int v7;  // ecx
    int v8;  // edx
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x6]
    char v4;  // [bp-0x5]

    v2 = v5;
    v4 = 0;
    v1 = &/* unsupported instruction */;
    v0 = &/* unsupported instruction */;
    v3 = sub_10337970();
    v6 = _INSERT(v3 CONCAT 0, 0, v4);
    v7 = _INSERT(0, 0, v3);
    v8 = _INSERT(0, 0, a3);
    return sub_10349ba0(a0, a1, a2, v8, v7, v6);
}
```

## `sub_10346480` `0x10346480`

_126 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10346480(unsigned int a0, unsigned int a1, int i, unsigned int a3, int a4, unsigned int a5)
{
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // fs
    unsigned long v13;  // 4144
    unsigned int v14;  // ebx
    unsigned int v15;  // esi
    unsigned int v16;  // edi
    unsigned long v17;  // 4168
    int v18;  // eax
    unsigned long v19;  // 4122
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x1c]
    int v4;  // [bp-0x18], Other Possible Types: unsigned int
    char *v5;  // [bp-0x14], Other Possible Types: unsigned int
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]
    char v9;  // [bp-0x4]

    v8 = 4294967295;
    v7 = sub_10370d80;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v6 = *((int *)v13);
    v5 = a0;
    v4 = a0;
    v3 = v14;
    v2 = v15;
    v1 = v16;
    v0 = g_1038e180 ^ &v9;
    v17 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v17) = &v6;
    v5 = &v0;
    v4 = i;
    for (v8 = 0; a3 > 0; i += 100)
    {
        v18 = sub_10346d30(i, a4);
        a3 -= 1;
    }
    v19 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v19) = v6;
    return v18;
}
```

## `sub_103464e5` `0x103464e5`

_2 bytes. (leaf/helper — see body)_

```c
void sub_103464e5(void)
{
    sub_103464f0();
    return;
}
```

## `sub_103464f0` `0x103464f0`

_33 bytes. (leaf/helper — see body)_

```c
extern char g_10346523;

int sub_103464f0(void)
{
    unsigned int v1;  // [bp+0xffff0]
    unsigned int v2;  // [bp+0x100000]
    unsigned int v3;  // [bp+0x10000c]

    if (v1 == v3)
    {
        sub_103533ea(0, 0);
        v2 = 4294967295;
        return &g_10346523;
    }
    return sub_103464fb();
}
```

## `sub_103464fb` `0x103464fb`

_20 bytes. (leaf/helper — see body)_

```c
int sub_103464fb(int a0)
{
    unsigned int v1;  // [bp+0xffff0]
    int v2;  // [bp+0x100018]

    sub_10340a00(v2, a0);
    v1 += 100;
    return sub_103464f0();
}
```

## `sub_10346540` `0x10346540`

_127 bytes. (leaf/helper — see body)_

```c
int sub_10346540(int a0)
{
    char v0;  // [bp-0x44]
    char v1;  // [bp-0x38]
    char v2;  // [bp-0x2c]
    char *v3;  // [bp-0x24]
    char *v4;  // [bp-0x20], Other Possible Types: unsigned int
    char *v5;  // [bp-0x1c], Other Possible Types: unsigned int
    char *v6;  // [bp-0x18], Other Possible Types: unsigned int
    char v7;  // [bp-0x7]
    char v8;  // [bp-0x6]
    char v9;  // [bp-0x5]
    char v10;  // [bp+0x8]
    char v11;  // [bp+0x14]
    char v12;  // [bp+0x20]

    v9 = 0;
    v6 = &v12;
    v5 = &v10;
    v8 = sub_10337970();
    v6 = _INSERT(v8 CONCAT 0, 0, v9);
    *((char *)&v5) = v8;
    v4 = &v12;
    v3 = &v10;
    *((char *)&v4) = *((char *)sub_103378b0(&v7));
    sub_103413d0(&v2, &v12);
    sub_10349c00(&v1, &v11);
    sub_10349c00(&v0, &v10, v0, &v1, &v11);
    sub_10349c20(a0);
    return a0;
}
```

## `sub_103465c0` `0x103465c0`

_55 bytes. (leaf/helper — see body)_

```c
int sub_103465c0(char a0, unsigned int a0, unsigned int a1, char a2, unsigned int a3, unsigned int a4, unsigned int a5)
{
    char v0;  // [bp-0x28]
    char v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x10]

    v2 = a5;
    sub_10349c00(&v1, &/* unsupported instruction */);
    sub_10349c00(&v0, &/* unsupported instruction */, v0, &v1, &/* unsupported instruction */);
    return sub_10349ca0();
}
```

## `sub_10346600` `0x10346600`

_127 bytes. (leaf/helper — see body)_

```c
int sub_10346600(int a0)
{
    char v0;  // [bp-0x44]
    char v1;  // [bp-0x38]
    char v2;  // [bp-0x2c]
    char *v3;  // [bp-0x24]
    char *v4;  // [bp-0x20], Other Possible Types: unsigned int
    char *v5;  // [bp-0x1c], Other Possible Types: unsigned int
    char *v6;  // [bp-0x18], Other Possible Types: unsigned int
    char v7;  // [bp-0x7]
    char v8;  // [bp-0x6]
    char v9;  // [bp-0x5]
    char v10;  // [bp+0x8]
    char v11;  // [bp+0x14]
    char v12;  // [bp+0x20]

    v9 = 0;
    v6 = &v12;
    v5 = &v10;
    v8 = sub_10337970();
    v6 = _INSERT(v8 CONCAT 0, 0, v9);
    *((char *)&v5) = v8;
    v4 = &v12;
    v3 = &v10;
    *((char *)&v4) = *((char *)sub_103378b0(&v7));
    sub_103413d0(&v2, &v12);
    sub_10349c00(&v1, &v11);
    sub_10349c00(&v0, &v10, v0, &v1, &v11);
    sub_10349cf0(a0);
    return a0;
}
```

## `sub_10346680` `0x10346680`

_101 bytes. (leaf/helper — see body)_

```c
int sub_10346680(char a0, char a0, int a1)
{
    int v9;  // edx
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x6]
    char v5;  // [bp-0x5]

    v5 = 0;
    v3 = &/* unsupported instruction */;
    v2 = &/* unsupported instruction */;
    v4 = sub_10337970();
    v3 = _INSERT(v4 CONCAT 0, 0, v5);
    *((char *)&v2) = v4;
    v1 = &/* unsupported instruction */;
    v0 = &/* unsupported instruction */;
    v9 = _INSERT(0, 0, *((char *)sub_103378b0((char *)&/* unsupported instruction */ + 1)));
    return sub_10349d90(sub_10349d70(&/* unsupported instruction */, sub_10349d70(&/* unsupported instruction */, a1, v9)));
}
```

## `sub_103466f0` `0x103466f0`

_37 bytes. (leaf/helper — see body)_

```c
int sub_103466f0(int a0, int a1, int a2, int a3)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10349de0(a1, a2, a3, a0, a0, &v1);
}
```

## `sub_10346720` `0x10346720`

_43 bytes. (leaf/helper — see body)_

```c
int sub_10346720(char a0, char a0, int a1)
{
    char v0;  // [bp+0x0]

    return sub_10349e30(sub_10349d70(&/* unsupported instruction */, sub_10349d70(&/* unsupported instruction */, a1, &v0)));
}
```

## `sub_10346750` `0x10346750`

_97 bytes. (leaf/helper — see body)_

```c
int sub_10346750(char a0, char a0, int a1)
{
    int v9;  // ecx
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x6]
    char v5;  // [bp-0x5]

    v5 = 0;
    v3 = &/* unsupported instruction */;
    v4 = sub_10337970();
    *((char *)&v3) = v5;
    v2 = _INSERT(v4 CONCAT 0, 0, v4);
    v1 = &/* unsupported instruction */;
    v0 = &/* unsupported instruction */;
    v9 = _INSERT(0, 0, *((char *)sub_103378b0((char *)&/* unsupported instruction */ + 1)));
    return sub_10349e60(sub_10349d70(&/* unsupported instruction */, sub_10349d70(&/* unsupported instruction */, a1, v9)));
}
```

## `sub_103467c0` `0x103467c0`

_64 bytes. (leaf/helper — see body)_

```c
char sub_103467c0(int a0, int a1, int a2, int a3)
{
    unsigned int v5;  // ecx
    int v6;  // eax
    int v7;  // ecx
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    char v3;  // [bp-0x6]
    char v4;  // [bp-0x5]

    v2 = v5;
    v4 = 0;
    v1 = &/* unsupported instruction */;
    v0 = &/* unsupported instruction */;
    v3 = sub_10337970();
    v6 = _INSERT(v3 CONCAT 0, 0, v4);
    v7 = _INSERT(0, 0, v3);
    return sub_10349ea0(a0, a1, a2, a3, v7, v6);
}
```

## `sub_10346800` `0x10346800`

_158 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390c2c;
extern char g_10390c3c;
extern char g_10390c44;

unsigned int sub_10346800(unsigned int idx, int a1)
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
    v3 = sub_10370db3;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_103468a0(a1, g_1038e180 ^ &v5);
    v4 = 0;
    v1 = (!a1 ? 0 : a1 + 40);
    v0 = v1;
    sub_10313b60(idx + 40);
    *((char **)idx) = &g_10390c44;
    *((char **)(idx + 20)) = &g_10390c3c;
    *((char **)(idx + 40)) = &g_10390c2c;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return idx;
}
```

## `sub_103468a0` `0x103468a0`

_148 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390c50;
extern char g_10390c58;

unsigned int * sub_103468a0(unsigned int *a0, unsigned int a1)
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
    v2 = sub_10370de3;
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v1 = *((int *)v8);
    v9 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v9) = &v1;
    sub_10346940(a1, g_1038e180 ^ &v4);
    v3 = 0;
    v0 = (!a1 ? 0 : a1 + 20);
    sub_10313a80(a0 + 5, v0);
    *(a0) = &g_10390c58;
    a0[5] = &g_10390c50;
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v10) = v1;
    return a0;
}
```

## `sub_10346940` `0x10346940`

_117 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390b7c;

unsigned int [5] sub_10346940(unsigned int *a0, unsigned int *index)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4154
    unsigned long v11;  // 4160
    unsigned int v0;  // [bp-0x18]
    unsigned int idx[5];  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_10370e08;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    idx = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    idx = a0;
    sub_1033fe70(idx, index);
    idx[0] = &g_10390b7c;
    idx[3] = index[3];
    idx[4] = index[4];
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return idx;
}
```

## `sub_103469c0` `0x103469c0`

_33 bytes. (leaf/helper — see body)_

```c
unsigned int sub_103469c0(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10346ac0(a0, &v1);
    return sub_103138b0(a0 + 12);
}
```

## `sub_103469f0` `0x103469f0`

_104 bytes. (leaf/helper — see body)_

```c
unsigned int [25] sub_103469f0(unsigned int *a0, unsigned int *index)
{
    unsigned int idx[25];  // [bp-0x8]

    idx = a0;
    idx = a0;
    idx[0] = *(index);
    sub_10319f70(&idx[1], index + 1);
    sub_10319f70(&idx[8], index + 8);
    sub_10346bd0(index + 15);
    idx[23] = index[23];
    idx[24] = index[24];
    return idx;
}
```

## `sub_10346a60` `0x10346a60`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10346a60(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10346f60(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_10346a90` `0x10346a90`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10346a90(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10346ed0(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_10346ac0` `0x10346ac0`

_121 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

void sub_10346ac0(unsigned int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4177
    unsigned long v11;  // 4181
    unsigned long v12;  // 4113
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned int
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_10370e67;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v4 = 1;
    v4 = 0;
    if (a0 != 12)
        v1 = a0 - 4;
    else
        v1 = 0;
    sub_10346b40();
    v4 = 4294967295;
    sub_10346c40();
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v2;
    return;
}
```

## `sub_10346b40` `0x10346b40`

_31 bytes. (leaf/helper — see body)_

```c
extern char g_10390c64;

void* sub_10346b40(void* a0)
{
    *((char **)(-0x4 + (char *)a0 + *((int *)((int)a0[4] + 4)))) = &g_10390c64;
    return a0;
}
```

## `sub_10346b60` `0x10346b60`

_53 bytes. (leaf/helper — see body)_

```c
int sub_10346b60(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10346ba0(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0 - 4);
    return a0 - 4;
}
```

## `sub_10346ba0` `0x10346ba0`

_33 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10346ba0(unsigned int a0)
{
    unsigned int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_10346b40(v0 + 4);
    return sub_103138b0(v0 + 4);
}
```

## `sub_10346bd0` `0x10346bd0`

_104 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    char field_8;
    char padding_9[3];
    unsigned int field_c;
    unsigned int field_10;
    unsigned int field_14;
} struct_0;

struct_0 * sub_10346bd0(struct_0 *idx, struct_0 *index)
{
    struct_0 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = idx;
    idx->field_0 = index->field_0;
    idx->field_4 = index->field_4;
    idx->field_8 = index->field_8;
    idx->field_c = index->field_c;
    idx->field_10 = index->field_10;
    idx->field_14 = index->field_14;
    sub_10346ce0(index + 1, idx, &v1);
    return idx;
}
```

## `sub_10346c40` `0x10346c40`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10346c40(int a0)
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
    v12 = sub_10346c90(g_1038e180 ^ &v3, a0, v10, sub_10370e98, -1, &v4);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v10;
    return v12;
}
```

## `sub_10346c90` `0x10346c90`

_78 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int * sub_10346c90(unsigned int *a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4140
    unsigned long v11;  // 4156
    unsigned int *v12;  // eax
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x18]
    unsigned int *v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_10370ecb;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    v4 = 0;
    v4 = 4294967295;
    v12 = sub_103368f0(v1 + 1);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_10346ce0` `0x10346ce0`

_28 bytes. (leaf/helper — see body)_

```c
int sub_10346ce0(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10349ec0(a1, a0, &v1);
    return a0;
}
```

## `sub_10346d00` `0x10346d00`

_46 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10346d00(char *a0)
{
    unsigned int v0;  // [bp-0xc]

    v0 = (!*(a0) ? 0 : sub_10331570(a0));
    return v0;
}
```

## `sub_10346d30` `0x10346d30`

_29 bytes. (leaf/helper — see body)_

```c
int sub_10346d30(int a0, int a1, int a2)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10349fb0(a1, a2, a0, &v1);
}
```

## `sub_10346d50` `0x10346d50`

_35 bytes. (leaf/helper — see body)_

```c
int sub_10346d50(void* a0)
{
    int v2;  // eax
    void* v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    v2 = sub_103131c0(v0);
    return v2 - sub_1033e670(v0);
}
```

## `sub_10346d80` `0x10346d80`

_118 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390c00;
extern char g_10390c08;

unsigned int * sub_10346d80(unsigned int *a0, unsigned int *a1)
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
    v3 = sub_10370f03;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_103433e0(v1, a1);
    v4 = 0;
    sub_103167f0(v1 + 5);
    *(v1) = &g_10390c08;
    v1[5] = &g_10390c00;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_10346e00` `0x10346e00`

_194 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390bdc;
extern char g_10390bec;
extern char g_10390bf4;

int sub_10346e00(unsigned int idx, unsigned int a1)
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
    v4 = sub_10370f33;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v0 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    sub_10343340(idx, a1);
    v5 = 0;
    sub_10316a00(idx + 40);
    v5 = 1;
    *((char **)idx) = &g_10390bf4;
    *((char **)(idx + 20)) = &g_10390bec;
    *((char **)(idx + 40)) = &g_10390bdc;
    v2 = (!a1 ? 0 : a1 + 20);
    v1 = (!idx ? 0 : idx + 20);
    sub_10316940(v1, v2);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v3;
    return idx;
}
```

## `sub_10346ed0` `0x10346ed0`

_132 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390c50;
extern char g_10390c58;

unsigned int sub_10346ed0(int a0)
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
    v3 = sub_10370f7f;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    *((char **)a0) = &g_10390c58;
    *((char **)(a0 + 20)) = &g_10390c50;
    v4 = 1;
    v4 = 0;
    v1 = (!a0 ? 0 : a0 + 20);
    sub_10313d70(v1);
    v4 = 4294967295;
    v12 = sub_10342e50(a0);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_10346f60` `0x10346f60`

_142 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390c2c;
extern char g_10390c3c;
extern char g_10390c44;

unsigned int sub_10346f60(unsigned int idx)
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
    v3 = sub_10370fcf;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    *((char **)idx) = &g_10390c44;
    *((char **)(idx + 20)) = &g_10390c3c;
    *((char **)(idx + 40)) = &g_10390c2c;
    v4 = 1;
    v4 = 0;
    v1 = (!idx ? 0 : idx + 40);
    sub_10313bb0(v1);
    v4 = 4294967295;
    v12 = sub_10346ed0(idx);
    v13 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v13) = v2;
    return v12;
}
```

## `sub_10346ff0` `0x10346ff0`

_148 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10346ff0(int a0)
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
    v5 = sub_10370ffb;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v4 = *((int *)v12);
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v4;
    v2 = sub_10350a53(44, g_1038e180 ^ &v7);
    v6 = 0;
    v1 = (!v2 ? 0 : sub_10346800(v2, a0 - 40));
    v3 = v1;
    v6 = 4294967295;
    v0 = (!v3 ? 0 : v3 + 40);
    v14 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v14) = v4;
    return v0;
}
```

## `sub_10347090` `0x10347090`

_42 bytes. (leaf/helper — see body)_

```c
extern int g_103a0274;

int sub_10347090(int a0)
{
    char v0;  // [bp-0x30]

    sub_10346800(&v0, a0 - 40);
    return sub_103533ea(&v0, &g_103a0274);
}
```

## `sub_103470c0` `0x103470c0`

_193 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[8];
    struct struct_0 *field_8;
} struct_1;

typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern unsigned int g_1038e180;
extern char g_10390c6c;
extern char g_10390c70;

struct_1 * sub_103470c0(struct_1 *idx, int a1, unsigned int a2)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4173
    char *v11;  // eax
    unsigned long v12;  // 4177
    unsigned long v15;  // 4145
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x18]
    char v2;  // [bp-0x11]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1037104f;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v0 = g_1038e180 ^ &v6;
    v11 = &v3;
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v12) = &v3;
    v1 = 0;
    if (a2)
    {
        idx->field_8 = &g_10390c70;
        v11 = sub_10313f60(idx + 1);
        v5 = 0;
        v1 |= 1;
    }
    v2 = 0;
    sub_1034a030(a1, _INSERT(v11, 0, v2));
    v5 = 1;
    sub_10347190(sub_10347270(0, 0));
    *((char **)&idx->padding_0[idx->field_8->field_4 + 8]) = &g_10390c6c;
    v15 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v15) = v3;
    return idx;
}
```

## `sub_10347190` `0x10347190`

_158 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern unsigned int g_1038e180;
extern char g_10390c64;
extern char g_10390c78;

struct_0 ** sub_10347190(struct_0 **a0, unsigned int a1, char a2, unsigned int a3)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4173
    unsigned long v10;  // 4177
    unsigned long v11;  // 4120
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1037108c;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = 0;
    if (a3)
    {
        *(a0) = &g_10390c78;
        sub_10313f60(a0 + 1);
        v4 = 0;
        v1 |= 1;
    }
    *((char **)((char *)a0 + *(a0)->field_4)) = &g_10390c64;
    sub_10313fe0((char *)a0 + *(a0)->field_4, a1, a2);
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return a0;
}
```

## `sub_10347230` `0x10347230`

_53 bytes. (leaf/helper — see body)_

```c
int sub_10347230(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_103469c0(v0 - 12);
    if (((char)a1 & 1))
        sub_10350abd(v0 - 12);
    return v0 - 12;
}
```

## `sub_10347270` `0x10347270`

_19 bytes. (leaf/helper — see body)_

```c
int sub_10347270(unsigned int *a0)
{
    unsigned int *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_10336b20(v0);
}
```

## `sub_10347290` `0x10347290`

_269 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    char field_8;
    char padding_9[3];
    int field_c;
    unsigned int field_10;
    int field_14;
} struct_0;

extern unsigned int g_1038e180;

int sub_10347290(struct_0 *a0, struct_0 *a1, int a2)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4172
    unsigned long v11;  // 4176
    unsigned int v13;  // eax
    unsigned long v15;  // 4113
    unsigned int v0;  // [bp-0x20]
    struct_0 **v1;  // [bp-0x18]
    struct_0 **v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_103710c0;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v0 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    if (a0->field_0 != 4294967295)
        sub_103451f0(a1, a0->field_0);
    if (a0->field_4 != 4294967295)
        sub_10316590(a1, a0->field_4);
    if (a0->field_8)
        sub_1034a230(_INSERT(a0, 0, a0->field_8));
    sub_103473d0(a0->field_c);
    sub_103147f0(a1, a0->field_10, 0);
    sub_103473a0(a0->field_14);
    v13 = (unsigned int)sub_1032e0a0(a0 + 1);
    if (v13)
    {
        sub_10347400(&v2, (unsigned int)sub_103301b0(a0 + 1));
        v5 = 4294967295;
        v13 = sub_103130c0(&v2);
    }
    else if (a2)
    {
        sub_10347400(&v1, a2);
        v5 = 4294967295;
        v13 = sub_103130c0(&v1);
    }
    v15 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v15) = v3;
    return v13;
}
```

## `sub_103473a0` `0x103473a0`

_40 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    int field_8;
    unsigned int field_c;
} struct_0;

int sub_103473a0(struct_0 *a0, unsigned int a1)
{
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    v0->field_c = a1 & 23;
    return sub_103140e0(v0, v0->field_8);
}
```

## `sub_103473d0` `0x103473d0`

_42 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[16];
    unsigned int field_10;
} struct_0;

int sub_103473d0(struct_0 *idx, unsigned short a1)
{
    unsigned int v0;  // [bp-0x8]

    v0 = idx->field_10;
    idx->field_10 = a1;
    return v0;
}
```

## `sub_10347400` `0x10347400`

_170 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern unsigned int g_1038e180;

struct_0 ** sub_10347400(unsigned int a0, struct_0 **a1, int a2)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4143
    unsigned long v11;  // 4157
    unsigned long v12;  // 4117
    unsigned int v0;  // [bp-0x1c]
    struct_0 **v1;  // [bp-0x18]
    char v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char v5;  // [bp-0x8], Other Possible Types: unsigned int
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_10371109;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    sub_103474b0(&v2, a2, g_1038e180 ^ &v6, a0, 0);
    v5 = 1;
    if (sub_10315c20(a0))
    {
        sub_10315c20(a0);
        sub_10347610(&v1, a2);
        v5 = 1;
        sub_103130c0(&v1);
    }
    sub_10314db0(a1, &v2);
    v0 = 1;
    v5 = 0;
    sub_103130c0(&v2);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v3;
    return a1;
}
```

## `sub_103474b0` `0x103474b0`

_147 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern unsigned int g_1038e180;

struct_0 ** sub_103474b0(struct_0 *a0, struct_0 **a1, int a2)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4141
    unsigned long v11;  // 4155
    unsigned long v12;  // 4117
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x18]
    char v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    char v5;  // [bp-0x8], Other Possible Types: unsigned int
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_10371151;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v3 = *((int *)v10);
    v0 = g_1038e180 ^ &v6;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v3;
    v1 = 0;
    sub_10314db0(&v2, a0[4].field_4);
    v5 = 1;
    sub_10347550(a2);
    sub_103475c0(1);
    sub_10314db0(a1, &v2);
    v1 |= 1;
    v5 = 0;
    sub_103130c0(&v2);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v3;
    return a1;
}
```

## `sub_10347550` `0x10347550`

_101 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

typedef struct struct_1 {
    struct struct_0 *field_0;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

struct_0 ** sub_10347550(struct_0 **a0, unsigned int a1)
{
    unsigned int v0;  // [bp-0x14]
    struct_1 **v1;  // [bp-0xc]
    struct_1 **v2;  // [bp-0x8]

    if (*(a0) == *((int *)a1))
        return a0;
    v1 = sub_10313110(*(a0));
    v2 = v1;
    if (v2)
        v0 = *(v2)->field_0(1);
    else
        v0 = 0;
    *(a0) = *((int *)a1);
    sub_10313500(*(a0));
    return a0;
}
```

