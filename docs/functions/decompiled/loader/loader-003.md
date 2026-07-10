# elfbot.dll decompiled — loader 0x00402df0..0x00403498

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_00402df0` `0x00402df0`

_19 bytes. (leaf/helper — see body)_

```c
int sub_402df0(void)
{
    int v0;  // [bp-0x4]

    sub_402e80(v0);
    sub_402524(v0);
    return;
}
```

## `sub_00402e03` `0x00402e03`

_1 bytes. (leaf/helper — see body)_

```c
int sub_402e03(void)
{
    sub_402e04();
    return;
}
```

## `sub_00402e04` `0x00402e04`

_6 bytes. (leaf/helper — see body)_

```c
int sub_402e04(void)
{
    return;
}
```

## `sub_00402e0a` `0x00402e0a`

_17 bytes. (leaf/helper — see body)_

```c
unsigned int sub_402e0a(unsigned int a0, char a1)
{
    unsigned int v1;  // eax
    char v2;  // dl
    unsigned int v3;  // 4105

    v1 = sub_402fac();
    v3 = _ccall(14, 13, (unsigned int)v2, 0, 0);
    if ((char)v3)
        return v1;
    return sub_402f94();
}
```

## `sub_00402e1b` `0x00402e1b`

_1 bytes. (leaf/helper — see body)_

```c
int sub_402e1b(void)
{
    sub_402e1c();
    return;
}
```

## `sub_00402e1c` `0x00402e1c`

_12 bytes. (leaf/helper — see body)_

```c
int sub_402e1c(void)
{
    void* *v1;  // eax

    if (v1)
        (int)(*(v1))[4]();
    return;
}
```

## `sub_00402e28` `0x00402e28`

_86 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    char field_4;
    char padding_5[15];
    struct struct_1 *field_14;
    unsigned int field_18;
    char padding_1c[4];
    char field_20;
} struct_0;

typedef struct struct_1 {
} struct_1;

int sub_402e28(void)
{
    unsigned int v5;  // ebx
    unsigned int v6;  // esi
    unsigned int v15;  // ecx
    unsigned int v16;  // ecx
    void* v7;  // eax
    void* v8;  // ebx
    void* v9;  // edx
    void* iter;  // edi
    unsigned int v11;  // ecx
    unsigned int v12;  // ecx
    unsigned int v13;  // ecx
    unsigned int idx;  // ebx
    unsigned int v0;  // [bp-0x14]
    struct_0 *v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0x8]
    unsigned int v3;  // [bp-0x4]

    v3 = v5;
    v2 = v6;
    v8 = v7;
    *((void* *)v9) = v7;
    iter = v9 + 4;
    v1 = (int)v8[40];
    for (v11 = ((int)v8[40] >> 2) - 1; v11; iter += 4)
    {
        v11 -= 1;
        *((unsigned int *)iter) = 0;
    }
    for (v12 = v1 & 3; v12; iter += 1)
    {
        v12 -= 1;
        *((char *)iter) = 0;
    }
    while (true)
    {
        if ((int)v8[72])
            v0 = (int)v8[72];
        if (!(int)v8[36])
            break;
        v8 = *((int *)(int)v8[36]);
    }
    if (&v1 == &/* unsupported instruction */)
        return;
    do
    {
        v13 = v1->field_0;
        idx = &v1->field_4;
        do
        {
            v15 = v13;
            if (*((int *)(idx + 16)))
                *((int *)(*((int *)(idx + 20)) + (char *)v9)) = *((int *)(idx + 16));
        } while ((idx += 28, v16 = v15 - 1, v13 = v15 - 1, v15 != 1));
    } while (false);
    return;
}
```

