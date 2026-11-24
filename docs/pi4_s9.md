# Semana 9 — Integración, go-to-market y pitch

## 1) Resumen

- **Nombre de la actividad:** _Integración del sistema, pruebas con usuarios, economía unitaria, regulación, pitch y demo_
- **Curso:** _Proyecto de Ingeniería IV_
- **Equipo:** _David López Ramírez_
- **Fecha:** _23/11/2026_
- **Descripción breve:** _Última clase de contenido. Con el prototipo de la semana 8 funcionando y el modelo económico actualizado, esta semana se preparó todo lo que **Zaqora** necesita para la evaluación final: las fronteras del sistema y sus seis pruebas, el protocolo de pruebas con usuarios, la economía unitaria de lanzamiento (CAC, churn, LTV y payback), el checklist regulatorio con fuentes oficiales, el guion del pitch de 3 minutos, el guion de la demo de 7 minutos y la ruta de las dos semanas de trabajo. El trabajo se hizo con Claude a partir de los prompts del curso, con los datos de Zaqora._

---

## 2) Punto de partida

**Concepto (semana 6):** **Ghost Engine**, una PWA en formato de novela visual: tras perder en Lichess, el villano que encarna el error del jugador le escribe y lo invita a un capítulo construido sobre esa misma partida.

**Lo que ya hay:**

- **Prototipo publicado y probado de punta a punta** (semana 8): aviso push de la app, escena con la posición real del error y registro de eventos en Supabase. La prueba con usuarios del segmento **no se ha hecho**.
- **Modelo económico vigente** (semana 8, actualización del 23/11/2026): \$59 MXN al mes con IVA (\$44.92 netos), costo de \$0.80 por usuario activo a 100 usuarios, narrador en la capa gratuita de Cloudflare Workers AI, VPN a 5 años de +\$9,281 y recuperación en el mes 21.
- **Producto de software**, sin componente físico: así se acordó con el profesor desde el inicio del curso. Por eso cada bloque de la clase, pensado para hardware, se traduce a su equivalente de software.

- **Objetivo de la semana:** Dejar decidido cómo se integra, se prueba, se lanza y se cuenta Zaqora, con números propios y con cada pendiente marcado.

---

## 3) Proceso — Integración, lanzamiento y pitch

### Paso 1 — Integración del sistema

**Las cuatro fronteras de Zaqora** (la clase usa sensor → microcontrolador → red → IA → app; en Zaqora la «lectura» es la partida de Lichess):

| # | Frontera | Lado A → lado B | Protocolo | Pregunta |
| :---: | :--- | :--- | :--- | :--- |
| **F1** | Partida → detector | API de Lichess → detector de derrotas | HTTPS, NDJSON (`/api/games/user`, `evals=true`) | ¿La derrota se detecta y trae análisis? |
| **F2** | Detector → celular | Detector → servicio push del navegador → *service worker* | Web Push con VAPID | ¿El aviso sale y llega? |
| **F3** | Motor → narrador | Hechos del motor (JSON) → LLM → validador | HTTPS (Workers AI) | ¿La frase del villano es utilizable? |
| **F4** | Escena → usuario y registro | PWA → jugador; PWA → Supabase | HTTPS / REST | ¿El jugador ve la posición correcta y queda registrado lo que hace? |

**Seis pruebas del sistema**, de la más barata a la más cara. Los criterios salen del PDS (semana 5) y del plan de la semana 8:

| # | Prueba (adaptada) | Qué se mide | Aprobado si | Estado y evidencia |
| :---: | :--- | :--- | :--- | :--- |
| **T1** | Activación sin ayuda | Tiempo y errores de alguien que no conoce Zaqora al abrir el enlace y activar los avisos | < 5 minutos sin intervención (en iPhone, incluida la instalación) | ⏳ **Pendiente.** Solo lo hizo el equipo (15/10/2026). |
| **T2** | Latencia derrota → aviso | Minutos entre el fin de la partida (Lichess) y el aviso (registro del script) | ≤ 10 minutos (plan de la semana 8) | ⚠️ **Parcial.** El 15/10 el script detectó las dos derrotas en el mismo minuto, pero porque se corrió a mano. Con `--cada 15` el peor caso es de 15 minutos: **no cumple por diseño**. Corrección: correrlo con `--cada 5`. |
| **T3** | Celular sin conexión | Se apaga la red del celular mientras sale el aviso y se vuelve a encender | El aviso llega al reconectar | ⏳ **Pendiente.** Hallazgo de diseño: el aviso se envía con `ttl=3600`, así que **si el celular pasa más de 1 hora sin red, el aviso se pierde**. Es aceptable (un aviso tardío ya no llega «justo después de perder»), pero hay que declararlo. |
| **T4** | Autonomía de la capa gratuita (equivalente de la batería) | Capítulos al mes que caben en la capa gratuita de Workers AI | Alcanza para el piloto de 20 usuarios | ✅ **Cumple (cálculo).** 10,000 neurons al día ≈ 148 capítulos al día ≈ 4,440 al mes → **222 usuarios activos** a 20 capítulos al mes. Ver el cálculo abajo. |
| **T5** | Falla de la API de IA | Qué ve el jugador si el LLM no responde | A los 4 s sale una plantilla; nunca un texto vacío ni inválido (RD-04) | ⏳ **Pendiente en el producto.** En el prototipo todas las frases son de plantilla, así que la falla no puede ocurrir; tampoco prueba nada. |
| **T6** | Operación continua | El detector corre 48 h seguidas con los participantes | Sin caídas ni derrotas sin aviso; los HTTP 429 de Lichess se esperan 60 s | ⏳ **Pendiente.** Se corre junto con las pruebas de usuario. |

