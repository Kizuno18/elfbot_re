# elfbot.dll decompiled — jiru 0x102f0f30..0x102f32dd

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_102f0f30` `0x102f0f30`

_192 bytes. (leaf/helper — see body)_

```c
int sub_102f0f30(int a0)
{
    char v0;  // [bp+0x0]

    a0 = sub_102f2bf0(a0, -0x8, &v0);
    a0 = sub_102f2ca0(a0, 5, 10);
    a0 = sub_102f2d00(a0, 23, 6);
    a0 = sub_102f2c20(a0, 22, 1, -5);
    a0 ^= 420175507;
    a0 = sub_102f2bf0(a0, -12);
    a0 = sub_102f2d00(a0, 15, 13);
    a0 ^= 3007219773;
    a0 = sub_102f2d00(a0, 8, 19);
    a0 = sub_102f2bf0(a0, -24);
    a0 ^= 211791105;
    return a0;
}
```

## `sub_102f0ff0` `0x102f0ff0`

_297 bytes. (leaf/helper — see body)_

```c
int sub_102f0ff0(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 3663736368;
    a0 = sub_102f2ca0(a0, 3, 21, &v0);
    a0 = sub_102f2c20(a0, 31, 0, 2);
    a0 = sub_102f2bf0(a0, 2);
    a0 = sub_102f2c20(a0, 8, 0x11, 2);
    a0 ^= 375105376;
    a0 = sub_102f2c20(a0, 26, 4, 16);
    a0 = sub_102f2ca0(a0, 2, 9);
    a0 = sub_102f2d00(a0, 0x11, 11);
    a0 = sub_102f2bf0(a0, 24);
    a0 ^= 244958609;
    a0 = sub_102f2bf0(a0, 21);
    a0 = sub_102f2c20(a0, 19, 5, 0x11);
    a0 ^= 2217901859;
    a0 = sub_102f2d00(a0, 3, 6);
    a0 = sub_102f2ca0(a0, 3, 22);
    a0 ^= 919234438;
    return a0;
}
```

## `sub_102f1120` `0x102f1120`

_295 bytes. (leaf/helper — see body)_

```c
int sub_102f1120(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 919234438;
    a0 = sub_102f2ca0(a0, 3, 22, &v0);
    a0 = sub_102f2d00(a0, 3, 6);
    a0 ^= 2217901859;
    a0 = sub_102f2c20(a0, 19, 5, -17);
    a0 = sub_102f2bf0(a0, -21);
    a0 ^= 244958609;
    a0 = sub_102f2bf0(a0, -24);
    a0 = sub_102f2d00(a0, 0x11, 11);
    a0 = sub_102f2ca0(a0, 2, 9);
    a0 = sub_102f2c20(a0, 26, 4, -0x10);
    a0 ^= 375105376;
    a0 = sub_102f2c20(a0, 8, 0x11, -2);
    a0 = sub_102f2bf0(a0, -2);
    a0 = sub_102f2c20(a0, 31, 0, -2);
    a0 = sub_102f2ca0(a0, 3, 21);
    a0 ^= 3663736368;
    return a0;
}
```

## `sub_102f1250` `0x102f1250`

_318 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102f1250(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 1328578488;
    a0 = sub_102f2d00(a0, 18, 11, &v0);
    a0 = sub_102f2ca0(a0, 2, 15);
    a0 = sub_102f2d00(a0, 20, 10);
    a0 ^= 3790145222;
    a0 = sub_102f2c20(a0, 24, 5, 3);
    a0 = sub_102f2ca0(a0, 8, 23);
    a0 = sub_102f2bf0(a0, 0x11);
    a0 = sub_102f2d00(a0, 31, 0);
    a0 = sub_102f2ca0(a0, 3, 13);
    a0 = sub_102f2d00(a0, 3, 6);
    a0 = sub_102f2c20(a0, 10, 4, 9);
    a0 = sub_102f2d00(a0, 14, 4);
    a0 ^= 1701183368;
    a0 = sub_102f2bf0(a0, 24);
    a0 ^= 2630557958;
    a0 = sub_102f2bf0(a0, 11);
    a0 = sub_102f2ca0(a0, 4, 15);
    return a0;
}
```

## `sub_102f1390` `0x102f1390`

_320 bytes. (leaf/helper — see body)_

```c
int sub_102f1390(int a0)
{
    char v0;  // [bp+0x0]

    a0 = sub_102f2ca0(a0, 4, 15, &v0);
    a0 = sub_102f2bf0(a0, -11);
    a0 ^= 2630557958;
    a0 = sub_102f2bf0(a0, -24);
    a0 ^= 1701183368;
    a0 = sub_102f2d00(a0, 14, 4);
    a0 = sub_102f2c20(a0, 10, 4, -9);
    a0 = sub_102f2d00(a0, 3, 6);
    a0 = sub_102f2ca0(a0, 3, 13);
    a0 = sub_102f2d00(a0, 31, 0);
    a0 = sub_102f2bf0(a0, -17);
    a0 = sub_102f2ca0(a0, 8, 23);
    a0 = sub_102f2c20(a0, 24, 5, -3);
    a0 ^= 3790145222;
    a0 = sub_102f2d00(a0, 20, 10);
    a0 = sub_102f2ca0(a0, 2, 15);
    a0 = sub_102f2d00(a0, 18, 11);
    a0 ^= 1328578488;
    return a0;
}
```

