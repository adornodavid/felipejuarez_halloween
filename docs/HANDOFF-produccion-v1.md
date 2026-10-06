# HANDOFF · producción Versión 1 (5-oct-2026 noche) — retomar con `FELIPE-JUAREZ-MIEDO-A-INVERTIR`

Storyboard **aprobado 11/11** por David (artifact https://claude.ai/artifact/QNx8bXAQrH5gKK92bAgQfR). Nota única en clip 1: «el audio al principio se escucha un poco IA y entrecortado» → **causa:** `remove_background_noise=true` en el speech-to-speech recortaba ataques (huecos −50 dB entre palabras). **Fix hecho:** voz **v3** (`media/07_voz/voz_Jonas_sts_v3_42s.mp3`, sin supresión, stability 0.6 / similarity 0.85) + room tone rosa −50 dB mezclado por clip (`build/test/voz_c*.wav`). `build/test/clip1_felipe_con_encendido_v3.mp4` ya usa v3 (pendiente que David lo oiga).

## Cortes reales de la toma de David (720×1248, 24 fps, 42.54 s) — scene cuts
c1 0–6.54 · c2 6.54–8.46 (perfil) · c3 8.46–19.79 (partido: c3a 8.46–13.0, c3b 13.0–19.79) · c4 19.79–22.29 (perfil, «…que sí tomó la decisión») · c5 22.29–26.54 («¿Y el terreno? …duplicado su valor») · c6 26.54–28.08 (mano, sin swap) · c7 28.08–31.58 («Lo que da miedo…») · negro 31.58–32.58 · c8 32.58–42.54 (partido: c8a 32.58–37.5 sentado→se levanta, c8b 37.5–42.54 CTA).
Drivers mudos en `build/drivers/` (c2/c4 también `_pad` a 3.58 s: Kling falló con <2.5 s).

## Stills aprobados (Nano Banana Pro, `build/stills/`)
c1 `build/test/still_b.png` · c2 `s_c2_b.png` · c3a `s_c3a_r1.png` · c3b `s_c3b.png` · c4 `s_c4_a.png` · c5 `s_c5_r2.png` · c7 `s_c7.png` · c8a `s_c8a_b.png` (sentado sillón showroom) · c8b `s_c8b_a.png` (de pie). Fallaron por cara distinta: s_c2_a, s_c4_b, s_c3a (v1), s_c5 (v1), s_c3a_r2 ok también, s_c5_r1 ✗, s_c8a_a ✗, s_c8b_b ok.
Lección: Nano Banana cambia la cara 1 de cada 3 veces aunque la ficha esté en las referencias → siempre `count=2` y poner un still YA aprobado como imagen 2.

## Higgsfield (Kling 3.0 Motion Control 1080p, `scene_control=image`)
| clip | image media_id | driver media_id | job |
|---|---|---|---|
| c1 | c0199d7f-091d-430b-9f76-d0dd515651b8 | f0020365-aa87-49a6-9075-a83d2627d96c | ✅ e02d4c8c-491d-4c2d-8a32-0529f3e1a41b → `build/test/clip1_kling_1080p.mp4` |
| c2 | d713ed32-f869-40cd-85c9-bf2b0ece71e1 | pad: bb3d7ea5-dcd1-4c0e-b0d6-e246196476fc (confirmar) | ✅ relanzado con pad: **7b579e4d-9079-415e-9e60-0b6524ee5868** (en curso); recortar resultado a 1.96 s |
| c3a | fb39f270-1757-42db-94b8-0ed0f18cce96 | cdd8edd3-c525-444a-bd67-9982d3be3061 | c7611c1f-2039-45ca-9615-4577352a187c (en curso) |
| c3b | c143a015-ee53-4de5-a0f3-2dea3af0f893 | cfb4648b-4220-4cb0-aa0f-b798d81bbe1c | 582fa07d-ee2c-44ea-8c60-2194351d143d (en curso) |
| c4 | 7ad7488a-5cee-45de-b5a3-43ff2b81e64a | pad: 95ac932c-1262-45d3-b96c-d66e07b68289 (confirmar) | ✅ relanzado con pad: **1574879a-cbef-48af-bc6d-5085d5132cca** (en curso); recortar resultado a 2.5 s |
| c5 | 048f690f-785d-46d2-934a-6609f04718a6 | 8c305344-c075-469d-87b0-9c3ece239ff6 | 58f18862-ded7-40d8-930b-96136fe4faf2 (en curso) |
| c7 | c89c5a9f-772c-49d5-b0eb-d1e2b9300f84 | 91c5af3b-7d76-47f0-8e23-7ba458c11227 | 64c5c1f2-4b86-4c53-b3e8-2610a4362ec3 (en curso) |
| c8a | 0d4523f0-68c4-4d7c-8fe1-96cf5fa6ef2b | a5032d12-4eb9-484b-976f-72dbdcead4c5 | 2b0b9288-eb75-4cb8-a0a3-7888aecb2ded (en curso) |
| c8b | 196edb46-27be-4eab-98dc-bdf78fd1ee36 | bff83251-e79f-4532-afde-be3eda14b90e | c4c0957f-523b-4a14-b65a-e6fac8da4aab (en curso) |
Resultados con `jobs_wait` → `result_url` → descargar a `build/kling/<clip>_kling_1080p.mp4`. Salida 1072×1936 30 fps. Para c2/c4 recortar el resultado a la duración original (1.96 / 2.5 s).

## Magnific (Lipsync 2.0, ≈420 cr/s)
Voces por clip ya subidas (creation ids): c2 `KLRN40Ukqp` · c3a `aF7gs3wfSh` · c3b `tCgjr9ymZJ` · c4 `6A8dpuriJO` · c5 `s7YAZd5l8e` · c7 `eI1bHwDdqL` · c8a `TdquCleVNR` · c8b `ovL1KPE829` (c1 v1: `ovL1mlq829`; para c1 rehacer con v3 `build/test/voz_jonas_v3_clip1_roomtone.wav`).
Por clip: `facecrop.py crop <kling> <crop> cx,cy,size --out 1280` (c1 usó 540,440,620; localizar cara con numpy del venv `tr-regina-castelo/.venv`) → subir recorte (`creations_request_upload` mp4 + PUT + finalize) → `video_speak mode=lipsync-2.0 videoUrl=<crop id> audioUrl=<voz id>` → `facecrop.py paste … --feather 48` → pegar voz. c8a cara chica: lipsync sobre el clip entero o recorte mayor. c6 = mano real de David keyeada sobre negro (sin IA).

## Montaje (pendiente, seguir el storyboard aprobado)
Intro Rudy (recortar 10→6 s; archivo en Drive `05_animacion_inicio`, NO descargado: gdown falla por permisos, pedir a David acceso directo o link) → c1 con 1 s negro + encendido 3 cuadros → c2…c7 → apagón 2.5 s negro → c8a con luces subiendo 0.6 s → c8b → outro negro logo TR + terraregia.com 3 s. Música `media/09_musica/horror_v1_elevenlabs.mp3` nivelada con `tools/music_bed.py` (sin ducking; silencio en el apagón; sube al final). SFX: cerillo, clic ON/OFF, tic reloj, luces. Subtítulos cine (`subs_v2.py` con tinta por palabra, estilo una línea serif). QA: hoja de contacto de TODAS las frases + tira de labios por clip. Entrega 1080p + 720p a Drive `Terra Regia - Felipe Juarez Miedo a Invertir/02 Version 1/`.

Gasto acumulado 5-oct: Magnific ≈ 150+2,400+1,200+900+300 = ~4,950 cr · Higgsfield ≈ 120. Saldos al cierre ≈ Magnific 106,900 · Higgsfield 4,190.

## Sesión 6-oct (retomada) — estado
- Kling 8/8 completados → `build/kling/<clip>_kling_1080p.mp4` (c2/c4 recortados: `_trim.mp4` 1.96 / 2.5 s). Hoja de contacto `build/qa/kling_contact_all.jpg` ✅ identidad/luz/props.
- Cajas de recorte de cara (coords del Kling 1072×1936) en `build/crops/boxes.txt`; recortes `build/crops/<clip>_crop.mp4` (1280²).
- Magnific: recortes subidos c1 `79MceqnJAL` · c2 `tCgjwWNmZJ` · c3a `JND0dKzOq4` · c3b `p8kqx2xehw` · c4 `1l2izfVr4r` · c5 `yieVBjfPW9` · c7 `UPTYDkhwny` · c8a `gOczVKfSXO` · c8b `w4VWpjY7EI`; voz c1 v3 `ovL1gDx829`.
- Lipsync 2.0 lanzados (16,000 cr): c1 `O6pTB9nynm` · c2 `TdqukeKVNR` · c3a `eI1bLIKdqL` · c3b `VXbQ1BdMMU` · c4 `yieVo3sPW9` · c5 `ovL1SfP829` · c7 `5j39AlZKxe` · c8a `XmxKlfrBfo` · c8b `DoKHxhHpcl` → bajar a `build/lipsync/<clip>_crop_ls.mp4` → `facecrop.py paste` con la caja de boxes.txt.
- **Crudos 4K + intro cerillo:** Rudy los puso en Drive «Campaña Terra Regia / Campaña Miedo a Invertir / terraregia-miedo-a-invertir-repo» (hay 2 copias; la de las 00:33 está VACÍA y es la que David zipeó). Copiados del lado del servidor, ya a nombre de David, a `Proyectos Claude Code/Terra Regia - Felipe Juarez Miedo a Invertir/00 Crudos 4K chroma (Rudy)` (11 MOV IMG_0303…0322 + 4 Javo_IMG_85xx) y `00 Intro cerillo y referencias (Rudy)` (intro_le-temes-a-invertir_story.mp4 + Felipe Juarez 2.0). Google Drive for desktop NO corría en la Mac (por eso nada sincronizaba); abierto 6-oct.
- ✅ Lipsync 9/9 bajados y pegados → `build/clips/<clip>_felipe.mp4` (con voz). c6 = mano real keyeada `build/clips/c6_mano_mudo.mp4` (`chromakey 0x1fa33a`). QA: `build/qa/lips_contact.jpg`, `build/qa/crops_contact.jpg`.
- ✅ Montaje: `tools/montaje_v1.py [intro.mp4]` → `build/v1/v1_cuerpo_sin_musica.mp4` + `build/v1/timeline.json` (offsets por clip; c8a/c8b +1.55 s por el apagón de 2.5 s). Outro = TR_white + terraregia.com 3 s.
- ✅ Subtítulos de cine: `tools/subs_cine.py` (Minion Pro 58, blanco 92 %, palabra que suena en ámbar #F2C14E, 16 frases de una línea, tinta oscura automática sobre fondo claro; palabras de `david_words.json` + offset del timeline). QA `build/qa/subs_contact.jpg`.
- ✅ Música: `tools/musica_v1.py` (RMS parejo, 0.55 intro · 0.32→0.42 cuerpo · 0 apagón · 0.22 showroom · 0.75 tras «terraregia.com»). → **`build/v1/V1_preview_sin_intro.mp4` (47.1 s)**.
- ▶️ FALTA: intro cerillo (en Drive, Google Drive for desktop con 6 días de atraso; o bajar por Chrome) → `python tools/montaje_v1.py <intro.mp4>` → subs → música → entregar a Drive `02 Version 1`. Después: SFX (clic ON/OFF, tic, luces), grade de c6 (luz de linterna), oír la voz v3 de c1.

## DEMO 2 (6-oct, mañana) — correcciones de David a la V1
Errores señalados: (1) faltaba la intro cerillo; (2) c1 debe arrancar a oscuras y ENCENDER la linterna; (3) de ~25 s en adelante la identidad se perdió (c7, c8a, c8b eran OTRA PERSONA: los stills s_c7/s_c8b_a ya venían con otra cara); (4) al final la linterna desaparecía: debe dejarla en una mesa; (5) gesto final de manos «presentando» con el texto terraregia.com completándose; (6) luz SOLO de la linterna en todo lo oscuro aunque cambie el ángulo; (7) lipsync mejorable; (8) showroom con mobiliario inventado → usar las fotos reales (`media/06_personaje/refs_showroom_real/`, copiadas de Downloads «show room Terra Regia»).
Hecho:
- Intro: `media/05_intro/intro_le-temes-a-invertir_story.mp4` (10 s, 1080×1920 24 fps; bajada por Chrome) → se usa 0–6 s.
- c1 encendido: `tools/encendido.py` → `build/clips/c1_felipe_encendido.mp4` (1.0 s a oscuras al 3 %, clic en 0.75 s con destello/rebote, luz plena en 4 cuadros; clic sintético + room tone). Nota: el 720p de Rudy YA empieza con la linterna encendida (no hay acción real en el crudo recortado; revisar los 4K cuando bajen).
- c7 v2: Kling MC con el STILL APROBADO DE c1 (`still_b`, media c0199d7f) + driver c7 → `build/kling/c7_v2_kling_1080p.mp4` (identidad ✅) → crop 540,440,620 → Lipsync 2.0 `O6pv1MXynm` → `build/clips/c7_felipe_v2.mp4`. A/B lipsync: Veed Sync 2.0 `P3dfxXb42C` (560 cr) vs Lipsync 2.0 (1,200 cr) → `build/qa/AB_lipsync_c7_izqLipsync2_derVeedSync2.mp4` (David decide).
- Toma 8 re-partida: c8a2 = 32.58–34.00 (deja la linterna en la mesa; driver `c8a2_mudo_pad_flip.mp4` ESPEJEADO para que alcance la mesa que en la foto real queda a la derecha; media 86f071bf) · c8b2 = 34.00–42.54 (de pie, CTA; media 719e2b43).
- Stills nuevos sobre FOTO REAL (plate 9:16 de `…MAY24-02.jpg`): c8a2 `build/stills/s_c8a2_b.png` (sentado en el sillón gris real, linterna hacia la mesa redonda real; media 75b752d5) · c8b2 `build/stills/s_c8b2_a_medium.png` (recorte plano medio del still A; media b18994db). Receta Nano Banana Pro: refs = [plate real, ficha ceja ok 1bb10755, still_b c0199d7f, cuadro de pose] + «use image 1 EXACTLY as background, do not add/move/remove furniture».
- Kling c8b2 job 44e21f84 · c8a2 job e349e74d FALLÓ (pro) → relanzado std 32fff249.
- Voces: `build/test/voz_c8b2.wav` (34.00–42.54 + room tone; Magnific `yieasg8PW9`) · `voz_c8a2.wav` solo room tone. Voz v3 verificada alineada con `david_words.json` (±0.02 s).
- Montaje DEMO 2: `tools/montaje_v2.py media/05_intro/intro_le-temes-a-invertir_story.mp4` → `build/v2/` · subtítulos `tools/subs_cine_v2.py` (+ título grande terraregia.com que se completa con el gesto, pico en 41.8 s del crudo) · música `tools/musica_v1.py` (lee build/v1/timeline.json → copiar/apuntar a build/v2).
Pendiente tras DEMO 2: luz de linterna en c6 (mano real está con luz de foro), SFX (clic/tic/luces), 4K crudos.
- ✅ **DEMO 2 RENDERIZADO: `build/v2/DEMO2_FelipeJuarez_MiedoAInvertir.mp4` (53.0 s, −16.7 LUFS).** Lipsync 2.0 en todo (David eligió Lipsync 2.0 sobre Veed Sync en el A/B de c7).
  Toma 8 final: c8a2 = Kling std de `s_c8a2_b` + driver espejeado, primeros 2.30 s (32.58–34.88), lipsync `3ztqHB0REY` · c8b2 = Kling v1 de `s_c8b2_a_medium` (b18994db) desde 0.9 s con ZOOM dinámico que cancela el zoom-out de Kling (`build/kling/c8b2_zoom_1080p.mp4`, 34.90–42.54), lipsync `yiefac2PW9` (caja 630,717,637). El Kling v2 con el still completo (c5fdf98d) INVENTÓ una lámpara colgante y plantas → descartado.
  c6 = mano real con grade de linterna (`c6_mano_linterna.mp4`, máscara radial cálida ×numpy; el `blend` de ffmpeg con máscara RGB salía VERDE).
  Render de subtítulos ahora por numpy (`subs_cine_v2.py`, 1.6 k cuadros en ~2 min; el grafo ffmpeg con ~100 overlays tardaba >10 min).
  Cajas de cara en `build/crops/boxes.txt` (c8b2z, c8a2u). Pendiente: la linterna NO queda visible sobre la mesa en c8b (Kling la desaparece) → opción: componer la linterna real sobre la mesa en post.

## V3 (6-oct tarde) — feedback de David al DEMO 2 y nueva receta «cabeza sobre still»
David: (1) luz incorrecta; (2) aparece el MICRÓFONO en vez de la linterna; (3) en los perfiles (c2/c4) Felipe «voltea a la izquierda» en vez de un perfil; (4) revisar toma 8. **Lipsync 2.0 confirmado** (Veed descartado).
Causa raíz: David grabó el croma con un micrófono de bola; Kling Motion Control copia la geometría del crudo y devuelve el micro (c2, c3a, c4, c7); c1/c5 conservaron la linterna por azar. c2/c4: los stills eran 3/4 con hombros de frente, no perfil 90°. c8a2: sentadilla, cara chica; c8b2: identidad deriva de 4 s en adelante.
**Receta V3 (piloto c3a ✅):** driver recortado a SOLO CABEZA (720×560 desde y=30; filas ≥572 oscuras → verde) `build/v3/c3a_head_driver.mp4` (HF media a1bd0d67) + still recortado alineado por la cara `build/v3/c3a_head_still.png` (crop 69,199,1382,1075 de s_c3a_r1; HF media c5ae8261) → Kling MC 1080p job 6c286804 → `build/v3/c3a_head_kling.mp4` (1600×1296) → Magnific upload `aF7GE3IfSh` → Lipsync 2.0 `bxiMkXG5Y2` (2,000 cr) → `build/lipsync/c3a_head_ls.mp4` → `tools/head_comp.py still cabeza out --place 1433,1161,28,262 --cut 1180,1230 --audio voz --light 770,1600,900,2100,0.5` → **`build/clips/c3a_felipe_v3.mp4`**.
Claves: alinear barba del Kling con la del still (medir fondo de barba por luminancia; Kling encoge la cara ~8 % y la sube ~50 px); rampa de máscara DENTRO de la barba (no en el cuello) para que no haya doble línea; el negro del Kling tapa el pelo del still. Pendiente aprobación de David → lote c1 c3b c5 c7 (misma receta) · c2/c4 stills de perfil 90° nuevos · toma 8.
