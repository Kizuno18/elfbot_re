# elfbot.dll decompiled — jiru 0x10350ec0..0x1035330e

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10350ec0` `0x10350ec0`

_711 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_10351034[4];
extern unsigned int g_103511d0[4];
extern unsigned int g_103a4cc8;

void* sub_10350ec0(void* a0, void* a1, unsigned int a2)
{
    void* v2;  // esi
    void* v3;  // edi
    unsigned int v12;  // ecx
    unsigned int v13;  // edx
    unsigned int v14;  // ecx
    void* iter;  // esi
    void* node;  // edi
    unsigned int v6;  // ecx
    unsigned int v7;  // edx
    unsigned int v8;  // ecx
    unsigned int v9;  // ecx
    void* iter1;  // edi
    void* iter2;  // esi
    void* v0;  // [bp-0x14]
    void* v1;  // [bp-0x10]

    v2 = a1;
    v3 = a0;
    if (v3 > v2 && v3 < a2 + v2)
    {
        iter = a2 + v2 - 4;
        node = a2 + v3 - 4;
        if (!((char)node & 3))
        {
            v6 = a2 >> 2;
            v7 = a2 & 3;
        }
        else
        {
            switch (a2)
            {
            case 0:
                break;
            case 1:
                goto LABEL_103511e8;
            case 2:
                goto LABEL_103511f8;
            case 3:
                goto LABEL_1035120c;
            default:
                v8 = a2 - (node & 3);
                switch (node & 3)
                {
                case 1:
                    v7 = 3 & v8;
                    *((char *)&node[3]) = (char)iter[3];
                    iter -= 1;
                    v6 = v8 >> 2;
                    node -= 1;
                    break;
                case 2:
                    v7 = 3 & v8;
                    *((char *)&node[3]) = (char)iter[3];
                    v6 = v8 >> 2;
                    *((char *)&node[2]) = (char)iter[2];
                    iter -= 2;
                    node -= 2;
                    break;
                case 3:
                    v7 = 3 & v8;
                    *((char *)&node[3]) = (char)iter[3];
                    *((char *)&node[2]) = (char)iter[2];
                    v6 = v8 >> 2;
                    *((char *)&node[1]) = (char)iter[1];
                    iter -= 3;
                    node -= 3;
                    break;
                }
            }
        }
        switch (v6)
        {
        case 0:
            *((int *)(28 + (char *)node + 4 * v9)) = *((int *)(28 + (char *)iter + 4 * v9));
        case 1:
            *((int *)(24 + (char *)node + 4 * v9)) = *((int *)(24 + (char *)iter + 4 * v9));
            break;
        case 2:
            *((int *)(20 + (char *)node + 4 * v9)) = *((int *)(20 + (char *)iter + 4 * v9));
            goto LABEL_1035119c;
        case 3:
LABEL_1035119c:
            *((int *)(16 + (char *)node + 4 * v9)) = *((int *)(16 + (char *)iter + 4 * v9));
            goto LABEL_103511a4;
        case 4:
LABEL_103511a4:
            *((int *)(12 + (char *)node + 4 * v9)) = *((int *)(12 + (char *)iter + 4 * v9));
            goto LABEL_103511ac;
        case 5:
LABEL_103511ac:
            *((int *)(8 + (char *)node + 4 * v9)) = *((int *)(8 + (char *)iter + 4 * v9));
            goto LABEL_103511b4;
        case 6:
LABEL_103511b4:
            *((int *)(4 + (char *)node + 4 * v9)) = *((int *)(4 + (char *)iter + 4 * v9));
            goto LABEL_103511c7;
        case 7:
LABEL_103511c7:
            goto g_103511d0[v7];
        default:
            for (; v6; iter += 0xfffffffc)
            {
                v6 -= 1;
                *((int *)node) = *((int *)iter);
                node += 0xfffffffc;
            }
            switch (v7)
            {
            case 0:
                return a0;
            case 1:
LABEL_103511e8:
                *((char *)&node[3]) = (char)iter[3];
                return a0;
            case 2:
LABEL_103511f8:
                *((char *)&node[3]) = (char)iter[3];
                *((char *)&node[2]) = (char)iter[2];
                return a0;
            case 3:
LABEL_1035120c:
                *((char *)&node[3]) = (char)iter[3];
                *((char *)&node[2]) = (char)iter[2];
                *((char *)&node[1]) = (char)iter[1];
                return a0;
            }
        }
    }
    iter1 = v3;
    iter2 = v2;
    if (a2 >= 0x100)
    {
        iter1 = v3;
        iter2 = v2;
        if (g_103a4cc8)
        {
            v1 = v3;
            v0 = v2;
            iter1 = v1;
            iter2 = v0;
            if ((v3 & 15) == (v2 & 15))
                return sub_103588c2();
        }
    }
    if (!((char)iter1 & 3))
    {
        v12 = a2 >> 2;
        v13 = a2 & 3;
    }
    else
    {
        switch (a2)
        {
        case 0:
            return a0;
        case 1:
            *((char *)iter1) = *((char *)iter2);
            return a0;
        case 2:
            *((char *)iter1) = *((char *)iter2);
            *((char *)&iter1[1]) = (char)iter2[1];
            return a0;
        case 3:
            *((char *)iter1) = *((char *)iter2);
            *((char *)&iter1[1]) = (char)iter2[1];
            *((char *)&iter1[2]) = (char)iter2[2];
            return a0;
        default:
            v14 = a2 - 4 + (iter1 & 3);
            switch (iter1 & 3)
            {
            case 0:
                break;
            case 1:
                v13 = 3 & v14;
                *((char *)iter1) = *((char *)iter2);
                *((char *)&iter1[1]) = (char)iter2[1];
                v12 = v14 >> 2;
                *((char *)&iter1[2]) = (char)iter2[2];
                iter2 += 3;
                iter1 += 3;
                break;
            case 2:
                v13 = 3 & v14;
                *((char *)iter1) = *((char *)iter2);
                v12 = v14 >> 2;
                *((char *)&iter1[1]) = (char)iter2[1];
                iter2 += 2;
                iter1 += 2;
                break;
            case 3:
                v13 = 3 & v14;
                *((char *)iter1) = *((char *)iter2);
                iter2 += 1;
                v12 = v14 >> 2;
                iter1 += 1;
                break;
            }
        }
    }
    switch (v12)
    {
    case 7:
        *((int *)(-28 + (char *)iter1 + 4 * v12)) = *((int *)(-28 + (char *)iter2 + 4 * v12));
    case 6:
        *((int *)(-24 + (char *)iter1 + 4 * v12)) = *((int *)(-24 + (char *)iter2 + 4 * v12));
        break;
    case 5:
        *((int *)(-20 + (char *)iter1 + 4 * v12)) = *((int *)(-20 + (char *)iter2 + 4 * v12));
        goto LABEL_10351000;
    case 4:
LABEL_10351000:
        *((int *)(-0x10 + (char *)iter1 + 4 * v12)) = *((int *)(-0x10 + (char *)iter2 + 4 * v12));
        goto LABEL_10351008;
    case 3:
LABEL_10351008:
        *((int *)(-12 + (char *)iter1 + 4 * v12)) = *((int *)(-12 + (char *)iter2 + 4 * v12));
        goto LABEL_10351010;
    case 2:
LABEL_10351010:
        *((int *)(-0x8 + (char *)iter1 + 4 * v12)) = *((int *)(-0x8 + (char *)iter2 + 4 * v12));
        goto LABEL_10351018;
    case 1:
LABEL_10351018:
        *((int *)(-0x4 + (char *)iter1 + 4 * v12)) = *((int *)(-0x4 + (char *)iter2 + 4 * v12));
        goto LABEL_1035102b;
    case 0:
LABEL_1035102b:
        goto g_10351034[v13];
    default:
        for (; v12; iter2 += 4)
        {
            v12 -= 1;
            *((int *)iter1) = *((int *)iter2);
            iter1 += 4;
        }
        goto g_10351034[v13];
    }
}
```

## `sub_10350f23` `0x10350f23`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10350f23(void)
{
}
```

## `sub_10350f43` `0x10350f43`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10350f43(void)
{
}
```

## `sub_10350f81` `0x10350f81`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10350f81(void)
{
}
```

## `sub_10350fa7` `0x10350fa7`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10350fa7(void)
{
}
```

## `sub_1035104b` `0x1035104b`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1035104b(void)
{
}
```

## `sub_10351057` `0x10351057`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10351057(void)
{
}
```

## `sub_10351069` `0x10351069`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10351069(void)
{
}
```

## `sub_10351083` `0x10351083`

_1 bytes. (leaf/helper — see body)_

```c
void sub_10351083(void)
{
}
```

## `sub_103510aa` `0x103510aa`

_2 bytes. (leaf/helper — see body)_

```c
void sub_103510aa(void)
{
}
```

## `sub_103510b5` `0x103510b5`

_3 bytes. (leaf/helper — see body)_

```c
void sub_103510b5(void)
{
}
```

## `sub_10351105` `0x10351105`

_3 bytes. (leaf/helper — see body)_

```c
void sub_10351105(void)
{
}
```

## `sub_1035112f` `0x1035112f`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1035112f(void)
{
}
```

## `sub_103511e7` `0x103511e7`

_1 bytes. (leaf/helper — see body)_

```c
void sub_103511e7(void)
{
}
```

## `sub_103511f5` `0x103511f5`

_3 bytes. (leaf/helper — see body)_

```c
void sub_103511f5(void)
{
}
```

## `sub_1035120b` `0x1035120b`

_1 bytes. (leaf/helper — see body)_

```c
void sub_1035120b(void)
{
}
```

## `sub_10351225` `0x10351225`

_275 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
} struct_0;

extern struct_0 *g_1038b0fc;
extern struct_0 *g_1038b208;
extern struct_0 *g_1038b20c;
extern struct_0 *g_1038b210;
extern struct_0 *g_1038b214;
extern char g_1038e180;
extern unsigned int g_1038e184;
extern char g_103950a8;
extern unsigned int g_103a3068;
extern unsigned int g_103a306c;
extern unsigned int g_103a3074;
extern unsigned int g_103a30b8;
extern unsigned int g_103a30c0;
extern unsigned short g_103a314c;
extern unsigned short g_103a3150;
extern unsigned short g_103a3154;
extern unsigned short g_103a3158;
extern unsigned int g_103a315c;
extern unsigned int g_103a3160;
extern unsigned int g_103a3164;
extern unsigned int g_103a3168;
extern unsigned int g_103a316c;
extern unsigned int g_103a3170;
extern char g_103a3174;
extern unsigned int g_103a3178;
extern unsigned short g_103a317c;
extern unsigned int g_103a3180;
extern unsigned int g_103a3184;
extern unsigned short g_103a3188;