## `sub_102f14d0` `0x102f14d0`

_410 bytes. (leaf/helper — see body)_

```c
int sub_102f14d0(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 3988409900;
    a0 = sub_102f2bf0(a0, 26, &v0);
    a0 ^= 715683355;
    a0 = sub_102f2c20(a0, 5, 19, 2);
    a0 ^= 2037879517;
    a0 = sub_102f2d00(a0, 12, 16);
    a0 = sub_102f2ca0(a0, 1, 22);
    a0 = sub_102f2c20(a0, 12, 6, 9);
    a0 = sub_102f2ca0(a0, 5, 9);
    a0 = sub_102f2c20(a0, 30, 0, 23);
    a0 = sub_102f2bf0(a0, 23);
    a0 ^= 3447280582;
    a0 = sub_102f2bf0(a0, 6);
    a0 = sub_102f2c20(a0, 0x11, 1, 15);
    a0 ^= 988664399;
    a0 = sub_102f2d00(a0, 20, 3);
    a0 = sub_102f2c20(a0, 4, 22, 2);
    a0 = sub_102f2d00(a0, 31, 0);
    a0 ^= 0xc93d3f00;
    a0 = sub_102f2bf0(a0, 26);
    a0 ^= 2507744040;
    a0 = sub_102f2c20(a0, 18, 7, 15);
    a0 = sub_102f2d00(a0, 4, 8);
    a0 ^= 1571686584;
    return a0;
}
```

## `sub_102f1670` `0x102f1670`

_407 bytes. (leaf/helper — see body)_

```c
int sub_102f1670(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 1571686584;
    a0 = sub_102f2d00(a0, 4, 8, &v0);
    a0 = sub_102f2c20(a0, 18, 7, -15);
    a0 ^= 2507744040;
    a0 = sub_102f2bf0(a0, -26);
    a0 ^= 0xc93d3f00;
    a0 = sub_102f2d00(a0, 31, 0);
    a0 = sub_102f2c20(a0, 4, 22, -2);
    a0 = sub_102f2d00(a0, 20, 3);
    a0 ^= 988664399;
    a0 = sub_102f2c20(a0, 0x11, 1, -15);
    a0 = sub_102f2bf0(a0, -6);
    a0 ^= 3447280582;
    a0 = sub_102f2bf0(a0, -23);
    a0 = sub_102f2c20(a0, 30, 0, -23);
    a0 = sub_102f2ca0(a0, 5, 9);
    a0 = sub_102f2c20(a0, 12, 6, -9);
    a0 = sub_102f2ca0(a0, 1, 22);
    a0 = sub_102f2d00(a0, 12, 16);
    a0 ^= 2037879517;
    a0 = sub_102f2c20(a0, 5, 19, -2);
    a0 ^= 715683355;
    a0 = sub_102f2bf0(a0, -26);
    a0 ^= 3988409900;
    return a0;
}
```

## `sub_102f1810` `0x102f1810`

_255 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102f1810(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 416886808;
    a0 = sub_102f2ca0(a0, 1, 0x11, &v0);
    a0 = sub_102f2d00(a0, 11, 10);
    a0 = sub_102f2ca0(a0, 3, 12);
    a0 = sub_102f2d00(a0, 3, 27);
    a0 = sub_102f2c20(a0, 0x11, 10, 16);
    a0 = sub_102f2ca0(a0, 6, 21);
    a0 = sub_102f2bf0(a0, 0x11);
    a0 = sub_102f2d00(a0, 4, 20);
    a0 = sub_102f2c20(a0, 12, 13, 6);
    a0 ^= 1564981388;
    a0 = sub_102f2d00(a0, 27, 2);
    a0 ^= 1363772270;
    a0 = sub_102f2c20(a0, 18, 6, 6);
    return a0;
}
```

## `sub_102f1910` `0x102f1910`

_256 bytes. (leaf/helper — see body)_

```c
int sub_102f1910(int a0)
{
    char v0;  // [bp+0x0]

    a0 = sub_102f2c20(a0, 18, 6, -6, &v0);
    a0 ^= 1363772270;
    a0 = sub_102f2d00(a0, 27, 2);
    a0 ^= 1564981388;
    a0 = sub_102f2c20(a0, 12, 13, -6);
    a0 = sub_102f2d00(a0, 4, 20);
    a0 = sub_102f2bf0(a0, -17);
    a0 = sub_102f2ca0(a0, 6, 21);
    a0 = sub_102f2c20(a0, 0x11, 10, -0x10);
    a0 = sub_102f2d00(a0, 3, 27);
    a0 = sub_102f2ca0(a0, 3, 12);
    a0 = sub_102f2d00(a0, 11, 10);
    a0 = sub_102f2ca0(a0, 1, 0x11);
    a0 ^= 416886808;
    return a0;
}
```

## `sub_102f1a10` `0x102f1a10`

_375 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102f1a10(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 3364042956;
    a0 = sub_102f2c20(a0, 0x11, 2, 2, &v0);
    a0 ^= 4207926464;
    a0 = sub_102f2d00(a0, 6, 9);
    a0 = sub_102f2ca0(a0, 8, 12);
    a0 ^= 1862376443;
    a0 = sub_102f2bf0(a0, 23);
    a0 ^= 1517688478;
    a0 = sub_102f2bf0(a0, 10);
    a0 = sub_102f2c20(a0, 10, 20, 3);
    a0 ^= 2014847042;
    a0 = sub_102f2bf0(a0, 14);
    a0 ^= 3408175289;
    a0 = sub_102f2c20(a0, 22, 3, 9);
    a0 = sub_102f2d00(a0, 11, 4);
    a0 = sub_102f2ca0(a0, 2, 15);
    a0 ^= 1841504376;
    a0 = sub_102f2bf0(a0, 24);
    a0 ^= 2386245147;
    a0 = sub_102f2d00(a0, 15, 6);
    a0 ^= 220376437;
    a0 = sub_102f2d00(a0, 12, 11);
    a0 = sub_102f2bf0(a0, 2);
    return a0;
}
```

