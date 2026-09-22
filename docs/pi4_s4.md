# Semana 4 — Mercado, valor y propuesta de valor

## 1) Resumen

- **Nombre de la actividad:** _Definición de Mercado, Competencia y Propuesta de Valor_
- **Curso:** _Proyecto de Ingeniería IV_
- **Equipo:** _David López Ramírez_
- **Fecha:** _17/09/2026_
- **Descripción breve:** _Continuando con el proyecto **Zaqora**, se estructuró el análisis de mercado pasando de la solución técnica a la oportunidad comercial. Se utilizaron herramientas de Inteligencia Artificial para definir el segmento accionable, dimensionar el mercado (TAM/SAM/SOM), mapear la competencia directa, indirecta y sustituta, construir un lienzo estratégico Blue Ocean y definir la propuesta de valor final integrando el marco IDEO y la Pirámide de Bain._

---

## 2) Punto de partida

**Concepto base (Zaqora):** El aprendizaje de ajedrez se convierte en el diseño de niveles de un videojuego de un solo jugador: cada «capítulo» es una lección disfrazada de misión, protagonizada por un personaje-villano que encarna un patrón de error real y recurrente del jugador. No hay ranking, no hay rival humano, no hay partida en línea contra otros: solo el jugador contra el mapa de la campaña, a su propio ritmo. El coaching ocurre dentro de la ficción —lo que dice el personaje, la trampa que tiende—, nunca como corrección fría ni comparación social. 

- **Objetivo de la semana:** Traducir este concepto técnico y emocional en un segmento accionable, un tamaño de mercado defendible, un mapa competitivo con sus barreras y una propuesta de valor clara (Canvas de mercado).

---

## 3) Proceso — Análisis de Mercado con IA

El proceso de esta semana requiere combinar búsquedas con datos reales (Perplexity) y análisis estratégico/creativo (Claude). A continuación, se detallan los prompts y análisis recibidos.

### Paso 1 — Perfil de segmento accionable

**Herramienta:** Claude (Definición de las cuatro capas del segmento accionable).

??? quote "Prompt completo — Ronda 1 (Claude, perfil de segmento accionable)"
    Actúa como un investigador de mercado con especialización en segmentación de clientes para negocios de producto digital en mercados emergentes latinoamericanos. Tu metodología combina datos demográficos verificables con análisis conductual y psicográfico basado en comportamiento observable — nunca en suposiciones sobre actitudes o valores generales. Cuando el equipo no tiene evidencia de una capa, lo señalas directamente en lugar de rellenar con hipótesis no marcadas. Un perfil honesto con huecos es más útil que uno completo con datos inventados.

    Somos emprendedores en México desarrollando un negocio que combina una aplicación con IA y una página web de venta. Hemos hecho entrevistas de validación:

    INSIGHTS DE ENTREVISTAS:
    La "espiral de revancha" es el verdadero enemigo. Los usuarios carecen de mecanismos de regulación en el momento de la frustración; su única solución actual es el abandono total ("apagar Lichess", "alejarme 20 minutos"). Zaqora no compite contra el análisis de Chess.com; compite contra el botón de "Cerrar ventana".

    SEGMENTO HIPÓTESIS DEL PAIN-GAIN MAP (semana 2):
    El dolor de perder partidas y el dolor social de la soberbia son suficientemente distintos de «no sé qué estudiar» como para probarlos en paralelo (dos framings de landing) antes de apostar todo el roadmap a la currícula de planes.

    OPORTUNIDAD EN UNA ORACIÓN:
    Existe una oportunidad para los jugadores amateur que necesitan ayuda en el entendimiento de las posiciones de ajedrez porque hoy es frustrante únicamente memorizar jugadas.

    Construye el perfil de segmento accionable en cuatro capas. Para cada dato indica si es VERIFICADO (viene de entrevistas o fuentes reales) o HIPÓTESIS (razonado pero sin confirmar). Si una capa no tiene evidencia suficiente, indícalo — no la inventes.

