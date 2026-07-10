# elfbot.dll decompiled — jiru 0x1036f333..0x1036f8b0

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1036f333` `0x1036f333`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036f333(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036f350` `0x1036f350`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036f350(void)
{
    int v1;  // [bp+0xffff4]

    sub_103362a0(v1);
    return;
}
```

## `sub_1036f358` `0x1036f358`

_11 bytes. (leaf/helper — see body)_

```c
int sub_1036f358(void)
{
    unsigned int v1;  // [bp+0xffff4]

    return sub_10313bb0(v1 + 60);
}
```

## `sub_1036f363` `0x1036f363`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036f363(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036f380` `0x1036f380`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036f380(void)
{
    int v1;  // [bp+0xffff4]

    sub_10331030(v1);
    return;
}
```

## `sub_1036f388` `0x1036f388`

_11 bytes. (leaf/helper — see body)_

```c
void sub_1036f388(void)
{
    int v1;  // [bp+0xffff4]

    sub_10313d70(v1 + 40);
    return;
}
```

## `sub_1036f393` `0x1036f393`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036f393(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036f3b0` `0x1036f3b0`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036f3b0(void)
{
    int v1;  // [bp+0xffff4]

    sub_10336490(v1);
    return;
}
```

## `sub_1036f3b8` `0x1036f3b8`

_11 bytes. (leaf/helper — see body)_

```c
int sub_1036f3b8(void)
{
    unsigned int v1;  // [bp+0xffff4]

    return sub_10313bb0(v1 + 60);
}
```

## `sub_1036f3c3` `0x1036f3c3`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036f3c3(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036f3e0` `0x1036f3e0`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036f3e0(void)
{
    int v1;  // [bp+0xffff4]

    sub_103311b0(v1);
    return;
}
```

## `sub_1036f3e8` `0x1036f3e8`

_11 bytes. (leaf/helper — see body)_

```c
void sub_1036f3e8(void)
{
    int v1;  // [bp+0xffff4]

    sub_10313d70(v1 + 40);
    return;
}
```

## `sub_1036f3f3` `0x1036f3f3`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036f3f3(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036f410` `0x1036f410`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036f410(void)
{
    int v1;  // [bp+0xffff4]

    sub_10336680(v1);
    return;
}
```

## `sub_1036f418` `0x1036f418`

_11 bytes. (leaf/helper — see body)_

```c
int sub_1036f418(void)
{
    unsigned int v1;  // [bp+0xffff4]

    return sub_10313bb0(v1 + 60);
}
```

## `sub_1036f423` `0x1036f423`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036f423(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036f440` `0x1036f440`

_8 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1036f440(void)
{
    int v1;  // [bp+0xffff4]

    return sub_10335b60(v1);
}
```

## `sub_1036f448` `0x1036f448`

_39 bytes. (leaf/helper — see body)_

```c
void sub_1036f448(void)
{
    int v1;  // [bp+0xffff0]
    int v2;  // [bp+0xffff4]

    if (!v2)
    {
        v1 = 0;
        sub_10313d70(v1);
        return;
    }
    v1 = v2 + 84;
    sub_10313d70(v1);
    return;
}
```

## `sub_1036f46f` `0x1036f46f`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036f46f(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036f490` `0x1036f490`

_8 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1036f490(void)
{
    int v1;  // [bp+0xffff4]

    return sub_10339190(v1);
}
```

## `sub_1036f498` `0x1036f498`

_39 bytes. (leaf/helper — see body)_

```c
int sub_1036f498(void)
{
    unsigned int v1;  // [bp+0xffff0]
    unsigned int v2;  // [bp+0xffff4]

    if (v2)
        v1 = v2 + 104;
    else
        v1 = 0;
    return sub_10313bb0(v1);
}
```

## `sub_1036f4bf` `0x1036f4bf`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036f4bf(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036f4e0` `0x1036f4e0`

_11 bytes. (leaf/helper — see body)_

```c
void sub_1036f4e0(void)
{
    unsigned int v0;  // [bp-0x4]
    unsigned int v2;  // [bp+0xffff0]

    v0 = v2;
    sub_10350abd();
    return;
}
```

## `sub_1036f4eb` `0x1036f4eb`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036f4eb(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036f510` `0x1036f510`

_8 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1036f510(void)
{
    int v1;  // [bp+0xffff4]

    return sub_10335fe0(v1);
}
```

## `sub_1036f518` `0x1036f518`

_39 bytes. (leaf/helper — see body)_

```c
void sub_1036f518(void)
{
    int v1;  // [bp+0xffff0]
    int v2;  // [bp+0xffff4]

    if (!v2)
    {
        v1 = 0;
        sub_10313d70(v1);
        return;
    }
    v1 = v2 + 84;
    sub_10313d70(v1);
    return;
}
```

## `sub_1036f53f` `0x1036f53f`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036f53f(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036f560` `0x1036f560`

