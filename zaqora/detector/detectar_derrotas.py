"""Mago de Oz para la prueba de la semana 8 de Zaqora.

Revisa las partidas públicas de Lichess de cada participante, detecta derrotas
nuevas y, por cada una, envía el aviso del villano como notificación push de la
PWA (variante A, B o C según el orden del participante). Al tocar el aviso, el
participante abre la escena con la posición de su error.

Uso:
    python detectar_derrotas.py                      # una revisión, sin enviar (muestra el aviso)
    python detectar_derrotas.py --cada 15 --enviar   # revisa cada 15 min y envía los avisos
    python detectar_derrotas.py --probar P1          # manda un aviso de prueba a P1
    python detectar_derrotas.py --ultima P1          # sesión de 30 min: aviso con la última derrota de P1
    python detectar_derrotas.py --ultima P1 --variante B
    python detectar_derrotas.py --ultima P1 --partida https://lichess.org/abcd1234   # una derrota concreta

Sin --enviar solo se revisa: no se envía nada ni se marca ninguna derrota como usada.
"""
import argparse
import base64
import csv
import json
import os
import shutil
import math
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

try:
    import chess
except ImportError:  # pragma: no cover
    sys.exit("Falta la librería python-chess:  python -m pip install --user chess")

AQUI = Path(__file__).parent
PARTICIPANTES = AQUI / "participantes.csv"
ESTADO = AQUI / "estado.json"
REGISTRO = AQUI / "registro_envios.csv"
SALIDA = AQUI / "mensajes_pendientes.txt"
CONFIG = AQUI / "config_local.json"

# Cambia esta dirección por la de la escena publicada (ver LEEME.md).
URL_ESCENA = "https://vidddda.github.io/Portafolio-193167/prototipo/escena.html"
# Si una derrota todavía no tiene análisis en Lichess, se espera hasta este tiempo antes de usarla
# (mientras tanto se puede pedir el análisis en la página de la partida).
# Si está Stockfish en la carpeta stockfish/, no se espera: la partida se analiza aquí.
ESPERA_ANALISIS_MIN = 30
_SF = sorted((AQUI / "stockfish").rglob("stockfish*.exe")) if (AQUI / "stockfish").exists() else []
STOCKFISH = (os.environ.get("ZAQORA_STOCKFISH") or (_SF[0] if _SF else None)
             or shutil.which("stockfish") or (Path("/usr/games/stockfish") if Path("/usr/games/stockfish").exists() else None))
SEGUNDOS_POR_POSICION = 0.08

# Narrador con IA gratuita (Cloudflare Workers AI). Si config_local.json no trae la cuenta y el token,
# la historia se arma con plantillas. Llama 3.1 8B se retiró el 20/11/2026; Mistral Small 3.1 (Apache 2.0)
# fue el que mejor escribió en español en la prueba del 24/11/2026.
MODELO_IA = "@cf/mistralai/mistral-small-3.1-24b-instruct"
RITMOS = {"ultraBullet": "de ultrabala", "bullet": "de bala", "blitz": "de blitz", "rapid": "rápida",
          "classical": "clásica", "correspondence": "por correspondencia"}
FINALES = {"mate": "con jaque mate", "resign": "con tu abandono", "outoftime": "por tiempo", "timeout": "por tiempo"}
TIPOS = {"Blunder": "un error grave", "Mistake": "un error", "Inaccuracy": "una imprecisión"}

# Patrón de error -> (villano, cómo lo cuenta la historia). Orden de prioridad al clasificar:
# tiempo > pieza sin defensa > apertura > final > medio juego.
PATRONES = {
    "tiempo": ("El Reloj de Arena", "te quedaste sin tiempo para pensar"),
    "colgada": ("El Carroñero", "dejaste piezas sin defensa"),
    "apertura": ("La Niebla", "te perdiste en la apertura"),
    "final": ("El Último Peón", "se te escapó el final"),
    "medio": ("La Horquilla Hambrienta", "te sorprendieron en el medio juego"),
}
HISTORIAL_PARTIDAS = 30        # partidas recientes que se revisan para la historia
HISTORIAL_DERROTAS = 12        # derrotas que se analizan como máximo (las más recientes)
MINIMO_PARTIDAS = 3            # con menos, no hay historia: se invita a jugar en Lichess
URL_LICHESS = "https://lichess.org/"
AGENTE = "Zaqora (prototipo escolar) https://vidddda.github.io/Portafolio-193167/"
URL_INICIO = URL_ESCENA.rsplit("/", 1)[0] + "/inicio.html"
DERROTAS_PRIMER_CONTACTO = 5
MENSAJES_PRIMER_CONTACTO = {
    "A": "Revisé tus últimas {n} derrotas y en cada una encontré dónde se te fue. Tus capítulos te esperan.",
    "B": "{n} derrotas, {n} capítulos. Yo ya sé dónde caíste. ¿Vienes?",
}
MENSAJES_HISTORIA = {
    "A": "Revisé tus últimas {total} partidas. Soy {villano}, y estuve en {veces} de tus derrotas. ¿Te atreves a volver a ellas?",
    "B": "{total} partidas, {derrotas} derrotas, y en {veces} estuve yo. Soy {villano}. ¿Vienes?",
}
MENSAJE_SIN_HISTORIA = "Todavía no tengo tu historia. Juega en Lichess: cuando pierdas, aquí empieza."

MENSAJES = {
    "A": "Esa partida dolió. Te vi caer con {color} en {n} jugadas, y yo estaba ahí. "
         "Soy {villano}. ¿Te atreves a volver a esa partida? {enlace}",
    "B": "Te estaba esperando. {n} jugadas con {color} y caíste justo donde yo sabía. "
         "¿Vienes a ver dónde fue? {enlace}",
    "C": "Esa partida dolió. Yo estaba ahí, en la jugada {jugada}: moviste {pieza} a {casilla}. "
         "Soy {villano}, y no es la primera vez que nos vemos. ¿Te atreves a volver? {enlace}",
}
PIEZAS = {chess.PAWN: "el peón", chess.KNIGHT: "el caballo", chess.BISHOP: "el alfil",
          chess.ROOK: "la torre", chess.QUEEN: "la dama", chess.KING: "el rey"}
SECUENCIAS = {"A primero": ["A", "B"], "B primero": ["B", "A"],
              "ABC": ["A", "B", "C"], "BCA": ["B", "C", "A"], "CAB": ["C", "A", "B"]}


def supabase_rest(metodo, ruta, cuerpo=None, prefer=None):
    """Llamada a la API de Supabase con la clave service_role. Devuelve el JSON o lanza HTTPError."""
    cfg = leer_config_local()
    if not cfg.get("supabase_url") or not cfg.get("supabase_service_key"):
        raise RuntimeError("sin Supabase")
    cab = {"apikey": cfg["supabase_service_key"], "Authorization": f"Bearer {cfg['supabase_service_key']}",
           "Content-Type": "application/json"}
    if prefer:
        cab["Prefer"] = prefer
    req = urllib.request.Request(f"{cfg['supabase_url']}/rest/v1/{ruta}", method=metodo, headers=cab,
                                 data=json.dumps(cuerpo).encode("utf-8") if cuerpo is not None else None)
    with urllib.request.urlopen(req, timeout=30) as r:
        texto = r.read().decode("utf-8")
    return json.loads(texto) if texto.strip() else None


