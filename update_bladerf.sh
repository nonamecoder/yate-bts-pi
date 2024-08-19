#!/bin/bash

wget -O hostedxA4-latest.rbf https://www.nuand.com/fpga/hostedxA4-latest.rbf
wget -O bladeRF_fw_latest.img https://www.nuand.com/fx3/bladeRF_fw_latest.img

if [ -f "hostedxA4-latest.rbf" ]; then
    bladeRF-cli -L hostedxA4-latest.rbf
else
    echo "FPGA file is not present"
fi

if [ -f "hostedxA4-latest.rbf" ]; then
    bladeRF-cli -f bladeRF_fw_latest.img
else
    echo "Firmware file is not present"
fi
