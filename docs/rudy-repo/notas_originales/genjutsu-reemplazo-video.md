---
name: genjutsu-reemplazo-video
description: Higgsfield Genjutsu (hf_mult_replace_object / hf_mult_motion_control) — precios, límites y la trampa de subtítulos inventados (30 sep 2026)
metadata:
  type: reference
---

Probado 30 sep 2026 con el video Terraregia (RUDY/Videos Finales/Terraregia/Video 1.mp4, actor en chroma con micrófono).

- **Precio 720p:** replace_object = 7 cr/s + 7 por clip (5s=42, 10s=77); motion_control = 7 cr/s (5s=35, 10s=70). 1080p replace 10s = 121. **480p replace 5s = 18 cr** (sirve para pruebas; sale 480x854). get_cost exige subir el video (role `video_references`) — sube clips ligeros solo para cotizar.
- **Un video de 48s completo lo rechaza (422)**: hay que ir por toma.
- Genjutsu sugiere el preset "IN THE DARK"; se destraba con `declined_preset_id`.
- Tarda ~10+ min por clip de 5s.
- **Salida:** 720x1280 a 24fps, recorta ~0.3s del final; el audio original se conserva alineado (offset 0).
- **Trampa:** QUEMÓ SUBTÍTULOS inventados (transcribió el audio) aunque el original no tenía texto → pedir explícitamente "no subtitles, no captions, no on-screen text".
- Resultado: identidad del personaje, ropa y sillón muy bien; pose y gestos idénticos; conserva el chroma. Micrófono→linterna sale como cilindro negro chico con lente encendido (se lee poco como linterna).

Ver [[felipe-juarez-personaje]].

- **Sí re-ilumina por prompt** (30 sep): pedir cuarto negro + luz de linterna desde abajo funcionó a la primera — fondo negro sin verde, cara con luz de abajo, linterna más grande y visible, sin subtítulos al prohibirlos, pantalón negro al pedir 'pure black, not brown'. La caída de luz en piernas/silla queda corta: se completa en edición con un viñeteo radial (script en terraregia-genjutsu-prueba/). Jobs: 720p con chroma `2018c235-eca4-420c-8ccf-9fca91a05b92`, 480p iluminado `48255752-93a6-4ea4-b707-83a2b18a4bb4`.
- **Abre el encuadre** si le pides reemplazar un objeto que NO sale en cuadro (1 oct: pedí el sillón en un plano cerrado sin silla y entregó cuerpo entero). Solo pedir objetos visibles + "keep exactly the same close framing, do NOT zoom out".
- Los subtítulos inventados reaparecen al azar aunque se prohíban al final del prompt → la prohibición va como punto 1.
- Iluminación de linterna desde abajo con imagen de referencia de luz: funciona pero puede quemar la cara (sobreexpuesta, manchas) → pedir "soft, well exposed, not blown out".
- Higgsfield sugiere presets ("IN THE DARK", "Earth zoom out"); se destraba con `declined_preset_id` del preset que proponga.
- Rol de referencias: se pueden citar por número ("reference image 3") en el orden de `medias`; el micrófono se cambió a la primera al poner "Replace the microphone with the flashlight from reference image 3" SIN describir el micrófono (pedido de Liz).
- **Límite de duración (2 oct 2026):** `get_cost` NO lo revela: cotizó 12/15/20/30 s sin quejarse (84/105/140/210 cr a 720p = 7 cr/s exactos, sin el +7). Lo comprobado: 11.4 s aceptado al enviar, 48 s rechazado (422) al enviar, < 2 s rechazado. El máximo real solo se sabe enviando. Videos de prueba subidos: 12s `cbd57388-…`, 15s `e61e1ed8-…`, 20s `a18356e0-…`, 30s `73f82a1b-…`.
- **Varias tomas con evento de luz (3 oct 2026):** en un envío 1+5+7 donde solo la 1ª toma tenía el encendido, Genjutsu aplicó la luz de horror solo a esa toma y dejó las otras con luz de estudio normal y linterna apagada. Mandar el clip con evento de luz por separado. 14.3 s sí lo acepta.
- No quita accesorios del actor (anillo) aunque se le pida.
- **Tiempos de un evento (5 oct 2026):** Genjutsu NO obedece segundos con decimales (pedí encendido en "0.45 s" y lo puso en 4.42 s), pero SÍ obedece la descripción con palabras ("at the very beginning, before his first word, ON for almost the entire video" → 0.79 s). Y sí respeta "turns ON INSTANTLY, NOT a slow fade-in" (2–3 cuadros).