## `sub_00402e7e` `0x00402e7e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_402e7e(void)
{
    sub_402e80();
    return;
}
```

## `sub_00402e80` `0x00402e80`

_32 bytes. (leaf/helper — see body)_

```c
int sub_402e80(void)
{
    void* *v5;  // esi
    void* *v1;  // esi
    void* *v2;  // esi
    void* *v3;  // esi

    do
    {
        v2 = v1;
        v3 = (int)(*(v2))[36];
        if ((int)(*(v2))[64])
            sub_4040f0();
    } while ((v5 = v3, (int)(*(v2))[36]));
    return;
}
```

## `sub_00402ea0` `0x00402ea0`

_33 bytes. (leaf/helper — see body)_

```c
int sub_402ea0(void)
{
    unsigned int v3;  // eax

    if (!v3)
        return;
    return;
}
```

## `sub_00402ec1` `0x00402ec1`

_3 bytes. (leaf/helper — see body)_

```c
int sub_402ec1(void)
{
    sub_402ec4();
    return;
}
```

## `sub_00402ec4` `0x00402ec4`

_46 bytes. (leaf/helper — see body)_

```c
int sub_402ec4(void)
{
    void* i;  // esi
    void* v3;  // esi
    unsigned short v4[2];  // edi
    unsigned int v5;  // ecx
    unsigned int v6;  // edi
    unsigned int v0;  // [bp-0x8]

    while (true)
    {
        v4 = (int)v3[48];
        if (v4)
        {
            v5 = v4[0];
            v0 = v5;
            v6 = &v4[1];
            do
            {
                if (!v5)
                    break;
            } while ((unsigned short)i != *((short *)v6));
            if (v4 == 0xfffffffe)
                return;
        }
        if (!(int)v3[36])
            return;
        v3 = *((int *)(int)v3[36]);
    }
}
```

## `sub_00402ef2` `0x00402ef2`

_2 bytes. (leaf/helper — see body)_

```c
int sub_402ef2(void)
{
    return sub_402ef4();
}
```

## `sub_00402ef4` `0x00402ef4`

_2 bytes. (leaf/helper — see body)_

```c
int sub_402ef4(void)
{
    sub_402ef8();
    return;
}
```

## `sub_00402ef8` `0x00402ef8`

_17 bytes. (leaf/helper — see body)_

```c
int sub_402ef8(void)
{
    void* v1;  // eax
    void* v2;  // edx

    if (v1 == v2)
        return;
}
```

## `sub_00402f07` `0x00402f07`

_1 bytes. (leaf/helper — see body)_

```c
void sub_402f07(void)
{
    sub_402f08(); /* do not return */
}
```

## `sub_00402f08` `0x00402f08`

_6 bytes. (leaf/helper — see body)_

```c
void sub_402f08(void)
{
    return;
}
```

## `sub_00402f1c` `0x00402f1c`

_22 bytes. (leaf/helper — see body)_

```c
int sub_402f1c(void)
{
    unsigned short *v1;  // edx
    void* *v2;  // eax

    if (*(v1) && *(v1) < 0xc000)
    {
        sub_402f2c();
        return;
    }
    goto (int)(*(v2))[16];
}
```

## `sub_00402f2c` `0x00402f2c`

_16 bytes. (leaf/helper — see body)_

```c
int sub_402f2c(void)
{
    unsigned int v2;  // cc_op
    unsigned int v3;  // cc_dep1
    unsigned int v4;  // cc_dep2
    unsigned int v5;  // cc_ndep
    unsigned int v6;  // 4104
    unsigned int v7;  // esi
    int v0;  // [bp-0x4]

    sub_402ec4(v0);
    v6 = _ccall(4, v2, v3, v4, v5);
    if ((char)v6)
        goto LABEL_0x402f3c;
    goto v7;
}
```

## `sub_00402f42` `0x00402f42`

_1 bytes. (leaf/helper — see body)_

```c
void sub_402f42(void)
{
    return;
}
```

## `sub_00402f43` `0x00402f43`

_1 bytes. (leaf/helper — see body)_

```c
void sub_402f43(void)
{
    sub_402f44();
    return;
}
```

## `sub_00402f44` `0x00402f44`

_41 bytes. (leaf/helper — see body)_

```c
int sub_402f44(void)
{
    char v4;  // dl
    void* v5;  // eax
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4127
    unsigned long v10;  // 4144
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]
    unsigned int v2;  // [bp-0x4]
    unsigned int v3;  // [bp+0x4]

    if (v4 >= 0)
        (int)v5[12](v0, v1, v2);
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v3 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v3;
    return;
}
```

## `sub_00402f6d` `0x00402f6d`

_5 bytes. (leaf/helper — see body)_

```c
void sub_402f6d(unsigned int a0)
{
    sub_4030c0();
    return;
}
```

## `sub_00402f72` `0x00402f72`

_31 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    struct struct_1 *field_c;
} struct_0;

typedef struct struct_1 {
    void* field_0;
} struct_1;

int sub_402f72(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, struct_0 *a10)
{
    void* *v0;  // eax

    v0 = &a10->field_c->field_0;
    if (v0)
    {
        (int)(*(v0))[4](v0);
        sub_402f94();
    }
    return sub_403498();
}
```

