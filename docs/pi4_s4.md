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

**Herramienta:** Perplexity.

Como en el paso siguiente, este dimensionamiento se trabajó en **dos rondas con prompts de autoría distinta**: el prompt del profesor (mercado mexicano en pesos, enfoque *top-down*) y uno propio (mercado global en dólares, *top-down* y *bottom-up*). Al final se comparan ambos.

??? quote "Prompt completo — Ronda 2, prompt del profesor (Perplexity, TAM/SAM/SOM)"
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

??? abstract "Respuesta completa — Ronda 2, prompt del profesor (Perplexity)"
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

#### Segunda ronda — prompt de autoría propia

Los bloques anteriores corresponden al **prompt provisto por el profesor**, que dimensiona el mercado mexicano en pesos a partir del segmento conductual. A continuación se repite el ejercicio con un **prompt escrito por mí**, que pide el dimensionamiento global en dólares combinando enfoque *top-down* y *bottom-up* con fuentes oficiales. La comparación de ambos cierra esta sección.

??? quote "Prompt completo — versión propia (Perplexity, TAM/SAM/SOM global)"
    Actúa como un analista de mercado e inversiones especializado en valoraciones para startups. Tu objetivo es calcular e investigar el TAM (Total Addressable Market), SAM (Serviceable Addressable Market) y SOM (Serviceable Obtainable Market) para el siguiente negocio:

    Videojuego de ajedrez que sirve para aprender y divertirse

    Para entregar el análisis, debes seguir estrictamente estas reglas:

    **1. METODOLOGÍA DE CÁLCULO**
    Utiliza una combinación de enfoque Top-Down (de arriba hacia abajo usando datos macroeconómicos) y Bottom-Up (de abajo hacia arriba usando precio medio de venta × número de clientes potenciales).
    Muestra explícitamente las fórmulas matemáticas que utilizaste para llegar a cada número.

    **2. INVESTIGACIÓN Y FUENTES REALES**
    Todos los datos macroeconómicos, tamaño del sector, tasa de crecimiento (CAGR) y número de empresas/consumidores deben provenir de fuentes oficiales y reconocidas (por ejemplo: Statista, Grand View Research, IBISWorld, McKinsey, Banco Mundial, informes de asociaciones del sector o entidades gubernamentales).
    Incluye el nombre de la fuente y el año del informe o dato utilizado junto a cada cifra relevante. Si no tienes un dato exacto de la fuente, indica la suposición (*assumption*) de manera explícita y lógica.

    **3. ESTRUCTURA DE LA RESPUESTA**
    TAM (Mercado Total Direccionable): Define la oportunidad global o regional total de la industria.
    SAM (Mercado Direccionable Servible): Filtra el TAM según el segmento de mercado específico al que realmente podemos atender según geografía, perfil de cliente o modelo de negocio actual.
    SOM (Mercado Alcanzable Servible): Estima la cuota de mercado realista que la empresa puede capturar en un horizonte de 3 a 5 años, considerando la competencia, capacidad operativa y presupuesto de marketing.

    **4. TABLA RESUMEN FINAL**
    Presenta los resultados finales en una tabla con las siguientes columnas:
    | Métrica | Valor Monetario (USD) | Metodología / Fórmula | Fuentes / Justificación |

??? abstract "Respuesta completa — versión propia (Perplexity)"
    **Alcance y supuestos**

    El producto se analiza como un videojuego digital multiplataforma de ajedrez, con aprendizaje integrado, modelo potencial *freemium* y monetización mediante suscripción, compra única o contenido premium.

    !!! warning "Advertencia de la propia herramienta"
        Las cifras son estimaciones de mercado, no una valoración financiera definitiva. El resultado depende especialmente de: precio medio anual por usuario de pago · porcentaje de jugadores de ajedrez interesados en aprender · geografías atendidas · capacidad de adquisición y retención · modelo de monetización elegido.

    Para evitar mezclar mercados no comparables se utilizan dos referencias: **mercado amplio** (industria global de videojuegos) y **mercado específico** (mercado global del ajedrez, que incluye productos digitales, físicos, educación, torneos y servicios relacionados).

    - Fortune Business Insights estimó el **mercado global del ajedrez en 3,450 millones de USD en 2025**, con un CAGR previsto del **9.28%** entre 2026 y 2034.
    - Como referencia del mercado digital, Newzoo estimó los ingresos globales de videojuegos de 2024 en **182,700 millones de USD**, con un CAGR de ~3.3% entre 2024 y 2027.

    ────────────────────────────────────────────────────────
    **TAM — Mercado Total Direccionable**

    *Enfoque top-down.* El TAM más defendible es el mercado global de ajedrez:

    > **TAM top-down = 3,450 millones de USD anuales** *(Fortune Business Insights, 2025)*

    Este valor es deliberadamente amplio: incluye productos físicos, digitales y servicios educativos, por lo que no todo el TAM es capturable por un videojuego. Proyección a cinco años con el CAGR publicado:

    > 3,450 × (1 + 0.0928)⁵ ≈ **5,400 millones de USD en 2030**
    > *Supone que el CAGR publicado para 2026-2034 se mantiene durante los cinco años.*

    *Enfoque bottom-up.* Se parte de la base de usuarios de Chess.com, que comunicó **más de 243 millones de miembros al 31 de diciembre de 2025**. Como no todos son activos ni todos pagarían, se aplican supuestos explícitos:

    | Variable | Valor | Origen |
    | :--- | :--- | :--- |
    | Miembros registrados | 243 millones | Chess.com Board Report, Q4 2025 |
    | Interesados en una experiencia de aprendizaje gamificada | 25% | *Assumption* |
    | Precio medio anual equivalente | 30 USD | *Assumption* (≈2.50 USD/mes) |

    > 243,000,000 × 0.25 × 30 USD = **1,823 millones de USD anuales**

    *TAM seleccionado.* Para planificación financiera se toma el **resultado bottom-up (1,823 millones)**, porque representa mejor el mercado monetizable de usuarios digitales interesados en aprender ajedrez. El dato top-down de 3,450 millones funciona como techo sectorial, pero incluye categorías que el producto no puede atender directamente.

    ────────────────────────────────────────────────────────
    **SAM — Mercado Direccionable Servible**

    Se supone que la primera versión estará disponible en Estados Unidos y Canadá, Europa Occidental, Australia y Nueva Zelanda, y Latinoamérica con soporte en español e inglés; distribución digital en PC, móvil y posiblemente consolas; público infantil, juvenil, familiar y adulto principiante.

    La ITU estimó ~6,000 millones de usuarios de Internet en 2025 (74% de la población mundial). Para no asumir que todo usuario conectado es cliente de videojuegos, se usa la base de Chess.com como *proxy* de interés demostrado en ajedrez.

    - **Filtro geográfico.** No existe desglose público de los 243 millones de miembros por geografía, así que se aplica una hipótesis prudente: **60%** pertenece a geografías atendibles por idioma, pagos, distribución y soporte → 243M × 0.60 = **145.8 millones de usuarios atendibles**.
    - **Filtro de interés por aprendizaje.** Duolingo informó en su carta a accionistas del 2T de 2025 que su curso de ajedrez superó **1 millón de usuarios activos diarios** solo en iOS y en inglés, poco después de su lanzamiento — valida la demanda por combinar ajedrez, aprendizaje y gamificación. Se mantiene el supuesto del **25%** de interés → 145.8M × 0.25 = **36.45 millones de usuarios**.

    > 145,800,000 × 0.25 × 30 USD = **1,094 millones de USD anuales**

    ────────────────────────────────────────────────────────
    **SOM — Mercado Alcanzable Servible**

    El SOM debe reflejar una empresa nueva que compite con Chess.com, Lichess, Duolingo Chess, apps móviles de tácticas y entrenamiento, videojuegos de ajedrez tradicionales y plataformas educativas de contenido gratuito. Por eso **no se aplica una cuota genérica del 1% o 5%**, sino una estimación *bottom-up* de usuarios de pago alcanzables.

    *Supuestos operativos a cinco años:* 25 millones de USD de inversión acumulada en producto, contenido, marketing y operaciones · adquisición principalmente digital y orgánica · conversión a pago del 3% de los registros captados · 1.5 millones de registros acumulados al quinto año · 30 USD de ingreso anual medio por usuario de pago.

    > 1,500,000 registros ÷ 145,800,000 atendibles ≈ **1.03%** de los usuarios geográficamente atendibles de Chess.com — ambicioso, pero más realista que suponer una cuota elevada frente a operadores establecidos.
    >
    > 1,500,000 × 3% = 45,000 usuarios de pago × 30 USD = **SOM base: 1.35 millones de USD anuales**

    *Escenario alternativo.* Si el producto alcanza 5 millones de registros y convierte al 5%:

    > 5,000,000 × 5% = 250,000 × 30 USD = **SOM alto: 7.5 millones de USD anuales**

    El SOM representa **ingresos recurrentes anualizados** al final del horizonte de 3 a 5 años, no ingresos acumulados del período. El SOM base equivale a ~**0.12% del SAM**; la baja cuota es coherente con un producto nuevo en una categoría dominada por plataformas con cientos de millones de usuarios.

    ────────────────────────────────────────────────────────
    **Tabla resumen final**

    | Métrica | Valor monetario (USD) | Metodología / Fórmula | Fuentes / Justificación |
    | :--- | :--- | :--- | :--- |
    | **TAM top-down** | 3,450 millones anuales | Tamaño de industria reportado | Fortune Business Insights, dato 2025: el mercado global del ajedrez se estimó en 3,450 millones de USD. |
    | **TAM proyectado 2030** | 5,400 millones anuales | 3,450 × (1 + 0.0928)⁵ | CAGR de 9.28% publicado por Fortune Business Insights para 2026-2034. |
    | **TAM bottom-up (seleccionado)** | 1,823 millones anuales | 243M miembros × 25% × 30 USD | Chess.com reportó más de 243 millones de miembros a diciembre de 2025. El 25% de interés y los 30 USD anuales son *assumptions* explícitas. |
    | **SAM** | 1,094 millones anuales | 243M × 60% × 25% × 30 USD | 60% geográficamente atendible y 25% interesado son *assumptions*. Compatible con ~6,000 millones de usuarios de Internet en 2025 según ITU. |
    | **SOM base (año 3-5)** | 1.35 millones anuales | 1.5M registros × 3% × 30 USD | *Assumptions* operativas de startup: 1.5 millones de registros acumulados, 3% de conversión y ARPU anual de 30 USD. |
    | **SOM alto (año 3-5)** | 7.5 millones anuales | 5M registros × 5% × 30 USD | Escenario de ejecución fuerte, sujeto a mayor inversión, distribución y retención. |

    **Interpretación para inversión.** La oportunidad es suficientemente grande para justificar la creación de una empresa: el TAM sectorial supera los 3,000 millones de USD y el SAM monetizable estimado supera los 1,000 millones. Sin embargo, **el principal riesgo no es el tamaño del mercado, sino la distribución**: Chess.com ya cuenta con más de 243 millones de miembros y Duolingo demostró una adopción inicial muy rápida de su producto de ajedrez. La tesis de inversión debería centrarse en una diferenciación clara: narrativa y progresión propias de un videojuego · mejor experiencia infantil y familiar · aprendizaje adaptativo con IA · modo historia, personajes, recompensas y competición · distribución mediante escuelas, creadores de contenido y plataformas educativas · enfoque en mercados donde las plataformas dominantes tengan menor localización.

    Estas cifras deben actualizarse después de validar con métricas reales de adquisición, retención a 30/90 días, conversión a pago y costo de adquisición de cliente.

    ??? note "Fuentes principales citadas por Perplexity"
        fortunebusinessinsights.com/chess-market-113098 · newzoo.com (Global Games Market Update, Q2 2025) · chess.com/board-reports/2025-q4 · itu.int (Statistics 2025) · investors.duolingo.com (carta a accionistas 2T 2025)

