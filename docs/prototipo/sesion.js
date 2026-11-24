/* Inicio de sesión con Lichess (OAuth 2.0 con PKCE, sin contraseña ni secretos en la página)
   y acceso a los capítulos del jugador a través de la función «capitulos» de Supabase.
   Zaqora solo pide a Lichess confirmar quién eres: no pide ningún permiso extra (sin «scopes»). */
(function () {
  const CFG = window.ZAQORA || {};
  const CLIENTE = "zaqora-prototipo";
  const LICHESS = "https://lichess.org";
  const leer = (k) => { try { return localStorage.getItem(k); } catch (e) { return null; } };
  const guardar = (k, v) => { try { v == null ? localStorage.removeItem(k) : localStorage.setItem(k, v); } catch (e) {} };
  const redireccion = () => new URL("inicio.html", location.href).href.split("?")[0];

  function b64url(bytes) {
    return btoa(String.fromCharCode(...new Uint8Array(bytes))).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
  }
  function aleatorio(n) { return b64url(crypto.getRandomValues(new Uint8Array(n))); }

  async function entrar() {
    const verificador = aleatorio(48), estado = aleatorio(16);
    const reto = b64url(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(verificador)));
    guardar("zaqora_oauth", JSON.stringify({ verificador, estado }));
    const u = new URL(LICHESS + "/oauth");
    u.search = new URLSearchParams({ response_type: "code", client_id: CLIENTE, redirect_uri: redireccion(),
                                     code_challenge_method: "S256", code_challenge: reto, state: estado }).toString();
    location.href = u.href;
  }

  /* Al volver de Lichess (?code=…&state=…): cambia el código por un token y confirma el usuario. */
  async function terminarEntrada() {
    const q = new URLSearchParams(location.search);
    if (!q.get("code") && !q.get("error")) return null;
    const limpiar = () => history.replaceState(null, "", location.pathname);
    let pendiente = null;
    try { pendiente = JSON.parse(leer("zaqora_oauth") || "null"); } catch (e) {}
    guardar("zaqora_oauth", null);
    if (q.get("error")) { limpiar(); throw new Error("No autorizaste a Zaqora en Lichess."); }
    if (!pendiente || pendiente.estado !== q.get("state")) { limpiar(); throw new Error("La respuesta de Lichess no coincide. Vuelve a intentarlo."); }
    const r = await fetch(LICHESS + "/api/token", {
      method: "POST", headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams({ grant_type: "authorization_code", code: q.get("code"),
                                  code_verifier: pendiente.verificador, redirect_uri: redireccion(), client_id: CLIENTE })
    });
    limpiar();
    if (!r.ok) throw new Error("Lichess no aceptó la entrada. Vuelve a intentarlo.");
    const token = (await r.json()).access_token;
    const cuenta = await fetch(LICHESS + "/api/account", { headers: { Authorization: `Bearer ${token}` } }).then((x) => x.json());
    guardar("zaqora_lichess_token", token);
    guardar("zaqora_lichess_usuario", cuenta.username || cuenta.id || "");
    return cuenta.username || cuenta.id;
  }

  async function salir() {
    const token = leer("zaqora_lichess_token");
    guardar("zaqora_lichess_token", null);
    guardar("zaqora_lichess_usuario", null);
    if (token) {
      try { await fetch(LICHESS + "/api/token", { method: "DELETE", headers: { Authorization: `Bearer ${token}` } }); } catch (e) {}
    }
  }

  /* Llama a la función «capitulos» con la sesión de Lichess. */
  async function capitulos(metodo, cuerpo) {
    const token = leer("zaqora_lichess_token");
    if (!token || !CFG.SUPABASE_URL) return null;
    const r = await fetch(`${CFG.SUPABASE_URL}/functions/v1/capitulos`, {
      method: metodo,
      headers: { "Authorization": `Bearer ${CFG.SUPABASE_KEY}`, "apikey": CFG.SUPABASE_KEY,
                 "x-lichess-token": token, "Content-Type": "application/json" },
      body: cuerpo ? JSON.stringify(cuerpo) : undefined,
      keepalive: metodo === "POST"
    });
    const datos = await r.json().catch(() => ({}));
    if (r.status === 401) { guardar("zaqora_lichess_token", null); guardar("zaqora_lichess_usuario", null); }
    if (!r.ok) throw new Error(datos.error || `La función respondió ${r.status}`);
    return datos;
  }

  window.ZaqoraSesion = {
    entrar, terminarEntrada, salir, capitulos,
    usuario: () => (leer("zaqora_lichess_token") ? leer("zaqora_lichess_usuario") : null)
  };
})();