## `sub_00402f91` `0x00402f91`

_3 bytes. (leaf/helper — see body)_

```c
int sub_402f91(void)
{
    sub_402f94();
    return;
}
```

## `sub_00402f94` `0x00402f94`

_6 bytes. (leaf/helper — see body)_

```c
int sub_402f94(void)
{
    void* *v1;  // eax

    (int)(*(v1))[8]();
    return;
}
```

## `sub_00402f9a` `0x00402f9a`

_2 bytes. (leaf/helper — see body)_

```c
void sub_402f9a(void)
{
    sub_402f9c();
    return;
}
```

## `sub_00402f9c` `0x00402f9c`

_14 bytes. (leaf/helper — see body)_

```c
int sub_402f9c(void)
{
    void* *v2;  // eax
    unsigned int v0;  // [bp-0x4]

    (int)(*(v2))[28](v0);
    return;
}
```

## `sub_00402faa` `0x00402faa`

_2 bytes. (leaf/helper — see body)_

```c
int sub_402faa(unsigned int a0, char a1)
{
    return sub_402fac();
}
```

## `sub_00402fac` `0x00402fac`

_15 bytes. (leaf/helper — see body)_

```c
int sub_402fac(void)
{
    unsigned int v1;  // edx
    unsigned int v2;  // 4105
    void* *v3;  // eax

    v2 = _ccall(14, 13, (unsigned int)(char)v1, 0, 0);
    if (!((char)v2))
        (int)(*(v3))[24](v1, v3);
    return;
}
```

## `sub_00402fbb` `0x00402fbb`

_1 bytes. (leaf/helper — see body)_

```c
void sub_402fbb(void)
{
    sub_402fbc();
    return;
}
```

## `sub_00402fbc` `0x00402fbc`

_27 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern char g_41e010;
extern struct_0 *g_420014;

void sub_402fbc(void)
{
    if (g_41e010 > 1)
        g_420014(250477279, 0, 0, 0);
    return;
}
```

## `sub_00402fd7` `0x00402fd7`

_1 bytes. (leaf/helper — see body)_

```c
void sub_402fd7(void)
{
    sub_402fd8();
    return;
}
```

## `sub_00402fd8` `0x00402fd8`

_33 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern char g_41e010;
extern struct_0 *g_420014;

int sub_402fd8(void)
{
    unsigned int v1;  // edx
    unsigned int v2;  // eax

    if (g_41e010)
        g_420014(250477284, 0, 2, &v1, v1, v2, v2);
    return;
}
```

## `sub_00402ff9` `0x00402ff9`

_24 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_420014;

unsigned int sub_402ff9(void)
{
    char v0;  // [bp+0x0]

    g_420014(250477280, 0, 1, &v0);
    return 0;
}
```

## `sub_00403011` `0x00403011`

_3 bytes. (leaf/helper — see body)_

```c
int sub_403011(void)
{
    return sub_403014();
}
```

## `sub_00403014` `0x00403014`

_19 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern char g_41e010;

void sub_403014(void)
{
    unsigned int v3;  // eax
    struct_0 *v4;  // ebx
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp-0x4]

    if (g_41e010 <= 1)
        return;
    v1 = v3;
    v0 = v4->field_4;
}
```

## `sub_00403027` `0x00403027`

_1 bytes. (leaf/helper — see body)_

```c
void sub_403027(void)
{
    sub_403028();
    return;
}
```

## `sub_00403028` `0x00403028`

_17 bytes. (leaf/helper — see body)_

```c
extern char g_41e010;

void sub_403028(void)
{
    unsigned int v3;  // eax
    unsigned int v4;  // ebx
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp-0x4]

    if (g_41e010 <= 1)
        return;
    v1 = v3;
    v0 = v4;
}
```

## `sub_00403039` `0x00403039`

_3 bytes. (leaf/helper — see body)_

```c
int sub_403039(unsigned int a0)
{
    return sub_40303c();
}
```

## `sub_0040303c` `0x0040303c`

_30 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
    unsigned int field_1;
} struct_0;