??? abstract "Respuesta completa — Ronda 1 (Claude)"
    **Nota metodológica previa:** Solo tengo tres insumos: (1) un extracto citado de entrevistas sobre la "espiral de revancha", (2) una hipótesis de trabajo del pain-gain map (semana 2, ya etiquetada como hipótesis por el propio equipo), y (3) una oración de oportunidad sin fuente explícita. No hay transcripciones completas, ni conteo de entrevistados, ni datos demográficos crudos. Eso limita fuertemente las Capas 1 y 4.

    **CAPA 1 — DEMOGRÁFICA**
    ¿Quién es con suficiente detalle para encontrarlo?
    · Juega ajedrez online en plataformas como Lichess (y probablemente Chess.com) → VERIFICADO (mención directa de "apagar Lichess" y referencia comparativa a Chess.com)
    · Es jugador "amateur" (no profesional/titulado) → HIPÓTESIS (aparece en la oración de oportunidad, sin cita de entrevista que lo respalde)
    · Rango de edad, género, ubicación geográfica, nivel socioeconómico, ocupación → SIN EVIDENCIA — no inventar. 
    · Nivel de habilidad (ELO aproximado, tiempo jugando ajedrez) → SIN EVIDENCIA

    *Esta capa está incompleta a propósito: hoy no podrías construir un anuncio segmentado por edad/ubicación/ingreso con lo que tienes. Es la capa con mayor déficit de evidencia.*

    **CAPA 2 — CONDUCTUAL**
    ¿Qué hace hoy para resolver el problema — proceso exacto, frecuencia, herramientas, workarounds?
    · Cuando pierde o se frustra, su único mecanismo es abandonar la sesión por completo ("apagar Lichess") → VERIFICADO
    · Como alternativa, se aleja físicamente de la actividad ("alejarme 20 minutos") en lugar de regular la frustración dentro del juego → VERIFICADO
    · No tiene un mecanismo de regulación emocional en el momento de la frustración — el abandono es la única herramienta disponible → VERIFICADO
    · Su método actual de estudio/mejora es memorizar jugadas (aperturas, líneas) en lugar de entender posiciones → HIPÓTESIS 
    · Usa o conoce las funciones de análisis post-partida de Chess.com como referencia de mercado → HIPÓTESIS 

    **CAPA 3 — PSICOGRÁFICA**
    ¿Qué le preocupa en sus propias palabras? ¿Qué lo motivaría a cambiar de solución?
    · Nombra su propio patrón de tilt/revancha compulsiva como el enemigo real, más que la falta de herramientas analíticas → VERIFICADO ("espiral de revancha")
    · Citas textuales de coping: "apagar Lichess", "alejarme 20 minutos" → VERIFICADO — muestran evitación como respuesta emocional, no resolución
    · Existe una dimensión de dolor social ligada a la soberbia (vergüenza/orgullo frente a otros jugadores) distinta del dolor de perder → HIPÓTESIS EXPLÍCITA del equipo
    · Qué lo motivaría concretamente a cambiar de solución → SIN EVIDENCIA

    **CAPA 4 — ECONÓMICA**
    ¿Cuánto le cuesta el problema hoy? ¿Cuánto podría pagar? ¿Quién decide la compra?
    · Costo actual del problema, Disposición a pagar, Quién decide la compra, Comparables de precio de la categoría → SIN EVIDENCIA
    *Esta capa no tiene ningún dato del equipo. No es que esté "débil": está vacía.*

    ────────────────────────────────────────────────────────
    **NIVEL DE CONOCIMIENTO DEL SEGMENTO:**

    *   **Capas con mayoría VERIFICADA:** Capa 2 (Conductual) y Capa 3 (Psicográfica).
    *   **Capas con mayoría de HIPÓTESIS o sin evidencia:** Capa 1 (Demográfica) y Capa 4 (Económica).

    **HIPÓTESIS CRÍTICAS SIN VERIFICAR:**
    1. **El dolor social de la soberbia es un segmento distinto y suficientemente fuerte.** Es la apuesta de mayor riesgo del pain-gain map.
    2. **Que el usuario memoriza jugadas en vez de entender posiciones como método actual de estudio.** Se usa como la justificación central de la oportunidad, pero no está citada como testimonio directo.
    3. **Que existe disposición y capacidad de pago suficiente para sostener el negocio.** Es la hipótesis de mayor impacto en viabilidad y la que menos evidencia tiene de las tres.

    **PERFIL EN UNA ORACIÓN:**
    *"Jugador de ajedrez online (Lichess) que, al perder o frustrarse, no tiene forma de regular esa frustración dentro del juego y solo sabe abandonar la sesión — perfil que aún no puedo describir por edad, ubicación, ingreso ni disposición de pago porque esa evidencia no existe todavía."*

---

### Paso 2 — Dimensionamiento TAM / SAM / SOM 

**Herramienta:** Perplexity (Búsqueda de mercado con fuentes reales).

??? quote "Prompt completo — Ronda 2 (Perplexity, TAM/SAM/SOM)"
    Actúa como analista de mercado con especialización en dimensionamiento para startups de software en América Latina. Tu metodología es el enfoque top-down con triangulación de fuentes verificables: INEGI, CEPAL, BID, reportes de industria con autor y año identificables. No inventes cifras — si no existe fuente verificable para un número, lo señalas y explicas cómo estimarlo con lógica de primer principio.

    Somos emprendedores en México:
    Concepto: Zaqora, empresa de un videojuego para aprender ajedrez y que construye su propia historia en base al usuario.
    Segmento objetivo: Jugador de ajedrez online (Lichess) que, al perder o frustrarse, no tiene forma de regular esa frustración dentro del juego y solo sabe abandonar la sesión.
    Precio estimado del producto/servicio: 300 MXN
    Modelo de ingresos: suscripción mensual, suscripción anual y freemium con upsell
    Mercado inicial: México
    Expansión potencial: LATAM en año 3+

    Construye TAM, SAM y SOM con este razonamiento explícito:
    TAM: Universo total con el problema Y disposición de pago. No solo "cuántos tienen el problema" — cuántos pagarían. Mostrar la reducción paso a paso con fuente de cada número.
    SAM: El subconjunto alcanzable con el modelo actual. Especificar exactamente qué lo reduce: geografía, canal, precio, idioma, tamaño mínimo de cliente.
    SOM: La porción realista en los primeros 2 años. Justificar el porcentaje con lógica de go-to-market concreta: cuántos vendedores, qué canal, qué geografía piloto. El número sin lógica no sirve.