## `sub_102f1b90` `0x102f1b90`

_375 bytes. (leaf/helper — see body)_

```c
int sub_102f1b90(int a0)
{
    char v0;  // [bp+0x0]

    a0 = sub_102f2bf0(a0, -2, &v0);
    a0 = sub_102f2d00(a0, 12, 11);
    a0 ^= 220376437;
    a0 = sub_102f2d00(a0, 15, 6);
    a0 ^= 2386245147;
    a0 = sub_102f2bf0(a0, -24);
    a0 ^= 1841504376;
    a0 = sub_102f2ca0(a0, 2, 15);
    a0 = sub_102f2d00(a0, 11, 4);
    a0 = sub_102f2c20(a0, 22, 3, -9);
    a0 ^= 3408175289;
    a0 = sub_102f2bf0(a0, -14);
    a0 ^= 2014847042;
    a0 = sub_102f2c20(a0, 10, 20, -3);
    a0 = sub_102f2bf0(a0, -10);
    a0 ^= 1517688478;
    a0 = sub_102f2bf0(a0, -23);
    a0 ^= 1862376443;
    a0 = sub_102f2ca0(a0, 8, 12);
    a0 = sub_102f2d00(a0, 6, 9);
    a0 ^= 4207926464;
    a0 = sub_102f2c20(a0, 0x11, 2, -2);
    a0 ^= 3364042956;
    return a0;
}
```

## `sub_102f1d10` `0x102f1d10`

_374 bytes. (leaf/helper — see body)_

```c
int sub_102f1d10(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 3675276393;
    a0 = sub_102f2c20(a0, 3, 26, 2, &v0);
    a0 = sub_102f2bf0(a0, 10);
    a0 = sub_102f2d00(a0, 2, 16);
    a0 ^= 182117759;
    a0 = sub_102f2ca0(a0, 1, 11);
    a0 = sub_102f2c20(a0, 30, 0, 13);
    a0 = sub_102f2bf0(a0, 15);
    a0 = sub_102f2d00(a0, 26, 3);
    a0 = sub_102f2bf0(a0, 9);
    a0 = sub_102f2ca0(a0, 3, 0x11);
    a0 = sub_102f2d00(a0, 31, 0);
    a0 ^= 1483982167;
    a0 = sub_102f2c20(a0, 12, 10, 11);
    a0 ^= 1220937039;
    a0 = sub_102f2ca0(a0, 5, 15);
    a0 = sub_102f2c20(a0, 12, 8, 5);
    a0 = sub_102f2ca0(a0, 7, 23);
    a0 = sub_102f2c20(a0, 31, 0, 22);
    a0 = sub_102f2ca0(a0, 5, 13);
    a0 ^= 1502793180;
    return a0;
}
```

## `sub_102f1e90` `0x102f1e90`

_374 bytes. (leaf/helper — see body)_

```c
int sub_102f1e90(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 1502793180;
    a0 = sub_102f2ca0(a0, 5, 13, &v0);
    a0 = sub_102f2c20(a0, 31, 0, -22);
    a0 = sub_102f2ca0(a0, 7, 23);
    a0 = sub_102f2c20(a0, 12, 8, -5);
    a0 = sub_102f2ca0(a0, 5, 15);
    a0 ^= 1220937039;
    a0 = sub_102f2c20(a0, 12, 10, -11);
    a0 ^= 1483982167;
    a0 = sub_102f2d00(a0, 31, 0);
    a0 = sub_102f2ca0(a0, 3, 0x11);
    a0 = sub_102f2bf0(a0, -9);
    a0 = sub_102f2d00(a0, 26, 3);
    a0 = sub_102f2bf0(a0, -15);
    a0 = sub_102f2c20(a0, 30, 0, -13);
    a0 = sub_102f2ca0(a0, 1, 11);
    a0 ^= 182117759;
    a0 = sub_102f2d00(a0, 2, 16);
    a0 = sub_102f2bf0(a0, -10);
    a0 = sub_102f2c20(a0, 3, 26, -2);
    a0 ^= 3675276393;
    return a0;
}
```

## `sub_102f2010` `0x102f2010`

_351 bytes. (leaf/helper — see body)_

