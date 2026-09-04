# Semana 2 — Búsqueda de Oportunidades

## 1) Resumen

- **Nombre de la actividad:** _Búsqueda y defensa de una oportunidad de negocio con apoyo de IA_
- **Curso:** _Proyecto de Ingeniería IV_
- **Equipo:** _David López Ramírez_
- **Fecha:** _03/09/2026_
- **Descripción breve:** _A partir de una idea inicial (una web de ajedrez con IA que enseña planes estratégicos), se recorrió un proceso de 7 pasos apoyado en IA generativa (**Perplexity** para investigación con fuentes y **Claude** para estrés, ideación y filtrado) hasta llegar a una oportunidad defendible y su reporte: **La Campaña (Modo Historia)**._

---

## 2) Punto de partida

**Idea original:** una página de ajedrez de entrenamiento personalizado con una IA que ayude a estudiar y entender los **planes** (planes, medio juego, finales).

- **Segmento inicial:** jugadores amateur / escuelas.
- **Dolor que se creía central:** «no saber qué estudiar para mejorar / no entender un tema».
- **Modelo:** app con IA + página web de venta. Capacidades del equipo: desarrollo de software e IA. Plazo: 6 meses a MVP comercializable.

---

## 3) Proceso — 7 pasos con IA

Cada paso combinó **Perplexity** (investigación con fuentes) y **Claude** (estrés crítico, ideación y filtrado). Abajo se incluyen los **prompts completos** y las **respuestas completas**; cada uno abre en su propio bloque desplegable. Los listados largos de URLs de fuentes se resumen como _«[listado de fuentes]»_ para facilitar la lectura.

### Paso 1 — Búsqueda de oportunidades en LATAM

**Herramientas:** Perplexity (mapeo del ecosistema) → Claude (estrés de inversionista).

??? quote "Prompt completo — Ronda 1 (Perplexity)"
    Actúa como un analista de inteligencia competitiva especializado en negocios de producto digital en América Latina, con experiencia en evaluar si una idea tiene espacio real en el mercado o si está entrando a un ecosistema ya saturado o con barreras no obvias. Tu metodología incluye análisis de actores existentes, detección de brechas no cubiertas, identificación de mercados adyacentes y evaluación de timing de mercado.

    Somos un equipo de emprendedores en México construyendo un negocio basado en dos componentes articulados: una aplicación con IA y una página web de venta. Nuestras capacidades abarcan desarrollo de software e IA. Tenemos seis meses para llegar a MVP comercializable.

    Nuestra idea actual es: una página de ajedrez de entrenamiento personalizado con una IA que ayude a estudiar y entender los planes (planes, medio juego, finales).

    Responde con datos verificables y fuentes:

    - **SATURACIÓN DEL ESPACIO:** ¿Quién más está atacando este problema en LATAM o en el mundo con soluciones que combinen software e IA? Menciona al menos 3 actores reales con su nivel de tracción actual.
    - **BRECHAS NO CUBIERTAS:** En el mismo espacio donde opera nuestra idea, ¿qué subproblemas o segmentos de usuario están siendo ignorados por los actores actuales? Dame 3 brechas concretas con evidencia de que son reales y de que representan disposición a pagar.
    - **MERCADOS ADYACENTES:** ¿Hay sectores o tipos de usuario donde una solución como la nuestra — app con IA + canal de venta digital — podría aplicarse con adaptaciones menores y donde el problema sea igual o más intenso?
    - **TIMING:** ¿Hay señales de que este mercado está listo para una solución integrada digital ahora? ¿Qué tendencia reciente lo indica o lo contradice?

??? abstract "Respuesta completa — Ronda 1 (Perplexity)"
    **Respuesta ejecutiva.** El espacio de entrenamiento de ajedrez con IA no está saturado, pero sí altamente consolidado en los segmentos de élite y principiantes. Los actores dominantes (Chess.com, Lichess, Chessify) compiten por usuarios globales con modelos freemium, pero dejan brechas estructurales en segmentos intermedios, mercados emergentes con pricing localizado y enfoques pedagógicos específicos (planes estratégicos, medio juego posicional). El timing es favorable: 2026 fue declarado el «Año del Ajedrez en la Educación» por FIDE, con políticas públicas activas en Latinoamérica que expanden la base de usuarios.

    **Saturación — actores existentes (software + IA):**

    | Actor | Modelo de IA | Tracción (2025-2026) | Pricing | Enfoque |
    |-------|--------------|----------------------|---------|---------|
    | Chess.com | Game Review con CAPS2, AI Coach integrado | 250M usuarios, $150M ingresos anuales (88% suscripciones) | $6.99–$49.99/año (Gold–Diamond) | Ecosistema todo-en-uno |
    | Lichess | Stockfish gratuito, análisis ilimitado | Plataforma gratuita más usada, sin modelo de pago | Gratis (donaciones) | Análisis gratuito, open data, puzzles |
    | Chessify | Cloud engine analysis, AI explanations | Competidor establecido en análisis en la nube | $12.99/mes | Análisis profundo con motores en la nube |
    | Aimchess | Analytics + drills personalizados según tus partidas | Conecta con Chess.com/Lichess; Pro $7.99/mes o $57.99/año | $7.99/mes | Diagnóstico de debilidades y entrenamiento focalizado |
    | Chessvia (Chessy) | AI coach conversacional con voz y chat | Early access con voz, $7–19/mes según tier | $7–19/mes | Coaching interactivo tipo «pregunta por qué» |
    | DecodeChess | Explicaciones de IA en lenguaje natural | 3 análisis gratis/día, Pro ~$10/mes | ~$10/mes, $80/año | Explicaciones de «por qué» funciona una jugada |

    Nivel de saturación: alto en el segmento global premium (Chess.com domina con 250M usuarios y $150M anuales). Sin embargo, ninguno tiene presencia significativa en LATAM con pricing localizado ni enfoque pedagógico en español para intermedios. Chess.com aplica regional pricing (Nigeria $0.67/mes vs Dinamarca $9.42/mes) pero sin estrategia específica para México/LATAM.

    **Brechas no cubiertas:**

    1. **Jugadores intermedios (1200-1800 Elo) que buscan entender planes, no solo tácticas.** Aimchess y DecodeChess se enfocan en análisis post-partida y explicaciones de jugadas individuales, pero no enseñan planificación estratégica a largo plazo; Chess.com Game Review da feedback por jugada (CAPS2) pero no construye un plan de estudio alrededor de debilidades de concepto. Adultos que juegan 20+ partidas/mes y pagan $7-10/mes por Aimchess se frustran porque la plataforma no les dice «qué estudiar esta semana». Disposición a pagar: Aimchess Pro convierte en $7-10/mes; Chessvia cobra $7-19/mes por coaching conversacional. _Oportunidad:_ una app que diagnostique el nivel de comprensión de planes (no solo precisión de jugadas) y genere un plan de 4-6 semanas con ejercicios de medio juego y finales posicionales.
    2. **Mercado LATAM con pricing localizado y contenido en español.** Chess.com aplica regional pricing global pero no hay evidencia de estrategia para México/LATAM. El mercado de instrucción de ajedrez online en México se estima en $150M (12% del mercado global LATAM), CAGR 7.5%; Brasil $120M, Argentina $100M. FIDE declaró 2026 el «Año del Ajedrez en la Educación» con pilotos en Costa Rica (10 escuelas públicas), Panamá (40 profesores entrenados) y Brasil (2,503 clubes escolares). Pricing óptimo en mercados emergentes ≈ 0.5-1% del ingreso mensual promedio → para México, $5-9 USD/mes. _Oportunidad:_ app con IA 100% en español, pricing PPP-adjusted ($5-8 USD/mes) y contenido alineado con programas escolares.
    3. **Enfoque pedagógico en «entender por qué» vs «qué jugada es mejor».** DecodeChess ofrece explicaciones en texto pero one-way y limitadas a posiciones específicas; Chessvia es conversacional pero general y en early access. Usuarios reportan que las explicaciones de motor son incomprensibles para intermedios («la evaluación es +0.7 pero no entiendo por qué»). Disposición a pagar: DecodeChess Pro $8.25/mes; Chessvia $7-19/mes; Dr. Wolf $49/año. _Oportunidad:_ IA que explique planes en lenguaje natural y permita preguntas tipo «¿por qué no puedo jugar f4 aquí?» con respuestas contextualizadas.

    **Mercados adyacentes:**

    1. **Educación escolar de ajedrez (B2B2C).** FIDE y gobiernos de LATAM invierten en ajedrez escolar (Costa Rica 10 escuelas, Brasil 2,503 clubes, Panamá 40 profesores). Los profesores no tienen herramientas para personalizar entre 30-40 alumnos ni plataforma de seguimiento. Adaptación: dashboard para profesores, contenido alineado con currículo FIDE «Chess in Education», pricing B2B por escuela/alumno.
    2. **Entrenamiento para otros juegos de estrategia (Go, Shogi, Xiangqi).** La arquitectura de IA para explicar planes es transferible; los motores (KataGo, Stockfish Shogi) dan evaluaciones pero no explican planes en lenguaje humano. Comunidades más pequeñas = menos competencia y menor TAM. Requiere entrenar modelo en bases de datos de Go/Shogi y validar TAM antes de invertir.
    3. **Coaching de IA para habilidades cognitivas (no ajedrez).** El ajedrez se usa como herramienta de desarrollo cognitivo en escuelas; la IA podría adaptarse a ejercicios de razonamiento lógico. El mercado de «brain training» está fragmentado y con escepticismo, pero el ajedrez tiene ventaja de credibilidad académica. Posicionar como «ajedrez para pensamiento crítico».

    **Timing — señales favorables:** 2026 = «Año del Ajedrez en la Educación» (FIDE), con presupuesto y pilotos en LATAM; mercado online LATAM $270M en 2026 → $686M en 2035 (CAGR 10.9%); madurez de la IA conversacional (Chessvia, DecodeChess, Dr. Wolf) y de los LLM; Chess.com se ralentiza en mercados desarrollados (crecimiento YoY 17.5%, pivota a ads). **Señales de riesgo:** Chess.com podría localizar pricing y features rápido (mitigación: nichos que ignora); baja penetración de tarjeta de crédito en México ~30% (mitigación: OXXO, Mercado Pago, SPEI); coaches humanos a $10-20/hora (mitigación: IA como complemento más económico).

    **Veredicto estratégico.** Saturado en el segmento global premium; espacio real en (a) intermedios 1200-1800 que buscan entender planes, (b) LATAM con pricing y contenido en español, (c) enfoque conversacional «pregunta por qué». Recomendación MVP 6 meses: nicho de jugadores 1400-1800 Elo en México, pricing $5-8 USD/mes ($90-150 MXN) con pagos OXXO/Mercado Pago, diferenciador de IA en español con preguntas conversacionales, y validación con pilotos escolares FIDE. _[listado de fuentes]_

??? quote "Prompt completo — Ronda 2 (Claude, estrés)"
    Actúa como un inversionista con experiencia en negocios de producto digital en mercados emergentes, conocido por hacer las preguntas que los equipos no quieren escuchar pero necesitan responder antes de comprometer seis meses en una idea. No eres destructivo — eres brutalmente honesto porque te importa que el negocio llegue a algo real y comercializable.

    Somos emprendedores en México. Nuestra idea es: una página de ajedrez de entrenamiento personalizado con una IA que ayude a estudiar y entender los planes (planes, medio juego, finales). Modelo de negocio: una aplicación con IA y una página web de venta. Capacidades: desarrollo de software e IA. Tenemos seis meses para llegar a MVP comercializable. _[Se adjunta el análisis de ecosistema del Paso 1.]_

    Hazme el estrés que más necesito — no el más cómodo:

    - **EL SUPUESTO MÁS PELIGROSO:** ¿Cuál es el supuesto sobre el usuario o el mercado que estamos dando por hecho y que, si resulta falso, hace que toda la idea pierda sentido? ¿Cómo lo probaríamos o refutaríamos en menos de una semana sin construir nada?
    - **LA ARISTA QUE NO VIMOS:** Basándote en las brechas del análisis de ecosistema, ¿hay una versión de nuestro negocio — cambiando el usuario objetivo, el problema atacado o cómo se articulan los componentes — que tenga un mercado más claro o una propuesta de valor más fuerte? Descríbela como pitch de 3 oraciones.
    - **EL PIVOTE MÍNIMO:** Si tuvieras que cambiar UNA sola cosa de nuestra idea para hacerla significativamente más fuerte, ¿qué cambiarías y por qué?

    Sé específico. No me des frameworks — dame decisiones accionables.

