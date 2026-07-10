# elfbot.dll decompiled — loader 0x0040675a..0x0040744d

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_0040675a` `0x0040675a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40675a(void)
{
    sub_40675c();
    return;
}
```

## `sub_0040675c` `0x0040675c`

_12 bytes. (leaf/helper — see body)_

```c
int sub_40675c(void)
{
    int v0;  // [bp-0x4]

    sub_403a10(v0);
    return;
}
```

## `sub_00406768` `0x00406768`

_241 bytes. (leaf/helper — see body)_

```c
int sub_406768(void)
{
    unsigned int v13;  // ebx
    char *v14;  // eax
    char v23[3];  // edx
    char v24;  // al
    char v25[3];  // esi
    char node[3];  // esi
    char v28[3];  // ebx
    char v29[3];  // ecx
    char v30[3];  // ecx
    char v31;  // al
    char v32[3];  // edx
    char *iter;  // edi
    char v33[3];  // ebx
    char v34[3];  // esi
    char *v35;  // edi
    char v36[3];  // ecx
    char v37[3];  // esi
    char *v38;  // edi
    char i[3];  // ecx
    char v41[3];  // ecx
    char *v42;  // edi
    char v16[3];  // ecx
    char v43[3];  // esi
    char v44[3];  // ecx
    char k[3];  // esi
    char iter1[3];  // ecx
    char v47[3];  // edx
    char iter2[3];  // ecx
    char v17[3];  // esi
    char v19[3];  // ecx
    char v20[3];  // edx
    char v21[3];  // edx
    char v22[3];  // ecx
    unsigned int v0;  // [bp-0x80]
    unsigned int v1;  // [bp-0x7c]
    unsigned int v2;  // [bp-0x28]
    char v3[3];  // [bp-0x24]
    char v4;  // [bp-0x1d]
    char v5[3];  // [bp-0x1c]
    unsigned int v6;  // [bp-0x18]
    unsigned int v7;  // [bp-0x14]
    char v8[3];  // [bp-0x10], Other Possible Types: unsigned int
    char *v9;  // [bp-0xc]
    unsigned int v10;  // [bp-0x8]
    unsigned int v12;  // [bp+0xc]

    v1 = v13;
    v6 = 0;
    v0 = 0;
    iter = v14;
    v17 = v16;
    v10 = 0;
    v9 = iter;
    v8 = 0;
    v7 = 0;
    v6 = 0;
    v19 = &v16[v12];
    while (true)
    {
        v22 = v19;
        if (!v21)
        {
            sub_406b5c();
            return;
        }
        while (true)
        {
            v23 = v21;
            if (v17 == v22)
            {
                sub_406b5c();
                return;
            }
            v24 = v17[0];
            v25 = &v17[1];
            v17 = v25;
            if (v17[0] == 37)
            {
                if (v25 == v22)
                {
                    sub_406b5c();
                    return;
                }
                v24 = v25[0];
                node = &v25[1];
                v17 = node;
                if (v25[0] != 37)
                {
                    v28 = &node[2];
                    v5 = v28;
                    v29 = v22;
                    while (true)
                    {
                        v30 = v29;
                        v4 = v24;
                        if (v24 == 45)
                        {
                            if (node == v30)
                            {
                                sub_406b5c();
                                return;
                            }
                            node = &node[1];
                        }
                        if ((char)sub_40684a() != 58)
                            break;
                        v8 = v28;
                        if (node == v16)
                        {
                            sub_406b5c();
                            return;
                        }
                        v24 = node[0];
                        node = &node[1];
                        v29 = v16;
                    }
                }
            }
            *(iter) = v24;
            iter += 1;
            v21 = &v23[1];
            if (v23 == 0x1)
            {
                sub_406b5c();
                return;
            }
        }
        v3 = v28;
        if (v31 == 46)
        {
            if (node == v16)
            {
                sub_406b5c();
                return;
            }
            node = &node[1];
            sub_40684a();
        }
        v2 = 4294967295;
        v17 = node;
        sub_406892(v20, v16);
        v32 = v20;
        v33 = v3 - v16;
        if (v3 < v16)
            v33 = NULL;
        v34 = node;
        v35 = iter;
        v36 = v16;
        if (v4 == 45)
        {
            v32 -= v16;
            v37 = node;
            v38 = iter;
            i = v16;
            if (v32 < i)
            {
                v32 = NULL;
                v37 = node;
                v38 = iter;
                i = v16 + v32;
            }
            for (; i; i = v41)
            {
                v41 = &i[1];
                *(v38) = v37[0];
                v42 = v38 + 1;
                v43 = &v37[1];
                v34 = v43;
                v35 = v42;
                v36 = v41;
                v37 = v43;
                v38 = v42;
            }
        }
        v44 = v36;
        iter = v35;
        k = v34;
        iter1 = v33;
        v47 = v32 - iter1;
        if (v32 < iter1)
        {
            iter1 += v47;
            v47 = NULL;
        }
        for (; iter1; iter += 1)
        {
            iter1 = &iter1[1];
            *(iter) = 32;
        }
        iter2 = v44;
        v21 = v47 - iter2;
        if (v47 < iter2)
        {
            iter2 += v21;
            v21 = NULL;
        }
        for (; iter2; k = &k[1])
        {
            iter2 = &iter2[1];
            *(iter) = k[0];
            iter += 1;
        }
        if (v7)
            sub_40675c(v21);
        v19 = v16;
    }
}
```

## `sub_0040684a` `0x0040684a`

_72 bytes. (leaf/helper — see body)_

```c
int sub_40684a(void)
{
    char v4;  // al
    char v5;  // al
    char *iter;  // esi
    char *v7;  // ecx
    unsigned int v8;  // eax
    unsigned int v1;  // [bp+0xffff8]
    unsigned int v2;  // [bp+0x10000c]

    if (v4 != 42)
    {
        while (true)
        {
            if (v5 < 48)
                return;
            if (v5 > 57)
                return;
            if (iter == v7)
                break;
            v5 = *(iter);
            iter += 1;
        }
    }
    else
    {
        v8 = v1;
        if (v8 <= v2)
            v1 += 1;
        if (iter != v7)
            return;
    }
}
```

## `sub_00406892` `0x00406892`

_127 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_4068b9[4];

int sub_406892(void)
{
    unsigned int v6[2];  // eax
    unsigned int v7;  // ebx
    char v8;  // cl
    unsigned int v9;  // 4098
    void* v10;  // esi
    unsigned int v1;  // [bp+0xfffd4]
    unsigned int v2;  // [bp+0xfffd8]
    unsigned int v3;  // [bp+0xffff8]
    unsigned int v4;  // [bp+0x10000c]
    unsigned int v5;  // [bp+0x100010]

    if (v3 <= v4)
    {
        v3 += 1;
        goto g_4068b9[*((char *)(v5 + v3 * 8 + 4))];
    }
    else
    {
        while (true)
        {
            sub_406b5c();
            v6 = sub_4066f0();
            v7 = /* unsupported instruction */ - 48;
            v1 = v6[0];
            v2 = v6[1];
            if (v8 == 0x44)
                break;
            if (v8 == 0x55)
            {
                sub_406955();
                return;
            }
        }
        if ((v2 & 0x80000000))
        {
            v9 = v1;
            v1 = -(v1);
            v2 += 0 < v9;
            v2 = -(v2);
            sub_406955();
            *((char *)&v10[1]) = 45;
        }
        else
        {
            sub_406955();
        }
        return;
    }
}
```

