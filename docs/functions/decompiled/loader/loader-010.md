# elfbot.dll decompiled — loader 0x00405790..0x00406748

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_00405790` `0x00405790`

_31 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_42075c;

int sub_405790(void)
{
    unsigned int v3;  // ebx
    unsigned int v4;  // esi
    unsigned int v5;  // eax
    unsigned int v6;  // edx
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp-0x4]

    v1 = v3;
    v0 = v4;
    if ((char)sub_4054f4())
        g_42075c(v5, v6);
    return;
}
```

## `sub_004057af` `0x004057af`

_1 bytes. (leaf/helper — see body)_

```c
int sub_4057af(void)
{
    sub_4057b0();
    return;
}
```

## `sub_004057b0` `0x004057b0`

_31 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_420760;

int sub_4057b0(void)
{
    unsigned int v3;  // ebx
    unsigned int v4;  // esi
    unsigned int v5;  // eax
    unsigned int v6;  // edx
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp-0x4]

    v1 = v3;
    v0 = v4;
    if ((char)sub_4054f4())
        g_420760(v5, v6);
    return;
}
```

## `sub_004057cf` `0x004057cf`

_1 bytes. (leaf/helper — see body)_

```c
void sub_4057cf(void)
{
    sub_4057d0();
    return;
}
```

## `sub_004057d0` `0x004057d0`

_36 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420724;

int sub_4057d0(void)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4146
    unsigned long v10;  // 4155
    unsigned long v11;  // 4171
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    char *v2;  // [bp-0x8], Other Possible Types: unsigned int
    char v3;  // [bp-0x4]
    char v4;  // [bp+0x0]

    v2 = &v3;
    v1 = sub_4057f5;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v0 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v0;
    g_420724 = g_420724 + 1;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v0;
    v2 = sub_4057fc;
    return sub_4057f4(&v4);
}
```

## `sub_004057f4` `0x004057f4`

_1 bytes. (leaf/helper — see body)_

```c
void sub_4057f4(void)
{
    return;
}
```

## `sub_004057f5` `0x004057f5`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_4057f5(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004057fa` `0x004057fa`

_2 bytes. (leaf/helper — see body)_

```c
void sub_4057fa(void)
{
    sub_4057f4();
    return;
}
```

## `sub_004057fc` `0x004057fc`

_2 bytes. (leaf/helper — see body)_

```c
void sub_4057fc(unsigned int a0)
{
    return;
}
```

## `sub_004057fe` `0x004057fe`

_10 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420724;

int sub_4057fe(void)
{
    unsigned int v1;  // eax

    g_420724 = g_420724 - 1;
    return v1;
}
```

## `sub_0040580c` `0x0040580c`

_3 bytes. (leaf/helper — see body)_

```c
int sub_40580c(void)
{
    unsigned int v1;  // eax

    while (true)
    {
        InterlockedIncrement(v1);
    }
}
```

## `sub_0040582c` `0x0040582c`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40582c(void)
{
    __debugbreak();
}
```

## `sub_0040585c` `0x0040585c`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40585c(void)
{
    __unsupported_jumpkind_Ijk_Privileged()
}
```

## `sub_00405864` `0x00405864`

_1 bytes. (leaf/helper — see body)_

```c
void sub_405864(void)
{
    __unsupported_jumpkind_Ijk_Privileged()
}
```

## `sub_004058e4` `0x004058e4`

_2 bytes. (leaf/helper — see body)_

```c
void sub_4058e4(void)
{
}
```

## `sub_0040599c` `0x0040599c`

_3 bytes. (leaf/helper — see body)_

```c
void sub_40599c(void)
{
    return;
}
```

## `sub_004059a4` `0x004059a4`

_1 bytes. (leaf/helper — see body)_

```c
void sub_4059a4(void)
{
    return;
}
```

## `sub_00405a04` `0x00405a04`

_1 bytes. (leaf/helper — see body)_

```c
void sub_405a04(unsigned int a0, unsigned int a1)
{
    return;
}
```

## `sub_00405a7c` `0x00405a7c`

_40 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_42076c;

int sub_405a7c(void)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4118
    unsigned long v8;  // 4123
    unsigned long v9;  // 4139
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]
    unsigned int v2;  // [bp+0x0]

    v1 = sub_405aa5;
    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v0 = *((int *)v7);
    v8 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v8) = &v1;
    g_42076c = g_42076c + 1;
    v9 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v9) = v1;
    v2 = sub_405aac;
    return sub_405aa4();
}
```

## `sub_00405aa4` `0x00405aa4`

_1 bytes. (leaf/helper — see body)_

```c
void sub_405aa4(void)
{
    return;
}
```

## `sub_00405aa5` `0x00405aa5`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_405aa5(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_00405aaa` `0x00405aaa`

_2 bytes. (leaf/helper — see body)_

