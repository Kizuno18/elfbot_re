# elfbot.dll decompiled — jdrv 0x1002e320..0x1002f12a

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_1002e320` `0x1002e320`

_15 bytes. (leaf/helper — see body)_

```c
void sub_1002e320(void)
{
    int v1;  // [bp+0x100000]

    sub_10038eb3(v1, 0);
}
```

## `sub_1002e332` `0x1002e332`

_15 bytes. (leaf/helper — see body)_

```c
void sub_1002e332(void)
{
    int v1;  // [bp+0x100000]

    sub_10038eb3(v1, 0);
}
```

## `sub_1002e344` `0x1002e344`

_15 bytes. (leaf/helper — see body)_

```c
void sub_1002e344(void)
{
    int v1;  // [bp+0x100000]

    sub_10038eb3(v1, 0);
}
```

## cmd_coretarget `0x1002e353`

Named — see [doc 11](../../11-*.md). _8 bytes. (leaf/helper — see body)_

```c
int sub_1002e353(void)
{
    unsigned int v2;  // ebx
    unsigned int v0;  // [bp-0x4]

    v0 = v2;
    sub_1002355e();
}
```

## `sub_1002e35e` `0x1002e35e`

_9 bytes. (leaf/helper — see body)_

```c
int sub_1002e35e(void)
{
    unsigned int v0;  // [bp+0x0]

    sub_100235e8(v0);
}
```

## `sub_1002e36a` `0x1002e36a`

_20 bytes. (leaf/helper — see body)_

```c
int sub_1002e36a(void)
{
    unsigned int v0;  // [bp+0x0]

    if (sub_100235e8(v0))
        sub_1002355e();
}
```

## cmd_name `0x1002e460`

Named — see [doc 11](../../11-*.md). _19 bytes. (leaf/helper — see body)_

```c
int sub_1002e460(void)
{
    int v2;  // ebx
    int v1;  // [bp+0xffffc]

    lstrcpy(v1, v2 + 4);
}
```

## cmd_id `0x1002e473`

Named — see [doc 11](../../11-*.md). _25 bytes. (leaf/helper — see body)_

```c
int sub_1002e473(void)
{
    unsigned int *v3;  // ebx
    unsigned int v0;  // [bp-0x4]
    PSTR v2;  // [bp+0xffffc]

    v0 = *(v3);
    wsprintfA(v2, "%d");
}
```

## cmd_posx `0x1002e48c`

Named — see [doc 11](../../11-*.md). _26 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[36];
    unsigned int field_24;
} struct_0;

int sub_1002e48c(void)
{
    struct_0 *v3;  // ebx
    unsigned int v0;  // [bp-0x4]
    PSTR v2;  // [bp+0xffffc]

    v0 = v3->field_24;
    wsprintfA(v2, "%d");
}
```

## cmd_distance `0x1002e4a6`

Named — see [doc 11](../../11-*.md). _57 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1005f854;
extern unsigned int g_1005f858;

int sub_1002e4a6(void)
{
    unsigned int idx[11];  // ebx
    int v4;  // eax
    unsigned int v5;  // ecx
    int v6;  // eax
    unsigned int v8;  // eax
    unsigned int v0;  // [bp-0x4]
    PSTR v2;  // [bp+0xffffc]

    v4 = g_1005f854 - idx[9];
    v5 = (v4 ^ v4 >> 31) - (v4 >> 31);
    v6 = g_1005f858 - idx[10];
    v8 = (v6 ^ v6 >> 31) - (v6 >> 31);
    if (v8 < v5)
        v8 = v5;
    v0 = v8;
    wsprintfA(v2, "%d");
}
```

## cmd_distx `0x1002e4df`

Named — see [doc 11](../../11-*.md). _37 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[36];
    unsigned int field_24;
} struct_0;

extern unsigned int g_1005f854;

int sub_1002e4df(void)
{
    struct_0 *v3;  // ebx
    int v4;  // eax
    unsigned int v0;  // [bp-0x4]
    PSTR v2;  // [bp+0xffffc]

    v4 = g_1005f854 - v3->field_24;
    v0 = (v4 ^ v4 >> 31) - (v4 >> 31);
    wsprintfA(v2, "%d");
}
```

## cmd_disty `0x1002e504`

