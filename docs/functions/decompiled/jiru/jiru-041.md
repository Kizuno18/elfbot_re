# elfbot.dll decompiled — jiru 0x103314c0..0x103328e0

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_103314c0` `0x103314c0`

_144 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

char * sub_103314c0(char *a0, int a1)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4139
    unsigned long v12;  // 4153
    unsigned long v13;  // 4129
    unsigned int v0;  // [bp-0x28]
    int v1;  // [bp-0x24], Other Possible Types: unsigned int
    unsigned int v2;  // [bp-0x1c]
    int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036db51;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v0 = g_1038e180 ^ &v7;
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    v2 = sub_1031a280(a0 + 4);
    v3 = sub_1031acf0(28, v2);
    v6 = 0;
    if (v3)
        v1 = sub_103145d0(v3, a1);
    else
        v1 = 0;
    *(a0) = 1;
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v13) = v4;
    return a0;
}
```

## `sub_10331550` `0x10331550`

_32 bytes. (leaf/helper — see body)_

```c
int sub_10331550(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10319f70(sub_10331570(a1, a0, &v1), a1);
}
```

## `sub_10331570` `0x10331570`

_34 bytes. (leaf/helper — see body)_

```c
char sub_10331570(int a0)
{
    int v2;  // eax
    char v0;  // [bp-0x6]

    v2 = _INSERT(0, 0, v0);
    return sub_10332720(sub_10332bd0(v2, a0));
}
```

## `sub_103315a0` `0x103315a0`

_32 bytes. (leaf/helper — see body)_

```c
char sub_103315a0(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10331570(a0);
    return sub_103325a0(a1, a0, &v1);
}
```

## `sub_103315c0` `0x103315c0`

_16 bytes. (leaf/helper — see body)_

```c
int sub_103315c0(char *a0)
{
    return _INSERT(a0, 0, *(a0));
}
```

## `sub_103315d0` `0x103315d0`

_144 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

char * sub_103315d0(char *a0, int a1)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4139
    unsigned long v12;  // 4153
    unsigned long v13;  // 4129
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x1c]
    int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]
    char v7;  // [bp-0x4]

    v6 = 4294967295;
    v5 = sub_1036db81;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v4 = *((int *)v11);
    v0 = g_1038e180 ^ &v7;
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v4;
    v2 = sub_1031a280(a0 + 4);
    v3 = sub_1031acf0(28, v2);
    v6 = 0;
    if (v3)
        v1 = sub_10332540(a1);
    else
        v1 = 0;
    *(a0) = 1;
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v13) = v4;
    return a0;
}
```

## `sub_10331660` `0x10331660`

_35 bytes. (leaf/helper — see body)_

```c
char * sub_10331660(char *a0)
{
    char *v2;  // eax
    char v0;  // [bp-0x6]

    v2 = a0;
    if (*(v2))
        v2 = sub_10332730(_INSERT(0, 0, v0));
    return v2;
}
```

## `sub_10331690` `0x10331690`

_19 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10331690(unsigned int a0)
{
    unsigned int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_10314de0();
}
```

## `sub_103316b0` `0x103316b0`

_672 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    unsigned int field_8;
    unsigned int field_c;
} struct_0;

extern unsigned int g_1038e180;