```c
int sub_102f2010(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 1715394988;
    a0 = sub_102f2ca0(a0, 1, 21, &v0);
    a0 ^= 1398360606;
    a0 = sub_102f2d00(a0, 4, 7);
    a0 = sub_102f2bf0(a0, 0x11);
    a0 = sub_102f2d00(a0, 7, 4);
    a0 = sub_102f2bf0(a0, 15);
    a0 = sub_102f2d00(a0, 6, 13);
    a0 ^= 384180624;
    a0 = sub_102f2d00(a0, 30, 1);
    a0 = sub_102f2c20(a0, 29, 1, 14);
    a0 = sub_102f2bf0(a0, 14);
    a0 = sub_102f2ca0(a0, 5, 0x11);
    a0 = sub_102f2bf0(a0, 11);
    a0 = sub_102f2c20(a0, 28, 2, 27);
    a0 = sub_102f2bf0(a0, 21);
    a0 = sub_102f2d00(a0, 30, 0);
    a0 = sub_102f2bf0(a0, 28);
    a0 = sub_102f2d00(a0, 28, 3);
    a0 ^= 2120068441;
    return a0;
}
```

## `sub_102f2170` `0x102f2170`

_351 bytes. (leaf/helper — see body)_

```c
int sub_102f2170(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 2120068441;
    a0 = sub_102f2d00(a0, 28, 3, &v0);
    a0 = sub_102f2bf0(a0, -28);
    a0 = sub_102f2d00(a0, 30, 0);
    a0 = sub_102f2bf0(a0, -21);
    a0 = sub_102f2c20(a0, 28, 2, -27);
    a0 = sub_102f2bf0(a0, -11);
    a0 = sub_102f2ca0(a0, 5, 0x11);
    a0 = sub_102f2bf0(a0, -14);
    a0 = sub_102f2c20(a0, 29, 1, -14);
    a0 = sub_102f2d00(a0, 30, 1);
    a0 ^= 384180624;
    a0 = sub_102f2d00(a0, 6, 13);
    a0 = sub_102f2bf0(a0, -15);
    a0 = sub_102f2d00(a0, 7, 4);
    a0 = sub_102f2bf0(a0, -17);
    a0 = sub_102f2d00(a0, 4, 7);
    a0 ^= 1398360606;
    a0 = sub_102f2ca0(a0, 1, 21);
    a0 ^= 1715394988;
    return a0;
}
```

## `sub_102f22d0` `0x102f22d0`

_322 bytes. (leaf/helper — see body)_

```c
int sub_102f22d0(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 1586298043;
    a0 = sub_102f2bf0(a0, 29, &v0);
    a0 ^= 235533603;
    a0 = sub_102f2c20(a0, 22, 7, 20);
    a0 = sub_102f2bf0(a0, 7);
    a0 = sub_102f2d00(a0, 7, 3);
    a0 ^= 2268678568;
    a0 = sub_102f2d00(a0, 4, 19);
    a0 = sub_102f2bf0(a0, 7);
    a0 = sub_102f2d00(a0, 26, 0);
    a0 = sub_102f2ca0(a0, 4, 11);
    a0 = sub_102f2bf0(a0, 23);
    a0 = sub_102f2d00(a0, 26, 3);
    a0 = sub_102f2ca0(a0, 3, 13);
    a0 = sub_102f2d00(a0, 28, 2);
    a0 ^= 1599867680;
    a0 = sub_102f2bf0(a0, 28);
    a0 = sub_102f2d00(a0, 7, 2);
    a0 ^= 856037315;
    return a0;
}
```

## `sub_102f2420` `0x102f2420`

_322 bytes. (leaf/helper — see body)_

```c
int sub_102f2420(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 856037315;
    a0 = sub_102f2d00(a0, 7, 2, &v0);
    a0 = sub_102f2bf0(a0, -28);
    a0 ^= 1599867680;
    a0 = sub_102f2d00(a0, 28, 2);
    a0 = sub_102f2ca0(a0, 3, 13);
    a0 = sub_102f2d00(a0, 26, 3);
    a0 = sub_102f2bf0(a0, -23);
    a0 = sub_102f2ca0(a0, 4, 11);
    a0 = sub_102f2d00(a0, 26, 0);
    a0 = sub_102f2bf0(a0, -7);
    a0 = sub_102f2d00(a0, 4, 19);
    a0 ^= 2268678568;
    a0 = sub_102f2d00(a0, 7, 3);
    a0 = sub_102f2bf0(a0, -7);
    a0 = sub_102f2c20(a0, 22, 7, -20);
    a0 ^= 235533603;
    a0 = sub_102f2bf0(a0, -29);
    a0 ^= 1586298043;
    return a0;
}
```

## `sub_102f2570` `0x102f2570`