int sub_10351225(void)
{
    unsigned int v4;  // ecx
    unsigned int v5;  // eax
    unsigned short v14;  // fs
    unsigned short v15;  // gs
    unsigned int v16;  // 4162
    unsigned int v17;  // id
    unsigned int v18;  // ac
    unsigned int v19;  // eax
    unsigned int v20;  // eax
    unsigned int v6;  // edx
    unsigned int v7;  // ebx
    unsigned int v8;  // esi
    unsigned int v9;  // edi
    unsigned short v10;  // ss
    unsigned short v11;  // cs
    unsigned short v12;  // ds
    unsigned short v13;  // es
    unsigned int v0;  // [bp-0x330]
    char v1;  // [bp-0x32c]
    unsigned int v2;  // [bp+0x0]
    unsigned int v3;  // [bp+0x4]

    if (v4 == *((int *)&g_1038e180))
        return;
    g_103a3170 = v5;
    g_103a316c = v4;
    g_103a3168 = v6;
    g_103a3164 = v7;
    g_103a3160 = v8;
    g_103a315c = v9;
    g_103a3188 = v10;
    g_103a317c = v11;
    g_103a3158 = v12;
    g_103a3154 = v13;
    g_103a3150 = v14;
    g_103a314c = v15;
    v16 = _ccall(6, &v1, 808, 0);
    v0 = v16 | 0x202 | v17 * 0x200000 & 0x200000 | v18 * 0x40000 & 0x40000;
    g_103a3180 = v16 | 0x202 | v17 * 0x200000 & 0x200000 | v18 * 0x40000 & 0x40000;
    *((int *)&g_103a3174) = /* unsupported instruction */;
    g_103a3178 = v2;
    g_103a3184 = &v3;
    g_103a30c0 = 65537;
    g_103a3074 = g_103a3178;
    g_103a3068 = 3221226505;
    g_103a306c = 1;
    g_103a30b8 = g_1038b214(*((int *)&g_1038e180), g_1038e184);
    sub_1035b125(1);
    g_1038b210(0);
    g_1038b20c(&g_103950a8);
    if (!g_103a30b8)
    {
        sub_1035b125(1);
        v19 = g_1038b0fc(3221226505);
        g_1038b208(v19);
    }
    else
    {
        v20 = g_1038b0fc(3221226505);
        g_1038b208(v20);
    }
    return;
}
```

## `sub_10351234` `0x10351234`

_5630 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10351234(void* iter, void* node, unsigned int a2)
{
    unsigned int i;  // edi
    unsigned int v3;  // eax
    unsigned int v12;  // esi
    unsigned int v102;  // esi
    unsigned int v103;  // ebx
    unsigned int v104;  // 4110
    void* v105;  // eax
    void* v106;  // ecx
    unsigned int v107;  // esi
    unsigned int v108;  // edx
    unsigned int v109;  // 4127
    unsigned int v110;  // esi
    unsigned int v111;  // edx
    unsigned int v13;  // ebx
    unsigned int v112;  // 4127
    unsigned int v113;  // esi
    unsigned int v114;  // edx
    unsigned int v115;  // 4127
    unsigned int v116;  // esi
    unsigned int v117;  // edx
    unsigned int v118;  // 4110
    unsigned int v119;  // esi
    unsigned int v120;  // edx
    unsigned int v121;  // 4127
    unsigned int v14;  // 4127
    unsigned int v122;  // esi
    unsigned int v123;  // edx
    unsigned int v124;  // 4127
    unsigned int v125;  // esi
    unsigned int v126;  // edx
    unsigned int v127;  // 4127
    unsigned int v128;  // esi
    unsigned int v129;  // edx
    unsigned int v130;  // 4110
    unsigned int v131;  // esi
    unsigned int v15;  // esi
    unsigned int v132;  // edx
    unsigned int v133;  // 4127
    unsigned int v134;  // esi
    unsigned int v135;  // edx
    unsigned int v136;  // 4127
    unsigned int v137;  // esi
    unsigned int v138;  // edx
    unsigned int v139;  // 4127
    unsigned int v140;  // esi
    unsigned int v141;  // edx
    unsigned int v16;  // ebx
    unsigned int v142;  // 4110
    unsigned int v143;  // esi
    unsigned int v144;  // edx
    unsigned int v145;  // 4127
    unsigned int v146;  // esi
    unsigned int v147;  // edx
    unsigned int v148;  // 4127
    unsigned int v149;  // esi
    unsigned int v150;  // edx
    unsigned int v151;  // 4127
    unsigned int v17;  // 4127
    unsigned int v152;  // esi
    unsigned int v153;  // edx
    unsigned int v154;  // 4110
    unsigned int v155;  // edx
    unsigned int v156;  // esi
    unsigned int v157;  // 4127
    unsigned int v158;  // esi
    unsigned int v159;  // edx
    unsigned int v160;  // 4127
    unsigned int v161;  // esi
    unsigned int v18;  // esi
    unsigned int v162;  // edx
    unsigned int v163;  // 4127
    unsigned int v164;  // esi
    unsigned int v165;  // edx
    unsigned int v166;  // 4110
    unsigned int v167;  // esi
    unsigned int v168;  // edx
    unsigned int v169;  // 4127
    unsigned int v170;  // esi
    unsigned int v171;  // edx
    unsigned int v19;  // ebx
    unsigned int v172;  // 4127
    unsigned int v173;  // esi
    unsigned int v174;  // edx
    unsigned int v175;  // 4127
    unsigned int v176;  // esi
    unsigned int v177;  // edx
    unsigned int v178;  // 4110
    unsigned int v179;  // esi
    unsigned int v180;  // edx
    unsigned int v181;  // 4126
    unsigned int v20;  // 4110
    unsigned int v182;  // esi
    unsigned int v183;  // edx
    unsigned int v184;  // 4126
    unsigned int v185;  // esi
    unsigned int v186;  // edx
    unsigned int v187;  // 4126
    unsigned int v188;  // eax
    unsigned int v189;  // ecx
    unsigned int v190;  // 4110
    unsigned int v191;  // esi
    unsigned int v21;  // esi
    unsigned int v192;  // edx
    unsigned int v193;  // 4127
    unsigned int v194;  // esi
    unsigned int v195;  // edx
    unsigned int v196;  // 4127
    unsigned int v197;  // esi
    unsigned int v198;  // edx
    unsigned int v199;  // 4127
    unsigned int v200;  // esi
    unsigned int v201;  // edx
    unsigned int v4;  // eax
    unsigned int v22;  // ebx
    unsigned int v202;  // 4110
    unsigned int v203;  // esi
    unsigned int v204;  // edx
    unsigned int v205;  // 4127
    unsigned int v206;  // esi
    unsigned int v207;  // edx
    unsigned int v208;  // 4127
    unsigned int v209;  // esi
    unsigned int v210;  // edx
    unsigned int v211;  // 4127
    unsigned int v23;  // 4127
    unsigned int v212;  // esi
    unsigned int v213;  // edx
    unsigned int v214;  // 4110
    unsigned int v215;  // esi
    unsigned int v216;  // edx
    unsigned int v217;  // 4127
    unsigned int v218;  // esi
    unsigned int v219;  // edx
    unsigned int v220;  // 4127
    unsigned int v221;  // esi
    unsigned int v24;  // esi
    unsigned int v222;  // edx
    unsigned int v223;  // 4127
    unsigned int v224;  // esi
    unsigned int v225;  // edx
    unsigned int v226;  // 4110
    unsigned int v227;  // esi
    unsigned int v228;  // edx
    unsigned int v229;  // 4127
    unsigned int v230;  // esi
    unsigned int v231;  // edx
    unsigned int v25;  // ebx
    unsigned int v232;  // 4127
    unsigned int v233;  // esi
    unsigned int v234;  // edx
    unsigned int v235;  // 4127
    unsigned int v236;  // esi
    unsigned int v237;  // edx
    unsigned int v238;  // 4110
    unsigned int v239;  // esi
    unsigned int v240;  // edx
    unsigned int v241;  // 4127
    unsigned int v26;  // 4127
    unsigned int v242;  // esi
    unsigned int v243;  // edx
    unsigned int v244;  // 4127
    unsigned int v245;  // esi
    unsigned int v246;  // edx
    unsigned int v247;  // 4127
    unsigned int v248;  // esi
    unsigned int v249;  // edx
    unsigned int v250;  // 4110
    unsigned int v251;  // edx
    unsigned int v27;  // esi
    unsigned int v252;  // esi
    unsigned int v253;  // 4127
    unsigned int v254;  // esi
    unsigned int v255;  // edx
    unsigned int v256;  // 4127
    unsigned int v257;  // esi
    unsigned int v258;  // edx
    unsigned int v259;  // 4127
    unsigned int v260;  // esi
    unsigned int v261;  // edx
    unsigned int v28;  // ebx
    unsigned int v262;  // 4110
    unsigned int v263;  // esi
    unsigned int v264;  // edx
    unsigned int v265;  // 4127
    unsigned int v266;  // esi
    unsigned int v267;  // edx
    unsigned int v268;  // 4127
    unsigned int v269;  // esi
    unsigned int v270;  // edx
    unsigned int v271;  // 4127
    unsigned int v29;  // 4127
    unsigned int v272;  // esi
    unsigned int v273;  // edx
    unsigned int v274;  // 4110
    unsigned int v275;  // esi
    unsigned int v276;  // edx
    unsigned int v277;  // 4127
    unsigned int v278;  // esi
    unsigned int v279;  // edx
    unsigned int v280;  // 4127
    unsigned int v281;  // esi
    unsigned int v30;  // esi
    unsigned int v282;  // edx
    unsigned int v283;  // 4127
    unsigned int v284;  // esi
    unsigned int v285;  // edx
    unsigned int v286;  // 4110
    unsigned int v287;  // esi
    unsigned int v288;  // edx
    unsigned int v289;  // 4127
    unsigned int v290;  // esi
    unsigned int v291;  // edx
    unsigned int v31;  // ebx
    unsigned int v292;  // 4127
    unsigned int v293;  // esi
    unsigned int v294;  // edx
    unsigned int v295;  // 4127
    unsigned int v296;  // esi
    unsigned int v297;  // edx
    unsigned int v298;  // 4110
    unsigned int v299;  // esi
    unsigned int v300;  // edx
    unsigned int v301;  // 4127
    unsigned int v5;  // eax
    unsigned int v32;  // 4110
    unsigned int v302;  // esi
    unsigned int v303;  // edx
    unsigned int v304;  // 4127
    unsigned int v305;  // esi
    unsigned int v306;  // edx
    unsigned int v307;  // 4127
    unsigned int v308;  // esi
    unsigned int v309;  // edx
    unsigned int v310;  // 4110
    unsigned int v311;  // esi
    unsigned int v33;  // esi
    unsigned int v312;  // edx
    unsigned int v313;  // 4127
    unsigned int v314;  // esi
    unsigned int v315;  // edx
    unsigned int v316;  // 4127
    unsigned int v317;  // esi
    unsigned int v318;  // edx
    unsigned int v319;  // 4127
    unsigned int v320;  // esi
    unsigned int v321;  // edx
    unsigned int v34;  // ebx
    unsigned int v322;  // 4110
    unsigned int v323;  // esi
    unsigned int v324;  // edx
    unsigned int v325;  // 4127
    unsigned int v326;  // esi
    unsigned int v327;  // edx
    unsigned int v328;  // 4127
    unsigned int v329;  // esi
    unsigned int v330;  // edx
    unsigned int v331;  // 4127
    unsigned int v35;  // 4127
    unsigned int v332;  // esi
    unsigned int v333;  // edx
    unsigned int v334;  // 4110
    unsigned int v335;  // edx
    unsigned int v336;  // esi
    unsigned int v337;  // 4127
    unsigned int v338;  // edx
    unsigned int v339;  // esi
    unsigned int v340;  // 4127
    unsigned int v341;  // edx
    unsigned int v36;  // esi
    unsigned int v342;  // esi
    unsigned int v343;  // 4127
    unsigned int v344;  // edx
    unsigned int v345;  // esi
    unsigned int v346;  // 4110
    unsigned int v347;  // esi
    unsigned int v348;  // edx
    unsigned int v349;  // 4127
    unsigned int v350;  // esi
    unsigned int v351;  // edx
    unsigned int v37;  // ebx
    unsigned int v352;  // 4127
    unsigned int v353;  // esi
    unsigned int v354;  // edx
    unsigned int v355;  // 4127
    unsigned int v356;  // esi
    unsigned int v357;  // edx
    unsigned int v358;  // 4110
    unsigned int v359;  // edx
    unsigned int v360;  // esi
    unsigned int v361;  // 4127
    unsigned int v38;  // 4127
    unsigned int v362;  // esi
    unsigned int v363;  // edx
    unsigned int v364;  // 4127
    unsigned int v365;  // esi
    unsigned int v366;  // edx
    unsigned int v367;  // 4127
    unsigned int v368;  // esi
    unsigned int v369;  // edx
    unsigned int v370;  // 4110
    unsigned int v371;  // esi
    unsigned int v39;  // esi
    unsigned int v372;  // edx
    unsigned int v373;  // 4127
    unsigned int v374;  // esi
    unsigned int v375;  // edx
    unsigned int v376;  // 4127
    unsigned int v377;  // esi
    unsigned int v378;  // edx
    unsigned int v379;  // 4127
    unsigned int v380;  // esi
    unsigned int v381;  // edx
    unsigned int v40;  // ebx
    unsigned int v382;  // 4110
    unsigned int v383;  // esi
    unsigned int v384;  // edx
    unsigned int v385;  // 4127
    unsigned int v386;  // esi
    unsigned int v387;  // edx
    unsigned int v388;  // 4127
    unsigned int v389;  // esi
    unsigned int v390;  // edx
    unsigned int v391;  // 4127
    unsigned int v41;  // 4127
    unsigned int v392;  // esi
    unsigned int v393;  // edx
    unsigned int v394;  // 4110
    unsigned int v395;  // esi
    unsigned int v396;  // edx
    unsigned int v397;  // 4127
    unsigned int v398;  // esi
    unsigned int v399;  // edx
    unsigned int v400;  // 4127
    unsigned int v401;  // esi
    unsigned int v6;  // ebx
    unsigned int v42;  // esi
    unsigned int v402;  // edx
    unsigned int v403;  // 4127
    unsigned int v404;  // esi
    unsigned int v405;  // edx
    unsigned int v406;  // 4110
    unsigned int v407;  // edx
    unsigned int v408;  // esi
    unsigned int v409;  // 4127
    unsigned int v410;  // esi
    unsigned int v411;  // edx
    unsigned int v43;  // ebx
    unsigned int v412;  // 4127
    unsigned int v413;  // esi
    unsigned int v414;  // edx
    unsigned int v415;  // 4127
    unsigned int v416;  // esi
    unsigned int v417;  // edx
    unsigned int v418;  // 4110
    unsigned int v419;  // esi
    unsigned int v420;  // edx
    unsigned int v421;  // 4127
    unsigned int v44;  // 4110
    unsigned int v422;  // esi
    unsigned int v423;  // edx
    unsigned int v424;  // 4127
    unsigned int v425;  // esi
    unsigned int v426;  // edx
    unsigned int v427;  // 4127
    unsigned int v428;  // esi
    unsigned int v429;  // edx
    unsigned int v430;  // 4110
    unsigned int v431;  // esi
    unsigned int v45;  // esi
    unsigned int v432;  // edx
    unsigned int v433;  // 4127
    unsigned int v434;  // esi
    unsigned int v435;  // edx
    unsigned int v436;  // 4127
    unsigned int v437;  // esi
    unsigned int v438;  // edx
    unsigned int v439;  // 4127
    unsigned int v440;  // esi
    unsigned int v441;  // edx
    unsigned int v46;  // ebx
    unsigned int v442;  // 4110
    unsigned int v443;  // esi
    unsigned int v444;  // edx
    unsigned int v445;  // 4126
    unsigned int v446;  // edx
    unsigned int v447;  // esi
    unsigned int v448;  // 4126
    unsigned int v449;  // ecx
    unsigned int v450;  // eax
    unsigned int v451;  // 4110
    unsigned int v47;  // 4127
    void* v452;  // ecx
    void* v453;  // esi
    unsigned int v454;  // eax
    unsigned int v455;  // edx
    unsigned int v456;  // 4127
    unsigned int v457;  // eax
    unsigned int v458;  // edx
    unsigned int v459;  // 4127
    unsigned int v460;  // eax
    unsigned int v461;  // edx
    unsigned int v48;  // esi
    unsigned int v462;  // 4127
    unsigned int v463;  // eax
    unsigned int v464;  // ecx
    void* v465;  // ecx
    void* v466;  // esi
    unsigned int v467;  // eax
    unsigned int v468;  // edx
    unsigned int v469;  // 4127
    unsigned int v470;  // eax
    unsigned int v471;  // edx
    unsigned int v49;  // ebx
    unsigned int v472;  // 4127
    void* v473;  // esi
    unsigned int v474;  // eax
    unsigned int v475;  // edx
    unsigned int v476;  // 4127
    unsigned int v50;  // 4127
    unsigned int v51;  // esi
    unsigned int v7;  // edx
    unsigned int v52;  // ebx
    unsigned int v53;  // 4127
    unsigned int v54;  // esi
    unsigned int v55;  // ebx
    unsigned int v56;  // 4110
    unsigned int v57;  // ebx
    unsigned int v58;  // esi
    unsigned int v59;  // 4127
    unsigned int v60;  // esi
    unsigned int v61;  // ebx
    unsigned int v8;  // esi
    unsigned int v62;  // 4127
    unsigned int v63;  // esi
    unsigned int v64;  // ebx
    unsigned int v65;  // 4127
    unsigned int v66;  // esi
    unsigned int v67;  // ebx
    unsigned int v68;  // 4110
    unsigned int v69;  // esi
    unsigned int v70;  // ebx
    unsigned int v71;  // 4127
    unsigned int v9;  // ebx
    unsigned int v72;  // esi
    unsigned int v73;  // ebx
    unsigned int v74;  // 4127
    unsigned int v75;  // esi
    unsigned int v76;  // ebx
    unsigned int v77;  // 4127
    unsigned int v78;  // esi
    unsigned int v79;  // ebx
    unsigned int v80;  // 4110
    unsigned int v81;  // esi
    unsigned int v10;  // 4127
    unsigned int v82;  // ebx
    unsigned int v83;  // 4127
    unsigned int v84;  // esi
    unsigned int v85;  // ebx
    unsigned int v86;  // 4127
    unsigned int v87;  // esi
    unsigned int v88;  // ebx
    unsigned int v89;  // 4127
    unsigned int v90;  // esi
    unsigned int v91;  // ebx
    unsigned int v11;  // esi
    unsigned int v92;  // 4110
    unsigned int v93;  // esi
    unsigned int v94;  // ebx
    unsigned int v95;  // 4127
    unsigned int v96;  // esi
    unsigned int v97;  // ebx
    unsigned int v98;  // 4127
    unsigned int v99;  // esi
    unsigned int v100;  // ebx
    unsigned int v101;  // 4127
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]

    v3 = a2;
    if (!v3)
        return 0;
    v4 = v3 - 1;
    if (v3 != 1)
    {
        v5 = v4 - 1;
        if (v4 == 1)
        {
            v473 = node;
            v474 = *((char *)iter);
            v475 = *((char *)v473);
            if (v474 != v475)
            {
                v476 = _ccall(15, 15, v474 - v475, 0, 0);
                if ((v476 & 1) * 2 != 1)
                    return (v476 & 1) * 2 - 1;
            }
            v463 = (char)iter[1];
            v464 = (char)v473[1];
        }
        else if (v5 != 1)
        {
            if (v5 != 2)
            {
                v1 = v6;
                v0 = 32;
                for (v7 = v0; i >= v7; i -= v7)
                {
                    if (*((int *)iter) != *((int *)node))
                    {
                        v8 = *((char *)iter);
                        v9 = *((char *)node);
                        if (v8 != v9 && !((v10 = (unsigned int)_ccall(15, 15, v8 - v9, 0, 0), v11 = (v10 & 1) * 2 - 1, (v10 & 1) * 2 == 1)) || (v12 = (unsigned int)(char)(char)iter[1], v13 = (unsigned int)(char)(char)node[1], v12 != v13 && !((v14 = (unsigned int)_ccall(15, 15, v12 - v13, 0, 0), v11 = (v14 & 1) * 2 - 1, (v14 & 1) * 2 == 1)) || (v15 = (unsigned int)(char)(char)iter[2], v16 = (unsigned int)(char)(char)node[2], v15 != v16 && !((v17 = (unsigned int)_ccall(15, 15, v15 - v16, 0, 0), v11 = (v17 & 1) * 2 - 1, (v17 & 1) * 2 == 1)))))
                            goto LABEL_10351700;
                        v18 = (char)iter[3];
                        v19 = (char)node[3];
                        v11 = v18 - v19;
                        if (v18 != v19)
                        {
                            v20 = _ccall(15, 15, v11, 0, 0);
                            v11 = (v20 & 1) * 2 - 1;
                        }
                    }
                    else
                    {
                        v11 = 0;
                    }
                    if (v11)
                        goto LABEL_10351700;
                    if ((int)iter[4] != (int)node[4])
                    {
                        v21 = (char)iter[4];
                        v22 = (char)node[4];
                        if (v21 != v22 && !((v23 = (unsigned int)_ccall(15, 15, v21 - v22, 0, 0), v11 = (v23 & 1) * 2 - 1, (v23 & 1) * 2 == 1)) || (v24 = (unsigned int)(char)(char)iter[5], v25 = (unsigned int)(char)(char)node[5], v24 != v25 && !((v26 = (unsigned int)_ccall(15, 15, v24 - v25, 0, 0), v11 = (v26 & 1) * 2 - 1, (v26 & 1) * 2 == 1)) || (v27 = (unsigned int)(char)(char)iter[6], v28 = (unsigned int)(char)(char)node[6], v27 != v28 && !((v29 = (unsigned int)_ccall(15, 15, v27 - v28, 0, 0), v11 = (v29 & 1) * 2 - 1, (v29 & 1) * 2 == 1)))))
                            goto LABEL_10351700;
                        v30 = (char)iter[7];
                        v31 = (char)node[7];
                        v11 = v30 - v31;
                        if (v30 != v31)
                        {
                            v32 = _ccall(15, 15, v11, 0, 0);
                            v11 = (v32 & 1) * 2 - 1;
                        }
                    }
                    else
                    {
                        v11 = 0;
                    }
                    if (v11)
                        goto LABEL_10351700;
                    if ((int)iter[8] != (int)node[8])
                    {
                        v33 = (char)iter[8];
                        v34 = (char)node[8];
                        if (v33 != v34 && !((v35 = (unsigned int)_ccall(15, 15, v33 - v34, 0, 0), v11 = (v35 & 1) * 2 - 1, (v35 & 1) * 2 == 1)) || (v36 = (unsigned int)(char)(char)iter[9], v37 = (unsigned int)(char)(char)node[9], v36 != v37 && !((v38 = (unsigned int)_ccall(15, 15, v36 - v37, 0, 0), v11 = (v38 & 1) * 2 - 1, (v38 & 1) * 2 == 1)) || (v39 = (unsigned int)(char)(char)iter[10], v40 = (unsigned int)(char)(char)node[10], v39 != v40 && !((v41 = (unsigned int)_ccall(15, 15, v39 - v40, 0, 0), v11 = (v41 & 1) * 2 - 1, (v41 & 1) * 2 == 1)))))
                            goto LABEL_10351700;
                        v42 = (char)iter[11];
                        v43 = (char)node[11];
                        v11 = v42 - v43;
                        if (v42 != v43)
                        {
                            v44 = _ccall(15, 15, v11, 0, 0);
                            v11 = (v44 & 1) * 2 - 1;
                        }
                    }
                    else
                    {
                        v11 = 0;
                    }
                    if (v11)
                        goto LABEL_10351700;
                    if ((int)iter[12] != (int)node[12])
                    {
                        v45 = (char)iter[12];
                        v46 = (char)node[12];
                        if (v45 != v46 && !((v47 = (unsigned int)_ccall(15, 15, v45 - v46, 0, 0), v11 = (v47 & 1) * 2 - 1, (v47 & 1) * 2 == 1)) || (v48 = (unsigned int)(char)(char)iter[13], v49 = (unsigned int)(char)(char)node[13], v48 != v49 && !((v50 = (unsigned int)_ccall(15, 15, v48 - v49, 0, 0), v11 = (v50 & 1) * 2 - 1, (v50 & 1) * 2 == 1)) || (v51 = (unsigned int)(char)(char)iter[14], v52 = (unsigned int)(char)(char)node[14], v51 != v52 && !((v53 = (unsigned int)_ccall(15, 15, v51 - v52, 0, 0), v11 = (v53 & 1) * 2 - 1, (v53 & 1) * 2 == 1)))))
                            goto LABEL_10351700;
                        v54 = (char)iter[15];
                        v55 = (char)node[15];
                        v11 = v54 - v55;
                        if (v54 != v55)
                        {
                            v56 = _ccall(15, 15, v11, 0, 0);
                            v11 = (v56 & 1) * 2 - 1;
                        }
                    }
                    else
                    {
                        v11 = 0;
                    }
                    if (v11)
                        goto LABEL_10351700;
                    if ((int)iter[16] != (int)node[16])
                    {
                        v57 = (char)node[16];
                        v58 = (char)iter[16];
                        if (v58 != v57 && !((v59 = (unsigned int)_ccall(15, 15, v58 - v57, 0, 0), v11 = (v59 & 1) * 2 - 1, (v59 & 1) * 2 == 1)) || (v60 = (unsigned int)(char)(char)iter[0x11], v61 = (unsigned int)(char)(char)node[0x11], v60 != v61 && !((v62 = (unsigned int)_ccall(15, 15, v60 - v61, 0, 0), v11 = (v62 & 1) * 2 - 1, (v62 & 1) * 2 == 1)) || (v63 = (unsigned int)(char)(char)iter[18], v64 = (unsigned int)(char)(char)node[18], v63 != v64 && !((v65 = (unsigned int)_ccall(15, 15, v63 - v64, 0, 0), v11 = (v65 & 1) * 2 - 1, (v65 & 1) * 2 == 1)))))
                            goto LABEL_10351700;
                        v66 = (char)iter[19];
                        v67 = (char)node[19];
                        v11 = v66 - v67;
                        if (v66 != v67)
                        {
                            v68 = _ccall(15, 15, v11, 0, 0);
                            v11 = (v68 & 1) * 2 - 1;
                        }
                    }
                    else
                    {
                        v11 = 0;
                    }
                    if (v11)
                        goto LABEL_10351700;
                    if ((int)iter[20] != (int)node[20])
                    {
                        v69 = (char)iter[20];
                        v70 = (char)node[20];
                        if (v69 != v70 && !((v71 = (unsigned int)_ccall(15, 15, v69 - v70, 0, 0), v11 = (v71 & 1) * 2 - 1, (v71 & 1) * 2 == 1)) || (v72 = (unsigned int)(char)(char)iter[21], v73 = (unsigned int)(char)(char)node[21], v72 != v73 && !((v74 = (unsigned int)_ccall(15, 15, v72 - v73, 0, 0), v11 = (v74 & 1) * 2 - 1, (v74 & 1) * 2 == 1)) || (v75 = (unsigned int)(char)(char)iter[22], v76 = (unsigned int)(char)(char)node[22], v75 != v76 && !((v77 = (unsigned int)_ccall(15, 15, v75 - v76, 0, 0), v11 = (v77 & 1) * 2 - 1, (v77 & 1) * 2 == 1)))))
                            goto LABEL_10351700;
                        v78 = (char)iter[23];
                        v79 = (char)node[23];
                        v11 = v78 - v79;
                        if (v78 != v79)
                        {
                            v80 = _ccall(15, 15, v11, 0, 0);
                            v11 = (v80 & 1) * 2 - 1;
                        }
                    }
                    else
                    {
                        v11 = 0;
                    }
                    if (v11)
                        goto LABEL_10351700;
                    if ((int)iter[24] != (int)node[24])
                    {
                        v81 = (char)iter[24];
                        v82 = (char)node[24];
                        if (v81 != v82 && !((v83 = (unsigned int)_ccall(15, 15, v81 - v82, 0, 0), v11 = (v83 & 1) * 2 - 1, (v83 & 1) * 2 == 1)) || (v84 = (unsigned int)(char)(char)iter[25], v85 = (unsigned int)(char)(char)node[25], v84 != v85 && !((v86 = (unsigned int)_ccall(15, 15, v84 - v85, 0, 0), v11 = (v86 & 1) * 2 - 1, (v86 & 1) * 2 == 1)) || (v87 = (unsigned int)(char)(char)iter[26], v88 = (unsigned int)(char)(char)node[26], v87 != v88 && !((v89 = (unsigned int)_ccall(15, 15, v87 - v88, 0, 0), v11 = (v89 & 1) * 2 - 1, (v89 & 1) * 2 == 1)))))
                            goto LABEL_10351700;
                        v90 = (char)iter[27];
                        v91 = (char)node[27];
                        v11 = v90 - v91;
                        if (v90 != v91)
                        {
                            v92 = _ccall(15, 15, v11, 0, 0);
                            v11 = (v92 & 1) * 2 - 1;
                        }
                    }
                    else
                    {
                        v11 = 0;
                    }
                    if (v11)
                        goto LABEL_10351700;
                    if ((int)iter[28] != (int)node[28])
                    {
                        v93 = (char)iter[28];
                        v94 = (char)node[28];
                        if (v93 != v94 && !((v95 = (unsigned int)_ccall(15, 15, v93 - v94, 0, 0), v11 = (v95 & 1) * 2 - 1, (v95 & 1) * 2 == 1)) || (v96 = (unsigned int)(char)(char)iter[29], v97 = (unsigned int)(char)(char)node[29], v96 != v97 && !((v98 = (unsigned int)_ccall(15, 15, v96 - v97, 0, 0), v11 = (v98 & 1) * 2 - 1, (v98 & 1) * 2 == 1)) || (v99 = (unsigned int)(char)(char)iter[30], v100 = (unsigned int)(char)(char)node[30], v99 != v100 && !((v101 = (unsigned int)_ccall(15, 15, v99 - v100, 0, 0), v11 = (v101 & 1) * 2 - 1, (v101 & 1) * 2 == 1)))))
                            goto LABEL_10351700;
                        v102 = (char)iter[31];
                        v103 = (char)node[31];
                        v11 = v102 - v103;
                        if (v102 != v103)
                        {
                            v104 = _ccall(15, 15, v11, 0, 0);
                            v11 = (v104 & 1) * 2 - 1;
                        }
                    }
                    else
                    {
                        v11 = 0;
                    }
                    if (v11)
                        goto LABEL_10351700;
                    iter += v7;
                    node += v7;
                }
                v105 = iter + i;
                v106 = node + i;
                switch (i)
                {
                case 2:
LABEL_103522d1:
                    if ((short)v105[2] == (short)v106[2])
                        goto LABEL_10351ad3;
                    goto LABEL_103522df;
                case 4:
LABEL_10351a56:
                    if ((int)v105[4] != (int)v106[4])
                    {
                        v179 = (char)(int)v105[4];
                        v180 = (char)v106[4];
                        if (v179 != v180 && !((v181 = (unsigned int)_ccall(15, 15, v179 - v180, 0, 0), v11 = (v181 & 1) * 2 - 1, !v11)) || (v182 = (unsigned int)(char)(char)v105[3], v183 = (unsigned int)(char)(char)v106[3], v182 != v183 && !((v184 = (unsigned int)_ccall(15, 15, v182 - v183, 0, 0), v11 = (v184 & 1) * 2 - 1, !v11)) || (v185 = (unsigned int)(char)(char)v105[2], v186 = (unsigned int)(char)(char)v106[2], v185 != v186 && !((v187 = (unsigned int)_ccall(15, 15, v185 - v186, 0, 0), v11 = (v187 & 1) * 2 - 1, !v11)))))
                        {
                        }
                        else
                        {
                            v188 = (char)v105[1];
                            v189 = (char)v106[1];
                            v11 = v188 - v189;
                            if (v188 != v189)
                            {
                                v190 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v190 & 1) * 2 - 1;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
                    }
                    if (v11)
                        goto LABEL_10351ad5;
                    goto LABEL_10351ad3;
                case 5:
LABEL_10351e36:
                    if ((int)v105[5] != (int)v106[5])
                    {
                        v263 = (char)(int)v105[5];
                        v264 = (char)v106[5];
                        if ((v263 == v264 || (v265 = (unsigned int)_ccall(15, 15, v263 - v264, 0, 0), v11 = (v265 & 1) * 2 - 1, !v11)) && !((v266 = (unsigned int)(char)(char)v105[4], v267 = (unsigned int)(char)(char)v106[4], v266 != v267 && !((v268 = (unsigned int)_ccall(15, 15, v266 - v267, 0, 0), v11 = (v268 & 1) * 2 - 1, !v11)) || (v269 = (unsigned int)(char)(char)v105[3], v270 = (unsigned int)(char)(char)v106[3], v269 != v270 && !((v271 = (unsigned int)_ccall(15, 15, v269 - v270, 0, 0), v11 = (v271 & 1) * 2 - 1, !v11))))))
                        {
                            v272 = (char)v105[2];
                            v273 = (char)v106[2];
                            v11 = v272 - v273;
                            if (v272 != v273)
                            {
                                v274 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v274 & 1) * 2 - 1;
                                goto LABEL_10351ebd;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_10351ebd:
                        if (!v11)
                            goto LABEL_10351ec5;
                        break;
                    }
                case 6:
LABEL_10352242:
                    if ((int)v105[6] != (int)v106[6])
                    {
                        v347 = (char)(int)v105[6];
                        v348 = (char)v106[6];
                        if ((v347 == v348 || (v349 = (unsigned int)_ccall(15, 15, v347 - v348, 0, 0), v11 = (v349 & 1) * 2 - 1, !v11)) && !((v350 = (unsigned int)(char)(char)v105[5], v351 = (unsigned int)(char)(char)v106[5], v350 != v351 && !((v352 = (unsigned int)_ccall(15, 15, v350 - v351, 0, 0), v11 = (v352 & 1) * 2 - 1, !v11)) || (v353 = (unsigned int)(char)(char)v105[4], v354 = (unsigned int)(char)(char)v106[4], v353 != v354 && !((v355 = (unsigned int)_ccall(15, 15, v353 - v354, 0, 0), v11 = (v355 & 1) * 2 - 1, !v11))))))
                        {
                            v356 = (char)v105[3];
                            v357 = (char)v106[3];
                            v11 = v356 - v357;
                            if (v356 != v357)
                            {
                                v358 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v358 & 1) * 2 - 1;
                                goto LABEL_103522c9;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_103522c9:
                        if (v11)
                            break;
                        goto LABEL_103522d1;
                    }
                case 7:
LABEL_10352663:
                    if ((int)v105[7] != (int)v106[7])
                    {
                        v431 = (char)(int)v105[7];
                        v432 = (char)v106[7];
                        if ((v431 == v432 || (v433 = (unsigned int)_ccall(15, 15, v431 - v432, 0, 0), v11 = (v433 & 1) * 2 - 1, !v11)) && !((v434 = (unsigned int)(char)(char)v105[6], v435 = (unsigned int)(char)(char)v106[6], v434 != v435 && !((v436 = (unsigned int)_ccall(15, 15, v434 - v435, 0, 0), v11 = (v436 & 1) * 2 - 1, !v11)) || (v437 = (unsigned int)(char)(char)v105[5], v438 = (unsigned int)(char)(char)v106[5], v437 != v438 && !((v439 = (unsigned int)_ccall(15, 15, v437 - v438, 0, 0), v11 = (v439 & 1) * 2 - 1, !v11))))))
                        {
                            v440 = (char)v105[4];
                            v441 = (char)v106[4];
                            v11 = v440 - v441;
                            if (v440 != v441)
                            {
                                v442 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v442 & 1) * 2 - 1;
                                goto LABEL_103526ea;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_103526ea:
                        if (!v11)
                            goto LABEL_103526f2;
                        break;
                    }
                case 8:
LABEL_103519c7:
                    if ((int)v105[8] != (int)v106[8])
                    {
                        v167 = (char)(int)v105[8];
                        v168 = (char)v106[8];
                        if ((v167 == v168 || (v169 = (unsigned int)_ccall(15, 15, v167 - v168, 0, 0), v11 = (v169 & 1) * 2 - 1, !v11)) && !((v170 = (unsigned int)(char)(char)v105[7], v171 = (unsigned int)(char)(char)v106[7], v170 != v171 && !((v172 = (unsigned int)_ccall(15, 15, v170 - v171, 0, 0), v11 = (v172 & 1) * 2 - 1, !v11)) || (v173 = (unsigned int)(char)(char)v105[6], v174 = (unsigned int)(char)(char)v106[6], v173 != v174 && !((v175 = (unsigned int)_ccall(15, 15, v173 - v174, 0, 0), v11 = (v175 & 1) * 2 - 1, !v11))))))
                        {
                            v176 = (char)v105[5];
                            v177 = (char)v106[5];
                            v11 = v176 - v177;
                            if (v176 != v177)
                            {
                                v178 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v178 & 1) * 2 - 1;
                                goto LABEL_10351a4e;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_10351a4e:
                        if (v11)
                            break;
                        goto LABEL_10351a56;
                    }
                case 9:
LABEL_10351da6:
                    if ((int)v105[9] != (int)v106[9])
                    {
                        v251 = (char)v106[9];
                        v252 = (char)v105[9];
                        if ((v252 == v251 || (v253 = (unsigned int)_ccall(15, 15, v252 - v251, 0, 0), v11 = (v253 & 1) * 2 - 1, !v11)) && !((v254 = (unsigned int)(char)(char)v105[8], v255 = (unsigned int)(char)(char)v106[8], v254 != v255 && !((v256 = (unsigned int)_ccall(15, 15, v254 - v255, 0, 0), v11 = (v256 & 1) * 2 - 1, !v11)) || (v257 = (unsigned int)(char)(char)v105[7], v258 = (unsigned int)(char)(char)v106[7], v257 != v258 && !((v259 = (unsigned int)_ccall(15, 15, v257 - v258, 0, 0), v11 = (v259 & 1) * 2 - 1, !v11))))))
                        {
                            v260 = (char)v105[6];
                            v261 = (char)v106[6];
                            v11 = v260 - v261;
                            if (v260 != v261)
                            {
                                v262 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v262 & 1) * 2 - 1;
                                goto LABEL_10351e2e;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_10351e2e:
                        if (v11)
                            break;
                        goto LABEL_10351e36;
                    }
                case 10:
LABEL_103521b2:
                    if ((int)v105[10] != (int)v106[10])
                    {
                        v335 = (char)v106[10];
                        v336 = (char)v105[10];
                        if ((v336 == v335 || (v337 = (unsigned int)_ccall(15, 15, v336 - v335, 0, 0), v11 = (v337 & 1) * 2 - 1, !v11)) && !((v338 = (unsigned int)(char)(char)v106[9], v339 = (unsigned int)(char)(char)v105[9], v339 != v338 && !((v340 = (unsigned int)_ccall(15, 15, v339 - v338, 0, 0), v11 = (v340 & 1) * 2 - 1, !v11)) || (v341 = (unsigned int)(char)(char)v106[8], v342 = (unsigned int)(char)(char)v105[8], v342 != v341 && !((v343 = (unsigned int)_ccall(15, 15, v342 - v341, 0, 0), v11 = (v343 & 1) * 2 - 1, !v11))))))
                        {
                            v344 = (char)v106[7];
                            v345 = (char)v105[7];
                            v11 = v345 - v344;
                            if (v345 != v344)
                            {
                                v346 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v346 & 1) * 2 - 1;
                                goto LABEL_1035223a;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_1035223a:
                        if (v11)
                            break;
                        goto LABEL_10352242;
                    }
                case 11:
LABEL_103525d4:
                    if ((int)v105[11] != (int)v106[11])
                    {
                        v419 = (char)(int)v105[11];
                        v420 = (char)v106[11];
                        if ((v419 == v420 || (v421 = (unsigned int)_ccall(15, 15, v419 - v420, 0, 0), v11 = (v421 & 1) * 2 - 1, !v11)) && !((v422 = (unsigned int)(char)(char)v105[10], v423 = (unsigned int)(char)(char)v106[10], v422 != v423 && !((v424 = (unsigned int)_ccall(15, 15, v422 - v423, 0, 0), v11 = (v424 & 1) * 2 - 1, !v11)) || (v425 = (unsigned int)(char)(char)v105[9], v426 = (unsigned int)(char)(char)v106[9], v425 != v426 && !((v427 = (unsigned int)_ccall(15, 15, v425 - v426, 0, 0), v11 = (v427 & 1) * 2 - 1, !v11))))))
                        {
                            v428 = (char)v105[8];
                            v429 = (char)v106[8];
                            v11 = v428 - v429;
                            if (v428 != v429)
                            {
                                v430 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v430 & 1) * 2 - 1;
                                goto LABEL_1035265b;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_1035265b:
                        if (v11)
                            break;
                        goto LABEL_10352663;
                    }
                case 12:
LABEL_10351937:
                    if ((int)v105[12] != (int)v106[12])
                    {
                        v155 = (char)v106[12];
                        v156 = (char)v105[12];
                        if ((v156 == v155 || (v157 = (unsigned int)_ccall(15, 15, v156 - v155, 0, 0), v11 = (v157 & 1) * 2 - 1, !v11)) && !((v158 = (unsigned int)(char)(char)v105[11], v159 = (unsigned int)(char)(char)v106[11], v158 != v159 && !((v160 = (unsigned int)_ccall(15, 15, v158 - v159, 0, 0), v11 = (v160 & 1) * 2 - 1, !v11)) || (v161 = (unsigned int)(char)(char)v105[10], v162 = (unsigned int)(char)(char)v106[10], v161 != v162 && !((v163 = (unsigned int)_ccall(15, 15, v161 - v162, 0, 0), v11 = (v163 & 1) * 2 - 1, !v11))))))
                        {
                            v164 = (char)v105[9];
                            v165 = (char)v106[9];
                            v11 = v164 - v165;
                            if (v164 != v165)
                            {
                                v166 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v166 & 1) * 2 - 1;
                                goto LABEL_103519bf;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_103519bf:
                        if (v11)
                            break;
                        goto LABEL_103519c7;
                    }
                case 13:
LABEL_10351d17:
                    if ((int)v105[13] != (int)v106[13])
                    {
                        v239 = (char)(int)v105[13];
                        v240 = (char)v106[13];
                        if ((v239 == v240 || (v241 = (unsigned int)_ccall(15, 15, v239 - v240, 0, 0), v11 = (v241 & 1) * 2 - 1, !v11)) && !((v242 = (unsigned int)(char)(char)v105[12], v243 = (unsigned int)(char)(char)v106[12], v242 != v243 && !((v244 = (unsigned int)_ccall(15, 15, v242 - v243, 0, 0), v11 = (v244 & 1) * 2 - 1, !v11)) || (v245 = (unsigned int)(char)(char)v105[11], v246 = (unsigned int)(char)(char)v106[11], v245 != v246 && !((v247 = (unsigned int)_ccall(15, 15, v245 - v246, 0, 0), v11 = (v247 & 1) * 2 - 1, !v11))))))
                        {
                            v248 = (char)v105[10];
                            v249 = (char)v106[10];
                            v11 = v248 - v249;
                            if (v248 != v249)
                            {
                                v250 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v250 & 1) * 2 - 1;
                                goto LABEL_10351d9e;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_10351d9e:
                        if (v11)
                            break;
                        goto LABEL_10351da6;
                    }
                case 14:
LABEL_10352123:
                    if ((int)v105[14] != (int)v106[14])
                    {
                        v323 = (char)(int)v105[14];
                        v324 = (char)v106[14];
                        if ((v323 == v324 || (v325 = (unsigned int)_ccall(15, 15, v323 - v324, 0, 0), v11 = (v325 & 1) * 2 - 1, !v11)) && !((v326 = (unsigned int)(char)(char)v105[13], v327 = (unsigned int)(char)(char)v106[13], v326 != v327 && !((v328 = (unsigned int)_ccall(15, 15, v326 - v327, 0, 0), v11 = (v328 & 1) * 2 - 1, !v11)) || (v329 = (unsigned int)(char)(char)v105[12], v330 = (unsigned int)(char)(char)v106[12], v329 != v330 && !((v331 = (unsigned int)_ccall(15, 15, v329 - v330, 0, 0), v11 = (v331 & 1) * 2 - 1, !v11))))))
                        {
                            v332 = (char)v105[11];
                            v333 = (char)v106[11];
                            v11 = v332 - v333;
                            if (v332 != v333)
                            {
                                v334 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v334 & 1) * 2 - 1;
                                goto LABEL_103521aa;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_103521aa:
                        if (v11)
                            break;
                        goto LABEL_103521b2;
                    }
                case 15:
LABEL_10352544:
                    if ((int)v105[15] != (int)v106[15])
                    {
                        v407 = (char)v106[15];
                        v408 = (char)v105[15];
                        if ((v408 == v407 || (v409 = (unsigned int)_ccall(15, 15, v408 - v407, 0, 0), v11 = (v409 & 1) * 2 - 1, !v11)) && !((v410 = (unsigned int)(char)(char)v105[14], v411 = (unsigned int)(char)(char)v106[14], v410 != v411 && !((v412 = (unsigned int)_ccall(15, 15, v410 - v411, 0, 0), v11 = (v412 & 1) * 2 - 1, !v11)) || (v413 = (unsigned int)(char)(char)v105[13], v414 = (unsigned int)(char)(char)v106[13], v413 != v414 && !((v415 = (unsigned int)_ccall(15, 15, v413 - v414, 0, 0), v11 = (v415 & 1) * 2 - 1, !v11))))))
                        {
                            v416 = (char)v105[12];
                            v417 = (char)v106[12];
                            v11 = v416 - v417;
                            if (v416 != v417)
                            {
                                v418 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v418 & 1) * 2 - 1;
                                goto LABEL_103525cc;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_103525cc:
                        if (v11)
                            break;
                        goto LABEL_103525d4;
                    }
                case 16:
LABEL_103518a8:
                    if ((int)v105[16] != (int)v106[16])
                    {
                        v143 = (char)(int)v105[16];
                        v144 = (char)v106[16];
                        if ((v143 == v144 || (v145 = (unsigned int)_ccall(15, 15, v143 - v144, 0, 0), v11 = (v145 & 1) * 2 - 1, !v11)) && !((v146 = (unsigned int)(char)(char)v105[15], v147 = (unsigned int)(char)(char)v106[15], v146 != v147 && !((v148 = (unsigned int)_ccall(15, 15, v146 - v147, 0, 0), v11 = (v148 & 1) * 2 - 1, !v11)) || (v149 = (unsigned int)(char)(char)v105[14], v150 = (unsigned int)(char)(char)v106[14], v149 != v150 && !((v151 = (unsigned int)_ccall(15, 15, v149 - v150, 0, 0), v11 = (v151 & 1) * 2 - 1, !v11))))))
                        {
                            v152 = (char)v105[13];
                            v153 = (char)v106[13];
                            v11 = v152 - v153;
                            if (v152 != v153)
                            {
                                v154 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v154 & 1) * 2 - 1;
                                goto LABEL_1035192f;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_1035192f:
                        if (v11)
                            break;
                        goto LABEL_10351937;
                    }
                case 17:
LABEL_10351c88:
                    if ((int)v105[0x11] != (int)v106[0x11])
                    {
                        v227 = (char)(int)v105[0x11];
                        v228 = (char)v106[0x11];
                        if ((v227 == v228 || (v229 = (unsigned int)_ccall(15, 15, v227 - v228, 0, 0), v11 = (v229 & 1) * 2 - 1, !v11)) && !((v230 = (unsigned int)(char)(char)v105[16], v231 = (unsigned int)(char)(char)v106[16], v230 != v231 && !((v232 = (unsigned int)_ccall(15, 15, v230 - v231, 0, 0), v11 = (v232 & 1) * 2 - 1, !v11)) || (v233 = (unsigned int)(char)(char)v105[15], v234 = (unsigned int)(char)(char)v106[15], v233 != v234 && !((v235 = (unsigned int)_ccall(15, 15, v233 - v234, 0, 0), v11 = (v235 & 1) * 2 - 1, !v11))))))
                        {
                            v236 = (char)v105[14];
                            v237 = (char)v106[14];
                            v11 = v236 - v237;
                            if (v236 != v237)
                            {
                                v238 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v238 & 1) * 2 - 1;
                                goto LABEL_10351d0f;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_10351d0f:
                        if (v11)
                            break;
                        goto LABEL_10351d17;
                    }
                case 18:
LABEL_10352094:
                    if ((int)v105[18] != (int)v106[18])
                    {
                        v311 = (char)(int)v105[18];
                        v312 = (char)v106[18];
                        if ((v311 == v312 || (v313 = (unsigned int)_ccall(15, 15, v311 - v312, 0, 0), v11 = (v313 & 1) * 2 - 1, !v11)) && !((v314 = (unsigned int)(char)(char)v105[0x11], v315 = (unsigned int)(char)(char)v106[0x11], v314 != v315 && !((v316 = (unsigned int)_ccall(15, 15, v314 - v315, 0, 0), v11 = (v316 & 1) * 2 - 1, !v11)) || (v317 = (unsigned int)(char)(char)v105[16], v318 = (unsigned int)(char)(char)v106[16], v317 != v318 && !((v319 = (unsigned int)_ccall(15, 15, v317 - v318, 0, 0), v11 = (v319 & 1) * 2 - 1, !v11))))))
                        {
                            v320 = (char)v105[15];
                            v321 = (char)v106[15];
                            v11 = v320 - v321;
                            if (v320 != v321)
                            {
                                v322 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v322 & 1) * 2 - 1;
                                goto LABEL_1035211b;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_1035211b:
                        if (v11)
                            break;
                        goto LABEL_10352123;
                    }
                case 19:
LABEL_103524b5:
                    if ((int)v105[19] != (int)v106[19])
                    {
                        v395 = (char)(int)v105[19];
                        v396 = (char)v106[19];
                        if ((v395 == v396 || (v397 = (unsigned int)_ccall(15, 15, v395 - v396, 0, 0), v11 = (v397 & 1) * 2 - 1, !v11)) && !((v398 = (unsigned int)(char)(char)v105[18], v399 = (unsigned int)(char)(char)v106[18], v398 != v399 && !((v400 = (unsigned int)_ccall(15, 15, v398 - v399, 0, 0), v11 = (v400 & 1) * 2 - 1, !v11)) || (v401 = (unsigned int)(char)(char)v105[0x11], v402 = (unsigned int)(char)(char)v106[0x11], v401 != v402 && !((v403 = (unsigned int)_ccall(15, 15, v401 - v402, 0, 0), v11 = (v403 & 1) * 2 - 1, !v11))))))
                        {
                            v404 = (char)v105[16];
                            v405 = (char)v106[16];
                            v11 = v404 - v405;
                            if (v404 != v405)
                            {
                                v406 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v406 & 1) * 2 - 1;
                                goto LABEL_1035253c;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_1035253c:
                        if (v11)
                            break;
                        goto LABEL_10352544;
                    }
                case 20:
LABEL_10351819:
                    if ((int)v105[20] != (int)v106[20])
                    {
                        v131 = (char)(int)v105[20];
                        v132 = (char)v106[20];
                        if ((v131 == v132 || (v133 = (unsigned int)_ccall(15, 15, v131 - v132, 0, 0), v11 = (v133 & 1) * 2 - 1, !v11)) && !((v134 = (unsigned int)(char)(char)v105[19], v135 = (unsigned int)(char)(char)v106[19], v134 != v135 && !((v136 = (unsigned int)_ccall(15, 15, v134 - v135, 0, 0), v11 = (v136 & 1) * 2 - 1, !v11)) || (v137 = (unsigned int)(char)(char)v105[18], v138 = (unsigned int)(char)(char)v106[18], v137 != v138 && !((v139 = (unsigned int)_ccall(15, 15, v137 - v138, 0, 0), v11 = (v139 & 1) * 2 - 1, !v11))))))
                        {
                            v140 = (char)v105[0x11];
                            v141 = (char)v106[0x11];
                            v11 = v140 - v141;
                            if (v140 != v141)
                            {
                                v142 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v142 & 1) * 2 - 1;
                                goto LABEL_103518a0;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_103518a0:
                        if (v11)
                            break;
                        goto LABEL_103518a8;
                    }
                case 21:
LABEL_10351bf9:
                    if ((int)v105[21] != (int)v106[21])
                    {
                        v215 = (char)(int)v105[21];
                        v216 = (char)v106[21];
                        if ((v215 == v216 || (v217 = (unsigned int)_ccall(15, 15, v215 - v216, 0, 0), v11 = (v217 & 1) * 2 - 1, !v11)) && !((v218 = (unsigned int)(char)(char)v105[20], v219 = (unsigned int)(char)(char)v106[20], v218 != v219 && !((v220 = (unsigned int)_ccall(15, 15, v218 - v219, 0, 0), v11 = (v220 & 1) * 2 - 1, !v11)) || (v221 = (unsigned int)(char)(char)v105[19], v222 = (unsigned int)(char)(char)v106[19], v221 != v222 && !((v223 = (unsigned int)_ccall(15, 15, v221 - v222, 0, 0), v11 = (v223 & 1) * 2 - 1, !v11))))))
                        {
                            v224 = (char)v105[18];
                            v225 = (char)v106[18];
                            v11 = v224 - v225;
                            if (v224 != v225)
                            {
                                v226 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v226 & 1) * 2 - 1;
                                goto LABEL_10351c80;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_10351c80:
                        if (v11)
                            break;
                        goto LABEL_10351c88;
                    }
                case 22:
LABEL_10352005:
                    if ((int)v105[22] != (int)v106[22])
                    {
                        v299 = (char)(int)v105[22];
                        v300 = (char)v106[22];
                        if ((v299 == v300 || (v301 = (unsigned int)_ccall(15, 15, v299 - v300, 0, 0), v11 = (v301 & 1) * 2 - 1, !v11)) && !((v302 = (unsigned int)(char)(char)v105[21], v303 = (unsigned int)(char)(char)v106[21], v302 != v303 && !((v304 = (unsigned int)_ccall(15, 15, v302 - v303, 0, 0), v11 = (v304 & 1) * 2 - 1, !v11)) || (v305 = (unsigned int)(char)(char)v105[20], v306 = (unsigned int)(char)(char)v106[20], v305 != v306 && !((v307 = (unsigned int)_ccall(15, 15, v305 - v306, 0, 0), v11 = (v307 & 1) * 2 - 1, !v11))))))
                        {
                            v308 = (char)v105[19];
                            v309 = (char)v106[19];
                            v11 = v308 - v309;
                            if (v308 != v309)
                            {
                                v310 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v310 & 1) * 2 - 1;
                                goto LABEL_1035208c;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_1035208c:
                        if (v11)
                            break;
                        goto LABEL_10352094;
                    }
                case 23:
LABEL_10352426:
                    if ((int)v105[23] != (int)v106[23])
                    {
                        v383 = (char)(int)v105[23];
                        v384 = (char)v106[23];
                        if ((v383 == v384 || (v385 = (unsigned int)_ccall(15, 15, v383 - v384, 0, 0), v11 = (v385 & 1) * 2 - 1, !v11)) && !((v386 = (unsigned int)(char)(char)v105[22], v387 = (unsigned int)(char)(char)v106[22], v386 != v387 && !((v388 = (unsigned int)_ccall(15, 15, v386 - v387, 0, 0), v11 = (v388 & 1) * 2 - 1, !v11)) || (v389 = (unsigned int)(char)(char)v105[21], v390 = (unsigned int)(char)(char)v106[21], v389 != v390 && !((v391 = (unsigned int)_ccall(15, 15, v389 - v390, 0, 0), v11 = (v391 & 1) * 2 - 1, !v11))))))
                        {
                            v392 = (char)v105[20];
                            v393 = (char)v106[20];
                            v11 = v392 - v393;
                            if (v392 != v393)
                            {
                                v394 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v394 & 1) * 2 - 1;
                                goto LABEL_103524ad;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_103524ad:
                        if (v11)
                            break;
                        goto LABEL_103524b5;
                    }
                case 24:
LABEL_1035178a:
                    if ((int)v105[24] != (int)v106[24])
                    {
                        v119 = (char)(int)v105[24];
                        v120 = (char)v106[24];
                        if ((v119 == v120 || (v121 = (unsigned int)_ccall(15, 15, v119 - v120, 0, 0), v11 = (v121 & 1) * 2 - 1, !v11)) && !((v122 = (unsigned int)(char)(char)v105[23], v123 = (unsigned int)(char)(char)v106[23], v122 != v123 && !((v124 = (unsigned int)_ccall(15, 15, v122 - v123, 0, 0), v11 = (v124 & 1) * 2 - 1, !v11)) || (v125 = (unsigned int)(char)(char)v105[22], v126 = (unsigned int)(char)(char)v106[22], v125 != v126 && !((v127 = (unsigned int)_ccall(15, 15, v125 - v126, 0, 0), v11 = (v127 & 1) * 2 - 1, !v11))))))
                        {
                            v128 = (char)v105[21];
                            v129 = (char)v106[21];
                            v11 = v128 - v129;
                            if (v128 != v129)
                            {
                                v130 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v130 & 1) * 2 - 1;
                                goto LABEL_10351811;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_10351811:
                        if (v11)
                            break;
                        goto LABEL_10351819;
                    }
                case 25:
LABEL_10351b6a:
                    if ((int)v105[25] != (int)v106[25])
                    {
                        v203 = (char)(int)v105[25];
                        v204 = (char)v106[25];
                        if ((v203 == v204 || (v205 = (unsigned int)_ccall(15, 15, v203 - v204, 0, 0), v11 = (v205 & 1) * 2 - 1, !v11)) && !((v206 = (unsigned int)(char)(char)v105[24], v207 = (unsigned int)(char)(char)v106[24], v206 != v207 && !((v208 = (unsigned int)_ccall(15, 15, v206 - v207, 0, 0), v11 = (v208 & 1) * 2 - 1, !v11)) || (v209 = (unsigned int)(char)(char)v105[23], v210 = (unsigned int)(char)(char)v106[23], v209 != v210 && !((v211 = (unsigned int)_ccall(15, 15, v209 - v210, 0, 0), v11 = (v211 & 1) * 2 - 1, !v11))))))
                        {
                            v212 = (char)v105[22];
                            v213 = (char)v106[22];
                            v11 = v212 - v213;
                            if (v212 != v213)
                            {
                                v214 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v214 & 1) * 2 - 1;
                                goto LABEL_10351bf1;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_10351bf1:
                        if (v11)
                            break;
                        goto LABEL_10351bf9;
                    }
                case 26:
LABEL_10351f76:
                    if ((int)v105[26] != (int)v106[26])
                    {
                        v287 = (char)(int)v105[26];
                        v288 = (char)v106[26];
                        if ((v287 == v288 || (v289 = (unsigned int)_ccall(15, 15, v287 - v288, 0, 0), v11 = (v289 & 1) * 2 - 1, !v11)) && !((v290 = (unsigned int)(char)(char)v105[25], v291 = (unsigned int)(char)(char)v106[25], v290 != v291 && !((v292 = (unsigned int)_ccall(15, 15, v290 - v291, 0, 0), v11 = (v292 & 1) * 2 - 1, !v11)) || (v293 = (unsigned int)(char)(char)v105[24], v294 = (unsigned int)(char)(char)v106[24], v293 != v294 && !((v295 = (unsigned int)_ccall(15, 15, v293 - v294, 0, 0), v11 = (v295 & 1) * 2 - 1, !v11))))))
                        {
                            v296 = (char)v105[23];
                            v297 = (char)v106[23];
                            v11 = v296 - v297;
                            if (v296 != v297)
                            {
                                v298 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v298 & 1) * 2 - 1;
                                goto LABEL_10351ffd;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_10351ffd:
                        if (v11)
                            break;
                        goto LABEL_10352005;
                    }
                case 27:
LABEL_10352397:
                    if ((int)v105[27] != (int)v106[27])
                    {
                        v371 = (char)(int)v105[27];
                        v372 = (char)v106[27];
                        if ((v371 == v372 || (v373 = (unsigned int)_ccall(15, 15, v371 - v372, 0, 0), v11 = (v373 & 1) * 2 - 1, !v11)) && !((v374 = (unsigned int)(char)(char)v105[26], v375 = (unsigned int)(char)(char)v106[26], v374 != v375 && !((v376 = (unsigned int)_ccall(15, 15, v374 - v375, 0, 0), v11 = (v376 & 1) * 2 - 1, !v11)) || (v377 = (unsigned int)(char)(char)v105[25], v378 = (unsigned int)(char)(char)v106[25], v377 != v378 && !((v379 = (unsigned int)_ccall(15, 15, v377 - v378, 0, 0), v11 = (v379 & 1) * 2 - 1, !v11))))))
                        {
                            v380 = (char)v105[24];
                            v381 = (char)v106[24];
                            v11 = v380 - v381;
                            if (v380 != v381)
                            {
                                v382 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v382 & 1) * 2 - 1;
                                goto LABEL_1035241e;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_1035241e:
                        if (v11)
                            break;
                        goto LABEL_10352426;
                    }
                case 28:
                    if ((int)v105[28] != (int)v106[28])
                    {
                        v107 = (char)(int)v105[28];
                        v108 = (char)v106[28];
                        if ((v107 == v108 || (v109 = (unsigned int)_ccall(15, 15, v107 - v108, 0, 0), v11 = (v109 & 1) * 2 - 1, !v11)) && !((v110 = (unsigned int)(char)(char)v105[27], v111 = (unsigned int)(char)(char)v106[27], v110 != v111 && !((v112 = (unsigned int)_ccall(15, 15, v110 - v111, 0, 0), v11 = (v112 & 1) * 2 - 1, !v11)) || (v113 = (unsigned int)(char)(char)v105[26], v114 = (unsigned int)(char)(char)v106[26], v113 != v114 && !((v115 = (unsigned int)_ccall(15, 15, v113 - v114, 0, 0), v11 = (v115 & 1) * 2 - 1, !v11))))))
                        {
                            v116 = (char)v105[25];
                            v117 = (char)v106[25];
                            v11 = v116 - v117;
                            if (v116 != v117)
                            {
                                v118 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v118 & 1) * 2 - 1;
                                goto LABEL_10351782;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_10351782:
                        if (v11)
                            break;
                        goto LABEL_1035178a;
                    }
                case 29:
                    if ((int)v105[29] != (int)v106[29])
                    {
                        v191 = (char)(int)v105[29];
                        v192 = (char)v106[29];
                        if ((v191 == v192 || (v193 = (unsigned int)_ccall(15, 15, v191 - v192, 0, 0), v11 = (v193 & 1) * 2 - 1, !v11)) && !((v194 = (unsigned int)(char)(char)v105[28], v195 = (unsigned int)(char)(char)v106[28], v194 != v195 && !((v196 = (unsigned int)_ccall(15, 15, v194 - v195, 0, 0), v11 = (v196 & 1) * 2 - 1, !v11)) || (v197 = (unsigned int)(char)(char)v105[27], v198 = (unsigned int)(char)(char)v106[27], v197 != v198 && !((v199 = (unsigned int)_ccall(15, 15, v197 - v198, 0, 0), v11 = (v199 & 1) * 2 - 1, !v11))))))
                        {
                            v200 = (char)v105[26];
                            v201 = (char)v106[26];
                            v11 = v200 - v201;
                            if (v200 != v201)
                            {
                                v202 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v202 & 1) * 2 - 1;
                                goto LABEL_10351b62;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_10351b62:
                        if (v11)
                            break;
                        goto LABEL_10351b6a;
                    }
                case 30:
                    if ((int)v105[30] != (int)v106[30])
                    {
                        v275 = (char)(int)v105[30];
                        v276 = (char)v106[30];
                        if ((v275 == v276 || (v277 = (unsigned int)_ccall(15, 15, v275 - v276, 0, 0), v11 = (v277 & 1) * 2 - 1, !v11)) && !((v278 = (unsigned int)(char)(char)v105[29], v279 = (unsigned int)(char)(char)v106[29], v278 != v279 && !((v280 = (unsigned int)_ccall(15, 15, v278 - v279, 0, 0), v11 = (v280 & 1) * 2 - 1, !v11)) || (v281 = (unsigned int)(char)(char)v105[28], v282 = (unsigned int)(char)(char)v106[28], v281 != v282 && !((v283 = (unsigned int)_ccall(15, 15, v281 - v282, 0, 0), v11 = (v283 & 1) * 2 - 1, !v11))))))
                        {
                            v284 = (char)v105[27];
                            v285 = (char)v106[27];
                            v11 = v284 - v285;
                            if (v284 != v285)
                            {
                                v286 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v286 & 1) * 2 - 1;
                                goto LABEL_10351f6e;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_10351f6e:
                        if (v11)
                            break;
                        goto LABEL_10351f76;
                    }
                case 31:
                    if ((int)v105[31] != (int)v106[31])
                    {
                        v359 = (char)v106[31];
                        v360 = (char)v105[31];
                        if ((v360 == v359 || (v361 = (unsigned int)_ccall(15, 15, v360 - v359, 0, 0), v11 = (v361 & 1) * 2 - 1, !v11)) && !((v362 = (unsigned int)(char)(char)v105[30], v363 = (unsigned int)(char)(char)v106[30], v362 != v363 && !((v364 = (unsigned int)_ccall(15, 15, v362 - v363, 0, 0), v11 = (v364 & 1) * 2 - 1, !v11)) || (v365 = (unsigned int)(char)(char)v105[29], v366 = (unsigned int)(char)(char)v106[29], v365 != v366 && !((v367 = (unsigned int)_ccall(15, 15, v365 - v366, 0, 0), v11 = (v367 & 1) * 2 - 1, !v11))))))
                        {
                            v368 = (char)v105[28];
                            v369 = (char)v106[28];
                            v11 = v368 - v369;
                            if (v368 != v369)
                            {
                                v370 = _ccall(15, 15, v11, 0, 0);
                                v11 = (v370 & 1) * 2 - 1;
                                goto LABEL_1035238f;
                            }
                        }
                    }
                    else
                    {
                        v11 = 0;
LABEL_1035238f:
                        if (v11)
                            break;
                        goto LABEL_10352397;
                    }
                case 3:
LABEL_103526f2:
                    v443 = (char)v105[3];
                    v444 = (char)v106[3];
                    if (v443 == v444 || (v445 = (unsigned int)_ccall(15, 15, v443 - v444, 0, 0), v11 = (v445 & 1) * 2 - 1, !v11))
                    {
LABEL_103522df:
                        v446 = (char)v106[2];
                        v447 = (char)v105[2];
                        if (v447 != v446 && !((v448 = (unsigned int)_ccall(15, 15, v447 - v446, 0, 0), v11 = (v448 & 1) * 2 - 1, !v11)))
                            goto LABEL_10352715;
                        goto LABEL_10351ec5;
                    }
                    else
                    {
LABEL_10352715:
                        goto LABEL_10351ad5;
                    }
                case 1:
LABEL_10351ec5:
                    v449 = (char)v106[1];
                    v450 = (char)v105[1];
                    v11 = v450 - v449;
                    if (v450 != v449)
                    {
                        v451 = _ccall(15, 15, v11, 0, 0);
                        v11 = (v451 & 1) * 2 - 1;
                        goto LABEL_10351ad5;
                    }
                    break;
                default:
LABEL_10351ad3:
                    v11 = 0;
                    goto LABEL_10351ad5;
                }
LABEL_10351700:
LABEL_10351ad5:
                return v11;
            }
            v452 = iter;
            v453 = node;
            v454 = *((char *)v452);
            v455 = *((char *)v453);
            if (v454 != v455)
            {
                v456 = _ccall(15, 15, v454 - v455, 0, 0);
                if ((v456 & 1) * 2 != 1)
                    return (v456 & 1) * 2 - 1;
            }
            v457 = (char)v452[1];
            v458 = (char)v453[1];
            if (v457 != v458)
            {
                v459 = _ccall(15, 15, v457 - v458, 0, 0);
                if ((v459 & 1) * 2 != 1)
                    return (v459 & 1) * 2 - 1;
            }
            v460 = (char)v452[2];
            v461 = (char)v453[2];
            if (v460 != v461)
            {
                v462 = _ccall(15, 15, v460 - v461, 0, 0);
                if ((v462 & 1) * 2 != 1)
                    return (v462 & 1) * 2 - 1;
            }
            v463 = (char)v452[3];
            v464 = (char)v453[3];
        }
        else
        {
            v465 = iter;
            v466 = node;
            v467 = *((char *)v465);
            v468 = *((char *)v466);
            if (v467 != v468)
            {
                v469 = _ccall(15, 15, v467 - v468, 0, 0);
                if ((v469 & 1) * 2 != 1)
                    return (v469 & 1) * 2 - 1;
            }
            v470 = (char)v465[1];
            v471 = (char)v466[1];
            if (v470 != v471)
            {
                v472 = _ccall(15, 15, v470 - v471, 0, 0);
                if ((v472 & 1) * 2 != 1)
                    return (v472 & 1) * 2 - 1;
            }
            v463 = (char)v465[2];
            v464 = (char)v466[2];
        }
    }
    else
    {
        v463 = *((char *)iter);
        v464 = *((char *)node);
    }
    return v463 - v464;
}
```

