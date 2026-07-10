# elfbot.dll decompiled — jiru 0x10365117..0x10368550

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10365117` `0x10365117`

_113 bytes. (leaf/helper — see body)_

```c
extern char g_103a3b70;
extern unsigned int g_103a3b80[4];

unsigned int sub_10365117(int a0)
{
    unsigned int v6;  // esi
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]
    unsigned int v5;  // [bp-0x4]

    if (a0 == -2)
    {
        *((unsigned int *)sub_103575f3()) = 0;
        *((unsigned int *)sub_103575e0()) = 9;
        return 4294967295;
    }
    v5 = v6;
    if (a0 >= 0 && a0 < *((int *)&g_103a3b70) && (*((char *)((a0 & 31) * 56 + g_103a3b80[a0 >> 5] + 4)) & 1))
        return *((int *)((a0 & 31) * 56 + g_103a3b80[a0 >> 5]));
    *((unsigned int *)sub_103575f3()) = 0;
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    *((unsigned int *)sub_103575e0()) = 9;
    sub_103535f2();
    return 4294967295;
}
```

## `sub_10365188` `0x10365188`

_146 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1b8;
extern unsigned int g_103a14e8;
extern unsigned int g_103a3b80[4];

void sub_10365188(unsigned int a0)
{
    int v6;  // edi
    unsigned int idx[4];  // esi
    unsigned int v8;  // ecx
    unsigned int v9;  // edx
    unsigned int v0[4];  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp+0x0]
    unsigned int v3;  // [bp+0xfffe8]
    unsigned int v4;  // [bp+0x100000]
    int v5;  // [bp+0x10000c]

    sub_1035b0cc(&g_103a14e8, 12);
    v6 = v5;
    idx = (v6 & 31) * 56 + g_103a3b80[v6 >> 5];
    v3 = 1;
    if (!idx[2])
    {
        v1 = 10;
        sub_1035a599(v8, v9, 10);
        v4 = 0;
        if (!idx[2])
        {
            v1 = 4000;
            v0 = &idx[3];
            if (!(unsigned int)sub_1035ca63())
            {
                v3 = 0;
                idx[2] = idx[2] + 1;
            }
            else
            {
                idx[2] = idx[2] + 1;
            }
        }
        v4 = 4294967294;
        sub_1036521f();
    }
    if (v3)
    {
        v1 = g_103a3b80[v6 >> 5] + (v6 & 31) * 56 + 12;
        g_1038b1b8(g_103a3b80[v6 >> 5] + (v6 & 31) * 56 + 12);
    }
    sub_1035b111(v1, &g_103a14e8, 12, v2);
    return;
}
```

## `sub_1036521a` `0x1036521a`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1036521a(void)
{
    sub_1036521f();
    return;
}
```

## `sub_1036521f` `0x1036521f`

_9 bytes. (leaf/helper — see body)_

```c
int sub_1036521f(void)
{
    return sub_1035a4c1(10);
}
```

## `sub_10365228` `0x10365228`

_34 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b1bc;
extern unsigned int g_103a3b80[4];

int sub_10365228(int a0)
{
    return g_1038b1bc(g_103a3b80[a0 >> 5] + (a0 & 31) * 56 + 12);
}
```

## `sub_1036524a` `0x1036524a`

_391 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    char field_4;
    char field_5;
    char padding_6[2];
    unsigned int field_8;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b1b8;
extern struct_1 *g_1038b1bc;
extern unsigned int g_103a1508;
extern unsigned int g_103a3b70;
extern void g_103a3b80;

void sub_1036524a(unsigned int a0)
{
    int idx;  // edi
    unsigned int v10;  // ecx
    unsigned int v11;  // edx
    void* node;  // esi
    void* v13;  // ebx
    struct_0 *iter;  // eax
    unsigned int *v15;  // ecx
    unsigned int v16;  // edi
    void* v0;  // [bp-0x18], Other Possible Types: unsigned int
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    int v4;  // [bp+0xfffdc]
    unsigned int v5;  // [bp+0xfffe0]
    void* v6;  // [bp+0xfffe4], Other Possible Types: struct_0 *
    unsigned int v7;  // [bp+0xfffe8]
    unsigned int v8;  // [bp+0x100000]

    sub_1035b0cc(&g_103a1508, 24);
    v7 = 4294967295;
    idx = 0;
    v5 = 0;
    v3 = 11;
    if (!sub_1035a4d6(v10, v11))
    {
        sub_1035b111(v2, 11, &g_103a1508, 24);
        return;
    }
    sub_1035a599(11, v11, 11);
    v8 = 0;
    while (true)
    {
        v4 = idx;
        if (idx >= 64)
            break;
        node = *((int *)&(&g_103a3b80)[4 * idx]);
        if (node)
        {
            while (true)
            {
                v6 = node;
                if (node >= *((int *)&(&g_103a3b80)[4 * idx]) + 0x700)
                    break;
                if (!((char)node[4] & 1))
                {
                    if (!(int)node[8])
                    {
                        sub_1035a599(v10, v11, 10);
                        v8 = 1;
                        if (!(int)node[8])
                        {
                            v1 = 4000;
                            v0 = node + 12;
                            if (!(unsigned int)sub_1035ca63())
                                v5 = 1;
                            else
                                *((unsigned int *)&node[8]) = (int)node[8] + 1;
                        }
                        v8 = 0;
                        sub_1036531d();
                    }
                    if (!v5)
                    {
                        v13 = node + 12;
                        g_1038b1b8(v13);
                        if (((char)node[4] & 1))
                        {
                            g_1038b1bc(v13);
                        }
                        else if (!v5)
                        {
                            *((char *)&node[4]) = 1;
                            *((unsigned int *)node) = 4294967295;
                            v0 = 56;
                            v7 = (node - *((int *)&(&g_103a3b80)[4 * idx])) / 56 + idx * 32;
                            break;
                        }
                    }
                }
                node += 56;
            }
            if (v7 != 4294967295)
                break;
            idx += 1;
        }
        else
        {
            iter = sub_103574c2(32, 56);
            v6 = iter;
            if (iter)
            {
                v15 = &(&g_103a3b80)[4 * idx];
                *(v15) = iter;
                for (g_103a3b70 = g_103a3b70 + 32; iter < *(v15) + 0x700; v6 = &iter[4].field_8)
                {
                    iter->field_4 = 0;
                    iter->field_0 = 4294967295;
                    iter->field_5 = 10;
                    iter->field_8 = 0;
                }
                v16 = idx * 32;
                v7 = v16;
                *((char *)(*((int *)&(&g_103a3b80)[4 * (v16 >> 5)]) + (v16 & 31) * 56 + 4)) = 1;
                if (!(unsigned int)sub_10365188(v16))
                {
                    v7 = 4294967295;
                    break;
                }
            }
        }
    }
    v8 = 4294967294;
    sub_103653e0();
    sub_1035b111(v2, 11, &g_103a1508, 24);
    return;
}
```

## `sub_10365317` `0x10365317`

_6 bytes. (leaf/helper — see body)_

```c
void sub_10365317(void)
{
    sub_1036531d();
    return;
}
```

## `sub_1036531d` `0x1036531d`

_9 bytes. (leaf/helper — see body)_

```c
int sub_1036531d(void)
{
    return sub_1035a4c1(10);
}
```

## `sub_103653e0` `0x103653e0`

_9 bytes. (leaf/helper — see body)_

```c
int sub_103653e0(void)
{
    return sub_1035a4c1(11);
}
```

## `sub_103653e9` `0x103653e9`

_194 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b040;
extern struct_0 *g_1038b07c;
extern struct_0 *g_1038b184;
extern struct_0 *g_1038b188;
extern struct_0 *g_1038b18c;
extern unsigned int g_1038e180;
extern unsigned int g_1038f170;
extern unsigned int g_1038f540;

short sub_103653e9(char a0)
{
    unsigned int v6;  // esi
    unsigned int v7;  // eax
    unsigned int v8;  // eax
    unsigned int v0;  // [bp-0x18]
    char v1;  // [bp-0x14]
    char v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0x8]
    char v4;  // [bp-0x4]

    v3 = g_1038e180 ^ &v4;
    v0 = v6;
    if (g_1038f170)
    {
        if (g_1038f540 == 4294967294)
            sub_103677fd();
        if (g_1038f540 == 4294967295)
            goto LABEL_1036541c;
        if (g_1038b184(g_1038f540, &/* unsupported instruction */, 1, &v1, 0))
        {
            g_1038f170 = 1;
LABEL_1036548e:
        }
        else if (g_1038f170 == 2 && g_1038b07c() == 120)
        {
            g_1038f170 = 0;
            goto LABEL_10365452;
        }
    }
    else
    {
LABEL_10365452:
        v7 = g_1038b188(0, &/* unsupported instruction */, 1, &v2, 5, 0, 0);
        v8 = g_1038b040(v7);
        if (g_1038f540 != 4294967295 && g_1038b18c(g_1038f540, &v2, v8, &v1, 0))
            goto LABEL_1036548e;
LABEL_1036541c:
    }
    return sub_10351225();
}
```

## `sub_103654ab` `0x103654ab`

_275 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
    char field_1;
} struct_0;

typedef struct struct_2 {
    char padding_0[112];
    unsigned int field_70;
} struct_2;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b104;

int sub_103654ab(unsigned short *a0, struct_0 *a1, int a2, unsigned int *a3)
{
    unsigned int v5;  // ebx
    unsigned int v6;  // esi
    unsigned int v7[6];  // eax
    int v8;  // ecx
    unsigned int v9[6];  // eax
    int v10;  // eax
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    struct_0 v2;  // [bp-0x14]
    struct_2 *idx;  // [bp-0xc]
    char v4;  // [bp-0x8]

    v1 = v5;
    v0 = v6;
    if (!a1 || !a2)
        return 0;
    if (a1->field_0)
    {
        sub_103536a7(&v2, a3);
        if (!*((int *)(v2 + 20)))
        {
            if (a0)
                *(a0) = a1->field_0;
LABEL_103654f6:
            if (!v4)
                return 1;
            idx->field_70 = idx->field_70 & 4294967293;
            return 1;
        }
        else
        {
            if (sub_1035de48(a1->field_0, &v2))
            {
                v7 = (unsigned int [6])v2;
                v8 = v7[7 + 1];
                v9 = v7;
                if (v8 > 1 && !((v9 = v7, a2 < v8 || (v9 = (unsigned int [6])v2, v9 = v9, !g_1038b104(v7[1], 9, a1, v8, a0, (unsigned int)(char)(a0))))) || a2 >= v9[7 + 1] && a1->field_1)
                {
                    v10 = v9[7 + 1];
                    if (!v4)
                        return v10;
                    idx->field_70 = idx->field_70 & 4294967293;
                    return v10;
                }
            }
            else
            {
                if (g_1038b104(*((int *)(v2 + 4)), 9, a1, 1, a0, a0))
                    goto LABEL_103654f6;
            }
            *((unsigned int *)sub_103575e0()) = 42;
            if (!v4)
                return -1;
            idx->field_70 = idx->field_70 & 4294967293;
            return -1;
        }
    }
    else if (a0)
    {
        *(a0) = 0;
    }
    return 0;
}
```

## `sub_103655be` `0x103655be`

_23 bytes. (leaf/helper — see body)_

```c
int sub_103655be(unsigned short *a0, char *a1, int a2)
{
    return sub_103654ab(a0, a1, a2, NULL);
}
```

## `sub_103655d5` `0x103655d5`

_555 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

typedef struct struct_1 {
    char padding_0[112];
    unsigned int field_70;
} struct_1;

typedef struct struct_2 {
    char padding_0[172];
    int field_ac;
    char padding_b0[24];
    unsigned int field_c8;
} struct_2;

unsigned int sub_103655d5(unsigned int *a0, char *a1, struct_0 **a2, unsigned int a3, unsigned int a4)
{
    char v9[3];  // esi
    unsigned int v10;  // ebx
    unsigned int v19;  // ecx
    char v20[3];  // edi
    unsigned int v21;  // eax
    char v11;  // bl
    char iter[3];  // edi
    struct_2 *v13;  // ecx
    struct_2 *v14;  // ecx
    unsigned int v15;  // eax
    char v16[3];  // edi
    unsigned int v17;  // eax
    unsigned int v18;  // ecx
    unsigned int v0;  // [bp-0x34]
    unsigned int v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x2c]
    unsigned int v3;  // [bp-0x28]
    unsigned int v4;  // [bp-0x24]
    struct_0 v5;  // [bp-0x18]
    struct_1 *idx;  // [bp-0x10]
    char v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]

    sub_103536a7(&v5, a0);
    v9 = a1;
    if (a2)
        *(a2) = v9;
    if (v9 && (!a3 || a3 >= 2 && a3 <= 36))
    {
        v4 = v10;
        v11 = v9[0];
        v8 = 0;
        iter = &v9[1];
        v13 = (struct_2 *)v5;
        while (true)
        {
            v14 = v13;
            if (v14->field_ac > 1)
            {
                v15 = sub_1035b7ea(v11, 8, &v5);
                v14 = (struct_2 *)v5;
            }
            else
            {
                v15 = *((char *)(v14->field_c8 + v11 * 2)) & 8;
            }
            if (!v15)
                break;
            v11 = iter[0];
            iter = &iter[1];
            v13 = v14;
        }
        if (v11 == 45)
        {
            a4 |= 2;
        }
        else if (!(v11 == 43))
        {
            goto LABEL_1036568f;
        }
        v11 = iter[0];
        iter = &iter[1];
LABEL_1036568f:
        if (a3 >= NULL && a3 != 1 && a3 <= 36)
        {
            if (!a3)
            {
                if (v11 != 48)
                {
                    a3 = 10;
                }
                else if (iter[0] != 120 && iter[0] != 88)
                {
                    a3 = 8;
                }
                else
                {
                    a3 = 16;
LABEL_103656e4:
                    if (iter[0] == 120 || iter[0] == 88)
                    {
                        v16 = &iter[1];
                        v11 = v16[0];
                        iter = &v16[1];
                    }
                }
            }
            else
            {
                if (a3 == 16 && v11 == 48)
                    goto LABEL_103656e4;
            }
            v17 = 4294967295 / a3;
            while (true)
            {
                if (((char)*((short *)(v14->field_c8 + v11 * 2)) & 4))
                {
                    v18 = v11 - 48;
                }
                else
                {
                    if (!(*((short *)(v14->field_c8 + v11 * 2)) & 259))
                        break;
                    v19 = v11;
                    if (v11 - 97 <= 25)
                        v19 -= 32;
                    v18 = v19 - 55;
                }
                if (v18 >= a3)
                    break;
                a4 |= 8;
                if (v8 >= v17 && (v8 != v17 || v18 > (unsigned int)(4294967295 % a3)))
                {
                    a4 |= 4;
                    if (!a2)
                        break;
                }
                else
                {
                    v8 = a3 * v8 + v18;
                }
                v11 = iter[0];
                iter = &iter[1];
            }
            v20 = &iter[1];
            if (!((char)a4 & 8))
            {
                if (a2)
                    v20 = a1;
                v8 = 0;
            }
            else if (((char)a4 & 4) || !((char)a4 & 1) && (((char)a4 & 2) && v8 > 0x80000000 || !((char)a4 & 2) && v8 > 2147483647))
            {
                *((unsigned int *)sub_103575e0()) = 0x22;
                v8 = (!((char)a4 & 1) ? -(-(0 < ((char)a4 & 2))) + 2147483647 : 4294967295);
            }
            if (a2)
                *(a2) = v20;
            if (((char)a4 & 2))
                v8 = -(v8);
            if (v7)
                idx->field_70 = idx->field_70 & 4294967293;
            v21 = v8;
        }
        else
        {
            if (a2)
                *(a2) = v9;
            if (v7)
                idx->field_70 = idx->field_70 & 4294967293;
            v21 = 0;
        }
        return v21;
    }
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    *((unsigned int *)sub_103575e0()) = 22;
    sub_103535f2();
    if (v7)
        idx->field_70 = idx->field_70 & 4294967293;
    return 0;
}
```

## `sub_10365800` `0x10365800`

_41 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

extern unsigned int g_1038e750;
extern unsigned int g_103a3058;

unsigned int sub_10365800(char *a0, struct_0 **a1, unsigned int a2)
{
    unsigned int v0;  // [bp-0x18]

    v0 = (!g_103a3058 ? &g_1038e750 : 0);
    return sub_103655d5((!g_103a3058 ? &g_1038e750 : 0), a0, a1, a2, 0);
}
```

## `sub_10365829` `0x10365829`

_2246 bytes. refs "1#SNAN", "1#IND", "1#INF"_

```c
typedef struct struct_0 {
    unsigned short field_0;
    char field_2;
    char field_3;
    char field_4;
    char field_5;
} struct_0;