??? abstract "Respuesta completa — Ronda 2 (Perplexity)"
    **DIMENSIONAMIENTO DE MERCADO**
    Concepto: Zaqora - videojuego narrativo para aprender ajedrez y regular la frustración después de perder partidas online.
    Mercado base: México. Precio de referencia: 300 MXN mensuales (3,600 MXN anuales).

    **TAM — Mercado Total Direccionable**
    Universo de partida: 100.2 millones (usuarios mexicanos de internet, INEGI 2024).
    ↓ Filtro 1 (Personas que juegan videojuegos): 68.7 millones (The CIU 2024).
    ↓ Filtro 2 (Afinidad por estrategia/rompecabezas): 28.9 millones (42.1% de gamers móviles, The CIU).
    ↓ Filtro 3 (Juegan ajedrez online): 1.37 millones (Supuesto base: 2% de los gamers).
    ↓ Filtro 4 (Frustración post-derrota): 824,400 (Supuesto: 60% de jugadores frecuentes).
    ↓ Filtro 5 (Disposición de pago): 82,440 compradores potenciales (Supuesto: 10% de conversión).
    *Universo final TAM:* 82,440 personas.
    *Valor anual TAM base:* 296.8 millones de MXN (82,440 x 3,600 MXN).

    **SAM — Mercado Alcanzable**
    Filtros aplicados al TAM:
    · Geografía (Solo México) e Idioma: se mantiene en 82,440.
    · Dispositivo (Smartphone/Navegador compatible): reduce a 65,952 (aplica filtro del 80%).
    · Capacidad de pago (Suscripciones saturadas): se mantiene el 10% optimista.
    *Universo SAM:* 65,952 personas.
    *Valor anual SAM:* 237.4 millones de MXN.

    **SOM — Mercado Obtenible (años 1–2)**
    *Meta:* 1,200 clientes pagadores.
    *Porcentaje del SAM:* 1.82%.
    *Lógica de go-to-market:* 2 personas en ventas/alianzas; 40 aliados (clubes/streamers) activados en 2 años, generando 30 clientes cada uno (40 x 30 = 1,200). Piloto en CDMX, Edomex, NL, Jalisco y Puebla.
    *Valor anual:* 4.32 millones de MXN (teóricos, antes de churn y descuentos).

    ────────────────────────────────────────────────────────
    **SEÑAL DE VIABILIDAD:**
    SOM × precio anual = 4.32 millones MXN.
    ¿Cubre costos operativos básicos de una startup de 4 personas?
    **Marginal.** Puede cubrir una operación muy austera, pero el ingreso real será menor por freemium, descuentos y cancelaciones, produciendo unos 2.4-3.24 millones efectivos.

    **FUENTES UTILIZADAS:**
    · INEGI, ENDUTIH 2024.
    · The Competitive Intelligence Unit, Evolución del Gaming Móvil 2024.
    · Bango/3Gem, Subscription Wars 2024.
    · Lichess, End of Year Update 2025.

---

### Paso 3 — Análisis Competitivo

**Herramienta:** Perplexity (Mapa de inteligencia competitiva de tres capas).

??? quote "Prompt completo — Ronda 3 (Perplexity, Mapa Competitivo)"
    Actúa como analista de inteligencia competitiva especializado en mercados de producto digital en América Latina. Tu metodología identifica tres capas de competidores con énfasis en actores reales y con tracción observable — no en listados genéricos de industria ni en productos que no han lanzado. Para cada competidor buscas su debilidad específica para el segmento del equipo, no sus debilidades generales.

    Somos emprendedores en México con un negocio que combina una aplicación con IA y una página web de venta.
    Concepto: Zaqora, empresa de un videojuego para aprender ajedrez y que construye su propia historia en base al usuario.
    Segmento objetivo: Jugador de ajedrez online (Lichess) que, al perder o frustrarse, no tiene forma de regular esa frustración dentro del juego y solo sabe abandonar la sesión.
    Dolor ⭐ que resolvemos: Frustración al perder.
    Precio estimado: 300 MXN.

    Mapea los tres tipos con evidencia real y observable:
    - DIRECTOS (mínimo 3): misma solución, mismo usuario.
    - INDIRECTOS (mínimo 3): diferente solución, mismo problema.
    - SUSTITUTOS (mínimo 2): cómo resuelve el usuario sin ningún producto similar al nuestro.

    Para cada competidor: Nombre y descripción (1 oración), Dónde opera, Precio o modelo de ingresos, y Su debilidad específica para nuestro segmento.