## `sub_103528b4` `0x103528b4`

_43 bytes. (leaf/helper — see body)_

```c
int sub_103528b4(unsigned int a0, unsigned int a1)
{
    unsigned int v2;  // ecx
    unsigned int v3;  // ebx
    unsigned long v4;  // ldt
    unsigned long v5;  // gdt
    unsigned short v6;  // fs
    unsigned long v7;  // 4138
    unsigned long v8;  // 4146
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v1 = v2;
    v0 = v3;
    v1 = a1 + 12;
    v7 = _ccall(v4, v5, (unsigned int)v6, 0);
    v8 = _ccall(v4, v5, (unsigned int)v6, 0);
    *((int *)v8) = *((int *)*((int *)v7));
    goto a0;
}
```

## `sub_103528df` `0x103528df`

_5 bytes. (leaf/helper — see body)_

```c
void sub_103528df(void)
{
    return;
}
```

## `sub_103528e4` `0x103528e4`

_7 bytes. (leaf/helper — see body)_

```c
int sub_103528e4(unsigned int a0, char a1)
{
    unsigned int v0;  // [bp+0x0]

    InterlockedExchange(&/* unsupported instruction */, v0);
}
```

## `sub_103528eb` `0x103528eb`

_82 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

unsigned int sub_103528eb(int a0, int a1, struct_0 *idx)
{
    unsigned long v2;  // ldt
    unsigned long v3;  // gdt
    unsigned int *v12;  // ebx
    unsigned long v13;  // 4150
    unsigned short v4;  // fs
    unsigned long v5;  // 4142
    unsigned int *v6;  // esi
    int v7;  // edi
    int v8;  // esi
    int v9;  // ebx
    unsigned int v10;  // eax
    unsigned long v11;  // 4139
    int v0;  // [bp-0x8]
    char v1;  // [bp+0x0]

    v0 = a0;
    v5 = _ccall(v2, v3, (unsigned int)v4, 0);
    v6 = *((int *)v5);
    sub_10369d26(a1, a0, idx, 0, v7, v8, v9, a0, v6, &v1);
    v10 = idx->field_4;
    idx->field_4 = v10 & 4294967293;
    v11 = _ccall(v2, v3, (unsigned int)v4, 0);
    v12 = v6;
    *(v12) = *((int *)v11);
    v13 = _ccall(v2, v3, (unsigned int)v4, 0);
    *((unsigned int **)v13) = v12;
    return v10 & 4294967293;
}
```

## `sub_1035293d` `0x1035293d`

_54 bytes. (leaf/helper — see body)_

```c
int sub_1035293d(void)
{
    int v7;  // eax
    int v0;  // [bp-0x18]
    int v1;  // [bp-0x14]
    int v2;  // [bp-0x10]
    int v3;  // [bp+0x4]
    int v4;  // [bp+0x8]
    int v5;  // [bp+0xc]
    int v6;  // [bp+0x10]

    sub_10358449(v3, v4, v5, v6, v7, 0, 0, 0, v0, v1, v2);
    return;
}
```

## `sub_10352973` `0x10352973`

_48 bytes. (leaf/helper — see body)_

```c
void sub_10352973(int a0, int *a1, int a2)
{
    int v0;  // [bp-0x4]

    sub_10351225(v0);
    sub_10358449(a0, a1[4], a2, 0, a1[3], a1[5], a1, 0);
    return;
}
```

## `sub_103529a3` `0x103529a3`

_213 bytes. (leaf/helper — see body)_

```c
extern char g_10352a4c;
extern unsigned int g_1038e180;