```c
void sub_405aaa(void)
{
    sub_405aa4();
    return;
}
```

## `sub_00405aac` `0x00405aac`

_2 bytes. (leaf/helper — see body)_

```c
void sub_405aac(unsigned int a0)
{
    return;
}
```

## `sub_00405aae` `0x00405aae`

_10 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_42076c;

int sub_405aae(void)
{
    unsigned int v1;  // eax

    g_42076c = g_42076c - 1;
    return v1;
}
```

## `sub_00405b6c` `0x00405b6c`

_31 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[1];
    char field_1;
} struct_0;

int sub_405b6c(void)
{
    unsigned short v4;  // cs
    unsigned int v5;  // cc_op
    unsigned int v14;  // 4101
    unsigned int v15;  // 4101
    struct_0 *v17;  // eax
    unsigned int v6;  // cc_dep1
    unsigned int v7;  // cc_dep2
    unsigned int v8;  // cc_ndep
    unsigned int v9;  // 4139
    unsigned int v10;  // cc_ndep
    unsigned int v11;  // eax
    unsigned int v12;  // cc_dep1
    unsigned int v13;  // 4140
    unsigned short v0;  // [bp-0x4]
    unsigned int v2;  // [bp+0x10]
    char *v3;  // [bp+0x18]

    v0 = v4;
    v9 = _ccall(v5, v6, v7, v8);
    v10 = v9;
    v12 = v11 - 1;
    v13 = _ccall(0, 21, v11 - 1, 0, v9);
    if ((char)v13)
        goto LABEL_0x405bb8;
    v14 = _ccall(8, 21, v12, 0, v10);
    if ((char)v14)
        goto LABEL_0x405bd8;
    v15 = _ccall(0, 21, v12, 0, v10);
    if (!((char)v15))
        goto LABEL_0x405b78;
    *(v3) = *(v3) + *((char *)&v3);
    *(v3) = *(v3) + *((char *)&v3);
    *(v3) = *(v3) + *((char *)&v3);
    *(v3) = *(v3) + *((char *)&v3);
    *(v3) = *(v3) + *((char *)&v3);
    *(v3) = *(v3) + *((char *)&v3);
    v17 = _INSERT(v3, 0, *((char *)&v3) & 92) + 1;
    v17->padding_0 = v17->padding_0 + (char)v2;
    v17->padding_0 = v17->padding_0 + *((char *)&v17);
}
```

## `sub_00405bd3` `0x00405bd3`

_16 bytes. (leaf/helper — see body)_

```c
int sub_405bd3(void)
{
    unsigned int v1;  // cc_op
    unsigned int v2;  // cc_dep1
    unsigned int v3;  // cc_dep2
    unsigned int v4;  // cc_ndep
    unsigned int v5;  // 4101
    char v6[2];  // eax
    char v7;  // 4098
    unsigned int v8;  // 4107
    char v9[2];  // eax
    char v10;  // dl

    v5 = _ccall(2, v1, v2, v3, v4);
    if ((char)v5)
    {
        v7 = v6[0];
        v6[0] = v6[0] + *((char *)&v6);
        v8 = _ccall(12, 1, (unsigned int)v7, (unsigned int)*((char *)(void*)&v6), 0);
        if ((char)v8)
            v6[0] = v6[0] + *((char *)&v6);
        v9 = &v6[1];
        v9[0] = v9[0] + v10;
        v9[0] = v9[0] + *((char *)&v9);
    }
}
```

## `sub_00405c7c` `0x00405c7c`

_39 bytes. (leaf/helper — see body)_

```c
extern char g_100040;

int sub_405c7c(void)
{
    unsigned int v2;  // 4098
    char *v3;  // eax
    unsigned int idx;  // ebx
    char v5;  // dh
    unsigned int v1;  // [bp+0x100049]

    v2 = v1;
    v1 = v2 | v3;
    if ((v2 | v3) >= 0 && (v2 | v3) < 0)
        *(v3) = *(v3) + *((char *)&v3);
    *(v3) = *(v3) + *((char *)&v3);
    *(v3) = *(v3) + *((char *)&v3);
    *(v3) = *(v3) + *((char *)&v3);
    *(v3) = *(v3) + *((char *)&v3);
    *(v3) = *(v3) + *((char *)&v3);
    *(v3) = *(v3) + *((char *)&v3);
    *(v3) = *(v3) + *((char *)&v3);
    *(v3) = *(v3) + *((char *)&v3);
    *(v3) = *(v3) + *((char *)&v3);
    *((char *)(idx * 2 + 1048640)) = *((char *)(idx * 2 + 1048640)) + v5;
    *(v3) = *(v3) + *((char *)&v3);
}
```

## `sub_00405cd4` `0x00405cd4`

_39 bytes. (leaf/helper — see body)_

