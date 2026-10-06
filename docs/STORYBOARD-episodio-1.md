# Storyboard · Episodio 1 «El que nunca se decidió a invertir»

Artifact (con notas y aprobación por escena, `db`): https://claude.ai/artifact/QNx8bXAQrH5gKK92bAgQfR
Generador: `tools/build_storyboard.py` (escenas, luz, motor, subtítulo, sonido por clip). Estado: **pendiente de aprobación de David** (regla: nada de Versión 1 sin storyboard aprobado).

## Prueba de identidad + lipsync (clip 1) — 5-oct-2026
- Still B (Nano Banana Pro, refs: cuadro de David + ficha Felipe 2.0 ceja ok + hoja identidad + cuadro de luz dura de Rudy; prompt en 14 bloques) → `build/test/still_b.png`. Still A (luz plana) descartado.
- Kling 3.0 Motion Control 1080p (driver = clip 1 de David 0.9–6.54 s, mudo) → `clip1_kling_1080p.mp4` (1072×1936, 5.6 s). Identidad, luz dura, linterna, reloj a la derecha y anillo: ✅.
- Lipsync 2.0 sobre recorte de cara (`facecrop.py crop 540,440,620 --out 1280`) con la voz Jonas (STS) = 2,400 cr → `clip1_facecrop_lipsync2.mp4` → paste feather 48 → `clip1_felipe_final.mp4`; con 1 s de negro + encendido en 3 cuadros: `clip1_felipe_con_encendido.mp4`.
- Gasto de la prueba: Magnific 150 (stills) + 2,400 (lipsync) + 1,200 (música) = 3,750 · Higgsfield ≈ 15.
- Voz: `media/07_voz/voz_Jonas_sts_42s.mp3` (speech-to-speech Jonas `UEVUUEpjHAbzM7B6Byeu` sobre la toma completa de David, `remove_background_noise`).
- Música v1: `media/09_musica/horror_v1_elevenlabs.mp3` (60 s; dinámica cruda: −39 dB intro / −19 medio / −48 final ⇒ nivelar con `music_bed.py`).