#### Comparación de los dos prompts

| | **Prompt del profesor** (bloques anteriores) | **Prompt propio** |
| :--- | :--- | :--- |
| **Unidad de medida** | Personas con el problema en México, valorizadas en MXN. | Dinero de la categoría a nivel global, en USD. |
| **Definición del producto** | Zaqora con su segmento conductual: quien abandona la sesión tras perder. | Genérica: «videojuego de ajedrez que sirve para aprender y divertirse». |
| **Metodología exigida** | Solo *top-down*, con embudo de filtros explícito y fuente por número. | *Top-down* **y** *bottom-up*, con las fórmulas matemáticas a la vista. |
| **Fuentes** | INEGI, The CIU, Bango/3Gem — nacionales y recientes. | Fortune Business Insights, Newzoo, Chess.com Board Report, ITU, Duolingo — sectoriales y globales, con enlace verificable. |
| **Resultado TAM** | 82,440 personas · 296.8 millones MXN anuales. | 1,823 millones de USD anuales. |
| **Resultado SAM** | 65,952 personas · 237.4 millones MXN anuales. | 1,094 millones de USD anuales. |
| **Resultado SOM** | 1,200 clientes · 4.32 millones MXN anuales (años 1-2). | 1.35 millones USD base / 7.5 millones USD alto (años 3-5). |
| **Lógica del SOM** | *Go-to-market* concreto: 2 personas en ventas, 40 aliados × 30 clientes, piloto en cinco estados. | Conversión del 3% sobre 1.5 millones de registros, con 25 millones de USD de inversión acumulada. |

**Qué aportó cada uno**

- **No miden lo mismo, y esa es la lección principal.** Uno cuenta *personas con un dolor específico en un país*; el otro cuenta *dinero de una categoría en el mundo*. Puestos lado a lado parecen contradecirse, pero responden a preguntas distintas: el primero sirve para planear la operación del primer año, el segundo para argumentar ante un inversionista que la categoría es lo bastante grande.
- **Mi prompt gana en trazabilidad, el del profesor en pertinencia.** Pedir las fórmulas explícitas y fuentes reconocidas produjo una cadena auditable: cada cifra se puede recalcular y cada supuesto está etiquetado como *assumption*. En cambio, al describir el producto de forma genérica («aprender y divertirse»), el mercado que dimensiona no es el de Zaqora, sino el de cualquier videojuego de ajedrez — un número grande que no me pertenece.
- **El embudo del profesor encadena supuestos sin fuente.** Los filtros de 2% (juegan ajedrez online), 60% (frustración post-derrota) y 10% (disposición de pago) son estimaciones sin respaldo; multiplicados entre sí determinan prácticamente todo el resultado. Su virtud es que apuntan exactamente al usuario de Zaqora; su riesgo es que un error en cualquiera de los tres mueve el TAM en un orden de magnitud.
- **Exigir *top-down* y *bottom-up* a la vez sirvió de control cruzado.** Los dos caminos dieron 3,450 y 1,823 millones de USD: una brecha de casi el doble que obligó a justificar cuál usar y por qué. El prompt del profesor, al pedir un solo método, no tiene con qué contrastar su propio resultado.
- **Escala incomparable en el SOM, por un supuesto que no es mío.** El SOM global de 1.35 millones de USD anuales equivale a unos 24 millones de MXN —cerca de seis veces el SOM nacional de 4.32 millones—, pero descansa en 25 millones de USD de inversión acumulada a cinco años, una cifra ajena a la realidad de este proyecto. El SOM del profesor, con dos personas en ventas y 40 aliados, es el único de los dos que puedo defender como plan.
- **Coinciden en el riesgo de fondo.** Ambos análisis concluyen que el problema no es el tamaño del mercado sino la distribución frente a plataformas con cientos de millones de usuarios. Esa coincidencia, viniendo de dos marcos y dos geografías distintas, es la conclusión más sólida del paso.

!!! note "Nota sobre la conversión de divisas"
    La comparación entre pesos y dólares es orientativa: se usó un tipo de cambio de referencia aproximado de 18 MXN/USD únicamente para poder contrastar los órdenes de magnitud, no como supuesto financiero del proyecto.

---

### Paso 3 — Análisis Competitivo

**Herramienta:** Perplexity.

Este paso se trabajó en **dos rondas con prompts de autoría distinta**: primero el prompt provisto por el profesor (mapa de inteligencia competitiva en tres capas) y después uno propio, planteado desde el marco de Océano Azul. Al final se comparan ambos.

??? quote "Prompt completo — Ronda 3, prompt del profesor (Perplexity, Mapa Competitivo)"
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

??? abstract "Respuesta completa — Ronda 3, prompt del profesor (Perplexity, Mapa Competitivo)"
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

#### Segunda ronda — prompt de autoría propia

Los bloques anteriores corresponden al **prompt provisto por el profesor** para este bloque, con la estructura de mapa competitivo en tres capas. A continuación se repite el ejercicio con un **prompt escrito por mí**, que ataca el mismo objetivo desde el marco de Océano Azul (matriz de las cuatro acciones y curva de valor) en lugar del mapa de tres capas. La comparación de ambos cierra esta sección.

