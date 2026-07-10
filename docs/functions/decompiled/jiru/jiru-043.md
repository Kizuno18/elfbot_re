# elfbot.dll decompiled — jiru 0x10334350..0x10335900

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10334350` `0x10334350`

_22 bytes. (leaf/helper — see body)_

```c
int sub_10334350(int a0)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10334370(a0, &v1);
    return a0;
}
```

## `sub_10334370` `0x10334370`

_73 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
    unsigned int field_4;
} struct_0;

typedef struct struct_0 {
    char padding_0[4];
    void* field_4;
    char padding_8[16];
    unsigned int field_18;
} struct_0;

struct_0 * sub_10334370(struct_0 *a0)
{
    unsigned int v2;  // eax
    struct_0 *idx;  // [bp-0x8]

    idx = a0;
    idx = a0;
    if (idx->field_0 != 0xfffffffe)
    {
        if (!idx->field_0)
            sub_10353616();
        v2 = sub_1031a4a0(idx->field_0);
        if (idx->field_4 <= v2)
            sub_10353616();
    }
    idx->field_4 = idx->field_4 - 2;
    return idx;
}
```

## `sub_103343c0` `0x103343c0`

_112 bytes. (leaf/helper — see body)_

```c
int sub_103343c0(int a0, char a1, unsigned int a2, char a3, unsigned int a4, int a5, int a6)
{
    unsigned int v2;  // ecx
    char v3;  // al
    int v4;  // eax
    int v5;  // ecx
    int v6;  // edx
    int v7;  // eax
    int v0;  // [bp-0x8], Other Possible Types: unsigned int
    char v1;  // [bp+0x0]

    v0 = v2;
    v0 = _INSERT(v2, 3, 0);
    v3 = sub_10337970(&/* unsupported instruction */, &/* unsupported instruction */, v0, &v1);
    *((char *)&v0 + 2) = v3;
    v4 = _INSERT(v3, 0, *((char *)((void*)&v0 + 3)));
    v5 = _INSERT(0, 0, *((char *)((void*)&v0 + 2)));
    v6 = _INSERT(0, 0, *((char *)sub_103378b0((char *)&v0 + 1, &/* unsupported instruction */, &/* unsupported instruction */, v5, v4)));
    v7 = sub_10337840(&/* unsupported instruction */, sub_10337840(&/* unsupported instruction */, a5, a6, v6));
    sub_10337860(a0, v7);
    return a0;
}
```

## `sub_10334430` `0x10334430`

_20 bytes. (leaf/helper — see body)_

```c
int sub_10334430(unsigned int a0, int a1)
{
    char v0;  // [bp+0x0]

    sub_10335b30(a1, &v0);
    return a0;
}
```

## `sub_10334450` `0x10334450`

_112 bytes. (leaf/helper — see body)_

```c
int sub_10334450(int a0, char a1, unsigned int a2, char a3, unsigned int a4, int a5, int a6)
{
    unsigned int v2;  // ecx
    char v3;  // al
    int v4;  // eax
    int v5;  // ecx
    int v6;  // edx
    int v7;  // eax
    int v0;  // [bp-0x8], Other Possible Types: unsigned int
    char v1;  // [bp+0x0]

    v0 = v2;
    v0 = _INSERT(v2, 3, 0);
    v3 = sub_10337970(&/* unsupported instruction */, &/* unsupported instruction */, v0, &v1);
    *((char *)&v0 + 2) = v3;
    v4 = _INSERT(v3, 0, *((char *)((void*)&v0 + 3)));
    v5 = _INSERT(0, 0, *((char *)((void*)&v0 + 2)));
    v6 = _INSERT(0, 0, *((char *)sub_103378b0((char *)&v0 + 1, &/* unsupported instruction */, &/* unsupported instruction */, v5, v4)));
    v7 = sub_10337840(&/* unsupported instruction */, sub_10337840(&/* unsupported instruction */, a5, a6, v6));
    sub_103378c0(a0, v7);
    return a0;
}
```

## `sub_103344c0` `0x103344c0`

_45 bytes. (leaf/helper — see body)_

```c
int sub_103344c0(int a0, int a1, int a2, int a3, int a4, int a5)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10337910(a1, a2, a3, a4, a5, a0, a0, &v1);
}
```

## `sub_103344f0` `0x103344f0`

_63 bytes. (leaf/helper — see body)_

