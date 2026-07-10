# elfbot.dll decompiled — jiru 0x1030cd80..0x10310c10

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1030cd80` `0x1030cd80`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030cd80(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 166;
    v7 = 177;
    v8 = 222;
    v9 = 166;
    v10 = 161;
    v11 = 7;
    v12 = 177;
    v13 = 145;
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

## `sub_1030ce90` `0x1030ce90`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030ce90(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 156;
    v7 = 80;
    v8 = 172;
    v9 = 154;
    v10 = 29;
    v11 = 37;
    v12 = 121;
    v13 = 181;
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

## `sub_1030cfa0` `0x1030cfa0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030cfa0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 31;
    v7 = 55;
    v8 = 213;
    v9 = 70;
    v10 = 0xaa;
    v11 = 23;
    v12 = 176;
    v13 = 156;
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

## `sub_1030d0b0` `0x1030d0b0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030d0b0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 33;
    v7 = 0x33;
    v8 = 21;
    v9 = 168;
    v10 = 15;
    v11 = 120;
    v12 = 192;
    v13 = 232;
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

## `sub_1030d1c0` `0x1030d1c0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030d1c0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 138;
    v7 = 0x44;
    v8 = 117;
    v9 = 0xee;
    v10 = 143;
    v11 = 116;
    v12 = 181;
    v13 = 190;
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

## `sub_1030d2d0` `0x1030d2d0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030d2d0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 72;
    v7 = 164;
    v8 = 189;
    v9 = 191;
    v10 = 99;
    v11 = 72;
    v12 = 82;
    v13 = 156;
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

## `sub_1030d3e0` `0x1030d3e0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030d3e0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 54;
    v7 = 23;
    v8 = 232;
    v9 = 202;
    v10 = 107;
    v11 = 224;
    v12 = 118;
    v13 = 9;
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

## `sub_1030d4f0` `0x1030d4f0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030d4f0(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 104;
    v8 = 237;
    v9 = 132;
    v10 = 188;
    v11 = 236;
    v12 = 29;
    v13 = 33;
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

## `sub_1030d600` `0x1030d600`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030d600(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 114;
    v7 = 247;
    v8 = 6;
    v9 = 82;
    v10 = 186;
    v11 = 8;
    v12 = 143;
    v13 = 208;
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

## `sub_1030d710` `0x1030d710`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030d710(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 213;
    v7 = 206;
    v8 = 112;
    v9 = 20;
    v10 = 160;
    v11 = 246;
    v12 = 86;
    v13 = 231;
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

## `sub_1030d820` `0x1030d820`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030d820(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 28;
    v7 = 26;
    v8 = 22;
    v9 = 174;
    v10 = 236;
    v11 = 166;
    v12 = 172;
    v13 = 201;
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

## `sub_1030d930` `0x1030d930`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030d930(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 0xee;
    v7 = 186;
    v8 = 24;
    v9 = 101;
    v10 = 13;
    v11 = 215;
    v12 = 74;
    v13 = 131;
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

## `sub_1030da40` `0x1030da40`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030da40(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 35;
    v7 = 11;
    v8 = 191;
    v9 = 3;
    v10 = 75;
    v11 = 163;
    v12 = 146;
    v13 = 126;
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

## `sub_1030db50` `0x1030db50`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030db50(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 50;
    v8 = 25;
    v9 = 69;
    v10 = 41;
    v11 = 241;
    v12 = 183;
    v13 = 32;
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

## `sub_1030dc60` `0x1030dc60`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030dc60(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 120;
    v7 = 244;
    v8 = 190;
    v9 = 174;
    v10 = 87;
    v11 = 67;
    v12 = 74;
    v13 = 14;
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

## `sub_1030dd70` `0x1030dd70`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030dd70(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 52;
    v8 = 199;
    v9 = 61;
    v10 = 69;
    v11 = 0xee;
    v12 = 168;
    v13 = 129;
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

## `sub_1030de80` `0x1030de80`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030de80(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 73;
    v7 = 115;
    v8 = 188;
    v9 = 66;
    v10 = 245;
    v11 = 150;
    v12 = 113;
    v13 = 0x11;
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

## `sub_1030df90` `0x1030df90`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030df90(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 139;
    v7 = 144;
    v8 = 179;
    v9 = 67;
    v10 = 89;
    v11 = 90;
    v12 = 107;
    v13 = 117;
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

## `sub_1030e0a0` `0x1030e0a0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030e0a0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 166;
    v7 = 147;
    v8 = 163;
    v9 = 107;
    v10 = 79;
    v11 = 41;
    v12 = 117;
    v13 = 218;
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

## `sub_1030e1b0` `0x1030e1b0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030e1b0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 44;
    v7 = 249;
    v8 = 0x22;
    v9 = 105;
    v10 = 150;
    v11 = 145;
    v12 = 66;
    v13 = 0x33;
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

