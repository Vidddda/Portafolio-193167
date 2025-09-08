# Mini-Pong

## 1) Resumen

- **Nombre del proyecto:** _Mini-Pong_  
- **Equipo:** _Carlos Ernesto Camacho Gonzalez y David López Ramírez_  
- **Curso:** _Sistemas Embebidos I_  
- **Fecha:** _07/09/2025_  
- **Descripción breve:** _Se elabora un mini-Pong para entender mejor el funcionamiento de las interrupciones._

---
## 2) Objetivos

- **General:** _Comprender la programación básica para la configuración de interrupciones._

## 3) Requisitos

**Software**
- _Visual Studio Code (Lenguaje de programación C)_

**Hardware**
- _Raspberry Pi Pico 2 RP2350_

**Conocimientos previos**
- _Programación básica en C_
- _Electrónica básica_
---

## 4) Desarrollo del Mini-Pong 

### Función

Se trata de un mini-Pong con 5 LEDs en línea y 2 botones, programados como interrupciones (ISR) para simular la "raqueta" del jugador exactamente cuando la "pelota" (un LED encendido) llega al extremo de su lado.

!!! note "Reglas del juego"

    * *Pelota:* es un único LED encendido que se mueve automáticamente de un extremo al otro (LED0→LED4→LED0…) a un ritmo fijo.

    * *Golpe (con ISR):* cada botón genera una interrupción.

        * El *BTN_J1* solo cuenta si, en el instante de la ISR, la pelota está en LED0.

        * El *BTN_J2* solo cuenta si, en el instante de la ISR, la pelota está en LED4.

        * Si *coincide*, la *pelota* rebota (invierte su dirección).

        * Si *no* coincide (la pelota no está en el último LED de ese lado), el botón se ignora.

    * *Fallo y punto:* si la pelota *alcanza LED0* y *no hubo golpe válido* del lado izquierdo en ese momento, *anota el jugador derecho*. Análogamente, si alcanza *LED4* sin golpe válido, *anota el jugador izquierdo*.

    * *Indicador de punto:* al anotar, se *parpadea el LED de punto 3 veces* del jugador que metió el punto (LED_J1 o LED_J2).

    * *Reinicio tras punto:* después del parpadeo, la pelota se reinicia en el centro (LED2) y comienza a moverse hacia el jugador que metió el punto.

    * *Inicio del juego:* al encender, la pelota inicia en LED2 y no se mueve hasta que se presione un botón y deberá moverse a la direccion opuesta del boton presionado.

### Código

```python
#include "pico/stdlib.h"

//Definición de PINes
#define BTN_J1 0   //Botón jugador izquierda
#define BTN_J2 1   //Botón jugador derecha
#define LED_J1 2   //LED indicador puntos J1
#define LED_J2 3   //LED indicador puntos J2
#define LED0 4     //Posición 0 de LED
#define LED1 5
#define LED2 6     //Centro de LEDs
#define LED3 7
#define LED4 8     //Posición 4 de LED
#define RESET 9    //Botón de reinicio

//Velocidades (ms)
#define VEL_PELOTA 100
#define VEL_REBOTE 300

//Variables globales
uint8_t POS = LED2;     //Pelota arranca en el centro
bool DIR = 1;           //1 = derecha, 0 = izquierda
bool START = false;     //Juego detenido al inicio

//Estados de interrupción
volatile bool GOLPE_J1 = false;
volatile bool GOLPE_J2 = false;
volatile bool START_J1 = false;
volatile bool START_J2 = false;
volatile bool RESET_STATE = false;

//Establece máscara de LEDs como global
uint32_t LEDS_MASK;

//Llamada de ISR
static void PONG(uint PIN, uint32_t EVENT_MASK);

//Llamada de BLINK
void BLINK(uint8_t LED);

//Llamada de REINICIAR
void REINICIAR();

//Llamada de MOVER_PELOTA
void MOVER_PELOTA();

int main() {
    //Inicialización de LEDs
    LEDS_MASK = (1u << LED_J1) | (1u << LED_J2) | (1u << LED0) | (1u << LED1) |(1u << LED2) | (1u << LED3) | (1u << LED4);

    gpio_init_mask(LEDS_MASK);
    gpio_set_dir_masked(LEDS_MASK, LEDS_MASK);
    gpio_clr_mask(LEDS_MASK);

    //Inicialización de botones
    gpio_init(BTN_J1);
    gpio_set_dir(BTN_J1, GPIO_IN);
    gpio_pull_up(BTN_J1);

    gpio_init(BTN_J2);
    gpio_set_dir(BTN_J2, GPIO_IN);
    gpio_pull_up(BTN_J2);

    gpio_init(RESET);
    gpio_set_dir(RESET, GPIO_IN);
    gpio_pull_up(RESET);

    gpio_set_mask(1u << POS); //LED inicial en centro

    //Habilitar IRQ por flanco de bajada
    gpio_set_irq_enabled_with_callback(BTN_J1, GPIO_IRQ_EDGE_FALL, true, &PONG);
    gpio_set_irq_enabled(BTN_J2, GPIO_IRQ_EDGE_FALL, true);
    gpio_set_irq_enabled(RESET, GPIO_IRQ_EDGE_FALL, true);

    while (true) {
        MOVER_PELOTA();
        sleep_ms(VEL_PELOTA);
    }
}

//ISR: activa rebote si la pelota está en el extremo o inicio de juego
static void PONG(uint PIN, uint32_t EVENT_MASK) {
    if (EVENT_MASK & GPIO_IRQ_EDGE_FALL) {
        if (PIN == BTN_J1) {
            if (!START) START_J1 = true;       //Arranque inicial
            else if (POS == LED0) GOLPE_J1 = true; //Rebote válido extremo izquierdo
        } else if (PIN == BTN_J2) {
            if (!START) START_J2 = true;       //Arranque inicial
            else if (POS == LED4) GOLPE_J2 = true; //Rebote válido extremo derecho
        } else if (PIN == RESET) {
            RESET_STATE = true;                   //Activar reinicio
        }
    }
    gpio_acknowledge_irq(PIN, EVENT_MASK);
}

void BLINK(uint8_t LED) {
    for (int i = 0; i < 3; i++) {
        gpio_put(LED, 1);
        sleep_ms(200);
        gpio_put(LED, 0);
        sleep_ms(200);
    }
}

void REINICIAR() {
    POS = LED2;
    START = false;
    GOLPE_J1 = false;
    GOLPE_J2 = false;
    START_J1 = false;
    START_J2 = false;
    gpio_clr_mask(LEDS_MASK);
    gpio_set_mask(1 << POS); //LED centro
}

void MOVER_PELOTA() {
    //Chequear reinicio
    if (RESET_STATE) {
        REINICIAR();
        RESET_STATE = false;
        return;
    }

    //Inicio del juego
    if (!START) {
        if (START_J1) { 
            DIR = 1;      //Hacia la derecha (opuesto al botón)
            START = true;
            START_J1 = false;
        } else if (START_J2) {
            DIR = 0;      //Hacia la izquierda
            START = true;
            START_J2 = false;
        }
        gpio_set_mask(1u << POS); //LED centro
        return;
    }

    //Mover pelota
    if (DIR && POS < LED4) POS++;
    else if (!DIR && POS > LED0) POS--;

    //Rebote o punto
    if (POS == LED0) {
        gpio_clr_mask(LEDS_MASK);
        gpio_set_mask(1 << POS);
        sleep_ms(VEL_REBOTE);
        if (GOLPE_J1) {
            DIR = 1; //Rebote válido
        } else {
            BLINK(LED_J2); //Punto jugador derecho
            POS = LED2;         //Reinicio al centro
            DIR = 1;            //Dirección hacia jugador que anotó
            START = true;     //Continuar movimiento automáticamente
        }
        GOLPE_J1 = false;
    } else if (POS == LED4) {
        gpio_clr_mask(LEDS_MASK);
        gpio_set_mask(1 << POS);
        sleep_ms(VEL_REBOTE);
        if (GOLPE_J2) {
            DIR = 0; //Rebote válido
        } else {
            BLINK(LED_J1); //Punto jugador izquierdo
            POS = LED2;         //Reinicio al centro
            DIR = 0;            //Rirección hacia jugador que anotó
            START = true;     //Continuar movimiento automáticamente
        }
        GOLPE_J2 = false;
    }

    //Actualizar LED de pelota
    gpio_clr_mask(LEDS_MASK);
    gpio_set_mask(1 << POS);
}
```
!!! note "Adición"

    Se integró un botón de RESET para cuando se quiera detener el juego, de manera que la pelota se quede en el centro de la "cancha".