unsigned int sub_103529a3(unsigned int *a0, unsigned int a1, int a2, unsigned int a3, unsigned int a4, unsigned int a5, unsigned int a6)
{
    unsigned long v15;  // ldt
    unsigned long v16;  // gdt
    unsigned short v17;  // fs
    unsigned long v18;  // 4195
    unsigned long v19;  // 4207
    unsigned long v20;  // 4111
    unsigned long v21;  // 4123
    unsigned long v22;  // 4107
    char v0;  // [bp-0x40]
    unsigned int v1;  // [bp-0x3c]
    unsigned int *v2;  // [bp-0x38]
    unsigned int *v3;  // [bp-0x30]
    unsigned int *v4;  // [bp-0x2c], Other Possible Types: unsigned int
    unsigned int v5;  // [bp-0x28]
    unsigned int v6;  // [bp-0x24]
    unsigned int v7;  // [bp-0x20]
    unsigned int v8;  // [bp-0x1c]
    unsigned int v9;  // [bp-0x18]
    unsigned int v10;  // [bp-0x14]
    char *v11;  // [bp-0x10], Other Possible Types: unsigned int
    char *v12;  // [bp-0xc], Other Possible Types: unsigned int
    unsigned int v13;  // [bp-0x8]
    char v14;  // [bp-0x4]

    if (a0 == 0x123)
    {
        *((char **)a1) = &g_10352a4c;
        return 1;
    }
    v4 = 0;
    v5 = sub_10352a78;
    v6 = g_1038e180 ^ &v4;
    v7 = a4;
    v8 = a1;
    v9 = a5;
    v10 = a6;
    v11 = 0;
    v12 = 0;
    v13 = 0;
    v11 = &v0;
    v12 = &v14;
    v18 = _ccall(v15, v16, (unsigned int)v17, 0);
    v4 = *((int *)v18);
    v19 = _ccall(v15, v16, (unsigned int)v17, 0);
    *((unsigned int ***)v19) = &v4;
    v2 = a0;
    v3 = *((int *)(sub_10358da8(v0, 1, a0, a2) + 128));
    v3(*(a0), &v2);
    v1 = 0;
    if (v13)
    {
        v20 = _ccall(v15, v16, (unsigned int)v17, 0);
        *(v4) = *((int *)*((int *)v20));
        v21 = _ccall(v15, v16, (unsigned int)v17, 0);
        *((unsigned int **)v21) = v4;
    }
    else
    {
        v22 = _ccall(v15, v16, (unsigned int)v17, 0);
        *((unsigned int **)v22) = v4;
    }
    return 0;
}
```

## `sub_10352a78` `0x10352a78`

_152 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;

typedef struct struct_1 {
    char padding_0[12];
    int field_c;
    int field_10;
    int field_14;
    int field_18;
    char padding_1c[8];
    unsigned int field_24;
} struct_1;

unsigned int sub_10352a78(struct_0 *a0, struct_1 *a1, int a2)
{
    int v1;  // ebx
    int v2;  // ecx
    char v0;  // [bp+0x0]

    sub_10351225(v1, v2, &v0);
    if (((char)a0->field_4 & 0x66))
    {
        a1->field_24 = 1;
        return 1;
    }
    sub_10358449(a0, a1->field_10, a2, 0, a1->field_c, a1->field_14, a1->field_18, 1);
    if (!a1->field_24)
        sub_103528eb(v2, a1, a0);
    sub_103529a3(0x123, &/* unsupported instruction */, 0, 0, 0, 0, 0);
    goto v2;
}
```