Named — see [doc 11](../../11-*.md). _37 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned int field_28;
} struct_0;

extern unsigned int g_1005f858;

int sub_1002e504(void)
{
    struct_0 *v3;  // ebx
    int v4;  // eax
    unsigned int v0;  // [bp-0x4]
    PSTR v2;  // [bp+0xffffc]

    v4 = g_1005f858 - v3->field_28;
    v0 = (v4 ^ v4 >> 31) - (v4 >> 31);
    wsprintfA(v2, "%d");
}
```

## cmd_posy `0x1002e529`

Named — see [doc 11](../../11-*.md). _26 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[40];
    unsigned int field_28;
} struct_0;

int sub_1002e529(void)
{
    struct_0 *v3;  // ebx
    unsigned int v0;  // [bp-0x4]
    PSTR v2;  // [bp+0xffffc]

    v0 = v3->field_28;
    wsprintfA(v2, "%d");
}
```

## cmd_posz `0x1002e543`

Named — see [doc 11](../../11-*.md). _26 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[44];
    unsigned int field_2c;
} struct_0;

int sub_1002e543(void)
{
    struct_0 *v3;  // ebx
    unsigned int v0;  // [bp-0x4]
    PSTR v2;  // [bp+0xffffc]

    v0 = v3->field_2c;
    wsprintfA(v2, "%d");
}
```

## cmd_dir `0x1002e55d`

Named — see [doc 11](../../11-*.md). _26 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[80];
    unsigned int field_50;
} struct_0;

int sub_1002e55d(void)
{
    struct_0 *v3;  // ebx
    unsigned int v0;  // [bp-0x4]
    PSTR v2;  // [bp+0xffffc]

    v0 = v3->field_50;
    wsprintfA(v2, "%d");
}
```

## cmd_outfit `0x1002e577`

Named — see [doc 11](../../11-*.md). _26 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[96];
    unsigned int field_60;
} struct_0;

int sub_1002e577(void)
{
    struct_0 *v3;  // ebx
    unsigned int v0;  // [bp-0x4]
    PSTR v2;  // [bp+0xffffc]

    v0 = v3->field_60;
    wsprintfA(v2, "%d");
}
```

## cmd_hppc `0x1002e591`

Named — see [doc 11](../../11-*.md). _29 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[136];
    unsigned int field_88;
} struct_0;

int sub_1002e591(void)
{
    struct_0 *v3;  // ebx
    unsigned int v0;  // [bp-0x4]
    PSTR v2;  // [bp+0xffffc]

    v0 = v3->field_88;
    wsprintfA(v2, "%d");
}
```

## cmd_speed `0x1002e5ae`

Named — see [doc 11](../../11-*.md). _29 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[140];
    unsigned int field_8c;
} struct_0;

int sub_1002e5ae(void)
{
    struct_0 *v3;  // ebx
    unsigned int v0;  // [bp-0x4]
    PSTR v2;  // [bp+0xffffc]

    v0 = v3->field_8c;
    wsprintfA(v2, "%d");
}
```

## cmd_isparalyzed `0x1002e5cb`

Named — see [doc 11](../../11-*.md). _32 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[140];
    unsigned int field_8c;
} struct_0;

void sub_1002e5cb(void)
{
    unsigned short *v2;  // ecx
    struct_0 *v3;  // ebx
    unsigned short *v1;  // [bp+0xffffc]

    v2 = v1;
    *(v2) = 48;
    if (v3->field_8c < 200)
        *(v2) = 49;
}
```

## cmd_color1 `0x1002e5eb`

Named — see [doc 11](../../11-*.md). _26 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[100];
    unsigned int field_64;
} struct_0;

int sub_1002e5eb(void)
{
    struct_0 *v3;  // ebx
    unsigned int v0;  // [bp-0x4]
    PSTR v2;  // [bp+0xffffc]

    v0 = v3->field_64;
    wsprintfA(v2, "%d");
}
```

## cmd_color2 `0x1002e605`

Named — see [doc 11](../../11-*.md). _26 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[104];
    unsigned int field_68;
} struct_0;

int sub_1002e605(void)
{
    struct_0 *v3;  // ebx
    unsigned int v0;  // [bp-0x4]
    PSTR v2;  // [bp+0xffffc]

    v0 = v3->field_68;
    wsprintfA(v2, "%d");
}
```