??? abstract "Respuesta completa — Ronda 2 (Claude, estrés)"
    Voy directo, sin suavizar.

    **1. El supuesto más peligroso.** No es «¿hay mercado en LATAM?» ni «¿la IA puede explicar ajedrez bien?». Es este: que los jugadores de 1200-1800 Elo que se estancan atribuyen su estancamiento a «no entender los planes estratégicos» y que ese dolor es lo suficientemente consciente y agudo como para sacar la tarjeta.

    En la realidad del ajedrez amateur, la mayoría de la gente que se estanca lo hace por blunders tácticos y falta de disciplina de estudio, no por falta de comprensión posicional — y cuando sienten frustración, lo que compran es «quiero dejar de perder piezas ya» (tácticas, puzzle rush, rating), no «quiero entender el medio juego profundamente» (que se siente como tarea escolar, no como alivio inmediato). Ni Aimchess ni DecodeChess, que su propio reporte cita como validación de willingness-to-pay, cobran específicamente por currícula de planes estratégicos — cobran por diagnóstico general y explicaciones puntuales. Están extrapolando de «la gente paga por coaching de IA en ajedrez» a «la gente pagará por ESTE ángulo específico», y son dos afirmaciones distintas.

    Segundo supuesto escondido: los tamaños de mercado LATAM ($150M México, CAGR 7.5%, desglose por país al punto decimal) vienen en parte de sitios como kingdomofchess.com e industryresearch.biz — patrón clásico de contenido generado por IA para posicionar en Google, no investigación verificada. Las fuentes de FIDE.com sí son primarias; el TAM no lo es.

    **Cómo refutarlo en menos de una semana sin construir nada:** no preguntar «¿pagarías por esto?». Hacer 15-20 conversaciones con jugadores 1200-1800 en México (grupos de Facebook «Ajedrez México», clubes, Discord de torneos) sobre comportamiento pasado: qué han pagado antes por ajedrez, cuánto, si lo terminaron, y qué buscaban. Si nadie pagó nunca por «entender planes» y todos pagaron por tácticas o Chess.com Diamond, el supuesto está muerto. En paralelo, una landing page en español con precio ancla real y ~$100-150 USD de tráfico pagado a México durante 5 días, midiendo compromiso de dinero real (un «aparta tu lugar con $50 MXN reembolsable» vía Mercado Pago), no clics ni emails. Y publicar el concepto crudo en r/chess y grupos mexicanos.

    **2. La arista que no vimos.** El propio análisis la señala y la entierra en «mercados adyacentes»: el hueco real no está en jugadores individuales compitiendo contra Chess.com gratis, está en los profesores de ajedrez escolar sin herramientas para personalizar entre 30-40 alumnos, justo cuando FIDE declaró 2026 «Año del Ajedrez en la Educación» con pilotos gubernamentales presupuestados en Costa Rica, Panamá y Brasil.

    _Pitch de 3 oraciones:_ Vendemos a escuelas, academias y federaciones de ajedrez en LATAM —no a jugadores individuales— una plataforma donde el profesor sube el progreso de sus 30-40 alumnos y la IA genera un diagnóstico por alumno y un plan de estudio semanal alineado al currículo FIDE «Chess in Education». El canal de venta es institucional: contactamos los pilotos gubernamentales ya en marcha y academias privadas, con licencias anuales por alumno en vez de suscripciones B2C peleando contra una app gratuita con 250M de usuarios. Esto convierte la «página de venta» en un caso de estudio con una escuela piloto real, no en un funnel genérico de $8/mes.

    **3. El pivote mínimo.** Cambiaría el cliente objetivo: de jugador individual que se autopaga (B2C) a profesor/escuela/federación que compra institucionalmente (B2B2C), manteniendo la app y el motor de IA intactos. La matemática de adquisición cambia radicalmente (necesitan ~850 suscriptores a $8/mes para $80,000 MXN/mes vs 5-8 escuelas con licencias anuales de $30-50k MXN); resuelve el problema de payment friction (instituciones pagan por factura o transferencia); y los saca de la colisión directa con Chess.com. Costo honesto: los ciclos de venta institucional en LATAM son de 2-4 meses; «6 meses a MVP comercializable» con contratos firmados es optimista — mejor conseguir 2-3 escuelas piloto gratis en el mes 2-3, generar el caso de estudio, y cerrar contratos pagados en el mes 5-6.

**Resultado clave:** el foco se mueve del «no entender planes» hacia el dolor de **perder partidas** y la **exclusión social**, y aparece la arista **B2B2C escolar** como alternativa.

### Paso 2 — Síntesis de _insights_

**Herramientas:** Claude (formular y auditar el insight implícito) → Perplexity (verificar los dos insights con fuentes citables).

??? quote "Prompt completo — Ronda 1 (Claude)"
    Actúa como un estratega de producto con experiencia en identificar los supuestos ocultos detrás de ideas de negocio — los insights implícitos que los equipos dan por ciertos sin haberlos formulado ni verificado. Tu especialidad es hacer visible lo que se asume como obvio, porque ahí es donde más frecuentemente fallan los negocios de software en mercados emergentes.

    Somos un equipo de emprendedores en México con una idea que combina una aplicación con IA y una página web de venta. Capacidades: desarrollo de software e IA. Seis meses para MVP. Nuestra idea: una página de ajedrez de entrenamiento personalizado con una IA que ayude a estudiar y entender los planes (planes, medio juego, finales). _[Se adjuntan las brechas del Paso 1 y el estrés del inversionista.]_

    Necesito que hagas tres cosas:

    1. **FORMULA EL INSIGHT IMPLÍCITO:** ¿Cuál es el insight sobre el usuario y el problema que nuestro equipo está dando por cierto sin haberlo verificado? Exprésalo en el formato de un insight sólido: quién, qué les cuesta, por qué no está resuelto, dónde está el espacio. No parafrasees nuestra idea — formula el supuesto que la sostiene.
    2. **AUDITA EL INSIGHT:** ¿Qué parte tiene más probabilidad de ser falsa o más débil de lo que asumimos? ¿Qué evidencia necesitaríamos para saber si es verdadera? ¿Hay una versión alternativa del insight — mismo problema, diferente usuario, o mismo usuario, diferente problema — que podría ser más sólida?
    3. **FORMULA EL INSIGHT DE LA ARISTA NUEVA:** Usando la arista alternativa del Paso 1, formula un segundo insight con el mismo formato y explica cómo se articularían app, artefacto y canal de venta alrededor de esa arista.

??? abstract "Respuesta completa — Ronda 1 (Claude)"
    **1. El insight implícito que están dando por cierto.**

    - **Quién:** jugadores adultos amateur en México, Elo 1200-1800 en partidas rápidas/blitz online, que juegan 20+ partidas/mes y ya pagan por alguna herramienta de ajedrez (Chess.com Diamond, Aimchess, un curso suelto).
    - **Qué les cuesta:** llevan tiempo estancados en su rating y —este es el punto que asumen sin haberlo escuchado de nadie— atribuyen conscientemente ese estancamiento a «no entiendo los planes estratégicos»: no saben qué hacer tras la apertura, cómo transicionar al medio juego, cómo jugar un final posicional.
    - **Por qué no está resuelto:** las herramientas que usan (Game Review, Aimchess, DecodeChess) dan feedback jugada-por-jugada o post-mortem de una partida, pero ninguna construye una currícula progresiva alrededor de conceptos ni les dice «esto te toca estudiar esta semana».
    - **Dónde está el espacio:** un producto que diagnostica nivel de comprensión conceptual (no solo precisión táctica) y genera un plan de 4-6 semanas con ejercicios de medio juego y finales.

    Este insight no es «hay demanda de coaching de ajedrez con IA» (eso sí está evidenciado). Es la capa de abajo, menos probada: que la causa que la gente se atribuye para su estancamiento es comprensión de planes, y que ese diagnóstico —no el síntoma— es lo que pagarían por resolver.

    **2. Auditoría del insight.** La parte con más probabilidad de ser falsa es la atribución causal. La mayoría de jugadores 1200-1800 se estanca por blunders tácticos, gestión del reloj y falta de disciplina — no por déficit posicional. Y el efecto Dunning-Kruger es fuerte en ajedrez amateur: «no entender el plan» es una explicación más halagadora y difícil de auto-diagnosticar que «se me fue la pieza». Aunque el diagnóstico correcto sea «planes», el usuario no lo siente como dolor agudo — se siente como tarea, no como alivio, y las compras de hobby por frustración van detrás del alivio inmediato. Segunda debilidad: Aimchess, DecodeChess y Chessvia validan que se paga por coaching de IA en general, no por currícula de planes estratégicos.

    _Evidencia necesaria:_ no preguntas de intención, sino comportamiento pasado y lenguaje espontáneo — pedir que describan, sin ayuda, la última vez que sintieron que no progresaban y dejar que ellos nombren la causa; minería de lenguaje en comunidades reales (contar «blunder/táctica/tiempo» vs «plan/estrategia»); test A/B de landing con dos pitches («deja de regalar piezas» vs «entiende por qué pierdes») al mismo tráfico, midiendo compromiso de dinero real.

    _Versión alternativa más sólida:_ mismo usuario, problema distinto — el dolor no es «no entiendo los planes» sino «no tengo estructura ni constancia para estudiar». Cambia el producto de «motor que explica conceptos» a «coach de hábito con accountability» (más Duolingo que libro de texto). Es más sólida porque explica por qué retendría suscripciones: la comprensión conceptual se agota; el hábito de estudio es recurrente.

    **3. El insight de la arista institucional.**

    - **Quién:** profesores y coordinadores de ajedrez escolar en escuelas públicas, academias privadas y programas federativos de LATAM (México, y los pilotos activos en Costa Rica, Panamá y Brasil bajo FIDE «Chess in Education 2026»), que manejan grupos de 20-40 alumnos de nivel heterogéneo.
    - **Qué les cuesta:** no tienen forma escalable de personalizar el entrenamiento; con 30-40 niños no pueden diagnosticar la debilidad de cada uno ni generar un plan diferenciado, y no tienen cómo mostrar a la escuela o al programa gubernamental evidencia de progreso individual que justifique el financiamiento.
    - **Por qué no está resuelto:** Chess.com, Lichess y ChessKid están diseñados para el jugador individual, no para la gestión de un salón — no producen reportes por alumno ni currícula alineada a un estándar educativo, y nadie ha construido la capa de «panel de profesor».
    - **Dónde está el espacio:** una plataforma donde el profesor conecta el avance de sus alumnos y la IA genera, por cada uno, diagnóstico y plan semanal, más un reporte agregado de aula para mostrar hacia arriba — vendida como licencia anual por alumno/escuela.

    _Cómo se reacomodan los componentes:_ la app es el mismo motor de IA, con una capa que pasa de «perfil de un jugador» a «panel de un profesor con 30-40 perfiles + reporte agregado»; el artefacto de venta deja de ser una landing de suscripción y se vuelve un caso de estudio (escuela piloto real, testimonio del coordinador, costo por alumno vs clases particulares, CTA «agenda una demo»); el canal deja de ser tráfico pagado hacia un checkout y se vuelve venta directa a los programas piloto ya identificados y presupuestados — lo que resuelve la baja penetración de tarjeta (pagan por factura) y la competencia frontal con Chess.com. _Tensión:_ los ciclos de venta institucional en LATAM no caben en un MVP de 6 meses; lo realista es usar el MVP individual como motor técnico y contenido de prueba que sostenga la conversación con la primera escuela.

