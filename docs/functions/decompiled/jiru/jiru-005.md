# elfbot.dll decompiled — jiru 0x102f62a0..0x102f7bc0

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_102f62a0` `0x102f62a0`

_165 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7f4;
extern unsigned int g_1038c7f8;

unsigned int sub_102f62a0(int a0)
{
    unsigned int v6;  // edx
    unsigned int v7;  // ebx
    unsigned int v9;  // eax
    unsigned short v10;  // bx
    unsigned int v11;  // eax
    unsigned int v12;  // eax
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102efd90(a0);
    v2 = v6;
    v1 = v7;
    v0 = v4 & 0xffff;
    v9 = _INSERT(v0, 1, 0);
    v10 = _INSERT(_INSERT(*((unsigned short *)((void*)&v7 + 1)), 1, 0), 0, 65);
    v11 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v12 = _INSERT((char)v11 * 0 | (char)(v11 >> 24), 0, ((char)v11 * 0 | (char)(v11 >> 24)) & (char)~(~(v10)));
    v3 = -(-(0 < v12));
    v5 = (g_1038c7f4 ^ g_1038c7f8) * 2;
    if (v3)
        v5 |= 1;
    return sub_102efcf0(v5);
}
```

## `sub_102f6350` `0x102f6350`

_160 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c840;
extern unsigned int g_1038c844;

unsigned int sub_102f6350(int a0)
{
    unsigned int v6;  // edx
    unsigned int v7;  // ebx
    unsigned int v9;  // eax
    unsigned short v10;  // bx
    unsigned int v11;  // eax
    unsigned int v12;  // eax
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f2940(a0);
    v2 = v6;
    v1 = v7;
    v0 = v4 & 0xffff;
    v9 = _INSERT(v0, 1, 0);
    v10 = _INSERT(_INSERT(*((unsigned short *)((void*)&v7 + 1)), 1, 0), 0, 128);
    v11 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v12 = _INSERT((char)v11 * 0 | (char)(v11 >> 24), 0, ((char)v11 * 0 | (char)(v11 >> 24)) & (char)~(~(v10)));
    v3 = -(0 < v12) + 1;
    v5 = (g_1038c840 ^ g_1038c844) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f27b0(v5);
}
```

## `sub_102f63f0` `0x102f63f0`

_189 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c800;
extern unsigned int g_1038c804;

int sub_102f63f0(unsigned int a0)
{
    unsigned short v6;  // ax
    unsigned int v7;  // edx
    unsigned int v16;  // 4146
    unsigned int v19;  // 4141
    unsigned int v22;  // 4140
    unsigned int v8;  // cc_dep1
    unsigned int v9;  // ebx
    char v10;  // bl
    unsigned int v11;  // 4130
    unsigned int v12;  // 4142
    unsigned int v13;  // 4144
    unsigned int v14;  // cc_ndep
    unsigned int v15;  // cc_dep1
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f04d0(a0);
    v6 = v4;
    v2 = v7;
    v8 = v6;
    v1 = v9;
    v0 = 0x1e00;
    v10 = v0;
    v11 = _ccall(0, 15, (unsigned int)v6, 0, 0);
    v0 = v6;
    v12 = _ccall(19, (unsigned int)(v10 - 5), 0, (unsigned int)(char)(v10 < 4));
    v13 = _ccall(19, (unsigned int)(v10 - 6), 0, v12);
    v14 = v13;
    v15 = v10 - 7;
    v16 = _ccall(0, 19, (unsigned int)(v10 - 7), 0, v13);
    v19 = _ccall(0, 19, 0x11, 0, 0);
    v22 = _ccall(0, 4, 6, 2, 0);
    v3 = -(0 < _INSERT(_INSERT(v0, 1, *((char *)((void*)&v0 + 1)) & v10 - 30) & 0xff, 0, (char)_INSERT(v0, 1, *((char *)((void*)&v0 + 1)) & v10 - 30) & 4)) + 1;
    v5 = (g_1038c800 ^ g_1038c804) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0430(v5);
}
```

## `sub_102f641f` `0x102f641f`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f641f(void)
{
}
```

## `sub_102f6436` `0x102f6436`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f6436(void)
{
}
```

## `sub_102f6458` `0x102f6458`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f6458(void)
{
}
```

## `sub_102f6474` `0x102f6474`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f6474(void)
{
}
```

## `sub_102f64c0` `0x102f64c0`

_382 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c844;
extern unsigned int g_1038c848;

