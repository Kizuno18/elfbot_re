# elfbot.dll decompiled — jiru 0x10300f20..0x10304da0

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10300f20` `0x10300f20`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10300f20(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 108;
    v8 = 169;
    v9 = 0x99;
    v10 = 190;
    v11 = 162;
    v12 = 192;
    v13 = 129;
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

## `sub_10301030` `0x10301030`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10301030(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 132;
    v7 = 58;
    v8 = 151;
    v9 = 165;
    v10 = 107;
    v11 = 29;
    v12 = 39;
    v13 = 90;
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

## `sub_10301140` `0x10301140`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10301140(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 16;
    v7 = 22;
    v8 = 140;
    v9 = 239;
    v10 = 248;
    v11 = 127;
    v12 = 240;
    v13 = 0xaa;
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

## `sub_10301250` `0x10301250`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10301250(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 171;
    v8 = 45;
    v9 = 160;
    v10 = 196;
    v11 = 214;
    v12 = 24;
    v13 = 159;
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

## `sub_10301360` `0x10301360`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10301360(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 24;
    v8 = 0x44;
    v9 = 65;
    v10 = 152;
    v11 = 109;
    v12 = 21;
    v13 = 129;
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

## `sub_10301470` `0x10301470`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10301470(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 169;
    v7 = 57;
    v8 = 123;
    v9 = 114;
    v10 = 62;
    v11 = 192;
    v12 = 65;
    v13 = 8;
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

## `sub_10301580` `0x10301580`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10301580(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 151;
    v8 = 84;
    v9 = 240;
    v10 = 158;
    v11 = 0xcc;
    v12 = 27;
    v13 = 69;
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

## `sub_10301690` `0x10301690`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10301690(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 0x77;
    v7 = 206;
    v8 = 165;
    v9 = 148;
    v10 = 169;
    v11 = 225;
    v12 = 103;
    v13 = 27;
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

## `sub_103017a0` `0x103017a0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_103017a0(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 234;
    v8 = 235;
    v9 = 0xcc;
    v10 = 37;
    v11 = 145;
    v12 = 243;
    v13 = 219;
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

## `sub_103018b0` `0x103018b0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_103018b0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 53;
    v7 = 83;
    v8 = 44;
    v9 = 133;
    v10 = 144;
    v11 = 169;
    v12 = 219;
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

## `sub_103019c0` `0x103019c0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_103019c0(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 40;
    v8 = 66;
    v9 = 0x88;
    v10 = 103;
    v11 = 196;
    v12 = 32;
    v13 = 110;
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

## `sub_10301ad0` `0x10301ad0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10301ad0(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 62;
    v8 = 11;
    v9 = 0xbb;
    v10 = 6;
    v11 = 66;
    v12 = 224;
    v13 = 223;
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

## `sub_10301be0` `0x10301be0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10301be0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 149;
    v7 = 246;
    v8 = 207;
    v9 = 233;
    v10 = 227;
    v11 = 31;
    v12 = 24;
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

## `sub_10301cf0` `0x10301cf0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10301cf0(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 60;
    v8 = 78;
    v9 = 210;
    v10 = 0xaa;
    v11 = 167;
    v12 = 246;
    v13 = 0x88;
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

## `sub_10301e00` `0x10301e00`

_254 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10301e00(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 131;
    v8 = 131;
    v9 = 66;
    v10 = 59;
    v11 = 211;
    v12 = 3;
    v13 = 26;
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

## `sub_10301f00` `0x10301f00`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10301f00(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 169;
    v8 = 39;
    v9 = 195;
    v10 = 0;
    v11 = 122;
    v12 = 92;
    v13 = 249;
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

## `sub_10302010` `0x10302010`

_256 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10302010(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 218;
    v8 = 147;
    v9 = 25;
    v10 = 185;
    v11 = 242;
    v12 = 71;
    v13 = 7;
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

## `sub_10302110` `0x10302110`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10302110(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 0xbb;
    v7 = 182;
    v8 = 0xaa;
    v9 = 96;
    v10 = 216;
    v11 = 81;
    v12 = 66;
    v13 = 167;
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

## `sub_10302220` `0x10302220`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10302220(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 19;
    v7 = 64;
    v8 = 226;
    v9 = 217;
    v10 = 82;
    v11 = 127;
    v12 = 48;
    v13 = 93;
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

## `sub_10302330` `0x10302330`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10302330(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 248;
    v8 = 44;
    v9 = 29;
    v10 = 99;
    v11 = 14;
    v12 = 150;
    v13 = 183;
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

## `sub_10302440` `0x10302440`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10302440(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 242;
    v8 = 198;
    v9 = 246;
    v10 = 155;
    v11 = 96;
    v12 = 9;
    v13 = 75;
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

## `sub_10302550` `0x10302550`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10302550(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 53;
    v7 = 218;
    v8 = 106;
    v9 = 161;
    v10 = 97;
    v11 = 185;
    v12 = 54;
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

## `sub_10302660` `0x10302660`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10302660(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 240;
    v8 = 16;
    v9 = 116;
    v10 = 229;
    v11 = 69;
    v12 = 16;
    v13 = 0x22;
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

## `sub_10302770` `0x10302770`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10302770(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 0;
    v8 = 158;
    v9 = 21;
    v10 = 5;
    v11 = 19;
    v12 = 74;
    v13 = 133;
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

## `sub_10302880` `0x10302880`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10302880(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 121;
    v8 = 114;
    v9 = 43;
    v10 = 180;
    v11 = 88;
    v12 = 10;
    v13 = 192;
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

## `sub_10302990` `0x10302990`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10302990(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 155;
    v7 = 84;
    v8 = 152;
    v9 = 247;
    v10 = 179;
    v11 = 190;
    v12 = 194;
    v13 = 147;
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

## `sub_10302aa0` `0x10302aa0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10302aa0(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 0x11;
    v8 = 220;
    v9 = 203;
    v10 = 173;
    v11 = 96;
    v12 = 37;
    v13 = 10;
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

## `sub_10302bb0` `0x10302bb0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10302bb0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 99;
    v7 = 225;
    v8 = 108;
    v9 = 95;
    v10 = 117;
    v11 = 106;
    v12 = 126;
    v13 = 79;
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

## `sub_10302cc0` `0x10302cc0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10302cc0(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 128;
    v8 = 169;
    v9 = 38;
    v10 = 216;
    v11 = 69;
    v12 = 124;
    v13 = 52;
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

## `sub_10302dd0` `0x10302dd0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10302dd0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 164;
    v7 = 0x77;
    v8 = 36;
    v9 = 0xee;
    v10 = 7;
    v11 = 58;
    v12 = 135;
    v13 = 177;
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

## `sub_10302ee0` `0x10302ee0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10302ee0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 87;
    v7 = 169;
    v8 = 222;
    v9 = 0xaa;
    v10 = 107;
    v11 = 43;
    v12 = 63;
    v13 = 41;
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

## `sub_10302ff0` `0x10302ff0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10302ff0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 169;
    v7 = 28;
    v8 = 206;
    v9 = 70;
    v10 = 228;
    v11 = 128;
    v12 = 203;
    v13 = 47;
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

## `sub_10303100` `0x10303100`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10303100(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 8;
    v7 = 71;
    v8 = 0xaa;
    v9 = 219;
    v10 = 69;
    v11 = 112;
    v12 = 40;
    v13 = 79;
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

## `sub_10303210` `0x10303210`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10303210(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 4;
    v7 = 0x99;
    v8 = 40;
    v9 = 0x99;
    v10 = 225;
    v11 = 41;
    v12 = 99;
    v13 = 87;
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

## `sub_10303320` `0x10303320`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10303320(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 64;
    v7 = 191;
    v8 = 14;
    v9 = 21;
    v10 = 50;
    v11 = 36;
    v12 = 5;
    v13 = 165;
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

## `sub_10303430` `0x10303430`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10303430(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 206;
    v8 = 106;
    v9 = 0x55;
    v10 = 190;
    v11 = 14;
    v12 = 144;
    v13 = 222;
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

## `sub_10303540` `0x10303540`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10303540(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 232;
    v7 = 80;
    v8 = 104;
    v9 = 144;
    v10 = 16;
    v11 = 215;
    v12 = 194;
    v13 = 158;
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

## `sub_10303650` `0x10303650`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10303650(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 233;
    v7 = 128;
    v8 = 50;
    v9 = 133;
    v10 = 1;
    v11 = 239;
    v12 = 183;
    v13 = 143;
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

## `sub_10303760` `0x10303760`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10303760(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 49;
    v8 = 191;
    v9 = 164;
    v10 = 92;
    v11 = 189;
    v12 = 35;
    v13 = 196;
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

## `sub_10303870` `0x10303870`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10303870(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 113;
    v7 = 248;
    v8 = 177;
    v9 = 55;
    v10 = 99;
    v11 = 67;
    v12 = 28;
    v13 = 128;
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

## `sub_10303980` `0x10303980`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10303980(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 155;
    v7 = 159;
    v8 = 163;
    v9 = 40;
    v10 = 134;
    v11 = 49;
    v12 = 226;
    v13 = 233;
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

## `sub_10303a90` `0x10303a90`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10303a90(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v8 = 210;
    v9 = 123;
    v10 = 196;
    v11 = 77;
    v12 = 179;
    v13 = 0x11;
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

## `sub_10303ba0` `0x10303ba0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10303ba0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 155;
    v7 = 172;
    v8 = 9;
    v9 = 112;
    v10 = 115;
    v11 = 94;
    v12 = 106;
    v13 = 1;
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

## `sub_10303cb0` `0x10303cb0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10303cb0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 109;
    v7 = 135;
    v8 = 0x88;
    v9 = 52;
    v10 = 132;
    v11 = 12;
    v12 = 77;
    v13 = 233;
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

## `sub_10303dc0` `0x10303dc0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10303dc0(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 19;
    v8 = 87;
    v9 = 157;
    v10 = 65;
    v11 = 0x33;
    v12 = 203;
    v13 = 77;
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

## `sub_10303ed0` `0x10303ed0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10303ed0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 55;
    v7 = 200;
    v8 = 200;
    v9 = 2;
    v10 = 235;
    v11 = 147;
    v12 = 207;
    v13 = 0xdd;
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

## `sub_10303fe0` `0x10303fe0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10303fe0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 222;
    v7 = 146;
    v8 = 18;
    v9 = 62;
    v10 = 36;
    v11 = 231;
    v12 = 27;
    v13 = 120;
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

## `sub_103040f0` `0x103040f0`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_103040f0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 146;
    v7 = 41;
    v8 = 244;
    v9 = 2;
    v10 = 15;
    v11 = 161;
    v12 = 145;
    v13 = 175;
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

## `sub_10304200` `0x10304200`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10304200(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 196;
    v7 = 152;
    v8 = 149;
    v9 = 111;
    v10 = 122;
    v11 = 230;
    v12 = 50;
    v13 = 5;
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

## `sub_10304310` `0x10304310`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10304310(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 53;
    v8 = 59;
    v9 = 244;
    v10 = 206;
    v11 = 66;
    v12 = 141;
    v13 = 24;
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

## `sub_10304420` `0x10304420`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10304420(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 131;
    v8 = 218;
    v9 = 193;
    v10 = 5;
    v11 = 30;
    v12 = 70;
    v13 = 245;
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

## `sub_10304530` `0x10304530`

_254 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10304530(unsigned int a0, unsigned int a1, unsigned int a2)
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
    v7 = 32;
    v8 = 96;
    v9 = 251;
    v10 = 0xee;
    v11 = 140;
    v12 = 53;
    v13 = 179;
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

## `sub_10304630` `0x10304630`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10304630(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 88;
    v7 = 184;
    v8 = 28;
    v9 = 234;
    v10 = 180;
    v11 = 100;
    v12 = 201;
    v13 = 145;
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

## `sub_10304740` `0x10304740`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10304740(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 99;
    v7 = 154;
    v8 = 227;
    v9 = 208;
    v10 = 196;
    v11 = 5;
    v12 = 95;
    v13 = 53;
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

## `sub_10304850` `0x10304850`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10304850(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 246;
    v7 = 0x22;
    v8 = 48;
    v9 = 202;
    v10 = 143;
    v11 = 88;
    v12 = 139;
    v13 = 129;
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

## `sub_10304960` `0x10304960`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10304960(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 109;
    v7 = 4;
    v8 = 93;
    v9 = 172;
    v10 = 182;
    v11 = 0x55;
    v12 = 18;
    v13 = 18;
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

## `sub_10304a70` `0x10304a70`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10304a70(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 121;
    v7 = 59;
    v8 = 92;
    v9 = 212;
    v10 = 26;
    v11 = 138;
    v12 = 140;
    v13 = 92;
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

## `sub_10304b80` `0x10304b80`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10304b80(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 39;
    v7 = 223;
    v8 = 126;
    v9 = 138;
    v10 = 94;
    v11 = 222;
    v12 = 61;
    v13 = 124;
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

## `sub_10304c90` `0x10304c90`

_257 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10304c90(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 0x66;
    v7 = 124;
    v8 = 72;
    v9 = 0x88;
    v10 = 16;
    v11 = 193;
    v12 = 0xee;
    v13 = 161;
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

## `sub_10304da0` `0x10304da0`

_254 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290[4];
extern unsigned int g_1038f708[4];
extern unsigned int g_1038f778[4];
extern char g_1038f7e8;
extern unsigned int g_103a17d8[4];

unsigned int sub_10304da0(unsigned int a0, unsigned int a1, unsigned int a2)
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

    v6 = 192;
    v7 = 129;
    v8 = 79;
    v9 = 0xdd;
    v10 = 41;
    v11 = 18;
    v12 = 75;
    v13 = 229;
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

