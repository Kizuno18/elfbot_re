# elfbot.dll decompiled — loader 0x0040b0b9..0x0040d989

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_0040b0b9` `0x0040b0b9`

_2 bytes. (leaf/helper — see body)_

```c
void sub_40b0b9(void)
{
    sub_40b0b3();
    return;
}
```

## `sub_0040b0bb` `0x0040b0bb`

_2 bytes. (leaf/helper — see body)_

```c
void sub_40b0bb(unsigned int a0)
{
    return;
}
```

## `sub_0040b0bd` `0x0040b0bd`

_40 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_42089c;

int sub_40b0bd(void)
{
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4150
    unsigned long v8;  // 4159
    unsigned long v9;  // 4170
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]

    v2 = &/* unsupported instruction */;
    v1 = sub_40b0e6;
    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v0 = *((int *)v7);
    v8 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int **)v8) = &v0;
    g_42089c = g_42089c - 1;
    v9 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((unsigned int *)v9) = v0;
    v2 = sub_40b0ed;
    return sub_40b0e5(/* unsupported instruction */);
}
```

## `sub_0040b0e5` `0x0040b0e5`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40b0e5(void)
{
    return;
}
```

## `sub_0040b0e6` `0x0040b0e6`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40b0e6(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0040b0eb` `0x0040b0eb`

_2 bytes. (leaf/helper — see body)_

```c
void sub_40b0eb(void)
{
    sub_40b0e5();
    return;
}
```

## `sub_0040b0ed` `0x0040b0ed`

_2 bytes. (leaf/helper — see body)_

```c
void sub_40b0ed(unsigned int a0)
{
    return;
}
```

## `sub_0040b218` `0x0040b218`

_6 bytes. (leaf/helper — see body)_

```c
int sub_40b218(void)
{
    return sub_4030c0;
}
```

## `sub_0040b21e` `0x0040b21e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40b21e(void)
{
    return sub_40b220();
}
```

## `sub_0040b220` `0x0040b220`

_6 bytes. (leaf/helper — see body)_

```c
extern char g_4031ec;

int sub_40b220(void)
{
    return &g_4031ec;
}
```

## `sub_0040b226` `0x0040b226`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40b226(void)
{
    return sub_40b228();
}
```

## `sub_0040b228` `0x0040b228`

_6 bytes. (leaf/helper — see body)_

```c
extern char g_4033ac;

int sub_40b228(void)
{
    return &g_4033ac;
}
```

## `sub_0040b22e` `0x0040b22e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40b22e(void)
{
    return sub_40b230();
}
```

## `sub_0040b230` `0x0040b230`

_6 bytes. (leaf/helper — see body)_

```c
int sub_40b230(void)
{
    return sub_403374;
}
```

## `sub_0040b236` `0x0040b236`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40b236(void)
{
    return sub_40b238();
}
```

## `sub_0040b238` `0x0040b238`

_6 bytes. (leaf/helper — see body)_

```c
int sub_40b238(void)
{
    return sub_403920;
}
```

## `sub_0040b23e` `0x0040b23e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40b23e(unsigned int a0)
{
    return sub_40b240();
}
```

## `sub_0040b240` `0x0040b240`

_281 bytes. (leaf/helper — see body)_

```c
unsigned int sub_40b240(void* idx)
{
    unsigned int v0;  // eax
    unsigned int v1;  // edx

    v0 = _INSERT(0, 0, 1);
    v1 = *((short *)(int)idx[88]);
    if (v1 <= 240)
    {
        if (v1 == 240)
        {
            *((char *)(int)idx[100]) = 1;
            return v0;
        }
        else if (v1 == 0x66)
        {
            *((char *)(int)idx[4]) = 1;
            *((unsigned int *)(int)idx[24]) = 2;
            return v0;
        }
        else if (v1 == 103)
        {
            *((char *)(int)idx[104]) = 1;
            return v0;
        }
    }
    else
    {
        if (v1 == 242)
        {
            *((char *)(int)idx[96]) = 1;
            if (*((char *)(int)idx[8]) == 15)
                return v0;
            if (!(int)idx[20])
                return v0;
            *((unsigned int *)((int)idx[20] + 4)) = 0;
            return v0;
        }
        else if (v1 == 243)
        {
            *((char *)(int)idx[92]) = 1;
            if (*((char *)(int)idx[8]) == 15)
                return v0;
            if (!(int)idx[20])
                return v0;
            *((unsigned int *)((int)idx[20] + 4)) = 0;
            return v0;
        }
    }
    if (((char)*((short *)(int)idx[88]) & 231) == 38)
    {
        *((char *)(int)idx[12]) = ((char)(*((short *)(int)idx[88]) >> 3) & 3) + 1;
        return v0;
    }
    else if (*((short *)(int)idx[88]) - 100 < 2)
    {
        *((char *)(int)idx[12]) = (char)*((short *)(int)idx[88]) - 95;
        return v0;
    }
    else
    {
        return 0;
    }
}
```

## `sub_0040b359` `0x0040b359`

_3 bytes. (leaf/helper — see body)_

```c
int sub_40b359(unsigned int a0)
{
    return sub_40b35c();
}
```

## `sub_0040b35c` `0x0040b35c`

_724 bytes. (leaf/helper — see body)_

```c
char sub_40b35c(void* idx)
{
    void* v0;  // eax
    void* v1;  // edx
    unsigned int v2;  // ecx
    char v3;  // al

    v0 = (int)idx[76];
    v1 = idx - 8;
    *((char *)v0) = *((char *)*((int *)v1));
    *((char *)(int)idx[72]) = 0;
    *((char *)(int)idx[0x44]) = (*((char *)v0) & 192) != 192;
    *((unsigned int *)(int)idx[64]) = *((char *)v0) & 7;
    *((unsigned int *)(int)idx[60]) = *((char *)v0) >> 3 & 7;
    *((unsigned int *)(int)idx[52]) = 0;
    *((unsigned int *)v1) = *((int *)v1) + 1;
    if ((*((char *)v0) & 192) == 64)
    {
        *((unsigned int *)(int)idx[48]) = 1;
    }
    else if ((*((char *)v0) & 192) != 128)
    {
        *((unsigned int *)(int)idx[48]) = 0;
    }
    else if (*((char *)(int)idx[104]))
    {
        *((unsigned int *)(int)idx[48]) = 2;
    }
    else
    {
        *((unsigned int *)(int)idx[48]) = 4;
    }
    if (*((char *)(int)idx[0x44]) && *((char *)(int)idx[104]))
    {
        if (*((int *)(int)idx[64]) >= 0 && *((int *)(int)idx[64]) <= 3)
        {
            *((unsigned int *)(int)idx[56]) = (*((int *)(int)idx[64]) & 1) + 6;
            *((unsigned int *)(int)idx[52]) = 1;
        }
        if (!(*((char *)v0) & 192) && *((int *)(int)idx[64]) == 6)
        {
            *((unsigned int *)(int)idx[48]) = 2;
            *((int *)(int)idx[64]) = -1;
        }
        else
        {
            switch (*((int *)(int)idx[64]))
            {
            case 0: case 1: case 7:
                *((int *)(int)idx[64]) = 3;
                break;
            case 2: case 3: case 6:
                *((int *)(int)idx[64]) = 5;
                break;
            case 4:
                *((int *)(int)idx[64]) = 6;
                break;
            case 5:
                *((int *)(int)idx[64]) = 7;
                break;
            }
        }
    }
    else
    {
        if (*((int *)(int)idx[64]) == 4 && *((char *)(int)idx[0x44]))
        {
            *((char *)(int)idx[72]) = *((char *)*((int *)v1));
            *((unsigned int *)v1) = *((int *)v1) + 1;
            *((unsigned int *)(int)idx[64]) = *((char *)(int)idx[72]) & 7;
            if ((*((char *)(int)idx[72]) & 56) != 32)
            {
                *((unsigned int *)(int)idx[52]) = 1 << ((char)(*((char *)(int)idx[72]) >> 6) & 31);
                *((unsigned int *)(int)idx[56]) = *((char *)(int)idx[72]) >> 3 & 7;
            }
        }
        if (!(*((char *)v0) & 192) && *((int *)(int)idx[64]) == 5)
        {
            *((unsigned int *)(int)idx[48]) = 4;
            *((int *)(int)idx[64]) = -1;
        }
    }
    *((int *)(int)idx[44]) = *((int *)v1);
    v2 = *((int *)(int)idx[48]) - 1;
    if (*((int *)(int)idx[48]) == 1)
    {
        *((int *)(int)idx[40]) = *((char *)*((int *)v1));
        *((unsigned int *)(int)idx[36]) = *((char *)*((int *)v1));
    }
    else if (v2 == 1)
    {
        *((int *)(int)idx[40]) = *((short *)*((int *)v1));
        *((unsigned int *)(int)idx[36]) = *((short *)*((int *)v1));
    }
    else if (v2 == 3)
    {
        *((int *)(int)idx[40]) = *((int *)*((int *)v1));
        *((int *)(int)idx[36]) = *((int *)*((int *)v1));
    }
    else
    {
        *((unsigned int *)(int)idx[40]) = 0;
        *((unsigned int *)(int)idx[36]) = 0;
    }
    *((int *)v1) = *((int *)v1) + *((int *)(int)idx[48]);
    v3 = *((char *)v0);
    *((char *)((int)idx[8] + 4)) = *((char *)v0);
    return v3;
}
```

## `sub_0040b650` `0x0040b650`

_228 bytes. (leaf/helper — see body)_

```c
unsigned int sub_40b650(void* idx)
{
    unsigned int v0;  // eax
    unsigned int v1;  // eax
    unsigned int v2;  // eax
    unsigned short v3;  // dx
    unsigned short v4;  // dx
    unsigned int v5;  // edx
    unsigned int v6;  // edx

    v0 = *((int *)(int)idx[84]) & 0xc00;
    v1 = v0 - 0x400;
    if (v0 == 0x400)
    {
        v2 = 1;
    }
    else if (v1 == 0x400)
    {
        v2 = 2;
    }
    else if (v1 == 0x800)
    {
        v2 = *((int *)(int)idx[24]);
    }
    else
    {
        v2 = 0;
        if (*((short *)(int)idx[88]) != 154)
        {
            v3 = *((short *)(int)idx[88]) - 160;
            v4 = v3 - 4;
            if (v3 < 4)
            {
                v2 = (!*((char *)(int)idx[104]) ? 4 : 2);
            }
            else if (v4 == 36)
            {
                v2 = 3;
            }
            else if (v4 == 70)
            {
                goto LABEL_40b6b6;
            }
        }
        else
        {
LABEL_40b6b6:
            v2 = *((int *)(int)idx[24]) + 2;
        }
    }
    v5 = v2;
    v6 = v5 - 1;
    if (v5 == 1)
    {
        *((int *)(int)idx[28]) = *((char *)(int)idx[8]);
        return v2;
    }
    else if (v6 != 1)
    {
        if (v6 == 3)
            *((int *)(int)idx[28]) = *((int *)(int)idx[8]);
        else
            *((unsigned int *)(int)idx[28]) = 0;
        return v2;
    }
    else
    {
        *((int *)(int)idx[28]) = *((short *)(int)idx[8]);
        return v2;
    }
}
```

## `sub_0040b734` `0x0040b734`

_1239 bytes. (leaf/helper — see body)_

```c
extern char g_40bc0c;