## `sub_00406955` `0x00406955`

_101 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_0;
extern unsigned int g_4;

unsigned int sub_406955(void)
{
    int v4;  // ecx
    void* iter;  // esi
    unsigned int v13;  // ecx
    unsigned int i;  // edx
    unsigned int v15;  // eax
    int v6;  // ebx
    int v7;  // ecx
    int v8;  // ecx
    char v9;  // dl
    char v10;  // dl
    unsigned int v11;  // edx
    unsigned int v12;  // eax
    char v1;  // [bp-0x52]
    unsigned int v2;  // [bp-0x24]

    v4 = 10;
    iter = &v1 + 1;
    do
    {
        v7 = v4;
        v8 = v7;
        v9 = sub_4045fc(v7, 0, v7, v6);
        v10 = v9 + 48;
        if (v9 + 48 >= 58)
            v10 += 7;
        iter -= 1;
        *((char *)iter) = v10;
        v6 = 0;
        g_0 = sub_404534(v8, 0, v8, 0);
        g_4 = v11;
        v12 = g_0 | v11;
        v4 = v8;
    } while (g_0 || v11);
    v13 = &v1 + 1 - iter;
    if (v2 > 16)
        return v12;
    i = v2 - v13;
    if (v2 <= v13)
        return v12;
    v15 = _INSERT(v12, 0, 48);
    do
    {
        iter -= 1;
        *((char *)iter) = v15;
        i -= 1;
    } while (i != 1);
    return v15;
}
```

## `sub_004069ba` `0x004069ba`

_44 bytes. (leaf/helper — see body)_

```c
int sub_4069ba(void)
{
    char v1;  // cl
    int v2;  // eax
    void* v3;  // esi

    if (v1 == 0x44)
    {
        if (v2 < 0)
        {
            sub_4069e6();
            *((char *)&v3[1]) = 45;
        }
        else
        {
            sub_4069e6();
        }
        return;
    }
    else if (v1 != 0x55)
    {
        if (v1 != 88)
            goto LABEL_0x4068fd;
    }
    else
    {
        sub_4069e6();
        return;
    }
}
```

## `sub_004069e6` `0x004069e6`

_59 bytes. (leaf/helper — see body)_

```c
int sub_4069e6(void)
{
    void* iter;  // esi
    unsigned int v5;  // eax
    unsigned int v6;  // eax
    char v7;  // dl
    char v8;  // dl
    unsigned int v9;  // ecx
    unsigned int i;  // edx
    char v1;  // [bp-0x63]
    unsigned int v2;  // [bp-0x24]

    iter = &v1 + 2;
    do
    {
        v6 = v5 / 10;
        v7 = v5 % 10;
        v8 = v7 + 48;
        if (v7 + 48 >= 58)
            v8 += 7;
    } while ((iter -= 1, *((char *)iter) = v8, v5 = v6, v5));
    v9 = &v1 + 2 - iter;
    if (v2 > 16)
        return;
    i = v2 - v9;
    if (v2 <= v9)
        return;
    do
    {
        iter -= 1;
        *((char *)iter) = 48;
        i -= 1;
    } while (i != 1);
    return;
}
```

## `sub_00406a21` `0x00406a21`

_15 bytes. (leaf/helper — see body)_

```c
void sub_406a21(char a0)
{
    if (a0 != 83)
        goto LABEL_0x4068fd;
    return;
}
```

## `sub_00406a30` `0x00406a30`

_50 bytes. (leaf/helper — see body)_

```c
int sub_406a30(void)
{
    char v3;  // cl
    unsigned short *v4;  // eax
    void* v2;  // [bp+0xffff4]

    if (v3 != 83)
        goto LABEL_0x4068fd;
    if (*(v4) <= 1)
        return;
    sub_406748();
    if (v2)
        return;
    return;
}
```

## `sub_00406a51` `0x00406a51`

_17 bytes. (leaf/helper — see body)_

```c
int sub_406a51(void)
{
    char v1;  // cl

    if (v1 != 83)
        goto LABEL_0x4068fd;
}
```

## `sub_00406a62` `0x00406a62`

_24 bytes. (leaf/helper — see body)_

```c
int sub_406a62(void)
{
    char v1;  // cl

    if (v1 != 83)
        goto LABEL_0x4068fd;
    sub_406a7f();
    return;
}
```

## `sub_00406a69` `0x00406a69`

_5 bytes. (leaf/helper — see body)_

```c
void sub_406a69(void)
{
}
```

## `sub_00406a7f` `0x00406a7f`

_14 bytes. (leaf/helper — see body)_

```c
int sub_406a7f(void)
{
    unsigned int *v2;  // esi
    unsigned int v0;  // [bp-0x4]

    v2(v0);
}
```

## `sub_00406a8d` `0x00406a8d`

_11 bytes. (leaf/helper — see body)_

```c
int sub_406a8d(void)
{
    char v1;  // cl

    if (v1 != 83)
        goto LABEL_0x4068fd;
}
```

## `sub_00406aa9` `0x00406aa9`

_32 bytes. (leaf/helper — see body)_

```c
int sub_406aa9(void)
{
    char v3;  // cl
    char *v4;  // edi
    unsigned int v5;  // ecx
    char *v0;  // [bp-0x4]
    unsigned int v2;  // [bp+0xfffe0]

    if (v3 != 83)
        goto LABEL_0x4068fd;
    v0 = v4;
    v5 = v2;
    if (!v2)
        return;
    do
    {
        if (!v5)
            break;
    } while (*(v4));
    return;
}
```

## `sub_00406ac9` `0x00406ac9`

_26 bytes. (leaf/helper — see body)_

```c
void sub_406ac9(char a0)
{
    unsigned int v1;  // [bp+0xfffe0]

    if (a0 != 80)
        goto LABEL_0x4068fd;
    v1 = 8;
}
```

## `sub_00406ae3` `0x00406ae3`

_88 bytes. (leaf/helper — see body)_

```c
int sub_406ae3(void)
{
    int v3;  // ebx
    char v4;  // cl
    int v5;  // eax
    int v1;  // [bp+0xfffe0]

    v3 = _INSERT(_INSERT(0, 1, 1), 0, 0);
    if (v4 != 71)
    {
        v3 = _INSERT(v3, 0, 1);
        if (v4 != 69)
        {
            if (v4 != 70)
            {
                if (v4 != 78)
                {
                    if (v4 == 77)
                        goto LABEL_0x406b10;
                    else
                        goto LABEL_0x4068fd;
                    sub_406b12();
                }
                else
                {
                    sub_406b12();
                }
                return;
            }
            else
            {
                sub_406b12();
                return;
            }
        }
    }
    v5 = v1;
    if (v1 > 18)
        v5 = 15;
    sub_406cd4(3, v5, v3);
    return;
}
```

## `sub_00406ae7` `0x00406ae7`

_2 bytes. (leaf/helper — see body)_

```c
void sub_406ae7(void)
{
}
```

## `sub_00406b12` `0x00406b12`

_31 bytes. (leaf/helper — see body)_

```c
int sub_406b12(char a0)
{
    unsigned int v1;  // [bp+0xfffe0]

    if (v1 <= 18)
        goto LABEL_0x406b43;
    if (a0 != 77)
        goto LABEL_0x406b43;
}
```

## `sub_00406b5c` `0x00406b5c`

_16 bytes. (leaf/helper — see body)_

```c
int sub_406b5c(void)
{
    int v0;  // [bp-0x8]
    int v1;  // [bp-0x4]

    sub_403a10(v0, v1);
    return;
}
```

## `sub_00406b7b` `0x00406b7b`

_1 bytes. (leaf/helper — see body)_

```c
int sub_406b7b(void)
{
    sub_406b7c();
    return;
}
```

## `sub_00406b7c` `0x00406b7c`

_64 bytes. (leaf/helper — see body)_

```c
int sub_406b7c(void)
{
    unsigned int v5;  // ebx
    unsigned int v6;  // esi
    unsigned int v7;  // edi
    unsigned int v8;  // eax
    unsigned int v9;  // ecx
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    int v3;  // [bp+0x4]
    int v4;  // [bp+0x8]

    v2 = v5;
    v1 = v6;
    v0 = v7;
    if (v8 && v9)
    {
        *((char *)(v8 + sub_406768(v3, v4, sub_406630()))) = 0;
        return;
    }
    return;
}
```

## `sub_00406bbc` `0x00406bbc`

_19 bytes. (leaf/helper — see body)_

```c
int sub_406bbc(void)
{
    int v2;  // ecx
    char v0;  // [bp+0x0]

    sub_406bd0(v2, &v0);
    return;
}
```

## `sub_00406bcf` `0x00406bcf`

_1 bytes. (leaf/helper — see body)_

```c
int sub_406bcf(void)
{
    sub_406bd0();
    return;
}
```

## `sub_00406bd0` `0x00406bd0`

_189 bytes. (leaf/helper — see body)_

```c
int sub_406bd0(void)
{
    unsigned int v3;  // eax
    unsigned int v4;  // edx
    unsigned int v5;  // ebx
    int v6;  // esi
    int v7;  // ebx
    int v8;  // ecx
    unsigned int v9;  // eax
    unsigned int i;  // eax
    unsigned int v0;  // [bp-0x1004]
    unsigned int v1;  // [bp-0x8]
    int v2;  // [bp+0x4]

    v0 = v3;
    v1 = v4;
    v5 = 0x1000;
    if (sub_403c80(v6, v7) < 0xc00)
    {
        v9 = sub_406768(v2, v8, sub_403c80());
    }
    else
    {
        v5 = sub_403c80();
        v9 = v5;
    }
    if (v9 < v5 - 1)
    {
        sub_403b00();
        return;
    }
    for (; i >= v5 - 1; i = sub_406768(v2, v8, sub_403c80()))
    {
        v5 *= 2;
        sub_403a10();
        sub_403f60();
    }
    sub_403f60();
    return;
}
```

## `sub_00406c8d` `0x00406c8d`

_3 bytes. (leaf/helper — see body)_

```c
int sub_406c8d(void)
{
    sub_406c90();
    return;
}
```

## `sub_00406c90` `0x00406c90`

_67 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_41e0fc;

int sub_406c90(void)
{
    char v2[2];  // edi
    char v3;  // al
    int v11;  // ecx
    char v12;  // eax
    char iter[2];  // edi
    char v5;  // bl
    char v6;  // edx
    char v7;  // edx
    char v8;  // al
    char v9;  // eax
    char *node;  // ebx
    char v0;  // [bp-0x8]

    v2[0] = v3;
    iter = &v2[1];
    if (!v5)
    {
        v6 = 0;
LABEL_406ca6:
        if (!v3)
            goto LABEL_406cad;
        v8 = *((char *)((void*)&_INSERT(v3, 1, v3) & 0xff + 1));
    }
    else
    {
        v6 = v7;
        if (v7 >= 0)
            goto LABEL_406ca6;
        v8 = 45;
        v6 = -(v6);
    }
    iter[0] = v8;
    iter = &iter[1];
LABEL_406cad:
    v9 = v6;
    v0 = v9;
    node = &v0;
    while (true)
    {
        v12 = v9 / g_41e0fc;
        *(node) = (char)(v9 % g_41e0fc) + 48;
        node += 1;
        v11 -= 1;
        v9 = v12;
        if (v9)
            continue;
        v9 = v12;
        if (v11 <= 0)
            break;
    }
    do
    {
        node += 1;
        iter[0] = *(node);
        iter = &iter[1];
    } while (node != &v0);
    return;
}
```

