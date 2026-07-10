# elfbot.dll decompiled — loader 0x00403ccc..0x00404484

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_00403ccc` `0x00403ccc`

_115 bytes. (leaf/helper — see body)_

```c
int sub_403ccc(void)
{
    int v1;  // edx
    int v2;  // ecx
    int v3;  // eax
    int v4;  // edi
    int v5;  // esi
    int v6;  // ebx
    void* v7;  // edi

    if (!v1)
    {
        sub_403a64();
        return;
    }
    else if (!v2)
    {
        sub_403a64();
        return;
    }
    else if (v1 == *((int *)v3))
    {
        sub_403c88();
        return;
    }
    else if (v2 != *((int *)v3))
    {
        sub_403a64(v2, v3);
        sub_403c88();
        return;
    }
    else
    {
        v7 = sub_403ad4(v3, v4, v5, v6);
        sub_402628(v3, v4, v5, v6);
        sub_402628();
        if (v7)
        {
            *((unsigned int *)&v7[8]) = (int)v7[8] - 1;
            sub_403a64();
        }
        else
        {
            sub_403a64();
        }
        return;
    }
}
```

## `sub_00403d3f` `0x00403d3f`

_1 bytes. (leaf/helper — see body)_

```c
void sub_403d3f(void)
{
    return;
}
```

## `sub_00403d40` `0x00403d40`

_128 bytes. (leaf/helper — see body)_

```c
int sub_403d40(void)
{
    void* v4;  // eax
    unsigned int v5;  // edx
    unsigned int v6;  // ebx
    void* v7;  // edi
    void* v8;  // edi
    unsigned int v9;  // edx
    unsigned int v10;  // edx
    unsigned int v11;  // edx
    unsigned int v12;  // ebx
    unsigned int v13;  // ebx
    void* v0;  // [bp-0x18]
    void* v1;  // [bp-0x14]
    int <0x403d40[is_2]|Stack bp, 1 B>;  // [bp+0x0]

    v1 = v4;
    v6 = v5;
    v7 = NULL;
    v8 = NULL;
    if ((&<0x403d40[is_2]|Stack bp, 1 B>)[v5])
    {
        v8 = v7;
        if (*((int *)v4) == (&<0x403d40[is_2]|Stack bp, 1 B>)[v5])
            v8 = v4;
    }
    do
    {
        v10 = v9;
        if ((&<0x403d40[is_2]|Stack bp, 1 B>)[v10] && v8 == (&<0x403d40[is_2]|Stack bp, 1 B>)[v10])
            v8 = NULL;
    } while ((v11 = v10 - 1, v9 = v10 - 1, v10 != 1));
    if (v8)
    {
        sub_403f60();
        v0 = v8;
        v6 -= 1;
    }
    else
    {
        v0 = sub_403ad4();
    }
    do
    {
        v12 = v6;
        if ((&<0x403d40[is_2]|Stack bp, 1 B>)[v12])
            sub_402628();
    } while ((v13 = v12 - 1, v6 = v12 - 1, v12 != 1));
    if (!v8)
    {
        if (v0)
            *((unsigned int *)&v0[8]) = (int)v0[8] - 1;
        sub_403a64();
    }
    goto <0x403d40[is_2]|Stack bp, 1 B>;
}
```

## `sub_00403dc4` `0x00403dc4`

_162 bytes. (leaf/helper — see body)_

```c
int sub_403dc4(void)
{
    void* v2;  // eax
    void* iter;  // esi
    unsigned int v12;  // ecx
    unsigned int v13;  // ebx
    void* v4;  // edx
    void* node;  // edi
    unsigned int v6;  // edx
    unsigned int v7;  // edx
    unsigned int v8;  // ecx
    unsigned int v9;  // ebx
    unsigned int v10;  // edx
    unsigned int v11;  // edx
    unsigned int v0;  // [bp-0x10]

    iter = v2;
    node = v4;
    if (v2 == v4)
    {
        return;
    }
    else if (!iter)
    {
        return;
    }
    else if (node)
    {
        v6 = (int)node[4];
        if ((int)iter[4] <= v6)
            v6 += (int)iter[4] - v6;
        v0 = v6;
        v7 = v6 >> 2;
        if ((v6 & 0xfffffffc))
        {
            do
            {
                v8 = *((int *)iter);
                v9 = *((int *)node);
                if (*((int *)iter) != *((int *)node))
                {
LABEL_403e4d:
                    return;
                }
                v10 = v7 - 1;
                if (v7 == 1)
                {
                    iter += 4;
                    node += 4;
                    break;
                }
                v8 = (int)iter[4];
                v9 = (int)node[4];
                if ((int)iter[4] != (int)node[4])
                    goto LABEL_403e4d;
            } while ((iter += 8, node += 8, v7 = v10 - 1, v10 != 1));
        }
        v11 = v0 & 3;
        if (!((char)v0 & 3))
            return;
        v12 = *((int *)iter);
        v13 = *((int *)node);
        if ((char)v12 != (char)v13)
        {
            return;
        }
        else if (v11 != 1)
        {
            if (*((char *)((void*)&v12 + 1)) != *((char *)((void*)&v13 + 1)))
            {
                return;
            }
            else if (v11 != 2 && (v12 & 0xff0000) != (v13 & 0xff0000))
            {
                return;
            }
        }
        return;
    }
    else
    {
        return;
    }
}
```

## `sub_00403e66` `0x00403e66`

_2 bytes. (leaf/helper — see body)_

```c
int sub_403e66(void)
{
    sub_403e68();
    return;
}
```

## `sub_00403e68` `0x00403e68`

_15 bytes. (leaf/helper — see body)_

```c
int sub_403e68(void)
{
    void* v1;  // eax
    unsigned int v2;  // 4107
    unsigned int v3;  // 4113

    if (v1)
    {
        v2 = _ccall(15, v1, 0, 0);
        v3 = _ccall(14, 18, (int)v1[8] + 1, 0, v2);
        if (!((char)v3))
            InterlockedIncrement(v1 - 8);
    }
    return;
}
```

## `sub_00403e77` `0x00403e77`

_1 bytes. (leaf/helper — see body)_

```c
int sub_403e77(void)
{
    sub_403e78();
    return;
}
```

## `sub_00403e78` `0x00403e78`

_11 bytes. (leaf/helper — see body)_

```c
int sub_403e78(void)
{
    return;
}
```

## `sub_00403e7d` `0x00403e7d`

_1 bytes. (leaf/helper — see body)_

```c
void sub_403e7d(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_00403e84` `0x00403e84`

_65 bytes. (leaf/helper — see body)_

```c
int sub_403e84(void)
{
    void* *v1;  // eax
    int v2;  // ebx
    unsigned int v11;  // 4116
    void* v3;  // eax
    void* v4;  // eax
    void* v5;  // eax
    unsigned int v6;  // cc_op
    unsigned int v7;  // cc_dep1
    unsigned int v8;  // cc_dep2
    unsigned int v9;  // cc_ndep
    unsigned int v10;  // 4110

    if (!*(v1))
    {
        return;
    }
    else if ((int)(*(v1))[8] != 1)
    {
        v3 = sub_403ad4(v2);
        v4 = *(v1);
        *(v1) = v3;
        sub_402628(v4);
        v5 = v4;
        v10 = _ccall(v6, v7, v8, v9);
        v11 = _ccall(12, 21, (int)v5[8] - 1, 0, v10);
        if ((char)v11)
            return;
        InterlockedDecrement(v5 - 8);
        if ((int)v5[8] == 1)
            sub_402524();
        return;
    }
    else
    {
        return;
    }
}
```

## `sub_00403ec5` `0x00403ec5`

_3 bytes. (leaf/helper — see body)_

```c
int sub_403ec5(void)
{
    return sub_403ec8();
}
```

## `sub_00403ec8` `0x00403ec8`

_5 bytes. (leaf/helper — see body)_

```c
int sub_403ec8(void)
{
    sub_403e84();
    return;
}
```

## `sub_00403ecd` `0x00403ecd`

_1 bytes. (leaf/helper — see body)_

```c
void sub_403ecd(void)
{
    return;
}
```

## `sub_00403ece` `0x00403ece`

_2 bytes. (leaf/helper — see body)_

```c
int sub_403ece(void)
{
    return sub_403ed0();
}
```

## `sub_00403ed0` `0x00403ed0`

_5 bytes. (leaf/helper — see body)_

```c
int sub_403ed0(void)
{
    sub_403e84();
    return;
}
```

## `sub_00403ed5` `0x00403ed5`

_1 bytes. (leaf/helper — see body)_

```c
void sub_403ed5(void)
{
    return;
}
```

## `sub_00403ed6` `0x00403ed6`

_2 bytes. (leaf/helper — see body)_

```c
int sub_403ed6(void)
{
    sub_403ed8();
    return;
}
```

## `sub_00403ed8` `0x00403ed8`

_63 bytes. (leaf/helper — see body)_

```c
int sub_403ed8(void)
{
    void* v2;  // eax
    int v3;  // ebx
    unsigned int v4;  // 4103
    int v5;  // edx
    int v6;  // edx
    unsigned int v7;  // 4109
    int v8;  // ecx
    int v0;  // [bp-0x4]

    if (v2 && (v3 = (int)v2[4], v3))
    {
        v4 = _ccall(15, v3, 0, 0);
        v6 = v5 - 1;
        v7 = _ccall(12, 21, v5 - 1, 0, v4);
        if ((char)v7)
        {
            v6 = 0;
LABEL_403eeb:
            if (v8 >= 0)
            {
                sub_403b00();
                return;
            }
        }
        else if (v6 < v3)
        {
            goto LABEL_403eeb;
        }
    }
    sub_403a10(v0);
    return;
}
```

## `sub_00403f17` `0x00403f17`

_1 bytes. (leaf/helper — see body)_

```c
void sub_403f17(void)
{
    return;
}
```

## `sub_00403f18` `0x00403f18`

_72 bytes. (leaf/helper — see body)_

```c
int sub_403f18(void)
{
    void* *v4;  // eax
    void* v5;  // edx
    unsigned int v6;  // 4107
    int v7;  // edx
    int v8;  // esi
    unsigned int v9;  // 4113
    int v10;  // ecx
    int v0;  // [bp-0xc]
    int v1;  // [bp-0x8]
    int v2;  // [bp-0x4]

    sub_403ec8(v0, v1, v2);
    v5 = *(v4);
    if (!v5)
        return;
    v6 = _ccall(15, v5, 0, 0);
    v8 = v7 - 1;
    v9 = _ccall(12, 21, v7 - 1, 0, v6);
    if ((char)v9)
    {
        return;
    }
    else if (v8 >= (int)v5[4])
    {
        return;
    }
    else if (v10 > NULL)
    {
        sub_402628();
        sub_403f60();
        return;
    }
    else
    {
        return;
    }
}
```

## `sub_00403f60` `0x00403f60`

_98 bytes. (leaf/helper — see body)_

```c
int sub_403f60(void)
{
    void* v4;  // edi
    int v5;  // edx
    void* *v6;  // eax
    void* v7;  // eax
    void* v8;  // eax
    int v0;  // [bp-0xc]
    int v1;  // [bp-0x8]
    int v2;  // [bp-0x4]

    v4 = NULL;
    if (v5 > 0)
    {
        v7 = *(v6);
        if (v7 && (int)v7[8] == 1)
        {
            sub_402544(v7 - 8);
            v8 = v7;
            *(v6) = v8;
            *((int *)&v8[4]) = v5;
            *(v5 + (char *)v8) = 0;
            return;
        }
        v4 = sub_403ad4();
        if (*(v6))
            sub_402628();
    }
    sub_403a10(v0, v1, v2);
    *(v6) = v4;
    return;
}
```

## `sub_00403fc2` `0x00403fc2`

_9 bytes. (leaf/helper — see body)_

```c
char sub_403fc2(void)
{
    return sub_4025ec();
}
```

## `sub_00403fcb` `0x00403fcb`

_1 bytes. (leaf/helper — see body)_

```c
void sub_403fcb(void)
{
    return;
}
```

## `sub_00403fcc` `0x00403fcc`

_21 bytes. (leaf/helper — see body)_

```c
int sub_403fcc(void)
{
    BSTR *v2;  // eax
    unsigned int v3;  // edx
    BSTR *v0;  // [bp-0x4]

    v3 = *(v2);
    if (v3)
    {
        *(v2) = 0;
        v0 = v2;
        SysFreeString(v3);
    }
    return;
}
```

## `sub_00403fe1` `0x00403fe1`

_3 bytes. (leaf/helper — see body)_

```c
int sub_403fe1(void)
{
    sub_403fe4();
    return;
}
```

## `sub_00403fe4` `0x00403fe4`

_33 bytes. (leaf/helper — see body)_

```c
int sub_403fe4(void)
{
    unsigned int *v1;  // eax
    unsigned int *iter;  // ebx
    unsigned int v3;  // edx
    unsigned int v4;  // esi
    unsigned int v5;  // esi
    unsigned int v6;  // eax
    unsigned int v7;  // esi

    iter = v1;
    v4 = v3;
    do
    {
        v5 = v4;
        v6 = *(iter);
        if (v6)
        {
            *(iter) = 0;
            SysFreeString(v6);
        }
    } while ((iter += 4, v7 = v5 - 1, v4 = v5 - 1, v5 != 1));
    return;
}
```

## `sub_00404005` `0x00404005`

_3 bytes. (leaf/helper — see body)_

```c
int sub_404005(unsigned int a0, unsigned int a1)
{
    return sub_404008();
}
```

## `sub_00404008` `0x00404008`

_36 bytes. (leaf/helper — see body)_

```c
int sub_404008(void)
{
    void* v1;  // edx
    BSTR *v2;  // eax

    if (!v1)
    {
        sub_403fcc();
        return;
    }
    if (((int)v1[4] & 4294967294))
        if (!SysReAllocStringLen(v2, v1, (int)v1[4] >> 1))
            goto LABEL_0x403fc4;
        else
            goto LABEL_0x40402b;
    else
        sub_403fcc();
    return;
}
```

## `sub_0040402c` `0x0040402c`

_47 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[1];
    char field_1;
} struct_0;

int sub_40402c(void)
{
    struct_0 *v4;  // edx
    unsigned int v5;  // ecx
    unsigned int v6;  // esi
    unsigned int v7;  // edi
    unsigned int v8;  // edi
    unsigned int v9;  // esi
    unsigned int v12;  // 4117
    int v0;  // [bp-0xc]
    int v1;  // [bp-0x8]
    int v2;  // [bp-0x4]

    v5 = v4->field_1;
    v6 = &(v4->padding_0)[v5 + 10];
    v7 = *((int *)&(v4[3].padding_0)[v5]);
    do
    {
        v8 = v7;
        v9 = v6;
        sub_40405c(v0, v1, v2);
        v12 = _ccall(14, 21, v8 - 1, 0, (unsigned int)(char)(v9 + 8 < v9));
        v6 = v9 + 8;
        v7 = v8 - 1;
    } while (!((char)v12));
    return;
}
```

## `sub_0040405b` `0x0040405b`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40405b(unsigned int a0)
{
    sub_40405c();
    return;
}
```

## `sub_0040405c` `0x0040405c`

_147 bytes. (leaf/helper — see body)_

```c
int sub_40405c(void)
{
    unsigned int v4;  // ecx
    unsigned int v5;  // ebx
    unsigned int v14;  // cc_op
    unsigned int v15;  // cc_dep1
    unsigned int v16;  // cc_dep2
    unsigned int v17;  // cc_ndep
    unsigned int v18;  // 4103
    unsigned int v20;  // 4109
    unsigned int v21;  // edi
    unsigned int v6;  // esi
    unsigned int v22;  // 4103
    unsigned int v24;  // 4109
    unsigned int v27;  // 4131
    unsigned int v7;  // edi
    unsigned int v30;  // 4119
    void* v8;  // eax
    void* ptr;  // ebx
    unsigned int v10;  // edi
    char *v11;  // edx
    char v12;  // al
    unsigned int v13;  // edi
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]
    unsigned int v2;  // [bp-0x4]

    if (!v4)
        return;
    v2 = v5;
    v1 = v6;
    v0 = v7;
    ptr = v8;
    v10 = v4;
    v12 = *(v11);
    if (!(*(v11) != 10 && v12 != 11))
    {
        do
        {
LABEL_40409c:
            *((unsigned int *)ptr) = 0;
            v30 = _ccall(14, 21, v10 - 1, 0, (unsigned int)(char)(ptr + 4 < ptr));
            ptr += 4;
            v10 -= 1;
        } while (!((char)v30));
    }
    else if (v12 == 12)
    {
        do
        {
            memset(ptr, 0, 16);
            v27 = _ccall(14, 21, v10 - 1, 0, (unsigned int)(char)(ptr + 16 < ptr));
            ptr += 16;
            v10 -= 1;
        } while (!((char)v27));
    }
    else if (v12 == 13)
    {
        do
        {
            v21 = v10;
            sub_40405c(/* unsupported instruction */);
            v22 = _ccall(v14, v15, v16, v17);
            v24 = _ccall(14, 21, v21 - 1, 0, v22);
            v10 = v21 - 1;
        } while (!((char)v24));
    }
    else if (v12 != 14)
    {
        if (v12 != 15 && v12 != 0x11)
        {
            sub_4025ec();
            return;
        }
        goto LABEL_40409c;
    }
    else
    {
        do
        {
            v13 = v10;
            sub_40402c(/* unsupported instruction */);
            v18 = _ccall(v14, v15, v16, v17);
            v20 = _ccall(14, 21, v13 - 1, 0, v18);
            v10 = v13 - 1;
        } while (!((char)v20));
    }
    return;
}
```

## `sub_004040ef` `0x004040ef`

_1 bytes. (leaf/helper — see body)_

```c
int sub_4040ef(void)
{
    sub_4040f0();
    return;
}
```

## `sub_004040f0` `0x004040f0`

_49 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[1];
    char field_1;
} struct_0;

int sub_4040f0(void)
{
    struct_0 *v4;  // edx
    unsigned int v5;  // ecx
    unsigned int v6;  // esi
    unsigned int v7;  // edi
    unsigned int v8;  // edi
    unsigned int v9;  // esi
    unsigned int v12;  // 4117
    int v0;  // [bp-0xc]
    int v1;  // [bp-0x8]
    int v2;  // [bp-0x4]

    v5 = v4->field_1;
    v6 = &(v4->padding_0)[v5 + 10];
    v7 = *((int *)&(v4[3].padding_0)[v5]);
    do
    {
        v8 = v7;
        v9 = v6;
        sub_404124(v0, v1, v2);
        v12 = _ccall(14, 21, v8 - 1, 0, (unsigned int)(char)(v9 + 8 < v9));
        v6 = v9 + 8;
        v7 = v8 - 1;
    } while (!((char)v12));
    return;
}
```