unsigned int sub_40b734(void* idx)
{
    unsigned int v0;  // eax
    unsigned int v1;  // edx
    unsigned int v10;  // cc_dep1
    unsigned int v11;  // cc_dep2
    unsigned int v12;  // 4103
    unsigned int v16;  // edx
    unsigned int v17;  // eax
    unsigned int v18;  // eax
    unsigned int v19;  // eax
    char *v2;  // eax
    unsigned int v23;  // eax
    unsigned int v24;  // eax
    unsigned int v25;  // eax
    unsigned int v27;  // edx
    int *v28;  // eax
    unsigned int v30;  // edx
    char *v32;  // eax
    char *v35;  // eax
    unsigned int v37;  // edx
    char v40;  // al
    char v41;  // al
    char v42;  // al
    char v45;  // al
    char *v48;  // eax
    unsigned int v49;  // eax
    char v7;  // 4111
    unsigned int v8;  // eax
    unsigned int v9;  // cc_op

    v0 = _INSERT((int)idx[84], 0, *((int *)(int)idx[84]) != 0xffff);
    if (*((int *)(int)idx[84]) == 0xffff)
    {
        return v0;
    }
    else if (*((short *)(int)idx[88]) > 0xff)
    {
        v1 = (char)*((short *)(int)idx[88]);
        if (v1 > 115)
        {
            if (v1 <= 195)
            {
                if (v1 != 195)
                {
                    if (v1 <= 178)
                    {
                        if (v1 != 178)
                        {
                            v27 = v1 - 124;
                            if (v27 >= 2)
                            {
                                if (v27 == 50)
                                {
                                    v28 = (int)idx[60];
                                    if (*((int *)(int)idx[60]) != 7 && (*((int *)(int)idx[60]) >= 4 || (v28 = (int *)(int)idx[0x44], !*((char *)(int)idx[0x44]))) && (*((int *)(int)idx[60]) <= 4 || !((v28 = (int *)(int)idx[0x44], !*((char *)(int)idx[0x44])))))
                                        return 0;
                                    return _INSERT(v28, 0, 1);
                                }
                                else
                                {
                                    return v0;
                                }
                            }
                            goto LABEL_40b9c6;
                        }
                    }
                    else
                    {
                        v30 = v1 - 180;
                        if (v30 >= 2)
                            return _INSERT((int)idx[60], 0, *((int *)(int)idx[60]) >= 4);
                    }
                }
            }
            else
            {
                if (v1 > 214)
                {
                    if (v1 != 230)
                        return v0;
LABEL_40ba4d:
                    v35 = (int)idx[4];
                    if (!*((char *)(int)idx[4]))
                    {
                        v35 = (int)idx[96];
                        if (!*((char *)(int)idx[96]))
                        {
                            v35 = (int)idx[92];
                            if (!*((char *)(int)idx[92]))
                                return 0;
                        }
                    }
                    return _INSERT(v35, 0, 1);
                }
                if (v1 == 214)
                    goto LABEL_40ba4d;
                if (v1 != 199)
                {
                    if (v1 != 208)
                        return v0;
LABEL_40b9c6:
                    v32 = (int)idx[4];
                    if (!*((char *)(int)idx[4]))
                    {
                        v32 = (int)idx[96];
                        if (!*((char *)(int)idx[96]))
                            return 0;
                    }
                    return _INSERT(v32, 0, 1);
                }
            }
            return _INSERT((int)idx[0x44], 0, *((char *)(int)idx[0x44]));
        }
        else if (v1 != 115)
        {
            if (v1 <= 32)
            {
                if (v1 != 32)
                {
                    if (v1 <= 13)
                    {
                        if (v1 == 13)
                        {
                            if (!*((char *)(int)idx[0x44]) || *((int *)(int)idx[60]) > 1)
                                return 0;
                            return _INSERT((int)idx[60], 0, 1);
                            return 0;
                        }
                        else if (v1 < 1)
                        {
                            return _INSERT((int)idx[60], 0, *((int *)(int)idx[60]) <= 5);
                        }
                        else if (v1 == 1)
                        {
                            if (*((int *)(int)idx[60]) == 5)
                                return 0;
                            v2 = (int)idx[0x44];
                            if (*((char *)(int)idx[0x44]) || !((v2 = (char *)(int)idx[60], *((int *)(int)idx[60]) <= 3)))
                            {
                                return _INSERT(v2, 0, 1);
                            }
                            return 0;
                        }
                        else
                        {
                            return v0;
                        }
                    }
                    else
                    {
                        if (v1 == 15)
                        {
                            v7 = *((char *)(int)idx[8]);
                            v8 = _INSERT((int)idx[8], 0, v7 - 8);
                            v9 = 4;
                            v10 = v7 - 8;
                            v11 = 183;
                            if (v7 - 8 <= 183)
                            {
                                v8 &= 0xff;
                                v9 = 0;
                                v11 = 0;
                                v10 = (&g_40bc0c)[v8 >> 3] >> ((char)v8 & 7) & 1;
                            }
                            v12 = _ccall(2, v9, v10, v11, 0);
                            return _INSERT(v8, 0, v12);
                        }
                        else if (v1 == 24)
                        {
                            if (!*((char *)(int)idx[0x44]) || *((int *)(int)idx[60]) > 3)
                                return 0;
                            return _INSERT((int)idx[60], 0, 1);
                            return 0;
                        }
                        else
                        {
                            return v0;
                        }
                    }
                }
            }
            else
            {
                if (v1 > 35)
                {
                    v16 = v1 - 108;
                    if (v16 < 2)
                        return _INSERT((int)idx[4], 0, *((char *)(int)idx[4]));
                    if (v16 - 5 < 2)
                    {
                        if (*((char *)(int)idx[0x44]))
                            return 0;
                        v17 = *((int *)(int)idx[60]) - 2;
                        v18 = v17;
                        if (*((int *)(int)idx[60]) == 2 || !((v19 = v17 - 2, v18 = v19, v17 != 2 && (v18 = v19 - 2, v19 != 2))))
                        {
                            return _INSERT(v18, 0, 1);
                        }
                        return 0;
                    }
                    else
                    {
                        return v0;
                    }
                }
                else if (!(v1 != 35 && v1 != 33))
                {
                    return _INSERT((int)idx[0x44], 0, *((char *)(int)idx[0x44]) ^ 1);
                }
                else if (v1 != 0x22)
                {
                    return v0;
                }
            }
            return _INSERT((int)idx[0x44], 0, *((char *)(int)idx[0x44]) ^ 1);
        }
        else
        {
            if (*((char *)(int)idx[0x44]))
                return 0;
            v23 = *((int *)(int)idx[60]) - 2;
            v24 = v23 - 2;
            if (v23 < 2 || !((v25 = v24 - 2, v24 = v25 - 2, v25 >= 2)))
            {
                return _INSERT(v24, 0, 1);
            }
            return 0;
        }
    }
    else
    {
        v37 = (char)*((short *)(int)idx[88]);
        if (v37 <= 217)
        {
            if (v37 != 217)
            {
                if (v37 <= 141)
                {
                    if (v37 != 141 && v37 != 98)
                    {
                        if (v37 == 140)
                            return _INSERT((int)idx[60], 0, *((int *)(int)idx[60]) <= 5);
                        return v0;
                    }
                }
                else
                {
                    if (v37 == 142)
                    {
                        return _INSERT((int)idx[60], 0, *((int *)(int)idx[60]) <= 5);
                    }
                    else if (v37 - 196 >= 2)
                    {
                        return v0;
                    }
                }
                return _INSERT((int)idx[0x44], 0, *((char *)(int)idx[0x44]));
            }
            else
            {
                if (*((char *)(int)idx[0x44]))
                    return _INSERT(v42 - 7 CONCAT 0, 0, 1);
                v40 = *((char *)(int)idx[76]) - -40;
                if (*((char *)(int)idx[76]) + 47 < 7 || !((v41 = v40 - 12, v40 - 10 >= 2 && (v42 = v41 - 4, v41 - 2 >= 2 && v42 != 7))))
                    return 0;
                return _INSERT(v42 - 7 CONCAT 0, 0, 1);
            }
        }
        else
        {
            if (v37 <= 223)
            {
                if (v37 == 223)
                {
                    if (*((char *)(int)idx[0x44]) || *((char *)(int)idx[76]) + 31 >= 7)
                        return _INSERT(*((char *)(int)idx[76]) - -24 CONCAT 0, 0, 1);
                    return 0;
                    return _INSERT(*((char *)(int)idx[76]) - -24 CONCAT 0, 0, 1);
                }
                else if (v37 == 218)
                {
                    if (*((char *)(int)idx[0x44]))
                        return _INSERT(v45 - 8 CONCAT 0, 0, 1);
                    v45 = *((char *)(int)idx[76]) + 24;
                    if (*((char *)(int)idx[76]) == 232 || v45 - 2 < 6)
                        return 0;
                    return _INSERT(v45 - 8 CONCAT 0, 0, 1);
                }
                else if (v37 == 219)
                {
                    if (*((char *)(int)idx[0x44]) || *((char *)(int)idx[76]) + 27 >= 3)
                        return _INSERT(*((char *)(int)idx[76]) - -24 CONCAT 0, 0, 1);
                    return 0;
                    return _INSERT(*((char *)(int)idx[76]) - -24 CONCAT 0, 0, 1);
                }
                else
                {
                    return v0;
                }
            }
            else
            {
                if (v37 == 254)
                {
                    return _INSERT((int)idx[60], 0, *((int *)(int)idx[60]) <= 1);
                }
                else if (v37 == 0xff)
                {
                    if (*((int *)(int)idx[60]) >= 7)
                        return 0;
                    v48 = (int)idx[0x44];
                    if (*((char *)(int)idx[0x44]) || !((v49 = *((int *)(int)idx[60]) - 3, *((int *)(int)idx[60]) == 3 || !((v48 = (char *)(v49 - 2), v49 != 2)))))
                    {
                        return _INSERT(v48, 0, 1);
                    }
                    return 0;
                }
                else
                {
                    return v0;
                }
            }
        }
    }
}
```

## `sub_0040bc24` `0x0040bc24`

_639 bytes. (leaf/helper — see body)_

```c
void* sub_40bc24(void* idx)
{
    unsigned int v1;  // ebx
    void* v2;  // eax
    void* v3;  // eax
    void* v4;  // eax
    char v5;  // al
    unsigned int *v6;  // eax
    void* v7;  // eax
    void* v8;  // eax
    void* v9;  // eax
    unsigned int v0;  // [bp-0x8]

    v0 = v1;
    if ((*((char *)((int)idx[84] + 1)) & 16))
    {
        *((char *)((int)idx[8] + 7)) = 1;
        *((int *)((int)idx[8] + 12)) = (int)idx[8];
        *((int *)((int)idx[8] + 8)) = (int)idx[8] + *((int *)(int)idx[32]) + *((int *)(int)idx[28]);
        *((int *)((int)idx[8] + 20)) = *((int *)(int)idx[32]);
        *((char *)((int)idx[8] + 24)) = *((short *)(int)idx[88]) - 224 >= 4;
        if (*((short *)(int)idx[88]) != 232)
        {
            v3 = (int)idx[8];
            *((char *)&v3[6]) = 1;
            return v3;
        }
        v2 = (int)idx[8];
        *((char *)&v2[5]) = 1;
        return v2;
    }
    else
    {
        if (*((short *)(int)idx[88]) == 0xff && *((int *)(int)idx[60]) - 2 < 4)
        {
            if (*((int *)(int)idx[60]) - 2 < 2)
                *((char *)((int)idx[8] + 5)) = 1;
            else
                *((char *)((int)idx[8] + 6)) = 1;
            if (*((int *)(int)idx[64]) == 0xffffffff && !*((int *)(int)idx[52]) && *((int *)(int)idx[48]) == 4)
            {
                *((int *)((int)idx[8] + 16)) = *((int *)(int)idx[44]);
                *((unsigned int *)((int)idx[8] + 20)) = 4;
                v4 = sub_40ddd8((int)idx[12]);
                *((char *)(int)idx[8]) = *((char *)&v4);
                return v4;
            }
            if (!(char)idx[16])
            {
                return idx;
            }
            else if (!(int)idx[20])
            {
                return idx;
            }
            else if (*((int *)(int)idx[64]) == 0xffffffff)
            {
                return (int)idx[64];
            }
            else if (!*((int *)((int)idx[20] + *((int *)(int)idx[64]) * 4)))
            {
                return *((int *)(int)idx[64]);
            }
            else if (*((int *)(int)idx[52]))
            {
                return (int)idx[52];
            }
            else if (!*((int *)(int)idx[48]))
            {
                if (*((char *)(int)idx[0x44]))
                {
                    *((int *)((int)idx[8] + 16)) = *((int *)((int)idx[20] + *((int *)(int)idx[64]) * 4));
                    v5 = sub_40ddd8((int)idx[12]);
                    *((char *)(int)idx[8]) = v5;
                }
                else
                {
                    v6 = *((int *)((int)idx[20] + *((int *)(int)idx[64]) * 4));
                    *((unsigned int **)((int)idx[8] + 12)) = v6;
                    *((unsigned int *)((int)idx[8] + 8)) = *(v6);
                }
                v7 = (int)idx[8];
                *((unsigned int *)&v7[20]) = 4;
                return v7;
            }
            else
            {
                return (int)idx[48];
            }
        }
        if (*((short *)(int)idx[88]) == 154)
        {
            v8 = (int)idx[8];
            *((char *)&v8[5]) = 1;
            return v8;
        }
        if (*((short *)(int)idx[88]) != 234)
            return v9;
        v9 = (int)idx[8];
        *((char *)&v9[6]) = 1;
        return v9;
    }
}
```

## `sub_0040bea3` `0x0040bea3`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40bea3(unsigned int a0)
{
    sub_40bea4();
    return;
}
```