unsigned int sub_102f64c0(int a0)
{
    unsigned int v8;  // ebx
    unsigned int v9;  // ecx
    unsigned int v19;  // eax
    unsigned int v20;  // eax
    unsigned short v21;  // ax
    unsigned int v22;  // cc_dep1
    unsigned int v23;  // 4506
    unsigned int v25;  // eax
    char v11;  // cl
    unsigned int v13;  // edx
    unsigned int v15;  // ecx
    unsigned int v16;  // ecx
    unsigned int v17;  // eax
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]

    v4 = v8;
    v6 = sub_102f2b60(a0);
    v3 = v9;
    v11 = (char)(~(~(12)) + 0x11) + 3;
    v2 = v13;
    if (!(__buildin_bswap32(v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & _INSERT(v11 + 13, 0, v11 + 18) + 14))
    {
        v4 = v8;
        v3 = v9;
        v15 = _INSERT(_INSERT(v9, 1, 0), 0, 164);
        v16 = v15 * 0x1000000 | v15 * 0x100 & 0xff0000 | v15 >> 8 & 0xff00 | v15 >> 24 & 0xff;
        v17 = _INSERT(_INSERT(v6 & 0xffff, 1, 0) & 0xff, 0, ~(~((char)_INSERT(v6 & 0xffff, 1, 0))));
        v19 = v17 * 0x1000000 | v17 * 0x100 & 0xff0000 | v17 >> 8 & 0xff00 | v17 >> 24 & 0xff;
        v20 = _INSERT((char)v19 * 0 | (char)(v19 >> 24), 0, ((char)v19 * 0 | (char)(v19 >> 24)) & (char)~(~(_INSERT((char)v16 * 0 | (char)(v16 >> 24), 0, ((char)v16 * 0 | (char)(v16 >> 24)) - 39))) + 3);
        v4 = -(0 < v20) + 1;
        v21 = v6;
        v3 = v8;
        v22 = v21;
        v2 = v8;
        v0 = 31;
        v23 = _ccall(0, 15, (unsigned int)v21, 0, 0);
        v1 = v21;
        if (-(0 < v20) + 1 != -(0 < _INSERT((char)v1 & (char)v0 - 31, 1, (char)v1 & (char)v0 - 31 & 243)) + 1)
            goto LABEL_102f6609;
        v25 = 1;
    }
    else
    {
LABEL_102f6609:
        v25 = 0;
    }
    v5 = v25;
    v7 = (g_1038c844 ^ g_1038c848) * 2;
    if (v5)
        v7 |= 1;
    return sub_102f2ad0(v7);
}
```

## `sub_102f65c3` `0x102f65c3`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f65c3(void)
{
}
```

## `sub_102f6650` `0x102f6650`

_147 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c800;
extern unsigned int g_1038c804;

int sub_102f6650(unsigned int a0)
{
    unsigned int v4;  // edx
    unsigned int v5;  // 4141
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v2 = sub_102f04d0(a0);
    v0 = v4;
    v5 = _ccall(0, 4, 14, 0xff, 0);
    v1 = -(0 < _INSERT(_INSERT(v2, 1, 0) & 0xff, 0, (char)_INSERT(v2, 1, 0) & 1)) + 1;
    v3 = (g_1038c800 ^ g_1038c804) * 2;
    if (v1)
        v3 |= 1;
    return sub_102f0430(v3);
}
```

## `sub_102f667d` `0x102f667d`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f667d(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f66f0` `0x102f66f0`

_176 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c80c;
extern unsigned int g_1038c810;

unsigned int sub_102f66f0(int a0)
{
    unsigned int v6;  // edx
    unsigned int v7;  // ebx
    unsigned int v9;  // eax
    unsigned short v10;  // bx
    unsigned int v11;  // eax
    unsigned int v12;  // eax
    unsigned int v0;  // [bp-0x28]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f0940(a0);
    v2 = v6;
    v1 = v7;
    v0 = v4 & 0xffff;
    v9 = _INSERT(v0, 1, 0);
    v10 = _INSERT(_INSERT(*((unsigned short *)((void*)&v7 + 1)), 1, 0), 0, 65);
    v11 = v9 * 0x1000000 | v9 * 0x100 & 0xff0000 | v9 >> 8 & 0xff00 | v9 >> 24 & 0xff;
    v12 = _INSERT((char)v11 * 0 | (char)(v11 >> 24), 0, ((char)v11 * 0 | (char)(v11 >> 24)) & (char)~(~(v10)));
    v3 = -(-(0 < v12));
    v5 = (g_1038c80c ^ g_1038c810) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0850(v5);
}
```

## `sub_102f67a0` `0x102f67a0`

_174 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7f8;
extern unsigned int g_1038c7fc;

int sub_102f67a0(unsigned int a0)
{
    unsigned int v5;  // ecx
    unsigned int v6;  // eax
    char v7;  // cl
    unsigned int v8;  // ecx
    unsigned int v9;  // edx
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v3 = sub_102effb0(a0);
    v1 = v5;
    v6 = v3 * 0x1000000 | v3 * 0x100 & 0xff0000 | v3 >> 8 & 0xff00 | v3 >> 24 & 0xff;
    v7 = (char)(~(~(75)) + 15) + 7;
    v8 = _INSERT(v7 + 13, 0, v7 - -14);
    v0 = v9;
    v2 = -(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 0x11)) + 1;
    v4 = (g_1038c7f8 ^ g_1038c7fc) * 2;
    if (!(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 0x11)) != 4294967295)
        v4 |= 1;
    return sub_102efe30(v4);
}
```

## `sub_102f6850` `0x102f6850`

_150 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e4;
extern unsigned int g_1038c7e8;

unsigned int sub_102f6850(int a0)
{
    unsigned short v7;  // ax
    unsigned int v8;  // edx
    unsigned int v9;  // cc_dep1
    unsigned int v10;  // ebx
    unsigned int v11;  // 4130
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v5 = sub_102ef460(a0);
    v7 = v5;
    v3 = v8;
    v9 = v7;
    v2 = v10;
    v0 = 0xd00;
    v11 = _ccall(0, 15, (unsigned int)v7, 0, 0);
    v1 = v7;
    v4 = -(0 < _INSERT(_INSERT(v1, 1, *((char *)((void*)&v1 + 1)) & (char)v0 - 13) & 0xff, 0, (char)_INSERT(v1, 1, *((char *)((void*)&v1 + 1)) & (char)v0 - 13) & 4)) + 1;
    v6 = (g_1038c7e4 ^ g_1038c7e8) * 2;
    if (v4)
        v6 |= 1;
    return sub_102ef3a0(v6);
}
```

## `sub_102f687f` `0x102f687f`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f687f(void)
{
}
```

## `sub_102f68f0` `0x102f68f0`

_126 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c838;
extern unsigned int g_1038c83c;

