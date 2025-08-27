# Comparación de microcontroladores

## 1) Resumen

- **Nombre de la actividad:** _Comparación de microcontroladores_
- **Autor:** _David López Ramírez_  
- **Curso:** _Sistemas Embebidos I_
- **Fecha:** _25/08/2025_  
- **Descripción breve:** _Los microcontroladores son dispositivos que integran CPU, memoria y periféricos, diseñados para controlar sistemas embebidos. Cuentan con RAM para datos temporales y Flash para almacenar programas de forma permanente. Entre sus periféricos destacan temporizadores, conversores ADC y módulos de comunicación como UART o I2C. Pueden ser de 8, 16 o 32 bits, con frecuencias que determinan su rendimiento. Su costo y disponibilidad varían, desde opciones económicas para prototipos hasta modelos avanzados para aplicaciones profesionales._


## 2) Objetivos

- **General:** _Comparar los diferentes microcontroladores, destacando el uso de cada uno de ellos para un área aplicable_


## 3) Desarrollo

| Microcontrolador     | STM32F411               | Raspberry Pi Pico 2  | Teensy 4.0        | ATTINY85-20PU     |
|---------------------:|:-----------------------:|:--------------------:|:---------------- :|-------------------|
| Periferícos          |Cortex-M4 @ 100 MHz; USB OTG FS; UART × 3; SPI × 5; I²C × 3; I²S × 5 (2 full-duplex); CAN × 3 (1 con CAN FD); 11 Timers (6 de 16 bits, 2 de 32 bits, 1 PWM); ADC de 12 bits; RTC; DMA × 32; Criptografía acelerada; Batch Acquisition Mode (BAM); Flexibility Matrix para interconexión de periféricos|Timers de 8 bits con 4 alarmas + AON Timer; UART × 2; SPI × 2; I²C × 2; PWM × 24 canales; USB 1.1 (host/dev); ADC 12 bits; PIO × 3 (12 state machines); sensor de temperatura|Pines: 40 digitales, 31 PMW, 14 analógicos; Puertos: 7 serial, 3 SPI, 3 I2C; Puertos de audio: 2 I2S/TDM, 1 S/DIF; Buses: 3 CAN (1 CAN FD); 32 canales DMA; Aceleración criptográfica y generador de números aleatorios; RTC para fecha/hora; FlexIO programable|Timers 8 bits + PWM; PWM alta frecuencia; USI; ADC 10 bits (single/diferencial); Watchdog; Comparador analógico|
| Memoria              |Flash: 512 KB/RAM: 128 KB|RAM: 4 MB/SRAM: 520 KB|Flash: 1984 KB/RAM: 1024 KB/EEPROM: 1 KB/Caché: 32 KB|Flash: 8 KB/SRAM: 512 B/EEPROM: 512 B|
| Ecosistema           |STM32CubeIDE; Keil MDK; IAR Embedded Workbench; PlatformIO; GCC ARM; STM32CubeMX; HAL/LL; Middleware USB/TCP/IP/FATFS/FreeRTOS; ST-Link; SWD/JTAG; Nucleo/Discovery; FreeRTOS/Zephyr/Mbed OS|Raspberry Pi SDK (C/C++); MicroPython; Thonny IDE; Visual Studio Code/PlatformIO; USB Bootloader integrado; SWD Debug|Arduino IDE + Teensyduino; Visual Micro; PlatformIO; CircuitPython; Línea de comandos con Makefile|AVR-GCC; Assembly AVR; Core de Arduino; AVRISP mkII; USBasp; TinyUSB|
| Costos               |$98MXN-$104MXN|$118.10MXN-$302.29MXN|$614.57MXN-$1165MXN|$87MXN-$110MXN|
| Arquitectura         |ARM Cortex-M4(RISC)|Dual Cortex-M33/Hazard3|ARM Cortex-M7|RISC|
| Velocidad de trabajo |100 MHz|150 MHz            |600 MHz|20 MHz|

### Raking de microcontroladores para micromouse

#### 1) Raspberry Pi Pico 2
- **Ventajas:** 
    * 150 MHz dual-core, 512 KB RAM.
    * Fácil de programar (C/C++ o MicroPython).
    * Muy barato y accesible.

- **Desventajas:** 
    * FPU menos avanzado.
    * Periféricos menos potentes que STM32.

#### 2) STM32F411
- **Ventajas:** 
    * 100 MHz, ARM Cortex-M4 con FPU.
    * ADC rápidos, timers avanzados, periféricos completos.
    * Ecosistema profesional.

- **Desventajas:** 
    * Programación más compleja.
    * Requiere programador externo.

#### 3) Teensy 4.0
- **Ventajas:** 
    * 600 MHz, ARM Cortex-M7, FPU y DSP.
    * Enorme potencia de cálculo.
    * Diversas opciones de programación.

- **Desventajas:** 
    * Caro.
    * Mucha potencia para un micromouse.
    * Mayor consumo.

#### 4) ATtiny85-20PU
- **Ventajas:** 
    * Barato y sencillo.
    * Bajo consumo.

- **Desventajas:** 
    * Solo 20 MHz, 512 B RAM.
    * Muy limitado en sensores, control y algoritmos.


## 4) Referencias

“Teensy® 4.0”. PJRC: Electronic Projects. Accedido el 27 de agosto de 2025. [En línea]. Disponible: [https://www.pjrc.com/store/teensy40.html](https://www.pjrc.com/store/teensy40.html)

“Attiny85-20pu pdf”. ALLDATASHEET.COM - Electronic Parts Datasheet Search. Accedido el 27 de agosto de 2025. [En línea]. Disponible: [https://www.alldatasheet.com/datasheet-pdf/view/163120/ATMEL/ATTINY85-20PU.html](https://www.alldatasheet.com/datasheet-pdf/view/163120/ATMEL/ATTINY85-20PU.html)

Raspberry Pi Datasheets. Accedido el 27 de agosto de 2025. [En línea]. Disponible: [https://datasheets.raspberrypi.com/pico/pico-2-datasheet.pdf](https://datasheets.raspberrypi.com/pico/pico-2-datasheet.pdf)

“Stm32f411 pdf”. ALLDATASHEET.COM - Electronic Parts Datasheet Search. Accedido el 27 de agosto de 2025. [En línea]. Disponible: [https://www.alldatasheet.com/datasheet-pdf/view/1179070/STMICROELECTRONICS/STM32F411.html](https://www.alldatasheet.com/datasheet-pdf/view/1179070/STMICROELECTRONICS/STM32F411.html)