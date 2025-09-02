# Outpus básicos

## 1) Resumen

- **Nombre del proyecto:** _Inputs_  
- **Equipo:** _Carlos Ernesto Camacho Gonzalez y David López Ramírez_  
- **Curso:** _Sistemas Embebidos I_  
- **Fecha:** _01/09/2025_  
- **Descripción breve:** _Introducción a la programación de entradas para el microcontrolador Raspberry Pi Pico 2 RP2350. Se presentan dos códigos básicos que leen botones para representar salidas en forma de LEDs._

---

## 2) Objetivos

- **General:** _Comprender la programación básica para la configuración de entradas._
- **Específicos:**
  - _Entender las funciones de básicas de programación en C para establecer entradas._

## 4) Requisitos

**Software**
- _Visual Studio Code (Lenguaje de programación C)_

**Hardware**
- _Raspberry Pi Pico 2 RP2350_

**Conocimientos previos**
- _Programación básica en C_
- _Electrónica básica_
---

## 5) Desarrollo

### 1)  Compuertas básicas AND / OR / XOR con 2 botones

#### Función

#### Código
```bash

#include "pico/stdlib.h"

// Pines AND
#define BTN_A 0      
#define BTN_B 1    
#define LED0   6
// Pines OR
#define BTN_C 2     
#define BTN_D 3    
#define LED1   7
// Pines XOR
#define BTN_E 4      
#define BTN_F 5    
#define LED2   8

bool AND() {
    bool A_PRESS = !gpio_get(BTN_A);
    bool B_PRESS = !gpio_get(BTN_B);
    return (A_PRESS && B_PRESS);
}

bool OR() {
    bool C_PRESS = !gpio_get(BTN_C);
    bool D_PRESS = !gpio_get(BTN_D);
    return (C_PRESS || D_PRESS);
}

bool XOR() {
    bool E_PRESS = !gpio_get(BTN_E);
    bool F_PRESS = !gpio_get(BTN_F);
    return (E_PRESS ^ F_PRESS);
}

int main(void) {
    // Inicialización pines AND
    gpio_init(LED0);
    gpio_set_dir(LED0, GPIO_OUT);

    gpio_init(BTN_A);
    gpio_set_dir(BTN_A, GPIO_IN);
    gpio_pull_up(BTN_A);

    gpio_init(BTN_B);
    gpio_set_dir(BTN_B, GPIO_IN);
    gpio_pull_up(BTN_B);

    // Inicialización pines OR
    gpio_init(LED1);
    gpio_set_dir(LED1, GPIO_OUT);

    gpio_init(BTN_C);
    gpio_set_dir(BTN_C, GPIO_IN);
    gpio_pull_up(BTN_C);

    gpio_init(BTN_D);
    gpio_set_dir(BTN_D, GPIO_IN);
    gpio_pull_up(BTN_D);

    // Inicialización pines XOR
    gpio_init(LED2);
    gpio_set_dir(LED2, GPIO_OUT);

    gpio_init(BTN_E);
    gpio_set_dir(BTN_E, GPIO_IN);
    gpio_pull_up(BTN_E);

    gpio_init(BTN_F);
    gpio_set_dir(BTN_F, GPIO_IN);
    gpio_pull_up(BTN_F);

    while (true) {
        // Función AND
        if (AND())  gpio_put(LED0, 1);
        else        gpio_put(LED0, 0);

        // Función OR
        if (OR())   gpio_put(LED1, 1);
        else        gpio_put(LED1, 0);

        // Función XOR
        if (XOR())  gpio_put(LED2, 1);
        else        gpio_put(LED2, 0);

        sleep_ms(10);
    }
}

```
#### Esquemático de conexión

<img src="../recursos/imgs/Tarea_2/Contador_binario_esq.png" alt="Esquemático para contador de 4 bits" width="420">

#### Vídeo

<video style="width:30%" muted="" controls="" alt="type:video">
   <source src="../recursos/archivos/Tarea_2/Contador_binario.mp4" type="video/mp4">
   </video>

### 2) Selector cíclico de 4 LEDs con avance/retroceso

#### Función

```bash

#include "pico/stdlib.h"

#define BTN_PREV 0      
#define BTN_NEXT 1    
#define LED0   2
#define LED1   3
#define LED2   4
#define LED3   5

uint8_t STATE = LED0 - 1;

int main(void) {
    const uint8_t LEDs_M = (1u << LED0 | 1u << LED1 | 1u << LED2 | 1u << LED3);

    gpio_init_mask(LEDs_M);
    gpio_set_dir_out_masked(LEDs_M);
    gpio_set_mask(LEDs_M);   
    gpio_clr_mask(LEDs_M);
    
    gpio_init(BTN_PREV);
    gpio_set_dir(BTN_PREV, GPIO_IN);
    gpio_pull_up(BTN_PREV);

    gpio_init(BTN_NEXT);
    gpio_set_dir(BTN_NEXT, GPIO_IN);
    gpio_pull_up(BTN_NEXT);

    bool NEXT_PREVSTATE = 1;
    bool PREV_PREVSTATE = 1;

    while (true) {
        bool NEXT_STATE = !gpio_get(BTN_NEXT);
        bool PREV_STATE = !gpio_get(BTN_PREV);

        // Siguiente LED
        if (NEXT_STATE && !NEXT_PREVSTATE) {
            if (STATE == LED3) {
                STATE = LED0;
            } else {
                STATE ++;
            }
            gpio_clr_mask(LEDs_M);                
            gpio_set_mask(1 << STATE);              
        }

        // Anterior LED
        if (PREV_STATE && !PREV_PREVSTATE) {
            if (STATE == LED0) {
                STATE = LED3;
            } else {
                STATE --;
            }
            gpio_clr_mask(LEDs_M);                
            gpio_set_mask(1 << STATE);              
        }

        NEXT_PREVSTATE = NEXT_STATE;
        PREV_PREVSTATE = PREV_STATE;

        sleep_ms(10);
    }
}

```


#### Esquemático de conexión

<img src="../recursos/imgs/Tarea_2/Barrido_esq.png" alt="Esquemático para Barrido de 5 LEDs" width="420">

#### Vídeo

<video style="width:30%" muted="" controls="" alt="type:video">
   <source src="../recursos/archivos/Tarea_2/Barrido_LEDs.mp4" type="video/mp4">
   </video>