## `sub_10352aa6` `0x10352aa6`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10352aa6(void)
{
}
```

## `sub_10352b0f` `0x10352b0f`

_3 bytes. (leaf/helper — see body)_

```c
int sub_10352b0f(void)
{
}
```

## `sub_10352b15` `0x10352b15`

_115 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
} struct_0;

int sub_10352b15(unsigned int *idx, int a1, int a2, unsigned int *a3, unsigned int *a4)
{
    unsigned int v1;  // ecx
    unsigned int v2;  // esi
    unsigned int v3;  // ebx
    unsigned int v4;  // ebx
    struct_0 *v5;  // eax
    unsigned int v6;  // esi
    unsigned int v0;  // [bp-0x8]

    v0 = v1;
    v2 = idx[3];
    v0 = idx[4];
    v3 = v2;
    while (true)
    {
        v4 = v3;
        idx = v2;
        do
        {
            if (a1 < 0)
            {
                v6 = v2 + 1;
                *(a3) = v6;
                *(a4) = v4;
                if (v4 > idx[3] || v6 > v4)
                    sub_1035911a();
                return v6 * 20 + v0;
            }
            if (v2 == 4294967295)
                sub_1035911a();
            v2 -= 1;
            v5 = v2 * 20 + v0;
        } while ((v5->field_4 >= a2 || a2 > v5[1].padding_0) && v2 != 4294967295);
        a1 -= 1;
        v3 = idx;
    }
}
```