## `sub_00404121` `0x00404121`

_3 bytes. (leaf/helper — see body)_

```c
int sub_404121(unsigned int a0)
{
    return sub_404124();
}
```

## `sub_00404124` `0x00404124`

_234 bytes. (leaf/helper — see body)_

```c
int sub_404124(void)
{
    int v5;  // ecx
    unsigned int v6;  // eax
    unsigned int v14;  // cc_dep1
    unsigned int v15;  // cc_dep2
    unsigned int v16;  // cc_ndep
    unsigned int v17;  // 4103
    unsigned int v19;  // 4109
    int v20;  // edi
    unsigned int v21;  // cc_op
    unsigned int v7;  // ebx
    unsigned int v22;  // 4103
    unsigned int v24;  // 4109
    int v25;  // edi
    unsigned int v26;  // 4103
    unsigned int v8;  // esi
    unsigned int v28;  // 4109
    int v29;  // edi
    unsigned int v30;  // 4103
    unsigned int v32;  // 4109
    unsigned int v9;  // edi
    int v33;  // edi
    unsigned int v34;  // 4103
    unsigned int v36;  // 4109
    int v10;  // edi
    char *v11;  // edx
    char v12;  // al
    int v13;  // edi
    unsigned int v0;  // [bp-0x10]
    unsigned int v1;  // [bp-0xc]
    unsigned int v2;  // [bp-0x8]
    unsigned int v3;  // [bp-0x4]

    if (!v5)
        return;
    v3 = v6;
    v2 = v7;
    v1 = v8;
    v0 = v9;
    v10 = v5;
    v12 = *(v11);
    if (*(v11) != 10)
    {
        if (v12 != 11)
        {
            if (v12 == 12)
            {
                do
                {
                    v33 = v10;
                    sub_404484();
                    v34 = _ccall(v21, v14, v15, v16);
                    v36 = _ccall(14, 21, v33 - 1, 0, v34);
                    v10 = v33 - 1;
                } while (!((char)v36));
            }
            else if (v12 == 13)
            {
                do
                {
                    v29 = v10;
                    sub_404124(/* unsupported instruction */);
                    v30 = _ccall(v21, v14, v15, v16);
                    v32 = _ccall(14, 21, v29 - 1, 0, v30);
                    v10 = v29 - 1;
                } while (!((char)v32));
            }
            else if (v12 == 14)
            {
                do
                {
                    v25 = v10;
                    sub_4040f0(/* unsupported instruction */);
                    v26 = _ccall(v21, v14, v15, v16);
                    v28 = _ccall(14, 21, v25 - 1, 0, v26);
                    v10 = v25 - 1;
                } while (!((char)v28));
            }
            else if (v12 == 15)
            {
                do
                {
                    v20 = v10;
                    sub_404e00();
                    v22 = _ccall(v21, v14, v15, v16);
                    v24 = _ccall(14, 21, v20 - 1, 0, v22);
                    v10 = v20 - 1;
                } while (!((char)v24));
            }
            else if (v12 == 0x11)
            {
                do
                {
                    v13 = v10;
                    sub_404814();
                    v17 = _ccall(v21, v14, v15, v16);
                    v19 = _ccall(14, 21, v13 - 1, 0, v17);
                    v10 = v13 - 1;
                } while (!((char)v19));
            }
            else
            {
                sub_4025ec();
                return;
            }
        }
        else
        {
            if (v5 <= 1)
                sub_403fcc();
            else
                sub_403fe4();
        }
    }
    else
    {
        if (v5 <= 1)
            sub_403a10();
        else
            sub_403a34();
    }
    return;
}
```

