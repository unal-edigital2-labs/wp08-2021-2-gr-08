# W07_Entrega-_final
1. python3 buildSoCproject.py
2. djtgcfg prog -d Nexys4DDR -i 0 -f ./build/nexys4ddr/gateware/nexys4ddr.bit
3. cd firmware/
4. make all
5. sudo lxterm /dev/ttyUSB1 --kernel firmware.bin