## `sub_10352b88` `0x10352b88`

_40 bytes. (leaf/helper — see body)_

```c
unsigned int [2] sub_10352b88(unsigned int *a0, unsigned int a1)
{
    int v0;  // [bp-0x4]

    *(a0) = a1;
    a0[1] = *((int *)(sub_10358da8(v0) + 152));
    *((unsigned int **)(sub_10358da8(v0) + 152)) = a0;
    return a0;
}
```

## `sub_10352bb0` `0x10352bb0`

_33 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    unsigned int field_0;
    struct struct_0 *field_4;
} struct_0;

unsigned int sub_10352bb0(unsigned int a0)
{
    struct_0 *iter;  // eax

    for (iter = *((int *)(sub_10358da8() + 152)); iter; iter = iter->field_4)
    {
        if (iter->field_0 == a0)
            return 0;
    }
    return 1;
}
```

## `sub_10352bd1` `0x10352bd1`

_76 bytes. (leaf/helper — see body)_

```c
unsigned int [39] sub_10352bd1(unsigned int *idx)
{
    unsigned int v1[39];  // eax
    unsigned int v2[39];  // eax
    unsigned int index[39];  // eax
    unsigned int v4[39];  // ecx
    int v0;  // [bp-0x4]

    if (idx == *((int *)(sub_10358da8(v0) + 152)))
    {
        v1 = sub_10358da8();
        v1[38] = idx[1];
        return v1;
    }
    v2 = *((int *)(sub_10358da8() + 152));
    while (true)
    {
        index = v2;
        if (!index[1])
            return sub_1035911a();
        v4 = index[1];
        if (idx == index[1])
        {
            index[1] = idx[1];
            return index;
        }
        v2 = v4;
    }
}
```

## `sub_10352c1d` `0x10352c1d`

_94 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1038e180;

unsigned int sub_10352c1d(int a0, int a1, int a2, int a3, int a4)
{
    unsigned long v3;  // ldt
    unsigned long v4;  // gdt
    unsigned short v5;  // fs
    unsigned long v6;  // 4211
    unsigned int v7;  // eax
    unsigned long v8;  // 4215
    unsigned int v9;  // eax
    unsigned long v10;  // 4112
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x1c]
    char v2;  // [bp+0x0]

    v0 = 0;
    v6 = _ccall(v3, v4, (unsigned int)v5, 0);
    v7 = *((int *)v6);
    v1 = *((int *)v6);
    v8 = _ccall(v3, v4, (unsigned int)v5, 0);
    *((unsigned int **)v8) = &v1;
    v9 = sub_10359170(a2, a0, a4, v7, sub_10352973, g_1038e180 ^ &v1, a1, a0, a3 + 1, &v2);
    v10 = _ccall(v3, v4, (unsigned int)v5, 0);
    *((unsigned int *)v10) = v7;
    return v9;
}
```