??? quote "Prompt completo — Ronda 2 (Perplexity, verificación A vs B)"
    Actúa como un analista de inteligencia competitiva con experiencia en evaluar la solidez de oportunidades de negocio digital en mercados emergentes latinoamericanos. Tu metodología: contrastar las afirmaciones de una oportunidad con datos verificables de fuentes primarias y secundarias — INEGI, BID, CEPAL, reportes de industria, bases de datos de comportamiento de mercado.

    Somos emprendedores en México con dos direcciones posibles y necesitamos datos reales para elegir la más sólida, no la más atractiva en papel.

    - **INSIGHT A (idea original):** jugadores adultos amateur en México, Elo 1200-1800, 20+ partidas/mes, que ya pagan por herramientas de ajedrez y atribuyen su estancamiento a «no entiendo los planes estratégicos»; el espacio es un producto que diagnostica comprensión conceptual y genera un plan de 4-6 semanas.
    - **INSIGHT B (arista):** profesores y coordinadores de ajedrez escolar en LATAM (pilotos FIDE 2026 en Costa Rica, Panamá, Brasil) que manejan 20-40 alumnos y no pueden personalizar ni reportar progreso; el espacio es una plataforma con panel de profesor + reporte agregado, licencia anual por alumno.

    Para cada insight, verifica con fuentes citables: **existencia y tamaño del segmento**, **costo real del problema** (pagos observables, costos de workarounds), **competencia específica** (usuario + problema + solución digital exacta), y **señal de mercado más fuerte** (pagos actuales, búsquedas, comunidades, intentos previos con tracción). Al terminar entrega una tabla comparativa con ✅/⚠️/❌ para: segmento verificado, costo documentado, competencia mapeada, señal de mercado. No me digas cuál elegir — dame los datos.

??? abstract "Respuesta completa — Ronda 2 (Perplexity, verificación A vs B)"
    **INSIGHT A — Jugadores adultos amateur (Elo 1200-1800).**

    - _Existencia y tamaño:_ el perfil existe, pero el tamaño en México es menor de lo que parece. Chess.com ~250M usuarios globales, ~2M suscriptores pagantes (>50% en Diamond, $119/año). Distribución de rating: 85%+ <1000, ~13% 1000-1600, ~1.3% 1600+. Jugadores con rating FIDE en México: 65,164 (agosto 2026). Cálculo: si México es ~2-3% del tráfico global de Chess.com → 40,000-75,000 usuarios, de los cuales ~13-15% caen en 1200-1800: **5,000-11,000 jugadores potenciales**, y solo una fracción paga por herramientas. Penetración de tarjeta de crédito en México: 14.2% (2024, World Bank Findex); cualquier tarjeta (débito+crédito): 70.7%. _Veredicto: el segmento existe pero es pequeño y disperso en México; no hay dato directo de «jugadores 1200-1800 que ya pagan por herramientas» en México._
    - _Costo real:_ hay pagos observables (Aimchess $7.99/mes o $57.99/año; DecodeChess ~$7/mes; Chess.com Diamond $119/año; clases particulares en México $200-220 MXN/hora; coaches internacionales $35-50 USD/hora). Limitaciones documentadas públicamente: Aimchess «describe síntomas, no causas»; DecodeChess «es single-game por diseño, no hay vista agregada»; Game Review «no hay vista de debilidad agregada, no hay arquetipo, no hay plan de entrenamiento». _Veredicto: costo parcialmente documentado; la afirmación de que la causa auto-atribuida es «comprensión de planes» es una inferencia sin respaldo directo._
    - _Competencia:_ Aimchess, DecodeChess, Chess.com Game Review, ChessMentor AI/Noctie/Chessvia (€8-14/mes), MyChessPlan (análisis de 100 juegos + plan de 30 días, $14.99 por plan, lo más cercano pero de pago único). _Veredicto ⚠️: competencia mapeada, pero el espacio «currícula progresiva de 4-6 semanas con diagnóstico conceptual» está abierto._
    - _Señal de mercado:_ crecimiento del mercado de instrucción online ($270.37M en 2025 → $686.04M en 2035, CAGR 10.9%); >60% de plataformas integran análisis AI-driven; comunidades activas (r/chess, foros). _Veredicto: señal moderada — hay crecimiento y disposición a pagar, pero no evidencia de demanda específica por «diagnóstico conceptual + currícula de 4-6 semanas»._

    **INSIGHT B — Profesores y coordinadores de ajedrez escolar (LATAM).**

    - _Existencia y tamaño:_ verificado con iniciativas gubernamentales y de FIDE. Costa Rica: piloto nacional en 10 escuelas públicas con 25 profesores entrenados (abril 2026); Ley N.º 10187 (2022) establece el ajedrez en escuelas públicas como interés nacional. Grupos de 20-40 alumnos por profesor son típicos. Lichess reporta ~10,000 teachers y ~300,000 students globalmente. México: no hay dato de pilotos gubernamentales de ajedrez escolar en las fuentes revisadas. _Veredicto ✅: el segmento existe y está verificado con pilotos activos en 2026; tamaño inicial pequeño (cientos de alumnos en Costa Rica), con intención de escalar._
    - _Costo real:_ el problema está implícito en el diseño de las herramientas (ChessKid Enterprise tiene «Group Kids Tab» pero sin diagnósticos individuales; Lichess Class permite homework pero no reportes agregados de aula; ChessPlay.io $99/mes flat para academias). No hay dato de «presupuesto por alumno» ni «pérdidas reportadas» en los pilotos FIDE. _Veredicto ⚠️: costo parcialmente documentado; sin presupuesto asignado ni pérdidas cuantificadas._
    - _Competencia:_ ChessKid Enterprise, Lichess Class (free), Chess.com Classroom (live teaching room, no gradebook), Chessido, Chess Nexus (free ≤30 estudiantes), ChessPlay.io ($99/mes). _Veredicto ⚠️: hueco verificable en «panel de profesor con diagnóstico individual + reporte agregado para dirección/ministerio/federación»._
    - _Señal de mercado:_ pilotos gubernamentales activos con respaldo de FIDE, CCA y ministerios; memorándum firmado en Costa Rica; plan de escalar nationwide si la evaluación es exitosa; «Educational integration» como driver del mercado global. _Veredicto ✅ en intención política, pero temprana en ejecución comercial — hay voluntad institucional pero no pagos observables todavía._

    **Tabla comparativa final:**

    | Criterio | Insight A | Insight B |
    |----------|:---:|:---:|
    | Segmento verificado | ⚠️ (pequeño y disperso en México) | ✅ (pilotos gubernamentales activos 2026) |
    | Costo documentado | ⚠️ (pagos $5-12/mes; sin dato de causa «planes») | ⚠️ (limitaciones documentadas; sin presupuesto asignado) |
    | Competencia mapeada | ⚠️ (hueco en currícula de 4-6 semanas) | ⚠️ (hueco en panel de profesor + reporte agregado) |
    | Señal de mercado | ⚠️ (crecimiento genérico, sin demanda específica) | ✅ (pilotos gubernamentales con respaldo FIDE) |

    _Observaciones:_ riesgo de penetración de tarjeta en Insight A (14.2% de adultos con tarjeta de crédito → el checkout individual puede ser cuello de botella); riesgo de ciclos de venta institucional de 12-24 meses en Insight B; ambos comparten el mismo motor de IA, lo que permite una estrategia secuencial (MVP individual → capa institucional). **Decisión provisional del equipo: Insight B.** _[listado de fuentes]_

**Resultado clave:** el insight original queda marcado como **débil en su atribución causal**; se identifica una versión alternativa (hábito de estudio) y la arista B2B2C, más sólida en señal de mercado.

### Paso 3 — Pain-Gain Map

**Herramientas:** mapa propio del equipo (Ronda 1) → Claude (auditoría sin piedad) → Perplexity (mercado de la arista).

??? note "Ronda 1 — Pain-Gain Map del equipo (borrador)"
    **Usuario / segmento:** jugadores amateur / escuelas de ajedrez.

    | Dolores (Pains) | Ganancias (Gains) |
    |-----------------|-------------------|
    | D1. Soberbia de los jugadores más experimentados ❌ | G1. Plan personalizado para cada jugador de acuerdo con sus partidas |
    | D2. No saber qué estudiar para mejorar o no entender un tema ✅ | G2. Explicaciones de temas (apertura, medio juego y finales) y posiciones |
    | D3. Perder muchas partidas ⚠️ | G3. Accesibilidad del idioma |

    **El espacio sin cubrir (versión del equipo):** el dolor más intenso es «no saber qué estudiar / no entender un tema»; la ganancia más deseada es «explicaciones de temas y posiciones». Frase: _«Existe una oportunidad para los jugadores amateur que necesitan ayuda en el entendimiento de las posiciones de ajedrez porque hoy es frustrante únicamente memorizar jugadas.»_

??? quote "Prompt completo — Ronda 2 (Claude, auditoría del mapa)"
    Actúa como un consultor de estrategia de producto con experiencia en identificar desalineaciones entre lo que un equipo cree que resuelve y lo que el usuario realmente necesita. Tu especialidad es el análisis de Pain-Gain Maps para detectar si una solución está atacando los dolores correctos o si existe una oportunidad más poderosa en los dolores que la solución ignora.

    Somos emprendedores en México con una idea que combina una aplicación con IA y una página web de venta. Construimos un Pain-Gain Map y auditamos qué dolores resuelve nuestra idea. Analízalo sin piedad.

    Nuestra idea: una página de ajedrez de entrenamiento personalizado con una IA que ayude a estudiar y entender los planes (planes, medio juego, finales).

    - **DOLORES:** soberbia de los jugadores más experimentados ❌ · no saber qué estudiar / no entender un tema ✅ · perder muchas partidas ⚠️
    - **GANANCIAS:** plan personalizado según sus partidas · explicaciones de temas y posiciones · accesibilidad del idioma

    Realiza tres análisis: **DESALINEACIÓN CRÍTICA** (¿hay algún dolor ❌ o ⚠️ más intenso o frecuente que el que resolvemos con ✅? ¿Atacamos el dolor correcto o el más conveniente?); **ARISTA DE NEGOCIO NO VISTA** (describe una versión alternativa que ataque esos dolores, cómo cambiarían los dos componentes, y formula la arista como oportunidad en una oración); **GANANCIAS NO ENTREGADAS** (cuál entrega peor la solución actual y cómo rediseñar un componente para entregarla mejor). Termina con una decisión recomendada: continuar / explorar la arista en paralelo / considerar pivote.