## `sub_0040bea4` `0x0040bea4`

_1262 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    struct struct_0 *field_0;
    unsigned int field_4;
    unsigned int field_8;
    char padding_c[8];
    unsigned int field_14;
    unsigned int field_18;
    unsigned int field_1c;
} struct_0;

struct_0 * sub_40bea4(void* idx)
{
    unsigned int v0;  // eax
    unsigned int v1;  // eax
    struct_0 *idx1;  // eax
    struct_0 *idx2;  // eax
    struct_0 *v12;  // eax
    unsigned int v13;  // eax
    unsigned int v14;  // eax
    unsigned int v15;  // eax
    struct_0 *v16;  // eax
    struct_0 *j;  // eax
    struct_0 *v18;  // eax
    unsigned int v19;  // eax
    unsigned int v2;  // eax
    struct_0 *v20;  // eax
    struct_0 *v21;  // eax
    struct_0 *v22;  // eax
    unsigned int v23;  // eax
    unsigned int v24;  // eax
    struct_0 *v25;  // eax
    struct_0 *v26;  // eax
    struct_0 *v27;  // eax
    struct_0 *v28;  // eax
    unsigned int v29;  // eax
    struct_0 *v3;  // eax
    struct_0 *v30;  // eax
    struct_0 *v31;  // eax
    unsigned int v32;  // eax
    unsigned int v33;  // eax
    struct_0 *v34;  // eax
    struct_0 *v35;  // eax
    struct_0 *v36;  // eax
    struct_0 *v4;  // eax
    struct_0 *index;  // eax
    unsigned int v6;  // eax
    unsigned int v7;  // eax
    unsigned int v8;  // eax
    struct_0 *v9;  // eax

    v0 = *((int *)(int)idx[84]) & 0xe000;
    if (v0 == 0x8000 || v0 == 0xc000 || v0 == 0xe000)
        *((struct_0 **)(int)idx[20]) = NULL;
    if (!*((char *)(int)idx[0x44]) && (v0 == 0x4000 || v0 == 0xa000 || v0 == 0xc000))
        *((unsigned int *)((int)idx[20] + *((int *)(int)idx[64]) * 4)) = 0;
    if (v0 == 0x2000 || v0 == 0xa000)
        *((unsigned int *)((int)idx[20] + *((int *)(int)idx[60]) * 4)) = 0;
    if (v0 == 0x6000 || v0 == 0xe000)
        *((unsigned int *)((int)idx[20] + (*((short *)(int)idx[88]) & 7) * 4)) = 0;
    if (*((short *)(int)idx[88]) > 0xff)
    {
        v1 = (char)*((short *)(int)idx[88]);
        if (v1 >= 126)
        {
            v6 = v1 - 126;
            v7 = v6 - 2;
            if (v6 >= 2)
            {
                v8 = v7 - 0x22;
                if (v7 != 0x22)
                {
                    if (v8 != 24)
                    {
                        if (v8 != 37)
                            return v8 - 37;
                    }
                    else
                    {
                        if (*((int *)(int)idx[60]) >= 5)
                        {
                            if (!*((char *)(int)idx[0x44]))
                            {
                                idx1 = *((int *)(int)idx[64]);
                                *((unsigned int *)((int)idx[20] + idx1 * 4)) = 0;
                                return idx1;
                            }
                            return (int)idx[0x44];
                        }
                        else
                        {
                            return (int)idx[60];
                        }
                    }
                }
                else
                {
                    idx2 = NULL;
                    do
                    {
                        *((unsigned int *)((int)idx[20] + idx2 * 4)) = 0;
                        idx2 = (char *)&idx2->field_0 + 1;
                    } while (idx2 != 4);
                    return idx2;
                }
            }
            else
            {
                v12 = (int)idx[92];
                if ((char)v12->field_0 || *((char *)(int)idx[0x44]))
                    return v12;
                *((unsigned int *)((int)idx[20] + *((int *)(int)idx[64]) * 4)) = 0;
                return v12;
            }
        }
        else if (v1 < 0x1)
        {
            if (*((int *)(int)idx[60]) > 0x1 || *((char *)(int)idx[0x44]))
                return index;
            index = *((int *)(int)idx[64]);
            *((unsigned int *)((int)idx[20] + index * 4)) = 0;
            return index;
        }
        else if (v1 != 0x1)
        {
            v2 = v1 - 44;
            if (v2 < 2)
            {
                if (!*((char *)(int)idx[96]) && !*((char *)(int)idx[92]))
                    return (int)idx[92];
                v3 = *((int *)(int)idx[60]);
                *((unsigned int *)((int)idx[20] + v3 * 4)) = 0;
                return v3;
            }
            else if (v2 - 5 >= 3)
            {
                return v2 - 8;
            }
        }
        else
        {
            if (*((int *)(int)idx[60]) != 4)
                return v4;
            v4 = (int)idx[0x44];
            if (!(char)v4->field_0)
                *((unsigned int *)((int)idx[20] + *((int *)(int)idx[64]) * 4)) = 0;
            return v4;
        }
        v9 = (int)idx[20];
        v9->field_8 = 0;
        return v9;
    }
    else
    {
        v13 = *((short *)(int)idx[88]);
        if (v13 < 172)
        {
            if (v13 <= 139)
            {
                if (v13 == 139)
                {
                    if (*((char *)(int)idx[0x44]))
                        return v18;
                    v18 = *((int *)((int)idx[20] + *((int *)(int)idx[64]) * 4));
                    *((struct_0 **)((int)idx[20] + *((int *)(int)idx[60]) * 4)) = v18;
                    return v18;
                }
                else if (v13 != 97)
                {
                    v14 = v13 - 108;
                    v15 = v14 - 2;
                    if (v14 >= 2)
                    {
                        if (v15 >= 2)
                        {
                            if (v15 - 18 >= 4 || *((char *)(int)idx[0x44]) || *((int *)(int)idx[60]) == 0x7)
                                return v16;
                            v16 = *((int *)(int)idx[64]);
                            *((unsigned int *)((int)idx[20] + v16 * 4)) = 0;
                            return v16;
                        }
                        else
                        {
                            v28 = (int)idx[20];
                            v28->field_18 = 0;
                            return v28;
                        }
                    }
                }
                else
                {
                    j = NULL;
                    do
                    {
                        *((unsigned int *)((int)idx[20] + j * 4)) = 0;
                        j = (char *)&j->field_0 + 1;
                    } while (j != 8);
                    return j;
                }
            }
            else
            {
                if (v13 != 0x99)
                {
                    v19 = v13 - 164;
                    if (v19 < 4)
                    {
                        *((unsigned int *)((int)idx[20] + 24)) = 0;
                        v20 = (int)idx[20];
                        v20->field_1c = 0;
                        return v20;
                    }
                    else if (v19 - 6 >= 2)
                    {
                        return v19 - 8;
                    }
                }
                else
                {
                    v21 = (int)idx[20];
                    v21->field_8 = 0;
                    return v21;
                }
            }
        }
        else
        {
            if (v13 < 200)
            {
                v22 = v13 - 172;
                v23 = (char *)&v22->field_0 + 2;
                if (v22 < 2)
                {
                    v28 = (int)idx[20];
                    v28->field_18 = 0;
                    return v28;
                }
                if (v23 >= 2)
                {
                    v24 = v23 - 10;
                    if (v24 >= 8)
                    {
                        if (v24 != 15 || *((char *)(int)idx[0x44]))
                            return v25;
                        v25 = (int)idx[4];
                        if (!(char)v25->field_0)
                            *((int *)((int)idx[20] + *((int *)(int)idx[64]) * 4)) = (int)idx[8];
                        return v25;
                    }
                    else
                    {
                        if (*((char *)(int)idx[4]))
                            return v26;
                        v26 = *((short *)(int)idx[88]) & 7;
                        *((int *)((int)idx[20] + v26 * 4)) = (int)idx[8];
                        return v26;
                    }
                }
            }
            else if (v13 < 224)
            {
                v29 = v13 - 200;
                if (v29 < 2)
                {
                    v31 = (int)idx[20];
                    v31->field_14 = 0;
                    return v31;
                }
                if (v29 != 23)
                    return v30;
                v30 = (int)idx[76];
                if ((char)v30->field_0 == 224)
                    *((struct_0 **)(int)idx[20]) = NULL;
                return v30;
            }
            else
            {
                v32 = v13 - 224;
                v33 = v32 - 3;
                if (v32 < 3)
                {
                    v36 = (int)idx[20];
                    v36->field_4 = 0;
                    return v36;
                }
                else if (v33 != 20)
                {
                    if (v33 != 28)
                        return v34;
                    v34 = (int)idx[60];
                    if (v34->field_0 <= 0x1 && !*((char *)(int)idx[0x44]))
                        *((unsigned int *)((int)idx[20] + *((int *)(int)idx[64]) * 4)) = 0;
                    return v34;
                }
                else
                {
                    if (*((int *)(int)idx[60]) < 4)
                        return v35;
                    v35 = (int)idx[20];
                    v35->field_8 = 0;
                    return v35;
                }
            }
        }
        v27 = (int)idx[20];
        v27->field_1c = 0;
        return v27;
    }
}
```

## `sub_0040c392` `0x0040c392`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40c392(void)
{
    sub_40c394();
    return;
}
```

