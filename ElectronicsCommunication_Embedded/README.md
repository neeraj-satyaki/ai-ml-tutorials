# Electronics & Communication + Embedded Systems

ECE topics tightly bound to CS — digital design, signals, comms, microcontrollers, embedded.

## Digital Logic
Boolean algebra, gates, combinational (adders, MUX, decoders, encoders), flip-flops/latches, sequential circuits, FSMs (Mealy/Moore), counters/shift registers, K-map + Quine-McCluskey minimization, hazards + timing.

## VLSI / Hardware Design
CMOS inverter, power (dynamic/leakage). RTL in Verilog/VHDL/SystemVerilog. Synthesis + STA. Place-and-route. SoC design, clock distribution. ASIC vs FPGA. Toolchains: Vivado, Quartus, Yosys/nextpnr. HDL simulation + testbench. UVM verification. DFT/DFM/DFY. Low-power design.

## Analog
Op-amps, filters (active/passive), oscillators, PLLs, ADCs/DACs (SAR, sigma-delta, flash, pipelined), comparators, biasing/bandgap, noise, LDOs, SMPS.

## Signal Processing
Sampling + Nyquist, quantization. Transforms: DFT/FFT, Z-transform. FIR/IIR filters, adaptive filters (LMS/RLS), multirate, wavelets, compressed sensing. DSP architectures (CMSIS-DSP).

## Communication Systems
**Modulation**: AM/FM/PM. **Digital**: ASK, FSK, PSK, QAM, OFDM. **Coding**: Hamming, Reed-Solomon, LDPC, Turbo, Convolutional, Polar. Source: Huffman, arithmetic. Shannon capacity. MIMO (spatial mux, beamforming). Cellular (3G→6G). WiFi (802.11 a/b/g/n/ac/ax/be=WiFi 7). BT Classic/LE/Mesh. Zigbee / Thread / Matter. LoRaWAN, NB-IoT, LTE-M. 5G NR (URLLC, eMBB, mMTC, slicing). Satellite (LEO / Starlink). RF propagation + fading.

## Microcontrollers / Microprocessors
8051, PIC, AVR, ARM Cortex-M (M0/M3/M4/M7/M33), ESP32/8266, RISC-V MCUs, STM32, nRF52, Raspberry Pi (app processor). NVIC interrupts, low-power modes, boot ROMs + bootloaders.

## Embedded Buses / Protocols
UART, SPI, I²C, I²S, CAN/CAN-FD, LIN, RS-232/485, USB (+ OTG, HID, MSC, CDC), Ethernet MII/RMII, 1-Wire, Modbus RTU/TCP, MQTT, CoAP, BLE GATT, OpenThread, Zigbee cluster.

## RTOS / Bare-Metal
Bare-metal super-loop vs interrupt-driven design. RTOS concepts: tasks, queues, semaphores, mutexes, event flags. FreeRTOS, Zephyr, ThreadX/AzureRTOS, Mbed OS, Contiki, TizenRT. Priority inversion + inheritance. Watchdog, stack analysis, static allocation.

## Sensors + Actuators
IMU (accel/gyro/mag), temperature/pressure/humidity/gas, proximity/ToF, image sensors (MIPI CSI), LIDAR/Radar/Ultrasonic, mic (I²S/PDM), GNSS. Motors (DC, stepper, BLDC, servo), encoders, PWM, H-bridge, FOC. Control: PID. Sensor fusion (Kalman, complementary filter).

## IoT + Edge AI
Architecture: device → edge → fog → cloud. TinyML (CMSIS-NN, TFLM), QAT, ONNX Runtime embedded, µTVM/Glow. Power budgeting. OTA (secure). Device identity (PKI, eSIM). Thread + Matter home protocols. Digital twin.

## PCB / Power Delivery
Schematic capture (KiCad, Altium, Eagle), layout, layer stack-up, high-speed routing + SI/PI, EMI/EMC, decoupling capacitor selection, power planes, PDN design. Debug: scopes, logic analyzers, JTAG/SWD.

## Books
- *Digital Design and Computer Architecture* — Harris & Harris.
- *CMOS VLSI Design* — Weste & Harris.
- *Understanding Digital Signal Processing* — Lyons.
- *Proakis — Digital Communications*.
- *Making Embedded Systems* — Elecia White.
- *Practical Electronics for Inventors* — Scherz & Monk.