int sub_102f68f0(unsigned int a0)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // eax
    unsigned int v8;  // ecx
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v2 = v6;
    v4 = sub_102f2420(a0);
    v1 = v6;
    v7 = v4 * 0x1000000 | v4 * 0x100 & 0xff0000 | v4 >> 8 & 0xff00 | v4 >> 24 & 0xff;
    v0 = v8;
    v3 = -(-(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & ~(~(50)) + 14)));
    v5 = (g_1038c838 ^ g_1038c83c) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f22d0(v5);
}
```

## `sub_102f6912` `0x102f6912`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102f6912(void)
{
}
```

## `sub_102f6980` `0x102f6980`

_264 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7f0;
extern unsigned int g_1038c7f4;

unsigned int sub_102f6980(int a0)
{
    unsigned int v5;  // ebx
    unsigned int v6;  // ecx
    unsigned int v16;  // 4600
    unsigned int v8;  // ecx
    unsigned int v9;  // ecx
    unsigned int v10;  // eax
    unsigned int v12;  // eax
    unsigned int v13;  // eax
    int v14;  // edx
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x10]
    int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v3 = sub_102efba0(a0);
    v1 = v5;
    v0 = v6;
    v8 = _INSERT(_INSERT(v6, 1, 0), 0, 164);
    v9 = v8 * 0x1000000 | v8 * 0x100 & 0xff0000 | v8 >> 8 & 0xff00 | v8 >> 24 & 0xff;
    v10 = _INSERT(_INSERT(v3 & 0xffff, 1, 0) & 0xff, 0, ~(~((char)_INSERT(v3 & 0xffff, 1, 0))));
    v12 = v10 * 0x1000000 | v10 * 0x100 & 0xff0000 | v10 >> 8 & 0xff00 | v10 >> 24 & 0xff;
    v13 = _INSERT((char)v12 * 0 | (char)(v12 >> 24), 0, ((char)v12 * 0 | (char)(v12 >> 24)) & (char)~(~(_INSERT((char)v9 * 0 | (char)(v9 >> 24), 0, ((char)v9 * 0 | (char)(v9 >> 24)) - 39))) + 3);
    v1 = -(0 < v13) + 1;
    v14 = -(0 < (v3 & 0x600)) + 1;
    v16 = _ccall(0, 6, -((unsigned int)(char)(0 < v13)) + 1, v14, 0);
    v2 = (-(0 < v13) + 1 == v14 ? 0 : 1);
    v4 = (g_1038c7f0 ^ g_1038c7f4) * 2;
    if (v2)
        v4 |= 1;
    return sub_102efa50(v4);
}
```

## `sub_102f6a90` `0x102f6a90`

_240 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7f8;
extern unsigned int g_1038c7fc;

int sub_102f6a90(unsigned int a0)
{
    unsigned int v5;  // ecx
    unsigned int v6;  // eax
    unsigned int v15;  // eax
    char v7;  // cl
    unsigned int v8;  // ecx
    unsigned int v9;  // edx
    int v10;  // edx
    unsigned int v11;  // 4524
    unsigned int v13;  // 4104
    unsigned int v14;  // 4104
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v3 = sub_102effb0(a0);
    v1 = v5;
    v6 = v3 * 0x1000000 | v3 * 0x100 & 0xff0000 | v3 >> 8 & 0xff00 | v3 >> 24 & 0xff;
    v7 = (char)(~(~(64)) + 26) + 3;
    v8 = _INSERT(v7 + 13, 0, v7 + 18);
    v0 = v9;
    v2 = -(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 0x11)) + 1;
    v10 = -(0 < (v3 & 0xf900)) + 1;
    v11 = _ccall(0, 15, 0, 0, 0);
    v13 = _ccall(0, 6, -((unsigned int)(char)(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 0x11))) + 1, v10, 0);
    if (-(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 0x11)) + 1 != v10)
    {
        v14 = _ccall(0, 15, 0, 0, 0);
        v15 = 1;
    }
    else
    {
        v15 = 0;
    }
    v2 = v15;
    v4 = (g_1038c7f8 ^ g_1038c7fc) * 2;
    if (v15)
        v4 |= 1;
    return sub_102efe30(v4);
}
```

## `sub_102f6b90` `0x102f6b90`

_188 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c808;
extern unsigned int g_1038c80c;