struct_0 * sub_103316b0(struct_0 *idx, unsigned int a1, int a2, int a3, char *a4)
{
    unsigned long v15;  // ldt
    unsigned long v16;  // gdt
    unsigned long v25;  // 4119
    unsigned short v17;  // fs
    unsigned long v18;  // 4148
    unsigned int v19;  // ebx
    unsigned int v20;  // esi
    unsigned int v21;  // edi
    unsigned long v22;  // 4170
    struct_0 *v23;  // eax
    unsigned int v24;  // eax
    unsigned int v0;  // [bp-0x40]
    unsigned int v1;  // [bp-0x3c]
    unsigned int v2;  // [bp-0x38]
    unsigned int v3;  // [bp-0x34]
    int v4;  // [bp-0x30]
    unsigned int v5;  // [bp-0x28]
    int v6;  // [bp-0x24]
    int v7;  // [bp-0x20]
    struct_0 *v8;  // [bp-0x1c], Other Possible Types: int
    char v9;  // [bp-0x15]
    char *v10;  // [bp-0x14], Other Possible Types: struct_0 *
    unsigned int v11;  // [bp-0x10]
    unsigned int v12;  // [bp-0xc]
    unsigned int v13;  // [bp-0x8]
    char v14;  // [bp-0x4]

    v13 = 4294967295;
    v12 = sub_1036dba0;
    v18 = _ccall(v15, v16, (unsigned int)v17, 0);
    v11 = *((int *)v18);
    v10 = idx;
    v3 = v19;
    v2 = v20;
    v1 = v21;
    v0 = g_1038e180 ^ &v14;
    v22 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int **)v22) = &v11;
    v10 = &v0;
    v9 = *(a4);
    v23 = sub_103303b0(idx);
    v8 = v23;
    if (a3)
    {
        v24 = sub_10331690(idx);
        if (v24 - sub_1032e2a0(idx) < a3)
        {
            v23 = sub_103319c0();
        }
        else if (v8 < sub_1032e2a0(idx) + a3)
        {
            v4 = (sub_10331690(idx) - (v8 >> 1) < v8 ? 0 : (struct struct_0 *)&v8->padding_0[v8 >> 1]);
            v8 = v4;
            if (v8 < sub_1032e2a0(idx) + a3)
                v8 = sub_1032e2a0(idx) + a3;
            v6 = sub_10314c40(idx, v8);
            v7 = v6;
            v13 = 0;
            v7 = sub_10334bf0(idx->field_4, a2, v6);
            v7 = sub_10330560(idx, v7, a3, &v9);
            sub_10334bf0(a2, idx->field_8, v7);
            v13 = 4294967295;
            a3 += sub_1032e2a0(idx);
            if (idx->field_4)
            {
                sub_1033e420(idx->field_4, idx->field_8);
                sub_1033e3d0(idx->field_4, idx->field_c - idx->field_4);
            }
            idx->field_c = v6 + v8;
            idx->field_8 = v6 + a3;
            v23 = idx;
            v23->field_4 = v6;
        }
        else if (idx->field_8 - a2 < a3)
        {
            sub_10334bf0(a2, idx->field_8, a2 + a3);
            v13 = 2;
            sub_10330560(idx, idx->field_8, a3 - (idx->field_8 - a2), &v9);
            v13 = 4294967295;
            idx->field_8 = idx->field_8 + a3;
            v23 = sub_10334c20(a2, idx->field_8 - a3, &v9);
        }
        else
        {
            v5 = idx->field_8;
            idx->field_8 = sub_10334bf0(v5 - a3, v5, idx->field_8);
            sub_10334c50(a2, v5 - a3, v5);
            v23 = sub_10334c20(a2, a2 + a3, &v9);
        }
    }
    v25 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int *)v25) = v11;
    return v23;
}
```

## `sub_103317e6` `0x103317e6`

_3 bytes. (leaf/helper — see body)_

```c
void sub_103317e6(void)
{
    sub_103317e9();
    return;
}
```

## `sub_103317e9` `0x103317e9`

_51 bytes. (leaf/helper — see body)_

```c
extern char g_10331823;

int sub_103317e9(void)
{
    int v4;  // eax
    int v1;  // [bp+0xfffe4]
    int v2;  // [bp+0xfffec]
    unsigned int v3;  // [bp+0x100000]

    sub_1033e420(v1, v4);
    sub_1033e3d0(v1, v2);
    sub_103533ea(0, 0);
    v3 = 4294967295;
    return &g_10331823;
}
```

## `sub_103318e9` `0x103318e9`

_47 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
} struct_0;

extern char g_1033191f;

int sub_103318e9(void)
{
    struct_0 *v1;  // [bp+0xfffdc]
    unsigned int v2;  // [bp+0x100000]
    unsigned int v3;  // [bp+0x100010]
    unsigned int v4;  // [bp+0x100014]

    sub_1033e420(v3 + v4, v1->field_8 + v4);
    sub_103533ea(0, 0);
    v2 = 4294967295;
    return &g_1033191f;
}
```

