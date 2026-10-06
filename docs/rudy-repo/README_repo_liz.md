# TERRAREGIA — "MIEDO A INVERTIR"

Video vertical de terror de 42.5 s para **TERRAREGIA** (desarrolladora inmobiliaria, showroom "Terra Regia – Concéntrico + Urban").
Producción: ARKAMIA (Liz Nava). Hecho del 30 sep al 5 oct de 2026 con **Higgsfield Genjutsu** (reemplazo de personaje y objetos en video), **nano banana pro** (personajes y props) y **ElevenLabs** (cambio de voz).

## Concepto

Un cuarto oscuro. Felipe Juarez enciende una linterna (luz desde abajo, tenebrosa, solo se le ve la cara) y habla. La linterna se apaga y todo queda en negro. En la última toma se levanta de un sillón, el cuarto se ilumina y resulta ser el showroom de Terraregia, con luz normal.

**Material crudo:** un actor (David) grabado en chroma con micrófono, 8 cortes, 720x1248 a 24 fps (`archivos/00_material_cliente/`). Genjutsu reemplaza:

- al actor por Felipe;
- el micrófono por la linterna;
- la caja por el sillón;
- el banco por la mesa alta;
- el chroma por el cuarto negro o el showroom.

## Versiones del personaje

| Versión | Descripción | Estado |
|---|---|---|
| **Felipe Juarez 1.0** | Señor de ~45 años, pelo y barba canosos | Primer corte completo (596 cr). Reemplazado el 2 oct |
| **Felipe Juarez 2.0** | Hombre de 30 y pocos, pelo corto casi negro, cejas gruesas, ojos café oscuro, barba completa oscura recortada | **Vigente** |

**Outfit (las dos versiones):**

- camisa verde **#152A23** abierta;
- playera blanca;
- cargo negro;
- tenis negros;
- reloj de correa café en la **muñeca izquierda**;
- sin pulseras.

Comparativa de las tres versiones, sincronizadas y con el audio de Felipe 2.0: `archivos/03_comparativa_versiones/comparativa_David_Felipe1_Felipe2.mp4`.

## Estructura del repositorio

```
01_ficha_referencia/               ← ficha vigente de Felipe 2.0 (ceja arreglada) + hoja 4K
02_voz/                            ← voice IDs de ElevenLabs
03_originales_chroma/              ← .MOV originales del actor (David) en chroma, 4K HEVC 30 fps + Clips Javo/
04_resultado/                      ← video final Felipe 2.0 + comparativa de versiones
05_animacion_inicio/               ← intro "¿Le temes a invertir?" (cerillo encendiéndose), 1080x1920, 24 fps, 10 s
README.md                          ← este documento (resumen de todo)
docs/
  estado_y_pendientes.md           ← qué está aprobado, qué falta, decisiones abiertas
  receta_genjutsu.md               ← cómo escribir el prompt y las lecciones aprendidas
  costos.md                        ← créditos de Higgsfield, desglosados
  ids_higgsfield.md                ← job_ids y media_ids de referencias
  voz_elevenlabs.md                ← voces probadas y método
  prompts/                         ← TEXTO EXACTO de cada envío (recuperado del historial)
  notas_originales/                ← notas de trabajo de Claude, tal cual (memoria)
archivos/
  00_material_cliente/             ← video crudo del actor (RUDY/Videos Finales/Terraregia)
  01_felipe-juarez-1.0_personaje/  ← outfit, 3 vistas y hoja del Felipe 1.0
  01_felipe-juarez-1.0_genjutsu/   ← clips fuente, resultados, pruebas, scripts y refs del 1er corte
  01_felipe-juarez-1.0_voz/        ← pruebas de voces y la versión final con Arturo Casares
  02_felipe-juarez-2.0/            ← todo lo de Felipe 2.0 (ver abajo)
  03_comparativa_versiones/        ← David vs Felipe 1.0 vs Felipe 2.0
```

### `archivos/02_felipe-juarez-2.0/`

- **`Felipe/`**: referencias del personaje.
  - **Ref vigente:** `felipe2_3_vistas faceless_ceja_v1 arreglo.png`, con la ceja arreglada por Liz en Photoshop.
  - También están la hoja 4K, el close-up, el cuerpo de frente y el de espalda.
- **`props/`**: linterna (close-up y de lado), mesa alta y sillón (3/4 y perfil). Los descartes están en `props/descartes/`.
- **`Clips/`**: los 8 cortes crudos (`N de 8.mp4`), `Video Final.mp4` y `Video Solo voz.mp4`.
- **`genjutsu/`**: fuentes concatenadas (`*_fuente.mp4`), resultados (`*_genjutsu_720p*.mp4`), comparativas ORIGINAL|FINAL y `quitar_silla_clip8.py`.
- **`refs/`**: `ref_luz_clip1_v3.png` es la referencia de luz dura, sacada del clip 1 aprobado. También están las comparaciones de luz entre tomas.
- **`ceja/`**: el proceso del retoque de la ceja.
- **`voz/`**: prueba con la voz "Jonas".
- **`trabajo/`**: auxiliares (tiras de cuadros, pruebas de cotización, hoja original de WhatsApp).

