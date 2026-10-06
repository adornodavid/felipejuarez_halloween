# V3 por tomas — feedback de David al DEMO 2 (6-oct) y plan de aprobación toma por toma

Regla de trabajo: **una toma a la vez, David autoriza, luego se junta**. El cuerpo NUNCA fijo: se conserva la actuación completa de David (Kling MC de cuerpo entero). El micrófono del croma se reemplaza por la linterna con Genjutsu «replace object» (35 cr HF/clip) sobre el clip ya con lipsync. Luz: todo oscuro, solo lo que alumbra la linterna (grade radial en post).

| Toma | Clip(s) | Tiempo DEMO 2 | Veredicto David | Qué hacer |
|---|---|---|---|---|
| 1 | c1 | 6.0–12.6 s | ✅ bien (lipsync mejorable después) | Dejar; refinar lipsync al final |
| 2 | c2 (perfil) | 12.6–14.5 | ✗ micrófono · «voltea a la izquierda» en vez de PERFIL | Still nuevo de perfil 90° (cámara al costado, como el crudo) → Kling MC → swap micro→linterna → lipsync |
| 3 | c3a + c3b | 14.5–25.8 | (micro + mucha luz) | Swap micro→linterna sobre los clips con lipsync + grade oscuro |
| 4 | c4 (perfil) | 25.8–28.3 | ✗ micrófono · gira · cambió el avatar | Igual que toma 2 |
| 5 | c5 | 28.3–32.6 | ✅ linterna y avatar correctos | Dejar; grade oscuro |
| 6 | c6 (mano) | 32.6–34.1 | ✗ se ve el croma ORIGINAL con el micro, no el avatar con la linterna | Swap micro→linterna sobre la mano real keyeada (o still de manos+linterna animado) |
| 7 | c7 | 34.1–37.6 | ✗ micrófono | Swap micro→linterna sobre c7_felipe_v2 (identidad ya correcta) + grade |
| 8 | c8a2 + c8b2 + outro | 40.1–53 | ✗ todo: silla se mueve, mal parado, no se ve qué hace con la linterna, cambia el avatar | Rehacer: dejar la linterna en la mesa visible, levantarse estable, plano medio CTA con identidad fija |

Gate: prueba Genjutsu en c3a (job 837feea3). Si el swap respeta cara y manos → tomas 2, 3, 4, 6, 7 por esa vía. Si no → inpainting por cuadro (Magnific retouch) o still+Kling con driver sin micro.

## Bitácora de ids (6-oct tarde)
- Genjutsu replace-object c3a ✅ job 837feea3 (entrada: c3a_mudo con lipsync, media 7e113646; ref linterna `build/v3/ref_linterna.png` media 9b713e99). Resultado 1072×1934 24 fps 4.375 s (recorta ~0.16 s al final → tpad). Lipsync SOBREVIVE al swap. → `build/clips/c3a_felipe_v3.mp4`.
- Genjutsu c3b job 1b44190b (media b6232ca9). c7 (media a394d5d1) y c6 (media 21db555f) dieron 422 mientras otro Genjutsu corría ⇒ **un Genjutsu a la vez**; relanzar al terminar c3b.
- Stills de perfil (Nano Banana 2.1, refs: cuadro real c2 d536d38c / c4 9120699b + ficha ceja ok c8b21869 + outfit perfil 5cebec45 + still_b c0199d7f): c2 → jobs 23b7e888 ✅(elegido) / 985f51b7 · c4 → 1d59536f ✅(elegido) / 04c78ea5. Archivos `build/stills/s_c2_p1.png s_c2_p2.png s_c4_p1.png s_c4_p2.png`.
- Kling MC c2: still 23b7e888 + driver pad bb3d7ea5 → job 3ac5af33 · c4: still 1d59536f + driver pad 95ac932c → job 331b90a6. Luego: recortar a 1.96/2.5 s → lipsync (voces Magnific c2 `KLRN40Ukqp`, c4 `6A8dpuriJO`) → Genjutsu swap micro→linterna.
- ⚠️ Genjutsu exige clips ≥ 4 s (los 422 de c7 3.5 s y c6 1.5 s): c7 → `c7_pad.mp4` 4.2 s (media fabe06ea, job a4d95ab3) · c6 → `c6_boomerang.mp4` 4.63 s (media fa6f41c4, job f65770d8). Recortar al final.
- Kling c2 (job 3ac5af33) CONSERVÓ la linterna (no necesita swap) → `c2_v3_kling_trim.mp4` 1.96 s → Magnific `yiebzRtPW9` → Lipsync 2.0 `jUzh4Y0LD0` (800 cr). Kling c4 (job 331b90a6) trae micro → pad 4.27 s (media 76b6a610) → Genjutsu job 93646456 → recortar 2.5 s → lipsync.
- c3b swap ✅ → `build/clips/c3b_felipe_v3.mp4` (6.79 s).
- ✅ **David 6-oct ~17:10: tomas 1-3 APROBADAS en estructura** (`build/v3/PREVIEW_tomas_1-3.mp4`). Notas para pasada final: «se ve muy IA/falso», lipsync aún mejorable, **voz acartonada/robotizada** (regenerar STS con menos stability / más style, o limpiar con Magnific). Movimientos y gestos ✅.
- c6 swap ✅ (job f65770d8, boomerang) → `build/clips/c6_mano_v3_mudo.mp4` 1.53 s (linterna plateada con ranuras; revisar que case con la negra de las otras tomas).
- c7 swap ✅ (job a4d95ab3, pad 4.2→recorte 3.5 s) → build/clips/c7_felipe_v3.mp4