```c
int sub_405cd4(void)
{
    char v2;  // 4097
    unsigned int v3;  // cc_op
    unsigned int v12;  // ebx
    char v13;  // cl
    unsigned int v4;  // cc_dep1
    unsigned int v5;  // cc_dep2
    unsigned int v6;  // cc_ndep
    unsigned int v7;  // 4109
    char v8;  // al
    char *v9;  // eax
    unsigned int v10;  // 4121
    unsigned int v11;  // 4101
    char v1;  // [bp+0x100049]

    v2 = v1;
    v7 = _ccall(v3, v4, v5, v6);
    v9 = _INSERT(v8 CONCAT 0, 0, v8 + v2 + ((char)v7 & 1));
    v10 = _ccall(8, 7, (unsigned int)v8, (unsigned int)(v2 ^ (char)v7 & 1), v7 & 1);
    if (!((char)v10))
    {
        v11 = _ccall(2, 7, (unsigned int)v8, (unsigned int)(v2 ^ (char)v7 & 1), v7 & 1);
        if ((char)v11)
            *(v9) = *(v9) + *((char *)&v9);
    }
    *(v9) = *(v9) + *((char *)&v9);
    *(v9) = *(v9) + *((char *)&v9);
    *(v9) = *(v9) + *((char *)&v9);
    *(v9) = *(v9) + *((char *)&v9);
    *(v9) = *(v9) + *((char *)&v9);
    *(v9) = *(v9) + *((char *)&v9);
    *(v9) = *(v9) + *((char *)&v9);
    *(v9) = *(v9) + *((char *)&v9);
    *(v9) = *(v9) + *((char *)&v9);
    *((char *)(/* unsupported instruction */ + v12 * 2 + 1048640)) = *((char *)(/* unsupported instruction */ + v12 * 2 + 1048640)) + v13;
    *(v9) = *(v9) + *((char *)&v9);
}
```

## `sub_00405cde` `0x00405cde`

_12 bytes. (leaf/helper — see body)_

```c
int sub_405cde(void)
{
    unsigned int v1;  // cc_op
    unsigned int v2;  // cc_dep1
    unsigned int v3;  // cc_dep2
    unsigned int v4;  // cc_ndep
    unsigned int v5;  // 4103
    unsigned int v6;  // 4109
    char *v7;  // eax

    v5 = _ccall(v1, v2, v3, v4);
    v6 = _ccall(8, 18, /* unsupported instruction */ + 1, 0, v5);
    if ((char)v6)
    {
        *(v7) = *(v7) + *((char *)&v7);
        *(v7) = *(v7) + *((char *)&v7);
        *(v7) = *(v7) + *((char *)&v7);
    }
    if ((char)(/* unsupported instruction */ == 2147483647 ? 1 : 0))
        goto LABEL_0x405d58;
    else
        goto LABEL_0x405ce4;
}
```

## `sub_00405e40` `0x00405e40`

_33 bytes. (leaf/helper — see body)_

```c
int sub_405e40(void)
{
    unsigned int v1;  // cc_op
    unsigned int v2;  // cc_dep1
    unsigned int v3;  // cc_dep2
    unsigned int v4;  // cc_ndep
    unsigned int v5;  // 4101
    unsigned int v6;  // 4101
    unsigned int v7;  // 4101
    char *v8;  // eax

    v5 = _ccall(4, v1, v2, v3, v4);
    if ((char)v5)
        goto LABEL_0x405e91;
    v6 = _ccall(6, v1, v2, v3, v4);
    if (!((char)v6))
    {
        v7 = _ccall(2, v1, v2, v3, v4);
        if ((char)v7)
            goto LABEL_405eac;
        else
            goto LABEL_0x405e46;
    }
    else
    {
        *(v8) = *(v8) + *((char *)&v8);
    }
LABEL_405eac:
    *(v8) = *(v8) + *((char *)&v8);
    *(v8) = *(v8) + *((char *)&v8);
    *(v8) = *(v8) + *((char *)&v8);
    *(v8) = *(v8) + *((char *)&v8);
    *(v8) = *(v8) + *((char *)&v8);
    *(v8) = *(v8) + *((char *)&v8);
    *(v8) = *(v8) + *((char *)&v8);
    *(v8) = *(v8) + *((char *)&v8);
    *(v8) = *(v8) + *((char *)&v8);
    *(v8) = *(v8) + *((char *)&v8);
    *(v8) = *(v8) + *((char *)&v8);
    *(v8) = *(v8) + *((char *)&v8);
}
```

## `sub_00405e98` `0x00405e98`

_38 bytes. (leaf/helper — see body)_