def leer_participantes():
    """Participantes del CSV (prueba con alias P0…P5) y jugadores registrados al entrar con Lichess (J1, J2…).
    Si un usuario de Lichess está en los dos, manda el CSV."""
    filas = []
    if PARTICIPANTES.exists():
        # utf-8-sig tolera el BOM que agrega Excel; el separador puede ser coma o punto y coma.
        with PARTICIPANTES.open(encoding="utf-8-sig", newline="") as f:
            texto = f.read()
        if texto.strip():
            sep = ";" if texto.splitlines()[0].count(";") > texto.splitlines()[0].count(",") else ","
            filas = [dict({k.strip(): (v or "").strip() for k, v in r.items() if k}, origen="csv")
                     for r in csv.DictReader(texto.splitlines(), delimiter=sep) if (r.get("usuario_lichess") or "").strip()]
    try:
        registrados = supabase_rest("GET", "jugadores?select=id,usuario,alias&activo=eq.true&order=id") or []
    except Exception:
        registrados = []
    ya = {f["usuario_lichess"].lower() for f in filas}
    for j in registrados:
        if j["usuario"].lower() in ya:
            continue
        filas.append({"alias": j["alias"], "usuario_lichess": j["usuario"], "villano": "", "origen": "cuenta",
                      "orden": "A primero" if j["id"] % 2 else "B primero"})
    if not filas:
        print("No hay participantes todavía: ni participantes.csv ni jugadores registrados en Supabase.")
    return filas


_ESTADO_EN = None   # "supabase" o "archivo"


def leer_estado():
    global _ESTADO_EN
    try:
        filas = supabase_rest("GET", "estado_detector?select=alias,datos") or []
        _ESTADO_EN = "supabase"
        return {f["alias"]: f["datos"] for f in filas}
    except Exception:
        _ESTADO_EN = "archivo"
    if ESTADO.exists():
        return json.loads(ESTADO.read_text(encoding="utf-8"))
    return {}


def guardar_estado(estado):
    if _ESTADO_EN == "supabase":
        filas = [{"alias": a, "datos": d, "actualizado": datetime.now(timezone.utc).isoformat()} for a, d in estado.items()]
        if filas:
            try:
                supabase_rest("POST", "estado_detector", filas, "resolution=merge-duplicates,return=minimal")
                return
            except Exception as e:
                print(f"  No se pudo guardar el estado en Supabase ({e}); se guarda en estado.json.")
    ESTADO.write_text(json.dumps(estado, indent=2, ensure_ascii=False), encoding="utf-8")


def pedir_partidas(usuario, desde_ms, maximo=20):
    """Partidas terminadas desde `desde_ms`, con análisis si existe. Una petición a la vez."""
    params = urllib.parse.urlencode({"since": desde_ms, "max": maximo, "evals": "true", "opening": "true",
                                     "clocks": "true", "moves": "true", "pgnInJson": "false", "finished": "true"})
    req = urllib.request.Request(f"https://lichess.org/api/games/user/{usuario}?{params}",
                                 headers={"Accept": "application/x-ndjson", "User-Agent": AGENTE})
    for intento in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return [json.loads(l) for l in r.read().decode("utf-8").splitlines() if l.strip()]
        except urllib.error.HTTPError as e:
            if e.code == 429:  # Lichess pide esperar al menos un minuto
                print("  Lichess pidió esperar (429). Espero 60 s…")
                time.sleep(60)
                continue
            print(f"  Error {e.code} al consultar a {usuario}")
            return []
        except urllib.error.URLError as e:
            print(f"  Sin conexión ({e.reason}). Reintento en 10 s…")
            time.sleep(10)
    return []


MAX_ENCUENTROS = 3
_ANALISIS = {}   # (id de partida, color) -> (clave principal, encuentros); evita analizar dos veces


def analizar_partida(partida, color):
    """Devuelve (clave principal, encuentros).
    Con Stockfish: hasta 3 encuentros (los errores más grandes del jugador, separados por al menos
    2 jugadas), en el orden de la partida; la clave principal es el error más grande.
    Sin Stockfish: un solo encuentro con el análisis de Lichess, si alguien lo pidió."""
    llave = (partida.get("id"), color)
    if llave in _ANALISIS:
        return _ANALISIS[llave]
    resultado = (None, [])
    candidatos = analizar_local(partida, color) if STOCKFISH else []
    if candidatos:
        elegidos = []
        for c in candidatos:                      # de mayor a menor caída
            if len(elegidos) >= MAX_ENCUENTROS or (elegidos and c["caida"] < 5):
                break
            if any(abs(c["jugada"] - e["jugada"]) < 2 for e in elegidos):
                continue
            elegidos.append(c)
        resultado = (elegidos[0], sorted(elegidos, key=lambda c: c["jugada"]))
    else:
        clave = momento_clave_lichess(partida, color)
        resultado = (clave, [clave] if clave else [])
    _ANALISIS[llave] = resultado
    return resultado


def momento_clave(partida, color):
    """Posición antes del peor error del participante y la mejor jugada."""
    return analizar_partida(partida, color)[0]


def encuentros_de(partida, color):
    try:
        return analizar_partida(partida, color)[1]
    except Exception:
        return []


def win_pct(cp):
    """Probabilidad de ganar (0–100) a partir de centipeones, con la fórmula que usa Lichess."""
    return 50 + 50 * (2 / (1 + math.exp(-0.00368208 * cp)) - 1)


VALOR = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0}


def clasificar(partida, pos, i, caida, respuesta, despues):
    """Patrón del error de la jugada `i` (ply), con reglas simples y verificables."""
    relojes, inicial = partida.get("clocks") or [], (partida.get("clock") or {}).get("initial")
    if inicial and i < len(relojes) and relojes[i] / 100 < max(10, 0.1 * inicial):
        return "tiempo"
    if respuesta is not None and caida >= 20 and despues.is_capture(respuesta):
        capturada = despues.piece_at(respuesta.to_square)
        if capturada and VALOR.get(capturada.piece_type, 0) >= 3:
            return "colgada"
    if pos.fullmove_number <= 10:
        return "apertura"
    piezas = sum(1 for _, pz in pos.piece_map().items() if pz.piece_type not in (chess.PAWN, chess.KING))
    if piezas <= 4:
        return "final"
    return "medio"


def analizar_local(partida, color):
    """Analiza la partida con Stockfish y devuelve las jugadas del participante ordenadas por cuánto
    bajaron su probabilidad de ganar (misma escala que el PDS: ≥30 grave, ≥20 error, ≥10 imprecisión)."""
    import chess.engine
    if partida.get("variant", "standard") not in ("standard", "chess960", "fromPosition"):
        return []
    jugadas = partida.get("moves", "").split()
    tablero = chess.Board(partida["initialFen"], chess960=partida.get("variant") == "chess960") \
        if partida.get("initialFen") else chess.Board()
    lado = chess.WHITE if color == "white" else chess.BLACK
    motor = chess.engine.SimpleEngine.popen_uci(str(STOCKFISH))
    try:
        limite = chess.engine.Limit(time=SEGUNDOS_POR_POSICION)
        posiciones, movs, evals, mejores = [], [], [], []
        b = tablero.copy()
        for i in range(len(jugadas) + 1):
            info = motor.analyse(b, limite)
            evals.append(info["score"].pov(lado).score(mate_score=10000))
            mejores.append(info.get("pv", [None])[0])
            posiciones.append(b.copy())
            if i < len(jugadas):
                mv = b.parse_san(jugadas[i])
                movs.append(mv)
                b.push(mv)
    finally:
        motor.quit()
    candidatos = []
    for i, mv in enumerate(movs):
        if posiciones[i].turn != lado or mejores[i] is None or mejores[i] == mv:
            continue
        caida = win_pct(evals[i]) - win_pct(evals[i + 1])
        pos = posiciones[i]
        pieza = pos.piece_at(mv.from_square)
        tipo = "Blunder" if caida >= 30 else "Mistake" if caida >= 20 else "Inaccuracy" if caida >= 10 else None
        candidatos.append({"fen": pos.fen(), "sol": mejores[i].uci(), "jugada": pos.fullmove_number,
                           "pieza": PIEZAS.get(pieza.piece_type, "la pieza") if pieza else "la pieza",
                           "casilla": chess.square_name(mv.to_square), "jugada_san": pos.san(mv),
                           "mejor_san": pos.san(mejores[i]), "tipo": tipo, "caida": round(caida),
                           "fuente": "stockfish", "partida": partida.get("id"),
                           "color": "w" if color == "white" else "b",
                           "patron": clasificar(partida, pos, i, caida, mejores[i + 1], posiciones[i + 1])})
    return sorted(candidatos, key=lambda c: -c["caida"])