## `sub_10352c80` `0x10352c80`

_43 bytes. (leaf/helper — see body)_

```c
int sub_10352c80(void)
{
    char *v3;  // eax
    unsigned int *v4;  // ecx
    unsigned int *i;  // eax
    char v0;  // [bp-0x4]
    unsigned int v1;  // [bp+0x0]

    v4 = &v1 - v3 & ~(-(&v1 < v3));
    for (i = &v0 & 0xfffff000; v4 < i; i += 0x400);
    *(v4) = v1;
    return;
}
```

## `sub_10352cb0` `0x10352cb0`

_138 bytes. (leaf/helper — see body)_

```c
void* sub_10352cb0(void* a0, void* a1)
{
    void* iter;  // edi
    void* node;  // ecx
    unsigned int v2;  // edx

    iter = a0;
    node = a1;
    if (((char)node & 3))
    {
        do
        {
            v2 = _INSERT(v2, 0, *((char *)node));
            node += 1;
            if (!*((char *)node))
            {
                *((char *)iter) = v2;
                return a0;
            }
        } while ((*((char *)iter) = (char)v2, iter += 1, node = node, ((char)node & 3)));
    }
    while (true)
    {
        v2 = *((int *)node);
        if (((*((int *)node) ^ 4294967295 ^ 2130640639 + *((int *)node)) & 0x81010100))
        {
            if (!(char)v2)
            {
                *((char *)iter) = v2;
                return a0;
            }
            else if (!*((char *)((void*)&v2 + 1)))
            {
                *((unsigned short *)iter) = v2;
                return a0;
            }
            else if (!(v2 & 0xff0000))
            {
                *((unsigned short *)iter) = v2;
                *((char *)&iter[2]) = 0;
                return a0;
            }
            else if (!(v2 & 0xff000000))
            {
                *((unsigned int *)iter) = v2;
                return a0;
            }
        }
        *((unsigned int *)iter) = v2;
        iter += 4;
        node += 4;
    }
}
```

## `sub_10352cb7` `0x10352cb7`

_9 bytes. (leaf/helper — see body)_

```c
void sub_10352cb7(unsigned int a0)
{
    sub_10352cc0();
    return;
}
```

## `sub_10352cc0` `0x10352cc0`

_101 bytes. (leaf/helper — see body)_

```c
int sub_10352cc0(void* a0)
{
    void* iter;  // ecx
    unsigned int v2;  // edi
    void* v3;  // ecx
    unsigned int v0;  // [bp-0x4]

    iter = a0;
    v0 = v2;
    if (!((char)iter & 3))
    {
        while (true)
        {
LABEL_10352ce0:
            v3 = iter + 4;
            iter = v3;
            if (!((*((int *)iter) ^ 4294967295 ^ 2130640639 + *((int *)iter)) & 0x81010100))
                continue;
            iter = v3;
            if (!((int)v3[4] & 0xff000000))
                break;
        }
    }
    while (true)
    {
        iter += 1;
        if (!*((char *)iter))
            break;
        iter = iter;
        if (!((char)iter & 3))
            goto LABEL_10352ce0;
    }
}
```

## `sub_10352da8` `0x10352da8`

_28 bytes. (leaf/helper — see body)_

```c
unsigned short * sub_10352da8(unsigned short *a0, unsigned short *iter)
{
    unsigned short *v0;  // ecx
    unsigned short i;  // ax

    v0 = a0;
    do
    {
        i = *(iter);
        *(v0) = i;
        iter += 1;
        v0 += 1;
    } while (i);
    return a0;
}
```

## `sub_10352dd5` `0x10352dd5`

_11 bytes. (leaf/helper — see body)_

```c
void sub_10352dd5(unsigned int a0, char a1)
{
    sub_10352de0();
    return;
}
```

## `sub_10352de0` `0x10352de0`

_195 bytes. (leaf/helper — see body)_

```c
void* sub_10352de0(void* a0, char a1)
{
    unsigned int v2;  // ebx
    void* iter;  // edx
    unsigned int v11;  // eax
    char v12;  // al
    void* v4;  // edx
    unsigned int v5;  // edi
    unsigned int v6;  // esi
    unsigned int v7;  // ebx
    unsigned int v8;  // ecx
    unsigned int v9;  // esi
    unsigned int v10;  // eax
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v2 = a1;
    iter = a0;
    if (((char)iter & 3))
    {
        do
        {
            v4 = iter;
            iter = v4 + 1;
            if (*((char *)v4) == (char)v2)
                return iter - 1;
            if (!*((char *)v4))
                return NULL;
            iter = iter;
        } while (((char)iter & 3));
    }
    v1 = v5;
    v0 = v6;
    v7 = (v2 | v2 * 0x100) * 0x10000 | v2 | v2 * 0x100;
    while (true)
    {
        v8 = *((int *)iter) ^ v7;
        v9 = 2130640639 + *((int *)iter);
        v10 = *((int *)iter) ^ 4294967295 ^ v9;
        iter += 4;
        if (((v8 ^ 4294967295 ^ 2130640639 + v8) & 0x81010100))
        {
            v11 = (int)iter[4];
            if ((char)v11 == (char)v7)
                return iter - 4;
            if (!(char)v11)
                break;
            if (*((char *)((void*)&v11 + 1)) == (char)v7)
                return iter - 3;
            if (!*((char *)((void*)&v11 + 1)))
                break;
            v12 = v11 >> 16;
            if (v12 == (char)v7)
                return iter - 2;
            if (!v12)
                break;
            if (v12 == (char)v7)
                return iter - 1;
            if (!v12)
                break;
        }
        else if ((v10 & 0x81010100) && ((v10 & 0x81010100 & 0x1010100) || !(v9 & 0x80000000)))
        {
            break;
        }
    }
    return NULL;
}
```

## `sub_10352ea0` `0x10352ea0`

_45 bytes. (leaf/helper — see body)_