```c
int sub_405e98(void)
{
    char v6;  // al
    unsigned int v7;  // 4103
    unsigned int v8;  // 4109
    char v9[96];  // eax
    unsigned int v1;  // [bp+0x8]
    unsigned int v2;  // [bp+0x14]
    unsigned int v3;  // [bp+0x18]
    char idx[96];  // [bp+0x1c]
    char v5;  // [bp+0x100051]

    if (v6 || v5)
    {
        v7 = _ccall(13, (unsigned int)(v6 | v5), 0, 0);
        v8 = _ccall(2, 18, v1 + 1, 0, v7);
        if ((char)v8)
            goto LABEL_405f13;
        else
            goto LABEL_0x405ea1;
    }
    else
    {
        idx[0] = idx[0] + *((char *)&idx);
        idx[0] = idx[0] + *((char *)&idx);
        idx[0] = idx[0] + *((char *)&idx);
        idx[0] = idx[0] + *((char *)&idx);
        idx[0] = idx[0] + *((char *)&idx);
        idx[0] = idx[0] + *((char *)&idx);
    }
LABEL_405f13:
    idx[0] = idx[0] + *((char *)&idx);
    idx[0] = idx[0] + *((char *)&idx);
    idx[0] = idx[0] + *((char *)&idx);
    idx[0] = idx[0] + *((char *)&idx);
    idx[95] = idx[95] + (char)v3;
    v9 = &idx[1];
    v9[0] = v9[0] + (char)v2;
    v9[0] = v9[0] + *((char *)&v9);
}
```

## `sub_00405fa0` `0x00405fa0`

_40 bytes. (leaf/helper — see body)_

```c
int sub_405fa0(void)
{
    unsigned int v2;  // 4098
    char idx[97];  // eax
    char v4;  // dl
    char v5[97];  // eax
    unsigned int v1;  // [bp+0x100053]

    v2 = v1;
    v1 = v2 | idx;
    if (v2 || idx)
        if ((v2 | idx) < 0)
            goto LABEL_40600d;
        else
            goto LABEL_0x405fa7;
    else
        idx[0] = idx[0] + *((char *)&idx);
LABEL_40600d:
    idx[0] = idx[0] + *((char *)&idx);
    idx[0] = idx[0] + *((char *)&idx);
    idx[0] = idx[0] + *((char *)&idx);
    idx[0] = idx[0] + *((char *)&idx);
    idx[0] = idx[0] + *((char *)&idx);
    idx[0] = idx[0] + *((char *)&idx);
    idx[0] = idx[0] + *((char *)&idx);
    idx[0] = idx[0] + *((char *)&idx);
    idx[0] = idx[0] + *((char *)&idx);
    idx[0] = idx[0] + *((char *)&idx);
    idx[0] = idx[0] + *((char *)&idx);
    idx[96] = idx[96] + v4;
    v5 = &idx[1];
    v5[0] = v5[0] + v4;
    v5[0] = v5[0] + *((char *)&v5);
}
```

## `sub_00406050` `0x00406050`

_29 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[110];
    struct struct_0 *field_6e;
} struct_1;

typedef struct struct_0 {
    char padding_0[64];
    char field_40;
} struct_0;