extern unsigned int g_1038e180;
extern unsigned int g_1038f220;
extern unsigned int g_1038f380;

int sub_10365829(unsigned int a0, unsigned int a1, unsigned short a2, int a3, char a4, struct_0 *idx)
{
    unsigned int v37;  // ebx
    unsigned int v38;  // esi
    unsigned short v47;  // di
    unsigned short v48;  // cx
    unsigned int iter;  // eax
    void* node;  // edi
    unsigned int v51;  // edx
    unsigned int v52;  // esi
    unsigned int iter1;  // eax
    unsigned int v54;  // 4108
    unsigned int v55;  // 4201
    unsigned int v56;  // 4105
    unsigned int v39;  // edi
    unsigned int v57;  // 4127
    unsigned short v58;  // cx
    unsigned short v59;  // si
    unsigned short v60;  // dx
    unsigned short v61;  // dx
    unsigned short v62;  // si
    unsigned short v63;  // cx
    unsigned int iter2;  // edi
    void* v65;  // eax
    unsigned int v66;  // edx
    unsigned short v40;  // dx
    unsigned int v67;  // ebx
    unsigned int v68;  // edi
    unsigned int v69;  // eax
    unsigned int v70;  // eax
    unsigned int j;  // eax
    unsigned int v72;  // 4127
    unsigned int v73;  // 4119
    struct_0 *idx1;  // edx
    unsigned short v75;  // cx
    int v76;  // esi
    int i;  // ebx
    char v78;  // sil
    unsigned int l;  // esi
    struct_0 *v80;  // ebx
    unsigned int v81;  // eax
    unsigned int v82;  // ecx
    unsigned int v83;  // ecx
    unsigned int v84;  // esi
    unsigned int v85;  // edi
    unsigned int v86;  // esi
    unsigned int v42;  // ecx
    unsigned int v87;  // eax
    unsigned int v88;  // edx
    struct_0 *v89;  // ebx
    struct_0 *n;  // ebx
    struct_0 *index;  // eax
    void* idx2;  // ecx
    void* v44;  // esi
    void* v45;  // esi
    unsigned short v46;  // dx
    unsigned int v0;  // [bp-0x98]
    unsigned int v1;  // [bp-0x94]
    unsigned int v2;  // [bp-0x90]
    unsigned int v3;  // [bp-0x8c]
    char *k;  // [bp-0x88], Other Possible Types: unsigned int
    unsigned int v5;  // [bp-0x84]
    unsigned int v6;  // [bp-0x80]
    unsigned int v7;  // [bp-0x7c]
    unsigned int v8;  // [bp-0x78]
    unsigned int v9;  // [bp-0x74]
    unsigned int v10;  // [bp-0x70]
    unsigned int v11;  // [bp-0x6c]
    void* v12;  // [bp-0x68]
    void* v13;  // [bp-0x60], Other Possible Types: unsigned int
    char v14[2];  // [bp-0x5c], Other Possible Types: unsigned int
    void* v15;  // [bp-0x58], Other Possible Types: unsigned int
    int i1;  // [bp-0x54]
    int m;  // [bp-0x50], Other Possible Types: unsigned int
    char v18[2];  // [bp-0x4c], Other Possible Types: unsigned int
    void* i0;  // [bp-0x48], Other Possible Types: unsigned int
    struct_0 *v20;  // [bp-0x44], Other Possible Types: int
    int v21;  // [bp-0x40], Other Possible Types: unsigned int
    unsigned int v22;  // [bp-0x3c]
    unsigned int v23;  // [bp-0x38]
    unsigned int v24;  // [bp-0x34]
    int v25;  // [bp-0x30]
    int v26;  // [bp-0x24], Other Possible Types: unsigned short, unsigned int
    unsigned int v27;  // [bp-0x22]
    unsigned int v28;  // [bp-0x20]
    unsigned int v29;  // [bp-0x1e]
    unsigned int v30;  // [bp-0x1c]
    unsigned short v31;  // [bp-0x1a]
    char v32;  // [bp-0x19]
    int v33;  // [bp-0x14], Other Possible Types: unsigned int
    unsigned int v34;  // [bp-0xc]
    unsigned int v35;  // [bp-0x8]
    char v36;  // [bp-0x4]

    v35 = g_1038e180 ^ &v36;
    v7 = v37;
    v6 = v38;
    v5 = v39;
    v33 = a0;
    *((unsigned short *)&v34) = a2;
    v40 = (unsigned short)v34 & 32767;
    *((char *)&v24) = 0xcc;
    *((char *)&v24 + 1) = 0xcc;
    *((char *)&v24 + 2) = 0xcc;
    *((char *)&v24 + 3) = 0xcc;
    *((char *)&v25) = 0xcc;
    *((char *)&(&v25)[1]) = 0xcc;
    *((char *)&(&v25)[2]) = 0xcc;
    *((char *)&(&v25)[3]) = 0xcc;
    *((char *)&(&v25)[4]) = 0xcc;
    *((char *)&(&v25)[5]) = 0xcc;
    *((char *)&(&v25)[6]) = 251;
    *((char *)&(&v25)[7]) = 63;
    v8 = 1;
    v10 = v34 & 0x8000;
    if ((unsigned short)v10)
        idx->field_2 = 45;
    else
        idx->field_2 = 32;
    if (!v40 && !a1 && !v33)
    {
        idx->field_0 = 0;
        idx->field_2 = ((char)(((unsigned short)v10 != 0x8000) + 1) & 13) + 32;
        idx->field_3 = 1;
        idx->field_4 = 48;
        idx->field_5 = 0;
        goto LABEL_103658d8;
    }
    if (v40 == 32767)
    {
        idx->field_0 = 1;
        if ((a1 != 0x80000000 || v33) && !(a1 & 0x40000000))
        {
            k = "1#SNAN";
            goto LABEL_1036595d;
        }
        if ((unsigned short)v10 && a1 == 0xc0000000)
        {
            if (v33)
                goto LABEL_10365958;
            k = "1#IND";
            goto LABEL_10365931;
        }
        else if (a1 == 0x80000000 && !v33)
        {
            k = "1#INF";
LABEL_10365931:
            if (sub_10359f58(&idx->field_4, 22, k))
            {
                k = 0;
                v3 = 0;
                v2 = 0;
                v1 = 0;
                v0 = 0;
                sub_103534f6();
            }
            idx->field_3 = 5;
        }
        else
        {
LABEL_10365958:
            k = "1#QNAN";
LABEL_1036595d:
            if (sub_10359f58(&idx->field_4, 22, k))
            {
                k = 0;
                v3 = 0;
                v2 = 0;
                v1 = 0;
                v0 = 0;
                sub_103534f6();
            }
            idx->field_3 = 6;
        }
    }
    else
    {
        m = (unsigned short)(((v40 >> 8) + (a1 >> 24) * 2) * 77 + v40 * 19728 - 323162868 >> 16);
        i = -((short)m);
        *((unsigned short *)&(&v26)[10]) = v40;
        *((unsigned int *)&(&v26)[6]) = a1;
        *((unsigned int *)&(&v26)[2]) = v33;
        *((unsigned short *)&v26) = 0;
        v11 = &g_1038f220;
        if (i)
        {
            if (i < 0)
            {
                i = -(i);
                v11 = &g_1038f380;
            }
            if (i)
            {
                do
                {
                    v11 += 84;
                    v42 = i & 7;
                    i >>= 3;
                    if (!v42)
                        continue;
                    idx2 = v42 * 12 + v11;
                    v12 = idx2;
                    if (*((short *)idx2) >= 0x8000)
                    {
                        v44 = idx2;
                        *((int *)&v21) = *((int *)v44);
                        v45 = v44 + 4;
                        *((int *)&(&v21)[4]) = *((int *)v45);
                        *((int *)&(&v21)[8]) = (int)v45[4];
                        *((unsigned int *)&(&v21)[2]) = *((unsigned int *)(&v21 + 2)) - 1;
                        v12 = &v21;
                        idx2 = &v21;
                    }
                    v46 = (unsigned short)*((unsigned int *)(&v26 + 10)) & 32767;
                    v47 = (short)idx2[10] & 32767;
                    v18 = 0;
                    v33 = (int)_INSERT(v33 CONCAT 0, 0, 0);
                    *((unsigned int *)&(&v33)[4]) = 0;
                    *((unsigned int *)&(&v33)[8]) = 0;
                    v48 = ((short)idx2[10] ^ (unsigned short)*((unsigned int *)(&v26 + 10))) & 0x8000;
                    iter = (unsigned short)(v47 + v46);
                    if (v46 < 32767 && v47 < 32767 && (unsigned short)iter <= 49149)
                    {
                        if ((unsigned short)iter <= 16319)
                        {
                            *((unsigned int *)&(&v26)[8]) = 0;
                            *((unsigned int *)&(&v26)[4]) = 0;
                            *((unsigned int *)&v26) = 0;
                            continue;
                        }
                        if (!v46 && (iter += 1, !(*((unsigned int *)((void*)&v26 + 8)) & 2147483647) && !*((unsigned int *)((void*)&v26 + 4)) && !*((unsigned int *)(void*)&v26)))
                        {
                            v31 = 0;
                            continue;
                        }
                        if (!v47 && (iter += 1, !((int)v12[8] & 2147483647) && !(int)v12[4] && !*((int *)v12)))
                        {
                            *((unsigned int *)&(&v26)[8]) = 0;
                            *((unsigned int *)&(&v26)[4]) = 0;
                            *((unsigned int *)&v26) = 0;
                            continue;
                        }
                        node = &v33 - 4;
                        v13 = 0;
                        i0 = &v33 - 4;
                        v20 = 5;
                        do
                        {
                            i1 = v20;
                            if (v20 > 0)
                            {
                                v14 = &v26 + v13 * 2;
                                v15 = v12 + 8;
                                do
                                {
                                    v51 = *((short *)v15) * (unsigned int)*(v14);
                                    v9 = 0;
                                    v52 = (int)node[4] + v51;
                                    if (v52 < (int)node[4] || v52 < v51)
                                        v9 = 1;
                                    node = i0;
                                    *((unsigned int *)&node[4]) = v52;
                                    if (v9)
                                        *((unsigned short *)node) = *((short *)node) + 1;
                                    v14 += 1;
                                    v15 -= 2;
                                    i1 -= 1;
                                } while (i1 > 0);
                            }
                        } while ((node += 2, v13 += 1, v20 = (int)(v20 - 1), i0 = node, v20 > 0));
                        iter1 = iter + 49154;
                        v54 = _ccall(14, 14, (unsigned int)(unsigned short)iter1, 0, 0);
                        if (!((char)v54))
                        {
                            do
                            {
                                if ((*((unsigned int *)(&v33 + 8)) & 0x80000000))
                                    break;
                            } while ((*((unsigned int *)&v33) = *((unsigned int *)(void*)&v33) * 2, iter1 += 0xffff, *((unsigned int *)&(&v33)[4]) = *((unsigned int *)((void*)&v33 + 4)) * 2 | *((unsigned int *)(void*)&v33) >> 31, *((unsigned int *)&(&v33)[8]) = *((unsigned int *)((void*)&v33 + 8)) * 2 | *((unsigned int *)((void*)&v33 + 4)) >> 31, v55 = (unsigned int)_ccall(14, 14, (unsigned int)(unsigned short)iter1, 0, 0), !((char)v55)));
                            v56 = _ccall(14, 14, (unsigned int)(unsigned short)iter1, 0, 0);
                            if (!((char)v56))
                                goto LABEL_10365bf4;
                        }
                        iter1 += 0xffff;
                        if ((unsigned short)iter1 < 0)
                        {
                            i0 = (unsigned short)-(iter1);
                            iter1 += i0;
                            do
                            {
                                if ((*((char *)&v33) & 1))
                                    v18 += 1;
                                *((unsigned int *)&(&v33)[8]) = *((unsigned int *)(&v33 + 8)) >> 1;
                                i0 -= 1;
                                *((unsigned int *)&(&v33)[4]) = *((unsigned int *)(&v33 + 4)) >> 1 | *((unsigned int *)(&v33 + 8)) * 0x80000000;
                                *((unsigned int *)&v33) = *((unsigned int *)&v33) >> 1 | *((unsigned int *)(&v33 + 4)) * 0x80000000;
                            } while (i0 != 1);
                            if (v18)
                                *((unsigned short *)&v33) = *((unsigned short *)&v33) | 1;
                        }
LABEL_10365bf4:
                        if (*((unsigned int *)&v33) > 0x8000 || (*((unsigned int *)&v33) & 0x1ffff) == 0x18000)
                        {
                            if (*((unsigned int *)(&v33 + 2)) == 4294967295)
                            {
                                *((unsigned int *)&(&v33)[2]) = 0;
                                if (*((unsigned int *)(&v33 + 6)) == 4294967295)
                                {
                                    *((unsigned int *)&(&v33)[6]) = 0;
                                    if (*((unsigned short *)(&v33 + 10)) == 65535)
                                    {
                                        *((unsigned short *)&(&v33)[10]) = 0x8000;
                                        iter1 += 1;
                                    }
                                    else
                                    {
                                        *((unsigned short *)&(&v33)[10]) = *((unsigned short *)(&v33 + 10)) + 1;
                                    }
                                }
                                else
                                {
                                    *((unsigned int *)&(&v33)[6]) = *((unsigned int *)(&v33 + 6)) + 1;
                                }
                            }
                            else
                            {
                                *((unsigned int *)&(&v33)[2]) = *((unsigned int *)(&v33 + 2)) + 1;
                            }
                        }
                        if ((unsigned short)iter1 < 32767)
                        {
                            v26 = *((unsigned short *)(&v33 + 2));
                            v27 = *((unsigned int *)(&v33 + 4));
                            v29 = *((unsigned int *)(&v33 + 8));
                            v31 = iter1 | v48;
                            continue;
                        }
                        goto LABEL_10365c62;
                    }
                    else
                    {
LABEL_10365c62:
                        v57 = _ccall(5, 0, (unsigned int)v48, 0);
                        v28 = 0;
                        v26 = 0;
                        v30 = (-(v57 & 1) & 0x80000000) + 0x7fff8000;
                    }
                } while (i);
            }
        }
        v58 = *((unsigned int *)(&v26 + 8)) >> 16;
        if (v58 >= 0x3fff)
        {
            v59 = *((unsigned int *)(&v25 + 6));
            m += 1;
            v60 = v58;
            v61 = v60 & 32767;
            v62 = v59 & 32767;
            v63 = (v59 ^ v60) & 0x8000;
            v14 = 0;
            v33 = (int)_INSERT(v33 CONCAT 0, 0, 0);
            *((unsigned int *)&(&v33)[4]) = 0;
            *((unsigned int *)&(&v33)[8]) = 0;
            iter2 = (unsigned short)(v62 + v61);
            if (!(v61 < 32767 && v62 < 32767 && (unsigned short)iter2 <= 49149))
            {
                v73 = _ccall(5, 0, (unsigned int)v63, 0);
                *((unsigned int *)&(&v26)[8]) = (-(v73 & 1) & 0x80000000) + 0x7fff8000;
            }
            else if ((unsigned short)iter2 <= 16319)
            {
LABEL_10365ceb:
                *((unsigned int *)&(&v26)[8]) = 0;
            }
            else if (!v61 && (iter2 += 1, !(*((unsigned int *)((void*)&v26 + 8)) & 2147483647) && !*((unsigned int *)((void*)&v26 + 4)) && !*((unsigned int *)(void*)&v26)))
            {
                *((unsigned short *)&(&v26)[10]) = 0;
                goto LABEL_10365ee6;
            }
            else
            {
                if (!v62 && !((iter2 += 1, (*((unsigned int *)((void*)&v25 + 4)) & 2147483647) || *((unsigned int *)(void*)&v25) || v24)))
                    goto LABEL_10365ceb;
                v15 = 0;
                v65 = &v33 - 4;
                v20 = 5;
                do
                {
                    i1 = v20;
                    if (v20 > 0)
                    {
                        v13 = &v25 - 4;
                        v18 = &v26 + v15 * 2;
                        do
                        {
                            i0 = 0;
                            v66 = (unsigned int)*(v18) * *((short *)v13);
                            v67 = (int)v65[4] + v66;
                            if (v67 < (int)v65[4] || v67 < v66)
                                i0 = 1;
                            *((unsigned int *)&v65[4]) = v67;
                            if (i0)
                                *((unsigned short *)v65) = *((short *)v65) + 1;
                            v18 += 1;
                            v13 -= 2;
                            i1 -= 1;
                        } while (i1 > 0);
                    }
                } while ((v65 += 2, v15 += 1, v20 = (int)(v20 - 1), v20 > 0));
                v68 = iter2 + 49154;
                v69 = 0;
                if ((unsigned short)v68 > 0)
                {
                    do
                    {
                    } while (!(*((unsigned int *)(&v33 + 8)) & 0x80000000) && (*((unsigned int *)&v33) = *((unsigned int *)(void*)&v33) * 2, v68 += 0xffff, *((unsigned int *)&(&v33)[4]) = *((unsigned int *)((void*)&v33 + 4)) * 2 | *((unsigned int *)(void*)&v33) >> 31, *((unsigned int *)&(&v33)[8]) = *((unsigned int *)((void*)&v33 + 8)) * 2 | *((unsigned int *)((void*)&v33 + 4)) >> 31, (unsigned short)v68 > 0));
                    if ((unsigned short)v68 > 0)
                        goto LABEL_10365e41;
                }
                v68 += 0xffff;
                if ((unsigned short)v68 < 0)
                {
                    v70 = (unsigned short)-(v68);
                    v68 += v70;
                    do
                    {
                        j = v70;
                        if ((*((char *)&v33) & 1))
                            v14 += 1;
                        *((unsigned int *)&(&v33)[8]) = *((unsigned int *)(&v33 + 8)) >> 1;
                        v69 = j - 1;
                        *((unsigned int *)&(&v33)[4]) = *((unsigned int *)(&v33 + 4)) >> 1 | *((unsigned int *)(&v33 + 8)) * 0x80000000;
                        *((unsigned int *)&v33) = *((unsigned int *)&v33) >> 1 | *((unsigned int *)(&v33 + 4)) * 0x80000000;
                        v70 = v69;
                    } while (j != 1);
                    if (v14 != v69)
                        *((unsigned short *)&v33) = *((unsigned short *)&v33) | 1;
                }
LABEL_10365e41:
                if (*((unsigned int *)&v33) > 0x8000 || (*((unsigned int *)&v33) & 0x1ffff) == 0x18000)
                {
                    if (*((unsigned int *)(&v33 + 2)) == 4294967295)
                    {
                        *((unsigned int *)&(&v33)[2]) = v69;
                        if (*((unsigned int *)(&v33 + 6)) == 4294967295)
                        {
                            *((unsigned int *)&(&v33)[6]) = v69;
                            if (*((unsigned short *)(&v33 + 10)) == 65535)
                            {
                                *((unsigned short *)&(&v33)[10]) = 0x8000;
                                v68 += 1;
                            }
                            else
                            {
                                *((unsigned short *)&(&v33)[10]) = *((unsigned short *)(&v33 + 10)) + 1;
                            }
                        }
                        else
                        {
                            *((unsigned int *)&(&v33)[6]) = *((unsigned int *)(&v33 + 6)) + 1;
                        }
                    }
                    else
                    {
                        *((unsigned int *)&(&v33)[2]) = *((unsigned int *)(&v33 + 2)) + 1;
                    }
                }
                if ((unsigned short)v68 >= 32767)
                {
                    *((unsigned int *)&(&v26)[4]) = v69;
                    *((unsigned int *)&v26) = v69;
                    v72 = _ccall(5, 0, (unsigned int)v63, 0);
                    *((unsigned int *)&(&v26)[8]) = (-(v72 & 1) & 0x80000000) + 0x7fff8000;
                }
                else
                {
                    *((unsigned short *)&v26) = *((unsigned short *)(&v33 + 2));
                    *((unsigned int *)&(&v26)[2]) = *((unsigned int *)(&v33 + 4));
                    *((unsigned int *)&(&v26)[6]) = *((unsigned int *)(&v33 + 8));
                    *((unsigned short *)&(&v26)[10]) = v68 | v63;
                }
                goto LABEL_10365ee6;
            }
            *((unsigned int *)&(&v26)[4]) = 0;
            *((unsigned int *)&v26) = 0;
        }
LABEL_10365ee6:
        idx1 = idx;
        v75 = m;
        idx1->field_0 = v75;
        if ((a4 & 1) && (a3 += (int)(short)v75, a3 <= 0))
        {
            idx1->field_0 = 0;
            idx1->field_3 = 1;
            idx1->field_2 = ((char)(((unsigned short)v10 != 0x8000) + 1) & 13) + 32;
            idx1->field_4 = 48;
            idx1->field_5 = 0;
            goto LABEL_103658d8;
        }
        else
        {
            k = 21;
            if (a3 > 21)
                a3 = 21;
            k = 8;
            v76 = (*((unsigned int *)(&v26 + 8)) >> 16) - 0x3ffe;
            *((unsigned short *)&(&v26)[10]) = 0;
            do
            {
                *((unsigned int *)&v26) = *((unsigned int *)&v26) * 2;
                *((unsigned int *)&(&v26)[4]) = *((unsigned int *)(&v26 + 4)) * 2 | *((unsigned int *)&v26) >> 31;
                *((unsigned int *)&(&v26)[8]) = *((unsigned int *)(&v26 + 8)) * 2 | *((unsigned int *)(&v26 + 4)) >> 31;
                k -= 1;
            } while (k != 1);
            if (v76 < 0)
            {
                v78 = -(v76);
                l = v78;
                if (v78 > 0)
                {
                    do
                    {
                        *((unsigned int *)&(&v26)[8]) = *((unsigned int *)(&v26 + 8)) >> 1;
                        l -= 1;
                        *((unsigned int *)&(&v26)[4]) = *((unsigned int *)(&v26 + 4)) >> 1 | *((unsigned int *)(&v26 + 8)) * 0x80000000;
                        *((unsigned int *)&v26) = *((unsigned int *)&v26) >> 1 | *((unsigned int *)(&v26 + 4)) * 0x80000000;
                    } while (l > 0);
                }
            }
            v80 = &idx1->field_4;
            v20 = v80;
            m = a3 + 1;
            if (m > 0)
            {
                do
                {
                    v81 = *((unsigned int *)(&v26 + 4));
                    v21 = *((unsigned int *)&v26);
                    v22 = *((unsigned int *)(&v26 + 4));
                    v23 = *((unsigned int *)(&v26 + 8));
                    v26 = *((unsigned int *)&v26) * 2;
                    v26 = (int)_INSERT(v26 CONCAT 0, 0, v26 * 2);
                    v82 = v81 * 2 | *((unsigned int *)&v26) >> 31;
                    v83 = (*((unsigned int *)(&v26 + 8)) * 2 | v81 >> 31) * 2 | v82 >> 31;
                    v84 = v82 * 2 | v26 >> 31;
                    v85 = v21 + *((unsigned int *)&v26);
                    if (v85 < *((unsigned int *)&v26) || (v86 = v84, v85 < v21))
                    {
                        v87 = v84 + 1;
                        v88 = 0;
                        if (v87 < v84 || v87 < 1)
                            v88 = 1;
                        v86 = v87;
                        if (v88)
                        {
                            v83 += 1;
                            v86 = v87;
                        }
                    }
                    i0 = v22 + v86;
                    if (i0 < v86)
                    {
                        v83 += 1;
                    }
                    else if (i0 < v22)
                    {
                        v83 += 1;
                    }
                    *((unsigned int *)&v26) = v85 * 2;
                    v30 = (v83 + v23) * 2 | i0 >> 31;
                    *((char *)&v80->field_0) = (char)(v30 >> 24) + 48;
                    v80 = (char *)&v80->field_0 + 1;
                    m -= 1;
                    *((unsigned int *)&(&v26)[4]) = i0 * 2 | v85 >> 31;
                    v32 = 0;
                } while (m > 0);
            }
            if ((char)v89->field_0 < 53)
            {
                for (n = (char *)&v89->field_0 + 1; n >= v20 && (char)n->field_0 == 48; n = (char *)&n->field_0 + 1);
                index = idx;
                if (n >= v20)
                    goto LABEL_10366094;
                index->field_0 = 0;
                index->field_3 = 1;
                index->field_2 = ((char)(((unsigned short)v10 != 0x8000) + 1) & 13) + 32;
                *((char *)&v20->field_0) = 48;
                index->field_5 = 0;
LABEL_103658d8:
            }
            else
            {
                for (v89 = (char *)&v80->field_0 + 1; n >= v20 && (char)n->field_0 == 57; n = (char *)&n->field_0 + 1)
                {
                    *((char *)&n->field_0) = 48;
                }
                index = idx;
                if (n < v20)
                {
                    n = (char *)&n->field_0 + 1;
                    index->field_0 = index->field_0 + 1;
                    *((char *)&n->field_0) = (char)n->field_0 + 1;
                }
                else
                {
                    *((char *)&n->field_0) = (char)n->field_0 + 1;
                }
LABEL_10366094:
                index->field_3 = *((char *)&n) - *((char *)&index) - 3;
                (&index->field_4)[*((char *)&n) - *((char *)&index) - 3] = 0;
            }
        }
    }
    return sub_10351225();
}
```

## `sub_103660ef` `0x103660ef`

_142 bytes. (leaf/helper — see body)_

```c
unsigned int sub_103660ef(char a0)
{
    unsigned int v2;  // eax
    unsigned int v3;  // ebx
    unsigned int v4;  // ecx
    unsigned int v5;  // esi
    unsigned int v0;  // [bp-0x4]

    v2 = 0;
    if (((char)v3 & 16))
        v2 = 1;
    if (((char)v3 & 8))
        v2 |= 4;
    if (((char)v3 & 4))
        v2 |= 8;
    if (((char)v3 & 2))
        v2 |= 16;
    if (((char)v3 & 1))
        v2 |= 32;
    if ((v3 & 0x80000))
        v2 |= 2;
    v4 = v3 & 0x300;
    v0 = v5;
    if (((unsigned short)v3 & 0x300))
    {
        if (v4 == 0x100)
        {
            v2 |= 0x400;
        }
        else if (v4 == 0x200)
        {
            v2 |= 0x800;
        }
        else if (v4 == 0x300)
        {
            v2 |= 0xc00;
        }
    }
    if (!(v3 & 0x30000))
    {
        v2 |= 0x300;
    }
    else if ((v3 & 0x30000) == 0x10000)
    {
        v2 |= 0x200;
    }
    if ((v3 & 0x40000))
        v2 |= 0x1000;
    return v2;
}
```

## `sub_1036617d` `0x1036617d`

_160 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1036617d(unsigned int a0, unsigned int a1)
{
    unsigned int v4;  // eax
    unsigned int v5;  // ebx
    unsigned int v6;  // esi
    unsigned int v7;  // edi
    unsigned int v8;  // ecx
    unsigned int v9;  // edx
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]
    unsigned int v2;  // [bp-0x4]

    v4 = 0;
    if (((char)a1 & 16))
        v4 = 128;
    v2 = v5;
    v1 = v6;
    v0 = v7;
    if (((char)a1 & 8))
        v4 |= 0x200;
    if (((char)a1 & 4))
        v4 |= 0x400;
    if (((char)a1 & 2))
        v4 |= 0x800;
    if (((char)a1 & 1))
        v4 |= 0x1000;
    if ((a1 & 0x80000))
        v4 |= 0x100;
    v8 = a1 & 0x300;
    if (((unsigned short)a1 & 0x300))
    {
        if (v8 == 0x100)
        {
            v4 |= 0x2000;
        }
        else if (v8 == 0x200)
        {
            v4 |= 0x4000;
        }
        else if (v8 == 0x300)
        {
            v4 |= 0x6000;
        }
    }
    v9 = a1 & 0x3000000;
    if (v9 == 0x1000000)
    {
        return v4 | 32832;
    }
    else if (v9 == 0x2000000)
    {
        return v4 | 64;
    }
    else if (v9 == 0x3000000)
    {
        return v4 | 0x8000;
    }
    else
    {
        return v4;
    }
}
```

