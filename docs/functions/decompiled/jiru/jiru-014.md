# elfbot.dll decompiled — jiru 0x10308df0..0x1030cc70

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10308df0` `0x10308df0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10308df0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 162;
    v7 = 94;
    v8 = 38;
    v9 = 225;
    v10 = 239;
    v11 = 0x33;
    v12 = 151;
    v13 = 215;
    v0 = 14;
    v14 = 7;
    idx = (&v6)[a0 >> 14 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_10308f00` `0x10308f00`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10308f00(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 78;
    v7 = 174;
    v8 = 217;
    v9 = 237;
    v10 = 0x22;
    v11 = 0x44;
    v12 = 150;
    v13 = 146;
    v0 = 7;
    v14 = 7;
    idx = (&v6)[a0 >> 7 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_10309010` `0x10309010`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10309010(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 216;
    v7 = 2;
    v8 = 198;
    v9 = 231;
    v10 = 169;
    v11 = 96;
    v12 = 242;
    v13 = 130;
    v0 = 2;
    v14 = 7;
    idx = (&v6)[a0 >> 2 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_10309120` `0x10309120`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10309120(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 1;
    v7 = 94;
    v8 = 209;
    v9 = 192;
    v10 = 166;
    v11 = 214;
    v12 = 94;
    v13 = 183;
    v0 = 10;
    v14 = 7;
    idx = (&v6)[a0 >> 10 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_10309230` `0x10309230`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10309230(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 26;
    v7 = 113;
    v8 = 0xaa;
    v9 = 99;
    v10 = 181;
    v11 = 180;
    v12 = 249;
    v13 = 65;
    v0 = 18;
    v14 = 7;
    idx = (&v6)[a0 >> 18 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_10309340` `0x10309340`

_254 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10309340(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 199;
    v7 = 109;
    v8 = 5;
    v9 = 147;
    v10 = 152;
    v11 = 32;
    v12 = 248;
    v13 = 57;
    v0 = 0;
    v14 = 7;
    idx = (&v6)[a0 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_10309440` `0x10309440`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10309440(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 141;
    v7 = 133;
    v8 = 0x55;
    v9 = 18;
    v10 = 239;
    v11 = 214;
    v12 = 96;
    v13 = 175;
    v0 = 0x11;
    v14 = 7;
    idx = (&v6)[a0 >> 0x11 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_10309550` `0x10309550`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10309550(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 104;
    v7 = 124;
    v8 = 16;
    v9 = 95;
    v10 = 173;
    v11 = 0xaa;
    v12 = 74;
    v13 = 97;
    v0 = 13;
    v14 = 7;
    idx = (&v6)[a0 >> 13 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_10309660` `0x10309660`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10309660(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 10;
    v7 = 146;
    v8 = 27;
    v9 = 151;
    v10 = 101;
    v11 = 167;
    v12 = 135;
    v13 = 189;
    v0 = 0x11;
    v14 = 7;
    idx = (&v6)[a0 >> 0x11 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_10309770` `0x10309770`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10309770(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 137;
    v7 = 251;
    v8 = 36;
    v9 = 77;
    v10 = 70;
    v11 = 158;
    v12 = 117;
    v13 = 118;
    v0 = 21;
    v14 = 7;
    idx = (&v6)[a0 >> 21 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_10309880` `0x10309880`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10309880(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 228;
    v7 = 37;
    v8 = 109;
    v9 = 200;
    v10 = 249;
    v11 = 166;
    v12 = 10;
    v13 = 48;
    v0 = 6;
    v14 = 7;
    idx = (&v6)[a0 >> 6 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_10309990` `0x10309990`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10309990(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 229;
    v7 = 24;
    v8 = 0x44;
    v9 = 57;
    v10 = 87;
    v11 = 0x55;
    v12 = 233;
    v13 = 47;
    v0 = 21;
    v14 = 7;
    idx = (&v6)[a0 >> 21 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_10309aa0` `0x10309aa0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10309aa0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 104;
    v7 = 179;
    v8 = 192;
    v9 = 3;
    v10 = 175;
    v11 = 67;
    v12 = 190;
    v13 = 12;
    v0 = 13;
    v14 = 7;
    idx = (&v6)[a0 >> 13 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_10309bb0` `0x10309bb0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10309bb0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 142;
    v7 = 65;
    v8 = 223;
    v9 = 169;
    v10 = 58;
    v11 = 149;
    v12 = 93;
    v13 = 24;
    v0 = 2;
    v14 = 7;
    idx = (&v6)[a0 >> 2 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_10309cc0` `0x10309cc0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10309cc0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 215;
    v7 = 249;
    v8 = 200;
    v9 = 242;
    v10 = 3;
    v11 = 0x77;
    v12 = 77;
    v13 = 77;
    v0 = 3;
    v14 = 7;
    idx = (&v6)[a0 >> 3 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_10309dd0` `0x10309dd0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10309dd0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 90;
    v7 = 97;
    v8 = 115;
    v9 = 208;
    v10 = 103;
    v11 = 72;
    v12 = 46;
    v13 = 0;
    v0 = 6;
    v14 = 7;
    idx = (&v6)[a0 >> 6 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_10309ee0` `0x10309ee0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10309ee0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 250;
    v7 = 0x55;
    v8 = 139;
    v9 = 224;
    v10 = 223;
    v11 = 36;
    v12 = 6;
    v13 = 0x33;
    v0 = 5;
    v14 = 7;
    idx = (&v6)[a0 >> 5 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_10309ff0` `0x10309ff0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10309ff0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 0;
    v7 = 12;
    v8 = 43;
    v9 = 46;
    v10 = 189;
    v11 = 86;
    v12 = 175;
    v13 = 155;
    v0 = 5;
    v14 = 7;
    idx = (&v6)[a0 >> 5 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030a100` `0x1030a100`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030a100(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 98;
    v7 = 142;
    v8 = 88;
    v9 = 52;
    v10 = 114;
    v11 = 225;
    v12 = 209;
    v13 = 215;
    v0 = 2;
    v14 = 7;
    idx = (&v6)[a0 >> 2 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030a210` `0x1030a210`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030a210(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 37;
    v7 = 174;
    v8 = 213;
    v9 = 108;
    v10 = 117;
    v11 = 176;
    v12 = 200;
    v13 = 114;
    v0 = 4;
    v14 = 7;
    idx = (&v6)[a0 >> 4 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030a320` `0x1030a320`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030a320(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 0x99;
    v7 = 82;
    v8 = 182;
    v9 = 100;
    v10 = 157;
    v11 = 96;
    v12 = 111;
    v13 = 103;
    v0 = 7;
    v14 = 7;
    idx = (&v6)[a0 >> 7 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030a430` `0x1030a430`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030a430(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 226;
    v7 = 49;
    v8 = 129;
    v9 = 152;
    v10 = 125;
    v11 = 143;
    v12 = 246;
    v13 = 140;
    v0 = 15;
    v14 = 7;
    idx = (&v6)[a0 >> 15 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030a540` `0x1030a540`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030a540(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 227;
    v7 = 220;
    v8 = 206;
    v9 = 201;
    v10 = 22;
    v11 = 0x88;
    v12 = 152;
    v13 = 161;
    v0 = 4;
    v14 = 7;
    idx = (&v6)[a0 >> 4 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030a650` `0x1030a650`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030a650(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 223;
    v7 = 83;
    v8 = 174;
    v9 = 31;
    v10 = 0x66;
    v11 = 0x11;
    v12 = 239;
    v13 = 140;
    v0 = 2;
    v14 = 7;
    idx = (&v6)[a0 >> 2 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030a760` `0x1030a760`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030a760(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 148;
    v7 = 127;
    v8 = 15;
    v9 = 198;
    v10 = 139;
    v11 = 172;
    v12 = 0;
    v13 = 149;
    v0 = 8;
    v14 = 7;
    idx = (&v6)[a0 >> 8 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030a870` `0x1030a870`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030a870(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 24;
    v7 = 177;
    v8 = 0x11;
    v9 = 243;
    v10 = 11;
    v11 = 176;
    v12 = 169;
    v13 = 40;
    v0 = 9;
    v14 = 7;
    idx = (&v6)[a0 >> 9 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030a980` `0x1030a980`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030a980(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 30;
    v7 = 150;
    v8 = 209;
    v9 = 248;
    v10 = 226;
    v11 = 49;
    v12 = 177;
    v13 = 0xbb;
    v0 = 9;
    v14 = 7;
    idx = (&v6)[a0 >> 9 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030aa90` `0x1030aa90`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030aa90(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 18;
    v7 = 0xdd;
    v8 = 118;
    v9 = 124;
    v10 = 223;
    v11 = 213;
    v12 = 179;
    v13 = 113;
    v0 = 19;
    v14 = 7;
    idx = (&v6)[a0 >> 19 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030aba0` `0x1030aba0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030aba0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 241;
    v7 = 162;
    v8 = 210;
    v9 = 160;
    v10 = 29;
    v11 = 91;
    v12 = 203;
    v13 = 18;
    v0 = 3;
    v14 = 7;
    idx = (&v6)[a0 >> 3 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030acb0` `0x1030acb0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030acb0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 180;
    v7 = 209;
    v8 = 0;
    v9 = 169;
    v10 = 48;
    v11 = 130;
    v12 = 197;
    v13 = 0x44;
    v0 = 2;
    v14 = 7;
    idx = (&v6)[a0 >> 2 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030adc0` `0x1030adc0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030adc0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 0xaa;
    v7 = 87;
    v8 = 82;
    v9 = 4;
    v10 = 140;
    v11 = 224;
    v12 = 245;
    v13 = 241;
    v0 = 7;
    v14 = 7;
    idx = (&v6)[a0 >> 7 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030aed0` `0x1030aed0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030aed0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 128;
    v7 = 198;
    v8 = 182;
    v9 = 45;
    v10 = 125;
    v11 = 13;
    v12 = 148;
    v13 = 39;
    v0 = 2;
    v14 = 7;
    idx = (&v6)[a0 >> 2 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030afe0` `0x1030afe0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030afe0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 65;
    v7 = 226;
    v8 = 50;
    v9 = 91;
    v10 = 241;
    v11 = 10;
    v12 = 111;
    v13 = 172;
    v0 = 3;
    v14 = 7;
    idx = (&v6)[a0 >> 3 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030b0f0` `0x1030b0f0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030b0f0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 143;
    v7 = 0x99;
    v8 = 44;
    v9 = 105;
    v10 = 154;
    v11 = 166;
    v12 = 201;
    v13 = 230;
    v0 = 18;
    v14 = 7;
    idx = (&v6)[a0 >> 18 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030b200` `0x1030b200`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030b200(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 26;
    v7 = 248;
    v8 = 11;
    v9 = 111;
    v10 = 45;
    v11 = 149;
    v12 = 148;
    v13 = 173;
    v0 = 20;
    v14 = 7;
    idx = (&v6)[a0 >> 20 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030b310` `0x1030b310`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030b310(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 47;
    v7 = 144;
    v8 = 69;
    v9 = 199;
    v10 = 83;
    v11 = 33;
    v12 = 216;
    v13 = 139;
    v0 = 13;
    v14 = 7;
    idx = (&v6)[a0 >> 13 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030b420` `0x1030b420`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030b420(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 0x11;
    v7 = 247;
    v8 = 0x99;
    v9 = 29;
    v10 = 66;
    v11 = 96;
    v12 = 83;
    v13 = 169;
    v0 = 5;
    v14 = 7;
    idx = (&v6)[a0 >> 5 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030b530` `0x1030b530`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030b530(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 173;
    v7 = 20;
    v8 = 0x88;
    v9 = 247;
    v10 = 86;
    v11 = 64;
    v12 = 63;
    v13 = 114;
    v0 = 15;
    v14 = 7;
    idx = (&v6)[a0 >> 15 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030b640` `0x1030b640`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030b640(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 244;
    v7 = 99;
    v8 = 108;
    v9 = 130;
    v10 = 91;
    v11 = 9;
    v12 = 215;
    v13 = 125;
    v0 = 14;
    v14 = 7;
    idx = (&v6)[a0 >> 14 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030b750` `0x1030b750`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030b750(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 36;
    v7 = 206;
    v8 = 0x55;
    v9 = 176;
    v10 = 205;
    v11 = 236;
    v12 = 11;
    v13 = 123;
    v0 = 8;
    v14 = 7;
    idx = (&v6)[a0 >> 8 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030b860` `0x1030b860`

_254 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030b860(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 65;
    v7 = 190;
    v8 = 1;
    v9 = 109;
    v10 = 176;
    v11 = 231;
    v12 = 40;
    v13 = 98;
    v0 = 0;
    v14 = 7;
    idx = (&v6)[a0 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030b960` `0x1030b960`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030b960(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 239;
    v7 = 200;
    v8 = 56;
    v9 = 244;
    v10 = 146;
    v11 = 184;
    v12 = 4;
    v13 = 206;
    v0 = 13;
    v14 = 7;
    idx = (&v6)[a0 >> 13 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030ba70` `0x1030ba70`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030ba70(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 237;
    v7 = 62;
    v8 = 180;
    v9 = 62;
    v10 = 169;
    v11 = 31;
    v12 = 26;
    v13 = 105;
    v0 = 3;
    v14 = 7;
    idx = (&v6)[a0 >> 3 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030bb80` `0x1030bb80`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030bb80(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 11;
    v7 = 202;
    v8 = 166;
    v9 = 245;
    v10 = 0x55;
    v11 = 138;
    v12 = 0;
    v13 = 59;
    v0 = 19;
    v14 = 7;
    idx = (&v6)[a0 >> 19 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030bc90` `0x1030bc90`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030bc90(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 185;
    v7 = 200;
    v8 = 38;
    v9 = 162;
    v10 = 53;
    v11 = 78;
    v12 = 70;
    v13 = 194;
    v0 = 16;
    v14 = 7;
    idx = (&v6)[a0 >> 16 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030bda0` `0x1030bda0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030bda0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 237;
    v7 = 67;
    v8 = 151;
    v9 = 29;
    v10 = 84;
    v11 = 107;
    v12 = 9;
    v13 = 168;
    v0 = 3;
    v14 = 7;
    idx = (&v6)[a0 >> 3 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030beb0` `0x1030beb0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030beb0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 86;
    v7 = 210;
    v8 = 0xcc;
    v9 = 24;
    v10 = 232;
    v11 = 0xaa;
    v12 = 152;
    v13 = 45;
    v0 = 15;
    v14 = 7;
    idx = (&v6)[a0 >> 15 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030bfc0` `0x1030bfc0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030bfc0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 57;
    v7 = 174;
    v8 = 95;
    v9 = 62;
    v10 = 100;
    v11 = 242;
    v12 = 148;
    v13 = 49;
    v0 = 8;
    v14 = 7;
    idx = (&v6)[a0 >> 8 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030c0d0` `0x1030c0d0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030c0d0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 9;
    v7 = 76;
    v8 = 233;
    v9 = 69;
    v10 = 14;
    v11 = 33;
    v12 = 242;
    v13 = 0x88;
    v0 = 0x11;
    v14 = 7;
    idx = (&v6)[a0 >> 0x11 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030c1e0` `0x1030c1e0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030c1e0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 107;
    v7 = 250;
    v8 = 5;
    v9 = 103;
    v10 = 188;
    v11 = 127;
    v12 = 183;
    v13 = 79;
    v0 = 11;
    v14 = 7;
    idx = (&v6)[a0 >> 11 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030c2f0` `0x1030c2f0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030c2f0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 127;
    v7 = 134;
    v8 = 140;
    v9 = 178;
    v10 = 201;
    v11 = 60;
    v12 = 111;
    v13 = 216;
    v0 = 20;
    v14 = 7;
    idx = (&v6)[a0 >> 20 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030c400` `0x1030c400`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030c400(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 230;
    v7 = 112;
    v8 = 249;
    v9 = 135;
    v10 = 121;
    v11 = 94;
    v12 = 16;
    v13 = 131;
    v0 = 0x11;
    v14 = 7;
    idx = (&v6)[a0 >> 0x11 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030c510` `0x1030c510`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030c510(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 63;
    v7 = 226;
    v8 = 16;
    v9 = 155;
    v10 = 129;
    v11 = 239;
    v12 = 211;
    v13 = 207;
    v0 = 18;
    v14 = 7;
    idx = (&v6)[a0 >> 18 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030c620` `0x1030c620`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030c620(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 168;
    v7 = 169;
    v8 = 0x33;
    v9 = 1;
    v10 = 247;
    v11 = 201;
    v12 = 241;
    v13 = 235;
    v0 = 14;
    v14 = 7;
    idx = (&v6)[a0 >> 14 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030c730` `0x1030c730`

_256 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030c730(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 105;
    v7 = 226;
    v8 = 224;
    v9 = 107;
    v10 = 25;
    v11 = 0xaa;
    v12 = 244;
    v13 = 95;
    v0 = 1;
    v14 = 7;
    idx = (&v6)[a0 >> 1 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030c830` `0x1030c830`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030c830(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 182;
    v7 = 142;
    v8 = 217;
    v9 = 0x22;
    v10 = 140;
    v11 = 137;
    v12 = 220;
    v13 = 140;
    v0 = 4;
    v14 = 7;
    idx = (&v6)[a0 >> 4 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030c940` `0x1030c940`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030c940(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 181;
    v7 = 22;
    v8 = 194;
    v9 = 87;
    v10 = 46;
    v11 = 84;
    v12 = 69;
    v13 = 184;
    v0 = 0x11;
    v14 = 7;
    idx = (&v6)[a0 >> 0x11 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030ca50` `0x1030ca50`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030ca50(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 147;
    v7 = 145;
    v8 = 16;
    v9 = 128;
    v10 = 67;
    v11 = 38;
    v12 = 143;
    v13 = 197;
    v0 = 0x11;
    v14 = 7;
    idx = (&v6)[a0 >> 0x11 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030cb60` `0x1030cb60`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030cb60(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 206;
    v7 = 181;
    v8 = 19;
    v9 = 0x22;
    v10 = 224;
    v11 = 33;
    v12 = 251;
    v13 = 16;
    v0 = 20;
    v14 = 7;
    idx = (&v6)[a0 >> 20 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

## `sub_1030cc70` `0x1030cc70`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030cc70(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int v16;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int idx;  // [bp-0x40]
    unsigned int idx1;  // [bp-0x3c]
    unsigned int *v3;  // [bp-0x38]
    unsigned int index;  // [bp-0x34]
    unsigned int v5;  // [bp-0x30]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int v11;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int v13;  // [bp-0x10]
    unsigned int v14;  // [bp-0xc]
    unsigned int v15;  // [bp-0x8]

    v6 = 154;
    v7 = 11;
    v8 = 222;
    v9 = 172;
    v10 = 33;
    v11 = 26;
    v12 = 129;
    v13 = 60;
    v0 = 21;
    v14 = 7;
    idx = (&v6)[a0 >> 21 & 7];
    index = idx / 28;
    idx1 = idx % 28;
    if (index == idx1)
        idx1 = (idx1 + 1) % 28;
    v3 = g_103a17d8[idx] ^ g_1038c290[index] ^ g_1038c290[idx1];
    v5 = g_1038f708[(&g_1038f7e8)[idx]](a1);
    v16 = v3(v5, a2);
    v15 = g_1038f778[(&g_1038f7e8)[idx]](v16);
    return v15 & 1;
}
```