_8 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1036f560(void)
{
    int v1;  // [bp+0xffff4]

    return sub_10339380(v1);
}
```

## `sub_1036f568` `0x1036f568`

_39 bytes. (leaf/helper — see body)_

```c
int sub_1036f568(void)
{
    unsigned int v1;  // [bp+0xffff0]
    unsigned int v2;  // [bp+0xffff4]

    if (v2)
        v1 = v2 + 104;
    else
        v1 = 0;
    return sub_10313bb0(v1);
}
```

## `sub_1036f58f` `0x1036f58f`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036f58f(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036f5b0` `0x1036f5b0`

_11 bytes. (leaf/helper — see body)_

```c
void sub_1036f5b0(void)
{
    unsigned int v0;  // [bp-0x4]
    unsigned int v2;  // [bp+0xffff0]

    v0 = v2;
    sub_10350abd();
    return;
}
```

## `sub_1036f5bb` `0x1036f5bb`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036f5bb(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036f5e0` `0x1036f5e0`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036f5e0(void)
{
    unsigned int v1;  // [bp+0xffff4]

    sub_103388a0(v1);
    return;
}
```

## `sub_1036f5e8` `0x1036f5e8`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036f5e8(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036f610` `0x1036f610`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036f610(void)
{
    unsigned int v1;  // [bp+0xffff4]

    sub_103388a0(v1);
    return;
}
```

## `sub_1036f618` `0x1036f618`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036f618(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036f640` `0x1036f640`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036f640(void)
{
    unsigned int v1;  // [bp+0xffff4]

    sub_103388a0(v1);
    return;
}
```

## `sub_1036f648` `0x1036f648`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036f648(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036f670` `0x1036f670`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036f670(void)
{
    unsigned int v1;  // [bp+0xffff4]

    sub_103388a0(v1);
    return;
}
```

## `sub_1036f678` `0x1036f678`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036f678(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036f6a0` `0x1036f6a0`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036f6a0(void)
{
    unsigned int v1;  // [bp+0xffff4]

    sub_103388a0(v1);
    return;
}
```

## `sub_1036f6a8` `0x1036f6a8`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036f6a8(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036f6d0` `0x1036f6d0`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036f6d0(void)
{
    unsigned int v1;  // [bp+0xffff4]

    sub_103388a0(v1);
    return;
}
```

## `sub_1036f6d8` `0x1036f6d8`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036f6d8(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036f700` `0x1036f700`

_8 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1036f700(void)
{
    return sub_103368a0(/* unsupported instruction */ - 20);
}
```

## `sub_1036f708` `0x1036f708`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036f708(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036f730` `0x1036f730`

_25 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1036f730(void)
{
    unsigned int v1;  // [bp+0xffff4]
    int v2;  // [bp+0x10000c]

    if (!((char)v1 & 1))
        return v1 & 1;
    v1 &= 4294967294;
    return sub_10339190(v2);
}
```

## `sub_1036f749` `0x1036f749`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036f749(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036f770` `0x1036f770`

_25 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1036f770(void)
{
    unsigned int v1;  // [bp+0xffff4]
    unsigned int v2;  // [bp+0x10000c]

    if (!((char)v1 & 1))
        return v1 & 1;
    v1 &= 4294967294;
    return sub_10339220(v2);
}
```

## `sub_1036f789` `0x1036f789`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036f789(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036f7b0` `0x1036f7b0`

_8 bytes. (leaf/helper — see body)_

```c
unsigned int * sub_1036f7b0(void)
{
    return sub_103369a0(/* unsupported instruction */ - 20);
}
```

## `sub_1036f7b8` `0x1036f7b8`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036f7b8(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036f7e0` `0x1036f7e0`

_25 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1036f7e0(void)
{
    unsigned int v1;  // [bp+0xffff4]
    int v2;  // [bp+0x10000c]

    if (!((char)v1 & 1))
        return v1 & 1;
    v1 &= 4294967294;
    return sub_10339380(v2);
}
```

## `sub_1036f7f9` `0x1036f7f9`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036f7f9(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036f820` `0x1036f820`

_25 bytes. (leaf/helper — see body)_

```c
unsigned int sub_1036f820(void)
{
    unsigned int v1;  // [bp+0xffff4]
    unsigned int v2;  // [bp+0x10000c]

    if (!((char)v1 & 1))
        return v1 & 1;
    v1 &= 4294967294;
    return sub_10339410(v2);
}
```

## `sub_1036f839` `0x1036f839`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036f839(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036f860` `0x1036f860`

_11 bytes. (leaf/helper — see body)_

```c
void sub_1036f860(void)
{
    unsigned int v1;  // [bp+0xffff0]

    sub_103388a0(v1 + 4);
    return;
}
```

## `sub_1036f86b` `0x1036f86b`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036f86b(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036f890` `0x1036f890`

_27 bytes. (leaf/helper — see body)_

```c
int sub_1036f890(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    sub_10351225();
    return sub_1035293d();
}
```

## `sub_1036f8b0` `0x1036f8b0`

_8 bytes. (leaf/helper — see body)_

```c
void sub_1036f8b0(void)
{
    sub_1031a3a0(/* unsupported instruction */ - 52);
    return;
}
```