??? abstract "Respuesta completa — Ronda 2 (Claude, auditoría del mapa)"
    **Pain-Gain Map auditado.** Usuario: jugador amateur adulto en México/LATAM, rating ~1200-1800 en rápidas/blitz online, juega con regularidad y ya gasta dinero en mejorar.

    - **Dolores (por intensidad):** ⭐ D1 Perder muchas partidas → ⚠️ · D2 No saber qué estudiar / no entender un tema → ✅ · D3 Soberbia de los jugadores más experimentados → ❌
    - **Ganancias (por deseo):** ⭐ G1 Plan personalizado según sus partidas → entregada: parcial · G2 Explicaciones de apertura, medio juego, finales y posiciones → bien · G3 Accesibilidad del idioma → bien

    **Desalineación crítica: parcialmente.** D1 (perder partidas) es el dolor más frecuente e inmediato —duele cada partida— y la solución solo lo toca de forma indirecta y lenta (⚠️). El dolor que sí resuelven de lleno (D2) es una causa que el propio jugador se atribuye, pero en 1200-1800 se pierde sobre todo por blunders tácticos y mal manejo del reloj, no por falta de comprensión estratégica: es un diagnóstico halagador, fácil de auto-reportar, y el más cómodo de construir con un LLM (explicar conceptos es barato; diagnosticar el patrón real de derrota requiere analizar partidas de verdad). Están resolviendo el dolor conveniente para el producto, no el más urgente para el usuario.

    **Arista de negocio identificada:** _«Existe una oportunidad adicional para el jugador que pierde partida tras partida y además se siente menospreciado o intimidado cada vez que busca ayuda de alguien más fuerte, porque hoy el aprendizaje de ajedrez viene empaquetado con jerarquía y soberbia (clubes, foros, coaches humanos) o con feedback frío de motor — y nuestra solución actual, centrada en enseñar planes estratégicos, no cubre ni el alivio inmediato de dejar de perder ni la necesidad de un espacio sin juicio para preguntar.»_ La app dejaría de ser un tutor conceptual y pasaría a ser un «revisor de partida» que, justo tras cada derrota, señala en tono cálido y sin tecnicismos el error concreto y corregible (blunder, tiempo, patrón repetido). La página de venta cambiaría de un mensaje educativo a uno emocional/comunitario («aquí nadie te va a hacer sentir tonto por preguntar»), con testimonios y captura del usuario justo después de una derrota.

    **Ganancia peor entregada: G1**, el plan «de acuerdo con sus partidas». Tal como está, la idea corre el riesgo de ser contenido genérico mapeado por Elo, no un diagnóstico real del historial. Para entregarla de verdad, la app necesita ingerir el PGN real del usuario (API de Chess.com/Lichess) y clasificar sus errores recurrentes —blunder táctico, apuro de tiempo, error posicional— antes de asignar contenido.

    **Decisión recomendada: [x] Explorar la arista en paralelo — ambas tienen potencial.** El dolor de perder partidas y el dolor social de la soberbia son suficientemente distintos de «no sé qué estudiar» como para probarlos en paralelo (dos framings de landing) antes de apostar todo el roadmap a la currícula de planes.

??? quote "Prompt completo — Ronda 3 (Perplexity, mercado de la arista)"
    Actúa como un analista de mercado con experiencia en evaluar el potencial comercial de oportunidades específicas en América Latina. Tu trabajo no es vender la idea — es decirle al emprendedor si el dolor tiene mercado suficiente para justificar construir alrededor de él.

    Nuestra idea actual resuelve «no saber qué estudiar / no entender un tema», para el jugador amateur adulto en México/LATAM (rating ~1200-1800, juega con regularidad, ya gasta dinero en mejorar). La arista que evaluamos ataca «perder muchas partidas». Oportunidad formulada: _[la arista del menosprecio y el espacio sin juicio]._

    Verifica con datos reales y entrega en este formato: **TAMAÑO DEL SEGMENTO** (¿cuántos usuarios en México/LATAM tienen este problema con frecuencia semanal o mayor? dato + fuente + confiabilidad), **EVIDENCIA DE DISPOSICIÓN A PAGAR** (pagos actuales, búsquedas, comunidades, intentos previos; veredicto clara/parcial/no encontrada), **COMPETENCIA EN ESTE ESPACIO ESPECÍFICO** (¿alguien ataca exactamente usuario + dolor + solución digital? actores reales con tracción; brecha sí/no/parcial) y **CONCLUSIÓN** (una oración: ¿tiene mercado suficiente para explorarla? sí / con condiciones / no, y por qué).

??? abstract "Respuesta completa — Ronda 3 (Perplexity, mercado de la arista)"
    **Tamaño del segmento.** ~1.2–1.8 millones de jugadores activos semanales en México y LATAM con rating 1200–1800 que juegan blitz/rapid online con regularidad (dato estimado, derivado de proxies: tráfico web por país + membresías globales + distribución de rating típica). Desglose: Chess.com ~268.6M miembros globales (julio 2026); LATAM ~9% de la base → ~24M miembros; rating 1200–1800 ≈ 40–50% de jugadores activos adultos; activos semanales ≈ 15–25% de registrados → segmento LATAM ≈ **2.2 millones**; México ≈ **0.5–0.8 millones** (estimación conservadora).

    **Evidencia de disposición a pagar: clara.** Chess.com ~1.5M suscriptores pagos globales, con pricing regional (Gold $0.67–$9.42/mes; LATAM $2–5/mes estimado); 85% de nuevos registros vienen de fuera de EE.UU. Mercado global de instrucción online $270M (2026), CAGR ~13%. Coaches con tracción: CircleChess, Russian Chess School ($49/mes), independientes ($20–150/hora); en México, Superprof.mx promedia $220 MXN/hora (97% satisfacción); AmazingTalker.mx desde $81 MXN por sesión de prueba. Foros: r/chess con hilos recurrentes de alta participación sobre «dread analysing losses», «traumatizing losses», «overcome tilting». Apps de AI coach: ChessLine (1k+ descargas, foco 1400–1800 Elo), IQChess, Chess Academy Pro, ChessMind AI ($7.99–$79.99/año); Outpost ~100,000 jugadores.

    **Competencia en este espacio específico:**

    | Plataforma | Enfoque | ¿Cubre «perder + juicio»? | Precio |
    |------------|---------|:---:|--------|
    | Chess.com Diamond | Análisis con motor + lecciones | Parcial (feedback frío, sin componente emocional) | $12.50/mes |
    | Sensei Chess | AI game analysis free | No (técnico, sin soporte emocional) | Gratis |
    | ChessMind AI | Diagnóstico de errores + plan personalizado | Parcial (weak skills, no experiencia subjetiva) | Freemium |
    | Chessiro | Explica errores en lenguaje simple + puzzles | Parcial (mejora comunicación, no aborda intimidación) | Gratis |
    | CircleChess | GM coaching + AI coach + psicología del ajedrez | Sí explícitamente («chess psychology integration») | $2–3/hora grupo |
    | Lichess | Análisis free + comunidad | No (comunidad puede ser jerárquica) | Gratis |

    Brecha confirmada: **parcial.** Ninguna plataforma posiciona explícitamente «espacio sin juicio para preguntar» como feature central; CircleChess es lo más cercano pero su foco es scholastic/kids y mercado US; las apps de AI coach resuelven el «qué estudiar» pero no el «me siento menospreciado al preguntar»; los foros son reactivos, no producto estructurado.

    **Conclusión para el equipo:** _sí, con condiciones_ — la arista tiene mercado suficiente si se posiciona como capa emocional/psicológica complementaria (no reemplazo del análisis técnico), apuntando a jugadores 1200–1800 en LATAM que ya pagan pero reportan frustración no resuelta; el riesgo es que el dolor sea real pero la disposición a pagar adicional por «sin juicio» sea baja si no se empaqueta con mejora medible de rating. _[listado de fuentes]_

**Resultado clave:** el Pain-Gain Map auditado reordena los dolores (⭐ D1 = perder partidas) y decide **explorar la arista en paralelo**.

### Paso 4 — SCAMPER + Remix de ideas

**Herramienta:** Claude en tres rondas (SCAMPER disruptivo → remix → filtro DVN).

??? note "Ronda 0 — SCAMPER inicial del equipo"
    | Letra | Idea original | Arista |
    |-------|---------------|--------|
    | Sustituir | Sustituir el LLM por una IA existente que explique las jugadas | El factor psicológico, por una IA amigable con refuerzo positivo |
    | Combinar | Conectarse a Lichess para apoyarse en su base de datos | Conectarse con una IA existente |
    | Adaptar | Adaptar la app/página para colegios, escuelas e individuos | Sistema progresivo con recompensas (como un videojuego) |
    | Modificar | Usar recursos y APIs gratuitos para la página | Que el estudio sea completamente un juego, no una app de estudio |
    | Poner en uso | Ya existen Lichess y Chess.com, que dominan | (igual) |
    | Eliminar | Centrarse en aprender con jugadores que te inspiran | Quitar el juego en línea y la clasificación; solo el progreso propio sin compararse |
    | Reordenar | Conectar tu perfil con Chess.com/Lichess y usar tus partidas para inspirar a otros | El usuario seguiría jugando aunque el proceso se reordene |

??? quote "Prompt completo — Ronda 1 (Claude, SCAMPER disruptivo)"
    Actúa como un facilitador senior de innovación disruptiva especializado en encontrar las versiones más radicales de ideas de negocio existentes — no mejoras incrementales, sino reencuadres que cambian quién se beneficia, cómo se entrega el valor, o por qué alguien pagaría. Tu metodología es SCAMPER aplicado con sesgo hacia la disrupción: para cada letra produces dos ideas exploración que desafían un supuesto central de la idea original (2–3 oraciones cada una).

    Somos emprendedores en México con un negocio de una aplicación con IA y una página web de venta. Capacidades: desarrollo de software e IA. Seis meses para MVP.

    - **Idea original:** una página de ajedrez de entrenamiento personalizado con una IA que ayude a estudiar y entender los planes (planes, medio juego, finales). Usuario: jugadores amateur / escuelas. Dolor ⭐: no saber qué estudiar / no entender un tema. Ganancia ⭐: plan personalizado según sus partidas.
    - **Supuestos centrales que nadie ha cuestionado:** que el usuario ocupará la app para aprender y se le quitará la frustración; que las explicaciones de posiciones y ejercicios lo harán mejorar.
    - **Arista de negocio:** existe una oportunidad adicional para el jugador que pierde partida tras partida y además se siente menospreciado o intimidado al buscar ayuda de alguien más fuerte, porque hoy el aprendizaje viene con jerarquía y soberbia o con feedback frío de motor — y nuestra solución no cubre ni el alivio inmediato ni el espacio sin juicio. Dolor que atacaría: perder muchas partidas.

    Aplica SCAMPER buscando las versiones más disruptivas. Para cada letra genera 2 ideas exploración. Criterio: si el resultado es «mejorar» la idea original, no fue suficientemente disruptivo. Guía por letra: **S** sustituir un supuesto central por algo inesperado; **C** fusionar un componente con la arista o con algo del entorno del usuario que la idea ignora; **A** adoptar un modelo de negocio de otro sector/país que resuelva un problema similar de forma radicalmente distinta; **M** llevar un atributo al límite absoluto; **P** otro segmento de usuario con el mismo problema pero más urgente o con más capacidad de pago; **E** eliminar algo dado por obligatorio y que el valor central sobreviva o mejore; **R** invertir quién detecta el problema, quién actúa, quién paga, o cuándo ocurre la intervención.

    FORMATO DE SALIDA: para cada letra, «Idea X1» y «Idea X2» con descripción de 2–3 oraciones y una línea de «Supuesto que rompe / Con qué se combina / Origen de la lógica / Atributo llevado al límite / Segmento alternativo / Qué se elimina / Qué se invierte».