## `sub_0040c394` `0x0040c394`

_532 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
    char padding_1[1];
    unsigned short field_2;
    char padding_4[1];
    char field_5;
    char field_6;
    char padding_7[21];
    struct struct_1 *field_1c;
    struct struct_1 *field_20;
} struct_0;

typedef struct struct_1 {
    char field_0;
} struct_1;

extern unsigned short g_41e4f4[4];
extern unsigned short g_41e6f4[4];
extern char g_41e8f4;
extern char g_41ea48;
extern char g_41eb48;

int sub_40c394(void)
{
    char *v18;  // eax
    unsigned long v19;  // ldt
    unsigned int v28;  // edx
    unsigned int v29;  // edx
    unsigned long v30;  // 4128
    unsigned long v20;  // gdt
    unsigned short v21;  // fs
    unsigned long v22;  // 4141
    unsigned long v23;  // 4150
    char *v24;  // edx
    char *v25;  // ecx
    unsigned int v26;  // edx
    char *v27;  // eax
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    char *v2;  // [bp-0x20]
    char *iter;  // [bp-0xc]
    char v4;  // [bp-0x4]
    struct_0 *idx;  // [bp+0x4]
    unsigned int v6;  // [bp+0x10]
    unsigned int *v7;  // [bp+0x14]
    unsigned int *v8;  // [bp+0x1c]
    unsigned int *v9;  // [bp+0x38]
    char *v10;  // [bp+0x40]
    unsigned int *v11;  // [bp+0x4c]
    void* v12;  // [bp+0x50]
    unsigned short *v13;  // [bp+0x54]
    char *v14;  // [bp+0x58]
    char *v15;  // [bp+0x5c]
    char *v16;  // [bp+0x60]
    char *v17;  // [bp+0x64]

    iter = v18;
    sub_4054b4();
    idx->field_1c = iter;
    if (iter)
    {
        *(v13) = 0;
        v2 = &v4;
        v1 = sub_40c534;
        v22 = _ccall(v19, v20, (unsigned int)v21, 0);
        v0 = *((int *)v22);
        v23 = _ccall(v19, v20, (unsigned int)v21, 0);
        *((unsigned int **)v23) = &v0;
        *(v24) = 0;
        *(v25) = 0;
        *(v17) = 0;
        *(v16) = 0;
        *(v15) = 0;
        *(v14) = 0;
        *(v7) = 4;
        do
        {
            *(v13) = *(iter);
            iter += 1;
        } while ((char)sub_40b240(&v4));
        if (*(v13) == 15)
        {
            *(v13) = *(iter);
            *((unsigned int *)v12) = g_41e6f4[*(v13)];
            *(v11) = *(&(&g_41eb48)[*(v13)]);
            *(v13) = *(v13) + 0xf00;
            iter += 1;
        }
        else
        {
            *((unsigned int *)v12) = g_41e4f4[*(v13)];
            *(v11) = *(&(&g_41ea48)[*(v13)]);
        }
        if ((*((char *)v12) & 56))
        {
            sub_40b35c(&v4);
            if (((char)*((int *)v12) & 56) == 8)
            {
                v26 = 10;
                v27 = &g_41e8f4;
                do
                {
                    v28 = v26;
                    if (*(v27) == *(v13))
                    {
                        if (*(v10))
                        {
                            *((unsigned int *)v12) = *((short *)&v27[2 + 2 * *(v9)]);
                            break;
                        }
                        else
                        {
                            *((unsigned int *)v12) = *((short *)&v27[18 + 2 * *(v9)]);
                            break;
                        }
                    }
                } while ((v27 += 0x22, v29 = v28 - 1, v26 = v28 - 1, v28 != 1));
            }
        }
        *(v8) = sub_40b650(&v4);
        if ((char)sub_40b734(&v4))
        {
            idx->field_0 = 1;
            sub_40bc24(&v4);
            if (v6)
                sub_40bea4(&v4);
        }
        iter = &iter[*(v8)];
        v30 = _ccall(v19, v20, (unsigned int)v21, 0);
        *((unsigned int *)v30) = v0;
        idx->field_2 = *(v13);
    }
    idx->field_20 = iter;
    if (!idx->field_6 && !idx->field_5)
        return;
    if (*((int *)&idx->padding_7[1]) == idx->field_20)
    {
        idx->field_6 = 0;
        idx->field_5 = 0;
        memset(&idx->padding_7[1], 0, 0x11);
    }
    return;
}
```

## `sub_0040c534` `0x0040c534`

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

unsigned int sub_40c534(int a0)
{
    struct_1 *v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x8]

    return sub_4030c0(v0, a0, v1);
}
```

## `sub_0040c539` `0x0040c539`

_11 bytes. (leaf/helper — see body)_

```c
void sub_40c539(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, unsigned int *a10)
{
    unsigned int v0;  // [bp+0x0]
    char *v1;  // [bp+0x10000c]

    *(v1) = 0;
    sub_4034ec(v0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10);
}
```

## `sub_0040c5b8` `0x0040c5b8`

_131 bytes. (leaf/helper — see body)_

```c
int sub_40c5b8(void)
{
    int v23;  // ecx
    int v24;  // edx
    int v25;  // edi
    int v26;  // esi
    int v27;  // ebx
    char v0;  // [bp-0x44]
    char v1;  // [bp-0x40]
    char v2;  // [bp-0x3c]
    char v3;  // [bp-0x38]
    char v4;  // [bp-0x34]
    char v5;  // [bp-0x30]
    char v6;  // [bp-0x2c]
    char v7;  // [bp-0x28]
    char v8;  // [bp-0x24]
    char v9;  // [bp-0x20]
    char v10;  // [bp-0x1c]
    char v11;  // [bp-0x17]
    char v12;  // [bp-0x16]
    char v13;  // [bp-0x15]
    char v14;  // [bp-0x14]
    char v15;  // [bp-0x10]
    char v16;  // [bp-0xc]
    char v17;  // [bp-0xa]
    char v18;  // [bp-0x9]
    char v19;  // [bp-0x8]
    char v20;  // [bp-0x7]
    int v21;  // [bp+0x4]
    int v22;  // [bp+0x8]

    sub_40c394(v21, v22, v23, v24, &v0, &v1, &v2, &v3, &v4, &v5, &v6, &v7, &v8, &v9, &v10, &v11, &v12, &v13, &v14, &v15, &v16, &v17, &v18, &v19, &v20, v25, v26, v27);
    return;
}
```