## `sub_1036621d` `0x1036621d`

_771 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a4cc8;

unsigned int sub_1036621d(unsigned int a0, unsigned int a1)
{
    unsigned int v5;  // fpround
    unsigned int v6;  // 4140
    unsigned int v12;  // 4143
    unsigned short v13;  // bx
    unsigned int v14;  // eax
    unsigned int v15;  // eax
    unsigned int v16;  // sseround
    unsigned int v17;  // 4124
    unsigned int v18;  // eax
    unsigned short v7;  // bx
    unsigned int v19;  // ecx
    unsigned int v20;  // ecx
    unsigned int v21;  // eax
    unsigned int v22;  // eax
    unsigned int v23;  // edx
    unsigned int v24;  // 4123
    unsigned int v25;  // eax
    unsigned int v26;  // ecx
    unsigned int v27;  // ecx
    unsigned int v28;  // eax
    unsigned int v29;  // eax
    unsigned int v30;  // eax
    unsigned int v8;  // eax
    unsigned int v9;  // eax
    unsigned int v10;  // eax
    unsigned long v11;  // 4140
    char v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    unsigned int v3;  // [bp-0x4]
    unsigned int v4;  // [bp+0x0]

    v6 = _ccall(v5);
    *((unsigned short *)&v1) = v6;
    v7 = v1;
    v30 = 0;
    if (((char)v7 & 1))
        v30 = 16;
    if (((char)v7 & 4))
        v30 |= 8;
    if (((char)v7 & 8))
        v30 |= 4;
    if (((char)v7 & 16))
        v30 |= 2;
    if (((char)v7 & 32))
        v30 |= 1;
    if (((char)v7 & 2))
        v30 |= 0x80000;
    v8 = v7;
    v9 = v8 & 0xc00;
    if (((unsigned short)v8 & 0xc00))
    {
        if (v9 == 0x400)
        {
            v30 |= 0x100;
        }
        else if (v9 == 0x800)
        {
            v30 |= 0x200;
        }
        else if (v9 == 0xc00)
        {
            v30 |= 0x300;
        }
    }
    if (!((unsigned short)v8 & 0x300))
    {
        v30 |= 0x20000;
    }
    else if (((unsigned short)v8 & 0x300) == 0x200)
    {
        v30 |= 0x10000;
    }
    if ((v7 & 0x1000))
        v30 |= 0x40000;
    v10 = ~(a1) & v30 | a0 & a1;
    v3 = v10;
    if (v10 != v30)
    {
        v1 = sub_103660ef(v0) & 0xffff;
        v11 = _ccall((unsigned int)(unsigned short)v1);
        v12 = _ccall((unsigned int)v11);
        *((unsigned short *)&v1) = v12;
        v13 = v1;
        v10 = 0;
        if (((char)v13 & 1))
            v10 = 16;
        if (((char)v13 & 4))
            v10 |= 8;
        if (((char)v13 & 8))
            v10 |= 4;
        if (((char)v13 & 16))
            v10 |= 2;
        if (((char)v13 & 32))
            v10 |= 1;
        if (((char)v13 & 2))
            v10 |= 0x80000;
        v14 = v13;
        v15 = v14 & 0xc00;
        if (((unsigned short)v14 & 0xc00))
        {
            if (v15 == 0x400)
            {
                v10 |= 0x100;
            }
            else if (v15 == 0x800)
            {
                v10 |= 0x200;
            }
            else if (v15 == 0xc00)
            {
                v10 |= 0x300;
            }
        }
        if (!((unsigned short)v14 & 0x300))
        {
            v10 |= 0x20000;
        }
        else if (((unsigned short)v14 & 0x300) == 0x200)
        {
            v10 |= 0x10000;
        }
        if ((v13 & 0x1000))
            v10 |= 0x40000;
        v4 = v10;
    }
    if (!g_103a4cc8)
        return v10;
    v17 = _ccall(v16 & 3);
    v2 = v17;
    v18 = v2;
    v30 = 0;
    if ((char)v18 < 0)
        v30 = 16;
    if (((unsigned short)v18 & 0x200))
        v30 |= 8;
    if (((unsigned short)v18 & 0x400))
        v30 |= 4;
    if (((unsigned short)v18 & 0x800))
        v30 |= 2;
    if (((unsigned short)v18 & 0x1000))
        v30 |= 1;
    if (((unsigned short)v18 & 0x100))
        v30 |= 0x80000;
    v19 = v18;
    v20 = v19 & 0x6000;
    if (((unsigned short)v19 & 0x6000))
    {
        if (v20 == 0x2000)
        {
            v30 |= 0x100;
        }
        else if (v20 == 0x4000)
        {
            v30 |= 0x200;
        }
        else if (v20 == 0x6000)
        {
            v30 |= 0x300;
        }
    }
    v21 = v18 & 32832;
    v22 = v21 - 64;
    if (v21 == 64)
    {
        v30 |= 0x2000000;
    }
    else if (v22 == 0x7fc0)
    {
        v30 |= 0x3000000;
    }
    else if (v22 == 0x8000)
    {
        v30 |= 0x1000000;
    }
    v23 = ~(a1 & 50856735) & v30 | a1 & 50856735 & a0;
    if (v23 != v30)
    {
        a1 = sub_1036617d(v20, v23);
        sub_10367849(a1);
        v24 = _ccall(v16 & 3);
        a1 = v24;
        v25 = a1;
        v30 = 0;
        if ((char)v25 < 0)
            v30 = 16;
        if (((unsigned short)v25 & 0x200))
            v30 |= 8;
        if (((unsigned short)v25 & 0x400))
            v30 |= 4;
        if (((unsigned short)v25 & 0x800))
            v30 |= 2;
        if (((unsigned short)v25 & 0x1000))
            v30 |= 1;
        if (((unsigned short)v25 & 0x100))
            v30 |= 0x80000;
        v26 = v25;
        v27 = v26 & 0x6000;
        if (((unsigned short)v26 & 0x6000))
        {
            if (v27 == 0x2000)
            {
                v30 |= 0x100;
            }
            else if (v27 == 0x4000)
            {
                v30 |= 0x200;
            }
            else if (v27 == 0x6000)
            {
                v30 |= 0x300;
            }
        }
        v28 = v25 & 32832;
        v29 = v28 - 64;
        if (v28 == 64)
        {
            v30 |= 0x2000000;
        }
        else if (v29 == 0x7fc0)
        {
            v30 |= 0x3000000;
        }
        else if (v29 == 0x8000)
        {
            v30 |= 0x1000000;
        }
    }
    return v30 | v3 | 0x80000000;
}
```

## `sub_10366520` `0x10366520`

_114 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10366520(void* idx)
{
    unsigned int v5;  // ebx
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]

    v5 = 4294967295;
    if (!idx)
    {
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        *((unsigned int *)sub_103575e0()) = 22;
        sub_103535f2();
        return 4294967295;
    }
    if (((char)idx[12] & 131))
    {
        v5 = sub_10362481(idx);
        sub_103678bb(idx);
        if (sub_10366ef8(sub_10360e67(idx)) < NULL)
        {
            v5 = 4294967295;
        }
        else if ((int)idx[28])
        {
            v4 = (int)idx[28];
            sub_1035345e();
            *((unsigned int *)&idx[28]) = 0;
        }
    }
    *((unsigned int *)&idx[12]) = 0;
    return v5;
}
```