??? quote "Prompt completo — versión propia (Perplexity, Análisis Competitivo y Océano Azul)"
    Actúa como un estratega experto en negocios y posicionamiento de mercado. Tu objetivo es ayudarme a desarrollar el Análisis Competitivo y Estrategia de Océano Azul para mi proyecto.

    Información de mi proyecto:
    Nombre/Idea de negocio: Zaqora — videojuego de ajedrez donde tú escribes tu propia historia
    Producto/Servicio principal: Videojuego para aprender ajedrez que arma una historia en base a tus partidas
    Público objetivo: Jugadores de ajedrez que suelen perder partidas
    Competidores principales conocidos: Chess Story, AI Dungeon + Chess y Story Time Chess

    Por favor, genera lo siguiente:

    **Matriz de Análisis Competitivo:**
    Identifica a los competidores directos e indirectos clave.
    Analiza sus fortalezas, debilidades, propuesta de valor y modelo de precios.

    **Diagnóstico del «Océano Rojo»:**
    Resume los factores principales en los que compite la industria actualmente y por qué el mercado está saturado o commodificado en esos puntos.

    **Matriz de las Cuatro Acciones (Estrategia Océano Azul):**
    Eliminar: Factores que la industria da por sentados pero que no aportan valor real.
    Reducir: Factores que se pueden reducir muy por debajo del estándar de la industria para bajar costos.
    Incrementar: Factores que deben elevarse muy por encima del estándar del mercado.
    Crear: Factores completamente nuevos que la industria nunca ha ofrecido para abrir una nueva demanda.

    **Curva de Valor y Propuesta Divergente:**
    Redacta una propuesta de valor única basada en las cuatro acciones anteriores, explicando cómo este enfoque nos saca de la competencia directa y nos posiciona en un espacio de mercado no disputado.

    Por favor, presenta la información de forma visual utilizando tablas donde aplique y puntos clave para facilitar su lectura.

??? abstract "Respuesta completa — versión propia (Perplexity)"
    **Análisis competitivo de Zaqora**

    Zaqora no debería posicionarse como «otra plataforma para aprender ajedrez». Su oportunidad está en convertir cada partida —especialmente una derrota— en una experiencia narrativa, emocional y educativa que motive al jugador a volver y mejorar.

    !!! warning "Advertencia de la propia herramienta"
        La información pública sobre Chess Story es limitada y puede referirse a productos distintos. Conviene validar sus características y precios antes de usar este análisis en un *pitch* formal.

    **1. Matriz competitiva**

    | Competidor | Tipo | Propuesta de valor | Fortalezas | Debilidades / oportunidad para Zaqora | Modelo de precios observado |
    | :--- | :--- | :--- | :--- | :--- | :--- |
    | **Chess Story / Chess2Story** | Directo | Convierte una partida de ajedrez en una historia ilustrada, con capítulos, personajes, arco dramático y ejercicios tácticos. | Combina análisis ajedrecístico con narrativa; ofrece análisis ilimitado, *teasers*, personajes y ejercicios. | Puede sentirse como un informe generado después de jugar, no como una aventura interactiva durante el aprendizaje. La personalización emocional y la progresión del jugador pueden ser limitadas. | Gratis con funciones básicas; historias desde ~2.79 USD; planes de 9, 19 y 39 USD al mes. |
    | **AI Dungeon + Chess** | Directo / sustituto | Usa IA generativa para crear aventuras abiertas y narrativas controladas por el jugador. | Gran libertad narrativa, alta rejugabilidad y capacidad de improvisación. | No está diseñado específicamente para enseñar ajedrez; separa la historia de la calidad de las decisiones en el tablero. La IA puede producir narrativas inconsistentes o poco pedagógicas. | Plan gratuito y suscripciones desde 14.99 USD mensuales; niveles superiores hasta 99.99 USD. |
    | **Story Time Chess** | Indirecto fuerte | Enseña ajedrez a niños mediante cuentos, personajes, piezas especiales y actividades físicas. | Excelente accesibilidad para principiantes; aprendizaje basado en cuentos; fuerte atractivo familiar. | Orientado principalmente a niños pequeños y a una experiencia de mesa. No resuelve el problema del jugador digital que pierde partidas y quiere comprender sus errores. | Juego físico ~39.99 USD; planes digitales de 15.99 y 22.99 USD mensuales según el contenido. |
    | **Chess.com / Lichess** | Indirecto | Jugar, estudiar, analizar partidas, resolver tácticas y competir en línea. | Gran base de usuarios, contenido abundante, análisis, rankings y efectos de red. | Experiencia centrada en rendimiento, rating y volumen de funciones; puede aumentar la frustración del jugador que pierde. La narrativa personal no es el centro del producto. | Lichess gratuito; Chess.com con funciones gratuitas y planes premium. |
    | **Lecciones y cursos de ajedrez** | Sustituto | Enseñanza estructurada mediante videos, ejercicios, entrenadores o profesores. | Profundidad pedagógica, autoridad de instructores y rutas de aprendizaje claras. | Menor interactividad emocional; normalmente no transforma los errores del usuario en una experiencia memorable. | Pago único, membresía o clases individuales, según el proveedor. |
    | **Videojuegos narrativos y RPG** | Sustituto | Ofrecen progresión, personajes, decisiones, recompensas y una historia que evoluciona. | Alta capacidad de *engagement* y retención; el jugador tiene una razón emocional para continuar. | Generalmente no enseñan ajedrez ni conectan narrativa con decisiones estratégicas reales. | Freemium, pago único, DLC o suscripción. |

    **Lectura estratégica.** Los competidores cubren dos extremos: **ajedrez educativo y competitivo** (precisión, rating, tácticas, progreso medible) y **narrativa interactiva** (libertad, personajes, drama, exploración). Zaqora puede ocupar el espacio entre ambos: *un juego narrativo en el que la calidad de tus decisiones ajedrecísticas cambia la historia.*

    ────────────────────────────────────────────────────────
    **2. Diagnóstico del Océano Rojo**

    | Factor dominante | Cómo compite la industria | Por qué está saturado |
    | :--- | :--- | :--- |
    | Rating y ranking | Se usan como medida principal de progreso. | Todas las plataformas ofrecen algún sistema de puntuación; es difícil diferenciarse únicamente por Elo. |
    | Cantidad de partidas | Se incentiva jugar más y acumular actividad. | La oferta es abundante y muchas partidas son intercambiables para el usuario. |
    | Análisis técnico | Se muestran evaluaciones de motor, errores, mejores jugadas y variantes. | Los motores están ampliamente disponibles y la información puede resultar intimidante para principiantes. |
    | Tácticas y puzzles | Ejercicios repetitivos para mejorar patrones. | Es funcionalidad estándar en casi todos los servicios importantes. |
    | Clases y videos | Se venden cursos, lecciones y contenido educativo. | Existe una enorme cantidad de contenido gratuito y de bajo costo. |
    | Competencia online | Torneos, partidas rápidas, rankings y desafíos. | Modelo dominado por plataformas con grandes comunidades y efectos de red. |
    | Suscripción | Se monetiza el acceso a análisis, contenido o funciones premium. | El usuario compara precios entre muchas plataformas similares. |
    | Precisión del motor | Se promete detectar los errores más importantes. | La precisión por sí sola no crea una experiencia emocional ni garantiza que el jugador aprenda. |

    **Problema central del mercado.** La industria trata la derrota como un dato: *«Perdiste porque tu evaluación cayó de +0.8 a −2.4.»* Para quien suele perder, esa explicación no responde: ¿en qué momento cambió realmente mi partida?, ¿qué estaba intentando hacer?, ¿qué patrón de error repito?, ¿cómo evito sentir que cada derrota es un fracaso?, ¿por qué debería jugar otra partida después de perder? **Ahí aparece la oportunidad: hacer que una derrota sea el inicio de una historia y no el final de una sesión.**

    ────────────────────────────────────────────────────────
    **3. Matriz de las Cuatro Acciones**

    | Acción | Decisiones estratégicas para Zaqora | Resultado esperado |
    | :--- | :--- | :--- |
    | **Eliminar** | La dependencia del rating como protagonista de la experiencia; el lenguaje excesivamente técnico; las listas interminables de variantes que el usuario no entiende. | Menor ansiedad y una experiencia más accesible para jugadores frustrados. |
    | **Reducir** | Funciones competitivas secundarias, tablas de clasificación, estadísticas vanidosas y análisis que no conducen a una acción concreta. | Menores costos de desarrollo y una experiencia más enfocada. |
    | **Incrementar** | La explicación contextual de los errores; la sensación de progreso; la personalización de personajes; la conexión entre una decisión del tablero y sus consecuencias; la calidad de los momentos de aprendizaje. | Mayor comprensión, motivación y retención. |
    | **Crear** | Una historia persistente basada en las partidas; personajes que representan patrones de juego; mundos y conflictos que cambian según las decisiones; capítulos de «revancha»; misiones diseñadas alrededor de errores recurrentes; un diario personal del jugador. | Nueva demanda entre jugadores que quieren mejorar pero no disfrutan del entrenamiento tradicional. |

    !!! example "Aplicación concreta propuesta"
        Después de una partida, Zaqora podría mostrar algo como:

        *«En el movimiento 18 abandonaste la defensa de la torre para atacar al rey enemigo. La maniobra parecía valiente, pero dejó abierto el paso hacia tu propio rey. En la historia, el consejo de la ciudad interpreta ese momento como una ruptura de confianza. En tu próxima misión tendrás que aprender a reconocer ataques prematuros.»*

        La clave es que la narrativa **no sustituya** al análisis ajedrecístico: debe traducirlo a una explicación que el jugador pueda recordar y aplicar.

    ────────────────────────────────────────────────────────
    **4. Curva de valor** — escala orientativa: 1 = bajo, 5 = alto.

    | Factor competitivo | Plataformas tradicionales | Chess Story | AI Dungeon + Chess | Story Time Chess | **Zaqora propuesto** |
    | :--- | :---: | :---: | :---: | :---: | :---: |
    | Juego competitivo | 5 | 2 | 1 | 1 | **3** |
    | Profundidad técnica | 5 | 3 | 1 | 2 | **3** |
    | Cantidad de puzzles | 5 | 4 | 1 | 2 | **3** |
    | Narrativa personalizada | 1 | 4 | 5 | 4 | **5** |
    | Consecuencias de las jugadas | 1 | 3 | 3 | 2 | **5** |
    | Progresión emocional | 2 | 3 | 4 | 4 | **5** |
    | Relevancia para jugadores que pierden | 2 | 3 | 2 | 1 | **5** |
    | Aprendizaje desde errores propios | 4 | 4 | 1 | 2 | **5** |
    | Libertad creativa | 1 | 3 | 5 | 3 | **4** |
    | Fricción y complejidad de uso | 4 | 3 | 2 | 3 | **2** |

    **Interpretación.** La curva debe ser deliberadamente distinta: no intentar ganar en cantidad de usuarios, funciones competitivas o profundidad técnica frente a Chess.com y Lichess; no intentar ganar a AI Dungeon en libertad narrativa general; no competir con Story Time Chess por el segmento infantil y familiar. **Dominar la conexión entre partida, error, historia y deseo de revancha.**

    ────────────────────────────────────────────────────────
    **5. Propuesta divergente**

    > **Propuesta de valor.** Zaqora convierte tus partidas de ajedrez en una aventura personal: cada jugada crea consecuencias, cada error revela un patrón de aprendizaje y cada derrota desbloquea una nueva oportunidad para cambiar tu historia.

    A diferencia de las plataformas tradicionales, Zaqora no presenta la derrota únicamente como una caída de rating. La convierte en: un capítulo jugable · una explicación comprensible del momento decisivo · una misión específica para corregir el error · una consecuencia dentro de un mundo persistente · una razón emocional para volver a intentarlo.

    **Posicionamiento recomendado.** *Para jugadores de ajedrez que suelen perder y se sienten frustrados con el entrenamiento tradicional, Zaqora es el videojuego narrativo que transforma sus partidas reales en una historia interactiva de aprendizaje, donde mejorar no significa solo subir el rating, sino cambiar el destino de su propio mundo.*

    **Espacio de mercado no disputado.** Zaqora puede crear una categoría propia: **«Ajedrez narrativo de superación personal.»** No sería principalmente una plataforma de torneos, ni un entrenador técnico tradicional, ni un generador de historias desconectadas del tablero, ni un producto infantil para aprender las reglas. Sería un sistema híbrido de: videojuego narrativo + entrenador basado en errores reales + simulador de decisiones y consecuencias + experiencia emocional de progreso.

    **Recomendaciones de enfoque para el producto inicial:** (1) importar o jugar una partida real, para que el usuario comience desde una experiencia propia; (2) detectar un único momento decisivo, evitando sobrecargarlo con diez errores técnicos; (3) convertirlo en una misión de revancha: practicar el patrón y volver a jugar una situación similar.

    **Métricas propuestas más allá del rating:** porcentaje de usuarios que vuelven después de perder · errores recurrentes corregidos · misiones completadas · partidas de revancha jugadas · retención a 7 y 30 días · percepción del jugador sobre su mejora y confianza.

    **Ventaja competitiva más difícil de copiar:** no la IA en sí, sino el conjunto de *memoria narrativa del jugador + historial de errores + mundo persistente + sistema de misiones personalizado*.

    ??? note "Fuentes citadas por Perplexity"
        chess2story.com/pricing · help.aidungeon.com/memberships-benefits · home.storytimechess.com · vat19.com/item/story-time-chess · storytimechess.com.au · dreamgen.com/blog/articles/ai-dungeon-review · dungeonsdeep.ai/blog/ai-dungeon-review-2026 · techshark.io/tools/ai-dungeon · store.steampowered.com/app/2002270 · smarterlearningguide.com/story-time-chess-review · prnewswire.com (Story Time Chess Level 2-3) · toolradar.com/tools/ai-dungeon/pricing