## cmd_color3 `0x1002e61f`

Named — see [doc 11](../../11-*.md). _26 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[108];
    unsigned int field_6c;
} struct_0;

int sub_1002e61f(void)
{
    struct_0 *v3;  // ebx
    unsigned int v0;  // [bp-0x4]
    PSTR v2;  // [bp+0xffffc]

    v0 = v3->field_6c;
    wsprintfA(v2, "%d");
}
```

## cmd_color4 `0x1002e639`

Named — see [doc 11](../../11-*.md). _26 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[112];
    unsigned int field_70;
} struct_0;

int sub_1002e639(void)
{
    struct_0 *v3;  // ebx
    unsigned int v0;  // [bp-0x4]
    PSTR v2;  // [bp+0xffffc]

    v0 = v3->field_70;
    wsprintfA(v2, "%d");
}
```

## cmd_skull `0x1002e653`

Named — see [doc 11](../../11-*.md). _29 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[148];
    unsigned int field_94;
} struct_0;

int sub_1002e653(void)
{
    struct_0 *v3;  // ebx
    unsigned int v0;  // [bp-0x4]
    PSTR v2;  // [bp+0xffffc]

    v0 = v3->field_94;
    wsprintfA(v2, "%d");
}
```

## cmd_party `0x1002e670`

Named — see [doc 11](../../11-*.md). _29 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[152];
    unsigned int field_98;
} struct_0;

int sub_1002e670(void)
{
    struct_0 *v3;  // ebx
    unsigned int v0;  // [bp-0x4]
    PSTR v2;  // [bp+0xffffc]

    v0 = v3->field_98;
    wsprintfA(v2, "%d");
}
```

## cmd_warbanner `0x1002e68d`

Named — see [doc 11](../../11-*.md). _29 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[160];
    unsigned int field_a0;
} struct_0;

int sub_1002e68d(void)
{
    struct_0 *v3;  // ebx
    unsigned int v0;  // [bp-0x4]
    PSTR v2;  // [bp+0xffffc]

    v0 = v3->field_a0;
    wsprintfA(v2, "%d");
}
```

## cmd_ismonster `0x1002e6aa`

Named — see [doc 11](../../11-*.md). _26 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[3];
    char field_3;
} struct_0;

void sub_1002e6aa(void)
{
    unsigned short *v2;  // ecx
    struct_0 *v3;  // ebx
    unsigned short *v1;  // [bp+0xffffc]

    v2 = v1;
    *(v2) = 48;
    if (v3->field_3 == 64)
        *(v2) = 49;
}
```

## cmd_isnpc `0x1002e6c4`

Named — see [doc 11](../../11-*.md). _41 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[3];
    char field_3;
} struct_0;

int sub_1002e6c4(void)
{
    struct_0 *v3;  // ebx
    unsigned short *v4;  // ecx
    struct_0 *v0;  // [bp-0x4]
    unsigned short *v2;  // [bp+0xffffc]

    *(v2) = 48;
    if (v3->field_3 == 64)
    {
        v0 = v3;
        if (sub_1000d287(v3 + 1))
            *(v4) = 49;
    }
}
```

## cmd_isplayer `0x1002e6ed`

Named — see [doc 11](../../11-*.md). _26 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[3];
    char field_3;
} struct_0;

void sub_1002e6ed(void)
{
    unsigned short *v2;  // ecx
    struct_0 *v3;  // ebx
    unsigned short *v1;  // [bp+0xffffc]

    v2 = v1;
    *(v2) = 48;
    if (v3->field_3 != 64)
        *(v2) = 49;
}
```

## cmd_isonscreen `0x1002e707`

Named — see [doc 11](../../11-*.md). _30 bytes. (leaf/helper — see body)_

```c
int sub_1002e707(void)
{
    int v2;  // ebx
    unsigned int v3;  // eax
    unsigned short *v4;  // ecx
    unsigned short *v1;  // [bp+0xffffc]

    v3 = sub_1003c23e(v2);
    v4 = v1;
    *(v4) = 48;
    if (v3)
        *(v4) = 49;
}
```

## cmd_isshootable `0x1002e725`

