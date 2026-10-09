# Semana 7 — Viabilidad técnica y económica

## 1) Resumen

- **Nombre de la actividad:** _Benchmarking de modelos de ingresos y modelo económico del producto_
- **Curso:** _Proyecto de Ingeniería IV_
- **Equipo:** _David López Ramírez_
- **Fecha:** _08/10/2026_
- **Descripción breve:** _Con el concepto de diseño elegido en la semana 6 (**Ghost Engine**), esta semana se empezó a responder si el negocio de **Zaqora** «cierra»: si los ingresos pueden cubrir los costos de forma sostenible. El primer paso fue un benchmarking de modelos de ingresos con Perplexity para entender cómo cobran productos parecidos, dónde abandona el usuario el proceso de pago y quién más podría pagar. El segundo, el modelo económico con Claude: costo unitario, precio, punto de equilibrio, flujo de caja y VPN. En cada paso se usaron dos prompts de autoría distinta: el del profesor y uno propio._

---

## 2) Punto de partida

**Concepto elegido (semana 6):** **Ghost Engine**, una PWA web en formato de novela visual: tras perder en Lichess, el villano que encarna el error del jugador le escribe y lo invita a un capítulo construido sobre esa misma partida.

**Propuesta de valor (semana 4):** _«Cuando pierdes en Lichess y estás por cerrar la app, Zaqora valida tu frustración y la convierte en el próximo capítulo de tu historia.»_

**Lo que ya sabíamos del dinero:**

- **Precio de referencia (semana 4):** \$300 MXN, tratado unas veces como suscripción mensual y otras como pago único. El modelo de ingresos seguía sin definirse.
- **Costo por usuario (semana 5):** ≈ \$5–10 MXN al mes con 15–20 usuarios beta, con un tope de \$30 MXN en el PDS. El precio mínimo viable salió en ≈ \$17–33 MXN al mes, y la arquitectura recomendó probar \$49–79 MXN en el piloto.
- **Riesgo de fondo:** el usuario usa Lichess precisamente porque es gratis, y su disposición a pagar no está verificada.

**Pertinencia, factibilidad y viabilidad:** las semanas 2 a 4 respondieron si vale la pena hacerlo; las semanas 5 y 6, cómo se puede hacer. Esta semana responde si es sostenible económicamente.

- **Objetivo de la semana:** Elegir un modelo de ingresos con evidencia de cómo cobran productos similares, como base para el modelo económico (costo unitario, precio, punto de equilibrio, flujo de caja y VPN).

!!! note "Adaptación a un producto de software"
    El modelo del curso es hardware (venta única o subsidiada) más suscripción. Zaqora no tiene hardware, así que, como en la semana 5, el BOM se traduce a costo por usuario activo (IA + infraestructura) y la «unidad» es el usuario beta.

---

## 3) Proceso — Modelo de ingresos y modelo económico con IA

### Paso 1 — Benchmarking de modelos de ingresos

**Herramienta:** Perplexity.

??? quote "Prompt completo — Prompt del profesor (Perplexity, benchmarking de modelos de ingresos)"
    Actúa como analista de inteligencia competitiva especializado en modelos de negocio para productos de software en mercados latinoamericanos y globales. Tu metodología consiste en identificar cómo empresas con ofertas similares están capturando valor — no solo su precio de lista, sino el modelo completo: quién paga, cuándo, bajo qué condición, y qué fricción existe en ese proceso de pago.

    Somos emprendedores en México con el siguiente producto:
    Zaqora: una PWA web que convierte el aprendizaje de ajedrez en un videojuego de un solo jugador, donde cada «capítulo» es una lección disfrazada de misión y el villano encarna un patrón de error real y recurrente del jugador, detectado en sus partidas de Lichess. No hay ranking, rival humano ni partida en línea: solo el jugador contra el mapa de la campaña, a su propio ritmo. El coaching ocurre dentro de la ficción, nunca como corrección fría ni comparación social.
    Propuesta de valor: Cuando pierdes en Lichess y estás por cerrar la app, Zaqora valida tu frustración y la convierte en el próximo capítulo de tu historia.
    Segmento objetivo: jugador amateur de ajedrez online (Lichess) que, al perder o frustrarse, no tiene forma de regular esa frustración dentro del juego y solo sabe abandonar la sesión («apagar Lichess», «alejarme 20 minutos»). Usa Lichess precisamente porque es gratis, y su disposición de pago aún no está verificada.

    Investiga 3 empresas o productos con oferta similar a la nuestra — pueden ser competidores directos, indirectos, o productos que resuelven el mismo tipo de problema en otro sector o mercado.

    Para cada empresa entrega:

    - EMPRESA: [nombre]
    - Qué ofrece: [descripción en 1 oración]
    - Modelo de ingresos: [cómo cobra — quién paga, cuándo, bajo qué condición]
    - Rango de precio: [precios documentados o estimados con fuente]
    - Momentos de fricción: [dónde el usuario típicamente duda o abandona el proceso de pago — prueba gratuita que no convierte, precio oculto hasta el final, contrato anual que genera resistencia]
    - Otros stakeholders: [¿hay alguien más que paga o podría pagar además del usuario final? distribuidores, instituciones, gobiernos, seguros, marcas que patrocinan]

    Al terminar las 3 empresas, responde:
    ¿Qué modelo de ingresos predomina en este espacio y por qué crees que es el elegido por la mayoría?
    ¿Hay algún stakeholder que nadie está cobrando actualmente y que podría ser una oportunidad de ingresos para un nuevo entrante?