## `sub_00406cd3` `0x00406cd3`

_1 bytes. (leaf/helper — see body)_

```c
void sub_406cd3(char a0)
{
    sub_406cd4();
    return;
}
```

## `sub_00406cd4` `0x00406cd4`

_226 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_406db0[4];
extern unsigned int g_420770;
extern char g_420774;
extern char g_420775;
extern char g_420776;
extern char g_420777;

int sub_406cd4(void)
{
    unsigned int v15;  // edi
    unsigned int v16;  // esi
    unsigned int v25;  // ecx
    unsigned int v26;  // ebx
    unsigned int v17;  // ebx
    char *v18;  // eax
    int v19;  // eax
    char v20;  // cl
    int v22;  // eax
    unsigned int v23;  // ecx
    char *i;  // esi
    int v0;  // [bp-0x40]
    unsigned int v1;  // [bp-0x3c]
    unsigned int v2;  // [bp-0x38]
    unsigned int v3;  // [bp-0x34]
    unsigned short v4;  // [bp-0x30]
    unsigned int v5;  // [bp-0x18]
    char v6;  // [bp-0x12]
    char v7;  // [bp-0x11]
    unsigned int v8;  // [bp-0x10]
    char v9;  // [bp-0xa]
    char v10;  // [bp-0x9]
    char *iter;  // [bp-0x8]
    int v12;  // [bp+0x4]
    int v13;  // [bp+0x8]
    char v14;  // [bp+0xc]

    v3 = v15;
    v2 = v16;
    v1 = v17;
    iter = v18;
    v10 = g_420777;
    v9 = g_420776;
    v8 = g_420770;
    v7 = g_420774;
    v6 = g_420775;
    v5 = 0;
    v19 = 19;
    if (!v20)
    {
        if (v19 < 2)
            v19 = 2;
        if (v19 > 18)
            v19 = 18;
    }
    v13 = v19;
    v0 = v19;
    v22 = 9999;
    if (v14 >= 2)
        v22 = v12;
    sub_406fac(v22);
    if (v4 - 32767 < 2)
    {
        sub_406dd3();
        i = v23 * 3 + sub_406dc4 + v5;
        for (v25 = 3; v25; i += 1)
        {
            v25 -= 1;
            *(iter) = *(i);
            iter += 1;
        }
        return;
    }
    else
    {
        v26 = v14;
        if ((char)v26 != 1 && ((char)v26 > 4 || v4 > v13))
            v26 = _INSERT(v26, 0, 0);
        (*((int *)((char *)&g_406db0[v26] + v5)) + v5)();
        return;
    }
}
```

## `sub_00406dc4` `0x00406dc4`

_6 bytes. (leaf/helper — see body)_

```c
void sub_406dc4(unsigned int a0)
{
    sub_406dca();
    return;
}
```

## `sub_00406dca` `0x00406dca`

_9 bytes. (leaf/helper — see body)_

```c
char sub_406dca(void)
{
    char *v1;  // esi
    char v2;  // al

    v2 = *(v1);
    if (!*(v1))
        v2 = 48;
    return v2;
}
```

## `sub_00406dd3` `0x00406dd3`

_10 bytes. (leaf/helper — see body)_

```c
char sub_406dd3(void)
{
    char v2;  // al
    char *v3;  // edi
    char v1;  // [bp+0xfffda]

    if (v1)
    {
        v2 = 45;
        *(v3) = 45;
    }
    return v2;
}
```

## `sub_00406ddd` `0x00406ddd`

_110 bytes. (leaf/helper — see body)_

```c
char sub_406ddd(void)
{
    unsigned int v4;  // ecx
    unsigned int v5;  // edx
    void* v22;  // edi
    void* iter;  // edi
    char *v23;  // esi
    char *v13;  // esi
    char *v14;  // esi
    unsigned int v15;  // ecx
    char *v16;  // esi
    unsigned int v17;  // ecx
    char v18;  // al
    unsigned short v19;  // ax
    unsigned int v6;  // ecx
    unsigned short v20;  // ax
    char *v21;  // esi
    void* v7;  // edi
    unsigned int v9;  // ecx
    void* i;  // edi
    void* node;  // edi
    unsigned short v1;  // [bp+0xfffd8]
    char v2;  // [bp+0xfffff]
    unsigned int v3;  // [bp+0x100010]

    sub_406dd3();
    v4 = v1;
    v5 = 0;
    if (v4 <= v3 && v4 >= 4294967293)
    {
        v6 = v4;
        if (v4 > 0)
            goto LABEL_406e10;
        *((char *)v22) = 48;
        v7 = v22 + 1;
        if (!*(v23))
            return 48;
        *((char *)v7) = v2;
        v9 = -(v6);
        for (i = v7 + 1; v9; i += 1)
        {
            v9 -= 1;
            *((char *)i) = 48;
        }
    }
    else
    {
        v6 = 1;
        v5 = 1;
        do
        {
LABEL_406e10:
            v14 = v13;
            v15 = v6;
            v16 = v14 + 1;
            if (!*(v14))
            {
                for (v18 = 48; v15; iter += 1)
                {
                    v15 -= 1;
                    *((char *)iter) = 48;
                }
            }
        } while ((*((char *)iter) = *(v14), iter += 1, v17 = v15 - 1, v6 = v15 - 1, v23 = v16, v15 != 1));
        v13 = v16 + 1;
        v18 = *(v16);
        if (!*(v16))
            goto LABEL_406e30;
        v19 = _INSERT(v18 CONCAT 0, 1, v18);
        v20 = _INSERT(v19, 0, v2);
        *((unsigned short *)iter) = v20;
        node = iter + 2;
    }
    while (true)
    {
        v21 = v13 + 1;
        v18 = *(v13);
        if (!*(v13))
            break;
        *((char *)node) = v18;
        node += 1;
        v13 = v21;
    }
LABEL_406e30:
    if (!v5)
        return v18;
    return sub_406c90();
}
```

## `sub_00406e3b` `0x00406e3b`

_39 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned short field_0;
    char field_2;
} struct_0;

char sub_406e3b(void)
{
    unsigned short v3;  // ax
    unsigned short v4;  // ax
    struct_0 *v5;  // edi
    struct_0 *iter;  // edi
    unsigned int i;  // ecx
    char v1;  // [bp+0xfffff]
    unsigned int v2;  // [bp+0x10000c]

    sub_406dd3();
    v3 = sub_406dca();
    v4 = _INSERT(v3, 1, v1);
    v5->field_0 = v4;
    iter = &v5->field_2;
    do
    {
        *((char *)&iter->field_0) = sub_406dca();
        iter = (char *)&iter->field_0 + 1;
    } while (i != 1);
    if (v2 < 4)
        goto LABEL_0x406e62;
}
```