**Cómo se calcula T4**, con números (igual que la autonomía de batería del ejemplo de la clase):

```text
Capa gratuita de Cloudflare Workers AI     = 10,000 neurons al día
Un capítulo con Llama 3.1 8B               ≈ 67.5 neurons  →  148 capítulos al día
Capítulos al mes                           = 148 × 30 = 4,440
Uso supuesto por usuario activo            = 20 capítulos al mes (semana 7)
Usuarios activos que caben                 = 4,440 / 20 = 222  →  cumple (piloto de 20)
```

**Falla encontrada al revisar F1 (23/11/2026).** Si una derrota no tenía análisis, el detector la marcaba como revisada y enviaba el aviso con una **posición de ejemplo**; el consejo de «pide el análisis y vuelve a correr el script» no servía, porque la partida ya no se volvía a leer. Se encontró leyendo el código frontera por frontera, no en una prueba. Corrección: la derrota sin análisis no se marca como revisada y se reintenta en cada vuelta hasta 30 minutos.

**Cómo debe degradarse Zaqora:**

| Si falla… | Qué pasa | Qué ve el jugador |
| :--- | :--- | :--- |
| **Internet del jugador** | El aviso espera en el servicio push hasta 1 hora | Nada; si vuelve a tiempo, el aviso llega. La escena abierta ya no necesita red para jugarse; el registro del evento se pierde sin romper nada. |
| **Lichess (o un 429)** | El detector espera 60 s y reintenta | Nada: el aviso llega más tarde. |
| **El análisis de Lichess** (partida sin evaluar) | El detector espera hasta 30 minutos a que exista el análisis (el operador lo pide en Lichess); después envía el aviso con una posición de ejemplo y se lo indica al operador | El aviso llega más tarde o, en el peor caso, con una posición que no es la suya. En el producto, Stockfish en el navegador hace el análisis (revisión DFM). |
| **La API de IA** | A los 4 s se usa la plantilla del villano | Una frase de plantilla, sin aviso de error. |

**Definición de listo:**

| Condición (adaptada) | Estado |
| :--- | :---: |
| Funciona sin la laptop del equipo | ❌ El detector corre en la laptop (mago de Oz). Pasa a pg_cron + Edge Function de Supabase. |
| La app está desplegada, no en el entorno de desarrollo | ✅ [Publicada en GitHub Pages](prototipo/activar.html) con https |
| La landing está publicada en internet | ⏳ Construida; falta publicarla (Paso 3) |
| El dato fluye de la partida a la pantalla sin intervención | ❌ Hay que pedir a mano el análisis de la partida en Lichess |

??? quote "Prompt 1 del curso — plan de integración y pruebas (adaptado a Zaqora)"
    Actúa como ingeniero de pruebas de sistemas conectados, con experiencia en productos con componentes de IA. Tu método es la bisección por fronteras: probar cada interfaz entre componentes con evidencia (log, medición, captura) antes de culpar al sistema completo. No propones pruebas que el equipo no pueda ejecutar con sus medios: laptop y teléfonos.

    Somos un equipo de ingeniería en México. Nuestro producto:  
    Nombre y qué hace: Zaqora. Cuando un jugador pierde en Lichess, un villano que encarna su error le manda un aviso push y lo invita a una escena con la posición real de su error.  
    Arquitectura (semana 5, revisada en la 8): PWA con *service worker*; detector en Python que lee la API pública de Lichess (NDJSON) y envía Web Push (VAPID); registro en Supabase; narrador con LLM en Cloudflare Workers AI (todavía no conectado).  
    Requerimientos de desempeño del PDS: primera frase del villano < 5 s; LLM con tiempo máximo de 4 s y después plantilla; aviso ≤ 10 min tras la derrota; costo ≤ \$30 MXN por usuario activo al mes.  
    Qué ya funciona por separado: aviso push, escena, registro de eventos, detección de derrotas.  
    Qué nunca hemos probado junto: el flujo completo con un jugador externo, el narrador con LLM, el detector corriendo días seguidos.

    Entrega: (1) las fronteras, (2) seis pruebas de la más barata a la más cara con criterio numérico, (3) los dos fallos más probables por frontera y (4) cómo debe degradarse si falla internet o la API de IA. Si falta un número en el PDS, dilo. No inventes requerimientos.

**Los dos fallos más probables por frontera:**

| Frontera | Fallo probable 1 | Fallo probable 2 | Primera prueba para distinguirlos |
| :--- | :--- | :--- | :--- |
| F1 | La partida no tiene análisis y no hay posición del error | Lichess responde 429 y la derrota se detecta tarde | Revisar la columna `con_analisis` y la hora de detección en `registro_envios.csv` |
| F2 | El participante no activó los avisos (o en iPhone no instaló la app) | La suscripción caducó o el celular estuvo > 1 h sin red | Buscar su alias en la tabla `suscripciones`; si está, enviar `--probar` |
| F3 | El LLM tarda más de 4 s | La frase inventa una jugada o rompe el formato | Guardar la entrada y la salida crudas de cada llamada y pasarlas por el validador |
| F4 | La escena abre con una posición equivocada (FEN o color) | El evento no llega a Supabase (sin red o clave errónea) | Comparar el FEN del enlace con la partida en Lichess; revisar la tabla `eventos` |

### Paso 2 — Pruebas con usuarios

!!! warning "Estado: no realizadas"
    Las cinco pruebas de usuario se hacen en la semana de trabajo B. Esta sección deja listo el protocolo; los resultados se llenan con lo que pase, no antes.

**Con quién:** 5 personas, mayores de edad. **Tres del segmento** (jugadores amateur de Lichess que juegan al menos 3 veces por semana) y **dos de otro equipo** del curso.

