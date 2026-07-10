# elfbot.dll decompiled — jiru 0x103717be..0x10373280

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_103717be` `0x103717be`

_26 bytes. (leaf/helper — see body)_

```c
int sub_103717be(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_103717e0` `0x103717e0`

_14 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a3af8;

unsigned int sub_103717e0(void)
{
    unsigned int v1;  // eax

    v1 = g_103a3af8;
    g_103a3af8 = v1 & 4294967294;
    return v1 & 4294967294;
}
```

## `sub_103717ee` `0x103717ee`

_26 bytes. (leaf/helper — see body)_

```c
int sub_103717ee(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_10371810` `0x10371810`

_14 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a3b18;

unsigned int sub_10371810(void)
{
    unsigned int v1;  // eax

    v1 = g_103a3b18;
    g_103a3b18 = v1 & 4294967294;
    return v1 & 4294967294;
}
```

## `sub_1037181e` `0x1037181e`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1037181e(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_10371840` `0x10371840`

_14 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a3b38;

unsigned int sub_10371840(void)
{
    unsigned int v1;  // eax

    v1 = g_103a3b38;
    g_103a3b38 = v1 & 4294967294;
    return v1 & 4294967294;
}
```

## `sub_1037184e` `0x1037184e`

_25 bytes. (leaf/helper — see body)_

```c
int sub_1037184e(void)
{
    unsigned int v1;  // [bp+0xfffd8]

    if (!((char)v1 & 1))
        return v1 & 1;
    v1 &= 4294967294;
    return (unsigned int)sub_10314610(/* unsupported instruction */ - 40);
}
```

## `sub_10371867` `0x10371867`

_25 bytes. (leaf/helper — see body)_

```c
int sub_10371867(void)
{
    unsigned int v1;  // [bp+0xfffd8]
    int v2;  // [bp+0x100008]

    if (!((char)v1 & 2))
        return v1 & 2;
    v1 &= 4294967293;
    return (unsigned int)sub_10314610(v2);
}
```

## `sub_10371880` `0x10371880`

_27 bytes. (leaf/helper — see body)_

```c
int sub_10371880(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_103718a0` `0x103718a0`

_25 bytes. (leaf/helper — see body)_

```c
int sub_103718a0(void)
{
    int v1;  // [bp+0xfffd0]
    unsigned int v2;  // [bp+0xfffd4]

    if (!((char)v2 & 1))
        return v2 & 1;
    v2 &= 4294967294;
    return (unsigned int)sub_10314610(v1);
}
```

## `sub_103718b9` `0x103718b9`

_8 bytes. (leaf/helper — see body)_

```c
void sub_103718b9(void)
{
    sub_10314610(/* unsupported instruction */ - 44);
    return;
}
```

## `sub_103718c1` `0x103718c1`

_40 bytes. (leaf/helper — see body)_

```c
int sub_103718c1(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_103718f0` `0x103718f0`

_8 bytes. (leaf/helper — see body)_

```c
unsigned int sub_103718f0(void)
{
    return sub_103698d0(/* unsupported instruction */ + 4);
}
```

## `sub_103718f8` `0x103718f8`

_8 bytes. (leaf/helper — see body)_

```c
int sub_103718f8(void)
{
    return sub_103698f0(/* unsupported instruction */ - 16);
}
```

## `sub_10371900` `0x10371900`

_27 bytes. (leaf/helper — see body)_

```c
int sub_10371900(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_10371920` `0x10371920`

_8 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10371920(void)
{
    return sub_10369ac0(/* unsupported instruction */ - 16);
}
```

## `sub_10371928` `0x10371928`

_27 bytes. (leaf/helper — see body)_

```c
int sub_10371928(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_10371950` `0x10371950`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a1794;

int sub_10371950(void)
{
    g_103a1794 = sub_10368c80();
    return g_103a1794;
}
```

## `sub_10371960` `0x10371960`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a1798;

int sub_10371960(void)
{
    g_103a1798 = sub_10368cf0();
    return g_103a1798;
}
```

## `sub_10371970` `0x10371970`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a17a0;

int sub_10371970(void)
{
    g_103a17a0 = sub_10368cf0();
    return g_103a17a0;
}
```

## `sub_10371980` `0x10371980`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a178c;

int sub_10371980(void)
{
    g_103a178c = sub_10368cf0();
    return g_103a178c;
}
```

## `sub_10371990` `0x10371990`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a1790;

int sub_10371990(void)
{
    g_103a1790 = sub_10368c80();
    return g_103a1790;
}
```

## `sub_103719a0` `0x103719a0`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a1785;

int sub_103719a0(void)
{
    return sub_1031a280(&g_103a1785);
}
```

## `sub_103719b0` `0x103719b0`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a1789;

int sub_103719b0(void)
{
    return sub_1031a280(&g_103a1789);
}
```

## `sub_103719c0` `0x103719c0`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a178b;

int sub_103719c0(void)
{
    return sub_1031a280(&g_103a178b);
}
```

## `sub_103719d0` `0x103719d0`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a1788;

int sub_103719d0(void)
{
    return sub_1031a280(&g_103a1788);
}
```

## `sub_103719e0` `0x103719e0`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a1786;

int sub_103719e0(void)
{
    return sub_1031a280(&g_103a1786);
}
```

## `sub_103719f0` `0x103719f0`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a179c;

int sub_103719f0(void)
{
    return sub_1031a280(&g_103a179c);
}
```

## `sub_10371a00` `0x10371a00`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a178a;

int sub_10371a00(void)
{
    return sub_1031a280(&g_103a178a);
}
```

## `sub_10371a10` `0x10371a10`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a1784;

int sub_10371a10(void)
{
    return sub_1031a280(&g_103a1784);
}
```

## `sub_10371a20` `0x10371a20`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a1787;

int sub_10371a20(void)
{
    return sub_1031a280(&g_103a1787);
}
```

## `sub_10371a30` `0x10371a30`

_17 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a17a8;

unsigned int * sub_10371a30(void)
{
    return sub_1033a4c0(&g_103a17a8, 0);
}
```

## `sub_10371a50` `0x10371a50`

_17 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a17ac;

unsigned int * sub_10371a50(void)
{
    return sub_1033a4c0(&g_103a17ac, 0);
}
```

## `sub_10371a70` `0x10371a70`

_17 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a17a4;

unsigned int * sub_10371a70(void)
{
    return sub_1033a4c0(&g_103a17a4, 0);
}
```

## `sub_10371a90` `0x10371a90`

_17 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a17b0;

unsigned int * sub_10371a90(void)
{
    return sub_1033a4c0(&g_103a17b0, 0);
}
```

## `sub_10371ab0` `0x10371ab0`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a17c8;

int sub_10371ab0(void)
{
    g_103a17c8 = sub_10368c80();
    return g_103a17c8;
}
```

## `sub_10371ac0` `0x10371ac0`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a17cc;

int sub_10371ac0(void)
{
    g_103a17cc = sub_10368cf0();
    return g_103a17cc;
}
```

## `sub_10371ad0` `0x10371ad0`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a17d4;

int sub_10371ad0(void)
{
    g_103a17d4 = sub_10368cf0();
    return g_103a17d4;
}
```

## `sub_10371ae0` `0x10371ae0`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a17c0;

int sub_10371ae0(void)
{
    g_103a17c0 = sub_10368cf0();
    return g_103a17c0;
}
```

## `sub_10371af0` `0x10371af0`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a17c4;

int sub_10371af0(void)
{
    g_103a17c4 = sub_10368c80();
    return g_103a17c4;
}
```

## `sub_10371b00` `0x10371b00`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a17bb;

int sub_10371b00(void)
{
    return sub_1031a280(&g_103a17bb);
}
```

## `sub_10371b10` `0x10371b10`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a17bd;

int sub_10371b10(void)
{
    return sub_1031a280(&g_103a17bd);
}
```

## `sub_10371b20` `0x10371b20`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a17bf;

int sub_10371b20(void)
{
    return sub_1031a280(&g_103a17bf);
}
```

## `sub_10371b30` `0x10371b30`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a17bc;

int sub_10371b30(void)
{
    return sub_1031a280(&g_103a17bc);
}
```

## `sub_10371b40` `0x10371b40`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a17b9;

int sub_10371b40(void)
{
    return sub_1031a280(&g_103a17b9);
}
```

## `sub_10371b50` `0x10371b50`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a17d0;

int sub_10371b50(void)
{
    return sub_1031a280(&g_103a17d0);
}
```

## `sub_10371b60` `0x10371b60`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a17be;

int sub_10371b60(void)
{
    return sub_1031a280(&g_103a17be);
}
```

## `sub_10371b70` `0x10371b70`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a17ba;

int sub_10371b70(void)
{
    return sub_1031a280(&g_103a17ba);
}
```

## `sub_10371b80` `0x10371b80`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a17b8;

int sub_10371b80(void)
{
    return sub_1031a280(&g_103a17b8);
}
```

## `sub_10371b90` `0x10371b90`

_5717 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c290;
extern unsigned int g_1038c294;
extern unsigned int g_1038c298;
extern unsigned int g_1038c29c;
extern unsigned int g_1038c2a0;
extern unsigned int g_1038c2a4;
extern unsigned int g_1038c2a8;
extern unsigned int g_1038c2ac;
extern unsigned int g_1038c2b0;
extern unsigned int g_1038c2b4;
extern unsigned int g_1038c2b8;
extern unsigned int g_1038c2bc;
extern unsigned int g_1038c2c0;
extern unsigned int g_1038c2c4;
extern unsigned int g_1038c2c8;
extern unsigned int g_1038c2cc;
extern unsigned int g_1038c2d0;
extern unsigned int g_1038c2d4;
extern unsigned int g_1038c2d8;
extern unsigned int g_1038c2dc;
extern unsigned int g_1038c2e0;
extern unsigned int g_1038c2e4;
extern unsigned int g_1038c2e8;
extern unsigned int g_1038c2ec;
extern unsigned int g_1038c2f0;
extern unsigned int g_1038c2f4;
extern unsigned int g_1038c2f8;
extern unsigned int g_1038c2fc;
extern char g_103a17d8;
extern char g_103a17dc;
extern char g_103a17e0;
extern char g_103a17e4;
extern char g_103a17e8;
extern char g_103a17ec;
extern char g_103a17f0;
extern char g_103a17f4;
extern char g_103a17f8;
extern char g_103a17fc;
extern char g_103a1800;
extern char g_103a1804;
extern char g_103a1808;
extern char g_103a180c;
extern char g_103a1810;
extern char g_103a1814;
extern char g_103a1818;
extern char g_103a181c;
extern char g_103a1820;
extern char g_103a1824;
extern char g_103a1828;
extern char g_103a182c;
extern char g_103a1830;
extern char g_103a1834;
extern char g_103a1838;
extern char g_103a183c;
extern char g_103a1840;
extern char g_103a1844;
extern char g_103a1848;
extern char g_103a184c;
extern char g_103a1850;
extern char g_103a1854;
extern char g_103a1858;
extern char g_103a185c;
extern char g_103a1860;
extern char g_103a1864;
extern char g_103a1868;
extern char g_103a186c;
extern char g_103a1870;
extern char g_103a1874;
extern char g_103a1878;
extern char g_103a187c;
extern char g_103a1880;
extern char g_103a1884;
extern char g_103a1888;
extern char g_103a188c;
extern char g_103a1890;
extern char g_103a1894;
extern char g_103a1898;
extern char g_103a189c;
extern char g_103a18a0;
extern char g_103a18a4;
extern char g_103a18a8;
extern char g_103a18ac;
extern char g_103a18b0;
extern char g_103a18b4;
extern char g_103a18b8;
extern char g_103a18bc;
extern char g_103a18c0;
extern char g_103a18c4;
extern char g_103a18c8;
extern char g_103a18cc;
extern char g_103a18d0;
extern char g_103a18d4;
extern char g_103a18d8;
extern char g_103a18dc;
extern char g_103a18e0;
extern char g_103a18e4;
extern char g_103a18e8;
extern char g_103a18ec;
extern char g_103a18f0;
extern char g_103a18f4;
extern char g_103a18f8;
extern char g_103a18fc;
extern char g_103a1900;
extern char g_103a1904;
extern char g_103a1908;
extern char g_103a190c;
extern char g_103a1910;
extern char g_103a1914;
extern char g_103a1918;
extern char g_103a191c;
extern char g_103a1920;
extern char g_103a1924;
extern char g_103a1928;
extern char g_103a192c;
extern char g_103a1930;
extern char g_103a1934;
extern char g_103a1938;
extern char g_103a193c;
extern char g_103a1940;
extern char g_103a1944;
extern char g_103a1948;
extern char g_103a194c;
extern char g_103a1950;
extern char g_103a1954;
extern char g_103a1958;
extern char g_103a195c;
extern char g_103a1960;
extern char g_103a1964;
extern char g_103a1968;
extern char g_103a196c;
extern char g_103a1970;
extern char g_103a1974;
extern char g_103a1978;
extern char g_103a197c;
extern char g_103a1980;
extern char g_103a1984;
extern char g_103a1988;
extern char g_103a198c;
extern char g_103a1990;
extern char g_103a1994;
extern char g_103a1998;
extern char g_103a199c;
extern char g_103a19a0;
extern char g_103a19a4;
extern char g_103a19a8;
extern char g_103a19ac;
extern char g_103a19b0;
extern char g_103a19b4;
extern char g_103a19b8;
extern char g_103a19bc;
extern char g_103a19c0;
extern char g_103a19c4;
extern char g_103a19c8;
extern char g_103a19cc;
extern char g_103a19d0;
extern char g_103a19d4;
extern char g_103a19d8;
extern char g_103a19dc;
extern char g_103a19e0;
extern char g_103a19e4;
extern char g_103a19e8;
extern char g_103a19ec;
extern char g_103a19f0;
extern char g_103a19f4;
extern char g_103a19f8;
extern char g_103a19fc;
extern char g_103a1a00;
extern char g_103a1a04;
extern char g_103a1a08;
extern char g_103a1a0c;
extern char g_103a1a10;
extern char g_103a1a14;
extern char g_103a1a18;
extern char g_103a1a1c;
extern char g_103a1a20;
extern char g_103a1a24;
extern char g_103a1a28;
extern char g_103a1a2c;
extern char g_103a1a30;
extern char g_103a1a34;
extern char g_103a1a38;
extern char g_103a1a3c;
extern char g_103a1a40;
extern char g_103a1a44;
extern char g_103a1a48;
extern char g_103a1a4c;
extern char g_103a1a50;
extern char g_103a1a54;
extern char g_103a1a58;
extern char g_103a1a5c;
extern char g_103a1a60;
extern char g_103a1a64;
extern char g_103a1a68;
extern char g_103a1a6c;
extern char g_103a1a70;
extern char g_103a1a74;
extern char g_103a1a78;
extern char g_103a1a7c;
extern char g_103a1a80;
extern char g_103a1a84;
extern char g_103a1a88;
extern char g_103a1a8c;
extern char g_103a1a90;
extern char g_103a1a94;
extern char g_103a1a98;
extern char g_103a1a9c;
extern char g_103a1aa0;
extern char g_103a1aa4;
extern char g_103a1aa8;
extern char g_103a1aac;
extern char g_103a1ab0;
extern char g_103a1ab4;
extern char g_103a1ab8;
extern char g_103a1abc;
extern char g_103a1ac0;
extern char g_103a1ac4;
extern char g_103a1ac8;
extern char g_103a1acc;
extern char g_103a1ad0;
extern char g_103a1ad4;
extern char g_103a1ad8;
extern char g_103a1adc;
extern char g_103a1ae0;
extern char g_103a1ae4;
extern char g_103a1ae8;
extern char g_103a1aec;
extern char g_103a1af0;
extern char g_103a1af4;
extern char g_103a1af8;
extern char g_103a1afc;
extern char g_103a1b00;
extern char g_103a1b04;
extern char g_103a1b08;
extern char g_103a1b0c;
extern char g_103a1b10;
extern char g_103a1b14;
extern char g_103a1b18;
extern char g_103a1b1c;
extern char g_103a1b20;
extern char g_103a1b24;
extern char g_103a1b28;
extern char g_103a1b2c;
extern char g_103a1b30;
extern char g_103a1b34;
extern char g_103a1b38;
extern char g_103a1b3c;
extern char g_103a1b40;
extern char g_103a1b44;
extern char g_103a1b48;
extern char g_103a1b4c;
extern char g_103a1b50;
extern char g_103a1b54;
extern char g_103a1b58;
extern char g_103a1b5c;
extern char g_103a1b60;
extern char g_103a1b64;
extern char g_103a1b68;
extern char g_103a1b6c;
extern char g_103a1b70;
extern char g_103a1b74;
extern char g_103a1b78;
extern char g_103a1b7c;
extern char g_103a1b80;
extern char g_103a1b84;
extern char g_103a1b88;
extern char g_103a1b8c;
extern char g_103a1b90;
extern char g_103a1b94;
extern char g_103a1b98;
extern char g_103a1b9c;
extern char g_103a1ba0;
extern char g_103a1ba4;
extern char g_103a1ba8;
extern char g_103a1bac;
extern char g_103a1bb0;
extern char g_103a1bb4;
extern char g_103a1bb8;
extern unsigned int g_103a1bbc;
extern char g_103a1bc0;
extern char g_103a1bc4;

int sub_10371b90(void)
{
    *((unsigned int *)&g_103a17d8) = sub_102fff10 ^ g_1038c290 ^ g_1038c294;
    *((unsigned int *)&g_103a17dc) = sub_102f5260 ^ g_1038c290 ^ g_1038c294;
    *((unsigned int *)&g_103a17e0) = sub_102fe830 ^ g_1038c290 ^ g_1038c298;
    *((unsigned int *)&g_103a17e4) = sub_102f6b90 ^ g_1038c290 ^ g_1038c29c;
    *((unsigned int *)&g_103a17e8) = sub_102f99a0 ^ g_1038c290 ^ g_1038c2a0;
    *((unsigned int *)&g_103a17ec) = sub_102fd770 ^ g_1038c290 ^ g_1038c2a4;
    *((unsigned int *)&g_103a17f0) = sub_102fb600 ^ g_1038c290 ^ g_1038c2a8;
    *((unsigned int *)&g_103a17f4) = sub_102fc180 ^ g_1038c290 ^ g_1038c2ac;
    *((unsigned int *)&g_103a17f8) = sub_102fb2c0 ^ g_1038c290 ^ g_1038c2b0;
    *((unsigned int *)&g_103a17fc) = sub_102f55f0 ^ g_1038c290 ^ g_1038c2b4;
    *((unsigned int *)&g_103a1800) = sub_102f5a00 ^ g_1038c290 ^ g_1038c2b8;
    *((unsigned int *)&g_103a1804) = sub_102f3180 ^ g_1038c290 ^ g_1038c2bc;
    *((unsigned int *)&g_103a1808) = sub_102febc0 ^ g_1038c290 ^ g_1038c2c0;
    *((unsigned int *)&g_103a180c) = sub_102ff730 ^ g_1038c290 ^ g_1038c2c4;
    *((unsigned int *)&g_103a1810) = sub_102f7bc0 ^ g_1038c290 ^ g_1038c2c8;
    *((unsigned int *)&g_103a1814) = sub_102f3c20 ^ g_1038c290 ^ g_1038c2cc;
    *((unsigned int *)&g_103a1818) = sub_102fde10 ^ g_1038c290 ^ g_1038c2d0;
    *((unsigned int *)&g_103a181c) = sub_102fdd80 ^ g_1038c290 ^ g_1038c2d4;
    *((unsigned int *)&g_103a1820) = sub_102f8bd0 ^ g_1038c290 ^ g_1038c2d8;
    *((unsigned int *)&g_103a1824) = sub_102f4090 ^ g_1038c290 ^ g_1038c2dc;
    *((unsigned int *)&g_103a1828) = sub_102f63f0 ^ g_1038c290 ^ g_1038c2e0;
    *((unsigned int *)&g_103a182c) = sub_102f3620 ^ g_1038c290 ^ g_1038c2e4;
    *((unsigned int *)&g_103a1830) = sub_102fcb70 ^ g_1038c290 ^ g_1038c2e8;
    *((unsigned int *)&g_103a1834) = sub_102f4300 ^ g_1038c290 ^ g_1038c2ec;
    *((unsigned int *)&g_103a1838) = sub_102f9db0 ^ g_1038c290 ^ g_1038c2f0;
    *((unsigned int *)&g_103a183c) = sub_102f9560 ^ g_1038c290 ^ g_1038c2f4;
    *((unsigned int *)&g_103a1840) = sub_102fa610 ^ g_1038c290 ^ g_1038c2f8;
    *((unsigned int *)&g_103a1844) = sub_102fe8e0 ^ g_1038c290 ^ g_1038c2fc;
    *((unsigned int *)&g_103a1848) = sub_102fa010 ^ g_1038c294 ^ g_1038c290;
    *((unsigned int *)&g_103a184c) = sub_102fef20 ^ g_1038c294 ^ g_1038c298;
    *((unsigned int *)&g_103a1850) = sub_102f5d90 ^ g_1038c294 ^ g_1038c298;
    *((unsigned int *)&g_103a1854) = sub_102f6850 ^ g_1038c294 ^ g_1038c29c;
    *((unsigned int *)&g_103a1858) = sub_102f7740 ^ g_1038c294 ^ g_1038c2a0;
    *((unsigned int *)&g_103a185c) = sub_102f6a90 ^ g_1038c294 ^ g_1038c2a4;
    *((unsigned int *)&g_103a1860) = sub_102fbd40 ^ g_1038c294 ^ g_1038c2a8;
    *((unsigned int *)&g_103a1864) = sub_102f53e0 ^ g_1038c294 ^ g_1038c2ac;
    *((unsigned int *)&g_103a1868) = sub_102fd890 ^ g_1038c294 ^ g_1038c2b0;
    *((unsigned int *)&g_103a186c) = sub_102f8a60 ^ g_1038c294 ^ g_1038c2b4;
    *((unsigned int *)&g_103a1870) = sub_102f7df0 ^ g_1038c294 ^ g_1038c2b8;
    *((unsigned int *)&g_103a1874) = sub_102fd0f0 ^ g_1038c294 ^ g_1038c2bc;
    *((unsigned int *)&g_103a1878) = sub_102fea30 ^ g_1038c294 ^ g_1038c2c0;
    *((unsigned int *)&g_103a187c) = sub_102f5720 ^ g_1038c294 ^ g_1038c2c4;
    *((unsigned int *)&g_103a1880) = sub_102f3a40 ^ g_1038c294 ^ g_1038c2c8;
    *((unsigned int *)&g_103a1884) = sub_102f4150 ^ g_1038c294 ^ g_1038c2cc;
    *((unsigned int *)&g_103a1888) = sub_102ff2e0 ^ g_1038c294 ^ g_1038c2d0;
    *((unsigned int *)&g_103a188c) = sub_102f3860 ^ g_1038c294 ^ g_1038c2d4;
    *((unsigned int *)&g_103a1890) = sub_102f6c50 ^ g_1038c294 ^ g_1038c2d8;
    *((unsigned int *)&g_103a1894) = sub_102fead0 ^ g_1038c294 ^ g_1038c2dc;
    *((unsigned int *)&g_103a1898) = sub_102f94c0 ^ g_1038c294 ^ g_1038c2e0;
    *((unsigned int *)&g_103a189c) = sub_102f38e0 ^ g_1038c294 ^ g_1038c2e4;
    *((unsigned int *)&g_103a18a0) = sub_102f96e0 ^ g_1038c294 ^ g_1038c2e8;
    *((unsigned int *)&g_103a18a4) = sub_102f4000 ^ g_1038c294 ^ g_1038c2ec;
    *((unsigned int *)&g_103a18a8) = sub_102f34a0 ^ g_1038c294 ^ g_1038c2f0;
    *((unsigned int *)&g_103a18ac) = sub_102fc2b0 ^ g_1038c294 ^ g_1038c2f4;
    *((unsigned int *)&g_103a18b0) = sub_102f5e20 ^ g_1038c294 ^ g_1038c2f8;
    *((unsigned int *)&g_103a18b4) = sub_102fcdc0 ^ g_1038c294 ^ g_1038c2fc;
    *((unsigned int *)&g_103a18b8) = sub_102fd040 ^ g_1038c298 ^ g_1038c290;
    *((unsigned int *)&g_103a18bc) = sub_102f5330 ^ g_1038c298 ^ g_1038c294;
    *((unsigned int *)&g_103a18c0) = sub_102f3f10 ^ g_1038c298 ^ g_1038c29c;
    *((unsigned int *)&g_103a18c4) = sub_102f4ae0 ^ g_1038c298 ^ g_1038c29c;
    *((unsigned int *)&g_103a18c8) = sub_102fd490 ^ g_1038c298 ^ g_1038c2a0;
    *((unsigned int *)&g_103a18cc) = sub_10300070 ^ g_1038c298 ^ g_1038c2a4;
    *((unsigned int *)&g_103a18d0) = sub_102f7ec0 ^ g_1038c298 ^ g_1038c2a8;
    *((unsigned int *)&g_103a18d4) = sub_102f7460 ^ g_1038c298 ^ g_1038c2ac;
    *((unsigned int *)&g_103a18d8) = sub_102fb850 ^ g_1038c298 ^ g_1038c2b0;
    *((unsigned int *)&g_103a18dc) = sub_102fb7c0 ^ g_1038c298 ^ g_1038c2b4;
    *((unsigned int *)&g_103a18e0) = sub_102fae50 ^ g_1038c298 ^ g_1038c2b8;
    *((unsigned int *)&g_103a18e4) = sub_102fd800 ^ g_1038c298 ^ g_1038c2bc;
    *((unsigned int *)&g_103a18e8) = sub_102fd540 ^ g_1038c298 ^ g_1038c2c0;
    *((unsigned int *)&g_103a18ec) = sub_102f7c60 ^ g_1038c298 ^ g_1038c2c4;
    *((unsigned int *)&g_103a18f0) = sub_102f45d0 ^ g_1038c298 ^ g_1038c2c8;
    *((unsigned int *)&g_103a18f4) = sub_102f7b30 ^ g_1038c298 ^ g_1038c2cc;
    *((unsigned int *)&g_103a18f8) = sub_102f8b10 ^ g_1038c298 ^ g_1038c2d0;
    *((unsigned int *)&g_103a18fc) = sub_102fefe0 ^ g_1038c298 ^ g_1038c2d4;
    *((unsigned int *)&g_103a1900) = sub_102f9c20 ^ g_1038c298 ^ g_1038c2d8;
    *((unsigned int *)&g_103a1904) = sub_102f6650 ^ g_1038c298 ^ g_1038c2dc;
    *((unsigned int *)&g_103a1908) = sub_102fc930 ^ g_1038c298 ^ g_1038c2e0;
    *((unsigned int *)&g_103a190c) = sub_102fc5a0 ^ g_1038c298 ^ g_1038c2e4;
    *((unsigned int *)&g_103a1910) = sub_102f4410 ^ g_1038c298 ^ g_1038c2e8;
    *((unsigned int *)&g_103a1914) = sub_102ff380 ^ g_1038c298 ^ g_1038c2ec;
    *((unsigned int *)&g_103a1918) = sub_102f7d40 ^ g_1038c298 ^ g_1038c2f0;
    *((unsigned int *)&g_103a191c) = sub_102f9010 ^ g_1038c298 ^ g_1038c2f4;
    *((unsigned int *)&g_103a1920) = sub_102face0 ^ g_1038c298 ^ g_1038c2f8;
    *((unsigned int *)&g_103a1924) = sub_102fcc00 ^ g_1038c298 ^ g_1038c2fc;
    *((unsigned int *)&g_103a1928) = sub_102fa3b0 ^ g_1038c29c ^ g_1038c290;
    *((unsigned int *)&g_103a192c) = sub_102fe040 ^ g_1038c29c ^ g_1038c294;
    *((unsigned int *)&g_103a1930) = sub_102f9b80 ^ g_1038c29c ^ g_1038c298;
    *((unsigned int *)&g_103a1934) = sub_102faf30 ^ g_1038c29c ^ g_1038c2a0;
    *((unsigned int *)&g_103a1938) = sub_102ff4e0 ^ g_1038c29c ^ g_1038c2a0;
    *((unsigned int *)&g_103a193c) = sub_102fde90 ^ g_1038c29c ^ g_1038c2a4;
    *((unsigned int *)&g_103a1940) = sub_102fbdf0 ^ g_1038c29c ^ g_1038c2a8;
    *((unsigned int *)&g_103a1944) = sub_102f79f0 ^ g_1038c29c ^ g_1038c2ac;
    *((unsigned int *)&g_103a1948) = sub_102f8dd0 ^ g_1038c29c ^ g_1038c2b0;
    *((unsigned int *)&g_103a194c) = sub_102f3790 ^ g_1038c29c ^ g_1038c2b4;
    *((unsigned int *)&g_103a1950) = sub_102fe6e0 ^ g_1038c29c ^ g_1038c2b8;
    *((unsigned int *)&g_103a1954) = sub_102f8c70 ^ g_1038c29c ^ g_1038c2bc;
    *((unsigned int *)&g_103a1958) = sub_102fd980 ^ g_1038c29c ^ g_1038c2c0;
    *((unsigned int *)&g_103a195c) = sub_102f90f0 ^ g_1038c29c ^ g_1038c2c4;
    *((unsigned int *)&g_103a1960) = sub_102f6d20 ^ g_1038c29c ^ g_1038c2c8;
    *((unsigned int *)&g_103a1964) = sub_102f8790 ^ g_1038c29c ^ g_1038c2cc;
    *((unsigned int *)&g_103a1968) = sub_102f6070 ^ g_1038c29c ^ g_1038c2d0;
    *((unsigned int *)&g_103a196c) = sub_102fda50 ^ g_1038c29c ^ g_1038c2d4;
    *((unsigned int *)&g_103a1970) = sub_102f6e80 ^ g_1038c29c ^ g_1038c2d8;
    *((unsigned int *)&g_103a1974) = sub_102fb010 ^ g_1038c29c ^ g_1038c2dc;
    *((unsigned int *)&g_103a1978) = sub_102f8700 ^ g_1038c29c ^ g_1038c2e0;
    *((unsigned int *)&g_103a197c) = sub_102f4250 ^ g_1038c29c ^ g_1038c2e4;
    *((unsigned int *)&g_103a1980) = sub_102fbb00 ^ g_1038c29c ^ g_1038c2e8;
    *((unsigned int *)&g_103a1984) = sub_102f4f80 ^ g_1038c29c ^ g_1038c2ec;
    *((unsigned int *)&g_103a1988) = sub_102f8070 ^ g_1038c29c ^ g_1038c2f0;
    *((unsigned int *)&g_103a198c) = sub_102fa210 ^ g_1038c29c ^ g_1038c2f4;
    *((unsigned int *)&g_103a1990) = sub_102f4870 ^ g_1038c29c ^ g_1038c2f8;
    *((unsigned int *)&g_103a1994) = sub_102fdcb0 ^ g_1038c29c ^ g_1038c2fc;
    *((unsigned int *)&g_103a1998) = sub_102f7650 ^ g_1038c2a0 ^ g_1038c290;
    *((unsigned int *)&g_103a199c) = sub_102f68f0 ^ g_1038c2a0 ^ g_1038c294;
    *((unsigned int *)&g_103a19a0) = sub_102ff5b0 ^ g_1038c2a0 ^ g_1038c298;
    *((unsigned int *)&g_103a19a4) = sub_102f6f30 ^ g_1038c2a0 ^ g_1038c29c;
    *((unsigned int *)&g_103a19a8) = sub_102f7130 ^ g_1038c2a0 ^ g_1038c2a4;
    *((unsigned int *)&g_103a19ac) = sub_102fffb0 ^ g_1038c2a0 ^ g_1038c2a4;
    *((unsigned int *)&g_103a19b0) = sub_102f6fd0 ^ g_1038c2a0 ^ g_1038c2a8;
    *((unsigned int *)&g_103a19b4) = sub_102f62a0 ^ g_1038c2a0 ^ g_1038c2ac;
    *((unsigned int *)&g_103a19b8) = sub_102f9420 ^ g_1038c2a0 ^ g_1038c2b0;
    *((unsigned int *)&g_103a19bc) = sub_102ff210 ^ g_1038c2a0 ^ g_1038c2b4;
    *((unsigned int *)&g_103a19c0) = sub_102fbb90 ^ g_1038c2a0 ^ g_1038c2b8;
    *((unsigned int *)&g_103a19c4) = sub_102f71e0 ^ g_1038c2a0 ^ g_1038c2bc;
    *((unsigned int *)&g_103a19c8) = sub_102f30b0 ^ g_1038c2a0 ^ g_1038c2c0;
    *((unsigned int *)&g_103a19cc) = sub_102f3400 ^ g_1038c2a0 ^ g_1038c2c4;
    *((unsigned int *)&g_103a19d0) = sub_102f75b0 ^ g_1038c2a0 ^ g_1038c2c8;
    *((unsigned int *)&g_103a19d4) = sub_102f9300 ^ g_1038c2a0 ^ g_1038c2cc;
    *((unsigned int *)&g_103a19d8) = sub_102fa2e0 ^ g_1038c2a0 ^ g_1038c2d0;
    *((unsigned int *)&g_103a19dc) = sub_102f9a30 ^ g_1038c2a0 ^ g_1038c2d4;
    *((unsigned int *)&g_103a19e0) = sub_102fee30 ^ g_1038c2a0 ^ g_1038c2d8;
    *((unsigned int *)&g_103a19e4) = sub_102f67a0 ^ g_1038c2a0 ^ g_1038c2dc;
    *((unsigned int *)&g_103a19e8) = sub_102fec90 ^ g_1038c2a0 ^ g_1038c2e0;
    *((unsigned int *)&g_103a19ec) = sub_102f78f0 ^ g_1038c2a0 ^ g_1038c2e4;
    *((unsigned int *)&g_103a19f0) = sub_102fe330 ^ g_1038c2a0 ^ g_1038c2e8;
    *((unsigned int *)&g_103a19f4) = sub_102f5f90 ^ g_1038c2a0 ^ g_1038c2ec;
    *((unsigned int *)&g_103a19f8) = sub_102f54a0 ^ g_1038c2a0 ^ g_1038c2f0;
    *((unsigned int *)&g_103a19fc) = sub_102fbfb0 ^ g_1038c2a0 ^ g_1038c2f4;
    *((unsigned int *)&g_103a1a00) = sub_102f4b60 ^ g_1038c2a0 ^ g_1038c2f8;
    *((unsigned int *)&g_103a1a04) = sub_102f6110 ^ g_1038c2a0 ^ g_1038c2fc;
    *((unsigned int *)&g_103a1a08) = sub_102f3990 ^ g_1038c2a4 ^ g_1038c290;
    *((unsigned int *)&g_103a1a0c) = sub_102f5ae0 ^ g_1038c2a4 ^ g_1038c294;
    *((unsigned int *)&g_103a1a10) = sub_102f6980 ^ g_1038c2a4 ^ g_1038c298;
    *((unsigned int *)&g_103a1a14) = sub_102f8f80 ^ g_1038c2a4 ^ g_1038c29c;
    *((unsigned int *)&g_103a1a18) = sub_102f9240 ^ g_1038c2a4 ^ g_1038c2a0;
    *((unsigned int *)&g_103a1a1c) = sub_102fcf80 ^ g_1038c2a4 ^ g_1038c2a8;
    *((unsigned int *)&g_103a1a20) = sub_102f50e0 ^ g_1038c2a4 ^ g_1038c2a8;
    *((unsigned int *)&g_103a1a24) = sub_102f8460 ^ g_1038c2a4 ^ g_1038c2ac;
    *((unsigned int *)&g_103a1a28) = sub_102fe990 ^ g_1038c2a4 ^ g_1038c2b0;
    *((unsigned int *)&g_103a1a2c) = sub_102fe290 ^ g_1038c2a4 ^ g_1038c2b4;
    *((unsigned int *)&g_103a1a30) = sub_102ff180 ^ g_1038c2a4 ^ g_1038c2b8;
    *((unsigned int *)&g_103a1a34) = sub_102fa9c0 ^ g_1038c2a4 ^ g_1038c2bc;
    *((unsigned int *)&g_103a1a38) = sub_102fab30 ^ g_1038c2a4 ^ g_1038c2c0;
    *((unsigned int *)&g_103a1a3c) = sub_102fb730 ^ g_1038c2a4 ^ g_1038c2c4;
    *((unsigned int *)&g_103a1a40) = sub_102fe470 ^ g_1038c2a4 ^ g_1038c2c8;
    *((unsigned int *)&g_103a1a44) = sub_102f4d90 ^ g_1038c2a4 ^ g_1038c2cc;
    *((unsigned int *)&g_103a1a48) = sub_102fa700 ^ g_1038c2a4 ^ g_1038c2d0;
    *((unsigned int *)&g_103a1a4c) = sub_102f9780 ^ g_1038c2a4 ^ g_1038c2d4;
    *((unsigned int *)&g_103a1a50) = sub_102f88d0 ^ g_1038c2a4 ^ g_1038c2d8;
    *((unsigned int *)&g_103a1a54) = sub_102fc0c0 ^ g_1038c2a4 ^ g_1038c2dc;
    *((unsigned int *)&g_103a1a58) = sub_102fa090 ^ g_1038c2a4 ^ g_1038c2e0;
    *((unsigned int *)&g_103a1a5c) = sub_102ffa30 ^ g_1038c2a4 ^ g_1038c2e4;
    *((unsigned int *)&g_103a1a60) = sub_102f64c0 ^ g_1038c2a4 ^ g_1038c2e8;
    *((unsigned int *)&g_103a1a64) = sub_102fcaa0 ^ g_1038c2a4 ^ g_1038c2ec;
    *((unsigned int *)&g_103a1a68) = sub_102fceb0 ^ g_1038c2a4 ^ g_1038c2f0;
    *((unsigned int *)&g_103a1a6c) = sub_102fe190 ^ g_1038c2a4 ^ g_1038c2f4;
    *((unsigned int *)&g_103a1a70) = sub_102fb690 ^ g_1038c2a4 ^ g_1038c2f8;
    *((unsigned int *)&g_103a1a74) = sub_102ffe80 ^ g_1038c2a4 ^ g_1038c2fc;
    *((unsigned int *)&g_103a1a78) = sub_102f8600 ^ g_1038c2a8 ^ g_1038c290;
    *((unsigned int *)&g_103a1a7c) = sub_102f91a0 ^ g_1038c2a8 ^ g_1038c294;
    *((unsigned int *)&g_103a1a80) = sub_102fdbf0 ^ g_1038c2a8 ^ g_1038c298;
    *((unsigned int *)&g_103a1a84) = sub_102f77e0 ^ g_1038c2a8 ^ g_1038c29c;
    *((unsigned int *)&g_103a1a88) = sub_102f3ad0 ^ g_1038c2a8 ^ g_1038c2a0;
    *((unsigned int *)&g_103a1a8c) = sub_102f3370 ^ g_1038c2a8 ^ g_1038c2a4;
    *((unsigned int *)&g_103a1a90) = sub_102fb460 ^ g_1038c2a8 ^ g_1038c2ac;
    *((unsigned int *)&g_103a1a94) = sub_102f5530 ^ g_1038c2a8 ^ g_1038c2ac;
    *((unsigned int *)&g_103a1a98) = sub_102f4960 ^ g_1038c2a8 ^ g_1038c2b0;
    *((unsigned int *)&g_103a1a9c) = sub_102f3020 ^ g_1038c2a8 ^ g_1038c2b4;
    *((unsigned int *)&g_103a1aa0) = sub_102f83a0 ^ g_1038c2a8 ^ g_1038c2b8;
    *((unsigned int *)&g_103a1aa4) = sub_102ffcb0 ^ g_1038c2a8 ^ g_1038c2bc;
    *((unsigned int *)&g_103a1aa8) = sub_102fb980 ^ g_1038c2a8 ^ g_1038c2c0;
    *((unsigned int *)&g_103a1aac) = sub_102faa80 ^ g_1038c2a8 ^ g_1038c2c4;
    *((unsigned int *)&g_103a1ab0) = sub_102fc7c0 ^ g_1038c2a8 ^ g_1038c2c8;
    *((unsigned int *)&g_103a1ab4) = sub_10300140 ^ g_1038c2a8 ^ g_1038c2cc;
    *((unsigned int *)&g_103a1ab8) = sub_102fd270 ^ g_1038c2a8 ^ g_1038c2d0;
    *((unsigned int *)&g_103a1abc) = sub_102f4c40 ^ g_1038c2a8 ^ g_1038c2d4;
    *((unsigned int *)&g_103a1ac0) = sub_102f5bc0 ^ g_1038c2a8 ^ g_1038c2d8;
    *((unsigned int *)&g_103a1ac4) = sub_102f3e60 ^ g_1038c2a8 ^ g_1038c2dc;
    *((unsigned int *)&g_103a1ac8) = sub_102fcce0 ^ g_1038c2a8 ^ g_1038c2e0;
    *((unsigned int *)&g_103a1acc) = sub_102f4a40 ^ g_1038c2a8 ^ g_1038c2e4;
    *((unsigned int *)&g_103a1ad0) = sub_102f8820 ^ g_1038c2a8 ^ g_1038c2e8;
    *((unsigned int *)&g_103a1ad4) = sub_102fc880 ^ g_1038c2a8 ^ g_1038c2ec;
    *((unsigned int *)&g_103a1ad8) = sub_102f3b80 ^ g_1038c2a8 ^ g_1038c2f0;
    *((unsigned int *)&g_103a1adc) = sub_102f6350 ^ g_1038c2a8 ^ g_1038c2f4;
    *((unsigned int *)&g_103a1ae0) = sub_102fe3d0 ^ g_1038c2a8 ^ g_1038c2f8;
    *((unsigned int *)&g_103a1ae4) = sub_102f5020 ^ g_1038c2a8 ^ g_1038c2fc;
    *((unsigned int *)&g_103a1ae8) = sub_102f5c70 ^ g_1038c2ac ^ g_1038c290;
    *((unsigned int *)&g_103a1aec) = sub_102f72b0 ^ g_1038c2ac ^ g_1038c294;
    *((unsigned int *)&g_103a1af0) = sub_102fa8a0 ^ g_1038c2ac ^ g_1038c298;
    *((unsigned int *)&g_103a1af4) = sub_102fd6c0 ^ g_1038c2ac ^ g_1038c29c;
    *((unsigned int *)&g_103a1af8) = sub_102ff650 ^ g_1038c2ac ^ g_1038c2a0;
    *((unsigned int *)&g_103a1afc) = sub_102f8560 ^ g_1038c2ac ^ g_1038c2a4;
    *((unsigned int *)&g_103a1b00) = sub_102f5f00 ^ g_1038c2ac ^ g_1038c2a8;
    *((unsigned int *)&g_103a1b04) = sub_102f6de0 ^ g_1038c2ac ^ g_1038c2b0;
    *((unsigned int *)&g_103a1b08) = sub_102fd3c0 ^ g_1038c2ac ^ g_1038c2b0;
    *((unsigned int *)&g_103a1b0c) = sub_102fad70 ^ g_1038c2ac ^ g_1038c2b4;
    *((unsigned int *)&g_103a1b10) = sub_102fb240 ^ g_1038c2ac ^ g_1038c2b8;
    *((unsigned int *)&g_103a1b14) = sub_102f7a80 ^ g_1038c2ac ^ g_1038c2bc;
    *((unsigned int *)&g_103a1b18) = sub_102fd320 ^ g_1038c2ac ^ g_1038c2c0;
    *((unsigned int *)&g_103a1b1c) = sub_102fac10 ^ g_1038c2ac ^ g_1038c2c4;
    *((unsigned int *)&g_103a1b20) = sub_102ffbf0 ^ g_1038c2ac ^ g_1038c2c8;
    *((unsigned int *)&g_103a1b24) = sub_102fe550 ^ g_1038c2ac ^ g_1038c2cc;
    *((unsigned int *)&g_103a1b28) = sub_102fc4b0 ^ g_1038c2ac ^ g_1038c2d0;
    *((unsigned int *)&g_103a1b2c) = sub_102f4cd0 ^ g_1038c2ac ^ g_1038c2d4;
    *((unsigned int *)&g_103a1b30) = sub_102fb530 ^ g_1038c2ac ^ g_1038c2d8;
    *((unsigned int *)&g_103a1b34) = sub_102fc210 ^ g_1038c2ac ^ g_1038c2dc;
    *((unsigned int *)&g_103a1b38) = sub_102f9cc0 ^ g_1038c2ac ^ g_1038c2e0;
    *((unsigned int *)&g_103a1b3c) = sub_102fb8e0 ^ g_1038c2ac ^ g_1038c2e4;
    *((unsigned int *)&g_103a1b40) = sub_102fe110 ^ g_1038c2ac ^ g_1038c2e8;
    *((unsigned int *)&g_103a1b44) = sub_102f9ae0 ^ g_1038c2ac ^ g_1038c2ec;
    *((unsigned int *)&g_103a1b48) = sub_102fe790 ^ g_1038c2ac ^ g_1038c2f0;
    *((unsigned int *)&g_103a1b4c) = sub_102fc710 ^ g_1038c2ac ^ g_1038c2f4;
    *((unsigned int *)&g_103a1b50) = sub_102f9eb0 ^ g_1038c2ac ^ g_1038c2f8;
    *((unsigned int *)&g_103a1b54) = sub_102f3d00 ^ g_1038c2ac ^ g_1038c2fc;
    *((unsigned int *)&g_103a1b58) = sub_102f89b0 ^ g_1038c2b0 ^ g_1038c290;
    *((unsigned int *)&g_103a1b5c) = sub_103001f0 ^ g_1038c2b0 ^ g_1038c294;
    *((unsigned int *)&g_103a1b60) = sub_102f36d0 ^ g_1038c2b0 ^ g_1038c298;
    *((unsigned int *)&g_103a1b64) = sub_102fca00 ^ g_1038c2b0 ^ g_1038c29c;
    *((unsigned int *)&g_103a1b68) = sub_102fc660 ^ g_1038c2b0 ^ g_1038c2a0;
    *((unsigned int *)&g_103a1b6c) = sub_102fbca0 ^ g_1038c2b0 ^ g_1038c2a4;
    *((unsigned int *)&g_103a1b70) = sub_102f7500 ^ g_1038c2b0 ^ g_1038c2a8;
    *((unsigned int *)&g_103a1b74) = sub_102fa460 ^ g_1038c2b0 ^ g_1038c2ac;
    *((unsigned int *)&g_103a1b78) = sub_102f47b0 ^ g_1038c2b0 ^ g_1038c2b4;
    *((unsigned int *)&g_103a1b7c) = sub_102fdf50 ^ g_1038c2b0 ^ g_1038c2b4;
    *((unsigned int *)&g_103a1b80) = sub_102f56a0 ^ g_1038c2b0 ^ g_1038c2b8;
    *((unsigned int *)&g_103a1b84) = sub_102ffb40 ^ g_1038c2b0 ^ g_1038c2bc;
    *((unsigned int *)&g_103a1b88) = sub_102ff7f0 ^ g_1038c2b0 ^ g_1038c2c0;
    *((unsigned int *)&g_103a1b8c) = sub_102ffda0 ^ g_1038c2b0 ^ g_1038c2c4;
    *((unsigned int *)&g_103a1b90) = sub_102f95f0 ^ g_1038c2b0 ^ g_1038c2c8;
    *((unsigned int *)&g_103a1b94) = sub_102f9910 ^ g_1038c2b0 ^ g_1038c2cc;
    *((unsigned int *)&g_103a1b98) = sub_102f5810 ^ g_1038c2b0 ^ g_1038c2d0;
    *((unsigned int *)&g_103a1b9c) = sub_102f3550 ^ g_1038c2b0 ^ g_1038c2d4;
    *((unsigned int *)&g_103a1ba0) = sub_102f9820 ^ g_1038c2b0 ^ g_1038c2d8;
    *((unsigned int *)&g_103a1ba4) = sub_102fa550 ^ g_1038c2b0 ^ g_1038c2dc;
    *((unsigned int *)&g_103a1ba8) = sub_102f66f0 ^ g_1038c2b0 ^ g_1038c2e0;
    *((unsigned int *)&g_103a1bac) = sub_102fa7f0 ^ g_1038c2b0 ^ g_1038c2e4;
    *((unsigned int *)&g_103a1bb0) = sub_102f8210 ^ g_1038c2b0 ^ g_1038c2e8;
    *((unsigned int *)&g_103a1bb4) = sub_102ff0b0 ^ g_1038c2b0 ^ g_1038c2ec;
    *((unsigned int *)&g_103a1bb8) = sub_102fb0b0 ^ g_1038c2b0 ^ g_1038c2f0;
    g_103a1bbc = sub_102fed40 ^ g_1038c2b0 ^ g_1038c2f4;
    *((unsigned int *)&g_103a1bc0) = sub_102f7fa0 ^ g_1038c2b0 ^ g_1038c2f8;
    *((unsigned int *)&g_103a1bc4) = sub_102ff880 ^ g_1038c2b0 ^ g_1038c2fc;
    return g_103a1bbc;
}
```

## `sub_103731f0` `0x103731f0`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a1be0;

int sub_103731f0(void)
{
    g_103a1be0 = sub_10368c80();
    return g_103a1be0;
}
```

## `sub_10373200` `0x10373200`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a1be4;

int sub_10373200(void)
{
    g_103a1be4 = sub_10368cf0();
    return g_103a1be4;
}
```

## `sub_10373210` `0x10373210`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a2230;

int sub_10373210(void)
{
    g_103a2230 = sub_10368cf0();
    return g_103a2230;
}
```

## `sub_10373220` `0x10373220`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a1bd8;

int sub_10373220(void)
{
    g_103a1bd8 = sub_10368cf0();
    return g_103a1bd8;
}
```

## `sub_10373230` `0x10373230`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a1bdc;

int sub_10373230(void)
{
    g_103a1bdc = sub_10368c80();
    return g_103a1bdc;
}
```

## `sub_10373240` `0x10373240`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a1bd1;

int sub_10373240(void)
{
    return sub_1031a280(&g_103a1bd1);
}
```

## `sub_10373250` `0x10373250`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a1bd5;

int sub_10373250(void)
{
    return sub_1031a280(&g_103a1bd5);
}
```

## `sub_10373260` `0x10373260`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a1bd7;

int sub_10373260(void)
{
    return sub_1031a280(&g_103a1bd7);
}
```

## `sub_10373270` `0x10373270`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a1bd4;

int sub_10373270(void)
{
    return sub_1031a280(&g_103a1bd4);
}
```

## `sub_10373280` `0x10373280`

_15 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a1bd2;

int sub_10373280(void)
{
    return sub_1031a280(&g_103a1bd2);
}
```