??? abstract "Respuesta completa — Ronda 1 (Claude, SCAMPER disruptivo)"
    **Idea base:** ajedrez personalizado con IA (planes, medio juego, finales).

    **S — Sustituir.**

    - _S1:_ la IA deja de ser correctora y se convierte en «anti-coach»: nunca señala el error técnico, solo entrega tras cada derrota una narrativa creíble que protege el ego («tuviste una posición ganadora hasta el movimiento 30», «el rival jugó una línea rara de memoria»). El producto no mejora el nivel de juego, mejora cómo se siente el jugador al recordar la partida. _Rompe:_ que la corrección honesta es lo que el usuario necesita.
    - _S2:_ el usuario deja de ser el jugador que pierde y pasa a ser el jugador fuerte: la IA le enseña a ganar sin humillar y certifica a esos jugadores como «rival amable» verificado, que la escuela o el club puede promocionar. _Rompe:_ que quien debe pagar y usar la app es la víctima de la humillación.

    **C — Combinar.**

    - _C1:_ la web de venta se combina con un mercado de revanchas: el jugador que perdió no compra una lección, compra una «segunda oportunidad» contra el mismo rival con un hándicap calculado por IA para que el resultado sea incierto de nuevo. Se vende el momento de la revancha, no el aprendizaje. _Con qué se combina:_ la arista del menosprecio + el impulso de desquite del entorno del jugador.
    - _C2:_ la app deja de vivir en una app propia y se combina con el grupo de WhatsApp del club o escuela donde ocurre la burla: un bot IA intercepta y suaviza los comentarios sarcásticos del chat antes de que el jugador los vea. Protección emocional como función de mensajería, no de entrenamiento. _Con qué se combina:_ el entorno social real donde sucede la humillación.

    **A — Adaptar.**

    - _A1:_ lógica de rating bidireccional de plataformas gig (Uber/Airbnb): un mercado de coaches y rivales con reputación pública de «trato humano», no solo de fuerza de juego — un jugador fuerte con mala reputación de trato pierde acceso aunque gane todo. _Origen:_ economía de plataformas con calificación bilateral, EE.UU.
    - _A2:_ lógica del hándicap de golf: en vez de un ELO competitivo expuesto, cada jugador recibe un ajuste dinámico que le permite «ganar» legítimamente contra cualquiera. El producto central pasa a ser el motor de emparejamiento con hándicap. _Origen:_ sistema de hándicap de golf, clubes de EE.UU./Reino Unido.

    **M — Modificar al extremo.**

    - _M1:_ anonimato al límite absoluto: no existen perfiles ni historial visible, ni para el propio usuario — cada sesión se «olvida» institucionalmente, como un modo incógnito permanente. _Atributo al límite:_ anonimato → de opcional a arquitectura obligatoria.
    - _M2:_ precio al extremo: gratis para siempre para el jugador que pierde, financiado por el lado fuerte del mercado (clubes, coaches, jugadores ganadores que pagan una «tarifa de cortesía» por jugar contra alguien en racha de derrotas). _Atributo al límite:_ precio → gratuito absoluto para la víctima, subsidiado por el lado dominante.

    **P — Poner en otro uso.**

    - _P1:_ psicólogos y ludoterapeutas que usan juegos como herramienta clínica: el producto se reempaqueta como instrumento profesional para trabajar tolerancia a la frustración y autoestima, vendido B2B a consultorios de psicología infantil y adolescente. _Segmento:_ psicólogos clínicos/ludoterapeutas.
    - _P2:_ academias deportivas juveniles (fútbol, tenis, esports) que sufren «choking» bajo presión: la capa de detección de tilt e intervención sin juicio se desacopla del ajedrez y se vende como infraestructura de bienestar mental competitivo. _Segmento:_ academias deportivas multidisciplina.

    **E — Eliminar.**

    - _E1:_ se elimina toda corrección de jugadas, incluso al final — solo queda un espacio de desahogo y registro emocional post-partida. _Por qué mejora:_ el alivio llega en segundos porque no depende de procesar la partida.
    - _E2:_ se elimina la interacción en tiempo real durante la partida — el producto solo actúa después, de forma asíncrona, para que el jugador nunca sienta que lo observan mientras juega. _Por qué mejora:_ desaparece la ansiedad de desempeño en el momento.

    **R — Reordenar.**

    - _R1:_ se invierte quién detecta el problema: no es el jugador quien pide ayuda (acto vulnerable) sino un tercero de confianza —padre, maestro, amigo— quien reporta anónimamente que alguien necesita apoyo, y la IA contacta proactivamente al jugador. _Qué se invierte:_ de autoreporte vulnerable a reporte de un tercero con consentimiento.
    - _R2:_ se invierte cuándo se paga: pago por resultado emocional, no por acceso — el usuario no paga nada hasta reportar, tras dos semanas, que se siente menos frustrado o más seguro. _Qué se invierte:_ de suscripción anticipada a pago condicionado al resultado percibido.

    **Elección del equipo:** S1, C1, C2 y M2.

??? quote "Prompt completo — Ronda 2 (Claude, remix)"
    Actúa como un sintetizador de conceptos de negocio con experiencia en crear propuestas de valor originales cruzando ideas que provienen de lógicas distintas. Tu especialidad es el remix: tomar dos o tres ideas aparentemente incompatibles y encontrar el concepto híbrido que ninguna era por sí sola. Un buen remix no suma features — reencuadra quién se beneficia, cómo se entrega el valor o por qué alguien pagaría.

    Somos emprendedores en México (app con IA + página web de venta; software e IA; seis meses a MVP). Usuario: jugadores de ajedrez amateur / escuelas. Oportunidad base: el jugador que pierde partida tras partida y se siente menospreciado al buscar ayuda, sin un espacio sin juicio para preguntar.

    Las 4 ideas de SCAMPER elegidas: **S1** (anti-coach narrativo que protege el ego), **C1** (mercado de revanchas con hándicap por IA), **C2** (bot que suaviza el chat del club), **M2** (gratis para quien pierde, lo paga el lado fuerte). Ideas propias del equipo a considerar: quitar el juego en línea y la clasificación (solo progreso propio); sistema progresivo con recompensas tipo videojuego.

    Genera 3 conceptos remix. Reglas: cada remix cruza al menos 2 ideas de fuentes distintas; el resultado no puede existir en ninguna idea individual (no basta juntar features); cada concepto se describe como un negocio completo (qué hace, para quién, cómo se articulan app con IA + canal de venta); al menos uno debe cambiar quién paga, quién usa, o cuándo ocurre la intervención. FORMATO: por remix, nombre corto evocador, ideas cruzadas, concepto en 3–4 oraciones, y «lo que el cruce genera que ninguna idea sola tenía» en 1 oración.

??? abstract "Respuesta completa — Ronda 2 (Claude, remix)"
    **Base:** el jugador amateur que pierde repetidamente necesita, además de mejorar, un espacio sin jerarquía ni burla para procesar sus derrotas — algo que ni el club, ni el foro, ni el motor frío le dan hoy.

    **Remix 1 — El Relato Oficial (S1 + C2).** La IA deja de escribir la narrativa protectora solo para lectura privada (S1); la publica directamente en el grupo de WhatsApp del club apenas termina la partida, antes de que nadie comente (C2). Se vuelve la «versión oficial» del resultado que circula en el chat («tuvo al rival contra las cuerdas hasta el movimiento 30»), dejando poco espacio para la burla porque el marco ya quedó puesto. Está pensado para escuelas y clubes que pierden alumnos por vergüenza: la app IA analiza cada partida y publica el relato vía bot; la web de venta le vende al club una licencia por número de miembros («protege la moral de tu plantel»). _El cruce_ cambia el momento de la intervención (de después a antes de la burla) y quién usa el producto (del jugador al club).

    **Remix 2 — Bolsa de Redención (C1 + M2).** El producto convierte cada racha de derrotas en un «cupo de redención» que jugadores fuertes pagan por ocupar: no compran acceso a un rival débil, compran el rol de ser quien lo ayuda a romper su racha, con hándicap por IA que mantiene el resultado incierto y acreditación pública si lo logran. El jugador en racha usa el producto gratis; el jugador fuerte o excoach que busca estatus paga. La app calcula el hándicap, gestiona el emparejamiento y lleva el marcador de «redenciones logradas»; la web ofrece el cupo como producto de estatus con precio dinámico según la racha. _El cruce_ invierte quién paga y por qué: el fuerte paga por el significado de resolver la historia de otro.

    **Remix 3 — Saga sin Marcador (S1 + ranking desactivado + recompensas progresivas).** Al eliminar el ranking y como la IA nunca revela el error técnico (S1), el sistema de recompensas tipo videojuego no puede premiar victorias ni puntaje: premia la calidad narrativa de cómo el jugador enfrentó cada partida, con insignias y «capítulos» de una saga personal («el que no se rindió», «la resistencia del movimiento 40») que se acumulan sin importar el resultado. La app convierte cada partida en un capítulo narrado; la web ofrece la «temporada» como un pase que desbloquea los capítulos de tu propio recorrido, con opción de imprimirlos. _El cruce_ crea una progresión tipo videojuego ciega al desempeño.

    **Modificación posterior — La Campaña (Modo Historia).** Se resuelve la tensión convirtiendo el aprendizaje mismo en el diseño de niveles de un videojuego de un solo jugador: cada «capítulo» es una lección disfrazada de misión, protagonizada por un personaje-villano que encarna el concepto a dominar —«El Espectro de las Horquillas» te clava horquillas hasta que aprendes a verlas venir; vencerlo en la historia es, mecánicamente, haber aprendido el patrón—. No hay ranking, ni rival humano, ni partida en línea: solo tú contra el mapa de la campaña, a tu ritmo. El coaching ocurre dentro de la ficción. La app IA genera y ajusta la campaña en tiempo real según tus partidas reales (sin decírtelo en términos técnicos); la web no vende lecciones ni acceso a un profesor, vende «temporadas» o «sagas» con arco temático (aperturas, finales, táctica media), como expansiones de un videojuego, y puede incluir el «libro de la saga» ilustrado como objeto de colección. _El cruce_ produce un currículum de ajedrez real cuya secuencia pedagógica está disuelta en diseño de niveles narrativo — el villano de cada capítulo ES la lección: enseñar sin corregir y progresar sin comparar.

??? quote "Prompt completo — Ronda 3 (Claude, filtro DVN)"
    Actúa como un evaluador crítico de conceptos de negocio con experiencia en filtrar ideas de producto digital bajo criterios de mercado real en América Latina. Tu metodología es el filtro DVN: evalúas cada concepto bajo tres lentes — deseable, novedoso y viable — y produces un veredicto honesto con justificación específica. No eres optimista por defecto: un ⚠️ o ❌ bien justificado vale más que un ✅ que no resiste una repregunta.

    Somos emprendedores en México (app con IA + página web de venta; software e IA; seis meses a MVP). Usuario: jugadores amateur / escuelas.

    Conceptos a filtrar: **A — El Relato Oficial**, **B — Bolsa de Redención**, **C — Saga sin Marcador**, **D — La Campaña (Modo Historia)** _[se incluye la descripción completa de cada uno]_.

    Evalúa cada concepto: 🔴 **Deseable** (¿lo querría de verdad, no solo lo aprobaría en una encuesta? ¿resuelve el dolor ⭐ mejor que lo que existe? ¿hay razón para creer que pagaría por esto específicamente?); 🟣 **Novedoso** (¿existe algo así en LATAM o el mundo con esta combinación exacta de usuario + problema + forma de entrega?); 🟢 **Viable** (¿se puede construir una primera versión con las capacidades descritas en seis meses, con los dos componentes juntos?). FORMATO: por concepto, ✅/⚠️/❌ en cada lente con justificación de 1–2 oraciones específicas y «pregunta que el equipo debe responder», más un puntaje DVN (✅ de 3) y un veredicto (llevar al Paso 5 / refinar antes / descartar).

