# Zaqora — prototipo de avisos del villano

Zaqora es una PWA para jugadores de ajedrez: cuando pierdes una partida en Lichess, un villano que encarna tu error recurrente te manda un aviso al celular y te invita a una escena construida sobre esa misma partida. Proyecto de David López Ramírez para Proyecto de Ingeniería IV. La documentación completa está en la página [Proyecto final](https://vidddda.github.io/Portafolio-193167/proyecto_final/).

## Estado

Prototipo de experiencia en modo «mago de Oz» (semana 8). Funciona de punta a punta con partidas reales: detecta la derrota, envía el aviso push y abre la escena con la posición antes del error. **Todavía no hay pruebas con usuarios externos** y el narrador con IA no está conectado (las frases son plantillas).

## Arquitectura

```text
Lichess API ──HTTPS NDJSON──▶ Detector de derrotas (Python, en la laptop)
                                   │  Web Push (VAPID)
                                   ▼
                         Servicio push del navegador ──▶ Service worker ──▶ Escena (PWA)
                                                                              │
Página de activación ──suscripción──▶ Supabase (suscripciones, eventos) ◀──eventos
Landing ──visitas, clics, pre-registros──▶ Supabase (eventos, preregistros)
```

| Parte | Dónde está | ¿Pública? |
| :--- | :--- | :---: |
| Página de activación, escena, service worker, manifest, iconos, `config.js` | [`docs/prototipo/`](../docs/prototipo/) | Sí |
| Landing y aviso de privacidad | `docs/landing/` (por publicar) | Sí |
| Detector de derrotas (`detectar_derrotas.py`), SQL de las tablas, plantilla de participantes | Carpeta local del proyecto | No |
| Clave `service_role` de Supabase y clave privada VAPID (`config_local.json`, `vapid_privada.pem`) | Carpeta local del proyecto | **Nunca** |
| Usuarios de Lichess de los participantes (`participantes.csv`) | Carpeta local del proyecto | **Nunca** |

`config.js` solo contiene datos que pueden ser públicos: la URL de Supabase, su clave *anon* y la clave pública VAPID. Las tablas tienen RLS de **solo inserción** para la clave *anon*: nadie puede leer, cambiar ni borrar datos desde el navegador.

## Cómo reproducirlo

1. Python 3.10+ y las librerías: `python -m pip install --user chess pywebpush`.
2. **Supabase (plan Free):** crea un proyecto y ejecuta en el SQL Editor el script de las tablas `suscripciones` y `eventos` (y, para la landing, `preregistros`). Copia la URL y la clave *anon* en `docs/prototipo/config.js`, y la URL y la clave `service_role` en `config_local.json` (local).
3. **Claves VAPID:** genera un par (por ejemplo, con `pywebpush` o `py_vapid`). La pública va en `config.js`; la privada, en `vapid_privada.pem` (local).
4. **Publica** `docs/` (GitHub Pages lo hace al hacer *push* a `main`). Los avisos push solo funcionan en https.
5. **Prueba contigo:** abre `…/prototipo/activar.html?p=P0` en tu celular, activa los avisos y corre `python detectar_derrotas.py --probar P0`.
6. **Prueba con participantes:** llena `participantes.csv` (alias, usuario de Lichess, orden de variantes) y corre `python detectar_derrotas.py --cada 5 --enviar`.

Detalles del detector:

- Revisa las partidas nuevas de cada participante cada `--cada` minutos, una petición a la vez, y espera 60 s si Lichess responde 429.
- Usa el análisis de Lichess para encontrar la posición antes del peor error. Si la derrota todavía no tiene análisis, espera hasta 30 minutos (puedes pedirlo en la página de la partida); después usa una posición de ejemplo y lo avisa.
- Un solo aviso por derrota, sin recordatorios. El aviso dura 1 hora en el servicio push (`ttl=3600`).

## Manual de usuario (beta)

1. Abre el enlace de activación que te mandamos en tu celular.
2. **Android:** toca «Activar avisos del villano». **iPhone (iOS 16.4+):** Compartir → «Agregar a pantalla de inicio», abre Zaqora desde el ícono y activa los avisos.
3. Juega en Lichess como siempre. Cuando pierdas, te llegará un aviso del villano.
4. Tócalo: «Muéstrame» revela la posición antes de tu error; «Déjame en paz» cierra el encuentro.
5. Toca la pieza y luego la casilla para encontrar la jugada que se te escapó. «Pista del villano» te ayuda.
6. Para salir, escribe ALTO o desactiva las notificaciones de Zaqora en tu navegador.

## Licencias de terceros

- El detector usa la API pública de Lichess según sus [términos de servicio](https://lichess.org/terms-of-service).
- El detector usa [python-chess](https://github.com/niklasf/python-chess) y [pywebpush](https://github.com/web-push-libs/pywebpush).
- La versión siguiente usará Stockfish (GPLv3) en el navegador y Llama 3.1 en Cloudflare Workers AI («Built with Llama»).