## `sub_0040c63b` `0x0040c63b`

_1 bytes. (leaf/helper — see body)_

```c
int sub_40c63b(void)
{
    sub_40c63c();
    return;
}
```

## `sub_0040c63c` `0x0040c63c`

_23 bytes. (leaf/helper — see body)_

```c
int sub_40c63c(void)
{
    int v1;  // edx
    int v2;  // esi
    int v3;  // ebx

    sub_40c5b8(v1, 0, v2, v3);
    return;
}
```

## `sub_0040c653` `0x0040c653`

_1 bytes. (leaf/helper — see body)_

```c
int sub_40c653(void)
{
    sub_40c654();
    return;
}
```

## `sub_0040c654` `0x0040c654`

_409 bytes. (leaf/helper — see body)_

```c
int sub_40c654(void)
{
    char v4;  // cl
    unsigned int v5;  // eax
    unsigned int v14;  // eax
    void* iter;  // edi
    unsigned int v16;  // eax
    void* idx;  // eax
    unsigned int v6;  // eax
    unsigned int v7;  // eax
    unsigned int index[4];  // edx
    unsigned int v9;  // eax
    unsigned int v10;  // eax
    unsigned int v11;  // edx
    unsigned int v12;  // eax
    void* v13;  // ecx
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    void* idx1;  // [bp+0x4]

    v1 = 0;
    v4 = 1;
    v5 = (int)idx1[36] - 1;
    if (v5 >= 0)
    {
        v6 = v5 + 1;
        v2 = 0;
        do
        {
            v7 = v6;
            index = *((int *)((int)idx1[8] + 28)) + v2 * 48;
            if (v9 == index[0])
            {
                if (!index[3] || v11 > index[3] && v11 < index[0])
                    index[3] = v11;
                v12 = 0;
                v13 = idx1 - 32;
                do
                {
                    if (*((int *)v13) != index[1 + v12])
                        index[1 + v12] = 0;
                } while ((v12 += 1, v13 += 4, v12 != 8));
                v4 = 0;
                break;
            }
            else if (v9 > index[0] && v9 <= index[1])
            {
                v1 = index[1];
                index[1] = v9 - 1;
                v14 = 0;
                iter = idx1 - 32;
                do
                {
                    if (*((int *)iter) != index[1 + v14])
                        *((unsigned int *)iter) = 0;
                } while ((v14 += 1, iter += 4, v14 != 8));
                if ((int)idx1[40] == v2)
                {
                    *((int *)&idx1[40]) = (int)idx1[36];
                    break;
                }
            }
        } while ((v2 += 1, v10 = v7 - 1, v6 = v7 - 1, v7 != 1));
    }
    if (!v4)
        return;
    v16 = sub_40464c();
    if (v16 == (int)idx1[36])
    {
        if (!*((int *)((int)idx1[8] + 28)))
        {
            v0 = 8;
            sub_404808();
        }
        else
        {
            v0 = sub_40464c() * 2;
            sub_404808();
        }
    }
    *((unsigned int *)&idx1[36]) = (int)idx1[36] + 1;
    idx = *((int *)((int)idx1[8] + 28)) + (int)idx1[36] * 48 - 48;
    *((unsigned int *)idx) = v9;
    *((unsigned int *)&idx[4]) = v1;
    *((char *)&idx[8]) = 0;
    *((char *)&idx[9]) = 0;
    *((unsigned int *)&idx[12]) = v11;
    sub_402628();
    return;
}
```

## `sub_0040c7ed` `0x0040c7ed`

_3 bytes. (leaf/helper — see body)_

```c
int sub_40c7ed(void)
{
    sub_40c7f0();
    return;
}
```

## `sub_0040c7f0` `0x0040c7f0`

_195 bytes. (leaf/helper — see body)_

```c
int sub_40c7f0(void)
{
    int v7;  // eax
    void* idx;  // eax
    unsigned int v9;  // eax
    unsigned int v10;  // edx
    char v11;  // cl
    unsigned int v0;  // [bp-0x14]
    int v1;  // [bp-0x10]
    int v2;  // [bp-0xc]
    int v3;  // [bp-0x8]
    char v4;  // [bp+0x0]
    char v5;  // [bp+0x4]
    void* v6;  // [bp+0x8]

    v7 = sub_40464c(v1, v2, v3, &v4);
    if (v7 == (int)v6[36])
    {
        if (!*((int *)((int)v6[8] + 28)))
        {
            v0 = 8;
            sub_404808();
        }
        else
        {
            v0 = sub_40464c() * 2;
            sub_404808();
        }
    }
    *((unsigned int *)&v6[36]) = (int)v6[36] + 1;
    idx = *((int *)((int)v6[8] + 28)) + (int)v6[36] * 48 - 48;
    *((unsigned int *)idx) = v9;
    *((unsigned int *)&idx[4]) = v10 + v9 - 1;
    *((char *)&idx[8]) = v11;
    *((char *)&idx[9]) = v5;
    *((unsigned int *)&idx[12]) = 0;
    sub_4054b4();
    return;
}
```

## `sub_0040c8b3` `0x0040c8b3`

_1 bytes. (leaf/helper — see body)_

```c
int sub_40c8b3(void)
{
    sub_40c8b4();
    return;
}
```

## `sub_0040c8b4` `0x0040c8b4`

_1364 bytes. (leaf/helper — see body)_