## `sub_00406e72` `0x00406e72`

_5 bytes. (leaf/helper — see body)_

```c
void sub_406e72(void)
{
    sub_406dd3();
}
```

## `sub_00406e77` `0x00406e77`

_101 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
    char field_1;
} struct_0;

char sub_406e77(unsigned int a0, unsigned int a1, unsigned int a2, char a3)
{
    unsigned int v3;  // ecx
    char v4;  // al
    unsigned int v12;  // cc_op
    unsigned int v13;  // cc_dep1
    unsigned int v14;  // cc_ndep
    unsigned int v15;  // edx
    struct_0 *iter;  // edi
    unsigned int v17;  // ecx
    unsigned int v18;  // edx
    unsigned int v19;  // 4115
    unsigned int v20;  // edx
    unsigned int v21;  // 4103
    struct_0 *v5;  // edi
    unsigned int v23;  // 4109
    char v24;  // al
    unsigned int v6;  // ebx
    unsigned int v7;  // ebx
    unsigned int v8;  // ecx
    unsigned int v9;  // ebx
    unsigned int i;  // edx
    char v11;  // 4102
    unsigned short v0;  // [bp-0x2c]
    char v1;  // [bp-0x6]
    char v2;  // [bp-0x5]

    v3 = v0;
    if (v3 <= 0)
    {
        v4 = 48;
        v5->field_0 = 48;
        iter = &v5->field_1;
    }
    else
    {
        v6 = 0;
        if (a3 != 2)
            v6 = (char)((unsigned short)(v3 - 1) % 3) + 1;
        while (true)
        {
            v7 = v6;
            iter->field_0 = sub_406dca();
            iter = &iter->field_1;
            v3 = v8 - 1;
            if (v8 == 1)
                break;
            v9 = v7 - 1;
            v6 = v9;
            if (v7 != 1 || (v6 = v9, !v1))
                continue;
            iter->field_0 = v1;
            iter = &iter->field_1;
            v6 = _INSERT(v9, 0, 3);
        }
    }
    if (!i)
        return v4;
    v11 = v2;
    v12 = 13;
    v13 = v11;
    v14 = 0;
    if (v11)
    {
        iter->field_0 = v11;
        iter = &iter->field_1;
    }
    if (v3)
    {
        do
        {
            v17 = v3;
            v18 = v15;
            iter->field_0 = 48;
            iter = &iter->field_1;
            v19 = _ccall(v12, v13, 0, v14);
            v20 = v18 - 1;
            if (v18 == 1)
                return 48;
            v21 = _ccall(21, v18 - 1, 0, v19);
            v14 = v21;
            v12 = 18;
            v13 = v17 + 1;
            v23 = _ccall(4, 18, v17 + 1, 0, v21);
            i = v20;
            v3 = v17 + 1;
        } while (!((char)v23));
    }
    do
    {
        iter->field_0 = sub_406dca();
        iter = &iter->field_1;
    } while (i != 1);
    return v24;
}
```

## `sub_00406edc` `0x00406edc`

_84 bytes. (leaf/helper — see body)_

```c
char sub_406edc(void)
{
    char v6;  // bl
    char v7;  // cl
    unsigned int i;  // ecx
    unsigned int v14;  // eax
    char v8;  // bl
    unsigned int v9;  // ebx
    char *v10;  // ebx
    unsigned int v11;  // ecx
    char *iter;  // edi
    unsigned int v0;  // [bp+0x0]
    char v1;  // [bp+0x4]
    char v2;  // [bp+0xfffda]
    unsigned int v3;  // [bp+0xffff0]
    char v4;  // [bp+0xffff6]
    char v5;  // [bp+0xffff7]

    v6 = v5;
    v7 = 3;
    if (v2)
    {
        v6 = v4;
        v7 = 15;
    }
    v8 = v6;
    if (v8 > v7)
        v8 = v7;
    v9 = _INSERT(v8 CONCAT 0, 0, v8 + v7);
    v10 = 4222783 + 5 * v9 + v3;
    v11 = 5;
    do
    {
        i = v11;
        v14 = _INSERT(v14, 0, *(v10));
        if (*(v10) == 64)
            break;
        if ((char)v14 == 36)
        {
            v14 = sub_406f30(v10, i);
        }
        else if ((char)v14 != 42)
        {
            *(iter) = v14;
            iter += 1;
        }
        else
        {
            v14 = sub_406e77(v10, i, v0, v1);
        }
        v10 += 1;
        v11 = i - 1;
    } while (i != 1);
    return v14;
}
```

## `sub_00406f30` `0x00406f30`

_15 bytes. (leaf/helper — see body)_

```c
void sub_406f30(void)
{
    void* node;  // esi
    unsigned int v3;  // ecx
    char *iter;  // edi
    void* v1;  // [bp+0xffff8]

    node = v1;
    if (!node)
        return;
    for (v3 = (int)node[4]; v3; node += 1)
    {
        v3 -= 1;
        *(iter) = *((char *)node);
        iter += 1;
    }
    return;
}
```

## `sub_00406fa9` `0x00406fa9`

_3 bytes. (leaf/helper — see body)_

```c
int sub_406fa9(void)
{
    sub_406fac();
    return;
}
```

## `sub_00406fac` `0x00406fac`

_54 bytes. (leaf/helper — see body)_

```c
int sub_406fac(void)
{
    char v5;  // cl
    int v0;  // [bp-0x30]
    int v1;  // [bp-0x2c]
    int v2;  // [bp-0x28]
    unsigned int v3;  // [bp-0x8]

    v3 = 0;
    if (!v5)
    {
        sub_406fd9(v0, v1, v2);
        return;
    }
    sub_4070fb(v0, v1, v2);
    return;
}
```

## `sub_00406fd9` `0x00406fd9`

_140 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    unsigned int field_4;
    char field_6;
    char padding_7[1];
    unsigned short field_8;
} struct_0;

typedef struct struct_1 {
    unsigned short field_0;
    char field_2;
    char field_3;
} struct_1;

unsigned int sub_406fd9(void)
{
    struct_0 *v3;  // esi
    unsigned int v4;  // eax
    unsigned int v5;  // eax
    int v6;  // ebx
    unsigned short v8;  // ftop
    struct_1 *idx;  // ebx
    unsigned short v1;  // [bp+0xffffa]
    unsigned int v2;  // [bp+0xffffc]

    v4 = _INSERT(0, 0, *((short *)&v3->field_6));
    v5 = v4 & 0x7fff;
    if (((unsigned short)v4 & 32767))
    {
        if (v5 != 0x7fff)
        {
            /* unsupported instruction */
            /* unsupported instruction */
            v2 = ((v5 - 0x3fff) * 19728 >> 16) + 1;
            /* unsupported instruction */
            /* unsupported instruction */
            sub_4029d0(v6);
            /* unsupported instruction */
            /* unsupported instruction */
            /* unsupported instruction */
            /* unsupported instruction */
            /* unsupported instruction */
            v1 = (v8 - 1 & 7) * 0x800 | CmpF((/* unsupported instruction */ ? /* unsupported instruction */ : nan), (/* unsupported instruction */ ? /* unsupported instruction */ : nan)) * 0x100 & 0x4500 & 0x4700;
            if (!(v1 & 0x4100))
                goto LABEL_0x40705a;
            if (!/* unsupported instruction */)
            {
                /* unsupported instruction */
                /* unsupported instruction */
                v2 += 1;
            }
            /* unsupported instruction */
            /* unsupported instruction */
            v2 += 1;
        }
        else if (!(*((short *)((char *)&v3->field_4 + 2)) & 0x8000))
        {
            idx->field_3 = 0;
            idx->field_0 = v5;
            idx->field_2 = (unsigned short)v4 >> 15;
            return v5;
        }
        else if (v3->field_0)
        {
            v5 = 0x8000;
        }
        else if (v3->field_4 != 0x80000000)
        {
            v5 = 0x8000;
        }
        else
        {
            idx->field_3 = 0;
            idx->field_0 = v5;
            idx->field_2 = (unsigned short)v4 >> 15;
            return v5;
        }
    }
    idx->field_3 = 0;
    idx->field_0 = v5;
    *((unsigned int *)&idx->field_2) = 0;
    return v5;
}
```