Named — see [doc 11](../../11-*.md). _50 bytes. (leaf/helper — see body)_

```c
int sub_1002e725(void)
{
    int v2[11];  // ebx
    unsigned short *v1;  // [bp+0xffffc]

    *(v1) = 48;
    if (sub_1003c23e(v2) && sub_10011678(v2[9], v2[10], 0))
        *(v1) = 49;
}
```

## cmd_canshoot `0x1002e757`

Named — see [doc 11](../../11-*.md). _93 bytes. (leaf/helper — see body)_

```c
int sub_1002e757(void)
{
    int v4;  // ebx
    int v5[11];  // eax
    int v1;  // [bp+0xfef80]
    int v2;  // [bp+0xfef84]
    unsigned short *v3;  // [bp+0xffffc]

    *(v3) = 48;
    if (sub_1003c23e(v4))
    {
        sub_10030225(v4);
        v5 = sub_100399af(/* unsupported instruction */ - 4264);
        if (v5 && sub_1003c55d(v5[9], v5[10], v1, v2, 0))
            *(v3) = 49;
    }
}
```

## cmd_isenemy `0x1002e7b4`

Named — see [doc 11](../../11-*.md). _33 bytes. (leaf/helper — see body)_

```c
int sub_1002e7b4(void)
{
    int v2;  // ebx
    unsigned int v3;  // eax
    unsigned short *v4;  // ecx
    unsigned short *v1;  // [bp+0xffffc]

    v3 = sub_1003a494(v2 + 4);
    v4 = v1;
    *(v4) = 48;
    if (v3)
        *(v4) = 49;
}
```

## cmd_isonnavi `0x1002e7d5`

Named — see [doc 11](../../11-*.md). _31 bytes. (leaf/helper — see body)_

```c
int sub_1002e7d5(void)
{
    int *v2;  // ebx
    unsigned int v3;  // eax
    unsigned short *v4;  // ecx
    unsigned short *v1;  // [bp+0xffffc]

    v3 = sub_1003b0f0(*(v2));
    v4 = v1;
    *(v4) = 48;
    if (v3)
        *(v4) = 49;
}
```

## cmd_isleader `0x1002e7f4`

Named — see [doc 11](../../11-*.md). _33 bytes. (leaf/helper — see body)_

```c
int sub_1002e7f4(void)
{
    int v2;  // ebx
    unsigned int v3;  // eax
    unsigned short *v4;  // ecx
    unsigned short *v1;  // [bp+0xffffc]

    v3 = sub_100303be(v2 + 4);
    v4 = v1;
    *(v4) = 48;
    if (v3)
        *(v4) = 49;
}
```

## cmd_isfriend `0x1002e815`

Named — see [doc 11](../../11-*.md). _33 bytes. (leaf/helper — see body)_

```c
int sub_1002e815(void)
{
    int v2;  // ebx
    unsigned int v3;  // eax
    unsigned short *v4;  // ecx
    unsigned short *v1;  // [bp+0xffffc]

    v3 = sub_1003a320(v2 + 4);
    v4 = v1;
    *(v4) = 48;
    if (v3)
        *(v4) = 49;
}
```

## cmd_issubenemy `0x1002e836`

Named — see [doc 11](../../11-*.md). _33 bytes. (leaf/helper — see body)_

```c
int sub_1002e836(void)
{
    int v2;  // ebx
    unsigned int v3;  // eax
    unsigned short *v4;  // ecx
    unsigned short *v1;  // [bp+0xffffc]

    v3 = sub_1003a550(v2 + 4);
    v4 = v1;
    *(v4) = 48;
    if (v3)
        *(v4) = 49;
}
```

## cmd_issubfriend `0x1002e857`

Named — see [doc 11](../../11-*.md). _33 bytes. (leaf/helper — see body)_

```c
int sub_1002e857(void)
{
    int v2;  // ebx
    unsigned int v3;  // eax
    unsigned short *v4;  // ecx
    unsigned short *v1;  // [bp+0xffffc]

    v3 = sub_1003a3da(v2 + 4);
    v4 = v1;
    *(v4) = 48;
    if (v3)
        *(v4) = 49;
}
```

## cmd_haslookinfo `0x1002e878`

Named — see [doc 11](../../11-*.md). _39 bytes. (leaf/helper — see body)_