## `sub_103319c0` `0x103319c0`

_113 bytes. refs "vector<T> too long"_

```c
extern unsigned int g_1038e180;
extern int g_1039ce9c;

void sub_103319c0(void)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4137
    unsigned long v12;  // 4151
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x58]
    char v1;  // [bp-0x54]
    char v2;  // [bp-0x38]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036dbc8;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v3 = *((int *)v11);
    v0 = g_1038e180 ^ &v6;
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v3;
    sub_10314590(&v1, "vector<T> too long");
    v5 = 0;
    sub_10331a40(&v1);
    sub_103533ea(&v2, &g_1039ce9c);
    v5 = 4294967295;
    sub_10314610(&v1);
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v13) = v3;
    return;
}
```

## `sub_10331a40` `0x10331a40`

_93 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390714;

int sub_10331a40(int a0, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4154
    unsigned long v11;  // 4128
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036dbf8;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_1032d470(v1, a1);
    *((char **)v1) = &g_10390714;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_10331aa0` `0x10331aa0`

_84 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390714;

void sub_10331aa0(int a0)
{
    unsigned long v7;  // ldt
    unsigned long v8;  // gdt
    unsigned short v9;  // fs
    unsigned long v10;  // 4139
    unsigned long v11;  // 4155
    unsigned long v12;  // 4113
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036dc28;
    v10 = _ccall(v7, v8, (unsigned int)v9, 0);
    v2 = *((int *)v10);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int **)v11) = &v2;
    v1 = a0;
    *((char **)v1) = &g_10390714;
    v4 = 0;
    v4 = 4294967295;
    sub_1032d4e0(v1);
    v12 = _ccall(v7, v8, (unsigned int)v9, 0);
    *((unsigned int *)v12) = v2;
    return;
}
```

## `sub_10331b00` `0x10331b00`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10331b00(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_10331aa0(v0);
    if (((char)a1 & 1))
        sub_10350abd(v0);
    return v0;
}
```

## `sub_10331b30` `0x10331b30`

_19 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10331b30(unsigned int a0)
{
    unsigned int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    return sub_1031ebc0();
}
```

## `sub_10331b50` `0x10331b50`

_707 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    unsigned int field_8;
    unsigned int field_c;
} struct_0;

extern unsigned int g_1038e180;