## `sub_10366592` `0x10366592`

_113 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a1530;

void sub_10366592(unsigned int a0)
{
    void* v9;  // esi
    unsigned int v10;  // ecx
    unsigned int v11;  // edx
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp+0x0]
    unsigned int v6;  // [bp+0xfffe8]
    unsigned int v7;  // [bp+0x100000]
    void* v8;  // [bp+0x10000c]

    sub_1035b0cc(&g_103a1530, 12);
    v6 = 4294967295;
    v9 = v8;
    if (!v9)
    {
        *((unsigned int *)sub_103575e0()) = 22;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        sub_103535f2();
        sub_1035b111(&g_103a1530, 12, v5, a0);
        return;
    }
    if (((char)v9[12] & 64))
    {
        *((unsigned int *)&v9[12]) = 0;
    }
    else
    {
        sub_1035cd52(v10, v11, v9);
        v7 = 0;
        v6 = sub_10366520(v9);
        v7 = 4294967294;
        sub_10366606();
    }
    sub_1035b111(&g_103a1530, 12, v5, a0);
    return;
}
```

## `sub_10366603` `0x10366603`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10366603(void)
{
    sub_10366606();
    return;
}
```

## `sub_10366606` `0x10366606`

_8 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[12];
    unsigned int field_c;
} struct_0;

int sub_10366606(void)
{
    struct_0 *v1;  // esi

    return sub_1035cdbc(v1);
}
```

## `sub_1036660e` `0x1036660e`

_215 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b07c;
extern struct_0 *g_1038b180;
extern unsigned int g_103a1550;
extern char g_103a3b70;
extern unsigned int g_103a3b80[4];

void sub_1036660e(unsigned int a0)
{
    unsigned int v9;  // eax
    unsigned int *v10;  // edi
    unsigned int v11;  // esi
    unsigned int *v12;  // eax
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp+0x0]
    unsigned int v6;  // [bp+0xfffe8]
    unsigned int v7;  // [bp+0x100000]
    unsigned int v8;  // [bp+0x10000c]

    sub_1035b0cc(&g_103a1550, 16);
    v9 = v8;
    if (v9 == 4294967294)
    {
        *((unsigned int *)sub_103575e0()) = 9;
    }
    else
    {
        if (v9 >= 0 && v9 < *((int *)&g_103a3b70))
        {
            v10 = &g_103a3b80[v9 >> 5];
            v11 = (v9 & 31) * 56;
            if ((*((char *)(v11 + *(v10) + 4)) & 1))
            {
                sub_10365188(v9);
                v7 = 0;
                if ((*((char *)(v11 + *(v10) + 4)) & 1))
                {
                    v9 = sub_10365117(v8);
                    if (!g_1038b180(v9))
                        v6 = g_1038b07c();
                    else
                        v6 = 0;
                    if (!v6)
                    {
                        v7 = 4294967294;
                        sub_103666e5();
                        sub_1035b111(v9, &g_103a1550, 16, v5);
                        return;
                    }
                    v12 = sub_103575f3();
                    *(v12) = v6;
                }
                *((unsigned int *)sub_103575e0()) = 9;
                v6 = 4294967295;
                v7 = 4294967294;
                sub_103666e5();
                sub_1035b111(v9, &g_103a1550, 16, v5);
                return;
            }
        }
        *((unsigned int *)sub_103575e0()) = 9;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        sub_103535f2();
    }
    sub_1035b111(v4, &g_103a1550, 16, v5);
    return;
}
```

## `sub_103666e5` `0x103666e5`

_10 bytes. (leaf/helper — see body)_

```c
int sub_103666e5(void)
{
    int v1;  // [bp+0x10000c]

    return sub_10365228(v1);
}
```

## `sub_103666ef` `0x103666ef`

_436 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b07c;
extern struct_0 *g_1038b17c;
extern struct_0 *g_1038b204;
extern struct_0 *g_1038b220;
extern struct_0 *g_1038b224;

unsigned int sub_103666ef(unsigned int a0, unsigned int a1, int a2, unsigned int a3, unsigned int a4)
{
    unsigned int v8;  // ebx
    unsigned int v9;  // esi
    unsigned int v18;  // 4101
    unsigned int v19;  // eax
    int v20;  // edi
    unsigned int v21;  // esi
    unsigned int v22;  // 4101
    unsigned int v24;  // eax
    unsigned int v25;  // eax
    int v26;  // edx
    unsigned int v27;  // esi
    unsigned int v10;  // edi
    int v28;  // edi
    unsigned int v29;  // 4124
    unsigned int v30;  // 4101
    int v31;  // esi
    unsigned int v32;  // eax
    unsigned int v33;  // eax
    int v34;  // eax
    unsigned int *v35;  // eax
    unsigned int v36;  // eax
    unsigned int v37;  // eax
    unsigned int v11;  // edx
    unsigned int v12;  // ecx
    unsigned int v13;  // eax
    unsigned int v14;  // ecx
    unsigned int v15;  // esi
    int v16;  // edi
    unsigned int v17;  // 4130
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x1c]
    int v4;  // [bp-0x14]
    int v5;  // [bp-0x10]
    int v6;  // [bp-0xc]
    void* v7;  // [bp-0x8]

    v2 = v8;
    v1 = v9;
    v0 = v10;
    v4 = 0;
    v5 = 0;
    v3 = sub_10360587(a0, a1, a2, 0, 0, 1);
    if ((v3 & v11) != 4294967295 && (v13 = sub_10360587(v12, v11, a2, 0, 0, 2), v14 = v13 & v11, v14 != 4294967295))
    {
        v15 = a3 - v13;
        v16 = a4 - v11 - (a3 < v13);
        v17 = _ccall(8, 12, a4, v11 ^ (unsigned int)(char)(a3 < v13), (unsigned int)(char)(a3 < v13));
        if (!((char)v17) && (v18 = (unsigned int)_ccall(14, 12, a4, v11 ^ (unsigned int)(char)(a3 < v13), (unsigned int)(char)(a3 < v13)), !((char)v18) || v15 > 0))
        {
            v19 = g_1038b224(8, 0x1000);
            v7 = g_1038b220(v19);
            if (!v7)
            {
                *((unsigned int *)sub_103575e0()) = 12;
            }
            else
            {
                v6 = sub_10367037(a2, 0x8000);
                do
                {
                    v20 = v16;
                    v21 = v15;
                    if (v20 >= 0 && !((v22 = (unsigned int)_ccall(14, 15, v20, 0, 0), (char)v22 && v21 < 0x1000)))
                        v24 = 0x1000;
                    else
                        v24 = v21;
                    if (sub_10360723(v12, v11, a2, v7, v24) == 4294967295)
                    {
                        if (*((int *)sub_103575f3()) == 5)
                            *((unsigned int *)sub_103575e0()) = 13;
                        v31 = -1;
                        v5 = -1;
                        goto LABEL_103667c7;
                    }
                } while ((v26 = (int)(v25 >> 31), v27 = v21 - v25, v28 = (int)(v20 - v26 - (unsigned int)(char)(v21 < v25)), v29 = (unsigned int)_ccall(8, 12, v20, v26 ^ (unsigned int)(char)(v21 < v25), (unsigned int)(char)(v21 < v25)), !((char)v29) && (v30 = (unsigned int)_ccall(14, 12, v20, v26 ^ (unsigned int)(char)(v21 < v25), (unsigned int)(char)(v21 < v25)), v15 = v27, v16 = v28, !((char)v30) || !((v15 = v27, v16 = v28, !v15)))));
                v31 = v4;
LABEL_103667c7:
                sub_10367037(a2, v6);
                v32 = g_1038b224(0, v7);
                g_1038b204(v32);
                goto LABEL_10366873;
            }
        }
        else if (!(v16 <= 0 && (v16 < 0 || v15 < 0)))
        {
LABEL_1036687f:
            if ((sub_10360587(v12, v11, a2, v3, v11, 0) & v11) != 4294967295)
                return 0;
        }
        else if ((sub_10360587(v14, v11, a2, a3, a4, 0) & v11) != 4294967295)
        {
            v33 = sub_10365117(a2);
            v34 = -(-(0 < g_1038b17c(v33))) - 1;
            v4 = v34;
            v5 = v4 >> 31;
            if ((v4 & v5) != 4294967295)
                goto LABEL_1036687f;
            *((unsigned int *)sub_103575e0()) = 13;
            v35 = sub_103575f3();
            *(v35) = g_1038b07c();
            v31 = v4;
LABEL_10366873:
            if ((v31 & v5) != 4294967295)
                goto LABEL_1036687f;
        }
    }
    v36 = *((int *)sub_103575e0());
    v37 = *((int *)sub_103575e0());
    return *((int *)sub_103575e0());
}
```

## `sub_103668a3` `0x103668a3`

_1473 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    char padding_0[4];
    char field_4;
} struct_2;

typedef struct struct_0 {
    char padding_0[4];
    char field_4;
    char field_5;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b07c;
extern struct_1 *g_1038b0a8;
extern struct_1 *g_1038b104;
extern char g_1038f178;
extern char g_103a3b70;
extern unsigned int g_103a3b80[4];

unsigned int sub_103668a3(unsigned int a0, void* a1, unsigned int iter)
{
    unsigned int v17;  // esi
    unsigned int v18;  // ebx
    unsigned int v27;  // eax
    unsigned int v28;  // ecx
    char v29[6];  // ecx
    struct_2 *v30;  // eax
    void* iter1;  // ebx
    void* v32;  // ecx
    void* v33;  // eax
    unsigned int v34;  // ecx
    struct_2 *v35;  // eax
    void* iter2;  // ebx
    unsigned int v19;  // esi
    unsigned int j;  // eax
    unsigned int v38;  // ecx
    unsigned int v39;  // ecx
    struct_0 *v40;  // ecx
    void* v41;  // ebx
    unsigned int v42;  // ebx
    unsigned int *v43;  // eax
    void* node;  // ebx
    void* v45;  // eax
    unsigned short v46;  // cx
    unsigned int v20;  // edi
    void* v47;  // ecx
    struct_2 *v48;  // esi
    unsigned int v49;  // eax
    unsigned int *v21;  // edi
    char v22[37];  // eax
    unsigned int v23;  // eax
    void* v24;  // eax
    unsigned int v25;  // eax
    unsigned int v26;  // edx
    void* v0;  // [bp-0x58]
    unsigned int *v1;  // [bp-0x44]
    unsigned int v2;  // [bp-0x40]
    unsigned int v3;  // [bp-0x3c]
    unsigned int v4;  // [bp-0x38]
    unsigned int v5;  // [bp-0x34]
    unsigned int v6;  // [bp-0x30]
    unsigned int v7;  // [bp-0x2c]
    unsigned int v8;  // [bp-0x28]
    unsigned int v9;  // [bp-0x24]
    char v10;  // [bp-0x1c], Other Possible Types: unsigned int
    unsigned int v11;  // [bp-0x18]
    void* v12;  // [bp-0x14], Other Possible Types: unsigned int
    void* v13;  // [bp-0x10]
    char v14;  // [bp-0xc], Other Possible Types: unsigned short
    char v15;  // [bp-0x6]
    char v16;  // [bp-0x5]

    v9 = v17;
    v8 = 4294967294;
    v11 = v8;
    if (a0 == v8)
    {
        *((unsigned int *)sub_103575f3()) = 0;
        *((unsigned int *)sub_103575e0()) = 9;
        return 4294967295;
    }
    v8 = v18;
    if (a0 < 0 || a0 >= *((int *)&g_103a3b70))
    {
        *((unsigned int *)sub_103575f3()) = 0;
        v7 = 0;
        v6 = 0;
        v5 = 0;
        v4 = 0;
        v3 = 0;
        *((unsigned int *)sub_103575e0()) = 9;
        sub_103535f2();
        v49 = 4294967295;
    }
    else
    {
        v19 = (a0 & 31) * 56;
        v7 = v20;
        v21 = &g_103a3b80[a0 >> 5];
        v22 = *(v21) + v19;
        if (!(v22[4] & 1))
        {
            *((unsigned int *)sub_103575f3()) = 0;
            *((unsigned int *)sub_103575e0()) = 9;
            goto LABEL_103669ab;
        }
        if (iter <= 2147483647)
        {
            v12 = 0;
            if (!(iter && !(v22[4] & 2)))
            {
                v49 = 0;
            }
            else if (a1)
            {
                v15 = v22[36] & 127;
                v23 = v22[36] & 127;
                v6 = 4;
                if (v23 != 1)
                {
                    iter = iter;
                    if (v23 == 2)
                    {
                        if (((char)~(iter) & 1))
                        {
                            iter &= 4294967294;
                            goto LABEL_10366986;
                        }
                    }
                    else
                    {
LABEL_10366986:
                        v24 = a1;
                        v13 = v24;
                        goto LABEL_10366a12;
                    }
                }
                else if (((char)~(iter) & 1))
                {
                    v25 = iter >> 1;
                    iter = 4;
                    if (v25 >= 4)
                        iter = v25;
                    v13 = sub_10357482(iter);
                    if (!v13)
                    {
                        *((unsigned int *)sub_103575e0()) = 12;
                        *((unsigned int *)sub_103575f3()) = 8;
LABEL_103669ee:
                        v49 = 4294967295;
                    }
                    else
                    {
                        v27 = sub_10360587(iter, v26, a0, 0, 0, 1);
                        v28 = *(v21);
                        *((unsigned int *)(v19 + v28 + 40)) = v27;
                        v24 = v13;
                        *((unsigned int *)(v19 + v28 + 44)) = v26;
LABEL_10366a12:
                        v29 = *(v21) + v19;
                        if ((v29[4] & 72) && v29[5] != 10 && iter)
                        {
                            *((char *)v24) = v29[5];
                            v24 += 1;
                            iter -= 1;
                            v12 = 1;
                            *((char *)(v19 + *(v21) + 5)) = 10;
                            if (v15 && *((char *)(v19 + *(v21) + 37)) != 10 && iter)
                            {
                                *((char *)v24) = *((char *)(v19 + *(v21) + 37));
                                v24 += 1;
                                iter -= 1;
                                v12 = 2;
                                *((char *)(v19 + *(v21) + 37)) = 10;
                                if (v15 == 1 && *((char *)(v19 + *(v21) + 38)) != 10 && iter)
                                {
                                    *((char *)v24) = *((char *)(v19 + *(v21) + 38));
                                    v24 += 1;
                                    iter -= 1;
                                    v12 = 3;
                                    *((char *)(v19 + *(v21) + 38)) = 10;
                                }
                            }
                        }
                        if (g_1038b0a8(*((int *)(v19 + *(v21))), v24, iter, &v10, 0) && v10 >= 0 && v10 <= iter)
                        {
                            v12 += v10;
                            v30 = v19 + *(v21) + 4;
                            if (!(v30->padding_0[0] & 128))
                                goto LABEL_10366cb8;
                            if (v15 != 2)
                            {
                                if (v10 && *((char *)v13) == 10)
                                    v30->padding_0[0] = v30->padding_0[0] | 4;
                                else
                                    v30->padding_0[0] = v30->padding_0[0] & 251;
                                iter1 = v13;
                                iter = iter1;
                                v12 += iter1;
                                if (iter1 < v12)
                                {
                                    do
                                    {
                                        v32 = iter;
                                        if (*((char *)v32) == 26)
                                        {
                                            v35 = v19 + *(v21) + 4;
                                            if (!(v35->padding_0[0] & 64))
                                            {
                                                v35->padding_0[0] = v35->padding_0[0] | 2;
                                                break;
                                            }
                                            else
                                            {
                                                *((char *)iter1) = *((char *)v32);
                                                iter1 += 1;
                                                break;
                                            }
                                        }
                                        if (*((char *)v32) != 13)
                                        {
                                            *((char *)iter1) = *((char *)v32);
                                            iter1 += 1;
                                            iter = v32 + 1;
                                            continue;
                                        }
                                        if (v32 < v12 - 1)
                                        {
                                            v33 = v32 + 1;
                                            if (*((char *)v33) == 10)
                                            {
                                                iter = v32 + 2;
                                                goto LABEL_10366b38;
                                            }
                                            else
                                            {
                                                iter = v33;
                                                goto LABEL_10366baf;
                                            }
                                        }
                                        else
                                        {
                                            iter += 1;
                                            if ((g_1038b0a8(*((int *)(v19 + *(v21))), &v16, 1, &v10, 0) || !g_1038b07c()) && v10)
                                            {
                                                if ((*((char *)(v19 + *(v21) + 4)) & 72))
                                                {
                                                    if (v16 != 10)
                                                    {
                                                        *((char *)iter1) = 13;
                                                        *((char *)(v19 + *(v21) + 5)) = v16;
                                                        iter1 += 1;
                                                        continue;
                                                    }
                                                }
                                                else
                                                {
                                                    if (iter1 != v13 || v16 != 10)
                                                    {
                                                        sub_10360587(v34, v26, a0, -1, 4294967295, 1);
                                                        if (v16 == 10)
                                                            continue;
                                                        goto LABEL_10366baf;
                                                    }
                                                }
LABEL_10366b38:
                                                *((char *)iter1) = 10;
                                                iter1 += 1;
                                            }
                                            else
                                            {
LABEL_10366baf:
                                                *((char *)iter1) = 13;
                                                iter1 += 1;
                                            }
                                        }
                                    } while (iter < v12);
                                }
                                v12 = iter1 - v13;
                                if (v15 != 1 || !v12)
                                    goto LABEL_10366cb8;
                                iter2 = iter1 - 1;
                                if (*((char *)iter2) >= 0)
                                {
                                    iter2 += 1;
                                    goto LABEL_10366c83;
                                }
                                j = 1;
                                for (v38 = *((char *)iter2); !(&g_1038f178)[v38] && j <= 4 && iter2 >= v13; j += 1)
                                {
                                    iter2 -= 1;
                                    v38 = *((char *)iter2);
                                }
                                v39 = *(&(&g_1038f178)[*((char *)iter2)]);
                                if (!v39)
                                {
                                    *((unsigned int *)sub_103575e0()) = 42;
LABEL_10366cb4:
                                    v11 = 4294967295;
                                }
                                else
                                {
                                    if (v39 + 1 == j)
                                    {
                                        iter2 += j;
                                    }
                                    else
                                    {
                                        v40 = *(v21) + v19;
                                        if ((v40->field_4 & 72))
                                        {
                                            v41 = iter2 + 1;
                                            v40->field_5 = *((char *)iter2);
                                            if (j >= 2)
                                            {
                                                *((char *)(v19 + *(v21) + 37)) = *((char *)v41);
                                                v41 += 1;
                                            }
                                            if (j == 3)
                                            {
                                                *((char *)(v19 + *(v21) + 38)) = *((char *)v41);
                                                v41 += 1;
                                            }
                                            iter2 = v41 - j;
                                        }
                                        else
                                        {
                                            sub_10360587(v40, -(j) >> 31, a0, -(j), -(j) >> 31, 1);
                                        }
                                    }
LABEL_10366c83:
                                    v42 = iter2 - v13;
                                    v12 = g_1038b104(65001, 0, v13, v42, a1, iter >> 1);
                                    if (!v12)
                                    {
                                        v43 = g_1038b07c();
                                        goto LABEL_10366cad;
                                    }
                                    else
                                    {
                                        v12 *= 2;
                                        *((unsigned int *)(v19 + *(v21) + 48)) = v12 != v42;
                                    }
                                }
                            }
                            else
                            {
                                if (v10 && *((short *)v13) == 10)
                                    v30->padding_0[0] = v30->padding_0[0] | 4;
                                else
                                    v30->padding_0[0] = v30->padding_0[0] & 251;
                                node = v13;
                                iter = node;
                                v12 += node;
                                if (node < v12)
                                {
                                    do
                                    {
                                        v45 = iter;
                                        v46 = *((short *)v45);
                                        if (v46 == 26)
                                        {
                                            v48 = v19 + *(v21) + 4;
                                            if (!(v48->padding_0[0] & 64))
                                            {
                                                v48->padding_0[0] = v48->padding_0[0] | 2;
                                                break;
                                            }
                                            else
                                            {
                                                *((short *)node) = *((short *)v45);
                                                node += 2;
                                                break;
                                            }
                                        }
                                        if (v46 != 13)
                                        {
                                            *((unsigned short *)node) = v46;
                                            node += 2;
                                            iter = v45 + 2;
                                            continue;
                                        }
                                        if (v45 < v12 - 2)
                                        {
                                            v47 = v45 + 2;
                                            if (*((short *)v47) == 10)
                                            {
                                                iter = v45 + 4;
                                                goto LABEL_10366d5b;
                                            }
                                            else
                                            {
                                                iter = v47;
                                                goto LABEL_10366df0;
                                            }
                                        }
                                        else
                                        {
                                            iter += 2;
                                            if ((g_1038b0a8(*((int *)(v19 + *(v21))), &v14, 2, &v10, 0) || !g_1038b07c()) && v10)
                                            {
                                                if ((*((char *)(v19 + *(v21) + 4)) & 72))
                                                {
                                                    if (v14 != 10)
                                                    {
                                                        *((unsigned short *)node) = 13;
                                                        *((char *)(v19 + *(v21) + 5)) = v14;
                                                        *((char *)(v19 + *(v21) + 37)) = *((char *)((void*)&v14 + 1));
                                                        *((char *)(v19 + *(v21) + 38)) = 10;
                                                        goto LABEL_10366df5;
                                                    }
                                                }
                                                else
                                                {
                                                    if (node != v13 || v14 != 10)
                                                    {
                                                        sub_10360587(v34, v26, a0, -2, 4294967295, 1);
                                                        if (v14 == 10)
                                                            continue;
                                                        goto LABEL_10366df0;
                                                    }
                                                }
LABEL_10366d5b:
                                                *((unsigned short *)node) = 10;
                                                goto LABEL_10366df5;
                                            }
                                            else
                                            {
LABEL_10366df0:
                                                *((unsigned short *)node) = 13;
LABEL_10366df5:
                                                node += 2;
                                            }
                                        }
                                    } while (iter < v12);
                                }
                                v12 = node - v13;
                            }
                        }
                        else
                        {
                            v43 = g_1038b07c();
                            v1 = 0x5;
                            if (v43 == v1)
                            {
                                *((unsigned int *)sub_103575e0()) = 9;
                                *((unsigned int **)sub_103575f3()) = v1;
                                goto LABEL_10366cb4;
                            }
                            if (v43 != 0x6d)
                            {
LABEL_10366cad:
                                sub_10357606(v43);
                                goto LABEL_10366cb4;
                            }
                            else
                            {
                                v11 = 0;
                            }
                        }
LABEL_10366cb8:
                        if (v13 != a1)
                        {
                            v0 = v13;
                            sub_1035345e();
                        }
                        v49 = v11;
                        if (v49 == 4294967294)
                            v49 = v12;
                    }
                }
            }
        }
        else
        {
            *((unsigned int *)sub_103575f3()) = 0;
            *((unsigned int *)sub_103575e0()) = 22;
LABEL_103669ab:
            v6 = 0;
            v5 = 0;
            v4 = 0;
            v3 = 0;
            v2 = 0;
            sub_103535f2();
            goto LABEL_103669ee;
        }
    }
    return v49;
}
```