unsigned int sub_102f6b90(int a0)
{
    unsigned int v6;  // edx
    char v7;  // al
    int v17;  // cc_dep1
    unsigned int v18;  // 4125
    unsigned int v19;  // eax
    unsigned int v20;  // 4108
    unsigned int v21;  // cc_dep1
    unsigned int v22;  // 4108
    unsigned int v23;  // 4159
    unsigned int v8;  // ebx
    char v9;  // bl
    char v10;  // bl
    unsigned int v11;  // 4165
    unsigned int v12;  // cc_ndep
    unsigned int v13;  // cc_dep1
    unsigned int v14;  // 4172
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f07c0(a0);
    v2 = v6;
    v7 = v4;
    v1 = v8;
    v0 = 10;
    v9 = v0;
    v10 = v9 - 6;
    v11 = _ccall(1, (unsigned int)(v9 - 4), 0xff, 0);
    v12 = v11;
    v13 = v9 - 6;
    v14 = _ccall(0, 19, (unsigned int)(v9 - 6), 0, v11);
    v17 = v7 & v10 - 4;
    v18 = _ccall(0, 13, (unsigned int)(v7 & v10 - 4), 0, 0);
    v19 = _INSERT(v7 & v10 - 4, 1, v7 & v10 - 4 & 8);
    if (v19)
    {
        v20 = _ccall(3, ~(v19), 1, 0);
        v21 = v20 | 1;
    }
    else
    {
        v22 = _ccall(3, ~(0), 1, 0);
        v21 = v22 & 4294967294;
    }
    v23 = _ccall(0, v21, 0, 0);
    v3 = -(-(v23 & 1));
    v5 = (g_1038c808 ^ g_1038c80c) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0730(v5);
}
```

## `sub_102f6bca` `0x102f6bca`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f6bca(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f6be3` `0x102f6be3`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f6be3(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f6c50` `0x102f6c50`

_194 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e0;
extern unsigned int g_1038c7e4;

int sub_102f6c50(unsigned int a0)
{
    unsigned int v6;  // edx
    char v7;  // al
    unsigned int v16;  // 4157
    unsigned int v17;  // eax
    unsigned int v18;  // 4108
    unsigned int v19;  // cc_dep1
    unsigned int v20;  // 4108
    unsigned int v21;  // 4163
    unsigned int v8;  // ebx
    char v9;  // bl
    char v10;  // bh
    unsigned int v11;  // cc_dep1
    unsigned int v12;  // 4141
    int v15;  // cc_dep1
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102ef270(a0);
    v2 = v6;
    v7 = v4;
    v1 = v8;
    v0 = 0x100;
    v9 = v0;
    v10 = v9 - 1;
    v11 = v9 - 1;
    v12 = _ccall(0, 19, (unsigned int)(v9 - 1), 0, 0);
    v15 = v7 & v10;
    v16 = _ccall(0, 13, (unsigned int)(v7 & v10), 0, 0);
    v17 = _INSERT(_INSERT(v7, 1, v7 & v10) & 0xff, 0, (char)_INSERT(v7, 1, v7 & v10) & 4);
    if (v17)
    {
        v18 = _ccall(3, ~(v17), 1, 0);
        v19 = v18 | 1;
    }
    else
    {
        v20 = _ccall(3, ~(0), 1, 0);
        v19 = v20 & 4294967294;
    }
    v21 = _ccall(0, v19, 0, 0);
    v3 = -(-(-(v21 & 1)));
    v5 = (g_1038c7e0 ^ g_1038c7e4) * 2;
    if (v3)
        v5 |= 1;
    return sub_102ef140(v5);
}
```

## `sub_102f6c81` `0x102f6c81`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f6c81(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f6ca2` `0x102f6ca2`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f6ca2(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f6d20` `0x102f6d20`

_185 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c818;
extern unsigned int g_1038c81c;

unsigned int sub_102f6d20(unsigned int a0)
{
    unsigned int v8;  // edx
    unsigned int v9;  // ebx
    unsigned int v11;  // eax
    unsigned int v12;  // 4206
    unsigned short v13;  // bx
    unsigned int v14;  // eax
    unsigned int v15;  // eax
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v2 = a0;
    v5 = sub_102f0f30(a0);
    v2 = v8;
    v1 = v9;
    v0 = v5 & 0xffff;
    v11 = _INSERT(v0, 1, 0);
    v12 = _ccall(0, 13, 0, 0, 0);
    v13 = _INSERT(_INSERT(*((unsigned short *)((void*)&v9 + 1)), 1, 0), 0, 128);
    v14 = v11 * 0x1000000 | v11 * 0x100 & 0xff0000 | v11 >> 8 & 0xff00 | v11 >> 24 & 0xff;
    v15 = _INSERT((char)v14 * 0 | (char)(v14 >> 24), 0, ((char)v14 * 0 | (char)(v14 >> 24)) & (char)~(~(v13)));
    v4 = -(0 < v15) + 1;
    v6 = (g_1038c818 ^ g_1038c81c) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f0e70(v6);
}
```

## `sub_102f6d40` `0x102f6d40`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f6d40(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f6d71` `0x102f6d71`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f6d71(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f6de0` `0x102f6de0`

_147 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c828;
extern unsigned int g_1038c82c;

unsigned int sub_102f6de0(int a0)
{
    unsigned int v4;  // edx
    unsigned int v5;  // 4141
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v2 = sub_102f1910(a0);
    v0 = v4;
    v5 = _ccall(0, 4, 14, 0xff, 0);
    v1 = -(0 < _INSERT(_INSERT(v2, 1, 0) & 0xff, 0, (char)_INSERT(v2, 1, 0) & 1)) + 1;
    v3 = (g_1038c828 ^ g_1038c82c) * 2;
    if (v1)
        v3 |= 1;
    return sub_102f1810(v3);
}
```

## `sub_102f6e0d` `0x102f6e0d`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f6e0d(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f6e80` `0x102f6e80`

_168 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7dc;
extern unsigned int g_1038c7e0;

unsigned int sub_102f6e80(int a0)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // eax
    unsigned int v8;  // ecx
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v2 = v6;
    v4 = sub_102ef020(a0);
    v1 = v6;
    v7 = v4 * 0x1000000 | v4 * 0x100 & 0xff0000 | v4 >> 8 & 0xff00 | v4 >> 24 & 0xff;
    v0 = v8;
    v2 = -(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & ~(~(114)) + 14)) + 1;
    v3 = _INSERT(-(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & ~(~(114)) + 14)) + 1, 0, -(0 < ((v7 * 0x1000000 | v7 * 0x100 & 0xff0000 | v7 >> 8 & 0xff00 | v7 >> 24 & 0xff) & ~(~(114)) + 14)) + 1 == -(0 < (v4 & 0xf900)) + 1);
    v5 = (g_1038c7dc ^ g_1038c7e0) * 2;
    if (v3)
        v5 |= 1;
    return sub_102eef00(v5);
}
```

## `sub_102f6ea2` `0x102f6ea2`

_5 bytes. (leaf/helper — see body)_

```c
void sub_102f6ea2(void)
{
}
```

## `sub_102f6f30` `0x102f6f30`

_158 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c824;
extern unsigned int g_1038c828;

int sub_102f6f30(unsigned int a0)
{
    unsigned int v5;  // ecx
    unsigned int v6;  // eax
    char v7;  // cl
    unsigned int v8;  // ecx
    unsigned int v9;  // edx
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v3 = sub_102f1670(a0);
    v1 = v5;
    v6 = v3 * 0x1000000 | v3 * 0x100 & 0xff0000 | v3 >> 8 & 0xff00 | v3 >> 24 & 0xff;
    v7 = (char)(~(~(12)) + 0x11) + 3;
    v8 = _INSERT(v7 + 13, 0, v7 + 18);
    v0 = v9;
    v2 = -(-(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 14)));
    v4 = (g_1038c824 ^ g_1038c828) * 2;
    if (0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 14))
        v4 |= 1;
    return sub_102f14d0(v4);
}
```