## `sub_0040420e` `0x0040420e`

_2 bytes. (leaf/helper — see body)_

```c
int sub_40420e(void)
{
    return sub_404210();
}
```

## `sub_00404210` `0x00404210`

_10 bytes. (leaf/helper — see body)_

```c
void sub_404210(void)
{
    sub_404124();
    return;
}
```

## `sub_0040421a` `0x0040421a`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40421a(void)
{
    return;
}
```

## `sub_0040421b` `0x0040421b`

_1 bytes. (leaf/helper — see body)_

```c
int sub_40421b(void)
{
    sub_40421c();
    return;
}
```

## `sub_0040421c` `0x0040421c`

_282 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[1];
    char field_1;
} struct_0;

typedef struct struct_2 {
    char padding_0[2];
    unsigned int field_2;
    unsigned int field_6;
    struct struct_3 *field_a;
    int field_e;
} struct_2;

typedef struct struct_3 {
    struct struct_1 *field_0;
} struct_3;

typedef struct struct_1 {
    char field_0;
    char field_1;
} struct_1;

int sub_40421c(void)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // esi
    unsigned int v16;  // eax
    unsigned int v17;  // ecx
    unsigned int v18;  // ebp
    unsigned int v8;  // edi
    struct_0 *v9;  // ecx
    struct_2 *iter;  // edi
    unsigned int v11;  // ebp
    int v12;  // eax
    unsigned int i;  // ebp
    char v14[2];  // edx
    char v15;  // cl
    int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]
    unsigned int v4;  // [bp-0x4]

    v4 = v6;
    v3 = v7;
    v2 = v8;
    iter = &(v9->padding_0)[v9->field_1 + 10];
    v11 = iter->field_2;
    v12 = 0;
    v1 = iter->field_6;
    do
    {
        i = v11;
        if (iter->field_2 > v12)
            sub_402628();
        v14 = *((int *)*((int *)iter->padding_0));
        v15 = v14[0];
        if (v14[0] == 10)
        {
            sub_403a64();
            v16 = 4;
        }
        else if (v15 == 11)
        {
            sub_404008();
            v16 = 4;
        }
        else if (v15 == 12)
        {
            sub_404474();
            v16 = 16;
        }
        else if (v15 == 13)
        {
            v17 = v14[1];
            v16 = *((int *)&v14[3 + v17]);
            sub_404338(*((int *)&v14[3 + v17]), *((int *)&v14[1 + v17]));
        }
        else if (v15 == 14)
        {
            v16 = *((int *)&v14[1 + v14[1]]);
            sub_40421c(*((int *)&v14[1 + v14[1]]));
        }
        else if (v15 != 15)
        {
            if (v15 != 0x11)
            {
                sub_4025ec();
                return;
            }
            sub_404850();
            v16 = 4;
        }
        else
        {
            sub_404e18();
            v16 = 4;
        }
        v12 = v16 + iter->field_2;
        iter = &iter->field_6;
        v18 = i - 1;
        v11 = v18;
    } while (i != 1);
    if (v0 > v12)
        sub_402628();
    return;
}
```