struct_0 * sub_10331b50(struct_0 *idx, unsigned int a1, int a2, int a3, unsigned short *a4)
{
    unsigned long v15;  // ldt
    unsigned long v16;  // gdt
    unsigned long v25;  // 4119
    unsigned short v17;  // fs
    unsigned long v18;  // 4148
    unsigned int v19;  // ebx
    unsigned int v20;  // esi
    unsigned int v21;  // edi
    unsigned long v22;  // 4170
    struct_0 *v23;  // eax
    unsigned int v24;  // eax
    unsigned int v0;  // [bp-0x40]
    unsigned int v1;  // [bp-0x3c]
    unsigned int v2;  // [bp-0x38]
    unsigned int v3;  // [bp-0x34]
    int v4;  // [bp-0x30]
    unsigned int v5;  // [bp-0x28]
    int v6;  // [bp-0x24]
    int v7;  // [bp-0x20]
    struct_0 *v8;  // [bp-0x1c], Other Possible Types: int
    unsigned short v9;  // [bp-0x18]
    char *v10;  // [bp-0x14], Other Possible Types: struct_0 *
    unsigned int v11;  // [bp-0x10]
    unsigned int v12;  // [bp-0xc]
    unsigned int v13;  // [bp-0x8]
    char v14;  // [bp-0x4]

    v13 = 4294967295;
    v12 = sub_1036dc50;
    v18 = _ccall(v15, v16, (unsigned int)v17, 0);
    v11 = *((int *)v18);
    v10 = idx;
    v3 = v19;
    v2 = v20;
    v1 = v21;
    v0 = g_1038e180 ^ &v14;
    v22 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int **)v22) = &v11;
    v10 = &v0;
    v9 = *(a4);
    v23 = sub_10330630(idx);
    v8 = v23;
    if (a3)
    {
        v24 = sub_10331b30(idx);
        if (v24 - sub_103306a0(idx) < a3)
        {
            v23 = sub_10331e80();
        }
        else if (v8 < sub_103306a0(idx) + a3)
        {
            v4 = (sub_10331b30(idx) - (v8 >> 1) < v8 ? 0 : (struct struct_0 *)&v8->padding_0[v8 >> 1]);
            v8 = v4;
            if (v8 < sub_103306a0(idx) + a3)
                v8 = sub_103306a0(idx) + a3;
            v6 = sub_1031eba0(idx, v8);
            v7 = v6;
            v13 = 0;
            v7 = sub_10334cc0(idx->field_4, a2, v6);
            v7 = sub_10330850(idx, v7, a3, &v9);
            sub_10334cc0(a2, idx->field_8, v7);
            v13 = 4294967295;
            a3 += sub_103306a0(idx);
            if (idx->field_4)
            {
                sub_1033e420(idx->field_4, idx->field_8);
                sub_1033e3d0(idx->field_4, idx->field_c - idx->field_4 >> 1);
            }
            idx->field_c = v6 + v8 * 2;
            v23 = idx;
            v23->field_8 = v6 + a3 * 2;
            idx->field_4 = v6;
        }
        else if (idx->field_8 - a2 >> 1 < a3)
        {
            sub_10334cc0(a2, idx->field_8, a2 + a3 * 2);
            v13 = 2;
            sub_10330850(idx, idx->field_8, a3 - (idx->field_8 - a2 >> 1), &v9);
            v13 = 4294967295;
            idx->field_8 = idx->field_8 + a3 * 2;
            v23 = sub_10334cf0(a2, idx->field_8 - a3 * 2, &v9);
        }
        else
        {
            v5 = idx->field_8;
            idx->field_8 = sub_10334cc0(v5 - a3 * 2, v5, idx->field_8);
            sub_10334d20(a2, v5 - a3 * 2, v5);
            v23 = sub_10334cf0(a2, a2 + a3 * 2, &v9);
        }
    }
    v25 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int *)v25) = v11;
    return v23;
}
```

## `sub_10331c88` `0x10331c88`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10331c88(void)
{
    sub_10331c8b();
    return;
}
```

## `sub_10331c8b` `0x10331c8b`

_51 bytes. (leaf/helper — see body)_

```c
extern char g_10331cc5;

int sub_10331c8b(void)
{
    int v4;  // eax
    int v1;  // [bp+0xfffe4]
    int v2;  // [bp+0xfffec]
    unsigned int v3;  // [bp+0x100000]

    sub_1033e420(v1, v4);
    sub_1033e3d0(v1, v2);
    sub_103533ea(0, 0);
    v3 = 4294967295;
    return &g_10331cc5;
}
```

## `sub_10331d9a` `0x10331d9a`

_53 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
} struct_0;

extern char g_10331dd6;

int sub_10331d9a(void)
{
    struct_0 *v1;  // [bp+0xfffdc]
    unsigned int v2;  // [bp+0x100000]
    unsigned int v3;  // [bp+0x100010]
    unsigned int v4;  // [bp+0x100014]

    sub_1033e420(v3 + v4 * 2, v1->field_8 + v4 * 2);
    sub_103533ea(0, 0);
    v2 = 4294967295;
    return &g_10331dd6;
}
```

## `sub_10331e80` `0x10331e80`

_113 bytes. refs "vector<T> too long"_

```c
extern unsigned int g_1038e180;
extern int g_1039ce9c;