## `sub_102f6fd0` `0x102f6fd0`

_339 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7dc;
extern unsigned int g_1038c7e0;

unsigned int sub_102f6fd0(int a0)
{
    unsigned int v8;  // edx
    unsigned int v9;  // ebx
    unsigned int v18;  // eax
    unsigned int v19;  // eax
    unsigned short v20;  // ax
    unsigned int v21;  // cc_dep1
    unsigned int v22;  // 4291
    unsigned int v23;  // eax
    unsigned int v24;  // 4244
    unsigned int v25;  // eax
    unsigned int v28;  // 4245
    unsigned int v31;  // 4151
    unsigned int v32;  // eax
    unsigned int v33;  // cc_ndep
    unsigned int v34;  // cc_dep1
    unsigned int v35;  // 4152
    unsigned int v11;  // eax
    unsigned int v38;  // eax
    unsigned short v12;  // bx
    unsigned int v13;  // eax
    unsigned int v14;  // eax
    unsigned int v16;  // eax
    unsigned short v17;  // bx
    unsigned int v0;  // [bp-0x24]
    unsigned int v1;  // [bp-0x24]
    unsigned int v2;  // [bp-0x20]
    unsigned int v3;  // [bp-0x1c]
    unsigned int v4;  // [bp-0x18]
    unsigned int v5;  // [bp-0x10]
    int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]

    v6 = sub_102ef020(a0);
    v4 = v8;
    v3 = v9;
    v2 = v6 & 0xffff;
    v11 = _INSERT(v2, 1, 0);
    v12 = _INSERT(_INSERT(*((unsigned short *)((void*)&v9 + 1)), 1, 0), 0, 64);
    v13 = v11 * 0x1000000 | v11 * 0x100 & 0xff0000 | v11 >> 8 & 0xff00 | v11 >> 24 & 0xff;
    v14 = _INSERT((char)v13 * 0 | (char)(v13 >> 24), 0, ((char)v13 * 0 | (char)(v13 >> 24)) & (char)~(~(v12)));
    if (!v14)
    {
        v4 = v8;
        v2 = v6 & 0xffff;
        v16 = _INSERT(v2, 1, 0);
        v17 = _INSERT(_INSERT(*((unsigned short *)((void*)&v3 + 1)), 1, 0), 0, 0x88);
        v18 = v16 * 0x1000000 | v16 * 0x100 & 0xff0000 | v16 >> 8 & 0xff00 | v16 >> 24 & 0xff;
        v19 = _INSERT((char)v18 * 0 | (char)(v18 >> 24), 0, ((char)v18 * 0 | (char)(v18 >> 24)) & (char)~(~(v17)));
        v4 = -(0 < v19) + 1;
        v20 = v6;
        v3 = v8;
        v21 = v20;
        v2 = v3;
        v0 = 31;
        v22 = _ccall(0, 15, (unsigned int)v20, 0, 0);
        v1 = v20;
        v23 = _INSERT((char)v1 & (char)v0 - 31, 1, (char)v1 & (char)v0 - 31 & 246);
        v24 = _ccall(12, 0, (unsigned int)(char)(0 < v23), (unsigned int)(char)(0 < v23));
        v25 = -(0 < v23) + 1;
        v28 = _ccall(0, 21, v25 - 1, 0, v24);
        v31 = _ccall(21, v25 - 1, 0, v24);
        v32 = v25;
        v33 = v31;
        v34 = v32 - 1;
        v35 = _ccall(0, 21, v32 - 1, 0, v31);
        if (-(0 < v19) + 1 != v32)
            goto LABEL_102f70f2;
        v38 = 1;
    }
    else
    {
LABEL_102f70f2:
        v38 = 0;
    }
    v5 = v38;
    v7 = (g_1038c7dc ^ g_1038c7e0) * 2;
    if (v5)
        v7 |= 1;
    return sub_102eef00(v7);
}
```

## `sub_102f708e` `0x102f708e`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f708e(void)
{
}
```

## `sub_102f70ce` `0x102f70ce`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f70ce(void)
{
}
```

## `sub_102f7130` `0x102f7130`

_176 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c808;
extern unsigned int g_1038c80c;

unsigned int sub_102f7130(int a0)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // ecx
    unsigned int v8;  // eax
    unsigned int v9;  // 4108
    unsigned int v10;  // cc_dep1
    unsigned int v11;  // 4108
    unsigned int v12;  // 4159
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f07c0(a0);
    v2 = v6;
    v1 = v7;
    v0 = 0x800;
    v8 = _INSERT(_INSERT(v4 & 0xffff, 1, (char)v4 & *((char *)((void*)&v0 + 1)) - 8) & 0xff, 0, (char)_INSERT(v4 & 0xffff, 1, (char)v4 & *((char *)((void*)&v0 + 1)) - 8) & 4);
    if (v8)
    {
        v9 = _ccall(3, ~(v8), 1, 0);
        v10 = v9 | 1;
    }
    else
    {
        v11 = _ccall(3, ~(0), 1, 0);
        v10 = v11 & 4294967294;
    }
    v12 = _ccall(0, v10, 0, 0);
    v3 = -(-(v12 & 1));
    v5 = (g_1038c808 ^ g_1038c80c) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0730(v5);
}
```