#### Comparación de los dos prompts

| | **Prompt del profesor** (bloques anteriores) | **Prompt propio** |
| :--- | :--- | :--- |
| **Rol asignado a la IA** | Analista de inteligencia competitiva en mercados digitales de LATAM. | Estratega de negocios y posicionamiento de mercado. |
| **Marco de salida exigido** | Mapa de tres capas: directos, indirectos y **sustitutos**, con mínimos por capa. | Océano Azul completo: matriz competitiva, diagnóstico de océano rojo, cuatro acciones y curva de valor. |
| **Contexto que entrega** | Segmento definido **por conducta** (abandona la sesión tras perder), dolor, precio y país. | Idea, producto, público general y una lista de competidores ya escogidos por mí. |
| **Restricción metodológica** | Exige actores **reales con tracción observable** y una debilidad específica para *nuestro* segmento. | Pide formato visual y tablas, sin restringir la evidencia. |
| **Resultado característico** | Identifica al competidor más peligroso: un **hábito gratuito** («2 derrotas = cerrar la app»). | Cuantifica la diferenciación en una **curva de valor** y define qué eliminar, reducir, incrementar y crear. |

**Qué aportó cada uno**

- **El prompt del profesor encuentra competidores que no son productos.** Al obligar a incluir una capa de sustitutos, aparece el hallazgo que sostiene toda la semana: el rival real es el gesto de cerrar la app, no otra empresa. Mi prompt nunca pidió esa capa, y por eso su matriz contiene únicamente productos — ninguna de sus seis filas es un comportamiento del usuario.
- **Mi prompt fuerza una decisión, no solo un diagnóstico.** La matriz de las cuatro acciones obliga a nombrar qué se va a **eliminar y reducir**, no únicamente qué hacer mejor. De ahí salen decisiones que el mapa competitivo no exigía: quitar el rating como protagonista y recortar funciones competitivas secundarias para bajar costos.
- **Mi prompt trajo precios con fuente verificable** (enlaces a las páginas de precios de cada competidor), mientras que el mapa de tres capas dio rangos de precio sin referencia. En sentido inverso, mi prompt aceptó como «competidores conocidos» los tres que yo ya había elegido, sin cuestionar si eran los correctos — sesgo que el prompt del profesor evita al pedirle a la IA que los descubra.
- **Coinciden en el núcleo del posicionamiento.** Dos prompts distintos, con marcos distintos, llegan a la misma frontera: la derrota como punto de partida y no como final de sesión. Esa coincidencia es la señal más fuerte de que el ángulo es sólido, porque no depende de cómo se formuló la pregunta.

**Limitación que ambos comparten:** ninguno verificó la existencia real de los competidores. La propia respuesta advierte que la información sobre Chess Story «es limitada y puede referirse a productos distintos» — el análisis sirve para orientar la estrategia, no para sostener un *pitch* sin validación previa.

---

### Paso 4 — Lienzo Estratégico (Océano Azul)

**Herramienta:** Claude.

Como en los pasos 2, 3 y 5, este lienzo se trabajó en **dos rondas con prompts de autoría distinta**: el prompt del profesor (lienzo contra competidores concretos) y uno propio (metodología canónica de Kim & Mauborgne contra la industria promedio). Al final se comparan ambos.

??? quote "Prompt completo — Ronda 4, prompt del profesor (Claude, Lienzo Estratégico Blue Ocean)"
    Actúa como estratega de innovación con experiencia en Blue Ocean Strategy aplicada a startups de software en mercados emergentes latinoamericanos. Tu especialidad es construir lienzos estratégicos que revelan la diferenciación real — no la que el equipo quiere ver sino la que los datos del mercado sugieren. Aplicas el Marco de las Cuatro Acciones (Eliminar / Reducir / Incrementar / Crear) antes de construir el lienzo, porque el lienzo es la consecuencia del marco, no el punto de partida. Cuando el equipo no tiene ventaja en un atributo, lo puntúas bajo — la honestidad del lienzo es su único valor real.

    Tenemos este mapa competitivo:
    [Se insertó el Mapa Competitivo del Paso 3, detallando actores directos, indirectos y el sustituto principal: "Regla de 2 derrotas = cerrar la app"]

    Nuestro concepto: Zaqora, empresa de un videojuego para aprender ajedrez y que construye su propia historia en base al usuario.
    Capacidades diferenciales del equipo: Conexión con base de datos y aprendizaje LLM. Así como desarrollo de aplicaciones con IA.
    Segmento accionable: Jugador de ajedrez online (Lichess) que, al perder o frustrarse, no tiene forma de regular esa frustración dentro del juego y solo sabe abandonar la sesión.

    Con estos insumos construye el lienzo estratégico Blue Ocean en dos pasos:
    PASO 1 — MARCO DE LAS CUATRO ACCIONES (Eliminar, Reducir, Incrementar, Crear con justificación).
    PASO 2 — LIENZO ESTRATÉGICO (Atributos, Tabla de Puntuación de 1 a 5, Lectura del Lienzo, Advertencia de Océano Rojo y Pregunta clave para el equipo).

