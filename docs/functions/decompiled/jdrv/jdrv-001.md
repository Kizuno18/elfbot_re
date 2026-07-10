# elfbot.dll decompiled — jdrv 0x10002d16..0x100117ef

angr pseudo-C for each function in this address range. Named functions link to their subsystem doc. Auto-summary lists the APIs/strings each touches.

## `sub_10002d16` `0x10002d16`

_48 bytes. calls SendMessageA_

```c
extern HWND g_1005f61a;

int sub_10002d16(void)
{
    unsigned int v1[2];  // eax
    unsigned int idx[11];  // [bp+0x4]

    v1[0] = idx[10];
    v1[1] = idx[2];
    SendMessageA(g_1005f61a, 273, 0x539, v1);
    return;
}
```

## registerDialogs `0x10002d46`

Named — see [doc 05](../../05-*.md). _824 bytes. refs "TBOTDLG7", "TBOTDLGA", "TBOTDLGB"_

```c
extern unsigned int g_100428e7;
extern char g_10042d7b;
extern HMODULE g_1005f60a;

int sub_10002d46(unsigned int a0)
{
    unsigned int iter;  // eax
    unsigned int v0;  // [bp-0x54]
    unsigned int v1;  // [bp-0x34]
    unsigned int v2;  // [bp-0x30]
    unsigned int v3;  // [bp-0x2c]
    unsigned int v4;  // [bp-0x28]
    unsigned int v5;  // [bp-0x24]
    unsigned int v6;  // [bp-0x20]
    HICON v7;  // [bp-0x1c]
    HCURSOR v8;  // [bp-0x18]
    unsigned int v9;  // [bp-0x14]
    unsigned int v10;  // [bp-0x10]
    unsigned int v11;  // [bp-0xc]
    HICON v12;  // [bp-0x8]

    InitCommonControls();
    v1 = 48;
    v2 = 3;
    v3 = sub_10003146;
    v4 = 0;
    v5 = 30;
    v0 = a0;
    v6 = a0;
    v9 = 16;
    v10 = &g_100428e7;
    v11 = "TBOTDLG7";
    v7 = LoadIconA(NULL, 0x7f00);
    v12 = v7;
    v8 = LoadCursorA(NULL, 0x7f00);
    sub_10002d16(&v1);
    v3 = sub_10006bce;
    v11 = "TBOTDLGA";
    v9 = 6;
    sub_10002d16(&v1);
    v3 = sub_1001eb33;
    v11 = "TBOTDLGB";
    v9 = 16;
    sub_10002d16(&v1);
    v3 = sub_1001e7c3;
    v11 = "TBOTDLGC";
    v9 = 16;
    sub_10002d16(&v1);
    v3 = sub_10007360;
    v11 = "TBOTDLGD";
    v9 = 16;
    sub_10002d16(&v1);
    v3 = sub_1001e3e5;
    v11 = "TBOTDLGE";
    v9 = 16;
    sub_10002d16(&v1);
    v3 = sub_10007ec4;
    v11 = "TBOTDLGF";
    v9 = 16;
    sub_10002d16(&v1);
    v3 = sub_1001e313;
    v11 = "TBOTDLGH";
    v9 = 16;
    sub_10002d16(&v1);
    v3 = sub_10007ca5;
    v11 = "TBOTDLGI";
    v9 = 16;
    sub_10002d16(&v1);
    v3 = sub_10007b55;
    v11 = "TBOTDLGJ";
    v9 = 16;
    sub_10002d16(&v1);
    v3 = sub_1001e1d9;
    v11 = "TBOTDLGK";
    v9 = 16;
    sub_10002d16(&v1);
    v3 = sub_1001df05;
    v11 = "TBOTDLGL";
    v9 = 16;
    sub_10002d16(&v1);
    v3 = sub_1001d5fd;
    v11 = "TBOTDLGM";
    v9 = 16;
    sub_10002d16(&v1);
    v3 = sub_1001d2e0;
    v11 = "TBOTDLGN";
    v9 = 16;
    sub_10002d16(&v1);
    v3 = sub_1001d151;
    v11 = "TBOTDLGO";
    v9 = 16;
    sub_10002d16(&v1);
    v3 = sub_10006d3b;
    v11 = "TBOTDLGP";
    v9 = 16;
    sub_10002d16(&v1);
    v3 = sub_1001ef0c;
    v11 = "TBOTDLGQ";
    v9 = 16;
    sub_10002d16(&v1);
    v3 = sub_1001a715;
    v11 = "TBOTDLGR";
    v9 = 16;
    sub_10002d16(&v1);
    v3 = sub_10019751;
    v11 = "TBOTDLGS";
    v9 = 16;
    sub_10002d16(&v1);
    v3 = sub_1000802f;
    v11 = "TBOTDLGT";
    v9 = 16;
    sub_10002d16(&v1);
    v3 = sub_100083b6;
    v11 = "TBOTDLGU";
    v9 = 16;
    sub_10002d16(&v1);
    v3 = sub_100086b3;
    v11 = "TBOTDLGV";
    v9 = 16;
    sub_10002d16(&v1);
    v3 = sub_1001b8be;
    v11 = "TBOTDLGW";
    v9 = 16;
    sub_10002d16(&v1);
    for (iter = &(&g_10042d7b)[GetModuleFileNameA(g_1005f60a, &g_10042d7b, 260)]; *((char *)iter) != 92 && iter > &g_10042d7b; iter -= 1);
    *((char *)(iter + 1)) = 0;
    return iter;
}
```

## `sub_1000307e` `0x1000307e`

_88 bytes. calls SendMessageA_

```c
extern unsigned int g_1005f60a;
extern HWND g_10072fc0;

LRESULT sub_1000307e(HWND a0, int a1, unsigned int a2)
{
    HWND v0;  // [bp-0x34], Other Possible Types: unsigned int
    int v1;  // [bp-0x30]
    unsigned int v2;  // [bp-0x2c]
    HWND v3;  // [bp-0x28]
    HWND v4;  // [bp-0x24]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]

    v1 = 44;
    v2 = 0x11;
    v0 = a0;
    v3 = a0;
    v4 = GetDlgItem(a0, a1);
    v0 = g_1005f60a;
    v5 = g_1005f60a;
    v0 = a2;
    v6 = a2;
    v7 = 0;
    return SendMessageA(g_10072fc0, 0x404, NULL, &v1);
}
```

## `sub_100030d6` `0x100030d6`

_112 bytes. refs "playerinfo\\", "%s\\playerinfo\\%c\\"_

```c
extern int g_10042f83;

int sub_100030d6(void)
{
    int v4;  // eax
    unsigned int i;  // ebx
    int v0;  // [bp-0x138]
    unsigned int v1;  // [bp-0x134]
    Byte v2[300];  // [bp-0x130]

    lstrcpy(v2, &g_10042f83);
    lstrcat(v2, "playerinfo\\");
    v4 = CreateDirectoryA(v2, NULL);
    for (i = 64; i <= 90; i += 1)
    {
        v1 = i;
        v0 = &g_10042f83;
        wsprintfA(v2, "%s\\playerinfo\\%c\\");
        v4 = CreateDirectoryA(v2, NULL);
    }
    return v4;
}
```

## dlgProc_AutoAim `0x10003146`

Named — see [doc 10](../../10-*.md). _14876 bytes. calls CreateWindowExA, MessageBoxA, SendDlgItemMessageA, SendMessageA; refs "aimgfb", "and still be able to hit enemies!!", "aimavalanche"_

```c
typedef struct struct_0 {
    char padding_0[32];
    char field_20;
    char padding_21[1023];
    char field_420;
    char padding_421[3];
    unsigned int field_424;
    char field_428;
    char padding_429[31];
    char field_448;
    char padding_449[1023];
    char field_848;
    char padding_849[3];
    unsigned int field_84c;
    char field_850;
    char padding_851[31];
    char field_870;
    char padding_871[1023];
    char field_c70;
    char padding_c71[3];
    unsigned int field_c74;
    char field_c78;
    char padding_c79[31];
    char field_c98;
    char padding_c99[1023];
    char field_1098;
    char padding_1099[7];
    char field_10a0;
    char padding_10a1[31];
    char field_10c0;
    char padding_10c1[1031];
    char field_14c8;
    char padding_14c9[31];
    char field_14e8;
    char padding_14e9[1031];
    char field_18f0;
    char padding_18f1[31];
    char field_1910;
    char padding_1911[1023];
    char field_1d10;
    char padding_1d11[3];
    unsigned int field_1d14;
    char field_1d18;
    char padding_1d19[31];
    char field_1d38;
    char padding_1d39[1023];
    char field_2138;
    char padding_2139[3];
    unsigned int field_213c;
    char field_2140;
    char padding_2141[31];
    char field_2160;
    char padding_2161[1023];
    char field_2560;
    char padding_2561[3];
    unsigned int field_2564;
    char field_2568;
    char padding_2569[31];
    char field_2588;
    char padding_2589[1023];
    char field_2988;
    char padding_2989[3];
    unsigned int field_298c;
    char field_2990;
    char padding_2991[31];
    char field_29b0;
    char padding_29b1[1023];
    char field_2db0;
    char padding_2db1[3];
    unsigned int field_2db4;
    char field_2db8;
    char padding_2db9[31];
    char field_2dd8;
    char padding_2dd9[1023];
    char field_31d8;
    char padding_31d9[3];
    unsigned int field_31dc;
    char field_31e0;
    char padding_31e1[31];
    char field_3200;
    char padding_3201[1023];
    char field_3600;
    char padding_3601[3];
    unsigned int field_3604;
    char field_3608;
    char padding_3609[31];
    char field_3628;
    char padding_3629[1023];
    char field_3a28;
    char padding_3a29[3];
    unsigned int field_3a2c;
    char field_3a30;
    char padding_3a31[31];
    char field_3a50;
    char padding_3a51[1023];
    char field_3e50;
    char padding_3e51[3];
    unsigned int field_3e54;
    char field_3e58;
    char padding_3e59[31];
    char field_3e78;
    char padding_3e79[1023];
    char field_4278;
    char padding_4279[3];
    unsigned int field_427c;
    char field_4280;
    char padding_4281[31];
    char field_42a0;
    char padding_42a1[1023];
    char field_46a0;
    char padding_46a1[3];
    unsigned int field_46a4;
    char field_46a8;
    char padding_46a9[31];
    char field_46c8;
    char padding_46c9[1023];
    char field_4ac8;
    char padding_4ac9[3];
    unsigned int field_4acc;
    char field_4ad0;
    char padding_4ad1[31];
    char field_4af0;
    char padding_4af1[1023];
    char field_4ef0;
    char padding_4ef1[3];
    unsigned int field_4ef4;
    char field_4ef8;
    char padding_4ef9[31];
    char field_4f18;
    char padding_4f19[1023];
    char field_5318;
    char padding_5319[3];
    unsigned int field_531c;
    char field_5320;
    char padding_5321[31];
    char field_5340;
    char padding_5341[1023];
    char field_5740;
    char padding_5741[3];
    unsigned int field_5744;
    char field_5748;
    char padding_5749[31];
    char field_5768;
    char padding_5769[1023];
    char field_5b68;
    char padding_5b69[3];
    unsigned int field_5b6c;
    char field_5b70;
    char padding_5b71[31];
    char field_5b90;
    char padding_5b91[1023];
    char field_5f90;
    char padding_5f91[3];
    unsigned int field_5f94;
    char field_5f98;
    char padding_5f99[31];
    char field_5fb8;
    char padding_5fb9[1023];
    char field_63b8;
    char padding_63b9[3];
    unsigned int field_63bc;
    char field_63c0;
    char padding_63c1[31];
    char field_63e0;
    char padding_63e1[1023];
    char field_67e0;
    char padding_67e1[3];
    unsigned int field_67e4;
    char field_67e8;
    char padding_67e9[31];
    char field_6808;
    char padding_6809[1023];
    char field_6c08;
    char padding_6c09[3];
    unsigned int field_6c0c;
    char field_6c10;
    char padding_6c11[31];
    char field_6c30;
    char padding_6c31[1023];
    char field_7030;
    char padding_7031[3];
    unsigned int field_7034;
    char field_7038;
    char padding_7039[31];
    char field_7058;
    char padding_7059[1023];
    char field_7458;
    char padding_7459[3];
    unsigned int field_745c;
    char field_7460;
    char padding_7461[31];
    char field_7480;
    char padding_7481[1023];
    char field_7880;
    char padding_7881[3];
    unsigned int field_7884;
    char field_7888;
    char padding_7889[31];
    char field_78a8;
    char padding_78a9[1023];
    char field_7ca8;
    char padding_7ca9[3];
    unsigned int field_7cac;
    char field_7cb0;
    char padding_7cb1[31];
    char field_7cd0;
    char padding_7cd1[1023];
    char field_80d0;
    char padding_80d1[3];
    unsigned int field_80d4;
    char field_80d8;
    char padding_80d9[31];
    char field_80f8;
    char padding_80f9[1023];
    char field_84f8;
    char padding_84f9[3];
    unsigned int field_84fc;
    char field_8500;
    char padding_8501[31];
    char field_8520;
    char padding_8521[1023];
    char field_8920;
    char padding_8921[3];
    unsigned int field_8924;
    char field_8928;
    char padding_8929[31];
    char field_8948;
    char padding_8949[1023];
    char field_8d48;
    char padding_8d49[3];
    unsigned int field_8d4c;
    char field_8d50;
    char padding_8d51[31];
    char field_8d70;
    char padding_8d71[1023];
    char field_9170;
    char padding_9171[3];
    unsigned int field_9174;
    char field_9178;
    char padding_9179[31];
    char field_9198;
    char padding_9199[1023];
    char field_9598;
    char padding_9599[3];
    unsigned int field_959c;
    char field_95a0;
    char padding_95a1[31];
    char field_95c0;
    char padding_95c1[1023];
    char field_99c0;
    char padding_99c1[3];
    unsigned int field_99c4;
    char field_99c8;
    char padding_99c9[31];
    char field_99e8;
    char padding_99e9[1023];
    char field_9de8;
    char padding_9de9[3];
    unsigned int field_9dec;
    char field_9df0;
    char padding_9df1[31];
    char field_9e10;
    char padding_9e11[1023];
    char field_a210;
    char padding_a211[3];
    unsigned int field_a214;
    char field_a218;
    char padding_a219[31];
    char field_a238;
    char padding_a239[1023];
    char field_a638;
    char padding_a639[3];
    unsigned int field_a63c;
    char field_a640;
    char padding_a641[31];
    char field_a660;
    char padding_a661[1023];
    char field_aa60;
    char padding_aa61[3];
    unsigned int field_aa64;
    char field_aa68;
    char padding_aa69[31];
    char field_aa88;
    char padding_aa89[1023];
    char field_ae88;
    char padding_ae89[3];
    unsigned int field_ae8c;
    char field_ae90;
    char padding_ae91[31];
    char field_aeb0;
    char padding_aeb1[1023];
    char field_b2b0;
    char padding_b2b1[3];
    unsigned int field_b2b4;
    char field_b2b8;
    char padding_b2b9[31];
    char field_b2d8;
    char padding_b2d9[1023];
    char field_b6d8;
    char padding_b6d9[3];
    unsigned int field_b6dc;
    char field_b6e0;
    char padding_b6e1[31];
    char field_b700;
    char padding_b701[1023];
    char field_bb00;
    char padding_bb01[3];
    unsigned int field_bb04;
    char field_bb08;
    char padding_bb09[31];
    char field_bb28;
    char padding_bb29[1023];
    char field_bf28;
    char padding_bf29[3];
    unsigned int field_bf2c;
    char field_bf30;
    char padding_bf31[31];
    char field_bf50;
    char padding_bf51[1023];
    char field_c350;
    char padding_c351[3];
    unsigned int field_c354;
    char field_c358;
    char padding_c359[31];
    char field_c378;
    char padding_c379[1023];
    char field_c778;
    char padding_c779[3];
    unsigned int field_c77c;
    char field_c780;
    char padding_c781[31];
    char field_c7a0;
    char padding_c7a1[1023];
    char field_cba0;
    char padding_cba1[3];
    unsigned int field_cba4;
    char field_cba8;
    char padding_cba9[31];
    char field_cbc8;
    char padding_cbc9[1023];
    char field_cfc8;
    char padding_cfc9[3];
    unsigned int field_cfcc;
    char field_cfd0;
    char padding_cfd1[31];
    char field_cff0;
    char padding_cff1[1023];
    char field_d3f0;
    char padding_d3f1[3];
    unsigned int field_d3f4;
    char field_d3f8;
    char padding_d3f9[31];
    char field_d418;
    char padding_d419[1023];
    char field_d818;
    char padding_d819[3];
    unsigned int field_d81c;
    char field_d820;
    char padding_d821[31];
    char field_d840;
    char padding_d841[1023];
    char field_dc40;
    char padding_dc41[3];
    unsigned int field_dc44;
    char field_dc48;
    char padding_dc49[31];
    char field_dc68;
    char padding_dc69[1023];
    char field_e068;
    char padding_e069[3];
    unsigned int field_e06c;
    char field_e070;
    char padding_e071[31];
    char field_e090;
    char padding_e091[1023];
    char field_e490;
    char padding_e491[3];
    unsigned int field_e494;
    char field_e498;
    char padding_e499[31];
    char field_e4b8;
    char padding_e4b9[1023];
    char field_e8b8;
    char padding_e8b9[3];
    unsigned int field_e8bc;
    char field_e8c0;
    char padding_e8c1[31];
    char field_e8e0;
    char padding_e8e1[1023];
    char field_ece0;
    char padding_ece1[3];
    unsigned int field_ece4;
    char field_ece8;
    char padding_ece9[31];
    char field_ed08;
    char padding_ed09[1031];
    char field_f110;
    char padding_f111[31];
    char field_f130;
    char padding_f131[1031];
    char field_f538;
    char padding_f539[31];
    char field_f558;
    char padding_f559[1031];
    char field_f960;
    char padding_f961[31];
    char field_f980;
    char padding_f981[1031];
    char field_fd88;
    char padding_fd89[31];
    char field_fda8;
    char padding_fda9[1031];
    char field_101b0;
    char padding_101b1[31];
    char field_101d0;
    char padding_101d1[1031];
    char field_105d8;
    char padding_105d9[31];
    char field_105f8;
    char padding_105f9[1031];
    char field_10a00;
    char padding_10a01[31];
    char field_10a20;
    char padding_10a21[1031];
    char field_10e28;
    char padding_10e29[31];
    char field_10e48;
    char padding_10e49[1031];
    char field_11250;
    char padding_11251[31];
    char field_11270;
    char padding_11271[1031];
    char field_11678;
    char padding_11679[31];
    char field_11698;
    char padding_11699[1031];
    char field_11aa0;
    char padding_11aa1[31];
    char field_11ac0;
    char padding_11ac1[1031];
    char field_11ec8;
    char padding_11ec9[31];
    char field_11ee8;
    char padding_11ee9[1031];
    char field_122f0;
    char padding_122f1[31];
    char field_12310;
    char padding_12311[1031];
    char field_12718;
    char padding_12719[31];
    char field_12738;
    char padding_12739[1031];
    char field_12b40;
    char padding_12b41[31];
    char field_12b60;
    char padding_12b61[1031];
    char field_12f68;
    char padding_12f69[31];
    char field_12f88;
    char padding_12f89[1031];
    char field_13390;
    char padding_13391[31];
    char field_133b0;
    char padding_133b1[1031];
    char field_137b8;
    char padding_137b9[31];
    char field_137d8;
    char padding_137d9[1031];
    char field_13be0;
    char padding_13be1[31];
    char field_13c00;
    char padding_13c01[1031];
    char field_14008;
    char padding_14009[31];
    char field_14028;
    char padding_14029[1031];
    char field_14430;
    char padding_14431[31];
    char field_14450;
    char padding_14451[1031];
    char field_14858;
    char padding_14859[31];
    char field_14878;
    char padding_14879[1031];
    char field_14c80;
    char padding_14c81[31];
    char field_14ca0;
    char padding_14ca1[1031];
    char field_150a8;
    char padding_150a9[31];
    char field_150c8;
    char padding_150c9[1031];
    char field_154d0;
    char padding_154d1[31];
    char field_154f0;
    char padding_154f1[1031];
    char field_158f8;
    char padding_158f9[31];
    char field_15918;
    char padding_15919[1031];
    char field_15d20;
    char padding_15d21[31];
    char field_15d40;
    char padding_15d41[1031];
    char field_16148;
    char padding_16149[31];
    char field_16168;
    char padding_16169[1031];
    char field_16570;
    char padding_16571[31];
    char field_16590;
    char padding_16591[1031];
    char field_16998;
    char padding_16999[31];
    char field_169b8;
    char padding_169b9[1027];
    unsigned int field_16dbc;
    char field_16dc0;
    char padding_16dc1[31];
    char field_16de0;
    char padding_16de1[1023];
    char field_171e0;
    char padding_171e1[3];
    unsigned int field_171e4;
    char field_171e8;
    char padding_171e9[31];
    char field_17208;
    char padding_17209[1023];
    char field_17608;
    char padding_17609[3];
    unsigned int field_1760c;
    char field_17610;
    char padding_17611[31];
    char field_17630;
    char padding_17631[1023];
    char field_17a30;
    char padding_17a31[3];
    unsigned int field_17a34;
    char field_17a38;
    char padding_17a39[31];
    char field_17a58;
    char padding_17a59[1023];
    char field_17e58;
    char padding_17e59[3];
    unsigned int field_17e5c;
    char field_17e60;
    char padding_17e61[31];
    char field_17e80;
    char padding_17e81[1023];
    char field_18280;
    char padding_18281[3];
    unsigned int field_18284;
    char field_18288;
    char padding_18289[31];
    char field_182a8;
    char padding_182a9[1023];
    char field_186a8;
    char padding_186a9[3];
    unsigned int field_186ac;
    char field_186b0;
    char padding_186b1[31];
    char field_186d0;
    char padding_186d1[1023];
    char field_18ad0;
    char padding_18ad1[3];
    unsigned int field_18ad4;
    char field_18ad8;
    char padding_18ad9[31];
    char field_18af8;
    char padding_18af9[1023];
    char field_18ef8;
    char padding_18ef9[3];
    unsigned int field_18efc;
    char field_18f00;
    char padding_18f01[31];
    char field_18f20;
    char padding_18f21[1023];
    char field_19320;
    char padding_19321[3];
    unsigned int field_19324;
    char field_19328;
    char padding_19329[31];
    char field_19348;
    char padding_19349[1023];
    char field_19748;
    char padding_19749[3];
    unsigned int field_1974c;
    char field_19750;
    char padding_19751[31];
    char field_19770;
    char padding_19771[1023];
    char field_19b70;
    char padding_19b71[3];
    unsigned int field_19b74;
    char field_19b78;
    char padding_19b79[31];
    char field_19b98;
    char padding_19b99[1023];
    char field_19f98;
    char padding_19f99[3];
    unsigned int field_19f9c;
    char field_19fa0;
    char padding_19fa1[31];
    char field_19fc0;
    char padding_19fc1[1023];
    char field_1a3c0;
    char padding_1a3c1[3];
    unsigned int field_1a3c4;
    char field_1a3c8;
    char padding_1a3c9[31];
    char field_1a3e8;
    char padding_1a3e9[1023];
    char field_1a7e8;
    char padding_1a7e9[3];
    unsigned int field_1a7ec;
    char field_1a7f0;
    char padding_1a7f1[31];
    char field_1a810;
    char padding_1a811[1023];
    char field_1ac10;
    char padding_1ac11[3];
    unsigned int field_1ac14;
    char field_1ac18;
    char padding_1ac19[31];
    char field_1ac38;
    char padding_1ac39[1023];
    char field_1b038;
    char padding_1b039[3];
    unsigned int field_1b03c;
    char field_1b040;
    char padding_1b041[31];
    char field_1b060;
    char padding_1b061[1023];
    char field_1b460;
    char padding_1b461[3];
    unsigned int field_1b464;
    char field_1b468;
    char padding_1b469[31];
    char field_1b488;
    char padding_1b489[1023];
    char field_1b888;
    char padding_1b889[3];
    unsigned int field_1b88c;
    char field_1b890;
    char padding_1b891[31];
    char field_1b8b0;
    char padding_1b8b1[1023];
    char field_1bcb0;
    char padding_1bcb1[3];
    unsigned int field_1bcb4;
    char field_1bcb8;
    char padding_1bcb9[31];
    char field_1bcd8;
    char padding_1bcd9[1023];
    char field_1c0d8;
    char padding_1c0d9[3];
    unsigned int field_1c0dc;
    char field_1c0e0;
    char padding_1c0e1[31];
    char field_1c100;
    char padding_1c101[1023];
    char field_1c500;
    char padding_1c501[3];
    unsigned int field_1c504;
    char field_1c508;
    char padding_1c509[31];
    char field_1c528;
    char padding_1c529[1023];
    char field_1c928;
    char padding_1c929[3];
    unsigned int field_1c92c;
    char field_1c930;
    char padding_1c931[31];
    char field_1c950;
    char padding_1c951[1023];
    char field_1cd50;
    char padding_1cd51[3];
    unsigned int field_1cd54;
    char field_1cd58;
    char padding_1cd59[31];
    char field_1cd78;
    char padding_1cd79[1023];
    char field_1d178;
    char padding_1d179[3];
    unsigned int field_1d17c;
    char field_1d180;
    char padding_1d181[31];
    char field_1d1a0;
    char padding_1d1a1[1023];
    char field_1d5a0;
    char padding_1d5a1[3];
    unsigned int field_1d5a4;
    char field_1d5a8;
    char padding_1d5a9[31];
    char field_1d5c8;
    char padding_1d5c9[1023];
    char field_1d9c8;
    char padding_1d9c9[3];
    unsigned int field_1d9cc;
    char field_1d9d0;
    char padding_1d9d1[31];
    char field_1d9f0;
    char padding_1d9f1[1023];
    char field_1ddf0;
    char padding_1ddf1[3];
    unsigned int field_1ddf4;
    char field_1ddf8;
    char padding_1ddf9[31];
    char field_1de18;
    char padding_1de19[1023];
    char field_1e218;
    char padding_1e219[3];
    unsigned int field_1e21c;
    char field_1e220;
    char padding_1e221[31];
    char field_1e240;
    char padding_1e241[1023];
    char field_1e640;
    char padding_1e641[3];
    unsigned int field_1e644;
    char field_1e648;
    char padding_1e649[31];
    char field_1e668;
    char padding_1e669[1023];
    char field_1ea68;
    char padding_1ea69[3];
    unsigned int field_1ea6c;
    char field_1ea70;
    char padding_1ea71[31];
    char field_1ea90;
    char padding_1ea91[1023];
    char field_1ee90;
    char padding_1ee91[3];
    unsigned int field_1ee94;
    char field_1ee98;
    char padding_1ee99[31];
    char field_1eeb8;
    char padding_1eeb9[1023];
    char field_1f2b8;
    char padding_1f2b9[3];
    unsigned int field_1f2bc;
    char field_1f2c0;
    char padding_1f2c1[31];
    char field_1f2e0;
    char padding_1f2e1[1023];
    char field_1f6e0;
    char padding_1f6e1[3];
    unsigned int field_1f6e4;
    char field_1f6e8;
    char padding_1f6e9[31];
    char field_1f708;
    char padding_1f709[1023];
    char field_1fb08;
    char padding_1fb09[3];
    unsigned int field_1fb0c;
    char field_1fb10;
    char padding_1fb11[31];
    char field_1fb30;
    char padding_1fb31[1023];
    char field_1ff30;
    char padding_1ff31[3];
    unsigned int field_1ff34;
    char field_1ff38;
    char padding_1ff39[31];
    char field_1ff58;
    char padding_1ff59[1023];
    char field_20358;
    char padding_20359[3];
    unsigned int field_2035c;
    char padding_20360[1064];
    char field_20788;
    char padding_20789[31];
    char field_207a8;
    char padding_207a9[1023];
    char field_20ba8;
    char padding_20ba9[3];
    unsigned int field_20bac;
    char field_20bb0;
    char padding_20bb1[31];
    char field_20bd0;
    char padding_20bd1[1023];
    char field_20fd0;
    char padding_20fd1[3];
    unsigned int field_20fd4;
    char field_20fd8;
    char padding_20fd9[31];
    char field_20ff8;
    char padding_20ff9[1023];
    char field_213f8;
    char padding_213f9[3];
    unsigned int field_213fc;
    char field_21400;
    char padding_21401[31];
    char field_21420;
    char padding_21421[1023];
    char field_21820;
    char padding_21821[3];
    unsigned int field_21824;
    char field_21828;
    char padding_21829[31];
    char field_21848;
    char padding_21849[1023];
    char field_21c48;
    char padding_21c49[3];
    unsigned int field_21c4c;
    char field_21c50;
    char padding_21c51[31];
    char field_21c70;
    char padding_21c71[1023];
    char field_22070;
    char padding_22071[3];
    unsigned int field_22074;
    char field_22078;
    char padding_22079[31];
    char field_22098;
    char padding_22099[1023];
    char field_22498;
    char padding_22499[3];
    unsigned int field_2249c;
    char field_224a0;
    char padding_224a1[31];
    char field_224c0;
    char padding_224c1[1023];
    char field_228c0;
    char padding_228c1[3];
    unsigned int field_228c4;
    char field_228c8;
    char padding_228c9[31];
    char field_228e8;
    char padding_228e9[1023];
    char field_22ce8;
    char padding_22ce9[3];
    unsigned int field_22cec;
    char field_22cf0;
    char padding_22cf1[31];
    char field_22d10;
    char padding_22d11[1023];
    char field_23110;
    char padding_23111[3];
    unsigned int field_23114;
    char field_23118;
    char padding_23119[31];
    char field_23138;
    char padding_23139[1023];
    char field_23538;
    char padding_23539[3];
    unsigned int field_2353c;
    char field_23540;
    char padding_23541[31];
    char field_23560;
    char padding_23561[1023];
    char field_23960;
    char padding_23961[3];
    unsigned int field_23964;
    char field_23968;
    char padding_23969[31];
    char field_23988;
    char padding_23989[1023];
    char field_23d88;
    char padding_23d89[3];
    unsigned int field_23d8c;
    char field_23d90;
    char padding_23d91[31];
    char field_23db0;
    char padding_23db1[1023];
    char field_241b0;
    char padding_241b1[3];
    unsigned int field_241b4;
    char field_241b8;
    char padding_241b9[31];
    char field_241d8;
    char padding_241d9[1023];
    char field_245d8;
    char padding_245d9[3];
    unsigned int field_245dc;
    char field_245e0;
    char padding_245e1[31];
    char field_24600;
    char padding_24601[1023];
    char field_24a00;
    char padding_24a01[3];
    unsigned int field_24a04;
    char field_24a08;
    char padding_24a09[31];
    char field_24a28;
    char padding_24a29[1023];
    char field_24e28;
    char padding_24e29[3];
    unsigned int field_24e2c;
    char field_24e30;
    char padding_24e31[31];
    char field_24e50;
    char padding_24e51[1023];
    char field_25250;
    char padding_25251[3];
    unsigned int field_25254;
    char field_25258;
    char padding_25259[31];
    char field_25278;
    char padding_25279[1023];
    char field_25678;
    char padding_25679[3];
    unsigned int field_2567c;
    char field_25680;
    char padding_25681[31];
    char field_256a0;
    char padding_256a1[1023];
    char field_25aa0;
    char padding_25aa1[3];
    unsigned int field_25aa4;
    char field_25aa8;
    char padding_25aa9[31];
    char field_25ac8;
    char padding_25ac9[1023];
    char field_25ec8;
    char padding_25ec9[3];
    unsigned int field_25ecc;
    char field_25ed0;
    char padding_25ed1[31];
    char field_25ef0;
    char padding_25ef1[1023];
    char field_262f0;
    char padding_262f1[3];
    unsigned int field_262f4;
    char field_262f8;
    char padding_262f9[31];
    char field_26318;
    char padding_26319[1023];
    char field_26718;
    char padding_26719[3];
    unsigned int field_2671c;
    char field_26720;
    char padding_26721[31];
    char field_26740;
    char padding_26741[1023];
    char field_26b40;
    char padding_26b41[3];
    unsigned int field_26b44;
    char field_26b48;
    char padding_26b49[31];
    char field_26b68;
    char padding_26b69[1023];
    char field_26f68;
    char padding_26f69[3];
    unsigned int field_26f6c;
    char field_26f70;
    char padding_26f71[31];
    char field_26f90;
    char padding_26f91[1023];
    char field_27390;
    char padding_27391[3];
    unsigned int field_27394;
    char field_27398;
    char padding_27399[31];
    char field_273b8;
    char padding_273b9[1023];
    char field_277b8;
    char padding_277b9[3];
    unsigned int field_277bc;
    char field_277c0;
    char padding_277c1[31];
    char field_277e0;
    char padding_277e1[1023];
    char field_27be0;
    char padding_27be1[3];
    unsigned int field_27be4;
    char field_27be8;
    char padding_27be9[31];
    char field_27c08;
    char padding_27c09[1023];
    char field_28008;
    char padding_28009[3];
    unsigned int field_2800c;
    char field_28010;
    char padding_28011[31];
    char field_28030;
    char padding_28031[1023];
    char field_28430;
    char padding_28431[3];
    unsigned int field_28434;
    char field_28438;
    char padding_28439[31];
    char field_28458;
    char padding_28459[1023];
    char field_28858;
    char padding_28859[3];
    unsigned int field_2885c;
    char field_28860;
    char padding_28861[31];
    char field_28880;
    char padding_28881[1023];
    char field_28c80;
    char padding_28c81[3];
    unsigned int field_28c84;
    char field_28c88;
    char padding_28c89[31];
    char field_28ca8;
    char padding_28ca9[1023];
    char field_290a8;
    char padding_290a9[3];
    unsigned int field_290ac;
    char field_290b0;
    char padding_290b1[31];
    char field_290d0;
    char padding_290d1[1023];
    char field_294d0;
    char padding_294d1[3];
    unsigned int field_294d4;
    char field_294d8;
    char padding_294d9[31];
    char field_294f8;
    char padding_294f9[1023];
    char field_298f8;
    char padding_298f9[3];
    unsigned int field_298fc;
    char field_29900;
    char padding_29901[31];
    char field_29920;
    char padding_29921[1023];
    char field_29d20;
    char padding_29d21[3];
    unsigned int field_29d24;
    char field_29d28;
    char padding_29d29[31];
    char field_29d48;
    char padding_29d49[1023];
    char field_2a148;
    char padding_2a149[3];
    unsigned int field_2a14c;
    char field_2a150;
    char padding_2a151[31];
    char field_2a170;
    char padding_2a171[1023];
    char field_2a570;
    char padding_2a571[3];
    unsigned int field_2a574;
    char field_2a578;
    char padding_2a579[31];
    char field_2a598;
    char padding_2a599[1023];
    char field_2a998;
    char padding_2a999[3];
    unsigned int field_2a99c;
    char field_2a9a0;
    char padding_2a9a1[31];
    char field_2a9c0;
    char padding_2a9c1[1023];
    char field_2adc0;
    char padding_2adc1[3];
    unsigned int field_2adc4;
    char field_2adc8;
    char padding_2adc9[31];
    char field_2ade8;
    char padding_2ade9[1023];
    char field_2b1e8;
    char padding_2b1e9[3];
    unsigned int field_2b1ec;
    char field_2b1f0;
    char padding_2b1f1[31];
    char field_2b210;
    char padding_2b211[1023];
    char field_2b610;
    char padding_2b611[3];
    unsigned int field_2b614;
} struct_0;

extern unsigned int g_10042929;
extern char g_10042d7b;
extern int g_10042e7f;
extern char g_10042f83;
extern unsigned int g_100445f1;
extern char g_1005dc8c;
extern struct_0 *g_1005e194;
extern unsigned int g_1005e198;
extern char g_1005f609;
extern HINSTANCE g_1005f60a;
extern unsigned int g_1005f616;
extern unsigned int g_1005f626;
extern char g_1005f651;
extern int g_10072f70;
extern int g_10072f74;
extern int g_10072f78;
extern int g_10072f7c;
extern void g_10072f80;
extern int g_10072f84;
extern void g_10072f88;
extern int g_10072f8c;
extern int g_10072f90;
extern int g_10072f94;
extern void g_10072fb8;
extern void g_10072fbc;
extern HWND g_10072fc0;
extern void g_10072fc4;
extern int g_10072fcc;
extern char g_100f9315;
extern unsigned int g_100f9495;
extern unsigned int g_100f9499;
extern unsigned int g_100f949d;
extern unsigned int g_100f94c1;
extern char g_100f94c6;
extern char g_100f94c7;
extern char g_100f94c8;
extern char g_100f94c9;
extern char g_100f94ca;
extern unsigned int g_100f94cb;
extern char g_100fa4ef;
extern char g_100fa4f0;
extern int g_100fa4f1;
extern int g_100fa531;
extern unsigned int g_100fa571;
extern unsigned int g_100fa575;
extern char g_100fa579;
extern char g_100fa97a;
extern char g_100fa97b;
extern int g_1012ad5f;
extern int g_1012fd60;
extern char g_10134e63;
extern char g_10134e64;
extern char g_10134e65;
extern unsigned int g_10134e66;
extern char g_10134e6a;
extern int g_10134e6b;
extern char g_1013526b;
extern char g_1013526d;
extern char g_1013526e;
extern char g_1013526f;
extern char g_10135270;
extern char g_10135271;
extern char g_10135272;
extern char g_10135273;
extern char g_10135274;
extern char g_10135275;
extern char g_10135276;
extern char g_10135277;
extern char g_10135278;
extern char g_1013527a;
extern int g_1013527b;
extern int g_1013a27c;
extern char g_1013f27d;
extern char g_1013f27e;
extern char g_1013f27f;
extern unsigned int g_1013f320;
extern char g_1013f324;
extern char g_1013f325;
extern char g_1013f326;
extern int g_1014f38a;
extern int g_1014f3aa;
extern int g_1014f3ca;
extern int g_1014f3ea;
extern char g_1014f40a;
extern char g_1014f40b;
extern char g_1014f40c;
extern char g_1014f40d;
extern char g_1014f40e;
extern char g_1014f40f;
extern unsigned int g_1014f410;
extern char g_1014f415;
extern char g_1014f416;
extern char g_1014f417;
extern char g_1014f418;
extern char g_1014f419;
extern unsigned int g_1014f41a;
extern char g_1014f41e;
extern char g_1014f41f;
extern char g_101d5e20;
extern char g_101d5e21;
extern char g_101d5e27;
extern char g_101d5e29;
extern char g_101d5e2a;
extern int g_101d5e2c;
extern int g_101d5e4c;
extern char g_101d5e6c;
extern char g_101d5e6d;
extern char g_101d5e6e;
extern char g_101d5e6f;
extern char g_101d5e70;
extern char g_101d5e71;
extern char g_101d5e72;
extern char g_101d5e73;
extern unsigned int g_63fe5c;

int sub_10003146(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v4;  // eax
    unsigned int v5;  // eax
    unsigned int idx;  // ebx
    unsigned int idx1;  // ebx
    unsigned int idx2;  // ebx
    unsigned int v106;  // ebx
    unsigned int v107;  // ebx
    unsigned int v108;  // ebx
    unsigned int v109;  // ebx
    unsigned int v110;  // ebx
    unsigned int v111;  // ebx
    unsigned int v112;  // ebx
    unsigned int v113;  // ebx
    unsigned int v15;  // ebx
    unsigned int v114;  // ebx
    unsigned int v115;  // ebx
    unsigned int v116;  // ebx
    unsigned int v117;  // ebx
    unsigned int v118;  // ebx
    unsigned int v119;  // ebx
    unsigned int v120;  // ebx
    unsigned int v121;  // ebx
    unsigned int v122;  // ebx
    unsigned int v123;  // ebx
    unsigned int v16;  // ebx
    unsigned int v124;  // ebx
    unsigned int v125;  // ebx
    unsigned int v126;  // ebx
    unsigned int v127;  // ebx
    unsigned int v128;  // ebx
    unsigned int v129;  // ebx
    unsigned int v130;  // ebx
    unsigned int v131;  // ebx
    unsigned int v132;  // ebx
    unsigned int v133;  // ebx
    unsigned int v17;  // ebx
    unsigned int v134;  // ebx
    unsigned int v135;  // ebx
    unsigned int v136;  // ebx
    unsigned int v137;  // ebx
    unsigned int v138;  // ebx
    unsigned int v139;  // ebx
    unsigned int v140;  // ebx
    unsigned int v141;  // ebx
    unsigned int v142;  // ebx
    unsigned int v143;  // ebx
    unsigned int v18;  // ebx
    unsigned int v144;  // ebx
    unsigned int v145;  // ebx
    unsigned int v146;  // ebx
    unsigned int v147;  // ebx
    unsigned int v148;  // ebx
    unsigned int v149;  // ebx
    unsigned int v150;  // ebx
    unsigned int v151;  // ebx
    unsigned int v152;  // ebx
    unsigned int v153;  // ebx
    unsigned int v19;  // ebx
    unsigned int v154;  // ebx
    unsigned int v155;  // ebx
    unsigned int v156;  // ebx
    unsigned int v157;  // ebx
    unsigned int v158;  // ebx
    unsigned int v159;  // ebx
    unsigned int v160;  // ebx
    unsigned int v161;  // ebx
    unsigned int v162;  // ebx
    unsigned int v163;  // ebx
    unsigned int v20;  // ebx
    unsigned int v164;  // ebx
    unsigned int v165;  // ebx
    unsigned int v166;  // ebx
    unsigned int v167;  // ebx
    unsigned int v168;  // ebx
    unsigned int v169;  // ebx
    unsigned int v170;  // ebx
    unsigned int i;  // ebx
    LRESULT count;  // eax
    LRESULT count1;  // eax
    unsigned int v21;  // ebx
    LRESULT count2;  // eax
    LRESULT v175;  // eax
    LRESULT v176;  // eax
    LRESULT v177;  // eax
    LRESULT v178;  // eax
    LRESULT v179;  // eax
    LRESULT v180;  // eax
    unsigned int v22;  // ebx
    unsigned int v23;  // ebx
    unsigned int v6;  // ebx
    unsigned int v24;  // ebx
    unsigned int v25;  // ebx
    unsigned int v26;  // ebx
    unsigned int v27;  // ebx
    unsigned int v28;  // ebx
    unsigned int v29;  // ebx
    unsigned int v30;  // ebx
    unsigned int v31;  // ebx
    unsigned int v32;  // ebx
    unsigned int v33;  // ebx
    unsigned int index;  // ebx
    unsigned int v34;  // ebx
    unsigned int v35;  // ebx
    unsigned int v36;  // ebx
    unsigned int v37;  // ebx
    unsigned int v38;  // ebx
    unsigned int v39;  // ebx
    unsigned int v40;  // ebx
    unsigned int v41;  // ebx
    unsigned int v42;  // ebx
    unsigned int v43;  // ebx
    unsigned int v8;  // ebx
    unsigned int v44;  // ebx
    unsigned int v45;  // ebx
    unsigned int v46;  // ebx
    unsigned int v47;  // ebx
    unsigned int v48;  // ebx
    unsigned int v49;  // ebx
    unsigned int v50;  // ebx
    unsigned int v51;  // ebx
    unsigned int v52;  // ebx
    unsigned int v53;  // ebx
    unsigned int v9;  // ebx
    unsigned int v54;  // ebx
    unsigned int v55;  // ebx
    unsigned int v56;  // ebx
    unsigned int v57;  // ebx
    unsigned int v58;  // ebx
    unsigned int v59;  // ebx
    unsigned int v60;  // ebx
    unsigned int v61;  // ebx
    unsigned int v62;  // ebx
    unsigned int v63;  // ebx
    unsigned int v10;  // ebx
    unsigned int v64;  // ebx
    unsigned int v65;  // ebx
    unsigned int v66;  // ebx
    unsigned int v67;  // ebx
    unsigned int v68;  // ebx
    unsigned int v69;  // ebx
    unsigned int v70;  // ebx
    unsigned int v71;  // ebx
    unsigned int v72;  // ebx
    unsigned int v73;  // ebx
    unsigned int v11;  // ebx
    unsigned int v74;  // ebx
    unsigned int v75;  // ebx
    unsigned int v76;  // ebx
    unsigned int v77;  // ebx
    unsigned int v78;  // ebx
    unsigned int v79;  // ebx
    unsigned int v80;  // ebx
    unsigned int v81;  // ebx
    unsigned int v82;  // ebx
    unsigned int v83;  // ebx
    unsigned int v12;  // ebx
    unsigned int v84;  // ebx
    unsigned int v85;  // ebx
    unsigned int v86;  // ebx
    unsigned int v87;  // ebx
    unsigned int v88;  // ebx
    unsigned int v89;  // ebx
    unsigned int v90;  // ebx
    unsigned int v91;  // ebx
    unsigned int v92;  // ebx
    unsigned int v93;  // ebx
    unsigned int v13;  // ebx
    unsigned int v94;  // ebx
    unsigned int v95;  // ebx
    unsigned int v96;  // ebx
    unsigned int v97;  // ebx
    unsigned int v98;  // ebx
    unsigned int v99;  // ebx
    unsigned int v100;  // ebx
    unsigned int v101;  // ebx
    unsigned int v102;  // ebx
    unsigned int v103;  // ebx
    unsigned int v0;  // [bp-0x440]
    unsigned int v1;  // [bp-0x43c]
    int v2;  // [bp-0x438]
    int v3;  // [bp-0x434]

    v4 = a1;
    if (v4 != 174 && v4 != 1337 && v4 != 12 && v4 != 13)
        if (v4 == 14)
            goto LABEL_1000316f;
        else
            goto LABEL_1000316f;
LABEL_1000316f:
    v5 = a1;
    if (v5 == 272)
    {
        v1 = a0;
        g_1005f626 = a0;
        g_1005e194 = GlobalAlloc(GPTR, 0x42800);
        lstrcpy(g_1005e194, "aimgfb");
        lstrcat(&g_1005e194->field_20, "will compute the best square to shoot a GFB so that it hits most enemies and ZERO friends and shoots it, by also considering protection zones and shot tracing if activated. It will never hit a friend (unless due to lag). If it is not possible to hit ");
        lstrcat(&g_1005e194->field_20, "enemies without hitting friends, the command will instead cast 'autoaim' and hit an enemy instead with the rune specified in 'Aim Type'. Since it does complete targeting computations, it may be possible to block yourself from attacks with magic walls ");
        lstrcat(&g_1005e194->field_20, "and still be able to hit enemies!!");
        g_1005e194->field_420 = 0;
        g_1005e194->field_424 = 0;
        v6 = &g_1005e194->field_428;
        lstrcpy(v6, "aimavalanche");
        lstrcat(v6 + 32, "will compute the best square to shoot an avalanche rune so that it hits most enemies and ZERO friends and shoots it, by also considering protection zones and shot tracing if activated. It will never hit a friend (unless due to lag). If it is not ");
        lstrcat(v6 + 32, "possible to hit enemies without hitting friends, the command will instead cast 'autoaim' and hit an enemy instead with the rune specified in 'Aim Type'. Since it does complete targeting computations, it may be possible to block yourself from attacks ");
        lstrcat(v6 + 32, "with magic walls and still be able to hit enemies!!");
        *((char *)(v6 + 1056)) = 0;
        *((unsigned int *)(v6 + 1060)) = 0;
        index = v6 + 1064;
        lstrcpy(index, "aimthunderstorm");
        lstrcat(index + 32, "will compute the best square to shoot an thunderstorm rune so that it hits most enemies and ZERO friends and shoots it, by also considering protection zones and shot tracing if activated. It will never hit a friend (unless due to lag). If it is not ");
        lstrcat(index + 32, "possible to hit enemies without hitting friends, the command will instead cast 'autoaim' and hit an enemy instead with the rune specified in 'Aim Type'. Since it does complete targeting computations, it may be possible to block yourself from attacks ");
        lstrcat(index + 32, "with magic walls and still be able to hit enemies!!");
        *((char *)(index + 1056)) = 0;
        *((unsigned int *)(index + 1060)) = 0;
        v8 = index + 1064;
        lstrcpy(v8, "aimstoneshower");
        lstrcat(v8 + 32, "will compute the best square to shoot an stone shower rune so that it hits most enemies and ZERO friends and shoots it, by also considering protection zones and shot tracing if activated. It will never hit a friend (unless due to lag). If it is not ");
        lstrcat(v8 + 32, "possible to hit enemies without hitting friends, the command will instead cast 'autoaim' and hit an enemy instead with the rune specified in 'Aim Type'. Since it does complete targeting computations, it may be possible to block yourself from attacks ");
        lstrcat(v8 + 32, "with magic walls and still be able to hit enemies!!");
        *((char *)(v8 + 1056)) = 0;
        *((unsigned int *)(v8 + 1060)) = 0;
        v9 = v8 + 1064;
        lstrcpy(v9, "aimtype");
        lstrcat(v9 + 32, "uses the Action/spell that is set in the aimbot section on a certain creature");
        lstrcat(v9 + 32, "\n\r\n\rExample: aimtype Dragon - uses the action/spell selected in the Aimbot section of the bot on a Dragon");
        *((char *)(v9 + 1056)) = 0;
        *((unsigned int *)(v9 + 1060)) = 1;
        v10 = v9 + 1064;
        lstrcpy(v10, "altnavdisplay");
        lstrcat(v10 + 32, "an alternative way of displaying navigation friends' and enemies' location. With this turned on, players will be displayed as little dots as if they are being located on a map. Leave this on auto or just hold down a key binded to it for a quick ");
        lstrcat(v10 + 32, "glimpse.");
        *((char *)(v10 + 1056)) = 1;
        *((unsigned int *)(v10 + 1060)) = 0;
        v11 = v10 + 1064;
        lstrcpy(v11, "attack");
        lstrcat(v11 + 32, "attacks a creature");
        lstrcat(v11 + 32, "\n\r\n\rExample: attack Dragon - attacks a Dragon on the screen, that depending on options may be the one with least hp and currently reachable. It could be used on 'auto' if you're lazy!");
        *((char *)(v11 + 1056)) = 0;
        *((unsigned int *)(v11 + 1060)) = 1;
        v12 = v11 + 1064;
        lstrcpy(v12, "autoaim");
        lstrcat(v12 + 32, "The native bot aim mechanism with consideration for most of the combined features. It's an offensive command that performs the action specified in 'Aim Type' field in the aimbot section on the best target. If you have a combo leader, it will focus ");
        lstrcat(v12 + 32, "fire on the leader's target if possible, otherwise it will select the best target from the enemy list. This accounts for some fast and synchronised team attacks and decision making.");
        *((char *)(v12 + 1056)) = 0;
        *((unsigned int *)(v12 + 1060)) = 0;
        v13 = v12 + 1064;
        lstrcpy(v13, "autoheal");
        lstrcat(v13 + 32, "forces healing of yourself if your hp is below 95%. Uses the spell in 'Spell Lo' field of the bot if possible, otherwise an uh Rune. This is useful if you get trapped and heavily spammed, since you will heal as soon as you lose some hp, but not ");
        lstrcat(v13 + 32, "for nothing thus not resulting in wasting your turn.");
        *((char *)(v13 + 1056)) = 4;
        *((unsigned int *)(v13 + 1060)) = 0;
        idx = v13 + 1064;
        lstrcpy(idx, "buyitems");
        lstrcat(idx + 32, "buys a specific amount of a certain item from an NPC. The npc must have a trade initiated with him beforehand");
        lstrcat(idx + 32, "\n\r\n\rExample: buyitems 1234 5 - buys 5 items of id 1234 from the NPC.");
        *((char *)(idx + 1056)) = 3;
        *((unsigned int *)(idx + 1060)) = 25154;
        v15 = idx + 1064;
        lstrcpy(v15, "buyitemsupto");
        lstrcat(v15 + 32, "buys a specific amount of a certain item from an NPC up to a certain total desired amount depending on how many you already have. You must count the items with 'countitems' or 'countitemsvisible' and the npc must have a trade ");
        lstrcat(v15 + 32, "initiated with him beforehand");
        *((char *)(v15 + 1056)) = 3;
        *((unsigned int *)(v15 + 1060)) = 25154;
        v16 = v15 + 1064;
        lstrcpy(v16, "closeallwindows");
        lstrcat(v16 + 32, "closes all open windows so that you may start anew");
        *((char *)(v16 + 1056)) = 3;
        *((unsigned int *)(v16 + 1060)) = 0;
        v17 = v16 + 1064;
        lstrcpy(v17, "countitems");
        lstrcat(v17 + 32, "counts the number of items and gets a server 'Using one of...' response. To be used by a following 'countlower' or 'counthigher' conditional command.");
        lstrcat(v17 + 32, "\n\r\n\rExample: countitems 1234 - counts the number of type 1234");
        *((char *)(v17 + 1056)) = 5;
        *((unsigned int *)(v17 + 1060)) = 66;
        v18 = v17 + 1064;
        lstrcpy(v18, "countitemsvisible");
        lstrcat(v18 + 32, "counts the number of items that are visible in your open windows and equipped inventory on the client side (does not need a server response and is this instantaneous). To be used by a following 'countlower' or 'counthigher' conditional command.");
        lstrcat(v18 + 32, "\n\r\n\rExample: countitemsvisible 1234 - counts the number of items of type 1234 that are visible");
        *((char *)(v18 + 1056)) = 5;
        *((unsigned int *)(v18 + 1060)) = 66;
        v19 = v18 + 1064;
        lstrcpy(v19, "dash");
        lstrcat(v19 + 32, "an exploit that makes you run significantly faster than you normally can. Works best for strong hasted mages.");
        lstrcat(v19 + 32, "\n\r\n\rYou must use the arrow keys to choose dashing direction and hold the hotkey that has 'dash' assigned to it for as long as you want to advance.");
        lstrcat(v19 + 32, "Try it on fast tiles such as in Venore or Thais. This is safe to use (so long as you don't do it in front of a GM and brag about it!)");
        *((char *)(v19 + 1056)) = 2;
        *((unsigned int *)(v19 + 1060)) = 0;
        v20 = v19 + 1064;
        lstrcpy(v20, "displaymap");
        lstrcat(v20 + 32, "displays a big minimap on your screen so that you can see the world in more detail. The map will also display all navigation players' and enemies' precise location. Left clicking on the minimap causes your character to move to that location.");
        lstrcat(v20 + 32, " Left clicking and dragging down causes the map to display the floor below, whereas dragging up causes it to display the floor above. Right clicking and dragging causes the map to scroll in the target direction.");
        lstrcat(v20 + 32, "\n\rThe map is big so it takes time to load. Map entries are cached on disk (full maps explored take about 100 MB) and in memory. Displaying the map for the first time might be slow, so be careful.");
        *((char *)(v20 + 1056)) = 1;
        *((unsigned int *)(v20 + 1060)) = 0;
        v21 = v20 + 1064;
        lstrcpy(v21, "displaytext");
        lstrcat(v21 + 32, "displays text on your screen on the coordinates specified by setpos and color specified by setcolor. Only 1 display/listas/dontlist command can be set for a bind/key.");
        lstrcat(v21 + 32, "\n\r\n\rExample: auto 200 setcolor 1 2 3 | setpos 50 50 | displaytext '$mp / $maxmp' - displays your current mp on max mp at pos x=50 y=50 from the top left corner of your screen in RGB color 1 2 3");
        *((char *)(v21 + 1056)) = 1;
        *((unsigned int *)(v21 + 1060)) = 3;
        v22 = v21 + 1064;
        lstrcpy(v22, "dontlist");
        lstrcat(v22 + 32, "do not list the current auto bind on the screen");
        lstrcat(v22 + 32, "\n\r\n\rExample: auto 2000 dontlist | hplower 60 say exura - do not list this bind as active even though it will be activated");
        *((char *)(v22 + 1056)) = 1;
        *((unsigned int *)(v22 + 1060)) = 0;
        v23 = v22 + 1064;
        lstrcpy(v23, "dropitems");
        lstrcat(v23 + 32, "this will drop all the items that you list on the ground. More items can be listed for this command one after the other, separated by spaces.");
        lstrcat(v23 + 32, "\n\r\n\rExample: dropitems 1234 1235 1236 - drops items 1234, 1235 and 1236 on the ground where you are currently standing");
        *((char *)(v23 + 1056)) = 5;
        *((unsigned int *)(v23 + 1060)) = 66;
        v24 = v23 + 1064;
        lstrcpy(v24, "dropitemsxyz");
        lstrcat(v24 + 32, "this will drop all the items that you list on a specific x y z position on the ground. More items can be listed for this command one after the other, separated by spaces.");
        lstrcat(v24 + 32, "\n\r\n\rExample: dropitemsxyz $posx [$posy+1] $posz 1234 1235 1236 - drops items 1234, 1235 and 1236 one square below where you are currently standing");
        *((char *)(v24 + 1056)) = 5;
        *((unsigned int *)(v24 + 1060)) = 1117950594;
        v25 = v24 + 1064;
        lstrcpy(v25, "eatfood");
        lstrcat(v25 + 32, "eats food from one of your open backpacks");
        lstrcat(v25 + 32, "\n\r\n\rExample: auto 30000 eatfood - will eat food that it finds in your open backpacks every 30000 milliseconds or 30 seconds");
        *((char *)(v25 + 1056)) = 3;
        *((unsigned int *)(v25 + 1060)) = 0;
        v26 = v25 + 1064;
        lstrcpy(v26, "end");
        lstrcat(v26 + 32, "ends execution of the bind right there and restarts at the beginning");
        *((char *)(v26 + 1056)) = 1;
        *((unsigned int *)(v26 + 1060)) = 0;
        v27 = v26 + 1064;
        lstrcpy(v27, "equipammy");
        lstrcat(v27 + 32, "equips amulet with a certain item id to your neck slot if such item isn't already present there. Item ids are displayed as white text upon looking on items. If your amulet slot already has a different amulet, it's important that the backpack ");
        lstrcat(v27 + 32, "containing your desired amulet has at least one free slot to perform the switch or Tibia will complain that the action isn't possible.");
        lstrcat(v27 + 32, "\n\r\n\rExample: equipammy 1234 - equips amulet with id 1234 (your bp with the item must be open). Useful when automated (elven amulets for pvp).");
        *((char *)(v27 + 1056)) = 3;
        *((unsigned int *)(v27 + 1060)) = 66;
        v28 = v27 + 1064;
        lstrcpy(v28, "equipboots");
        lstrcat(v28 + 32, "just like equipring, but equips boots with a certain item id");
        lstrcat(v28 + 32, "\n\r\n\rExample: equipboots 1234 - equips boots with id 1234 (your bp with the item must be open). Can be used to switch softboots at a certain mp level.");
        *((char *)(v28 + 1056)) = 3;
        *((unsigned int *)(v28 + 1060)) = 66;
        v29 = v28 + 1064;
        lstrcpy(v29, "equiplhand");
        lstrcat(v29 + 32, "just like equipring, but equips an item with a certain item id on your left hand");
        lstrcat(v29 + 32, "\n\r\n\rExample: equiplhand 1234 - equips an item with id 1234 (your bp with the item must be open). Can be used to switch weapons for instance.");
        *((char *)(v29 + 1056)) = 3;
        *((unsigned int *)(v29 + 1060)) = 66;
        v30 = v29 + 1064;
        lstrcpy(v30, "equiprhand");
        lstrcat(v30 + 32, "just like equipring, but equips an item with a certain item id on your right hand");
        lstrcat(v30 + 32, "\n\r\n\rExample: equiprhand 1234 - equips an item with id 1234 (your bp with the item must be open). Can be used to switch weapons for instance.");
        *((char *)(v30 + 1056)) = 3;
        *((unsigned int *)(v30 + 1060)) = 66;
        v31 = v30 + 1064;
        lstrcpy(v31, "equipbelt");
        lstrcat(v31 + 32, "just like equipring, but equips an item with a certain item id on your belt slot");
        lstrcat(v31 + 32, "\n\r\n\rExample: equipbelt 1234 - equips an item with id 1234 (your bp with the item must be open). Can be used to switch ammunition type for instance.");
        *((char *)(v31 + 1056)) = 3;
        *((unsigned int *)(v31 + 1060)) = 66;
        v32 = v31 + 1064;
        lstrcpy(v32, "equipring");
        lstrcat(v32 + 32, "equips ring with a certain item id to your ring slot if such item isn't already present there. Item ids are displayed as white text upon looking on items. If your ring slot already has a different ring, it's important that the backpack ");
        lstrcat(v32 + 32, "containing your desired ring has at least one free slot to perform the switch or Tibia will complain that the action isn't possible.");
        lstrcat(v32 + 32, "\n\r\n\rExample: equipring 1234 - equips ring with id 1234 (your bp with the item must be open). Useful when automated.");
        *((char *)(v32 + 1056)) = 3;
        *((unsigned int *)(v32 + 1060)) = 66;
        v33 = v32 + 1064;
        lstrcpy(v33, "equipsring");
        lstrcat(v33 + 32, "works just like equipring, but is used for rings that sparkle and require therefore two different ids to operate (such as time rings or life rings). The first id is the normal id and the second id is the id of the ring when it is sparkling.");
        lstrcat(v33 + 32, "\n\r\n\rExample: auto 200 equipsring 3053 3090 - properly keeps a time ring (which is a sparkling ring) equipped");
        *((char *)(v33 + 1056)) = 3;
        *((unsigned int *)(v33 + 1060)) = 0x4242;
        v34 = v33 + 1064;
        lstrcpy(v34, "ewave");
        lstrcat(v34 + 32, "will cast the 'Energy Wave' spell only if your attack target or an enemy is in the area of effect of the spell in the direction that you are facing");
        *((char *)(v34 + 1056)) = 0;
        *((unsigned int *)(v34 + 1060)) = 0;
        v35 = v34 + 1064;
        lstrcpy(v35, "exivalast");
        lstrcat(v35 + 32, "re-exivas the last person that you have exivaed. You must have exivaed the person with a simple (not some fancy 'eX iVa name') 'exiva name' spell for this to work");
        *((char *)(v35 + 1056)) = 1;
        *((unsigned int *)(v35 + 1060)) = 0;
        v36 = v35 + 1064;
        lstrcpy(v36, "exivatarget");
        lstrcat(v36 + 32, "exivas the person that is currently your target");
        *((char *)(v36 + 1056)) = 1;
        *((unsigned int *)(v36 + 1060)) = 0;
        v37 = v36 + 1064;
        lstrcpy(v37, "explo");
        lstrcat(v37 + 32, "uses an explosion rune on a creature");
        *((char *)(v37 + 1056)) = 0;
        *((unsigned int *)(v37 + 1060)) = 1;
        v38 = v37 + 1064;
        lstrcpy(v38, "exoricon");
        lstrcat(v38 + 32, "casts the 'exori con' spell if you have enough mana and target (the one you're currently attacking) hp is below a certain percentage. Useful for dealing unexpected final blows as a team in synch as the target gets hit down gradually");
        lstrcat(v38 + 32, "\n\r\n\rExample: auto 100 exoricon 30 - when active, will automatically combo your current attack target with the 'exori con' spell if his hp goes below 30%");
        *((char *)(v38 + 1056)) = 0;
        *((unsigned int *)(v38 + 1060)) = 18;
        v39 = v38 + 1064;
        lstrcpy(v39, "exorihur");
        lstrcat(v39 + 32, "casts the 'exori hur' spell if you have enough mana and target (the one you're currently attacking) hp is below a certain percentage. Useful for dealing unexpected final blows as a team in synch as the target gets hit down gradually");
        lstrcat(v39 + 32, "\n\r\n\rExample: auto 100 exorihur 30 - when active, will automatically combo your current attack target with the 'exori hur' spell if his hp goes below 30%");
        *((char *)(v39 + 1056)) = 0;
        *((unsigned int *)(v39 + 1060)) = 18;
        v40 = v39 + 1064;
        lstrcpy(v40, "exorigran");
        lstrcat(v40 + 32, "casts the 'exori gran' spell if you have enough mana and target (the one you're currently attacking) hp is below a certain percentage. Useful for dealing unexpected final blows as a team in synch as the target gets hit down gradually. ");
        lstrcat(v40 + 32, "There is also a check requiring the target to be near you.");
        lstrcat(v40 + 32, "\n\r\n\rExample: auto 100 exorigran 30 - when active, will automatically combo your current attack target with the 'exori gran' spell if his hp goes below 30% and if he is near you");
        *((char *)(v40 + 1056)) = 0;
        *((unsigned int *)(v40 + 1060)) = 18;
        v41 = v40 + 1064;
        lstrcpy(v41, "follow");
        lstrcat(v41 + 32, "follows a creature");
        lstrcat(v41 + 32, "\n\r\n\rExample: follow friend - follows one of your friends");
        *((char *)(v41 + 1056)) = 2;
        *((unsigned int *)(v41 + 1060)) = 1;
        v42 = v41 + 1064;
        lstrcpy(v42, "goinvisible");
        lstrcat(v42 + 32, "casts the spell 'utana vid' if you are not currently invisible");
        lstrcat(v42 + 32, "\n\r\n\rExample: isonscreen 'Orc Berzerker' goinvisible - will make you invisible if an Orc Berzerker appears on the screen");
        *((char *)(v42 + 1056)) = 5;
        *((unsigned int *)(v42 + 1060)) = 0;
        v43 = v42 + 1064;
        lstrcpy(v43, "gotolabel");
        lstrcat(v43 + 32, "continues following waypoints at the waypoint for which you have set a specific label. Useful for makeing custom loops at certain conditions. This could be for example preceded by a condition such as 'caphigher 500'");
        lstrcat(v43 + 32, ". This can also be used in hotkeys (not just action scripts), to branch to certain parts of the code (ifplayerattacking).");
        lstrcat(v43 + 32, "\n\r\n\rExample: gotolabel dontdroploot - goes back to the waypoint that you labeled 'dondroptloot', to probably avoid some script or waypoints that take you to a drop loot spot and drop it there");
        *((char *)(v43 + 1056)) = 5;
        *((unsigned int *)(v43 + 1060)) = 3;
        v44 = v43 + 1064;
        lstrcpy(v44, "haste");
        lstrcat(v44 + 32, "casts 'utani hur' if you are not already hasted and have sufficient mana. Good to use on 'auto' to have permanent haste and one thing less to worry about.");
        *((char *)(v44 + 1056)) = 2;
        *((unsigned int *)(v44 + 1060)) = 0;
        v45 = v44 + 1064;
        lstrcpy(v45, "healparalysis");
        lstrcat(v45 + 32, "a paralysis safety measure that lets you heal off paralysis with a certain spell. The spell could for instance be 'utani hur', 'utani gran hur', 'exura', 'exura san', etc.");
        lstrcat(v45 + 32, "\n\r\n\rExample: auto 200 manashield | stronghaste | healparalysis utani gran hur - a bind that keep you strong hasted and mana shield and that will automatically heal off paralyssis for you during battle");
        *((char *)(v45 + 1056)) = 4;
        *((unsigned int *)(v45 + 1060)) = 35;
        v46 = v45 + 1064;
        lstrcpy(v46, "health");
        lstrcat(v46 + 32, "uses a light health potion on a creature when its hp is below a certain percentage. The target creatue must stand right next to you to be considered.");
        lstrcat(v46 + 32, "\n\r\n\rExample: health 70 self - uses a great spirit potion on yourself if your hp is below 70%");
        *((char *)(v46 + 1056)) = 4;
        *((unsigned int *)(v46 + 1060)) = 274;
        v47 = v46 + 1064;
        lstrcpy(v47, "shealth");
        lstrcat(v47 + 32, "uses a strong health potion on a creature when its hp is below a certain percentage. The target creatue must stand right next to you to be considered.");
        lstrcat(v47 + 32, "\n\r\n\rExample: shealth 70 self - uses a great spirit potion on yourself if your hp is below 70%");
        *((char *)(v47 + 1056)) = 4;
        *((unsigned int *)(v47 + 1060)) = 274;
        v48 = v47 + 1064;
        lstrcpy(v48, "ghealth");
        lstrcat(v48 + 32, "uses a great health potion on a creature when its hp is below a certain percentage. The target creatue must stand right next to you to be considered.");
        lstrcat(v48 + 32, "\n\r\n\rExample: ghealth 70 Reaper - uses a great spirit potion on character named 'Reaper' if his hp is below 70% and he's standing next to you");
        *((char *)(v48 + 1056)) = 4;
        *((unsigned int *)(v48 + 1060)) = 274;
        v49 = v48 + 1064;
        lstrcpy(v49, "uhealth");
        lstrcat(v49 + 32, "uses a ultimate health potion on a creature when its hp is below a certain percentage. The target creatue must stand right next to you to be considered.");
        lstrcat(v49 + 32, "\n\r\n\rExample: uhealth 70 friend - uses a great spirit potion on a friend that is standing next to you who's hp is below 70%");
        *((char *)(v49 + 1056)) = 4;
        *((unsigned int *)(v49 + 1060)) = 274;
        v50 = v49 + 1064;
        lstrcpy(v50, "gshealth");
        lstrcat(v50 + 32, "uses a great spirit potion on a creature when its hp is below a certain percentage. The target creatue must stand right next to you to be considered.");
        lstrcat(v50 + 32, "\n\r\n\rExample: gshealth 70 self - uses a great spirit potion on yourself if your hp is below 70%");
        *((char *)(v50 + 1056)) = 4;
        *((unsigned int *)(v50 + 1060)) = 274;
        v51 = v50 + 1064;
        lstrcpy(v51, "hmm");
        lstrcat(v51 + 32, "uses a heavy magic missile rune on a creature");
        lstrcat(v51 + 32, "\n\r\n\rExample: hmm dragon - will use a hmm rune on a nearby dragon (depending on aimbot options, it could choose the one with lowest hp%)");
        *((char *)(v51 + 1056)) = 0;
        *((unsigned int *)(v51 + 1060)) = 1;
        v52 = v51 + 1064;
        lstrcpy(v52, "icicle");
        lstrcat(v52 + 32, "uses an icicle rune on a creature");
        lstrcat(v52 + 32, "\n\r\n\rExample: icicle dragon lord - will use an icicle rune on a nearby dragon lord (depending on aimbot options, it could choose the one with lowest hp%)");
        *((char *)(v52 + 1056)) = 0;
        *((unsigned int *)(v52 + 1060)) = 1;
        v53 = v52 + 1064;
        lstrcpy(v53, "ihpc");
        lstrcat(v53 + 32, "uses a ih rune on a creautre that's hp is below a certain percentage");
        lstrcat(v53 + 32, "\n\r\n\rExample: ihpc 50 Demon Skeleton - uses a ih rune on blocking monsters to prevent them from dying. Useful when automated.");
        *((char *)(v53 + 1056)) = 4;
        *((unsigned int *)(v53 + 1060)) = 274;
        v54 = v53 + 1064;
        lstrcpy(v54, "keepmagwall");
        lstrcat(v54 + 32, "will keep shooting a magwall on the square you last attempted to shoot or shot a magwall on, to try and put one up right after the current one goes off.");
        lstrcat(v54 + 32, "\n\r\n\rExample: auto 100 keepmagwall - keeps spamming a mag wall on the last square you shot a magwall on. Careful, might lag you!");
        *((char *)(v54 + 1056)) = 1;
        *((unsigned int *)(v54 + 1060)) = 0;
        v55 = v54 + 1064;
        lstrcpy(v55, "listas");
        lstrcat(v55 + 32, "lists an auto bind as a certain custom text instead of the whole bind");
        lstrcat(v55 + 32, "\n\r\n\rExample: auto 100 | listas 'Healing on standby...' | hplower 60 { say exura | listas 'Healing active...' | wait 2000 } - displays a different text depending on what the bind is doing");
        *((char *)(v55 + 1056)) = 1;
        *((unsigned int *)(v55 + 1060)) = 3;
        v56 = v55 + 1064;
        lstrcpy(v56, "lootitems");
        lstrcat(v56 + 32, "loots items as defined in the lootitems.txt file. Works best on 'auto'. See the 'Extras' secion of the help topics for more details. ");
        lstrcat(v56 + 32, "\n\r\n\rExample: auto 200 lootitems - will repeatedly try to loot items from open windows every 200 milliseconds when the bind gets activated");
        *((char *)(v56 + 1056)) = 3;
        *((unsigned int *)(v56 + 1060)) = 0;
        v57 = v56 + 1064;
        lstrcpy(v57, "magwall");
        lstrcat(v57 + 32, "a simple mag wall command. It will shoot a mag wall two squares (to best account for delay) in front of a creature. Useful whether the creature is either running after you or from you and most effective when running in a straight line.");
        *((char *)(v57 + 1056)) = 1;
        *((unsigned int *)(v57 + 1060)) = 1;
        v58 = v57 + 1064;
        lstrcpy(v58, "makerune");
        lstrcat(v58 + 32, "makes a certain rune. Your belt/arrow slot must be free for this command to function.");
        lstrcat(v58 + 32, "\n\r\n\rExample: auto 200 makerune [$maxmp-20] 'adori frigo' - makes an icicle rune if your mp is at least 20 below your max");
        *((char *)(v58 + 1056)) = 1;
        *((unsigned int *)(v58 + 1060)) = 9010;
        v59 = v58 + 1064;
        lstrcpy(v59, "mana");
        lstrcat(v59 + 32, "uses a light mana potion on a creature (only logical to use on self, won't do anything if mana is full)");
        lstrcat(v59 + 32, "\n\r\n\rExample: mana self - uses a light mana potion on yourself if your mp isn't full");
        *((char *)(v59 + 1056)) = 4;
        *((unsigned int *)(v59 + 1060)) = 1;
        v60 = v59 + 1064;
        lstrcpy(v60, "smana");
        lstrcat(v60 + 32, "uses a strong mana potion on a creature (only logical to use on self, won't do anything if mana is full)");
        lstrcat(v60 + 32, "\n\r\n\rExample: smana self - uses a strong mana potion on yourself if your mp isn't full");
        *((char *)(v60 + 1056)) = 4;
        *((unsigned int *)(v60 + 1060)) = 1;
        v61 = v60 + 1064;
        lstrcpy(v61, "gmana");
        lstrcat(v61 + 32, "uses a great mana potion on a creature (only logical to use on self, won't do anything if mana is full)");
        lstrcat(v61 + 32, "\n\r\n\rExample: gmana self - uses a great mana potion on yourself if your mp isn't full");
        *((char *)(v61 + 1056)) = 4;
        *((unsigned int *)(v61 + 1060)) = 1;
        v62 = v61 + 1064;
        lstrcpy(v62, "gsmana");
        lstrcat(v62 + 32, "uses a great spirit potion on a creature (only logical to use on self, won't do anything if mana is full)");
        lstrcat(v62 + 32, "\n\r\n\rExample: gsmana self - uses a great spirit potion on yourself if your mp isn't full");
        *((char *)(v62 + 1056)) = 4;
        *((unsigned int *)(v62 + 1060)) = 1;
        v63 = v62 + 1064;
        lstrcpy(v63, "manashield");
        lstrcat(v63 + 32, "casts 'utamo vita' if you are not already mana shielded and have sufficient mana. Good to use on 'auto' to have permanent manashields and one thing less to worry about.");
        *((char *)(v63 + 1056)) = 4;
        *((unsigned int *)(v63 + 1060)) = 0;
        v64 = v63 + 1064;
        lstrcpy(v64, "movee");
        lstrcat(v64 + 32, "moves you east. The purpose is to be used on some numlock keys while retaining others for other binds.");
        *((char *)(v64 + 1056)) = 2;
        *((unsigned int *)(v64 + 1060)) = 0;
        v65 = v64 + 1064;
        lstrcpy(v65, "moven");
        lstrcat(v65 + 32, "moves you north. The purpose is to be used on some numlock keys while retaining others for other binds.");
        *((char *)(v65 + 1056)) = 2;
        *((unsigned int *)(v65 + 1060)) = 0;
        v66 = v65 + 1064;
        lstrcpy(v66, "moves");
        lstrcat(v66 + 32, "moves you south. The purpose is to be used on some numlock keys while retaining others for other binds.");
        *((char *)(v66 + 1056)) = 2;
        *((unsigned int *)(v66 + 1060)) = 0;
        v67 = v66 + 1064;
        lstrcpy(v67, "movew");
        lstrcat(v67 + 32, "moves you west. The purpose is to be used on some numlock keys while retaining others for other binds.");
        *((char *)(v67 + 1056)) = 2;
        *((unsigned int *)(v67 + 1060)) = 0;
        v68 = v67 + 1064;
        lstrcpy(v68, "movene");
        lstrcat(v68 + 32, "moves you north-east. The purpose is to be used on some numlock keys while retaining others for other binds.");
        *((char *)(v68 + 1056)) = 2;
        *((unsigned int *)(v68 + 1060)) = 0;
        v69 = v68 + 1064;
        lstrcpy(v69, "movenw");
        lstrcat(v69 + 32, "moves you north-west. The purpose is to be used on some numlock keys while retaining others for other binds.");
        *((char *)(v69 + 1056)) = 2;
        *((unsigned int *)(v69 + 1060)) = 0;
        v70 = v69 + 1064;
        lstrcpy(v70, "movese");
        lstrcat(v70 + 32, "moves you south-east. The purpose is to be used on some numlock keys while retaining others for other binds.");
        *((char *)(v70 + 1056)) = 2;
        *((unsigned int *)(v70 + 1060)) = 0;
        v71 = v70 + 1064;
        lstrcpy(v71, "movesw");
        lstrcat(v71 + 32, "moves you south-west. The purpose is to be used on some numlock keys while retaining others for other binds.");
        *((char *)(v71 + 1056)) = 2;
        *((unsigned int *)(v71 + 1060)) = 0;
        v72 = v71 + 1064;
        lstrcpy(v72, "moveitems");
        lstrcat(v72 + 32, "moves all items of a certain id to a window with a certain type.");
        lstrcat(v72 + 32, "\n\r\n\rExample: moveitems 1234 Red Backpack - move all items of type found in open windows (that are not already in a window called Red Backpack) to a window called Red Backpack with free space.");
        *((char *)(v72 + 1056)) = 3;
        *((unsigned int *)(v72 + 1060)) = 13122;
        v73 = v72 + 1064;
        lstrcpy(v73, "moveitemsonto");
        lstrcat(v73 + 32, "moves all items of a certain id onto a container with a certain id at a certain index present in some open window with a certain name. If index is 0, it will try moving the item onto all containers of that id.");
        lstrcat(v73 + 32, "\n\r\n\rExample: moveitemsonto 1234 1235 1 'Red Backpack' - move all items of id 1234 onto the 1st container of id 1235 found in a window called 'Red Backpack'");
        *((char *)(v73 + 1056)) = 3;
        *((unsigned int *)(v73 + 1060)) = 855786050;
        v74 = v73 + 1064;
        lstrcpy(v74, "npcsay");
        lstrcat(v74 + 32, "says the following text in the npc window");
        lstrcat(v74 + 32, "\n\r\n\rExample: npcsay trade - initiates a trade with a nearby npc. The npc needs to have 'hi' said to him first, however");
        *((char *)(v74 + 1056)) = 1;
        *((unsigned int *)(v74 + 1060)) = 19;
        v75 = v74 + 1064;
        lstrcpy(v75, "openbeltitem");
        lstrcat(v75 + 32, "opens the item that is located in your belt slot in a new window");
        *((char *)(v75 + 1056)) = 3;
        *((unsigned int *)(v75 + 1060)) = 0;
        v76 = v75 + 1064;
        lstrcpy(v76, "openbpitem");
        lstrcat(v76 + 32, "opens the item that is located in your bp slot in a new window");
        *((char *)(v76 + 1056)) = 3;
        *((unsigned int *)(v76 + 1060)) = 0;
        v77 = v76 + 1064;
        lstrcpy(v77, "openitem");
        lstrcat(v77 + 32, "opens an item with a certain id at a certain index that appears in one of your open windows of a certain type (the type is specified by either the item ID associated to the window, or the window name). ");
        lstrcat(v77 + 32, " The 2nd parameter is an index, which specifies which item in sequence that you want to open: the 1st, the 2nd, the 3rd, etc.. The item is opened in the same window.");
        lstrcat(v77 + 32, "\n\r\n\rExample: openitem 1234 3 Red Backpack - opens the 3rd item of type 1234 that is located in a window called 'Red Backpack'.");
        *((char *)(v77 + 1056)) = 3;
        *((unsigned int *)(v77 + 1060)) = 3371586;
        v78 = v77 + 1064;
        lstrcpy(v78, "openitemnew");
        lstrcat(v78 + 32, "same as 'openitem', but the item is opened in a new window instead.");
        *((char *)(v78 + 1056)) = 3;
        *((unsigned int *)(v78 + 1060)) = 3371586;
        v79 = v78 + 1064;
        lstrcpy(v79, "opengrounditem");
        lstrcat(v79 + 32, "finds on the ground up to 1 square around you an item with a certain id and opens it. As an easy way to open depot lockers of which there is multiple types, you can specifiy 'dp' for the itemid parameter.");
        lstrcat(v79 + 32, "\n\r\n\rExample: opengrounditem dp - opens a depot locker box that is located somewhere around you on the ground.");
        *((char *)(v79 + 1056)) = 3;
        *((unsigned int *)(v79 + 1060)) = 66;
        v80 = v79 + 1064;
        lstrcpy(v80, "opengroundxyz");
        lstrcat(v80 + 32, "opens the item that is on a certain x y z location in a new window");
        lstrcat(v80 + 32, "\n\r\n\rExample: opengroundxyz 3200 32100 7 - opens the item found on the square with the specified coordinates in a new window");
        *((char *)(v80 + 1056)) = 3;
        *((unsigned int *)(v80 + 1060)) = 10654338;
        v81 = v80 + 1064;
        lstrcpy(v81, "paralyze");
        lstrcat(v81 + 32, "uses paralyze rune on a creature");
        lstrcat(v81 + 32, "\n\r\n\rExample: paralyze target - paralyzes your current attack target");
        *((char *)(v81 + 1056)) = 0;
        *((unsigned int *)(v81 + 1060)) = 1;
        v82 = v81 + 1064;
        lstrcpy(v82, "pickupitems");
        lstrcat(v82 + 32, "this will pickup all items on the tile that you are currently standing to an open container window specificed by you (ranging from 0-15)");
        *((char *)(v82 + 1056)) = 5;
        *((unsigned int *)(v82 + 1060)) = 2;
        v83 = v82 + 1064;
        lstrcpy(v83, "playsound");
        lstrcat(v83 + 32, "plays a certain .wav sound file, which must me located/placed in your 'ElfBot NG/sounds' folder.");
        lstrcat(v83 + 32, "\n\r\n\rExample: auto 200 hplower 400 playsound alarm.wav - will play alarm.wav file if you hp is lower than 400");
        *((char *)(v83 + 1056)) = 1;
        *((unsigned int *)(v83 + 1060)) = 3;
        v84 = v83 + 1064;
        lstrcpy(v84, "pm");
        lstrcat(v84 + 32, "private messages text to a certain player");
        lstrcat(v84 + 32, "\n\r\n\rExample: pm 'Player' 'hello there' - privates messages the words 'hello there' to the character named 'Player'");
        *((char *)(v84 + 1056)) = 1;
        *((unsigned int *)(v84 + 1060)) = 0x1313;
        v85 = v84 + 1064;
        lstrcpy(v85, "reachgrounditem");
        lstrcat(v85 + 32, "walks up to an item found on-screen (or 1-2 sqaure off screen) that is currently reachable and is on top (there is nothing on the item). You may use 'dp' for the itemid parameter to reach one of the multiple dp types.");
        lstrcat(v85 + 32, "\n\r\n\rExample: reachgrounditem dp - reaches an accessible an openable depot locker box");
        *((char *)(v85 + 1056)) = 3;
        *((unsigned int *)(v85 + 1060)) = 66;
        v86 = v85 + 1064;
        lstrcpy(v86, "reconnect");
        lstrcat(v86 + 32, "reconnects you on the last character you were on");
        lstrcat(v86 + 32, "\n\r\n\rExample: auto 100 ifnot $connected { reconnect | wait 6000 }");
        *((char *)(v86 + 1056)) = 1;
        *((unsigned int *)(v86 + 1060)) = 0;
        v87 = v86 + 1064;
        lstrcpy(v87, "refillammo");
        lstrcat(v87 + 32, "refills any item in your left hand, right hand or belt slot if it's count is below 100 and if it is also found in any open backpack.");
        lstrcat(v87 + 32, "\n\r\n\rExample: auto 15000 refillammo - refills your ammunition every 15 seconds. Don't make this too fast automatically, because refilling bolts for instance every time one is missing might needlessly lag you.");
        *((char *)(v87 + 1056)) = 3;
        *((unsigned int *)(v87 + 1060)) = 0;
        v88 = v87 + 1064;
        lstrcpy(v88, "refillmana");
        lstrcat(v88 + 32, "a feature that works in combination with the nav server's exact mana display. This function will have every connected friend executing it help mana fluid each other when they go low on mana. ");
        lstrcat(v88 + 32, "This results in extremely fast mana restoration rates (best used on mages). The first parameter is the amount of missing mana from someone's max mana, the second is the distance in squares that you can tolerate ");
        lstrcat(v88 + 32, "being from the target to fluid him up. You must be manashielded to be fluided up by others.");
        lstrcat(v88 + 32, "\n\r\n\rExample: refillmana 1000 2 - will walk up to a nav friend up to 1 square to fluid him up if his mana goes 1000 below his max");
        *((char *)(v88 + 1056)) = 4;
        *((unsigned int *)(v88 + 1060)) = 21042;
        v89 = v88 + 1064;
        lstrcpy(v89, "refillhealth");
        lstrcat(v89 + 32, "a feature that works in combination with the player info display feature (it must be enabled). This function will heal any friend that has missing a certain amount of health from his max.");
        lstrcat(v89 + 32, "This may result in more efficient use of potions and healing. The first parameter is the amount of hp missing from someone's max hp, the second is the distance in squares that you can tolerate ");
        lstrcat(v89 + 32, "being from the target to fluid him up. This uses the 'Heal Friend' potion listed in the 'Healing' panel of the GUI.");
        lstrcat(v89 + 32, "\n\r\n\rExample: refillhealth 600 2 - will walk up to 1 suqare towards a friend to fluid him up if his hp goes 600 below his max");
        *((char *)(v89 + 1056)) = 4;
        *((unsigned int *)(v89 + 1060)) = 21026;
        v90 = v89 + 1064;
        lstrcpy(v90, "say");
        lstrcat(v90 + 32, "says the following text in default chat");
        lstrcat(v90 + 32, "\n\r\n\rExample: say exori vis - says 'exori vis' in default chat, resulting in the spell 'energy strike' being cast");
        *((char *)(v90 + 1056)) = 1;
        *((unsigned int *)(v90 + 1060)) = 19;
        v91 = v90 + 1064;
        lstrcpy(v91, "scrollview");
        lstrcat(v91 + 32, "scrolls the view to see the offscreen tiles in the direction that you are facing. If you run the command again while facing in the same direction, it goes back to normal. ");
        lstrcat(v91 + 32, "With this, you can see and shoot runes such as gfbs, sds, or even magic walls offscreen. However, you can only shoot offscreen 2 squares to the south and 1 square to the north. It is not possible to shoot offscreen to the west or to the east.");
        *((char *)(v91 + 1056)) = 1;
        *((unsigned int *)(v91 + 1060)) = 0;
        v92 = v91 + 1064;
        lstrcpy(v92, "sd");
        lstrcat(v92 + 32, "uses a sudden death rune on a creature");
        lstrcat(v92 + 32, "\n\r\n\rExample: sd enemy - shoots a sd run on the best enemy from enemy list, depending on options");
        *((char *)(v92 + 1056)) = 0;
        *((unsigned int *)(v92 + 1060)) = 1;
        v93 = v92 + 1064;
        lstrcpy(v93, "sellitems");
        lstrcat(v93 + 32, "sells a specific amount of a certain item to an NPC. The npc must have a trade initiated with him beforehand. The amount can be 100 even if you don't have that many items. It will simply sell all that you have.");
        lstrcat(v93 + 32, "\n\r\n\rExample: sellitems 1234 100 - sell all items of id 1234 to the NPC.");
        *((char *)(v93 + 1056)) = 3;
        *((unsigned int *)(v93 + 1060)) = 25154;
        v94 = v93 + 1064;
        lstrcpy(v94, "sellitemsdownto");
        lstrcat(v94 + 32, "sells a specific amount of a certain item to an NPC down to a certain total desired amount depending on how many you already have. You must count the items with 'countitems' or 'countitemsvisible' and the npc must have a trade initiated ");
        lstrcat(v94 + 32, "with him beforehand.");
        *((char *)(v94 + 1056)) = 3;
        *((unsigned int *)(v94 + 1060)) = 25154;
        v95 = v94 + 1064;
        lstrcpy(v95, "setautocombo");
        lstrcat(v95 + 32, "a quick way to enable or disable automatic combo fire setting in the aimbot portion of the bot");
        lstrcat(v95 + 32, "\n\r\n\rExample: setautocombo off - turns auto combo off so that you may for instance magic wall or paralyze with more chances of success");
        *((char *)(v95 + 1056)) = 6;
        *((unsigned int *)(v95 + 1060)) = 4;
        v96 = v95 + 1064;
        lstrcpy(v96, "setcaption");
        lstrcat(v96 + 32, "changes the text of your Tibia Client's window");
        lstrcat(v96 + 32, "\n\r\n\rExample: auto 200 setcaption '$name' - sets the caption of your Tibia Client window to the name of your character");
        *((char *)(v96 + 1056)) = 1;
        *((unsigned int *)(v96 + 1060)) = 3;
        v97 = v96 + 1064;
        lstrcpy(v97, "setcolor");
        lstrcat(v97 + 32, "sets the color for text to be display using 'displaytext' or auto binds to be listed as in RGB format. You can get the values by using the color picker at the Navigation dialog.");
        lstrcat(v97 + 32, "\n\r\n\rExample: setcolor 200 200 200 - sets a light greyish color to draw text in");
        *((char *)(v97 + 1056)) = 1;
        *((unsigned int *)(v97 + 1060)) = 0x20202;
        v98 = v97 + 1064;
        lstrcpy(v98, "setpos");
        lstrcat(v98 + 32, "sets the position for text to be display using 'displaytext'");
        *((char *)(v98 + 1056)) = 1;
        *((unsigned int *)(v98 + 1060)) = 37506;
        v99 = v98 + 1064;
        lstrcpy(v99, "settargeting");
        lstrcat(v99 + 32, "a quick way to enable or disable the run targeting setting in the targeting portion of the bot");
        lstrcat(v99 + 32, "\n\r\n\rExample: settargeting on - turns on the targeting feature so that the bot will control how your character attacks creatures");
        *((char *)(v99 + 1056)) = 6;
        *((unsigned int *)(v99 + 1060)) = 4;
        v100 = v99 + 1064;
        lstrcpy(v100, "setfollowwaypoints");
        lstrcat(v100 + 32, "a quick way to enable or disable the following of waypoints setting in the cavebot portion of the bot");
        lstrcat(v100 + 32, "\n\r\n\rExample: setfollowwaypoints off - turns off the following of waypoints so that you may move around freely");
        *((char *)(v100 + 1056)) = 6;
        *((unsigned int *)(v100 + 1060)) = 4;
        v101 = v100 + 1064;
        lstrcpy(v101, "sio");
        lstrcat(v101 + 32, "casts the druid 'exura sio' spell on a creautre that's hp is below a certain percentage");
        lstrcat(v101 + 32, "\n\r\n\rExample: sio 60 Brave Warrior - casts the sio spell if Brave Warrior's hp is below 60%. Such healing binds are good to be active automatically to be able to react fast.");
        *((char *)(v101 + 1056)) = 4;
        *((unsigned int *)(v101 + 1060)) = 274;
        v102 = v101 + 1064;
        lstrcpy(v102, "skin");
        lstrcat(v102 + 32, "a command that will look for reachable skinnable corpses x squares around you, walk up to the closest one and skin it with an obsidian knife. Make sure you use the ids of the skinnable corpses, those 10 seconds after a monster has dropped.");
        lstrcat(v102 + 32, "\n\r\n\rExample: skin 2 1234 1235 1236 - will skin corpses with ids 1234, 1235 and 1236 that are up to 2 squares away from you");
        *((char *)(v102 + 1056)) = 3;
        *((unsigned int *)(v102 + 1060)) = 16978;
        v103 = v102 + 1064;
        lstrcpy(v103, "skip");
        lstrcat(v103 + 32, "for use in cavebot action scripts. This command will finish executing the current action script and skip to the next waypoint in sequence,");
        lstrcat(v103 + 32, "\n\r\n\rExample: isnotlocation skip - if your character is not standing where the action waypoint has been set, the following script will not execute and will skip to the next waypoint. Otherwise, the script will continue.");
        *((char *)(v103 + 1056)) = 5;
        *((unsigned int *)(v103 + 1060)) = 0;
        idx1 = v103 + 1064;
        lstrcpy(idx1, "soulf");
        lstrcat(idx1 + 32, "soulfires creatures. The bot remembers who has been soulfired for 20 seconds and doesn't soulfire the same person twice for this amount of time");
        lstrcat(idx1 + 32, "\n\r\n\rExample: soulf enemy - will shoot soulfires on all the people currently on your screen and enemy list");
        *((char *)(idx1 + 1056)) = 0;
        *((unsigned int *)(idx1 + 1060)) = 1;
        idx2 = idx1 + 1064;
        lstrcpy(idx2, "spydown");
        lstrcat(idx2 + 32, "will level spy on the levels below you by an offset of one or more. It will keep spying by the same offset even if you change floors, so use the other command to return to normal.");
        *((char *)(idx2 + 1056)) = 1;
        *((unsigned int *)(idx2 + 1060)) = 0;
        v106 = idx2 + 1064;
        lstrcpy(v106, "spyup");
        lstrcat(v106 + 32, "will level spy on the levels above you by an offset of one or more. It will keep spying by the same offset even if you change floors, so use the other command to return to normal.");
        *((char *)(v106 + 1056)) = 1;
        *((unsigned int *)(v106 + 1060)) = 0;
        v107 = v106 + 1064;
        lstrcpy(v107, "set");
        lstrcat(v107 + 32, "creates a new variables or uses an existing one and assigns a certain value to it");
        lstrcat(v107 + 32, "\n\r\n\rExample: set $mylowmp [$maxmp - 50] - creates a variable called $mylowmp and assigns the value of $maxmp - 50 to it");
        *((char *)(v107 + 1056)) = 1;
        *((unsigned int *)(v107 + 1060)) = 2;
        v108 = v107 + 1064;
        lstrcpy(v108, "setattackmode");
        lstrcat(v108 + 32, "sets your current attack/chase mode. Possible choices are 'offensive', 'balanced' 'defensive' for the attack mode and 'stand', 'chase' for the chase mode. Note that the attack mode icon ");
        lstrcat(v108 + 32, "will not be changed in your client even though the setting really did take place.");
        lstrcat(v108 + 32, "setattackmode 'balanced' 'stand' - set your attack mode to balanced/stand");
        *((char *)(v108 + 1056)) = 0;
        *((unsigned int *)(v108 + 1060)) = 0x303;
        v109 = v108 + 1064;
        lstrcpy(v109, "stackitems");
        lstrcat(v109 + 32, "this will stack all countable items that are split accross piles of less than 100 together. Useful for stacking gold after selling some items, for example");
        *((char *)(v109 + 1056)) = 5;
        *((unsigned int *)(v109 + 1060)) = 0;
        v110 = v109 + 1064;
        lstrcpy(v110, "stalagmite");
        lstrcat(v110 + 32, "uses a stalagmite rune on a creature");
        lstrcat(v110 + 32, "\n\r\n\rExample: stalagmite dragon - will use a stalagmite rune on a nearby dragon (depending on aimbot options, it could choose the one with lowest hp%)");
        *((char *)(v110 + 1056)) = 0;
        *((unsigned int *)(v110 + 1060)) = 1;
        v111 = v110 + 1064;
        lstrcpy(v111, "statusmessage");
        lstrcat(v111 + 32, "will display a white statusmessage in the bottom center of the screen. Can be used to let you know what happens when you press a certain key, for instance.");
        *((char *)(v111 + 1056)) = 1;
        *((unsigned int *)(v111 + 1060)) = 3;
        v112 = v111 + 1064;
        lstrcpy(v112, "stopattack");
        lstrcat(v112 + 32, "will stop attacking/following the creature you are currently attacking/following");
        *((char *)(v112 + 1056)) = 0;
        *((unsigned int *)(v112 + 1060)) = 0;
        v113 = v112 + 1064;
        lstrcpy(v113, "stronghaste");
        lstrcat(v113 + 32, "casts 'utani gran hur' if you are not already hasted and have sufficient mana. Good to use on 'auto' to have permanent haste and one thing less to worry about.");
        *((char *)(v113 + 1056)) = 2;
        *((unsigned int *)(v113 + 1060)) = 0;
        v114 = v113 + 1064;
        lstrcpy(v114, "swapequip");
        lstrcat(v114 + 32, "swap an item from one inventory slot to another. The destination slot must of course be empty. The possibilities are: 'helmet' 'amulet' 'backpack' 'chest' 'lhand' 'rhand' 'legs' 'boots' 'ring' 'belt'");
        lstrcat(v114 + 32, "\n\r\n\rExample: swapequip 'ring' 'belt' - moves the item in your ring slot to your belt/arrow slot");
        *((char *)(v114 + 1056)) = 3;
        *((unsigned int *)(v114 + 1060)) = 0x303;
        v115 = v114 + 1064;
        lstrcpy(v115, "turnoff");
        lstrcat(v115 + 32, "turns an auto bind off");
        *((char *)(v115 + 1056)) = 1;
        *((unsigned int *)(v115 + 1060)) = 0;
        v116 = v115 + 1064;
        lstrcpy(v116, "uh");
        lstrcat(v116 + 32, "uses a uh rune on a creature (its hp must be less then 95% for it to be considered).");
        lstrcat(v116 + 32, "\n\r\n\rExample: uh friend - uhs a friend out of your list (depending on options, it may be the friend with least hp, therefore the one that probably needs it most)");
        *((char *)(v116 + 1056)) = 4;
        *((unsigned int *)(v116 + 1060)) = 1;
        v117 = v116 + 1064;
        lstrcpy(v117, "uhpc");
        lstrcat(v117 + 32, "uses a uh rune on a creautre that's hp is below a certain percentage");
        lstrcat(v117 + 32, "\n\r\n\rExample: uhpc 40 friend - uses a uh rune on any friend that's hp is below 40%. Useful when automated.");
        *((char *)(v117 + 1056)) = 4;
        *((unsigned int *)(v117 + 1060)) = 274;
        v118 = v117 + 1064;
        lstrcpy(v118, "unequip");
        lstrcat(v118 + 32, "unequips an item from one of your inventory slots and puts it into a specific backpack");
        lstrcat(v118 + 32, "\n\r\n\rExample: unequip 'ring' 'Yellow backpack' - puts the item that is in your ring slot and places it into a yellow backpack");
        *((char *)(v118 + 1056)) = 3;
        *((unsigned int *)(v118 + 1060)) = 13059;
        v119 = v118 + 1064;
        lstrcpy(v119, "useoncreature");
        lstrcat(v119 + 32, "uses an item with a certain id on a creature, just like when using the new tibia hotkeys");
        lstrcat(v119 + 32, "\n\r\n\rExample: useoncreature 1234 self - uses item 1234 on yourself.");
        *((char *)(v119 + 1056)) = 3;
        *((unsigned int *)(v119 + 1060)) = 322;
        v120 = v119 + 1064;
        lstrcpy(v120, "useitem");
        lstrcat(v120 + 32, "uses an item with a certain id (like when eating food), just like when using the new tibia hotkeys");
        lstrcat(v120 + 32, "\n\r\n\rExample: useitem 1234 - uses item 1234.");
        *((char *)(v120 + 1056)) = 3;
        *((unsigned int *)(v120 + 1060)) = 66;
        v121 = v120 + 1064;
        lstrcpy(v121, "usegrounditem");
        lstrcat(v121 + 32, "finds on the ground up to 1 square around you an item with a certain id and uses it");
        lstrcat(v121 + 32, "\n\r\n\rExample: usegrounditem 1234 - uses item 1234 that is located on the ground somewhere around you");
        *((char *)(v121 + 1056)) = 3;
        *((unsigned int *)(v121 + 1060)) = 66;
        v122 = v121 + 1064;
        lstrcpy(v122, "usegroundxyz");
        lstrcat(v122 + 32, "use the item that is on a certain x y z location");
        lstrcat(v122 + 32, "\n\r\n\rExample: usegroundxyz 3200 32100 7 - uses the item found on the square with the specified coordinates");
        *((char *)(v122 + 1056)) = 3;
        *((unsigned int *)(v122 + 1060)) = 10654338;
        v123 = v122 + 1064;
        lstrcpy(v123, "useongrounditem");
        lstrcat(v123 + 32, "uses an item from your inventory on a ground item that is found up to 1 square around you");
        lstrcat(v123 + 32, "\n\r\n\rExample: useongrounditem 1234 3000 - uses item 1234 on an item 3000 found on the ground around you");
        *((char *)(v123 + 1056)) = 3;
        *((unsigned int *)(v123 + 1060)) = 0x4242;
        v124 = v123 + 1064;
        lstrcpy(v124, "repeatuseongroundxyz");
        lstrcat(v124 + 32, "repeats the usage of an item from your inventory on a ground item as long as that item is found on that square. Please add the z coordinate manually because the hotkey wizard doesn't currently support more than 4 parameters.");
        lstrcat(v124 + 32, "\n\r\n\rExample: repeatuseongroundxyz 1234 1235 32000 32000 7 - uses item 1234 on an item 1235 found on the ground at location xyz as long as item 1235 is located there. Used for digging tombholes and breaking items/walls.");
        *((char *)(v124 + 1056)) = 3;
        *((unsigned int *)(v124 + 1060)) = 2458010178;
        v125 = v124 + 1064;
        lstrcpy(v125, "useongroundxyz");
        lstrcat(v125 + 32, "use a certain item from your inventory on the item that is on a certain x y z location");
        lstrcat(v125 + 32, "\n\r\n\rExample: useongroundxyz 1234 3200 32100 7 - uses the item 1234 on the square with the specified coordinates");
        *((char *)(v125 + 1056)) = 3;
        *((unsigned int *)(v125 + 1060)) = 2727510594;
        v126 = v125 + 1064;
        lstrcpy(v126, "wait");
        lstrcat(v126 + 32, "waits a certain interval of time before executing the next command.");
        lstrcat(v126 + 32, "\n\r\n\rExample: wait 2000 - waits 2000 milliseconds or 2 seconds before executing the next command in sequence.");
        *((char *)(v126 + 1056)) = 5;
        *((unsigned int *)(v126 + 1060)) = 2;
        v127 = v126 + 1064;
        lstrcpy(v127, "wave");
        lstrcat(v127 + 32, "will cast a custom wave spell only if your attack target or an enemy is in the area of effect of the spell in the direction that you are facing");
        lstrcat(v127 + 32, "\n\r\n\rExample: wave exevo vis hur - will cast ewave spell if there is a target or enemy in the direction that you are facing");
        *((char *)(v127 + 1056)) = 0;
        *((unsigned int *)(v127 + 1060)) = 35;
        v128 = v127 + 1064;
        lstrcpy(v128, "xlog");
        lstrcat(v128 + 32, "x-logs you out of the game without the need of shutting the client. This way, you can also log back in quickly if need be because your char-list will stay open");
        *((char *)(v128 + 1056)) = 1;
        *((unsigned int *)(v128 + 1060)) = 0;
        v129 = v128 + 2128;
        lstrcpy(v129, "No condition");
        g_1005e198 = v129;
        lstrcat(v129 + 32, "this action is to be cast without a condition, already had conditions added to it, or already has conditions embedded into its command and doesn't need any more");
        lstrcat(v129 + 32, "\n\r\n\rExample: manashield - this command has the 'cast manashield only if not mana shielded already' condition already embedded in its command");
        *((char *)(v129 + 1056)) = 7;
        *((unsigned int *)(v129 + 1060)) = 0;
        v130 = v129 + 1064;
        lstrcpy(v130, "countlower");
        lstrcat(v130 + 32, "this conditional can be used after using 'countitems' or 'countitemsvisible'. It will execute a certain command if the count was found to be lower than a certain amount");
        lstrcat(v130 + 32, "\n\r\n\rExample: countlower 10 gotolabel buyspears - assuming a script command 'countitems 1234' was used to count the amount of spears of id 1234, will skip to the wpt labeled 'buyspears' if the amount is lower than 10");
        *((char *)(v130 + 1056)) = 7;
        *((unsigned int *)(v130 + 1060)) = 98;
        v131 = v130 + 1064;
        lstrcpy(v131, "counthigher");
        lstrcat(v131 + 32, "this conditional can be used after using 'countitems' or 'countitemsvisible'. It will execute a certain command if the count was found to be higher or EQUAL than a certain amount");
        *((char *)(v131 + 1056)) = 7;
        *((unsigned int *)(v131 + 1060)) = 98;
        v132 = v131 + 1064;
        lstrcpy(v132, "caplower");
        lstrcat(v132 + 32, "only executes the command if your capacity is lower than a certain amount");
        *((char *)(v132 + 1056)) = 7;
        *((unsigned int *)(v132 + 1060)) = 2;
        v133 = v132 + 1064;
        lstrcpy(v133, "caphigher");
        lstrcat(v133 + 32, "only executes the command if your capacity is higher or EQUAL to a certain amount");
        *((char *)(v133 + 1056)) = 7;
        *((unsigned int *)(v133 + 1060)) = 2;
        v134 = v133 + 1064;
        lstrcpy(v134, "if");
        lstrcat(v134 + 32, "executes a command only if the expression given evaluats to true (not-zero)");
        lstrcat(v134 + 32, "\n\r\n\rExample: auto 200 if [$mp > 500] { say exura | wait 5000 } - casts exura if your mp is higher than 500");
        *((char *)(v134 + 1056)) = 7;
        *((unsigned int *)(v134 + 1060)) = 3;
        v135 = v134 + 1064;
        lstrcpy(v135, "ifnot");
        lstrcat(v135 + 32, "executes a command only if the expression given evaluats to false (zero). Same as doing: if [$expression == 0].");
        lstrcat(v135 + 32, "\n\r\n\rExample: auto 200 ifnot $connected { reconnect | wait 5000 } - reconnects you if not connected");
        *((char *)(v135 + 1056)) = 7;
        *((unsigned int *)(v135 + 1060)) = 3;
        v136 = v135 + 1064;
        lstrcpy(v136, "else");
        lstrcat(v136 + 32, "executes a command if the corresponding if/ifnot expression has evaluated to false");
        lstrcat(v136 + 32, "\n\r\n\rExample: auto 200 ifnot $connected { reconnect | wait 5000 } else { useitem 3031 | wait 5000 } - reconnects you if not connected, otherwises sends a useless command every 5 seconds to keep you online");
        *((char *)(v136 + 1056)) = 7;
        *((unsigned int *)(v136 + 1060)) = 0;
        v137 = v136 + 1064;
        lstrcpy(v137, "ifdefaultmessage");
        lstrcat(v137 + 32, "executes a command only if a default chat message has been received within the past 2 seconds");
        lstrcat(v137 + 32, "\n\r\n\rExample: auto 200 ifdefaultmessage { wait 3000 | say ?? | wait 5000 } - says ?? if a defaultmessage has been said");
        *((char *)(v137 + 1056)) = 7;
        *((unsigned int *)(v137 + 1060)) = 0;
        v138 = v137 + 1064;
        lstrcpy(v138, "ifplayerattacking");
        lstrcat(v138 + 32, "executes a command only if a player has attacked you within the past 2 seconds");
        lstrcat(v138 + 32, "\n\r\n\rExample: auto 200 ifplayerattacking { attack $pkname | wait 3000 } - counterattacks the player that has attacked you");
        *((char *)(v138 + 1056)) = 7;
        *((unsigned int *)(v138 + 1060)) = 0;
        v139 = v138 + 1064;
        lstrcpy(v139, "ifprivatemessage");
        lstrcat(v139 + 32, "executes a command only if a privated chat message has been received within the past 2 seconds");
        lstrcat(v139 + 32, "\n\r\n\rExample: auto 200 ifdefaultmessage { wait 3000 | say ?? | wait 5000 } - says ?? if a defaultmessage has been said");
        *((char *)(v139 + 1056)) = 7;
        *((unsigned int *)(v139 + 1060)) = 0;
        v140 = v139 + 1064;
        lstrcpy(v140, "ifdrunk");
        lstrcat(v140 + 32, "executes a command only if you are drunk");
        lstrcat(v140 + 32, "\n\r\n\rExample: auto 200 ifdrunk { equipring 1234 | wait 30000 | equipring 1235 } - equips ring 1234 if you are drunk, waits 30 seconds and equips ring 1235 to see if you are no longer drunk");
        *((char *)(v140 + 1056)) = 7;
        *((unsigned int *)(v140 + 1060)) = 0;
        v141 = v140 + 1064;
        lstrcpy(v141, "ifgm");
        lstrcat(v141 + 32, "executes a command only if a gm is detected around you");
        lstrcat(v141 + 32, "\n\r\n\rExample: auto 200 ifgm { wait 5000 | say oooh! | wait 6000 | say sup | turnoff } - greets gm when he comes and turns the hotkey off");
        *((char *)(v141 + 1056)) = 7;
        *((unsigned int *)(v141 + 1060)) = 0;
        v142 = v141 + 1064;
        lstrcpy(v142, "ifnogm");
        lstrcat(v142 + 32, "executes a command only if a gm is not detected around you");
        lstrcat(v142 + 32, "\n\r\n\rExample: auto 200 ifnogm mphigher 60 say exura - casts the exura spell when your mp is higher than 60 only if a gm is not around you");
        *((char *)(v142 + 1056)) = 7;
        *((unsigned int *)(v142 + 1060)) = 0;
        v143 = v142 + 1064;
        lstrcpy(v143, "ifplayeronscreen");
        lstrcat(v143 + 32, "executes a command only if a player is on your screen");
        lstrcat(v143 + 32, "\n\r\n\rExample: auto 200 ifplayeronscreen { wait 4000 | say hi there wait 120000 } - says hi there if a player enters your screen, and waits 2 minutes");
        *((char *)(v143 + 1056)) = 7;
        *((unsigned int *)(v143 + 1060)) = 0;
        v144 = v143 + 1064;
        lstrcpy(v144, "ifnoplayeronscreen");
        lstrcat(v144 + 32, "executes a command only if a player is not on your screen");
        lstrcat(v144 + 32, "\n\r\n\rExample: auto 200 ifnoplayeronscreen mphigher 90 say adori - makes a hmm rune only if a player is not on your screen");
        *((char *)(v144 + 1056)) = 7;
        *((unsigned int *)(v144 + 1060)) = 0;
        v145 = v144 + 1064;
        lstrcpy(v145, "ifhasted");
        lstrcat(v145 + 32, "executes a command only if you are hasted");
        lstrcat(v145 + 32, "\n\r\n\rExample: ifhasted equipring 1234 - equips ring 1234 if you are hasted");
        *((char *)(v145 + 1056)) = 7;
        *((unsigned int *)(v145 + 1060)) = 0;
        v146 = v145 + 1064;
        lstrcpy(v146, "ifnothasted");
        lstrcat(v146 + 32, "executes a command only if you are not hasted");
        lstrcat(v146 + 32, "\n\r\n\rExample: ifnothasted say uTaNi HuR - casts haste if you are not hasted");
        *((char *)(v146 + 1056)) = 7;
        *((unsigned int *)(v146 + 1060)) = 0;
        v147 = v146 + 1064;
        lstrcpy(v147, "ifmanashielded");
        lstrcat(v147 + 32, "executes a command only if you are manashielded");
        lstrcat(v147 + 32, "\n\r\n\rExample: ifmanashielded mplower 500 gmana self - uses a great mana potion on yourself if you are manashielded and your mp is lower than 500");
        *((char *)(v147 + 1056)) = 7;
        *((unsigned int *)(v147 + 1060)) = 0;
        v148 = v147 + 1064;
        lstrcpy(v148, "ifnotmanashielded");
        lstrcat(v148 + 32, "executes a command only if you are not manashielded");
        lstrcat(v148 + 32, "\n\r\n\rExample: ifnotmanashielded say uTaMo ViTa - casts utamo vita if you are not manashielded");
        *((char *)(v148 + 1056)) = 7;
        *((unsigned int *)(v148 + 1060)) = 0;
        v149 = v148 + 1064;
        lstrcpy(v149, "ifpoisoned");
        lstrcat(v149 + 32, "executes a command only if you are poisoned");
        lstrcat(v149 + 32, "\n\r\n\rExample: ifpoisoned say exana pox - casts antidote spell if you are poisoned");
        *((char *)(v149 + 1056)) = 7;
        *((unsigned int *)(v149 + 1060)) = 0;
        v150 = v149 + 1064;
        lstrcpy(v150, "ifparalyzed");
        lstrcat(v150 + 32, "executes a command only if you are paralyzed");
        lstrcat(v150 + 32, "\n\r\n\rExample: ifparalyzed say exura - casts healing spell if you are paralyzed");
        *((char *)(v150 + 1056)) = 7;
        *((unsigned int *)(v150 + 1060)) = 0;
        v151 = v150 + 1064;
        lstrcpy(v151, "ifnotparalyzed");
        lstrcat(v151 + 32, "executes a command only if you are paralyzed");
        *((char *)(v151 + 1056)) = 7;
        *((unsigned int *)(v151 + 1060)) = 0;
        v152 = v151 + 1064;
        lstrcpy(v152, "isattackedname");
        lstrcat(v152 + 32, "exectues the command only if your attackbox target is of a specific name. The target must be on screen.");
        lstrcat(v152 + 32, "\n\r\n\rExample: isattackedname 'Demon' say exori vis");
        *((char *)(v152 + 1056)) = 7;
        *((unsigned int *)(v152 + 1060)) = 3;
        v153 = v152 + 1064;
        lstrcpy(v153, "islocation");
        lstrcat(v153 + 32, "for cavebot action scripts only. Will execute the command only if the character is standing at the location where the action waypoint was set.");
        lstrcat(v153 + 32, "\n\r\n\rExample: islocation dropitems 1234 - will drop all items with id 1234 only if you are standing at the location where the action waypoint was set.");
        *((char *)(v153 + 1056)) = 7;
        *((unsigned int *)(v153 + 1060)) = 0;
        v154 = v153 + 1064;
        lstrcpy(v154, "isnotlocation");
        lstrcat(v154 + 32, "for cavebot action scripts only. Will execute the command only if the character is NOT standing at the location where the action waypoint was set.");
        lstrcat(v154 + 32, "\n\r\n\rExample: isnotlocation gotolabel runagain - will go to waypoint labeled 'runagain' if the character did not meet a certain final location");
        *((char *)(v154 + 1056)) = 7;
        *((unsigned int *)(v154 + 1060)) = 0;
        v155 = v154 + 1064;
        lstrcpy(v155, "isonscreen");
        lstrcat(v155 + 32, "only exectues a command if a creature with a certain name is on screen. Note that the name needs to be put between single quotes ('name').");
        lstrcat(v155 + 32, "\n\r\n\rExample: auto 200 isonscreen 'Demon Skeleton' goinvisible - will go invisible if a Demon Skeleton appears on your screen");
        *((char *)(v155 + 1056)) = 7;
        *((unsigned int *)(v155 + 1060)) = 3;
        v156 = v155 + 1064;
        lstrcpy(v156, "isnotonscreen");
        lstrcat(v156 + 32, "only exectues a command if a creature with a certain name is not on screen. Note that the name needs to be put between single quotes ('name').");
        lstrcat(v156 + 32, "\n\r\n\rExample: auto 200 isnotonscreen 'Demon Skeleton' playsound missing.wav - will play a sound file when your summoned Demon Skeleton disappears.");
        *((char *)(v156 + 1056)) = 7;
        *((unsigned int *)(v156 + 1060)) = 3;
        v157 = v156 + 1064;
        lstrcpy(v157, "isposz");
        lstrcat(v157 + 32, "exectues the command only if your z position is equal to a certain amount");
        lstrcat(v157 + 32, "\n\r\n\rExample: isposz 8 gotowaypoint gofromfloor8 - will go to label gofromfloor8 if you are on floor level 8");
        *((char *)(v157 + 1056)) = 7;
        *((unsigned int *)(v157 + 1060)) = 2;
        v158 = v157 + 1064;
        lstrcpy(v158, "istargeting");
        lstrcat(v158 + 32, "exectues the command only if the targeting system is currently dealing with a target");
        lstrcat(v158 + 32, "\n\r\n\rExample: istargeting isattackedname 'Rotworm' say exori vis - casts energy strike if the target is a Rotworm and if Targeting is on/targeting it.");
        *((char *)(v158 + 1056)) = 7;
        *((unsigned int *)(v158 + 1060)) = 0;
        v159 = v158 + 1064;
        lstrcpy(v159, "isnottargeting");
        lstrcat(v159 + 32, "exectues the command only if the targeting system is not currently dealing with a target");
        lstrcat(v159 + 32, "\n\r\n\rExample: isnottargeting skin 1234 - skin corpses 1234 if the targeting system isn't currently dealing with a creature");
        *((char *)(v159 + 1056)) = 7;
        *((unsigned int *)(v159 + 1060)) = 0;
        v160 = v159 + 1064;
        lstrcpy(v160, "istargetname");
        lstrcat(v160 + 32, "exectues the command only if your target is of a specific name. The target must be on screen.");
        lstrcat(v160 + 32, "\n\r\n\rExample: istargetname 'Demon' icicle target - shoots an icicle on the target if his name is Demon");
        *((char *)(v160 + 1056)) = 7;
        *((unsigned int *)(v160 + 1060)) = 3;
        v161 = v160 + 1064;
        lstrcpy(v161, "hplower");
        lstrcat(v161 + 32, "only executes the command if your hitpoints are lower than a certain amount");
        lstrcat(v161 + 32, "\n\r\n\rExample: hplower 500 equipammy 1234 - Useful on 'auto'. Will equip the amulet with id 1234 if your hp goes below 500");
        *((char *)(v161 + 1056)) = 7;
        *((unsigned int *)(v161 + 1060)) = 2;
        v162 = v161 + 1064;
        lstrcpy(v162, "hphigher");
        lstrcat(v162 + 32, "only executes the command if your hp is higher or EQUAL to a certain amount");
        lstrcat(v162 + 32, "\n\r\n\rExample: hphigher 500 equipammy 1235 - Useful on 'auto'. Will equip the amulet with id 1235 if your hp goes above or equal to 500");
        *((char *)(v162 + 1056)) = 7;
        *((unsigned int *)(v162 + 1060)) = 2;
        v163 = v162 + 1064;
        lstrcpy(v163, "hpmissinglower");
        lstrcat(v163 + 32, "only executes the command the hitpoints that you are missing from your max hp are lower than a certain amount");
        lstrcat(v163 + 32, "\n\r\n\rExample: hpmissinglower 100 equipammy 1234 - equips amulet 1234 if you are missing less than 100 hp");
        *((char *)(v163 + 1056)) = 7;
        *((unsigned int *)(v163 + 1060)) = 2;
        v164 = v163 + 1064;
        lstrcpy(v164, "hpmissinghigher");
        lstrcat(v164 + 32, "only executes the command the hitpoints that you are missing from your max hp are higher OR EQUAL than a certain amount");
        lstrcat(v164 + 32, "\n\r\n\rExample: hpmissinghigher 100 say exura - casts 'exura' if you are missing 100 hp or more");
        *((char *)(v164 + 1056)) = 7;
        *((unsigned int *)(v164 + 1060)) = 2;
        v165 = v164 + 1064;
        lstrcpy(v165, "mplower");
        lstrcat(v165 + 32, "only executes the command if your mp is lower than a certain amount");
        lstrcat(v165 + 32, "\n\r\n\rExample: mplower 500 mana self - Useful on 'auto'. Will drink a mana fluid if your mp goes below 500");
        *((char *)(v165 + 1056)) = 7;
        *((unsigned int *)(v165 + 1060)) = 2;
        v166 = v165 + 1064;
        lstrcpy(v166, "mphigher");
        lstrcat(v166 + 32, "only executes the command if your mp is higher or EQUAL to a certain amount");
        lstrcat(v166 + 32, "\n\r\n\rExample: mphigher 20 say exori vis - will cast 'energy strike' only if you have at least 20 mana");
        *((char *)(v166 + 1056)) = 7;
        *((unsigned int *)(v166 + 1060)) = 2;
        v167 = v166 + 1064;
        lstrcpy(v167, "mpmissinglower");
        lstrcat(v167 + 32, "only executes the command the amount of mana that you are missing from your max mp is lower than a certain amount");
        lstrcat(v167 + 32, "\n\r\n\rExample: mpmissinglower 5 say exura - says exura if you are missing less than 5 mp");
        *((char *)(v167 + 1056)) = 7;
        *((unsigned int *)(v167 + 1060)) = 2;
        v168 = v167 + 1064;
        lstrcpy(v168, "mpmissinghigher");
        lstrcat(v168 + 32, "only executes the command the amount of mana that you are missing from your max mp is higher OR EQUAL than a certain amount");
        lstrcat(v168 + 32, "\n\r\n\rExample: mpmissinghigher 1000 gmana self - uses a great mana potion if your mp is missing 1000 mana or more");
        *((char *)(v168 + 1056)) = 7;
        *((unsigned int *)(v168 + 1060)) = 2;
        v169 = v168 + 1064;
        lstrcpy(v169, "safe");
        lstrcat(v169 + 32, "only executes the command if the bot isn't currently trying to heal you with the settings specified in the GUI. It is no longer useful for attack commands since you can attack and heal with magic at the same time");
        lstrcat(v169 + 32, "; however, you might still want to place it in front of heal friend commands to heal yourself over your friends.");
        lstrcat(v169 + 32, "\n\r\n\rExample: safe sio 60 friend - will sio a friend only if you are not trying to heal yourself");
        *((char *)(v169 + 1056)) = 7;
        *((unsigned int *)(v169 + 1060)) = 0;
        v170 = v169 + 1064;
        lstrcpy(v170, "targethplower");
        lstrcat(v170 + 32, "only executes the command if your current target's (the one you're attacking) hp% is lower than a certain amount. Can be used with the 'exura gran', other combo commands or even sd runes.");
        lstrcat(v170 + 32, "\n\r\n\rExample: auto 200 targethplower 30 mphigher 1200 say exevo gran mas vis - when active, will automatically cast the 'Ultimate Explosion' spell if your target's hp goes below 30% and if you have at least 1200 mana. Can be dangerous if multiple people do it!");
        *((char *)(v170 + 1056)) = 7;
        *((unsigned int *)(v170 + 1060)) = 2;
        g_10072fc0 = CreateWindowExA(WS_EX_RIGHTSCROLLBAR, "tooltips_class32", NULL, 2147483715, -0x80000000, -0x80000000, -0x80000000, -0x80000000, a0, NULL, g_1005f60a, NULL);
        SetWindowPos(g_10072fc0, 0xffffffff, 0, 0, 0, 0, 19);
        SendMessageA(g_10072fc0, 1048, NULL, 0xfa);
        SendMessageA(g_10072fc0, 1027, 0x2, 0x7d00);
        SendMessageA(g_10072fc0, 1027, 0x1, 0x3e8);
        g_10042929 = CreateFontA(12, 0, 0, 0, 0, 0, 0, 0, 0xff, 0, 0, 0, 0, "Lucida Console");
        g_1005f616 = GetProcessHeap();
        lstrcpy(&g_10042f83, &g_10042d7b);
        lstrcat(&g_10042f83, "minimaps\\");
        CreateDirectoryA(&g_10042f83, NULL);
        lstrcpy(&g_10042f83, &g_10042d7b);
        lstrcat(&g_10042f83, "scripts\\");
        CreateDirectoryA(&g_10042f83, NULL);
        for (i = 0; i < 16; i += 1)
        {
            v1 = i;
            v0 = &g_10042d7b;
            wsprintfA(&g_10042f83, "%s\\minimaps\\%d\\");
            CreateDirectoryA(&g_10042f83, NULL);
        }
        lstrcpy(&g_10042f83, &g_10042d7b);
        sub_100030d6();
        lstrcpy(&g_10042e7f, &g_10042d7b);
        lstrcat(&g_10042e7f, "scripts\\");
        lstrcat(&g_10042d7b, "elfsettings\\");
        CreateDirectoryA(&g_10042d7b, NULL);
        sub_100244e1(v2, v3);
        sub_1001f57d(*((int *)&g_10072f80), 4000, sub_1001e3e5);
        sub_1001f57d(*((int *)&g_10072f88), 5000, sub_10007ec4);
        sub_1001f57d(*((int *)&g_10072fb8), 6000, sub_1001e313);
        sub_1001f57d(*((int *)&g_10072fbc), 7000, sub_10007ca5);
        sub_1001f57d(*((int *)&g_10072fc4), 8000, sub_10007b55);
        sub_1001f57d(g_10072f8c, 13000, sub_1001a715);
        sub_1001f57d(g_10072f94, 14000, sub_10019751);
        sub_1001f57d(g_10072f90, 18000, sub_1001b8be);
        sub_1000307e(a0, 1004, "The aimbot is the heart of the pvp-bot. Setup of the key features takes place in this panel. These settings affect the general behavior of the bot through hotkeys like 'autoaim' or comboing.");
        sub_1000307e(a0, 1001, "Several auto-healing methods can be set here. Different spells at different hitpoint levels and healing with both spells and potions at the same time is possible for paladins and knights.");
        sub_1000307e(a0, 1002, "Allies, enemies, sub-allies and sub-enemies can all be listed here to help the bot recognize who is who. Some options offered to you may also help you recognize them visually more easily.");
        sub_1000307e(a0, 1003, "The Heads-up-display can display various useful information on your screen at your leisure to help you visualize and evaluate the environment with better accuracy.");
        sub_1000307e(a0, 1013, "Extra options that don't fit in any of the other categories. Many miscellaneous features are located here.");
        sub_1000307e(a0, 1010, "The creature spy gives you a list of all players and monsters within range. It lists the floor that they are on, their name, position, health, speed and if available their experience level. It is useful to have a view on the entire surrounding in one place, without the need of spying on different floors.");
        sub_1000307e(a0, 1011, "Reconnects you to the game onto the same character that was last online.");
        sub_1000307e(a0, 0x404, "Most of the bot functionality relies on the use of advanced hotkey commands. The strenght of these hotkeys relies in their induced clever and quicker bot calculations & reactions, customizability, easy access & control and automated actions that can be quickly activated or deactivated as required by the situation. Another advantage is that most keys won't cancel your walking like regular Tibia hotkeys do, so you can for instance run and mana fluid at the same time.");
        sub_1000307e(a0, 1005, "Very similar to hotkeys, shortkeys have the same functionality with the difference that they get triggered differently. Instead of pressing a key to execute a command, shortkeys trigger by writing some defined short text in default chat. For example, you can set up a shortkey 't' that has for command 'say hi thais yes' to enabled you to quickly travel boats, or one for 'pt' that has for command 'say please bring me to thais'. All you would then have to do then is to type p/pt in default chat and have it say the complete sentence for you. All in all, it's the same thing as hotkeys with a different triggering method, which may be more convenient in some cases.");
        sub_1000307e(a0, 1029, "Links is a never before seen feature in bot technology. It allows 2 or more people to control or merely watch the same character. It takes for the person that will be normally logged on the character to start a links server on his computer to which other people will connect and exchange information with. The additional people don't need and won't obtain the account number and password of the character when doing this. It is still recommended to do this with people you trust a little, seeing as giving your ip address away may be a slight security risk (but comparable to using ventrilo, sending files over msn or visting outside websites). Some ideas can be to link with yourself and have 2 clients open scouting the floors above and below yourself at all times, to have an extra view of your friend in a war, or to watch someone perform quests or other events.");
        sub_1000307e(a0, 1042, "The navigation system was created to easily coordinate team movements as well to lighten up and ease communication of enemy and friend positions and activities.To do this, it takes someone to host a (provided) navigation server which will share information with every ally that is connected to it through the bot. Every friend connected will communicate his exact position to all other allies connected to the server. Furthermore, if a friend sees an enemy that is on his enemy list he will send the coordinates of that player to everyone else connected. All those will appear on your screen in the direction that they are situated (displaying must be enabled in HUD options).");
        sub_1000307e(a0, 1606, "This will save the settings for the character that is currently online on the current save slot and apply all the settings that were made in the bot panels. Make sure you remember to press this button every time you change a setting.");
        sub_1000307e(a0, 1017, "This will load the settings for the character that is currently online from the current save slot.");
        sub_1000307e(a0, 1043, "Clicking on this button will choose slot 1 as the save slot for this character. This is also the default slot when the bot starts.");
        sub_1000307e(a0, 1044, "Clicking on this button will choose slot 2 as the save slot for this character.");
        sub_1000307e(a0, 1045, "Clicking on this button will choose slot 3 as the save slot for this character.");
        sub_1000307e(a0, 1046, "Clicking on this button will choose slot 4 as the save slot for this character.");
        sub_1000307e(a0, 1047, "Clicking on this button will choose slot 5 as the save slot for this character.");
        sub_1000307e(a0, 1006, "An advanced cavebot with various AI behaviours for hunting different kinds of monsters as different vocations. It will be finished in the next major release.");
        sub_1000307e(a0, 1007, "Contains a handful of useful tips for operating ElfBot NG.");
        if (*((int *)0x64a9c0) == 31)
            return 0;
        lstrcpy(&g_1005dc8c, &g_10042d7b);
        lstrcat(&g_1005dc8c, "Startup");
        g_100f9315 = 1;
        sub_1001f5bd(g_10072f90, 18000);
        return 0;
    }
    else if (v5 == 273)
    {
        switch (a2)
        {
        case 1001:
            sub_1001f57d(*((int *)&g_10072f80), 4000, sub_1001e3e5);
            return 0;
        case 1002:
            sub_1001f57d(*((int *)&g_10072fb8), 6000, sub_1001e313);
            return 0;
        case 1003:
            sub_1001f57d(*((int *)&g_10072fc4), 8000, sub_10007b55);
            return 0;
        case 1004:
            sub_1001f57d(*((int *)&g_10072fbc), 7000, sub_10007ca5);
            return 0;
        case 1005:
            sub_1001f57d(g_10072fcc, 10000, sub_10006d3b);
            return 0;
        case 1006:
            sub_1001f57d(g_10072f94, 14000, sub_10019751);
            return 0;
        case 1007:
            MessageBoxA(a0, "Welcome to ElfBot NG!\n\r\n\rThe main panel has several subsections that contain settings related to them within. This panel can be brought at any time by pressing 'Shift+F12'. A lighthack is also available to you and can be toggled by pressing 'Shift+F11'. \n\r\n\rWhen changing settings, it is IMPORTANT that you realise that you need to hit the 'Save' button on the main panel for them to apply and become active in game. Also, each character has 5 save slots available to him. There isn't just 5 slots for all your characters. \n\r\n\rSome bot function work straight from the interface, but for most others you will have to operate them through hotkeys and shortkeys. There is a wizard for creating those and you can also visit the forums and website for more examples. \n\r\n\rThe website for ElfBot NG is: http://elfbot.tibiabot.com. The ElfBot NG forums are a subcategory of the TibiaBot NG forums. Happy ElfBotting! ", "ElfBot NG Help", MB_APPLMODAL);
            return 0;
        case 1008:
            sub_1001f57d(g_10072f78, 12000, sub_1001ef0c);
            return 0;
        case 1009:
            sub_1001f57d(g_10072f8c, 13000, sub_1001a715);
            return 0;
        case 1010:
            sub_1001f57d(g_10072f70, 1900, sub_10006bce);
            return 0;
        case 1011:
            sub_10039bbb();
            return 0;
        case 1013:
            sub_1001f57d(*((int *)&g_10072f88), 5000, sub_10007ec4);
            return 0;
        case 1014:
            sub_1001f57d(g_10072f90, 18000, sub_1001b8be);
            return 0;
        case 1017:
            sub_1001f5bd();
            return 0;
        case 1028:
            sub_1001f57d(g_10072f84, 3000, sub_10007360);
            return 0;
        case 1029:
            sub_1001f57d(g_10072f74, 2200, sub_1001eb33);
            return 0;
        case 1042:
            sub_1001f57d(g_10072f7c, 2201, sub_1001e7c3);
            return 0;
        case 1606:
            g_100f94c9 = (char)SendDlgItemMessageA(*((int *)&g_10072fbc), 1011, 240, NULL, NULL);
            g_1013f27d = (char)SendDlgItemMessageA(*((int *)&g_10072fbc), 1003, 240, NULL, NULL);
            g_100fa4ef = (char)SendDlgItemMessageA(*((int *)&g_10072fbc), 1010, 240, NULL, NULL);
            g_100fa97a = (char)SendDlgItemMessageA(*((int *)&g_10072fbc), 1008, 240, NULL, NULL);
            g_10134e6a = (char)SendDlgItemMessageA(*((int *)&g_10072fbc), 1002, 240, NULL, NULL);
            g_1013f320 = SendDlgItemMessageA(*((int *)&g_10072fbc), 1001, 240, NULL, NULL);
            if (!g_1013f320)
                g_63fe5c = 0;
            g_1013526b = 0;
            g_100fa97b = (char)SendDlgItemMessageA(*((int *)&g_10072fbc), 1007, 240, NULL, NULL);
            SendDlgItemMessageA(*((int *)&g_10072fbc), 1015, 13, 0x400, &g_10134e6b);
            SendDlgItemMessageA(*((int *)&g_10072fbc), 1017, 13, 0x20, &g_1014f38a);
            SendDlgItemMessageA(*((int *)&g_10072fbc), 0x3fe, 13, 0x20, &g_1014f3ca);
            SendDlgItemMessageA(*((int *)&g_10072fbc), 0x3fc, 13, 0x20, &g_1014f3aa);
            SendDlgItemMessageA(*((int *)&g_10072fbc), 1037, 13, 0x20, &g_101d5e2c);
            SendDlgItemMessageA(*((int *)&g_10072fbc), 1039, 13, 0x20, &g_101d5e4c);
            g_1014f40a = (char)SendDlgItemMessageA(*((int *)&g_10072fbc), 1027, 240, NULL, NULL);
            g_1014f40b = (char)SendDlgItemMessageA(*((int *)&g_10072fbc), 1033, 240, NULL, NULL);
            g_1014f40c = (char)SendDlgItemMessageA(*((int *)&g_10072fbc), 0x404, 240, NULL, NULL);
            g_1014f40d = (char)SendDlgItemMessageA(*((int *)&g_10072fbc), 1009, 240, NULL, NULL);
            g_1014f40e = (char)SendDlgItemMessageA(*((int *)&g_10072fbc), 1025, 240, NULL, NULL);
            g_1014f40f = (char)SendDlgItemMessageA(*((int *)&g_10072fbc), 1026, 240, NULL, NULL);
            g_101d5e6c = (char)SendDlgItemMessageA(*((int *)&g_10072fbc), 1040, 240, NULL, NULL);
            count = SendDlgItemMessageA(*((int *)&g_10072fbc), 1012, 392, NULL, NULL);
            if (count != 0xffffffff)
            {
                g_100f94cb = g_100f94cb & 63;
                g_100f94cb = g_100f94cb | count * 64;
            }
            count1 = SendDlgItemMessageA(*((int *)&g_10072fbc), 1006, 392, NULL, NULL);
            if (count1 != 0xffffffff)
            {
                g_100f94cb = g_100f94cb & 0xffffffc0;
                g_100f94cb = g_100f94cb | count1;
            }
            g_1013f27f = (char)SendDlgItemMessageA(*((int *)&g_10072fbc), 1004, 240, NULL, NULL);
            g_1014f41e = (char)SendDlgItemMessageA(*((int *)&g_10072fbc), 1036, 240, NULL, NULL);
            g_1014f41f = (char)SendDlgItemMessageA(*((int *)&g_10072fbc), 0x400, 240, NULL, NULL);
            g_101d5e2a = (char)SendDlgItemMessageA(*((int *)&g_10072fbc), 1042, 392, NULL, NULL);
            g_100f94ca = (char)SendDlgItemMessageA(*((int *)&g_10072f88), 1004, 240, NULL, NULL);
            g_100f94c6 = (char)SendDlgItemMessageA(*((int *)&g_10072f88), 1006, 240, NULL, NULL);
            g_1013f27e = (char)SendDlgItemMessageA(*((int *)&g_10072f88), 1003, 240, NULL, NULL);
            g_1013f324 = (char)SendDlgItemMessageA(*((int *)&g_10072f88), 1005, 240, NULL, NULL);
            g_1013f325 = (char)SendDlgItemMessageA(*((int *)&g_10072f88), 1007, 240, NULL, NULL);
            g_1013f326 = (char)SendDlgItemMessageA(*((int *)&g_10072f88), 1008, 240, NULL, NULL);
            g_100fa4f0 = ~(SendDlgItemMessageA(*((int *)&g_10072f88), 1009, 240, NULL, NULL)) & 1;
            g_1014f416 = (char)SendDlgItemMessageA(*((int *)&g_10072f88), 1010, 240, NULL, NULL);
            g_1014f417 = (char)SendDlgItemMessageA(*((int *)&g_10072f88), 1011, 240, NULL, NULL);
            g_1014f418 = (char)SendDlgItemMessageA(*((int *)&g_10072f88), 1012, 240, NULL, NULL);
            g_101d5e27 = (char)SendDlgItemMessageA(*((int *)&g_10072f88), 1014, 240, NULL, NULL);
            g_101d5e29 = (char)SendDlgItemMessageA(*((int *)&g_10072f88), 1015, 240, NULL, NULL);
            g_101d5e6d = (char)SendDlgItemMessageA(*((int *)&g_10072f88), 1016, 240, NULL, NULL);
            g_101d5e73 = (char)SendDlgItemMessageA(*((int *)&g_10072f88), 1017, 240, NULL, NULL);
            g_101d5e72 = (char)SendDlgItemMessageA(*((int *)&g_10072f88), 1018, 240, NULL, NULL);
            g_100f94c8 = (char)SendDlgItemMessageA(*((int *)&g_10072fc4), 1005, 240, NULL, NULL);
            g_100fa579 = (char)SendDlgItemMessageA(*((int *)&g_10072fc4), 1003, 240, NULL, NULL);
            g_1013526d = (char)SendDlgItemMessageA(*((int *)&g_10072fc4), 1012, 240, NULL, NULL);
            g_1013526e = (char)SendDlgItemMessageA(*((int *)&g_10072fc4), 1011, 240, NULL, NULL);
            g_1013526f = (char)SendDlgItemMessageA(*((int *)&g_10072fc4), 1014, 240, NULL, NULL);
            g_10135270 = (char)SendDlgItemMessageA(*((int *)&g_10072fc4), 1013, 240, NULL, NULL);
            g_10135271 = (char)SendDlgItemMessageA(*((int *)&g_10072fc4), 1010, 240, NULL, NULL);
            g_10135272 = (char)SendDlgItemMessageA(*((int *)&g_10072fc4), 1004, 240, NULL, NULL);
            g_10135273 = (char)SendDlgItemMessageA(*((int *)&g_10072fc4), 1002, 240, NULL, NULL);
            g_10135274 = (char)SendDlgItemMessageA(*((int *)&g_10072fc4), 1006, 240, NULL, NULL);
            g_10135275 = (char)SendDlgItemMessageA(*((int *)&g_10072fc4), 1008, 240, NULL, NULL);
            g_10135276 = (char)SendDlgItemMessageA(*((int *)&g_10072fc4), 1009, 240, NULL, NULL);
            g_10135277 = (char)SendDlgItemMessageA(*((int *)&g_10072fc4), 1015, 240, NULL, NULL);
            g_1013527a = (char)SendDlgItemMessageA(*((int *)&g_10072fc4), 1016, 240, NULL, NULL);
            g_101d5e20 = (char)SendDlgItemMessageA(*((int *)&g_10072fc4), 1017, 240, NULL, NULL);
            g_101d5e21 = (char)SendDlgItemMessageA(*((int *)&g_10072fc4), 1018, 240, NULL, NULL);
            sub_1002b02b(1);
            SendDlgItemMessageA(*((int *)&g_10072f80), 0x3ff, 13, 0x40, &g_100fa4f1);
            SendDlgItemMessageA(*((int *)&g_10072f80), 0x3fc, 13, 0x20, &g_1005f651);
            g_100f9495 = sub_10040900(&g_1005f651);
            SendDlgItemMessageA(*((int *)&g_10072f80), 1018, 13, 0x20, &g_1005f651);
            g_100f9499 = sub_10040900(&g_1005f651);
            SendDlgItemMessageA(*((int *)&g_10072f80), 1009, 13, 0x40, &g_100fa531);
            SendDlgItemMessageA(*((int *)&g_10072f80), 1011, 13, 0x20, &g_1005f651);
            g_100fa575 = sub_10040900(&g_1005f651);
            SendDlgItemMessageA(*((int *)&g_10072f80), 1013, 13, 0x20, &g_1005f651);
            g_100fa571 = sub_10040900(&g_1005f651);
            SendDlgItemMessageA(*((int *)&g_10072f80), 1016, 13, 0x20, &g_1005f651);
            g_100f949d = sub_10040900(&g_1005f651);
            SendDlgItemMessageA(*((int *)&g_10072f80), 1006, 13, 0x20, &g_1005f651);
            g_10134e66 = sub_10040900(&g_1005f651);
            SendDlgItemMessageA(*((int *)&g_10072f80), 1029, 13, 0x20, &g_1005f651);
            g_1014f41a = sub_10040900(&g_1005f651);
            count2 = SendDlgItemMessageA(*((int *)&g_10072f80), 1034, 392, NULL, NULL);
            if (count2 != 0xffffffff)
                g_100f94c1 = count2;
            v175 = SendDlgItemMessageA(*((int *)&g_10072f80), 1014, 392, NULL, NULL);
            if (v175 != 0xffffffff)
                g_1014f410 = v175;
            v176 = SendDlgItemMessageA(*((int *)&g_10072f80), 1003, 392, NULL, NULL);
            if (v176 != 0xffffffff)
                g_10134e63 = *((char *)&v176);
            v177 = SendDlgItemMessageA(*((int *)&g_10072f80), 1032, 392, NULL, NULL);
            if (v177 != 0xffffffff)
                g_1014f419 = *((char *)&v177);
            v178 = SendDlgItemMessageA(*((int *)&g_10072f80), 1026, 392, NULL, NULL);
            if (v178 != 0xffffffff)
                g_10134e64 = *((char *)&v178);
            v179 = SendDlgItemMessageA(*((int *)&g_10072f80), 0x400, 392, NULL, NULL);
            if (v179 != 0xffffffff)
                g_10134e65 = *((char *)&v179);
            v180 = SendDlgItemMessageA(*((int *)&g_10072f80), 1032, 392, NULL, NULL);
            if (v180 != 0xffffffff)
                g_1014f415 = *((char *)&v180);
            SendDlgItemMessageA(*((int *)&g_10072fb8), 1003, 13, 0x5000, &g_1012ad5f);
            SendDlgItemMessageA(*((int *)&g_10072fb8), 1002, 13, 0x5000, &g_1012fd60);
            SendDlgItemMessageA(*((int *)&g_10072fb8), 1011, 13, 0x5000, &g_1013527b);
            SendDlgItemMessageA(*((int *)&g_10072fb8), 1008, 13, 0x5000, &g_1013a27c);
            SendDlgItemMessageA(*((int *)&g_10072fb8), 1014, 13, 0x20, &g_1014f3ea);
            g_100f94c7 = (char)SendDlgItemMessageA(*((int *)&g_10072fb8), 1006, 240, NULL, NULL);
            g_10135278 = (char)SendDlgItemMessageA(*((int *)&g_10072fb8), 1007, 240, NULL, NULL);
            g_101d5e6e = (char)SendDlgItemMessageA(*((int *)&g_10072fb8), 1017, 240, NULL, NULL);
            g_101d5e6f = (char)SendDlgItemMessageA(*((int *)&g_10072fb8), 1018, 240, NULL, NULL);
            g_101d5e70 = (char)SendDlgItemMessageA(*((int *)&g_10072fb8), 0x3fc, 240, NULL, NULL);
            g_101d5e71 = (char)SendDlgItemMessageA(*((int *)&g_10072fb8), 1019, 240, NULL, NULL);
            sub_10039d8a(&g_1005f651, &g_1005f651, &g_1005f651, &g_1005f651, &g_1005f651);
            sub_100200ff();
            return 0;
        default:
            if (a2 >= 1043 && a2 <= 1047)
            {
                g_100445f1 = a2 - 1042;
                g_1005dc8c = 0;
                g_100f9315 = 0;
                return 0;
            }
            if (a2 != 1012)
                return 0;
            sub_10006b62();
            return 0;
        }
    }
    else if (v5 == 1337)
    {
        sub_1002b02b(a2);
        return 0;
    }
    else if (v5 == 16)
    {
        ShowWindow(a0, SW_HIDE);
        g_1005f609 = 0;
        return 0;
    }
    else if (a1 == 2)
    {
        PostQuitMessage(0);
        return 0;
    }
    else
    {
        return (unsigned int)sub_10002c6e(a0, a1, a2, a3);
    }
}
```

## `sub_10006b62` `0x10006b62`

_108 bytes. refs "All Files"_

```c
typedef struct OPENFILENAMEA {
    unsigned int lStructSize;
    HWND hwndOwner;
    HINSTANCE hInstance;
    PSTR lpstrFilter;
    PSTR lpstrCustomFilter;
    unsigned int nMaxCustFilter;
    unsigned int nFilterIndex;
    PSTR lpstrFile;
    unsigned int nMaxFile;
    PSTR lpstrFileTitle;
    unsigned int nMaxFileTitle;
    PSTR lpstrInitialDir;
    PSTR lpstrTitle;
    enum OPEN_FILENAME_FLAGS Flags;
    unsigned short nFileOffset;
    unsigned short nFileExtension;
    PSTR lpstrDefExt;
    LPARAM lCustData;
    void* lpfnHook;
    PSTR lpTemplateName;
    void* pvReserved;
    unsigned int dwReserved;
    enum OPEN_FILENAME_FLAGS_EX FlagsEx;
} OPENFILENAMEA;

extern char g_10042d7b;
extern char g_1005dc8c;
extern unsigned int g_1005f60a;
extern unsigned int g_1005f626;
extern char g_100f9315;

int sub_10006b62(void)
{
    int v3;  // eax
    unsigned int v0;  // [bp-0x5c]
    OPENFILENAMEA v1;  // [bp-0x50]

    v1.pvReserved = &v1.dwReserved;
    sub_1002ae81(&v1, 76);
    v1.lStructSize = 76;
    v0 = g_1005f626;
    v1.hwndOwner = g_1005f626;
    v0 = g_1005f60a;
    v1.hInstance = g_1005f60a;
    v1.lpstrFilter = "All Files";
    v1.lpstrFile = &g_1005dc8c;
    v1.nMaxFile = 260;
    *((unsigned int *)&v1.Flags) = 2621444;
    v1.lpstrTitle = "Select or type a filename to be used as save slot";
    v1.lpstrInitialDir = &g_10042d7b;
    v3 = GetOpenFileNameA(&v1);
    if (v3)
        g_100f9315 = 0;
    return v3;
}
```

## dlgProc_HudCreatureList `0x10006bce`

Named — see [doc 10](../../10-*.md). _149 bytes. calls SendDlgItemMessageA_

```c
extern WPARAM g_10042929;
extern unsigned int g_10072f70;
extern int g_10072fd4;

int sub_10006bce(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v0;  // [bp-0x214]

    if (a1 == 272)
    {
        SendDlgItemMessageA(a0, 1901, 48, g_10042929, NULL);
        sub_1002ae81(&g_10072fd4, 16800);
        v0 = a0;
        g_10072f70 = a0;
        return 0;
    }
    else if (a1 == 20)
    {
        return 20;
    }
    else if (a1 == 5)
    {
        MoveWindow(GetDlgItem(a0, 1901), 0, 0, (unsigned short)a3, a3 >> 16, 1);
        return 0;
    }
    else
    {
        return (unsigned int)sub_10002c6e(a0, a1, a2, a3);
    }
}
```

## `sub_10006c1b` `0x10006c1b`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10006c1b(void)
{
}
```

## `sub_10006c65` `0x10006c65`

_107 bytes. calls SendDlgItemMessageA_

```c
extern HWND g_10072f84;

int sub_10006c65(unsigned int a0, WPARAM a1)
{
    int v2;  // ecx

    SendDlgItemMessageA(g_10072f84, 4000 + a0, 241, a1, NULL);
    EnableWindow(GetDlgItem(g_10072f84, 5000 + a0), _INSERT(a1, 0, !a1));
    v2 = _INSERT(a1, 0, !a1);
    return EnableWindow(GetDlgItem(g_10072f84, 6000 + a0), v2);
}
```

## `sub_10006cd0` `0x10006cd0`

_107 bytes. calls SendDlgItemMessageA_

```c
extern HWND g_10072fcc;

int sub_10006cd0(unsigned int a0, WPARAM a1)
{
    int v2;  // ecx

    SendDlgItemMessageA(g_10072fcc, 4000 + a0, 241, a1, NULL);
    EnableWindow(GetDlgItem(g_10072fcc, 5000 + a0), _INSERT(a1, 0, !a1));
    v2 = _INSERT(a1, 0, !a1);
    return EnableWindow(GetDlgItem(g_10072fcc, 6000 + a0), v2);
}
```

## dlgProc_Shortkeys `0x10006d3b`

Named — see [doc 10](../../10-*.md). _1573 bytes. calls CreateWindowExA, SendDlgItemMessageA, SendMessageA; refs ");
        sub_1000307e(a0, 1003, ", ");
        sub_1000307e(a0, 1003, ", "MS Sans Serif"_

```c
typedef struct WINDOWPLACEMENT {
    unsigned int length;
    enum WINDOWPLACEMENT_FLAGS flags;
    unsigned int showCmd;
    POINT ptMinPosition;
    POINT ptMaxPosition;
    RECT rcNormalPosition;
} WINDOWPLACEMENT;

typedef struct struct_0 {
    char padding_0[33];
    char field_21;
} struct_0;

typedef struct POINT {
    int x;
    int y;
} POINT;

typedef struct RECT {
    int left;
    int top;
    int right;
    int bottom;
} RECT;

extern Byte g_100429fa;
extern int g_1005f520;
extern unsigned int g_1005f528;
extern LPARAM g_1005f52c;
extern WPARAM g_1005f530;
extern HINSTANCE g_1005f60a;
extern int g_10072fc8;
extern unsigned int g_10072fcc;
extern char g_10106b02;
extern char g_10106b23[4];
extern char g_10106b24[4];
extern char g_10135279;
extern int g_1013f327;

int sub_10006d3b(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v10;  // ecx
    unsigned int v11;  // ecx
    int j;  // ebx
    HWND v21;  // eax
    int v22;  // ecx
    int v24;  // ecx
    unsigned short v26;  // ax
    unsigned int v27;  // ebx
    unsigned int v12;  // ecx
    unsigned int i;  // ecx
    HWND v14;  // ebx
    unsigned int v15;  // eax
    void* count;  // eax
    unsigned int idx;  // edi
    HWND v18;  // eax
    unsigned int v19;  // ebx
    int v0;  // [bp-0xa4], Other Possible Types: unsigned int
    HWND v1;  // [bp-0xa0]
    int v2;  // [bp-0x84], Other Possible Types: char
    unsigned int iter;  // [bp-0x68]
    struct_0 *v4;  // [bp-0x64]
    HWND v5;  // [bp-0x40], Other Possible Types: unsigned int
    void* len;  // [bp-0x3c]
    WINDOWPLACEMENT v7;  // [bp-0x38]
    unsigned int v8;  // [bp-0xc]
    int v9;  // [bp-0x8]

    if (a1 == 272)
    {
        v0 = a0;
        g_10072fcc = a0;
        SendDlgItemMessageA(a0, 1005, 12, NULL, &g_1013f327);
        SendDlgItemMessageA(a0, 1001, 241, g_10135279, NULL);
        sub_1000307e(a0, 1001, "This option enables or disables the functionality of the below bot shortkeys.");
        sub_1000307e(a0, 1003, "Guides you through a comprehensive wizard for creating your own shortkey.");
        sub_1000307e(a0, 1003, "Enter a symbol with which will let you type elfbot commands in default chat if preceded by it. For example, if you use /, typing /say hi in default chat will make your character say hi.");
        v1 = GetDlgItem(a0, 1002);
        g_1005f528 = 0;
        v2 = (int)_INSERT(v2 CONCAT 0, 0, 28);
        *((unsigned int *)&(&v2)[4]) = 23;
        *((unsigned int *)&(&v2)[8]) = 0;
        *((unsigned int *)&(&v2)[16]) = 1;
        *((unsigned int *)&(&v2)[12]) = 96;
        *((unsigned int *)&(&v2)[20]) = 0;
        *((unsigned int *)&(&v2)[24]) = 0;
        SetScrollInfo(a0, SB_VERT, &v2, 1);
        len = CreateFontA(14, 0, 0, 0, 400, 0, 0, 0, 0xff, 0, 0, 2, 0, "MS Sans Serif");
        v9 = 24;
        GetWindowPlacement(a0, &v7);
        g_1005f520 = *((unsigned int *)((void*)&v7 + 36)) - *((unsigned int *)((void*)&v7 + 28));
        v10 = 0;
        iter = 0;
        while (true)
        {
            v11 = v10;
            if (v11 >= 127)
                break;
            v12 = v11 + 1;
            v10 = v12;
            if (!g_10106b24[546 * v11])
                continue;
            iter = v12;
            v10 = v12;
        }
        iter += 1;
        iter += 12;
        if (iter > 128)
            iter = 127;
        for (i = 0; i < iter; i = v8 + 1)
        {
            v8 = i;
            v4 = &(&g_10106b02)[546 * i];
            CreateWindowExA(WS_EX_RIGHTSCROLLBAR, "BUTTON", &g_100429fa, 1342242819, 10, v9, 16, 16, a0, 4000 + v8, g_1005f60a, NULL);
            sub_1000307e(a0, v8 + 4000, "When this checkbox is unchecked, the corresponding shortkey is available for editing, but will not work. Check this checkbox to make the shortkey active.");
            v5 = CreateWindowExA(WS_EX_STATICEDGE, "EDIT", &g_100429fa, 1342242944, 30, v9, 50, 16, a0, 5000 + v8, g_1005f60a, NULL);
            sub_1000307e(a0, v8 + 5000, "Place the shortkey text here that will trigger the command when said in default chat.");
            SendMessageA(v5, 48, len, NULL);
            SendMessageA(v5, 197, 0x21, NULL);
            SendMessageA(v5, 12, NULL, v4);
            v14 = CreateWindowExA(WS_EX_STATICEDGE, "EDIT", &g_100429fa, 1342242944, 84, v9, g_1005f520 - 94, 16, a0, 6000 + v8, g_1005f60a, NULL);
            sub_1000307e(a0, v8 + 6000, "Type or paste the desired bot shortkey command in here. The command must follow a specific syntax. You can use the Shortkey wizard by clicking on the 'Create Shortkey' button if you are not familiar with it.");
            SendMessageA(v14, 48, len, NULL);
            SendMessageA(v14, 12, NULL, v4 + 1);
            v9 += 24;
            sub_10006cd0(v8, v4->field_21);
        }
        return 0;
    }
    else if (a1 == 273)
    {
        v15 = a2;
        v5 = (unsigned short)v15;
        if ((unsigned short)v5 == 1003)
        {
            sub_1001f57d(g_10072fc8, 9000, sub_1001e1d9);
            return 0;
        }
        if ((unsigned short)v5 == 1001)
        {
            g_10135279 = (char)SendDlgItemMessageA(a0, 1001, 240, NULL, NULL);
            return 0;
        }
        if ((unsigned short)v5 == 1005)
        {
            SendDlgItemMessageA(a0, 1005, 13, 0x2, &g_1013f327);
            return 0;
        }
        if ((unsigned short)v5 >= 5000 && (unsigned short)v5 < 5128)
        {
            if ((unsigned short)(v15 >> 16) == 0x300)
            {
                SendMessageA(a3, 13, 0x21, &(&g_10106b02)[2730000 + 546 * v5]);
                return 0;
            }
            return 0;
        }
        if ((unsigned short)v5 >= 4000 && (unsigned short)v5 < 4128)
        {
            count = SendMessageA(a3, 240, NULL, NULL);
            idx = v5 - 4000;
            g_10106b23[546 * idx] = *((char *)&count);
            sub_10006cd0(idx, count);
            return 0;
        }
        if ((unsigned short)v5 < 6000)
            return 0;
        if ((unsigned short)v5 <= 6127)
        {
            SendMessageA(a3, 13, 0x200, &g_10106b24[3276000 + 546 * v5]);
            return 0;
        }
        return 0;
    }
    else if (a1 == 5)
    {
        v0 = a3;
        g_1005f52c = a3;
        v0 = a2;
        g_1005f530 = a2;
        v18 = GetDlgItem(a0, 1002);
        v19 = _INSERT(a3, 0, (unsigned short)a3 - 3);
        g_1005f520 = (unsigned short)v19;
        MoveWindow(v18, 3, 0, g_1005f520, v19 >> 16, 0);
        for (j = 0; j < 96 && (v21 = GetDlgItem(a0, j + 6000), v21); j += 1)
        {
            v22 = (j - g_1005f528) * 24 + 42;
            if (v22 < 36 || v22 > 40000)
                v22 = -100;
            v0 = v22;
            MoveWindow(v21, 84, v22, g_1005f520 - 94, 16, 0);
            v0 = v22;
            v24 = v22;
            MoveWindow(GetDlgItem(a0, j + 5000), 30, v24, 50, 16, 0);
            MoveWindow(GetDlgItem(a0, j + 4000), 9, v24, 16, 16, 0);
        }
        InvalidateRect(a0, NULL, 1);
        return 0;
    }
    else if (a1 == 277)
    {
        v26 = (unsigned short)a2 ^ 65535;
        v27 = a2 >> 16;
        v0 = g_1005f528;
        if (v26 == 65527)
            return 0;
        if (v26 == 65534)
        {
            v27 = g_1005f528 + 1;
        }
        else if (v26 == 65535)
        {
            v27 = g_1005f528;
            if (g_1005f528)
                v27 = g_1005f528 - 1;
        }
        else if (v26 == 65532)
        {
            v27 = g_1005f528 + 4;
            if (v27 > 95)
                v27 = 95;
        }
        else if (v26 == 65533)
        {
            v27 = (g_1005f528 < 4 ? 0 : g_1005f528 - 4);
        }
        g_1005f528 = v27;
        sub_100409e0(&v2, 0, 28);
        v2 = (int)_INSERT(v2 CONCAT 0, 0, 28);
        *((unsigned int *)&(&v2)[4]) = 20;
        *((unsigned int *)&(&v2)[20]) = v27;
        *((unsigned int *)&(&v2)[24]) = v27;
        SetScrollInfo(a0, SB_VERT, &v2, 1);
        SendMessageA(a0, 5, g_1005f530, g_1005f52c);
        return 0;
    }
    else
    {
        return (unsigned int)sub_10002c6e(a0, a1, a2, a3);
    }
}
```

## dlgProc_Hotkeys `0x10007360`

Named — see [doc 10](../../10-*.md). _1704 bytes. calls CreateWindowExA, SendDlgItemMessageA, SendMessageA; refs ");
        sub_1000307e(a0, 1003, ", ");
        sub_1000307e(a0, 1048, ", ");
        sub_1000307e(a0, 1047, "_

```c
typedef struct WINDOWPLACEMENT {
    unsigned int length;
    enum WINDOWPLACEMENT_FLAGS flags;
    unsigned int showCmd;
    POINT ptMinPosition;
    POINT ptMaxPosition;
    RECT rcNormalPosition;
} WINDOWPLACEMENT;

typedef struct POINT {
    int x;
    int y;
} POINT;

typedef struct RECT {
    int left;
    int top;
    int right;
    int bottom;
} RECT;

extern Byte g_100429fa;
extern char g_100445f0;
extern int g_1005f520;
extern unsigned int g_1005f524;
extern unsigned int g_1005f528;
extern LPARAM g_1005f52c;
extern WPARAM g_1005f530;
extern HINSTANCE g_1005f60a;
extern unsigned int g_10072f84;
extern int g_10072fa0;
extern unsigned int g_10072fb4;
extern int g_10072fc8;
extern char g_100f94c5;
extern char g_100faa3c[4];
extern char g_100faa3d[4];
extern char g_100faa3e[4];
extern char g_1013f32b;

int sub_10007360(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v12;  // ecx
    unsigned int v13;  // ecx
    void* count;  // eax
    unsigned int idx;  // edi
    HWND v24;  // eax
    unsigned int v25;  // ebx
    int j;  // ebx
    HWND v27;  // eax
    int v28;  // ecx
    int v30;  // ecx
    unsigned int v14;  // ecx
    unsigned short v32;  // ax
    unsigned int v33;  // ebx
    unsigned int i;  // ecx
    unsigned int v16;  // ecx
    char *v17;  // esi
    char *v18;  // edi
    HWND v19;  // ebx
    unsigned int v20;  // eax
    unsigned short v21;  // ax
    int v0;  // [bp-0xa4], Other Possible Types: unsigned int
    HWND v1;  // [bp-0xa0]
    int v2;  // [bp-0x84], Other Possible Types: char
    unsigned int iter;  // [bp-0x68]
    char v4[2];  // [bp-0x64]
    char v5;  // [bp-0x60]
    char v6;  // [bp-0x5f]
    HWND v7;  // [bp-0x40], Other Possible Types: unsigned int
    void* len;  // [bp-0x3c]
    WINDOWPLACEMENT v9;  // [bp-0x38]
    unsigned int v10;  // [bp-0xc]
    int v11;  // [bp-0x8]

    if (a1 == 272)
    {
        v0 = a0;
        g_10072f84 = a0;
        SendDlgItemMessageA(a0, 1001, 241, g_100f94c5, NULL);
        SendDlgItemMessageA(a0, 1048, 241, g_1013f32b, NULL);
        sub_1000307e(a0, 1001, "This option enables or disables the functionality of the below bot hotkeys.");
        sub_1000307e(a0, 1003, "Guides you through a comprehensive wizard for creating your own hotkey.");
        sub_1000307e(a0, 1048, "Check to enable the execution of persistent hotkeys (a list of hotkeys that do not require keys to operate and run all the time).");
        sub_1000307e(a0, 1047, "Click here to edit the peristent hotkey list. One hotkey per line should be placed. 'auto' hotkeys are allowed.");
        v1 = GetDlgItem(a0, 1002);
        g_1005f528 = 0;
        v2 = (int)_INSERT(v2 CONCAT 0, 0, 28);
        *((unsigned int *)&(&v2)[4]) = 23;
        *((unsigned int *)&(&v2)[8]) = 0;
        *((unsigned int *)&(&v2)[16]) = 1;
        *((unsigned int *)&(&v2)[12]) = 96;
        *((unsigned int *)&(&v2)[20]) = 0;
        *((unsigned int *)&(&v2)[24]) = 0;
        SetScrollInfo(a0, SB_VERT, &v2, 1);
        len = CreateFontA(14, 0, 0, 0, 400, 0, 0, 0, 0xff, 0, 0, 2, 0, "MS Sans Serif");
        v11 = 24;
        GetWindowPlacement(a0, &v9);
        g_1005f520 = *((unsigned int *)((void*)&v9 + 36)) - *((unsigned int *)((void*)&v9 + 28));
        v12 = 0;
        iter = 0;
        while (true)
        {
            v13 = v12;
            if (v13 >= 96)
                break;
            v14 = v13 + 1;
            v12 = v14;
            if (!g_100faa3e[0x202 * v13])
                continue;
            iter = v14;
            v12 = v14;
        }
        iter += 1;
        iter += 12;
        if (iter > 96)
            iter = 96;
        for (i = 0; i < iter; i = v10 + 1)
        {
            v10 = i;
            v4 = &g_100faa3c[0x202 * i];
            CreateWindowExA(WS_EX_RIGHTSCROLLBAR, "BUTTON", &g_100429fa, 1342242819, 10, v11, 16, 16, a0, 4000 + v10, g_1005f60a, NULL);
            sub_1000307e(a0, v10 + 4000, "When this checkbox is unchecked, the corresponding hotkey is available for editing, but will not work. Check this checkbox to make the hotkey active.");
            v7 = CreateWindowExA(WS_EX_STATICEDGE, "EDIT", &g_100429fa, 1342242819, 30, v11, 38, 16, a0, 5000 + v10, g_1005f60a, NULL);
            sub_1000307e(a0, v10 + 5000, "Click in this field to set focus on it and press any key or mouse button to set it for this hotkey.");
            SendMessageA(v7, 48, len, NULL);
            SendMessageA(v7, 197, 0x1, NULL);
            v16 = v4[0];
            v17 = "lmouse";
            while (true)
            {
                if (v17 < &g_100445f0)
                {
                    if (v17[15] == (char)v16)
                    {
                        v18 = v17;
                        break;
                    }
                    else
                    {
                        v17 += 16;
                    }
                }
                else
                {
                    if (v16)
                    {
                        v5 = 35;
                        sub_10040940(v16, &v6);
                    }
                    else
                    {
                        v5 = 0;
                    }
                    v18 = &v5;
                    break;
                }
            }
            SendMessageA(v7, 12, NULL, v18);
            v19 = CreateWindowExA(WS_EX_STATICEDGE, "EDIT", &g_100429fa, 1342242944, 72, v11, g_1005f520 - 82, 16, a0, 6000 + v10, g_1005f60a, NULL);
            sub_1000307e(a0, v10 + 6000, "Type or paste the desired bot hotkey in here. The hotkey must follow a specific syntax. You can use the Hotkey wizard by clicking on the 'Create Hotkey' button if you are not familiar with it.");
            SendMessageA(v19, 48, len, NULL);
            SendMessageA(v19, 12, NULL, v4 + 1);
            v11 += 24;
            sub_10006c65(v10, v4[1]);
        }
        return 0;
    }
    else if (a1 == 273)
    {
        v20 = a2;
        v7 = (unsigned short)v20;
        v21 = v20 >> 16;
        if ((unsigned short)v7 == 1047)
        {
            g_10072fb4 = 1;
            sub_1001f57d(g_10072fa0, 16000, sub_100083b6);
            return 0;
        }
        if ((unsigned short)v7 == 1048)
        {
            g_1013f32b = (char)SendDlgItemMessageA(a0, 1048, 240, NULL, NULL);
            return 0;
        }
        if ((unsigned short)v7 == 1003)
        {
            sub_1001f57d(g_10072fc8, 9000, sub_1001e1d9);
            return 0;
        }
        if ((unsigned short)v7 == 1001)
        {
            g_100f94c5 = (char)SendDlgItemMessageA(a0, 1001, 240, NULL, NULL);
            return 0;
        }
        if ((unsigned short)v7 >= 5000 && (unsigned short)v7 < 5096)
        {
            if (v21 == 0x100)
            {
                sub_1002af42(v7);
                g_1005f524 = v7;
                return 0;
            }
            if (v21 != 0x200)
                return 0;
            g_1005f524 = 0;
            return 0;
        }
        if ((unsigned short)v7 >= 4000 && (unsigned short)v7 < 0x1000)
        {
            count = SendMessageA(a3, 240, NULL, NULL);
            idx = v7 - 4000;
            g_100faa3d[0x202 * idx] = *((char *)&count);
            sub_10006c65(idx, count);
            return 0;
        }
        if ((unsigned short)v7 < 6000)
            return 0;
        if ((unsigned short)v7 <= 6096)
        {
            SendMessageA(a3, 13, 0x200, &g_100faa3e[3084000 + 0x202 * v7]);
            return 0;
        }
        return 0;
    }
    else if (a1 == 5)
    {
        v0 = a3;
        g_1005f52c = a3;
        v0 = a2;
        g_1005f530 = a2;
        v24 = GetDlgItem(a0, 1002);
        v25 = _INSERT(a3, 0, (unsigned short)a3 - 3);
        g_1005f520 = (unsigned short)v25;
        MoveWindow(v24, 3, 0, g_1005f520, v25 >> 16, 0);
        for (j = 0; j < 96 && (v27 = GetDlgItem(a0, j + 6000), v27); j += 1)
        {
            v28 = (j - g_1005f528) * 24 + 42;
            if (v28 < 36 || v28 > 40000)
                v28 = -100;
            v0 = v28;
            MoveWindow(v27, 72, v28, g_1005f520 - 82, 16, 0);
            v0 = v28;
            v30 = v28;
            MoveWindow(GetDlgItem(a0, j + 5000), 30, v30, 38, 16, 0);
            MoveWindow(GetDlgItem(a0, j + 4000), 9, v30, 16, 16, 0);
        }
        InvalidateRect(a0, NULL, 1);
        return 0;
    }
    else if (a1 == 277)
    {
        v32 = (unsigned short)a2 ^ 65535;
        v33 = a2 >> 16;
        v0 = g_1005f528;
        if (v32 == 65527)
            return 0;
        if (v32 == 65534)
        {
            v33 = g_1005f528 + 1;
        }
        else if (v32 == 65535)
        {
            v33 = g_1005f528;
            if (g_1005f528)
                v33 = g_1005f528 - 1;
        }
        else if (v32 == 65532)
        {
            v33 = g_1005f528 + 4;
            if (v33 > 95)
                v33 = 95;
        }
        else if (v32 == 65533)
        {
            v33 = (g_1005f528 < 4 ? 0 : g_1005f528 - 4);
        }
        g_1005f528 = v33;
        sub_100409e0(&v2, 0, 28);
        v2 = (int)_INSERT(v2 CONCAT 0, 0, 28);
        *((unsigned int *)&(&v2)[4]) = 20;
        *((unsigned int *)&(&v2)[20]) = v33;
        *((unsigned int *)&(&v2)[24]) = v33;
        SetScrollInfo(a0, SB_VERT, &v2, 1);
        SendMessageA(a0, 5, g_1005f530, g_1005f52c);
        return 0;
    }
    else
    {
        return (unsigned int)sub_10002c6e(a0, a1, a2, a3);
    }
}
```

## `sub_10007a08` `0x10007a08`

_333 bytes. calls SendDlgItemMessageA; refs "Disconnect", "Connect"_

```c
extern char g_1005f537;
extern SOCKET g_1005f539;
extern HWND g_10072f7c;
extern int g_100fa97c;
extern int g_100fa9bc;
extern int g_100fa9fc;
extern int g_10134d61;
extern char g_1013526c;
extern unsigned int g_1013f31c;

int sub_10007a08(void)
{
    unsigned int v2;  // ebx
    unsigned int sock;  // eax
    unsigned int count;  // eax
    int v0[17];  // [bp-0x48]

    if (!g_1005f537)
    {
        if (v2)
        {
            SendDlgItemMessageA(g_10072f7c, 1004, 13, 0x40, &g_100fa97c);
            SendDlgItemMessageA(g_10072f7c, 1012, 13, 0x40, v0);
            g_1013f31c = sub_10040900(v0);
            SendDlgItemMessageA(g_10072f7c, 1006, 13, 0x40, &g_100fa9bc);
            SendDlgItemMessageA(g_10072f7c, 1003, 13, 0x40, &g_100fa9fc);
            SendDlgItemMessageA(g_10072f7c, 1009, 13, 0x20, &g_10134d61);
            sock = SendDlgItemMessageA(g_10072f7c, 1007, 12, NULL, "Disconnect");
        }
        if (g_1005f539)
        {
            shutdown(g_1005f539, SD_BOTH);
            sock = closesocket(g_1005f539);
            g_1005f539 = 0;
        }
        g_1005f537 = 1;
        g_1013526c = 1;
        return sock;
    }
    else
    {
        g_1005f537 = 0;
        if (g_1005f539)
        {
            shutdown(g_1005f539, SD_BOTH);
            closesocket(g_1005f539);
            g_1005f539 = 0;
        }
        count = SendDlgItemMessageA(g_10072f7c, 1007, 12, NULL, "Connect");
        g_1013526c = 0;
        return count;
    }
}
```

## dlgProc_HudOnScreenInfo `0x10007b55`

Named — see [doc 10](../../10-*.md). _336 bytes. refs ");
        sub_1000307e(a0, 1011, ", ");
        sub_1000307e(a0, 1014, ", ");
        sub_1000307e(a0, 1012, "_

```c
extern unsigned int g_10072fc4;

int sub_10007b55(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v0;  // [bp-0x18]

    if (a1 == 272)
    {
        v0 = a0;
        g_10072fc4 = a0;
        sub_1000307e(a0, 1005, "Enables the Player Information feature overall. It is for displaying additionnal information for each player on-screen. That information is gathered by looking at them.");
        sub_1000307e(a0, 1011, "This option will display the guild name underneath each player, if available.");
        sub_1000307e(a0, 1014, "This option will display the vocation, level, and current (1% near) and maximum health points underneath each player.");
        sub_1000307e(a0, 1012, "This option will look at each on-screen player automatically for you in order to gather information. This is done invisibly for you without showing the green look text. Otherwise, you have to look at them manually yourself.");
        sub_1000307e(a0, 1013, "This option will display an estimation of the current/max mp of every mage on screen to the best amount of information available. Every mage that you encounter will have his amount of mana assumed to be at his max mp and displayed in orange on him. Every time he receives damage on his mana shield, this amount will be reduced from the display. Every time he drinks a fluid, 200 mana will be added to his current mana.");
        sub_1000307e(a0, 1003, "Enables the On-Screen Information feature overall. It is for displaying all kinds of additionnal helpful information.");
        sub_1000307e(a0, 1010, "Displays general information such as the latency/ping to the server, average experience per hour, total damage received in the past second and the current target in the top-left corner of the screen.");
        sub_1000307e(a0, 1004, "This will add everyone that died to a 15 minutes countdown timer and list him in red in the top left corner of your screen with the time remaining for the PZ lock to wear off. Max of 10 slots. To reset these timers, press Load on the bot.");
        sub_1000307e(a0, 1002, "For every magic wall that you see spawned on the screen (or a little bit off-screen, and on different floors too), this will display a 20 seconds timer on it to inform you of how much longer the magic wall will last.");
        sub_1000307e(a0, 1006, "Everytime someone heals by more than 1%, this will spawn a light blue floating number over him to indicate the percentage that his hp has increased by. This is useful to clearly see the healing amount and frequency (is someone else healing him too?) of the spell/rune.");
        sub_1000307e(a0, 1008, "For every player or monster that is losing it's hp per second at a higher rate than 1%, this will display a red '-n%/s' text below his name to indicate the extent of the loss being dealt. This is useful for instance to see if you are able to outdamage someone's healing ability or just an useful information overall. For example, if a knight can heal for 35% of his hp in 1 second and is getting damaged by -40% per second, he will eventually run out of hp and die.");
        sub_1000307e(a0, 1009, "This option will display a green countdown to zero timer when you cast a haste spell, a purple one when you cast the invisibility spell, a blue one when you cast the mana shield spell and a yellow one when you shoot a magic wall to inform you of the time remaining of the effect duration.");
        sub_1000307e(a0, 1015, "This will display every person you exiva on the edge of the screen in the direction that the exiva provided. Keep in mind that it is only an aproximation, and if the target is close, reexivaing more often will refresh it and give a better renewed estimation. Enemies will appear in red and friends as blue. Furthermore, this will also display navigation Friends and the Enemies that they see. The codes in addition to the name are: E(exiva), S(seen by friend or yourself), A(ally connected to navigation), followed by a number stating the age of the information in seconds, and finally D(distance) followed by the number indicating the difference in squares x+y to you.");
        sub_1000307e(a0, 1016, "Will display all 'auto' binds that are currently active in the top center of your screen along with the key that activates them. Useful if you need to be fully aware of what the bot is doing for you exactly.");
        return 0;
    }
    else if (a1 == 273)
    {
        return 0;
    }
    else if (a1 == 16)
    {
        ShowWindow(a0, SW_HIDE);
        return 0;
    }
    else
    {
        return (unsigned int)sub_10002c6e(a0, a1, a2, a3);
    }
}
```

## dlgProc_AutoAimCombo `0x10007ca5`

Named — see [doc 10](../../10-*.md). _543 bytes. calls SendDlgItemMessageA; refs "No Action", "Attack", "Follow"_

```c
extern LPARAM g_10043544;
extern LPARAM g_100435c8;
extern HWND g_10072fbc;

int sub_10007ca5(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    int i;  // ebx
    LPARAM *j;  // ebx
    int k;  // ebx
    unsigned int v0;  // [bp-0x38]
    int v1[8];  // [bp-0x34]
    int v2[4];  // [bp-0x14]

    if (a1 == 272)
    {
        v0 = a0;
        g_10072fbc = a0;
        SendDlgItemMessageA(a0, 1012, 385, NULL, "No Action");
        SendDlgItemMessageA(a0, 1012, 385, 0x1, "Attack");
        SendDlgItemMessageA(a0, 1012, 385, 0x2, "Follow");
        for (i = 200; i <= 2000; i += 100)
        {
            sub_10040940(i, v1);
            lstrcat(v1, " ms");
            SendDlgItemMessageA(a0, 1042, 385, 0xffffffff, v1);
        }
        for (j = &g_10043544; j < &g_100435c8; j += 1)
        {
            SendDlgItemMessageA(a0, 1006, 385, 0xffffffff, *(j));
        }
        for (k = 1; k < 11; k += 1)
        {
            sub_10040940(k, v2);
            SendDlgItemMessageA(a0, 1031, 385, 0xffffffff, v2);
        }
        sub_1000307e(g_10072fbc, 1011, "When selecting targets, this instructs the targeting system to target the friend for healing or enemy for attacking with the least amount of health *percentage* first.");
        sub_1000307e(g_10072fbc, 1003, "When selecting targets, this instructs the targeting system to target the enemy with the lowest amount of current hp. Often this will be a mage, a low level paladin or knight, or someone being hit down.In terms of priorities, if the other targeting options such as 'Prioritize mage with least mp' is enabled, it will have priority over this option if it finds a mage to target.");
        sub_1000307e(g_10072fbc, 1010, "Automatically triggers attacks with specified combo leader(s). Even if you chose to leave this off, you can still combo manually at your command by using the 'autoaim' bind. This will then issue a more voluntary attack on the current leader's target. For safety, anyone using elfbot won't react if an SD shot by a leader is on someone that is in the friend or subfriend lists.");
        sub_1000307e(g_10072fbc, 1002, "This option works together with the mana amounts approximation. Every instance of enemy selection will prioritize targetting on the mage that has the least amount of current mp. Binds making use of this are for example 'sd enemy' or 'autoaim'.");
        sub_1000307e(g_10072fbc, 1007, "This option will make the bot ignore enemies standing in PZs and rather choose ones that are outside. This prevents the bot from becoming stuck on trying to kill a target it can't hit and doing nothing. Most of the known Depots/Boats/Temples are flagged as protections zones.");
        sub_1000307e(g_10072fbc, 1008, "Whenever targeting enemies or friends, the bot will attempt to predict the trajectory that the projectile will take and determine if obstacles will obstruct the shot. If so, the bot will skip to the next enemy/friend and you won't be stuck trying to target someone you can't hit.");
        sub_1000307e(g_10072fbc, 1009, "This option instructs the bot to use the newer inventory actions that work even with closed backpacks. If not checked, instead each backpack is scanned manually. Turning this off is useful for using items from containers on the ground.");
        sub_1000307e(g_10072fbc, 1001, "This will show a white selection box in real-time around the best enemy which the command 'autoaim' is going to target.");
        sub_1000307e(g_10072fbc, 1015, "Name of the leader(s) to synchronize attacks with. The combo triggers only when the leader shoots a SD rune. It is possible to insert multiple leaders in this field, separated by commas. For example: 'Bubble1, Another Leader2, PlayerName23' (without the single quotes) will trigger a combo reaction whenever either of those shoot a SD rune. There is also some additional logic associated to this to smoothen the process by eliminating some nuisances this may cause (i.e. infinite chain reactions).");
        sub_1000307e(g_10072fbc, 1012, "Determines the type of action to be taken by the 'autoaim' hotkey and for comboing. Several choices are available, and even in combinations of two. To change the current setting, use your arrow up and down keys. Other combo strategies can be used through the use of binds.");
        sub_1000307e(g_10072fbc, 1004, "If this option is selected, the subenemy/enemy/ autoaim target selection system will ignore players that are skulled and combo fire will not trigger on skulled players either. It will still be possible to sd such players manually though by using 'sd target' for example.");
        return 0;
    }
    else if (a1 == 273)
    {
        return 0;
    }
    else if (a1 == 16)
    {
        ShowWindow(a0, SW_HIDE);
        return 0;
    }
    else
    {
        return (unsigned int)sub_10002c6e(a0, a1, a2, a3);
    }
}
```

## dlgProc_GraphicsTweaks `0x10007ec4`

Named — see [doc 10](../../10-*.md). _363 bytes. calls SendDlgItemMessageA, WritePrivateProfileStringA; refs ");
        sub_1000307e(a0, 1006, ", ");
        sub_1000307e(a0, 1002, ", ");
        sub_1000307e(a0, 1003, "_

```c
extern int g_10042f83;
extern char g_1004476a;
extern unsigned int g_10072f88;
extern char g_100ee8bb;

int sub_10007ec4(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v0;  // [bp-0x878]
    int v1;  // [bp-0x874], Other Possible Types: unsigned short
    int v2;  // [bp-0x870]
    int v3;  // [bp-0x86c]
    int v4;  // [bp-0x868]
    int v5;  // [bp-0x864]
    Byte v6[1080];  // [bp-0x43c]

    if (a1 == 272)
    {
        v0 = a0;
        g_10072f88 = a0;
        sub_1000307e(a0, 1004, "This feature is useful to enjoy increased framerates, specially on slower systems, or simply to reduce CPU use. What it does is reduce the refresh rate of the game GUI to 10fps and focuses ressources to redraw the game world more often instead. It is possible to even double in overall fps this way. This feature will also disable graphics when the client is minimised to reduce CPU usage to 0, which makes it possible to have multiple clients running at the same time without lagging your computer or to be able to perform other tasks with Tibia running in the background.");
        sub_1000307e(a0, 1006, "This allows you to reuse the same object multiple times with losing the crosshair icon. The object must not change place after being used in the inventory.");
        sub_1000307e(a0, 1002, "This option will hide the GUI interface of the client and stretch the world-view to the entire client window. The Tibia client also gains top-most status and does not disappear under other windows and can be resised further down than usual. The side effect of these is that the mouse must be disabled because the location of mouse coordinates don't correspond anymore. GUI windows such as channel list don't appear either and it is necessary to turn world view off to exit the client. This feature is however still useful to watch cams, multiple clients or a small view of your friend or yourself on different levels while you are playing. The framerate of a world-view only client gets capped to 20 if it is not the window currently having focus.");
        sub_1000307e(a0, 1003, "This allows you to see player names off-screen and through floors to have a better idea of their positioning.");
        if (!g_1004476a)
            return 0;
        SendDlgItemMessageA(a0, 1013, 241, 0x1, NULL);
        return 0;
    }
    else if (a1 == 273)
    {
        if (a2 == 1002)
        {
            g_100ee8bb = (char)SendDlgItemMessageA(a0, 1002, 240, NULL, NULL);
            sub_10039c81(v1, v2, v3, v4, v5);
            return 0;
        }
        else if (a2 == 1013)
        {
            v1 = 48;
            if (SendDlgItemMessageA(a0, 1013, 240, NULL, NULL))
                v1 = 49;
            lstrcpy(v6, &g_10042f83);
            lstrcat(v6, "elfbot.ini");
            WritePrivateProfileStringA("GlobalSettings", "LoadLastSkin", &v1, v6);
            return 0;
        }
        else
        {
            return 0;
        }
    }
    else
    {
        if (a1 == 16)
        {
            ShowWindow(a0, SW_HIDE);
            return 0;
        }
        return (unsigned int)sub_10002c6e(a0, a1, a2, a3);
    }
}
```

## dlgProc_TargetingEditor `0x1000802f`

Named — see [doc 10](../../10-*.md). _291 bytes. calls SendDlgItemMessageA_

```c
extern HWND g_10072f94;
extern unsigned int g_10072f98;
extern char g_100f0e44;
extern char g_101e6eb4;

int sub_1000802f(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    LRESULT count;  // eax
    unsigned int count1;  // eax
    unsigned int count2;  // eax
    unsigned int v0;  // [bp-0x1c]
    int v1;  // [bp-0x10]
    int v2;  // [bp-0xc]
    int v3;  // [bp-0x8]

    if (a1 == 272)
    {
        v0 = a0;
        g_10072f98 = a0;
        return 0;
    }
    else if (a1 == 273)
    {
        if (a2 == 1003)
        {
            count = SendDlgItemMessageA(g_10072f94, 0x404, 392, NULL, NULL);
            if (count != 0xffffffff)
            {
                SendDlgItemMessageA(a0, 1002, 13, 0x20, 0x30 * count + &g_101e6eb4);
                if (g_100f0e44)
                {
                    count1 = SendDlgItemMessageA(g_10072f94, 0x404, 398, NULL, NULL);
                    count2 = SendDlgItemMessageA(g_10072f94, 0x404, 392, NULL, NULL);
                    sub_100160d6(count1, count2, v1, v2, v3);
                    SendDlgItemMessageA(g_10072f94, 0x404, 407, count1, NULL);
                    SendDlgItemMessageA(g_10072f94, 0x404, 390, count2, NULL);
                }
            }
            DestroyWindow(a0);
            return 0;
        }
        else
        {
            return 0;
        }
    }
    else
    {
        if (a1 == 16)
        {
            DestroyWindow(a0);
            return 0;
        }
        return (unsigned int)sub_10002c6e(a0, a1, a2, a3);
    }
}
```

## `sub_10008152` `0x10008152`

_306 bytes. (leaf/helper — see body)_

```c
extern int g_10084f8b;
extern int g_1008720b;
extern int g_10087d8b;
extern int g_1008890b;
extern unsigned int g_1008910b;
extern int g_1009a536;
extern unsigned int g_100f49d5;
extern unsigned int g_101f2ea8;

void sub_10008152(void)
{
    unsigned int v10;  // esi
    char *iter;  // edi
    unsigned int i;  // ecx
    unsigned int v13;  // edx
    int v14;  // edi
    int idx;  // edi
    int v0;  // [bp-0x1054], Other Possible Types: unsigned int
    unsigned int v1;  // [bp-0x1050]
    unsigned int v2;  // [bp-0x104c]
    unsigned int v3;  // [bp-0x1048]
    int index;  // [bp-0x1010]
    int v5;  // [bp-0x100c]
    char v6;  // [bp-0x1004], Other Possible Types: unsigned int
    char v7;  // [bp-0x1000]
    char v8;  // [bp-0xe05]

    sub_1002ae81(&g_10084f8b, 0x200);
    sub_1002ae81(&g_1008720b, 0x200);
    sub_1002ae81(&g_10087d8b, 0x200);
    sub_1002ae81(&g_1008890b, 0x200);
    sub_1002ae81(&g_1009a536, 0x10100);
    v10 = &g_101f2ea8;
    iter = &v6;
    v5 = &g_1009a536;
    index = 224;
    i = 0;
    while (i < 0x10000)
    {
        v13 = _INSERT(0, 0, *((char *)(i + v10)));
        if (!*((char *)(i + v10)) || (char)v1 == 13)
        {
            *(iter) = 0;
            v8 = 0;
            v3 = v10;
            v2 = i;
            v1 = v13;
            v14 = v5;
            *((char *)v14) = 1;
            v0 = g_100f49d5;
            (&g_1008910b)[index] = g_100f49d5;
            v0 = v14;
            lstrcpy(v0 + 2, &v6);
            idx = v0;
            if ((v6 | 0x20202020) == 1869903201 && v7 == 32)
            {
                *((char *)(idx + 1)) = 1;
                sub_10030442(&v6, index, 0);
            }
            else
            {
                *((char *)(idx + 1)) = 255;
            }
            v10 = v3;
            if (!(char)v1)
                return;
            v5 += 0x202;
            index += 1;
            iter = &v6;
            i = v2 + 2;
        }
        else
        {
            *(iter) = v1;
            iter += 1;
            i += 1;
        }
    }
    return;
}
```

## `sub_10008284` `0x10008284`

_306 bytes. (leaf/helper — see body)_

```c
extern int g_1008518b;
extern int g_1008740b;
extern int g_10087f8b;
extern int g_10088b0b;
extern unsigned int g_1008910b;
extern int g_100aa636;
extern unsigned int g_100f49d5;
extern unsigned int g_1013f32c;

void sub_10008284(void)
{
    unsigned int v10;  // esi
    char *iter;  // edi
    unsigned int i;  // ecx
    unsigned int v13;  // edx
    int v14;  // edi
    int idx;  // edi
    int v0;  // [bp-0x1054], Other Possible Types: unsigned int
    unsigned int v1;  // [bp-0x1050]
    unsigned int v2;  // [bp-0x104c]
    unsigned int v3;  // [bp-0x1048]
    int index;  // [bp-0x1010]
    int v5;  // [bp-0x100c]
    char v6;  // [bp-0x1004], Other Possible Types: unsigned int
    char v7;  // [bp-0x1000]
    char v8;  // [bp-0xe05]

    sub_1002ae81(&g_1008518b, 0x200);
    sub_1002ae81(&g_1008740b, 0x200);
    sub_1002ae81(&g_10087f8b, 0x200);
    sub_1002ae81(&g_10088b0b, 0x200);
    sub_1002ae81(&g_100aa636, 0x10100);
    v10 = &g_1013f32c;
    iter = &v6;
    v5 = &g_100aa636;
    index = 352;
    i = 0;
    while (i < 0x10000)
    {
        v13 = _INSERT(0, 0, *((char *)(i + v10)));
        if (!*((char *)(i + v10)) || (char)v1 == 13)
        {
            *(iter) = 0;
            v8 = 0;
            v3 = v10;
            v2 = i;
            v1 = v13;
            v14 = v5;
            *((char *)v14) = 1;
            v0 = v14;
            lstrcpy(v0 + 2, &v6);
            idx = v0;
            v0 = g_100f49d5;
            (&g_1008910b)[index] = g_100f49d5;
            if ((v6 | 0x20202020) == 1869903201 && v7 == 32)
            {
                *((char *)(idx + 1)) = 1;
                sub_10030442(&v6, index, 0);
            }
            else
            {
                *((char *)(idx + 1)) = 255;
            }
            v10 = v3;
            if (!(char)v1)
                return;
            v5 += 0x202;
            index += 1;
            iter = &v6;
            i = v2 + 2;
        }
        else
        {
            *(iter) = v1;
            iter += 1;
            i += 1;
        }
    }
    return;
}
```

## dlgProc_ScriptEditor `0x100083b6`

Named — see [doc 10](../../10-*.md). _765 bytes. refs " Persistent commands list", " Edit Cavebot Script", "Load Script"_

```c
extern unsigned int g_10072f9c;
extern unsigned int g_10072fa0;
extern unsigned int g_10072fa4;
extern unsigned int g_10072fa8;
extern unsigned int g_10072fac;
extern unsigned int g_10072fb0;
extern unsigned int g_10072fb4;
extern void* g_100f0d2c;
extern int g_1013f32c;
extern int g_101f2ea8;

int sub_100083b6(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v5;  // ebx
    unsigned int v0;  // [bp-0x14]
    unsigned int v1;  // [bp-0x10]
    int v2;  // [bp-0xc]
    unsigned int v3;  // [bp-0x8]
    char v4;  // [bp+0x0]

    if (a1 == 272)
    {
        v1 = a0;
        v0 = g_10072fb4;
        if (!g_10072fb4)
        {
            g_10072f9c = a0;
            SendDlgItemMessageA(a0, 1002, 12, NULL, &g_101f2ea8);
        }
        else
        {
            if (g_10072fb4 == 1)
            {
                g_10072fa0 = a0;
                SendDlgItemMessageA(a0, 1002, 12, NULL, &g_1013f32c);
                SetWindowTextA(a0, " Persistent commands list");
            }
            else
            {
                if (g_10072fb4 == 2)
                {
                    g_10072fa4 = a0;
                    SetWindowTextA(a0, " Edit Cavebot Script");
                    SendDlgItemMessageA(a0, 1003, 12, NULL, "Load Script");
                    sub_100188f9(v2, g_10072fb4, &v4, v4, a0);
                }
                else
                {
                    if (g_10072fb4 == 3)
                    {
                        g_10072fa8 = a0;
                        SetWindowTextA(a0, " Edit Targeting Script");
                        SendDlgItemMessageA(a0, 1003, 12, NULL, "Load Script");
                        sub_10018d8a(v2, g_10072fb4, &v4, v4, a0);
                    }
                    else
                    {
                        if (g_10072fb4 == 4)
                        {
                            g_10072fac = a0;
                            SetWindowTextA(a0, " Edit Icons Script");
                            SendDlgItemMessageA(a0, 1003, 12, NULL, "Load Icons");
                            sub_100193a1(v2, g_10072fb4, &v4, v4, a0);
                        }
                    }
                }
            }
        }
        sub_10040940(g_10072fb4, &v2);
        SendDlgItemMessageA(a0, 1001, 12, NULL, &v2);
        return 0;
    }
    else if (a1 == 273)
    {
        if (a2 == 1003)
        {
            SendDlgItemMessageA(a0, 1001, 13, 0x20, &v2);
            v3 = sub_10040900(&v2);
            if (!sub_10040900(&v2))
            {
                SendDlgItemMessageA(a0, 1002, 13, 0x1005e, &g_101f2ea8);
                sub_10008152();
                return 0;
            }
            if (sub_10040900(&v2) == 1)
            {
                SendDlgItemMessageA(a0, 1002, 13, 0x1005e, &g_1013f32c);
                sub_10008284();
                return 0;
            }
            if (sub_10040900(&v2) != 2 && sub_10040900(&v2) != 3 && sub_10040900(&v2) != 4)
                return 0;
            v5 = HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, 0x200000);
            SendDlgItemMessageA(a0, 1002, 13, 0x200000, v5);
            v0 = a0;
            g_10072fb0 = a0;
            sub_1001686c(v5);
            HeapFree(GetProcessHeap(), HEAP_NONE, v5);
            return 0;
        }
        else if (a2 == 1004)
        {
            g_100f0d2c = GlobalAlloc(8194, 0x200000);
            SendDlgItemMessageA(a0, 1002, 13, 0x200000, GlobalLock(g_100f0d2c));
            OpenClipboard(NULL);
            EmptyClipboard();
            GlobalUnlock(g_100f0d2c);
            SetClipboardData(1, g_100f0d2c);
            CloseClipboard();
            GlobalFree(g_100f0d2c);
            return 0;
        }
        else if (a2 == 1005)
        {
            OpenClipboard(NULL);
            SendDlgItemMessageA(a0, 1002, 12, NULL, GetClipboardData(1));
            CloseClipboard();
            return 0;
        }
        else
        {
            return 0;
        }
    }
    else
    {
        if (a1 == 16)
        {
            DestroyWindow(a0);
            return 0;
        }
        return (unsigned int)sub_10002c6e(a0, a1, a2, a3);
    }
}
```

## dlgProc_Skin `0x100086b3`

Named — see [doc 10](../../10-*.md). _823 bytes. calls GetPrivateProfileStringA, SendDlgItemMessageA, SendMessageA, WritePrivateProfileStringA; refs "elfbot.ini", "GlobalSettings", "LoadLastSkin"_

```c
extern Byte g_100429fa;
extern char g_10042d7b;
extern char g_1004476a;
extern char g_1005f609;
extern unsigned int g_1005f60a;
extern HWND g_1005f61a;
extern char g_100f9368;

int sub_100086b3(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    void* i;  // ecx
    void* v7;  // ecx
    void* count1;  // eax
    char *node;  // esi
    void* iter;  // edi
    char v11;  // 4101
    void* v0;  // [bp-0x238], Other Possible Types: unsigned int
    Byte v1[300];  // [bp-0x234]
    Byte v2[128];  // [bp-0x108]
    char v3;  // [bp-0x88]
    char v4;  // [bp-0x8]

    if (a1 == 272)
    {
        lstrcpy(v1, &g_10042d7b);
        lstrcat(v1, "elfbot.ini");
        GetPrivateProfileStringA("GlobalSettings", "LoadLastSkin", &g_100429fa, &v3, &v4, v1);
        if (*((short *)&v3) == 49)
        {
            g_1004476a = 1;
            GetPrivateProfileStringA("GlobalSettings", "LastSkin", &g_100429fa, &v3, &v4, v1);
            goto LABEL_100088e0;
        }
        else
        {
            GetPrivateProfileStringA("GlobalSettings", "LastSkin", &g_100429fa, v2, &v4, v1);
            lstrcpy(v1, &g_10042d7b);
            lstrcat(v1, "Skins\\*.msstyles");
            DlgDirListA(a0, v1, 1001, 0, DDL_READONLY);
            SendDlgItemMessageA(a0, 1001, 385, NULL, "<No Skin>");
            SendDlgItemMessageA(a0, 1001, 390, NULL, NULL);
            for (i = NULL; i < SendDlgItemMessageA(a0, 1001, 395, NULL, NULL); i = v7 + 1)
            {
                v0 = i;
                SendDlgItemMessageA(a0, 1001, 393, i, &v3);
                v7 = i;
                if (!lstrcmpi(&v3, v2))
                {
                    SendDlgItemMessageA(a0, 1001, 390, v7, NULL);
                    return 0;
                }
            }
            return 0;
        }
    }
    else
    {
        if (a1 == 273)
        {
            if (a2 == 1002)
            {
                count1 = SendDlgItemMessageA(a0, 1001, 392, NULL, NULL);
                if (count1 == 0xffffffff)
                    goto LABEL_10008973;
                SendDlgItemMessageA(a0, 1001, 393, count1, &v3);
                lstrcpy(v1, &g_10042d7b);
                lstrcat(v1, "elfbot.ini");
                WritePrivateProfileStringA("GlobalSettings", "LastSkin", &v3, v1);
LABEL_100088e0:
                DestroyWindow(a0);
                if (lstrcmp(&v3, "<No Skin>"))
                {
                    node = &g_10042d7b;
                    for (iter = v1; *(node); iter += 1)
                    {
                        v11 = *(node);
                        *((char *)iter) = *(node);
                        if (v11 == 92)
                        {
                            *((unsigned short *)iter) = 0x5c5c;
                            iter += 1;
                        }
                        node += 1;
                    }
                    *((char *)iter) = 0;
                    lstrcat(v1, "Skins\\\\");
                    lstrcat(v1, &v3);
                    lstrcpy(&g_100f9368, v1);
                    SendMessageA(g_1005f61a, 273, 0x53b, &g_100f9368);
                }
LABEL_10008973:
            }
            else if (a2 == 1003)
            {
                DestroyWindow(a0);
            }
            else
            {
                return 0;
            }
        }
        else
        {
            if (a1 == 16)
            {
                DestroyWindow(a0);
            }
            else if (a1 != 2)
            {
                return (unsigned int)sub_10002c6e(a0, a1, a2, a3);
            }
            else
            {
                return 0;
            }
        }
        g_1005f609 = 1;
        SetFocus(sub_10039b62(v1));
        v0 = 0;
        SetFocus(sub_10002c87(g_1005f60a, 0x3fc, 0, sub_10003146));
        return 0;
    }
}
```

## `sub_10008975` `0x10008975`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10008975(void)
{
}
```

## `sub_100089ca` `0x100089ca`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100089ca(void)
{
}
```

## `sub_10008a1d` `0x10008a1d`

_78 bytes. (leaf/helper — see body)_

```c
extern char g_1800000c;

int sub_10008a1d(void)
{
    void* v2;  // eax
    unsigned int v3;  // ecx
    char *v12;  // eax
    unsigned int *v13;  // eax
    char *v14;  // ecx
    char v15;  // al
    unsigned int *v16;  // eax
    char v17;  // al
    char *v18;  // eax
    char v4;  // dl
    unsigned int *v5;  // eax
    char *v6;  // edx
    char v7;  // al
    char *v8;  // edi
    char *v9;  // ebx
    char *v10;  // esi
    unsigned int *v11;  // eax
    char v0;  // [bp+0x0]
    unsigned int v1;  // [bp+0x4]

    *((unsigned int *)v2) = *((int *)v2) + 1;
    *((char *)v2) = *((char *)v2) + *((char *)&v2);
    *((char *)v2) = *((char *)v2) + *((char *)&v2);
    *((char *)v2) = *((char *)v2) + *((char *)&v2);
    (&v0)[v3] = (&v0)[v3] + v4;
    *((char *)v2) = *((char *)v2) + *((char *)&v2);
    g_1800000c = g_1800000c + v4;
    v5 = _INSERT(v2, 0, *((char *)&v2));
    v6 = _INSERT(v4 CONCAT 0, 0, v4 + *((char *)((void*)&v3 + 1)));
    v7 = (char)v5 | (char)*(v5);
    *(v8) = *(v8) + (char)v3;
    *(v9) = *(v9) + v4 + *((char *)((void*)&v3 + 1));
    *(v10) = *(v10) + v4 + *((char *)((void*)&v3 + 1));
    v11 = _INSERT(v7, 0, v7);
    v12 = v11 | *(v11);
    *(v12) = *(v12) + v4 + *((char *)((void*)&v3 + 1));
    v13 = _INSERT(v12, 0, *((char *)&v12));
    v14 = _INSERT(v3, 1, *((char *)((void*)&v3 + 1)) * 2);
    v15 = (char)v13 | (char)*(v13);
    *(v6) = *(v6) + v4 + *((char *)((void*)&v3 + 1));
    v16 = _INSERT(v15, 1, v15 + *((char *)((void*)&v3 + 1)) * 2);
    v17 = (char)v16 | (char)*(v16);
    *(v14) = *(v14) + v4 + *((char *)((void*)&v3 + 1));
    *(v6) = *(v6) + *((char *)&v9) + *((char *)((void*)&v3 + 1));
    v18 = _INSERT(v17, 0, v17);
    *((char *)(&v1 + v14)) = *((char *)(&v1 + v14)) + *((char *)&v9) + *((char *)((void*)&v3 + 1));
    *(v18) = *(v18) + v17;
}
```

## `sub_10008a6b` `0x10008a6b`

_982 bytes. calls SendDlgItemMessageA; refs " ms", "Don't", " sq"_

```c
extern char g_100424d2;
extern char g_100425a1;
extern char g_1004263d;
extern char g_1004350a;
extern char g_10043538;
extern LPARAM g_10043544;
extern LPARAM g_100435c8;
extern HWND g_10072f8c;
extern unsigned int g_101dfe94;

int sub_10008a6b(void)
{
    char *v2;  // ecx
    char *v3;  // ebx
    LPARAM *i1;  // ebx
    unsigned int i2;  // ebx
    unsigned int i3;  // ebx
    unsigned int i4;  // ebx
    unsigned int i5;  // ebx
    char v4;  // dl
    int i;  // ebx
    int j;  // ebx
    int k;  // ebx
    int l;  // ebx
    int m;  // ebx
    unsigned int n;  // ebx
    unsigned int i0;  // ebx
    char v1;  // [bp+0xfff8f]

    *(v2) = *(v2) + *((char *)&v3);
    *(v3) = *(v3) + *((char *)&v3);
    v1 += v4;
    g_101dfe94 = 19;
    SendDlgItemMessageA(g_10072f8c, 1001, 1030, NULL, 0x640000);
    SendDlgItemMessageA(g_10072f8c, 1001, 1045, NULL, 0x4);
    SendDlgItemMessageA(g_10072f8c, 1002, 1030, NULL, 0x640000);
    SendDlgItemMessageA(g_10072f8c, 1002, 1045, NULL, 0x4);
    SendDlgItemMessageA(g_10072f8c, 1003, 1030, NULL, 0x640000);
    SendDlgItemMessageA(g_10072f8c, 1003, 1045, NULL, 0x4);
    SendDlgItemMessageA(g_10072f8c, 1004, 1030, NULL, 0x640000);
    SendDlgItemMessageA(g_10072f8c, 1004, 1045, NULL, 0x4);
    SendDlgItemMessageA(g_10072f8c, 1039, 1030, NULL, 0x640000);
    SendDlgItemMessageA(g_10072f8c, 1039, 1045, NULL, 0x4);
    SendDlgItemMessageA(g_10072f8c, 1044, 1030, NULL, 0x640000);
    SendDlgItemMessageA(g_10072f8c, 1044, 1045, NULL, 0x4);
    for (i = 0; i < 11; i += 1)
    {
        sub_10040940(i, /* unsupported instruction */ - 32);
        SendDlgItemMessageA(g_10072f8c, 1017, 385, 0xffffffff, /* unsupported instruction */ - 32);
    }
    for (j = 2; j < 10; j += 1)
    {
        sub_10040940(j, /* unsupported instruction */ - 32);
        SendDlgItemMessageA(g_10072f8c, 1013, 385, 0xffffffff, /* unsupported instruction */ - 32);
        SendDlgItemMessageA(g_10072f8c, 1052, 385, 0xffffffff, /* unsupported instruction */ - 32);
    }
    for (k = 1; k < 5; k += 1)
    {
        sub_10040940(k, /* unsupported instruction */ - 32);
        SendDlgItemMessageA(g_10072f8c, 1040, 385, 0xffffffff, /* unsupported instruction */ - 32);
    }
    for (l = 100; l <= 30000; l += 100)
    {
        sub_10040940(l, /* unsupported instruction */ - 32);
        lstrcat(/* unsupported instruction */ - 32, " ms");
        SendDlgItemMessageA(g_10072f8c, 1047, 385, 0xffffffff, /* unsupported instruction */ - 32);
    }
    SendDlgItemMessageA(g_10072f8c, 1069, 385, 0xffffffff, "Don't");
    for (m = 1; m <= 8; m += 1)
    {
        sub_10040940(m, /* unsupported instruction */ - 32);
        lstrcat(/* unsupported instruction */ - 32, " sq");
        SendDlgItemMessageA(g_10072f8c, 1069, 385, 0xffffffff, /* unsupported instruction */ - 32);
    }
    for (n = 0; n < 12; n += 4)
    {
        SendDlgItemMessageA(g_10072f8c, 1042, 385, 0xffffffff, *((int *)&(&g_10043538)[n]));
    }
    for (i0 = 0; i0 < 12; i0 += 4)
    {
        SendDlgItemMessageA(g_10072f8c, 1041, 385, 0xffffffff, *((int *)&(&g_1004350a)[i0]));
    }
    for (i1 = &g_10043544; i1 < &g_100435c8; i1 += 1)
    {
        SendDlgItemMessageA(g_10072f8c, 1054, 385, 0xffffffff, *(i1));
    }
    for (i2 = 0; i2 < 0x44; i2 += 4)
    {
        SendDlgItemMessageA(g_10072f8c, 1025, 385, 0xffffffff, *((int *)&(&g_100424d2)[i2]));
    }
    for (i3 = 0; i3 < 10; i3 += 1)
    {
        SendDlgItemMessageA(g_10072f8c, 1057, 385, 0xffffffff, 268470766 + 4 * i3);
    }
    for (i4 = 0; i4 < 52; i4 += 4)
    {
        SendDlgItemMessageA(g_10072f8c, 1058, 385, 0xffffffff, *((int *)&(&g_100425a1)[i4]));
    }
    for (i5 = 0; i5 < 28; i5 += 4)
    {
        SendDlgItemMessageA(g_10072f8c, 1070, 385, 0xffffffff, *((int *)&(&g_1004263d)[i5]));
    }
    return;
}
```

## `sub_10008e41` `0x10008e41`

_523 bytes. refs "WAVE", "fmt ", "data"_

```c
typedef struct struct_5 {
    struct struct_0 *field_0;
} struct_5;

typedef struct struct_0 {
    char padding_0[8];
    struct struct_1 *field_8;
    char padding_c[32];
    struct struct_1 *field_2c;
    char padding_30[4];
    struct struct_1 *field_34;
    char padding_38[20];
    struct struct_1 *field_4c;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern int g_10042f83;
extern struct_5 *g_10052658;
extern unsigned int g_10052680;
extern char g_10052684;
extern unsigned int g_10052688;
extern char g_1005268c;
extern unsigned int g_10052690;
extern unsigned int g_10052698;

unsigned int sub_10008e41(int a0, struct_5 **a1)
{
    HMMIO v12;  // eax
    Byte v0[4];  // [bp-0x78]
    char v1;  // [bp-0x74], Other Possible Types: unsigned int
    SByte *v2;  // [bp-0x70], Other Possible Types: char
    SByte v3[18];  // [bp-0x6a]
    int v4;  // [bp-0x58], Other Possible Types: unsigned int (32 bits)[5]
    unsigned int v5[5];  // [bp-0x44]
    HMMIO v6;  // [bp-0x30]
    char v7;  // [bp-0x2c], Other Possible Types: unsigned int
    unsigned int v8;  // [bp-0x28]
    unsigned int v9;  // [bp-0x24]
    char *v10;  // [bp-0x1c]
    struct_0 **v11;  // [bp-0x8], Other Possible Types: unsigned int

    lstrcpy(v0, &g_10042f83);
    lstrcat(v0, a0);
    v11 = *(a1);
    if (v11)
    {
        *(v11)->field_8(v11);
        v11 = NULL;
    }
    v12 = mmioOpenA(v0, NULL, 0x10000);
    if (v12)
    {
        v6 = v12;
        strncpy(&v5[2], "WAVE", 4);
        if (!mmioDescend(v6, v5, NULL, 32))
        {
            strncpy(v4, "fmt ", 4);
            if (!mmioDescend(v6, v4, v5, 16) && mmioRead(v6, v3, *((unsigned int *)(&v4 + 4))) == *(&v4[1]))
            {
                mmioAscend(v6, v4, 0);
                strncpy(v4, "data", 4);
                if (!mmioDescend(v6, v4, v5, 16))
                {
                    RtlZeroMemory(&v7, 36);
                    v7 = 36;
                    v8 = 0x8000;
                    v9 = *(&v4[1]);
                    v10 = &v3[0];
                    g_10052680 = &g_10052680;
                    g_10052688 = &g_10052684;
                    g_10052690 = &g_10052688;
                    g_10052698 = &g_1005268c;
                    if (!(*((int *)&g_10052658->field_0->padding_c[0]))(g_10052658, &v7, &v11, 0) && !*(v11)->field_2c(v11, 0, *((unsigned int *)(&v4 + 4)), &v2, &v1, 0, 0, 0))
                    {
                        mmioRead(v6, v2, *((unsigned int *)(&v4 + 4)));
                        if (!*(v11)->field_4c(v11, v2, v1, 0, 0))
                        {
                            *(v11)->field_34(v11, 0);
                            mmioClose(v6, 0);
                            *(a1) = v11;
                            return 0;
                        }
                    }
                }
            }
        }
        mmioClose(v6, 0);
        if (v11)
        {
            *(v11)->field_8(v11);
            v11 = 0;
        }
    }
    *(a1) = NULL;
    return 2147500037;
}
```

## `sub_1000904c` `0x1000904c`

_246 bytes. calls DirectSoundCreate_

```c
typedef struct struct_4 {
    char padding_0[8];
    struct struct_1 *field_8;
    char padding_c[44];
    struct struct_1 *field_38;
} struct_4;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[12];
    struct struct_1 *field_c;
    char padding_10[8];
    struct struct_1 *field_18;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

extern struct_3 *g_10052658;

unsigned int sub_1000904c(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3)
{
    unsigned int v9;  // eax
    struct_4 **v0;  // [bp-0x40], Other Possible Types: char, unsigned int
    char v1;  // [bp-0x3a], Other Possible Types: unsigned short
    unsigned short v2;  // [bp-0x38]
    unsigned int v3;  // [bp-0x36]
    unsigned int v4;  // [bp-0x32]
    unsigned short v5;  // [bp-0x2e]
    unsigned short v6;  // [bp-0x2c]
    char v7;  // [bp-0x28], Other Possible Types: unsigned int
    unsigned int v8;  // [bp-0x24]

    if (DirectSoundCreate(NULL, &g_10052658, 0))
    {
        return 2147500037;
    }
    else if (g_10052658->field_0->field_18(g_10052658, a0, 2))
    {
        return 2147500037;
    }
    else
    {
        RtlZeroMemory(&v7, 36);
        v7 = 36;
        v8 = 1;
        if (g_10052658->field_0->field_c(g_10052658, &v7, &v0, 0))
            return 2147500037;
        RtlZeroMemory(&v1, 18);
        v1 = 1;
        v2 = a1;
        v6 = a3;
        v9 = a3 * a1 >> 3;
        v5 = v9;
        v3 = a2;
        v4 = v9 * a2;
        if (*(v0)->field_38(v0, &v1))
            return 2147500037;
        if (!v0)
            return 0;
        *(v0)->field_8(v0);
        v0 = 0;
        return 0;
    }
}
```

## `sub_10009142` `0x10009142`

_366 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[8];
    struct struct_1 *field_8;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

typedef struct struct_2 {
    struct struct_0 *field_0;
} struct_2;

extern struct_2 *g_10052658;
extern struct_2 *g_1005265c;
extern struct_2 *g_10052660;
extern struct_2 *g_10052664;
extern struct_2 *g_10052668;
extern struct_2 *g_1005266c;
extern struct_2 *g_10052670;
extern struct_2 *g_10052674;
extern struct_2 *g_10052678;
extern struct_2 *g_1005267c;

unsigned int sub_10009142(void)
{
    if (g_1005265c)
    {
        g_1005265c->field_0->field_8(g_1005265c);
        g_1005265c = 0;
    }
    if (g_10052660)
    {
        g_10052660->field_0->field_8(g_10052660);
        g_10052660 = 0;
    }
    if (g_10052670)
    {
        g_10052670->field_0->field_8(g_10052670);
        g_10052670 = 0;
    }
    if (g_10052664)
    {
        g_10052664->field_0->field_8(g_10052664);
        g_10052664 = 0;
    }
    if (g_10052668)
    {
        g_10052668->field_0->field_8(g_10052668);
        g_10052668 = 0;
    }
    if (g_1005266c)
    {
        g_1005266c->field_0->field_8(g_1005266c);
        g_1005266c = 0;
    }
    if (g_10052678)
    {
        g_10052678->field_0->field_8(g_10052678);
        g_10052678 = 0;
    }
    if (g_10052674)
    {
        g_10052674->field_0->field_8(g_10052674);
        g_10052674 = 0;
    }
    if (g_1005267c)
    {
        g_1005267c->field_0->field_8(g_1005267c);
        g_1005267c = 0;
    }
    if (g_10052658)
    {
        g_10052658->field_0->field_8(g_10052658);
        g_10052658 = 0;
    }
    return 0;
}
```

## `sub_100092b0` `0x100092b0`

_191 bytes. refs "sounds\\elfng.wav", "sounds\\playeronscreen.wav", "sounds\\gmdetected.wav"_

```c
typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

typedef struct struct_0 {
    char padding_0[8];
    struct struct_1 *field_8;
    char padding_c[32];
    struct struct_1 *field_2c;
    char padding_30[4];
    struct struct_1 *field_34;
    char padding_38[20];
    struct struct_1 *field_4c;
} struct_0;

extern int g_1005265c;
extern struct_0 **g_10052660;
extern struct_0 **g_10052664;
extern struct_0 **g_10052668;
extern struct_0 **g_1005266c;
extern struct_0 **g_10052670;
extern struct_0 **g_10052674;
extern struct_0 **g_10052678;
extern struct_0 **g_1005267c;
extern unsigned int g_1005f626;
extern unsigned int g_10287f3c;

unsigned int sub_100092b0(void)
{
    unsigned int v1;  // eax

    v1 = sub_1000904c(g_1005f626, 2, 44100, 16);
    if (!v1)
    {
        sub_10008e41("sounds\\elfng.wav", &g_1005265c);
        sub_1000936f(g_1005265c);
        sub_10008e41("sounds\\playeronscreen.wav", &g_10052660);
        sub_10008e41("sounds\\gmdetected.wav", &g_10052670);
        sub_10008e41("sounds\\playerattacking.wav", &g_10052664);
        sub_10008e41("sounds\\defaultmessage.wav", &g_10052668);
        sub_10008e41("sounds\\privatemessage.wav", &g_1005266c);
        sub_10008e41("sounds\\monster.wav", &g_10052678);
        sub_10008e41("sounds\\disconnected.wav", &g_10052674);
        sub_10008e41("sounds\\loot.wav", &g_1005267c);
        return 0;
    }
    g_10287f3c = 1;
    return v1;
}
```

## `sub_1000936f` `0x1000936f`

_52 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[48];
    struct struct_1 *field_30;
    struct struct_1 *field_34;
} struct_0;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern unsigned int g_10287f3c;

void sub_1000936f(struct_0 **a0)
{
    if (!a0)
        return;
    if (g_10287f3c)
        return;
    *(a0)->field_34(a0, 0);
    *(a0)->field_30(a0, 0, 0, 0);
    return;
}
```

## `sub_100093a3` `0x100093a3`

_175 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[80];
    unsigned int field_50;
} struct_0;

extern SOCKET g_100428d5;
extern unsigned int g_10052660[4];
extern unsigned int g_100580f8;
extern unsigned int g_100580fc;
extern struct_0 *g_1005f7ed;
extern char g_101d5e6d;
extern char g_10207f12[4];
extern unsigned int g_10287f3c;
extern unsigned int g_10287f40;
extern unsigned int g_63fedc;

int sub_100093a3(void)
{
    unsigned int v12;  // eax
    unsigned int v13;  // ecx
    unsigned int v14;  // edx
    unsigned int v15;  // ebx
    unsigned int v16;  // esi
    unsigned int v17;  // edi
    char v18[3];  // ebx
    char v0[3];  // [bp-0x2c]
    unsigned int v1;  // [bp-0x28]
    unsigned int v2;  // [bp-0x24]
    char *v3;  // [bp-0x20]
    char *v4;  // [bp-0x1c]
    unsigned int v5;  // [bp-0x18]
    unsigned int v6;  // [bp-0x14]
    unsigned int v7;  // [bp-0x10]
    unsigned int v8;  // [bp-0xc]
    int v9;  // [bp-0x8], Other Possible Types: char
    char v10;  // [bp-0x4]
    unsigned int v11;  // [bp+0x4]

    v8 = v12;
    v7 = v13;
    v6 = v14;
    v5 = v15;
    v4 = &v9;
    v3 = &v10;
    v2 = v16;
    v1 = v17;
    v18 = &g_10207f12[3 * v11];
    if (v18[0])
    {
        if (!g_10287f3c)
        {
            v0 = v18;
            sub_1000936f(g_10052660[v11]);
        }
        if (!g_101d5e6d)
            g_100580f8 = 1;
    }
    if (v18[1])
    {
        g_100580fc = 1;
        if (!g_10287f40)
        {
            g_63fedc = 0;
            *((unsigned short *)&v9) = 1;
            if (g_1005f7ed)
            {
                *((char *)&(&v9)[2]) = (char)g_1005f7ed->field_50 + 111;
                sub_1002ade7(&v9, 3, v18);
                v18 = &v9;
            }
        }
        g_10287f40 = 10;
    }
    if (v18[2])
        shutdown(g_100428d5, SD_BOTH);
    return;
}
```

## `sub_10009452` `0x10009452`

_55 bytes. (leaf/helper — see body)_

```c
typedef struct FLASHWINFO {
    unsigned int cbSize;
    HWND hwnd;
    enum FLASHWINFO_FLAGS dwFlags;
    unsigned int uCount;
    unsigned int dwTimeout;
} FLASHWINFO;

int sub_10009452(void)
{
    int v2;  // ebx
    FLASHWINFO v0;  // [bp-0x18]

    v0.cbSize = 20;
    v0.hwnd = sub_10039b62(v2, v0.cbSize);
    *((unsigned int *)&v0.dwFlags) = 15;
    v0.uCount = 5;
    v0.dwTimeout = 0;
    return FlashWindowEx(&v0);
}
```

## `sub_10009489` `0x10009489`

_197 bytes. (leaf/helper — see body)_

```c
typedef struct struct_3 {
    struct struct_1 *field_0;
    char field_1;
    char field_2;
    char padding_3[1];
    unsigned int field_4;
    unsigned int field_8;
    unsigned int field_c;
} struct_3;

typedef struct struct_0 {
    char padding_0[80];
    unsigned int field_50;
} struct_0;

typedef struct struct_1 {
    char padding_0[48];
    struct struct_2 *field_30;
} struct_1;

typedef struct struct_2 {
    unsigned int field_0;
} struct_2;

extern SOCKET g_100428d5;
extern struct_3 g_10052660;
extern unsigned int g_100580f8;
extern unsigned int g_100580fc;
extern struct_0 *g_1005f7ed;
extern char g_101d5e6d;
extern char g_10207f12[4];
extern unsigned int g_10287f3c;
extern unsigned int g_10287f40;
extern unsigned int g_63fedc;

int sub_10009489(void)
{
    unsigned int v12;  // eax
    unsigned int v13;  // ecx
    unsigned int v14;  // edx
    unsigned int v15;  // ebx
    unsigned int v16;  // esi
    unsigned int v17;  // edi
    struct_3 *v18;  // ebx
    struct_3 *v0;  // [bp-0x40]
    unsigned int v1;  // [bp-0x2c]
    unsigned int v2;  // [bp-0x28]
    char *v3;  // [bp-0x24]
    unsigned int v4;  // [bp-0x20]
    unsigned int v5;  // [bp-0x1c]
    unsigned int v6;  // [bp-0x18]
    unsigned int v7;  // [bp-0x14]
    unsigned int v8;  // [bp-0x10]
    int v9;  // [bp-0x8]
    char v10;  // [bp-0x4]
    unsigned int idx;  // [bp+0x4]

    v8 = v12;
    v7 = v13;
    v6 = v14;
    v5 = v15;
    v4 = &v15;
    v3 = &v10;
    v2 = v16;
    v1 = v17;
    v18 = &g_10207f12[3 * idx];
    if ((char)v18->field_0)
    {
        v18 = v18;
        if ((&g_10052660.field_0)[idx])
        {
            v18 = v18;
            if (!g_10287f3c)
            {
                v0 = (&g_10052660.field_0)[idx];
                (*((int *)(*((int *)&(&g_10052660.field_0)[idx]->padding_0[0]) + 48)))((&g_10052660.field_0)[idx], 0, 0, 0, v18);
                v18 = v0;
            }
        }
        if (!g_101d5e6d)
            g_100580f8 = 1;
    }
    if (*((char *)&v18->field_0 + 1) && !v15)
    {
        g_100580fc = 1;
        if (!g_10287f40)
        {
            g_63fedc = 0;
            *((unsigned short *)&v9) = 1;
            if (g_1005f7ed)
            {
                *((char *)&(&v9)[2]) = (char)g_1005f7ed->field_50 + 111;
                sub_1002ade7(&v9, 3, v18);
                v18 = &v9;
            }
        }
        g_10287f40 = 10;
    }
    if (*((char *)&v18->field_0 + 2))
        shutdown(g_100428d5, SD_BOTH);
    return;
}
```

## `sub_1000954e` `0x1000954e`

_175 bytes. refs "sounds\\%s"_

```c
typedef struct struct_2 {
    char field_0;
    char padding_1[127];
    struct struct_3 *field_80;
} struct_2;

typedef struct struct_0 {
    char padding_0[48];
    struct struct_1 *field_30;
} struct_0;

typedef struct struct_3 {
    struct struct_0 *field_0;
} struct_3;

typedef struct struct_1 {
    unsigned int field_0;
} struct_1;

extern unsigned int g_10287f3c;
extern struct_2 g_10287f44;
extern struct_2 g_10288fc4;

int sub_1000954e(int a0)
{
    struct_2 *iter;  // ebx
    unsigned int dst;  // eax
    struct_0 **v0;  // [bp-0x20c], Other Possible Types: struct_2 *, int
    Byte v1[512];  // [bp-0x208]
    struct_0 **v2;  // [bp-0x8]

    iter = &g_10287f44.field_0;
    while (true)
    {
        if (iter >= &g_10288fc4.field_0)
            return dst;
        if (!iter->field_0)
        {
            v0 = a0;
            dst = wsprintfA(v1, "sounds\\%s");
            if (!g_10287f3c)
            {
                v0 = iter;
                dst = sub_10008e41(v1, &iter->field_80);
            }
            if (iter->field_80)
            {
                dst = lstrcpy(iter, a0);
                break;
            }
        }
        else
        {
            dst = lstrcmpi(iter, a0);
            if (!dst)
                break;
        }
        iter += 1;
    }
    v0 = iter->field_80;
    v2 = iter->field_80;
    if (!g_10287f3c)
        dst = *(v2)->field_30(v2, 0, 0, 0);
    return dst;
}
```

## `sub_100095b1` `0x100095b1`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100095b1(void)
{
}
```

## `sub_1000d287` `0x1000d287`

_83 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_1000d21f[4];

unsigned int sub_1000d287(char *a0)
{
    unsigned int v2;  // ecx
    char v0;  // [bp-0x9]
    unsigned int i[4];  // [bp-0x8]

    v2 = *(a0);
    if ((char)v2 < 65)
    {
        return 0;
    }
    else if ((char)v2 <= 90)
    {
        v0 = v2;
        for (i = g_1000d21f[65 + v2]; (char)i[0] == v0; i += 2)
        {
            if (!lstrcmpi(i, a0))
                return 1;
        }
        return 0;
    }
    else
    {
        return 0;
    }
}
```

## `sub_1000d2da` `0x1000d2da`

_1678 bytes. refs "Trace paths space exceeded!", "Trace paths space exceeded!", "Trace paths space exceeded!"_

```c
typedef struct struct_0 {
    unsigned short field_0;
    unsigned short field_2;
    char padding_4[16];
    char field_14;
} struct_0;

typedef struct struct_2 {
    unsigned short field_0;
    unsigned short field_2;
    struct struct_0 *field_4;
    char padding_8[2];
    unsigned short field_a;
    unsigned int field_c;
    char padding_10[4];
    char field_14;
} struct_2;

typedef struct struct_17 {
    unsigned short field_0;
    unsigned short field_2;
    unsigned int field_4;
    unsigned short field_8;
    char padding_a[6];
    unsigned int field_10;
    char field_14;
    char field_15;
    char field_16;
} struct_17;

extern struct_17 *g_10052774;
extern char g_10052784;
extern unsigned int g_10052785[4];
extern unsigned int g_10053d69[4];
extern unsigned int g_10288fc4[4];

unsigned int sub_1000d2da(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int idx;  // ecx
    unsigned int v14[4];  // eax
    char v23;  // al
    unsigned int v24;  // ebx
    unsigned int v25;  // esi
    unsigned int v26;  // eax
    struct_2 *idx1;  // esi
    char v28;  // al
    unsigned int v29;  // ebx
    unsigned int v30;  // edx
    unsigned int v31;  // esi
    unsigned int v32;  // eax
    unsigned int idx2;  // ecx
    struct_2 *v33;  // esi
    char v34;  // al
    unsigned int v35;  // edx
    unsigned int v36;  // esi
    unsigned int v37;  // eax
    struct_2 *v38;  // esi
    char v39;  // al
    unsigned int n;  // ecx
    unsigned short v41[2];  // ecx
    unsigned int v42;  // ebx
    unsigned int m;  // ecx
    unsigned int v43;  // edx
    unsigned int v44;  // esi
    unsigned int v45;  // eax
    struct_2 *v46;  // esi
    char v47;  // al
    unsigned int v48;  // edx
    unsigned int v49;  // esi
    unsigned int v50;  // eax
    struct_2 *v51;  // esi
    char v52;  // al
    struct_0 *v17;  // ecx
    unsigned int v53;  // ebx
    unsigned int v54;  // esi
    unsigned int v55;  // eax
    struct_2 *v56;  // esi
    char v57;  // al
    unsigned int v58;  // edx
    unsigned int v59;  // esi
    unsigned int v60;  // eax
    struct_2 *v61;  // esi
    char v62;  // al
    unsigned int v18;  // edx
    unsigned int v19;  // ebx
    unsigned int v20;  // esi
    unsigned int v21;  // eax
    struct_2 *index;  // esi
    unsigned int v0;  // [bp-0x74]
    unsigned int v1;  // [bp-0x70]
    char v2;  // [bp-0x6c]
    unsigned int v3;  // [bp-0x2c]
    unsigned int v4;  // [bp-0x28]
    unsigned int v5;  // [bp-0x24]
    unsigned int v6;  // [bp-0x20]
    unsigned int v7;  // [bp-0x1c]
    unsigned int iter;  // [bp-0x18]
    unsigned int v9;  // [bp-0x14]
    unsigned int node;  // [bp-0x10]
    unsigned int iter1;  // [bp-0xc]
    unsigned int j;  // [bp-0x8]

    for (idx = 0; idx < 16; idx += 1)
    {
        v14 = g_10053d69[idx];
        if (a2)
            v14 = (unsigned int)((g_10053d69[idx] * a2 & 4294967295) / 5) + g_10053d69[idx];
        *((unsigned int *[4])&(&v2)[4 * idx]) = v14;
    }
    v3 = 0;
    iter = 0;
    for (j = 0; j < 14; j += 1)
    {
        iter1 = 0;
        while (iter1 < 18)
        {
            idx2 = (j * 18 + iter1) * 8;
            *((unsigned int *)(idx2 + (char *)&g_10288fc4[0])) = 0;
            if (*((int *)(idx2 + (char *)&g_10052785[0])) >= 4294967294)
            {
                *((unsigned int *)(idx2 + (char *)&g_10288fc4[0])) = 4294967295;
                iter1 += 1;
            }
            else
            {
                iter1 += 1;
            }
        }
    }
    g_10052774->field_0 = a0;
    g_10052774->field_2 = a1;
    g_10288fc4[36 * a1 + 2 * a0] = 1;
    g_10052774->field_10 = 0;
    g_10052774->field_15 = 0;
    g_10052774->field_4 = 0;
    g_10052774->field_8 = 0;
    g_10052774->field_14 = 0;
    g_10052774->field_16 = 0;
    iter = 1;
    v9 = 0;
    v6 = 0;
    v5 = 0;
    v4 = 0;
    node = 1;
    while (node < 16)
    {
        m = v9;
        for (v7 = iter; m < v7; m = v1 + 1)
        {
            v1 = m;
            v17 = &g_10052774[m];
            v18 = v17->field_2;
            v19 = v17->field_0 + 1;
            if (v19 < 18 && v18 < 14)
            {
                v20 = (v18 * 18 + v19) * 8;
                if (v19 == 8 && v18 == 6)
                    return 2;
                if (!*((int *)(v20 + (char *)&g_10288fc4[0])))
                {
                    v21 = *((int *)&(&v2)[4 * node]);
                    *((unsigned int *)(v20 + (char *)&g_10288fc4[0])) = v21;
                    if (iter >= 400000)
                    {
                        sub_10025172("Trace paths space exceeded!");
                        return 0;
                    }
                    index = &g_10052774[iter];
                    iter += 1;
                    index->field_0 = v19;
                    index->field_2 = v18;
                    index->field_4 = v17;
                    index->field_c = v21;
                    v0 = v21;
                    v23 = v17->field_14;
                    if (!v17->field_14)
                        v23 = 2;
                    index->field_14 = v23;
                    index->field_a = node;
                }
            }
            v24 = v19 - 2;
            if (v24 < 18 && v18 < 14)
            {
                v25 = (v18 * 18 + v24) * 8;
                if (v24 == 8 && v18 == 6)
                    return 4;
                if (!*((int *)(v25 + (char *)&g_10288fc4[0])))
                {
                    v26 = *((int *)&(&v2)[4 * node]);
                    *((unsigned int *)(v25 + (char *)&g_10288fc4[0])) = v26;
                    if (iter >= 400000)
                    {
                        sub_10025172("Trace paths space exceeded!");
                        return 0;
                    }
                    idx1 = &g_10052774[iter];
                    iter += 1;
                    idx1->field_0 = v24;
                    idx1->field_2 = v18;
                    idx1->field_4 = v17;
                    idx1->field_c = v26;
                    v0 = v26;
                    v28 = v17->field_14;
                    if (!v17->field_14)
                        v28 = 4;
                    idx1->field_14 = v28;
                    idx1->field_a = node;
                }
            }
            v29 = v24 + 1;
            v30 = v18 + 1;
            if (v29 < 18 && v30 < 14)
            {
                v31 = (v30 * 18 + v29) * 8;
                if (v29 == 8 && v30 == 6)
                    return 3;
                if (!*((int *)(v31 + (char *)&g_10288fc4[0])))
                {
                    v32 = *((int *)&(&v2)[4 * node]);
                    *((unsigned int *)(v31 + (char *)&g_10288fc4[0])) = v32;
                    if (iter >= 400000)
                    {
                        sub_10025172("Trace paths space exceeded!");
                        return 0;
                    }
                    v33 = &g_10052774[iter];
                    iter += 1;
                    v33->field_0 = v29;
                    v33->field_2 = v30;
                    v33->field_4 = v17;
                    v33->field_c = v32;
                    v0 = v32;
                    v34 = v17->field_14;
                    if (!v17->field_14)
                        v34 = 3;
                    v33->field_14 = v34;
                    v33->field_a = node;
                }
            }
            v35 = v30 - 2;
            if (v29 < 18 && v35 < 14)
            {
                v36 = (v35 * 18 + v29) * 8;
                if (v29 == 8 && v35 == 6)
                    return 1;
                if (!*((int *)(v36 + (char *)&g_10288fc4[0])))
                {
                    v37 = *((int *)&(&v2)[4 * node]);
                    *((unsigned int *)(v36 + (char *)&g_10288fc4[0])) = v37;
                    if (iter >= 400000)
                    {
                        sub_10025172("Trace paths space exceeded!");
                        return 0;
                    }
                    v38 = &g_10052774[iter];
                    iter += 1;
                    v38->field_0 = v29;
                    v38->field_2 = v35;
                    v38->field_4 = v17;
                    v38->field_c = v37;
                    v0 = v37;
                    v39 = v17->field_14;
                    if (!v17->field_14)
                        v39 = 1;
                    v38->field_14 = v39;
                    v38->field_a = node;
                }
            }
        }
        if (g_10052784)
        {
            n = v6;
            for (v4 = v5; n < v4; n = v1 + 1)
            {
                v1 = n;
                v41 = &g_10052774[n];
                v42 = v41[0] + 1;
                v43 = v41[1] - 1;
                if (v42 < 18 && v43 < 14)
                {
                    v44 = (v43 * 18 + v42) * 8;
                    if (v42 == 8 && v43 == 6)
                        return 5;
                    if (!*((int *)(v44 + (char *)&g_10288fc4[0])))
                    {
                        v45 = *((int *)&(&v2)[4 * node]);
                        *((unsigned int *)(v44 + (char *)&g_10288fc4[0])) = v45;
                        if (iter >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return 0;
                        }
                        v46 = &g_10052774[iter];
                        iter += 1;
                        v46->field_0 = v42;
                        v46->field_2 = v43;
                        v46->field_4 = v41;
                        v46->field_c = v45;
                        v0 = v45;
                        v47 = v41[5];
                        if (!(char)v41[5])
                            v47 = 5;
                        v46->field_14 = v47;
                        v46->field_a = node;
                    }
                }
                v48 = v43 + 2;
                if (v42 < 18 && v48 < 14)
                {
                    v49 = (v48 * 18 + v42) * 8;
                    if (v42 == 8 && v48 == 6)
                        return 6;
                    if (!*((int *)(v49 + (char *)&g_10288fc4[0])))
                    {
                        v50 = *((int *)&(&v2)[4 * node]);
                        *((unsigned int *)(v49 + (char *)&g_10288fc4[0])) = v50;
                        if (iter >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return 0;
                        }
                        v51 = &g_10052774[iter];
                        iter += 1;
                        v51->field_0 = v42;
                        v51->field_2 = v48;
                        v51->field_4 = v41;
                        v51->field_c = v50;
                        v0 = v50;
                        v52 = v41[5];
                        if (!(char)v41[5])
                            v52 = 6;
                        v51->field_14 = v52;
                        v51->field_a = node;
                    }
                }
                v53 = v42 - 2;
                if (v53 < 18 && v48 < 14)
                {
                    v54 = (v48 * 18 + v53) * 8;
                    if (v53 == 8 && v48 == 6)
                        return 7;
                    if (!*((int *)(v54 + (char *)&g_10288fc4[0])))
                    {
                        v55 = *((int *)&(&v2)[4 * node]);
                        *((unsigned int *)(v54 + (char *)&g_10288fc4[0])) = v55;
                        if (iter >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return 0;
                        }
                        v56 = &g_10052774[iter];
                        iter += 1;
                        v56->field_0 = v53;
                        v56->field_2 = v48;
                        v56->field_4 = v41;
                        v56->field_c = v55;
                        v0 = v55;
                        v57 = v41[5];
                        if (!(char)v41[5])
                            v57 = 7;
                        v56->field_14 = v57;
                        v56->field_a = node;
                    }
                }
                v58 = v48 - 2;
                if (v53 < 18 && v58 < 14)
                {
                    v59 = (v58 * 18 + v53) * 8;
                    if (v53 == 8 && v58 == 6)
                        return 8;
                    if (!*((int *)(v59 + (char *)&g_10288fc4[0])))
                    {
                        v60 = *((int *)&(&v2)[4 * node]);
                        *((unsigned int *)(v59 + (char *)&g_10288fc4[0])) = v60;
                        if (iter >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return 0;
                        }
                        v61 = &g_10052774[iter];
                        iter += 1;
                        v61->field_0 = v53;
                        v61->field_2 = v58;
                        v61->field_4 = v41;
                        v61->field_c = v60;
                        v0 = v60;
                        v62 = v41[5];
                        if (!(char)v41[5])
                            v62 = 8;
                        v61->field_14 = v62;
                        v61->field_a = node;
                    }
                }
            }
            v6 = v9;
            v5 = v7;
            v9 = v5;
            if (v5 == iter)
            {
                if (v6 == v5)
                    return 0;
                node += 1;
            }
            else
            {
                node += 1;
            }
        }
        else
        {
            v9 = v7;
            if (v9 == iter)
                return 0;
            node += 1;
        }
    }
    return 0;
}
```

## `sub_1000d946` `0x1000d946`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1000d946(void)
{
}
```

## `sub_1000d96a` `0x1000d96a`

_78 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_10052785[4];
extern unsigned int g_10288fc4[4];

void sub_1000d96a(void)
{
    unsigned int idx;  // ecx
    unsigned int j;  // [bp+0xffffc]
    unsigned int i;  // [bp+0x100000]

    for (i = 0; i < 14; i += 1)
    {
        j = 0;
        while (j < 18)
        {
            idx = (i * 18 + j) * 8;
            if (*((int *)(idx + (char *)&g_10288fc4[0])) >= 4294967294)
            {
                j += 1;
            }
            else if (*((int *)(idx + (char *)&g_10052785[0])) < 4294967294)
            {
                *((int *)(idx + (char *)&g_10052785[0])) = *((int *)(idx + (char *)&g_10052785[0])) + *((int *)(idx + (char *)&g_10288fc4[0]));
                *((unsigned int *)(/* unsupported instruction */ - 8)) = j + 1;
            }
            else
            {
                *((unsigned int *)(/* unsupported instruction */ - 8)) = j + 1;
            }
        }
    }
    return;
}
```

## `sub_1000d9b8` `0x1000d9b8`

_1745 bytes. refs "Trace paths space exceeded!", "Trace paths space exceeded!", "Trace paths space exceeded!"_

```c
typedef struct struct_17 {
    unsigned short field_0;
    unsigned short field_2;
    unsigned int field_4;
    unsigned short field_8;
    unsigned short field_a;
    char padding_c[4];
    unsigned int field_10;
    char field_14;
    char field_15;
    char field_16;
} struct_17;

typedef struct struct_0 {
    unsigned short field_0;
    unsigned short field_2;
    char padding_4[16];
    char field_14;
} struct_0;

typedef struct struct_2 {
    unsigned short field_0;
    unsigned short field_2;
    struct struct_0 *field_4;
    char padding_8[2];
    unsigned short field_a;
    unsigned int field_c;
    char padding_10[4];
    char field_14;
} struct_2;

extern unsigned int g_10052774;
extern char g_10052784;
extern unsigned int g_10052785[4];
extern unsigned int g_10053d69[4];
extern char g_10053da9;
extern unsigned int g_10288fc4[4];

unsigned int sub_1000d9b8(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int idx;  // ecx
    unsigned int v14[4];  // eax
    struct_0 *idx1;  // ecx
    unsigned int v24;  // edx
    unsigned int v25;  // ebx
    unsigned int v26;  // esi
    unsigned int v27;  // eax
    struct_2 *idx2;  // esi
    char v29;  // al
    unsigned int v30;  // ebx
    unsigned int v31;  // esi
    unsigned int v32;  // eax
    unsigned int v15;  // ecx
    struct_2 *v33;  // esi
    char v34;  // al
    unsigned int v35;  // ebx
    unsigned int v36;  // edx
    unsigned int v37;  // esi
    unsigned int v38;  // eax
    struct_2 *v39;  // esi
    char v40;  // al
    unsigned int v41;  // edx
    unsigned int v42;  // esi
    unsigned int v16;  // eax
    unsigned int v43;  // eax
    struct_2 *v44;  // esi
    char v45;  // al
    unsigned int n;  // ecx
    unsigned short v47[2];  // ecx
    unsigned int v48;  // ebx
    unsigned int v49;  // edx
    unsigned int v50;  // esi
    unsigned int v51;  // eax
    struct_2 *v52;  // esi
    unsigned int v17;  // ebx
    char v53;  // al
    unsigned int v54;  // edx
    unsigned int v55;  // esi
    unsigned int v56;  // eax
    struct_2 *v57;  // esi
    char v58;  // al
    unsigned int v59;  // ebx
    unsigned int v60;  // esi
    unsigned int v61;  // eax
    struct_2 *v62;  // esi
    unsigned int v18;  // ecx
    char v63;  // al
    unsigned int v64;  // edx
    unsigned int v65;  // esi
    unsigned int v66;  // eax
    struct_2 *v67;  // esi
    char v68;  // al
    struct_17 *v19;  // eax
    char v20;  // 4143
    unsigned int v21;  // ecx
    unsigned int m;  // ecx
    unsigned int v0;  // [bp-0x74]
    unsigned int v1;  // [bp-0x70]
    char v2;  // [bp-0x6c]
    unsigned int v3;  // [bp-0x2c]
    unsigned int v4;  // [bp-0x28]
    unsigned int v5;  // [bp-0x24]
    unsigned int v6;  // [bp-0x20]
    unsigned int v7;  // [bp-0x1c]
    unsigned int iter1;  // [bp-0x18]
    unsigned int v9;  // [bp-0x14]
    unsigned int iter;  // [bp-0x10]
    unsigned int node;  // [bp-0xc]
    unsigned int j;  // [bp-0x8]

    for (idx = 0; idx < 16; idx += 1)
    {
        v14 = g_10053d69[idx];
        if (a2)
            v14 = (unsigned int)((g_10053d69[idx] * a2 & 4294967295) / 5) + g_10053d69[idx];
        *((unsigned int *[4])&(&v2)[4 * idx]) = v14;
    }
    v3 = 0;
    iter1 = 0;
    for (j = 0; j < 14; j += 1)
    {
        node = 0;
        while (node < 18)
        {
            v15 = (j * 18 + node) * 8;
            *((unsigned int *)(v15 + (char *)&g_10288fc4[0])) = 0;
            if (*((int *)(v15 + (char *)&g_10052785[0])) >= 4294967294)
            {
                *((unsigned int *)(v15 + (char *)&g_10288fc4[0])) = 4294967295;
                node += 1;
            }
            else
            {
                v16 = node - a0 + 1;
                v17 = j - a1 + 1;
                if (v16 > 2)
                {
                    node += 1;
                }
                else if (v17 <= 2)
                {
                    v18 = v17 * 3 + v16;
                    v19 = iter1 * 23 + g_10052774;
                    iter1 += 1;
                    v20 = (&g_10053da9)[v18];
                    v21 = _INSERT(v18, 0, (&g_10053da9)[v18]);
                    v19->field_4 = 0;
                    v19->field_8 = 0;
                    v19->field_10 = 0;
                    v19->field_15 = 0;
                    v19->field_16 = 0;
                    v19->field_14 = v20;
                    v19->field_0 = node;
                    v19->field_2 = j;
                    v19->field_a = 1;
                    if (!v19->field_14)
                        v19->field_a = 0;
                    *((unsigned int *)(v21 + (char *)&g_10288fc4[0])) = 1;
                    node += 1;
                }
                else
                {
                    node += 1;
                }
            }
        }
    }
    v9 = 0;
    v6 = 0;
    v5 = 0;
    v4 = 0;
    iter = 1;
    while (iter < 16)
    {
        m = v9;
        for (v7 = iter1; m < v7; m = v1 + 1)
        {
            v1 = m;
            idx1 = m * 23 + g_10052774;
            v24 = idx1->field_2;
            v25 = idx1->field_0 + 1;
            if (v25 < 18 && v24 < 14)
            {
                v26 = (v24 * 18 + v25) * 8;
                if (v25 == 8 && v24 == 6)
                    return 2;
                if (!*((int *)(v26 + (char *)&g_10288fc4[0])))
                {
                    v27 = *((int *)&(&v2)[4 * iter]);
                    *((unsigned int *)(v26 + (char *)&g_10288fc4[0])) = v27;
                    if (iter1 >= 400000)
                    {
                        sub_10025172("Trace paths space exceeded!");
                        return 0;
                    }
                    idx2 = iter1 * 23 + g_10052774;
                    iter1 += 1;
                    idx2->field_0 = v25;
                    idx2->field_2 = v24;
                    idx2->field_4 = idx1;
                    idx2->field_c = v27;
                    v0 = v27;
                    v29 = idx1->field_14;
                    if (!idx1->field_14)
                        v29 = 2;
                    idx2->field_14 = v29;
                    idx2->field_a = iter;
                }
            }
            v30 = v25 - 2;
            if (v30 < 18 && v24 < 14)
            {
                v31 = (v24 * 18 + v30) * 8;
                if (v30 == 8 && v24 == 6)
                    return 4;
                if (!*((int *)(v31 + (char *)&g_10288fc4[0])))
                {
                    v32 = *((int *)&(&v2)[4 * iter]);
                    *((unsigned int *)(v31 + (char *)&g_10288fc4[0])) = v32;
                    if (iter1 >= 400000)
                    {
                        sub_10025172("Trace paths space exceeded!");
                        return 0;
                    }
                    v33 = iter1 * 23 + g_10052774;
                    iter1 += 1;
                    v33->field_0 = v30;
                    v33->field_2 = v24;
                    v33->field_4 = idx1;
                    v33->field_c = v32;
                    v0 = v32;
                    v34 = idx1->field_14;
                    if (!idx1->field_14)
                        v34 = 4;
                    v33->field_14 = v34;
                    v33->field_a = iter;
                }
            }
            v35 = v30 + 1;
            v36 = v24 + 1;
            if (v35 < 18 && v36 < 14)
            {
                v37 = (v36 * 18 + v35) * 8;
                if (v35 == 8 && v36 == 6)
                    return 3;
                if (!*((int *)(v37 + (char *)&g_10288fc4[0])))
                {
                    v38 = *((int *)&(&v2)[4 * iter]);
                    *((unsigned int *)(v37 + (char *)&g_10288fc4[0])) = v38;
                    if (iter1 >= 400000)
                    {
                        sub_10025172("Trace paths space exceeded!");
                        return 0;
                    }
                    v39 = iter1 * 23 + g_10052774;
                    iter1 += 1;
                    v39->field_0 = v35;
                    v39->field_2 = v36;
                    v39->field_4 = idx1;
                    v39->field_c = v38;
                    v0 = v38;
                    v40 = idx1->field_14;
                    if (!idx1->field_14)
                        v40 = 3;
                    v39->field_14 = v40;
                    v39->field_a = iter;
                }
            }
            v41 = v36 - 2;
            if (v35 < 18 && v41 < 14)
            {
                v42 = (v41 * 18 + v35) * 8;
                if (v35 == 8 && v41 == 6)
                    return 1;
                if (!*((int *)(v42 + (char *)&g_10288fc4[0])))
                {
                    v43 = *((int *)&(&v2)[4 * iter]);
                    *((unsigned int *)(v42 + (char *)&g_10288fc4[0])) = v43;
                    if (iter1 >= 400000)
                    {
                        sub_10025172("Trace paths space exceeded!");
                        return 0;
                    }
                    v44 = iter1 * 23 + g_10052774;
                    iter1 += 1;
                    v44->field_0 = v35;
                    v44->field_2 = v41;
                    v44->field_4 = idx1;
                    v44->field_c = v43;
                    v0 = v43;
                    v45 = idx1->field_14;
                    if (!idx1->field_14)
                        v45 = 1;
                    v44->field_14 = v45;
                    v44->field_a = iter;
                }
            }
        }
        if (g_10052784)
        {
            n = v6;
            for (v4 = v5; n < v4; n = v1 + 1)
            {
                v1 = n;
                v47 = n * 23 + g_10052774;
                v48 = v47[0] + 1;
                v49 = v47[1] - 1;
                if (v48 < 18 && v49 < 14)
                {
                    v50 = (v49 * 18 + v48) * 8;
                    if (v48 == 8 && v49 == 6)
                        return 5;
                    if (!*((int *)(v50 + (char *)&g_10288fc4[0])))
                    {
                        v51 = *((int *)&(&v2)[4 * iter]);
                        *((unsigned int *)(v50 + (char *)&g_10288fc4[0])) = v51;
                        if (iter1 >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return 0;
                        }
                        v52 = iter1 * 23 + g_10052774;
                        iter1 += 1;
                        v52->field_0 = v48;
                        v52->field_2 = v49;
                        v52->field_4 = v47;
                        v52->field_c = v51;
                        v0 = v51;
                        v53 = v47[5];
                        if (!(char)v47[5])
                            v53 = 5;
                        v52->field_14 = v53;
                        v52->field_a = iter;
                    }
                }
                v54 = v49 + 2;
                if (v48 < 18 && v54 < 14)
                {
                    v55 = (v54 * 18 + v48) * 8;
                    if (v48 == 8 && v54 == 6)
                        return 6;
                    if (!*((int *)(v55 + (char *)&g_10288fc4[0])))
                    {
                        v56 = *((int *)&(&v2)[4 * iter]);
                        *((unsigned int *)(v55 + (char *)&g_10288fc4[0])) = v56;
                        if (iter1 >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return 0;
                        }
                        v57 = iter1 * 23 + g_10052774;
                        iter1 += 1;
                        v57->field_0 = v48;
                        v57->field_2 = v54;
                        v57->field_4 = v47;
                        v57->field_c = v56;
                        v0 = v56;
                        v58 = v47[5];
                        if (!(char)v47[5])
                            v58 = 6;
                        v57->field_14 = v58;
                        v57->field_a = iter;
                    }
                }
                v59 = v48 - 2;
                if (v59 < 18 && v54 < 14)
                {
                    v60 = (v54 * 18 + v59) * 8;
                    if (v59 == 8 && v54 == 6)
                        return 7;
                    if (!*((int *)(v60 + (char *)&g_10288fc4[0])))
                    {
                        v61 = *((int *)&(&v2)[4 * iter]);
                        *((unsigned int *)(v60 + (char *)&g_10288fc4[0])) = v61;
                        if (iter1 >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return 0;
                        }
                        v62 = iter1 * 23 + g_10052774;
                        iter1 += 1;
                        v62->field_0 = v59;
                        v62->field_2 = v54;
                        v62->field_4 = v47;
                        v62->field_c = v61;
                        v0 = v61;
                        v63 = v47[5];
                        if (!(char)v47[5])
                            v63 = 7;
                        v62->field_14 = v63;
                        v62->field_a = iter;
                    }
                }
                v64 = v54 - 2;
                if (v59 < 18 && v64 < 14)
                {
                    v65 = (v64 * 18 + v59) * 8;
                    if (v59 == 8 && v64 == 6)
                        return 8;
                    if (!*((int *)(v65 + (char *)&g_10288fc4[0])))
                    {
                        v66 = *((int *)&(&v2)[4 * iter]);
                        *((unsigned int *)(v65 + (char *)&g_10288fc4[0])) = v66;
                        if (iter1 >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return 0;
                        }
                        v67 = iter1 * 23 + g_10052774;
                        iter1 += 1;
                        v67->field_0 = v59;
                        v67->field_2 = v64;
                        v67->field_4 = v47;
                        v67->field_c = v66;
                        v0 = v66;
                        v68 = v47[5];
                        if (!(char)v47[5])
                            v68 = 8;
                        v67->field_14 = v68;
                        v67->field_a = iter;
                    }
                }
            }
            v6 = v9;
            v5 = v7;
            v9 = v5;
            if (v5 == iter1)
            {
                if (v6 == v5)
                    return 0;
                iter += 1;
            }
            else
            {
                iter += 1;
            }
        }
        else
        {
            v9 = v7;
            if (v9 == iter1)
                return 0;
            iter += 1;
        }
    }
    return 0;
}
```

## `sub_1000dad5` `0x1000dad5`

_39 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
    unsigned short field_8;
    char padding_a[6];
    unsigned int field_10;
    char field_14;
    char field_15;
    char field_16;
} struct_0;

int sub_1000dad5(void)
{
    struct_0 *idx;  // eax
    unsigned int v1;  // [bp+0xffff0]

    idx->field_10 = 0;
    idx->field_15 = 0;
    idx->field_4 = 0;
    idx->field_8 = 0;
    idx->field_14 = 0;
    idx->field_16 = 0;
    v1 = 1;
}
```

## `sub_1000e08e` `0x1000e08e`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1000e08e(void)
{
}
```

## `sub_1000e0b2` `0x1000e0b2`

_78 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_10052785[4];
extern unsigned int g_10288fc4[4];

void sub_1000e0b2(void)
{
    unsigned int idx;  // ecx
    unsigned int j;  // [bp+0xffffc]
    unsigned int i;  // [bp+0x100000]

    for (i = 0; i < 14; i += 1)
    {
        j = 0;
        while (j < 18)
        {
            idx = (i * 18 + j) * 8;
            if (*((int *)(idx + (char *)&g_10288fc4[0])) >= 4294967294)
            {
                j += 1;
            }
            else if (*((int *)(idx + (char *)&g_10052785[0])) < 4294967294)
            {
                *((int *)(idx + (char *)&g_10052785[0])) = *((int *)(idx + (char *)&g_10052785[0])) + *((int *)(idx + (char *)&g_10288fc4[0]));
                *((unsigned int *)(/* unsupported instruction */ - 8)) = j + 1;
            }
            else
            {
                *((unsigned int *)(/* unsupported instruction */ - 8)) = j + 1;
            }
        }
    }
    return;
}
```

## `sub_1000e100` `0x1000e100`

_1463 bytes. refs "Trace paths space exceeded!", "Trace paths space exceeded!", "Trace paths space exceeded!"_

```c
typedef struct struct_18 {
    unsigned short field_0;
    unsigned short field_2;
    unsigned int field_4;
    unsigned short field_8;
    char padding_a[6];
    unsigned int field_10;
    char field_14;
    char field_15;
    char field_16;
} struct_18;

typedef struct struct_0 {
    unsigned short field_0;
    unsigned short field_2;
    char padding_4[16];
    char field_14;
} struct_0;

typedef struct struct_2 {
    unsigned short field_0;
    unsigned short field_2;
    struct struct_0 *field_4;
    char padding_8[2];
    unsigned short field_a;
    unsigned int field_c;
    char padding_10[4];
    char field_14;
} struct_2;

extern struct_18 *g_10052774;
extern char g_10052784;
extern unsigned int g_10052785[4];
extern unsigned int g_10053d69[4];
extern unsigned int g_10288fc4[4];

unsigned int sub_1000e100(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int idx;  // ecx
    unsigned int v14[4];  // eax
    struct_2 *index;  // esi
    char v24;  // al
    unsigned int v25;  // ebx
    unsigned int v26;  // esi
    unsigned int v27;  // eax
    struct_2 *idx1;  // esi
    char v29;  // al
    unsigned int v30;  // ebx
    unsigned int v31;  // edx
    unsigned int v32;  // esi
    unsigned int idx2;  // ecx
    unsigned int v33;  // eax
    struct_2 *v34;  // esi
    char v35;  // al
    unsigned int v36;  // edx
    unsigned int v37;  // esi
    unsigned int v38;  // eax
    struct_2 *v39;  // esi
    char v40;  // al
    unsigned int n;  // ecx
    struct_0 *v42;  // ecx
    struct_18 *v16;  // eax
    unsigned int v43;  // ebx
    unsigned int v44;  // edx
    unsigned int v45;  // esi
    unsigned int v46;  // eax
    struct_2 *v47;  // esi
    char v48;  // al
    unsigned int v49;  // edx
    unsigned int v50;  // esi
    unsigned int v51;  // eax
    struct_2 *v52;  // esi
    unsigned int m;  // ecx
    char v53;  // al
    unsigned int v54;  // ebx
    unsigned int v55;  // esi
    unsigned int v56;  // eax
    struct_2 *v57;  // esi
    char v58;  // al
    unsigned int v59;  // edx
    unsigned int v60;  // esi
    unsigned int v61;  // eax
    struct_2 *v62;  // esi
    struct_0 *v18;  // ecx
    char v63;  // al
    unsigned int v64;  // ecx
    unsigned int v19;  // edx
    unsigned int v20;  // ebx
    unsigned int v21;  // esi
    unsigned int v22;  // eax
    unsigned int v0;  // [bp-0x74]
    unsigned int v1;  // [bp-0x70]
    char v2;  // [bp-0x6c]
    unsigned int v3;  // [bp-0x2c]
    unsigned int v4;  // [bp-0x28]
    unsigned int v5;  // [bp-0x24]
    unsigned int v6;  // [bp-0x20]
    unsigned int v7;  // [bp-0x1c]
    unsigned int iter1;  // [bp-0x18]
    unsigned int v9;  // [bp-0x14]
    unsigned int iter;  // [bp-0x10]
    unsigned int node;  // [bp-0xc]
    unsigned int iter2;  // [bp-0x8]

    for (idx = 0; idx < 16; idx += 1)
    {
        v14 = g_10053d69[idx];
        if (a2)
            v14 = (unsigned int)((g_10053d69[idx] * a2 & 4294967295) / 5) + g_10053d69[idx];
        *((unsigned int *[4])&(&v2)[4 * idx]) = v14;
    }
    v3 = 0;
    for (iter2 = 0; iter2 < 14; iter2 += 1)
    {
        node = 0;
        while (node < 18)
        {
            idx2 = (iter2 * 18 + node) * 8;
            *((unsigned int *)(idx2 + (char *)&g_10288fc4[0])) = 0;
            if (*((int *)(idx2 + (char *)&g_10052785[0])) >= 4294967294)
            {
                *((unsigned int *)(idx2 + (char *)&g_10288fc4[0])) = 4294967295;
                node += 1;
            }
            else
            {
                node += 1;
            }
        }
    }
    v16 = g_10052774;
    g_10052774->field_0 = a0;
    g_10052774->field_2 = a1;
    g_10288fc4[36 * a1 + 2 * a0] = 1;
    g_10052774->field_10 = 0;
    g_10052774->field_15 = 0;
    g_10052774->field_4 = 0;
    g_10052774->field_8 = 0;
    g_10052774->field_14 = 0;
    g_10052774->field_16 = 0;
    iter1 = 1;
    v9 = 0;
    v6 = 0;
    v5 = 0;
    v4 = 0;
    iter = 1;
    while (iter < 16)
    {
        m = v9;
        for (v7 = iter1; m < v7; m = v1 + 1)
        {
            v1 = m;
            v18 = &g_10052774[m];
            v19 = v18->field_2;
            v20 = v18->field_0 + 1;
            if (v20 < 18 && v19 < 14)
            {
                v21 = (v19 * 18 + v20) * 8;
                if (!*((int *)(v21 + (char *)&g_10288fc4[0])))
                {
                    v22 = *((int *)&(&v2)[4 * iter]);
                    *((unsigned int *)(v21 + (char *)&g_10288fc4[0])) = v22;
                    if (iter1 >= 400000)
                    {
                        sub_10025172("Trace paths space exceeded!");
                        return 0;
                    }
                    index = &g_10052774[iter1];
                    iter1 += 1;
                    index->field_0 = v20;
                    index->field_2 = v19;
                    index->field_4 = v18;
                    index->field_c = v22;
                    v0 = v22;
                    v24 = v18->field_14;
                    if (!v18->field_14)
                        v24 = 2;
                    index->field_14 = v24;
                    index->field_a = iter;
                }
            }
            v25 = v20 - 2;
            if (v25 < 18 && v19 < 14)
            {
                v26 = (v19 * 18 + v25) * 8;
                if (!*((int *)(v26 + (char *)&g_10288fc4[0])))
                {
                    v27 = *((int *)&(&v2)[4 * iter]);
                    *((unsigned int *)(v26 + (char *)&g_10288fc4[0])) = v27;
                    if (iter1 >= 400000)
                    {
                        sub_10025172("Trace paths space exceeded!");
                        return 0;
                    }
                    idx1 = &g_10052774[iter1];
                    iter1 += 1;
                    idx1->field_0 = v25;
                    idx1->field_2 = v19;
                    idx1->field_4 = v18;
                    idx1->field_c = v27;
                    v0 = v27;
                    v29 = v18->field_14;
                    if (!v18->field_14)
                        v29 = 4;
                    idx1->field_14 = v29;
                    idx1->field_a = iter;
                }
            }
            v30 = v25 + 1;
            v31 = v19 + 1;
            if (v30 < 18 && v31 < 14)
            {
                v32 = (v31 * 18 + v30) * 8;
                if (!*((int *)(v32 + (char *)&g_10288fc4[0])))
                {
                    v33 = *((int *)&(&v2)[4 * iter]);
                    *((unsigned int *)(v32 + (char *)&g_10288fc4[0])) = v33;
                    if (iter1 >= 400000)
                    {
                        sub_10025172("Trace paths space exceeded!");
                        return 0;
                    }
                    v34 = &g_10052774[iter1];
                    iter1 += 1;
                    v34->field_0 = v30;
                    v34->field_2 = v31;
                    v34->field_4 = v18;
                    v34->field_c = v33;
                    v0 = v33;
                    v35 = v18->field_14;
                    if (!v18->field_14)
                        v35 = 3;
                    v34->field_14 = v35;
                    v34->field_a = iter;
                }
            }
            v36 = v31 - 2;
            if (v30 < 18 && v36 < 14)
            {
                v37 = (v36 * 18 + v30) * 8;
                if (!*((int *)(v37 + (char *)&g_10288fc4[0])))
                {
                    v38 = *((int *)&(&v2)[4 * iter]);
                    *((unsigned int *)(v37 + (char *)&g_10288fc4[0])) = v38;
                    if (iter1 >= 400000)
                    {
                        sub_10025172("Trace paths space exceeded!");
                        return 0;
                    }
                    v39 = &g_10052774[iter1];
                    iter1 += 1;
                    v39->field_0 = v30;
                    v39->field_2 = v36;
                    v39->field_4 = v18;
                    v39->field_c = v38;
                    v0 = v38;
                    v40 = v18->field_14;
                    if (!v18->field_14)
                        v40 = 1;
                    v39->field_14 = v40;
                    v39->field_a = iter;
                }
            }
        }
        if (g_10052784)
        {
            n = v6;
            for (v4 = v5; n < v4; n = v1 + 1)
            {
                v1 = n;
                v42 = &g_10052774[n];
                v43 = v42->field_0 + 1;
                v44 = v42->field_2 - 1;
                if (v43 < 18 && v44 < 14)
                {
                    v45 = (v44 * 18 + v43) * 8;
                    if (!*((int *)(v45 + (char *)&g_10288fc4[0])))
                    {
                        v46 = *((int *)&(&v2)[4 * iter]);
                        *((unsigned int *)(v45 + (char *)&g_10288fc4[0])) = v46;
                        if (iter1 >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return 0;
                        }
                        v47 = &g_10052774[iter1];
                        iter1 += 1;
                        v47->field_0 = v43;
                        v47->field_2 = v44;
                        v47->field_4 = v42;
                        v47->field_c = v46;
                        v0 = v46;
                        v48 = v42->field_14;
                        if (!v42->field_14)
                            v48 = 5;
                        v47->field_14 = v48;
                        v47->field_a = iter;
                    }
                }
                v49 = v44 + 2;
                if (v43 < 18 && v49 < 14)
                {
                    v50 = (v49 * 18 + v43) * 8;
                    if (!*((int *)(v50 + (char *)&g_10288fc4[0])))
                    {
                        v51 = *((int *)&(&v2)[4 * iter]);
                        *((unsigned int *)(v50 + (char *)&g_10288fc4[0])) = v51;
                        if (iter1 >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return 0;
                        }
                        v52 = &g_10052774[iter1];
                        iter1 += 1;
                        v52->field_0 = v43;
                        v52->field_2 = v49;
                        v52->field_4 = v42;
                        v52->field_c = v51;
                        v0 = v51;
                        v53 = v42->field_14;
                        if (!v42->field_14)
                            v53 = 6;
                        v52->field_14 = v53;
                        v52->field_a = iter;
                    }
                }
                v54 = v43 - 2;
                if (v54 < 18 && v49 < 14)
                {
                    v55 = (v49 * 18 + v54) * 8;
                    if (!*((int *)(v55 + (char *)&g_10288fc4[0])))
                    {
                        v56 = *((int *)&(&v2)[4 * iter]);
                        *((unsigned int *)(v55 + (char *)&g_10288fc4[0])) = v56;
                        if (iter1 >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return 0;
                        }
                        v57 = &g_10052774[iter1];
                        iter1 += 1;
                        v57->field_0 = v54;
                        v57->field_2 = v49;
                        v57->field_4 = v42;
                        v57->field_c = v56;
                        v0 = v56;
                        v58 = v42->field_14;
                        if (!v42->field_14)
                            v58 = 7;
                        v57->field_14 = v58;
                        v57->field_a = iter;
                    }
                }
                v59 = v49 - 2;
                if (v54 < 18 && v59 < 14)
                {
                    v60 = (v59 * 18 + v54) * 8;
                    if (!*((int *)(v60 + (char *)&g_10288fc4[0])))
                    {
                        v61 = *((int *)&(&v2)[4 * iter]);
                        *((unsigned int *)(v60 + (char *)&g_10288fc4[0])) = v61;
                        if (iter1 >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return 0;
                        }
                        v62 = &g_10052774[iter1];
                        iter1 += 1;
                        v62->field_0 = v54;
                        v62->field_2 = v59;
                        v62->field_4 = v42;
                        v62->field_c = v61;
                        v0 = v61;
                        v63 = v42->field_14;
                        if (!v42->field_14)
                            v63 = 8;
                        v62->field_14 = v63;
                        v62->field_a = iter;
                    }
                }
            }
            v6 = v9;
            v16 = v7;
            v5 = v16;
            v9 = v16;
            if (v16 != iter1)
            {
                iter += 1;
            }
            else if (v6 == v5)
            {
                v16 = 0;
                break;
            }
            else
            {
                iter += 1;
            }
        }
        else
        {
            v16 = v7;
            v9 = v16;
            if (v16 == iter1)
            {
                v16 = 0;
                break;
            }
            else
            {
                iter += 1;
            }
        }
    }
    for (iter2 = 0; iter2 < 14; iter2 += 1)
    {
        node = 0;
        while (node < 18)
        {
            v64 = (iter2 * 18 + node) * 8;
            v16 = *((int *)(v64 + (char *)&g_10288fc4[0]));
            if (v16 >= 4294967294)
            {
                node += 1;
            }
            else if (*((int *)(v64 + (char *)&g_10052785[0])) < 4294967294)
            {
                *((struct_18 **)(v64 + (char *)&g_10052785[0])) = *((int *)(v64 + (char *)&g_10052785[0])) + (char *)v16;
                node += 1;
            }
            else
            {
                node += 1;
            }
        }
    }
    return v16;
}
```

## `sub_1000e64d` `0x1000e64d`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1000e64d(void)
{
}
```

## `sub_1000e6b9` `0x1000e6b9`

_3364 bytes. refs "Trace paths space exceeded!", "Trace paths space exceeded!", "Trace paths space exceeded!"_

```c
typedef struct struct_0 {
    unsigned short field_0;
    unsigned short field_2;
    struct struct_1 *field_4;
    unsigned short field_8;
    unsigned short field_a;
    unsigned int field_c;
    unsigned int field_10;
    char field_14;
} struct_0;

typedef struct struct_8 {
    unsigned short field_0;
    unsigned short field_2;
    char padding_4[4];
    unsigned short field_8;
    char padding_a[6];
    unsigned int field_10;
    char field_14;
    char field_15;
} struct_8;

typedef struct struct_9 {
    unsigned short field_0;
    unsigned short field_2;
    struct struct_8 *field_4;
    unsigned short field_8;
    unsigned short field_a;
    unsigned int field_c;
    unsigned int field_10;
    char field_14;
    char field_15;
} struct_9;

typedef struct struct_17 {
    unsigned short field_0;
    unsigned short field_2;
    unsigned int field_4;
    unsigned short field_8;
    unsigned short field_a;
    char padding_c[4];
    unsigned int field_10;
    char field_14;
    char padding_15[2];
    char field_17;
    char padding_18[22];
    char field_2e;
} struct_17;

typedef struct struct_1 {
    unsigned short field_0;
    unsigned short field_2;
    char padding_4[4];
    unsigned short field_8;
} struct_1;

extern struct_17 *g_10052774;
extern unsigned int g_10052780;
extern char g_10052784;
extern unsigned int g_10052785[4];
extern unsigned int g_10052a95;
extern unsigned int g_10052b1d;
extern unsigned int g_10052b2d;
extern unsigned int g_10052bb5;
extern unsigned int g_10053db2[4];
extern unsigned int g_10288fc4[4];
extern unsigned int g_102892d4;
extern unsigned int g_1028935c;
extern unsigned int g_10289364;
extern unsigned int g_1028936c;
extern unsigned int g_102893f4;
extern unsigned int g_102897a4[4];
extern unsigned int g_102897a8[4];
extern unsigned int g_102897ac[4];
extern unsigned int g_102897e4[4];
extern unsigned int g_102897e8;

unsigned int [4] sub_1000e6b9(unsigned int a0, unsigned int a1, unsigned int *a2)
{
    unsigned int idx;  // ecx
    unsigned int v32[4];  // ecx
    struct_0 *index;  // esi
    char v42;  // al
    unsigned int v43;  // edx
    unsigned int v44;  // edi
    unsigned int v45;  // eax
    unsigned int v46;  // ebx
    unsigned int idx1;  // esi
    unsigned int v48;  // eax
    struct_0 *idx2;  // esi
    char v50;  // al
    unsigned int v33[4];  // eax
    unsigned int v51;  // edx
    unsigned int v52;  // edi
    unsigned int v53;  // eax
    unsigned int v54;  // ebx
    unsigned int v55;  // edx
    unsigned int v56;  // esi
    unsigned int v57;  // eax
    struct_0 *v58;  // esi
    char v59;  // al
    unsigned int v60;  // edx
    unsigned int iter;  // edi
    unsigned int v61;  // edi
    unsigned int v62;  // eax
    unsigned int v63;  // edx
    unsigned int v64;  // esi
    unsigned int v65;  // eax
    struct_0 *v66;  // esi
    char v67;  // al
    unsigned int v68;  // edx
    unsigned int v69;  // edi
    unsigned int v70;  // eax
    unsigned int m;  // ecx
    unsigned int n;  // ecx
    struct_8 *v72;  // ecx
    unsigned int v73;  // ebx
    unsigned int v74;  // edx
    unsigned int v75;  // esi
    unsigned int v76;  // eax
    struct_9 *v77;  // esi
    char v78;  // al
    unsigned int v79;  // edx
    unsigned int v80;  // edi
    unsigned short v36[5];  // ecx
    unsigned int v81;  // eax
    unsigned int v82;  // edx
    unsigned int v83;  // esi
    unsigned int v84;  // eax
    struct_9 *v85;  // esi
    char v86;  // al
    unsigned int v87;  // edx
    unsigned int v88;  // edi
    unsigned int v89;  // eax
    unsigned int v90;  // ebx
    unsigned int v37;  // edx
    unsigned int v91;  // esi
    unsigned int v92;  // eax
    struct_9 *v93;  // esi
    char v94;  // al
    unsigned int v95;  // edx
    unsigned int v96;  // edi
    unsigned int v97;  // eax
    unsigned int v98;  // edx
    unsigned int v99;  // esi
    unsigned int v100;  // eax
    unsigned int v38;  // ebx
    struct_9 *v101;  // esi
    char v102;  // al
    unsigned int v103;  // edx
    unsigned int v104;  // edi
    unsigned int v105;  // eax
    unsigned int v106[4];  // eax
    unsigned int v107;  // ecx
    struct_17 *iter1;  // ebx
    unsigned int v109;  // ecx
    unsigned int v110;  // ecx
    unsigned int v39;  // esi
    unsigned int v111;  // ecx
    unsigned int v112;  // ecx
    unsigned int v40;  // eax
    unsigned int v0;  // [bp-0x9c]
    struct_0 *v1;  // [bp-0x98], Other Possible Types: struct_9 *
    char *v2;  // [bp-0x94]
    char *v3;  // [bp-0x90]
    unsigned int v4;  // [bp-0x8c]
    unsigned int v5;  // [bp-0x88]
    struct_8 *v6;  // [bp-0x84], Other Possible Types: unsigned short [5], unsigned int
    unsigned int v7;  // [bp-0x80]
    unsigned int v8;  // [bp-0x7c]
    unsigned int v9;  // [bp-0x78]
    unsigned int v10;  // [bp-0x74]
    unsigned int v11[4];  // [bp-0x70]
    unsigned int v12;  // [bp-0x2c]
    unsigned int v13;  // [bp-0x2c]
    unsigned int v14;  // [bp-0x2c]
    unsigned int v15;  // [bp-0x2c]
    unsigned int v16;  // [bp-0x2c]
    unsigned int v17;  // [bp-0x2c]
    unsigned int v18;  // [bp-0x2c]
    unsigned int v19;  // [bp-0x2c]
    unsigned int v20;  // [bp-0x2c]
    unsigned int v21;  // [bp-0x28]
    unsigned int v22;  // [bp-0x24]
    unsigned int v23;  // [bp-0x20]
    unsigned int v24;  // [bp-0x1c]
    unsigned int node;  // [bp-0x18]
    unsigned int v26;  // [bp-0x14]
    unsigned int iter2;  // [bp-0x10]
    unsigned int l;  // [bp-0xc]
    unsigned int i;  // [bp-0x8]
    char v30;  // [bp-0x4]

    v12 = 0;
    for (i = 0; i < 14; i += 1)
    {
        l = 0;
        while (l < 18)
        {
            idx = (i * 18 + l) * 8;
            *((unsigned int *)(idx + (char *)&g_10288fc4[0])) = 0;
            if (*((int *)(idx + (char *)&g_10052785[0])) >= 4294967294)
            {
                *((unsigned int *)(idx + (char *)&g_10288fc4[0])) = 4294967295;
                l += 1;
            }
            else
            {
                l += 1;
            }
        }
    }
    v32 = (a1 - 6 ^ a1 - 6 >> 31) - (a1 - 6 >> 31);
    v33 = (a0 - 8 ^ a0 - 8 >> 31) - (a0 - 8 >> 31);
    if (v33 == a2 && v32 == a2)
        return v33;
    node = 0;
    g_10052774->field_0 = 8;
    g_10052774->field_2 = 6;
    g_10052774->field_4 = 0;
    g_10052774->field_8 = 0;
    g_10052774->field_10 = 0;
    g_10052774->padding_15[0] = 0;
    g_10052774->padding_15[1] = 0;
    g_10052774->field_14 = 255;
    iter = &g_10052774->field_17;
    node += 1;
    g_10289364 = 1;
    if (v32 == a2)
    {
        if (a0 >= 8 && g_10052b1d < 4294967294)
        {
            *((unsigned short *)iter) = 7;
            *((unsigned short *)(iter + 2)) = 6;
            *((unsigned int *)(iter + 4)) = 0;
            *((unsigned short *)(iter + 8)) = 0;
            *((unsigned int *)(iter + 16)) = 0;
            *((char *)(iter + 21)) = 0;
            *((char *)(iter + 22)) = 0;
            *((char *)(iter + 20)) = 4;
            *((char *)(iter + 20)) = 0;
            g_1028935c = 1;
            iter += 23;
            node += 1;
        }
        if (a0 <= 8 && g_10052b2d < 4294967294)
        {
            *((unsigned short *)iter) = 9;
            *((unsigned short *)(iter + 2)) = 6;
            *((unsigned int *)(iter + 4)) = 0;
            *((unsigned short *)(iter + 8)) = 0;
            *((unsigned int *)(iter + 16)) = 0;
            *((char *)(iter + 21)) = 0;
            *((char *)(iter + 22)) = 0;
            *((char *)(iter + 20)) = 2;
            g_1028936c = 1;
            iter += 23;
            node += 1;
        }
    }
    if (v32 < a2 && v33 == a2)
    {
        if (a1 >= 6 && g_10052a95 < 4294967294)
        {
            *((unsigned short *)iter) = 8;
            *((unsigned short *)(iter + 2)) = 5;
            *((unsigned int *)(iter + 4)) = 0;
            *((unsigned short *)(iter + 8)) = 0;
            *((unsigned int *)(iter + 16)) = 0;
            *((char *)(iter + 21)) = 0;
            *((char *)(iter + 22)) = 0;
            *((char *)(iter + 20)) = 1;
            g_102892d4 = 1;
            iter += 23;
            node += 1;
        }
        if (a1 <= 6 && g_10052bb5 < 4294967294)
        {
            *((unsigned short *)iter) = 8;
            *((unsigned short *)(iter + 2)) = 7;
            *((unsigned int *)(iter + 4)) = 0;
            *((unsigned short *)(iter + 8)) = 0;
            *((unsigned int *)(iter + 16)) = 0;
            *((char *)(iter + 21)) = 0;
            *((char *)(iter + 22)) = 0;
            *((char *)(iter + 20)) = 3;
            g_102893f4 = 1;
            node += 1;
        }
    }
    if (node < 2)
        return v33;
    v26 = 0;
    v23 = 0;
    v22 = 0;
    v21 = 0;
    iter2 = 1;
    while (iter2 < 18)
    {
        m = v26;
        for (v24 = node; m < v24; m += 1)
        {
            v8 = m;
            v36 = 23 * m + (char *)g_10052774;
            v37 = v36[1];
            v38 = v36[0] + 1;
            if (v38 < 18 && v37 < 14)
            {
                v39 = (v37 * 18 + v38) * 8;
                if (!*((int *)(v39 + (char *)&g_10288fc4[0])) || *((int *)(v39 + (char *)&g_10288fc4[0])) == iter2)
                {
                    *((unsigned int *)(v39 + (char *)&g_10288fc4[0])) = iter2;
                    v40 = *((int *)(v39 + (char *)&g_10052785[0]));
                    if (!*((char *)&v36[2] + 1))
                    {
                        if (node >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return NULL;
                        }
                        index = 23 * node + (char *)g_10052774;
                        node += 1;
                        index->field_0 = v38;
                        index->field_2 = v37;
                        index->field_4 = v36;
                        index->field_c = v40;
                        v7 = v40;
                        v42 = v36[2];
                        if (!(char)v36[2])
                            v42 = 2;
                        index->field_14 = v42;
                        index->field_a = iter2;
                        if (v40 < 4294967294 && *((int *)&v36[1 + 3]) < 4294967294)
                            index->field_10 = v40 + *((int *)&v36[1 + 3]);
                        index->field_8 = v36[4];
                        *((char *)&index[1].field_0) = 0;
                        v7 = v37;
                        index->field_8 = index->field_8 + (unsigned short)((8 - (unsigned short)v38 ^ 8 - (unsigned short)v38 >> 31) - (8 - (unsigned short)v38 >> 31));
                        v43 = v37;
                        v7 = v43;
                        v44 = (unsigned short)v43;
                        index->field_8 = index->field_8 + (unsigned short)((8 - v44 ^ 8 - v44 >> 31) - (8 - v44 >> 31));
                        v45 = index->field_8;
                        if (v45 > v12)
                        {
                            v17 = v45;
                            v12 = v17;
                        }
                        v7 = v17;
                        v6 = v36;
                        v5 = v43;
                        v4 = v38;
                        v3 = &v8;
                        v2 = &v30;
                        v1 = index;
                        v0 = v44;
                        *((char *)&index[1].field_0) = 0;
                        if ((a0 - v38 ^ a0 - v38 >> 31) - (a0 - v38 >> 31) <= a2 && (a1 - v5 ^ a1 - v5 >> 31) - (a1 - v5 >> 31) <= a2)
                            *((char *)&index[1].field_0) = 1;
                        v36 = v6;
                        v37 = v5;
                        v38 = v4;
                    }
                }
            }
            v46 = v38 - 2;
            if (v46 < 18 && v37 < 14)
            {
                idx1 = (v37 * 18 + v46) * 8;
                if (!*((int *)(idx1 + (char *)&g_10288fc4[0])) || *((int *)(idx1 + (char *)&g_10288fc4[0])) == iter2)
                {
                    *((unsigned int *)(idx1 + (char *)&g_10288fc4[0])) = iter2;
                    v48 = *((int *)(idx1 + (char *)&g_10052785[0]));
                    if (!*((char *)&v36[2] + 1))
                    {
                        if (node >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return NULL;
                        }
                        idx2 = 23 * node + (char *)g_10052774;
                        node += 1;
                        idx2->field_0 = v46;
                        idx2->field_2 = v37;
                        idx2->field_4 = v36;
                        idx2->field_c = v48;
                        v7 = v48;
                        v50 = v36[2];
                        if (!(char)v36[2])
                            v50 = 4;
                        idx2->field_14 = v50;
                        idx2->field_a = iter2;
                        if (v48 < 4294967294 && *((int *)&v36[1 + 3]) < 4294967294)
                            idx2->field_10 = v48 + *((int *)&v36[1 + 3]);
                        idx2->field_8 = v36[4];
                        *((char *)&idx2[1].field_0) = 0;
                        v7 = v37;
                        idx2->field_8 = idx2->field_8 + (unsigned short)((8 - (unsigned short)v46 ^ 8 - (unsigned short)v46 >> 31) - (8 - (unsigned short)v46 >> 31));
                        v51 = v37;
                        v7 = v51;
                        v52 = (unsigned short)v51;
                        idx2->field_8 = idx2->field_8 + (unsigned short)((8 - v52 ^ 8 - v52 >> 31) - (8 - v52 >> 31));
                        v53 = idx2->field_8;
                        if (v53 > v12)
                        {
                            v18 = v53;
                            v12 = v18;
                        }
                        v7 = v18;
                        v6 = v36;
                        v5 = v51;
                        v4 = v46;
                        v3 = &v8;
                        v2 = &v30;
                        v1 = idx2;
                        v0 = v52;
                        *((char *)&idx2[1].field_0) = 0;
                        if ((a0 - v46 ^ a0 - v46 >> 31) - (a0 - v46 >> 31) <= a2 && (a1 - v5 ^ a1 - v5 >> 31) - (a1 - v5 >> 31) <= a2)
                            *((char *)&idx2[1].field_0) = 1;
                        v36 = v6;
                        v37 = v5;
                        v46 = v4;
                    }
                }
            }
            v54 = v46 + 1;
            v55 = v37 + 1;
            if (v54 < 18 && v55 < 14)
            {
                v56 = (v55 * 18 + v54) * 8;
                if (!*((int *)(v56 + (char *)&g_10288fc4[0])) || *((int *)(v56 + (char *)&g_10288fc4[0])) == iter2)
                {
                    *((unsigned int *)(v56 + (char *)&g_10288fc4[0])) = iter2;
                    v57 = *((int *)(v56 + (char *)&g_10052785[0]));
                    if (!*((char *)&v36[2] + 1))
                    {
                        if (node >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return NULL;
                        }
                        v58 = 23 * node + (char *)g_10052774;
                        node += 1;
                        v58->field_0 = v54;
                        v58->field_2 = v55;
                        v58->field_4 = v36;
                        v58->field_c = v57;
                        v7 = v57;
                        v59 = v36[2];
                        if (!(char)v36[2])
                            v59 = 3;
                        v58->field_14 = v59;
                        v58->field_a = iter2;
                        if (v57 < 4294967294 && *((int *)&v36[1 + 3]) < 4294967294)
                            v58->field_10 = v57 + *((int *)&v36[1 + 3]);
                        v58->field_8 = v36[4];
                        *((char *)&v58[1].field_0) = 0;
                        v7 = v55;
                        v58->field_8 = v58->field_8 + (unsigned short)((8 - (unsigned short)v54 ^ 8 - (unsigned short)v54 >> 31) - (8 - (unsigned short)v54 >> 31));
                        v60 = v55;
                        v7 = v60;
                        v61 = (unsigned short)v60;
                        v58->field_8 = v58->field_8 + (unsigned short)((8 - v61 ^ 8 - v61 >> 31) - (8 - v61 >> 31));
                        v62 = v58->field_8;
                        if (v62 > v12)
                        {
                            v19 = v62;
                            v12 = v19;
                        }
                        v7 = v19;
                        v6 = v36;
                        v5 = v60;
                        v4 = v54;
                        v3 = &v8;
                        v2 = &v30;
                        v1 = v58;
                        v0 = v61;
                        *((char *)&v58[1].field_0) = 0;
                        if ((a0 - v54 ^ a0 - v54 >> 31) - (a0 - v54 >> 31) <= a2 && (a1 - v5 ^ a1 - v5 >> 31) - (a1 - v5 >> 31) <= a2)
                            *((char *)&v58[1].field_0) = 1;
                        v36 = v6;
                        v55 = v5;
                        v54 = v4;
                    }
                }
            }
            v63 = v55 - 2;
            if (v54 < 18 && v63 < 14)
            {
                v64 = (v63 * 18 + v54) * 8;
                if (!*((int *)(v64 + (char *)&g_10288fc4[0])) || *((int *)(v64 + (char *)&g_10288fc4[0])) == iter2)
                {
                    *((unsigned int *)(v64 + (char *)&g_10288fc4[0])) = iter2;
                    v65 = *((int *)(v64 + (char *)&g_10052785[0]));
                    if (!*((char *)&v36[2] + 1))
                    {
                        if (node >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return NULL;
                        }
                        v66 = 23 * node + (char *)g_10052774;
                        node += 1;
                        v66->field_0 = v54;
                        v66->field_2 = v63;
                        v66->field_4 = v36;
                        v66->field_c = v65;
                        v7 = v65;
                        v67 = v36[2];
                        if (!(char)v36[2])
                            v67 = 1;
                        v66->field_14 = v67;
                        v66->field_a = iter2;
                        if (v65 < 4294967294 && *((int *)&v36[1 + 3]) < 4294967294)
                            v66->field_10 = v65 + *((int *)&v36[1 + 3]);
                        v66->field_8 = v36[4];
                        *((char *)&v66[1].field_0) = 0;
                        v7 = v63;
                        v66->field_8 = v66->field_8 + (unsigned short)((8 - (unsigned short)v54 ^ 8 - (unsigned short)v54 >> 31) - (8 - (unsigned short)v54 >> 31));
                        v68 = v63;
                        v7 = v68;
                        v69 = (unsigned short)v68;
                        v66->field_8 = v66->field_8 + (unsigned short)((8 - v69 ^ 8 - v69 >> 31) - (8 - v69 >> 31));
                        v70 = v66->field_8;
                        if (v70 > v12)
                        {
                            v20 = v70;
                            v12 = v20;
                        }
                        v7 = v20;
                        v6 = v36;
                        v5 = v68;
                        v4 = v54;
                        v3 = &v8;
                        v2 = &v30;
                        v1 = v66;
                        v0 = v69;
                        *((char *)&v66[1].field_0) = 0;
                        if ((a0 - v54 ^ a0 - v54 >> 31) - (a0 - v54 >> 31) <= a2 && (a1 - v5 ^ a1 - v5 >> 31) - (a1 - v5 >> 31) <= a2)
                            *((char *)&v66[1].field_0) = 1;
                    }
                }
            }
        }
        if (g_10052784)
        {
            n = v23;
            for (v21 = v22; n < v21; n += 1)
            {
                v8 = n;
                v72 = 23 * n + (char *)g_10052774;
                v73 = v72->field_0 + 1;
                v74 = v72->field_2 - 1;
                if (v73 < 18 && v74 < 14)
                {
                    v75 = (v74 * 18 + v73) * 8;
                    if (!*((int *)(v75 + (char *)&g_10288fc4[0])) || *((int *)(v75 + (char *)&g_10288fc4[0])) == iter2 && node < 10000)
                    {
                        *((unsigned int *)(v75 + (char *)&g_10288fc4[0])) = iter2;
                        v76 = *((int *)(v75 + (char *)&g_10052785[0]));
                        if (!v72->field_15)
                        {
                            if (node >= 400000)
                            {
                                sub_10025172("Trace paths space exceeded!");
                                return NULL;
                            }
                            v77 = 23 * node + (char *)g_10052774;
                            node += 1;
                            v77->field_0 = v73;
                            v77->field_2 = v74;
                            v77->field_4 = v72;
                            v77->field_c = v76;
                            v7 = v76;
                            v78 = v72->field_14;
                            if (!v72->field_14)
                                v78 = 5;
                            v77->field_14 = v78;
                            v77->field_a = iter2;
                            if (v76 < 4294967294 && v72->field_10 < 4294967294)
                                v77->field_10 = v76 * 3 + v72->field_10;
                            v77->field_8 = v72->field_8;
                            v77->field_15 = 0;
                            v7 = v74;
                            v77->field_8 = v77->field_8 + (unsigned short)((8 - (unsigned short)v73 ^ 8 - (unsigned short)v73 >> 31) - (8 - (unsigned short)v73 >> 31));
                            v79 = v74;
                            v7 = v79;
                            v80 = (unsigned short)v79;
                            v77->field_8 = v77->field_8 + (unsigned short)((8 - v80 ^ 8 - v80 >> 31) - (8 - v80 >> 31));
                            v81 = v77->field_8;
                            if (v81 > v12)
                            {
                                v13 = v81;
                                v12 = v13;
                            }
                            v7 = v13;
                            v6 = v72;
                            v5 = v79;
                            v4 = v73;
                            v3 = &v8;
                            v2 = &v30;
                            v1 = v77;
                            v0 = v80;
                            v77->field_15 = 0;
                            if ((a0 - v73 ^ a0 - v73 >> 31) - (a0 - v73 >> 31) <= a2 && (a1 - v5 ^ a1 - v5 >> 31) - (a1 - v5 >> 31) <= a2)
                                v77->field_15 = 1;
                            v72 = v6;
                            v74 = v5;
                            v73 = v4;
                        }
                    }
                }
                v82 = v74 + 2;
                if (v73 < 18 && v82 < 14)
                {
                    v83 = (v82 * 18 + v73) * 8;
                    if (!*((int *)(v83 + (char *)&g_10288fc4[0])) || *((int *)(v83 + (char *)&g_10288fc4[0])) == iter2 && node < 10000)
                    {
                        *((unsigned int *)(v83 + (char *)&g_10288fc4[0])) = iter2;
                        v84 = *((int *)(v83 + (char *)&g_10052785[0]));
                        if (!v72->field_15)
                        {
                            if (node >= 400000)
                            {
                                sub_10025172("Trace paths space exceeded!");
                                return NULL;
                            }
                            v85 = 23 * node + (char *)g_10052774;
                            node += 1;
                            v85->field_0 = v73;
                            v85->field_2 = v82;
                            v85->field_4 = v72;
                            v85->field_c = v84;
                            v7 = v84;
                            v86 = v72->field_14;
                            if (!v72->field_14)
                                v86 = 6;
                            v85->field_14 = v86;
                            v85->field_a = iter2;
                            if (v84 < 4294967294 && v72->field_10 < 4294967294)
                                v85->field_10 = v84 * 3 + v72->field_10;
                            v85->field_8 = v72->field_8;
                            v85->field_15 = 0;
                            v7 = v82;
                            v85->field_8 = v85->field_8 + (unsigned short)((8 - (unsigned short)v73 ^ 8 - (unsigned short)v73 >> 31) - (8 - (unsigned short)v73 >> 31));
                            v87 = v82;
                            v7 = v87;
                            v88 = (unsigned short)v87;
                            v85->field_8 = v85->field_8 + (unsigned short)((8 - v88 ^ 8 - v88 >> 31) - (8 - v88 >> 31));
                            v89 = v85->field_8;
                            if (v89 > v12)
                            {
                                v14 = v89;
                                v12 = v14;
                            }
                            v7 = v14;
                            v6 = v72;
                            v5 = v87;
                            v4 = v73;
                            v3 = &v8;
                            v2 = &v30;
                            v1 = v85;
                            v0 = v88;
                            v85->field_15 = 0;
                            if ((a0 - v73 ^ a0 - v73 >> 31) - (a0 - v73 >> 31) <= a2 && (a1 - v5 ^ a1 - v5 >> 31) - (a1 - v5 >> 31) <= a2)
                                v85->field_15 = 1;
                            v72 = v6;
                            v82 = v5;
                            v73 = v4;
                        }
                    }
                }
                v90 = v73 - 2;
                if (v90 < 18 && v82 < 14)
                {
                    v91 = (v82 * 18 + v90) * 8;
                    if (!*((int *)(v91 + (char *)&g_10288fc4[0])) || *((int *)(v91 + (char *)&g_10288fc4[0])) == iter2 && node < 10000)
                    {
                        *((unsigned int *)(v91 + (char *)&g_10288fc4[0])) = iter2;
                        v92 = *((int *)(v91 + (char *)&g_10052785[0]));
                        if (!v72->field_15)
                        {
                            if (node >= 400000)
                            {
                                sub_10025172("Trace paths space exceeded!");
                                return NULL;
                            }
                            v93 = 23 * node + (char *)g_10052774;
                            node += 1;
                            v93->field_0 = v90;
                            v93->field_2 = v82;
                            v93->field_4 = v72;
                            v93->field_c = v92;
                            v7 = v92;
                            v94 = v72->field_14;
                            if (!v72->field_14)
                                v94 = 7;
                            v93->field_14 = v94;
                            v93->field_a = iter2;
                            if (v92 < 4294967294 && v72->field_10 < 4294967294)
                                v93->field_10 = v92 * 3 + v72->field_10;
                            v93->field_8 = v72->field_8;
                            v93->field_15 = 0;
                            v7 = v82;
                            v93->field_8 = v93->field_8 + (unsigned short)((8 - (unsigned short)v90 ^ 8 - (unsigned short)v90 >> 31) - (8 - (unsigned short)v90 >> 31));
                            v95 = v82;
                            v7 = v95;
                            v96 = (unsigned short)v95;
                            v93->field_8 = v93->field_8 + (unsigned short)((8 - v96 ^ 8 - v96 >> 31) - (8 - v96 >> 31));
                            v97 = v93->field_8;
                            if (v97 > v12)
                            {
                                v15 = v97;
                                v12 = v15;
                            }
                            v7 = v15;
                            v6 = v72;
                            v5 = v95;
                            v4 = v90;
                            v3 = &v8;
                            v2 = &v30;
                            v1 = v93;
                            v0 = v96;
                            v93->field_15 = 0;
                            if ((a0 - v90 ^ a0 - v90 >> 31) - (a0 - v90 >> 31) <= a2 && (a1 - v5 ^ a1 - v5 >> 31) - (a1 - v5 >> 31) <= a2)
                                v93->field_15 = 1;
                            v72 = v6;
                            v82 = v5;
                            v90 = v4;
                        }
                    }
                }
                v98 = v82 - 2;
                if (v90 < 18 && v98 < 14)
                {
                    v99 = (v98 * 18 + v90) * 8;
                    if (!*((int *)(v99 + (char *)&g_10288fc4[0])) || *((int *)(v99 + (char *)&g_10288fc4[0])) == iter2 && node < 10000)
                    {
                        *((unsigned int *)(v99 + (char *)&g_10288fc4[0])) = iter2;
                        v100 = *((int *)(v99 + (char *)&g_10052785[0]));
                        if (!v72->field_15)
                        {
                            if (node >= 400000)
                            {
                                sub_10025172("Trace paths space exceeded!");
                                return NULL;
                            }
                            v101 = 23 * node + (char *)g_10052774;
                            node += 1;
                            v101->field_0 = v90;
                            v101->field_2 = v98;
                            v101->field_4 = v72;
                            v101->field_c = v100;
                            v7 = v100;
                            v102 = v72->field_14;
                            if (!v72->field_14)
                                v102 = 8;
                            v101->field_14 = v102;
                            v101->field_a = iter2;
                            if (v100 < 4294967294 && v72->field_10 < 4294967294)
                                v101->field_10 = v100 * 3 + v72->field_10;
                            v101->field_8 = v72->field_8;
                            v101->field_15 = 0;
                            v7 = v98;
                            v101->field_8 = v101->field_8 + (unsigned short)((8 - (unsigned short)v90 ^ 8 - (unsigned short)v90 >> 31) - (8 - (unsigned short)v90 >> 31));
                            v103 = v98;
                            v7 = v103;
                            v104 = (unsigned short)v103;
                            v101->field_8 = v101->field_8 + (unsigned short)((8 - v104 ^ 8 - v104 >> 31) - (8 - v104 >> 31));
                            v105 = v101->field_8;
                            if (v105 > v12)
                            {
                                v16 = v105;
                                v12 = v16;
                            }
                            v7 = v16;
                            v6 = v72;
                            v5 = v103;
                            v4 = v90;
                            v3 = &v8;
                            v2 = &v30;
                            v1 = v101;
                            v0 = v104;
                            v101->field_15 = 0;
                            if ((a0 - v90 ^ a0 - v90 >> 31) - (a0 - v90 >> 31) <= a2 && (a1 - v5 ^ a1 - v5 >> 31) - (a1 - v5 >> 31) <= a2)
                                v101->field_15 = 1;
                        }
                    }
                }
            }
            v23 = v26;
            v22 = v24;
            v26 = v22;
            if (v22 != node)
            {
                iter2 += 1;
            }
            else if (v23 == v22)
            {
                break;
            }
            else
            {
                iter2 += 1;
            }
        }
        else
        {
            v26 = v24;
            if (v26 == node)
                break;
            else
                iter2 += 1;
        }
    }
    v106 = sub_1002ae81(&g_102897a4[0], 216);
    v11 = NULL;
    v9 = 0;
    v10 = 0;
    v107 = 23 * node + (char *)g_10052774;
    for (iter1 = g_10052774; iter1 < v107; iter1 = &iter1->field_17)
    {
        v6 = v107;
        if (iter1->padding_15[0])
        {
            v109 = iter1->field_a;
            v106 = 1000 * v109 * g_10053db2[v109];
            if (iter1->field_10)
            {
                v106 /= iter1->field_10;
                v110 = iter1->field_14;
                if (g_10052780 != 4294967295 && v110 == g_10052780)
                    v106 *= 2;
                if (v106 > v11)
                {
                    v11 = v106;
                    v10 = v110;
                    v110 = iter1->field_a;
                    v9 = v110;
                }
                v111 = v110 * 16;
                *((unsigned int *[4])(v111 + (char *)&g_102897a4[0])) = *((int *)(v111 + (char *)&g_102897a4[0])) + (char *)v106;
                *((unsigned int *)(v111 + (char *)&g_102897a8[0])) = *((int *)(v111 + (char *)&g_102897a8[0])) + 1;
                if (v106 > *((int *)(v111 + (char *)&g_102897ac[0])))
                    *((unsigned int *[4])(v111 + (char *)&g_102897ac[0])) = v106;
                v112 = iter1->field_a;
                if (v106 > g_102897e4[2 * v112])
                {
                    g_102897e4[2 * v112] = v106;
                    (&g_102897e8)[2 * v112] = iter1->field_14;
                }
            }
        }
        v107 = v6;
    }
    return v106;
}
```

## `sub_1000e8d8` `0x1000e8d8`

_39 bytes. (leaf/helper — see body)_

```c
typedef struct struct_0 {
    char padding_0[4];
    unsigned int field_4;
    unsigned short field_8;
    char padding_a[6];
    unsigned int field_10;
    char field_14;
    char field_15;
    char field_16;
} struct_0;

int sub_1000e8d8(void)
{
    struct_0 *idx;  // eax
    unsigned int v1;  // [bp+0xffff0]

    idx->field_10 = 0;
    idx->field_15 = 0;
    idx->field_4 = 0;
    idx->field_8 = 0;
    idx->field_14 = 0;
    idx->field_16 = 0;
    v1 = 1;
}
```

## `sub_1000f30d` `0x1000f30d`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1000f30d(void)
{
}
```

## `sub_1000f406` `0x1000f406`

_4 bytes. (leaf/helper — see body)_

```c
void sub_1000f406(void)
{
    return;
}
```

## `sub_1000f40a` `0x1000f40a`

_2976 bytes. refs "Trace paths space exceeded!", "Trace paths space exceeded!", "Trace paths space exceeded!"_

```c
typedef struct struct_0 {
    unsigned short field_0;
    unsigned short field_2;
    struct struct_1 *field_4;
    unsigned short field_8;
    unsigned short field_a;
    unsigned int field_c;
    unsigned int field_10;
    char field_14;
    char field_15;
} struct_0;

typedef struct struct_2 {
    unsigned short field_0;
    unsigned short field_2;
    struct struct_1 *field_4;
    unsigned short field_8;
    unsigned short field_a;
    unsigned int field_c;
    unsigned int field_10;
    char field_14;
} struct_2;

typedef struct struct_8 {
    unsigned short field_0;
    unsigned short field_2;
    char padding_4[4];
    unsigned short field_8;
    char padding_a[6];
    unsigned int field_10;
    char field_14;
    char field_15;
} struct_8;

typedef struct struct_17 {
    unsigned short field_0;
    unsigned short field_2;
    unsigned int field_4;
    unsigned short field_8;
    unsigned short field_a;
    char padding_c[4];
    unsigned int field_10;
    char field_14;
    char field_15;
    char field_16;
    char field_17;
} struct_17;

typedef struct struct_1 {
    unsigned short field_0;
    unsigned short field_2;
    char padding_4[4];
    unsigned short field_8;
} struct_1;

extern struct_17 *g_10052774;
extern unsigned int g_10052780;
extern char g_10052784;
extern unsigned int g_10052785[4];
extern unsigned int g_10053db2[4];
extern unsigned int g_10288fc4[4];
extern unsigned int g_10289364;
extern unsigned int g_102897a4[4];
extern unsigned int g_102897a8[4];
extern unsigned int g_102897ac[4];
extern unsigned int g_102897e4[4];
extern unsigned int g_102897e8;

unsigned int [4] sub_1000f40a(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int idx;  // ecx
    unsigned int m;  // ecx
    unsigned int v33;  // edi
    unsigned int v34;  // eax
    unsigned int v35;  // ebx
    unsigned int idx1;  // esi
    unsigned int v37;  // eax
    struct_2 *index;  // esi
    char v39;  // al
    unsigned int v40;  // edx
    unsigned int v41;  // edi
    unsigned int v42;  // eax
    unsigned short idx2[5];  // ecx
    unsigned int v43;  // ebx
    unsigned int v44;  // edx
    unsigned int v45;  // esi
    unsigned int v46;  // eax
    struct_2 *v47;  // esi
    char v48;  // al
    unsigned int v49;  // edx
    unsigned int v50;  // edi
    unsigned int v51;  // eax
    unsigned int v52;  // edx
    unsigned int v26;  // edx
    unsigned int v53;  // esi
    unsigned int v54;  // eax
    struct_2 *v55;  // esi
    char v56;  // al
    unsigned int v57;  // edx
    unsigned int v58;  // edi
    unsigned int v59;  // eax
    unsigned int n;  // ecx
    struct_8 *v61;  // ecx
    unsigned int v62;  // ebx
    unsigned int v27;  // ebx
    unsigned int v63;  // edx
    unsigned int v64;  // esi
    unsigned int v65;  // eax
    struct_0 *v66;  // esi
    char v67;  // al
    unsigned int v68;  // edx
    unsigned int v69;  // edi
    unsigned int v70;  // eax
    unsigned int v71;  // edx
    unsigned int v72;  // esi
    unsigned int v28;  // esi
    unsigned int v73;  // eax
    struct_0 *v74;  // esi
    char v75;  // al
    unsigned int v76;  // edx
    unsigned int v77;  // edi
    unsigned int v78;  // eax
    unsigned int v79;  // ebx
    unsigned int v80;  // esi
    unsigned int v81;  // eax
    struct_0 *v82;  // esi
    unsigned int v29;  // eax
    char v83;  // al
    unsigned int v84;  // edx
    unsigned int v85;  // edi
    unsigned int v86;  // eax
    unsigned int v87;  // edx
    unsigned int v88;  // esi
    unsigned int v89;  // eax
    struct_0 *v90;  // esi
    char v91;  // al
    unsigned int v92;  // edx
    struct_0 *v30;  // esi
    unsigned int v93;  // edi
    unsigned int v94;  // eax
    unsigned int v95[4];  // eax
    unsigned int v96;  // ecx
    struct_17 *node;  // ebx
    unsigned int v98;  // ecx
    unsigned int v99;  // ecx
    unsigned int v100;  // ecx
    unsigned int v101;  // ecx
    char v31;  // al
    unsigned int v32;  // edx
    unsigned int v0;  // [bp-0x9c]
    struct_2 *v1;  // [bp-0x98], Other Possible Types: struct_0 *
    char *v2;  // [bp-0x94]
    char *v3;  // [bp-0x90]
    unsigned int v4;  // [bp-0x8c]
    unsigned int v5;  // [bp-0x88]
    struct_8 *v6;  // [bp-0x84], Other Possible Types: unsigned short [5], unsigned int
    unsigned int v7;  // [bp-0x80]
    unsigned int v8;  // [bp-0x7c]
    unsigned int v9;  // [bp-0x78]
    unsigned int v10;  // [bp-0x74]
    unsigned int v11[4];  // [bp-0x70]
    unsigned int v12;  // [bp-0x2c]
    unsigned int v13;  // [bp-0x28]
    unsigned int v14;  // [bp-0x24]
    unsigned int v15;  // [bp-0x20]
    unsigned int v16;  // [bp-0x1c]
    unsigned int iter1;  // [bp-0x18]
    unsigned int v18;  // [bp-0x14]
    unsigned int iter;  // [bp-0x10]
    unsigned int iter2;  // [bp-0xc]
    unsigned int i;  // [bp-0x8]
    char v22;  // [bp-0x4]

    v12 = 0;
    for (i = 0; i < 14; i += 1)
    {
        iter2 = 0;
        while (iter2 < 18)
        {
            idx = (i * 18 + iter2) * 8;
            *((unsigned int *)(idx + (char *)&g_10288fc4[0])) = 0;
            if (*((int *)(idx + (char *)&g_10052785[0])) >= 4294967294)
            {
                *((unsigned int *)(idx + (char *)&g_10288fc4[0])) = 4294967295;
                iter2 += 1;
            }
            else
            {
                iter2 += 1;
            }
        }
    }
    g_10052774->field_0 = 8;
    g_10052774->field_2 = 6;
    g_10289364 = 1;
    g_10052774->field_10 = 0;
    g_10052774->field_15 = 0;
    g_10052774->field_4 = 0;
    g_10052774->field_8 = 0;
    g_10052774->field_14 = 0;
    g_10052774->field_16 = 0;
    iter1 = 1;
    v18 = 0;
    v15 = 0;
    v14 = 0;
    v13 = 0;
    iter = 1;
    while (iter < 18)
    {
        m = v18;
        for (v16 = iter1; m < v16; m += 1)
        {
            v8 = m;
            idx2 = 23 * m + (char *)g_10052774;
            v26 = idx2[1];
            v27 = idx2[0] + 1;
            if (v27 < 18 && v26 < 14)
            {
                v28 = (v26 * 18 + v27) * 8;
                if (!*((int *)(v28 + (char *)&g_10288fc4[0])) || *((int *)(v28 + (char *)&g_10288fc4[0])) == iter)
                {
                    *((unsigned int *)(v28 + (char *)&g_10288fc4[0])) = iter;
                    v29 = *((int *)(v28 + (char *)&g_10052785[0]));
                    if (!*((char *)&idx2[2] + 1))
                    {
                        if (iter1 >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return NULL;
                        }
                        v30 = 23 * iter1 + (char *)g_10052774;
                        iter1 += 1;
                        v30->field_0 = v27;
                        v30->field_2 = v26;
                        v30->field_4 = idx2;
                        v30->field_c = v29;
                        v7 = v29;
                        v31 = idx2[2];
                        if (!(char)idx2[2])
                            v31 = 2;
                        v30->field_14 = v31;
                        v30->field_a = iter;
                        if (v29 < 4294967294 && *((int *)&idx2[1 + 3]) < 4294967294)
                            v30->field_10 = v29 + *((int *)&idx2[1 + 3]);
                        v30->field_8 = idx2[4];
                        v30->field_15 = 0;
                        v7 = v26;
                        v30->field_8 = v30->field_8 + (unsigned short)((8 - (unsigned short)v27 ^ 8 - (unsigned short)v27 >> 31) - (8 - (unsigned short)v27 >> 31));
                        v32 = v26;
                        v7 = v32;
                        v33 = (unsigned short)v32;
                        v30->field_8 = v30->field_8 + (unsigned short)((8 - v33 ^ 8 - v33 >> 31) - (8 - v33 >> 31));
                        v34 = v30->field_8;
                        if (v34 > v12)
                            v12 = v34;
                        v7 = v12;
                        v6 = idx2;
                        v5 = v32;
                        v4 = v27;
                        v3 = &v8;
                        v2 = &v22;
                        v1 = v30;
                        v0 = v33;
                        v30->field_15 = 0;
                        if ((a0 - v27 ^ a0 - v27 >> 31) - (a0 - v27 >> 31) <= a2 && (a1 - v5 ^ a1 - v5 >> 31) - (a1 - v5 >> 31) <= a2)
                            v30->field_15 = 1;
                        idx2 = v6;
                        v26 = v5;
                        v27 = v4;
                    }
                }
            }
            v35 = v27 - 2;
            if (v35 < 18 && v26 < 14)
            {
                idx1 = (v26 * 18 + v35) * 8;
                if (!*((int *)(idx1 + (char *)&g_10288fc4[0])) || *((int *)(idx1 + (char *)&g_10288fc4[0])) == iter)
                {
                    *((unsigned int *)(idx1 + (char *)&g_10288fc4[0])) = iter;
                    v37 = *((int *)(idx1 + (char *)&g_10052785[0]));
                    if (!*((char *)&idx2[2] + 1))
                    {
                        if (iter1 >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return NULL;
                        }
                        index = 23 * iter1 + (char *)g_10052774;
                        iter1 += 1;
                        index->field_0 = v35;
                        index->field_2 = v26;
                        index->field_4 = idx2;
                        index->field_c = v37;
                        v7 = v37;
                        v39 = idx2[2];
                        if (!(char)idx2[2])
                            v39 = 4;
                        index->field_14 = v39;
                        index->field_a = iter;
                        if (v37 < 4294967294 && *((int *)&idx2[1 + 3]) < 4294967294)
                            index->field_10 = v37 + *((int *)&idx2[1 + 3]);
                        index->field_8 = idx2[4];
                        *((char *)&index[1].field_0) = 0;
                        v7 = v26;
                        index->field_8 = index->field_8 + (unsigned short)((8 - (unsigned short)v35 ^ 8 - (unsigned short)v35 >> 31) - (8 - (unsigned short)v35 >> 31));
                        v40 = v26;
                        v7 = v40;
                        v41 = (unsigned short)v40;
                        index->field_8 = index->field_8 + (unsigned short)((8 - v41 ^ 8 - v41 >> 31) - (8 - v41 >> 31));
                        v42 = index->field_8;
                        if (v42 > v12)
                            v12 = v42;
                        v7 = v12;
                        v6 = idx2;
                        v5 = v40;
                        v4 = v35;
                        v3 = &v8;
                        v2 = &v22;
                        v1 = index;
                        v0 = v41;
                        *((char *)&index[1].field_0) = 0;
                        if ((a0 - v35 ^ a0 - v35 >> 31) - (a0 - v35 >> 31) <= a2 && (a1 - v5 ^ a1 - v5 >> 31) - (a1 - v5 >> 31) <= a2)
                            *((char *)&index[1].field_0) = 1;
                        idx2 = v6;
                        v26 = v5;
                        v35 = v4;
                    }
                }
            }
            v43 = v35 + 1;
            v44 = v26 + 1;
            if (v43 < 18 && v44 < 14)
            {
                v45 = (v44 * 18 + v43) * 8;
                if (!*((int *)(v45 + (char *)&g_10288fc4[0])) || *((int *)(v45 + (char *)&g_10288fc4[0])) == iter)
                {
                    *((unsigned int *)(v45 + (char *)&g_10288fc4[0])) = iter;
                    v46 = *((int *)(v45 + (char *)&g_10052785[0]));
                    if (!*((char *)&idx2[2] + 1))
                    {
                        if (iter1 >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return NULL;
                        }
                        v47 = 23 * iter1 + (char *)g_10052774;
                        iter1 += 1;
                        v47->field_0 = v43;
                        v47->field_2 = v44;
                        v47->field_4 = idx2;
                        v47->field_c = v46;
                        v7 = v46;
                        v48 = idx2[2];
                        if (!(char)idx2[2])
                            v48 = 3;
                        v47->field_14 = v48;
                        v47->field_a = iter;
                        if (v46 < 4294967294 && *((int *)&idx2[1 + 3]) < 4294967294)
                            v47->field_10 = v46 + *((int *)&idx2[1 + 3]);
                        v47->field_8 = idx2[4];
                        *((char *)&v47[1].field_0) = 0;
                        v7 = v44;
                        v47->field_8 = v47->field_8 + (unsigned short)((8 - (unsigned short)v43 ^ 8 - (unsigned short)v43 >> 31) - (8 - (unsigned short)v43 >> 31));
                        v49 = v44;
                        v7 = v49;
                        v50 = (unsigned short)v49;
                        v47->field_8 = v47->field_8 + (unsigned short)((8 - v50 ^ 8 - v50 >> 31) - (8 - v50 >> 31));
                        v51 = v47->field_8;
                        if (v51 > v12)
                            v12 = v51;
                        v7 = v12;
                        v6 = idx2;
                        v5 = v49;
                        v4 = v43;
                        v3 = &v8;
                        v2 = &v22;
                        v1 = v47;
                        v0 = v50;
                        *((char *)&v47[1].field_0) = 0;
                        if ((a0 - v43 ^ a0 - v43 >> 31) - (a0 - v43 >> 31) <= a2 && (a1 - v5 ^ a1 - v5 >> 31) - (a1 - v5 >> 31) <= a2)
                            *((char *)&v47[1].field_0) = 1;
                        idx2 = v6;
                        v44 = v5;
                        v43 = v4;
                    }
                }
            }
            v52 = v44 - 2;
            if (v43 < 18 && v52 < 14)
            {
                v53 = (v52 * 18 + v43) * 8;
                if (!*((int *)(v53 + (char *)&g_10288fc4[0])) || *((int *)(v53 + (char *)&g_10288fc4[0])) == iter)
                {
                    *((unsigned int *)(v53 + (char *)&g_10288fc4[0])) = iter;
                    v54 = *((int *)(v53 + (char *)&g_10052785[0]));
                    if (!*((char *)&idx2[2] + 1))
                    {
                        if (iter1 >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return NULL;
                        }
                        v55 = 23 * iter1 + (char *)g_10052774;
                        iter1 += 1;
                        v55->field_0 = v43;
                        v55->field_2 = v52;
                        v55->field_4 = idx2;
                        v55->field_c = v54;
                        v7 = v54;
                        v56 = idx2[2];
                        if (!(char)idx2[2])
                            v56 = 1;
                        v55->field_14 = v56;
                        v55->field_a = iter;
                        if (v54 < 4294967294 && *((int *)&idx2[1 + 3]) < 4294967294)
                            v55->field_10 = v54 + *((int *)&idx2[1 + 3]);
                        v55->field_8 = idx2[4];
                        *((char *)&v55[1].field_0) = 0;
                        v7 = v52;
                        v55->field_8 = v55->field_8 + (unsigned short)((8 - (unsigned short)v43 ^ 8 - (unsigned short)v43 >> 31) - (8 - (unsigned short)v43 >> 31));
                        v57 = v52;
                        v7 = v57;
                        v58 = (unsigned short)v57;
                        v55->field_8 = v55->field_8 + (unsigned short)((8 - v58 ^ 8 - v58 >> 31) - (8 - v58 >> 31));
                        v59 = v55->field_8;
                        if (v59 > v12)
                            v12 = v59;
                        v7 = v12;
                        v6 = idx2;
                        v5 = v57;
                        v4 = v43;
                        v3 = &v8;
                        v2 = &v22;
                        v1 = v55;
                        v0 = v58;
                        *((char *)&v55[1].field_0) = 0;
                        if ((a0 - v43 ^ a0 - v43 >> 31) - (a0 - v43 >> 31) <= a2 && (a1 - v5 ^ a1 - v5 >> 31) - (a1 - v5 >> 31) <= a2)
                            *((char *)&v55[1].field_0) = 1;
                    }
                }
            }
        }
        if (g_10052784)
        {
            n = v15;
            for (v13 = v14; n < v13; n += 1)
            {
                v8 = n;
                v61 = 23 * n + (char *)g_10052774;
                v62 = v61->field_0 + 1;
                v63 = v61->field_2 - 1;
                if (v62 < 18 && v63 < 14)
                {
                    v64 = (v63 * 18 + v62) * 8;
                    if (!*((int *)(v64 + (char *)&g_10288fc4[0])) || *((int *)(v64 + (char *)&g_10288fc4[0])) == iter && iter1 < 10000)
                    {
                        *((unsigned int *)(v64 + (char *)&g_10288fc4[0])) = iter;
                        v65 = *((int *)(v64 + (char *)&g_10052785[0]));
                        if (!v61->field_15)
                        {
                            if (iter1 >= 400000)
                            {
                                sub_10025172("Trace paths space exceeded!");
                                return NULL;
                            }
                            v66 = 23 * iter1 + (char *)g_10052774;
                            iter1 += 1;
                            v66->field_0 = v62;
                            v66->field_2 = v63;
                            v66->field_4 = v61;
                            v66->field_c = v65;
                            v7 = v65;
                            v67 = v61->field_14;
                            if (!v61->field_14)
                                v67 = 5;
                            v66->field_14 = v67;
                            v66->field_a = iter;
                            if (v65 < 4294967294 && v61->field_10 < 4294967294)
                                v66->field_10 = v65 * 3 + v61->field_10;
                            v66->field_8 = v61->field_8;
                            v66->field_15 = 0;
                            v7 = v63;
                            v66->field_8 = v66->field_8 + (unsigned short)((8 - (unsigned short)v62 ^ 8 - (unsigned short)v62 >> 31) - (8 - (unsigned short)v62 >> 31));
                            v68 = v63;
                            v7 = v68;
                            v69 = (unsigned short)v68;
                            v66->field_8 = v66->field_8 + (unsigned short)((8 - v69 ^ 8 - v69 >> 31) - (8 - v69 >> 31));
                            v70 = v66->field_8;
                            if (v70 > v12)
                                v12 = v70;
                            v7 = v12;
                            v6 = v61;
                            v5 = v68;
                            v4 = v62;
                            v3 = &v8;
                            v2 = &v22;
                            v1 = v66;
                            v0 = v69;
                            v66->field_15 = 0;
                            if ((a0 - v62 ^ a0 - v62 >> 31) - (a0 - v62 >> 31) <= a2 && (a1 - v5 ^ a1 - v5 >> 31) - (a1 - v5 >> 31) <= a2)
                                v66->field_15 = 1;
                            v61 = v6;
                            v63 = v5;
                            v62 = v4;
                        }
                    }
                }
                v71 = v63 + 2;
                if (v62 < 18 && v71 < 14)
                {
                    v72 = (v71 * 18 + v62) * 8;
                    if (!*((int *)(v72 + (char *)&g_10288fc4[0])) || *((int *)(v72 + (char *)&g_10288fc4[0])) == iter && iter1 < 10000)
                    {
                        *((unsigned int *)(v72 + (char *)&g_10288fc4[0])) = iter;
                        v73 = *((int *)(v72 + (char *)&g_10052785[0]));
                        if (!v61->field_15)
                        {
                            if (iter1 >= 400000)
                            {
                                sub_10025172("Trace paths space exceeded!");
                                return NULL;
                            }
                            v74 = 23 * iter1 + (char *)g_10052774;
                            iter1 += 1;
                            v74->field_0 = v62;
                            v74->field_2 = v71;
                            v74->field_4 = v61;
                            v74->field_c = v73;
                            v7 = v73;
                            v75 = v61->field_14;
                            if (!v61->field_14)
                                v75 = 6;
                            v74->field_14 = v75;
                            v74->field_a = iter;
                            if (v73 < 4294967294 && v61->field_10 < 4294967294)
                                v74->field_10 = v73 * 3 + v61->field_10;
                            v74->field_8 = v61->field_8;
                            v74->field_15 = 0;
                            v7 = v71;
                            v74->field_8 = v74->field_8 + (unsigned short)((8 - (unsigned short)v62 ^ 8 - (unsigned short)v62 >> 31) - (8 - (unsigned short)v62 >> 31));
                            v76 = v71;
                            v7 = v76;
                            v77 = (unsigned short)v76;
                            v74->field_8 = v74->field_8 + (unsigned short)((8 - v77 ^ 8 - v77 >> 31) - (8 - v77 >> 31));
                            v78 = v74->field_8;
                            if (v78 > v12)
                                v12 = v78;
                            v7 = v12;
                            v6 = v61;
                            v5 = v76;
                            v4 = v62;
                            v3 = &v8;
                            v2 = &v22;
                            v1 = v74;
                            v0 = v77;
                            v74->field_15 = 0;
                            if ((a0 - v62 ^ a0 - v62 >> 31) - (a0 - v62 >> 31) <= a2 && (a1 - v5 ^ a1 - v5 >> 31) - (a1 - v5 >> 31) <= a2)
                                v74->field_15 = 1;
                            v61 = v6;
                            v71 = v5;
                            v62 = v4;
                        }
                    }
                }
                v79 = v62 - 2;
                if (v79 < 18 && v71 < 14)
                {
                    v80 = (v71 * 18 + v79) * 8;
                    if (!*((int *)(v80 + (char *)&g_10288fc4[0])) || *((int *)(v80 + (char *)&g_10288fc4[0])) == iter && iter1 < 10000)
                    {
                        *((unsigned int *)(v80 + (char *)&g_10288fc4[0])) = iter;
                        v81 = *((int *)(v80 + (char *)&g_10052785[0]));
                        if (!v61->field_15)
                        {
                            if (iter1 >= 400000)
                            {
                                sub_10025172("Trace paths space exceeded!");
                                return NULL;
                            }
                            v82 = 23 * iter1 + (char *)g_10052774;
                            iter1 += 1;
                            v82->field_0 = v79;
                            v82->field_2 = v71;
                            v82->field_4 = v61;
                            v82->field_c = v81;
                            v7 = v81;
                            v83 = v61->field_14;
                            if (!v61->field_14)
                                v83 = 7;
                            v82->field_14 = v83;
                            v82->field_a = iter;
                            if (v81 < 4294967294 && v61->field_10 < 4294967294)
                                v82->field_10 = v81 * 3 + v61->field_10;
                            v82->field_8 = v61->field_8;
                            v82->field_15 = 0;
                            v7 = v71;
                            v82->field_8 = v82->field_8 + (unsigned short)((8 - (unsigned short)v79 ^ 8 - (unsigned short)v79 >> 31) - (8 - (unsigned short)v79 >> 31));
                            v84 = v71;
                            v7 = v84;
                            v85 = (unsigned short)v84;
                            v82->field_8 = v82->field_8 + (unsigned short)((8 - v85 ^ 8 - v85 >> 31) - (8 - v85 >> 31));
                            v86 = v82->field_8;
                            if (v86 > v12)
                                v12 = v86;
                            v7 = v12;
                            v6 = v61;
                            v5 = v84;
                            v4 = v79;
                            v3 = &v8;
                            v2 = &v22;
                            v1 = v82;
                            v0 = v85;
                            v82->field_15 = 0;
                            if ((a0 - v79 ^ a0 - v79 >> 31) - (a0 - v79 >> 31) <= a2 && (a1 - v5 ^ a1 - v5 >> 31) - (a1 - v5 >> 31) <= a2)
                                v82->field_15 = 1;
                            v61 = v6;
                            v71 = v5;
                            v79 = v4;
                        }
                    }
                }
                v87 = v71 - 2;
                if (v79 < 18 && v87 < 14)
                {
                    v88 = (v87 * 18 + v79) * 8;
                    if (!*((int *)(v88 + (char *)&g_10288fc4[0])) || *((int *)(v88 + (char *)&g_10288fc4[0])) == iter && iter1 < 10000)
                    {
                        *((unsigned int *)(v88 + (char *)&g_10288fc4[0])) = iter;
                        v89 = *((int *)(v88 + (char *)&g_10052785[0]));
                        if (!v61->field_15)
                        {
                            if (iter1 >= 400000)
                            {
                                sub_10025172("Trace paths space exceeded!");
                                return NULL;
                            }
                            v90 = 23 * iter1 + (char *)g_10052774;
                            iter1 += 1;
                            v90->field_0 = v79;
                            v90->field_2 = v87;
                            v90->field_4 = v61;
                            v90->field_c = v89;
                            v7 = v89;
                            v91 = v61->field_14;
                            if (!v61->field_14)
                                v91 = 8;
                            v90->field_14 = v91;
                            v90->field_a = iter;
                            if (v89 < 4294967294 && v61->field_10 < 4294967294)
                                v90->field_10 = v89 * 3 + v61->field_10;
                            v90->field_8 = v61->field_8;
                            v90->field_15 = 0;
                            v7 = v87;
                            v90->field_8 = v90->field_8 + (unsigned short)((8 - (unsigned short)v79 ^ 8 - (unsigned short)v79 >> 31) - (8 - (unsigned short)v79 >> 31));
                            v92 = v87;
                            v7 = v92;
                            v93 = (unsigned short)v92;
                            v90->field_8 = v90->field_8 + (unsigned short)((8 - v93 ^ 8 - v93 >> 31) - (8 - v93 >> 31));
                            v94 = v90->field_8;
                            if (v94 > v12)
                                v12 = v94;
                            v7 = v12;
                            v6 = v61;
                            v5 = v92;
                            v4 = v79;
                            v3 = &v8;
                            v2 = &v22;
                            v1 = v90;
                            v0 = v93;
                            v90->field_15 = 0;
                            if ((a0 - v79 ^ a0 - v79 >> 31) - (a0 - v79 >> 31) <= a2 && (a1 - v5 ^ a1 - v5 >> 31) - (a1 - v5 >> 31) <= a2)
                                v90->field_15 = 1;
                        }
                    }
                }
            }
            v15 = v18;
            v14 = v16;
            v18 = v14;
            if (v14 != iter1)
            {
                iter += 1;
            }
            else if (v15 == v14)
            {
                break;
            }
            else
            {
                iter += 1;
            }
        }
        else
        {
            v18 = v16;
            if (v18 == iter1)
                break;
            else
                iter += 1;
        }
    }
    v95 = sub_1002ae81(&g_102897a4[0], 216);
    v11 = NULL;
    v9 = 0;
    v10 = 0;
    v96 = 23 * iter1 + (char *)g_10052774;
    for (node = g_10052774; node < v96; node = &node->field_17)
    {
        v6 = v96;
        if (node->field_15)
        {
            v98 = node->field_a;
            v95 = 1000 * v98 * g_10053db2[v98];
            if (node->field_10)
            {
                v95 /= node->field_10;
                v99 = node->field_14;
                if (g_10052780 != 4294967295 && v99 == g_10052780)
                    v95 *= 2;
                if (v95 > v11)
                {
                    v11 = v95;
                    v10 = v99;
                    v99 = node->field_a;
                    v9 = v99;
                }
                v100 = v99 * 16;
                *((unsigned int *[4])(v100 + (char *)&g_102897a4[0])) = *((int *)(v100 + (char *)&g_102897a4[0])) + (char *)v95;
                *((unsigned int *)(v100 + (char *)&g_102897a8[0])) = *((int *)(v100 + (char *)&g_102897a8[0])) + 1;
                if (v95 > *((int *)(v100 + (char *)&g_102897ac[0])))
                    *((unsigned int *[4])(v100 + (char *)&g_102897ac[0])) = v95;
                v101 = node->field_a;
                if (v95 > g_102897e4[2 * v101])
                {
                    g_102897e4[2 * v101] = v95;
                    (&g_102897e8)[2 * v101] = node->field_14;
                }
            }
        }
        v96 = v6;
    }
    return v95;
}
```

## `sub_1000feb3` `0x1000feb3`

_2 bytes. (leaf/helper — see body)_

```c
void sub_1000feb3(void)
{
}
```

## `sub_1000ffac` `0x1000ffac`

_4 bytes. (leaf/helper — see body)_

```c
void sub_1000ffac(void)
{
    return;
}
```

## `sub_1000ffb0` `0x1000ffb0`

_2874 bytes. refs "Trace paths space exceeded!", "Trace paths space exceeded!", "Trace paths space exceeded!"_

```c
typedef struct struct_0 {
    unsigned short field_0;
    unsigned short field_2;
    struct struct_1 *field_4;
    unsigned short field_8;
    unsigned short field_a;
    unsigned int field_c;
    unsigned int field_10;
    char field_14;
    char field_15;
} struct_0;

typedef struct struct_2 {
    unsigned short field_0;
    unsigned short field_2;
    struct struct_1 *field_4;
    unsigned short field_8;
    unsigned short field_a;
    unsigned int field_c;
    unsigned int field_10;
    char field_14;
} struct_2;

typedef struct struct_8 {
    unsigned short field_0;
    unsigned short field_2;
    char padding_4[4];
    unsigned short field_8;
    char padding_a[6];
    unsigned int field_10;
    char field_14;
} struct_8;

typedef struct struct_17 {
    unsigned short field_0;
    unsigned short field_2;
    char padding_4[6];
    unsigned short field_a;
    unsigned int field_c;
    unsigned int field_10;
    char field_14;
    char field_15;
    char padding_16[1];
    char field_17;
} struct_17;

typedef struct struct_1 {
    unsigned short field_0;
    unsigned short field_2;
    char padding_4[4];
    unsigned short field_8;
} struct_1;

extern struct_17 *g_10052774;
extern char g_10052784;
extern unsigned int g_10052785[4];
extern unsigned int g_10052b25;
extern unsigned int g_10288fc4[4];
extern unsigned int g_10289364;
extern int g_102897a4;

unsigned int sub_1000ffb0(unsigned int a0, unsigned int a1, unsigned int a2)
{
    unsigned int idx;  // ecx
    unsigned int m;  // ecx
    unsigned int v38;  // edi
    unsigned int v39;  // eax
    unsigned int v40;  // ebx
    unsigned int idx1;  // esi
    unsigned int v42;  // eax
    struct_2 *index;  // esi
    char v44;  // al
    unsigned int v45;  // edx
    unsigned int v46;  // edi
    unsigned int v47;  // eax
    unsigned short idx2[5];  // ecx
    unsigned int v48;  // ebx
    unsigned int v49;  // edx
    unsigned int v50;  // esi
    unsigned int v51;  // eax
    struct_2 *v52;  // esi
    char v53;  // al
    unsigned int v54;  // edx
    unsigned int v55;  // edi
    unsigned int v56;  // eax
    unsigned int v57;  // edx
    unsigned int v31;  // edx
    unsigned int v58;  // esi
    unsigned int v59;  // eax
    struct_2 *v60;  // esi
    char v61;  // al
    unsigned int v62;  // edx
    unsigned int v63;  // edi
    unsigned int v64;  // eax
    unsigned int n;  // ecx
    struct_8 *v66;  // ecx
    unsigned int v67;  // ebx
    unsigned int v32;  // ebx
    unsigned int v68;  // edx
    unsigned int v69;  // esi
    unsigned int v70;  // eax
    struct_0 *v71;  // esi
    char v72;  // al
    unsigned int v73;  // edx
    unsigned int v74;  // edi
    unsigned int v75;  // eax
    unsigned int v76;  // edx
    unsigned int v77;  // esi
    unsigned int v33;  // esi
    unsigned int v78;  // eax
    struct_0 *v79;  // esi
    char v80;  // al
    unsigned int v81;  // edx
    unsigned int v82;  // edi
    unsigned int v83;  // eax
    unsigned int v84;  // ebx
    unsigned int v85;  // esi
    unsigned int v86;  // eax
    struct_0 *v87;  // esi
    unsigned int v34;  // eax
    char v88;  // al
    unsigned int v89;  // edx
    unsigned int v90;  // edi
    unsigned int v91;  // eax
    unsigned int v92;  // edx
    unsigned int v93;  // esi
    unsigned int v94;  // eax
    struct_0 *v95;  // esi
    char v96;  // al
    unsigned int v97;  // edx
    struct_0 *v35;  // esi
    unsigned int v98;  // edi
    unsigned int v99;  // eax
    unsigned int v100;  // eax
    unsigned int v101;  // ecx
    struct_17 *node;  // ebx
    char v36;  // al
    unsigned int v37;  // edx
    unsigned int v0;  // [bp-0xa4]
    struct_2 *v1;  // [bp-0xa0], Other Possible Types: struct_0 *
    char *v2;  // [bp-0x9c]
    char *v3;  // [bp-0x98]
    unsigned int v4;  // [bp-0x94]
    unsigned int v5;  // [bp-0x90]
    struct_8 *v6;  // [bp-0x8c], Other Possible Types: unsigned short [5], unsigned int
    unsigned int v7;  // [bp-0x88]
    unsigned int v8;  // [bp-0x84]
    unsigned int v9;  // [bp-0x80]
    unsigned int v10;  // [bp-0x80]
    unsigned int v11;  // [bp-0x80]
    unsigned int v12;  // [bp-0x7c]
    unsigned int v13;  // [bp-0x78]
    unsigned int v14;  // [bp-0x78]
    unsigned int v15;  // [bp-0x74]
    unsigned int v16;  // [bp-0x70]
    unsigned int v17;  // [bp-0x2c]
    unsigned int v18;  // [bp-0x28]
    unsigned int v19;  // [bp-0x24]
    unsigned int v20;  // [bp-0x20]
    unsigned int v21;  // [bp-0x1c]
    unsigned int iter1;  // [bp-0x18]
    unsigned int v23;  // [bp-0x14]
    unsigned int iter;  // [bp-0x10]
    unsigned int iter2;  // [bp-0xc]
    unsigned int i;  // [bp-0x8]
    char v27;  // [bp-0x4]

    v17 = 0;
    for (i = 0; i < 14; i += 1)
    {
        iter2 = 0;
        while (iter2 < 18)
        {
            idx = (i * 18 + iter2) * 8;
            *((unsigned int *)(idx + (char *)&g_10288fc4[0])) = 0;
            if (*((int *)(idx + (char *)&g_10052785[0])) >= 4294967294)
            {
                *((unsigned int *)(idx + (char *)&g_10288fc4[0])) = 4294967295;
                iter2 += 1;
            }
            else
            {
                iter2 += 1;
            }
        }
    }
    g_10052774->field_0 = 8;
    g_10052774->field_2 = 6;
    g_10289364 = 1;
    if (a0 - 7 <= 2 && a1 - 5 <= 2)
    {
        g_10052774->field_c = g_10052b25;
        g_10052774->field_10 = g_10052b25;
        g_10052774->field_15 = 1;
    }
    else
    {
        g_10052774->field_10 = 0;
        g_10052774->field_15 = 0;
    }
    *((unsigned int *)&g_10052774->padding_4[0]) = 0;
    *((unsigned short *)&g_10052774->padding_4[4]) = 0;
    g_10052774->field_14 = 0;
    g_10052774->padding_16[0] = 0;
    iter1 = 1;
    v23 = 0;
    v20 = 0;
    v19 = 0;
    v18 = 0;
    iter = 1;
    while (iter < 18)
    {
        m = v23;
        for (v21 = iter1; m < v21; m += 1)
        {
            v8 = m;
            idx2 = 23 * m + (char *)g_10052774;
            v31 = idx2[1];
            v32 = idx2[0] + 1;
            if (v32 < 18 && v31 < 14)
            {
                v33 = (v31 * 18 + v32) * 8;
                if (!*((int *)(v33 + (char *)&g_10288fc4[0])) || *((int *)(v33 + (char *)&g_10288fc4[0])) == iter)
                {
                    *((unsigned int *)(v33 + (char *)&g_10288fc4[0])) = iter;
                    v34 = *((int *)(v33 + (char *)&g_10052785[0]));
                    if (iter1 >= 400000)
                    {
                        sub_10025172("Trace paths space exceeded!");
                        return 0;
                    }
                    v35 = 23 * iter1 + (char *)g_10052774;
                    iter1 += 1;
                    v35->field_0 = v32;
                    v35->field_2 = v31;
                    v35->field_4 = idx2;
                    v35->field_c = v34;
                    v7 = v34;
                    v36 = idx2[2];
                    if (!(char)idx2[2])
                        v36 = 2;
                    v35->field_14 = v36;
                    v35->field_a = iter;
                    if (v7 < 4294967294 && *((int *)&idx2[1 + 3]) < 4294967294)
                        v35->field_10 = v7 + *((int *)&idx2[1 + 3]);
                    v35->field_8 = idx2[4];
                    v35->field_15 = 0;
                    v7 = v31;
                    v35->field_8 = v35->field_8 + (unsigned short)((8 - (unsigned short)v32 ^ 8 - (unsigned short)v32 >> 31) - (8 - (unsigned short)v32 >> 31));
                    v37 = v31;
                    v7 = v37;
                    v38 = (unsigned short)v37;
                    v35->field_8 = v35->field_8 + (unsigned short)((8 - v38 ^ 8 - v38 >> 31) - (8 - v38 >> 31));
                    v39 = v35->field_8;
                    if (v39 > v17)
                        v17 = v39;
                    v7 = v17;
                    v6 = idx2;
                    v5 = v37;
                    v4 = v32;
                    v3 = &v8;
                    v2 = &v27;
                    v1 = v35;
                    v0 = v38;
                    v35->field_15 = 0;
                    if ((a0 - v32 ^ a0 - v32 >> 31) - (a0 - v32 >> 31) <= a2 && (a1 - v5 ^ a1 - v5 >> 31) - (a1 - v5 >> 31) <= a2)
                        v35->field_15 = 1;
                    idx2 = v6;
                    v31 = v5;
                    v32 = v4;
                }
            }
            v40 = v32 - 2;
            if (v40 < 18 && v31 < 14)
            {
                idx1 = (v31 * 18 + v40) * 8;
                if (!*((int *)(idx1 + (char *)&g_10288fc4[0])) || *((int *)(idx1 + (char *)&g_10288fc4[0])) == iter)
                {
                    *((unsigned int *)(idx1 + (char *)&g_10288fc4[0])) = iter;
                    v42 = *((int *)(idx1 + (char *)&g_10052785[0]));
                    if (iter1 >= 400000)
                    {
                        sub_10025172("Trace paths space exceeded!");
                        return 0;
                    }
                    index = 23 * iter1 + (char *)g_10052774;
                    iter1 += 1;
                    index->field_0 = v40;
                    index->field_2 = v31;
                    index->field_4 = idx2;
                    index->field_c = v42;
                    v7 = v42;
                    v44 = idx2[2];
                    if (!(char)idx2[2])
                        v44 = 4;
                    index->field_14 = v44;
                    index->field_a = iter;
                    if (v7 < 4294967294 && *((int *)&idx2[1 + 3]) < 4294967294)
                        index->field_10 = v7 + *((int *)&idx2[1 + 3]);
                    index->field_8 = idx2[4];
                    *((char *)&index[1].field_0) = 0;
                    v7 = v31;
                    index->field_8 = index->field_8 + (unsigned short)((8 - (unsigned short)v40 ^ 8 - (unsigned short)v40 >> 31) - (8 - (unsigned short)v40 >> 31));
                    v45 = v31;
                    v7 = v45;
                    v46 = (unsigned short)v45;
                    index->field_8 = index->field_8 + (unsigned short)((8 - v46 ^ 8 - v46 >> 31) - (8 - v46 >> 31));
                    v47 = index->field_8;
                    if (v47 > v17)
                        v17 = v47;
                    v7 = v17;
                    v6 = idx2;
                    v5 = v45;
                    v4 = v40;
                    v3 = &v8;
                    v2 = &v27;
                    v1 = index;
                    v0 = v46;
                    *((char *)&index[1].field_0) = 0;
                    if ((a0 - v40 ^ a0 - v40 >> 31) - (a0 - v40 >> 31) <= a2 && (a1 - v5 ^ a1 - v5 >> 31) - (a1 - v5 >> 31) <= a2)
                        *((char *)&index[1].field_0) = 1;
                    idx2 = v6;
                    v31 = v5;
                    v40 = v4;
                }
            }
            v48 = v40 + 1;
            v49 = v31 + 1;
            if (v48 < 18 && v49 < 14)
            {
                v50 = (v49 * 18 + v48) * 8;
                if (!*((int *)(v50 + (char *)&g_10288fc4[0])) || *((int *)(v50 + (char *)&g_10288fc4[0])) == iter)
                {
                    *((unsigned int *)(v50 + (char *)&g_10288fc4[0])) = iter;
                    v51 = *((int *)(v50 + (char *)&g_10052785[0]));
                    if (iter1 >= 400000)
                    {
                        sub_10025172("Trace paths space exceeded!");
                        return 0;
                    }
                    v52 = 23 * iter1 + (char *)g_10052774;
                    iter1 += 1;
                    v52->field_0 = v48;
                    v52->field_2 = v49;
                    v52->field_4 = idx2;
                    v52->field_c = v51;
                    v7 = v51;
                    v53 = idx2[2];
                    if (!(char)idx2[2])
                        v53 = 3;
                    v52->field_14 = v53;
                    v52->field_a = iter;
                    if (v7 < 4294967294 && *((int *)&idx2[1 + 3]) < 4294967294)
                        v52->field_10 = v7 + *((int *)&idx2[1 + 3]);
                    v52->field_8 = idx2[4];
                    *((char *)&v52[1].field_0) = 0;
                    v7 = v49;
                    v52->field_8 = v52->field_8 + (unsigned short)((8 - (unsigned short)v48 ^ 8 - (unsigned short)v48 >> 31) - (8 - (unsigned short)v48 >> 31));
                    v54 = v49;
                    v7 = v54;
                    v55 = (unsigned short)v54;
                    v52->field_8 = v52->field_8 + (unsigned short)((8 - v55 ^ 8 - v55 >> 31) - (8 - v55 >> 31));
                    v56 = v52->field_8;
                    if (v56 > v17)
                        v17 = v56;
                    v7 = v17;
                    v6 = idx2;
                    v5 = v54;
                    v4 = v48;
                    v3 = &v8;
                    v2 = &v27;
                    v1 = v52;
                    v0 = v55;
                    *((char *)&v52[1].field_0) = 0;
                    if ((a0 - v48 ^ a0 - v48 >> 31) - (a0 - v48 >> 31) <= a2 && (a1 - v5 ^ a1 - v5 >> 31) - (a1 - v5 >> 31) <= a2)
                        *((char *)&v52[1].field_0) = 1;
                    idx2 = v6;
                    v49 = v5;
                    v48 = v4;
                }
            }
            v57 = v49 - 2;
            if (v48 < 18 && v57 < 14)
            {
                v58 = (v57 * 18 + v48) * 8;
                if (!*((int *)(v58 + (char *)&g_10288fc4[0])) || *((int *)(v58 + (char *)&g_10288fc4[0])) == iter)
                {
                    *((unsigned int *)(v58 + (char *)&g_10288fc4[0])) = iter;
                    v59 = *((int *)(v58 + (char *)&g_10052785[0]));
                    if (iter1 >= 400000)
                    {
                        sub_10025172("Trace paths space exceeded!");
                        return 0;
                    }
                    v60 = 23 * iter1 + (char *)g_10052774;
                    iter1 += 1;
                    v60->field_0 = v48;
                    v60->field_2 = v57;
                    v60->field_4 = idx2;
                    v60->field_c = v59;
                    v7 = v59;
                    v61 = idx2[2];
                    if (!(char)idx2[2])
                        v61 = 1;
                    v60->field_14 = v61;
                    v60->field_a = iter;
                    if (v7 < 4294967294 && *((int *)&idx2[1 + 3]) < 4294967294)
                        v60->field_10 = v7 + *((int *)&idx2[1 + 3]);
                    v60->field_8 = idx2[4];
                    *((char *)&v60[1].field_0) = 0;
                    v7 = v57;
                    v60->field_8 = v60->field_8 + (unsigned short)((8 - (unsigned short)v48 ^ 8 - (unsigned short)v48 >> 31) - (8 - (unsigned short)v48 >> 31));
                    v62 = v57;
                    v7 = v62;
                    v63 = (unsigned short)v62;
                    v60->field_8 = v60->field_8 + (unsigned short)((8 - v63 ^ 8 - v63 >> 31) - (8 - v63 >> 31));
                    v64 = v60->field_8;
                    if (v64 > v17)
                        v17 = v64;
                    v7 = v17;
                    v6 = idx2;
                    v5 = v62;
                    v4 = v48;
                    v3 = &v8;
                    v2 = &v27;
                    v1 = v60;
                    v0 = v63;
                    *((char *)&v60[1].field_0) = 0;
                    if ((a0 - v48 ^ a0 - v48 >> 31) - (a0 - v48 >> 31) <= a2 && (a1 - v5 ^ a1 - v5 >> 31) - (a1 - v5 >> 31) <= a2)
                        *((char *)&v60[1].field_0) = 1;
                }
            }
        }
        if (g_10052784)
        {
            n = v20;
            for (v18 = v19; n < v18; n += 1)
            {
                v8 = n;
                v66 = 23 * n + (char *)g_10052774;
                v67 = v66->field_0 + 1;
                v68 = v66->field_2 - 1;
                if (v67 < 18 && v68 < 14)
                {
                    v69 = (v68 * 18 + v67) * 8;
                    if (!*((int *)(v69 + (char *)&g_10288fc4[0])) || *((int *)(v69 + (char *)&g_10288fc4[0])) == iter && iter1 < 10000)
                    {
                        *((unsigned int *)(v69 + (char *)&g_10288fc4[0])) = iter;
                        v70 = *((int *)(v69 + (char *)&g_10052785[0]));
                        if (iter1 >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return 0;
                        }
                        v71 = 23 * iter1 + (char *)g_10052774;
                        iter1 += 1;
                        v71->field_0 = v67;
                        v71->field_2 = v68;
                        v71->field_4 = v66;
                        v71->field_c = v70;
                        v7 = v70;
                        v72 = v66->field_14;
                        if (!v66->field_14)
                            v72 = 5;
                        v71->field_14 = v72;
                        v71->field_a = iter;
                        if (v7 < 4294967294 && v66->field_10 < 4294967294)
                            v71->field_10 = v7 * 3 + v66->field_10;
                        v71->field_8 = v66->field_8;
                        v71->field_15 = 0;
                        v7 = v68;
                        v71->field_8 = v71->field_8 + (unsigned short)((8 - (unsigned short)v67 ^ 8 - (unsigned short)v67 >> 31) - (8 - (unsigned short)v67 >> 31));
                        v73 = v68;
                        v7 = v73;
                        v74 = (unsigned short)v73;
                        v71->field_8 = v71->field_8 + (unsigned short)((8 - v74 ^ 8 - v74 >> 31) - (8 - v74 >> 31));
                        v75 = v71->field_8;
                        if (v75 > v17)
                            v17 = v75;
                        v7 = v17;
                        v6 = v66;
                        v5 = v73;
                        v4 = v67;
                        v3 = &v8;
                        v2 = &v27;
                        v1 = v71;
                        v0 = v74;
                        v71->field_15 = 0;
                        if ((a0 - v67 ^ a0 - v67 >> 31) - (a0 - v67 >> 31) <= a2 && (a1 - v5 ^ a1 - v5 >> 31) - (a1 - v5 >> 31) <= a2)
                            v71->field_15 = 1;
                        v66 = v6;
                        v68 = v5;
                        v67 = v4;
                    }
                }
                v76 = v68 + 2;
                if (v67 < 18 && v76 < 14)
                {
                    v77 = (v76 * 18 + v67) * 8;
                    if (!*((int *)(v77 + (char *)&g_10288fc4[0])) || *((int *)(v77 + (char *)&g_10288fc4[0])) == iter && iter1 < 10000)
                    {
                        *((unsigned int *)(v77 + (char *)&g_10288fc4[0])) = iter;
                        v78 = *((int *)(v77 + (char *)&g_10052785[0]));
                        if (iter1 >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return 0;
                        }
                        v79 = 23 * iter1 + (char *)g_10052774;
                        iter1 += 1;
                        v79->field_0 = v67;
                        v79->field_2 = v76;
                        v79->field_4 = v66;
                        v79->field_c = v78;
                        v7 = v78;
                        v80 = v66->field_14;
                        if (!v66->field_14)
                            v80 = 6;
                        v79->field_14 = v80;
                        v79->field_a = iter;
                        if (v7 < 4294967294 && v66->field_10 < 4294967294)
                            v79->field_10 = v7 * 3 + v66->field_10;
                        v79->field_8 = v66->field_8;
                        v79->field_15 = 0;
                        v7 = v76;
                        v79->field_8 = v79->field_8 + (unsigned short)((8 - (unsigned short)v67 ^ 8 - (unsigned short)v67 >> 31) - (8 - (unsigned short)v67 >> 31));
                        v81 = v76;
                        v7 = v81;
                        v82 = (unsigned short)v81;
                        v79->field_8 = v79->field_8 + (unsigned short)((8 - v82 ^ 8 - v82 >> 31) - (8 - v82 >> 31));
                        v83 = v79->field_8;
                        if (v83 > v17)
                            v17 = v83;
                        v7 = v17;
                        v6 = v66;
                        v5 = v81;
                        v4 = v67;
                        v3 = &v8;
                        v2 = &v27;
                        v1 = v79;
                        v0 = v82;
                        v79->field_15 = 0;
                        if ((a0 - v67 ^ a0 - v67 >> 31) - (a0 - v67 >> 31) <= a2 && (a1 - v5 ^ a1 - v5 >> 31) - (a1 - v5 >> 31) <= a2)
                            v79->field_15 = 1;
                        v66 = v6;
                        v76 = v5;
                        v67 = v4;
                    }
                }
                v84 = v67 - 2;
                if (v84 < 18 && v76 < 14)
                {
                    v85 = (v76 * 18 + v84) * 8;
                    if (!*((int *)(v85 + (char *)&g_10288fc4[0])) || *((int *)(v85 + (char *)&g_10288fc4[0])) == iter && iter1 < 10000)
                    {
                        *((unsigned int *)(v85 + (char *)&g_10288fc4[0])) = iter;
                        v86 = *((int *)(v85 + (char *)&g_10052785[0]));
                        if (iter1 >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return 0;
                        }
                        v87 = 23 * iter1 + (char *)g_10052774;
                        iter1 += 1;
                        v87->field_0 = v84;
                        v87->field_2 = v76;
                        v87->field_4 = v66;
                        v87->field_c = v86;
                        v7 = v86;
                        v88 = v66->field_14;
                        if (!v66->field_14)
                            v88 = 7;
                        v87->field_14 = v88;
                        v87->field_a = iter;
                        if (v7 < 4294967294 && v66->field_10 < 4294967294)
                            v87->field_10 = v7 * 3 + v66->field_10;
                        v87->field_8 = v66->field_8;
                        v87->field_15 = 0;
                        v7 = v76;
                        v87->field_8 = v87->field_8 + (unsigned short)((8 - (unsigned short)v84 ^ 8 - (unsigned short)v84 >> 31) - (8 - (unsigned short)v84 >> 31));
                        v89 = v76;
                        v7 = v89;
                        v90 = (unsigned short)v89;
                        v87->field_8 = v87->field_8 + (unsigned short)((8 - v90 ^ 8 - v90 >> 31) - (8 - v90 >> 31));
                        v91 = v87->field_8;
                        if (v91 > v17)
                            v17 = v91;
                        v7 = v17;
                        v6 = v66;
                        v5 = v89;
                        v4 = v84;
                        v3 = &v8;
                        v2 = &v27;
                        v1 = v87;
                        v0 = v90;
                        v87->field_15 = 0;
                        if ((a0 - v84 ^ a0 - v84 >> 31) - (a0 - v84 >> 31) <= a2 && (a1 - v5 ^ a1 - v5 >> 31) - (a1 - v5 >> 31) <= a2)
                            v87->field_15 = 1;
                        v66 = v6;
                        v76 = v5;
                        v84 = v4;
                    }
                }
                v92 = v76 - 2;
                if (v84 < 18 && v92 < 14)
                {
                    v93 = (v92 * 18 + v84) * 8;
                    if (!*((int *)(v93 + (char *)&g_10288fc4[0])) || *((int *)(v93 + (char *)&g_10288fc4[0])) == iter && iter1 < 10000)
                    {
                        *((unsigned int *)(v93 + (char *)&g_10288fc4[0])) = iter;
                        v94 = *((int *)(v93 + (char *)&g_10052785[0]));
                        if (iter1 >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return 0;
                        }
                        v95 = 23 * iter1 + (char *)g_10052774;
                        iter1 += 1;
                        v95->field_0 = v84;
                        v95->field_2 = v92;
                        v95->field_4 = v66;
                        v95->field_c = v94;
                        v7 = v94;
                        v96 = v66->field_14;
                        if (!v66->field_14)
                            v96 = 8;
                        v95->field_14 = v96;
                        v95->field_a = iter;
                        if (v7 < 4294967294 && v66->field_10 < 4294967294)
                            v95->field_10 = v7 * 3 + v66->field_10;
                        v95->field_8 = v66->field_8;
                        v95->field_15 = 0;
                        v7 = v92;
                        v95->field_8 = v95->field_8 + (unsigned short)((8 - (unsigned short)v84 ^ 8 - (unsigned short)v84 >> 31) - (8 - (unsigned short)v84 >> 31));
                        v97 = v92;
                        v7 = v97;
                        v98 = (unsigned short)v97;
                        v95->field_8 = v95->field_8 + (unsigned short)((8 - v98 ^ 8 - v98 >> 31) - (8 - v98 >> 31));
                        v99 = v95->field_8;
                        if (v99 > v17)
                            v17 = v99;
                        v7 = v17;
                        v6 = v66;
                        v5 = v97;
                        v4 = v84;
                        v3 = &v8;
                        v2 = &v27;
                        v1 = v95;
                        v0 = v98;
                        v95->field_15 = 0;
                        if ((a0 - v84 ^ a0 - v84 >> 31) - (a0 - v84 >> 31) <= a2 && (a1 - v5 ^ a1 - v5 >> 31) - (a1 - v5 >> 31) <= a2)
                            v95->field_15 = 1;
                    }
                }
            }
            v20 = v23;
            v19 = v21;
            v23 = v19;
            if (v19 != iter1)
            {
                iter += 1;
            }
            else if (v20 == v19)
            {
                break;
            }
            else
            {
                iter += 1;
            }
        }
        else
        {
            v23 = v21;
            if (v23 == iter1)
                break;
            else
                iter += 1;
        }
    }
    v100 = sub_1002ae81(&g_102897a4, 216);
    v16 = 0;
    v13 = 0;
    v15 = 0;
    v101 = 23 * iter1 + (char *)g_10052774;
    v12 = 4294967295;
    v9 = 4294967295;
    v13 = 4294967295;
    for (node = g_10052774; node < v101; node = &node->field_17)
    {
        v6 = v101;
        v10 = v9;
        if (node->field_15)
        {
            v100 = node->field_c;
            if (v100 < v12 || v100 == v12 && v11 < v9 || (v13 = v13, v10 = v9, v100 == v12 && !((v13 = v13, v10 = v9, v11 != v10 || (v13 = v13, v10 = v9, v14 >= v13)))))
            {
                v12 = v100;
                v11 = node->field_10;
                v14 = node->field_a;
                v15 = node->field_14;
                v13 = v14;
                v10 = v11;
            }
        }
        v9 = v10;
        v101 = v6;
    }
    return v100;
}
```

## `sub_10010a33` `0x10010a33`

_2 bytes. (leaf/helper — see body)_

```c
void sub_10010a33(void)
{
}
```

## `sub_10010aec` `0x10010aec`

_4 bytes. (leaf/helper — see body)_

```c
void sub_10010aec(void)
{
    return;
}
```

## `sub_10010af0` `0x10010af0`

_2762 bytes. refs "Trace paths space exceeded!", "Trace paths space exceeded!", "Trace paths space exceeded!"_

```c
typedef struct struct_0 {
    unsigned short field_0;
    unsigned short field_2;
    struct struct_1 *field_4;
    unsigned short field_8;
    unsigned short field_a;
    unsigned int field_c;
    unsigned int field_10;
    char field_14;
    char field_15;
} struct_0;

typedef struct struct_4 {
    unsigned short field_0;
    unsigned short field_2;
    struct struct_1 *field_4;
    unsigned short field_8;
    unsigned short field_a;
    unsigned int field_c;
    unsigned int field_10;
    char field_14;
} struct_4;

typedef struct struct_8 {
    unsigned short field_0;
    unsigned short field_2;
    char padding_4[4];
    unsigned short field_8;
    char padding_a[6];
    unsigned int field_10;
    char field_14;
} struct_8;

typedef struct struct_17 {
    unsigned short field_0;
    unsigned short field_2;
    unsigned int field_4;
    unsigned short field_8;
    unsigned short field_a;
    char padding_c[4];
    unsigned int field_10;
    char field_14;
    char field_15;
    char field_16;
    char field_17;
} struct_17;

typedef struct struct_1 {
    unsigned short field_0;
    unsigned short field_2;
    char padding_4[4];
    unsigned short field_8;
} struct_1;

extern struct_17 *g_10052774;
extern unsigned int g_10052780;
extern char g_10052784;
extern unsigned int g_10052785[4];
extern unsigned int g_10053dfa[4];
extern unsigned int g_10288fc4[4];
extern unsigned int g_10289364;
extern unsigned int g_102897a4[4];
extern unsigned int g_102897a8[4];
extern unsigned int g_102897ac[4];
extern unsigned int g_102897e4[4];
extern unsigned int g_102897e8;

unsigned int [4] sub_10010af0(void)
{
    unsigned int idx;  // ecx
    unsigned int m;  // ecx
    unsigned int v27;  // ebx
    unsigned int v28;  // edx
    unsigned int v29;  // eax
    unsigned int v30;  // ebx
    unsigned int v31;  // ebx
    unsigned int idx1;  // esi
    unsigned int v33;  // eax
    struct_0 *index;  // esi
    char v35;  // al
    unsigned short idx2[5];  // ecx
    unsigned int v36;  // ebx
    unsigned int v37;  // edx
    unsigned int v38;  // eax
    unsigned int v39;  // ebx
    unsigned int v40;  // edx
    unsigned int v41;  // ebx
    unsigned int v42;  // esi
    unsigned int v43;  // eax
    struct_4 *v44;  // esi
    unsigned int v20;  // edx
    char v45;  // al
    unsigned int v46;  // ebx
    unsigned int v47;  // edx
    unsigned int v48;  // eax
    unsigned int v49;  // edx
    unsigned int v50;  // esi
    unsigned int v51;  // eax
    struct_4 *v52;  // esi
    char v53;  // al
    unsigned int v21;  // ebx
    unsigned short v54;  // bx
    unsigned int v55;  // edx
    unsigned int v56;  // eax
    unsigned int n;  // ecx
    struct_8 *v58;  // ecx
    unsigned int v59;  // ebx
    unsigned int v60;  // edx
    unsigned int v61;  // ebx
    unsigned int v62;  // esi
    unsigned int v22;  // ebx
    unsigned int v63;  // eax
    struct_0 *v64;  // esi
    char v65;  // al
    unsigned int v66;  // ebx
    unsigned int v67;  // edx
    unsigned int v68;  // eax
    unsigned int v69;  // edx
    unsigned int v70;  // ebx
    unsigned int v71;  // esi
    unsigned int v23;  // esi
    unsigned int v72;  // eax
    struct_0 *v73;  // esi
    char v74;  // al
    unsigned int v75;  // ebx
    unsigned int v76;  // edx
    unsigned int v77;  // eax
    unsigned int v78;  // ebx
    unsigned int v79;  // ebx
    unsigned int v80;  // esi
    unsigned int v24;  // eax
    unsigned int v81;  // eax
    struct_0 *v82;  // esi
    char v83;  // al
    unsigned int v84;  // ebx
    unsigned int v85;  // edx
    unsigned int v86;  // eax
    unsigned int v87;  // edx
    unsigned int v88;  // esi
    unsigned int v89;  // eax
    struct_0 *v25;  // esi
    struct_0 *v90;  // esi
    char v91;  // al
    unsigned short v92;  // bx
    unsigned int v93;  // edx
    unsigned int v94;  // eax
    unsigned int v95[4];  // eax
    unsigned int v96;  // ecx
    struct_17 *node;  // ebx
    unsigned int v98;  // ecx
    char v26;  // al
    unsigned int v99;  // ecx
    unsigned int v100;  // ecx
    unsigned int v101;  // ecx
    unsigned int v0;  // [bp-0x84]
    unsigned int v1;  // [bp-0x80]
    unsigned int v2;  // [bp-0x7c]
    unsigned int v3;  // [bp-0x78]
    unsigned int v4;  // [bp-0x74]
    unsigned int v5[4];  // [bp-0x70]
    unsigned int v6;  // [bp-0x2c]
    unsigned int v7;  // [bp-0x28]
    unsigned int v8;  // [bp-0x24]
    unsigned int v9;  // [bp-0x20]
    unsigned int v10;  // [bp-0x1c]
    unsigned int iter2;  // [bp-0x18]
    unsigned int v12;  // [bp-0x14]
    unsigned int iter;  // [bp-0x10]
    unsigned int iter1;  // [bp-0xc]
    unsigned int i;  // [bp-0x8]

    v6 = 0;
    for (i = 0; i < 14; i += 1)
    {
        iter1 = 0;
        while (iter1 < 18)
        {
            idx = (i * 18 + iter1) * 8;
            *((unsigned int *)(idx + (char *)&g_10288fc4[0])) = 0;
            if (*((int *)(idx + (char *)&g_10052785[0])) >= 4294967294)
            {
                *((unsigned int *)(idx + (char *)&g_10288fc4[0])) = 4294967295;
                iter1 += 1;
            }
            else
            {
                iter1 += 1;
            }
        }
    }
    g_10052774->field_0 = 8;
    g_10052774->field_2 = 6;
    g_10289364 = 1;
    g_10052774->field_10 = 0;
    g_10052774->field_15 = 0;
    g_10052774->field_4 = 0;
    g_10052774->field_8 = 0;
    g_10052774->field_14 = 0;
    g_10052774->field_16 = 0;
    iter2 = 1;
    v12 = 0;
    v9 = 0;
    v8 = 0;
    v7 = 0;
    iter = 1;
    while (iter < 18)
    {
        m = v12;
        for (v10 = iter2; m < v10; m += 1)
        {
            v2 = m;
            idx2 = 23 * m + (char *)g_10052774;
            v20 = idx2[1];
            v21 = idx2[0] + 1;
            v22 = v21;
            if (v22 < 18)
            {
                v22 = v21;
                if (v20 < 14)
                {
                    v23 = (v20 * 18 + v21) * 8;
                    if (!*((int *)(v23 + (char *)&g_10288fc4[0])) || (v22 = v21, *((int *)(v23 + (char *)&g_10288fc4[0])) == iter))
                    {
                        *((unsigned int *)(v23 + (char *)&g_10288fc4[0])) = iter;
                        v24 = *((int *)(v23 + (char *)&g_10052785[0]));
                        if (iter2 >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return NULL;
                        }
                        v25 = 23 * iter2 + (char *)g_10052774;
                        iter2 += 1;
                        v25->field_0 = v21;
                        v25->field_2 = v20;
                        v25->field_4 = idx2;
                        v25->field_c = v24;
                        v1 = v24;
                        v26 = idx2[2];
                        if (!(char)idx2[2])
                            v26 = 2;
                        v25->field_14 = v26;
                        v25->field_a = iter;
                        if (v1 < 4294967294 && *((int *)&idx2[1 + 3]) < 4294967294)
                            v25->field_10 = v1 + *((int *)&idx2[1 + 3]);
                        v25->field_8 = idx2[4];
                        v25->field_15 = 0;
                        v27 = _INSERT(v21, 0, v21);
                        v28 = v20;
                        if (!(unsigned short)v21 || (v28 = _INSERT(v20, 0, (unsigned short)v20), v28 = v28, !(unsigned short)v20 || (v28 = v28, (unsigned short)v27 == 0x11 || (v28 = v28, (unsigned short)v28 == 13))))
                            v25->field_15 = 1;
                        v1 = v28;
                        v25->field_8 = v25->field_8 + (unsigned short)((8 - (unsigned short)v27 ^ 8 - (unsigned short)v27 >> 31) - (8 - (unsigned short)v27 >> 31));
                        v20 = v28;
                        v1 = v28;
                        v25->field_8 = v25->field_8 + (unsigned short)((8 - (unsigned short)v20 ^ 8 - (unsigned short)v20 >> 31) - (8 - (unsigned short)v20 >> 31));
                        v29 = v25->field_8;
                        if (v29 > v6)
                            v6 = v29;
                        v22 = v27;
                    }
                }
            }
            v30 = v22 - 2;
            v31 = v30;
            if (v31 < 18)
            {
                v31 = v30;
                if (v20 < 14)
                {
                    idx1 = (v20 * 18 + v30) * 8;
                    if (!*((int *)(idx1 + (char *)&g_10288fc4[0])) || (v31 = v30, *((int *)(idx1 + (char *)&g_10288fc4[0])) == iter))
                    {
                        *((unsigned int *)(idx1 + (char *)&g_10288fc4[0])) = iter;
                        v33 = *((int *)(idx1 + (char *)&g_10052785[0]));
                        if (iter2 >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return NULL;
                        }
                        index = 23 * iter2 + (char *)g_10052774;
                        iter2 += 1;
                        index->field_0 = v30;
                        index->field_2 = v20;
                        index->field_4 = idx2;
                        index->field_c = v33;
                        v1 = v33;
                        v35 = idx2[2];
                        if (!(char)idx2[2])
                            v35 = 4;
                        index->field_14 = v35;
                        index->field_a = iter;
                        if (v1 < 4294967294 && *((int *)&idx2[1 + 3]) < 4294967294)
                            index->field_10 = v1 + *((int *)&idx2[1 + 3]);
                        index->field_8 = idx2[4];
                        index->field_15 = 0;
                        v36 = _INSERT(v30, 0, v30);
                        v37 = v20;
                        if (!(unsigned short)v30 || (v37 = _INSERT(v20, 0, (unsigned short)v20), v37 = v37, !(unsigned short)v20 || (v37 = v37, (unsigned short)v36 == 0x11 || (v37 = v37, (unsigned short)v37 == 13))))
                            index->field_15 = 1;
                        v1 = v37;
                        index->field_8 = index->field_8 + (unsigned short)((8 - (unsigned short)v36 ^ 8 - (unsigned short)v36 >> 31) - (8 - (unsigned short)v36 >> 31));
                        v20 = v37;
                        v1 = v37;
                        index->field_8 = index->field_8 + (unsigned short)((8 - (unsigned short)v20 ^ 8 - (unsigned short)v20 >> 31) - (8 - (unsigned short)v20 >> 31));
                        v38 = index->field_8;
                        if (v38 > v6)
                            v6 = v38;
                        v31 = v36;
                    }
                }
            }
            v39 = v31 + 1;
            v40 = v20 + 1;
            v41 = v39;
            if (v41 < 18)
            {
                v41 = v39;
                if (v40 < 14)
                {
                    v42 = (v40 * 18 + v39) * 8;
                    if (!*((int *)(v42 + (char *)&g_10288fc4[0])) || (v41 = v39, *((int *)(v42 + (char *)&g_10288fc4[0])) == iter))
                    {
                        *((unsigned int *)(v42 + (char *)&g_10288fc4[0])) = iter;
                        v43 = *((int *)(v42 + (char *)&g_10052785[0]));
                        if (iter2 >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return NULL;
                        }
                        v44 = 23 * iter2 + (char *)g_10052774;
                        iter2 += 1;
                        v44->field_0 = v39;
                        v44->field_2 = v40;
                        v44->field_4 = idx2;
                        v44->field_c = v43;
                        v1 = v43;
                        v45 = idx2[2];
                        if (!(char)idx2[2])
                            v45 = 3;
                        v44->field_14 = v45;
                        v44->field_a = iter;
                        if (v1 < 4294967294 && *((int *)&idx2[1 + 3]) < 4294967294)
                            v44->field_10 = v1 + *((int *)&idx2[1 + 3]);
                        v44->field_8 = idx2[4];
                        *((char *)&v44[1].field_0) = 0;
                        v46 = _INSERT(v39, 0, v39);
                        v47 = v40;
                        if (!(unsigned short)v39 || (v47 = _INSERT(v40, 0, (unsigned short)v40), v47 = v47, !(unsigned short)v40 || (v47 = v47, (unsigned short)v46 == 0x11 || (v47 = v47, (unsigned short)v47 == 13))))
                            *((char *)&v44[1].field_0) = 1;
                        v1 = v47;
                        v44->field_8 = v44->field_8 + (unsigned short)((8 - (unsigned short)v46 ^ 8 - (unsigned short)v46 >> 31) - (8 - (unsigned short)v46 >> 31));
                        v40 = v47;
                        v1 = v47;
                        v44->field_8 = v44->field_8 + (unsigned short)((8 - (unsigned short)v40 ^ 8 - (unsigned short)v40 >> 31) - (8 - (unsigned short)v40 >> 31));
                        v48 = v44->field_8;
                        if (v48 > v6)
                            v6 = v48;
                        v41 = v46;
                    }
                }
            }
            v49 = v40 - 2;
            if (v41 < 18 && v49 < 14)
            {
                v50 = (v49 * 18 + v41) * 8;
                if (!*((int *)(v50 + (char *)&g_10288fc4[0])) || *((int *)(v50 + (char *)&g_10288fc4[0])) == iter)
                {
                    *((unsigned int *)(v50 + (char *)&g_10288fc4[0])) = iter;
                    v51 = *((int *)(v50 + (char *)&g_10052785[0]));
                    if (iter2 >= 400000)
                    {
                        sub_10025172("Trace paths space exceeded!");
                        return NULL;
                    }
                    v52 = 23 * iter2 + (char *)g_10052774;
                    iter2 += 1;
                    v52->field_0 = v41;
                    v52->field_2 = v49;
                    v52->field_4 = idx2;
                    v52->field_c = v51;
                    v1 = v51;
                    v53 = idx2[2];
                    if (!(char)idx2[2])
                        v53 = 1;
                    v52->field_14 = v53;
                    v52->field_a = iter;
                    if (v1 < 4294967294 && *((int *)&idx2[1 + 3]) < 4294967294)
                        v52->field_10 = v1 + *((int *)&idx2[1 + 3]);
                    v52->field_8 = idx2[4];
                    *((char *)&v52[1].field_0) = 0;
                    v54 = v41;
                    v55 = v49;
                    if (!(unsigned short)v41 || (v55 = _INSERT(v49, 0, (unsigned short)v49), v55 = v55, !(unsigned short)v49 || (v55 = v55, v54 == 0x11 || (v55 = v55, (unsigned short)v55 == 13))))
                        *((char *)&v52[1].field_0) = 1;
                    v1 = v55;
                    v52->field_8 = v52->field_8 + (unsigned short)((8 - v54 ^ 8 - v54 >> 31) - (8 - v54 >> 31));
                    v1 = v55;
                    v52->field_8 = v52->field_8 + (unsigned short)((8 - (unsigned short)v55 ^ 8 - (unsigned short)v55 >> 31) - (8 - (unsigned short)v55 >> 31));
                    v56 = v52->field_8;
                    if (v56 > v6)
                        v6 = v56;
                }
            }
        }
        if (g_10052784)
        {
            n = v9;
            for (v7 = v8; n < v7; n += 1)
            {
                v2 = n;
                v58 = 23 * n + (char *)g_10052774;
                v59 = v58->field_0 + 1;
                v60 = v58->field_2 - 1;
                v61 = v59;
                if (v61 < 18)
                {
                    v61 = v59;
                    if (v60 < 14)
                    {
                        v62 = (v60 * 18 + v59) * 8;
                        if (!*((int *)(v62 + (char *)&g_10288fc4[0])) || (v61 = v59, *((int *)(v62 + (char *)&g_10288fc4[0])) == iter && (v61 = v59, iter2 < 10000)))
                        {
                            *((unsigned int *)(v62 + (char *)&g_10288fc4[0])) = iter;
                            v63 = *((int *)(v62 + (char *)&g_10052785[0]));
                            if (iter2 >= 400000)
                            {
                                sub_10025172("Trace paths space exceeded!");
                                return NULL;
                            }
                            v64 = 23 * iter2 + (char *)g_10052774;
                            iter2 += 1;
                            v64->field_0 = v59;
                            v64->field_2 = v60;
                            v64->field_4 = v58;
                            v64->field_c = v63;
                            v1 = v63;
                            v65 = v58->field_14;
                            if (!v58->field_14)
                                v65 = 5;
                            v64->field_14 = v65;
                            v64->field_a = iter;
                            if (v1 < 4294967294 && v58->field_10 < 4294967294)
                                v64->field_10 = v1 * 3 + v58->field_10;
                            v64->field_8 = v58->field_8;
                            v64->field_15 = 0;
                            v66 = _INSERT(v59, 0, v59);
                            v67 = v60;
                            if (!(unsigned short)v59 || (v67 = _INSERT(v60, 0, (unsigned short)v60), v67 = v67, !(unsigned short)v60 || (v67 = v67, (unsigned short)v66 == 0x11 || (v67 = v67, (unsigned short)v67 == 13))))
                                v64->field_15 = 1;
                            v1 = v67;
                            v64->field_8 = v64->field_8 + (unsigned short)((8 - (unsigned short)v66 ^ 8 - (unsigned short)v66 >> 31) - (8 - (unsigned short)v66 >> 31));
                            v60 = v67;
                            v1 = v67;
                            v64->field_8 = v64->field_8 + (unsigned short)((8 - (unsigned short)v60 ^ 8 - (unsigned short)v60 >> 31) - (8 - (unsigned short)v60 >> 31));
                            v68 = v64->field_8;
                            if (v68 > v6)
                                v6 = v68;
                            v61 = v66;
                        }
                    }
                }
                v69 = v60 + 2;
                v70 = v61;
                if (v70 < 18)
                {
                    v70 = v61;
                    if (v69 < 14)
                    {
                        v71 = (v69 * 18 + v61) * 8;
                        if (!*((int *)(v71 + (char *)&g_10288fc4[0])) || (v70 = v61, *((int *)(v71 + (char *)&g_10288fc4[0])) == iter && (v70 = v61, iter2 < 10000)))
                        {
                            *((unsigned int *)(v71 + (char *)&g_10288fc4[0])) = iter;
                            v72 = *((int *)(v71 + (char *)&g_10052785[0]));
                            if (iter2 >= 400000)
                            {
                                sub_10025172("Trace paths space exceeded!");
                                return NULL;
                            }
                            v73 = 23 * iter2 + (char *)g_10052774;
                            iter2 += 1;
                            v73->field_0 = v61;
                            v73->field_2 = v69;
                            v73->field_4 = v58;
                            v73->field_c = v72;
                            v1 = v72;
                            v74 = v58->field_14;
                            if (!v58->field_14)
                                v74 = 6;
                            v73->field_14 = v74;
                            v73->field_a = iter;
                            if (v1 < 4294967294 && v58->field_10 < 4294967294)
                                v73->field_10 = v1 * 3 + v58->field_10;
                            v73->field_8 = v58->field_8;
                            v73->field_15 = 0;
                            v75 = _INSERT(v61, 0, v61);
                            v76 = v69;
                            if (!(unsigned short)v61 || (v76 = _INSERT(v69, 0, (unsigned short)v69), v76 = v76, !(unsigned short)v69 || (v76 = v76, (unsigned short)v75 == 0x11 || (v76 = v76, (unsigned short)v76 == 13))))
                                v73->field_15 = 1;
                            v1 = v76;
                            v73->field_8 = v73->field_8 + (unsigned short)((8 - (unsigned short)v75 ^ 8 - (unsigned short)v75 >> 31) - (8 - (unsigned short)v75 >> 31));
                            v69 = v76;
                            v1 = v76;
                            v73->field_8 = v73->field_8 + (unsigned short)((8 - (unsigned short)v69 ^ 8 - (unsigned short)v69 >> 31) - (8 - (unsigned short)v69 >> 31));
                            v77 = v73->field_8;
                            if (v77 > v6)
                                v6 = v77;
                            v70 = v75;
                        }
                    }
                }
                v78 = v70 - 2;
                v79 = v78;
                if (v79 < 18)
                {
                    v79 = v78;
                    if (v69 < 14)
                    {
                        v80 = (v69 * 18 + v78) * 8;
                        if (!*((int *)(v80 + (char *)&g_10288fc4[0])) || (v79 = v78, *((int *)(v80 + (char *)&g_10288fc4[0])) == iter && (v79 = v78, iter2 < 10000)))
                        {
                            *((unsigned int *)(v80 + (char *)&g_10288fc4[0])) = iter;
                            v81 = *((int *)(v80 + (char *)&g_10052785[0]));
                            if (iter2 >= 400000)
                            {
                                sub_10025172("Trace paths space exceeded!");
                                return NULL;
                            }
                            v82 = 23 * iter2 + (char *)g_10052774;
                            iter2 += 1;
                            v82->field_0 = v78;
                            v82->field_2 = v69;
                            v82->field_4 = v58;
                            v82->field_c = v81;
                            v1 = v81;
                            v83 = v58->field_14;
                            if (!v58->field_14)
                                v83 = 7;
                            v82->field_14 = v83;
                            v82->field_a = iter;
                            if (v1 < 4294967294 && v58->field_10 < 4294967294)
                                v82->field_10 = v1 * 3 + v58->field_10;
                            v82->field_8 = v58->field_8;
                            v82->field_15 = 0;
                            v84 = _INSERT(v78, 0, v78);
                            v85 = v69;
                            if (!(unsigned short)v78 || (v85 = _INSERT(v69, 0, (unsigned short)v69), v85 = v85, !(unsigned short)v69 || (v85 = v85, (unsigned short)v84 == 0x11 || (v85 = v85, (unsigned short)v85 == 13))))
                                v82->field_15 = 1;
                            v1 = v85;
                            v82->field_8 = v82->field_8 + (unsigned short)((8 - (unsigned short)v84 ^ 8 - (unsigned short)v84 >> 31) - (8 - (unsigned short)v84 >> 31));
                            v69 = v85;
                            v1 = v85;
                            v82->field_8 = v82->field_8 + (unsigned short)((8 - (unsigned short)v69 ^ 8 - (unsigned short)v69 >> 31) - (8 - (unsigned short)v69 >> 31));
                            v86 = v82->field_8;
                            if (v86 > v6)
                                v6 = v86;
                            v79 = v84;
                        }
                    }
                }
                v87 = v69 - 2;
                if (v79 < 18 && v87 < 14)
                {
                    v88 = (v87 * 18 + v79) * 8;
                    if (!*((int *)(v88 + (char *)&g_10288fc4[0])) || *((int *)(v88 + (char *)&g_10288fc4[0])) == iter && iter2 < 10000)
                    {
                        *((unsigned int *)(v88 + (char *)&g_10288fc4[0])) = iter;
                        v89 = *((int *)(v88 + (char *)&g_10052785[0]));
                        if (iter2 >= 400000)
                        {
                            sub_10025172("Trace paths space exceeded!");
                            return NULL;
                        }
                        v90 = 23 * iter2 + (char *)g_10052774;
                        iter2 += 1;
                        v90->field_0 = v79;
                        v90->field_2 = v87;
                        v90->field_4 = v58;
                        v90->field_c = v89;
                        v1 = v89;
                        v91 = v58->field_14;
                        if (!v58->field_14)
                            v91 = 8;
                        v90->field_14 = v91;
                        v90->field_a = iter;
                        if (v1 < 4294967294 && v58->field_10 < 4294967294)
                            v90->field_10 = v1 * 3 + v58->field_10;
                        v90->field_8 = v58->field_8;
                        v90->field_15 = 0;
                        v92 = v79;
                        v93 = v87;
                        if (!(unsigned short)v79 || (v93 = _INSERT(v87, 0, (unsigned short)v87), v93 = v93, !(unsigned short)v87 || (v93 = v93, v92 == 0x11 || (v93 = v93, (unsigned short)v93 == 13))))
                            v90->field_15 = 1;
                        v1 = v93;
                        v90->field_8 = v90->field_8 + (unsigned short)((8 - v92 ^ 8 - v92 >> 31) - (8 - v92 >> 31));
                        v1 = v93;
                        v90->field_8 = v90->field_8 + (unsigned short)((8 - (unsigned short)v93 ^ 8 - (unsigned short)v93 >> 31) - (8 - (unsigned short)v93 >> 31));
                        v94 = v90->field_8;
                        if (v94 > v6)
                            v6 = v94;
                    }
                }
            }
            v9 = v12;
            v8 = v10;
            v12 = v8;
            if (v8 != iter2)
            {
                iter += 1;
            }
            else if (v9 == v8)
            {
                break;
            }
            else
            {
                iter += 1;
            }
        }
        else
        {
            v12 = v10;
            if (v12 == iter2)
                break;
            else
                iter += 1;
        }
    }
    v95 = sub_1002ae81(&g_102897a4[0], 216);
    v5 = NULL;
    v3 = 0;
    v4 = 0;
    v96 = 23 * iter2 + (char *)g_10052774;
    for (node = g_10052774; node < v96; node = &node->field_17)
    {
        v0 = v96;
        v98 = node->field_a;
        v95 = 1000 * v98 * g_10053dfa[v98];
        if (node->field_10)
        {
            v95 /= node->field_10;
            if (node->field_15)
                v95 = (unsigned int)((v95 * 6 & 4294967295) / 5);
            v99 = node->field_14;
            if (g_10052780 != 4294967295 && v99 == g_10052780)
                v95 *= 2;
            if (v95 > v5)
            {
                v5 = v95;
                v4 = v99;
                v99 = node->field_a;
                v3 = v99;
            }
            v100 = v99 * 16;
            *((unsigned int *[4])(v100 + (char *)&g_102897a4[0])) = *((int *)(v100 + (char *)&g_102897a4[0])) + (char *)v95;
            *((unsigned int *)(v100 + (char *)&g_102897a8[0])) = *((int *)(v100 + (char *)&g_102897a8[0])) + 1;
            if (v95 > *((int *)(v100 + (char *)&g_102897ac[0])))
                *((unsigned int *[4])(v100 + (char *)&g_102897ac[0])) = v95;
            v101 = node->field_a;
            if (v95 > g_102897e4[2 * v101])
            {
                g_102897e4[2 * v101] = v95;
                (&g_102897e8)[2 * v101] = node->field_14;
            }
        }
        v96 = v0;
    }
    return v95;
}
```

## `sub_100114b9` `0x100114b9`

_2 bytes. (leaf/helper — see body)_

```c
void sub_100114b9(void)
{
}
```

## `sub_100115bc` `0x100115bc`

_188 bytes. (leaf/helper — see body)_

```c
extern unsigned int g_10052785[4];
extern unsigned int g_10052f78;
extern unsigned int g_100530bc;

void* sub_100115bc(unsigned int a0, void* a1, unsigned int a2, unsigned int a3)
{
    unsigned int v6;  // ebx
    void* v7;  // eax
    unsigned int v8;  // ebx
    unsigned int v9;  // edx
    void* v10;  // eax
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    void* v2;  // [bp-0x14]
    unsigned int v3;  // [bp-0x10]
    unsigned int i;  // [bp-0xc]
    unsigned int iter;  // [bp-0x8]

    if (a2 == 1)
    {
        v1 = &g_10052f78;
    }
    else if (a2 == 2)
    {
        v1 = &g_100530bc;
    }
    else
    {
        return v10;
    }
    v0 = v6;
    a3 = (unsigned int)(a3 * 7 / 5) + 7;
    v3 = a0 - 8;
    v2 = a1 - 8;
    for (i = 0; i < 18; i += 1)
    {
        iter = 0;
        while (iter < 18)
        {
            v7 = i + v2;
            v8 = iter + v3;
            if (v7 >= 0xe)
            {
                iter += 1;
            }
            else if (v8 < 18)
            {
                v9 = *((char *)(i * 18 + iter + v1));
                if (v9)
                {
                    v7 = 0x90 * v7 + 8 * v8 + (char *)&g_10052785[0];
                    if (*((int *)v7) < 4294967294)
                    {
                        *((unsigned int *)v7) = *((int *)v7) + a3 * v9;
                        iter += 1;
                    }
                    else
                    {
                        iter += 1;
                    }
                }
                else
                {
                    iter += 1;
                }
            }
            else
            {
                iter += 1;
            }
        }
    }
    return v7;
}
```

## `sub_10011678` `0x10011678`

_375 bytes. (leaf/helper — see body)_

```c
extern int g_10052768;
extern int g_1005276c;

unsigned int sub_10011678(int a0, int a1, unsigned int a2)
{
    unsigned int v9;  // ebx
    int v10;  // eax
    int v19;  // ecx
    int v20;  // ecx
    int v21;  // eax
    int v11;  // eax
    int v12;  // eax
    int iter;  // esi
    int node;  // edi
    int v15;  // ecx
    unsigned int v16;  // eax
    int v17;  // esi
    int v18;  // edi
    unsigned int v0;  // [bp-0x30]
    unsigned int v1;  // [bp-0x2c]
    int v2;  // [bp-0x20]
    int v3;  // [bp-0x1c]
    int v4;  // [bp-0x18]
    int v5;  // [bp-0x14]
    int v6;  // [bp-0x10]
    unsigned int v7;  // [bp-0xc]
    unsigned int v8;  // [bp-0x8]

    v0 = v9;
    v10 = a0 - g_10052768;
    if (v10 < 40)
    {
        v8 = 1;
        v6 = v10;
    }
    else
    {
        v8 = 4294967295;
        v6 = ~(v6) + 1;
    }
    v11 = a1 - g_1005276c;
    if (v11 < 40)
    {
        v7 = 1;
        v5 = v11;
    }
    else
    {
        v7 = 4294967295;
        v5 = ~(v5) + 1;
    }
    v1 = 0;
    if (v6 != v5)
    {
        if (v8 == 1 && v7 == 4294967295)
        {
            if (v5 <= v6)
                v1 = 1;
        }
        else
        {
            if (v8 == 4294967295 && v7 == 4294967295)
            {
                v1 = 1;
            }
            else if (v8 == 4294967295 && v7 == 1 && v5 > v6)
            {
                v1 = 1;
            }
        }
    }
    if (v1)
    {
        v3 = a0;
        v2 = a1;
        v8 = ~(v8) + 1;
        v7 = ~(v7) + 1;
    }
    else
    {
        v3 = g_10052768;
        v2 = g_1005276c;
    }
    v12 = v6;
    if (v12 < v5)
        v12 = v5;
    v4 = v12;
    iter = 0;
    node = 0;
    v15 = 0;
    if (v1)
        v15 = -1;
    while (true)
    {
        if (a2)
        {
            v16 = *((char *)(a2 + (v2 - g_1005276c + 6) * 18 + v3 - g_10052768 + 8));
            v17 = iter;
            v18 = node;
            v19 = v15;
        }
        else
        {
            v16 = sub_1003c87c(v3, v2, v15, node, iter);
            v17 = v15;
            v18 = v2;
            v19 = v3;
        }
        v20 = v19;
        node = v18;
        iter = v17;
        if (v16)
            return 0;
        v15 = v20 + 1;
        if (v15 >= v4)
            return 1;
        iter += v6;
        node += v5;
        v21 = v4;
        if (iter >= v21)
        {
            iter -= v21;
            v3 += v8;
        }
        if (node >= v21)
        {
            node -= v21;
            v2 += v7;
        }
    }
}
```

## `sub_100117ef` `0x100117ef`

_333 bytes. (leaf/helper — see body)_

```c
unsigned int sub_100117ef(unsigned int a0, unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4)
{
    unsigned int v8;  // eax
    unsigned int v9;  // eax
    unsigned int v10;  // eax
    unsigned int iter;  // esi
    unsigned int node;  // edi
    unsigned int v13;  // ecx
    unsigned int v14;  // eax
    unsigned int v0;  // [bp-0x44]
    unsigned int i;  // [bp-0x40]
    unsigned int v2;  // [bp-0x3c]
    unsigned int v3;  // [bp-0x38]
    unsigned int v4;  // [bp-0x14]
    unsigned int v5;  // [bp-0x10]
    unsigned int v6;  // [bp-0xc]
    unsigned int v7;  // [bp-0x8]

    v8 = a3 - 3;
    if (v8 < 40)
    {
        v7 = 1;
        v5 = v8;
    }
    else
    {
        v7 = 4294967295;
        v5 = ~(v5) + 1;
    }
    v9 = a4 - 3;
    if (v9 < 40)
    {
        v6 = 1;
        v4 = v9;
    }
    else
    {
        v6 = 4294967295;
        v4 = ~(v4) + 1;
    }
    v3 = 0;
    if (v5 != v4)
    {
        if (v7 == 1 && v6 == 4294967295)
        {
            if (v4 <= v5)
                v3 = 1;
        }
        else
        {
            if (v7 == 4294967295 && v6 == 4294967295)
            {
                v3 = 1;
            }
            else if (v7 == 4294967295 && v6 == 1 && v4 > v5)
            {
                v3 = 1;
            }
        }
    }
    if (v3)
    {
        v2 = a0 + a3 - 3;
        i = a1 + a4 - 3;
        v7 = ~(v7) + 1;
        v6 = ~(v6) + 1;
    }
    else
    {
        v2 = a0;
        i = a1;
    }
    v10 = v5;
    if (v10 < v4)
        v10 = v4;
    v0 = v10;
    iter = 0;
    node = 0;
    v13 = 0;
    if (v3)
        v13 = 4294967295;
    for (; !*((char *)(a2 + i * 18 + v2)); i += v6)
    {
        v13 += 1;
        if (v13 >= v0)
            return 1;
        iter += v5;
        node += v4;
        v14 = v0;
        if (iter >= v14)
        {
            iter -= v14;
            v2 += v7;
        }
        if (node >= v14)
            node -= v14;
    }
    return 0;
}
```

