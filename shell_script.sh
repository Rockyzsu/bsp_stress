sudo ./tegraflash.py --bct bct_p2894.bct --bl cboot.bin.signed --cfg flash_t210_darcy_android_sdmmc.xml --odmdata 0x1296000 --bldtb tegra210-darcy-p2894-0050-a04-00.dtb --chip 0x21 --applet rcm_1_signed.rcm --nct ./nct.bin --cmd "read EKS EKS_bak.bin; read FCT fct_bak.bin; read NCT nct_bak.bin;secureflash; write FCT fct_bak.bin; write NCT nct_bak.bin; write EKS EKS_bak.bin; reboot;" --securedev

