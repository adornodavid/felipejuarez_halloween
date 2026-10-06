---
name: felipe-juarez-2-0
description: FELIPE JUAREZ 2.0 — protagonista vigente de "Miedo a invertir" (2 oct 2026): hombre ~30s pelo casi negro y barba oscura; hoja 4K, 3 fotos de estudio con outfit verde, props (linterna/mesa/sillón) y sus job_ids
metadata:
  type: project
---

Reemplaza al primer Felipe ([[felipe-juarez-personaje]]) en [[terraregia-miedo-a-invertir]]. Hombre de ~30 y pocos, pelo casi negro corto, cejas gruesas, ojos café oscuro, barba completa recortada; SIN canas (no envejecerlo). Liz lo mandó como hoja "HOJA DE REFERENCIA DE PERSONAJE" de WhatsApp (1586x992, baja calidad) con saco gris + camisa blanca + pantalón navy; lo vestimos con el outfit del primer Felipe (camisa verde #152A23 abierta, playera blanca, cargo negro, tenis negros, reloj de correa café en muñeca izquierda, sin pulseras).

Carpeta: `~/Downloads/CLAUDE/felipe-juarez-2.0/`
- `hoja_felipe2_mejorada_4k.png` — hoja reescalada (bytedance upscale 4k, 2 cr). job `40da97d3-d720-4967-9a29-d6898d4f1c35`. Recorte de rostros reescalado: job `c957795a-44a8-4fe9-a92c-22034cf2ace7`.
- `1_closeup_rostro.png` job `e96d0f41-ecc4-41ef-9450-48a220871ed9` (cara un poco más ancha/joven y barba más rala que la hoja).
- `2_cuerpo_frente.png` job `0f649692-27d1-4251-ad4a-e77739d7d630` (la cara más fiel).
- `3_cuerpo_espalda.png` job `13675023-2aae-4221-80d9-c7b3e0667f7d`.
- `felipe2_3_vistas.png` — las 3 juntas en una sola (5287x2832, misma altura, marco gris del fondo), pedido de Liz.
- media_ids subidos: hoja original `b9a4ba1e-594b-42d8-af60-1b47d2a90f54`, rostros `078a1285-bec3-4d0d-91b0-2f8858884242`, cuerpo `d793d042-9d5c-4899-9a22-596aa5e37dda`.

Receta: nano_banana_pro con ref 1 = hoja 4K (identidad) y ref 2 = 3 vistas del outfit `4c9a53dc-…`, diciendo "ignore that man's face" y "Do NOT use the grey blazer…" ; fondo gris neutro de estudio. Las 3 salieron a la primera. Aprobadas por Liz (2 oct).

**Props de estudio (2 oct 2026)** en `~/Downloads/CLAUDE/felipe-juarez-2.0/props/` — Liz: fondo gris plano, luz pareja, SIN cast shadows. Rechazos en `props/descartes/`.
- linterna close up frente `7b3f9522-f0cd-4768-92d7-49c4d8615462` (sale 3/4, no de frente puro); linterna completa de lado `469788cb-32d8-4d01-9858-a386584ee346` — la 1ª salió con un FANTASMA borroso porque la ref original trae una mancha difuminada abajo a la izquierda: usar el close up generado como referencia, no la foto original.
- mesa alta completa `5d9d0388-72f8-48b5-987a-d4c6b8635d43`.
- sillón 3/4 `4ff7ac26-8d20-4466-885c-341a1cbf4351` (la 1ª tenía sombra suave; se quitó con "recreate exactly but remove every shadow"); sillón perfil `7ce1b420-ce55-4f17-be04-7a598dca2e85` (pedí 90° y aun así queda ligeramente girado).
- media_ids de las refs originales re-subidas: linterna `5a6f92e6-76d0-4351-b154-50e4e7e0418c`, mesa `233aaba4-33e5-400f-88bc-7a1f0589f263`, sillón `e5a0f7c1-634f-428f-ac99-d5280d21d158`.
- Costo: nano_banana_pro = 2 cr por imagen (transactions la cobra como Nano Banana Pro aunque el job diga nano_banana_2). Día 2 oct en Felipe 2.0 + props: 26 cr.

El avance de los clips en Genjutsu con este personaje está en [[terraregia-felipe2-clips]].


**Ceja (5 oct 2026):** a Liz no le gusta el mechón despeinado/abierto al inicio de la ceja izquierda de Felipe (la de la DERECHA de la imagen, junto a la nariz) en la cara de referencia (`felipe2_3_vistas faceless.jpg` panel izq. = `1_closeup_rostro.png`). Retoque v1 con nano_banana_pro (job `36ca5d29-c6c2-4b81-9c42-1e659df85175`, 2 cr) sobre recorte `ceja/cara_original_crop.png` (crop 500,250–1650,1400 del faceless): quitó el abanico pero dejó pelos parados/tiesos tipo cepillo, distinto a la otra ceja. Salió alineada al original (sin desplazamiento), así que se puede parchar solo la ceja con máscara elíptica (centro 650,532 en el recorte). En los clips de terror la zona queda en sombra y no se nota. Pegado en la hoja completa: `ceja/felipe2_3_vistas faceless_ceja_v1.png` (PNG sin pérdida, 5287x2832). Liz lo va a terminar en Photoshop (suavizar el inicio tieso); cuando lo regrese, subirlo como nueva ref 1 en vez de `62f9daf0-…`.
**Ceja FINAL (5 oct):** Liz la arregló en Photoshop → `Felipe/felipe2_3_vistas faceless_ceja_v1 arreglo.png`, subida como media `1c3921d4-dd74-445a-8f6a-ad3331959083`. **Esta es la ref 1 vigente** desde el clip 8 (antes `62f9daf0-…`). La `.jpg` faceless original sigue intacta.