unsigned int sub_40303c(struct_0 *a0)
{
    unsigned int v1;  // eax
    unsigned int v2;  // eax

    if (!a0)
        return v2;
    v1 = *((int *)&(&a0->field_0)[1]);
    if (a0->field_0 != 233)
    {
        if (a0->field_0 == 235)
            v1 = (char)v1;
        else
            return v1;
    }
    return v1;
}
```

## `sub_0040305a` `0x0040305a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40305a(void)
{
    return sub_40305c();
}
```

## `sub_0040305c` `0x0040305c`

_39 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
    char padding_1[3];
    unsigned int field_1;
} struct_0;

extern char g_41e010;
extern struct_0 *g_420014;

int sub_40305c(struct_0 *a0, unsigned int a1)
{
    unsigned int v4;  // eax
    unsigned int v5;  // ecx
    unsigned int v6;  // eax
    struct_0 *v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]
    unsigned int v2;  // [bp-0x4]

    if (g_41e010 <= 1)
        return v6;
    v2 = v4;
    v1 = a1;
    v0 = a0;
    sub_40303c(a0);
    g_420014(250477281, 0, 1, &v5, v5);
    return &/* unsupported instruction */;
}
```

## `sub_00403083` `0x00403083`

_1 bytes. (leaf/helper — see body)_

```c
void sub_403083(void)
{
    sub_403084();
    return;
}
```

## `sub_00403084` `0x00403084`

_28 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern char g_41e010;
extern struct_0 *g_420014;

void sub_403084(void)
{
    unsigned int v1;  // edx

    if (g_41e010 > 1)
        g_420014(250477282, 0, 1, &v1, v1);
    return;
}
```

## `sub_004030a0` `0x004030a0`

_30 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern char g_41e010;
extern struct_0 *g_420014;

int sub_4030a0(void)
{
    unsigned int v2;  // eax
    unsigned int v0;  // [bp-0x4]

    v0 = v2;
    if (g_41e010 > 1)
        g_420014(250477283, 0, 2, &/* unsupported instruction */);
    return;
}
```

## `sub_004030be` `0x004030be`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4030be(unsigned int a0)
{
    return sub_4030c0();
}
```

## `sub_004030c0` `0x004030c0`

_266 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
    char padding_8[4];
    struct struct_1 *field_c;
    char padding_10[4];
    struct struct_1 *field_14;
    struct struct_1 *field_18;
} struct_1;

typedef struct struct_2 {
    char padding_0[4];
    unsigned int field_4;
} struct_2;

typedef struct struct_4 {
    struct struct_4 *field_0;
} struct_4;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern char g_41e010;
extern char g_41e014;
extern struct_0 *g_420010;
extern struct_0 *g_420018;

unsigned int sub_4030c0(struct_1 *a0, int a1, unsigned int a2)
{
    struct_1 *idx;  // eax
    struct_1 *v8;  // edx
    struct_2 *index;  // esi
    unsigned int v18;  // edi
    unsigned long v19;  // ldt
    unsigned long v20;  // gdt
    unsigned short v21;  // fs
    unsigned long v22;  // 4129
    int v23;  // edx
    struct_4 **v24;  // eax
    unsigned int v25;  // ebx
    struct_1 *v9;  // ecx
    struct_1 *v10;  // eax
    struct_1 *v11;  // eax
    struct_1 *v12;  // ecx
    struct_1 *v13;  // eax
    struct_1 *v14;  // edx
    struct_1 *idx1;  // eax
    unsigned int v16;  // ebx
    struct_4 **v0;  // [bp-0x34]
    int v1;  // [bp-0x2c]
    struct_1 *v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    struct_1 *v4;  // [bp-0x8], Other Possible Types: struct_2 *
    unsigned int v5;  // [bp-0x4]
    struct_1 *v6;  // [bp+0x0]

    idx = a0;
    if (((char)idx->field_4 & 6))
        return 1;
    v8 = idx->field_18;
    v9 = idx->field_14;
    v10 = idx;
    if (v10->field_0 != 250477278)
    {
        sub_402db4();
        if (!g_420010)
            return 1;
        v8 = g_420010();
        if (!v8)
            return 1;
        if (a0->field_0 != 0xeefface && !((v8 = (struct_1 *)sub_402fd8(), g_41e014 <= 0 || g_41e010 > 0)))
        {
            v4 = &a0;
            if (!UnhandledExceptionFilter(&/* unsupported instruction */, v8))
                return 1;
            v11 = v6;
            v12 = v11->field_c;
            goto LABEL_403174;
        }
        else
        {
            v9 = a0->field_c;
            v10 = a0;
        }
    }
    v13 = v10;
    v11 = v13;
    v4 = v8;
    v12 = v9;
    if (g_41e014 > 1)
    {
        v11 = v13;
        v4 = v8;
        v12 = v9;
        if (g_41e010 <= 0)
        {
            v2 = &a0;
            v11 = v8;
            v4 = v9;
            v12 = v2;
            if (!UnhandledExceptionFilter(&/* unsupported instruction */, v4, v11, v13))
                return 1;
        }
    }
LABEL_403174:
    v14 = v4;
    idx1 = v11;
    idx1->field_4 = idx1->field_4 | 2;
    v5 = v16;
    v4 = index;
    v3 = v18;
    v22 = _ccall(v19, v20, (unsigned int)v21, 0);
    v23 = a1;
    g_420018(v23, v1, idx1, 0, v12, v14, idx1, *((int *)v22));
    v24 = sub_404fdc(v23, v1, idx1, 0, v12, v14, idx1, *((int *)v22));
    v0 = *(v24);
    *(v24) = &v0;
    v25 = index->field_4;
    index->field_4 = sub_4031c4;
    sub_403028();
    goto v25 + 5;
}
```