??? abstract "Respuesta completa — Ronda 4, prompt del profesor (Claude)"
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

#### Segunda ronda — prompt de autoría propia

Los bloques anteriores corresponden al **prompt provisto por el profesor**, que parte del mapa competitivo del Paso 3 y puntúa a competidores concretos. A continuación se repite el ejercicio con un **prompt escrito por mí**, apegado a la metodología canónica de Kim & Mauborgne: curva de la industria promedio, matriz ERRC, lienzo con justificación por factor y validación con los tres criterios (foco, divergencia y mensaje contundente). La comparación de ambos cierra esta sección.

??? quote "Prompt completo — versión propia (Lienzo Estratégico, Kim & Mauborgne)"
    Actúa como un consultor en estrategia de negocio e innovación especializado en la metodología de la Estrategia del Océano Azul (Chan Kim & Renée Mauborgne). Tu objetivo es ayudarme a construir un Lienzo Estratégico (*Strategy Canvas*) y desarrollar un perfil estratégico divergente para el siguiente negocio:

    Zaqora, empresa de un videojuego para aprender ajedrez y que construye su propia historia en base al usuario. Segmento objetivo: Jugador de ajedrez online (Lichess) que, al perder o frustrarse, no tiene forma de regular esa frustración dentro del juego y solo sabe abandonar la sesión. Dolor ⭐ que resolvemos: Frustración al perder. Precio estimado: 300 MXN.

    Por favor, sigue estrictamente esta estructura paso a paso:

    **1. FACTORES DE COMPETENCIA DE LA INDUSTRIA (Curva de Valor Actual)**
    Identifica de 6 a 8 factores clave en los que la industria actualmente invierte y compite (ej. precio, personalización, velocidad, variedad, complejidad de uso, etc.).
    Asigna una puntuación estimada del 1 (muy bajo) al 5 (muy alto) al competidor promedio/estándar de la industria en cada factor.

    **2. MATRIZ DE LAS 4 ACCIONES (Esquema de las Cuatro Acciones / ERRC)**
    Aplica el marco de trabajo para romper el *trade-off* entre valor y costo:
    ELIMINAR: Factores que la industria da por sentados pero que aportan poco valor real al cliente.
    REDUCIR: Factores que pueden ser reducidos muy por debajo del estándar de la industria para bajar costos.
    INCREMENTAR: Factores que deben elevarse muy por encima del estándar actual para resolver fricciones del usuario.
    CREAR: Factores completamente nuevos que la industria nunca ha ofrecido para atraer a «no clientes».

    **3. LIENZO ESTRATÉGICO EN TABLA (Comparativa de Curvas de Valor)**
    Genera una tabla comparativa ordenando los factores de competencia con la siguiente estructura:
    | Factor de Competencia / Valor | Industria Tradicional (1-5) | Nuestra Propuesta Océano Azul (1-5) | Acción ERRC Aplicada | Justificación Estratégica |

    **4. EVALUACIÓN Y MENSAJE DE LA NUEVA ESTRATEGIA**
    Sintetiza los resultados validando que la nueva curva de valor cumpla con los 3 criterios clave:
    Foco: ¿En cuáles factores específicos se concentra el esfuerzo de la empresa?
    Divergencia: ¿De qué manera la curva de valor se aleja visual y funcionalmente del estándar de la industria?
    Slogan contundente: Redacta una frase impactante, clara y transparente (máximo 12 palabras) que resuma la nueva propuesta de valor.

??? abstract "Respuesta completa — versión propia"
    **Estrategia del Océano Azul: Zaqora**

    **Planteamiento.** Zaqora no compite con Lichess o Chess.com por ser «mejor plataforma de ajedrez». Atiende al jugador que la industria ya pierde: el que cierra la pestaña enojado después de una derrota. Ese jugador es un **no cliente de primer nivel**: juega, pero está a un paso de irse.

    ────────────────────────────────────────────────────────
    **1. Factores de competencia de la industria (curva de valor actual)**

    Se toma como referencia al competidor promedio: Lichess, Chess.com, Chessable y apps de puzzles.

    | # | Factor | Industria (1–5) | Por qué |
    | :---: | :--- | :---: | :--- |
    | 1 | Precio (nivel de cobro) | 3 | Va de gratis (Lichess) a suscripciones premium y cursos caros. |
    | 2 | Ranking ELO y tablas públicas | 5 | Es el centro de la experiencia. El número manda. |
    | 3 | Volumen de contenido (puzzles, cursos, aperturas) | 5 | Compiten por tener bibliotecas enormes. |
    | 4 | Análisis técnico con motor (evaluaciones, líneas) | 5 | Stockfish, precisión en %, *blunders* marcados en rojo. |
    | 5 | Variedad de ritmos y modos (bullet, blitz, torneos, variantes) | 5 | Juego rápido e inmediato, muchas partidas seguidas. |
    | 6 | Personalización del aprendizaje | 2 | Casi siempre es genérica: el mismo curso para todos. |
    | 7 | Progresión y motivación (gamificación) | 3 | Rachas, insignias y puzzles diarios, sin un hilo que les dé sentido. |

    **Lo que nadie ofrece:** qué hacer con la emoción después de perder. La derrota solo aparece como un número de ELO que baja y un análisis frío.

    ────────────────────────────────────────────────────────
    **2. Matriz de las 4 acciones (ERRC)**

    | ELIMINAR | REDUCIR |
    | :--- | :--- |
    | **ELO y tablas públicas:** el juicio público alimenta la frustración. El nivel se calibra de forma interna e invisible.<br><br>**Ritmos hiperrápidos (bullet/blitz):** favorecen el «una más» impulsivo y el *tilt*. | **Volumen de contenido:** menos lecciones, pero elegidas para cada jugador.<br><br>**Análisis técnico con motor:** se reduce a 1 o 2 ideas clave explicadas en lenguaje humano, sin *centipawns*.<br><br>**Precio:** 300 MXN en un solo pago, por debajo de las suscripciones premium anuales. |

    | INCREMENTAR | CREAR |
    | :--- | :--- |
    | **Personalización del aprendizaje:** el juego detecta los errores recurrentes del jugador y construye el reto siguiente a partir de ellos.<br><br>**Progresión y motivación:** cada partida, ganada o perdida, avanza algo que importa. | **Regulación emocional de la frustración:** micro-rituales después de perder (pausa, reencuadre, «¿qué aprendiste?») y un cierre de sesión sano en lugar de huir.<br><br>**Historia adaptativa construida por el jugador:** la narrativa cambia según su estilo, sus errores y sus derrotas. Perder abre capítulos en vez de castigar. |

    ────────────────────────────────────────────────────────
    **3. Lienzo estratégico**

    | Factor de competencia / valor | Industria tradicional (1–5) | Zaqora Océano Azul (1–5) | Acción ERRC | Justificación estratégica |
    | :--- | :---: | :---: | :---: | :--- |
    | Precio (nivel de cobro) | 3 | 2 | Reducir | Un pago único de 300 MXN baja la barrera de entrada y evita la fatiga de las suscripciones. |
    | Ranking ELO y tablas públicas | 5 | 1 | Eliminar | La comparación pública es el detonante principal de la frustración del segmento. |
    | Ritmos hiperrápidos y torneos | 5 | 1 | Eliminar | Favorecen el *tilt* y las revanchas impulsivas, justo lo contrario de regular la emoción. |
    | Volumen de contenido | 5 | 2 | Reducir | Menos contenido, pero relevante, cuesta menos producir y abruma menos al jugador. |
    | Análisis técnico con motor | 5 | 2 | Reducir | Un «−3.2» no enseña a un jugador frustrado. Una idea clara sí. |
    | Personalización del aprendizaje | 2 | 5 | Incrementar | Ataca la causa de las derrotas repetidas: los errores propios, no los genéricos. |
    | Progresión y motivación | 3 | 5 | Incrementar | Si perder también hace avanzar algo, el jugador deja de abandonar la sesión. |
    | Regulación emocional post-derrota | 1 | 5 | Crear | Es el dolor principal que resuelve: da una salida a la frustración dentro del juego. |
    | Historia adaptativa construida por el jugador | 1 | 5 | Crear | Es la diferencia más difícil de copiar. Convierte cada partida en narrativa personal. |

    **Curvas de valor (visualización rápida):**

    ```text
                            1   2   3   4   5
    Precio                  ····I···Z
    ELO público             Z···············I
    Ritmos rápidos          Z···············I
    Volumen contenido       ····Z···········I
    Análisis motor          ····Z···········I
    Personalización         ····I···········Z
    Progresión              ········I·······Z
    Regulación emocional    I···············Z
    Historia adaptativa     I···············Z

    I = Industria   Z = Zaqora
    ```

    Las dos curvas casi se cruzan en espejo: donde la industria está en su punto más alto, Zaqora está en el más bajo, y al revés.

    ────────────────────────────────────────────────────────
    **4. Evaluación de la nueva estrategia**

    **Foco.** La inversión se concentra en tres factores: **regulación emocional después de perder** (el dolor principal), **historia adaptativa** (la diferencia difícil de copiar) y **personalización del aprendizaje** (lo que convierte el alivio emocional en mejora real). Todo lo demás se recorta a propósito, lo que libera recursos: no hace falta competir en motor, volumen ni infraestructura de torneos.

    **Divergencia.** La industria compite en la dimensión competitiva y técnica —rating, velocidad, cantidad, precisión—; Zaqora compite en la dimensión emocional y narrativa. *Visualmente:* la curva de Zaqora es casi el negativo de la de la industria. *Funcionalmente:* en una plataforma tradicional una derrota es un número que baja; en Zaqora es un capítulo que empieza. No es «otro Lichess con mejor diseño», sino otra categoría: **videojuego narrativo de crecimiento a través del ajedrez**.

    **Slogan (11 palabras):**

    > **«Pierde una partida, gana un capítulo: el ajedrez que te entiende.»**

    *Opciones alternativas:* «Aquí perder no te saca del juego: te hace avanzar.» · «Tu historia se escribe con cada derrota.»