```c
unsigned int sub_103344f0(unsigned int a0, int a1)
{
    unsigned int v0;  // [bp-0xc]
    int v1;  // [bp-0x8], Other Possible Types: unsigned int

    if (a1 <= 0 && (a1 < 0 || a0 < 0))
    {
        v0 = -(a0);
        v1 = -(a1 + (0 < a0));
        return v0;
    }
    v0 = a0;
    v1 = a1;
    return v0;
}
```

## `sub_10334530` `0x10334530`

_5 bytes. (leaf/helper — see body)_

```c
void sub_10334530(void)
{
    return;
}
```

## `sub_10334540` `0x10334540`

_372 bytes. (leaf/helper — see body)_

```c
void* sub_10334540(void* a0, void* a1, unsigned int a2)
{
    void* v2;  // edx
    unsigned int v3;  // edx
    unsigned int v4;  // ecx
    void* v5;  // ecx
    unsigned int v6;  // ecx
    unsigned int v7;  // edx
    unsigned int v8;  // eax
    unsigned int v0;  // [bp-0x10]
    void* v1;  // [bp-0x8]

    v1 = a0;
    v1 = a0;
    if (sub_10332660(v1) || sub_10332660(a2))
    {
        if (sub_10332a00(v1) || sub_10332a00(a2))
        {
            sub_10330cc0(a1);
            return a1;
        }
        v2 = v1;
        v0 = (int)v2[4];
        if (sub_10330d20(*((int *)v2), v2, *((int *)v2)) && !((v0 = v3, !sub_10330d20(v4, v3, sub_1032ff80(a2)))) || !((v5 = v1, v0 = (unsigned int)(int)v5[4], !sub_103325c0(v5, (int)v5[4], *((int *)v5)) || (v0 = v3, !sub_103325c0(v4, v3, sub_1032ff80(a2))))))
        {
            sub_10330cc0(a1);
            return a1;
        }
        else if (sub_10332970(v1, v3))
        {
            v6 = (int)v1[4];
            *((int *)a1) = *((int *)v1);
            *((unsigned int *)&a1[4]) = v6;
            return a1;
        }
        else
        {
            v0 = v3;
            if (sub_10330d20(v4, v3, sub_1032ff80(a2)))
            {
                sub_10330c90(a1, v3, a1);
                return a1;
            }
            v0 = v3;
            v7 = sub_103325c0(v4, v3, sub_1032ff80(a2));
            if (v7)
            {
                sub_10330c60(v4, v7, a1);
                return a1;
            }
        }
    }
    v8 = sub_1032ff80(a2);
    sub_1032fad0(a1, *((int *)v1) - v8, (int)v1[4] - v3 - (*((int *)v1) < v8));
    return a1;
}
```

## `sub_103346c0` `0x103346c0`

_106 bytes. (leaf/helper — see body)_

```c
int sub_103346c0(unsigned int *a0)
{
    unsigned int v3;  // eax
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp+0x0]

    v0 = *(a0);
    v1 = a0[1];
    v3 = *(a0);
    return sub_10354870(v3 + 0x2ac18000, a0[1] - 27111902 - (v3 < 0xd53e8000), 10, 0, 0xd53e8000, 27111902, 0xd53e8000, 0, v3 + 0x2ac18000, a0[1] - 27111902 - (v3 < 0xd53e8000), 27111902, 0, &v2);
}
```

## `sub_10334730` `0x10334730`

_64 bytes. (leaf/helper — see body)_

```c
char sub_10334730(int a0, int a1, int a2, int a3)
{
    unsigned int v2;  // ecx
    char v3;  // al
    int v4;  // eax
    int v5;  // ecx
    int v0;  // [bp-0x8], Other Possible Types: unsigned int
    char v1;  // [bp+0x0]

    v0 = v2;
    v0 = _INSERT(v2, 3, 0);
    v3 = sub_10337970(&/* unsupported instruction */, &/* unsupported instruction */, v0, &v1);
    *((char *)&v0 + 2) = v3;
    v4 = _INSERT(v3, 0, *((char *)((void*)&v0 + 3)));
    v5 = _INSERT(0, 0, *((char *)((void*)&v0 + 2)));
    return sub_10337980(a0, a1, a2, a3, v5, v4);
}
```

## `sub_10334770` `0x10334770`

_64 bytes. (leaf/helper — see body)_