## `sub_0040705b` `0x0040705b`

_133 bytes. (leaf/helper — see body)_

```c
int sub_40705b(void)
{
    unsigned int v4;  // cc_op
    unsigned int v5;  // cc_dep1
    unsigned short v13;  // ax
    unsigned short v14;  // ax
    int v16;  // edi
    unsigned int v17;  // 4119
    int v18;  // edi
    int v19;  // edi
    unsigned int v6;  // cc_dep2
    unsigned int v7;  // cc_ndep
    unsigned int v8;  // 4101
    void* v9;  // ebx
    void* iter;  // edi
    unsigned int i;  // edx
    unsigned short v12;  // ax
    unsigned int v1;  // [bp+0xffffc]
    unsigned int v2;  // [bp+0x10000c]
    int v3;  // [bp+0x100010]

    v8 = _ccall(4, v4, v5, v6, v7);
    if (!((char)v8))
        goto LABEL_0x407045;
    iter = v9 + 3;
    i = 9;
    do
    {
        v13 = _INSERT(v12, 0, *((char *)(i + /* unsupported instruction */ - 25)) >> 4);
        v14 = _INSERT(v13, 1, *((char *)(i + /* unsupported instruction */ - 25)) & 15);
        v12 = v14 + 0x3030;
        *((unsigned short *)iter) = v12;
        iter += 2;
        i -= 1;
    } while (i != 1);
    *((char *)iter) = 0;
    v16 = v1 + v2;
    v17 = _ccall(8, 3, v1, v2, 0);
    if (!((char)v17))
    {
        if (v16 >= v3)
            v16 = v3;
        if (v16 < 18)
        {
            if (*(3 + (char *)v9 + v16) < 53)
                goto LABEL_4070c6;
            do
            {
                *(3 + (char *)v9 + v16) = 0;
                v18 = v16 - 1;
                if (v16 - 1 < 0)
                {
                    *((unsigned short *)&v9[3]) = 49;
                    v1 += 1;
                    break;
                }
            } while ((*((char *)(3 + (char *)v9 + v18)) = *((char *)(3 + (char *)v9 + v18)) + 1, v16 = v18, *((char *)(3 + (char *)v9 + v16)) > 57));
        }
        else
        {
            v16 = 18;
            do
            {
LABEL_4070c6:
                *(3 + (char *)v9 + v16) = 0;
                v19 = v16 - 1;
                if (v16 - 1 < 0)
                    break;
            } while ((v16 = v19, *((char *)(3 + (char *)v9 + v16)) == 48));
        }
    }
}
```