```c
typedef struct struct_2 {
    char padding_0[6];
    char field_6;
    char field_7;
    void* field_8;
    unsigned int field_c;
    unsigned int field_10;
    char padding_14[12];
    struct struct_3 *field_20;
} struct_2;

typedef struct struct_1 {
    char padding_0[10];
    unsigned short field_a;
    struct struct_0 *field_c;
} struct_1;

typedef struct struct_10 {
    char field_0;
    char padding_1[3];
    void* field_4;
    struct struct_3 *field_8;
    unsigned int field_c;
    char field_10;
    char padding_11[3];
    unsigned int field_14;
    unsigned int field_18;
} struct_10;

typedef struct struct_3 {
    unsigned int field_0;
} struct_3;

typedef struct struct_0 {
    char padding_0[8];
    unsigned int field_8;
} struct_0;

extern unsigned int g_41e4e4;

int sub_40c8b4(void)
{
    unsigned int v21;  // ebx
    unsigned int v22;  // esi
    unsigned int idx;  // eax
    void* v32;  // eax
    unsigned int v33;  // edi
    unsigned int i;  // edi
    unsigned int v35;  // edi
    char k[4];  // esi
    char node[4];  // edi
    unsigned int v38;  // ecx
    unsigned short v39;  // ax
    unsigned short v40;  // ax
    unsigned int v23;  // edi
    char v41;  // al
    char v42;  // al
    int v43;  // edi
    int v44;  // edi
    unsigned int v45;  // esi
    int v46;  // edi
    int v47;  // edi
    int v48;  // eax
    struct_10 *idx1;  // eax
    unsigned int v50;  // edx
    unsigned long v24;  // ldt
    int v51;  // edi
    int v52;  // edi
    unsigned int v53;  // esi
    int v54;  // edi
    int v55;  // edi
    unsigned int idx2;  // eax
    unsigned int v57;  // edx
    unsigned int v58;  // ecx
    unsigned int v59;  // ebx
    unsigned long v60;  // 4118
    unsigned long v25;  // gdt
    unsigned short v26;  // fs
    unsigned long v27;  // 4188
    unsigned long v28;  // 4192
    struct_2 *v29;  // eax
    int v30;  // esi
    int v0;  // [bp-0x84]
    void* v1;  // [bp-0x80]
    int v2;  // [bp-0x7c]
    unsigned int v3;  // [bp-0x78]
    unsigned int v4;  // [bp-0x74]
    char *v5;  // [bp-0x70]
    unsigned int v6;  // [bp-0x6c]
    unsigned int v7;  // [bp-0x68]
    unsigned int v8;  // [bp-0x64]
    unsigned int v9;  // [bp-0x60]
    unsigned int v10;  // [bp-0x5c]
    char v11;  // [bp-0x58]
    unsigned long v12;  // [bp-0x34]
    void* v13;  // [bp-0x2c]
    void* v14;  // [bp-0x18]
    unsigned int v15;  // [bp-0x10]
    struct_1 *iter;  // [bp-0xc], Other Possible Types: unsigned int
    char v17;  // [bp-0x6]
    char v18;  // [bp-0x5]
    char v19;  // [bp-0x4]
    void* index;  // [bp+0x4]

    v8 = v21;
    v7 = v22;
    v6 = v23;
    v10 = 0;
    v9 = 0;
    v15 = 0;
    v5 = &v19;
    v4 = sub_40ce1e;
    v27 = _ccall(v24, v25, (unsigned int)v26, 0);
    v3 = *((int *)v27);
    v28 = _ccall(v24, v25, (unsigned int)v26, 0);
    *((unsigned int **)v28) = &v3;
    if (v29->padding_0[5] || v29->field_6)
    {
        if (v29->field_c || v29->field_10)
        {
            v18 = 0;
            v32 = v29->field_8;
            if (v32 == (int)index[44])
            {
                v18 = 1;
                sub_40c654(index);
            }
            else if (v32 == (int)index[16])
            {
                v18 = 1;
                sub_40c654(index);
                sub_40c63c();
                if (*((char *)((void*)&v12 + 6)) && (int)index[48] < v13 && *((int *)&v29->padding_14[8]) > v13 && (char)v13[5] == 104 && (int)v13[4] > (int)index[48])
                    sub_40c654(index);
            }
            else if (v32 == (int)index[24])
            {
                v18 = 1;
                v1 = 0x1;
                sub_40c7f0(1, index);
                v33 = v29->field_20->field_0;
                if (v29->field_20->field_0)
                {
                    iter = 1;
                    do
                    {
                        i = v33;
                        sub_40c654(index);
                        iter += 1;
                        v35 = i - 1;
                        v33 = v35;
                        v1 = index;
                    } while (i != 1);
                }
            }
            else if (v32 == (int)index[20])
            {
                v18 = 1;
            }
            else if (v29->field_8 == g_41e4e4 && v29->field_8 && *((int *)(*((int *)((int)index[8] + 28)) + (int)index[40] * 48)) < *((int *)&v29->padding_14[8]))
            {
                iter = NULL;
                sub_40c63c();
                while ((char)v12 && *((int *)&v29->padding_14[8]) != v14)
                {
                    if (*((unsigned short *)((void*)&v12 + 2)) == 184)
                        iter = (int)v14[1];
                    sub_40c63c();
                    k = &v11;
                    node = &v12;
                    for (v38 = 9; v38; k += 1)
                    {
                        v38 -= 1;
                        *(node) = *(k);
                        node += 1;
                    }
                }
                if (iter)
                {
                    iter = &iter->field_a;
                    v39 = *((short *)&iter->padding_0[0]);
                    v40 = v39 - 1;
                    if (v39 < 1)
                    {
                        sub_40c654(index);
                    }
                    else if (v39 == 1)
                    {
                        sub_40c654(index);
                    }
                    else if (!(v40 - 1) * 0x10000)
                    {
                        sub_40c654(index);
                    }
                    else if (!(v40 - 2) * 0x10000)
                    {
                        for (iter = *((int *)&iter->padding_0[2]) + 8; *((int *)iter); iter += 20)
                        {
                            sub_40c654(index);
                        }
                    }
                }
            }
            if (*((int *)&v29->padding_14[0]) == 4 && (v29->padding_0[5] || v29->field_8 < (int)index[52] || v29->field_8 > (int)index[56] || v18))
            {
                if (v29->field_8)
                {
                    v1 = (int)index[60];
                    if ((char)sub_40ddd8((int)index[60]))
                    {
                        v41 = v17 + 23;
                        if (v17 == 233 || (v42 = v41 - 2, v41 == 2 || v41 == 22 || v41 - 25 < 2))
                        {
                            sub_40c63c();
                            if ((char)v12 && v13 && (!(char)sub_40a54c() || (sub_40ab6c(&v10), !v10)) && (char)sub_40a54c())
                            {
                                sub_40ab6c(&v9);
                                if (v9)
                                    v29->field_8 = v13;
                            }
                        }
                    }
                }
                v18 = 1;
                v43 = sub_404654();
                if (v43 >= 0)
                {
                    v44 = v43 + 1;
                    v45 = 0;
                    do
                    {
                        v46 = v44;
                        if (*((int *)(*((int *)((int)index[8] + 32)) + v45 * 28 + 8)) == v29->field_20)
                        {
                            v18 = 0;
                            break;
                        }
                    } while ((v45 += 1, v47 = (int)(v46 - 1), v44 = (int)(v46 - 1), v46 != 1));
                }
                if (v18)
                {
                    v0 = sub_40464c() + 1;
                    sub_404808();
                    v48 = sub_404654();
                    idx1 = *((int *)((int)index[8] + 32)) + v48 * 28;
                    idx1->field_0 = v29->padding_0[5];
                    idx1->field_4 = *((int *)&v29->padding_14[8]);
                    idx1->field_8 = v29->field_20;
                    idx1->field_c = v29->field_8;
                    idx1->field_10 = v29->field_7;
                    idx1->field_14 = v29->field_c;
                    v50 = v29->field_10;
                    idx1->field_18 = v50;
                    if (v50)
                        *((unsigned int *)((int)index[8] + 48)) = *((int *)((int)index[8] + 48)) + 4;
                }
            }
            else
            {
                sub_40c654(index);
                v1 = index;
            }
            v51 = sub_404654();
            if (v51 >= 0)
            {
                v52 = v51 + 1;
                v53 = 0;
                do
                {
                    v54 = v52;
                    if (*((int *)(*((int *)((int)index[8] + 36)) + v53 * 12 + 4)) == *((int *)&v29->padding_14[8]))
                    {
                        idx2 = sub_404654() * 3;
                        v57 = *((int *)((int)index[8] + 36));
                        v58 = v53 * 3;
                        v59 = *((int *)((int)index[8] + 36));
                        *((int *)(v59 + v58 * 4)) = *((int *)(v57 + idx2 * 4));
                        *((int *)(v59 + v58 * 4 + 4)) = *((int *)(v57 + idx2 * 4 + 4));
                        *((int *)(v59 + v58 * 4 + 8)) = *((int *)(v57 + idx2 * 4 + 8));
                        v0 = sub_404654();
                        sub_404808();
                        break;
                    }
                } while ((v53 += 1, v55 = (int)(v54 - 1), v52 = (int)(v54 - 1), v54 != 1));
            }
        }
        else
        {
            v30 = sub_40464c();
            v2 = v30 + 1;
            sub_404808();
            idx = v30 * 3;
            *((char *)(*((int *)((int)index[8] + 36)) + idx * 4)) = v29->padding_0[5];
            *((int *)(*((int *)((int)index[8] + 36)) + idx * 4 + 4)) = *((int *)&v29->padding_14[8]);
            *((struct struct_3 **)(*((int *)((int)index[8] + 36)) + idx * 4 + 8)) = v29->field_20;
        }
    }
    v60 = _ccall(v24, v25, (unsigned int)v26, 0);
    *((void* *)v60) = v1;
    v3 = sub_40ce25;
    sub_40ce08();
    return;
}
```

## `sub_0040ce08` `0x0040ce08`

_22 bytes. (leaf/helper — see body)_

```c
int sub_40ce08(void)
{
    sub_403a34();
    return sub_403a10();
}
```

## `sub_0040ce1e` `0x0040ce1e`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40ce1e(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0040ce23` `0x0040ce23`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40ce23(void)
{
    return sub_40ce08();
}
```

## `sub_0040ce25` `0x0040ce25`

_7 bytes. (leaf/helper — see body)_

```c
void sub_40ce25(unsigned int a0, unsigned int a1)
{
    return;
}
```

## `sub_0040ce2c` `0x0040ce2c`

_1070 bytes. (leaf/helper — see body)_

```c
typedef struct struct_1 {
    unsigned int field_0;
    char padding_4[24];
    struct struct_0 *field_1c;
    unsigned int field_20;
} struct_1;

typedef struct struct_0 {
    char padding_0[1];
    unsigned int field_1;
} struct_0;

int sub_40ce2c(void)
{
    int v13;  // edi
    struct_1 *v14;  // esi
    void* i;  // esi
    char node[4];  // edi
    unsigned int v24;  // ecx
    struct_1 *v25;  // esi
    char j[4];  // esi
    unsigned int v27;  // ecx
    struct_1 *iter;  // edi
    unsigned short v29;  // ax
    unsigned short v30;  // ax
    int v15;  // ebx
    char v33;  // al
    unsigned int v34;  // eax
    void* v35;  // eax
    char *v36;  // edx
    unsigned int v37;  // ebx
    unsigned int v38;  // ebx
    unsigned int k;  // ebx
    unsigned int v40;  // ebx
    int v16;  // ebx
    int v17;  // ebx
    int v18;  // ebx
    unsigned int v19;  // eax
    int v20;  // ebx
    struct_1 *idx;  // esi
    struct_1 *v0;  // [bp-0x7c]
    struct_1 *v1;  // [bp-0x74]
    char v2;  // [bp-0x5c]
    char v3;  // [bp-0x38]
    unsigned int v4;  // [bp-0x18]
    unsigned int v5;  // [bp-0x14]
    char v6;  // [bp-0x10]
    char v7;  // [bp-0xf]
    char v8;  // [bp-0xe]
    char v9;  // [bp-0xd]
    unsigned int v10;  // [bp-0xc]
    unsigned int iter1;  // [bp-0x8]
    void* index;  // [bp+0x4]

    v4 = 0;
    v7 = 0;
    v10 = *((int *)(*((int *)((int)index[8] + 28)) + (int)index[40] * 48));
    sub_402628(v13, v14, v15);
    v5 = (int)index[56];
    v16 = sub_404654();
    if (v16 >= 0)
    {
        v17 = v16 + 1;
        iter1 = 0;
        do
        {
            v18 = v17;
            v19 = *((int *)(*((int *)((int)index[8] + 28)) + iter1 * 48));
            if (v19 > *((int *)(*((int *)((int)index[8] + 28)) + (int)index[40] * 48)) && v19 < v5)
                v5 = v19;
        } while ((iter1 += 1, v20 = (int)(v18 - 1), v17 = (int)(v18 - 1), v18 != 1));
    }
    while (true)
    {
        v1 = idx;
        i = index - 32;
        node = &v3;
        for (v24 = 8; v24; i += 4)
        {
            v24 -= 1;
            *((int *)&node[0]) = *((int *)i);
            node += 1;
        }
        v25 = idx;
        sub_40c5b8(&v2, (int)index[60]);
        v0 = v25;
        j = &v2;
        v27 = 9;
        for (iter = v25; v27; j += 1)
        {
            v27 -= 1;
            *((char [4])&iter->field_0) = *(j);
            iter = iter->padding_4;
        }
        idx = v25;
        if (!(char)idx->field_0 || !((*((unsigned int *)(*((int *)((int)index[8] + 28)) + (int)index[40] * 48 + 4)) = idx->field_20 - 1, v29 = *((short *)((char *)&idx->field_0 + 2)) - 194, v29 >= 2 && (v30 = v29 - 8, v29 - 8 >= 2 && v29 != 13))))
            break;
        if (*((short *)((char *)&idx->field_0 + 2)) == 104 && idx->field_20 - (char *)idx->field_1c == 5 && *((char *)idx->field_20) == 100)
        {
            v4 = *((int *)(idx->field_1c->padding_0)[1]);
        }
        else if (v4)
        {
            if (*((short *)((char *)&idx->field_0 + 2)) == 0xff && ((idx->padding_4[0] & 248) == 48 && idx->field_20 - (char *)idx->field_1c == 3 && !*((int *)&(&v3)[4 * (idx->padding_4[0] & 7)]) || idx->padding_4[0] == 53 && idx->field_20 - (char *)idx->field_1c == 7 && !*((int *)(idx->field_1c->padding_0)[3])))
                sub_40c654(index);
            v4 = 0;
        }
        if (!v7)
        {
            if (*((short *)((char *)&idx->field_0 + 2)) == 131 && idx->padding_4[0] + 8 < 8)
            {
                v7 = *((char *)(v10 + 2));
                v8 = idx->padding_4[0] & 7;
                v9 = 0;
            }
        }
        else
        {
            if (!v9)
            {
                if (*((short *)((char *)&idx->field_0 + 2)) == 0x77 || *((short *)((char *)&idx->field_0 + 2)) == 127 || *((short *)((char *)&idx->field_0 + 2)) == 3975 || *((short *)((char *)&idx->field_0 + 2)) == 3983)
                {
                    v9 = 1;
                    v7 += 1;
                }
                else if (*((short *)((char *)&idx->field_0 + 2)) == 115 || *((short *)((char *)&idx->field_0 + 2)) == 125 || *((short *)((char *)&idx->field_0 + 2)) == 3971 || *((short *)((char *)&idx->field_0 + 2)) == 3981)
                {
                    v9 = 1;
                }
                else
                {
                    v7 = 0;
                }
            }
            else
            {
                if (*((short *)((char *)&idx->field_0 + 2)) == 0xff && idx->padding_4[0] == 36 && (*((char *)(v10 + 2)) & 199) == 133 && (*((char *)(v10 + 2)) >> 3 & 7) == v8 && *((int *)(v10 + 3)) == idx->field_20)
                {
                    v37 = v7 - 1;
                    if (v37 >= 0)
                    {
                        v38 = v37 + 1;
                        iter1 = 0;
                        do
                        {
                            k = v38;
                            sub_40c654(index);
                            iter1 += 1;
                            v40 = k - 1;
                            v38 = v40;
                        } while (k != 1);
                    }
                    sub_40c7f0(0, index);
                    break;
                }
                else
                {
                    v7 = 0;
                }
            }
        }
        if (!*((int *)&idx->padding_4[4]) || *((int *)&idx->padding_4[4]) != (int)index[12])
            v33 = 0;
        else
            v33 = 1;
        v6 = v33;
        sub_40c8b4(index);
        v34 = *((int *)(*((int *)((int)index[8] + 28)) + (int)index[36] * 48 - 48));
        if (v34 > *((int *)(*((int *)((int)index[8] + 28)) + (int)index[40] * 48)) && v34 < v5)
            v5 = v34;
        if (v6 || idx->padding_4[2] && (*((short *)((char *)&idx->field_0 + 2)) - 233 < 3 || *((short *)((char *)&idx->field_0 + 2)) == 0xff && (idx->padding_4[0] & 48) == 32))
            break;
        v10 = idx->field_20;
        v6 = 0;
        iter1 = 8;
        v35 = index - 32;
        v36 = &v3;
        do
        {
            if (*((int *)&v36) != *((int *)v35))
            {
                v6 = 1;
                break;
            }
        } while ((v36 += 4, v35 += 4, iter1 -= 1, iter1 = iter1, iter1 != 1));
        if (v6 || v10 >= v5)
        {
            sub_40c654(index);
            break;
        }
    }
    if (v10 > v5)
        *((char *)&idx->field_0) = 0;
    return;
}
```

## `sub_0040d25a` `0x0040d25a`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40d25a(void)
{
    sub_40d25c();
    return;
}
```

