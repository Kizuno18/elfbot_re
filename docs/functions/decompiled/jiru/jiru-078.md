# elfbot.dll decompiled — jiru 0x1036c463..0x1036c84b

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1036c463` `0x1036c463`

_25 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1036c463(void)
{
    unsigned int v1;  // [bp+0xfffc8]
    int v2;  // [bp+0x10000c]

    if (!((char)v1 & 1))
        return v1 & 1;
    v1 &= 4294967294;
    return sub_1031a040(v2);
}
```

## `sub_1036c47c` `0x1036c47c`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036c47c(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036c497` `0x1036c497`

_14 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a2984;

unsigned int sub_1036c497(void)
{
    unsigned int v1;  // eax

    v1 = g_103a2984;
    g_103a2984 = v1 & 4294967294;
    return v1 & 4294967294;
}
```

## `sub_1036c4a5` `0x1036c4a5`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036c4a5(void)
{
    sub_10314610(/* unsupported instruction */ - 56);
    return;
}
```

## `sub_1036c4ad` `0x1036c4ad`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036c4ad(void)
{
    sub_1032e3f0(/* unsupported instruction */ - 28);
    return;
}
```

## `sub_1036c4b5` `0x1036c4b5`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036c4b5(void)
{
    sub_1031a3a0(/* unsupported instruction */ - 84);
    return;
}
```

## `sub_1036c4bd` `0x1036c4bd`

_31 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1036c4bd(void)
{
    unsigned int v1;  // [bp+0xfff2c]
    int v2;  // [bp+0x10000c]

    if (!((char)v1 & 1))
        return v1 & 1;
    v1 &= 4294967294;
    return sub_1031a0e0(v2);
}
```

## `sub_1036c4dc` `0x1036c4dc`

_11 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1036c4dc(void)
{
    return sub_1031a040(/* unsupported instruction */ - 212);
}
```

## `sub_1036c4e7` `0x1036c4e7`