int sub_406050(void)
{
    unsigned int v1;  // cc_op
    unsigned int v2;  // cc_dep1
    char *v11;  // eax
    char v12;  // dl
    unsigned int v3;  // cc_dep2
    unsigned int v4;  // cc_ndep
    unsigned int v5;  // 4107
    struct_1 *v6;  // ecx
    struct_0 *idx;  // ecx
    unsigned int v8;  // 4101
    unsigned int v9;  // 4101
    unsigned int v10;  // 4101

    v5 = _ccall(5, v1, v2, v3, v4);
    if ((char)v5)
    {
        idx = *((int *)&(v6->padding_0)[1]);
        v8 = _ccall(6, v1, v2, v3, v4);
        if ((char)v8)
            goto LABEL_4060b7;
        else
            goto LABEL_0x406056;
    }
    else
    {
        v9 = _ccall(6, v1, v2, v3, v4);
        if ((char)v9)
            goto LABEL_4060b7;
        else
            goto LABEL_0x406056;
    }
LABEL_4060b7:
    v10 = _ccall(2, v1, v2, v3, v4);
    if (!((char)v10))
    {
        *(v11) = *(v11) + *((char *)&v11);
        *(v11) = *(v11) + *((char *)&v11);
        *(v11) = *(v11) + *((char *)&v11);
        *(v11) = *(v11) + *((char *)&v11);
        *(v11) = *(v11) + *((char *)&v11);
        idx->field_40 = idx->field_40 + *((char *)((void*)&v11 + 1));
        *(v11) = *(v11) + v12;
        *(v11) = *(v11) + *((char *)&v11);
    }
}
```

## `sub_004060b0` `0x004060b0`

_26 bytes. (leaf/helper — see body)_

```c
int sub_4060b0(void)
{
    unsigned int v1;  // cc_op
    unsigned int v2;  // cc_dep1
    unsigned int v3;  // cc_dep2
    unsigned int v4;  // cc_ndep
    unsigned int v5;  // 4101
    unsigned int v6;  // 4101
    unsigned int v7;  // 4101
    char *v8;  // eax

    v5 = _ccall(6, v1, v2, v3, v4);
    if (!((char)v5))
        goto LABEL_0x4060b2;
    v6 = _ccall(2, v1, v2, v3, v4);
    if ((char)v6)
    {
        *(v8) = *(v8) + *((char *)&v8);
        *(v8) = *(v8) + *((char *)&v8);
        *(v8) = *(v8) + *((char *)&v8);
        *(v8) = *(v8) + *((char *)&v8);
        *(v8) = *(v8) + *((char *)&v8);
        *(v8) = *(v8) + *((char *)&v8);
        *(v8) = *(v8) + *((char *)&v8);
        *(v8) = *(v8) + *((char *)&v8);
        *(v8) = *(v8) + *((char *)&v8);
        *(v8) = *(v8) + *((char *)&v8);
    }
    v7 = _ccall(2, v1, v2, v3, v4);
    if ((char)v7)
        goto LABEL_0x4060a2;
    else
        goto LABEL_0x406117;
}
```

## `sub_004061c4` `0x004061c4`

_40 bytes. (leaf/helper — see body)_

```c
int sub_4061c4(void)
{
    char v2;  // 4097
    char v3;  // al
    char v4[2];  // eax
    char v5;  // 4142
    unsigned int v6;  // 4173
    char v7[2];  // eax
    char v8;  // dl
    char v1;  // [bp+0x100054]

    v2 = v1;
    v4 = v3 | v2;
    if ((v3 | v2) >= 0)
        if ((v3 | v2) <= 0)
            goto LABEL_406234;
        else
            goto LABEL_0x4061cb;
    else
        v4[0] = v4[0] + *((char *)&v4);
LABEL_406234:
    v4[0] = v4[0] + *((char *)&v4);
    v4[0] = v4[0] + *((char *)&v4);
    v4[0] = v4[0] + *((char *)&v4);
    v4[0] = v4[0] + *((char *)&v4);
    v4[0] = v4[0] + *((char *)&v4);
    v4[0] = v4[0] + *((char *)&v4);
    v4[0] = v4[0] + *((char *)&v4);
    v4[0] = v4[0] + *((char *)&v4);
    v4[0] = v4[0] + *((char *)&v4);
    v4[0] = v4[0] + *((char *)&v4);
    v4[0] = v4[0] + *((char *)&v4);
    v5 = v4[0];
    v4[0] = v4[0] + *((char *)&v4);
    v6 = _ccall(8, 1, (unsigned int)v5, (unsigned int)*((char *)(void*)&v4), 0);
    if ((char)v6)
        goto LABEL_0x4062b0;
    v7 = &v4[1];
    v7[0] = v7[0] + v8;
    v7[0] = v7[0] + *((char *)&v7);
}
```

## `sub_0040622a` `0x0040622a`

_28 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[1];
    char field_1;
} struct_0;

int sub_40622a(void)
{
    unsigned int v1;  // cc_op
    unsigned int v2;  // cc_dep1
    unsigned int v3;  // cc_dep2
    unsigned int v4;  // cc_ndep
    unsigned int v5;  // 4101
    unsigned int v6;  // 4101
    struct_0 *idx;  // eax
    char *v8;  // eax

    v5 = _ccall(6, v1, v2, v3, v4);
    if (!((char)v5))
        goto LABEL_0x4061bc;
    v6 = _ccall(8, v1, v2, v3, v4);
    if ((char)v6)
    {
        *(v8) = *(v8) + *((char *)&v8);
        *(v8) = *(v8) + *((char *)&v8);
        *(v8) = *(v8) + *((char *)&v8);
        *(v8) = *(v8) + *((char *)&v8);
        *(v8) = *(v8) + *((char *)&v8);
        *(v8) = *(v8) + *((char *)&v8);
        *(v8) = *(v8) + *((char *)&v8);
        *(v8) = *(v8) + *((char *)&v8);
        *(v8) = *(v8) + *((char *)&v8);
        *(v8) = *(v8) + *((char *)&v8);
    }
    idx->field_1 = idx->field_1 + *((char *)&(struct struct_0 *)&idx->field_1);
}
```

## `sub_0040632c` `0x0040632c`

_46 bytes. (leaf/helper — see body)_