void sub_10331e80(void)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4137
    unsigned long v12;  // 4151
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x58]
    char v1;  // [bp-0x54]
    char v2;  // [bp-0x38]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036dc78;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v3 = *((int *)v11);
    v0 = g_1038e180 ^ &v6;
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v3;
    sub_10314590(&v1, "vector<T> too long");
    v5 = 0;
    sub_10331a40(&v2, &v1);
    sub_103533ea(&v2, &g_1039ce9c);
    v5 = 4294967295;
    sub_10314610(&v1);
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v13) = v3;
    return;
}
```

## `sub_10331f00` `0x10331f00`

_57 bytes. (leaf/helper — see body)_

```c
unsigned int [2] sub_10331f00(unsigned int *a0, unsigned int *a1, int a2)
{
    unsigned int v2[2];  // eax
    unsigned int v3;  // edx
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v0 = *(a0);
    v1 = a0[1];
    v2 = sub_103262d0(&v0, a2);
    v3 = v2[1];
    *(a1) = v2[0];
    a1[1] = v3;
    return a1;
}
```

## `sub_10331f40` `0x10331f40`

_19 bytes. (leaf/helper — see body)_

```c
void sub_10331f40(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_103327a0(a0, &v1);
    return;
}
```

## `sub_10331f60` `0x10331f60`

_33 bytes. (leaf/helper — see body)_

```c
int sub_10331f60(int a0, int a1, int a2)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10334d90(a1, a2, a0, a0, &v1);
}
```

## `sub_10331f90` `0x10331f90`

_761 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    unsigned int field_8;
    unsigned int field_c;
} struct_0;

extern unsigned int g_1038e180;

void sub_10331f90(struct_0 *idx, unsigned int a1, int a2, int a3, int a4)
{
    unsigned long v16;  // ldt
    unsigned long v17;  // gdt
    unsigned short v18;  // fs
    unsigned long v19;  // 4149
    unsigned int v20;  // ebx
    unsigned int v21;  // esi
    unsigned int v22;  // edi
    unsigned long v23;  // 4174
    unsigned int v24;  // eax
    unsigned long v25;  // 4120
    unsigned int v0;  // [bp-0x5c]
    unsigned int v1;  // [bp-0x58]
    unsigned int v2;  // [bp-0x54]
    unsigned int v3;  // [bp-0x50]
    int v4;  // [bp-0x4c]
    unsigned int v5;  // [bp-0x44]
    int v6;  // [bp-0x40]
    int v7;  // [bp-0x3c]
    int v8;  // [bp-0x38], Other Possible Types: unsigned int
    char v9;  // [bp-0x34]
    unsigned int v10;  // [bp-0x18]
    char *v11;  // [bp-0x14], Other Possible Types: struct_0 *
    unsigned int v12;  // [bp-0x10]
    unsigned int v13;  // [bp-0xc]
    char v14;  // [bp-0x8], Other Possible Types: unsigned int
    char v15;  // [bp-0x4]

    v14 = 4294967295;
    v13 = sub_1036dca8;
    v19 = _ccall(v16, v17, (unsigned int)v18, 0);
    v12 = *((int *)v19);
    v11 = idx;
    v10 = g_1038e180 ^ &v15;
    v3 = v20;
    v2 = v21;
    v1 = v22;
    v0 = v10;
    v23 = _ccall(v16, v17, (unsigned int)v18, 0);
    *((unsigned int **)v23) = &v12;
    v11 = &v0;
    sub_1031e760(&v9, a4);
    v14 = 0;
    v8 = sub_10330880(idx);
    if (a3)
    {
        v24 = (unsigned int)sub_10331f40(idx);
        if (v24 - sub_10330920(idx) < a3)
        {
            sub_10332300();
        }
        else if (v8 < sub_10330920(idx) + a3)
        {
            v4 = ((unsigned int)sub_10331f40(idx) - (v8 >> 1) < v8 ? 0 : (v8 >> 1) + v8);
            v8 = v4;
            if (v8 < sub_10330920(idx) + a3)
                v8 = sub_10330920(idx) + a3;
            v6 = sub_10332380(v8);
            v7 = v6;
            v14 = 1;
            v7 = sub_10334dd0(idx->field_4, a2, v6);
            v7 = sub_10330ad0(idx, v7, a3, &v9);
            sub_10334dd0(a2, idx->field_8, v7);
            v14 = 0;
            a3 += sub_10330920(idx);
            if (idx->field_4)
            {
                sub_10331f60(idx, idx->field_4, idx->field_8);
                sub_1033e3d0(idx->field_4, (idx->field_c - idx->field_4) / 28);
            }
            idx->field_c = v8 * 28 + v6;
            idx->field_8 = a3 * 28 + v6;
            idx->field_4 = v6;
        }
        else if ((int)((idx->field_8 - a2) / 28) < a3)
        {
            sub_10334dd0(a2, idx->field_8, a3 * 28 + a2);
            v14 = 3;
            sub_10330ad0(idx, idx->field_8, a3 - (int)((idx->field_8 - a2) / 28), &v9);
            v14 = 0;
            idx->field_8 = a3 * 28 + idx->field_8;
            sub_10334e00(a2, idx->field_8 - a3 * 28, &v9);
        }
        else
        {
            v5 = idx->field_8;
            idx->field_8 = sub_10334dd0(v5 - a3 * 28, v5, idx->field_8);
            sub_10334e30(a2, v5 - a3 * 28, v5);
            sub_10334e00(a2, a3 * 28 + a2, &v9);
        }
    }
    v14 = 4294967295;
    sub_1031a3a0(&v9);
    v25 = _ccall(v16, v17, (unsigned int)v18, 0);
    *((unsigned int *)v25) = v12;
    sub_10351225();
    return;
}
```