## Mapa de clips (crudos de Felipe 2.0)

| Clip | Duración | Plano | Notas |
|---|---|---|---|
| 1 | 6.54 s | Close-up de frente | Encendido de la linterna. El actor habla desde el 1.17 s |
| 2 | 1.92 s | Close-up de lado | Menos de 2 s, va pegado a otro |
| 3 | 11.33 s | Close-up de frente | |
| 4 | 2.5 s | Close-up de lado | |
| 5 | 4.25 s | Close-up de frente | |
| 6 | 1.54 s | Detalle de mano, se ven las piernas | Menos de 2 s, va pegado a otro |
| 7 | 3.5 s | Close-up de frente | Se ve el pantalón |
| 8 | 9.96 s | Sentado, luego abre a cuerpo completo | Toma final en el showroom |

Las tomas se mandan agrupadas por envío porque Higgsfield rechaza clips de menos de 2 s.

## Archivos finales vigentes (Felipe 2.0)

| Clips | Archivo | Estado |
|---|---|---|
| 1 | `genjutsu/clip_1_genjutsu_720p_v3.mp4` | ✅ Aprobado por Liz |
| 2+4+6 | `genjutsu/clips_2_4_6_genjutsu_720p.mp4` | Sin aprobar (luz más frontal que el resto) |
| 3 | `genjutsu/clip_3_genjutsu_720p.mp4` | **Sin reloj**, pendiente de decisión |
| 5+7 | `genjutsu/clips_5_7_genjutsu_720p_v3.mp4` | Luz dura, igual a la del clip 1. Falta el OK |
| 8 | `genjutsu/clip_8_genjutsu_720p_sin_silla.mp4` | Versión normal. La silla blanca se borró en edición |

Detalle en `docs/estado_y_pendientes.md`.

## Reglas de Liz (obligatorias)

1. **Cada envío a Higgsfield lo autoriza Liz.** Antes se le enseñan el prompt y la cotización (`get_cost`, que no gasta créditos).
2. **Todo a 720p.** 480p solo para pruebas.
3. **Nunca mencionar canas** (gray hair/beard), ni siquiera en negativo, porque confunde a Genjutsu.
4. **El anillo se queda.** No mencionarlo.
5. **Reloj:** correa café **siempre a la DERECHA de la pantalla** en tomas de frente (= su muñeca izquierda). La otra muñeca va sin reloj.
6. **Personaje** solo de la hoja "faceless" (el cuerpo de en medio no tiene cara a propósito). Describir solo lo que es, sin inventar rasgos.
7. **Cambios quirúrgicos:** aplicar solo lo que Liz lista. Las inconsistencias se señalan, pero no se corrigen por cuenta propia.
8. **Comparativas** lado a lado (ORIGINAL | FINAL) para revisar cada resultado.
9. Si sale el pantalón (clip 6), pedir cargo negro. Si no sale, no mencionarlo, porque Genjutsu abre el plano.

## Costos (resumen)

- **Felipe 1.0:** 596 cr.
- **Felipe 2.0:** 579 cr al 5 oct 2026.
- **Total del proyecto:** ≈ **1,175 créditos de Higgsfield**.

Las voces de ElevenLabs se cobran aparte. Desglose en `docs/costos.md`.

## Herramientas

- **Higgsfield** (MCP):
  - `generate_video` con `model: hf_mult_replace_object` (Genjutsu);
  - `generate_image` con `nano_banana_pro`;
  - `media_upload` → PUT → `media_confirm` para subir archivos;
  - `get_cost` para cotizar;
  - `transactions` para el gasto.
- **ElevenLabs:** API speech-to-speech, modelo `eleven_multilingual_sts_v2`.
- **ffmpeg + Python (PIL, numpy, OpenCV):**
  - concatenar fuentes;
  - comparativas (el ffmpeg de esta Mac no tiene `drawtext`, así que las etiquetas son PNG hechos con PIL);
  - medir la luz cuadro por cuadro (`signalstats` YAVG);
  - detectar dónde empieza el habla (`silencedetect`);
  - borrar la silla (`quitar_silla*.py`);
  - corregir el cambio de lente (`corregir_lente.py`).

## Nota sobre el tamaño

El repositorio pesa unos **3.8 GB**. Los originales en chroma (`03_originales_chroma/`, 2.0 GB) incluyen 8 `.MOV` de más de 100 MB, que GitHub solo acepta con **Git LFS**. El `.gitattributes` ya manda a LFS todos los `.mp4`, `.MOV`, `.mov`, `.png`, `.jpg`, `.mp3` y `.wav`.