_278 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102f2570(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 919214333;
    a0 = sub_102f2bf0(a0, 24, &v0);
    a0 ^= 674609931;
    a0 = sub_102f2c20(a0, 9, 4, 7);
    a0 = sub_102f2bf0(a0, 9);
    a0 = sub_102f2ca0(a0, 3, 20);
    a0 = sub_102f2d00(a0, 31, 0);
    a0 = sub_102f2c20(a0, 7, 7, 5);
    a0 = sub_102f2bf0(a0, 25);
    a0 ^= 206582254;
    a0 = sub_102f2bf0(a0, 5);
    a0 ^= 1452272139;
    a0 = sub_102f2bf0(a0, 13);
    a0 = sub_102f2ca0(a0, 4, 21);
    a0 = sub_102f2c20(a0, 27, 3, 21);
    a0 = sub_102f2d00(a0, 20, 2);
    return a0;
}
```

## `sub_102f2690` `0x102f2690`

_278 bytes. (leaf/helper — see body)_

```c
int sub_102f2690(int a0)
{
    char v0;  // [bp+0x0]

    a0 = sub_102f2d00(a0, 20, 2, &v0);
    a0 = sub_102f2c20(a0, 27, 3, -21);
    a0 = sub_102f2ca0(a0, 4, 21);
    a0 = sub_102f2bf0(a0, -13);
    a0 ^= 1452272139;
    a0 = sub_102f2bf0(a0, -5);
    a0 ^= 206582254;
    a0 = sub_102f2bf0(a0, -25);
    a0 = sub_102f2c20(a0, 7, 7, -5);
    a0 = sub_102f2d00(a0, 31, 0);
    a0 = sub_102f2ca0(a0, 3, 20);
    a0 = sub_102f2bf0(a0, -9);
    a0 = sub_102f2c20(a0, 9, 4, -7);
    a0 ^= 674609931;
    a0 = sub_102f2bf0(a0, -24);
    a0 ^= 919214333;
    return a0;
}
```

## `sub_102f27b0` `0x102f27b0`

_396 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102f27b0(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 3719120726;
    a0 = sub_102f2c20(a0, 9, 11, 4, &v0);
    a0 = sub_102f2ca0(a0, 5, 11);
    a0 = sub_102f2d00(a0, 6, 20);
    a0 = sub_102f2ca0(a0, 7, 23);
    a0 = sub_102f2bf0(a0, 31);
    a0 = sub_102f2ca0(a0, 3, 13);
    a0 = sub_102f2bf0(a0, 31);
    a0 = sub_102f2d00(a0, 26, 3);
    a0 = sub_102f2c20(a0, 22, 1, 10);
    a0 = sub_102f2d00(a0, 14, 10);
    a0 ^= 2417055656;
    a0 = sub_102f2bf0(a0, 8);
    a0 = sub_102f2c20(a0, 6, 12, 3);
    a0 ^= 4230292074;
    a0 = sub_102f2bf0(a0, 9);
    a0 = sub_102f2d00(a0, 30, 1);
    a0 = sub_102f2bf0(a0, 4);
    a0 = sub_102f2d00(a0, 31, 0);
    a0 = sub_102f2bf0(a0, 4);
    a0 = sub_102f2d00(a0, 25, 5);
    a0 = sub_102f2bf0(a0, 24);
    return a0;
}
```

## `sub_102f2940` `0x102f2940`

_396 bytes. (leaf/helper — see body)_

```c
int sub_102f2940(int a0)
{
    char v0;  // [bp+0x0]

    a0 = sub_102f2bf0(a0, -24, &v0);
    a0 = sub_102f2d00(a0, 25, 5);
    a0 = sub_102f2bf0(a0, -0x4);
    a0 = sub_102f2d00(a0, 31, 0);
    a0 = sub_102f2bf0(a0, -0x4);
    a0 = sub_102f2d00(a0, 30, 1);
    a0 = sub_102f2bf0(a0, -9);
    a0 ^= 4230292074;
    a0 = sub_102f2c20(a0, 6, 12, -3);
    a0 = sub_102f2bf0(a0, -0x8);
    a0 ^= 2417055656;
    a0 = sub_102f2d00(a0, 14, 10);
    a0 = sub_102f2c20(a0, 22, 1, -10);
    a0 = sub_102f2d00(a0, 26, 3);
    a0 = sub_102f2bf0(a0, -31);
    a0 = sub_102f2ca0(a0, 3, 13);
    a0 = sub_102f2bf0(a0, -31);
    a0 = sub_102f2ca0(a0, 7, 23);
    a0 = sub_102f2d00(a0, 6, 20);
    a0 = sub_102f2ca0(a0, 5, 11);
    a0 = sub_102f2c20(a0, 9, 11, -0x4);
    a0 ^= 3719120726;
    return a0;
}
```

## `sub_102f2ad0` `0x102f2ad0`

_140 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102f2ad0(unsigned int a0)
{
    char v0;  // [bp+0x0]

    a0 ^= 809630357;
    a0 = sub_102f2bf0(a0, 0x11, &v0);
    a0 = sub_102f2d00(a0, 19, 11);
    a0 ^= 2260408473;
    a0 = sub_102f2bf0(a0, 15);
    a0 = sub_102f2d00(a0, 3, 1);
    a0 = sub_102f2c20(a0, 7, 11, 4);
    a0 = sub_102f2bf0(a0, 22);
    return a0;
}
```

## `sub_102f2b60` `0x102f2b60`

_142 bytes. (leaf/helper — see body)_

```c
int sub_102f2b60(int a0)
{
    char v0;  // [bp+0x0]

    a0 = sub_102f2bf0(a0, -22, &v0);
    a0 = sub_102f2c20(a0, 7, 11, -0x4);
    a0 = sub_102f2d00(a0, 3, 1);
    a0 = sub_102f2bf0(a0, -15);
    a0 ^= 2260408473;
    a0 = sub_102f2d00(a0, 19, 11);
    a0 = sub_102f2bf0(a0, -17);
    a0 ^= 809630357;
    return a0;
}
```

## `sub_102f2bf0` `0x102f2bf0`

_43 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102f2bf0(unsigned int a0, int a1)
{
    if (a1 < 0)
        a1 += 32;
    return a0 >> ((char)a1 & 31) | a0 << ((char)(32 - a1) & 31);
}
```