## `sub_103320d1` `0x103320d1`

_3 bytes. (leaf/helper — see body)_

```c
void sub_103320d1(void)
{
    sub_103320d4();
    return;
}
```

## `sub_103320d4` `0x103320d4`

_51 bytes. (leaf/helper — see body)_

```c
extern char g_1033210e;

int sub_103320d4(unsigned int a0, int a1)
{
    int v1;  // [bp+0xfffc0]
    int v2;  // [bp+0xfffc8]
    int v3;  // [bp+0xfffd0]
    unsigned int v4;  // [bp+0x100000]

    sub_10331f60(v1, v2, a1);
    sub_1033e3d0(v2, v3);
    sub_103533ea(0, 0);
    v4 = 0;
    return &g_1033210e;
}
```

## `sub_103321f4` `0x103321f4`

_53 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
} struct_0;

extern char g_10332230;

int sub_103321f4(void)
{
    struct_0 *v1;  // [bp+0xfffc0]
    unsigned int v2;  // [bp+0x100000]
    unsigned int v3;  // [bp+0x100010]
    unsigned int v4;  // [bp+0x100014]

    sub_10331f60(v1, v4 * 28 + v3, v4 * 28 + v1->field_8);
    sub_103533ea(0, 0);
    v2 = 0;
    return &g_10332230;
}
```

## `sub_10332300` `0x10332300`

_113 bytes. refs "vector<T> too long"_

```c
extern unsigned int g_1038e180;
extern int g_1039ce9c;

