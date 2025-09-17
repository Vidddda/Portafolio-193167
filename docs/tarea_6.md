# Alarmas aplicadas

## 1) Resumen

- **Nombre del proyecto:** _Alarmas aplicadas_  
- **Equipo:** _Carlos Ernesto Camacho Gonzalez y David López Ramírez_  
- **Curso:** _Sistemas Embebidos I_  
- **Fecha:** _16/09/2025_  
- **Descripción breve:** _Se configurarán cuatro alarmas para controlar LEDs a diferentes frecuencias y se -modificará el juego del Mini-Pong para ajustar su velocidad mediante botones sin usar la función "delay"._

---

## 2) Objetivos

- **General:** _Comprender y aplicar el uso de temporizadores mediante la implementación de alarmas._
- **Específicos:**
  - _Configurar y utilizar cuatro alarmas para controlar LEDs a diferentes frecuencias de manera independiente._
  - _Modificar el juego de Mini-Pong para ajustar su velocidad en tiempo real mediante botones._

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

### 1)  Cuatro alarmas

#### Función

Con dos botones (pull-up; presionado=0) para simular cada compuerta, se encienden tres LEDs que muestran en paralelo los resultados de AND, OR y XOR. 

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

<div style="display:flex; justify-content:center;">
    <img src="../recursos/imgs/Tarea_6/Secuencia_Alarmas_esq.png" alt="Esquemático para secuencia de LEDs" width="420">
</div>

#### Vídeo

<div style="display:flex; justify-content:center;">
  <video style="width:100%;" muted controls>
    <source src="../recursos/archivos/Tarea_6/Secuencia_Alarma.mp4" type="video/mp4">
  </video>
</div>

### 2) Mini-pong con velocidad variable

#### Función

Con ayuda de dos botones (BTN_J1 y BTN_J2) se controla la dirección de la "pelota" representada por un LED que se desplaza entre cinco posiciones. El juego inicia detenido y comienza cuando alguno de los jugadores presiona su botón. Si la pelota alcanza un extremo y no es golpeada, se activa un parpadeo en el LED del contrario para indicar el punto. Además, se implementaron botones (BTN_MÁS y BTN_MENOS) para aumentar o disminuir la velocidad del juego en tiempo real, así como un botón de reinicio y un antirrebote.

