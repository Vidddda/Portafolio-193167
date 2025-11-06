# Modulación por ancho de pulso - PWM

## 1) Resumen

- **Nombre del proyecto:** _Control ADC_  
- **Equipo:** _Carlos Ernesto Camacho Gonzalez, David López Ramírez, Rodrigo Miranda Flores y Luis Javier Vega Tello_  
- **Curso:** _Sistemas Embebidos I_  
- **Fecha:** _06/11/2025_  
- **Descripción breve:** _Control ADC_

---

## 2) Objetivos

- **General:** _Comprender el conversor analógico a digital._

## 3) Requisitos

**Software**
- _Visual Studio Code (Lenguaje de programación C)_

**Hardware**
- _Raspberry Pi Pico 2 RP2350_

**Conocimientos previos**
- _Programación básica en C_
- _Electrónica básica_
---

## 4) Desarrollo

### 1)  ADC Luxometro

#### Función
Con ayuda de unn código se marca la luminosidad de 0-100% usando un LDR.
#### Código
```bash

#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/adc.h"
 
// Configurar el canal ADC a usar
#define ADC_INPUT 0 // canal 0
 
#define ADC_MIN 850    // valor cuando tapas la LDR
#define ADC_MAX 3100   // valor con luz máxima
 
int main() {
    stdio_init_all();
    adc_init();
    // Configura el pin GPIO correspondiente como entrada ADC
    adc_gpio_init(26); // GPIO26 suele mapear a ADC0 en Pico 2
    // Seleccionar canal
    adc_select_input(ADC_INPUT);
 
    while (true) {
        uint16_t adc = adc_read(); // 12 bits alineados a 0..4095
 
        if (adc < ADC_MIN) adc = ADC_MIN;
        if (adc > ADC_MAX) adc = ADC_MAX;
 
        // Calcular porcentaje de luz 0–100
        float luz = (adc - ADC_MIN) * 100.0f / (ADC_MAX - ADC_MIN);
 
        printf("ADC: %u\tLuz: %.1f%%\n", adc, luz);
        sleep_ms(200);
    }
}

```
#### Esquemático de conexión

<img src="../recursos/imgs/Tarea_9/Esq_LDR.jpg" alt="Esquemático para luxometro" width="420">

#### Vídeo

[https://www.youtube.com/shorts/VtgWAUczVmI](https://www.youtube.com/shorts/VtgWAUczVmI)


### 2) Servo con ADC

#### Función
Se crea un código para mover un servo usando un potenciometro y un adc que vaya 0-180 grados

```bash

#include <iostream>
#include "pico/stdlib.h"
#include "hardware/adc.h"
#include "hardware/pwm.h"
 
using namespace std;
 
#define SERVO_PIN 0    
#define POT_PIN 26      
 
int main() {
    stdio_init_all();
 
   //inicializar ADC
    adc_init();
    adc_gpio_init(POT_PIN);
    adc_select_input(0);
    adc_set_clkdiv(479.0f);          
    adc_fifo_setup(true, false, 1, false, false);  
    adc_fifo_drain();                
    adc_run(true);                    
 
   //inicializar PWM para el servo
    gpio_set_function(SERVO_PIN, GPIO_FUNC_PWM);
    uint slice_num = pwm_gpio_to_slice_num(SERVO_PIN); //aplicar configuracion al slice
 
    pwm_set_clkdiv(slice_num, 64.0f);
    pwm_set_wrap(slice_num, 39062);  
//ajustar frecuencia del pwm
    pwm_set_enabled(slice_num, true);
 
    while (true) {
 
        if (adc_fifo_get_level() > 0) { //para ver si hay algo dentro del fifo
            uint16_t valor_adc = adc_fifo_get();
 
 
            float duty = 0.025f + (valor_adc / 4095.0f) * 0.1f;
 
            pwm_set_gpio_level(SERVO_PIN, duty * 39062);
 
 
        }
 
        sleep_ms(20);
    }
 
    return 0;
}

```

#### Esquemático de conexión

<div style="display:flex; justify-content:center;">
    <img src="../recursos/imgs/Tarea_9/Esq_servo.jpg" alt="Esquemático para Servo" width="420">
</div>

#### Vídeo

[https://www.youtube.com/shorts/L8Vw-Pges6I](https://www.youtube.com/shorts/L8Vw-Pges6I)