def momento_clave_lichess(partida, color):
    """Lo mismo, con el análisis que Lichess ya tiene (si alguien lo pidió)."""
    jugadas = partida.get("moves", "").split()
    analisis = partida.get("analysis")
    if not analisis:
        return None
    lado = 0 if color == "white" else 1
    prioridad = {"Blunder": 3, "Mistake": 2, "Inaccuracy": 1}
    mejor, peor = None, 0
    for i, a in enumerate(analisis):
        if i % 2 != lado or "best" not in a or "judgment" not in a:
            continue
        peso = prioridad.get(a["judgment"].get("name"), 0)
        if peso > peor:
            peor, mejor = peso, i
    if mejor is None:
        return None
    tablero = chess.Board(partida.get("initialFen", chess.STARTING_FEN)) if partida.get("initialFen") else chess.Board()
    for san in jugadas[:mejor]:
        tablero.push_san(san)
    fen = tablero.fen()
    jugada_hecha = tablero.parse_san(jugadas[mejor])
    pieza = tablero.piece_at(jugada_hecha.from_square)
    try:
        mejor_san = tablero.san(chess.Move.from_uci(analisis[mejor]["best"]))
    except Exception:
        mejor_san = ""
    return {
        "fen": fen,
        "sol": analisis[mejor]["best"],
        "jugada": tablero.fullmove_number,
        "pieza": PIEZAS.get(pieza.piece_type, "la pieza") if pieza else "la pieza",
        "casilla": chess.square_name(jugada_hecha.to_square),
        "jugada_san": tablero.san(jugada_hecha),
        "mejor_san": mejor_san,
        "tipo": analisis[mejor]["judgment"].get("name"),
        "fuente": "lichess",
    }


def construir_historia(p, variante="A"):
    """Capítulo con las últimas partidas del participante. Devuelve (item, None) o (None, motivo)."""
    if not STOCKFISH:
        return None, "Falta Stockfish en la carpeta stockfish/."
    usuario = p["usuario_lichess"].strip()
    partidas = [g for g in pedir_partidas(usuario, 0, HISTORIAL_PARTIDAS)
                if g.get("variant", "standard") in ("standard", "chess960", "fromPosition")]
    if len(partidas) < MINIMO_PARTIDAS:
        return None, f"solo tiene {len(partidas)} partidas"
    ganadas = derrotas = tablas = 0
    perdidas = []
    ritmos = {}
    for g in partidas:
        pl = g.get("players", {})
        color = "white" if pl.get("white", {}).get("user", {}).get("name", "").lower() == usuario.lower() else "black"
        ritmos[g.get("speed", "")] = ritmos.get(g.get("speed", ""), 0) + 1
        if not g.get("winner"):
            tablas += 1
        elif g["winner"] == color:
            ganadas += 1
        else:
            derrotas += 1
            perdidas.append((g, color))
    if not perdidas:
        return None, "no tiene derrotas recientes"
    # El peor error de cada derrota (las más recientes primero)
    errores = []
    for g, color in perdidas[:HISTORIAL_DERROTAS]:
        try:
            cands = analizar_local(g, color)
        except Exception:
            continue
        if cands:
            errores.append(dict(cands[0], fin=datetime.fromtimestamp(g.get("lastMoveAt", 0) / 1000)))
    if not errores:
        return None, "no se pudo analizar ninguna derrota"
    conteo = {}
    for e in errores:
        conteo[e["patron"]] = conteo.get(e["patron"], 0) + 1
    patron = max(conteo, key=lambda k: (conteo[k], sum(e["caida"] for e in errores if e["patron"] == k)))
    villano, descripcion = PATRONES[patron]
    del_patron = sorted([e for e in errores if e["patron"] == patron], key=lambda e: -e["caida"])
    resto = sorted([e for e in errores if e["patron"] != patron], key=lambda e: -e["caida"])
    elegidos = (del_patron + resto)[:MAX_ENCUENTROS]
    elegidos.sort(key=lambda e: e["fin"])                       # en el orden en que se jugaron
    principal = max(elegidos, key=lambda e: e["caida"])
    ritmo = max(ritmos, key=ritmos.get) if ritmos else ""
    item = {"alias": p["alias"], "variante": variante, "partida": "historia", "modo": "historia",
            "fin": datetime.now(), "n": len(partidas),
            "color": "blancas" if principal["color"] == "w" else "negras",
            "villano": villano, "clave": principal, "encuentros": elegidos, "ritmo": ritmo,
            "apertura": "", "final": "",
            "resumen": {"partidas": len(partidas), "ganadas": ganadas, "perdidas": derrotas, "tablas": tablas,
                        "ritmo_mas_jugado": RITMOS.get(ritmo, ""), "patron": descripcion,
                        "derrotas_con_ese_patron": conteo[patron], "derrotas_analizadas": len(errores)}}
    return item, None


VARIABLES = {"supabase_url": "ZAQORA_SUPABASE_URL", "supabase_service_key": "ZAQORA_SUPABASE_SERVICE_KEY",
             "vapid_contacto": "ZAQORA_VAPID_CONTACTO", "vapid_privada": "ZAQORA_VAPID_PRIVADA_ARCHIVO",
             "cloudflare_account_id": "CLOUDFLARE_ACCOUNT_ID", "cloudflare_token": "CLOUDFLARE_TOKEN"}


def leer_config_local():
    """config_local.json (en tu laptop) y, encima, las variables de entorno (en GitHub Actions)."""
    try:
        cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    except Exception:
        cfg = {}
    for clave, variable in VARIABLES.items():
        if os.environ.get(variable):
            cfg[clave] = os.environ[variable]
    return cfg


NUM_PRUEBAS = {1: "uno de esos momentos", 2: "dos momentos de esa partida", 3: "tres momentos de esa partida"}