**Protocolo de 30 minutos adaptado a Zaqora:**

| Min | Qué pasa | Qué se observa |
| :---: | :--- | :--- |
| 0–3 | Guion fijo: «Estamos probando el producto, no a ti. Piensa en voz alta.» | Nada que explicar del producto |
| 3–10 | **Tarea 1:** abrir el enlace de activación en su celular y activar los avisos del villano (en iPhone, primero agregar a la pantalla de inicio) | ¿Lo logra sin ayuda? Tiempo, errores, dudas (es la prueba T1) |
| 10–20 | **Tarea 2:** el operador dispara el aviso con su última derrota real; el participante lo abre y juega el encuentro | ¿Abre el aviso? ¿Elige «Muéstrame» o «Déjame en paz»? ¿Entiende qué le pide el villano? ¿Resuelve? |
| 20–25 | **Tarea 3:** encontrar el precio en la landing y dejar su correo en el pre-registro | ¿Encuentra el precio? ¿Completa el CTA? |
| 25–30 | Entrevista de cierre | La última vez que perdiste, ¿qué hiciste justo después? ¿Qué te costó? ¿Cuánto pagarías? ¿A quién se lo mandarías? |

Por cada tarea se registra: completó sin ayuda (sí o no), tiempo, errores y dudas, SEQ de 1 a 7 y citas textuales. Los hallazgos se clasifican en crítico, mayor y menor antes de corregir nada. La hoja de observación de la semana 8 se reutiliza con estas tres tareas.

**Prueba de campo (la de la semana 8, todavía pendiente):** además de la sesión de 30 minutos, los tres participantes del segmento dejan los avisos activos 3 a 5 días con el detector corriendo. Es la única forma de medir lo que la sesión no puede: si alguien que **de verdad** acaba de perder abre el aviso.

??? quote "Prompt 2 del curso — síntesis de pruebas de usuario (se ejecuta con las notas reales)"
    Actúa como investigador de usabilidad de productos conectados. Sintetizas observaciones sin defender el diseño: reportas lo que la gente hizo, no lo que dijo que le gustaba. Distingues el problema de su causa y no propones rediseños sin evidencia.

    Notas de [N] sesiones de prueba, una por usuario. Por cada tarea registramos: si completó sin ayuda, tiempo, errores, SEQ (1 a 7) y citas textuales.

    [pegar las notas]

    Entrega: (1) tabla por tarea con tasa de éxito sin ayuda, tiempo mediano y SEQ promedio; (2) hallazgos por severidad, con cuántos usuarios lo vivieron y una cita; (3) los tres cambios de mayor impacto con menor esfuerzo y la hipótesis que prueba cada uno; (4) lo que NO podemos concluir con esta muestra; (5) señal de negocio, separando compromisos reales (dejó datos, pre-registró, pagó) de opiniones.

### Paso 3 — Go-to-market y economía unitaria

**Cliente número 1.** Un jugador de Lichess mexicano, adulto, de 1200 a 1800, que juega varias veces por semana y que la semana pasada perdió tres partidas seguidas y cerró la sesión. Los cuatro rasgos del *early adopter*:

| Rasgo | En Zaqora | Evidencia |
| :--- | :--- | :--- |
| Tiene el dolor agudo | Pierde rachas de partidas y rating | Entrevistas de la semana 3: «Perdí tres partidas seguidas… apagué Lichess» |
| Ya intentó resolverlo | Cierra la sesión o se aleja 20 minutos; revisa la partida sin motor | Entrevistas de la semana 3 |
| Puede decidir y pagar | El propio jugador paga; no hay comprador institucional | Segmento de la semana 4 |
| Habla con otros como él | Clubes, Discord, grupos de WhatsApp y *streamers* de ajedrez en español | HIPÓTESIS: no medido |

**Canales elegidos:**

| Canal | Por qué | Qué se aprende |
| :--- | :--- | :--- |
| **Venta directa** a jugadores de clubes y conocidos (los primeros 20) | David es maestro de ajedrez: es el canal con menos costo y más aprendizaje | Objeciones, activación, uso real |
| **Landing con pre-registro y precio visible** | Mide si alguien deja su correo por una promesa con precio, antes de programar los pagos | Visitas → clics en el CTA → pre-registros |
| **Comunidades y *streamers* en español** (siguiente paso) | El jugador en *tilt* no busca ayuda: hay que llegarle donde ya está | Costo por usuario activado |

**Sin cobro anticipado.** Durante el curso solo se mide intención con pre-registro y precio visible. Cobrar exige RFC, CFDI y cumplir la LFPC en suscripciones (Paso 4).

**Economía unitaria.** Zaqora no tiene hardware subsidiado, así que la inversión por cliente es solo el CAC. Cada cifra va marcada como **medida** (sale de una fuente o de un precio verificado) o **supuesta** (no se ha medido).

| Dato | Valor | Origen |
| :--- | ---: | :--- |
| Precio de suscripción | \$59 MXN al mes con IVA | Decisión de la semana 7 · **supuesto** (no validado con usuarios) |
| Ingreso neto por suscriptor (sin IVA ni comisión de Stripe) | \$44.92 | Precios de Stripe MX verificados (semana 7) · **medido** |
| Costo operativo por usuario activo | \$0.80 al mes | Modelo vigente a 100 usuarios (semana 8) · **medido** sobre precios verificados |
| Conversión de activo a pago | 5 % | **Supuesto** (semana 7) |
| Horas para activar a un usuario | 0.25 h (15 min) | **Supuesto**: mensajes, explicación y activación de avisos |
| Costo de la hora del equipo | \$80 MXN | **Supuesto** (tarifa del ejemplo del curso) |
| Churn mensual | 10 % | **Supuesto**: no hay ningún suscriptor todavía |