```c
int sub_1002e878(void)
{
    char v2[81];  // eax
    unsigned short *v3;  // ecx
    unsigned short *v1;  // [bp+0xffffc]

    v2 = sub_10023861();
    v3 = v1;
    *(v3) = 48;
    if (v2[78] || v2[80])
        *(v3) = 49;
}
```

## cmd_guild `0x1002e89f`

Named — see [doc 11](../../11-*.md). _26 bytes. (leaf/helper — see body)_

```c
int sub_1002e89f(void)
{
    int v2;  // eax
    int v1;  // [bp+0xffffc]

    v2 = sub_10023861();
    lstrcpy(v1, v2 + 32);
}
```

## cmd_voc `0x1002e8b9`

Named — see [doc 11](../../11-*.md). _30 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[76];
    char field_4c;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
} struct_1;


int sub_1002e8b9(void)
{
    struct_0 *v2;  // eax
    struct_1 **v1;  // [bp+0xffffc]

    v2 = sub_10023861();
    *(v1) = *((int *)(0x10058100 + 4 * v2->field_4c));
}
```

## cmd_vocation `0x1002e8d7`

Named — see [doc 11](../../11-*.md). _33 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[76];
    char field_4c;
} struct_0;

extern unsigned int g_100438fc[4];

int sub_1002e8d7(void)
{
    struct_0 *v2;  // eax
    int v1;  // [bp+0xffffc]

    v2 = sub_10023861();
    lstrcpy(v1, g_100438fc[v2->field_4c]);
}
```

## cmd_level `0x1002e8f8`

Named — see [doc 11](../../11-*.md). _25 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[72];
    int field_48;
} struct_0;

int sub_1002e8f8(void)
{
    struct_0 *v2;  // eax
    int v1;  // [bp+0xffffc]

    v2 = sub_10023861();
    sub_10040940(v2->field_48, v1);
}
```

## cmd_isknight `0x1002e911`

Named — see [doc 11](../../11-*.md). _39 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[76];
    char field_4c;
} struct_0;

int sub_1002e911(void)
{
    struct_0 *v2;  // eax
    unsigned short *v3;  // ecx
    unsigned short *v1;  // [bp+0xffffc]

    v2 = sub_10023861();
    v3 = v1;
    *(v3) = 48;
    if (v2->field_4c == 1 || v2->field_4c == 5)
        *(v3) = 49;
}
```

## cmd_ispaladin `0x1002e938`

Named — see [doc 11](../../11-*.md). _39 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[76];
    char field_4c;
} struct_0;

int sub_1002e938(void)
{
    struct_0 *v2;  // eax
    unsigned short *v3;  // ecx
    unsigned short *v1;  // [bp+0xffffc]

    v2 = sub_10023861();
    v3 = v1;
    *(v3) = 48;
    if (v2->field_4c == 2 || v2->field_4c == 6)
        *(v3) = 49;
}
```

## cmd_issorcerer `0x1002e95f`

Named — see [doc 11](../../11-*.md). _39 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[76];
    char field_4c;
} struct_0;

int sub_1002e95f(void)
{
    struct_0 *v2;  // eax
    unsigned short *v3;  // ecx
    unsigned short *v1;  // [bp+0xffffc]

    v2 = sub_10023861();
    v3 = v1;
    *(v3) = 48;
    if (v2->field_4c == 3 || v2->field_4c == 7)
        *(v3) = 49;
}
```

## cmd_isdruid `0x1002e986`

Named — see [doc 11](../../11-*.md). _39 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[76];
    char field_4c;
} struct_0;

int sub_1002e986(void)
{
    struct_0 *v2;  // eax
    unsigned short *v3;  // ecx
    unsigned short *v1;  // [bp+0xffffc]

    v2 = sub_10023861();
    v3 = v1;
    *(v3) = 48;
    if (v2->field_4c == 4 || v2->field_4c == 8)
        *(v3) = 49;
}
```

## cmd_ismage `0x1002e9ad`

Named — see [doc 11](../../11-*.md). _50 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[76];
    char field_4c;
} struct_0;

int sub_1002e9ad(void)
{
    struct_0 *v2;  // eax
    unsigned short *v3;  // ecx
    char v4;  // dl
    unsigned short *v1;  // [bp+0xffffc]

    v2 = sub_10023861();
    v3 = v1;
    *(v3) = 48;
    v4 = v2->field_4c;
    if (v2->field_4c == 3 || v4 == 4 || v4 == 7 || v4 == 8)
        *(v3) = 49;
}
```