```c
int sub_40632c(void)
{
    char v2;  // 4098
    unsigned int v3;  // cc_op
    unsigned int v4;  // cc_dep1
    unsigned int v5;  // cc_dep2
    unsigned int v6;  // cc_ndep
    unsigned int v7;  // 4109
    char *v8;  // eax
    unsigned int v9;  // 4121
    unsigned int v10;  // 4101
    char v1;  // [bp+0x100045]

    v2 = v1;
    v7 = _ccall(v3, v4, v5, v6);
    v1 = v2 + *((char *)&v8) + ((char)v7 & 1);
    v9 = _ccall(2, 7, (unsigned int)v2, (unsigned int)(*((char *)(void*)&v8) ^ (char)v7 & 1), v7 & 1);
    if ((char)v9)
    {
        v10 = _ccall(2, 7, (unsigned int)v2, (unsigned int)(*((char *)(void*)&v8) ^ (char)v7 & 1), v7 & 1);
    }
    else
    {
        *(v8) = *(v8) + *((char *)&v8);
        *(v8) = *(v8) + *((char *)&v8);
    }
    *(v8) = *(v8) + *((char *)&v8);
    *(v8) = *(v8) + *((char *)&v8);
    *(v8) = *(v8) + *((char *)&v8);
    *(v8) = *(v8) + *((char *)&v8);
    *(v8) = *(v8) + *((char *)&v8);
    *(v8) = *(v8) + *((char *)&v8);
    *(v8) = *(v8) + *((char *)&v8);
    *(v8) = *(v8) + *((char *)&v8);
    *(v8) = *(v8) + *((char *)&v8);
    *(v8) = *(v8) + *((char *)&v8);
    205562916();
}
```

## `sub_004063ec` `0x004063ec`

_35 bytes. (leaf/helper — see body)_

```c
char [3] sub_4063ec(unsigned int a0, unsigned int a1, unsigned int a2, char *a3, char a4, char a5, char *a6, unsigned int a7, unsigned int a8)
{
    unsigned int v0;  // cc_op
    unsigned int v1;  // cc_dep1
    unsigned int v11;  // 4109
    unsigned int v12;  // ebp
    char v13[3];  // eax
    char v14;  // 4103
    unsigned int v15;  // 4136
    char v16[3];  // eax
    char v17;  // 4114
    unsigned int v18;  // cc_dep1
    unsigned int v19;  // cc_dep2
    unsigned int v2;  // cc_dep2
    unsigned int v20;  // 4159
    unsigned int v3;  // cc_ndep
    unsigned int v4;  // 4101
    unsigned int v5;  // 4104
    unsigned int v6;  // ebp
    unsigned int v7;  // ebx
    unsigned int v8;  // 4125
    unsigned int v9;  // 4103

    v4 = _ccall(4, v0, v1, v2, v3);
    if ((char)v4)
        goto LABEL_0x406454;
    v5 = _ccall(v0, v1, v2, v3);
    v6 = a1;
    v8 = _ccall(2, 18, v7 + 1, 0, v5);
    if ((char)v8)
    {
        v9 = _ccall(18, v7 + 1, 0, v5);
        v11 = _ccall(2, 18, v6 + 1, 0, v9);
        v12 = v6 + 1;
        if ((char)v11)
            goto LABEL_406467;
        else
            goto LABEL_0x4063f5;
    }
    else
    {
        __unsupported_jumpkind_Ijk_NoDecode()
        v12 = v6;
    }
LABEL_406467:
    v13 = a6 + 1;
    v13[0] = v13[0] + a5;
    v14 = v13[0];
    v13[0] = v13[0] + *((char *)&v13);
    v15 = _ccall(1, (unsigned int)v14, (unsigned int)*((char *)(void*)&v13), 0);
    v13[0] = v13[0] - a4 - ((char)v15 & 1);
    v16 = &v13[1];
    v17 = v16[0];
    v16[0] = v17 + a5;
    v18 = v17;
    v19 = a5;
    a6 = a3;
    v20 = _ccall(8, 1, (unsigned int)v17, (unsigned int)a5, 0);
    if ((char)v20)
        goto LABEL_0x406475;
    else
        goto LABEL_0x4064e8;
}
```

## `sub_0040645c` `0x0040645c`

_10 bytes. (leaf/helper — see body)_

```c
int sub_40645c(void)
{
    unsigned int v1;  // cc_op
    unsigned int v2;  // cc_dep1
    unsigned int v3;  // cc_dep2
    unsigned int v4;  // cc_ndep
    unsigned int v5;  // 4123
    unsigned int *v6;  // ebx
    char *v7;  // eax

    v5 = _ccall(v1, v2, v3, v4);
    *(v6) = &v7[*(v6) + (v5 & 1)];
    *(v7) = *(v7) + *((char *)&v7);
    *(v7) = *(v7) + *((char *)&v6);
}
```

## `sub_00406479` `0x00406479`

_2 bytes. (leaf/helper — see body)_

```c
void sub_406479(void)
{
    unsigned int v1;  // cc_op
    unsigned int v2;  // cc_dep1
    unsigned int v3;  // cc_dep2
    unsigned int v4;  // cc_ndep
    unsigned int v5;  // 4101

    v5 = _ccall(2, v1, v2, v3, v4);
    if ((char)v5)
        goto LABEL_0x40647b;
    else
        goto LABEL_0x406406;
}
```