??? abstract "Respuesta completa — Ronda 3 (Claude, filtro DVN)"
    **Concepto A — El Relato Oficial.** 🔴 Deseable ⚠️: resuelve el dolor real (vergüenza pública en el chat) pero publica algo sobre el jugador sin pedirle permiso en el momento — puede sentirse tan invasivo como la burla, sobre todo si el «spin» suena artificial. 🟣 Novedoso ✅: no se conoce un producto que combine análisis de ajedrez con inserción automática de narrativa protectora en un chat grupal antes de que otros comenten. 🟢 Viable ⚠️: el bot y el motor de análisis son construibles en 6 meses, pero el concepto asume que la IA «sabe» qué pasó en la partida — en un club físico no hay registro digital salvo captura manual. **Puntaje: 1/3 — refinar antes.**

    **Concepto B — Bolsa de Redención.** 🔴 Deseable ⚠️: el comprador (jugador fuerte/excoach) obtiene solo estatus en una comunidad pequeña y privada — incentivo de ego débil; no hay evidencia de que alguien pague dinero real por «ayudar a un desconocido a romper una racha». 🟣 Novedoso ✅: invierte el modelo «amateur paga por jugar con el pro» a «el fuerte paga por redimir al débil con hándicap calculado». 🟢 Viable ❌: requiere sistema de rating/historial, motor de hándicap dinámico validado, matchmaking y marketplace de pago variable — choca con que el segmento juega mayoritariamente presencial, no en una plataforma propia. **Puntaje: 1/3 — descartar.**

    **Concepto C — Saga sin Marcador.** 🔴 Deseable ⚠️: el segmento valoraría la ausencia de ranking, pero es dudoso que pague por una «temporada narrativa» cuando lichess/chess.com ya ofrecen rachas de puzzles y logros gratis. 🟣 Novedoso ✅: el progreso narrativo coleccionable desacoplado de ganar/perder existe en fitness/hábitos (Zombies, Run!; Habitica) pero no aplicado a ajedrez amateur en LATAM con esta literalidad. 🟢 Viable ⚠️: narración vía IA e insignias son viables, pero arrastra el problema de captura de partidas y suma impresión física (fulfillment) fuera de las capacidades declaradas. **Puntaje: 1/3 — refinar antes.**

    **Concepto D — La Campaña (Modo Historia).** 🔴 Deseable ✅: es el único concepto que elimina por completo el rival humano y la comparación social — ataca la vergüenza en la raíz (no hay nadie que pueda burlarse) en vez de gestionar la burla después, como A, B y C. 🟣 Novedoso ⚠️: el «personaje-villano que encarna un patrón táctico» ya existe (Fritz y Chesster de ChessKid, Magnus Trainer de Chessable) — la novedad real depende de si el villano se genera a partir de los errores específicos del jugador o si es un currículo genérico. 🟢 Viable ✅: es el más contenible — no depende de captura de partidas de club ni de matchmaking ni de infraestructura de juego de terceros; es contenido generado (narrativa + puzzles) más un motor de progresión, dentro de «desarrollo de software e IA» en 6 meses. **Puntaje: 2/3 — llevar al Paso 5.**

**Resultado clave:** de 4 conceptos, **La Campaña** es el único sin bloqueador duro de viabilidad y con deseabilidad ✅.

### Paso 5 — Validación preliminar de deseabilidad

**Herramientas:** Perplexity (5 señales para cada concepto) → Claude (diagnóstico comparativo AxolotlChess vs La Campaña + hipótesis).

??? quote "Prompt completo — 5 señales (Perplexity)"
    Actúa como un investigador de mercado especializado en validar la deseabilidad de oportunidades de negocio en América Latina usando evidencia de comportamiento observable — no proyecciones ni opiniones de expertos. Tu metodología: buscar señales concretas de que un problema existe y duele lo suficiente como para que alguien pague por resolverlo: pagos actuales a soluciones imperfectas, comunidades activas, frecuencia documentada, costo cuantificable y workarounds en uso. Si la evidencia no existe o es débil, lo dices directamente.

    Somos emprendedores en México (app con IA + página web de venta). Verifica cada una de las 5 señales de deseabilidad con evidencia real y observable, buscando en fuentes primarias (comunidades online, grupos de Facebook, foros, YouTube, reseñas de productos similares, reportes de industria, INEGI, BID, CEPAL).

    _[Se corre el mismo prompt para dos conceptos:]_ **AxolotlChess** (IA que ayuda a estudiar y entender los planes; segmento: jugadores amateur que evitan clubes/foros/partidas rankeadas por miedo a la comparación; dolor: no saber qué estudiar) y **La Campaña** (modo historia de un solo jugador con villanos que encarnan patrones de error; mismo segmento; dolor: perder partidas).

    - **SEÑAL 1 — Pago actual por soluciones imperfectas:** ¿este segmento ya paga por algo que resuelve parcialmente el problema, aunque sea caro o insuficiente? Productos, precios reales, frecuencia.
    - **SEÑAL 2 — Comunidades activas:** ¿dónde habla este segmento del problema, busca soluciones o se queja? Grupos de Facebook, subreddits, foros, YouTube, con ejemplos concretos.
    - **SEÑAL 3 — Frecuencia del problema:** ¿con qué regularidad lo experimenta? ¿Datos documentados de frecuencia?
    - **SEÑAL 4 — Costo observable:** ¿cuánto le cuesta NO resolverlo? Pérdidas, costos de workarounds, tiempo con costo calculable.
    - **SEÑAL 5 — Workarounds en uso:** ¿ya inventó soluciones caseras, adaptaciones o procesos manuales?

    FORMATO: por señal, evidencia encontrada con fuente, ejemplo/periodicidad/tipo de costo según corresponda, y veredicto ✅ confirmada / ⚠️ parcial / ❌ no encontrada. Termina con un resumen de señales ✅/⚠️/❌ de 5.

??? abstract "Respuesta completa — 5 señales, concepto AxolotlChess (Perplexity)"
    **Segmento:** jugadores amateur que evitan clubes/foros/partidas rankeadas por miedo a la comparación.

    - **Señal 1 — Pago por soluciones imperfectas ✅.** Mercado activo de apps y servicios con suscripción: Chess.com desde $4.17/mes (Gold anual) hasta $12.50/mes (Diamond), ~1M descargas/mes y ~$5M ingresos/mes reportados; Chessable $11.99/mes o $74.99/año (PRO con repetición espaciada); apps con IA como Chess Academy Pro ($7.99/mes o $79.99/año), Chesshood ($2.99/mes o $24.99/año), Chessy ($7.99/mes o $49.99/año); Dr. Wolf ~$60k mensuales con 20k descargas. _Ejemplo:_ Chess.com Diamond a $99/año con análisis completo, puzzles ilimitados y herramientas avanzadas.
    - **Señal 2 — Comunidades activas ✅.** r/chessbeginners con publicaciones diarias de frustración y ansiedad («Learning chess, make me feel exhausted», «So frustrated», «I Been Playing Chess Nearly Daily For Last 2 Years Yet I Am Still Terrible»); r/chess con discusiones de estancamiento («Plateauing After Fast Improvement»), ansiedad («Chess Anxiety») y síndrome del impostor; foros de Chess.com y Lichess («Ego, Poor Attitude, and Ladder Anxiety!», «The Fear of Speaking Freely in Online Chess»); YouTube con canales de mejora para amateurs. r/chess tiene cientos de miles de miembros; r/chessbeginners, comunidad sustancial con actividad diaria.
    - **Señal 3 — Frecuencia del problema ✅.** Los amateurs dedicados juegan diaria o casi diariamente; el tiempo de estudio recomendado es 15-60 min/día (3-7 h/semana el «sweet spot» para club 800-2000 ELO); la frustración y el estancamiento son recurrentes. Periodicidad: diaria a semanal (surge cada vez que el jugador se sienta a entrenar o tras cada sesión).
    - **Señal 4 — Costo observable ✅.** Tiempo: 4-7 h/semana típicas para adultos que buscan mejora, a menudo ineficientes sin plan. Dinero: clases privadas en México $200-220 MXN/hora ($11-12 USD); plataformas internacionales $15-150 USD/hora; coaches en Lichess $30-40 USD/hora; un principiante reporta estar dispuesto a gastar $400-500 USD en su hobby. Emocional: ansiedad de rating, síndrome del impostor, abandono por mesetas; un terapeuta en formación describe el ajedrez como «muy doloroso» psicológicamente. Tipo de costo: tiempo (principal), dinero (secundario), riesgo emocional (significativo).
    - **Señal 5 — Workarounds en uso ✅.** Hojas de cálculo y trackers manuales (tutoriales en YouTube, plantillas «Chess Training Progress Tracker» en Scribd, «Chess Study Plan» en PDF, productos en Gumroad ~$20 USD); análisis manual de PGN (guías para importar partidas de Chess.com/Lichess, checklists post-partida, herramientas como ChessMD); planes de estudio auto-diseñados («12-Step Chess Improvement Plan», plantillas semanales, calculadoras de tiempo de estudio). Documentado en YouTube, Scribd, foros de Chess.com y Lichess, blogs especializados.

    **Resumen: 5 de 5 señales confirmadas ✅** (0 parciales, 0 ausentes).

    _Observaciones clave para AxolotlChess:_ el segmento existe y es vocal; ya paga, pero por soluciones genéricas (ninguna se posiciona para el que evita la comparación social); el dolor emocional está ampliamente documentado; los workarounds son manuales y frágiles (justo lo que la IA podría automatizar); nadie combina (a) personalización basada en partidas reales, (b) enfoque en planes y entendimiento y (c) experiencia diseñada para evitar la ansiedad de comparación. La deseabilidad está confirmada; el riesgo principal es la ejecución: poder construir una IA que realmente entienda planes y medio juego (no solo tácticas) y poder diseñar una experiencia que reduzca la ansiedad en lugar de aumentarla. _[listado de fuentes]_

??? abstract "Respuesta completa — 5 señales, concepto La Campaña (Perplexity)"
    **Segmento:** jugadores amateur que evitan clubes/foros/partidas rankeadas por miedo a la comparación o la burla, pero que sí quieren mejorar.

    - **Señal 1 — Pago por soluciones imperfectas ✅.** Clases particulares en México: $180–$350 MXN/hora (rango $100–$560 según instructor). Cursos online en español: ChessEnigma (Rey Enigma) desde $28 USD (~$560 MXN) hasta paquetes de $297–$321 USD (~$6,000–$6,400 MXN) con acceso de por vida. Chess.com: Gold $4.17/mes, Platinum $6.67/mes, Diamond $12.50/mes. Apps con IA: Coach Ajedrez, IQChess, ChessLine (CHF 4.99/mes ~$110 MXN), sin personalización narrativa. _Ejemplo:_ un jugador intermedio en México paga ~$229 MXN/hora en Superprof y muchos contratan sesiones recurrentes (1–2/semana) durante meses.
    - **Señal 2 — Comunidades activas ✅.** Grupos de WhatsApp y Telegram en México y LATAM («Chess Club», «Team México», «Ajedrecistas por el Mundo», «Team Ajedrez Virtual») con enlaces públicos; foros de Chess.com y Lichess con participación hispana sobre ansiedad por rating y autoestudio; canales de YouTube en español («El Peón Cuántico», «Ajedrez con Boudy», «Rey Enigma») con videos sobre «por qué pierdes partidas», «cómo estudiar solo», «ansiedad en ajedrez»; blogs y academias (The Zugzwang Members, Ajedrez en Minutos, Ajedrez.pro) sobre psicología del jugador amateur. Los canales de YouTube citados suman >500k suscriptores combinados.
    - **Señal 3 — Frecuencia del problema ✅.** Testimonios documentados: los amateurs pierden entre 40–60% de sus partidas de forma consistente, con series de derrotas que generan bloqueo mental. Los intermedios juegan 1–2 partidas rápidas/día en promedio (~4.5 h/semana de entrenamiento recomendado). Ansiedad y evitación: usuarios reportan semanas sin jugar por miedo a la comparación. Periodicidad: semanal, con picos diarios y semanas de evitación.
    - **Señal 4 — Costo observable ✅.** Clases: 1 clase/semana a $229 MXN/hora durante 6 meses ≈ **$5,500 MXN**; 2 clases/semana ≈ $11,000 MXN. Cursos premium: paquetes de ChessEnigma $297–$321 USD, con jugadores que compran varios sumando $500–$800 USD (~$10,000–$16,000 MXN). Suscripciones: Chess.com Diamond ~$250 MXN/mes → **$3,000 MXN/año**; ChessLine ~$1,320 MXN/año. Costo de oportunidad del tiempo: ~4.5 h/semana; a salario mínimo (~$250 MXN/día), 18 h/mes ≈ **~$1,800 MXN/mes**. Tipo de costo: dinero + tiempo.
    - **Señal 5 — Workarounds en uso ✅.** Autoestudio con YouTube y libros («ver a Gotham, Rosen, Finegold, Agadmator», leer «How to Study Chess on Your Own»); jugar contra uno mismo (girar el tablero, apps en modo Hand-Off); cuentas de entrenamiento anónimas en Lichess/Chess.com para jugar sin presión de rating; rutinas de exposición gradual a torneos pequeños. Documentado en foros de Lichess y Chess.com, blogs (The Zugzwang, Ajedrez.pro, Ajedrez en Minutos) y YouTube en español.

    **Resumen: 5 de 5 señales confirmadas ✅** (0 parciales, 0 ausentes). La evidencia es robusta: el segmento existe, duele lo suficiente (pagan cientos a miles de pesos), se organiza en comunidades activas, experimenta el problema con frecuencia semanal, incurre en costos observables y ya inventó workarounds caseros. La oportunidad para La Campaña está en diferenciarse de esos workarounds fragmentados y fríos con un sistema estructurado de gamificación narrativa que elimine la comparación social. _[listado de fuentes]_

