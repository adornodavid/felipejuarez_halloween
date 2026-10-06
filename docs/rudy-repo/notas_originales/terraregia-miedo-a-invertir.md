---
name: terraregia-miedo-a-invertir
description: Campaña "MIEDO A INVERTIR" de TERRAREGIA (30 sep–2 oct 2026) — video de terror de 42.5 s con Felipe Juarez hecho en Genjutsu; estructura por clips, receta de prompt, costos, voz de ElevenLabs y dónde está cada archivo
metadata:
  type: project
---

**Campaña:** "MIEDO A INVERTIR" · **Cliente:** TERRAREGIA (desarrolladora; showroom "Terra Regia – Concéntrico + Urban") · **Personaje:** Felipe Juarez ([[felipe-juarez-personaje]]); reemplazado el 2 oct 2026 por **Felipe Juarez 2.0** ([[felipe-juarez-2-0]]); el rehacer de clips va en [[terraregia-felipe2-clips]].

**Concepto (de Liz):** cuarto oscuro, Felipe enciende una linterna (luz desde abajo, tenebrosa, solo se ve la cara), habla; la linterna se apaga, negro; última toma: se levanta de un sillón, el cuarto se ilumina y es el showroom de Terraregia, luz normal. Material crudo: actor en chroma con micrófono, `~/Downloads/RUDY/Videos Finales/Terraregia/Video 1.mp4` (48 s, 8 cortes).

**Carpetas:**
- `~/Downloads/CLAUDE/terraregia-genjutsu-prueba/` — todo: clips fuente `Clip 1..7 de 8.mp4`, resultados `clipN_genjutsu_720p*.mp4`, toma final `toma_final_showroom_720p_sin_silla.mp4` (también en `Clips Finales/`), `Outro TerraRegia_continuo.mp4`, scripts (`corregir_lente.py`, `quitar_silla.py`, `clip1_luz_edicion.py`), referencias (`ref_linterna_sola.jpg`, `ref_sillon.jpg`, `ref_mesa_alta.jpg`, `ref_iluminacion_linterna.png`, `showroom.jpg`). Liz armó el final ella misma: `Clip Original.mp4` / `Clip Voz.mp4` / `Video FInal Solo Voz.mp4` (720x1248, 24 fps, 42.5 s). Comparativa vigente: `comparativa_original_vs_clip_voz.mp4`.
- `~/Downloads/CLAUDE/terraregia-voz/` — voz cambiada: `Video Final Voz Arturo Casares.mp4` y las pruebas.

**Resultado por clip (todos Genjutsu `hf_mult_replace_object` 720p):**
- Clip 1 (encendido de linterna): job `5f5f2f16-e795-4525-ae38-1e5205cb66bf`. Liz prefirió el encendido que inventa Genjutsu ("silueta apenas visible, luego la luz se ve encenderse") sobre mi parpadeo en edición.
- Clips 2+4+5 en un solo envío (2 era < 2 s, Higgsfield lo rechaza solo): `a48cc2d5-443c-4b3d-a47a-feb7856fbeb6`, separados por cuadro de corte.
- Clip 3: v2 `62ebde8f-c6b8-4ef4-9118-dbd839195f5e` (manos subieron de 85 % a 68–80 % del cuadro, pero volvieron manchas de luz en la cara). v1 `a39259b0-…`.
- Clips 6 (detalle de manos) + 7 (apagado + zoom out): `1bf12125-adf8-4f4b-9f0b-f4a30ce98fac`; manos clavadas a la altura del original. Al 7 le agregué parpadeo de apagado en edición (Liz lo pidió): `clip7_genjutsu_720p_parpadeo.mp4`.
- Toma final showroom: `135de18e-058c-4ac9-b3d3-b004d6daae1a` + silla blanca borrada en edición.

**Receta de prompt que funcionó** (ver [[genjutsu-reemplazo-video]]): 1) NO text primero; 2) mismo encuadre cerrado, no zoom out; 3) proporciones del cuerpo + altura de manos en % del cuadro medida del original ("hands must NOT drop to stomach"); 4) "Replace the microphone with the flashlight from reference image 3" SIN describir el micrófono (pedido de Liz); 5) personaje de ref 1-2; 6) cuarto negro + luz desde abajo como ref 4, "soft, well exposed, not blown out, no light bands"; 7) cuerpo muy oscuro. Si la linterna ya está encendida en la toma: decirlo explícito ("already ON from the first frame, never turns on again") — Liz lo advirtió. Referencias: 3 vistas sin pulseras `4c9a53dc-1068-409e-80df-156d193549f1`, rostros `feb10921-…`, linterna `8e7a0d2d-671f-4c87-ab2d-5f184deac1c2`, luz `c4a9970e-8861-4888-a048-c3e724e63377`, sillón `97bc0ebe-…`, mesa alta `ebff942c-…`, showroom `1f823f09-4d4a-478d-9976-abddb7149d39`.

**Costo total del proyecto:** 596 créditos Higgsfield (toma final 142, clip 1 91, clips 2/4/5 70, clip 3 168, clips 6/7 63, pruebas 62). Liz pide el conteo seguido: sacarlo de `transactions`.

**Voz:** ElevenLabs speech-to-speech con **Arturo Casares** (`N2HSRirbsHTZ8DE2WqjB`); Liz quería "serio, elegante, 50-60 años, clara y tenebrosa" y descartó Salvatore, El Faraón y Josué Maya. Ver [[elevenlabs-instalado]].

**Cómo trabaja Liz aquí:** pruebas a 480p para ahorrar y finales a 720p; antes de mandar quiere oír qué se le pedirá a Genjutsu; quiere comparativas lado a lado con etiquetas ORIGINAL/FINAL; no aplicar ajustes de edición sin que los pida ("no apliques nada"). Ver [[liz-cambios-quirurgicos]], [[iphone-cambio-de-lente]].