## `sub_102f2c20` `0x102f2c20`

_115 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102f2c20(unsigned int a0, unsigned int a1, char a2, int a3)
{
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    if (a3 < 0)
        a3 += a1;
    v1 = (1 << ((char)a1 & 31)) - 1;
    v0 = a0 >> (a2 & 31) & v1;
    v0 = (v0 >> ((char)a3 & 31) | v0 << ((char)(a1 - a3) & 31)) & v1;
    a0 &= ~(v1 << (a2 & 31));
    a0 |= v0 << (a2 & 31);
    return a0;
}
```

## `sub_102f2ca0` `0x102f2ca0`

_94 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102f2ca0(unsigned int a0, char a1, char a2)
{
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    unsigned int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]

    v0 = (1 << (a1 & 31)) - 1;
    v2 = v0 << (a2 & 31);
    v3 = a0 & v0;
    v1 = (a0 & v2) >> (a2 & 31);
    a0 &= ~(v0 | v2);
    a0 |= v3 << (a2 & 31) | v1;
    return a0;
}
```

## `sub_102f2d00` `0x102f2d00`

_139 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102f2d00(unsigned int a0, int a1, char a2)
{
    int i;  // [bp-0x18]
    unsigned int v1;  // [bp-0x14]
    unsigned int v2;  // [bp-0x10]
    unsigned int v3;  // [bp-0xc]
    unsigned int v4;  // [bp-0x8]

    v2 = (1 << ((char)a1 & 31)) - 1 << (a2 & 31);
    v1 = ~(v2) & a0;
    v4 = 1 << (a2 & 31);
    v3 = 1 << ((char)(a2 + a1 - 1) & 31);
    for (i = 0; i < a1; i += 1)
    {
        if ((a0 & v4))
            v1 |= v3;
        v4 *= 2;
        v3 >>= 1;
    }
    return v1;
}
```

## `sub_102f2d90` `0x102f2d90`

_10 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102f2d90(void)
{
    return 1;
}
```

## `sub_102f2da0` `0x102f2da0`

_18 bytes. (leaf/helper — see body)_

```c
int sub_102f2da0(unsigned int a0)
{
    return -(0 < (a0 & 65)) + 1;
}
```

## `sub_102f2dc0` `0x102f2dc0`

_11 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102f2dc0(unsigned int a0)
{
    return a0 & 1;
}
```

## `sub_102f2dd0` `0x102f2dd0`

_71 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102f2dd0(unsigned int a0)
{
    unsigned int v1;  // ecx
    unsigned int v0;  // [bp-0x8]

    v0 = v1;
    if (!((char)a0 & 64) && !(0 < (a0 & 128)) + 1 == !(0 < (a0 & 0x800)) + 1)
    {
        v0 = 1;
        return v0;
    }
    v0 = 0;
    return v0;
}
```

## `sub_102f2e20` `0x102f2e20`

_45 bytes. (leaf/helper — see body)_

```c
int sub_102f2e20(unsigned int a0)
{
    return -(0 < (a0 & 128)) + 1 != -(0 < (a0 & 0x800)) + 1;
}
```

## `sub_102f2e50` `0x102f2e50`

_19 bytes. (leaf/helper — see body)_

```c
int sub_102f2e50(unsigned int a0)
{
    return -(-(0 < (a0 & 0x800)));
}
```

## `sub_102f2e70` `0x102f2e70`

_17 bytes. (leaf/helper — see body)_

```c
int sub_102f2e70(unsigned int a0)
{
    return -(-(0 < (a0 & 4)));
}
```

## `sub_102f2e90` `0x102f2e90`

_19 bytes. (leaf/helper — see body)_

```c
int sub_102f2e90(unsigned int a0)
{
    return -(-(0 < (a0 & 128)));
}
```

## `sub_102f2eb0` `0x102f2eb0`

_17 bytes. (leaf/helper — see body)_

```c
int sub_102f2eb0(unsigned int a0)
{
    return -(-(0 < (a0 & 64)));
}
```

## `sub_102f2ed0` `0x102f2ed0`

_17 bytes. (leaf/helper — see body)_

```c
int sub_102f2ed0(unsigned int a0)
{
    return -(-(0 < (a0 & 65)));
}
```

## `sub_102f2ef0` `0x102f2ef0`

_18 bytes. (leaf/helper — see body)_

```c
int sub_102f2ef0(unsigned int a0)
{
    return -(0 < (a0 & 1)) + 1;
}
```

## `sub_102f2f10` `0x102f2f10`

_71 bytes. (leaf/helper — see body)_

```c
unsigned int sub_102f2f10(unsigned int a0)
{
    unsigned int v1;  // ecx
    unsigned int v0;  // [bp-0x8]

    v0 = v1;
    if (!((char)a0 & 64) && !(0 < (a0 & 128)) + 1 == !(0 < (a0 & 0x800)) + 1)
    {
        v0 = 0;
        return v0;
    }
    v0 = 1;
    return v0;
}
```

## `sub_102f2f60` `0x102f2f60`

_45 bytes. (leaf/helper — see body)_