??? quote "Prompt completo — Diagnóstico comparativo (Claude)"
    Actúa como un mentor de emprendimiento con experiencia en ayudar a equipos a decidir entre dos direcciones de negocio usando evidencia de mercado. Tu especialidad es el diagnóstico comparativo: cuando un equipo tiene dos conceptos posibles, identificas cuál tiene más deseabilidad real, cuál tiene más riesgo de suicidio creativo y cuál merece los recursos. Eres directo — no recomiendas «explorar los dos» cuando los datos favorecen claramente uno.

    Somos emprendedores en México (app con IA + página web de venta; seis meses a MVP). Evaluamos dos conceptos y necesitamos un diagnóstico comparativo de deseabilidad: **Concepto A — AxolotlChess** (idea original evolucionada) y **Concepto B — La Campaña** (concepto con la arista integrada). _[Se adjuntan las verificaciones de deseabilidad de 5 señales de cada uno, ambas 5/5.]_

    Haz tres cosas: **DIAGNÓSTICO COMPARATIVO** (¿cuál tiene deseabilidad más sólida según la evidencia? ¿dónde está la diferencia más importante — tipo de señales, intensidad del dolor, claridad del segmento?); **RIESGO DE SUICIDIO CREATIVO POR CONCEPTO** (¿cuál de los tres tipos — sin dolor real / ya existe / no puede construirse — es el riesgo principal de cada uno?); **MAPA DE HIPÓTESIS** (2 hipótesis falseables por concepto, las más críticas antes de elegir, con «cómo probarla» en una entrevista de 20 min). Formato falseable: «creemos que [usuario] experimenta [situación] con frecuencia [X] y pagaría [rango] porque [razón]. Si esto es falso, [qué cambiaría].» Termina con un veredicto: concepto con mayor deseabilidad, por qué, y recomendación.

??? abstract "Respuesta completa — Diagnóstico comparativo (Claude)"
    **Concepto A — AxolotlChess.** Deseabilidad: **Media.** Fortaleza: Señal 1 en volumen bruto (el mercado de IA de ajedrez ya mueve dinero real — Chess.com ~$5M/mes, Dr. Wolf ~$60k/mes). Riesgo: esa misma Señal 1 no prueba el diferenciador — toda la evidencia es de «gente paga por mejorar en ajedrez con IA» en general; ninguna app citada se posiciona para el segmento que evita la comparación. Suicidio creativo más probable: **ya existe.** Nivel de riesgo: **Alto.**

    **Concepto B — La Campaña.** Deseabilidad: **Alta.** Fortaleza: Señal 3 + Señal 4 combinadas — el dolor está cuantificado y atado al mecanismo de evitación (40-60% de partidas perdidas, semanas sin jugar por ansiedad), y la evidencia está en el terreno real de los fundadores (pesos mexicanos, ChessEnigma en español, grupos «Team México», canales de YouTube hispanos). Riesgo: Señal 1 tiene el mismo problema que en A — la disposición a pagar demostrada es por clases y cursos genéricos, no por una campaña narrativa sin ranking. Suicidio creativo más probable: **ya existe.** Nivel de riesgo: **Medio.**

    La diferencia más importante no está en el tipo de señales (ambos 5/5) ni en si el dolor es real (confirmado en los dos). Está en la claridad del segmento y en qué tan bien la evidencia corresponde al mercado real: la verificación de B usa fuentes en español, precios en MXN y comunidades mexicanas identificables; la de A es mayoritariamente anglosajona (Reddit en inglés, precios en USD, Chess.com global). Para un negocio que arranca en México con seis meses de pista, esa es la diferencia entre evidencia que describe a tu comprador real y evidencia que describe al mercado global genérico. Además ya estaba anticipado: en el Filtro DVN, «La Campaña» fue el único con 2/3 y sin bloqueador de viabilidad.

    **Hipótesis — Concepto A.** _H1:_ el jugador amateur mexicano que evita clubes y partidas rankeadas por miedo a la comparación pierde o evita jugar con frecuencia semanal, y pagaría $100-150 MXN/mes por una IA que explique planes de medio juego sin mostrarle rating ni comparación, porque hoy Chess.com y Chessable sí exponen leaderboards. Si es falso: el «sin comparación» no genera disposición a pagar sobre una app genérica, y AxolotlChess compite por el mismo dólar que Chess.com. _Prueba:_ dos mockups del mismo ejercicio (uno con leaderboard, otro sin) y preguntar cuál usaría y cuánto pagaría por cada uno. _H2:_ preferiría explicaciones de IA sobre sus propias partidas antes que cursos genéricos de YouTube o spreadsheets, porque sus workarounds exigen conocimiento previo que le falta. Si es falso: confía más en un humano (coach o YouTuber conocido) y el producto necesita un componente humano híbrido.

    **Hipótesis — Concepto B.** _H1:_ el jugador amateur mexicano que evita la comparación pierde o deja de jugar semanas por miedo al juicio, y pagaría $100-200 MXN/mes por una campaña de un solo jugador sin ranking, porque sus workarounds (cuentas anónimas, jugar contra sí mismo) dan anonimato pero ningún feedback estructurado. Si es falso: quiere una señal de progreso comparativa aunque sea anónima, y el modo campaña se percibe como «juego», no como entrenamiento serio. _Prueba:_ describir el modo campaña y preguntar «¿esto se siente como una herramienta seria para mejorar o como un juego para pasar el rato?». _H2:_ preferiría enfrentar a «El Espectro de las Horquillas» dentro de una narrativa antes que una clase particular o un curso en video, porque elimina la exposición de ser evaluado en tiempo real. Si es falso: valora el contacto humano y el concepto necesita un componente humano para no sentirse solitario.

    **Veredicto: B — La Campaña.** La evidencia de B está anclada al mercado real donde van a vender (pesos mexicanos, comunidades y creadores en español, tasa de pérdida del 40-60% ligada a la evitación semanal), mientras que la de A prueba el mercado genérico de entrenamiento, no el ángulo específico de evitar la comparación; y B ya salió como el concepto más viable en el Filtro DVN. **Recomendación:** llevar B al Paso 6, con una condición no negociable — demostrar que los villanos/patrones se generan dinámicamente a partir de los errores reales de cada jugador (defendible como IA propia), no como currículo fijo, porque así ya lo hacen Chessable y ChessKid, gratis o más barato.

**Resultado clave:** ambos conceptos llegan a **5/5 señales**, pero el diagnóstico comparativo recomienda **La Campaña** por la calidad de la evidencia y la viabilidad.

### Paso 6 — Criterios de selección de oportunidad

**Herramienta:** matriz de selección del equipo (3 criterios).

??? note "Matriz de selección completa"
    | Criterio | AxolotlChess | La Campaña |
    |----------|--------------|------------|
    | **1 · Pasión** — ¿seguiría el equipo sin calificación? | Sí — amor al ajedrez y a compartir conocimiento | Sí — «me gustan los videojuegos y el ajedrez; combinarlos me emociona» |
    | **2 · Habilidad** — ¿pueden nombrar hoy el componente técnico? | Parcial — riesgo: bases de datos, inicio de sesión, ciberseguridad | Parcial — riesgo: bases de datos, inicio de sesión, animaciones |
    | **3 · Mercado** — señales confirmadas + tamaño | 3/5 señales · ~40,000 usuarios MX / ~384,000 LATAM · Pasa: Sí | 3/5 señales · ~88,000 usuarios MX / ~440,000 LATAM · Pasa: Sí |
    | **Resultado** | 3/3 ✅ → Paso 7 | 3/3 ✅ → Paso 7 |

    **Concepto elegido para el Paso 7:** _La Campaña_. Por qué este y no el otro: más usuarios potenciales en México y en Latinoamérica.

### Paso 7 — Elección y defensa de la oportunidad

El entregable del Paso 7 es el **Reporte de Oportunidad**, que consolida los resultados de los pasos anteriores en el formato de la actividad.

#### Reporte de Oportunidad — Semana 2

- **Equipo:** David López Ramírez
- **Concepto elegido:** La Campaña (Modo Historia)

##### 1. El problema

**Segmento específico:** jugadores amateur adultos de ajedrez en México y LATAM, rating ~1200–1800 Elo en rápidas/blitz online, que **evitan clubes, foros y partidas rankeadas** por miedo a la comparación o la burla, pero que **sí quieren mejorar**, no solo sentirse mejor. Ya gastan dinero en su mejora (Chess.com, cursos sueltos, algún coach).

**Dolor:** pierden partidas de forma constante (40–60 % de sus partidas según foros y comunidades) y, cuando buscan ayuda de alguien más fuerte, sienten menosprecio o intimidación. Hoy el aprendizaje de ajedrez viene empaquetado con **jerarquía y soberbia** (clubes, foros, coaches) o con el **feedback frío de un motor**.

**Workaround actual con costo observable:**

- Clases particulares en México: ~$229 MXN/hora → **$5,500–$11,000 MXN** en 6 meses (1–2 clases/semana).
- Cursos grabados genéricos (tipo ChessEnigma): **$6,000–$16,400 MXN** por acceso de por vida a varios cursos.
- Suscripciones a apps genéricas: Chess.com Diamond ~$3,000 MXN/año; apps de IA (ChessLine ~$1,320 MXN/año, Chesshood…).
- Autoestudio sin estructura (YouTube, hojas de cálculo, checklists de PGN) y cuentas anónimas para jugar sin presión de rating — evitan la ansiedad pero pierden todo feedback estructurado.
- ~4.5 h/semana de estudio sin plan → ~**$1,800 MXN/mes** de costo de oportunidad (valorando el tiempo a salario mínimo).

##### 2. Evidencia de deseabilidad

Verificación del Paso 5 — **5 de 5 señales confirmadas** con evidencia observable:

**Señal 1 — Pago por soluciones imperfectas ✅**