## `sub_102f71e0` `0x102f71e0`

_191 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c800;
extern unsigned int g_1038c804;

int sub_102f71e0(unsigned int a0)
{
    unsigned int v6;  // edx
    char v7;  // al
    unsigned int v16;  // 4157
    unsigned int v17;  // eax
    unsigned int v18;  // 4108
    unsigned int v19;  // cc_dep1
    unsigned int v20;  // 4108
    unsigned int v21;  // 4163
    unsigned int v8;  // ebx
    char v9;  // bl
    char v10;  // bh
    unsigned int v11;  // cc_dep1
    unsigned int v12;  // 4141
    int v15;  // cc_dep1
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f04d0(a0);
    v2 = v6;
    v7 = v4;
    v1 = v8;
    v0 = 0x100;
    v9 = v0;
    v10 = v9 - 1;
    v11 = v9 - 1;
    v12 = _ccall(0, 19, (unsigned int)(v9 - 1), 0, 0);
    v15 = v7 & v10;
    v16 = _ccall(0, 13, (unsigned int)(v7 & v10), 0, 0);
    v17 = _INSERT(_INSERT(v7, 1, v7 & v10) & 0xff, 0, (char)_INSERT(v7, 1, v7 & v10) & 4);
    if (v17)
    {
        v18 = _ccall(3, ~(v17), 1, 0);
        v19 = v18 | 1;
    }
    else
    {
        v20 = _ccall(3, ~(0), 1, 0);
        v19 = v20 & 4294967294;
    }
    v21 = _ccall(0, v19, 0, 0);
    v3 = -(-(-(v21 & 1)));
    v5 = (g_1038c800 ^ g_1038c804) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0430(v5);
}
```

## `sub_102f7211` `0x102f7211`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f7211(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f7232` `0x102f7232`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f7232(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f72b0` `0x102f72b0`

_408 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c844;
extern unsigned int g_1038c848;

unsigned int sub_102f72b0(int a0)
{
    unsigned int v8;  // ebx
    unsigned int v9;  // ecx
    unsigned int v19;  // eax
    char v20;  // cl
    unsigned int v21;  // cc_dep1
    unsigned int v23;  // eax
    unsigned short v24;  // ax
    unsigned int v25;  // cc_dep1
    unsigned int v26;  // 4168
    unsigned int v27;  // 4212
    unsigned int v31;  // eax
    char v11;  // cl
    unsigned int v13;  // edx
    unsigned int v15;  // ecx
    unsigned int v16;  // ecx
    unsigned int v17;  // eax
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]

    v4 = v8;
    v6 = sub_102f2b60(a0);
    v3 = v9;
    v11 = (char)(~(~(~(~(12)) + 7)) + 10) + 3;
    v2 = v13;
    if (!(__buildin_bswap32(v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & _INSERT(v11 + 13, 0, v11 + 18) + 14))
    {
        v4 = v8;
        v3 = v9;
        v15 = _INSERT(_INSERT(v9, 1, 0), 0, 164);
        v16 = v15 * 0x1000000 | v15 * 0x100 & 0xff0000 | v15 >> 8 & 0xff00 | v15 >> 24 & 0xff;
        v17 = _INSERT(_INSERT(v6 & 0xffff, 1, 0) & 0xff, 0, ~(~((char)_INSERT(v6 & 0xffff, 1, 0))));
        v19 = v17 * 0x1000000 | v17 * 0x100 & 0xff0000 | v17 >> 8 & 0xff00 | v17 >> 24 & 0xff;
        v20 = ~(~(_INSERT((char)v16 * 0 | (char)(v16 >> 24), 0, ((char)v16 * 0 | (char)(v16 >> 24)) - 39)));
        v21 = v20 + 1;
        v23 = _INSERT((char)v19 * 0 | (char)(v19 >> 24), 0, ((char)v19 * 0 | (char)(v19 >> 24)) & v20 + 3);
        v4 = -(0 < v23) + 1;
        v24 = v6;
        v3 = v8;
        v25 = v24;
        v2 = v8;
        v0 = 31;
        v26 = _ccall(0, 15, (unsigned int)v24, 0, 0);
        v1 = v24;
        v27 = _ccall(0, 19, 243, 0, 0);
        if (-(0 < v23) + 1 != -(0 < _INSERT((char)v1 & (char)v0 - 31, 1, (char)v1 & (char)v0 - 31 & 243)) + 1)
            goto LABEL_102f7419;
        v31 = 1;
    }
    else
    {
LABEL_102f7419:
        v31 = 0;
    }
    v5 = v31;
    v7 = (g_1038c844 ^ g_1038c848) * 2;
    if (v5)
        v7 |= 1;
    return sub_102f2ad0(v7);
}
```

## `sub_102f739e` `0x102f739e`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f739e(void)
{
}
```

## `sub_102f73c6` `0x102f73c6`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f73c6(void)
{
}
```

## `sub_102f73fe` `0x102f73fe`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f73fe(void)
{
}
```

## `sub_102f7460` `0x102f7460`

_158 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c840;
extern unsigned int g_1038c844;

unsigned int sub_102f7460(int a0)
{
    unsigned int v5;  // ecx
    unsigned int v6;  // eax
    char v7;  // cl
    unsigned int v8;  // ecx
    unsigned int v9;  // edx
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v3 = sub_102f2940(a0);
    v1 = v5;
    v6 = v3 * 0x1000000 | v3 * 0x100 & 0xff0000 | v3 >> 8 & 0xff00 | v3 >> 24 & 0xff;
    v7 = (char)(~(~(13)) + 0x11) + 3;
    v8 = _INSERT(v7 + 13, 0, v7 + 18);
    v0 = v9;
    v2 = -(-(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 14)));
    v4 = (g_1038c840 ^ g_1038c844) * 2;
    if (0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 14))
        v4 |= 1;
    return sub_102f27b0(v4);
}
```

## `sub_102f7500` `0x102f7500`

_164 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c81c;
extern unsigned int g_1038c820;

int sub_102f7500(unsigned int a0)
{
    unsigned int v5;  // ecx
    unsigned int v6;  // eax
    char v7;  // cl
    unsigned int v8;  // ecx
    unsigned int v9;  // edx
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v3 = sub_102f1120(a0);
    v1 = v5;
    v6 = v3 * 0x1000000 | v3 * 0x100 & 0xff0000 | v3 >> 8 & 0xff00 | v3 >> 24 & 0xff;
    v7 = (char)(~(~(6)) + 24) + 3;
    v8 = _INSERT(v7 + 13, 0, v7 + 18);
    v0 = v9;
    v2 = -(-(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 14)));
    v4 = (g_1038c81c ^ g_1038c820) * 2;
    if (0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 14))
        v4 |= 1;
    return sub_102f0ff0(v4);
}
```

## `sub_102f75b0` `0x102f75b0`

_157 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7fc;
extern unsigned int g_1038c800;

unsigned int sub_102f75b0(int a0)
{
    unsigned int v5;  // ecx
    unsigned int v6;  // edx
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v3 = sub_102f02b0(a0);
    v1 = v5;
    v0 = v6;
    v2 = 1;
    v4 = (g_1038c7fc ^ g_1038c800) * 2;
    if (v2)
        v4 |= 1;
    return sub_102f0130(v4);
}
```

