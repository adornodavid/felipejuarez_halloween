# Felipe Juárez · Terra Regia «Miedo a invertir» (Halloween 2026)

Repo de producción del video **Episodio 1 — «El que nunca se decidió a invertir»** (vertical 9:16, ≈55 s con intro y outro). Avatar IA **Felipe Juárez** sobre la actuación real de **David Adorno** en croma. Hereda la receta y los aprendizajes de **Regina Torres / Castelo** (repo `adornodavid/regina_torres_terraregia`, carpeta `videos-ia/`, skill `regina-video-ia`).

## Concepto
Cuarto negro. Felipe enciende una linterna desde abajo (solo se ve su cara, luz dura) y cuenta la historia de alguien que «lo pensó» y perdió el terreno. Giro: «Lo que da miedo es dejar pasar oportunidades.» Se levanta, el cuarto se ilumina: es el showroom de Terra Regia. CTA: «En Terra Regia tenemos el terreno donde tu dinero sí crece. Conoce más en terraregia.com.» Antes: intro animada «¿Le temes a invertir?» (cerillo, 10 s). Después: outro logo TR + terraregia.com.

## Decisiones de David (5-oct-2026)
- Modelo en croma = David. Swap de personaje completo a **Felipe Juárez 2.0** (ficha `media/06_personaje/felipe2_3_vistas_faceless_ceja_arreglo.png` + hoja de identidad `hoja_referencia_personaje_identidad.jpeg`). Outfit: camisa verde `#152A23` abierta, playera blanca, cargo negro, reloj café muñeca izquierda (derecha de pantalla), anillo se queda.
- **Voz: Jonas Mexican `UEVUUEpjHAbzM7B6Byeu`** (ElevenLabs, speech-to-speech sobre la voz de David: conserva tiempos).
- Toma 8 (showroom) se parte en dos planos para que la cara mida ≥150 px.
- Mejoras pedidas sobre la referencia de Rudy: lipsync, voz, «se ve muy IA», subtítulos cinematográficos (no real estate), outro con logo TR + terraregia.com, música de miedo.
- **Regla: storyboard aprobado antes de la Versión 1.** Luego por clips: proporciones, animación de la linterna, intro, outro, lipsync, cambios de toma.

## Receta (de Regina, adaptada)
Still de Felipe en el cuadro de David (Nano Banana Pro con ficha + referencia de luz dura `ref_luz_clip1_v3.png`) → **Kling 3.0 Motion Control** con el crudo real como driver → **Lipsync 2.0** en recorte de cara con la voz Jonas → montaje ffmpeg/PIL (`tools/`), música sin ducking (cama RMS, `music_bed.py` de Castelo), subtítulos por palabra (`subs_v2.py`, tinta por palabra). Descartados por experiencia: Genjutsu para identidad/boca, OmniHuman, Seedance modify.

## Estructura
```
docs/GUION-definitivo-episodio-1.md   ← lo que David DIJO (manda) vs guion escrito; tiempos por frase; mapa de 8 clips
docs/STORYBOARD-episodio-1.md         ← storyboard aprobado (y link al artifact con notas)
docs/rudy-repo/                       ← docs del repo de Rudy/Liz (receta Genjutsu, costos, ids, prompts, notas) — referencia histórica
tools_download_drive.py               ← baja TODO el material de Drive a media/ (ids incluidos)
tools/                                ← scripts de producción (comp, facecrop, subs, música, build)
media/ (ignorado)                     ← 01 crudos 4K · 02 otro ángulo · 03 cortes 720p · 04 referencia · 05 intro · 06 personaje · 07 voz · 08 genjutsu de Rudy
```
Drive del cliente: carpeta `terraregia-miedo-a-invertir-repo` (rudycomunicacion) + `Personaje/` (David).