## `sub_0040d25c` `0x0040d25c`

_150 bytes. (leaf/helper — see body)_

```c
int sub_40d25c(void)
{
    unsigned int *v1;  // eax
    unsigned int v2;  // esi
    int v3;  // esi
    unsigned int v4;  // edx
    int i;  // esi
    unsigned int index;  // ecx
    unsigned int v7;  // esi
    void* idx;  // [bp+0x4]

    *((unsigned int *)((int)idx[8] + 8)) = 4294967295;
    *(v1) = 0;
    v2 = (int)idx[36] - 1;
    if (v2 >= 0)
    {
        v3 = v2 + 1;
        v4 = 0;
        do
        {
            i = v3;
            index = v4 * 6;
            if (*((int *)(*((int *)((int)idx[8] + 28)) + index * 8)) < *((int *)((int)idx[8] + 8)))
                *((int *)((int)idx[8] + 8)) = *((int *)(*((int *)((int)idx[8] + 28)) + index * 8));
            if (*((int *)(*((int *)((int)idx[8] + 28)) + index * 8 + 4)) > *(v1))
                *(v1) = *((int *)(*((int *)((int)idx[8] + 28)) + index * 8 + 4));
            v4 += 1;
            v7 = i - 1;
            v3 = v7;
        } while (i != 1);
    }
    *((unsigned int *)((int)idx[8] + 12)) = *(v1) - *((int *)((int)idx[8] + 8)) + 1;
    return;
}
```

## `sub_0040d2f2` `0x0040d2f2`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40d2f2(unsigned int a0)
{
    return sub_40d2f4();
}
```

## `sub_0040d2f4` `0x0040d2f4`

_74 bytes. (leaf/helper — see body)_

```c
int sub_40d2f4(void* a0)
{
    unsigned int idx[8];  // esi
    int v1;  // eax
    int v2;  // eax
    unsigned int v3;  // ebx
    int v4;  // eax
    unsigned int v5;  // edx

    idx = (int)a0[8];
    v1 = (int)a0[36] - 1;
    if (v1 < 0)
        return v1;
    v2 = v1 + 1;
    v3 = 0;
    while (true)
    {
        v4 = v2;
        v5 = v3 * 6;
        if (*((int *)(idx[7] + v5 * 8)) == idx[2])
        {
            idx[2] = *((int *)(idx[7] + v5 * 8 + 4)) + 1;
            return sub_40d2f4(a0);
        }
        v3 += 1;
        v2 = v4 - 1;
        if (v4 == 1)
            return v4 - 1;
    }
}
```

## `sub_0040d33e` `0x0040d33e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40d33e(void)
{
    sub_40d340();
    return;
}
```

## `sub_0040d340` `0x0040d340`

_1411 bytes. (leaf/helper — see body)_

```c
typedef struct MEMORY_BASIC_INFORMATION {
    void* BaseAddress;
    void* AllocationBase;
    enum PAGE_PROTECTION_FLAGS AllocationProtect;
    UIntPtr RegionSize;
    enum VIRTUAL_ALLOCATION_TYPE State;
    enum PAGE_PROTECTION_FLAGS Protect;
    enum PAGE_TYPE Type;
} MEMORY_BASIC_INFORMATION;

typedef struct struct_0 {
    char field_0;
    char padding_1[3];
    void* field_4;
    unsigned int field_8;
    unsigned int field_c;
    void* field_10;
    unsigned int field_14;
    char padding_18[4];
    void* field_1c;
    char padding_20[4];
    unsigned int field_24;
    char field_28;
    char padding_29[3];
    char field_2c;
    char padding_2d[3];
    unsigned int field_30;
} struct_0;