??? abstract "Respuesta completa — Prompt del profesor (Perplexity)"
    Con base en la investigación realizada, aquí está el análisis competitivo solicitado:

    ---

    **EMPRESA 1: ChessMood**

    - **Qué ofrece:** Plataforma de cursos de ajedrez en video creados por Grandes Maestros, con más de 500 horas de contenido estructurado (aperturas, medio juego, finales, psicología) y eventos en vivo semanales. [1] [2] [3]
    - **Modelo de ingresos:** Suscripción recurrente con dos *tiers* (Essential y Pro). El usuario paga mensualmente o anualmente para mantener acceso a la biblioteca de cursos. [2] [4] [1]
    - **Rango de precio:** Essential: \$79/mes (facturado anualmente, \$948/año) o \$99/mes (facturación mensual). Pro: \$99/mes (anual, \$1,188/año) o \$129/mes (mensual). Plan gratuito básico disponible con acceso limitado. [3] [5] [6] [2]
    - **Momentos de fricción:**
        - *Precio elevado percibido:* casi \$1,200/año para el *tier* Pro es una barrera significativa para jugadores amateur que vienen de Lichess gratuito. [2]
        - *Decisión anual vs. mensual:* aunque el plan anual ofrece descuento (~20 %), requiere compromiso de largo plazo que genera resistencia en usuarios no comprometidos. [2]
        - *Prueba de 30 días con reembolso:* aunque existe garantía de devolución, el usuario debe pagar por adelantado y luego solicitar reembolso, lo que añade fricción cognitiva. [2]
    - **Otros stakeholders:** No hay evidencia de modelos B2B (escuelas, corporativos) en ChessMood. Solo B2C directo. [4] Potencial no explotado: academias de ajedrez o clubes podrían licenciar acceso grupal, pero no está documentado como oferta activa.

    **EMPRESA 2: Chessable**

    - **Qué ofrece:** Plataforma de estudio de ajedrez basada en repetición espaciada (MoveTrainer), con cursos individuales de aperturas, tácticas y finales creados por GMs y entrenadores. [7] [8] [9]
    - **Modelo de ingresos:** Híbrido: (1) venta de cursos individuales de por vida (modelo de tienda) + (2) suscripción PRO anual que actúa como «tarjeta de descuento» (20–30 % *off* en cursos) y desbloquea funciones adicionales. [8] [9] [10] [11]
    - **Rango de precio:** Cursos individuales: \$20–\$100+ cada uno (pago único, acceso perpetuo). PRO *membership*: \$11.99/mes o \$74.99/año (≈ \$6.25/mes efectivo). [9] [11] [12] [7] [8]
    - **Momentos de fricción:**
        - *El modelo de tienda genera «fatiga de decisión»:* el usuario debe evaluar curso por curso, lo que puede retrasar o abortar la compra. [9]
        - *PRO solo vale la pena si gastas ~\$250/año en cursos:* para jugadores casuales, el ROI no es claro, lo que reduce conversión a suscripción. [9]
        - *Cursos gratuitos limitados:* aunque hay decenas de cursos gratis, el contenido premium está fragmentado, obligando al usuario a navegar un *marketplace* en lugar de una biblioteca unificada. [10] [13]
    - **Otros stakeholders:** Entrenadores/*coaches*: compran cursos para asignar a sus alumnos (B2B2C indirecto). [10] Escuelas: no hay programa documentado de licenciamiento institucional, pero el modelo de cursos individuales podría adaptarse para venta grupal. [10]

    **EMPRESA 3: Duolingo (referente de gamificación en aprendizaje)**

    - **Qué ofrece:** Aplicación de aprendizaje de idiomas gamificada, con lecciones cortas, rachas diarias, vidas limitadas y progresión por niveles. [14] [15] [16]
    - **Modelo de ingresos:** *Freemium* con dos *streams*: (1) suscripción «Super Duolingo» que elimina anuncios y fricciones (vidas ilimitadas, progreso offline) + (2) publicidad para usuarios gratuitos. [16] [17] [18] [14]
    - **Rango de precio:** Super Duolingo: \$6.99/mes (≈ \$84/año). Duolingo for Business: \$75.09/año por usuario (licenciamiento corporativo). [18] [19] [14] [16]
    - **Momentos de fricción:**
        - *«Pagar para quitar fricción» vs. misión educativa:* históricamente, Duolingo tuvo resistencia interna a monetizar porque cobrar por aprender más rápido iba en contra de su misión. [14]
        - *Conversión baja:* solo una minoría de usuarios gratuitos convierte a Super, a pesar de la base masiva (38M+ usuarios). [17] [16]
        - *Anual vs. mensual:* 70 % de ingresos vienen de planes anuales, lo que sugiere que los usuarios prefieren compromiso de largo plazo una vez convencidos, pero la barrera inicial es alta. [20]
    - **Otros stakeholders:** Empresas (B2B): Duolingo for Business licencia a corporativos para capacitación de empleados (\$75/año por usuario). [19] [21] [18] Escuelas/universidades: licenciamiento institucional con precios académicos (\$50–\$100/estudiante/año para paquetes completos). [22] [18] Gobiernos/ONGs: potencial para programas de alfabetización o integración de migrantes, aunque no documentado como *stream* mayoritario. [22]

    ---

    **Síntesis: modelo predominante y oportunidad no explotada**

    **¿Qué modelo de ingresos predomina y por qué?**

    El modelo *freemium* con suscripción recurrente es el predominante en este espacio (ChessMood, Chessable PRO, Duolingo, Magnus Trainer, Noctie.ai). [23] [24] [25] [1] [4]

    Razones de su predominio:

    1. **Alineación con el valor continuo:** El aprendizaje de ajedrez (como idiomas o fitness) es un proceso continuo. La suscripción refleja que el valor se entrega de forma recurrente (nuevos cursos, análisis de partidas, actualizaciones). [26] [27] [4]
    2. **Barrera de entrada baja:** El *tier* gratuito permite capturar usuarios que vienen de Lichess sin fricción inicial. La conversión ocurre cuando el usuario ya está comprometido emocionalmente (tras frustración, racha, o progreso visible). [15] [28] [23]
    3. **LTV (*Lifetime Value*) predecible:** Las suscripciones generan ingresos recurrentes que facilitan la planificación y la reinversión en contenido. Chess.com reporta ~88 % de ingresos por suscripciones. [29] [17]
    4. **Gamificación + fricción pagable:** Modelos como Duolingo muestran que se puede monetizar quitando fricciones (vidas ilimitadas, sin anuncios) sin cobrar por el contenido en sí, lo que preserva la misión educativa mientras se genera *revenue*. [30] [15] [14]

    **¿Hay algún stakeholder que nadie está cobrando actualmente?**

    Sí: escuelas, clubes de ajedrez y programas educativos (B2B institucional).

    Evidencia de oportunidad:

    - Chess.com ya explota esto con ChessKid.com como vehículo B2B para escuelas y academias, pero es un producto separado (enfocado en niños, interfaz segura para clases). [31] [29]
    - Duolingo genera ingresos significativos con Duolingo for Schools y Duolingo for Business, con LTV 10–20x mayor que consumidores individuales y contratos de 12–36 meses. [32] [18] [19] [22]
    - El mercado de licenciamiento B2B en apps educativas creció 37 % en 2025, con firmas educativas comprando licencias empresariales para integración en currículos. [33]

    Para Zaqora, esto representa una oportunidad porque:

    1. Tu producto resuelve regulación emocional post-derrota, lo cual es relevante no solo para jugadores individuales sino para entrenadores que gestionan grupos de alumnos frustrados. Un *coach* podría licenciar Zaqora para asignar «misiones de regulación» tras torneos o sesiones de práctica.
    2. Clubes y academias de ajedrez en Latinoamérica podrían integrar Zaqora como herramienta de retención: cuando un alumno pierde en Lichess, en lugar de abandonar, se le asigna un capítulo de Zaqora como «tarea de recuperación emocional».
    3. Modelo de licenciamiento institucional: vender acceso grupal a academias (ej. \$5–10/alumno/mes en volumen) con *dashboard* para entrenadores (ver progreso de alumnos en misiones, patrones de error recurrentes del grupo). Esto sería análogo a Duolingo for Schools pero enfocado en regulación emocional + aprendizaje contextual.
    4. Ningún competidor directo (ChessMood, Chessable, Noctie) tiene oferta B2B documentada para escuelas o clubes. ChessKid existe pero es para niños y no aborda la frustración post-derrota. [29] [31]

    **Implicaciones para Zaqora**

    Dado que tu segmento objetivo son jugadores amateur de Lichess que no tienen disposición de pago verificada y usan la plataforma precisamente porque es gratis, el modelo *freemium* es casi obligatorio para capturar usuarios. Sin embargo, la conversión a pago será baja si solo cobras al usuario final.

    Recomendación estratégica:

    1. **Freemium B2C:** Capítulos básicos gratuitos (3–5 misiones) para validar que el usuario completa el ciclo frustración → misión → regulación. Cobrar por biblioteca completa de misiones o por análisis avanzado de patrones de error.
    2. **B2B institucional como *stream* principal:** Licenciar a academias, clubes y entrenadores en México/Latam como herramienta de retención de alumnos. El entrenador paga, el alumno usa gratis (o con funciones limitadas). Esto alinea incentivos: el *coach* quiere que el alumno no abandone tras perder; Zaqora es la solución.
    3. **Precio B2B sugerido:** \$5–10/alumno/mes en volumen (50+ alumnos), con *dashboard* básico incluido. Esto es 40–60 % más barato que ChessMood pero con propuesta de valor distinta (regulación emocional, no solo contenido).

    ---

    *Fuentes (selección de las 58 citadas):* [1] chessentials.com · [2] chessmood.com/pricing · [7]–[13] chesspivot.com, chessily.com, chesscore.io, circlechess.com, raindropchess.com · [14] techcrunch.com (Duolingo EC-1) · [18] untaylored.com · [19] duolingo.com/business · [20] purchasely.com · [29] chess-com-application.daykhin.com · [31] pythonblogs.com · [33] marketreportsworld.com.

[Descargar la respuesta completa con todas las fuentes (PDF)](recursos/archivos/PI4_S7/Benchmarking_Prompt_Profesor.pdf)

#### Segunda ronda — prompt de autoría propia

Para la segunda ronda escribí un prompt que obligara a presentar las tres empresas en una sola tabla comparativa y a pensar «fuera de la caja» quién más se beneficia indirectamente del valor de Zaqora.

??? quote "Prompt completo — Segunda ronda, prompt propio (Perplexity, benchmarking de modelos de ingresos)"
    Actúa como un analista de negocios y estratega de producto experto. Quiero que realices un ejercicio de "Benchmarking de modelos de ingresos" para mi producto.

    Mi producto/servicio es: Zaqora, una PWA web que convierte el aprendizaje de ajedrez en un videojuego de un solo jugador: cada «capítulo» es una lección disfrazada de misión y el villano encarna un patrón de error real y recurrente del jugador, detectado en sus partidas de Lichess. No hay ranking, rival humano ni partida en línea, y el coaching ocurre dentro de la ficción, nunca como corrección fría ni comparación social. Propuesta de valor: «Cuando pierdes en Lichess y estás por cerrar la app, Zaqora valida tu frustración y la convierte en el próximo capítulo de tu historia.» Nuestro usuario es un jugador amateur de ajedrez online en México que, al perder o frustrarse, solo sabe abandonar la sesión; usa Lichess precisamente porque es gratis y su disposición de pago aún no está verificada.

    **Objetivo:** Investigar cómo otras empresas con ofertas similares están cobrando. El objetivo no es copiar, sino entender el espacio de posibilidades real y los momentos de fricción que ya existen en el mercado.

    **Instrucciones:**

    1. Selecciona 3 empresas del mundo real que ofrezcan productos o servicios similares al mío. Pueden ser competidores directos o productos análogos que resuelvan el mismo tipo de problema en otro sector o mercado.
    2. Para cada empresa, analiza y define:
        - Qué producto o servicio venden exactamente.
        - Su modelo de ingresos (quién paga, cuándo, bajo qué condición).
        - Su rango de precio visible en el mercado.
        - Notas sobre fricción (¿cuáles son los posibles momentos de fricción que experimenta el usuario en su proceso de pago?).
        - Otros stakeholders (¿qué otros actores podrían aportar ingresos a su modelo y actualmente están ignorando?).
    3. Presenta los hallazgos estrictamente usando la siguiente tabla en formato Markdown, con las columnas: Producto o servicio similar ([Empresa] - [Breve descripción]) | Modelo de ingresos (quién paga, cuándo) | Rango de precio | Notas (Fricción en el pago y otros stakeholders).
    4. Después de generar la tabla, responde de forma analítica, estratégica y profunda a estas dos preguntas:
        - ¿Qué modelo están usando mayoritariamente los competidores analizados y por qué crees que eligieron ese?
        - ¿Hay algún stakeholder (actor) al que los competidores no le están cobrando y que podría ser una fuente de ingresos innovadora para mi negocio? (Piensa fuera de la caja: ¿quién más se beneficia indirectamente del valor que aporta mi producto?).

??? abstract "Respuesta completa — Segunda ronda, prompt propio (Perplexity)"
    | Producto o servicio similar | Modelo de ingresos (quién paga, cuándo) | Rango de precio | Notas (Fricción en el pago y otros stakeholders) |
    | :--- | :--- | :--- | :--- |
    | **Chess.com** — Plataforma de juego, análisis y aprendizaje de ajedrez online | Suscripción escalonada B2C: el jugador paga mensual o anualmente por desbloquear lecciones, puzzles, análisis de partidas, estadísticas y funciones avanzadas. Existe un nivel gratuito con límites; los planes Premium amplían el acceso y Diamond incorpora explicaciones de entrenador y análisis más profundos. [1] [2] [3] | Aproximadamente US\$5.46–US\$13.65 al mes y US\$38.23–US\$92.84 al año en México, según el nivel y el ciclo de cobro. [4] | **Fricción:** el usuario gratuito debe entender qué límite le afecta y si el beneficio justifica una suscripción recurrente; los distintos niveles pueden generar confusión; el valor percibido depende de usar la plataforma con frecuencia. El pago puede sentirse como una barrera especialmente para usuarios acostumbrados a Lichess gratuito. **Stakeholders no monetizados directamente:** entrenadores independientes, clubes, escuelas y padres podrían pagar por paneles, seguimiento y contenido; también podrían existir acuerdos con plataformas de torneos o federaciones. |
    | **Chessable** — Plataforma de cursos de ajedrez con repetición espaciada y entrenamiento de variantes | Modelo híbrido: suscripción PRO B2C para funciones premium, cursos gratuitos y compra individual de cursos avanzados. El usuario paga una membresía mensual o anual y, adicionalmente, puede comprar cursos creados por autores o grandes maestros. [5] [6] [7] | PRO: US\$11.99 al mes o US\$74.99 al año. Los cursos individuales suelen situarse aproximadamente entre US\$20 y US\$100, con descuentos para miembros PRO. [6] [8] | **Fricción:** doble decisión de compra —suscripción más curso—; el usuario puede no saber si PRO incluye el contenido que quiere o solo mejora la experiencia; el precio anual exige confianza anticipada; los cursos de mayor valor suelen depender de un autor concreto. **Stakeholders no monetizados directamente:** autores y entrenadores podrían recibir herramientas de venta, analítica o financiación; clubes, academias y padres podrían adquirir licencias; plataformas como Lichess podrían participar mediante integración o afiliación, aunque eso requeriría acuerdos y una clara separación de intereses. |
    | **Habitica** — Aplicación de hábitos y productividad convertida en un juego de rol | Suscripción B2C opcional: el producto básico es gratuito y el usuario paga por beneficios premium, elementos cosméticos, gemas y ventajas de personalización. También ofrece planes grupales, donde un responsable paga una cuota mensual más un importe por miembro adicional. [9] [10] [11] | US\$4.99 al mes; US\$14.99 trimestrales; US\$29.99 semestrales; US\$47.99 anuales. El plan grupal parte de US\$9 al mes más US\$3 por miembro adicional. Los precios pueden variar por ubicación. [9] [10] | **Fricción:** el usuario puede percibir que está pagando por personalización más que por un resultado funcional; una suscripción opcional necesita recordatorios constantes de valor; el modelo grupal exige invitar y coordinar a otros usuarios. **Stakeholders no monetizados directamente:** empresas que quieren mejorar hábitos de empleados, *coaches*, terapeutas, profesores y comunidades podrían pagar por espacios privados, seguimiento agregado o programas patrocinados. |

    ---

    **Modelo predominante**

    El patrón dominante es el *freemium* con suscripción recurrente. Chess.com y Chessable convierten el acceso gratuito en un embudo hacia funciones avanzadas, contenido ilimitado o personalización; Habitica aplica la misma lógica, aunque hace más opcional la relación entre pago y progreso. La evidencia más clara en ajedrez es que las funciones que se cobran son análisis, explicación, profundidad, continuidad y comodidad, mientras que el acceso básico conserva suficiente utilidad para atraer usuarios. Chess.com, por ejemplo, mantiene funciones gratuitas de revisión, pero reserva el uso ilimitado y análisis avanzado para niveles Premium. [12]

    Las empresas probablemente eligen este modelo por cuatro razones:

    1. **Reduce la barrera de entrada.** Un jugador puede probar el producto sin comprometer dinero, algo importante para un público acostumbrado a Lichess, cuyo servicio principal es gratuito y se financia mediante donaciones. [13] [14]
    2. **Conecta el ingreso con el hábito.** La suscripción funciona cuando el usuario vuelve con frecuencia para estudiar, revisar partidas o mantener una racha.
    3. **Permite segmentar disposición de pago.** Un usuario ocasional permanece gratis; uno intensivo paga por límites más altos; uno avanzado paga por análisis, contenido o explicaciones.
    4. **Mejora la previsibilidad financiera.** El cobro mensual o anual es más estable que depender exclusivamente de compras individuales o donaciones.

    Para Zaqora, copiar una suscripción completa desde el día uno sería arriesgado. La propuesta no es simplemente «más análisis de ajedrez»: interviene en un momento emocional específico —la derrota inmediatamente después de jugar— y debe demostrar primero que consigue que el usuario no abandone la sesión. Por ello, el valor inicial podría ser más fácil de probar con un modelo híbrido: capítulos iniciales gratuitos, una temporada narrativa o paquete de misiones de pago, y una suscripción solo cuando Zaqora haya identificado suficientes patrones recurrentes para generar contenido personalizado de forma continua.

    La fricción crítica no será únicamente el precio. Será el momento del cobro. Si Zaqora muestra una pantalla de pago justo después de que el usuario pierda, puede parecer que monetiza su frustración. En cambio, podría presentar el siguiente capítulo gratuito como una respuesta inmediata y reservar el pago para una promesa futura clara: más patrones detectados, temporadas completas, análisis histórico o personalización narrativa.

    **Stakeholders alternativos**

    El stakeholder más interesante que los competidores de ajedrez suelen dejar fuera es **Lichess como canal de adquisición e integración**, no necesariamente como cliente directo. Zaqora se beneficia de las partidas jugadas en Lichess y convierte esa frustración en una experiencia de aprendizaje posterior. Si consigue aumentar la retención saludable —que el jugador vuelva a aprender en vez de abandonar—, podría aportar valor a Lichess sin competir frontalmente con su misión gratuita.

    Un modelo potencial sería una alianza de integración o afiliación en la que:

    - Lichess recibe una comisión por usuarios que autorizan la conexión y se convierten en clientes de Zaqora.
    - Zaqora financia parte de esa comisión mediante una cuota por activación, un porcentaje de suscripciones o una contribución fija.
    - El usuario mantiene su experiencia gratuita en Lichess y recibe una transición voluntaria hacia Zaqora después de sus partidas.
    - La colaboración se limita a consentimiento explícito, privacidad y exportación autorizada de datos; no debería convertir los datos de partidas en publicidad invasiva.

    No asumiría que Lichess aceptaría este acuerdo: su modelo está basado en donaciones, voluntariado y ausencia de anuncios, por lo que una alianza comercial podría entrar en tensión con sus principios. Sin embargo, precisamente por eso conviene considerar una variante compatible: Zaqora podría hacer una contribución proporcional a Lichess por cada usuario que conecte su cuenta, o permitir que el usuario divida su pago entre Zaqora y una donación a Lichess. [15] [13]

    Otros stakeholders potenciales son:

    - **Academias, clubes y entrenadores:** pagarían por asignar misiones, detectar patrones comunes de sus alumnos y revisar progreso sin necesidad de corregir cada partida manualmente.
    - **Padres de jugadores jóvenes:** podrían pagar por una experiencia que fomente perseverancia y aprendizaje sin rankings, presión social ni exposición pública.
    - **Escuelas y programas extracurriculares:** podrían comprar licencias por grupo o por cohorte para enseñar tolerancia al error y pensamiento estratégico.
    - **Organizadores de torneos y comunidades de ajedrez:** podrían patrocinar temporadas temáticas posteriores a eventos, por ejemplo, una campaña de «aprender de las derrotas del torneo».
    - **Marcas de hardware, cafés, editoriales y plataformas educativas:** podrían financiar capítulos patrocinados, pero solo si la integración es contextual y no interrumpe la ficción.

    La oportunidad más defendible parece ser un modelo **B2C para validar el producto y B2B2C para escalarlo**: comenzar con un jugador amateur que paga poco por una temporada o una suscripción ligera, y posteriormente vender licencias a clubes, entrenadores y academias. Así, Zaqora no depende únicamente de que un usuario acostumbrado a lo gratuito acepte pagar después de perder; también puede capturar el valor que reciben quienes quieren que ese jugador practique, persevere y mejore.

    ---

    *Fuentes (selección de las 30 citadas):* [1]–[3] support.chess.com y chess.com/membership · [4] mobeigi.com (precios regionales de Chess.com) · [5]–[8] apps.apple.com, chesspivot.com, kingdomofchess.com · [9]–[11] apps.apple.com, habitica.com/static/plans, habitica.com/static/terms · [12] support.chess.com (Game Review) · [13]–[15] lichess.org/about, lichess.org/faq, lichess.org/patron.

[Descargar la respuesta completa con todas las fuentes (PDF)](recursos/archivos/PI4_S7/Benchmarking_Prompt_Propio.pdf)

#### Comparación de los dos prompts

| | **Prompt del profesor** | **Prompt propio** |
| :--- | :--- | :--- |
| **Rol asignado** | Analista de inteligencia competitiva en modelos de negocio. | Analista de negocios y estratega de producto. |
| **Formato** | Ficha por empresa con 6 campos; la fricción trae ejemplos (prueba que no convierte, precio oculto, contrato anual). | Una sola tabla de 4 columnas, con fricción y stakeholders en la misma celda. |
| **Empresas elegidas** | ChessMood, Chessable y Duolingo. | Chess.com, Chessable y Habitica. |
| **Precios** | Precios de lista en dólares. | Chess.com con precios regionales para México. |
| **Modelo predominante** | *Freemium* con suscripción recurrente. | *Freemium* con suscripción recurrente. |
| **Stakeholder no explotado** | Escuelas, clubes y academias (B2B institucional). | Lichess como canal de adquisición; después, academias, clubes, entrenadores y padres. |
| **Recomendación** | *Freemium* B2C + **B2B institucional como fuente principal**, a \$5–10 por alumno al mes. | **B2C para validar y B2B2C para escalar**: capítulos gratis, temporada o suscripción ligera, licencias después. |

**Qué aportó cada uno**

- **Coinciden en lo esencial.** Las dos rondas encontraron que el modelo dominante es *freemium* con suscripción, que Chessable cobra con una doble decisión (PRO más cursos) y que academias, clubes y entrenadores son el stakeholder que casi nadie cobra. Esa coincidencia es la base más firme para elegir el modelo de ingresos.
- **Al profesor le faltó el competidor más obvio y a mí me sobró uno lejano.** La ronda del profesor no incluye Chess.com, que es la alternativa de pago más directa para un jugador de Lichess. Mi ronda sí, y con precios regionales para México, que son el ancla real de precio para el usuario. A cambio, Habitica está más lejos del problema que Duolingo, aunque es la mejor referencia de «juego de rol para cambiar un hábito».
- **Mi ronda encontró la fricción que importa a Zaqora: el momento del cobro.** Una pantalla de pago justo después de perder parecería monetizar la frustración. La ronda del profesor habla de fricciones genéricas (precio alto, plan anual, reembolso), útiles para el mercado pero no para la propuesta de valor.
- **La recomendación del profesor cambia de cliente.** Poner al B2B institucional como fuente principal convierte a Zaqora en una herramienta para entrenadores, cuando el segmento es un jugador amateur que pierde solo en Lichess. Mi ronda llega a los mismos clubes y academias, pero como segunda etapa, después de validar con el jugador.
- **Mi ronda propuso un stakeholder que nadie más vería: Lichess.** Como canal de adquisición, con una contribución por usuario conectado o una donación compartida. La propia respuesta advierte que choca con los principios de Lichess (sin anuncios, financiado por donaciones), así que es una hipótesis para explorar con cuidado, no un ingreso para el modelo.
- **El formato del profesor es más fácil de auditar.** Cada afirmación lleva su fuente en el campo que corresponde. Mi tabla mete fricción y stakeholders en una sola celda, lo que dificulta compararlas empresa por empresa.
- **Ojo con los datos.** No verifiqué los precios citados; algunos varían según la región y la fecha (por ejemplo, los de ChessMood y los de Chess.com). Antes de usarlos en el modelo económico hay que confirmarlos en las páginas oficiales.

---

### Paso 2 — Modelo económico del producto

**Herramienta:** Claude.

Con el modelo de ingresos del Paso 1 (*freemium* B2C, \$49–99 MXN al mes), se construyó el modelo económico: costo unitario, precio, punto de equilibrio, flujo de caja y VPN.

??? quote "Prompt completo — Prompt del profesor (Claude, modelo económico del producto)"
    Actúa como un analista financiero con especialización en modelos de negocio para startups de software en mercados emergentes latinoamericanos. Tu metodología combina el análisis de costos reales con proyecciones financieras conservadoras — siempre que hay incertidumbre, usas el escenario menos favorable para no generar falsas expectativas. Cuando los números no cierran, lo dices directamente y propones qué palancas puede mover el equipo: reducir costos, ajustar precio, cambiar modelo de ingresos, o reducir el alcance.

    Somos un equipo de emprendedores en México con un producto de software sin hardware. Necesitamos construir nuestro modelo económico antes de comprometer recursos en el desarrollo. Como no hay hardware, el BOM se traduce a costo por usuario activo (IA + infraestructura) y la «unidad» es el usuario.

    **NUESTRO PRODUCTO:**
    Nombre: Zaqora — concepto Ghost Engine
    Descripción: PWA web en formato de novela visual que convierte el aprendizaje de ajedrez en un videojuego de un solo jugador: tras perder en Lichess, el villano que encarna el error recurrente del jugador le escribe y lo invita a un capítulo construido sobre esa misma partida. Es para jugadores amateur de ajedrez online (Lichess) en México que, al perder, solo saben abandonar la sesión; usan Lichess porque es gratis y su disposición de pago aún no está verificada.
    Propuesta de valor: Cuando pierdes en Lichess y estás por cerrar la app, Zaqora valida tu frustración y la convierte en el próximo capítulo de tu historia.

    **MODELO DE INGRESOS ELEGIDO:**
    Freemium B2C. Los primeros capítulos son gratis; se cobra una temporada narrativa o una suscripción ligera cuando ya hay patrones suficientes para personalizar. Las licencias para academias y entrenadores (B2B2C) no esperan al año 2, pero tampoco cambian el producto (ver la decisión de abajo). Nunca se cobra justo después de una derrota.
    Justificación: el benchmarking (Chess.com, Chessable, ChessMood, Duolingo, Habitica) mostró que el freemium con suscripción recurrente domina el espacio, y el usuario objetivo está acostumbrado a lo gratuito, así que hace falta un nivel gratis para captarlo.
    Precio de hardware: \$0 MXN (no aplica: no hay hardware)
    Precio de suscripción: \$49–99 MXN/mes, o un pago único por temporada (rango coherente con el benchmark; por validar con usuarios beta)

    **NUESTRO BOM (componentes principales):**

    - LLM narrador (~20 capítulos/mes por usuario, modelo tipo Haiku), Anthropic o Google: \$3–6 MXN por usuario/mes
    - Worker con Stockfish (compartido), Railway o Fly.io: ~\$5 USD/mes entre todos
    - Costo variable total estimado: ≈ \$5–10 MXN por usuario/mes (tope del PDS: \$30 MXN)

    Costo fijo del piloto (en lugar de PCB + ensamble):

    - Cuenta de Google Play (pago único): ~\$460 MXN
    - Dominio para la landing: ~\$250 MXN
    - Créditos de API del LLM (\$20 USD): ~\$370 MXN
    - Worker durante 2 meses: ~\$185 MXN
    - Total del piloto: ~\$1,300 MXN (tope del curso: \$3,000 MXN)

    Costo de carcasa: \$0 MXN (no aplica)
    Mano de obra de ensamble y prueba: \$0 MXN (desarrollo propio, sin sueldo en el piloto)

    **COSTO DE LA IA:**
    Modelo usado: Claude Haiku o Gemini Flash (salida JSON estructurada; el LLM solo narra, el análisis lo hace Stockfish)
    Llamadas por día por usuario: ~0.7 (≈ 20 capítulos al mes)
    Tokens promedio por llamada: ~3,000 de entrada y ~1,000 de salida (el español usa ~30 % más tokens que el inglés)
    Precio por token: [precio vigente del proveedor, por verificar]
    Costo calculado: ≈ \$0.15–0.30 USD (≈ \$3–6 MXN)/mes por usuario

    **INFRAESTRUCTURA CLOUD:**
    Servicio: Supabase (Postgres + Auth + Edge Functions, plan gratuito) + worker en Python con Stockfish en Railway o Fly.io
    Costo estimado: ~\$5 USD (≈ \$93 MXN)/mes para 15–20 usuarios activos

    **VOLUMEN OBJETIVO:**
    Prueba de mercado (año 1): 15–20 usuarios beta
    Crecimiento año 2: hasta 1,200 clientes de pago (SOM de la semana 4 para los años 1–2)

    Con esta información, construye el modelo económico completo:

    1. **COSTO UNITARIO REAL:** Desglose completo del costo por usuario activo a volumen de 10 (prueba de mercado) y a volumen de 100 (escala inicial). Incluir: porción de cloud + porción de IA + overhead (15%) + contingencias (25%).
    2. **PRECIO DE VENTA:** Cost-plus con margen del 40%: ¿cuánto sería? Value-based: dado el valor que entrega al usuario, ¿cuánto podría cobrar? ¿El segmento pagaría ese precio? Precio recomendado y por qué.
    3. **PUNTO DE EQUILIBRIO:** Con el precio recomendado, ¿cuántos usuarios de pago necesitan para cubrir los costos fijos del primer año? ¿Es ese número alcanzable con los recursos del equipo?
    4. **FLUJO DE CAJA A 12 MESES:** Proyección mes a mes asumiendo: altas de usuarios según el plan de volumen, con la conversión de gratis a pago que consideres conservadora; suscripciones acumuladas (usuarios de pago activos × precio mensual); costos fijos mensuales (cloud, IA, overhead); inversión inicial en el mes 0. ¿En qué mes se alcanza flujo de caja positivo?
    5. **VPN DEL PROYECTO (simplificado):** Con los flujos del paso 4 y una tasa de descuento del 15% (costo de oportunidad razonable para emprendedor en México), ¿el VPN es positivo? ¿El proyecto crea valor en 12 meses?

    **FORMATO DE SALIDA:** MODELO ECONÓMICO (producto · modelo de ingresos) → COSTO UNITARIO (a 10 y a 100 usuarios, componente de mayor costo, % de la IA) → PRECIO DE VENTA (cost-plus 40 %, value-based, recomendado y por qué) → PUNTO DE EQUILIBRIO (usuarios de pago año 1, ¿alcanzable? ✅/⚠️/❌) → FLUJO DE CAJA (mes de flujo positivo, inversión acumulada antes de *break-even*) → VPN A 12 MESES (tasa 15 %) → ALERTAS (si algo no cierra; si la IA destruye el margen; si el mercado paga menos que el cost-plus) → PALANCAS DISPONIBLES (2–3 decisiones para mejorar la viabilidad).

??? abstract "Respuesta completa — Prompt del profesor (Claude)"
    **Modelo económico de Zaqora: freemium B2C**

    **Supuestos base** (cuando hubo duda tomé el escenario menos favorable):

    - **Precio de la IA:** Claude Haiku 4.5 cuesta \$1 USD por millón de tokens de entrada y \$5 USD por millón de salida (lista vigente de Anthropic). El precio de Gemini Flash no lo verifiqué.
    - **Tipo de cambio:** \$18.5 MXN/USD, el mismo que implican sus cifras.
    - **Costo de IA por usuario:** 20 capítulos × (3,000 tokens de entrada + 1,000 de salida) dan \$0.16 USD. Le sumé 30 % por el español (por si sus tokens no lo incluían) y queda en **\$0.21 USD ≈ \$3.85 MXN al mes**. Coincide con su estimado.
    - **Ingreso real por suscriptor:** el precio al usuario incluye 16 % de IVA. La pasarela (Stripe o Mercado Pago) cobra cerca de 3.6 % + \$3 MXN, más IVA sobre esa comisión. De \$59 MXN les quedan **\$44.92 MXN netos**.
    - **Escala de 100 usuarios:** el plan gratuito de Supabase pausa los proyectos inactivos, así que en producción conviene contar con el plan Pro (\$25 USD). Para 100 usuarios supuse además un worker de \$10 USD.

    ---

    **MODELO ECONÓMICO** · Producto: Zaqora — Ghost Engine · Modelo de ingresos: *Freemium* B2C (suscripción ligera)

    **COSTO UNITARIO (por usuario activo al mes)**

    | Concepto | 10 usuarios | 100 usuarios |
    | :--- | ---: | ---: |
    | Cloud (prorrateo) | \$9.25 | \$6.48 (Supabase Pro + worker de \$10 USD) |
    | IA (Haiku 4.5) | \$3.85 | \$3.85 |
    | Subtotal directo | \$13.10 | \$10.33 |
    | + Overhead 15 % | \$1.97 | \$1.55 |
    | + Contingencia 25 % | \$3.77 | \$2.97 |
    | **TOTAL** | **\$18.83 MXN** | **\$14.85 MXN** |

    - **Componente de mayor costo:** infraestructura *cloud*, 71 % del costo directo a 10 usuarios y 63 % a 100. Es un costo fijo que se reparte entre pocos usuarios.
    - **El costo de la IA representa:** 29 % del costo unitario a 10 usuarios y 37 % a 100. **La IA NO destruye el margen.**

    **PRECIO DE VENTA**

    - **Cost-plus (40 % de margen sobre el precio):** \$31 MXN/mes a 10 usuarios y \$25 MXN/mes a 100. Antes de IVA y comisiones; ya incluidos, \$40 y \$33 MXN.
    - **Value-based:** hasta \$79 MXN/mes. Ese es el techo psicológico frente a lo que un mexicano paga por *streaming* o por Duolingo Super. Pero el segmento eligió Lichess por ser gratis y su disposición de pago es CERO hasta demostrar lo contrario. Escenario conservador: \$49 MXN.
    - **Precio recomendado: \$59 MXN/mes con IVA incluido** (y una temporada de 3 meses a \$149) — por qué: \$49 deja solo \$36.71 netos, porque la comisión fija de \$3 MXN pesa mucho en tickets bajos. \$59 deja \$44.92 netos, unas 3 veces el costo unitario a escala, y sigue dentro de su benchmark de \$49–99. La temporada reduce comisiones y la sensación de «suscripción».

    **PUNTO DE EQUILIBRIO**

    - **Costos del año 1:** piloto \$1,300 + operación \$1,548 = \$2,848 MXN.
    - **Usuarios de pago necesarios año 1:** 7 usuarios pagando desde el mes 4 hasta el 12 (63 suscripciones-mes ÷ \$44.92). Para cubrir solo la operación mensual: 4.
    - **¿Alcanzable? ❌** — Con 20 usuarios beta, 7 de pago es 35 % de conversión. El *freemium* suele convertir entre 2 % y 5 %. Con 5 % tendrán 1 usuario de pago. Ojo: el dinero en juego es pequeño (menos de \$3,000). El costo real es el tiempo del equipo sin sueldo, que este modelo no cuenta.

    **FLUJO DE CAJA (resumen)**

    - **Mes de flujo positivo:** ninguno en 12 meses (cada mes desde el 4 cierra en −\$98).
    - **Inversión acumulada a 12 meses:** −\$2,444 MXN (no hay punto de equilibrio en el año).

    **VPN A 12 MESES (tasa 15 % anual = 1.17 % mensual)**

    **VPN = −\$2,359 MXN → Proyecto inviable como negocio en 12 meses.** El año 1, tal como está planeado, es un experimento de validación y no un negocio. Esto no es malo, pero hay que presupuestarlo así.

    ---

    **ALERTAS:**

    1. **El volumen del año 1 (20 usuarios) no puede sostener ni un worker de \$5 USD.** No es un problema de precio. Es un problema de escala: con 20 usuarios no hay precio razonable que cierre.
    2. **Los usuarios gratuitos son el costo oculto.** Con 5 % de conversión, cada suscriptor carga con 19 usuarios gratis. Si los gratuitos consumen 20 capítulos al mes, cada suscriptor arrastra unos \$73 de IA, por encima de los \$44.92 que deja. Hay que poner un tope de unos 5 capítulos al mes en el plan gratuito; con eso baja a unos \$18.
    3. **La disposición de pago no está verificada y es el supuesto que decide todo.** Antes de escribir código de pagos, prueben una preventa o una lista de espera con precio. Si menos de 2 de los 20 beta pagan, el B2C puro no se sostiene.
    4. **Si distribuyen como TWA en Google Play y venden contenido digital dentro de la app, Google exige su sistema de cobro (15 %).** Cobrar por la web les deja más.
    5. **Al pasar de 20 a 100 usuarios, Supabase Pro (\$462/mes) se vuelve el costo dominante.** Con 100 activos y 5 % de conversión (5 de pago) siguen en negativo; necesitan unos 15–20 de pago a ese volumen.

    **PALANCAS DISPONIBLES:**

    1. **Adelantar B2B2C (academias y entrenadores).** Una licencia de \$500–1,500 MXN al mes por academia cubre todo el costo fijo con un solo cliente. Es la palanca más fuerte, porque no depende de la conversión del jugador gratuito.
    2. **Volumen antes que precio.** El *break-even* mensual está en unos 4 de pago a 20 activos y unos 8 a 100 (con Supabase gratuito). Lleguen a unos 150–200 activos en el año 1 con comunidades de Lichess, Discord y clubes en México, antes de optimizar el precio.
    3. **Bajar el costo fijo y de IA:**
        - Usar *prompt caching* en el prompt base del narrador. La parte cacheada baja unas 10 veces su costo de entrada; el ahorro estimado en IA es de 30–40 %.
        - Usar el Batch API (50 % menos) para capítulos no urgentes. Encaja bien, porque la regla de «nunca cobrar justo después de una derrota» ya acepta que el capítulo no sea instantáneo.
        - Correr Stockfish en el navegador (WASM) en lugar del worker. Eso elimina los \$92.5 MXN al mes de costo fijo.

    ---

    **Detalle del flujo de caja (MXN)**

    Supuestos de la tabla:

    - **Usuarios activos:** 5, 10 y 15 en los meses 1 a 3, y 20 a partir del mes 4.
    - **Paywall:** se activa en el mes 4, cuando ya hay patrones suficientes para personalizar. Desde ahí hay 1 usuario de pago (5 % de conversión).
    - **Costos ya pagados en el piloto:** el worker de los meses 1 y 2 y los créditos de API (\$370 MXN). Los créditos alcanzan para los 12 meses si el plan gratuito tiene tope.
    - **Egresos:** incluyen 15 % de overhead y 25 % de contingencia.

    | Mes | Activos | Pago | Ingreso neto | Egresos | Flujo | Acumulado |
    | :---: | :---: | :---: | ---: | ---: | ---: | ---: |
    | 0 | — | — | — | 1,300.00 | −1,300.00 | −1,300.00 |
    | 1 | 5 | 0 | 0 | 48.89 | −48.89 | −1,348.89 |
    | 2 | 10 | 0 | 0 | 57.31 | −57.31 | −1,406.20 |
    | 3 | 15 | 0 | 0 | 158.23 | −158.23 | −1,564.44 |
    | 4–12 | 20 | 1 | 44.92 | 142.63 | −97.71 c/u | −2,443.87 |

    Pueden pensarlo así: el año 1 es una validación que cuesta unos \$2,500 MXN. La pregunta que tienen que contestar ahí no es «¿ganamos dinero?», sino «¿al menos 2 de cada 20 usuarios pagan, o una academia firma?». Si alguna se cumple, el modelo del año 2 cierra. Si ninguna se cumple, conviene replantear el modelo de ingresos antes de construir más.

#### Segunda ronda — prompt de autoría propia

Para la segunda ronda pedí un modelo a dos años de una startup con equipo, con métricas unitarias (LTV, CAC), embudo *freemium* y punto de equilibrio con sueldos.

??? quote "Prompt completo — Segunda ronda, prompt propio (Claude, modelo económico a 2 años)"
    Actúa como un CFO fraccional y analista financiero experto en startups B2C (SaaS y Gaming) en América Latina. Tu tarea es construir un modelo económico y financiero básico a 2 años para una startup en etapa inicial, utilizando un enfoque de cálculo desde los primeros principios (bottom-up y top-down). No inventes datos irrealistas; si asumes un porcentaje (ej. churn rate o costo de conversión), justifícalo con estándares de la industria del gaming/e-learning.

    **CONTEXTO DEL NEGOCIO:**

    - Concepto: Zaqora, un videojuego de ajedrez de un solo jugador que usa IA (LLM integrado con API de Lichess) para convertir las derrotas del usuario en una campaña narrativa adaptativa.
    - Segmento: Jugadores amateur en México que sufren "tilt" y abandonan la sesión por frustración.
    - Modelo de Ingresos: Freemium con upsell a suscripción mensual de \$300 MXN y opción anual.
    - Mercado Obtenible (SOM Año 1-2): Meta de 1,200 clientes pagadores (ingresos brutos teóricos de ~\$4.32 millones MXN/año).
    - Estrategia de Go-to-Market: Adquisición B2B2C mediante 40 aliados clave (clubes de ajedrez y streamers), donde cada uno genera 30 clientes.
    - Estructura Base: Startup conformada por un equipo operativo de 4 fundadores.

    **ENTREGABLES REQUERIDOS (Genera el reporte con tablas Markdown):**

    1. **Estructura de Costos (COGS y OPEX):**
        - Costos variables (COGS): Servidores de nube, costo estimado de tokens/API del motor LLM por usuario activo al mes, comisiones de pasarelas de pago (Stripe/Apple/Google) y márgenes o comisiones de ingresos compartidos para los aliados (streamers/clubes).
        - Costos fijos (OPEX): Salario de supervivencia para el equipo de 4 personas, costos legales/contables y herramientas de software.
    2. **Métricas Unitarias (Unit Economics):**
        - Estimación del LTV (Life Time Value) basada en un churn rate realista para aplicaciones gamificadas de nicho.
        - Estimación del CAC (Costo de Adquisición de Clientes) contemplando el modelo orgánico y de alianzas.
        - Ratio LTV:CAC esperado.
    3. **Embudo de Adquisición Freemium:** Considerando tasas de conversión estándar de la industria (ej. 3% al 5%), calcula cuántos usuarios gratuitos totales (MAU) necesitamos adquirir para alcanzar la meta de los 1,200 usuarios de pago.
    4. **Análisis de Punto de Equilibrio (Break-Even):** ¿Cuántos usuarios de pago recurrentes activos a \$300 MXN/mes se necesitan exactamente para cubrir los costos fijos y variables del equipo de 4 personas? Muestra la fórmula y el margen de contribución.
    5. **Riesgos del Modelo Financiero:** Identifica los 2 mayores riesgos de flujo de caja de este modelo operativo (ej. el costo computacional del LLM a escala vs. el precio fijo de suscripción) y propone 2 mitigaciones tácticas.

??? abstract "Respuesta completa — Segunda ronda, prompt propio (Claude)"
    **Zaqora: modelo económico y financiero a 24 meses**

    **Supuestos base:** tipo de cambio de 18.5 MXN/USD. El precio de \$300 MXN incluye IVA, porque en México el precio al consumidor debe mostrarse con impuestos. Plan anual de \$2,400 MXN (equivale a \$200 al mes, 33 % de descuento). Mezcla de 70 % mensual y 30 % anual.

    > ⚠️ **Primer ajuste de CFO:** los \$4.32M de ingreso teórico (1,200 × \$300 × 12) no son ingreso real. Quitando el IVA, la mezcla de planes y la rampa de adquisición, el **Año 1 cierra en ~\$1.19M MXN netos** y el **Año 2 en ~\$4.7M MXN**. Los \$4.32M solo se alcanzan como *run-rate* hacia el mes 12.

    ---

    **1. Estructura de costos**

    *1a. Costos variables (COGS) por usuario de pago al mes*

    | Concepto | Plan mensual | Plan anual (al mes) | Justificación |
    | :--- | ---: | ---: | :--- |
    | **Ingreso neto de IVA** | **\$258.6** | **\$172.4** | \$300 / 1.16 y \$2,400 / 1.16 / 12 |
    | Pasarelas (50 % tiendas, 50 % web) | \$26.3 | \$16.7 | Apple/Google cobran 15 % (Small Business Program). Stripe MX cobra 3.6 % + \$3 por cobro. La web pesa más porque los aliados comparten links directos |
    | Revenue share para aliados (20 %) | \$51.7 | \$34.5 | Estándar de afiliados en suscripción: 20–30 % recurrente. Propuesta: 20 % durante 12 meses |
    | Tokens del LLM | \$10.0 | \$10.0 | Ver cálculo abajo |
    | Nube (backend, BD, análisis, CDN) | \$5.0 | \$5.0 | ~US\$0.27 por usuario activo. La API de Lichess es gratuita; Stockfish puede correr en el cliente |
    | **Subsidio freemium** (24 usuarios gratuitos por cada pagador) | \$19.2 | \$19.2 | Cada usuario gratuito cuesta ~\$0.80 al mes (3 narrativas con modelo ligero + infraestructura). Es un costo oculto que suele olvidarse |
    | Reembolsos y contracargos (1.5 %) | \$3.9 | \$2.6 | Estándar en suscripciones B2C |
    | **Total COGS** | **\$116.1** | **\$87.9** | |
    | **Margen de contribución** | **\$142.5 (55 %)** | **\$84.5 (49 %)** | |
    | **Contribución ponderada (70/30)** | **\$125.1 por usuario al mes** | | |

    *Cálculo del costo del LLM (usuario de pago típico al mes):*

    - 25 derrotas narradas × (6k tokens de entrada + 1k de salida) = 150k / 25k.
    - 20 mensajes de coach × (3k + 0.5k) = 60k / 10k.
    - Total: **210k tokens de entrada y 35k de salida al mes.**
    - Con un ruteo de 70 % Haiku 4.5 (US\$1 / US\$5 por millón de tokens) y 30 % Sonnet 5.5 (US\$2 / US\$10), más *prompt caching* (las lecturas de caché cuestan ~10 %), sale en ~US\$0.37, unos \$6.9 MXN.
    - Le sumo 40 % de colchón por reintentos y usuarios intensivos: **\$10 MXN**.

    *1b. Costos fijos (OPEX) al mes*

    | Concepto | Año 1 | Año 2 | Nota |
    | :--- | ---: | ---: | :--- |
    | Salarios de supervivencia (4 × \$18,000, asimilados) + 3 % de ISN | \$74,200 | \$88,000 | En el Año 2 sube a ~\$21,000 por persona |
    | Contador externo + legal amortizado | \$8,000 | \$9,000 | Legal: SAPI, T&C, aviso de privacidad (LFPDPPP), marca IMPI |
    | Herramientas de software | \$6,500 | \$7,000 | Workspace, GitHub, Figma, Sentry, analítica, cuentas de desarrollador Apple y Google |
    | Infraestructura fija (staging, BD mínima) | \$3,000 | \$3,000 | |
    | Programa de aliados (torneos, premios, kits) | \$8,000 | \$8,000 | |
    | **Total OPEX** | **\$99,700** | **\$115,000** | |

    Además hay un gasto único antes del lanzamiento de **\$125,000**: constitución (\$25k), bono de activación de \$1,500 por aliado (\$60k) y *streams* patrocinados (\$40k).

    ---

    **2. Métricas unitarias (Unit Economics)**

    *Churn:*

    - **Plan mensual: 10 % al mes.** Los reportes de la industria, como *State of Subscription Apps* de RevenueCat, ubican la retención de planes mensuales en juegos y educación en 8–15 % de churn mensual. Un nicho de alta intención, como el ajedrez, cae en la parte baja del rango. Vida esperada: 10 meses.
    - **Plan anual: 35 % de renovación.** El rango típico B2C es 30–45 %. Vida esperada: 1.54 años (~18.5 meses).

    | Métrica | Mensual | Anual | Ponderado |
    | :--- | ---: | ---: | ---: |
    | LTV de ingreso neto | \$2,586 | \$3,183 | \$2,765 |
    | **LTV de contribución** (después de COGS y rev share) | \$1,425 | \$1,558 | **\$1,465** |

    *CAC:*

    | Canal | CAC | Cálculo |
    | :--- | ---: | :--- |
    | Aliados, solo efectivo | \$163 | (\$96k del programa anual + \$60k de bonos + \$40k de *streams*) / 1,200 |
    | Aliados, *fully loaded* (incluye 50 % del tiempo de un fundador) | **\$253** | + \$108k / 1,200 |
    | Orgánico (ASO, contenido, referidos) | ~\$100 | Herramientas de contenido |
    | Paid ads (solo referencia, no está en el plan) | ~\$460 | CPI en LatAm ~US\$1 / 4 % de conversión |

    *Ratio LTV:CAC:*

    | Vista | LTV | CAC | Ratio |
    | :--- | ---: | ---: | ---: |
    | Operativa (rev share como COGS) | \$1,465 | \$253 | **5.8x** |
    | Conservadora (rev share de 12 meses reclasificado como CAC) | \$2,018 | \$637 | **3.2x** |
    | Payback del CAC | | | **~2 meses** |

    Las dos vistas superan el umbral de 3x. La vista conservadora es la que conviene mostrarle a un inversionista.

    ---

    **3. Embudo de adquisición freemium**

    Para tener 1,200 usuarios de pago **activos** al mes 12 con un churn ponderado de 7 % al mes, hacen falta **~1,730 altas brutas de pago** en el año.

    | Conversión MAU → pago | MAU necesarios en estado estable | Instalaciones acumuladas (35 % de activación a MAU) | Instalaciones por aliado |
    | :--- | ---: | ---: | ---: |
    | 3 % (conservador) | 40,000 | ~114,000 | ~2,860 |
    | **4 % (base)** | **30,000** | **~86,000** | **~2,140** |
    | 5 % (optimista) | 24,000 | ~69,000 | ~1,710 |

    > ⚠️ **Hallazgo crítico sobre el GTM:** «40 aliados × 30 clientes» no funciona parejo para todos. Un club de 80 miembros activos necesitaría que el 37 % pague, cuando en un club real esperaría cerca de 12 %. Lo recomiendo recomponer así: **10 streamers × 90 pagadores = 900** y **30 clubes × 10 pagadores = 300**. Los streamers generan el volumen y los clubes aportan retención y credibilidad.

    ---

    **4. Punto de equilibrio**

    ```text
    Usuarios en equilibrio = Costos fijos mensuales / Margen de contribución por usuario

    Margen de contribución = Precio neto de IVA − COGS variable por usuario
                           = $258.6 − $116.1 = $142.5 (55.1%)
    ```

    | Escenario | Cálculo | **Usuarios de pago activos** |
    | :--- | :--- | ---: |
    | 100 % plan mensual a \$300, Año 1 | \$99,700 / \$142.5 | **700** |
    | Mezcla 70/30, Año 1 | \$99,700 / \$125.1 | **797** |
    | Mezcla 70/30, Año 2 (OPEX de \$115k) | \$115,000 / \$125.1 | **920** |

    *Proyección trimestral* (contribución = ingreso neto menos COGS; EBITDA = contribución menos OPEX):

    | Trimestre | Activos al cierre | Ingreso neto | Contribución | OPEX | EBITDA |
    | :--- | ---: | ---: | ---: | ---: | ---: |
    | Q1 (desarrollo) | 0 | \$0 | \$0 | \$299k | −\$299k |
    | Q2 | 250 | \$105k | \$56k | \$299k | −\$243k |
    | Q3 | 700 | \$372k | \$200k | \$299k | −\$99k |
    | Q4 | 1,200 | \$715k | \$384k | \$299k | **+\$85k** |
    | Q5–Q8 | 1,420 → 2,050 | \$4.71M (Año 2) | — | \$1.38M | **+\$1.15M** |

    - El equilibrio operativo llega en el **mes 10**.
    - El valle de caja es de **−\$766k MXN**, contando el gasto de prelanzamiento.
    - **Hay que levantar ~\$1.0M MXN** (pre-seed, FFF o un programa como Startup México), que cubre el valle más un colchón de 3 meses.

    ---

    **5. Riesgos de flujo de caja y mitigaciones**

    | # | Riesgo | Impacto cuantificado |
    | :--- | :--- | :--- |
    | **R1** | **Costo del LLM a escala contra un precio fijo.** Usuarios intensivos (más de 60 derrotas al mes) atendidos solo con Sonnet, sumado al subsidio de los usuarios gratuitos. | Un usuario intensivo puede costar ~\$43 al mes en vez de \$10. Si 20 % de la base es intensiva, la contribución mensual cae de \$142 a ~\$115 y el equilibrio sube de 700 a ~870 usuarios. Una caída del peso a 21 MXN/USD encarece todavía más el costo en dólares. |
    | **R2** | **Concentración en aliados y churn temprano.** El 100 % de la adquisición pasa por 40 terceros. Si 3 de los 10 streamers bajan su actividad, se pierde ~27 % del *pipeline*. Además, el 20 % de rev share se paga desde el día 1, y los cobros de las tiendas llegan unos 45 días después. | Con un churn mensual de 15 % en lugar de 10 %, el LTV baja a ~\$950 y el valle de caja se profundiza a ~\$1.1M. |

    *Mitigaciones tácticas:*

    1. **Topes y ruteo del LLM (contra R1).** Limitar el plan gratuito a 3 narrativas al mes y dar al de pago un uso justo de 40 narrativas, con un paquete extra de \$49. Rutear el 80 % de las llamadas a Haiku y usar Sonnet solo en los capítulos clave de la campaña. Precalcular narrativas genéricas por tipo de apertura o error con la Batch API, que cuesta 50 % menos. Poner una alerta si el costo del LLM supera el 8 % del ingreso neto. **Objetivo: costo del LLM por debajo de \$8 por usuario de pago.**
    2. **Rev share escalonado y empuje al plan anual (contra R2).** Pagar al aliado 20 % los primeros 6 meses y 10 % del mes 7 al 12, siempre después de que el cobro se liquide, nunca por adelantado. Ofrecer el plan anual con un incentivo, por ejemplo un capítulo exclusivo. Subir la mezcla de 30 % a 45 % anual adelanta ~\$400k de caja en el Año 1 y reduce el churn efectivo. Abrir un canal orgánico (referidos y torneos propios) que llegue al 25 % de las altas en el Año 2.

    > **Alerta de precio:** \$300 MXN (~US\$16) está por encima de Chess.com Diamond (~US\$14 al mes en EE. UU.), y Lichess es gratis. Antes de fijarlo, conviene probar dos precios en paralelo: **\$300 contra \$179**. Con \$179 el equilibrio sube a unos 1,500 usuarios, pero la conversión podría duplicarse. Es la variable con más sensibilidad de todo el modelo.

#### Comparación de los dos prompts

| | **Prompt del profesor** | **Prompt propio** |
| :--- | :--- | :--- |
| **Rol asignado** | Analista financiero conservador: si hay duda, el escenario menos favorable. | CFO fraccional de startups B2C (SaaS y *gaming*). |
| **Supuestos de entrada** | Los de esta semana: precio de \$49–99, 15–20 usuarios beta, costos del piloto de la semana 5, sin sueldos. | Los de la semana 4: \$300 al mes, 1,200 clientes, 40 aliados y 4 fundadores con sueldo. |
| **Horizonte** | 12 meses, mes a mes, con VPN al 15 %. | 24 meses por trimestre, sin VPN ni TIR. |
| **Precio** | Recomienda **\$59 MXN** con IVA (\$44.92 netos). | Usa **\$300 MXN** (\$258.6 netos) y propone probarlo contra \$179. |
| **Costo de la IA por usuario** | **\$3.85 MXN** (20 capítulos con Haiku 4.5). | **\$10 MXN** (25 derrotas + 20 mensajes, con 30 % de Sonnet y colchón de 40 %). |
| **Punto de equilibrio** | 7 de pago en el año (35 % de conversión): **no alcanzable**. | **700–920** usuarios de pago activos. |
| **Veredicto** | **VPN = −\$2,359 MXN**: el año 1 es una validación de ~\$2,500, no un negocio. | Equilibrio en el **mes 10**, pero hay que levantar **~\$1.0M MXN**. |

**Qué aportó cada uno**

- **Mi prompt usó supuestos que el propio Paso 1 ya había descartado.** Volví a pedir \$300 MXN al mes y 1,200 clientes con 40 aliados, cuando el benchmarking acababa de mostrar que ese precio está fuera de mercado. La respuesta lo detectó por su cuenta («\$300 está por encima de Chess.com Diamond»). Los números de mi modelo son coherentes entre sí, pero describen una empresa que no es la que el benchmark recomienda.
- **Los dos modelos responden preguntas distintas, y las dos sirven.** El del profesor pregunta si el piloto se sostiene, y la respuesta es no: con 20 usuarios no hay precio que cierre. El mío pregunta cuánto hace falta para que el equipo viva de esto: unos 800 usuarios de pago y ~\$1.0M MXN de inversión. Juntos dicen que el problema de Zaqora no es la IA ni el precio, sino la escala.
- **El sueldo cambia todo el modelo.** El del profesor no cuenta el tiempo del equipo (y lo advierte como alerta); el mío lo pone como el 74 % del OPEX. Con sueldos, los \$2,500 del piloto pasan a \$99,700 al mes.
- **Coinciden en el costo oculto: los usuarios gratuitos.** El profesor calcula que cada suscriptor carga con 19 gratuitos (~\$73 de IA si no hay tope) y propone 5 capítulos al mes; el mío, 24 gratuitos (~\$19) con un tope de 3 narrativas. Los dos llegan a la misma regla: el plan gratuito necesita un límite.
- **Coinciden en el IVA, las comisiones y las palancas.** Los dos descuentan el 16 % de IVA y la comisión de la pasarela antes de calcular el margen, y los dos proponen *prompt caching* y Batch API para bajar el costo de la IA.
- **El del profesor cumple el formato del curso; el mío, no.** La tarea pide flujo de caja mes a mes a 12 meses y VPN al 15 %. Mi modelo da LTV, CAC y un embudo útiles para un inversionista, pero no calcula VPN ni TIR.
- **Mi modelo encontró un error en mi plan de adquisición.** «40 aliados × 30 clientes» exigiría que el 37 % de un club pague; recomponerlo como 10 *streamers* y 30 clubes es un hallazgo que el modelo del profesor no podía dar, porque no incluía aliados.
- **Datos por verificar.** El precio de Haiku 4.5 (US\$1 / US\$5 por millón de tokens) coincide con la lista de Anthropic. El modelo «Sonnet 5.5» y su precio (US\$2 / US\$10) también coinciden con la lista de Anthropic. La comisión de Stripe México (3.6 % + \$3, sin IVA) se confirmó en su página; las de Mercado Pago y las tiendas siguen sin verificar.

---

## 4) Entregable — Viabilidad económica de Zaqora

**Equipo:** _David López Ramírez_ · **Producto:** _Zaqora_ · **Concepto:** _Ghost Engine_ · **Fecha:** _08/10/2026_

### 1. Benchmarking consolidado

Las cinco empresas de las dos rondas. Las conversiones a pesos usan un tipo de cambio de referencia de 18.5 MXN/USD (el mismo del PDS) y son solo orientativas.

| Empresa | Qué ofrece | Modelo de ingresos | Precio mensual | ≈ MXN al mes | Fricción principal |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Chess.com** | Juego, análisis y lecciones de ajedrez | *Freemium* + suscripción escalonada | US\$5.46–13.65 (precio para México) | ≈ \$101–253 | Entender qué límite gratuito te afecta y cuál de los niveles conviene. |
| **Chessable** | Cursos con repetición espaciada | Híbrido: PRO + cursos de pago único | PRO US\$11.99 (US\$74.99/año); cursos US\$20–100 | ≈ \$222 (PRO mensual) | Doble decisión: suscripción y curso. |
| **ChessMood** | Cursos en video de grandes maestros | Suscripción en dos niveles | US\$79–129 | ≈ \$1,460–2,390 | Precio alto y compromiso anual. |
| **Duolingo** | Idiomas gamificados | *Freemium* + Super + publicidad + B2B | US\$6.99 | ≈ \$129 | Poca conversión de gratis a pago. |
| **Habitica** | Hábitos como juego de rol | *Freemium* + suscripción cosmética + planes grupales | US\$4.99 (US\$47.99/año) | ≈ \$92 | Se siente como pagar por personalización, no por un resultado. |

**Modelo predominante:** *freemium* con suscripción recurrente, en las dos rondas.

**Stakeholders no explotados:** academias, clubes y entrenadores (las dos rondas); padres y escuelas; Lichess como canal de adquisición, condicionado a sus principios.

### 2. Implicaciones para el modelo de ingresos de Zaqora

!!! warning "Modelo decidido, disposición a pagar por validar"
    Este modelo resume lo que dicen las dos rondas de benchmarking. El modelo económico (Paso 2) confirma que el costo cabe, pero el año 1 no cierra: falta medir la disposición a pagar de los usuarios beta.

- **Modelo propuesto:** *freemium* B2C. Los primeros capítulos son gratis; se cobra una temporada narrativa o una suscripción ligera cuando ya hay patrones suficientes para personalizar. Las licencias para academias y entrenadores (B2B2C) no esperan al año 2, pero tampoco cambian el producto (ver la decisión de abajo).
- **Desafío de diseño:** el momento del cobro. Nunca mostrar una pantalla de pago justo después de una derrota: el siguiente capítulo es gratis y el pago se ofrece a cambio de una promesa futura (más villanos, temporadas completas, historial).
- **El precio de la semana 4 queda fuera de mercado.** \$300 MXN al mes está por encima de Chess.com, Chessable, Duolingo y Habitica en México; solo ChessMood cobra más. Un rango coherente con el benchmark y con el piloto propuesto en la semana 5 está entre \$49 y \$99 MXN al mes, o un pago único por temporada.
- **Decisión sobre las licencias (B2B2C):** buscar **una academia piloto a partir del mes 7**, después de tres meses de datos con jugadores, que pague el acceso de sus alumnos a Zaqora tal como es, **sin construir un *dashboard*** para entrenadores. Es la única palanca que vuelve positivo el VPN del año 1, y hacerlo así no desvía el producto del jugador que pierde solo. El escenario base no cuenta ese ingreso hasta que haya una carta de intención firmada, para no inflar el modelo.
- **Decisión sobre Google Play:** el piloto **incluye** la cuenta de desarrollador (US\$25, pago único), además de la distribución por URL.
- **El costo no es el problema.** El modelo económico pone el costo en \$18.83 MXN por usuario a 10 usuarios y \$14.85 a 100, y el precio recomendado (\$59 MXN) deja \$44.92 netos. El riesgo sigue siendo que el usuario acepte pagar algo.

### 3. Modelo económico

Resumen del modelo del Paso 2 con el prompt del profesor, que es el que sigue el formato del curso (12 meses, VPN al 15 %) y usa el modelo de ingresos elegido. Tipo de cambio: 18.5 MXN/USD.

| Concepto | Resultado |
| :--- | :--- |
| **Costo unitario** (por usuario activo al mes) | **\$18.83 MXN a 10 usuarios** · \$14.85 MXN a 100 usuarios (incluye 15 % de overhead y 25 % de contingencia) |
| **Componente de mayor costo** | Infraestructura *cloud*: 71 % del costo directo a 10 usuarios y 63 % a 100 |
| **Peso de la IA** | 29 % del costo unitario a 10 usuarios y 37 % a 100: no destruye el margen |
| **Precio cost-plus (40 %)** | \$40 MXN al mes a 10 usuarios y \$33 MXN a 100, con IVA y comisiones |
| **Precio value-based** | Hasta \$79 MXN al mes; escenario conservador, \$49 MXN |
| **Precio recomendado** | **\$59 MXN al mes con IVA** (\$44.92 netos) o temporada de 3 meses a \$149 MXN |
| **Punto de equilibrio año 1** | 7 usuarios de pago desde el mes 4 (35 % de conversión sobre 20 beta): ❌ no alcanzable |
| **Flujo de caja** | Ningún mes positivo en 12 meses; acumulado de −\$2,444 MXN |
| **VPN a 12 meses (15 %)** | **−\$2,359 MXN → inviable como negocio en 12 meses**: el año 1 es una validación |

**Costo mensual de la IA** (arquitectura del concepto Ghost Engine: el LLM solo narra; el análisis lo hace Stockfish):

| Concepto | Valor |
| :--- | :--- |
| Modelo | Claude Haiku 4.5: US\$1 por millón de tokens de entrada y US\$5 por millón de salida (**verificado** en la lista de precios de Anthropic el 08/10/2026) |
| Llamadas por usuario | ~20 capítulos al mes (≈ 0.7 al día) |
| Tokens por llamada | 3,000 de entrada + 1,000 de salida, más 30 % por el español |
| Costo por usuario activo | US\$0.21 ≈ **\$3.85 MXN al mes** |
| 20 usuarios beta | ≈ \$77 MXN al mes |
| 100 usuarios | ≈ \$385 MXN al mes |
| 1,200 usuarios | ≈ \$4,620 MXN al mes |

Las cifras por volumen multiplican el costo por usuario activo; los usuarios gratuitos cuentan igual mientras el plan gratuito no tenga tope. Con un tope de 5 capítulos al mes, cada usuario gratuito cuesta cerca de una cuarta parte.

**Qué falta para que cierre:** al menos 2 de cada 20 usuarios beta pagando, o una academia con licencia de \$500–1,500 MXN al mes. El modelo a dos años (prompt propio) agrega la otra cara: si el equipo cobra sueldo, el equilibrio está en ~800 usuarios de pago y hace falta levantar ~\$1.0M MXN.

### 4. Hoja de cálculo del modelo

[Descargar el modelo económico (Excel)](recursos/archivos/PI4_S7/Zaqora_Modelo_Economico_S7.xlsx)

El libro reconstruye el modelo del Paso 2 con todas las fórmulas visibles. Tiene siete hojas: **Supuestos** (todos los datos de entrada; azul = editable, verde = precio verificado, amarillo = supuesto clave), **BOM**, **Costo IA**, **Costo unitario**, **Flujo de caja**, **Sensibilidad** y **Ejercicios** (4–9). Al cambiar un supuesto, todo se recalcula.

Coincide con la respuesta de la IA en el costo unitario (\$18.83 y \$14.84 MXN), el costo de la IA (\$3.85 MXN) y el ingreso neto por suscriptor (\$44.92 MXN). El VPN sale más negativo (**−\$2,636** contra −\$2,359) por una diferencia de supuestos: en la hoja, los créditos de API (\$370 MXN) se consumen mes a mes y se agotan en el mes 7 si el plan gratuito no tiene tope; la respuesta de la IA suponía que alcanzaban para todo el año. La inversión inicial es de \$1,222.48 porque el dominio verificado cuesta US\$11.08 (\$205) y no los \$250 estimados.

**Flujo de caja mes a mes (escenario base: 20 usuarios beta, 5 % de conversión, cobro desde el mes 4, sin tope gratuito, con cuenta de Google Play, sin ingresos de academias)**

| Mes | Activos | De pago | Ingreso neto | Cloud | IA pagada | Egresos totales | Flujo neto | Acumulado | Flujo descontado |
| :---: | :---: | :---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | — | — | — | — | — | 1,222.48 | −1,222.48 | −1,222.48 | −1,222.48 |
| 1 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | −1,222.48 | 0 |
| 2 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | −1,222.48 | 0 |
| 3 | 15 | 0 | 0 | 92.50 | 0 | 132.97 | −132.97 | −1,355.45 | −128.40 |
| 4 | 20 | 1 | 44.92 | 92.50 | 0 | 132.97 | −88.05 | −1,443.50 | −84.04 |
| 5 | 20 | 1 | 44.92 | 92.50 | 0 | 132.97 | −88.05 | −1,531.55 | −83.07 |
| 6 | 20 | 1 | 44.92 | 92.50 | 0 | 132.97 | −88.05 | −1,619.60 | −82.11 |
| 7 | 20 | 1 | 44.92 | 92.50 | 53.28 | 209.56 | −164.64 | −1,784.24 | −151.75 |
| 8 | 20 | 1 | 44.92 | 92.50 | 76.96 | 243.60 | −198.68 | −1,982.92 | −181.00 |
| 9 | 20 | 1 | 44.92 | 92.50 | 76.96 | 243.60 | −198.68 | −2,181.60 | −178.91 |
| 10 | 20 | 1 | 44.92 | 92.50 | 76.96 | 243.60 | −198.68 | −2,380.28 | −176.84 |
| 11 | 20 | 1 | 44.92 | 92.50 | 76.96 | 243.60 | −198.68 | −2,578.96 | −174.79 |
| 12 | 20 | 1 | 44.92 | 92.50 | 76.96 | 243.60 | −198.68 | −2,777.64 | −172.77 |
| **Total** | | | **404.26** | **925.00** | **438.08** | **3,181.91** | **−2,777.64** | | **VPN = −2,636.16** |

Egresos = (cloud + IA pagada) × 1.4375 (15 % de overhead y 25 % de contingencia), más la inversión del mes 0. Los meses 1 y 2 no tienen egresos porque el worker está prepagado en el piloto y la IA se cubre con los créditos. La TIR no existe: ningún flujo es positivo. Tasa mensual equivalente al 15 % anual: 1.17 %.

**Escenarios** (calculados con la misma hoja, cambiando solo las palancas de Supuestos):

| Escenario | Flujo acumulado a 12 meses | VPN (15 %) | Primer mes positivo |
| :--- | ---: | ---: | :---: |
| Base | −\$2,778 | **−\$2,636** | Ninguno |
| Tope de 5 capítulos en el plan gratuito | −\$2,148 | **−\$2,073** | Ninguno |
| Base + 1 academia piloto a \$1,000/mes desde el mes 7 | +\$3,222 | **+\$2,736** | Mes 7 |
| Tope de 5 + academia piloto desde el mes 7 | +\$3,852 | **+\$3,299** | Mes 7 |
| Cambiar el narrador a Claude Haiku 5.5 (sin tope, sin academia) | −\$2,148 | **−\$2,073** | Ninguno |

Todos los escenarios incluyen la cuenta de Google Play (inversión inicial de \$1,222.48). Con Haiku 5.5 el costo de la IA baja de \$3.85 a \$0.50 MXN por usuario y el costo unitario de \$18.83 a \$14.02 a 10 usuarios; su VPN coincide con el del tope de 5 capítulos porque, en ambos casos, los créditos de API alcanzan para los 12 meses y la IA no genera pagos en efectivo.

**Sensibilidad al precio:** con la operación del mes 12, a \$59 MXN hacen falta 6 suscriptores (30 % de 20 usuarios activos, o 6 % de 100); a \$99, 4; a \$300, 2. Ningún precio razonable cierra con 20 usuarios: el problema es la escala, no el precio.

#### «BOM» verificado (08/10/2026)

Precios consultados en las páginas oficiales de cada proveedor. Están también en la hoja **BOM** del libro, con fondo verde. En servicios, el «tiempo de entrega» es el tiempo de alta o activación; el único con espera real es la cuenta de Google Play, así que conviene abrirla primero.

| Componente | Proveedor | Precio verificado | Fuente | Nota | Tiempo de entrega |
| :--- | :--- | :--- | :--- | :--- | :--- |
| LLM narrador | Anthropic, Claude Haiku 4.5 | US\$1 (entrada) / US\$5 (salida) por millón de tokens | platform.claude.com, *Pricing* | Ya aparece como modelo heredado; *cache* a US\$0.10 y Batch API a US\$0.50 / US\$2.50 | Inmediato (clave de API) |
| Alternativa de LLM | Anthropic, Claude Haiku 5.5 | US\$0.10 / US\$0.50 por millón (prompts de hasta 100k tokens) | platform.claude.com, *Pricing* | Tokenizador nuevo: ~30 % más tokens por el mismo texto. Aun así, ~7.7 veces más barato | Inmediato |
| Worker con Stockfish | Railway, plan Hobby | US\$5 al mes, con US\$5 de uso incluido | railway.com/pricing | El uso extra se cobra aparte (~US\$20 por vCPU al mes en uso continuo). Fly.io no tiene nivel gratuito | Inmediato (despliegue en minutos) |
| Base de datos y autenticación | Supabase Free | US\$0 (50,000 usuarios activos, 500 MB) | supabase.com/pricing | Pausa el proyecto tras 1 semana sin actividad | Inmediato |
| Base de datos a escala | Supabase Pro | Desde US\$25 al mes | supabase.com/pricing | 100,000 usuarios activos, 8 GB | Inmediato (cambio de plan) |
| Dominio | Porkbun, .com | US\$11.08 al año (registro y renovación) | porkbun.com | Un .mx cuesta US\$35.57 | Minutos (registro y DNS) |
| Cuenta de desarrollador | Google Play | US\$25, pago único | Ayuda de Play Console | Incluida en el piloto | 1–2 semanas (supuesto): exige verificación de identidad y Google no publica un plazo |
| Pasarela de pago | Stripe México | 3.6 % + \$3.00 MXN por cobro con tarjeta nacional | stripe.com/mx/pricing | Las comisiones excluyen IVA | Inmediato en modo de prueba; cobros reales tras verificar la cuenta |
| *Hosting* de la PWA y la landing | Cloudflare Pages, plan gratuito | US\$0 | developers.cloudflare.com | 500 *builds* al mes, 20,000 archivos. Vercel Hobby se descartó: solo permite uso personal no comercial | Inmediato (despliegue en minutos) |
| Tipo de cambio | Banxico, FIX | 17.978 MXN/USD (07/10/2026) | banxico.org.mx | El modelo usa 18.5 como colchón conservador (~3 %) | — |

### 5. Ejercicios 4–9 (VPN, TIR y sensibilidad)

Resueltos con las fórmulas de la clase. La TIR se calcula por interpolación lineal, como pide el curso, y se compara con la TIR exacta (función `TIR` de Excel). Los mismos cálculos están, con fórmulas, en la hoja **Ejercicios** del libro de Excel.

$$
VPN = -A + \sum_{t=1}^{n} \frac{F_t}{(1+r)^t} \qquad TIR \approx r_1 + (r_2 - r_1)\,\frac{VPN_1}{VPN_1 - VPN_2}
$$

Regla de decisión: **VPN > 0** y **TIR > tasa de descuento** → el proyecto es viable.

??? example "Ejercicio 4 — InnovaTech: \$250,000 USD, \$60,000 USD al año por 6 años, tasa del 11 %"
    Como los flujos son iguales, se puede usar el factor de anualidad:

    $$
    FA = \frac{1-(1.11)^{-6}}{0.11} = 4.2305 \qquad VPN = -250{,}000 + 60{,}000 \times 4.2305 = -250{,}000 + 253{,}832.27
    $$

    | Año | Flujo | ÷ (1.11)^t | Valor presente |
    | :---: | ---: | ---: | ---: |
    | 1 | 60,000 | 1.1100 | 54,054.05 |
    | 2 | 60,000 | 1.2321 | 48,697.35 |
    | 3 | 60,000 | 1.3676 | 43,871.48 |
    | 4 | 60,000 | 1.5181 | 39,523.86 |
    | 5 | 60,000 | 1.6851 | 35,607.08 |
    | 6 | 60,000 | 1.8704 | 32,078.45 |
    | | | **Suma** | **253,832.27** |

    - **VPN (11 %) = +\$3,832.27 USD**
    - **TIR por interpolación:** con r₁ = 11 % (VPN = +3,832.27) y r₂ = 12 % (VPN = −3,315.56): 11 % + 1 % × 3,832.27 / 7,147.83 = **11.54 %** (exacta: 11.53 %).
    - **Decisión: viable, pero por muy poco.** El VPN es apenas el 1.5 % de la inversión y la TIR supera la tasa por medio punto: un error pequeño en los flujos lo vuelve inviable.

??? example "Ejercicio 5 — Inversión de \$50,000 USD; flujos de 7,500 / 12,000 / 20,000 / 25,000; tasa del 4 %"
    | Año | Flujo | ÷ (1.04)^t | Valor presente |
    | :---: | ---: | ---: | ---: |
    | 1 | 7,500 | 1.0400 | 7,211.54 |
    | 2 | 12,000 | 1.0816 | 11,094.67 |
    | 3 | 20,000 | 1.1249 | 17,779.93 |
    | 4 | 25,000 | 1.1699 | 21,370.10 |
    | | | **Suma** | **57,456.24** |

    - **VPN (4 %) = −50,000 + 57,456.24 = +\$7,456.24 USD**
    - **TIR por interpolación:** r₁ = 4 % (+7,456.24) y r₂ = 10 % (−1,162.83): 4 % + 6 % × 7,456.24 / 8,619.07 = **9.19 %** (exacta: 9.10 %).
    - **Decisión: viable.** Los flujos crecen con el tiempo, así que el proyecto es sensible a la tasa: por encima de ~9.1 % deja de crear valor.

??? example "Ejercicio 6 — Maquinaria: \$1,000,000 USD; flujos de 300K / 350K / 375K / 300K + salvamento de 150K; tasa del 10 %"
    El valor de salvamento se suma al flujo del año 4: 300,000 + 150,000 = 450,000.

    | Año | Flujo | ÷ (1.10)^t | Valor presente |
    | :---: | ---: | ---: | ---: |
    | 1 | 300,000 | 1.1000 | 272,727.27 |
    | 2 | 350,000 | 1.2100 | 289,256.20 |
    | 3 | 375,000 | 1.3310 | 281,743.05 |
    | 4 | 450,000 | 1.4641 | 307,356.05 |
    | | | **Suma** | **1,151,082.58** |

    - **VPN (10 %) = −1,000,000 + 1,151,082.58 = +\$151,082.58 USD**
    - **TIR por interpolación:** r₁ = 10 % (+151,082.58) y r₂ = 20 % (−72,916.67): 10 % + 10 % × 151,082.58 / 223,999.25 = **16.74 %** (exacta: 16.35 %).
    - **Decisión: viable.** Sin el valor de salvamento, el VPN bajaría en 102,452 (150,000 / 1.4641) a +\$48,630: el salvamento aporta dos tercios del valor creado.

??? example "Ejercicio 7 — Proyecto X contra Y: \$50,000 cada uno, tasa del 8 %"
    | Año | Flujo X | VP de X | Flujo Y | VP de Y |
    | :---: | ---: | ---: | ---: | ---: |
    | 1 | 25,000 | 23,148.15 | 10,000 | 9,259.26 |
    | 2 | 25,000 | 21,433.47 | 20,000 | 17,146.78 |
    | 3 | 25,000 | 19,845.81 | 45,000 | 35,722.45 |
    | **Suma** | | **64,427.42** | | **62,128.49** |

    | | Proyecto X | Proyecto Y |
    | :--- | ---: | ---: |
    | **VPN (8 %)** | **+\$14,427.42** | +\$12,128.49 |
    | TIR por interpolación | 23.45 % (20 % y 25 %) | 18.31 % (15 % y 20 %) |
    | TIR exacta | 23.38 % | 18.22 % |

    - **Decisión: el proyecto X es más rentable.** Gana por VPN y por TIR. Los dos suman \$75,000 sin descontar, pero X recupera el dinero antes; por eso, a cualquier tasa mayor que 0 %, X vale más que Y.

??? example "Ejercicio 8 — Proyecto X (\$50,000; \$25,000 × 3 años) a distintas tasas"
    $$
    VPN = -50{,}000 + 25{,}000 \times \frac{1-(1+r)^{-3}}{r}
    $$

    | Tasa | Factor de anualidad | VPN | Decisión |
    | :---: | ---: | ---: | :--- |
    | 8 % | 2.5771 | **+\$14,427.42** | Aceptar |
    | 15 % | 2.2832 | **+\$7,080.63** | Aceptar |
    | 20 % | 2.1065 | **+\$2,662.04** | Aceptar, con poco margen |
    | 25 % | 1.9520 | **−\$1,200.00** | Rechazar |

    - **Cómo cambia la decisión:** el VPN cae conforme sube la tasa y cambia de signo en la TIR (23.38 %). Por debajo de esa tasa el proyecto se acepta; por encima, se rechaza.

??? example "Ejercicio 9 — Global Solutions: \$500,000 USD; flujos de 180K / 200K / 190K / 170K; costo de capital del 14 % (verificación de la solución de la clase)"
    | Año | Flujo | VP al 14 % | VP al 22 % |
    | :---: | ---: | ---: | ---: |
    | 1 | 180,000 | 157,894.74 | 147,540.98 |
    | 2 | 200,000 | 153,893.51 | 134,372.48 |
    | 3 | 190,000 | 128,244.59 | 104,634.31 |
    | 4 | 170,000 | 100,653.65 | 76,737.84 |
    | **VPN** | | **+\$40,686.48** | **−\$36,714.38** |

    - **TIR por interpolación:** 14 % + 8 % × 40,686.48 / 77,400.86 = **18.21 %** (exacta: 17.95 %).
    - **Decisión: viable**, porque la TIR (≈ 18 %) supera el costo de capital (14 %).
    - **Diferencias con la solución de la clase:** los años 3 y 4 al 14 % dan 128,244.59 y 100,653.65 (en clase, 128,384 y 100,560), así que el VPN al 14 % es +40,686 y no +40,732; al 22 %, −36,714 y no −36,560. La conclusión no cambia: la TIR interpolada sigue en ≈ 18.2 %.

**Lo que enseñan los seis ejercicios:**

- **La interpolación lineal sobrestima la TIR** en todos los casos (entre 0.01 y 0.4 puntos), porque la curva del VPN es convexa: la recta entre dos tasas queda por encima de la curva. Mientras más separadas estén r₁ y r₂, mayor el error (ejercicio 6, con 10 puntos de separación).
- **Un VPN positivo pequeño no es una decisión segura** (ejercicio 4): conviene mirarlo junto con la sensibilidad a la tasa (ejercicio 8).
- **Para Zaqora,** la TIR no existe en los 12 meses porque ningún flujo es positivo: no hay tasa que haga el VPN igual a cero. Por eso la viabilidad se juzga por el VPN (−\$2,681) y por lo que hace falta para volverlo positivo.

### 6. Pendientes del entregable

- [x] **Modelo económico:** costo unitario, precio cost-plus y value-based, punto de equilibrio, flujo de caja a 12 meses y VPN al 15 % (Paso 2).
- [x] **Costo mensual de la IA** por usuario activo (sección 3 y hoja «Costo IA»).
- [x] **Hoja de cálculo con fórmulas visibles** (sección 4).
- [x] **Precios del «BOM» confirmados** en las páginas oficiales (08/10/2026), con *hosting* en Cloudflare Pages.
- [x] **Palancas decididas:** el piloto incluye cuenta de Google Play; se busca una academia piloto desde el mes 7, sin *dashboard*.
- [ ] **Carta de intención de una academia** antes del mes 7, para pasar la licencia del escenario objetivo al base.
- [ ] **Evaluar Claude Haiku 5.5** como narrador: la misma escena con los dos modelos, comparando calidad del español y tono.
- [ ] **Prueba de disposición a pagar:** preventa o lista de espera con precio (\$59 MXN) entre los usuarios beta, antes de programar los pagos.
- [x] **Ejercicios 4–9** de la presentación (sección 5 y hoja «Ejercicios»).
---

## 5) Reflexión

- **Todos cobran igual, y eso no es una buena noticia.** Que el *freemium* con suscripción domine en ajedrez, idiomas y hábitos dice que es lo que funciona para retener, no que vaya a funcionar con un jugador que usa Lichess porque es gratis. El benchmark marca el piso; la disposición a pagar hay que medirla.
- **Mi precio de la semana 4 estaba fuera de mercado.** \$300 MXN al mes es más de lo que cobra Chess.com en México por su nivel más alto. Sin este benchmark lo habría llevado así al modelo económico.
- **El dónde se cobra pesa tanto como el cuánto.** La idea más útil de la semana no es un precio, sino una regla de diseño: no cobrar en el momento de la derrota. Es la misma lógica de «validar antes de corregir», aplicada al pago.
- **Un nuevo cliente puede cambiar el producto.** Poner a los entrenadores como fuente principal de ingresos parece atractivo, pero obligaría a diseñar un *dashboard* y misiones asignadas, y a dejar en segundo plano al jugador que pierde solo. Primero hay que validar con el usuario para el que se diseñó Zaqora.
- **El año 1 no es un negocio, es un experimento, y está bien.** El modelo del profesor da un VPN de −\$2,359 MXN: con 20 usuarios no hay precio que cierre. Lo que hay que presupuestar es una validación de unos \$2,500 MXN con una pregunta clara: ¿pagan al menos 2 de cada 20?
- **Un modelo financiero responde la pregunta que le haces.** Mi prompt reutilizó los supuestos de la semana 4 (\$300 al mes, 1,200 clientes, sueldos) y armó una startup que necesita \$1.0M MXN; el del profesor, con los datos de esta semana, armó un piloto de \$2,500. Ninguno está mal, pero mezclar los supuestos de dos semanas distintas sin revisarlos fue un error mío.
- **La IA no es el costo que temía.** Con Haiku, el narrador cuesta \$3.85 MXN por usuario al mes; lo caro es la infraestructura fija repartida entre pocos usuarios, y los usuarios gratuitos sin tope. La decisión de que el LLM solo narre (semana 5) es la que mantiene ese número bajo.
- **Verificar los precios cambió una decisión.** Al confirmar el BOM apareció Claude Haiku 5.5, unas 7.7 veces más barato por capítulo que el modelo que había elegido, y se descartó Vercel Hobby porque prohíbe el uso comercial. Ninguno de los dos hallazgos estaba en las respuestas de la IA.
- **Las cifras de una IA de búsqueda también hay que verificarlas.** Las dos rondas citan fuentes, pero algunos precios son de reseñas de terceros y cambian por región. Antes del modelo económico hay que confirmarlos en las páginas oficiales.

### Preguntas de cierre

| Pregunta | Respuesta |
| :--- | :--- |
| ¿Cuál es el costo unitario real del producto a 10 unidades? | \$18.83 MXN por usuario activo al mes a 10 usuarios (\$14.85 a 100), con overhead y contingencia. El 71 % del costo directo es infraestructura *cloud* fija. |
| ¿Qué modelo de ingresos eligieron y cuál es el desafío de diseño para que funcione? | *Freemium* B2C: capítulos gratis y suscripción ligera de \$59 MXN al mes o temporada de \$149. El desafío es la conversión: cobrar sin hacerlo justo después de una derrota, con un tope en el plan gratuito, y lograr que paguen al menos 2 de cada 20 usuarios. |
| ¿Cuánto cuesta mensualmente la IA por usuario activo? | ≈ \$3.85 MXN (US\$0.21) con Claude Haiku 4.5 y 20 capítulos al mes. Mi modelo a dos años, con un uso más intenso y colchón, lo pone en \$10 MXN. |
| ¿El VPN a 12 meses es positivo con números reales? | No: **−\$2,359 MXN** al 15 % en la respuesta de la IA y **−\$2,636 MXN** en la hoja de cálculo, donde los créditos de API se agotan en el mes 7. Solo se vuelve positivo (+\$2,736) si se suma una academia piloto desde el mes 7. El año 1 es una validación. |