```c
char sub_10334770(int a0, int a1, int a2, int a3)
{
    unsigned int v2;  // ecx
    char v3;  // al
    int v4;  // eax
    int v5;  // ecx
    int v0;  // [bp-0x8], Other Possible Types: unsigned int
    char v1;  // [bp+0x0]

    v0 = v2;
    v0 = _INSERT(v2, 3, 0);
    v3 = sub_10337970(&/* unsupported instruction */, &/* unsupported instruction */, v0, &v1);
    *((char *)&v0 + 2) = v3;
    v4 = _INSERT(v3, 0, *((char *)((void*)&v0 + 3)));
    v5 = _INSERT(0, 0, *((char *)((void*)&v0 + 2)));
    return sub_103379a0(a0, a1, a2, a3, v5, v4);
}
```

## `sub_103347b0` `0x103347b0`

_64 bytes. (leaf/helper — see body)_

```c
char sub_103347b0(int a0, int a1, int a2, int a3)
{
    unsigned int v2;  // ecx
    char v3;  // al
    int v4;  // eax
    int v5;  // ecx
    int v0;  // [bp-0x8], Other Possible Types: unsigned int
    char v1;  // [bp+0x0]

    v0 = v2;
    v0 = _INSERT(v2, 3, 0);
    v3 = sub_10337970(&/* unsupported instruction */, &/* unsupported instruction */, v0, &v1);
    *((char *)&v0 + 2) = v3;
    v4 = _INSERT(v3, 0, *((char *)((void*)&v0 + 3)));
    v5 = _INSERT(0, 0, *((char *)((void*)&v0 + 2)));
    return sub_103379c0(a0, a1, a2, a3, v5, v4);
}
```

## `sub_103347f0` `0x103347f0`

_162 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern int g_1039d580;

unsigned int sub_103347f0(int a0)
{
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // fs
    unsigned long v13;  // 4137
    unsigned long v14;  // 4151
    unsigned int v15;  // eax
    unsigned long v16;  // 4113
    int v0;  // [bp-0x9c]
    unsigned int v1;  // [bp-0x98]
    int v2;  // [bp-0x94]
    int v3;  // [bp-0x90]
    char v4;  // [bp-0x8c]
    char v5;  // [bp-0x4c]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]
    char v9;  // [bp-0x4]

    v8 = 4294967295;
    v7 = sub_1036e118;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v6 = *((int *)v13);
    v1 = g_1038e180 ^ &v9;
    v14 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v14) = &v6;
    v0 = a0;
    sub_10334530();
    v3 = sub_10337a80(&v5, a0);
    v2 = v3;
    v8 = 0;
    sub_10337ae0(&v4, v2);
    sub_103533ea(&v4, &g_1039d580);
    v8 = 4294967295;
    v15 = sub_10336490(&v4, &g_1039d580);
    v16 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v16) = v6;
    return v15;
}
```

## `sub_103348a0` `0x103348a0`

_162 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern int g_1039d634;

unsigned int sub_103348a0(int a0)
{
    unsigned long v10;  // ldt
    unsigned long v11;  // gdt
    unsigned short v12;  // fs
    unsigned long v13;  // 4137
    unsigned long v14;  // 4151
    unsigned int v15;  // eax
    unsigned long v16;  // 4113
    int v0;  // [bp-0x9c]
    unsigned int v1;  // [bp-0x98]
    int v2;  // [bp-0x94]
    int v3;  // [bp-0x90]
    char v4;  // [bp-0x8c]
    char v5;  // [bp-0x4c]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]
    char v9;  // [bp-0x4]

    v8 = 4294967295;
    v7 = sub_1036e148;
    v13 = _ccall(v10, v11, (unsigned int)v12, 0);
    v6 = *((int *)v13);
    v1 = g_1038e180 ^ &v9;
    v14 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int **)v14) = &v6;
    v0 = a0;
    sub_10334530();
    v3 = sub_10337b40(&v5, a0);
    v2 = v3;
    v8 = 0;
    sub_10337ba0(&v4, v2);
    sub_103533ea(&v4, &g_1039d634);
    v8 = 4294967295;
    v15 = sub_10336680(&v4, &g_1039d634);
    v16 = _ccall(v10, v11, (unsigned int)v12, 0);
    *((unsigned int *)v16) = v6;
    return v15;
}
```