## `sub_10366e64` `0x10366e64`

_148 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    char padding_0[60];
    char field_3c;
    char padding_3d[55];
    char field_74;
} struct_1;

typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

typedef struct struct_0 {
    struct struct_1 *field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
} struct_0;

extern struct_2 *g_1038b07c;
extern struct_2 *g_1038b128;
extern struct_0 g_103a3b80;

unsigned int sub_10366e64(int a0)
{
    unsigned int v2;  // esi
    unsigned int v3;  // edi
    unsigned int v4;  // eax
    unsigned int v5;  // eax
    unsigned int *v6;  // eax
    unsigned int v0;  // [bp-0x8]
    unsigned int v1;  // [bp-0x4]

    v1 = v2;
    v0 = v3;
    if (sub_10365117(a0) != 4294967295 && ((a0 != 1 || !(g_103a3b80.field_0->field_74 & 1)) && (a0 != 2 || !(g_103a3b80.field_0->field_3c & 1)) || (v4 = sub_10365117(2), sub_10365117(1) != sub_10365117(2))) && !((v5 = sub_10365117(a0), g_1038b128(sub_10365117(a0)))))
        v6 = g_1038b07c();
    else
        v6 = NULL;
    sub_10365096(a0);
    (&g_103a3b80.field_0)[a0 >> 5]->padding_0[4 + 56 * (a0 & 31)] = 0;
    if (!v6)
        return 0;
    sub_10357606(v6);
    return 4294967295;
}
```

## `sub_10366ef8` `0x10366ef8`

_195 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a1570;
extern char g_103a3b70;
extern unsigned int g_103a3b80[4];

void sub_10366ef8(unsigned int a0)
{
    unsigned int v9;  // eax
    unsigned int *v10;  // ebx
    unsigned int v11;  // esi
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp+0x0]
    unsigned int v6;  // [bp+0xfffe8]
    unsigned int v7;  // [bp+0x100000]
    unsigned int v8;  // [bp+0x10000c]

    sub_1035b0cc(&g_103a1570, 16);
    v9 = v8;
    if (v9 == 4294967294)
    {
        *((unsigned int *)sub_103575f3()) = 0;
        *((unsigned int *)sub_103575e0()) = 9;
    }
    else
    {
        if (v9 >= 0 && v9 < *((int *)&g_103a3b70))
        {
            v10 = &g_103a3b80[v9 >> 5];
            v11 = (v9 & 31) * 56;
            if ((*((char *)(*(v10) + v11 + 4)) & 1))
            {
                sub_10365188(v9);
                v7 = 0;
                if ((*((char *)(*(v10) + v11 + 4)) & 1))
                {
                    v6 = sub_10366e64(v8);
                }
                else
                {
                    *((unsigned int *)sub_103575e0()) = 9;
                    v6 = 4294967295;
                }
                v7 = 4294967294;
                sub_10366fbb();
                sub_1035b111(&g_103a1570, 16, v5, a0);
                return;
            }
        }
        *((unsigned int *)sub_103575f3()) = 0;
        *((unsigned int *)sub_103575e0()) = 9;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        sub_103535f2();
    }
    sub_1035b111(&g_103a1570, 16, v5, a0);
    return;
}
```

## `sub_10366fbb` `0x10366fbb`

_10 bytes. (leaf/helper — see body)_

```c
int sub_10366fbb(void)
{
    int v1;  // [bp+0x10000c]

    return sub_10365228(v1);
}
```

## `sub_10366fc5` `0x10366fc5`

_114 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    char padding_0[4];
    char field_4;
} struct_2;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b07c;
extern struct_0 *g_1038b1a4;
extern unsigned int g_103a3b80[4];

unsigned int sub_10366fc5(int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v1;  // esi
    unsigned int v2;  // eax
    unsigned int v3;  // edi
    unsigned int v4;  // edi
    unsigned int *v6;  // eax
    struct_2 *v7;  // eax
    unsigned int v0;  // [bp-0x4]

    v0 = v1;
    v2 = sub_10365117(a0);
    if (v2 == 4294967295)
    {
        *((unsigned int *)sub_103575e0()) = 9;
        return 4294967295;
    }
    v4 = g_1038b1a4(v2, a1, 0, a2, v3);
    v6 = (v4 == 4294967295 ? g_1038b07c() : NULL);
    if (!v6)
    {
        v7 = g_103a3b80[a0 >> 5] + (a0 & 31) * 56 + 4;
        v7->padding_0[0] = v7->padding_0[0] & 253;
        return v4;
    }
    sub_10357606(v6);
    return 4294967295;
}
```

## `sub_10367037` `0x10367037`

_188 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    char field_4;
    char padding_5[31];
    char field_24;
} struct_0;

typedef struct struct_1 {
    char padding_0[36];
    char field_24;
} struct_1;

extern unsigned int g_103a3b80[4];

unsigned int sub_10367037(int a0, unsigned int a1)
{
    unsigned int v0;  // edx
    unsigned int *v1;  // esi
    struct_0 *idx;  // ecx
    int v3;  // eax
    struct_1 *v4;  // ecx
    char v5;  // dl
    struct_1 *v6;  // ecx

    v0 = (a0 & 31) * 56;
    v1 = &g_103a3b80[a0 >> 5];
    idx = *(v1) + v0;
    a0 = idx->field_4 & 128;
    v3 = idx->field_24 * 2 >> 1;
    if (a1 == 0x4000)
    {
        idx->field_4 = idx->field_4 | 128;
        v6 = *(v1) + v0 + 36;
        v6->padding_0[0] = v6->padding_0[0] & 128;
    }
    else if (a1 != 0x8000)
    {
        if (!(a1 != 0x10000 && a1 != 0x20000))
        {
            idx->field_4 = idx->field_4 | 128;
            v4 = *(v1) + v0 + 36;
            v5 = v4->padding_0[0] & 130 | 2;
        }
        else if (a1 == 0x40000)
        {
            idx->field_4 = idx->field_4 | 128;
            v4 = *(v1) + v0 + 36;
            v5 = v4->padding_0[0] & 129 | 1;
        }
        else
        {
            return (!a0 ? 0x8000 : (-(0 < v3) & 0xc000) + 0x4000);
        }
        v4->padding_0[0] = v5;
    }
    else
    {
        idx->field_4 = idx->field_4 & 127;
    }
    return (!a0 ? 0x8000 : (-(0 < v3) & 0xc000) + 0x4000);
}
```

## `sub_103670f3` `0x103670f3`

_52 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a3abc;

unsigned int sub_103670f3(unsigned int *a0)
{
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    if (a0)
    {
        *(a0) = g_103a3abc;
        return 0;
    }
    v4 = 0;
    v3 = 0;
    v2 = 0;
    v1 = 0;
    v0 = 0;
    *((unsigned int *)sub_103575e0()) = 22;
    sub_103535f2();
    v4 = 22;
    return v4;
}
```

## `sub_10367127` `0x10367127`

_173 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

typedef struct struct_2 {
    char padding_0[112];
    unsigned int field_70;
} struct_2;

unsigned int sub_10367127(unsigned int a0, unsigned int *a1)
{
    unsigned int v5;  // ebx
    unsigned int v6;  // eax
    unsigned int v7;  // eax
    unsigned int v0;  // [bp-0x1c]
    struct_0 v1;  // [bp-0x18]
    struct_2 *idx;  // [bp-0x10]
    char v3;  // [bp-0xc]
    char v4;  // [bp-0x8], Other Possible Types: unsigned short

    if ((unsigned short)a0 == 65535)
        return 0xffff;
    v0 = v5;
    sub_103536a7(&v1, a1);
    if (!*((int *)(v1 + 20)))
    {
        v6 = a0;
        if ((unsigned short)(v6 - 65) <= 25)
        {
            v6 += 32;
            goto LABEL_10367163;
        }
    }
    else if ((unsigned short)a0 < 0x100)
    {
        v7 = (unsigned short)a0;
        if (sub_10363ca3(a0, 1, &v1))
        {
            v6 = _INSERT(v7, 0, *((char *)(*((int *)(v1 + 0xcc)) + v7)));
LABEL_10367163:
            v7 = (unsigned short)v6;
        }
    }
    else
    {
        v7 = (unsigned short)a0;
        if (sub_10367b48(&v1, *((int *)((unsigned int)v1 + 20)), 0x100, &/* unsupported instruction */, 1, &v4, 1, *((int *)((unsigned int)v1 + 4))))
            v7 = v4;
    }
    if (!v3)
        return v7;
    idx->field_70 = idx->field_70 & 4294967293;
    return v7;
}
```