## `sub_004031c4` `0x004031c4`

_5 bytes. (leaf/helper — see body)_

```c
void sub_4031c4(unsigned int a0, unsigned int a1)
{
    sub_403374();
    return;
}
```

## `sub_004031c9` `0x004031c9`

_27 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

int sub_4031c9(void)
{
    struct_0 **v1;  // eax

    v1 = sub_404fdc();
    *(v1) = *(v1)->field_0;
    return sub_402e1c();
}
```

## `sub_004031ea` `0x004031ea`

_73 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_42000c;

unsigned int sub_4031ea(unsigned int *a0, unsigned int a1)
{
    if (((char)a0[1] & 6))
        return 1;
    if (*(a0) == 250477278)
        return sub_40322d();
    sub_402db4();
    if (!g_42000c)
    {
        return 1;
    }
    else if (!g_42000c())
    {
        return 1;
    }
    return sub_40322d();
}
```

## `sub_0040322d` `0x0040322d`

_319 bytes. (leaf/helper — see body)_

```c
typedef struct struct_3 {
    char padding_0[4];
    struct struct_1 *field_4;
} struct_3;

typedef struct struct_6 {
    unsigned int field_0;
    unsigned int field_4;
    char padding_8[4];
    struct struct_6 *field_c;
    char padding_10[4];
    struct struct_6 *field_14;
    struct struct_6 *field_18;
} struct_6;

typedef struct struct_2 {
    void* field_0;
} struct_2;

typedef struct struct_1 {
    char padding_0[5];
    unsigned int field_5;
    struct struct_2 *field_9;
    char padding_d[4];
    char field_11;
} struct_1;

typedef struct struct_5 {
    unsigned int field_0;
} struct_5;

extern char g_40334c;
extern char g_41e010;
extern char g_41e014;
extern struct_5 *g_420010;
extern struct_5 *g_420018;

int sub_40322d(void)
{
    struct_3 *idx;  // edx
    unsigned int v8;  // ebx
    unsigned int v17;  // cc_dep1
    unsigned int v18;  // cc_dep2
    unsigned int v19;  // cc_ndep
    unsigned int v20;  // 4101
    struct_6 *index;  // eax
    struct_6 *v24;  // edx
    struct_6 *v25;  // ecx
    struct_6 *v26;  // eax
    unsigned int iter;  // esi
    struct_6 *v27;  // eax
    struct_6 *idx1;  // eax
    struct_6 *v29;  // ecx
    struct_6 *v30;  // edx
    unsigned long v31;  // ldt
    unsigned long v32;  // gdt
    unsigned short v33;  // fs
    unsigned long v34;  // 4133
    unsigned int v35;  // ebx
    struct_2 **v36;  // eax
    unsigned int v10;  // ebx
    void* *v11;  // eax
    void* v12;  // eax
    void* v13;  // edi
    void* v14;  // edi
    void* v15;  // eax
    unsigned int v16;  // cc_op
    struct_2 **v0;  // [bp-0x38]
    int v1;  // [bp-0x34]
    struct_6 *v2;  // [bp-0x20]
    struct_6 *v3;  // [bp-0x18]
    char v4;  // [bp-0xc], Other Possible Types: unsigned int
    struct_6 *v5;  // [bp+0x0]
    struct_6 *v6;  // [bp+0x4]

    v8 = *((int *)&(idx->field_4->padding_0)[1]);
    iter = (char *)&idx->field_4->field_5 + 1;
LABEL_40323c:
    v10 = v8;
    v11 = *((int *)iter);
    if (*((int *)iter))
    {
        v13 = v12;
        while (true)
        {
            v14 = v13;
            v15 = *(v11);
            if (v15 == v14 || (int)v15[40] == (int)v14[40] && *((char *)(int)v15[44]) == *((char *)(int)v14[44]) && (sub_402860(), v20 = (unsigned int)_ccall(4, v16, v17, v18, v19), (char)v20))
                break;
            v11 = *((int *)iter);
            if ((int)v14[36])
            {
                v13 = *((int *)(int)v14[36]);
            }
            else
            {
                iter += 8;
                v8 = v10 - 1;
                goto LABEL_40323c;
            }
        }
    }
    index = v6;
    v24 = index->field_18;
    v25 = index->field_14;
    if (index->field_0 != 250477278)
    {
        g_420010();
        v26 = sub_402fd8();
        v27 = v26;
        if (g_41e014 > 0)
        {
            v27 = v26;
            if (g_41e010 <= 0)
            {
                v3 = &v4;
                v27 = v3;
                if (!UnhandledExceptionFilter(&v4, v26))
                    goto LABEL_0x40336c;
                else
                    goto LABEL_4032cd;
            }
        }
LABEL_4032cd:
        idx1 = v5;
        v29 = idx1->field_c;
    }
    else
    {
        v27 = v24;
        v29 = v25;
        idx1 = index;
        if (g_41e014 > 1)
        {
            v27 = v24;
            v29 = v25;
            idx1 = index;
            if (g_41e010 <= 0)
            {
                v2 = &v4;
                v27 = v25;
                v29 = v2;
                idx1 = v24;
                if (!UnhandledExceptionFilter(&v4, v27, idx1, index))
                    goto LABEL_0x40336c;
                else
                    goto LABEL_4032ff;
            }
        }
    }
LABEL_4032ff:
    v30 = v27;
    v34 = _ccall(v31, v32, (unsigned int)v33, 0);
    v35 = *((int *)v34);
    idx1->field_4 = idx1->field_4 | 2;
    g_420018(v6, v1, idx1, 0, iter, v29, v30, idx1, v35);
    v36 = sub_404fdc(v1, idx1, 0, iter, v29, v30, idx1, v35);
    v0 = *(v36);
    *(v36) = &v0;
    *((char **)(v4 + 4)) = &g_40334c;
    sub_403014();
    goto v6->field_4;
}
```

