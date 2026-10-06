---
name: felipe-juarez-personaje
description: FELIPE JUAREZ — personaje (señor canoso) de la campaña "Miedo a invertir" de Terraregia; hoja de referencia, outfit camisa verde #152A23, job_ids y media_ids. Reemplazado por Felipe Juarez 2.0 el 2 oct 2026 (ver felipe-juarez-2-0)
metadata:
  type: project
---

**Se llama Felipe Juarez** (nombre dado por Liz el 2 oct 2026) y es el protagonista de [[terraregia-miedo-a-invertir]]. Liz anunció que pronto mandará otro personaje que lo reemplaza: **Felipe Juarez 2.0** — cuando llegue, rehacer referencias (3 vistas, rostro, outfit) con el mismo método y guardar sus media_ids en una memoria nueva.

Liz mandó un outfit (camisa olivo abierta + playera blanca + cargo negro, foto de mentalmens.com) y pidió cambiar la camisa a verde **#152A23**; luego ponérselo a su personaje (hombre ~45, pelo y barba canosos, hoja "HOJA DE REFERENCIA DE PERSONAJE", original en camisa de cuadros azul + jeans + tenis blancos).

Entregas en `~/Downloads/CLAUDE/`:
- `outfit-camisa-verde/` — turnaround de 4 vistas con modelo genérico. job `4d8e88b7-562b-4c54-9b47-004422982d28` (sirve de referencia del outfit).
- `personaje-outfit-verde/` — el personaje en 3 vistas (frente/perfil/espalda) con el outfit. job `adfde710-bacc-4484-8408-ad37e9123fd9`; versión SIN pulseras (la vigente, 30 sep) job `4c9a53dc-1068-409e-80df-156d193549f1` — Liz: "no podemos tener inconsistencias".

media_ids: cuerpo 3 vistas del personaje `581876b7-704b-4a37-9cf1-0eeb0e10e6b6`, rostros `feb10921-0f4b-44a1-9f70-03134c3520d0`.

Método que funcionó a la primera: editar el recorte de sus 3 vistas (nano_banana_pro 2k, 1:1) pasando como 2ª referencia el turnaround del outfit — conserva cara y poses. Los tenis negros los inventé yo (el outfit original no mostraba pies). Ver [[chica-personaje-angulos]].

**Hoja de referencia completa con el outfit verde** (30 sep 2026) en `~/Downloads/CLAUDE/personaje-hoja-outfit-verde/hoja_personaje_outfit_verde.png` (1586x992, misma medida que la original). Se armó SOBRE la hoja original: solo se reemplazaron los paneles con ropa (cuerpo = las 3 vistas sin pulseras; rostros, expresiones y detalles = recortes editados con nano banana y mapeados panel por panel; círculo+texto de VESTIMENTA en la paleta). Títulos y etiquetas son los originales, no pasaron por IA. Script en `trabajo/armar.py`. Nano banana REACOMODA la cuadrícula al editar un bloque, así que hay que detectar los paneles del resultado y mapear cada uno a su caja; pegar el bloque completo en las coordenadas originales queda desalineado. En el panel MANO DERECHA el reloj cambió de smartwatch a analógico.