#### Comparación de los dos prompts

| | **Prompt del profesor** (bloques anteriores) | **Prompt propio** |
| :--- | :--- | :--- |
| **Contra quién se compara** | Cuatro curvas: Chess.com Lessons, Chess Story, el hábito «2 derrotas» y Zaqora. | Dos curvas: el competidor promedio de la industria y Zaqora. |
| **Insumo de partida** | El mapa competitivo del Paso 3 y las capacidades técnicas del equipo. | Solo el concepto, el segmento, el dolor y el precio. |
| **Atributos resultantes** | Centrados en el mecanismo del producto: *onboarding*, integración nativa con la sesión, motor LLM. | Centrados en cómo compite la industria: ELO público, ritmos rápidos, volumen de contenido, precio. |
| **Trazabilidad ERRC → lienzo** | El marco y el lienzo van en secciones separadas. | Una columna del lienzo indica la acción ERRC de cada factor. |
| **Cierre** | Advertencia de océano rojo + pregunta crítica para el equipo. | Validación de foco y divergencia + eslogan de 11 palabras. |

**Qué aportó cada uno**

- **El del profesor se puede accionar; el mío se puede explicar.** Comparar contra competidores con nombre dice exactamente dónde Zaqora gana y dónde pierde frente a cada uno. Comparar contra una «industria promedio», que es el método canónico de Kim & Mauborgne, muestra algo distinto y también útil: que toda la industria compite en la misma dimensión, y que ahí no hay nada que ganar.
- **Mi lienzo no admite ni una desventaja, y eso es un problema.** Los nueve factores salen a favor de Zaqora, y la conclusión —«la curva es casi el negativo de la industria»— suena contundente precisamente porque nada la contradice. El prompt del profesor incluía una instrucción que el mío no tiene: *cuando el equipo no tiene ventaja en un atributo, puntúalo bajo*. De ahí salen la advertencia de océano rojo y la brecha honesta en integración nativa (3 contra 5 del hábito de cerrar la app), que es el riesgo mayor del proyecto. **Mi lienzo no lo ve porque ni siquiera incluye ese factor.**
- **Mi prompt aporta dos decisiones de producto que el otro no toca:** eliminar los ritmos hiperrápidos —bullet y blitz favorecen la revancha impulsiva, justo lo contrario de regular la emoción— y bajar deliberadamente el nivel de cobro. Ninguna aparecía en el análisis previo.
- **La trazabilidad ERRC → lienzo es la mejora de forma más útil.** Que cada factor cargue su acción (*eliminar, reducir, incrementar, crear*) y su justificación impide el lienzo decorativo donde las puntuaciones se ponen a ojo; cada número queda amarrado a una decisión declarada.
- **El eslogan es el entregable que faltaba.** Kim & Mauborgne exigen tres criterios: foco, divergencia y **mensaje contundente**. El prompt del profesor cubre los dos primeros; sin pedir el tercero, el lienzo queda sin la frase que lo comunica hacia afuera.
- **Segunda aparición del mismo desajuste de precio.** Esta ronda vuelve a tratar los 300 MXN como **pago único** («un pago único de 300 MXN… evita la fatiga de las suscripciones»), igual que la ronda propia del Paso 5, mientras que el dimensionamiento del Paso 2 los asume como **suscripción mensual**. Que la discrepancia aparezca en dos rondas independientes confirma que el modelo de ingresos sigue sin estar definido, y que la definición cambia tanto la estrategia de precio como el tamaño de mercado.
- **Coinciden en las dos decisiones estructurales.** Ambos marcos, por caminos distintos, **eliminan el ranking competitivo** y **crean la narrativa adaptativa**. Son las dos decisiones que sobreviven a cualquier formulación de la pregunta, y por eso son las que definen el producto.

---

### Paso 5 — La Propuesta de Valor (IDEO / Bain)

**Herramienta:** Claude.

Como en los pasos 2 y 3, la propuesta de valor se trabajó en **dos rondas con prompts de autoría distinta**: el prompt del profesor (IDEO + Pirámide de Bain) y uno propio (*Value Proposition Canvas* + fórmula de Geoff Moore). Al final se comparan ambos.

??? quote "Prompt completo — Ronda 5, prompt del profesor (Claude, Propuesta de Valor)"
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

??? abstract "Respuesta completa — Ronda 5, prompt del profesor (Claude)"
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

#### Segunda ronda — prompt de autoría propia

Los bloques anteriores corresponden al **prompt provisto por el profesor**, que sintetiza la propuesta de valor con los marcos IDEO y Pirámide de Bain. A continuación se repite el ejercicio con un **prompt escrito por mí**, construido sobre el *Value Proposition Canvas* de Osterwalder y la fórmula de Geoff Moore, y con entregables listos para usar en la página de venta. La comparación de ambos cierra esta sección.

??? quote "Prompt completo — versión propia (Value Proposition Canvas + Geoff Moore)"
    Actúa como un estratega de marca y especialista en marketing de producto (PMM). Tu objetivo es redactar una propuesta de valor sólida, clara y persuasiva para el siguiente negocio:

    Zaqora, empresa de un videojuego para aprender ajedrez y que construye su propia historia en base al usuario. Segmento objetivo: Jugador de ajedrez online (Lichess) que, al perder o frustrarse, no tiene forma de regular esa frustración dentro del juego y solo sabe abandonar la sesión. Dolor ⭐ que resolvemos: Frustración al perder. Precio estimado: 300 MXN.

    Para desarrollar la propuesta de valor, sigue estrictamente este proceso:

    **1. PERFIL DEL CLIENTE (Value Proposition Canvas)**
    Trabajos del cliente (*Customer Jobs*): ¿Qué intenta lograr el cliente en su día a día o trabajo?
    Dolores (*Pains*): ¿Qué le frustra, obstaculiza o genera riesgo antes, durante o después de intentar resolver su problema?
    Ganancias (*Gains*): ¿Qué resultados o beneficios concretos espera o le sorprenderían positivamente?

    **2. MAPA DEL VALOR**
    Productos/Servicios: Lo que ofrece la empresa para solucionar el problema.
    Aliviadores de dolores (*Pain Relievers*): Cómo el producto elimina explícitamente los dolores identificados.
    Creadores de ganancias (*Gain Creators*): Cómo el producto genera el resultado esperado o supera las expectativas.

    **3. FORMULACIÓN DE LA PROPUESTA DE VALOR**
    La declaración corta (Fórmula de Geoff Moore): «Para [cliente objetivo] que [necesidad o problema], nuestro [nombre del producto/servicio] es un [categoría de mercado] que [beneficio clave/solución]. A diferencia de [competencia/alternativa actual], nosotros [diferenciador clave].»
    Elevator Pitch (2-3 frases): Una versión conversacional, clara y sin jerga técnica para explicar en 30 segundos.
    Titular para sitio web (Landing Page): 1 Titular llamativo (H1) + 1 Subtitular explicativo (H2) + 3 Puntos clave de beneficios (*bullet points*).

    **4. PRUEBA DE ÁCIDO (Validación)**
    Analiza la propuesta generada y responde brevemente:
    ¿Es clara? (¿Se entiende en menos de 5 segundos?)
    ¿Es específica? (¿Evita clichés como «somos los mejores» o «servicio de calidad»?)
    ¿Es diferenciada? (¿Explica por qué elegirte a ti y no a la competencia?)