## `sub_103671d4` `0x103671d4`

_236 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

typedef struct struct_1 {
    char padding_0[4];
    int field_4;
    unsigned int field_8;
    int field_c;
} struct_1;

unsigned int sub_103671d4(int a0, int a1, int a2, unsigned int a3)
{
    unsigned int v10;  // esi
    unsigned int v11;  // eax
    unsigned int v12;  // eax
    unsigned int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x2c]
    unsigned int v2;  // [bp-0x28]
    unsigned int v3;  // [bp-0x24]
    unsigned int v4;  // [bp-0x20]
    unsigned int v5;  // [bp-0x1c]
    struct_0 v6;  // [bp-0x14]
    struct_1 *v7;  // [bp-0x10]
    struct_0 *idx;  // [bp-0xc]
    char v9;  // [bp-0x8]

    sub_103536a7(&v6, a3);
    if (!a2)
    {
        if (!v9)
            return 0;
        idx[8].field_8 = idx[8].field_8 & 4294967293;
        return 0;
    }
    else
    {
        if (a0 && a1)
        {
            v5 = v10;
            if (a2 > 2147483647)
            {
                v4 = 0;
                v3 = 0;
                v2 = 0;
                v1 = 0;
                v0 = 0;
                *((unsigned int *)sub_103575e0()) = 22;
                sub_103535f2();
LABEL_1036729d:
                if (v9)
                    idx[8].field_8 = idx[8].field_8 & 4294967293;
                v11 = 2147483647;
            }
            else
            {
                if (!v7->field_8)
                {
                    v11 = sub_10367f51(a0, a1, a2, a3);
                }
                else
                {
                    v12 = sub_10367f11(&v6, v7->field_c, 4097, a0, a2, a1, a2, v7->field_4);
                    if (!v12)
                        goto LABEL_1036729d;
                    v11 = v12 - 2;
                }
                if (v9)
                    idx[8].field_8 = idx[8].field_8 & 4294967293;
            }
            return v11;
        }
        v5 = 0;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        *((unsigned int *)sub_103575e0()) = 22;
        sub_103535f2();
        if (!v9)
            return 2147483647;
        idx[8].field_8 = idx[8].field_8 & 4294967293;
        return 2147483647;
    }
}
```

## `sub_103672c0` `0x103672c0`

_23 bytes. (leaf/helper — see body)_

```c
unsigned int sub_103672c0(int a0, int a1, int a2)
{
    return sub_103671d4(a0, a1, a2, 0);
}
```

## `sub_103672d7` `0x103672d7`

_149 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b040;
extern unsigned int g_103a3024;

unsigned int sub_103672d7(unsigned int a0)
{
    unsigned int v7;  // ebx
    unsigned int v8;  // esi
    unsigned int v9;  // edi
    unsigned int iter;  // edi
    unsigned int v11;  // eax
    unsigned int v0;  // [bp-0x9c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc], Other Possible Types: unsigned int
    unsigned int v5;  // [bp-0x8]

    v5 = a0;
    v4 = a0;
    v3 = v7;
    v2 = v8;
    v1 = v9;
    iter = g_103a3024;
    v5 = 0;
    v11 = *((int *)g_103a3024);
    if (!*((int *)g_103a3024))
        return 0;
    do
    {
        v4 = g_1038b040(0, 0, v11, 4294967295, 0, 0, 0, 0);
        if (!v4)
            return 4294967295;
        v5 = sub_103574c2(v4, 1);
        if (!v5)
            return 4294967295;
        if (!g_1038b040(0, 0, *((int *)iter), 4294967295, v5, v4, 0, 0))
        {
            v0 = v5;
            sub_1035345e();
            return 4294967295;
        }
        if (sub_103680f3(&v5, 0) < 0 && v5)
        {
            v0 = v5;
            sub_1035345e();
            v5 = 0;
        }
        iter += 4;
        v11 = *((int *)iter);
    } while (*((int *)iter));
    return 0;
}
```

## `sub_1036736c` `0x1036736c`

_548 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    char padding_0[4];
    unsigned int field_4;
    char padding_8[12];
    unsigned int field_14;
} struct_2;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b040;
extern struct_0 *g_1038b07c;
extern struct_0 *g_1038b1a8;
extern struct_0 *g_1038b1ac;
extern unsigned int g_1038e180;
extern char g_1039487c;
extern unsigned int g_103a3ab8;

int sub_1036736c(struct_2 **a0, unsigned int a1, unsigned int a2, int a3, void* a4, unsigned int a5, unsigned int a6)
{
    unsigned int v12;  // ebx
    unsigned int v13;  // esi
    unsigned int v21;  // eax
    unsigned int *v22;  // ebx
    unsigned int *iter;  // eax
    unsigned int v24;  // edi
    void* v25;  // esi
    unsigned int v14;  // edi
    unsigned int v15;  // eax
    unsigned int v16;  // eax
    unsigned int v17;  // esi
    unsigned int v18;  // eax
    char *node;  // eax
    unsigned int v0;  // [bp-0x70]
    unsigned int v1;  // [bp-0x68]
    unsigned int v2;  // [bp-0x50]
    unsigned int v3;  // [bp-0x34]
    unsigned int v4;  // [bp-0x20]
    unsigned int v5;  // [bp-0x1c]
    unsigned int v6;  // [bp-0x18]
    unsigned int v7;  // [bp-0x14]
    unsigned int v8;  // [bp-0x10]
    char *v9;  // [bp-0xc], Other Possible Types: char
    unsigned int v10;  // [bp-0x8]
    char v11;  // [bp-0x4]

    v10 = g_1038e180 ^ &v11;
    v6 = v12;
    v5 = v13;
    v4 = v14;
    if (a3 < -1)
        return sub_10351225();
    v15 = g_103a3ab8;
    if (!v15)
    {
        if (g_1038b1a8(1, &g_1039487c, 1, &v9))
        {
            g_103a3ab8 = 1;
            g_1038b1a8(a1, a2, a3, a4);
            return sub_10351225();
        }
        if (g_1038b07c() == 120)
        {
            v3 = 2;
            v15 = 2;
            g_103a3ab8 = 2;
        }
        else
        {
            v15 = g_103a3ab8;
        }
    }
    if (v15 == 1)
    {
        g_1038b1a8(a1, a2, a3, a4);
        return sub_10351225();
    }
    else if (v15 == 2 || !v15)
    {
        v8 = 0;
        if (!a6)
            a6 = *(a0)->field_14;
        if (!a5)
            a5 = *(a0)->field_4;
        v16 = sub_1035fd30(a6);
        if (a5 != v16 && v16 != -1)
            a5 = v16;
        v2 = a5;
        v17 = g_1038b040(a5, 0, a2, a3, 0, 0, 0, 0);
        v7 = v17;
        if (v17)
        {
            if (v17 > 0 && v17 <= 0xffffffe0)
            {
                v18 = v17 + 8;
                if (v18 <= 0x400)
                {
                    sub_1035de90();
                    node = &v2;
                    if (!&v2)
                        goto LABEL_10367487;
                    v2 = 0xcccc;
                    goto LABEL_10367484;
                }
                else
                {
                    node = sub_10355a15(v18);
                    if (node)
                    {
                        *((unsigned int *)&node) = 0xdddd;
LABEL_10367484:
                        node += 8;
                    }
                }
LABEL_10367487:
                v9 = node;
            }
            else
            {
                v9 = NULL;
            }
            if (v9)
            {
                sub_10350ad0(v9, 0, v17);
                v1 = a2;
                v0 = a5;
                if (g_1038b040(a5, 0, a2, a3, v9, v17, 0, 0))
                {
                    if (v17 + 1 > 0 && v17 + 1 <= 2147483632)
                    {
                        v21 = v17 * 2 + 10;
                        if (v21 <= 0x400)
                        {
                            sub_1035de90();
                            if (!&v0)
                            {
                                sub_103548d8(v9);
                                return sub_10351225();
                            }
                            v0 = 0xcccc;
                            v22 = &v1;
                        }
                        else
                        {
                            iter = sub_10355a15(v21);
                            if (iter)
                            {
                                *(iter) = 0xdddd;
                                iter += 2;
                            }
                            v22 = iter;
                        }
                    }
                    else
                    {
                        v22 = NULL;
                    }
                    if (v22)
                    {
                        if (!a6)
                            a6 = *(a0)->field_14;
                        v24 = a3 * 2;
                        v25 = v24 + (char *)v22;
                        *((unsigned short *)v25) = 65535;
                        *((unsigned short *)&v25[2]) = 65535;
                        v8 = g_1038b1ac(a6, a1, v9, v7, v22);
                        if ((short)v25[2] != 65535 && *((short *)v25) == 65535)
                            sub_10350ec0(a4, v22, v24);
                        else
                            v8 = 0;
                        sub_103548d8(v22);
                    }
                }
                sub_103548d8(v9);
                return sub_10351225();
            }
        }
    }
    return sub_10351225();
}
```

## `sub_10367590` `0x10367590`

_62 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

int sub_10367590(unsigned int *a0, unsigned int a1, unsigned int a2, int a3, void* a4, unsigned int a5, unsigned int a6)
{
    int v3;  // eax
    struct_0 v0;  // [bp-0x14]
    struct_0 *idx;  // [bp-0xc]
    char v2;  // [bp-0x8]

    sub_103536a7(&v0, a0);
    v3 = sub_1036736c(&v0, a1, a2, a3, a4, a5, a6);
    if (v2)
        idx[8].field_8 = idx[8].field_8 & 4294967293;
    return v3;
}
```

## `sub_103675d0` `0x103675d0`

_97 bytes. (leaf/helper — see body)_

```c
unsigned int sub_103675d0(char *iter, char *node, unsigned int a2)
{
    unsigned int i;  // ecx
    char v1;  // ah
    char v2;  // al
    char v3;  // al
    unsigned int v4;  // cc_dep1
    unsigned int v5;  // cc_dep2
    unsigned int v6;  // ecx

    if (!a2)
        return a2;
    do
    {
        i = a2;
        v1 = *(iter);
        v2 = *(node);
        v3 = v2;
        if (!*(iter) || (v3 = v2, v3 = v3, !v2))
            break;
        iter += 1;
        node += 1;
        if (v1 >= 65 && v1 <= 90)
            v1 += 32;
        if (v3 >= 65 && v3 <= 90)
            v3 += 32;
        v4 = v1;
        v5 = v3;
        if (v1 != v3)
            goto LABEL_10367621;
        v6 = i - 1;
        a2 = v6;
    } while (i != 1);
    v4 = v1;
    v5 = v3;
    if (v1 == v3)
        return 0;
LABEL_10367621:
    if (v4 >= v5)
        return 0;
    return 4294967295;
    return 0;
}
```

## `sub_10367631` `0x10367631`

_460 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    char field_a;
} struct_0;

extern unsigned int g_1038e180;

void sub_10367631(char *iter, unsigned int i, struct_0 *ptr)
{
    unsigned int v10;  // ebx
    unsigned int v11;  // esi
    unsigned int v20;  // ebx
    unsigned int v21;  // esi
    unsigned int v22;  // ebx
    unsigned int v23;  // esi
    unsigned int v24;  // ecx
    unsigned int v25;  // edi
    unsigned int v26;  // ebx
    unsigned int v27;  // edx
    unsigned int v28;  // esi
    unsigned int v29;  // ecx
    unsigned int v12;  // edi
    unsigned int v30;  // edx
    unsigned int v31;  // ecx
    unsigned int v32;  // edx
    unsigned int v33;  // esi
    unsigned int v34;  // edi
    unsigned int v35;  // ecx
    struct_0 *v13;  // esi
    unsigned int v14;  // edi
    unsigned int v15;  // edx
    unsigned int v16;  // ecx
    unsigned int v17;  // esi
    unsigned int v18;  // edx
    unsigned int v19;  // edi
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x20]
    unsigned int node;  // [bp-0x1c]
    unsigned int v4;  // [bp-0x18]
    unsigned int v5;  // [bp-0x14]
    unsigned int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]
    char v9;  // [bp-0x4]

    v8 = g_1038e180 ^ &v9;
    v2 = v10;
    v1 = v11;
    v0 = v12;
    node = 16462;
    memset(ptr, 0, 12);
    if (i > 0)
    {
        do
        {
            v5 = ptr->field_0;
            v13 = &ptr->field_4;
            v6 = v13->field_0;
            v7 = v13->field_4;
            v14 = ptr->field_0 * 2;
            v15 = ptr->field_4 * 2 | ptr->field_0 >> 31;
            v4 = v14;
            v4 = 0;
            v16 = (ptr->field_8 * 2 | ptr->field_4 >> 31) * 2 | v15 >> 31;
            v17 = v14 * 2;
            v18 = v15 * 2 | v14 >> 31;
            v19 = v17 + v5;
            ptr->field_0 = v17;
            ptr->field_4 = v18;
            ptr->field_8 = v16;
            if (v19 < v17 || v19 < v5)
                v4 = 1;
            v20 = 0;
            ptr->field_0 = v19;
            if (v4)
            {
                v21 = v18 + 1;
                if (v21 < v18 || v21 < 1)
                    v20 = 1;
                ptr->field_4 = v21;
                if (v20)
                    ptr->field_8 = v16 + 1;
            }
            v22 = ptr->field_4 + v6;
            v23 = 0;
            if (v22 < ptr->field_4 || v22 < v6)
                v23 = 1;
            ptr->field_4 = v22;
            if (v23)
                ptr->field_8 = ptr->field_8 + 1;
            ptr->field_8 = ptr->field_8 + v7;
            v4 = 0;
            v24 = v19 * 2;
            v25 = v22 * 2 | v19 >> 31;
            v26 = ptr->field_8 * 2 | v22 >> 31;
            ptr->field_0 = v24;
            ptr->field_4 = v25;
            ptr->field_8 = v26;
            v27 = *(iter);
            v28 = v24 + v27;
            v5 = v27;
            if (v28 < v24 || v28 < v5)
                v4 = 1;
            ptr->field_0 = v28;
            if (v4)
            {
                v29 = v25 + 1;
                v30 = 0;
                if (v29 < v25 || v29 < 1)
                    v30 = 1;
                ptr->field_4 = v29;
                if (v30)
                    ptr->field_8 = v26 + 1;
            }
            i -= 1;
            iter += 1;
        } while (i > 0);
    }
    for (; !ptr->field_8; ptr->field_0 = v32)
    {
        v31 = ptr->field_4;
        ptr->field_8 = v31 >> 16;
        v32 = ptr->field_0 * 0x10000;
        node += 0xfff0;
        ptr->field_4 = v31 * 0x10000 | ptr->field_0 >> 16;
    }
    if (!(0x8000 & ptr->field_8))
    {
        do
        {
            v33 = ptr->field_0;
            v34 = ptr->field_4;
            node += 0xffff;
            ptr->field_0 = v33 * 2;
            v35 = ptr->field_8 * 2 | v34 >> 31;
            ptr->field_4 = v34 * 2 | v33 >> 31;
            ptr->field_8 = v35;
        } while (!((unsigned short)v35 & 0x8000));
    }
    *((unsigned short *)((char *)&ptr->field_8 + 2)) = node;
    sub_10351225();
    return;
}
```

## `sub_103677fd` `0x103677fd`

_31 bytes. refs "CONOUT$"_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b120;
extern unsigned int g_1038f540;

int sub_103677fd(void)
{
    g_1038f540 = g_1038b120("CONOUT$", 0x40000000, 3, 0, 3, 0, 0);
    return g_1038f540;
}
```

## `sub_1036781c` `0x1036781c`

_45 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b128;
extern unsigned int g_1038f53c;
extern unsigned int g_1038f540;

unsigned int sub_1036781c(void)
{
    unsigned int v2;  // esi
    unsigned int v3;  // eax
    unsigned int v0;  // [bp-0x4]

    v0 = v2;
    if (g_1038f540 != 4294967295 && g_1038f540 != 4294967294)
        g_1038b128(g_1038f540);
    v3 = g_1038f53c;
    if (g_1038f53c != 4294967295 && g_1038f53c != 4294967294)
        v3 = g_1038b128(g_1038f53c);
    return v3;
}
```

## `sub_10367849` `0x10367849`

_68 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038f55c;
extern unsigned int g_103a1590;
extern unsigned int g_103a4cc8;

void sub_10367849(unsigned int a0)
{
    unsigned int v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x100000]
    char v2;  // [bp+0x10000c], Other Possible Types: unsigned int

    sub_1035b0cc(&g_103a1590, 8);
    if (!g_103a4cc8)
    {
        sub_1035b111(&g_103a1590, 8, v0, a0);
        return;
    }
    if ((v2 & 64) && g_1038f55c)
    {
        v1 = 0;
        v1 = 4294967294;
        sub_1035b111(&g_103a1590, 8, v0, a0);
        return;
    }
    v2 = *((int *)&v2) & 4294967231;
    sub_1035b111(&g_103a1590, 8, v0, a0);
    return;
}
```