- Clases particulares en México $180–350 MXN/hora (promedio $229). Cursos en español de ChessEnigma (Rey Enigma) $28–321 USD con acceso de por vida. Chess.com Diamond $119/año. Apps de IA $2.99–12.50/mes.
- _Fuente:_ Superprof.mx y Cronoshare.com.mx (clases); chessenigma.com y tuscursoscloud.com (cursos); páginas de precios de Chess.com; fichas de App Store / Google Play (Chess Academy Pro, Chesshood, ChessLine).

**Señal 2 — Comunidades activas ✅**

- Grupos públicos de WhatsApp/Telegram («Team México», «Ajedrecistas por el Mundo», «Team Ajedrez Virtual»); canales de YouTube en español (El Peón Cuántico, Ajedrez con Boudy, Rey Enigma) con **>500k suscriptores combinados** y videos sobre «por qué pierdes partidas» y «ansiedad en ajedrez»; hilos de foro de Chess.com y Lichess sobre ansiedad de rating y miedo al juicio.
- _Fuente:_ enlaces de invitación públicos de los grupos; foros de chess.com y lichess.org («Chess Anxiety», «Ego, Poor Attitude, and Ladder Anxiety!», «The Fear of Speaking Freely in Online Chess»); páginas de los canales de YouTube.

**Señal 3 — Frecuencia del problema ✅**

- Testimonios documentados: los amateurs pierden **40–60 % de sus partidas** de forma consistente; usuarios reportan **semanas sin jugar** por ansiedad o miedo a la comparación. Los intermedios juegan 1–2 partidas rápidas/día (~4.5 h/semana de entrenamiento recomendado). Periodicidad: semanal, con picos diarios y semanas de evitación.
- _Fuente:_ hilos de r/chess y r/TournamentChess («How to improve/get over traumatizing losses», «How did you overcome tilting»); planes de entrenamiento en blogs especializados (oldschoolchess.com, mychessplan.com).

**Señal 4 — Costo observable ✅**

- Dinero: $3,000–$16,000 MXN según la vía (clases $5,500–11,000 MXN/6 meses; cursos $6,000–16,400 MXN; Chess.com Diamond $3,000 MXN/año). Tiempo: ~$1,800 MXN/mes de costo de oportunidad (4.5 h/semana a salario mínimo ~$250 MXN/día).
- _Fuente:_ precios verificados de Superprof.mx y chessenigma.com; cálculo propio con salario mínimo (CONASAMI 2026).

**Señal 5 — Workarounds en uso ✅**

- Autoestudio con YouTube y libros («How to Study Chess on Your Own»); jugar contra uno mismo; cuentas de entrenamiento anónimas en Lichess/Chess.com; rutinas de exposición gradual a torneos pequeños; hojas de cálculo y plantillas PDF de seguimiento; checklists de análisis de PGN.
- _Fuente:_ plantillas en Scribd («Chess Training Progress Tracker», «Chess Study Plan»); tutoriales de YouTube sobre spreadsheets; foros de Lichess/Chess.com; blogs The Zugzwang, Ajedrez.pro, Ajedrez en Minutos.

##### 3. Pain-Gain Map

**Usuario:** jugador amateur adulto en México/LATAM, ~1200–1800 Elo, juega con regularidad y ya gasta dinero en mejorar.

| # | Dolores (ordenados por intensidad) | Ganancias (ordenadas por deseo) |
|---|------------------------------------|---------------------------------|
| 1 | ⭐ **D1.** Perder muchas partidas (40–60 %) — el dolor más frecuente e inmediato | ⭐ **G1.** Plan personalizado para cada jugador según sus partidas reales |
| 2 | **D2.** No saber qué estudiar para mejorar / no entender un tema | **G2.** Explicaciones de apertura, medio juego y finales y de posiciones |
| 3 | **D3.** Ansiedad de rating y síndrome del impostor → evita torneos y partidas competitivas | **G3.** Sentir progreso y validación sin depender de ganar ni de compararse |
| 4 | **D4.** Falta de una vista agregada de sus errores recurrentes entre partidas | **G4.** Accesibilidad del idioma (contenido y coaching 100 % en español) |
| 5 | **D5.** Soberbia o menosprecio de los jugadores más experimentados al pedir ayuda | **G5.** Un espacio de entrenamiento sin exposición ni evaluación de un tercero en tiempo real |

##### 4. Concepto recomendado

**La Campaña (Modo Historia).** El aprendizaje de ajedrez se convierte en el **diseño de niveles de un videojuego de un solo jugador**: cada «capítulo» es una lección disfrazada de misión, protagonizada por un **personaje-villano** que encarna un patrón de error real y recurrente del jugador (p. ej. «El Espectro de las Horquillas»). No hay ranking, no hay rival humano, no hay partida en línea contra otros: solo el jugador contra el mapa de la campaña, a su propio ritmo. El coaching ocurre **dentro de la ficción** —lo que dice el personaje, la trampa que tiende—, nunca como corrección fría ni comparación social; la web vende «temporadas» o «sagas» por tema (aperturas, medio juego, finales) en vez de una suscripción genérica.

**Letras SCAMPER que lo originaron:**

- **S — Sustituir:** la IA deja de ser correctora directa y pasa a ser una narrativa que protege el ego mientras enseña (idea S1).
- **E — Eliminar:** se quita el ranking y la comparación entre jugadores; queda solo el progreso propio.
- **A — Adaptar:** se adopta la lógica de progresión y recompensas de un videojuego («capítulos» y «temporadas» en vez de niveles de estudio).

**Puntaje DVN (Concepto D):** 🔴 Deseable ✅ · 🟣 Novedoso ⚠️ · 🟢 Viable ✅ → **2 de 3**, llevado al Paso 5 y confirmado luego con 5/5 señales de deseabilidad.

- **Deseable ✅** — es el único concepto que elimina el rival humano y la comparación en la raíz del dolor, en vez de gestionar la burla después de que ocurre.
- **Novedoso ⚠️** — el «villano por patrón táctico» ya existe (Chessable, ChessKid); la novedad real depende de que el villano se **genere dinámicamente** a partir de los errores propios del jugador, no de un currículo fijo.
- **Viable ✅** — no depende de capturar partidas de club físico ni de _matchmaking_ en línea; es contenido generado (narrativa + puzzles) más un motor de progresión, dentro de las capacidades del equipo.

##### 5. La oportunidad en una oración

!!! quote ""
    «Existe una oportunidad para el **jugador amateur de ajedrez en México/LATAM** que necesita **dejar de perder partidas y aprender sin sentirse juzgado**, porque hoy el aprendizaje de ajedrez viene empaquetado con jerarquía y soberbia (clubes, coaches, foros) o con el feedback frío de un motor, sin ningún espacio libre de comparación social para progresar a su propio ritmo.»

Es **falseable**: alguien podría objetar «lo que el jugador amateur quiere es ganar más rápido, no un espacio sin juicio» — y esa objeción posible es lo que hace que la oración esté bien formulada.

##### 6. Por qué este equipo

- **Criterio 1 — Pasión (razón personal):** el equipo seguiría aunque no hubiera calificación de por medio. Nos gustan los videojuegos y también el ajedrez; poder combinarlos en un mismo producto nos emociona genuinamente.
- **Criterio 2 — Habilidad (elemento técnico concreto):** el motor central conecta con la **API de Chess.com/Lichess** para ingerir el historial real de partidas de cada jugador (formato PGN) y usa un **modelo de lenguaje (LLM)** para clasificar los errores recurrentes —blunder táctico, apuro de tiempo, error posicional— y generar dinámicamente los «villanos» y capítulos de la campaña. Componente más arriesgado: base de datos, sistema de inicio de sesión y animaciones — conviene acotar su alcance para el MVP de 6 meses.

##### 7. Hipótesis para la Semana 3

- **H1 — Disposición a pagar.** Creemos que el jugador amateur mexicano que evita la comparación social pierde partidas o deja de jugar semanas seguidas por miedo al juicio, y pagaría **$100–200 MXN/mes** por una campaña de un solo jugador donde el coaching ocurre dentro de la ficción y no hay ranking, porque hoy sus workarounds (cuentas anónimas, jugar contra sí mismo) le dan anonimato pero ningún feedback estructurado. _Si esto es falso:_ el jugador sí quiere una señal de progreso comparativa (aunque sea anónima), el modo campaña se percibe como «juego» y no como «entrenamiento serio», y baja su disposición a pagar precio de entrenamiento.
- **H2 — Preferencia sobre alternativas.** Creemos que el jugador amateur preferiría enfrentar a un «villano» dentro de una narrativa de campaña antes que tomar una clase particular o un curso en video, porque elimina la exposición de tener a alguien evaluándolo en tiempo real. _Si esto es falso:_ el jugador valora el contacto humano —aunque genere algo de ansiedad— porque le da una validación que una narrativa de IA no reemplaza, y el concepto necesita un componente humano para no sentirse solitario ni abandonarse a las pocas semanas.
- **H3 — Personalización como diferenciador.** Creemos que el jugador amateur pagaría más por una campaña donde los «villanos» se generan dinámicamente a partir de los errores reales de sus propias partidas que por un currículo fijo de lecciones genéricas por nivel, porque Chessable (Magnus Trainer) y ChessKid (Fritz y Chesster) ya ofrecen contenido fijo gratis o barato. _Si esto es falso:_ el jugador no percibe ni valora la diferencia entre un villano personalizado y uno genérico, y «La Campaña» pierde su defensa frente a competidores establecidos.

---

##### 8. Lo que cambió

- **El supuesto cuestionado:** antes creíamos que la idea resolvía «no saber qué estudiar / no entender los planes» para jugadores 1200–1800, con una IA que explicara aperturas, medio juego y finales. El estrés del Paso 2 mostró que ese dolor (D2) es una **atribución halagadora y difícil de auto-diagnosticar**, y el más cómodo de construir con un LLM — no necesariamente el más urgente para el usuario.
- **La arista encontrada:** el dolor más intenso y frecuente **no es cognitivo sino emocional y social** — perder partidas de forma constante (D1) y sentirse menospreciado al pedir ayuda (D5).
- **Cómo modificó la dirección del concepto:** se pasó de un tutor conceptual de planes estratégicos a **«La Campaña»**, un modo historia de un solo jugador, sin ranking ni comparación, donde el coaching vive en la narrativa y el «villano» de cada capítulo encarna un patrón de error real del jugador.
- **Concepto B como oportunidad de expansión:** la idea original (AxolotlChess: IA que explica planes) no se descarta — puede integrarse más adelante como el «conocimiento» que el jugador desbloquea al vencer a cada villano, una vez validado el motor técnico y con evidencia real de que el mecanismo de personalización (H3) funciona.

##### Lo que el equipo tiene claro al cerrar la sesión

- **¿Quién específicamente tiene el problema?** El jugador amateur adulto de ajedrez en México/LATAM, ~1200–1800 Elo en rápidas/blitz online, que evita clubes, foros y partidas rankeadas por miedo a la comparación o la burla y que ya gasta dinero en mejorar.
- **¿Qué evidencia de que el problema es real y duele?** 5 de 5 señales verificadas; en particular la **Señal 1** (pagos observables a clases, cursos y suscripciones — Superprof, ChessEnigma, Chess.com) y la **Señal 3** (40–60 % de partidas perdidas y semanas de evitación documentadas en foros de r/chess y Lichess).
- **Primera hipótesis a probar en la Semana 3 (H1):** «Creemos que el jugador amateur que evita la comparación pierde partidas o deja de jugar semanas seguidas por miedo al juicio y pagaría $100–200 MXN/mes por una campaña de un solo jugador sin ranking, porque sus workarounds actuales le dan anonimato pero ningún feedback estructurado. Si esto es falso, el concepto necesita ofrecer una señal de progreso comparativa (aunque sea anónima) y reposicionarse como entrenamiento serio y no como juego.»