## `sub_102f7650` `0x102f7650`

_225 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c80c;
extern unsigned int g_1038c810;

unsigned int sub_102f7650(int a0)
{
    unsigned int v6;  // edx
    char v7;  // al
    int v17;  // cc_dep1
    unsigned int v18;  // 4125
    unsigned int v19;  // eax
    unsigned int v20;  // 4108
    unsigned int v21;  // cc_dep1
    unsigned int v22;  // 4108
    unsigned int v23;  // 4133
    unsigned int v24;  // 4134
    unsigned int v25;  // eax
    unsigned int v8;  // ebx
    unsigned int v28;  // 4135
    unsigned int v31;  // 4119
    unsigned int v32;  // eax
    unsigned int v35;  // 4120
    char v9;  // bl
    unsigned int v38;  // 4135
    unsigned int v39;  // eax
    unsigned int v40;  // cc_ndep
    unsigned int v41;  // cc_dep1
    unsigned int v42;  // 4136
    char v10;  // bl
    unsigned int v11;  // 4165
    unsigned int v12;  // cc_ndep
    unsigned int v13;  // cc_dep1
    unsigned int v14;  // 4172
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f0940(a0);
    v2 = v6;
    v7 = v4;
    v1 = v8;
    v0 = 10;
    v9 = v0;
    v10 = v9 - 6;
    v11 = _ccall(1, (unsigned int)(v9 - 4), 0xff, 0);
    v12 = v11;
    v13 = v9 - 6;
    v14 = _ccall(0, 19, (unsigned int)(v9 - 6), 0, v11);
    v17 = v7 & v10 - 4;
    v18 = _ccall(0, 13, (unsigned int)(v7 & v10 - 4), 0, 0);
    v19 = _INSERT(v7 & v10 - 4, 1, v7 & v10 - 4 & 8);
    if (v19)
    {
        v20 = _ccall(3, ~(v19), 1, 0);
        v21 = v20 | 1;
    }
    else
    {
        v22 = _ccall(3, ~(0), 1, 0);
        v21 = v22 & 4294967294;
    }
    v23 = _ccall(0, v21, 0, 0);
    v24 = _ccall(12, 0, v23 & 1, v23 & 1);
    v25 = -(v23 & 1) + 1;
    v28 = _ccall(0, 21, v25 - 1, 0, v24);
    v31 = _ccall(21, v25 - 1, 0, v24);
    v32 = v25;
    v35 = _ccall(0, 21, v32 - 1, 0, v31);
    v38 = _ccall(21, v32 - 1, 0, v31);
    v39 = v32;
    v40 = v38;
    v41 = v39 - 1;
    v42 = _ccall(0, 21, v39 - 1, 0, v38);
    v3 = v39;
    v5 = (g_1038c80c ^ g_1038c810) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0850(v5);
}
```

## `sub_102f768a` `0x102f768a`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f768a(void)
{
}
```

## `sub_102f76a5` `0x102f76a5`

_1 bytes. (leaf/helper — see body)_

```c
void sub_102f76a5(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f76e1` `0x102f76e1`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f76e1(void)
{
}
```

## `sub_102f76f0` `0x102f76f0`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f76f0(void)
{
}
```

## `sub_102f7701` `0x102f7701`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f7701(void)
{
}
```

## `sub_102f7740` `0x102f7740`

_151 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7e0;
extern unsigned int g_1038c7e4;

int sub_102f7740(unsigned int a0)
{
    unsigned int v7;  // ebx
    unsigned int v8;  // edx
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v3 = v7;
    v5 = sub_102ef270(a0);
    v2 = v8;
    v1 = v7;
    v0 = v5 & 0xffff;
    v4 = 1;
    v6 = (g_1038c7e0 ^ g_1038c7e4) * 2;
    if (v4)
        v6 |= 1;
    return sub_102ef140(v6);
}
```