## `sub_10367876` `0x10367876`

_28 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

unsigned int sub_10367876(void)
{
    struct_0 **v1;  // [bp+0xffff0]

    if (*(v1)->field_0 == 3221225477)
    {
        return 1;
    }
    else if (*(v1)->field_0 != 3221225501)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
```

## `sub_10367892` `0x10367892`

_18 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038f55c;

void sub_10367892(void)
{
    unsigned int v1;  // [bp+0x10000c]

    g_1038f55c = 0;
    v1 &= 4294967231;
}
```

## `sub_103678bb` `0x103678bb`

_44 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
    unsigned int field_c;
} struct_0;

unsigned int sub_103678bb(struct_0 *ptr)
{
    unsigned int v1;  // eax
    unsigned int v0;  // [bp-0x8]

    v1 = ptr->field_c;
    if (!((char)v1 & 131))
    {
        return v1;
    }
    else if (((char)v1 & 8))
    {
        v0 = ptr->field_8;
        sub_1035345e();
        ptr->field_c = ptr->field_c & 4294966263;
        memset(ptr, 0, 12);
        return 0;
    }
    else
    {
        return v1;
    }
}
```

## `sub_103678e7` `0x103678e7`

_609 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
    char padding_8[12];
    unsigned int field_14;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern struct_1 *g_1038b040;
extern struct_1 *g_1038b07c;
extern struct_1 *g_1038b104;
extern struct_1 *g_1038b228;
extern struct_1 *g_1038b22c;
extern unsigned int g_1038e180;
extern char g_1039487c;
extern unsigned int g_103a3ac0;

int sub_103678e7(struct_0 **a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned short *a4, int a5, char *a6, unsigned int a7, unsigned int a8)
{
    unsigned int v17;  // ebx
    unsigned int v18;  // esi
    unsigned int v27;  // edi
    unsigned int v28;  // eax
    unsigned int *iter;  // eax
    unsigned int v30;  // esi
    unsigned int v31;  // eax
    unsigned int *node;  // eax
    unsigned int v33;  // eax
    unsigned int *v19;  // ebx
    unsigned int v20;  // edi
    unsigned short *v21;  // eax
    int v22;  // ecx
    unsigned short *v23;  // eax
    int v24;  // ecx
    unsigned short *v25;  // eax
    unsigned int v26;  // eax
    unsigned int v0;  // [bp-0xbc]
    unsigned int v1;  // [bp-0xb8]
    unsigned int v2;  // [bp-0xb4]
    char *v3;  // [bp-0xb0], Other Possible Types: unsigned int
    unsigned int v4;  // [bp-0xac]
    unsigned int v5;  // [bp-0x94]
    unsigned int v6;  // [bp-0x90]
    unsigned int v7;  // [bp-0x5c]
    unsigned int v8;  // [bp-0x58]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int *v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]
    char v16;  // [bp-0x4]

    v15 = g_1038e180 ^ &v16;
    v11 = v17;
    v10 = v18;
    v19 = NULL;
    v9 = v20;
    if (!g_103a3ac0)
    {
        if (g_1038b22c(0, 0x100, &g_1039487c, 1, 0, 0))
        {
            g_103a3ac0 = 1;
        }
        else if (g_1038b07c() == 120)
        {
            g_103a3ac0 = 2;
        }
    }
    if (a5 > 0)
    {
        v21 = a4;
        v22 = a5;
        do
        {
            v23 = v21;
            v24 = v22 - 1;
            if (!*(v23))
                goto LABEL_1036795c;
        } while ((v25 = v23 + 2, v21 = v23 + 2, v22 = v24, v22));
        v24 = -1;
LABEL_1036795c:
        a5 += 4294967295 - v24;
    }
    if (g_103a3ac0 == 1)
    {
        g_1038b22c(a2, a3, a4, a5, a6, a7);
    }
    else if (g_103a3ac0 == 2 || !g_103a3ac0)
    {
        v13 = 0;
        if (!a2)
            a2 = *(a0)->field_14;
        if (!a8)
            a8 = *(a0)->field_4;
        v26 = sub_1035fd30(a2);
        if (a8 != v26 && v26 != 4294967295)
            a8 = v26;
        v8 = a8;
        v27 = g_1038b040(a8, 0, a4, a5, 0, 0, 0, 0);
        v12 = v27;
        if (!v27)
            goto LABEL_103679e2;
        if (v27 > 0 && !((v7 = 0xffffffe0, 0xffffffe0 / v27 < 1)))
        {
            v28 = v27 + 8;
            if (v28 <= 0x400)
            {
                sub_1035de90();
                iter = &v8;
                if (!&v8)
                    goto LABEL_10367a28;
                v8 = 0xcccc;
                goto LABEL_10367a25;
            }
            else
            {
                iter = sub_10355a15(v28);
                if (iter)
                {
                    *(iter) = 0xdddd;
LABEL_10367a25:
                    iter += 2;
                }
            }
LABEL_10367a28:
            v14 = iter;
        }
        else
        {
            v14 = NULL;
        }
        if (!v14)
            goto LABEL_103679e2;
        if (g_1038b040(a8, 0, a4, a5, v14, v27, 0, 0))
        {
            v6 = a2;
            v30 = g_1038b228(a2, a3, v14, v27, 0, 0);
            if (v30)
            {
                if (v30 > 0)
                {
                    v5 = 0xffffffe0;
                    if (0xffffffe0 / v30 >= 1)
                    {
                        v31 = v30 + 8;
                        if (v31 <= 0x400)
                        {
                            sub_1035de90();
                            node = &v6;
                            if (!&v6)
                                goto LABEL_10367aac;
                            v6 = 0xcccc;
                            goto LABEL_10367aa9;
                        }
                        else
                        {
                            node = sub_10355a15(v31);
                            if (node)
                            {
                                *(node) = 0xdddd;
LABEL_10367aa9:
                                node += 2;
                            }
                        }
LABEL_10367aac:
                        v19 = node;
                    }
                }
                if (v19)
                {
                    if (g_1038b228(a2, a3, v14, v12, v19, v30))
                    {
                        if (((unsigned short)a3 & 0x400))
                        {
                            v33 = a7;
                            v13 = v30;
                            if (v33)
                            {
                                if (v33 <= v30)
                                    v30 = v33 - 1;
                                if (sub_1035f222(a6, v33, v19, v30))
                                {
                                    v4 = 0;
                                    v3 = 0;
                                    v2 = 0;
                                    v1 = 0;
                                    v0 = 0;
                                    sub_103534f6();
                                }
                            }
                        }
                        else
                        {
                            if (!a7)
                            {
                                v4 = 0;
                                v3 = 0;
                            }
                            else
                            {
                                v4 = a7;
                                v3 = a6;
                            }
                            v13 = g_1038b104(a8, 1, v19, v30);
                        }
                    }
                    sub_103548d8(v19);
                }
            }
        }
        sub_103548d8(v14);
    }
    else
    {
LABEL_103679e2:
    }
    return sub_10351225();
}
```

## `sub_10367b48` `0x10367b48`

_64 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

int sub_10367b48(unsigned int *a0, unsigned int a1, unsigned int a2, unsigned short *a3, int a4, char *a5, unsigned int a6, unsigned int a7)
{
    unsigned int v3;  // edx
    int v4;  // eax
    struct_0 v0;  // [bp-0x14]
    struct_0 *idx;  // [bp-0xc]
    char v2;  // [bp-0x8]

    sub_103536a7(&v0, a0);
    v4 = sub_103678e7(&v0, v3, a1, a2, a3, a4, a5, a6, a7);
    if (v2)
        idx[8].field_8 = idx[8].field_8 & 4294967293;
    return v4;
}
```

## `sub_10367b88` `0x10367b88`

_905 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    char padding_0[4];
    unsigned int field_4;
    char padding_8[12];
    unsigned int field_14;
} struct_2;

typedef struct struct_5 {
    char field_0;
} struct_5;

typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b07c;
extern struct_0 *g_1038b104;
extern struct_0 *g_1038b174;
extern struct_0 *g_1038b178;
extern struct_0 *g_1038b230;
extern unsigned int g_1038e180;
extern char g_1039487c;
extern unsigned int g_103a3ac4;

int sub_10367b88(struct_2 **a0, char *a1, unsigned int a2, unsigned int a3, int a4, char *a5, int a6, unsigned int a7)
{
    unsigned int v20;  // ebx
    unsigned int v21;  // esi
    char *v30;  // eax
    int v31;  // ecx
    char *v32;  // eax
    int v33;  // ecx
    char v35[2];  // eax
    char v36[2];  // eax
    unsigned int v37;  // eax
    unsigned int *iter;  // eax
    unsigned int v22;  // edi
    unsigned int v39;  // ebx
    unsigned int v40;  // 4101
    unsigned int v41;  // eax
    struct_5 **v42;  // edi
    struct_5 **node;  // eax
    char *v44;  // edi
    char *v45;  // ebx
    unsigned int v46;  // esi
    char *v23;  // ebx
    char *v24;  // eax
    int v25;  // ecx
    char *v26;  // eax
    int v27;  // ecx
    int v29;  // edx
    unsigned int v0;  // [bp-0xa8]
    unsigned int v1;  // [bp-0xa4]
    char *v2;  // [bp-0x9c]
    unsigned int v3;  // [bp-0x78]
    char *v4;  // [bp-0x74], Other Possible Types: unsigned int
    char *v5;  // [bp-0x70]
    unsigned int v6;  // [bp-0x60]
    char *v7;  // [bp-0x58]
    unsigned int v8;  // [bp-0x3c]
    unsigned int v9;  // [bp-0x38]
    unsigned int v10;  // [bp-0x34]
    unsigned int v11;  // [bp-0x30]
    unsigned int v12;  // [bp-0x2c]
    char *v13;  // [bp-0x28]
    unsigned int *v14;  // [bp-0x24]
    char *v15;  // [bp-0x20]
    char v16;  // [bp-0x1c], Other Possible Types: unsigned int
    char v17;  // [bp-0x16]
    unsigned int v18;  // [bp-0x8]
    char v19;  // [bp-0x4]

    v18 = g_1038e180 ^ &v19;
    v10 = v20;
    v9 = v21;
    v8 = v22;
    v23 = a1;
    v13 = v23;
    v15 = a5;
    if (!g_103a3ac4)
    {
        if (g_1038b174(0, 0, &g_1039487c, 1, &g_1039487c, 1))
        {
            g_103a3ac4 = 1;
        }
        else if (g_1038b07c() == 120)
        {
            g_103a3ac4 = 2;
        }
    }
    if (a4 > 0)
    {
        v24 = v23;
        v25 = a4;
        do
        {
            v26 = v24;
            v27 = v25 - 1;
            if (!*(v26))
                goto LABEL_10367c02;
        } while ((v24 = v26 + 1, v25 = v27, v25));
        v27 = -1;
LABEL_10367c02:
        a4 += 4294967295 - v27;
        goto LABEL_10367c0a;
    }
    if (a4 >= -1)
    {
LABEL_10367c0a:
        v29 = a6;
        if (v29 > 0)
        {
            v30 = v15;
            v31 = v29;
            do
            {
                v32 = v30;
                v33 = v31 - 1;
                if (!*(v32))
                    goto LABEL_10367c24;
            } while ((v30 = v32 + 1, v31 = v33, v31));
            v33 = -1;
LABEL_10367c24:
            v29 += 4294967295 - v33;
            a6 = v29;
            goto LABEL_10367c42;
        }
        if (v29 >= -1)
        {
LABEL_10367c42:
            if (!(g_103a3ac4 != 2 && g_103a3ac4))
            {
                v44 = NULL;
                v45 = NULL;
                if (!a2)
                    a2 = *(a0)->field_14;
                if (!a7)
                    a7 = *(a0)->field_4;
                v46 = sub_1035fd30(a2);
                if (v46 != -1)
                {
                    if (v46 != a7)
                    {
                        v45 = sub_1035fd77(a7, v46, v13, &a4, 0, 0);
                        if (v45)
                        {
                            v44 = sub_1035fd77(a7, v46, v15, &a6, 0, 0);
                            if (!v44)
                            {
                                v7 = v45;
                                sub_1035345e();
                            }
                            else
                            {
                                v13 = v45;
                                v15 = v44;
                                goto LABEL_10367ed1;
                            }
                        }
                    }
                    else
                    {
LABEL_10367ed1:
                        g_1038b178(a2, a3, v13, a4, v15, a6);
                        if (!v45)
                            return sub_10351225();
                        v5 = v45;
                        sub_1035345e();
                        v4 = v44;
                        sub_1035345e();
                        return sub_10351225();
                    }
                }
            }
            else if (g_103a3ac4 == 1)
            {
                v12 = 0;
                if (!a7)
                    a7 = *(a0)->field_4;
                if (!a4 || !v29)
                {
                    if (a4 == v29)
                    {
LABEL_10367c82:
                        v6 = 2;
                        return sub_10351225();
                    }
                    if (v29 > 1)
                        return sub_10351225();
                    if (a4 > 1)
                    {
                        v6 = 3;
                        return sub_10351225();
                    }
                    else if (g_1038b230(a7, &v16))
                    {
                        if (a4 > 0)
                        {
                            if (v16 < 2)
                            {
                                v6 = 3;
                                return sub_10351225();
                            }
                            v35 = &v17;
                            if (*(&v17))
                            {
                                do
                                {
                                    if (!v35[1])
                                    {
                                        v6 = 3;
                                        return sub_10351225();
                                    }
                                    if (*(v23) >= v35[0] && *(v23) <= v35[1])
                                        goto LABEL_10367c82;
                                } while ((v35 += 2, v35[0]));
                            }
                        }
                        else
                        {
                            if (a6 <= 0)
                                goto LABEL_10367d17;
                            if (v16 < 2)
                                return sub_10351225();
                            v36 = &v17;
                            if (!*(&v17))
                                return sub_10351225();
                            while (true)
                            {
                                if (!v36[1])
                                    return sub_10351225();
                                if (*(v15) >= v36[0] && *(v15) <= v36[1])
                                    break;
                                v36 += 1;
                                if (!v36[0])
                                    return sub_10351225();
                            }
                            goto LABEL_10367c82;
                        }
                    }
                }
                else
                {
LABEL_10367d17:
                    v4 = a7;
                    v11 = g_1038b104(a7, 9, v23, a4, 0, 0);
                    if (v11)
                    {
                        if (v11 > 0 && !((v3 = 0xffffffe0, 0xffffffe0 / v11 < 2)))
                        {
                            v37 = v11 * 2 + 8;
                            if (v37 <= 0x400)
                            {
                                sub_1035de90();
                                iter = &v4;
                                if (!&v4)
                                    goto LABEL_10367d7b;
                                v4 = 0xcccc;
                                goto LABEL_10367d78;
                            }
                            else
                            {
                                iter = sub_10355a15(v37);
                                if (iter)
                                {
                                    *(iter) = 0xdddd;
LABEL_10367d78:
                                    iter += 2;
                                }
                            }
LABEL_10367d7b:
                            v14 = iter;
                        }
                        else
                        {
                            v14 = NULL;
                        }
                        if (v14)
                        {
                            if (g_1038b104(a7, 1, v13, a4, v14, v11))
                            {
                                v2 = v15;
                                v1 = a7;
                                v39 = g_1038b104(a7, 9, v15, a6, 0, 0);
                                if (v39)
                                {
                                    v40 = _ccall(14, 15, v39, 0, 0);
                                    if (!((char)v40) && !((v0 = 0xffffffe0, 0xffffffe0 / v39 < 2)))
                                    {
                                        v41 = v39 * 2 + 8;
                                        if (v41 <= 0x400)
                                        {
                                            sub_1035de90();
                                            if (!&v1)
                                            {
                                                sub_103548d8(v14);
                                                return sub_10351225();
                                            }
                                            v1 = 0xcccc;
                                            v42 = &v2;
                                        }
                                        else
                                        {
                                            node = sub_10355a15(v41);
                                            if (node)
                                            {
                                                *(node) = 0xdddd;
                                                node += 2;
                                            }
                                            v42 = node;
                                        }
                                    }
                                    else
                                    {
                                        v42 = NULL;
                                    }
                                    if (v42)
                                    {
                                        if (g_1038b104(a7, 1, v15, a6, v42, v39))
                                            v12 = g_1038b174(a2, a3, v14, v11, v42, v39);
                                        sub_103548d8(v42);
                                    }
                                }
                            }
                            sub_103548d8(v14);
                            return sub_10351225();
                        }
                    }
                }
            }
        }
    }
    return sub_10351225();
}
```