int sub_40d340(void)
{
    unsigned int v31;  // ebx
    unsigned int v32;  // esi
    void* index;  // eax
    void* idx;  // edx
    unsigned int v43;  // ecx
    void* idx1;  // edx
    unsigned int v45;  // edx
    unsigned int v46;  // eax
    int v47;  // eax
    int v48;  // eax
    int v49;  // ebx
    int v50;  // eax
    unsigned int v33;  // edi
    int v51;  // eax
    int v52;  // ebx
    int v53;  // eax
    int v54;  // eax
    unsigned int v55;  // esi
    int v56;  // eax
    int v57;  // eax
    int v58;  // edx
    int v59;  // eax
    int v60;  // eax
    unsigned int v34;  // ecx
    unsigned int v61;  // ebx
    int v62;  // eax
    int v63;  // eax
    unsigned int v64;  // ebx
    int v65;  // esi
    unsigned int idx2;  // eax
    int v67;  // eax
    int v68;  // eax
    int v69;  // eax
    char j[4];  // esi
    unsigned long v35;  // ldt
    char iter[4];  // edi
    unsigned int v72;  // ecx
    unsigned long v73;  // 4118
    unsigned long v36;  // gdt
    unsigned short v37;  // fs
    unsigned long v38;  // 4189
    unsigned long v39;  // 4193
    void* v40;  // eax
    int v0;  // [bp-0xd8]
    unsigned int v1;  // [bp-0xcc]
    unsigned int v2;  // [bp-0xc8]
    char *v3;  // [bp-0xc4]
    unsigned int v4;  // [bp-0xc0]
    unsigned int v5;  // [bp-0xbc]
    unsigned int v6;  // [bp-0xb8]
    unsigned int v7;  // [bp-0xb4]
    char v8;  // [bp-0xb0]
    MEMORY_BASIC_INFORMATION v9;  // [bp-0x8c]
    char v10;  // [bp-0x70], Other Possible Types: unsigned long long
    unsigned int v11;  // [bp-0x68]
    unsigned int v12;  // [bp-0x64]
    unsigned int v13;  // [bp-0x60]
    int v14;  // [bp-0x5c]
    char v15;  // [bp-0x58]
    void* v16;  // [bp-0x50]
    char i;  // [bp-0x49]
    unsigned int v18;  // [bp-0x48]
    unsigned int v19;  // [bp-0x44]
    unsigned int v20;  // [bp-0x3c]
    unsigned int v21;  // [bp-0x38]
    int v22;  // [bp-0x30], Other Possible Types: unsigned int
    int v23;  // [bp-0x2c]
    int v24;  // [bp-0x28]
    char v25;  // [bp-0x4]
    struct_0 *v26;  // [bp+0x4]
    int v27;  // [bp+0x8], Other Possible Types: unsigned int
    int v28;  // [bp+0xc], Other Possible Types: unsigned int
    int v29;  // [bp+0x10], Other Possible Types: unsigned int
    int v30;  // [bp+0x14], Other Possible Types: unsigned int

    v6 = v31;
    v5 = v32;
    v4 = v33;
    v7 = 0;
    v22 = v34;
    v3 = &v25;
    v2 = sub_40d8cf;
    v38 = _ccall(v35, v36, (unsigned int)v37, 0);
    v1 = *((int *)v38);
    v39 = _ccall(v35, v36, (unsigned int)v37, 0);
    *((unsigned int **)v39) = &v1;
    if (!v22)
        v22 = sub_40b218();
    if (!v30)
        v30 = sub_40b220();
    if (!v29)
        v29 = sub_40b228();
    if (!v28)
        v28 = sub_40b230();
    if (!v27)
        v27 = sub_40b238();
    sub_404210();
    sub_4054b4();
    if (VirtualQuery(v40, &v9, 0x1c) == 0x1c && v9.State == 0x1000)
    {
        index = sub_40a658();
        if (index)
        {
            idx = ((short)index[24] == 523 ? index + 264 : index + 248);
            if (((char)idx[36] & 32))
            {
                v43 = v9.AllocationBase;
                v21 = (int)idx[12] + v43;
                v20 = (int)idx[8] + v21 - 1;
                idx1 = idx + 40;
                if (((char)idx1[36] & 32))
                    v20 = (int)idx1[12] + v43 + (int)idx1[8] - 1;
            }
            else if ((short)index[24] == 523)
            {
                v21 = (int)index[44] + v9.AllocationBase;
                v20 = (int)index[28] + v21;
            }
            else
            {
                v21 = (int)index[44] + v9.AllocationBase;
                v20 = (int)index[28] + v21;
            }
            if ((short)index[24] != 523)
            {
                v45 = (int)index[48] + v9.AllocationBase;
                v46 = (int)index[36] + v45 + (int)index[32] - 1;
                if (v45 < v21)
                    v21 = v45;
                if (v46 > v20)
                    v20 = v46;
            }
        }
        else
        {
            v21 = v9.BaseAddress;
            v20 = v21 + (char *)v9.RegionSize;
        }
        v26->field_4 = v40;
        v26->field_28 = 0;
        v26->field_2c = 1;
        v24 = 0;
        sub_4054b4();
        sub_40c654(&v25);
        while (true)
        {
            v23 = -1;
            v47 = v24 - 1;
            if (v47 >= 0)
            {
                v48 = v47 + 1;
                v49 = 0;
                do
                {
                    v50 = v48;
                    if (!*((int *)(4 + (char *)v26->field_1c + 48 * v49)))
                    {
                        v23 = v49;
                        break;
                    }
                } while ((v49 = (int)(v49 + 1), v51 = (int)(v50 - 1), v48 = (int)(v50 - 1), v50 != 1));
            }
            if (v23 == -1)
            {
                v52 = sub_404654();
                if (v52 >= 0)
                {
                    do
                    {
                        i = 0;
                        v53 = v24 - 1;
                        if (v53 >= 0)
                        {
                            v54 = v53 + 1;
                            v55 = 0;
                            do
                            {
                                v56 = v54;
                                if (*((int *)(v26->field_24 + v52 * 12 + 4)) >= *((int *)((char *)v26->field_1c + 48 * v55)) && *((int *)(v26->field_24 + v52 * 12 + 8)) <= *((int *)(4 + (char *)v26->field_1c + 48 * v55)))
                                {
                                    sub_40c5b8(&v10, v58);
                                    if (v11)
                                    {
                                        sub_40c8b4(&v25);
                                        if (!*((int *)(-44 + (char *)v26->field_1c + 48 * v24)))
                                        {
                                            v23 = v24 - 1;
                                            i = 1;
                                            break;
                                        }
                                    }
                                }
                            } while ((v55 += 1, v57 = (int)(v56 - 1), v54 = (int)(v56 - 1), v56 != 1));
                        }
                    } while (!i && (v52 = (int)(v52 - 1), v52 != -1));
                }
            }
            if (v23 == -1)
            {
                i = 0;
                v59 = sub_404654();
                if (v59 >= 0)
                {
                    v60 = v59 + 1;
                    v61 = 0;
                    do
                    {
                        v62 = v60;
                        if (!*((char *)(v26->field_24 + v61 * 12)))
                        {
                            i = 1;
                            break;
                        }
                    } while ((v61 += 1, v63 = (int)(v62 - 1), v60 = (int)(v62 - 1), v62 != 1));
                }
                if (!i)
                    break;
                sub_40d25c(&v25);
                sub_40d2f4(&v25);
                if (v26->field_8 - 1 == v19 || v19 - v26->field_8 >= 0x400)
                    break;
                v23 = v24;
                sub_4054b4();
                sub_40c654(&v25);
                sub_40ce2c(&v25);
                if ((char)v10)
                    continue;
                v24 = v23;
                *((char *)&v10) = 1;
                break;
            }
            else
            {
                sub_40ce2c(&v25);
                if (!(char)v10)
                    break;
            }
        }
        v0 = v24;
        sub_404808();
        if (!(char)v10)
        {
            v26->field_0 = 0;
            v26->field_10 = v16;
            v26->field_14 = 7798785;
            sub_403be8();
        }
        else
        {
            v26->field_0 = 1;
            sub_40d25c(&v25);
            v26->field_30 = v26->field_30 + v26->field_c + 4;
            v64 = 0;
            v65 = 0;
            do
            {
                i = 1;
                idx2 = v64 * 6;
                if (*(8 + (char *)v26->field_1c + 8 * idx2) || *(9 + (char *)v26->field_1c + 8 * idx2) || *((int *)(12 + (char *)v26->field_1c + 8 * idx2)))
                    break;
                v65 += *((int *)(4 + (char *)v26->field_1c + 8 * idx2)) - *((int *)((char *)v26->field_1c + 8 * idx2)) + 1;
                v67 = sub_404654();
                if (v67 > 0)
                {
                    v18 = 1;
                    do
                    {
                        v68 = v67;
                        if (*((int *)((char *)v26->field_1c + 48 * v18)) == *((int *)(4 + (char *)v26->field_1c + 48 * v64)) + 1)
                        {
                            v64 = v18;
                            i = 0;
                            break;
                        }
                    } while ((v18 += 1, v69 = (int)(v68 - 1), v67 = (int)(v68 - 1), v68 != 1));
                }
            } while (!i);
            if (v65 >= 6)
            {
                v26->field_28 = 1;
                v16 = v26->field_4;
                do
                {
                    sub_40c63c();
                    j = &v8;
                    iter = &v10;
                    for (v72 = 9; v72; j += 1)
                    {
                        v72 -= 1;
                        *(iter) = *(j);
                        iter += 1;
                    }
                    if ((*((char *)((void*)&v10 + 5)) || *((char *)((void*)&v10 + 6))) && (v12 || v13) && !v15 && v14 < 4)
                    {
                        v26->field_28 = 0;
                        break;
                    }
                } while (v16 - v26->field_4 < 6);
            }
        }
    }
    else
    {
        v26->field_0 = 0;
        v26->field_10 = v40;
        v26->field_14 = 87;
        sub_409ccc();
        sub_403a64();
    }
    v73 = _ccall(v35, v36, (unsigned int)v37, 0);
    *((struct MEMORY_BASIC_INFORMATION **)v73) = &v9;
    v1 = sub_40d8d6;
    sub_40d8c3();
    return;
}
```

## `sub_0040d8c3` `0x0040d8c3`

_12 bytes. (leaf/helper — see body)_

```c
int sub_40d8c3(void)
{
    return sub_403a10();
}
```

## `sub_0040d8cf` `0x0040d8cf`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40d8cf(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0040d8d4` `0x0040d8d4`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40d8d4(void)
{
    return sub_40d8c3();
}
```

## `sub_0040d8d6` `0x0040d8d6`

_9 bytes. (leaf/helper — see body)_

```c
void sub_40d8d6(unsigned int a0, unsigned int a1)
{
    return;
}
```

## `sub_0040d8df` `0x0040d8df`

_1 bytes. (leaf/helper — see body)_

```c
int sub_40d8df(void)
{
    sub_40d8e0();
    return;
}
```

## `sub_0040d8e0` `0x0040d8e0`

_29 bytes. (leaf/helper — see body)_

```c
int sub_40d8e0(void)
{
    int v1;  // edx
    int v2;  // esi
    int v3;  // ebx

    sub_40d340(v1, 0, 0, 0, 0, v2, v3);
    return;
}
```

## `sub_0040d8fd` `0x0040d8fd`

_3 bytes. (leaf/helper — see body)_

```c
int sub_40d8fd(void)
{
    return sub_40d900();
}
```

## `sub_0040d900` `0x0040d900`

_118 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_4208c8;

int sub_40d900(void)
{
    unsigned long v5;  // ldt
    unsigned long v6;  // gdt
    unsigned short v7;  // fs
    unsigned long v8;  // 4165
    unsigned int v9;  // 4111
    unsigned long v10;  // 4169
    int v11;  // ebx
    unsigned long v12;  // 4120
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x14]
    char v2;  // [bp-0x4]
    char v3;  // [bp+0x0]

    v8 = _ccall(v5, v6, (unsigned int)v7, 0);
    v9 = *((int *)v8);
    v0 = *((int *)v8);
    v10 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int **)v10) = &v0;
    if (!g_4208c8)
    {
        sub_409eac(v9, sub_40d984, &v2, v11, 0, 0, &v3);
        if (!(GetVersion() & 0x80000000))
        {
            sub_409ee0();
            g_4208c8 = GetModuleHandleW(NULL);
        }
        else
        {
            g_4208c8 = sub_4052c4(0);
        }
    }
    v12 = _ccall(v5, v6, (unsigned int)v7, 0);
    *((unsigned int *)v12) = v9;
    v1 = sub_40d98b;
    return sub_40d976(v11, 0, 0, &v3);
}
```

## `sub_0040d976` `0x0040d976`

_14 bytes. (leaf/helper — see body)_

```c
int sub_40d976(void)
{
    return sub_403a34();
}
```

## `sub_0040d984` `0x0040d984`

_5 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_40d984(unsigned int a0, unsigned int a1)
{
    struct_0 *v0;  // [bp+0x0]

    return sub_403374(v0, a0);
}
```

## `sub_0040d989` `0x0040d989`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40d989(void)
{
    return sub_40d976();
}
```

