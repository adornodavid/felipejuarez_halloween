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
| c2 | d713ed32-f869-40cd-85c9-bf2b0ece71e1 | pad: bb3d7ea5-dcd1-4c0e-b0d6-e246196476fc (confirmar) | fc07f7d8… FALLÓ (driver 1.96 s) → relanzar con pad |
| c3a | fb39f270-1757-42db-94b8-0ed0f18cce96 | cdd8edd3-c525-444a-bd67-9982d3be3061 | c7611c1f-2039-45ca-9615-4577352a187c (en curso) |
| c3b | c143a015-ee53-4de5-a0f3-2dea3af0f893 | cfb4648b-4220-4cb0-aa0f-b798d81bbe1c | 582fa07d-ee2c-44ea-8c60-2194351d143d (en curso) |
| c4 | 7ad7488a-5cee-45de-b5a3-43ff2b81e64a | pad: 95ac932c-1262-45d3-b96c-d66e07b68289 (confirmar) | 3bbd5179… FALLÓ (driver 2.5 s) → relanzar con pad |
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