## `sub_102f77e0` `0x102f77e0`

_258 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c80c;
extern unsigned int g_1038c810;

unsigned int sub_102f77e0(int a0)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // ecx
    unsigned int v10;  // ecx
    unsigned int v11;  // eax
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f0940(a0);
    v2 = v6;
    v1 = v7;
    v0 = _INSERT(v4 & 0xffff, 1, 0);
    v10 = _INSERT(_INSERT(v7, 1, 0), 0, 125);
    v11 = _INSERT(v0, 0, (char)v0 & (char)~(~(v10)) + 3);
    v2 = -(0 < v11) + 1;
    v3 = _INSERT(-(0 < v11) + 1, 0, -(0 < v11) + 1 == -(0 < (v4 & 0xfc00)) + 1);
    v5 = (g_1038c80c ^ g_1038c810) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0850(v5);
}
```

## `sub_102f78f0` `0x102f78f0`

_247 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c814;
extern unsigned int g_1038c818;

unsigned int sub_102f78f0(int a0)
{
    unsigned int v6;  // ebx
    unsigned int v7;  // ecx
    unsigned int v10;  // ecx
    unsigned int v11;  // eax
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102f0dc0(a0);
    v2 = v6;
    v1 = v7;
    v0 = _INSERT(v4 & 0xffff, 1, 0);
    v10 = _INSERT(_INSERT(v7, 1, 0), 0, 125);
    v11 = _INSERT(v0, 0, (char)v0 & (char)~(~(v10)) + 3);
    v2 = -(0 < v11) + 1;
    v3 = _INSERT(-(0 < v11) + 1, 0, -(0 < v11) + 1 == -(0 < (v4 & 0xfc00)) + 1);
    v5 = (g_1038c814 ^ g_1038c818) * 2;
    if (v3)
        v5 |= 1;
    return sub_102f0d10(v5);
}
```

## `sub_102f79f0` `0x102f79f0`

_129 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c83c;
extern unsigned int g_1038c840;

unsigned int sub_102f79f0(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v7;  // ebx
    unsigned int v8;  // esi
    unsigned int v9;  // edi
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v4 = v7;
    v3 = v8;
    v2 = v9;
    v1 = v7;
    v0 = a0;
    v5 = (!a3 && 1 ? 1 : 0);
    v6 = (g_1038c83c ^ g_1038c840) * 2;
    if (v5)
        v6 |= 1;
    return sub_102f2570(v6);
}
```

## `sub_102f7a80` `0x102f7a80`

_161 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c828;
extern unsigned int g_1038c82c;

unsigned int sub_102f7a80(int a0)
{
    unsigned int v5;  // ecx
    unsigned int v6;  // eax
    char v7;  // cl
    unsigned int v8;  // ecx
    unsigned int v9;  // edx
    unsigned int v0;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v3 = sub_102f1910(a0);
    v1 = v5;
    v6 = v3 * 0x1000000 | v3 * 0x100 & 0xff0000 | v3 >> 8 & 0xff00 | v3 >> 24 & 0xff;
    v7 = (char)(~(~(76)) + 14) + 3;
    v8 = _INSERT(v7 + 11, 0, v7 + 18);
    v0 = v9;
    v2 = -(-(0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 0x11)));
    v4 = (g_1038c828 ^ g_1038c82c) * 2;
    if (0 < ((v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v8 + 0x11))
        v4 |= 1;
    return sub_102f1810(v4);
}
```

## `sub_102f7b30` `0x102f7b30`

_138 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7f8;
extern unsigned int g_1038c7fc;

int sub_102f7b30(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v7;  // ebx
    unsigned int v8;  // esi
    unsigned int v9;  // edi
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x14]
    unsigned int v4;  // [bp-0x10]
    unsigned int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v4 = v7;
    v3 = v8;
    v2 = v9;
    v1 = v7;
    v0 = a0;
    v5 = (!a3 && 1 ? 1 : 0);
    v6 = (g_1038c7f8 ^ g_1038c7fc) * 2;
    if (v5)
        v6 |= 1;
    return sub_102efe30(v6);
}
```

## `sub_102f7bc0` `0x102f7bc0`

_146 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7f8;
extern unsigned int g_1038c7fc;

int sub_102f7bc0(unsigned int a0)
{
    unsigned int v4;  // cc_ndep
    unsigned int v5;  // 4129
    unsigned int v8;  // 4131
    unsigned int v10;  // eax
    unsigned int v11;  // eax
    int v0;  // [bp-0x18]
    int <0x102f7bc0[is_2]|Stack bp-0x10, 1 B>;  // [bp-0x10]
    unsigned int v1;  // [bp-0x10]
    int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v2 = sub_102effb0(a0);
    v4 = &<0x102f7bc0[is_2]|Stack bp-0x10, 1 B> < &/* unsupported instruction */;
    v5 = _ccall(0, 19, 2, 0, (unsigned int)(char)(&<0x102f7bc0[is_2]|Stack bp-0x10, 1 B> < &/* unsupported instruction */));
    v0 = v2;
    v8 = _ccall(0, 4, 2, 2, 0);
    v10 = _INSERT(_INSERT(v0, 0, (char)v0 & 1), 1, ~(0));
    v11 = v10 * 0x1000000 | v10 * 0x100 & 0xff0000 | v10 >> 8 & 0xff00 | v10 >> 24 & 0xff;
    v1 = -(0 < _INSERT((char)v11 * 0 | (char)(v11 >> 24), 1, ~((char)v11 * 0 | (char)(v11 >> 24)))) + 1;
    v3 = (g_1038c7f8 ^ g_1038c7fc) * 2;
    if (v1)
        v3 |= 1;
    return sub_102efe30(v3);
}
```

