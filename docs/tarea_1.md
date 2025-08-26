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
| Periferícos          |                         |                      |                   |                   |
| Memoria              |Flash: 512 KB/RAM: 128 KB|RAM: 4 MB/SRAM: 520 KB|Flash: 1984 KB/RAM: 1024 KB/EEPROM: 1 KB|Flash: 8 KB/SRAM: 512 KB/EEPROM: 512KB               |
| Ecosistema           |                         |                      |                   |               |
| Costos               |$98MXN-$104MXN|$118.10MXN-$302.29MXN|$614.57MXN-$1165MXN|$87MXN-$110MXN|
| Arquitectura         |ARM Cortex-M4(RISC)|Dual Cortex-M33/Hazard3|ARM Cortex-M7|RISC|
| Velocidad de trabajo |100 MHz|150 MHz            |600 MHz|20 MHz|