_11 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1036c4e7(void)
{
    return sub_10319f00(/* unsupported instruction */ - 180);
}
```

## `sub_1036c4f2` `0x1036c4f2`

_30 bytes. (leaf/helper — see body)_

```c
int sub_1036c4f2(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036c510` `0x1036c510`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036c510(void)
{
    sub_1032e280(/* unsupported instruction */ - 28);
    return;
}
```

## `sub_1036c518` `0x1036c518`

_25 bytes. (leaf/helper — see body)_

```c
int sub_1036c518(void)
{
    unsigned int v1;  // [bp+0xfffe4]
    int v2;  // [bp+0x10000c]

    if (!((char)v1 & 1))
        return v1 & 1;
    v1 &= 4294967294;
    return (unsigned int)sub_10314610(v2);
}
```

## `sub_1036c531` `0x1036c531`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036c531(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036c54c` `0x1036c54c`

_14 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a298c;

unsigned int sub_1036c54c(void)
{
    unsigned int v1;  // eax

    v1 = g_103a298c;
    g_103a298c = v1 & 4294967294;
    return v1 & 4294967294;
}
```

## `sub_1036c55a` `0x1036c55a`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036c55a(void)
{
    sub_10314610(/* unsupported instruction */ - 56);
    return;
}
```

## `sub_1036c562` `0x1036c562`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036c562(void)
{
    sub_1032e3f0(/* unsupported instruction */ - 28);
    return;
}
```

## `sub_1036c56a` `0x1036c56a`

_31 bytes. (leaf/helper — see body)_

```c
int sub_1036c56a(void)
{
    unsigned int v1;  // [bp+0xfff4c]
    int v2;  // [bp+0x10000c]

    if (!((char)v1 & 1))
        return v1 & 1;
    v1 &= 4294967294;
    return (unsigned int)sub_1031a3a0(v2);
}
```

## `sub_1036c589` `0x1036c589`

_11 bytes. (leaf/helper — see body)_

```c
void sub_1036c589(void)
{
    sub_10314610(/* unsupported instruction */ - 180);
    return;
}
```

## `sub_1036c594` `0x1036c594`

_11 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1036c594(void)
{
    return sub_10319f00(/* unsupported instruction */ - 152);
}
```

## `sub_1036c59f` `0x1036c59f`

_30 bytes. (leaf/helper — see body)_

```c
int sub_1036c59f(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036c5bd` `0x1036c5bd`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036c5bd(void)
{
    sub_1032e280(/* unsupported instruction */ - 28);
    return;
}
```

## `sub_1036c5c5` `0x1036c5c5`

_25 bytes. (leaf/helper — see body)_

```c
int sub_1036c5c5(void)
{
    unsigned int v1;  // [bp+0xfffe4]
    int v2;  // [bp+0x10000c]

    if (!((char)v1 & 1))
        return v1 & 1;
    v1 &= 4294967294;
    return (unsigned int)sub_10314610(v2);
}
```

## `sub_1036c5de` `0x1036c5de`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036c5de(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036c5f9` `0x1036c5f9`

_14 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a2994;

unsigned int sub_1036c5f9(void)
{
    unsigned int v1;  // eax

    v1 = g_103a2994;
    g_103a2994 = v1 & 4294967294;
    return v1 & 4294967294;
}
```

## `sub_1036c607` `0x1036c607`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036c607(void)
{
    sub_10314610(/* unsupported instruction */ - 56);
    return;
}
```

## `sub_1036c60f` `0x1036c60f`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036c60f(void)
{
    sub_1032e3f0(/* unsupported instruction */ - 28);
    return;
}
```

## `sub_1036c617` `0x1036c617`

_31 bytes. (leaf/helper — see body)_

```c
int sub_1036c617(void)
{
    unsigned int v1;  // [bp+0xfff4c]
    int v2;  // [bp+0x10000c]

    if (!((char)v1 & 1))
        return v1 & 1;
    v1 &= 4294967294;
    return (unsigned int)sub_1031a3a0(v2);
}
```

## `sub_1036c636` `0x1036c636`

_11 bytes. (leaf/helper — see body)_

```c
void sub_1036c636(void)
{
    sub_10314610(/* unsupported instruction */ - 180);
    return;
}
```

## `sub_1036c641` `0x1036c641`

_11 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1036c641(void)
{
    return sub_10319f00(/* unsupported instruction */ - 152);
}
```

## `sub_1036c64c` `0x1036c64c`

_30 bytes. (leaf/helper — see body)_

```c
int sub_1036c64c(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036c66a` `0x1036c66a`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036c66a(void)
{
    sub_1032e280(/* unsupported instruction */ - 28);
    return;
}
```

## `sub_1036c672` `0x1036c672`

_25 bytes. (leaf/helper — see body)_

```c
int sub_1036c672(void)
{
    unsigned int v1;  // [bp+0xfffe4]
    int v2;  // [bp+0x10000c]

    if (!((char)v1 & 1))
        return v1 & 1;
    v1 &= 4294967294;
    return (unsigned int)sub_10314610(v2);
}
```

## `sub_1036c68b` `0x1036c68b`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036c68b(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036c6a6` `0x1036c6a6`

_14 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a299c;

unsigned int sub_1036c6a6(void)
{
    unsigned int v1;  // eax

    v1 = g_103a299c;
    g_103a299c = v1 & 4294967294;
    return v1 & 4294967294;
}
```

## `sub_1036c6b4` `0x1036c6b4`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036c6b4(void)
{
    sub_10314610(/* unsupported instruction */ - 56);
    return;
}
```

## `sub_1036c6bc` `0x1036c6bc`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036c6bc(void)
{
    sub_1032e3f0(/* unsupported instruction */ - 28);
    return;
}
```

## `sub_1036c6c4` `0x1036c6c4`

_31 bytes. (leaf/helper — see body)_

```c
int sub_1036c6c4(void)
{
    unsigned int v1;  // [bp+0xfff4c]
    int v2;  // [bp+0x10000c]

    if (!((char)v1 & 1))
        return v1 & 1;
    v1 &= 4294967294;
    return (unsigned int)sub_1031a3a0(v2);
}
```

## `sub_1036c6e3` `0x1036c6e3`

_11 bytes. (leaf/helper — see body)_

```c
void sub_1036c6e3(void)
{
    sub_10314610(/* unsupported instruction */ - 180);
    return;
}
```

## `sub_1036c6ee` `0x1036c6ee`

_11 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1036c6ee(void)
{
    return sub_10319f00(/* unsupported instruction */ - 152);
}
```

## `sub_1036c6f9` `0x1036c6f9`

_30 bytes. (leaf/helper — see body)_

```c
int sub_1036c6f9(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036c717` `0x1036c717`

_14 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a29a4;

unsigned int sub_1036c717(void)
{
    unsigned int v1;  // eax

    v1 = g_103a29a4;
    g_103a29a4 = v1 & 4294967294;
    return v1 & 4294967294;
}
```

## `sub_1036c725` `0x1036c725`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036c725(void)
{
    sub_10314610(/* unsupported instruction */ - 40);
    return;
}
```

## `sub_1036c72d` `0x1036c72d`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036c72d(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036c748` `0x1036c748`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036c748(void)
{
    sub_1032e280(/* unsupported instruction */ - 0x44);
    return;
}
```

## `sub_1036c750` `0x1036c750`

_11 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1036c750(void)
{
    return sub_10319f00(/* unsupported instruction */ - 168);
}
```

## `sub_1036c75b` `0x1036c75b`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036c75b(void)
{
    sub_10314610(/* unsupported instruction */ - 52);
    return;
}
```

## `sub_1036c763` `0x1036c763`

_31 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1036c763(void)
{
    unsigned int v1;  // [bp+0xfff58]
    int v2;  // [bp+0x10000c]

    if (!((char)v1 & 1))
        return v1 & 1;
    v1 &= 4294967294;
    return sub_1031a040(v2);
}
```

## `sub_1036c782` `0x1036c782`

_40 bytes. (leaf/helper — see body)_

```c
int sub_1036c782(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036c7aa` `0x1036c7aa`

_14 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a29ac;

unsigned int sub_1036c7aa(void)
{
    unsigned int v1;  // eax

    v1 = g_103a29ac;
    g_103a29ac = v1 & 4294967294;
    return v1 & 4294967294;
}
```

## `sub_1036c7b8` `0x1036c7b8`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036c7b8(void)
{
    sub_10314610(/* unsupported instruction */ - 96);
    return;
}
```

## `sub_1036c7c0` `0x1036c7c0`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036c7c0(void)
{
    sub_1032e3f0(/* unsupported instruction */ - 0x44);
    return;
}
```

## `sub_1036c7c8` `0x1036c7c8`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036c7c8(void)
{
    sub_1031a3a0(/* unsupported instruction */ - 128);
    return;
}
```

## `sub_1036c7d0` `0x1036c7d0`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036c7d0(void)
{
    sub_1031a3a0(/* unsupported instruction */ - 52);
    return;
}
```

## `sub_1036c7d8` `0x1036c7d8`

_31 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1036c7d8(void)
{
    unsigned int v1;  // [bp+0xfff00]
    int v2;  // [bp+0x10000c]

    if (!((char)v1 & 1))
        return v1 & 1;
    v1 &= 4294967294;
    return sub_1031a0e0(v2);
}
```

## `sub_1036c7f7` `0x1036c7f7`

_11 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1036c7f7(void)
{
    return sub_1031a040(/* unsupported instruction */ - 0x100);
}
```

## `sub_1036c802` `0x1036c802`

_11 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1036c802(void)
{
    return sub_10319f00(/* unsupported instruction */ - 224);
}
```

## `sub_1036c80d` `0x1036c80d`

_40 bytes. (leaf/helper — see body)_

```c
int sub_1036c80d(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036c835` `0x1036c835`

_14 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_103a29b4;

unsigned int sub_1036c835(void)
{
    unsigned int v1;  // eax

    v1 = g_103a29b4;
    g_103a29b4 = v1 & 4294967294;
    return v1 & 4294967294;
}
```

## `sub_1036c843` `0x1036c843`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036c843(void)
{
    sub_10314610(/* unsupported instruction */ - 40);
    return;
}
```

## `sub_1036c84b` `0x1036c84b`

_11 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1036c84b(void)
{
    return sub_10319f00(/* unsupported instruction */ - 140);
}
```