```bash

#include "pico/stdlib.h"
#include "hardware/irq.h"
#include "hardware/structs/timer.h"
#include "hardware/gpio.h"


#define BTN_J1 0   // Botón jugador izquierda
#define BTN_J2 1   // Botón jugador derecha
#define LED_J1 2   // LED indicador puntos J1
#define LED_J2 3   // LED indicador puntos J2
#define LED0 4     // Posición 0 de LED
#define LED1 5
#define LED2 6     // Centro de LEDs
#define LED3 7
#define LED4 8     // Posición 4 de LED
#define RESET 9    // Botón de reinicio

//  Botones NUEVOS 
#define BTN_MAS   10  // Subir velocidad
#define BTN_MENOS 11  // Bajar velocidad

//  Alarmas del timer
#define ALARMA_JUEGO_NUM  0  // tick de juego
#define ALARMA_PUNTO_NUM  1  // parpadeo de punto
#define IRQ_ALARMA_JUEGO  timer_hardware_alarm_get_irq_num(timer_hw, ALARMA_JUEGO_NUM)
#define IRQ_ALARMA_PUNTO  timer_hardware_alarm_get_irq_num(timer_hw, ALARMA_PUNTO_NUM)

//  Velocidades (ms) 
#define VEL_PELOTA 100
#define VEL_REBOTE 300

// Rango y paso de velocidad (us)
#define VEL_MIN_US        40000u
#define VEL_MAX_US       400000u
#define VEL_PASO_US       20000u   // salto entre us
#define ANTIRREBOTE_VEL_US 120000u // antirrebote para botones de velocidad

uint8_t POS = LED2;     // Pelota arranca en el centro
bool DIR = 1;           // 1 = derecha, 0 = izquierda
bool START = false;     // Juego detenido al inicio

volatile bool GOLPE_J1 = false;
volatile bool GOLPE_J2 = false;
volatile bool START_J1 = false;
volatile bool START_J2 = false;
volatile bool RESET_STATE = false;

//  Máscaras 
uint32_t LEDS_MASK;                   
static uint32_t MASCARA_LEDS_POS;     // solo LEDs de posición, no marca

//  Tiempo y tick 
static inline uint32_t microsegundos(void){ return timer_hw->timerawl; }
static volatile uint32_t VEL_PELOTA_US = (uint32_t)VEL_PELOTA * 1000u; // periodo del tick en µs
static volatile uint32_t PROXIMO_TICK_US = 0;
static volatile uint32_t ULTIMO_CAMBIO_VEL_US = 0; // antirrebote de BTN_MAS/BTN_MENOS

//  Ventana de rebote fija en tiempo 
#define REBOTE_US ((uint32_t)VEL_REBOTE * 1000u)
static volatile bool EN_PARED = false;
static volatile uint32_t VENTANA_HASTA_US = 0;

//  Parpadeo no bloqueante (ALARMA_PUNTO)
static volatile bool PARPADEO_ACTIVO = false;
static volatile uint8_t  PIN_LED_PARPADEO = 0;
static volatile uint8_t  PARPADEOS_RESTANTES = 0;
static volatile uint32_t PROXIMO_PARPADEO_US = 0;
#define PARPADEO_MEDIO_US 200000u // 200 ms ON/OFF

//  Prototipos requeridos 
static void PONG(uint PIN, uint32_t EVENT_MASK);
void BLINK(uint8_t LED);
void REINICIAR();
void MOVER_PELOTA(void);

// ---- ISRs de alarmas 
static void irq_alarma_juego(void){
    hw_clear_bits(&timer_hw->intr, 1u << ALARMA_JUEGO_NUM);
    MOVER_PELOTA();
    PROXIMO_TICK_US += VEL_PELOTA_US;
    timer_hw->alarm[ALARMA_JUEGO_NUM] = PROXIMO_TICK_US;
}

static void irq_alarma_punto(void){
    hw_clear_bits(&timer_hw->intr, 1u << ALARMA_PUNTO_NUM);

    if (!PARPADEO_ACTIVO || PARPADEOS_RESTANTES == 0){
        gpio_put(PIN_LED_PARPADEO, 0);
        PARPADEO_ACTIVO = false;
        return;
    }
    sio_hw->gpio_togl = (1u << PIN_LED_PARPADEO);
    PARPADEOS_RESTANTES--;
    PROXIMO_PARPADEO_US += PARPADEO_MEDIO_US;
    timer_hw->alarm[ALARMA_PUNTO_NUM] = PROXIMO_PARPADEO_US;
}

int main() {
    // LEDs
    LEDS_MASK = (1u << LED_J1) | (1u << LED_J2) | (1u << LED0) | (1u << LED1) |
                (1u << LED2) | (1u << LED3) | (1u << LED4);
    MASCARA_LEDS_POS = (1u << LED0) | (1u << LED1) | (1u << LED2) | (1u << LED3) | (1u << LED4);

    gpio_init_mask(LEDS_MASK);
    gpio_set_dir_masked(LEDS_MASK, LEDS_MASK);
    gpio_clr_mask(LEDS_MASK);

    // Botones 
    gpio_init(BTN_J1);   gpio_set_dir(BTN_J1, GPIO_IN);   gpio_pull_up(BTN_J1);
    gpio_init(BTN_J2);   gpio_set_dir(BTN_J2, GPIO_IN);   gpio_pull_up(BTN_J2);
    gpio_init(RESET);    gpio_set_dir(RESET,  GPIO_IN);   gpio_pull_up(RESET);
    gpio_init(BTN_MAS);  gpio_set_dir(BTN_MAS, GPIO_IN);  gpio_pull_up(BTN_MAS);
    gpio_init(BTN_MENOS);gpio_set_dir(BTN_MENOS, GPIO_IN);gpio_pull_up(BTN_MENOS);

    gpio_set_mask(1u << POS); // LED inicial en centro

    // IRQ GPIO por flanco de bajada 
    gpio_set_irq_enabled_with_callback(BTN_J1, GPIO_IRQ_EDGE_FALL, true, &PONG);
    gpio_set_irq_enabled(BTN_J2,   GPIO_IRQ_EDGE_FALL, true);
    gpio_set_irq_enabled(RESET,    GPIO_IRQ_EDGE_FALL, true);
    gpio_set_irq_enabled(BTN_MAS,  GPIO_IRQ_EDGE_FALL, true);
    gpio_set_irq_enabled(BTN_MENOS,GPIO_IRQ_EDGE_FALL, true);

    // Timer de sistema en µs
    timer_hw->source = 0u;
    uint32_t ahora = microsegundos();

    // Programa ALARMA_JUEGO (primer tick)
    PROXIMO_TICK_US = ahora + VEL_PELOTA_US;
    timer_hw->alarm[ALARMA_JUEGO_NUM] = PROXIMO_TICK_US;

    // Limpia flags, registra handlers y habilita
    hw_clear_bits(&timer_hw->intr, (1u << ALARMA_JUEGO_NUM) | (1u << ALARMA_PUNTO_NUM));
    irq_set_exclusive_handler(IRQ_ALARMA_JUEGO,  irq_alarma_juego);
    irq_set_exclusive_handler(IRQ_ALARMA_PUNTO,  irq_alarma_punto);
    hw_set_bits(&timer_hw->inte, (1u << ALARMA_JUEGO_NUM) | (1u << ALARMA_PUNTO_NUM));
    irq_set_enabled(IRQ_ALARMA_JUEGO,  true);
    irq_set_enabled(IRQ_ALARMA_PUNTO,  true);

    while (true) { tight_loop_contents(); }
}

// ---- ISR GPIO 
static void PONG(uint PIN, uint32_t EVENT_MASK) {
    if (EVENT_MASK & GPIO_IRQ_EDGE_FALL) {
        if (PIN == BTN_J1) {
            if (!START) START_J1 = true;
            else if (POS == LED0) GOLPE_J1 = true;
        } else if (PIN == BTN_J2) {
            if (!START) START_J2 = true;
            else if (POS == LED4) GOLPE_J2 = true;
        } else if (PIN == RESET) {
            RESET_STATE = true;
        } else if (PIN == BTN_MAS || PIN == BTN_MENOS) {
            uint32_t t = microsegundos();
            // antirrebote botones de velocidad
            if ((int32_t)(t - ULTIMO_CAMBIO_VEL_US) > (int32_t)ANTIRREBOTE_VEL_US) {
                if (PIN == BTN_MAS) {
                    // más rápido = menor periodo
                    if (VEL_PELOTA_US > VEL_MIN_US + VEL_PASO_US - 1) VEL_PELOTA_US -= VEL_PASO_US;
                    else VEL_PELOTA_US = VEL_MIN_US;
                } else {
                    // más lento = mayor periodo
                    if (VEL_PELOTA_US < VEL_MAX_US - VEL_PASO_US + 1) VEL_PELOTA_US += VEL_PASO_US;
                    else VEL_PELOTA_US = VEL_MAX_US;
                }
                // re-alinear próximo tick para notar el cambio de inmediato
                PROXIMO_TICK_US = t + VEL_PELOTA_US;
                timer_hw->alarm[ALARMA_JUEGO_NUM] = PROXIMO_TICK_US;
                ULTIMO_CAMBIO_VEL_US = t;
            }
        }
    }
    gpio_acknowledge_irq(PIN, EVENT_MASK);
}

//  BLINK del original: ahora inicia parpadeo no bloqueante
void BLINK(uint8_t LED) {
    PIN_LED_PARPADEO = LED;
    PARPADEOS_RESTANTES = 6; // 3 destellos ON/OFF
    gpio_put(PIN_LED_PARPADEO, 0);
    PARPADEO_ACTIVO = true;
    PROXIMO_PARPADEO_US = microsegundos() + PARPADEO_MEDIO_US;
    timer_hw->alarm[ALARMA_PUNTO_NUM] = PROXIMO_PARPADEO_US;
}

void REINICIAR() {
    POS = LED2;
    START = false;
    GOLPE_J1 = false;
    GOLPE_J2 = false;
    START_J1 = false;
    START_J2 = false;
    EN_PARED = false;
    PARPADEO_ACTIVO = false;
    gpio_put(LED_J1, 0);
    gpio_put(LED_J2, 0);
    gpio_clr_mask(MASCARA_LEDS_POS);
    gpio_set_mask(1u << POS); // LED centro
}

void MOVER_PELOTA() {
    uint32_t tnow = microsegundos();

    if (RESET_STATE) {
        REINICIAR();
        RESET_STATE = false;
        return;
    }

    if (!START) {
        if (START_J1) { DIR = 1; START = true; START_J1 = false; }
        else if (START_J2) { DIR = 0; START = true; START_J2 = false; }
        gpio_set_mask(1u << POS); // LED centro
        return;
    }

    // Ventana fija cuando está en pared
    if (EN_PARED) {
        if ((int32_t)(tnow - VENTANA_HASTA_US) >= 0) {
            if (POS == LED0) {
                if (GOLPE_J1) { DIR = 1; }
                else { BLINK(LED_J2); POS = LED2; DIR = 1; START = true; }
                GOLPE_J1 = false;
            } else if (POS == LED4) {
                if (GOLPE_J2) { DIR = 0; }
                else { BLINK(LED_J1); POS = LED2; DIR = 0; START = true; }
                GOLPE_J2 = false;
            }
            EN_PARED = false;
            gpio_clr_mask(MASCARA_LEDS_POS);
            gpio_set_mask(1u << POS);
        }
        return; // mientras dura la ventana no se mueve
    }

    // Mover pelota 1 paso
    if (DIR && POS < LED4) POS++;
    else if (!DIR && POS > LED0) POS--;

    // Si llegó a pared, abrir ventana
    if (POS == LED0 || POS == LED4) {
        EN_PARED = true;
        VENTANA_HASTA_US = tnow + REBOTE_US;
    }

    gpio_clr_mask(MASCARA_LEDS_POS);
    gpio_set_mask(1u << POS);
}

```


#### Esquemático de conexión

<div style="display:flex; justify-content:center;">
    <img src="../recursos/imgs/Tarea_6/Mini_Pong_Alarmas_esq.png" alt="Esquemático para Mini-Pong con velocidad variable" width="420">
</div>

#### Vídeo

<div style="display:flex; justify-content:center;">
  <video style="width:100%; max-width:300px;" muted controls>
    <source src="../recursos/archivos/Tarea_6/Pong_alarma.mp4" type="video/mp4">
  </video>
</div>