void sub_10332300(void)
{
    unsigned long v8;  // ldt
    unsigned long v9;  // gdt
    unsigned short v10;  // fs
    unsigned long v11;  // 4137
    unsigned long v12;  // 4151
    unsigned long v13;  // 4113
    unsigned int v0;  // [bp-0x58]
    char v1;  // [bp-0x54]
    char v2;  // [bp-0x38]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]
    char v6;  // [bp-0x4]

    v5 = 4294967295;
    v4 = sub_1036dcd8;
    v11 = _ccall(v8, v9, (unsigned int)v10, 0);
    v3 = *((int *)v11);
    v0 = g_1038e180 ^ &v6;
    v12 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int **)v12) = &v3;
    sub_10314590(&v1, "vector<T> too long");
    v5 = 0;
    sub_10331a40(&v2, &v1);
    sub_103533ea(&v2, &g_1039ce9c);
    v5 = 4294967295;
    sub_10314610(&v1);
    v13 = _ccall(v8, v9, (unsigned int)v10, 0);
    *((unsigned int *)v13) = v3;
    return;
}
```

## `sub_10332380` `0x10332380`

_27 bytes. (leaf/helper — see body)_

```c
int sub_10332380(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10334ea0(a1, 0, a0, &v1);
}
```

## `sub_103323a0` `0x103323a0`

_32 bytes. (leaf/helper — see body)_

```c
int sub_103323a0(int a0, int a1, int a2)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_103327f0(a1, a2, a0, &v1);
    return a0;
}
```

## `sub_103323c0` `0x103323c0`

_57 bytes. (leaf/helper — see body)_

```c
unsigned int [2] sub_103323c0(int *a0, unsigned int *a1, int a2)
{
    unsigned int v1[2];  // eax
    unsigned int v2;  // edx
    char v0;  // [bp+0x0]

    v1 = sub_103327d0(a2, a0, *(a0), a0[1], &v0);
    v2 = v1[1];
    *(a1) = v1[0];
    a1[1] = v2;
    return a1;
}
```

## `sub_10332400` `0x10332400`

_25 bytes. (leaf/helper — see body)_

```c
int sub_10332400(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10332840(a1, a0, &v1);
}
```

## `sub_10332420` `0x10332420`

_57 bytes. (leaf/helper — see body)_

```c
unsigned int [2] sub_10332420(int *a0, unsigned int *a1, int a2)
{
    unsigned int v1[2];  // eax
    unsigned int v2;  // edx
    char v0;  // [bp+0x0]

    v1 = sub_10332880(a2, a0, *(a0), a0[1], &v0);
    v2 = v1[1];
    *(a1) = v1[0];
    a1[1] = v2;
    return a1;
}
```

## `sub_10332460` `0x10332460`

_25 bytes. (leaf/helper — see body)_

```c
int sub_10332460(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_103328a0(a1, a0, &v1);
}
```

## `sub_10332480` `0x10332480`

_57 bytes. (leaf/helper — see body)_

```c
unsigned int [2] sub_10332480(int *a0, unsigned int *a1, int a2)
{
    unsigned int v1[2];  // eax
    unsigned int v2;  // edx
    char v0;  // [bp+0x0]

    v1 = sub_10332920(a2, a0, *(a0), a0[1], &v0);
    v2 = v1[1];
    *(a1) = v1[0];
    a1[1] = v2;
    return a1;
}
```

## `sub_103324c0` `0x103324c0`

_25 bytes. (leaf/helper — see body)_

```c
int sub_103324c0(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_103328e0(a1, a0, &v1);
}
```

## `sub_103324e0` `0x103324e0`

_93 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390714;

int sub_103324e0(int a0, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4154
    unsigned long v11;  // 4128
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036dd08;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_1032d580(v1, a1);
    *((char **)v1) = &g_10390714;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_10332540` `0x10332540`