## `sub_10334950` `0x10334950`

_366 bytes. (leaf/helper — see body)_

```c
void* sub_10334950(void* a0, void* a1, unsigned int a2)
{
    void* v2;  // edx
    void* v3;  // ecx
    unsigned int v4;  // edx
    unsigned int v5;  // ecx
    unsigned int v6;  // edx
    unsigned int v7;  // ecx
    unsigned int v8;  // eax
    unsigned int v0;  // [bp-0xc]
    void* v1;  // [bp-0x8]

    v1 = a0;
    v1 = a0;
    if (sub_10332660(v1) || (char)sub_10334b50())
    {
        if (sub_10332a00(v1) || (char)sub_10334b20())
        {
            sub_10330cc0(a1);
            return a1;
        }
        v2 = v1;
        v0 = (int)v2[4];
        if (sub_10330d20(*((int *)v2), v2, *((int *)v2)) && (char)sub_10334ac0(sub_10336b20()) || !((v3 = v1, v0 = (unsigned int)(int)v3[4], !sub_103325c0(v3, (int)v3[4], *((int *)v3)) || !(char)sub_10334af0(sub_10336b20()))))
        {
            sub_10330cc0(a1);
            return a1;
        }
        else if (sub_10332970(v1, v4))
        {
            v5 = (int)v1[4];
            *((int *)a1) = *((int *)v1);
            *((unsigned int *)&a1[4]) = v5;
            return a1;
        }
        else if ((char)sub_10334af0(sub_10336b20()))
        {
            sub_10330c60(a1, v4, a1);
            return a1;
        }
        else
        {
            v6 = sub_10334ac0(sub_10336b20()) & 0xff;
            if (v6)
            {
                sub_10330c90(v7, v6, a1);
                return a1;
            }
        }
    }
    v8 = sub_10336b20();
    sub_1032fad0(a1, v8 + *((int *)v1), (int)v1[4] + (v8 + *((int *)v1) < v8));
    return a1;
}
```

## `sub_10334ac0` `0x10334ac0`

_37 bytes. (leaf/helper — see body)_

```c
char sub_10334ac0(unsigned int a0)
{
    int v1;  // ecx
    char v0;  // [bp+0x0]

    sub_1032fd30(&/* unsupported instruction */);
    return a0 == sub_10336b20(v1, &v0);
}
```

## `sub_10334af0` `0x10334af0`

_37 bytes. (leaf/helper — see body)_

```c
char sub_10334af0(unsigned int a0)
{
    int v1;  // ecx
    char v0;  // [bp+0x0]

    sub_1032fd00(&/* unsupported instruction */);
    return a0 == sub_10336b20(v1, &v0);
}
```

## `sub_10334b20` `0x10334b20`

_44 bytes. (leaf/helper — see body)_

```c
char sub_10334b20(unsigned int *a0)
{
    unsigned int v2;  // eax
    char v0;  // [bp-0x8]

    sub_1032fd60(&v0);
    v2 = sub_10336b20(a0);
    return *(a0) == v2;
}
```

## `sub_10334b50` `0x10334b50`

_62 bytes. (leaf/helper — see body)_

```c
char sub_10334b50(unsigned int *a0)
{
    unsigned int v0;  // [bp-0xc]

    if (!(char)sub_10334b90() && !sub_10334b20(a0))
        v0 = 0;
    else
        v0 = 1;
    return v0;
}
```

## `sub_10334b90` `0x10334b90`

_84 bytes. (leaf/helper — see body)_

```c
char sub_10334b90(unsigned int a0)
{
    unsigned int v4;  // eax
    unsigned int v5;  // eax
    unsigned int v0;  // [bp-0x14]
    char v1;  // [bp-0xc]
    char v2;  // [bp-0x8]

    sub_1032fd30(&v2);
    v4 = sub_10336b20();
    if (*((int *)a0) != v4)
    {
        sub_1032fd00(&v1);
        v5 = sub_10336b20();
        if (*((int *)a0) == v5)
            goto LABEL_10334bd6;
        v0 = 0;
    }
    else
    {
LABEL_10334bd6:
        v0 = 1;
    }
    return v0;
}
```

## `sub_10334bf0` `0x10334bf0`

_37 bytes. (leaf/helper — see body)_

```c
int sub_10334bf0(int a0, int a1, int a2, int a3)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10337c00(a1, a2, a3, a0, a0, &v1);
}
```

