# YateBTS 2024

Everything to build and run the latest Yate + YateBTS + bladeRF xA4 for an old GSM 2G base station.

Yate 6.4.1 and YateBTS 6.1.1 use the latest bladeRF firmware and FPGA (tested with 2.4.0 and 0.15.3).

This build was tested on:
- Raspberry Pi 5
- bladeRF 2.0 micro xA4
- Raspberry Pi OS Bookworm (based on Debian 12 Bookworm), GCC-11, Apache2, PHP 5.6

Clone the repo and run `install.sh` as a user; you will be asked for your sudo password at some point.
Compilation takes approximately 10-15 minutes on a Raspberry Pi 5. The script will install all dependencies, compile sources, and install Apache2 + PHP 5.6 (if you choose the NiPC web interface).