## `sub_004064ac` `0x004064ac`

_31 bytes. (leaf/helper — see body)_

```c
int sub_4064ac(void)
{
    int v1;  // ecx
    int v2;  // edx
    int v3;  // edi
    int v4;  // esi
    int v5;  // ebx

    sub_407a78(v1, v2, v3, v4, v5);
    sub_403470(v1, v2, v3, v4, v5);
}
```

## `sub_004064ce` `0x004064ce`

_2 bytes. (leaf/helper — see body)_

```c
void sub_4064ce(void)
{
    sub_4064d0();
    return;
}
```

## `sub_004064d0` `0x004064d0`

_17 bytes. (leaf/helper — see body)_

```c
void sub_4064d0(int a0, unsigned int a1)
{
    int v1;  // ebx

    sub_4028f0(a0, v1);
    if (!a0)
        goto LABEL_0x4064e3;
    else
        goto LABEL_0x4064e1;
}
```

## `sub_00406500` `0x00406500`

_77 bytes. (leaf/helper — see body)_

```c
int sub_406500(void)
{
    int iter;  // edi
    unsigned int v6;  // edx
    int v0;  // [bp-0x10]
    int v1;  // [bp-0xc]
    int v2;  // [bp-0x8]
    int v3;  // [bp-0x4]

    iter = sub_403c80(v0, v1, v2, v3);
    sub_403e78(v0, v1, v2, v3);
    if (iter <= 0)
        return;
    while (true)
    {
        if (*((char *)(v6 + iter - 1)) && sub_4066d0())
        {
            if ((char)sub_4081fc() == 2)
                iter -= 1;
            else
                return;
        }
        iter -= 1;
        if (iter <= 0)
            return;
    }
}
```

## `sub_0040654d` `0x0040654d`

_3 bytes. (leaf/helper — see body)_

```c
int sub_40654d(void)
{
    sub_406550();
    return;
}
```

## `sub_00406550` `0x00406550`

_40 bytes. (leaf/helper — see body)_

```c
int sub_406550(void)
{
    int v1;  // edi
    int v2;  // esi
    int v3;  // ebx
    int v4;  // edx

    sub_406500(v1, v2, v3);
    sub_403ed8(v4);
    return;
}
```

## `sub_00406583` `0x00406583`

_42 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[86];
    char field_56;
} struct_0;

int sub_406583(void)
{
    struct_0 *idx;  // ebx
    int v2;  // edx
    int v3;  // edi

    idx->field_56 = idx->field_56 + (char)v2;
    sub_406500(v3);
    sub_403ed8(v2);
    return;
}
```

## `sub_004065bb` `0x004065bb`

_116 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    int field_0;
    unsigned int field_4;
} struct_0;

int sub_4065bb(void)
{
    char v12;  // dl
    unsigned int v13;  // ebx
    PSTR v14;  // eax
    int v15;  // eax
    struct_0 *v16;  // ecx
    unsigned int v17;  // edx
    int v18;  // eax
    struct_0 *v19;  // ecx
    unsigned int v0;  // [bp-0x1c]
    char v2;  // [bp+0xfff8f]
    unsigned int v3;  // [bp+0xfffec]
    unsigned int v4;  // [bp+0xffff0]
    int v5;  // [bp+0xffff4]
    int v6;  // [bp+0xffff8]
    int v7;  // [bp+0xffffc]
    int v8;  // [bp+0x100000]
    PSTR v9;  // [bp+0x10000c]
    struct_0 *v10;  // [bp+0x100010]
    struct_0 *v11;  // [bp+0x100014]

    v2 += v12;
    v0 = v13;
    v14 = v9;
    if (!v9)
        v14 = NULL;
    GetDiskFreeSpaceA(v14, /* unsupported instruction */ - 4, /* unsupported instruction */ - 8, /* unsupported instruction */ - 12, /* unsupported instruction */ - 16);
    v3 = v8 * v7;
    v4 = 0;
    v15 = sub_404494(v6, 0);
    v16 = v10;
    v16->field_0 = v15;
    v16->field_4 = v17;
    v18 = sub_404494(v5, 0);
    v19 = v11;
    v19->field_0 = v18;
    v19->field_4 = v17;
    return;
}
```

## `sub_0040662f` `0x0040662f`

_1 bytes. (leaf/helper — see body)_

```c
int sub_40662f(void)
{
    sub_406630();
    return;
}
```

## `sub_00406630` `0x00406630`

_23 bytes. (leaf/helper — see body)_

```c
int sub_406630(void)
{
    char *v1;  // edi

    do
    {
        if (false)
            break;
    } while (*(v1));
    return;
}
```

## `sub_00406647` `0x00406647`

_1 bytes. (leaf/helper — see body)_

```c
int sub_406647(void)
{
    sub_406648();
    return;
}
```

## `sub_00406648` `0x00406648`