## `sub_10334c20` `0x10334c20`

_43 bytes. (leaf/helper — see body)_

```c
int sub_10334c20(char a0, char a0, int a1)
{
    char v0;  // [bp+0x0]

    return sub_10337c50(sub_10349d70(&/* unsupported instruction */, sub_10349d70(&/* unsupported instruction */, a1, &v0)));
}
```

## `sub_10334c50` `0x10334c50`

_97 bytes. (leaf/helper — see body)_

```c
int sub_10334c50(char a0, char a0, int a1)
{
    unsigned int v3;  // ecx
    char v4;  // al
    int v5;  // edx
    int v6;  // eax
    int v7;  // ecx
    int v0;  // [bp-0x8], Other Possible Types: unsigned int
    char v1;  // [bp+0x0]

    v0 = v3;
    v0 = _INSERT(v3, 3, 0);
    v4 = sub_10337970(&/* unsupported instruction */, v0, &v1);
    *((char *)&v0 + 2) = v4;
    v5 = _INSERT(0, 0, *((char *)((void*)&v0 + 3)));
    v6 = _INSERT(v4, 0, *((char *)((void*)&v0 + 2)));
    v7 = _INSERT(0, 0, *((char *)sub_103378b0((char *)&v0 + 1, &/* unsupported instruction */, &/* unsupported instruction */, v6, v5)));
    return sub_10337c80(sub_10349d70(&/* unsupported instruction */, sub_10349d70(&/* unsupported instruction */, a1, v7)));
}
```

## `sub_10334cc0` `0x10334cc0`

_37 bytes. (leaf/helper — see body)_

```c
int sub_10334cc0(int a0, int a1, int a2, int a3)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10337cc0(a1, a2, a3, a0, a0, &v1);
}
```

## `sub_10334cf0` `0x10334cf0`

_43 bytes. (leaf/helper — see body)_

```c
int sub_10334cf0(char a0, char a0, int a1)
{
    char v0;  // [bp+0x0]

    return sub_10337d10(sub_10349d70(&/* unsupported instruction */, sub_10349d70(&/* unsupported instruction */, a1, &v0)));
}
```

## `sub_10334d20` `0x10334d20`

_97 bytes. (leaf/helper — see body)_

```c
int sub_10334d20(char a0, char a0, int a1)
{
    unsigned int v3;  // ecx
    char v4;  // al
    int v5;  // edx
    int v6;  // eax
    int v7;  // ecx
    int v0;  // [bp-0x8], Other Possible Types: unsigned int
    char v1;  // [bp+0x0]

    v0 = v3;
    v0 = _INSERT(v3, 3, 0);
    v4 = sub_10337970(&/* unsupported instruction */, v0, &v1);
    *((char *)&v0 + 2) = v4;
    v5 = _INSERT(0, 0, *((char *)((void*)&v0 + 3)));
    v6 = _INSERT(v4, 0, *((char *)((void*)&v0 + 2)));
    v7 = _INSERT(0, 0, *((char *)sub_103378b0((char *)&v0 + 1, &/* unsupported instruction */, &/* unsupported instruction */, v6, v5)));
    return sub_10337d40(sub_10349d70(&/* unsupported instruction */, sub_10349d70(&/* unsupported instruction */, a1, v7)));
}
```

## `sub_10334d90` `0x10334d90`

_51 bytes. (leaf/helper — see body)_

```c
int sub_10334d90(int a0, int a1, int a2)
{
    int v2;  // ecx
    int v3;  // edx
    char v0;  // [bp-0x5]
    char v1;  // [bp+0x0]

    v0 = sub_10337970(&/* unsupported instruction */, &/* unsupported instruction */, v2, &v1);
    v3 = _INSERT(0, 0, v0);
    return sub_10337d80(a0, a1, a2, v3);
}
```

## `sub_10334dd0` `0x10334dd0`

_37 bytes. (leaf/helper — see body)_

```c
int sub_10334dd0(int a0, int a1, int a2, int a3)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    return sub_10337db0(a1, a2, a3, a0, a0, &v1);
}
```

## `sub_10334e00` `0x10334e00`

_43 bytes. (leaf/helper — see body)_