??? abstract "Respuesta completa — Ronda 3 (Perplexity, Mapa Competitivo)"
    ════════════════════════════════════════════════════════
    MAPA COMPETITIVO — ZAQORA
    Segmento: Jugador de ajedrez online (Lichess/Chess.com) que abandona la sesión por frustración tras perder
    ════════════════════════════════════════════════════════

    **DIRECTOS**
    *(Misma solución: videojuego de ajedrez con narrativa + mismo usuario: jugador frustrado que necesita regulación emocional)*
    1. **Chess Story** — Aventura de ajedrez offline con modo historia por capítulos y países, pero sin adaptación emocional ni IA narrativa — Opera en: Global (Google Play MX) — Precio: Gratis con compras in-app — **Debilidad específica:** La narrativa es preescrita y genérica, no responde al estado emocional del usuario ni construye historia basada en sus derrotas; el jugador frustrado no encuentra validación emocional ni transformación de su pérdida en progreso narrativo.
    2. **AI Dungeon + Chess (combinación usuario)** — Plataforma de narrativa IA que usuarios adaptan manualmente para incluir ajedrez mediante scripts como BronzeChess — Opera en: Global — Precio: Freemium ($9.99-19.99/mes) — **Debilidad específica:** Requiere que el usuario configure manualmente la experiencia; no hay integración nativa ajedrez-emoción-narrativa, y el jugador frustrado no tiene la energía cognitiva ni el interés en "construir" su propia herramienta en estado de *tilt*.
    3. **Story Time Chess** — Juego de tablero físico con narrativa para niños que enseña ajedrez mediante historias — Opera en: Global (envío a MX) — Precio: ~$60-80 USD — **Debilidad específica:** Diseñado para niños de 4+ años sin experiencia; el jugador online frustrado (adolescente/adulto) lo percibe como infantil y no resuelve su dolor emocional post-derrota en plataformas digitales.

    **INDIRECTOS**
    *(Diferente solución: coaching/entrenamiento emocional — mismo problema: frustración y abandono post-derrota)*
    1. **Chess.com Game Review + Lessons** — Análisis de partidas y lecciones estructuradas con componente psicológico implícito — Opera en: Global (fuerte presencia en MX/LATAM) — Precio: $49.99-79.99 USD/año — **Debilidad específica:** El análisis es técnico y frío; no hay acompañamiento emocional explícito ni transformación de la frustración en narrativa; el usuario en *tilt* recibe datos ("perdiste aquí") sin validación, lo que intensifica la autocrítica negativa.
    2. **Chess Coach Pro / Chessy (AI Coach apps)** — Apps de coaching IA que analizan partidas y dan feedback personalizado — Opera en: Global (App Store MX) — Precio: $7.99/mes o $49.99-79.99 USD/año — **Debilidad específica:** Se enfocan en mejora técnica (aperturas, tácticas), no en regulación emocional; el jugador en *tilt* necesita primero calmarse, no que le digan "tu error fue en la jugada 23".
    3. **MyMentalCoach / Chess Psychology Training** — Servicios de coaching psicológico especializado en ajedrez (humano o contenido guiado) — Opera en: Global — Precio: Desde $50-150 USD/sesión — **Debilidad específica:** Requiere iniciativa proactiva del usuario (buscar, agendar, pagar); el jugador frustrado que abandona la sesión no va a buscar un coach psicológico en ese momento.

    **SUSTITUTOS**
    *(Comportamientos naturales de regulación sin software especializado)*
    1. **Regla de "2 derrotas = cerrar la app"** — Comportamiento documentado en comunidades: el usuario se autoimpone detenerse tras 2 pérdidas consecutivas — **Costo para el usuario:** Tiempo perdido (sesión abortada sin aprendizaje ni cierre emocional) + frustración acumulada que se traslada a otras actividades; no hay transformación, solo evitación.
    2. **Análisis manual post-enfriamiento** — El usuario espera 30+ minutos, luego revisa la partida solo o con motor — **Costo para el usuario:** 20-60 minutos adicionales + carga cognitiva emocional de autoanalizarse sin guía; muchos abandonan este proceso por ser doloroso, perpetuando el ciclo de frustración.

    ────────────────────────────────────────────────────────
    **EL COMPETIDOR MÁS PELIGROSO:**
    **La "Regla de 2 derrotas = cerrar la app" (Sustituto #1)**

    *   **Por qué es difícil de desplazar:** Cero fricción (no requiere descargas ni pagos); inmediato (se activa en el instante exacto del dolor); validación social en comunidades (Reddit, foros); y es 100% gratuito.
    *   **Qué tendría que ofrecer Zaqora para que el usuario cambie:**
        1. *Intervención en el momento exacto:* Acceso o integración fluida previa a cerrar la sesión.
        2. *Validación emocional inmediata:* Reconocer y normalizar el estado de *tilt* en los primeros 30 segundos.
        3. *Transformación narrativa en tiempo real:* Convertir la derrota específica en un "capítulo" de su historia personal.
        4. *Cero fricción de adopción:* Onboarding de 1-2 minutos máximo.
        5. *Precio anclado a valor:* $300 MXN posicionado como "menos que una sesión de coaching tradicional".

    *Nota de Océano Azul:* No se identificaron competidores directos con tracción observable en México/LATAM que combinen videojuego de ajedrez + narrativa IA adaptativa + regulación emocional post-derrota, confirmando un espacio blanco comercial.

---

### Paso 4 — Lienzo Estratégico (Océano Azul)

**Herramienta:** Claude (Lienzo estratégico Blue Ocean y Marco de las Cuatro Acciones).

??? quote "Prompt completo — Ronda 4 (Claude, Lienzo Estratégico Blue Ocean)"
    Actúa como estratega de innovación con experiencia en Blue Ocean Strategy aplicada a startups de software en mercados emergentes latinoamericanos. Tu especialidad es construir lienzos estratégicos que revelan la diferenciación real — no la que el equipo quiere ver sino la que los datos del mercado sugieren. Aplicas el Marco de las Cuatro Acciones (Eliminar / Reducir / Incrementar / Crear) antes de construir el lienzo, porque el lienzo es la consecuencia del marco, no el punto de partida. Cuando el equipo no tiene ventaja en un atributo, lo puntúas bajo — la honestidad del lienzo es su único valor real.

    Tenemos este mapa competitivo:
    [Se insertó el Mapa Competitivo del Paso 3, detallando actores directos, indirectos y el sustituto principal: "Regla de 2 derrotas = cerrar la app"]

    Nuestro concepto: Zaqora, empresa de un videojuego para aprender ajedrez y que construye su propia historia en base al usuario.
    Capacidades diferenciales del equipo: Conexión con base de datos y aprendizaje LLM. Así como desarrollo de aplicaciones con IA.
    Segmento accionable: Jugador de ajedrez online (Lichess) que, al perder o frustrarse, no tiene forma de regular esa frustración dentro del juego y solo sabe abandonar la sesión.

    Con estos insumos construye el lienzo estratégico Blue Ocean en dos pasos:
    PASO 1 — MARCO DE LAS CUATRO ACCIONES (Eliminar, Reducir, Incrementar, Crear con justificación).
    PASO 2 — LIENZO ESTRATÉGICO (Atributos, Tabla de Puntuación de 1 a 5, Lectura del Lienzo, Advertencia de Océano Rojo y Pregunta clave para el equipo).

??? abstract "Respuesta completa — Ronda 4 (Claude)"
    ════════════════════════════════════════════════════════
    LIENZO ESTRATÉGICO BLUE OCEAN
    Concepto: Zaqora · Segmento: Jugador de ajedrez online en Lichess que, tras perder y frustrarse, no tiene forma de regular esa emoción dentro del juego y solo sabe cerrar la sesión.
    ════════════════════════════════════════════════════════

    ## MARCO DE LAS CUATRO ACCIONES

    **ELIMINAR — el concepto no ofrecerá:**
    · **Sistema de ranking/rating competitivo interno:** El segmento ya tiene un rating en Lichess que es, precisamente, la fuente de su frustración. Añadir otro número que lo compare reproduce la presión que buscamos aliviar. El equipo puntúa bajo aquí a propósito: no es un descuido, es una decisión estratégica.

    **REDUCIR — el concepto ofrecerá muy por debajo del estándar:**
    · **Profundidad de análisis técnico post-partida:** Chess.com Game Review y las apps de coaching IA han llevado esto al extremo para el jugador que quiere mejorar en frío. El jugador en tilt no tiene esa energía; darle un desglose técnico profundo en ese instante intensifica la autocrítica. Zaqora ofrecerá una versión mínima y opcional.

    **INCREMENTAR — el concepto ofrecerá muy por encima del estándar:**
    · **Validación emocional inmediata post-derrota:** Ningún competidor directo, indirecto o sustituto lo hace bien. Chess.com Lessons es frío; Chess Story es genérico; la "regla de 2 derrotas" ofrece alivio por evitación. Este es el atributo que el segmento valora más y que nadie está sirviendo.

    **CREAR — el concepto introducirá por primera vez:**
    · **Motor narrativo adaptativo basado en datos reales (vía LLM):** Ningún competidor convierte la derrota específica que el usuario acaba de vivir en un capítulo de una historia que evoluciona con su historial real. Esto es posible por la capacidad diferencial del equipo, no por especulación.

    ────────────────────────────────────────────────────────
    ## ATRIBUTOS DEL LIENZO:

    1. **Profundidad técnica del análisis post-partida** — qué tan detallado es el desglose.
    2. **Ranking/sistema competitivo interno** — existencia de un rating dentro de la app.
    3. **Facilidad de onboarding sin configuración previa** — tiempo y pasos hasta obtener valor.
    4. **Validación emocional inmediata post-derrota** — reconocimiento explícito de la frustración.
    5. **Transformación narrativa personalizada de la derrota** — la partida perdida se convierte en historia propia.
    6. **Integración nativa con la sesión de juego** — capacidad de intervenir sin que el usuario salga de la plataforma.
    7. **Motor narrativo adaptativo vía LLM + datos históricos** — la historia se construye con el patrón real de derrotas.
    8. **Precio accesible vs. valor percibido** — relación costo/beneficio frente a alternativas de coaching.

    ## TABLA DE PUNTUACIÓN (1=muy bajo · 5=muy alto):

    | Atributo | Chess.com Lessons | Chess Story | Regla "2 derrotas" | Zaqora |
    |---|:---:|:---:|:---:|:---:|
    | Profundidad técnica análisis | 5 | 1 | 1 | 2 |
    | Ranking/sistema competitivo interno | 4 | 1 | 1 | 0 |
    | Facilidad de onboarding | 3 | 4 | 5 | 4 |
    | Validación emocional inmediata | 1 | 1 | 2 | 5 |
    | Transformación narrativa personalizada | 1 | 2 | 1 | 5 |
    | Integración nativa con la sesión | 1 | 0 | 5 | 3 |
    | Motor narrativo adaptativo (LLM) | 0 | 1 | 0 | 5 |
    | Precio accesible vs. valor | 3 | 4 | 5 | 3 |

    *(Nota: el atributo ELIMINADO puntúa 0 para el concepto. Los atributos CREADOS puntúan 0 donde ningún competidor lo ofrece).*

    ────────────────────────────────────────────────────────
    ## LECTURA DEL LIENZO:

    La curva de Zaqora se distancia radicalmente de la competencia al liderar en **Validación emocional inmediata (5)**, **Transformación narrativa personalizada (5)** y la introducción exclusiva del **Motor narrativo adaptativo vía LLM (5)**, mientras decide deliberadamente no competir y puntuar cero en **Ranking/sistema competitivo interno (0)**.

    **El océano azul en una oración:**
    Zaqora no compite por ser mejor coach técnico ni mejor app de ajedrez narrativo genérico; crea un espacio nuevo donde la derrota específica del usuario, en el momento exacto en que ocurre y sin salir de su sesión, se transforma en parte de una historia personal construida con sus propios datos.

    **ADVERTENCIA DE OCÉANO ROJO:**
    En *facilidad de onboarding*, Zaqora empata con Chess Story (4) y queda por debajo de la "regla de 2 derrotas" (5). Si el equipo compite por fricción de instalación como argumento de venta, terminará en una guerra contra un hábito gratuito que ya ganó esa batalla por diseño. También hay una brecha honesta en *integración nativa con la sesión* (3 vs. 5 del hábito de "cerrar la app").

    **PREGUNTA CLAVE PARA EL EQUIPO:**
    ¿Es técnica y comercialmente viable construir una integración lo suficientemente cercana a la sesión de Lichess (overlay, extensión o notificación instantánea post-derrota) en el MVP? Si el usuario debe abrir una app aparte, el argumento de desplazar a la "regla de 2 derrotas" se debilita.

---

### Paso 5 — La Propuesta de Valor (IDEO / Bain)

**Herramienta:** Claude (Síntesis de propuesta de valor con framework IDEO y Pirámide de Bain).

??? quote "Prompt completo — Ronda 5 (Claude, Propuesta de Valor)"
    Actúa como estratega de marca y comunicación con experiencia construyendo propuestas de valor para productos de software en etapa early-stage en mercados latinoamericanos. Tu metodología combina el framework Insightful/Unique/Targeted de IDEO con la Pirámide de Valor de Bain: una propuesta sólida opera en el nivel funcional como mínimo, aspira al emocional, y es articulable en una oración que cualquier persona puede memorizar y repetir sin haber visto el producto.

    Los criterios que no negocias:
    ✅ Nombra al usuario específico — no "nuestros clientes"
    ✅ Nombra el resultado concreto que obtiene — no la feature
    ✅ Implica por qué esta solución y no otra disponible
    ❌ No usa: plataforma, solución integral, innovador, de última generación, revolucionario, ecosistema
    ❌ No describe el producto — describe el valor que entrega

    Somos emprendedores en México con un negocio que combina una aplicación con IA y una página web de venta.
    Insumos del análisis de hoy:
    - PERFIL DE SEGMENTO: Jugador de ajedrez online (Lichess) que, al perder o frustrarse, no tiene forma de regular esa frustración dentro del juego y solo sabe abandonar la sesión.
    - DOLOR ⭐ Y GANANCIA ⭐: Dolor: Frustración por perder y soberbia de otros jugadores. Ganancia: Aprender sin presión y crear una narrativa.
    - EL COMPETIDOR MÁS PELIGROSO: La "Regla de 2 derrotas = cerrar la app".
    - PRECIO ESTIMADO: 300 MXN.

    Con estos insumos construye la propuesta de valor en tres pasos:
    PASO 1 — NIVEL EN LA PIRÁMIDE DE BAIN.
    PASO 2 — VALIDACIÓN IDEO (Insightful, Unique, Targeted).
    PASO 3 — TRES VERSIONES (Funcional, Emocional, La más fuerte) en máximo 25 palabras y justificadas. Finaliza con la diferencia entre Oferta y Propuesta de Valor.

??? abstract "Respuesta completa — Ronda 5 (Claude)"
    ════════════════════════════════════════════════════════
    PROPUESTA DE VALOR — ZAQORA
    ════════════════════════════════════════════════════════

    **NIVEL EN PIRÁMIDE DE BAIN:**
    *   **Nivel actual:** Emocional.
    *   **Justificación:** El atributo que domina el lienzo (validación emocional inmediata) no es una feature funcional sino un alivio afectivo en el momento exacto de la derrota — eso define el nivel en el que compite hoy.
    *   **Oportunidad de subir:** Sí, pero con cautela. El motor narrativo adaptativo podría empujar hacia lo transformador (el usuario empieza a leer sus derrotas como progreso de una identidad), pero prometer esto ahora sin evidencia de retención real sería exagerar.

    **EVALUACIÓN IDEO:**
    *   **Insightful ✅** — Nadie en el mapa (directo, indirecto o sustituto) valida la frustración en los primeros 30 segundos; es el hueco real, no uno inventado.
    *   **Unique ✅** — El motor narrativo vía API de Lichess + LLM que usa el historial real del usuario es difícil de replicar rápido: exige integración técnica y diseño narrativo a la vez.
    *   **Targeted ⚠️** — El segmento está bien definido por comportamiento, pero el propio análisis advierte que si el MVP es una app separada y no un overlay, Zaqora no llega al usuario en el instante que lo define.

    ────────────────────────────────────────────────────────
    **VERSIÓN 1 — FUNCIONAL:**
    *"Al jugador de Lichess que cierra la app tras perder, Zaqora convierte esa derrota en el próximo capítulo de su historia."*
    *   **Fuerza:** Es verificable — describe una acción concreta del producto.
    *   **Limitación:** Omite la validación emocional inmediata, sonando a narrativa genérica más.

    **VERSIÓN 2 — EMOCIONAL:**
    *"Para el jugador de Lichess que cierra la app tras perder, Zaqora valida tu frustración en segundos y la convierte en tu historia."*
    *   **Fuerza:** Nombra el dolor exacto del segmento y ofrece alivio en el instante donde hoy no recibe ninguno.
    *   **Riesgo:** "Valida tu frustración" puede sonar a promesa terapéutica.

    **VERSIÓN 3 — LA MÁS FUERTE:**
    *"Cuando pierdes en Lichess y estás por cerrar la app, Zaqora valida tu frustración y la convierte en el próximo capítulo de tu historia."*
    *   **Por qué esta es la más fuerte:** Intercepta al usuario en el instante de decisión que el análisis identifica como el campo de batalla real — antes de cerrar la sesión — y en esa misma oración entrega tanto el resultado funcional como el emocional, algo que V1 y V2 lograban por separado pero no juntas.

    ────────────────────────────────────────────────────────
    **OFERTA vs. PROPUESTA DE VALOR:**

    *   **Oferta del producto (qué venden):** "Una app con inteligencia artificial que genera una historia narrativa personalizada a partir de tus partidas de ajedrez en Lichess, usando tu historial real de derrotas y victorias."
    *   **Propuesta de valor (por qué lo compran):** "Cuando pierdes en Lichess y estás por cerrar la app, Zaqora valida tu frustración y la convierte en el próximo capítulo de tu historia."

    **La diferencia en una línea:**
    La oferta describe *qué* hace el motor; la propuesta describe *cuándo y por qué* el usuario la elige en vez de cerrar la app — el sujeto pasa del producto a la persona en el momento exacto del dolor, apuntando directamente al hábito gratuito que hoy gana esa pelea.

---

## 4) Entregable — Canvas de Mercado


| Sección del Canvas | Componente | Descripción y Hallazgos |
| :--- | :--- | :--- |
| **SEGMENTO ACCIONABLE** | **Demográfica** | Jugadores de ajedrez online (Lichess/Chess.com) de nivel amateur (intermedios y avanzados en desarrollo), mayoritariamente adultos jóvenes en México. |
| | **Conductual** | Cuando pierden o se frustran, no regulan la emoción dentro de la plataforma y su único workaround es abandonar la sesión por completo («cerrar Lichess» o alejarse 20 minutos). |
| | **Psicográfica** | Sienten frustración intensa ante la derrota y la soberbia de jugadores más experimentados; atrapados en la espiral de revancha, reconocen que saben que deben parar pero terminan empeorando su rendimiento y humor. |
| | **Económica** | Costo medido en tiempo perdido, caídas severas de rating en malas rachas y frustración acumulada; disposición a pagar estimada en torno a 300 MXN mensuales (comparable con alternativas de coaching o suscripciones de valor). |
| | **Hipótesis críticas** | Que el usuario prefiera una experiencia narrativa frente a la inercia del hábito gratuito de cerrar la app, y que la integración técnica permita capturarlo en el instante exacto del *tilt*. |
| **TAMAÑO DE MERCADO** | **TAM** | **82,440 personas** con el problema y disposición de pago en México · *Fuente:* INEGI, The CIU y estimación de conversión sobre usuarios activos. |
| | **SAM** | **65,952 personas** · *Filtros:* Usuarios con dispositivos compatibles y alcance geográfico nacional en México. |
| | **SOM (Año 1-2)** | **1,200 clientes pagadores** (1.82% del SAM) · *Lógica:* Canales de adquisición mediante aliados clave (clubes y streamers) y estrategias de *go-to-market* piloto en zonas urbanas principales. |
| **MAPA COMPETITIVO** | **Directos (3)** | • **Chess Story:** Narrativa genérica y preescrita, sin adaptación al estado emocional ni integración de datos reales de derrotas.<br>• **AI Dungeon + Chess:** Requiere configuración manual compleja por usuario, careciendo de integración nativa.<br>• **Story Time Chess:** Enfocado puramente en niños pequeños, inadecuado para jugadores online adultos. |
| | **Indirectos (3)** | • **Chess.com Game Review + Lessons:** Análisis frío y estrictamente técnico que intensifica la autocrítica sin validación emocional.<br>• **Chess Coach Pro / Chessy:** Centrados exclusivamente en tácticas y aperturas, ignorando por completo la regulación emocional del *tilt*.<br>• **MyMentalCoach / Chess Psychology Training:** Solución reactiva que exige proactividad y presupuesto elevado por sesión, llegando tarde al momento crítico. |
| | **Sustitutos (2)** | • **Regla de «2 derrotas = cerrar la app»:** Costo de tiempo perdido, sesión abortada sin aprendizaje ni cierre, y frustración trasladada a otras actividades.<br>• **Análisis manual post-enfriamiento:** Costo de 20 a 60 minutos adicionales de carga cognitiva y autoevaluación dolorosa sin guía experta. |
| | **El más peligroso** | El sustituto de la **«Regla de 2 derrotas = cerrar la app»** por su total ausencia de fricción, inmediatez absoluta, gratuidad y validación dentro de la comunidad de ajedrez. |
| **LIENZO BLUE OCEAN** | **Atributos (6–7)** | Profundidad técnica del análisis, Ranking interno, Facilidad de onboarding, Validación emocional inmediata, Transformación narrativa personalizada, Integración nativa con la sesión, Motor narrativo adaptativo (LLM), Relación precio/valor. |
| | **Tabla de puntuación** | Liderazgo contundente de Zaqora en validación emocional (5), narrativa personalizada (5) y motor LLM adaptativo (5), con puntaje cero en ranking competitivo interno para evitar la presión. |
| | **El hueco azul** | Zaqora crea un espacio donde la derrota específica del usuario, en el momento exacto en que ocurre y sin salir de su sesión, se transforma en parte de una historia personal construida con sus propios datos. |
| **PROPUESTA DE VALOR** | **Oferta técnica** | Una aplicación con inteligencia artificial que genera una historia narrativa personalizada a partir de tus partidas de ajedrez en Lichess, usando tu historial real de derrotas y victorias. |
| | **Propuesta de valor** | *«Cuando pierdes en Lichess y estás por cerrar la app, Zaqora valida tu frustración y la convierte en el próximo capítulo de tu historia.»* |
| | **Nivel Pirámide Bain** | Emocional |
| | **Error de la 1ª versión** | Se enfocaba en describir las funcionalidades técnicas o analíticas del producto en lugar de conectar directamente con el sujeto en el momento exacto del dolor emocional frente a su alternativa competitiva. |

---

## 5) Propuesta de valor — versión revisada (v2)

!!! note "Criterios de esta segunda iteración"
    Una propuesta de valor tiene que **sostenerse sola**: entenderse en una lectura, sin contexto previo y sin apoyarse en marcas de terceros para explicarse. Al releer la v1 contra ese estándar aparecieron tres fallas, y de ahí sale esta reescritura. La v1 se conserva arriba para dejar visible la evolución del razonamiento.

### 5.1 Diagnóstico de la v1

> *«Cuando pierdes en Lichess y estás por cerrar la app, Zaqora valida tu frustración y la convierte en el próximo capítulo de tu historia.»*

| Falla | Dónde está | Por qué importa |
| :--- | :--- | :--- |
| **Depende de una marca ajena** | «en Lichess» | Excluye a quien juega en otra plataforma o en tablero físico, y ata el posicionamiento a una plataforma que no controlo. Si el lector no conoce Lichess, la frase pierde su anclaje. |
| **Promesa abstracta** | «valida tu frustración» | No describe nada observable. El usuario no puede imaginar qué pasa en pantalla, y la frase roza el registro terapéutico sin serlo. |
| **Requiere contexto previo** | «el próximo capítulo de tu historia» | Solo se entiende si ya se leyó qué es La Campaña. Una propuesta de valor no puede exigir haber leído las semanas anteriores. |

### 5.2 Tres versiones nuevas (máx. 25 palabras, sin marcas de terceros)

=== "Funcional"

    > *«Zaqora toma la partida que acabas de perder y la convierte en un nivel diseñado contra tu error, para que sigas jugando en vez de cerrar.»*

    **Fuerza:** todo es observable — se entiende qué hace el producto sin conocer el mercado.
    **Limitación:** no dice por qué se elegiría frente al análisis gratuito que ya existe.

=== "Emocional"

    > *«Perder deja de terminar tu sesión: Zaqora transforma tu peor racha en una partida que sí quieres jugar, sin rating y sin nadie mirando.»*

    **Fuerza:** nombra el momento exacto del dolor y el alivio concreto.
    **Limitación:** deja implícito el mecanismo; si no se acompaña, suena a promesa.

=== "La más fuerte ⭐"

    > *«Cuando pierdes y estás por cerrar el tablero, Zaqora convierte esa derrota en el siguiente nivel de tu campaña: juegas contra tu error, sin rating.»*

    **Por qué esta:** intercepta al usuario en el instante de decisión que el análisis identificó como el campo de batalla real; «juegas contra tu error» explica el mecanismo en tres palabras y «sin rating» dice, sin decirlo, por qué esto y no el análisis técnico que hoy existe. No nombra ninguna plataforma: *«el tablero»* funciona igual para quien juega en línea o en persona.

!!! tip "Prueba de autonomía aplicada"
    Criterio: **un lector que no conoce el proyecto, el mercado ni el ajedrez en línea debe entenderla completa en una lectura.** La v2 se verificó eliminando toda palabra que exigiera contexto previo (nombres de plataformas, «capítulo», «validar») y comprobando que cada término restante fuera una acción o un objeto reconocible: *perder*, *cerrar*, *tablero*, *nivel*, *error*, *rating*.

### 5.3 Cómo deja Zaqora de depender de Lichess

La observación no era solo de redacción: el diseño original tenía a la API de Lichess como **única** vía de entrada de datos, lo que convertía a un tercero en punto único de falla (cambio de términos de uso, cierre de la API, o simplemente un usuario que juega en otro sitio). El producto se rediseña con tres vías de captura, en orden de independencia:

| Vía | Cómo entra la partida | Dependencia externa |
| :--- | :--- | :--- |
| **1. Tablero propio (núcleo)** | El usuario juega los niveles de la campaña dentro de Zaqora; el error se detecta sobre partidas generadas en casa. | **Ninguna.** Zaqora funciona completa aunque no exista ningún conector. |
| **2. Importación de PGN** | El usuario sube o pega el archivo PGN de cualquier partida. El PGN es un formato abierto y estándar, no propiedad de nadie. | **Ninguna.** Cubre cualquier plataforma, torneo presencial o app. |
| **3. Conectores opcionales** | APIs públicas de plataformas en línea para sincronizar el historial automáticamente. | **Sustituible.** Son una comodidad de *onboarding*, no el motor. Si una cae, quedan las vías 1 y 2. |

**Consecuencia para el segmento:** el perfil deja de describirse como «jugador de Lichess» y pasa a describirse por conducta — *jugador amateur de ajedrez en línea que, tras perder, abandona la sesión porque no tiene forma de seguir jugando sin arriesgar su rating*. La conducta es la que define el mercado; la plataforma donde ocurre es un detalle de implementación.

!!! note "Actualización del Canvas"
    La fila **PROPUESTA DE VALOR** del Canvas de la sección 4 queda reemplazada por la v2:
    *«Cuando pierdes y estás por cerrar el tablero, Zaqora convierte esa derrota en el siguiente nivel de tu campaña: juegas contra tu error, sin rating.»*
    La **oferta técnica** se reformula sin marca ajena: *«Una aplicación con IA que genera una campaña narrativa personalizada a partir de tus propias partidas, jugadas en Zaqora o importadas desde cualquier plataforma.»*

---

## 6) Reflexión

- **Los números de mercado se ven más sólidos de lo que son.** El TAM/SAM/SOM salió de encadenar supuestos de conversión sobre datos de INEGI y The CIU. La cifra final (82,440 personas) es defendible solo si el supuesto va escrito al lado; sin él, es una cifra prestada. Aprendí a no presentar un número sin su cadena de derivación.
- **El competidor más peligroso no era un producto.** Todo el mapa competitivo apuntaba a apps, y el análisis terminó señalando un hábito gratuito: cerrar la sesión después de dos derrotas. Competir contra una costumbre exige un producto que llegue en el momento exacto, no uno con más funciones.