## `sub_00404336` `0x00404336`

_2 bytes. (leaf/helper — see body)_

```c
int sub_404336(void)
{
    sub_404338();
    return;
}
```

## `sub_00404338` `0x00404338`

_242 bytes. (leaf/helper — see body)_

```c
int sub_404338(void)
{
    unsigned int v1;  // ebp
    char v2[2];  // ecx
    unsigned int v11;  // ebp
    unsigned int k;  // ebp
    unsigned int v13;  // ebp
    unsigned int j;  // ebp
    unsigned int v15;  // ebp
    unsigned int i;  // ebp
    int v17;  // edi
    int v18;  // esi
    int v19;  // ebx
    unsigned int v20;  // ebp
    char v3;  // cl
    unsigned int i0;  // ebp
    unsigned int v5;  // ebp
    unsigned int n;  // ebp
    unsigned int v7;  // ebp
    unsigned int m;  // ebp
    unsigned int v9;  // ebp
    unsigned int l;  // ebp
    unsigned int v0;  // [bp+0x4]

    v1 = v0;
    v3 = v2[0];
    if (v2[0] == 10)
    {
        do
        {
            i = v1;
            sub_403a64(/* unsupported instruction */, v17, v18, v19);
            v20 = i - 1;
            v1 = v20;
        } while (i != 1);
        return;
    }
    else if (v3 == 11)
    {
        do
        {
            j = v1;
            sub_404008();
            v15 = j - 1;
            v1 = v15;
        } while (j != 1);
        return;
    }
    else if (v3 == 12)
    {
        do
        {
            k = v1;
            sub_404474();
            v13 = k - 1;
            v1 = v13;
        } while (k != 1);
        return;
    }
    else if (v3 == 13)
    {
        do
        {
            l = v1;
            sub_404338(*((int *)&v2[3 + v2[1]]));
            v11 = l - 1;
            v1 = v11;
        } while (l != 1);
        return;
    }
    else if (v3 == 14)
    {
        do
        {
            m = v1;
            sub_40421c();
            v9 = m - 1;
            v1 = v9;
        } while (m != 1);
        return;
    }
    else if (v3 == 15)
    {
        do
        {
            n = v1;
            sub_404e18();
            v7 = n - 1;
            v1 = v7;
        } while (n != 1);
        return;
    }
    else if (v3 != 0x11)
    {
        sub_4025ec();
        return;
    }
    else
    {
        do
        {
            i0 = v1;
            sub_404850();
            v5 = i0 - 1;
            v1 = v5;
        } while (i0 != 1);
        return;
    }
}
```