```c
int sub_10334e00(char a0, char a0, int a1)
{
    char v0;  // [bp+0x0]

    return sub_10337e00(sub_10349d70(&/* unsupported instruction */, sub_10349d70(&/* unsupported instruction */, a1, &v0)));
}
```

## `sub_10334e30` `0x10334e30`

_97 bytes. (leaf/helper — see body)_

```c
int sub_10334e30(char a0, char a0, int a1)
{
    unsigned int v3;  // ecx
    char v4;  // al
    int v5;  // edx
    int v6;  // eax
    int v7;  // ecx
    int v0;  // [bp-0x8], Other Possible Types: unsigned int
    char v1;  // [bp+0x0]

    v0 = v3;
    v0 = _INSERT(v3, 3, 0);
    v4 = sub_10337970(&/* unsupported instruction */, v0, &v1);
    *((char *)&v0 + 2) = v4;
    v5 = _INSERT(0, 0, *((char *)((void*)&v0 + 3)));
    v6 = _INSERT(v4, 0, *((char *)((void*)&v0 + 2)));
    v7 = _INSERT(0, 0, *((char *)sub_103378b0((char *)&v0 + 1, &/* unsupported instruction */, &/* unsupported instruction */, v6, v5)));
    return sub_10337e30(sub_10349d70(&/* unsupported instruction */, sub_10349d70(&/* unsupported instruction */, a1, v7)));
}
```

## `sub_10334ea0` `0x10334ea0`

_77 bytes. (leaf/helper — see body)_

```c
extern int g_10399bb4;

int sub_10334ea0(unsigned int a0)
{
    unsigned int v0;  // [bp-0x14]
    char v1;  // [bp-0x10]

    if (a0 <= 0)
    {
        a0 = 0;
    }
    else if ((unsigned int)(4294967295 / a0) < 28)
    {
        v0 = 0;
        sub_10315880(&v1);
        sub_103533ea(&v1, &g_10399bb4);
    }
    return sub_10350a53(a0 * 28);
}
```

## `sub_10334ef0` `0x10334ef0`

_84 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10334ef0(int a0, int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned long v10;  // 4154
    unsigned long v11;  // 4123
    unsigned int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036e178;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_103145d0(v1, a1);
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_10334f50` `0x10334f50`

_158 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390784;
extern char g_10390794;
extern char g_1039079c;

unsigned int sub_10334f50(unsigned int idx, int a1)
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
    v3 = sub_1036e1b3;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_10334ff0(a1, g_1038e180 ^ &v5);
    v4 = 0;
    v1 = (!a1 ? 0 : a1 + 60);
    v0 = v1;
    sub_10313b60(idx + 60);
    *((char **)idx) = &g_1039079c;
    *((char **)(idx + 40)) = &g_10390794;
    *((char **)(idx + 60)) = &g_10390784;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return idx;
}
```

## `sub_10334ff0` `0x10334ff0`

_148 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103907a8;
extern char g_103907b0;

int sub_10334ff0(unsigned int a0, unsigned int a1)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4139
    unsigned long v10;  // 4153
    unsigned long v11;  // 4135
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036e1e3;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_10314290(a0, a1);
    v4 = 0;
    v1 = (!a1 ? 0 : a1 + 40);
    sub_10313a80(a0 + 40, v1);
    *((char **)a0) = &g_103907b0;
    *((char **)(a0 + 40)) = &g_103907a8;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return a0;
}
```

## `sub_10335090` `0x10335090`

_158 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103907bc;
extern char g_103907cc;
extern char g_103907d4;

unsigned int sub_10335090(unsigned int idx, int a1)
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
    v3 = sub_1036e213;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_10335130(a1, g_1038e180 ^ &v5);
    v4 = 0;
    v1 = (!a1 ? 0 : a1 + 60);
    v0 = v1;
    sub_10313b60(idx + 60);
    *((char **)idx) = &g_103907d4;
    *((char **)(idx + 40)) = &g_103907cc;
    *((char **)(idx + 60)) = &g_103907bc;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return idx;
}
```

## `sub_10335130` `0x10335130`

_148 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103907e0;
extern char g_103907e8;