```c
void* sub_10352ea0(void* a0, char i)
{
    void* v0;  // edi

    do
    {
        if (false)
            break;
    } while (*((char *)a0));
    v0 = a0 - 1;
    do
    {
        if (false)
            break;
    } while (i != *((char *)v0));
    if ((char)v0[1] == i)
        return v0 + 1;
    return NULL;
}
```

## `sub_10352ecd` `0x10352ecd`

_34 bytes. (leaf/helper — see body)_

```c
unsigned short * sub_10352ecd(unsigned short *i, unsigned short a1)
{
    for (; *(i); i += 1)
    {
        if (*(i) == a1)
            return i;
    }
    return NULL;
}
```

## `sub_10352eef` `0x10352eef`

_48 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10352eef(unsigned short *a0, unsigned short a1)
{
    unsigned short v0[2];  // eax
    unsigned short v1[2];  // eax
    unsigned int v2;  // 4125

    v0 = a0;
    do
    {
        v0 = &v0[1];
    } while (v0[0]);
    do
    {
        v1 = &v1[1];
    } while (v1 != a0 && v1[0] != a1);
    v2 = _ccall(5, 0, (unsigned int)(v1[0] - a1), 0);
    return v1 & ~(-(v2 & 1));
}
```

## `sub_10352f20` `0x10352f20`

_139 bytes. (leaf/helper — see body)_

```c
int sub_10352f20(void* a0)
{
    void* iter;  // ecx
    unsigned int v1;  // eax

    iter = a0;
    if (!((char)iter & 3))
    {
        while (true)
        {
LABEL_10352f50:
            iter += 4;
            if (!((*((int *)iter) ^ 4294967295 ^ 2130640639 + *((int *)iter)) & 0x81010100))
                continue;
            v1 = (int)iter[4];
            if (!(char)v1)
                return iter - 4 - a0;
            if (!*((char *)((void*)&v1 + 1)))
                return iter - 3 - a0;
            if (!(v1 & 0xff0000))
                return iter - 2 - a0;
            iter = iter;
            if (!(v1 & 0xff000000))
                break;
        }
    }
    while (true)
    {
        iter += 1;
        if (!*((char *)iter))
            break;
        iter = iter;
        if (!((char)iter & 3))
            goto LABEL_10352f50;
    }
    return iter - 1 - a0;
}
```

## `sub_10352fb0` `0x10352fb0`

_292 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char field_0;
    char field_1[4];
} struct_0;

void* sub_10352fb0(void* a0, struct_0 *a1, unsigned int a2)
{
    unsigned int v2;  // ecx
    unsigned int v3;  // esi
    unsigned int iter;  // ecx
    unsigned int iter1;  // ebx
    unsigned int v9;  // ecx
    unsigned int v10;  // eax
    unsigned int v11;  // edx
    char v13;  // 4107
    void* iter2;  // edi
    unsigned int i;  // ecx
    unsigned int v4;  // ebx
    struct_0 *node;  // esi
    unsigned int v6;  // ecx
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v2 = a2;
    if (!v2)
        return a0;
    v1 = v3;
    v0 = v4;
    iter1 = v2;
    node = a1;
    iter2 = a0;
    if (!((char)node & 3))
    {
        v6 = v2 >> 2;
        if (!(v2 & 0xfffffffc))
            goto LABEL_10353003;
        goto LABEL_1035305f;
    }
    do
    {
        v10 = _INSERT(v10, 0, node->field_0);
        node = node->field_1;
        *((char *)iter2) = node->field_0;
        iter2 += 1;
        iter = v2 - 1;
        if (v2 == 1)
            return a0;
        if (!(char)v10)
        {
            if (((char)iter2 & 3))
            {
                do
                {
                    *((char *)iter2) = v10;
                    iter2 += 1;
                    iter -= 1;
                    if (iter == 1)
                        return a0;
                } while ((iter = iter, ((char)iter2 & 3)));
            }
            iter1 = iter;
            i = iter >> 2;
            goto LABEL_103530b7;
        }
    } while ((v2 = iter, node = node, ((char)node & 3)));
    iter1 = iter;
    v6 = iter >> 2;
    if (!(iter & 0xfffffffc))
        goto LABEL_10352ffe;
    while (true)
    {
LABEL_1035305f:
        v9 = v6;
        v10 = *((int *)&node->field_0) ^ 4294967295 ^ 2130640639 + *((int *)&node->field_0);
        v11 = *((int *)&node->field_0);
        node = &node->field_1[3];
        if (!(v10 & 0x81010100))
        {
            *((unsigned int *)iter2) = v11;
            iter2 += 4;
            v6 = v9 - 1;
            if (v9 == 1)
            {
LABEL_10352ffe:
                iter1 &= 3;
                if (!((char)iter1 & 3))
                    return a0;
                while (true)
                {
LABEL_10353003:
                    v13 = node->field_0;
                    v10 = _INSERT(v10, 0, v13);
                    node = node->field_1;
                    *((char *)iter2) = v13;
                    iter2 += 1;
                    if (!v13)
                        break;
                    iter1 -= 1;
                    if (iter1 == 1)
                        return a0;
                }
                goto LABEL_10353048;
            }
        }
        else
        {
            if ((char)v11)
            {
                if (!*((char *)((void*)&v11 + 1)))
                {
                    *((unsigned int *)iter2) = v11 & 0xff;
                    goto LABEL_103530ad;
                }
                else if (!(v11 & 0xff0000))
                {
                    *((unsigned int *)iter2) = v11 & 0xffff;
                    goto LABEL_103530ad;
                }
                else if (!(v11 & 0xff000000))
                {
                    *((unsigned int *)iter2) = v11;
                    goto LABEL_103530ad;
                }
            }
            *((unsigned int *)iter2) = 0;
LABEL_103530ad:
            iter2 += 4;
            v10 = 0;
            i = v9 - 1;
            if (v9 == 1)
                goto LABEL_103530c3;
LABEL_103530b7:
            v10 = 0;
            do
            {
                *((unsigned int *)iter2) = 0;
                iter2 += 4;
                i -= 1;
            } while (i != 1);
LABEL_103530c3:
            iter1 &= 3;
            if (!((char)iter1 & 3))
                return a0;
            while (true)
            {
LABEL_10353048:
                iter1 -= 1;
                if (iter1 == 1)
                    break;
                *((char *)iter2) = v10;
                iter2 += 1;
            }
            return a0;
        }
    }
}
```

## `sub_103530d4` `0x103530d4`

_22 bytes. (leaf/helper — see body)_

```c
int sub_103530d4(unsigned short *a0)
{
    unsigned short *v0;  // eax
    unsigned short *v1;  // eax
    unsigned short *v2;  // eax

    v0 = a0;
    do
    {
        v2 = v0 + 1;
        v0 = v2;
    } while (*(v1));
    return (v1 + 1 - a0 >> 1) - 1;
}
```

## `sub_103530ea` `0x103530ea`

_61 bytes. (leaf/helper — see body)_

```c
void* sub_103530ea(void* a0, unsigned short *node, unsigned int a2)
{
    void* v0;  // edi
    unsigned short v1;  // ax
    void* iter;  // edi
    unsigned int v3;  // ecx
    unsigned int v4;  // ecx
    unsigned int v5;  // ecx
    unsigned int v6;  // ecx
    unsigned int v7;  // 4106
    unsigned int v8;  // ecx

    if (!a2)
        return a0;
    v0 = a0;
    do
    {
        v1 = *(node);
        *((unsigned short *)v0) = v1;
        iter = v0 + 2;
        node += 1;
    } while (v1 && (v3 = a2 - 1, a2 -= 1, v0 = iter, a2 != 1));
    v4 = a2;
    if (!v4)
        return a0;
    v5 = v4 - 1;
    if (v4 == 1)
        return a0;
    for (v6 = v5 >> 1; v6; iter += 4)
    {
        v6 -= 1;
        *((unsigned int *)iter) = 0;
    }
    v7 = _ccall(27, v5 >> 1, v5, 0);
    for (v8 = 0 + (v7 & 1); v8; iter += 2)
    {
        v8 -= 1;
        *((unsigned short *)iter) = 0;
    }
    return a0;
}
```

## `sub_10353127` `0x10353127`

_123 bytes. (leaf/helper — see body)_

```c
unsigned int sub_10353127(char *a0, int a1)
{
    int v7;  // esi
    unsigned int v8;  // eax
    int v0;  // [bp-0x28]
    char *v1;  // [bp-0x24]
    int v2;  // [bp-0x20]
    int v3;  // [bp-0x20]
    char *v4;  // [bp-0x1c]
    unsigned int v5;  // [bp-0x18]
    char v6;  // [bp+0xc]

    if (a1 && a0)
    {
        v4 = a0;
        v1 = a0;
        v2 = 2147483647;
        v5 = 66;
        v8 = sub_10359373(&v1, a1, 0, &v6, v7);
        v3 = v2 - 1;
        if (v2 - 1 >= 0)
            *(v1) = 0;
        else
            sub_103591bc(0, &v1);
        return v8;
    }
    *((unsigned int *)sub_103575e0(v0)) = 22;
    sub_103535f2(0, 0, 0, 0, 0);
    return 4294967295;
}
```

## `sub_103531a2` `0x103531a2`

_28 bytes. (leaf/helper — see body)_

```c
int sub_103531a2(int a0, int a1, int a2)
{
    char v0;  // [bp+0x10]

    return sub_10359dd1(a0, a1, a2, 0, &v0);
}
```

## `sub_103531be` `0x103531be`

_14 bytes. (leaf/helper — see body)_

```c
extern char g_103945a8;

void sub_103531be(int a0)
{
    *((char **)a0) = &g_103945a8;
    sub_10359e57(a0);
    return;
}
```

## `sub_103531cc` `0x103531cc`

_28 bytes. (leaf/helper — see body)_

```c
int sub_103531cc(int a0, char a1)
{
    int v0;  // [bp-0x8]

    sub_103531be(a0);
    if ((a1 & 1))
    {
        v0 = a0;
        sub_10350abd();
    }
    return a0;
}
```

## `sub_103531e8` `0x103531e8`

_27 bytes. (leaf/helper — see body)_

```c
int sub_103531e8(int a0, int a1)
{
    return -(0 < sub_10359ed0(a1 + 9, a0 + 9)) + 1;
}
```

## `sub_10353203` `0x10353203`

_17 bytes. (leaf/helper — see body)_

```c
extern char g_103945b0;

unsigned int [3] sub_10353203(unsigned int *idx)
{
    idx[1] = 0;
    idx[2] = 0;
    *(idx) = &g_103945b0;
    return idx;
}
```

## `sub_10353214` `0x10353214`

_78 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    unsigned int field_8;
} struct_0;

extern char g_103945b0;

struct_0 * sub_10353214(struct_0 *idx, void* a1)
{
    int v0;  // esi
    int v1;  // eax

    *((char **)&idx->padding_0[0]) = &g_103945b0;
    if (*((int *)a1))
    {
        v0 = sub_10352f20(*((int *)a1)) + 1;
        v1 = sub_10355a15(v0);
        idx->field_4 = v1;
        if (v1)
            sub_10359f58(v1, v0, *((int *)a1));
    }
    else
    {
        idx->field_4 = 0;
    }
    idx->field_8 = 1;
    return idx;
}
```

## `sub_10353262` `0x10353262`

_24 bytes. (leaf/helper — see body)_

```c
extern char g_103945b0;

unsigned int [3] sub_10353262(unsigned int *idx, unsigned int *a1)
{
    unsigned int v0;  // ecx

    *(idx) = &g_103945b0;
    v0 = *(a1);
    idx[2] = 0;
    idx[1] = v0;
    return idx;
}
```

## `sub_1035327a` `0x1035327a`

_88 bytes. (leaf/helper — see body)_

```c
extern char g_103945b0;

void* sub_1035327a(void* idx, void* index)
{
    unsigned int v0;  // eax
    unsigned int v1;  // eax
    int v2;  // edi
    int v3;  // eax

    *((char **)idx) = &g_103945b0;
    v0 = (int)index[8];
    *((unsigned int *)&idx[8]) = v0;
    v1 = (int)index[4];
    if (!v0)
    {
        *((unsigned int *)&idx[4]) = v1;
        return idx;
    }
    else if (v1)
    {
        v2 = sub_10352f20(v1) + 1;
        v3 = sub_10355a15(v2);
        *((int *)&idx[4]) = v3;
        if (!v3)
            return idx;
        sub_10359f58(v3, v2, (int)index[4]);
        return idx;
    }
    else
    {
        *((unsigned int *)&idx[4]) = 0;
        return idx;
    }
}
```

## `sub_103532d2` `0x103532d2`

_22 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    unsigned int field_8;
} struct_0;

extern char g_103945b0;

void sub_103532d2(struct_0 *a0)
{
    unsigned int v1;  // 4098

    v1 = a0->field_8;
    *((char **)&a0->padding_0[0]) = &g_103945b0;
    if (v1)
        sub_1035345e(a0->field_4);
    return;
}
```

## `sub_103532e8` `0x103532e8`

_13 bytes. refs "Unknown exception"_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
} struct_0;


unsigned int sub_103532e8(struct_0 *a0)
{
    unsigned int v1;  // eax

    v1 = a0->field_4;
    if (!a0->field_4)
        v1 = "Unknown exception";
    return v1;
}
```

## `sub_103532f5` `0x103532f5`

_25 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    int field_4;
    unsigned int field_8;
} struct_0;

extern char g_103945d0;

struct_0 * sub_103532f5(struct_0 *a0)
{
    unsigned int v0;  // [bp+0x4]

    sub_10353214(a0, &v0);
    *((char **)&a0->padding_0[0]) = &g_103945d0;
    return a0;
}
```

## `sub_1035330e` `0x1035330e`

_24 bytes. (leaf/helper — see body)_

```c
extern char g_103945d0;

void* sub_1035330e(void* a0, void* a1)
{
    sub_1035327a(a0, a1);
    *((char **)a0) = &g_103945d0;
    return a0;
}
```

