# Modulación por ancho de pulso - PWM

## 1) Resumen

- **Nombre del proyecto:** _Modulación por ancho de pulso - PWM_  
- **Equipo:** _Carlos Ernesto Camacho Gonzalez y David López Ramírez_  
- **Curso:** _Sistemas Embebidos I_  
- **Fecha:** _30/09/2025_  
- **Descripción breve:** _Estas prácticas muestran aplicaciones prácticas de la generación de frecuencias: control de velocidad de un motor mediante el PWM, generación de notas con un buzzer variando la frecuencia, y síntesis de una señal senoidal de 60 Hz mediante PWM más un filtro RC._

---

## 2) Objetivos

- **General:** _Aplicar la modulación por ancho de pulso (PWM) en diferentes contextos de control y generación de señales, integrando componentes electrónicos y de programación._
- **Específicos:**
  - _Implementar circuitos y programas que regulen velocidad de motores DC y generen tonos musicales con un buzzer mediante variación de duty cycle y frecuencia._

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

### 1)  Control de Duty Cycle — Motor DC

#### Función
Se configura un pin PWM para controlar un motor DC y utiliza dos botones para cambiar entre tres valores de duty cycle (baja, media y alta velocidad). Con cada pulsación se actualiza la velocidad seleccionada.

#### Código
```bash


```
#### Esquemático de conexión

<img src="../recursos/imgs/Tarea_2/Contador_binario_esq.png" alt="Esquemático para contador de 4 bits" width="420">

#### Vídeo

<video style="width:30%" muted="" controls="" alt="type:video">
   <source src="../recursos/archivos/Tarea_2/Contador_binario.mp4" type="video/mp4">
   </video>

### 2) Control de Frecuencia — Canción con Buzzer

#### Función
Genera una melodía en un buzzer variando la frecuencia del PWM mientras mantiene un duty fijo de 50 %. Para ello recorre una tabla de notas con frecuencias y duraciones, reproduciendo cada una con pausas definidas para hacer la melodía clara.

```bash

```

#### Esquemático de conexión

<div style="display:flex; justify-content:center;">
    <img src="../recursos/imgs/Tarea_2/Barrido_esq.png" alt="Esquemático para Barrido de 5 LEDs" width="420">
</div>

#### Vídeo

<div style="display:flex; justify-content:center;">
  <video style="width:100%; max-width:300px;" muted controls>
    <source src="../recursos/archivos/Tarea_2/Barrido_LEDs.mp4" type="video/mp4">
  </video>
</div>

### 3) Generación de Señales — Senoidal de 60 Hz con PWM + Filtro RC

#### Función
Produce una señal senoidal aproximada de 60 Hz modulando el duty cycle del PWM de acuerdo con una función seno. La salida se pasa por un filtro RC pasabajos, lo que permite observar en el osciloscopio la onda PWM sin filtrar y la señal senoidal suavizada.


```bash

```

#### Esquemático de conexión

<div style="display:flex; justify-content:center;">
    <img src="../recursos/imgs/Tarea_2/Secuencia_de_Gray_esq.png" alt="Esquemático para Secuencia de Gray" width="420">
</div>

#### Vídeo

<div style="display:flex; justify-content:center;">
  <video style="width:100%; max-width:300px;" muted controls>
    <source src="../recursos/archivos/Tarea_2/Secuencia_de_Gray.mp4" type="video/mp4">
  </video>
</div>