unsigned int * sub_10335130(unsigned int *a0, unsigned int a1)
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
    v2 = sub_1036e243;
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v1 = *((int *)v8);
    v9 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v9) = &v1;
    sub_103351d0(a1, g_1038e180 ^ &v4);
    v3 = 0;
    v0 = (!a1 ? 0 : a1 + 40);
    sub_10313a80(a0 + 10, v0);
    *(a0) = &g_103907e8;
    a0[10] = &g_103907e0;
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v10) = v1;
    return a0;
}
```

## `sub_103351d0` `0x103351d0`

_93 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1039064c;

int sub_103351d0(int a0, int a1)
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
    v3 = sub_1036e268;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_10333d80(v1, a1);
    *((char **)v1) = &g_1039064c;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_10335230` `0x10335230`

_87 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103907f4;

int sub_10335230(int a0)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4135
    unsigned int v9;  // eax
    unsigned long v10;  // 4151
    unsigned long v11;  // 4128
    int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v9 = *((int *)v8);
    v1 = *((int *)v8);
    v0 = a0;
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v10) = &v1;
    sub_10353203(g_1038e180 ^ &v2, a0, v9, sub_1036e298, -1, &v3);
    *((char **)a0) = &g_103907f4;
    v11 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v11) = v9;
    return a0;
}
```

## `sub_10335290` `0x10335290`

_16 bytes. (leaf/helper — see body)_

```c
int sub_10335290(unsigned int a0)
{
    return "boost::bad_get: failed value get using boost::get";
}
```

## `sub_103352a0` `0x103352a0`

_75 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_103352a0(int a0)
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
    v12 = sub_103532d2(g_1038e180 ^ &v3, a0, v10, sub_1036e2c8, -1, &v4);
    v13 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v13) = v10;
    return v12;
}
```

## `sub_103352f0` `0x103352f0`

_93 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103907f4;

int sub_103352f0(int a0, int a1)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4138
    unsigned int v8;  // eax
    unsigned long v9;  // 4154
    unsigned long v10;  // 4128
    int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v8 = *((int *)v7);
    v1 = *((int *)v7);
    v0 = a0;
    v9 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v9) = &v1;
    sub_1035327a(a1, g_1038e180 ^ &v2, a0, v8, sub_1036e2f8, -1, &v3);
    *((char **)a0) = &g_103907f4;
    v10 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v10) = v8;
    return a0;
}
```

## `sub_10335350` `0x10335350`

_158 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390834;
extern char g_10390844;
extern char g_1039084c;

unsigned int sub_10335350(unsigned int idx, int a1)
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
    v3 = sub_1036e333;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_103353f0(a1, g_1038e180 ^ &v5);
    v4 = 0;
    v1 = (!a1 ? 0 : a1 + 60);
    v0 = v1;
    sub_10313b60(idx + 60);
    *((char **)idx) = &g_1039084c;
    *((char **)(idx + 40)) = &g_10390844;
    *((char **)(idx + 60)) = &g_10390834;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return idx;
}
```

## `sub_103353f0` `0x103353f0`

_148 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390858;
extern char g_10390860;

unsigned int * sub_103353f0(unsigned int *a0, unsigned int a1)
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
    v2 = sub_1036e363;
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v1 = *((int *)v8);
    v9 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v9) = &v1;
    sub_10335490(a1, g_1038e180 ^ &v4);
    v3 = 0;
    v0 = (!a1 ? 0 : a1 + 40);
    sub_10313a80(a0 + 10, v0);
    *(a0) = &g_10390860;
    a0[10] = &g_10390858;
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v10) = v1;
    return a0;
}
```

## `sub_10335490` `0x10335490`

_93 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1039069c;

int sub_10335490(int a0, int a1)
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
    v3 = sub_1036e388;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_10333d80(v1, a1);
    *((char **)v1) = &g_1039069c;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_103354f0` `0x103354f0`

_158 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_1039086c;
extern char g_1039087c;
extern char g_10390884;

unsigned int sub_103354f0(unsigned int idx, int a1)
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
    v3 = sub_1036e3c3;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    sub_10335590(a1, g_1038e180 ^ &v5);
    v4 = 0;
    v1 = (!a1 ? 0 : a1 + 60);
    v0 = v1;
    sub_10313b60(idx + 60);
    *((char **)idx) = &g_10390884;
    *((char **)(idx + 40)) = &g_1039087c;
    *((char **)(idx + 60)) = &g_1039086c;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return idx;
}
```

## `sub_10335590` `0x10335590`

_148 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_10390890;
extern char g_10390898;

unsigned int * sub_10335590(unsigned int *a0, unsigned int a1)
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
    v2 = sub_1036e3f3;
    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v1 = *((int *)v8);
    v9 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v9) = &v1;
    sub_10335630(a1, g_1038e180 ^ &v4);
    v3 = 0;
    v0 = (!a1 ? 0 : a1 + 40);
    sub_10313a80(a0 + 10, v0);
    *(a0) = &g_10390898;
    a0[10] = &g_10390890;
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v10) = v1;
    return a0;
}
```