def historia_plantilla(item, encuentros):
    if item.get("resumen"):
        r = item["resumen"]
        momentos = NUM_PRUEBAS.get(len(encuentros), "uno de esos momentos").replace("de esa partida", "de esas partidas")
        tablas = f" y empataste {r['tablas']}" if r["tablas"] else ""
        ritmo = f" Juegas sobre todo partidas {r['ritmo_mas_jugado']}." if r["ritmo_mas_jugado"] else ""
        ritmo = ritmo.replace("partidas de ", "")
        p1 = f"Revisé tus últimas {r['partidas']} partidas: ganaste {r['ganadas']}, perdiste {r['perdidas']}{tablas}.{ritmo}"
        p2 = f"En {r['derrotas_con_ese_patron']} de tus derrotas {r['patron']}. Ahí aparezco yo: soy {item['villano']}."
        if item["variante"] == "B":
            p3 = f"Siempre caes en lo mismo. Te espero en {momentos}: a ver si esta vez sí."
        else:
            p3 = f"Sé que esas partidas dolieron. Si crees que puedes cambiar lo que pasó, te espero en {momentos}."
        return [p1, p2, p3]
    c = item["clave"] or {}
    ritmo = RITMOS.get(item.get("ritmo"), "")
    apertura = f", en la apertura «{item['apertura']}»" if item.get("apertura") else ""
    p1 = f"Jugaste con {item['color']} una partida {ritmo} de {item['n']} jugadas{apertura}.".replace("  ", " ")
    if c:
        tipo = TIPOS.get(c.get("tipo"), "el momento en que la partida cambió")
        p2 = f"En la jugada {c['jugada']} moviste {c['pieza']} a {c['casilla']}. Fue {tipo}, y desde ahí la partida fue mía."
    else:
        p2 = "Hubo un momento en que la partida cambió de dueño. Yo lo vi."
    final = FINALES.get(item.get("final"), "")
    pruebas = NUM_PRUEBAS.get(len(encuentros), "una prueba")
    if item["variante"] == "B":
        p3 = f"Terminó {final}. Sabía exactamente dónde ibas a caer. Te espero en {pruebas}: a ver si esta vez sí."
    else:
        p3 = f"Terminó {final}. Sé que dolió. Si crees que puedes cambiar lo que pasó, te espero en {pruebas}."
    return [p1, p2, p3.replace("Terminó .", "Terminó.")]


def dialogos_plantilla(item, encuentros):
    """Por encuentro: el villano reta (antes) y reacciona (despues); el consejero de tu bando guía (consejo).
    El villano nunca da pistas ni dice qué hacer."""
    burla = item["variante"] == "B"
    consejos = ["Aquí había algo mejor. Encuéntralo: toca una pieza y luego su casilla.",
                "Tranquilo, este momento lo podemos cambiar. Busca una jugada mejor.",
                "Este es el momento decisivo. Respira y encuentra la jugada."]
    salida = []
    for i, c in enumerate(encuentros):
        ultimo = i == len(encuentros) - 1
        pieza = c["pieza"]
        Pieza = pieza[:1].upper() + pieza[1:]
        j, cas = c["jugada"], c["casilla"]
        if burla:
            antes = [f"Jugada {j}. {Pieza} a {cas}. Yo ya sabía que caerías.",
                     f"Jugada {j}. Moviste {pieza} a {cas} y me reí.",
                     f"Jugada {j}. {Pieza} a {cas}: mi trampa favorita. Encuéntrala si puedes."][i % 3]
            despues = "…Hmph. Esta vez no. Nos volveremos a ver." if ultimo else "Suerte. La siguiente no será tan fácil."
        else:
            antes = [f"Jugada {j}. Moviste {pieza} a {cas}, justo donde yo quería.",
                     f"Jugada {j}. {Pieza} a {cas}… ahí la partida empezó a ser mía.",
                     f"Jugada {j}. {Pieza} a {cas}. Ahí te gané."][i % 3]
            despues = "…Esta vez no. Nos volveremos a ver." if ultimo else "Una no basta. Te espero en la siguiente."
        salida.append({"antes": antes, "consejo": consejos[i % 3] if len(encuentros) > 1 or i else consejos[0],
                       "despues": despues})
    return salida