_84 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10332540(unsigned int a0, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4154
    unsigned long v11;  // 4123
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036dd38;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_1031e760(v1, a1);
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_103325a0` `0x103325a0`

_25 bytes. (leaf/helper — see body)_

```c
int sub_103325a0(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10332940(a1, a0, &v1);
}
```

## `sub_103325c0` `0x103325c0`

_70 bytes. (leaf/helper — see body)_

```c
char sub_103325c0(unsigned int a0, unsigned int a1, int a2)
{
    unsigned int v4;  // edx
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    unsigned int v2[2];  // [bp-0xc]
    unsigned int v3;  // [bp+0x8]

    v1 = sub_1032ff80(sub_10330c90(a0, a1, v2));
    if (a2 == v1 && v3 == v4)
        v0 = 1;
    else
        v0 = 0;
    return v0;
}
```

## `sub_10332610` `0x10332610`

_70 bytes. (leaf/helper — see body)_

```c
char sub_10332610(int a0)
{
    unsigned int v4;  // edx
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    unsigned int v2[2];  // [bp-0xc]
    unsigned int v3;  // [bp+0x8]

    v1 = sub_1032ff80(sub_10330cc0(v2));
    if (a0 == v1 && v3 == v4)
        v0 = 1;
    else
        v0 = 0;
    return v0;
}
```

## `sub_10332660` `0x10332660`

_62 bytes. (leaf/helper — see body)_

```c
char sub_10332660(unsigned int a0)
{
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v1 = a0;
    if (!(char)sub_10332970() && !(char)sub_10332a00())
        v0 = 0;
    else
        v0 = 1;
    return v0;
}
```

## `sub_103326a0` `0x103326a0`

_9 bytes. (leaf/helper — see body)_

```c
unsigned short sub_103326a0(void)
{
    return 31;
}
```

## `sub_103326b0` `0x103326b0`

_9 bytes. (leaf/helper — see body)_

```c
unsigned short sub_103326b0(void)
{
    return 10000;
}
```

## `sub_103326c0` `0x103326c0`

_9 bytes. (leaf/helper — see body)_

```c
unsigned short sub_103326c0(void)
{
    return 12;
}
```

## `sub_103326d0` `0x103326d0`

_25 bytes. (leaf/helper — see body)_

```c
int sub_103326d0(int *a0)
{
    int *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10332a60(*(a0), a0, &v1);
}
```

## `sub_103326f0` `0x103326f0`

_30 bytes. (leaf/helper — see body)_

```c
int sub_103326f0(int *a0, unsigned int a1)
{
    int *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_1033a4c0(*(a0), a0, &v1);
    return a1;
}
```

## `sub_10332710` `0x10332710`

_10 bytes. (leaf/helper — see body)_

```c
void sub_10332710(void)
{
    char v0;  // [bp+0x0]

    sub_1033bb20(&v0);
    return;
}
```

## `sub_10332720` `0x10332720`

_16 bytes. (leaf/helper — see body)_

```c
int sub_10332720(unsigned int a0, unsigned int a1)
{
    return a1;
}
```

## `sub_10332730` `0x10332730`

_34 bytes. (leaf/helper — see body)_

```c
char * sub_10332730(char *a0)
{
    char *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_103257d0(sub_10331570(v0));
    *(v0) = 0;
    return v0;
}
```

## `sub_10332760` `0x10332760`

_62 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

int sub_10332760(unsigned int *a0, struct_0 *a1)
{
    unsigned int v0[2];  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    if (v0[0] != 4294967294 && (!v0[0] || v0[0] != a1->padding_0))
        sub_10353616();
    return v0[1] - a1->field_4 >> 1;
}
```

## `sub_103327a0` `0x103327a0`

_44 bytes. (leaf/helper — see body)_

```c
unsigned int sub_103327a0(void)
{
    unsigned int v4;  // ecx
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v1 = v4;
    v2 = 153391689;
    v0 = (v2 <= 0 ? 1 : v2);
    return v0;
}
```

## `sub_103327d0` `0x103327d0`

_28 bytes. (leaf/helper — see body)_

```c
int sub_103327d0(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10332ab0(a1, a0, &v1);
    return a0;
}
```

## `sub_103327f0` `0x103327f0`

_74 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    struct struct_0 *field_0;
    unsigned int field_4;
} struct_1;

typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

struct_1 * sub_103327f0(struct_1 *a0, unsigned int a1, struct_0 *a2)
{
    struct_1 *v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10341910(a0, &v1);
    if (!a2 || a2->field_4 > a1 || a1 > a2[1].padding_0)
        sub_10353616();
    a0->field_0 = a2;
    a0->field_4 = a1;
    return a0;
}
```

## `sub_10332840` `0x10332840`

_50 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

int sub_10332840(unsigned int *a0, struct_0 *a1)
{
    unsigned int v0[2];  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    if (!*(a0) || *(a0) != a1->padding_0)
        sub_10353616(a0, &v1);
    return a0[1] - a1->field_4;
}
```

## `sub_10332880` `0x10332880`

_28 bytes. (leaf/helper — see body)_

```c
int sub_10332880(int a0, int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10332b10(a1, a0, &v1);
    return a0;
}
```

## `sub_103328a0` `0x103328a0`

_52 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

int sub_103328a0(unsigned int *a0, struct_0 *a1)
{
    unsigned int v0[2];  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    if (!*(a0) || *(a0) != a1->padding_0)
        sub_10353616(a0, &v1);
    return a0[1] - a1->field_4 >> 1;
}
```

## `sub_103328e0` `0x103328e0`

_58 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

int sub_103328e0(unsigned int *a0, struct_0 *a1)
{
    unsigned int v0[2];  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    if (!*(a0) || *(a0) != a1->padding_0)
        sub_10353616(a0, &v1);
    return (a0[1] - a1->field_4) / 28;
}
```