## `sub_004070eb` `0x004070eb`

_16 bytes. (leaf/helper — see body)_

```c
int sub_4070eb(void)
{
    char *v1;  // eax
    char v2;  // 4097
    char v11;  // 4121
    char v12;  // dl
    unsigned int v13;  // 4152
    unsigned int v14;  // 4153
    char *v15;  // eax
    char *v3;  // eax
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4135
    char v8;  // ch
    void* v9;  // eax
    void* v10;  // eax

    v2 = *(v1);
    v3 = _INSERT(v1, 0, *((char *)&v1) | v2);
    *(v3) = *(v3) + (*((char *)&v1) | v2);
    v7 = _ccall(v4, v5, (unsigned int)v6, v3);
    *((char *)v7) = *((char *)v7) + (*((char *)&v1) | v2);
    v9 = _INSERT(v3, 0, (*((char *)&v1) | v2) + v8);
    v10 = v9 + *((int *)v9);
    v11 = *((char *)v10);
    *((char *)v10) = *((char *)v10) + v12;
    v13 = _ccall(1, (unsigned int)v11, (unsigned int)v12, 0);
    v14 = _ccall((unsigned short)v13 CONCAT *((unsigned short *)(void*)&v10), 39);
    v15 = _INSERT(v10, 0, v14);
    *(v15) = *(v15) + *((char *)&v15);
    sub_4070fb();
    return;
}
```

