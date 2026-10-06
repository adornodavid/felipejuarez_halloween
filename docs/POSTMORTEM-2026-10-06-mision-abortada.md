# POSTMORTEM — «Miedo a invertir» Episodio 1 (Felipe Juárez) — MISIÓN ABORTADA 6-oct-2026

**Decisión de David (6-oct, ~18:00):** abortar. El video NO se logró. Se retomará más adelante desde cero o desde lo rescatable que se lista abajo.

## Qué se intentó (cronología del 6-oct)
1. **V1 / DEMO 2** (mañana): Kling 3.0 Motion Control sobre el croma de David + Lipsync 2.0 + montaje. David lo rechazó: micrófono en vez de linterna, luz plana, perfiles «volteando» en vez de perfil, toma 8 inservible, avatar cambiaba.
2. **V3 «cabeza sobre still»** (tarde): driver recortado a cabeza + still con cuerpo fijo (`tools/head_comp.py`). Rechazado: mentón cortado, cuerpo muerto, «no respeta el storyboard».
3. **V3 «Genjutsu replace-object»**: Kling de cuerpo entero + reemplazo micro→linterna. Tomas 1-3 aprobadas «en estructura» pero «se ve muy IA/falso», lipsync flojo, voz «acartonada/robotizada».
4. **Tomas 4-7 v2/v3**: rechazadas dos veces (c4 era otro avatar; c6 mostraba las manos reales de David; audio cosido con hueco).
5. **Toma 8 v3/v4**: rechazada (audio desfasado 0.9 s por un wav mal recortado; avatar «otro»; no seguía el crudo). La v4 (driver completo + 4K + zoom + lipsync) quedó renderizada en `build/v3/PREVIEW_V3_completo.mp4` pero David abortó antes de evaluarla.

## Por qué no se logró (causas de fondo, no excusas)
- **El prop del croma era un micrófono.** Kling Motion Control copia la geometría del crudo; cada clip requería un reemplazo posterior (Genjutsu) que añade una capa de IA y de degradación. El material debió grabarse con la linterna real (o sin prop).
- **Identidad inestable a lo largo de 10 clips.** Cada still nuevo (Nano Banana) tenía ~1/3 de probabilidad de cambiar la cara; en planos abiertos (toma 8) la cara es tan chica que la identidad y el lipsync no se sostienen. Reusar un único still aprobado por ángulo fue la única mitigación que funcionó.
- **Lipsync 2.0 no alcanza el estándar de David** en esta cadena (crudo → Kling → swap → lipsync): la boca sigue el audio pero se percibe «IA».
- **La voz** (ElevenLabs speech-to-speech Jonas v3, stability 0.6) suena acartonada. No se iteró porque la llave de ElevenLabs no está en el repo.
- **Proceso**: iteré rápido sobre previews en vez de entregar una toma perfecta y esperar. Cada preview con un error (manos reales, otro avatar, hueco de audio, desfase) quemó confianza. El desfase de la toma 8 fue un error mío de recorte de wav (34.90 vs 34.00).

## Qué SÍ sirve para el siguiente intento
- `build/clips/c1_felipe_encendido.mp4`, `c2_felipe_v3.mp4`, `c3a_felipe_v3.mp4`, `c3b_felipe_v3.mp4` (tomas 1-3 aprobadas en estructura).
- Stills aprobados: `build/test/still_b.png` (c1, identidad y luz), `build/stills/s_c2_p1.png` (perfil 90°, usar para c2 Y c4), `s_c3a_r1.png`, `s_c5_r2.png`, `s_c8a2_b.png` (sentado en showroom real).
- Herramientas probadas: `tools/facecrop.py`, `tools/zoom_path.py`, `tools/montaje_v3.py` (voz continua por tramos), `tools/subs_cine_v2.py`, `tools/musica_v1.py`, `tools/encendido.py`.
- Lecciones de pipeline: Genjutsu replace-object ≥4 s y conserva lipsync; mismo still por ángulo; voz continua, nunca clip a clip; Kling MC re-encuadra al driver (plano abierto = cara chica).
- Bitácora completa de ids (Higgsfield/Magnific) en `docs/PLAN-V3-por-tomas.md` y `docs/HANDOFF-produccion-v1.md`.

## Recomendación para el reintento (una sola ruta)
1. **Regrabar el croma con la linterna REAL encendida** (o pedirle a Rudy el 4K con linterna si existe). Elimina el reemplazo de prop y la mitad de la degradación.
2. Grabar la toma 8 en plano medio fijo (sin que la cámara abra): la cara grande sostiene identidad y lipsync.
3. Un solo still maestro por ángulo (frontal, perfil, showroom) aprobado por David ANTES de animar; cero stills nuevos durante producción.
4. Voz: iterar el STS con David oyendo 3 variantes antes de cualquier lipsync; conseguir la llave de ElevenLabs.
5. Entregar UNA toma terminada al 100 % (con subs, música y grade) y no avanzar hasta aprobación.

## Gasto del 6-oct (aprox.)
Magnific ≈ 39,000 cr (lipsyncs ×9 + 2,000 + 800 + 1,200 ×2 + 3,600 ×2 + 4,000) · Higgsfield ≈ 310 cr (Kling MC ×8, Genjutsu ×6, Nano Banana ×4, i2v ×4, Topaz 4K ×1). Saldos al cierre: Magnific ~46,000 · Higgsfield ~3,800.
