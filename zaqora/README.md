# Zaqora — prototipo

Zaqora es una PWA para jugadores de ajedrez: cuando pierdes en Lichess, un villano que encarna tu error recurrente te reta a volver a esa partida, y un consejero de tu bando te ayuda a encontrar las jugadas que se te escaparon. Proyecto de David López Ramírez para Proyecto de Ingeniería IV. La documentación completa está en la página [Proyecto final](https://vidddda.github.io/Portafolio-193167/proyecto_final/) y en la [semana 9](https://vidddda.github.io/Portafolio-193167/pi4_s9/).

**Probarlo:** https://vidddda.github.io/Portafolio-193167/prototipo/activar.html

## Estado (24/11/2026)

- Entrar con la cuenta de Lichess (OAuth con PKCE, sin contraseña ni permisos extra); registro automático con un código J1, J2…
- Primer contacto: las **últimas 5 derrotas** se vuelven 5 capítulos; llega un solo aviso que abre Inicio.
- Cada capítulo: historia en 3 partes y hasta 3 encuentros (los errores más grandes de la partida), con el villano que reta y el consejero del bando que guía. Textos de IA (Mistral Small 3.1) con plantilla de respaldo.
- Cada derrota nueva genera su capítulo. El detector corre en GitHub Actions cada 10 minutos o al tocar «Revisar mis partidas ahora».
- Una sesión de prueba con un jugador externo; faltan cuatro y la prueba de campo.

## Arquitectura

```text
Celular (PWA: Inicio, activación, escena)
  │  Entrar con Lichess (OAuth PKCE) ─────────────▶ Lichess
  │  token de Lichess ──▶ Supabase · función «capitulos» ──▶ Lichess (¿quién es?)
  │                         │  lee/escribe jugadores, capítulos, avance
  │                         └─▶ GitHub (Revisar ahora: lanza el detector)
  │  eventos (solo inserción) ──▶ Supabase
  ▲
  │ Web Push (VAPID)
  │
GitHub Actions · detector (cada 10 min o a petición)
  ├─ partidas ◀── Lichess API (NDJSON)
  ├─ análisis: Stockfish 19
  ├─ historia y diálogos ◀──▶ Cloudflare Workers AI (Mistral Small 3.1)
  └─ estado, capítulos, suscripciones ◀──▶ Supabase (service_role)
```

| Parte | Dónde está |
| :--- | :--- |
| Páginas (Inicio, activación, escena, aviso de privacidad), `sesion.js`, `sw.js`, `manifest.webmanifest`, `config.js`, piezas de los bandos | [`docs/prototipo/`](../docs/prototipo/) |
| Detector de derrotas | [`zaqora/detector/detectar_derrotas.py`](detector/detectar_derrotas.py) |
| Flujo de GitHub Actions | [`.github/workflows/detector.yml`](../.github/workflows/detector.yml) |
| Función de Supabase y scripts SQL | Fuera del repositorio (carpeta del proyecto); se describen abajo |
| Claves privadas (service_role de Supabase, VAPID privada, token de Cloudflare, token de GitHub) | **Solo** en los secretos de GitHub Actions y de Supabase. Nunca en el repositorio |

`config.js` solo contiene datos públicos: la URL de Supabase, su clave *anon* y la clave pública VAPID.

## Datos (Supabase)

Todas las tablas tienen RLS activado. La página solo puede **insertar** en `eventos` y `suscripciones`; nadie puede leer desde el navegador.

| Tabla | Para qué |
| :--- | :--- |
| `jugadores` | Quien entra con Lichess: usuario, código J#, `activo`, `ultima_revision` |
| `capitulos` | Cada capítulo enviado: usuario, villano, enlace de la escena y avance |
| `estado_detector` | Qué partidas ya revisó el detector y si ya envió el primer contacto |
| `suscripciones` | La suscripción a avisos de cada teléfono, por código |
| `eventos` | Lo que hace cada jugador en la escena y en Inicio, por código |

La función `capitulos` (Edge Function) recibe el token de Lichess del jugador, le pregunta a Lichess quién es y solo entonces devuelve o actualiza sus capítulos; también lanza «Revisar ahora» (una vez cada 3 minutos).

## Cómo reproducirlo

1. **Supabase:** crea un proyecto, ejecuta los scripts SQL (`eventos`, `suscripciones`, `capitulos`, `jugadores`, `estado_detector`, columna `ultima_revision`) y publica la función `capitulos`. Guarda en sus secretos `ZAQORA_GITHUB_TOKEN` (token de GitHub con permiso de **Actions: Read and write** sobre este repositorio).
2. **Claves VAPID:** genera un par. La pública va en `config.js`; la privada, en el secreto de GitHub.
3. **Cloudflare:** cuenta gratuita, Account ID y un token de Workers AI.
4. **Secretos de GitHub** (Settings → Secrets and variables → Actions): `ZAQORA_SUPABASE_URL`, `ZAQORA_SUPABASE_SERVICE_KEY`, `ZAQORA_VAPID_CONTACTO`, `ZAQORA_VAPID_PRIVADA` (en una sola línea), `CLOUDFLARE_ACCOUNT_ID`, `CLOUDFLARE_TOKEN`.
5. **Publica** `docs/` en GitHub Pages. El flujo **Detector de derrotas** corre solo cada 10 minutos; también se lanza a mano desde la pestaña Actions.

### Detector en una laptop (opcional)

```
python -m pip install --user chess pywebpush
python zaqora/detector/detectar_derrotas.py                   # revisa sin enviar nada
python zaqora/detector/detectar_derrotas.py --enviar --cada 5 # revisa y envía cada 5 min
python zaqora/detector/detectar_derrotas.py --ver-historia J1  # muestra el primer contacto sin enviar
python zaqora/detector/detectar_derrotas.py --historia J1      # envía el primer contacto
python zaqora/detector/detectar_derrotas.py --probar-ia J1     # prueba la historia con IA
```

Lee las claves de un `config_local.json` junto al script o de las mismas variables `ZAQORA_*` y `CLOUDFLARE_*`, y busca Stockfish en `stockfish/`, en `ZAQORA_STOCKFISH` o en el sistema. No lo corras al mismo tiempo que GitHub Actions: el mismo jugador podría recibir avisos dobles.

## Manual de usuario

1. Abre Zaqora en tu celular (en iPhone, agrégala a la pantalla de inicio desde Safari y ábrela desde el ícono).
2. Elige tu bando y toca **Entrar con Lichess**; autoriza a Zaqora.
3. En Inicio, toca **Activar** y permite las notificaciones.
4. En unos minutos llegan tus últimas 5 derrotas como capítulos.
5. En cada capítulo: lee la historia, toca **Muéstrame** y encuentra la jugada (toca la pieza y luego la casilla). El consejero te da pistas; tras 3 intentos te enseña la jugada.
6. Juega en Lichess como siempre; cada derrota te llega como un reto. **Revisar mis partidas ahora** lo adelanta.
7. **Salir** quita tus capítulos del teléfono y deja de recibir avisos ahí; vuelven al entrar otra vez.

## Licencias de terceros

- [Stockfish](https://github.com/official-stockfish/Stockfish) (GPLv3): análisis de las partidas.
- [Mistral Small 3.1](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503) (Apache 2.0) en Cloudflare Workers AI: historia y diálogos.
- [python-chess](https://github.com/niklasf/python-chess) y [pywebpush](https://github.com/web-push-libs/pywebpush) en el detector.
- API pública y OAuth de Lichess, según sus [términos de servicio](https://lichess.org/terms-of-service).
- Piezas de los bandos: assets propios del proyecto.