```c
int sub_102f2f60(unsigned int a0)
{
    return -(0 < (a0 & 128)) + 1 == -(0 < (a0 & 0x800)) + 1;
}
```

## `sub_102f2f90` `0x102f2f90`

_20 bytes. (leaf/helper — see body)_

```c
int sub_102f2f90(unsigned int a0)
{
    return -(0 < (a0 & 0x800)) + 1;
}
```

## `sub_102f2fb0` `0x102f2fb0`

_18 bytes. (leaf/helper — see body)_

```c
int sub_102f2fb0(unsigned int a0)
{
    return -(0 < (a0 & 4)) + 1;
}
```

## `sub_102f2fd0` `0x102f2fd0`

_20 bytes. (leaf/helper — see body)_

```c
int sub_102f2fd0(unsigned int a0)
{
    return -(0 < (a0 & 128)) + 1;
}
```

## `sub_102f2ff0` `0x102f2ff0`

_18 bytes. (leaf/helper — see body)_

```c
int sub_102f2ff0(unsigned int a0)
{
    return -(0 < (a0 & 64)) + 1;
}
```

## `sub_102f3010` `0x102f3010`

_14 bytes. (leaf/helper — see body)_

```c
int sub_102f3010(unsigned int a0, unsigned int a1)
{
    return !a1;
}
```

## `sub_102f3020` `0x102f3020`

_142 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c800;
extern unsigned int g_1038c804;

int sub_102f3020(unsigned int a0)
{
    unsigned int v7;  // edx
    unsigned int v8;  // ebx
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x10]
    int v5;  // [bp-0xc]
    unsigned int v6;  // [bp-0x8]

    v5 = sub_102f04d0(a0);
    v3 = v7;
    v2 = v8;
    v0 = 31;
    v1 = v5 & 0xffff;
    v4 = -(-(0 < _INSERT((char)v1 & (char)v0 - 31, 1, (char)v1 & (char)v0 - 31 & 247)));
    v6 = (g_1038c800 ^ g_1038c804) * 2;
    if (v4)
        v6 |= 1;
    return sub_102f0430(v6);
}
```

## `sub_102f30b0` `0x102f30b0`

_175 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7f0;
extern unsigned int g_1038c7f4;

unsigned int sub_102f30b0(int a0)
{
    unsigned int v6;  // edx
    unsigned int v7;  // ebx
    unsigned int v17;  // 4135
    unsigned int v20;  // 4119
    unsigned int v21;  // eax
    unsigned int v24;  // 4120
    unsigned int v8;  // eax
    unsigned int v27;  // 4135
    unsigned int v28;  // eax
    unsigned int v29;  // cc_ndep
    unsigned int v30;  // cc_dep1
    unsigned int v31;  // 4136
    unsigned int v9;  // 4108
    unsigned int v10;  // cc_dep1
    unsigned int v11;  // 4108
    unsigned int v12;  // 4133
    unsigned int v13;  // 4134
    unsigned int v14;  // eax
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x1c]
    unsigned int v2;  // [bp-0x18]
    unsigned int v3;  // [bp-0x10]
    int v4;  // [bp-0xc]
    unsigned int v5;  // [bp-0x8]

    v4 = sub_102efba0(a0);
    v2 = v6;
    v1 = v7;
    v0 = 3;
    v8 = _INSERT((char)v4 & (char)v0 - 3, 1, (char)v4 & (char)v0 - 3 & 8);
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
    v13 = _ccall(12, 0, v12 & 1, v12 & 1);
    v14 = -(v12 & 1) + 1;
    v17 = _ccall(0, 21, v14 - 1, 0, v13);
    v20 = _ccall(21, v14 - 1, 0, v13);
    v21 = v14;
    v24 = _ccall(0, 21, v21 - 1, 0, v20);
    v27 = _ccall(21, v21 - 1, 0, v20);
    v28 = v21;
    v29 = v27;
    v30 = v28 - 1;
    v31 = _ccall(0, 21, v28 - 1, 0, v27);
    v3 = v28;
    v5 = (g_1038c7f0 ^ g_1038c7f4) * 2;
    if (v3)
        v5 |= 1;
    return sub_102efa50(v5);
}
```

## `sub_102f30fb` `0x102f30fb`

_10 bytes. (leaf/helper — see body)_

```c
void sub_102f30fb(void)
{
    unsigned int v1;  // cc_op
    unsigned int v2;  // cc_dep1
    unsigned int v3;  // cc_dep2
    unsigned int v4;  // cc_ndep
    unsigned int v5;  // 4101

    v5 = _ccall(0, v1, v2, v3, v4);
}
```

## `sub_102f3101` `0x102f3101`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f3101(void)
{
}
```

## `sub_102f3118` `0x102f3118`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f3118(void)
{
}
```

## `sub_102f3127` `0x102f3127`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f3127(void)
{
}
```

## `sub_102f3138` `0x102f3138`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f3138(void)
{
}
```

## `sub_102f3180` `0x102f3180`

_464 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038c7f4;
extern unsigned int g_1038c7f8;