### Esquemático

<div style="display:flex; justify-content:center;">
    <img src="../recursos/imgs/Tarea_4/Pong_esq.png" alt="Esquemático para Selector Ciclíco" width="420">
</div>

#### Cálculos de corriente

#### Caso 1: LED consume 1.8V

Considerando que:

$V_{GPIO} = 3.3V\\$

$V_{LED} = 1.8V\\$

$I_{GPIO} = 12\,mA$

Entonces:

$V_{T} = 1.5V\\$

Por lo tanto:

$R_{MIN} = \frac{V_{T}}{I_{GPIO}} = \frac{1.5V}{12\,mA} = 125\Omega$

Sin embargo, considerando la corriente total del I/O (3V3):

$I_{I/O} = 50\,mA$

Los $125\Omega$ no son suficientes, debido a que se cuentan con 7 LEDs. Por lo tanto, la corriente máxima que puede tener cada pin es de $I_{MAX} = 7.14\,mA$. Considerando lo anterior:

$R_{MIN_{REAL_{1.8V}} } = \frac{V_{T}}{I_{PERMITIDA}} = \frac{1.5V}{7.14\,mA} = 210\Omega$

#### Caso 2: LED consume 2V

Por otro lado, considerando que:

$V_{GPIO} = 3.3V\\$

$V_{LED} = 2V\\$

$I_{PERMITIDA} = 7.14\,mA$

Entonces:

$R_{MIN_{REAL_{2V}} } = \frac{V_{T}}{I_{PERMITIDA}} = \frac{1.3V}{7.14\,mA} = 182\Omega$

Tomando en cuenta ambos casos, para evitar forzar la corriente del I/O, se escogieron resistencias de $220 \Omega$, aunque estás podrían incrementar para reducir el consumo de corriente.

De manera que la corriente es:

$I_{LED_{1.5V}} = \frac{1.5V}{220} = 6.81\,mA$

$I_{LED_{1.3V}} = \frac{1.3V}{220} = 5.91\,mA$

Tomando esto en cuenta, la corriente total oscila entre $41.37\,mA$ ~ $47.67\,mA$

#### Botones 

Considerando que la corriente restante es de $2.33\,mA$, entonces:

$I_{BTNs} = 0.78\,mA$

Debido a que se cuentan con 3 botones, la resistencia miníma para cada uno de ellos sería:

$R_{MIN} = \frac{3.3V}{0.78\,mA} = 4.23\,k\Omega$

Sin embargo, esto forzaría al RP2350, por lo tanto, se escogió una resistencia de $10\,k\Omega$.


### Video

<div style="display:flex; justify-content:center;">
  <video style="width:100%; max-width:900px;" muted controls>
    <source src="../recursos/archivos/Tarea_4/Pong.mp4" type="video/mp4">
  </video>
</div>