## `sub_004070fb` `0x004070fb`

_117 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    int field_4;
} struct_0;

typedef struct struct_1 {
    unsigned short field_0;
    char field_2;
    char field_3;
} struct_1;

unsigned int sub_4070fb(void)
{
    struct_0 *v4;  // esi
    unsigned int v5;  // eax
    struct_1 *idx;  // ebx
    int v6;  // edx
    unsigned int v7;  // eax
    int v9;  // edi
    unsigned int v10;  // eax
    int v11;  // edx
    unsigned int v12;  // 4130
    unsigned int v1;  // [bp+0xfffe4]
    int v2;  // [bp+0xfffe8]
    int v3;  // [bp+0x10000c]

    v5 = v4->field_0;
    if (!v5 && !v4->field_4)
    {
        idx->field_3 = 0;
        idx->field_0 = 0;
        idx->field_2 = 0;
        return 0;
    }
    v6 = v4->field_4;
    v7 = v5;
    if (v6 < 0)
    {
        v6 = -(v6) - (0 < v5);
        v7 = -(v5);
    }
    v9 = v3;
    if (v3 < 0)
        v9 = 0;
    if (v9 >= 4)
    {
        v9 = 4;
        do
        {
            v12 = _ccall(2, 12, v6, 232830643 ^ (unsigned int)(char)(v7 < 0xa7640000), (unsigned int)(char)(v7 < 0xa7640000));
            v7 += 0x589c0000;
            v6 = v6 - 232830643 - (v7 < 0xa7640000);
        } while (!((char)v12));
        v7 = v10 - 0x589c0000;
        v6 = v11 + 232830643 + (v10 - 0x589c0000 < v10);
    }
    v1 = v7;
    v2 = v6;
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
    if (4 == v9)
        goto LABEL_0x407162;
    /* unsupported instruction */
    /* unsupported instruction */
}
```

## `sub_00407163` `0x00407163`

_94 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[3];
    char field_3;
} struct_0;

int sub_407163(unsigned int a0, unsigned int a1)
{
    unsigned int v1;  // cc_op
    unsigned int v2;  // cc_dep1
    char v10;  // ah
    char v11;  // al
    unsigned int v12;  // 4129
    char v13;  // al
    unsigned int v15;  // ecx
    unsigned int v3;  // cc_dep2
    unsigned int v4;  // cc_ndep
    unsigned int v5;  // 4101
    struct_0 *v6;  // ebx
    struct_0 *iter;  // edi
    unsigned int v8;  // ecx
    char v9;  // 4109

    v5 = _ccall(4, v1, v2, v3, v4);
    if (!((char)v5))
        goto LABEL_0x40714d;
    iter = &v6->field_3;
    if (!a0)
    {
        v8 = 9;
        while (true)
        {
            v15 = v8;
            v9 = *((char *)(v15 + /* unsupported instruction */ - 25));
            v10 = v9;
            v11 = v9 >> 4;
            v12 = _ccall(4, 25, (unsigned int)v9 >> 4, (unsigned int)v9 >> 3, 0);
            if (!((char)v12) || !((v13 = v10 & 15, !(v10 & 15))))
                break;
            v8 = v15 - 1;
        }
    }
    else
    {
        iter->padding_0[0] = (char)a0 + 48;
        iter = &iter->padding_0[1];
        v15 = 9;
        goto LABEL_407192;
    }
    while (true)
    {
        iter->padding_0[0] = v13 + 48;
        iter = &iter->padding_0[1];
        v15 -= 1;
        if (v15 == 1)
            break;
LABEL_407192:
        v10 = *((char *)(v15 + /* unsupported instruction */ - 25));
        v11 = *((char *)(v15 + /* unsupported instruction */ - 25)) >> 4;
        iter->padding_0[0] = v11 + 48;
        iter = &iter->padding_0[1];
        v13 = v10 & 15;
    }
    do
    {
        iter->padding_0[0] = 0;
        iter = &iter->padding_0[1];
    } while (iter->padding_0[0] == 48);
}
```

## `sub_004071d8` `0x004071d8`

_74 bytes. (leaf/helper — see body)_

```c
int sub_4071d8(void)
{
    unsigned int v2;  // eax
    LPArray v3;  // edx
    char v0;  // [bp-0x104]

    if (sub_40529c(v2, v3, &v0, 0x100) <= 0)
    {
        sub_403a64();
        return;
    }
    sub_403b00();
    return;
}
```