??? abstract "Respuesta completa — versión propia"
    **Propuesta de valor: Zaqora**

    **1. Perfil del cliente**

    | Dimensión | Contenido |
    | :--- | :--- |
    | **Trabajos funcionales** | Mejorar su rating, entender por qué pierde y aprender aperturas, táctica y finales sin que se le haga pesado. |
    | **Trabajos emocionales** | Disfrutar el ajedrez aunque pierda y sentir que avanza. |
    | **Trabajos sociales** | Que lo vean como un jugador que mejora, no como alguien que se rinde. |

    **Dolores**

    - Pierde una o varias partidas seguidas y lo único que hace es cerrar la sesión.
    - Se enoja, juega partidas rápidas por revancha (*tilt*) y sigue perdiendo rating.
    - La plataforma no le da nada para procesar la derrota: hay análisis técnico, pero nada que atienda cómo se siente.
    - Después de una racha mala vuelve con miedo a jugar, o deja de jugar varios días.
    - Los cursos y puzzles tradicionales le parecen tareas escolares y no lo enganchan.

    **Ganancias**

    - Que perder tenga sentido: sentir que cada derrota sirve para algo.
    - Mejorar su rating y su comprensión del juego.
    - Una experiencia que se sienta suya, adaptada a su estilo y a sus errores.
    - Le sorprendería positivamente que el juego «recordara» sus partidas y las convirtiera en historia.

    ────────────────────────────────────────────────────────
    **2. Mapa del valor**

    **Productos y servicios**

    - Un videojuego de ajedrez con narrativa adaptativa: la historia se construye con las partidas, errores y victorias del jugador.
    - Misiones de aprendizaje (táctica, aperturas, finales) integradas en la trama.
    - Mecánicas de pausa y reflexión después de una derrota.
    - Pago único de 300 MXN, sin suscripción.

    | Dolor identificado | Aliviador de dolor |
    | :--- | :--- |
    | La derrota termina la sesión | Perder no termina la sesión, **abre un capítulo nuevo**: el personaje reacciona, aparece un reto de redención y el jugador tiene una razón para quedarse. |
    | Revancha impulsiva (*tilt*) | En vez de lanzar otra partida rápida, el juego propone **pausas guiadas y misiones cortas de bajo riesgo** que bajan la tensión. |
    | Falta de acompañamiento emocional | El error se convierte en una lección dentro de la historia: *«tu rival explotó la columna abierta; tu mentor te enseña a defenderla»*. |
    | Aburrimiento del entrenamiento | El aprendizaje llega como **progreso narrativo**, no como lista de ejercicios. |

    **Creadores de ganancias**

    - **Progreso visible:** la historia avanza también cuando pierdes, así que siempre hay sensación de avance.
    - **Personalización:** los errores recurrentes del jugador se vuelven los rivales y retos de su historia.
    - **Transferencia a la partida real:** practica justo lo que le cuesta y lo aplica en sus partidas en línea.
    - **Memoria emocional:** la historia es única para cada jugador y le da orgullo seguirla.

    ────────────────────────────────────────────────────────
    **3. Formulación de la propuesta de valor**

    **Declaración corta (fórmula de Geoff Moore)**

    > Para **jugadores de ajedrez online que, al perder, se frustran y solo saben abandonar la sesión**, Zaqora es un **videojuego de ajedrez narrativo** que **convierte cada derrota en un capítulo de su propia historia y en una lección que los hace volver con más ganas**. A diferencia de las plataformas de juego y las apps de entrenamiento, **que te muestran el error y te dejan solo con el enojo**, nosotros **construimos una historia alrededor de tus partidas, para que perder se sienta como avanzar**.

    **Elevator pitch**

    > ¿Sabes esa sensación de perder tres partidas seguidas y cerrar todo con coraje? Zaqora es un videojuego que toma tus derrotas y las convierte en la historia de tu personaje: cada error se vuelve un reto que te enseña justo lo que te faltó. Juegas, aprendes y, sobre todo, ya no te vas enojado.

    **Titulares para la página de venta**

    | Elemento | Texto |
    | :--- | :--- |
    | **H1** | Perder también es parte de tu historia. |
    | **H2** | Zaqora es el videojuego de ajedrez que convierte tus derrotas en capítulos, retos y lecciones hechos a tu medida, para que dejes de abandonar y empieces a mejorar. |
    | **Beneficio 1** | *Pierdes, pero no te vas:* cada derrota abre una misión de redención en lugar de una pantalla vacía. |
    | **Beneficio 2** | *Aprendes de tus propios errores:* la historia se construye con las jugadas que más te cuestan. |
    | **Beneficio 3** | *Una aventura solo tuya:* por 300 MXN, pago único, sin suscripciones. |

    ────────────────────────────────────────────────────────
    **4. Prueba de ácido**

    | Criterio | Veredicto | Análisis |
    | :--- | :--- | :--- |
    | **¿Es clara?** | ✅ Sí | «Perder también es parte de tu historia» se entiende en menos de 5 segundos y conecta directo con el dolor. *Riesgo:* sin el H2, alguien podría no saber que se trata de ajedrez — conviene poner un tablero o una pieza visible junto al titular. |
    | **¿Es específica?** | ✅ Sí | Evita clichés y nombra un momento concreto (perder y cerrar la sesión), un mecanismo concreto (la derrota abre un capítulo o misión) y un precio concreto. *Falta* un dato que la respalde, como «X % de jugadores sigue jugando después de una derrota»: vale la pena medirlo en pruebas con usuarios. |
    | **¿Es diferenciada?** | ✅ Sí | Las plataformas de juego compiten en análisis técnico y los cursos en contenido; nadie ataca la frustración con narrativa personalizada. *La debilidad es el precio:* la alternativa principal es gratuita, así que hay que justificar los 300 MXN con una demo o un primer capítulo sin costo que haga sentir el valor antes de pagar. |

#### Comparación de los dos prompts

| | **Prompt del profesor** (bloques anteriores) | **Prompt propio** |
| :--- | :--- | :--- |
| **Marco metodológico** | IDEO (*Insightful / Unique / Targeted*) + Pirámide de Valor de Bain. | *Value Proposition Canvas* de Osterwalder + fórmula de Geoff Moore. |
| **Punto de partida** | Insumos ya sintetizados en los pasos previos: perfil, dolor ⭐, competidor más peligroso, precio. | El cliente desde cero: trabajos, dolores y ganancias antes de redactar una sola línea. |
| **Restricciones de forma** | Máximo 25 palabras, lista explícita de palabras prohibidas (*plataforma, solución integral, innovador, ecosistema*…). | Ninguna restricción de extensión ni de vocabulario. |
| **Entregable** | Tres versiones de una frase (funcional, emocional, la más fuerte) + diferencia entre oferta y propuesta de valor. | Canvas completo + declaración larga + *elevator pitch* + H1/H2/beneficios + prueba de ácido. |
| **Validación incluida** | Evaluación IDEO y nivel en la pirámide de Bain. | Prueba de ácido de tres preguntas: claridad, especificidad y diferenciación. |

**Qué aportó cada uno**

- **El del profesor produce una frase; el mío produce el material de la página.** Las restricciones de extensión y la lista de palabras prohibidas obligan a destilar hasta una oración memorizable. Mi prompt, sin ese límite, entrega una declaración de Geoff Moore de casi sesenta palabras: completa y precisa, pero imposible de repetir de memoria. A cambio, deja listos el titular, el subtitular, los tres beneficios y el *pitch* hablado.
- **Mi prompt muestra de dónde sale la propuesta.** Al exigir el Canvas antes de redactar, queda visible la cadena dolor → aliviador → frase. El prompt del profesor parte de un diagnóstico ya hecho en los pasos anteriores, así que su propuesta es más afilada pero menos auditable: no se ve el razonamiento, solo el resultado.
- **La prueba de ácido encontró una debilidad que el otro marco no toca:** la alternativa principal del usuario es gratuita, y ninguna de las dos propuestas lo resuelve. De ahí sale una decisión concreta de producto — primer capítulo o demo sin costo antes de pedir los 300 MXN — que no aparecía en ninguna parte del análisis previo.
- **Discrepancia detectada entre pasos.** Mi prompt entregó el precio como «300 MXN» sin especificar periodicidad, y la respuesta lo interpretó como **pago único sin suscripción**. En el Paso 2, en cambio, los mismos 300 MXN se dimensionaron como **suscripción mensual** (3,600 MXN anuales). Es la misma cifra leída de dos formas que difieren por un factor de doce en ingreso por usuario, y por lo tanto en todo el TAM. Definir el modelo de ingresos —pago único o suscripción— es un pendiente que ninguno de los dos prompts resolvió, porque ninguno lo preguntó.
- **Coinciden en el núcleo, otra vez.** Ambos marcos, con métodos y salidas distintas, llegan a la misma idea: la derrota deja de cerrar la sesión y pasa a abrir un capítulo. Que dos caminos independientes aterricen en la misma frase es la mejor señal de que el posicionamiento no depende de cómo se formuló la pregunta.

---

## 4) Entregable — Canvas de Mercado

**Equipo:** _David López Ramírez_ · **Concepto:** _Zaqora_