## cmd_maxhp `0x1002e9df`

Named — see [doc 11](../../11-*.md). _27 bytes. (leaf/helper — see body)_

```c
int sub_1002e9df(void)
{
    unsigned int v2;  // ecx
    int v1;  // [bp+0xffffc]

    v2 = *((short *)(sub_10023861() + 82));
    sub_10040940(v2, v1);
}
```

## cmd_hp `0x1002e9fa`

Named — see [doc 11](../../11-*.md). _27 bytes. (leaf/helper — see body)_

```c
int sub_1002e9fa(void)
{
    unsigned int v2;  // ecx
    int v1;  // [bp+0xffffc]

    v2 = *((short *)(sub_10023861() + 84));
    sub_10040940(v2, v1);
}
```

## cmd_maxmp `0x1002ea15`

Named — see [doc 11](../../11-*.md). _53 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[100];
    unsigned short field_64;
} struct_0;

extern unsigned int g_1005f551;

int sub_1002ea15(void)
{
    int *v2;  // ebx
    struct_0 *v3;  // eax
    unsigned int v4;  // ecx
    int v1;  // [bp+0xffffc]

    if (g_1005f551 && !((v3 = (struct_0 *)sub_1003b0f0(*(v2)), !v3)))
        v4 = v3->field_64;
    else
        v4 = *((short *)(sub_10023861() + 86));
    sub_10040940(v4, v1);
}
```

## cmd_mp `0x1002ea4a`

Named — see [doc 11](../../11-*.md). _59 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[98];
    unsigned short field_62;
} struct_0;

extern unsigned int g_1005f551;

int sub_1002ea4a(void)
{
    int *v2;  // ebx
    struct_0 *v3;  // eax
    unsigned int v4;  // ecx
    unsigned short v5[45];  // eax
    int v1;  // [bp+0xffffc]

    if (g_1005f551 && !((v3 = (struct_0 *)sub_1003b0f0(*(v2)), !v3)))
    {
        v4 = v3->field_62;
    }
    else
    {
        v5 = sub_10023861();
        v4 = v5[43] - v5[44];
    }
    sub_10040940(v4, v1);
}
```

## cmd_attackedme `0x1002ea85`

Named — see [doc 11](../../11-*.md). _36 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[137];
    char field_89;
} struct_0;

int sub_1002ea85(void)
{
    struct_0 *v2;  // eax
    unsigned short *v3;  // ecx
    unsigned short *v1;  // [bp+0xffffc]

    v2 = sub_10023861();
    v3 = v1;
    *(v3) = 48;
    if (v2->field_89)
        *(v3) = 49;
}
```

## cmd_exposedcount `0x1002eaa9`

Named — see [doc 11](../../11-*.md). _33 bytes. (leaf/helper — see body)_

```c
int sub_1002eaa9(void)
{
    int v2;  // eax
    unsigned short *v1;  // [bp+0xffffc]

    v2 = sub_10037fa1();
    *(v1) = 48;
    if (v2)
        sub_10040940(v2, v1);
}
```

## cmd_shotcount `0x1002eaca`

Named — see [doc 11](../../11-*.md). _33 bytes. (leaf/helper — see body)_

```c
int sub_1002eaca(void)
{
    int v2;  // eax
    unsigned short *v1;  // [bp+0xffffc]

    v2 = sub_10037f84();
    *(v1) = 48;
    if (v2)
        sub_10040940(v2, v1);
}
```

## `sub_1002f0b6` `0x1002f0b6`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1002f0b6(void)
{
}
```

## `sub_1002f0d3` `0x1002f0d3`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1002f0d3(void)
{
}
```

## `sub_1002f0f0` `0x1002f0f0`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1002f0f0(void)
{
}
```

## `sub_1002f10d` `0x1002f10d`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1002f10d(void)
{
}
```

## `sub_1002f12a` `0x1002f12a`

_5 bytes. (leaf/helper — see body)_

```c
void sub_1002f12a(void)
{
}
```