```text
Usuarios activos por cada usuario de pago = 1 ÷ 0.05                     = 20
Costo operativo por usuario de pago       = 20 × $0.80                    = $16.00
Contribución mensual                      = 44.92 − 16.00                  = $28.92
CAC                                       = 20 usuarios × 0.25 h × $80      = $400
Inversión por cliente                     = CAC + hardware (0)             = $400
Vida media                                = 1 ÷ 0.10                       = 10 meses
LTV                                       = 28.92 × 10                     = $289
LTV ÷ inversión                           = 289 ÷ 400                      = 0.72
Payback                                   = 400 ÷ 28.92                    = 13.8 meses
```

**Lectura:** con estos supuestos **no cierra**: LTV ÷ inversión de 0.72 contra la regla de 3, y payback de 13.8 meses contra la regla de 12. El costo de la nube no es el problema (\$0.80 por usuario); el problema es que cada suscriptor cuesta 20 usuarios activados.

**Qué palanca mueve más** (cada insumo cambia 25 % por separado):

| Cambio de 25 % | LTV ÷ inversión | Payback |
| :--- | :---: | :---: |
| Caso base | 0.72 | 13.8 meses |
| Precio sube a \$73.75 | 1.03 | 9.8 |
| Precio baja a \$44.25 | 0.42 | 23.8 |
| Conversión sube a 6.25 % | 1.00 | 10.0 |
| Conversión baja a 3.75 % | 0.44 | 22.6 |
| Churn baja a 7.5 % | 0.96 | 13.8 |
| Churn sube a 12.5 % | 0.58 | 13.8 |
| CAC baja a \$300 | 0.96 | 10.4 |
| CAC sube a \$500 | 0.58 | 17.3 |

El **precio** y la **conversión** mueven más que el churn y el CAC. La conversión pesa doble porque cambia al mismo tiempo el CAC y la contribución: cada usuario de pago carga menos usuarios gratuitos.

**Tres palancas concretas:**

| Palanca | Qué la sostiene | LTV ÷ inversión | Payback |
| :--- | :--- | :---: | :---: |
| **Conversión de 5 % a 10 %** | Tope de capítulos gratis y cobro fuera del momento de la derrota (semana 7) | 1.85 | 5.4 meses |
| **+ churn de 10 % a 6 %** | Valor que se acumula: el elenco de villanos y el historial de cada jugador | **3.08** | 5.4 meses |
| **Conversión de 10 % y activación en 9 minutos** (en lugar de 15) | Activación sin ayuda (T1) y llegada por comunidades | **3.08** | 3.3 meses |

Llegar a 3 necesita **dos** palancas, y las dos dependen de algo que no se ha medido. Eso es lo que se va a ir a medir en el piloto: qué tasa de conversión y cuánto tiempo de activación son reales.

??? quote "Prompt 3 del curso — economía unitaria (con los datos de Zaqora)"
    Actúa como analista financiero de startups de software con suscripción. Calculas con los números que te dan, muestras la aritmética completa y no completas datos faltantes con supuestos propios: si falta uno, lo pides. Cuando el resultado no cierra, no lo suavizas.

    Datos de nuestro modelo (semanas 7 y 8): precio de suscripción mensual \$59 MXN con IVA (\$44.92 netos); costo operativo mensual por usuario activo \$0.80; sin hardware.  
    Datos de adquisición: conversión de activo a pago 5 % (supuesto); 0.25 h por usuario activado a \$80 la hora (supuesto); sin viáticos ni publicidad; churn mensual esperado 10 % (supuesto).

    Calcula: CAC, contribución mensual, vida media, LTV, inversión por cliente, LTV ÷ inversión y payback. Después: si cumple la regla práctica; cuál de los insumos mueve más el resultado, cambiando cada uno 25 % por separado; y tres palancas concretas con su efecto numérico. Formato: tabla de cálculo y después máximo 8 líneas de lectura.

**Landing.** Se construyó con la anatomía de la clase y está lista para publicarse en `…/landing/`:

| Elemento | En la landing de Zaqora |
| :--- | :--- |
| Headline | «Perdiste en Lichess. Tu villano ya sabe dónde fue.» y, debajo, la propuesta de valor de la semana 4 |
| Visual | La escena real del prototipo (sellada y despierta) en un celular |
| Tres beneficios | No tienes que analizar en caliente · Tu error de siempre tiene cara y se puede vencer · Sin rating ni comparaciones |
| Demo corta | ⏳ Video de 30 s del aviso llegando y la escena abriéndose (por grabar); por ahora, las capturas |
| Evidencia | Cita de las entrevistas de la semana 3 |
| Precio visible | \$59 MXN al mes con IVA; los primeros capítulos, gratis; sin cobro durante la beta |
| Un solo CTA | «Quiero entrar a la beta»: pre-registro con correo |
| Metadatos | `title`, `description` y Open Graph con la captura de la escena |
| Métricas | Visitas, clics en el CTA y pre-registros, en Supabase (tabla `eventos` y tabla `preregistros`, solo inserción) |
| Aviso de privacidad | Página aparte con los seis elementos del artículo 15 de la LFPDPPP |

### Paso 4 — Regulación mínima viable

Checklist hecho con búsqueda en fuentes oficiales el 23/11/2026. Zaqora es software, así que radio, NOM, baterías y REP no aplican. **No es asesoría legal: es una ruta de verificación.**