## `sub_00407222` `0x00407222`

_2 bytes. (leaf/helper — see body)_

```c
int sub_407222(void)
{
    sub_407224();
    return;
}
```

## `sub_00407224` `0x00407224`

_40 bytes. (leaf/helper — see body)_

```c
int sub_407224(void)
{
    unsigned int v1;  // eax
    LPArray v2;  // edx

    if (sub_40529c(v1, v2, &/* unsupported instruction */, 2) <= 0)
        return;
    return;
}
```

## `sub_0040724c` `0x0040724c`

_59 bytes. (leaf/helper — see body)_

```c
int sub_40724c(void)
{
    int v3;  // ecx
    int v4;  // edi
    int v5;  // esi
    int v6;  // ebx
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]
    unsigned int *v2;  // [bp+0x4]

    v0 = v3;
    sub_4071d8(v2, v4, v5, v6, v3, &v1);
    if (!*(v2))
        sub_404e44();
    return;
}
```

## `sub_00407287` `0x00407287`

_1 bytes. (leaf/helper — see body)_

```c
void sub_407287(void)
{
    sub_407288();
    return;
}
```

## `sub_00407288` `0x00407288`

_261 bytes. (leaf/helper — see body)_

```c
int sub_407288(void)
{
    unsigned int v15;  // ebx
    unsigned int v16;  // esi
    unsigned long v25;  // 4118
    unsigned int v17;  // edi
    unsigned long v18;  // ldt
    unsigned long v19;  // gdt
    unsigned short v20;  // fs
    unsigned long v21;  // 4167
    unsigned long v22;  // 4176
    unsigned int i;  // ebx
    unsigned int j;  // ebx
    unsigned int v0;  // [bp-0x6c]
    unsigned int v1;  // [bp-0x34]
    unsigned int v2;  // [bp-0x30]
    char *v3;  // [bp-0x2c]
    unsigned int v4;  // [bp-0x28]
    unsigned int v5;  // [bp-0x24]
    unsigned int v6;  // [bp-0x20]
    unsigned int v7;  // [bp-0x1c]
    unsigned int v8;  // [bp-0x18]
    unsigned int v9;  // [bp-0x14]
    unsigned int v10;  // [bp-0x10]
    unsigned int v11;  // [bp-0xc]
    unsigned int v12;  // [bp-0x8]
    char v13;  // [bp-0x4]

    v12 = 0;
    v11 = 0;
    v10 = 0;
    v9 = 0;
    v8 = 0;
    v7 = 0;
    v6 = v15;
    v5 = v16;
    v4 = v17;
    v3 = &v13;
    v2 = sub_40739b;
    v21 = _ccall(v18, v19, (unsigned int)v20, 0);
    v1 = *((int *)v21);
    v22 = _ccall(v18, v19, (unsigned int)v20, 0);
    *((unsigned int **)v22) = &v1;
    v12 = sub_40530c();
    i = 1;
    do
    {
        sub_40724c(&v10, 11, &v13);
        sub_403a64(11, &v13);
        sub_40724c(&v9, 11, &v13);
        sub_403a64(11, &v13);
        i += 1;
    } while (i != 13);
    j = 1;
    do
    {
        v11 = (j + 5) % 7;
        sub_40724c(&v8, 6, &v13);
        sub_403a64(6, &v13);
        sub_40724c(&v7, 6, &v13);
        sub_403a64(6, &v13);
        j += 1;
    } while (j != 8);
    v25 = _ccall(v18, v19, (unsigned int)v20, 0);
    *((unsigned int *)v25) = 6;
    v0 = sub_4073a2;
    return sub_40738d();
}
```

## `sub_0040738d` `0x0040738d`

_14 bytes. (leaf/helper — see body)_

```c
int sub_40738d(void)
{
    return sub_403a34();
}
```

## `sub_0040739b` `0x0040739b`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40739b(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_004073a0` `0x004073a0`

_2 bytes. (leaf/helper — see body)_

```c
int sub_4073a0(void)
{
    return sub_40738d();
}
```

## `sub_004073a2` `0x004073a2`

_7 bytes. (leaf/helper — see body)_

```c
void sub_4073a2(unsigned int a0, unsigned int a1)
{
    return;
}
```

## `sub_004073a9` `0x004073a9`

_61 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_42083c[4];

unsigned int sub_4073a9(void)
{
    unsigned int i;  // ebx

    for (i = 1; g_42083c[i]; i += 1)
    {
        if (i == 7)
            return 0;
    }
    sub_403be8();
    return 1;
}
```

## `sub_004073e6` `0x004073e6`

_95 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420858[4];

int sub_4073e6(unsigned int a0)
{
    unsigned int v7;  // ebx
    unsigned int v8;  // esi
    unsigned long v9;  // ldt
    unsigned long v10;  // gdt
    unsigned short v11;  // fs
    unsigned long v12;  // 4143
    unsigned long v13;  // 4152
    unsigned int idx;  // ebx
    int v15;  // ecx
    unsigned long v16;  // 4118
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v5 = 0;
    v4 = v7;
    v3 = v8;
    v2 = &/* unsupported instruction */;
    v1 = sub_40744d;
    v12 = _ccall(v9, v10, (unsigned int)v11, 0);
    v0 = *((int *)v12);
    v13 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int **)v13) = &v0;
    idx = 1;
    while (true)
    {
        if (g_420858[idx] != 0xffffffff)
        {
            if (idx == 7)
                break;
            idx += 1;
        }
        else
        {
            sub_403be8();
            g_420858[idx] = (unsigned int)sub_4064d0(v15, 0);
            break;
        }
    }
    v16 = _ccall(v9, v10, (unsigned int)v11, 0);
    *((unsigned int *)v16) = v0;
    v2 = sub_407454;
    return sub_407444();
}
```

## `sub_00407444` `0x00407444`

_8 bytes. (leaf/helper — see body)_

```c
int sub_407444(void)
{
    sub_403a10();
}
```

## `sub_0040744d` `0x0040744d`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40744d(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