## `sub_0040442a` `0x0040442a`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40442a(void)
{
    return;
}
```

## `sub_0040442b` `0x0040442b`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40442b(void)
{
    sub_40442c();
    return;
}
```

## `sub_0040442c` `0x0040442c`

_7 bytes. (leaf/helper — see body)_

```c
char sub_40442c(void)
{
    return sub_4025ec();
}
```

## `sub_00404433` `0x00404433`

_1 bytes. (leaf/helper — see body)_

```c
void sub_404433(void)
{
    return;
}
```

## `sub_00404434` `0x00404434`

_21 bytes. (leaf/helper — see body)_

```c
int sub_404434(void)
{
    unsigned short *v1;  // eax

    if (*(v1) >= 2 && *(v1) != 10)
        sub_40442c();
    return;
}
```

## `sub_00404449` `0x00404449`

_3 bytes. (leaf/helper — see body)_

```c
int sub_404449(void)
{
    return sub_40444c();
}
```

## `sub_0040444c` `0x0040444c`

_31 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420658;

int sub_40444c(void)
{
    unsigned int idx;  // eax

    idx = 0;
    do
    {
        (&g_420658)[idx] = sub_40442c;
        idx += 1;
    } while (idx != 43);
    g_420658 = sub_404434;
    return sub_404434;
}
```

## `sub_0040446b` `0x0040446b`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40446b(void)
{
    sub_40446c();
    return;
}
```