| Tema | ¿Aplica? | Qué exige | Documento o trámite | Quién lo emite | Costo y tiempo | Estatus |
| :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| **Radio y homologación** | No | Zaqora no tiene radio propia: usa el celular del jugador | — | — | — | No aplica |
| **Datos personales** | **Sí** | Aviso de privacidad desde que se recaban los datos, con 6 elementos mínimos: identidad y domicilio del responsable, datos tratados, finalidades, opciones para limitar su uso, medios para los derechos ARCO y cómo se avisan los cambios (art. 15). Respuesta a una solicitud ARCO en máximo 20 días y aplicarla en los 15 siguientes (art. 31). La autoridad es la Secretaría Anticorrupción y Buen Gobierno (art. 2, fr. XV). | Aviso de privacidad (lo redacta el responsable) | David López Ramírez, como responsable | Sin costo; ya redactado para la landing | **VERIFICADO** · [LFPDPPP, texto vigente](https://www.diputados.gob.mx/LeyesBiblio/ref/lfpdppp.htm) (DOF 20-03-2025, vigente desde el día siguiente; última reforma DOF 14-11-2025) |
| **Seguridad, etiquetado y baterías** | No | Sin producto físico | — | — | — | No aplica |
| **Licencia de Stockfish** (rival y análisis) | **Sí** | GPLv3: al distribuir el binario WASM hay que ofrecer su código fuente correspondiente y el aviso de licencia, sin restricciones adicionales (secciones 5, 6 y 10) | Enlace a la fuente exacta del *build* y aviso en la app (ya lo exige RR-03) | El equipo | Sin costo | **VERIFICADO** · [Copying.txt de Stockfish](https://github.com/official-stockfish/Stockfish/blob/master/Copying.txt) |
| **Licencia de Llama 3.1** (narrador) | **Sí** | Uso comercial permitido y sin regalías; licencia aparte solo arriba de 700 millones de usuarios al mes; mostrar «Built with Llama» y cumplir la política de uso aceptable | «Built with Llama» en la app y la documentación | El equipo | Sin costo | **VERIFICADO** · [Llama 3.1 Community License](https://www.llama.com/llama3_1/license/) |
| **Cloudflare Workers AI** | **Sí** | No usa el contenido de los clientes para entrenar modelos; no retiene entradas ni salidas en la inferencia estándar | Declararlo en el aviso de privacidad como encargado | Cloudflare | Capa gratuita | **VERIFICADO** · [Data usage de Workers AI](https://developers.cloudflare.com/workers-ai/platform/data-usage/) |
| **API de Lichess** | **Sí** | Se permite el uso personal y comercial de sus servicios, API incluida, con límites razonables que decide Lichess; el abuso de la API está prohibido y el acceso se puede revocar sin aviso | Respetar límites (1 petición a la vez, esperar tras un 429) | Lichess | Sin costo | **VERIFICADO** · [Terms of Service de Lichess](https://lichess.org/terms-of-service) (01/08/2026) |
| **Términos de venta y consumidor** | **Sí** | En comercio electrónico: domicilio físico, teléfonos y medios para reclamar antes de la transacción; conocer términos, costos y cargos; informar de forma clara y destacada los **cobros automáticos recurrentes** (periodicidad, monto y fecha), con consentimiento expreso; avisar al menos **5 días naturales antes de una renovación automática** y permitir **cancelar de inmediato** (art. 76 BIS, fr. III, V, VIII y IX; las dos últimas, DOF 12-12-2025) | Términos de servicio y flujo de cancelación en la app | El equipo (PROFECO vigila) | Sin costo | **VERIFICADO** · [LFPC, texto vigente](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPC.pdf) |
| **Pagos con tarjeta** | Al cobrar | Cuenta de Stripe México verificada | Alta en Stripe | Stripe | 3.6 % + \$3 MXN por cobro (verificado en la semana 7) | **POR VERIFICAR** · requisitos de alta (RFC, cuenta bancaria) no publicados en [stripe.com/mx](https://stripe.com/mx) |
| **Obligaciones fiscales** | Al cobrar | RFC con actividad, CFDI e IVA de 16 % en servicios digitales | Inscripción en el RFC | SAT | Sin dato verificado | **POR VERIFICAR** · el portal del SAT no se pudo consultar; confirmar con el SAT o un contador |
| **Google Play** | Si se publica ahí | Prueba cerrada con 12 testers durante 14 días (cuentas personales) y facturación de Google obligatoria en bienes digitales (15 % en suscripciones) | Cuenta de desarrollador | Google | US\$25, pago único | **VERIFICADO** en la semana 8 (Ayuda de Play Console) |
| **Economía circular** | No | Sin residuos físicos; el equivalente es borrar los datos del usuario (derechos ARCO) | — | — | — | No aplica |
| **Exportación** | No, por ahora | Se vende primero en México | — | — | — | No aplica |
| **Marca** | **Sí** | Registro de «Zaqora» en las clases 9 y 41 | Solicitud de registro de marca | IMPI | Sin dato verificado | **POR VERIFICAR** · la búsqueda de la semana 3 no encontró registros; la solicitud no se ha presentado |

**Qué se puede hacer en una prueba de mercado de 5 a 10 usuarios** (sin cobrar):

- Pre-registro en la landing con el aviso de privacidad publicado.
- Prueba del prototipo con consentimiento por escrito, solo mayores de edad y alias en lugar del usuario de Lichess (ya está así).
- Usar la API de Lichess dentro de sus límites.

**Qué debe estar resuelto antes de vender a un tercero:**

- RFC y CFDI (SAT) y la cuenta de Stripe verificada.
- Términos de servicio con domicilio físico y teléfono, cobro recurrente explicado, aviso 5 días antes de renovar y cancelación inmediata en la app (LFPC 76 BIS).
- Aviso de privacidad de la app completa (partidas, avisos push, eventos), no solo el de la landing.
- «Built with Llama» y el enlace a la fuente de Stockfish dentro de la app.
- Solicitud de marca en el IMPI.

### Paso 5 — El pitch de 3 minutos

**Guion** (344 palabras, 2:39 hablados a 130 palabras por minuto; quedan 21 segundos de aire):

| Parte | Guion | Palabras | Segundos |
| :--- | :--- | :---: | :---: |
| **1. Impacto y problema** (35 s) | Un jugador de Lichess nos contó que perdió tres partidas seguidas y apagó todo. No las analizó, porque, en sus palabras, «sabía que iba a buscar excusas». Otro puede pasar una hora jugando partidas que no quería, solo para recuperar la anterior. Esa racha le cuesta rating y tiempo, y una clase particular de 229 pesos la hora no llega en el momento en que todo se rompe: justo después de perder. | 72 | 33.2 |
| **2. Solución y por qué nosotros** (35 s) | Zaqora llega en ese momento. Minutos después de tu derrota te escribe un villano que encarna tu error de siempre y te invita a un capítulo construido sobre esa misma partida. Chess.com te da un análisis frío cuando estás enojado; Zaqora primero reconoce que dolió y después te enseña dónde fue, sin rating ni comparaciones. En la demostración verán llegar ese aviso después de una derrota real. | 67 | 30.9 |
| **3. Mercado y modelo** (35 s) | En México estimamos 66 mil jugadores en línea que se frustran al perder y pagarían por mejorar. Cobramos 59 pesos al mes, menos que Chess.com o Duolingo. Como el análisis corre en el teléfono y el narrador usa una capa gratuita de inteligencia artificial, cada usuario activo nos cuesta 80 centavos al mes. Con 50 suscriptores al quinto año, la inversión se recupera en el mes 21. | 67 | 30.9 |
| **4. Tracción** (35 s) | Entrevistamos a tres jugadores, y los tres, después de perder, dejan de jugar en lugar de analizar. Construimos el prototipo y funciona de punta a punta con partidas reales: detecta la derrota, envía el aviso y abre la escena. Lo que todavía no tenemos es lo más importante: ningún jugador externo lo ha usado. Esa es la primera prueba que vamos a correr. | 63 | 29.1 |
| **5. Equipo** (15 s) | Soy David López: ingeniero mecatrónico, desarrollador y maestro de ajedrez. Diseñé, programé y calculé solo todo lo que verán hoy, y sigo después del curso. | 25 | 11.5 |
| **6. Ask y cierre** (25 s) | Pedimos cinco jugadores de Lichess que reciban el aviso durante una semana, y un club o streamer en español para un piloto de 20 usuarios. En 90 días mediremos si abren el aviso y si uno de cada veinte paga. Cuando pierdes, Zaqora convierte esa derrota en tu próximo capítulo. | 50 | 23.1 |
| **Total** | | **344** | **158.8** |

La confesión honesta es una sola: ningún jugador externo lo ha usado. Las palabras prohibidas (innovador, plataforma, solución integral, revolucionario) no aparecen.

**Evidencia de cada cifra:**

| Afirmación | Fuente | Estado |
| :--- | :--- | :--- |
| Perdió tres partidas seguidas y «sabía que iba a buscar excusas» | Entrevistas 2 y 3, semana 3 | Evidencia |
| Una hora jugando partidas que no quería | Entrevista 1, semana 3 | Evidencia |
| Clase particular de 229 pesos la hora | Precio promedio en México, semana 2 | Evidencia (fuentes de la semana 2) |
| 66 mil jugadores que se frustran y pagarían | SAM de 65,952, semana 4 | **PENDIENTE**: tres filtros del embudo son supuestos propios |
| 59 pesos, menos que Chess.com (\$101–253) o Duolingo (\$129) | Benchmarking, semana 7 | Evidencia |
| 80 centavos por usuario activo al mes | Modelo vigente a 100 usuarios, semana 8 | Evidencia (a 20 usuarios son \$4.00) |
| 50 suscriptores al año 5; recuperación en el mes 21 | Flujo de caja a 5 años, semana 8 | **PENDIENTE**: conversión y crecimiento supuestos |
| Los tres dejan de jugar en lugar de analizar | Entrevistas, semana 3 | Evidencia (muestra de 3) |
| El prototipo funciona de punta a punta | Prueba de funcionamiento del 15/10/2026, semana 8 | Evidencia |

**Las preguntas más difíciles del jurado:**

| Pregunta | Respuesta corta | Dónde está |
| :--- | :--- | :--- |
| ¿Cuánto cuesta servir a un usuario y cómo lo sabes? | \$0.80 al mes a 100 usuarios y \$4.00 a 20, con precios verificados en las páginas de cada proveedor | Semanas 7 y 8 (BOM y DFM) |
| ¿Por qué no lo hace Chess.com? | Su análisis llega frío y con evaluación numérica; Zaqora apuesta a que el jugador en *tilt* no quiere eso. El competidor más peligroso no es Chess.com, es cerrar la app | Semana 4 (mapa competitivo y lienzo) |
| ¿Qué pasa si se acaba la IA gratuita o sube su precio? | La capa gratuita alcanza para 222 usuarios; el excedente se paga a precio de Haiku 5.5 (unos \$0.50 por usuario al mes), y si la IA falla, el villano habla con plantillas | Semana 8 y Paso 1 (T4, T5) |
| ¿Cuántos clientes necesitas para no perder dinero? | 2 suscriptores recuperan la inversión del año 1; la economía por cliente pide conversión de 10 % y churn de 6 % para llegar a 3 | Semanas 7 y 8, Paso 3 |
| ¿Qué necesitas para vender legalmente? | Aviso de privacidad (listo), términos con cobro recurrente y cancelación inmediata (LFPC 76 BIS), RFC y CFDI, Stripe verificado | Paso 4 |
| ¿Qué hace que un jugador no cancele? | HIPÓTESIS: que el elenco de villanos y su historial se vuelvan suyos. No hay datos de churn | Paso 3 |

??? quote "Prompt 5 del curso — guion de pitch (con el material de Zaqora)"
    Actúa como coach de pitch para fundadores técnicos, con experiencia en jurados de aceleradoras. Tu objetivo es que el pitch venda: que el jurado sienta el problema, quiera el producto, crea los números y sepa qué se le pide. Cada afirmación tiene evidencia detrás; sin evidencia no hay afirmación, hay un pendiente. Prefieres una persona o una cifra a un adjetivo.

    Propuesta de valor (semana 4): «Cuando pierdes en Lichess y estás por cerrar la app, Zaqora valida tu frustración y la convierte en el próximo capítulo de tu historia.»  
    Usuario y evidencia (semana 3): 3 entrevistas; citas «No intenté analizar las partidas en ese momento porque sabía que iba a buscar excusas» y «Puedo pasar una hora jugando partidas que realmente no quería jugar».  
    Mercado (semana 4): TAM 82,440, SAM 65,952, SOM 1,200 personas, con tres filtros supuestos.  
    Modelo: \$59 MXN al mes con IVA; \$0.80 por usuario activo; LTV ÷ inversión 0.72; payback 13.8 meses.  
    Evidencia de pruebas: prototipo probado de punta a punta por el equipo; ninguna prueba con usuarios externos todavía; ningún pre-registro.  
    Equipo: David López Ramírez, una sola persona.  
    Ask: 5 jugadores para la prueba y un club o *streamer* para un piloto de 20 usuarios durante 90 días.

    Escribe el guion de 3 minutos con el presupuesto de 35, 35, 35, 35, 15 y 25 segundos (76, 76, 76, 76, 32 y 54 palabras; total entre 330 y 360). Después entrega (a) las afirmaciones sin evidencia marcadas como PENDIENTE y (b) las 5 preguntas más difíciles del jurado y de dónde sale la respuesta.

### Paso 6 — La demo de 7 minutos

La demo recorre un solo camino: el jugador pierde, le llega el aviso del villano, abre la escena y termina en la landing. Necesita **dos personas**: David narra y un compañero opera la laptop y el celular.

| Tiempo | Quién | Qué se hace y se dice | Plan B |
| :--- | :--- | :--- | :--- |
| **0:00–0:45** · Contexto | Narrador | Muestra el celular. «Este jugador acaba de perder tres partidas. Les voy a mostrar el camino completo: pierde, el villano le escribe, enfrenta su error y decide si lo compra.» | Captura de la escena sellada |
| **0:45–3:15** · Camino principal | Operador | En el celular de demo, abre el enlace de activación y activa los avisos (el jurado ve el permiso). Envía un aviso con la última derrota ya preparada: llega la notificación del villano, se toca y abre la escena sellada; «Muéstrame» revela la posición real y el operador resuelve la jugada clave. Narrador: «el villano no se burla: primero reconoce que dolió». | Video de respaldo de este tramo (90 s) |
| **3:15–4:45** · Provocar el evento | Operador | Pierde en vivo una partida **casual contra la computadora de Lichess** (no contra otra cuenta: abandonar a propósito contra una persona viola las reglas de juego limpio de Lichess). Pide el análisis de la partida y el detector, corriendo cada minuto, envía el aviso con **esa** posición. Narrador: «en el producto revisa cada 5 minutos; hoy, cada minuto, para que lo vean» y «hoy el análisis lo pido a mano; en el producto lo hace Stockfish en el teléfono». | Partida perdida el día anterior, ya analizada, y video |
| **4:45–5:45** · Fallo manejado | Operador | Pone el celular en modo avión y se envía otro aviso: no llega. Quita el modo avión: el aviso llega solo, porque el servicio push lo guarda hasta 1 hora. Narrador: «si pasa más de una hora sin red, el aviso ya no llega, y es a propósito: un aviso tardío ya no es "justo después de perder"». | Video de la prueba T3 |
| **5:45–6:30** · La compra | Narrador | Muestra un QR. El jurado abre la landing en su teléfono: headline, precio de 59 pesos al mes y el botón de pre-registro. Un integrante del jurado o el operador deja su correo y se ve entrar el registro en Supabase. | Captura de la landing y de la tabla de pre-registros |
| **6:30–7:00** · Cierre | Narrador | «Hoy funciona esto: la derrota, el aviso y la escena. Falta esto: el narrador con IA está conectado solo en diseño, y ningún jugador externo lo ha probado. Siguiente paso: cinco jugadores esta semana y un piloto de 20.» | Ninguno: es solo voz |

**Atajos que se declaran en voz alta:** el detector corre en la laptop (mago de Oz), revisa cada minuto en lugar de cada 5 y el análisis de la partida se pide a mano en Lichess.

**Lista de verificación 15 minutos antes:** celular y laptop cargados; hotspot propio probado (no depender del Wi-Fi del salón); avisos activados en el celular de demo; detector corriendo con `--cada 1` y la partida de respaldo lista; landing abierta en una pestaña y QR impreso; videos de respaldo en el celular y en la laptop; proyección y cronómetro probados.

### Paso 7 — Ruta de cierre

Equipo de una persona: todas las tareas son de David, salvo la ayuda del operador en los ensayos y la demo.

| Semana de trabajo | Tarea | Punto de control |
| :--- | :--- | :--- |
| **A · construir y conectar** | Publicar la landing y crear la tabla `preregistros` en Supabase | La landing responde en internet y un pre-registro de prueba aparece en la tabla |
| | Detector con `--cada 5` y prueba T2 con una derrota propia | Aviso ≤ 10 min tras la derrota |
| | Pruebas T1 (con alguien que no conozca Zaqora) y T3 (modo avión) | Resultados en la tabla del Paso 1 |
| | Checklist regulatorio (hecho) y aviso de privacidad publicado | — |
| | Secciones 1 a 16 de la página de proyecto final al día | Hecho en la versión del 23/11/2026 |
| **B · probar, corregir y contar** | Cinco pruebas de usuario (tres del segmento, dos de otro equipo) y prueba de campo de 3 a 5 días | Notas por tarea, síntesis con el Prompt 2 |
| | Pruebas T5 y T6 (48 h del detector durante la prueba de campo) | — |
| | Pitch grabado en video, visto y reescrito | Video publicado sin iniciar sesión |
| | Demo ensayada tres veces con el operador y video de respaldo grabado | Tercer ensayo sin detenerse |
| | Secciones 17 a 22, resumen ejecutivo y anexos de la página de proyecto final | — |

**Congelamiento:** después del último ensayo solo se corrigen fallas críticas.

---

## 4) Entregable — Semana 9

| Entregable | Estado | Dónde |
| :--- | :---: | :--- |
| Economía unitaria con los números propios | ✅ | [Paso 3](#paso-3-go-to-market-y-economia-unitaria) |
| Esqueleto del pitch de 3 minutos con pendientes marcados | ✅ | [Paso 5](#paso-5-el-pitch-de-3-minutos) |
| Guion de la demo de 7 minutos con plan B por tramo | ✅ | [Paso 6](#paso-6-la-demo-de-7-minutos) |
| Ruta de las dos semanas con responsables | ✅ | [Paso 7](#paso-7-ruta-de-cierre) |
| Checklist regulatorio con estatus VERIFICADO o POR VERIFICAR | ✅ | [Paso 4](#paso-4-regulacion-minima-viable) |
| Fronteras y plan de pruebas T1 a T6 | ✅ (pruebas parcialmente hechas) | [Paso 1](#paso-1-integracion-del-sistema) |
| Landing publicada y accesible en internet | ⏳ Construida, falta publicar | Paso 3 |
| Reporte de pruebas de usuario con cinco sesiones | ⏳ Protocolo listo, sesiones pendientes | [Paso 2](#paso-2-pruebas-con-usuarios) |
| Pitch grabado en video | ⏳ Guion listo | Paso 5 |
| Demo ensayada tres veces con video de respaldo | ⏳ Guion listo | Paso 6 |
| Página de proyecto final | ✅ Primera versión | [Proyecto final](proyecto_final.md) |
| Documentación técnica (README, arquitectura, manual de usuario) | ✅ | [Proyecto final, secciones 8 y 12 y anexos B y C](proyecto_final.md) |

---

## 5) Reflexión

- **La economía unitaria contradice al flujo de caja, y los dos tienen razón.** El flujo a 5 años es positivo porque los costos son casi cero; la economía por cliente no cierra porque cada suscriptor cuesta 20 usuarios activados. El primer número dice que el negocio no quiebra; el segundo, que todavía no crece.
- **La palanca más fuerte es la que no he medido.** La conversión mueve el resultado más que el churn o el CAC, y no tengo un solo dato de conversión. Lo mismo pasa con la apertura del aviso. Todo lo que falta medir cabe en una prueba con cinco personas.
- **Leer la ley cambió el producto.** La reforma a la LFPC de diciembre de 2025 obliga a avisar 5 días antes de renovar una suscripción y a permitir cancelar de inmediato. No estaba en ningún documento de las semanas anteriores, y ahora es un requisito de la app.
- **Las reglas de Lichess cambiaron la demo.** Mi primera idea para provocar el evento era perder a propósito contra otra cuenta; eso es *sandbagging* según sus términos. La demo pierde contra la computadora.
- **Un pitch honesto con una sola confesión obliga a elegir.** Tenía dos datos débiles (la economía por cliente y la falta de usuarios). Dejé la falta de usuarios porque es la que el ask resuelve; la otra queda para las preguntas.

### Preguntas de cierre

| Pregunta | Respuesta |
| :--- | :--- |
| ¿En cuál de las cuatro fronteras es más probable que falle y qué registro pondrán ahí? | En F1: la partida sin análisis no tiene posición del error y no hay aviso. El registro ya existe: la columna `con_analisis` de `registro_envios.csv`. La corrección de fondo es el análisis con Stockfish en el teléfono. |
| ¿Cuál es su CAC, su LTV y su relación LTV ÷ inversión, y qué palanca mueve más? | CAC \$400, LTV \$289 y LTV ÷ inversión 0.72, todos con supuestos. Lo que más mueve es el precio y, sobre todo, la conversión, que cambia a la vez el CAC y la contribución. |
| ¿Cuál tema regulatorio puede impedirles vender y qué fuente lo confirma? | Cobrar una suscripción sin RFC y sin cumplir el art. 76 BIS de la LFPC (cobro recurrente claro, aviso de renovación y cancelación inmediata). La LFPC está verificada en el texto vigente de la Cámara de Diputados; lo fiscal, POR VERIFICAR con el SAT. |
| ¿Qué evidencia tienen para cada parte del pitch y cuáles son pendientes? | Problema y tracción: entrevistas y prueba de funcionamiento. Pendientes: el tamaño del mercado (filtros supuestos), las proyecciones a 5 años y cualquier dato de uso de jugadores externos. |
| ¿Cuál es el camino principal de la demo, qué evento provocan y cuál es su plan B? | Activación → aviso → escena → landing. El evento es una derrota en vivo contra la computadora de Lichess que dispara el aviso con esa posición. Plan B: una partida perdida el día anterior y el video de respaldo. |