## `sub_00403372` `0x00403372`

_2 bytes. (leaf/helper — see body)_

```c
int sub_403372(unsigned int a0, unsigned int a1)
{
    return sub_403374();
}
```

## `sub_00403374` `0x00403374`

_33 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

extern char g_4033a4;

unsigned int sub_403374(struct_0 *a0, unsigned int a1)
{
    if (!((char)a0->field_4 & 6))
        return 1;
    *((char **)(a1 + 4)) = &g_4033a4;
    return sub_40338f();
}
```

## `sub_0040338f` `0x0040338f`

_21 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
    char padding_1[3];
    unsigned int field_1;
} struct_0;

int sub_40338f(struct_0 *a0, unsigned int a1)
{
    unsigned int *v5;  // ecx
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    unsigned int v3;  // [bp-0x4]

    sub_40305c((char *)&a0->field_1 + 1, a1);
    v5(v0, v1, v2, v3);
}
```

## `sub_004033aa` `0x004033aa`

_196 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

typedef struct struct_2 {
    unsigned int field_0;
    unsigned int field_4;
    char padding_8[4];
    struct struct_3 *field_c;
} struct_2;

typedef struct struct_3 {
    void* field_0;
} struct_3;

typedef struct struct_4 {
    unsigned int field_0;
} struct_4;