_13 bytes. (leaf/helper — see body)_

```c
int sub_406648(void)
{
    int v0;  // [bp-0x4]

    sub_402628(v0);
    return;
}
```

## `sub_00406655` `0x00406655`

_3 bytes. (leaf/helper — see body)_

```c
int sub_406655(void)
{
    sub_406658();
    return;
}
```

## `sub_00406658` `0x00406658`

_49 bytes. (leaf/helper — see body)_

```c
int sub_406658(void)
{
    void* v1;  // edx
    void* v2;  // edi
    void* iter;  // edi
    void* node;  // esi
    unsigned int v12;  // ecx
    unsigned int v3;  // ecx
    unsigned int v4;  // ecx
    unsigned int v5;  // cc_dep1
    unsigned int v6;  // ecx
    unsigned int v8;  // ebx
    unsigned int v9;  // ecx

    v2 = v1;
    v4 = v3;
    v5 = v3;
    v6 = v3;
    if (v4)
    {
        do
        {
            if (!v4)
                break;
        } while (*((char *)v2));
        v6 = v4;
        if (!v5)
            v6 = v4 + 1;
    }
    v8 = v3 - v6;
    for (v9 = v8 >> 2; v9; node += 4)
    {
        v9 -= 1;
        *((int *)iter) = *((int *)node);
        iter += 4;
    }
    for (v12 = v8 & 3; v12; node += 1)
    {
        v12 -= 1;
        *((char *)iter) = *((char *)node);
        iter += 1;
    }
    *((char *)iter) = 0;
    return;
}
```

## `sub_00406689` `0x00406689`

_3 bytes. (leaf/helper — see body)_

```c
int sub_406689(void)
{
    sub_40668c();
    return;
}
```

## `sub_0040668c` `0x0040668c`

_66 bytes. (leaf/helper — see body)_

```c
int sub_40668c(void)
{
    unsigned int v1;  // eax
    char *v2;  // edx
    char *v11;  // edi
    void* v12;  // esi
    unsigned int v13;  // 4101
    char *v3;  // edi
    unsigned int v4;  // ecx
    unsigned int v5;  // ecx
    unsigned int v6;  // ebx
    unsigned int v7;  // cc_op
    unsigned int v8;  // cc_dep1
    unsigned int v9;  // cc_dep2
    unsigned int v10;  // edx

    v1 = 0;
    v3 = v2;
    v5 = v4;
    if (!v5)
        return;
    do
    {
        if (!v5)
            break;
    } while (*(v3));
    v6 = v4 - v5;
    v7 = 15;
    v8 = 0;
    v9 = 0;
    v10 = 0;
    while (true)
    {
        if (!v6)
            goto LABEL_4066a7;
        if (*((char *)v12) == *(v11))
            continue;
LABEL_4066a7:
        v13 = _ccall(4, v7, v8, v9, 0);
        if ((char)v13)
            return;
        v8 = _INSERT(v1, 0, (char)v12[1]);
        if ((char)v12[1] >= 97 && (char)v8 <= 122)
            v8 = _INSERT(v8, 0, (char)v8 - 32);
        v9 = _INSERT(v10, 0, v11[1]);
        if (v11[1] >= 97 && (char)v9 <= 122)
            v9 = _INSERT(v9, 0, (char)v9 - 32);
        v7 = 6;
        v1 = v8 - v9;
        v10 = v9;
        if (v8 != v10)
            return;
    }
}
```

## `sub_004066ce` `0x004066ce`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4066ce(void)
{
    sub_4066d0();
    return;
}
```

## `sub_004066d0` `0x004066d0`

_32 bytes. (leaf/helper — see body)_

```c
int sub_4066d0(void)
{
    char *v2;  // eax
    char *v3;  // edi
    unsigned int v4;  // ecx
    char i;  // dl
    char *v0;  // [bp-0x8]

    v0 = v2;
    do
    {
        if (false)
            break;
    } while (*(v3));
    v4 = ~(4294967295);
    do
    {
        if (!v4)
            break;
    } while (i != *(v0));
    return;
}
```

## `sub_004066f0` `0x004066f0`

_88 bytes. (leaf/helper — see body)_

```c
int sub_4066f0(void)
{
    unsigned int v4;  // ecx
    unsigned int v5;  // ebx
    int v0;  // [bp-0x34]
    char *v1;  // [bp-0x14]
    char v2;  // [bp-0x10]

    v5 = v4;
    if (v5 > 31)
        v5 = 31;
    if ((char)sub_408220() == 1)
        v5 -= 1;
    sub_406648();
    *((char *)&v0 + v5) = 0;
    v1 = &v0;
    v2 = 6;
    sub_4064ac();
    return;
}
```

## `sub_00406748` `0x00406748`

_18 bytes. (leaf/helper — see body)_

```c
int sub_406748(void)
{
    sub_40447c();
    return;
}
```