## `sub_10367f11` `0x10367f11`

_64 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

int sub_10367f11(unsigned int *a0, unsigned int a1, unsigned int a2, char *a3, int a4, char *a5, int a6, unsigned int a7)
{
    int v3;  // eax
    struct_0 v0;  // [bp-0x14]
    struct_0 *idx;  // [bp-0xc]
    char v2;  // [bp-0x8]

    sub_103536a7(&v0, a0);
    v3 = sub_10367b88(&v0, a3, a1, a2, a4, a5, a6, a7);
    if (v2)
        idx[8].field_8 = idx[8].field_8 & 4294967293;
    return v3;
}
```

## `sub_10367f51` `0x10367f51`

_248 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

int sub_10367f51(char *a0, char *a1, int a2, unsigned int *a3)
{
    unsigned int v9;  // esi
    unsigned int v10;  // eax
    unsigned int v11;  // eax
    unsigned int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x2c]
    unsigned int v2;  // [bp-0x28]
    unsigned int v3;  // [bp-0x24]
    unsigned int v4;  // [bp-0x20]
    unsigned int v5;  // [bp-0x1c]
    struct_0 v6;  // [bp-0x14]
    struct_0 *idx;  // [bp-0xc]
    char v8;  // [bp-0x8]

    sub_103536a7(&v6, a3);
    if (!a2)
    {
        if (!v8)
            return 0;
        idx[8].field_8 = idx[8].field_8 & 4294967293;
        return 0;
    }
    else
    {
        if (a0 && a1)
        {
            v5 = v9;
            if (a2 > 2147483647)
            {
                v4 = 0;
                v3 = 0;
                v2 = 0;
                v1 = 0;
                v0 = 0;
                *((unsigned int *)sub_103575e0()) = 22;
                sub_103535f2();
                goto LABEL_10368026;
            }
            if (!*((int *)(v6 + 16)))
            {
                v10 = sub_10363d89(a0, a1, a2, &v6);
                goto LABEL_10368039;
            }
            else
            {
                v11 = sub_10367f11(&v6, *((int *)(v6 + 16)), 4097, a0, a2, a1, a2, *((int *)(v6 + 8)));
                if (!v11)
                {
                    *((unsigned int *)sub_103575e0()) = 22;
LABEL_10368026:
                    if (v8)
                        idx[8].field_8 = idx[8].field_8 & 4294967293;
                    v10 = 2147483647;
                }
                else
                {
                    v10 = v11 - 2;
LABEL_10368039:
                    if (v8)
                        idx[8].field_8 = idx[8].field_8 & 4294967293;
                }
            }
            return v10;
        }
        v5 = 0;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        *((unsigned int *)sub_103575e0()) = 22;
        sub_103535f2();
        if (!v8)
            return 2147483647;
        idx[8].field_8 = idx[8].field_8 & 4294967293;
        return 2147483647;
    }
}
```

## `sub_10368049` `0x10368049`

_77 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    int field_0;
} struct_0;

extern struct_0 *g_103a301c;

int sub_10368049(int a0)
{
    int *v0;  // esi
    int v1;  // edi

    v0 = &g_103a301c->field_0;
    while (true)
    {
        if (!*(v0))
            return -(v0 - g_103a301c >> 2);
        if (!sub_103672c0(a0, *(v0), v1) && (*((char *)(v1 + *(v0))) == 61 || !*((char *)(v1 + *(v0)))))
            break;
        v0 += 1;
    }
    return v0 - g_103a301c >> 2;
}
```

## `sub_10368096` `0x10368096`

_93 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_10368096(void)
{
    unsigned int v4;  // ecx
    int v5;  // eax
    int *v6;  // edi
    int *v7;  // ecx
    unsigned int v9;  // ebx
    unsigned int v10;  // esi
    unsigned int *iter;  // esi
    unsigned int i;  // eax
    int *node;  // ebx
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int *v2;  // [bp-0x8], Other Possible Types: unsigned int

    v2 = v4;
    v5 = 0;
    if (!v6)
        return NULL;
    v7 = v6;
    if (*(v7))
    {
        do
        {
            v5 += 1;
            v7 += 1;
        } while (*(v7));
    }
    v1 = v9;
    v0 = v10;
    iter = sub_103574c2(v5 + 1, 4);
    v2 = iter;
    if (!iter)
        sub_10353c92(9);
    i = *(v6);
    for (node = v6; i; i = *(node))
    {
        *(iter) = sub_1036833f(i);
        iter += 1;
        node += 1;
    }
    *(iter) = 0;
    return v2;
}
```

## `sub_103680f3` `0x103680f3`

_588 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
    char field_1;
} struct_0;

typedef struct struct_2 {
    struct struct_0 *field_0;
    unsigned int field_4;
} struct_2;

typedef struct struct_4 {
    unsigned int field_0;
} struct_4;

extern struct_4 *g_1038b064;
extern struct_4 *g_103a301c;
extern char g_103a3020;
extern struct_4 *g_103a3024;

unsigned int sub_103680f3(struct_0 **a0, unsigned int a1)
{
    unsigned int v13;  // ebx
    unsigned int v14;  // edi
    char v23[2];  // esi
    unsigned int v24;  // edi
    char v25[2];  // eax
    unsigned int v15;  // esi
    unsigned int *v16;  // eax
    unsigned int v17;  // ecx
    unsigned int v18;  // edi
    struct struct_0 *i[2];  // esi
    int v20;  // eax
    unsigned int v21;  // eax
    struct_2 *v22;  // ecx
    unsigned int v0;  // [bp-0x38]
    unsigned int v1;  // [bp-0x34]
    char v2[2];  // [bp-0x30], Other Possible Types: unsigned int
    unsigned int v3;  // [bp-0x2c]
    char v4[2];  // [bp-0x28], Other Possible Types: unsigned int
    unsigned int v5;  // [bp-0x24]
    unsigned int v6;  // [bp-0x20]
    unsigned int v7;  // [bp-0x1c]
    unsigned int *v8;  // [bp-0x18]
    unsigned int v9;  // [bp-0x14]
    char v10[2];  // [bp-0x10]
    unsigned int v11;  // [bp-0xc]
    char v12[2];  // [bp-0x8]

    v7 = v13;
    v6 = v14;
    v9 = 0;
    if (!a0)
    {
        v5 = 0;
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        *((unsigned int *)sub_103575e0()) = 22;
        sub_103535f2();
        return 4294967295;
    }
    v5 = v15;
    v12 = *(a0);
    if (v12 && !((v10 = (char [2])sub_10368449(v12, 61), !v10 || v12 == v10)))
    {
        v16 = &g_103a301c->field_0;
        v11 = !v10[1];
        if (v16 == *((int *)&g_103a3020))
        {
            v16 = sub_10368096();
            g_103a301c = v16;
        }
        if (!v16)
        {
            if (a1 && g_103a3024)
            {
                if (sub_103672d7(v17))
                    goto LABEL_10368181;
            }
            else
            {
                if (!v11)
                {
                    g_103a301c = sub_10357482(4);
                    if (!g_103a301c)
                        return 4294967295;
                    g_103a301c->field_0 = 0;
                    if (!g_103a3024)
                    {
                        g_103a3024 = sub_10357482(4);
                        if (!g_103a3024)
                            return 4294967295;
                        g_103a3024->field_0 = 0;
                    }
                }
                else
                {
                    return 0;
                }
            }
        }
        v8 = &g_103a301c->field_0;
        if (g_103a301c)
        {
            v18 = sub_10368049(v12);
            if (v18 >= NULL && g_103a301c->field_0)
            {
                i = &g_103a301c[v18];
                v4 = i[0];
                sub_1035345e();
                if (!v11)
                {
                    i[0] = v12;
                    *(a0) = NULL;
                    goto LABEL_10368292;
                }
                else
                {
                    for (; i[0]; i = &v8[1 + v18])
                    {
                        i[0] = i[1];
                    }
                    if (v18 < 0x3fffffff && !((v20 = sub_10357555(g_103a301c, v18, 4), !v20)))
                        goto LABEL_1036828d;
                    goto LABEL_10368292;
                }
            }
            else
            {
                if (v11)
                {
                    v4 = v12;
                    sub_1035345e();
                    *(a0) = NULL;
                    return 0;
                }
                if (v18 < NULL)
                    v18 = -(v18);
                v21 = v18 + 2;
                if (v21 >= v18 && v21 < 0x3fffffff && (v20 = sub_10357555(g_103a301c, 4, v21), v20))
                {
                    v22 = v20 + v18 * 4;
                    v22->field_0 = v12;
                    v22->field_4 = 0;
                    *(a0) = NULL;
LABEL_1036828d:
                    g_103a301c = v20;
LABEL_10368292:
                    if (a1)
                    {
                        v23 = v12;
                        v24 = sub_103574c2(sub_10352f20(v23) + 2, 1);
                        if (v24)
                        {
                            if (sub_10359f58(v24, sub_10352f20(v23) + 2, v23))
                            {
                                v4 = 0;
                                v3 = 0;
                                v2 = 0;
                                v1 = 0;
                                v0 = 0;
                                sub_103534f6();
                            }
                            v25 = v24 - (char *)v23 + v10;
                            v25[0] = 0;
                            if (!g_1038b064(v24, ~(-(0 < v11)) & &v25[1]))
                            {
                                v9 = 4294967295;
                                *((unsigned int *)sub_103575e0()) = 42;
                            }
                            v2 = v24;
                            sub_1035345e();
                        }
                    }
                    if (!v11)
                        return v9;
                    v2 = v12;
                    sub_1035345e();
                    *(a0) = NULL;
                    return v9;
                }
            }
        }
    }
    else
    {
LABEL_10368181:
        *((unsigned int *)sub_103575e0()) = 22;
    }
    return 4294967295;
}
```

## `sub_1036833f` `0x1036833f`

_80 bytes. (leaf/helper — see body)_

```c
int sub_1036833f(void* a0)
{
    unsigned int v7;  // esi
    unsigned int v8;  // edi
    unsigned int v9;  // esi
    unsigned int v10;  // edi
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]

    if (!a0)
        return 0;
    v6 = v7;
    v5 = v8;
    v9 = sub_10352f20(a0) + 1;
    v10 = sub_10355a15(v9);
    if (!v10)
    {
        v10 = 0;
    }
    else if (sub_10359f58(v10, v9, a0))
    {
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        sub_103534f6();
    }
    return v10;
}
```

## `sub_1036838f` `0x1036838f`

_186 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    void* field_8;
    char field_c;
} struct_0;

typedef struct struct_1 {
    char padding_0[8];
    unsigned int field_8;
} struct_1;

char [2] sub_1036838f(char *a0, unsigned int a1, unsigned int *a2)
{
    char iter[2];  // eax
    unsigned int v10;  // esi
    unsigned short v11;  // cx
    char v12[2];  // eax
    unsigned int v0;  // [bp-0x2c]
    unsigned int v1;  // [bp-0x28]
    unsigned int v2;  // [bp-0x24]
    unsigned int v3;  // [bp-0x20]
    unsigned int v4;  // [bp-0x1c]
    struct_0 v5;  // [bp-0x14]
    struct_1 *v6;  // [bp-0x10]
    struct_0 *idx;  // [bp-0xc]
    char v8;  // [bp-0x8]

    sub_103536a7(&v5, a2);
    iter = a0;
    if (!iter)
    {
        v4 = 0;
        v3 = 0;
        v2 = 0;
        v1 = 0;
        v0 = 0;
        *((unsigned int *)sub_103575e0()) = 22;
        sub_103535f2();
        if (!v8)
            return NULL;
        idx[8].field_8 = idx[8].field_8 & 4294967293;
        return NULL;
    }
    else
    {
        v4 = v10;
        if (!v6->field_8)
        {
            iter = sub_10352de0(iter, a1);
        }
        else
        {
            while (true)
            {
                v11 = iter[0];
                if (v11)
                {
                    if ((v6[2].padding_0[5 + (char)v11] & 4))
                    {
                        v12 = &iter[1];
                        if (!v12[0])
                        {
LABEL_10368437:
                            if (!v8)
                                return NULL;
                            idx[8].field_8 = idx[8].field_8 & 4294967293;
                            return NULL;
                        }
                        if (a1 == (v11 * 0x100 | v12[0]))
                        {
                            iter = &v12[1];
                            break;
                        }
                        else
                        {
                            iter = &v12[1];
                            continue;
                        }
                    }
                    if (a1 == v11)
                        goto LABEL_10368421;
                    iter = &iter[1];
                }
                else
                {
LABEL_10368421:
                    if (a1 != v11)
                        goto LABEL_10368437;
                    break;
                }
            }
        }
        if (!v8)
            return iter;
        idx[8].field_8 = idx[8].field_8 & 4294967293;
        return iter;
    }
}
```

## `sub_10368449` `0x10368449`

_19 bytes. (leaf/helper — see body)_

```c
char [2] sub_10368449(char *a0, unsigned int a1)
{
    return sub_1036838f(a0, a1, NULL);
}
```

## `sub_10368460` `0x10368460`

_10 bytes. (leaf/helper — see body)_

```c
void sub_10368460(unsigned int *a0)
{
    unsigned int v0;  // [bp-0x4]

    v0 = *(a0);
    sub_10350eb5();
    return;
}
```

## `sub_10368470` `0x10368470`

_209 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b07c;
extern struct_0 *g_1038b170;
extern unsigned int g_103a3ad8;
extern unsigned int g_103a3adc;
extern unsigned int g_103a3ae0;

unsigned int * sub_10368470(unsigned int a0, unsigned int *a1)
{
    unsigned int v1[7];  // eax
    unsigned int v2;  // eax
    unsigned int v3;  // esi
    unsigned int v4;  // eax
    unsigned int idx[7];  // ecx
    unsigned int v6[7];  // ecx
    unsigned int *v0;  // [bp+0x0]

    v1 = a1;
    v2 = g_1038b170((v1[6] < 16 ? (unsigned int [7])&v1[1] : v1[1]));
    if (v2 == 4294967295)
    {
        v4 = g_1038b07c(v3);
        idx = a1;
        idx[1] = g_103a3ad8;
        idx[0] = v4;
        if (v4 != 2 && v4 != 3 && v4 != 123 && v4 != 87 && v4 != 161 && v4 != 53)
        {
            if (v4 == 32)
            {
                idx[0] = g_103a3adc;
                idx[1] = g_103a3ae0;
                *(v0) = 9;
            }
            else
            {
                *(v0) = 0;
            }
            return v0;
        }
        idx[0] = g_103a3adc;
        idx[1] = g_103a3ae0;
        *(v0) = 1;
        return v0;
    }
    else
    {
        v6 = a1;
        v6[0] = g_103a3adc;
        v6[1] = g_103a3ae0;
        a0 = 3;
        if (!((char)v2 & 16))
            a0 = 2;
        *(v0) = a0;
        return v0;
    }
}
```

## `sub_10368550` `0x10368550`

_209 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b07c;
extern struct_0 *g_1038b16c;
extern unsigned int g_103a3ad8;
extern unsigned int g_103a3adc;
extern unsigned int g_103a3ae0;

unsigned int * sub_10368550(unsigned int a0, unsigned int *a1)
{
    unsigned int v1[7];  // eax
    unsigned int v2;  // eax
    unsigned int v3;  // esi
    unsigned int v4;  // eax
    unsigned int idx[7];  // ecx
    unsigned int v6[7];  // ecx
    unsigned int *v0;  // [bp+0x0]

    v1 = a1;
    v2 = g_1038b16c((v1[6] < 8 ? (unsigned int [7])&v1[1] : v1[1]));
    if (v2 == 4294967295)
    {
        v4 = g_1038b07c(v3);
        idx = a1;
        idx[1] = g_103a3ad8;
        idx[0] = v4;
        if (v4 != 2 && v4 != 3 && v4 != 123 && v4 != 87 && v4 != 161 && v4 != 53)
        {
            if (v4 == 32)
            {
                idx[0] = g_103a3adc;
                idx[1] = g_103a3ae0;
                *(v0) = 9;
            }
            else
            {
                *(v0) = 0;
            }
            return v0;
        }
        idx[0] = g_103a3adc;
        idx[1] = g_103a3ae0;
        *(v0) = 1;
        return v0;
    }
    else
    {
        v6 = a1;
        v6[0] = g_103a3adc;
        v6[1] = g_103a3ae0;
        a0 = 3;
        if (!((char)v2 & 16))
            a0 = 2;
        *(v0) = a0;
        return v0;
    }
}
```