extern char g_41e010;
extern char g_41e014;
extern struct_4 *g_420018;

unsigned int sub_4033aa(struct_0 *a0, unsigned int a1)
{
    struct_0 *v3;  // eax
    unsigned int v4;  // cc_op
    unsigned long v13;  // gdt
    unsigned short v14;  // fs
    unsigned long v15;  // 4122
    unsigned int v5;  // cc_dep1
    unsigned int v6;  // cc_dep2
    unsigned int v7;  // cc_ndep
    unsigned int v8;  // 4101
    struct_0 *idx;  // eax
    struct_2 *v10;  // edi
    unsigned int v11;  // esi
    unsigned long v12;  // ldt
    unsigned int v0;  // [bp-0x18]
    struct_0 *v1;  // [bp+0x0]
    unsigned int v2;  // [bp+0x100004]

    if (((char)a0->field_4 & 6))
        return 1;
    v3 = (unsigned int)sub_402db4();
    v8 = _ccall(4, v4, v5, v6, v7);
    if (!((char)v8) && g_41e014 > 0 && g_41e010 <= 0 || (idx = v3, g_41e014 > 1 && !((idx = v3, g_41e010 > 0))))
    {
        if (UnhandledExceptionFilter(&/* unsupported instruction */))
            idx = v1;
        else
            return 1;
    }
    idx->field_4 = idx->field_4 | 2;
    g_420018(a1, v0, idx, 0, /* unsupported instruction */, v10, v11);
    if (v2 == 250477278)
    {
        if (v10->field_c)
            (int)v10->field_c->field_0[32]();
        sub_402e1c();
    }
    v15 = _ccall(v12, v13, (unsigned int)v14, 0);
    *((unsigned int *)v15) = v10->field_0;
    goto v10->field_4 + 5;
}
```

## `sub_0040346e` `0x0040346e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40346e(void)
{
    return sub_403470();
}
```

## `sub_00403470` `0x00403470`

_39 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420014;

int sub_403470(void)
{
    unsigned int v13;  // eax
    unsigned int v14;  // eax
    unsigned int v15;  // edi
    unsigned int v16;  // esi
    unsigned int v17;  // ebx
    unsigned int v0;  // [bp-0x2c]
    unsigned int v1;  // [bp-0x28]
    unsigned int v2;  // [bp-0x24]
    unsigned int v3;  // [bp-0x20]
    char *v4;  // [bp-0x1c]
    unsigned int v5;  // [bp-0x18]
    unsigned int v6;  // [bp-0x14]
    unsigned int v7;  // [bp-0x10]
    unsigned int v8;  // [bp-0xc]
    unsigned int v9;  // [bp-0x8]
    char *v10;  // [bp+0x0]
    unsigned int v11;  // [bp+0x0]
    unsigned int v12;  // [bp+0x4]

    if (!v13)
        v14 = sub_403a04();
    v10 = &v12;
    v9 = v15;
    v8 = v16;
    v7 = v17;
    v6 = v14;
    v5 = v11;
    v4 = &v5;
    v3 = 7;
    v2 = 1;
    v1 = 250477278;
    v0 = v5;
    goto g_420014;
}
```

## `sub_00403497` `0x00403497`

_1 bytes. (leaf/helper — see body)_

```c
void sub_403497(void)
{
    return;
}
```

## `sub_00403498` `0x00403498`

_81 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    unsigned int field_0;
    char padding_4[8];
    struct struct_0 *field_c;
} struct_1;

typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
} struct_0;

extern char g_4034e3;

unsigned int sub_403498(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int *a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int a10, unsigned int a11)
{
    struct_1 **v0;  // eax
    struct_1 *v1;  // edx
    struct_0 *idx;  // eax
    unsigned long v3;  // ldt
    unsigned long v4;  // gdt
    unsigned short v5;  // fs
    unsigned long v6;  // 4124

    *((char **)(a11 + 4)) = &g_4034e3;
    v0 = sub_404fdc();
    v1 = *(v0);
    *(v0) = v1->field_0;
    idx = v1->field_c;
    idx->field_4 = idx->field_4 & 4294967293;
    if (idx->field_0 != 250477278)
    {
        sub_402e1c();
        sub_402fbc();
    }
    v6 = _ccall(v3, v4, (unsigned int)v5, 0);
    *(a4) = *((int *)*((int *)v6));
    return 1;
}
```