## `sub_10335630` `0x10335630`

_93 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;
extern char g_103906d0;

int sub_10335630(int a0, int a1)
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
    v3 = sub_1036e418;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = a0;
    v0 = g_1038e180 ^ &v5;
    v10 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v10) = &v2;
    v1 = a0;
    sub_10333d80(v1, a1);
    *((char **)v1) = &g_103906d0;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v11) = v2;
    return v1;
}
```

## `sub_10335690` `0x10335690`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10335690(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10336140(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_103356c0` `0x103356c0`

_44 bytes. (leaf/helper — see body)_

```c
int sub_103356c0(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_103360b0(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_103356f0` `0x103356f0`

_44 bytes. (leaf/helper — see body)_

```c
int sub_103356f0(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10336330(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_10335720` `0x10335720`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10335720(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_103362a0(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_10335750` `0x10335750`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10335750(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    sub_103352a0(v0);
    if (((char)a1 & 1))
        sub_10350abd(v0);
    return v0;
}
```

## `sub_10335780` `0x10335780`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10335780(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10336520(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_103357b0` `0x103357b0`

_44 bytes. (leaf/helper — see body)_

```c
int sub_103357b0(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10336490(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_103357e0` `0x103357e0`

_44 bytes. (leaf/helper — see body)_

```c
int sub_103357e0(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10336710(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_10335810` `0x10335810`

_44 bytes. (leaf/helper — see body)_

```c
int sub_10335810(int a0, unsigned int a1)
{
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    sub_10336680(a0, &v1);
    if (((char)a1 & 1))
        sub_10350abd(a0);
    return a0;
}
```

## `sub_10335840` `0x10335840`

_47 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[20];
    int field_14;
} struct_0;

int sub_10335840(struct_0 *a0, int a1)
{
    int v1;  // eax
    struct_0 *v0;  // [bp-0x8]

    v0 = a0;
    v0 = a0;
    v1 = sub_1031fca0(a1);
    return sub_103369f0(0, v0->field_14, a1, v1);
}
```

## `sub_10335870` `0x10335870`

_136 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10335870(unsigned int a0, int a1)
{
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4140
    unsigned long v13;  // 4154
    unsigned long v14;  // 4117
    unsigned int v0;  // [bp-0x40]
    int v1;  // [bp-0x3c]
    int v2;  // [bp-0x38]
    unsigned int v3;  // [bp-0x30]
    char v4;  // [bp-0x2c]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    char v7;  // [bp-0x8], Other Possible Types: unsigned int
    char v8;  // [bp-0x4]

    v7 = 4294967295;
    v6 = sub_1036e461;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v5 = *((int *)v12);
    v0 = g_1038e180 ^ &v8;
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v5;
    v3 = 0;
    v2 = sub_10332ce0(a0, &v4);
    v1 = v2;
    v7 = 1;
    sub_10335900(a1, a0, v1);
    v3 |= 1;
    v7 = 0;
    sub_10314610(&v4);
    v14 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v14) = v5;
    return a1;
}
```

## `sub_10335900` `0x10335900`

_88 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

int sub_10335900(int a0, unsigned int a1, int a2)
{
    unsigned long v6;  // ldt
    unsigned long v7;  // gdt
    unsigned short v8;  // fs
    unsigned long v9;  // 4138
    unsigned int v10;  // ecx
    unsigned long v11;  // 4154
    unsigned long v12;  // 4131
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    char v5;  // [bp-0x4]

    v4 = 4294967295;
    v3 = sub_1036e499;
    v9 = _ccall(v6, v7, (unsigned int)v8, 0);
    v2 = *((int *)v9);
    v1 = v10;
    v0 = g_1038e180 ^ &v5;
    v11 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int **)v11) = &v2;
    v1 = 0;
    sub_103145d0(a0, a2);
    v12 = _ccall(v6, v7, (unsigned int)v8, 0);
    *((unsigned int *)v12) = v2;
    return a0;
}
```