| Sección del Canvas | Componente | Descripción y Hallazgos |
| :--- | :--- | :--- |
| **1. SEGMENTO ACCIONABLE** | **Demográfica** | Jugadores de ajedrez en línea de nivel amateur (intermedios y avanzados en desarrollo), mayoritariamente adultos jóvenes en México, que juegan varias veces por semana en plataformas gratuitas. |
| | **Conductual** | Tras perder dos o tres partidas seguidas no regulan la emoción dentro de la plataforma: su único *workaround* es abandonar la sesión por completo —cerrar la app o alejarse 20 minutos—. Algunos aplican una regla autoimpuesta de «2 derrotas = cerrar». |
| | **Psicográfica** | *«No intenté analizar las partidas en ese momento porque sabía que iba a buscar excusas.»* Sienten frustración intensa ante la derrota y ante la soberbia de jugadores más experimentados; quedan atrapados en la espiral de revancha y reconocen que deberían parar, pero siguen jugando y empeoran su rendimiento y su humor. |
| | **Económica** | Costo medido en tiempo perdido, caídas de rating en las malas rachas y frustración acumulada. Disposición a pagar estimada en 300 MXN por comparación con alternativas de *coaching* (clases particulares en México: 200-220 MXN/hora). **Quién decide:** el propio usuario paga; no hay comprador institucional. |
| | **Hipótesis críticas sin verificar** | **1. Modelo de ingresos sin definir:** los 300 MXN se han tratado como *suscripción mensual* en el dimensionamiento y como *pago único* en la estrategia de precio y la propuesta de valor — una diferencia de 12× en ingreso por usuario que arrastra todo el TAM.<br>**2. Preferencia frente al hábito gratuito:** que el usuario elija una experiencia narrativa en vez de la inercia de cerrar la app.<br>**3. Captura en el momento del *tilt*:** que sea viable intervenir antes de que cierre la sesión; si debe abrir una app aparte, el argumento se debilita.<br>**4. Disposición a pagar real:** los 300 MXN son una estimación por comparación, no una cifra medida con usuarios. |
| **2. TAMAÑO DE MERCADO** | **TAM** | **82,440 personas** con el problema y disposición de pago en México · **296.8 millones de MXN anuales** (82,440 × 3,600 MXN).<br>*Fuente:* INEGI ENDUTIH 2024 (100.2 millones de usuarios de internet) y The CIU 2024 (68.7 millones de jugadores; 42.1% con afinidad por estrategia).<br>*Advertencia:* los tres últimos filtros del embudo —2% juega ajedrez en línea, 60% se frustra al perder, 10% convierte— son supuestos propios sin fuente y determinan la mayor parte del resultado. |
| | **SAM** | **65,952 personas** · **237.4 millones de MXN anuales**.<br>*Filtros:* geografía (solo México) e idioma español; dispositivo compatible —smartphone o navegador—, que recorta al 80%. |
| | **SOM (año 1-2)** | **1,200 clientes pagadores** (1.82% del SAM) · **4.32 millones de MXN anuales** teóricos, antes de *churn* y descuentos.<br>*Lógica:* 2 personas dedicadas a ventas y alianzas; 40 aliados (clubes y *streamers*) activados en 24 meses, con 30 clientes cada uno; piloto en CDMX, Edomex, Nuevo León, Jalisco y Puebla.<br>*Señal de viabilidad:* marginal — el ingreso efectivo rondaría 2.4-3.24 millones de MXN, suficiente solo para una operación muy austera. |
| **3. MAPA COMPETITIVO** | **Directos (3)** | • **Chess Story:** narrativa preescrita y genérica; no se adapta al estado emocional ni usa los datos reales de las derrotas.<br>• **AI Dungeon + Chess:** exige configuración manual del usuario; sin integración nativa ajedrez-emoción-narrativa, y alguien en *tilt* no tiene energía para construir su propia herramienta.<br>• **Story Time Chess:** diseñado para niños de 4+ años; el adulto que juega en línea lo percibe como infantil. |
| | **Indirectos (3)** | • **Chess.com Game Review + Lessons:** análisis técnico y frío que intensifica la autocrítica justo cuando el usuario necesita lo contrario.<br>• **Chess Coach Pro / Chessy:** centrados en tácticas y aperturas; ignoran la regulación emocional del *tilt*.<br>• **MyMentalCoach / Chess Psychology Training:** exigen iniciativa y presupuesto por sesión; llegan tarde al momento crítico. |
| | **Sustitutos (2)** | • **Regla de «2 derrotas = cerrar la app»:** sesión abortada sin aprendizaje ni cierre emocional, y frustración trasladada a otras actividades.<br>• **Análisis manual tras enfriarse:** 20 a 60 minutos adicionales de carga cognitiva y autoevaluación dolorosa sin guía. |
| | **El más peligroso** | La **regla de «2 derrotas = cerrar la app»**. No es un producto, es un hábito: cero fricción, gratuito, inmediato en el instante exacto del dolor y validado dentro de la comunidad. Zaqora no compite contra el análisis de Chess.com, compite contra el botón de cerrar la ventana. |
| **4. LIENZO BLUE OCEAN** | **Atributos (7)** | Profundidad técnica del análisis · Ranking competitivo interno · Facilidad de *onboarding* · Validación emocional inmediata post-derrota · Transformación narrativa personalizada mediante LLM · Integración nativa con la sesión de juego · Relación precio/valor. |
| | **Tabla de puntuación** | Zaqora lidera en validación emocional inmediata (5) y transformación narrativa personalizada (5), y puntúa **cero en ranking competitivo interno** — una decisión, no una carencia: el segmento ya tiene un rating, y ese número es precisamente la fuente de su frustración. *(Tabla completa debajo.)* |
| | **El hueco azul** | Zaqora crea un espacio donde la derrota específica del usuario, en el momento exacto en que ocurre y sin salir de su sesión, se transforma en parte de una historia personal construida con sus propios datos. |
| | **Advertencia de océano rojo** | En facilidad de *onboarding* Zaqora empata con Chess Story y queda por debajo del hábito de cerrar la app; en integración nativa con la sesión pierde 3 contra 5. Competir por fricción de instalación sería pelear en el terreno donde el hábito gratuito ya ganó. |
| **5. PROPUESTA DE VALOR** | **Oferta (descripción técnica)** | Una aplicación con inteligencia artificial que genera una historia narrativa personalizada a partir de tus partidas de ajedrez, usando tu historial real de derrotas y victorias. |
| | **Propuesta de valor** (23 palabras) | *«Cuando pierdes en Lichess y estás por cerrar la app, Zaqora valida tu frustración y la convierte en el próximo capítulo de tu historia.»* |
| | **Nivel en pirámide de Bain** | **Emocional.** El atributo que domina el lienzo —validación emocional inmediata— no es una función, es un alivio afectivo en el momento de la derrota. El motor narrativo podría empujar hacia lo transformador, pero prometerlo hoy, sin evidencia de retención, sería exagerar. |
| | **Error de la 1ª versión** | **Describir el producto en lugar del valor.** Se enfocaba en las funcionalidades técnicas y analíticas en vez de situar al usuario en el instante exacto del dolor frente a su alternativa actual. La corrección fue cambiar el sujeto de la frase: del producto a la persona. |

**Tabla de puntuación del lienzo** (1 = muy bajo · 5 = muy alto):

| Atributo | Chess.com Lessons | Chess Story | Regla «2 derrotas» | **Zaqora** |
| :--- | :---: | :---: | :---: | :---: |
| Profundidad técnica del análisis | 5 | 1 | 1 | **2** |
| Ranking competitivo interno | 4 | 1 | 1 | **0** |
| Facilidad de *onboarding* | 3 | 4 | 5 | **4** |
| Validación emocional inmediata | 1 | 1 | 2 | **5** |
| Transformación narrativa personalizada (LLM) | 0 | 2 | 0 | **5** |
| Integración nativa con la sesión | 1 | 0 | 5 | **3** |
| Relación precio/valor | 3 | 4 | 5 | **3** |
---

## 5) Reflexión

- **Los números de mercado se ven más sólidos de lo que son.** El TAM/SAM/SOM salió de encadenar supuestos de conversión sobre datos de INEGI y The CIU. La cifra final (82,440 personas) es defendible solo si el supuesto va escrito al lado; sin él, es una cifra prestada. Aprendí a no presentar un número sin su cadena de derivación.
- **El competidor más peligroso no era un producto.** Todo el mapa competitivo apuntaba a apps, y el análisis terminó señalando un hábito gratuito: cerrar la sesión después de dos derrotas. Competir contra una costumbre exige un producto que llegue en el momento exacto, no uno con más funciones.
- **El lienzo estratégico sirve sobre todo para decidir qué no hacer.** El movimiento más importante del Blue Ocean no fue subir un atributo, sino poner cero deliberado en ranking interno: añadir otro número comparativo habría reproducido justo la presión que el producto quiere aliviar.
- **Segmentar por conducta resultó más útil que segmentar por demografía.** Edad, ingreso y ubicación no predicen nada aquí; el momento en que alguien cierra la sesión tras perder sí define a quién le sirve el producto y cuándo hay que llegarle.