## `sub_1030e2c0` `0x1030e2c0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030e2c0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 218;
    v7 = 172;
    v8 = 222;
    v9 = 1;
    v10 = 124;
    v11 = 126;
    v12 = 154;
    v13 = 212;
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

## `sub_1030e3d0` `0x1030e3d0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030e3d0(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 66;
    v8 = 92;
    v9 = 203;
    v10 = 0xee;
    v11 = 0xaa;
    v12 = 144;
    v13 = 182;
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

## `sub_1030e4e0` `0x1030e4e0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030e4e0(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 147;
    v8 = 158;
    v9 = 220;
    v10 = 39;
    v11 = 145;
    v12 = 113;
    v13 = 212;
    v0 = 12;
    v14 = 7;
    idx = (&v6)[a0 >> 12 & 7];
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

## `sub_1030e5f0` `0x1030e5f0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030e5f0(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 78;
    v8 = 183;
    v9 = 62;
    v10 = 195;
    v11 = 28;
    v12 = 240;
    v13 = 86;
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

## `sub_1030e700` `0x1030e700`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030e700(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 61;
    v7 = 130;
    v8 = 142;
    v9 = 240;
    v10 = 35;
    v11 = 240;
    v12 = 171;
    v13 = 205;
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

## `sub_1030e810` `0x1030e810`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030e810(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 0xdd;
    v8 = 143;
    v9 = 244;
    v10 = 33;
    v11 = 69;
    v12 = 64;
    v13 = 158;
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

## `sub_1030e920` `0x1030e920`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030e920(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 231;
    v7 = 59;
    v8 = 0x77;
    v9 = 131;
    v10 = 241;
    v11 = 36;
    v12 = 52;
    v13 = 138;
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

## `sub_1030ea30` `0x1030ea30`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030ea30(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 111;
    v7 = 64;
    v8 = 109;
    v9 = 43;
    v10 = 74;
    v11 = 224;
    v12 = 178;
    v13 = 79;
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

## `sub_1030eb40` `0x1030eb40`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030eb40(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 20;
    v8 = 142;
    v9 = 175;
    v10 = 55;
    v11 = 82;
    v12 = 202;
    v13 = 106;
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

## `sub_1030ec50` `0x1030ec50`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030ec50(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 117;
    v7 = 173;
    v8 = 156;
    v9 = 0x11;
    v10 = 177;
    v11 = 132;
    v12 = 144;
    v13 = 74;
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

## `sub_1030ed60` `0x1030ed60`