def historia_ia(item, encuentros, cfg):
    """Pide a Cloudflare Workers AI la historia y los diálogos de cada encuentro.
    Devuelve {"historia": [...], "encuentros": [{"antes", "despues"}, ...]} o None si falla o no pasa el validador."""
    cuenta, token = cfg.get("cloudflare_account_id"), cfg.get("cloudflare_token")
    if not cuenta or not token or not encuentros:
        return None
    c = item["clave"] or encuentros[0]
    hechos = {"color_del_jugador": item["color"], "ritmo": RITMOS.get(item.get("ritmo"), ""),
              "jugadas_totales": item["n"], "apertura": item.get("apertura") or "",
              "como_termino": FINALES.get(item.get("final"), ""),
              "error_principal": {"jugada": c["jugada"], "pieza": c["pieza"], "casilla": c["casilla"],
                                  "gravedad": TIPOS.get(c.get("tipo"), "el momento en que la partida cambió")},
              "encuentros": [{"jugada": e["jugada"], "pieza_que_movio": e["pieza"], "casilla_destino": e["casilla"],
                              "gravedad": TIPOS.get(e.get("tipo"), "un detalle")} for e in encuentros]}
    if item.get("resumen"):
        hechos = {"resumen_de_sus_ultimas_partidas": {k: v for k, v in item["resumen"].items()
                                                      if k != "derrotas_analizadas"},
                  "encuentros": hechos["encuentros"]}
    tono = ("Te burlas con elegancia, sin insultos ni groserías." if item["variante"] == "B"
            else "Primero reconoces que la derrota dolió; nunca te burlas ni regañas.")
    n = len(encuentros)
    sistema = (f"Eres {item['villano']}, el villano de un juego de ajedrez que encarna el error del jugador. "
               "Hablas con el jugador en segunda persona, en español de México. El jugador hizo todas las jugadas: di 'moviste', nunca 'moví'. Hablas de ti en primera persona y nunca dices tu propio nombre. " + tono + " "
               "Eres el antagonista: retas, presumes y reaccionas, pero NUNCA das pistas, consejos ni instrucciones. "
               "En la escena también habla el consejero del bando del jugador, un aliado que lo anima y le dice qué hacer. "
               "Escribe: (a) 'historia': exactamente 3 párrafos tuyos de 1 o 2 frases (máximo 200 caracteres cada uno): "
               + ("cómo le ha ido en sus últimas partidas (usa el resumen), el error que más repite (tú eres ese error) "
                  "y un reto a volver a esos momentos; " if item.get("resumen") else
                  "cómo empezó la partida, el error principal y un reto a volver a esos momentos; ") +
               f"(b) 'encuentros': exactamente {n} objetos, uno por encuentro y en el mismo orden, cada uno con "
               "'antes' (tú, al mostrar la posición: menciona la jugada, la pieza y la casilla de ese encuentro y presume "
               "o reta; sin consejos; máximo 140 caracteres), 'consejo' (el consejero, en segunda persona: anima y pide "
               "buscar una jugada mejor, sin decir cuál ni qué pieza; máximo 120 caracteres) y 'despues' (tú, cuando el "
               "jugador lo resuelve: te molesta o lo minimizas; máximo 100 caracteres; en el último, despídete hasta la "
               "próxima derrota). "
               "Usa SOLO los hechos que te dan. No inventes jugadas, casillas, piezas, nombres ni números. "
               "Nadie dice cuál era la jugada correcta. "
               'Responde solo con JSON: {"historia": ["...", "...", "..."], '
               '"encuentros": [{"antes": "...", "consejo": "...", "despues": "..."}]}')
    cuerpo = json.dumps({"messages": [{"role": "system", "content": sistema},
                                      {"role": "user", "content": json.dumps(hechos, ensure_ascii=False)}],
                         "max_tokens": 900, "temperature": 0.7}).encode("utf-8")
    modelo = cfg.get("cloudflare_modelo", MODELO_IA)
    req = urllib.request.Request(f"https://api.cloudflare.com/client/v4/accounts/{cuenta}/ai/run/{modelo}",
                                 data=cuerpo, headers={"Authorization": f"Bearer {token}",
                                                       "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            resp = json.loads(r.read().decode("utf-8")).get("result", {}).get("response")
        if isinstance(resp, str):
            inicio, fin = resp.find("{"), resp.rfind("}")
            resp = json.loads(resp[inicio:fin + 1])
    except Exception as e:
        print(f"  La IA no respondió ({e}); se usa la plantilla.")
        return None
    return resp if validar_capitulo(resp, encuentros) else None


def validar_capitulo(resp, encuentros):
    """El villano no puede inventar casillas ni revelar ninguna solución; formato y largo fijos."""
    import re
    if not isinstance(resp, dict):
        return False
    historia, dialogos = resp.get("historia"), resp.get("encuentros")
    if not isinstance(historia, list) or len(historia) != 3 or \
            not all(isinstance(p, str) and 10 < len(p) <= 260 for p in historia):
        print("  La historia de la IA no tiene el formato esperado; se usa la plantilla.")
        return False
    if not isinstance(dialogos, list) or len(dialogos) != len(encuentros) or not all(
            isinstance(d, dict) and isinstance(d.get("antes"), str) and isinstance(d.get("despues"), str)
            and isinstance(d.get("consejo"), str) and 5 < len(d["antes"]) <= 200 and 5 < len(d["consejo"]) <= 180
            and 2 < len(d["despues"]) <= 160 for d in dialogos):
        print("  Los diálogos de la IA no tienen el formato esperado; se usa la plantilla.")
        return False
    texto = " ".join(historia + [d["antes"] + " " + d["consejo"] + " " + d["despues"] for d in dialogos])
    permitidas = {e["casilla"] for e in encuentros}
    casillas = set(re.findall(r"\b[a-h][1-8]\b", texto))
    if casillas - permitidas:
        print(f"  La IA mencionó casillas que no están en los hechos ({', '.join(sorted(casillas - permitidas))}); se usa la plantilla.")
        return False
    for e in encuentros:
        if e.get("mejor_san") and e["mejor_san"].rstrip("+#") in texto:
            print("  La IA reveló una jugada correcta; se usa la plantilla.")
            return False
    return True



def revisar(participantes, estado):
    nuevas = []
    for p in participantes:
        alias, usuario = p["alias"].strip(), p["usuario_lichess"].strip()
        info = estado.setdefault(alias, {"vistas": [], "enviados": 0,
                                         "desde": int(datetime.now(timezone.utc).timestamp() * 1000)})
        partidas = pedir_partidas(usuario, info["desde"])
        time.sleep(2)  # una petición a la vez, con pausa
        for g in partidas:
            if g["id"] in info["vistas"]:
                continue
            jugadores = g.get("players", {})
            color = "white" if jugadores.get("white", {}).get("user", {}).get("name", "").lower() == usuario.lower() else "black"
            ganador = g.get("winner")
            if not ganador or ganador == color:
                info["vistas"].append(g["id"])
                continue  # solo derrotas
            try:
                clave = momento_clave(g, color)
            except Exception:  # variantes raras o PGN inesperado: se elige el momento a mano
                clave = None
            minutos = (time.time() * 1000 - g.get("lastMoveAt", g.get("createdAt", 0))) / 60000
            if clave is None and minutos < ESPERA_ANALISIS_MIN and not STOCKFISH:
                print(f"  {alias}: la derrota {g['id']} todavía no tiene análisis en Lichess. "
                      f"Pídelo en https://lichess.org/{g['id']}; se vuelve a revisar en la siguiente vuelta "
                      f"(espera máxima: {ESPERA_ANALISIS_MIN} min).")
                continue  # no se marca como vista: se reintenta
            info["vistas"].append(g["id"])
            secuencia = SECUENCIAS.get(p.get("orden", "A primero").strip(), ["A", "B"])
            if p.get("origen") == "csv" and info["enviados"] >= len(secuencia):
                print(f"  {alias}: ya recibió todas sus variantes; esta derrota no se usa.")
                continue
            variante = secuencia[info["enviados"] % len(secuencia)]
            n = math.ceil(len(g.get("moves", "").split()) / 2)
            fin = datetime.fromtimestamp(g.get("lastMoveAt", g.get("createdAt", 0)) / 1000)
            villano = p.get("villano", "").strip() or villano_de(clave)
            nuevas.append({"alias": alias, "variante": variante, "partida": g["id"], "fin": fin,
                           "n": n, "color": "blancas" if color == "white" else "negras",
                           "villano": villano, "clave": clave, **datos_partida(g), "encuentros": encuentros_de(g, color)})
    return nuevas


def ultima_derrota(p):
    """Para la sesión de 30 minutos: la derrota más reciente (de las últimas 20 partidas) que ya tenga
    análisis en Lichess. Devuelve (partida, color, clave) o (None, partida_sin_analisis, None)."""
    usuario = p["usuario_lichess"].strip()
    sin_analisis = None
    for g in pedir_partidas(usuario, 0):   # Lichess las entrega de la más nueva a la más vieja
        jugadores = g.get("players", {})
        color = "white" if jugadores.get("white", {}).get("user", {}).get("name", "").lower() == usuario.lower() else "black"
        if not g.get("winner") or g["winner"] == color:
            continue
        try:
            clave = momento_clave(g, color)
        except Exception:
            clave = None
        if clave:
            return g, color, clave
        sin_analisis = sin_analisis or g
    return None, sin_analisis, None


def pedir_partida(partida_id):
    """Una partida concreta de Lichess, con análisis si existe."""
    params = urllib.parse.urlencode({"evals": "true", "opening": "true", "moves": "true", "pgnInJson": "false"})
    req = urllib.request.Request(f"https://lichess.org/game/export/{partida_id}?{params}",
                                 headers={"Accept": "application/json", "User-Agent": AGENTE})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        sys.exit(f"Lichess respondió {e.code} al pedir la partida {partida_id}. Revisa el id.")


def sesion(alias, variante_pedida, partida_id=None):
    p = next((x for x in leer_participantes() if x["alias"].strip() == alias), None)
    if not p or not p.get("usuario_lichess", "").strip():
        sys.exit(f"{alias} no está en participantes.csv o no tiene usuario de Lichess.")
    cfg = config()
    if partida_id:
        # acepta el id o el enlace completo (también …/black o con #jugada)
        partes = [x for x in partida_id.split("#")[0].replace("https://", "").split("/") if x and "lichess.org" not in x]
        partida_id = partes[0][:8] if partes else partida_id
        g = pedir_partida(partida_id)
        usuario = p["usuario_lichess"].strip().lower()
        jugadores = g.get("players", {})
        if usuario == jugadores.get("white", {}).get("user", {}).get("name", "").lower():
            color = "white"
        elif usuario == jugadores.get("black", {}).get("user", {}).get("name", "").lower():
            color = "black"
        else:
            sys.exit(f"{alias} no jugó la partida {partida_id}.")
        if not g.get("winner") or g["winner"] == color:
            sys.exit(f"La partida {partida_id} no es una derrota de {alias}.")
        try:
            clave = momento_clave(g, color)
        except Exception:
            clave = None
        if not clave:
            sys.exit(f"La partida {partida_id} no tiene análisis (o no hay un error marcado). Pide el análisis en "
                     f"https://lichess.org/{partida_id} y vuelve a correr este comando.")
    else:
        g, color, clave = ultima_derrota(p)
    if not g:
        if color:  # aquí 'color' trae la derrota sin análisis
            sys.exit(f"Ninguna derrota reciente de {alias} tiene análisis. Pide el análisis en "
                     f"https://lichess.org/{color['id']} y vuelve a correr este comando.")
        sys.exit(f"{alias} no tiene derrotas en sus últimas 20 partidas.")
    secuencia = SECUENCIAS.get(p.get("orden", "A primero").strip(), ["A", "B"])
    variante = variante_pedida or secuencia[0]
    item = {"alias": alias, "variante": variante, "partida": g["id"],
            "fin": datetime.fromtimestamp(g.get("lastMoveAt", g.get("createdAt", 0)) / 1000),
            "n": math.ceil(len(g.get("moves", "").split()) / 2),
            "color": "blancas" if color == "white" else "negras",
            "villano": p.get("villano", "").strip() or "La Horquilla Hambrienta", "clave": clave,
            **datos_partida(g), "encuentros": encuentros_de(g, color)}
    enlace, _, aviso = armar(item, con_ia=True)
    err = enviar_push(alias, item["villano"], aviso, enlace, g["id"], cfg)
    enviado = "no" if err else f"{datetime.now():%d/%m/%Y %H:%M}"
    if err is None:
        guardar_capitulo(item, enlace, cfg)
    print(err or f"Aviso de sesión enviado a {alias} (variante {variante}, partida del {item['fin']:%d/%m %H:%M}).\n"
                 f"{item['villano']} — {aviso}\nEscena: {enlace}")
    nuevo = not REGISTRO.exists()
    with REGISTRO.open("a", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow(["participante", "variante", "partida", "fin_de_la_partida", "detectada",
                        "con_analisis", "aviso_enviado"])
        w.writerow([alias, f"{variante} (sesión)", g["id"], f"{item['fin']:%d/%m/%Y %H:%M}",
                    f"{datetime.now():%d/%m/%Y %H:%M}", "sí", enviado])


def capitulos_primer_contacto(p, variante):
    """Un capítulo por cada una de las últimas derrotas (hasta 5), del más viejo al más nuevo."""
    usuario = p["usuario_lichess"].strip()
    partidas = [g for g in pedir_partidas(usuario, 0, HISTORIAL_PARTIDAS)
                if g.get("variant", "standard") in ("standard", "chess960", "fromPosition")]
    derrotas = []
    for g in partidas:
        pl = g.get("players", {})
        color = "white" if pl.get("white", {}).get("user", {}).get("name", "").lower() == usuario.lower() else "black"
        if g.get("winner") and g["winner"] != color:
            derrotas.append((g, color))
        if len(derrotas) >= DERROTAS_PRIMER_CONTACTO:
            break
    items = []
    for g, color in reversed(derrotas):
        try:
            clave = momento_clave(g, color)
        except Exception:
            clave = None
        if not clave:
            continue
        items.append({"alias": p["alias"], "variante": variante, "partida": g["id"],
                      "fin": datetime.fromtimestamp(g.get("lastMoveAt", g.get("createdAt", 0)) / 1000),
                      "n": math.ceil(len(g.get("moves", "").split()) / 2),
                      "color": "blancas" if color == "white" else "negras",
                      "villano": p.get("villano", "").strip() or villano_de(clave), "clave": clave,
                      **datos_partida(g), "encuentros": encuentros_de(g, color)})
    return items


def enviar_historia(alias, cfg, variante=None, solo_mostrar=False):
    """Primer contacto: un capítulo por cada una de las últimas 5 derrotas y UN solo aviso.
    Con cuenta de Lichess el aviso abre Inicio (ahí están los 5); con CSV abre el más reciente.
    Sin derrotas, invita a jugar en Lichess. Devuelve True si se envió (o se mostró) algo."""
    p = next((x for x in leer_participantes() if x["alias"].strip() == alias), None)
    if not p:
        print(f"{alias} no está registrado (ni en participantes.csv ni en Supabase).")
        return False
    if not STOCKFISH:
        print("  Falta Stockfish: no se puede analizar.")
        return False
    secuencia = SECUENCIAS.get(p.get("orden", "A primero").strip(), ["A", "B"])
    variante = variante or secuencia[0]
    print(f"  {alias}: analizando sus últimas {DERROTAS_PRIMER_CONTACTO} derrotas…")
    items = capitulos_primer_contacto(p, variante)
    if not items:
        enlace = f"{URL_ESCENA}?{urllib.parse.urlencode({'p': alias, 'modo': 'nueva'})}"
        print(f"  {alias}: sin derrotas recientes. Se le invita a jugar en Lichess.\n  {MENSAJE_SIN_HISTORIA}\n  Escena: {enlace}")
        if solo_mostrar:
            return True
        err = enviar_push(alias, "Zaqora", MENSAJE_SIN_HISTORIA, enlace, "historia", cfg)
        print("  " + (err or "Invitación enviada."))
        return err is None
    enlaces = []
    for item in items:
        enlace, _, _ = armar(item, con_ia=True)
        enlaces.append(enlace)
        print(f"  · {item['fin']:%d/%m} {item['villano']} ({item['historia_fuente']}, "
              f"{len(item['encuentros'])} encuentros) https://lichess.org/{item['partida']}")
    aviso = MENSAJES_PRIMER_CONTACTO["B" if variante == "B" else "A"].format(n=len(items))
    destino = f"{URL_INICIO}?{urllib.parse.urlencode({'p': alias})}" if p.get("origen") == "cuenta" else enlaces[-1]
    print(f"  Aviso: {aviso}\n  Abre: {destino}")
    if solo_mostrar:
        return True
    for item, enlace in zip(items, enlaces):
        guardar_capitulo(item, enlace, cfg)
    err = enviar_push(alias, "Zaqora", aviso, destino, "historia", cfg)
    print("  " + (err or f"Primer contacto enviado ({len(items)} capítulos)."))
    return err is None


def id_capitulo(enlace):
    """El mismo identificador que calcula la escena (hash FNV-1a del parámetro c)."""
    q = urllib.parse.parse_qs(urllib.parse.urlparse(enlace).query)
    texto = (q.get("c") or [None])[0] or f"{(q.get('fen') or [''])[0]}|{(q.get('sol') or [''])[0]}"
    h = 2166136261
    for ch in texto:
        h ^= ord(ch)
        h = (h * 16777619) & 0xFFFFFFFF
    return str(h)


def guardar_capitulo(item, enlace, cfg):
    """Guarda en Supabase el capítulo enviado, ligado al usuario de Lichess, para que el jugador
    lo vea en Inicio al entrar con Lichess. Si ya existe, no lo toca (conserva el avance)."""
    p = next((x for x in leer_participantes() if x["alias"].strip() == item["alias"]), None)
    if not p or not cfg:
        return
    fila = {"id": id_capitulo(enlace), "usuario": p["usuario_lichess"].strip().lower(), "alias": item["alias"],
            "villano": item["villano"], "modo": "historia" if item.get("resumen") else "derrota",
            "total": max(1, len(item.get("encuentros") or [])), "enlace": urllib.parse.urlparse(enlace).query}
    req = urllib.request.Request(f"{cfg['supabase_url']}/rest/v1/capitulos", method="POST",
                                 data=json.dumps(fila).encode("utf-8"),
                                 headers={"apikey": cfg["supabase_service_key"],
                                          "Authorization": f"Bearer {cfg['supabase_service_key']}",
                                          "Content-Type": "application/json",
                                          "Prefer": "resolution=ignore-duplicates,return=minimal"})
    try:
        urllib.request.urlopen(req, timeout=30).close()
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("  (La tabla capitulos no existe todavía: el capítulo no quedará en Inicio al entrar con Lichess.)")
        else:
            print(f"  No se pudo guardar el capítulo en Supabase: {e.code} {e.read().decode('utf-8', 'replace')[:200]}")
    except Exception as e:
        print(f"  No se pudo guardar el capítulo en Supabase: {e}")


def config():
    cfg = leer_config_local()
    if not cfg:
        sys.exit("Falta config_local.json o las variables de entorno ZAQORA_* (ver LEEME.md).")
    for k in ("supabase_url", "supabase_service_key", "vapid_contacto"):
        if not cfg.get(k) or "CAMBIA" in cfg.get(k, ""):
            sys.exit(f"Llena '{k}' en config_local.json antes de enviar avisos.")
    # La clave debe ser la service_role: con la anon, Supabase no deja leer las suscripciones
    # y el script creería que nadie activó los avisos.
    try:
        import base64
        carga = cfg["supabase_service_key"].split(".")[1]
        carga += "=" * (-len(carga) % 4)
        rol = json.loads(base64.urlsafe_b64decode(carga)).get("role")
    except Exception:
        rol = None
    if rol and rol != "service_role":
        sys.exit(f"La clave en 'supabase_service_key' es de rol '{rol}'. Pega la clave service_role "
                 "(Project Settings → API), no la anon.")
    return cfg


def suscripcion_de(alias, cfg):
    """Última suscripción push del participante (se lee con la clave service_role)."""
    q = urllib.parse.urlencode({"participante": f"eq.{alias}", "order": "creado.desc", "limit": 1,
                                "select": "suscripcion"})
    req = urllib.request.Request(f"{cfg['supabase_url']}/rest/v1/suscripciones?{q}",
                                 headers={"apikey": cfg["supabase_service_key"],
                                          "Authorization": f"Bearer {cfg['supabase_service_key']}"})
    with urllib.request.urlopen(req, timeout=30) as r:
        filas = json.loads(r.read().decode("utf-8"))
    return filas[0]["suscripcion"] if filas else None


def enviar_push(alias, titulo, cuerpo, url, etiqueta, cfg):
    """Envía el aviso; devuelve None si salió bien o el texto del error."""
    try:
        from pywebpush import webpush, WebPushException
    except ImportError:
        sys.exit("Falta pywebpush:  python -m pip install --user pywebpush")
    sub = suscripcion_de(alias, cfg)
    if not sub:
        return f"{alias} no ha activado los avisos (no hay suscripción)."
    try:
        webpush(subscription_info=sub,
                data=json.dumps({"titulo": titulo, "cuerpo": cuerpo, "url": url, "etiqueta": etiqueta}),
                vapid_private_key=str(AQUI / cfg.get("vapid_privada", "vapid_privada.pem")),
                vapid_claims={"sub": cfg["vapid_contacto"]}, ttl=3600)
        return None
    except (WebPushException, Exception) as e:  # también errores de red
        return f"No se pudo enviar a {alias}: {e}"


def villano_de(clave):
    """El villano del patrón del error principal (bestiario); si no hay patrón, La Horquilla Hambrienta."""
    return PATRONES.get((clave or {}).get("patron"), ("La Horquilla Hambrienta", ""))[0]


def datos_partida(g):
    """Hechos de la partida que usa la historia del villano."""
    return {"apertura": (g.get("opening") or {}).get("name", ""), "ritmo": g.get("speed", ""),
            "final": g.get("status", "")}


def armar(item, con_ia=False):
    c = item["clave"]
    params = {"p": item["alias"], "v": item["variante"], "villano": item["villano"],
              "color": "w" if item["color"] == "blancas" else "b"}
    encuentros = item.get("encuentros") or ([c] if c else [])
    # El capítulo (historia + encuentros con diálogos) viaja en el enlace como base64url de un JSON:
    # {"h": [párrafos], "e": [{"f": FEN, "s": solución UCI, "j": jugada, "a": antes, "d": después}]}
    capitulo = historia_ia(item, encuentros, leer_config_local()) if con_ia else None
    fuente = "ia" if capitulo else "plantilla"
    capitulo = capitulo or {"historia": historia_plantilla(item, encuentros),
                            "encuentros": dialogos_plantilla(item, encuentros)}
    item["historia"], item["dialogos"], item["historia_fuente"] = capitulo["historia"], capitulo["encuentros"], fuente
    paquete = {"h": capitulo["historia"],
               "e": [{"f": e["fen"], "s": e["sol"], "j": e["jugada"], "a": d["antes"], "k": d.get("consejo", ""),
                      "d": d["despues"], "c": e.get("color", params["color"])}
                     for e, d in zip(encuentros, capitulo["encuentros"])]}
    params["c"] = base64.urlsafe_b64encode(json.dumps(paquete, ensure_ascii=False, separators=(",", ":"))
                                           .encode("utf-8")).decode().rstrip("=")
    params["hf"] = fuente
    if item.get("resumen"):
        params["m"] = "h"          # capítulo hecho con el historial (Inicio lo distingue)
    enlace = f"{URL_ESCENA}?{urllib.parse.urlencode(params)}"
    datos = {"color": item["color"], "n": item["n"], "villano": item["villano"], "enlace": "{ENLACE CORTO}",
             "jugada": c["jugada"] if c else "?", "pieza": c["pieza"] if c else "?", "casilla": c["casilla"] if c else "?"}
    if item.get("resumen"):
        r = item["resumen"]
        mensaje = MENSAJES_HISTORIA["B" if item["variante"] == "B" else "A"].format(
            total=r["partidas"], derrotas=r["perdidas"], veces=r["derrotas_con_ese_patron"], villano=item["villano"]) + " {ENLACE CORTO}"
    else:
        mensaje = MENSAJES[item["variante"]].format(**datos)
    # El aviso push no lleva enlace: tocarlo abre la escena.
    aviso = mensaje.rsplit(" {ENLACE CORTO}", 1)[0].rstrip(": ").rstrip()
    if not aviso.endswith(("?", ".", "!")):
        aviso += "."
    return enlace, mensaje, aviso


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--cada", type=float, default=0, help="minutos entre revisiones (0 = una sola vez)")
    ap.add_argument("--enviar", action="store_true", help="envía los avisos push (sin esto solo los muestra)")
    ap.add_argument("--probar", metavar="ALIAS", help="envía un aviso de prueba a ese participante y termina")
    ap.add_argument("--ultima", metavar="ALIAS",
                    help="sesión de prueba: envía el aviso con la última derrota analizada de ese participante")
    ap.add_argument("--variante", choices=["A", "B", "C"], help="con --ultima: variante del mensaje")
    ap.add_argument("--partida", metavar="ID", help="con --ultima: envía esa partida (id o enlace de Lichess)")
    ap.add_argument("--solo", metavar="ALIAS", help="con --enviar: revisa solo a ese jugador («Revisar ahora»)")
    ap.add_argument("--historia", metavar="ALIAS",
                    help="envía el primer capítulo hecho con las últimas partidas (o la invitación a jugar si no tiene)")
    ap.add_argument("--ver-historia", metavar="ALIAS", help="como --historia, pero solo lo muestra, sin enviar")
    ap.add_argument("--probar-ia", metavar="ALIAS",
                    help="genera la historia de la última derrota de ese participante con la IA y la muestra, sin enviar nada")
    args = ap.parse_args()
    if args.historia or args.ver_historia:
        alias = (args.historia or args.ver_historia).strip()
        ok = enviar_historia(alias, None if args.ver_historia else config(), args.variante,
                             solo_mostrar=bool(args.ver_historia))
        if ok and args.historia:
            # Que el detector automático (laptop o GitHub) no lo vuelva a enviar
            estado = leer_estado()
            info = estado.setdefault(alias, {"vistas": [], "enviados": 0,
                                             "desde": int(datetime.now(timezone.utc).timestamp() * 1000)})
            info["historia"] = f"{datetime.now():%d/%m/%Y %H:%M}"
            guardar_estado(estado)
        return
    if args.probar_ia:
        p = next((x for x in leer_participantes() if x["alias"].strip() == args.probar_ia.strip()), None)
        if not p:
            sys.exit(f"{args.probar_ia} no está en participantes.csv.")
        cfg = leer_config_local()
        if not cfg.get("cloudflare_account_id") or not cfg.get("cloudflare_token"):
            print("config_local.json no tiene 'cloudflare_account_id' y 'cloudflare_token': se mostrará la plantilla.")
        g, color, clave = ultima_derrota(p)
        if not g:
            sys.exit("No encontré una derrota reciente para probar.")
        item = {"alias": p["alias"], "variante": args.variante or "A", "partida": g["id"],
                "n": math.ceil(len(g.get("moves", "").split()) / 2), "color": "blancas" if color == "white" else "negras",
                "villano": p.get("villano", "").strip() or "La Horquilla Hambrienta", "clave": clave, **datos_partida(g), "encuentros": encuentros_de(g, color)}
        enlace, _, _ = armar(item, con_ia=True)
        print(f"Partida https://lichess.org/{g['id']} · error principal en la jugada {clave['jugada']} ({clave.get('fuente')})")
        print(f"Historia ({item['historia_fuente']}):\n  " + "\n  ".join(item["historia"]))
        for i, (e, d) in enumerate(zip(item["encuentros"], item["dialogos"])):
            print(f"Encuentro {i + 1} · jugada {e['jugada']} ({e['jugada_san']}, caída {e.get('caida', '?')}):\n"
                  f"  villano: {d['antes']}\n  consejero: {d.get('consejo', '')}\n  villano al resolver: {d['despues']}")
        print(f"Enlace: {len(enlace)} caracteres")
        print(f"Escena: {enlace}")
        return
    if args.ultima:
        sesion(args.ultima.strip(), args.variante, args.partida)
        return
    if args.probar:
        cfg = config()
        err = enviar_push(args.probar, "Zaqora", "Aviso de prueba: si lo ves, los avisos funcionan.",
                          f"{URL_ESCENA}?p={urllib.parse.quote(args.probar)}&v=prueba", "prueba", cfg)
        print(err or f"Aviso de prueba enviado a {args.probar}.")
        return
    cfg = config() if args.enviar else None
    while True:
        participantes = leer_participantes()
        if args.solo:
            participantes = [p for p in participantes if p["alias"].strip() == args.solo.strip()]
        estado = leer_estado()
        print(f"[{datetime.now():%d/%m %H:%M}] Revisando {len(participantes)} participantes…")
        if args.enviar and os.environ.get("GITHUB_ACTIONS") == "true" and _ESTADO_EN != "supabase":
            # En la nube no hay estado.json que dure entre corridas: sin la tabla se repetirían los avisos.
            sys.exit("Falta la tabla estado_detector en Supabase (3 - jugadores y estado.sql). No se envía nada.")
        if args.enviar:
            # Primer capítulo con el historial: en cuanto el participante activa los avisos.
            for p in participantes:
                info = estado.setdefault(p["alias"], {"vistas": [], "enviados": 0,
                                                      "desde": int(datetime.now(timezone.utc).timestamp() * 1000)})
                if info.get("historia"):
                    continue
                try:
                    activo = suscripcion_de(p["alias"], cfg)
                except Exception:
                    activo = None
                if not activo:
                    continue
                if enviar_historia(p["alias"], cfg):
                    info["historia"] = f"{datetime.now():%d/%m/%Y %H:%M}"
            guardar_estado(estado)
        nuevas = revisar(participantes, estado)
        if not args.enviar:
            # Solo revisar: muestra lo que se enviaría y NO toca estado.json ni los registros,
            # así esas derrotas se siguen pudiendo enviar después con --enviar.
            for item in nuevas:
                enlace, _, aviso = armar(item)
                print(f"\n--- {item['alias']} · variante {item['variante']} · derrota de {item['fin']:%d/%m %H:%M} "
                      f"(https://lichess.org/{item['partida']}) ---\n{item['villano']} — {aviso}\n"
                      f"Historia (plantilla; la de IA se genera al enviar):\n  " + "\n  ".join(item["historia"]) +
                      "".join(f"\n  Encuentro {i + 1} (jugada {e['jugada']}): {d['antes']} / {d['despues']}"
                              for i, (e, d) in enumerate(zip(item.get("encuentros") or [], item["dialogos"]))) +
                      f"\nEscena: {enlace}"
                      + ("" if item["clave"] else "\n   Sin análisis: la escena usaría una posición de ejemplo."))
            print("\n  Sin derrotas nuevas." if not nuevas else
                  "\n  (Solo revisión: no se envió nada. Para enviar: --enviar, o una sola con --ultima ALIAS --partida ID)")
            if args.cada <= 0:
                break
            time.sleep(args.cada * 60)
            continue
        nuevo_registro = not REGISTRO.exists()
        with REGISTRO.open("a", encoding="utf-8", newline="") as f, SALIDA.open("a", encoding="utf-8") as out:
            w = csv.writer(f)
            if nuevo_registro:
                w.writerow(["participante", "variante", "partida", "fin_de_la_partida", "detectada",
                            "con_analisis", "aviso_enviado"])
            for item in nuevas:
                enlace, mensaje, aviso = armar(item, con_ia=True)
                enviado = "no"
                if args.enviar:
                    err = enviar_push(item["alias"], item["villano"], aviso, enlace, item["partida"], cfg)
                    if err:
                        print("  " + err)
                    else:
                        enviado = f"{datetime.now():%d/%m/%Y %H:%M}"
                        estado[item["alias"]]["enviados"] += 1
                        guardar_capitulo(item, enlace, cfg)
                bloque = (f"\n=== {item['alias']} · variante {item['variante']} · derrota de {item['fin']:%d/%m %H:%M} ===\n"
                          f"Aviso ({'enviado ' + enviado if enviado != 'no' else 'no enviado'}):\n"
                          f"{item['villano']} — {aviso}\nEscena: {enlace}\n")
                if not item["clave"]:
                    bloque += (f"   Ojo: pasaron {ESPERA_ANALISIS_MIN} min y la partida sigue sin análisis en Lichess "
                               f"(https://lichess.org/{item['partida']}); la escena usa una posición de ejemplo. "
                               "Si quieres la posición real, elige el momento a mano y mándale el enlace corregido.\n")
                print(bloque)
                out.write(bloque)
                w.writerow([item["alias"], item["variante"], item["partida"], f"{item['fin']:%d/%m/%Y %H:%M}",
                            f"{datetime.now():%d/%m/%Y %H:%M}", "sí" if item["clave"] else "no", enviado])
        guardar_estado(estado)
        if not nuevas:
            print("  Sin derrotas nuevas.")
        if args.cada <= 0:
            break
        time.sleep(args.cada * 60)


if __name__ == "__main__":
    main()