unsigned int sub_102f3180(int a0)
{
    unsigned int v8;  // ebx
    unsigned int v9;  // ecx
    unsigned int v18;  // cc_dep1
    unsigned int v22;  // ecx
    unsigned int v23;  // ecx
    unsigned int v24;  // eax
    char v25;  // cl
    unsigned int v26;  // 4273
    char v27;  // cl
    unsigned int v28;  // 4279
    unsigned int v31;  // 4286
    unsigned int v34;  // 4108
    unsigned int v35;  // 4114
    unsigned int v36;  // 4120
    unsigned int v37;  // 4126
    unsigned int v38;  // cc_ndep
    unsigned int v39;  // cc_dep1
    unsigned int v40;  // 4133
    unsigned int v44;  // eax
    char v45;  // cl
    char v46;  // al
    unsigned int v47;  // cc_dep1
    char v12;  // cl
    char v48;  // cl
    int v50;  // cc_dep1
    unsigned int v51;  // eax
    unsigned int v52;  // 4105
    unsigned short v53;  // ax
    unsigned int v54;  // cc_dep1
    unsigned int v55;  // 4164
    unsigned int v56;  // 4212
    unsigned int v60;  // eax
    unsigned int v14;  // ecx
    unsigned int v15;  // edx
    unsigned int v16;  // ecx
    unsigned int v17;  // cc_ndep
    unsigned int v0;  // [bp-0x20]
    unsigned int v1;  // [bp-0x20]
    unsigned int v2;  // [bp-0x1c]
    unsigned int v3;  // [bp-0x18]
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]

    v4 = v8;
    v6 = sub_102efd90(a0);
    v3 = v9;
    v12 = (char)~(~(~(~(12)) + 7)) + 3;
    v14 = _INSERT(v12 + 23, 0, v12 + 28) - -9;
    v2 = v15;
    v16 = v14 + 4;
    v17 = v14 + 4 < v14;
    v18 = v16 + 1;
    if (!(__buildin_bswap32(v6 * 0x1000000 | v6 * 0x100 & 0xff0000 | v6 >> 8 & 0xff00 | v6 >> 24 & 0xff) & v16 + 1))
    {
        v4 = v8;
        v3 = v9;
        v22 = _INSERT(_INSERT(v9, 1, 0), 0, 164);
        v23 = v22 * 0x1000000 | v22 * 0x100 & 0xff0000 | v22 >> 8 & 0xff00 | v22 >> 24 & 0xff;
        v24 = _INSERT(_INSERT(v6 & 0xffff, 1, 0) & 0xff, 0, ~(~((char)_INSERT(v6 & 0xffff, 1, 0))));
        v25 = (char)v23 * 0 | (char)(v23 >> 24);
        v26 = _ccall(1, (unsigned int)(v25 - 20), 12, 0);
        v27 = v25 - 10;
        v28 = _ccall(19, (unsigned int)(v25 - 9), 0, v26);
        v31 = _ccall(0, 19, (unsigned int)(v25 - 10), 0, v28);
        v34 = _ccall(19, (unsigned int)(v25 - 10), 0, v28);
        v35 = _ccall(19, (unsigned int)(v27 - 1), 0, v34);
        v36 = _ccall(19, (unsigned int)(v27 - 2), 0, v35);
        v37 = _ccall(19, (unsigned int)(v27 - 3), 0, v36);
        v38 = v37;
        v39 = v27 - 4;
        v40 = _ccall(0, 19, (unsigned int)(v27 - 4), 0, v37);
        v44 = v24 * 0x1000000 | v24 * 0x100 & 0xff0000 | v24 >> 8 & 0xff00 | v24 >> 24 & 0xff;
        v45 = ~(~(_INSERT(v27 - 4 CONCAT 0, 0, v27 - 29)));
        v46 = (char)v44 * 0 | (char)(v44 >> 24);
        v47 = v45 + 1;
        v48 = v45 + 3;
        v50 = v46 & v48;
        v51 = _INSERT(v46, 0, v46 & v48);
        v52 = _ccall(0, 13, (unsigned int)(v46 & v48), 0, 0);
        v4 = -(0 < v51) + 1;
        v53 = v6;
        v3 = v8;
        v54 = v53;
        v2 = v8;
        v0 = 31;
        v55 = _ccall(0, 15, (unsigned int)v53, 0, 0);
        v1 = v53;
        v56 = _ccall(0, 19, 243, 0, 0);
        if (-(0 < v51) + 1 != -(0 < _INSERT((char)v1 & (char)v0 - 31, 1, (char)v1 & (char)v0 - 31 & 243)) + 1)
            goto LABEL_102f3330;
        v60 = 1;
    }
    else
    {
LABEL_102f3330:
        v60 = 0;
    }
    v5 = v60;
    v7 = (g_1038c7f4 ^ g_1038c7f8) * 2;
    if (v5)
        v7 |= 1;
    return sub_102efcf0(v7);
}
```

## `sub_102f31af` `0x102f31af`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f31af(void)
{
}
```

## `sub_102f3200` `0x102f3200`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f3200(void)
{
}
```

## `sub_102f3263` `0x102f3263`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f3263(void)
{
}
```

## `sub_102f3278` `0x102f3278`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f3278(void)
{
}
```

## `sub_102f32a8` `0x102f32a8`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f32a8(void)
{
}
```

## `sub_102f32b7` `0x102f32b7`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f32b7(void)
{
    __unsupported_jumpkind_Ijk_NoDecode()
}
```

## `sub_102f32dd` `0x102f32dd`

_3 bytes. (leaf/helper — see body)_

```c
void sub_102f32dd(void)
{
}
```