_256 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030ed60(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 186;
    v7 = 26;
    v8 = 164;
    v9 = 203;
    v10 = 135;
    v11 = 0x66;
    v12 = 107;
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

## `sub_1030ee60` `0x1030ee60`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030ee60(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 115;
    v7 = 79;
    v8 = 223;
    v9 = 232;
    v10 = 160;
    v11 = 225;
    v12 = 214;
    v13 = 63;
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

## `sub_1030ef70` `0x1030ef70`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030ef70(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 160;
    v7 = 76;
    v8 = 179;
    v9 = 0xee;
    v10 = 164;
    v11 = 121;
    v12 = 130;
    v13 = 28;
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

## `sub_1030f080` `0x1030f080`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030f080(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 110;
    v8 = 145;
    v9 = 78;
    v10 = 149;
    v11 = 0xee;
    v12 = 67;
    v13 = 30;
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

## `sub_1030f190` `0x1030f190`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030f190(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 224;
    v7 = 12;
    v8 = 8;
    v9 = 117;
    v10 = 213;
    v11 = 213;
    v12 = 234;
    v13 = 180;
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

## `sub_1030f2a0` `0x1030f2a0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030f2a0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 20;
    v7 = 232;
    v8 = 117;
    v9 = 71;
    v10 = 227;
    v11 = 37;
    v12 = 216;
    v13 = 73;
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

## `sub_1030f3b0` `0x1030f3b0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030f3b0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 95;
    v7 = 81;
    v8 = 70;
    v9 = 219;
    v10 = 175;
    v11 = 123;
    v12 = 26;
    v13 = 200;
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

## `sub_1030f4c0` `0x1030f4c0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030f4c0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 201;
    v7 = 167;
    v8 = 98;
    v9 = 43;
    v10 = 123;
    v11 = 174;
    v12 = 89;
    v13 = 245;
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

## `sub_1030f5d0` `0x1030f5d0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030f5d0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 0xcc;
    v7 = 180;
    v8 = 186;
    v9 = 48;
    v10 = 165;
    v11 = 47;
    v12 = 232;
    v13 = 15;
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

## `sub_1030f6e0` `0x1030f6e0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030f6e0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 220;
    v7 = 152;
    v8 = 240;
    v9 = 74;
    v10 = 62;
    v11 = 95;
    v12 = 122;
    v13 = 228;
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

## `sub_1030f7f0` `0x1030f7f0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030f7f0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 220;
    v7 = 100;
    v8 = 77;
    v9 = 161;
    v10 = 251;
    v11 = 0xbb;
    v12 = 110;
    v13 = 124;
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

## `sub_1030f900` `0x1030f900`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030f900(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 247;
    v8 = 148;
    v9 = 140;
    v10 = 185;
    v11 = 186;
    v12 = 195;
    v13 = 174;
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

## `sub_1030fa10` `0x1030fa10`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030fa10(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 81;
    v7 = 44;
    v8 = 95;
    v9 = 245;
    v10 = 209;
    v11 = 218;
    v12 = 52;
    v13 = 0x33;
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

## `sub_1030fb20` `0x1030fb20`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030fb20(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 48;
    v7 = 171;
    v8 = 210;
    v9 = 137;
    v10 = 134;
    v11 = 103;
    v12 = 69;
    v13 = 138;
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

## `sub_1030fc30` `0x1030fc30`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030fc30(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 62;
    v7 = 8;
    v8 = 230;
    v9 = 80;
    v10 = 133;
    v11 = 78;
    v12 = 180;
    v13 = 4;
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

## `sub_1030fd40` `0x1030fd40`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030fd40(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 140;
    v7 = 58;
    v8 = 28;
    v9 = 144;
    v10 = 217;
    v11 = 217;
    v12 = 41;
    v13 = 241;
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

## `sub_1030fe50` `0x1030fe50`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030fe50(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 151;
    v7 = 13;
    v8 = 28;
    v9 = 169;
    v10 = 21;
    v11 = 197;
    v12 = 93;
    v13 = 196;
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

## `sub_1030ff60` `0x1030ff60`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_1030ff60(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 42;
    v8 = 15;
    v9 = 225;
    v10 = 35;
    v11 = 59;
    v12 = 9;
    v13 = 44;
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

## `sub_10310070` `0x10310070`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10310070(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 108;
    v7 = 108;
    v8 = 157;
    v9 = 128;
    v10 = 59;
    v11 = 67;
    v12 = 209;
    v13 = 28;
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

## `sub_10310180` `0x10310180`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10310180(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 137;
    v8 = 55;
    v9 = 226;
    v10 = 98;
    v11 = 0xee;
    v12 = 31;
    v13 = 230;
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

## `sub_10310290` `0x10310290`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10310290(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 200;
    v7 = 167;
    v8 = 4;
    v9 = 145;
    v10 = 212;
    v11 = 226;
    v12 = 211;
    v13 = 237;
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

## `sub_103103a0` `0x103103a0`

_254 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_103103a0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 106;
    v7 = 131;
    v8 = 23;
    v9 = 76;
    v10 = 134;
    v11 = 41;
    v12 = 235;
    v13 = 225;
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

## `sub_103104a0` `0x103104a0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_103104a0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 235;
    v7 = 12;
    v8 = 39;
    v9 = 167;
    v10 = 133;
    v11 = 147;
    v12 = 0x99;
    v13 = 179;
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

## `sub_103105b0` `0x103105b0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_103105b0(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 208;
    v8 = 148;
    v9 = 64;
    v10 = 211;
    v11 = 246;
    v12 = 239;
    v13 = 6;
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

## `sub_103106c0` `0x103106c0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_103106c0(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 87;
    v8 = 38;
    v9 = 190;
    v10 = 95;
    v11 = 120;
    v12 = 94;
    v13 = 240;
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

## `sub_103107d0` `0x103107d0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_103107d0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 116;
    v7 = 249;
    v8 = 242;
    v9 = 45;
    v10 = 32;
    v11 = 106;
    v12 = 107;
    v13 = 12;
    v0 = 12;
    v14 = 7;
    idx = (&v6)[a0 >> 12 & 7];
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

## `sub_103108e0` `0x103108e0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_103108e0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 167;
    v7 = 31;
    v8 = 165;
    v9 = 224;
    v10 = 72;
    v11 = 203;
    v12 = 169;
    v13 = 201;
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

## `sub_103109f0` `0x103109f0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_103109f0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 191;
    v7 = 66;
    v8 = 148;
    v9 = 5;
    v10 = 228;
    v11 = 70;
    v12 = 249;
    v13 = 152;
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

## `sub_10310b00` `0x10310b00`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10310b00(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 0x88;
    v7 = 0xee;
    v8 = 28;
    v9 = 229;
    v10 = 245;
    v11 = 82;
    v12 = 173;
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

## `sub_10310c10` `0x10310c10`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10310c10(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 49;
    v7 = 79;
    v8 = 57;
    v9 = 0x55;
    v10 = 22;
    v11 = 44;
    v12 = 73;
    v13 = 224;
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

