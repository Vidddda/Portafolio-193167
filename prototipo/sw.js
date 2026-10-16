/* Service worker del prototipo: muestra el aviso del villano y abre la escena al tocarlo. */
self.addEventListener("install", () => self.skipWaiting());
self.addEventListener("activate", (e) => e.waitUntil(self.clients.claim()));

self.addEventListener("push", (event) => {
  let datos = {};
  try { datos = event.data ? event.data.json() : {}; } catch (e) { datos = { cuerpo: event.data && event.data.text() }; }
  const titulo = datos.titulo || "Zaqora";
  event.waitUntil(self.registration.showNotification(titulo, {
    body: datos.cuerpo || "Tu villano te está esperando.",
    icon: "icono-192.png",
    badge: "icono-192.png",
    tag: datos.etiqueta || "zaqora",      // un solo aviso por derrota: no se acumulan
    data: { url: datos.url || "escena.html" }
  }));
});

self.addEventListener("notificationclick", (event) => {
  event.notification.close();
  const url = new URL(event.notification.data.url, self.registration.scope).href;
  event.waitUntil(self.clients.openWindow(url));
});