## `sub_0040446c` `0x0040446c`

_6 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420658;

void sub_40446c(void)
{
    goto g_420658;
}
```

## `sub_00404472` `0x00404472`

_1 bytes. (leaf/helper — see body)_

```c
void sub_404472(void)
{
    return;
}
```

## `sub_00404473` `0x00404473`

_1 bytes. (leaf/helper — see body)_

```c
void sub_404473(void)
{
    sub_404474();
    return;
}
```

## `sub_00404474` `0x00404474`

_6 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_42065c;

void sub_404474(void)
{
    goto g_42065c;
}
```

## `sub_0040447a` `0x0040447a`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40447a(void)
{
    return;
}
```

## `sub_0040447b` `0x0040447b`

_1 bytes. (leaf/helper — see body)_

```c
void sub_40447b(void)
{
    sub_40447c();
    return;
}
```

## `sub_0040447c` `0x0040447c`

_6 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_420684;

void sub_40447c(void)
{
    goto g_420684;
}
```

## `sub_00404482` `0x00404482`

_1 bytes. (leaf/helper — see body)_

```c
void sub_404482(void)
{
    return;
}
```

## `sub_00404483` `0x00404483`

_1 bytes. (leaf/helper — see body)_

```c
void sub_404483(void)
{
    sub_404484();
    return;
}
```

## `sub_00404484` `0x00404484`

_8 bytes. (leaf/helper — see body)_

```c
int sub_404484(void)
{
    sub_40446c();
    return;
}
```

